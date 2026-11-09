"""Loading, segmentation and scoring for the mouse TEM images of dandiset 001436.

Zaimi, Wabartha, Herman, Antonsanti, Perone & Cohen-Adad (2018), AxonDeepSeg, Scientific
Reports 8, 3816, doi:10.1038/s41598-018-22181-4.

The dandiset is a BIDS microscopy dataset (no NWB): one 8-bit grey png per TEM image under
`sub-<mouse>/micr/`, a sidecar `sub-<mouse>_TEM.json` per mouse with the pixel size, and three
manual masks per image under `derivatives/labels/` (axon, myelin, and axonmyelin with 128 for
myelin and 255 for axon). Files are read from the archive at the pinned version into memory;
nothing is written to disk.

The model is the paper's released TEM model, `models/default_TEM_model_v1` of
https://github.com/neuropoly/axondeepseg at commit 7f6013221b2a862e107a7e23f3c8662eba3ba64b,
read from GitHub at that commit. The paper's code runs it in TensorFlow 1 (`tf.contrib`), which
cannot be installed with Python 3.13, so `unet_forward` rebuilds the network of
`network_construction.py` (`uconv_net`) with TensorFlow 2 operations of the same definition, from
the checkpoint's weights. Where each detail comes from:

- Network (`network_construction.py` and `config_network.json` of the model): per layer
  convolution without bias, batch normalisation with the stored moving mean and variance
  (`tf.contrib.layers.batch_norm`, `is_training=False`, epsilon 0.001, its default), ReLU;
  dropout is off at inference. Padding 'SAME' (the default of `tf.contrib.layers.conv2d`).
  Downsampling by a 5 x 5 convolution of stride 2 (`downconv`); upsampling by
  `tf.image.resize_images` (bilinear, TF 1 semantics, no half-pixel centres) followed by a
  2 x 2 convolution (`upconv-d*`, built with `conv_relu`), then concatenation [skip, upsampled].
  The final 1 x 1 convolution has a bias and, as `tf.contrib.layers.conv2d` defaults to, a ReLU;
  `apply_model.perform_batch_inference` takes the argmax of that output (ties go to class 0).
- Inference (`segment.py` and `apply_model.py`): working pixel size 0.01 um
  (`generate_resolution`, TEM, patch 512); overlap 25 pixels (`default_overlap`); the image
  contrast inverted once (255 - image) for `default_TEM_model_v1`; resampling by
  `skimage.transform.rescale(..., preserve_range=True).astype(int)`; patches by
  `im2patches_overlap`, each preprocessed by `apply_legacy_preprocess` (histogram equalisation
  then standardisation); stitching by `patches2im_overlap`; the class map resized back to the
  native shape by `skimage.transform.resize` and cast to uint8. The code required
  scikit-image >= 0.12.3, and in February 2018 the release was 0.13.1, whose `rescale` and
  `resize` used order 1, mode 'constant' and no anti-aliasing, and whose `equalize_hist` used an
  exact integer histogram (`np.bincount`) for integer images; those settings are given
  explicitly here (`legacy_equalize_hist`), as the defaults of the installed version differ.
- Ground truth (paper, Methods, Ground truth labelling: background 0, myelin 127, axon 255; and
  `testing/launch_performance_metrics.py`, axon above 200, myelin from 50 to 200): here the
  axon class is the axon mask and the myelin class the myelin mask of the dandiset.
- Scores: Dice per image over all pixels (`pw_dice`, `testing/segmentation_scoring.py`;
  Methods, Equation 1); three-class pixel-wise accuracy (Methods, Pixel-wise accuracy);
  detection sensitivity and precision by `score_analysis` (`segmentation_scoring.py`, min_area
  2, connected components with 8-connectivity, values rounded to 3 decimals as the code does).
"""

from __future__ import annotations

import io
import json
import os
import tempfile
import urllib.error
import urllib.request

import numpy as np
import pandas as pd
from PIL import Image
from skimage import measure
from skimage.transform import rescale, resize

DANDISET_ID = "001436"
DANDISET_VERSION = "0.250512.1625"
API = "https://api.dandiarchive.org/api"

