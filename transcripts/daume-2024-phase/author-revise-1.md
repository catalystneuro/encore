# 000673 · author-revise-1 · run 41201740813

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/000673/verifier-1-report.md; ls entries/000673-daume-2024 entries/000673-daume-2024/*
```

```
Sat Oct 31 12:36:55 UTC 2026
**Verification report, round 1: Daume et al. 2024 on DANDI:000673 (0.240118.2135)**

The claims file has 57 claims. The three notebooks test 30 of them; the other 27 were not run, and none of the three notebooks marks fig3h as tested or blocked.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| cohort-counts | reproduced | All counts match exactly: 44 sessions, 36 patients, 1,454 units, 1,922 LFP channels, and every per-area count (nb1 cell 12). |
| fig1d-rt-load | reproduced | Median RT is 1.233 s (load 1) and 1.360 s (load 3), both within tolerance; t43 = 5.33, p = 0.0001 (nb1 cell 14). The mean-RT variant gives no effect (t = −0.48), because RTs up to 74 s pull the means. |
| fig1d-accuracy-load | reproduced | 95.10% against 91.02%; t43 = −5.24, p = 0.0001 (nb1 cell 15). |
| behaviour-overall-accuracy | reproduced | 93.05 ± 7.22%; false negatives 76.08 ± 20.11% of errors; both within tolerance (nb1 cell 17). |
| fig2a-theta-gamma-pac | reproduced | The largest mean z is at 4 Hz phase, 80 Hz amplitude; at 4 and 6 Hz there are local maxima at 50/40 Hz and 80 Hz (lfp cell 7). Only artefact reading (a) is shown. |
| fig2b-pac-channel-proportions | partially_reproduced | Reading (a): hippocampus 144, amygdala 130, vmPFC 41 and dACC 14 are within tolerance and all far above the null (p = 0.005). pre-SMA is 17 against 5, out of tolerance. Reading (b) puts four counts out of tolerance (lfp cell 9). |
| fig2c-hippocampus-load | reproduced | Load 1 is higher under both readings: n = 144, t = −4.16, FDR p = 0.001; reading (b) FDR p = 0.014 (lfp cell 11). |
| fig2c-no-load-effect-other-areas | not_reproduced | Reading (a): amygdala FDR p = 0.0475 and pre-SMA 0.0017, both with load 3 higher. Reading (b): pre-SMA and dACC FDR p = 0.014 (lfp cell 11). |
| edf2b-hippocampus-load-patients | reproduced | Reading (a): hippocampus, 23 patients, p = 0.0095, load 1 higher; no other area p < 0.05. This depends on O1: under (b) the hippocampus g
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/protocol.md; ls docs
```

```
<persisted-output>
Output too large (35.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/42b13f94-ac3c-4a66-b7cb-5fe3ed6c0bf9/tool-results/byhbarqus.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-12`. Record this version in the attempt's provenance.

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
cat entries/000673-daume-2024/entry.yaml; cat entries/000673-daume-2024/README.md; ls attempts 2>/dev/null | head; ls; ls transcripts/000673; ls questions | head
```

```
schema_version: 1
name: 000673-daume-2024
type: reproduction
title: Phase-amplitude coupling and working memory in human hippocampus (Daume et al. 2024)
description: Tests the findings of Daume et al. (2024) on dandiset 000673, which holds 44 sessions of
  a Sternberg working memory task in 36 epilepsy patients, with 1,454 single neurons and 1,922
  microwire LFP channels from the hippocampus, amygdala, pre-SMA, dACC and vmPFC. It tests the cohort,
  behaviour, category neurons and their maintenance activity, and the LFP theta-gamma
  phase-amplitude coupling and its load effect, and the selection and firing of PAC neurons. The
  spike-field coherence, noise correlation and decoding analyses were not run.
license: Apache-2.0
notebooks:
- path: reproduce_daume_2024.ipynb
  title: Behaviour and single neurons (Daume et al. 2024, dandiset 000673)
  runtime_minutes: 4
- path: reproduce_daume_2024_lfp.ipynb
  title: LFP phase-amplitude coupling (Daume et al. 2024, dandiset 000673)
  runtime_minutes: 20
- path: reproduce_daume_2024_pac_neurons.ipynb
  title: PAC neurons (Daume et al. 2024, dandiset 000673)
[... 101 more lines not kept]
```

**Agent**

Let me read the protocol in full.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/42b13f94-ac3c-4a66-b7cb-5fe3ed6c0bf9/tool-results/byhbarqus.txt"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-12`. Record this version in the attempt's provenance.
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
[... 604 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l attempts/000673-daume-2024-01.yaml; cat attempts/000673-daume-2024-01.yaml | head -400; ls docs/agents
```

```
582 attempts/000673-daume-2024-01.yaml
schema_version: 2
id: 000673-daume-2024-01
dataset:
  archive: dandi
  id: "000673"
  version: 0.240118.2135
  doi: 10.48324/dandi.000673/0.240118.2135
paper: doi:10.1038/s41586-024-07309-z
date: 2026-10-31
entry: 000673-daume-2024
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-12
  runner:
[... 395 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,600p attempts/000673-daume-2024-01.yaml; cat docs/agents/author-revise.md
```

```
blocked_by: other
  notebook: reproduce_daume_2024_pac_neurons.ipynb
  output: claim:pac-category-overlap
  notes: Too few PAC neurons under the claim's own selection (8 hippocampal and 5 amygdala, against
    79 and 163) for the overlap to describe the paper's populations. For the record, 4 of 8 and 2 of
    5 are category neurons; the binomial test gives p = 0.16 and 0.57 and the hypergeometric test p
    = 0.13 and 0.64.
- claim: edf7a-pac-neurons-no-category-decoding
  outcome: blocked
  blocked_by: other
  notes: Needs PAC neurons that are not category neurons; the selection gave 4 such neurons in the
    hippocampus and 3 in the amygdala (pac-neuron-counts), too few to decode from. The decoding of
    category neurons alone was not run.
- claim: fig4c-pac-neuron-firing-single-trial-pac
  outcome: blocked
  blocked_by: other
  notebook: reproduce_daume_2024_pac_neurons.ipynb
  output: claim:fig4c-pac-neuron-firing-single-trial-pac
  notes: Too few PAC neurons (8 hippocampal and 5 amygdala pairs). For the record, the hippocampal SC
    term is not significant (O5 a, p = 0.85; O5 b, p = 0.18) and the amygdala term gives p = 0.0496
[... 172 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "^verifications:" attempts/*.yaml | head -3; f=$(grep -l "^verifications:" attempts/*.yaml | head -1); awk '/^verifications:/,0' $f | head -80; ls questions/000673.yaml 2>/dev/null && cat questions/000673.yaml
```

```
Exit code 2
attempts/000003-senzai-2017-01.yaml
attempts/000004-chandravadia-2020-01.yaml
attempts/000005-yu-2016-01.yaml
verifications:
- date: '2026-10-16'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the
    helper module and the claims file, with the paper. The verifier queried the archive metadata and tested
    helper functions on synthetic inputs. Its report had no attempt record and gave its own outcome for
    each claim; all 31 agree with the record.
  results:
  - claim: unit-counts
    agrees: true
    outcome: partially_reproduced
    reason: GC 609 is inside 527 to 645, but MC 568 is outside 450 to 550.
    response: No change needed.
  - claim: first-stage-labels
    agrees: true
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/000673/; wc -l claims/000673/*; ls paper/; ls executed/ 2>/dev/null | head; python -c "
import json
for nb in ['reproduce_daume_2024','reproduce_daume_2024_lfp','reproduce_daume_2024_pac_neurons']:
    d=json.load(open(f'entries/000673-daume-2024/{nb}.ipynb'))
    print(nb,len(d['cells']))
    for i,c in enumerate(d['cells']):
        print(i,c['cell_type'],c['metadata'].get('tags'),repr(''.join(c['source'])[:80]))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l entries/000673-daume-2024/sbcat.py; sed -n 1,140p entries/000673-daume-2024/sbcat.py; timeout 20 curl -sI https://raw.githubusercontent.com/rutishauserlab/SBCAT-release-NWB/a25e8cc3f61630a428f190381745257d4506f148/README.md | head -3
```

Result: the fetched text is not kept.

**Agent**

I'm working through the verifier's report now. First I'm checking the paper's code for the PAC neuron GLM's data layout (problem 1).

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://raw.githubusercontent.com/rutishauserlab/SBCAT-release-NWB/a25e8cc3f61630a428f190381745257d4506f148; curl -s https://api.github.com/repos/rutishauserlab/SBCAT-release-NWB/git/trees/a25e8cc3f61630a428f190381745257d4506f148?recursive=1 | python -c "import json,sys; [print(t['path']) for t in json.load(sys.stdin)['tree']]" | grep -v "^MATLAB/helpers/.*/" | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/sb; cd $TMPDIR/sb; B=https://raw.githubusercontent.com/rutishauserlab/SBCAT-release-NWB/a25e8cc3f61630a428f190381745257d4506f148/NWB_SBCAT_analysis/helpers/internal/PAC; for f in NWB_samplePAC_SU.m plot_PAC_neuron.m artif_trials.mat; do curl -s -o $f $B/$f; done; ls -la; cat NWB_samplePAC_SU.m
```

```
total 28
drwxr-xr-x 2 runner runner 4096 Oct 31 12:37 .
drwx------ 6 runner runner 4096 Oct 31 12:37 ..
-rw-r--r-- 1 runner runner 5179 Oct 31 12:37 NWB_samplePAC_SU.m
-rw-r--r-- 1 runner runner  203 Oct 31 12:37 artif_trials.mat
-rw-r--r-- 1 runner runner 6282 Oct 31 12:37 plot_PAC_neuron.m
function [figOut] = NWB_samplePAC_SU(nwbAll, all_units, paths)
% - nwbAll: a cell array of all nwb files imported in NWB_SBCAT_import_main
% operation: 
% - paths: Paths defined in NWB_SBCAT_import_main. The path of interest is
% the code path, which is used to load the dataset of the trials selected
% for the computation of LFP PAC
% - all_units: The output of NWB_SB_extractUnits

fs = filesep;

sample_sub = 26;
sample_ses = 1;


