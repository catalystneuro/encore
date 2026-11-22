# hasnain-2025 · claims · run 44972751719

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ | grep -i hasnain; ls claims | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ | grep -i hasnain; ls claims | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,200p docs/protocol.md; ls paper | grep -i -E "hasnain"; ls paper | head
```

```
# Protocol for an attempt

Version: `pilot-18`. Record this version in the attempt's provenance.

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
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml | head -150; cat papers/datasets/hasnain-2025.yaml; wc -c paper/*; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 25,140p claims/fouke-2025.yaml; tail -60 claims/fouke-2025.yaml; cat papers/datasets/hasnain-2025.yaml; wc -c paper/*; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I've read the protocol and the example claims file. Next I'm reading the paper text.

**Agent calls Bash**

```bash
cat papers/datasets/hasnain-2025.yaml; wc -c paper/*; ls paper
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml",
 "offset": 40,
 "limit": 90
}
```

```
40	    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the
41	    species' median speeds for the nine whole-field stimuli computed here are within 10% of the
42	    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is
43	    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be
44	    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
45	    the counts per species are compared instead. The sign of the zebrafish turning response
46	    to codes 9 and 11 is reported, as the code and the protocol file disagree on which of them
47	    is lateral right.
48	- id: fig1d-dc-faster-all-codes
49	  statement: Danionella cerebrum (DC) swim at a higher median velocity than zebrafish (ZF)
50	    across the visual stimuli.
51	  source: Results, Larval DC exhibit higher average swimming speeds, paragraph 1; Figure 1D
52	  quote: DC show a significantly higher median velocity across all stimuli than ZF
53	  statistics:
54	  - test: two-way ANOVA, main species effect
55	    p: 0.05
56	    p_relation: "<"
57	  criterion: Tested without stimulus names, over all 21 stimulus codes. For each fish and code
58	    the median over trials of the trial speed in pixels per second; a two-way ANOVA (type II)
59	    of these values on species, code and their interaction. Reproduced when the species effect
[... 70 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.10.17.682917.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1101-2025.10.17.682917.txt').read(); i=t.find('Neural net', 50000); print(t[i:i+42000])"
```

```
<persisted-output>
Output too large (40.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/f382155f-ed6d-41ec-b398-cb2a77301659/tool-results/btc9mouuw.txt

Preview (first 2KB):
Neural network models Neural network models were trained to predict single trial neural firing rates from orofacial movements ( Fig. 3a ). Orofacial movements were provided to the network as input in the form of singular vectors of video data and motion energy data. Video data from both the side view and the bottom view were concatenated so that both movement direction and amplitude could be captured. 100 video and 100 motion energy singular vectors (SV) were obtained through the Facemap GUI 68 . Training data consisted of 70% of trials and the remaining trials were used for testing. Before splitting the data into train/test sets, the number of left and right trials were sampled without replacement equal to the minimum number of trials between the trial types. The neural network architecture was kept the same as in ref 68 , consisting of an initial one-dimensional convolutional layer that learned ten temporal filters from the input data, followed by a 2-layer feedforward network with ReLU nonlinearity, and a final readout layer that transformed learned features to predictions of single trial firing rates. The feedforward layers had dimensionalities of 50 and 256. The readout layer was a fully-connected layer with output dimensions equal to the number of neurons in a session. Dropout with a probability of 0.2 was added to the feedforward layers. Individual networks were trained to predict neural activity from each session over 1000 epochs or until the test loss decreased by less than 1 × 10 −5 for 20 consecutive epochs. The learning rate was initialized at 1 × 10 −2 and decreased by 10% if the test loss increased for 5 consecutive epochs. Optimization was performed using the AdamW optimizer in PyTorch. Equal numbers of left and right trials were sampled a
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/f382155f-ed6d-41ec-b398-cb2a77301659/tool-results/btc9mouuw.txt"
}
```

```
1	Neural network models Neural network models were trained to predict single trial neural firing rates from orofacial movements ( Fig. 3a ). Orofacial movements were provided to the network as input in the form of singular vectors of video data and motion energy data. Video data from both the side view and the bottom view were concatenated so that both movement direction and amplitude could be captured. 100 video and 100 motion energy singular vectors (SV) were obtained through the Facemap GUI 68 . Training data consisted of 70% of trials and the remaining trials were used for testing. Before splitting the data into train/test sets, the number of left and right trials were sampled without replacement equal to the minimum number of trials between the trial types. The neural network architecture was kept the same as in ref 68 , consisting of an initial one-dimensional convolutional layer that learned ten temporal filters from the input data, followed by a 2-layer feedforward network with ReLU nonlinearity, and a final readout layer that transformed learned features to predictions of single trial firing rates. The feedforward layers had dimensionalities of 50 and 256. The readout layer was a fully-connected layer with output dimensions equal to the number of neurons in a session. Dropout with a probability of 0.2 was added to the feedforward layers. Individual networks were trained to predict neural activity from each session over 1000 epochs or until the test loss decreased by less than 1 × 10 −5 for 20 consecutive epochs. The learning rate was initialized at 1 × 10 −2 and decreased by 10% if the test loss increased for 5 consecutive epochs. Optimization was performed using the AdamW optimizer in PyTorch. Equal numbers of left and right trials were sampled and subsequently divided into an 80/20 train/test split. The variance explained of a single neuron’s firing rates were calculated as: V E = 1 - ∑ t x t - x ^ t 2 ∑ t x t - x ¯ 2 where x t is the single trial firing 
[... 208 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -l "relation: reuses" papers/datasets/*.yaml | head -5; grep -rn "data_missing\|data: elsewhere\|not_public\|unavailable" claims/*.yaml | head -20; grep -n "data:" docs/*.md | head -30
```

```
papers/datasets/alasfour-2024.yaml
papers/datasets/burman-2023.yaml
papers/datasets/cambrainha-2025.yaml
papers/datasets/clark-2026.yaml
papers/datasets/du-2026.yaml
claims/andrews-2024.yaml:174:  data: elsewhere
claims/azcorra-2023.yaml:729:  data: elsewhere
claims/azcorra-2023.yaml:750:  data: elsewhere
claims/azcorra-2023.yaml:774:  data: elsewhere
claims/azcorra-2023.yaml:782:  data: elsewhere
claims/berg-2020.yaml:208:  data: elsewhere
claims/berg-2020.yaml:240:  data: elsewhere
claims/berg-2020.yaml:263:  data: elsewhere
claims/berg-2020.yaml:295:  data: elsewhere
claims/berg-2020.yaml:319:  data: elsewhere
claims/berg-2020.yaml:332:  data: elsewhere
claims/berg-2020.yaml:353:  data: elsewhere
claims/berg-2020.yaml:374:  data: elsewhere
claims/berg-2020.yaml:394:  data: elsewhere
claims/berg-2020.yaml:557:  data: elsewhere
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 236,300p docs/protocol.md; grep -l "^paper: " claims/burman-2023.yaml claims/alasfour-2024.yaml; head -60 claims/burman-2023.yaml; ls schema* tools/ 2>/dev/null; ls docs
```

```
`inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dataset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dataset.
   - `with_labels` is for outside sources that only name or map codes the
     dataset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
     the missing names are recorded as a finding (`metadata_insufficient`).
   - When outside data has to be matched to the dataset's cells, sessions
     or subjects, a claim of its own (`kind: link`) tests the link. Link
     claims are the registry's checks, not findings of the paper, so the
     author adds them to the claims file; they are the only claims the
     author writes. A link claim says how
     records are matched (an identifier, or, where there is none, summary
     values the paper or its code published, such as per-condition medians),
[... 169 more lines not kept]
```

**Agent**

The Burman 2023 claims file is a close template: it also reuses a public dataset alongside the authors' own unpublished recordings. Next I'm reading the claims schema and the linked subspaceID code.

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; sed -n 60,140p claims/burman-2023.yaml
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
[... 262 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/economolab/subspaceID && cd subspaceID && git log -1 --format='%H %ci' && find . -type f -not -path './.git/*' | head -100 && cat README* | head -80
```

```
d593949fef8a39fe0a6eb54a21fc05cbca7bae84 2024-10-24 09:11:17 -0400
./__init__.py
./manopt/CREDITS.txt
./manopt/LICENSE.txt
./manopt/manopt/tools/multiprod.m
./manopt/manopt/tools/._multiskewh.m
./manopt/manopt/tools/smallestinconvexhull.m
./manopt/manopt/tools/._dsqrtm.m
./manopt/manopt/tools/productmanifold.m
./manopt/manopt/tools/multisqnorm.m
./manopt/manopt/tools/plotprofile.m
./manopt/manopt/tools/._powermanifold.m
./manopt/manopt/tools/matrixlincomb.m
./manopt/manopt/tools/factorygpuhelper.m
./manopt/manopt/tools/checkhessian.m
./manopt/manopt/tools/lyapunov_symmetric.m
./manopt/manopt/tools/checkdiff.m
./manopt/manopt/tools/lyapunov_symmetric_eig.m
./manopt/manopt/tools/._multitrace.m
./manopt/manopt/tools/._multiscale.m
[... 125 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/subspaceID && find . -type f -not -path './.git/*' -not -path './manopt/*' && cat example.m; for f in $(find . -name "*.m" -not -path './manopt/*' -not -name example.m); do echo "=== $f"; cat $f; done
```

```
./__init__.py
./funcs.py
./example.ipynb
./LICENSE
./__pycache__/funcs.cpython-311.pyc
./__pycache__/desktop.ini
./orthogonal_subspaces.m
./README.md
./example.m
./desktop.ini
./exampleData.mat

% clear,clc,close all

% add manopt and funcs directory to path
manoptPath = pwd; % path to manopt 
addpath(genpath(fullfile(manoptPath,'manopt')))

%% LOAD SOME DATA

[... 255 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/subspaceID && grep -n "def \|alpha\|zscore\|eigs\|dNull\|= 1[05]" funcs.py | head -40; python3 -c "
import json;nb=json.load(open('example.ipynb'))
for c in nb['cells']:
  if c['cell_type']=='code': print(''.join(c['source'])[:800]); print('---')" | head -120
```

```
4:from scipy.stats import zscore
17:def create_cost_and_egrad(manifold, eigvalsNull, eigvalsPotent, dNull, dPotent, Ppotent, Pnull, covNull, covPotent):
22:    def cost(Q):
26:        normNull = np.sum(eigvalsNull[1:dNull])
32:    def euclidean_gradient(Q):
34:        normNull = np.sum(eigvalsNull[1:dNull])
40:def orthogonal_subspaces(nNeurons, dNull, dPotent, covNull, covPotent):
42:    # Q, matrix of size (nNeurons,nDimensions), where nDimensions = dNull + dPotent
44:    #   The first dPotent columns corresponds to the potent subspace, and the last dNull columns the null subspace
50:    manifold = Stiefel(nNeurons, dNull + dPotent)
59:    eigvalsPotent, _ = np.linalg.eig(covPotent) # hoping that these all eigs are positive, still only divinding by largest algebraic +ve values
63:    Ppotent = np.concatenate((np.eye(dPotent), np.zeros((dNull,dPotent))), axis=0)
64:    Pnull = np.concatenate((np.zeros((dPotent,dNull)), np.eye(dNull)), axis=0)
67:    cost, egrad = create_cost_and_egrad(manifold, eigvalsNull, eigvalsPotent, dNull, dPotent, Ppotent, Pnull, covNull, covPotent)
import matplotlib.pyplot as plt
import autograd.numpy as np
from scipy.io import loadmat
from scipy.stats import zscore

import pymanopt
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000363/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['draft_version']['name']); print(d.get('most_recent_published_version'))"; curl -s https://api.dandiarchive.org/api/dandisets/000363/versions/draft/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['description'][:2000]); print(d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent**

I have what I need from the paper and code. Before writing, I'm checking how the quote checker normalizes text, since this text has unusual spacing.

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py
```

```
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
import sys
import unicodedata
from pathlib import Path

[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:4000]); print([k for k in s['properties']])"
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 83 more lines not kept]
```

**Agent**

Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/hasnain-2025.yaml",
 "content": "# Claims for Hasnain, Han & Economo (2025), \"Mapping neural subspace dynamics onto the structure\n# of the mouse descending motor system\", bioRxiv doi:10.1101/2025.10.17.682917, tested on\n# DANDI:000363 (Mesoscale Activity Map Dataset), which the paper reuses.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-22,\n# protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).\n#\n# Text read. The preprint (version 1, posted 2025-10-17), full text from PMC (PMC12632980), in\n# paper/10.1101-2025.10.17.682917.txt: Abstract, Introduction, Results, Discussion, Methods, the\n# legends of Extended Data Figures 1 to 3, and the legends of Figures 1 to 4. The paper has no\n# separate supplement (PMC lists none); the Extended Data legends are in the text. No PDF was\n# supplied, so no figure was read; every claim rests on the text.\n#\n# Code read. github.com/economolab/subspaceID, commit d593949fef8a39fe0a6eb54a21fc05cbca7bae84,\n# the only code the paper links (\"Code for identifying movement-null and movement-potent\n# subspaces\"). It holds orthogonal_subspaces.m (the manopt optimization of the Methods'\n# objective, each term normalized by the sum of the top-d eigenvalues of its covariance, with a\n# regularization weight alpha that example.m sets to 0), example.m (z-scores each neuron over all\n# bins and trials, takes the covariance of stationary and of moving bins, fixes 15 dimensions per\n# subspace, rng(101)), and a Python port (funcs.py, example.ipynb). It holds none of the paper's\n# other analyses (session selection, movement masks, dimensionality, variance explained,\n# selectivity, decoding, UMAP). The rest of the paper's code \"will be made available on Github\n# upon publication\".\n#\n# Data the paper used, as it reports them.\n# (1) The paper's own recordings (Figures 1 to 3, Extended Data Figures 2 and 3). 9 mice (3 male,\n# 6 female, C57BL/6J or VGAT-ChR2-EYFP negative), 27 sessions, delayed-response auditory licking\n# task (sample tones, 1.2 s delay, go cue). Neuropixels 1.0 (4 sessions) and 2.0 (23 sessions) in\n# ALM (13 sessions, 49 L-ETNs, 1020 UNs) and tjM1 (14 sessions, 55 L-ETNs, 830 UNs); L-ETNs\n# phototagged by retrograde ChR2 from the medulla and confirmed by collision tests. 400 Hz side and\n# bottom video, motion energy, DeepLabCut tongue tracking, Facemap singular vectors. These data are\n# not public (\"Data will be made publicly available upon publication\") and are not in DANDI:000363.\n# Their claims are kept, as data the paper recorded (data: dataset), and cannot be tested here.\n# (2) The MAP dataset, DANDI:000363 (Chen et al. 2024, ref 58), used for Figure 4: Neuropixels\n# recordings in mice doing the same delayed-response task. The paper takes sessions with at least\n# 30 units classified as 'good' in each region of interest: bilateral ALM sessions (20 sessions,\n# 10 mice, 961 right and 1055 left ALM units), and simultaneous ALM and medullary reticular nuclei\n# sessions (IRN, GRN and PARN; 604 ALM and 724 medulla units). ALM units are those labelled MOs in\n# the Allen CCF on probes described as targeting ALM. Movement is taken from the provided jaw and\n# nose keypoint tracking (side camera, 300 Hz). Measured variables used: unit spike times, unit\n# CCF location and quality label, probe target, trial times and types (lick left or right,\n# correct or error), and the jaw and nose keypoints.\n#\n# Method for the claims on DANDI:000363, from the Methods (\"Curation of Mesoscale Activity Map\n# Dataset\", \"Subspace identification\", \"Dimensionality of subspaces\", \"Identifying selective\n# neurons\", \"UMAP embeddings\", \"Cross-region decoding\") and the subspaceID code. Cited in the\n# criteria as M1 to M10. Where the paper leaves a detail open, the readings are named.\n# M1 Sessions. Sessions with at least 30 'good' units in each region of interest (Methods). The\n#    count of ALM and medulla sessions is open, between (S1) 16 sessions (Results; Figure 4c\n#    legend; every statistic of Figure 4 has n = 16) and (S2) 11 sessions from 7 mice (Methods).\n#    The bilateral ALM count is 20 sessions from 10 mice in both places, but the unit count\n#    differs (1116 neurons in the Results, 2016 units in the Methods).\n# M2 Units. Open between (U1) only units labelled 'good' in the regions of interest and (U2) all\n#    units in those regions of the selected sessions; the Methods use 'good' only to select\n#    sessions. The reported unit counts (604 ALM, 724 medulla; 961 and 1055 ALM) decide between\n#    them where they can. The ALM hemisphere in ALM and medulla sessions is not stated; all ALM\n#    units of the session are pooled, a reading of \"ALM: 604 units\". Medulla units are those in\n#    IRN, GRN or PARN, both hemispheres pooled.\n# M3 Firing rates. Spike counts in 5 ms bins, smoothed with a causal Gaussian kernel of 20 ms\n#    s.d. (Methods). Each neuron's single-trial activity has the mean baseline activity across\n#    trials subtracted and is divided by the standard deviation across trials, baseline -2.1 to\n#    -1.85 s before the go cue (Subspace identification; the Coding direction section gives -2.15\n#    to -1.85 s). The z-scoring of example.m (over all bins and trials) is a variant. All correct\n#    and error trials enter the subspace estimate (Methods). The trial window is not stated for\n#    the MAP data. Readings (W1) -2.15 s to +1.5 s around the go cue (the baseline start to the end\n#    of the late response epoch, the widest span the Methods' windows give) and (W2) -1.8 s to\n#    +1.5 s (the task epochs of the selectivity analysis only).\n# M4 Moving and stationary bins. Per session, the velocity magnitude of the jaw and nose\n#    keypoints, averaged, is thresholded by hand; movement bouts (at least 100 ms continuous)\n#    separated by 50 ms or less are merged (Methods). The threshold is open; the paper's procedure\n#    for its own data sets it between the two modes of the bimodal histogram (Videography and\n#    behavioral analysis), and that is the reading here. Whether supra-threshold runs shorter than\n#    100 ms count as moving is open, between (B1) they are stationary and (B2) they are moving.\n#    Keypoint velocities are resampled to the 5 ms bins.\n# M5 Subspaces. The Methods' objective, solved with manopt trust regions as orthogonal_subspaces.m\n#    does, alpha 0, computed in each region of a session independently (Results, paragraph on\n#    MAP). The dimensions d_null and d_potent are the number of eigenvalues of the stationary and\n#    moving covariances above the 95th percentile of 1000 shuffles of the time bins of each neuron\n#    separately (Dimensionality of subspaces). The Methods add a garbled sentence on sessions with\n#    forty or fewer neurons; it is read as (D1) no cap other than d_null + d_potent no larger than\n#    the number of neurons, or (D2) each dimension capped at 20 (example.m notes that above 20\n#    dimensions optimization is slow). The fixed 15 dimensions of example.m are a variant.\n# M6 Variance explained of a subspace (Figure 4c). VE = Tr(Q'CQ) / sum of the top d eigenvalues\n#    of C (Methods). Which C and which d are open. Readings (V1) C is the covariance of all\n#    single-trial activity, d the subspace's own dimension, and for both subspaces together d =\n#    d_null + d_potent; (V2) the same C normalized by its total variance, so that the two\n#    subspaces' values add up to that of both, as the paper's 37 + 41 = 78% do; (V3) C_stationary\n#    for the null and C_moving for the potent subspace, as in the objective.\n# M7 Selectivity (Figure 4b). For each unit, random equal samples of correct right and left\n#    trials; firing rate averaged within each epoch (seconds from the go cue; sample -1.8 to -1.2,\n#    early delay -1.2 to -0.5, late delay -0.5 to 0, early response 0 to 0.5, late response 0.5 to\n#    1.5); AUROC right against left, 1000 label shuffles, p the share of shuffles with |AUROC -\n#    0.5| at least the observed; significant below 0.05/5 (Bonferroni over the 5 epochs). The\n#    number of trials sampled is open; the reading is the smaller of the two trial counts. How\n#    the five epochs map onto the paper's three (sample, delay, response) is open between (E1) a\n#    unit selective in either sub-epoch counts for the epoch and (E2) each sub-epoch alone, every\n#    one reported.\n# M8 Cross-region decoding (Figure 4d). Movement-null projections of single trials. For each time\n#    bin t, ridge regression (lambda 0.01) from the source projections at t and the 8 preceding\n#    bins (D_source x 9 predictors) to all target dimensions at t; 70% of trials to train, 30% to\n#    test; R2 on the test set at each bin, averaged over all task epochs per session; paired t\n#    tests over sessions (Methods). The Results say \"the previous 40 ms\"; the Methods' 45 ms\n#    (t and 8 bins) is used. Open details. The trials used (T1 all trials, T2 correct trials\n#    only). The R2 over several target dimensions, (R1) one minus the residual over the total sum\n#    of squares pooled over dimensions, or (R2) the mean of each dimension's R2. Whether the\n#    predictors are standardized before the ridge (MATLAB's ridge() does so by default, and the\n#    paper uses it for Figure 3) is open; both are run. The ALM to ALM value is (A1) the mean of\n#    both directions per session, or (A2) each direction alone. The span averaged is the task\n#    epochs of M7, -1.8 to +1.5 s.\n# M9 Dimensionality (Figure 4e). Open between (N1) the shuffle count of M5 from the stationary\n#    bins (the Methods' only dimensionality procedure) and (N2) the participation ratio of the\n#    eigenvalues of the movement-null activity, the effective dimensionality of ref 70 that the\n#    Results cite. ALM against medulla, paired t test over sessions.\n# M10 UMAP (Figure 4f). Equal numbers of left and right correct trials, half to train and half to\n#    test; trial-averaged movement-null reconstructions (X Q Q') of both trial types concatenated\n#    in time; z-scored per unit on the training set; run_umap with 2 components, 30 neighbours,\n#    min_dist 0.3, cosine metric, fitted on the training data of ALM and medulla units together,\n#    test data transformed (Methods). umap-learn with the same parameters stands in for the MATLAB\n#    run_umap; the seed is a standard choice.\n#\n# Tolerances. The paper's stated spread where it gives one (s.d. over sessions for Figure 4c,\n# s.e.m. for Figure 4d and the paper's own data); otherwise 10% of the reported value. For a\n# directional result the paper tested, the criterion also asks for the same direction at p < 0.05\n# with the paper's test.\nschema_version: 2\npaper: doi:10.1101/2025.10.17.682917\nclaims:\n- id: own-recordings-cohort\n  statement: The paper's own recordings comprise 27 sessions in 9 mice, with 49 L-ETNs and 1020 UNs in\n    ALM (13 sessions) and 55 L-ETNs and 830 UNs in tjM1 (14 sessions), 104 of 1954 units (5.3%) being\n    L-ETNs.\n  source: Methods, Analysis of electrophysiological recordings, last paragraph; Results, Similarity in\n    subspace preference is robust to false-negatives, paragraph 1\n  quote: For ALM, our dataset consisted of 49 L-ETNs and 1020 UNs (415 single units and 605 multi units\n    from 13 sessions). For tjM1, our dataset consisted of 55 L-ETNs and 830 UNs (433 single units and 397\n    multi units from 14 sessions).\n  expected:\n  - quantity: ALM L-ETNs\n    value: 49\n    tolerance: 4.9\n  - quantity: ALM UNs\n    value: 1020\n    tolerance: 102\n  - quantity: tjM1 L-ETNs\n    value: 55\n    tolerance: 5.5\n  - quantity: tjM1 UNs\n    value: 830\n    tolerance: 83\n  criterion: Not testable on DANDI:000363, which holds the MAP recordings of Chen et al. (2024) only;\n    the paper's own recordings are not public (\"Data will be made publicly available upon publication\").\n    Were they available, counts of units passing the inclusion rules of the Methods (Bombcell 'single'\n    or 'multi', no more than 20% shared spikes with L-ETNs, sessions with at least 20 units above 1 Hz).\n- id: fig1i-selectivity-proportions\n  statement: The proportion of L-ETNs selective for trial type in each task epoch is similar to that of\n    UNs (sample 24% against 20%, delay 31% against 34%, response 60% against 51%).\n  source: Results, Cell-type specific recordings of MCtx dynamics during movement, paragraph 2; Figure 1i\n  quote: 'The proportion of L-ETNs that exhibit trial-type selectivity in each of the task epochs was similar\n    to that of the UN population (sample: 24% of L-ETNs, 20% of UNs; delay: 31% of L-ETNs, 34% of UNs; response:\n    60% of L-ETNs, 51% of UNs)'\n  expected:\n  - quantity: L-ETNs selective in sample epoch\n    value: 24\n    tolerance: 2.4\n    unit: percent\n  - quantity: UNs selective in sample epoch\n    value: 20\n    tolerance: 2.0\n    unit: percent\n  - quantity: L-ETNs selective in delay epoch\n    value: 31\n    tolerance: 3.1\n    unit: percent\n  - quantity: UNs selective in delay epoch\n    value: 34\n    tolerance: 3.4\n    unit: percent\n  - quantity: L-ETNs selective in response epoch\n    value: 60\n    tolerance: 6.0\n    unit: percent\n  - quantity: UNs selective in response epoch\n    value: 51\n    tolerance: 5.1\n    unit: percent\n  criterion: Not testable on DANDI:000363; the paper's own recordings are not public. Were they available,\n    selectivity as in M7.\n- id: fig2c-subspace-variance\n  statement: In the paper's recordings the movement-null and movement-potent subspaces capture similar\n    shares of single-trial variance (37 +- 7.5% and 41 +- 6.9%, mean +- s.d. over 27 sessions), 78% together.\n  source: Results, Subspace specificity of L-ETNs, paragraph 2; Figure 2c\n  quote: 'We found that the movement-null and movement-potent subspaces contained similar proportions of\n    neural variance and together captured 78% of the variance in single-trial neural activity ( Fig. 2c ;\n    movement-null: 37 ± 7.5%, mean ± s.d.; movement-potent: 41 ± 6.9%; n = 27 sessions).'\n  expected:\n  - quantity: movement-null variance explained\n    value: 37\n    tolerance: 7.5\n    unit: percent\n  - quantity: movement-potent variance explained\n    value: 41\n    tolerance: 6.9\n    unit: percent\n  - quantity: both subspaces variance explained\n    value: 78\n    tolerance: 7.8\n    unit: percent\n  criterion: Not testable on DANDI:000363; the paper's own recordings are not public. Were they available,\n    variance explained as in M6.\n- id: fig2e-potent-only-units\n  statement: More units than expected from random subspaces have activity almost entirely in the\n    movement-potent subspace (subspace preference near -1).\n  source: Results, Subspace specificity of L-ETNs, paragraph 2; Figure 2e; Discussion, paragraph 2\n  quote: As in previous work, we observed an unusually large number of units with activity contained almost\n    entirely within the movement-potent subspace ( Fig. 2e )\n  criterion: Not testable on DANDI:000363; the paper's own recordings are not public. Were they available,\n    the preference index of each UN (Methods, Subspace preference) compared with its distribution under\n    1000 random covariance-aligned subspaces; the paper gives no cut for \"almost entirely\".\n- id: fig2f-letn-preference-like-un\n  statement: The subspace preferences of L-ETNs cannot be distinguished from those of UNs (two-sample t\n    test, p = 0.30).\n  source: Results, Subspace specificity of L-ETNs, paragraph 3; Figure 2f\n  quote: Surprisingly, we found that the subspace preferences of L-ETNs could not be distinguished from UNs\n    ( Fig. 2f ; p = 0.30 , two-sample t -test).\n  statistics:\n  - test: two-sample t-test\n    p: 0.30\n    n: 104 L-ETNs and 1850 UNs\n  criterion: Not testable on DANDI:000363; the paper's own recordings are not public. Were they available,\n    a claim of absence judged by a two-sided two-sample t test of the preference index, L-ETNs against\n    UNs, at p < 0.05.\n- id: fig2gh-letn-span-subspaces\n  statement: In UMAP embeddings of activity reconstructed from each subspace, L-ETNs populate the full\n    extent of both the movement-null and the movement-potent embeddings, though not uniformly.\n  source: Results, Subspace specificity of L-ETNs, paragraph 4; Figure 2g, h\n  quote: L-ETNs populated the full extent of both subspaces, albeit not necessarily uniformly ( Fig. 2g , h ).\n  criterion: Not testable on DANDI:000363; the paper's own recordings are not public. Were they available,\n    UMAP as in M10 on L-ETNs and UNs; the paper judges coverage by inspection.\n- id: ed2f-false-negatives\n  statement: After excluding 140 L-ETN-like UNs (by waveform and firing statistics and nearness to lower\n    layer 5b), the subspace preferences of L-ETNs remain indistinguishable from UNs (p = 0.22).\n  source: Results, Similarity in subspace preference is robust to false-negatives; Extended Data Figure 2f\n  quote: Applying these criteria yielded 140 L-ETN-like UNs. Excluding these from the UN population did not\n    qualitatively alter any results. The subspace preferences of L-ETNs remained indistinguishable from\n    UNs ( Extended Data Fig. 2f ; p = 0.22 , two-sample t -test).\n  statistics:\n  - test: two-sample t-test\n    p: 0.22\n  expected:\n  - quantity: L-ETN-like UNs excluded\n    value: 140\n    tolerance: 14\n  criterion: Not testable on DANDI:000363; the paper's own recordings and waveforms are not public. Were\n    they available, the LDA and distance rule of the Methods, then a claim of absence judged by a two-sided\n    two-sample t test at p < 0.05.\n- id: fig3c-network-beats-linear\n  statement: Neural networks predicting single-trial firing rates from video explain 27.9 +- 20.2% of\n    the variance (mean +- s.d., 1954 neurons), more than ridge regression (10.6 +- 17.9%), paired t\n    test p = 1.1e-10.\n  source: Results, Investigating movement encoding using a nonlinear model, paragraph 1; Figure 3c\n  quote: Neural network models explained 27.9 ± 20.2% (mean ± s.d., n = 1954 neurons) of the variance in\n    MCtx activity, outperforming linear regression models (10.6 ± 17.9%; Fig. 3c ; p = 1.1 × 10 - 10 ,\n    paired two-sided t -test)\n  statistics:\n  - test: paired two-sided t-test\n    p: 1.1e-10\n    n: 1954 neurons\n  expected:\n  - quantity: neural network variance explained\n    value: 27.9\n    tolerance: 2.79\n    unit: percent\n  - quantity: ridge regression variance explained\n    value: 10.6\n    tolerance: 1.06\n    unit: percent\n  criterion: Not testable on DANDI:000363; the paper's own recordings and videos are not public. The\n    s.d. given is the spread over neurons, so 10% of each mean is used as the tolerance.\n- id: fig3d-letn-un-movement-encoding\n  statement: Movements explain L-ETN activity no better than UN activity in the neural network model\n    (26.4 +- 17.9% against 28.0 +- 20.1%, p = 0.39).\n  source: Results, Investigating movement encoding using a nonlinear model, paragraph 2; Figure 3d\n  quote: 'Again, L-ETNs could not be distinguished from UNs in terms of how well their dynamics were explained\n    by movements (L-ETN: 26.4 ± 17.9%, mean ± s.d., UN: 28.0 ± 20.1%; p = 0.39 , two-sample t -test).'\n  statistics:\n  - test: two-sample t-test\n    p: 0.39\n    n: 104 L-ETNs and 1850 UNs\n  expected:\n  - quantity: L-ETN variance explained\n    value: 26.4\n    tolerance: 2.64\n    unit: percent\n  - quantity: UN variance explained\n    value: 28.0\n    tolerance: 2.8\n    unit: percent\n  criterion: Not testable on DANDI:000363; the paper's own recordings are not public. A claim of absence\n    judged by a two-sided two-sample t test at p < 0.05.\n- id: ed3-letn-fast-switch\n  statement: L-ETN coding directions change rapidly at the go cue, before movement onset (105 +- 36 ms\n    after the go cue), while the UN switch is slower; the slope of the change from 0 to 150 ms is larger\n    for L-ETNs (paired t test, p = 7.6e-18).\n  source: Results, Coding specificity of L-ETNs; Extended Data Figure 3b to d\n  quote: L-ETN dynamics changed rapidly at the go cue, just preceding movement initiation, whereas the UN\n    state switch was slower and followed movement onset ( Extended Data Fig. 3b – d ; p = 7.6 × 10 - 18 ,\n    paired t -test between slope of curves in Extended Data Fig. 3d ; movement onset\n  statistics:\n  - test: paired t-test on bootstrap slopes\n    p: 7.6e-18\n    n: 1000 bootstrap iterations\n  expected:\n  - quantity: movement onset after go cue\n    value: 105\n    tolerance: 36\n    unit: ms\n  criterion: Not testable on DANDI:000363; the paper's own recordings are not public.\n- id: ed3a-cd-early-un-not-letn\n  statement: The identity of the upcoming movement, along the early-sample coding direction, is stably\n    encoded in UNs until the go cue but decays to baseline in L-ETNs after the sample epoch.\n  source: Results, Coding specificity of L-ETNs; Extended Data Figure 3a legend\n  quote: Further, we found that the identity of upcoming movements was stably encoded in UNs, but not L-ETNs\n    ( Extended Data Fig. 3a ).\n  criterion: Not testable on DANDI:000363; the paper's own recordings are not public. Were they available,\n    hierarchical bootstrap of CD early projections, 5 to 95% intervals against zero (Methods).\n- id: map-session-selection\n  statement: In the MAP dataset, the paper's selection gives 20 bilateral ALM sessions from 10 mice (961\n    right and 1055 left ALM units) and ALM and medulla sessions with 604 ALM units and 724 medullary\n    reticular nucleus units.\n  source: Methods, Curation of Mesoscale Activity Map Dataset (MAP); Results, A subset of null dynamics is\n    found downstream of motor cortex, paragraphs 1 and 3\n  quote: For simultaneous bilateral ALM recordings, we included 20 sessions from 10 mice, consisting of 2016\n    units (961 from right ALM and 1055 from left ALM). For simultaneous ALM and medulla recordings, we\n    included 11 sessions from 7 mice, consisting of 1328 units (604 from ALM and 724 from medulla).\n  expected:\n  - quantity: bilateral ALM sessions\n    value: 20\n    tolerance: 2\n  - quantity: right ALM units\n    value: 961\n    tolerance: 96.1\n  - quantity: left ALM units\n    value: 1055\n    tolerance: 105.5\n  - quantity: ALM units in ALM and medulla sessions\n    value: 604\n    tolerance: 60.4\n  - quantity: medulla units in ALM and medulla sessions\n    value: 724\n    tolerance: 72.4\n  criterion: Sessions and units selected as in M1 and M2. The ALM and medulla session count is open between\n    (S1) 16 (Results and Figure 4) and (S2) 11 (Methods); the bilateral ALM unit count between 2016\n    (Methods) and 1116 (Results). Reproduced when, under one reading of M2, the session counts match one\n    of the readings and every unit count is within tolerance; partially reproduced when the session\n    counts match and some unit counts do not. The count of mice is reported.\n- id: fig4b-medulla-selectivity\n  statement: Medullary reticular nucleus units are selective for lick direction in each epoch, most in the\n    response epoch (sample 7%, delay 21%, response 49% of 724 units).\n  source: Results, A subset of null dynamics is found downstream of motor cortex, paragraph 2; Figure 4b\n  quote: 'Many units exhibited selectivity for either right or left licks in different task epochs, although\n    selectivity was most prominent during the response epoch (sample: 7%; delay: 21%; response: 49%; n = 724\n    units Fig. 4b ).'\n  depends_on:\n  - map-session-selection\n  expected:\n  - quantity: medulla units selective in sample epoch\n    value: 7\n    tolerance: 0.7\n    unit: percent\n  - quantity: medulla units selective in delay epoch\n    value: 21\n    tolerance: 2.1\n    unit: percent\n  - quantity: medulla units selective in response epoch\n    value: 49\n    tolerance: 4.9\n    unit: percent\n  criterion: Medulla units of M2, selectivity as in M7. Reproduced when, under one reading of M7 and M2,\n    all three percentages are within tolerance; partially reproduced when the order (response highest,\n    sample lowest) holds but a value is outside tolerance.\n- id: fig4c-alm-null-potent-similar\n  statement: In MAP ALM the movement-null and movement-potent subspaces explain comparable variance (36.0\n    +- 7.40% and 37.1 +- 8.70%, mean +- s.d.; paired t test p = 0.15, 16 sessions).\n  source: Results, A subset of null dynamics is found downstream of motor cortex, paragraph 3; Figure 4c\n  quote: 'In the MAP dataset, the variance explained by movement-null and movement-potent subspaces in the\n    ALM was similar to that reported here, with both subspaces explaining comparable amounts of variance\n    (movement-null: 36.0 ± 7.40%, mean ± s.d.; movement-potent: 37.1 ± 8.70%; p = 0.15 , paired two-sample\n    t -test; n = 16 sessions; Fig. 4c ).'\n  statistics:\n  - test: paired two-sample t-test\n    p: 0.15\n    n: 16 sessions\n  depends_on:\n  - map-session-selection\n  expected:\n  - quantity: ALM movement-null variance explained\n    value: 36.0\n    tolerance: 7.40\n    unit: percent\n  - quantity: ALM movement-potent variance explained\n    value: 37.1\n    tolerance: 8.70\n    unit: percent\n  criterion: ALM units of the ALM and medulla sessions (M1, M2), subspaces from ALM alone (M3 to M5),\n    variance explained per session (M6). A claim of absence, judged on the paper's test, a two-sided paired\n    t test over sessions of null against potent variance explained. Reproduced when it gives p >= 0.05 and\n    both means are within tolerance under one reading of M1 to M6; not reproduced when p < 0.05 under the\n    reading whose means match. The difference is reported under every reading.\n- id: fig4c-medulla-null-smaller\n  statement: In the medullary reticular nuclei the movement-null subspace explains less variance than the\n    movement-potent subspace (26.4 +- 3.90% against 44.8 +- 7.12%, mean +- s.d.; paired t test p = 1.9e-9,\n    16 sessions).\n  source: Results, A subset of null dynamics is found downstream of motor cortex, paragraph 3; Figure 4c,\n    right\n  quote: 'In contrast, in the medulla, the movement-null subspace explained less variance than the\n    movement-potent subspace (movement-null: 26.4 ± 3.90%, mean ± s.d.; movement-potent: 44.8 ± 7.12%; p =\n    1.9 × 10 - 9 , paired two-sample t -test; n = 16 sessions; Fig. 4c , right).'\n  statistics:\n  - test: paired two-sample t-test\n    p: 1.9e-9\n    n: 16 sessions\n  depends_on:\n  - map-session-selection\n  expected:\n  - quantity: medulla movement-null variance explained\n    value: 26.4\n    tolerance: 3.90\n    unit: percent\n  - quantity: medulla movement-potent variance explained\n    value: 44.8\n    tolerance: 7.12\n    unit: percent\n  criterion: Medulla units of the ALM and medulla sessions (M1, M2), subspaces from the medulla alone (M3\n    to M5), variance explained per session (M6). Reproduced when, under one reading, null is below potent\n    with p < 0.05 in a two-sided paired t test over sessions and both means are within tolerance;\n    partially reproduced when the test holds and a mean is outside tolerance.\n- id: fig4d-alm-predicts-medulla-null\n  statement: Medullary movement-null activity is predicted from ALM movement-null activity (40 +- 8.1%,\n    mean +- s.e.m.) nearly as well as contralateral ALM predicts ALM (54 +- 7.0%).\n  source: Results, A subset of null dynamics is found downstream of motor cortex, paragraph 4; Figure 4d\n  quote: Medullary movement-null activity could be predicted from ALM movement-null dynamics (40 ± 8.1%, mean\n    ± s.e.m; Fig. 4d ) nearly as accurately as from the contralateral ALM (54 ± 7.0%, mean ± s.e.m; Fig. 4d ).\n  depends_on:\n  - map-session-selection\n  expected:\n  - quantity: ALM to medulla movement-null R2\n    value: 40\n    tolerance: 8.1\n    unit: percent\n  - quantity: ALM to contralateral ALM movement-null R2\n    value: 54\n    tolerance: 7.0\n    unit: percent\n  criterion: Decoding as in M8, ALM to medulla on the ALM and medulla sessions, ALM to ALM on the bilateral\n    sessions (each hemisphere's subspaces from its own units). Reproduced when, under one reading of M1 to\n    M8, both means are within tolerance and the ALM to medulla mean is below the ALM to ALM mean. The paper\n    reports no test of \"nearly as accurately\"; none is applied.\n- id: fig4d-decoding-asymmetry\n  statement: Prediction is asymmetric; ALM movement-null activity is predicted less well from the medulla\n    (21 +- 6.7%, mean +- s.e.m.) than the medulla from ALM (paired t test p = 1.2e-4, 16 sessions).\n  source: Results, A subset of null dynamics is found downstream of motor cortex, paragraph 4; Figure 4d\n  quote: ALM movement-null dynamics were less accurately predicted from movement-null dynamics in medullary\n    reticular nuclei (21 ± 6.7%, mean ± s.e.m; p = 1.2 × 10 - 4 , paired t -test comparing ALM-to-medulla\n    and medulla-to-ALM predictions; n = 16 sessions; Fig. 4d ).\n  statistics:\n  - test: paired t-test, ALM-to-medulla against medulla-to-ALM\n    p: 1.2e-4\n    n: 16 sessions\n  depends_on:\n  - map-session-selection\n  expected:\n  - quantity: medulla to ALM movement-null R2\n    value: 21\n    tolerance: 6.7\n    unit: percent\n  criterion: Decoding as in M8 on the ALM and medulla sessions. Reproduced when, under one reading,\n    medulla to ALM is below ALM to medulla with p < 0.05 in a two-sided paired t test over sessions and the\n    medulla to ALM mean is within tolerance; partially reproduced when the test holds and the mean is\n    outside tolerance.\n- id: fig4e-medulla-null-lower-dimension\n  statement: The movement-null subspace has lower dimensionality in the medullary reticular nuclei than in\n    ALM (paired t test, p = 7.4e-5).\n  source: Results, A subset of null dynamics is found downstream of motor cortex, paragraph 5; Figure 4e\n  quote: Consistent with the latter, the dimensionality of the movement-null subspace was lower in medullary\n    reticular nuclei than in ALM ( Fig. 4e ; p = 7.4 × 10 - 5 , paired t -test).\n  statistics:\n  - test: paired t-test\n    p: 7.4e-5\n    n: 16 sessions\n  depends_on:\n  - map-session-selection\n  criterion: Dimensionality per region and session as in M9, readings N1 and N2. Reproduced when, under one\n    reading, the medulla value is below the ALM value with p < 0.05 in a two-sided paired t test over the ALM\n    and medulla sessions. The unit counts per region are reported, since N1 depends on them.\n- id: fig4f-medulla-null-not-spanning-alm\n  statement: In a joint UMAP embedding of movement-null activity, medullary units do not span the set of\n    movement-null activity patterns seen in ALM.\n  source: Results, A subset of null dynamics is found downstream of motor cortex, paragraph 5; Figure 4f\n  quote: Further, examining a UMAP embedding of ALM and medullary movement-null activity, we found that the\n    activity patterns observed in the medullary nuclei did not span the collection of movement-null\n    activity patterns observed in the ALM ( Fig. 4f )\n  depends_on:\n  - map-session-selection\n  criterion: UMAP as in M10 on ALM and medulla units of the ALM and medulla sessions. The paper gives no\n    measure; it judges the embedding by inspection (Figure 4f legend shows ALM patterns with no medulla\n    neighbour). Reproduced when the test-set embedding has a region holding ALM units with no medulla unit\n    near them, and the medulla units fall within the region occupied by ALM units; the embedding is shown\n    and the judgment stated as resting on inspection.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/hasnain-2025.yaml paper/10.1101-2025.10.17.682917.txt; grep -n "—\|rather" claims/hasnain-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -v "^#" claims/hasnain-2025.yaml | grep -nE "^\s+[^-'][^:]*: |^\s*-?\s*[a-z_]+: [^'].*: " | head; git status --short
```

```
5:  statement: The paper's own recordings comprise 27 sessions in 9 mice, with 49 L-ETNs and 1020 UNs in
8:  source: Methods, Analysis of electrophysiological recordings, last paragraph; Results, Similarity in
10:  quote: For ALM, our dataset consisted of 49 L-ETNs and 1020 UNs (415 single units and 605 multi units
14:  - quantity: ALM L-ETNs
15:    value: 49
16:    tolerance: 4.9
17:  - quantity: ALM UNs
18:    value: 1020
19:    tolerance: 102
20:  - quantity: tjM1 L-ETNs
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
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml
d=yaml.safe_load(open('claims/hasnain-2025.yaml'))
for c in d['claims']:
  for k,v in c.items():
    if isinstance(v,str) and ': ' in v: print(c['id'],k)
"; grep -n "^  [a-z]*: '" claims/hasnain-2025.yaml | cut -c1-60
```

```
fig1i-selectivity-proportions quote
fig2c-subspace-variance quote
fig3d-letn-un-movement-encoding quote
fig4b-medulla-selectivity quote
fig4c-alm-null-potent-similar quote
fig4c-medulla-null-smaller quote
157:  quote: 'The proportion of L-ETNs that exhibit trial-ty
191:  quote: 'We found that the movement-null and movement-p
282:  quote: 'Again, L-ETNs could not be distinguished from 
359:  quote: 'Many units exhibited selectivity for either ri
384:  quote: 'In the MAP dataset, the variance explained by 
414:  quote: 'In contrast, in the medulla, the movement-null
```

**Agent**

I wrote `claims/hasnain-2025.yaml`. The quote checker passes it: 19 claims, 19 quotes, 9 statistical values, 0 problems. Nothing is committed.

**Text read.** The bioRxiv preprint, version 1 (PMC12632980), full text: Results, Discussion, Methods, and the legends of Figures 1 to 4 and Extended Data Figures 1 to 3. The paper has no separate supplement. No PDF was supplied, so I read no figures; every claim rests on the text.

**Code read.** github.com/economolab/subspaceID at commit d593949. It holds only the subspace optimization (`orthogonal_subspaces.m` with manopt, an example script and a Python port). The paper's other analysis code is "to be made available upon publication".

**Claims.**
- **Totals:** 19 claims, all with quotes. 9 have statistics and 8 have a criterion only. The other 11 have expected values and a criterion; none relies on expected values alone.
- **Testable on DANDI:000363 (8 claims):** the Figure 4 analyses of the reused MAP dataset. They cover session and unit selection, medulla selectivity, variance explained by each subspace in ALM and in the medulla, ALM-to-medulla and medulla-to-ALM decoding, dimensionality, and the UMAP embedding.
- **Not testable here (11 claims):** Figures 1 to 3 and Extended Data 2 and 3 use the paper's own recordings. The paper says these "will be made publicly available upon publication", so they are not public. These claims stay `data: dataset` and can be blocked as `data_missing`.

**Details the paper leaves open, with the readings named**
- **ALM and medulla session count:** 16 (Results and all Figure 4 statistics) or 11 sessions from 7 mice (Methods). The bilateral ALM unit count also disagrees: 1116 in the Results, 2016 in the Methods.
- **Units used:** only units labelled 'good', or all units in the regions of selected sessions. 'Good' is stated only as a session filter. The ALM hemisphere in ALM and medulla sessions is not stated; all ALM units are pooled.
- **Trial window for MAP:** -2.15 to +1.5 s or -1.8 to +1.5 s around the go cue. Normalization follows the Methods' baseline z-score; the code's whole-trace z-score is a variant.
- **Movement threshold:** set by hand per session. The reading is the trough between the two histogram modes, from the paper's own-data procedure. Above-threshold runs shorter than 100 ms count either as stationary or as moving.
- **Subspace dimensions:** a garbled Methods sentence about sessions with forty or fewer neurons. Readings: no cap beyond the neuron count, or a cap of 20 per subspace. The example script's fixed 15 is a variant.
- **Variance explained (Figure 4c):** the covariance and dimension used are open. Readings: full covariance normalized by its top-d eigenvalues, full covariance normalized by total variance (this makes 37 + 41 = 78 add up), or the stationary and moving covariances.
- **Selectivity (Figure 4b):** the five sub-epochs either combine into sample, delay and response, or are scored separately. The number of trials sampled is open.
- **Decoding (Figure 4d):**
  - Trials used: all trials or correct trials only.
  - How R² combines across target dimensions: pooled, or averaged per dimension.
  - Whether predictors are standardized before the ridge.
  - The ALM-to-ALM value: both directions averaged, or each direction alone.
  - Window: the Results say 40 ms, the Methods 45 ms; the Methods' 45 ms is used.
- **Dimensionality (Figure 4e):** the Methods' shuffle-based count, or the effective dimensionality (participation ratio) of the reference the Results cite.
- **UMAP (Figure 4f):** the paper gives no measure and judges by inspection, so the criterion rests on inspection.

**Missing from the paper.** Nothing a claim needed for the MAP analyses, beyond the open details above. Tolerances use the paper's s.d. for Figure 4c and its s.e.m. for Figure 4d.

## End of run

24 turns, 4 minutes, $1.66 at API prices, result: success.