ADS_REPO = "neuropoly/axondeepseg"
ADS_COMMIT = "7f6013221b2a862e107a7e23f3c8662eba3ba64b"
TEM_MODEL_DIR = "AxonDeepSeg/models/default_TEM_model_v1"

WORKING_PIXEL_UM = 0.01   # segment.py, generate_resolution, TEM model with 512 patches
OVERLAP = 25              # segment.py, default_overlap
PATCH = 512               # config_network.json, trainingset_patchsize
BN_EPSILON = 1e-3         # tf.contrib.layers.batch_norm default
MIN_AREA = 2              # segmentation_scoring.score_analysis default
CLASS_BG, CLASS_MYELIN, CLASS_AXON = 0, 1, 2  # apply_model paint values 0, 127, 255


# ------------------------------------------------------------------ archive access

def _get_json(url, retries=8):
    """GET a JSON document, waiting and retrying when the server asks to slow down (429)."""
    import time
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code not in (429, 502, 503) or attempt == retries - 1:
                raise
            time.sleep(min(60, 5 * 2 ** attempt))


def list_assets(version=DANDISET_VERSION):
    """All assets of the pinned version, as a DataFrame (path, asset_id, size)."""
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=1000"
    rows = []
    while url:
        page = _get_json(url)
        rows += [{"path": a["path"], "asset_id": a["asset_id"], "size": a["size"]}
                 for a in page["results"]]
        url = page["next"]
    return pd.DataFrame(rows)


def version_metadata(version=DANDISET_VERSION):
    return _get_json(f"{API}/dandisets/{DANDISET_ID}/versions/{version}/")


def read_bytes(asset_id, retries=4):
    """Read one asset into memory from the archive."""
    url = f"{API}/assets/{asset_id}/download/"
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(url, timeout=120) as r:
                return r.read()
        except Exception:
            if attempt == retries - 1:
                raise


# The dataset's data are themselves images (TEM micrographs and their masks), so they are decoded
# with Pillow; this reads the dataset's own files from the archive, not a figure.
_decode_image = Image.open


def read_png(asset_id):
    return np.array(_decode_image(io.BytesIO(read_bytes(asset_id))))


def sample_table(assets):
    """One row per TEM image with its three label masks and the mouse's pixel size."""
    paths = dict(zip(assets.path, assets.asset_id))
    rows = []
    for p in sorted(assets.path):
        if p.startswith("sub-") and p.endswith("_TEM.png"):
            name = p.split("/")[-1][:-len("_TEM.png")]
            subject, sample = name.split("_")
            lab = f"derivatives/labels/{subject}/micr/{name}_TEM_seg-"
            rows.append({
                "subject": subject, "sample": sample, "image": paths[p],
                "axon": paths.get(lab + "axon-manual.png"),
                "myelin": paths.get(lab + "myelin-manual.png"),
                "axonmyelin": paths.get(lab + "axonmyelin-manual.png"),
                "sidecar": paths.get(f"{subject}/micr/{subject}_TEM.json"),
            })
    return pd.DataFrame(rows)


def load_sample(row):
    """Image, ground-truth class map (0 bg, 1 myelin, 2 axon) and the three masks."""
    img = read_png(row["image"])
    axon = read_png(row["axon"])
    myelin = read_png(row["myelin"])
    am = read_png(row["axonmyelin"])
    gt = np.zeros(img.shape, np.uint8)
    gt[myelin > 127] = CLASS_MYELIN
    gt[axon > 127] = CLASS_AXON
    return img, gt, {"axon": axon, "myelin": myelin, "axonmyelin": am}


# ------------------------------------------------------------------ model

