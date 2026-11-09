# 001960 · author-revise-1 · run 42187012363

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/001960/verifier-1-report.md; ls entries/001960-qi-2026 entries/001960-qi-2026/*; grep -n "Hand over for verification" -A60 docs/protocol.md | head -120
```

```
Fri Nov  6 08:26:56 UTC 2026
**Verifier report, round 1: Qi et al. 2026, DANDI:001960 v0.261013.2016**

The claims file has 56 claims. The attempt tests 45 and blocks 11, across three notebooks (`qi2026_excitability_connectivity` = EC, `qi2026_spontaneous` = SP, `qi2026_excitability_spontaneous` = ES). My outcomes: 31 reproduced, 7 partially reproduced, 5 not reproduced, 13 blocked.

### A. Outcomes

| claim id | my outcome | reason |
|---|---|---|
| jf608-brighter | blocked (data_missing) | The archive API lists 7 assets (3 sessions × 2 mice plus a raw excerpt). There is no JF585/JF608 comparison. |
| targeting-signal-to-background | blocked (data_missing) | There are no wide-field and targeted images of the same field. The excerpt is a targeted-illumination movie. |
| spike-snr-and-detection-errors | not_reproduced | SNR (1/noise) is 3.18–3.45 under every reading (SP cell 6), below 4.5 ± 0.7. The Methods' definition (s.d. of the 1-frame difference, no √2) matches the notebook's. The false-discovery and false-negative rates were not computed. |
| snr-decay-one-hour | reproduced | Mean of ratios is 72.9% (QC) and 77.3% (all); ratio of means is 69.8% and 73.4%. All are within 76 ± 13 (SP cell 8). |
| fig1d-stimulation-fold-change | blocked (data_missing) | No 76-cell periodic-stimulation session in the asset list. |
| off-target-length-constants | blocked (data_missing) | No lattice experiment. |
| l1-sampling-density | blocked (data_missing) | No z-stack, only a GFP maximum projection. |
| adaptation-vadp-correlation | reproduced | Reading (a): R = 0.232, p = 4.5e-8, n = 543 (EC cell 13). |
| fig2c-three-bins | reproduced | Cluster sizes are exactly {94, 110, 116} (EC cell 15). |
| fig2gk-bin-profiles | reproduced | 8 of 8 orderings hold under both readings (EC cell 17). |
| two-mice-intrinsic-distributions | blocked (methods_underspecified) | The named readings disagree: all cells give 4/5 (time constant p = 0.101), QC cells give 5/5 (time-constant p = 0.048). The 
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; ls attempts/ | grep 001960; ls questions/ | grep 1960; ls transcripts/001960; cat entries/001960-qi-2026/entry.yaml; wc -l entries/001960-qi-2026/l1opto.py; ls executed/ 2>/dev/null | head; ls claims | grep 1960
```

```
615 docs/protocol.md
001960-qi-2026-01.yaml
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
verifier-1.md
schema_version: 1
name: 001960-qi-2026
type: reproduction
title: All-optical electrophysiology of layer 1 interneurons (Qi et al. 2026)
description: Tests the findings of Qi, Parot, Wang, Pomeroy, Lavis and Cohen (2026) on dandiset 001960,
  which holds, for two NDNF-Cre::NPY-GFP mice, a spontaneous session, an intrinsic-excitability
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,200p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-13`. Record this version in the attempt's provenance.

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
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,442p docs/protocol.md; sed -n 523,615p docs/protocol.md
```

```
### 1. Establish what can be tested

Do this before any analysis.

1. List the dataset's files and read its metadata from the archive. Open a
   file and list everything it holds, including every column of every table.
2. Work out which of the subjects, sessions, conditions and measured
   variables that the claims file describes are in the dataset. A dataset
   that names a paper may hold only part of its data. Check for recordings
   deposited more than once (identical traces, frame counts or annotations),
   report each pair, and count each recording once. Where the analysis treats
   a unit as the same across sessions, show that it is, or state it as an
   assumption and also give results per session.
3. Choose the version to pin. Pin the version the paper cites, as the claims
   file gives it. If it cites none, pin the most recent published version,
   unless an earlier one matches the claims file's description better. Say
   why in the notebook's header. If versions differ in content the analysis
   uses, show the difference.
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
[... 315 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l attempts/001960-qi-2026-01.yaml questions/001960.yaml; sed -n 1,80p attempts/001960-qi-2026-01.yaml; grep -n "^[a-z_]*:" attempts/001960-qi-2026-01.yaml; cat transcripts/001960/author-answers-report.md
```

```
685 attempts/001960-qi-2026-01.yaml
wc: questions/001960.yaml: No such file or directory
  685 total
schema_version: 2
id: 001960-qi-2026-01
dataset:
  archive: dandi
  id: "001960"
  version: 0.261013.2016
  doi: 10.48324/dandi.001960/0.261013.2016
paper: doi:10.64898/2026.10.05.756595
date: 2026-11-06
entry: 001960-qi-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 80,685p attempts/001960-qi-2026-01.yaml
```

```
<persisted-output>
Output too large (30.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/9cf27494-45b6-4ef6-85fb-c849afae2ab4/tool-results/bgesx4tal.txt

Preview (first 2KB):
  outcome: blocked
  blocked_by: data_missing
  notes: The spinning-disk z-stack is not deposited. The raw-movie excerpt holds only a 47-plane GFP
    maximum projection and a 21-plane RFP projection of the field, which cannot give the cell count
    in the cylinder.
- claim: adaptation-vadp-correlation
  outcome: reproduced
  notebook: qi2026_excitability_connectivity.ipynb
  output: claim:adaptation-vadp-correlation
  measured: 0.232
  notes: Over the 543 QC cells of the two sparseOpto sessions R = 0.232, p = 4.5e-8 (reading (a));
    all 640 cells give R = 0.186. No selection gives the paper's n = 564.
- claim: fig2c-three-bins
  outcome: reproduced
  notebook: qi2026_excitability_connectivity.ipynb
  output: claim:fig2c-three-bins
[... 25 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001960-qi-2026-01.yaml",
 "offset": 100,
 "limit": 590
}
```

```
100	  notes: Ward clustering of the column-wise z-scored five properties of the 320 cells of
101	    M-YQ0201-29 gives clusters of 110, 94 and 116 cells, the paper's counts as a set.
102	- claim: fig2gk-bin-profiles
103	  outcome: reproduced
104	  notebook: qi2026_excitability_connectivity.ipynb
105	  output: claim:fig2gk-bin-profiles
106	  notes: All eight orderings hold with maximum rate (bin medians 39.0, 19.7, 30.9 Hz) and with the
107	    Figure 2F trial-average rate (23.1, 9.5, 16.3 Hz). Rheobase 0.386, 0.326, 0.102 SH; adaptation
108	    0.278, -0.167, 0.484; membrane time constant 15.3, 18.9, 14.9 ms. Two membrane time constants are
109	    removed as outliers by the code's 6 s.d. rule.
110	  deviations:
111	  - The Figure 2F rate is the mean over the trial of the code's trial-average firing rate in each
112	    cell's blue-stimulated trials.
113	- claim: two-mice-intrinsic-distributions
114	  outcome: reproduced
115	  notebook: qi2026_excitability_connectivity.ipynb
116	  output: claim:two-mice-intrinsic-distributions
117	  notes: With the QC cells (reading (b), 286 and 257) all five calls match, rheobase p = 1.0e-4,
118	    membrane time constant p = 0.048, V_adp 0.84, maximum rate 0.93, adaptation 0.48. With all 320
119	    cells per mouse (reading (a), the legend's n) four match; the membrane time constant gives
[... 567 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/001960/; wc -l claims/001960/*; ls paper/; sed -n 1,140p claims/001960/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001960; grep -n "^- id:" *.yaml
```

```
90:- id: jf608-brighter
117:- id: targeting-signal-to-background
139:- id: spike-snr-and-detection-errors
165:- id: snr-decay-one-hour
180:- id: fig1d-stimulation-fold-change
197:- id: off-target-length-constants
218:- id: l1-sampling-density
237:- id: adaptation-vadp-correlation
258:- id: fig2c-three-bins
278:- id: fig2gk-bin-profiles
296:- id: two-mice-intrinsic-distributions
320:- id: synaptic-connection-counts
359:- id: ipsp-median-amplitude
382:- id: detection-limits
406:- id: gap-junction-connection-counts
444:- id: hadamard-stimulation-rates
473:- id: spikelet-not-scatter
490:- id: highmag-footprint
510:- id: lasso-off-target-correction
538:- id: connection-distance-structure
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims/001960; f=10.64898-2026.10.05.756595.yaml; sed -n 139,165p $f; sed -n 296,406p $f; sed -n 444,538p $f; sed -n 603,612p $f
```

```
- id: spike-snr-and-detection-errors
  statement: Single-spike SNR (spike height over baseline shot noise) was 4.5 +/- 0.7; the
    estimated false-discovery proportion of spike detection was 17 +/- 13% and the
    false-negative rate 28 +/- 19%.
  source: Results, Molecular and optical tools, paragraph 5; Supplementary Figure 7
  quote: The single-spike SNR (spike-height:baseline shot noise) was 4.5 ± 0.7 (mean ± s.d.).
    Using a fitted mixture model, we estimated the spike-detection false-discovery proportion
    to be 17 ± 13% across all neurons, and false-negative rate to be 28 ± 19%
  expected:
  - quantity: spike SNR
    value: 4.5
    tolerance: 0.7
  - quantity: false-discovery proportion
    value: 17
    tolerance: 13
    unit: percent
  - quantity: false-negative rate
    value: 28
    tolerance: 19
    unit: percent
[... 223 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims/001960; f=10.64898-2026.10.05.756595.yaml; sed -n 716,741p $f; sed -n 817,893p $f; sed -n 1007,1155p $f; sed -n 1198,1238p $f; sed -n 1302,1333p $f; sed -n 1434,1453p $f
```

```
- id: fig3lo-variance-components
  statement: A linear mixed-effects model attributes more variance of IPSP amplitude to
    presynaptic than to postsynaptic identity, and more variance of IPSP decay time constant
    to postsynaptic than to presynaptic identity, each ordering holding in all but under 0.1%
    of bootstrap simulations.
  source: Figure 3L, 3O legends; Methods, Linear mixed effects model
  quote: "More variance of IPSP amplitude is explained by presynaptic identity than by
    postsynaptic identity ... ***: < 0.001 of the simulations produced higher postsynaptic
    variance ... More variance of IPSP decay time constant is explained by postsynaptic
    identity than by presynaptic identity"
  statistics:
  - about: amplitude, presynaptic against postsynaptic variance
    test: parametric bootstrap of the mixed model, 2000 simulations
    p: 0.001
    p_relation: "<"
  - about: decay time constant, postsynaptic against presynaptic variance
    test: parametric bootstrap of the mixed model, 2000 simulations
    p: 0.001
    p_relation: "<"
  criterion: As in code, tutorials/tutorial5_pre_post_variance. Connected QC pairs of both
[... 325 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; for nb in *.ipynb; do echo "== $nb"; python -c "
import json,sys
nb=json.load(open('$nb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(i,c['cell_type'],c.get('metadata',{}).get('tags',[]),len(src),repr(src[:90]))
"; done
```

```
== qi2026_excitability_connectivity.ipynb
0 markdown [] 3653 '# Reproducing Qi et al. (2026) from dandiset 001960\n\nPaper. Qi, Parot, Wang, Pomeroy, Lavi'
1 code [] 359 'import os\nos.environ.setdefault("OMP_NUM_THREADS", "4")\nimport time\nimport numpy as np\nimp'
2 markdown [] 450 '## Data check\n\nEvery session file holds a units table of 320 cells (all detected cells, wi'
3 code ['sanity'] 1127 'rows = []\nU = {}\nfor m in L.MICE:\n    for s in L.SESSIONS:\n        u = L.units(m, s)\n     '
4 code ['sanity'] 334 '# Sampling interval, from the stored timestamps of every session\nfor m in L.MICE:\n    for '
5 code ['sanity'] 403 '# Intrinsic properties (sparseOpto units table): ranges and units\nfor m in L.MICE:\n    P ='
6 code ['sanity'] 1176 '# Pairwise metrics: table order, distances, and value ranges\nPM = {}\nfor m in L.MICE:\n    '
7 code ['sanity'] 1795 '# Orientation of the per-pair series: row k of the table holds the presynaptic spike times'
8 code ['sanity'] 1089 '# Do unit ids refer to the same cells across the three sessions of a mouse?\nfrom scipy.spa'
9 code ['sanity'] 790 '# Duplicate recordings: compare spike counts and the first 2000 frames of voltage between '
10 code ['sanity'] 1180 '# Shared clock of stimulus and response (sparseOpto, M-YQ0201-29): spike rate of the stimu'
11 markdown [] 815 '## Figure 1 claims that need recordings not in the dandiset\n\nThe dandiset holds, per mouse'
12 markdown [] 383 '## Figure 2: intrinsic excitability\n\n### adaptation-vadp-correlation\n> Spike-rate adaptati'
13 code ['claim:adaptation-vadp-correlation'] 811 'PROPS = {m: L.intrinsic_properties(m) for m in L.MICE}\nQC_OPTO = {m: U[m, "sparseOpto"]["p'
14 markdown [] 237 '**Result: reproduced.** With the 543 QC cells (reading (a)) R = 0.232 (p = 4.5e-8), within'
15 markdown [] 402 '### fig2c-three-bins\n> Ward hierarchical clustering of the five z-scored intrinsic propert'
16 code ['claim:fig2c-three-bins'] 507 'from scipy.cluster.hierarchy import linkage
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed/001960-qi-2026/ 2>/dev/null; sed -n 1,140p entries/001960-qi-2026/l1opto.py; grep -n "^def \|^class " entries/001960-qi-2026/l1opto.py
```

```
"""Loading and measures for dandiset 001960 (Qi, Parot, Wang, Pomeroy, Lavis and Cohen 2026).

Wide-area all-optical electrophysiology of about 320 layer 1 interneurons in each of two
NDNF-Cre::NPY-GFP mice (M-YQ0201-27 and M-YQ0201-29), with three sessions per mouse:
``behavior`` (spontaneous activity), ``sparseOpto`` (intrinsic excitability mapping) and
``sparsePulseHad`` (connectivity mapping), plus a raw-movie excerpt of one behavior session.

Files are streamed from the DANDI Archive with remfile and h5py; nothing is downloaded to disk.
The large voltage arrays are stored time x cell in blocks of 10,000 frames, so they are read in
time blocks over all cells, and reduced as they are read.

Where a parameter comes from is said at each function: "claims" for the claim's criterion
(which cites the paper or its code), "paper" with the passage for a detail taken from the paper
(protocol, author step 1.6), "code" for the paper's code, https://github.com/adamcohenlab/
Qi2026WideAreaL1 at commit 181ad475520224c44d27903e7522d3e2aa76857d, "assumption" for a choice
the paper leaves open, and "standard" for a detail that cannot change a result.
"""
from __future__ import annotations

import functools
[... 153 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import h5py, remfile, numpy, scipy, sklearn, pandas; print('ok')"; which python; ls -a; grep -n "def \|venv\|uv " tools/entry.py | head -60
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import h5py, remfile, numpy, scipy, sklearn, pandas; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'h5py'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
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
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n PYTHON_VERSION tools/entry.py | head -3; uv venv --quiet --python 3.12 $TMPDIR/venv 2>&1 | tail -2; uv pip install --quiet --python $TMPDIR/venv/bin/python -r entries/001960-qi-2026/requirements.lock.txt 2>&1 | tail -3; $TMPDIR/venv/bin/python -c "import h5py, remfile, umap; print('ok')"
```

```
59:PYTHON_VERSION = "3.13"
335:    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--python-version", PYTHON_VERSION,
350:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
ok
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; time $TMPDIR/venv/bin/python -c "
import l1opto as L, h5py
print(L.assets())
f=L.open_file('M-YQ0201-27','sparsePulseHad')
def show(name,obj):
    if isinstance(obj,h5py.Dataset):
        print(name,obj.shape,obj.dtype,obj.chunks)
f.visititems(show)
" 2>&1 | grep -v "^units/.*_index" | head -120
```

```
{'sub-M-YQ0201-27/sub-M-YQ0201-27_ses-sparseOpto_behavior+ophys.nwb': '95b0523b-3981-464d-8cc5-8d0789a12073', 'sub-M-YQ0201-27/sub-M-YQ0201-27_ses-behavior_behavior+ophys.nwb': 'f5d362e5-0f27-42af-8166-37835d4d62f6', 'sub-M-YQ0201-29/sub-M-YQ0201-29_ses-sparseOpto_behavior+ophys.nwb': '7a91354a-0ae7-4f97-b9b3-26000820a583', 'sub-M-YQ0201-29/sub-M-YQ0201-29_ses-behavior_behavior+ophys.nwb': '175ad19c-e469-452d-a8dc-3c57c9f0c88f', 'sub-M-YQ0201-29/sub-M-YQ0201-29_ses-sparsePulseHad_behavior+ophys.nwb': 'd27cf030-acbe-476b-9026-6a8ef4cb0243', 'sub-M-YQ0201-27/sub-M-YQ0201-27_ses-sparsePulseHad_behavior+ophys.nwb': '9ef53fc8-42a0-496b-ad43-15bebd9870b4', 'sub-M-YQ0201-29/sub-M-YQ0201-29_ses-behavior-rawexcerpt_behavior+ophys.nwb': '20f36138-2e20-4823-b80d-418bad0c65c4'}
acquisition/face_video/data (160640, 352, 352) uint8 (128, 352, 352)
acquisition/face_video/format () object None
acquisition/face_video/timestamps (160640,) float64 (1000,)
analysis/matlab_variable_lookup/id (32,) int64 None
analysis/matlab_variable_lookup/mapping_notes (32,) object None
analysis/matlab_variable_lookup/matlab_variable (32,) object None
analysis/matlab_variable_lookup/nwb_path (32,) object None
analysis/pairwise_connectivity_metrics/distance_pixels (102400,) float64 None
analysis/pairwise_connectivity_metrics/gap_junction_connection (102400,) uint8 None
analysis/pairwise_connectivity_metrics/hadamard_orthogonal_spike_times (39011337,) float64 None
analysis/pairwise_connectivity_metrics/hadamard_orthogonal_spike_times_index (102400,) uint64 None
analysis/pairwise_connectivity_metrics/id (102400,) int64 None
analysis/pairwise_connectivity_metrics/ipsp_amplitude_norm_per_presynaptic_spike (102400,) float64 None
analysis/pairwise_connectivity_metrics/ipsp_decay_source_units (102400,) float64 None
analysis/pairwise_connectivity_metrics/ipsp_decay_standard_error_source_units (102400,) float64 None
analysis/pairwise_connectivity_metrics/postsynaptic_unit_id (102400,) float64 None
analysis/pairw
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -c *.txt; grep -n -i "lasso\|wave propagation\|detection probability\|interstitial\|scattered fluor\|P(spk\|Analysis for mapping\|Gap junction mapping\|Detecting spikes" *.txt | head -60
```

```
151772 10.64898-2026.10.05.756595.txt
107:Mapping synaptic and gap junctional connectivity by all-optical electrophysiology in vivo (A) Synaptic connectivity mapping. Top: targeted stimulation evoked spikes in presynaptic cell i . Bottom: trial-averaged response (n = 283 trials) in postsynaptic cell j . (B) Synaptic connectivity matrix for one mouse. The contrast of each matrix element is modulated by its p-value: 0.001 corresponds to maximum contrast, 0.5 corresponds to zero contrast. Inhibitory post-synaptic potential (IPSP) amplitude is measured in units of spike height per presynaptic spike. (C) Gap junction mapping. Cells were stimulated with 750 ms pulses in a pseudo-random sequence to evoke rapid spiking (blue). Spike-triggered average waveforms in a pre-junctional cell, i , and post-junctional cell, j (n = 7215 spikes of cell i). (D) Gap junctional connectivity matrix for one mouse. The contrast of each matrix element is modulated by its p-value: 0.001 corresponds to maximum contrast, 0.5 corresponds to zero contrast. Spikelet amplitude is measured in units of spike height. (E) Distance-dependent decay in IPSP amplitude. Box plots show median amplitude in 60-μm wide bins of cell-cell distance (box top and bottom: 25 th and 75 th percentile, whisker length: 1.5x inter-quartile range). Green: mouse 1, orange: mouse 2. (F) Distance-dependent population average IPSP waveform. Cell pairs were divided into 10 distance bins (bin size = 30 μm), and the average IPSP waveform was computed for each bin. Blue light scatter evoked a small stimulus artifact for closely spaced cell pairs (blue shading). (G) Distance-dependent decay in spikelet amplitude. Box plots show median amplitude in 60-μm wide bins of cell-cell distance, for two mice (box features same as in E). (H) Top: distance-dependent population average spikelet waveform. Cell pairs were divided into 10 distance bins (bin size = 30 μm), and the average spikelet waveform was computed for each bin. Bottom: spikele
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; f=*.txt; sed -n 449,495p $f; sed -n 537,541p $f; sed -n 1320,1360p $f; sed -n 1435,1450p $f; sed -n 1575,1592p $f
```

```
## Detecting spikes, estimating false positive/negative rates, and calculating SNR

Spike detection was adapted from Volpy 91 . In brief, we first generated a template spike waveform for each cell by averaging its 500 largest spikes. This template was then used as a matched filter and applied to the fluorescence traces. Spikes were then detected by thresholding the filtered trace. We estimated the noise distribution using the negative portion of the filtered trace, and chose a threshold that set the false-positive rate to ∼500 spikes per hour. To estimate the false positive and negative rates, we modeled the supra-threshold peaks as a mixture of two truncated (by the detection threshold) Gaussian distributions for supra-threshold noise (false positive) and detected spikes (real positive) respectively. We estimated the parameters of these truncated Gaussians via maximum likelihood estimation. We defined spike height as the mean of the spike Gaussian distribution, and the fluorescence trace was normalized by this spike height. We defined SNR as the ratio between the spike amplitude and shot noise. We estimated the shot noise as standard deviation of the 1-frame difference of the fluorescence trace. Standard deviation was approximated as 1.4826 times the median absolute deviation to avoid contamination from spikes.

## Face movie analysis

Whisking motion was extracted from the facial videography by first averaging pixels in a manually defined region around the whisker pad. We then defined motion as the absolute 1-frame difference of the pixel-average trace. The trace was then smoothed by an 8-frame moving median filter.

We observed that the log-transformed whisking motion has a bimodal gaussian distribution, corresponding to quiet and whisking epochs. We fitted a gaussian mixture model to the log-transformed whisking motion, and set the whisking threshold at the cross-over point of the two gaussian distributions. We defined whisking epochs to be whenever the whisking
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python -c "
import json
nb=json.load(open('qi2026_excitability_connectivity.ipynb'))
for i in [21,22,23,46,47,48,55,56,57]:
    print('-----',i); print(''.join(nb['cells'][i]['source']))
"; sed -n 418,520p l1opto.py
```

```
----- 21
### two-mice-intrinsic-distributions
> The two mice show similar broad distributions of intrinsic properties; by two-sided rank-sum tests
> they differ in optical rheobase (p <= 0.001) and membrane time constant (0.01 < p <= 0.05), not in
> V_adp, maximum rate or adaptation.
----- 22
for nm, sel27, sel29 in [("(a) all cells", np.ones(320, bool), np.ones(320, bool)),
                         ("(b) QC cells", QC_OPTO["M-YQ0201-27"], QC_OPTO["M-YQ0201-29"])]:
    print(f"reading {nm}: n = {sel27.sum()} and {sel29.sum()}")
    calls = {}
    for j, p in enumerate(L.PROPERTIES):
        a, b = PROPS["M-YQ0201-27"][sel27, j], PROPS["M-YQ0201-29"][sel29, j]
        a, b = a[np.isfinite(a)], b[np.isfinite(b)]
        pv = stats.ranksums(a, b).pvalue
        calls[p] = pv <= 0.05
        print(f"   {p:28s} median {np.median(a):8.4f} vs {np.median(b):8.4f}  p = {pv:.3g}")
    want = {"optical_rheobase_norm": True, "membrane_time_constant_ms": True, "adp_blue_norm": False,
            "max_firing_rate_hz": False, "pulse_adaptation": False}
    print("   calls matching the paper:", sum(calls[k] == v for k, v in want.items()), "of 5")
----- 23
[... 203 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python -c "
import json
nb=json.load(open('qi2026_excitability_connectivity.ipynb'))
for i in [1,3,5,6,24,25,62,63,72,74,75,76]:
    print('-----',i); print(''.join(nb['cells'][i]['source']))
"; sed -n 640,672p l1opto.py
```

```
----- 1
import os
os.environ.setdefault("OMP_NUM_THREADS", "4")
import time
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import l1opto as L

T0 = time.time()
pd.set_option("display.width", 160)
print("dandiset", L.DANDISET, "version", L.VERSION)
assets = L.assets()
for p, a in sorted(assets.items()):
    print(p, a)
----- 3
rows = []
U = {}
for m in L.MICE:
[... 362 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/dev; cat > $TMPDIR/dev/ec1.py <<'EOF'
import sys; sys.path.insert(0, "entries/001960-qi-2026")
import numpy as np, pandas as pd
from scipy import stats
import l1opto as L
U = {(m, s): L.units(m, s) for m in L.MICE for s in ("sparseOpto", "sparsePulseHad")}
PROPS = {m: L.intrinsic_properties(m) for m in L.MICE}
QC = {m: U[m, "sparseOpto"]["passed_qc"] for m in L.MICE}
# P5
want = {"optical_rheobase_norm": True, "membrane_time_constant_ms": True, "adp_blue_norm": False,
        "max_firing_rate_hz": False, "pulse_adaptation": False}
for nm, s27, s29 in [("(a) all", np.ones(320, bool), np.ones(320, bool)), ("(b) QC", QC[L.MICE[0]], QC[L.MICE[1]])]:
    for zero_missing in (False, True):
        calls = {}
        out = []
        for j, p in enumerate(L.PROPERTIES):
            a, b = PROPS[L.MICE[0]][s27, j], PROPS[L.MICE[1]][s29, j]
            a, b = a[np.isfinite(a)], b[np.isfinite(b)]
            if zero_missing and p == "membrane_time_constant_ms":
                print("  zeros", (a == 0).sum(), (b == 0).sum())
                a, b = a[a > 0], b[b > 0]
            pv = stats.ranksums(a, b).pvalue
            calls[p] = pv <= 0.05
            out.append(f"{p[:12]} {pv:.3g} n={len(a)},{len(b)}")
        print(nm, "zero->missing" if zero_missing else "", sum(calls[k] == v for k, v in want.items()), out)
# zeros: QC status
for m in L.MICE:
    t = PROPS[m][:, 4]
    print(m, "tau==0 cells", np.nonzero(t == 0)[0], "qc", QC[m][t == 0])
# P4
for selnm in ("all flags", "QC 60-400", "QC within 400"):
    for kind, col, flag in [("IPSP", "ipsp_amplitude_norm_per_presynaptic_spike", "synaptic_connection"),
                            ("spikelet", "spikelet_amplitude_normalized", "gap_junction_connection")]:
        vs = []
        for m in L.MICE:
            M, q, QQ, D, sets = L.pair_sets(m)
            T = {"all flags": np.ones_like(QQ), "QC 60-400": sets["60 to 400 um"], "QC within 400": sets["within 400 um"]}[selnm]
            w = M[col][M[flag] & T]
            vs.append(w[np.isfinite(w)])
        v = np.concatenate(vs); pos = v[v > 0]
        print(selnm, kind, len(v), len(v) - len(pos), f"raw {stats.skew(v):.2f} log {stats.skew(np.log(pos)):.2f}",
              [f"{stats.skew(np.log(w[w>0])):.2f}" for w in vs])
# P13
for selnm in ("QC 60-400", "QC within 400", "all flags"):
    rows = []
    for m in L.MICE:
        M, q, QQ, D, sets = L.pair_sets(m)
        g = U[m, "sparsePulseHad"]["gfp_positive"]
        T = {"all flags": np.ones_like(QQ), "QC 60-400": sets["60 to 400 um"], "QC within 400": sets["within 400 um"]}[selnm]
        ii, jj = np.nonzero(M["synaptic_connection"] & T)
        rows.append(pd.DataFrame(dict(post=g[jj], tau=1e3 * M["ipsp_decay_source_units"][ii, jj])))
    d = pd.concat(rows); d = d[np.isfinite(d.tau) & (d.tau > 0)]
    for cap in (False, True):
        e = d[d.tau < 399] if cap else d
        a, b = e.tau[e.post], e.tau[~e.post]
        print(selnm, "excl cap" if cap else "", f"NPY+ {a.mean():.1f}+/-{a.std():.1f} n={len(a)}  NPY- {b.mean():.1f}+/-{b.std():.1f} n={len(b)} p={stats.ranksums(a,b).pvalue:.2g}", "capped", (d.tau >= 399).sum())
EOF
cd $TMPDIR/dev && time $TMPDIR/venv/bin/python ec1.py
```

```
(a) all  4 ['adp_blue_nor 0.179 n=320,320', 'optical_rheo 1.13e-05 n=320,320', 'max_firing_r 0.197 n=320,320', 'pulse_adapta 0.24 n=320,320', 'membrane_tim 0.101 n=320,320']
  zeros 7 0
(a) all zero->missing 5 ['adp_blue_nor 0.179 n=320,320', 'optical_rheo 1.13e-05 n=320,320', 'max_firing_r 0.197 n=320,320', 'pulse_adapta 0.24 n=320,320', 'membrane_tim 0.0313 n=313,320']
(b) QC  5 ['adp_blue_nor 0.835 n=286,257', 'optical_rheo 0.000103 n=286,257', 'max_firing_r 0.932 n=286,257', 'pulse_adapta 0.477 n=286,257', 'membrane_tim 0.0482 n=286,257']
  zeros 2 0
(b) QC zero->missing 5 ['adp_blue_nor 0.835 n=286,257', 'optical_rheo 0.000103 n=286,257', 'max_firing_r 0.932 n=286,257', 'pulse_adapta 0.477 n=286,257', 'membrane_tim 0.0333 n=284,257']
M-YQ0201-27 tau==0 cells [ 44  54  55 107 151 276 288] qc [ True  True False False False False False]
M-YQ0201-29 tau==0 cells [] qc []
all flags IPSP 1753 0 raw 2.21 log 0.10 ['-0.03', '0.29']
all flags spikelet 7443 0 raw 4.64 log 0.73 ['0.73', '0.86']
QC 60-400 IPSP 1467 0 raw 2.46 log 0.13 ['0.00', '0.34']
QC 60-400 spikelet 5752 0 raw 3.15 log 0.41 ['0.43', '0.49']
QC within 400 IPSP 1505 0 raw 2.41 log 0.12 ['-0.00', '0.31']
QC within 400 spikelet 6006 0 raw 4.68 log 0.70 ['0.71', '0.81']
QC 60-400  NPY+ 77.4+/-101.2 n=760  NPY- 65.2+/-102.3 n=709 p=3.1e-13 capped 91
QC 60-400 excl cap NPY+ 57.1+/-62.6 n=715  NPY- 41.9+/-53.4 n=663 p=1.8e-16 capped 91
QC within 400  NPY+ 80.5+/-105.1 n=784  NPY- 67.2+/-105.1 n=723 p=8.5e-14 capped 104
QC within 400 excl cap NPY+ 57.4+/-62.5 n=731  NPY- 41.9+/-53.1 n=672 p=3.6e-17 capped 104
all flags  NPY+ 82.2+/-108.3 n=873  NPY- 69.0+/-107.0 n=882 p=2.1e-14 capped 128
all flags excl cap NPY+ 57.0+/-63.5 n=809  NPY- 43.1+/-55.5 n=818 p=1.6e-17 capped 128
[... 5 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/001960-qi-2026/l1opto.py",
 "old_string": "    simulate from the fitted model, refit by REML, n_boot times). Returns rows of\n    (s2_pre, s2_post, s2_resid, converged).\"\"\"\n    rng = np.random.default_rng(seed)\n    out = []\n    for _ in range(n_boot):\n        f = model.fit(model.simulate(fit, rng), reml=True, start=fit[\"lg\"])\n        out.append((f[\"s2_pre\"], f[\"s2_post\"], f[\"s2_resid\"], f[\"converged\"]))\n    return np.array(out, dtype=float)",
 "new_string": "    simulate from the fitted model, refit by REML, n_boot times). Returns rows of\n    (s2_pre, s2_post, s2_resid, converged, s2_pre2, s2_post2, converged2), where the last three\n    come from a second refit of the same simulated data started from the grid search, made\n    only when the first did not report convergence (NaN otherwise).\"\"\"\n    rng = np.random.default_rng(seed)\n    out = []\n    for _ in range(n_boot):\n        ys = model.simulate(fit, rng)\n        f = model.fit(ys, reml=True, start=fit[\"lg\"])\n        row = [f[\"s2_pre\"], f[\"s2_post\"], f[\"s2_resid\"], f[\"converged\"], np.nan, np.nan, np.nan]\n        if not f[\"converged\"]:\n            g = model.fit(ys, reml=True)\n            row[4:] = [g[\"s2_pre\"], g[\"s2_post\"], g[\"converged\"]]\n        out.append(row)\n    return np.array(out, dtype=float)"
}
```

```
The file entries/001960-qi-2026/l1opto.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python - <<'EOF'
import json
nb=json.load(open('qi2026_excitability_connectivity.ipynb'))
src=''.join(nb['cells'][56]['source'])
open('/tmp/claude/x','w') if False else None
import os
open(os.environ.get('TMPDIR','/tmp')+'/dev/cell56.py','w').write(src)
EOF
cat > $TMPDIR/dev/ec2.py <<'EOF'
import sys, time; sys.path.insert(0, "entries/001960-qi-2026")
import numpy as np, pandas as pd
import l1opto as L
pair_sets = L.pair_sets
exec(open(sys.argv[1]).read())
EOF
cd $TMPDIR/dev; time $TMPDIR/venv/bin/python ec2.py cell56.py
```

```
amplitude: 1467 pairs ({'M-YQ0201-27': 800, 'M-YQ0201-29': 667}), 417 presynaptic and 446 postsynaptic cells; AIC {'linear distance': np.float64(2140.6), 'log distance': np.float64(2134.3)} -> log distance
   REML variances: pre 0.1445, post 0.0579, residual 0.1374
   bootstrap (1963 of 2000 refits converged, 262 s): pre > post in 100.00%, post > pre in 0.00%; 95% interval of pre - post [0.0545, 0.1216]
decay weights: unweighted residual variance 0.718, median measurement variance 0.057, s0^2 = 0.661, effective n 1364 of 1469
decay: 1469 pairs ({'M-YQ0201-27': 802, 'M-YQ0201-29': 667}), 419 presynaptic and 447 postsynaptic cells; AIC {'linear distance': np.float64(4077.1), 'log distance': np.float64(4067.9)} -> log distance
   REML variances: pre 0.0213, post 0.1111, residual 0.5929
   bootstrap (1949 of 2000 refits converged, 453 s): pre > post in 0.00%, post > pre in 100.00%; 95% interval of pre - post [-0.1410, -0.0407]

real	12m8.170s
user	47m40.769s
sys	0m0.733s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python - <<'EOF'
import json
p='qi2026_excitability_connectivity.ipynb'
nb=json.load(open(p))
c=nb['cells'][56]
src=''.join(c['source'])
old='''    frac_pre = np.mean(boot[ok, 0] > boot[ok, 1])
    print(f"   bootstrap ({ok.sum()} of {len(boot)} refits converged, {time.time() - tb:.0f} s): pre > post in {100*frac_pre:.2f}%, "
          f"post > pre in {100*(1-frac_pre):.2f}%; 95% interval of pre - post "
          f"[{np.percentile(boot[ok,0]-boot[ok,1], 2.5):.4f}, {np.percentile(boot[ok,0]-boot[ok,1], 97.5):.4f}]")'''
new='''    frac_pre = np.mean(boot[ok, 0] > boot[ok, 1])
    print(f"   bootstrap ({ok.sum()} of {len(boot)} refits converged, {time.time() - tb:.0f} s): pre > post in {100*frac_pre:.2f}%, "
          f"post > pre in {100*(1-frac_pre):.2f}%; 95% interval of pre - post "
          f"[{np.percentile(boot[ok,0]-boot[ok,1], 2.5):.4f}, {np.percentile(boot[ok,0]-boot[ok,1], 97.5):.4f}]")
    # every refit, the non-converged ones included: as fitted, and refitted from the grid start
    bad = ~ok
    pre2 = np.where(bad, boot[:, 4], boot[:, 0]); post2 = np.where(bad, boot[:, 5], boot[:, 1])
    adverse = (lambda a, b: a <= b) if kind == "amplitude" else (lambda a, b: a >= b)
    print(f"   all {len(boot)} refits as fitted: adverse ordering in {adverse(boot[:, 0], boot[:, 1]).sum()} "
          f"({100*adverse(boot[:, 0], boot[:, 1]).mean():.2f}%), of which {adverse(boot[bad, 0], boot[bad, 1]).sum()} among the "
          f"{bad.sum()} non-converged; non-converged pre - post ranges {np.min(boot[bad,0]-boot[bad,1]):.4f} to {np.max(boot[bad,0]-boot[bad,1]):.4f}")
    print(f"   non-converged refitted from the grid start ({int(np.nansum(boot[bad, 6]))} of {bad.sum()} converge): adverse ordering in "
          f"{adverse(pre2, post2).sum()} of {len(boot)} ({100*adverse(pre2, post2).mean():.2f}%)")'''
assert old in src
src=src.replace(old,new)
c['source']=src.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat; tail -c 300 qi2026_excitability_connectivity.ipynb | od -c | tail -3; git show HEAD:entries/001960-qi-2026/qi2026_excitability_connectivity.ipynb | tail -c 50 | od -c | tail -3
```

```
entries/001960-qi-2026/l1opto.py                            | 13 ++++++++++---
 .../001960-qi-2026/qi2026_excitability_connectivity.ipynb   | 11 ++++++++++-
 2 files changed, 20 insertions(+), 4 deletions(-)
0000420   :       4   ,  \n       "   n   b   f   o   r   m   a   t   _
0000440   m   i   n   o   r   "   :       5  \n   }  \n
0000454
0000040   o   r   m   a   t   _   m   i   n   o   r   "   :       5  \n
0000060   }  \n
0000062
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/nbed.py <<'EOF'
import json, sys
def load(p): return json.load(open(p))
def save(nb, p):
    json.dump(nb, open(p, 'w'), indent=1, ensure_ascii=False); open(p, 'a').write('\n')
def find(nb, start):
    idx = [i for i, c in enumerate(nb['cells']) if ''.join(c['source']).startswith(start)]
    assert len(idx) == 1, (start, idx); return idx[0]
def cell(kind, src, tags=None):
    c = {"cell_type": kind, "metadata": ({"tags": tags} if tags else {}), "source": src.splitlines(keepends=True)}
    if kind == "code": c.update(execution_count=None, outputs=[])
    return c
def set_src(nb, i, src): nb['cells'][i]['source'] = src.splitlines(keepends=True)
def get(nb, i): return ''.join(nb['cells'][i]['source'])
def replace(nb, i, old, new):
    s = get(nb, i); assert old in s, old[:80]; set_src(nb, i, s.replace(old, new))
EOF
cd entries/001960-qi-2026; python -c "
import json
nb=json.load(open('qi2026_excitability_connectivity.ipynb'))
print(nb['cells'][13]['metadata'], nb['cells'][14]['metadata'], list(nb['cells'][13].keys()))
for i in [36,49,50,51,61,64,65,66,71,73,80]:
    print('-----',i); print(''.join(nb['cells'][i]['source']))
"
```

```
{'tags': ['claim:adaptation-vadp-correlation']} {} ['cell_type', 'execution_count', 'id', 'metadata', 'outputs', 'source']
----- 36
### spikelet-not-scatter, highmag-footprint, detection-limits, lasso-off-target-correction (blocked)

spikelet-not-scatter needs the cross-STA fluorescence of interstitial pixels within 400 um of each
triggering cell. Only the raw-movie excerpt holds pixels: 1,152,000 frames of 328 x 448 uint16
pixels (338 GB), which would have to be streamed whole. The excerpt's own pixel subset
(`mc_pixel_subset`) holds only the 5,712 pixels of the cell disks, not interstitial pixels. The
read rate measured in this run (about 45 MB/s, printed in the data check timing) puts the movie
at over two hours, over the notebook limit; it is blocked `too_large`.
highmag-footprint needs 7.5x recordings the dandiset does not hold. detection-limits needs the
per-pair null distributions (10,000 and 5,000 draws of pulses or spikes per pair), and
lasso-off-target-correction needs per-trial evoked spike counts and the lasso penalty; neither the
per-trial IPSP responses nor the penalty and the selection of the 1755 pairs are given.
----- 49
### interaction-kernel
> The population-average effect of one L1 spike is a brief excitatory pulse of about 2 ms spreading
> at 0.28 m/s with a decay length of about 160 um, followed by inhibition that peaks around 30 ms
> and decays with a time constant of about 35 ms.

[... 208 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python - <<'EOF'
import sys, os; sys.path.insert(0, os.environ['TMPDIR'] + '/dev')
from nbed import *
p = 'qi2026_excitability_connectivity.ipynb'
nb = load(p)
# two-mice
i = find(nb, 'for nm, sel27, sel29 in [("(a) all cells"')
set_src(nb, i, '''# membrane_time_constant_ms is exactly 0 for 7 cells of M-YQ0201-27 (data check), a value no fitted
# exponential decay can take; the main variant treats it as a failed fit (missing), and keeping it is shown.
for zero_tau in ("as missing", "kept as a value"):
    for nm, sel27, sel29 in [("(a) all cells", np.ones(320, bool), np.ones(320, bool)),
                             ("(b) QC cells", QC_OPTO["M-YQ0201-27"], QC_OPTO["M-YQ0201-29"])]:
        print(f"reading {nm}, membrane time constant of 0 {zero_tau}: n = {sel27.sum()} and {sel29.sum()}")
        calls = {}
        for j, p in enumerate(L.PROPERTIES):
            a, b = PROPS["M-YQ0201-27"][sel27, j], PROPS["M-YQ0201-29"][sel29, j]
            a, b = a[np.isfinite(a)], b[np.isfinite(b)]
            if p == "membrane_time_constant_ms" and zero_tau == "as missing":
                a, b = a[a != 0], b[b != 0]
            pv = stats.ranksums(a, b).pvalue
            calls[p] = pv <= 0.05
            print(f"   {p:28s} median {np.median(a):8.4f} vs {np.median(b):8.4f}  n = {len(a)}, {len(b)}  p = {pv:.3g}")
        want = {"optical_rheobase_norm": True, "membrane_time_constant_ms": True, "adp_blue_norm": False,
                "max_firing_rate_hz": False, "pulse_adaptation": False}
        print("   calls matching the paper:", sum(calls[k] == v for k, v in want.items()), "of 5")
''')
# log-normal
i = find(nb, '### amplitudes-log-normal')
set_src(nb, i, '''### amplitudes-log-normal
> IPSP and spikelet amplitudes both follow approximately log-normal distributions.

Amplitudes of connected pairs, both mice pooled. The selection is the claims file's shared method:
QC cells, and pairs under 60 um left out of the gap-junction analyses (Results, Gap junction
coupling, paragraph 4), so connected QC pairs 60 to 400 um, the pairs of Supplementary Figure 19's
neighbouring panels (the code's band, 1,467 synaptic and 5,752 gap-junction pairs). All stored flags
and QC pairs within 400 um are shown as variants. Reading chosen in the claims file: skewness of
log amplitudes within -0.5 to 0.5 and skewness of raw amplitudes above 1.
''')
i = find(nb, 'for kind, col, flag in [("IPSP", "ipsp_amplitude_norm_per_presynaptic_spike", "synaptic_connection"),\n                        ("spikelet"')
set_src(nb, i, '''for selnm in ("QC 60 to 400 um", "QC within 400 um", "all stored flags"):
    print(selnm)
    for kind, col, flag in [("IPSP", "ipsp_amplitude_norm_per_presynaptic_spike", "synaptic_connection"),
                            ("spikelet", "spikelet_amplitude_normalized", "gap_junction_connection")]:
        per = []
        for m in L.MICE:
            M, q, QQ, D, sets = pair_sets(m)
            T = {"QC 60 to 400 um": sets["60 to 400 um"], "QC within 400 um": sets["within 400 um"],
                 "all stored flags": np.ones_like(QQ)}[selnm]
            w = M[col][M[flag] & T]
            per.append(w[np.isfinite(w)])
        v = np.concatenate(per)
        pos = v[v > 0]
        print(f"   {kind}: n = {len(v)} connected pairs, {len(v) - len(pos)} with amplitude <= 0 left out of the log; "
              f"skewness raw {stats.skew(v):.2f}, log {stats.skew(np.log(pos)):.2f}")
        for m, w in zip(L.MICE, per):
            w = w[w > 0]
            print(f"      {m}: n = {len(w)}, skewness raw {stats.skew(w):.2f}, log {stats.skew(np.log(w)):.2f}")
''')
# npy duration
i = find(nb, 'for band in ("within 400 um", "60 to 400 um"):\n    d = pd.concat(percell[band])')
s = get(nb, i)
s = s.replace('''    for selnm, T in [("QC 60-400 um", sets["60 to 400 um"]), ("all flags", np.ones_like(QQ))]:''',
 '''    for selnm, T in [("QC 60-400 um", sets["60 to 400 um"]), ("QC within 400 um", sets["within 400 um"]),
                     ("all flags", np.ones_like(QQ))]:''')
old = '''for selnm, d in AMP.groupby("sel"):
    d = d[np.isfinite(d.tau_ms) & (d.tau_ms > 0)]
    a, b = d.tau_ms[d.post_pos], d.tau_ms[~d.post_pos]
    print(f"IPSP decay, {selnm}: NPY+ post {a.mean():.1f} +/- {a.std():.1f} ms (n = {len(a)}), NPY- post {b.mean():.1f} +/- {b.std():.1f} ms "
          f"(n = {len(b)}); rank-sum p = {stats.ranksums(a, b).pvalue:.2g}")'''
assert old in s
s = s.replace(old, '''# The code's IPSP fit bounds the decay at 0.4 s (data check); a fit that ends on the bound has not
# found a decay, so fits at the bound are shown left out as well as kept.
for selnm, d in AMP.groupby("sel", sort=False):
    d = d[np.isfinite(d.tau_ms) & (d.tau_ms > 0)]
    at_bound = d.tau_ms >= 399.5
    for fits, e in [("all finite fits", d), ("fits at the 0.4 s bound left out", d[~at_bound])]:
        a, b = e.tau_ms[e.post_pos], e.tau_ms[~e.post_pos]
        print(f"IPSP decay, {selnm}, {fits} ({at_bound.sum()} at the bound): NPY+ post {a.mean():.1f} +/- {a.std():.1f} ms (n = {len(a)}), "
              f"NPY- post {b.mean():.1f} +/- {b.std():.1f} ms (n = {len(b)}); rank-sum p = {stats.ranksums(a, b).pvalue:.2g}")''')
s = s.replace('''for selnm, d in AMP.groupby("sel"):
    d = d[np.isfinite(d.amp)]''', '''for selnm, d in AMP[AMP.sel != "QC within 400 um"].groupby("sel"):
    d = d[np.isfinite(d.amp)]''')
set_src(nb, i, s)
# classifier: scaling inside each training fold
i = find(nb, 'from sklearn.linear_model import LogisticRegression')
s = get(nb, i)
s = s.replace('''def split_scores(X, y, n_splits, seed, cols=None):
    cols = list(range(X.shape[1])) if cols is None else cols
    sss = StratifiedShuffleSplit(n_splits=n_splits, test_size=0.2, random_state=seed)
    out = []
    for tr, te in sss.split(X, y):
        clf = LogisticRegression(max_iter=1000).fit(X[tr][:, cols], y[tr])''', '''def model(scale):
    """Logistic regression; for z-scored features the scaler is fitted on the training cells of
    each split only, so no test cell enters the scaling."""
    lr = LogisticRegression(max_iter=1000)
    return make_pipeline(StandardScaler(), lr) if scale == "z-scored" else lr


def split_scores(X, y, n_splits, seed, cols=None, scale="z-scored"):
    cols = list(range(X.shape[1])) if cols is None else cols
    sss = StratifiedShuffleSplit(n_splits=n_splits, test_size=0.2, random_state=seed)
    out = []
    for tr, te in sss.split(X, y):
        clf = model(scale).fit(X[tr][:, cols], y[tr])''')
s = s.replace('''def shuffled_chance(X, y, n_rep, seed):
    r = np.random.default_rng(seed)
    out = []
    for k in range(n_rep):
        ys = r.permutation(y)
        for tr, te in StratifiedKFold(5, shuffle=True, random_state=k).split(X, ys):
            clf = LogisticRegression(max_iter=1000).fit(X[tr], ys[tr])''', '''def shuffled_chance(X, y, n_rep, seed, scale="z-scored"):
    r = np.random.default_rng(seed)
    out = []
    for k in range(n_rep):
        ys = r.permutation(y)
        for tr, te in StratifiedKFold(5, shuffle=True, random_state=k).split(X, ys):
            clf = model(scale).fit(X[tr], ys[tr])''')
old = '''        Xs = (X - X.mean(0)) / X.std(0, ddof=1) if scale == "z-scored" else X
        n_sp = 10000 if (nm == "pooled" and scale == "z-scored") else 1000
        sc = split_scores(Xs, y, n_sp, 1)
        ch = shuffled_chance(Xs, y, 200 if n_sp == 10000 else 50, 2)'''
assert old in s
s = s.replace(old, '''        n_sp = 10000 if (nm == "pooled" and scale == "z-scored") else 1000
        sc = split_scores(X, y, n_sp, 1, scale=scale)
        ch = shuffled_chance(X, y, 200 if n_sp == 10000 else 50, 2, scale=scale)''')
old = '''full = split_scores(Xz, g_all, 1000, 3).mean()
drops = {p: full - split_scores(Xz, g_all, 1000, 3, [k for k in range(5) if k != j]).mean() for j, p in enumerate(L.PROPERTIES)}'''
assert old in s
s = s.replace(old, '''full = split_scores(P_all, g_all, 1000, 3).mean()
drops = {p: full - split_scores(P_all, g_all, 1000, 3, [k for k in range(5) if k != j]).mean() for j, p in enumerate(L.PROPERTIES)}''')
set_src(nb, i, s)
i = find(nb, '### npy-classifier')
replace(nb, i, 'Stratified splits and the default L2 penalty', 'Z-scoring is fitted on the training cells of each split. Stratified splits and the default L2 penalty')
# vsupp of control average
i = find(nb, 'Z = 140\nfr = lambda a, b')
s = get(nb, i)
old = '''        out[grp] = dict(n=len(sel), n_ctrl=len(cv_all), a=a, b=b, c=c, p_one=p1, p_two=p2,
                        ctrl_median=np.median(cv_all), ctrl_mean=np.mean(cv_all), **extra)'''
assert old in s
s = s.replace(old, '''        out[grp] = dict(n=len(sel), n_ctrl=len(cv_all), a=a, b=b, c=c, p_one=p1, p_two=p2,
                        ctrl_median=np.median(cv_all), ctrl_mean=np.mean(cv_all),
                        ctrl_avg=measure(cavg), pair_avg=measure(avg), **extra)''')
old = '''             f"controls median {r['ctrl_median']:.4f}, mean {r['ctrl_mean']:.4f}; rank-sum p one-sided {r['p_one']:.2g}, two-sided {r['p_two']:.2g}")'''
assert old in s
s = s.replace(old, '''             f"controls median {r['ctrl_median']:.4f}, mean {r['ctrl_mean']:.4f}, measure of the weighted control average "
             f"{r['ctrl_avg']:.4f} (of the weighted pair average {r['pair_avg']:.4f}); rank-sum p one-sided {r['p_one']:.2g}, two-sided {r['p_two']:.2g}")''')
set_src(nb, i, s)
# FWHM baselines
i = find(nb, 'from scipy.optimize import curve_fit\nlag_t')
s = get(nb, i)
old = s[s.index('base = np.median(sp_pop[np.r_[0:100, 181:281]])'):s.index('# decay length of probability')]
new = '''def fwhm(base):
    half = base + (sp_pop[pk] - base) / 2
    lo_i = pk
    while lo_i > 0 and sp_pop[lo_i] > half:
        lo_i -= 1
    hi_i = pk
    while hi_i < 280 and sp_pop[hi_i] > half:
        hi_i += 1
    # linear interpolation of the two half crossings
    x_lo = lo_i + (half - sp_pop[lo_i]) / (sp_pop[lo_i + 1] - sp_pop[lo_i])
    x_hi = hi_i - 1 + (sp_pop[hi_i - 1] - half) / (sp_pop[hi_i - 1] - sp_pop[hi_i])
    return x_hi - x_lo


print(f"spikelet population peak {sp_pop[pk]:.5f} SH at lag {pk - c0} frames")
# baselines: lags beyond +/-40 frames (main), and the flanks of the spikelet used for its amplitude
# (frames -4 to -2 and 4 to 6, Methods, Analysis for mapping gap junction connections), which sit on
# the slow hump of the waveform
for nm, base in [("median of lags beyond +/-40 frames", np.median(sp_pop[np.r_[0:100, 181:281]])),
                 ("mean of frames -4 to -2 and 4 to 6", sp_pop[np.r_[c0 - 4:c0 - 1, c0 + 4:c0 + 7]].mean())]:
    w_ = fwhm(base)
    print(f"   baseline {nm} ({base:.5f}): FWHM {w_ * L.DT * 1e3:.2f} ms ({w_:.2f} frames)")
'''
s = s.replace(old, new)
set_src(nb, i, s)
save(nb, p)
EOF
grep -n "beyond +/-50" qi2026_excitability_connectivity.ipynb | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/run_cells.py <<'EOF'
import sys, json, os, time
os.chdir("entries/001960-qi-2026")
sys.path.insert(0, os.getcwd())
import matplotlib; matplotlib.use("Agg")
nb = json.load(open(sys.argv[1]))
idx = [int(x) for x in sys.argv[2].split(",")]
g = {}
for i in idx:
    t = time.time()
    print(f"######## cell {i}", flush=True)
    exec(compile("".join(nb["cells"][i]["source"]), f"cell{i}", "exec"), g)
    print(f"######## cell {i} took {time.time()-t:.0f} s", flush=True)
EOF
cd entries/001960-qi-2026; python -c "
import json
nb=json.load(open('qi2026_excitability_connectivity.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code': print(i, ''.join(c['source'])[:60].replace(chr(10),' | '))
"
```

```
1 import os | os.environ.setdefault("OMP_NUM_THREADS", "4") | impo
3 rows = [] | U = {} | for m in L.MICE: |     for s in L.SESSIONS: |  
4 # Sampling interval, from the stored timestamps of every ses
5 # Intrinsic properties (sparseOpto units table): ranges and 
6 # Pairwise metrics: table order, distances, and value ranges
7 # Orientation of the per-pair series: row k of the table hol
8 # Do unit ids refer to the same cells across the three sessi
9 # Duplicate recordings: compare spike counts and the first 2
10 # Shared clock of stimulus and response (sparseOpto, M-YQ020
13 PROPS = {m: L.intrinsic_properties(m) for m in L.MICE} | QC_OP
16 from scipy.cluster.hierarchy import linkage, fcluster | P29 = 
19 name_of = {94: "bin1", 116: "bin2", 110: "bin3"} | lab = np.ar
22 # membrane_time_constant_ms is exactly 0 for 7 cells of M-YQ
25 pair_sets = L.pair_sets |  | rows = [] | percell = {} | for m in L.M
28 amps = {} | for m in L.MICE: |     M, q, QQ, D, sets = pair_sets
31 rows = [] | gpc = {} | for m in L.MICE: |     M, q, QQ, D, sets = 
34 had = [] | for m in L.MICE: |     f = L.open_file(m, "sparsePuls
38 def binned_prob(kind, lo, width, mice=L.MICE): |     edges = n
41 edges = np.linspace(60, 400, 7) | for variant in ["code select
44 def speed_fit(traces, centers): |     nT = traces.shape[0] |    
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; time $TMPDIR/venv/bin/python run_cells.py entries/001960-qi-2026/qi2026_excitability_connectivity.ipynb 1,3,6,13,22,25,31,44,47,50,62,69,72,75 2>&1 | grep -v "^sub-\|^   [a-z_]* *finite" | tail -120
```

```
M-YQ0201-27: outgoing 2.77 +/- 2.95, tested 25.1, probability 11.6%
   M-YQ0201-29: outgoing 2.33 +/- 2.78, tested 24.6, probability 9.7%
######## cell 25 took 0 s
######## cell 31
M-YQ0201-27: all gap-junction flags 4516, involving a non-QC cell 819
M-YQ0201-29: all gap-junction flags 2927, involving a non-QC cell 618
         mouse           band  connections  tested  median_spikelet
0  M-YQ0201-27  within 400 um         3697    7426         0.011820
1  M-YQ0201-27   60 to 400 um         3553    7280         0.011384
2  M-YQ0201-29  within 400 um         2309    7150         0.013463
3  M-YQ0201-29   60 to 400 um         2199    7032         0.012866
within 400 um: outgoing 10.43 +/- 5.87, incoming 10.43 +/- 5.30, probability 41.9 +/- 19.0% (n = 576 cells)
60 to 400 um: outgoing 9.99 +/- 5.74, incoming 9.99 +/- 5.09, probability 40.9 +/- 19.1% (n = 576 cells)
pooled median spikelet, 60 to 400 um: 0.0120 SH (expected 0.012 +/- 0.0012)
pooled median spikelet, within 400 um: 0.0125 SH (expected 0.012 +/- 0.0012)
######## cell 31 took 0 s
######## cell 44
code, 12 bins 60-420 um: pooled speed 0.265 m/s; per mouse [0.255 0.291]; delays (ms) 27 [0.35 0.37 0.56 0.8  0.85 0.99 0.99 1.12 1.19 1.38 1.52 1.63], 29 [0.51 0.51 0.68 0.95 0.97 1.15 1.16 1.31 1.39 1.38 1.38 1.57]
caption, 10 bins 60-360 um: pooled speed 0.248 m/s; per mouse [0.258 0.261]; delays (ms) 27 [0.35 0.37 0.56 0.8  0.85 0.99 0.99 1.12 1.19 1.38], 29 [0.51 0.51 0.68 0.95 0.97 1.15 1.16 1.31 1.39 1.38]
######## cell 44 took 15 s
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python -c "
import json
nb=json.load(open('qi2026_spontaneous.ipynb'))
for i in [1,2,3,20,24,25,26]:
    print('-----',i); print(''.join(nb['cells'][i]['source']))
"; sed -n 225,345p l1opto.py
```

```
----- 1
import os
os.environ.setdefault("OMP_NUM_THREADS", "4")
import time
import warnings
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import l1opto as L

warnings.filterwarnings("ignore", category=RuntimeWarning)
T0 = time.time()
print("dandiset", L.DANDISET, "version", L.VERSION)
U = {(m, s): L.units(m, s) for m in L.MICE for s in L.SESSIONS}
ST4 = {m: L.fig4_stage2(m) for m in L.MICE}  # stored state-dependent correlation arrays, binned by distance
----- 2
## Spontaneous sessions: one pass per mouse

The Figure 1 SNR claims, the Figure 4 voltage claims and the Figure 6 behaviour claims use the two
[... 340 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; $TMPDIR/venv/bin/python -c "
import l1opto as L
f=L.open_file('M-YQ0201-29','behavior')
print(f['general/notes'][()].decode()[:3000])
print(f['general/experiment_description'][()].decode()[:1500])
print(f['units/x_um'].attrs.get('description'), f['units/y_um'].attrs.get('description'))
print(f['processing/optical_voltage/subthreshold_voltage/data'].chunks, f['processing/optical_voltage/subthreshold_voltage/data'].shape)
"; grep -n -i "medial\|posterior\|anterior\|lateral" ../../paper/*.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; grep -n "^from\|^import" l1opto.py; df -h $TMPDIR | tail -1; nproc; free -g | head -2
```

```
18:from __future__ import annotations
20:import functools
22:import h5py
23:import numpy as np
24:import remfile
25:import requests
/dev/root       145G   59G   86G  41% /tmp/claude-1001
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          11           0           3          14
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; cat >> l1opto.py <<'EOF'


# ------------------------------------------------------------------ wave propagation (Supplementary Fig. 21)
def wave_events(V, x_um, y_um, quiet, whisk, segment="extrema"):
    """Wave propagation events (paper, Methods, Wave propagation analysis): peaks of the first
    derivative of the population-average subthreshold voltage above 3.5 times its s.d. over the
    whisking frames, in quiet frames. ``quiet`` and ``whisk`` are the frames analysed in each state.

    The Methods leave open the parts that set the count and the speed, so each is a reading
    (assumption, the notebook runs them all): the derivative is the centred difference of the
    population average, which is already smooth (the stored subthreshold voltage is smoothed);
    each event spans the voltage minimum and maximum flanking the peak, read as ``"extrema"``, the
    adjacent turning points of the average (the run of positive derivative holding the peak), or
    ``"window"``, the minimum in the 250 ms before and the maximum in the 250 ms after the peak.
    Events are counted per derivative peak and per distinct span (peaks sharing a span merged).

    Returns the threshold and a list of events (peak frame, first and last frame of the span)."""
    from scipy.signal import find_peaks
    pop = V.mean(1, dtype=np.float64)
    d = np.gradient(pop)
    thr = 3.5 * np.std(d[whisk])
    pk, _ = find_peaks(d, height=thr)
    pk = pk[quiet[pk]]
    n = len(pop)
    w = int(round(0.25 / DT))
    pos = d > 0
    ev = []
    for p in pk:
        if segment == "extrema":
            lo = p
            while lo > 0 and pos[lo - 1]:
                lo -= 1
            hi = p
            while hi < n - 1 and pos[hi + 1]:
                hi += 1
        else:
            a, b = max(0, p - w), min(n, p + w + 1)
            lo = a + int(np.argmin(pop[a:p + 1]))
            hi = p + int(np.argmax(pop[p:b]))
        if quiet[lo:hi + 1].all():
            ev.append((p, lo, hi))
    return thr, ev


def event_lags(X):
    """Lag (frames, signed: positive when the second cell lags the first) of the maximum of the
    cross-correlation of every pair of columns of an event snippet X (frames x cells), over all
    lags the snippet allows (Methods: "the lag-time with the maximum correlation for each pair")."""
    X = X - X.mean(0)
    L_ = X.shape[0]
    nf = 2 * L_
    F = np.fft.rfft(X, nf, axis=0)
    nc = X.shape[1]
    lag = np.zeros((nc, nc))
    lags = np.r_[np.arange(0, L_), np.arange(-L_ + 1, 0)]
    idx = np.r_[np.arange(0, L_), np.arange(nf - L_ + 1, nf)]
    for i in range(nc):
        cc = np.fft.irfft(np.conj(F[:, i:i + 1]) * F, nf, axis=0)[idx]
        lag[i] = lags[np.argmax(cc, axis=0)]
    return lag


def wave_speed(lag, x_um, y_um):
    """Speeds of one event from its pair lags (frames) and the cell positions: (a) distance
    regressed on absolute lag, (b) absolute lag regressed on distance, inverted (the claims file's
    two readings of "the slope of the line relating lag-time to separation"), and (c) a plane-wave
    fit of signed lag on the displacement vector, which also gives a direction (a variant). Speeds
    in mm/s, direction in radians in the image frame (x, y of the units table)."""
    iu = np.triu_indices(len(x_um), 1)
    dx = (x_um[None, :] - x_um[:, None])[iu]
    dy = (y_um[None, :] - y_um[:, None])[iu]
    dist = np.hypot(dx, dy)
    tl = lag[iu] * DT  # s
    at = np.abs(tl)
    out = {}
    if np.ptp(at) > 0:
        out["a"] = np.polyfit(at, dist, 1)[0] * 1e-3  # um/s -> mm/s
        sl = np.polyfit(dist, at, 1)[0]
        out["b"] = (1 / sl) * 1e-3 if sl > 0 else np.nan
    else:
        out["a"] = out["b"] = np.nan
    s, *_ = np.linalg.lstsq(np.column_stack([dx, dy]), tl, rcond=None)
    ns = np.hypot(*s)
    out["c"] = (1 / ns) * 1e-3 if ns > 0 else np.nan
    out["c_dir"] = np.arctan2(s[1], s[0])
    return out


def phase_direction(Z, x_um, y_um, grid_um=160.0, fwhm_um=325.0):
    """Propagation direction of one event from the phase gradient (Methods, Wave propagation
    analysis): Z is the analytic (Hilbert) signal of each cell averaged over the event (cells),
    smoothed with a Gaussian of 325 um full width at half maximum (assumption: "325 um wide" read as
    the FWHM) onto a 160 um grid; the flow field is the phase gradient, and the wave travels down
    it. Returns the circular mean direction (radians, image frame) of the flow vectors."""
    sig = fwhm_um / 2.355
    gx = np.arange(x_um.min(), x_um.max() + grid_um, grid_um)
    gy = np.arange(y_um.min(), y_um.max() + grid_um, grid_um)
    GX, GY = np.meshgrid(gx, gy)
    w = np.exp(-((GX[..., None] - x_um) ** 2 + (GY[..., None] - y_um) ** 2) / (2 * sig ** 2))
    Zg = (w * Z).sum(-1) / w.sum(-1)
    dzy, dzx = np.gradient(Zg, grid_um)
    a2 = np.abs(Zg) ** 2
    phx = np.imag(np.conj(Zg) * dzx) / a2
    phy = np.imag(np.conj(Zg) * dzy) / a2
    u = -(phx + 1j * phy)
    u = u[np.isfinite(u) & (np.abs(u) > 0)]
    return float(np.angle(np.mean(u / np.abs(u))))
EOF
cat > $TMPDIR/dev/wave.py <<'EOF'
import sys, time; sys.path.insert(0, "entries/001960-qi-2026")
import numpy as np
from scipy.signal import hilbert
import l1opto as L
m = sys.argv[1]; nmax = int(sys.argv[2])
t = time.time()
B = L.load_behavior(m, subthreshold=False)
f = L.open_file(m, "behavior")
d = f["processing/optical_voltage/subthreshold_voltage/data"]
sel = B["cells"]
V = np.empty((nmax, len(sel)), np.float32)
for a, x in L.iter_blocks(d, 100_000, stop=nmax):
    V[a:a + len(x)] = x[:, sel]
print("loaded", time.time() - t)
n = nmax
guard = L.chunk_guard(B["n_frames"], B["frames_per_chunk"], 1000)[:n]
q = B["quiet"][:n] & ~B["run_guard"][:n] & ~guard
w = B["whisk"][:n] & ~B["run_guard"][:n] & ~guard
x, y = B["x_um"], B["y_um"]
for seg in ("extrema", "window"):
    t = time.time()
    thr, ev = L.wave_events(V, x, y, q, w, segment=seg)
    spans = sorted(set((lo, hi) for _, lo, hi in ev))
    L_ = np.array([hi - lo + 1 for lo, hi in spans])
    print(seg, "thr", thr, "peaks", len(ev), "spans", len(spans), "span frames median", np.median(L_), np.percentile(L_, [5, 95]), "quiet s", q.sum()*L.DT)
    sp = []
    for lo, hi in spans[:200]:
        if hi - lo + 1 < 5: continue
        lag = L.event_lags(V[lo:hi + 1].astype(np.float64))
        s = L.wave_speed(lag, x, y)
        a0, b0 = max(0, lo - 300), min(n, hi + 301)
        Zs = hilbert(V[a0:b0] - V[a0:b0].mean(0), axis=0)[lo - a0:hi - a0 + 1].mean(0)
        s["dir"] = L.phase_direction(Zs, x, y)
        sp.append(s)
    print("  time per event", (time.time() - t) / max(1, len(sp)))
    for k in ("a", "b", "c"):
        v = np.array([s[k] for s in sp]); v = v[np.isfinite(v)]
        print(f"  {k}: mean {v.mean():.1f} sd {v.std():.1f} median {np.median(v):.1f} n {len(v)}")
    dirs = np.array([s["dir"] for s in sp]); cd = np.array([s["c_dir"] for s in sp])
    print("  phase dir circ mean", np.degrees(np.angle(np.mean(np.exp(1j*dirs)))), "R", abs(np.mean(np.exp(1j*dirs))),
          " plane dir", np.degrees(np.angle(np.mean(np.exp(1j*cd)))), abs(np.mean(np.exp(1j*cd))),
          " agreement cos", np.mean(np.cos(dirs - cd)))
EOF
cd $TMPDIR/dev; time $TMPDIR/venv/bin/python wave.py M-YQ0201-29 600000
```

```
loaded 64.05513525009155
extrema thr 0.027036255528538864 peaks 798 spans 488 span frames median 35.0 [20. 57.] quiet s 394.14831000000004
  time per event 0.042592352628707884
  a: mean 10.4 sd 6.0 median 9.9 n 200
  b: mean 755.7 sd 1398.1 median 388.6 n 196
  c: mean 852.2 sd 924.2 median 566.0 n 200
  phase dir circ mean 81.79527636382623 R 0.1689174932118997  plane dir 43.17946578260557 0.2425629766716337  agreement cos 0.38408481238131287
window thr 0.027036255528538864 peaks 712 spans 434 span frames median 143.5 [ 35.65 315.75] quiet s 394.14831000000004
  time per event 0.24048476815223693
  a: mean 5.6 sd 5.0 median 3.9 n 200
  b: mean 178.6 sd 292.5 median 68.4 n 200
  c: mean 185.0 sd 289.1 median 83.7 n 200
  phase dir circ mean 114.36375302052392 R 0.12784017374307075  plane dir 96.20137389328299 0.12369522889832997  agreement cos 0.25934354371030427

real	2m1.689s
user	1m1.772s
sys	0m1.380s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python - <<'EOF'
import re
s = open('l1opto.py').read()
old = '''def p_spk_given_v(V, spike_frames_list, mask, edges, offset=0):
    """P(spk|V) per cell: histogram of V at spike frames over histogram of all V in the mask,
    divided by the 1.27 ms exposure (paper, Methods, P(spk|V); code Figure 4E-F). Spike frames
    are kept when the frame is in the mask; with ``offset`` the voltage is read ``offset``
    frames before the spike (the Methods' "10 ms before" reading)."""
    nb = len(edges) - 1
    allc = np.zeros((V.shape[1], nb))
    spkc = np.zeros((V.shape[1], nb))
    for k in range(V.shape[1]):
        v = V[mask, k]'''
new = '''def p_spk_given_v(V, spike_frames_list, mask, edges, offset=0, window=0):
    """P(spk|V) per cell: histogram of V at spike frames over histogram of all V in the mask,
    divided by the 1.27 ms exposure (paper, Methods, P(spk|V); code Figure 4E-F). Spike frames
    are kept when the frame is in the mask; with ``offset`` the voltage is read ``offset``
    frames before the spike. With ``window`` > 0 the voltage of every frame, spike frames and
    all frames alike, is the mean over the ``window`` frames before it (the Results' and Fig. 4E
    legend's "10 ms interval before" reading, 8 frames = 10.2 ms)."""
    nb = len(edges) - 1
    allc = np.zeros((V.shape[1], nb))
    spkc = np.zeros((V.shape[1], nb))
    if window:
        mask = mask.copy()
        mask[:window] = False
    for k in range(V.shape[1]):
        if window:
            cs = np.concatenate([[0.0], np.cumsum(V[:, k], dtype=np.float64)])
            vk = np.full(V.shape[0], np.nan)
            vk[window:] = (cs[window:-1] - cs[:-window - 1]) / window  # frames t - window .. t - 1
            v = vk[mask]
            fr = spike_frames_list[k]
            fr = fr[mask[fr]]
            allc[k] = np.histogram(v, edges)[0]
            spkc[k] = np.histogram(vk[fr], edges)[0]
            continue
        v = V[mask, k]'''
assert old in s
s = s.replace(old, new)
open('l1opto.py', 'w').write(s)
EOF
$TMPDIR/venv/bin/python -c "
import numpy as np, l1opto as L
V=np.random.randn(1000,2).astype(np.float32); m=np.ones(1000,bool)
sf=[np.array([20,50,100]),np.array([30])]
r,a,s=L.p_spk_given_v(V,sf,m,np.linspace(-3,3,7),window=8)
print(a.sum(1), s.sum(1))
k=0; t=50; print(V[t-8:t,k].mean())
"
```

```
[992. 992.] [3. 1.]
0.5425121
```

**Agent**

Now the SP notebook edits: wave events in the pass, the new traveling-waves section, and the sigmoid variants.

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python - <<'EOF'
import sys, os; sys.path.insert(0, os.environ['TMPDIR'] + '/dev')
from nbed import *
p = 'qi2026_spontaneous.ipynb'
nb = load(p)
i = find(nb, 'from scipy.signal import butter, filtfilt, find_peaks, welch')
s = get(nb, i)
s = s.replace("from scipy.signal import butter, filtfilt, find_peaks, welch", "from scipy.signal import butter, filtfilt, find_peaks, welch, hilbert")
old = '''    # --- P(spk|V), quiet, code masks (analysisEF), at the spike frame and 8 frames (10 ms) before
    for off in (0, 8):
        rate, allc, spkc = L.p_spk_given_v(V, sf, analysisEF, VEDGES_F4, offset=off)
        R[f"pspkv_off{off}"] = (rate, allc, spkc)'''
assert old in s
s = s.replace(old, '''    # --- P(spk|V), quiet, code masks (analysisEF), at the spike frame and 8 frames (10 ms) before,
    #     and with V the mean of the 8 frames (10.2 ms) before each frame
    for off in (0, 8):
        rate, allc, spkc = L.p_spk_given_v(V, sf, analysisEF, VEDGES_F4, offset=off)
        R[f"pspkv_off{off}"] = (rate, allc, spkc)
    R["pspkv_win8"] = L.p_spk_given_v(V, sf, analysisEF, VEDGES_F4, window=8)''')
old = '''    R["quiet"], R["whisk"], R["run_guard"] = B["quiet"], B["whisk"], B["run_guard"]'''
assert old in s
s = s.replace(old, old + '''
    # --- wave propagation events (Methods, Wave propagation analysis; l1opto.wave_events): quiet and
    #     whisking frames without running and outside +/-1000 frames of a chunk edge, whole session
    tw = time.time()
    wq = quiet_nr & ~B["chunk_guard_1000"]
    ww = whisk_nr & ~B["chunk_guard_1000"]
    R["waves"] = {}
    for seg, step in (("extrema", 1), ("window", 4)):
        thr, ev = L.wave_events(V, B["x_um"], B["y_um"], wq, ww, segment=seg)
        spans = sorted(set((lo, hi) for _, lo, hi in ev))
        rows = []
        for lo, hi in spans[::step]:  # every 4th span for the longer "window" spans (run time)
            if hi - lo + 1 < 5:
                continue
            lag = L.event_lags(V[lo:hi + 1].astype(np.float64))
            sp_ = L.wave_speed(lag, B["x_um"], B["y_um"])
            a0, b0 = max(0, lo - 300), min(n, hi + 301)
            Zs = hilbert(V[a0:b0] - V[a0:b0].mean(0), axis=0)[lo - a0:hi - a0 + 1].mean(0)
            sp_["dir"] = L.phase_direction(Zs, B["x_um"], B["y_um"])
            sp_["lo"], sp_["hi"] = lo, hi
            rows.append(sp_)
        R["waves"][seg] = dict(thr=thr, peaks=np.array([e[0] for e in ev]), spans=spans, step=step,
                               quiet_s=wq.sum() * L.DT, table=pd.DataFrame(rows))
    print(f"   wave events in {time.time() - tw:.0f} s")''')
set_src(nb, i, s)
# traveling waves section
i = find(nb, '### traveling-waves (blocked)')
set_src(nb, i, '''### traveling-waves
> Quiet-state oscillations are traveling waves with various directions, a slight bias toward
> medial-posterior, and a mean speed of 18.2 +/- 8.3 mm/s (3,858 events, 2 mice); a 5 Hz
> oscillation has a wavelength of about 4 mm.

Methods, Wave propagation analysis, with no code: events are peaks of the derivative of the
population-average subthreshold voltage (QC cells) above 3.5 times its s.d. during whisking, in
quiet epochs; each event spans the voltage minimum to maximum flanking the peak; its speed is the
slope of the line relating the lag of the peak cross-correlation of every cell pair to their
separation; its direction is that of the flow field of the Hilbert phase (325 um Gaussian, 160 um
grid). Quiet and whisking frames are the stored masks without running and outside +/-1000 frames
of a chunk edge (the code's Figure 4 masks), over the whole session. The Methods leave open the
parts that set the count and the speed, so each is run (`l1opto.wave_events`): the span as the
adjacent turning points of the average ("extrema") or the minimum and maximum within 250 ms
("window"); events counted per derivative peak or per distinct span; the speed (a) distance
regressed on absolute lag, (b) absolute lag on distance, inverted (the claims file's readings), and
(c) a plane-wave fit of signed lag on displacement (a variant). The "window" spans are long, so
every fourth span is used for their speeds. The first 2000 s (the code's Figure 4 window) are shown
as a variant for the count. The files do not give the orientation of the x and y axes relative to
the brain (data check), so directions are in the image frame and the medial-posterior bias cannot
be tested.
''')
nb['cells'].insert(i + 1, cell("code", '''for seg in ("extrema", "window"):
    print(f"span reading '{seg}':")
    tot_p = tot_s = 0
    allsp = []
    for m in L.MICE:
        W = BEH[m]["waves"][seg]
        pk_ = W["peaks"]; sp_ = W["spans"]
        early = np.sum((pk_ >= 5000) & (pk_ < round(2000 / L.DT)))
        early_s = sum(1 for lo, hi in sp_ if 5000 <= lo < round(2000 / L.DT))
        tot_p += len(pk_); tot_s += len(sp_)
        t = W["table"]; allsp.append(t)
        ln = np.array([hi - lo + 1 for lo, hi in sp_]) * L.DT * 1e3
        print(f"   {m}: threshold {W['thr']:.4f} SH/frame; {W['quiet_s']:.0f} s quiet; {len(pk_)} derivative peaks, {len(sp_)} distinct spans "
              f"(first 2000 s: {early} and {early_s}); span {np.median(ln):.0f} ms median ({np.percentile(ln, 5):.0f} to {np.percentile(ln, 95):.0f}); "
              f"speeds from {len(t)} spans")
        for k in ("a", "b", "c"):
            v = t[k].values; v = v[np.isfinite(v)]
            print(f"      speed ({k}): mean {v.mean():.1f} +/- {v.std(ddof=1):.1f} mm/s, median {np.median(v):.1f} (n = {len(v)})")
    t = pd.concat(allsp)
    print(f"   both mice: {tot_p} derivative peaks, {tot_s} distinct spans")
    for k in ("a", "b", "c"):
        v = t[k].values; v = v[np.isfinite(v)]
        print(f"      speed ({k}): mean {v.mean():.1f} +/- {v.std(ddof=1):.1f} mm/s, median {np.median(v):.1f}, "
              f"5 to 95 percentile {np.percentile(v, 5):.1f} to {np.percentile(v, 95):.1f} (n = {len(v)} of {len(t)})")
    for m, tm in zip(L.MICE, allsp):
        for nm, col in (("phase gradient", "dir"), ("plane-wave fit", "c_dir")):
            z = np.exp(1j * tm[col].values)
            print(f"      {m} {nm} direction (image frame, 0 = +x, 90 = +y): circular mean {np.degrees(np.angle(z.mean())):.0f} deg, "
                  f"resultant length {abs(z.mean()):.2f}")
''', ["claim:traveling-waves"]))
nb['cells'].insert(i + 2, cell("markdown", '''**Result: PENDING**'''))
# sigmoid
i = find(nb, '### voltage-to-spike-sigmoid')
set_src(nb, i, '''### voltage-to-spike-sigmoid
> Each cell's spontaneous voltage-to-spike relationship is sigmoidal, with substantial cell-to-cell
> variation in threshold and maximum rate.

P(spk|V) per QC cell in the code's quiet analysis frames (code, Figure 4E-F), V bins of 0.04 SH from
-2 to 2. V is read three ways: at the spike frame (the code, and the Methods' V(t_s), "the
subthreshold voltage at spike times"); as the sample 8 frames (10.2 ms) before it; and as the mean
over the 8 frames (10.2 ms) before each frame, for spike frames and all frames alike (the Results'
and the Figure 4E legend's "10 ms interval"). A four-parameter logistic fitted over bins holding at
least 100 frames (the claims file's reading). Since a logistic fitted to a curve that has not
saturated can put its top far beyond the data, the spread of maxima is also given for the largest
observed rate of each cell and for fits whose top lies within twice that rate.
''')
i = find(nb, 'vc = (VEDGES_F4[:-1] + VEDGES_F4[1:]) / 2')
s = get(nb, i)
s = s.replace('''for off in (0, 8):
    rows = []
    for m in L.MICE:
        rate, allc, spkc = BEH[m][f"pspkv_off{off}"]''', '''for off in ("off0", "off8", "win8"):
    label = {"off0": "V at the spike frame", "off8": "V 8 frames before the spike", "win8": "V the mean of the 8 frames before"}[off]
    rows = []
    for m in L.MICE:
        rate, allc, spkc = BEH[m][f"pspkv_{off}"]''')
s = s.replace('''                rows.append(dict(mouse=m, r2=np.nan, v0=np.nan, top=np.nan)); continue''', '''                rows.append(dict(mouse=m, r2=np.nan, v0=np.nan, top=np.nan, ymax=np.nan)); continue''')
s = s.replace('''                rows.append(dict(mouse=m, r2=r2, v0=p[2], top=p[1]))
            except Exception:
                rows.append(dict(mouse=m, r2=np.nan, v0=np.nan, top=np.nan))''', '''                rows.append(dict(mouse=m, r2=r2, v0=p[2], top=p[1], ymax=np.nanmax(y)))
            except Exception:
                rows.append(dict(mouse=m, r2=np.nan, v0=np.nan, top=np.nan, ymax=np.nanmax(y)))''')
old = '''    print(f"V {off} frames before the spike: {len(d)} cells, fits failed {d.r2.isna().sum()}; R^2 >= 0.9 in {good.sum()} "
          f"({100*good.mean():.0f}%); among those, midpoint {d.v0[good].mean():.3f} +/- {d.v0[good].std():.3f} SH (CV {cv(d.v0[good]):.2f}), "
          f"maximum {d.top[good].median():.1f} Hz median (CV {cv(d.top[good]):.2f})")'''
assert old in s
s = s.replace(old, '''    print(f"{label}: {len(d)} cells, fits failed {d.r2.isna().sum()}; R^2 >= 0.9 in {good.sum()} "
          f"({100*good.mean():.0f}%); among those, midpoint {d.v0[good].mean():.3f} +/- {d.v0[good].std():.3f} SH (CV {cv(d.v0[good]):.2f}), "
          f"maximum {d.top[good].median():.1f} Hz median (CV {cv(d.top[good]):.2f})")
    inside = good & (d.top <= 2 * d.ymax)
    print(f"   largest observed rate among the R^2 >= 0.9 cells: median {d.ymax[good].median():.1f} Hz, CV {cv(d.ymax[good]):.2f}; "
          f"fits with the top within twice the largest observed rate: {inside.sum()} of {good.sum()}, top CV {cv(d.top[inside]):.2f}, "
          f"midpoint CV {cv(d.v0[inside]):.2f}")''')
set_src(nb, i, s)
save(nb, p)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; time $TMPDIR/venv/bin/python -c "
import l1opto as L, h5py, requests
aid=L.assets()['sub-M-YQ0201-29/sub-M-YQ0201-29_ses-behavior-rawexcerpt_behavior+ophys.nwb']
s3=requests.head(f'{L.API}/assets/{aid}/download/',allow_redirects=True).url
import remfile
f=h5py.File(remfile.File(s3),'r')
def show(name,obj):
    if isinstance(obj,h5py.Dataset) and not name.startswith('specifications'):
        print(name,obj.shape,obj.dtype,obj.chunks,obj.compression, (obj.attrs.get('description') or '')[:150] if not isinstance(obj.attrs.get('description'),bytes) else obj.attrs.get('description')[:150])
f.visititems(show)
print(f['general/notes'][()][:2500])
r=requests.get(f'{L.API}/dandisets/001960/versions/0.261013.2016/assets/{aid}/').json()
print(r.get('description') or r.get('wasGeneratedBy'), r.get('contentSize'))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 11, in <module>
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/h5py/_hl/group.py", line 407, in __getitem__
    return self._get(name)
           ^^^^^^^^^^^^^^^
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "/tmp/claude-1001/venv/lib/python3.12/site-packages/h5py/_hl/group.py", line 421, in _get
    oid = h5o.open(self.id, self._e(name), lapl=lapl)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "h5py/_objects.pyx", line 54, in h5py._objects.with_phil.wrapper
  File "h5py/_objects.pyx", line 55, in h5py._objects.with_phil.wrapper
  File "h5py/h5o.pyx", line 255, in h5py.h5o.open
KeyError: "Unable to synchronously open object (object 'notes' doesn't exist)"
acquisition/images/segmentation_reference_image (328, 448) float32 None None Mean image of the 10-second excerpt used for footprint initialisation, after optical-flow registration and after regression against a 2x3 spatially do
acquisition/images/structural_gfp (328, 448) float32 None None GFP structural z-stack (NPY-positive cells). Maximum-intensity projection of source variable hadStack_gfp over its 47 planes; the full stack is not de
acquisition/images/structural_rfp (328, 448) float32 None None RFP structural z-stack (Voltron expression). Maximum-intensity projection of source variable hadStack_rfp over its 21 planes; the full stack is not de
acquisition/raw_voltage_movie/data (1152000, 328, 448) uint16 (16, 328, 448) gzip 
acquisition/raw_voltage_movie/format () object None None 
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python -c "
import json
nb=json.load(open('qi2026_spontaneous.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code': print(i, c['metadata'].get('tags'), ''.join(c['source'])[:50].replace(chr(10),' | '))
"; date -u
```

```
1 None import os | os.environ.setdefault("OMP_NUM_THREADS",
3 ['sanity'] from scipy.signal import butter, filtfilt, find_pe
4 ['sanity'] # Shared clock of the face-camera whisking trace a
6 ['claim:spike-snr-and-detection-errors'] snr_rows = [] | for m in L.MICE: |     R = BEH[m] |     
9 ['claim:snr-decay-one-hour'] for cells in ("QC", "all"): |     ratios, first, las
12 ['claim:subthreshold-correlation-length'] F4 = {m: L.fig4_statistics(ST4[m]) for m in L.MICE
15 ['claim:subthreshold-low-dimensional'] pca_rows = [] | for m in L.MICE: |     for rd, key in 
18 ['claim:quiet-state-oscillations'] for m in L.MICE: |     out = {} |     for st in ("quie
21 ['claim:traveling-waves'] for seg in ("extrema", "window"): |     print(f"span
24 ['claim:spike-synchrony-localized'] for m in L.MICE: |     s = F4[m] |     print(f"{m}: sy
27 ['claim:voltage-to-spike-sigmoid'] vc = (VEDGES_F4[:-1] + VEDGES_F4[1:]) / 2 | logistic
30 ['claim:fig4g-private-depolarizations'] def slopes(N): |     cnt = N.sum(1) |     cm = (N * vc
33 ['claim:fig4hi-self-sta-diverges'] lag_f = np.arange(-140, 141) | for m in L.MICE: |     
36 ['claim:npy-fraction-and-similarity'] for m in L.MICE: |     print(m, "NPY+ of 320:", {s: 
39 ['claim:npy-subthreshold-similar'] for m in L.MICE: |     R = BEH[m] |     pos, neg = R["
42 ['claim:npy-umap-groups'] import umap | from sklearn.cluster import KMeans | cou
45 ['claim:npy-whisking-onset-rates'] bef = np.concatenate([BEH[m]["rate_before"] for m 
48 ['claim:npy-oscillation-peak-rates'] print("peaks per mouse:", {m: len(BEH[m]["osc_peak
51 ['claim:npy-state-dependent-excitability'] def pv46(st): |     num = np.concatenate([BEH[m][f"p
54 None print(f"notebook run time {(time.time() - T0) / 60
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; time $TMPDIR/venv/bin/python run_cells.py entries/001960-qi-2026/qi2026_spontaneous.ipynb 1,3,21,27 2>&1 | tail -60; date -u
```

```
M-YQ0201-27: 247 QC cells, 2880000 frames (3658 s); quiet 0.472, whisking 0.365, running guard 0.108 of frames; running speed -0.134 to 0.034 m/s; subthreshold 0.1 to 99.9 percentile [-1.99  1.54] SH
   wave events in 185 s
   reduced in 711 s; 4279 oscillation peaks, 688 whisking onsets (reconstruction 14 of 15), 60 frames with more than 15 cells spiking
M-YQ0201-29: 258 QC cells, 2880000 frames (3658 s); quiet 0.547, whisking 0.297, running guard 0.098 of frames; running speed -0.054 to 0.019 m/s; subthreshold 0.1 to 99.9 percentile [-2.43  1.46] SH
   wave events in 209 s
   reduced in 726 s; 5886 oscillation peaks, 551 whisking onsets (reconstruction 9 of 15), 11 frames with more than 15 cells spiking
######## cell 3 took 1438 s
######## cell 21
span reading 'extrema':
   M-YQ0201-27: threshold 0.0272 SH/frame; 1705 s quiet; 3254 derivative peaks, 2155 distinct spans (first 2000 s: 718 and 398); span 33 ms median (10 to 70); speeds from 2155 spans
      speed (a): mean 8.6 +/- 9.8 mm/s, median 7.9 (n = 2155)
      speed (b): mean 6091.7 +/- 28845.2 mm/s, median 921.6 (n = 1887)
      speed (c): mean 2797.5 +/- 4879.9 mm/s, median 1205.5 (n = 2155)
   M-YQ0201-29: threshold 0.0260 SH/frame; 1985 s quiet; 3655 derivative peaks, 2291 distinct spans (first 2000 s: 2548 and 1566); span 41 ms median (23 to 69); speeds from 2291 spans
      speed (a): mean 11.5 +/- 8.5 mm/s, median 10.5 (n = 2291)
      speed (b): mean 1693.4 +/- 18180.9 mm/s, median 505.1 (n = 2229)
      speed (c): mean 1123.9 +/- 2429.1 mm/s, median 608.4 (n = 2291)
   both mice: 6909 derivative peaks, 4446 distinct spans
      speed (a): mean 10.1 +/- 9.3 mm/s, median 9.5, 5 to 95 percentile -1.4 to 22.5 (n = 4446 of 4446)
      speed (b): mean 3709.8 +/- 23772.2 mm/s, median 632.3, 5 to 95 percentile 167.8 to 10518.2 (n = 4116 of 4446)
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python -c "
import json
nb=json.load(open('qi2026_excitability_connectivity.ipynb'))
print(''.join(nb['cells'][34]['source']))"; time $TMPDIR/venv/bin/python -c "
import l1opto as L, numpy as np, time
m='M-YQ0201-29'
f=L.open_file(m,'sparsePulseHad')
d=f['stimulus/presentation/blue_stimulation_per_cell/data']
print(d.compression, d.chunks)
tt=f['intervals/trials/trial_type'][:]; st=f['intervals/trials/start_time'][:]; sp=f['intervals/trials/stop_time'][:]
print(set(tt), (sp-st)[:5], st[:5])
ts=f['stimulus/presentation/blue_stimulation_per_cell/timestamps']
t=time.time(); x=d[0:100000]; print('read 100k', time.time()-t)
print(np.unique(x)[:10], (x>0).sum(0)[:10], (x>0).any(1).sum())
on=(x[1:]>0)&(x[:-1]==0)
r,c=np.nonzero(on); print(len(r), np.unique(r)[:20], np.bincount(np.unique(r,return_counts=True)[1])[:20])
# pulse length
k=c[0]; s=r[0]+1; print('pulse len', np.argmax(x[s:,k]==0))
u=L.units(m,'sparsePulseHad'); print(np.nanpercentile(u['estimated_spikes_per_blue_pulse'],[0,10,50,90,100]))
M=L.pair_matrices(m); a=M['ipsp_amplitude_norm_per_presynaptic_spike']; print('finite amp', np.isfinite(a).sum(), 'max dist finite', M['distance_um'][np.isfinite(a)].max(), (a!=0).sum())
"
```

```
had = []
for m in L.MICE:
    f = L.open_file(m, "sparsePulseHad")
    tt = f["intervals/trials/trial_type"][:]
    ts = L.series_timestamps(m, "sparsePulseHad")
    starts = np.searchsorted(ts, f["intervals/trials/start_time"][:])
    stops = np.searchsorted(ts, f["intervals/trials/stop_time"][:], side="right")
    blue = f["stimulus/presentation/blue_stimulation_per_cell/data"]
    u = U[m, "sparsePulseHad"]
    sfr = [L.spike_frames(x, ts) for x in u["spike_times"]]
    on_frames = np.zeros(320)
    off_frames = np.zeros(320)
    on_spk = np.zeros(320)
    off_spk = np.zeros(320)
    n_stim = np.zeros(320)
    hidx = np.nonzero(tt == b"hadamard_gap_junction_mapping")[0]
    spk_mat_idx = [np.sort(x) for x in sfr]
    for t in hidx:
        a, b = starts[t], stops[t]
        x = blue[a:b] > 0
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; sed -n 146,200p l1opto.py
```

```
def distance_matrix_um(x_um, y_um):
    xy = np.column_stack([x_um, y_um])
    return np.sqrt(((xy[:, None, :] - xy[None, :, :]) ** 2).sum(-1))


# ------------------------------------------------------------------ time series
def series_timestamps(mouse, session, path="processing/optical_voltage/normalized_voltage"):
    return open_file(mouse, session)[f"{path}/timestamps"][:]


def iter_blocks(dataset, block=100_000, start=0, stop=None, cols=None):
    """Yield (first_frame, array) over time blocks of a time x cell dataset."""
    stop = dataset.shape[0] if stop is None else stop
    for a in range(start, stop, block):
        b = min(stop, a + block)
        x = dataset[a:b]
        if cols is not None:
            x = x[:, cols]
        yield a, x

[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; cat >> l1opto.py <<'EOF'


# ------------------------------------------------------------------ per-pulse responses (Supplementary Fig. 16)
PULSE_FRAMES = 16  # 20 ms blue pulses (Methods; 16 frames in blue_stimulation_per_cell, data check)


def pulse_responses(mouse, resp_window=(16, 48), base_window=(-20, 0), spike_window=(0, 20)):
    """One row per 20 ms blue pulse of the sparse_pulse_synaptic_mapping trials of a
    sparsePulseHad session, for the lasso correction of off-target spiking (paper, Methods,
    Analysis for mapping synaptic connections, paragraph 3; Supplementary Fig. 16).

    Pulses are the rising edges of ``blue_stimulation_per_cell``; the cells lit at an onset are its
    targets. Per pulse and cell: the response, mean normalized voltage over frames
    ``resp_window`` after onset (20 to 60 ms, around the IPSP peak of about 30 ms and its decay,
    Results and Fig. 3F; assumption) minus the mean over ``base_window`` (the 25 ms before onset);
    and the evoked spikes, spikes in frames ``spike_window`` (the pulse and 5 ms after) minus spikes
    in the 20 frames before onset (a standard choice). Returns onset frames, the target mask
    (pulses x cells), responses and evoked spike counts (pulses x cells, float32)."""
    f = open_file(mouse, "sparsePulseHad")
    ts = series_timestamps(mouse, "sparsePulseHad")
    tt = f["intervals/trials/trial_type"][:]
    st = np.searchsorted(ts, f["intervals/trials/start_time"][:])
    sp = np.searchsorted(ts, f["intervals/trials/stop_time"][:], side="right")
    pulse_trial = np.zeros(len(ts), bool)
    for t in np.nonzero(tt == b"sparse_pulse_synaptic_mapping")[0]:
        pulse_trial[st[t]:sp[t]] = True
    u = units(mouse, "sparsePulseHad")
    sfr = [np.sort(spike_frames(x, ts)) for x in u["spike_times"]]
    blue = f["stimulus/presentation/blue_stimulation_per_cell/data"]
    volt = f["processing/optical_voltage/normalized_voltage/data"]
    n = len(ts)
    pad_lo, pad_hi = -min(base_window[0], -20), max(resp_window[1], spike_window[1])
    onsets, targets, resp = [], [], []
    block = 100_000
    for a in range(0, n, block):
        b = min(n, a + block)
        a0, b0 = max(0, a - pad_lo - 1), min(n, b + pad_hi)
        x = blue[a0:b0] > 0
        rise = x[1:] & ~x[:-1]
        on_rows = np.nonzero(rise.any(1))[0] + 1 + a0
        on_rows = on_rows[(on_rows >= a) & (on_rows < b) & (on_rows - pad_lo >= 0) & (on_rows + pad_hi <= n)]
        on_rows = on_rows[pulse_trial[on_rows]]
        if len(on_rows) == 0:
            continue
        V = volt[a0:b0]
        for o in on_rows:
            k = o - a0
            onsets.append(o)
            targets.append(rise[k - 1])
            r_ = V[k + resp_window[0]:k + resp_window[1]].mean(0) - V[k + base_window[0]:k + base_window[1]].mean(0)
            resp.append(r_.astype(np.float32))
    onsets = np.array(onsets)
    evoked = np.zeros((len(onsets), len(sfr)), np.float32)
    for c, fr in enumerate(sfr):
        inn = np.searchsorted(fr, onsets + spike_window[1]) - np.searchsorted(fr, onsets + spike_window[0])
        pre = np.searchsorted(fr, onsets) - np.searchsorted(fr, onsets - (spike_window[1] - spike_window[0]))
        evoked[:, c] = inn - pre
    return onsets, np.array(targets), np.array(resp), evoked
EOF
cat > $TMPDIR/dev/lasso1.py <<'EOF'
import sys, time, pickle, os; sys.path.insert(0, "entries/001960-qi-2026")
import numpy as np
import l1opto as L
out = {}
for m in L.MICE:
    t = time.time()
    out[m] = L.pulse_responses(m)
    o, T, Y, E = out[m]
    print(m, time.time() - t, "pulses", len(o), "targets per pulse", np.bincount(T.sum(1))[:15], "per cell", np.percentile(T.sum(0), [0, 50, 100]))
pickle.dump(out, open(os.environ["TMPDIR"] + "/dev/pulses.pkl", "wb"))
EOF
cd $TMPDIR/dev; time $TMPDIR/venv/bin/python lasso1.py
```

```
M-YQ0201-27 238.1279182434082 pulses 14400 targets per pulse [   0    0    0    1   24  745 3423 5667 3439 1084   17] per cell [281. 282. 480.]
M-YQ0201-29 234.39407467842102 pulses 14400 targets per pulse [   0    0    0    0    7  368 2300 4859 4719 1906  241] per cell [243. 316. 480.]

real	7m52.879s
user	0m45.222s
sys	0m16.341s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/lasso2.py <<'EOF'
import sys, time, pickle, os; sys.path.insert(0, "entries/001960-qi-2026")
import numpy as np
from scipy import stats
from sklearn.linear_model import LassoCV, Lasso
import warnings; warnings.filterwarnings("ignore")
import l1opto as L
P = pickle.load(open(os.environ["TMPDIR"] + "/dev/pulses.pkl", "rb"))
res = []
t0 = time.time()
for m in L.MICE:
    o, T, Y, E = P[m]
    M = L.pair_matrices(m)
    D = M["distance_um"]
    amp = M["ipsp_amplitude_norm_per_presynaptic_spike"]
    u = L.units(m, "sparsePulseHad")
    s_hat = u["estimated_spikes_per_blue_pulse"]
    # spiking matrix: targets get the stored per-pulse estimate (Methods), others their detected evoked spikes
    S = np.where(T, s_hat[None, :], E).astype(float)
    print(m, "off-target evoked spikes per pulse, cells within 60 um of a target vs beyond 400 um:")
    near = np.zeros_like(T); far = np.ones_like(T)
    for p in range(len(o)):
        tg = np.nonzero(T[p])[0]
        dmin = D[tg].min(0)
        near[p] = (dmin < 60) & ~T[p]; far[p] = dmin > 400
    print("   ", E[near].mean(), E[far].mean())
    raw = np.full((320, 320), np.nan); Wa = np.full((320, 320), np.nan); Wb = np.full((320, 320), np.nan)
    for j in range(320):
        cand = np.nonzero((D[:, j] <= 400) & (np.arange(320) != j))[0]
        rows = ~T[:, j]
        X = S[rows][:, cand]; y = Y[rows, j].astype(float)
        farp = rows & np.array([D[np.nonzero(T[p])[0], j].min() > 800 for p in range(len(o))])
        art = Y[farp, j].mean()
        for i in cand:
            ti = T[:, i] & rows
            raw[i, j] = (Y[ti, j].mean() - art) / s_hat[i]
        cv = LassoCV(cv=10, n_alphas=40, fit_intercept=True, random_state=0).fit(X, y)
        mse = cv.mse_path_.mean(1); se = cv.mse_path_.std(1) / np.sqrt(cv.mse_path_.shape[1])
        k = np.argmin(mse)
        a1 = cv.alphas_[np.nonzero(mse <= mse[k] + se[k])[0][0]]  # largest alpha within 1 s.e. (alphas descending)
        Wa[cand, j] = cv.coef_
        Wb[cand, j] = Lasso(alpha=a1, fit_intercept=True).fit(X, y).coef_
        if j % 80 == 0: print(j, time.time() - t0, cv.alpha_, a1)
    res.append((m, raw, Wa, Wb, M["synaptic_connection"], amp, D))
pickle.dump(res, open(os.environ["TMPDIR"] + "/dev/lasso_res.pkl", "wb"))
for name, sel_fn in [("all flags", lambda S, D: S), ("flags 60-400", lambda S, D: S & (D > 60) & (D < 400))]:
    r_raw, r_a, r_b, r_st = [], [], [], []
    for m, raw, Wa, Wb, S, amp, D in res:
        sel = sel_fn(S, D) & np.isfinite(raw)
        r_raw.append(raw[sel]); r_a.append(Wa[sel]); r_b.append(Wb[sel]); r_st.append(-amp[sel])
    raw_, a_, b_, st_ = map(np.concatenate, (r_raw, r_a, r_b, r_st))
    print(name, "n", len(raw_), "raw vs stored R", stats.pearsonr(raw_, st_)[0])
    for nm, w in (("cv-min", a_), ("1se", b_)):
        print(f"  {nm}: R corrected vs raw {stats.pearsonr(w, raw_)[0]:.3f}; vs stored {stats.pearsonr(w, st_)[0]:.3f}; "
              f"frac >20% diff from raw {np.mean(np.abs(w - raw_) > 0.2 * np.abs(raw_)):.3f}; zeroed {np.mean(w == 0):.3f}")
EOF
cd $TMPDIR/dev; time $TMPDIR/venv/bin/python lasso2.py
```

```
Exit code 1
M-YQ0201-27 off-target evoked spikes per pulse, cells within 60 um of a target vs beyond 400 um:
    0.37480316 0.0037815415
Traceback (most recent call last):
  File "/tmp/claude-1001/dev/lasso2.py", line 36, in <module>
    cv = LassoCV(cv=10, n_alphas=40, fit_intercept=True, random_state=0).fit(X, y)
         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: LassoCV.__init__() got an unexpected keyword argument 'n_alphas'

real	0m7.014s
user	0m2.014s
sys	0m0.378s
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; sed -i 's/n_alphas=40/alphas=40/' lasso2.py; time $TMPDIR/venv/bin/python lasso2.py
```

```
M-YQ0201-27 off-target evoked spikes per pulse, cells within 60 um of a target vs beyond 400 um:
    0.37480316 0.0037815415
0 6.105559825897217 2.4967095965896376e-05 0.02091437802807066
80 23.639521598815918 0.00025894661678209894 0.012750227489125987
160 41.09453058242798 2.5989153087462687e-05 0.025989153087462687
240 58.08656883239746 6.519048377941097e-05 0.013239650222291025
M-YQ0201-29 off-target evoked spikes per pulse, cells within 60 um of a target vs beyond 400 um:
    0.3849361 0.004455662
0 80.14897561073303 1.570651114295842e-05 0.01570651114295842
80 98.22902536392212 3.137546102223565e-05 0.03137546102223565
160 116.09110260009766 1.691223665776255e-05 0.01691223665776255
240 133.54003810882568 0.00015341465279660718 0.006327781244485368
all flags n 393 raw vs stored R 0.06884942440537403
  cv-min: R corrected vs raw 0.207; vs stored 0.385; frac >20% diff from raw 0.944; zeroed 0.087
  1se: R corrected vs raw nan; vs stored nan; frac >20% diff from raw 1.000; zeroed 1.000
flags 60-400 n 384 raw vs stored R 0.08071356919278498
  cv-min: R corrected vs raw 0.148; vs stored 0.498; frac >20% diff from raw 0.951; zeroed 0.089
  1se: R corrected vs raw nan; vs stored nan; frac >20% diff from raw 1.000; zeroed 1.000

real	2m32.451s
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/lasso3.py <<'EOF'
import sys, time, pickle, os; sys.path.insert(0, "entries/001960-qi-2026")
import numpy as np
from scipy import stats
import l1opto as L
P = pickle.load(open(os.environ["TMPDIR"] + "/dev/pulses.pkl", "rb"))
for m in L.MICE:
    o, T, Y, E = P[m]
    M = L.pair_matrices(m); D = M["distance_um"]; amp = M["ipsp_amplitude_norm_per_presynaptic_spike"]
    s_hat = L.units(m, "sparsePulseHad")["estimated_spikes_per_blue_pulse"]
    q = L.units(m, "sparsePulseHad")["passed_qc"]
    Tf = T.astype(float)
    near = (Tf @ (D <= 400).astype(float)) > 0  # pulses x cells: some target within 400 um
    art = np.array([Y[~near[:, j], j].mean() for j in range(320)])
    cnt = Tf.T @ np.ones(len(o))
    meanresp = (Tf.T @ Y) / cnt[:, None]  # [i, j] mean response of j over pulses targeting i
    raw = (meanresp - art[None, :]) / s_hat[:, None]
    # shared component: median over j 300-400 um from i
    sh = np.array([np.median(raw[i, (D[i] > 300) & (D[i] <= 400)]) for i in range(320)])
    raw2 = raw - sh[:, None]
    tested = (amp != 0) & (D > 0)
    S = M["synaptic_connection"]
    for nm, r in (("raw", raw), ("raw minus shared", raw2)):
        print(m, nm, "tested pairs R vs -amp", round(stats.pearsonr(r[tested], -amp[tested])[0], 3),
              "flags R", round(stats.pearsonr(r[S], -amp[S])[0], 3), "flags median raw", np.median(r[S]), "median -amp", np.median(-amp[S]),
              "unconnected tested median", np.median(r[tested & ~S]))
EOF
cd $TMPDIR/dev; $TMPDIR/venv/bin/python lasso3.py
```

```
M-YQ0201-27 raw tested pairs R vs -amp nan flags R nan flags median raw -0.019962270582171034 median -amp nan unconnected tested median 9.670709934369711e-05
M-YQ0201-27 raw minus shared tested pairs R vs -amp nan flags R nan flags median raw -0.01917319060828869 median -amp nan unconnected tested median 0.0003342158082571809
M-YQ0201-29 raw tested pairs R vs -amp 0.324 flags R 0.615 flags median raw -0.016602846275599145 median -amp -0.029237300306475745 unconnected tested median 0.0015283527021957236
M-YQ0201-29 raw minus shared tested pairs R vs -amp 0.327 flags R 0.623 flags median raw -0.015840667227672838 median -amp -0.029237300306475745 unconnected tested median 0.0008551667601603848
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; python - <<'EOF'
s = open('lasso2.py').read()
s = s.replace('''        farp = rows & np.array([D[np.nonzero(T[p])[0], j].min() > 800 for p in range(len(o))])
        art = Y[farp, j].mean()''', '''        art = Y[~near400[:, j], j].mean()''')
s = s.replace('''    raw = np.full((320, 320), np.nan)''', '''    near400 = (T.astype(float) @ (D <= 400).astype(float)) > 0
    raw = np.full((320, 320), np.nan)''')
s = s.replace('''        sel = sel_fn(S, D) & np.isfinite(raw)''', '''        sel = sel_fn(S, D) & np.isfinite(raw) & np.isfinite(amp)''')
s = s.replace('''    print(m, "off-target evoked spikes per pulse''', '''    if False: print(m, "off-target evoked spikes per pulse''')
s = s.replace('''    print("   ", E[near].mean(), E[far].mean())''', '')
s = s.replace('''    for p in range(len(o)):''', '''    for p in []:''')
open('lasso2.py', 'w').write(s)
EOF
time $TMPDIR/venv/bin/python lasso2.py 2>&1 | grep -v "^[0-9]"
```

```
all flags n 1753 raw vs stored R 0.6421308052353538
  cv-min: R corrected vs raw 0.760; vs stored 0.394; frac >20% diff from raw 0.973; zeroed 0.052
  1se: R corrected vs raw 0.159; vs stored 0.005; frac >20% diff from raw 1.000; zeroed 0.998
flags 60-400 n 1699 raw vs stored R 0.8074025918945854
  cv-min: R corrected vs raw 0.686; vs stored 0.505; frac >20% diff from raw 0.982; zeroed 0.053
  1se: R corrected vs raw 0.122; vs stored 0.033; frac >20% diff from raw 1.000; zeroed 0.998

real	2m33.407s
user	9m25.501s
sys	0m4.229s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; python - <<'EOF'
s = open('lasso2.py').read()
old = '''    S = np.where(T, s_hat[None, :], E).astype(float)'''
assert old in s
s = s.replace(old, '''    # off-target spiking only for cells within 100 um of a target of the pulse (4 off-target
    # firing length constants of 25 um, Results); elsewhere zero
    Tf = T.astype(float)
    off = ((Tf @ (D <= 100).astype(float)) > 0) & ~T
    S = np.where(T, s_hat[None, :], np.where(off, E, 0.0)).astype(float)
    print(m, "off-target entries", off.sum(), "mean evoked", E[off].mean())''')
open('lasso2.py', 'w').write(s)
EOF
time $TMPDIR/venv/bin/python lasso2.py 2>&1 | grep -v "^[0-9]"
```

```
M-YQ0201-27 off-target entries 201535 mean evoked 0.1488476
M-YQ0201-29 off-target entries 196125 mean evoked 0.13752964
all flags n 1753 raw vs stored R 0.6421308052353538
  cv-min: R corrected vs raw 0.937; vs stored 0.609; frac >20% diff from raw 0.719; zeroed 0.188
  1se: R corrected vs raw 0.054; vs stored 0.049; frac >20% diff from raw 1.000; zeroed 0.999
flags 60-400 n 1699 raw vs stored R 0.8074025918945854
  cv-min: R corrected vs raw 0.912; vs stored 0.779; frac >20% diff from raw 0.729; zeroed 0.192
  1se: R corrected vs raw 0.062; vs stored 0.051; frac >20% diff from raw 1.000; zeroed 0.999

real	2m35.336s
user	9m29.716s
sys	0m3.842s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; python - <<'EOF'
s = open('lasso2.py').read()
old = '''        X = S[rows][:, cand]; y = Y[rows, j].astype(float)'''
assert old in s
s = s.replace(old, '''        X = S[rows][:, cand]; y = Y[rows, j].astype(float)
        sd = X.std(0); sd[sd == 0] = 1
        X = X / sd''')
s = s.replace('''        Wa[cand, j] = cv.coef_
        Wb[cand, j] = Lasso(alpha=a1, fit_intercept=True).fit(X, y).coef_''', '''        Wa[cand, j] = cv.coef_ / sd
        Wb[cand, j] = Lasso(alpha=a1, fit_intercept=True).fit(X, y).coef_ / sd''')
open('lasso2s.py', 'w').write(s)
EOF
time $TMPDIR/venv/bin/python lasso2s.py 2>&1 | grep -v "^[0-9]"
```

```
M-YQ0201-27 off-target entries 201535 mean evoked 0.1488476
M-YQ0201-29 off-target entries 196125 mean evoked 0.13752964
all flags n 1753 raw vs stored R 0.6421308052353538
  cv-min: R corrected vs raw 0.950; vs stored 0.625; frac >20% diff from raw 0.775; zeroed 0.211
  1se: R corrected vs raw 0.121; vs stored 0.020; frac >20% diff from raw 1.000; zeroed 0.998
flags 60-400 n 1699 raw vs stored R 0.8074025918945854
  cv-min: R corrected vs raw 0.932; vs stored 0.791; frac >20% diff from raw 0.784; zeroed 0.214
  1se: R corrected vs raw 0.072; vs stored 0.059; frac >20% diff from raw 1.000; zeroed 0.999

real	2m32.145s
user	9m19.986s
sys	0m4.188s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; time $TMPDIR/venv/bin/python -c "
import l1opto as L, numpy as np, time
f=L.open_file('M-YQ0201-29','behavior-rawexcerpt') if False else None
import h5py, remfile, requests
aid=L.assets()['sub-M-YQ0201-29/sub-M-YQ0201-29_ses-behavior-rawexcerpt_behavior+ophys.nwb']
s3=requests.head(f'{L.API}/assets/{aid}/download/',allow_redirects=True).url
f=h5py.File(remfile.File(s3),'r')
d=f['acquisition/raw_voltage_movie/data']
t=time.time(); x=d[0:16*20]; print('20 chunks', time.time()-t, x.dtype, x.mean())
t=time.time(); x=d[160000:160000+16*60]; print('60 chunks', time.time()-t)
F=f['processing/ophys/Fluorescence/roi_response_series/data']
t=time.time(); y=F[:, :4]; print('4 traces full', time.time()-t, y.shape)
print(f['intervals/recording_chunks/start_time'][:], f['intervals/recording_chunks/stop_time'][:], f['intervals/recording_chunks/chunk_id'][:])
"
```

```
20 chunks 3.0473110675811768 uint16 19841.705622443755
60 chunks 8.82175087928772
4 traces full 5.80986213684082 (1152000, 4)
[   0.       365.75875  731.5175  1097.27625] [ 365.75873  731.51748 1097.27623 1463.03498] [0 1 2 3]

real	0m22.046s
user	0m1.840s
sys	0m1.044s
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; cat >> l1opto.py <<'EOF'


def lasso_correction(targets, resp, evoked, dist_um, spikes_per_pulse, offtarget_um=100.0, seed=0):
    """Off-target correction of the IPSP matrix (paper, Methods, Analysis for mapping synaptic
    connections, paragraph 3; Supplementary Fig. 16A: R = S W, W by lasso).

    For each postsynaptic cell j, over the pulses that do not target j: the response of j is
    regressed on the spikes each candidate presynaptic cell k (within 400 um of j, k != j) fired
    in the pulse, with an intercept (the blue-flash response, which the Methods subtract as the
    mean response to faraway stimulation). Spikes of a targeted cell are its stored
    ``estimated_spikes_per_blue_pulse`` (Methods: the evoked count of bursting cells is estimated
    from the spectrum); spikes of a non-targeted cell are its detected evoked spikes when it lies
    within ``offtarget_um`` of a target (4 off-target firing length constants of 25 um, Results),
    and zero elsewhere (assumption: detected counts far from any target are spontaneous noise).
    Penalty by 10-fold cross-validation (scikit-learn LassoCV, 40 penalties, unstandardized
    predictors): (a) the penalty of least error, (b) the largest within one standard error of it
    (the claims file's readings); ordinary least squares is shown as a variant.

    The raw matrix ("assuming only on-target stimulation") is the mean response of j over pulses
    targeting i, minus its mean over pulses with no target within 400 um of j, divided by the spikes
    per pulse of i. All matrices are [pre, post] in SH per presynaptic spike."""
    from sklearn.linear_model import Lasso, LassoCV, LinearRegression
    T = np.asarray(targets, bool)
    n_cells = T.shape[1]
    Tf = T.astype(float)
    off = ((Tf @ (dist_um <= offtarget_um).astype(float)) > 0) & ~T
    S = np.where(T, spikes_per_pulse[None, :], np.where(off, evoked, 0.0)).astype(float)
    near400 = (Tf @ (dist_um <= 400).astype(float)) > 0
    raw, wa, wb, wo = (np.full((n_cells, n_cells), np.nan) for _ in range(4))
    alphas = np.zeros((n_cells, 2))
    for j in range(n_cells):
        cand = np.nonzero((dist_um[:, j] <= 400) & (np.arange(n_cells) != j))[0]
        rows = ~T[:, j]
        y = resp[rows, j].astype(float)
        art = resp[~near400[:, j], j].mean()
        for i in cand:
            raw[i, j] = (resp[T[:, i] & rows, j].mean() - art) / spikes_per_pulse[i]
        X = S[rows][:, cand]
        cv = LassoCV(cv=10, alphas=40, fit_intercept=True, random_state=seed).fit(X, y)
        mse = cv.mse_path_.mean(1)
        se = cv.mse_path_.std(1) / np.sqrt(cv.mse_path_.shape[1])
        k = int(np.argmin(mse))
        a1 = cv.alphas_[np.nonzero(mse <= mse[k] + se[k])[0][0]]  # alphas_ run from large to small
        wa[cand, j] = cv.coef_
        wb[cand, j] = Lasso(alpha=a1, fit_intercept=True).fit(X, y).coef_
        wo[cand, j] = LinearRegression().fit(X, y).coef_
        alphas[j] = cv.alpha_, a1
    return dict(raw=raw, cv_min=wa, one_se=wb, ols=wo, alphas=alphas, offtarget=off, S=S)
EOF
python - <<'EOF'
import sys, os; sys.path.insert(0, os.environ['TMPDIR'] + '/dev')
from nbed import *
p = 'qi2026_excitability_connectivity.ipynb'
nb = load(p)
i = find(nb, '### spikelet-not-scatter, highmag-footprint, detection-limits, lasso-off-target-correction (blocked)')
set_src(nb, i, '''### spikelet-not-scatter, highmag-footprint, detection-limits (blocked)

spikelet-not-scatter needs the cross-STA fluorescence of interstitial pixels within 400 um of each
triggering cell. Only the raw-movie excerpt holds pixels: 1,152,000 frames of 328 x 448 uint16
pixels in gzip chunks of 16 frames; its stored pixel subset (`mc_pixel_subset`) holds only the 5,712
pixels of the cell disks, not interstitial pixels. A partial test on a subset of frames is possible
(reading the movie runs at about 110 frames per second, so 40,000 frames take about 6 minutes) but
was not built in the time of this revision; the claim stays blocked `too_large` for the whole
movie (about 3 hours at that rate). highmag-footprint needs 7.5x recordings the dandiset does not
hold. detection-limits needs each pair's connection statistic and its null distribution; the
pairwise table holds only the calls, amplitudes, decays and distances (its full listing is printed
below), and rebuilding the paper's statistic (the residual sums of squares of the IPSP model with
and without its double exponential, Methods) for 10,000 null draws per tested pair is out of reach
(see the timing below).
''')
nb['cells'].insert(i + 1, cell("code", '''# Everything stored in the pairwise table, and the cost of the paper's connection statistic
from scipy.optimize import least_squares
for m in L.MICE:
    g = L.open_file(m, "sparsePulseHad")["analysis/pairwise_connectivity_metrics"]
    print(m, {k: g[k].shape for k in g.keys()})
lag_s = (np.arange(281) - 140) * L.DT
tpost = np.clip(lag_s, 0, None)
rng_fit = np.random.default_rng(5)
yy = -0.03 * (np.exp(-tpost / 0.035) - np.exp(-tpost / 0.005)) * (lag_s > 0) + rng_fit.normal(0, 0.01, 281)
h1 = lambda p: p[0] * (np.exp(-tpost / p[1]) - np.exp(-tpost / p[2])) * (lag_s > 0) + p[3] + p[4] * lag_s + p[5] * lag_s ** 2 - yy
tf = time.time()
for _ in range(50):
    least_squares(h1, [-0.02, 0.03, 0.004, 0, 0, 0], bounds=([-1, 0.006, 0.001, -1, -10, -100], [1, 0.4, 0.05, 1, 10, 100]))
per_fit = (time.time() - tf) / 50
n_tested = sum(int(L.pair_sets(m)[4]["within 400 um"].sum()) for m in L.MICE)
print(f"one double-exponential IPSP fit: {per_fit*1e3:.1f} ms; {n_tested} tested pairs x 10,000 null draws x 1 fit = "
      f"{n_tested * 1e4 * per_fit / 3600:.0f} h")
''', ["claim:detection-limits"]))
nb['cells'].insert(i + 2, cell("markdown", '''### lasso-off-target-correction
> Correcting the IPSP matrix for spikes evoked in non-targeted cells by lasso regression changes
> little; the corrected and raw matrices correlate with R = 0.82 and fewer than 20% of significant
> IPSPs differ by more than 20%.

The dandiset does not store the paper's matrices, so both are rebuilt from the sparsePulseHad
sessions with `l1opto.pulse_responses` and `l1opto.lasso_correction`, whose docstrings say where each
choice comes from. One row per 20 ms pulse (the Methods' 14,400 trials, each cell targeted 243 to
480 times): the response of every cell, its mean normalized voltage 20 to 60 ms after onset minus
the 25 ms before (assumption: a window around the IPSP peak of about 30 ms, since the paper's
per-trial response is not given), and the evoked spikes of every cell. The model is R = S W
(Supplementary Fig. 16A) with S the spikes per pulse of targeted cells (stored estimate) and of
non-targeted cells within 100 um of a target (detected), fitted per postsynaptic cell by lasso with
an intercept. Penalty readings (a) least cross-validated error, (b) the largest within one standard
error (claims file); least squares as a variant. The comparison is over the 1755 pairs, the stored
synaptic flags of both mice (955 and 800; the 2 without a stored amplitude are kept here since the
rebuilt matrices do not need it), and pairs 60 to 400 um as a variant: Pearson R of corrected
against raw, and the fraction of pairs whose corrected value differs from the raw by more than 20%
of the raw. The rebuilt raw matrix is compared with the stored amplitudes to show that it measures
the same IPSPs.
'''))
nb['cells'].insert(i + 3, cell("code", '''tl = time.time()
LASSO = {}
for m in L.MICE:
    onsets, T_p, Y_p, E_p = L.pulse_responses(m)
    M, q, QQ, D, sets = pair_sets(m)
    s_hat = U[m, "sparsePulseHad"]["estimated_spikes_per_blue_pulse"]
    dmin = np.where(T_p[:, :, None], D[None, :, :], np.inf).min(1)  # pulses x cells: distance to the nearest target
    print(f"{m}: {len(onsets)} pulses, {T_p.sum(1).min()} to {T_p.sum(1).max()} targets per pulse, each cell targeted "
          f"{T_p.sum(0).min()} to {T_p.sum(0).max()} times; evoked spikes per pulse in non-targeted cells within 60 um of a target "
          f"{E_p[(dmin < 60) & ~T_p].mean():.3f}, 60 to 100 um {E_p[(dmin >= 60) & (dmin < 100) & ~T_p].mean():.3f}, "
          f"beyond 400 um {E_p[dmin > 400].mean():.4f}; targeted cells, stored estimate {np.mean(s_hat):.2f}, detected {E_p[T_p].mean():.2f}")
    LASSO[m] = L.lasso_correction(T_p, Y_p, E_p, D, s_hat)
    del T_p, Y_p, E_p, dmin
print(f"pulses and fits in {time.time() - tl:.0f} s")
for selnm in ("all stored flags", "flags 60 to 400 um"):
    acc = {k: [] for k in ("raw", "cv_min", "one_se", "ols", "stored")}
    for m in L.MICE:
        M, q, QQ, D, sets = pair_sets(m)
        sel = M["synaptic_connection"] & ((D > 60) & (D < 400) if selnm != "all stored flags" else True)
        for k in ("raw", "cv_min", "one_se", "ols"):
            acc[k].append(LASSO[m][k][sel])
        acc["stored"].append(-M["ipsp_amplitude_norm_per_presynaptic_spike"][sel])
    acc = {k: np.concatenate(v) for k, v in acc.items()}
    ok = np.isfinite(acc["stored"])
    print(f"\\n{selnm}: {len(acc['raw'])} pairs; rebuilt raw against stored amplitude R = {stats.pearsonr(acc['raw'][ok], acc['stored'][ok])[0]:.3f} "
          f"({ok.sum()} with a stored amplitude); median rebuilt raw {np.median(acc['raw']):.4f}, stored {np.median(acc['stored'][ok]):.4f} SH per spike")
    for k, nm in (("cv_min", "(a) least CV error"), ("one_se", "(b) one standard error"), ("ols", "least squares (variant)")):
        w, r = acc[k], acc["raw"]
        rr = stats.pearsonr(w, r) if np.ptp(w) > 0 else (np.nan, np.nan)
        print(f"   {nm}: corrected against raw R = {rr[0]:.3f} (p = {rr[1]:.2g}); differing by more than 20% of raw: "
              f"{100*np.mean(np.abs(w - r) > 0.2 * np.abs(r)):.1f}%; set to zero {100*np.mean(w == 0):.1f}%; "
              f"median ratio corrected / raw {np.median(w / r):.2f}")
for m in L.MICE:
    a = LASSO[m]["alphas"]
    print(f"{m}: penalty (a) median {np.median(a[:, 0]):.2g}, (b) median {np.median(a[:, 1]):.2g}; off-target entries in S {LASSO[m]['offtarget'].sum()}")
''', ["claim:lasso-off-target-correction"]))
nb['cells'].insert(i + 4, cell("markdown", '''**Result: PENDING**'''))
save(nb, p)
EOF
echo done
```

```
done
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python - <<'EOF'
import sys, os; sys.path.insert(0, os.environ['TMPDIR'] + '/dev')
from nbed import *
p = 'qi2026_excitability_connectivity.ipynb'
nb = load(p)
i = find(nb, 'tl = time.time()\nLASSO = {}')
replace(nb, i, '''    dmin = np.where(T_p[:, :, None], D[None, :, :], np.inf).min(1)  # pulses x cells: distance to the nearest target''',
 '''    dmin = np.array([D[t_].min(0) for t_ in T_p])  # pulses x cells: distance to the nearest target''')
save(nb, p)
EOF
cd $TMPDIR/dev; python - <<'EOF'
import json
nb=json.load(open('entries/001960-qi-2026/qi2026_excitability_connectivity.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code' and (c['metadata'].get('tags') or [''])[0] in ('claim:detection-limits','claim:lasso-off-target-correction'): print(i)
EOF
```

```
37
39
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; cat > patch_pulses.py <<'EOF'
import pickle, os
_P = pickle.load(open(os.environ["TMPDIR"] + "/dev/pulses.pkl", "rb"))
L.pulse_responses = lambda m: _P[m]
EOF
python - <<'EOF'
s=open('run_cells.py').read()
s=s.replace('''idx = [int(x) for x in sys.argv[2].split(",")]
g = {}
for i in idx:''','''idx = sys.argv[2].split(",")
g = {}
for i in idx:
    if i.startswith("patch:"):
        exec(open(i[6:]).read(), g); continue
    i = int(i)''')
open('run_cells.py','w').write(s)
EOF
time $TMPDIR/venv/bin/python run_cells.py entries/001960-qi-2026/qi2026_excitability_connectivity.ipynb 1,3,patch:$TMPDIR/dev/patch_pulses.py,25,37,39 2>&1 | grep -v "^sub-" | tail -30
```

```
within 400 um, per cell (n = 576 QC cells, 2 mice): outgoing 2.62 +/- 2.93, incoming 2.62 +/- 2.62, tested 25.3 +/- 8.6, probability 10.8 +/- 11.7% (0 cells with no tested partner)
   M-YQ0201-27: outgoing 2.86 +/- 3.02, tested 25.6, probability 11.7%
   M-YQ0201-29: outgoing 2.37 +/- 2.83, tested 25.0, probability 9.8%

60 to 400 um, per cell (n = 576 QC cells, 2 mice): outgoing 2.55 +/- 2.87, incoming 2.55 +/- 2.61, tested 24.8 +/- 8.5, probability 10.7 +/- 11.6% (0 cells with no tested partner)
   M-YQ0201-27: outgoing 2.77 +/- 2.95, tested 25.1, probability 11.6%
   M-YQ0201-29: outgoing 2.33 +/- 2.78, tested 24.6, probability 9.7%
######## cell 25 took 2 s
######## cell 37
M-YQ0201-27 {'distance_pixels': (102400,), 'gap_junction_connection': (102400,), 'hadamard_orthogonal_spike_times': (39011337,), 'hadamard_orthogonal_spike_times_index': (102400,), 'id': (102400,), 'ipsp_amplitude_norm_per_presynaptic_spike': (102400,), 'ipsp_decay_source_units': (102400,), 'ipsp_decay_standard_error_source_units': (102400,), 'postsynaptic_unit_id': (102400,), 'presynaptic_unit_id': (102400,), 'spikelet_amplitude_normalized': (102400,), 'synaptic_connection': (102400,)}
M-YQ0201-29 {'distance_pixels': (102400,), 'gap_junction_connection': (102400,), 'hadamard_orthogonal_spike_times': (29865553,), 'hadamard_orthogonal_spike_times_index': (102400,), 'id': (102400,), 'ipsp_amplitude_norm_per_presynaptic_spike': (102400,), 'ipsp_decay_source_units': (102400,), 'ipsp_decay_standard_error_source_units': (102400,), 'postsynaptic_unit_id': (102400,), 'presynaptic_unit_id': (102400,), 'spikelet_amplitude_normalized': (102400,), 'synaptic_connection': (102400,)}
one double-exponential IPSP fit: 46.2 ms; 14576 tested pairs x 10,000 null draws x 1 fit = 1870 h
######## cell 37 took 2 s
######## cell 39
M-YQ0201-27: 14400 pulses, 3 to 10 targets per pulse, each cell targeted 281 to 480 times; evoked spikes per pulse in non-targeted cells within 60 um of a target 0.375, 60 to 100 um 0.040,
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 342,440p tools/entry.py; cat .gitignore | head -30
```

```
def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
    # A kernel of the entry's own environment, under a name no other kernel on the machine has, so
    # nbconvert cannot pick up some other "python3" kernel (a user's or a conda install's).
    kernel = f"registry-{entry_dir.name}"
    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
                ["uv", "pip", "install", "--quiet", "--python", str(python),
                 "-r", str(entry_dir / "requirements.lock.txt"), *HARNESS],
                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
        if subprocess.run(cmd).returncode != 0:
            print(f"error: could not build the environment ({' '.join(cmd[:3])})", file=sys.stderr)
            return 1

    results, failed = [], False
    for notebook in entry["notebooks"]:
        name = notebook["path"]
        started = time.time()
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python - <<'EOF'
import sys, os; sys.path.insert(0, os.environ['TMPDIR'] + '/dev')
from nbed import *
p = 'qi2026_spontaneous.ipynb'
nb = load(p)
i = find(nb, 'snr_rows = []')
nb['cells'].insert(i + 1, cell("code", '''# What the raw-movie excerpt holds (its DANDI metadata mentions "the demixing and spike-finding
# products"): every dataset outside the NWB specifications, to see whether a matched-filter
# output or a fitted spike mixture is stored
import h5py
fx = L.open_file("M-YQ0201-29", "behavior-rawexcerpt")
listing = []
fx.visititems(lambda name, obj: listing.append((name, obj.shape, str(obj.dtype)))
              if isinstance(obj, h5py.Dataset) and not name.startswith("specifications") else None)
for name, shape, dt in listing:
    print(f"   {name} {shape} {dt}")
print("datasets named like a filter, template, threshold or mixture:",
      [n for n, _, _ in listing if any(k in n.lower() for k in ("filter", "template", "thresh", "mixture", "gauss", "snr"))])
''', ["claim:spike-snr-and-detection-errors"]))
save(nb, p)
EOF
grep -n "def asset_path" -A3 l1opto.py
```

```
49:def asset_path(mouse: str, session: str) -> str:
50-    return f"sub-{mouse}/sub-{mouse}_ses-{session}_behavior+ophys.nwb"
51-
52-
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; cat > t.py <<'EOF'
import sys, time; sys.path.insert(0, "entries/001960-qi-2026")
import l1opto as L, json
nb = json.load(open("entries/001960-qi-2026/qi2026_spontaneous.ipynb"))
src = [ "".join(c["source"]) for c in nb["cells"] if "".join(c["source"]).startswith("# What the raw-movie")][0]
t = time.time(); exec(src); print(time.time() - t)
EOF
time $TMPDIR/venv/bin/python t.py
```

```
acquisition/images/segmentation_reference_image (328, 448) float32
   acquisition/images/structural_gfp (328, 448) float32
   acquisition/images/structural_rfp (328, 448) float32
   acquisition/raw_voltage_movie/data (1152000, 328, 448) uint16
   acquisition/raw_voltage_movie/format () object
   acquisition/raw_voltage_movie/timestamps (1152000,) float64
   file_create_date (1,) object
   general/experiment_description () object
   general/optophysiology/imaging_plane/description () object
   general/optophysiology/imaging_plane/excitation_lambda () float64
   general/optophysiology/imaging_plane/grid_spacing (2,) float64
   general/optophysiology/imaging_plane/imaging_rate () float64
   general/optophysiology/imaging_plane/indicator () object
   general/optophysiology/imaging_plane/location () object
   general/optophysiology/imaging_plane/opticalchannel/description () object
   general/optophysiology/imaging_plane/opticalchannel/emission_lambda () float64
   general/session_id () object
   general/subject/date_of_birth (1,) object
   general/subject/description () object
   general/subject/genotype () object
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd  timeout 300 python tools/entry.py check entries/001960-qi-2026 2>&1 | tail -20
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
0 error(s)
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python - <<'EOF'
import sys, os, uuid; sys.path.insert(0, os.environ['TMPDIR'] + '/dev')
from nbed import *
for p in ('qi2026_excitability_connectivity.ipynb', 'qi2026_spontaneous.ipynb'):
    nb = load(p)
    for c in nb['cells']:
        if 'id' not in c: c['id'] = uuid.uuid4().hex[:8]
    save(nb, p)
EOF
cd  python tools/entry.py lock entries/001960-qi-2026 && git diff --stat; date -u
```

```
wrote entries/001960-qi-2026/requirements.lock.txt
 entries/001960-qi-2026/l1opto.py                   | 245 ++++++++++++++++-
 .../qi2026_excitability_connectivity.ipynb         | 296 ++++++++++++++++-----
 entries/001960-qi-2026/qi2026_spontaneous.ipynb    | 156 +++++++++--
 3 files changed, 610 insertions(+), 87 deletions(-)
Fri Nov  6 09:56:17 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; cat >> l1opto.py <<'EOF'


# ------------------------------------------------------------------ scattered fluorescence (Supplementary Fig. 17)
def scatter_sta(mouse="M-YQ0201-29", n_frames=32_000, start=0, bin_px=4, block=1600):
    """Cross-STA fluorescence of interstitial pixels in the raw-movie excerpt (paper, Methods,
    Analysis for mapping gap junction connections, paragraph 4), on a subset of frames.

    The movie is read for frames ``start`` to ``start + n_frames`` (a subset: the whole excerpt is
    1,152,000 frames) and averaged in ``bin_px`` x ``bin_px`` pixel bins (26 um; a computational
    choice, the scatter varies over tens of um). Interstitial bins are those holding no pixel of
    any cell's footprint (``image_mask`` > 0; Supplementary Fig. 17A: "Regions containing other
    cells were excluded"). For each cell (trigger), the STA of every interstitial bin over lags -6
    to 6 frames, and the STA of the trigger's own footprint (mask-weighted mean of its pixels).
    The STA fluorescence is normalized by the trigger's spike fluorescence, frame 0 minus frame
    -2 of its own STA, and the scatter amplitude is extracted as a spikelet: the mean of frames
    {0, 1} minus the mean of frames {-4, -3, -2, 4, 5, 6} (Methods). Returns per trigger cell and
    interstitial bin the normalized scatter amplitude, the distance (um), and spike counts."""
    from scipy import sparse
    f = open_file(mouse, "behavior-rawexcerpt")
    mov = f["acquisition/raw_voltage_movie/data"]
    ts = f["acquisition/raw_voltage_movie/timestamps"][:]
    H, Wd = mov.shape[1:]
    masks = f["processing/ophys/ImageSegmentation/plane_segmentation/image_mask"][:]
    u = units(mouse, "behavior-rawexcerpt")
    n_cells = masks.shape[0]
    hb, wb = H // bin_px, Wd // bin_px
    cellpix = (masks > 0).any(0)[:hb * bin_px, :wb * bin_px]
    inter = ~cellpix.reshape(hb, bin_px, wb, bin_px).any((1, 3)).ravel()
    gy, gx = np.meshgrid((np.arange(hb) + 0.5) * bin_px - 0.5, (np.arange(wb) + 0.5) * bin_px - 0.5, indexing="ij")
    gx, gy = gx.ravel()[inter], gy.ravel()[inter]
    dist = np.hypot(u["x_pixel"][:, None] - gx[None, :], u["y_pixel"][:, None] - gy[None, :]) * PIXEL_UM
    Mw = sparse.csr_matrix(masks.reshape(n_cells, -1).astype(np.float64))
    Mw = sparse.diags(1 / np.asarray(Mw.sum(1)).ravel()) @ Mw
    lags = np.arange(-6, 7)
    stop = start + n_frames
    sfr = [spike_frames(x, ts) for x in u["spike_times"]]
    sfr = [s_[(s_ >= start + 6) & (s_ < stop - 6)] for s_ in sfr]
    sta_pix = np.zeros((n_cells, len(lags), inter.sum()))
    sta_own = np.zeros((n_cells, len(lags)))
    for a in range(start, stop, block):
        a0, b0 = max(start, a - 6), min(stop, a + block + 6)
        X = mov[a0:b0].astype(np.float32)
        own = (Mw @ X.reshape(len(X), -1).T.astype(np.float64)).T  # frames x cells
        Xb = X[:, :hb * bin_px, :wb * bin_px].reshape(len(X), hb, bin_px, wb, bin_px).mean((2, 4)).reshape(len(X), -1)[:, inter]
        for k, l in enumerate(lags):
            rows, cols = [], []
            for c, s_ in enumerate(sfr):
                s_ = s_[(s_ >= a) & (s_ < min(a + block, stop))]
                rows.append(np.full(len(s_), c)); cols.append(s_ + l - a0)
            rows, cols = np.concatenate(rows), np.concatenate(cols)
            P = sparse.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(n_cells, len(X)))
            sta_pix[:, k] += P @ Xb
            sta_own[:, k] += P @ own[:, np.arange(n_cells)].diagonal() if False else np.asarray(P.multiply(own.T).sum(1)).ravel()
    n_spk = np.array([len(s_) for s_ in sfr])
    with np.errstate(invalid="ignore", divide="ignore"):
        sta_pix /= n_spk[:, None, None]
        sta_own /= n_spk[:, None]
    z = 6
    spike_f = sta_own[:, z] - sta_own[:, z - 2]
    ext = lambda S: S[:, [z, z + 1]].mean(1) - S[:, [z - 4, z - 3, z - 2, z + 4, z + 5, z + 6]].mean(1)
    amp = ext(sta_pix) / spike_f[:, None]
    return dict(amp=amp, dist=dist, n_spikes=n_spk, spike_f=spike_f, own_sta=sta_own, n_bins=int(inter.sum()),
                qc=u["passed_qc"])
EOF
grep -n "behavior-rawexcerpt\|def units" l1opto.py | head; cat > $TMPDIR/dev/scat.py <<'EOF'
import sys, time; sys.path.insert(0, "entries/001960-qi-2026")
import numpy as np, l1opto as L
t = time.time()
r = L.scatter_sta(n_frames=int(sys.argv[1]))
print("time", time.time() - t, "bins", r["n_bins"], "spikes median", np.median(r["n_spikes"]), "spike_f median", np.median(r["spike_f"]))
print("own STA median over cells", np.round(np.median(r["own_sta"] - r["own_sta"][:, :1], 0), 1))
ed = np.arange(0, 401, 40)
for a, b in zip(ed[:-1], ed[1:]):
    s = (r["dist"] >= a) & (r["dist"] < b) & r["qc"][:, None]
    print(a, b, s.sum(), np.nanmean(r["amp"][s]), np.nanmedian(r["amp"][s]))
EOF
cd $TMPDIR/dev; time $TMPDIR/venv/bin/python scat.py 3200
```

```
67:def units(mouse: str, session: str) -> dict:
926:    f = open_file(mouse, "behavior-rawexcerpt")
931:    u = units(mouse, "behavior-rawexcerpt")
time 59.99833273887634 bins 5971 spikes median 3.0 spike_f median nan
own STA median over cells [nan nan nan nan nan nan nan nan nan nan nan nan nan]
0 40 199 0.03279926949455601 0.03953593962535238
40 80 2148 0.012848464691350186 0.01308890553589973
80 120 4627 0.0052501837985679855 0.00378387178451117
120 160 6878 0.01495328167543644 0.0035159003693082318
160 200 9073 -0.000669645057844781 0.002063124843504778
200 240 11048 0.014262289711911161 0.0026869190258779225
240 280 13000 -0.0009053375961296605 0.001886769922204691
280 320 15271 -0.0004574709663380816 0.0010742689035625915
320 360 16895 -0.0014172952736216798 0.0012892791500752733
360 400 18770 0.0021679919139591807 0.0009611833384480115

real	1m0.316s
user	0m10.038s
sys	0m3.523s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python - <<'EOF'
s = open('l1opto.py').read()
s = s.replace('''            sta_own[:, k] += P @ own[:, np.arange(n_cells)].diagonal() if False else np.asarray(P.multiply(own.T).sum(1)).ravel()''',
'''            sta_own[:, k] += np.asarray(P.multiply(own.T).sum(1)).ravel()''')
open('l1opto.py', 'w').write(s)
import sys, os, uuid; sys.path.insert(0, os.environ['TMPDIR'] + '/dev')
from nbed import *
p = 'qi2026_excitability_connectivity.ipynb'
nb = load(p)
i = find(nb, '### spikelet-not-scatter, highmag-footprint, detection-limits (blocked)')
set_src(nb, i, '''### highmag-footprint, detection-limits (blocked)

highmag-footprint needs 7.5x recordings the dandiset does not hold. detection-limits needs each
pair's connection statistic and its null distribution; the pairwise table holds only the calls,
amplitudes, decays and distances (its full listing is printed below), and rebuilding the paper's
statistic (the residual sums of squares of the IPSP model with and without its double exponential,
Methods) for 10,000 null draws per tested pair is out of reach (see the timing below).
''')
k = find(nb, '### lasso-off-target-correction')
new_md = cell("markdown", '''### spikelet-not-scatter
> Fluorescence scattered from a spiking cell decays over a much shorter distance than the spikelet
> amplitude (spikelet to scatter ratio above 2.5 at 60 um), so pairs under 60 um were excluded.

Only the raw-movie excerpt (M-YQ0201-29, behavior session, 1,152,000 frames) holds interstitial
pixels. The whole movie would take about 3 hours to read at the measured rate, so this is a partial
test on its first 40,000 frames (51 s), with `l1opto.scatter_sta` (Methods, Analysis for mapping gap
junction connections, paragraph 4): cross-STA fluorescence of interstitial pixels (4 x 4 pixel bins,
26 um, holding no footprint pixel) within 400 um of each triggering cell, normalized by the
trigger's spike fluorescence (frame 0 minus frame -2 of its own STA), and extracted as a spikelet.
Trigger cells are the excerpt's QC cells with at least 20 spikes in the frames read. Spikelets are
the stored `spikelet_amplitude_normalized` of the M-YQ0201-29 connectivity session, QC pairs, all
pairs (as Supplementary Fig. 17B's "cell pairs") and connected pairs as a variant. 40 um bins
(Supplementary Fig. 17B); the bin holding 60 um is 40 to 80 um. Means as the criterion, medians as a
variant, since a few triggers with small spike fluorescence give large normalized values.
''')
new_code = cell("code", '''tl = time.time()
SC = L.scatter_sta("M-YQ0201-29", n_frames=40_000)
use = SC["qc"] & (SC["n_spikes"] >= 20)
print(f"scatter STA over 40,000 frames in {time.time() - tl:.0f} s: {SC['n_bins']} interstitial bins; {use.sum()} QC trigger cells with >= 20 spikes "
      f"(spikes per cell median {np.median(SC['n_spikes'][use]):.0f}); spike fluorescence median {np.median(SC['spike_f'][use]):.1f} counts, "
      f"{np.sum(SC['spike_f'][use] <= 0)} triggers with spike fluorescence <= 0")
M29, q29, QQ29, D29, sets29 = pair_sets("M-YQ0201-29")
spk = M29["spikelet_amplitude_normalized"]
edges_s = np.arange(0, 401, 40)
rows_s = []
for a, b in zip(edges_s[:-1], edges_s[1:]):
    s_ = (SC["dist"] >= a) & (SC["dist"] < b) & use[:, None]
    v = SC["amp"][s_]
    pr = QQ29 & (D29 >= a) & (D29 < b) & np.isfinite(spk)
    rows_s.append(dict(bin=f"{a}-{b}", scatter_n=len(v), scatter_mean=np.mean(v), scatter_median=np.median(v),
                       spikelet_pairs=int(pr.sum()), spikelet_mean=spk[pr].mean(), spikelet_median=np.median(spk[pr]),
                       connected_mean=spk[pr & M29["gap_junction_connection"]].mean()))
SCT = pd.DataFrame(rows_s)
SCT["ratio_mean"] = SCT.spikelet_mean / SCT.scatter_mean
SCT["ratio_median"] = SCT.spikelet_median / SCT.scatter_median
SCT["ratio_connected"] = SCT.connected_mean / SCT.scatter_mean
print(SCT.round(4).to_string())
b1, b3 = SCT.iloc[1], SCT.iloc[3]
print(f"from the 40-80 to the 120-160 um bin: scatter mean falls to {b3.scatter_mean / b1.scatter_mean:.2f} of its value "
      f"(median {b3.scatter_median / b1.scatter_median:.2f}), spikelet mean to {b3.spikelet_mean / b1.spikelet_mean:.2f} "
      f"(median {b3.spikelet_median / b1.spikelet_median:.2f}; connected {b3.connected_mean / b1.connected_mean:.2f})")
# split-half check of the scatter: triggers split by unit id parity
for par in (0, 1):
    s_ = (SC["dist"] >= 40) & (SC["dist"] < 80) & (use & (np.arange(len(use)) % 2 == par))[:, None]
    print(f"   triggers with {'even' if par == 0 else 'odd'} unit ids: 40-80 um scatter mean {SC['amp'][s_].mean():.4f}, median {np.median(SC['amp'][s_]):.4f}")
''', ["claim:spikelet-not-scatter"])
new_res = cell("markdown", "**Result: PENDING**")
for c in (new_md, new_code, new_res):
    c['id'] = uuid.uuid4().hex[:8]
nb['cells'][k:k] = [new_md, new_code, new_res]
save(nb, p)
EOF
grep -n '"behavior-rawexcerpt"' l1opto.py | head -3; $TMPDIR/venv/bin/python -c "
import sys; sys.path.insert(0,'.'); import l1opto as L; u=L.units('M-YQ0201-29','behavior-rawexcerpt'); print(u.keys())"
```

```
926:    f = open_file(mouse, "behavior-rawexcerpt")
931:    u = units(mouse, "behavior-rawexcerpt")
dict_keys(['id', 'spike_times', 'x_pixel', 'y_pixel', 'x_um', 'y_um', 'gfp_positive', 'passed_qc', 'edge_distance_pixels', 'tutorial_cell'])
```

**Agent calls Bash**

```bash
cd $TMPDIR/dev; cat > patch_sc.py <<'EOF'
_orig = L.scatter_sta
L.scatter_sta = lambda m, n_frames: _orig(m, n_frames=8000)
EOF
idx=$(python -c "
import json
nb=json.load(open('entries/001960-qi-2026/qi2026_excitability_connectivity.ipynb'))
print([i for i,c in enumerate(nb['cells']) if 'claim:spikelet-not-scatter' in c['metadata'].get('tags',[])][0])")
echo $idx; time $TMPDIR/venv/bin/python run_cells.py entries/001960-qi-2026/qi2026_excitability_connectivity.ipynb 1,3,25,patch:$TMPDIR/dev/patch_sc.py,$idx 2>&1 | grep -v "^sub-" | tail -22
```

```
39

60 to 400 um, per cell (n = 576 QC cells, 2 mice): outgoing 2.55 +/- 2.87, incoming 2.55 +/- 2.61, tested 24.8 +/- 8.5, probability 10.7 +/- 11.6% (0 cells with no tested partner)
   M-YQ0201-27: outgoing 2.77 +/- 2.95, tested 25.1, probability 11.6%
   M-YQ0201-29: outgoing 2.33 +/- 2.78, tested 24.6, probability 9.7%
######## cell 25 took 2 s
######## cell 39
scatter STA over 40,000 frames in 95 s: 5971 interstitial bins; 104 QC trigger cells with >= 20 spikes (spikes per cell median 58); spike fluorescence median -498.4 counts, 104 triggers with spike fluorescence <= 0
       bin  scatter_n  scatter_mean  scatter_median  spikelet_pairs  spikelet_mean  spikelet_median  connected_mean  ratio_mean  ratio_median  ratio_connected
0     0-40         71        0.0342          0.0383              32         0.1121           0.1009          0.1163      3.2762        2.6387           3.3993
1    40-80        786        0.0146          0.0118             240         0.0456           0.0396          0.0507      3.1220        3.3482           3.4744
2   80-120       1874        0.0045          0.0037             398         0.0211           0.0182          0.0253      4.6798        4.9662           5.6014
3  120-160       2764        0.0027          0.0029             618         0.0126           0.0116          0.0179      4.6782        4.0080           6.6422
4  160-200       3700        0.0018          0.0021             680         0.0080           0.0080          0.0137      4.3625        3.7966           7.4214
5  200-240       4476        0.0016          0.0018             806         0.0055           0.0054          0.0124      3.5786        3.0709           8.0164
6  240-280       5291        0.0021          0.0018             918         0.0042           0.0041          0.0112      2.0501        2.2540           5.4221
7  280-320       6226        0.0014          0.0010            1122         0.0032           0.0032          0.0112      2.3301        3.1483    
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py all entries/001960-qi-2026 2>&1 | grep -v MissingIDField | tail -15; date -u
```

```
Fri Nov  6 10:00:56 UTC 2026
Installed kernelspec registry-001960-qi-2026 in executed/001960-qi-2026/.venv/share/jupyter/kernels/registry-001960-qi-2026
0 error(s)
pass  qi2026_excitability_connectivity.ipynb  (2388 s)
pass  qi2026_spontaneous.ipynb  (1640 s)
pass  qi2026_excitability_spontaneous.ipynb  (801 s)

real	80m36.000s
user	88m55.327s
sys	2m8.369s
Fri Nov  6 11:21:32 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/001960-qi-2026; cat > $TMPDIR/dev/out.py <<'EOF'
import json, sys
nb = json.load(open(sys.argv[1]))
want = sys.argv[2].split(",")
for i, c in enumerate(nb["cells"]):
    tags = c.get("metadata", {}).get("tags", [])
    if c["cell_type"] == "code" and any(t.replace("claim:", "") in want for t in tags):
        print("=====", tags)
        for o in c.get("outputs", []):
            if "text" in o: print("".join(o["text"])[-4000:])
EOF
python $TMPDIR/dev/out.py qi2026_excitability_connectivity.ipynb two-mice-intrinsic-distributions,fig3lo-variance-components,spikelet-not-scatter,detection-limits,lasso-off-target-correction
```

```
===== ['claim:two-mice-intrinsic-distributions']
reading (a) all cells, membrane time constant of 0 as missing: n = 320 and 320
   adp_blue_norm                median   0.1113 vs   0.1135  n = 320, 320  p = 0.179
   optical_rheobase_norm        median   0.3463 vs   0.2903  n = 320, 320  p = 1.13e-05
   max_firing_rate_hz           median  30.8045 vs  30.1759  n = 320, 320  p = 0.197
   pulse_adaptation             median   0.2740 vs   0.2628  n = 320, 320  p = 0.24
   membrane_time_constant_ms    median  16.9067 vs  16.0315  n = 313, 320  p = 0.0313
   calls matching the paper: 5 of 5
reading (b) QC cells, membrane time constant of 0 as missing: n = 286 and 257
   adp_blue_norm                median   0.1114 vs   0.1098  n = 286, 257  p = 0.835
   optical_rheobase_norm        median   0.3419 vs   0.2862  n = 286, 257  p = 0.000103
   max_firing_rate_hz           median  30.6823 vs  31.4332  n = 286, 257  p = 0.932
   pulse_adaptation             median   0.2754 vs   0.2628  n = 286, 257  p = 0.477
   membrane_time_constant_ms    median  16.9212 vs  16.1094  n = 284, 257  p = 0.0333
   calls matching the paper: 5 of 5
reading (a) all cells, membrane time constant of 0 kept as a value: n = 320 and 320
   adp_blue_norm                median   0.1113 vs   0.1135  n = 320, 320  p = 0.179
   optical_rheobase_norm        median   0.3463 vs   0.2903  n = 320, 320  p = 1.13e-05
   max_firing_rate_hz           median  30.8045 vs  30.1759  n = 320, 320  p = 0.197
   pulse_adaptation             median   0.2740 vs   0.2628  n = 320, 320  p = 0.24
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/001960-qi-2026; python $TMPDIR/dev/out.py qi2026_spontaneous.ipynb traveling-waves,voltage-to-spike-sigmoid | head -60; python $TMPDIR/dev/out.py qi2026_spontaneous.ipynb spike-snr-and-detection-errors | tail -5; for nb in *.ipynb; do python -c "
import json; nb=json.load(open('$nb')); print('$nb', ''.join(nb['cells'][-1]['outputs'][0]['text']))"; done
```

```
===== ['claim:traveling-waves']
span reading 'extrema':
   M-YQ0201-27: threshold 0.0272 SH/frame; 1705 s quiet; 3254 derivative peaks, 2155 distinct spans (first 2000 s: 718 and 398); span 33 ms median (10 to 70); speeds from 2155 spans
      speed (a): mean 8.6 +/- 9.8 mm/s, median 7.9 (n = 2155)
      speed (b): mean 6091.7 +/- 28845.2 mm/s, median 921.6 (n = 1887)
      speed (c): mean 2797.5 +/- 4879.9 mm/s, median 1205.5 (n = 2155)
   M-YQ0201-29: threshold 0.0260 SH/frame; 1985 s quiet; 3655 derivative peaks, 2291 distinct spans (first 2000 s: 2548 and 1566); span 41 ms median (23 to 69); speeds from 2291 spans
      speed (a): mean 11.5 +/- 8.5 mm/s, median 10.5 (n = 2291)
      speed (b): mean 1693.4 +/- 18180.9 mm/s, median 505.1 (n = 2229)
      speed (c): mean 1123.9 +/- 2429.1 mm/s, median 608.4 (n = 2291)
   both mice: 6909 derivative peaks, 4446 distinct spans
      speed (a): mean 10.1 +/- 9.3 mm/s, median 9.5, 5 to 95 percentile -1.4 to 22.5 (n = 4446 of 4446)
      speed (b): mean 3709.8 +/- 23772.2 mm/s, median 632.3, 5 to 95 percentile 167.8 to 10518.2 (n = 4116 of 4446)
      speed (c): mean 1935.1 +/- 3908.9 mm/s, median 765.9, 5 to 95 percentile 173.5 to 6684.6 (n = 4446 of 4446)
      M-YQ0201-27 phase gradient direction (image frame, 0 = +x, 90 = +y): circular mean 79 deg, resultant length 0.13
      M-YQ0201-27 plane-wave fit direction (image frame, 0 = +x, 90 = +y): circular mean 65 deg, resultant length 0.10
      M-YQ0201-29 phase gradient direction (image frame, 0 = +x, 90 = +y): circular mean 94 deg, resultant length 0.16
      M-YQ0201-29 plane-wave fit direction (image frame, 0 = +x, 90 = +y): circular mean 41 deg, resultant length 0.17
span reading 'window':
   M-YQ0201-27: threshold 0.0272 SH/frame; 1705 s quiet; 2935 derivative peaks, 1777 distinct spans (first 2000 s: 627 and 355); span 189 ms median (48 to 394); speeds from 445 spans
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls questions | head -3; f=$(ls questions/*.yaml | head -1); head -30 $f; grep -n "verifications" -A30 attempts/*.yaml | grep -v 001960 | head -50; cat entries/001960-qi-2026/README.md | head -60
```

```
000005.yaml
000006.yaml
000008.yaml
dandiset: "000005"
paper: doi:10.1038/nn.4412
questions:
- claim: fs-vm-touch-whisking
  asked: 2026-10-20
  question: At what resolution is dVm/dt of the touch-aligned average Vm taken for the latency rule,
    the recording's own sampling rate (10 or 20 kHz) or the average in 1 ms bins as for the spike
    PSTH? The same question applies to the laser-onset latencies of exc-thalamus-photoinhibition and
    to exc-vm-touch-whisking.
  passage: Touch latency was identified as the latency from touch onset to the time when dVm/dt
    crossed baseline (3x s.d. of the dVm/dt between 0 and 25 ms before touch). All touch-spike PSTHs
    were constructed with a bin size of 1 ms. (Online Methods, Data analysis)
  why: At the full sampling rate two of the five whole-cell FS cells cross the threshold at 0.0 and
    0.3 ms and the mean latency is 1.88 ms (not reproduced); in 1 ms bins the mean over three cells
    is 3.67 to 4.17 ms (within 4.0 +- 0.4). For the thalamic and cortical light the full rate gives
    0.1 ms for both, the 1 ms bins 5.0 and 2.0 ms.
  answer: >-
[... 109 more lines not kept]
```

**Agent**

Now writing the EC conclusions.

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; python - <<'EOF'
import sys, os; sys.path.insert(0, os.environ['TMPDIR'] + '/dev')
from nbed import *
p = 'qi2026_excitability_connectivity.ipynb'
nb = load(p)
def setres(start, text):
    set_src(nb, find(nb, start), text)
setres('**Result: reproduced.** With the QC cells (reading (b)) all five calls match the paper:', '''**Result: reproduced, resting on an assumption.** With a membrane time constant of exactly 0 (7
cells of M-YQ0201-27) treated as a failed fit, both readings give the paper's five calls: rheobase
differs (p = 1.1e-5 all cells, 1.0e-4 QC cells), membrane time constant differs (p = 0.031 and
0.033, n = 313 and 284 against 320 and 257), and V_adp, maximum rate and adaptation do not (p = 0.18
to 0.93). Kept as values, the zeros give four of five calls under reading (a) (time constant
p = 0.101) and five under (b) (p = 0.048).''')
setres('**Result: partially reproduced.** IPSP amplitudes meet the reading', '''**Result: reproduced.** With the claims file's selection (QC pairs 60 to 400 um), IPSP amplitudes
have skewness 2.46 raw and 0.13 on the log scale (1,467 pairs) and spikelet amplitudes 3.15 and 0.41
(5,752 pairs; 0.43 and 0.49 per mouse), both inside the chosen reading. Pairs under 60 um carry the
lack of fit: with them, the spikelet log skewness is 0.70 (QC pairs within 400 um) and 0.73 (all
stored flags), outside it.''')
i = find(nb, '**Result: not reproduced.** The inhibition peaks 33.0 ms after pulse onset')
replace(nb, i, '''The population spikelet waveform
has a full width at half maximum of 22.7 ms, not about 2 ms,''', '''The population spikelet waveform
has a full width at half maximum of 22.7 ms with the far-lag baseline, and 4.94 ms with the
spikelet's own flanking frames as baseline, not about 2 ms either way,''')
setres('**Result: reproduced.** Log distance is chosen for both models', '''**Result: reproduced.** Log distance is chosen for both models (by 6.2 and 9.2 AIC units, the
tutorial's published values). For amplitude (1,467 pairs) the presynaptic variance is 0.1445 and the
postsynaptic 0.0579; no refit of 2,000 has postsynaptic at or above presynaptic, among the 1,963
converged refits, among all refits as fitted (the 37 non-converged have pre minus post 0.029 to
0.118), and with the non-converged refitted from the grid start. For decay (1,469 pairs; s0^2 =
0.661 and effective n 1,364, the tutorial's values) the postsynaptic variance is 0.1111 and the
presynaptic 0.0213; 1 of the 2,000 refits as fitted has presynaptic at or above postsynaptic
(0.05%), none of the 51 non-converged (pre minus post -0.144 to -0.047), and still 1 of 2,000 after
refitting them, under the 0.1% bound.''')
i = find(nb, '**Result: fig5e-inhibition-in-spontaneous-voltage reproduced.**')
replace(nb, i, '''The controls' own change from -20 to -5 ms to
15 to 30 ms is +0.012 (mean; median +0.003) for the top-quintile controls and +0.019 (median +0.007)
for all, outside 0.01 +/- 0.001; the criterion does not test this value.''', '''The controls' own change from -20 to -5 ms to
15 to 30 ms, measured on the spike-weighted control-average waveform as the paper's "STA waveform",
is +0.0097 for the controls of all connected pairs, within 0.01 +/- 0.001, and +0.0049 for those of
the top quintile; per control pair it is +0.012 (mean; median +0.003) and +0.019 (median +0.007).
The criterion does not test this value.''')
setres('**Result: reproduced.** Pooled z-scored features give 76.8% balanced accuracy', '''**Result: reproduced.** With the z-scoring fitted on the training cells of each split, pooled
features give 76.8% balanced accuracy (2.5 to 97.5 percentiles 69.3 to 83.9% over 10,000 splits)
against 50.0% for shuffled labels, within 4 and 5 points of 78% and 50%. After-depolarization has
the largest coefficient (-1.33) and the largest drop when left out (5.5 points). The intervals
printed are wider than the paper's.''')
i = find(nb, '**Result: npy-connection-probability reproduced.**')
s = get(nb, i)
s = s[:s.index('npy-ipsp-duration reproduced.')] + '''npy-ipsp-duration reproduced, resting on an assumption. With the fits that end on the code's 0.4 s
bound left out (91 of 1,469 in the QC pairs 60 to 400 um), decay time constants in NPY+ postsynaptic
cells average 57.1 +/- 62.6 ms (715 pairs) and in NPY- cells 41.9 +/- 53.4 ms (663), against the
paper's 58 +/- 63 (699) and 43 +/- 54 (646); rank-sum p = 1.8e-16. QC pairs within 400 um give 57.4 and
41.9 ms (731 and 672 pairs), also within tolerance. With the fits at the bound kept, the means are
77.4 and 65.2 ms (760 and 709 pairs, inside tolerance) in the 60 to 400 um band and 80.5 and 67.2 ms
(784 and 723 pairs) within 400 um, where the NPY- count is outside 646 +/- 65.
'''
set_src(nb, i, s)
# detection limits result and scatter, lasso
i = find(nb, '# Everything stored in the pairwise table')
nb['cells'].insert(i + 1, cell("markdown", '''**Result: blocked (too large).** The pairwise table holds no per-pair statistic, p-value or null.
One fit of the IPSP model takes 48 ms here, so the null statistics of the 14,576 tested pairs
(10,000 draws each) would take about 1,950 hours, and the pairs "near detection cutoff" cannot be
picked without them.'''))
nb['cells'][-1]['id'] = 'x'
import uuid
for c in nb['cells']:
    if c.get('id') in (None, 'x'): c['id'] = uuid.uuid4().hex[:8]
i = find(nb, 'tl = time.time()\nSC = L.scatter_sta')
set_src(nb, i + 1, '''**Result: reproduced, on a subset of the movie.** Over the first 40,000 frames of the excerpt (189
QC trigger cells, 107 spikes each in median), the normalized scatter in the 40 to 80 um bin is
0.0150 (mean; median 0.0126; 0.0148 and 0.0153 for the two halves of the triggers) against a mean
spikelet of 0.0456 over QC pairs of the same mouse, a ratio of 3.03 (median 3.14; connected pairs
3.37), above 2.25. From the 40 to 80 um bin to the 120 to 160 um bin the scatter falls to 0.23 of
its value and the spikelet to 0.28, so the scatter falls faster, as the criterion requires. The
test covers 3.5% of one mouse's excerpt, the only movie deposited.''')
i = find(nb, 'tl = time.time()\nLASSO = {}')
set_src(nb, i + 1, '''**Result: not reproduced, resting on assumptions.** The rebuilt raw matrix measures the stored
IPSPs (R = 0.64 with the stored amplitudes over the 1,755 flagged pairs, 0.81 over those 60 to
400 um). Under reading (a) the corrected matrix correlates with the raw at R = 0.937 (0.912 for 60
to 400 um), above 0.82 +/- 0.082, and 71.9% of the pairs differ by more than 20% (19% are set to
zero), not under 22%. Under reading (b) the penalty sets 99.9% of the coefficients to zero (R =
0.05). Without a penalty the correction still moves 37% of the pairs by more than 20% (R = 0.970).
The per-pulse response window and the treatment of off-target spikes are assumptions (the paper
gives neither), so the numbers rest on them.'''))
save(nb, p)
EOF
echo ok
```

```
File "<stdin>", line 82
    gives neither), so the numbers rest on them.'''))
                                                    ^
SyntaxError: unmatched ')'
ok
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; fc -ln 2>/dev/null | true; echo skip
```

```
skip
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; cat > $TMPDIR/dev/concl_ec.py <<'PYEOF'
import sys, os, uuid; sys.path.insert(0, os.environ['TMPDIR'] + '/dev')
from nbed import *
p = 'qi2026_excitability_connectivity.ipynb'
nb = load(p)
def setres(start, text):
    set_src(nb, find(nb, start), text)
setres('**Result: reproduced.** With the QC cells (reading (b)) all five calls match the paper:', '''**Result: reproduced, resting on an assumption.** With a membrane time constant of exactly 0 (7
cells of M-YQ0201-27) treated as a failed fit, both readings give the paper's five calls: rheobase
differs (p = 1.1e-5 all cells, 1.0e-4 QC cells), membrane time constant differs (p = 0.031 and
0.033, n = 313 and 284 against 320 and 257), and V_adp, maximum rate and adaptation do not (p = 0.18
to 0.93). Kept as values, the zeros give four of five calls under reading (a) (time constant
p = 0.101) and five under (b) (p = 0.048).''')
setres('**Result: partially reproduced.** IPSP amplitudes meet the reading', '''**Result: reproduced.** With the claims file's selection (QC pairs 60 to 400 um), IPSP amplitudes
have skewness 2.46 raw and 0.13 on the log scale (1,467 pairs) and spikelet amplitudes 3.15 and 0.41
(5,752 pairs; 0.43 and 0.49 per mouse), both inside the chosen reading. Pairs under 60 um carry the
lack of fit: with them, the spikelet log skewness is 0.70 (QC pairs within 400 um) and 0.73 (all
stored flags), outside it.''')
i = find(nb, '**Result: not reproduced.** The inhibition peaks 33.0 ms after pulse onset')
replace(nb, i, '''The population spikelet waveform
has a full width at half maximum of 22.7 ms, not about 2 ms,''', '''The population spikelet waveform
has a full width at half maximum of 22.7 ms with the far-lag baseline, and 4.94 ms with the
spikelet's own flanking frames as baseline, not about 2 ms either way,''')
setres('**Result: reproduced.** Log distance is chosen for both models', '''**Result: reproduced.** Log distance is chosen for both models (by 6.2 and 9.2 AIC units, the
tutorial's published values). For amplitude (1,467 pairs) the presynaptic variance is 0.1445 and the
postsynaptic 0.0579; no refit of 2,000 has postsynaptic at or above presynaptic, among the 1,963
converged refits, among all refits as fitted (the 37 non-converged have pre minus post 0.029 to
0.118), and with the non-converged refitted from the grid start. For decay (1,469 pairs; s0^2 =
0.661 and effective n 1,364, the tutorial's values) the postsynaptic variance is 0.1111 and the
presynaptic 0.0213; 1 of the 2,000 refits as fitted has presynaptic at or above postsynaptic
(0.05%), none of the 51 non-converged (pre minus post -0.144 to -0.047), and still 1 of 2,000 after
refitting them, under the 0.1% bound.''')
i = find(nb, '**Result: fig5e-inhibition-in-spontaneous-voltage reproduced.**')
replace(nb, i, '''The controls' own change from -20 to -5 ms to
15 to 30 ms is +0.012 (mean; median +0.003) for the top-quintile controls and +0.019 (median +0.007)
for all, outside 0.01 +/- 0.001; the criterion does not test this value.''', '''The controls' own change from -20 to -5 ms to
15 to 30 ms, measured on the spike-weighted control-average waveform as the paper's "STA waveform",
is +0.0097 for the controls of all connected pairs, within 0.01 +/- 0.001, and +0.0049 for those of
the top quintile; per control pair it is +0.012 (mean; median +0.003) and +0.019 (median +0.007).
The criterion does not test this value.''')
setres('**Result: reproduced.** Pooled z-scored features give 76.8% balanced accuracy', '''**Result: reproduced.** With the z-scoring fitted on the training cells of each split, pooled
features give 76.8% balanced accuracy (2.5 to 97.5 percentiles 69.3 to 83.9% over 10,000 splits)
against 50.0% for shuffled labels, within 4 and 5 points of 78% and 50%. After-depolarization has
the largest coefficient (-1.33) and the largest drop when left out (5.5 points). The intervals
printed are wider than the paper's.''')
i = find(nb, '**Result: npy-connection-probability reproduced.**')
s = get(nb, i)
s = s[:s.index('npy-ipsp-duration reproduced.')] + '''npy-ipsp-duration reproduced, resting on an assumption. With the fits that end on the code's 0.4 s
bound left out (91 of 1,469 in the QC pairs 60 to 400 um), decay time constants in NPY+ postsynaptic
cells average 57.1 +/- 62.6 ms (715 pairs) and in NPY- cells 41.9 +/- 53.4 ms (663), against the
paper's 58 +/- 63 (699) and 43 +/- 54 (646); rank-sum p = 1.8e-16. QC pairs within 400 um give 57.4 and
41.9 ms (731 and 672 pairs), also within tolerance. With the fits at the bound kept, the means are
77.4 and 65.2 ms (760 and 709 pairs, inside tolerance) in the 60 to 400 um band and 80.5 and 67.2 ms
(784 and 723 pairs) within 400 um, where the NPY- count is outside 646 +/- 65.
'''
set_src(nb, i, s)
i = find(nb, '# Everything stored in the pairwise table')
nb['cells'].insert(i + 1, cell("markdown", '''**Result: blocked (too large).** The pairwise table holds no per-pair statistic, p-value or null.
One fit of the IPSP model takes 48 ms here, so the null statistics of the 14,576 tested pairs
(10,000 draws each) would take about 1,950 hours, and the pairs "near detection cutoff" cannot be
picked without them.'''))
i = find(nb, 'tl = time.time()\nSC = L.scatter_sta')
set_src(nb, i + 1, '''**Result: reproduced, on a subset of the movie.** Over the first 40,000 frames of the excerpt (189
QC trigger cells, 107 spikes each in median), the normalized scatter in the 40 to 80 um bin is
0.0150 (mean; median 0.0126; 0.0148 and 0.0153 for the two halves of the triggers) against a mean
spikelet of 0.0456 over QC pairs of the same mouse, a ratio of 3.03 (median 3.14; connected pairs
3.37), above 2.25. From the 40 to 80 um bin to the 120 to 160 um bin the scatter falls to 0.23 of
its value and the spikelet to 0.28, so the scatter falls faster, as the criterion requires. The
test covers 3.5% of one mouse's excerpt, the only movie deposited.''')
i = find(nb, 'tl = time.time()\nLASSO = {}')
set_src(nb, i + 1, '''**Result: not reproduced, resting on assumptions.** The rebuilt raw matrix measures the stored
IPSPs (R = 0.64 with the stored amplitudes over the 1,755 flagged pairs, 0.81 over those 60 to
400 um). Under reading (a) the corrected matrix correlates with the raw at R = 0.937 (0.912 for 60
to 400 um), above 0.82 +/- 0.082, and 71.9% of the pairs differ by more than 20% (19% are set to
zero), not under 22%. Under reading (b) the penalty sets 99.9% of the coefficients to zero (R =
0.05). Without a penalty the correction still moves 37% of the pairs by more than 20% (R = 0.970).
The per-pulse response window and the treatment of off-target spikes are assumptions (the paper
gives neither), so the numbers rest on them.''')
setres('**Result: reproduced.** The median IPSP of connected pairs is -0.0297 SH pooled', '''**Result: partially reproduced.** The median IPSP of connected pairs is -0.0297 SH pooled (-0.0303
and -0.0292 per mouse), within 0.0028 of -0.028. The cross-STA depolarization, the claims file's
reading for the 20%, is computed per mouse and averaged, as the criterion says: 0.217 (M-YQ0201-27)
and 0.250 SH (M-YQ0201-29), mean 0.234, outside 0.20 +/- 0.02; one mouse alone is inside.''')
for c in nb['cells']:
    if 'id' not in c: c['id'] = uuid.uuid4().hex[:8]
save(nb, p)
PYEOF
python $TMPDIR/dev/concl_ec.py && python -c "
import json
nb=json.load(open('qi2026_excitability_connectivity.ipynb'))
for c in nb['cells']:
    s=''.join(c['source'])
    if 'ipsp-median-amplitude' in s[:40] or s.startswith('**Result: partially reproduced.** The median'): print(s[:600]); print('--')
" | head -30
```

```
### ipsp-median-amplitude
> The median unitary IPSP among connected pairs was -2.8% of a spike height per presynaptic spike,
> while correlated spontaneous fluctuations were about 20% of a spike height.

IPSP amplitude: stored `ipsp_amplitude_norm_per_presynaptic_spike` (stored positive; sign flipped)
of pairs with `synaptic_connection` set. Fluctuations: the reading chosen in the claims file, the
code's cross-STA depolarization (reproduce_figure4_from_nwb.m STATS: range of each pair's quiet
spike-triggered voltage over lags -100 to -2 frames, mean over pairs 60 to 400 um apart), from the
stor
--
**Result: partially reproduced.** The median IPSP of connected pairs is -0.0297 SH pooled (-0.0303
and -0.0292 per mouse), within 0.0028 of -0.028. The cross-STA depolarization, the claims file's
reading for the 20%, is computed per mouse and averaged, as the criterion says: 0.217 (M-YQ0201-27)
and 0.250 SH (M-YQ0201-29), mean 0.234, outside 0.20 +/- 0.02; one mouse alone is inside.
--
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; cat > $TMPDIR/dev/concl_ec2.py <<'PYEOF'
import sys, os; sys.path.insert(0, os.environ['TMPDIR'] + '/dev')
from nbed import *
p = 'qi2026_excitability_connectivity.ipynb'
nb = load(p)
i = find(nb, '## Summary')
s = get(nb, i)
for a, b in [("| two-mice-intrinsic-distributions | reproduced |", "| two-mice-intrinsic-distributions | reproduced (assumption) |"),
             ("| ipsp-median-amplitude | reproduced |", "| ipsp-median-amplitude | partially reproduced |"),
             ("| amplitudes-log-normal | partially reproduced |", "| amplitudes-log-normal | reproduced |"),
             ("| npy-ipsp-duration | reproduced |", "| npy-ipsp-duration | reproduced (assumption) |"),
             ("| hadamard-stimulation-rates | reproduced |", "| hadamard-stimulation-rates | reproduced (assumption) |"),
             ("| spikelet-not-scatter | blocked: too large |\n| detection-limits, lasso-off-target-correction | blocked: methods underspecified |",
              "| spikelet-not-scatter | reproduced (subset of the movie) |\n| lasso-off-target-correction | not reproduced (assumption) |\n| detection-limits | blocked: too large |")]:
    assert a in s, a
    s = s.replace(a, b)
old = '''does not re-run the paper's detection and fitting.'''
assert old in s
s = s.replace(old, '''does not re-run the paper's detection and fitting, except where a claim needs what is not
stored: the lasso correction rebuilds per-pulse responses and evoked spikes from the voltage and
the stimulation (with an assumed response window), and the scatter control reads the first 40,000
frames of the raw-movie excerpt.''')
set_src(nb, i, s)
save(nb, p)
PYEOF
python $TMPDIR/dev/concl_ec2.py; python -c "
import json
nb=json.load(open('qi2026_spontaneous.ipynb'))
for c in nb['cells']:
    s=''.join(c['source'])
    if s.startswith('**Result') and any(k in s for k in ['single-spike SNR','At the peak frame','With V at the spike frame']) or s.startswith('## Summary'): print(s); print('--')
"
```

```
**Result: not reproduced.** The single-spike SNR of the stored normalized voltage is 3.33 (mean over
the 505 QC cells of the behavior sessions; 3.18 over all 640 cells), and 3.0 to 3.9 per mouse and
session under every reading, below 4.5 +/- 0.7. Measured with the spike heights found in the data
(median 0.88 to 0.96 SH) it is lower (2.8 to 3.0). The false-discovery and false-negative rates were
not tested: no matched-filter output is stored.
--
**Result: reproduced, resting on an assumption.** With V at the spike frame (the code, whose
Figure 4 script records that the author confirmed this computation) the logistic explains at least
90% of the variance for 262 of 505 cells (52%; 133 of 247 and 129 of 258), and their midpoints
(CV 0.82) and maxima (CV 4.54) vary across cells. With V 10 ms before the spike (the Methods'
wording) only 121 cells (24%) pass, so the outcome rests on the code's reading.
--
**Result: reproduced, resting on an assumption.** At the peak frame (reading (b), assumed since
the claim compares the subtypes at the peaks) NPY- cells fire at a median 1.10 Hz and NPY+ cells at
0.74 Hz (p = 7.5e-6), while the voltages do not differ (p = 0.22). Over +/-300 frames (reading (a))
the rate difference holds (p = 1.5e-4) but the voltages differ at p = 0.022.
--
## Summary

| Claim | Outcome |
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; cat > $TMPDIR/dev/concl_sp.py <<'PYEOF'
import sys, os; sys.path.insert(0, os.environ['TMPDIR'] + '/dev')
from nbed import *
p = 'qi2026_spontaneous.ipynb'
nb = load(p)
i = find(nb, '**Result: not reproduced.** The single-spike SNR')
replace(nb, i, '''not tested: no matched-filter output is stored.''', '''not tested: no matched-filter output or fitted mixture is stored, in the session files or in the
raw-movie excerpt, whose datasets (listed above) are the movie, fluorescence traces, footprints,
motion traces, a pixel subset and spike times.''')
i = find(nb, '**Result: reproduced, resting on an assumption.** With V at the spike frame')
set_src(nb, i, '''**Result: reproduced, resting on an assumption.** With V at the spike frame (the code, and the
Methods' V(t_s)) the logistic explains at least 90% of the variance for 262 of 505 cells (52%; 133 of
247 and 129 of 258), and their midpoints (CV 0.82) and maxima (CV 4.56) vary across cells. The
fitted maxima are partly unconstrained extrapolations, but the spread holds without them: the
largest observed rate has CV 0.59, and the 221 fits whose top lies within twice that rate have
top CV 0.64 and midpoint CV 0.29. With V the mean over the 10 ms before (the Results' and the
legend's interval) 214 cells (42%) pass, and with the single sample 10 ms before 121 (24%), so the
outcome rests on the Methods' and the code's reading, and the pass is narrow (262 of 505).''')
i = find(nb, '**Result: reproduced, resting on an assumption.** At the peak frame')
set_src(nb, i, '''**Result: blocked (methods underspecified).** The criterion's two readings give different
outcomes, and the claims file blocks such a claim. At the peak frame (reading (b)) NPY- cells fire
at a median 1.10 Hz and NPY+ cells at 0.74 Hz (p = 7.5e-6), while the voltages do not differ
(p = 0.22), as the claim says. Over +/-300 frames (reading (a)) the rate difference holds
(p = 1.5e-4) but the voltages differ at p = 0.022.''')
i = find(nb, '**Result: PENDING**')
set_src(nb, i, '''**Result: not reproduced, resting on assumptions.** No reading gives both the count and the speed.
With the span between the adjacent turning points, the 4,446 distinct spans (6,909 derivative peaks)
are outside 3,858 +/- 386, and the mean speed under reading (a) is 10.1 +/- 9.3 mm/s (8.6 and 11.5 per
mouse), just inside 18.2 +/- 8.3. With the span between the extremes within 250 ms, the 3,775 spans
are inside the tolerance (6,198 peaks are not), but the speed under (a) is 6.2 +/- 7.8 mm/s,
outside it. Reading (b) and the plane-wave variant give hundreds to thousands of mm/s in every
case (medians 70 to 920 mm/s), since most pairs peak at near-zero lag within these short spans.
The directions are broad (resultant lengths 0.09 to 0.17), and the files do not orient the image
axes on the brain, so the medial-posterior bias could not be tested. The span, the counting and
the analysed frames are the Methods' open details, run as readings.''')
i = find(nb, '## Summary')
s = get(nb, i)
for a, b in [("| traveling-waves | blocked: methods underspecified |", "| traveling-waves | not reproduced (assumptions) |"),
             ("| voltage-to-spike-sigmoid | reproduced |", "| voltage-to-spike-sigmoid | reproduced (assumption) |"),
             ("| npy-oscillation-peak-rates | reproduced |", "| npy-oscillation-peak-rates | blocked: methods underspecified |")]:
    assert a in s, a
    s = s.replace(a, b)
old = "the detection error rates are not\ncomputed."
assert old in s
s = s.replace(old, '''the detection error rates are not
computed. The wave analysis has no code; its open details are run as readings.''')
old = "the chosen whisking reconstructions 14 and 9)."
assert old in s
s = s.replace(old, old + ''' The x and y axes of the cell positions are not oriented on the brain
in the files, so directions can be given only in the image frame.''')
set_src(nb, i, s)
save(nb, p)
PYEOF
python $TMPDIR/dev/concl_sp.py && echo ok; date -u
```

```
ok
Fri Nov  6 11:23:38 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
for nbn in ("qi2026_excitability_connectivity.ipynb", "qi2026_spontaneous.ipynb"):
    src = json.load(open(f"entries/001960-qi-2026/{nbn}"))
    ex = json.load(open(f"executed/001960-qi-2026/{nbn}"))
    exc = [c for c in ex["cells"] if c["cell_type"] == "code"]
    sc = [c for c in src["cells"] if c["cell_type"] == "code"]
    assert len(exc) == len(sc)
    for a, b in zip(sc, exc):
        assert "".join(a["source"]) == "".join(b["source"]), "code differs"
    k = iter(exc)
    ex["cells"] = [next(k) if c["cell_type"] == "code" else c for c in src["cells"]]
    json.dump(ex, open(f"executed/001960-qi-2026/{nbn}", "w"), indent=1, ensure_ascii=False)
    print(nbn, "ok")
EOF
```

```
qi2026_excitability_connectivity.ipynb ok
qi2026_spontaneous.ipynb ok
```

**Agent calls Bash**

```bash
cd  ls schemas; python -c "
import json,glob
s=json.load(open([f for f in glob.glob('schemas/*') if 'attempt' in f][0]))
v=s['properties']['verifications']
print(json.dumps(v,indent=0)[:3000])
" ; python -c "
import json,glob
s=json.load(open([f for f in glob.glob('schemas/*') if 'attempt' in f][0]))
print(json.dumps(s.get('\$defs',s.get('definitions',{})).get('proposed',''),indent=0)[:1500])
print(list(s.get('\$defs',{}).keys()))"
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
{
"type": "array",
"items": {
"type": "object",
"additionalProperties": false,
"required": [
"date",
"kind",
"by",
"results"
],
"properties": {
"date": {
"type": "string",
"format": "date"
},
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dev/rec.py <<'PYEOF'
import yaml
p = "attempts/001960-qi-2026-01.yaml"
R = yaml.safe_load(open(p))
O = {o["claim"]: o for o in R["outcomes"]}
orig = {k: v["outcome"] for k, v in O.items()}
EC, SP = "qi2026_excitability_connectivity.ipynb", "qi2026_spontaneous.ipynb"
def put(cid, **kw):
    o = O[cid]
    for k in ("blocked_by", "assumed", "measured", "notebook", "output", "proposed"):
        if k in kw and kw[k] is None:
            o.pop(k, None); kw.pop(k)
    o.update(kw)
    order = ["claim", "outcome", "blocked_by", "notebook", "output", "assumed", "measured", "notes", "deviations"]
    O[cid] = {k: o[k] for k in order if k in o} | {k: v for k, v in o.items() if k not in order}

put("two-mice-intrinsic-distributions", outcome="reproduced", assumed=True,
    notes="With the 7 membrane time constants of exactly 0 in M-YQ0201-27 treated as failed fits, both readings give the paper's five calls: rheobase p = 1.1e-5 (all cells) and 1.0e-4 (QC cells), membrane time constant p = 0.031 and 0.033 (313 and 284 cells against 320 and 257), V_adp, maximum rate and adaptation p = 0.18 to 0.93. Kept as values, the zeros give four of five calls under reading (a) (time constant p = 0.101) and five under reading (b) (p = 0.048).",
    deviations=["Assumed is that a membrane time constant of exactly 0 is a failed fit, so it is left out: no fitted exponential decay has a time constant of 0, and the file flags none of them (findings). Both treatments are shown."])
put("ipsp-median-amplitude", outcome="partially_reproduced", measured=[-0.0297, 0.234],
    notes="The pooled median IPSP of connected pairs is -0.0297 SH (-0.0303 and -0.0292 per mouse), within 0.0028 of -0.028. The cross-STA depolarization, the claims file's reading for the 20%, is computed per mouse and averaged as its criterion says, 0.217 (M-YQ0201-27) and 0.250 SH (M-YQ0201-29), mean 0.234, outside 0.20 +/- 0.02; the per-mouse clause of the criterion applies to the IPSP median.")
put("detection-limits", outcome="blocked", blocked_by="too_large", notebook=EC, output="claim:detection-limits",
    notes="The pairwise table holds only the calls, amplitudes, decays, distances and Hadamard spike times (its full listing is in the notebook), no per-pair statistic, p-value or null distribution. Rebuilding the paper's statistic (the residual sums of squares of the IPSP model with and without its double exponential) for 10,000 null draws per tested pair takes about 1,950 hours at the 48 ms per fit measured in the notebook (14,576 tested pairs), and the 100 pairs per mouse near the cutoff cannot be picked without every pair's p-value. The claims file's readings of the 50% point were therefore not run.")
put("spikelet-not-scatter", outcome="reproduced", blocked_by=None, notebook=EC, output="claim:spikelet-not-scatter", measured=3.03,
    notes="On the first 40,000 frames of the raw-movie excerpt (M-YQ0201-29; 189 QC trigger cells with at least 20 spikes, 107 in median), the normalized scatter of interstitial pixels in the 40 to 80 um bin is 0.0150 (mean; median 0.0126; 0.0148 and 0.0153 for two halves of the triggers) and the mean spikelet of the same mouse's QC pairs 0.0456, a ratio of 3.03 (median 3.14; connected pairs only 3.37), above 2.25. From the 40 to 80 um bin to the 120 to 160 um bin the scatter falls to 0.23 of its value and the spikelet to 0.28.",
    deviations=["A subset: 40,000 of the excerpt's 1,152,000 frames (51 s), since reading the whole movie at the measured rate of about 110 frames per second would take about 3 hours.",
                "Pixels are averaged in 4 x 4 bins (26 um), and interstitial bins are those holding no pixel of any footprint (a computational choice; Supplementary Fig. 17A excludes regions containing cells).",
                "The spikelets compared are the stored spikelet amplitudes of the M-YQ0201-29 connectivity session over all QC pairs, the only spikelets stored; the scatter comes from that mouse's spontaneous session."])
put("lasso-off-target-correction", outcome="not_reproduced", blocked_by=None, notebook=EC, output="claim:lasso-off-target-correction", assumed=True, measured=[0.937, 71.9],
    notes="Rebuilt from the 14,400 pulses of each sparsePulseHad session (each cell targeted 243 to 480 times, the paper's range). The rebuilt raw matrix correlates with the stored amplitudes at R = 0.64 over the 1,755 stored synaptic flags (955 + 800, the paper's n) and 0.81 over those 60 to 400 um. Under reading (a) the corrected matrix correlates with the raw at R = 0.937 (0.912 for 60 to 400 um), above 0.82 +/- 0.082, and 71.9% of the pairs differ by more than 20% (18.9% set to zero), not under 22%. Under reading (b) 99.9% of coefficients are zero (R = 0.05). Least squares without a penalty still moves 37% of pairs by more than 20% (R = 0.970).",
    deviations=["The per-pulse response is the mean normalized voltage 20 to 60 ms after pulse onset minus the 25 ms before (assumed; the paper gives no per-trial measure, and its fitted IPSP model is not run per pulse).",
                "Spikes of a targeted cell are its stored estimated_spikes_per_blue_pulse (Methods); spikes of a non-targeted cell are its detected evoked spikes when it lies within 100 um of a target and zero elsewhere (assumed, from the 25 um off-target firing length constant of the Results).",
                "The lasso is fitted per postsynaptic cell over pulses not targeting it, with an intercept for the blue-flash response, with scikit-learn's LassoCV (10 folds, 40 penalties, unstandardized predictors); the paper's software and settings are not given.",
                "The 1755 pairs are taken to be the stored synaptic flags of both mice (955 and 800), which number 1755; the claims file says their choice is not given (questions)."])
put("amplitudes-log-normal", outcome="reproduced",
    notes="With the claims file's shared selection (QC cells, pairs under 60 um left out of gap-junction analyses), QC pairs 60 to 400 um: IPSP skewness 2.46 raw and 0.13 log (1,467 pairs), spikelet 3.15 raw and 0.41 log (5,752 pairs; 0.43 and 0.49 per mouse), both inside the chosen reading. With pairs under 60 um the spikelet log skewness is 0.70 (QC within 400 um) and 0.73 (all stored flags), outside it.",
    deviations=["The paper shows a Gaussian fit to log histograms with no test; the skewness bounds are the claims file's reading."])
O["interaction-kernel"]["notes"] = O["interaction-kernel"]["notes"].replace("has a FWHM of 22.7 ms, not about 2 ms,", "has a FWHM of 22.7 ms with the far-lag baseline and 4.94 ms with the spikelet's flanking frames (-4 to -2, 4 to 6) as baseline, not about 2 ms either way,")
O["interaction-kernel"]["deviations"] = ["The paper gives no method for Supplementary Movie 3; every measure is the claims file's reading. The FWHM is measured on the population Hadamard cross-spike STA with the median of lags beyond +/-40 frames as baseline (a standard choice), and with the mean of the spikelet's flanking frames as a variant."]
put("fig3lo-variance-components",
    notes="Log distance is chosen by 6.2 (amplitude) and 9.2 (decay) AIC units, and the decay weights give s0^2 = 0.661 and effective n 1,364, as the tutorial reports. Amplitude (1,467 pairs): presynaptic variance 0.1445 against postsynaptic 0.0579; no refit of 2,000 has postsynaptic at or above presynaptic, whether over the 1,963 converged, over all as fitted, or with the 37 non-converged refitted from the grid start. Decay (1,469 pairs): postsynaptic 0.1111 against presynaptic 0.0213; 1 of the 2,000 refits as fitted has presynaptic at or above postsynaptic (0.05%), none of the 51 non-converged, and 1 of 2,000 after refitting them, under 0.1%.")
put("traveling-waves", outcome="not_reproduced", blocked_by=None, notebook=SP, output="claim:traveling-waves", assumed=True, measured=[10.1, 4446],
    notes="No reading gives both the count and the speed. With each event spanning the adjacent turning points of the population average, the 4,446 distinct spans (6,909 derivative peaks) are outside 3,858 +/- 386, and the mean speed under reading (a) is 10.1 +/- 9.3 mm/s (8.6 and 11.5 per mouse), just inside 18.2 +/- 8.3. With the span between the extremes within 250 ms, 3,775 spans are inside the tolerance but the speed under (a) is 6.2 +/- 7.8 mm/s, outside. Reading (b) and a plane-wave variant give medians of 70 to 920 mm/s. Directions are broad (resultant lengths 0.09 to 0.17), and the image axes are not oriented on the brain in the files, so the medial-posterior bias was not tested. Measured values are the first span reading under (a).",
    deviations=["The Methods leave open the derivative's smoothing, the window of the flanking minimum and maximum, how peaks are counted and the lag range; run as readings (derivative of the stored, already smoothed subthreshold average; spans between adjacent turning points or the extremes within 250 ms; counts per derivative peak and per distinct span; all lags a span allows). For the 250 ms spans every fourth span gives a speed (run time).",
                "Quiet and whisking frames are the stored masks without running and outside +/-1000 frames of a chunk edge (the code's Figure 4 masks), over the whole session; the first 2000 s are shown for the counts.",
                "The 325 um Gaussian of the phase map is read as its full width at half maximum (assumed)."])
put("voltage-to-spike-sigmoid",
    notes="With V at the spike frame (the code and the Methods' V(t_s)) a four-parameter logistic explains at least 90% of the variance for 262 of 505 cells (52%), with CV 0.82 of the midpoints and 4.56 of the fitted maxima. The largest observed rate has CV 0.59, and the 221 fits whose top lies within twice it have top CV 0.64 and midpoint CV 0.29. With V the mean of the 10 ms before (the Results' and legend's interval) 214 cells (42%) pass, with the single sample 10 ms before 121 (24%).",
    deviations=["The readings give different outcomes. Assumed is V at the spike frame, which is what the Methods' V(t_s) and the code compute (the code's Figure 4 script records that the author confirmed this computation and kept the legend's wording); the Results and the Figure 4E legend speak of a 10 ms interval, run as the mean of the 8 frames (10.2 ms) before and as the sample 8 frames before. The claims file attributes the 10 ms to the Methods (questions)."])
O["fig5e-inhibition-in-spontaneous-voltage"]["notes"] = "Under reading (a) the top quintile (294 pairs) gives -0.0189 SH and all 1,467 connected pairs -0.0095 SH; (b) -0.0188 and -0.0099; (c) -0.0213 and -0.0095. Rank-sum p = 2.4e-31 and 6.4e-39 one-sided against the controls. The controls' own change, measured on the spike-weighted control-average waveform, is +0.0097 for the controls of all connected pairs (within 0.01 +/- 0.001) and +0.0049 for those of the top quintile; per control pair the means are +0.012 and +0.019 (medians 0.003 and 0.007). The criterion tests the two pair values only."
O["npy-classifier"]["deviations"] = ["Stratified splits and scikit-learn's default L2 penalty are standard choices the Methods do not fix; z-scoring is fitted on the training cells of each split. The printed intervals are wider than the paper's."]
put("npy-ipsp-duration", assumed=True, measured=[57.1, 41.9, 715, 663],
    notes="With the 91 fits that end on the code's 0.4 s bound left out, decay of connected QC pairs 60 to 400 um is 57.1 +/- 62.6 ms in NPY+ postsynaptic cells (715 pairs) and 41.9 +/- 53.4 ms in NPY- (663), p = 1.8e-16, against 58 +/- 63 (699) and 43 +/- 54 (646). QC pairs within 400 um give 57.4 and 41.9 ms (731 and 672). With the fits at the bound kept, the 60 to 400 um band gives 77.4 and 65.2 ms (760 and 709, inside tolerance) and the within-400 um selection 80.5 and 67.2 ms (784 and 723), where the NPY- count is outside 646 +/- 65.",
    deviations=["The decay is taken in seconds; the file gives no unit, and the code's fit bounds (0.006 to 0.4) are in seconds.",
                "Assumed is that a decay on the 0.4 s bound is a fit that found no decay and is left out; the selections differ in outcome only when such fits are kept and pairs under 60 um are included. Leaving them out gives the paper's means and s.d. within 1 ms."])
put("npy-oscillation-peak-rates", outcome="blocked", blocked_by="methods_underspecified", assumed=None,
    notes="The criterion's readings give different outcomes, and the claims file blocks such a claim. At the peak frame (reading (b)) NPY- cells fire at 1.10 Hz and NPY+ at 0.74 Hz (medians, p = 7.5e-6) and the voltages do not differ (p = 0.22). Over +/-300 frames (reading (a)) the rate difference holds (p = 1.5e-4) but the voltages differ (p = 0.022). 4,279 and 5,886 peaks (code 5,888 for M-YQ0201-29).",
    deviations=["Which value of the peak-triggered average is a cell's value is not stated; asked of the authors (findings)."])
O["spike-snr-and-detection-errors"]["notes"] = O["spike-snr-and-detection-errors"]["notes"].replace("since no matched-filter output or fitted mixture is stored;", "since no matched-filter output or fitted mixture is stored, in the session files or in the raw-movie excerpt (its datasets are listed in the notebook);")
R["outcomes"] = [O[o["claim"]] for o in R["outcomes"]]
yaml.safe_dump(R, open(p, "w"), sort_keys=False, width=100, allow_unicode=True)
import collections
print(collections.Counter(o["outcome"] for o in R["outcomes"]), sum(1 for o in R["outcomes"] if o.get("assumed")))
yaml.safe_dump(orig, open("/tmp/claude-1001/dev/orig.yaml", "w"))
PYEOF
git show HEAD:attempts/001960-qi-2026-01.yaml > $TMPDIR/dev/rec_orig.yaml; python $TMPDIR/dev/rec.py; grep -n "spike-snr" -A8 attempts/001960-qi-2026-01.yaml | head -12
```

```
Counter({'reproduced': 36, 'blocked': 9, 'not_reproduced': 6, 'partially_reproduced': 5}) 6
39:- claim: spike-snr-and-detection-errors
40-  outcome: not_reproduced
41-  notebook: qi2026_spontaneous.ipynb
42:  output: claim:spike-snr-and-detection-errors
43-  measured: 3.33
44-  notes: The stored voltage is normalized by each cell's spike height, so the SNR is 1 over the shot noise
45-    (1.4826 x MAD of the 1-frame difference). It is 3.33 over the 505 QC cells of the behavior sessions
46-    (3.18 over all 640) and 3.0 to 3.9 per mouse and session under every reading, below 4.5 +/- 0.7. With
47-    the spike heights found in the traces (median 0.88 to 0.96 SH) it is 2.8 to 3.0. The false-discovery
48-    and false-negative rates were not computed, since no matched-filter output or fitted mixture is stored,
49-    in the session files or in the raw-movie excerpt (its datasets are listed in the notebook); the SNR
50-    alone decides the outcome under every reading.
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dev/rec2.py <<'PYEOF'
import yaml
p = "attempts/001960-qi-2026-01.yaml"
R = yaml.safe_load(open(p))
orig = yaml.safe_load(open("/tmp/claude-1001/dev/orig.yaml"))
F = R["findings"]
for f in F:
    if f["kind"] == "metadata_insufficient":
        f["statement"] += " The x and y axes are not oriented on the brain (no anterior, posterior, medial or lateral direction is stored), so the directions of the wave analysis can be given only in the image frame."
    if f["statement"].startswith("For the authors. Wave propagation analysis"):
        f["statement"] = "For the authors. Wave propagation analysis; how were peaks of the derivative separated or merged, was the derivative smoothed, in what window were the flanking minimum and maximum sought, and is lag signed or absolute against separation? Spans between adjacent turning points give 4,446 events and 10.1 mm/s, spans within 250 ms 3,775 events and 6.2 mm/s; lag regressed on distance gives hundreds of mm/s."
    if f["statement"].startswith("For the authors. Detection limits and the lasso"):
        f["statement"] = "For the authors. Detection limits and the lasso correction; which 100 pairs near the cutoff, how the 50% point was estimated, which per-trial response entered the lasso, and its penalty. The per-pair statistics and nulls are not stored. A rebuilt lasso (per-pulse voltage 20 to 60 ms after onset, cross-validated penalty) gives R = 0.94 with the raw matrix and 72% of pairs changed by more than 20%."
F.append({"kind": "methods_unavailable", "statement": "For the authors. IPSP durations (Supplementary Fig. 25C); were decay fits that end on the 0.4 s bound left out? Left out, the means are 57.1 and 41.9 ms (paper 58 and 43); kept, 77.4 and 65.2 ms."})
V = yaml.safe_load(open("/tmp/claude-1001/dev/verif.yaml"))
R["verifications"] = V
yaml.safe_dump(R, open(p, "w"), sort_keys=False, width=100, allow_unicode=True)
for r in V[0]["results"]:
    assert r["agrees"] == (r["outcome"] == orig[r["claim"]]), r["claim"]
print(len(V[0]["results"]))
PYEOF
echo written
```

```
written
```

**Agent calls Bash**

```bash
cat > $TMPDIR/dev/verif.yaml <<'EOF'
- date: 2026-11-06
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 1. The executed notebooks of the first run with the conclusion cells and the summaries
    removed, the helper module and the claims file, with the paper. The verifier queried the archive's
    asset list and tested helper functions on synthetic inputs. Report in
    transcripts/001960/verifier-1-report.md.
  results:
  - claim: jf608-brighter
    agrees: true
    outcome: blocked
    reason: The archive API lists 7 assets (3 sessions x 2 mice plus a raw excerpt). There is no JF585/JF608 comparison.
    response: No change needed.
  - claim: targeting-signal-to-background
    agrees: true
    outcome: blocked
    reason: There are no wide-field and targeted images of the same field. The excerpt is a targeted-illumination movie.
    response: No change needed.
  - claim: spike-snr-and-detection-errors
    agrees: true
    outcome: not_reproduced
    reason: SNR (1/noise) is 3.18 to 3.45 under every reading, below 4.5 +/- 0.7. The Methods' definition matches the notebook's. The false-discovery and false-negative rates were not computed. It also noted that the raw excerpt's metadata mentions the demixing and spike-finding products and its contents were not checked (problem 7).
    response: Added a listing of every dataset of the raw-movie excerpt; it holds no matched-filter output or fitted mixture, so the error rates still cannot be read from the files. Outcome kept.
  - claim: snr-decay-one-hour
    agrees: true
    outcome: reproduced
    reason: Mean of ratios is 72.9% (QC) and 77.3% (all); ratio of means is 69.8% and 73.4%. All are within 76 +/- 13.
    response: No change needed.
  - claim: fig1d-stimulation-fold-change
    agrees: true
    outcome: blocked
    reason: No 76-cell periodic-stimulation session in the asset list.
    response: No change needed.
  - claim: off-target-length-constants
    agrees: true
    outcome: blocked
    reason: No lattice experiment.
    response: No change needed.
  - claim: l1-sampling-density
    agrees: true
    outcome: blocked
    reason: No z-stack, only a GFP maximum projection.
    response: No change needed.
  - claim: adaptation-vadp-correlation
    agrees: true
    outcome: reproduced
    reason: Reading (a) R = 0.232, p = 4.5e-8, n = 543.
    response: No change needed.
  - claim: fig2c-three-bins
    agrees: true
    outcome: reproduced
    reason: Cluster sizes are exactly {94, 110, 116}.
    response: No change needed.
  - claim: fig2gk-bin-profiles
    agrees: true
    outcome: reproduced
    reason: 8 of 8 orderings hold under both readings.
    response: No change needed.
  - claim: two-mice-intrinsic-distributions
    agrees: false
    outcome: blocked
    reason: The named readings disagree; all cells give 4/5 (time constant p = 0.101), QC cells give 5/5 (p = 0.048), so the header rule blocks it. M-YQ0201-27 has 7 membrane time constants of exactly 0, which look like failed fits; treating them as missing may make the two readings agree (problem 5).
    response: Ran both readings with the zeros treated as missing. Both then give the five calls (time constant p = 0.031 and 0.033), so the readings agree; outcome kept as reproduced, now marked as resting on the assumption that a time constant of 0 is a failed fit, with the zeros kept as values also shown.
  - claim: synaptic-connection-counts
    agrees: true
    outcome: reproduced
    reason: 802/7280 and 667/7032 in 60 to 400 um. Per cell 2.62 out, 25.3 tested, 10.8%.
    response: No change needed. The claims file's citation of 800 connections in the band is asked of a reader (questions).
  - claim: ipsp-median-amplitude
    agrees: false
    outcome: partially_reproduced
    reason: The pooled median IPSP of -0.0297 is within tolerance. The cross-STA fluctuation averages 0.234 (0.217 and 0.250 per mouse) against 0.20 +/- 0.02.
    response: Changed to partially reproduced. The criterion computes the fluctuation per mouse and averaged, and its per-mouse clause applies to the IPSP median, so the average 0.234 is the value judged.
  - claim: detection-limits
    agrees: true
    outcome: blocked
    reason: Blocked as methods_underspecified, but the claims file gives readings. What is missing is the per-pair statistic or null, which could be rebuilt from stored data; the notebook never lists the full contents of the pairwise table (problem 3).
    response: Added the full listing of the pairwise table (no statistic, p-value or null is stored) and a timing of the paper's IPSP fit (48 ms), which puts the nulls of the 14,576 tested pairs at about 1,950 hours; the pairs near the cutoff cannot be chosen without them. Blocked reason changed to too_large.
  - claim: gap-junction-connection-counts
    agrees: true
    outcome: reproduced
    reason: 3553 and 2199; 9.99 out, 9.99 in, 40.9%; median spikelet 0.0120.
    response: No change needed.
  - claim: hadamard-stimulation-rates
    agrees: true
    outcome: reproduced
    reason: 26.5 Hz on, 3.6 Hz off, 12,929 evoked spikes. There are 650 stimuli if stimuli means 750 ms on-steps (the Methods' step); 360 if it means on-blocks.
    response: No change needed.
  - claim: spikelet-not-scatter
    agrees: true
    outcome: blocked
    reason: The excerpt is 356.8 GB, but a subset of frames would allow a partial test; too_large assumes the whole movie must be read (problem 10).
    response: Added a partial test on the first 40,000 frames of the excerpt (about 7 minutes). The scatter-to-spikelet ratio at 40 to 80 um is 3.03 and the scatter falls faster than the spikelet, so the outcome changed to reproduced, with the subset as a deviation.
  - claim: highmag-footprint
    agrees: true
    outcome: blocked
    reason: No 7.5x recordings.
    response: No change needed.
  - claim: lasso-off-target-correction
    agrees: true
    outcome: blocked
    reason: The stated block reason is wrong; 1755 = 955 + 800 stored synaptic flags, the penalty readings are in the claims file, and per-trial responses can be derived from the stored data (problem 2).
    response: Rebuilt the per-pulse responses and evoked spikes of the 14,400 pulses per mouse and ran the lasso under both penalty readings over the 1755 flagged pairs. Under (a) R = 0.937 and 72% of pairs change by more than 20%; under (b) almost every coefficient is zero. Outcome changed to not reproduced, resting on the assumed response window and off-target rule. The claims file's statement that the 1755 pairs are not given is asked of a reader.
  - claim: connection-distance-structure
    agrees: true
    outcome: partially_reproduced
    reason: Probabilities 23.5% and 83.0% match; gap-junction length constant under (b) is 156 to 161 um. Synaptic length constant is 151 to 362 um under every reading against 105, and M-YQ0201-29 out-degree fits a power law better.
    response: No change needed.
  - claim: fig3eg-amplitude-falls-with-distance
    agrees: true
    outcome: reproduced
    reason: Nearest bin median exceeds farthest for both measures in both mice; Spearman rho < 0, p << 0.05.
    response: No change needed.
  - claim: fig3h-conduction-speed
    agrees: true
    outcome: reproduced
    reason: Pooled 0.265 m/s, within 0.28 +/- 0.028.
    response: No change needed.
  - claim: amplitudes-log-normal
    agrees: false
    outcome: not_reproduced
    reason: Spikelet log-skew is 0.73, above 0.5. The selection deviates from the claims file; it uses all stored flags (7443 spikelet pairs) where the header requires QC cells and drops pairs under 60 um (5752 pairs), so this is provisional (problem 4).
    response: Rerun on QC pairs 60 to 400 um, the header's selection. The spikelet log skewness is 0.41 and the IPSP 0.13, both inside the reading, so the outcome changed to reproduced; the other selections are shown.
  - claim: interaction-kernel
    agrees: true
    outcome: not_reproduced
    reason: Peak 33.0 ms is in range, but the decay of 39.4 or 47.9 ms, FWHM 22.7 ms and length constant of 72 or 96 um are outside tolerance. The FWHM baseline sits on a slow hump (problem 11).
    response: Added the FWHM with the spikelet's flanking frames as baseline, 4.94 ms, still not about 2 ms. Outcome kept.
  - claim: fig3jk-presynaptic-sets-amplitude
    agrees: true
    outcome: reproduced
    reason: R = 0.609 and 0.263, n = 497 and 482, exact.
    response: No change needed.
  - claim: fig3mn-postsynaptic-sets-decay
    agrees: true
    outcome: reproduced
    reason: Incoming R = 0.330 (p = 4.7e-18); outgoing R = 0.075, p = 0.056.
    response: No change needed.
  - claim: fig3lo-variance-components
    agrees: true
    outcome: reproduced
    reason: Reproduced (fragile). Amplitude pre > post in 100%; decay post > pre in 99.95% of converged refits. Non-converged refits were excluded; two adverse non-converged refits out of 31 would flip it, and their variances are not shown (problem 6).
    response: Added every refit, the non-converged ones as fitted and refitted from the grid start. None of them has the adverse ordering; over all 2,000 the adverse share is 0% (amplitude) and 0.05% (decay). Outcome kept.
  - claim: gap-junction-no-identity-effect
    agrees: true
    outcome: not_reproduced
    reason: R = 0.214, 0.298, 0.268, 0.314; three of four are >= 0.26.
    response: No change needed.
  - claim: subthreshold-correlation-length
    agrees: true
    outcome: reproduced
    reason: 0.638 / 0.518; 2.42 / 4.03 mm.
    response: No change needed.
  - claim: subthreshold-low-dimensional
    agrees: true
    outcome: reproduced
    reason: Reading (a), averaged, 70.7% quiet, 67.5% whisking, quiet > whisking.
    response: No change needed.
  - claim: quiet-state-oscillations
    agrees: true
    outcome: reproduced
    reason: Quiet/whisking 1 to 10 Hz power ratio is 4.94 and 2.92.
    response: No change needed.
  - claim: traveling-waves
    agrees: true
    outcome: blocked
    reason: No analysis was run although the data and a Methods procedure exist; the open details should have been run under the readings the paper allows (problem 1).
    response: Ran the Methods procedure with its open details as readings (span of an event, counting, speed fit). No reading gives both the event count and the speed within tolerance, and the direction cannot be oriented on the brain, so the outcome changed to not reproduced, resting on those readings.
  - claim: spike-synchrony-localized
    agrees: true
    outcome: partially_reproduced
    reason: Reading (a) 277.1 and 270.7 um, half-width 2.54 ms. FWHM averaged over mice is 71.1 ms against 80 +/- 8 (M-YQ0201-27 alone, 78.7, would pass). Averaging over mice is an unstated aggregation choice (problem 14).
    response: No change. The criterion says the values are fitted per mouse and averaged, and the per-mouse values are printed.
  - claim: voltage-to-spike-sigmoid
    agrees: true
    outcome: reproduced
    reason: Reproduced (marginal). At the spike frame 52% of cells have R^2 >= 0.9 and both CVs are > 0.2; the Methods (V(t_s)) and the code agree on this reading. The caption variant was a single sample 8 frames before the spike, not a 10 ms interval, and the fitted maxima (CV 4.54) are unconstrained extrapolations (problem 8).
    response: Added the 10 ms interval reading (mean of the 8 frames before, 42% pass), the largest observed rate (CV 0.59) and fits with bounded tops (CV 0.64 and 0.29). Outcome kept, resting on the Methods' and code's reading. The claims file's attribution of the 10 ms to the Methods is asked of a reader.
  - claim: fig4g-private-depolarizations
    agrees: true
    outcome: reproduced
    reason: Slope ratio 2.89 pooled.
    response: No change needed.
  - claim: fig4hi-self-sta-diverges
    agrees: true
    outcome: reproduced
    reason: Increase 0.176 and 0.182 against s.d. 0.015 and 0.007; self above cross at -30 ms.
    response: No change needed.
  - claim: fig5a-rheobase-predicts-spontaneous-excitability
    agrees: true
    outcome: reproduced
    reason: rho = -1.00 in both conditions for M-YQ0201-27 code bins.
    response: No change needed.
  - claim: supp22-rheobase-correlations
    agrees: true
    outcome: reproduced
    reason: Reading (a) R = -0.573 and -0.311, n = 543.
    response: No change needed.
  - claim: fig5b-adaptation-dvdt
    agrees: true
    outcome: reproduced
    reason: R = 0.274 (Methods reading) and 0.262 (code reading); M-YQ0201-27 top bin is highest.
    response: No change needed.
  - claim: fig5c-adp-bursting
    agrees: true
    outcome: reproduced
    reason: Main reading R = 0.546.
    response: No change needed.
  - claim: fig5e-inhibition-in-spontaneous-voltage
    agrees: false
    outcome: partially_reproduced
    reason: Under (c), -0.0213 and -0.0095 with p << 0.05. The controls' +1% rise is not matched; control medians are 0.003 to 0.008, means 0.012 to 0.019, and the rise is never measured on the control-average waveform (problem 9).
    response: Added the rise on the spike-weighted control-average waveform; it is +0.0097 for the controls of all connected pairs, within 0.01 +/- 0.001, and +0.0049 for the top quintile's. Outcome kept as reproduced, since the criterion tests the two pair values; the disagreement is recorded, and the criterion's "both values" against three expected values is asked of a reader.
  - claim: fig5e-inhibition-in-spontaneous-rate
    agrees: true
    outcome: partially_reproduced
    reason: Under (a) rates are 0.190 and 0.083 Hz, but spikes lost fail under every reading.
    response: No change needed.
  - claim: fig5g-gap-junction-synchrony
    agrees: true
    outcome: partially_reproduced
    reason: Under (a) 0.80 and 0.29 Hz, but spikes gained (0.0022 and 0.0009) fail.
    response: No change needed.
  - claim: inhibition-gap-balance
    agrees: true
    outcome: blocked
    reason: Readings give ratios of 6.96, inf, 1.37 and -0.19; reading (c) gives about 1.96. Its inputs did not reproduce.
    response: No change needed.
  - claim: npy-fraction-and-similarity
    agrees: true
    outcome: reproduced
    reason: NPY+ counts are within tolerance in every session; SNR and rate similar; KS p >= 0.08.
    response: No change needed.
  - claim: npy-intrinsic-differences
    agrees: true
    outcome: reproduced
    reason: 5 of 5 at p <= 0.001.
    response: No change needed.
  - claim: npy-classifier
    agrees: true
    outcome: reproduced
    reason: 76.8% against chance 50.0%; V_adp is top under both readings. Features are z-scored on all cells before the train/test split, a mild leakage (problem 12).
    response: The scaler is now fitted on the training cells of each split; the numbers are unchanged (76.8%, chance 50.0%, V_adp top).
  - claim: npy-connection-probability
    agrees: true
    outcome: reproduced
    reason: 13.7% against 7.4%, n = 307 and 269, p = 1.4e-9.
    response: No change needed.
  - claim: npy-ipsp-amplitude
    agrees: true
    outcome: reproduced
    reason: -0.0372 (977 pairs) against -0.0311 (490 pairs), p = 8e-7, counts exact.
    response: No change needed. The claims file's citation of 800 connections is asked of a reader.
  - claim: npy-ipsp-duration
    agrees: true
    outcome: reproduced
    reason: Reproduced (fragile). QC 60 to 400 um, 77.4 against 65.2 ms, n = 760 and 709, p = 3e-13; the NPY- count is just inside 646 +/- 65. The header-consistent selection (QC cells within 400 um, no 60 um cut) was not run and would likely push NPY- above 711; means include fits capped at 0.4 s (problem 13).
    response: Added QC pairs within 400 um and the fits at the 0.4 s bound left out. Left out, both selections give the paper's means within 1.5 ms (57.1 and 41.9 ms; 715 and 663 pairs). Kept, the within-400 um NPY- count is 723, outside. Outcome kept, now resting on the assumption that fits on the bound are failed fits.
  - claim: npy-gap-junction-no-difference
    agrees: true
    outcome: not_reproduced
    reason: Consistent-direction outgoing effects in probability and spikelet amplitude, and incoming effects in amplitude.
    response: No change needed.
  - claim: npy-subthreshold-similar
    agrees: true
    outcome: reproduced
    reason: M-YQ0201-29 R = 0.973, slope 0.933 or 1.015.
    response: No change needed.
  - claim: npy-umap-groups
    agrees: true
    outcome: reproduced
    reason: Medians over seeds 158.5/205 and 201/300; Fisher p ~1e-23.
    response: No change needed.
  - claim: npy-whisking-onset-rates
    agrees: true
    outcome: reproduced
    reason: NPY+ 1.06 to 2.20 Hz (p = 6e-8); NPY- 1.27 to 1.50 Hz (p = 0.76).
    response: No change needed.
  - claim: npy-oscillation-peak-rates
    agrees: false
    outcome: blocked
    reason: Reading (b) passes. Reading (a) fails because the voltage differs (p = 0.022), so the readings disagree.
    response: Changed to blocked (methods underspecified), as the claims file's header rule requires when its named readings give different outcomes.
  - claim: npy-state-dependent-excitability
    agrees: true
    outcome: reproduced
    reason: All four comparisons hold at p <= 0.05.
    response: No change needed.
EOF
cd  python $TMPDIR/dev/rec2.py
```

```
56
```

**Agent calls Bash**

```bash
date -u; cd  cat > questions/001960.yaml <<'EOF'
dandiset: "001960"
paper: doi:10.64898/2026.10.05.756595
questions:
- claim: voltage-to-spike-sigmoid
  asked: 2026-11-06
  question: The criterion says "The Methods/caption say V in the 10 ms before spikes". The Methods
    define V(t_s) as the subthreshold voltage at spike times; only the Results and the Figure 4E
    legend speak of a 10 ms interval. Should the criterion attribute the 10 ms reading to the
    Results and the legend, and name the Methods' V(t_s) with the code's spike-frame reading?
  passage: We calculated the empirical spike probability conditioned on subthreshold voltage as
    where V(t s ) is the subthreshold voltage at spike times and P(V) is the distribution of all
    subthreshold voltages. (Methods, P(spk|V) for spontaneous and optically evoked firing)
  why: The readings give different outcomes. V at the spike frame passes (262 of 505 cells, 52%),
    the mean of the 10 ms before does not (42%), nor the sample 10 ms before (24%). The outcome rests
    on the spike-frame reading, which the Methods support, but the criterion presents the 10 ms as
    the Methods' reading.
- claim: fig5e-inhibition-in-spontaneous-voltage
  asked: 2026-11-06
  question: The expected values list three quantities (top quintile, median strength, and the
    controls' rise of 1%), but the criterion is met "when both values are within tolerance". Is the
    controls' rise part of the test?
  passage: The STA waveform showed an increase by 1% of a spike height in the interval 15 - 30 ms
    after the triggering spike vs. the -20 to - 5 ms before the spike (Results, Local connectivity
    shapes network dynamics, paragraph 2)
  why: The pair values pass under reading (c). The controls' rise is +0.0097 on the control-average
    waveform of all connected pairs (within 0.01 +/- 0.001) but +0.0049 for the top quintile's
    controls and +0.003 to +0.019 per control pair, so whether it is tested, and on which controls,
    could change the outcome.
- claim: lasso-off-target-correction
  asked: 2026-11-06
  question: The criterion says the choice of the 1755 pairs is not given. The stored synaptic
    connection flags of the two mice number 955 and 800, 1755 in all. Are the 1755 pairs the
    connected pairs, so that the comparison is over them?
  passage: The two matrices are highly correlated, with a Pearson correlation coefficient of 0.82,
    p < 2E-308, n = 1755 pairs from 2 mice, and less than 20% of statistically significant IPSPs
    differ from the connectivity matrix by more than 20% (Supplementary Figure 16C)
  why: The attempt took the 1755 pairs to be the stored flags; another set of pairs would change
    both the correlation and the fraction of changed IPSPs.
- claim: synaptic-connection-counts
  asked: 2026-11-06
  question: The criterion (and npy-ipsp-amplitude) cites the code as giving 800 connections for
    M-YQ0201-27 in the 60 to 400 um band. The data have 802 flags there, 800 of them with a finite
    amplitude, and the paper says 802. Should the citation say 802 connections, 800 with an
    amplitude?
  passage: We identified 802 statistically significant synaptic connections out of 7,280 pairs
    tested in one mouse, and 667 of 7,032 pairs tested in a second mouse. (Results, Synaptic
    inhibition, paragraph 6)
  why: It does not change the outcome (the counts match the paper under the band reading), but
    the criterion's number reads as a count of connections when it is a count of amplitudes.
EOF
python -c "import yaml; yaml.safe_load(open('questions/001960.yaml'))" && echo ok
```

```
Fri Nov  6 11:26:07 UTC 2026
ok
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
p = "attempts/001960-qi-2026-01.yaml"
R = yaml.safe_load(open(p))
for o in R["outcomes"]:
    if o["claim"] in ("fig5e-inhibition-in-spontaneous-voltage", "synaptic-connection-counts", "npy-ipsp-amplitude"):
        o["notes"] += " A possible misreading in the claims file is asked of a reader (questions)."
yaml.safe_dump(R, open(p, "w"), sort_keys=False, width=100, allow_unicode=True)
s = open("entries/001960-qi-2026/README.md").read()
a = s.index("| Claims | Outcome |"); b = s.index("A failure to reproduce here")
s = s[:a] + '''| Claims | Outcome |
|---|---|
| Intrinsic properties and their three clusters, two-mouse comparison (Figure 2, four claims) | Reproduced |
| Synaptic and gap-junction connection counts, Hadamard rates, distance decay, conduction speed, log-normal amplitudes (Figure 3, six claims) | Reproduced |
| IPSP median and size of correlated fluctuations | Partially reproduced |
| Scatter control from the raw movie (first 40,000 frames) | Reproduced |
| Presynaptic identity sets IPSP amplitude, postsynaptic sets decay, mixed-model variances (Figure 3J to O) | Reproduced (three claims) |
| Connection structure with distance | Partially reproduced |
| Population interaction kernel; gap-junction strength without identity effect; lasso off-target correction | Not reproduced |
| Spontaneous correlations, dimensionality, oscillations, voltage-to-spike curves, private depolarizations (Figure 4, six claims) | Reproduced |
| Traveling waves | Not reproduced |
| Spike-synchrony length constants and widths | Partially reproduced |
| SNR decay over an hour | Reproduced |
| Single-spike SNR and detection errors | Not reproduced |
| Intrinsic properties shape spontaneous firing (Figure 5A to C, Supplementary Figure 22, four claims) | Reproduced |
| Inhibition in spontaneous voltage | Reproduced |
| Inhibition in spontaneous rate; gap-junction synchrony | Partially reproduced |
| NPY subtypes: counts, intrinsic differences, classifier, connectivity, UMAP groups, whisking and state effects (Figure 6, ten claims) | Reproduced |
| NPY subtypes do not differ in gap-junction connectivity | Not reproduced |
| Figure 1 tool experiments, high-magnification footprints (seven claims) | Blocked: data missing |
| Detection limits | Blocked: too large |
| Inhibition-gap balance; rates at oscillation peaks | Blocked: methods underspecified |

Of the 56 claims, 47 are tested (36 reproduced, 5 partially reproduced, 6 not reproduced) and 9
blocked. Six outcomes rest on an assumption about a method the paper leaves open
(two-mice-intrinsic-distributions, hadamard-stimulation-rates, voltage-to-spike-sigmoid,
npy-ipsp-duration, lasso-off-target-correction, traveling-waves).

''' + s[b:]
s = s.replace("excerpt. Of the 56 claims, 45 are tested and 11 blocked.", "excerpt. Of the 56 claims, 47 are tested and 9 blocked.")
s = s.replace("Figure 6 excitability and connectivity claims (about 16 minutes).", "Figure 6 excitability and connectivity claims, the lasso correction and the scatter control (about 40 minutes).")
s = s.replace("behaviour claims (about 11 minutes;", "behaviour claims and the wave analysis (about 27 minutes;")
s = s.replace("Supplementary Figure 22 (about 10 minutes).", "Supplementary Figure 22 (about 13 minutes).")
open("entries/001960-qi-2026/README.md", "w").write(s)
e = open("entries/001960-qi-2026/entry.yaml").read()
e = e.replace("runtime_minutes: 16", "runtime_minutes: 40").replace("runtime_minutes: 11", "runtime_minutes: 27").replace("runtime_minutes: 10", "runtime_minutes: 13")
open("entries/001960-qi-2026/entry.yaml", "w").write(e)
import collections
print(collections.Counter((o["outcome"], o.get("blocked_by")) for o in R["outcomes"]))
EOF
grep -n "about\|minutes" entries/001960-qi-2026/README.md | tail -5; python tools/entry.py check entries/001960-qi-2026 2>&1 | grep -v "MissingID\|_validate" | tail -15
```

```
Counter({('reproduced', None): 36, ('blocked', 'data_missing'): 6, ('not_reproduced', None): 6, ('partially_reproduced', None): 5, ('blocked', 'methods_underspecified'): 2, ('blocked', 'too_large'): 1})
6:connectivity-mapping session of about 320 layer 1 interneurons imaged at 787 Hz, and a raw-movie
33:blocked. Six outcomes rest on an assumption about a method the paper leaves open
46:  Figure 6 excitability and connectivity claims, the lasso correction and the scatter control (about 40 minutes).
48:  behaviour claims and the wave analysis (about 27 minutes; it holds one session's voltage, 3 GB, in memory at a time).
49:- `qi2026_excitability_spontaneous.ipynb`: Figure 5A to C and Supplementary Figure 22 (about 13 minutes).
0 error(s)
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; sed -i 's/high-magnification footprints (seven claims)/high-magnification footprints (six claims)/' README.md; python -c "
import json
for n in ['qi2026_excitability_connectivity.ipynb','qi2026_spontaneous.ipynb']:
    nb=json.load(open(n)); print(''.join(nb['cells'][0]['source'])); print('=======')
"
```

```
# Reproducing Qi et al. (2026) from dandiset 001960

Paper. Qi, Parot, Wang, Pomeroy, Lavis and Cohen, "Large-scale all-optical electrophysiology
links excitability and connectivity to circuit dynamics in vivo", bioRxiv preprint
doi:10.64898/2026.10.05.756595 (version 1). The claims file `claims/001960/10.64898-2026.10.05.756595.yaml`
was written from the full text of that preprint (main text, figure legends, Methods) and its
supplementary information PDF, and checked by a second reader.

Dataset. DANDI:001960, version 0.261013.2016 (doi:10.48324/dandi.001960/0.261013.2016),
streamed from the archive. The paper's Data availability statement names the dandiset without a
version, and this is the only published version (the draft has the same 7 assets and the same
size, 505,494,176,572 bytes), so the most recent published version is pinned, as the protocol
asks when no version is cited.

Code read for methods. The paper's code, https://github.com/adamcohenlab/Qi2026WideAreaL1 at
commit 181ad475520224c44d27903e7522d3e2aa76857d, which the claims file cites for many criteria.
Every method detail is cited in the helper `l1opto.py` or in the cell that uses it.

The attempt has three notebooks, so that each runs well inside the time limit: this one (data
check, intrinsic properties, connectivity, the effect of connections on spontaneous activity, and
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/001960-qi-2026; cat > $TMPDIR/dev/hdr.py <<'PYEOF'
import sys, os; sys.path.insert(0, os.environ['TMPDIR'] + '/dev')
from nbed import *
p = 'qi2026_excitability_connectivity.ipynb'
nb = load(p)
s = get(nb, 0)
for a, b in [("| spikelet-not-scatter | none | blocked, too large (raw movie) |\n| detection-limits, lasso-off-target-correction | none | blocked, methods underspecified |",
              "| spikelet-not-scatter, lasso-off-target-correction | this one | tested (the scatter on a subset of the raw movie) |\n| detection-limits | this one | blocked, too large (the per-pair nulls are not stored) |"),
             ("| npy-intrinsic-differences, npy-classifier, npy-connection-probability, npy-ipsp-amplitude, npy-ipsp-duration, npy-gap-junction-no-difference | this one | tested |",
              "| npy-intrinsic-differences, npy-classifier, npy-connection-probability, npy-ipsp-amplitude, npy-ipsp-duration, npy-gap-junction-no-difference | this one | tested |"),
             ("npy-whisking-onset-rates, npy-oscillation-peak-rates, npy-state-dependent-excitability | qi2026_spontaneous | tested |\n| traveling-waves | qi2026_spontaneous | blocked, methods underspecified |",
              "npy-whisking-onset-rates, npy-state-dependent-excitability, traveling-waves | qi2026_spontaneous | tested |\n| npy-oscillation-peak-rates | qi2026_spontaneous | blocked, methods underspecified (both readings shown) |"),
             ("Of the 56 claims, 45 are tested and 11 blocked.", "Of the 56 claims, 47 are tested and 9 blocked.")]:
    assert a in s, a[:50]
    s = s.replace(a, b)
set_src(nb, 0, s)
save(nb, p)
p = 'qi2026_spontaneous.ipynb'
nb = load(p)
s = get(nb, 0)
for a, b in [("| traveling-waves | blocked, methods underspecified |", "| traveling-waves | tested |"),
             ("npy-whisking-onset-rates, npy-oscillation-peak-rates, npy-state-dependent-excitability | tested |",
              "npy-whisking-onset-rates, npy-state-dependent-excitability | tested |\n| npy-oscillation-peak-rates | blocked, methods underspecified (both readings shown) |")]:
    assert a in s, a[:50]
    s = s.replace(a, b)
set_src(nb, 0, s)
save(nb, p)
PYEOF
python $TMPDIR/dev/hdr.py && grep -c "assumption" qi2026_excitability_connectivity.ipynb; python -c "
import json
nb=json.load(open('qi2026_excitability_spontaneous.ipynb')); print(''.join(nb['cells'][16]['source'])[-800:])"
```

```
10
## Summary

| Claim | Outcome |
|---|---|
| fig5a-rheobase-predicts-spontaneous-excitability | reproduced |
| supp22-rheobase-correlations | reproduced |
| fig5b-adaptation-dvdt | reproduced |
| fig5c-adp-bursting | reproduced |

How the analysis differs from the paper's. It follows the code's Figure 5 streaming pass on the
stored subthreshold voltage, blue waveforms and spike times. The selection of 543 cells is the QC
cells of the two sparseOpto sessions, which is the paper's n. The rate at V = 0.5 SH is read from
the bin [0.50, 0.55) SH and at dV/dt = 0.35 from [0.34, 0.37).

What was found about the dataset. The median-rule and stored quiet masks agree on 84% of frames
in M-YQ0201-27 (the code's number) and 61% in M-YQ0201-29.
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
for nbn in ("qi2026_excitability_connectivity.ipynb", "qi2026_spontaneous.ipynb"):
    src = json.load(open(f"entries/001960-qi-2026/{nbn}"))
    ex = json.load(open(f"executed/001960-qi-2026/{nbn}"))
    exc = [c for c in ex["cells"] if c["cell_type"] == "code"]
    sc = [c for c in src["cells"] if c["cell_type"] == "code"]
    assert len(exc) == len(sc) and all("".join(a["source"]) == "".join(b["source"]) for a, b in zip(sc, exc))
    k = iter(exc)
    ex["cells"] = [next(k) if c["cell_type"] == "code" else c for c in src["cells"]]
    json.dump(ex, open(f"executed/001960-qi-2026/{nbn}", "w"), indent=1, ensure_ascii=False)
print("ok")
EOF
python tools/entry.py check entries/001960-qi-2026 2>&1 | grep -v "MissingID\|_validate" | tail; python tools/entry.py handover entries/001960-qi-2026 2>&1 | tail -1; grep -rn "—\|rather" entries/001960-qi-2026/*.md questions/001960.yaml attempts/001960-qi-2026-01.yaml | head; python - <<'EOF'
import json,re
for n in ["qi2026_excitability_connectivity.ipynb","qi2026_spontaneous.ipynb"]:
    nb=json.load(open("entries/001960-qi-2026/"+n))
    for c in nb["cells"]:
        s="".join(c["source"])
        if "—" in s or re.search(r"\brather\b", s): print(n, s[:80])
EOF
git status --short
```

```
ok
0 error(s)
wrote executed/001960-qi-2026/handover
 M attempts/001960-qi-2026-01.yaml
 M entries/001960-qi-2026/README.md
 M entries/001960-qi-2026/entry.yaml
 M entries/001960-qi-2026/l1opto.py
 M entries/001960-qi-2026/qi2026_excitability_connectivity.ipynb
 M entries/001960-qi-2026/qi2026_spontaneous.ipynb
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
?? questions/001960.yaml
[... 1 more lines not kept]
```

**Agent**

I've revised the attempt for every point in the round-1 report, re-run the entry, and recorded the round. The full run passed in about 81 min: 40, 27 and 13 min for the three notebooks. `entry.py check` reports 0 errors and the handover is rebuilt. After the run I edited only markdown cells (conclusions, summaries, headers), and copied them into the executed copies without re-executing; the code cells and their outputs are unchanged. Nothing is committed.

**Outcome changes.** Of the 56 claims, 47 are now tested (36 reproduced, 5 partially reproduced, 6 not reproduced) and 9 are blocked, against 45 tested and 11 blocked before.
- **amplitudes-log-normal**: partially reproduced → reproduced. On the claims file's own selection (QC pairs 60 to 400 um), the spikelet log skew is 0.41 and the IPSP log skew 0.13, both inside the bounds. The earlier failure came from the pairs under 60 um.
- **ipsp-median-amplitude**: reproduced → partially reproduced, as the verifier said. The criterion averages the two mice's fluctuation values, and the average, 0.234, is outside 0.20 +/- 0.02.
- **npy-oscillation-peak-rates**: reproduced → blocked (methods underspecified). Its two named readings disagree, and the claims file's header blocks such claims.
- **spikelet-not-scatter**: blocked → reproduced, on the first 40,000 frames of the raw movie. The spikelet-to-scatter ratio at 40 to 80 um is 3.03, and the scatter falls off faster than the spikelet.
- **lasso-off-target-correction**: blocked → not reproduced, resting on assumptions. I rebuilt per-pulse responses and evoked spikes for the 14,400 pulses per mouse. With the cross-validated penalty, R = 0.937 and 72% of pairs change by more than 20%. With the one-standard-error penalty, almost every coefficient is zero.
- **traveling-waves**: blocked → not reproduced, resting on assumptions. I ran the Methods procedure, with each open detail as a reading. No reading gets both the event count and the speed within tolerance. The direction could not be tested, because the files do not say how the image axes sit on the brain; I added this as a finding.
- **detection-limits**: still blocked, now as too large. The pairwise table stores no per-pair statistic or null distribution. Rebuilding the nulls would take about 1,950 hours at the measured 48 ms per fit.

**Kept, with outputs added.**
- **two-mice-intrinsic-distributions**: reproduced. Treating the 7 membrane time constants of exactly 0 as failed fits makes both readings agree; this is now marked as an assumption.
- **npy-ipsp-duration**: reproduced. Leaving out the 91 fits that end on the 0.4 s bound gives 57.1 and 41.9 ms against the paper's 58 and 43; also marked as an assumption.
- **fig3lo-variance-components**: reproduced. Over all 2,000 refits, including the non-converged ones and their refits, the adverse share is 0% (amplitude) and 0.05% (decay), under the 0.1% bound.
- **fig5e-inhibition-in-spontaneous-voltage**: still reproduced; the disagreement with the verifier is recorded. Measured on the control-average waveform, the controls' rise is +0.0097 for all connected pairs, inside tolerance, but +0.0049 for the top quintile.
- **voltage-to-spike-sigmoid**: still reproduced, narrowly. I added the 10 ms interval reading (42% of cells pass, below half) and bounded-top fits (CVs 0.64 and 0.29). It passes only on the spike-frame reading the Methods and code use.
- **npy-classifier**: z-scoring now happens inside each training split; the numbers are unchanged.
- **interaction-kernel**: added a second FWHM baseline, which gives 4.94 ms instead of 22.7 ms; still not the claimed ~2 ms.
- **spike-snr-and-detection-errors**: the raw-movie excerpt is now listed in full; it holds no matched-filter output or fitted mixture.

**Record and questions.**
- The attempt record has a `verifications` entry for round 1, with all 56 claims, the verifier's reasons and my responses.
- I added findings on the image-axis orientation, on the fits at the decay bound, and updated the wave and lasso method questions for the authors.
- I created `questions/001960.yaml` with the four claims-file misreadings the verifier reported (voltage-to-spike-sigmoid, fig5e voltage, lasso, and the "800" count).

**Not done.**
- The spike-detection false-discovery and false-negative rates were not rebuilt. They would not change the outcome, since the SNR alone fails under every reading.
- spike-synchrony-localized is unchanged: its criterion says to average the two mice, and the per-mouse values are printed.

## End of run

78 turns, 181 minutes, $9.55 at API prices, result: success.
