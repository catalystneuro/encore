# memar-2026 · claims · run 44896998686

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls; ls paper claims tools | head -50; grep -n "^#" docs/protocol.md
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,200p docs/protocol.md; ls paper; ls paper/* | grep -i memar
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -l paper/*; cat claims/fouke-2025.yaml | head -150; cat papers/datasets/memar-2026.yaml 2>/dev/null; grep -n memar papers/keys.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.48550-arxiv.2606.11415.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls schemas; sed -n 1,60p tools/claims_check.py; ls -t claims | head -5
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
[... 49 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.48550-arxiv.2606.11415.txt",
 "offset": 1367
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I've read the full preprint (v1, with appendix tables II and III; there is no separate supplement). Next I'll read the linked code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/neurovium/SpatiallyMaskedRegression smr && cd smr && git log -1 --format='%H %ci' && find . -type f -not -path './.git/*' | head -100
```

```
244dcdbd67f217873c2a52b77485d97c6fa9bf0e 2026-06-24 16:49:51 -0400
./neighborhood.py
./test_hungarian.py
./visualize.py
./test_neighborhood.py
./verify_mask_intensity.py
./notebooks/visualization.ipynb
./notebooks/_helpers.py
./notebooks/README.md
./notebooks/visualize_sample_signals.ipynb
./test_similarity.py
./model.py
./run_coverage_experiment.py
./configs/device_path.example.yaml
./configs/device_path.yaml
./configs/settings.yaml
./utils.py
./LICENSE
./Test_new_subject_iEEG.py
./__pycache__/neighborhood.cpython-311.pyc
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/smr && wc -l *.py *.md configs/*.yaml && cat README.md METHODS.md configs/settings.yaml
```

```
<persisted-output>
Output too large (32.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/abd1218f-0f61-446a-9d85-b37661312f03/tool-results/b1g9kb1k4.txt

Preview (first 2KB):
   150 Load_preprocess_data.py
    87 ReconModel.py
   280 Test_new_subject_iEEG.py
   186 generate_adj_matrix_ieeg_unseen.py
    87 main.py
   163 model.py
   309 neighborhood.py
   174 path.py
   250 run_coverage_experiment.py
   249 setting.py
   222 similarity.py
    84 test_hungarian.py
   131 test_model_factory.py
   175 test_neighborhood.py
   112 test_similarity.py
   431 train.py
[... 32 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/abd1218f-0f61-446a-9d85-b37661312f03/tool-results/b1g9kb1k4.txt"
}
```

```
1	   150 Load_preprocess_data.py
2	    87 ReconModel.py
3	   280 Test_new_subject_iEEG.py
4	   186 generate_adj_matrix_ieeg_unseen.py
5	    87 main.py
6	   163 model.py
7	   309 neighborhood.py
8	   174 path.py
9	   250 run_coverage_experiment.py
10	   249 setting.py
11	   222 similarity.py
12	    84 test_hungarian.py
13	   131 test_model_factory.py
14	   175 test_neighborhood.py
15	   112 test_similarity.py
16	   431 train.py
17	   307 utils.py
18	   127 verify_mask_intensity.py
19	   212 visualize.py
20	   432 METHODS.md
[... 744 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/smr && cat utils.py Load_preprocess_data.py
```

```
"""
Miscellaneous helpers for the SMR pipeline.

Mask / neighborhood logic lives in ``fixed/neighborhood.py``. This module
contains:

    * Environment / reproducibility setup (``configure_environment``).
    * Settings serialisation (``save_settings_to_json``).
    * iEEG preprocessing (``preprocess_iEEG``) used by the Dandiset path.
    * Trial epoching utilities for raw ECoG.
    * Dandiset extraction (``extract_data_dandi``).

The legacy ``find_index_mask_eeg`` / ``find_index_mask_ieeg`` and
``nearest_neighbors`` helpers from ``new/utils.py`` were intentionally
removed: their job is now done by ``fixed/neighborhood.py``.
"""

from __future__ import annotations

import json
[... 438 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/smr && cat neighborhood.py main.py && sed -n 1,140p setting.py | grep -n "def \|fs\|return" | head -60
```

```
"""
Unified neighborhood / spatial-mask utilities for the SMR pipeline.

This module exposes a single entry point, ``find_index_mask``, that supports
both neighborhood-definition strategies used in the project so far:

    method='atlas'   -- the strategy described in the manuscript:
                          * EEG : adjacency in the standardized 10-10 / 10-5
                                  montage, encoded as fixed regional groups
                                  (matches `gihub_repo/utils.py`).
                          * iEEG: anatomical proximity from the AAL atlas,
                                  encoded as channels sharing the same
                                  anatomical label as the target.
    method='knn'     -- the strategy implemented in `new/utils.py`:
                          * The k channels closest to the target in projected
                            Euclidean coordinate space (x,y for EEG, x,z for
                            iEEG).

Either strategy returns a *neighborhood set* N(i) which is then passed
through a uniform `mask_intensity` knob, so the masking semantics described
[... 396 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/smr && cat notebooks/README.md && cat notebooks/_helpers.py | head -150 && python3 -c "
import json;nb=json.load(open('notebooks/visualization.ipynb'))
for c in nb['cells']:
    print('-----',c['cell_type']);print(''.join(c['source']))
"
```

```
# `fixed/notebooks/` — replication notebooks

Two Jupyter notebooks reproduce the figures in the paper using outputs
of the `fixed/` package:

* `visualization.ipynb` — Figures **2, 4, 6**
  (per-subject intra/cross/surrogate bars, mask-intensity sweep,
  electrode coverage).
* `visualize_sample_signals.ipynb` — Figure **3**
  (sample original-vs-reconstructed trace panels with scale bars).

Both notebooks read from the `results_dir` configured in
`configs/device_path.yaml`; no machine-specific paths anywhere.

## Step-by-step run order

The notebooks only *plot*; the underlying training has to be done first.
Run the commands below in this order from the `fixed/` directory. Edit
`configs/settings.yaml` before each command to set `dataset_type` and
`mode` as listed; `main.py` overrides `mask_intensity` and
[... 599 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/smr && cat train.py
```

```
"""
Training pipeline for SMR, with the unified neighborhood/masking utility from
`fixed/neighborhood.py` and the model factory from `fixed/model.py` threaded
through.

Differences vs. `new/train.py`:
  1. The two per-modality calls
         find_index_mask_eeg(...)  /  find_index_mask_ieeg(...)
     are replaced by a single call to `find_index_mask(...)`, which takes a
     `method` argument (`'atlas'` or `'knn'`) read from `settings`.
  2. A new optional `settings.neighborhood_method` (default `'atlas'`) and
     `settings.neighborhood_k` (default 9) select the neighborhood definition.
  3. A new optional `settings.model_type` (default `'instantaneous'`)
     selects between the instantaneous `ReconModel` and the
     `LaggedReconModelConfigurable`. The latter reads `settings.lags_ms`
     (default `[20, 30, 50, 60]`).
  4. Result paths get a `nbhd-<method>` suffix so atlas-mode and knn-mode runs
     don't overwrite each other.

Everything else (loss, optimizer, regularization, splits, early stopping) is
[... 412 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/smr && cat ReconModel.py && sed -n 1,80p model.py && cat Test_new_subject_iEEG.py && grep -n "def \|dcorr\|mean\|zscore" visualize.py
```

```
"""
Core PyTorch modules for SMR signal reconstruction.

This module exposes two model classes that are used by the training
pipeline:

    * ReconModel        -- instantaneous (lag-0) baseline.
    * LaggedReconModel  -- multi-lag variant with one linear branch per lag
                           plus an instantaneous main branch.

Both modules accept a ``mask_index`` argument at forward time to drop the
masked channels from the input before the linear projection.

The configurable lagged variant used by the training pipeline lives in
``fixed/model.py`` (`LaggedReconModelConfigurable`); it has the same
semantics as ``LaggedReconModel`` but accepts the lag set via constructor.
"""

import torch
import torch.nn as nn
[... 454 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/smr && sed -n 56,82p visualize.py; sed -n 149,180p visualize.py; cat similarity.py | sed -n 1,120p; grep -n "cross_subject_pearson\|hungarian\|def \|length_policy" generate_adj_matrix_ieeg_unseen.py
```

```
# Distance correlation (CPU numpy)
# ---------------------------------------------------------------------------
def distance_correlation(x, y):
    """Sample distance correlation between two 1-D arrays."""
    x = np.atleast_1d(x)
    y = np.atleast_1d(y)
    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("Inputs must be 1D arrays.")

    n = x.shape[0]
    if y.shape[0] != n:
        raise ValueError("Arrays must have the same length.")

    a = np.abs(x[:, None] - x[None, :])
    b = np.abs(y[:, None] - y[None, :])

    A = a - a.mean(axis=0) - a.mean(axis=1)[:, None] + a.mean()
    B = b - b.mean(axis=0) - b.mean(axis=1)[:, None] + b.mean()

    dcov = np.sum(A * B) / (n * n)
[... 167 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/smr && sed -n 1,120p run_coverage_experiment.py; cat path.py | grep -n "ieeg\|eeg" | head -30; cat configs/device_path.example.yaml
```

```
"""
Driver for the *Local / Non-Local / All* coverage experiment (Figure 6
in the paper).

This script trains the SMR model three times per subject under three
different masking schemes:

  * ``local``     -- only the local neighborhood ``N(i)`` is available
                     as predictors of electrode ``i``. Every other
                     channel is masked.
  * ``non_local`` -- ``N(i)`` is masked. Only non-local channels are
                     available. (Equivalent to mask_intensity = 1.0 in
                     the standard sweep.)
  * ``all``       -- only the target electrode is masked. Every other
                     channel is available. (Equivalent to
                     mask_intensity = 0.0 in the standard sweep.)

Outputs are written to::

    <results_dir>/coverage/<dataset_type>/sub_<subject>/
[... 160 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000055/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:1500])"; curl -s https://api.dandiarchive.org/api/dandisets/000055/versions/draft/info/ | python3 -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('name'));print(d.get('description'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python3 -c "
import numpy as np
ie={'intra':[.585,.647,.535,.452,.524,.428,.531,.487,.635,.605,.612,.593],'lag':[.590,.649,.559,.451,.515,.428,.533,.489,.622,.601,.614,.596],'cross':[.331,.483,.440,.325,.509,.285,.415,.377,.409,.363,.395,.340],'ph':[.176,.252,.207,.176,.149,.149,.187,.184,.132,.181,.190,.187],'ia':[.213,.228,.344,.156,.220,.111,.297,.220,.295,.228,.213,.253],'bl':[.148,.112,.698,.397,.129,.126,.159,.180,.130,.113,.112,.107]}
ee={'intra':[.897,.925,.980,.927,.893,.864,.894,.883,.882,.925,.918,.918,.872,.909,.928],'cross':[.784,.782,.522,.635,.770,.783,.823,.837,.773,.895,.899,.831,.750,.840,.819],'ph':[.107,.123,.298,.154,.116,.108,.103,.112,.088,.125,.107,.107,.109,.100,.105],'ia':[.213,.130,.341,.352,.123,.112,.204,.116,.194,.131,.113,.154,.179,.202,.189],'bl':[.147,.111,.399,.296,.133,.124,.159,.119,.130,.112,.112,.106,.146,.175,.130]}
for n,d in [('ieeg',ie),('eeg',ee)]:
  for k,v in d.items(): print(n,k,len(v),round(np.mean(v),3),round(np.std(v),3),round(np.std(v,ddof=1),3))
print(sum(a>b for a,b in zip(ie['intra'],ie['cross'])), sum(a>b for a,b in zip(ee['intra'],ee['cross'])))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
uv run --offline python -c "
import numpy as np
ie={'intra':[.585,.647,.535,.452,.524,.428,.531,.487,.635,.605,.612,.593],'lag':[.590,.649,.559,.451,.515,.428,.533,.489,.622,.601,.614,.596],'cross':[.331,.483,.440,.325,.509,.285,.415,.377,.409,.363,.395,.340],'ph':[.176,.252,.207,.176,.149,.149,.187,.184,.132,.181,.190,.187],'ia':[.213,.228,.344,.156,.220,.111,.297,.220,.295,.228,.213,.253],'bl':[.148,.112,.698,.397,.129,.126,.159,.180,.130,.113,.112,.107]}
ee={'intra':[.897,.925,.980,.927,.893,.864,.894,.883,.882,.925,.918,.918,.872,.909,.928],'cross':[.784,.782,.522,.635,.770,.783,.823,.837,.773,.895,.899,.831,.750,.840,.819],'ph':[.107,.123,.298,.154,.116,.108,.103,.112,.088,.125,.107,.107,.109,.100,.105],'ia':[.213,.130,.341,.352,.123,.112,.204,.116,.194,.131,.113,.154,.179,.202,.189],'bl':[.147,.111,.399,.296,.133,.124,.159,.119,.130,.112,.112,.106,.146,.175,.130]}
for n,d in [('ieeg',ie),('eeg',ee)]:
  for k,v in d.items(): print(n,k,len(v),round(np.mean(v),3),round(np.std(v),3),round(np.std(v,ddof=1),3))
print(sum(a>b for a,b in zip(ie['intra'],ie['cross'])), sum(a>b for a,b in zip(ee['intra'],ee['cross'])))
print([round(a-b,3) for a,b in zip(ie['lag'],ie['intra'])])
"
```

```
Exit code 1
Using CPython 3.13.18 interpreter at: /opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
Creating virtual environment at: .venv
error: Failed to download `pymupdf==2.1`
  cause: Network connectivity is disabled, but the requested data wasn't found in the cache: https://files.pythonhosted.org/packages/f4/dc/e244c162ab621a45bfe36e33fe432264ef7e40592f739474864df66a2dd8/pymupdf-2.1-cp311-abi3-manylinux_2_28_x86_64.whl

hint: `pymupdf` (v2.1) was included because `encore-science` depends on `pymupdf`
```

**Agent calls Bash**

```bash
cd  git status --short; rm -rf .venv; python3 -c "
from statistics import mean,pstdev,stdev
ie={'intra':[.585,.647,.535,.452,.524,.428,.531,.487,.635,.605,.612,.593],'lag':[.590,.649,.559,.451,.515,.428,.533,.489,.622,.601,.614,.596],'cross':[.331,.483,.440,.325,.509,.285,.415,.377,.409,.363,.395,.340],'ph':[.176,.252,.207,.176,.149,.149,.187,.184,.132,.181,.190,.187],'ia':[.213,.228,.344,.156,.220,.111,.297,.220,.295,.228,.213,.253],'bl':[.148,.112,.698,.397,.129,.126,.159,.180,.130,.113,.112,.107]}
ee={'intra':[.897,.925,.980,.927,.893,.864,.894,.883,.882,.925,.918,.918,.872,.909,.928],'cross':[.784,.782,.522,.635,.770,.783,.823,.837,.773,.895,.899,.831,.750,.840,.819],'ph':[.107,.123,.298,.154,.116,.108,.103,.112,.088,.125,.107,.107,.109,.100,.105],'ia':[.213,.130,.341,.352,.123,.112,.204,.116,.194,.131,.113,.154,.179,.202,.189],'bl':[.147,.111,.399,.296,.133,.124,.159,.119,.130,.112,.112,.106,.146,.175,.130]}
for n,d in [('ieeg',ie),('eeg',ee)]:
  for k,v in d.items(): print(n,k,len(v),round(mean(v),3),round(pstdev(v),3),round(stdev(v),3))
print([round(a-b,3) for a,b in zip(ie['lag'],ie['intra'])])
print(sum(min(ie[k][i] for k in ('ph','ia','bl'))<ie['intra'][i] and max(ie[k][i] for k in ('ph','ia','bl'))<ie['intra'][i] for i in range(12)))
"; git status --short
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
?? scripts
ieeg intra 12 0.553 0.068 0.071
ieeg lag 12 0.554 0.068 0.071
ieeg cross 12 0.389 0.064 0.066
ieeg ph 12 0.181 0.029 0.031
ieeg ia 12 0.231 0.06 0.062
ieeg bl 12 0.201 0.168 0.175
eeg intra 15 0.908 0.028 0.029
eeg cross 15 0.783 0.093 0.096
eeg ph 15 0.124 0.049 0.05
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; grep -l "elsewhere" claims/*.yaml | head -3
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:12000])"; grep -n -B2 -A3 "where:" claims/andrews-2024.yaml | head -30
```

```
required": [
        "where"
       ]
      }
     }
    ]
   }
  },
  "checks": {
   "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "date",
     "kind",
     "ready"
    ],
    "properties": {
[... 139 more lines not kept]
```

**Agent**

I have what I need. Writing `claims/memar-2026.yaml`: 20 claims. The iEEG claims are tested on DANDI:000055. The EEG claims are marked `elsewhere` (BNCI Horizon 2020).

**Agent calls Write**

```json
{
 "file_path": "claims/memar-2026.yaml",
 "content": "# Claims for Ostadsharif Memar & Dehghani (2026), \"Spatially Masked Regression Reveals Local and\n# Distributed Predictability in Electrophysiological Recordings\", doi:10.48550/arxiv.2606.11415.\n#\n# Provenance. Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-21, protocol as stated in docs/protocol.md (pilot-18), Reader role.\n#\n# Text read. The arXiv preprint, version 1 (arXiv:2606.11415v1, dated 11 June 2026), full text as\n# stored under paper/ (paper/10.48550-arxiv.2606.11415.txt, \"Version: preprint\"): main text,\n# Material and Methods (sections II A to II H, Algorithms 1 to 4), Results, Discussion, and the\n# appendix Tables II (iEEG) and III (EEG) and Figure 6. The paper has no separate supplement and\n# cites none. No version of record was available. The PDF was not needed; the table values were\n# read from the text, row by row in the column order the headers give.\n#\n# Code read. GitHub neurovium/SpatiallyMaskedRegression (linked in the paper's footnote and Code\n# Availability), commit 244dcdbd67f217873c2a52b77485d97c6fa9bf0e (2026-06-24, after the preprint's\n# date). It holds the model (ReconModel.py, model.py), intra-subject training and the EEG\n# cross-subject path (train.py, main.py), the iEEG cross-subject path (similarity.py,\n# generate_adj_matrix_ieeg_unseen.py, Test_new_subject_iEEG.py), the coverage experiment\n# (run_coverage_experiment.py), surrogates (Load_preprocess_data.py), the neighborhood and mask\n# (neighborhood.py), settings (configs/settings.yaml), a METHODS.md map from the paper to the code,\n# and the figure notebooks (notebooks/). Its module docstrings call it a \"fixed\" version that\n# changes earlier code in places (the mask sweep, the CBEM similarity), so it may not be the code\n# that produced the reported numbers. It does not build the iEEG trials used for training; it loads\n# them from pickled per-subject arrays (\"patient_<n>_reformat.pkl\", coordinates in\n# \"elec_coor_all_move_rest.pkl\") made by a pipeline that is not in the repository.\n# utils.extract_data_dandi is a separate DANDI path (one session, sub-01 ses-3, reach events,\n# 0.5 to 100 Hz, Hilbert envelope, decimation to 10 Hz) that does not match the Methods and is\n# not used by the reported runs.\n#\n# Data the paper used.\n# - iEEG. AJILE12 (Peterson et al. 2022), DANDI:000055, which is the dataset for this file.\n#   12 subjects (8 male, 4 female, mean age 29 ± 7 years) under clinical epilepsy monitoring,\n#   electrodes in one hemisphere each (5 right, 7 left), placement varying across subjects\n#   (Figure 6 shows each subject's electrodes and their AAL regions). Video-identified\n#   upper-limb movement events annotate the recordings. Signals were preprocessed (DC removal and\n#   linear detrending, 0.5 to 150 Hz Butterworth band-pass, 60 Hz notch, 120 Hz low-pass, |z| > 5\n#   samples replaced by the channel median, common average reference, per-channel z-scoring\n#   across time) and cut into 2 s trials centred on movement events (Methods II A a). The dataset\n#   description gives 500 Hz recordings from at least 64 electrodes per participant and wrist\n#   movement events. Measured variables used here are the iEEG voltage per electrode, the\n#   electrodes' MNI coordinates (for the neighborhood), and the movement event times.\n# - EEG. Upper Limb Movements EEG (Ofner et al. 2017, PLoS ONE 12 e0182578), from the BNCI\n#   Horizon 2020 database. 15 healthy subjects, 61 scalp electrodes, six right-arm movements and\n#   rest, one session of execution and one of kinesthetic imagery on different days; band-pass and\n#   notch filtered and z-scored per channel, then cut into trials (Methods II A b). It is not in\n#   DANDI:000055. Its claims are data elsewhere; the paper names the database only, with no\n#   accession or version, and does not say which session (execution, imagery or both) or which\n#   trial window was used.\n#\n# Common iEEG pipeline, with its sources. Claims below refer to it.\n# - Model. For each target electrode i, a linear map (weights and a bias) from the unmasked\n#   electrodes to electrode i at each time sample (Eq. 1; ReconModel.py). Loss is the mean absolute\n#   error plus lambda1 = 1e-5 times the L1 norm and lambda2 = 1e-4 times the squared L2 norm of all\n#   trainable parameters, bias included (Eq. 2, Methods II F; train.py). Adam; mini-batches of\n#   trials; no dropout (Methods II C, II F). Learning rate 0.01, batch size 32, patience 200 epochs,\n#   at most 10000 epochs (configs/settings.yaml; the paper says only that these came from a coarse\n#   validation search). Seeds 42 (utils.configure_environment).\n# - Data split. Each subject's trial array is z-scored across trials, then split 64/16/20 into\n#   train, validation and test trials by two nested 80/20 random splits with a fixed seed (Methods\n#   II D 1). The code z-scores each channel and time sample across trials (scipy zscore, axis 0)\n#   and uses random_state 42. Early stopping on the epoch-averaged validation loss; the lowest\n#   validation-loss checkpoint is evaluated on the test trials.\n# - Score. Distance correlation (Eqs. 8 to 14, the standard biased V-statistic, 0 when the\n#   denominator is 0) between the original and reconstructed test trial of electrode i, per trial,\n#   averaged over test trials. A subject's value is the mean over electrodes (Table II legend,\n#   \"mean ± SD across electrodes\"); an average is the mean over subjects of the subject values,\n#   and its ± is the population SD across subjects (the Average rows of Tables II and III equal\n#   these to the printed precision, checked here by arithmetic on the table).\n# - Neighborhood N(i). The 9 electrodes nearest to i in the (x, z) projection of the MNI\n#   coordinates, i itself excluded (Methods II B). Variant from the code: its default and the\n#   notebooks use method 'atlas', N(i) = electrodes with the same AAL label as i\n#   (neighborhood.py, configs/settings.yaml, README calling it \"manuscript-matching\"). Methods\n#   first; the atlas neighborhood is to be shown as a variant.\n# - Mask intensity m. ceil(m |N(i)|) electrodes drawn at random from N(i) are masked with i\n#   (Results D). The code masks round(m |N(i)|) (neighborhood.find_index_mask), which differs at\n#   m = 0.25 (2 against 3 of 9) and m = 0.5 (4 against 5). Methods first; round is a variant.\n# - The mask intensity behind the intra-subject, lagged and surrogate columns of Table II and\n#   Figure 2 is not stated in the paper. The code settles it as m = 1.0, the full neighborhood\n#   masked (notebooks/visualization.ipynb, Figure 2 cell, \"mask_intensity=1.0 (full local mask,\n#   matching the paper)\"; donor matrices for cross-subject transfer come from intensity 100). This\n#   file follows the code; m = 0 (only the target masked) is to be shown as a variant.\n#\n# Details the paper and code leave open for the iEEG trials, with the readings the text allows.\n# Each analysis is to be run under each reading; outcomes resting on one are marked so.\n# - Which movement events. The paper says \"2-second trials centered on movement events\" and\n#   \"upper-limb movement\" annotations. Readings: (a) the dataset's wrist movement (reach) events,\n#   2 s centred on each event's start time (the event and alignment extract_data_dandi uses);\n#   (b) movement trials together with rest trials, as the code's coordinate file name\n#   (\"all_move_rest\") suggests.\n# - Which recording days. Not stated. Reading: all sessions of each subject, pooled per subject.\n# - Where preprocessing is applied. Not stated. Readings: (a) on each session's continuous\n#   recording before epoching; (b) on each 2 s epoch. The steps are those of the Methods; the\n#   code's preprocess_iEEG adds a median filter, a Hilbert envelope and optional decimation that\n#   the Methods do not list, so they are left out, and the envelope may be shown as a variant.\n# - Trial and electrode exclusion. The paper names none beyond the |z| > 5 replacement. Standard\n#   choice, no trial or electrode is excluded; the code's PSD-based trial rejection\n#   (utils.rem_bad_trials_PSD, on the unused DANDI path) may be shown as a variant.\n# - Subject order. Tables II and III list subjects in rows without identifiers. Reading: row n is\n#   AJILE12 participant n (sub-01 to sub-12), checked against the hemisphere and electrode layout\n#   Figure 6 shows for each subject.\nschema_version: 2\npaper: doi:10.48550/arxiv.2606.11415\nclaims:\n- id: intra-ieeg-mean\n  statement: In the intra-subject setting, SMR reconstructs held-out iEEG with a mean distance\n    correlation of 0.553 ± 0.068 across the 12 AJILE12 subjects.\n  source: Results, III A, paragraph 1; Table II, Average row, Intra-Subject column\n  quote: Mean Dist ... Corr across subjects was 0.908 ± 0.028 for the EEG dataset and 0.553 ± 0.068\n    for the iEEG dataset\n  data: dataset\n  expected:\n  - quantity: mean over 12 subjects of intra-subject DistCorr, iEEG\n    value: 0.553\n    tolerance: 0.068\n  criterion: The common iEEG pipeline of the opening comment at m = 1.0, scored per test trial\n    and averaged over trials, electrodes and then subjects. Reproduced when the average is within\n    tolerance under one reading of the open trial details; the values under every reading, and\n    under the variants (atlas neighborhood, round instead of ceil, m = 0), are reported.\n- id: table2-ieeg-intra-subjects\n  statement: Intra-subject iEEG DistCorr differs across subjects, from 0.428 to 0.647, with the\n    subject values Table II and Figure 2A give.\n  source: Table II, Intra-Subject column; Figure 2A\n  quote: Subject-wise distance correlation (DistCorr; mean ± SD across electrodes) for iEEG in the\n    intra-subject, lagged, cross-subject, and surrogate conditions\n  data: dataset\n  depends_on:\n  - intra-ieeg-mean\n  expected:\n  - quantity: subject 1 intra-subject DistCorr\n    value: 0.585\n    tolerance: 0.041\n  - quantity: subject 2 intra-subject DistCorr\n    value: 0.647\n    tolerance: 0.038\n  - quantity: subject 3 intra-subject DistCorr\n    value: 0.535\n    tolerance: 0.035\n  - quantity: subject 4 intra-subject DistCorr\n    value: 0.452\n    tolerance: 0.036\n  - quantity: subject 5 intra-subject DistCorr\n    value: 0.524\n    tolerance: 0.034\n  - quantity: subject 6 intra-subject DistCorr\n    value: 0.428\n    tolerance: 0.021\n  - quantity: subject 7 intra-subject DistCorr\n    value: 0.531\n    tolerance: 0.028\n  - quantity: subject 8 intra-subject DistCorr\n    value: 0.487\n    tolerance: 0.025\n  - quantity: subject 9 intra-subject DistCorr\n    value: 0.635\n    tolerance: 0.041\n  - quantity: subject 10 intra-subject DistCorr\n    value: 0.605\n    tolerance: 0.040\n  - quantity: subject 11 intra-subject DistCorr\n    value: 0.612\n    tolerance: 0.032\n  - quantity: subject 12 intra-subject DistCorr\n    value: 0.593\n    tolerance: 0.032\n  criterion: Subject values from intra-ieeg-mean, with tolerance the SD across electrodes the\n    table gives for that subject. Reproduced when all 12 are within tolerance under one reading;\n    partially reproduced when 6 to 11 are; not reproduced below 6. The Spearman rank correlation\n    of the 12 values with the table's is reported. Subject order follows the reading in the\n    opening comment.\n- id: intra-eeg-mean\n  statement: In the intra-subject setting, SMR reconstructs held-out scalp EEG with a mean\n    distance correlation of 0.908 ± 0.028 across the 15 subjects.\n  source: Results, III A, paragraph 1; Table III, Average row, Intra-Subject column\n  quote: Mean Dist ... Corr across subjects was 0.908 ± 0.028 for the EEG dataset\n  data: elsewhere\n  where: BNCI Horizon 2020 database, Upper Limb Movements EEG (Ofner et al. 2017, PLoS ONE 12\n    e0182578); the paper gives no accession or version\n  expected:\n  - quantity: mean over 15 subjects of intra-subject DistCorr, EEG\n    value: 0.908\n    tolerance: 0.028\n  criterion: As intra-ieeg-mean, on the EEG data, with N(i) the 9 electrodes nearest in the (x, y)\n    plane of the montage (Methods II B; the code's variant is the 10-10/10-5 regional groups of\n    neighborhood.py). Which EEG session (execution, imagery or both) and which trials are open;\n    each is a reading.\n- id: intra-eeg-above-ieeg\n  statement: Intra-subject reconstruction is consistently stronger in EEG than in iEEG.\n  source: Discussion, paragraph 5; Tables II and III\n  quote: In the intra-subject setting, reconstruction was consistently stronger in EEG than in iEEG\n  data: elsewhere\n  where: BNCI Horizon 2020 database, Upper Limb Movements EEG (Ofner et al. 2017, PLoS ONE 12\n    e0182578), with DANDI:000055 for the iEEG\n  depends_on:\n  - intra-ieeg-mean\n  - intra-eeg-mean\n  criterion: No test is reported. In Tables II and III the lowest EEG subject (0.864) is above the\n    highest iEEG subject (0.647). Reproduced when the EEG average exceeds the iEEG average and\n    every EEG subject value exceeds every iEEG subject value; partially reproduced when only the\n    averages are ordered.\n- id: cross-ieeg-mean\n  statement: Transferring learned inter-electrode matrices from other subjects, through\n    correlation-based electrode mapping and per-electrode donor selection, reconstructs a target\n    subject's trial-averaged iEEG with a mean DistCorr of 0.389 ± 0.064, without fitting weights\n    on the target.\n  source: Results, III B, paragraph 3; Table II, Average row, Cross-Subject column\n  quote: In this setting, the model achieved an ... DistCorr of 0.389±0.064\n  data: dataset\n  depends_on:\n  - intra-ieeg-mean\n  expected:\n  - quantity: mean over 12 subjects of cross-subject DistCorr, iEEG\n    value: 0.389\n    tolerance: 0.064\n  criterion: Method from Methods II D 2 and Algorithm 2, with the code where they are silent.\n    Donor matrices M_learn are the intra-subject weight matrices at m = 1.0 (code, donor directory\n    intesity_100). For each target and donor, C(i, j) is the Pearson correlation of target\n    electrode i and donor electrode j averaged over paired trials 1 to min(R_s, R_s') with NaN\n    trials left out (Eq. 3); the code instead correlates the trial-concatenated series truncated\n    to a common length (similarity.cross_subject_pearson), to be shown as a variant. A one-to-one\n    assignment maximising summed correlation (Hungarian, scipy linear_sum_assignment); unmatched\n    target electrodes get no row from that donor. M_est = P M_learn P^T. The target's trials are\n    split 50/50 into validation and test (random_state 42); for each electrode, the donor whose\n    row gives the highest DistCorr on the z-scored trial-averaged validation signals is chosen,\n    and DistCorr on the z-scored trial-averaged test signals is its score (Methods II D 2).\n    Electrodes with no matched donor are left out of the mean (the code's nanmean). Reproduced\n    when the average is within tolerance under one reading.\n- id: table2-ieeg-cross-subjects\n  statement: Cross-subject iEEG DistCorr ranges over subjects from 0.285 to 0.509, with the\n    subject values Table II and Figure 2A give.\n  source: Table II, Cross-Subject column; Figure 2A\n  quote: the Cross-Subject column reports DistCorr on trial-averaged signals\n  data: dataset\n  depends_on:\n  - cross-ieeg-mean\n  expected:\n  - quantity: subject 1 cross-subject DistCorr\n    value: 0.331\n    tolerance: 0.007\n  - quantity: subject 2 cross-subject DistCorr\n    value: 0.483\n    tolerance: 0.013\n  - quantity: subject 3 cross-subject DistCorr\n    value: 0.440\n    tolerance: 0.012\n  - quantity: subject 4 cross-subject DistCorr\n    value: 0.325\n    tolerance: 0.006\n  - quantity: subject 5 cross-subject DistCorr\n    value: 0.509\n    tolerance: 0.016\n  - quantity: subject 6 cross-subject DistCorr\n    value: 0.285\n    tolerance: 0.004\n  - quantity: subject 7 cross-subject DistCorr\n    value: 0.415\n    tolerance: 0.010\n  - quantity: subject 8 cross-subject DistCorr\n    value: 0.377\n    tolerance: 0.013\n  - quantity: subject 9 cross-subject DistCorr\n    value: 0.409\n    tolerance: 0.010\n  - quantity: subject 10 cross-subject DistCorr\n    value: 0.363\n    tolerance: 0.007\n  - quantity: subject 11 cross-subject DistCorr\n    value: 0.395\n    tolerance: 0.014\n  - quantity: subject 12 cross-subject DistCorr\n    value: 0.340\n    tolerance: 0.007\n  criterion: Subject values from cross-ieeg-mean, with tolerance the SD across electrodes the\n    table gives. Reproduced when all 12 are within tolerance under one reading; partially\n    reproduced when 6 to 11 are; not reproduced below 6. The Spearman rank correlation with the\n    table's values is reported.\n- id: cross-below-intra-ieeg\n  statement: Cross-subject iEEG performance is lower than intra-subject performance but keeps\n    appreciable predictive power.\n  source: Results, III B, paragraph 1; Table II; Figure 2A\n  quote: As expected, performance decreased relative to the intra-subject setting, but the model\n    retained appreciable predictive power\n  data: dataset\n  depends_on:\n  - intra-ieeg-mean\n  - cross-ieeg-mean\n  criterion: No test is reported. In Table II every subject's cross-subject value is below its\n    intra-subject value. Reproduced when the cross-subject average is below the intra-subject\n    average and above the phase-shuffled surrogate average of surrogate-ieeg, and the\n    cross-subject value is below the intra-subject value in at least 11 of 12 subjects; partially\n    reproduced when only the averages are so ordered. Note that the two settings score different\n    signals (single trials against trial averages; Methods II D 2), as the paper does.\n- id: cross-eeg-mean\n  statement: For EEG, transferring a randomly chosen reference subject's matrix, trained at full\n    local masking, directly to the target gives a mean cross-subject DistCorr of 0.783 ± 0.093.\n  source: Results, III B, paragraph 2; Table III, Average row, Cross-Subject column\n  quote: subject DistCorr of 0.783 ± 0.093, indicating robust transfer of the learned\n    inter-electrode structure\n  data: elsewhere\n  where: BNCI Horizon 2020 database, Upper Limb Movements EEG (Ofner et al. 2017, PLoS ONE 12\n    e0182578); the paper gives no accession or version\n  expected:\n  - quantity: mean over 15 subjects of cross-subject DistCorr, EEG\n    value: 0.783\n    tolerance: 0.093\n  criterion: One reference subject drawn at random for each target (Results III B;\n    train.evaluate_model, random.choice), its m = 1.0 models applied unchanged to all of the\n    target's z-scored trials, scored per trial as in the intra-subject setting\n    (visualize.save_mse_all_trials). The draw is random; the result over several draws is\n    reported.\n- id: transfer-penalty-larger-ieeg\n  statement: The drop from intra-subject to cross-subject performance is much larger in iEEG\n    than in EEG.\n  source: Results, III B, paragraphs 1 and 4; Discussion, paragraph 5\n  quote: with the magnitude of the transfer penalty differing markedly between EEG and iEEG\n  data: elsewhere\n  where: BNCI Horizon 2020 database, Upper Limb Movements EEG (Ofner et al. 2017, PLoS ONE 12\n    e0182578), with DANDI:000055 for the iEEG\n  depends_on:\n  - intra-ieeg-mean\n  - cross-ieeg-mean\n  - intra-eeg-mean\n  - cross-eeg-mean\n  criterion: No test is reported. From the paper's averages, the cross over intra ratio is 0.70\n    for iEEG (0.389 / 0.553) and 0.86 for EEG (0.783 / 0.908). Reproduced when the iEEG ratio is\n    below the EEG ratio; the ratios and the differences are reported.\n- id: lagged-ieeg-no-gain\n  statement: Adding lagged predictors (0, 20, 30, 50 and 60 ms) barely changes iEEG\n    reconstruction (0.554 ± 0.067 against 0.553 ± 0.068).\n  source: Results, III C, paragraph 2; Table II, Lagged column\n  quote: For iEEG, the corresponding values were 0.554±0.067 and 0.553±0.068, respectively. ...\n    adding delayed predictors did not materially improve reconstruction\n  data: dataset\n  depends_on:\n  - intra-ieeg-mean\n  expected:\n  - quantity: mean over 12 subjects of lagged intra-subject DistCorr, iEEG\n    value: 0.554\n    tolerance: 0.067\n  criterion: The lagged model of Eq. 6 with lags {0, 20, 30, 50, 60} ms, each lag its own weight\n    vector, offsets ceil(tau fs / 1000) samples (10, 15, 25 and 30 at 500 Hz, where the code's\n    floor gives the same), predictors shifted within each trial with zeros before the trial start\n    (model.LaggedReconModelConfigurable), all other settings as the instantaneous run at m = 1.0\n    (Methods II E; main.py run_lagged_too). A claim of no material gain; the paper reports no\n    test. Reproduced when the lagged average is within tolerance and differs from the\n    instantaneous average by less than 10% of the instantaneous average; not reproduced when the\n    lagged average exceeds the instantaneous one by 10% or more. The paired per-subject\n    differences and a Wilcoxon signed-rank test over the 12 subjects are reported as context.\n- id: lagged-eeg-no-gain\n  statement: Adding lagged predictors barely changes EEG reconstruction (0.910 ± 0.027 against\n    0.908 ± 0.028).\n  source: Results, III C, paragraph 2; Table III, Lagged column\n  quote: EEG performance was 0.910 ± 0.027, compared with 0.908 ± 0.028\n  data: elsewhere\n  where: BNCI Horizon 2020 database, Upper Limb Movements EEG (Ofner et al. 2017, PLoS ONE 12\n    e0182578); the paper gives no accession or version\n  depends_on:\n  - intra-eeg-mean\n  expected:\n  - quantity: mean over 15 subjects of lagged intra-subject DistCorr, EEG\n    value: 0.910\n    tolerance: 0.027\n  criterion: As lagged-ieeg-no-gain, on the EEG data.\n- id: fig4a-mask-sweep-ieeg\n  statement: In iEEG, DistCorr decreases as more of the target's local neighborhood is masked\n    (mask intensity 0, 25, 50, 75 and 100%).\n  source: Results, III D, paragraph 3; Figure 4A\n  quote: In each case, DistCorr decreased as mask intensity increased\n  data: dataset\n  criterion: The common iEEG pipeline run at each m in {0, 0.25, 0.5, 0.75, 1.0}, with ceil(m\n    |N(i)|) neighbors drawn at random and masked with the target (Results III D). Reproduced when\n    the average over subjects decreases at every step from m = 0 to m = 1.0 under one reading;\n    partially reproduced when the m = 1.0 average is below the m = 0 average but some step does\n    not decrease; not reproduced otherwise. The number of subjects whose own values decrease at\n    every step is reported.\n- id: full-mask-above-zero-ieeg\n  statement: With the whole local neighborhood masked, iEEG reconstruction remains above zero,\n    so the target signal is not determined by its immediate neighborhood alone.\n  source: Results, III D, paragraph 3; Figure 4A\n  quote: At the same time, reconstruction re ... mains above zero even under full local masking\n  data: dataset\n  depends_on:\n  - fig4a-mask-sweep-ieeg\n  criterion: The m = 1.0 values of fig4a-mask-sweep-ieeg. The sample DistCorr is never negative,\n    so the paper's comparison with zero is read with the surrogate floor it reports. Reproduced\n    when every subject's m = 1.0 value exceeds that subject's phase-shuffled surrogate value from\n    surrogate-ieeg; partially reproduced when the average does but some subjects do not.\n- id: fig4b-mask-sweep-eeg\n  statement: In EEG, DistCorr decreases as mask intensity increases, and stays above zero with\n    the whole neighborhood masked.\n  source: Results, III D, paragraph 3; Figure 4B\n  quote: In each case, DistCorr decreased as mask intensity increased\n  data: elsewhere\n  where: BNCI Horizon 2020 database, Upper Limb Movements EEG (Ofner et al. 2017, PLoS ONE 12\n    e0182578); the paper gives no accession or version\n  criterion: As fig4a-mask-sweep-ieeg and full-mask-above-zero-ieeg, on the EEG data.\n- id: fig5a-coverage-ieeg\n  statement: In iEEG, reconstruction is best with all electrodes as predictors, and local\n    electrodes alone consistently outperform non-local electrodes alone.\n  source: Results, III E, paragraph 2; Figure 5A\n  quote: As expected, the best performance was achieved when both local and non-local inputs were\n    available ... Notably, the model trained with only local electrodes consistently outperformed\n    the non-local configuration\n  data: dataset\n  criterion: Three runs of the common iEEG pipeline per subject (Results III E;\n    run_coverage_experiment.py). Local, predictors are N(i) only; Non-local, N(i) and the target\n    masked; All, only the target masked. Reproduced when, under one reading, the subject average\n    is ordered All > Local > Non-local and Local exceeds Non-local in at least 11 of 12 subjects\n    (\"consistently\"); partially reproduced when the averages are so ordered but fewer subjects\n    are. The per-subject values of the three conditions are reported.\n- id: fig5b-coverage-eeg\n  statement: In EEG, reconstruction is best with all electrodes as predictors, and local\n    electrodes alone consistently outperform non-local electrodes alone.\n  source: Results, III E, paragraph 2; Figure 5B\n  quote: Notably, the model trained with only local electrodes consistently outperformed the\n    non-local configuration\n  data: elsewhere\n  where: BNCI Horizon 2020 database, Upper Limb Movements EEG (Ofner et al. 2017, PLoS ONE 12\n    e0182578); the paper gives no accession or version\n  criterion: As fig5a-coverage-ieeg, on the EEG data, with at least 14 of 15 subjects for\n    \"consistently\".\n- id: surrogate-ieeg\n  statement: On iEEG surrogates, intra-subject DistCorr falls from 0.553 to 0.181 (phase\n    shuffle), 0.232 (IAAFT) and 0.201 (block shuffle).\n  source: Results, III F, paragraph 3; Table II, Phase Shuffle, IAAFT and Block Shuffle columns\n  quote: For iEEG (Table II), the mean DistCorr decreased from 0.553 ± 0.068 for the origi ... nal\n    data to 0.181 ± 0.029, 0.232 ± 0.060, and 0.201 ± 0.168 for phase-shuffled, IAAFT, and\n    block-shuffled surrogates\n  data: dataset\n  depends_on:\n  - intra-ieeg-mean\n  expected:\n  - quantity: mean over 12 subjects of DistCorr, phase-shuffled iEEG\n    value: 0.181\n    tolerance: 0.029\n  - quantity: mean over 12 subjects of DistCorr, IAAFT iEEG\n    value: 0.232\n    tolerance: 0.060\n  - quantity: mean over 12 subjects of DistCorr, block-shuffled iEEG\n    value: 0.201\n    tolerance: 0.168\n  criterion: Surrogates made per trial and per channel independently from the preprocessed trials\n    (Algorithm 4; Load_preprocess_data.load_per_subject), then put through the common pipeline at\n    m = 1.0 (notebooks/visualization.ipynb). Phase shuffle, the positive-frequency phases of the\n    FFT permuted with Hermitian symmetry and the DC kept (Load_preprocess_data.shuffle_phase).\n    IAAFT, 5 iterations from a random permutation (iaaft_1d). Block shuffle, blocks of 0.5 s\n    permuted with leftover samples appended (block_shuffle_1d; the paper does not give B, the\n    code's default settles it). The Methods say end-matched segmentation was used for the phase\n    surrogates and the code has none; readings (a) as the code, no end matching; (b) each trial\n    trimmed to the sub-segment whose first and last samples and slopes match best before the\n    shuffle. Random draws are a standard choice. Reproduced when all three averages are within\n    tolerance and each is below the original average under one reading. Per-subject values are\n    reported; in Table II subject 3's block-shuffle value (0.698) is above its original (0.535).\n- id: surrogate-eeg\n  statement: On EEG surrogates, intra-subject DistCorr falls from 0.908 to 0.124 (phase shuffle),\n    0.184 (IAAFT) and 0.160 (block shuffle).\n  source: Results, III F, paragraph 3; Table III, Phase Shuffle, IAAFT and Block Shuffle columns\n  quote: For EEG (Table III), the corresponding decrease was from 0.908±0.028 to 0.124±0.049,\n    0.184±0.073, and 0.160±0.078\n  data: elsewhere\n  where: BNCI Horizon 2020 database, Upper Limb Movements EEG (Ofner et al. 2017, PLoS ONE 12\n    e0182578); the paper gives no accession or version\n  depends_on:\n  - intra-eeg-mean\n  expected:\n  - quantity: mean over 15 subjects of DistCorr, phase-shuffled EEG\n    value: 0.124\n    tolerance: 0.049\n  - quantity: mean over 15 subjects of DistCorr, IAAFT EEG\n    value: 0.184\n    tolerance: 0.073\n  - quantity: mean over 15 subjects of DistCorr, block-shuffled EEG\n    value: 0.160\n    tolerance: 0.078\n  criterion: As surrogate-ieeg, on the EEG data.\n- id: surrogate-order-ieeg\n  statement: In iEEG, phase shuffling degrades reconstruction most and IAAFT surrogates keep the\n    most reconstructability of the three surrogates.\n  source: Results, III F, paragraph 4; Table II\n  quote: The strongest average degradation was observed under phase shuffling ... IAAFT surrogates\n    preserved more low ... order properties and therefore retained somewhat more recon\n  data: dataset\n  depends_on:\n  - surrogate-ieeg\n  criterion: The three surrogate averages of surrogate-ieeg. Reproduced when phase shuffle <\n    block shuffle < IAAFT, the order of Table II (0.181, 0.201, 0.232); partially reproduced\n    when phase shuffle is lowest but block shuffle and IAAFT are in the other order.\n- id: surrogate-order-eeg\n  statement: In EEG, phase shuffling degrades reconstruction most and IAAFT surrogates keep the\n    most reconstructability of the three surrogates.\n  source: Results, III F, paragraph 4; Table III\n  quote: The strongest average degradation was observed under phase shuffling\n  data: elsewhere\n  where: BNCI Horizon 2020 database, Upper Limb Movements EEG (Ofner et al. 2017, PLoS ONE 12\n    e0182578); the paper gives no accession or version\n  depends_on:\n  - surrogate-eeg\n  criterion: As surrogate-order-ieeg, on the EEG averages (Table III order 0.124, 0.160, 0.184).\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 tools/claims_check.py claims/memar-2026.yaml paper/10.48550-arxiv.2606.11415.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -v '^#' claims/memar-2026.yaml | grep -nE '[^ ]: ' | grep -vE '^[0-9]+:\s*(- )?[a-z_]+: ' ; grep -nE '—|rather' claims/memar-2026.yaml; git status --short claims
```

```
?? claims/memar-2026.yaml
```

**Agent**

I wrote `claims/memar-2026.yaml`. The quote checker reports 20 claims, 20 quotes, 0 problems. Nothing was committed.

**Text read**
- arXiv preprint v1 (2606.11415v1, dated 11 June 2026), the full text under `paper/`: main text, Methods II A to H with Algorithms 1 to 4, Results, Discussion, and the appendix Tables II and III and Fig. 6.
- There is no supplement and the paper cites none, so nothing the results rest on is missing. I did not need the PDF.
- Code: github.com/neurovium/SpatiallyMaskedRegression at commit 244dcdb (2026-06-24). That commit is two weeks after the preprint, and the code describes itself as a "fixed" version of earlier code. It may not be the code that produced the reported numbers.

**Counts**
- 20 claims, all with quotes, none marked inferred.
- No statistics fields: the paper reports no tests or intervals, only mean ± SD.
- 11 claims have expected values. The tolerance is the paper's stated SD: across subjects for averages, across electrodes for per-subject values.
- All 20 claims have criteria.
- 10 claims use DANDI:000055 (iEEG). The other 10 are EEG claims or EEG against iEEG comparisons, marked `data: elsewhere` (BNCI Horizon 2020, Ofner et al. 2017).
- I checked by arithmetic that each table's Average row is the mean ± population SD of the subject rows.

**Details left open, with the readings named**
- **Neighborhood:** the Methods use the 9 nearest electrodes by projected MNI distance. The code's default is "same AAL label". I followed the Methods and named the code's choice as a variant.
- **Number of neighbors masked:** the Methods use ceil(m·|N|), the code uses round(m·|N|). Methods followed, code as a variant.
- **Mask intensity for the intra-subject, lagged and surrogate numbers:** the paper doesn't say. The figure notebook settles it as m = 1.0, so I followed that, with m = 0 as a variant.
- **Cross-subject correlation matrix:** the Methods (Eq. 3) average Pearson correlations over paired trials. The code correlates concatenated trials. Methods followed, code as a variant.
- **Phase-shuffle surrogates:** the Methods say end-matched segmentation was used; the code has none. Readings: (a) no end matching; (b) end-matched trimming.
- **iEEG trials:**
  - Which events. Readings: (a) reach onsets, 2 s centred on each; (b) movement plus rest trials.
  - Which days. Reading: all sessions pooled per subject.
  - Where preprocessing is applied. Readings: (a) on the continuous recording before epoching; (b) on each epoch.
  - Exclusions. Standard choice of none, with the code's PSD-based trial rejection as a variant.
- **Subject order:** I read table row n as AJILE12 participant n. The author is to check this against Fig. 6.
- **Settled by the code where the paper is silent:** learning rate 0.01, batch size 32, patience 200, seed 42, block length 0.5 s, and z-scoring per channel and time sample across trials.

**Missing from the paper or code**
- The iEEG trial-building pipeline. The code loads pre-made pickles. Its DANDI extraction path (one session, Hilbert envelope, 10 Hz) does not match the Methods.
- Any accession or version for the EEG dataset, and which EEG session and trials were used.
- Any statistical test. Every claim of absence or ordering (the lagged model's lack of gain, the surrogate ranking, Local above Non-local) has a rule set in this file instead.
- One finding the paper does not mention: Table II shows block shuffling above the original data for iEEG subject 3 (0.698 vs 0.535).

## End of run

26 turns, 5 minutes, $2.34 at API prices, result: success.
