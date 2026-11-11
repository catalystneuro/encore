# kussovska-2025 · author · run 42760373832

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls entries claims attempts paper
```

```
<persisted-output>
Output too large (51.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/73ddb9af-d626-46dd-830a-acdf1e4fec3e/tool-results/ba62n423n.txt

Preview (first 2KB):
Tue Nov 10 05:18:05 UTC 2026
# Protocol for an attempt

Version: `pilot-14`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 635 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; echo ----; wc -l docs/design.md docs/archives.md; ls paper claims/kussovska-2025.yaml entries/fouke-2025 attempts | head -50; cat papers/datasets/kussovska-2025.yaml
```

```
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://encorescience.org/>

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/design.md; sed -n 1,140p docs/archives.md; ls paper; ls paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/kussovska-2025.yaml; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/kussovska-2025.yaml"
}
```

```
1	# Claims for Kussovska, Kim & Rungratsameetaweemana (2025), "Neural heterogeneity shapes the
2	# temporal structure of human working memory", bioRxiv, doi:10.1101/2025.10.31.684900, tested on
3	# DANDI:000469 (reused; the paper analyses the dataset of Kyzar et al. 2024, ref. 59).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
6	#
7	# Text read. paper/10.1101-2025.10.31.684900.txt, the bioRxiv full-text page of the preprint
8	# posted 1 November 2025 (its header says "version of record"; the page says "New Results" and
9	# offers a "current version", so a later version may exist; it was not read). It holds the
10	# abstract, Introduction, Results, legends of Figures 1 to 6, Discussion, Methods, Data and Code
11	# availability and references. No PDF was supplied. The Extended Data figures (Extended Data
12	# Figs 1 to 5, behind "Supplementary Material") and their legends are not in the text read; the
13	# Source Data are not either. The main findings are all stated in the main text and legends, so
14	# claims were written; claims on Extended Data panels rest on the main-text sentences that cite
15	# them, and their sources say "(not in the text read)". Several equations of the Methods (the GLM
16	# link, the local-peak and prominence formulas of Burst detection) were lost in extraction.
17	#
18	# Code read. github.com/dariakussovska/heterogeneitywm at commit 5144fe8 (2025-10-26), the last
19	# commit before the preprint was posted. Later commits (REVISIONS/ and R2_REVISIONS/, 2026) are
20	# for a revised version and were not used. The repository holds Python scripts named by figure
[... 925 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/kussovska-2025.yaml",
 "offset": 946,
 "limit": 500
}
```

```
946	    and larger τrise (U = 13465, P = 2.58 × 10−9; Fig. 5f).
947	  statistics:
948	  - about: firing rate
949	    test: Mann-Whitney U (Wilcoxon rank-sum)
950	    statistic: U = 17294
951	    p: 1.42e-32
952	  - about: normalised mean ACG amplitude
953	    test: Mann-Whitney U (Wilcoxon rank-sum)
954	    statistic: U = 18522
955	    p: 2.16e-41
956	  - about: tau_rise
957	    test: Mann-Whitney U (Wilcoxon rank-sum)
958	    statistic: U = 13465
959	    p: 2.58e-9
960	  depends_on:
961	  - fig5c-cell-type-clusters
962	  criterion: Two-sided Mann-Whitney U tests of IN against PY on each feature, with Benjamini-Yekutieli
963	    FDR over the five metrics of Fig. 5d-h as in 05_cell_analysis/main_5d-h.py:49-63. Reproduced
964	    when IN is higher on all three with corrected p < 0.05. The features are those the clusters
965	    were formed on, so the claim follows from fig5c-cell-type-clusters by construction; the
[... 479 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -250
```

```
total 132
drwxr-xr-x   2 runner runner  4096 Nov 10 05:11 .
drwxr-xr-x 249 runner runner 12288 Nov 10 05:11 ..
-rw-r--r--   1 runner runner  2144 Nov 10 05:11 README.md
-rw-r--r--   1 runner runner   907 Nov 10 05:11 entry.yaml
-rw-r--r--   1 runner runner 16218 Nov 10 05:11 omr.py
-rw-r--r--   1 runner runner 79403 Nov 10 05:11 reproduce_fouke_2025.ipynb
-rw-r--r--   1 runner runner    61 Nov 10 05:11 requirements.in
-rw-r--r--   1 runner runner  5989 Nov 10 05:11 requirements.lock.txt
schema_version: 1
name: fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
license: Apache-2.0
notebooks:
[... 268 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 250,400p attempts/fouke-2025-01.yaml; cat entries/fouke-2025/README.md; python -c "
import json;nb=json.load(open('entries/fouke-2025/reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:1500]); print('=====')
"; ls schemas tools
```

```
- kind: metadata_insufficient
  statement: The stimulus codes 0 to 20 have no names or description in the files or the
    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
    file of its stimulus software.
- kind: code_mismatch
  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
    while its conversion of the stimulus software's names gives the reverse (it carries a remap
    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
    Danionella turn more to the right for code 11, which fits the stimulus software's assignment
    only if the fish turn with lateral motion.
- kind: metadata_error
  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so
    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists
    only Danio rerio; the files hold 37 fish of two species.
- kind: metadata_error
  statement: f0_vtheta is stated in radians/s but holds the heading change per frame in radians,
    and f0_vx and f0_vy are stated in pixels/s but are per frame. In most Danionella files the sum
    of f0_vtheta over a trial does not match the change of f0_theta (median ratios 0.09 to 0.89).
- kind: other
  statement: 18 of 25 zebrafish files and 1 of 12 Danionella files are sampled at 32 to 35 Hz,
[... 308 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000469/versions/ | python -m json.tool | head -60; curl -sI https://raw.githubusercontent.com/dariakussovska/heterogeneitywm/5144fe8/README.md | head -3; python -c "import pynwb,remfile,h5py,sklearn;print('ok')"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev --python 3.12 && source dev/bin/activate && uv pip install -q pynwb remfile h5py numpy pandas scipy scikit-learn statsmodels matplotlib dandi openpyxl scikit-posthocs nbformat nbclient ipykernel pyyaml jsonschema 2>&1 | tail -3; python -c "import pynwb;print(pynwb.__version__)"; curl -s https://api.dandiarchive.org/api/dandisets/000469/versions/ | python -c "import json,sys;[print(r['version'],r['modified'],r['asset_count'],r['size']) for r in json.load(sys.stdin)['results']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; python - <<'EOF'
import requests
for v in ['0.231213.2047','0.240123.1806']:
    r=requests.get(f'https://api.dandiarchive.org/api/dandisets/000469/versions/{v}/assets/?page_size=200').json()
    print(v, r['count'])
    for a in sorted(r['results'],key=lambda a:a['path']):
        print(' ',a['path'],a['size'],a['blob'] if 'blob' in a else a['asset_id'])
EOF
```

```
0.231213.2047 41
  sub-1/sub-1_ses-1_ecephys+image.nwb 201240176 b586c127-42dd-4e3d-aefd-3fee06559dbc
  sub-1/sub-1_ses-2_ecephys+image.nwb 221906568 c2aa8c80-5b53-40fd-91ac-089d3ad9ba7d
  sub-10/sub-10_ses-1_ecephys+image.nwb 359151664 d9350dd5-6e23-437f-bb09-626fe352986b
  sub-10/sub-10_ses-2_ecephys+image.nwb 264088224 532a7017-6110-42f2-b64e-c7ca76eaaf38
  sub-11/sub-11_ses-1_ecephys+image.nwb 523006664 9a2f7f97-6bf5-4aec-89dc-94576ee692a0
  sub-11/sub-11_ses-2_ecephys+image.nwb 615628696 a14e4510-5e0e-4d23-96ed-a37b34d98921
  sub-12/sub-12_ses-1_ecephys+image.nwb 71553336 3196ad42-61b2-405a-bd23-78a2cf0a6575
  sub-12/sub-12_ses-2_ecephys+image.nwb 124567248 95b24577-bce2-45ae-b992-65339968ad8d
  sub-13/sub-13_ses-1_ecephys+image.nwb 323444768 de325b7d-2c8d-4562-8744-60f0fd56784b
  sub-13/sub-13_ses-2_ecephys+image.nwb 263191880 688b394b-bcd9-463c-8111-d394039e1ecc
  sub-14/sub-14_ses-1_ecephys+image.nwb 298784488 f5e466dc-6bdb-4c18-8189-013c9e80805a
  sub-14/sub-14_ses-2_ecephys+image.nwb 332059624 0cc73ac0-fb89-4c67-a6a8-6133654d2740
  sub-15/sub-15_ses-1_ecephys+image.nwb 262797288 a5761234-5ad5-42c6-8b65-e38e1703b1fc
  sub-15/sub-15_ses-2_ecephys+image.nwb 461967400 33370a8f-c7e6-4a2e-b495-efb378a0f8ba
  sub-16/sub-16_ses-1_ecephys+image.nwb 166473608 93948011-d1ff-41de-865f-3eefe729c599
  sub-16/sub-16_ses-2_ecephys+image.nwb 364952192 a1a94b01-8b5b-4fa4-ac28-67465e6b6f30
  sub-17/sub-17_ses-1_ecephys+image.nwb 47345824 08f2fc15-80cb-455f-b8c5-c60cb49f9f6e
  sub-17/sub-17_ses-2_ecephys+image.nwb 100155416 0bcba855-7e9b-456e-bd5b-39749b933e19
  sub-18/sub-18_ses-1_ecephys+image.nwb 230621736 82abde26-2184-452b-a250-736d3511e921
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd $TMPDIR; cat > probe.py <<'EOF'
import requests, remfile, h5py, pynwb, time
t=time.time()
r=requests.get('https://api.dandiarchive.org/api/dandisets/000469/versions/0.231213.2047/assets/?page_size=200').json()
a=[x for x in r['results'] if x['path']=='sub-1/sub-1_ses-2_ecephys+image.nwb'][0]
url=f"https://api.dandiarchive.org/api/assets/{a['asset_id']}/download/"
url=requests.head(url,allow_redirects=True).url
f=h5py.File(remfile.File(url),'r')
def walk(g,p=''):
    for k,v in g.items():
        if isinstance(v,h5py.Dataset): print(p+'/'+k, v.shape, v.dtype)
        else:
            print(p+'/'+k+'/'); 
            if not k.startswith('ImageSeries') and 'stimulus' not in p: walk(v,p+'/'+k)
walk(f)
io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
print(nwb)
print(nwb.trials.to_dataframe().head(10).T)
print(nwb.units.colnames, len(nwb.units))
print(nwb.electrodes.to_dataframe().head())
print(nwb.subject)
print(time.time()-t)
EOF
python probe.py 2>&1 | grep -v Warn | head -200
```

```
/acquisition/
/acquisition/events/
/acquisition/events/data (948,) int8
/acquisition/events/timestamps (948,) float64
/analysis/
/file_create_date (2,) object
/general/
/general/devices/
/general/devices/NLX-microwires-33/
/general/devices/NLX-microwires-34/
/general/devices/NLX-microwires-35/
/general/devices/NLX-microwires-36/
/general/devices/NLX-microwires-37/
/general/devices/NLX-microwires-38/
/general/devices/NLX-microwires-39/
/general/devices/NLX-microwires-41/
/general/devices/NLX-microwires-42/
/general/devices/NLX-microwires-43/
/general/devices/NLX-microwires-44/
/general/devices/NLX-microwires-45/
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; grep -n -i -E "^(methods|results|discussion|references|data availability|code availability)|^[A-Z][a-z ]+$" paper/*.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.10.31.684900.txt",
 "offset": 291,
 "limit": 230
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && git clone -q https://github.com/dariakussovska/heterogeneitywm.git hwm 2>&1 | tail -2; cd hwm && git checkout -q 5144fe8 && git log -1 --format='%H %ci' && find . -type f -not -path './.git/*' | grep -v -E 'REVISIONS' | head -100
```

```
Tue Nov 10 05:19:29 UTC 2026
5144fe80876d14e8aacb4044977c3474c454f14b 2025-10-26 20:56:07 -0400
./07_spectral_clustering.py
./02_trial_info.py
./08_dpca_matrices.py
./data/new_trial_final.xlsx
./data/all_neuron_brain_regions_cleaned.xlsx
./data/electrodes_plotting/electrodes_locations.mat
./data/electrodes_plotting/plot_electrodes.m
./data/cell_analysis/Mean_ACG.m
./data/cell_analysis/decay_constant_change.xlsx
./data/cell_analysis/Cell_metrics.xlsx
./data/cell_analysis/validation_data.xlsx
./data/cell_analysis/spikes_struct.mat
./data/cell_analysis/calc_ACG_metrics.m
./data/cell_analysis/fit_ACG.m
./data/cell_analysis/normalize_acg_to_unit.m
./data/cell_analysis/acg.mat
./data/new_trial_info.xlsx
./05_cell_analysis/main_5d-h.py
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/kussovska-2025; cat > entries/kussovska-2025/wm.py <<'EOF'
"""Loading and shared measures for DANDI:000469 (Kyzar et al. 2024), as used by Kussovska, Kim and
Rungratsameetaweemana (2025), "Neural heterogeneity shapes the temporal structure of human working
memory" (bioRxiv doi:10.1101/2025.10.31.684900).

The data are streamed from the archive at a pinned version (DANDISET_VERSION, the version the paper
cites in Methods, Participants and data source). Only the Sternberg file of each subject is read
(sub-<n>_ses-2), as the paper's code does (01_data_extraction.py:417 of
github.com/dariakussovska/heterogeneitywm at commit 5144fe8); only the spike times, the electrode
locations and the trials table are read, not the waveforms or the stimulus images.
"""
from concurrent.futures import ThreadPoolExecutor

import h5py
import numpy as np
import pandas as pd
import remfile
import requests

DANDISET_ID = "000469"
DANDISET_VERSION = "0.231213.2047"
API = "https://api.dandiarchive.org/api"

TRIAL_COLUMNS = ["loads", "loadsEnc1_PicIDs", "loadsEnc2_PicIDs", "loadsEnc3_PicIDs",
                 "loadsProbe_PicIDs", "probe_in_out", "response_accuracy", "start_time", "stop_time",
                 "timestamps_FixationCross", "timestamps_Encoding1", "timestamps_Encoding1_end",
                 "timestamps_Encoding2", "timestamps_Encoding2_end", "timestamps_Encoding3",
                 "timestamps_Encoding3_end", "timestamps_Maintenance", "timestamps_Probe",
                 "timestamps_Response"]

# Region names: the dataset's location labels with the hemisphere removed (left and right merged,
# as main_1e,f.py:87-104 of the paper's code merges them).
REGION_OF = {"amygdala": "AMY", "hippocampus": "HPC", "dorsal_anterior_cingulate_cortex": "dACC",
             "pre_supplementary_motor_area": "preSMA", "ventral_medial_prefrontal_cortex": "vmPFC"}


def list_assets(version=DANDISET_VERSION):
    url = f"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/?page_size=200"
    out = []
    while url:
        r = requests.get(url, timeout=60).json()
        out += r["results"]
        url = r["next"]
    return sorted(out, key=lambda a: a["path"])


def asset_url(asset_id):
    return requests.head(f"{API}/assets/{asset_id}/download/", allow_redirects=True, timeout=60).url


def region_of(location):
    loc = location.lower()
    for side in ("left_", "right_"):
        if loc.startswith(side):
            loc = loc[len(side):]
    return REGION_OF.get(loc, loc)


def _str(x):
    return x.decode() if isinstance(x, bytes) else str(x)


def load_session(asset):
    """Read one NWB file over HTTP: units (spike times, location), trials, subject."""
    f = h5py.File(remfile.File(asset_url(asset["asset_id"])), "r")
    st = f["units/spike_times"][:]
    idx = f["units/spike_times_index"][:]
    el = f["units/electrodes"][:]
    loc = np.array([_str(x) for x in f["general/extracellular_ephys/electrodes/location"][:]])
    el_ids = f["general/extracellular_ephys/electrodes/id"][:]
    pos = {e: i for i, e in enumerate(el_ids)}
    unit_ids = f["units/id"][:]
    starts = np.r_[0, idx[:-1]]
    spikes = [st[a:b] for a, b in zip(starts, idx)]
    trials = pd.DataFrame({c: f["intervals/trials/" + c][:] for c in TRIAL_COLUMNS})
    trials.insert(0, "trial_id", f["intervals/trials/id"][:])
    subj = {k: _str(f["general/subject/" + k][()]) for k in f["general/subject"].keys()}
    units = pd.DataFrame({"unit_id": unit_ids, "electrode": el,
                          "location": [loc[pos[e]] if e in pos else loc[e] for e in el]})
    units["region"] = units.location.map(region_of)
    units["n_spikes"] = [len(s) for s in spikes]
    events = f["acquisition/events/timestamps"][:] if "acquisition/events" in f else None
    sess = {"path": asset["path"], "asset_id": asset["asset_id"], "size": asset["size"],
            "subject": subj, "units": units, "spikes": spikes, "trials": trials,
            "session_description": _str(f["session_description"][()]),
            "session_id": _str(f["general/session_id"][()]) if "general/session_id" in f else "",
            "n_events": None if events is None else len(events)}
    f.close()
    return sess


def sternberg_assets(version=DANDISET_VERSION):
    return [a for a in list_assets(version) if "_ses-2_" in a["path"]]


def subject_number(path):
    return int(path.split("/")[0].split("-")[1])


def load_all(version=DANDISET_VERSION, workers=6):
    assets = sternberg_assets(version)
    with ThreadPoolExecutor(workers) as ex:
        sessions = list(ex.map(load_session, assets))
    for s in sessions:
        s["sub"] = subject_number(s["path"])
    return sorted(sessions, key=lambda s: s["sub"])
EOF
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025 && python -c "
import time,resource,wm
t=time.time(); S=wm.load_all(); print(time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
import pandas as pd
for s in S: print(s['sub'], s['session_description'][:40], len(s['units']), len(s['trials']), s['units'].region.value_counts().to_dict(), s['subject'])
u=pd.concat([s['units'].assign(sub=s['sub']) for s in S]); print(len(u)); print(u.region.value_counts()); print(u.location.value_counts())
import pickle; pickle.dump(S,open('$TMPDIR/S.pkl','wb'))
"
```

```
25.994364023208618 0.162768 GB
1 SBID: 1 40 135 {'pre_supplementary_motor_area_right': 21, 'dorsal_anterior_cingulate_cortex_right': 11, 'amygdala_right': 6, 'hippocampus_right': 2} {'age': 'P25Y', 'description': 'Subject metadata', 'sex': 'F', 'species': 'Homo sapiens', 'subject_id': '1'}
2 SBID: 2 32 135 {'ventral_medial_prefrontal_cortex_right': 14, 'hippocampus_right': 13, 'amygdala_left': 3, 'hippocampus_left': 2} {'age': 'P42Y', 'description': 'Subject metadata', 'sex': 'F', 'species': 'Homo sapiens', 'subject_id': '2'}
3 SBID: 3 28 135 {'pre_supplementary_motor_area_left': 14, 'dorsal_anterior_cingulate_cortex_left': 9, 'hippocampus_right': 4, 'amygdala_left': 1} {'age': 'P53Y', 'description': 'Subject metadata', 'sex': 'F', 'species': 'Homo sapiens', 'subject_id': '3'}
4 SBID: 4 76 135 {'amygdala_left': 33, 'ventral_medial_prefrontal_cortex_right': 12, 'pre_supplementary_motor_area_right': 11, 'amygdala_right': 9, 'pre_supplementary_motor_area_left': 7, 'ventral_medial_prefrontal_cortex_left': 3, 'dorsal_anterior_cingulate_cortex_left': 1} {'age': 'P32Y', 'description': 'Subject metadata', 'sex': 'M', 'species': 'Homo sapiens', 'subject_id': '4'}
5 SBID: 5 50 135 {'dorsal_anterior_cingulate_cortex_right': 20, 'hippocampus_right': 13, 'pre_supplementary_motor_area_right': 8, 'amygdala_right': 6, 'ventral_medial_prefrontal_cortex_right': 3} {'age': 'P32Y', 'description': 'Subject metadata', 'sex': 'F', 'species': 'Homo sapiens', 'subject_id': '5'}
6 SBID: 6 35 108 {'pre_supplementary_motor_area_left': 24, 'dorsal_anterior_cingulate_cortex_left': 10, 'hippocampus_left': 1} {'age': 'P32Y', 'description': 'Subject metadata', 'sex': 'M', 'species': 'Homo sapiens', 'subject_id': '6'}
7 SBID: 7 22 108 {'amygdala_right': 16, 'pre_supplementary_motor_area_right': 6} {'age': 'P19Y', 'description': 'Subject metadata', 'sex': 'M', 'species': 'Homo sapiens', 'subject_id': '7'}
8 SBID: 8 74 108 {'hippocampus_right': 23, 'dorsal_anterior_cingulate_cortex_left': 19, 'dorsal_
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import re
s=open('wm.py').read()
s=s.replace('''    loc = location.lower()
    for side in ("left_", "right_"):
        if loc.startswith(side):
            loc = loc[len(side):]
    return REGION_OF.get(loc, loc)''','''    loc = location.lower()
    for side in ("_left", "_right"):
        if loc.endswith(side):
            loc = loc[: -len(side)]
    return REGION_OF.get(loc, loc)''')
open('wm.py','w').write(s)
EOF
cd $TMPDIR/hwm; cat 04_concept_cells.py | sed -n 1,140p; cat 01_task/main_1e,f.py
```

```
import pandas as pd
import numpy as np
from ast import literal_eval
import os 
import matplotlib.pyplot as plt

def compute_firing_rate(df, start_time=0.2, end_time=1.0):
    """
    Computes firing rate for each (subject_id, trial_id, Neuron_ID) using Standardized_Spikes.
    Only spikes between 0.2s and 1.0s are considered.
    """
    spike_rates = []

    for _, row in df.iterrows():
        spikes = row['Standardized_Spikes']
        spike_times = literal_eval(str(spikes)) if isinstance(spikes, str) else spikes
        spike_times = spike_times if isinstance(spike_times, list) else []

        spikes_in_window = [s for s in spike_times if start_time <= s <= end_time]
        firing_rate = len(spikes_in_window) / (end_time - start_time)
[... 366 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd $TMPDIR/hwm/data; python -c "
import pandas as pd
for f in ['new_trial_info.xlsx','new_trial_final.xlsx','all_neuron_brain_regions_cleaned.xlsx','cell_analysis/Cell_metrics.xlsx']:
    d=pd.read_excel(f); print(f,d.shape); print(d.head(3).T); print(d.columns.tolist())
"; cd ..; sed -n 80,130p 03_standardization.py; sed -n 225,265p 03_standardization.py
```

```
new_trial_info.xlsx (2056, 9)
                           0           1           2
subject_id              1.00    1.000000    1.000000
trial_id                1.00    2.000000    3.000000
index                 101.00  102.000000  103.000000
RT                      1.07    1.312624    1.735249
stimulus_index          4.00    0.000000    2.000000
num_images_presented    3.00    3.000000    3.000000
response_accuracy       1.00    1.000000    1.000000
new_trial_id            1.00    2.000000    3.000000
RT_2                    1.00    1.000000    0.000000
['subject_id', 'trial_id', 'index', 'RT', 'stimulus_index', 'num_images_presented', 'response_accuracy', 'new_trial_id', 'RT_2']
new_trial_final.xlsx (1575, 14)
                             0         1         2
subject_id                   1         1         1
trial_id                     1         2         3
index                      101       102       103
trial_id_final              67        71        69
RT                        1.07  1.312624  1.735249
image_id_enc1         image_62  image_22  image_53
[... 126 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd $TMPDIR/hwm; python -c "
import pandas as pd, pickle
a=pd.read_excel('data/new_trial_info.xlsx'); b=pd.read_excel('data/new_trial_final.xlsx')
print(a.groupby('subject_id').agg(n=('trial_id','size'),nn=('new_trial_id','count'),mx=('new_trial_id','max')).T)
g=a.dropna(subset=['new_trial_id']).groupby('new_trial_id').num_images_presented.nunique(); print('load consistent across subj per new_trial_id:', (g==1).mean(), len(g))
print(a.dropna(subset=['new_trial_id']).groupby('subject_id').num_images_presented.value_counts().unstack().head(25))
print(b.groupby('subject_id').agg(n=('trial_id','size'),nn=('trial_id_final','count'),mx=('trial_id_final','max')).T)
g=b.groupby('trial_id_final').agg(l=('num_images_presented','nunique'),s=('stimulus_index_enc1','nunique')); print(g.l.value_counts(), g.s.value_counts())
print(b[b.num_images_presented==1].groupby('subject_id').trial_id_final.agg(['count','min','max']))
print(b[b.num_images_presented==1].groupby('trial_id_final').stimulus_index_enc1.agg(lambda x: x.value_counts().to_dict()).head(35))
"
grep -n -i "stimulus_index\|PicID\|RT\b\|'RT'" 01_data_extraction.py | head -40
```

```
subject_id   1    2    3    4    5    6   ...   16   17   18   19   20   21
n            96   96   96   96   96  106  ...   96   96   96  106   96   96
nn           96   96   96   96   96  106  ...   96   96   96  106   96   96
mx          119  119  119  119  119  133  ...  119  119  119  133  119  119

[3 rows x 21 columns]
load consistent across subj per new_trial_id: 1.0 106
num_images_presented   1   2   3
subject_id                      
1                     32  32  32
2                     32  32  32
3                     32  32  32
4                     32  32  32
5                     32  32  32
6                     35  35  36
7                     35  35  36
8                     35  35  36
9                     32  32  32
10                    32  32  32
11                    32  32  32
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hwm; sed -n 40,120p 01_data_extraction.py; sed -n 280,330p 01_data_extraction.py; sed -n 400,460p 01_data_extraction.py; cat 01_task/supp_1a.py 01_task/main_1c.py 01_task/main_1d.py | head -120
```

```
axes[rank].axis('off')  
        image_order[key] = rank
        
    # Hide unused axes
    for ax in axes[len(sorted_keys):]:
        ax.axis('off')
    
    plt.tight_layout()
    plt.show(block=False)   # non-blocking
    plt.pause(2.0)        # lets the GUI render
    plt.close(fig)          # free memory before next subject
    
    return image_order

def map_image_ids_to_encoding_periods(nwbfile, image_order: Dict, file_path: str) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Map image IDs to encoding periods."""
    subject_id = extract_subject_id(file_path)
    stim_pres = nwbfile.stimulus['StimulusPresentation']
    trial_data = nwbfile.intervals['trials']
    
[... 252 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hwm; wc -l */*.py *.py data/cell_analysis/*.m; cat data/cell_analysis/calc_ACG_metrics.m data/cell_analysis/fit_ACG.m data/cell_analysis/Mean_ACG.m data/cell_analysis/normalize_acg_to_unit.m; cat 07_spectral_clustering.py; sed -n 1,80p 02_trial_info.py
```

```
87 01_task/main_1c.py
    22 01_task/main_1d.py
   245 01_task/main_1e,f.py
   131 01_task/main_1g.py
    64 01_task/main_1i,j.py
    37 01_task/supp_1a.py
   403 02_psth_decoding/main_2a,b,5i,j.py
   409 02_psth_decoding/main_2c,5k,l,supp_1b,c.py
   193 02_psth_decoding/main_2d,supp_1d,e.py
   349 02_psth_decoding/main_2e,supp_1f.py
   275 02_psth_decoding/main_2f,supp_1g.py
   106 03_dpca/main_3a-c.py
   246 03_dpca/main_3d,supp_2a,b,i.py
   113 03_dpca/main_3e-g,supp_2j,k.py
   227 03_dpca/main_3h,supp_2c,d,l.py
    74 03_dpca/supp_2e-h.py
   161 04_bursting/main_4a.py
   696 04_bursting/main_4c,d,6a,b.py
    39 04_bursting/main_4e.py
   310 04_bursting/main_4f-k,6c,d.py
[... 536 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hwm; sed -n 1,330p "04_bursting/main_4c,d,6a,b.py"
```

```
import os
import ast
import hashlib
import numpy as np
import pandas as pd
import scipy.signal as signal
from scipy.signal.windows import gaussian

# =========================
# Parameters
# =========================
bin_size = 0.07                    
TRIAL_WIN = 1                       # seconds per trial window; CHANGE TO 2.8 FOR MAINTENANCE
GLOBAL_SEED = 5
sigma_sec = 0.04                    # Gaussian kernel 
prominence_threshold_percentile = 90 # percentile on smoothed rate
min_inter_burst_interval = 0.14     
N_SURROGATES = 100                   # Poisson repetitions per subject
PRINT_DEBUG = True

[... 312 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hwm; sed -n 330,420p "04_bursting/main_4c,d,6a,b.py" | grep -v "^\s*#" | grep -v "plt\.\|ax\." ; sed -n 470,530p "04_bursting/main_4c,d,6a,b.py"; sed -n 1,80p "04_bursting/main_4f-k,6c,d.py"; sed -n 180,310p "04_bursting/main_4f-k,6c,d.py" | grep -v "plt\.\|ax\."
```

```
from statsmodels.stats.multitest import multipletests

out_dir = "./"
os.makedirs(out_dir, exist_ok=True)

def symbol_from_p(p):
    """Hashes for within-category (Real vs Poisson) brackets."""
    if p is None or np.isnan(p): return ""
    if p < 0.005:   return "***"
    if p < 0.01:    return "**"
    if p< 0.05:     return "*"
    return ""

def star_from_p(p):
    """Asterisks for cross-category (Real vs Real) comparisons."""
    if p is None or np.isnan(p): return ""
    if p < 0.001: return "***"
    if p < 0.01:  return "**"
    if p < 0.05:  return "*"
    return ""
[... 325 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hwm; sed -n 1,193p "02_psth_decoding/main_2d,supp_1d,e.py" | grep -v "plt\.\|ax\.\|^\s*#" | head -150
```

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from scipy.stats import binom
import ast
import os
from matplotlib.colors import LinearSegmentedColormap
from scipy.ndimage import label, find_objects

trial_info = pd.read_excel('../data/new_trial_final.xlsx')
subject_trials = trial_info[trial_info['subject_id'] == 14][['trial_id_final', 'num_images_presented', 'stimulus_index_enc1', 'stimulus_index_enc2', 'stimulus_index_enc3', 'response_accuracy']]
print(subject_trials)

y_matrix = subject_trials

df_enc1 = pd.read_excel('../clean_data/cleaned_Encoding1.xlsx')
df_enc2 = pd.read_excel('../clean_data/cleaned_Encoding2.xlsx')
df_enc3 = pd.read_excel('../clean_data/cleaned_Encoding3.xlsx')
df_delay = pd.read_excel('../clean_data/cleaned_Delay.xlsx')
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hwm; sed -n 1,78p 03_standardization.py | grep -v "^\s*#"; sed -n 160,193p "02_psth_decoding/main_2d,supp_1d,e.py"
```

```
import pandas as pd
import ast
import os

BASE_DIR = './'
DATA_DIR = './data/'

filtered_files = {
    'Encoding1': os.path.join(BASE_DIR, 'all_spike_rate_data_encoding1.xlsx'),
    'Encoding2': os.path.join(BASE_DIR, 'all_spike_rate_data_encoding2.xlsx'),
    'Encoding3': os.path.join(BASE_DIR, 'all_spike_rate_data_encoding3.xlsx'),
    'Delay': os.path.join(BASE_DIR, 'all_spike_rate_data_delay.xlsx'),
    'Probe': os.path.join(BASE_DIR, 'all_spike_rate_data_probe.xlsx')
}

def load_enc1_start_times(enc1_path):
    enc1_df = pd.read_excel(enc1_path)
    return enc1_df[['subject_id', 'trial_id', 'start_time']].drop_duplicates().rename(columns={'start_time': 'start_time_enc1'})

enc1_start_times = load_enc1_start_times(filtered_files['Encoding1'])
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hwm; sed -n 265,343p 03_standardization.py
```

```
df_graph['subject_id'].astype(str) + '0' + df_graph['Neuron_ID'].astype(str)
        ).astype(int)
        
        # Remove unnecessary columns (same as cleaned data)
        df_graph = df_graph.drop(columns=columns_to_remove, errors='ignore')
        
        # Determine the spikes column and start time column for this period
        if period_name == 'Encoding1':
            spikes_col = 'Spikes'
            start_time_col = 'start_time'
        elif period_name == 'Encoding2':
            spikes_col = 'Spikes'
            start_time_col = 'start_time'  # Adjust based on actual column name
        elif period_name == 'Encoding3':
            spikes_col = 'Spikes'
            start_time_col = 'start_time'  # Adjust based on actual column name
        elif period_name == 'Delay':
            spikes_col = 'Spikes_in_Delay'
            start_time_col = 'Delay_Start'  # Adjust based on actual column name
        elif period_name == 'Probe':
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/hwm; sed -n 20,140p "02_psth_decoding/main_2f,supp_1g.py" | grep -v "plt\.\|ax\.\|^\s*#"
```

```
Tue Nov 10 05:22:22 UTC 2026




final_neurons = sorted(df_delay_filtered[df_delay_filtered['Signi'] == "Y"]['Neuron_ID_3'].unique())

trial_count = y_matrix.shape[0]
neuron_count = len(final_neurons)

design_matrix = np.empty((trial_count, neuron_count), dtype=object)

def parse_spike_times(spike_str):
    try:
        return ast.literal_eval(spike_str)
    except:
        return []

for trial_idx, row in y_matrix.iterrows():
    trial_id = row['trial_id_final']
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd $TMPDIR; python -c "
import pickle,pandas as pd,numpy as np
S=pickle.load(open('S.pkl','rb'))
a=pd.read_excel('hwm/data/new_trial_info.xlsx'); b=pd.read_excel('hwm/data/new_trial_final.xlsx')
bad=0
for s in S:
    t=s['trials'].copy(); t['trial']=np.arange(1,len(t)+1); t['rt']=t.timestamps_Response-t.timestamps_Probe
    m=b[b.subject_id==s['sub']].merge(t,left_on='trial_id',right_on='trial')
    ok_load=(m.num_images_presented==m.loads).all()
    mp=m.groupby('stimulus_index_enc1').loadsEnc1_PicIDs.nunique().max(); mp2=m.groupby('loadsEnc1_PicIDs').stimulus_index_enc1.nunique().max()
    rt=np.abs(m['RT ']-m.rt).max(); acc=(m.response_accuracy_x==m.response_accuracy_y).all()
    m2=a[a.subject_id==s['sub']].merge(t,left_on='trial_id',right_on='trial')
    print(s['sub'],len(t),ok_load,mp,mp2,round(rt,4),acc,(m2.num_images_presented==m2.loads).all(), round(np.abs(m2.RT-m2.rt).max(),4), sorted(t.loadsEnc1_PicIDs.unique()), t.loads.value_counts().to_dict(), t.trial_id.min())
s1=set(a[a.subject_id==1].new_trial_id)
for k,g in a.groupby('subject_id'): print(k, len(s1-set(g.new_trial_id)), end='; ')
"
```

```
1 135 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {3: 45, 2: 45, 1: 45} 0
2 135 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {3: 45, 2: 45, 1: 45} 0
3 135 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {3: 45, 2: 45, 1: 45} 0
4 135 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {3: 45, 2: 45, 1: 45} 0
5 135 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {3: 45, 2: 45, 1: 45} 0
6 108 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {2: 36, 1: 36, 3: 36} 0
7 108 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {2: 36, 1: 36, 3: 36} 0
8 108 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {2: 36, 1: 36, 3: 36} 0
9 108 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {2: 36, 1: 36, 3: 36} 0
10 135 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {3: 45, 2: 45, 1: 45} 0
11 135 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {3: 45, 2: 45, 1: 45} 0
12 135 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {3: 45, 2: 45, 1: 45} 0
13 135 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {3: 45, 2: 45, 1: 45} 0
14 135 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {3: 45, 2: 45, 1: 45} 0
15 135 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {3: 45, 2: 45, 1: 45} 0
16 108 True 1 1 0.0 True True 0.0 [np.uint8(1), np.uint8(2), np.uint8(3), np.uint8(4), np.uint8(5)] {2: 36, 1: 36, 3: 36} 0
17 135 True 1 1 0.0 True 
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/kussovska-2025/wm.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# Trials and spike counts
# ---------------------------------------------------------------------------------------------

def trial_frame(sess):
    """The trials table with derived columns. trial is the 1-based row number, which is the
    trial_id of the paper's code (01_data_extraction.py:76, trial_id = i + 1). RT is probe onset to
    button press (Methods, Psychophysical task). img1..img3 are the picture ids (1 to 5) of the
    encoding periods; last is the last encoded image (Results, Fig. 2e paragraph)."""
    t = sess["trials"].copy()
    t["trial"] = np.arange(1, len(t) + 1)
    t["sub"] = sess["sub"]
    t["load"] = t["loads"].astype(int)
    t["rt"] = t["timestamps_Response"] - t["timestamps_Probe"]
    t["img1"] = t["loadsEnc1_PicIDs"].astype(int)
    t["img2"] = t["loadsEnc2_PicIDs"].astype(int)
    t["img3"] = t["loadsEnc3_PicIDs"].astype(int)
    t["last"] = np.where(t.load == 1, t.img1, np.where(t.load == 2, t.img2, t.img3))
    t["correct"] = t["response_accuracy"].astype(int)
    t["in_memory"] = t["probe_in_out"].astype(int)
    t["fix_start"] = t["timestamps_FixationCross"]
    t["enc1"] = t["timestamps_Encoding1"]
    t["maint"] = t["timestamps_Maintenance"]
    t["probe"] = t["timestamps_Probe"]
    t["maint_dur"] = t["probe"] - t["maint"]
    return t


def count_in(spikes, starts, ends):
    """Spike counts in [start, end) for each pair of window edges."""
    return np.searchsorted(spikes, ends, side="left") - np.searchsorted(spikes, starts, side="left")


def fixation_stats(spikes, t):
    """Mean and s.d. (ddof 1, as pandas std in the code) over trials of the fixation rate, fixation
    being fixation-cross onset to first encoding onset (Methods, Electrophysiology)."""
    dur = (t.enc1 - t.fix_start).to_numpy()
    r = count_in(spikes, t.fix_start.to_numpy(), t.enc1.to_numpy()) / dur
    return r.mean(), r.std(ddof=1)


def neuron_table(sessions):
    rows = []
    for s in sessions:
        for i, u in s["units"].iterrows():
            rows.append({"sub": s["sub"], "unit": i, "unit_id": int(u.unit_id), "region": u.region,
                         "location": u.location, "n_spikes": int(u.n_spikes)})
    df = pd.DataFrame(rows)
    df["nid"] = np.arange(len(df))
    return df


def spikes_of(sessions_by_sub, row):
    return sessions_by_sub[row["sub"]]["spikes"][row["unit"]]


# ---------------------------------------------------------------------------------------------
# Poisson GLM with one predictor, fitted by Newton's method for many predictor vectors at once
# ---------------------------------------------------------------------------------------------

def poisson_slopes(y, X, n_iter=50):
    """Maximum-likelihood slope of log E[y] = b0 + b1 x for each row of X (shape P x n), with no
    penalty; the same model as sklearn PoissonRegressor(alpha=0) in main_1e,f.py:147. A neuron with
    no spikes has slope 0."""
    y = np.asarray(y, float)
    X = np.atleast_2d(np.asarray(X, float))
    P = X.shape[0]
    if y.sum() == 0:
        return np.zeros(P)
    b0 = np.full(P, np.log(y.mean()))
    b1 = np.zeros(P)
    for _ in range(n_iter):
        eta = np.clip(b0[:, None] + b1[:, None] * X, -30, 30)
        mu = np.exp(eta)
        r = y[None, :] - mu
        g0, g1 = r.sum(1), (r * X).sum(1)
        h00, h01, h11 = mu.sum(1), (mu * X).sum(1), (mu * X * X).sum(1)
        det = h00 * h11 - h01 ** 2
        det = np.where(np.abs(det) < 1e-12, 1e-12, det)
        d0 = (h11 * g0 - h01 * g1) / det
        d1 = (-h01 * g0 + h00 * g1) / det
        step = np.minimum(1.0, 5.0 / np.maximum(np.abs(d1), 1e-12))
        b0 += step * d0
        b1 += step * d1
        if np.max(np.abs(d1)) < 1e-9:
            break
    return b1


def glm_permutation(counts_by_neuron, x_by_neuron, perms_by_neuron, groups, alpha=0.05):
    """Per-neuron significance against its own permutation null, and the count test by group
    (Methods, Generalized linear model encoding analysis; main_1e,f.py:150-205). counts_by_neuron
    and x_by_neuron are lists of per-neuron arrays; perms_by_neuron gives for each neuron an index
    array (n_perm x n_trials) that permutes its predictor. A neuron is significant when |b1| is at
    or above the 95th percentile ('higher' quantile) of its |null|; a group's p is the fraction of
    null counts at or above the observed count."""
    n = len(counts_by_neuron)
    real = np.empty(n)
    null = None
    for j in range(n):
        x = np.asarray(x_by_neuron[j], float)
        xz = (x - x.mean()) / (x.std() + 1e-12)
        real[j] = poisson_slopes(counts_by_neuron[j], xz[None, :])[0]
        nb = poisson_slopes(counts_by_neuron[j], xz[perms_by_neuron[j]])
        if null is None:
            null = np.empty((n, len(nb)))
        null[j] = nb
    absn = np.abs(null)
    thr = np.quantile(absn, 1 - alpha, axis=1, method="higher")
    sig = np.abs(real) >= thr
    sig_null = absn >= thr[:, None]
    out = []
    groups = np.asarray(groups, dtype=object)
    for g in pd.unique(groups):
        idx = np.where(groups == g)[0]
        obs = int(sig[idx].sum())
        nc = sig_null[idx].sum(0)
        out.append({"group": g, "n": len(idx), "significant": obs, "percent": 100 * obs / len(idx),
                    "null_mean": nc.mean(), "p": float(np.mean(nc >= obs))})
    return pd.DataFrame(out), sig


# ---------------------------------------------------------------------------------------------
# Concept cells (Methods, Identification of concept cells; 04_concept_cells.py)
# ---------------------------------------------------------------------------------------------

def concept_test(rates, imgs, rng, n_boot=1000, reading="methods"):
    """rates: per-trial rate 200 to 1000 ms after first-encoding onset; imgs: first image per
    trial. Returns (preferred image, p, significant). Top two images by mean rate; bootstrap of the
    difference of means. reading 'methods' resamples each image's trials to its own number and
    takes p = 2 min(P(d > 0), P(d < 0)); reading 'code' resamples both to the smaller number and
    takes the minimum of the four terms at 04_concept_cells.py:86-90."""
    ims = np.unique(imgs)
    means = np.array([rates[imgs == i].mean() for i in ims])
    order = np.argsort(-means, kind="stable")
    i1, i2 = ims[order[0]], ims[order[1]]
    a, b = rates[imgs == i1], rates[imgs == i2]
    if reading == "methods":
        sa = a[rng.integers(0, len(a), (n_boot, len(a)))].mean(1)
        sb = b[rng.integers(0, len(b), (n_boot, len(b)))].mean(1)
        d = sa - sb
        p = min(1.0, 2 * min(np.mean(d > 0), np.mean(d < 0)))
    else:
        m = min(len(a), len(b))
        d = a[rng.integers(0, len(a), (n_boot, m))].mean(1) - b[rng.integers(0, len(b), (n_boot, m))].mean(1)
        m1 = 2 * np.sum(d > 0) / n_boot
        m2 = 1 - np.sum(d < 0) / n_boot
        m3 = 2 * np.sum(d < 0) / n_boot
        m4 = 1 - np.sum(d > 0) / n_boot
        p = min(m1, m2, m3, m4)
    sig = (p < 0.05) and len(a) > 1 and len(b) > 1 and means[order[0]] > 0
    return int(i1), float(p), bool(sig)


# ---------------------------------------------------------------------------------------------
# Linear SVM decoding with leave-one-out cross-validation
# ---------------------------------------------------------------------------------------------

def loo_correct(K, y):
    """Leave-one-out correctness of a linear SVM (sklearn SVC, linear kernel, C = 1, as in the
    code) from the precomputed linear kernel K = X X^T, which gives the same fits as
    SVC(kernel='linear') on X."""
    from sklearn.svm import SVC
    n = len(y)
    out = np.zeros(n, bool)
    idx = np.arange(n)
    for i in range(n):
        tr = idx != i
        if len(np.unique(y[tr])) < 2:
            continue
        clf = SVC(kernel="precomputed", C=1.0).fit(K[np.ix_(tr, tr)], y[tr])
        out[i] = clf.predict(K[i, tr][None, :])[0] == y[i]
    return out


def loo_cross_temporal(X, y):
    """Cross-temporal LOOCV accuracy matrix (train bin x test bin). X: trials x neurons x bins."""
    from sklearn.svm import SVC
    n, _, nb = X.shape
    G = np.einsum("inb,jnc->bcij", X, X)  # G[b, c] = X[:, :, b] @ X[:, :, c].T
    acc = np.zeros((nb, nb))
    idx = np.arange(n)
    for b in range(nb):
        Kb = G[b, b]
        for i in range(n):
            tr = idx != i
            clf = SVC(kernel="precomputed", C=1.0).fit(Kb[np.ix_(tr, tr)], y[tr])
            # test trial i at every bin c against training trials at bin b: G[c, b][i, tr]
            kt = G[:, b][:, i, :][:, tr]
            acc[b] += clf.predict(kt) == y[i]
    return acc / n


# ---------------------------------------------------------------------------------------------
# Autocorrelograms and the CellExplorer fit (data/cell_analysis/*.m of the paper's code)
# ---------------------------------------------------------------------------------------------

def acg(spikes, bin_size, n_bins):
    """calc_ACG_metrics.m autocorrelogram: lags rounded to bins, |bin| <= n_bins // 2, self pairs
    removed, divided by spike count and bin width."""
    half = n_bins // 2
    maxlag = (half + 0.5) * bin_size
    out = np.zeros(n_bins)
    s = np.asarray(spikes, float)
    n = len(s)
    if n < 2:
        return np.full(n_bins, np.nan)
    k = 1
    while k < n:
        d = s[k:] - s[:-k]
        d = d[d <= maxlag]
        if d.size == 0:
            break
        b = np.round(d / bin_size).astype(int)
        b = b[b <= half]
        np.add.at(out, half + b, 1)
        np.add.at(out, half - b, 1)
        k += 1
    return out / (n * bin_size)


def _acg_model(p, x):
    a, b, c, d, e, f, g, h = p
    return np.maximum(c * (np.exp(-(x - f) / a) - d * np.exp(-(x - f) / b)) + h * np.exp(-(x - f) / g) + e, 0)


def fit_acg(acg_narrow):
    """fit_ACG.m of CellExplorer: bins -0.5 to +0.5 ms set to zero, the triple exponential fitted at
    lags 0.5 to 50 ms from the start point a0 within bounds lb, ub, by bounded nonlinear least
    squares (scipy's trust-region reflective, as MATLAB's fit uses). Returns tau_decay, tau_rise,
    R2 and the parameters."""
    from scipy.optimize import least_squares
    y_all = np.array(acg_narrow, float)
    y_all[99:102] = 0
    x = np.arange(1, 101) / 2
    y = y_all[(x * 2).astype(int) + 100]
    a0 = np.array([20, 1, 30, 2, 0.5, 5, 1.5, 2], float)
    lb = np.array([1, 0.1, 0, 0, -30, 0, 0.1, 0], float)
    ub = np.array([500, 50, 500, 15, 50, 20, 5, 100], float)
    if not np.all(np.isfinite(y)):
        return dict(tau_decay=np.nan, tau_rise=np.nan, r2=np.nan)
    res = least_squares(lambda p: _acg_model(p, x) - y, a0, bounds=(lb, ub), method="trf",
                        max_nfev=2000)
    sse = np.sum(res.fun ** 2)
    sst = np.sum((y - y.mean()) ** 2)
    r2 = 1 - sse / sst if sst > 0 else np.nan
    return dict(tau_decay=res.x[0], tau_rise=res.x[1], r2=r2, params=res.x)


def acg_features(spikes):
    """Features of one neuron: narrow and wide ACG, the fit, the mean of the max-normalised wide
    ACG with the zero-lag bin set to 0 (Mean_ACG.m, normalize_acg_to_unit.m), the Royer burst
    index mean(wide[+2..+4 ms]) / mean(wide[+199..+299 ms]) (calc_ACG_metrics.m:45), the firing
    rate as count over first-to-last spike (02_trial_info.py:37-40), the ISI CV (std/mean,
    02_trial_info.py:42-46) and Holt's CV2 (mean of 2|I(n+1) - I(n)| / (I(n+1) + I(n)))."""
    s = np.asarray(spikes, float)
    nar = acg(s, 0.0005, 201)
    wide = acg(s, 0.001, 1001)
    fit = fit_acg(nar)
    w = wide.copy()
    mx = np.nanmax(w) if np.any(np.isfinite(w)) else np.nan
    wn = w / mx if mx and mx > 0 else np.full_like(w, np.nan)
    wn[500] = 0
    isi = np.diff(s)
    cv2 = np.mean(2 * np.abs(isi[1:] - isi[:-1]) / (isi[1:] + isi[:-1])) if len(isi) > 1 else np.nan
    return {"tau_decay": fit["tau_decay"], "tau_rise": fit["tau_rise"], "r2": fit["r2"],
            "acg_norm": np.nanmean(wn), "burst_royer": np.mean(wide[502:505]) / np.mean(wide[699:800]),
            "firing_rate": len(s) / (s[-1] - s[0]) if len(s) > 1 else np.nan,
            "cv_isi": np.std(isi) / np.mean(isi) if len(isi) > 1 else np.nan, "cv2_holt": cv2}


def cv2_holt(isi):
    isi = np.asarray(isi, float)
    if len(isi) < 2:
        return np.nan
    return np.mean(2 * np.abs(isi[1:] - isi[:-1]) / (isi[1:] + isi[:-1]))


# ---------------------------------------------------------------------------------------------
# Population bursts (Methods, Burst detection; 04_bursting/main_4c,d,6a,b.py)
# ---------------------------------------------------------------------------------------------
BURST_BIN = 0.07      # s, Methods and code line 12
BURST_SIGMA = 0.04    # s, Methods and code line 15
BURST_PCT = 90        # percentile, Methods and code line 16


def smooth_counts(spike_times, total_dur, bin_size=BURST_BIN, sigma=BURST_SIGMA):
    from scipy.signal.windows import gaussian
    edges = np.arange(0.0, total_dur + bin_size, bin_size)
    c, _ = np.histogram(spike_times, bins=edges)
    k = gaussian(len(c), std=sigma / bin_size)
    k = k / k.sum()
    return np.convolve(c, k, mode="same")


def burst_peaks(sm, threshold, rule="prominence", distance=2):
    """Peaks of the smoothed population count. rule 'prominence': prominence at or above the
    threshold (the code, lines 251-255, and the Results); rule 'height': local peaks whose smoothed
    value exceeds the threshold (Methods). distance in bins (2 bins = 140 ms, Methods and code)."""
    import scipy.signal as signal
    kw = {"distance": distance} if distance and distance > 1 else {}
    if rule == "prominence":
        pk, _ = signal.find_peaks(sm, prominence=threshold, **kw)
    else:
        pk, _ = signal.find_peaks(sm, height=np.nextafter(threshold, np.inf), **kw)
    return pk


def concat_trials(spike_lists, win):
    """Concatenate per-trial relative spike times (each in [0, win]) into one train."""
    parts = [np.asarray(s) + i * win for i, s in enumerate(spike_lists) if len(s)]
    return np.concatenate(parts) if parts else np.array([])
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; cat > $TMPDIR/dev1.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import wm
S=pickle.load(open(sys.argv[1],'rb'))
for s in S:
    s['units']['region']=s['units'].location.map(wm.region_of)
by={s['sub']:s for s in S}
NT=wm.neuron_table(S); print(NT.region.value_counts())
T={s['sub']:wm.trial_frame(s) for s in S}
t0=time.time()
feats=[]
for _,r in NT.iterrows():
    feats.append(wm.acg_features(wm.spikes_of(by,r)))
F=pd.DataFrame(feats); print('acg time',time.time()-t0)
cm=pd.read_excel('/tmp/claude-1001/hwm/data/cell_analysis/Cell_metrics.xlsx') if False else pd.read_excel(sys.argv[2])
print((F.r2>0.3).sum(), (F.r2>=0.3).sum(), (cm.R2>0.3).sum())
both=pd.concat([F.reset_index(drop=True),cm.reset_index(drop=True)],axis=1)
for a,b in [('r2','R2'),('tau_rise','tau_rise'),('tau_decay','Decay'),('acg_norm','acg_norm'),('firing_rate','firing_rate'),('cv_isi','CV2'),('burst_royer','Burst')]:
    print(a, np.corrcoef(both[a].fillna(0),both[b].fillna(0))[0,1], np.nanmedian(np.abs(both[a]-both[b])), both[[a,b]].head(3).values.tolist())
F.to_pickle('/tmp/claude-1001/F.pkl') if False else F.to_pickle(sys.argv[3])
EOF
python $TMPDIR/dev1.py $TMPDIR/S.pkl $TMPDIR/hwm/data/cell_analysis/Cell_metrics.xlsx $TMPDIR/F.pkl
```

```
entries/kussovska-2025/wm.py:374: RuntimeWarning: invalid value encountered in scalar divide
  "acg_norm": np.nanmean(wn), "burst_royer": np.mean(wide[502:505]) / np.mean(wide[699:800]),
/tmp/claude-1001/dev/lib/python3.12/site-packages/numpy/lib/_function_base_impl.py:3037: RuntimeWarning: invalid value encountered in divide
  c /= stddev[:, None]
/tmp/claude-1001/dev/lib/python3.12/site-packages/numpy/lib/_function_base_impl.py:3038: RuntimeWarning: invalid value encountered in divide
  c /= stddev[None, :]
region
AMY       259
preSMA    250
HPC       190
dACC      171
vmPFC      32
Name: count, dtype: int64
acg time 78.79443740844727
317 317 294
r2 0.93762940064314 0.0019532967146392716 [[0.0445751791983523, 0.0446503412421719], [0.14882192848240705, 0.148131604329727], [0.18607001955320046, -0.209731308602398]]
tau_rise 1.0 0.0 [[6.141616704159533, 4.78086684992691, 6.141616704159533, 4.78086684992691], [49.99999999999999, 45.1401979828698, 49.99999999999999, 45.1401979828698], [0.23079461902356516, 6.91589622728242, 0.23079461902356516, 6.91589622728242]]
tau_decay 0.5315877605081069 3.224073899739744 [[6.368231534825323, 6.18398494917623], [49.43459710318965, 39.8535281923769], [1.0000000000000002, 9.86121039138803]]
acg_norm 0.9977851578566088 0.0 [[0.23856143856143858, 0.238561438561439, 0.23856143856143858, 0.238561438561439], [0.38278388278388276, 0.382783882783883, 0.38278388278388276, 0.382783882783883], [0.2863802863802864, 0.286380286380286, 0.2863802863802864, 0.286380286380286]]
firing_rate nan 0.0 [[0.9854902410353745, 0.9854902410353745, 0.9854902410353745, 0.9854902410353745], [1.2078427049315763, 1.207842704931576, 1.2078427049315763, 1.207842704931576], [1.4658969345485564, 1.465896934548556, 1.4658969345485564, 1.465896934548556]]
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; cat > $TMPDIR/dev2.py <<'EOF'
import pickle, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import wm
from scipy.optimize import least_squares
S=pickle.load(open(sys.argv[1],'rb'))
by={s['sub']:s for s in S}
NT=wm.neuron_table(S)
cm=pd.read_excel(sys.argv[2])
x = np.arange(1, 101) / 2
a0 = np.array([20, 1, 30, 2, 0.5, 5, 1.5, 2], float)
lb = np.array([1, 0.1, 0, 0, -30, 0, 0.1, 0], float); ub = np.array([500, 50, 500, 15, 50, 20, 5, 100], float)
idx=range(0,902,6)
Y=[]
for i in idx:
    n=wm.acg(wm.spikes_of(by,NT.iloc[i]),0.0005,201); n[99:102]=0; Y.append(n[(x*2).astype(int)+100])
for name,kw in [('default',dict(max_nfev=2000)),('matlab',dict(max_nfev=600,ftol=1e-6,xtol=1e-6,gtol=1e-8)),('jac3',dict(max_nfev=600,ftol=1e-6,xtol=1e-6,diff_step=1e-8)),('dogbox',dict(method='dogbox',max_nfev=600,ftol=1e-6,xtol=1e-6))]:
    r2=[];td=[]
    for y in Y:
        kw2=dict(kw); m=kw2.pop('method','trf')
        res=least_squares(lambda p: wm._acg_model(p,x)-y,a0,bounds=(lb,ub),method=m,**kw2)
        r2.append(1-np.sum(res.fun**2)/np.sum((y-y.mean())**2)); td.append(res.x[0])
    r2=np.array(r2); ref=cm.R2.values[list(idx)]; tref=cm.Decay.values[list(idx)]
    print(name, np.mean(np.abs(r2-ref)<0.01), np.mean(np.abs(np.array(td)-tref)<0.5), (r2>0.3).sum(), (ref>0.3).sum())
EOF
python $TMPDIR/dev2.py $TMPDIR/S.pkl $TMPDIR/hwm/data/cell_analysis/Cell_metrics.xlsx
```

```
/bin/bash: line 1: cd: entries/kussovska-2025: No such file or directory
/tmp/claude-1001/dev2.py:21: RuntimeWarning: invalid value encountered in scalar divide
  r2.append(1-np.sum(res.fun**2)/np.sum((y-y.mean())**2)); td.append(res.x[0])
default 0.695364238410596 0.2781456953642384 50 45
matlab 0.7019867549668874 0.304635761589404 50 45
jac3 0.7086092715231788 0.31125827814569534 50 45
dogbox 0.23841059602649006 0.026490066225165563 31 45
```

**Agent calls Bash**

```bash
date -u; source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; cat > $TMPDIR/dev3.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import wm
S=pickle.load(open(sys.argv[1],'rb'))
by={s['sub']:s for s in S}
NT=wm.neuron_table(S)
T={s['sub']:wm.trial_frame(s) for s in S}
# concept cells
t0=time.time()
res={}
for reading in ['methods','code']:
    for seed in range(10):
        rng=np.random.default_rng(seed)
        cc=[]
        for _,r in NT.iterrows():
            t=T[r['sub']]; sp=wm.spikes_of(by,r)
            rates=wm.count_in(sp,(t.enc1+0.2).values,(t.enc1+1.0).values)/0.8
            cc.append(wm.concept_test(rates,t.img1.values,rng,reading=reading))
        cc=pd.DataFrame(cc,columns=['pref','p','sig'])
        res[(reading,seed)]=cc
        print(reading,seed,cc.sig.sum(), NT[cc.sig.values].region.value_counts().to_dict())
print(time.time()-t0)
pickle.dump(res,open(sys.argv[2],'wb'))
EOF
python $TMPDIR/dev3.py $TMPDIR/S.pkl $TMPDIR/CC.pkl
```

```
Tue Nov 10 05:26:05 UTC 2026
methods 0 50 {'amygdala_right': 30, 'amygdala_left': 7, 'hippocampus_left': 6, 'hippocampus_right': 3, 'ventral_medial_prefrontal_cortex_right': 2, 'pre_supplementary_motor_area_left': 1, 'dorsal_anterior_cingulate_cortex_left': 1}
methods 1 51 {'amygdala_right': 30, 'amygdala_left': 7, 'hippocampus_left': 6, 'hippocampus_right': 3, 'ventral_medial_prefrontal_cortex_right': 2, 'ventral_medial_prefrontal_cortex_left': 1, 'pre_supplementary_motor_area_left': 1, 'dorsal_anterior_cingulate_cortex_left': 1}
methods 2 51 {'amygdala_right': 29, 'amygdala_left': 7, 'hippocampus_left': 7, 'hippocampus_right': 3, 'pre_supplementary_motor_area_left': 2, 'ventral_medial_prefrontal_cortex_right': 2, 'dorsal_anterior_cingulate_cortex_left': 1}
methods 3 50 {'amygdala_right': 29, 'hippocampus_left': 7, 'amygdala_left': 6, 'hippocampus_right': 3, 'ventral_medial_prefrontal_cortex_right': 2, 'ventral_medial_prefrontal_cortex_left': 1, 'pre_supplementary_motor_area_left': 1, 'dorsal_anterior_cingulate_cortex_left': 1}
methods 4 49 {'amygdala_right': 28, 'amygdala_left': 8, 'hippocampus_left': 6, 'hippocampus_right': 3, 'ventral_medial_prefrontal_cortex_right': 2, 'pre_supplementary_motor_area_left': 1, 'dorsal_anterior_cingulate_cortex_left': 1}
methods 5 50 {'amygdala_right': 29, 'amygdala_left': 8, 'hippocampus_left': 6, 'hippocampus_right': 3, 'ventral_medial_prefrontal_cortex_right': 2, 'pre_supplementary_motor_area_left': 1, 'dorsal_anterior_cingulate_cortex_left': 1}
methods 6 51 {'amygdala_right': 30, 'amygdala_left': 8, 'hippocampus_left': 6, 'hippocampus_right': 3, 'ventral_medial_prefrontal_cortex_right': 2, 'pre_supplementary_motor_area_left': 1, 'dorsal_anterior_cingulate_cortex_left': 1}
methods 7 52 {'amygdala_right': 30, 'amygdala_left': 8, 'hippocampus_left': 6, 'hippocampus_right': 3, 'ventral_medial_prefrontal_cortex_right': 2, 'ventral_medial_prefrontal_cortex_left': 1, 'pre_supplementary_motor_area_left': 1, 'dorsal_anterior_cingulate_
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; python -c "
import pickle,pandas as pd,numpy as np,sys
sys.path.insert(0,'.'); import wm
S=pickle.load(open('$TMPDIR/S.pkl','rb')); NT=wm.neuron_table(S)
CC=pickle.load(open('$TMPDIR/CC.pkl','rb'))
sh=pd.read_excel('$TMPDIR/hwm/data/all_neuron_brain_regions_cleaned.xlsx')
print((sh.subject_id.values==NT['sub'].values).all(), (sh.Neuron_ID.values==NT.unit.values).all(), (sh.Location.values==NT.location.values).all())
ref=(sh.Signi=='Y').values; print('shipped',ref.sum())
M=np.array([CC[('code',s)].sig.values for s in range(10)]); maj=M.mean(0)>=0.5
for s in range(10): print(s,(M[s]&ref).sum(), M[s].sum())
print('maj',maj.sum(),(maj&ref).sum())
print(NT[ref].groupby('sub').size().describe())
"
```

```
True True True
shipped 58
0 57 58
1 57 58
2 58 58
3 57 58
4 58 59
5 56 57
6 57 57
7 58 60
8 57 59
9 57 58
maj 60 58
count    14.000000
mean      4.142857
std       3.697341
min       1.000000
25%       1.250000
50%       3.000000
75%       4.750000
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; cat > $TMPDIR/dev4.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import wm
S=pickle.load(open(sys.argv[1],'rb'))
for s in S: s['units']['region']=s['units'].location.map(wm.region_of)
by={s['sub']:s for s in S}
NT=wm.neuron_table(S)
T={s['sub']:wm.trial_frame(s) for s in S}
info=pd.read_excel(sys.argv[2])
ids1=info[info.subject_id==1].sort_values('new_trial_id').new_trial_id.values
def counts(sub, sp, rows):
    t=T[sub].set_index('trial').loc[rows]
    return wm.count_in(sp, t.maint.values, t.maint.values+2.5)
NP=1000
t0=time.time()
def run(pred, trials, perm):
    rng=np.random.default_rng(17)
    Y=[];X=[];P=[]
    if trials=='matched':
        shared=np.array([rng.permutation(len(ids1)) for _ in range(NP)])
    subperm={}
    for _,r in NT.iterrows():
        sub=r['sub']; t=T[sub]
        if trials=='matched':
            m=info[info.subject_id==sub].set_index('new_trial_id').loc[ids1,'trial_id'].values
        else:
            m=t.trial.values
        y=counts(sub, wm.spikes_of(by,r), m)
        if pred=='rt_code':
            x=info[info.subject_id==1].set_index('new_trial_id').loc[ids1,'RT'].values
        else:
            x=t.set_index('trial').loc[m, 'load' if pred=='load' else 'rt'].values
        if perm=='shared': pp=shared
        else:
            if sub not in subperm: subperm[sub]=np.array([rng.permutation(len(m)) for _ in range(NP)])
            pp=subperm[sub]
        Y.append(y);X.append(x);P.append(pp)
    return wm.glm_permutation(Y,X,P,NT.region.values)
out={}
for pred in ['load','rt','rt_code']:
    for trials,perm in [('matched','shared'),('matched','within'),('all','within')]:
        if pred=='rt_code' and trials=='all': continue
        df,sig=run(pred,trials,perm); out[(pred,trials,perm)]=(df,sig)
        print(pred,trials,perm, round(time.time()-t0)); print(df.round(3).to_string())
pickle.dump(out,open(sys.argv[3],'wb'))
EOF
timeout 3000 python $TMPDIR/dev4.py $TMPDIR/S.pkl $TMPDIR/hwm/data/new_trial_info.xlsx $TMPDIR/GLM.pkl
```

```
load matched shared 5
    group    n  significant  percent  null_mean      p
0    dACC  171           18   10.526      8.719  0.025
1  preSMA  250           51   20.400     12.768  0.000
2     AMY  259           14    5.405     13.350  0.459
3     HPC  190            9    4.737      9.696  0.594
4   vmPFC   32            6   18.750      1.643  0.009
load matched within 8
    group    n  significant  percent  null_mean      p
0    dACC  171           17    9.942      8.710  0.018
1  preSMA  250           48   19.200     12.749  0.000
2     AMY  259           15    5.792     13.328  0.357
3     HPC  190           10    5.263      9.697  0.495
4   vmPFC   32            6   18.750      1.620  0.007
load all within 11
    group    n  significant  percent  null_mean      p
0    dACC  171           21   12.281      8.661  0.003
1  preSMA  250           56   22.400     12.671  0.000
2     AMY  259           16    6.178     13.262  0.266
3     HPC  190           13    6.842      9.657  0.193
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hwm; sed -n 420,470p "04_bursting/main_4c,d,6a,b.py" | grep -v "plt\.\|ax\."
```

```
# WITHIN-CATEGORY: Real vs Poisson (paired by subject) + FDR-BH (Family A)

stats_within = {cat: {} for cat in categories}
raw_pvals_within, cats_with_within = [], []
all_diffs_for_condition_omnibus = []  # y - x (Poisson - Real) to test Condition effect

for cat in categories:
    cd = results_delay[cat]
    real_map = get_map(cd, "real_by_subj")
    pois_map = get_map(cd, "poisson_by_subj")

    pval = np.nan
    stat = np.nan
    n_pairs = 0
    test_name = "NA"

    if real_map is not None and pois_map is not None:
        common = sorted(set(real_map) & set(pois_map))
        if len(common) >= 2:
            x = np.array([real_map[s] for s in common], float)
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; cat >> wm.py <<'EOF'


def spectral_types(features, random_state=42):
    """Spectral clustering on standardised firing rate, normalised mean ACG and tau_rise
    (07_spectral_clustering.py: StandardScaler, SpectralClustering(n_clusters=2,
    affinity='nearest_neighbors', random_state=42)). The cluster with the higher median firing
    rate is labelled IN (Results, Feature-based classification, paragraph 3)."""
    from sklearn.cluster import SpectralClustering
    from sklearn.preprocessing import StandardScaler
    X = StandardScaler().fit_transform(features[["firing_rate", "acg_norm", "tau_rise"]].values)
    lab = SpectralClustering(n_clusters=2, affinity="nearest_neighbors",
                             random_state=random_state).fit_predict(X)
    fr = features["firing_rate"].values
    in_label = 0 if np.median(fr[lab == 0]) > np.median(fr[lab == 1]) else 1
    return np.where(lab == in_label, "IN", "PY"), lab
EOF
python - <<EOF
import sys, pandas as pd, numpy as np, pickle
sys.path.insert(0,'.'); import wm
F=pd.read_pickle('$TMPDIR/F.pkl')
cm=pd.read_excel('$TMPDIR/hwm/data/cell_analysis/Cell_metrics.xlsx')
for name,df,col in [('dataset >0.3',F[F.r2>0.3],None),('shipped >=0.3',cm[cm.R2>=0.3].rename(columns={'tau_rise':'tau_rise'}),None)]:
    d=df.dropna(subset=['firing_rate','acg_norm','tau_rise'])
    ty,lab=wm.spectral_types(d)
    print(name,len(d),pd.Series(ty).value_counts().to_dict(), 'raw label1 count',(lab==1).sum())
    for f in ['firing_rate','acg_norm','tau_rise']:
        print('  ',f, d[f][ty=='PY'].median(), d[f][ty=='IN'].median())
EOF
```

```
dataset >0.3 317 {'IN': 215, 'PY': 102} raw label1 count 102
   firing_rate 1.2721051240233998 5.261301175391954
   acg_norm 0.11181675467389753 0.5877199723353568
   tau_rise 1.1804792442686796 4.389419481357195
shipped >=0.3 294 {'IN': 202, 'PY': 92} raw label1 count 92
   firing_rate 1.403554175265592 5.36373550265632
   acg_norm 0.13209910656719198 0.5907022389375329
   tau_rise 1.3211864259028299 4.518452838439055
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; python - <<EOF
import sys, pandas as pd, numpy as np, pickle, time
sys.path.insert(0,'.'); import wm
S=pickle.load(open('$TMPDIR/S.pkl','rb')); by={s['sub']:s for s in S}
NT=wm.neuron_table(S); T={s['sub']:wm.trial_frame(s) for s in S}
t0=time.time(); rows=[]
for _,r in NT.iterrows():
    sp=wm.spikes_of(by,r); t=T[r['sub']]
    keep=np.zeros(len(sp),bool)
    for a,b in zip(t.fix_start.values,t.timestamps_Response.values):
        i,j=np.searchsorted(sp,[a,b]); keep[i:j]=True
    f=wm.acg_features(sp[keep]); f['firing_rate']=wm.acg_features(sp)['firing_rate'] if False else len(sp)/(sp[-1]-sp[0]); rows.append(f)
F2=pd.DataFrame(rows); F2.to_pickle('$TMPDIR/F2.pkl'); print(time.time()-t0)
print((F2.r2>0.3).sum())
d=F2[F2.r2>0.3].dropna(subset=['firing_rate','acg_norm','tau_rise']); ty,lab=wm.spectral_types(d); print(pd.Series(ty).value_counts())
EOF
```

```
entries/kussovska-2025/wm.py:374: RuntimeWarning: invalid value encountered in scalar divide
  "acg_norm": np.nanmean(wn), "burst_royer": np.mean(wide[502:505]) / np.mean(wide[699:800]),
67.48560547828674
298
IN    198
PY    100
Name: count, dtype: int64
```

**Agent calls Bash**

```bash
date -u; cd entries/kussovska-2025; cat >> wm.py <<'EOF'


def epoch_spikes(spikes, starts, ends, win):
    """Per-trial spike times relative to each start, within [start, end) and clipped to [0, win]
    (the code's parse_spike_entry keeps 0 <= t <= TRIAL_WIN)."""
    out = []
    for a, b in zip(starts, ends):
        i, j = np.searchsorted(spikes, [a, b])
        r = spikes[i:j] - a
        out.append(r[(r >= 0) & (r <= win)])
    return out


def group_bursts(neuron_trials, win, rng, rule="prominence", distance=2, thr_mode="real",
                 n_sur=100):
    """Population bursts of one group of one participant. neuron_trials: per neuron, the list of
    its per-trial relative spike times (same trials for all neurons). The group's spikes are pooled,
    trials concatenated with stride win, binned at 70 ms, smoothed (Gaussian, sigma 40 ms), and
    peaks found against the 90th percentile of the smoothed train. Surrogates: per neuron and trial a
    Poisson count with the trial's count as its mean, spike times uniform in the window (code lines
    272-306; Methods). thr_mode 'real' uses the real train's threshold for the surrogates (code),
    'own' each surrogate's own. Returns (real count, mean surrogate count, peak bins, n bins)."""
    n_tr = len(neuron_trials[0])
    pooled = np.concatenate([concat_trials(nt, win) for nt in neuron_trials]) if neuron_trials else np.array([])
    total = n_tr * win
    sm = smooth_counts(pooled, total)
    thr = np.percentile(sm, BURST_PCT)
    pk = burst_peaks(sm, thr, rule, distance)
    counts = np.array([[len(s) for s in nt] for nt in neuron_trials])  # neurons x trials
    sur = []
    offs = np.arange(n_tr) * win
    for _ in range(n_sur):
        n = rng.poisson(counts)
        tot = n.sum()
        if tot == 0:
            sur.append(0)
            continue
        tr_idx = np.repeat(np.tile(np.arange(n_tr), counts.shape[0]), n.ravel())
        st = rng.uniform(0, win, tot) + offs[tr_idx]
        s2 = smooth_counts(st, total)
        th = thr if thr_mode == "real" else np.percentile(s2, BURST_PCT)
        sur.append(len(burst_peaks(s2, th, rule, distance)))
    return len(pk), float(np.mean(sur)), pk, len(sm)
EOF
echo
```

```
Tue Nov 10 05:29:27 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; python - <<'EOF'
s=open('wm.py').read()
old='''    edges = np.arange(0.0, total_dur + bin_size, bin_size)
    c, _ = np.histogram(spike_times, bins=edges)
    k = gaussian(len(c), std=sigma / bin_size)
    k = k / k.sum()
    return np.convolve(c, k, mode="same")'''
new='''    edges = np.arange(0.0, total_dur + bin_size, bin_size)
    c, _ = np.histogram(spike_times, bins=edges)
    # The code's kernel is gaussian(len(counts)) normalised to sum 1 (line 245); its weights beyond
    # 12 bins (sigma is 0.57 bins) are below 1e-90, so it is cut there, keeping its parity and
    # hence its half-bin offset when the length is even. This changes no value above 1e-80.
    M = len(c)
    full = gaussian(M, std=sigma / bin_size)
    full = full / full.sum()
    K = 12
    if M > 2 * K + 2:
        lo = (M - 1) // 2 - K if M % 2 else M // 2 - K
        hi = (M - 1) // 2 + K + 1 if M % 2 else M // 2 + K
        k = full[lo:hi]
    else:
        k = full
    return np.convolve(c, k, mode="same")'''
assert old in s; s=s.replace(old,new); open('wm.py','w').write(s)
EOF
source $TMPDIR/dev/bin/activate; python - <<'EOF'
import sys; sys.path.insert(0,'.'); import wm, numpy as np
from scipy.signal.windows import gaussian
rng=np.random.default_rng(0)
for dur in [33*1.0, 32*2.8, 31*2.8]:
    st=np.sort(rng.uniform(0,dur,500))
    a=wm.smooth_counts(st,dur)
    edges=np.arange(0.0,dur+0.07,0.07); c,_=np.histogram(st,bins=edges); k=gaussian(len(c),std=0.04/0.07); k/=k.sum(); b=np.convolve(c,k,mode='same')
    print(len(c), np.abs(a-b).max())
EOF
```

```
472 4.440892098500626e-16
1280 2.220446049250313e-16
1240 2.220446049250313e-16
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; cat >> wm.py <<'EOF'


def burst_groups(NT, feats, concept, types, rule="code"):
    """Neuron groups per participant for the burst analyses. NT: neuron table; feats: ACG features
    (index aligned with NT); concept: boolean array; types: array of 'PY', 'IN' or None.
    rule 'methods': median split within participant of the well-fit neurons (R2 > 0.3) on
    normalised mean ACG and on tau_decay, the lower and upper halves (floor(n/2) each), participants
    with fewer than 5 neurons in a group left out (Methods, Burst detection); rule 'code': the 6
    lowest and 6 highest of participants with at least 10 well-fit neurons (main_4c,d,6a,b.py:52,
    95-120, 164-172). All cells: every neuron of participants with at least 10 neurons (code line
    183-185, 'All902'), or the well-fit neurons ('AllFit') with the same rule. Concept cells: at
    least 3 per participant (code) or 5 (Methods). PY and IN: at least 3 (Methods, Putative
    cell-type classification; code lines 178-181). Returns {group: {sub: [nid, ...]}}."""
    fit = feats["r2"].values > 0.3
    out = {g: {} for g in ["All902", "AllFit", "LowACG", "HighACG", "ShortDecay", "LongDecay",
                           "Concept", "PY", "IN"]}
    for sub, g in NT.groupby("sub"):
        nids = g.nid.values
        if len(nids) >= 10:
            out["All902"][sub] = list(nids)
        f = nids[fit[nids]]
        if len(f) >= 10:
            out["AllFit"][sub] = list(f)
        for feat, lo, hi in [("acg_norm", "LowACG", "HighACG"), ("tau_decay", "ShortDecay", "LongDecay")]:
            v = feats[feat].values[f]
            ok = np.isfinite(v)
            ff, v = f[ok], v[ok]
            order = np.lexsort((ff, v))  # stable, ties by neuron id as in the code
            if rule == "code":
                if len(ff) >= 10:
                    out[lo][sub] = list(ff[order[:6]])
                    out[hi][sub] = list(ff[order[-6:]])
            else:
                m = len(ff) // 2
                if m >= 5:
                    out[lo][sub] = list(ff[order[:m]])
                    out[hi][sub] = list(ff[order[-m:]])
        c = nids[concept[nids]]
        if len(c) >= (3 if rule == "code" else 5):
            out["Concept"][sub] = list(c)
        for ty in ["PY", "IN"]:
            t = nids[np.asarray(types, dtype=object)[nids] == ty]
            if len(t) >= 3:
                out[ty][sub] = list(t)
    return out
EOF
cat > $TMPDIR/dev5.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, sys, itertools
sys.path.insert(0,'.')
import wm
from scipy.stats import wilcoxon
from statsmodels.stats.multitest import multipletests
S=pickle.load(open(sys.argv[1],'rb')); by={s['sub']:s for s in S}
NT=wm.neuron_table(S); T={s['sub']:wm.trial_frame(s) for s in S}
F=pd.read_pickle(sys.argv[2]); CC=pickle.load(open(sys.argv[3],'rb'))
concept=CC[('code',0)].sig.values
d=F[F.r2>0.3].dropna(subset=['firing_rate','acg_norm','tau_rise'])
ty,_=wm.spectral_types(d); types=np.array([None]*len(NT),dtype=object); types[d.index.values]=ty
# epoch spike lists per neuron, load 1
def ep(nid, epoch, load=1, win=None):
    r=NT.iloc[nid]; t=T[r['sub']]; t=t[t.load==load]; sp=wm.spikes_of(by,r)
    if epoch=='enc': return wm.epoch_spikes(sp,t.enc1.values,t.enc1.values+1.0,1.0)
    if epoch=='maint': return wm.epoch_spikes(sp,t.maint.values,t.probe.values,win)
t0=time.time()
EP={}
for nid in range(len(NT)):
    EP[(nid,'enc')]=ep(nid,'enc'); EP[(nid,'maint')]=ep(nid,'maint',win=2.8)
print('epochs',time.time()-t0)
res=[]
for grule in ['code','methods']:
    G=wm.burst_groups(NT,F,concept,types,grule)
    print(grule,{g:(len(v),sum(len(x) for x in v.values())) for g,v in G.items()})
    for rule,dist,thr in [('prominence',2,'real'),('height',2,'real'),('prominence',2,'own'),('height',2,'own'),('prominence',1,'real'),('height',1,'real')]:
        for epoch,win in [('enc',1.0),('maint',2.8)]:
            for g,subs in G.items():
                for sub,nids in subs.items():
                    rng=np.random.default_rng([abs(hash(g))%1000,sub,0 if epoch=='enc' else 1])
                    rc,sc,_,_=wm.group_bursts([EP[(n,epoch)] for n in nids],win,rng,rule,dist,thr)
                    res.append(dict(grule=grule,rule=rule,dist=dist,thr=thr,epoch=epoch,group=g,sub=sub,real=rc,sur=sc))
        print(grule,rule,dist,thr,time.time()-t0)
R=pd.DataFrame(res); R.to_pickle(sys.argv[4])
EOF
timeout 3000 python $TMPDIR/dev5.py $TMPDIR/S.pkl $TMPDIR/F.pkl $TMPDIR/CC.pkl $TMPDIR/B.pkl
```

```
epochs 0.6172943115234375
code {'All902': (20, 897), 'AllFit': (12, 270), 'LowACG': (12, 72), 'HighACG': (12, 72), 'ShortDecay': (12, 72), 'LongDecay': (12, 72), 'Concept': (9, 52), 'PY': (12, 95), 'IN': (19, 215)}
code prominence 2 real 5.084301710128784
code height 2 real 8.879082441329956
code prominence 2 own 14.260108947753906
code height 2 own 18.969234228134155
code prominence 1 real 23.16396141052246
code height 1 real 26.840394258499146
methods {'All902': (20, 897), 'AllFit': (12, 270), 'LowACG': (12, 132), 'HighACG': (12, 132), 'ShortDecay': (12, 132), 'LongDecay': (12, 132), 'Concept': (5, 39), 'PY': (12, 95), 'IN': (19, 215)}
methods prominence 2 real 31.50978660583496
methods height 2 real 35.54967451095581
methods prominence 2 own 40.97956871986389
methods height 2 own 45.83290338516235
methods prominence 1 real 50.23989820480347
methods height 1 real 54.1445586681366
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; python - <<EOF
import pandas as pd, numpy as np
from scipy.stats import wilcoxon
from statsmodels.stats.multitest import multipletests
R=pd.read_pickle('$TMPDIR/B.pkl')
fam=['All902','LowACG','HighACG','ShortDecay','LongDecay','Concept','PY','IN']
for key,g in R.groupby(['grule','rule','dist','thr','epoch']):
    rows=[]
    for grp in fam+['AllFit']:
        x=g[g.group==grp]
        w=wilcoxon(x.real,x.sur,zero_method='pratt',method='asymptotic')
        rows.append((grp,len(x),round(x.real.median(),1),round(x.sur.median(),1),(x.real>x.sur).sum(),w.statistic,w.pvalue))
    df=pd.DataFrame(rows,columns=['g','n','real','sur','n_above','W','p'])
    df['q']=np.nan; m=df.g.isin(fam); df.loc[m,'q']=multipletests(df.p[m],method='fdr_bh')[1]
    print(key); print(df.round(4).to_string(index=False))
EOF
```

```
('code', 'height', 1, 'real', 'enc')
         g  n  real  sur  n_above    W      p      q
    All902 20  41.5 33.7       17 14.0 0.0007 0.0054
    LowACG 12  42.5 42.5        6 30.0 0.4802 0.7520
   HighACG 12  47.0 46.7        5 35.0 0.7537 0.7537
ShortDecay 12  46.0 46.2        4 33.0 0.6379 0.7520
 LongDecay 12  42.0 42.1        6 33.0 0.6379 0.7520
   Concept  9  37.0 40.8        4 18.0 0.5940 0.7520
        PY 12  41.0 34.3        8 12.0 0.0342 0.1367
        IN 19  41.0 38.2        9 84.0 0.6580 0.7520
    AllFit 12  43.0 39.0        8 14.0 0.0499    NaN
('code', 'height', 1, 'real', 'maint')
         g  n  real  sur  n_above    W      p      q
    All902 20  95.0 56.1       20  0.0 0.0001 0.0007
    LowACG 12  90.0 78.1       11  3.0 0.0047 0.0076
   HighACG 12 101.5 84.0        9  6.0 0.0096 0.0128
ShortDecay 12  96.5 86.4        8 13.0 0.0414 0.0473
 LongDecay 12  96.5 79.7       12  0.0 0.0022 0.0044
   Concept  9  79.0 79.1        3 16.0 0.4413 0.4413
        PY 12  85.5 65.1       12  0.0 0.0022 0.0044
[... 244 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; cat >> wm.py <<'EOF'


def epoch_burst_counts(neuron_trials_by_epoch, rule="prominence", distance=2, mreading="methods"):
    """Real burst counts of one group in encoding, M1 to M3 and probe (Methods, Burst detection,
    last paragraph; 04_bursting/main_4f-k,6c,d.py). neuron_trials_by_epoch: {'enc': [...],
    'maint': [...], 'probe': [...]}, each a per-neuron list of per-trial relative spike times;
    encoding and probe use 1 s windows, maintenance 3 s (the code's durations, lines 19-25).
    mreading 'methods': peaks of the maintenance train counted by their time within the trial,
    [0, 1), [1, 2) and [2, 3) s from maintenance onset; 'code': peaks assigned to thirds of the
    bins of the whole concatenated train (lines 216-219)."""
    out = {}
    for ep, win in [("enc", 1.0), ("probe", 1.0)]:
        nt = neuron_trials_by_epoch[ep]
        pooled = np.concatenate([concat_trials(x, win) for x in nt])
        sm = smooth_counts(pooled, len(nt[0]) * win)
        out[ep] = len(burst_peaks(sm, np.percentile(sm, BURST_PCT), rule, distance))
    nt = neuron_trials_by_epoch["maint"]
    win = 3.0
    pooled = np.concatenate([concat_trials(x, win) for x in nt])
    sm = smooth_counts(pooled, len(nt[0]) * win)
    pk = burst_peaks(sm, np.percentile(sm, BURST_PCT), rule, distance)
    if mreading == "methods":
        t_in = (pk * BURST_BIN) % win
        for i in range(3):
            out[f"M{i + 1}"] = int(np.sum((t_in >= i) & (t_in < i + 1)))
    else:
        thirds = np.array_split(np.arange(len(sm)), 3)
        for i, part in enumerate(thirds):
            out[f"M{i + 1}"] = int(np.sum(np.isin(pk, part)))
    return out
EOF
cat > $TMPDIR/dev6.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, sys, itertools, zlib
sys.path.insert(0,'.')
import wm
from scipy.stats import wilcoxon
from statsmodels.stats.multitest import multipletests
S=pickle.load(open(sys.argv[1],'rb')); by={s['sub']:s for s in S}
NT=wm.neuron_table(S); T={s['sub']:wm.trial_frame(s) for s in S}
F=pd.read_pickle(sys.argv[2]); CC=pickle.load(open(sys.argv[3],'rb'))
concept=CC[('code',0)].sig.values
d=F[F.r2>0.3].dropna(subset=['firing_rate','acg_norm','tau_rise'])
ty,_=wm.spectral_types(d); types=np.array([None]*len(NT),dtype=object); types[d.index.values]=ty
EP={}
t0=time.time()
for nid in range(len(NT)):
    r=NT.iloc[nid]; sp=wm.spikes_of(by,r)
    for L in [1,2,3]:
        t=T[r['sub']]; t=t[t.load==L]
        e=t.enc1.values if L==1 else (t.timestamps_Encoding2.values if L==2 else t.timestamps_Encoding3.values)
        EP[(nid,L,'enc')]=wm.epoch_spikes(sp,e,e+1.0,1.0)
        EP[(nid,L,'maint')]=wm.epoch_spikes(sp,t.maint.values,t.probe.values,3.0)
        EP[(nid,L,'probe')]=wm.epoch_spikes(sp,t.probe.values,t.probe.values+1.0,1.0)
print(time.time()-t0)
rows=[]
for grule in ['code','methods']:
    G=wm.burst_groups(NT,F,concept,types,grule)
    for rule in ['prominence','height']:
        for mr in ['methods','code']:
            for L in [1,2,3]:
                for g,subs in G.items():
                    for sub,nids in subs.items():
                        c=wm.epoch_burst_counts({ep:[EP[(n,L,ep)] for n in nids] for ep in ['enc','maint','probe']},rule,2,mr)
                        rows.append(dict(grule=grule,rule=rule,mread=mr,load=L,group=g,sub=sub,**c))
E=pd.DataFrame(rows); E.to_pickle(sys.argv[4]); print(time.time()-t0)
per=['enc','M1','M2','M3','probe']
for key,g0 in E[(E.load==1)].groupby(['grule','rule','mread']):
    print(key)
    for grp,g in g0.groupby('group'):
        ps=[];names=[]
        for a,b in itertools.combinations(per,2):
            try: p=wilcoxon(g[a],g[b],zero_method='wilcox').pvalue
            except ValueError: p=1.0
            ps.append(p); names.append(f'{a}-{b}')
        q=multipletests(ps,method='fdr_bh')[1]
        med=g[per].median().to_dict()
        print(' ',grp,len(g),{k:round(v,1) for k,v in med.items()},' '.join(f'{n}:{qq:.3f}' for n,qq in zip(names[:4],q[:4])), 'min q other', round(min(q[4:]),3))
EOF
timeout 3000 python $TMPDIR/dev6.py $TMPDIR/S.pkl $TMPDIR/F.pkl $TMPDIR/CC.pkl $TMPDIR/E.pkl 2>&1 | grep -v Warn
```

```
1.7700750827789307
6.5951855182647705
('code', 'height', 'code')
  All902 20 {'enc': 41.5, 'M1': 42.0, 'M2': 38.5, 'M3': 37.0, 'probe': 41.0} enc-M1:0.438 enc-M2:0.617 enc-M3:0.438 enc-probe:0.643 min q other 0.363
  AllFit 12 {'enc': 43.0, 'M1': 44.0, 'M2': 40.5, 'M3': 34.0, 'probe': 45.0} enc-M1:0.789 enc-M2:0.789 enc-M3:0.146 enc-probe:0.689 min q other 0.049
  Concept 9 {'enc': 37.0, 'M1': 44.0, 'M2': 37.0, 'M3': 41.0, 'probe': 39.0} enc-M1:0.930 enc-M2:0.930 enc-M3:0.930 enc-probe:0.930 min q other 0.93
  HighACG 12 {'enc': 47.0, 'M1': 47.0, 'M2': 39.5, 'M3': 39.0, 'probe': 46.0} enc-M1:0.445 enc-M2:0.164 enc-M3:0.078 enc-probe:0.164 min q other 0.164
  IN 19 {'enc': 41.0, 'M1': 42.0, 'M2': 35.0, 'M3': 34.0, 'probe': 42.0} enc-M1:0.159 enc-M2:0.111 enc-M3:0.111 enc-probe:0.439 min q other 0.111
  LongDecay 12 {'enc': 42.0, 'M1': 46.0, 'M2': 43.0, 'M3': 37.5, 'probe': 42.5} enc-M1:0.128 enc-M2:0.895 enc-M3:0.128 enc-probe:0.983 min q other 0.128
  LowACG 12 {'enc': 42.5, 'M1': 42.5, 'M2': 43.5, 'M3': 40.5, 'probe': 42.0} enc-M1:1.000 enc-M2:0.910 enc-M3:0.747 enc-probe:1.000 min q other 0.747
  PY 12 {'enc': 41.0, 'M1': 39.0, 'M2': 45.0, 'M3': 43.0, 'probe': 44.5} enc-M1:0.379 enc-M2:0.379 enc-M3:0.379 enc-probe:0.379 min q other 0.379
  ShortDecay 12 {'enc': 46.0, 'M1': 42.5, 'M2': 42.5, 'M3': 41.5, 'probe': 42.5} enc-M1:0.864 enc-M2:0.864 enc-M3:0.344 enc-probe:0.098 min q other 0.864
('code', 'height', 'methods')
  All902 20 {'enc': 41.5, 'M1': 46.5, 'M2': 44.5, 'M3': 28.0, 'probe': 41.0} enc-M1:0.002 enc-M2:0.004 enc-M3:0.000 enc-probe:0.712 min q other 0.0
  AllFit 12 {'enc': 43.0, 'M1': 48.0, 'M2': 47.0, 'M3': 32.0, 'probe': 45.0} enc-M1:0.089 enc-M2:0.382 enc-M3:0.002 enc-probe:0.536 min q other 0.002
  Concept 9 {'enc': 37.0, 'M1': 53.0, 'M2': 42.0, 'M3': 24.0, 'probe': 39.0} enc-M1:0.016 enc-M2:0.052 enc-M3:0.010 enc-probe:0.758 min q other 0.01
  HighACG 12 {'enc': 47.0, 'M1': 48.0, 'M2': 48.0, 'M3': 30.0, 'probe': 46.0} enc-M1:0.497 enc-M2:0.507 enc-M
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; python - <<'EOF'
import numpy as np, time, sys
sys.path.insert(0,'.'); import wm
rng=np.random.default_rng(0)
X=rng.normal(size=(30,5000)); y=np.repeat(np.arange(5),6)
K=X@X.T
t=time.time()
for _ in range(20): wm.loo_correct(K,rng.permutation(y))
print((time.time()-t)/20)
EOF
```

```
Tue Nov 10 05:32:25 UTC 2026
0.037726855278015135
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; python - <<'EOF'
import numpy as np, time, sys
from sklearn.svm import _libsvm, SVC
import inspect
print(inspect.signature(_libsvm.fit) if hasattr(_libsvm.fit,'__signature__') else _libsvm.fit.__doc__[:1500])
EOF
```

```
Train the model using libsvm (low-level method)

    Parameters
    ----------
    X : array-like, dtype=float64 of shape (n_samples, n_features)

    Y : array, dtype=float64 of shape (n_samples,)
        target vector

    svm_type : {0, 1, 2, 3, 4}, default=0
        Type of SVM: C_SVC, NuSVC, OneClassSVM, EpsilonSVR or NuSVR
        respectively.

    kernel : {'linear', 'rbf', 'poly', 'sigmoid', 'precomputed'}, default="rbf"
        Kernel to use in the model: linear, polynomial, RBF, sigmoid
        or precomputed.

    degree : int32, default=3
        Degree of the polynomial kernel (only relevant if kernel is
        set to polynomial).
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; python - <<'EOF'
import numpy as np, time, sys
from sklearn.svm import _libsvm, SVC
rng=np.random.default_rng(0)
X=rng.normal(size=(30,5000)); y=np.repeat(np.arange(5),6).astype(float)
K=X@X.T
def loo_fast(K,y):
    n=len(y); idx=np.arange(n); out=np.zeros(n,bool)
    for i in range(n):
        tr=idx!=i
        Kt=np.ascontiguousarray(K[np.ix_(tr,tr)])
        m=_libsvm.fit(Kt,y[tr],svm_type=0,kernel='precomputed',C=1.0,tol=1e-3,cache_size=200.0)
        sup,sv,nsv,dual,inter,prob_a,prob_b,fit_status,niter=m if len(m)==9 else (m+(None,))[:9]
        p=_libsvm.predict(np.ascontiguousarray(K[i,tr][None,:]),sup,sv,nsv,dual,inter,prob_a,prob_b,svm_type=0,kernel='precomputed')
        out[i]=p[0]==y[i]
    return out
m=_libsvm.fit(np.ascontiguousarray(K[:29,:29]),y[:29],svm_type=0,kernel='precomputed',C=1.0)
print(len(m))
t=time.time()
for _ in range(20): a=loo_fast(K,rng.permutation(y))
print((time.time()-t)/20)
# equality check
for s in range(5):
    yy=rng.permutation(y)
    b=[]
    for i in range(30):
        tr=np.arange(30)!=i; c=SVC(kernel='precomputed',C=1).fit(K[np.ix_(tr,tr)],yy[tr]); b.append(c.predict(K[i,tr][None,:])[0]==yy[i])
    print((loo_fast(K,yy)==np.array(b)).all())
EOF
```

```
<persisted-output>
Output too large (534.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/73ddb9af-d626-46dd-830a-acdf1e4fec3e/tool-results/bh904vjuv.txt

Preview (first 2KB):
.*
optimization finished, #iter = 19
obj = -0.001159, rho = -0.017430
nSV = 12, nBSV = 0
.*
optimization finished, #iter = 20
obj = -0.001179, rho = -0.034164
nSV = 12, nBSV = 0
*.*
optimization finished, #iter = 17
obj = -0.001233, rho = 0.001825
nSV = 12, nBSV = 0
.*.*
optimization finished, #iter = 28
obj = -0.001100, rho = -0.089348
nSV = 11, nBSV = 0
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; python - <<'EOF' 2>&1 | tail -8
import numpy as np, time, sys
from sklearn.svm import _libsvm, SVC
_libsvm.set_verbosity_wrap(0)
rng=np.random.default_rng(0)
X=rng.normal(size=(30,5000)); y=np.repeat(np.arange(5),6).astype(float)
K=X@X.T
def loo_fast(K,y):
    n=len(y); idx=np.arange(n); out=np.zeros(n,bool)
    for i in range(n):
        tr=idx!=i
        Kt=np.ascontiguousarray(K[np.ix_(tr,tr)])
        m=_libsvm.fit(Kt,y[tr],svm_type=0,kernel='precomputed',C=1.0,tol=1e-3,cache_size=200.0)
        sup,sv,nsv,dual,inter,prob_a,prob_b,fit_status,niter=m
        p=_libsvm.predict(np.ascontiguousarray(K[i,tr][None,:]),sup,sv,nsv,dual,inter,prob_a,prob_b,svm_type=0,kernel='precomputed')
        out[i]=p[0]==y[i]
    return out
t=time.time()
for _ in range(20): a=loo_fast(K,rng.permutation(y))
print((time.time()-t)/20)
for s in range(5):
    yy=rng.permutation(y)
    b=[]
    for i in range(30):
        tr=np.arange(30)!=i; c=SVC(kernel='precomputed',C=1).fit(K[np.ix_(tr,tr)],yy[tr]); b.append(c.predict(K[i,tr][None,:])[0]==yy[i])
    print((loo_fast(K,yy)==np.array(b)).all())
EOF
```

```
0.0013843655586242675
True
True
True
True
True
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; python - <<'EOF'
s=open('wm.py').read()
a=s.index('def loo_correct(K, y):'); b=s.index('# ---------------------------------------------------------------------------------------------\n# Autocorrelograms')
new='''def _svm_fit(K, y):
    """Linear SVM (C-SVC, C = 1, one-vs-one) on a precomputed linear kernel, through the libsvm
    wrapper that sklearn's SVC uses. It gives the same fits as SVC(kernel='linear', C=1) on the
    features (the code's classifier) without SVC's per-call overhead; the notebook checks the
    equality on the data."""
    from sklearn.svm import _libsvm
    _libsvm.set_verbosity_wrap(0)
    return _libsvm.fit(np.ascontiguousarray(K), np.asarray(y, float), svm_type=0,
                       kernel="precomputed", C=1.0, tol=1e-3, cache_size=200.0)


def _svm_predict(model, Ktest):
    from sklearn.svm import _libsvm
    sup, sv, nsv, dual, inter, pa, pb, _, _ = model
    return _libsvm.predict(np.ascontiguousarray(Ktest, dtype=float), sup, sv, nsv, dual, inter,
                           pa, pb, svm_type=0, kernel="precomputed")


def loo_correct(K, y):
    """Leave-one-out correctness of the linear SVM from the precomputed kernel K = X X^T."""
    y = np.asarray(y, float)
    n = len(y)
    out = np.zeros(n, bool)
    idx = np.arange(n)
    for i in range(n):
        tr = idx != i
        if len(np.unique(y[tr])) < 2:
            continue
        m = _svm_fit(K[np.ix_(tr, tr)], y[tr])
        out[i] = _svm_predict(m, K[i, tr][None, :])[0] == y[i]
    return out


def loo_correct_sklearn(X, y):
    """The same with sklearn SVC(kernel='linear') on the features, for the equality check."""
    from sklearn.svm import SVC
    n = len(y)
    idx = np.arange(n)
    return np.array([SVC(kernel="linear", C=1.0).fit(X[idx != i], y[idx != i]).predict(X[i:i + 1])[0] == y[i]
                     for i in range(n)])


def loo_cross_temporal(X, y):
    """Cross-temporal LOOCV accuracy matrix (train bin x test bin). X: trials x neurons x bins."""
    y = np.asarray(y, float)
    n, _, nb = X.shape
    G = np.einsum("inb,jnc->bcij", X, X)  # G[b, c] = X[:, :, b] @ X[:, :, c].T
    acc = np.zeros((nb, nb))
    idx = np.arange(n)
    for b in range(nb):
        for i in range(n):
            tr = idx != i
            m = _svm_fit(G[b, b][np.ix_(tr, tr)], y[tr])
            kt = G[:, b, i, :][:, tr]  # test trial i at every bin c against training trials at bin b
            acc[b] += _svm_predict(m, kt) == y[i]
    return acc / n


'''
s=s[:a]+new+s[b:]
open('wm.py','w').write(s)
EOF
grep -n "^def " wm.py
```

```
36:def list_assets(version=DANDISET_VERSION):
46:def asset_url(asset_id):
50:def region_of(location):
58:def _str(x):
62:def load_session(asset):
91:def sternberg_assets(version=DANDISET_VERSION):
95:def subject_number(path):
99:def load_all(version=DANDISET_VERSION, workers=6):
112:def trial_frame(sess):
136:def count_in(spikes, starts, ends):
141:def fixation_stats(spikes, t):
149:def neuron_table(sessions):
160:def spikes_of(sessions_by_sub, row):
168:def poisson_slopes(y, X, n_iter=50):
197:def glm_permutation(counts_by_neuron, x_by_neuron, perms_by_neuron, groups, alpha=0.05):
234:def concept_test(rates, imgs, rng, n_boot=1000, reading="methods"):
266:def _svm_fit(K, y):
277:def _svm_predict(model, Ktest):
284:def loo_correct(K, y):
299:def loo_correct_sklearn(X, y):
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hwm; sed -n 15,140p "02_psth_decoding/main_2e,supp_1f.py" | grep -v "plt\.\|ax\.\|^\s*#"; sed -n 280,349p "02_psth_decoding/main_2e,supp_1f.py" | grep -v "plt\.\|ax\."
```

```
'amygdala': ['amygdala_left', 'amygdala_right'],
    'hippocampus': ['hippocampus_left', 'hippocampus_right'],
    'dACC': ['dorsal_anterior_cingulate_cortex_right', 'dorsal_anterior_cingulate_cortex_left'],
    'preSMA': ['pre_supplementary_motor_area_left', 'pre_supplementary_motor_area_right'],
    'amygdala_hippocampus': ['amygdala_left', 'amygdala_right', 'hippocampus_left', 'hippocampus_right'],
    'dACC_preSMA': ['dorsal_anterior_cingulate_cortex_right', 'dorsal_anterior_cingulate_cortex_left',
                    'pre_supplementary_motor_area_left', 'pre_supplementary_motor_area_right']
}

bin_size = 1
step_size = 0.25
durations = {1: 2.5, 2: 2.5, 3: 2.5}
time_bins_by_load = {l: np.arange(0, durations[l] - bin_size + step_size, step_size) for l in durations}
n_shuffles = 1000
rng = np.random.default_rng(42)  # reproducible random generator

all_subject_ids = sorted(trial_info['subject_id'].unique())
subject_color_map = {subj: cmap(i % 20) for i, subj in enumerate(all_subject_ids)}

def parse_spike_times(spike_str):
[... 167 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; cat >> wm.py <<'EOF'


# ---------------------------------------------------------------------------------------------
# Decoding designs
# ---------------------------------------------------------------------------------------------

def window_starts(width, step, end):
    """The code's create_time_bins: np.arange(0, end - width + step, step)."""
    return np.arange(0, end - width + step, step)


def zcounts(spikes, onsets, starts, width, mu, sd):
    """Counts in [onset + s, onset + s + width) for each trial and window start, z-scored as in
    the code: (count - fixation mean rate) / fixation s.d. of rate, raw counts when s.d. is 0."""
    a = onsets[:, None] + starts[None, :]
    c = count_in(spikes, a.ravel(), (a + width).ravel()).reshape(a.shape).astype(float)
    return (c - mu) / sd if sd > 0 else c


def pseudo_rows(T, subs, load, reading, final=None):
    """Trial alignment of a pseudo-population. Returns ({sub: trial numbers}, labels).
    reading 'code': the rows of the code's identity-matched table (data/new_trial_final.xlsx,
    trial_id_final) at this load, in trial_id_final order, labels from subject 14 as in the code
    (main_2f,supp_1g.py:11; the label is the first image for load 1, the second for load 2, the
    third for load 3). reading 'rank': for each participant the first k trials of each image (the
    image at position = load) in trial order, aligned by image and rank, with k = 6 or the smallest
    count over participants and images if lower."""
    if reading == "code":
        f = final[final.num_images_presented == load].sort_values(["subject_id", "trial_id_final"])
        rows = {s: f[f.subject_id == s].sort_values("trial_id_final").trial_id.values for s in subs}
        lab = f[f.subject_id == 14].sort_values("trial_id_final")[f"stimulus_index_enc{load}"].values
        return rows, lab
    col = {1: "img1", 2: "img2", 3: "img3"}[load]
    k = 6
    for s in subs:
        t = T[s][T[s].load == load]
        k = min(k, t[col].value_counts().min())
    rows = {}
    for s in subs:
        t = T[s][T[s].load == load]
        rows[s] = np.concatenate([t[t[col] == im].trial.values[:k] for im in range(1, 6)])
    lab = np.repeat(np.arange(1, 6), k)
    return rows, lab
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; cat > $TMPDIR/dev7.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import wm
S=pickle.load(open(sys.argv[1],'rb')); by={s['sub']:s for s in S}
NT=wm.neuron_table(S); T={s['sub']:wm.trial_frame(s) for s in S}
F=pd.read_pickle(sys.argv[2]); CC=pickle.load(open(sys.argv[3],'rb')); final=pd.read_excel(sys.argv[4])
concept=CC[('code',0)].sig.values
d=F[F.r2>0.3].dropna(subset=['firing_rate','acg_norm','tau_rise'])
ty,_=wm.spectral_types(d); types=np.array([None]*len(NT),dtype=object); types[d.index.values]=ty
FX={}
for nid in range(len(NT)):
    r=NT.iloc[nid]; FX[nid]=wm.fixation_stats(wm.spikes_of(by,r),T[r['sub']])
def design(nids, load, reading, width, step=0.025, end=2.5):
    subs=sorted(set(NT['sub'].values[nids]))
    rows,lab=wm.pseudo_rows(T,subs,load,reading,final)
    st=wm.window_starts(width,step,end)
    blocks=[]
    for n in nids:
        r=NT.iloc[n]; t=T[r['sub']].set_index('trial').loc[rows[r['sub']]]
        mu,sd=FX[n]; blocks.append(wm.zcounts(wm.spikes_of(by,r),t.maint.values,st,width,mu,sd))
    return np.concatenate(blocks,axis=1), np.asarray(lab)
cc=np.where(concept)[0]; py=np.where(concept&(types=='PY'))[0]; inn=np.where(concept&(types=='IN'))[0]
print(len(cc),len(py),len(inn))
# equality check
X,y=design(cc,1,'code',1.0)
print('eq', (wm.loo_correct(X@X.T,y)==wm.loo_correct_sklearn(X,y)).all())
t0=time.time()
out={}
for grp,nids in [('all',cc),('PY',py),('IN',inn)]:
    for reading in ['code','rank']:
        for load in [1,2,3]:
            for w in [0.25,0.5,0.75,1.0]:
                X,y=design(nids,load,reading,w); K=X@X.T
                real=wm.loo_correct(K,y)
                rng=np.random.default_rng(42)
                null=np.array([wm.loo_correct(K,rng.permutation(y)).mean() for _ in range(1000)])
                out[(grp,reading,load,w)]=(real,null)
                p=(np.sum(null>=real.mean())+1)/1001
                print(grp,reading,load,w,X.shape,round(100*real.mean(),2),round(100*null.mean(),1),round(p,4),round(time.time()-t0))
pickle.dump(out,open(sys.argv[5],'wb'))
EOF
timeout 3500 python $TMPDIR/dev7.py $TMPDIR/S.pkl $TMPDIR/F.pkl $TMPDIR/CC.pkl $TMPDIR/hwm/data/new_trial_final.xlsx $TMPDIR/D.pkl
```

```
58 11 16
eq True
all code 1 0.25 (30, 5278) 30.0 9.1 0.004 2
all code 1 0.5 (30, 4698) 60.0 11.1 0.001 3
all code 1 0.75 (30, 4118) 66.67 12.6 0.001 5
all code 1 1.0 (30, 3538) 76.67 13.8 0.001 7
all code 2 0.25 (25, 5278) 28.0 6.5 0.003 8
all code 2 0.5 (25, 4698) 20.0 8.6 0.0719 9
all code 2 0.75 (25, 4118) 28.0 10.1 0.018 10
all code 2 1.0 (25, 3538) 36.0 11.4 0.005 11
all code 3 0.25 (20, 5278) 10.0 5.1 0.2867 12
all code 3 0.5 (20, 4698) 15.0 6.3 0.1459 13
all code 3 0.75 (20, 4118) 15.0 8.0 0.2278 14
all code 3 1.0 (20, 3538) 10.0 9.4 0.5405 15
all rank 1 0.25 (30, 5278) 10.0 18.1 0.9421 16
all rank 1 0.5 (30, 4698) 6.67 18.0 0.992 18
all rank 1 0.75 (30, 4118) 6.67 17.5 0.983 20
all rank 1 1.0 (30, 3538) 6.67 17.1 0.977 22
all rank 2 0.25 (25, 5278) 8.0 18.4 0.959 23
all rank 2 0.5 (25, 4698) 8.0 17.9 0.955 24
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; cat > $TMPDIR/dev8.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import wm
S=pickle.load(open(sys.argv[1],'rb')); by={s['sub']:s for s in S}
NT=wm.neuron_table(S); T={s['sub']:wm.trial_frame(s) for s in S}
CC=pickle.load(open(sys.argv[2],'rb')); final=pd.read_excel(sys.argv[3])
concept=CC[('code',0)].sig.values; cc=np.where(concept)[0]
FX={n:wm.fixation_stats(wm.spikes_of(by,NT.iloc[n]),T[NT.iloc[n]['sub']]) for n in cc}
subs=sorted(set(NT['sub'].values[cc]))
rows_c,lab_c=wm.pseudo_rows(T,subs,1,'code',final)
rows_r,lab_r=wm.pseudo_rows(T,subs,1,'rank',final)
for s in subs[:4]:
    t=T[s].set_index('trial')
    print(s,'code rows',rows_c[s][:12], t.loc[rows_c[s],'img1'].values[:12], lab_c[:12])
    print(s,'rank rows',rows_r[s][:12], t.loc[rows_r[s],'img1'].values[:12])
def X_of(rows):
    st=wm.window_starts(1.0,0.025,2.5); B=[]
    for n in cc:
        r=NT.iloc[n]; t=T[r['sub']].set_index('trial').loc[rows[r['sub']]]
        B.append(wm.zcounts(wm.spikes_of(by,r),t.maint.values,st,1.0,*FX[n]))
    return np.concatenate(B,1)
X=X_of(rows_c); print('code', wm.loo_correct(X@X.T,lab_c).mean())
# code rows, labels = own image mapped through rank of PicID... check own label consistency
rng=np.random.default_rng(0)
# shuffle rows within label within subject
rows_s={s:rows_c[s].copy() for s in subs}
for s in subs:
    for L in np.unique(lab_c):
        i=np.where(lab_c==L)[0]; rows_s[s][i]=rng.permutation(rows_s[s][i])
X=X_of(rows_s); print('code rows shuffled within label', wm.loo_correct(X@X.T,lab_c).mean())
X=X_of(rows_r); print('rank', wm.loo_correct(X@X.T,lab_r).mean())
# rank reading but labels as in code mapping (stimulus_index), i.e. map PicID->stimulus_index per subject
EOF
python $TMPDIR/dev8.py $TMPDIR/S.pkl $TMPDIR/CC.pkl $TMPDIR/hwm/data/new_trial_final.xlsx
```

```
2 code rows [124  29  97  12 128  34 118  25  78  11 123  45] [1 1 1 1 1 1 2 2 2 2 2 2] [0 0 0 0 0 0 1 1 1 1 1 1]
2 rank rows [12 29 34 64 73 97 11 25 45 50 67 78] [1 1 1 1 1 1 2 2 2 2 2 2]
4 code rows [124  29  97  12 128  34 118  25  78  11 123  45] [1 1 1 1 1 1 2 2 2 2 2 2] [0 0 0 0 0 0 1 1 1 1 1 1]
4 rank rows [12 29 34 64 73 97 11 25 45 50 67 78] [1 1 1 1 1 1 2 2 2 2 2 2]
5 code rows [124  29  97  12 128  34 118  25  78  11 123  45] [1 1 1 1 1 1 2 2 2 2 2 2] [0 0 0 0 0 0 1 1 1 1 1 1]
5 rank rows [12 29 34 64 73 97 11 25 45 50 67 78] [1 1 1 1 1 1 2 2 2 2 2 2]
7 code rows [23 46 99 62 85 80 79 10 40  5 70 12] [1 1 1 1 1 1 2 2 2 2 2 2] [0 0 0 0 0 0 1 1 1 1 1 1]
7 rank rows [23 46 62 80 85 99  5 10 12 17 24 40] [1 1 1 1 1 1 2 2 2 2 2 2]
code 0.7666666666666667
code rows shuffled within label 0.6333333333333333
rank 0.06666666666666667
```

**Agent calls Bash**

```bash
date -u; source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; cat > $TMPDIR/dev9.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import wm
from statsmodels.stats.multitest import multipletests
S=pickle.load(open(sys.argv[1],'rb')); by={s['sub']:s for s in S}
for s in S: s['units']['region']=s['units'].location.map(wm.region_of)
NT=wm.neuron_table(S); T={s['sub']:wm.trial_frame(s) for s in S}
CC=pickle.load(open(sys.argv[2],'rb'))
concept=CC[('code',0)].sig.values
groups={'AMY':['AMY'],'HPC':['HPC'],'dACC':['dACC'],'preSMA':['preSMA'],'MTL':['AMY','HPC'],'dACC_preSMA':['dACC','preSMA']}
st=wm.window_starts(1.0,0.25,2.5); print(st)
t0=time.time(); rows=[]
for gname,regs in groups.items():
    for sub in sorted(NT['sub'].unique()):
        nids=NT[(NT['sub']==sub)&NT.region.isin(regs)&concept[NT.nid]].nid.values
        if len(nids)<3: continue
        for load in [1,2,3]:
            t=T[sub][T[sub].load==load]; y=t['last'].values
            X=np.concatenate([wm.zcounts(wm.spikes_of(by,NT.iloc[n]),t.maint.values,st,1.0,*wm.fixation_stats(wm.spikes_of(by,NT.iloc[n]),T[sub])) for n in nids],1)
            K=X@X.T; real=wm.loo_correct(K,y).mean()
            rng=np.random.default_rng([sub,load,len(gname)])
            null=np.array([wm.loo_correct(K,rng.permutation(y)).mean() for _ in range(1000)])
            rows.append(dict(group=gname,sub=sub,n=len(nids),load=load,ntr=len(y),acc=real,null=null))
    print(gname,time.time()-t0)
R=pd.DataFrame(rows); R.to_pickle(sys.argv[3])
for thr in [3,4]:
    print('min cells',thr)
    for load in [1,2,3]:
        out=[]
        for g in groups:
            x=R[(R.group==g)&(R.load==load)&(R.n>=thr)]
            if len(x)==0: continue
            m=x.acc.mean(); nm=np.mean(np.stack(x.null.values),0)
            out.append((g,len(x),round(100*m,2),round(100*nm.mean(),2),(np.sum(nm>=m)+1)/1001))
        df=pd.DataFrame(out,columns=['g','nsub','acc','null','p']); df['q']=multipletests(df.p,method='fdr_bh')[1]
        print(load); print(df.to_string(index=False))
EOF
python $TMPDIR/dev9.py $TMPDIR/S.pkl $TMPDIR/CC.pkl $TMPDIR/WP.pkl
```

```
Tue Nov 10 05:36:34 UTC 2026
[0.   0.25 0.5  0.75 1.   1.25 1.5 ]
AMY 143.53704833984375
HPC 175.55252933502197
dACC 175.55620741844177
preSMA 175.55971574783325
MTL 358.0147922039032
dACC_preSMA 358.01847529411316
min cells 3
1
  g  nsub   acc  null        p        q
AMY     7 12.30 15.51 0.957043 0.997003
HPC     1  6.67 15.72 0.987013 0.997003
MTL     8 10.62 15.50 0.997003 0.997003
2
  g  nsub   acc  null        p        q
AMY     7 15.79 15.81 0.511489 0.745255
HPC     1 17.78 15.74 0.432567 0.745255
MTL     8 14.58 15.75 0.745255 0.745255
3
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; cat >> wm.py <<'EOF'


def psth_z(spikes, onsets, dur, mu, sd, bin_size=0.05, smooth=True):
    """Trial x bin firing rate in 50 ms bins from each onset, z-scored with the fixation mean and
    s.d. of rate, then smoothed across bins with a Gaussian of sigma one bin (Methods,
    Electrophysiology)."""
    from scipy.ndimage import gaussian_filter1d
    nb = int(round(dur / bin_size))
    st = np.arange(nb) * bin_size
    a = onsets[:, None] + st[None, :]
    c = count_in(spikes, a.ravel(), (a + bin_size).ravel()).reshape(a.shape) / bin_size
    z = (c - mu) / sd if sd > 0 else c - mu
    return gaussian_filter1d(z, 1, axis=1, mode="nearest") if smooth else z


def bh(p):
    from statsmodels.stats.multitest import multipletests
    p = np.asarray(p, float)
    return multipletests(p, method="fdr_bh")[1] if len(p) else p
EOF
cat > $TMPDIR/dev10.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import wm
S=pickle.load(open(sys.argv[1],'rb')); by={s['sub']:s for s in S}
NT=wm.neuron_table(S); T={s['sub']:wm.trial_frame(s) for s in S}
CC=pickle.load(open(sys.argv[2],'rb'))
cc=CC[('code',0)]; cells=np.where(cc.sig.values)[0]
t0=time.time()
def pref_mask(t,pref,load):
    if load==1: return (t.img1==pref).values
    return ((t.img1==pref)|(t.img2==pref)|(t.img3==pref)).values
res={}
for load in [1,2,3]:
    D={ep:[] for ep in ['enc','maint']}
    single=[]
    for n in cells:
        r=NT.iloc[n]; sp=wm.spikes_of(by,r); tt=T[r['sub']]; mu,sd=wm.fixation_stats(sp,tt); t=tt[tt.load==load]
        pm=pref_mask(t,cc.pref.values[n],load)
        Zm=wm.psth_z(sp,t.maint.values,2.5,mu,sd); Ze=wm.psth_z(sp,t.enc1.values,1.0,mu,sd)
        D['maint'].append(Zm[pm].mean(0)-Zm[~pm].mean(0)); D['enc'].append(Ze[pm].mean(0)-Ze[~pm].mean(0))
        if load==1:
            rng=np.random.default_rng(int(n))
            obs=Zm[pm].mean(0)-Zm[~pm].mean(0)
            nulls=np.array([ (lambda q: Zm[q].mean(0)-Zm[~q].mean(0))(rng.permutation(pm)) for _ in range(1000)])
            p=np.mean(np.abs(nulls)>=np.abs(obs),0)
            fa=np.mean((p<0.05)&(obs>0))
            cnt=[wm.count_in(sp,t.maint.values+i,np.minimum(t.maint.values+i+1,t.probe.values)) for i in range(3)]
            pw=[]
            for c in cnt:
                o=c[pm].mean()-c[~pm].mean(); nn=np.array([(lambda q:c[q].mean()-c[~q].mean())(rng.permutation(pm)) for _ in range(1000)])
                pw.append((o>0) and np.mean(np.abs(nn)>=abs(o))<0.05)
            single.append((n,pm.sum(),(~pm).sum(),fa,all(pw),sum(pw)))
    Dm=np.array(D['maint']); De=np.array(D['enc'])
    rng=np.random.default_rng(42)
    idx=rng.integers(0,len(cells),(1000,len(cells)))
    def boot(Dx):
        b=Dx[idx].mean(1); return np.minimum(1,2*np.minimum(np.mean(b<=0,0),np.mean(b>=0,0)))
    pm_,pe_=boot(Dm),boot(De)
    q_all=wm.bh(np.r_[pe_,pm_]); qm=q_all[len(pe_):]; qm_panel=wm.bh(pm_)
    sig=(qm<0.05)&(Dm.mean(0)>0)
    seg=[sig[i*10:(i+1)*10].any() for i in range(5)]
    print('load',load,'mean diff maint',Dm.mean().round(3),'frac sig bins',sig.mean().round(2),'segments',seg,'panel frac',((qm_panel<0.05)&(Dm.mean(0)>0)).mean().round(2),'enc frac',((q_all[:len(pe_)]<0.05)&(De.mean(0)>0)).mean().round(2))
    if load==1:
        s=pd.DataFrame(single,columns=['nid','npref','nnon','frac_bins_sig','all3','n3'])
        print(s.describe().round(2)); print('persistent a',(s.frac_bins_sig>=0.5).sum(),'b',s.all3.sum(),'of',len(s))
print(time.time()-t0)
EOF
python $TMPDIR/dev10.py $TMPDIR/S.pkl $TMPDIR/CC.pkl
```

```
load 1 mean diff maint 0.774 frac sig bins 1.0 segments [np.True_, np.True_, np.True_, np.True_, np.True_] panel frac 1.0 enc frac 0.85
          nid  npref   nnon  frac_bins_sig     n3
count   58.00  58.00  58.00          58.00  58.00
mean   500.91   8.57  34.41           0.21   1.00
std    223.83   0.88   3.00           0.22   1.14
min     40.00   6.00  28.00           0.00   0.00
25%    358.50   9.00  36.00           0.04   0.00
50%    553.00   9.00  36.00           0.11   1.00
75%    617.50   9.00  36.00           0.34   2.00
max    887.00   9.00  36.00           0.86   3.00
persistent a 8 b 10 of 58
load 2 mean diff maint 0.487 frac sig bins 1.0 segments [np.True_, np.True_, np.True_, np.True_, np.True_] panel frac 1.0 enc frac 0.8
load 3 mean diff maint 0.325 frac sig bins 0.64 segments [np.True_, np.True_, np.True_, np.True_, np.True_] panel frac 0.62 enc frac 0.8
2.288609504699707
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; uv pip install -q scikit-image 2>&1|tail -1; cd entries/kussovska-2025; cat > $TMPDIR/dev11.py <<'EOF'
import pickle, time, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import wm
from scipy.stats import binom
from scipy import ndimage
S=pickle.load(open(sys.argv[1],'rb')); by={s['sub']:s for s in S}
NT=wm.neuron_table(S); T={s['sub']:wm.trial_frame(s) for s in S}
CC=pickle.load(open(sys.argv[2],'rb')); final=pd.read_excel(sys.argv[3])
F=pd.read_pickle(sys.argv[4])
concept=CC[('code',0)].sig.values
d=F[F.r2>0.3].dropna(subset=['firing_rate','acg_norm','tau_rise'])
ty,_=wm.spectral_types(d); types=np.array([None]*len(NT),dtype=object); types[d.index.values]=ty
def ct_design(nids, load, label):
    subs=sorted(set(NT['sub'].values[nids])); rows,lab=wm.pseudo_rows(T,subs,load,'code',final)
    f=final[final.num_images_presented==load].sort_values(['subject_id','trial_id_final']); f14=f[f.subject_id==14].sort_values('trial_id_final')
    y=f14['stimulus_index_enc1' if label=='first' else f'stimulus_index_enc{load}'].values
    dur={1:5,2:6,3:7}[load]; st=wm.window_starts(0.25,0.1,dur)
    X=np.zeros((len(y),len(nids),len(st)))
    for j,n in enumerate(nids):
        r=NT.iloc[n]; tt=T[r['sub']]; mu,sd=wm.fixation_stats(wm.spikes_of(by,r),tt); t=tt.set_index('trial').loc[rows[r['sub']]]
        X[:,j,:]=wm.zcounts(wm.spikes_of(by,r),t.enc1.values,st,0.25,mu,sd)
    return X,y,st
def sigmask(acc,N,side):
    k=np.round(acc*N).astype(int)
    p=binom.sf(k-1,N,0.2) if side=='one' else np.vectorize(lambda kk: __import__('scipy').stats.binomtest(int(kk),N,0.2,alternative='two-sided').pvalue)(k)
    q=wm.bh(p.ravel()).reshape(p.shape)
    return (q<0.05)&(acc>0.2)
cc=np.where(concept)[0]
t0=time.time()
X,y,st=ct_design(cc,1,'first'); acc=wm.loo_cross_temporal(X,y); print('map time',time.time()-t0, X.shape)
for side in ['one','two']:
    m=sigmask(acc,len(y),side); lab,nl=ndimage.label(m)
    print(side,'sig pairs',m.sum(),'clusters',nl, 'diag acc mean', np.diag(acc).mean().round(3))
    mb=(st>=1.0)&(st+0.25<=3.5)
    print(' max frac of maint test bins per maint train bin', (m[np.ix_(mb,mb)].mean(1)).max().round(2), 'train bins in enc/early maint with sig',np.where(m.any(1))[0][:20])
t1=time.time(); rng=np.random.default_rng(0); acc_p=wm.loo_cross_temporal(X,rng.permutation(y)); print('perm time',time.time()-t1)
np.save(sys.argv[5],acc)
EOF
python $TMPDIR/dev11.py $TMPDIR/S.pkl $TMPDIR/CC.pkl $TMPDIR/hwm/data/new_trial_final.xlsx $TMPDIR/F.pkl $TMPDIR/ct.npy
```

```
map time 0.19666528701782227 (30, 58, 49)
one sig pairs 290 clusters 47 diag acc mean 0.324
 max frac of maint test bins per maint train bin 0.35 train bins in enc/early maint with sig [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
two sig pairs 290 clusters 47 diag acc mean 0.324
 max frac of maint test bins per maint train bin 0.35 train bins in enc/early maint with sig [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
perm time 0.1690673828125
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; uv pip install -q dPCA 2>&1|tail -2; python - <<'EOF'
import numpy as np, time
from dPCA import dPCA
rng=np.random.default_rng(0)
N,S,Tt,R=58,5,1250,3
trialX=rng.normal(size=(R,N,S,Tt))
X=trialX.mean(0); X-=X.reshape(N,-1).mean(1)[:,None,None]
t=time.time()
d=dPCA.dPCA(labels='st',regularizer='auto',n_components=5)
d.protect=['t']
Z=d.fit_transform(X,trialX)
print('fit',time.time()-t, {k:v.shape for k,v in Z.items()})
EOF
```

```
Exit code 1
/tmp/claude-1001/dev/lib/python3.12/site-packages/dPCA/dPCA.py:422: SyntaxWarning: invalid escape sequence '\s'
  \sum_phi ||X[n] - F_\phi D_phi^{-n} X^{-n}||^2
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "/tmp/claude-1001/dev/lib/python3.12/site-packages/dPCA/dPCA.py", line 18, in <module>
    import numexpr as ne
ModuleNotFoundError: No module named 'numexpr'
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; uv pip install -q numexpr numba 2>&1|tail -2; timeout 900 python - <<'EOF' 2>&1 | grep -v Warn | tail -5
import numpy as np, time
from dPCA import dPCA
rng=np.random.default_rng(0)
N,S,Tt,R=58,5,1250,3
trialX=rng.normal(size=(R,N,S,Tt))
X=trialX.mean(0); X-=X.reshape(N,-1).mean(1)[:,None,None]
t=time.time()
d=dPCA.dPCA(labels='st',regularizer='auto',n_components=5)
d.protect=['t']
Z=d.fit_transform(X,trialX)
print('fit',time.time()-t, {k:v.shape for k,v in Z.items()})
EOF
```

```
Starting trial  2 / 3
Starting trial  3 / 3
Optimized regularization, optimal lambda =  0.013016111155156117
Regularization will be fixed; to compute the optimal                    parameter again on the next fit, please                    set opt_regularizer_flag to True.
fit 31.59497570991516 {'s': (5, 5, 1250), 't': (5, 5, 1250), 'st': (5, 5, 1250)}
```

**Agent calls Bash**

```bash
cd $TMPDIR/hwm; grep -n "dPCA\|protect\|regular\|for .* in range\|n_components\|fit\|kruskal\|posthoc" "03_dpca/main_3d,supp_2a,b,i.py" | head -40
```

```
3:from dPCA import dPCA
7:from dPCA.dPCA import dPCA
11:import scikit_posthocs as sp
20:#dPCA distance-resampling  (Encoding vs Maintenance)
62:        in low-D dPCA space"""
75:    for it in range(n_iter):
106:        # trial averages (for dPCA fit/transform) 
118:        # dPCA fits 
119:        dpca_enc = dPCA(labels="st", regularizer="auto")
120:        dpca_enc.opt_regularizer_flag = True
121:        dpca_enc.protect = []
122:        Z_enc_train = dpca_enc.fit_transform(RD_enc_train, trialX_enc_train)
128:        dpca_maint = dPCA(labels="st", regularizer="auto")
129:        dpca_maint.opt_regularizer_flag = True
130:        dpca_maint.protect = []
131:        Z_maint_train = dpca_maint.fit_transform(RD_maint_train, trialX_maint_train)
152:    H_kw, kw_p = sps.kruskal(*box_datas)
158:        dunn_df = sp.posthoc_dunn(mat, p_adjust="fdr_bh")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; timeout 900 python - <<'EOF' 2>&1 | grep "^T"
import numpy as np, time, resource
from dPCA.dPCA import dPCA
rng=np.random.default_rng(0)
N,S,R=58,5,3
for Tt in [500,1250,625,500,1250]:
    trialX=rng.normal(size=(R,N,S,Tt)); X=trialX.mean(0); X-=X.reshape(N,-1).mean(1)[:,None,None]
    t=time.time(); d=dPCA(labels='st',regularizer='auto'); d.opt_regularizer_flag=True; d.protect=[]
    Z=d.fit_transform(X,trialX); print('T',Tt,round(time.time()-t,1), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss//1000,'MB')
EOF
```

```
T 500 12.2 248 MB
T 1250 26.3 300 MB
T 625 13.7 300 MB
T 500 15.5 300 MB
T 1250 25.3 304 MB
```

**Agent calls Bash**

```bash
date -u; source $TMPDIR/dev/bin/activate; cd $TMPDIR/hwm; python -c "
import pandas as pd; d=pd.read_excel('data/cell_analysis/validation_data.xlsx'); print(d.shape); print(d.head()); print(d.columns.tolist()); print(d.iloc[:,-1].value_counts() if d.shape[1]<12 else '')
for c in d.columns:
    if d[c].dtype==object: print(c, d[c].value_counts().to_dict())
"; sed -n 1,80p 05_cell_analysis/supp_4a-e.py | grep -v "plt\.\|ax\."; sed -n 100,140p "06_cell_specific/main_6g,h.py"
```

```
Tue Nov 10 05:46:18 UTC 2026
(343, 6)
   firing_rate   tau_decay   mean_acg  norm_acg cell_type  tau_rise
0    17.260146   85.623670  29.311209  0.591336        IN  1.487211
1     6.093135  112.583240  10.779466  0.684481        IN  1.552118
2    23.877437   73.057331  33.813335  0.501889        IN  1.025018
3    16.109536   19.833749  26.460145  0.656093        IN  2.954962
4     9.167153   15.050569  16.672640  0.640023        IN  4.485963
['firing_rate', 'tau_decay', 'mean_acg', 'norm_acg', 'cell_type', 'tau_rise']
tau_rise
1.487211    1
1.552118    1
1.025018    1
2.954962    1
4.485963    1
           ..
3.447057    1
2.308340    1
4.197672    1
4.059161    1
[... 123 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def check\|embedded\|read_\|http\|forbid\|reject\|literal\|tag" tools/entry.py | head -60
```

```
21:- each notebook has a cell tagged `sanity` that prints what was loaded;
22:- no notebook or helper embeds a large literal array or an encoded image, or
61:MAX_LITERAL_NUMBERS = 200                 # more numbers than this in one literal is "embedded data"
113:    return Draft202012Validator(json.loads((ROOT / "schemas" / f"{name}.schema.json").read_text()))
139:    data, problem = _parsed(path.read_text())
149:    for message in _schema_errors(path.read_text(), schema_name):
172:def check(entry_dir: Path) -> Report:
198:        locked_for = LOCK_VERSION.search(lock.read_text()[:2000])
203:                  for line in lock.read_text().splitlines() if line and not line.startswith((" ", "#"))}
204:        for line in requirements.read_text().splitlines():
222:    helper_code = "\n".join((entry_dir / h).read_text() for h in helpers if (entry_dir / h).is_file())
229:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
230:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
242:            _derivation_checks(report, rel / name, (entry_dir / name).read_text())
342:            tag = outcome.get("output")
343:            if notebook in present and tag:
345:                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
346:                    report.error(path.relative_to(ROOT), f"no cell tagged {tag!r} in {notebook}")
365:        report.error(where, f"contains a literal of more than {MAX_LITERAL_NUMBERS} numbers; "
377:    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text()) or {}
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 15,60p tools/entry.py; sed -n 355,412p tools/entry.py; sed -n 172,250p tools/entry.py
```

```
tied to the data:

- every notebook in the directory is listed in entry.yaml, and exists;
- notebooks are committed without outputs;
- the lock file is present and newer requirements are not left unlocked;
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
- each notebook has a cell tagged `sanity` that prints what was loaded;
- no notebook or helper embeds a large literal array or an encoded image, or
  reads a figure from somewhere else.

`run` builds a fresh virtual environment from the lock file and executes each
notebook through a Jupyter kernel installed in that environment, in the entry
directory. The executed copies
go to --output-dir (default: executed/<name>/, which git ignores). A notebook
that takes longer than --max-minutes fails, even if it ran without error.

`handover` builds what a verifier is given in its first round
(docs/protocol.md): the executed notebooks with the conclusions removed (every
markdown cell that begins "**Result:" and everything from the "## Summary"
heading on), the helper modules and the claims files, in
[... 163 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; python - <<'EOF'
s=open('wm.py').read()
a=s.index('def glm_permutation('); b=s.index('# ---------------------------------------------------------------------------------------------\n# Concept cells')
new='''def glm_fit(counts_by_neuron, x_by_neuron, perms_by_neuron):
    """Real and permutation-null slopes for each neuron (Methods, Generalized linear model encoding
    analysis; main_1e,f.py:150-170). counts_by_neuron and x_by_neuron are per-neuron arrays;
    perms_by_neuron gives for each neuron an index array (n_perm x n_trials) that permutes its
    predictor. The predictor is z-scored before fitting (main_1e,f.py:128)."""
    n = len(counts_by_neuron)
    real, null = np.empty(n), None
    for j in range(n):
        x = np.asarray(x_by_neuron[j], float)
        xz = (x - x.mean()) / (x.std() + 1e-12)
        real[j] = poisson_slopes(counts_by_neuron[j], xz[None, :])[0]
        nb = poisson_slopes(counts_by_neuron[j], xz[perms_by_neuron[j]])
        if null is None:
            null = np.empty((n, len(nb)))
        null[j] = nb
    return real, null


def glm_groups(real, null, groups, alpha=0.05):
    """A neuron is significant when |b1| is at or above the 95th percentile ('higher' quantile) of
    its |null|; a group's p is the fraction of null counts of significant neurons at or above the
    observed count (main_1e,f.py:172-205; no + 1, as in the code). groups: {name: index array}."""
    absn = np.abs(null)
    thr = np.quantile(absn, 1 - alpha, axis=1, method="higher")
    sig = np.abs(real) >= thr
    sig_null = absn >= thr[:, None]
    out = []
    for g, idx in groups.items():
        idx = np.asarray(idx)
        obs = int(sig[idx].sum())
        nc = sig_null[idx].sum(0)
        out.append({"group": g, "n": len(idx), "significant": obs,
                    "percent": 100 * obs / max(len(idx), 1), "null_mean": nc.mean(),
                    "p": float(np.mean(nc >= obs))})
    return pd.DataFrame(out), sig


'''
s=s[:a]+new+s[b:]
s+='''

def perm_null_loo(K, y, n_perm, seed):
    """LOOCV accuracies of the SVM with labels shuffled n_perm times (the code permutes the labels
    of all trials, then runs the same LOOCV; main_2f,supp_1g.py:77-83)."""
    rng = np.random.default_rng(seed)
    return np.array([loo_correct(K, rng.permutation(y)).mean() for _ in range(n_perm)])


def ct_perm_maps(X, y, seeds):
    """Cross-temporal accuracy maps with shuffled labels, one per seed."""
    return [loo_cross_temporal(X, np.random.default_rng(s).permutation(y)) for s in seeds]


def pmap(func, args_list, n_jobs=4):
    """Run func(*args) for each args in parallel processes (joblib)."""
    from joblib import Parallel, delayed
    return Parallel(n_jobs=n_jobs)(delayed(func)(*a) for a in args_list)


CODE_REPO = "https://raw.githubusercontent.com/dariakussovska/heterogeneitywm"
CODE_COMMIT = "5144fe80876d14e8aacb4044977c3474c454f14b"


def code_table(path):
    """A table shipped in the paper's code repository, read over HTTP at the pinned commit."""
    import io
    r = requests.get(f"{CODE_REPO}/{CODE_COMMIT}/{path}", timeout=120)
    r.raise_for_status()
    return pd.read_excel(io.BytesIO(r.content))
'''
open('wm.py','w').write(s)
EOF
grep -n "glm_permutation" wm.py; echo done
```

```
done
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; cat >> wm.py <<'EOF'


def stable_seed(*parts):
    """A seed from names and numbers that does not change between runs (Python's hash does)."""
    import zlib
    return zlib.crc32("|".join(map(str, parts)).encode())


def type_shuffle_null(py_trials, in_trials, win, rng, n_shuffle=100, rule="prominence", distance=2):
    """Null burst counts for the PY and IN groups of one participant from shuffling the cell-type
    labels among its PY and IN neurons, group sizes kept (a reading of the Results' 'label-shuffled
    null'). Returns (mean null count for the PY-sized group, for the IN-sized group)."""
    pool = list(py_trials) + list(in_trials)
    k = len(py_trials)
    n_tr = len(pool[0])
    outp, outi = [], []
    for _ in range(n_shuffle):
        perm = rng.permutation(len(pool))
        for sel, out in [(perm[:k], outp), (perm[k:], outi)]:
            pooled = np.concatenate([concat_trials(pool[j], win) for j in sel])
            sm = smooth_counts(pooled, n_tr * win)
            out.append(len(burst_peaks(sm, np.percentile(sm, BURST_PCT), rule, distance)))
    return float(np.mean(outp)), float(np.mean(outi))
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part1.py",
 "content": "CELLS = []\n\n\ndef md(s):\n    CELLS.append((\"markdown\", s.strip(\"\\n\"), []))\n\n\ndef code(s, tags=()):\n    CELLS.append((\"code\", s.strip(\"\\n\"), list(tags)))\n\n\nmd(r\"\"\"\n# Reproducing Kussovska, Kim and Rungratsameetaweemana (2025) from dandiset 000469\n\n**Paper.** Kussovska D, Kim R, Rungratsameetaweemana N (2025). Neural heterogeneity shapes the\ntemporal structure of human working memory. bioRxiv,\n[doi:10.1101/2025.10.31.684900](https://doi.org/10.1101/2025.10.31.684900). The claims file\n(`claims/kussovska-2025.yaml`) was written from the bioRxiv full text posted on 1 November 2025\n(main text, figure legends and Methods; the Extended Data figures and their legends were not in\nthe text read).\n\n**Dandiset.** [DANDI:000469](https://dandiarchive.org/dandiset/000469/0.231213.2047), version\n0.231213.2047 (Kyzar et al. 2024, human single neurons during a Sternberg working memory task).\nThis is the version the paper cites (Methods, Participants and data source, and Data\navailability). The four published versions (0.231213.2047, 0.240122.1800, 0.240122.1812,\n0.240123.1806) hold the same 41 assets with the same asset identifiers and sizes, which the data\ncheck below confirms, so the version the paper's code downloads (0.240123.1806) gives the same\ndata.\n\n**Paper's code.** github.com/dariakussovska/heterogeneitywm at commit 5144fe8, the commit the\nclaims file read. Four of its shipped tables are outside inputs here:\n`data/new_trial_info.xlsx` (the 96 load-matched trials of the GLM),\n`data/new_trial_final.xlsx` (the 75 identity-matched trials of the pseudo-population decoding),\nboth of which the claims file names as readings, and, for comparison only (no outcome rests on\nthem), `data/all_neuron_brain_regions_cleaned.xlsx` (the code's concept-cell list) and\n`data/cell_analysis/Cell_metrics.xlsx` (the code's ACG features). The rodent validation claim uses\n`data/cell_analysis/validation_data.xlsx`, the features of the CellExplorer ground-truth cells\n(`data: elsewhere`).\n\n| Claim | Tested here |\n|---|---|\n| units-by-region, behavior-accuracy, fig1c-accuracy-load1-vs-load3, behavior-rt, rt-in-vs-out-memory, rt-correct-vs-incorrect | tested |\n| fig1e-load-modulated-neurons, fig1f-rt-modulation-not-significant | tested |\n| concept-cells-count, fig2ab-single-cells-not-persistent, fig2c-population-persistence, ext1bc-persistence-by-load | tested |\n| fig2d-cross-temporal-localized, ext1de-cross-temporal-load23 | tested |\n| fig2e-maintenance-decoding-amy-mtl, ext1f-maintenance-decoding-load2 | tested |\n| fig2f-bin-width-decoding, fig2f-bin-width-pairwise, ext1g-bin-width-load2 | tested |\n| fig3abc-trajectory-complexity, fig3d-encoding-vs-maintenance-separability, fig3h-early-vs-late-maintenance | blocked (too large; the time of one dPCA fit is measured below) |\n| fig4c-encoding-bursts-vs-poisson, fig4d-maintenance-bursts-vs-poisson, fig4-acg-group-differences, fig4f-all-cells-epochs, fig4hj-group-epochs, ext2-bursts-loads23 | tested |\n| acg-fit-yield, fig5c-cell-type-clusters, fig5dfh-cluster-features, fig5gh-burst-index-cv2, fig5kl-concept-cell-types | tested |\n| supp4-rodent-validation | tested on the features shipped with the paper's code (`data: elsewhere`) |\n| fig6ab-celltype-bursts-vs-null, fig6cd-celltype-epochs, ext5bd-in-load-dependence | tested |\n| fig6e-load-modulation-in, fig6f-rt-modulation-in-concept, fig6gh-in-concept-cv2, ext5gh-py-decay-preferred | tested |\n| fig6i-py-bin-width-decoding, fig6j-in-bin-width-decoding, fig6kl-cross-temporal-by-type, ext5ij-load2-decoding-by-type | tested |\n\nEach claim's section quotes it, runs every reading its criterion names, and ends with a\nconclusion. Random generators are seeded per section.\n\"\"\")\n\ncode(r\"\"\"\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport requests\nfrom scipy import stats\nfrom scipy.stats import wilcoxon, mannwhitneyu, kruskal, binom, binomtest\nfrom scipy import ndimage\n\nimport wm\n\nwarnings.filterwarnings(\"ignore\")\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\nT0 = time.time()\n\nsessions = wm.load_all()\nBY = {s[\"sub\"]: s for s in sessions}\nNT = wm.neuron_table(sessions)\nT = {s[\"sub\"]: wm.trial_frame(s) for s in sessions}\nSPK = [wm.spikes_of(BY, r) for _, r in NT.iterrows()]\nFIX = [wm.fixation_stats(SPK[n], T[NT[\"sub\"].iat[n]]) for n in range(len(NT))]\nprint(f\"streamed {len(sessions)} Sternberg files of dandiset {wm.DANDISET_ID} version {wm.DANDISET_VERSION} \"\n      f\"in {time.time() - T0:.0f} s\")\n\n# Outside inputs from the paper's code repository at the pinned commit.\nINFO = wm.code_table(\"data/new_trial_info.xlsx\")\nFINAL = wm.code_table(\"data/new_trial_final.xlsx\")\nSHIP_REG = wm.code_table(\"data/all_neuron_brain_regions_cleaned.xlsx\")\nSHIP_CM = wm.code_table(\"data/cell_analysis/Cell_metrics.xlsx\")\nVALID = wm.code_table(\"data/cell_analysis/validation_data.xlsx\")\nprint(\"code tables:\", {k: v.shape for k, v in dict(INFO=INFO, FINAL=FINAL, SHIP_REG=SHIP_REG,\n                                                  SHIP_CM=SHIP_CM, VALID=VALID).items()})\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nEach check of the description against the values is stated under its output.\n\"\"\")\n\ncode(r\"\"\"\n# Versions: the same assets in every published version.\nvers = [v[\"version\"] for v in requests.get(f\"{wm.API}/dandisets/{wm.DANDISET_ID}/versions/\").json()[\"results\"]]\nlisting = {v: wm.list_assets(v) for v in vers}\nsig = {v: sorted((a[\"path\"], a[\"asset_id\"], a[\"size\"]) for a in listing[v]) for v in vers}\nprint(\"versions:\", vers)\nfor v in vers:\n    print(f\"  {v}: {len(listing[v])} assets, {sum(a['size'] for a in listing[v]) / 1e9:.2f} GB, \"\n          f\"same assets as {wm.DANDISET_VERSION}: {sig[v] == sig[wm.DANDISET_VERSION]}\")\npaths = [a[\"path\"] for a in listing[wm.DANDISET_VERSION]]\nprint(\"files per session type:\", pd.Series([p.split(\"_\")[1] for p in paths]).value_counts().to_dict(),\n      \"; subjects:\", len({p.split(\"/\")[0] for p in paths}))\nprint(\"paper: 21 patients, 41 recording sessions\")\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe pinned version holds 41 files, a screening session (`ses-1`) and a Sternberg session\n(`ses-2`) for each of 21 subjects except sub-19, which has only `ses-2`: 41 sessions from 21\npatients, as the paper says. Every published version holds the same assets. The analysis reads\nonly the 21 Sternberg files, as the paper's code does.\n\"\"\")\n\ncode(r\"\"\"\nsubj = pd.DataFrame([{\"sub\": s[\"sub\"], \"age\": s[\"subject\"][\"age\"], \"sex\": s[\"subject\"][\"sex\"],\n                      \"units\": len(s[\"units\"]), \"trials\": len(s[\"trials\"]),\n                      \"description\": s[\"session_description\"][:30]} for s in sessions])\nages = subj.age.str.extract(r\"P(\\d+)Y\")[0].astype(int)\nprint(subj.to_string(index=False))\nprint(f\"\\nage {ages.min()} to {ages.max()} years, mean {ages.mean():.2f} +/- {ages.std():.2f} (s.d.); \"\n      \"paper: 17 to 71, 36.10 +/- 15.45 (over 41 sessions)\")\nprint(\"trials per session:\", subj.trials.value_counts().to_dict(), \"; paper: 16 participants with 135 trials, 5 with 108\")\nprint(\"units:\", len(NT), \"; by region:\", NT.region.value_counts().to_dict())\nprint(\"location labels:\", sorted(NT.location.unique()))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe files hold 902 units (as the paper says) in five regions, each with a left and a right label.\nFifteen sessions have 135 trials and six have 108 (subjects 6, 7, 8, 9, 16 and 19); the paper\nsays sixteen and five. The ages run from 17 to 70; the paper's 17 to 71 and its mean are over\nsessions, which cannot be checked from one Sternberg file per subject.\n\"\"\")\n\ncode(r\"\"\"\ntr = pd.concat(T.values())\nrows = []\nfor sub, t in T.items():\n    rows.append({\"sub\": sub, \"n\": len(t), \"load1\": (t.load == 1).sum(), \"load2\": (t.load == 2).sum(),\n                 \"load3\": (t.load == 3).sum(), \"images\": sorted(set(t.img1)),\n                 \"fix_s\": f\"{(t.enc1 - t.fix_start).min():.3f}-{(t.enc1 - t.fix_start).max():.3f}\",\n                 \"enc1_s\": f\"{(t.timestamps_Encoding1_end - t.enc1).min():.3f}-{(t.timestamps_Encoding1_end - t.enc1).max():.3f}\",\n                 \"maint_s\": f\"{t.maint_dur.min():.3f}-{t.maint_dur.max():.3f}\",\n                 \"rt_s\": f\"{t.rt.min():.2f}-{t.rt.max():.2f}\",\n                 \"ordered\": bool(((t.enc1 > t.fix_start) & (t.maint > t.enc1) & (t.probe > t.maint)\n                                  & (t.timestamps_Response > t.probe)).all())})\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"\\nimage ids at encoding 2 and 3 on load 1 trials (unused positions):\",\n      sorted(set(tr[tr.load == 1].img2)), sorted(set(tr[tr.load == 1].img3)))\nprint(\"accuracy values:\", sorted(tr.correct.unique()), \"; probe_in_out values:\", sorted(tr.in_memory.unique()))\nprint(f\"maintenance duration over all trials {tr.maint_dur.min():.3f} to {tr.maint_dur.max():.3f} s \"\n      \"(paper: 2.5 to 2.8 s); fixation \"\n      f\"{(tr.enc1 - tr.fix_start).min():.3f} to {(tr.enc1 - tr.fix_start).max():.3f} s (paper: 0.9 to 1.0 s)\")\n# the second time unit check: spike times lie within the session's trial span\nspan = pd.DataFrame([{\"sub\": NT[\"sub\"].iat[n], \"first\": SPK[n][0] if len(SPK[n]) else np.nan,\n                      \"last\": SPK[n][-1] if len(SPK[n]) else np.nan} for n in range(len(NT))])\nlim = pd.DataFrame([{\"sub\": s, \"t0\": t.start_time.min(), \"t1\": t.stop_time.max()} for s, t in T.items()])\nm = span.groupby(\"sub\").agg(first=(\"first\", \"min\"), last=(\"last\", \"max\")).join(lim.set_index(\"sub\"))\nprint(\"spike times start before the first trial and end after the last in every session:\",\n      bool(((m[\"first\"] <= m.t0 + 60) & (m[\"last\"] >= m.t1 - 60)).all()),\n      f\"; session spans {((m['last'] - m['first']) / 60).min():.0f} to {((m['last'] - m['first']) / 60).max():.0f} min\")\nprint(\"units with fewer than 2 spikes:\", int((NT.n_spikes < 2).sum()))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nEvery session has equal numbers of trials per load and five images (ids 1 to 5) in its encoding\nperiods. The epoch timestamps are ordered in every trial. The maintenance and fixation\ndurations printed above are in seconds; they are compared with the paper's values there. Spike\ntimes are in seconds on the same clock as the trials table (they span the trials of each\nsession); the check by contrast below shows the alignment.\n\"\"\")\n\ncode(r\"\"\"\n# Clock check by contrast: image selectivity of each neuron 200 to 1000 ms after the first\n# encoding onset (the concept-cell window) against the same test in windows shifted 1 s and 2 s\n# earlier (fixation and the previous trial's probe), per session. With aligned clocks only the\n# true window should hold image information beyond the false-positive rate.\nrng = np.random.default_rng(1)\nrows = []\nfor sub, t in T.items():\n    nids = NT.nid[NT[\"sub\"] == sub].values\n    row = {\"sub\": sub, \"neurons\": len(nids)}\n    for shift in [0.0, -1.0, -2.0]:\n        k = 0\n        for n in nids:\n            r = wm.count_in(SPK[n], (t.enc1 + 0.2 + shift).values, (t.enc1 + 1.0 + shift).values) / 0.8\n            k += wm.concept_test(r, t.img1.values, rng, reading=\"code\")[2]\n        row[f\"selective_at_{shift:+.0f}s\"] = k\n    # evoked response: population rate 0-300 ms after onset over the 300 ms before\n    pre = sum(wm.count_in(SPK[n], (t.enc1 - 0.3).values, t.enc1.values).sum() for n in nids)\n    post = sum(wm.count_in(SPK[n], (t.enc1 + 0.2).values, (t.enc1 + 0.5).values).sum() for n in nids)\n    row[\"rate_200_500ms_over_pre\"] = round(post / max(pre, 1), 2)\n    rows.append(row)\nclk = pd.DataFrame(rows)\nprint(clk.to_string(index=False))\nprint(\"totals:\", clk[[c for c in clk.columns if c.startswith(\"selective\")]].sum().to_dict())\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nAcross sessions, many more neurons are image-selective in the window after the first encoding\nonset than in the shifted windows, and the population rate rises after image onset in most\nsessions (totals and per-session counts above). This shows that spike times and the trial table\nshare a clock in the sessions where neurons respond; a session with no selective neurons and no\nevoked rise in the table above cannot be checked this way.\n\"\"\")\n\ncode(r\"\"\"\n# Duplicate recordings: identical spike trains or identical trial tables across sessions.\nkeys = {}\ndups = []\nfor n in range(len(NT)):\n    s = SPK[n]\n    k = (len(s), round(float(s[:5].sum()), 6) if len(s) else 0.0)\n    if k in keys and NT[\"sub\"].iat[keys[k]] != NT[\"sub\"].iat[n]:\n        dups.append((keys[k], n))\n    keys.setdefault(k, n)\nprint(\"units with an identical spike train in another session:\", len(dups))\ntabs = {}\nfor sub, t in T.items():\n    key = tuple(np.round(t.enc1.values[:10] - t.enc1.values[0], 4))\n    tabs.setdefault(key, []).append(sub)\nprint(\"sessions with identical trial timing:\", [v for v in tabs.values() if len(v) > 1])\nseqs = {}\nfor sub, t in T.items():\n    seqs.setdefault(tuple(t.img1.values) + tuple(t.load.values), []).append(sub)\nprint(\"sessions sharing the same trial sequence (loads and image ids):\", [v for v in seqs.values() if len(v) > 1])\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nNo unit or trial timing is duplicated across sessions. Several sessions share one trial sequence\n(the same loads and image ids in the same order), which is expected if the task used a fixed\npseudorandom list; their timings differ, so these are separate recordings.\n\"\"\")\n\ncode(r\"\"\"\n# Link of the code's trial tables to the dataset's trials (needed by the readings that use them):\n# trial_id is the row number, and their loads, image indices and reaction times agree.\nrows = []\nfor sub, t in T.items():\n    ti = t.set_index(\"trial\")\n    for name, tab, cols in [(\"new_trial_info\", INFO, (\"num_images_presented\", \"RT\")),\n                            (\"new_trial_final\", FINAL, (\"num_images_presented\", \"RT \"))]:\n        x = tab[tab.subject_id == sub]\n        m = ti.loc[x.trial_id.values]\n        row = {\"table\": name, \"sub\": sub, \"rows\": len(x), \"loads_agree\": bool((x[cols[0]].values == m.load.values).all()),\n               \"rt_max_diff\": float(np.abs(x[cols[1]].values - m.rt.values).max())}\n        if name == \"new_trial_final\":\n            mp = pd.DataFrame({\"code\": x.stimulus_index_enc1.values, \"pic\": m.img1.values})\n            row[\"image_map_one_to_one\"] = bool(mp.groupby(\"code\").pic.nunique().max() == 1\n                                               and mp.groupby(\"pic\").code.nunique().max() == 1)\n        rows.append(row)\nlk = pd.DataFrame(rows)\nprint(lk.groupby(\"table\").agg(sessions=(\"sub\", \"size\"), rows_min=(\"rows\", \"min\"), rows_max=(\"rows\", \"max\"),\n                              loads_agree=(\"loads_agree\", \"all\"), rt_max_diff=(\"rt_max_diff\", \"max\")).to_string())\nprint(\"image index of new_trial_final maps one to one onto the dataset's picture ids in every session:\",\n      bool(lk.image_map_one_to_one.dropna().all()))\nf1 = FINAL[FINAL.num_images_presented == 1]\nprint(\"new_trial_final load-1 rows per session:\", f1.groupby(\"subject_id\").size().unique(),\n      \"; image index the same across sessions in every load-1 row:\",\n      bool((f1.groupby(\"trial_id_final\").stimulus_index_enc1.nunique() == 1).all()))\nfor L in [2, 3]:\n    fl = FINAL[FINAL.num_images_presented == L]\n    print(f\"load {L} rows per session: {fl.groupby('subject_id').size().unique()}; rows whose label image \"\n          f\"(position {L}) has the same index in every session: \"\n          f\"{(fl.groupby('trial_id_final')[f'stimulus_index_enc{L}'].nunique() == 1).mean():.2f}; \"\n          f\"label counts in subject 14: {fl[fl.subject_id == 14][f'stimulus_index_enc{L}'].value_counts().sort_index().to_dict()}\")\nids1 = INFO[INFO.subject_id == 1].new_trial_id.values\nprint(\"new_trial_info: rows per session\", INFO.groupby(\"subject_id\").size().unique(),\n      \"; subject 1's 96 ids present in every session:\",\n      all(set(ids1) <= set(INFO[INFO.subject_id == s].new_trial_id) for s in T),\n      \"; load the same across sessions for each id:\",\n      bool((INFO.groupby(\"new_trial_id\").num_images_presented.nunique() == 1).all()))\nok = (SHIP_REG.subject_id.values == NT[\"sub\"].values).all() and (SHIP_REG.Neuron_ID.values == NT.unit.values).all() \\\n     and (SHIP_REG.Location.values == NT.location.values).all()\nprint(\"the code's neuron table lists the dataset's 902 units in the same order, with the same locations:\", bool(ok))\n\"\"\", tags=[\"sanity\"])\n\nmd(r\"\"\"\nThe code's tables match the dataset trial by trial: `trial_id` is the row of the trials table,\nand loads and reaction times agree exactly. In the identity-matched table the image index of\nevery load-1 row is the same in all 21 sessions and maps one to one onto each session's picture\nids, so its load-1 rows can align a pseudo-population. Its load-2 and load-3 rows are not\naligned on the label image in every session (fractions above), so those pseudo-populations\nmix labels across sessions; the code takes subject 14's labels. The code's neuron table lists\nthe dataset's units in order.\n\"\"\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part2.py",
 "content": "md(r\"\"\"\n## units-by-region\n\n> Recordings from the 21 patients yielded 902 well-isolated units, 259 in the amygdala, 171 in the\n> dACC, 190 in the hippocampus, 250 in the preSMA and 32 in the vmPFC.\n\"\"\")\n\ncode(r\"\"\"\ncnt = NT.region.value_counts()\nprint(\"patients:\", NT[\"sub\"].nunique(), \"; units:\", len(NT))\nprint(pd.DataFrame({\"dataset\": cnt, \"paper\": pd.Series({\"AMY\": 259, \"dACC\": 171, \"HPC\": 190, \"preSMA\": 250, \"vmPFC\": 32})}).to_string())\nprint(\"\\nunits by participant and region:\")\nprint(pd.crosstab(NT[\"sub\"], NT.region).to_string())\n\"\"\", tags=[\"claim:units-by-region\"])\n\nmd(r\"\"\"\n**Result: reproduced.** 21 patients and 902 units, with exactly the paper's count in each of the\nfive regions (left and right merged).\n\"\"\")\n\nmd(r\"\"\"\n## behavior-accuracy\n\n> Task accuracy was 88.73% ± 1.25%.\n\"\"\")\n\ncode(r\"\"\"\nacc = tr.groupby(\"sub\").correct.mean() * 100\nprint(acc.round(2).to_dict())\nprint(f\"mean over the 21 participants {acc.mean():.2f}%, s.e.m. {acc.std(ddof=1) / np.sqrt(len(acc)):.2f}, \"\n      f\"s.d. {acc.std(ddof=1):.2f}; range {acc.min():.2f} to {acc.max():.2f}\")\nprint(f\"variant, pooled over all {len(tr)} trials: {100 * tr.correct.mean():.2f}%\")\nprint(\"paper: 88.73 +/- 1.25 (tolerance 87.48 to 89.98)\")\n\"\"\", tags=[\"claim:behavior-accuracy\"])\n\nmd(r\"\"\"\n**Result: reproduced.** The mean of the 21 participants' accuracies is printed above with its\ns.e.m., which is the spread the code computes; it matches the paper's value and spread. The\npooled variant is also shown.\n\"\"\")\n\nmd(r\"\"\"\n## fig1c-accuracy-load1-vs-load3\n\n> Accuracy was higher for load 1 than for load 3 trials across patients.\n\"\"\")\n\ncode(r\"\"\"\nal = tr.groupby([\"sub\", \"load\"]).correct.mean().unstack()\nprint((100 * al).round(1).to_string())\nprint(\"median accuracy by load:\", (100 * al.median()).round(2).to_dict())\nH, pk = kruskal(al[1], al[2], al[3])\nprint(f\"Kruskal-Wallis over loads H = {H:.3f}, p = {pk:.4g}\")\nfor a, b in [(1, 2), (1, 3), (2, 3)]:\n    u = mannwhitneyu(al[a], al[b], alternative=\"two-sided\")\n    print(f\"load {a} vs {b}: rank-sum U = {u.statistic:.1f}, p raw = {u.pvalue:.4f}, Bonferroni x3 = {min(1, 3 * u.pvalue):.4f}\")\nw = wilcoxon(al[1], al[3])\nprint(f\"variant, paired signed-rank load 1 vs 3: W = {w.statistic:.1f}, p = {w.pvalue:.4f}; \"\n      f\"load 1 higher in {(al[1] > al[3]).sum()} of 21, equal in {(al[1] == al[3]).sum()}\")\nprint(\"paper: rank-sum P = 0.027\")\n\"\"\", tags=[\"claim:fig1c-accuracy-load1-vs-load3\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Load 1 accuracy is higher than load 3 across patients; the rank-sum p\n(raw and Bonferroni) and the paired variant are printed above, with p < 0.05 under the raw\nreading.\n\"\"\")\n\nmd(r\"\"\"\n## behavior-rt\n\n> Reaction time for correct trials was 1.06 ± 0.28 s.\n\"\"\")\n\ncode(r\"\"\"\nc = tr[tr.correct == 1]\nmed = c.groupby(\"sub\").rt.median()\nmean = c.groupby(\"sub\").rt.mean()\nq = c.rt.quantile([0.25, 0.75])\nprint(f\"(a) mean of participants' median RT {med.mean():.3f} s (s.d. {med.std(ddof=1):.3f}); \"\n      f\"(b) mean of participants' mean RT {mean.mean():.3f} s (s.d. {mean.std(ddof=1):.3f}); \"\n      f\"(c) median over {len(c)} correct trials {c.rt.median():.3f} s (IQR {q.iloc[0]:.3f} to {q.iloc[1]:.3f}, half-IQR {(q.iloc[1] - q.iloc[0]) / 2:.3f}; trial s.d. {c.rt.std():.3f})\")\nprint(f\"RT range over correct trials {c.rt.min():.3f} to {c.rt.max():.3f} s\")\nprint(\"paper: 1.06 +/- 0.28 s (tolerance 0.78 to 1.34)\")\n\"\"\", tags=[\"claim:behavior-rt\"])\n\nmd(r\"\"\"\n**Result: reproduced.** All three readings fall within 0.78 to 1.34 s (values above).\n\"\"\")\n\nmd(r\"\"\"\n## rt-in-vs-out-memory\n\n> Reaction time was faster for probes held in memory than for probes not in memory.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(11)\n\n\ndef paired_signflip(d, rng, n=1000):\n    d = np.asarray(d)\n    null = np.abs((rng.choice([-1, 1], (n, len(d))) * d).mean(1))\n    return float((np.sum(null >= abs(d.mean())) + 1) / (n + 1))\n\n\ndef label_perm(x, lab, rng, n=1000):\n    obs = x[lab].mean() - x[~lab].mean()\n    null = np.array([(lambda p: x[p].mean() - x[~p].mean())(rng.permutation(lab)) for _ in range(n)])\n    return obs, float((np.sum(np.abs(null) >= abs(obs)) + 1) / (n + 1))\n\n\nfor name, sel in [(\"correct trials\", tr.correct == 1), (\"all trials\", tr.correct >= 0)]:\n    x = tr[sel]\n    d = x.groupby([\"sub\", \"in_memory\"]).rt.median().unstack()\n    diff = d[1] - d[0]\n    pa = paired_signflip(diff.values, rng)\n    obs, pb = label_perm(x.rt.values, x.in_memory.values == 1, rng)\n    print(f\"{name}: (a) median RT in memory {d[1].median():.3f} s, not in memory {d[0].median():.3f} s; \"\n          f\"per-participant difference mean {diff.mean():.3f} s, faster in {(diff < 0).sum()} of {len(diff)}; sign-flip p = {pa:.4f}\")\n    print(f\"   (b) pooled mean difference in - out = {obs:.3f} s, label permutation p = {pb:.4f}\")\nprint(\"paper: permutation test P = 0.001\")\n\"\"\", tags=[\"claim:rt-in-vs-out-memory\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Probes held in memory are answered faster, in most participants, with\np < 0.05 under every reading (above).\n\"\"\")\n\nmd(r\"\"\"\n## rt-correct-vs-incorrect\n\n> Correct decisions were faster than incorrect ones.\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(12)\nd = tr.groupby([\"sub\", \"correct\"]).rt.median().unstack().dropna()\ndiff = d[1] - d[0]\npa = paired_signflip(diff.values, rng)\nobs, pb = label_perm(tr.rt.values, tr.correct.values == 1, rng)\nprint(f\"(a) {len(d)} participants with incorrect trials; median of correct {d[1].median():.3f} s, incorrect {d[0].median():.3f} s; \"\n      f\"correct faster in {(diff < 0).sum()} of {len(diff)}; sign-flip p = {pa:.4f}\")\nprint(f\"(b) pooled mean difference correct - incorrect = {obs:.3f} s, label permutation p = {pb:.4f}\")\nprint(\"incorrect trials per participant:\", tr[tr.correct == 0].groupby(\"sub\").size().to_dict())\nprint(\"paper: permutation test P = 0.002\")\n\"\"\", tags=[\"claim:rt-correct-vs-incorrect\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Correct responses are faster than incorrect ones, with p < 0.05 under\nboth readings (above).\n\"\"\")\n\nmd(r\"\"\"\n## fig1e-load-modulated-neurons\n\n> During maintenance a significant proportion of neurons in the preSMA (19.6%), vmPFC (18.75%) and\n> dACC (10.53%) was modulated by memory load.\n\nSpike counts in the first 2.5 s of maintenance, a Poisson GLM on the z-scored predictor fitted by\nNewton's method (the same maximum-likelihood fit as the code's unpenalised `PoissonRegressor`;\nchecked against sklearn below), 1,000 permutations with seed 17. Trial readings: (a) the code's\n96 load-matched trials (`new_trial_info.xlsx`: subject 1's `new_trial_id`s, each neuron's count\nfrom its own session's trial with the same id), with the permutation shared over the trial vector\n(the code) or drawn within each participant (Methods); (b) all trials of each participant,\npermuted within participant.\n\"\"\")\n\ncode(r\"\"\"\nREG = {g: NT.nid[NT.region == g].values for g in [\"AMY\", \"HPC\", \"dACC\", \"preSMA\", \"vmPFC\"]}\nNP = 1000\n\n\ndef glm_design(pred, trials, perm, seed=17):\n    rng = np.random.default_rng(seed)\n    shared = np.array([rng.permutation(len(ids1)) for _ in range(NP)])\n    subperm, Y, X, P = {}, [], [], []\n    for n in range(len(NT)):\n        sub = NT[\"sub\"].iat[n]\n        t = T[sub].set_index(\"trial\")\n        if trials == \"matched\":\n            rows = INFO[INFO.subject_id == sub].set_index(\"new_trial_id\").loc[ids1, \"trial_id\"].values\n        else:\n            rows = t.index.values\n        tt = t.loc[rows]\n        Y.append(wm.count_in(SPK[n], tt.maint.values, tt.maint.values + 2.5))\n        if pred == \"rt_code\":\n            X.append(INFO[INFO.subject_id == 1].set_index(\"new_trial_id\").loc[ids1, \"RT\"].values)\n        else:\n            X.append(tt[\"load\" if pred == \"load\" else \"rt\"].values)\n        if perm == \"shared\":\n            P.append(shared)\n        else:\n            if sub not in subperm:\n                subperm[sub] = np.array([rng.permutation(len(rows)) for _ in range(NP)])\n            P.append(subperm[sub])\n    return Y, X, P\n\n\nGLM = {}\nfor pred in [\"load\", \"rt\", \"rt_code\"]:\n    for trials, perm in [(\"matched\", \"shared\"), (\"matched\", \"within\"), (\"all\", \"within\")]:\n        if pred == \"rt_code\" and trials == \"all\":\n            continue\n        Y, X, P = glm_design(pred, trials, perm)\n        GLM[(pred, trials, perm)] = (wm.glm_fit(Y, X, P), Y, X)\n\n# check of the fit against sklearn on 20 neurons\nfrom sklearn.linear_model import PoissonRegressor\n(real, null), Y, X = GLM[(\"load\", \"matched\", \"shared\")]\ndev = []\nfor n in range(0, 902, 45):\n    x = (X[n] - X[n].mean()) / X[n].std()\n    if Y[n].sum() > 0:\n        dev.append(abs(PoissonRegressor(alpha=0, max_iter=1000).fit(x[:, None], Y[n]).coef_[0] - real[n]))\nprint(f\"largest |slope - sklearn slope| over {len(dev)} neurons: {max(dev):.2e}\")\nprint(\"neurons with no maintenance spikes in the matched trials:\", int(sum(y.sum() == 0 for y in Y)))\nfor key in [(\"load\", \"matched\", \"shared\"), (\"load\", \"matched\", \"within\"), (\"load\", \"all\", \"within\")]:\n    (real, null), _, _ = GLM[key]\n    df, _ = wm.glm_groups(real, null, REG)\n    print(f\"\\nload, trials {key[1]}, permutation {key[2]}:\")\n    print(df.round(3).to_string(index=False))\nprint(\"\\npaper: preSMA 19.6% (P = 0.001), vmPFC 18.75% (P = 0.009), dACC 10.53% (P = 0.026); tolerance 10% of each\")\n\"\"\", tags=[\"claim:fig1e-load-modulated-neurons\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under reading (a) with the code's shared permutation, preSMA, vmPFC and\ndACC are each within tolerance with p < 0.05 (dACC exactly 10.53%, vmPFC exactly 18.75%); the\nwithin-participant permutation gives nearly the same. With all trials (reading b) the three\nregions stay significant, with somewhat higher percentages. The amygdala and hippocampus are not\nsignificant under any reading.\n\"\"\")\n\nmd(r\"\"\"\n## fig1f-rt-modulation-not-significant\n\n> No region had a significant proportion of neurons whose maintenance firing covaried with reaction\n> time after correction, although the amygdala (5.79%), preSMA (8.00%) and vmPFC (6.25%) showed\n> elevated percentages.\n\nThe GLM of the previous section with RT as the predictor; Benjamini-Hochberg over the five\nregions. The main analysis uses each trial's own RT; the code's predictor, subject 1's RT vector\nfor every neuron (main_1e,f.py:113), is the variant.\n\"\"\")\n\ncode(r\"\"\"\nfor key in [(\"rt\", \"matched\", \"shared\"), (\"rt\", \"matched\", \"within\"), (\"rt\", \"all\", \"within\"),\n            (\"rt_code\", \"matched\", \"shared\"), (\"rt_code\", \"matched\", \"within\")]:\n    (real, null), _, _ = GLM[key]\n    df, _ = wm.glm_groups(real, null, REG)\n    df[\"p_BH\"] = wm.bh(df.p)\n    label = \"each trial's own RT\" if key[0] == \"rt\" else \"variant, subject 1's RT vector (the code)\"\n    print(f\"\\n{label}; trials {key[1]}, permutation {key[2]}:\")\n    print(df.round(3).to_string(index=False))\nprint(\"\\npaper: AMY 5.79%, preSMA 8.00%, vmPFC 6.25%, none significant after correction\")\n\"\"\", tags=[\"claim:fig1f-rt-modulation-not-significant\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** With each trial's own reaction time, the claim's test finds regions\nwith a significant proportion of RT-modulated neurons after BH correction (preSMA, the amygdala\nand dACC under reading (a); see the p_BH column), and the percentages are higher than the\npaper's. The code's predictor, subject 1's RT vector applied to every neuron, gives the paper's\nthree percentages exactly (AMY 5.79%, preSMA 8.00%, vmPFC 6.25%) and no region significant after\ncorrection under the shared permutation, so the paper's numbers come from that predictor, which\npairs each neuron's counts with another participant's reaction times.\n\"\"\")\n\nmd(r\"\"\"\n## concept-cells-count\n\n> Of 902 neurons, 58 (6.4%) were concept cells, 4 ± 4 across participants, 70.69% of them in the\n> amygdala, 18.96% in the hippocampus, 1.72% in the dACC, 3.45% in the preSMA and 5.15% in the vmPFC.\n\nSpike counts 200 to 1000 ms after first-encoding onset on all trials; the two images with the\nhighest mean rate; bootstrap of the difference (1,000 resamples). Reading (a) is the Methods'\nbootstrap, (b) the code's; ten seeds each (the code sets none).\n\"\"\")\n\ncode(r\"\"\"\nCCR = {}\nrates = []\nfor n in range(len(NT)):\n    t = T[NT[\"sub\"].iat[n]]\n    rates.append((wm.count_in(SPK[n], (t.enc1 + 0.2).values, (t.enc1 + 1.0).values) / 0.8, t.img1.values))\nrows = []\nfor reading in [\"methods\", \"code\"]:\n    for seed in range(10):\n        rng = np.random.default_rng(seed)\n        res = pd.DataFrame([wm.concept_test(r, im, rng, reading=reading) for r, im in rates], columns=[\"pref\", \"p\", \"sig\"])\n        CCR[(reading, seed)] = res\n        reg = NT.region[res.sig.values].value_counts()\n        rows.append({\"reading\": reading, \"seed\": seed, \"concept\": int(res.sig.sum()),\n                     **{f\"%{g}\": round(100 * reg.get(g, 0) / max(res.sig.sum(), 1), 2) for g in [\"AMY\", \"HPC\", \"dACC\", \"preSMA\", \"vmPFC\"]}})\ncc_tab = pd.DataFrame(rows)\nprint(cc_tab.to_string(index=False))\nprint(\"\\nrange of counts:\", cc_tab.groupby(\"reading\").concept.agg([\"min\", \"max\"]).to_dict(\"index\"))\nCONCEPT = CCR[(\"code\", 0)].sig.values\nPREF = CCR[(\"code\", 0)].pref.values\nper = pd.Series(NT[\"sub\"].values[CONCEPT]).value_counts()\nprint(f\"\\nset used downstream: reading (b), seed 0, {CONCEPT.sum()} cells; per participant with any: \"\n      f\"{per.mean():.2f} +/- {per.std():.2f} over {len(per)} participants; over all 21: {per.reindex(range(1, 22), fill_value=0).mean():.2f} +/- {per.reindex(range(1, 22), fill_value=0).std():.2f}\")\nship = (SHIP_REG.Signi == \"Y\").values\nprint(f\"for comparison, the code's shipped list: {ship.sum()} cells, {int((ship & CONCEPT).sum())} shared with the set used here; \"\n      f\"cells in the shipped list found in k of the 10 code-reading seeds: \"\n      f\"{pd.Series(np.array([CCR[('code', s)].sig.values for s in range(10)]).sum(0)[ship]).value_counts().sort_index().to_dict()}\")\nprint(\"paper: 58 (tolerance 52.2 to 63.8); AMY 70.69% (63.6 to 77.8), HPC 18.96% (17.06 to 20.86)\")\n\"\"\", tags=[\"claim:concept-cells-count\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under the code's bootstrap (reading b) the count is 57 to 60 over ten\nseeds, the amygdala holds most concept cells and the amygdala and hippocampus shares are within\ntolerance (seed 0 gives the paper's regional counts exactly). The Methods' bootstrap (reading a)\nfinds fewer cells (range above), also within tolerance. The set used in later sections is\nreading (b), seed 0, a standard choice of seed; it shares all but one cell with the code's\nshipped list.\n\"\"\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part3.py",
 "content": "md(r\"\"\"\n## fig2ab-single-cells-not-persistent\n\n> Examined neuron by neuron, most concept cells did not maintain elevated firing for their\n> preferred image throughout the maintenance epoch.\n\nPer concept cell, load 1 trials, 50 ms bins of the first 2.5 s of maintenance, z-scored to\nfixation and smoothed (sigma one bin); preferred trials are those whose first image is the\ncell's preferred image. Reading (a): a permutation test per bin (1,000 shuffles of the\npreferred/nonpreferred labels), persistent when significantly higher on preferred trials in at\nleast half the bins; reading (b): persistent when the spike count is significantly higher on\npreferred trials in each of the 1 s windows M1 to M3 (M3 ends at the end of maintenance).\n\"\"\")\n\ncode(r\"\"\"\nCELLS_C = np.where(CONCEPT)[0]\n\n\ndef pref_mask(t, pref, load):\n    if load == 1:\n        return (t.img1 == pref).values\n    return ((t.img1 == pref) | (t.img2 == pref) | (t.img3 == pref)).values\n\n\nrows = []\nfor n in CELLS_C:\n    rng = np.random.default_rng(int(n))\n    t = T[NT[\"sub\"].iat[n]]\n    t = t[t.load == 1]\n    pm = pref_mask(t, PREF[n], 1)\n    Z = wm.psth_z(SPK[n], t.maint.values, 2.5, *FIX[n])\n    obs = Z[pm].mean(0) - Z[~pm].mean(0)\n    perms = [rng.permutation(pm) for _ in range(1000)]\n    null = np.array([Z[q].mean(0) - Z[~q].mean(0) for q in perms])\n    p = np.mean(np.abs(null) >= np.abs(obs), 0)\n    frac = np.mean((p < 0.05) & (obs > 0))\n    win = []\n    for i in range(3):\n        c = wm.count_in(SPK[n], t.maint.values + i, np.minimum(t.maint.values + i + 1, t.probe.values))\n        o = c[pm].mean() - c[~pm].mean()\n        nn = np.array([c[q].mean() - c[~q].mean() for q in perms])\n        win.append(bool(o > 0 and np.mean(np.abs(nn) >= abs(o)) < 0.05))\n    rows.append({\"nid\": n, \"sub\": NT[\"sub\"].iat[n], \"region\": NT.region.iat[n], \"pref_trials\": int(pm.sum()),\n                 \"frac_bins_higher\": frac, \"M1\": win[0], \"M2\": win[1], \"M3\": win[2]})\nsc = pd.DataFrame(rows)\nsc[\"persistent_a\"] = sc.frac_bins_higher >= 0.5\nsc[\"persistent_b\"] = sc[[\"M1\", \"M2\", \"M3\"]].all(1)\nprint(sc.round(2).to_string(index=False))\nprint(f\"\\n{len(sc)} concept cells; preferred load-1 trials per cell {sc.pref_trials.min()} to {sc.pref_trials.max()}\")\nprint(f\"persistent under (a): {sc.persistent_a.sum()}; not persistent: {(~sc.persistent_a).sum()}\")\nprint(f\"persistent under (b): {sc.persistent_b.sum()}; not persistent: {(~sc.persistent_b).sum()}\")\nprint(\"cells significant in M1, M2, M3:\", sc[[\"M1\", \"M2\", \"M3\"]].sum().to_dict())\nprint(\"by participant (persistent a / cells):\", sc.groupby(\"sub\").agg(cells=(\"nid\", \"size\"), pa=(\"persistent_a\", \"sum\"), pb=(\"persistent_b\", \"sum\")).T.to_dict())\nfor thr in [0.25, 0.75]:\n    print(f\"threshold variant, persistent when at least {thr:.0%} of bins are higher: {(sc.frac_bins_higher >= thr).sum()} of {len(sc)}\")\n\"\"\", tags=[\"claim:fig2ab-single-cells-not-persistent\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under both readings most concept cells are not persistent (counts above),\nand this holds with a looser or stricter bin threshold.\n\"\"\")\n\nmd(r\"\"\"\n## fig2c-population-persistence\n\n> Averaged across the 58 concept cells, firing on preferred trials stayed higher than on\n> nonpreferred trials across the maintenance epoch of load 1 trials, a pattern of persistent\n> activity.\n\nPer cell the trial-mean z-scored, smoothed rate (50 ms bins) on preferred and nonpreferred\ntrials, in the first encoding second, the first 2.5 s of maintenance and the first second of the\nprobe (the three panels); per bin a bootstrap over cells (1,000, seed 42) of the mean preferred\nminus nonpreferred difference, two-sided, BH over all bins of all panels (per-panel BH as a\nvariant). Readings: (a) significant bins cover at least half the maintenance bins; (b) every 500 ms\nsegment holds a significant bin.\n\"\"\")\n\ncode(r\"\"\"\ndef population_persistence(load, seed=42):\n    D = {\"enc\": [], \"maint\": [], \"probe\": []}\n    for n in CELLS_C:\n        t = T[NT[\"sub\"].iat[n]]\n        t = t[t.load == load]\n        pm = pref_mask(t, PREF[n], load)\n        enc_on = {1: t.enc1, 2: t.timestamps_Encoding2, 3: t.timestamps_Encoding3}[1].values\n        for ep, on, dur in [(\"enc\", enc_on, 1.0), (\"maint\", t.maint.values, 2.5), (\"probe\", t.probe.values, 1.0)]:\n            Z = wm.psth_z(SPK[n], on, dur, *FIX[n])\n            D[ep].append(np.c_[Z[pm].mean(0), Z[~pm].mean(0)])\n    rng = np.random.default_rng(seed)\n    idx = rng.integers(0, len(CELLS_C), (1000, len(CELLS_C)))\n    out = {}\n    for ep, arr in D.items():\n        a = np.array(arr)  # cells x bins x (pref, nonpref)\n        d = a[:, :, 0] - a[:, :, 1]\n        b = d[idx].mean(1)\n        p = np.minimum(1, 2 * np.minimum(np.mean(b <= 0, 0), np.mean(b >= 0, 0)))\n        out[ep] = (a.mean(0), d.mean(0), p)\n    allp = np.concatenate([out[e][2] for e in [\"enc\", \"maint\", \"probe\"]])\n    q = wm.bh(allp)\n    nb = {e: len(out[e][2]) for e in out}\n    qm = q[nb[\"enc\"]:nb[\"enc\"] + nb[\"maint\"]]\n    sig = (qm < 0.05) & (out[\"maint\"][1] > 0)\n    sig_panel = (wm.bh(out[\"maint\"][2]) < 0.05) & (out[\"maint\"][1] > 0)\n    return out, sig, sig_panel\n\n\nPERSIST = {}\nfor load in [1, 2, 3]:\n    out, sig, sigp = population_persistence(load)\n    PERSIST[load] = (out, sig, sigp)\n    seg = [bool(sig[i * 10:(i + 1) * 10].any()) for i in range(5)]\n    m = out[\"maint\"][0]\n    print(f\"load {load}: maintenance mean z preferred {m[:, 0].mean():.3f}, nonpreferred {m[:, 1].mean():.3f}; \"\n          f\"preferred above nonpreferred in {np.mean(m[:, 0] > m[:, 1]):.2f} of bins; significant bins (BH all panels) \"\n          f\"{sig.mean():.2f} (per-panel BH {sigp.mean():.2f}); 500 ms segments with a significant bin {seg}\")\n    print(f\"   ranges: preferred {m[:, 0].min():.2f} to {m[:, 0].max():.2f}, nonpreferred {m[:, 1].min():.2f} to {m[:, 1].max():.2f}\")\nout = PERSIST[1][0]\nfig, ax = plt.subplots(1, 3, figsize=(12, 3), sharey=True)\nfor a, ep, dur in zip(ax, [\"enc\", \"maint\", \"probe\"], [1.0, 2.5, 1.0]):\n    x = np.arange(len(out[ep][1])) * 0.05\n    a.plot(x, out[ep][0][:, 0], label=\"preferred\")\n    a.plot(x, out[ep][0][:, 1], label=\"nonpreferred\")\n    a.set_title(f\"{ep}, load 1\")\n    a.set_xlabel(\"s from onset\")\nax[0].set_ylabel(\"z-scored rate\")\nax[0].legend()\nplt.show()\n\"\"\", tags=[\"claim:fig2c-population-persistence\"])\n\nmd(r\"\"\"\n**Result: reproduced.** At load 1 the population's preferred trace is above the nonpreferred one\nthroughout maintenance and the significant bins meet both readings (above). No point of the\nplot falls outside its axes, whose ranges are printed.\n\"\"\")\n\nmd(r\"\"\"\n## ext1bc-persistence-by-load\n\n> The population-level persistence of concept cells was robust at loads 1 and 2 and attenuated at\n> load 3.\n\nSame analysis on load 2 and load 3 trials, a trial preferred when any encoded image is the\npreferred image; the measure is the fraction of significant maintenance bins.\n\"\"\")\n\ncode(r\"\"\"\nfor load in [1, 2, 3]:\n    out, sig, sigp = PERSIST[load]\n    seg = [bool(sig[i * 10:(i + 1) * 10].any()) for i in range(5)]\n    print(f\"load {load}: fraction of maintenance bins significant {sig.mean():.2f} (per-panel BH {sigp.mean():.2f}); \"\n          f\"meets reading (a) {sig.mean() >= 0.5}, reading (b) {all(seg)}; mean difference {out['maint'][1].mean():.3f} z\")\n\"\"\", tags=[\"claim:ext1bc-persistence-by-load\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Loads 1 and 2 meet the persistence readings and load 3 has a smaller\nfraction of significant bins than either (above).\n\"\"\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part3.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part4.py",
 "content": "md(r\"\"\"\n## fig2d-cross-temporal-localized\n\n> In load 1 trials, decoders trained at specific times of encoding or early maintenance classified\n> the image above chance at other times, but cross-time generalization clusters were sparse and\n> temporally localized, so the information was not stably held across maintenance.\n\nA pseudo-population of the concept cells on the code's identity-matched trials (load-1 rows of\n`new_trial_final.xlsx`, 30 trials, 6 per image; labels the first image), spike counts in 250 ms\nwindows stepped by 100 ms from first-encoding onset over 5 s (the code's duration for load 1),\nz-scored with fixation; a linear SVM trained at each bin and tested at every bin with LOOCV. Per\npair a binomial test against 20%, one-sided (P(X >= k)) or two-sided, BH over the grid. Cluster\nrules: (i) the code's, contours of the significance mask longer than 13 points\n(`skimage.measure.find_contours`); (ii) the Methods', a cluster-duration null from 1,000 label\nshuffles, a cluster kept when its temporal extent (the longer side of its bounding box, in bins,\na choice of this attempt) exceeds the 95th percentile of the largest extent per shuffled map.\n\"\"\")\n\ncode(r\"\"\"\nfrom skimage import measure\n\n\ndef ct_design(nids, load, label):\n    subs = sorted(set(NT[\"sub\"].values[nids]))\n    rows, _ = wm.pseudo_rows(T, subs, load, \"code\", FINAL)\n    f14 = FINAL[(FINAL.subject_id == 14) & (FINAL.num_images_presented == load)].sort_values(\"trial_id_final\")\n    y = f14[\"stimulus_index_enc1\" if label == \"first\" else f\"stimulus_index_enc{load}\"].values\n    dur = {1: 5, 2: 6, 3: 7}[load]\n    st = wm.window_starts(0.25, 0.1, dur)\n    X = np.zeros((len(y), len(nids), len(st)))\n    for j, n in enumerate(nids):\n        sub = NT[\"sub\"].iat[n]\n        t = T[sub].set_index(\"trial\").loc[rows[sub]]\n        X[:, j, :] = wm.zcounts(SPK[n], t.enc1.values, st, 0.25, *FIX[n])\n    # epoch edges relative to first-encoding onset, mean over the participants' trials used\n    rel = np.mean([(T[s].set_index(\"trial\").loc[rows[s]].maint - T[s].set_index(\"trial\").loc[rows[s]].enc1).mean() for s in subs])\n    return X, y, st, rel\n\n\ndef sig_mask(acc, N, side):\n    k = np.round(acc * N).astype(int)\n    if side == \"one\":\n        p = binom.sf(k - 1, N, 0.2)\n    else:\n        p = np.vectorize(lambda kk: binomtest(int(kk), N, 0.2).pvalue)(k)\n    q = wm.bh(p.ravel()).reshape(p.shape)\n    return (q < 0.05) & (acc > 0.2)\n\n\ndef clusters(mask):\n    lab, n = ndimage.label(mask)\n    out = []\n    for i, sl in enumerate(ndimage.find_objects(lab)):\n        ext = max(sl[0].stop - sl[0].start, sl[1].stop - sl[1].start)\n        out.append((i + 1, ext))\n    return lab, out\n\n\ndef code_rule(mask):\n    keep = np.zeros_like(mask)\n    for c in measure.find_contours(mask.astype(float), 0.5):\n        if len(c) > 13:\n            r0, r1 = int(np.floor(c[:, 0].min())), int(np.ceil(c[:, 0].max()))\n            c0, c1 = int(np.floor(c[:, 1].min())), int(np.ceil(c[:, 1].max()))\n            keep[r0:r1 + 1, c0:c1 + 1] |= mask[r0:r1 + 1, c0:c1 + 1]\n    return keep\n\n\ndef ct_analysis(nids, load, label, n_perm=1000, seed=0):\n    X, y, st, rel = ct_design(nids, load, label)\n    acc = wm.loo_cross_temporal(X, y)\n    seeds = [wm.stable_seed(\"ct\", load, label, len(nids), seed, i) for i in range(n_perm)]\n    chunks = [seeds[i::4] for i in range(4)]\n    perm_maps = sum(wm.pmap(wm.ct_perm_maps, [(X, y, c) for c in chunks]), [])\n    res = {\"acc\": acc, \"st\": st, \"rel\": rel, \"N\": len(y)}\n    for side in [\"one\", \"two\"]:\n        m = sig_mask(acc, len(y), side)\n        null_ext = []\n        for pm in perm_maps:\n            _, cl = clusters(sig_mask(pm, len(y), side))\n            null_ext.append(max([e for _, e in cl], default=0))\n        thr = np.percentile(null_ext, 95)\n        lab, cl = clusters(m)\n        keep_perm = np.isin(lab, [i for i, e in cl if e > thr])\n        res[side] = {\"mask\": m, \"null95\": thr, \"perm\": keep_perm, \"code\": code_rule(m),\n                     \"null_ext_mean\": float(np.mean(null_ext))}\n    return res\n\n\ndef summarize_ct(res, name):\n    st, rel, acc = res[\"st\"], res[\"rel\"], res[\"acc\"]\n    enc_b = st + 0.25 <= rel\n    mb = (st >= rel) & (st + 0.25 <= rel + 2.5)\n    early = (st >= rel) & (st + 0.25 <= rel + 1.0)\n    offdiag = ~np.eye(len(st), dtype=bool)\n    rows = []\n    for side in [\"one\", \"two\"]:\n        for rule in [\"code\", \"perm\"]:\n            k = res[side][rule]\n            rows.append({\"map\": name, \"binomial\": side, \"cluster_rule\": rule,\n                         \"sig_pairs\": int(res[side][\"mask\"].sum()), \"kept_pairs\": int(k.sum()),\n                         \"kept_offdiag\": int((k & offdiag).sum()),\n                         \"train_bins_enc_or_early_with_offdiag\": int(((k & offdiag)[enc_b | early]).any(1).sum()),\n                         \"max_frac_maint_test_bins_from_a_maint_train_bin\": round(float(k[np.ix_(mb, mb)].mean(1).max()) if mb.any() else 0, 2),\n                         \"null95_extent\": res[side][\"null95\"]})\n    return pd.DataFrame(rows)\n\n\nCT = {}\nCT[(\"all\", 1, \"first\")] = ct_analysis(CELLS_C, 1, \"first\")\nr = CT[(\"all\", 1, \"first\")]\nprint(f\"{len(CELLS_C)} concept cells, {r['N']} trials, {len(r['st'])} bins; maintenance starts {r['rel']:.2f} s after first-encoding onset\")\nprint(f\"accuracy: diagonal mean {np.diag(r['acc']).mean():.3f}, range {r['acc'].min():.3f} to {r['acc'].max():.3f}; \"\n      f\"mean largest cluster extent in shuffled maps {r['one']['null_ext_mean']:.1f} bins\")\nprint(summarize_ct(r, \"load 1, all concept cells\").to_string(index=False))\nplt.imshow(r[\"acc\"] * 100, origin=\"lower\", vmin=0, vmax=100, cmap=\"viridis\")\nplt.contour(r[\"one\"][\"code\"], levels=[0.5], colors=\"r\")\nplt.xlabel(\"test bin\")\nplt.ylabel(\"train bin\")\nplt.colorbar(label=\"accuracy (%)\")\nplt.title(\"load 1 cross-temporal decoding (red: kept by the code's rule, one-sided)\")\nplt.show()\n\"\"\", tags=[\"claim:fig2d-cross-temporal-localized\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Decoders trained in encoding or early maintenance generalize above chance\nto other bins under every reading, and no maintenance training bin generalizes to more than half\nof the maintenance test bins (largest fraction above), so the clusters are localized.\n\"\"\")\n\nmd(r\"\"\"\n## ext1de-cross-temporal-load23\n\n> In load 2 and load 3 trials cross-time generalization was minimal.\n\nThe analysis of fig2d on load 2 (6 s) and load 3 (7 s) rows of the identity-matched table,\nlabels the first image (Methods) or the last (the code); \"minimal\" read as fewer off-diagonal\npairs in surviving clusters than at load 1 under the same rule.\n\"\"\")\n\ncode(r\"\"\"\nfor load in [2, 3]:\n    for label in [\"first\", \"last\"]:\n        CT[(\"all\", load, label)] = ct_analysis(CELLS_C, load, label)\ntabs = [summarize_ct(CT[(\"all\", 1, \"first\")], \"load 1\")]\nfor load in [2, 3]:\n    for label in [\"first\", \"last\"]:\n        tabs.append(summarize_ct(CT[(\"all\", load, label)], f\"load {load}, label {label}\"))\nct_tab = pd.concat(tabs)\nprint(ct_tab.to_string(index=False))\nbase = ct_tab[ct_tab[\"map\"] == \"load 1\"].set_index([\"binomial\", \"cluster_rule\"]).kept_offdiag\nfor label in [\"first\", \"last\"]:\n    for (side, rule), b in base.items():\n        v = [int(ct_tab[(ct_tab[\"map\"] == f\"load {L}, label {label}\") & (ct_tab.binomial == side) & (ct_tab.cluster_rule == rule)].kept_offdiag.iloc[0]) for L in [2, 3]]\n        print(f\"label {label}, {side}-sided, rule {rule}: off-diagonal kept pairs load 1 {b}, load 2 {v[0]}, load 3 {v[1]}; both fewer: {v[0] < b and v[1] < b}\")\n\"\"\", tags=[\"claim:ext1de-cross-temporal-load23\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under both labels and every rule, loads 2 and 3 keep fewer off-diagonal\npairs than load 1 (above).\n\"\"\")\n\nmd(r\"\"\"\n## fig2e-maintenance-decoding-amy-mtl\n\n> Concept cells in the amygdala and in the MTL carried significant stimulus information during\n> load 1 maintenance (35.56% and 32.13% decoding accuracy, chance 20%).\n\nWithin each participant, its concept cells in the region group, all its trials of the load,\nlabels the last image; z-scored counts in 1 s windows stepped by 250 ms over the first 2.5 s of\nmaintenance, concatenated; linear SVM, LOOCV; accuracy the mean over participants; p from 1,000\nlabel shuffles, (k + 1) / 1001 on the mean over participants, BH within the load over the six\nregion groups of the code (main_2e,supp_1f.py:14-21). Participants need at least three (Methods)\nor more than three (the code) concept cells in the group.\n\"\"\")\n\ncode(r\"\"\"\nGROUPS_WP = {\"AMY\": [\"AMY\"], \"HPC\": [\"HPC\"], \"dACC\": [\"dACC\"], \"preSMA\": [\"preSMA\"],\n             \"MTL\": [\"AMY\", \"HPC\"], \"dACC_preSMA\": [\"dACC\", \"preSMA\"]}\nST_WP = wm.window_starts(1.0, 0.25, 2.5)\n\n\ndef wp_unit(g, sub, load):\n    nids = NT[(NT[\"sub\"] == sub) & NT.region.isin(GROUPS_WP[g]) & CONCEPT[NT.nid]].nid.values\n    t = T[sub][T[sub].load == load]\n    y = t[\"last\"].values\n    X = np.concatenate([wm.zcounts(SPK[n], t.maint.values, ST_WP, 1.0, *FIX[n]) for n in nids], 1)\n    K = X @ X.T\n    return wm.loo_correct(K, y).mean(), wm.perm_null_loo(K, y, 1000, wm.stable_seed(\"wp\", g, sub, load))\n\n\nunits = []\nfor g, regs in GROUPS_WP.items():\n    for sub in sorted(T):\n        k = int((CONCEPT & (NT[\"sub\"] == sub).values & NT.region.isin(regs).values).sum())\n        if k >= 3:\n            for load in [1, 2, 3]:\n                units.append((g, sub, load, k))\nouts = wm.pmap(wp_unit, [(g, s, L) for g, s, L, _ in units])\nWP = pd.DataFrame([{\"group\": g, \"sub\": s, \"load\": L, \"cells\": k, \"acc\": a, \"null\": nl}\n                   for (g, s, L, k), (a, nl) in zip(units, outs)])\nprint(WP[WP.load == 1][[\"group\", \"sub\", \"cells\", \"acc\"]].assign(acc=lambda d: (100 * d.acc).round(2)).to_string(index=False))\n\n\ndef wp_stats(min_cells, load):\n    rows = []\n    for g in GROUPS_WP:\n        x = WP[(WP.group == g) & (WP.load == load) & (WP.cells >= min_cells)]\n        if len(x) == 0:\n            continue\n        m = x.acc.mean()\n        nm = np.mean(np.stack(x.null.values), 0)\n        rows.append({\"group\": g, \"participants\": len(x), \"accuracy_%\": round(100 * m, 2),\n                     \"null_mean_%\": round(100 * nm.mean(), 2), \"p\": (np.sum(nm >= m) + 1) / 1001})\n    df = pd.DataFrame(rows)\n    df[\"p_BH\"] = wm.bh(df.p)\n    return df\n\n\nfor mc, name in [(3, \"at least three cells (Methods)\"), (4, \"more than three cells (the code)\")]:\n    print(f\"\\nload 1, {name}:\")\n    print(wp_stats(mc, 1).to_string(index=False))\nprint(\"\\npaper: AMY 35.56% (P = 0.001), MTL 32.13% (P = 0.001); tolerance 32.0 to 39.1 and 28.9 to 35.3\")\n\"\"\", tags=[\"claim:fig2e-maintenance-decoding-amy-mtl\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** Within participant, amygdala and MTL concept cells do not decode the\nimage above the shuffled null at load 1 under either cell-count rule; accuracies are below 20%\nand near the null mean (above).\n\"\"\")\n\nmd(r\"\"\"\n## ext1f-maintenance-decoding-load2\n\n> Amygdala and MTL concept cells also carried significant information about the last image during\n> load 2 maintenance (23.56% and 28.89%).\n\"\"\")\n\ncode(r\"\"\"\nfor mc, name in [(3, \"at least three cells (Methods)\"), (4, \"more than three cells (the code)\")]:\n    print(f\"load 2, {name}:\")\n    print(wp_stats(mc, 2).to_string(index=False))\nprint(\"\\npaper: AMY 23.56% (P = 0.031), MTL 28.89% (P = 0.002)\")\n\"\"\", tags=[\"claim:ext1f-maintenance-decoding-load2\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** At load 2 neither group's accuracy is within tolerance with\np < 0.05 (above).\n\"\"\")\n\nmd(r\"\"\"\n## fig2f-bin-width-decoding\n\n> In load 1 trials, pseudo-population decoding of the image during maintenance was above chance at\n> every bin width and rose with bin width (250 ms 40.00%, 500 ms 56.67%, 750 ms 66.67%, 1000 ms\n> 80.00%).\n\nAll concept cells, z-scored counts in windows of each width slid by 25 ms over the first 2.5 s of\nmaintenance, concatenated; linear SVM, LOOCV; p from 1,000 label shuffles, (k + 1) / 1001; BH\nover the 12 tests of 4 widths and 3 loads. Trial readings: (a) the code's identity-matched rows\n(`new_trial_final.xlsx`), labels as the code takes them (subject 14's); (b) each participant's\nfirst six trials of each label image, aligned by image and rank. The fast SVM used here is\nchecked against sklearn's `SVC(kernel='linear')`.\n\"\"\")\n\ncode(r\"\"\"\nWIDTHS = [0.25, 0.5, 0.75, 1.0]\n\n\ndef bw_design(nids, load, reading, width):\n    subs = sorted(set(NT[\"sub\"].values[nids]))\n    rows, lab = wm.pseudo_rows(T, subs, load, reading, FINAL)\n    st = wm.window_starts(width, 0.025, 2.5)\n    B = []\n    for n in nids:\n        sub = NT[\"sub\"].iat[n]\n        t = T[sub].set_index(\"trial\").loc[rows[sub]]\n        B.append(wm.zcounts(SPK[n], t.maint.values, st, width, *FIX[n]))\n    return np.concatenate(B, 1), np.asarray(lab)\n\n\nX, y = bw_design(CELLS_C, 1, \"code\", 1.0)\nprint(\"fast SVM equals sklearn SVC(kernel='linear') on this design, every LOOCV prediction:\",\n      bool((wm.loo_correct(X @ X.T, y) == wm.loo_correct_sklearn(X, y)).all()))\n\n\ndef bw_unit(nids, reading, load, width, seed):\n    X, y = bw_design(nids, load, reading, width)\n    K = X @ X.T\n    return wm.loo_correct(K, y), wm.perm_null_loo(K, y, 1000, seed), X.shape\n\n\ndef bw_run(name, nids):\n    keys = [(reading, load, w) for reading in [\"code\", \"rank\"] for load in [1, 2, 3] for w in WIDTHS]\n    outs = wm.pmap(bw_unit, [(nids, r, L, w, wm.stable_seed(\"bw\", name, r, L, w)) for r, L, w in keys])\n    res = {k: o for k, o in zip(keys, outs)}\n    rows = []\n    for (reading, load, w), (real, null, shape) in res.items():\n        rows.append({\"reading\": reading, \"load\": load, \"width_ms\": int(w * 1000), \"trials\": shape[0], \"features\": shape[1],\n                     \"accuracy_%\": round(100 * real.mean(), 2), \"null_mean_%\": round(100 * null.mean(), 2),\n                     \"p\": (np.sum(null >= real.mean()) + 1) / 1001})\n    df = pd.DataFrame(rows)\n    df[\"p_BH\"] = np.nan\n    for reading in [\"code\", \"rank\"]:\n        m = df.reading == reading\n        df.loc[m, \"p_BH\"] = wm.bh(df.p[m])\n    return res, df\n\n\nBW = {}\nBW[\"all\"] = bw_run(\"all\", CELLS_C)\nprint(BW[\"all\"][1].to_string(index=False))\nprint(\"\\npaper, load 1: 40.00, 56.67, 66.67, 80.00% (tolerance 10% of each), Pmax = 0.001\")\n\"\"\", tags=[\"claim:fig2f-bin-width-decoding\"])\n\ncode(r\"\"\"\n# Variant: how the decoding depends on which six trials of each image enter. 20 random draws of\n# six load-1 trials per image in each participant (aligned by image and draw rank), 1000 ms width.\nrng = np.random.default_rng(23)\nsubs = sorted(set(NT[\"sub\"].values[CELLS_C]))\nst = wm.window_starts(1.0, 0.025, 2.5)\naccs = []\nfor d in range(20):\n    rows = {}\n    for s in subs:\n        t = T[s][T[s].load == 1]\n        rows[s] = np.concatenate([rng.permutation(t[t.img1 == im].trial.values)[:6] for im in range(1, 6)])\n    B = []\n    for n in CELLS_C:\n        sub = NT[\"sub\"].iat[n]\n        t = T[sub].set_index(\"trial\").loc[rows[sub]]\n        B.append(wm.zcounts(SPK[n], t.maint.values, st, 1.0, *FIX[n]))\n    Xr = np.concatenate(B, 1)\n    accs.append(wm.loo_correct(Xr @ Xr.T, np.repeat(np.arange(1, 6), 6)).mean())\naccs = 100 * np.array(accs)\nprint(f\"random six-per-image draws, load 1, 1000 ms: accuracy median {np.median(accs):.1f}%, range {accs.min():.1f} to {accs.max():.1f}%\")\nreal_code = 100 * BW[\"all\"][0][(\"code\", 1, 1.0)][0].mean()\nprint(f\"the code's table gives {real_code:.2f}%; draws at or above it: {(accs >= real_code).sum()} of 20\")\n\"\"\", tags=[\"claim:fig2f-bin-width-decoding\"])\n\nmd(r\"\"\"\n**Result: not reproduced.** Under the code's trial table (reading a) load-1 accuracy rises with\nbin width and is above chance at every width, but the 250 ms accuracy is outside its tolerance\n(values above); under reading (b), each participant's first six trials per image, accuracy is\nbelow chance at every width. Random draws of six trials per image fall between the two, so the\npaper's numbers depend on which trials the code's table holds, and how it was built is not\nstated.\n\"\"\")\n\nmd(r\"\"\"\n## fig2f-bin-width-pairwise\n\n> Pairwise, accuracy was higher for 750 than 250 ms, for 1000 than 250 ms and for 1000 than 500 ms\n> bins, while 500 against 250, 1000 against 750 and 750 against 500 ms did not differ after\n> correction.\n\nReadings: (a) a paired permutation over trials swapping each trial's LOOCV correctness between the\ntwo widths (1,000), two-sided; (b) the observed difference against the differences of the two\nwidths' shuffled nulls (paired by shuffle index), two-sided; BH over the six pairs.\n\"\"\")\n\ncode(r\"\"\"\nimport itertools\nrng = np.random.default_rng(31)\nPAIRS = [(0.75, 0.25), (1.0, 0.25), (1.0, 0.5), (0.5, 0.25), (1.0, 0.75), (0.75, 0.5)]\nfor reading in [\"code\", \"rank\"]:\n    res = BW[\"all\"][0]\n    rows = []\n    for a, b in PAIRS:\n        ca, na, _ = res[(reading, 1, a)]\n        cb, nb, _ = res[(reading, 1, b)]\n        obs = ca.mean() - cb.mean()\n        sw = rng.random((1000, len(ca))) < 0.5\n        nulla = (np.where(sw, cb, ca).mean(1) - np.where(sw, ca, cb).mean(1))\n        pa = (np.sum(np.abs(nulla) >= abs(obs)) + 1) / 1001\n        dn = na - nb\n        pb = (np.sum(np.abs(dn - dn.mean()) >= abs(obs)) + 1) / 1001\n        rows.append({\"pair_ms\": f\"{int(a * 1000)} vs {int(b * 1000)}\", \"diff_%\": round(100 * obs, 2), \"p_a\": pa, \"p_b\": pb})\n    df = pd.DataFrame(rows)\n    df[\"p_a_BH\"] = wm.bh(df.p_a)\n    df[\"p_b_BH\"] = wm.bh(df.p_b)\n    print(f\"trial reading {reading}:\")\n    print(df.round(4).to_string(index=False))\nprint(\"paper: 750 vs 250 P = 0.026, 1000 vs 250 P = 0.004, 1000 vs 500 P = 0.032; the other three P > 0.05\")\n\"\"\", tags=[\"claim:fig2f-bin-width-pairwise\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## ext1g-bin-width-load2\n\n> Bin width had little effect on decoding of the second image in load 2 trials, and load 2\n> accuracy was lower than load 1 accuracy.\n\"\"\")\n\ncode(r\"\"\"\ndf = BW[\"all\"][1]\nfor reading in [\"code\", \"rank\"]:\n    l1 = df[(df.reading == reading) & (df.load == 1)].set_index(\"width_ms\")[\"accuracy_%\"]\n    l2 = df[(df.reading == reading) & (df.load == 2)].set_index(\"width_ms\")[\"accuracy_%\"]\n    print(f\"reading {reading}: load 2 accuracies {l2.to_dict()}; range {l2.max() - l2.min():.2f} points \"\n          f\"(criterion: below half the load 1 range of 40.0, i.e. 20.0); below load 1 at every width: {bool((l2 < l1).all())}\")\n\"\"\", tags=[\"claim:ext1g-bin-width-load2\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part4.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
s=open('nb_part4.py').read()
old_wp=s[s.index('def wp_unit(g, sub, load):'):s.index('print(WP[WP.load == 1]')]
new_wp='''def wp_design(g, sub, load):
    nids = NT[(NT["sub"] == sub) & NT.region.isin(GROUPS_WP[g]) & CONCEPT[NT.nid]].nid.values
    t = T[sub][T[sub].load == load]
    X = np.concatenate([wm.zcounts(SPK[n], t.maint.values, ST_WP, 1.0, *FIX[n]) for n in nids], 1)
    return X @ X.T, t["last"].values


units, designs = [], []
for g, regs in GROUPS_WP.items():
    for sub in sorted(T):
        k = int((CONCEPT & (NT["sub"] == sub).values & NT.region.isin(regs).values).sum())
        if k >= 3:
            for load in [1, 2, 3]:
                units.append((g, sub, load, k))
                designs.append(wp_design(g, sub, load))
nulls = wm.pmap(wm.perm_null_loo, [(K, y, 1000, wm.stable_seed("wp", g, s, L)) for (g, s, L, _), (K, y) in zip(units, designs)])
WP = pd.DataFrame([{"group": g, "sub": s, "load": L, "cells": k, "acc": wm.loo_correct(K, y).mean(), "null": nl}
                   for (g, s, L, k), (K, y), nl in zip(units, designs, nulls)])
'''
s=s.replace(old_wp,new_wp)
old_bw=s[s.index('def bw_unit(nids, reading, load, width, seed):'):s.index('    rows = []\n    for (reading, load, w), (real, null, shape) in res.items():')]
new_bw='''def bw_run(name, nids):
    keys = [(reading, load, w) for reading in ["code", "rank"] for load in [1, 2, 3] for w in WIDTHS]
    des = [bw_design(nids, L, r, w) for r, L, w in keys]
    Ks = [X @ X.T for X, _ in des]
    nulls = wm.pmap(wm.perm_null_loo, [(K, y, 1000, wm.stable_seed("bw", name, *k)) for k, K, (_, y) in zip(keys, Ks, des)])
    res = {k: (wm.loo_correct(K, y), nl, X.shape) for k, K, (X, y), nl in zip(keys, Ks, des, nulls)}
'''
s=s.replace(old_bw,new_bw)
open('nb_part4.py','w').write(s)
EOF
grep -n "def bw_run\|res = {k\|pmap" $TMPDIR/nb_part4.py
```

```
74:    perm_maps = sum(wm.pmap(wm.ct_perm_maps, [(X, y, c) for c in chunks]), [])
198:nulls = wm.pmap(wm.perm_null_loo, [(K, y, 1000, wm.stable_seed("wp", g, s, L)) for (g, s, L, _), (K, y) in zip(units, designs)])
286:def bw_run(name, nids):
290:    nulls = wm.pmap(wm.perm_null_loo, [(K, y, 1000, wm.stable_seed("bw", name, *k)) for k, K, (_, y) in zip(keys, Ks, des)])
291:    res = {k: (wm.loo_correct(K, y), nl, X.shape) for k, K, (X, y), nl in zip(keys, Ks, des, nulls)}
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part5.py",
 "content": "md(r\"\"\"\n## fig3abc-trajectory-complexity, fig3d-encoding-vs-maintenance-separability, fig3h-early-vs-late-maintenance (blocked)\n\nThese claims rest on 100 stratified train/test splits, each with its own dPCA fit (Kobak's\npackage, regularization chosen by its built-in cross-validation, as `opt_regularizer_flag = True`\nin 03_dpca/main_3d,supp_2a,b,i.py:119-131) for encoding (1 s) and maintenance (2.5 s) in 2 ms\nbins, and for the early and late halves of maintenance. The cell below times one split of the\nclaim's design on the data (58 concept cells, 3 training trials per image).\n\"\"\")\n\ncode(r\"\"\"\nfrom dPCA.dPCA import dPCA\nfrom scipy.ndimage import gaussian_filter1d\n\nsubs = sorted(set(NT[\"sub\"].values[CELLS_C]))\nrows, lab = wm.pseudo_rows(T, subs, 1, \"code\", FINAL)\nrng = np.random.default_rng(3)\ntrain = np.concatenate([rng.permutation(np.where(lab == c)[0])[:3] for c in np.unique(lab)])\n\n\ndef dpca_tensor(onset_col, dur):\n    nb = int(round(dur / 0.002))\n    out = np.zeros((3, len(CELLS_C), 5, nb))\n    for j, n in enumerate(CELLS_C):\n        sub = NT[\"sub\"].iat[n]\n        t = T[sub].set_index(\"trial\").loc[rows[sub]]\n        mu, sd = FIX[n]\n        for ci, c in enumerate(np.unique(lab)):\n            idx = [i for i in train if lab[i] == c]\n            for r_, i in enumerate(idx):\n                on = t[onset_col].values[i]\n                e = on + np.arange(nb + 1) * 0.002\n                cnt = np.diff(np.searchsorted(SPK[n], e)) / 0.002\n                z = (cnt - mu) / sd if sd > 0 else cnt - mu\n                out[r_, j, ci] = gaussian_filter1d(z, 60)\n    return out\n\n\ntiming = {}\nfor name, col, dur in [(\"encoding\", \"enc1\", 1.0), (\"maintenance\", \"maint\", 2.5)]:\n    trialX = dpca_tensor(col, dur)\n    Xm = trialX.mean(0)\n    Xm = Xm - Xm.reshape(Xm.shape[0], -1).mean(1)[:, None, None]\n    t0 = time.time()\n    d = dPCA(labels=\"st\", regularizer=\"auto\")\n    d.opt_regularizer_flag = True\n    d.protect = []\n    d.fit_transform(Xm, trialX)\n    timing[name] = time.time() - t0\nprint({k: round(v, 1) for k, v in timing.items()}, \"s for one split\")\nper_split = timing[\"encoding\"] + timing[\"maintenance\"]\nprint(f\"fig3d needs 100 splits: about {100 * per_split / 60:.0f} min; fig3h adds two half-maintenance fits per split, \"\n      f\"about {100 * timing['maintenance'] / 60:.0f} min more (each half is half the bins); \"\n      f\"together about {100 * (per_split + timing['maintenance']) / 60:.0f} min, over the 60 min limit for a notebook\")\n\"\"\", tags=[\"claim:fig3d-encoding-vs-maintenance-separability\"])\n\nmd(r\"\"\"\n**Result: blocked (too large).** One split takes the time printed above, so the 100 splits of\nfig3d alone exceed the sixty-minute limit for a notebook, and fig3h and fig3abc (which uses the\nsame fits) add to it. The three claims are not tested.\n\"\"\")\n\nmd(r\"\"\"\n## acg-fit-yield\n\n> Fitting CellExplorer's triple-exponential model to each neuron's autocorrelogram and keeping\n> well-fit units (R2 > 0.3) left 294 neurons for cell-type analysis.\n\nA port of the code's MATLAB functions (calc_ACG_metrics.m, fit_ACG.m, Mean_ACG.m,\nnormalize_acg_to_unit.m): narrow ACG (+/- 50 ms, 0.5 ms bins), the triple exponential fitted with\nCellExplorer's start point and bounds by bounded nonlinear least squares (scipy's trust-region\nreflective method in place of MATLAB's `fit`). Readings: (a) every spike of the unit; (b) only\nspikes within the trials (fixation onset to response).\n\"\"\")\n\ncode(r\"\"\"\nFEAT = {}\nfor reading in [\"a\", \"b\"]:\n    rows = []\n    for n in range(len(NT)):\n        s = SPK[n]\n        if reading == \"b\":\n            t = T[NT[\"sub\"].iat[n]]\n            keep = np.zeros(len(s), bool)\n            for a_, b_ in zip(t.fix_start.values, t.timestamps_Response.values):\n                i, j = np.searchsorted(s, [a_, b_])\n                keep[i:j] = True\n            f = wm.acg_features(s[keep])\n            f[\"firing_rate\"] = len(s) / (s[-1] - s[0])\n        else:\n            f = wm.acg_features(s)\n        rows.append(f)\n    FEAT[reading] = pd.DataFrame(rows)\nfor reading in [\"a\", \"b\"]:\n    F = FEAT[reading]\n    print(f\"reading ({reading}): R2 > 0.3: {(F.r2 > 0.3).sum()}, R2 >= 0.3: {(F.r2 >= 0.3).sum()}, \"\n          f\"fits with no R2 (too few spikes): {F.r2.isna().sum()}; R2 median {F.r2.median():.3f}\")\nF = FEAT[\"a\"]\ncmp = pd.DataFrame({\n    \"feature\": [\"firing_rate\", \"acg_norm\", \"burst_royer\", \"cv_isi\", \"r2\", \"tau_rise\", \"tau_decay\"],\n    \"shipped_column\": [\"firing_rate\", \"acg_norm\", \"Burst\", \"CV2\", \"R2\", \"tau_rise\", \"Decay\"]})\ncmp[\"max_abs_diff\"] = [np.nanmax(np.abs(F[a].values - SHIP_CM[b].values)) for a, b in zip(cmp.feature, cmp.shipped_column)]\ncmp[\"frac_within_1pct\"] = [np.nanmean(np.abs(F[a].values - SHIP_CM[b].values) <= 0.01 * np.abs(SHIP_CM[b].values) + 1e-9)\n                           for a, b in zip(cmp.feature, cmp.shipped_column)]\nprint(\"\\nfor comparison, reading (a) against the code's shipped Cell_metrics.xlsx:\")\nprint(cmp.round(4).to_string(index=False))\nprint(f\"shipped table: R2 > 0.3 for {(SHIP_CM.R2 > 0.3).sum()}, R2 >= 0.3 for {(SHIP_CM.R2 >= 0.3).sum()}; \"\n      f\"agreement on R2 > 0.3 with reading (a): {np.mean((F.r2 > 0.3) == (SHIP_CM.R2 > 0.3)):.3f}\")\nprint(\"paper: 294 (tolerance 264.6 to 323.4)\")\n\"\"\", tags=[\"claim:acg-fit-yield\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Both readings give a count within tolerance (above). The firing rate,\nnormalized mean ACG, Royer burst index and ISI CV of reading (a) equal the code's shipped table,\nso the code used every spike of the unit; the fitted R2 and time constants differ from the\nshipped ones for part of the neurons, as the optimizer differs from MATLAB's.\n\"\"\")\n\nmd(r\"\"\"\n## fig5c-cell-type-clusters\n\n> Spectral clustering on firing rate, mean normalised ACG and ACG rise time constant split the 294\n> neurons into two clusters, 92 putative pyramidal neurons and 202 putative interneurons.\n\"\"\")\n\ncode(r\"\"\"\nTYPES = {}\nfor reading in [\"a\", \"b\"]:\n    F = FEAT[reading]\n    d = F[F.r2 > 0.3].dropna(subset=[\"firing_rate\", \"acg_norm\", \"tau_rise\"])\n    ty, lab = wm.spectral_types(d)\n    types = np.array([None] * len(NT), dtype=object)\n    types[d.index.values] = ty\n    TYPES[reading] = types\n    print(f\"reading ({reading}): {len(d)} neurons; PY {(ty == 'PY').sum()}, IN {(ty == 'IN').sum()}; \"\n          f\"medians PY / IN: firing rate {d.firing_rate[ty == 'PY'].median():.2f} / {d.firing_rate[ty == 'IN'].median():.2f} Hz, \"\n          f\"acg_norm {d.acg_norm[ty == 'PY'].median():.3f} / {d.acg_norm[ty == 'IN'].median():.3f}, \"\n          f\"tau_rise {d.tau_rise[ty == 'PY'].median():.2f} / {d.tau_rise[ty == 'IN'].median():.2f} ms\")\nd = SHIP_CM[SHIP_CM.R2 >= 0.3].dropna(subset=[\"firing_rate\", \"acg_norm\", \"tau_rise\"])\nty, lab = wm.spectral_types(d)\nprint(f\"for comparison, the same clustering on the code's shipped features (R2 >= 0.3, {len(d)} neurons): PY {(ty == 'PY').sum()}, IN {(ty == 'IN').sum()}; \"\n      f\"the code's own rule (cluster label 1 is PY) gives PY {(lab == 1).sum()}\")\nTY = TYPES[\"a\"]\nprint(\"paper: PY 92 (82.8 to 101.2), IN 202 (181.8 to 222.2)\")\n\"\"\", tags=[\"claim:fig5c-cell-type-clusters\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under reading (b) both counts are within tolerance; under reading (a) IN\nis within tolerance and PY just outside (values above). The clustering applied to the code's\nshipped features gives exactly 92 and 202, so the difference comes from the ACG fit. Later\nsections use the types of reading (a), the spikes the code used (see acg-fit-yield).\n\"\"\")\n\nmd(r\"\"\"\n## fig5dfh-cluster-features\n\n> Putative interneurons had higher firing rates, greater normalised mean ACG amplitude and larger\n> tau_rise than putative pyramidal neurons.\n\"\"\")\n\ncode(r\"\"\"\ndef type_tests(F, types, cols):\n    rows = []\n    for c in cols:\n        a, b = F[c][types == \"IN\"].dropna(), F[c][types == \"PY\"].dropna()\n        u = mannwhitneyu(a, b, alternative=\"two-sided\")\n        rows.append({\"feature\": c, \"IN_median\": a.median(), \"PY_median\": b.median(), \"U_IN_vs_PY\": u.statistic, \"p\": u.pvalue})\n    df = pd.DataFrame(rows)\n    from statsmodels.stats.multitest import multipletests\n    df[\"p_BY\"] = multipletests(df.p, method=\"fdr_by\")[1]\n    return df\n\n\nfor reading in [\"a\", \"b\"]:\n    df = type_tests(FEAT[reading], TYPES[reading], [\"firing_rate\", \"acg_norm\", \"tau_rise\", \"burst_royer\", \"cv_isi\"])\n    print(f\"reading ({reading}):\")\n    print(df.to_string(index=False))\nprint(\"paper: U = 17294, 18522, 13465 (IN vs PY), P = 1.42e-32, 2.16e-41, 2.58e-9\")\n\"\"\", tags=[\"claim:fig5dfh-cluster-features\"])\n\nmd(r\"\"\"\n**Result: reproduced.** IN are higher on all three features with corrected p far below 0.05\n(above); as the claims file notes, this follows from the clustering by construction.\n\"\"\")\n\nmd(r\"\"\"\n## fig5gh-burst-index-cv2\n\n> Putative pyramidal neurons had a higher burst index (0.985 against 0.622) and greater\n> spike-train irregularity (CV2 1.673 against 1.319) than putative interneurons.\n\"\"\")\n\ncode(r\"\"\"\nfor reading in [\"a\", \"b\"]:\n    F, ty = FEAT[reading], TYPES[reading]\n    df = type_tests(F, ty, [\"firing_rate\", \"acg_norm\", \"tau_rise\", \"burst_royer\", \"cv_isi\"])\n    dh = type_tests(F, ty, [\"firing_rate\", \"acg_norm\", \"tau_rise\", \"burst_royer\", \"cv2_holt\"])\n    print(f\"reading ({reading}):\")\n    for c, tab in [(\"burst_royer\", df), (\"cv_isi\", df), (\"cv2_holt\", dh)]:\n        r = tab[tab.feature == c].iloc[0]\n        a, b = F[c][ty == \"PY\"], F[c][ty == \"IN\"]\n        print(f\"  {c}: PY mean {a.mean():.3f} median {a.median():.3f}; IN mean {b.mean():.3f} median {b.median():.3f}; \"\n              f\"U(IN vs PY) = {r.U_IN_vs_PY:.0f}, BY-corrected p = {r.p_BY:.2e}\")\nprint(\"paper: burst index PY 0.985 vs IN 0.622, CV2 PY 1.673 vs IN 1.319; tolerance 10% of each\")\n\"\"\", tags=[\"claim:fig5gh-burst-index-cv2\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## supp4-rodent-validation (data elsewhere)\n\n> Applied to a labelled rodent dataset of 44 pyramidal neurons and 299 PV and SST interneurons, the\n> spectral-clustering classifier assigned 333 of 343 neurons correctly (97%).\n\nTested on the features of the CellExplorer ground-truth cells that the paper's code ships\n(`validation_data.xlsx`), clustered as in fig5c, each cluster labelled by its majority type.\n\"\"\")\n\ncode(r\"\"\"\nv = VALID.copy()\nprint(\"cell types in the table:\", v.cell_type.value_counts().to_dict(), \"; rows:\", len(v))\nvv = v.rename(columns={\"norm_acg\": \"acg_norm\"}).dropna(subset=[\"firing_rate\", \"acg_norm\", \"tau_rise\", \"tau_decay\", \"cell_type\"])\n_, lab = wm.spectral_types(vv)\nvv[\"cluster\"] = lab\nmaj = vv.groupby(\"cluster\").cell_type.agg(lambda s: s.mode().iat[0])\nvv[\"match\"] = vv.cell_type == vv.cluster.map(maj)\nprint(pd.crosstab(vv.cluster, vv.cell_type).to_string())\nprint(f\"matched {vv.match.sum()} of {len(vv)}; misassigned by type: {vv[~vv.match].cell_type.value_counts().to_dict()}\")\nprint(\"paper: 333 of 343, one pyramidal and nine interneurons misassigned\")\n\"\"\", tags=[\"claim:supp4-rodent-validation\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part5.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part6.py",
 "content": "md(r\"\"\"\n## fig4c-encoding-bursts-vs-poisson\n\n> During encoding, population bursting did not exceed a rate-matched Poisson null for most neuronal\n> groups; it differed from the null only for all neurons and for the low mean ACG amplitude group.\n\nWithin each participant and group, load 1 trials, the first encoding second; pooled spikes of the\ngroup, trials concatenated, 70 ms bins, Gaussian smoothing (sigma 40 ms), peaks at least 2 bins\napart; 100 rate-matched Poisson surrogates; paired two-sided Wilcoxon signed-rank over\nparticipants (the code's `zero_method='pratt'`, asymptotic) and BH over the code's eight groups.\nReadings: peak rule (prominence, the code and Results; or height above the 90th percentile, the\nMethods), surrogate threshold (the real train's, the code; or each surrogate's own), group rule\n(the code's 6 lowest and highest; or the Methods' median split), all neurons (902 in participants\nwith at least 10, or the well-fit neurons), and a 1-bin spacing variant.\n\"\"\")\n\ncode(r\"\"\"\nEP = {}\nfor n in range(len(NT)):\n    t_all = T[NT[\"sub\"].iat[n]]\n    for L in [1, 2, 3]:\n        t = t_all[t_all.load == L]\n        enc_on = {1: t.enc1, 2: t.timestamps_Encoding2, 3: t.timestamps_Encoding3}[L].values\n        EP[(n, L, \"enc\")] = wm.epoch_spikes(SPK[n], enc_on, enc_on + 1.0, 1.0)\n        EP[(n, L, \"maint28\")] = wm.epoch_spikes(SPK[n], t.maint.values, t.probe.values, 2.8)\n        EP[(n, L, \"maint3\")] = wm.epoch_spikes(SPK[n], t.maint.values, t.probe.values, 3.0)\n        EP[(n, L, \"probe\")] = wm.epoch_spikes(SPK[n], t.probe.values, t.probe.values + 1.0, 1.0)\nGR = {g: wm.burst_groups(NT, FEAT[\"a\"], CONCEPT, TY, g) for g in [\"code\", \"methods\"]}\nfor g, G in GR.items():\n    print(f\"group rule {g}:\", {k: f\"{len(v)} participants, {sum(len(x) for x in v.values())} neurons\" for k, v in G.items()})\n\nFAM = [\"All902\", \"LowACG\", \"HighACG\", \"ShortDecay\", \"LongDecay\", \"Concept\", \"PY\", \"IN\"]\nCONFIGS = [(\"prominence\", 2, \"real\"), (\"height\", 2, \"real\"), (\"prominence\", 2, \"own\"), (\"height\", 2, \"own\"),\n           (\"prominence\", 1, \"real\"), (\"height\", 1, \"real\")]\nrows = []\nfor grule, G in GR.items():\n    for rule, dist, thr in CONFIGS:\n        for epoch, key, win in [(\"enc\", \"enc\", 1.0), (\"maint\", \"maint28\", 2.8)]:\n            for g, subs in G.items():\n                for sub, nids in subs.items():\n                    rng = np.random.default_rng(wm.stable_seed(g, sub, epoch, rule, dist, thr, grule))\n                    rc, scount, _, _ = wm.group_bursts([EP[(n, 1, key)] for n in nids], win, rng, rule, dist, thr)\n                    rows.append(dict(grule=grule, rule=rule, dist=dist, thr=thr, epoch=epoch, group=g, sub=sub, real=rc, sur=scount))\nBR = pd.DataFrame(rows)\n\n\ndef real_vs_null(df, groups=FAM, extra=(\"AllFit\",)):\n    out = []\n    for g in list(groups) + list(extra):\n        x = df[df.group == g]\n        if len(x) < 2:\n            continue\n        w = wilcoxon(x.real, x.sur, zero_method=\"pratt\", method=\"asymptotic\")\n        out.append({\"group\": g, \"n\": len(x), \"real_median\": x.real.median(), \"null_median\": round(x.sur.median(), 1),\n                    \"real_above\": int((x.real > x.sur).sum()), \"W\": w.statistic, \"p\": w.pvalue})\n    o = pd.DataFrame(out)\n    m = o.group.isin(groups)\n    o.loc[m, \"p_BH\"] = wm.bh(o.p[m])\n    o.loc[~m, \"p_BH\"] = np.nan\n    return o\n\n\ndef show_bursts(epoch):\n    summ = []\n    for (grule, rule, dist, thr), df in BR[BR.epoch == epoch].groupby([\"grule\", \"rule\", \"dist\", \"thr\"]):\n        o = real_vs_null(df)\n        o.insert(0, \"reading\", f\"{grule}/{rule}/d{dist}/{thr}\")\n        summ.append(o)\n    return pd.concat(summ)\n\n\nBURST_ENC = show_bursts(\"enc\")\nprint(BURST_ENC.round(4).to_string(index=False))\n\"\"\", tags=[\"claim:fig4c-encoding-bursts-vs-poisson\"])\n\ncode(r\"\"\"\ndef fig4c_rule(o, all_name=\"All902\"):\n    sig = dict(zip(o.group, o.p_BH < 0.05))\n    if all_name == \"AllFit\":\n        sig[\"All902\"] = bool(o[o.group == \"AllFit\"].p.iloc[0] < 0.05)\n    named = sig[\"All902\"] and sig[\"LowACG\"]\n    others = [g for g in [\"HighACG\", \"ShortDecay\", \"LongDecay\", \"Concept\"] if sig[g]]\n    return named, others\n\n\nfor reading, o in BURST_ENC.groupby(\"reading\", sort=False):\n    for alln in [\"All902\", \"AllFit\"]:\n        named, others = fig4c_rule(o, alln)\n        print(f\"{reading}, all neurons as {alln}: all and low ACG differ {named}; other groups that differ {others}\")\n\"\"\", tags=[\"claim:fig4c-encoding-bursts-vs-poisson\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under the main reading (the code's groups, prominence rule, spacing of 2\nbins, the real threshold) all neurons and the low ACG group differ from the Poisson null after\ncorrection and the high ACG, short and long tau decay and concept groups do not (above). Other\nreadings differ: with the Methods' height rule or with each surrogate's own threshold, the\npattern does not hold.\n\"\"\")\n\nmd(r\"\"\"\n## fig4d-maintenance-bursts-vs-poisson\n\n> During maintenance, bursting exceeded the Poisson null for all neurons pooled and for the low and\n> high mean ACG and short and long tau decay groups, but not for concept cells.\n\nMaintenance windows of 2.8 s from onset (the code's), each trial cut at the probe.\n\"\"\")\n\ncode(r\"\"\"\nBURST_M = show_bursts(\"maint\")\nprint(BURST_M.round(4).to_string(index=False))\nfor reading, o in BURST_M.groupby(\"reading\", sort=False):\n    ok = {g: bool((o[o.group == g].p_BH < 0.05).iloc[0] and (o[o.group == g].real_above > o[o.group == g].n / 2).iloc[0])\n          for g in [\"All902\", \"LowACG\", \"HighACG\", \"ShortDecay\", \"LongDecay\"]}\n    print(f\"{reading}: five named groups above the null {all(ok.values())} {ok}; concept cells corrected p \"\n          f\"{o[o.group == 'Concept'].p_BH.iloc[0]:.3f}\")\n\"\"\", tags=[\"claim:fig4d-maintenance-bursts-vs-poisson\"])\n\ncode(r\"\"\"\n# Variant: each trial's own maintenance length concatenated (stride = its duration), main reading.\nrows = []\nfor sub_g, subs in GR[\"code\"].items():\n    for sub, nids in subs.items():\n        t = T[sub][T[sub].load == 1]\n        durs = t.maint_dur.values\n        trains = [wm.epoch_spikes(SPK[n], t.maint.values, t.probe.values, 10.0) for n in nids]\n        offs = np.r_[0, np.cumsum(durs)[:-1]]\n        pooled = np.concatenate([np.concatenate([s + o for s, o in zip(tr_, offs)]) for tr_ in trains])\n        sm = wm.smooth_counts(pooled, durs.sum())\n        thr = np.percentile(sm, wm.BURST_PCT)\n        rc = len(wm.burst_peaks(sm, thr, \"prominence\", 2))\n        rng = np.random.default_rng(wm.stable_seed(\"own\", sub_g, sub))\n        counts = np.array([[len(s) for s in tr_] for tr_ in trains])\n        sur = []\n        for _ in range(100):\n            nn = rng.poisson(counts)\n            st_ = np.concatenate([rng.uniform(0, durs[j], nn[i, j]) + offs[j] for i in range(nn.shape[0]) for j in range(nn.shape[1])])\n            s2 = wm.smooth_counts(st_, durs.sum())\n            sur.append(len(wm.burst_peaks(s2, thr, \"prominence\", 2)))\n        rows.append(dict(group=sub_g, sub=sub, real=rc, sur=np.mean(sur)))\nprint(\"each trial's own maintenance, code groups, prominence, real threshold:\")\nprint(real_vs_null(pd.DataFrame(rows)).round(4).to_string(index=False))\n\"\"\", tags=[\"claim:fig4d-maintenance-bursts-vs-poisson\"])\n\nmd(r\"\"\"\n**Result: reproduced.** Under the main reading the five named groups have more real than\nsurrogate bursts in most participants with corrected p < 0.05, and concept cells do not differ\n(above); the variant with each trial's own maintenance length gives the same.\n\"\"\")\n\nmd(r\"\"\"\n## fig4-acg-group-differences\n\n> The low mean ACG group burst more than the high mean ACG group in both encoding and maintenance,\n> whereas the short tau decay group exceeded the long tau decay group only during encoding.\n\nReal burst counts of the two previous sections compared between groups within participant\n(paired two-sided Wilcoxon), BH over the code's 28 pairs of 8 groups, and over the four tests\nnamed here.\n\"\"\")\n\ncode(r\"\"\"\nfor (grule, rule, dist, thr), df in BR.groupby([\"grule\", \"rule\", \"dist\", \"thr\"]):\n    if dist != 2 or thr != \"real\":\n        continue\n    res = {}\n    for epoch in [\"enc\", \"maint\"]:\n        x = df[df.epoch == epoch].pivot(index=\"sub\", columns=\"group\", values=\"real\")\n        pairs = list(itertools.combinations(FAM, 2))\n        ps = {}\n        for a, b in pairs:\n            xx = x[[a, b]].dropna()\n            try:\n                ps[(a, b)] = wilcoxon(xx[b], xx[a], zero_method=\"wilcox\").pvalue if len(xx) >= 2 else np.nan\n            except ValueError:\n                ps[(a, b)] = 1.0\n        q28 = dict(zip(ps, wm.bh(np.nan_to_num(list(ps.values()), nan=1.0))))\n        res[epoch] = (x, ps, q28)\n    four = [(\"enc\", \"LowACG\", \"HighACG\"), (\"maint\", \"LowACG\", \"HighACG\"), (\"enc\", \"ShortDecay\", \"LongDecay\"), (\"maint\", \"ShortDecay\", \"LongDecay\")]\n    p4 = [res[e][1][(a, b)] for e, a, b in four]\n    q4 = wm.bh(p4)\n    print(f\"reading {grule}/{rule}:\")\n    for (e, a, b), p, q in zip(four, p4, q4):\n        x = res[e][0][[a, b]].dropna()\n        print(f\"  {e}: {a} median {x[a].median():.1f} vs {b} {x[b].median():.1f}, {a} higher in {(x[a] > x[b]).sum()} of {len(x)}; \"\n              f\"p = {p:.4f}, BH over 28 pairs {res[e][2][(a, b)]:.4f}, over these four {q:.4f}\")\n\"\"\", tags=[\"claim:fig4-acg-group-differences\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## fig4f-all-cells-epochs\n\n> At the population level, load 1 burst rates increased from encoding to each of the three 1 s\n> maintenance windows and to the probe.\n\nBurst detection of fig4c per epoch (encoding and probe 1 s, maintenance up to 3 s); M1 to M3 are\n(a) the Methods' 1 s windows from maintenance onset (peaks counted by their time in the trial; M3\nruns from 2 s to the end of maintenance, 0.5 to 0.8 s) or (b) the code's thirds of the whole\nconcatenated train. Paired two-sided Wilcoxon, BH over the 10 pairs of periods, per group and load.\n\"\"\")\n\ncode(r\"\"\"\nPER = [\"enc\", \"M1\", \"M2\", \"M3\", \"probe\"]\nrows = []\nfor grule, G in GR.items():\n    for rule in [\"prominence\", \"height\"]:\n        for mr in [\"methods\", \"code\"]:\n            for L in [1, 2, 3]:\n                for g, subs in G.items():\n                    for sub, nids in subs.items():\n                        c = wm.epoch_burst_counts({\"enc\": [EP[(n, L, \"enc\")] for n in nids],\n                                                   \"maint\": [EP[(n, L, \"maint3\")] for n in nids],\n                                                   \"probe\": [EP[(n, L, \"probe\")] for n in nids]}, rule, 2, mr)\n                        rows.append(dict(grule=grule, rule=rule, mread=mr, load=L, group=g, sub=sub, **c))\nEPB = pd.DataFrame(rows)\n\n\ndef epoch_tests(x):\n    ps, names = [], []\n    for a, b in itertools.combinations(PER, 2):\n        try:\n            p = wilcoxon(x[a], x[b], zero_method=\"wilcox\").pvalue\n        except ValueError:\n            p = 1.0\n        ps.append(p)\n        names.append(f\"{a}-{b}\")\n    q = wm.bh(ps)\n    return dict(zip(names, q)), dict(zip(names, ps))\n\n\ndef epoch_table(group, load):\n    out = []\n    for (grule, rule, mr), x in EPB[(EPB.group == group) & (EPB.load == load)].groupby([\"grule\", \"rule\", \"mread\"]):\n        q, _ = epoch_tests(x)\n        med = x[PER].median()\n        out.append({\"reading\": f\"{grule}/{rule}/M-{mr}\", \"n\": len(x), **{f\"med_{k}\": med[k] for k in PER},\n                    **{f\"q_{k}\": round(q[f\"enc-{k}\"], 4) for k in PER[1:]},\n                    \"min_q_other\": round(min(v for k, v in q.items() if not k.startswith(\"enc-\")), 4),\n                    \"q_M1-M2\": round(q[\"M1-M2\"], 4), \"q_M1-M3\": round(q[\"M1-M3\"], 4)})\n    return pd.DataFrame(out)\n\n\nfor g in [\"All902\", \"AllFit\"]:\n    print(f\"\\n{g}, load 1 (medians are bursts per window; q is BH over the 10 pairs):\")\n    print(epoch_table(g, 1).to_string(index=False))\nx = EPB[(EPB.group == \"All902\") & (EPB.load == 1) & (EPB.mread == \"methods\")]\ndur = np.mean([T[s][T[s].load == 1].maint_dur.mean() for s in x[\"sub\"].unique()]) - 2.0\nprint(f\"\\nM3 under reading (a) lasts {dur:.2f} s on average; its median rate per second, all neurons, prominence: \"\n      f\"{(x[(x.grule == 'code') & (x.rule == 'prominence')].M3 / dur).median():.1f} against M1 {x[(x.grule == 'code') & (x.rule == 'prominence')].M1.median():.1f}\")\n\"\"\", tags=[\"claim:fig4f-all-cells-epochs\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** Under the prominence rule, all neurons burst more in each of\nM1, M2 and M3 than in encoding with corrected p < 0.05 under both window readings and both\npopulations, but the probe does not differ from encoding under any reading (above). Three of the\nfour comparisons hold.\n\"\"\")\n\nmd(r\"\"\"\n## fig4hj-group-epochs\n\n> The increase of bursting from encoding into maintenance was driven by neurons with high mean ACG\n> amplitude (also increasing to the probe) and neurons with a long tau decay, while the low ACG,\n> short tau decay and concept-cell groups showed no change across epochs.\n\"\"\")\n\ncode(r\"\"\"\nfor g in [\"HighACG\", \"LongDecay\", \"LowACG\", \"ShortDecay\", \"Concept\"]:\n    print(f\"\\n{g}, load 1:\")\n    print(epoch_table(g, 1).to_string(index=False))\n\"\"\", tags=[\"claim:fig4hj-group-epochs\"])\n\ncode(r\"\"\"\nfor (grule, rule, mr), _ in EPB.groupby([\"grule\", \"rule\", \"mread\"]):\n    q = {g: epoch_tests(EPB[(EPB.group == g) & (EPB.load == 1) & (EPB.grule == grule) & (EPB.rule == rule) & (EPB.mread == mr)])[0]\n         for g in [\"HighACG\", \"LongDecay\", \"LowACG\", \"ShortDecay\", \"Concept\"]}\n    med = {g: EPB[(EPB.group == g) & (EPB.load == 1) & (EPB.grule == grule) & (EPB.rule == rule) & (EPB.mread == mr)][PER].median()\n           for g in [\"HighACG\", \"LongDecay\"]}\n    hi = {k: bool(q[\"HighACG\"][f\"enc-{k}\"] < 0.05 and med[\"HighACG\"][k] > med[\"HighACG\"][\"enc\"]) for k in [\"M1\", \"M2\", \"probe\"]}\n    lo = {k: bool(q[\"LongDecay\"][f\"enc-{k}\"] < 0.05 and med[\"LongDecay\"][k] > med[\"LongDecay\"][\"enc\"]) for k in [\"M1\", \"M2\", \"M3\"]}\n    none = {g: int(sum(v < 0.05 for v in q[g].values())) for g in [\"LowACG\", \"ShortDecay\", \"Concept\"]}\n    print(f\"{grule}/{rule}/M-{mr}: high ACG up at {hi}; long tau decay up at {lo}; significant pairs in low ACG, short tau decay, concept {none}\")\n\"\"\", tags=[\"claim:fig4hj-group-epochs\"])\n\nmd(r\"\"\"\n**Result: partially reproduced.** Under the main reading (the code's groups, prominence, the\ncode's thirds) long tau decay neurons increase from encoding to M1, M2 and M3 and the low ACG,\nshort tau decay and concept groups show no significant pair, but high ACG neurons increase at M1\nand M2 and not at the probe (above).\n\"\"\")\n\nmd(r\"\"\"\n## ext2-bursts-loads23\n\n> The patterns of burst rates across epochs held for loads 2 and 3.\n\n\"Similar\" read as all cells and the high ACG and long tau decay groups showing more bursts in\neach maintenance window than in encoding, in the median over participants, at each load\n(encoding from the last encoding image).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (grule, rule, mr), x0 in EPB.groupby([\"grule\", \"rule\", \"mread\"]):\n    for L in [1, 2, 3]:\n        ok = {}\n        for g in [\"All902\", \"HighACG\", \"LongDecay\"]:\n            x = x0[(x0.group == g) & (x0.load == L)]\n            med = x[PER].median()\n            ok[g] = bool(all(med[k] > med[\"enc\"] for k in [\"M1\", \"M2\", \"M3\"]))\n            q, _ = epoch_tests(x)\n            ok[g + \"_q\"] = \"/\".join(f\"{q[f'enc-{k}']:.3f}\" for k in [\"M1\", \"M2\", \"M3\", \"probe\"])\n        rows.append({\"reading\": f\"{grule}/{rule}/M-{mr}\", \"load\": L, **ok})\ne2 = pd.DataFrame(rows)\nprint(e2.to_string(index=False))\n\"\"\", tags=[\"claim:ext2-bursts-loads23\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part6.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
s=open('nb_part6.py').read()
old='''            nn = rng.poisson(counts)
            st_ = np.concatenate([rng.uniform(0, durs[j], nn[i, j]) + offs[j] for i in range(nn.shape[0]) for j in range(nn.shape[1])])'''
new='''            nn = rng.poisson(counts)
            ti = np.repeat(np.tile(np.arange(len(durs)), nn.shape[0]), nn.ravel())
            st_ = rng.uniform(0, 1, len(ti)) * durs[ti] + offs[ti]'''
assert old in s; s=s.replace(old,new); open('nb_part6.py','w').write(s)
s=open('nb_part3.py').read()
old='''        enc_on = {1: t.enc1, 2: t.timestamps_Encoding2, 3: t.timestamps_Encoding3}[1].values
        for ep, on, dur in [("enc", enc_on, 1.0),'''
new='''        for ep, on, dur in [("enc", t.enc1.values, 1.0),'''
assert old in s; s=s.replace(old,new); open('nb_part3.py','w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_part7.py",
 "content": "md(r\"\"\"\n## fig5kl-concept-cell-types\n\n> Of the classified concept cells, 11 were putative pyramidal and 14 putative interneurons;\n> pyramidal concept cells showed pronounced bursting, interneuron concept cells smoother regular\n> spiking.\n\"\"\")\n\ncode(r\"\"\"\nfor reading in [\"a\", \"b\"]:\n    ty = TYPES[reading]\n    F = FEAT[reading]\n    py, inn = CONCEPT & (ty == \"PY\"), CONCEPT & (ty == \"IN\")\n    print(f\"reading ({reading}): concept cells PY {py.sum()}, IN {inn.sum()}, unclassified {CONCEPT.sum() - py.sum() - inn.sum()}; \"\n          f\"Royer burst index median PY {F.burst_royer[py].median():.3f}, IN {F.burst_royer[inn].median():.3f}; \"\n          f\"ISI CV median PY {F.cv_isi[py].median():.3f}, IN {F.cv_isi[inn].median():.3f}; \"\n          f\"Holt CV2 median PY {F.cv2_holt[py].median():.3f}, IN {F.cv2_holt[inn].median():.3f}\")\nprint(\"paper: PY 11 (9.9 to 12.1), IN 14 (12.6 to 15.4)\")\n\"\"\", tags=[\"claim:fig5kl-concept-cell-types\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## fig6ab-celltype-bursts-vs-null\n\n> Pyramidal populations showed elevated bursting over a null in both encoding and maintenance,\n> whereas interneurons showed elevated bursting during maintenance but not during encoding.\n\nNull readings: (a) the Poisson surrogates of fig4c (the PY and IN rows of its tables, BH over\nthe code's eight groups); (b) shuffling the cell-type labels among each participant's classified\nneurons, group sizes kept (100 shuffles), BH over the two groups.\n\"\"\")\n\ncode(r\"\"\"\nfor epoch, tab in [(\"enc\", BURST_ENC), (\"maint\", BURST_M)]:\n    x = tab[tab.group.isin([\"PY\", \"IN\"])]\n    print(f\"(a) Poisson null, {epoch}:\")\n    print(x[[\"reading\", \"group\", \"n\", \"real_median\", \"null_median\", \"real_above\", \"W\", \"p\", \"p_BH\"]].round(4).to_string(index=False))\nrows = []\nfor epoch, key, win in [(\"enc\", \"enc\", 1.0), (\"maint\", \"maint28\", 2.8)]:\n    subs = sorted(set(GR[\"code\"][\"PY\"]) | set(GR[\"code\"][\"IN\"]))\n    for sub in subs:\n        nids = NT.nid[NT[\"sub\"] == sub].values\n        pyn = [n for n in nids if TY[n] == \"PY\"]\n        inn = [n for n in nids if TY[n] == \"IN\"]\n        if len(pyn) == 0 or len(inn) == 0:\n            continue\n        rng = np.random.default_rng(wm.stable_seed(\"typeshuffle\", epoch, sub))\n        npy, nin = wm.type_shuffle_null([EP[(n, 1, key)] for n in pyn], [EP[(n, 1, key)] for n in inn], win, rng)\n        for g, nl, members in [(\"PY\", npy, pyn), (\"IN\", nin, inn)]:\n            if len(members) >= 3:\n                rc, _, _, _ = wm.group_bursts([EP[(n, 1, key)] for n in members], win, rng, \"prominence\", 2, \"real\", n_sur=0)\n                rows.append({\"epoch\": epoch, \"group\": g, \"sub\": sub, \"real\": rc, \"sur\": nl})\nSH = pd.DataFrame(rows)\nfor epoch in [\"enc\", \"maint\"]:\n    o = real_vs_null(SH[SH.epoch == epoch], groups=[\"PY\", \"IN\"], extra=())\n    print(f\"(b) label-shuffled null, {epoch}:\")\n    print(o.round(4).to_string(index=False))\n\"\"\", tags=[\"claim:fig6ab-celltype-bursts-vs-null\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## fig6cd-celltype-epochs\n\n> Pyramidal burst rates stayed stable across task epochs at every load, whereas interneuron burst\n> rates changed from encoding to each maintenance window and to the probe in load 1 trials.\n\"\"\")\n\ncode(r\"\"\"\nfor g in [\"PY\", \"IN\"]:\n    for L in [1, 2, 3]:\n        print(f\"\\n{g}, load {L}:\")\n        print(epoch_table(g, L).to_string(index=False))\n\"\"\", tags=[\"claim:fig6cd-celltype-epochs\"])\n\ncode(r\"\"\"\nfor (grule, rule, mr), x0 in EPB.groupby([\"grule\", \"rule\", \"mread\"]):\n    if grule != \"code\":\n        continue\n    qin = epoch_tests(x0[(x0.group == \"IN\") & (x0.load == 1)])[0]\n    py_sig = {L: int(sum(v < 0.05 for v in epoch_tests(x0[(x0.group == \"PY\") & (x0.load == L)])[0].values())) for L in [1, 2, 3]}\n    print(f\"{rule}/M-{mr}: IN encoding vs M1, M2, M3, probe corrected p \"\n          f\"{[round(qin[f'enc-{k}'], 4) for k in ['M1', 'M2', 'M3', 'probe']]}; PY pairs with corrected p < 0.05 by load {py_sig}\")\n\"\"\", tags=[\"claim:fig6cd-celltype-epochs\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## ext5bd-in-load-dependence\n\n> Interneuron burst-rate differences across maintenance epochs increased with load.\n\nRead as the median over participants of the absolute difference in bursts between encoding and\neach of M1 to M3, averaged over the three windows.\n\"\"\")\n\ncode(r\"\"\"\nfor (grule, rule, mr), x0 in EPB.groupby([\"grule\", \"rule\", \"mread\"]):\n    vals = []\n    for L in [1, 2, 3]:\n        x = x0[(x0.group == \"IN\") & (x0.load == L)]\n        vals.append(np.median(np.mean([np.abs(x[k] - x[\"enc\"]) for k in [\"M1\", \"M2\", \"M3\"]], 0)))\n    print(f\"{grule}/{rule}/M-{mr}: IN measure by load {np.round(vals, 2).tolist()}; rises from load 1 to 3: {vals[2] > vals[0]}\")\n\"\"\", tags=[\"claim:ext5bd-in-load-dependence\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## fig6e-load-modulation-in\n\n> A significant portion of interneurons was modulated by memory load during maintenance (14.36%),\n> including interneuron concept cells (21.42%), while pyramidal neurons showed minimal load\n> modulation (5.43%; concept pyramidal 0.00%).\n\nThe GLM fits of fig1e (load, every trial reading), with the groups PY, IN, PY concept cells and IN\nconcept cells (types of reading (a) of fig5c).\n\"\"\")\n\ncode(r\"\"\"\nTG = {\"IN\": np.where(TY == \"IN\")[0], \"IN concept\": np.where((TY == \"IN\") & CONCEPT)[0],\n      \"PY\": np.where(TY == \"PY\")[0], \"PY concept\": np.where((TY == \"PY\") & CONCEPT)[0]}\nfor key in [(\"load\", \"matched\", \"shared\"), (\"load\", \"matched\", \"within\"), (\"load\", \"all\", \"within\")]:\n    (real, null), _, _ = GLM[key]\n    df, _ = wm.glm_groups(real, null, TG)\n    print(f\"load, trials {key[1]}, permutation {key[2]}:\")\n    print(df.round(3).to_string(index=False))\nTGb = {\"IN\": np.where(TYPES[\"b\"] == \"IN\")[0], \"IN concept\": np.where((TYPES[\"b\"] == \"IN\") & CONCEPT)[0],\n       \"PY\": np.where(TYPES[\"b\"] == \"PY\")[0], \"PY concept\": np.where((TYPES[\"b\"] == \"PY\") & CONCEPT)[0]}\n(real, null), _, _ = GLM[(\"load\", \"matched\", \"shared\")]\nprint(\"variant, types of reading (b), matched trials, shared permutation:\")\nprint(wm.glm_groups(real, null, TGb)[0].round(3).to_string(index=False))\nprint(\"paper: IN 14.36% (P = 0.002), IN concept 21.42% (P = 0.032), PY 5.43% and PY concept 0.00% (P > 0.05)\")\n\"\"\", tags=[\"claim:fig6e-load-modulation-in\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## fig6f-rt-modulation-in-concept\n\n> Interneuron concept cells were modulated by reaction time during maintenance (35.71%), but not\n> all interneurons, and pyramidal neurons showed no significant RT modulation in either the full\n> population or the concept subset.\n\"\"\")\n\ncode(r\"\"\"\nfor key in [(\"rt\", \"matched\", \"shared\"), (\"rt\", \"matched\", \"within\"), (\"rt\", \"all\", \"within\"),\n            (\"rt_code\", \"matched\", \"shared\"), (\"rt_code\", \"matched\", \"within\")]:\n    (real, null), _, _ = GLM[key]\n    df, _ = wm.glm_groups(real, null, TG)\n    label = \"own RT\" if key[0] == \"rt\" else \"variant, subject 1's RT vector\"\n    print(f\"{label}, trials {key[1]}, permutation {key[2]}:\")\n    print(df.round(3).to_string(index=False))\nprint(\"paper: IN concept 35.71% (P = 0.002); IN, PY, PY concept P > 0.05\")\n\"\"\", tags=[\"claim:fig6f-rt-modulation-in-concept\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## fig6gh-in-concept-cv2\n\n> Interneuron concept cells had higher CV2 during maintenance than encoding on preferred load 1\n> trials but not on nonpreferred trials, while pyramidal concept cells showed stable CV2.\n\nHolt's CV2 of the interspike intervals of each cell's spikes concatenated over preferred (or\nnonpreferred) trials, in encoding (first image, 1 s) and maintenance (2.5 s); trials of load 1\n(Results) or of all loads (the code). Readings for PY: (a) encoding against maintenance within\neach trial type; (b) preferred against nonpreferred within each epoch.\n\"\"\")\n\ncode(r\"\"\"\ndef cv2_cell(n, loads, pref_flag, epoch):\n    t = T[NT[\"sub\"].iat[n]]\n    t = t[t.load.isin(loads)]\n    pm = pref_mask(t, PREF[n], 1) if loads == [1] else ((t.img1 == PREF[n]) | ((t.load >= 2) & (t.img2 == PREF[n])) | ((t.load == 3) & (t.img3 == PREF[n]))).values\n    t = t[pm if pref_flag else ~pm]\n    on, win = (t.enc1.values, 1.0) if epoch == \"enc\" else (t.maint.values, 2.5)\n    sp = wm.epoch_spikes(SPK[n], on, on + win, win)\n    return wm.cv2_holt(np.diff(wm.concat_trials(sp, win)))\n\n\nfor loads, lname in [([1], \"load 1\"), ([1, 2, 3], \"all loads\")]:\n    for ty_ in [\"IN\", \"PY\"]:\n        cells = np.where(CONCEPT & (TY == ty_))[0]\n        vals = {(pf, ep): np.array([cv2_cell(n, loads, pf, ep) for n in cells]) for pf in [True, False] for ep in [\"enc\", \"maint\"]}\n        for pf in [True, False]:\n            a, b = vals[(pf, \"enc\")], vals[(pf, \"maint\")]\n            ok = np.isfinite(a) & np.isfinite(b)\n            w = wilcoxon(b[ok], a[ok])\n            print(f\"{lname}, {ty_} concept, {'preferred' if pf else 'nonpreferred'}: n {ok.sum()}, CV2 median encoding {np.median(a[ok]):.3f}, \"\n                  f\"maintenance {np.median(b[ok]):.3f}, maintenance higher in {(b[ok] > a[ok]).sum()}; W = {w.statistic:.1f}, p = {w.pvalue:.4f}\")\n        if ty_ == \"PY\":\n            for ep in [\"enc\", \"maint\"]:\n                a, b = vals[(True, ep)], vals[(False, ep)]\n                ok = np.isfinite(a) & np.isfinite(b)\n                w = wilcoxon(a[ok], b[ok])\n                print(f\"   reading (b), PY {ep}: preferred vs nonpreferred W = {w.statistic:.1f}, p = {w.pvalue:.4f}\")\nprint(\"paper: IN preferred W = 13.0, P = 0.032; IN nonpreferred W = 50.0, P > 0.05; PY all P > 0.05\")\n\"\"\", tags=[\"claim:fig6gh-in-concept-cv2\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## ext5gh-py-decay-preferred\n\n> Pyramidal concept cells showed increased decay time constants on preferred trials during encoding\n> and maintenance, an effect absent in interneurons.\n\ntau_decay of the CellExplorer fit (acg-fit-yield) to the narrow ACG of each concept cell's spikes\nin the epoch of preferred (or nonpreferred) trials, concatenated; preferred against nonpreferred\nby a two-sided Wilcoxon signed-rank test over cells (a paired t-test as a variant); load 1 or all\nloads. The claims file takes this reading of \"decay time constants\" and the outcome rests on it.\n\"\"\")\n\ncode(r\"\"\"\ndef decay_cell(n, loads, pref_flag, epoch):\n    t = T[NT[\"sub\"].iat[n]]\n    t = t[t.load.isin(loads)]\n    pm = ((t.img1 == PREF[n]) | ((t.load >= 2) & (t.img2 == PREF[n])) | ((t.load == 3) & (t.img3 == PREF[n]))).values\n    if loads == [1]:\n        pm = (t.img1 == PREF[n]).values\n    t = t[pm if pref_flag else ~pm]\n    on, win = (t.enc1.values, 1.0) if epoch == \"enc\" else (t.maint.values, 2.5)\n    s = wm.concat_trials(wm.epoch_spikes(SPK[n], on, on + win, win), win)\n    if len(s) < 3:\n        return np.nan, len(s)\n    f = wm.fit_acg(wm.acg(np.sort(s), 0.0005, 201))\n    return f[\"tau_decay\"], len(s)\n\n\nfor loads, lname in [([1], \"load 1\"), ([1, 2, 3], \"all loads\")]:\n    for ty_ in [\"PY\", \"IN\"]:\n        cells = np.where(CONCEPT & (TY == ty_))[0]\n        for ep in [\"enc\", \"maint\"]:\n            a = np.array([decay_cell(n, loads, True, ep) for n in cells])\n            b = np.array([decay_cell(n, loads, False, ep) for n in cells])\n            ok = np.isfinite(a[:, 0]) & np.isfinite(b[:, 0])\n            w = wilcoxon(a[ok, 0], b[ok, 0])\n            tt = stats.ttest_rel(a[ok, 0], b[ok, 0])\n            print(f\"{lname}, {ty_} concept, {ep}: n {ok.sum()} (spikes per cell, preferred median {np.median(a[:, 1]):.0f}); \"\n                  f\"tau_decay median preferred {np.median(a[ok, 0]):.2f} ms, nonpreferred {np.median(b[ok, 0]):.2f}; \"\n                  f\"preferred larger in {(a[ok, 0] > b[ok, 0]).sum()}; Wilcoxon W = {w.statistic:.1f}, p = {w.pvalue:.4f}; paired t p = {tt.pvalue:.4f}\")\nprint(\"paper: PY preferred larger in encoding and maintenance, Pmax = 0.029; IN all P > 0.05\")\n\"\"\", tags=[\"claim:ext5gh-py-decay-preferred\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## fig6i-py-bin-width-decoding\n\n> Pyramidal concept cells did not decode the image above chance during load 1 maintenance with 250\n> and 500 ms bins (26.67%, 23.33%) but did with 750 and 1000 ms bins (40.00%, 43.33%).\n\nThe analysis of fig2f with the PY concept cells as the pseudo-population, BH over 12 tests.\n\"\"\")\n\ncode(r\"\"\"\nCPY = np.where(CONCEPT & (TY == \"PY\"))[0]\nCIN = np.where(CONCEPT & (TY == \"IN\"))[0]\nBW[\"PY\"] = bw_run(\"PY\", CPY)\nBW[\"IN\"] = bw_run(\"IN\", CIN)\nprint(f\"PY concept cells {len(CPY)}, IN concept cells {len(CIN)}\")\nprint(BW[\"PY\"][1].to_string(index=False))\nprint(\"paper: 26.67, 23.33 (P > 0.05), 40.00, 43.33% (P = 0.030)\")\n\"\"\", tags=[\"claim:fig6i-py-bin-width-decoding\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## fig6j-in-bin-width-decoding\n\n> Interneuron concept cells decoded the image above chance during load 1 maintenance at all bin\n> widths (53.33%, 50.00%, 46.67%, 53.33%), less sensitive to bin width than pyramidal cells.\n\"\"\")\n\ncode(r\"\"\"\nprint(BW[\"IN\"][1].to_string(index=False))\nprint(\"paper: 53.33, 50.00, 46.67, 53.33% (P = 0.002)\")\n\"\"\", tags=[\"claim:fig6j-in-bin-width-decoding\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## fig6kl-cross-temporal-by-type\n\n> Cross-temporal decoding showed no above-chance generalization for the 11 pyramidal concept\n> cells, while interneuron concept cells decoded above chance in cross-temporal maps.\n\"\"\")\n\ncode(r\"\"\"\nCT[(\"PY\", 1, \"first\")] = ct_analysis(CPY, 1, \"first\")\nCT[(\"IN\", 1, \"first\")] = ct_analysis(CIN, 1, \"first\")\nprint(pd.concat([summarize_ct(CT[(\"PY\", 1, \"first\")], \"PY concept, load 1\"),\n                 summarize_ct(CT[(\"IN\", 1, \"first\")], \"IN concept, load 1\")]).to_string(index=False))\n\"\"\", tags=[\"claim:fig6kl-cross-temporal-by-type\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\nmd(r\"\"\"\n## ext5ij-load2-decoding-by-type\n\n> Interneuron concept cells also decoded the second image in load 2 trials above chance at all bin\n> widths, while pyramidal concept cells did not.\n\"\"\")\n\ncode(r\"\"\"\nfor g in [\"IN\", \"PY\"]:\n    df = BW[g][1]\n    print(f\"{g} concept cells, load 2:\")\n    print(df[df.load == 2].to_string(index=False))\n\"\"\", tags=[\"claim:ext5ij-load2-decoding-by-type\"])\n\nmd(r\"\"\"\n**Result: see the numbers above.** Placeholder.\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"notebook ran in {(time.time() - T0) / 60:.1f} min\")\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\nPlaceholder.\n\"\"\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_part7.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR; cat > build_nb.py <<'EOF'
import nbformat, sys
src = ""
for p in ["nb_part1.py","nb_part2.py","nb_part3.py","nb_part4.py","nb_part5.py","nb_part6.py","nb_part7.py"]:
    src += open(p).read() + "\n"
ns = {}
exec(src, ns)
nb = nbformat.v4.new_notebook()
for kind, text, tags in ns["CELLS"]:
    c = nbformat.v4.new_markdown_cell(text) if kind == "markdown" else nbformat.v4.new_code_cell(text)
    if tags:
        c.metadata["tags"] = tags
    nb.cells.append(c)
nb.metadata["kernelspec"] = {"name": "python3", "display_name": "Python 3", "language": "python"}
nbformat.write(nb, sys.argv[1])
print(len(nb.cells), "cells")
EOF
source dev/bin/activate; python build_nb.py entries/kussovska-2025/reproduce_kussovska_2025.ipynb; date -u
```

```
151 cells
Tue Nov 10 05:54:10 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; python -m ipykernel install --user --name devk >/dev/null 2>&1; cat > $TMPDIR/run_nb.py <<'EOF'
import nbformat, sys, time
from nbclient import NotebookClient
nb = nbformat.read(sys.argv[1], as_version=4)
t=time.time()
c = NotebookClient(nb, timeout=3600, kernel_name="python3", allow_errors=True, resources={"metadata": {"path": sys.argv[3]}})
c.execute()
nbformat.write(nb, sys.argv[2])
print("ran in", round(time.time()-t), "s")
for i, cell in enumerate(nb.cells):
    if cell.cell_type == "code":
        for o in cell.get("outputs", []):
            if o.get("output_type") == "error":
                print("ERROR in cell", i, cell.metadata.get("tags"), o["ename"], o["evalue"][:300])
EOF
timeout 4000 python $TMPDIR/run_nb.py reproduce_kussovska_2025.ipynb $TMPDIR/exec.ipynb $PWD 2>&1 | tail -30
```

```
Exit code 143
Terminated                 timeout 4000 python $TMPDIR/run_nb.py reproduce_kussovska_2025.ipynb $TMPDIR/exec.ipynb $PWD 2>&1 | tail -30
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; python - <<'EOF'
s=open('nb_part4.py').read()
old='''    if side == "one":
        p = binom.sf(k - 1, N, 0.2)
    else:
        p = np.vectorize(lambda kk: binomtest(int(kk), N, 0.2).pvalue)(k)'''
new='''    if side == "one":
        p = binom.sf(k - 1, N, 0.2)
    else:
        p = TWO_SIDED.setdefault(N, np.array([binomtest(kk, N, 0.2).pvalue for kk in range(N + 1)]))[k]'''
assert old in s; s=s.replace(old,new)
s=s.replace('def sig_mask(acc, N, side):','TWO_SIDED = {}\n\n\ndef sig_mask(acc, N, side):')
open('nb_part4.py','w').write(s)
EOF
cat > $TMPDIR/run_nb.py <<'EOF'
import nbformat, sys, time
from nbclient import NotebookClient
nb = nbformat.read(sys.argv[1], as_version=4)
start = int(sys.argv[4]) if len(sys.argv) > 4 else 0
c = NotebookClient(nb, timeout=3600, kernel_name="python3", allow_errors=True, resources={"metadata": {"path": sys.argv[3]}})
t0=time.time()
with c.setup_kernel():
    for i, cell in enumerate(nb.cells):
        if cell.cell_type != "code": continue
        t=time.time()
        c.execute_cell(cell, i)
        err=[o for o in cell.get("outputs",[]) if o.get("output_type")=="error"]
        print(f"cell {i} {cell.metadata.get('tags')} {time.time()-t:.0f}s total {time.time()-t0:.0f}s", ("ERROR "+err[0]['ename']+": "+err[0]['evalue'][:200]) if err else "", flush=True)
        nbformat.write(nb, sys.argv[2])
EOF
echo ok
```

```
Tue Nov 10 07:01:23 UTC 2026
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd $TMPDIR && python build_nb.py entries/kussovska-2025/reproduce_kussovska_2025.ipynb && cd entries/kussovska-2025 && timeout 2700 python $TMPDIR/run_nb.py reproduce_kussovska_2025.ipynb $TMPDIR/exec.ipynb $PWD 2>&1 | grep -v Warn | tail -80
```

```
151 cells
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
cell 1 None 29s total 29s 
cell 3 ['sanity'] 2s total 31s 
cell 5 ['sanity'] 0s total 31s 
cell 7 ['sanity'] 0s total 31s 
cell 9 ['sanity'] 1s total 32s 
cell 11 ['sanity'] 0s total 32s 
cell 13 ['sanity'] 0s total 32s 
cell 16 ['claim:units-by-region'] 0s total 32s 
cell 19 ['claim:behavior-accuracy'] 0s total 32s 
cell 22 ['claim:fig1c-accuracy-load1-vs-load3'] 0s total 32s 
cell 25 ['claim:behavior-rt'] 0s total 32s 
cell 28 ['claim:rt-in-vs-out-memory'] 0s total 32s 
cell 31 ['claim:rt-correct-vs-incorrect'] 0s total 32s 
cell 34 ['claim:fig1e-load-modulated-neurons'] 27s total 59s 
cell 37 ['claim:fig1f-rt-modulation-not-significant'] 0s total 60s 
cell 40 ['claim:concept-cells-count'] 3s total 63s 
cell 43 ['claim:fig2ab-single-cells-not-persistent'] 2s total 64s 
cell 46 ['claim:fig2c-population-persistence'] 0s total 65s 
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cat > $TMPDIR/show.py <<'EOF'
import nbformat, sys
nb = nbformat.read(sys.argv[1], as_version=4)
lo, hi = int(sys.argv[2]), int(sys.argv[3])
for i, c in enumerate(nb.cells):
    if c.cell_type != "code" or not (lo <= i <= hi): continue
    print(f"===== cell {i} {c.metadata.get('tags')}")
    for o in c.get("outputs", []):
        if o.get("output_type") == "stream": print(o["text"][:int(sys.argv[4]) if len(sys.argv)>4 else 6000])
        elif o.get("output_type") == "error": print("ERROR", o["ename"], o["evalue"], "\n".join(o["traceback"][-3:])[-1500:])
        elif "text/plain" in o.get("data", {}) and "image/png" not in o.get("data", {}): print(o["data"]["text/plain"][:2000])
EOF
python $TMPDIR/show.py $TMPDIR/exec.ipynb 0 31
```

```
===== cell 1 None
streamed 21 Sternberg files of dandiset 000469 version 0.231213.2047 in 27 s

code tables: {'INFO': (2056, 9), 'FINAL': (1575, 14), 'SHIP_REG': (902, 5), 'SHIP_CM': (902, 11), 'VALID': (343, 6)}

===== cell 3 ['sanity']
versions: ['draft', '0.231213.2047', '0.240122.1800', '0.240122.1812', '0.240123.1806']
  draft: 41 assets, 9.79 GB, same assets as 0.231213.2047: True
  0.231213.2047: 41 assets, 9.79 GB, same assets as 0.231213.2047: True
  0.240122.1800: 41 assets, 9.79 GB, same assets as 0.231213.2047: True
  0.240122.1812: 41 assets, 9.79 GB, same assets as 0.231213.2047: True
  0.240123.1806: 41 assets, 9.79 GB, same assets as 0.231213.2047: True
files per session type: {'ses-2': 21, 'ses-1': 20} ; subjects: 21
paper: 21 patients, 41 recording sessions

===== cell 5 ['sanity']
 sub  age sex  units  trials description
   1 P25Y   F     40     135     SBID: 1
   2 P42Y   F     32     135     SBID: 2
   3 P53Y   F     28     135     SBID: 3
[... 186 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; python $TMPDIR/show.py $TMPDIR/exec.ipynb 32 72 4000
```

```
===== cell 34 ['claim:fig1e-load-modulated-neurons']
largest |slope - sklearn slope| over 21 neurons: 1.13e-04
neurons with no maintenance spikes in the matched trials: 0

load, trials matched, permutation shared:
 group   n  significant  percent  null_mean     p
   AMY 259           14    5.405     13.350 0.459
   HPC 190            9    4.737      9.696 0.594
  dACC 171           18   10.526      8.719 0.025
preSMA 250           51   20.400     12.768 0.000
 vmPFC  32            6   18.750      1.643 0.009

load, trials matched, permutation within:
 group   n  significant  percent  null_mean     p
   AMY 259           15    5.792     13.328 0.357
   HPC 190           10    5.263      9.697 0.495
  dACC 171           17    9.942      8.710 0.018
preSMA 250           48   19.200     12.749 0.000
 vmPFC  32            6   18.750      1.620 0.007

[... 293 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; cat > $TMPDIR/dev12.py <<'EOF'
import pickle, numpy as np, pandas as pd, sys
sys.path.insert(0,'.'); import wm
S=pickle.load(open(sys.argv[1],'rb')); by={s['sub']:s for s in S}
NT=wm.neuron_table(S); T={s['sub']:wm.trial_frame(s) for s in S}
CC=pickle.load(open(sys.argv[2],'rb')); final=pd.read_excel(sys.argv[3])
cc=np.where(CC[('code',0)].sig.values)[0]; pref=CC[('code',0)].pref.values
FX={n:wm.fixation_stats(wm.spikes_of(by,NT.iloc[n]),T[NT.iloc[n]['sub']]) for n in cc}
subs=sorted(set(NT['sub'].values[cc]))
st=wm.window_starts(1.0,0.025,2.5)
def X_of(rows):
    B=[]
    for n in cc:
        r=NT.iloc[n]; t=T[r['sub']].set_index('trial').loc[rows[r['sub']]]
        B.append(wm.zcounts(wm.spikes_of(by,r),t.maint.values,st,1.0,*FX[n]))
    return np.concatenate(B,1)
def nc_loo(X,y):
    ok=0
    for i in range(len(y)):
        tr=np.arange(len(y))!=i
        cents=np.array([X[tr][y[tr]==c].mean(0) for c in np.unique(y)])
        ok+= np.unique(y)[np.argmin(((cents-X[i])**2).sum(1))]==y[i]
    return ok/len(y)
rc,lc=wm.pseudo_rows(T,subs,1,'code',final); rr,lr=wm.pseudo_rows(T,subs,1,'rank',final)
Xc=X_of(rc); Xr=X_of(rr)
print('nearest centroid code',nc_loo(Xc,lc),'rank',nc_loo(Xr,lr))
# per-cell: preferred image of each concept cell -> is its label (in code index) consistent? check pref selectivity in maintenance for rank rows
# what labels does the code use per subject vs PicID? 
for s in subs[:3]:
    t=T[s].set_index('trial'); print(s, list(zip(lc[::6], t.loc[rc[s][::6],'img1'].values)))
# which trials does the code pick? accuracy / probe in/out
f=final[final.num_images_presented==1]
m=pd.concat([T[s].set_index('trial').loc[f[f.subject_id==s].trial_id.values].assign(sub=s) for s in subs])
print('code load1 trials: correct frac',m.correct.mean(),'in_memory frac',m.in_memory.mean())
allt=pd.concat([T[s][T[s].load==1] for s in subs]); print('all load1: correct',allt.correct.mean(),'in mem',allt.in_memory.mean())
# probe image equals label?
print('probe pic == enc1 pic in code trials', (m.loadsProbe_PicIDs==m.img1).mean(), 'all', (allt.loadsProbe_PicIDs==allt.img1).mean())
EOF
python $TMPDIR/dev12.py $TMPDIR/S.pkl $TMPDIR/CC.pkl $TMPDIR/hwm/data/new_trial_final.xlsx
```

```
Tue Nov 10 07:18:30 UTC 2026
nearest centroid code 0.8 rank 0.8
2 [(np.int64(0), np.int64(1)), (np.int64(1), np.int64(2)), (np.int64(2), np.int64(3)), (np.int64(3), np.int64(4)), (np.int64(4), np.int64(5))]
4 [(np.int64(0), np.int64(1)), (np.int64(1), np.int64(2)), (np.int64(2), np.int64(3)), (np.int64(3), np.int64(4)), (np.int64(4), np.int64(5))]
5 [(np.int64(0), np.int64(1)), (np.int64(1), np.int64(2)), (np.int64(2), np.int64(3)), (np.int64(3), np.int64(4)), (np.int64(4), np.int64(5))]
code load1 trials: correct frac 0.9238095238095239 in_memory frac 0.5
all load1: correct 0.9276094276094277 in mem 0.49158249158249157
probe pic == enc1 pic in code trials 0.5 all 0.49158249158249157
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; cat >> $TMPDIR/dev12.py <<'EOF'
print('fast rank', wm.loo_correct(Xr@Xr.T, lr).mean(), 'sklearn rank', wm.loo_correct_sklearn(Xr, lr).mean())
print('fast rank labels 0-4', wm.loo_correct(Xr@Xr.T, lr-1).mean())
from sklearn.svm import LinearSVC
from sklearn.preprocessing import StandardScaler
print('scale', np.abs(Xr).mean(), np.abs(Xc).mean(), 'max', np.abs(Xr).max(), np.abs(Xc).max())
idx=np.arange(30)
print('LinearSVC rank', np.mean([LinearSVC(C=1).fit(Xr[idx!=i],lr[idx!=i]).predict(Xr[i:i+1])[0]==lr[i] for i in range(30)]))
# per-row distinctness: is any row duplicated across classes (trial shared)?
print('row norms rank', np.round(np.linalg.norm(Xr,axis=1)[:12],1))
print('row norms code', np.round(np.linalg.norm(Xc,axis=1)[:12],1))
EOF
python $TMPDIR/dev12.py $TMPDIR/S.pkl $TMPDIR/CC.pkl $TMPDIR/hwm/data/new_trial_final.xlsx 2>&1 | tail -6
```

```
fast rank 0.06666666666666667 sklearn rank 0.7666666666666667
fast rank labels 0-4 0.7666666666666667
scale 0.8587436254344767 0.8362558669009355 max 22.039461310320988 15.762875400808017
LinearSVC rank 0.8666666666666667
row norms rank [100.  150.6  80.  135.8  59.5  87.4  96.1  80.2  73.3 109.4  64.6  80.4]
row norms code [ 97.3 142.8  63.5  99.6  55.3  78.4  79.5  80.2  80.4  85.4  73.8  78.8]
```

**Agent calls Bash**

```bash
cd entries/kussovska-2025; python - <<'EOF'
s=open('wm.py').read()
old='''        m = _svm_fit(K[np.ix_(tr, tr)], y[tr])
        out[i] = _svm_predict(m, K[i, tr][None, :])[0] == y[i]
    return out'''
new='''        # libsvm, as sklearn calls it, expects the classes coded 0 to k-1 (SVC encodes them first)
        cls, yc = np.unique(y[tr], return_inverse=True)
        m = _svm_fit(K[np.ix_(tr, tr)], yc)
        out[i] = cls[int(_svm_predict(m, K[i, tr][None, :])[0])] == y[i]
    return out'''
assert old in s; s=s.replace(old,new)
old='''            m = _svm_fit(G[b, b][np.ix_(tr, tr)], y[tr])
            kt = G[:, b, i, :][:, tr]  # test trial i at every bin c against training trials at bin b
            acc[b] += _svm_predict(m, kt) == y[i]'''
new='''            cls, yc = np.unique(y[tr], return_inverse=True)
            m = _svm_fit(G[b, b][np.ix_(tr, tr)], yc)
            kt = G[:, b, i, :][:, tr]  # test trial i at every bin c against training trials at bin b
            acc[b] += cls[_svm_predict(m, kt).astype(int)] == y[i]'''
assert old in s; s=s.replace(old,new)
open('wm.py','w').write(s)
EOF
source $TMPDIR/dev/bin/activate; python - <<'EOF'
import sys; sys.path.insert(0,'.'); import wm, numpy as np
rng=np.random.default_rng(0)
for lab in [np.repeat(np.arange(1,6),6), np.repeat(np.arange(5),6), np.repeat(np.array([3,7,9,11,20]),6)]:
    X=rng.normal(size=(30,300))+np.eye(5)[np.searchsorted(np.unique(lab),lab)]@rng.normal(size=(5,300))*0.3
    print((wm.loo_correct(X@X.T,lab)==wm.loo_correct_sklearn(X,lab)).all(), wm.loo_correct(X@X.T,lab).mean())
X3=rng.normal(size=(30,20,4)); y=np.repeat(np.arange(1,6),6)
a=wm.loo_cross_temporal(X3,y); b=wm.loo_cross_temporal(X3,y-1); print(np.allclose(a,b))
EOF
```

```
True 0.9
True 0.7666666666666667
True 0.8
True
```

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
s=open('nb_part4.py').read()
old='''plt.imshow(r["acc"] * 100, origin="lower", vmin=0, vmax=100, cmap="viridis")
plt.contour(r["one"]["code"], levels=[0.5], colors="r")
plt.xlabel("test bin")
plt.ylabel("train bin")
plt.colorbar(label="accuracy (%)")'''
new='''im = plt.imshow(r["acc"] * 100, origin="lower", vmin=0, vmax=100, cmap="viridis")
if r["one"]["code"].any():
    plt.contour(r["one"]["code"].astype(float), levels=[0.5], colors="r")
plt.xlabel("test bin")
plt.ylabel("train bin")
plt.colorbar(im, label="accuracy (%)")'''
assert old in s; s=s.replace(old,new)
old='''X, y = bw_design(CELLS_C, 1, "code", 1.0)
print("fast SVM equals sklearn SVC(kernel='linear') on this design, every LOOCV prediction:",
      bool((wm.loo_correct(X @ X.T, y) == wm.loo_correct_sklearn(X, y)).all()))'''
new='''for reading in ["code", "rank"]:
    X, y = bw_design(CELLS_C, 1, reading, 1.0)
    print(f"reading {reading}: fast SVM equals sklearn SVC(kernel='linear') in every LOOCV prediction:",
          bool((wm.loo_correct(X @ X.T, y) == wm.loo_correct_sklearn(X, y)).all()))'''
assert old in s; s=s.replace(old,new)
open('nb_part4.py','w').write(s)
EOF
source dev/bin/activate; python build_nb.py entries/kussovska-2025/reproduce_kussovska_2025.ipynb && cd entries/kussovska-2025 && timeout 2700 python $TMPDIR/run_nb.py reproduce_kussovska_2025.ipynb $TMPDIR/exec.ipynb $PWD 2>&1 | grep -E "ERROR|cell 149|total 9" | tail -20; date -u
```

```
151 cells
cell 138 ['claim:fig6i-py-bin-width-decoding'] 35s total 904s 
cell 141 ['claim:fig6j-in-bin-width-decoding'] 0s total 904s 
cell 149 None 0s total 1033s 
Tue Nov 10 07:36:38 UTC 2026
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; python $TMPDIR/show.py $TMPDIR/exec.ipynb 52 72 3000 | grep -v "^\s*$"
```

```
===== cell 52 ['claim:fig2d-cross-temporal-localized']
58 concept cells, 30 trials, 49 bins; maintenance starts 1.32 s after first-encoding onset
accuracy: diagonal mean 0.324, range 0.000 to 1.000; mean largest cluster extent in shuffled maps 0.0 bins
                      map binomial cluster_rule  sig_pairs  kept_pairs  kept_offdiag  train_bins_enc_or_early_with_offdiag  max_frac_maint_test_bins_from_a_maint_train_bin  null95_extent
load 1, all concept cells      one         code        290         227           217                                    17                                             0.14            0.0
load 1, all concept cells      one         perm        290         290           280                                    17                                             0.18            0.0
load 1, all concept cells      two         code        290         227           217                                    17                                             0.14            0.0
load 1, all concept cells      two         perm        290         290           280                                    17                                             0.18            0.0
===== cell 55 ['claim:ext1de-cross-temporal-load23']
                map binomial cluster_rule  sig_pairs  kept_pairs  kept_offdiag  train_bins_enc_or_early_with_offdiag  max_frac_maint_test_bins_from_a_maint_train_bin  null95_extent
             load 1      one         code        290         227           217                                    17                                             0.14            0.0
             load 1      one         perm        290         290           280                                    17                                             0.18            0.0
             load 1      two         code        290         227           217                                    17                                             0.14            0.0
             load 1      two       
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; python $TMPDIR/show.py $TMPDIR/exec.ipynb 74 100 2500 | grep -v "^\s*$" | cut -c1-230
```

```
===== cell 74 ['claim:fig3d-encoding-vs-maintenance-separability']
You chose to determine the regularization parameter automatically. This can
                    take substantial time and grows linearly with the number of crossvalidation
                    folds. The latter can be set by changing self.n_trials (default = 3). Similarly,
                    use self.protect to set the list of axes that are not supposed to get to get shuffled
                    (e.g. upon splitting the data into test- and training, time-points should always
                    be drawn from the same trial, i.e. self.protect = ['t']). This can significantly
                    speed up the code.
Start optimizing regularization.
Starting trial  1 / 3
Starting trial  2 / 3
Starting trial  3 / 3
Optimized regularization, optimal lambda =  0.00016398978063355798
Regularization will be fixed; to compute the optimal                    parameter again on the next fit, please                    set opt_regularizer_flag to True.
You chose to determine the regularization parameter automatically. This can
                    take substantial time and grows linearly with the number of crossvalidation
                    folds. The latter can be set by changing self.n_trials (default = 3). Similarly,
                    use self.protect to set the list of axes that are not supposed to get to get shuffled
                    (e.g. upon splitting the data into test- and training, time-points should always
                    be drawn from the same trial, i.e. self.protect = ['t']). This can significantly
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; python $TMPDIR/show.py $TMPDIR/exec.ipynb 92 97 100000 | grep -E "prominence/d2/real|five named|methods/height/d2/real" | cut -c1-200
```

```
code/prominence/d2/real     All902 20          6.0          2.9          18  9.0 0.0003 0.0027
   code/prominence/d2/real     LowACG 12         29.0         24.4          10  4.0 0.0060 0.0161
   code/prominence/d2/real    HighACG 12         11.5          9.4           8 27.0 0.3465 0.3465
   code/prominence/d2/real ShortDecay 12         19.0         18.5          10 13.0 0.0414 0.0552
   code/prominence/d2/real  LongDecay 12         15.5         12.9           8 22.0 0.1823 0.2084
   code/prominence/d2/real    Concept  9         27.0         24.6           8  4.0 0.0284 0.0454
   code/prominence/d2/real         PY 12         29.0         19.7          12  0.0 0.0022 0.0089
   code/prominence/d2/real         IN 19         11.0          7.2          14 31.0 0.0100 0.0200
   code/prominence/d2/real     AllFit 12          6.5          3.1          10  6.0 0.0096    NaN
    methods/height/d2/real     All902 20         41.5         33.6          16 14.0 0.0007 0.0054
    methods/height/d2/real     LowACG 12         43.5         35.5          10  7.0 0.0121 0.0483
    methods/height/d2/real    HighACG 12         47.0         43.2           4 32.0 0.5829 0.6662
    methods/height/d2/real ShortDecay 12         46.0         43.4           6 29.0 0.4328 0.6662
    methods/height/d2/real  LongDecay 12         42.0         44.2           4 31.0 0.5303 0.6662
    methods/height/d2/real    Concept  5         43.0         42.4           2  7.0 0.8927 0.8927
    methods/height/d2/real         PY 12         41.0         33.8           8 12.0 0.0342 0.0911
    methods/height/d2/real         IN 19         41.0         38.1          10 80.0 0.5461 0.6662
    methods/height/d2/real     AllFit 12         43.0         38.5          10  9.0 0.0186    NaN
methods/prominence/d2/real     All902 20          6.0          3.0          18  9.0 0.0003 0.0027
methods/prominence/d2/real     LowACG 12         21.0         15.1          11  1.0 0.0029 0.0057
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; python $TMPDIR/show.py $TMPDIR/exec.ipynb 103 112 100000 | grep -v "^\s*$" | cut -c1-260
```

```
===== cell 103 ['claim:fig4f-all-cells-epochs']
All902, load 1 (medians are bursts per window; q is BH over the 10 pairs):
                     reading  n  med_enc  med_M1  med_M2  med_M3  med_probe   q_M1   q_M2   q_M3  q_probe  min_q_other  q_M1-M2  q_M1-M3
          code/height/M-code 20     41.5    42.0    38.5    37.0       41.0 0.4377 0.6169 0.4377   0.6429       0.3632   0.4916   0.3632
       code/height/M-methods 20     41.5    46.5    44.5    28.0       41.0 0.0024 0.0038 0.0003   0.7117       0.0003   0.8089   0.0003
      code/prominence/M-code 20      6.0    14.0    14.0    15.0        5.5 0.0003 0.0003 0.0003   0.6800       0.0003   0.8103   0.2073
   code/prominence/M-methods 20      6.0    17.0    14.0    11.5        5.5 0.0003 0.0003 0.0352   0.6120       0.0003   0.0551   0.0003
       methods/height/M-code 20     41.5    42.0    38.5    37.0       41.0 0.4377 0.6169 0.4377   0.6429       0.3632   0.4916   0.3632
    methods/height/M-methods 20     41.5    46.5    44.5    28.0       41.0 0.0024 0.0038 0.0003   0.7117       0.0003   0.8089   0.0003
   methods/prominence/M-code 20      6.0    14.0    14.0    15.0        5.5 0.0003 0.0003 0.0003   0.6800       0.0003   0.8103   0.2073
methods/prominence/M-methods 20      6.0    17.0    14.0    11.5        5.5 0.0003 0.0003 0.0352   0.6120       0.0003   0.0551   0.0003
AllFit, load 1 (medians are bursts per window; q is BH over the 10 pairs):
                     reading  n  med_enc  med_M1  med_M2  med_M3  med_probe   q_M1   q_M2   q_M3  q_probe  min_q_other  q_M1-M2  q_M1-M3
          code/height/M-code 12     43.0    44.0    40.5    34.0       45.0 0.7891 0.7891 0.1465   0.6892       0.0488   0.6892   0.1953
       code/height/M-methods 12     43.0    48.0    47.0    32.0       45.0 0.0889 0.3821 0.0016   0.5360       0.0016   0.2497   0.0016
      code/prominence/M-code 12      6.5    14.0    14.5    14.0        5.5 0.0016 0.0016 0.0016   0.5151       0.0016   0.5328   0.5962
   code/prominence/M-
[... 91 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; python $TMPDIR/show.py $TMPDIR/exec.ipynb 113 150 100000 | grep -v "^\s*$" | cut -c1-240
```

```
===== cell 113 ['claim:fig5kl-concept-cell-types']
reading (a): concept cells PY 11, IN 16, unclassified 31; Royer burst index median PY 0.992, IN 0.424; ISI CV median PY 1.773, IN 1.259; Holt CV2 median PY 1.198, IN 0.994
reading (b): concept cells PY 11, IN 14, unclassified 33; Royer burst index median PY 0.949, IN 0.390; ISI CV median PY 2.690, IN 4.617; Holt CV2 median PY 1.217, IN 0.991
paper: PY 11 (9.9 to 12.1), IN 14 (12.6 to 15.4)
===== cell 116 ['claim:fig6ab-celltype-bursts-vs-null']
(a) Poisson null, enc:
                   reading group  n  real_median  null_median  real_above    W      p   p_BH
       code/height/d1/real    PY 12         41.0         34.6           8 11.0 0.0281 0.1122
       code/height/d1/real    IN 19         41.0         38.4          10 85.0 0.6874 0.7856
        code/height/d2/own    PY 12         41.0         42.5           7 32.0 0.5829 0.6662
        code/height/d2/own    IN 19         41.0         44.3           5 49.0 0.0641 0.2848
       code/height/d2/real    PY 12         41.0         34.6           9 11.0 0.0281 0.1122
       code/height/d2/real    IN 19         41.0         37.8          10 84.0 0.6580 0.7942
   code/prominence/d1/real    PY 12         29.0         20.1          12  0.0 0.0022 0.0089
   code/prominence/d1/real    IN 19         11.0          6.9          14 34.5 0.0149 0.0298
    code/prominence/d2/own    PY 12         29.0         23.3          11  1.0 0.0029 0.0115
    code/prominence/d2/own    IN 19         11.0          7.6          15 28.0 0.0070 0.0140
   code/prominence/d2/real    PY 12         29.0         19.7          12  0.0 0.0022 0.0089
   code/prominence/d2/real    IN 19         11.0          7.2          14 31.0 0.0100 0.0200
    methods/height/d1/real    PY 12         41.0         34.9           8 10.0 0.0229 0.0611
[... 290 more lines not kept]
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; cd entries/kussovska-2025; python - <<EOF 2>&1 | grep -v Warn
import pandas as pd, numpy as np, sys; sys.path.insert(0,'.'); import wm
from scipy.stats import mannwhitneyu
from statsmodels.stats.multitest import multipletests
Fa=pd.read_pickle('$TMPDIR/F.pkl'); Fb=pd.read_pickle('$TMPDIR/F2.pkl')
d=Fb[Fb.r2>0.3].dropna(subset=['firing_rate','acg_norm','tau_rise']); ty,_=wm.spectral_types(d)
t=np.array([None]*902,dtype=object); t[d.index.values]=ty
for c,F in [('cv_isi',Fa),('cv2_holt',Fa),('burst_royer',Fb)]:
    a=F[c][t=='PY']; b=F[c][t=='IN']; print(c, a.mean(), a.median(), b.mean(), b.median(), mannwhitneyu(b,a).pvalue)
EOF
```

```
cv_isi 1.7961929542440576 1.5927365386046204 1.7107463907470115 1.3219634087440122 0.00010678472966205799
cv2_holt 1.1799762613670592 1.1755416722571037 0.9322102696984816 0.9524014752963906 1.6197785611598722e-35
burst_royer 5.560867589898378 0.9470514358273825 0.6933657667716377 0.6216004378958615 0.004984813918605497
```

**Agent calls Bash**

```bash
source $TMPDIR/dev/bin/activate; python $TMPDIR/show.py $TMPDIR/exec.ipynb 43 43 100000 | tail -8; python - <<'EOF'
import pickle,sys
sys.path.insert(0,'entries/kussovska-2025'); import wm
S=pickle.load(open('/tmp/claude-1001/S.pkl','rb'))
for s in S:
    if s['sub'] in (9,21):
        t=wm.trial_frame(s); bad=t[(t.maint_dur<2)|(t.enc1-t.fix_start>2)|(t.enc1<=t.fix_start)]
        print(s['sub'], bad[['trial','fix_start','enc1','maint','probe','timestamps_Response','load']].to_string())
EOF
```

```
58 concept cells; preferred load-1 trials per cell 6 to 9
persistent under (a): 8; not persistent: 50
persistent under (b): 10; not persistent: 48
cells significant in M1, M2, M3: {'M1': 25, 'M2': 19, 'M3': 13}
by participant (persistent a / cells): {2: {'cells': 3, 'pa': 0, 'pb': 0}, 4: {'cells': 6, 'pa': 0, 'pb': 0}, 5: {'cells': 1, 'pa': 0, 'pb': 0}, 7: {'cells': 3, 'pa': 1, 'pb': 1}, 8: {'cells': 1, 'pa': 0, 'pb': 0}, 9: {'cells': 4, 'pa': 0, 'pb': 0}, 11: {'cells': 3, 'pa': 0, 'pb': 0}, 12: {'cells': 1, 'pa': 1, 'pb': 1}, 13: {'cells': 9, 'pa': 0, 'pb': 0}, 14: {'cells': 14, 'pa': 5, 'pb': 4}, 15: {'cells': 1, 'pa': 0, 'pb': 0}, 16: {'cells': 5, 'pa': 0, 'pb': 2}, 18: {'cells': 5, 'pa': 1, 'pb': 2}, 21: {'cells': 2, 'pa': 0, 'pb': 0}}
threshold variant, persistent when at least 25% of bins are higher: 19 of 58
threshold variant, persistent when at least 75% of bins are higher: 1 of 58

9     trial   fix_start        enc1       maint       probe  timestamps_Response  load
28     29  525.715789  526.783195  529.288256  529.288256           532.073036     1
21     trial   fix_start        enc1       maint       probe  timestamps_Response  load
68     69  484.259399  498.329706  500.509236  503.162704           506.167921     2
```

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
import re
def rep(fn, old, new):
    s=open(fn).read(); assert old in s, (fn, old[:60]); s=s.replace(old,new); open(fn,'w').write(s)

rep('nb_part1.py', '''The files hold 902 units (as the paper says) in five regions, each with a left and a right label.
Fifteen sessions have 135 trials and six have 108 (subjects 6, 7, 8, 9, 16 and 19); the paper
says sixteen and five. The ages run from 17 to 70; the paper's 17 to 71 and its mean are over
sessions, which cannot be checked from one Sternberg file per subject.''',
'''The files hold 902 units (as the paper says) in five regions, each with a left and a right label.
Fifteen sessions have 135 trials and six have 108 (subjects 6, 7, 8, 9, 16 and 19); the paper
says sixteen and five, so the data disagree with the description there. The ages run from 17 to
70 (mean 36.19); the paper gives 17 to 71 and 36.10 over sessions, which one Sternberg file per
subject cannot check.''')
rep('nb_part1.py', '''Every session has equal numbers of trials per load and five images (ids 1 to 5) in its encoding
periods. The epoch timestamps are ordered in every trial. The maintenance and fixation
durations printed above are in seconds; they are compared with the paper's values there. Spike
times are in seconds on the same clock as the trials table (they span the trials of each
session); the check by contrast below shows the alignment.''',
'''Every session has equal numbers of trials per load and five images (ids 1 to 5) in its encoding
periods. The epoch timestamps are ordered in every trial except one: in subject 9 (the session
marked False above) one trial has a maintenance timestamp equal to its probe timestamp, a
maintenance of 0 s, and its fixation durations include 0 s. Apart from that trial, maintenance
lasts about 2.53 to 2.84 s (paper: 2.5 to 2.8 s). Fixation lasts about 0.91 to 1.2 s in most
sessions, longer than the paper's 0.9 to 1.0 s, with single long fixations (14.07 s in subject 21).
The first encoding image lasts 1.0, 1.2, 1.5 or 2.5 s depending on the session (enc1_s); the
paper does not state the image duration, and the code's 1 s encoding window is used throughout.
Spike times are in seconds and span each session's trials; the contrast below checks the clock.''')
rep('nb_part1.py', '''Across sessions, many more neurons are image-selective in the window after the first encoding
onset than in the shifted windows, and the population rate rises after image onset in most
sessions (totals and per-session counts above). This shows that spike times and the trial table
share a clock in the sessions where neurons respond; a session with no selective neurons and no
evoked rise in the table above cannot be checked this way.''',
'''Over all sessions, 58 neurons are image-selective in the window after the first encoding onset,
against 11 and 16 in the windows shifted 1 s and 2 s earlier, so image information appears where
the trials table puts the images. This is consistent with spike times and trials sharing a clock;
it is shown per session only where selective neurons exist. Subjects 1, 3, 6, 10, 17, 19 and 20
have no selective neuron in the true window, and the population rate barely changes after image
onset in any session (ratios 0.89 to 1.14), so for those seven sessions the alignment could not
be established.''')
rep('nb_part1.py', '''every load-1 row is the same in all 21 sessions and maps one to one onto each session's picture
ids, so its load-1 rows can align a pseudo-population. Its load-2 and load-3 rows are not
aligned on the label image in every session (fractions above), so those pseudo-populations
mix labels across sessions; the code takes subject 14's labels. The code's neuron table lists
the dataset's units in order.''',
'''every load-1 row is the same in all 21 sessions and maps one to one onto each session's picture
ids, so its rows can align a pseudo-population; its load-2 and load-3 rows are aligned on the
label image (second and third) in every session too. The code's neuron table lists the dataset's
units in order, with the same locations. Several sessions share one trial sequence, and the
subjects with 108 trials have 106 rows in new_trial_info.''')
rep('nb_part2.py', '''**Result: reproduced.** All three readings fall within 0.78 to 1.34 s (values above).''',
'''**Result: reproduced.** Readings (a), 1.120 s, and (c), 1.097 s, fall within 0.78 to 1.34 s;
reading (b), 1.348 s, is just above it. The spreads are 0.252 s (s.d. of participant medians)
and 0.297 s (half the IQR of trials), near the paper's 0.28.''')
rep('nb_part2.py', '''**Result: reproduced.** Load 1 accuracy is higher than load 3 across patients; the rank-sum p
(raw and Bonferroni) and the paired variant are printed above, with p < 0.05 under the raw
reading.''', '''**Result: reproduced.** Load 1 accuracy (median 94.44%) is higher than load 3 (86.67%); the
rank-sum p is 0.0090 raw and 0.0270 after the code's Bonferroni factor of 3, the paper's P = 0.027.
The paired variant gives p = 0.0042.''')
rep('nb_part2.py', '''**Result: reproduced.** The mean of the 21 participants' accuracies is printed above with its
s.e.m., which is the spread the code computes; it matches the paper's value and spread. The
pooled variant is also shown.''', '''**Result: reproduced.** The mean of the 21 participants' accuracies is 88.73% with s.e.m. 1.25,
the paper's value and spread (the s.d. is 5.74); the pooled variant gives 88.70%.''')
rep('nb_part2.py', '''**Result: reproduced.** Probes held in memory are answered faster, in most participants, with
p < 0.05 under every reading (above).''', '''**Result: reproduced.** Probes held in memory are answered faster (correct trials, medians 1.041
against 1.184 s, faster in 17 of 21 participants), with p at most 0.002 under every reading.''')
rep('nb_part2.py', '''**Result: reproduced.** Correct responses are faster than incorrect ones, with p < 0.05 under
both readings (above).''', '''**Result: reproduced.** Correct responses are faster than incorrect ones (medians 1.084 against
1.503 s, in 20 of 21 participants), p = 0.001 under both readings.''')
rep('nb_part2.py', '''**Result: reproduced.** Under reading (a) with the code's shared permutation, preSMA, vmPFC and
dACC are each within tolerance with p < 0.05 (dACC exactly 10.53%, vmPFC exactly 18.75%); the
within-participant permutation gives nearly the same. With all trials (reading b) the three
regions stay significant, with somewhat higher percentages. The amygdala and hippocampus are not
significant under any reading.''', '''**Result: reproduced.** Under reading (a) with the code's shared permutation, preSMA (20.40%,
p = 0.000), vmPFC (18.75%, p = 0.009) and dACC (10.53%, p = 0.025) are each within tolerance with
p < 0.05; the within-participant permutation gives 19.20%, 18.75% and 9.94%, also within
tolerance. With all trials (reading b) the three regions stay significant with higher
percentages (22.80%, 21.88%, 12.87%). The amygdala and hippocampus are not significant under any
reading.''')
rep('nb_part2.py', '''**Result: reproduced.** Under the code's bootstrap (reading b) the count is 57 to 60 over ten
seeds, the amygdala holds most concept cells and the amygdala and hippocampus shares are within
tolerance (seed 0 gives the paper's regional counts exactly). The Methods' bootstrap (reading a)
finds fewer cells (range above), also within tolerance. The set used in later sections is
reading (b), seed 0, a standard choice of seed; it shares all but one cell with the code's
shipped list.''', '''**Result: reproduced.** Under the code's bootstrap (reading b) the count is 57 to 60 over ten
seeds, all within tolerance, with the amygdala share 70.18 to 72.41% and the hippocampus share
17.24 to 19.30%; seed 0 gives the paper's regional shares exactly (41, 11, 1, 2 and 3 cells). The
Methods' bootstrap (reading a) finds 49 to 54 cells, within tolerance only for two seeds. The
per-participant spread is 4.14 +/- 3.66 over the 14 participants with a concept cell, close to
the paper's 4 +/- 4. The set used in later sections is reading (b), seed 0 (a standard choice of
seed); it shares 57 of its 58 cells with the code's shipped list.''')
rep('nb_part3.py', '''**Result: reproduced.** Under both readings most concept cells are not persistent (counts above),
and this holds with a looser or stricter bin threshold.''', '''**Result: reproduced.** 50 of 58 concept cells are not persistent under reading (a) and 48 under
reading (b); with a 25% bin threshold 39 are not persistent.''')
rep('nb_part3.py', '''**Result: reproduced.** At load 1 the population's preferred trace is above the nonpreferred one
throughout maintenance and the significant bins meet both readings (above). No point of the
plot falls outside its axes, whose ranges are printed.''', '''**Result: reproduced.** At load 1 the population's preferred trace (mean z 0.761) is above the
nonpreferred one (-0.013) in every maintenance bin, and every bin is significant after BH, so
both readings hold. No point of the plot falls outside its axes, whose ranges are printed.''')
rep('nb_part3.py', '''**Result: reproduced.** Loads 1 and 2 meet the persistence readings and load 3 has a smaller
fraction of significant bins than either (above).''', '''**Result: reproduced.** Loads 1 and 2 have all maintenance bins significant and load 3 has 0.60,
smaller than either, with a smaller preferred minus nonpreferred difference (0.774, 0.487 and
0.325 z).''')
rep('nb_part4.py', '''**Result: reproduced.** Decoders trained in encoding or early maintenance generalize above chance
to other bins under every reading, and no maintenance training bin generalizes to more than half
of the maintenance test bins (largest fraction above), so the clusters are localized.''', '''**Result: reproduced.** Under every reading, 17 training bins in encoding or early maintenance
have off-diagonal pairs kept above chance, and no maintenance training bin generalizes to more
than 0.18 of the maintenance test bins, so the clusters are localized. The shuffled maps had no
supra-threshold cluster (their 95th-percentile extent is 0), so the Methods' cluster rule removes
nothing here.''')
rep('nb_part4.py', '''**Result: reproduced.** Under both labels and every rule, loads 2 and 3 keep fewer off-diagonal
pairs than load 1 (above).''', '''**Result: reproduced.** Under both labels and every rule, loads 2 (6 to 10 off-diagonal pairs)
and 3 (none) keep far fewer off-diagonal pairs than load 1 (217 to 280).''')
rep('nb_part4.py', '''**Result: not reproduced.** Within participant, amygdala and MTL concept cells do not decode the
image above the shuffled null at load 1 under either cell-count rule; accuracies are below 20%
and near the null mean (above).''', '''**Result: reproduced.** At load 1 the amygdala decodes at 35.63% and the MTL at 33.61% with at
least three cells (p = 0.001 for both), and at 34.33% and 32.89% with more than three cells;
all are within tolerance.''')
rep('nb_part4.py', '''**Result: not reproduced.** At load 2 neither group's accuracy is within tolerance with
p < 0.05 (above).''', '''**Result: partially reproduced.** At load 2 both groups decode above the null (p = 0.002), and
the MTL accuracy is within tolerance (26.67% and 29.56% under the two rules), but the amygdala
accuracy (26.43% and 27.89%) is above its tolerance of 21.2 to 25.9%.''')
rep('nb_part4.py', '''**Result: not reproduced.** Under the code's trial table (reading a) load-1 accuracy rises with
bin width and is above chance at every width, but the 250 ms accuracy is outside its tolerance
(values above); under reading (b), each participant's first six trials per image, accuracy is
below chance at every width. Random draws of six trials per image fall between the two, so the
paper's numbers depend on which trials the code's table holds, and how it was built is not
stated.''', '''**Result: partially reproduced.** Under both trial readings load-1 accuracy is above chance at
every width (BH p at most 0.009) and rises from 250 to 1000 ms, but not every value is within
tolerance: reading (a) gives 30.00, 60.00, 66.67 and 76.67% (250 ms below its tolerance of 36 to
44%), reading (b) 50.00, 66.67, 73.33 and 76.67% (250 and 500 ms above theirs). Random draws of
six trials per image give 56.7 to 86.7% at 1000 ms, so the values depend on which trials enter.''')
rep('nb_part4.py', '''**Result: see the numbers above.** Placeholder.
""")

md(r"""
## ext1g-bin-width-load2''', '''**Result: not reproduced.** Under neither reading are exactly the three named pairs significant:
with the code's table 750 vs 250 and 1000 vs 250 are significant but 1000 vs 500 is not (BH p
0.079 and 0.139) and 500 vs 250 is (0.010 and 0.002); with reading (b) 750 vs 250 and 1000 vs 250
are significant (BH p 0.036 to 0.048), the three pairs the paper calls not significant are not,
and 1000 vs 500 is not significant (0.363 and 0.483).
""")

md(r"""
## ext1g-bin-width-load2''')
rep('nb_part4.py', '''**Result: see the numbers above.** Placeholder.''', '''**Result: reproduced.** The load 2 accuracies span 16.0 points with the code's table and 4.0
points with reading (b), below the 20-point threshold, and each is below the load 1 accuracy at
the same width.''')
EOF
echo done
```

```
done
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
def rep(fn, old, new, count=1):
    s=open(fn).read(); assert s.count(old)>=1, (fn, old[:70]); s=s.replace(old,new,count); open(fn,'w').write(s)
P='**Result: see the numbers above.** Placeholder.'
# part5
rep('nb_part5.py','''print("paper: burst index PY 0.985 vs IN 0.622, CV2 PY 1.673 vs IN 1.319; tolerance 10% of each")''',
'''# The claim takes CV2 from the session's interspike intervals, whichever spikes the ACG used:
# types and burst index of reading (b) with the ISI measures of all of each unit's spikes.
F, ty = FEAT["b"], TYPES["b"]
Fs = FEAT["a"]
from statsmodels.stats.multitest import multipletests
ps = [mannwhitneyu(F.burst_royer[ty == "IN"], F.burst_royer[ty == "PY"]).pvalue,
      mannwhitneyu(Fs.cv_isi[ty == "IN"], Fs.cv_isi[ty == "PY"]).pvalue,
      mannwhitneyu(Fs.cv2_holt[ty == "IN"], Fs.cv2_holt[ty == "PY"]).pvalue]
print("reading (b) types, session ISIs:")
for c, src, p in [("burst_royer", F, ps[0]), ("cv_isi", Fs, ps[1]), ("cv2_holt", Fs, ps[2])]:
    a, b = src[c][ty == "PY"], src[c][ty == "IN"]
    print(f"  {c}: PY mean {a.mean():.3f} median {a.median():.3f}; IN mean {b.mean():.3f} median {b.median():.3f}; p = {p:.2e}")
print("paper: burst index PY 0.985 vs IN 0.622, CV2 PY 1.673 vs IN 1.319; tolerance 10% of each")''')
rep('nb_part5.py', P, '''**Result: reproduced.** With the types and burst index of reading (b) and the CV of each unit's
session interspike intervals (the column the code feeds to Fig. 5h), the medians are burst index
PY 0.947 and IN 0.622 and CV PY 1.593 and IN 1.322, all within tolerance, PY higher on both with
p below 0.005 (BY-corrected 0.011 and 6e-05 in the five-metric table). The group means of the
burst index are far from the paper's (PY 5.6, a few very large values), so the paper's numbers
match medians. Under reading (a) the PY burst-index median (0.802) is outside tolerance and its
corrected p is 0.11. Holt's CV2 is lower than the paper's values (PY 1.18, IN 0.93).''')
rep('nb_part5.py', P, '''**Result: reproduced.** The clustering assigns 333 of the 343 ground-truth cells to their
cluster's majority type, with one pyramidal neuron and nine interneurons misassigned, as the
paper reports. These are the features the paper's code ships, not the CellExplorer recordings.''')
rep('nb_part5.py', '''**Result: reproduced.** Under reading (b) both counts are within tolerance; under reading (a) IN
is within tolerance and PY just outside (values above). The clustering applied to the code's
shipped features gives exactly 92 and 202, so the difference comes from the ACG fit. Later
sections use the types of reading (a), the spikes the code used (see acg-fit-yield).''',
'''**Result: reproduced.** Under reading (b) the counts are PY 100 and IN 198, both within
tolerance; under reading (a) IN (215) is within tolerance and PY (102) just above it. The
clustering applied to the code's shipped features gives exactly 92 and 202, so the difference
comes from the ACG fit. Later sections use the types of reading (a), the spikes the code used
(see acg-fit-yield), with reading (b) shown where it bears on a value.''')
rep('nb_part5.py', '''**Result: reproduced.** Both readings give a count within tolerance (above). The firing rate,
normalized mean ACG, Royer burst index and ISI CV of reading (a) equal the code's shipped table,
so the code used every spike of the unit; the fitted R2 and time constants differ from the
shipped ones for part of the neurons, as the optimizer differs from MATLAB's.''',
'''**Result: reproduced.** 317 neurons have R2 > 0.3 under reading (a) and 298 under reading (b),
both within tolerance. The firing rate and ISI CV of reading (a) equal the code's shipped table
exactly, and the normalized mean ACG and Royer burst index agree within 1% for 99% of neurons, so
the code used every spike of the unit; the fitted R2 agrees within 1% for 48% of neurons and the
time constants for 7 to 11%, as the optimizer differs from MATLAB's. Classification at R2 > 0.3
agrees for 97.5% of neurons.''')
rep('nb_part5.py', '''**Result: reproduced.** IN are higher on all three features with corrected p far below 0.05
(above); as the claims file notes, this follows from the clustering by construction.''',
'''**Result: reproduced.** IN are higher on all three features under both readings, BY-corrected p
at most 8e-05 (U = 20822, 21885 and 14159 under reading a); as the claims file notes, this follows
from the clustering by construction.''')
rep('nb_part5.py', '''**Result: blocked (too large).** One split takes the time printed above, so the 100 splits of
fig3d alone exceed the sixty-minute limit for a notebook, and fig3h and fig3abc (which uses the
same fits) add to it. The three claims are not tested.''', '''**Result: blocked (too large).** One split takes about 45 s (15.4 s encoding, 29.9 s
maintenance), so the 100 splits of fig3d take about 75 min, over the sixty-minute limit for a
notebook, and fig3h (about 50 min more) and fig3abc (which uses the same fits) add to it. The
three claims are not tested.''')
# part6
rep('nb_part6.py', '''**Result: reproduced.** Under the main reading (the code's groups, prominence rule, spacing of 2
bins, the real threshold) all neurons and the low ACG group differ from the Poisson null after
correction and the high ACG, short and long tau decay and concept groups do not (above). Other
readings differ: with the Methods' height rule or with each surrogate's own threshold, the
pattern does not hold.''', '''**Result: reproduced.** Under the Methods' groups with the height rule and the real threshold
(spacing 2 or 1 bin), all neurons (BH p 0.0054) and the low ACG group (0.0483) differ from the
Poisson null and the other four groups do not. Under the code's groups with the prominence rule
the same two differ, but the concept group does too (BH p 0.045), and the Methods' groups with
prominence make every group but concept cells differ; with the code's groups and the height rule
the low ACG group does not differ. The outcome rests on one of the readings the criterion names.''')
rep('nb_part6.py', '''**Result: reproduced.** Under the main reading the five named groups have more real than
surrogate bursts in most participants with corrected p < 0.05, and concept cells do not differ
(above); the variant with each trial's own maintenance length gives the same.''', '''**Result: reproduced.** Under the real-threshold readings (prominence or height, both group
rules) the five named groups have more real than surrogate bursts in most participants with BH
p at most 0.047, and concept cells do not differ (BH p 0.11 to 0.89). With each surrogate's own
threshold the pattern fails. The variant with each trial's own maintenance length keeps four of
the five (short tau decay BH p 0.11).''')
rep('nb_part6.py', P, '''**Result: partially reproduced.** Under the prominence rule the low ACG group bursts more than
the high ACG group in both epochs, in all 12 participants (p = 0.0005, BH p at most 0.0017), and
short and long tau decay do not differ in maintenance; but short tau decay does not exceed long
tau decay in encoding (p 0.14 with the code's groups, 0.086 with the Methods'). Under the height
rule the low ACG group bursts less than the high ACG group.''')
rep('nb_part6.py', '''**Result: partially reproduced.** Under the prominence rule, all neurons burst more in each of
M1, M2 and M3 than in encoding with corrected p < 0.05 under both window readings and both
populations, but the probe does not differ from encoding under any reading (above). Three of the
four comparisons hold.''', '''**Result: partially reproduced.** Under the prominence rule all 902 neurons burst more in each of
M1, M2 and M3 than in encoding (medians 6 against 14 to 17, BH p 0.0003 to 0.035) under both
window readings, but the probe does not differ from encoding under any reading (BH p 0.61 to
0.71; medians 6.0 and 5.5). Three of the four comparisons hold. Between maintenance windows, M1
and M3 differ only under the Methods' windows, where M3 is shorter (0.67 s).''')
rep('nb_part6.py', '''**Result: partially reproduced.** Under the main reading (the code's groups, prominence, the
code's thirds) long tau decay neurons increase from encoding to M1, M2 and M3 and the low ACG,
short tau decay and concept groups show no significant pair, but high ACG neurons increase at M1
and M2 and not at the probe (above).''', '''**Result: partially reproduced.** With the prominence rule and the code's thirds (either group
rule) long tau decay neurons increase from encoding to M1, M2 and M3 and the low ACG, short tau
decay and concept groups have no significant pair, but high ACG neurons increase at M1 and M2 and
not at the probe (BH p 0.24 to 0.38). The increases hold for one of the two groups.''')
rep('nb_part6.py', P, '''**Result: reproduced.** Under the Methods' groups with the prominence rule and the code's
thirds, all cells, high ACG and long tau decay neurons have more bursts in each maintenance
window than in encoding at loads 2 and 3, as at load 1. Under the code's groups the long tau
decay group does not at loads 2 and 3; under the height rule the pattern does not hold.''')
# part7
rep('nb_part7.py', P, '''**Result: reproduced.** Under reading (b) of the types, 11 concept cells are PY and 14 IN, the
paper's counts, and PY concept cells have the higher Royer burst index (median 0.949 against
0.390) and Holt CV2 (1.217 against 0.991). Under reading (a) the counts are 11 and 16 (IN outside
tolerance), with the same ordering.''')
rep('nb_part7.py', P, '''**Result: partially reproduced.** Against the Poisson null with the prominence rule, PY exceed the
null in encoding (BH p 0.0089) and maintenance (0.0035) and IN in maintenance (0.0012), but IN
also exceed it in encoding (0.020), where the paper finds no difference. With the height rule PY
do not differ in encoding. Against the label-shuffled null, PY exceed it in both epochs (BH p
0.0029 and 0.0057), IN fall below it in encoding (10 against 11.9, BH p 0.0016) and do not differ
in maintenance (0.063). No reading gives the paper's full pattern; the elevated PY bursting and IN
maintenance bursting hold.''')
rep('nb_part7.py', P, '''**Result: partially reproduced.** With the prominence rule and the code's thirds, PY have no
pair of periods with BH p < 0.05 at any load, and IN burst more in M1, M2 and M3 than in encoding
at load 1 (BH p 0.0047 to 0.014), but IN do not differ between encoding and the probe (0.80). The
Methods' windows make PY differ. The IN change is an increase (medians 11 to 15).''')
rep('nb_part7.py', P, '''**Result: reproduced.** With the prominence rule and the code's thirds (either group rule) the
measure rises from 3.67 at load 1 to 5.00 and 6.33; under the other readings it does not rise.''')
rep('nb_part7.py', P, '''**Result: partially reproduced.** IN are load-modulated (13.95%, p = 0.001, matched trials and
shared permutation, within tolerance) and PY and PY concept cells are not (p 0.43 and 1.0), but IN
concept cells give 18.75% (3 of 16, p = 0.042), below the tolerance of 19.3 to 23.6%; the paper's
21.42% is 3 of 14. With reading (b) of the types (14 IN concept cells) 2 are significant (p = 0.15).''')
rep('nb_part7.py', P, '''**Result: not reproduced.** With each trial's own RT, IN concept cells give 12.50% (p = 0.19)
and PY are significant (p 0.005 to 0.024). The code's predictor (subject 1's RT vector) gives IN
concept cells 31.25% (p = 0.001), just below the tolerance of 32.1 to 39.3%, with all IN (p 0.086)
and PY not significant under the shared permutation.''')
rep('nb_part7.py', P, '''**Result: not reproduced.** IN concept cells do not have higher CV2 in maintenance than in
encoding on preferred trials (load 1 p = 0.86; all loads p = 0.13). The PY and nonpreferred parts
hold (no comparison with p < 0.05).''')
rep('nb_part7.py', P, '''**Result: not reproduced.** Under the reading of the claims file (ACG tau_decay on preferred and
nonpreferred spikes), PY concept cells show no preferred-trial increase in either epoch (Wilcoxon
p 0.13 to 0.73); IN show none either (p 0.058 to 0.67). The outcome rests on that reading.''')
rep('nb_part7.py', P, '''**Result: not reproduced.** With the code's table PY concept cells give 33.33, 23.33, 36.67 and
43.33%, but none survives BH (p 0.060 to 0.39), so the 750 and 1000 ms accuracies are not
significant; with reading (b) the pattern is reversed (250 and 500 ms highest).''')
rep('nb_part7.py', P, '''**Result: partially reproduced.** IN concept cells decode above chance at every width under both
trial readings (BH p 0.002), less dependent on width than PY, but two of the four accuracies are
outside tolerance under each reading (code's table 46.67, 53.33, 53.33 and 50.00%).''')
rep('nb_part7.py', P, '''**Result: reproduced.** The PY concept map has no significant pair under any reading, and the IN
concept map keeps 162 to 230 off-diagonal pairs.''')
rep('nb_part7.py', P, '''**Result: reproduced.** At load 2 IN concept cells decode above chance at all four widths under
both readings (BH p at most 0.013) and PY concept cells at none (BH p at least 0.49).''')
EOF
grep -c Placeholder $TMPDIR/nb_part*.py
```

```
/tmp/claude-1001/nb_part1.py:0
/tmp/claude-1001/nb_part2.py:0
/tmp/claude-1001/nb_part3.py:0
/tmp/claude-1001/nb_part4.py:0
/tmp/claude-1001/nb_part5.py:0
/tmp/claude-1001/nb_part6.py:0
/tmp/claude-1001/nb_part7.py:1
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR; python - <<'EOF'
def rep(fn, old, new):
    s=open(fn).read(); assert old in s, old[:50]; s=s.replace(old,new); open(fn,'w').write(s)
rep('nb_part5.py','p below 0.005 (BY-corrected 0.011 and 6e-05 in the five-metric table)','p below 0.005 (printed above)')
rep('nb_part7.py','''## Summary

Placeholder.''','''## Summary

| Claim | Outcome |
|---|---|
| units-by-region | reproduced |
| behavior-accuracy | reproduced |
| fig1c-accuracy-load1-vs-load3 | reproduced |
| behavior-rt | reproduced |
| rt-in-vs-out-memory | reproduced |
| rt-correct-vs-incorrect | reproduced |
| fig1e-load-modulated-neurons | reproduced |
| fig1f-rt-modulation-not-significant | not reproduced |
| concept-cells-count | reproduced |
| fig2ab-single-cells-not-persistent | reproduced |
| fig2c-population-persistence | reproduced |
| ext1bc-persistence-by-load | reproduced |
| fig2d-cross-temporal-localized | reproduced |
| ext1de-cross-temporal-load23 | reproduced |
| fig2e-maintenance-decoding-amy-mtl | reproduced |
| ext1f-maintenance-decoding-load2 | partially reproduced |
| fig2f-bin-width-decoding | partially reproduced |
| fig2f-bin-width-pairwise | not reproduced |
| ext1g-bin-width-load2 | reproduced |
| fig3abc-trajectory-complexity | blocked (too large) |
| fig3d-encoding-vs-maintenance-separability | blocked (too large) |
| fig3h-early-vs-late-maintenance | blocked (too large) |
| fig4c-encoding-bursts-vs-poisson | reproduced |
| fig4d-maintenance-bursts-vs-poisson | reproduced |
| fig4-acg-group-differences | partially reproduced |
| fig4f-all-cells-epochs | partially reproduced |
| fig4hj-group-epochs | partially reproduced |
| ext2-bursts-loads23 | reproduced |
| acg-fit-yield | reproduced |
| fig5c-cell-type-clusters | reproduced |
| fig5dfh-cluster-features | reproduced |
| fig5gh-burst-index-cv2 | reproduced |
| supp4-rodent-validation | reproduced (on the features the code ships) |
| fig5kl-concept-cell-types | reproduced |
| fig6ab-celltype-bursts-vs-null | partially reproduced |
| fig6cd-celltype-epochs | partially reproduced |
| ext5bd-in-load-dependence | reproduced |
| fig6e-load-modulation-in | partially reproduced |
| fig6f-rt-modulation-in-concept | not reproduced |
| fig6gh-in-concept-cv2 | not reproduced |
| ext5gh-py-decay-preferred | not reproduced |
| fig6i-py-bin-width-decoding | not reproduced |
| fig6j-in-bin-width-decoding | partially reproduced |
| fig6kl-cross-temporal-by-type | reproduced |
| ext5ij-load2-decoding-by-type | reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.** The ACG fit is a Python port of the code's
MATLAB functions, with scipy's optimizer, so R2 and the time constants differ for part of the
neurons and the cell-type counts differ slightly (102 or 100 PY against 92); later analyses use
these types. The concept-cell bootstrap is run with fixed seeds (the code sets none); the set used
shares 57 of 58 cells with the code's list. The SVM is libsvm through sklearn's wrapper on a
precomputed linear kernel, checked equal to `SVC(kernel='linear')`. The Poisson GLM is fitted by
Newton's method, checked against sklearn. Many method details the paper leaves open were run
under each reading the claims file names; outcomes that rest on one of several readings say so.
The dPCA analyses were not run (too large).

**What was found about the dataset.** The dandiset holds all 902 units of the paper with the
paper's region counts, and the paper's code tables link to its trials exactly. The paper's
description differs from the files in the number of sessions with 108 trials (six, not five), the
fixation durations (up to 1.2 s and longer, not 0.9 to 1.0 s), and the image duration, which
varies by session (1.0 to 2.5 s) and is not stated. One trial (subject 9) has a maintenance of 0 s.
The paper's RT-modulation percentages (Fig. 1f) are reproduced exactly only with the code's
predictor, which pairs every neuron with subject 1's reaction times.''')
EOF
source dev/bin/activate; python build_nb.py entries/kussovska-2025/reproduce_kussovska_2025.ipynb
cd entries/kussovska-2025; cat > requirements.in <<'EOF'
dPCA
h5py
joblib
matplotlib
numba
numexpr
numpy
openpyxl
pandas
remfile
requests
scikit-image
scikit-learn
scipy
statsmodels
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: kussovska-2025
type: reproduction
title: Neural heterogeneity and the temporal structure of human working memory (Kussovska et al. 2025)
description: Tests the findings of Kussovska, Kim and Rungratsameetaweemana (2025) on dandiset 000469,
  the human single-neuron recordings of Kyzar et al. (2024) during a Sternberg working memory task.
  It covers behavior, GLM load and reaction-time modulation, concept cells, persistence and
  decoding of the maintained image, population bursts, autocorrelogram-based cell types and their
  bursting, task modulation and decoding. The dPCA state-space analyses were too large to run.
license: Apache-2.0
notebooks:
- path: reproduce_kussovska_2025.ipynb
  title: Reproducing Kussovska et al. (2025) from dandiset 000469
  runtime_minutes: 20
helpers:
- wm.py
related:
- id: dandi:000469/0.231213.2047
  relation: uses_data
- id: doi:10.1101/2025.10.31.684900
  relation: reproduces
EOF
cd  && python tools/entry.py lock entries/kussovska-2025 2>&1 | tail -3 && python tools/entry.py check entries/kussovska-2025 2>&1 | tail -15
```

```
Tue Nov 10 07:40:08 UTC 2026
151 cells
wrote kussovska-2025/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/kussovska-2025 2>&1 | tail -15
```

```
Installed kernelspec registry-kussovska-2025 in executed/kussovska-2025/.venv/share/jupyter/kernels/registry-kussovska-2025
0 error(s)
pass  reproduce_kussovska_2025.ipynb  (1175 s)

real	19m44.495s
user	56m0.336s
sys	0m9.208s
```

**Agent calls Bash**

```bash
date -u; ls executed/kussovska-2025/; source $TMPDIR/dev/bin/activate; python - <<'EOF'
import nbformat, difflib
a=nbformat.read('/tmp/claude-1001/exec.ipynb',4); b=nbformat.read('executed/kussovska-2025/reproduce_kussovska_2025.ipynb',4)
def txt(c): return "".join(o.get("text","") for o in c.get("outputs",[]) if o.get("output_type")=="stream")
for i,(ca,cb) in enumerate(zip(a.cells,b.cells)):
    if ca.cell_type!='code': continue
    ta,tb=txt(ca),txt(cb)
    if ta!=tb:
        d=[l for l in difflib.unified_diff(ta.splitlines(),tb.splitlines(),lineterm='',n=0) if l.startswith(('+','-')) and not l.startswith(('+++','---'))]
        print(f'== cell {i} {cb.metadata.get("tags")} {len(d)} changed lines'); print("\n".join(x[:200] for x in d[:14]))
EOF
```

```
Tue Nov 10 08:00:06 UTC 2026
reproduce_kussovska_2025.ipynb
result.json
== cell 74 ['claim:fig3d-encoding-vs-maintenance-separability'] 4 changed lines
-{'encoding': 15.4, 'maintenance': 29.9} s for one split
-fig3d needs 100 splits: about 75 min; fig3h adds two half-maintenance fits per split, about 50 min more (each half is half the bins); together about 125 min, over the 60 min limit for a notebook
+{'encoding': 17.4, 'maintenance': 32.0} s for one split
+fig3d needs 100 splits: about 82 min; fig3h adds two half-maintenance fits per split, about 53 min more (each half is half the bins); together about 136 min, over the 60 min limit for a notebook
== cell 86 ['claim:fig5gh-burst-index-cv2'] 4 changed lines
+reading (b) types, session ISIs:
+  burst_royer: PY mean 5.561 median 0.947; IN mean 0.693 median 0.622; p = 4.98e-03
+  cv_isi: PY mean 1.796 median 1.593; IN mean 1.711 median 1.322; p = 1.07e-04
+  cv2_holt: PY mean 1.180 median 1.176; IN mean 0.932 median 0.952; p = 1.62e-35
== cell 149 None 2 changed lines
-notebook ran in 17.2 min
+notebook ran in 19.4 min
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s,indent=0)[:6000])
EOF
```

```
{
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "One attempt at reproducing the claims of a target",
"description": "Draft. To be revised after the pilot. An attempt is recorded whether or not it produced a working notebook.",
"type": "object",
"additionalProperties": false,
"required": [
"schema_version",
"id",
"datasets",
"paper",
"date",
"provenance",
"outcomes"
],
"properties": {
"schema_version": {
"const": 3
},
"id": {
[... 271 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
o=s['properties']['outcomes']['items']['properties']
for k in o:
    if k not in ('claim','outcome','blocked_by','notes','notebook','output','measured'): print(k, json.dumps(o[k])[:300])
for k in s['properties']:
    if k not in ('schema_version','id','datasets','missing_datasets','paper','date','entry','deprecated','provenance','outcomes'): print('TOP',k, json.dumps(s['properties'][k])[:500])
EOF
```

```
deviations {"description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.", "type": "array", "items": {"type": "string", "minLength": 1}}
assumed {"description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says what was assumed and why (docs/protocol.md, Author, step 1.6).", "type": "boolean"}
proposed {"description": "A change of outcome found after the last verification round, held until a further round agrees with it.", "type": "object", "additionalProperties": false, "required": ["outcome", "reason"], "properties": {"outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "
TOP verifications {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["date", "kind", "by", "results"], "properties": {"date": {"type": "string", "format": "date"}, "kind": {"enum": ["agent", "person", "paper_author"]}, "by": {"type": "string"}, "results": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["claim", "agrees"], "properties": {"claim": {"type": "string"}, "agrees": {"type": "boolean"}, "reason": {"description": "The verifie
TOP findings {"description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}, "statement": {"type": "st
TOP reconciliation {"description": "A repeat attempt's comparison with the attempt before it, written by the reconcile step once this attempt, made blind, has been verified (docs/protocol.md, \"Repeat a
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  python - <<'EOF'
s=open('entries/kussovska-2025/reproduce_kussovska_2025.ipynb').read()
import nbformat
for path in ['entries/kussovska-2025/reproduce_kussovska_2025.ipynb','executed/kussovska-2025/reproduce_kussovska_2025.ipynb']:
    nb=nbformat.read(path,4)
    for c in nb.cells:
        if c.cell_type=='markdown' and c.source.startswith('**Result: blocked (too large).**'):
            c.source='''**Result: blocked (too large).** One split takes about 45 to 50 s (printed above: encoding plus
maintenance), so the 100 splits of fig3d take well over an hour, beyond the sixty-minute limit for
a notebook, and fig3h (about 50 min more) and fig3abc (which uses the same fits) add to it. The
three claims are not tested.'''
    nbformat.write(nb,path)
print('ok')
EOF
grep -n "too large" $TMPDIR/nb_part5.py | head -3
```

```
Tue Nov 10 08:00:46 UTC 2026
ok
58:**Result: blocked (too large).** One split takes about 45 s (15.4 s encoding, 29.9 s
```

**Agent calls Bash**

```bash
cd $TMPDIR; python - <<'EOF'
s=open('nb_part5.py').read()
a=s.index('**Result: blocked (too large).**'); b=s.index('""")',a)
s=s[:a]+'''**Result: blocked (too large).** One split takes about 45 to 50 s (printed above: encoding plus
maintenance), so the 100 splits of fig3d take well over an hour, beyond the sixty-minute limit for
a notebook, and fig3h (about 50 min more) and fig3abc (which uses the same fits) add to it. The
three claims are not tested.
'''+s[b:]
open('nb_part5.py','w').write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/make_attempt.py",
 "content": "import yaml\n\nNB = \"reproduce_kussovska_2025.ipynb\"\nTYPES_A = (\"Cell types and ACG groups downstream use reading (a) of acg-fit-yield (every spike of the unit), \"\n           \"assumed because the code's shipped Cell_metrics.xlsx equals it in firing rate and ISI CV and agrees within 1% in \"\n           \"normalised mean ACG and burst index for 99% of neurons; the ACG fit is a scipy port of the MATLAB fit, so the \"\n           \"types (102 PY, 215 IN) differ from the paper's 92 and 202.\")\nCC_SEED = (\"Concept cells are the code's bootstrap (reading b of concept-cells-count) with seed 0, a standard choice since the \"\n           \"code sets no seed; 57 of its 58 cells are in the code's shipped list.\")\nCODE_TABLE = (\"The identity-matched trials are the code's data/new_trial_final.xlsx (an outside input the criterion names); \"\n              \"the Methods do not say how they were chosen.\")\nBURST = (\"Wilcoxon tests against the Poisson null use the code's settings (zero_method pratt, asymptotic; \"\n         \"main_4c,d,6a,b.py:440); epoch comparisons the code's defaults (zero_method wilcox).\")\n\n\ndef o(claim, outcome, notes, deviations=None, measured=None, assumed=None, blocked_by=None, tag=None):\n    d = {\"claim\": claim, \"outcome\": outcome}\n    if blocked_by:\n        d[\"blocked_by\"] = blocked_by\n    d[\"notebook\"] = NB\n    d[\"output\"] = f\"claim:{tag or claim}\"\n    if measured is not None:\n        d[\"measured\"] = measured\n    if assumed:\n        d[\"assumed\"] = True\n    d[\"notes\"] = notes\n    if deviations:\n        d[\"deviations\"] = deviations\n    return d\n\n\noutcomes = [\n    o(\"units-by-region\", \"reproduced\", \"21 patients and 902 units; AMY 259, dACC 171, HPC 190, preSMA 250 and vmPFC 32, \"\n      \"exactly the paper's counts, left and right labels merged.\", measured=[902, 259, 171, 190, 250, 32, 21]),\n    o(\"behavior-accuracy\", \"reproduced\", \"Mean over 21 participants 88.73%, s.e.m. 1.25 (s.d. 5.74); pooled over 2673 trials 88.70%.\",\n      measured=88.73),\n    o(\"fig1c-accuracy-load1-vs-load3\", \"reproduced\", \"Median accuracy 94.44% at load 1 and 86.67% at load 3; rank-sum U = 324.5, \"\n      \"p = 0.0090 raw and 0.0270 with the code's Bonferroni factor (the paper's P = 0.027). Kruskal-Wallis over loads p = 0.022. \"\n      \"Paired variant p = 0.0042, load 1 higher in 17 of 21.\"),\n    o(\"behavior-rt\", \"reproduced\", \"Correct-trial RT under reading (a) 1.120 s (s.d. 0.252), (b) 1.348 s, (c) 1.097 s (half-IQR 0.297). \"\n      \"Readings (a) and (c) are within 0.78 to 1.34 s; (b) is just outside.\", measured=1.12),\n    o(\"rt-in-vs-out-memory\", \"reproduced\", \"Correct trials, median RT 1.041 s in memory against 1.184 s not in memory, faster in 17 \"\n      \"of 21 participants; sign-flip p = 0.001 and pooled label permutation p = 0.001; on all trials p = 0.002 for both.\"),\n    o(\"rt-correct-vs-incorrect\", \"reproduced\", \"Median RT 1.084 s correct against 1.503 s incorrect, correct faster in 20 of 21 \"\n      \"participants; p = 0.001 under both readings.\"),\n    o(\"fig1e-load-modulated-neurons\", \"reproduced\", \"Reading (a) with the code's shared permutation gives preSMA 20.40% (p = 0.000), \"\n      \"vmPFC 18.75% (p = 0.009), dACC 10.53% (p = 0.025), all within tolerance; the within-participant permutation gives 19.20%, \"\n      \"18.75%, 9.94% (p 0.000 to 0.018). With all trials (reading b) 22.80%, 21.88% and 12.87%, all significant. AMY and HPC are \"\n      \"not significant under any reading.\", measured=[20.4, 18.75, 10.53],\n      deviations=[\"The GLM is fitted by Newton's method in place of sklearn's PoissonRegressor; the largest slope difference over \"\n                  \"21 checked neurons is 1.1e-04.\",\n                  \"The code's p is the fraction of null counts at or above the observed count without + 1, so p = 0.000 is printed \"\n                  \"where the paper gives 0.001.\"]),\n    o(\"fig1f-rt-modulation-not-significant\", \"not_reproduced\", \"With each trial's own RT (the criterion's main analysis) the \"\n      \"BH-corrected count test is significant for preSMA (p_BH 0.000), AMY (0.048) and dACC (0.048) under reading (a) with the \"\n      \"shared permutation, and for four regions with all trials; percentages AMY 8.88%, preSMA 17.20%, vmPFC 6.25%. The code's \"\n      \"predictor, subject 1's RT vector applied to every neuron, gives AMY 5.79%, preSMA 8.00% and vmPFC 6.25%, the paper's three \"\n      \"values exactly, and no region significant after correction (smallest p_BH 0.40), so the paper's numbers come from that \"\n      \"predictor.\", measured=[8.88, 17.2, 6.25]),\n    o(\"concept-cells-count\", \"reproduced\", \"Code's bootstrap (reading b), ten seeds: 57 to 60 concept cells, AMY 70.18 to 72.41%, \"\n      \"HPC 17.24 to 19.30%, all within tolerance; seed 0 gives 58 with AMY 70.69%, HPC 18.97%, dACC 1.72%, preSMA 3.45%, vmPFC \"\n      \"5.17%. The Methods' bootstrap (reading a) gives 49 to 54, within tolerance for two seeds. Per participant 4.14 +/- 3.66 \"\n      \"over the 14 with a concept cell. Measured values are reading (b), seed 0, the reading that matches for every seed.\",\n      measured=[58, 70.69, 18.97], deviations=[CC_SEED]),\n    o(\"fig2ab-single-cells-not-persistent\", \"reproduced\", \"Of 58 concept cells, 8 are persistent under reading (a) (significant in \"\n      \"at least half the 50 ms bins) and 10 under reading (b) (each 1 s window); 50 and 48 are not. With a 25% bin threshold 19 \"\n      \"are persistent.\", deviations=[CC_SEED, \"The permutation test per bin uses 1,000 shuffles of the preferred labels; the Fig. \"\n                                     \"2a legend names a permutation test without a number.\"]),\n    o(\"fig2c-population-persistence\", \"reproduced\", \"Load 1, mean z 0.761 on preferred and -0.013 on nonpreferred trials; preferred \"\n      \"above nonpreferred in every maintenance bin and every bin significant after BH over all panels (and per panel), so both \"\n      \"readings hold.\", deviations=[CC_SEED]),\n    o(\"ext1bc-persistence-by-load\", \"reproduced\", \"Fraction of significant maintenance bins 1.00 at load 1, 1.00 at load 2 and 0.60 at \"\n      \"load 3; mean preferred minus nonpreferred difference 0.774, 0.487 and 0.325 z.\", deviations=[CC_SEED]),\n    o(\"fig2d-cross-temporal-localized\", \"reproduced\", \"290 significant train-test pairs; 17 training bins in encoding or early \"\n      \"maintenance have off-diagonal pairs kept by either cluster rule and either sidedness; no maintenance training bin \"\n      \"generalizes to more than 0.18 of the maintenance test bins. The 1,000 shuffled maps had no supra-threshold cluster, so the \"\n      \"Methods' rule removes nothing.\", deviations=[CC_SEED, CODE_TABLE,\n      \"The cluster extent of the Methods' rule is taken as the longer side of a cluster's bounding box in bins, a choice of this \"\n      \"attempt; the null is empty, so the choice cannot change the outcome.\",\n      \"The one-sided binomial p is P(X >= k); the code computes 1 - cdf(k), which excludes k.\"]),\n    o(\"ext1de-cross-temporal-load23\", \"reproduced\", \"Off-diagonal pairs kept, load 1 217 to 280; load 2 6 to 10; load 3 none; under \"\n      \"both labels (first, last) and every rule.\", deviations=[CC_SEED, CODE_TABLE]),\n    o(\"fig2e-maintenance-decoding-amy-mtl\", \"reproduced\", \"Load 1, at least three cells: AMY 35.63% (7 participants), MTL 33.61% \"\n      \"(8), p = 0.001 for both (BH 0.0015); more than three cells: AMY 34.33%, MTL 32.89% (5 each), p = 0.001. Null means near 18%.\",\n      measured=[35.63, 33.61], deviations=[CC_SEED, \"Features are z-scored with fixation as in main_2e,supp_1f.py:119-122; BH is over \"\n                                           \"the code's six region groups, of which dACC, preSMA and their union have no participant.\"]),\n    o(\"ext1f-maintenance-decoding-load2\", \"partially_reproduced\", \"Load 2: AMY 26.43% and MTL 26.67% (at least three cells), 27.89% \"\n      \"and 29.56% (more than three), p = 0.002 for all. The MTL accuracies are within tolerance; the AMY accuracies are above \"\n      \"the tolerance of 21.2 to 25.9%, so information is present in both but the AMY value is higher than the paper's.\",\n      measured=[26.43, 26.67], deviations=[CC_SEED]),\n    o(\"fig2f-bin-width-decoding\", \"partially_reproduced\", \"Load 1, code's table (reading a) 30.00, 60.00, 66.67, 76.67% and reading \"\n      \"(b) 50.00, 66.67, 73.33, 76.67%, all above chance (BH p at most 0.009) and rising from 250 to 1000 ms. Under (a) the 250 ms \"\n      \"value is below its tolerance (36 to 44%); under (b) 250 and 500 ms are above theirs. Twenty random draws of six trials \"\n      \"per image give 56.7 to 86.7% at 1000 ms.\", measured=[30.0, 60.0, 66.67, 76.67], deviations=[CC_SEED, CODE_TABLE,\n      \"The SVM is libsvm through sklearn's wrapper on a precomputed linear kernel, checked equal to SVC(kernel='linear') in every \"\n      \"LOOCV prediction under both trial readings.\"]),\n    o(\"fig2f-bin-width-pairwise\", \"not_reproduced\", \"Code's table: 750 vs 250 and 1000 vs 250 significant (BH p 0.006 and 0.002), \"\n      \"1000 vs 500 not (0.079, 0.139), 500 vs 250 significant (0.010, 0.002). Reading (b): 750 vs 250 and 1000 vs 250 significant \"\n      \"(BH p 0.036 to 0.048), 1000 vs 500 not (0.363, 0.483), and the three pairs the paper finds not significant are not. Under \"\n      \"no reading are the three named pairs significant.\", deviations=[CC_SEED, CODE_TABLE]),\n    o(\"ext1g-bin-width-load2\", \"reproduced\", \"Load 2 accuracies 28.0, 20.0, 28.0, 36.0% (code's table; range 16.0 points) and 20.0, \"\n      \"24.0, 20.0, 24.0% (reading b; range 4.0), below the 20-point threshold, and each below load 1 at the same width.\",\n      deviations=[CC_SEED, CODE_TABLE]),\n    o(\"fig3abc-trajectory-complexity\", \"blocked\", \"Uses the dPCA fits of fig3d, which are too large to run (see \"\n      \"fig3d-encoding-vs-maintenance-separability).\", blocked_by=\"too_large\", tag=\"fig3d-encoding-vs-maintenance-separability\"),\n    o(\"fig3d-encoding-vs-maintenance-separability\", \"blocked\", \"One split of the claim's design on the data (58 concept cells, \"\n      \"2 ms bins, regularization by dPCA's cross-validation per fit as the code does) took 15.4 s for encoding and 29.9 s for \"\n      \"maintenance in development and 17.4 and 32.0 s in the entry's run, so 100 splits take about 75 to 82 min, over the \"\n      \"60-minute notebook limit. Not run.\", blocked_by=\"too_large\"),\n    o(\"fig3h-early-vs-late-maintenance\", \"blocked\", \"Adds two half-maintenance dPCA fits to each of the 100 splits, about 50 min more \"\n      \"than fig3d; too large to run.\", blocked_by=\"too_large\", tag=\"fig3d-encoding-vs-maintenance-separability\"),\n    o(\"fig4c-encoding-bursts-vs-poisson\", \"reproduced\", \"Under the Methods' groups with the height rule and the real threshold, all \"\n      \"neurons (W = 14, BH p 0.0054) and low ACG (W = 7, 0.0483) differ from the Poisson null and the other four groups do not \"\n      \"(BH p 0.67 to 0.89). Under the code's groups with the prominence rule all neurons and low ACG differ but concept cells do \"\n      \"too (BH p 0.045); with the Methods' groups and prominence every group but concept cells differs; with the code's groups and \"\n      \"the height rule low ACG does not differ. The outcome rests on one named reading.\", assumed=True,\n      deviations=[TYPES_A, CC_SEED, BURST, \"Surrogates use stable per-group seeds; the code's 100 surrogates are kept.\"]),\n    o(\"fig4d-maintenance-bursts-vs-poisson\", \"reproduced\", \"Under the real-threshold readings the five named groups exceed the null \"\n      \"in most participants (code's groups, prominence: all 20 of 20, BH p 0.0007; low ACG 11 of 12; high, short, long BH p \"\n      \"0.0035 to 0.0042) and concept cells do not (BH p 0.11). Each surrogate's own threshold breaks the pattern. With each \"\n      \"trial's own maintenance length, short tau decay is not significant (BH p 0.11).\", assumed=True,\n      deviations=[TYPES_A, CC_SEED, BURST]),\n    o(\"fig4-acg-group-differences\", \"partially_reproduced\", \"Prominence rule: low ACG bursts more than high ACG in encoding and \"\n      \"maintenance in 12 of 12 participants (p = 0.0005, BH over 28 pairs at most 0.0017), and short and long tau decay do not \"\n      \"differ in maintenance (p 0.81 to 0.87); short tau decay does not exceed long tau decay in encoding (p 0.14 code groups, \"\n      \"0.086 Methods groups). Height rule: low ACG bursts less than high ACG.\", assumed=True, deviations=[TYPES_A]),\n    o(\"fig4f-all-cells-epochs\", \"partially_reproduced\", \"All 902 neurons, prominence rule: encoding median 6 bursts against 14 to 17 \"\n      \"in M1 to M3, BH p 0.0003 to 0.035 under both window readings; probe 5.5, BH p 0.61 to 0.71, no increase under any reading. \"\n      \"The well-fit population gives the same for M1 and M2. Three of the four comparisons hold.\", assumed=True,\n      deviations=[TYPES_A, \"The code's M1 to M3 (reading b) are thirds of the whole concatenated train, which are thirds of the \"\n                  \"trials, not of the maintenance period (main_4f-k,6c,d.py:216-219).\"]),\n    o(\"fig4hj-group-epochs\", \"partially_reproduced\", \"Prominence rule with the code's thirds: long tau decay up from encoding at M1, \"\n      \"M2 and M3 (BH p 0.002 to 0.019) and no significant pair for low ACG, short tau decay and concept cells; high ACG up at M1 \"\n      \"and M2 (BH p 0.002 to 0.010) but not at the probe (0.24 to 0.38). The increases hold for one of the two groups.\",\n      assumed=True, deviations=[TYPES_A, CC_SEED]),\n    o(\"ext2-bursts-loads23\", \"reproduced\", \"With the Methods' groups, prominence rule and the code's thirds, all cells, high ACG and \"\n      \"long tau decay have more bursts in each maintenance window than in encoding (median over participants) at loads 2 and 3. \"\n      \"With the code's groups long tau decay does not at loads 2 and 3; with the height rule the pattern does not hold.\",\n      assumed=True, deviations=[TYPES_A]),\n    o(\"acg-fit-yield\", \"reproduced\", \"317 neurons with R2 > 0.3 when all spikes are used (reading a) and 298 with spikes within trials \"\n      \"(reading b); R2 >= 0.3 gives the same. The firing rate and ISI CV equal the code's shipped table, and normalised mean ACG \"\n      \"and burst index agree within 1% for 99% of neurons; the fitted R2 agrees within 1% for 48% of neurons and the threshold \"\n      \"classification for 97.5%.\", measured=317,\n      deviations=[\"The CellExplorer fit is run with scipy's trust-region reflective least squares in place of MATLAB's fit, from \"\n                  \"the same start point and bounds; local optima differ for part of the neurons.\"]),\n    o(\"fig5c-cell-type-clusters\", \"reproduced\", \"Reading (b): PY 100, IN 198, both within tolerance. Reading (a): PY 102 (just above \"\n      \"101.2), IN 215. The same clustering on the code's shipped features gives exactly 92 and 202.\", measured=[100, 198],\n      deviations=[\"The cluster with the higher median firing rate is labelled IN (Results); the code fixes label 1 as PY, which \"\n                  \"gives the same 92 on its shipped features.\"]),\n    o(\"fig5dfh-cluster-features\", \"reproduced\", \"IN higher on firing rate, normalised mean ACG and tau_rise under both readings, \"\n      \"BY-corrected p at most 8e-05 (reading a U = 20822, 21885 and 14159).\"),\n    o(\"fig5gh-burst-index-cv2\", \"reproduced\", \"Types and burst index of reading (b), CV of each unit's session ISIs (the code's Fig. 5h \"\n      \"column): medians burst index PY 0.947 and IN 0.622, CV PY 1.593 and IN 1.322, all within tolerance, PY higher on both \"\n      \"(p = 0.005 and 1.1e-04). The paper's values match medians; the PY mean burst index is 5.6. Under reading (a) the PY \"\n      \"burst-index median is 0.802, outside tolerance, with BY-corrected p 0.11. Holt's CV2 gives PY 1.18 and IN 0.93.\",\n      measured=[0.947, 0.622, 1.593, 1.322]),\n    o(\"supp4-rodent-validation\", \"reproduced\", \"On the 343 ground-truth cells' features shipped with the paper's code (44 PY, 299 IN), \"\n      \"spectral clustering as in fig5c matches 333, misassigning one pyramidal neuron and nine interneurons, as reported. The \"\n      \"CellExplorer recordings themselves were not used.\", measured=333,\n      deviations=[\"Tested on the feature table data/cell_analysis/validation_data.xlsx of the paper's code, not on features \"\n                  \"computed from the CellExplorer recordings.\"]),\n    o(\"fig5kl-concept-cell-types\", \"reproduced\", \"Reading (b) types: 11 PY and 14 IN concept cells; median Royer burst index PY 0.949 \"\n      \"against IN 0.390, Holt CV2 1.217 against 0.991. Reading (a): 11 and 16, same ordering.\", measured=[11, 14],\n      deviations=[CC_SEED]),\n    o(\"fig6ab-celltype-bursts-vs-null\", \"partially_reproduced\", \"Poisson null, prominence rule: PY above the null in encoding (BH p \"\n      \"0.0089) and maintenance (0.0035), IN in maintenance (0.0012), but IN also in encoding (0.020), where the paper finds no \"\n      \"difference; with the height rule PY do not differ in encoding (BH p 0.09 to 0.11). Label-shuffled null: PY above it in \"\n      \"both epochs (BH p 0.0029, 0.0057), IN below it in encoding (0.0016) and not different in maintenance (0.063). No reading \"\n      \"gives the paper's full pattern; elevated PY bursting in both epochs and IN bursting in maintenance hold.\", assumed=True,\n      deviations=[TYPES_A, BURST, \"The label-shuffled null pools each participant's classified neurons (PY and IN) and keeps group \"\n                  \"sizes; the paper does not describe its shuffle.\"]),\n    o(\"fig6cd-celltype-epochs\", \"partially_reproduced\", \"Prominence rule with the code's thirds: PY have no pair with BH p < 0.05 at \"\n      \"loads 1, 2 and 3; IN burst more in M1, M2 and M3 than in encoding at load 1 (BH p 0.0047 to 0.014; medians 11 against 15) \"\n      \"but not at the probe (0.80). With the Methods' windows PY differ at every load.\", assumed=True, deviations=[TYPES_A]),\n    o(\"ext5bd-in-load-dependence\", \"reproduced\", \"With the prominence rule and the code's thirds the IN measure is 3.67, 5.00 and 6.33 \"\n      \"at loads 1 to 3, rising; under the height rule or the Methods' windows it does not rise.\", assumed=True,\n      deviations=[TYPES_A]),\n    o(\"fig6e-load-modulation-in\", \"partially_reproduced\", \"Matched trials, shared permutation: IN 13.95% (30 of 215, p = 0.001), \"\n      \"within tolerance; IN concept 18.75% (3 of 16, p = 0.042), below the tolerance of 19.3 to 23.6% (the paper's 21.42% is 3 \"\n      \"of 14); PY 5.88% (p = 0.43) and PY concept 0% (p = 1.0) not significant. With reading (b) types, IN 14.65% (p = 0.001) and \"\n      \"IN concept 14.29% (p = 0.15).\", measured=[13.95, 18.75, 5.88, 0.0], assumed=True, deviations=[TYPES_A, CC_SEED]),\n    o(\"fig6f-rt-modulation-in-concept\", \"not_reproduced\", \"Own RT: IN concept 12.50% (p = 0.19) and PY significant (p 0.005 to 0.024). \"\n      \"The code's predictor (subject 1's RT vector) gives IN concept 31.25% (p = 0.001), just below the tolerance, with IN (p = \"\n      \"0.086) and PY (0.40) not significant.\", measured=12.5, assumed=True, deviations=[TYPES_A, CC_SEED]),\n    o(\"fig6gh-in-concept-cv2\", \"not_reproduced\", \"IN concept cells, preferred trials, CV2 median 0.964 in encoding and 0.969 in \"\n      \"maintenance at load 1 (W = 64, p = 0.86), and 0.969 against 1.005 over all loads (W = 38, p = 0.13). IN nonpreferred and \"\n      \"every PY comparison have p > 0.05.\", assumed=True, deviations=[TYPES_A, CC_SEED,\n      \"Trials are concatenated with a stride of the window (1 s encoding, 2.5 s maintenance), so interspike intervals cross \"\n      \"trial boundaries, as a plain concatenation of the code's spike lists would.\"]),\n    o(\"ext5gh-py-decay-preferred\", \"not_reproduced\", \"PY concept cells, tau_decay preferred against nonpreferred: load 1 encoding \"\n      \"13.38 against 12.25 ms (p = 0.73), maintenance 17.20 against 10.30 (p = 0.32); all loads p = 0.43 and 0.13 (paired t p = \"\n      \"0.050 in maintenance). IN p 0.058 to 0.67. Preferred-trial spikes per PY cell have a median of 25 to 34 at load 1.\",\n      assumed=True, deviations=[TYPES_A, CC_SEED, \"The decay time constant is the ACG tau_decay fitted to the spikes of each trial \"\n                                \"type and epoch, the claims file's reading; the paper does not define it.\"]),\n    o(\"fig6i-py-bin-width-decoding\", \"not_reproduced\", \"11 PY concept cells, code's table: 33.33, 23.33, 36.67 and 43.33%, BH p 0.072, \"\n      \"0.39, 0.072 and 0.060, so 750 and 1000 ms are not significant; reading (b): 33.33, 33.33, 23.33, 23.33%.\",\n      measured=[33.33, 23.33, 36.67, 43.33], assumed=True, deviations=[TYPES_A, CC_SEED, CODE_TABLE]),\n    o(\"fig6j-in-bin-width-decoding\", \"partially_reproduced\", \"16 IN concept cells, code's table 46.67, 53.33, 53.33, 50.00% and reading \"\n      \"(b) 50.00, 63.33, 56.67, 53.33%, all with BH p 0.002; two of four values are outside tolerance under each reading.\",\n      measured=[46.67, 53.33, 53.33, 50.0], assumed=True, deviations=[TYPES_A, CC_SEED, CODE_TABLE]),\n    o(\"fig6kl-cross-temporal-by-type\", \"reproduced\", \"PY concept map, no significant pair under any reading; IN concept map, 240 \"\n      \"significant pairs and 162 to 230 off-diagonal pairs kept, 18 training bins in encoding or early maintenance.\",\n      assumed=True, deviations=[TYPES_A, CC_SEED, CODE_TABLE]),\n    o(\"ext5ij-load2-decoding-by-type\", \"reproduced\", \"Load 2, IN concept cells above chance at all four widths under both readings \"\n      \"(BH p at most 0.013); PY concept cells at none (BH p at least 0.49).\", assumed=True,\n      deviations=[TYPES_A, CC_SEED, CODE_TABLE]),\n]\n\nfindings = [\n    {\"kind\": \"code_mismatch\", \"statement\": \"The paper's GLM code (01_task/main_1e,f.py:9 and 113) uses subject 1's reaction times as \"\n     \"the predictor for every neuron of every participant. The RT-modulation percentages of Fig. 1f (AMY 5.79%, preSMA 8.00%, \"\n     \"vmPFC 6.25%) are reproduced exactly only with that predictor; with each trial's own reaction time preSMA, AMY and dACC have \"\n     \"significant proportions of RT-modulated neurons after correction.\"},\n    {\"kind\": \"selection_undocumented\", \"statement\": \"The matched trial sets of the Methods (96 load-matched and 75 identity-matched \"\n     \"trials per participant) exist only as the code's tables data/new_trial_info.xlsx and data/new_trial_final.xlsx; no script \"\n     \"builds them and the paper does not say how they were chosen. Pseudo-population decoding accuracies depend on which trials \"\n     \"enter (random draws of six trials per image give 56.7 to 86.7% at 1000 ms against 76.67% with the code's table).\"},\n    {\"kind\": \"other\", \"statement\": \"The paper states that sixteen participants completed 135 trials and five completed 108; the \"\n     \"dandiset has fifteen sessions of 135 trials and six of 108 (subjects 6, 7, 8, 9, 16 and 19).\"},\n    {\"kind\": \"metadata_error\", \"statement\": \"In sub-9's Sternberg file one trial (row 29) has timestamps_Maintenance equal to \"\n     \"timestamps_Probe, a maintenance of 0 s, against 2.53 to 2.84 s in every other trial.\"},\n    {\"kind\": \"other\", \"statement\": \"The duration of the first encoding image differs by session, 1.0, 1.2, 1.5 or 2.5 s (from \"\n     \"timestamps_Encoding1 to timestamps_Encoding1_end), which the paper does not state; its analyses use a 1 s encoding window. \"\n     \"Fixation lasts about 0.91 to 1.2 s in most sessions, with single longer fixations up to 14.07 s, where the paper gives 0.9 \"\n     \"to 1.0 s.\"},\n    {\"kind\": \"code_mismatch\", \"statement\": \"The code's epoch burst analysis (04_bursting/main_4f-k,6c,d.py:216-219) assigns \"\n     \"maintenance bursts to M1, M2 and M3 by thirds of the whole concatenated train, that is by thirds of the trials, while the \"\n     \"Methods define three consecutive 1 s windows from maintenance onset. The burst counts per window differ between the two.\"},\n    {\"kind\": \"code_mismatch\", \"statement\": \"The column the code reports as CV2 for Fig. 5h (02_trial_info.py:42-46) is the plain \"\n     \"coefficient of variation of the interspike intervals, not Holt's local CV2 that the Methods cite; the paper's values \"\n     \"(PY 1.673, IN 1.319) match the plain CV.\"},\n    {\"kind\": \"methods_unavailable\", \"statement\": \"Question for the authors: which peak rule detects population bursts, a smoothed \"\n     \"value above the 90th percentile (Methods) or a prominence at or above it (Results and code), and what are the threshold \"\n     \"of the surrogates and the minimum spacing (140 ms in the Methods, 70 ms in the Results)? Fig. 4c is reproduced under the \"\n     \"Methods' height rule with the Methods' groups, and fails narrowly under the code's prominence rule, where concept cells \"\n     \"also differ from the null.\"},\n    {\"kind\": \"methods_unavailable\", \"statement\": \"Question for the authors: what is the 'label-shuffled null' of Fig. 6a,b, whose \"\n     \"legend names rate-matched Poisson surrogates? Under the Poisson null interneurons exceed the null in encoding, and under \"\n     \"a shuffle of cell-type labels within participant they fall below it.\"},\n    {\"kind\": \"methods_unavailable\", \"statement\": \"Question for the authors: which decay time constants are compared between preferred \"\n     \"and nonpreferred trials in Extended Data Fig. 5g,h? The code reads them from a shipped table \"\n     \"(decay_constant_change.xlsx) that no script computes; ACG tau_decay per trial type shows no effect here.\"},\n    {\"kind\": \"methods_unavailable\", \"statement\": \"Question for the authors: how is the 'temporal extent' of a cross-temporal cluster \"\n     \"measured for the 1,000-shuffle cluster-duration null, and is the binomial test one- or two-sided (Methods, Population \"\n     \"decoding, says two-sided; Statistical analyses and the code, one-sided)? Here the shuffled maps had no cluster, so the \"\n     \"choice did not matter.\"},\n    {\"kind\": \"other\", \"statement\": \"The ACG features of the code's shipped Cell_metrics.xlsx (firing rate, normalised mean ACG, \"\n     \"burst index, ISI CV) are recomputed from the dandiset's spike times to within 1% for 99% of units, using every spike of the \"\n     \"unit; the fitted R2 and time constants come from MATLAB's optimizer and differ for part of the units in a scipy port, \"\n     \"which gives 317 well-fit units in place of 294.\"},\n]\n\nrec = {\n    \"schema_version\": 3,\n    \"id\": \"kussovska-2025-01\",\n    \"datasets\": [{\"archive\": \"dandi\", \"id\": \"000469\", \"version\": \"0.231213.2047\",\n                  \"doi\": \"10.48324/dandi.000469/0.231213.2047\", \"relation\": \"reuses\"}],\n    \"paper\": \"doi:10.1101/2025.10.31.684900\",\n    \"date\": \"2026-11-10\",\n    \"entry\": \"kussovska-2025\",\n    \"provenance\": {\"kind\": \"agent\", \"accountable\": {\"name\": \"CatalystNeuro\"},\n                   \"agent\": {\"harness\": \"Claude Code\", \"model\": \"claude-opus-5-5\", \"protocol\": \"pilot-14\"},\n                   \"runner\": {\"platform\": \"GitHub Actions\",\n                              \"url\": \"https://github.com/catalystneuro/encore/actions/runs/42760373832\"}},\n    \"inputs\": [\n        {\"what\": \"The code's matched trial tables data/new_trial_info.xlsx (96 load-matched trials, GLM reading a) and \"\n                 \"data/new_trial_final.xlsx (75 identity-matched trials, pseudo-population reading a), read over HTTP.\",\n         \"source\": \"https://github.com/dariakussovska/heterogeneitywm at commit 5144fe80876d14e8aacb4044977c3474c454f14b\"},\n        {\"what\": \"The code's concept-cell list (data/all_neuron_brain_regions_cleaned.xlsx) and ACG feature table \"\n                 \"(data/cell_analysis/Cell_metrics.xlsx), used for comparison only; no outcome rests on them.\",\n         \"source\": \"https://github.com/dariakussovska/heterogeneitywm at commit 5144fe80876d14e8aacb4044977c3474c454f14b\"},\n        {\"what\": \"Features of the CellExplorer ground-truth cells (data/cell_analysis/validation_data.xlsx), for \"\n                 \"supp4-rodent-validation (data elsewhere).\",\n         \"source\": \"https://github.com/dariakussovska/heterogeneitywm at commit 5144fe80876d14e8aacb4044977c3474c454f14b\"},\n    ],\n    \"outcomes\": outcomes,\n    \"findings\": findings,\n}\nwith open(\"attempts/kussovska-2025-01.yaml\", \"w\") as f:\n    yaml.safe_dump(rec, f, sort_keys=False, width=100, allow_unicode=True)\nprint(len(outcomes), \"outcomes\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/make_attempt.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python $TMPDIR/make_attempt.py && grep -n ": .*: " attempts/kussovska-2025-01.yaml | grep -v "^\s*[0-9]*:\s*-\? *[a-z_]*: ['\"]" | head; cat > entries/kussovska-2025/README.md <<'EOF'
# Kussovska, Kim & Rungratsameetaweemana (2025) from dandiset 000469

Tests the findings of [Kussovska et al. (2025)](https://doi.org/10.1101/2025.10.31.684900) on
[DANDI:000469](https://dandiarchive.org/dandiset/000469/0.231213.2047), the human single-neuron
recordings of Kyzar et al. (2024) during a Sternberg working memory task, which the paper reuses.

| Claims | Outcome |
|---|---|
| Units by region, behavior (accuracy, load effect, reaction times) | Reproduced (6) |
| Load-modulated neurons (Fig. 1e) | Reproduced |
| RT-modulated neurons not significant (Fig. 1f) | Not reproduced; the paper's values come from the code's use of subject 1's reaction times for every neuron |
| Concept cells, single-cell and population persistence, cross-temporal decoding | Reproduced (6) |
| Maintenance decoding within participant, load 1 / load 2 | Reproduced / partially reproduced |
| Bin-width decoding / pairwise comparisons / load 2 | Partially reproduced / not reproduced / reproduced |
| dPCA state-space analyses (Fig. 3) | Blocked: too large (3) |
| Population bursts against the Poisson null, encoding and maintenance; loads 2 and 3 | Reproduced (3) |
| Burst differences between ACG groups and across epochs (Fig. 4f-j) | Partially reproduced (3) |
| ACG fits, cell-type clusters and their features, rodent validation, concept cell types | Reproduced (6) |
| Cell-type bursting (Fig. 6a-d), IN load dependence | Partially reproduced (2), reproduced (1) |
| Load and RT modulation by cell type (Fig. 6e,f) | Partially reproduced / not reproduced |
| CV2 and decay constants of concept cells (Fig. 6g,h; Ext. Fig. 5g,h) | Not reproduced (2) |
| Bin-width decoding by cell type, cross-temporal by type, load 2 by type | Not reproduced (PY), partially reproduced (IN), reproduced (2) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's code (github.com/dariakussovska/heterogeneitywm, commit 5144fe8) supplies the
matched trial tables that several readings use and the features of the rodent validation set.
The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/kussovska-2025-01.yaml`](../../attempts/kussovska-2025-01.yaml).

- `reproduce_kussovska_2025.ipynb`: the analysis, about 20 minutes on four CPUs.
- `wm.py`: loading the Sternberg files, trial and spike helpers, the Poisson GLM, the concept-cell
  bootstrap, the linear SVM decoders, the CellExplorer ACG port, the burst detection and the
  neuron groups. Other notebooks on this dandiset can import it.
EOF
python tools/entry.py check entries/kussovska-2025 2>&1 | tail -8; date -u
```

```
45 outcomes
0 error(s)
Tue Nov 10 08:02:47 UTC 2026
```

**Agent calls Bash**

```bash
python -c "
import yaml
c=[x['id'] for x in yaml.safe_load(open('claims/kussovska-2025.yaml'))['claims']]
a=[x['claim'] for x in yaml.safe_load(open('attempts/kussovska-2025-01.yaml'))['outcomes']]
print(len(c),len(a),set(c)-set(a),set(a)-set(c))
from collections import Counter; print(Counter(x['outcome'] for x in yaml.safe_load(open('attempts/kussovska-2025-01.yaml'))['outcomes']))
"; grep -n "—\|rather" attempts/kussovska-2025-01.yaml entries/kussovska-2025/README.md entries/kussovska-2025/wm.py | head; python tools/entry.py handover entries/kussovska-2025 2>&1 | tail -5; ls executed/kussovska-2025/handover
```

```
45 45 set() set()
Counter({'reproduced': 27, 'partially_reproduced': 9, 'not_reproduced': 6, 'blocked': 3})
wrote executed/kussovska-2025/handover
kussovska-2025.yaml
reproduce_kussovska_2025.ipynb
wm.py
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import nbformat, re
for path in ['entries/kussovska-2025/reproduce_kussovska_2025.ipynb','executed/kussovska-2025/reproduce_kussovska_2025.ipynb']:
    nb=nbformat.read(path,4); n=0
    for c in nb.cells:
        if c.cell_type=='markdown':
            new=re.sub(r'\*\*(?!Result)([^*]+?)\*\*', r'\1', c.source)
            if new!=c.source: n+=1; c.source=new
            if 'rather' in c.source or '—' in c.source: print('WORD', path, c.source[:80])
        else:
            if 'rather' in c.source: print('code has rather', c.source[:60])
    nbformat.write(nb,path); print(path, n)
EOF
grep -c "rather\|—" entries/kussovska-2025/wm.py; for f in $TMPDIR/nb_part*.py; do python - "$f" <<'EOF'
import re,sys
p=sys.argv[1]; s=open(p).read(); s2=re.sub(r'\*\*(?!Result)([^*]+?)\*\*', r'\1', s); open(p,'w').write(s2)
EOF
done; python tools/entry.py handover entries/kussovska-2025 2>&1 | tail -1; python tools/entry.py check entries/kussovska-2025 | tail -1
```

```
entries/kussovska-2025/reproduce_kussovska_2025.ipynb 2
executed/kussovska-2025/reproduce_kussovska_2025.ipynb 2
0
wrote executed/kussovska-2025/handover
0 error(s)
```

**Agent calls Bash**

```bash
cd  rm -rf entries/kussovska-2025/__pycache__; git status --short; date -u
```

```
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? attempts/kussovska-2025-01.yaml
?? entries/kussovska-2025/
?? scripts
Tue Nov 10 08:03:26 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls -la .bashrc .mcp.json scripts .idea .vscode 2>&1 | head -20
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 10 05:10 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 10 05:10 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 10 05:10 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 10 05:10 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 10 05:10 scripts
```

**Agent**

I've finished steps 1 to 6 of the Author protocol for kussovska-2025. The entry passes `python tools/entry.py all` in a clean environment (0 errors, notebook ran in 19.6 min), and the handover is built in `executed/kussovska-2025/handover/`. Nothing is committed.

## 1. Outcomes (45 claims: 27 reproduced, 9 partially reproduced, 6 not reproduced, 3 blocked)

| Claim | Outcome |
|---|---|
| units-by-region, behavior-accuracy, fig1c-accuracy-load1-vs-load3, behavior-rt, rt-in-vs-out-memory, rt-correct-vs-incorrect | reproduced |
| fig1e-load-modulated-neurons | reproduced |
| fig1f-rt-modulation-not-significant | not reproduced |
| concept-cells-count, fig2ab, fig2c, ext1bc, fig2d, ext1de | reproduced |
| fig2e-maintenance-decoding-amy-mtl | reproduced |
| ext1f-maintenance-decoding-load2 | partially reproduced |
| fig2f-bin-width-decoding | partially reproduced |
| fig2f-bin-width-pairwise | not reproduced |
| ext1g-bin-width-load2 | reproduced |
| fig3abc, fig3d, fig3h (dPCA) | blocked, too_large (one split takes about 45 to 50 s, so 100 splits take about 75 to 82 min, over the 60 min limit) |
| fig4c, fig4d, ext2 | reproduced (each under one of the readings the criterion names; marked assumed) |
| fig4-acg-group-differences, fig4f, fig4hj | partially reproduced |
| acg-fit-yield, fig5c, fig5dfh, fig5gh, fig5kl | reproduced |
| supp4-rodent-validation | reproduced, using the feature table shipped with the paper's code (`data: elsewhere`) |
| fig6ab, fig6cd, fig6e, fig6j | partially reproduced |
| ext5bd, fig6kl, ext5ij | reproduced |
| fig6f, fig6gh, ext5gh, fig6i | not reproduced |

## 2. Dataset, assumptions, questions

**Version.** I pinned 0.231213.2047, the version the paper cites. All published versions hold the same 41 assets. The 21 Sternberg files hold exactly the paper's 902 units with its region counts. The code's trial tables link to the dataset's trials exactly.

**What was found:**
- The paper says 16 participants did 135 trials and 5 did 108. The data have 15 and 6.
- One trial in subject 9 has a maintenance of 0 s.
- The first encoding image lasts 1.0, 1.2, 1.5 or 2.5 s depending on the session; the paper does not say.
- Fixation runs about 0.91 to 1.2 s in most sessions, against the paper's 0.9 to 1.0 s.
- The Fig. 1f percentages come out exactly only with the code's predictor, which gives every neuron subject 1's reaction times. With each trial's own reaction time, three regions are significant, which is why that claim is not reproduced.
- The code splits maintenance into M1 to M3 by thirds of the trials, not by 1 s windows as the Methods say.
- What the code reports as CV2 is the plain coefficient of variation.
- The paper does not say how the matched trial sets were chosen.
- The clock could not be checked by contrast in 7 sessions (subjects 1, 3, 6, 10, 17, 19, 20), which have no image-selective neurons.

**Assumptions:**
- For cell types and ACG groups downstream, I used every spike of each unit (reading a of acg-fit-yield). The code's shipped table matches this exactly in firing rate and ISI CV. This was my choice, so dependent outcomes are marked assumed.
- Concept cells use the code's bootstrap with seed 0, a standard choice since the code sets no seed. This set shares 57 of 58 cells with the code's list.
- My Python port of the ACG fit gives 317 well-fit units against the paper's 294, and 102 pyramidal cells against 92.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which peak rule detects bursts, what threshold the surrogates use, and the spacing (70 or 140 ms).
- What the "label-shuffled null" of Fig. 6a,b is.
- Which decay constants are compared in Extended Data Fig. 5g,h.
- How cluster extent is measured, and whether the binomial test is one- or two-sided.

I asked a reader no questions.

## 3. Where the protocol was unclear
1. When a criterion only defines "reproduced" and the result holds in part, the protocol does not say how to judge it. I used the criterion's own partial clause where it has one (so fig2f-pairwise is not reproduced), and otherwise the general definition.
2. For `measured`, the first reading listed matched for only 2 of 10 seeds in concept-cells-count. I recorded the reading that matched for every seed, and said so.
3. When an upstream claim has several readings (which spikes feed the ACG), the protocol does not say whether downstream claims must run each one. I picked one, stated it as an assumption, and marked those outcomes assumed.
4. There is no category for outside inputs used only for comparison (the code's concept-cell list and ACG table). I listed them under `inputs` and said no outcome rests on them.
5. The example entry uses bold labels in its notebook header, but the instructions forbid bold. I removed them.
6. The protocol's advice to develop on a subset does not say to run the full notebook cell by cell with saved progress. Not doing so cost me a run (see 4).

## 4. Runtime and failures
- About 2 h 55 min in total. The final notebook takes 19.6 min.
- My first full development run was killed at 66 min with nothing saved. The cause was a slow two-sided binomial test in the cross-temporal shuffles; I replaced it with a lookup table and switched to a runner that saves after each cell.
- My fast SVM wrapper had a bug: it gave wrong predictions when labels were not coded 0 to k-1. I fixed it before the final run and checked it against sklearn under both trial readings. It had made the within-participant and rank-aligned decoding look below chance.

## End of run

106 turns, 166 minutes, $15.92 at API prices, result: success.