def load_tem_model():
    """Weights of default_TEM_model_v1 at ADS_COMMIT, as a dict of numpy arrays.

    The checkpoint reader needs files, so the two checkpoint files are put in a temporary
    directory that is removed at once; this is the model, not the dataset.
    """
    import tensorflow as tf
    base = f"https://raw.githubusercontent.com/{ADS_REPO}/{ADS_COMMIT}/{TEM_MODEL_DIR}/"
    with tempfile.TemporaryDirectory() as d:
        for f in ("model.ckpt.index", "model.ckpt.data-00000-of-00001"):
            with urllib.request.urlopen(base + f) as r, open(os.path.join(d, f), "wb") as out:
                out.write(r.read())
        reader = tf.train.load_checkpoint(os.path.join(d, "model.ckpt"))
        names = [k for k in reader.get_variable_to_shape_map()
                 if "Adam" not in k and "Momentum" not in k]
        weights = {k: reader.get_tensor(k) for k in names}
    config = _get_json(base + "config_network.json")
    return weights, config


def unet_forward(weights, config, batch):
    """Raw output (after the final ReLU) of uconv_net for a batch of 512 x 512 patches."""
    import tensorflow as tf
    depth = config["depth"]
    ncv = config["convolution_per_layer"]

    def conv_bn_relu(x, scope, stride=1):
        w = weights[f"{scope}/convolution/weights"]
        x = tf.nn.conv2d(x, w, strides=stride, padding="SAME")
        p = f"{scope}/convolution/bn/"
        x = (x - weights[p + "moving_mean"]) / np.sqrt(weights[p + "moving_variance"] + BN_EPSILON)
        x = x * weights[p + "gamma"] + weights[p + "beta"]
        return tf.nn.relu(x)

    net = tf.convert_to_tensor(np.asarray(batch, np.float32)[..., None])
    skips = []
    for i in range(depth):
        for c in range(ncv[i]):
            net = conv_bn_relu(net, f"cconv-d{i}-c{c}")
        skips.append(net)
        net = conv_bn_relu(net, f"downconv-d{i}", stride=2)
    for i in range(depth):
        d = depth - i - 1
        size = [int(net.shape[1]) * 2, int(net.shape[2]) * 2]
        net = tf.raw_ops.ResizeBilinear(images=net, size=size, align_corners=False,
                                        half_pixel_centers=False)
        net = conv_bn_relu(net, f"upconv-d{d}")
        net = tf.concat([skips[d], net], axis=3)
        for c in range(ncv[d]):
            net = conv_bn_relu(net, f"econv-d{d}-c{c}")
    out = tf.nn.conv2d(net, weights["finalconv/weights"], strides=1, padding="SAME")
    out = tf.nn.relu(out + weights["finalconv/biases"])
    return out.numpy()


# ------------------------------------------------------------------ AxonDeepSeg pipeline

def legacy_equalize_hist(patch):
    """skimage 0.13 equalize_hist for an integer image: exact integer histogram, then interp."""
    patch = np.asarray(patch)
    offset = 0
    lo = patch.min()
    if lo < 0:
        offset = lo
    hist = np.bincount((patch - offset).ravel())
    centers = np.arange(len(hist)) + offset
    idx = np.nonzero(hist)[0][0]
    hist, centers = hist[idx:], centers[idx:]
    cdf = hist.cumsum()
    cdf = cdf / float(cdf[-1])
    return np.interp(patch.flat, centers, cdf).reshape(patch.shape)


def preprocess_patch(patch):
    """apply_legacy_preprocess: histogram equalisation, then standardisation per patch."""
    p = legacy_equalize_hist(patch)
    return (p - p.mean()) / p.std()


def im2patches_overlap(img, overlap=OVERLAP, scw=PATCH):
    cropped = img[overlap:-overlap, overlap:-overlap]
    spw = scw - 2 * overlap
    qh, rh = divmod(cropped.shape[0], spw)
    qw, rw = divmod(cropped.shape[1], spw)
    L_h = [spw * e for e in range(qh)]
    L_w = [spw * e for e in range(qw)]
    if rh:
        L_h.append(cropped.shape[0] - spw)
    if rw:
        L_w.append(cropped.shape[1] - spw)
    xx, yy = np.meshgrid(L_h, L_w)
    pos = [[int(a), int(b)] for a, b in zip(np.ravel(xx), np.ravel(yy))]
    patches = [preprocess_patch(img[a:a + scw, b:b + scw]) for a, b in pos]
    return patches, pos


