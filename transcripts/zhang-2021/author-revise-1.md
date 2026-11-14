# zhang-2021 · author-revise-1 · run 43594534614

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/zhang-2021/verifier-1-report.md; ls entries/zhang-2021; cat docs/protocol.md | wc -l
```

```
Sat Nov 14 12:25:49 UTC 2026
**A. Outcomes** (11 claims in the claims file)

| claim | outcome | reason |
|---|---|---|
| fig1-csi-s2 | reproduced | Cell 15: with the code's positions (R3) S2 gives 0.740, 0.718 and 0.676, all within tolerance and above every null value under both permutation readings (p ≤ 1/1001). The R2 reading also passes. The 2-D variant fails only on attend-humans (0.664 against 0.675). |
| att-csi-group | reproduced | Cell 18, R3: the means are 0.665, 0.729 and 0.525, all within tolerance. Reading (b), the group mean above every mean null value, passes for all three conditions. Reading (a) fails for passive because S3 passive (0.061) does not exceed every null value. |
| supp-csi-per-subject | reproduced | Cell 20: R3 has 10 of 12 values within tolerance, R2 has 11 of 12, and all 12 are significant at p < 0.01 under null (a). The misses are S3 passive (0.061 against 0.05 ± 0.005) and S5 attend-humans (0.767). |
| att-passive-lower | not_reproduced | Cell 22: at most 3 of 5 subjects count at the bound (R3, matched, ii, reading b), and 4 of 5 are needed. S1 and S6 have passive CSI at or above attend-humans, so d_mean is about 0 (p 0.38 to 0.53), and this holds under every reading. The 4 of 5 in the R1/matched/i row at p < 0.05 is the variant that does not decide. |
| att-classification | reproduced | Cell 24: contiguous folds give 44.4% (Euclidean) and 53.4% (density), and random folds with Euclidean give 46.6%, all within 48.4 ± 7.6 and above every null mean. Chance under the procedure is 7.8 to 9.1%, against the paper's 8.3%. |
| att-weights-cortex | blocked (data_missing) | Cell 25: the paper's per-subject ROIs from localizers are not deposited. Part of the claim could still be tested with an fsaverage atlas (see B3). |
| game-csi | reproduced | Cell 28, reading (b): S1 0.702 and S7 0.581, both within tolerance and above every null value. Reading (a) misses for S7 (0.549 against a lower bound of 0.558), and reading (c) misses for both. The pas
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/protocol.md
```

```
<persisted-output>
Output too large (39.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b561b78a-7e67-4a9d-a830-b696571ecc52/tool-results/bk3sfksvg.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-15`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
ls docs; cat entries/zhang-2021/entry.yaml; ls attempts* 2>/dev/null; ls; ls questions claims 2>/dev/null | grep zhang
```

```
agents
archives.md
author-responses.md
badges.md
conversion-tracker.md
design.md
encore.md
fixing-conversions.md
paper-first.md
pilot-notes
pilot-notes.md
pipeline.md
protocol.md
queue.md
schema_version: 1
name: zhang-2021
type: reproduction
title: Voxel-based state space modeling in a visual attention task and a video game (Zhang et al. 2021)
description: Tests the findings of Zhang, Gao, Cukur and Gallant (2021) on CRCNS data set vim-4, which
  holds deconvolved whole-cortex fMRI of five of the six subjects of a visual attention task and the
[... 352 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; grep -n -i "verif\|round\|proposed" docs/protocol.md | head -80
```

```
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
165:### 4. Data from outside the paper's own recordings
173:### 5. Check
186:### 6. Answer questions
199:## Author
215:### 1. Establish what can be tested
345:### 2. Check the data against its description
360:### 3. Write the entry
431:### 4. Lock, check and run
451:### 5. Record the attempt
524:### 6. Hand over for verification
562:## Repeat attempts
604:## Local and remote datasets
627:## Verifier
631:### Round 1: without the author's conclusions
656:### Round 2: with the author's conclusions
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 199,626p docs/protocol.md
```

```
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested: do not change a claim's statement, expected values or
criterion. A method detail the claims file lacks is taken from the paper
(step 6).

**Time.** An author run is stopped five hours after it starts, and whatever
is not recorded by then is lost. The prompt says when the run started and the
time by which to finish. Check the clock (`date -u`) between steps. When that
time comes, stop analysing and finish: record each claim not yet tested as
blocked, `too_large` where the computation is what stopped it, saying how far
it got, then write the attempt record and run the entry's checks. A record
with some claims blocked for time is worth more than a run that is cut off.

### 1. Establish what can be tested

Do this before any analysis.

[... 408 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/zhang-2021-01.yaml; cat questions/zhang-2021.yaml 2>/dev/null; ls executed/zhang-2021
```

```
schema_version: 3
id: zhang-2021-01
datasets:
- archive: crcns
  id: vim-4
  version: unversioned
  doi: 10.6080/K0668BDF
  relation: primary
paper: doi:10.3389/fnins.2020.565976
date: 2026-11-14
entry: zhang-2021
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-15
  runner:
[... 228 more lines not kept]
```

**Agent**

Starting on the round-1 revision. Reading the claims file and notebook now.

**Agent calls Bash**

```bash
cat claims/zhang-2021.yaml; wc -c entries/zhang-2021/*; cat entries/zhang-2021/requirements.in
```

```
<persisted-output>
Output too large (30.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b561b78a-7e67-4a9d-a830-b696571ecc52/tool-results/b60mvk86k.txt

Preview (first 2KB):
# Claims for Zhang, Gao, Cukur & Gallant (2021), Frontiers in Neuroscience 14:565976,
# "Voxel-Based State Space Modeling Recovers Task-Related Cognitive States in Naturalistic fMRI
# Experiments", doi:10.3389/fnins.2020.565976, on CRCNS data set vim-4 (doi:10.6080/K0668BDF).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
# protocol as stated in docs/protocol.md (Reader), version pilot-14.
#
# Text read: the version of record (PMC8145286, open access), as JATS XML flattened to text under
# paper/: main text, Materials and Methods, figure legends, Table 1, and the supplement
# (Data_Sheet_1.DOCX, legends of Supplementary Figures 1 to 5). No PDF was supplied. The
# per-subject CSI values of the attention task are printed only inside the images of
# Supplementary Figures 1 and 2; they were read from the images in the supplement file (S1
# 0.51, 0.79, 0.64; S3 0.70, 0.71, 0.05; S4 0.64, 0.69, 0.47; S5 0.66, 0.74, 0.59; S6 0.60, 0.71,
# 0.61, for attend-humans, attend-vehicles and passive). The images of Figures 1 to 4 of the main
# text were not available, so the pattern of Figure 3B is not known here. Two inconsistencies of
# the paper, noted where they matter. (1) The means of the six per-subject CSIs in Figure 1 and
# the supplement (0.64, 0.72, 0.51) are not exactly the means the Results give (0.66, 0.74, 0.53).
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A40 "id: att-weights-cortex\|id: game-weights-two-groups" claims/zhang-2021.yaml
```

```
261:- id: att-weights-cortex
262-  statement: The human-presence dimension of the attention-task state space has its weights in
263-    face and body areas (FFA, OFA, EBA), MT+, LO, the frontal operculum and the inferior frontal
264-    sulcus; the vehicle-presence dimension in RSC, PPA, OPA, IPS, FEF and around the inferior
265-    frontal sulcus.
266-  source: Results, The Voxel-Based State Space Method Recovers a State Space for Variables in
267-    the Attention Task, paragraph 4; Figure 2; Supplementary Figure 3
268-  quote: The “human presence” dimension projects heavily onto FFA ( Kanwisher et al., 1997 ), OFA (
269-    Gauthier et al., 2000 ), and EBA ( Downing et al., 2001 ) ... In contrast, the “vehicle
270-    presence” dimension projects strongly onto RSC ( Maguire, 2001 ; Epstein, 2008 ), PPA (
271-    Epstein et al., 1999 ), and OPA ( Dilks et al., 2013 )
272-  data: with_inputs
273-  criterion: The ROIs were delineated per subject from functional localizer and retinotopic
274-    mapping data (Methods, Preprocessing and Visualization, paragraph 2), which the paper does
275-    not deposit and the data set's description does not list; the author decides whether an
276-    outside ROI source (for example an fsaverage atlas through the data set's mappers) can be
277-    used. Which weights are mapped is open; the readings are (a) the OLS weights B, (b) the
278-    denoised weights B_L, and (c) the state directions Q_S, each sign-oriented so that the
279-    dimension's own state has a positive mean position. Figure 2 and Supplementary Figure 3
280-    threshold voxels by the prediction performance of a semantic encoding model at uncorrected p
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; cat README.md; grep -n "def \|^[A-Z_]* = \|url\|http" statespace.py | head -80
```

```
# Zhang et al. (2021) on CRCNS vim-4

Tests the findings of Zhang, Gao, Cukur and Gallant (2021), "Voxel-Based State Space Modeling
Recovers Task-Related Cognitive States in Naturalistic fMRI Experiments", Frontiers in Neuroscience
14:565976, on CRCNS data set vim-4 (doi:10.6080/K0668BDF), streamed from the public CRCNS bucket.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

- `reproduce_zhang_2021.ipynb`: the data check and one section per claim.
- `statespace.py`: loading, the state space of the paper's code (computed in the space of the 24
  principal components), the cluster separation index and the classifiers.

The notebook streams about 7 GB and runs in about 20 minutes with 4 GB of memory.
42:BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-4/live/"
43:DOI = "10.6080/K0668BDF"
44:VERSION = "unversioned"
45:ATT_SUBJECTS = ["S1", "S2", "S3", "S5", "S6"]  # S4 not released (data description)
46:GAME_SUBJECTS = ["S1", "S7"]
47:CONDITIONS = ["passive", "human", "vehicle"]  # stacking order of the code's Example.ipynb
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; sed -n 1,150p statespace.py
```

```
"""Loading and state space measures for CRCNS vim-4 (Zhang, Gao, Cukur & Gallant 2021).

The data set is streamed from the public CRCNS bucket; nothing is written to disk.

Where each method comes from:

- State space: the paper's Methods ("Voxel-Based State Space Modeling") and its
  code, gallantlab/state-space at commit 6ffb3c3, `extract_state_space_positions`
  (claims file, opening comment): OLS of the responses on the task variables
  with an intercept column (pinv of the normal equations), PCA with 24
  components on the [TR x voxel] responses, denoised weights U U^T B^T, the
  first (variables) columns of Q from the QR of the denoised weights, positions
  = responses x those columns, z-scored per dimension over the TRs fitted.
- Computation in PC space (an exact rewrite, not a change of method): every
  denoised weight vector lies in the span of the 24 components C (24 x voxels,
  orthonormal rows), so with Z = Y C^T the OLS coefficients projected on the
  components are pinv(P^T P) P^T Z, the QR of C^T M equals C^T times the QR of
  M, and the positions are Z Q_M. The PCA itself is computed exactly from the
  TR x TR Gram matrix Y Y^T (the eigenvectors of the centred Gram matrix); the
  code's scikit-learn PCA(24) uses a randomized solver for this shape, which
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; curl -sI https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-4/live/Mappers/S7.hdf | head -5; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=vim-4/live/Mappers" | tr '<' '\n' | grep -E "^Key|^Size" ; curl -sI https://api.github.com/repos/VPNL/visfAtlas | head -3; curl -sI https://zenodo.org | head -2; curl -sI https://figshare.com | head -2
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd entries/zhang-2021; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/vim-4/live/Mappers/old/README.txt; echo; python -c "
import statespace as s
for p in ['Mappers/S7.hdf','Mappers/old/S1.hdf']:
    print(p, s.hdf_layout(p))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  ls -a; ls ~/.cache 2>/dev/null; grep -n "venv\|uv " tools/entry.py | head -20
```

```
.
..
.bash_profile
.bashrc
.claude
.env
.env.development
.env.development.local
.env.local
.env.production
.env.production.local
.env.test
.env.test.local
.git
.gitconfig
.github
.gitignore
.gitmodules
.idea
.mcp.json
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -a executed/zhang-2021; sed -n 545,575p tools/entry.py
```

```
.
..
.clean-run.json
.venv
reproduce_zhang_2021.ipynb
result.json
    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
    if stamp:
        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
        for r in stamp["results"]:
            print(f"pass  {r['notebook']}  ({r['seconds']} s, reused)")
        print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
        return 0
    (output_dir / STAMP).unlink(missing_ok=True)   # whatever is there is no longer what a run left
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
[... 17 more lines not kept]
```

**Agent**

Using the executed copy's venv for development.

**Agent calls Bash**

```bash
cd entries/zhang-2021; P=executed/zhang-2021/.venv/bin/python; $P -c "
import statespace as s
for p in ['Mappers/S7.hdf','Mappers/old/S1.hdf']:
    print(p, s.hdf_layout(p))
"; $P -m pip list 2>/dev/null | head -50; cat requirements.in
```

```
Mappers/S7.hdf [('pixmap_data', (1425974,), 'float64'), ('pixmap_indices', (1425974,), 'int32'), ('pixmap_indptr', (1442220,), 'int32'), ('pixmap_shape', (2,), 'int64'), ('pixmask', (2284, 1024), 'bool'), ('vox_to_fsavg_left_data', (165420,), 'float64'), ('vox_to_fsavg_left_indices', (165420,), 'int32'), ('vox_to_fsavg_left_indptr', (163843,), 'int32'), ('vox_to_fsavg_left_shape', (2,), 'int64'), ('vox_to_fsavg_right_data', (164706,), 'float64'), ('vox_to_fsavg_right_indices', (164706,), 'int32'), ('vox_to_fsavg_right_indptr', (163843,), 'int32'), ('vox_to_fsavg_right_shape', (2,), 'int64')]
Mappers/old/S1.hdf [('pixmap_data', (1155714,), 'float64'), ('pixmap_indices', (1155714,), 'int32'), ('pixmap_indptr', (1155715,), 'int32'), ('pixmap_shape', (2,), 'int64'), ('pixmask', (1883, 1024), 'bool'), ('vox_to_fsavg_left_data', (163273,), 'float64'), ('vox_to_fsavg_left_indices', (163273,), 'int32'), ('vox_to_fsavg_left_indptr', (163843,), 'int32'), ('vox_to_fsavg_left_shape', (2,), 'int64'), ('vox_to_fsavg_right_data', (163682,), 'float64'), ('vox_to_fsavg_right_indices', (163682,), 'int32'), ('vox_to_fsavg_right_indptr', (163843,), 'int32'), ('vox_to_fsavg_right_shape', (2,), 'int64')]
aiohttp
fsspec
h5py
matplotlib
numpy
pandas
requests
scikit-learn
scipy
```

**Agent calls ToolSearch**

```json
{
 "query": "select:WebSearch,WebFetch",
 "max_results": 2
}
```

Result: no output.

**Agent calls WebSearch**

```json
{
 "query": "visfAtlas Rosenke 2021 fsaverage download annot zenodo OR github"
}
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sIL https://download.brainvoyager.com/data/visfAtlas.zip | grep -i -E "HTTP|length|last-mod|etag"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -o visf.zip https://download.brainvoyager.com/data/visfAtlas.zip; sha256sum visf.zip; unzip -l visf.zip | grep -i -E "fsaverage|annot|label" | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; unzip -l visf.zip | grep -i -E "MPA|README|pdf|txt" | head; curl -s https://api.figshare.com/v2/articles/3498446 | python3 -c "
import json,sys; d=json.load(sys.stdin); print(d['title'], d['doi'], d.get('version'))
for f in d['files']: print(f['name'], f['size'], f['download_url'], f.get('computed_md5'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; unzip -o -q visf.zip 'visfAtlas/FreeSurfer/*'; sed -e 's/\\[a-z0-9]*//g' visfAtlas/FreeSurfer/README.rtf | tr -s '{} ' | tail -40; executed/zhang-2021/.venv/bin/python -c "import nibabel" ; python3 -c "import nibabel; print(nibabel.__version__)"
```

```
Exit code 1
 "We used the functional atlas of visual cortex developed by Rosenke et al. (2020)'85'94
 


 
Downloaded content:


 
Files

 -108 
 Width5460Width3 
 Width7740Width3 


 MPM_
 hemisphere_area.
 label
[... 29 more lines not kept]
```

**Agent calls WebFetch**

```json
{
 "url": "https://www.biorxiv.org/content/10.1101/2020.01.22.916239v4.full",
 "prompt": "List the visfAtlas areas and which category (faces, bodies, places, characters, motion) each belongs to, with their naming (e.g. IOG-faces, CoS-places, TOS-places, LOS-bodies). Quote the passage. Is there a medial place area (MPA/RSC) in the atlas? Which areas are named FFA, OFA, EBA, PPA, OPA?"
}
```

Result: the fetched text is not kept.

**Agent calls WebFetch**

```json
{
 "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC7727347/",
 "prompt": "List the visfAtlas areas and which category (faces, bodies, places, characters, motion) each belongs to, with their naming (e.g. IOG-faces, CoS-places, TOS-places, LOS-bodies). Quote the passages verbatim. Is there a medial place area (MPA/RSC) in the atlas? Does the paper relate them to FFA, OFA, EBA, PPA, OPA names? Quote."
}
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd entries/zhang-2021; sed -n 150,420p statespace.py; curl -sI https://download.brainvoyager.com/data/visfAtlas.zip | grep -i accept
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 -c "
import json
nb=json.load(open('reproduce_zhang_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(i,c['cell_type'],c.get('metadata',{}).get('tags'),len(src), src[:150].replace(chr(10),' | '))
"
```

```
0 markdown None 2958 # Reproducing Zhang, Gao, Cukur & Gallant (2021) from CRCNS vim-4 |  | Paper: Zhang T, Gao JS, Cukur T, Gallant JL (2021). Voxel-Based State Space Modelin
1 code None 309 import time, resource | import numpy as np | import pandas as pd | import matplotlib.pyplot as plt | import requests | import statespace as ss |  | pd.set_option("d
2 markdown None 13 ## Data check
3 code ['sanity'] 838 # Files in the data set and their current MD5 sums (checksums.md5 in the bucket) | listing = requests.get("https://crcnsarchive.s3-us-west-2.amazonaws.c
4 code ['sanity'] 658 # Layout of every data file: datasets, shapes and dtypes (no data read) | for f in ["VisualAttention/Data/S%d.hdf" % i for i in (1, 2, 3, 5, 6)] + \ |    
5 code ['sanity'] 1817 # Attention task labels: states.hdf, and the semantic labels they should follow | st = ss.load_attention_states() | for c in ss.CONDITIONS: |     v = st[c] | 
6 code ['sanity'] 1952 # Load each attention subject's deconvolved data (stacked passive, human, vehicle), keep the | # 2700 x 2700 Gram matrix, and run the paper's code itsel
7 code ['sanity'] 736 # Per-condition means of the voxels: the attentive conditions are z-scored per voxel within the condition, | # so the attention variable (-1 human, 0 pa
8 code ['sanity'] 898 # Clock check for the attention task: CSI of the presence clusters when the presence labels are | # shifted in time within each condition (refitted at e
9 code ['sanity'] 1512 # Video game data | game = {} | for s in ss.GAME_SUBJECTS: |     t = time.time() |     g = ss.load_game(s) |     G = g["G"] |     Z, _, ve = ss.pca_scores(G, np.a
10 code ['sanity'] 662 # Clock check for the video game: CSI (one cluster per state) with the state matrix shifted in time | rng = np.random.default_rng(101) | rows = [] | for s i
11 markdown None 2662 Checks of the description against the data, from the outputs above: |  | - The deconvolved attention files hold 900 TRs per condition for S1, S2, S3, S5 a
12 mark
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 -c "
import json
nb=json.load(open('reproduce_zhang_2021.ipynb'))
for i in [0,1,6,7,9,10,11,13,25,30,33,42,44,45]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
===== 0
# Reproducing Zhang, Gao, Cukur & Gallant (2021) from CRCNS vim-4

Paper: Zhang T, Gao JS, Cukur T, Gallant JL (2021). Voxel-Based State Space Modeling Recovers
Task-Related Cognitive States in Naturalistic fMRI Experiments. Frontiers in Neuroscience
14:565976. doi:10.3389/fnins.2020.565976.

Claims: `claims/zhang-2021.yaml`, written from the version of record (PMC8145286) and its
supplement (Data_Sheet_1.DOCX), with the paper's code, gallantlab/state-space at commit 6ffb3c3.

Dataset: CRCNS vim-4, "Whole-brain BOLD activity recorded by fMRI during a visual attention task
and a video game task", doi:10.6080/K0668BDF, streamed from the public bucket
`s3://crcnsarchive/vim-4/live/`. Version: `unversioned`. CRCNS data sets have no versions; the
files read are those under `vim-4/live/` as of 2026-11-14 (data description version 0.8 of
2026-04-06), which is the only published copy of the data files (`vim-4/old/` holds only older
versions of the description). The paper cites the data set by its DOI, with no version. The MD5
sums of the files read, from the data set's `checksums.md5`, are:

| file | MD5 |
|---|---|
[... 382 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; P=executed/zhang-2021/.venv/bin/python; uv pip install --quiet --python $P nibabel 2>&1 | tail -2; cd $TMPDIR; curl -sL -o lh.hcp.annot https://ndownloader.figshare.com/files/5528816; $P -c "
import nibabel as nib
for f in ['visfAtlas/FreeSurfer/lh.visfAtlas.annot','visfAtlas/FreeSurfer/rh.visfAtlas.annot','lh.hcp.annot']:
    lab,ctab,names=nib.freesurfer.read_annot(f)
    import numpy as np
    print(f, lab.shape, [ (n.decode(), int((lab==i).sum())) for i,n in enumerate(names)][:200])
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 - <<'EOF'
import json
nb=json.load(open('reproduce_zhang_2021.ipynb'))
for i in [3,4,5,8,15,19,22,28,36,39]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
EOF
```

```
===== 3
# Files in the data set and their current MD5 sums (checksums.md5 in the bucket)
listing = requests.get("https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=vim-4/").text
import re
files = [(k, int(s)) for k, s in re.findall(r"<Key>(.*?)</Key>.*?<Size>(\d+)</Size>", listing) if not k.endswith("/")]
print(f"{len(files)} files under vim-4/")
for k, s in files:
    print(f"  {s/1e6:10.2f} MB  {k}")
md5 = dict(l.split()[::-1] for l in requests.get(ss.BASE + "checksums.md5").text.strip().splitlines())
read_files = ["VisualAttention/Data/deconv/S%d.hdf" % i for i in (1, 2, 3, 5, 6)] + [
    "VisualAttention/Stimuli/states.hdf", "VisualAttention/Stimuli/semantics.hdf",
    "VideoGame/Data/S1.npy", "VideoGame/Data/S7.npy", "VideoGame/Stimuli/S1.hdf", "VideoGame/Stimuli/S7.hdf"]
for f in read_files:
    print(md5[f], f)
===== 4
# Layout of every data file: datasets, shapes and dtypes (no data read)
for f in ["VisualAttention/Data/S%d.hdf" % i for i in (1, 2, 3, 5, 6)] + \
         ["VisualAttention/Data/deconv/S%d.hdf" % i for i in (1, 2, 3, 5, 6)] + \
         ["VisualAttention/Stimuli/states.hdf", "VisualAttention/Stimuli/semantics.hdf",
          "VideoGame/Stimuli/S1.hdf", "VideoGame/Stimuli/S7.hdf"] + \
[... 210 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; cat >> statespace.py <<'EOF'


# ---------------------------------------------------------------- cortical regions

VISF_URL = "https://download.brainvoyager.com/data/visfAtlas.zip"
VISF_SHA256 = "2eae192d3aeab8f9812991c8a9bc2822d10c4d0a621172aaa43df1900660799d"
HCP_URL = {"lh": "https://ndownloader.figshare.com/files/5528816",
           "rh": "https://ndownloader.figshare.com/files/5528819"}
HCP_MD5 = {"lh": "46a102b59b2fb1bb4bd62d51bf02e975", "rh": "75e96b331940227bbcb07c1c791c2463"}

# Regions of the claims, as unions of atlas areas on fsaverage (an assumption: the paper's
# ROIs were drawn per subject from localizers, which are not public).
# visfAtlas (Rosenke et al. 2021, doi:10.1093/cercor/bhaa246): the face areas on the
# fusiform (mFus, pFus) form the FFA, IOG-faces is the OFA, the lateral body areas (LOS, ITG,
# MTG) form the EBA, CoS-places is the PPA and TOS-places (right hemisphere only) the OPA.
# HCP-MMP1.0 (Glasser et al. 2016, on fsaverage: doi:10.6084/m9.figshare.3498446.v2) for the
# regions visfAtlas lacks, with the area names of Glasser et al. (2016), Supplementary
# Neuroanatomical Results.
ATT_REGIONS = {
    "FFA": ("visf", ["mFus-faces", "pFus-faces"]),
    "OFA": ("visf", ["IOG-faces"]),
    "EBA": ("visf", ["LOS-bodies", "ITG-bodies", "MTG-bodies"]),
    "MT+": ("visf", ["hMT"]),
    "PPA": ("visf", ["CoS-places"]),
    "OPA": ("visf", ["TOS-places"]),
    "RSC": ("hcp", ["RSC"]),
    "LO": ("hcp", ["LO1", "LO2", "LO3"]),
    "FO": ("hcp", ["FOP1", "FOP2", "FOP3", "FOP4", "FOP5"]),
    "IFS": ("hcp", ["IFSa", "IFSp"]),
    "IPS": ("hcp", ["IPS1", "IP0", "IP1", "IP2", "LIPv", "LIPd", "VIP", "MIP", "AIP"]),
    "FEF": ("hcp", ["FEF"]),
    "SEF": ("hcp", ["SCEF"]),
}
_PFC = ["8C", "8Av", "i6-8", "s6-8", "SFL", "8BL", "9p", "9a", "8Ad", "p9-46v", "a9-46v", "46", "9-46d",
        "44", "45", "47l", "a47r", "p47r", "IFJa", "IFJp", "IFSa", "IFSp",
        "10d", "10pp", "a10p", "p10p", "11l", "13l", "OFC", "47m", "47s", "pOFC",
        "10r", "10v", "9m", "8BM", "p32", "d32", "s32", "a24", "25"]
GAME_REGIONS = {
    "TPJ": ("hcp", ["TPOJ1", "TPOJ2", "TPOJ3", "PGi", "PGs"]),
    "precuneus": ("hcp", ["7m", "PCV", "POS2", "31pd", "31pv"]),
    "prefrontal": ("hcp", _PFC),
    "motor": ("hcp", ["4"]),
    "premotor": ("hcp", ["6a", "6d", "6v", "6r", "55b", "PEF"]),
    "SMA": ("hcp", ["6ma", "6mp"]),
    "IPS": ATT_REGIONS["IPS"],
    "FEF": ("hcp", ["FEF"]),
    "SEF": ("hcp", ["SCEF"]),
}


def parse_annot(buf):
    """Vertex labels and names of a FreeSurfer .annot file (bytes), new colour table format."""
    import io
    f = io.BytesIO(buf)
    i4 = lambda n=1: np.frombuffer(f.read(4 * n), ">i4")
    vnum = int(i4()[0])
    vd = i4(2 * vnum).reshape(-1, 2)
    values = np.zeros(vnum, np.int64)
    values[vd[:, 0]] = vd[:, 1]
    assert int(i4()[0]) == 1  # colour table present
    assert int(i4()[0]) == -2  # version 2
    i4()  # max structure id
    f.read(int(i4()[0]))  # name of the original table
    names, codes = [], []
    for _ in range(int(i4()[0])):
        i4()  # structure id
        names.append(f.read(int(i4()[0])).rstrip(b"\x00").decode())
        r, g, b, _t = i4(4)
        codes.append(int(r) + int(g) * 256 + int(b) * 65536)
    lookup = dict(zip(codes, names))
    return np.array([lookup.get(int(v), "") for v in values])


def load_atlases():
    """Vertex names per hemisphere for both atlases: {"visf"|"hcp": {"lh": names, "rh": names}}.

    Each file is read into memory and checked against its published checksum."""
    import hashlib, io, zipfile
    import requests
    z = requests.get(VISF_URL, timeout=600).content
    assert hashlib.sha256(z).hexdigest() == VISF_SHA256
    out = {"visf": {}, "hcp": {}}
    with zipfile.ZipFile(io.BytesIO(z)) as zf:
        for h in ("lh", "rh"):
            out["visf"][h] = parse_annot(zf.read(f"visfAtlas/FreeSurfer/{h}.visfAtlas.annot"))
    for h in ("lh", "rh"):
        b = requests.get(HCP_URL[h], timeout=600).content
        assert hashlib.md5(b).hexdigest() == HCP_MD5[h]
        out["hcp"][h] = np.array([n[2:-4] if n.endswith("_ROI") else "" for n in parse_annot(b)])
    return out


def load_mapper(subject):
    """The data set's voxel-to-fsaverage mappers, {"lh"|"rh": CSR [vertices x voxels]}."""
    from scipy import sparse
    d = read_hdf(f"Mappers/{subject}.hdf")
    side = {"lh": "left", "rh": "right"}
    return {h: sparse.csr_matrix((d[f"vox_to_fsavg_{s}_data"], d[f"vox_to_fsavg_{s}_indices"],
                                  d[f"vox_to_fsavg_{s}_indptr"]), shape=tuple(d[f"vox_to_fsavg_{s}_shape"]))
            for h, s in side.items()}


def region_matrix(mapper, atlases, regions, voxel_mask=None):
    """[voxel x region] matrix whose product with a voxel map gives the region's mean on fsaverage.

    A region's mean is taken over its vertices (both hemispheres) that the mapper reaches,
    each vertex the mapper's weighted mean of its voxels. voxel_mask keeps only some voxels
    (a vertex counts when it reaches a kept voxel). Returns the matrix and the vertices used.
    """
    from scipy import sparse
    cols, nvert = [], []
    for atlas, areas in regions.values():
        col, n = 0, 0
        for h, Mh in mapper.items():
            if voxel_mask is not None:
                Mh = Mh @ sparse.diags(voxel_mask.astype(float))
            rows = np.isin(atlas_names(atlases, atlas, h), areas) & (np.diff(Mh.indptr) > 0)
            col = col + np.asarray(Mh[rows].sum(0)).ravel()
            n += int(rows.sum())
        cols.append(col / max(n, 1))
        nvert.append(n)
    return np.column_stack(cols), nvert


def atlas_names(atlases, atlas, h):
    return atlases[atlas][h]


def load_region_series(path, R_mat, npy=False):
    """Stream a [TR x voxel] file and return its product with R_mat ([TR x region])."""
    if npy:
        with _open(path) as f:
            np.lib.format.read_magic(f)
            shape, _, dtype = np.lib.format.read_array_header_1_0(f)
            Y = np.frombuffer(f.read(), dtype=dtype).reshape(shape).astype(np.float64)
    else:
        with _open(path) as f, h5py.File(f, "r") as h:
            Y = np.vstack([h[c][()] for c in CONDITIONS])
    out = Y @ R_mat
    del Y
    return out


def region_weights(Z, X, S, sign_X=None):
    """Mean weight per region of each state dimension, under the three readings of the claims file.

    Z [TR x 24] PCA scores of the TRs fitted, X [TR x d] variables, S [TR x region] the
    responses averaged per region (Y R_mat). The components are C = diag(1/sqrt(w)) U^T Yc,
    with Z = U sqrt(w), so for a vector z in PC space the voxel map C^T z has region means
    Sc^T (Z / w) z. Readings: "B" the OLS weights (the code's coeffs, from S itself), "B_L"
    the denoised weights, "Q_S" the state directions. Each dimension is oriented so that its
    own state's TRs (X[:, j] > 0) have a positive mean position: along Q_S for Q_S, along the
    denoised weights for B and B_L. Returns {reading: [region x d]}.
    """
    d = X.shape[1]
    P = np.column_stack([X, np.ones(len(X))])
    pinv = np.linalg.pinv(P.T @ P)
    B = (pinv @ (P.T @ S))[:d].T  # region x d
    coef = (pinv @ (P.T @ Z))[:d]  # d x 24
    w = (Z ** 2).sum(0)
    Sc = S - S.mean(0)
    to_reg = Sc.T @ (Z / w)  # region x 24
    Q, _ = state_directions(Z, X)
    out = {"B": B, "B_L": to_reg @ coef.T, "Q_S": to_reg @ Q}
    sx = X if sign_X is None else sign_X
    for key, dirs in [("B_L", coef.T), ("Q_S", Q)]:
        p = Z @ dirs
        sg = np.array([np.sign(p[sx[:, j] > 0, j].mean() - p[:, j].mean()) if sx[:, j].any() else 1.0
                       for j in range(d)])
        if key == "B_L":
            out["B"] = out["B"] * sg
        out[key] = out[key] * sg
    return out
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 - <<'EOF'
import re
s=open('statespace.py').read()
s=s.replace("rows = np.isin(atlas_names(atlases, atlas, h), areas)","rows = np.isin(atlases[atlas][h], areas)")
s=s.replace('''

def atlas_names(atlases, atlas, h):
    return atlases[atlas][h]
''','')
open('statespace.py','w').write(s)
EOF
P=executed/zhang-2021/.venv/bin/python; time $P - <<'EOF'
import statespace as ss, numpy as np, nibabel as nib, time, os
t=time.time(); A=ss.load_atlases(); print('atlas', time.time()-t)
lab,ctab,names=nib.freesurfer.read_annot(os.environ['TMPDIR']+'/visfAtlas/FreeSurfer/lh.visfAtlas.annot')
ref=np.array([names[i].decode() if i>=0 else '' for i in lab]); ref[ref=='Unknown']=''
print('visf lh agree', (ref==A['visf']['lh']).mean())
lab,ctab,names=nib.freesurfer.read_annot(os.environ['TMPDIR']+'/lh.hcp.annot')
ref=np.array([names[i].decode()[2:-4] if i>=0 and names[i].decode().endswith('_ROI') else '' for i in lab])
print('hcp lh agree', (ref==A['hcp']['lh']).mean())
for name,(atl,areas) in {**ss.ATT_REGIONS, **ss.GAME_REGIONS}.items():
    for h in 'lh','rh':
        miss=[a for a in areas if a not in set(A[atl][h])]
        if miss: print(name,h,'missing',miss)
t=time.time(); M=ss.load_mapper('S2'); print({h:m.shape for h,m in M.items()}, time.time()-t)
R,nv=ss.region_matrix(M,A,ss.ATT_REGIONS); print(R.shape, dict(zip(ss.ATT_REGIONS,nv)), time.time()-t)
np.save(os.environ['TMPDIR']+'/R_S2.npy',R)
EOF
```

```
atlas 4.728747129440308
visf lh agree 0.08165183530474482
hcp lh agree 1.0
OPA lh missing ['TOS-places']
{'lh': (163842, 48819), 'rh': (163842, 48819)} 1.3355093002319336
(48819, 13) {'FFA': 1962, 'OFA': 703, 'EBA': 4714, 'MT+': 880, 'PPA': 2879, 'OPA': 1193, 'RSC': 2066, 'LO': 1798, 'FO': 5541, 'IFS': 2602, 'IPS': 14496, 'FEF': 1673, 'SEF': 1958} 1.3734774589538574

real	0m13.293s
user	0m8.565s
sys	0m0.427s
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; P=executed/zhang-2021/.venv/bin/python; $P - <<'EOF'
import statespace as ss, numpy as np, nibabel as nib, os, collections
f=os.environ['TMPDIR']+'/visfAtlas/FreeSurfer/lh.visfAtlas.annot'
lab,ctab,names=nib.freesurfer.read_annot(f)
print(collections.Counter(lab.tolist()).most_common(5))
print(ctab[:4])
mine=ss.parse_annot(open(f,'rb').read())
print(collections.Counter(mine.tolist()).most_common(5))
EOF
```

```
[(-1, 150464), (10, 1440), (12, 1361), (15, 1136), (6, 1035)]
[[      0       0       0       0       0]
 [    239      59      44       0 2898927]
 [    203      24      29       0 1906891]
 [    153       0      13       0  852121]]
[('Unknown', 150464), ('CoS-places', 1440), ('v1d', 1361), ('v1v', 1136), ('MTG-bodies', 1035)]
```

**Agent**

Parser agrees with nibabel (the difference is only how unlabelled vertices are named). Now testing the region weights on S2.

**Agent calls Bash**

```bash
cd entries/zhang-2021; P=executed/zhang-2021/.venv/bin/python; time $P - <<'EOF'
import statespace as ss, numpy as np, os, time, pandas as pd
R=np.load(os.environ['TMPDIR']+'/R_S2.npy')
t=time.time()
with ss._open("VisualAttention/Data/deconv/S2.hdf") as f, ss.h5py.File(f,"r") as h:
    Y=np.vstack([h[c][()] for c in ss.CONDITIONS])
print('load',time.time()-t, Y.dtype, Y.shape)
G=Y@Y.T; S=Y@R
st=ss.load_attention_states(); X=np.vstack([st[c] for c in ss.CONDITIONS])
Z,_,_=ss.pca_scores(G,np.arange(2700))
W=ss.region_weights(Z,X[:,:3],S)
# check against voxel-level direct computation
P_=np.column_stack([X,np.ones(2700)]); B=(np.linalg.pinv(P_.T@P_)@(P_.T@Y))[:3]
from sklearn.decomposition import PCA
p=PCA(24,svd_solver='full').fit(Y); C=p.components_
BL=(C.T@(C@B.T)).T
print('B check', np.abs(B@R - W['B'].T*np.sign(W['B'].T/(B@R+1e-30))).max())
print(np.round(W['B_L'].T[:2],4)); print(np.round((BL@R)[:2],4))
Q=ss.state_directions(Z,X)[0]
print(pd.DataFrame({k:np.round(v[:,0]-v[:,1],4) for k,v in W.items()}, index=list(ss.ATT_REGIONS)))
EOF
```

```
load 29.258806705474854 float64 (2700, 48819)
B check 3.3306690738754696e-16
[[ 0.3291  0.4144  0.3343  0.6638  0.2656  0.0968 -0.0319  0.5801 -0.0453
   0.1419 -0.0285  0.4783  0.3768]
 [ 0.1568  0.1815  0.4199  0.3103  0.9001  0.8743  0.2652  0.3935  0.2066
   0.357   0.6956  0.7728  0.4971]]
[[ 0.3291  0.4144  0.3343  0.6638  0.2656  0.0968 -0.0319  0.5801 -0.0453
   0.1419 -0.0285  0.4783  0.3768]
 [ 0.1568  0.1815  0.4199  0.3103  0.9001  0.8743  0.2652  0.3935  0.2066
   0.357   0.6956  0.7728  0.4971]]
          B     B_L     Q_S
FFA  0.1735  0.1723  0.0016
OFA  0.2629  0.2329  0.0021
EBA -0.0808 -0.0856 -0.0005
MT+  0.3710  0.3535  0.0033
PPA -0.6289 -0.6345 -0.0050
OPA -0.7899 -0.7776 -0.0063
RSC -0.2784 -0.2971 -0.0024
LO   0.2130  0.1866  0.0018
FO  -0.2462 -0.2519 -0.0021
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; P=executed/zhang-2021/.venv/bin/python; time $P - <<'EOF'
import statespace as ss, numpy as np, os, time, pandas as pd
A=ss.load_atlases()
st=ss.load_attention_states(); X=np.vstack([st[c] for c in ss.CONDITIONS])
res={}
for s in ss.ATT_SUBJECTS:
    R,nv=ss.region_matrix(ss.load_mapper(s),A,ss.ATT_REGIONS)
    with ss._open(f"VisualAttention/Data/deconv/{s}.hdf") as f, ss.h5py.File(f,"r") as h:
        Y=np.vstack([h[c][()] for c in ss.CONDITIONS])
    G=Y@Y.T; S=Y@R; del Y
    Z,_,_=ss.pca_scores(G,np.arange(2700))
    W=ss.region_weights(Z,X,S)
    for k,v in W.items():
        res[s,k]=pd.DataFrame(v[:,:2],index=list(ss.ATT_REGIONS),columns=['hum','veh'])
    print(s, {k: (lambda d: ((d.loc[['FFA','OFA','EBA'],'hum']>0)&(d.loc[['FFA','OFA','EBA'],'hum']>d.loc[['FFA','OFA','EBA'],'veh'])).tolist()+((d.loc[['RSC','PPA','OPA'],'veh']>0)&(d.loc[['RSC','PPA','OPA'],'veh']>d.loc[['RSC','PPA','OPA'],'hum'])).tolist())(res[s,k]) for k in W})
    print(res[s,'B'].round(3).T.to_string())
EOF
```

```
S1 {'B': [True, True, True, True, True, True], 'B_L': [True, True, True, True, True, True], 'Q_S': [True, True, False, True, True, True]}
       FFA    OFA    EBA    MT+    PPA    OPA    RSC     LO     FO    IFS    IPS    FEF    SEF
hum  0.466  0.475  0.295  0.177 -0.060 -0.042 -0.266  0.489 -0.218  0.148 -0.331  0.253  0.035
veh  0.176  0.145  0.278  0.419  0.751  0.733  0.259  0.417  0.044  0.001  0.500  0.380  0.317
S2 {'B': [True, True, False, True, True, True], 'B_L': [True, True, False, True, True, True], 'Q_S': [True, True, False, True, True, True]}
       FFA    OFA    EBA    MT+    PPA    OPA    RSC     LO     FO    IFS    IPS    FEF    SEF
hum  0.331  0.441  0.335  0.666  0.257  0.094 -0.029  0.594 -0.036  0.135 -0.020  0.478  0.387
veh  0.158  0.178  0.416  0.295  0.886  0.884  0.250  0.381  0.210  0.353  0.702  0.761  0.491
S3 {'B': [True, True, False, True, True, True], 'B_L': [True, True, False, True, True, True], 'Q_S': [True, True, True, True, True, True]}
       FFA    OFA    EBA    MT+    PPA   OPA    RSC     LO     FO    IFS    IPS    FEF    SEF
hum  0.387  0.278  0.313  0.413  0.162  0.18 -0.074  0.344  0.002  0.058  0.093  0.469  0.141
veh  0.145  0.093  0.314  0.315  0.623  0.58  0.075  0.346 -0.023  0.193  0.420  0.447  0.113
S5 {'B': [True, True, True, True, True, True], 'B_L': [True, True, True, True, True, True], 'Q_S': [True, True, True, True, True, True]}
       FFA    OFA    EBA    MT+    PPA    OPA    RSC     LO     FO    IFS    IPS    FEF    SEF
hum  0.542  0.368  0.582  0.701  0.108 -0.047 -0.175  0.407  0.055  0.145 -0.037  0.430  0.163
veh  0.103 -0.115  0.297  0.499  0.840  0.701  0.336  0.286  0.193  0.293  0.467  0.457  0.467
S6 {'B': [True, True, True, True, True, True], 'B_L': [True, True, True, True, True, True], 'Q_S': [True, True, True, True, True, True]}
       FFA    OFA    EBA    MT+    PPA    OPA    RSC     LO     FO    IFS    IPS    FEF    SEF
hum  0.735  0.472  0.512  0.872  0.128 -0.028 -0.107  0.718  0.158  0.259  0.
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
for i in [4,5,6,9,10,25]:
    for o in nb['cells'][i].get('outputs',[]):
        t=''.join(o.get('text',''))
        print('=====',i); print(t[:6000])
EOF
grep -n -i "deconvol\|wordnet\|FIR\|ridge\|semantic" paper/*.txt | head -30; ls paper
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  F=/home/runner/.claude/projects/-home-runner-work-encore-encore/b561b78a-7e67-4a9d-a830-b696571ecc52/tool-results/b64y4sk7d.txt; grep -n "semantics\|states.hdf\|Stimuli/S" $F | head; grep -n "^=====\ [569]\|^S[0-9]:\|voxels per mapper\|game voxels" $F | head -30; ls paper; grep -l -i "deconvol" paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "deconvol\|wordnet\|FIR\|ridge\|localizer\|semantic\|encoding model" paper/10.3389-fnins.2020.565976.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/zhang-2021; cat >> statespace.py <<'EOF'


def fir(F, delays=(1, 2, 3, 4)):
    """Features delayed by 1 to 4 TRs, concatenated (Methods, "Deconvolution of the
    Hemodynamic Response in the Attention Task")."""
    out = []
    for k in delays:
        D = np.zeros_like(F)
        D[k:] = F[:-k]
        out.append(D)
    return np.hstack(out)


def semantic_model_r(subject, sem, alphas=(1e1, 1e2, 1e3, 1e4, 1e5), k=10):
    """Cross-validated prediction of the raw attention BOLD by the WordNet FIR model.

    Reading (ii) of att-weights-cortex. The paper's deconvolution model: WordNet labels
    (semantics.hdf: "attentive" for the human and vehicle runs, "passive" for the passive
    runs), delayed 1 to 4 TRs within each condition, ridge regression with 10-fold
    cross-validation. Folds are contiguous tenths of each condition. One ridge parameter
    per subject, the one with the highest mean prediction correlation over voxels (the
    paper does not say how it was chosen; an assumption). Returns per-voxel correlation of
    the held-out predictions with the responses (all folds pooled) and the number of TRs.
    """
    with _open(f"VisualAttention/Data/{subject}.hdf") as f, h5py.File(f, "r") as h:
        Y = np.vstack([h[c][()].astype(np.float32) for c in CONDITIONS])
        sizes = [h[c].shape[0] for c in CONDITIONS]
    feats = {"passive": sem["passive"], "human": sem["attentive"], "vehicle": sem["attentive"]}
    X = np.vstack([fir(feats[c]) for c in CONDITIONS]).astype(np.float32)
    starts = np.cumsum([0] + sizes)
    fold_of = np.concatenate([np.array_split(np.arange(n), k) and
                              np.repeat(np.arange(k), [len(a) for a in np.array_split(np.arange(n), k)])
                              for n in sizes])
    pred = np.zeros((len(alphas),) + Y.shape, np.float32)
    for j in range(k):
        te, tr = fold_of == j, fold_of != j
        U, s, Vt = np.linalg.svd(X[tr], full_matrices=False)
        UtY = U.T @ Y[tr]
        Xte_V = X[te] @ Vt.T
        for a, alpha in enumerate(alphas):
            pred[a, te] = (Xte_V * (s / (s ** 2 + alpha))) @ UtY
    Yc = Y - Y.mean(0)
    r = []
    for a in range(len(alphas)):
        Pc = pred[a] - pred[a].mean(0)
        r.append((Pc * Yc).sum(0) / np.sqrt((Pc ** 2).sum(0) * (Yc ** 2).sum(0) + 1e-30))
    r = np.array(r)
    best = int(np.argmax(np.nanmean(r, 1)))
    return r[best], alphas[best], len(Y), np.nanmean(r, 1)
EOF
P=executed/zhang-2021/.venv/bin/python; time $P - <<'EOF'
import statespace as ss, numpy as np, time
sem=ss.read_hdf("VisualAttention/Stimuli/semantics.hdf")
t=time.time()
r,a,n,mr=ss.semantic_model_r('S2',sem)
print(time.time()-t, a, n, mr, (r>0).mean())
from scipy import stats
tt=r*np.sqrt((n-2)/(1-r**2)); p=stats.t.sf(tt,n-2); print('sig frac', (p<0.05).mean())
np.save('/tmp/claude/r_S2.npy' if False else __import__('os').environ['TMPDIR']+'/r_S2.npy', r)
import resource; print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
```

```
379.29893040657043 1000.0 5400 [0.01212115 0.01725474 0.02088877 0.02003368 0.01447   ] 0.7086380302750979
sig frac 0.40527253733177654
11.7656

real	6m23.223s
user	21m30.488s
sys	0m11.986s
```

**Agent calls Bash**

```bash
date -u
```

```
Sat Nov 14 12:42:33 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 - <<'EOF'
s=open('statespace.py').read()
i=s.index('def semantic_model_r')
s=s[:i]+'''def semantic_model_r(subject, sem, voxels, alphas=(1e1, 1e2, 1e3, 1e4, 1e5), k=10):
    """Cross-validated prediction of the raw attention BOLD by the WordNet FIR model.

    Reading (ii) of att-weights-cortex, for the voxels given (those the regions reach). The
    paper's deconvolution model (Methods, "Deconvolution of the Hemodynamic Response in the
    Attention Task"): WordNet labels (semantics.hdf: "attentive" for the human and vehicle
    runs, "passive" for the passive runs), delayed 1 to 4 TRs within each condition, ridge
    regression with 10-fold cross-validation. Folds are contiguous tenths of each condition.
    One ridge parameter per subject, the one with the highest mean prediction correlation
    over these voxels (the paper does not say how it was chosen; an assumption). Returns the
    per-voxel correlation of the held-out predictions (all folds pooled) with the responses,
    the ridge parameter, the number of TRs and the mean correlation per ridge parameter.
    """
    with _open(f"VisualAttention/Data/{subject}.hdf") as f, h5py.File(f, "r") as h:
        Y = np.vstack([h[c][()][:, voxels].astype(np.float32) for c in CONDITIONS])
        sizes = [h[c].shape[0] for c in CONDITIONS]
    feats = {"passive": sem["passive"], "human": sem["attentive"], "vehicle": sem["attentive"]}
    X = np.vstack([fir(feats[c]) for c in CONDITIONS]).astype(np.float32)
    fold_of = np.concatenate([np.repeat(np.arange(k), [len(a) for a in np.array_split(np.arange(n), k)])
                              for n in sizes])
    pred = np.zeros((len(alphas),) + Y.shape, np.float32)
    for j in range(k):
        te, tr = fold_of == j, fold_of != j
        U, s, Vt = np.linalg.svd(X[tr], full_matrices=False)
        UtY = U.T @ Y[tr]
        Xte_V = X[te] @ Vt.T
        for a, alpha in enumerate(alphas):
            pred[a, te] = (Xte_V * (s / (s ** 2 + alpha))) @ UtY
    Yc = Y - Y.mean(0)
    r = np.array([((P - P.mean(0)) * Yc).sum(0) /
                  np.sqrt(((P - P.mean(0)) ** 2).sum(0) * (Yc ** 2).sum(0) + 1e-30) for P in pred])
    best = int(np.argmax(r.mean(1)))
    return r[best], alphas[best], len(Y), r.mean(1)
'''
open('statespace.py','w').write(s)
EOF
P=executed/zhang-2021/.venv/bin/python; time $P - <<'EOF'
import statespace as ss, numpy as np, time, os, resource
R=np.load(os.environ['TMPDIR']+'/R_S2.npy')
vox=np.nonzero((R[:, :7]!=0).any(1))[0]; print(len(vox), R.shape)
sem=ss.read_hdf("VisualAttention/Stimuli/semantics.hdf")
t=time.time()
r,a,n,mr=ss.semantic_model_r('S2',sem,vox)
print(time.time()-t, a, n, mr)
rfull=np.load(os.environ['TMPDIR']+'/r_S2.npy'); print('agree with full run', np.abs(rfull[vox]-r).max())
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
```

```
2303 (48819, 13)
248.25493097305298 10000.0 5400 [0.03263165 0.05054802 0.06546669 0.06603947 0.05904297]
agree with full run 0.047547854
4.31408

real	4m11.539s
user	13m6.955s
sys	0m7.734s
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; P=executed/zhang-2021/.venv/bin/python; $P - <<'EOF'
import statespace as ss, numpy as np, time
t=time.time()
with ss._open("VisualAttention/Data/S2.hdf") as f, ss.h5py.File(f,"r") as h:
    for c in ss.CONDITIONS: print(c, h[c].chunks, h[c].compression)
    Y=h['passive'][()]
print('passive read', time.time()-t)
sem=ss.read_hdf("VisualAttention/Stimuli/semantics.hdf")
X=ss.fir(sem['passive']).astype(np.float32)
t=time.time(); np.linalg.svd(X[:3240],full_matrices=False); print('svd',time.time()-t)
t=time.time(); w,V=np.linalg.eigh(X.T@X); print('eigh',time.time()-t)
EOF
```

```
passive None None
human None None
vehicle None None
passive read 34.325093507766724
svd 9.9432053565979
eigh 4.5652384757995605
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 - <<'EOF'
s=open('statespace.py').read()
old='''        U, s, Vt = np.linalg.svd(X[tr], full_matrices=False)
        UtY = U.T @ Y[tr]
        Xte_V = X[te] @ Vt.T
        for a, alpha in enumerate(alphas):
            pred[a, te] = (Xte_V * (s / (s ** 2 + alpha))) @ UtY'''
new='''        Xtr = X[tr].astype(np.float64)
        s2, V = np.linalg.eigh(Xtr.T @ Xtr)  # ridge in the eigenbasis of X^T X
        VtXtY = (V.T @ (Xtr.T @ Y[tr])).astype(np.float32)
        Xte_V = (X[te] @ V).astype(np.float32)
        for a, alpha in enumerate(alphas):
            pred[a, te] = (Xte_V / (np.clip(s2, 0, None) + alpha).astype(np.float32)) @ VtXtY'''
assert old in s; s=s.replace(old,new); open('statespace.py','w').write(s)
EOF
P=executed/zhang-2021/.venv/bin/python; time $P - <<'EOF'
import statespace as ss, numpy as np, time, os
R=np.load(os.environ['TMPDIR']+'/R_S2.npy')
vox=np.nonzero((R[:, :7]!=0).any(1))[0]
sem=ss.read_hdf("VisualAttention/Stimuli/semantics.hdf")
t=time.time(); r,a,n,mr=ss.semantic_model_r('S2',sem,vox); print(time.time()-t, a, mr)
rfull=np.load(os.environ['TMPDIR']+'/r_S2.npy'); print('vs svd run (alpha 1e3)', np.abs(rfull[vox]-r).max())
EOF
```

```
121.45039391517639 10000.0 [0.03263165 0.05054802 0.06546669 0.06603947 0.05904297]
vs svd run (alpha 1e3) 0.047547832

real	2m4.681s
user	5m4.729s
sys	0m6.362s
```

**Agent**

(ii) now runs in about 2 minutes per subject, restricted to the voxels the regions reach. Wiring the loaders to keep those voxels.

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 - <<'EOF'
s=open('statespace.py').read()
old='''def load_attention_gram(subject, X_check=None):
    """Stream one subject's deconvolved responses, stacked passive, human, vehicle.

    Returns the 2700 x 2700 Gram matrix and summaries; the voxel data are
    dropped. With X_check, also the positions from the paper's code on the full
    voxel data.
    """
    with _open(f"VisualAttention/Data/deconv/{subject}.hdf") as f, h5py.File(f, "r") as h:
        Y = np.vstack([h[c][()] for c in CONDITIONS])
    out = gram_summary(Y)
    if X_check is not None:
        out["code_positions"] = code_positions(X_check, Y)
    del Y'''
new='''def load_attention_gram(subject, X_check=None, keep=None):
    """Stream one subject's deconvolved responses, stacked passive, human, vehicle.

    Returns the 2700 x 2700 Gram matrix and summaries; the voxel data are
    dropped. With X_check, also the positions from the paper's code on the full
    voxel data and the norm of each row of its OLS coefficients (`coeffs`, voxel
    space). With keep, also the responses of those voxels (float32).
    """
    with _open(f"VisualAttention/Data/deconv/{subject}.hdf") as f, h5py.File(f, "r") as h:
        Y = np.vstack([h[c][()] for c in CONDITIONS])
    out = gram_summary(Y)
    if X_check is not None:
        out["code_positions"] = code_positions(X_check, Y)
        P = np.column_stack([X_check, np.ones(len(X_check))])
        out["code_coef_norm"] = np.linalg.norm(np.linalg.pinv(P.T @ P) @ (P.T @ Y), axis=1)
    if keep is not None:
        out["Y_keep"] = Y[:, keep].astype(np.float32)
    del Y'''
assert old in s; s=s.replace(old,new)
old='''def load_game(subject):
    """Stream one subject's video game BOLD (npy) and its state labels."""
    with _open(f"VideoGame/Data/{subject}.npy") as f:
        np.lib.format.read_magic(f)
        shape, fortran, dtype = np.lib.format.read_array_header_1_0(f)
        Y = np.frombuffer(f.read(), dtype=dtype).reshape(shape).astype(np.float64)
    out = gram_summary(Y)
    del Y
    st = read_hdf(f"VideoGame/Stimuli/{subject}.hdf")
    out["X"] = st["behavioural_state"].astype(float)
    out["labels"] = [s.decode().strip().lower() for s in st["state_labels"]]
    return out'''
new='''def load_game(subject, keep=None):
    """Stream one subject's video game BOLD (npy) and its state labels.

    Also the voxel maps of the OLS weights B and denoised weights B_L of every state (data
    set column order, states with no TRs dropped), for the correlation variant of
    game-weights-two-groups, and with keep the responses of those voxels (float32).
    """
    with _open(f"VideoGame/Data/{subject}.npy") as f:
        np.lib.format.read_magic(f)
        shape, fortran, dtype = np.lib.format.read_array_header_1_0(f)
        Y = np.frombuffer(f.read(), dtype=dtype).reshape(shape).astype(np.float64)
    out = gram_summary(Y)
    st = read_hdf(f"VideoGame/Stimuli/{subject}.hdf")
    out["X"] = st["behavioural_state"].astype(float)
    out["labels"] = [s.decode().strip().lower() for s in st["state_labels"]]
    X, names = game_matrix(out["X"], out["labels"], "dataset")
    Z, _, _ = pca_scores(out["G"], np.arange(len(Y)))
    P = np.column_stack([X, np.ones(len(X))])
    pinv = np.linalg.pinv(P.T @ P)
    coef = (pinv @ (P.T @ Z))[:-1]
    out["B_vox"] = (pinv @ (P.T @ Y))[:-1]
    out["BL_vox"] = ((Y - Y.mean(0)).T @ ((Z / (Z ** 2).sum(0)) @ coef.T)).T
    out["map_names"] = names
    if keep is not None:
        out["Y_keep"] = Y[:, keep].astype(np.float32)
    del Y
    return out'''
assert old in s; s=s.replace(old,new)
s += '''

def cv_ols_r(Y, X, k=10):
    """Per-voxel correlation of cross-validated OLS predictions (with intercept) with the
    responses, 10 contiguous folds pooled: reading (ii) of game-weights-two-groups, the
    nine-state model as the encoding model (claims file)."""
    P = np.column_stack([X, np.ones(len(X))])
    pred = np.zeros(Y.shape, np.float64)
    for te in np.array_split(np.arange(len(Y)), k):
        tr = np.setdiff1d(np.arange(len(Y)), te)
        W = np.linalg.pinv(P[tr].T @ P[tr]) @ (P[tr].T @ Y[tr])
        pred[te] = P[te] @ W
    Pc, Yc = pred - pred.mean(0), Y - Y.mean(0)
    return (Pc * Yc).sum(0) / np.sqrt((Pc ** 2).sum(0) * (Yc ** 2).sum(0) + 1e-30)


def r_pvalue(r, n):
    """One-sided p of a correlation above zero, from the t distribution with n - 2 df."""
    from scipy import stats
    r = np.clip(r, -0.999999, 0.999999)
    return stats.t.sf(r * np.sqrt((n - 2) / (1 - r ** 2)), n - 2)
'''
open('statespace.py','w').write(s)
EOF
grep -n "import" statespace.py | head
```

```
37:import fsspec
38:import h5py
39:import numpy as np
40:from scipy import linalg
104:    from scipy import stats
105:    from sklearn.decomposition import PCA
483:    import io
508:    import hashlib, io, zipfile
509:    import requests
525:    from scipy import sparse
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
s=open('entries/zhang-2021/statespace.py').read()
i=s.index('def load_region_series'); j=s.index('def region_weights')
s=s[:i]+s[j:]; open('entries/zhang-2021/statespace.py','w').write(s)
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    for o in c.get('outputs',[]):
        t=''.join(o.get('text',''))
        for l in t.splitlines():
            if 'elapsed' in l or 'done in' in l: print(i,l)
for i in [22,25,34,42]:
    pass
EOF
```

```
9 elapsed 238 s, peak memory 4.3 GB
13 S1 done in 44 s
13 S2 done in 44 s
13 S3 done in 44 s
13 S5 done in 44 s
13 S6 done in 44 s
13 elapsed 458 s, peak memory 4.3 GB
25 elapsed 873 s
28 S1 done in 76 s
28 S2 done in 76 s
28 S3 done in 75 s
28 S5 done in 75 s
28 S6 done in 75 s
28 elapsed 1250 s
33 elapsed 1339 s
36 elapsed 1440 s
42 S1 done in 126 s
42 S7 done in 88 s
42 elapsed 1654 s, peak memory 4.3 GB
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 - <<'EOF'
import json
nb=json.load(open('reproduce_zhang_2021.ipynb'))
for i in [12,17,20,23,24,26,27,29,31,34,37,40,41,43]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
EOF
```

```
===== 12
## Attention task: CSI per subject and condition

Shared by fig1-csi-s2, att-csi-group and supp-csi-per-subject. The CSI of the four presence
clusters within each condition, in the state space fitted once on the three conditions stacked.
Because the third axis is undefined in these data, three readings are computed:

- R3, "code": the paper's code run as written on the full voxel data (its third axis is whatever
  rounding gives on this machine);
- R2, "random third axis": the median over 100 random third axes, orthogonal to the human and
  vehicle axes in the space of the 24 PCs (the distribution of what an arbitrary third axis gives);
- R1, "2D": the human-vehicle plane alone.

CSI values are means over 10 Monte Carlo seeds. The null refits the state space with permuted
presence labels, 1000 times per reading of the claims file: (a) the (human, vehicle) rows shuffled
over all TRs, and (b) circularly shifted by a random lag within each condition. Each null draw uses
a random third axis (for R3 and R2) or the plane (for R1) and one Monte Carlo seed.
===== 17
**Result: reproduced, resting on an assumption about the third axis.** With the paper's code (R3)
the S2 CSIs are 0.740 (attend-humans), 0.718 (attend-vehicles) and 0.676 (passive), all within
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/zhang-2021; python3 - <<'EOF'
s=open('statespace.py').read()
old='''    "SEF": ("hcp", ["SCEF"]),
}
_PFC'''
new='''    "SEF": ("hcp", ["SCEF"]),
    # variants of the body, face and place areas, not used by the criterion
    "LOS-bodies": ("visf", ["LOS-bodies"]),
    "ITG-bodies": ("visf", ["ITG-bodies"]),
    "MTG-bodies": ("visf", ["MTG-bodies"]),
    "OTS-bodies": ("visf", ["OTS-bodies"]),
    "FFC (HCP)": ("hcp", ["FFC"]),
    "PHA1-3 (HCP)": ("hcp", ["PHA1", "PHA2", "PHA3"]),
    "POS1 (HCP)": ("hcp", ["POS1"]),
}
_PFC'''
assert old in s; s=s.replace(old,new); open('statespace.py','w').write(s)
EOF
```

```
Sat Nov 14 12:51:45 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; cat > $TMPDIR/edit1.py <<'PYEOF'
import json
p='reproduce_zhang_2021.ipynb'
nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source']=s.splitlines(keepends=True)
def code(s, tags=None):
    c={"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":s.splitlines(keepends=True)}
    if tags: c["metadata"]["tags"]=tags
    return c
def md(s): return {"cell_type":"markdown","metadata":{},"source":s.splitlines(keepends=True)}
def rep(i, old, new):
    s=src(i); assert old in s, (i, old); setsrc(i, s.replace(old, new))

# cell 6: keep voxels, code coef norms
rep(6, 'd = ss.load_attention_gram(s, X_check=X_att)', 'd = ss.load_attention_gram(s, X_check=X_att, keep=att_keep[s])')
rep(6, 'att[s] = dict(G=G, Z=Z, code_pos=cp, ve=ve, n_vox=d["n_vox"])', 'att[s] = dict(G=G, Z=Z, code_pos=cp, ve=ve, n_vox=d["n_vox"], Y_keep=d["Y_keep"])')
rep(6, '''f"{np.linalg.norm(coef[1]):.3g}, attention {np.linalg.norm(coef[2]):.3g}; |r|''', '''f"{np.linalg.norm(coef[1]):.3g}, attention {np.linalg.norm(coef[2]):.3g}; the code's own OLS coefficients in voxel space, norm per row "
          f"(human, vehicle, attention, intercept) {np.array2string(d['code_coef_norm'], precision=3)}; |r|''')
# cell 9: game keep + old mappers + run structure
rep(9, 'g = ss.load_game(s)', 'g = ss.load_game(s, keep=game_keep.get(s))')
rep(9, 'print("voxels per mapper:", mapper_vox)', '''print("voxels per mapper:", mapper_vox)
old_vox = {f"old/S{i}": ss.read_hdf(f"Mappers/old/S{i}.hdf", ["vox_to_fsavg_left_shape"])["vox_to_fsavg_left_shape"][1] for i in (1, 5, 6)}
print("voxels per superseded mapper (Mappers/old, see its README):", old_vox)''')
regions_cell = code('''# Cortical regions on fsaverage, for att-weights-cortex and game-weights-two-groups. The paper's ROIs are
# not public; two public atlases on fsaverage are read into memory and checked against their published
# checksums (visfAtlas, Rosenke et al. 2021; HCP-MMP1.0, Glasser et al. 2016, on fsaverage), and mapped
# to each subject's voxels with the data set's own mappers. A region's mean of a voxel map is the mean
# over the region's fsaverage vertices that the mapper reaches (helper, region_matrix).
atlases = ss.load_atlases()
mappers = {s: ss.load_mapper(s) for s in ss.ATT_SUBJECTS + ["S7"]}
regmat, regvert = {}, {}
for s in ss.ATT_SUBJECTS:
    regmat[s], regvert[s] = ss.region_matrix(mappers[s], atlases, ss.ATT_REGIONS)
regmat["game", "S7"], regvert["game", "S7"] = ss.region_matrix(mappers["S7"], atlases, ss.GAME_REGIONS)
print("fsaverage vertices per region (both hemispheres) in each atlas:",
      {k: int(sum(np.isin(atlases[a][h], areas).sum() for h in ("lh", "rh"))) for k, (a, areas) in {**ss.ATT_REGIONS, **ss.GAME_REGIONS}.items()})
print("vertices per region that each subject's mapper reaches (attention regions):")
print(pd.DataFrame({s: regvert[s] for s in ss.ATT_SUBJECTS}, index=list(ss.ATT_REGIONS)).T.to_string())
print("S7, video game regions:", dict(zip(ss.GAME_REGIONS, regvert["game", "S7"])))
att_keep = {s: np.nonzero((regmat[s] != 0).any(1))[0] for s in ss.ATT_SUBJECTS}
game_keep = {"S7": np.nonzero((regmat["game", "S7"] != 0).any(1))[0]}
print("voxels the regions reach:", {s: len(v) for s, v in att_keep.items()}, "| S7 video game:", len(game_keep["S7"]))''', ["sanity"])
runs_cell = code('''# Run structure of the video game data: the correlation of consecutive TRs' voxel patterns, whose
# lowest values mark where runs were joined (asked by the verifier, to see whether S1's 65 min are part
# of a 90-min session). The paper's runs are 325 volumes with 10 discarded at each end (305 TRs).
for s in ss.GAME_SUBJECTS:
    G = game[s]["G"]
    nrm = np.sqrt(np.diag(G))
    c = np.array([G[t, t + 1] / nrm[t] / nrm[t + 1] for t in range(len(G) - 1)])
    low = np.sort(np.argsort(c)[:8]) + 1
    print(f"{s}: {len(G)} TRs; consecutive-TR correlation median {np.median(c):.3f}, 1st percentile {np.percentile(c, 1):.3f}; "
          f"the 8 lowest at the start of TRs {low.tolist()} (values {np.round(c[low - 1], 3).tolist()}); "
          f"gaps between them {np.diff(np.concatenate([[0], low, [len(G)]])).tolist()}")''', ["sanity"])

# att-passive-lower: keep nulls and print quantiles
rep(25, 'pl_rows = []', 'pl_rows, pl_null = [], {}')
rep(25, '                null = np.array(null)\n', '                null = np.array(null)\n                pl_null[s, variant, scheme, refit] = null\n')
rep(25, 'print(f"elapsed {time.time()-T0:.0f} s")', '''print("\\nnull distribution of d_mean (mean attentive CSI minus passive), R3: observed and null quantiles")
for s in ss.ATT_SUBJECTS:
    for scheme in ["matched", "global"]:
        for refit in ["i", "ii"]:
            q = np.percentile(pl_null[s, "R3", scheme, refit][:, 2], [50, 95, 99, 100])
            obs = pl[(pl.subject == s) & (pl.variant == "R3") & (pl.scheme == scheme) & (pl.null == refit)].d_mean.iloc[0]
            print(f"  {s} {scheme:7s} null {refit:2s}: observed {obs:.4f}; null median {q[0]:.4f}, 95% {q[1]:.4f}, 99% {q[2]:.4f}, max {q[3]:.4f}")
print(f"elapsed {time.time()-T0:.0f} s")''')

# game-csi lag +1 variant cell
lag_csi = code('''# Variant (asked by the verifier): labels moved one TR later (BOLD at TR t+1 paired with the state at t),
# since the game data are not deconvolved. 200 permutations per reading.
rng = np.random.default_rng(41)
for s in ss.GAME_SUBJECTS:
    X, names = ss.game_matrix(game[s]["X"], game[s]["labels"], "dataset")
    X1 = np.roll(X, 1, axis=0)
    X1[0] = 0
    Z = game[s]["Z"]
    pos = ss.positions(Z, X1)
    for reading in "abc":
        mem, nm, dropped = ss.game_members(X1, names, reading)
        v = np.mean([ss.csi(pos, mem, np.random.default_rng(k)) for k in range(10)])
        null = np.array([ss.csi(ss.positions(Z, Xp), ss.game_members(Xp, names, reading)[0], rng)
                         for Xp in (X1[rng.permutation(len(X1))] for _ in range(200))])
        e, tol = exp_g[s]
        print(f"{s} lag +1 reading {reading}: CSI {v:.3f} (lag 0: {game_csi[s, reading]:.3f}); expected {e} +/- {tol}, "
              f"within: {abs(v - e) <= tol}; null max {null.max():.3f}; above every null value: {v > null.max()}")''', ["claim:game-csi"])

# game-classification: refactor into function, fix class drop (B7), add lag +1 variant
s42 = src(42)
s42 = s42.replace('''rng = np.random.default_rng(6)
gc_rows, gc_null = [], {}
for s in ss.GAME_SUBJECTS:
    t = time.time()
    X, names = ss.game_matrix(game[s]["X"], game[s]["labels"], "dataset")
''', '''def game_classification(s, X, names, rng, n_perm):
    gc_rows, gc_null = [], {}
''')
assert 'def game_classification' in s42
# indent body by 4 after function def: lines from "    n, d = X.shape" until "    print(f\\"{s} done"
lines = s42.splitlines()
out=[]; inside=False
for l in lines:
    if l.startswith('def game_classification'):
        out.append(l); inside=True; continue
    if inside and l.startswith('    gc_rows, gc_null'):
        out.append(l); continue
    if inside and l.startswith('    print(f"{s} done in'):
        out.append('    return gc_rows, gc_null'); inside=False; continue
    if inside:
        out.append(('    ' + l) if l.strip() else l)
    else:
        out.append(l)
s42='\n'.join(out)
s42 = s42.replace('                null = np.array([run(rng).mean() for _ in range(N_PERM_CLF)])',
                  '                null = np.array([run(rng).mean() for _ in range(n_perm)])')
s42 = s42.replace("p=(1 + (null >= accs.mean()).sum()) / (N_PERM_CLF + 1)))", "p=(1 + (null >= accs.mean()).sum()) / (n_perm + 1)))")
# B7: score only classes kept in the fold
old7 = '''                            pred = ss.nearest_cluster(ptr, lab_tr, pte[m], cl, rule)
'''
new7 = '''                            pred = ss.nearest_cluster(ptr, lab_tr, pte[m], cl, rule)
                            # score only the classes this fold could predict (a class too small to fit
                            # in this fold would otherwise count with a recall of 0)
                            accs.append(ss.balanced_accuracy(H[:, [classes.index(c) for c in cl]], pred, cl))
                            continue
'''
assert old7 in s42; s42 = s42.replace(old7, new7)
s42 = s42.replace('gcl = pd.DataFrame(gc_rows)', '''rng = np.random.default_rng(6)
gc_rows, gc_null = [], {}
for s in ss.GAME_SUBJECTS:
    t = time.time()
    X, names = ss.game_matrix(game[s]["X"], game[s]["labels"], "dataset")
    r_, n_ = game_classification(s, X, names, rng, N_PERM_CLF)
    gc_rows += r_
    gc_null.update(n_)
    print(f"{s} done in {time.time()-t:.0f} s")
gcl = pd.DataFrame(gc_rows)''')
setsrc(42, s42)
lag_clf = code('''# Variant (asked by the verifier): labels moved one TR later, 200 permutations per reading.
rng = np.random.default_rng(61)
rows = []
for s in ss.GAME_SUBJECTS:
    X, names = ss.game_matrix(game[s]["X"], game[s]["labels"], "dataset")
    X1 = np.roll(X, 1, axis=0)
    X1[0] = 0
    rows += game_classification(s, X1, names, rng, 200)[0]
g1 = pd.DataFrame(rows)
g1["within"] = [abs(r.bal_acc - exp_c[r.subject][0]) <= exp_c[r.subject][1] for r in g1.itertuples()]
g1["above_null"] = g1.bal_acc > g1.null_max
print(g1.drop(columns=["left_out"]).round(4).to_string(index=False))
print("readings at lag +1 where both subjects are within tolerance and above every null value:")
print(g1.groupby(["folds", "labels", "rule"]).apply(lambda g: bool((g.within & g.above_null).all()), include_groups=False).to_string())''', ["claim:game-classification"])

# fig3b centred p (B8)
s39 = src(39)
s39 = s39.replace('''    p = (1 + (np.abs(null) >= np.abs(M)[None]).sum(0)) / (N_PERM_G + 1)
    off = ~np.eye(d, dtype=bool)
    for bonf, ntest in [("a", d * (d - 1)), ("b", d * d)]:''', '''    p0 = (1 + (np.abs(null) >= np.abs(M)[None]).sum(0)) / (N_PERM_G + 1)
    # centred on the null's mean (asked by the verifier): rows are permuted together, so the null of a pair
    # of mutually exclusive states is not centred on zero
    mu = null.mean(0)
    pc = (1 + (np.abs(null - mu) >= np.abs(M - mu)[None]).sum(0)) / (N_PERM_G + 1)
    off = ~np.eye(d, dtype=bool)
    for centre, p, bonf, ntest in [(c_, p_, b_, n_) for c_, p_ in [("zero", p0), ("null mean", pc)]
                                   for b_, n_ in [("a", d * (d - 1)), ("b", d * d)]]:''')
s39 = s39.replace('''        res3b[s, order, sign, bonf] = (sig, names)
        print(f"{s} order {order:7s} sign {sign:4s} Bonferroni {bonf}''', '''        res3b[s, order, sign, bonf, centre] = (sig, names)
        print(f"{s} order {order:7s} sign {sign:4s} centre {centre:9s} Bonferroni {bonf}''')
s39 = s39.replace('''        for bonf in "ab":
            s1, n1 = res3b["S1", order, sign, bonf]
            s7, n7 = res3b["S7", order, sign, bonf]''', '''        for bonf, centre in [(b_, c_) for b_ in "ab" for c_ in ["zero", "null mean"]]:
            s1, n1 = res3b["S1", order, sign, bonf, centre]
            s7, n7 = res3b["S7", order, sign, bonf, centre]''')
s39 = s39.replace('''            print(f"order {order:7s} sign {sign:4s} Bonferroni {bonf}: S1''', '''            print(f"order {order:7s} sign {sign:4s} centre {centre:9s} Bonferroni {bonf}: S1''')
s39 = s39.replace('sig, names = res3b[s, "table1", "own", "a"]', 'sig, names = res3b[s, "table1", "own", "a", "zero"]')
setsrc(39, s39)

# att-weights-cortex: replace cell 30
aw_md = md(open('/dev/stdin').read()) if False else None
PYEOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; cat >> $TMPDIR/edit1.py <<'PYEOF'
aw_md = md('''### att-weights-cortex

> The human-presence dimension of the attention-task state space has its weights in face and body
> areas (FFA, OFA, EBA), MT+, LO, the frontal operculum and the inferior frontal sulcus; the
> vehicle-presence dimension in RSC, PPA, OPA, IPS, FEF and around the inferior frontal sulcus.

The paper drew its ROIs per subject from functional localizer and retinotopic mapping data
(Methods, Preprocessing and Visualization, paragraph 2), which are not public. The claims file
lets the author use an outside source, naming an fsaverage atlas through the data set's mappers,
and that is done here (an assumption: group atlas regions in place of each subject's localizer
ROIs). The category areas come from visfAtlas (Rosenke et al. 2021), whose authors relate its
fusiform face areas (mFus, pFus) to the FFA, its lateral body areas (LOS, ITG, MTG) to the EBA and
CoS-places to the PPA; IOG-faces is taken as the OFA and TOS-places (right hemisphere only) as the
OPA. RSC, LO, FO, IFS, IPS, FEF and SEF come from HCP-MMP1.0 (Glasser et al. 2016) on fsaverage.
Other definitions of the body, face and place areas are shown as variants.

Weights, the readings of the claims file: (a) the OLS weights B, (b) the denoised weights B_L,
(c) the state directions Q_S, each oriented so that its own state's TRs have a positive mean
position. They are computed exactly from the region-averaged responses and the PCA of all voxels
(helper, region_weights). Thresholds: (i) none; (ii) voxels whose prediction by the WordNet FIR
model (delays 1 to 4, ridge, 10 contiguous folds per condition, on the non-deconvolved BOLD of the
three conditions) correlates with the response at one-sided p < 0.05 uncorrected (t test of r),
computed for the voxels the regions reach. Per subject and region, the mean weight over the
region's vertices. A subject counts when the human-presence weight is positive and above the
vehicle-presence weight in FFA, OFA and EBA, and the reverse in RSC, PPA and OPA; 4 of 5 subjects
are needed under a reading.''')
aw_code1 = code('''aw_rows, sem_fit = [], {}
for s in ss.ATT_SUBJECTS:
    t = time.time()
    r, alpha, n, mean_r = ss.semantic_model_r(s, sem, att_keep[s])
    p = ss.r_pvalue(r, n)
    sig = np.zeros(regmat[s].shape[0], bool)
    sig[att_keep[s][p < 0.05]] = True
    R_thr, nv_thr = ss.region_matrix(mappers[s], atlases, ss.ATT_REGIONS, voxel_mask=sig)
    sem_fit[s] = dict(alpha=alpha, n_vox=len(att_keep[s]), n_sig=int(sig.sum()))
    Yk = att[s]["Y_keep"].astype(np.float64)
    for thr, R in [("i", regmat[s]), ("ii", R_thr)]:
        W = ss.region_weights(att[s]["Z"], X_att, Yk @ R[att_keep[s]])
        for reading, w in W.items():
            for k, reg in enumerate(ss.ATT_REGIONS):
                aw_rows.append(dict(subject=s, threshold=thr, weights=reading, region=reg, human=w[k, 0], vehicle=w[k, 1]))
    print(f"{s}: WordNet model ridge parameter {alpha:g} (mean r per parameter {np.round(mean_r, 4).tolist()}), "
          f"{n} TRs; {sig.sum()} of {len(att_keep[s])} region voxels significant at p < 0.05 "
          f"({sig.sum() / len(att_keep[s]):.0%}); vertices per region after the threshold "
          f"{dict(zip(ss.ATT_REGIONS, nv_thr))}; {time.time()-t:.0f} s, peak memory {mem_gb():.1f} GB")
aw = pd.DataFrame(aw_rows)''', ["claim:att-weights-cortex"])
aw_code2 = code('''HUM, VEH = ["FFA", "OFA", "EBA"], ["RSC", "PPA", "OPA"]
def region_ok(g, reg, dim):
    h, v = g.loc[reg, "human"], g.loc[reg, "vehicle"]
    return (h > 0 and h > v) if dim == "human" else (v > 0 and v > h)
rows = []
for (s, thr, reading), g in aw.groupby(["subject", "threshold", "weights"]):
    g = g.set_index("region")
    fails = [r for r in HUM if not region_ok(g, r, "human")] + [r for r in VEH if not region_ok(g, r, "vehicle")]
    rows.append(dict(subject=s, threshold=thr, weights=reading, holds=not fails, failing_regions=fails))
awc = pd.DataFrame(rows)
print(awc.to_string(index=False))
print("\\nsubjects of 5 in which the pattern holds, per reading (4 needed):")
print(awc.groupby(["threshold", "weights"]).holds.sum().to_string())
print("\\nsubjects of 5 in which each region has the expected dimension positive and larger:")
cnt = {}
for (thr, reading), g in aw.groupby(["threshold", "weights"]):
    cnt[thr, reading] = {reg: int(sum(region_ok(gs.set_index("region"), reg, dim) for _, gs in g.groupby("subject")))
                         for reg, dim in [(r, "human") for r in HUM + ["MT+", "LO", "FO", "IFS", "SEF", "LOS-bodies", "ITG-bodies",
                                                                       "MTG-bodies", "OTS-bodies", "FFC (HCP)"]] +
                                         [(r, "vehicle") for r in VEH + ["IPS", "FEF", "IFS", "FO", "PHA1-3 (HCP)", "POS1 (HCP)"]]}
print(pd.DataFrame(cnt).to_string())
print("\\nmean weights, threshold (i), OLS weights B (human / vehicle):")
t_ = aw[(aw.threshold == "i") & (aw.weights == "B")]
print(t_.assign(hv=[f"{h:+.3f} / {v:+.3f}" for h, v in zip(t_.human, t_.vehicle)])
      .pivot(index="region", columns="subject", values="hv").loc[list(ss.ATT_REGIONS)].to_string())
print("\\nrange of every mean weight shown:", {k: (round(float(g[["human", "vehicle"]].min().min()), 4), round(float(g[["human", "vehicle"]].max().max()), 4))
                                            for k, g in aw.groupby("weights")})''', ["claim:att-weights-cortex"])

gw_md = md('''### game-weights-two-groups

> The video game state dimensions fall into two groups, dead, round start, safe explore, unsafe
> explore and flash in TPJ, precuneus and prefrontal cortex (default-mode areas), and kill, engage
> close, engage far and run away in motor, premotor and supplementary motor areas, IPS, FEF and
> SEF; the weights are largely consistent across the two subjects.

S1's video game data (73,594 voxels) match no mapper in the data set (current or superseded, data
check), so S1's weights cannot be placed on the cortex: only S7 can be tested by region, and the
consistency between subjects cannot be measured. Regions from HCP-MMP1.0 on fsaverage (the
assumption of att-weights-cortex; the areas of each region are listed in the helper): TPJ,
precuneus and prefrontal cortex for the first group; motor, premotor and supplementary motor
cortex, IPS, FEF and SEF for the second. Weights as in att-weights-cortex, Q_S under both orders
of the variables. Thresholds: (i) none; (ii) voxels whose prediction by the nine-state OLS model
(10 contiguous folds) correlates with the response at one-sided p < 0.05 Bonferroni-corrected over
all of the subject's voxels.

A dimension of the first group counts when its mean weight is positive in each of TPJ, precuneus
and prefrontal cortex and the mean over these three regions is above the mean over the six
regions of the second group; a dimension of the second group, the reverse. One dimension may
fail. A stricter variant asks every own region to be above every other region.''')
gw_code1 = code('''G1, G2 = ["dead", "round start", "safe explore", "unsafe explore", "flash"], ["kill", "engage close", "engage far", "run away"]
R1_, R2_ = ["TPJ", "precuneus", "prefrontal"], ["motor", "premotor", "SMA", "IPS", "FEF", "SEF"]
s = "S7"
X7, names7 = ss.game_matrix(game[s]["X"], game[s]["labels"], "dataset")
Yk = game[s]["Y_keep"].astype(np.float64)
r7 = ss.cv_ols_r(Yk, X7)
p7 = ss.r_pvalue(r7, len(X7))
sig7 = np.zeros(game[s]["n_vox"], bool)
sig7[game_keep[s][p7 < 0.05 / game[s]["n_vox"]]] = True
R_thr7, nv_thr7 = ss.region_matrix(mappers[s], atlases, ss.GAME_REGIONS, voxel_mask=sig7)
print(f"{s}: {sig7.sum()} of {len(game_keep[s])} region voxels significant (Bonferroni over {game[s]['n_vox']}); "
      f"vertices per region after the threshold {dict(zip(ss.GAME_REGIONS, nv_thr7))}")
gw_rows = []
for thr, R in [("i", regmat["game", s]), ("ii", R_thr7)]:
    S = Yk @ R[game_keep[s]]
    for order in ["dataset", "table1"]:
        Xo, nameso = ss.game_matrix(game[s]["X"], game[s]["labels"], order)
        W = ss.region_weights(game[s]["Z"], Xo, S)
        for reading, w in W.items():
            if reading != "Q_S" and order == "table1":
                continue  # B and B_L do not depend on the order
            for j, st_ in enumerate(nameso):
                for k, reg in enumerate(ss.GAME_REGIONS):
                    gw_rows.append(dict(threshold=thr, weights=reading if reading != "Q_S" else f"Q_S ({order})",
                                        state=st_, region=reg, w=w[k, j]))
gw = pd.DataFrame(gw_rows)
tab = gw[(gw.threshold == "i") & (gw.weights == "B")].pivot(index="state", columns="region", values="w")
print("\\nS7 mean weights, threshold (i), OLS weights B:")
print(tab.loc[[x for x in G1 + G2 if x in tab.index], R1_ + R2_].round(3).to_string())
print("range of every mean weight:", {k: (round(float(g.w.min()), 4), round(float(g.w.max()), 4)) for k, g in gw.groupby("weights")})''', ["claim:game-weights-two-groups"])
gw_code2 = code('''rows = []
for (thr, reading), g in gw.groupby(["threshold", "weights"]):
    t_ = g.pivot(index="state", columns="region", values="w")
    fails, fails_strict = [], []
    for st_ in t_.index:
        own, other = (R1_, R2_) if st_ in G1 else (R2_, R1_)
        ok = (t_.loc[st_, own] > 0).all() and t_.loc[st_, own].mean() > t_.loc[st_, other].mean()
        ok_strict = (t_.loc[st_, own] > 0).all() and t_.loc[st_, own].min() > t_.loc[st_, other].max()
        if not ok: fails.append(st_)
        if not ok_strict: fails_strict.append(st_)
    rows.append(dict(threshold=thr, weights=reading, n_dims=len(t_), failing=fails, holds=len(fails) <= 1,
                     failing_strict=fails_strict, holds_strict=len(fails_strict) <= 1))
gwc = pd.DataFrame(rows)
print("S7: dimensions failing the grouping (one may fail):")
print(gwc.to_string(index=False))
# Variant not from the paper: correlation across all voxels between the weight maps of every pair of
# dimensions, average-linkage clustering on 1 - r cut into two groups (both subjects; no mapper needed)
from scipy.cluster import hierarchy
from scipy.spatial.distance import squareform
for s in ss.GAME_SUBJECTS:
    for key in ["B_vox", "BL_vox"]:
        r = np.corrcoef(game[s][key])
        cut = hierarchy.fcluster(hierarchy.linkage(squareform(1 - r, checks=False), "average"), 2, "maxclust")
        nm = game[s]["map_names"]
        print(f"\\n{s} {key[:-4]} maps: clusters", {k: [nm[i] for i in np.nonzero(cut == k)[0]] for k in (1, 2)})
        print(pd.DataFrame(r, index=nm, columns=nm).round(2).to_string())''', ["claim:game-weights-two-groups"])

# Insert cells (from the end backwards so indices hold)
C[44:45] = [gw_md, gw_code1, gw_code2]
C.insert(43, lag_clf)  # after game-classification code (42), before its result (43)
C.insert(34, lag_csi)  # after game-csi code (33)
C[30:31] = [aw_md, aw_code1, aw_code2]
C.insert(10, runs_cell)  # after game data cell 9
C.insert(6, regions_cell)  # before attention loading
json.dump(nb, open(p, 'w'), indent=1, ensure_ascii=False)
open(p,'a').write('\n')
PYEOF
cp reproduce_zhang_2021.ipynb $TMPDIR/nb_backup.ipynb; python3 $TMPDIR/edit1.py && python3 -c "
import json
nb=json.load(open('reproduce_zhang_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    print(i,c['cell_type'],c.get('metadata',{}).get('tags'), ''.join(c['source'])[:70].replace(chr(10),' | '))
"; git diff --stat
```

```
0 markdown None # Reproducing Zhang, Gao, Cukur & Gallant (2021) from CRCNS vim-4 |  | Pap
1 code None import time, resource | import numpy as np | import pandas as pd | import ma
2 markdown None ## Data check
3 code ['sanity'] # Files in the data set and their current MD5 sums (checksums.md5 in t
4 code ['sanity'] # Layout of every data file: datasets, shapes and dtypes (no data read
5 code ['sanity'] # Attention task labels: states.hdf, and the semantic labels they shou
6 code ['sanity'] # Cortical regions on fsaverage, for att-weights-cortex and game-weigh
7 code ['sanity'] # Load each attention subject's deconvolved data (stacked passive, hum
8 code ['sanity'] # Per-condition means of the voxels: the attentive conditions are z-sc
9 code ['sanity'] # Clock check for the attention task: CSI of the presence clusters whe
10 code ['sanity'] # Video game data | game = {} | for s in ss.GAME_SUBJECTS: |     t = time.ti
11 code ['sanity'] # Run structure of the video game data: the correlation of consecutive
12 code ['sanity'] # Clock check for the video game: CSI (one cluster per state) with the
13 markdown None Checks of the description against the data, from the outputs above: |  | -
14 markdown None ## Attention task: CSI per subject and condition |  | Shared by fig1-csi-s
15 code None N_PERM = 1000 | rng = np.random.default_rng(1) | csi_obs, csi_null, csi_se
16 markdown None ### fig1-csi-s2 |  | > In subject S2 the four presence states (neither, hu
17 code ['claim:fig1-csi-s2'] exp = {"human": (0.75, 0.075), "vehicle": (0.69, 0.069), "passive": (0
18 code ['claim:fig1-csi-s2'] fig, axes = plt.subplots(1, 3, figsize=(12, 4)) | cols = ["#ff5100", "#0
19 markdown None **Result: reproduced, resting on an assumption about the third axis.**
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 -c "
import json
nb=json.load(open('reproduce_zhang_2021.ipynb'))
print(''.join(nb['cells'][47]['source']))
"; git diff reproduce_zhang_2021.ipynb | head -30
```

```
def game_classification(s, X, names, rng, n_perm):
    gc_rows, gc_null = [], {}
        n, d = X.shape
        nst = X.sum(1)
        for scheme in ["contig", "random"]:
            fs = ss.fold_scores(game[s]["G"], ss.folds(n, scheme, rng))
            for lab in "ab":
                use = (nst == 1) if lab == "a" else (nst >= 1)
                single = np.where(nst == 1, X.argmax(1), -1)
                for rule in ["euclid", "density"]:
                    counts = X[use].sum(0)
                    minc = 1 if rule == "euclid" else 2 * (d + 1)
                    classes = [c for c in range(d) if counts[c] >= minc]
                    left = [names[c] for c in range(d) if counts[c] < minc]
                    # held-out TRs scored under this label reading, and which of the classes each has
                    scored = [(use[te], X[te][use[te]][:, classes] > 0) for tr, te, Ztr, Zte in fs]
                    def run(perm_rng=None):
                        accs = []
                        for (tr, te, Ztr, Zte), (m, H) in zip(fs, scored):
                            Xtr = X[tr] if perm_rng is None else X[tr][perm_rng.permutation(len(tr))]
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 - <<'EOF'
import json
p='reproduce_zhang_2021.ipynb'
nb=json.load(open(p))
c=nb['cells'][47]; s=''.join(c['source'])
head, rest = s.split('    gc_rows, gc_null = [], {}\n',1)
body, tail = rest.split('    return gc_rows, gc_null\n',1)
body='\n'.join(l[4:] if l.startswith('    ') else l for l in body.split('\n'))
bad='''                            pred = ss.nearest_cluster(ptr, lab_tr, pte[m], cl, rule)
                        # score only the classes this fold could predict (a class too small to fit
                        # in this fold would otherwise count with a recall of 0)
                        accs.append(ss.balanced_accuracy(H[:, [classes.index(c) for c in cl]], pred, cl))
                        continue
'''
good='''                            pred = ss.nearest_cluster(ptr, lab_tr, pte[m], cl, rule)
                            # score only the classes this fold could predict (a class too small to fit
                            # in this fold would otherwise count with a recall of 0)
                            accs.append(ss.balanced_accuracy(H[:, [classes.index(c) for c in cl]], pred, cl))
                            continue
'''
assert bad in body, body[:3000]
body=body.replace(bad,good)
s=head+'    gc_rows, gc_null = [], {}\n'+body+'    return gc_rows, gc_null\n'+tail
c['source']=s.splitlines(keepends=True)
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
print(s[:2600])
EOF
```

```
def game_classification(s, X, names, rng, n_perm):
    gc_rows, gc_null = [], {}
    n, d = X.shape
    nst = X.sum(1)
    for scheme in ["contig", "random"]:
        fs = ss.fold_scores(game[s]["G"], ss.folds(n, scheme, rng))
        for lab in "ab":
            use = (nst == 1) if lab == "a" else (nst >= 1)
            single = np.where(nst == 1, X.argmax(1), -1)
            for rule in ["euclid", "density"]:
                counts = X[use].sum(0)
                minc = 1 if rule == "euclid" else 2 * (d + 1)
                classes = [c for c in range(d) if counts[c] >= minc]
                left = [names[c] for c in range(d) if counts[c] < minc]
                # held-out TRs scored under this label reading, and which of the classes each has
                scored = [(use[te], X[te][use[te]][:, classes] > 0) for tr, te, Ztr, Zte in fs]
                def run(perm_rng=None):
                    accs = []
                    for (tr, te, Ztr, Zte), (m, H) in zip(fs, scored):
                        Xtr = X[tr] if perm_rng is None else X[tr][perm_rng.permutation(len(tr))]
[... 21 more lines not kept]
```

**Agent**

Fixed an indentation slip from the refactor. Now a quick test run on two attention subjects with few permutations before the full run.

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 - <<'EOF'
import json, os
nb=json.load(open('reproduce_zhang_2021.ipynb'))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    s=''.join(c['source'])
    s=s.replace('import statespace as ss\n','import statespace as ss\nss.ATT_SUBJECTS = ["S2", "S3"]\n')
    s=s.replace('N_PERM = 1000','N_PERM = 10').replace('N_PERM_G = 20000','N_PERM_G = 200').replace('N_PERM_CLF = 1000','N_PERM_CLF = 5')
    s=s.replace('for _ in range(200)','for _ in range(5)').replace('rng, 200)[0]','rng, 5)[0]').replace('for _ in range(100)','for _ in range(3)')
    c['source']=s
json.dump(nb,open('test_tmp.ipynb','w'))
EOF
date -u; time executed/zhang-2021/.venv/bin/python -m jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output $TMPDIR/test_out.ipynb test_tmp.ipynb 2>&1 | tail -30
```

```
Sat Nov 14 12:53:31 UTC 2026
[NbConvertApp] Converting notebook test_tmp.ipynb to notebook
executed/zhang-2021/.venv/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 288510 bytes to /tmp/claude-1001/test_out.ipynb

real	8m37.545s
user	19m45.309s
sys	0m20.640s
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 - <<'EOF'
import json,os
nb=json.load(open(os.environ['TMPDIR']+'/test_out.ipynb'))
print(nb['nbformat'], nb['nbformat_minor'], 'id' in json.load(open('reproduce_zhang_2021.ipynb'))['cells'][0])
for i in [6,7,10,11,27,33,34,38,44,47,48,51,52]:
    for o in nb['cells'][i].get('outputs',[]):
        t=''.join(o.get('text','')) or str(o.get('evalue',''))
        print('=====',i); print(t[-3500:])
EOF
```

```
4 5 True
===== 6
fsaverage vertices per region (both hemispheres) in each atlas: {'FFA': 1975, 'OFA': 703, 'EBA': 4747, 'MT+': 900, 'PPA': 3029, 'OPA': 1196, 'RSC': 2142, 'LO': 1801, 'FO': 5600, 'IFS': 2622, 'IPS': 14832, 'FEF': 1682, 'SEF': 2014, 'LOS-bodies': 1233, 'ITG-bodies': 1809, 'MTG-bodies': 1705, 'OTS-bodies': 936, 'FFC (HCP)': 1670, 'PHA1-3 (HCP)': 3083, 'POS1 (HCP)': 2013, 'TPJ': 11146, 'precuneus': 7604, 'prefrontal': 57895, 'motor': 7870, 'premotor': 10840, 'SMA': 5071}
vertices per region that each subject's mapper reaches (attention regions):
     FFA  OFA   EBA  MT+   PPA   OPA   RSC    LO    FO   IFS    IPS   FEF   SEF  LOS-bodies  ITG-bodies  MTG-bodies  OTS-bodies  FFC (HCP)  PHA1-3 (HCP)  POS1 (HCP)
S2  1962  703  4714  880  2879  1193  2066  1798  5541  2602  14496  1673  1958        1215        1807        1692         927       1665          2947        1990
S3  1975  703  4745  898  2989  1196  2079  1800  5550  2598  14672  1680  1960        1233        1808        1704         932       1670          3067        2006
S7, video game regions: {'TPJ': 11146, 'precuneus': 7604, 'prefrontal': 57676, 'motor': 7870, 'premotor': 10840, 'SMA': 5071, 'IPS': 14832, 'FEF': 1682, 'SEF': 2004}
voxels the regions reach: {'S2': 5908, 'S3': 5982} | S7 video game: 16509

===== 7
S2: 48819 voxels (0 constant, 0 NaN), voxel means -0.301 to 0.306, SDs 0.894 to 1.203; 24 PCs explain 89.7%; |weights| in PC space human 121, vehicle 123, attention 7.35e-15; the code's own OLS coefficients in voxel space, norm per row (human, vehicle, attention, intercept) [1.211e+02 1.236e+02 1.260e-13 9.676e+01]; |r| rewrite vs code per axis [1.     1.     0.3457]; mean r of same-frame TRs {'passive-human': 0.09946298979776794, 'passive-vehicle': 0.07050453268014109, 'human-vehicle': 0.2569188841368312}; 37 s, peak memory 3.0 GB

===== 7
S3: 47512 voxels (0 constant, 0 NaN), voxel means -0.086 to 0.095, SDs 0.816 to 1.119; 24 PCs explain 68.4%; |weights| in PC space human 93.7, v
[... 331 more lines not kept]
```

**Agent calls Bash**

```bash
cd  rm entries/zhang-2021/test_tmp.ipynb; date -u; timeout 7000 python tools/entry.py all entries/zhang-2021 2>&1 | tail -20; date -u
```

```
Sat Nov 14 13:02:29 UTC 2026
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-zhang-2021 in executed/zhang-2021/.venv/share/jupyter/kernels/registry-zhang-2021
0 error(s)
pass  reproduce_zhang_2021.ipynb  (3095 s)
Sat Nov 14 13:54:16 UTC 2026
```

**Agent**

Full run passed in 52 min (under the 60-min limit). Reading the results.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
for i in [6,7,11,12,27,33,34,38,51,52]:
    for o in nb['cells'][i].get('outputs',[]):
        t=''.join(o.get('text','')) or str(o.get('evalue',''))
        print('=====',i); print(t[-5000:])
EOF
```

```
===== 6
fsaverage vertices per region (both hemispheres) in each atlas: {'FFA': 1975, 'OFA': 703, 'EBA': 4747, 'MT+': 900, 'PPA': 3029, 'OPA': 1196, 'RSC': 2142, 'LO': 1801, 'FO': 5600, 'IFS': 2622, 'IPS': 14832, 'FEF': 1682, 'SEF': 2014, 'LOS-bodies': 1233, 'ITG-bodies': 1809, 'MTG-bodies': 1705, 'OTS-bodies': 936, 'FFC (HCP)': 1670, 'PHA1-3 (HCP)': 3083, 'POS1 (HCP)': 2013, 'TPJ': 11146, 'precuneus': 7604, 'prefrontal': 57895, 'motor': 7870, 'premotor': 10840, 'SMA': 5071}
vertices per region that each subject's mapper reaches (attention regions):
     FFA  OFA   EBA  MT+   PPA   OPA   RSC    LO    FO   IFS    IPS   FEF   SEF  LOS-bodies  ITG-bodies  MTG-bodies  OTS-bodies  FFC (HCP)  PHA1-3 (HCP)  POS1 (HCP)
S1  1975  703  4745  899  3016  1196  1633  1801  5596  2616  14789  1682  1990        1233        1808        1704         934       1670          3064        2007
S2  1962  703  4714  880  2879  1193  2066  1798  5541  2602  14496  1673  1958        1215        1807        1692         927       1665          2947        1990
S3  1975  703  4745  898  2989  1196  2079  1800  5550  2598  14672  1680  1960        1233        1808        1704         932       1670          3067        2006
S5  1975  701  4740  899  3020  1189  2026  1801  5565  2611  14708  1682  1963        1227        1809        1704         935       1670          3069        2009
S6  1962  703  4729  899  3008  1192  1670  1798  5586  2613  14632  1651  2011        1220        1807        1702         934       1660          3065        1997
S7, video game regions: {'TPJ': 11146, 'precuneus': 7604, 'prefrontal': 57676, 'motor': 7870, 'premotor': 10840, 'SMA': 5071, 'IPS': 14832, 'FEF': 1682, 'SEF': 2004}
voxels the regions reach: {'S1': 5965, 'S2': 5908, 'S3': 5982, 'S5': 5945, 'S6': 6065} | S7 video game: 16509

===== 7
S1: 51608 voxels (14 constant, 0 NaN), voxel means -0.284 to 0.291, SDs 0.405 to 1.213; 24 PCs explain 84.1%; |weights| in PC space human 117, vehicle 106, attention 9.0
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
for i in [17,21,24,37,41,44,47,48]:
    for o in nb['cells'][i].get('outputs',[]):
        t=''.join(o.get('text','')) or str(o.get('evalue',''))
        print('=====',i); print(t[:3800])
EOF
```

```
===== 17
R3_code   human    CSI 0.743 (expected 0.75 +/- 0.075; within: True); above every null value: (a) True (max 0.040), (b) True (max 0.322)
R3_code   vehicle  CSI 0.721 (expected 0.69 +/- 0.069; within: True); above every null value: (a) True (max 0.056), (b) True (max 0.326)
R3_code   passive  CSI 0.675 (expected 0.67 +/- 0.067; within: True); above every null value: (a) True (max 0.062), (b) True (max 0.352)
  -> R3_code: all three within tolerance: True
R2_median human    CSI 0.723 (expected 0.75 +/- 0.075; within: True); above every null value: (a) True (max 0.040), (b) True (max 0.322)
R2_median vehicle  CSI 0.718 (expected 0.69 +/- 0.069; within: True); above every null value: (a) True (max 0.056), (b) True (max 0.326)
R2_median passive  CSI 0.657 (expected 0.67 +/- 0.067; within: True); above every null value: (a) True (max 0.062), (b) True (max 0.352)
  -> R2_median: all three within tolerance: True
R1_2d     human    CSI 0.664 (expected 0.75 +/- 0.075; within: False); above every null value: (a) True (max 0.030), (b) True (max 0.283)
R1_2d     vehicle  CSI 0.668 (expected 0.69 +/- 0.069; within: True); above every null value: (a) True (max 0.036), (b) True (max 0.303)
R1_2d     passive  CSI 0.632 (expected 0.67 +/- 0.067; within: True); above every null value: (a) True (max 0.042), (b) True (max 0.332)
  -> R1_2d: all three within tolerance: False
R2 5 to 95% range over random third axes: {'human': (np.float64(0.683), np.float64(0.784)), 'vehicle': (np.float64(0.684), np.float64(0.779)), 'passive': (np.float64(0.638), np.float64(0.681))}

===== 21
second reference, means of the paper's per-subject values over the same five subjects: {'human': np.float64(0.644), 'vehicle': np.float64(0.728), 'passive': np.float64(0.512)}
R3_code   human    mean 0.665 +/- 0.104 (SD over 5) (expected 0.66 +/- 0.09; within: True); every subject above every null value: {'a': True, 'b': True}; mean above every mean null value: {'a': True, 'b': True} (max mean null a 0.029, 
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
def out(i):
    return '\n'.join(''.join(o.get('text','')) for o in nb['cells'][i].get('outputs',[]))
print(out(15)[-2500:])
t=out(27); print('\n'.join(l for l in t.splitlines() if ' R3 ' in l or 'subject' in l)[:4000])
print(out(30)[-1500:])
t=out(44); print('\n'.join(l for l in t.splitlines() if l.startswith('S7') or l.startswith('order'))[:6000])
print(out(8)[-800:], out(9)[-800:])
EOF
```

```
S1 done in 60 s

S2 done in 61 s

S3 done in 60 s

S5 done in 60 s

S6 done in 60 s
   subject condition  R3_code  R3_seed_sd  R2_median  R2_5pct  R2_95pct  R1_2d  null3d_max_a  null2d_max_a  null3d_max_b  null2d_max_b
0       S1   passive    0.620       0.006      0.638    0.616     0.658  0.609         0.055         0.035         0.334         0.315
1       S1     human    0.515       0.007      0.543    0.503     0.609  0.483         0.045         0.037         0.336         0.297
2       S1   vehicle    0.744       0.008      0.762    0.730     0.790  0.716         0.053         0.041         0.088         0.067
3       S2   passive    0.675       0.005      0.657    0.638     0.681  0.632         0.062         0.042         0.352         0.332
4       S2     human    0.743       0.004      0.723    0.683     0.784  0.664         0.040         0.030         0.322         0.283
5       S2   vehicle    0.721       0.004      0.718    0.684     0.779  0.668         0.056         0.036         0.326         0.303
6       S3   passive    0.061       0.003      0.059    0.042     0.082  0.028         0.065         0.047         0.099         0.063
7       S3     human    0.696       0.006      0.703    0.669     0.761  0.647         0.048         0.033         0.339         0.301
8       S3   vehicle    0.761       0.004      0.728    0.699     0.807  0.674         0.043         0.033         0.303         0.272
9       S5   passive    0.614       0.006      0.622    0.602     0.657  0.592         0.094         0.045         0.347         0.284
[... 98 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; python3 -c "
import json,yaml
" 2>/dev/null; grep -n -A30 '"inputs"' schemas/attempt*.json | head -60; grep -n -A60 '"verifications"' schemas/attempt*.json | head -120
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
608:    "inputs": {
609-      "description": "Everything the attempt used that is not in the dataset.",
610-      "type": "array",
611-      "items": {
612-        "type": "object",
613-        "additionalProperties": false,
614-        "required": [
615-          "what",
616-          "source"
617-        ],
618-        "properties": {
619-          "what": {
620-            "type": "string",
621-            "minLength": 1
622-          },
623-          "source": {
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 446,470p schemas/attempt.schema.json; grep -l "verifications:" attempts/*.yaml | head -3; f=$(grep -l "verifications:" attempts/*.yaml | head -1); grep -n -A25 "^verifications:" $f | head -40
```

```
}
          },
          "reviewed": {
            "description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.",
            "type": "string"
          }
        }
      }
    },
    "findings": {
      "description": "What the attempt found, whatever the outcomes: about the dataset itself (`about: data`, for its owner and the archive, shown on the dataset's page) or about the paper (`about: paper`, shown on the paper's page).",
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "kind",
          "statement"
        ],
        "properties": {
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 - <<'EOF'
import json, uuid
p='reproduce_zhang_2021.ipynb'
nb=json.load(open(p))
c=nb['cells'][34]; s=''.join(c['source'])
old='''    cnt[thr, reading] = {reg: int('''
new='''    cnt[thr, reading] = {f"{reg} ({dim})": int('''
assert old in s; s=s.replace(old,new)
s=s.replace('print("\\nsubjects of 5 in which each region has the expected dimension positive and larger:")',
            'print("\\nsubjects of 5 in which each region has the named dimension positive and above the other:")')
c['source']=s.splitlines(keepends=True)
for c in nb['cells']:
    if 'id' not in c: c['id']=uuid.uuid4().hex[:8]
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
EOF
python3 -c "
import json;nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
t='\n'.join(''.join(o.get('text','')) for o in nb['cells'][30]['outputs']); print(t[:1800])"
```

```
S1 done in 103 s

S2 done in 100 s

S3 done in 102 s

S5 done in 103 s

S6 done in 102 s
subject  folds    rule  accuracy  fold_sd  null_mean  null_max   p
     S1 contig  euclid     42.33     9.50       8.78     16.78 0.0
     S1 contig density     54.48     8.58       8.93     15.15 0.0
     S1 random  euclid     45.70     4.68       8.15     11.67 0.0
     S1 random density     55.52     3.80       7.80     12.19 0.0
     S2 contig  euclid     46.78     6.82       8.82     17.41 0.0
     S2 contig density     56.85     6.19       9.05     16.70 0.0
     S2 random  euclid     48.30     2.33       7.98     13.78 0.0
     S2 random density     60.63     2.59       7.79     11.63 0.0
     S3 contig  euclid     39.93    13.33       8.98     15.52 0.0
     S3 contig density     45.59    15.49       9.28     15.93 0.0
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd entries/zhang-2021; python3 -c "
import json
nb=json.load(open('reproduce_zhang_2021.ipynb'))
print(''.join(nb['cells'][13]['source']))"
```

```
Sat Nov 14 13:55:27 UTC 2026
Checks of the description against the data, from the outputs above:

- The deconvolved attention files hold 900 TRs per condition for S1, S2, S3, S5 and S6 (30 min each
  at a 2 s TR, three 10-min runs as the paper says); S4 is absent, as the description says. The
  passive deconvolved data are already subsampled to the 900 TRs of the attentive movies. The
  selection indices cover 1800 s, and applying the code's subsampling to the passive semantic
  labels reproduces the attentive labels (correlation printed above), which is consistent with
  the passive data and labels sharing the attentive clock.
- `states.hdf` has the same presence labels in all three conditions; the third column codes the
  condition as -1 (attend humans), 0 (passive) and +1 (attend vehicles). The description does not
  give this coding. The vehicle column follows the semantic category `vehicle.n.01` exactly, and
  the human column follows `person.n.01` closely.
- The attentive conditions are z-scored per voxel within each condition (voxel means of zero, so
  the norm of each attentive condition's mean pattern is zero), while the passive TRs, subsampled
  after z-scoring, are not. With the attention variable coded -1, 0, +1 and an intercept, its OLS
  weight is the difference of the two attentive means, which is zero: the printed attention weight
  is at the level of rounding (1e-13), so the third axis of the state space is set by rounding
  noise. This is analysed in each attention claim below.
- The PC-space rewrite gives the code's human and vehicle axes exactly (|r| = 1.0000); its third
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; cat > $TMPDIR/edit2.py <<'PYEOF'
import json, uuid
p='reproduce_zhang_2021.ipynb'
nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source']=s.rstrip('\n').splitlines(keepends=True)
def rep(i, old, new):
    s=src(i); assert old in s, (i, old); setsrc(i, s.replace(old, new))
def md(s): return {"cell_type":"markdown","id":uuid.uuid4().hex[:8],"metadata":{},"source":s.rstrip('\n').splitlines(keepends=True)}

# header
rep(0, "Only the layouts of the other files (non-deconvolved BOLD, mappers) are read.",
"""The non-deconvolved attention BOLD (`VisualAttention/Data/S*.hdf`) is read for the encoding-model
threshold of att-weights-cortex, and the mappers (`Mappers/S*.hdf`) to place weights on fsaverage.

Outside inputs, for the two cortical claims only (the claims file allows an fsaverage atlas):
visfAtlas (Rosenke et al. 2021, Cerebral Cortex 31:603, doi:10.1093/cercor/bhaa246), the zip its
authors publish at download.brainvoyager.com/data/visfAtlas.zip, SHA-256 2eae192d...799d (checked
on reading); and HCP-MMP1.0 projected on fsaverage, doi:10.6084/m9.figshare.3498446.v2 (MD5 sums
checked on reading).""")
rep(0, "| att-weights-cortex | blocked: the paper's functional ROIs (localizer and retinotopy data) are not public |",
       "| att-weights-cortex | tested with atlas regions in place of the paper's ROIs, which are not public |")
rep(0, "| game-weights-two-groups | blocked: the paper's ROIs are not public, and S1's game data have no matching mapper |",
       "| game-weights-two-groups | tested in S7 only, with atlas regions; S1's game data have no matching mapper |")

# data check text
rep(13, "24 PCs explain about 85 to 90% of the variance here, against\n  about 70% in the paper.",
"""24 PCs explain 68 to 90% of the variance here, against about
  70% in the paper. The code's own OLS coefficients in voxel space give the same picture: the norm
  of the attention row is about 1e-13, against about 1e2 for the human and vehicle rows, so the
  code's third axis is set by rounding too. The R3 values below therefore move slightly between
  runs (S2 attend-humans 0.740 in the first run, 0.743 in this one).""")
rep(13, """- Labels and BOLD share a clock as far as shifted labels show: the attention CSI peaks at lag 0,
  as deconvolved data should, and the game CSI peaks within one TR of lag 0. This is consistent
  with, not proof of, aligned labels.""",
"""- Labels and BOLD share a clock as far as shifted labels show: the attention CSI peaks at lag 0,
  as deconvolved data should. The game CSI peaks at lag +1 TR in both subjects (S1 0.729 against
  0.691 at lag 0; S7 0.569 against 0.547), as a hemodynamic delay in data that are not deconvolved
  would give. The paper does not say whether the game labels were shifted; lag 0 is used, and the
  game CSI and classification are also shown at lag +1. This is consistent with, not proof of,
  aligned labels.""")
rep(13, """- Video game: S7 has 1320 TRs (44 min, the paper's 45 min). S1 has 1950 TRs, 65 min, where the
  paper says one subject played 90 min in six 15-min runs.""",
"""- Video game: S7 has 1320 TRs (44 min, the paper's 45 min). S1 has 1950 TRs, 65 min, where the
  paper says one subject played 90 min in six 15-min runs. The correlation of consecutive TRs
  drops to -0.44 to -0.48 exactly at TRs 325, 650, 975, 1300 and 1625, so S1's data are six
  blocks of 325 TRs (10.9 min each), as six runs of the 325-volume length the paper gives for its
  acquisitions would be. The deposited S1 data are therefore six whole runs, consistent with the
  paper's six runs but not with its 15 minutes per run. In S7 the dips at TRs 440 and 880 are
  weaker (-0.08 and -0.03), consistent with three runs of 440 TRs (14.7 min).""")
rep(13, """attention data), so S1's game weights cannot be put on fsaverage with the files given.""",
"""attention data), nor any of the superseded mappers in `Mappers/old` (S1 81,137, S5 84,038, S6
  86,842), so S1's game weights cannot be put on fsaverage with the files given.""")

# fig1 result
setsrc(19, """**Result: reproduced, resting on an assumption about the third axis.** With the paper's code (R3)
the S2 CSIs are 0.743 (attend-humans), 0.721 (attend-vehicles) and 0.675 (passive), all within
tolerance of 0.75, 0.69 and 0.67, and each exceeds every one of 1000 null values under both
permutation readings (null maxima 0.040 to 0.062 under (a), 0.322 to 0.352 under (b); p <= 0.001,
the bound 1000 permutations reach, not the paper's 1e-5). The median over random third axes (R2)
also matches (0.723, 0.718, 0.657). In the human-vehicle plane alone (R1) the attend-humans CSI is
0.664, outside tolerance. The third axis of the state space has no weight in these data, so the
values depend on it: over random third axes the attend-humans CSI ranges from 0.683 to 0.784 (5 to
95%), within tolerance throughout.""")
setsrc(22, """**Result: reproduced, resting on an assumption about the third axis.** Over the five released
subjects, R3 gives mean CSIs of 0.665 +/- 0.104 (attend-humans), 0.731 +/- 0.023 (attend-vehicles)
and 0.524 +/- 0.260 (passive), all within the paper's spreads of 0.66 +/- 0.09, 0.74 +/- 0.03 and
0.53 +/- 0.24; R2 gives 0.658, 0.728 and 0.523. Under group reading (b), each mean exceeds the
maximum of the mean null CSIs (at most 0.110). Under reading (a), every subject is significant in
the attentive conditions but not in passive, where S3's CSI (0.061) does not exceed its null. In
the plane alone (R1) the attend-vehicles mean, 0.675, is outside tolerance. The second reference,
the means of the paper's own per-subject values over these subjects (0.644, 0.728, 0.512), is also
close to the R3 means.""")
setsrc(25, """**Result: reproduced, resting on an assumption about the third axis.** With R3, 10 of the 12
per-subject CSIs are within 10% of the values in Supplementary Figures 1 and 2 (11 of 12 with R2,
10 of 12 with R1). The two outside are S3 passive (0.061 against 0.05, a tolerance of 0.005) and
S5 attend-humans (0.767 against 0.66, within tolerance under R2 at 0.694). Under permutation
reading (a) all 12 R3 CSIs are significant at p < 0.01: eleven exceed every null value
(p = 0.001) and S3 passive has p = 0.002. Under reading (b) S3 passive has p = 0.045, so 11 of 12
are significant. The R1 counts are printed above. S3's passive CSI is close to the floor of the
measure, as in the paper (0.05).""")
rep(26, "code's QR, which now gives the third axis a real weight. R1 (the plane) is shown as a variant.",
"""code's QR, which now gives the third axis a real weight, while the observed third axis is noise,
so the observed value and the null (i) are not computed the same way for R3; the observed CSIs
also average 10 Monte Carlo seeds where each null draw uses one. Null (ii) has neither difference.
R1 (the plane) is shown as a variant. The null quantiles of the mean difference are printed for
every subject.""")
setsrc(28, """**Result: not reproduced.** At the threshold that 1000 permutations allow (the difference
exceeding every null value), the passive CSI is significantly lower than the attentive CSIs in 2
or 3 of the 5 subjects under every combination of reading and null run with the code's positions
(R3), and in 1 with the plane (R1), where the criterion needs 4 of 5. At p < 0.05 the counts are
at most 3 with R3 and at most 4 with R1 (reading b, matched permutation, refitted). S3 and S5 show
the effect clearly (mean differences 0.668 and 0.135, above every null value). In S1 and S6 the
attend-humans CSI is below the passive one (S1 0.515 against 0.620; S6 0.605 against 0.651), as in
the paper's own figure values for these subjects, and the mean of the two attentive CSIs is within
0.010 of passive (p 0.30 to 0.51). S2's mean difference, 0.057, lies above the null's 99th
percentile (0.042 to 0.055) and below or near its maximum (0.052 to 0.084), p = 0.001 to 0.010.
The counts are the same under null (ii), which is computed as the observed values are.""")
setsrc(31, """**Result: reproduced.** The mean accuracy over the five subjects is 43.7% (contiguous folds,
Euclidean), 53.8% (contiguous, density), 46.6% (random, Euclidean) and 56.3% (random, density),
against 48.4 +/- 7.6%; three of the four readings are within tolerance, and all four exceed every
one of 1000 mean null accuracies (maxima 9.7 to 12.5%). Chance under this procedure, the mean of
the null, is 7.8 to 9.1%, close to the paper's 8.3%. Per subject the accuracy is 39.9 to 60.6%.
The first run gave 44.4% and 53.4% for the contiguous readings with the same code and seeds; the
third axis of each fold's state space carries almost no weight, so rounding can move it.""")
PYEOF
python3 $TMPDIR/edit2.py && echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; cat > $TMPDIR/edit3.py <<'PYEOF'
import json, uuid
p='reproduce_zhang_2021.ipynb'
nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source']=s.rstrip('\n').splitlines(keepends=True)
def rep(i, old, new):
    s=src(i); assert old in s, (i, old); setsrc(i, s.replace(old, new))
def md(s): return {"cell_type":"markdown","id":uuid.uuid4().hex[:8],"metadata":{},"source":s.rstrip('\n').splitlines(keepends=True)}
rep(31, "the\nthird axis of each fold's state space carries almost no weight, so rounding can move it.",
    "the\ncause was not traced; the likeliest is rounding in the third axis of each fold's state space,\nwhich carries little weight.")
assert src(34).startswith('HUM, VEH') and src(52).startswith('rows = []')
aw_res = md("""**Result: reproduced under one reading, resting on assumptions about the regions.** With the
encoding-model threshold (ii), the human-presence weight is positive and above the vehicle-presence
weight in FFA, OFA and EBA, and the reverse holds in RSC, PPA and OPA, in 4 of 5 subjects under
each of the three weight readings (B, B_L, Q_S); S2 fails in EBA. Without a threshold (i) the
pattern holds in 3 of 5 under each reading: EBA fails in S2 and S3 (B, B_L) or S1 and S2 (Q_S).
FFA, OFA, RSC, PPA and OPA hold in all five subjects under every reading; the outcome rests on EBA,
whose atlas definition (the lateral body areas of visfAtlas) is an assumption: LOS-bodies alone
holds in 5 of 5 under (ii). Of the other regions the claim names, MT+ (4 of 5) and LO (4 or 5)
follow the human-presence dimension and IPS (5 of 5) the vehicle-presence dimension; SEF, FEF, FO
and IFS are mixed (counts above). The regions are group-atlas areas, not the subjects' localizer
ROIs, and the WordNet model's ridge parameter was chosen per subject (1e3 or 1e4); 57 to 71% of
the region voxels pass its threshold.""")
gw_res = md("""**Result: not reproduced in S7, resting on assumptions about the regions; S1 cannot be placed on
the cortex.** In S7 three to five of the eight dimensions fail the grouping under every reading,
where one may fail: dead, safe explore and unsafe explore under every reading, and engage far,
run away, round start or engage close under some. Safe explore has negative OLS weights in all
nine regions (-0.008 to -0.240, threshold i). With the Bonferroni threshold (ii) and the OLS or
denoised weights, three fail. S1's game data match no mapper, so S1 and the consistency between
the two subjects could not be tested. In the variant not taken from the paper, the correlation of
S1's denoised weight maps across voxels splits the nine dimensions into exactly the paper's two
groups (flash, safe explore, unsafe explore, dead, round start; engage close, engage far, run away,
kill), while S7's maps split into safe and unsafe explore against the rest. The regions are
HCP-MMP1.0 areas chosen to match the names in the paper, not the paper's ROIs.""")
C.insert(53, gw_res)
C.insert(35, aw_res)
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='markdown': print(i, ''.join(c['source'])[:60].replace('\n',' '))
PYEOF
python3 $TMPDIR/edit3.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/edit3.py", line 10, in <module>
    rep(31, "the\nthird axis of each fold's state space carries almost no weight, so rounding can move it.",
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        "the\ncause was not traced; the likeliest is rounding in the third axis of each fold's state space,\nwhich carries little weight.")
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/edit3.py", line 8, in rep
    s=src(i); assert old in s, (i, old); setsrc(i, s.replace(old, new))
                     ^^^^^^^^
AssertionError: (31, "the\nthird axis of each fold's state space carries almost no weight, so rounding can move it.")
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; sed -i 's/rep(31, "the\\nthird axis of each fold'"'"'s state space carries almost no weight, so rounding can move it.",/rep(31, "the third axis of each fold'"'"'s state space carries almost no weight, so rounding can move it.",/; s/    "the\\ncause was not traced; the likeliest is rounding in the third axis of each fold'"'"'s state space,\\nwhich carries little weight.")/    "the cause was not traced; the likeliest is rounding in the third axis of each fold'"'"'s state space,\\nwhich carries little weight.")/' $TMPDIR/edit3.py; sed -n 10,11p $TMPDIR/edit3.py; python3 -c "
import json;print(repr(''.join(json.load(open('reproduce_zhang_2021.ipynb'))['cells'][31]['source'])[-200:]))"
```

```
rep(31, "the third axis of each fold's state space carries almost no weight, so rounding can move it.",
    "the cause was not traced; the likeliest is rounding in the third axis of each fold's state space,\nwhich carries little weight.")
"d every\none of 1000 mean null accuracies (maxima 9.7 to 12.5%). Chance under this procedure, the mean of\nthe null, is 7.8 to 9.1%, close to the paper's 8.3%. Per subject the accuracy is 40.8 to 60.6%."
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; echo "json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')" >> $TMPDIR/edit2.py; python3 $TMPDIR/edit2.py && python3 $TMPDIR/edit3.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/edit3.py", line 10, in <module>
    rep(31, "the third axis of each fold's state space carries almost no weight, so rounding can move it.",
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        "the cause was not traced; the likeliest is rounding in the third axis of each fold's state space,\nwhich carries little weight.")
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/edit3.py", line 8, in rep
    s=src(i); assert old in s, (i, old); setsrc(i, s.replace(old, new))
                     ^^^^^^^^
AssertionError: (31, "the third axis of each fold's state space carries almost no weight, so rounding can move it.")
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 - <<'EOF'
import os
f=os.environ['TMPDIR']+'/edit3.py'; s=open(f).read()
s=s.replace('''rep(31, "the third axis''','''rep(31, "the\\nthird axis''')
open(f,'w').write(s)
EOF
python3 $TMPDIR/edit3.py
```

```
0 # Reproducing Zhang, Gao, Cukur & Gallant (2021) from CRCNS 
2 ## Data check
13 Checks of the description against the data, from the outputs
14 ## Attention task: CSI per subject and condition  Shared by 
16 ### fig1-csi-s2  > In subject S2 the four presence states (n
19 **Result: reproduced, resting on an assumption about the thi
20 ### att-csi-group  > Across subjects the presence states are
22 **Result: reproduced, resting on an assumption about the thi
23 ### supp-csi-per-subject  > In each subject and each attenti
25 **Result: reproduced, resting on an assumption about the thi
26 ### att-passive-lower  > Attention increases state separatio
28 **Result: not reproduced.** At the threshold that 1000 permu
29 ### att-classification  > Held-out TRs of the attention task
31 **Result: reproduced.** The mean accuracy over the five subj
32 ### att-weights-cortex  > The human-presence dimension of th
35 **Result: reproduced under one reading, resting on assumptio
36 ## Video game task  States with no TRs are dropped (flash in
37 ### game-csi  > In the video game task the behavioural state
40 **Result: reproduced under one reading of the clusters.** Wi
41 ### game-mutual-negative-projection  > The mutually exclusiv
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; cat > $TMPDIR/edit4.py <<'PYEOF'
import json, uuid
p='reproduce_zhang_2021.ipynb'
nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source']=s.rstrip('\n').splitlines(keepends=True)
def rep(i, old, new):
    s=src(i); assert old in s, (i, old); setsrc(i, s.replace(old, new))
assert src(40).startswith('**Result: reproduced under one reading')
setsrc(40, """**Result: reproduced under one reading of the clusters.** With one cluster per state from TRs
that have exactly one state (reading b), the CSI is 0.702 in S1 and 0.581 in S7, within tolerance
of 0.72 and 0.62, and both exceed every null value (null maxima 0.270 and 0.258). With every TR in
the cluster of each of its states (reading a), S1 is within (0.694) and S7 just outside (0.549,
tolerance down to 0.558). With the three groups of Figure 3A (reading c), both are lower (0.513 and
0.388). All six values exceed their nulls. With the labels moved one TR later, where the CSI
peaks, readings (a) and (b) are within tolerance in both subjects (S1 0.728 and 0.760, S7 0.566
and 0.583, each above all 200 null values) and reading (c) is not (0.593 and 0.418).""")
assert src(46).startswith('**Result: reproduced.** Under every sign')
setsrc(46, """**Result: reproduced.** Under every sign, order, Bonferroni and null-centre reading, both
subjects have significant off-diagonal projections (S1 44 to 48 pairs, S7 20 to 33), some pairs are
significant in one direction only (10 to 20), and the two subjects' sets of significant pairs
differ (12 to 27 shared). Centring the two-sided test on the null's mean in place of zero changes
the counts by at most one pair. The figure's own matrix was not available to compare pair by pair.""")
rep(47, "out of that rule (listed below). Null: training state rows permuted, 1000 times.",
"""out of that rule (listed below). Under labels (a) a class with too few single-state TRs in a
training fold is left out of that fold, and the fold's balanced accuracy is taken over the classes
it could predict (in the first run such a class was scored with a recall of 0). Null: training
state rows permuted, 1000 times. As a variant, the labels moved one TR later (200 permutations).""")
assert src(50).startswith('**Result: partially reproduced.**')
setsrc(50, """**Result: partially reproduced.** Every reading is far above its null (p = 0.001; chance under
this procedure 10.8 to 16.4%, against the paper's 11%). S7's balanced accuracy is within the
paper's 30.4 +/- 4.2% with contiguous folds (26.4 to 33.8%) and above it with random folds (36.8 to
46.5%). S1's is above the paper's 32.8 +/- 3.8% under every reading (42.8 to 54.6%), so no reading
puts both subjects within tolerance. With the labels one TR later the accuracies rise (S1 45.7 to
60.5%, S7 28.4 to 50.9%) and the same holds. Random folds put neighbouring, autocorrelated TRs in
training and test sets and give higher values than contiguous folds; the outcome does not depend
on this, since S1 is above tolerance under both. S1's data are six whole runs of 325 TRs (65 min,
data check), where the paper reports 90 min, so the S1 data may differ from those the paper
analysed, which could account for S1 being above the paper's value.""")
# summary
s=src(55)
s=s.replace("| att-weights-cortex | blocked, data_missing (the paper's ROIs are not public) |",
            "| att-weights-cortex | reproduced under the encoding-model threshold (4 of 5 subjects), 3 of 5 without it; atlas regions in place of the paper's ROIs |")
s=s.replace("| game-weights-two-groups | blocked, data_missing (ROIs; no mapper for S1's game voxels) |",
            "| game-weights-two-groups | not reproduced: fails in S7 under every reading (atlas regions); S1 cannot be mapped |")
s=s.replace("""- S7's game state space has 8 dimensions (no flash TRs).""",
"""- S7's game state space has 8 dimensions (no flash TRs).
- The paper's functional ROIs are not public; the two cortical claims use group-atlas regions on
  fsaverage (visfAtlas and HCP-MMP1.0) through the data set's mappers, an assumption.
- The game labels are used at lag 0; the CSI peaks at lag +1, shown as a variant.""")
s=s.replace("""- S1's video game data hold 1950 TRs (65 min), where the paper and the description say one
  subject played 90 min; S7's hold 44 min, as stated.""",
"""- S1's video game data hold 1950 TRs (65 min) in six blocks of 325 TRs, where the paper and the
  description say one subject played 90 min in six 15-min runs; S7's hold 44 min, as stated.""")
s=s.replace("""- S1's video game data have 73,594 voxels, a voxel set no mapper in the data set matches.""",
"""- S1's video game data have 73,594 voxels, a voxel set no mapper in the data set matches,
  current or superseded.""")
s=s.replace("""- No functional ROI, localizer or retinotopy data are deposited.""",
"""- No functional ROI, localizer or retinotopy data are deposited.
- The code's attention coefficients are at the level of rounding (about 1e-13), so the R3 CSIs
  move slightly from run to run.""")
setsrc(55, s)
json.dump(nb, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
print(src(55))
PYEOF
python3 $TMPDIR/edit4.py
```

```
## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning
and the differences from the paper's method.

| claim | outcome |
|---|---|
| fig1-csi-s2 | reproduced (assumption: third axis as the code gives it) |
| att-csi-group | reproduced (same assumption) |
| supp-csi-per-subject | reproduced (10 of 12 values; all significant under reading a) |
| att-passive-lower | not reproduced (2 or 3 of 5 subjects at the bound reached) |
| att-classification | reproduced |
| att-weights-cortex | reproduced under the encoding-model threshold (4 of 5 subjects), 3 of 5 without it; atlas regions in place of the paper's ROIs |
| game-csi | reproduced (one reading of the clusters) |
| game-mutual-negative-projection | reproduced (assumption: data set's column order) |
| fig3b-state-relations | reproduced |
| game-classification | partially reproduced (S1 above the paper's value) |
| game-weights-two-groups | not reproduced: fails in S7 under every reading (atlas regions); S1 cannot be mapped |

How the analysis differs from the paper's:
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 - <<'EOF'
s=open('README.md').read()
s=s.replace("""- `statespace.py`: loading, the state space of the paper's code (computed in the space of the 24
  principal components), the cluster separation index and the classifiers.

The notebook streams about 7 GB and runs in about 20 minutes with 4 GB of memory.""",
"""- `statespace.py`: loading, the state space of the paper's code (computed in the space of the 24
  principal components), the cluster separation index, the classifiers, and the atlas regions and
  encoding models of the two cortical claims.

The two cortical claims use two public fsaverage atlases in place of the paper's ROIs, which are
not deposited: visfAtlas (Rosenke et al. 2021, doi:10.1093/cercor/bhaa246) and HCP-MMP1.0 on
fsaverage (doi:10.6084/m9.figshare.3498446.v2). Both are read into memory and checked against
their checksums.

The notebook streams about 16 GB and runs in about 55 minutes with 6 GB of memory.""")
open('README.md','w').write(s)
s=open('entry.yaml').read()
s=s.replace("""  and the projections between video game states. The functional ROIs behind the cortical maps are not
  in the data set.""","""  and the projections between video game states. The functional ROIs behind the cortical maps are not
  in the data set; the cortical claims use public fsaverage atlases through the data set's mappers.""")
s=s.replace("runtime_minutes: 25","runtime_minutes: 55")
open('entry.yaml','w').write(s)
EOF
git diff entry.yaml README.md | head -40; date -u
```

```
diff --git a/entries/zhang-2021/README.md b/entries/zhang-2021/README.md
index a49f4fd..e442a6d 100644
--- a/entries/zhang-2021/README.md
+++ b/entries/zhang-2021/README.md
@@ -9,6 +9,12 @@ and the differences from the paper's method.
 
 - `reproduce_zhang_2021.ipynb`: the data check and one section per claim.
 - `statespace.py`: loading, the state space of the paper's code (computed in the space of the 24
-  principal components), the cluster separation index and the classifiers.
+  principal components), the cluster separation index, the classifiers, and the atlas regions and
+  encoding models of the two cortical claims.
 
-The notebook streams about 7 GB and runs in about 20 minutes with 4 GB of memory.
+The two cortical claims use two public fsaverage atlases in place of the paper's ROIs, which are
+not deposited: visfAtlas (Rosenke et al. 2021, doi:10.1093/cercor/bhaa246) and HCP-MMP1.0 on
+fsaverage (doi:10.6084/m9.figshare.3498446.v2). Both are read into memory and checked against
+their checksums.
+
+The notebook streams about 16 GB and runs in about 55 minutes with 6 GB of memory.
diff --git a/entries/zhang-2021/entry.yaml b/entries/zhang-2021/entry.yaml
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/zhang-2021; python3 - <<'EOF'
s=open('statespace.py').read()
old='''  are readings named in the claims file.
"""'''
new='''  are readings named in the claims file.
- Cortical regions (att-weights-cortex, game-weights-two-groups): the paper's
  per-subject ROIs are not public, and the claims file allows an fsaverage atlas
  through the data set's mappers. Regions are unions of visfAtlas and
  HCP-MMP1.0 areas (an assumption, listed in ATT_REGIONS and GAME_REGIONS); a
  region's mean of a voxel map is the mean over its fsaverage vertices that the
  mapper reaches. Weights per region are computed exactly from the
  region-averaged responses (region_weights). The encoding-model thresholds are
  the claims file's readings (ii), with the details stated in semantic_model_r
  and cv_ols_r.
"""'''
assert old in s; s=s.replace(old,new,1); open('statespace.py','w').write(s)
EOF
grep -n "—\|rather" statespace.py README.md entry.yaml reproduce_zhang_2021.ipynb | head; cd  python tools/entry.py check entries/zhang-2021 2>&1 | tail -5
```

```
0 error(s)
```

**Agent**

Text written; launching the final full run (about 52 min).

**Agent calls Bash**

```bash
cd  date -u; timeout 7000 python tools/entry.py all entries/zhang-2021 2>&1 | tail -5; date -u
```

```
Sat Nov 14 13:57:06 UTC 2026
Installed kernelspec registry-zhang-2021 in executed/zhang-2021/.venv/share/jupyter/kernels/registry-zhang-2021
0 error(s)
pass  reproduce_zhang_2021.ipynb  (3068 s)
Sat Nov 14 14:48:24 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('executed/zhang-2021/reproduce_zhang_2021.ipynb'))
def out(i):
    return '\n'.join(''.join(o.get('text','')) for o in nb['cells'][i].get('outputs',[]))
import re
print(out(7)[:300]); print(out(11)); print(out(12)[-300:])
print(out(17)[:700]); print(out(21)[300:900])
t=out(24); print(t[:1500])
t=out(27); print(t[t.index('subjects of 5'):t.index('null distribution')])
print(out(30)[-900:])
print(out(34)[-4200:])
print(out(38)); print(out(44)[:400])
t=out(48); print(t[:400]); print(out(49)[:2000]); print(out(52)[:2600]); print(out(53)[:2000])
EOF
```

```
S1: 51608 voxels (14 constant, 0 NaN), voxel means -0.284 to 0.291, SDs 0.405 to 1.213; 24 PCs explain 84.1%; |weights| in PC space human 117, vehicle 106, attention 9.06e-15; the code's own OLS coefficients in voxel space, norm per row (human, vehicle, attention, intercept) [1.177e+02 1.063e+02 9.7
S1: 1950 TRs; consecutive-TR correlation median 0.318, 1st percentile 0.079; the 8 lowest at the start of TRs [172, 325, 650, 869, 975, 1300, 1625, 1739] (values [-0.027, -0.462, -0.469, 0.007, -0.477, -0.467, -0.441, 0.005]); gaps between them [172, 153, 325, 219, 106, 325, 325, 114, 211]
S7: 1320 TRs; consecutive-TR correlation median 0.376, 1st percentile 0.094; the 8 lowest at the start of TRs [11, 30, 31, 66, 237, 440, 880, 1036] (values [0.024, 0.027, -0.2, 0.004, 0.037, -0.084, -0.03, 0.034]); gaps between them [11, 19, 1, 35, 171, 203, 440, 156, 284]

ject                                                                             
S1       0.514  0.538  0.569  0.629  0.691  0.729  0.687  0.606  0.600  0.590  0.518
S7       0.452  0.461  0.500  0.512  0.547  0.569  0.556  0.557  0.528  0.532  0.540
lag of the peak per subject: {'S1': 1, 'S7': 1}

R3_code   human    CSI 0.743 (expected 0.75 +/- 0.075; within: True); above every null value: (a) True (max 0.040), (b) True (max 0.322)
R3_code   vehicle  CSI 0.721 (expected 0.69 +/- 0.069; within: True); above every null value: (a) True (max 0.056), (b) True (max 0.326)
R3_code   passive  CSI 0.675 (expected 0.67 +/- 0.067; within: True); above every null value: (a) True (max 0.062), (b) True (max 0.352)
  -> R3_code: all three within tolerance: True
R2_median human    CSI 0.723 (expected 0.75 +/- 0.075; within: True); above every null value: (a) True (max 0.040), (b) True (max 0.322)
R2_median vehicle  CSI 0.718 (expected 0.69 +/- 0.069; within: True); above every null value: (a) True (m
alue: {'a': True, 'b': True}; mean above every mean null value: {'a': True, 'b': True} (max mean null a 0.029, b 0.110)
R3_code   v
[... 185 more lines not kept]
```

**Agent**

Final run passed (51 min) and the numbers match the first revised run exactly. Writing the attempt record now.

**Agent calls Bash**

```bash
cd  python3 -c "import yaml; print(yaml.__version__)"; head -5 attempts/zhang-2021-01.yaml; grep -n "kind: link\|data:" claims/zhang-2021.yaml | head
```

```
6.0.3
schema_version: 3
id: zhang-2021-01
datasets:
- archive: crcns
  id: vim-4
272:  data: with_inputs
418:  data: with_inputs
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec.py <<'PYEOF'
import yaml
p='attempts/zhang-2021-01.yaml'
d=yaml.safe_load(open(p))
O={o['claim']:o for o in d['outcomes']}

o=O['fig1-csi-s2']
o['measured']=[0.743,0.721,0.675]
o['notes']=("With the paper's code run on the full voxel data (R3), S2's CSIs are 0.743 (attend-humans), "
 "0.721 (attend-vehicles) and 0.675 (passive), each within tolerance and above every one of 1000 null values "
 "under both permutation readings (p <= 0.001, the bound reached; the paper reports p < 1e-5). The median over "
 "random third axes (R2) gives 0.723, 0.718 and 0.657, also within tolerance, and over random third axes the "
 "attend-humans CSI ranges from 0.683 to 0.784 (5 to 95%), within tolerance throughout. In the human-vehicle "
 "plane alone (R1) attend-humans is 0.664, outside tolerance. The code's own attention coefficients are about "
 "1e-13 in norm (human and vehicle about 1e2), so its third axis is set by rounding and the R3 values move "
 "slightly between runs (0.740, 0.718, 0.676 in the first run).")

o=O['att-csi-group']
o['measured']=[0.665,0.731,0.524]
o['notes']=("Over the five released subjects (R3) the mean CSIs are 0.665 +/- 0.104, 0.731 +/- 0.023 and "
 "0.524 +/- 0.260 for attend-humans, attend-vehicles and passive, within the paper's spreads. Under group "
 "reading (b) each mean exceeds the maximum of 1000 mean null CSIs (at most 0.110). Under reading (a) every "
 "subject is significant at the bound in the attentive conditions but S3's passive CSI (0.061) does not exceed "
 "every null value. R2 gives 0.658, 0.728 and 0.523; R1 gives 0.602, 0.675 (outside tolerance) and 0.492. The "
 "means of the paper's own per-subject values over these subjects are 0.644, 0.728 and 0.512.")

o=O['supp-csi-per-subject']
o['measured']=[0.515,0.744,0.620,0.696,0.761,0.061,0.767,0.730,0.614,0.605,0.699,0.651]
o['notes']=("With R3, 10 of 12 values are within 10% of the supplement's; outside are S3 passive (0.061 against "
 "0.05, tolerance 0.005) and S5 attend-humans (0.767 against 0.66). Under permutation reading (a) all 12 are "
 "significant at p < 0.01 (S3 passive p = 0.002, the others 0.001); under reading (b) S3 passive has p = 0.045. "
 "R2 puts 11 of 12 within tolerance with the same significance; R1 puts 10 within but S3 passive is not "
 "significant under either reading (p = 0.078 and 0.355), so R1 would make the claim partially reproduced.")

o=O['att-passive-lower']
o['notes']=("At the threshold 1000 permutations allow (the difference above every null value, p <= 0.001), the "
 "passive CSI is significantly lower in 2 of 5 subjects under reading (a) with the code's positions (S3, S5), "
 "and 2 or 3 under reading (b), for every null (refitted or not) and both permutation schemes; the criterion "
 "needs 4 of 5. At p < 0.05 the counts are at most 3 (R3) and at most 4 (R1, reading b, matched, refitted). In "
 "S1 and S6 attend-humans is below passive (0.515 against 0.620; 0.605 against 0.651), as in the paper's own "
 "figure values for these subjects, and the mean attentive CSI is within 0.010 of passive (p 0.30 to 0.51). "
 "S2's mean difference, 0.057, lies above its null's 99th percentile (0.042 to 0.055) and below or near its "
 "maximum (0.052 to 0.084), p 0.001 to 0.010. Null (ii), computed as the observed values are, gives the same "
 "counts as the refitted null (i). Measured is the count under reading (a), null (i), matched permutation.")

o=O['att-classification']
o['measured']=43.7
o['notes']=("Mean accuracy over the five subjects is 43.7% (contiguous folds, Euclidean), 53.8% (contiguous, "
 "density), 46.6% (random, Euclidean) and 56.3% (random, density), against 48.4 +/- 7.6%; three readings are "
 "within tolerance and all exceed every one of 1000 mean null accuracies (maxima 9.7 to 12.5%). Chance under "
 "this procedure (null mean) is 7.8 to 9.1%, close to the paper's 8.3%. Per subject 39.9 to 60.6%. The first "
 "run gave 44.4% and 53.4% for the contiguous readings with the same code and seeds; the cause was not traced, "
 "the likeliest being rounding in the third axis of each fold's state space.")

o=O['att-weights-cortex']
o.clear()
o.update({'claim':'att-weights-cortex','outcome':'reproduced','assumed':True,
 'notebook':'reproduce_zhang_2021.ipynb','output':'claim:att-weights-cortex','measured':4,
 'notes':("With the encoding-model threshold (ii), the human-presence weight is positive and above the "
  "vehicle-presence weight in FFA, OFA and EBA, and the reverse holds in RSC, PPA and OPA, in 4 of 5 subjects "
  "under each weight reading (OLS B, denoised B_L, Q_S); S2 fails in EBA (human 0.335, vehicle 0.416 with B, "
  "no threshold). Without a threshold (i) the pattern holds in 3 of 5 under each reading, EBA failing in S2 "
  "and S3 (B, B_L) or S1 and S2 (Q_S). FFA, OFA, RSC, PPA and OPA hold in all five subjects under every "
  "reading, so the outcome rests on EBA and on the threshold; LOS-bodies alone holds in 5 of 5 under (ii). Of "
  "the other named regions, MT+ (4 of 5) and LO (4 or 5) follow the human-presence dimension and IPS (5 of 5) "
  "the vehicle-presence dimension; SEF (2), FEF (2 or 3), FO (1 to 3) and IFS (2 or 3) are mixed. Measured is "
  "the count under threshold (ii) with the OLS weights, the first reading that matches."),
 'deviations':[
  ("Assumed that group-atlas regions on fsaverage can stand in for the paper's per-subject localizer ROIs, "
   "which are not public; the claims file leaves this to the author and names an fsaverage atlas through the "
   "data set's mappers. FFA (mFus and pFus faces), OFA (IOG-faces), EBA (LOS, ITG and MTG bodies), PPA "
   "(CoS-places), OPA (TOS-places, right hemisphere only) and MT+ (hMT) from visfAtlas (Rosenke et al. 2021), "
   "whose authors relate the fusiform face areas to the FFA, the lateral body areas to the EBA and CoS-places "
   "to the PPA; RSC, LO, FO, IFS, IPS, FEF and SEF from HCP-MMP1.0 areas of the same names. Other definitions "
   "of the body, face and place areas are shown as variants."),
  ("The WordNet model of threshold (ii) follows the paper's deconvolution model (Methods, Deconvolution of the "
   "Hemodynamic Response in the Attention Task: WordNet labels, FIR delays 1 to 4 TRs, ridge with 10-fold "
   "cross-validation), fitted on the non-deconvolved BOLD of the three conditions for the voxels the regions "
   "reach. The ridge parameter is one per subject, the one with the highest mean prediction correlation (an "
   "assumption; the paper does not say), and a voxel passes when the correlation of its held-out prediction "
   "has one-sided p < 0.05 by the t distribution (the claims file leaves the test open)."),
  "Five of the paper's six subjects; S4 is not released."]})

o=O['game-weights-two-groups']
o.clear()
o.update({'claim':'game-weights-two-groups','outcome':'not_reproduced','assumed':True,
 'notebook':'reproduce_zhang_2021.ipynb','output':'claim:game-weights-two-groups',
 'notes':("Only S7 can be tested by region: S1's video game data (73,594 voxels) match no mapper in the data set, "
  "current or superseded, so S1 and the consistency between subjects could not be tested. In S7, three to five "
  "of the eight dimensions fail the grouping under every reading, where one may fail: dead, safe explore and "
  "unsafe explore under every reading, and engage far, run away, round start or engage close under some (4 "
  "fail with OLS or denoised weights and no threshold, 3 with the Bonferroni threshold, 5 with Q_S under "
  "either order). Safe explore has negative OLS weights in all nine regions (-0.008 to -0.240). Since the "
  "criterion asks for the pattern in both subjects, failing in S7 decides the outcome. In the variant not "
  "taken from the paper, the correlation of S1's denoised weight maps across voxels splits the nine dimensions "
  "into exactly the paper's two groups, while S7's split into safe and unsafe explore against the rest."),
 'deviations':[
  ("Assumed HCP-MMP1.0 areas on fsaverage for the regions the paper names (TPJ as TPOJ1-3, PGi and PGs; "
   "precuneus as 7m, PCV, POS2, 31pd and 31pv; prefrontal as the dorsolateral, inferior frontal, orbital and "
   "polar and medial prefrontal areas of Glasser et al. 2016; motor 4; premotor 6a, 6d, 6v, 6r, 55b and PEF; "
   "supplementary motor 6ma and 6mp; IPS as IPS1, IP0-2, LIPv, LIPd, VIP, MIP and AIP; FEF; SEF as SCEF), in "
   "place of the paper's ROIs, which are not public."),
  ("Threshold (ii) uses the nine-state OLS model, 10 contiguous folds, one-sided t test of the prediction "
   "correlation, Bonferroni over all of the subject's voxels, as the claims file names it. A dimension counts "
   "when its mean weight is positive in each of its group's regions and the mean over them is above the mean "
   "over the other group's regions; a stricter variant is shown."),
  "S1 could not be placed on the cortex; S7 has no flash dimension."]})

o=O['game-csi']
o['notes']=o['notes']+(" With the labels one TR later, where the CSI peaks in both subjects, readings (a) and (b) are "
 "within tolerance in both subjects (S1 0.728 and 0.760, S7 0.566 and 0.583) and reading (c) is not; the paper "
 "does not say whether the game labels were shifted.")

o=O['fig3b-state-relations']
o['notes']=("Under every sign, order, Bonferroni and null-centre reading, S1 has 44 to 48 and S7 20 to 33 "
 "significant off-diagonal projections (p < 0.01 corrected, 20,000 permutations, smallest p 5e-5), 10 to 20 "
 "pairs are significant in one direction only, and the subjects share 12 to 27 of their significant pairs. "
 "Centring the two-sided test on the null's mean in place of zero changes the counts by at most one pair. The "
 "paper's matrix could not be compared pair by pair.")

o=O['game-classification']
o['measured']=[46.5,33.8]
o['notes']=("Every reading is above its null (p = 0.001; chance under this procedure 10.8 to 16.4%, against the "
 "paper's 11%). S7 is within 30.4 +/- 4.2% with contiguous folds (26.4 to 33.8%) and above it with random folds "
 "(36.8 to 46.5%). S1 is above 32.8 +/- 3.8% under every reading (42.8 to 54.6%), so no reading puts both within "
 "tolerance; with the labels one TR later the same holds (S1 45.7 to 60.5%, S7 28.4 to 50.9%). Random folds put "
 "autocorrelated neighbouring TRs in training and test sets and give higher values; the outcome does not depend "
 "on the fold scheme. The S1 data are six whole runs of 325 TRs (65 min) where the paper reports 90 min, so they "
 "may not be the data the paper analysed, which could account for S1 being above the paper's value. Measured is "
 "the first reading (contiguous folds, Euclidean, single-state TRs).")
o['deviations']=o['deviations']+[("Under single-state labels a class with too few TRs in a training fold is left "
 "out of that fold and the fold's balanced accuracy is taken over the classes it could predict; in the first "
 "run such a class was scored with a recall of 0.")]

d['inputs']=[
 {'what':("visfAtlas, probabilistic functional atlas of occipito-temporal cortex on fsaverage (Rosenke et al. 2021, "
  "Cerebral Cortex 31:603), files FreeSurfer/lh.visfAtlas.annot and rh.visfAtlas.annot from the zip its authors "
  "publish at https://download.brainvoyager.com/data/visfAtlas.zip, SHA-256 "
  "2eae192d3aeab8f9812991c8a9bc2822d10c4d0a621172aaa43df1900660799d, checked on reading; used for "
  "att-weights-cortex"),
  'source':'doi:10.1093/cercor/bhaa246'},
 {'what':("HCP-MMP1.0 parcellation projected on fsaverage, lh.HCP-MMP1.annot and rh.HCP-MMP1.annot (MD5 "
  "46a102b59b2fb1bb4bd62d51bf02e975 and 75e96b331940227bbcb07c1c791c2463, checked on reading); used for "
  "att-weights-cortex and game-weights-two-groups"),
  'source':'doi:10.6084/m9.figshare.3498446.v2'}]

F=d['findings']
for f in F:
    if f['statement'].startswith('The S1 video game data hold 1950 TRs'):
        f['statement']=("The S1 video game data hold 1950 TRs (65 min at the 2.0045 s TR), where the data description "
         "and the paper say one subject played for 90 minutes in six 15-min runs. The correlation of consecutive "
         "TRs drops to -0.44 to -0.48 exactly at TRs 325, 650, 975, 1300 and 1625, so the data are six blocks of "
         "325 TRs (10.9 min each), the 325-volume run length the paper gives for its acquisitions. S7's 1320 TRs "
         "(44 min) match the stated 45 minutes.")
    if f['statement'].startswith('No mapper matches the S1 video game data'):
        f['statement']=("No mapper matches the S1 video game data, which have 73,594 voxels; the S1 mapper has "
         "51,608 voxels, the voxel set of S1's attention data, and the superseded mappers in Mappers/old have "
         "81,137 (S1), 84,038 (S5) and 86,842 (S6). S1's game weights cannot be placed on fsaverage or the "
         "flatmap with the files given.")
    if f['statement'].startswith('The functional ROIs, and the localizer'):
        f['statement']=("The functional ROIs, and the localizer and retinotopic mapping data the paper used to "
         "define them, are not in the data set, so the cortical claims of Figures 2 and 4 cannot be tested on the "
         "paper's regions; this attempt used public fsaverage atlases through the data set's mappers.")
F.append({'kind':'methods_unavailable','statement':("Question for the paper's authors. Were the video game state "
 "labels shifted in time against the BOLD, which is not deconvolved? The CSI peaks with the labels one TR "
 "later in both subjects (S1 0.729 against 0.691 at lag 0). This attempt used the labels as stored.")})
F.append({'kind':'methods_unavailable','statement':("Question for the paper's authors. Which encoding models and "
 "tests set the voxel thresholds of Figures 2 and 4, and how was the ridge parameter of the WordNet "
 "deconvolution model chosen? The attention cortical claim holds in 4 of 5 subjects with a WordNet-model "
 "threshold and in 3 of 5 without one. This attempt chose one ridge parameter per subject by mean prediction "
 "correlation and a one-sided t test of the correlation.")})

V={'date':'2026-11-14','kind':'agent',
 'by':'Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
 'reviewed':("The first executed notebook (commit 1caefc7) with the conclusion cells and the summary removed, the "
  "helper module and the claims file, with the paper's full text. The verifier read the archive's mappers "
  "(including Mappers/old/S1.hdf) and tested the helpers (jsd, pca_scores, positions, shuffle_conditions, "
  "balanced_accuracy) on synthetic inputs. It had no attempt record."),
 'results':[]}
R=V['results']
def add(c, agrees, out, reason, response): R.append({'claim':c,'agrees':agrees,'outcome':out,'reason':reason,'response':response})
add('fig1-csi-s2', True, 'reproduced',
 ("Cell 15: with the code's positions (R3) S2 gives 0.740, 0.718 and 0.676, all within tolerance and above every "
  "null value under both permutation readings (p <= 1/1001). The R2 reading also passes. The 2-D variant fails "
  "only on attend-humans (0.664 against 0.675). Problem 1: each attentive condition is z-scored per voxel, so the "
  "OLS weight of the attention variable is about 1e-14 and the code's third axis is set by rounding noise; the R3 "
  "CSIs depend on the machine. For S2 the R2 5 to 95% range stays within tolerance, so the claim does not hinge "
  "on it. Not checked: whether the code's own third axis on the full data is also noise; printing the code's "
  "coeffs norm for the attention row would settle it."),
 ("Printed the norm of each row of the code's own OLS coefficients in voxel space: the attention row is about "
  "1e-13 against about 1e2 for human and vehicle, so the code's third axis is noise too. This run gives 0.743, "
  "0.721 and 0.675, which shows the run-to-run movement; the record and notebook give the new values and say "
  "why they move. Outcome unchanged."))
add('att-csi-group', True, 'reproduced',
 ("Cell 18, R3: the means are 0.665, 0.729 and 0.525, all within tolerance. Reading (b), the group mean above every "
  "mean null value, passes for all three conditions. Reading (a) fails for passive because S3 passive (0.061) does "
  "not exceed every null value."),
 "No change beyond the R3 values of this run (0.665, 0.731, 0.524), which move by rounding as for fig1-csi-s2.")
add('supp-csi-per-subject', True, 'reproduced',
 ("Cell 20: R3 has 10 of 12 values within tolerance, R2 has 11 of 12, and all 12 are significant at p < 0.01 under "
  "null (a). The misses are S3 passive (0.061 against 0.05 +/- 0.005) and S5 attend-humans (0.767)."),
 "No change beyond the R3 values of this run; counts and significance are the same.")
add('att-passive-lower', True, 'not_reproduced',
 ("Cell 22: at most 3 of 5 subjects count at the bound (R3, matched, ii, reading b), and 4 of 5 are needed. S1 and "
  "S6 have passive CSI at or above attend-humans, so d_mean is about 0 (p 0.38 to 0.53), and this holds under "
  "every reading. The 4 of 5 in the R1/matched/i row at p < 0.05 is the variant that does not decide. Problem 2: "
  "in the refit null (i) for R3 mixing conditions gives the attention axis a real weight while the observed third "
  "axis is noise, and the observed CSIs average 10 seeds while each null draw uses one; null (ii) has neither "
  "issue and gives the same counts. Not checked: the full null distributions, for example S2's d_mean null "
  "quantiles."),
 ("Printed the null quantiles (median, 95%, 99%, maximum) of d_mean for every subject, scheme and null: S2's 0.057 "
  "is above the 99th percentile (0.042 to 0.055) and below or near the maximum (0.052 to 0.084). Stated in the "
  "method text that null (i) for R3 is not computed as the observed value is, and that null (ii) has neither "
  "difference and gives the same counts. Outcome unchanged."))
add('att-classification', True, 'reproduced',
 ("Cell 24: contiguous folds give 44.4% (Euclidean) and 53.4% (density), and random folds with Euclidean give "
  "46.6%, all within 48.4 +/- 7.6 and above every null mean. Chance under the procedure is 7.8 to 9.1%, against "
  "the paper's 8.3%. Problem 6: shuffled TR folds put autocorrelated neighbouring TRs in both training and test "
  "sets, and contiguous folds have no gap at their edges; the attention outcome is decided under contiguous folds."),
 ("No change in method. This run gives 43.7% and 53.8% for the contiguous readings with the same code and seeds; "
  "the notes say so. Folds with a gap were not run, since the outcome already holds under contiguous folds."))
add('att-weights-cortex', True, 'blocked',
 ("Cell 25: the paper's per-subject ROIs from localizers are not deposited. Part of the claim could still be "
  "tested with an fsaverage atlas. Problem 3 (affects a conclusion): the claims file leaves the choice of an "
  "outside ROI source to the author and names an fsaverage atlas through the data set's mappers; the current "
  "mappers match the voxel counts of all five attention subjects, so the claim could have been tested in part on "
  "all five subjects with atlas ROIs (for example FFA, PPA, EBA, RSC, OPA parcels on fsaverage). The notebook "
  "gives no reason against it beyond calling it a substitute."),
 ("Tested the claim with atlas regions: visfAtlas for FFA, OFA, EBA, PPA, OPA and MT+, HCP-MMP1.0 for the other "
  "regions, mapped with the data set's mappers, all three weight readings and both thresholds, including the "
  "WordNet encoding model of reading (ii). The pattern holds in 4 of 5 subjects with the threshold and 3 of 5 "
  "without, so the outcome changes from blocked to reproduced, resting on the atlas regions and the threshold."))
add('game-csi', True, 'reproduced',
 ("Cell 28, reading (b): S1 0.702 and S7 0.581, both within tolerance and above every null value. Reading (a) "
  "misses for S7 (0.549 against a lower bound of 0.558), and reading (c) misses for both. The pass therefore "
  "depends on one reading, with 7 and 6 clusters. Problem 5: the game CSI peaks at a lag of +1 TR in both "
  "subjects; the notebook uses lag 0 without examining the shift, and at lag +1 reading (a) for S7 would fall "
  "within tolerance; the alignment of the game labels was assumed and not established."),
 ("Added the CSI with the labels one TR later under all three readings with a null: (a) and (b) are within "
  "tolerance in both subjects (S7 reading a 0.566), (c) is not. The data check now says the CSI peaks at +1 in "
  "both subjects and that lag 0 is used; a question to the authors asks how the labels were aligned. Outcome "
  "unchanged."))
add('game-mutual-negative-projection', True, 'reproduced',
 ("Cell 30: with the dataset column order, both projections are negative at p = 5e-5 in both subjects, under both "
  "sign rules. With the Table 1 order, S7's safe-explore on engage-close is -0.018 (p = 0.94), so the result "
  "depends on the order."),
 "No change; the dependence on the order is already the stated assumption.")
add('fig3b-state-relations', True, 'reproduced',
 ("Cell 32: under every reading each subject has many significant off-diagonal pairs (S1 45 or 48, S7 32 or 20), "
  "some pairs are significant in one direction only, and the two subjects' sets differ. Problem 8: the two-sided "
  "p uses |null| >= |M| centred on zero, not on the null's centre, and because rows are permuted together, "
  "mutually exclusive states keep a shifted null."),
 ("Added the test centred on the null's mean as a further reading: the counts change by at most one pair (S1 44 "
  "to 48, S7 20 to 33). Outcome unchanged."))
add('game-classification', True, 'partially_reproduced',
 ("Cell 34: every reading is significant (p = 0.001). S1 lies above tolerance under all readings (42.8 to 54.6% "
  "against 32.8 +/- 3.8), so no reading puts both subjects within tolerance. S7 is within tolerance only with "
  "contiguous folds. Chance matches the paper's 11% where all 9 classes are kept (11.1%). Problem 4: S1's game data "
  "hold 65 min where the paper says 90 min and match no mapper, so they may not be the exact input the paper used; "
  "the notebook does not draw this into game-classification. Problem 7: under reading (a) with the density rule a "
  "class can drop out of a fold while still being scored, with a recall of 0. Not checked: the S1 run structure "
  "and the accuracies with labels shifted by +1 TR."),
 ("Fixed the scoring so that a class left out of a training fold is not scored in that fold; the first reading "
  "is now 46.5% (S1) and 33.8% (S7). Added the S1 run structure (six blocks of 325 TRs, so the 65 min are six "
  "whole runs, not a subset) and the accuracies with labels one TR later (no reading puts both within "
  "tolerance). The notes now say the S1 data may differ from the paper's input, which could account for S1 "
  "being high. Outcome unchanged."))
add('game-weights-two-groups', True, 'blocked',
 ("Cell 35: the region definitions are not deposited, and S1's game data match no mapper. Only S7 could be tested "
  "in part, with an atlas. Problem 3: S7's game data match its mapper (87,000 voxels); S1's game data (73,594 "
  "voxels) match neither the current S1 mapper (51,608) nor Mappers/old/S1.hdf (81,137). The notebook never "
  "checked the old mappers."),
 ("Printed the voxel counts of the superseded mappers (none matches S1's game data) and tested S7 with "
  "HCP-MMP1.0 regions under every weight, order and threshold reading. Three to five of eight dimensions fail "
  "where one may, so the claim, which asks for the pattern in both subjects, fails in S7; the outcome changes "
  "from blocked to not_reproduced, resting on the atlas regions. S1 and the consistency between subjects remain "
  "untested."))
d['verifications']=[V]
yaml.safe_dump(d, open(p,'w'), sort_keys=False, width=110, allow_unicode=True)
PYEOF
python3 $TMPDIR/rec.py && grep -n '": \|: .*: ' attempts/zhang-2021-01.yaml | head; grep -c "rather\|—" attempts/zhang-2021-01.yaml
```

```
Exit code 1
222:  notes: 'Only S7 can be tested by region: S1''s video game data (73,594 voxels) match no mapper in the data set,
316:    reason: 'Cell 15: with the code''s positions (R3) S2 gives 0.740, 0.718 and 0.676, all within tolerance and
323:    response: 'Printed the norm of each row of the code''s own OLS coefficients in voxel space: the attention row
330:    reason: 'Cell 18, R3: the means are 0.665, 0.729 and 0.525, all within tolerance. Reading (b), the group mean
337:    reason: 'Cell 20: R3 has 10 of 12 values within tolerance, R2 has 11 of 12, and all 12 are significant at p
343:    reason: 'Cell 22: at most 3 of 5 subjects count at the bound (R3, matched, ii, reading b), and 4 of 5 are needed.
356:    reason: 'Cell 24: contiguous folds give 44.4% (Euclidean) and 53.4% (density), and random folds with Euclidean
367:    reason: 'Cell 25: the paper''s per-subject ROIs from localizers are not deposited. Part of the claim could still
373:    response: 'Tested the claim with atlas regions: visfAtlas for FFA, OFA, EBA, PPA, OPA and MT+, HCP-MMP1.0 for
380:    reason: 'Cell 28, reading (b): S1 0.702 and S7 0.581, both within tolerance and above every null value. Reading
0
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/zhang-2021 2>&1 | tail -5; ls tools | head -30; git diff --stat
```

```
0 error(s)
__pycache__
agent_run.py
archive_transcripts.sh
archives
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
contributors.py
conversion_issue.py
datasets.py
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rln "attempt.schema" tools tests scripts 2>/dev/null | head; python tools/entry.py --help 2>&1 | head -20
```

```
tools/build_site.py
tests/test_build_site.py
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--fresh] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python,hash}
                entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py run entries/zhang-2021 2>&1 | tail -3; git status --short; date -u
```

```
pass  reproduce_zhang_2021.ipynb  (3068 s, reused)
reused the executed copies of 2026-11-14 14:48 UTC: nothing the run reads has changed since (hash 00e6cc5dd07d). Nothing was executed and no environment was built; --fresh runs it again.
 M attempts/zhang-2021-01.yaml
 M entries/zhang-2021/README.md
 M entries/zhang-2021/entry.yaml
 M entries/zhang-2021/reproduce_zhang_2021.ipynb
 M entries/zhang-2021/statespace.py
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
Sat Nov 14 14:50:21 UTC 2026
```

**Agent calls Bash**

```bash
cd  grep -c "rather\|—" entries/zhang-2021/reproduce_zhang_2021.ipynb entries/zhang-2021/statespace.py entries/zhang-2021/README.md attempts/zhang-2021-01.yaml
```

```
entries/zhang-2021/reproduce_zhang_2021.ipynb:0
entries/zhang-2021/statespace.py:0
entries/zhang-2021/README.md:0
attempts/zhang-2021-01.yaml:0
```

**Agent**

I've worked through all of the verifier's round-1 report. The final run of `python tools/entry.py all entries/zhang-2021` passed in 51 minutes, under the 60-minute limit, and the entry and record checks report 0 errors. Nothing is committed.

**Outcome changes (both were blocked as `data_missing`)**
- **att-weights-cortex: now reproduced, resting on assumptions.** This follows the verifier's point 3. I used two public fsaverage atlases through the data set's own mappers: visfAtlas (Rosenke et al. 2021) for FFA, OFA, EBA, PPA, OPA and MT+, and HCP-MMP1.0 for RSC, LO, FO, IFS, IPS, FEF and SEF.
  - With the claims file's threshold (ii), the WordNet encoding model I added to the helper, the pattern holds in 4 of 5 subjects under all three weight readings. Without a threshold it holds in 3 of 5.
  - FFA, OFA, RSC, PPA and OPA hold in all five subjects. The outcome rests on EBA, which fails in S2 under every reading.
- **game-weights-two-groups: now not reproduced, resting on assumptions.** Only S7 can be placed on the cortex. In S7, 3 to 5 of the 8 dimensions fail the grouping under every reading, where the criterion allows one. S1 and the consistency between the two subjects stay untested.
  - In a variant that doesn't decide the outcome, S1's denoised weight maps cluster into exactly the paper's two groups.

The other nine outcomes are unchanged.

**Other fixes and added outputs**
- **Code's third axis:** the code's own coefficient for the attention variable is about 1e-13, against about 1e2 for human and vehicle, so its third axis is rounding noise too. As a result, the values from the code's own axis move slightly between runs: S2's are now 0.743, 0.721 and 0.675, against 0.740, 0.718 and 0.676 before. Classification on contiguous folds moved from 44.4% to 43.7% with the same seeds; I did not trace the cause. All numbers in the notebook and record match this run.
- **att-passive-lower:** the full null quantiles are printed. S2's difference (0.057) is above the 99th percentile but not above every null value. I stated that the refitted null is not computed the way the observed value is.
- **S1 game data:** they are six whole runs of 325 TRs, so the 65 minutes are not a subset of a longer session. They match no mapper, including the superseded ones in `Mappers/old`. The record finding is revised, and game-classification now notes that this could explain why S1 comes out above the paper's value.
- **Game labels one TR later:** the game CSI and classification are now also run this way. S7's CSI under reading (a) is then within tolerance, and no classification reading puts both subjects within tolerance.
- **Classification scoring:** a class dropped from a training fold is no longer scored with a recall of 0. The first reading is now 46.5% (S1) and 33.8% (S7).
- **fig3b:** added a test centred on the null's mean. The counts change by at most one pair.
- **Record:** added the round-1 `verifications` block, the two atlases under `inputs` (pinned by DOI and checksum), and two new questions for the paper's authors: how the game labels were aligned in time, and which encoding models set the map thresholds.

**Not done**
- Folds with a gap at their edges (point 6) were not run. The outcomes already hold under contiguous folds, and S1 is above tolerance under both fold schemes.
- No question was added to `questions/zhang-2021.yaml`, because the verifier reported no misreading of the claims file.
- The full run now takes 51 minutes, up from 28, mostly because of the WordNet model.

## End of run

76 turns, 145 minutes, $5.94 at API prices, result: success.