[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sb; cat plot_PAC_neuron.m; python -c "
import scipy.io as s; print(s.loadmat('artif_trials.mat'))"
```

```
Exit code 1
function [figOut] = plot_PAC_neuron(spike_times,datMat,srate,low_fb,HF_steps,tcutEdge)

%% plot_PAC_neuron(spike_times,datMat,srate,low_fb,HF_steps,tcutEdge)
% Plots the data table used to compute the GLMs for PAC neuron selection
%
% Input:
% spike_times:  matrix containing the spike times from a given neuron (samples x trials). The
%               matrix should contain zeros and ones. Ones indicate a spike
%               at a certain sample in a trial.
% datMat:       LFP data for a given channel (samples x trials)
% srate:        sampling rate
% low_fb:       frequency band for the low frequency signal in Hz [lower edge, higher edge];
% HF_steps:     center frequencies for the higher amplitude in Hz [lower edge : stepsize : higher end]
% tcutEdge:     time to cut off at the edges of each trial to prevent filter artifacts in s (full time will be cutoff at the beginning and end of trial;  0 = no cutoff) 
%
% JD 2023

n_phase_bins = 10; 
rng('shuffle')
[... 165 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "PAC neuron" paper/*.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'EOF'
t=open('paper/10.1038-s41586-024-07309-z.txt').read()
import re
for key in ['Selection of PAC neurons','PAC neurons were selected','identify neurons whose','Single-trial PAC','single-trial PAC','Spike-field coherence','SFC was computed']:
    for m in re.finditer(re.escape(key),t):
        print('=====',key,m.start()); print(t[m.start()-200:m.start()+2500]); break
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'EOF'
t=open('paper/10.1038-s41586-024-07309-z.txt').read()
i=t.find('Model 3:',70335); j=t.find('end{document}',i)
k=t.find('PAC neurons were selected')
print(t[j:j+3000])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 - <<'EOF'
t=open('paper/10.1038-s41586-024-07309-z.txt').read()
i=t.find('Selection of PAC neurons')
j=t.find('Noise correlations and population',i)
s=t[i:j]
import re
s=re.sub(r'\\documentclass.*?\\end\{document\}','[EQ]',s,flags=re.S)
print(s[1800:])
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^def \|^    def " entries/000673-daume-2024/sbcat.py
```

```
75:def area_of(location: str) -> str:
86:def hemisphere_of(location: str) -> str:
90:def list_assets(version: str = DANDISET_VERSION) -> list[dict]:
101:def asset_url(asset: dict) -> str:
105:def _open(asset: dict) -> h5py.File:
109:def _str(x) -> str:
113:def load_session(asset: dict) -> dict:
165:def add_trial_columns(tr: pd.DataFrame) -> pd.DataFrame:
176:def load_all(assets: list[dict] | None = None, workers: int = 12) -> list[dict]:
184:def count_in(spikes: np.ndarray, starts: np.ndarray, stops: np.ndarray, closed: bool = False) -> np.ndarray:
191:def maintenance_rates(s: dict, unit: int) -> np.ndarray:
197:def baseline_rates(s: dict, unit: int) -> np.ndarray:
203:def presentations(s: dict) -> tuple[np.ndarray, np.ndarray]:
218:def _t1(d: np.ndarray, axis=-1) -> np.ndarray:
223:def perm_ttest_1samp(d, rng, n_perm: int = N_PERM) -> dict:
237:def perm_ttest_paired(x, y, rng, n_perm: int = N_PERM) -> dict:
245:def _t2(a, b, axis=-1):
252:def perm_ttest_unpaired(a, b, rng, n_perm: int = N_PERM) -> dict:
264:def fdr_bh(p) -> np.ndarray:
277:def _anova_f(groups_sum, groups_n, total_ss, grand_sum, N, k):
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 335,410p entries/000673-daume-2024/sbcat.py; sed -n 785,955p entries/000673-daume-2024/sbcat.py
```

```
def read_lfp(asset: dict) -> tuple[np.ndarray, float, float]:
    """The whole LFP array (samples x channels, microvolts as stored), its rate and start time."""
    import fsspec
    with fsspec.filesystem("http").open(asset_url(asset), "rb", block_size=16 * 2 ** 20, cache_type="readahead") as fh:
        f = h5py.File(fh, "r")
        d = f["acquisition/LFPs/data"]
        st0 = f["acquisition/LFPs/starting_time"]
        x = d[:].astype(np.float32)
        rate, start = float(st0.attrs["rate"]), float(st0[()])
        f.close()
    return x, rate, start


def epochs(x: np.ndarray, rate: float, start: float, onsets: np.ndarray, win=EPOCH) -> np.ndarray:
    """Epochs (trials x samples x channels) from win[0] to win[1] s around each onset."""
    n = int(round((win[1] - win[0]) * rate)) + 1
    i0 = np.round((onsets + win[0] - start) * rate).astype(int)
    idx = i0[:, None] + np.arange(n)[None, :]
    return x[idx]

[... 228 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims/000673; grep -n "^- id:\|^  - id:\|^[a-z_]*:" 10.1038-s41586-024-07309-z.yaml | head -90
```

```
112:schema_version: 2
113:dataset:
116:paper: doi:10.1038/s41586-024-07309-z
117:claims:
118:- id: cohort-counts
144:- id: fig1d-rt-load
167:- id: fig1d-accuracy-load
188:- id: behaviour-overall-accuracy
205:- id: fig2a-theta-gamma-pac
218:- id: fig2b-pac-channel-proportions
251:- id: fig2c-hippocampus-load
269:- id: fig2c-no-load-effect-other-areas
307:- id: edf2b-hippocampus-load-patients
324:- id: edf2c-low-gamma-no-load-effect
334:- id: tables1-slow-fast-theta
358:- id: fig2f-rt-single-trial-pac
388:- id: edf3-hippocampus-pac-controls
412:- id: edf3a-kappa-load
429:- id: edf3e-nesting
451:- id: edf3f-raw-mi-load
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,111p claims/000673/10.1038-s41586-024-07309-z.yaml | sed -n 30,111p; sed -n 388,451p claims/000673/10.1038-s41586-024-07309-z.yaml; sed -n 525,560p claims/000673/10.1038-s41586-024-07309-z.yaml; sed -n 679,830p claims/000673/10.1038-s41586-024-07309-z.yaml
```

```
# pre-SMA, 188 dACC, 206 vmPFC) sorted with OSort, and 1,922 microwire LFP channels (586, 421, 283,
# 325, 307); the LFP was low-passed at 175 Hz and downsampled to 400 Hz after spike waveforms were
# interpolated out. Task: a Sternberg working memory task of 140 trials, 70 load 1 and 70 load 3,
# with pictures from five categories (faces, animals, cars or tools, fruits, landscapes); each
# picture 2 s on screen, then a 2.55 to 2.85 s maintenance period, then a probe (match or
# non-match) answered by button press. The code reads, from each session's trials table, the
# timestamps of fixation, encoding 1 to 3, maintenance, probe and response, the picture IDs of
# encoding 1 to 3 and the probe (the category is the first digit of the picture ID), the load,
# probe_in_out and response_accuracy. The data availability statement names DANDI 000673, which
# the dandiset's title and description match (44 sessions); it should hold every experiment of
# the paper.
#
# General rules for the criteria below.
# (G1) Unless a criterion says otherwise, a claim of an effect is reproduced when the paper's test,
#      run as described, gives p < 0.05 (after the correction the paper applied) in the direction
#      the paper reports, and every expected value is within tolerance; partially reproduced when
#      the test holds and an expected value is out of tolerance; not reproduced when the test does
#      not hold. A claim of absence follows the protocol: the paper's test, as written.
# (G2) Tests. "Two-sided permutation-based t-test" is statcond.m (EEGLAB) with method 'perm',
#      10,000 permutations, paired over neurons, channels, pairs or sessions unless the paper says
[... 314 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000673-daume-2024; python3 -c "
import json
d=json.load(open('reproduce_daume_2024_lfp.ipynb'))
for i in [0,1,2,7,10,13,26,29,37,43]:
    print('#### cell',i); print(''.join(d['cells'][i]['source']))
"
```

```
#### cell 0
# Daume et al. (2024) on dandiset 000673: LFP phase-amplitude coupling

**Paper.** Daume J, Kaminski J, Schjetnan AGP, Salimpour Y, Khan U, Kyzar M, Reed CM, Anderson WS,
Valiante TA, Mamelak AN, Rutishauser U (2024). Control of working memory by phase-amplitude
coupling of human hippocampal neurons. *Nature* 629, 393-401.
[doi:10.1038/s41586-024-07309-z](https://doi.org/10.1038/s41586-024-07309-z).

**Dandiset.** [DANDI:000673](https://dandiarchive.org/dandiset/000673/0.240118.2135), version
0.240118.2135, the version the paper cites (reference 59); see the header of
`reproduce_daume_2024.ipynb` for the later versions.

**Text the claims were written from.** The version of record (PMC11078732) with its Methods,
legends and Supplementary Information, and the paper's code (SBCAT-release-NWB at a25e8cc3).

This notebook tests the claims on LFP phase-amplitude coupling (PAC). Each channel's LFP is
streamed, cut into -0.5 to 3 s epochs around maintenance onset, filtered trial by trial as the
paper's code does, and Tort's modulation index (MI) is z-scored against 200 trial-shuffled
surrogates (`sbcat.py` says where each parameter comes from). Every result is shown under both
readings of the artefact rejection (O1): (a) on the epochs, (b) on whole trials.
[... 223 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 455,790p sbcat.py
```

```
med = np.median(rt[m])
        fast |= m & (rt <= med)
        slow |= m & (rt > med)
    return fast, slow


# ----------------------------------------------------------------------------- PAC engine

PHASE_CENTRES = np.arange(2, 15, 2)          # Methods, PAC; cfc_tort_comodulogram.m defaults
AMP_CENTRES = np.arange(30, 151, 5)
N_BINS = 18
N_SURR = 200
EPOCH_N = 1400                                # -0.5 to 3 s at 400 Hz
CUT = 200                                     # 0.5 s cut at each edge (tcutEdge = 0.5)
THETA = (4, 6)                                # O3: phase centres of theta (3 to 7 Hz)
HIGH_GAMMA = (70, 140)                        # O3: amplitude centres 70 to 140 Hz
LOW_GAMMA = (30, 55)                          # O3: amplitude centres 30 to 55 Hz
SLOW_THETA, FAST_THETA = (2, 4), (6, 8)       # tables1 reading (a)

_KERNELS: dict = {}
[... 314 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; nproc; free -g | head -2; ls .venv* 2>/dev/null | head -3; which python; python -c "import scipy, numpy; print(scipy.__version__)"; sed -n 1,60p tools/entry.py | head -60; cat requirements.in
```

```
Sat Oct 31 12:39:29 UTC 2026
4
               total        used        free      shared  buff/cache   available
Mem:              15           1          12           0           2          14
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import scipy, numpy; print(scipy.__version__)
    ^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'scipy'
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 dev && VIRTUAL_ENV=$TMPDIR/dev uv pip install -q -r entries/000673-daume-2024/requirements.lock.txt 2>&1 | tail -2; $TMPDIR/dev/bin/python -c "
import scipy.io as s; print(s.loadmat('$TMPDIR/sb/artif_trials.mat'))"
```

```
{'__header__': b'MATLAB 5.0 MAT-file, Platform: MACI64, Created on: Fri Nov 10 17:56:55 2023', '__version__': '1.0', '__globals__': [], 'artif_trials': array([[  4],
       [  5],
       [ 10],
       [ 11],
       [ 12],
       [ 22],
       [ 24],
       [ 28],
       [ 31],
       [ 60],
       [ 69],
       [ 70],
       [ 71],
       [ 79],
       [ 88],
       [117],
       [118]], dtype=uint8)}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000673-daume-2024; time $TMPDIR/dev/bin/python - <<'EOF'
import numpy as np, sbcat, scipy.io
A=sbcat.list_assets()
a=[x for x in A if 'sub-26' in x['path']]; print([x['path'] for x in a])
s=sbcat.load_session(a[0]) if False else None
S=sbcat.load_all(a)
s=S[0]
x,rate,start=sbcat.read_lfp(s['asset'])
print(x.shape, len(s['lfp_electrodes']))
tr=s['trials']; T=len(tr)
on=tr.timestamps_Maintenance.to_numpy(); i0=np.round((on-0.5-start)*rate).astype(int)
fix=np.round((tr.timestamps_FixationCross.to_numpy()-start)*rate).astype(int)
resp=np.round((tr.timestamps_Response.to_numpy()-start)*rate).astype(int)
paper=set(scipy.io.loadmat('/tmp/x.mat' if False else __import__('os').environ['TMPDIR']+'/sb/artif_trials.mat')['artif_trials'].ravel()-1)
el=s['electrodes'].iloc[s['lfp_electrodes']].reset_index(drop=True)
for ch in range(x.shape[1]):
    d=x[i0[:,None]+np.arange(1400)[None,:],ch].astype(float)
    ma=sbcat.artefact_mask([d[t] for t in range(T)])
    mb=sbcat.artefact_mask([x[fix[t]:resp[t]+1,ch].astype(float) for t in range(T)])
    ra,rb=set(np.where(~ma)[0]),set(np.where(~mb)[0])
    print(ch, el.area[ch], len(ra), len(rb), len(ra&paper), len(rb&paper), len(paper))
EOF
```

```
['sub-26/sub-26_ses-1_ecephys+image.nwb', 'sub-26/sub-26_ses-2_ecephys+image.nwb']
(617421, 36) 36
0 hippocampus 17 39 4 4 17
1 hippocampus 25 49 2 4 17
2 hippocampus 15 27 2 3 17
3 hippocampus 8 19 1 3 17
4 hippocampus 18 41 2 3 17
5 hippocampus 3 4 1 1 17
6 hippocampus 5 19 1 4 17
7 amygdala 2 4 2 2 17
8 hippocampus 8 19 3 5 17
9 hippocampus 9 17 4 5 17
10 hippocampus 5 16 3 4 17
11 hippocampus 5 13 1 1 17
12 hippocampus 9 22 2 5 17
13 hippocampus 7 15 2 4 17
14 hippocampus 4 11 2 3 17
15 hippocampus 32 61 4 10 17
16 hippocampus 3 8 3 3 17
17 hippocampus 23 43 4 6 17
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 277,334p sbcat.py; sed -n 407,445p sbcat.py; python3 -c "
import json
d=json.load(open('reproduce_daume_2024.ipynb'))
for i in [22,25,33,42]:
    print('#### cell',i); print(''.join(d['cells'][i]['source']))
"; sed -n 608,660p ../../claims/000673/10.1038-s41586-024-07309-z.yaml
```

```
def _anova_f(groups_sum, groups_n, total_ss, grand_sum, N, k):
    ss_between = (groups_sum ** 2 / groups_n).sum(-1) - grand_sum ** 2 / N
    ss_within = total_ss - (groups_sum ** 2 / groups_n).sum(-1)
    return (ss_between / (k - 1)) / (ss_within / (N - k))


def category_selection(rates: np.ndarray, cats: np.ndarray, rng, n_perm: int = 2000,
                       label_sets: np.ndarray | None = None) -> dict:
    """Category neuron test of NWB_calcSelective_SB.m for one neuron.

    rates: rate per presentation; cats: category codes. If label_sets (L x N) is given, the test
    is also applied to each relabelling (the shuffled-label null); the permutation null of each
    statistic depends only on the values and group sizes, so it is drawn once and reused.
    """
    rates = np.asarray(rates, float)
    N = len(rates)
    ucat = np.unique(cats)
    k = len(ucat)
    total_ss = float((rates ** 2).sum())
    grand = float(rates.sum())
[... 219 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
t=open('paper/10.1038-s41586-024-07309-z.txt').read()
import re
for key in ['Extended Data Fig. 3','bycycle','peak frequenc','phase–phase']:
    for m in list(re.finditer(re.escape(key),t))[:6]:
        print('=====',key,m.start()); print(t[max(0,m.start()-300):m.start()+700].replace('\n',' '))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; VIRTUAL_ENV=$TMPDIR/dev uv pip install -q bycycle 2>&1 | tail -2; $TMPDIR/dev/bin/python -c "
import bycycle, neurodsp; print(bycycle.__version__, neurodsp.__version__)
from bycycle import compute_features
import numpy as np, time
fs=400; t=np.arange(1400)/fs; sig=np.sin(2*np.pi*5*t)+0.3*np.random.randn(1400)
t0=time.time()
for i in range(50): df=compute_features(sig, fs, (3,7))
print((time.time()-t0)/50); print(df.columns.tolist()); print(df[['sample_peak','time_rdsym','time_ptsym','is_burst']].head())
"
```

```
Exit code 1
Sat Oct 31 12:40:51 UTC 2026
Traceback (most recent call last):
  File "<string>", line 3, in <module>
    from bycycle import compute_features
ImportError: cannot import name 'compute_features' from 'bycycle' (/tmp/claude-1001/dev/lib/python3.13/site-packages/bycycle/__init__.py)
1.2.0 2.3.0
```

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python -c "
import bycycle; print(dir(bycycle))
from bycycle.features import compute_features
import numpy as np, time
fs=400; t=np.arange(1400)/fs; sig=np.sin(2*np.pi*5*t)+0.3*np.random.randn(1400)
t0=time.time()
for i in range(20): df=compute_features(sig, fs, (3,7))
print((time.time()-t0)/20); print(df.columns.tolist()); print(df[['sample_peak','time_rdsym','time_ptsym','is_burst']].head())
" 2>&1 | tail -12
```

```
warnings.warn("""
Traceback (most recent call last):
  File "<string>", line 7, in <module>
    for i in range(20): df=compute_features(sig, fs, (3,7))
                           ~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/bycycle/features/features.py", line 148, in compute_features
    df_features = detect_bursts_cycles(df_features, **threshold_kwargs)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/bycycle/burst/cycle.py", line 96, in detect_bursts_cycles
    is_burst[0] = False
    ~~~~~~~~^^^
ValueError: assignment destination is read-only
['Bycycle', 'BycycleGroup', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', 'burst', 'cyclepoints', 'features', 'group', 'objs', 'plts', 'utils', 'version']
```

**Agent calls Bash**

```bash
sed -n 60,110p $TMPDIR/dev/lib/python3.13/site-packages/bycycle/burst/cycle.py; grep -n "pandas" entries/000673-daume-2024/requirements.lock.txt
```

```
Notes
    -----
    * The first and last period cannot be considered oscillating if the consistency measures are
      used.

    Examples
    --------
    Apply thresholding for consistency burst detection:

    >>> from bycycle.features import compute_burst_features, compute_shape_features
    >>> from neurodsp.sim import sim_bursty_oscillation
    >>> fs = 500
    >>> sig = sim_bursty_oscillation(10, fs, freq=10)
    >>> df_shapes = compute_shape_features(sig, fs, f_range=(8, 12))
    >>> df_burst = compute_burst_features(df_shapes, sig)
    >>> df_burst = detect_bursts_cycles(df_burst)
    """

    # Ensure arguments are within valid ranges
    check_param_range(amp_fraction_threshold, 'amp_fraction_threshold', (0, 1))
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/dev/bin/python - <<'EOF' 2>&1 | grep -v Warn | tail -12
import numpy as np, time, warnings
warnings.filterwarnings("ignore")
import bycycle.features.features as bf
import bycycle.burst.cycle as bc
src_fn = bc.detect_bursts_cycles
def patched(df, amp_fraction_threshold=0., amp_consistency_threshold=.5, period_consistency_threshold=.5, monotonicity_threshold=.8, min_n_cycles=3):
    ok = ((df['amp_fraction'] > amp_fraction_threshold) & (df['amp_consistency'] > amp_consistency_threshold)
          & (df['period_consistency'] > period_consistency_threshold) & (df['monotonicity'] > monotonicity_threshold)).to_numpy().copy()
    ok[0] = ok[-1] = False
    df['is_burst'] = bc.check_min_burst_cycles(ok, min_n_cycles=min_n_cycles)
    return df
import inspect; print(inspect.signature(src_fn))
bf.detect_bursts_cycles = patched
fs=400; t=np.arange(1400)/fs; sig=np.sin(2*np.pi*5*t)+0.5*np.random.randn(1400)
t0=time.time()
for i in range(20): df=bf.compute_features(sig, fs, (3,7))
print((time.time()-t0)/20); print(df.columns.tolist()); print(df[['sample_peak','time_rdsym','time_ptsym','is_burst']].head())
EOF
```

```
(df_features, amp_fraction_threshold=0.0, amp_consistency_threshold=0.5, period_consistency_threshold=0.5, monotonicity_threshold=0.8, min_n_cycles=3)
0.008319246768951415
['amp_fraction', 'amp_consistency', 'period_consistency', 'monotonicity', 'period', 'time_peak', 'time_trough', 'volt_peak', 'volt_trough', 'time_decay', 'time_rise', 'volt_decay', 'volt_rise', 'volt_amp', 'time_rdsym', 'time_ptsym', 'band_amp', 'sample_peak', 'sample_last_zerox_decay', 'sample_zerox_decay', 'sample_zerox_rise', 'sample_last_trough', 'sample_next_trough', 'is_burst']
   sample_peak  time_rdsym  time_ptsym  is_burst
0           92    0.418919    0.519481     False
1          178    0.505882    0.378378     False
2          263    0.530864    0.466667     False
3          341    0.500000    0.562500     False
4          428    0.635135    0.493827     False
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000673-daume-2024/sbcat.py",
 "old_string": "        avg = np.mean(windows, 0)\n        c, w = half, 9                                 # 22.5 ms each side (45 ms window)\n        seg = avg[c - w - 1:c + w + 2]\n        n_max = int(((seg[1:-1] > seg[:-2]) & (seg[1:-1] > seg[2:])).sum())\n        out[name] = {\"nested\": n_max >= 3, \"n_maxima\": n_max, \"n_windows\": len(windows)}\n    return out",
 "new_string": "        avg = np.mean(windows, 0)\n        n_max = local_maxima(avg)\n        out[name] = {\"nested\": n_max >= 3, \"n_maxima\": n_max, \"n_windows\": len(windows), \"avg\": avg.astype(np.float32)}\n    return out\n\n\ndef local_maxima(avg: np.ndarray, w: int = 9) -> int:\n    \"\"\"Local maxima (samples larger than both neighbours) of an averaged 201-sample window within\n    w samples of its centre; w = 9 is 22.5 ms each side, the 45 ms of the Methods.\"\"\"\n    c = (len(avg) - 1) // 2\n    seg = avg[c - w - 1:c + w + 2]\n    return int(((seg[1:-1] > seg[:-2]) & (seg[1:-1] > seg[2:])).sum())\n\n\n# Extended Data Fig. 3 controls (edf3-hippocampus-pac-controls)\nFINE_PHASE = np.arange(3.0, 7.01, 0.5)       # Extended Data Fig. 3h: phase steps of 0.5 Hz, theta band\nFINE_AMPS = AMP_CENTRES[(AMP_CENTRES >= HIGH_GAMMA[0]) & (AMP_CENTRES <= HIGH_GAMMA[1])]\n\n\ndef _patch_bycycle():\n    \"\"\"bycycle 1.2 writes into a read-only array under pandas 3 (copy-on-write); this replaces its\n    detect_bursts_cycles by the same rule on a writable copy (defaults unchanged).\"\"\"\n    import bycycle.burst.cycle as bc\n    import bycycle.features.features as bf\n\n    def detect(df, amp_fraction_threshold=0.0, amp_consistency_threshold=0.5,\n               period_consistency_threshold=0.5, monotonicity_threshold=0.8, min_n_cycles=3):\n        ok = ((df[\"amp_fraction\"] > amp_fraction_threshold) & (df[\"amp_consistency\"] > amp_consistency_threshold)\n              & (df[\"period_consistency\"] > period_consistency_threshold)\n              & (df[\"monotonicity\"] > monotonicity_threshold)).to_numpy().copy()\n        ok[0] = ok[-1] = False\n        df[\"is_burst\"] = bc.check_min_burst_cycles(ok, min_n_cycles=min_n_cycles)\n        return df\n    bf.detect_bursts_cycles = detect\n    return bf.compute_features\n\n\ndef theta_cycle_features(data: np.ndarray, srate: float = FS_LFP) -> np.ndarray:\n    \"\"\"Per trial (rows of the -0.5 to 3 s epochs): sums and counts of bycycle's rise-decay\n    (time_rdsym) and peak-trough (time_ptsym) symmetry over cycles with their peak in 0 to 2.5 s,\n    for burst cycles (default thresholds) and for all cycles. Columns: rd_burst, pt_burst,\n    n_burst, rd_all, pt_all, n_all. bycycle with f_range 3-7 Hz and its default settings\n    (criterion of edf3-hippocampus-pac-controls).\"\"\"\n    import warnings\n    compute_features = _patch_bycycle()\n    out = np.zeros((data.shape[0], 6))\n    with warnings.catch_warnings():\n        warnings.simplefilter(\"ignore\")\n        for t in range(data.shape[0]):\n            try:\n                df = compute_features(data[t], srate, (3, 7))\n            except Exception:\n                continue\n            inw = (df.sample_peak >= CUT) & (df.sample_peak < EPOCH_N - CUT)\n            b = inw & df.is_burst.astype(bool)\n            out[t] = [df.time_rdsym[b].sum(), df.time_ptsym[b].sum(), b.sum(),\n                      df.time_rdsym[inw].sum(), df.time_ptsym[inw].sum(), inw.sum()]\n    return out\n\n\ndef fine_bin_sums(tf, data_n: int) -> tuple[np.ndarray, np.ndarray]:\n    \"\"\"Per-trial bin sums of high-gamma amplitude over theta phase for the phase centres of\n    FINE_PHASE (2 Hz bandwidth) and the amplitude centres of FINE_AMPS (bandwidth twice the phase\n    centre), as the comodulogram (Extended Data Fig. 3h). Returns sums (trials x phases x bins x\n    amps) and counts (trials x phases x bins).\"\"\"\n    T = data_n\n    sums = np.zeros((T, len(FINE_PHASE), N_BINS, len(FINE_AMPS)), np.float32)\n    counts = np.zeros((T, len(FINE_PHASE), N_BINS), np.float32)\n    for i, p in enumerate(FINE_PHASE):\n        ph = np.angle(tf.analytic(p - 1, p + 1))[:, CUT:EPOCH_N - CUT]\n        bins = np.clip(np.digitize(np.degrees(ph), np.linspace(-180, 180, N_BINS + 1)) - 1, 0, N_BINS - 1)\n        oh = (bins[:, :, None] == np.arange(N_BINS)[None, None, :]).astype(np.float32)\n        counts[:, i] = oh.sum(1)\n        for j, a in enumerate(FINE_AMPS):\n            am = np.abs(tf.analytic(a - p, a + p))[:, CUT:EPOCH_N - CUT].astype(np.float32)\n            sums[:, i, :, j] = np.einsum(\"tsb,ts->tb\", oh, am)\n    return sums, counts\n\n\nPPC_PAIRS = [(p, a) for p in THETA for a in FINE_AMPS]\n\n\ndef ppc_pair_sums(tf) -> np.ndarray:\n    \"\"\"Per trial, the sum over 0 to 2.5 s of exp(i (n theta_p - phi_a)) for each phase centre p of\n    THETA and amplitude centre a of 70 to 140 Hz, n = round(a / p) (the second reading of the\n    phase-phase coupling ratio: each phase and amplitude centre pair of O3). Trials x pairs.\"\"\"\n    out = []\n    for p, a in PPC_PAIRS:\n        th = np.angle(tf.analytic(p - 1, p + 1))[:, CUT:EPOCH_N - CUT]\n        ga = np.angle(tf.analytic(a - p, a + p))[:, CUT:EPOCH_N - CUT]\n        out.append(np.exp(1j * (int(round(a / p)) * th - ga)).sum(1))\n    return np.array(out).T.astype(np.complex64)"
}
```

```
The file entries/000673-daume-2024/sbcat.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000673-daume-2024/sbcat.py",
 "old_string": "                \"masks\": masks, \"readings\": {}}\n        for reading in [\"a\", \"b\"]:",
 "new_string": "                \"masks\": masks, \"readings\": {}}\n        if el.area[ch] == \"hippocampus\":\n            # Extended Data Fig. 3 controls, per correct trial (no random draws)\n            info[\"cycles\"] = theta_cycle_features(data[cidx])\n            info[\"ppc_pairs\"] = ppc_pair_sums(tfc)\n            fine_sums, fine_counts = fine_bin_sums(tfc, len(cidx))\n        for reading in [\"a\", \"b\"]:"
}
```

```
The file entries/000673-daume-2024/sbcat.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000673-daume-2024/sbcat.py",
 "old_string": "                for name, trs in [(\"l1\", l1s), (\"l3\", l3s)]:\n                    out[f\"ppc_{name}\"] = float(np.abs(np.mean(np.exp(1j * (21 * th[trs] - gph[trs])))))",
 "new_string": "                for name, trs in [(\"l1\", l1s), (\"l3\", l3s)]:\n                    out[f\"ppc_{name}\"] = float(np.abs(np.mean(np.exp(1j * (21 * th[trs] - gph[trs])))))\n                    # raw MI over the fine phase grid (Extended Data Fig. 3h), phases x amplitudes\n                    out[f\"fine_mi_{name}\"] = mi_from_bins(fine_sums[trs].sum(0).transpose(0, 1, 2),\n                                                          fine_counts[trs].sum(0))"
}
```

```
The file entries/000673-daume-2024/sbcat.py has been updated successfully.
```

**Agent calls Bash**

```bash
cd entries/000673-daume-2024 && python3 - <<'EOF'
p='sbcat.py'; s=open(p).read()
s=s.replace("mi_from_bins(fine_sums[trs].sum(0).transpose(0, 1, 2),\n                                                          fine_counts[trs].sum(0))","mi_from_bins(fine_sums[trs].sum(0), fine_counts[trs].sum(0))")
old='''    out = []
    for p, a in PPC_PAIRS:
        th = np.angle(tf.analytic(p - 1, p + 1))[:, CUT:EPOCH_N - CUT]
        ga'''
new='''    out, th_of = [], {}
    for p, a in PPC_PAIRS:
        if p not in th_of:
            th_of[p] = np.angle(tf.analytic(p - 1, p + 1))[:, CUT:EPOCH_N - CUT]
        th = th_of[p]
        ga'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
grep -n "fine_mi_" sbcat.py
```

```
856:                    out[f"fine_mi_{name}"] = mi_from_bins(fine_sums[trs].sum(0), fine_counts[trs].sum(0))
```

**Agent**

Now timing one session (sub-26 ses-1, 36 channels, mostly hippocampal) with the old and new code paths.

**Agent calls Bash**

```bash
git stash -q && cp sbcat.py $TMPDIR/sbcat_old.py && git stash pop -q && git diff --stat; time $TMPDIR/dev/bin/python - <<'EOF'
import numpy as np, time, sys, importlib.util
import sbcat
A=sbcat.list_assets()
S=sbcat.load_all([x for x in A if 'sub-26_ses-1' in x['path']])
s=S[0]
print(s['electrodes'].iloc[s['lfp_electrodes']].area.value_counts().to_dict())
t0=time.time(); r=sbcat.process_session_lfp(s, 201, 0); print('new', time.time()-t0)
spec=importlib.util.spec_from_file_location('old', __import__('os').environ['TMPDIR']+'/sbcat_old.py'); old=importlib.util.module_from_spec(spec); spec.loader.exec_module(old)
t0=time.time(); r0=old.process_session_lfp(s, 201, 0); print('old', time.time()-t0)
c=[c for c in r['channels'] if c['area']=='hippocampus'][0]; c0=[c for c in r0['channels'] if c['area']=='hippocampus'][0]
print(np.allclose(c['readings']['a']['z_l1'][4], c0['readings']['a']['z_l1'][4]))
o=c['readings']['a']; print(o['fine_mi_l1'].shape, c['cycles'][:3], c['ppc_pairs'].shape, o['nesting']['peak']['n_maxima'])
import pickle; pickle.dump(r, open(__import__('os').environ['TMPDIR']+'/r26.pkl','wb'))
EOF
```

```
entries/000673-daume-2024/sbcat.py | 103 +++++++++++++++++++++++++++++++++++--
 1 file changed, 99 insertions(+), 4 deletions(-)
{'hippocampus': 28, 'amygdala': 8}
new 158.2677137851715
old 95.79698753356934
True
(9, 15) [[ 0.          0.          0.          5.64614806  5.00681792 10.        ]
 [ 0.          0.          0.          4.98491306  4.83719491 10.        ]
 [ 0.          0.          0.          5.08212327  5.64116926 10.        ]] (140, 30) 3

real	4m17.410s
user	10m18.577s
sys	0m5.631s
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='sbcat.py'; s=open(p).read()
reps=[
("def process_session_lfp(s: dict, seed: int, si: int) -> dict:","def process_session_lfp(s: dict, seed: int, si: int, controls: bool = False, areas=None) -> dict:"),
("""    (O2), and MI is computed for both loads together ('all') and each load.
    \"\"\"""","""    (O2), and MI is computed for both loads together ('all') and each load. Each channel's random
    draws are seeded by (seed, session, channel, reading), so a channel gives the same result
    whichever other channels are processed. `areas` restricts the channels; `controls` adds the
    Extended Data Fig. 3 controls of hippocampal channels (theta cycles, phase-phase coupling of
    each centre pair, the 0.5 Hz phase grid).
    \"\"\""""),
("""    for ch in range(E.shape[2]):
        data = E[:, :, ch].astype(np.float64)""","""    for ch in range(E.shape[2]):
        if areas is not None and el.area[ch] not in areas:
            continue
        data = E[:, :, ch].astype(np.float64)"""),
("""        if el.area[ch] == "hippocampus":
            # Extended Data Fig. 3 controls""","""        if controls and el.area[ch] == "hippocampus":
            # Extended Data Fig. 3 controls"""),
("""                    # raw MI over the fine phase grid (Extended Data Fig. 3h), phases x amplitudes
                    out[f"fine_mi_{name}"]""","""                    # raw MI over the fine phase grid (Extended Data Fig. 3h), phases x amplitudes
                    if controls:
                        out[f"fine_mi_{name}"]"""),
("""def _lfp_job(args):
    s, seed, si = args
    return process_session_lfp(s, seed, si)""","""def _lfp_job(args):
    s, seed, si, controls, areas = args
    return process_session_lfp(s, seed, si, controls, areas)"""),
("""def run_all_lfp(sessions: list[dict], seed: int, workers: int = 6) -> list[dict]:
    \"\"\"process_session_lfp on every session with LFP, in parallel processes (largest first).\"\"\"
    from concurrent.futures import ProcessPoolExecutor
    jobs = [(s, seed, si) for si, s in enumerate(sessions) if len(s["lfp_electrodes"])]""","""def run_all_lfp(sessions: list[dict], seed: int, workers: int = 6, controls: bool = False, areas=None) -> list[dict]:
    \"\"\"process_session_lfp on every session with LFP (in `areas`, if given), in parallel processes
    (largest first).\"\"\"
    from concurrent.futures import ProcessPoolExecutor
    jobs = [(s, seed, si, controls, areas) for si, s in enumerate(sessions) if len(s["lfp_electrodes"])
            and (areas is None or s["electrodes"].area.iloc[s["lfp_electrodes"]].isin(areas).any())]"""),
]
for a,b in reps:
    assert a in s, a[:60]; s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "fine_mi_\|if controls" sbcat.py; sed -n '/if controls:/,+2p' sbcat.py
```

```
807:        if controls and el.area[ch] == "hippocampus":
862:                    if controls:
863:                        out[f"fine_mi_{name}"] = mi_from_bins(fine_sums[trs].sum(0), fine_counts[trs].sum(0))
                    if controls:
                        out[f"fine_mi_{name}"] = mi_from_bins(fine_sums[trs].sum(0), fine_counts[trs].sum(0))
            info["readings"][reading] = out
```

**Agent calls Bash**

```bash
date -u; python3 -c "
import json
d=json.load(open('reproduce_daume_2024_lfp.ipynb'))
for i in [4,5,9,11,14,15,17,27,36,38,41,42,44,45]:
    print('#### cell',i); print(''.join(d['cells'][i]['source']))
"
```

```
Sat Oct 31 12:46:58 UTC 2026
#### cell 4
one = ch[ch.reading == "a"]
print("LFP channels by area:", one.area.value_counts().reindex(sbcat.AREAS).to_dict(), "; total", len(one))
info = pd.DataFrame([{"path": r["path"], "lfp_samples": r["lfp_shape"][0], "channels": r["lfp_shape"][1],
                      "lfp_s": r["lfp_shape"][0] / 400, "task_end_s": S[r["session"]]["trials"].stop_time.max()} for r in R])
print("LFP length minus the end of the last trial (s): min %.1f, max %.1f" % ((info.lfp_s - info.task_end_s).min(), (info.lfp_s - info.task_end_s).max()))
print("LFP rate and unit as stored:", {(s["lfp_info"]["rate"], s["lfp_info"]["unit"], s["lfp_info"]["conversion"]) for s in S if s["lfp_info"]})
sd = pd.Series([c["sd_uV"] for r in R for c in r["channels"]])
p99 = pd.Series([c["p99_abs_uV"] for r in R for c in r["channels"]])
print("per-channel s.d. of the epochs (stored units): median %.1f, range %.2f to %.1f; 99th percentile of |LFP|: median %.1f, max %.1f" % (
    sd.median(), sd.min(), sd.max(), p99.median(), p99.max()))
for rd in READINGS:
    d = ch[ch.reading == rd]
    rem = d.n_trials - d.kept_trials
    print(f"reading {rd}: trials removed per channel {rem.mean():.1f} +/- {rem.std():.1f} ({100 * rem.sum() / d.n_trials.sum():.1f}%); "
          f"trials per load after subsampling: median {d.n_per_load.median():.0f}, range {d.n_per_load.min()} to {d.n_per_load.max()}; "
          f"channels with fewer than 3 per load (left out): {int((d.n_per_load < 3).sum())}")
print("paper: 20.4 +/- 13.9 trials (14.6%) removed per wire, with visual inspection")
fp = pd.Series({r["path"]: r["lfp_fingerprint"] for r in R})
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='sbcat.py'; s=open(p).read()
old='''    key = el.location.astype(str) + "|" + el.x.round(2).astype(str) + "|" + el.y.round(2).astype(str) + "|" + el.z.round(2).astype(str)
'''
new='''    key = bundle_keys(el)
'''
assert old in s; s=s.replace(old,new)
old2='''def process_session_pac_neurons('''
new2='''def bundle_keys(el: pd.DataFrame) -> pd.Series:
    """Bundle of each electrode: its location and coordinates (the files name no bundle)."""
    return el.location.astype(str) + "|" + el.x.round(2).astype(str) + "|" + el.y.round(2).astype(str) + "|" + el.z.round(2).astype(str)


def process_session_pac_neurons('''
s=s.replace(old2,new2,1); open(p,'w').write(s)
EOF
time $TMPDIR/dev/bin/python - <<'EOF'
import numpy as np, pandas as pd, pickle, os, time, warnings
warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
import sbcat
A=sbcat.list_assets()
S=sbcat.load_all([x for x in A if 'sub-26_ses-1' in x['path']])
r=pickle.load(open(os.environ['TMPDIR']+'/r26.pkl','rb')); r['session']=0
for c in r['channels']: c['session']=0
t0=time.time(); cat_table,_=sbcat.category_table(S, seed=103); print('cat', time.time()-t0)
HG = np.where((sbcat.AMP_CENTRES >= 70) & (sbcat.AMP_CENTRES <= 140))[0]
def zhg(o): return float(np.mean([o["z_all"][p][HG].mean() for p in sbcat.THETA]))
cat = cat_table[cat_table.is_category & cat_table.area.isin(sbcat.MTL)].reset_index(drop=True)
rates = sbcat.trial_rates(S, cat)
print(len(cat))
rows=[]
for rd in ["a"]:
    parts=[]
    for i,u in cat.iterrows():
        s=S[u.session]; keys=sbcat.bundle_keys(s["electrodes"]); k=keys[u.electrode]
        on=s["trials"].timestamps_Maintenance.to_numpy()
        sc_all=sbcat.count_in(s["spikes"][u.unit], on, on+2.5)
        for c in r["channels"]:
            o=c["readings"][rd]
            if o is None or keys[s["lfp_electrodes"][c["channel"]]]!=k or zhg(o)<=1.64: continue
            idx=c["trial_index"]; keep=c["masks"][rd][idx]
            st=c["st_thetaHG"][keep]
            parts.append(pd.DataFrame({"pac_a":st,"pac_b":(st-np.nanmean(st))/np.nanstd(st),"sc":sc_all[idx][keep],
               "load":s["trials"].load.to_numpy()[idx][keep].astype(str),"pref":rates[i]["pref"][idx][keep],
               "patient":u.subject,"pair":f"{u.session}_{u.unit}_{c['channel']}","area":u.area}))
    df=pd.concat(parts).dropna()
    print(df.groupby('area').pair.nunique())
    for a in ["hippocampus"]:
        for tr in ["all","preferred"]:
            d=df[(df.area==a)&((tr=="all")|df.pref)]
            for o5 in "ab":
                t0=time.time()
                m=smf.mixedlm(f"pac_{o5} ~ sc * load", d, groups="patient", vc_formula={"pair":"0 + C(pair)"}).fit(reml=True)
                print(a,tr,o5,len(d),m.params["sc"],m.tvalues["sc"],m.pvalues["sc"],time.time()-t0)
EOF
```

```
Exit code 1
cat 1.6576941013336182
11
area
amygdala       10
hippocampus    17
Name: pair, dtype: int64
Traceback (most recent call last):
  File "<stdin>", line 37, in <module>
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/statsmodels/regression/mixed_linear_model.py", line 2384, in fit
    rslt = super().fit(
        start_params=packed,
    ...<2 lines>...
        **fit_kwargs,
    )
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/statsmodels/base/model.py", line 610, in fit
    xopt, retvals, optim_settings = optimizer._fit(
                                    ~~~~~~~~~~~~~~^
        f,
        ^^
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/f3h.py <<'EOF'
import numpy as np, pandas as pd, pickle, os, time, warnings
warnings.filterwarnings("ignore")
import statsmodels.formula.api as smf
import sbcat
A=sbcat.list_assets()
S=sbcat.load_all([x for x in A if 'sub-26_ses-1' in x['path']])
r=pickle.load(open(os.environ['TMPDIR']+'/r26.pkl','rb')); r['session']=0
for c in r['channels']: c['session']=0
cat_table,_=sbcat.category_table(S, seed=103)
HG = np.where((sbcat.AMP_CENTRES >= 70) & (sbcat.AMP_CENTRES <= 140))[0]
def zhg(o): return float(np.mean([o["z_all"][p][HG].mean() for p in sbcat.THETA]))
cat = cat_table[cat_table.is_category & cat_table.area.isin(sbcat.MTL)].reset_index(drop=True)
rates = sbcat.trial_rates(S, cat)
for rd in ["a"]:
    parts=[]
    for i,u in cat.iterrows():
        s=S[u.session]; keys=sbcat.bundle_keys(s["electrodes"]); k=keys[u.electrode]
        on=s["trials"].timestamps_Maintenance.to_numpy()
        sc_all=sbcat.count_in(s["spikes"][u.unit], on, on+2.5)
        for c in r["channels"]:
            o=c["readings"][rd]
            if o is None or keys[s["lfp_electrodes"][c["channel"]]]!=k or zhg(o)<=1.64: continue
            idx=c["trial_index"]; keep=c["masks"][rd][idx]
            st=c["st_thetaHG"][keep]
            parts.append(pd.DataFrame({"pac_a":st,"pac_b":(st-np.nanmean(st))/np.nanstd(st),"sc":sc_all[idx][keep],
               "load":s["trials"].load.to_numpy()[idx][keep].astype(str),"pref":rates[i]["pref"][idx][keep],
               "patient":u.subject,"pair":f"{u.session}_{u.unit}_{c['channel']}","area":u.area}))
    df=pd.concat(parts).dropna().reset_index(drop=True)
    print(df.groupby('area').pair.nunique())
    for a in ["hippocampus"]:
        for tr in ["all","preferred"]:
            d=df[(df.area==a)&((tr=="all")|df.pref)].reset_index(drop=True)
            for o5 in "ab":
                t0=time.time()
                m=smf.mixedlm(f"pac_{o5} ~ sc * load", d, groups="patient", vc_formula={"pair":"0 + C(pair)"}).fit(reml=True)
                print(a,tr,o5,len(d),m.params["sc"],m.tvalues["sc"],m.pvalues["sc"],time.time()-t0)
EOF
$TMPDIR/dev/bin/python $TMPDIR/f3h.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/f3h.py", line 4, in <module>
    import sbcat
ModuleNotFoundError: No module named 'sbcat'
```

**Agent calls Bash**

```bash
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/f3h.py
```

```
/tmp/claude-1001/f3h.py:35: ConvergenceWarning: The MLE may be on the boundary of the parameter space.
  m=smf.mixedlm(f"pac_{o5} ~ sc * load", d, groups="patient", vc_formula={"pair":"0 + C(pair)"}).fit(reml=True)
/tmp/claude-1001/dev/lib/python3.13/site-packages/statsmodels/base/model.py:589: SingularMatrixWarning: Random effects covariance is singular
  return -self.score(params, *args) / nobs
/tmp/claude-1001/dev/lib/python3.13/site-packages/statsmodels/base/model.py:589: SingularMatrixWarning: Random effects covariance is singular
  return -self.score(params, *args) / nobs
/tmp/claude-1001/dev/lib/python3.13/site-packages/statsmodels/base/model.py:589: SingularMatrixWarning: Random effects covariance is singular
  return -self.score(params, *args) / nobs
/tmp/claude-1001/dev/lib/python3.13/site-packages/statsmodels/base/model.py:589: SingularMatrixWarning: Random effects covariance is singular
  return -self.score(params, *args) / nobs
/tmp/claude-1001/dev/lib/python3.13/site-packages/statsmodels/base/model.py:589: SingularMatrixWarning: Random effects covariance is singular
  return -self.score(params, *args) / nobs
/tmp/claude-1001/dev/lib/python3.13/site-packages/statsmodels/base/model.py:589: SingularMatrixWarning: Random effects covariance is singular
  return -self.score(params, *args) / nobs
/tmp/claude-1001/dev/lib/python3.13/site-packages/statsmodels/base/model.py:589: SingularMatrixWarning: Random effects covariance is singular
  return -self.score(params, *args) / nobs
/tmp/claude-1001/dev/lib/python3.13/site-packages/statsmodels/base/model.py:589: SingularMatrixWarning: Random effects covariance is singular
  return -self.score(params, *args) / nobs
/tmp/claude-1001/dev/lib/python3.13/site-packages/statsmodels/base/model.py:589: SingularMatrixWarning: Random effects covariance is singular
  return -self.score(params, *args) / nobs
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 218,264p sbcat.py
```

```
def _t1(d: np.ndarray, axis=-1) -> np.ndarray:
    n = d.shape[axis]
    return d.mean(axis) / (d.std(axis, ddof=1) / np.sqrt(n))


def perm_ttest_1samp(d, rng, n_perm: int = N_PERM) -> dict:
    """Two-sided sign-flip permutation t-test of d against 0 (paired test of differences)."""
    d = np.asarray(d, float)
    d = d[np.isfinite(d)]
    n = len(d)
    if n < 2:
        return {"n": n, "t": np.nan, "df": n - 1, "p": np.nan, "mean": float(d.mean()) if n else np.nan}
    t_obs = float(_t1(d))
    signs = rng.choice([-1.0, 1.0], size=(n_perm, n))
    t_perm = _t1(signs * d[None, :], axis=1)
    p = (np.sum(np.abs(t_perm) >= abs(t_obs)) + 1) / (n_perm + 1)
    return {"n": n, "t": t_obs, "df": n - 1, "p": float(p), "mean": float(d.mean())}


def perm_ttest_paired(x, y, rng, n_perm: int = N_PERM) -> dict:
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import nbformat, yaml; print('ok')"; python3 -c "
import json
d=json.load(open('reproduce_daume_2024_lfp.ipynb'))
print(d['metadata']); print(d['cells'][40]['source'] if isinstance(d['cells'][40]['source'],str) else ''.join(d['cells'][40]['source'])[:600])"
```

```
ok
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
rng = np.random.default_rng(308)
freqs = R[0]["freqs"]
for rd in READINGS:
    d = ch[(ch.reading == rd) & (ch.area == "hippocampus") & (ch.n_per_load >= 3)]
    for fr_name, (f0, f1) in [("2-150 Hz", (2, 150)), ("30-150 Hz", (30, 150))]:
        fm = (freqs >= f0) & (freqs <= f1) & ~((freqs >= 58) & (freqs <= 62)) & ~((freqs >= 118) & (freqs <= 122))
        sl = {}
        for L in (1, 3):
            sl[L] = np.array([np.polyfit(np.log10(freqs[fm]), np.log10(chan_index[(r.session, r.channel)]["readings"][rd][f"psd_l{L}"][fm]), 1)[0]
                              for r in d.itertuples()])
```

**Agent**

Now writing the new controls notebook (hippocampal channels only, so the LFP notebook stays under its time limit).

**Agent calls Bash**

```bash
cat > $TMPDIR/mk_controls.py <<'PYEOF'
import nbformat as nbf
nb = nbf.v4.new_notebook()
nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}}
C = []
def md(s, tags=None):
    c = nbf.v4.new_markdown_cell(s); C.append(c)
def code(s, tags=None):
    c = nbf.v4.new_code_cell(s)
    if tags: c.metadata["tags"] = tags
    C.append(c)

md("""# Daume et al. (2024) on dandiset 000673: hippocampal PAC controls

**Paper.** Daume J, Kaminski J, Schjetnan AGP, Salimpour Y, Khan U, Kyzar M, Reed CM, Anderson WS,
Valiante TA, Mamelak AN, Rutishauser U (2024). Control of working memory by phase-amplitude
coupling of human hippocampal neurons. *Nature* 629, 393-401.
[doi:10.1038/s41586-024-07309-z](https://doi.org/10.1038/s41586-024-07309-z).

**Dandiset.** [DANDI:000673](https://dandiarchive.org/dandiset/000673/0.240118.2135), version
0.240118.2135, the version the paper cites (reference 59); see the header of
`reproduce_daume_2024.ipynb` for the later versions.

**Text the claims were written from.** The version of record (PMC11078732) with its Methods,
legends and Supplementary Information, and the paper's code (SBCAT-release-NWB at a25e8cc3).

This notebook tests the controls of Extended Data Fig. 3 on the hippocampal PAC channels. It
repeats, for the 586 hippocampal channels only, the channel processing of
`reproduce_daume_2024_lfp.ipynb` (each channel's random draws are seeded by session, channel and
artefact reading, so the PAC channels are the same 144 and 125 as there), and adds the theta
cycle features of bycycle, the phase-phase coupling of each phase and amplitude centre pair, and
a comodulogram with 0.5 Hz phase steps. It is kept apart so that neither notebook exceeds the
time limit.

| Claim | Tested here |
|---|---|
| edf3-hippocampus-pac-controls | yes |
""")
code("""import os
for _k in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[_k] = "1"   # many small computations run in parallel processes
import time
import warnings

import numpy as np
import pandas as pd
from scipy import stats

import sbcat

pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 40)
warnings.filterwarnings("ignore")

started = time.time()
S = sbcat.load_all(sbcat.list_assets())
print(f"loaded trials and units of {len(S)} files in {time.time() - started:.0f} s")
t0 = time.time()
R = sbcat.run_all_lfp(S, seed=201, workers=6, controls=True, areas=["hippocampus"])
print(f"LFP of {len(R)} sessions, {sum(len(r['channels']) for r in R)} hippocampal channels, processed in {(time.time() - t0) / 60:.1f} min")""")
code("""HG = np.where((sbcat.AMP_CENTRES >= 70) & (sbcat.AMP_CENTRES <= 140))[0]
READINGS = ["a", "b"]
rows = []
for r in R:
    for c in r["channels"]:
        for rd in READINGS:
            o = c["readings"][rd]
            base = {"session": c["session"], "subject": c["subject"], "channel": c["channel"], "reading": rd,
                    "kept_trials": int(c["masks"][rd].sum()), "n_trials": len(c["masks"][rd])}
            if o is None:
                rows.append({**base, "n_per_load": 0})
                continue
            rows.append({**base, "n_per_load": o["n_per_load"],
                         "z_thetaHG": float(np.mean([o["z_all"][p][HG].mean() for p in sbcat.THETA])),
                         "z1_thetaHG": float(np.mean([o["z_l1"][p][HG].mean() for p in sbcat.THETA])),
                         "z3_thetaHG": float(np.mean([o["z_l3"][p][HG].mean() for p in sbcat.THETA]))})
ch = pd.DataFrame(rows)
chan_index = {(c["session"], c["channel"]): c for r in R for c in r["channels"]}


def hpc_sig(rd):
    return ch[(ch.reading == rd) & (ch.z_thetaHG > 1.64)]""")
md("## Data check")
code("""print("hippocampal LFP channels:", int((ch.reading == "a").sum()), "(paper 586) in", ch.session.nunique(), "sessions of", ch.subject.nunique(), "patients")
for rd in READINGS:
    d = hpc_sig(rd)
    print(f"reading {rd}: {len(d)} channels with significant theta-high-gamma PAC (as in reproduce_daume_2024_lfp.ipynb), "
          f"load 1 mean z {d.z1_thetaHG.mean():.2f}, load 3 {d.z3_thetaHG.mean():.2f}")
cyc = np.concatenate([c["cycles"] for c in chan_index.values()])
print("theta cycles (bycycle, 3-7 Hz) with their peak in 0 to 2.5 s, per correct trial: all cycles median %.0f (range %d to %d); "
      "burst cycles median %.0f (range %d to %d); trials with no burst cycle %.1f%%" % (
          np.median(cyc[:, 5]), cyc[:, 5].min(), cyc[:, 5].max(), np.median(cyc[:, 2]), cyc[:, 2].min(), cyc[:, 2].max(),
          100 * (cyc[:, 2] == 0).mean()))
allc = cyc[:, 5] > 0
print("range of the mean asymmetry per trial (all cycles): rise-decay %.3f to %.3f, peak-trough %.3f to %.3f" % (
    (cyc[allc, 3] / cyc[allc, 5]).min(), (cyc[allc, 3] / cyc[allc, 5]).max(), (cyc[allc, 4] / cyc[allc, 5]).min(), (cyc[allc, 4] / cyc[allc, 5]).max()))
print("phase-phase pairs (phase centre, amplitude centre, n):", [(p, int(a), int(round(a / p))) for p, a in sbcat.PPC_PAIRS])""", tags=["sanity"])
md("""## edf3-hippocampus-pac-controls

> The hippocampal load effect on PAC was not explained by theta or gamma power, theta waveform
> asymmetry, theta-gamma phase-phase coupling, preferred phase or PAC peak frequency.

Every test is a two-sided paired permutation t-test between loads over the PAC channels, on the
trials of the PAC analysis (the equal-count subsamples of each load), as the criterion and the
Extended Data Fig. 3 legend say.

- Power, theta (3-7 Hz) and high gamma (70-140 Hz): readings (a) mean squared Hilbert amplitude
  of the PAC filters; (b) the Welch spectrum of 0 to 2.5 s averaged over the band (log10).
- Waveform asymmetry: bycycle (version in the lock file) with f_range 3-7 Hz and its default
  burst thresholds, on each trial's -0.5 to 3 s epoch, cycles with their peak in 0 to 2.5 s;
  rise-decay (`time_rdsym`) and peak-trough (`time_ptsym`) symmetry averaged over cycles per load
  ("averaged estimates ... across cycles during the maintenance period from the same trials used
  for our PAC analysis within each load", Methods, PAC). The Methods do not say whether only
  burst cycles count; burst cycles (bycycle's default use) and all cycles are both shown. Each
  is also tested against 0.5 (symmetric), as the criterion asks.
- Phase-phase coupling, n:m phase locking value: readings (a) the ratio of the band centres,
  1:21 (5 and 105 Hz); (b) each pair of a theta phase centre (4, 6 Hz) and a high-gamma
  amplitude centre (70 to 140 Hz) of O3, n the ratio rounded to an integer, averaged over pairs.
- Preferred phase: the load difference of each channel's preferred phase, readings (a) V test
  against 0; (b) permutation t-test of the wrapped differences against 0.
- PAC peak frequency (Extended Data Fig. 3h): raw MI with phase centres 3 to 7 Hz in 0.5 Hz steps
  (2 Hz bandwidth) and amplitude centres 70 to 140 Hz (bandwidth twice the phase centre), per
  load; "the frequency bin for which PAC was maximal for the theta and the gamma band
  separately" is read as the maximum of the mean over the other axis (main), and as the
  coordinates of the single largest bin (variant).""")
code("""rng = np.random.default_rng(309)
freqs = R[0]["freqs"]
centres = np.radians(np.linspace(-180, 180, sbcat.N_BINS + 1)[:-1] + 180 / sbcat.N_BINS)
n_samp = sbcat.EPOCH_N - 2 * sbcat.CUT
edf3_tables = {}
for rd in READINGS:
    d = hpc_sig(rd)
    V = {k: {1: [], 3: []} for k in ["theta power, Hilbert", "high-gamma power, Hilbert", "theta power, Welch",
                                     "high-gamma power, Welch", "rise-decay symmetry, burst cycles",
                                     "peak-trough symmetry, burst cycles", "rise-decay symmetry, all cycles",
                                     "peak-trough symmetry, all cycles", "phase locking 1:21 (a)",
                                     "phase locking, each centre pair (b)", "theta peak frequency (Hz)",
                                     "gamma peak frequency (Hz)", "theta peak frequency, largest bin (Hz)",
                                     "gamma peak frequency, largest bin (Hz)"]}
    pref = {1: [], 3: []}
    for r in d.itertuples():
        c = chan_index[(r.session, r.channel)]
        o = c["readings"][rd]
        for L in (1, 3):
            pos = np.searchsorted(c["trial_index"], o[f"trials_l{L}"])
            V["theta power, Hilbert"][L].append(np.log10(c["theta_power"][pos].mean()))
            V["high-gamma power, Hilbert"][L].append(np.log10(c["hg_power"][pos].mean()))
            V["theta power, Welch"][L].append(np.log10(o[f"psd_l{L}"][(freqs >= 3) & (freqs <= 7)].mean()))
            V["high-gamma power, Welch"][L].append(np.log10(o[f"psd_l{L}"][(freqs >= 70) & (freqs <= 140)].mean()))
            cy = c["cycles"][pos].sum(0)
            V["rise-decay symmetry, burst cycles"][L].append(cy[0] / cy[2] if cy[2] else np.nan)
            V["peak-trough symmetry, burst cycles"][L].append(cy[1] / cy[2] if cy[2] else np.nan)
            V["rise-decay symmetry, all cycles"][L].append(cy[3] / cy[5] if cy[5] else np.nan)
            V["peak-trough symmetry, all cycles"][L].append(cy[4] / cy[5] if cy[5] else np.nan)
            V["phase locking 1:21 (a)"][L].append(o[f"ppc_l{L}"])
            V["phase locking, each centre pair (b)"][L].append(np.mean(np.abs(c["ppc_pairs"][pos].sum(0)) / (len(pos) * n_samp)))
            fm = o[f"fine_mi_l{L}"]                           # phases x amplitudes
            V["theta peak frequency (Hz)"][L].append(sbcat.FINE_PHASE[np.argmax(fm.mean(1))])
            V["gamma peak frequency (Hz)"][L].append(sbcat.FINE_AMPS[np.argmax(fm.mean(0))])
            ip, ia = np.unravel_index(np.argmax(fm), fm.shape)
            V["theta peak frequency, largest bin (Hz)"][L].append(sbcat.FINE_PHASE[ip])
            V["gamma peak frequency, largest bin (Hz)"][L].append(sbcat.FINE_AMPS[ia])
            P = o[f"P_thetaHG_l{L}"]
            pref[L].append(np.angle(np.sum(P * np.exp(1j * centres))))
    res = []
    for k, v in V.items():
        t = sbcat.perm_ttest_paired(v[3], v[1], rng)
        res.append({"test": k, "n": t["n"], "load1": t["mean_y"], "load3": t["mean_x"], "t(3-1)": t["t"], "p": t["p"]})
    dphi = np.angle(np.exp(1j * (np.array(pref[3]) - np.array(pref[1]))))
    n = len(dphi)
    m = np.mean(np.exp(1j * dphi))
    u = n * np.abs(m) * np.cos(np.angle(m)) * np.sqrt(2 / n)
    res.append({"test": "preferred phase 3-1, V test against 0 (a)", "n": n, "t(3-1)": u, "p": 1 - stats.norm.cdf(u)})
    t = sbcat.perm_ttest_1samp(np.degrees(dphi), rng)
    res.append({"test": "preferred phase 3-1, wrapped, t-test against 0 (b) (deg)", "n": t["n"], "load3": t["mean"], "t(3-1)": t["t"], "p": t["p"]})
    tab = pd.DataFrame(res)
    edf3_tables[rd] = tab
    print(f"artefact reading {rd}: {len(d)} PAC channels")
    print(tab.round(4).to_string(index=False))
    print("mean resultant length of the preferred phase differences: %.3f; circular mean %.1f deg; |difference| < 20 deg in %d of %d channels" % (
        np.abs(m), np.degrees(np.angle(m)), int((np.abs(np.degrees(dphi)) < 20).sum()), n))
    sym = []
    for k in ["rise-decay symmetry, burst cycles", "peak-trough symmetry, burst cycles", "rise-decay symmetry, all cycles", "peak-trough symmetry, all cycles"]:
        both = np.nanmean([V[k][1], V[k][3]], 0)
        t = sbcat.perm_ttest_1samp(both - 0.5, rng)
        sym.append({"asymmetry against 0.5 (mean of loads)": k, "n": t["n"], "mean": t["mean"] + 0.5, "t": t["t"], "p": t["p"]})
    print(pd.DataFrame(sym).round(4).to_string(index=False))
    print("channels without a burst cycle in a load:", int(np.sum(np.isnan(V["rise-decay symmetry, burst cycles"][1]) | np.isnan(V["rise-decay symmetry, burst cycles"][3]))))
    for k in ["theta peak frequency (Hz)", "gamma peak frequency (Hz)"]:
        print(f"{k}: range load 1 {min(V[k][1])} to {max(V[k][1])}, load 3 {min(V[k][3])} to {max(V[k][3])}")
    print()
print("paper: no load difference in any of these (Extended Data Fig. 3b, c, d, g, h; n = 137)")""", tags=["claim:edf3-hippocampus-pac-controls"])
md("**Result: PLACEHOLDER**")
md("""## Summary

PLACEHOLDER""")
code('print(f"notebook ran in {(time.time() - started) / 60:.1f} min")')
nb.cells = C
nbf.write(nb, "reproduce_daume_2024_lfp_controls.ipynb")
PYEOF
python $TMPDIR/mk_controls.py && ls
```

```
README.md
__pycache__
entry.yaml
reproduce_daume_2024.ipynb
reproduce_daume_2024_lfp.ipynb
reproduce_daume_2024_lfp_controls.ipynb
reproduce_daume_2024_pac_neurons.ipynb
requirements.in
requirements.lock.txt
sbcat.py
```

**Agent calls Bash**

```bash
rm -rf __pycache__; cat > $TMPDIR/runcells.py <<'EOF'
import sys, os, json, pickle, time, warnings
warnings.filterwarnings("ignore")
import numpy as np, pandas as pd
from scipy import stats
import sbcat
nbp, rpk = sys.argv[1], sys.argv[2]
A=sbcat.list_assets()
S=sbcat.load_all(A)
r=pickle.load(open(rpk,'rb'))
si=[i for i,s in enumerate(S) if 'sub-26_ses-1' in s['path']][0]
r['session']=si
for c in r['channels']: c['session']=si
R=[r]; started=time.time()
d=json.load(open(nbp))
cells=[c for c in d['cells'] if c['cell_type']=='code'][1:]
for c in cells[:int(sys.argv[3]) if len(sys.argv)>3 else None]:
    src=''.join(c['source'])
    exec(src)
EOF
PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/runcells.py reproduce_daume_2024_lfp_controls.ipynb $TMPDIR/r26.pkl 2>&1 | tail -60
```

```
hippocampal LFP channels: 36 (paper 586) in 1 sessions of 1 patients
reading a: 11 channels with significant theta-high-gamma PAC (as in reproduce_daume_2024_lfp.ipynb), load 1 mean z 3.49, load 3 3.83
reading b: 11 channels with significant theta-high-gamma PAC (as in reproduce_daume_2024_lfp.ipynb), load 1 mean z 2.42, load 3 3.25
Traceback (most recent call last):
  File "/tmp/claude-1001/runcells.py", line 18, in <module>
    exec(src)
    ~~~~^^^^^
  File "<string>", line 6, in <module>
KeyError: 'cycles'
```

**Agent calls Bash**

```bash
sed -i "s/^R=\[r\]; started/if 'controls' in nbp: r['channels']=[c for c in r['channels'] if c['area']=='hippocampus']\nR=[r]; started/" $TMPDIR/runcells.py; PYTHONPATH=. $TMPDIR/dev/bin/python $TMPDIR/runcells.py reproduce_daume_2024_lfp_controls.ipynb $TMPDIR/r26.pkl 2>&1 | tail -60
```

```
range of the mean asymmetry per trial (all cycles): rise-decay 0.307 to 0.684, peak-trough 0.347 to 0.638
phase-phase pairs (phase centre, amplitude centre, n): [(4, 70, 18), (4, 75, 19), (4, 80, 20), (4, 85, 21), (4, 90, 22), (4, 95, 24), (4, 100, 25), (4, 105, 26), (4, 110, 28), (4, 115, 29), (4, 120, 30), (4, 125, 31), (4, 130, 32), (4, 135, 34), (4, 140, 35), (6, 70, 12), (6, 75, 12), (6, 80, 13), (6, 85, 14), (6, 90, 15), (6, 95, 16), (6, 100, 17), (6, 105, 18), (6, 110, 18), (6, 115, 19), (6, 120, 20), (6, 125, 21), (6, 130, 22), (6, 135, 22), (6, 140, 23)]
artefact reading a: 9 PAC channels
                                                    test  n   load1   load3  t(3-1)      p
                                    theta power, Hilbert  9  3.0359  3.0298 -0.3818 0.6978
                               high-gamma power, Hilbert  9  1.4712  1.4715  0.0994 0.9231
                                      theta power, Welch  9  2.1937  2.1933 -0.0255 0.9778
                                 high-gamma power, Welch  9 -0.2907 -0.2853  1.2796 0.2510
                       rise-decay symmetry, burst cycles  0     NaN     NaN     NaN    NaN
                      peak-trough symmetry, burst cycles  0     NaN     NaN     NaN    NaN
                         rise-decay symmetry, all cycles  9  0.5008  0.4993 -0.6239 0.5393
                        peak-trough symmetry, all cycles  9  0.4850  0.4876  1.1747 0.3005
                                  phase locking 1:21 (a)  9  0.0064  0.0103  1.9865 0.0842
                     phase locking, each centre pair (b)  9  0.0089  0.0090  0.4966 0.6228
                               theta peak frequency (Hz)  9  3.7778  3.2222 -1.8182 0.2512
                               gamma peak frequency (Hz)  9 84.4444 84.4444  0.0000 1.0000
                  theta peak frequency, largest bin (Hz)  9  3.2222  3.3889  0.6667 0.6141
                  gamma peak frequency, largest bin (Hz)  9 83.8889 79.4444 -0.8835 0.5048
               preferred phase
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json
d=json.load(open('reproduce_daume_2024_pac_neurons.ipynb'))
for i in [0,1,3,5,7]:
    print('#### cell',i); print(''.join(d['cells'][i]['source']))
"; sed -n 140,183p sbcat.py
```

```
#### cell 0
# Daume et al. (2024) on dandiset 000673: PAC neurons

**Paper.** Daume J et al. (2024). Control of working memory by phase-amplitude coupling of human
hippocampal neurons. *Nature* 629, 393-401.
[doi:10.1038/s41586-024-07309-z](https://doi.org/10.1038/s41586-024-07309-z).

**Dandiset.** [DANDI:000673](https://dandiarchive.org/dandiset/000673/0.240118.2135), version
0.240118.2135, the version the paper cites (reference 59); see the header of
`reproduce_daume_2024.ipynb`.

**Text the claims were written from.** The version of record (PMC11078732) with its Methods,
legends and Supplementary Information, and the paper's code (SBCAT-release-NWB at a25e8cc3).

This notebook selects PAC neurons (Methods, Selection of PAC neurons; `sbcat.py` says where each
parameter comes from) and tests the claims on them that need only spikes and the LFP of their
bundle. Artefact rejection uses reading (a) of O1 (on the epochs), the reading adopted in
`reproduce_daume_2024_lfp.ipynb`.

| Claim | Tested here |
[... 163 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='sbcat.py'; s=open(p).read()
old='''        "unsorted_units": unsorted, "lfp_electrodes": lfp_el, "lfp_info": lfp_info, "events": events,
    }'''
new='''        "unsorted_units": unsorted, "lfp_electrodes": lfp_el, "lfp_info": lfp_info, "events": events,
        "units_columns": {k: tuple(u[k].shape) for k in u.keys() if isinstance(u[k], h5py.Dataset)},
    }'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
python3 -c "
import json
d=json.load(open('reproduce_daume_2024.ipynb'))
for i in [0,4,23,28,31,34,37,43,44]:
    print('#### cell',i); print(''.join(d['cells'][i]['source']))
"
```

```
#### cell 0
# Daume et al. (2024) on dandiset 000673: behaviour and single neurons

**Paper.** Daume J, Kaminski J, Schjetnan AGP, Salimpour Y, Khan U, Kyzar M, Reed CM, Anderson WS,
Valiante TA, Mamelak AN, Rutishauser U (2024). Control of working memory by phase-amplitude
coupling of human hippocampal neurons. *Nature* 629, 393-401.
[doi:10.1038/s41586-024-07309-z](https://doi.org/10.1038/s41586-024-07309-z).

**Dandiset.** [DANDI:000673](https://dandiarchive.org/dandiset/000673/0.240118.2135), version
0.240118.2135. The paper's reference 59 cites this version ("v.0.240118.2135"), so it is pinned,
as the protocol asks. Four later versions exist (0.240524.1751, 0.240524.1758, 0.250122.0110 and
the draft); in 0.250122.0110 every one of the 44 files has a new asset with a size a few hundred
kilobytes smaller, with the same paths. The analysis here does not use the later versions.

**Text the claims were written from.** The version of record (PMC11078732), with the Methods,
figure legends, Extended Data legends and Supplementary Information, and the paper's code
(github.com/rutishauserlab/SBCAT-release-NWB at commit a25e8cc3).

This notebook tests the claims on behaviour and single-neuron firing. The LFP claims are in
`reproduce_daume_2024_lfp.ipynb`. Claims tested here:
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "add_argument\|def cmd_\|max-minutes\|max_minutes" ../../tools/entry.py | head -30
```

```
29:that takes longer than --max-minutes fails, even if it ran without error.
342:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float) -> int:
371:        if ok and seconds > max_minutes * 60:
373:            error = f"took {seconds / 60:.0f} minutes; the limit is {max_minutes:.0f}"
428:    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover"])
429:    parser.add_argument("entry", type=Path, nargs="+",
431:    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
432:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
433:    parser.add_argument("--max-minutes", type=float, default=30,
469:    return run(entry_dir, output_dir, args.timeout, args.max_minutes)
```

**Agent calls Bash**

```bash
sed -n 300,400p ../../tools/entry.py
```

```
if outcome.get("claim") not in known:
                report.error(path.relative_to(ROOT), f"claim {outcome.get('claim')!r} is not in the claims file")
            notebook = outcome.get("notebook")
            if notebook and notebook not in listed:
                report.error(path.relative_to(ROOT), f"notebook {notebook!r} is not in the entry")
            tag = outcome.get("output")
            if notebook in present and tag:
                nb = nbformat.read(entry_dir / notebook, as_version=4)
                if not any(tag in c.metadata.get("tags", []) for c in nb.cells):
                    report.error(path.relative_to(ROOT), f"no cell tagged {tag!r} in {notebook}")
    return report


def _local_data(code: str, start: int) -> bool:
    """Whether a local path in the code is inside the dataset directory `encore check` gave (ENCORE_LOCAL_DATA):
    the one local path an entry on a local dataset may name."""
    allowed = os.environ.get("ENCORE_LOCAL_DATA", "").rstrip("/")
    return bool(allowed) and code.startswith(allowed, start) and code[start + len(allowed):start + len(allowed) + 1] in ("/", "'", '"')


[... 82 more lines not kept]
```

**Agent**

Plan set: I'll edit all notebooks now, run each on the full data in a dev environment, then do the final `entry.py all` run. Editing the LFP notebook first.

**Agent calls Bash**

```bash
cat > $TMPDIR/ed_lfp.py <<'PYEOF'
import nbformat as nbf
p = "reproduce_daume_2024_lfp.ipynb"
nb = nbf.read(p, as_version=4)
cells = nb.cells
def src(i): return cells[i].source
def find(prefix):
    for i, c in enumerate(cells):
        if c.source.startswith(prefix): return i
    raise KeyError(prefix)

# header table
h = cells[0]
h.source = h.source.replace("| edf3-hippocampus-pac-controls | in part (power, phase-phase coupling, preferred phase); blocked |\n",
  "| edf3-hippocampus-pac-controls | in `reproduce_daume_2024_lfp_controls.ipynb` |\n")
h.source = h.source.replace("| methods-spectral-slope | yes |", "| methods-spectral-slope | yes |\n| fig3h-pac-category-firing | yes |")
assert "fig3h" in h.source and "lfp_controls" in h.source

# sanity: removed trials distribution, and the paper's own artefact trials for one channel
i = find('one = ch[ch.reading == "a"]')
cells[i].source += '''
for rd in READINGS:
    d = ch[ch.reading == rd]
    rem = d.n_trials - d.kept_trials
    print(f"reading {rd}: trials removed per channel, percentiles 0/25/50/75/90/100: {np.percentile(rem, [0, 25, 50, 75, 90, 100]).round(1).tolist()}; "
          f"channels with none removed {int((rem == 0).sum())} of {len(rem)}; histogram (0-4, 5-9, ..., 50+): "
          f"{np.bincount(np.minimum(rem // 5, 10), minlength=11).tolist()}")'''
new_cell = nbf.v4.new_code_cell('''# The paper's code (NWB_samplePAC_SU.m, SBCAT-release-NWB at a25e8cc3) ships the artefact trials of
# its example: sub-26, session 1, LFP channel 33 (1-based), in artif_trials.mat. Compare them with the
# trials each reading of O1 removes on that channel.
import io
import urllib.request
from scipy.io import loadmat
url = ("https://raw.githubusercontent.com/rutishauserlab/SBCAT-release-NWB/a25e8cc3f61630a428f190381745257d4506f148/"
       "NWB_SBCAT_analysis/helpers/internal/PAC/artif_trials.mat")
with urllib.request.urlopen(url) as r_:
    paper_artif = set(int(v) - 1 for v in loadmat(io.BytesIO(r_.read()))["artif_trials"].ravel())
si26 = [i for i, s in enumerate(S) if s["subject"] == "26" and s["session"] == "1"]
print("sub-26 session 1:", [S[i]["path"] for i in si26])
c26 = chan_index[(si26[0], 32)]
print(f"channel 33 ({c26['location']}): the paper's code removes {len(paper_artif)} trials")
for rd in READINGS:
    rem = set(np.where(~c26["masks"][rd])[0])
    print(f"  reading {rd} removes {len(rem)}; {len(rem & paper_artif)} of them among the paper's {len(paper_artif)}, "
          f"{len(rem - paper_artif)} that the paper kept")''')
new_cell.metadata["tags"] = ["sanity"]
cells.insert(i + 1, new_cell)

# comodulogram under both readings
i = find('for rd in ["a"]:\n    Z = np.array')
s = cells[i].source
s = s.replace('for rd in ["a"]:\n    Z = np.array([[c["readings"][rd]["z_all"][p] for p in sbcat.PHASE_CENTRES]',
              'for rd in READINGS:\n    PH = sbcat.PHASE_CENTRES if rd == "a" else np.array([2, 4, 6, 8])   # reading (b) computes phase 2-8 Hz only\n    Z = np.array([[c["readings"][rd]["z_all"][int(p)] for p in PH]')
s = s.replace('print(f"reading {rd}: {len(Z)} channels; mean z comodulogram (rows phase 2-14 Hz, columns amplitude 30-150 Hz):")',
              'print(f"reading {rd}: {len(Z)} channels; mean z comodulogram (rows phase {PH[0]}-{PH[-1]} Hz, columns amplitude 30-150 Hz):")')
s = s.replace("print(pd.DataFrame(mean_z, index=sbcat.PHASE_CENTRES,", "print(pd.DataFrame(mean_z, index=PH,")
s = s.replace('print(f"largest mean z {mean_z[ip, ia]:.2f} at phase {sbcat.PHASE_CENTRES[ip]} Hz', 'print(f"largest mean z {mean_z[ip, ia]:.2f} at phase {PH[ip]} Hz')
s = s.replace("prof = mean_z[list(sbcat.PHASE_CENTRES).index(p)]", "prof = mean_z[list(PH).index(p)]")
s = s.replace("(int(sbcat.PHASE_CENTRES[np.unravel_index(m.argmax(), m.shape)[0]])", "(int(PH[np.unravel_index(m.argmax(), m.shape)[0]])")
s = s.replace('extent=[27.5, 152.5, 1, 15]', 'extent=[27.5, 152.5, PH[0] - 1, PH[-1] + 1]')
assert s.count("PH") >= 7, s
cells[i].source = s

# pre-SMA channels, per channel
i = find('print(fig2c[fig2c.area != "hippocampus"]')
cells[i].source += '''
for rd in READINGS:
    d = ch[(ch.reading == rd) & (ch.area == "preSMA") & (ch.z_thetaHG > 1.64)]
    print(f"\\npre-SMA PAC channels, reading {rd} (z of theta-high-gamma MI per load):")
    print(d[["subject", "session", "channel", "z1_thetaHG", "z3_thetaHG"]].assign(diff=d.z3_thetaHG - d.z1_thetaHG).round(2).to_string(index=False))
    r_ = sbcat.perm_ttest_paired(d.z3_thetaHG, d.z1_thetaHG, np.random.default_rng(310))
    w = stats.wilcoxon(d.z3_thetaHG, d.z1_thetaHG)
    top = d.assign(diff=d.z3_thetaHG - d.z1_thetaHG).sort_values("diff").iloc[:-3]
    r3 = sbcat.perm_ttest_paired(top.z3_thetaHG, top.z1_thetaHG, np.random.default_rng(311))
    print(f"load 3 higher in {int((d.z3_thetaHG > d.z1_thetaHG).sum())} of {len(d)}; paired permutation t-test p = {r_['p']:.4f}; "
          f"Wilcoxon signed-rank p = {w.pvalue:.4f}; without the 3 channels of largest load 3 excess, t = {r3['t']:.2f}, p = {r3['p']:.4f}")'''

# fig2f trimmed RT variants
i = find("glm_rows = []\nfor rd in READINGS:")
cells[i].source += '''
# Variants on artefact reading (a): RTs below 10 s only, and log RT (the paper states no trimming)
var_rows = []
for a in ["hippocampus", "amygdala", "vmPFC"]:
    d = ch[(ch.reading == "a") & (ch.area == a) & (ch.z_thetaHG > 1.64)]
    parts = []
    for r in d.itertuples():
        c = chan_index[(r.session, r.channel)]
        tr = S[r.session]["trials"]
        idx = c["trial_index"]
        keep = c["masks"]["a"][idx]
        pac = c["st_thetaHG"][keep]
        parts.append(pd.DataFrame({"rt": tr.rt.to_numpy()[idx][keep], "load": tr.load.to_numpy()[idx][keep].astype(str),
                                   "pac_a": pac, "pac_b": (pac - np.nanmean(pac)) / np.nanstd(pac),
                                   "patient": r.subject, "channel": f"{r.session}_{r.channel}"}))
    dfa = pd.concat(parts).dropna().reset_index(drop=True)
    for vname, dv in [("RT < 10 s", dfa[dfa.rt < 10].reset_index(drop=True)), ("log10 RT", dfa.assign(rt=np.log10(dfa.rt)))]:
        for o5 in ["a", "b"]:
            m = smf.mixedlm(f"rt ~ pac_{o5} * load", dv, groups="patient", vc_formula={"channel": "0 + C(channel)"}).fit(reml=True)
            var_rows.append({"variant": vname, "O5": o5, "area": a, "trials": len(dv), "estimate": m.params[f"pac_{o5}"],
                             "t": m.tvalues[f"pac_{o5}"], "p": m.pvalues[f"pac_{o5}"]})
print("\\nartefact reading (a), variants:")
print(pd.DataFrame(var_rows).round(5).to_string(index=False))'''

# nesting window variants
i = find("rng = np.random.default_rng(307)")
cells[i].source += '''
# How the count depends on the window for local maxima (45 ms in the Methods), reading (a)
d = hpc_sig("a")
rows_ = []
for nr in ["amp", "peak"]:
    avgs = [chan_index[(r.session, r.channel)]["readings"]["a"]["nesting"][nr]["avg"] for r in d.itertuples()]
    for w in [5, 7, 9, 11, 13, 17]:
        nmax = np.array([sbcat.local_maxima(a_, w) for a_ in avgs])
        rows_.append({"alignment": nr, "window_ms": round(2 * w * 2.5, 1), "nested (>= 3 maxima)": int((nmax >= 3).sum()), "of": len(d)})
print(pd.DataFrame(rows_).pivot(index="window_ms", columns="alignment", values="nested (>= 3 maxima)").to_string())'''

# remove the edf3 section (moved to the controls notebook)
i = find("### edf3-hippocampus-pac-controls")
del cells[i:i + 3]

# fig3h section before the summary
i = find("## Summary")
md = nbf.v4.new_markdown_cell('''## fig3h-pac-category-firing

> Trial by trial, single-trial theta-high-gamma PAC was weakly positively related to the spike
> count of hippocampal category neurons, but not of amygdala category neurons.

Category neurons are selected as in `reproduce_daume_2024.ipynb` (same function and seed, so the
same 94 hippocampal and 181 amygdala neurons). Each is paired with every significant PAC channel
of its bundle (the electrodes of a session with the same location and coordinates; the files name
no bundle). Per pair, the correct trials clean for the channel; SC is the spike count 0 to 2.5 s
after maintenance onset; single-trial PAC under O5 (a) raw and (b) z-scored within the channel.
The model of Table S3, PAC ~ 1 + SC + load + SC x load + (1 | patient) + (1 | patient:pair),
fitted with statsmodels MixedLM (REML) in place of fitglme, under the trial readings of the
criterion: (a) all correct trials, (b) correct preferred trials. Artefact reading (a) of O1 is the
one adopted; reading (b) is also shown.''')
code = nbf.v4.new_code_cell('''t0 = time.time()
cat_table, _ = sbcat.category_table(S, seed=103)      # the same selection and seed as reproduce_daume_2024.ipynb
cat = cat_table[cat_table.is_category & cat_table.area.isin(sbcat.MTL)].reset_index(drop=True)
cat_trials = sbcat.trial_rates(S, cat)
print(f"category selection in {time.time() - t0:.0f} s:", cat.area.value_counts().to_dict())
h3_rows, pair_rows = [], []
for rd in READINGS:
    parts = []
    for i, u in cat.iterrows():
        s = S[u.session]
        keys = sbcat.bundle_keys(s["electrodes"])
        on = s["trials"].timestamps_Maintenance.to_numpy()
        sc_all = sbcat.count_in(s["spikes"][u.unit], on, on + 2.5)
        for ci, e in enumerate(s["lfp_electrodes"]):
            if keys[e] != keys[u.electrode] or (u.session, ci) not in chan_index:
                continue
            row = ch[(ch.reading == rd) & (ch.session == u.session) & (ch.channel == ci)].iloc[0]
            if not row.z_thetaHG > 1.64:
                continue
            c = chan_index[(u.session, ci)]
            idx = c["trial_index"]
            keep = c["masks"][rd][idx]
            st = c["st_thetaHG"][keep]
            parts.append(pd.DataFrame({"pac_a": st, "pac_b": (st - np.nanmean(st)) / np.nanstd(st), "sc": sc_all[idx][keep],
                                       "load": s["trials"].load.to_numpy()[idx][keep].astype(str),
                                       "pref": cat_trials[i]["pref"][idx][keep], "patient": u.subject,
                                       "pair": f"{u.session}_{u.unit}_{ci}", "area": u.area}))
    df3 = pd.concat(parts).dropna().reset_index(drop=True)
    for a in sbcat.MTL:
        da = df3[df3.area == a]
        pair_rows.append({"artefact": rd, "area": a, "pairs": da.pair.nunique(), "neurons": da.pair.str.rsplit("_", n=1).str[0].nunique(),
                          "patients": da.patient.nunique(), "trials": len(da), "spike count median": da.sc.median(), "max": da.sc.max()})
        for trials in ["all", "preferred"]:
            d = da[(trials == "all") | da.pref].reset_index(drop=True)
            for o5 in ["a", "b"]:
                try:
                    m = smf.mixedlm(f"pac_{o5} ~ sc * load", d, groups="patient", vc_formula={"pair": "0 + C(pair)"}).fit(reml=True)
                    h3_rows.append({"artefact": rd, "area": a, "trials": trials, "O5": o5, "pairs": d.pair.nunique(), "n": len(d),
                                    "SC estimate": m.params["sc"], "t": m.tvalues["sc"], "p": m.pvalues["sc"],
                                    "SC x load p": m.pvalues["sc:load[T.3]"], "converged": m.converged})
                except Exception as e_:   # report a failed fit
                    h3_rows.append({"artefact": rd, "area": a, "trials": trials, "O5": o5, "error": str(e_)[:80]})
print(pd.DataFrame(pair_rows).to_string(index=False))
print("paper: 151 hippocampal and 423 amygdala neuron-channel combinations")
print(pd.DataFrame(h3_rows).round(5).to_string(index=False))
print("paper (Table S3): hippocampus SC estimate 0.002, t = 2.40, p = 0.017; amygdala -0.001, t = -0.75, p = 0.45")''')
code.metadata["tags"] = ["claim:fig3h-pac-category-firing"]
res = nbf.v4.new_markdown_cell("**Result: PLACEHOLDER**")
cells[i:i] = [md, code, res]
nbf.write(nb, p)
print("ok")
PYEOF
python $TMPDIR/ed_lfp.py
```

```
ok
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import nbformat as nbf
p="reproduce_daume_2024_lfp.ipynb"; nb=nbf.read(p,as_version=4)
for c in nb.cells:
    c.source=c.source.replace("{np.bincount(np.minimum(rem // 5, 10), minlength=11).tolist()}","{np.bincount(np.minimum(rem.to_numpy().astype(int) // 5, 10), minlength=11).tolist()}")
    c.source=c.source.replace('si26 = [i for i, s in enumerate(S) if s["subject"] == "26" and s["session"] == "1"]','si26 = [i for i, s in enumerate(S) if "sub-26_ses-1_" in s["path"]]')
nbf.write(nb,p)
EOF
date -u; PYTHONPATH=. timeout 900 $TMPDIR/dev/bin/python $TMPDIR/runcells.py reproduce_daume_2024_lfp.ipynb $TMPDIR/r26.pkl 2>&1 | grep -v "Warning\|warn\|return -self\|m = smf\|rslt = super" | tail -150
```

```
Sat Oct 31 12:52:12 UTC 2026
{'a': 36, 'b': 36}
LFP channels by area: {'hippocampus': 28.0, 'amygdala': 8.0, 'preSMA': nan, 'dACC': nan, 'vmPFC': nan} ; total 36
LFP length minus the end of the last trial (s): min 211.7, max 211.7
LFP rate and unit as stored: {(400.0, 'microvolts', 1.0)}
per-channel s.d. of the epochs (stored units): median 58.3, range 23.28 to 109.3; 99th percentile of |LFP|: median 169.6, max 402.8
reading a: trials removed per channel 8.7 +/- 7.0 (6.2%); trials per load after subsampling: median 66, range 51 to 69; channels with fewer than 3 per load (left out): 0
reading b: trials removed per channel 19.7 +/- 14.0 (14.0%); trials per load after subsampling: median 59, range 31 to 68; channels with fewer than 3 per load (left out): 0
paper: 20.4 +/- 13.9 trials (14.6%) removed per wire, with visual inspection
files sharing the sum of their first 4,000 LFP samples (duplicates): none
reading a: trials removed per channel, percentiles 0/25/50/75/90/100: [2.0, 4.0, 6.0, 10.2, 17.5, 32.0]; channels with none removed 0 of 36; histogram (0-4, 5-9, ..., 50+): [12, 14, 3, 4, 1, 1, 1, 0, 0, 0, 0]
reading b: trials removed per channel, percentiles 0/25/50/75/90/100: [4.0, 8.8, 15.5, 24.8, 40.5, 61.0]; channels with none removed 0 of 36; histogram (0-4, 5-9, ..., 50+): [3, 7, 6, 8, 3, 2, 0, 2, 3, 1, 1]
sub-26 session 1: ['sub-26/sub-26_ses-1_ecephys+image.nwb']
channel 33 (hippocampus_right): the paper's code removes 17 trials
  reading a removes 4; 4 of them among the paper's 17, 0 that the paper kept
  reading b removes 9; 4 of them among the paper's 17, 5 that the paper kept
{'shift_-2.0': 1.53, 'shift_-1.0': 2.21, 'shift_0.0': 3.08}
sessions whose median ratio is larger at the true onset than at both shifts: 1 of 1
sessions where it is not: []
reading a: 36 channels; mean z comodulogram (rows phase 2-14 Hz, columns amplitude 30-150 Hz):
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/^import numpy as np, pandas as pd$/import numpy as np, pandas as pd\nimport matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt\nimport statsmodels.formula.api as smf/' $TMPDIR/runcells.py; PYTHONPATH=. timeout 900 $TMPDIR/dev/bin/python $TMPDIR/runcells.py reproduce_daume_2024_lfp.ipynb $TMPDIR/r26.pkl 2>&1 | grep -v "Warning\|warn\|return -self\|m = smf\|rslt = super" | sed -n '/largest mean z per area/,$p' | head -150
```

```
largest mean z per area (phase, amplitude): {'hippocampus': (2, 75, 5.49), 'amygdala': (6, 40, 5.12), 'preSMA': (2, 30, nan), 'dACC': (2, 30, nan), 'vmPFC': (2, 30, nan)}
reading b: 36 channels; mean z comodulogram (rows phase 2-8 Hz, columns amplitude 30-150 Hz):
    30    35    40    45    50    55    60    65    70    75    80    85    90    95    100   105   110   115   120   125   130   135   140   145   150
2  1.14  1.13  1.47  2.01  2.45  2.21  2.12  2.80  3.33  3.45  3.05  2.45  2.07  1.81  1.67  1.55  1.52  1.55  1.53  1.57  1.50  1.43  1.37  1.36  1.33
4  0.89  1.36  2.14  2.55  2.61  2.61  2.78  3.27  3.72  3.79  3.47  2.96  2.70  2.41  2.01  1.52  1.26  1.29  1.36  1.47  1.53  1.57  1.60  1.56  1.42
6  1.17  1.67  2.22  2.46  2.73  2.68  2.72  2.66  2.81  3.05  2.91  2.28  1.83  1.73  1.51  1.34  1.31  1.47  1.54  1.51  1.43  1.39  1.44  1.47  1.42
8  1.18  1.24  1.58  1.81  2.21  2.69  2.64  2.42  2.47  2.79  2.68  2.72  2.27  1.80  1.77  1.72  1.71  1.76  1.76  1.76  1.70  1.54  1.36  1.18  1.06
largest mean z 3.79 at phase 4 Hz, amplitude 75 Hz
phase 4 Hz: local maxima of the amplitude profile at [50, 75, 140] Hz
phase 6 Hz: local maxima of the amplitude profile at [50, 60, 75, 120, 145] Hz
largest mean z per area (phase, amplitude): {'hippocampus': (4, 75, 4.34), 'amygdala': (6, 40, 5.93), 'preSMA': (2, 30, nan), 'dACC': (2, 30, nan), 'vmPFC': (2, 30, nan)}
Traceback (most recent call last):
  File "/tmp/claude-1001/runcells.py", line 21, in <module>
    exec(src)
    ~~~~^^^^^
  File "<string>", line 13, in <module>
TypeError: object of type 'numpy.float64' has no len()
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import os
p=os.environ['TMPDIR']+'/runcells.py'; s=open(p).read()
s=s.replace("    src=''.join(c['source'])\n    exec(src)","    src=''.join(c['source'])\n    try:\n        exec(src)\n    except Exception as e:\n        print('CELL ERROR', src[:60].replace(chr(10),' '), repr(e)[:200])")
open(p,'w').write(s)
EOF
PYTHONPATH=. timeout 900 $TMPDIR/dev/bin/python $TMPDIR/runcells.py reproduce_daume_2024_lfp.ipynb $TMPDIR/r26.pkl 2>&1 | grep -v "Warning\|warn\|return -self\|m = smf\|rslt = super" | sed -n '/largest mean z per area/,$p' | tail -n +4 | head -150
```

```
2  1.14  1.13  1.47  2.01  2.45  2.21  2.12  2.80  3.33  3.45  3.05  2.45  2.07  1.81  1.67  1.55  1.52  1.55  1.53  1.57  1.50  1.43  1.37  1.36  1.33
4  0.89  1.36  2.14  2.55  2.61  2.61  2.78  3.27  3.72  3.79  3.47  2.96  2.70  2.41  2.01  1.52  1.26  1.29  1.36  1.47  1.53  1.57  1.60  1.56  1.42
6  1.17  1.67  2.22  2.46  2.73  2.68  2.72  2.66  2.81  3.05  2.91  2.28  1.83  1.73  1.51  1.34  1.31  1.47  1.54  1.51  1.43  1.39  1.44  1.47  1.42
8  1.18  1.24  1.58  1.81  2.21  2.69  2.64  2.42  2.47  2.79  2.68  2.72  2.27  1.80  1.77  1.72  1.71  1.76  1.76  1.76  1.70  1.54  1.36  1.18  1.06
largest mean z 3.79 at phase 4 Hz, amplitude 75 Hz
phase 4 Hz: local maxima of the amplitude profile at [50, 75, 140] Hz
phase 6 Hz: local maxima of the amplitude profile at [50, 60, 75, 120, 145] Hz
largest mean z per area (phase, amplitude): {'hippocampus': (4, 75, 4.34), 'amygdala': (6, 40, 5.93), 'preSMA': (2, 30, nan), 'dACC': (2, 30, nan), 'vmPFC': (2, 30, nan)}
CELL ERROR paper_counts = {"hippocampus": 137, "amygdala": 130, "preSMA TypeError("object of type 'numpy.float64' has no len()")
reading        area  n  load1  load3  t(3-1)      p  channels_load1_higher  p_fdr
      a hippocampus  9 4.1002 4.0013 -0.1134 0.9080                    7.0 0.9080
      a    amygdala  2 0.7355 3.0551  4.4849 0.4996                    0.0 0.9080
      a      preSMA  0    NaN    NaN     NaN    NaN                    NaN    NaN
      a        dACC  0    NaN    NaN     NaN    NaN                    NaN    NaN
      a       vmPFC  0    NaN    NaN     NaN    NaN                    NaN    NaN
      b hippocampus  9 2.8520 3.2538  0.6702 0.5211                    5.0 0.5211
      b    amygdala  2 0.4680 3.2550 43.4313 0.5036                    0.0 0.5211
      b      preSMA  0    NaN    NaN     NaN    NaN                    NaN    NaN
      b        dACC  0    NaN    NaN     NaN    NaN                    NaN    NaN
      b       vmPFC  0    NaN    NaN     NaN    NaN                    N
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
PYTHONPATH=. timeout 900 $TMPDIR/dev/bin/python $TMPDIR/runcells.py reproduce_daume_2024_lfp.ipynb $TMPDIR/r26.pkl 2>&1 | grep -v "Warning\|warn\|return -self\|m = smf\|rslt = super" | sed -n '/^ *O5 *area\|artefact  *O5/,$p' | head -80
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
PYTHONPATH=. timeout 900 $TMPDIR/dev/bin/python $TMPDIR/runcells.py reproduce_daume_2024_lfp.ipynb $TMPDIR/r26.pkl > $TMPDIR/lfp_test.txt 2>&1; grep -v "Warning\|warn\|return -self\|m = smf\|rslt = super" $TMPDIR/lfp_test.txt | grep -n "CELL ERROR\|paper (Table S2)\|variants\|Nesting\|window_ms\|category selection\|paper (Table S3)"
```

```
42:CELL ERROR paper_counts = {"hippocampus": 137, "amygdala": 130, "preSMA TypeError("object of type 'numpy.float64' has no len()")
190:CELL ERROR glm_rows = [] for rd in READINGS:     for a in ["hippocampus ValueError('No objects to concatenate')
197:Nesting readings: 'amp' aligns windows on the maximum of gamma amplitude (the Methods' words),
205:window_ms           
217:category selection in 115 s: {'amygdala': 181, 'hippocampus': 94}
241:paper (Table S3): hippocampus SC estimate 0.002, t = 2.40, p = 0.017; amygdala -0.001, t = -0.75, p = 0.45
```

**Agent calls Bash**

```bash
grep -v "Warning\|warn\|return -self\|m = smf\|rslt = super" $TMPDIR/lfp_test.txt | sed -n 195,245p
```

```
reading b: n = 9, raw MI load 1 1.92e-04, load 3 2.22e-04, t(3-1) = 1.22, p = 0.2968; channels with load 1 higher: 4
paper: n = 137; t(136) = -4.0264, p = 0.0001
Nesting readings: 'amp' aligns windows on the maximum of gamma amplitude (the Methods' words),
'peak' on the maximum of the gamma-filtered signal (a gamma peak).
artefact a, nesting amp: nested 1 of 9 PAC channels (11.11%), 3.6% of all 28 hippocampal channels; channels by number of local maxima [5, 1, 2, 1]; load test in nested channels t(3-1) = nan, p = nan, load 1 nan, load 3 nan
artefact a, nesting peak: nested 8 of 9 PAC channels (88.89%), 78.6% of all 28 hippocampal channels; channels by number of local maxima [0, 0, 1, 8]; load test in nested channels t(3-1) = -0.07, p = 0.9469, load 1 4.14, load 3 4.07
artefact b, nesting amp: nested 2 of 9 PAC channels (22.22%), 7.1% of all 28 hippocampal channels; channels by number of local maxima [5, 2, 0, 2]; load test in nested channels t(3-1) = 2.07, p = 0.5014, load 1 3.98, load 3 6.39
artefact b, nesting peak: nested 7 of 9 PAC channels (77.78%), 71.4% of all 28 hippocampal channels; channels by number of local maxima [0, 0, 2, 7]; load test in nested channels t(3-1) = 0.70, p = 0.4782, load 1 2.79, load 3 3.33
paper: 110 of 137 (80.29%); t(109) = -4.10, p = 0.0001
alignment  amp  peak
window_ms           
25.0         0     1
35.0         0     8
45.0         1     8
55.0         1     8
65.0         1     8
85.0         1     8

artefact a, 30-150 Hz: n = 28, slope load 1 -2.1151 +/- 0.6988, load 3 -2.1125 +/- 0.6918, t(1-3) = -0.44, p = 0.6671
artefact b, 2-150 Hz: n = 28, slope load 1 -2.0058 +/- 0.2441, load 3 -1.9858 +/- 0.2423, t(1-3) = -6.35, p = 0.0001
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import nbformat as nbf
p="reproduce_daume_2024_lfp.ipynb"; nb=nbf.read(p,as_version=4)
for c in nb.cells:
    c.source=c.source.replace('print(pd.DataFrame(h3_rows).round(5).to_string(index=False))','print(pd.DataFrame(h3_rows).to_string(index=False, float_format=lambda v: f"{v:.4g}"))')
nbf.write(nb,p)
p="reproduce_daume_2024.ipynb"; nb=nbf.read(p,as_version=4)
c=nb.cells[4]
c.source+='''
# Columns of the units table (for the waveform measure of Extended Data Fig. 8d,e)
ucols = pd.Series({s["path"]: tuple(sorted(s["units_columns"])) for s in S})
print("\\nunits table columns, by the number of files that have them:", ucols.value_counts().to_dict())
wf = [s["units_columns"].get("waveform_mean") for s in S]
print("waveform_mean shapes (first 3 files):", wf[:3], "; files without it:", sum(w is None for w in wf))'''
nbf.write(nb,p)
p="reproduce_daume_2024_pac_neurons.ipynb"; nb=nbf.read(p,as_version=4)
c=nb.cells[5]
c.source+='''
# Uncorrected counts per area: neurons with at least one combination (channel, load) passing both tests at p < 0.01
okr = pd.DataFrame((p12 < 0.01) & (p13 < 0.01)).groupby(neuron_key.to_numpy()).any()
cu = okr.groupby(area_of.reindex(okr.index).to_numpy()).sum()
for a in sbcat.MTL:
    null = cu.loc[a].to_numpy()[1:]
    print(f"{a}, uncorrected: {int(cu.loc[a, 0])} of {int(avail[a])} neurons; shuffles mean {null.mean():.1f}, max {null.max()}")
print("combinations per neuron (channels x loads): median %d, range %d to %d" % (
    pairs.groupby(["session", "unit"]).size().median(), pairs.groupby(["session", "unit"]).size().min(), pairs.groupby(["session", "unit"]).size().max()))'''
nbf.write(nb,p)
EOF
grep -n "waveform\|units_columns" sbcat.py | head
```

```
114:    """Trials, units and electrodes of one file; no LFP and no waveforms."""
159:        "units_columns": {k: tuple(u[k].shape) for k in u.keys() if isinstance(u[k], h5py.Dataset)},
```

**Agent calls Bash**

```bash
echo bycycle >> requirements.in && sort -o requirements.in requirements.in && cat requirements.in && cd ../.. && python tools/entry.py lock entries/000673-daume-2024 && grep -n "bycycle\|neurodsp\|pandas==" entries/000673-daume-2024/requirements.lock.txt
```

```
aiohttp
bycycle
fsspec
h5py
matplotlib
numpy
pandas
remfile
requests
scipy
statsmodels
wrote entries/000673-daume-2024/requirements.lock.txt
11:bycycle==1.2.0
46:    #   bycycle
47:    #   neurodsp
54:neurodsp==2.3.0
55:    # via bycycle
59:    #   bycycle
64:    #   neurodsp
75:pandas==3.1.0
[... 3 more lines not kept]
```

**Agent**

Now updating entry.yaml and the record's notebook pointers so the check passes, then starting the full run.

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='entries/000673-daume-2024/entry.yaml'; s=open(p).read()
old='''- path: reproduce_daume_2024_pac_neurons.ipynb'''
new='''- path: reproduce_daume_2024_lfp_controls.ipynb
  title: Hippocampal PAC controls (Daume et al. 2024, dandiset 000673)
  runtime_minutes: 14
- path: reproduce_daume_2024_pac_neurons.ipynb'''
s=s.replace(old,new)
s=s.replace("runtime_minutes: 20","runtime_minutes: 24")
open(p,'w').write(s)
p='attempts/000673-daume-2024-01.yaml'; s=open(p).read()
old='''- claim: edf3-hippocampus-pac-controls
  outcome: blocked
  blocked_by: too_large
  notebook: reproduce_daume_2024_lfp.ipynb'''
new='''- claim: edf3-hippocampus-pac-controls
  outcome: blocked
  blocked_by: too_large
  notebook: reproduce_daume_2024_lfp_controls.ipynb'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)
EOF
python tools/entry.py check entries/000673-daume-2024 2>&1 | tail -5; date -u
```

```
0 error(s)
Sat Oct 31 13:04:12 UTC 2026
```

**Agent calls Bash**

```bash
time python tools/entry.py run entries/000673-daume-2024 2>&1 | tail -30; date -u
```

```
Installed kernelspec registry-000673-daume-2024 in executed/000673-daume-2024/.venv/share/jupyter/kernels/registry-000673-daume-2024
took 42 minutes; the limit is 30
pass  reproduce_daume_2024.ipynb  (191 s)
FAIL  reproduce_daume_2024_lfp.ipynb  (2536 s)
pass  reproduce_daume_2024_lfp_controls.ipynb  (1266 s)
pass  reproduce_daume_2024_pac_neurons.ipynb  (565 s)

real	76m2.847s
user	244m7.268s
sys	3m16.620s
Sat Oct 31 14:20:17 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/000673-daume-2024 && python3 - <<'EOF'
import json
d=json.load(open('reproduce_daume_2024_lfp.ipynb'))
for i,c in enumerate(d['cells']):
    if c['cell_type']!='code': continue
    m=c.get('metadata',{}).get('execution',{})
    s=m.get('iopub.execute_input'); e=m.get('shell.execute_reply')
    print(i, c['metadata'].get('tags'), s and e and (__import__('datetime').datetime.fromisoformat(e.replace('Z',''))-__import__('datetime').datetime.fromisoformat(s.replace('Z',''))).total_seconds())
print(''.join(o.get('text','') for o in d['cells'][1]['outputs']))
EOF
```

```
Exit code 1
1 None 2370.734986
2 None 1.09144
4 ['sanity'] 0.02282
5 ['sanity'] 0.143137
6 ['sanity'] 0.013999
8 ['claim:fig2a-theta-gamma-pac'] 0.354699
11 ['claim:fig2b-pac-channel-proportions'] 0.074259
14 ['claim:fig2c-hippocampus-load'] 0.099623
15 ['claim:fig2c-no-load-effect-other-areas'] 0.025083
18 ['claim:edf2b-hippocampus-load-patients'] 0.04927
21 ['claim:edf2c-low-gamma-no-load-effect'] 0.104902
24 ['claim:tables1-slow-fast-theta'] 0.715634
27 ['claim:fig2f-rt-single-trial-pac'] 5.79601
30 None 0.002407
32 ['claim:edf3a-kappa-load'] 0.063695
35 ['claim:edf3f-raw-mi-load'] 0.031815
38 ['claim:edf3e-nesting'] 0.090615
41 ['claim:methods-spectral-slope'] 0.565894
44 ['claim:fig3h-pac-category-firing'] 153.940613
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/000673-daume-2024 && python3 - <<'EOF'
import json
for nb in ['reproduce_daume_2024_lfp.ipynb','reproduce_daume_2024_lfp_controls.ipynb','reproduce_daume_2024_pac_neurons.ipynb','reproduce_daume_2024.ipynb']:
    d=json.load(open(nb))
    c=[c for c in d['cells'] if c['cell_type']=='code'][0]
    print(nb, ''.join(''.join(o.get('text','')) for o in c['outputs']))
EOF
git log --format="%h %ad %s" -3 -- entries/000673-daume-2024/entry.yaml; ls ../../transcripts/000673/; grep -o "processed in [0-9.]* min" ../../transcripts/000673/author.md | head
```

```
reproduce_daume_2024_lfp.ipynb loaded trials and units of 44 files in 62 s
LFP of 43 sessions, 1922 channels, processed in 38.4 min

reproduce_daume_2024_lfp_controls.ipynb loaded trials and units of 44 files in 63 s
LFP of 38 sessions, 586 hippocampal channels, processed in 20.0 min

reproduce_daume_2024_pac_neurons.ipynb loaded trials and units of 44 files in 65 s
category selection in 115 s
spike counts for 9640 neuron-channel-load combinations x 201 pairings in 2.3 min

reproduce_daume_2024.ipynb loaded 44 files of dandiset 000673 version 0.240118.2135 in 59 s

answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author.md
claims-check-report.md
claims-check.md
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -o "nproc[^\"]\{0,80\}" transcripts/000673/author.md | head -5; grep -o '"[0-9]*\\\\n' transcripts/000673/author.md | head -3; grep -o "pass  reproduce[^)]*)" transcripts/000673/*.md | head; grep -o "notebook ran in [0-9.]* min" transcripts/000673/*.md | head
```

```
nproc; free -g; uv --version
"\\n
"\\n
"\\n
transcripts/000673/author-answers.md:pass  reproduce_daume_2024.ipynb  (238 s)
transcripts/000673/author-answers.md:pass  reproduce_daume_2024_pac_neurons.ipynb  (702 s)
transcripts/000673/author.md:pass  reproduce_daume_2024.ipynb  (193 s)
transcripts/000673/author.md:pass  reproduce_daume_2024_lfp.ipynb  (1209 s)
transcripts/000673/author.md:pass  reproduce_daume_2024.ipynb  (196 s)
transcripts/000673/author.md:pass  reproduce_daume_2024_lfp.ipynb  (1202 s)
transcripts/000673/author.md:pass  reproduce_daume_2024_pac_neurons.ipynb  (492 s)
```

**Agent calls Bash**

```bash
cd entries/000673-daume-2024 && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONPATH=. $TMPDIR/dev/bin/python - <<'EOF'
import numpy as np, time, sbcat
rng=np.random.default_rng(0)
data=rng.standard_normal((130,1400))
t0=time.time(); tf=sbcat.TrialFilter(data); res=sbcat.channel_pac(data, tf=tf); t1=time.time(); rb=sbcat.channel_pac_bands(data, tf=tf); t2=time.time()
print('channel_pac',t1-t0,'bands',t2-t1)
both=np.arange(120)
t0=time.time()
for k in range(10): c=sbcat.pac_condition(res[4], both, rng)
print('pac_condition x1', (time.time()-t0)/10)
EOF
```

```
channel_pac 1.7365078926086426 bands 0.39758849143981934
pac_condition x1 0.021515250205993652
```

**Agent calls Bash**

```bash
cd executed/000673-daume-2024 && cat > $TMPDIR/show.py <<'EOF'
import json, sys
d=json.load(open(sys.argv[1]))
for i,c in enumerate(d['cells']):
    if c['cell_type']!='code': continue
    tags=c['metadata'].get('tags',[])
    if len(sys.argv)>2 and not any(t in sys.argv[2:] for t in tags) and str(i) not in sys.argv[2:]: continue
    print('==== cell',i,tags)
    for o in c['outputs']:
        if 'text' in o: print(''.join(o['text']))
        elif o.get('output_type')=='error': print('ERROR', o['ename'], o['evalue'])
EOF
python3 $TMPDIR/show.py reproduce_daume_2024_lfp_controls.ipynb
```

```
==== cell 1 []
loaded trials and units of 44 files in 63 s

LFP of 38 sessions, 586 hippocampal channels, processed in 20.0 min

==== cell 2 []
==== cell 4 ['sanity']
hippocampal LFP channels: 586 (paper 586) in 38 sessions of 30 patients
reading a: 144 channels with significant theta-high-gamma PAC (as in reproduce_daume_2024_lfp.ipynb), load 1 mean z 4.62, load 3 3.80
reading b: 125 channels with significant theta-high-gamma PAC (as in reproduce_daume_2024_lfp.ipynb), load 1 mean z 4.14, load 3 3.46
theta cycles (bycycle, 3-7 Hz) with their peak in 0 to 2.5 s, per correct trial: all cycles median 12 (range 6 to 16); burst cycles median 0 (range 0 to 6); trials with no burst cycle 99.9%
range of the mean asymmetry per trial (all cycles): rise-decay 0.107 to 0.840, peak-trough 0.283 to 0.746
phase-phase pairs (phase centre, amplitude centre, n): [(4, 70, 18), (4, 75, 19), (4, 80, 20), (4, 85, 21), (4, 90, 22), (4, 95, 24), (4, 100, 25), (4, 105, 26), (4, 110, 28), (4, 115, 29), (4, 120, 30), (4, 125, 31), (4, 130, 32), (4, 135, 34), (4, 140, 35), (6, 70, 12), (6, 75, 12), (6, 80, 13), (6, 85, 14), (6, 90, 15), (6, 95, 16), (6, 100, 17), (6, 105, 18), (6, 110, 18), (6, 115, 19), (6, 120, 20), (6, 125, 21), (6, 130, 22), (6, 135, 22), (6, 140, 23)]

==== cell 6 ['claim:edf3-hippocampus-pac-controls']
artefact reading a: 144 PAC channels
                                                    test   n   load1   load3  t(3-1)      p
                                    theta power, Hilbert 144  2.6732  2.6815  1.2017 0.2294
                               high-gamma power, Hilbert 144  1.0749  1.0816  2.0863 0.0353
                                      theta power, Welch 144  1.8345  1.8456  1.4606 0.1553
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
python3 $TMPDIR/show.py reproduce_daume_2024_lfp.ipynb sanity claim:fig2a-theta-gamma-pac claim:fig2c-no-load-effect-other-areas 2>&1 | head -150
```

```
==== cell 4 ['sanity']
LFP channels by area: {'hippocampus': 586, 'amygdala': 421, 'preSMA': 283, 'dACC': 325, 'vmPFC': 307} ; total 1922
LFP length minus the end of the last trial (s): min 1.1, max 211.7
LFP rate and unit as stored: {(400.0, 'microvolts', 1.0)}
per-channel s.d. of the epochs (stored units): median 34.4, range 4.26 to 525.2; 99th percentile of |LFP|: median 104.8, max 3000.9
reading a: trials removed per channel 16.0 +/- 12.0 (11.4%); trials per load after subsampling: median 58, range 15 to 70; channels with fewer than 3 per load (left out): 0
reading b: trials removed per channel 36.2 +/- 22.8 (25.9%); trials per load after subsampling: median 48, range 0 to 68; channels with fewer than 3 per load (left out): 4
paper: 20.4 +/- 13.9 trials (14.6%) removed per wire, with visual inspection
files sharing the sum of their first 4,000 LFP samples (duplicates): none
reading a: trials removed per channel, percentiles 0/25/50/75/90/100: [0.0, 9.0, 13.0, 19.0, 29.9, 106.0]; channels with none removed 3 of 1922; histogram (0-4, 5-9, ..., 50+): [123, 436, 520, 391, 186, 73, 61, 35, 26, 18, 53]
reading b: trials removed per channel, percentiles 0/25/50/75/90/100: [0.0, 20.0, 30.0, 47.0, 69.0, 132.0]; channels with none removed 2 of 1922; histogram (0-4, 5-9, ..., 50+): [18, 57, 154, 239, 227, 237, 225, 135, 113, 81, 436]

==== cell 5 ['sanity']
sub-26 session 1: ['sub-26/sub-26_ses-1_ecephys+image.nwb']
channel 33 (hippocampus_right): the paper's code removes 17 trials
  reading a removes 4; 4 of them among the paper's 17, 0 that the paper kept
  reading b removes 9; 4 of them among the paper's 17, 5 that the paper kept

==== cell 6 ['sanity']
{'shift_-2.0': 1.58, 'shift_-1.0': 1.4, 'shift_0.0': 2.49}
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
python3 $TMPDIR/show.py reproduce_daume_2024_lfp.ipynb claim:fig2f-rt-single-trial-pac claim:edf3e-nesting claim:fig3h-pac-category-firing claim:edf2b-hippocampus-load-patients claim:edf3f-raw-mi-load 2>&1
```

```
==== cell 18 ['claim:edf2b-hippocampus-load-patients']
reading        area  patients  load1  load3  t(1-3)      p  patients_load1_higher
      a hippocampus        23 3.9687 3.2301  2.2616 0.0095                     18
      a    amygdala        27 2.8140 3.1784 -1.6857 0.1021                     11
      a      preSMA         6 1.7115 4.7877 -1.1594 0.3120                      2
      a        dACC         8 0.9797 0.9948 -0.0417 0.9921                      3
      a       vmPFC        12 2.1086 2.1599 -0.1211 0.9233                      7
      b hippocampus        20 3.6051 3.1090  1.5014 0.1127                     14
      b    amygdala        25 2.6486 3.0270 -1.6992 0.1086                      9
      b      preSMA         5 2.0252 5.4497 -0.9968 0.4411                      2
      b        dACC         4 1.7814 0.5825  3.6894 0.1240                      4
      b       vmPFC        10 1.9590 2.2559 -0.6765 0.5230                      4
paper: hippocampus n = 23 patients, p = 0.0049

==== cell 27 ['claim:fig2f-rt-single-trial-pac']
artefact O5        area  channels  trials  estimate        t       p  interaction_p  converged
       a  a hippocampus       144   16103  23.76932  1.14855 0.25074        0.00747       True
       a  b hippocampus       144   16103   0.00943  0.46569 0.64144        0.13131       True
       a  a    amygdala       130   14469  12.40929  0.60994 0.54190        0.03180       True
       a  b    amygdala       130   14469  -0.05230 -1.99550 0.04599        0.14715       True
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
python3 $TMPDIR/show.py reproduce_daume_2024.ipynb 4 claim:category-cell-counts claim:edf8fgh-frontal-controls 2>&1 | tail -40; python3 $TMPDIR/show.py reproduce_daume_2024_pac_neurons.ipynb claim:pac-neuron-counts
```

```
==== cell 22 ['claim:category-cell-counts']
selection and 500 label shuffles in 116 s
       area  neurons  category  percent  paper  within_10pct  null_mean  null_p99  p_shuffle  above_p99
hippocampus      360        94   26.111     89          True     16.794     26.01      0.002       True
   amygdala      496       181   36.492    181          True     23.458     37.00      0.002       True
     preSMA      204        18    8.824     18          True      9.450     17.00      0.010       True
       dACC      188        13    6.915     14          True      8.300     16.00      0.088      False
      vmPFC      206        40   19.417     37          True      9.522     18.00      0.002       True

category neurons per patient (MTL):
subject   1  10  11  12  13  14  15  16  17  18  19   2  20  21  22  23  24  25  26  27  28  29   3  30  31  32  33  34  35  36   4   5   6   7   8   9
sum      22   3   6   7   0   2   7  17  14   1  28   9   4  21   6   1   1   4  21   3   9   3   8   1  17   8   7   4   0   1   9  11   4   3   9   4
size     48  23  15  21   3   4  22  30  45  27  77  25  28  40  68   6   7  11  35  12  21  22  13  16  50  27  30  12   1  10  21  22  12  17  23  12

preferred categories of MTL category neurons: {1: 88, 2: 56, 3: 44, 4: 48, 5: 39}
post hoc two-sided p < 0.05: {'hippocampus': 87, 'amygdala': 174, 'preSMA': 18, 'dACC': 14, 'vmPFC': 41}
post hoc two-sided p < 0.1: {'hippocampus': 94, 'amygdala': 182, 'preSMA': 19, 'dACC': 15, 'vmPFC': 43}

==== cell 42 ['claim:edf8fgh-frontal-controls']
  area  paper_n  min_incorrect reading   n  correct  incorrect       t      p
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
python3 $TMPDIR/show.py reproduce_daume_2024.ipynb 4 | tail -4; date -u
```

```
units table columns, by the number of files that have them: {('clusterID_orig', 'electrodes', 'id', 'spike_times', 'spike_times_index', 'waveform_mean', 'waveform_sd', 'waveforms', 'waveforms_index', 'waveforms_index_index', 'waveforms_isolation_distance', 'waveforms_mean_proj_dist', 'waveforms_mean_snr', 'waveforms_peak_snr'): 43, ('clusterID_orig', 'electrodes', 'id', 'spike_times', 'spike_times_index', 'waveforms', 'waveforms_index', 'waveforms_index_index', 'waveforms_isolation_distance', 'waveforms_mean_proj_dist', 'waveforms_mean_snr', 'waveforms_peak_snr'): 1}
waveform_mean shapes (first 3 files): [(46, 256), (41, 256), (36, 256)] ; files without it: 1

Sat Oct 31 14:22:18 UTC 2026
```

**Agent**

Now timing the spike-field coherence core on one session, so the SFC claims' `too_large` block rests on a measured estimate.

**Agent calls Bash**

```bash
cd entries/000673-daume-2024 && OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 PYTHONPATH=. $TMPDIR/dev/bin/python - <<'EOF'
import numpy as np, time, sbcat
from scipy import fft as sfft
A=sbcat.list_assets(); S=sbcat.load_all([a for a in A if 'sub-26_ses-1' in a['path']]); s=S[0]
x,rate,start=sbcat.read_lfp(s['asset'])
tr=s['trials']; on=tr.timestamps_Maintenance.to_numpy(); ok=tr.correct.to_numpy()
i0=np.round((on-0.5-start)*rate).astype(int)
data=x[i0[:,None]+np.arange(1400)[None,:],0].astype(np.float64)[ok]
freqs=np.logspace(np.log10(2),np.log10(150),40); cyc=np.logspace(np.log10(3),np.log10(10),40)
t0=time.time()
T,n=data.shape; ph=np.empty((T,1000,40),np.float32)
for j,(f,c) in enumerate(zip(freqs,cyc)):
    sd=c/(2*np.pi*f); t=np.arange(-4*sd,4*sd+1/rate,1/rate); w=np.exp(2j*np.pi*f*t)*np.exp(-t**2/(2*sd**2))
    m=n+len(w)-1; nf=sfft.next_fast_len(m); y=sfft.ifft(sfft.fft(data,nf,axis=1)*sfft.fft(w,nf)[None,:],axis=1); h=(len(w)-1)//2
    ph[:,:,j]=np.angle(y[:,h:h+n])[:,200:1200]
tw=time.time()-t0
print('wavelets per channel', tw)
rng=np.random.default_rng(0)
# one pair: 300 spikes in condition A, 200 in B
def mvl(trial,samp): return np.abs(np.exp(1j*ph[trial,samp,:]).mean(0))
nA,nB=300,200
trA=rng.integers(0,T,nA); sA=rng.integers(0,1000,nA); trB=rng.integers(0,T,nB); sB=rng.integers(0,1000,nB)
t0=time.time()
E=np.exp(1j*ph[trA,sA,:]).astype(np.complex64)
sub=np.array([rng.choice(nA,nB,replace=False) for _ in range(500)])
v=np.abs(E[sub].mean(1)).mean(0)
t1=time.time()-t0
t0=time.time()
for k in range(500):
    js=np.clip(sA+rng.integers(-100,101,nA),0,999)
    Ej=np.exp(1j*ph[trA,js,:]).astype(np.complex64)
    vv=np.abs(Ej[sub[:1]].mean(1))
t2=time.time()-t0
print('500 subsamples', t1, '500 surrogates (one subsample each)', t2, '500x500', t2+500*t1)
EOF
```

```
wavelets per channel 0.2728719711303711
500 subsamples 0.015526056289672852 500 surrogates (one subsample each) 0.2948617935180664 500x500 8.057889938354492
```

**Agent calls Bash**

```bash
cd  cat questions/000023.yaml | head -40; ls schemas
```

```
# Questions from attempt 000023-berg-2020-01 (author, 2026-10-23) about the claims file
# claims/000023/10.1101-2020.03.31.018820.yaml. Each is asked under docs/protocol.md, Author, step 1.6;
# the attempt runs every reading it can see, or blocks the claim as methods_underspecified until the
# question is answered.
dandiset: "000023"
paper: doi:10.1101/2020.03.31.018820
questions:
- claim: features-and-labels-link
  also: [cohort-cells, cohort-donors, cohort-type-counts, fig3d-depth-by-type, fig4e-human-ephys-anova,
    fig4-glp2r-sag, edtable1-species-ephys, edfig6-classifier-human-ephys, fig5c-frem3-ephys-depth,
    fig6-deep-ephys-anova, fig6c-carm1p1-upstroke-rin, fig6c-col22a1-rin-fi-sag, fig2ef-pathology-ephys]
  asked: 2026-10-23
  question: The criterion matches cells "by the specimen ID (SpecimenID in the code's cell table)", but
    no file carries a SpecimenID. Each file carries the donor (in its cell name, such as
    H17.06.003.11.07.04, and as subject_id) and an ephys session id (session_id, in the file name)
    that is 13 to 685 below one SpecimenID of the same donor in the code's table. Should cells be
    matched (M1) only through a SpecimenID stored in the files, which matches none, or (M2) through
    the SpecimenID recovered from the file, the next id of the same donor in the code's table, with
    the code's per-cell features as the check?
  passage: None in the paper; the Methods name no identifiers. The code joins its tables on SpecimenID
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/questions.schema.json'));print(json.dumps(s,indent=0)[:2500])"; grep -n "verifications" -A60 schemas/attempt.schema.json | grep -n "agrees\|outcome\|reason\|response\|reviewed\|by\|kind\|date\|required\|proposed" | head -40
```

```
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import json;s=json.load(open('schemas/questions.schema.json'));print(json.dumps(s,indent=0)[:2500])
                            ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'schemas/questions.schema.json'
6:339-        "required": [
7:340-          "date",
8:341-          "kind",
9:342-          "by",
13:346-          "date": {
15:348-            "format": "date"
17:350-          "kind": {
24:357-          "by": {
32:365-              "required": [
34:367-                "agrees"
40:373-                "agrees": {
43:376-                "reason": {
44:377-                  "description": "The verifier's reason, in its own words.",
47:380-                "response": {
48:381-                  "description": "What the author changed or replied, kept apart from the verifier's reason.",
[... 2 more lines not kept]
```

**Agent**

Writing the questions file (the V-test misreading the verifier reported).

**Agent calls Write**

```json
{
 "file_path": "questions/000673.yaml",
 "content": "# Questions from attempt 000673-daume-2024-01 (author-revise-1, 2026-10-31) about the claims file\n# claims/000673/10.1038-s41586-024-07309-z.yaml. Each is asked under docs/protocol.md, Author, step 1.6,\n# and \"Hand over for verification\"; the claim is tested as the file has it.\ndandiset: \"000673\"\npaper: doi:10.1038/s41586-024-07309-z\nquestions:\n- claim: edf3-hippocampus-pac-controls\n  asked: 2026-10-31\n  question: The criterion's reading (a) of the preferred phase test is \"a V test of the per-channel\n    differences against 0\", judged with the rule that the claim is reproduced when \"none of the tests\n    gives p < 0.05\". A V test against a mean direction of 0 tests whether the differences are\n    concentrated around 0, so a small p supports \"no phase shift\" and is not evidence of a difference.\n    Read with the rule, reading (a) counts as a failure exactly when the paper's finding holds. Should\n    reading (a) be dropped, or judged the other way (no shift when the V test is significant), or\n    should the preferred phase part rest only on reading (b), the permutation t-test of the wrapped\n    differences against 0?\n  passage: Extended Data Fig. 3g legend, \"The difference in theta phase at which gamma amplitude was\n    maximal between the two load conditions was not significantly different from zero (bottom\n    part)\"; the legend's t-tests cover panels a-f and h, not g.\n  why: Here the V test gives p < 0.0001 under both artefact readings (mean resultant length 0.94,\n    circular mean -1.6 degrees), while the permutation t-test of reading (b) gives p = 0.71. Under the\n    criterion as written the V test adds one more test with p < 0.05. In this attempt the outcome is\n    not_reproduced either way, because the high-gamma power and gamma peak frequency tests also give p\n    < 0.05 under the adopted artefact reading, so the question bears on later attempts.\n  reported_by: verifier-1\n"
}
```

```
File created successfully at: questions/000673.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -rn "questions" tools/*.py | head -10; grep -rhn "^  [a-z_]*:" questions/*.yaml | sed 's/^[0-9]*://' | awk '{print $1}' | sort | uniq -c | sort -rn | head -15
```

```
tools/build_site.py:322:    (papers/manifest.yaml), each claims file's last check, and each attempt's open questions."""
tools/build_site.py:325:    checks, questions, items = {}, {}, {}
tools/build_site.py:330:    for path in sorted((ROOT / "questions").glob("*.yaml")):
tools/build_site.py:332:        q = q.get("questions", []) if isinstance(q, dict) else q
tools/build_site.py:333:        questions[key_of_dir(path.stem)] = sum(1 for x in q if not x.get("answered"))
tools/build_site.py:335:    return {"papers": {key_of_dir(str(k)): v for k, v in papers.items()}, "checks": checks, "questions": questions,
tools/build_site.py:498:                  ("attempt", "Attempt"), ("questions", "Questions"), ("verified", "Verified")]
tools/build_site.py:539:    inputs = data.get("pipeline") or {"papers": {}, "checks": {}, "questions": {}}
tools/build_site.py:553:        open_q = inputs["questions"].get(d, 0)
tools/build_site.py:569:            "questions": ("todo", f"{open_q} open") if open_q else ("none", ""),
    203 why:
    203 question:
    199 passage:
    199 asked:
    125 answered:
    125 answer:
     36 also:
     26 attempt:
      1 reported_by:
```

**Agent calls Bash**

```bash
sed -i 's/^  reported_by: verifier-1$/  attempt: 000673-daume-2024-01/' questions/000673.yaml; grep -rh -B2 "^  attempt:" questions/*.yaml | head -5; tail -2 questions/000673.yaml; python -c "import yaml;yaml.safe_load(open('questions/000673.yaml'))"
```

```
questions:
- claim: pt-tagged-units
  attempt: 000006-economo-2018-02
--
    opening comment (Unit inclusion) and the pt-tagged-units criterion.
    < 0.05 under the adopted artefact reading, so the question bears on later attempts.
  attempt: 000673-daume-2024-01
```

**Agent calls Bash**

```bash
sed -n 205,218p claims/000673/10.1038-s41586-024-07309-z.yaml; sed -n 358,388p claims/000673/10.1038-s41586-024-07309-z.yaml; sed -n 1242,1272p claims/000673/10.1038-s41586-024-07309-z.yaml
```

```
- id: fig2a-theta-gamma-pac
  statement: Across all recorded channels, PAC during maintenance was strongest between theta
    phase (3-7 Hz) and the amplitude of a low (30-55 Hz) and a high (70-140 Hz) gamma band.
  source: Results, Hippocampal PAC is modulated by WM load, paragraph 1; Figure 2a
  quote: PAC was strongest between the phase in the theta range (3–7 Hz) and the amplitude in two
    different gamma-frequency bands ... a lower (30–55 Hz) and a higher gamma range (70–140 Hz)
  criterion: Comodulogram as in cfc_tort_comodulogram.m (Methods, PAC; O1, O2) on the -0.5 to 3 s
    epochs of subsampled correct trials of both loads, cut to 0 to 2.5 s, phase centres 2 to 14
    Hz (2 Hz bandwidth), amplitude centres 30 to 150 Hz in 5 Hz steps (bandwidth twice the phase
    centre), 18 bins, z-scored against 200 trial-shuffled surrogates; averaged over channels
    (1,917 in the paper). Reproduced when the largest mean z lies at a phase centre of 4 or 6 Hz,
    and the amplitude profile at those phase centres has a local maximum within 30 to 55 Hz and
    another within 70 to 140 Hz.
- id: fig2b-pac-channel-proportions
- id: fig2f-rt-single-trial-pac
  statement: In the hippocampus, stronger single-trial theta-high-gamma PAC went with faster RTs,
    while no such relation held in the amygdala or vmPFC.
  source: Results, Hippocampal PAC is modulated by WM load, paragraph 2; Figure 2f; Supplementary
    Table S2
  quote: In the hippocampus, faster RTs were associated with stronger single-trial estimates of
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/md_lfp.py <<'PYEOF'
import nbformat as nbf
def setmd(nb, prefix, text, after_tag=None):
    if after_tag:
        idx = [i for i, c in enumerate(nb.cells) if after_tag in c.metadata.get("tags", [])][-1]
        for j in range(idx + 1, len(nb.cells)):
            if nb.cells[j].cell_type == "markdown" and nb.cells[j].source.startswith("**Result"):
                nb.cells[j].source = text; return
        raise KeyError(after_tag)
    for c in nb.cells:
        if c.cell_type == "markdown" and c.source.startswith(prefix):
            c.source = text; return
    raise KeyError(prefix)

p = "entries/000673-daume-2024/reproduce_daume_2024_lfp.ipynb"
nb = nbf.read(p, as_version=4)
nb.cells[0].source = nb.cells[0].source.replace(
    "readings of the artefact rejection (O1): (a) on the epochs, (b) on whole trials.",
    "readings of the artefact rejection (O1): (a) on the epochs, (b) on whole trials. Where they\n"
    "disagree, (a) is adopted: on the one channel whose rejected trials the paper's code ships\n"
    "(`artif_trials.mat`, sub-26 session 1, channel 33), every trial (a) removes is among the paper's,\n"
    "while (b) removes 5 trials the paper kept (data check below).")
setmd(nb, None, """**Result: reproduced.** Under reading (a), over 1,922 channels, the largest mean z (2.16) is at
phase 4 Hz and amplitude 80 Hz; at 4 Hz the amplitude profile has local maxima at 50 Hz (within 30
to 55) and 80 Hz (within 70 to 140). Under reading (b), computed for phase centres 2 to 8 Hz over
1,918 channels, the largest mean z (1.73) is again at 4 Hz and 80 Hz, with local maxima at 45 and
80 Hz. Both readings meet the criterion.""", after_tag="claim:fig2a-theta-gamma-pac")
setmd(nb, None, """**Result: fig2c-hippocampus-load reproduced.** Hippocampal PAC is lower in load 3 than in load 1
under both readings (a: 144 channels, t = -4.16, FDR p = 0.0010; b: 125 channels, t = -3.05, FDR p
= 0.014).

**Result: fig2c-no-load-effect-other-areas not reproduced.** Under reading (a) the pre-SMA (17
channels, load 3 higher, FDR p = 0.0017) and the amygdala (130 channels, load 3 higher, FDR p =
0.0475) differ between loads; under (b) the pre-SMA (FDR p = 0.014) and the dACC (8 channels,
load 1 higher, FDR p = 0.014) do. The vmPFC does not differ under either (p = 0.93, 0.94). The
pre-SMA channels come from five patients; four channels of sub-4 (session 37) have z values of 19
to 25 in load 3 against 4 to 7 in load 1, and seven of sub-11 (session 3) are also higher in load
3. Load 3 is higher in 14 of the 17 channels (Wilcoxon p = 0.0011), and without the three channels
of largest excess the test still gives p = 0.0045 under reading (a); under (b) it gives p = 0.059.""",
      after_tag="claim:fig2c-no-load-effect-other-areas")
setmd(nb, None, """**Result: reproduced, resting on an assumption.** Under reading (a), 23 patients have hippocampal
PAC channels (paper 23), their means are higher in load 1 (3.97 against 3.23, p = 0.0095; 18 of 23
patients), and no other area differs (p >= 0.10). Under reading (b) the hippocampus gives p = 0.11
over 20 patients. Reading (a) is adopted (header and data check: the paper's own rejected trials
on its example channel include every trial (a) removes).""", after_tag="claim:edf2b-hippocampus-load-patients")
setmd(nb, None, """**Result: not reproduced.** No combination of artefact reading (a, b) and single-trial PAC reading
(O5 a, b) gives a significant hippocampal PAC term (p = 0.25, 0.64, 0.19, 0.20); under artefact
reading (a) its estimate is positive. The amygdala term reaches p = 0.046 under (a, O5 b). As
variants under reading (a), with RTs below 10 s only the hippocampal term is negative but not
significant (p = 0.16 and 0.094); with log10 RT it is negative under O5 (b) (t = -2.72, p = 0.0066)
and not under O5 (a) (p = 0.13). The claim's test is on RT itself (Table S2 gives the estimate in
ms), so the variants do not change the outcome.""", after_tag="claim:fig2f-rt-single-trial-pac")
setmd(nb, None, """**Result: reproduced, resting on an assumption.** Aligned on gamma peaks, 105 of 144 PAC channels
(72.92%) are nested under reading (a), within tolerance of 110, and PAC is lower in load 3 in them
(t = -3.61, p = 0.0002). Aligned on gamma amplitude maxima, as the Methods' words read, only 9 are
nested (6.25%) and the load test fails (p = 0.77). The count under the peak alignment is 104 to 114
for windows of 35 to 85 ms (30 for 25 ms), and 4 to 15 under the amplitude alignment for every
window, so the outcome rests on the alignment and not on the window. The alignment on gamma peaks
is adopted (see the attempt record).""", after_tag="claim:edf3e-nesting")
setmd(nb, None, """**Result: not reproduced.** Over 166 hippocampal pairs of a category neuron and a PAC channel of
its bundle (paper 151) and 450 amygdala pairs (paper 423), under artefact reading (a), the
hippocampal spike count term is not positive with p < 0.05 under any reading: all trials, O5 (a)
p = 0.15 and (b) p = 0.77; preferred trials, O5 (a) p = 0.15 (estimate negative) and (b) t = -2.44,
p = 0.015, negative, the opposite sign to the paper's. The amygdala term is not significant under
any reading (p >= 0.21), as in the paper. Under artefact reading (b) the result is the same
(hippocampus p = 0.09 to 0.70 for positive estimates, preferred O5 (b) negative with p = 0.024).
The SC x load interaction is significant in the hippocampus under every reading (p <= 0.002), so
the load 1 slope that the SC term estimates differs from the load 3 slope.""",
      after_tag="claim:fig3h-pac-category-firing")
for c in nb.cells:
    if c.cell_type == "markdown" and c.source.startswith("## Summary"):
        c.source = """## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| fig2a-theta-gamma-pac | reproduced |
| fig2b-pac-channel-proportions | partially reproduced (17 pre-SMA channels against 5) |
| fig2c-hippocampus-load | reproduced |
| fig2c-no-load-effect-other-areas | not reproduced (pre-SMA, and amygdala or dACC) |
| edf2b-hippocampus-load-patients | reproduced, resting on artefact reading (a) |
| edf2c-low-gamma-no-load-effect | not reproduced (pre-SMA) |
| tables1-slow-fast-theta | not reproduced (pre-SMA tests also significant) |
| fig2f-rt-single-trial-pac | not reproduced |
| edf3a-kappa-load | reproduced |
| edf3e-nesting | reproduced, resting on the alignment on gamma peaks |
| edf3f-raw-mi-load | reproduced, resting on artefact reading (a) |
| methods-spectral-slope | not reproduced, resting on the 2 to 150 Hz range |
| fig3h-pac-category-firing | not reproduced |
| edf3-hippocampus-pac-controls | in `reproduce_daume_2024_lfp_controls.ipynb` |

How the analysis differs from the paper's: the artefact rejection is the automated part only
(the visual inspection cannot be repeated), under two readings of the span it is computed on;
reading (a) removes 11.4% of trials per channel and reading (b) 25.9%, against the paper's 14.6%
with visual inspection; where the readings disagree, (a) is adopted, as the paper's own rejected
trials on its example channel contain every trial (a) removes and only 4 of the 9 that (b)
removes. The single-trial PAC, the nesting alignment, the slope's frequency range and the power
estimate are not given by the paper. Mixed models are fitted with statsmodels in place of fitglme.

What was found about the dataset: the LFP of 1,922 channels is there for 43 of the 44 sessions
(sub-20 has none), at 400 Hz in microvolts, and shares the trial clock (probe-locked contrast,
37 of 43 sessions). The files do not mark the trials or channels the paper's visual inspection
removed. Without them, the 17 significant pre-SMA channels, with a mean z of 6.87 in load 3
against 1.81 in load 1 under reading (a), decide several of the absence claims."""
nbf.write(nb, p)

p = "entries/000673-daume-2024/reproduce_daume_2024_lfp_controls.ipynb"
nb = nbf.read(p, as_version=4)
setmd(nb, None, """**Result: not reproduced, resting on an assumption.** Under artefact reading (a), the one adopted,
over 144 PAC channels, two load tests give p < 0.05: high-gamma power is higher in load 3 (Hilbert
t = 2.09, p = 0.035; Welch t = 2.69, p = 0.006), and the gamma peak frequency is higher in load 3
(86.8 against 93.0 Hz, t = 3.04, p = 0.003; as the coordinate of the single largest bin, p = 0.34).
Theta power (p = 0.23, 0.16), rise-decay and peak-trough symmetry (all cycles p = 0.34 and 0.50;
burst cycles, found in only 8 channels in both loads, p = 0.17 and 0.79), phase-phase locking
(1:21 p = 0.90; each centre pair p = 0.82), the theta peak frequency (p = 0.49; largest bin p =
0.080) and the preferred phase t-test (p = 0.71) do not differ. The V test of the phase
differences against 0 gives p < 0.0001 (mean resultant length 0.94, circular mean -1.6 degrees),
which shows differences concentrated at 0; whether the criterion's rule should count it is asked
of a reader. No asymmetry differs from 0.5 (p >= 0.072). Under artefact reading (b) (125
channels) no load test gives p < 0.05 (high-gamma power p = 0.13 and 0.058; gamma peak frequency
p = 0.17), so the outcome rests on reading (a).""", after_tag="claim:edf3-hippocampus-pac-controls")
for c in nb.cells:
    if c.cell_type == "markdown" and c.source.startswith("## Summary"):
        c.source = """## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

| Claim | Outcome |
|---|---|
| edf3-hippocampus-pac-controls | not reproduced, resting on artefact reading (a) (high-gamma power and gamma peak frequency differ between loads) |

How the analysis differs from the paper's: the artefact rejection is the automated part only,
reading (a) adopted as in `reproduce_daume_2024_lfp.ipynb`; bycycle 1.2 is run with a replacement
of its burst detection that applies the same default thresholds to a writable copy (it fails
under pandas 3 otherwise); the power estimate, the phase-phase ratio, whether only burst cycles
count, and the definition of the peak frequency are not given and are each shown under two
readings.

What was found about the dataset: nothing beyond `reproduce_daume_2024_lfp.ipynb`. With
bycycle's default burst thresholds, 99.9% of the 0 to 2.5 s windows of correct trials have no
burst cycle."""
nbf.write(nb, p)
print("ok")
PYEOF
python $TMPDIR/md_lfp.py
```

```
ok
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import nbformat as nbf
fx={"entries/000673-daume-2024/reproduce_daume_2024_lfp_controls.ipynb":[("the gamma peak frequency is higher in load 3\n(86.8 against 93.0 Hz, t = 3.04","the gamma peak frequency is higher in load 3\n(93.0 against 86.8 Hz in load 1, t = 3.04")],
"entries/000673-daume-2024/reproduce_daume_2024_lfp.ipynb":[("(hippocampus p = 0.09 to 0.70 for positive estimates, preferred O5 (b) negative with p = 0.024)","(hippocampus: positive estimates with p = 0.090 and 0.65, negative ones with p = 0.70 and, on\npreferred trials under O5 (b), p = 0.024)"),
("pre-SMA channels come from five patients; four channels of sub-4 (session 37) have z values of 19\nto 25 in load 3 against 4 to 7 in load 1","pre-SMA channels come from six patients; four channels of sub-4 (session 37) have z values of 19\nto 25 in load 3 against 3.5 to 6.8 in load 1")]}
for p,reps in fx.items():
    nb=nbf.read(p,as_version=4)
    for a,b in reps:
        n=sum(a in c.source for c in nb.cells); assert n==1,(a,n)
        for c in nb.cells: c.source=c.source.replace(a,b)
    nbf.write(nb,p)
EOF
date -u
```

```
Sat Oct 31 14:24:11 UTC 2026
```

**Agent calls Bash**

```bash
python3 -c "
import nbformat as nbf
nb=nbf.read('entries/000673-daume-2024/reproduce_daume_2024_pac_neurons.ipynb',as_version=4)
for i in [6,10,16,19,22,23]: print(i, nb.cells[i].source,'\n')
"
```

```
6 **Result: partially reproduced.** With FDR over the combinations of an area and load (O9 a), 8 of
269 hippocampal (2.97%) and 5 of 422 amygdala neurons (1.18%) qualify, against 79 of 212 and 163
of 358; with FDR over each neuron's channels (b), 12 and 24. Both counts exceed every shuffled
count but one (p = 0.005 in both areas under both readings), so the selection finds more than
chance, but the counts are far out of tolerance. 

10 **Result: blocked.** With 8 hippocampal and 5 amygdala PAC neurons (paper 79 and 163), the
overlap (4 of 8 and 2 of 5) does not test the paper's populations; the tests are printed above. 

16 **Result: blocked.** The tests above are on 8 hippocampal PAC neurons, against the paper's 79, and
are not a test of the paper's population. 

19 **Result: blocked.** The tests above are on 5 amygdala PAC neurons, against the paper's 163. 

22 **Result: blocked.** The fits above use 8 hippocampal and 5 amygdala neuron-channel pairs, against
the paper's 79 and 163. 

23 ## Summary

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import nbformat as nbf
p='entries/000673-daume-2024/reproduce_daume_2024_pac_neurons.ipynb'
nb=nbf.read(p,as_version=4)
nb.cells[6].source="""**Result: partially reproduced.** With FDR over the combinations of an area and load (O9 a), 8 of
269 hippocampal (2.97%) and 5 of 422 amygdala neurons (1.18%) qualify, against 79 of 212 and 163
of 358; with FDR over each neuron's channels (b), 12 and 24. Both counts exceed every shuffled
count but one (p = 0.005 in both areas under both readings), so the selection finds more than
chance, but the counts are far out of tolerance. Even without any correction, 41 hippocampal and
66 amygdala neurons have a combination passing both tests at p < 0.01 (shuffles at most 13 and
14), fewer than the paper's counts after FDR. The paper's plot_PAC_neuron.m fits the three GLMs to
the 20 aggregated bin counts of one neuron-channel pair, with no random effect (fitglme with
fixed effects only), as `sbcat.py` does, so neither a per-trial layout nor a random effect is the
difference."""
nbf.write(nb,p)
p='entries/000673-daume-2024/reproduce_daume_2024.ipynb'
nb=nbf.read(p,as_version=4)
c=nb.cells[0]
c.source=c.source.replace("This notebook tests the claims on behaviour and single-neuron firing. The LFP claims are in\n`reproduce_daume_2024_lfp.ipynb`.","This notebook tests the claims on behaviour and single-neuron firing. The LFP claims are in\n`reproduce_daume_2024_lfp.ipynb` and `reproduce_daume_2024_lfp_controls.ipynb`.")
c.source=c.source.replace("| SFC, noise correlation and decoding claims | blocked (see the attempt record) |","| fig3h-pac-category-firing | in `reproduce_daume_2024_lfp.ipynb` |\n| SFC, noise correlation and decoding claims | blocked (see the attempt record) |")
assert "lfp_controls" in c.source and "fig3h" in c.source
def setres(tag, text):
    idx=[i for i,c in enumerate(nb.cells) if tag in c.metadata.get('tags',[])][-1]
    for j in range(idx+1,len(nb.cells)):
        if nb.cells[j].cell_type=='markdown' and nb.cells[j].source.startswith('**Result'):
            nb.cells[j].source=text; return
    raise KeyError(tag)
setres('claim:category-cell-counts',"""**Result: partially reproduced.** Every count is within 10% of the paper's (hippocampus 94, amygdala
181, vmPFC 40, pre-SMA 18, dACC 13), and the hippocampus, amygdala and vmPFC exceed the 99th
percentile of the shuffle null (p = 0.002 each). The dACC does not (p = 0.088), but the pre-SMA's
18 also exceeds its 99th percentile of 17 (p = 0.010), where the paper reports no excess. The
pre-SMA sits at the boundary: 18 is one above the 99th percentile, and p = 0.010 equals the 0.01
threshold, so with 500 shuffles the two forms of the rule do not separate it from chance clearly.""")
setres('claim:fig3b-persistent-activity',"""**Result: partially reproduced.** Over 275 MTL category neurons (paper 270), maintenance rates
exceed baseline in preferred and non-preferred trials under both readings (p = 0.0001 each). The
preferred against non-preferred test gives p = 0.0013 in % of baseline (b) but p = 0.072 in Hz
(a), so the criterion (all three tests under both readings) holds only in part. Under reading (b)
alone, the reading adopted for the claims that leave the choice open, all three tests hold.""")
setres('claim:edf8fgh-frontal-controls',"""**Result: blocked** (panels f and g need spike-field coherence, not run). Panel h: in % of baseline
(the adopted reading of O6) with at least one incorrect trial, the n are the paper's exactly (pre-SMA
201, dACC 180, vmPFC 201) and no area differs (p = 0.54, 0.71, 0.97); in Hz with at least one
incorrect trial the pre-SMA differs (incorrect 3.07 against correct 2.91 Hz, p = 0.039), with two
or three incorrect trials it does not (p = 0.089, 0.11). That the % of baseline reading gives the
paper's n in all three areas (neurons with no baseline spike drop out) supports it as the reading
of the paper's firing rate tests.""")
for c in nb.cells:
    if c.cell_type=='markdown' and c.source.startswith('## Summary'):
        c.source=c.source.replace("| edf8fgh-frontal-controls | blocked (SFC not run; panel h shown) |","| edf8fgh-frontal-controls | blocked (SFC not run; panel h holds in % of baseline) |")
        c.source=c.source.replace("The LFP claims are in `reproduce_daume_2024_lfp.ipynb` and","The LFP claims are in `reproduce_daume_2024_lfp.ipynb` and `reproduce_daume_2024_lfp_controls.ipynb`, and")
        c.source=c.source.replace("and RTs reach 74 s.","and RTs reach 74 s. The units table holds waveforms (`waveforms`, and `waveform_mean` of 256\nsamples in 43 of the 44 files).")
        print(c.source[-900:])
nbf.write(nb,p)
EOF
```

```
llows the paper's code, with
the shuffled-label null drawn by shuffling the labels of a session's presentations together; the
permutation tests flip the signs of paired differences (10,000 draws); whether rates are compared
in Hz or in % of baseline is not stated, both are shown, and % of baseline is adopted where they
disagree; units recorded in several sessions of
one patient are counted once per session, as the paper's totals do.

What was found about the dataset: every count of the paper is in it; the trials table agrees with
the TTL events; spike times are unsorted in four units of two files (three in sub-13 jump back by
about 1,320 s, as if two spike trains were concatenated); the maintenance period lasts 2.53 to
3.20 s, against 2.55 to 2.85 s in the Methods; and RTs reach 74 s. The units table holds waveforms (`waveforms`, and `waveform_mean` of 256
samples in 43 of the 44 files).
```

**Agent**

Updating the README, then the attempt record.

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='entries/000673-daume-2024/README.md'; s=open(p).read()
old_start=s.index('| Claims | Outcome |'); old_end=s.index('The attempt record,')
table='''| Claims | Outcome |
|---|---|
| Cohort counts, behaviour (RT, accuracy, false negatives) | Reproduced (4) |
| Category neuron counts; their persistent and selective maintenance activity, overall and by area | Partially reproduced (3) |
| Category neurons fire more in correct trials; no RT effect | Reproduced (2; one rests on rates as % of baseline) |
| Category neurons fire more in load 1 (preferred trials) | Not reproduced (rests on rates as % of baseline) |
| Theta-gamma comodulogram; hippocampal PAC lower in load 3, per channel and per patient; kappa; raw MI; nesting | Reproduced (6; three rest on an assumption) |
| Proportions of PAC channels | Partially reproduced (pre-SMA 17 channels against 5) |
| No load effect in other areas or for low gamma; only hippocampal high gamma in Table S1 | Not reproduced (pre-SMA channels differ) |
| Single-trial PAC predicts RT or category neuron firing; spectral slope does not differ; PAC controls of Extended Data Fig. 3 | Not reproduced (4) |
| PAC neuron counts | Partially reproduced (8 and 5 against 79 and 163, above chance) |
| Spike-field coherence; claims on PAC neurons, noise correlations and decoding | Blocked (32) |

'''
s=s[:old_start]+table+s[old_end:]
s=s.replace('''- `reproduce_daume_2024_lfp.ipynb`: LFP phase-amplitude coupling, under two readings of the
  artefact rejection (about 20 minutes, most of it streaming the LFP and filtering every channel).''','''- `reproduce_daume_2024_lfp.ipynb`: LFP phase-amplitude coupling, under two readings of the
  artefact rejection, and single-trial PAC against category neuron firing (about 24 minutes in the
  first run and 42 minutes in the revision's run, most of it filtering every channel and
  computing the surrogates; the run time depends on the machine).
- `reproduce_daume_2024_lfp_controls.ipynb`: the controls of Extended Data Fig. 3 on the
  hippocampal channels (power, bycycle waveform asymmetry, phase-phase coupling, preferred phase,
  PAC peak frequency; about 21 minutes).''')
open(p,'w').write(s)
p='entries/000673-daume-2024/entry.yaml'; s=open(p).read()
s=s.replace('''phase-amplitude coupling and its load effect, and the selection and firing of PAC neurons. The
  spike-field coherence, noise correlation and decoding analyses were not run.''','''phase-amplitude coupling, its load effect and its controls, single-trial PAC against reaction time
  and category neuron firing, and the selection and firing of PAC neurons. The spike-field
  coherence, noise correlation and decoding analyses were not run.''')
s=s.replace("runtime_minutes: 24","runtime_minutes: 42").replace("runtime_minutes: 14","runtime_minutes: 21").replace("runtime_minutes: 8\n","runtime_minutes: 10\n")
open(p,'w').write(s)
EOF
cat entries/000673-daume-2024/entry.yaml | head -30
```

```
schema_version: 1
name: 000673-daume-2024
type: reproduction
title: Phase-amplitude coupling and working memory in human hippocampus (Daume et al. 2024)
description: Tests the findings of Daume et al. (2024) on dandiset 000673, which holds 44 sessions of
  a Sternberg working memory task in 36 epilepsy patients, with 1,454 single neurons and 1,922
  microwire LFP channels from the hippocampus, amygdala, pre-SMA, dACC and vmPFC. It tests the cohort,
  behaviour, category neurons and their maintenance activity, and the LFP theta-gamma
  phase-amplitude coupling, its load effect and its controls, single-trial PAC against reaction time
  and category neuron firing, and the selection and firing of PAC neurons. The spike-field
  coherence, noise correlation and decoding analyses were not run.
license: Apache-2.0
notebooks:
- path: reproduce_daume_2024.ipynb
  title: Behaviour and single neurons (Daume et al. 2024, dandiset 000673)
  runtime_minutes: 4
- path: reproduce_daume_2024_lfp.ipynb
  title: LFP phase-amplitude coupling (Daume et al. 2024, dandiset 000673)
  runtime_minutes: 42
- path: reproduce_daume_2024_lfp_controls.ipynb
[... 10 more lines not kept]
```

**Agent**

Now the attempt record: outcome changes, notes, and the round-1 `verifications` block.

**Agent calls Bash**

```bash
cat > $TMPDIR/rec.py <<'PYEOF'
import re
p = 'attempts/000673-daume-2024-01.yaml'
s = open(p).read()
def rep(old, new):
    global s
    assert s.count(old) == 1, (s.count(old), old[:80])
    s = s.replace(old, new)

def block(claim):
    i = s.index(f"- claim: {claim}\n")
    j = s.find("\n- claim: ", i + 5)
    k = s.find("\nfindings:", i)
    end = min(x for x in [j, k] if x != -1)
    return i, end + 1

def set_block(claim, text):
    global s
    i, e = block(claim)
    s = s[:i] + text.rstrip("\n") + "\n" + s[e:]

ART = ("On the one channel whose rejected trials the paper's code ships (artif_trials.mat with "
       "NWB_samplePAC_SU.m, sub-26 session 1, LFP channel 33), the paper removes 17 trials; reading (a) "
       "removes 4, all among them, and reading (b) removes 9, 5 of which the paper kept.")

set_block("fig2a-theta-gamma-pac", f"""- claim: fig2a-theta-gamma-pac
  outcome: reproduced
  notebook: reproduce_daume_2024_lfp.ipynb
  output: claim:fig2a-theta-gamma-pac
  notes: Under artefact reading (a), the mean z-scored MI over 1,922 channels (paper 1,917) is
    largest (2.16) at phase 4 Hz and amplitude 80 Hz; at phase 4 Hz the amplitude profile has local
    maxima at 50 Hz (within 30-55) and 80 Hz (within 70-140), and at 6 Hz at 40 and 80 Hz. Under
    reading (b), computed for phase centres 2 to 8 Hz, the mean over 1,918 channels is largest (1.73)
    at 4 Hz and 80 Hz, with local maxima at 45 and 80 Hz. Both readings meet the criterion. Per area
    the maximum is at phase 4 Hz in the hippocampus (75 Hz) and amygdala (50 Hz under a, 45 Hz under
    b) and at 2 Hz in the frontal areas.
  deviations:
  - The visual inspection of the artefact rejection cannot be repeated (O1); both automated readings
    were run. Under reading (b) the notebook computes phase centres 2 to 8 Hz only, the ones its
    other claims use.
  - Filters follow pop_eegfiltnew's default design (windowed sinc, Hamming) and firfilt's edge
    padding, reimplemented in Python (sbcat.py); the 200 surrogates draw a random permutation of the
    trials, as cfc_tort_comodulogram.m does.""")

rep("""    vmPFC, pre-SMA and dACC out of tolerance; the proportions again exceed the null.
  deviations:
  - Artefact rejection without the visual inspection (O1), under two readings of the span it is
    computed on.""", """    vmPFC, pre-SMA and dACC out of tolerance; the proportions again exceed the null.
  deviations:
  - Artefact rejection without the visual inspection (O1), under two readings of the span it is
    computed on. The counts are judged under reading (a), adopted for the claims where the readings
    disagree. """ + ART)

rep("""    17 or 12 significant channels where the paper has 5, and load 1 is higher in only 3 of the 17.""",
"""    17 or 12 significant channels where the paper has 5, and load 1 is higher in only 3 of the 17.
    The 17 channels come from six patients; four of sub-4 (session 37) have z values of 19 to 25 in
    load 3 against 3.5 to 6.8 in load 1, and seven of sub-11 (session 3) are also higher in load 3.
    The effect does not rest on a few outliers alone - Wilcoxon p = 0.0011, and without the three
    channels of largest load 3 excess p = 0.0045 (reading a; under b, p = 0.059).""")

rep("""    reading (b), on whole trials, removes 36.2 +/- 22.8 (25.9%), more than the paper's total.
- claim: edf2c""", f"""    reading (b), on whole trials, removes 36.2 +/- 22.8 (25.9%), more than the paper's total.
    {ART}
- claim: edf2c""")

rep("""  - Assumed artefact reading (a), as for edf2b-hippocampus-load-patients; the readings give
    different outcomes.""", f"""  - Assumed artefact reading (a), as for edf2b-hippocampus-load-patients; the readings give
    different outcomes. {ART}""")

rep("""    Correct, clean trials of 144 hippocampal channels (16,103 trials) under (a).""",
"""    Correct, clean trials of 144 hippocampal channels (16,103 trials) under (a). Variants under
    reading (a) - with RTs below 10 s the hippocampal term is negative and not significant (O5 a, p =
    0.16; O5 b, p = 0.094); with log10 RT it is negative under O5 (b) (t = -2.72, p = 0.0066) and not
    under O5 (a) (p = 0.13). The claim's test is on RT itself (Table S2 gives the estimate in ms), so
    the variants do not change the outcome.""")

set_block("edf3-hippocampus-pac-controls", """- claim: edf3-hippocampus-pac-controls
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_daume_2024_lfp_controls.ipynb
  output: claim:edf3-hippocampus-pac-controls
  notes: Under artefact reading (a), over 144 PAC channels, two load tests give p < 0.05 -
    high-gamma power is higher in load 3 (Hilbert t = 2.09, p = 0.035; Welch t = 2.69, p = 0.006)
    and the gamma peak frequency is higher in load 3 (93.0 against 86.8 Hz, t = 3.04, p = 0.003;
    as the coordinate of the single largest bin, p = 0.34). Theta power (p = 0.23, 0.16), rise-decay
    and peak-trough symmetry (all cycles p = 0.34 and 0.50; burst cycles, present in both loads in
    only 8 channels, p = 0.17 and 0.79), phase-phase locking (1 to 21, p = 0.90; each centre pair, p
    = 0.82), the theta peak frequency (p = 0.49; largest bin p = 0.080) and the preferred phase
    t-test (p = 0.71) do not differ. The V test of the phase differences against 0 gives p < 0.0001
    (mean resultant length 0.94, circular mean -1.6 degrees), which shows differences concentrated
    at 0; the criterion's rule would count it as a test with p < 0.05, which is asked of a reader
    (questions/000673.yaml). No asymmetry differs from 0.5 (p >= 0.072). With two load tests
    significant the criterion gives not reproduced. Under artefact reading (b) (125 channels) no
    load test gives p < 0.05 (high-gamma power p = 0.13 and 0.058, gamma peak frequency p = 0.17).
  deviations:
  - Assumed artefact reading (a), as for edf2b-hippocampus-load-patients; the readings give
    different outcomes.
  - Theta waveform asymmetry from bycycle 1.2 with f_range 3-7 Hz and its default settings on each
    trial's -0.5 to 3 s epoch, cycles with their peak in 0 to 2.5 s, averaged per load over the
    trials of the PAC analysis (Methods, PAC - "We averaged estimates for peak-to-trough as well as
    rise-to-decay asymmetries across cycles during the maintenance period from the same trials used
    for our PAC analysis within each load"). Its burst detection fails under pandas 3 and is
    replaced by the same default thresholds applied to a writable copy. Whether only burst cycles
    count is not stated; both are shown. With the default thresholds 99.9% of trial windows have no
    burst cycle.
  - PAC peak frequency (Extended Data Fig. 3h legend - "recomputed PAC using a finer resolution for
    phase frequencies (i.e., a step size of 0.5 instead of 2 Hz) and determined the frequency bin
    for which PAC was maximal for the theta and the gamma band separately") from raw MI per load,
    phase centres 3 to 7 Hz in 0.5 Hz steps and amplitude centres 70 to 140 Hz; read as the maximum
    of the mean over the other axis, with the coordinates of the largest bin as a variant. Raw MI
    is used as no surrogates are described for this panel.
  - Phase-phase coupling under both readings of the criterion; for the second, n is the ratio of
    each amplitude centre to the phase centre, rounded to an integer.""")

set_block("edf3e-nesting", None if False else s[block("edf3e-nesting")[0]:block("edf3e-nesting")[1]].replace(
"""    (p = 0.77).
  deviations:""", """    (p = 0.77). The count depends on the alignment and not on the window - with local maxima counted
    within 35 to 85 ms the peak alignment gives 104 to 114 nested channels (30 within 25 ms), and
    the amplitude alignment 4 to 15 for every window.
  deviations:"""))

set_block("fig3h-pac-category-firing", """- claim: fig3h-pac-category-firing
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_daume_2024_lfp.ipynb
  output: claim:fig3h-pac-category-firing
  notes: Under artefact reading (a), 166 hippocampal pairs of a category neuron and a significant PAC
    channel of its bundle (52 neurons, 15 patients; paper 151) and 450 amygdala pairs (paper 423).
    The hippocampal spike count term is not positive with p < 0.05 under any reading - all correct
    trials, O5 (a) estimate 1.6e-6, p = 0.15, O5 (b) -3.8e-4, p = 0.77; preferred trials, O5 (a)
    -3.1e-6, p = 0.15, O5 (b) -0.0045, t = -2.44, p = 0.015, negative where the paper's is positive
    (0.002, t = 2.40, p = 0.017). The amygdala term has p >= 0.21 under every reading, as in the
    paper. Under artefact reading (b) (145 and 410 pairs) the hippocampal term is positive with p =
    0.090 and 0.65 or negative (p = 0.70; preferred O5 b, p = 0.024). The SC x load interaction is
    significant in the hippocampus under every reading (p <= 0.002). The readings agree that the
    claimed positive relation is absent, so the outcome is not reproduced.
  deviations:
  - Pairs as in the criterion; the claim's depends_on (fig3f-gamma-sfc-preferred) names the SFC
    pairs, which are the same category neuron and PAC channel pairs, so the claim was run without
    the SFC. Bundles are the electrodes of a session with the same location and coordinates.
  - Mixed model fitted with statsmodels MixedLM (REML), random intercepts for patient and for pair
    within patient, in place of fitglme. Artefact reading (a) assumed, as for
    edf2b-hippocampus-load-patients; reading (b) gives the same outcome.""")

SFC = ("Timed on sub-26 session 1 while preparing (not run in a notebook) - the 40 wavelets take 0.27 s "
       "per channel, and for one neuron-channel pair, condition and load 500 spike subsamples take 0.016 s "
       "and 500 jittered surrogates with one subsample each 0.29 s, or about 8 s if each surrogate is "
       "averaged over 500 subsamples as the observed value is. With about 1,000 MTL pairs, two "
       "conditions, two loads and two readings of O8, the second form is about 18 CPU hours (over 4 "
       "hours on the 4 cores of the runner), beyond the 30-minute notebook limit; the first form (about "
       "45 CPU minutes) would fit, but its cluster tests and ANOVAs were not written in this run for lack "
       "of time.")
rep("""- claim: fig3f-gamma-sfc-preferred
  outcome: blocked
  blocked_by: too_large
  notes: Spike-field coherence (40 Morlet wavelets, 500 spike subsamples and 500 jittered surrogates
    per neuron-channel pair and condition, cluster tests with 10,000 permutations) was not started
    for lack of time in this run; no subset was timed. The data it needs (spikes, LFP, bundles
    inferred from location and coordinates) are in the dataset.""", f"""- claim: fig3f-gamma-sfc-preferred
  outcome: blocked
  blocked_by: too_large
  notes: Spike-field coherence (40 Morlet wavelets, 500 spike subsamples and 500 jittered surrogates
    per neuron-channel pair and condition, cluster tests with 10,000 permutations) was not run. {SFC}
    The data it needs (spikes, LFP, bundles inferred from location and coordinates) are in the
    dataset.""")

rep("""  notes: Panels f and g need spike-field coherence (40 wavelets, 500 spike subsamples and 500
    jittered surrogates per neuron-channel pair and load), which this run did not start for lack of
    time; no subset was timed. Panel h was run - with at least one incorrect trial, pre-SMA (204
    neurons in Hz, 201 in % of baseline; paper 201) correct 2.91 against incorrect 3.07 Hz, p =
    0.039, and in % of baseline p = 0.54; dACC (183 and 180; paper 180) p = 0.83 and 0.71; vmPFC
    (202 and 201; paper 201) p = 0.60 and 0.97. So panel h shows one difference in Hz in the pre-SMA
    and none in % of baseline.""", """  notes: Panels f and g need spike-field coherence, which was not run (timing under
    fig3f-gamma-sfc-preferred). Panel h was run - with at least one incorrect trial, pre-SMA (204
    neurons in Hz, 201 in % of baseline; paper 201) correct 2.91 against incorrect 3.07 Hz, p =
    0.039, and in % of baseline p = 0.54; dACC (183 and 180; paper 180) p = 0.83 and 0.71; vmPFC
    (202 and 201; paper 201) p = 0.60 and 0.97. In % of baseline, the reading adopted for the
    firing rate tests (fig3c-category-load), panel h holds and its n equal the paper's in all three
    areas; in Hz the pre-SMA differs with one incorrect trial and not with two or three (p = 0.089,
    0.11).""")

rep("""    no excess. With a post hoc threshold of two-sided p < 0.05 the counts are 87, 174, 41, 18 and 14.""",
"""    no excess. With a post hoc threshold of two-sided p < 0.05 the counts are 87, 174, 41, 18 and 14.
    The pre-SMA sits at the boundary - 18 is one above the 99th percentile and p = 0.010 equals the
    threshold - so with 500 shuffles neither form of the rule separates it clearly from chance.""")

rep("""    both readings, so the claim holds in part. In 24 of 34 patients the preferred rate is higher.""",
"""    both readings, so the claim holds in part. In 24 of 34 patients the preferred rate is higher.
    Under reading (b) alone, adopted for fig3c and fig3d, all three tests hold.""")

rep("""    with those panels (Fig. 4f gives "correct, P = 0.0001;
    incorrect, P = 0.0001" against baseline for the plotted values), so the tests are taken to be on
    the plotted values.""", """    with those panels (Fig. 4f gives "correct, P = 0.0001;
    incorrect, P = 0.0001" against baseline for the plotted values), so the tests are taken to be on
    the plotted values. The data support this - with at least one incorrect trial, the % of baseline
    reading gives exactly the paper's n for the frontal areas in Extended Data Fig. 8h (201, 180 and
    201; neurons with no baseline spike drop out), and the Hz reading does not (204, 183, 202).""")

rep("""    269 and 422 MTL neurons have LFP in their bundle, against the paper's 212 and 358.""",
"""    269 and 422 MTL neurons have LFP in their bundle, against the paper's 212 and 358. Without any
    correction, 41 hippocampal and 66 amygdala neurons have a combination passing both tests at p <
    0.01 (shuffles at most 13 and 14), still fewer than the paper's counts after FDR. The paper's
    plot_PAC_neuron.m fits the three GLMs to the 20 aggregated bin counts of one neuron-channel pair
    with fixed effects only, as sbcat.py does, so neither a per-trial layout nor a random effect
    explains the difference.""")

rep("""    blocked. The mean waveforms needed for the trough-to-peak time are in the files.""",
"""    blocked. The mean waveforms needed for the trough-to-peak time are in the files (waveform_mean,
    256 samples, in 43 of the 44 files; waveforms in all 44).""")

rep("""    paper analysed 212 and 358 ("pre-processing steps removed broadband LFPs for some of the
    neurons").""", """    paper analysed 212 and 358 ("pre-processing steps removed broadband LFPs for some of the
    neurons"). The paper's code ships the rejected trials of one example channel (artif_trials.mat,
    sub-26 session 1, channel 33, 17 trials), which shows the information exists for the paper's
    own analysis.""")

rep("""    The two give different outcomes for Extended Data Fig. 2b and 3f; this attempt assumed the
    epochs.""", """    The two give different outcomes for Extended Data Fig. 2b and 3f; this attempt assumed the
    epochs, which agree with the paper's rejected trials on the one channel its code ships.""")
open(p, 'w').write(s)
print("ok")
PYEOF
python3 $TMPDIR/rec.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/rec.py", line 190, in <module>
    rep("""    with those panels (Fig. 4f gives "correct, P = 0.0001;
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        incorrect, P = 0.0001" against baseline for the plotted values), so the tests are taken to be on
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<3 lines>...
        reading gives exactly the paper's n for the frontal areas in Extended Data Fig. 8h (201, 180 and
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        201; neurons with no baseline spike drop out), and the Hz reading does not (204, 183, 202).""")
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/rec.py", line 6, in rep
    assert s.count(old) == 1, (s.count(old), old[:80])
           ^^^^^^^^^^^^^^^^^
AssertionError: (0, '    with those panels (Fig. 4f gives "correct, P = 0.0001;\n    incorrect, P = 0.')
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import os
p=os.environ['TMPDIR']+'/rec.py'; s=open(p).read()
a=s.index('rep("""    with those panels (Fig. 4f gives'); b=s.index('rep("""    269 and 422 MTL')
new='''rep("""    the plotted values.
- claim: fig3d""", """    the plotted values. The data support this - with at least one incorrect trial, the % of baseline
    reading gives exactly the paper's n for the frontal areas in Extended Data Fig. 8h (201, 180 and
    201; neurons with no baseline spike drop out), and the Hz reading does not (204, 183, 202).
- claim: fig3d""")

'''
s=s[:a]+new+s[b:]
open(p,'w').write(s)
EOF
grep -n "the plotted values" attempts/000673-daume-2024-01.yaml; python3 $TMPDIR/rec.py && python -c "import yaml;yaml.safe_load(open('attempts/000673-daume-2024-01.yaml'))" && git diff --stat
```

```
131:    incorrect, P = 0.0001" against baseline for the plotted values), so the tests are taken to be on
132:    the plotted values.
ok
 attempts/000673-daume-2024-01.yaml                 | 149 ++++++++---
 entries/000673-daume-2024/README.md                |  13 +-
 entries/000673-daume-2024/entry.yaml               |  12 +-
 .../000673-daume-2024/reproduce_daume_2024.ipynb   |  32 ++-
 .../reproduce_daume_2024_lfp.ipynb                 | 281 +++++++++++++++------
 .../reproduce_daume_2024_pac_neurons.ipynb         |  17 +-
 entries/000673-daume-2024/requirements.in          |   1 +
 entries/000673-daume-2024/requirements.lock.txt    |  14 +-
 entries/000673-daume-2024/sbcat.py                 | 134 +++++++++-
 9 files changed, 501 insertions(+), 152 deletions(-)
```

**Agent calls Bash**

```bash
sed -n 330,420p schemas/attempt.schema.json
```

```
}
        ]
      }
    },
    "verifications": {
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
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "agree" tools/entry.py | head -20
```

```
278:        agreed = {}
281:                agreed[r["claim"]] = r.get("outcome") if r.get("agrees") else None
295:            verified = agreed.get(outcome.get("claim"))
298:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
```

**Agent calls Bash**

```bash
sed -n 270,300p tools/entry.py
```

```
continue
        recorded = [o.get("claim") for o in attempt.get("outcomes", [])]
        for claim in sorted(known - set(recorded)):
            report.error(where, f"claim {claim!r} has no outcome; give every claim one, blocked included")
        for claim in sorted({c for c in recorded if recorded.count(c) > 1}):
            report.error(where, f"claim {claim!r} has more than one outcome")
        # The latest round that reviewed a claim decides it; a third round may review only some. Round 1
        # does not bind: the revision after it may change outcomes, and round 2 reviews them.
        agreed = {}
        for rnd in (attempt.get("verifications") or [])[1:]:
            for r in rnd["results"]:
                agreed[r["claim"]] = r.get("outcome") if r.get("agrees") else None
        kinds = kinds_by_target.get((dataset_id(attempt), attempt.get("paper")), {})
        for outcome in attempt.get("outcomes", []):
            # A claim on data in another archive names where they are, so it is never blocked for missing data,
            # and when it is tested the archive is an input. Only the latest attempt is held to this: the
            # claims file is shared, and an earlier attempt may predate the claim's `elsewhere`.
            if kinds.get(outcome.get("claim")) == "elsewhere" and path == mine[-1]:
                if outcome.get("blocked_by") == "data_missing":
                    report.error(where, f"claim {outcome.get('claim')!r} has its data in another archive "
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/ver.py <<'PYEOF'
import yaml
R = []
def r(claim, agrees, outcome, reason, response):
    R.append({"claim": claim, "agrees": agrees, "outcome": outcome, "reason": reason, "response": response})
NOCH = "No change to the outcome."
r("cohort-counts", True, "reproduced", "All counts match exactly - 44 sessions, 36 patients, 1,454 units, 1,922 LFP channels, and every per-area count.", NOCH)
r("fig1d-rt-load", True, "reproduced", "Median RT is 1.233 s (load 1) and 1.360 s (load 3), both within tolerance; t43 = 5.33, p = 0.0001. The mean-RT variant gives no effect (t = -0.48), because RTs up to 74 s pull the means.", NOCH)
r("fig1d-accuracy-load", True, "reproduced", "95.10% against 91.02%; t43 = -5.24, p = 0.0001.", NOCH)
r("behaviour-overall-accuracy", True, "reproduced", "93.05 +/- 7.22%; false negatives 76.08 +/- 20.11% of errors; both within tolerance.", NOCH)
r("fig2a-theta-gamma-pac", True, "reproduced", "The largest mean z is at 4 Hz phase, 80 Hz amplitude; at 4 and 6 Hz there are local maxima at 50/40 Hz and 80 Hz. Only artefact reading (a) is shown (problem 8 - the claims file asks for both).",
  "Added the reading (b) comodulogram (phase centres 2 to 8 Hz, the ones computed under b) - largest mean z at 4 Hz and 80 Hz, local maxima at 45 and 80 Hz, so both readings meet the criterion. The outcome no longer rests on an assumption (assumed removed).")
r("fig2b-pac-channel-proportions", True, "partially_reproduced", "Reading (a) - hippocampus 144, amygdala 130, vmPFC 41 and dACC 14 are within tolerance and all far above the null (p = 0.005). pre-SMA is 17 against 5, out of tolerance. Reading (b) puts four counts out of tolerance.",
  "No change to the outcome. The counts are judged under reading (a), now supported by the paper's own rejected trials on one channel (problem 6).")
r("fig2c-hippocampus-load", True, "reproduced", "Load 1 is higher under both readings - n = 144, t = -4.16, FDR p = 0.001; reading (b) FDR p = 0.014.", NOCH)
r("fig2c-no-load-effect-other-areas", True, "not_reproduced", "Reading (a) - amygdala FDR p = 0.0475 and pre-SMA 0.0017, both with load 3 higher. Reading (b) - pre-SMA and dACC FDR p = 0.014. In pre-SMA only 3 of 17 channels have load 1 higher, yet the load 3 mean is 6.9 against 1.8; a few outlier channels probably drive the effect; this was not inspected (problem 9).",
  "Added the per-channel pre-SMA z values by load under both readings, a Wilcoxon test and the test without the three channels of largest load 3 excess. The channels come from six patients; four of sub-4 have z of 19 to 25 in load 3, but load 3 is higher in 14 of 17 channels (Wilcoxon p = 0.0011) and the test holds without the three largest (p = 0.0045; under b, p = 0.059). Outcome kept.")
r("edf2b-hippocampus-load-patients", True, "reproduced", "Reading (a) - hippocampus, 23 patients, p = 0.0095, load 1 higher; no other area p < 0.05. This depends on O1; under (b) the hippocampus gives p = 0.11. O1 has no tie-break; reading (a) removes 11.4% of trials and (b) 25.9%, against the paper's 14.6% with visual inspection, which favours (a) (problem 6).",
  "Found a tie-break in the paper's code - artif_trials.mat, shipped with NWB_samplePAC_SU.m, lists the 17 trials the paper rejected on its example channel (sub-26 session 1, channel 33). Reading (a) removes 4 trials there, all among the 17; reading (b) removes 9, 5 of which the paper kept. Added this comparison and the distribution of removed trials per channel to the data check, and the reason to the deviation. Outcome kept, still marked as resting on reading (a).")
r("edf2c-low-gamma-no-load-effect", True, "not_reproduced", "pre-SMA p = 0.003 uncorrected and 0.015 FDR, under both readings.", NOCH)
r("tables1-slow-fast-theta", True, "not_reproduced", "Under every reading, pre-SMA tests (and under one reading hippocampal slow theta-low gamma) also give p < 0.05, not just the two hippocampal high-gamma tests. The notebook counts 20 tests against the claims file's 19, because pre-SMA has fast-theta channels here (problem 11).",
  "No change to the outcome. The 20th test is the pre-SMA fast theta to high gamma test, which the paper's table leaves out because its pre-SMA had too few channels; the notes already say so.")
r("fig2f-rt-single-trial-pac", True, "not_reproduced", "The hippocampal PAC term is not significant under any reading (p 0.19-0.64; the estimate is positive under artefact (a)). The amygdala gives p = 0.046 under O5(b). The RTs used are untrimmed (up to 16.8 s); outliers can reverse a mean-based effect, and this was not tested (problem 7).",
  "Added variants under reading (a) - RTs below 10 s (hippocampal term negative, p = 0.16 and 0.094) and log10 RT (negative, p = 0.0066 under O5 b, 0.13 under O5 a). The claim's test is on RT itself (Table S2 in ms), so the outcome is kept; the variants are in the notes.")
r("edf3-hippocampus-pac-controls", False, "partially_reproduced", "Under artefact (a), gamma power is higher in load 3 by both estimates (p = 0.035 and 0.006); theta power, phase-phase coupling and the preferred-phase t-test show no difference. Waveform asymmetry, peak frequency and the second phase-phase-coupling ratio were not run. A V test of the load differences against 0 tests concentration around 0, so a significant V test supports no phase shift; the claims file's reading (a), with its rule that no test gives p < 0.05, misreads the test (problem 5).",
  "Ran the missing parts in a new notebook, reproduce_daume_2024_lfp_controls.ipynb - bycycle rise-decay and peak-trough symmetry (no load difference), phase-phase locking for each centre pair (p = 0.82), and the PAC peak frequency on a 0.5 Hz phase grid (theta peak p = 0.49; gamma peak higher in load 3, p = 0.003, with the largest-bin variant p = 0.34). With high-gamma power and gamma peak frequency both differing under the adopted reading (a), the criterion gives not reproduced; the outcome changes from blocked to not_reproduced, resting on reading (a) (under b no load test gives p < 0.05). The V test misreading is added to questions/000673.yaml; the claim is tested as written.")
r("edf3a-kappa-load", True, "reproduced", "t = -4.54, p = 0.0001 (a); p = 0.0024 (b).", NOCH)
r("edf3e-nesting", True, "reproduced", "Holds only under the notebook's own 'peak' alignment - 105 of 144 nested (in tolerance), load test p = 0.0002. Under the Methods' literal 'amplitude maximum' alignment only 9 of 144 are nested. The assumption is stated and plausible (aligning on the envelope maximum averages out gamma cycles), but edf3e rests entirely on it (problem 4).",
  "Added the nesting count under windows of 25 to 85 ms for both alignments - 104 to 114 under the peak alignment for 35 to 85 ms, 4 to 15 under the amplitude alignment for every window. The outcome rests on the alignment, not the window; assumption and question for the authors kept.")
r("edf3f-raw-mi-load", True, "reproduced", "Reading (a) - t = -4.03, p = 0.0002. Reading (b) - p = 0.066.", "No change to the outcome; the deviation now cites the paper's own rejected trials as the support for reading (a).")
r("methods-spectral-slope", True, "not_reproduced", "Over 2-150 Hz the slope differs between loads (p = 0.007 and 0.002). Over 30-150 Hz it does not (p = 0.12 and 0.28). The 2-150 Hz values match the paper's -1.753 +/- 0.39 far better than 30-150 Hz, so that range is the likelier reading. The difference itself is tiny (0.004).", NOCH)
r("category-cell-counts", True, "partially_reproduced", "All counts are within tolerance (94, 181, 40, 18, 13). pre-SMA sits at the threshold - 18 exceeds the 99th percentile of 17, but p = 0.010; above the 99th percentile and p < 0.01 disagree at the boundary (problem 10).",
  "No change to the outcome; the conclusion and notes now say the pre-SMA is at the boundary of both forms of the rule.")
r("fig3b-persistent-activity", True, "partially_reproduced", "Both baseline tests give p = 0.0001 under both readings. Preferred against non-preferred gives p = 0.072 in Hz (a) and p = 0.0013 in % change (b); the criterion needs both readings. Under O6 (b), which the frontal n support (problem 3), fig3b reproduces in full.",
  "Outcome kept, as the criterion asks for both readings; the notes say that under reading (b) alone all three tests hold.")
r("edf4b-persistent-activity-by-area", True, "partially_reproduced", "The vmPFC part holds (all p >= 0.06). The hippocampal and amygdala preference tests fail in Hz (p = 0.24, 0.18) and hold in % (p = 0.019, 0.039). Under O6 (b) edf4b reproduces in full (problem 3).",
  "Outcome kept, as the criterion (through fig3b) asks for both readings.")
r("fig3c-category-load", False, "partially_reproduced", "In Hz - preferred trials p = 0.022 (load 1 higher), non-preferred p = 0.20. In % - preferred p = 0.77. Under O6 (b), which % change with at least 1 incorrect trial supports by reproducing the paper's frontal n exactly (201, 180, 201), fig3c fails (problem 3).",
  "Outcome kept as not_reproduced, resting on reading (b) of O6, the reading the verifier's problem 3 supports; the deviation now gives that evidence. Under (a) the claim would be reproduced, which the notes show.")
r("fig3d-category-correct-incorrect", True, "reproduced", "All trials, % change, at least 1 or 2 incorrect trials - p = 0.0035 and 0.010, n = 251 and 229 (paper 246). This is fragile - in Hz p = 0.12-0.40, and every preferred-trial reading fails.", NOCH)
r("category-no-rt-effect", True, "reproduced", "All p >= 0.05 (lowest 0.098).", NOCH)
r("pac-neuron-counts", True, "partially_reproduced", "The shuffle test holds (p = 0.005), but only 8 of 269 hippocampal and 5 of 422 amygdala neurons qualify (12 and 24 under FDR reading b), against 79 and 163. No code bug found; the gap lies in a method detail never probed - per-trial observations or random effects in fitglme, or which FDR family. Uncorrected, 1.8% of combinations pass against 0.1% in shuffles (problem 1).",
  "Read plot_PAC_neuron.m at the pinned commit - it fits the three fitglme models to the 20 aggregated bin counts with fixed effects only, as sbcat.py does, so neither a per-trial layout nor a random effect is the difference. Added the uncorrected counts per area (41 of 269 and 66 of 422, shuffles at most 13 and 14), still below the paper's counts after FDR. Outcome kept; the question for the authors stays.")
for c, out, rs in [("pac-category-overlap", "partially_reproduced", "The overlap does not exceed chance (p = 0.13 and 0.57), but the counts (4 and 2) are far out of tolerance and rest on n = 8 and 5."),
                   ("fig4c-pac-neuron-firing-single-trial-pac", "not_reproduced", "Hippocampal SC term p = 0.85 and 0.18; amygdala p = 0.050 and 0.041. Only 8 and 5 pairs, so this is not an informative test."),
                   ("fig4e-hippocampus-pac-neurons-accuracy", "partially_reproduced", "Correct > incorrect holds (p = 0.02-0.03); maintenance against baseline fails (p = 0.51); n = 8 against 63."),
                   ("fig4g-hippocampus-pac-neurons-load", "not_reproduced", "Both baseline tests fail, and load 3 < load 1 is significant (p = 0.009); n = 8."),
                   ("fig4-amygdala-pac-neurons", "partially_reproduced", "Baseline test p = 0.12 fails; the other three tests are null as claimed; n = 5.")]:
    r(c, False, out, rs + " Every claim built on PAC neurons is run at n = 8 and 5 and cannot test the paper (problem 1).",
      "Kept blocked (other) and recorded the disagreement - the verifier's own problem 1 says these tests, on 8 and 5 neurons against 79 and 163, cannot test the paper's populations; the results are kept in the notes for the record.")
r("edf8fgh-frontal-controls", True, "blocked", "Panels f and g (SFC) were not run, though the data are present. Panel h - pre-SMA p = 0.039 in Hz with at least 1 incorrect trial. In % with at least 1 incorrect trial, the n are exactly the paper's 201/180/201 and all p > 0.5.",
  "Kept blocked (too_large) for panels f and g, with the timing of the SFC now given (see fig3f-gamma-sfc-preferred). The notes now say panel h holds in % of baseline, the adopted reading, with the paper's n exactly.")
r("fig3h-pac-category-firing", False, "blocked", "fig3h appears nowhere - it is not in any notebook's table and not covered by the blocked line, yet every input it needs (category neurons x PAC channels) is already computed (problem 2).",
  "Tested in reproduce_daume_2024_lfp.ipynb - 166 hippocampal and 450 amygdala pairs (paper 151 and 423); no reading gives a positive hippocampal spike count term with p < 0.05 (on preferred trials under O5 b it is negative, p = 0.015), and the amygdala term is null. Outcome changed from blocked to not_reproduced.")
SFC_T = "Nothing in the archive blocks these; the archive lists all 44 files, with LFP in 43 sessions and units in all, and the notebooks load spikes, trials and LFP for every area. Testable now with no PAC-neuron selection."
SFC_R = "Kept blocked (too_large). The SFC core was timed on one session while preparing - with each of the 500 surrogates averaged over 500 spike subsamples as the observed value is, about 18 CPU hours for the MTL pairs, beyond the notebook limit; with one subsample per surrogate it would fit, but its cluster tests and ANOVAs were not written in this run for lack of time. The notes give the timing."
for c in ["fig3f-gamma-sfc-preferred", "fig3g-gamma-sfc-anova", "edf5d-sfc-high-gamma-power", "edf5c-theta-sfc-null", "edf5fg-gamma-sfc-all-channels-patients"]:
    r(c, False, "blocked", SFC_T, SFC_R)
r("edf7a-pac-neurons-no-category-decoding", False, "blocked", SFC_T + " (the category-neuron part, chance 20%)",
  "Kept blocked (other). The claim compares PAC neurons that are not category neurons with category neurons; with 4 and 3 such PAC neurons the comparison cannot be made, and the decoding of category neurons alone was not written in this run for lack of time.")
r("fig5cd-no-effect-category-amygdala", False, "blocked", SFC_T + " (the category-neuron part)",
  "Kept blocked (other). Its category-neuron part needs the cross-regional SFC, which was not run (timing under fig3f-gamma-sfc-preferred), and its comparison is with the PAC neurons of fig5b.")
r("fig6g-signal-noise-angle", False, "blocked", SFC_T,
  "Kept blocked (other). It compares the signal and noise axes of sessions with and without PAC neurons, from the decoding of fig6c, so it rests on the PAC neuron selection (8 and 5 neurons); not run.")
PACB = "Testable but on the failed selection - these could run only on the notebook's 8 and 5 PAC neurons."
for c in ["edf7bc-pac-neuron-local-sfc", "fig5b-hippocampus-vmpfc-theta-sfc-load", "fig5e-random-subsets", "fig5f-theta-sfc-rt", "edf8b-vmpfc-sfc-patients", "edf8c-pac-against-category",
          "fig6a-noise-correlations", "edf9ef-non-category-pac-pairs", "fig6c-adding-pac-neurons", "fig6d-removing-pac-neurons", "fig6e-decoding-difference", "edf9g-non-category-pac-decoding",
          "edf9jk-amygdala-decoding", "fig6h-projection-variance", "fig6i-noise-correlations-rt", "edf9hil-noise-correlations-rt-controls", "fig6j-specific-to-pac-pairs"]:
    r(c, True, "blocked", PACB, "Kept blocked (other), as the selection gives 8 and 5 PAC neurons against 79 and 163.")
r("edf8de-narrow-spiking", True, "blocked", PACB + " It also needs waveforms; the helper's docstring implies the files hold them, but this could not be confirmed from the API metadata.",
  "Kept blocked (other). Added a print of every file's units-table columns - waveform_mean (256 samples) is in 43 of the 44 files and waveforms in all 44.")
ver = [{"date": "2026-10-31", "kind": "agent",
        "by": "Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebooks)",
        "reviewed": ("Round 1. The executed notebooks of the author run with the conclusion cells and the summary "
                     "removed, the helper module and the claims file, with the paper. The verifier queried the archive "
                     "metadata and tested helper functions on synthetic inputs. Its report gave its own outcome for "
                     "each claim; it disagreed with 15 recorded outcomes, 6 of them on claims it found tested and 9 on "
                     "claims the record blocks."),
        "results": R}]
txt = yaml.safe_dump({"verifications": ver}, sort_keys=False, width=100, allow_unicode=True)
p = "attempts/000673-daume-2024-01.yaml"
s = open(p).read()
assert "verifications:" not in s
s = s.rstrip("\n") + "\n" + txt
open(p, "w").write(s)
import collections
print(len(R), collections.Counter(x["agrees"] for x in R))
PYEOF
python3 $TMPDIR/ver.py && python tools/entry.py check entries/000673-daume-2024 2>&1 | tail -5
```

```
57 Counter({True: 41, False: 16})
0 error(s)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/000673-daume-2024-01.yaml'; s=open(p).read()
import re
i=s.index('  reviewed: Round 1.'); j=s.index('  results:', i)
new='''  reviewed: Round 1. The executed notebooks of the author run with the conclusion cells and the summary
    removed, the helper module and the claims file, with the paper. The verifier queried the archive
    metadata and tested helper functions on synthetic inputs. Its report gave its own outcome for each
    claim; it disagreed with 16 recorded outcomes - fig3c-category-load, and 15 claims the record
    blocked, 6 of which it judged from results printed in the notebooks and 9 it found testable from
    the archive.
'''
s=s[:i]+new+s[j:]
open(p,'w').write(s)
import yaml; yaml.safe_load(open(p))
EOF
python tools/entry.py check entries/000673-daume-2024 2>&1 | tail -2; date -u
```

```
0 error(s)
Sat Oct 31 14:27:30 UTC 2026
```

**Agent**

Record written and the check passes. Starting the final `entry.py all` run (about 75 min).

**Agent calls Bash**

```bash
time python tools/entry.py all entries/000673-daume-2024 2>&1 | tail -12; date -u
```

```
Installed kernelspec registry-000673-daume-2024 in executed/000673-daume-2024/.venv/share/jupyter/kernels/registry-000673-daume-2024
took 42 minutes; the limit is 30
0 error(s)
pass  reproduce_daume_2024.ipynb  (191 s)
FAIL  reproduce_daume_2024_lfp.ipynb  (2531 s)
pass  reproduce_daume_2024_lfp_controls.ipynb  (1286 s)
pass  reproduce_daume_2024_pac_neurons.ipynb  (558 s)

real	76m13.928s
user	245m22.593s
sys	3m18.004s
Sat Oct 31 15:43:56 UTC 2026
```

**Agent**

Same result: three pass, and the LFP notebook runs 42 min against the 30-min limit. Spot-checking that the numbers in the conclusions match this run.

**Agent calls Bash**

```bash
cd executed/000673-daume-2024; python3 $TMPDIR/show.py reproduce_daume_2024_lfp_controls.ipynb claim:edf3-hippocampus-pac-controls | sed -n 3,20p; python3 $TMPDIR/show.py reproduce_daume_2024_lfp.ipynb claim:fig3h-pac-category-firing | tail -20; python3 $TMPDIR/show.py reproduce_daume_2024_lfp.ipynb 5 claim:edf3e-nesting | grep -A9 "window_ms\|reading a removes"; python3 $TMPDIR/show.py reproduce_daume_2024_lfp.ipynb claim:fig2f-rt-single-trial-pac | tail -14; python3 $TMPDIR/show.py reproduce_daume_2024_pac_neurons.ipynb claim:pac-neuron-counts | tail -4
```

```
test   n   load1   load3  t(3-1)      p
                                    theta power, Hilbert 144  2.6732  2.6815  1.2017 0.2294
                               high-gamma power, Hilbert 144  1.0749  1.0816  2.0863 0.0353
                                      theta power, Welch 144  1.8345  1.8456  1.4606 0.1553
                                 high-gamma power, Welch 144 -0.6816 -0.6726  2.6910 0.0060
                       rise-decay symmetry, burst cycles   8  0.4045  0.4566  1.6443 0.1736
                      peak-trough symmetry, burst cycles   8  0.4744  0.4656 -0.3031 0.7928
                         rise-decay symmetry, all cycles 144  0.4995  0.4987 -0.9558 0.3404
                        peak-trough symmetry, all cycles 144  0.4977  0.4973 -0.6712 0.4982
                                  phase locking 1:21 (a) 144  0.0075  0.0074 -0.1268 0.9014
                     phase locking, each centre pair (b) 144  0.0096  0.0096 -0.2272 0.8204
                               theta peak frequency (Hz) 144  3.5764  3.5139 -0.7399 0.4875
                               gamma peak frequency (Hz) 144 86.8056 92.9514  3.0360 0.0030
                  theta peak frequency, largest bin (Hz) 144  3.6840  3.5139 -1.7850 0.0795
                  gamma peak frequency, largest bin (Hz) 144 88.6111 90.7639  0.9705 0.3407
               preferred phase 3-1, V test against 0 (a) 144     NaN     NaN 15.8916 0.0000
preferred phase 3-1, wrapped, t-test against 0 (b) (deg) 144     NaN -0.7176 -0.3871 0.7090
mean resultant length of the preferred phase differences: 0.937; circular mean -1.6 deg; |difference| < 20 deg in 106 of 144 channels
paper: 151 hippocampal and 423 amygdala neuron-channel combinations
artefact        area    trials O5  pairs     n  SC estimate        t       p  SC x load p  converged
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "p <= 0.002)" attempts/000673-daume-2024-01.yaml entries/000673-daume-2024/*.ipynb | cut -c1-150; sed -i 's/significant in the hippocampus under every reading (p <= 0.002)/significant in the hippocampus under every reading (p <= 0.0025)/' attempts/000673-daume-2024-01.yaml entries/000673-daume-2024/reproduce_daume_2024_lfp.ipynb; grep -c "p <= 0.0025" attempts/000673-daume-2024-01.yaml entries/000673-daume-2024/reproduce_daume_2024_lfp.ipynb
```

```
attempts/000673-daume-2024-01.yaml:430:    significant in the hippocampus under every reading (p <= 0.002). The readings agree that the
entries/000673-daume-2024/reproduce_daume_2024_lfp.ipynb:995:    "The SC x load interaction is significant in the hippocampus under every reading (p <
attempts/000673-daume-2024-01.yaml:1
entries/000673-daume-2024/reproduce_daume_2024_lfp.ipynb:1
```

**Agent calls Bash**

```bash
sed -i 's/(about 24 minutes in the\n  first run/X/' entries/000673-daume-2024/README.md; python3 - <<'EOF'
p='entries/000673-daume-2024/README.md'; s=open(p).read()
old="artefact rejection, and single-trial PAC against category neuron firing (about 24 minutes in the\n  first run and 42 minutes in the revision's run, most of it filtering every channel and\n  computing the surrogates; the run time depends on the machine)."
assert old in s
s=s.replace(old,"artefact rejection, and single-trial PAC against category neuron firing (20 minutes in the\n  author run and 42 minutes in the revision's run, over the 30-minute limit, most of it filtering\n  every channel and computing the surrogates; the run time depends on the machine).")
open(p,'w').write(s)
EOF
python tools/entry.py check entries/000673-daume-2024 2>&1 | tail -1; grep -n " — \|rather" attempts/000673-daume-2024-01.yaml questions/000673.yaml entries/000673-daume-2024/README.md | head; git status --short; date -u
```

```
0 error(s)
 M attempts/000673-daume-2024-01.yaml
 M entries/000673-daume-2024/README.md
 M entries/000673-daume-2024/entry.yaml
 M entries/000673-daume-2024/reproduce_daume_2024.ipynb
 M entries/000673-daume-2024/reproduce_daume_2024_lfp.ipynb
 M entries/000673-daume-2024/reproduce_daume_2024_pac_neurons.ipynb
 M entries/000673-daume-2024/requirements.in
 M entries/000673-daume-2024/requirements.lock.txt
 M entries/000673-daume-2024/sbcat.py
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
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la scripts .idea .vscode 2>&1 | head; ls -la .bashrc .mcp.json
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 12:31 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 12:31 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 12:31 scripts
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 12:31 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 31 12:31 .mcp.json
```

**Agent**

I've worked through every point in the round-1 report and re-run the entry with `python tools/entry.py all`. The check passes with 0 errors. Three notebooks pass, but `reproduce_daume_2024_lfp.ipynb` fails the 30-minute limit: it took 42 minutes, both times I ran it. Its channel processing took 38 minutes here, against 18 minutes in the author run. The per-channel work is unchanged (about 3.5 s per channel), so this looks like a slower runner, but CI will mark it as failed on a runner like this one.

**Outcome changes**
- **`edf3-hippocampus-pac-controls`**: blocked → `not_reproduced`, resting on artefact reading (a). The missing parts now run in a new notebook, `reproduce_daume_2024_lfp_controls.ipynb`. Two load tests give p < 0.05:
  - high-gamma power (p = 0.035 and 0.006);
  - gamma peak frequency (p = 0.003; reading it as the single largest bin instead gives p = 0.34).
  Waveform asymmetry, phase-phase coupling (both ratios), theta peak frequency and the preferred-phase t-test show no difference. Under reading (b) no load test is significant.
- **`fig3h-pac-category-firing`**: blocked → `not_reproduced`. On 166 hippocampal and 450 amygdala pairs (paper 151 and 423), no reading gives a positive hippocampal spike-count term. One reading gives a negative one (p = 0.015), and the amygdala term is null.
- **`fig2a-theta-gamma-pac`**: still reproduced, no longer marked as resting on an assumption. Reading (b) now also meets the criterion (peak at 4 Hz and 80 Hz, local maxima at 45 and 80 Hz).

**Added or corrected**
- **Tie-break for the artefact rejection reading (problem 6).** The paper's code ships `artif_trials.mat`, the 17 trials the paper rejected on its example channel (sub-26 session 1, channel 33). Reading (a) removes 4 trials there, all among the paper's; reading (b) removes 9, five of which the paper kept. This comparison and the spread of removed trials per channel are in the data check, and the record cites it wherever reading (a) is assumed.
- **PAC neurons (problem 1).** The paper's `plot_PAC_neuron.m` fits fixed-effects GLMs to 20 pooled bin counts, as `sbcat.py` does. So a per-trial layout or a random effect is not the difference the verifier suspected. Even uncorrected, only 41 hippocampal and 66 amygdala neurons qualify, fewer than the paper's 79 and 163 after correction.
- **Firing rate units (problem 3).** The evidence that rates are compared as % of baseline (the paper's frontal n match exactly) is now in `fig3c`'s deviation and `edf8fgh`'s notes.
- **Other outputs the verifier asked for:**
  - the 17 pre-SMA channels one by one: six patients, and the effect survives dropping the three largest (p = 0.0045);
  - `fig2f` with RT below 10 s and with log RT. With log RT the hippocampal term turns negative and significant under one single-trial PAC reading (p = 0.0066), but the claim's test is on RT itself, so the outcome stands;
  - the nesting count under windows of 25 to 85 ms: it depends on the alignment, not the window;
  - the units-table columns: waveforms are in all 44 files.
- **Questions file.** I added `questions/000673.yaml` with the V-test misreading (problem 5). The claim is unchanged.
- **Record.** The round-1 `verifications` block covers all 57 claims: the verifier disagreed with 16.

**Disagreements kept**
- `fig3c-category-load` stays `not_reproduced`, assumed. The verifier would give partially reproduced, but its own problem 3 supports the % of baseline reading, under which the claim fails.
- The five PAC-neuron firing claims stay blocked (other). The verifier gave outcomes for them, but its own problem 1 says tests on 8 and 5 neurons cannot test the paper's populations.
- `fig3b` and `edf4b` stay partially reproduced, as their criterion requires both firing-rate readings. The notes say they hold in full under % of baseline alone.

**Not done**
- **Spike-field coherence** (`fig3f`, `fig3g`, `edf5c`, `edf5d`, `edf5fg`, panels f and g of `edf8fgh`): still blocked as `too_large`, now with a measured estimate. I timed it on one session while preparing, outside any notebook. With each surrogate averaged over 500 spike subsamples like the observed value, it needs about 18 CPU hours. With one subsample per surrogate it would fit, but there was no time to write it.
- **`edf7a`, `fig5cd` and `fig6g`** stay blocked: they need SFC, the decoding analysis, or the PAC-neuron selection, none of which was run.

**Time**
To keep the LFP notebook from growing further, the Extended Data Fig. 3 controls run in the new controls notebook (21 min). After the final run I corrected one number in markdown only (an interaction p bound, from 0.002 to 0.0025), which changes no outputs. I did not commit.

## End of run

95 turns, 188 minutes, result: success.