def patches2im_overlap(preds, pos, overlap=OVERLAP, scw=PATCH):
    """Stitching of patch_management_tools.patches2im_overlap (same writes, same order)."""
    o = overlap
    spw = scw - 2 * o
    h_l, w_l = np.max(np.stack(pos), axis=0)
    new = np.zeros((h_l + scw, w_l + scw))
    for (a, b), e in zip(pos, preds):
        if a == 0:
            if b == 0:
                new[0:o, 0:o] = e[0:o, 0:o]
                new[o:scw - o, 0:o] = e[o:-o, 0:o]
                new[0:o, o:scw - o] = e[0:o, o:-o]
            else:
                if b == w_l:
                    new[0:o, -o:] = e[0:o, -o:]
                new[0:o, b + o:b + scw - o] = e[0:o, o:-o]
        if b == 0 and a != 0:
            new[a + o:a + scw - o, 0:o] = e[o:-o, 0:o]
        if a == h_l:
            if b == w_l:
                new[-o:, -o:] = e[-o:, -o:]
                new[h_l + o:-o, -o:] = e[o:-o, -o:]
                new[-o:, w_l + o:-o] = e[-o:, o:-o]
            else:
                if b == 0:
                    new[-o:, 0:o] = e[-o:, 0:o]
                new[-o:, b + o:b + scw - o] = e[-o:, o:-o]
        if b == w_l and b != h_l:
            new[a + o:a + scw - o, -o:] = e[o:-o, -o:]
    for (a, b), e in zip(pos, preds):
        new[a + o:a + o + spw, b + o:b + o + spw] = e[o:-o, o:-o]
    return new


def segment(img, pixel_um, weights, config, invert=True, batch_size=4):
    """Class map (0 bg, 1 myelin, 2 axon) at the native shape, as segment.py gives it."""
    x = 255 - img.astype(np.int64) if invert else img.astype(np.int64)
    coeff = pixel_um / WORKING_PIXEL_UM
    rs = rescale(x.astype(np.uint8), coeff, order=1, mode="constant", preserve_range=True,
                 anti_aliasing=False).astype(int)
    patches, pos = im2patches_overlap(rs)
    preds = []
    for i in range(0, len(patches), batch_size):
        out = unet_forward(weights, config, patches[i:i + batch_size])
        preds += list(np.argmax(out, axis=3))
    stitched = patches2im_overlap(preds, pos)
    back = resize(stitched, img.shape, order=1, mode="constant", anti_aliasing=False)
    return back.astype(np.uint8), rs.shape, len(patches)


# ------------------------------------------------------------------ scores

def pw_dice(a, b):
    a, b = a.astype(bool), b.astype(bool)
    s = a.sum() + b.sum()
    return 1.0 if s == 0 else 2.0 * np.logical_and(a, b).sum() / s


def pixel_accuracy(pred, gt):
    return float(np.mean(pred == gt))


def score_analysis(groundtruth, prediction, min_area=MIN_AREA):
    """segmentation_scoring.score_analysis: [sensitivity, precision, TP, FP, P]."""
    lp = measure.label(prediction, connectivity=2)
    rp = measure.regionprops(lp)
    cent = np.array([list(r.centroid) for r in rp]).astype(int).reshape(-1, 2)
    areas = np.array([r.area for r in rp])
    cent = cent[areas > min_area] if len(areas) else cent
    cent = np.unique(cent, axis=0)  # the code keeps the centroids in a set
    lt = measure.label(groundtruth, connectivity=2)
    P = int(lt.max())
    # A predicted centroid matches the ground-truth object whose pixels contain it; each
    # ground-truth object with at least one centroid is one true positive.
    lab_at = lt[cent[:, 0], cent[:, 1]] if len(cent) else np.array([], int)
    TP = len(np.unique(lab_at[lab_at > 0]))
    FP = int(np.sum(lab_at == 0))
    sens = round(TP / P, 3) if P else np.nan
    prec = round(TP / (TP + FP), 3) if (TP + FP) else np.nan
    return sens, prec, TP, FP, P


