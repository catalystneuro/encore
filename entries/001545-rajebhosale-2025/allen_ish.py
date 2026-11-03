"""Allen Developing Mouse Brain Atlas ISH at E18.5, for figs9c-embryonic-sgc-genes.

The claims file says the paper read public Allen E18.5 ISH images for Penk, Scg2, Nrg1 and Cit
and names no experiment ids; any E18.5 series of the gene is a reading. The atlas holds one
E18.5 series per gene (found by query, product 3, Developing Mouse Brain). Everything is read
from the Allen API (https://api.brain-map.org/api/v2) into memory; nothing is written to disk.

Locating the dentate gyrus. The E18.5 reference annotation (reference space 5,
E18pt5_DevMouse2012_annotation.zip, well-known file 263212128) is coarse: its smallest unit
here is the medial pallium (hippocampal allocortex, structure 16114), and neither the dentate
gyrus nor its granule cell layer is drawn, in the 3D annotation or in the annotated atlas
plates. So the medial pallium is cropped from the annotation, and the dentate gyrus inside it is
located by eye on one section (an assumption, said in the notebook) and carried to the other
series through the atlas's own alignment (the image_to_reference and reference_to_image
services). Crop sizes and the downsampling are display choices.
"""

from __future__ import annotations

import io
import zipfile
from concurrent.futures import ThreadPoolExecutor

import numpy as np
import requests
from PIL import ImageFile

API = "https://api.brain-map.org/api/v2"
REFERENCE_SPACE = 5       # E18.5 Brain
ANNOTATION_FILE = 263212128
MPALL = 16114             # medial pallium (hippocampal allocortex), developing mouse ontology


def query(criteria: str) -> list[dict]:
    r = requests.get(f"{API}/data/query.json", params=dict(criteria=criteria), timeout=120).json()
    if not r.get("success"):
        raise RuntimeError(f"Allen API query failed: {r.get('msg')}")
    return r["msg"]


def e185_series(gene: str) -> list[dict]:
    """Every Developing Mouse Brain ISH series of a gene at E18.5."""
    return query(f"model::SectionDataSet,rma::criteria,products[id$eq3],genes[acronym$eq'{gene}'],"
                 f"specimen(donor(age[name$eq'E18.5'])),rma::include,plane_of_section,rma::options[num_rows$eqall]")


def section_images(series_id: int) -> dict[int, dict]:
    return {s["id"]: s for s in query(f"model::SectionImage,rma::criteria,[data_set_id$eq{series_id}],"
                                      f"rma::options[num_rows$eqall]")}


def mpall_mask() -> np.ndarray:
    """Medial pallium voxels of the E18.5 annotation, indexed (ML, DV, AP) at 20, 16, 16 um."""
    raw = requests.get(f"{API}/well_known_file_download/{ANNOTATION_FILE}", timeout=300).content
    z = zipfile.ZipFile(io.BytesIO(raw))
    a = np.frombuffer(z.read("annotation.raw"), dtype=np.uint32).reshape(278, 370, 581)
    return a == MPALL


def image_to_reference(image_id: int, x: float, y: float) -> dict:
    return requests.get(f"{API}/image_to_reference/{image_id}.json", params=dict(x=x, y=y),
                        timeout=60).json()["msg"]["image_to_reference"]


def reference_to_image(x: float, y: float, z: float, series_id: int) -> dict:
    return requests.get(f"{API}/reference_to_image/{REFERENCE_SPACE}.json",
                        params=dict(x=x, y=y, z=z, section_data_set_ids=series_id), timeout=60).json()["msg"][0]["image_sync"]


def mpall_area(series_id: int, mask: np.ndarray) -> list[dict]:
    """Per section: its medial-lateral level in the reference and the medial pallium voxels there."""
    secs = sorted(section_images(series_id).values(), key=lambda s: s["section_number"])

    def one(s):
        ref = image_to_reference(s["id"], s["width"] / 2, s["height"] / 2)
        zi = int(round((ref["z"] + 160) / 20))  # annotation offset -160 um, spacing 20 um
        area = int(mask[zi].sum()) if 0 <= zi < mask.shape[0] else 0
        return dict(image_id=s["id"], section=s["section_number"], ml_um=ref["z"], mpall_voxels=area)

    with ThreadPoolExecutor(8) as ex:
        return list(ex.map(one, secs))


def crop(image: dict, cx: float, cy: float, half_um: tuple[float, float], downsample: int, view: str | None = None):
    """A crop centred on (cx, cy), in the section image's own pixel coordinates (1 um pixels at
    full resolution), returned as an RGB array; view='expression' gives the atlas's expression mask."""
    p = dict(downsample=downsample, quality=85, left=int(image["x"] + cx - half_um[0]),
             top=int(image["y"] + cy - half_um[1]), width=int(2 * half_um[0]), height=int(2 * half_um[1]))
    if view:
        p["view"] = view
    r = requests.get(f"{API}/image_download/{image['id']}", params=p, timeout=120)
    r.raise_for_status()
    # The ISH section images are this claim's data, streamed from the atlas and decoded in memory.
    parser = ImageFile.Parser()
    parser.feed(r.content)
    return np.asarray(parser.close().convert("RGB"))


def structure_density(series_id: int, structure_ids: list[int]) -> dict[str, float]:
    """The atlas's expression density (expressing pixels over all pixels) per structure."""
    rows = query(f"model::StructureUnionize,rma::criteria,section_data_set[id$eq{series_id}],"
                 f"structure[id$in{','.join(map(str, structure_ids))}],rma::include,structure,rma::options[num_rows$eqall]")
    return {r["structure"]["acronym"]: r["expression_density"] for r in rows}