def scores(pred, gt):
    """Axon Dice, myelin Dice, accuracy, sensitivity, precision for one image."""
    pa, ga = pred == CLASS_AXON, gt == CLASS_AXON
    pm, gm = pred == CLASS_MYELIN, gt == CLASS_MYELIN
    sens, prec, tp, fp, p = score_analysis(ga, pa)
    return {"axon_dice": pw_dice(pa, ga), "myelin_dice": pw_dice(pm, gm),
            "accuracy": pixel_accuracy(pred, gt), "sensitivity": sens, "precision": prec,
            "TP": tp, "FP": fp, "P": p,
            "pred_axon_frac": pa.mean(), "gt_axon_frac": ga.mean(),
            "pred_myelin_frac": pm.mean(), "gt_myelin_frac": gm.mean()}


def original_graph_output(patches):
    """Output of finalconv/Relu in the model's own saved TF 1 graph (model.ckpt.meta at
    ADS_COMMIT), run with training_phase False, to check `unet_forward` against it."""
    import tensorflow as tf
    base = f"https://raw.githubusercontent.com/{ADS_REPO}/{ADS_COMMIT}/{TEM_MODEL_DIR}/"
    with tempfile.TemporaryDirectory() as d:
        for f in ("model.ckpt.meta", "model.ckpt.index", "model.ckpt.data-00000-of-00001"):
            with urllib.request.urlopen(base + f) as r, open(os.path.join(d, f), "wb") as out:
                out.write(r.read())
        with tf.Graph().as_default() as g:
            saver = tf.compat.v1.train.import_meta_graph(os.path.join(d, "model.ckpt.meta"),
                                                         clear_devices=True)
            with tf.compat.v1.Session(graph=g) as sess:
                saver.restore(sess, os.path.join(d, "model.ckpt"))
                return sess.run(g.get_tensor_by_name("finalconv/Relu:0"),
                                feed_dict={"input:0": np.asarray(patches, np.float32),
                                           "training_phase:0": False})


def image_checks(img, gt, masks, shift=50):
    """Checks of one image and its masks against their description.

    Returns the mask values, whether the axonmyelin mask agrees with the axon and myelin masks,
    the overlap of axon and myelin, and the grey-level contrast between myelin and the rest of
    the image with the masks in place and shifted by `shift` pixels (a standard choice; myelin
    is the darkest structure in TEM, so a mask that is aligned with its image gives a larger
    contrast than a shifted one).
    """
    am_raw = masks["axonmyelin"]
    # Some axonmyelin pngs are grey plus alpha; the grey channel holds the classes.
    am = am_raw[..., 0] if am_raw.ndim == 3 else am_raw
    ax, my = masks["axon"] > 127, masks["myelin"] > 127
    my_s = np.roll(my, (shift, shift), axis=(0, 1))
    f = img.astype(float)
    return {
        "axon_values": tuple(np.unique(masks["axon"]).tolist()),
        "myelin_values": tuple(np.unique(masks["myelin"]).tolist()),
        "axonmyelin_values": tuple(np.unique(am).tolist()),
        "axonmyelin_channels": 1 if am_raw.ndim == 2 else am_raw.shape[2],
        "axonmyelin_alpha": tuple(np.unique(am_raw[..., 1]).tolist()) if am_raw.ndim == 3 else None,
        "mask_dims": (masks["axon"].ndim, masks["myelin"].ndim, img.ndim),
        "am_agrees": bool(np.array_equal(am == 255, ax) and np.array_equal(am == 128, my)),
        "axon_myelin_overlap": int(np.logical_and(ax, my).sum()),
        "contrast": f[~my].mean() - f[my].mean(),
        "contrast_shifted": f[~my_s].mean() - f[my_s].mean(),
        "img_min": int(img.min()), "img_max": int(img.max()),
        "height": img.shape[0], "width": img.shape[1],
    }


def thumbnail(img, n=32):
    """Block means on an n x n grid, to look for images deposited twice."""
    h, w = img.shape[0] // n * n, img.shape[1] // n * n
    return img[:h, :w].reshape(n, h // n, n, w // n).mean(axis=(1, 3)).ravel()


# ------------------------------------------------------------------ group labels (outside input)

# The White Matter Microscopy Database (https://osf.io/yp4qg/, doi:10.17605/OSF.IO/YP4QG), which
# the paper's Data availability statement names, has a component for the NYU mouse data of
# ref. 27 (OSF node adrcs). Its folder histology/MiceMyelinQuantification holds the raw TEM
# images in one folder per diet group and time point, and one sub-folder per mouse, named by
# the mouse number (with G/S suffixes). Only the folder names are used, to label each mouse of
# the dandiset as control or cuprizone; the link is tested in the notebook.
OSF_NODE = "adrcs"
OSF_ROOT = "NewYorkUniversitySchoolOfMedicine/histology/MiceMyelinQuantification"


def _osf_children(url):
    url += ("&" if "?" in url else "?") + "page[size]=100"
    out = []
    while url:
        d = _get_json(url)
        out += d["data"]
        url = d["links"].get("next")
    return out


def osf_mouse_folders():
    """One row per mouse folder of the OSF deposit: group folder, mouse folder, mouse number,
    and the address of its file list."""
    import re
    url = f"https://api.osf.io/v2/nodes/{OSF_NODE}/files/osfstorage/"
    for part in OSF_ROOT.split("/"):
        node = next(x for x in _osf_children(url) if x["attributes"]["name"] == part)
        url = node["relationships"]["files"]["links"]["related"]["href"]
    rows = []

    def walk(url, group):
        for x in _osf_children(url):
            a = x["attributes"]
            if a["kind"] != "folder":
                continue
            sub = x["relationships"]["files"]["links"]["related"]["href"]
            m = re.match(r"^(\d+)", a["name"])
            if m:
                rows.append({"group_folder": group, "mouse_folder": a["name"],
                             "mouse": int(m.group(1)), "files_url": sub})
            else:
                walk(sub, a["name"])  # a group folder (one is nested in another)

    walk(url, None)
    return pd.DataFrame(rows)


def osf_files(files_url):
    """Files of one OSF folder: name, size, OSF file id, modified date."""
    return pd.DataFrame([{"name": f["attributes"]["name"], "size": f["attributes"]["size"],
                          "id": f["id"], "modified": f["attributes"]["date_modified"]}
                         for f in _osf_children(files_url) if f["attributes"]["kind"] == "file"])


def read_osf_image(file_id):
    with urllib.request.urlopen(f"https://osf.io/download/{file_id}/", timeout=300) as r:
        return np.array(_decode_image(io.BytesIO(r.read())))


# ------------------------------------------------------------------ the whole dataset

def process_sample(row, data, weights, config):
    """Checks, and the scores of the segmentation with and without the contrast inversion."""
    import hashlib
    img, gt, masks = data
    out = {"subject": row["subject"], "sample": row["sample"],
           "sha1": hashlib.sha1(img.tobytes()).hexdigest(),
           "gt_sha1": hashlib.sha1(gt.tobytes()).hexdigest()}
    out.update(image_checks(img, gt, masks))
    out["thumb"] = thumbnail(img)
    for invert, tag in ((True, "inv"), (False, "noinv")):
        pred, rs_shape, n_patches = segment(img, row["pixel_um"], weights, config, invert=invert)
        for k, v in scores(pred, gt).items():
            out[f"{tag}_{k}"] = v
    out["resampled_shape"] = rs_shape
    out["n_patches"] = n_patches
    return out


def run_all(table, weights, config, workers=4):
    """process_sample over every row, reading the files ahead in threads."""
    from concurrent.futures import ThreadPoolExecutor
    rows = [r for _, r in table.iterrows()]
    results = []
    with ThreadPoolExecutor(workers) as pool:
        futures = [pool.submit(load_sample, r) for r in rows[:workers]]
        for i, r in enumerate(rows):
            data = futures[i].result()
            if i + workers < len(rows):
                futures.append(pool.submit(load_sample, rows[i + workers]))
            futures[i] = None
            results.append(process_sample(r, data, weights, config))
    return pd.DataFrame(results)


def osf_thumbnails(files, shape, max_files=4, min_bytes=25e6):
    """Thumbnails of up to `max_files` (in name order) full-size micrographs (files over `min_bytes`, not the
    'check' overlays) of one OSF mouse folder, cropped to the dandiset's image `shape` from the
    top left (the dandiset's images are cropped at the bottom, README). One thumbnail per
    colour channel, as the OSF files are RGB."""
    big = files[(files["size"] > min_bytes) & ~files["name"].str.contains("check")]
    out = []
    for _, f in big.sort_values("name").head(max_files).iterrows():
        im = read_osf_image(f["id"])
        im = im[..., None] if im.ndim == 2 else im
        if im.shape[0] < shape[0] or im.shape[1] < shape[1]:
            out.append((f["name"], f["id"], im.shape, None))
            continue
        crop = im[:shape[0], :shape[1]]
        out.append((f["name"], f["id"], im.shape,
                    [thumbnail(crop[..., k].astype(float)) for k in range(crop.shape[2])]))
    return out


def best_match(thumbs, dandi_thumbs):
    """For each channel thumbnail, the absolute correlation with every dandiset thumbnail;
    returns the largest over channels, per dandiset image."""
    D = np.asarray(dandi_thumbs, float)
    D = (D - D.mean(1, keepdims=True)) / D.std(1, keepdims=True)
    best = np.zeros(len(D))
    for t in thumbs:
        t = (t - t.mean()) / t.std()
        best = np.maximum(best, np.abs(D @ t) / len(t))
    return best


# ------------------------------------------------------------------ macaque image (data elsewhere)

# The macaque TEM images of ref. 7 (Stikov et al. 2015) are in the White Matter Microscopy
# Database, OSF node yp4qg, folder MontrealNeurologicalInstitute/histology/Macaque: data/sampleN
# holds three images per sample (NIfTI, 2300 x 3040) and segmentation/sampleN one myelin mask
# (myelin.nii, 0 or 1) and one axon mask (avf.nii, 0 or 1/255) per sample. The NIfTI headers
# give a voxel size of 2.0, which is not the pixel size; Table 1 of the paper gives 0.009 um for
# the macaque test image, used here (2300 x 3040 pixels at 0.009 um is 20.7 x 27.4 um, the
# 27 x 21 um2 of Table 1).
MACAQUE_NODE = "yp4qg"
MACAQUE_ROOT = "MontrealNeurologicalInstitute/histology/Macaque"
MACAQUE_PIXEL_UM = 0.009  # paper, Table 1


def osf_macaque_files():
    """One row per file: kind (data or segmentation), sample, name, OSF id, size, modified."""
    url = f"https://api.osf.io/v2/nodes/{MACAQUE_NODE}/files/osfstorage/"
    for part in MACAQUE_ROOT.split("/"):
        node = next(x for x in _osf_children(url) if x["attributes"]["name"] == part)
        url = node["relationships"]["files"]["links"]["related"]["href"]
    rows = []
    for kind in _osf_children(url):
        for s in _osf_children(kind["relationships"]["files"]["links"]["related"]["href"]):
            for f in _osf_children(s["relationships"]["files"]["links"]["related"]["href"]):
                rows.append({"kind": kind["attributes"]["name"], "sample": s["attributes"]["name"],
                             "name": f["attributes"]["name"], "id": f["id"],
                             "size": f["attributes"]["size"],
                             "modified": f["attributes"]["date_modified"]})
    return pd.DataFrame(rows).sort_values(["kind", "sample", "name"]).reset_index(drop=True)


def read_osf_nifti(file_id):
    """A 2D NIfTI image of the OSF deposit, read into memory."""
    import nibabel as nib
    with urllib.request.urlopen(f"https://osf.io/download/{file_id}/", timeout=300) as r:
        img = nib.Nifti1Image.from_bytes(r.read())
    return np.asarray(img.dataobj).squeeze()


def macaque_ground_truth(myelin, axon):
    """Class map (0 bg, 1 myelin, 2 axon) from the two masks; axon where both are set."""
    gt = np.zeros(myelin.shape, np.uint8)
    gt[myelin > 0] = CLASS_MYELIN
    gt[axon > 0] = CLASS_AXON
    return gt
