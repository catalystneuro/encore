# peron-2020 · author-revise-2 · run 43660383766

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/peron-2020/verifier-2-report.md; ls entries/peron-2020 entries/peron-2020/*; grep -n "" docs/protocol.md | sed -n '1,400p' | grep -n -i "step 6\|Hand over\|round 2\|proposed" | head -30
```

**Agent calls ReportFindings**

```json
{
 "findings": []
}
```

```
No findings reported.
```

```
Sun Nov 15 00:56:30 UTC 2026
## Round-2 verifier report: Peron et al. 2020 (CRCNS ssc-11), attempt peron-2020-01

Counts come from the files themselves. The claims file has 31 claims and the attempt record has 31 outcomes with the same IDs: 18 reproduced, 6 partially reproduced, 5 not reproduced, 2 blocked. Six outcomes are marked `assumed: true`, all of them model claims. Cell indices below are positions in the current notebook, counted from 0.

### 1. Outcomes

**The 24 data claims.** I agree with all 24 stated outcomes. The three where I disagreed in round 1 (touch-ablation-size, whisking-ablation-size, per-mouse-table) are now partially reproduced, which matches my round-1 outcomes. They rest on these outputs:
- **touch-ablation-size:** cell 19, rank rule 79.3 ± 27.1.
- **whisking-ablation-size:** 4.43% of the touch neurons per barrel column, and percentiles of 75.4 and 75.8.
- **per-mouse-table:** cell 69, 23 of 24 rows match under the Methods cylinder.

The other 21 are unchanged from round 1 and still agree with the printed numbers.

**Model claims.**

| Claim | Stated | My view |
|---|---|---|
| model-amplification-increases | reproduced (assumed) | **Agree.** Every 0.4 sweep strength (15–50) is below every 0.2 strength (150–400), so the direction does not depend on the calibration (cell 74). Reading (c) cannot be tested: 0.17 is more than the input-recipient share of 200/1,700 = 0.118, so the criterion's "under each reading" is met only for (a) and (b). |
| model-equal-connectivity-ablation-increases | not_reproduced (assumed) | **Do not agree as it stands.** The outcome depends on the attempt's own choice to count inhibitory neurons (about 250 of the 415 neurons per network, cell 80). With excitatory neurons only, scores rise in 30 of 30 networks (p = 1.9e-09), the claimed direction, with values outside tolerance. By the record's own rule for the Pconn 0.4 claim, that is partially reproduced. The printed counts argue against the all-neuron reading. The pap
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
676 docs/protocol.md
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
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 199,345p docs/protocol.md; sed -n 451,676p docs/protocol.md
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

[... 354 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts/ | grep peron; wc -l attempts/peron-2020-01.yaml; ls questions/ | grep peron; cat questions/peron-2020.yaml | head -80; ls executed/peron-2020 2>/dev/null
```

```
peron-2015-01.yaml
peron-2020-01.yaml
965 attempts/peron-2020-01.yaml
peron-2015.yaml
peron-2020.yaml
# Questions from attempt peron-2020-01 (author-revise-1, 2026-11-14) about the claims file
# claims/peron-2020.yaml. Raised by the round-1 verifier (transcripts/peron-2020/verifier-1-report.md,
# problems 2 and 10, and the outcome table) and asked under docs/protocol.md, "Hand over for
# verification"; the claims are tested as written.
questions:
- claim: touch-ablation-size
  asked: 2026-11-14
  question: >-
    The criterion defines the percentile as "the rank of its pre-ablation Rtouch among the
    included touch neurons' pre-ablation Rtouch of its mouse" and cites ablation_summ_stats.m for
    it. The code's rule is not a rank: it takes the position of the first included neuron whose
    score exceeds the ablated neuron's, over the number included, so an ablated neuron that scores
    above every included neuron (or has no score) gets 1/N, not 1. Should the criterion give the
    code's rule, which the paper's "70th ± 35th percentile" follows, or the rank it states?
  passage: >-
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/peron-2020-01.yaml
```

```
<persisted-output>
Output too large (60.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/22505f7c-76cf-4f9f-9a00-8561d42fd1d2/tool-results/bbpykjoik.txt

Preview (first 2KB):
schema_version: 3
id: peron-2020-01
datasets:
- archive: crcns
  id: ssc-11
  version: unversioned
  doi: 10.6080/K0Z31WWG
  relation: primary
paper: doi:10.1038/s41586-020-2062-x
date: '2026-11-14'
entry: peron-2020
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 31 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/22505f7c-76cf-4f9f-9a00-8561d42fd1d2/tool-results/bbpykjoik.txt"
}
```

```
1	schema_version: 3
2	id: peron-2020-01
3	datasets:
4	- archive: crcns
5	  id: ssc-11
6	  version: unversioned
7	  doi: 10.6080/K0Z31WWG
8	  relation: primary
9	paper: doi:10.1038/s41586-020-2062-x
10	date: '2026-11-14'
11	entry: peron-2020
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-15
20	  runner:
[... 946 more lines not kept]
```

**Agent calls Bash**

```bash
cat executed/peron-2020/result.json | head -50; python - <<'EOF'
import json
nb=json.load(open('executed/peron-2020/reproduce_peron_2020.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(i,c['cell_type'],len(src),src[:100].replace('\n',' | '))
EOF
```

```
{
 "entry": "peron-2020",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_peron_2020.ipynb",
   "ok": true,
   "seconds": 2225,
   "error": null
  }
 ]
}
0 markdown 2936 # Reproducing Peron et al. (2020) from CRCNS ssc-11 |  | Paper. Peron S, Pancholi R, Voelcker B, Wittenb
1 code 838 import time | import warnings |  | import matplotlib.pyplot as plt | import numpy as np | import pandas as pd | 
2 markdown 265 ## Data check |  | What each archive holds, against the data descriptor ("session_neuropilone_????_merge
3 code 2346 rows = [] | for a in sorted(data): |     for dname, files in data[a]["sess"].items(): |         for fn, r 
4 code 1589 # every member of every archive, by kind | kinds = [] | for a in sorted(data): |     for name, size in dat
5 markdown 342 Duplicates. The analysis code reuses one directory as the post-ablation data of one | ablation and the
6 code 525 fp = {} | for a in sorted(data): |     for dname, fl in data[a]["sess"].items(): |         for fn, r in fl
7 markdown 450 Clocks. The encoding scores were computed by the authors; this attempt does not recompute | them from 
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('executed/peron-2020/reproduce_peron_2020.ipynb'))
for i,c in enumerate(nb['cells'][71:],start=71):
    print(f"=== {i} {c['cell_type']}")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data']: print('--OUT--');print(''.join(o['data']['text/plain'])[:3000])
EOF
```

```
<persisted-output>
Output too large (44.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/22505f7c-76cf-4f9f-9a00-8561d42fd1d2/tool-results/bxasuw4if.txt

Preview (first 2KB):
=== 71 markdown
## Network model claims

The model outputs were not deposited (claims file, `data: elsewhere`), so the network of the
Methods ("Network model") is rebuilt here in numpy and numba (helper `peron2020_model.py`, whose
docstring gives the source of every parameter). The paper used Brian2; this is a
reimplementation of the same equations and parameters, not the paper's code.

What the Methods leave open, and the choice made for each (each an assumption, recorded in the
attempt):

- The size of the background PSP. The Methods give its frequencies (5,000 and 2,000 Hz) and say
  they were "selected so that the tonic firing rate of these populations were approximately 0.5
  Hz for excitatory neurons and 10 Hz for inhibitory neurons". One PSP per population is set
  here to give those rates at Pconn 0.2 without stimulus (first cell below).
- The sign of inhibitory PSPs: -1 mV ("All connections had the same strength, which was chosen
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/22505f7c-76cf-4f9f-9a00-8561d42fd1d2/tool-results/bxasuw4if.txt"
}
```

```
1	=== 71 markdown
2	## Network model claims
3	
4	The model outputs were not deposited (claims file, `data: elsewhere`), so the network of the
5	Methods ("Network model") is rebuilt here in numpy and numba (helper `peron2020_model.py`, whose
6	docstring gives the source of every parameter). The paper used Brian2; this is a
7	reimplementation of the same equations and parameters, not the paper's code.
8	
9	What the Methods leave open, and the choice made for each (each an assumption, recorded in the
10	attempt):
11	
12	- The size of the background PSP. The Methods give its frequencies (5,000 and 2,000 Hz) and say
13	  they were "selected so that the tonic firing rate of these populations were approximately 0.5
14	  Hz for excitatory neurons and 10 Hz for inhibitory neurons". One PSP per population is set
15	  here to give those rates at Pconn 0.2 without stimulus (first cell below).
16	- The sign of inhibitory PSPs: -1 mV ("All connections had the same strength, which was chosen
17	  so that the resulting post-synaptic potential (PSP) is 1 mV").
18	- The stimulus amplitude is its peak current; its value comes from the readings of the claims
19	  file's opening comment, (a) fraction of excitatory neurons with score above 0.1 equal to 0.108,
20	  (b) smallest Kolmogorov-Smirnov distance to the pooled pre-ablation Rtouch of the touch ablation
[... 565 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper/; grep -n "model-" claims/peron-2020.yaml | head; sed -n 1,60p claims/peron-2020.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 60,330p claims/peron-2020.yaml
```

```
# The code applies the cylinder as lateral distance < 10 um and signed depth difference < 30
# um (get_ablation_data.m), which also drops every neuron shallower than the ablated one within
# 10 um laterally; the Methods cylinder (|depth difference| < 30 um) is the main reading and
# the code's rule a variant. For each mouse, the median of the included neurons' scores before
# and after ablation; across mice, the grand median and the adjusted MAD (1.4826 x MAD); pre
# against post by the Wilcoxon signed-rank test on the paired mouse medians; ablation types
# compared by the Wilcoxon rank-sum test on the per-mouse changes (Methods, Statistical
# analyses; ablation_figure_score_change.m). The response-similarity analysis uses an
# encoding-score cutoff of 0.25 in place of 0.1, with the same shuffle rule (Methods; code).
#
# Tolerances. The +/- values the paper gives with its grand medians and means are the spread
# across mice (adjusted MAD or s.d.), not an uncertainty of the statistic; as the attempt
# reruns the same mice, the statistic itself should come out close, so each value takes 10% of
# itself. Simulation values take 10% likewise, as the networks are random.
#
# Simulation claims (data elsewhere). The model outputs were not deposited; they are to be
# regenerated from the Methods. Open in the Methods and not settled by the repository: the
# input strength for Pconn 0.2 and 0.4, chosen as the one whose excitatory encoding-score
# distribution "most closely" matched the in vivo data "in terms of distribution shape and
# fraction of neurons encoding the stimulus". The paper matched to the data of its ref. 7
[... 251 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i "all neurons\|excitatory neurons\|Network model\|encoding score criteria\|spared neurons" 10.1038-s41586-020-2062-x.txt | head -40
```

```
34:network models. Recurrence among cortical neurons with similar selectivity 
43:input to a subnetwork of the excitatory neurons (200 out of 1,700), corresponding to the number of L2/3 barrel cortex neurons that respond 
67:spared neurons increased after simulated ablation of 10% of the subnetwork14, owing to reduced feedback inhibition13,20 (encoding score, 
84:scores for spared neurons, from 0.243 ± 0.049 to 0.143 ± 0.028 (connectivity = 0.4; P < 0.001, n = 30 networks), because of reduced amplification (Fig. 1d–f). Networks in the all-or-none regime19 were robust 
101:representation and examining the effect on spared neurons. Several 
102:excitatory neurons were ablated using multiphoton excitation9,10 
272:excitatory connectivity. a, The L2/3 network model comprises a subnetwork 
273:of 200 excitatory neurons (black) receiving sensory input (dark grey), a larger 
282:(PSTHs) show mean values across all neurons and networks (n = 30). Bottom, 
283:excitatory neurons within subnetwork; middle, excitatory neurons outside 
288:inhibition dominates and responses among spared neurons increase. In the 
303:Ablation of whisking neurons did not degrade the whisking representation. Our network model suggests that the slower kinetics of 
315:effects of ablation on spared neurons should increase with the similarity 
323:not all neurons were recorded simultaneously (Fig. 2c, Methods), it 
575:Mateo, C. et al. In vivo optogenetic stimulation of neocortical excitatory neurons drives 
785:Network model
857:td is the spike transmission delay. The sum over j is over all neurons, 
860:excitatory and 300 (15%) were inhibitory16. Excitatory neurons had 
864:average, 35 mV for all neurons15,16. Each neuron was assigned a value 
879:excitatory population (1,500 neurons). Although all neurons in L2/3 
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 270,300p paper/10.1038-s41586-020-2062-x.txt; sed -n 905,975p paper/10.1038-s41586-020-2062-x.txt; grep -n -i "imaged\|recorded excitatory\|only excitatory\|inhibitory neurons" paper/10.1038-s41586-020-2062-x.txt | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/peron-2020/reproduce_peron_2020.ipynb'))
for i in [0,1,18,19,20,38]:
    c=nb['cells'][i]
    print(f"=== {i}");print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:2500])
EOF
grep -n "def run_jobs\|def effect\|def spared\|def stimulus\|cache\|CACHE" entries/peron-2020/peron2020_model.py entries/peron-2020/peron2020.py | head -30
```

```
=== 0
# Reproducing Peron et al. (2020) from CRCNS ssc-11

Paper. Peron S, Pancholi R, Voelcker B, Wittenbach JD, Olafsdottir HF, Freeman J, Svoboda K
(2020). Recurrent interactions in local cortical circuits. *Nature* 579, 256-259.
[doi:10.1038/s41586-020-2062-x](https://doi.org/10.1038/s41586-020-2062-x). The claims file
(`claims/peron-2020.yaml`) was written from the version of record, with its Methods, Extended
Data figure legends, Extended Data Table 1 and reporting summary.

Data set. [CRCNS ssc-11](https://doi.org/10.6080/K0Z31WWG) (doi:10.6080/K0Z31WWG), read
from the public bucket `crcnsarchive` under `ssc-11/live/data/`, one `an<id>.tar.gz` per mouse
(16 files, 128 GB). CRCNS data sets are not versioned, so the version is recorded as
`unversioned`; the bucket holds one copy of each file (no `old/` folder), the one described by
the data descriptor version 0.6 (20 February 2020), which is the version the paper's data
statement points to. It is pinned here by the MD5 sums of `checksums.md5`, printed below for
every file read, so that a later change is detectable.

Reading. A gzip stream cannot be read at an offset, so each archive is streamed once from
front to back and every member the claims use is reduced in memory as it passes (helper
`peron2020.py`). Nothing is written to disk. Four archives are read at a time; the full pass
[... 174 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2020; grep -n "^def \|^    def \|^[A-Z_]* = " peron2020.py | head -60; sed -n 380,430p peron2020_model.py; nproc; free -g
```

```
50:BASE = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-11/live/data/"
51:CHECKSUMS = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-11/live/checksums.md5"
52:FILELIST = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-11/live/filelist.txt"
53:DATASET = "ssc-11"
54:VERSION = "unversioned"  # CRCNS data sets are not versioned; the MD5 sums pin the files
55:DOI = "10.6080/K0Z31WWG"
57:PRE = "session_neuropilone_preablate_merged"
58:POST = "session_neuropilone_postablate_merged"
61:def _p(t):
66:ABLATIONS = {
94:ANIMS = {
99:MICE = sorted({a for v in ANIMS.values() for a in v})
100:NYU = {"276013", "275801", "275798", "274577", "274424", "272761", "278288", "278759"}
102:WHISK_FEAT = "eventBasedDff_k16t14_MeanWhiskerAmplitudeGLMScore"
103:TOUCH_FEAT = "eventBasedDff_k16t14_{}AbsMaxKappaZeroNotouchGLMScore"
110:def checksums():
115:def _feat(cf, key):
122:def _triggered(trace, ca_t, onsets, lags):
132:def reduce_sess(raw: bytes, wtag=None):
218:def _h5str(d):
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/explore; cat > $TMPDIR/explore/sweep.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0, "entries/peron-2020")
import peron2020_model as PM
SW = {(0.2, 10.0): [0, 25, 50, 75, 100, 125, 150], (0.4, 10.0): [0, 3, 6, 9, 12, 15], (0.4, 50.0): [0, 1, 2, 3]}
t = time.time()
jobs = [dict(kind="pre_only", seeds=[900 + k], pconn=pc, strength=float(s), peak_ms=pk) for (pc, pk), ss in SW.items() for s in ss for k in range(2)]
sw = PM.run_jobs(jobs)
print("sweep", time.time() - t, "s", flush=True)
import pickle; pickle.dump(sw, open(sys.argv[1], "wb"))
EOF
cd $TMPDIR/explore && time python sweep.py sw.pkl
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/explore/sweep.py", line 1, in <module>
    import sys, time, numpy as np
ModuleNotFoundError: No module named 'numpy'

real	0m0.030s
user	0m0.027s
sys	0m0.002s
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/entry.py | grep -n "venv\|python\|uv" | head; ls -a | head -30; ls executed/
```

```
3:    python tools/entry.py lock  entries/<name>   # pin the environment
4:    python tools/entry.py check entries/<name>   # validate metadata and conventions
5:    python tools/entry.py check entries/*/       # the same for every entry, in one process
6:    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
7:    python tools/entry.py all   entries/<name>   # check, then run
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
41:Requires `uv` on PATH, and `pyyaml`, `jsonschema` and `nbformat` to run this
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
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "uv \|\"uv\"\|venv" tools/entry.py | head -20
```

```
448:    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--generate-hashes", "--python-version", version,
519:        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
555:    venv = (output_dir / ".venv").resolve()
556:    python = venv / "bin" / "python"
560:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
561:                ["uv", "pip", "install", "--quiet", "--python", str(python),
563:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
577:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
```

**Agent calls Bash**

```bash
cd  uv venv --quiet --python 3.13 $TMPDIR/venv && uv pip install --quiet --python $TMPDIR/venv/bin/python -r entries/peron-2020/requirements.lock.txt && echo ok; cd $TMPDIR/explore && time $TMPDIR/venv/bin/python sweep.py sw.pkl
```

```
ok
sweep 82.65347361564636 s

real	1m25.443s
user	4m42.811s
sys	0m37.195s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat > $TMPDIR/explore/invivo.py <<'EOF'
import sys, time, numpy as np
sys.path.insert(0, "entries/peron-2020")
import peron2020 as P
t = time.time()
data, sizes = P.load_all(mice=P.ANIMS["touch"], workers=4)
iv = np.concatenate([P.ablation_table(data[a], a, "touch")[0].t_pre.dropna().values for a in P.ANIMS["touch"]])
np.save("invivo.npy", iv)
print(len(iv), np.median(iv), time.time() - t)
EOF
cd $TMPDIR/explore && $TMPDIR/venv/bin/python invivo.py
```

```
entries/peron-2020/peron2020.py:205: RuntimeWarning: Mean of empty slice
  pop = np.nanmean(dff[sel], axis=0) if len(sel) else np.nanmean(dff, axis=0)
entries/peron-2020/peron2020.py:205: RuntimeWarning: Mean of empty slice
  pop = np.nanmean(dff[sel], axis=0) if len(sel) else np.nanmean(dff, axis=0)
entries/peron-2020/peron2020.py:205: RuntimeWarning: Mean of empty slice
  pop = np.nanmean(dff[sel], axis=0) if len(sel) else np.nanmean(dff, axis=0)
entries/peron-2020/peron2020.py:298: RuntimeWarning: Mean of empty slice
  pop = np.nanmean(dset[:, sel], axis=1) if len(sel) else np.nanmean(dset[()], axis=1)
entries/peron-2020/peron2020.py:298: RuntimeWarning: Mean of empty slice
  pop = np.nanmean(dset[:, sel], axis=1) if len(sel) else np.nanmean(dset[()], axis=1)
entries/peron-2020/peron2020.py:205: RuntimeWarning: Mean of empty slice
  pop = np.nanmean(dff[sel], axis=0) if len(sel) else np.nanmean(dff, axis=0)
69291 -0.019979162997649482 620.4448771476746
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/explore && $TMPDIR/venv/bin/python - <<'EOF'
import sys, pickle, numpy as np
sys.path.insert(0, "entries/peron-2020")
import peron2020_model as PM
from scipy import stats
sw = pickle.load(open("sw.pkl","rb")); iv = np.load("invivo.npy")
keys = sorted({(d["pconn"], d["peak"], d["strength"]) for d in sw})
for k in keys:
    ds=[d for d in sw if (d["pconn"], d["peak"], d["strength"])==k]
    e=np.concatenate([d["pre"][:PM.NEXC] for d in ds])
    print(k, f"frac>0.1 {np.mean(e>0.1):.3f} KS {stats.ks_2samp(e,iv).statistic:.3f} median {np.median(e):.3f} q10 {np.quantile(e,.1):.3f} q90 {np.quantile(e,.9):.3f} nonrecip>0.1 {np.mean(np.concatenate([d['pre'][PM.NS:PM.NEXC] for d in ds])>0.1):.3f}")
print("invivo q", np.quantile(iv,[.1,.5,.9]))
EOF
```

```
(0.2, 10.0, 0.0) frac>0.1 0.001 KS 0.516 median 0.000 q10 -0.008 q90 0.014 nonrecip>0.1 0.001
(0.2, 10.0, 25.0) frac>0.1 0.026 KS 0.507 median 0.000 q10 -0.012 q90 0.016 nonrecip>0.1 0.000
(0.2, 10.0, 50.0) frac>0.1 0.044 KS 0.483 median 0.000 q10 -0.015 q90 0.012 nonrecip>0.1 0.000
(0.2, 10.0, 75.0) frac>0.1 0.054 KS 0.468 median 0.000 q10 -0.020 q90 0.014 nonrecip>0.1 0.000
(0.2, 10.0, 100.0) frac>0.1 0.067 KS 0.469 median 0.000 q10 -0.018 q90 0.024 nonrecip>0.1 0.000
(0.2, 10.0, 125.0) frac>0.1 0.077 KS 0.470 median 0.000 q10 -0.019 q90 0.037 nonrecip>0.1 0.001
(0.2, 10.0, 150.0) frac>0.1 0.091 KS 0.476 median 0.000 q10 -0.019 q90 0.072 nonrecip>0.1 0.000
(0.4, 10.0, 0.0) frac>0.1 0.000 KS 0.514 median 0.000 q10 -0.010 q90 0.013 nonrecip>0.1 0.000
(0.4, 10.0, 3.0) frac>0.1 0.001 KS 0.523 median 0.000 q10 -0.006 q90 0.017 nonrecip>0.1 0.001
(0.4, 10.0, 6.0) frac>0.1 0.001 KS 0.525 median 0.000 q10 -0.006 q90 0.028 nonrecip>0.1 0.000
(0.4, 10.0, 9.0) frac>0.1 0.009 KS 0.522 median 0.000 q10 -0.007 q90 0.034 nonrecip>0.1 0.000
(0.4, 10.0, 12.0) frac>0.1 0.068 KS 0.538 median 0.000 q10 -0.002 q90 0.047 nonrecip>0.1 0.000
(0.4, 10.0, 15.0) frac>0.1 0.079 KS 0.547 median 0.000 q10 0.000 q90 0.056 nonrecip>0.1 0.000
(0.4, 50.0, 0.0) frac>0.1 0.016 KS 0.510 median 0.000 q10 -0.016 q90 0.026 nonrecip>0.1 0.014
(0.4, 50.0, 1.0) frac>0.1 0.017 KS 0.525 median 0.000 q10 -0.011 q90 0.030 nonrecip>0.1 0.015
(0.4, 50.0, 2.0) frac>0.1 0.021 KS 0.519 median 0.000 q10 -0.013 q90 0.029 nonrecip>0.1 0.013
(0.4, 50.0, 3.0) frac>0.1 0.081 KS 0.536 median 0.000 q10 -0.004 q90 0.068 nonrecip>0.1 0.010
invivo q [-0.07941111 -0.01997916  0.12113789]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  grep -n -i "mCherry\|Slc17a7\|Emx1\|nuclear\|excitatory" paper/10.1038-s41586-020-2062-x.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 95,110p paper/10.1038-s41586-020-2062-x.txt; sed -n 1070,1085p paper/10.1038-s41586-020-2062-x.txt; grep -n -i "Ai162\|cre\b\|GCaMP6s" paper/10.1038-s41586-020-2062-x.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  date -u; grep -rn "proposed" tools/entry.py schemas/ 2>/dev/null | head -20; ls schemas 2>/dev/null
```

```
Sun Nov 15 01:11:26 UTC 2026
tools/entry.py:372:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
schemas/attempt.schema.json:303:          "proposed": {
schemas/claims.schema.json:3:  "title": "Claims proposed for one target (a dataset and one of its papers)",
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
```

**Agent calls Bash**

```bash
cd  sed -n 290,340p schemas/attempt.schema.json; sed -n 340,390p tools/entry.py; grep -n "verifications" -A60 schemas/attempt.schema.json | grep -n "\"[a-z_]*\":" | head -30
```

```
},
          "deviations": {
            "description": "How the test differed from the paper's method or data, e.g. one session of four, or a substituted model.",
            "type": "array",
            "items": {
              "type": "string",
              "minLength": 1
            }
          },
          "assumed": {
            "description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says what was assumed and why (docs/protocol.md, Author, step 1.6).",
            "type": "boolean"
          },
          "proposed": {
            "description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
            "type": "object",
            "additionalProperties": false,
            "required": [
              "outcome",
              "reason"
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 386,470p schemas/attempt.schema.json
```

```
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
          "kind": {
            "enum": [
              "agent",
              "person",
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/peron-2020/reproduce_peron_2020.ipynb'))
for i in [4,37,54,56,57,69]:
    c=nb['cells'][i]
    print(f"=== {i}");print(''.join(c['source'])[:1500])
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:4000])
EOF
```

```
=== 4
# every member of every archive, by kind
kinds = []
for a in sorted(data):
    for name, size in data[a]["members"]:
        rel = name.split("/", 1)[1] if "/" in name else ""
        k = ("session struct" if rel.endswith("sess_struct.mat") else "JRC ablation log" if "/ablation_log_" in rel
             else "NYU attempt log" if "_attempt_" in rel else "curation file" if (rel.endswith("manualCurationData.mat") or rel.endswith("ablation_ids_manually_curated.mat") or (rel.count("/") == 0 and rel.endswith(".mat")))
             else "directory" if size == 0 else "other")
        kinds.append({"mouse": a, "kind": k, "size": size, "name": rel})
kinds = pd.DataFrame(kinds)
print(kinds.groupby("kind").agg(n=("size", "size"), GB=("size", lambda s: round(s.sum() / 1e9, 1))).to_string())
print("\nOther files:")
oth = kinds[kinds.kind == "other"].copy()
oth["base"] = oth.name.map(lambda n: n.rsplit("/", 1)[-1])
oth["ext"] = oth.base.map(lambda n: n.rsplit(".", 1)[-1].lower() if "." in n else "(none)")
print(f"{len(oth)} files; by extension:", oth.ext.value_counts().to_dict())
for a, g in oth.groupby("mouse"):
    print(f"an{a}: {len(g)} files, {round(g['size'].sum() / 1e6, 1)} MB:", sorted(set(g.base)))
hist = oth[oth.base.str.contains("iba|gfap|histo|slice|section|\\.tif|\\.czi|\\.lsm|\\.nd2|\\.jpg|\\.png", case=False, regex=True)]
[... 232 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2020; python -c "
import json;nb=json.load(open('reproduce_peron_2020.ipynb'));print(len(nb['cells']), sum(len(c.get('outputs',[])) for c in nb['cells']))
for i in [76,80,85,88,91]: print(i, nb['cells'][i]['metadata'])
"; cat README.md | head -60
```

```
95 0
76 {}
80 {'tags': ['claim:model-equal-connectivity-ablation-increases', 'claim:model-increased-connectivity-ablation-decreases']}
85 {'tags': ['claim:model-more-ablation-larger-decline']}
88 {'tags': ['claim:model-slow-input-sensitive']}
91 {'tags': ['claim:model-response-similarity']}
# Peron et al. (2020) from CRCNS ssc-11

Tests the findings of [Peron et al. (2020)](https://doi.org/10.1038/s41586-020-2062-x),
"Recurrent interactions in local cortical circuits", that can be tested on
[CRCNS ssc-11](https://doi.org/10.6080/K0Z31WWG): volumetric calcium imaging of L2/3 of mouse
barrel cortex in 16 mice before and after 24 targeted ablations of touch, whisking or silent
neurons. The notebook streams the 16 archives (128 GB) from the public CRCNS bucket once, in
about 17 minutes, and reduces them in memory. It then rebuilds the network model of the Methods
(2,000 leaky integrate-and-fire neurons, helper `peron2020_model.py`) and simulates 30 networks
per condition, in about 30 minutes.

| Claim | Outcome |
|---|---|
| Model: amplification grows with subnetwork connectivity | Reproduced (resting on assumptions) |
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2020; python - <<'EOF'
import json
nb=json.load(open('reproduce_peron_2020.ipynb'))
for i in [0,18,20,38,71,73,75,76,78,80,81,83,85,86,88,89,91,92,93]:
    print(f"=== {i}"); print(''.join(nb['cells'][i]['source']))
EOF
```

```
=== 0
# Reproducing Peron et al. (2020) from CRCNS ssc-11

Paper. Peron S, Pancholi R, Voelcker B, Wittenbach JD, Olafsdottir HF, Freeman J, Svoboda K
(2020). Recurrent interactions in local cortical circuits. *Nature* 579, 256-259.
[doi:10.1038/s41586-020-2062-x](https://doi.org/10.1038/s41586-020-2062-x). The claims file
(`claims/peron-2020.yaml`) was written from the version of record, with its Methods, Extended
Data figure legends, Extended Data Table 1 and reporting summary.

Data set. [CRCNS ssc-11](https://doi.org/10.6080/K0Z31WWG) (doi:10.6080/K0Z31WWG), read
from the public bucket `crcnsarchive` under `ssc-11/live/data/`, one `an<id>.tar.gz` per mouse
(16 files, 128 GB). CRCNS data sets are not versioned, so the version is recorded as
`unversioned`; the bucket holds one copy of each file (no `old/` folder), the one described by
the data descriptor version 0.6 (20 February 2020), which is the version the paper's data
statement points to. It is pinned here by the MD5 sums of `checksums.md5`, printed below for
every file read, so that a later change is detectable.

Reading. A gzip stream cannot be read at an offset, so each archive is streamed once from
front to back and every member the claims use is reduced in memory as it passes (helper
`peron2020.py`). Nothing is written to disk. Four archives are read at a time; the full pass
[... 284 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2020; python - <<'EOF'
import json
nb=json.load(open('reproduce_peron_2020.ipynb'))
print(''.join(nb['cells'][94]['source']))
print(''.join(nb['cells'][74]['source'])[:300])
EOF
```

```
## Summary

| Claim | Outcome | Note |
|---|---|---|
| model-amplification-increases | Reproduced (assumed) | Matched strength 218 at Pconn 0.2, 28.2 at 0.4 (calibration a); reading (c) cannot be met |
| model-equal-connectivity-ablation-increases | Not reproduced (assumed) | 0.287 -> 0.279 (all neurons); excitatory neurons rise, 0.546 -> 0.562; values outside tolerance |
| model-increased-connectivity-ablation-decreases | Partially reproduced (assumed) | 0.282 -> 0.096, p < 0.001; values outside tolerance |
| model-all-or-none-robust | Blocked | Extrapolated input strength at Pconn 0.44 is negative; reset pulse not specified |
| model-more-ablation-larger-decline | Partially reproduced (assumed) | Decline grows with size; R = -0.726 / -0.558, outside -0.65 ± 0.065 |
| model-slow-input-sensitive | Partially reproduced (assumed) | 0.269 -> 0.088 at Pconn 0.4, no change at 0.2; values outside tolerance |
| model-response-similarity | Not reproduced (assumed) | Slopes positive at Pconn 0.4 (p = 0.0014) |
| neurons-per-mouse | Reproduced | 8,126 ± 2,436; all 16 counts equal Extended Data Table 1 |
| representation-sizes | Reproduced | Reading (a), score above 0.1 |
| touch-ablation-size | Partially reproduced | 16.8 ± 12.8 and 5.85%; percentile 79.3 ± 27.1 by the criterion's rank rule (70.3 ± 35.0 by the code's) |
| touch-ablation-reduces-touch | Reproduced | 0.123 -> 0.100, p = 0.004 |
| touch-ablation-touch-count | Reproduced | 932 -> 716, reading (a) |
| touch-ablation-whisking-unchanged | Reproduced | p = 0.820 |
| ablation-size-correlation | Reproduced | R = -0.790 and -0.761 |
| distance-dependence-touch | Reproduced | -0.133 / -0.056, lambda 87 um, reading (a) |
| distance-dependence-whisking-absent | Reproduced | p = 0.164 |
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2020; cat > $TMPDIR/edit1.py <<'PYEOF'
import json
F = 'reproduce_peron_2020.ipynb'
nb = json.load(open(F))
def src(i): return ''.join(nb['cells'][i]['source'])
def setsrc(i, s):
    lines = s.split('\n')
    nb['cells'][i]['source'] = [l + '\n' for l in lines[:-1]] + [lines[-1]]
def rep(i, old, new):
    s = src(i)
    assert old in s, (i, old[:60])
    setsrc(i, s.replace(old, new))

# cell 0: size and time
rep(0, "(16 files, 128 GB)", "(16 files, 120.9 GB compressed)")
rep(0, "the full pass\ntakes about 17 minutes.", "the full pass\ntakes about 11 minutes (648 s in the run below).")
# cell 18: percentile rule
rep(18, """The percentile follows ablation_summ_stats.m: the position of the first included neuron whose
score exceeds the ablated neuron's, over the number of included neurons (1 when none exceeds
it), pooled over ablated neurons.""",
"""Two percentile rules, pooled over ablated neurons. The criterion's rule is a rank: the fraction
of included neurons whose score is at or below the ablated neuron's (1 when none exceeds it;
ablated neurons with no score are left out). The code's rule (ablation_summ_stats.m) is the
position of the first included neuron whose score exceeds the ablated neuron's, over the number
of included neurons; when none exceeds it, or the ablated neuron has no score, the position is
the first, so the value is 1/N (the synthetic check below gives 0.01 for a score above all
100).""")
# cell 20: silent targeting
rep(20, "is 0.079 Hz); the rule was applied by the authors at targeting time, on other data.",
    "is 0.079 Hz). The paper gives the 0.025 Hz rule for choosing targets; 12 of the 130 ablated\nneurons are above it in these pre-ablation data.")
# cell 38
rep(38, "The ± values above (median-based) are therefore about half the paper's.",
    "The ± values above (median-based) are therefore about half the paper's for the touch\nablations (0.011 / 0.016 against 0.021 / 0.037), and about a tenth for the whisking ablations\n(Rtouch 0.008 / 0.009 against 0.081 / 0.069), whose paper values come from the zero-padded\nmatrix.")
# cell 71: assumptions
rep(71, """- The stimulus amplitude is its peak current; its value comes from the readings of the claims
  file's opening comment, (a) fraction of excitatory neurons with score above 0.1 equal to 0.108,
  (b) smallest Kolmogorov-Smirnov distance to the pooled pre-ablation Rtouch of the touch ablation
  mice, (c) fraction equal to 0.17.
- Which neurons enter "all neurons that met the 0.1 encoding score criteria": all neurons of the
  network (main, as the Methods say "all neurons") and excitatory neurons only (variant).""",
"""- The stimulus amplitude is its peak current; its value comes from the readings of the claims
  file's opening comment, (a) fraction of excitatory neurons with score above 0.1 equal to 0.108,
  (b) smallest Kolmogorov-Smirnov distance to the pooled pre-ablation Rtouch of the touch ablation
  mice, (c) fraction equal to 0.17. Reading (b) sets a strength only where its smallest distance
  lies at a positive strength inside the sweep, which reaches down to no input.
- Which neurons enter "all neurons that met the 0.1 encoding score criteria": excitatory
  neurons only (main) and all neurons of the network, inhibitory ones included (variant). The
  Methods match the input on the "distributions of excitatory neuron encoding scores", ablate
  "the 20 excitatory neurons with the highest encoding score", and the in vivo data the model
  stands for are of excitatory neurons (Ai162 x Slc17a7-IRES2-cre mice; Emx1-IRES-cre mice,
  whose mCherry marks "only ... nuclei of excitatory neurons"; Methods, Mice). The paper's
  counts for Fig. 3b (3,466 and 3,779 neurons above 0.25 over 30 networks) are also nearer the
  excitatory counts here than those of all neurons (model-response-similarity cell). An earlier
  revision of this notebook counted all neurons; the outcomes that the change moves are proposed
  in the attempt record for a further verification round.""")
# cell 73
rep(73, """Reading (a) interpolates linearly to the fraction 0.108, reading
(c) to 0.17, and reading (b) takes the strength of the grid with the smallest distance.""",
"""Reading (a) interpolates linearly to the fraction 0.108, reading
(c) to 0.17, and reading (b) takes the strength of the grid with the smallest distance, set
only when that strength is positive and inside the grid. Each sweep starts at no input (strength
0), so that a minimum at the weakest strength tried can be told from one at no input.""")
# cell 74: sweep code
rep(74, """SW = {(0.2, 10.0): [150, 175, 200, 225, 250, 300, 400], (0.4, 10.0): [15, 20, 25, 30, 35, 40, 50],
      (0.2, 50.0): [50, 70, 90, 110, 140, 200], (0.4, 50.0): [3, 5, 7, 9, 12, 15]}""",
"""SW = {(0.2, 10.0): [0, 25, 50, 75, 100, 125, 150, 175, 200, 225, 250, 300, 400], (0.4, 10.0): [0, 3, 6, 9, 12, 15, 20, 25, 30, 35, 40, 50],
      (0.2, 50.0): [0, 25, 50, 70, 90, 110, 140, 200], (0.4, 50.0): [0, 1, 2, 3, 5, 7, 9, 12, 15]}""")
rep(74, """f"range {invivo.min():.3f} to {invivo.max():.3f}")""",
    """f"range {invivo.min():.3f} to {invivo.max():.3f}, fraction exactly 0 {np.mean(invivo == 0):.3f}")""")
rep(74, """"frac_exc_0.1": np.mean(e > 0.1),""", """"frac_exc_0.1": np.mean(e > 0.1), "frac_exc_zero": np.mean(e == 0),""")
rep(74, """    STR[("b", pc, pk)] = float(x[np.argmin(g.KS.values)])
    print(f"Pconn {pc}, peak {pk:.0f} ms: (a) {STR[('a', pc, pk)]:.1f}; (b) {STR[('b', pc, pk)]:.1f} (KS {g.KS.min():.3f}); \"""",
"""    k = int(np.argmin(g.KS.values))
    STR[("b", pc, pk)] = float(x[k]) if 0 < k < len(x) - 1 else np.nan  # a minimum at no input or at the strongest input sets none
    print(f"Pconn {pc}, peak {pk:.0f} ms: (a) {STR[('a', pc, pk)]:.1f}; (b) {STR[('b', pc, pk)]:.1f} (smallest KS {g.KS.min():.3f} at strength {x[k]:g}; "
          f"next smallest {np.sort(g.KS.values)[1]:.3f}); \"""")
# cell 76: main population first
rep(76, """    for pop in ["all", "exc"]:
        e, p = summarize(c, size, pop)
        res[pop] = (e, p)
        print(f"{label}, {'all neurons' if pop == 'all' else 'excitatory only'}:""",
"""    for pop in ["exc", "all"]:
        e, p = summarize(c, size, pop)
        res[pop] = (e, p)
        print(f"{label}, {'all neurons (variant)' if pop == 'all' else 'excitatory only (main)'}:""")
rep(76, 'def summarize(c, size=20, pop="all", thresh=0.1):', 'def summarize(c, size=20, pop="exc", thresh=0.1):')
rep(80, """e, _ = MODEL[("a", 0.2)]["all"]
print("\\nReading (a), Pconn 0.2, per network:")""", """e, _ = MODEL[("a", 0.2)]["exc"]
print("\\nReading (a), Pconn 0.2, excitatory neurons, per network:")""")
rep(85, """    for pop in ["all", "exc"]:""", """    for pop in ["exc", "all"]:""")
rep(85, """{'all neurons' if pop == 'all' else 'excitatory only'}, {lab}""", """{'all neurons (variant)' if pop == 'all' else 'excitatory only (main)'}, {lab}""")
rep(91, """        for pop in ["all", "exc"]:""", """        for pop in ["exc", "all"]:""")
rep(91, """{'all neurons' if pop == 'all' else 'excitatory only'}: {n_} neurons""", """{'all neurons (variant)' if pop == 'all' else 'excitatory only (main)'}: {n_} neurons""")
json.dump(nb, open(F, 'w'), indent=1, ensure_ascii=False)
open(F, 'a').write('\n')
PYEOF
python $TMPDIR/edit1.py && git diff --stat
```

```
entries/peron-2020/reproduce_peron_2020.ipynb | 75 +++++++++++++++++----------
 1 file changed, 48 insertions(+), 27 deletions(-)
```

**Agent calls Bash**

```bash
cd  git diff entries/peron-2020/reproduce_peron_2020.ipynb | head -30; git show HEAD:entries/peron-2020/reproduce_peron_2020.ipynb | tail -c 300 | od -c | tail -3
```

```
diff --git a/entries/peron-2020/reproduce_peron_2020.ipynb b/entries/peron-2020/reproduce_peron_2020.ipynb
index 0b5348f..8822bf6 100644
--- a/entries/peron-2020/reproduce_peron_2020.ipynb
+++ b/entries/peron-2020/reproduce_peron_2020.ipynb
@@ -15,7 +15,7 @@
     "\n",
     "Data set. [CRCNS ssc-11](https://doi.org/10.6080/K0Z31WWG) (doi:10.6080/K0Z31WWG), read\n",
     "from the public bucket `crcnsarchive` under `ssc-11/live/data/`, one `an<id>.tar.gz` per mouse\n",
-    "(16 files, 128 GB). CRCNS data sets are not versioned, so the version is recorded as\n",
+    "(16 files, 120.9 GB compressed). CRCNS data sets are not versioned, so the version is recorded as\n",
     "`unversioned`; the bucket holds one copy of each file (no `old/` folder), the one described by\n",
     "the data descriptor version 0.6 (20 February 2020), which is the version the paper's data\n",
     "statement points to. It is pinned here by the MD5 sums of `checksums.md5`, printed below for\n",
@@ -24,7 +24,7 @@
     "Reading. A gzip stream cannot be read at an offset, so each archive is streamed once from\n",
     "front to back and every member the claims use is reduced in memory as it passes (helper\n",
     "`peron2020.py`). Nothing is written to disk. Four archives are read at a time; the full pass\n",
-    "takes about 17 minutes.\n",
+    "takes about 11 minutes (648 s in the run below).\n",
     "\n",
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2020; cat > $TMPDIR/edit2.py <<'PYEOF'
import json
F = 'reproduce_peron_2020.ipynb'
nb = json.load(open(F))
def src(i): return ''.join(nb['cells'][i]['source'])
def setsrc(i, s):
    lines = s.split('\n')
    nb['cells'][i]['source'] = [l + '\n' for l in lines[:-1]] + [lines[-1]]
def rep(i, old, new):
    s = src(i); assert old in s, (i, old[:60]); setsrc(i, s.replace(old, new))
rep(0, "takes about 11 minutes (648 s in the run below).", "takes about 11 minutes.")

setsrc(78, """**Result: reproduced, resting on assumptions.** Under calibration (a) the matched strength is
218.0 at Pconn 0.2 and 28.2 at 0.4, so normalized amplification at 0.4 is 7.74, and the strength
at 0.4 is below that at 0.2. Reading (a) is weakly set at Pconn 0.2: the fraction above 0.1 moves
only from 0.106 to 0.109 between strengths 200 and 225, with two networks per strength, which
bears on how large the amplification is, not on its direction. Reading (b) sets no strength at
Pconn 0.4: with the sweep extended down to no input, the smallest KS distance for the touch input
is at strength 0 (0.514), and the distance hardly depends on the input (0.514 to 0.579 over the
whole sweep), because about half of the model's excitatory neurons score exactly 0 (no spike
near a stimulus) while in vivo almost none does. At Pconn 0.2 its minimum is at 75 (0.468, with
0.469 and 0.470 at 100 and 125). Reading (c), the fraction 0.17, cannot be met: the largest
fraction of excitatory neurons above 0.1 in any sweep is 0.119, as nearly only the 200
input-recipient neurons (11.8% of the excitatory population) reach it. The claim holds under the
one reading that sets both strengths. Amplification here is far larger than the paper's Fig. 1c.""")

setsrc(81, """**Result: model-equal-connectivity-ablation-increases not reproduced as verified; partially
reproduced under the revised population (proposed), resting on assumptions.** At Pconn 0.2 under
calibration (a), the spared excitatory neurons (above 0.1 before or after, ablated ones left
out) go from a grand median of 0.546 to 0.562 (signed-rank p = 1.9e-09, 30 of 30 networks
increase), the claimed increase at p < 0.001, with both values far outside 0.237 ± 0.024 and
0.274 ± 0.027. Counting all neurons (variant), the scores fall, 0.287 to 0.279 (p = 6.3e-05, 4
of 30 increase), and 0.287 is outside tolerance. The verified outcome, not reproduced, was set
with all neurons counted; under the revised choice the effect is present and the values are
not, which is partially reproduced, as for the Pconn 0.4 claim. The change is proposed for a
further verification round.

**Result: model-increased-connectivity-ablation-decreases partially reproduced, resting on
assumptions.** At Pconn 0.4 ablation lowers the spared neurons' scores under both populations:
0.356 to 0.231 (excitatory, p = 3.9e-07, 4 of 30 increase) and 0.282 to 0.096 (all neurons, p =
1.9e-08). Neither gives both grand medians within 0.243 ± 0.024 and 0.143 ± 0.014.""")

setsrc(83, """**Result: not tested (blocked, methods underspecified).** Linear extrapolation of the two matched
strengths to Pconn 0.44 gives -9.8 under calibration (a), and readings (b) and (c) set no
strength at Pconn 0.4, so twice the extrapolated strength, the input the Methods use in this
regime, is not a positive current here. The negative value follows from this attempt's
calibration, whose amplification at Pconn 0.4 (7.7) is far above the paper's Fig. 1c. The
Methods also give neither the matched strengths nor the strength and length of the reset pulse
to the inhibitory population, and the pulse they place 300 ms after each onset falls on the
next onset at the 300 ms interval of the claims file. No run was made.""")

setsrc(86, """**Result: model-more-ablation-larger-decline partially reproduced as verified; reproduced under
the revised population (proposed), resting on assumptions.** Under calibration (a), with
excitatory neurons, the median change falls with each larger ablation (0, -0.026, -0.123 and
-0.209 for 0, 10, 20 and 50 ablated), and the change correlates with the net score ablated, R =
-0.590 with the 0-ablation networks (p = 1.3e-12, n = 120), within -0.65 ± 0.065, and -0.456
without them (p = 6.3e-06). The criterion asks for R within tolerance under one of the two
readings and a larger decline at each size, so it is met. With all neurons (variant) R is
-0.726 and -0.558, both outside the tolerance. The verified outcome, partially reproduced, was
set with all neurons counted; the change to reproduced is proposed for a further verification
round. Calibration (b) gave the runs of the earlier revision (R = -0.774 and -0.678 with all
neurons); with its sweep extended to no input it sets no strength at Pconn 0.4 (calibration
cell), so it is not run.""")

setsrc(89, """**Result: model-slow-input-sensitive partially reproduced, resting on assumptions.** With the
slow-input strength set anew under calibration (a) (6.6 at Pconn 0.4, 87.3 at 0.2), the score of
the excitatory neurons at Pconn 0.4 falls from 0.314 to 0.104 (p = 3.9e-07, 3 of 30 networks
increase); the post value is within 0.104 ± 0.010 and the pre value is outside 0.143 ± 0.014. At
Pconn 0.2 it rises, 0.803 to 0.850 (p = 1.9e-09, 30 of 30), so it is not degraded, as the claim
says. With the touch-input strength (slow reading (a)) the score does not fall at Pconn 0.4
(0.952 to 0.947, p = 0.16). All neurons (variant) give 0.269 to 0.088 at Pconn 0.4 and no change
at 0.2 (0.424 to 0.424, p = 0.21) with the strength set anew. No reading gives both grand
medians within tolerance, so the effect is present and the values are not. Calibration (b) sets
no strength for the slow input at Pconn 0.4 (calibration cell).""")

setsrc(92, """**Result: model-response-similarity not reproduced, resting on assumptions.** Under calibration
(a), with excitatory neurons, the per-network slopes of the change in score against response
similarity are negative at Pconn 0.2 (30 of 30, sign test p = 1.9e-09) and show no dependence at
Pconn 0.4 (11 of 30 negative, p = 0.2), the reverse of the claim, which needs negative slopes at
0.4 and none at 0.2. All neurons (variant) give positive slopes at Pconn 0.4 (6 of 30 negative,
p = 0.0014) and mostly positive ones at 0.2 (8 of 30 negative, p = 0.016). The bin-mean fit
leans the same way. The excitatory counts (4,327 at Pconn 0.2 and 4,058 at 0.4) are nearer the
paper's 3,779 and 3,466 than the counts of all neurons (7,815 and 7,078).""")

setsrc(93, """### What the model section shows

The rebuilt network reproduces the direction of the paper's results at increased connectivity
(amplification grows with Pconn; ablation lowers scores at Pconn 0.4, more for larger
ablations, for touch and for slow input) and, with excitatory neurons counted, the rise in
scores at equal connectivity, but not the paper's numbers, nor the response-similarity result.
The choices the outcomes rest on are those listed at the top of the section (background PSP,
inhibitory PSP, stimulus amplitude, which neurons are counted) and the calibration: (a) is the
only reading that sets both matched strengths, as (b)'s smallest distance lies at no input at
Pconn 0.4 and (c) cannot be met. Under the calibration the background gives 0.51 Hz and 10.35
Hz without stimulus, as the Methods ask, but at Pconn 0.4 the stimulus raises the excitatory
rate to 2.78 Hz. The median score of the excitatory neurons above 0.1 is 0.553 at strength 200
and 0.578 at 225 (calibration sweep, Pconn 0.2), and the grand median of the spared excitatory
neurons is 0.546, about 2.3 times the paper's 0.237. A failure here may be a failure of this
reimplementation, not of the paper's model.""")

s = src(94)
for old, new in [
 ("| model-amplification-increases | Reproduced (assumed) | Matched strength 218 at Pconn 0.2, 28.2 at 0.4 (calibration a); reading (c) cannot be met |",
  "| model-amplification-increases | Reproduced (assumed) | Matched strength 218 at Pconn 0.2, 28.2 at 0.4 (calibration a); readings (b) and (c) set no strength at 0.4 |"),
 ("| model-equal-connectivity-ablation-increases | Not reproduced (assumed) | 0.287 -> 0.279 (all neurons); excitatory neurons rise, 0.546 -> 0.562; values outside tolerance |",
  "| model-equal-connectivity-ablation-increases | Not reproduced (assumed); partially reproduced proposed | Excitatory neurons rise, 0.546 -> 0.562, p = 1.9e-09; values outside tolerance; all neurons fall, 0.287 -> 0.279 |"),
 ("| model-increased-connectivity-ablation-decreases | Partially reproduced (assumed) | 0.282 -> 0.096, p < 0.001; values outside tolerance |",
  "| model-increased-connectivity-ablation-decreases | Partially reproduced (assumed) | 0.356 -> 0.231 (excitatory), p < 0.001; values outside tolerance |"),
 ("| model-more-ablation-larger-decline | Partially reproduced (assumed) | Decline grows with size; R = -0.726 / -0.558, outside -0.65 ± 0.065 |",
  "| model-more-ablation-larger-decline | Partially reproduced (assumed); reproduced proposed | Decline grows with size; R = -0.590 with the 0-ablation networks (excitatory), within -0.65 ± 0.065; all neurons -0.726 / -0.558 |"),
 ("| model-slow-input-sensitive | Partially reproduced (assumed) | 0.269 -> 0.088 at Pconn 0.4, no change at 0.2; values outside tolerance |",
  "| model-slow-input-sensitive | Partially reproduced (assumed) | 0.314 -> 0.104 at Pconn 0.4 (excitatory), no decline at 0.2; pre value outside tolerance |"),
 ("| model-response-similarity | Not reproduced (assumed) | Slopes positive at Pconn 0.4 (p = 0.0014) |",
  "| model-response-similarity | Not reproduced (assumed) | Excitatory: slopes negative at Pconn 0.2 (p = 1.9e-09), none at 0.4 (p = 0.2); all neurons: positive at 0.4 |"),
 ("The Methods cylinder (|dz| < 30 um) is the main reading and the code's signed rule\na variant; outcomes are the same under both.",
  "The Methods cylinder (|dz| < 30 um) is the main reading and the code's signed rule\na variant; outcomes are the same under both except per-mouse-table (23 of 24 rows match under the\nMethods cylinder, 24 of 24 under the code's rule)."),
 ("inhibitory PSPs, the stimulus amplitude and the counted population chosen as stated in its\nsection; its outcomes rest on those choices.",
  "inhibitory PSPs, the stimulus amplitude and the counted population (excitatory neurons) chosen\nas stated in its section; its outcomes rest on those choices. Two model outcomes have a change\nproposed for a further verification round, as the counted population was revised after the\nsecond round."),
 ("neuron counts, ablated counts and per-ablation score changes equal Extended Data Table 1.",
  "neuron counts and ablated counts equal Extended Data Table 1 in all 24 rows, and the\nper-ablation score changes match it within 0.005 in 23 of 24 rows under the Methods cylinder\n(several differ by 0.001 to 0.002; all 24 match with the code's cylinder)."),
]:
    assert old in s, old[:50]; s = s.replace(old, new)
setsrc(94, s)
json.dump(nb, open(F, 'w'), indent=1, ensure_ascii=False)
PYEOF
python $TMPDIR/edit2.py && git -C  diff --stat
```

```
entries/peron-2020/reproduce_peron_2020.ipynb | 228 +++++++++++++++-----------
 1 file changed, 134 insertions(+), 94 deletions(-)
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/peron-2020 2>&1 | tail -30; date -u
```

```
Sun Nov 15 01:13:42 UTC 2026
Installed kernelspec registry-peron-2020 in executed/peron-2020/.venv/share/jupyter/kernels/registry-peron-2020
0 error(s)
pass  reproduce_peron_2020.ipynb  (2346 s)
Sun Nov 15 01:53:03 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/peron-2020/reproduce_peron_2020.ipynb'))
for i in [1]+list(range(72,92)):
    c=nb['cells'][i]
    if c['cell_type']!='code': continue
    print(f"=== {i}")
    for o in c.get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[:6000])
        if o.get('output_type')=='error': print(o['ename'], o['evalue'])
EOF
```

```
=== 1
CRCNS ssc-11, version unversioned (doi:10.6080/K0Z31WWG)
streamed 16 archives in 1052 s
an250220.tar.gz  md5 485e8eff7dcd90d773c5cb8735452295   9.68 GB  read  9.68 GB in  293 s, reconnections 0, errors 0
an257218.tar.gz  md5 966d79a04169a6b714c2ce3f6f414156   4.94 GB  read  4.94 GB in  155 s, reconnections 0, errors 0
an257220.tar.gz  md5 baac8233000d77db40423dfce0366e5f   2.69 GB  read  2.69 GB in   86 s, reconnections 0, errors 0
an258836.tar.gz  md5 cf76b797f5ad3815e660bb8ae84c8efb   8.38 GB  read  8.38 GB in  260 s, reconnections 0, errors 0
an271211.tar.gz  md5 d184f2804f815ada357da0b7268cd613  11.81 GB  read 11.81 GB in  557 s, reconnections 0, errors 0
an272761.tar.gz  md5 46bac15b704c04375a6f338a7746a58a   2.86 GB  read  2.86 GB in  110 s, reconnections 0, errors 0
an274424.tar.gz  md5 42a603f246ea67a22403feff9c70fd10   3.68 GB  read  3.68 GB in  142 s, reconnections 0, errors 0
an274577.tar.gz  md5 8b5fb408a172294ad0d6e06d107a32d1   7.06 GB  read  7.06 GB in  418 s, reconnections 0, errors 0
an275798.tar.gz  md5 c1f15d73c9d30f266d5bea89197c898f  11.04 GB  read 11.04 GB in  345 s, reconnections 0, errors 0
an275801.tar.gz  md5 783986e5a323a1d7c265669ec23bfba0  11.88 GB  read 11.88 GB in  345 s, reconnections 0, errors 0
an276013.tar.gz  md5 f38b3825ed1539435046a83dc42a6f22   8.55 GB  read  8.55 GB in  252 s, reconnections 0, errors 0
an278288.tar.gz  md5 3854befded92d6fb30dce1b7817c9449   8.18 GB  read  8.18 GB in  241 s, reconnections 0, errors 0
an278759.tar.gz  md5 c8c8ae66d85b2161e3c7597fb4f5a6e0   4.79 GB  read  4.79 GB in  141 s, reconnections 0, errors 0
an278937.tar.gz  md5 d63a40e4386ba34127c7d6164f1427aa   8.27 GB  read  8.27 GB in  226 s, reconnections 0, errors 0
an278939.tar.gz  md5 1374085c2466dff3e8f9d2617d299dbe   9.56 GB  read  9.56 GB in  267 s, reconnections 0, errors 0
an281915.tar.gz  md5 7a90f6b602691490abc56dcd0505136b   7.50 GB  read  7.50 GB in  312 s, reconnections 0, errors 0

[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "executed" tools/entry.py | head -30; git status --short
```

```
8:    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies
27:directory. The executed copies
28:go to --output-dir (default: executed/<name>/, which git ignores). A notebook
30:A run that passes leaves a stamp beside the executed copies (.clean-run.json):
31:a hash of everything the run read (`hash` prints it) and of each executed
36:(docs/protocol.md): the executed notebooks with the conclusions removed (every
39:executed/<name>/handover/. Run the entry first.
65:STAMP = ".clean-run.json"                 # beside the executed copies: what they were made from (entry_hash)
67:REUSE_DAYS = 30                           # executed copies older than this are made again
457:    """The text each claim-tagged cell of an executed notebook printed, by tag."""
474:    `before` (its executed notebooks). The entry moves to the new version only when nothing differs; otherwise
489:            differ.append(f"{nb['path']}: no earlier executed copy in {before} to compare with")
526:    """The stamp of executed copies that a run now would only make again: made from this hash, each copy still as
550:        print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
551:              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
620:        executed = output_dir / notebook["path"]
621:        if not executed.is_file():
622:            print(f"error: no executed copy of {notebook['path']} in {output_dir}; run the entry first",
625:        nb = strip_conclusions(nbformat.read(executed, as_version=4))
648:    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 20,40p tools/entry.py; sed -n 500,560p tools/entry.py
```

```
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
- each notebook has a cell tagged `sanity` that prints what was loaded;
- no notebook or helper embeds a large literal array or an encoded image, or
  reads a figure from somewhere else.

`run` builds a fresh virtual environment from the lock file and executes each
notebook through a Jupyter kernel installed in that environment, in the entry
directory. The executed copies
go to --output-dir (default: executed/<name>/, which git ignores). A notebook
that takes longer than --max-minutes fails, even if it ran without error.
A run that passes leaves a stamp beside the executed copies (.clean-run.json):
a hash of everything the run read (`hash` prints it) and of each executed
copy. `run` asked again with nothing changed since reuses those copies and says
so, without executing anything; --fresh executes all the same.

`handover` builds what a verifier is given in its first round
(docs/protocol.md): the executed notebooks with the conclusions removed (every
markdown cell that begins "**Result:" and everything from the "## Summary"
heading on), the helper modules and the claims files, in
executed/<name>/handover/. Run the entry first.
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/peron-2020/reproduce_peron_2020.ipynb'))
for i in [19,24,54,69]:
    for o in nb['cells'][i].get('outputs',[]):
        if 'text' in o: print(i, ''.join(o['text'])[:700])
EOF
```

```
19 touch    ablated per mouse [50, 9, 15, 15, 11, 17, 14, 11, 9]: mean 16.78, s.d. 12.77, mean/287 = 5.85%
whisking ablated per mouse [12, 13, 8, 11, 25, 9, 11]: mean 12.71, s.d. 5.68, mean/287 = 4.43%
silent   ablated per mouse [20, 16, 16, 15, 20, 14, 13, 16]: mean 16.25, s.d. 2.55, mean/287 = 5.66%
synthetic: code rule [np.float64(0.51), 0.01] rank rule [np.float64(0.5), np.float64(1.0)]
touch percentile: rank rule (criterion) mean 79.3, s.d. 27.1 (n = 145); code rule mean 70.3, s.d. 35.0 (n = 151); ablated neurons scoring above every included neuron 9, with a NaN score 6, of 151

19 whisking, Methods (Rwhisking among whisking neurons) percentile: rank rule (criterion) mean 75.4, s.d. 31.8 (n = 89); code rule mean 68.8, s.d. 36.2 (n = 89); ablated neurons scoring above every included neuron 6, with a NaN score 0, of 89
whisking, code (Rwhisking among touch neurons' Rtouch) percentile: rank rule (criterion) mean 75.8, s.d. 30.2 (n = 89); code rule mean 65.9, s.d. 36.5 (n = 89); ablated neurons scoring above every included neuron 9, with a NaN score 0, of 89
touch per mouse percentile (rank rule): {'250220': np.float64(71.5), '257220': np.float64(92.8), '258836': np.float64(72.8), '271211': np.float64(89.0), '281915': np.float64(79.6), '274424': np.float64(75.3), '272761':
24 [methods cylinder] touch ablation, Rtouch: grand median 0.123 -> 0.100 (adjusted MAD 0.011, 0.016); neurons 7121; signed-rank p = 0.004; median change -0.0287, mice with a decline 9 of 9

24 [code cylinder] touch ablation, Rtouch: grand median 0.123 -> 0.100 (adjusted MAD 0.011, 0.016); neurons 7089; signed-rank p = 0.004; median change -0.0285, mice with a decline 9 of 9
 mouse    pre   post  change    n  n_a_pre  n_a_post  n_adrop_pre  n_adrop_post  n_b_pre  n_b_post  score_ablated
250220 0.1501 0.0283 -0.1218  881     1244       824         1208           818      749       450        12.1935
257220 0.1158 0.1107 -0.0051  390      613       532          604           527      316       266 
[... 10 more lines not kept]
```

**Agent**

Now final text edits to the notebook and README before the final run.

**Agent calls Bash**

```bash
cd entries/peron-2020; cat > $TMPDIR/edit3.py <<'PYEOF'
import json
F = 'reproduce_peron_2020.ipynb'
nb = json.load(open(F))
def src(i): return ''.join(nb['cells'][i]['source'])
def setsrc(i, s):
    lines = s.split('\n'); nb['cells'][i]['source'] = [l + '\n' for l in lines[:-1]] + [lines[-1]]
def rep(i, old, new):
    s = src(i); assert old in s, (i, old[:60]); setsrc(i, s.replace(old, new))
rep(0, "takes about 11 minutes.", "takes 11 to 18 minutes, depending on the connection (648 s in one run and 1,052 s in\nanother; the time of this run is printed below).")
rep(78, """whole sweep), because about half of the model's excitatory neurons score exactly 0 (no spike
near a stimulus) while in vivo almost none does.""", """whole sweep, 0.514 to 0.582), because 0.66 to 0.75 of the model's excitatory neurons score
exactly 0 at every strength while no in vivo neuron does (fraction 0.000).""")
rep(78, "(0.514 to 0.579 over the\nwhole sweep, 0.514 to 0.582)", "(over the\nwhole sweep, 0.514 to 0.582)")
json.dump(nb, open(F, 'w'), indent=1, ensure_ascii=False)
PYEOF
python $TMPDIR/edit3.py; python -c "
import json;nb=json.load(open('reproduce_peron_2020.ipynb'));print(''.join(nb['cells'][78]['source']))"
```

```
**Result: reproduced, resting on assumptions.** Under calibration (a) the matched strength is
218.0 at Pconn 0.2 and 28.2 at 0.4, so normalized amplification at 0.4 is 7.74, and the strength
at 0.4 is below that at 0.2. Reading (a) is weakly set at Pconn 0.2: the fraction above 0.1 moves
only from 0.106 to 0.109 between strengths 200 and 225, with two networks per strength, which
bears on how large the amplification is, not on its direction. Reading (b) sets no strength at
Pconn 0.4: with the sweep extended down to no input, the smallest KS distance for the touch input
is at strength 0 (0.514), and the distance hardly depends on the input (over the
whole sweep, 0.514 to 0.582), because 0.66 to 0.75 of the model's excitatory neurons score
exactly 0 at every strength while no in vivo neuron does (fraction 0.000). At Pconn 0.2 its minimum is at 75 (0.468, with
0.469 and 0.470 at 100 and 125). Reading (c), the fraction 0.17, cannot be met: the largest
fraction of excitatory neurons above 0.1 in any sweep is 0.119, as nearly only the 200
input-recipient neurons (11.8% of the excitatory population) reach it. The claim holds under the
one reading that sets both strengths. Amplification here is far larger than the paper's Fig. 1c.
```

**Agent calls Bash**

```bash
cd entries/peron-2020; python - <<'EOF'
import json
F='reproduce_peron_2020.ipynb'
nb=json.load(open(F))
s=''.join(nb['cells'][78]['source'])
s=s.replace("while no in vivo neuron does (fraction 0.000).","while almost no in vivo neuron\ndoes (fraction 0.000 to three decimals).")
lines=s.split('\n'); nb['cells'][78]['source']=[l+'\n' for l in lines[:-1]]+[lines[-1]]
json.dump(nb, open(F,'w'), indent=1, ensure_ascii=False)
EOF
sed -n 60,200p README.md
```

```
(Bash completed with no output)
```

**Agent**

Now the README.

**Agent calls Bash**

```bash
cd entries/peron-2020; python - <<'EOF'
F='README.md'
s=open(F).read()
for old,new in [
("The notebook streams the 16 archives (128 GB) from the public CRCNS bucket once, in\nabout 17 minutes, and reduces them in memory.",
 "The notebook streams the 16 archives (120.9 GB compressed) from the public CRCNS bucket once,\nin 11 to 18 minutes depending on the connection, and reduces them in memory."),
("per condition, in about 30 minutes.", "per condition, in about 21 minutes."),
("| Model: ablation raises scores at equal connectivity | Not reproduced (resting on assumptions) |",
 "| Model: ablation raises scores at equal connectivity | Not reproduced (resting on assumptions); partially reproduced proposed for a third verification round |"),
("| Model: larger ablations, larger declines | Partially reproduced (resting on assumptions) |",
 "| Model: larger ablations, larger declines | Partially reproduced (resting on assumptions); reproduced proposed for a third verification round |"),
]:
    assert old in s, old[:40]; s=s.replace(old,new)
open(F,'w').write(s)
EOF
git -C  diff README.md | head; grep -n "model\|Model" README.md | head
```

```
8:in 11 to 18 minutes depending on the connection, and reduces them in memory. It then rebuilds the network model of the Methods
9:(2,000 leaky integrate-and-fire neurons, helper `peron2020_model.py`) and simulates 30 networks
14:| Model: amplification grows with subnetwork connectivity | Reproduced (resting on assumptions) |
15:| Model: ablation raises scores at equal connectivity | Not reproduced (resting on assumptions); partially reproduced proposed for a third verification round |
16:| Model: ablation lowers scores at increased connectivity | Partially reproduced (resting on assumptions) |
17:| Model: all-or-none networks robust to ablation | Blocked: the Methods' input rule gives no positive strength here |
18:| Model: larger ablations, larger declines | Partially reproduced (resting on assumptions); reproduced proposed for a third verification round |
19:| Model: slow input also sensitive at increased connectivity | Partially reproduced (resting on assumptions) |
20:| Model: decline follows response similarity | Not reproduced (resting on assumptions) |
```

**Agent calls Bash**

```bash
cd entries/peron-2020; grep -n -i "inhibitory ones\|all neurons\|KS\|Kolmogorov\|reading (b)" peron2020_model.py peron2020.py | head; sed -n 1,30p README.md | sed -n 1,12p
```

```
peron2020_model.py:4:regenerated here (claims file, model claims, ``data: elsewhere``). Several networks are
peron2020_model.py:100:    """K independent networks, simulated together."""
peron2020_model.py:344:    encoders by pre-ablation score), for a batch of networks. The pre and post runs of a
peron2020.py:13:  properties, and a touch-triggered population dF/F used to check the clocks.
peron2020.py:51:CHECKSUMS = "https://crcnsarchive.s3-us-west-2.amazonaws.com/ssc-11/live/checksums.md5"
peron2020.py:110:def checksums():
peron2020.py:111:    txt = requests.get(CHECKSUMS, timeout=60).text
# Peron et al. (2020) from CRCNS ssc-11

Tests the findings of [Peron et al. (2020)](https://doi.org/10.1038/s41586-020-2062-x),
"Recurrent interactions in local cortical circuits", that can be tested on
[CRCNS ssc-11](https://doi.org/10.6080/K0Z31WWG): volumetric calcium imaging of L2/3 of mouse
barrel cortex in 16 mice before and after 24 targeted ablations of touch, whisking or silent
neurons. The notebook streams the 16 archives (120.9 GB compressed) from the public CRCNS bucket once,
in 11 to 18 minutes depending on the connection, and reduces them in memory. It then rebuilds the network model of the Methods
(2,000 leaky integrate-and-fire neurons, helper `peron2020_model.py`) and simulates 30 networks
per condition, in about 21 minutes.

| Claim | Outcome |
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/peron-2020 2>&1 | tail -5; date -u
```

```
Sun Nov 15 01:53:53 UTC 2026
Installed kernelspec registry-peron-2020 in executed/peron-2020/.venv/share/jupyter/kernels/registry-peron-2020
0 error(s)
pass  reproduce_peron_2020.ipynb  (2233 s)
Sun Nov 15 02:31:19 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/peron-2020/reproduce_peron_2020.ipynb'))
o=nb['cells'][1]['outputs'][0]['text']; print(''.join(o)[:120])
for i in [74,76,80,85,88,91]:
    t=''.join(''.join(o.get('text','')) for o in nb['cells'][i]['outputs'])
    import re
    print(i, [l for l in t.split('\n') if 'Pconn' in l and ('(b)' in l or 'grand median' in l or 'neurons;' in l)][:8] if i!=85 else t[:900])
EOF
```

```
CRCNS ssc-11, version unversioned (doi:10.6080/K0Z31WWG)
streamed 16 archives in 949 s
an250220.tar.gz  md5 485e8eff7dcd
74 ['Pconn 0.2, peak 10 ms: (a) 218.0; (b) 75.0 (smallest KS 0.468 at strength 75; next smallest 0.469); (c) nan (largest fraction reached 0.119)', 'Pconn 0.2, peak 50 ms: (a) 87.3; (b) 70.0 (smallest KS 0.442 at strength 70; next smallest 0.444); (c) nan (largest fraction reached 0.117)', 'Pconn 0.4, peak 10 ms: (a) 28.2; (b) nan (smallest KS 0.514 at strength 0; next smallest 0.522); (c) nan (largest fraction reached 0.116)', 'Pconn 0.4, peak 50 ms: (a) 6.6; (b) nan (smallest KS 0.510 at strength 0; next smallest 0.519); (c) nan (largest fraction reached 0.118)', '  reading (b): strength 75.0 at Pconn 0.2 and nan at 0.4; amplification at 0.4 = nan; strength at 0.4 below that at 0.2: not set']
76 []
80 ['reading (a), Pconn 0.2, touch input, 20 ablated, excitatory only (main): grand median 0.546 -> 0.562 (adjusted MAD 0.012, 0.011); signed-rank p = 1.9e-09; networks with an increase 30 of 30; neurons per network 166 (range 156 to 170)', 'reading (a), Pconn 0.2, touch input, 20 ablated, all neurons (variant): grand median 0.287 -> 0.279 (adjusted MAD 0.016, 0.015); signed-rank p = 6.3e-05; networks with an increase 4 of 30; neurons per network 415 (range 399 to 446)', 'reading (a), Pconn 0.4, touch input, 20 ablated, excitatory only (main): grand median 0.356 -> 0.231 (adjusted MAD 0.065, 0.177); signed-rank p = 3.9e-07; networks with an increase 4 of 30; neurons per network 166 (range 105 to 187)', 'reading (a), Pconn 0.4, touch input, 20 ablated, all neurons (variant): grand median 0.282 -> 0.096 (adjusted MAD 0.080, 0.084); signed-rank p = 1.9e-08; networks with an increase 2 of 30; neurons per network 382 (range 139 to 454)']
85 reading (a), excitatory only (main), with the 0-ablation networks: R = -0.590, p = 1.3e-12, n = 120
reading (a), excitatory only (main), without them: R = -0.456, p = 6.3e-06, n = 90
   median change by size {0: 0.0, 10
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
s=open('attempts/peron-2020-01.yaml').read()
d=yaml.safe_load(s)
for w in [100,105,110]:
    o=yaml.safe_dump(d, sort_keys=False, allow_unicode=True, width=w)
    import difflib
    n=sum(1 for l in difflib.unified_diff(s.splitlines(),o.splitlines(),lineterm='',n=0) if l.startswith(('+','-')))
    print(w,n)
EOF
```

```
100 0
105 997
110 1093
```

**Agent calls Bash**

```bash
cd  sed -n 1,200p transcripts/peron-2020/verifier-1-report.md | grep -n -i "blocked\|allowed" | head; ls transcripts/peron-2020/
```

```
5:| model-amplification-increases | blocked (other: not attempted) | Nothing was run; cell 0 says only "network simulations… blocked". The claims file sets `data: elsewhere` and gives a criterion that can be run (see B1). |
6:| model-equal-connectivity-ablation-increases | blocked (other) | As above. |
7:| model-increased-connectivity-ablation-decreases | blocked (other) | As above. |
8:| model-all-or-none-robust | blocked (other) | As above. |
9:| model-more-ablation-larger-decline | blocked (other) | As above. |
10:| model-slow-input-sensitive | blocked (other) | As above. |
11:| model-response-similarity | blocked (other) | As above. |
34:| glial-reaction-local | blocked (data_missing) | Confirmed against the archive: filelist.txt and the S3 listing hold only the 16 `an*.tar.gz`, docs and checksums. The members listed in cell 4 are session, log and curation `.mat` files, with no histology. |
39:1. **[affects a conclusion]** Cell 0: the seven model claims are marked blocked without one of the allowed reasons. The Methods give every LIF parameter (τ, ΔV ± 50%, τexc/τinh, tref, delays, connection probabilities, PSPs, input waveform, background rates, dt, 20 s runs). The claims file supplies readings for the parameters the paper leaves open (input strength under readings a–c, reset pulse, slow-input strength). The simulations could have been run; the scale is about 30 networks × a few conditions.
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec.py <<'PYEOF'
import yaml
F = 'attempts/peron-2020-01.yaml'
d = yaml.safe_load(open(F))
O = {o['claim']: o for o in d['outcomes']}

OLD_CAL = ("Assumption. The input strength is the peak current of the beta(3,5) waveform. It is set by the claims "
           "file's readings from sweeps of two networks per strength; reading (a) is adopted where the readings differ, "
           "as reading (b)'s KS minimum lies at the weakest strength of both touch-input sweeps (the distance grows with "
           "strength) and reading (c), 17%, cannot be reached (largest fraction 0.119, as almost only the 200 input-recipient "
           "neurons pass 0.1).")
NEW_CAL = ("Assumption. The input strength is the peak current of the beta(3,5) waveform. It is set by the claims "
           "file's readings from sweeps of two networks per strength, each sweep starting at no input. Only reading (a) "
           "sets both matched strengths (218.0 at Pconn 0.2, 28.2 at 0.4). Reading (b) is set only where its smallest KS "
           "distance lies at a positive strength inside the sweep; at Pconn 0.4 it lies at no input (0.514 for the touch "
           "input, 0.510 for the slow input), as 0.66 to 0.75 of the model's excitatory neurons score exactly 0 at every "
           "strength. Reading (c), 17%, cannot be reached (largest fraction 0.119, as almost only the 200 input-recipient "
           "neurons pass 0.1).")
OLD_POP = ("Assumption. \"All neurons that met the 0.1 encoding score criteria\" (Methods) is taken as all neurons of the "
           "network, inhibitory ones included; excitatory neurons alone are shown as a variant.")
NEW_POP = ("Assumption, revised after verification round 2. \"All neurons that met the 0.1 encoding score criteria\" "
           "(Methods) is taken as the excitatory neurons. The Methods calibrate the input on the \"distributions of "
           "excitatory neuron encoding scores\", ablate \"The 20 excitatory neurons with the highest encoding score\", and "
           "the in vivo data the model stands for are of excitatory neurons (Ai162 x Slc17a7-IRES2-cre mice, and "
           "Emx1-IRES-cre mice whose mCherry marks only excitatory nuclei; Methods, Mice). The paper's Fig. 3b counts "
           "(3,466 and 3,779 neurons above 0.25) are also nearer the excitatory counts here (4,058 and 4,327) than those of "
           "all neurons (7,078 and 7,815). All neurons, inhibitory ones included, are shown as a variant; the outcomes "
           "verified in round 2 were set with all neurons counted.")
for c, o in O.items():
    if not c.startswith('model-'):
        continue
    dv = o['deviations']
    assert OLD_CAL in dv and OLD_POP in dv, c
    o['deviations'] = [NEW_CAL if x == OLD_CAL else NEW_POP if x == OLD_POP else x for x in dv]

o = O['model-amplification-increases']
o['notes'] = ("Under calibration reading (a) the matched input strength is 218.0 at Pconn 0.2 and 28.2 at Pconn 0.4, so "
    "normalized amplification at 0.4 is 7.74, and the strength at 0.4 is below that at 0.2. Reading (a) is weakly set "
    "at Pconn 0.2 (the fraction above 0.1 moves from 0.106 to 0.109 between strengths 200 and 225, two networks per "
    "strength), which bears on the size of the amplification, not its direction. With the sweeps extended down to no "
    "input, reading (b) sets 75.0 at Pconn 0.2 and no strength at 0.4, where the smallest KS distance is at no input "
    "(0.514; 0.522 at the next strength). Reading (c), a fraction of 0.17 excitatory neurons above 0.1, cannot be met "
    "(largest fraction over all sweeps 0.119, below the input-recipient share of 200 of 1,700). The criterion's "
    "condition holds under the one reading that sets both strengths. Amplification is far larger than in the paper's "
    "Fig. 1c. The outcome rests on the assumptions of the model (deviations).")

o = O['model-equal-connectivity-ablation-increases']
o['measured'] = [0.546, 0.562]
o['notes'] = ("At Pconn 0.2 under calibration (a), 30 networks, the spared excitatory neurons (above 0.1 before or "
    "after, ablated ones left out) go from a grand median of 0.546 to 0.562 after the 20 strongest encoders are ablated "
    "(signed-rank p = 1.9e-09, 30 of 30 networks increase), the claimed increase at p < 0.001, with both values far "
    "outside 0.237 ± 0.024 and 0.274 ± 0.027. All neurons (variant) go from 0.287 to 0.279 (p = 6.3e-05, 4 of 30 "
    "increase), a decrease. The verified outcome, not reproduced, was set with all neurons counted; the population was "
    "revised after round 2, and the change of outcome is proposed. Calibration (b) sets no strength at Pconn 0.4 and is "
    "not run.")
o['proposed'] = {'outcome': 'partially_reproduced', 'reason': (
    "The verifier (round 2) found the all-neuron count contestable, and the revision adopts excitatory neurons, as the "
    "Methods calibrate and ablate excitatory neurons, the in vivo data are of excitatory neurons, and the paper's Fig. 3b "
    "neuron counts are nearer the excitatory counts. With them the scores rise in 30 of 30 networks (0.546 to 0.562, p "
    "= 1.9e-09), the effect the claim states, while both grand medians are outside tolerance; the effect is present and "
    "the values are not, the rule the record applies to the Pconn 0.4 claim (notebook, model-equal-connectivity cell).")}

o = O['model-increased-connectivity-ablation-decreases']
o['measured'] = [0.356, 0.231]
o['notes'] = ("At Pconn 0.4 under calibration (a), ablation lowers the spared neurons' scores in both populations over "
    "30 networks: 0.356 to 0.231 for excitatory neurons (p = 3.9e-07, 4 of 30 increase) and 0.282 to 0.096 for all "
    "neurons (variant, p = 1.9e-08). Neither gives both grand medians within 0.243 ± 0.024 and 0.143 ± 0.014, so the "
    "effect is present and the values are not. Calibration (b) sets no strength at Pconn 0.4.")

o = O['model-all-or-none-robust']
o['notes'] = ("Not run. The criterion sets the input at Pconn 0.44 to twice the strength extrapolated linearly from "
    "the two matched strengths (Methods). The extrapolation gives -9.8 under calibration (a), and readings (b) and (c) "
    "set no strength at Pconn 0.4, so the Methods' rule gives no positive input here. The negative value follows from "
    "this attempt's calibration, whose amplification at Pconn 0.4 (7.7) is far above the paper's Fig. 1c. The Methods "
    "give neither the matched strengths nor the strength and length of the reset pulse to the inhibitory population, "
    "and the pulse 300 ms after each onset falls on the next onset at the 300 ms interval of the claims file. Any input "
    "and pulse chosen in their place would be arbitrary.")

o = O['model-more-ablation-larger-decline']
o['measured'] = [-0.59]
o['notes'] = ("Pconn 0.4, calibration (a), 30 networks per size. For the excitatory neurons the median change falls "
    "with each larger ablation (0, -0.026, -0.123 and -0.209 for 0, 10, 20 and 50 ablated). The change correlates with "
    "the net score ablated, R = -0.590 with the 0-ablation networks (p = 1.3e-12, n = 120), within -0.65 ± 0.065, and "
    "R = -0.456 without them (p = 6.3e-06, n = 90). All neurons (variant) give -0.726 and -0.558, both outside the "
    "tolerance. Calibration (b), which in the earlier revision gave -0.774 and -0.678 at strengths at the bottom of its "
    "sweep, sets no strength at Pconn 0.4 once the sweep reaches no input, and is not run. The verified outcome, "
    "partially reproduced, was set with all neurons counted; the change of outcome is proposed.")
o['proposed'] = {'outcome': 'reproduced', 'reason': (
    "With the population revised to excitatory neurons (see model-equal-connectivity-ablation-increases), the "
    "criterion is met under calibration (a), the only calibration that sets both strengths once the sweeps reach no "
    "input; R = -0.590 with the 0-ablation networks (p = 1.3e-12), within -0.65 ± 0.065, and the median change is more "
    "negative at each larger size (0, -0.026, -0.123, -0.209). The margin is small (the bound is -0.585) "
    "(notebook, model-more-ablation-larger-decline cell).")}

o = O['model-slow-input-sensitive']
o['measured'] = [0.314, 0.104]
o['notes'] = ("With the slow-input strength set anew under calibration (a) (reading (b) of the criterion; 6.6 at Pconn "
    "0.4, 87.3 at 0.2), the score of the excitatory neurons falls at Pconn 0.4 from 0.314 to 0.104 (p = 3.9e-07, 3 of "
    "30 networks increase), the post value within 0.104 ± 0.010 and the pre value outside 0.143 ± 0.014, and rises at "
    "Pconn 0.2 (0.803 to 0.850, p = 1.9e-09), so it is not degraded there. With the touch strength (reading (a)) it "
    "does not fall at Pconn 0.4 (0.952 to 0.947, p = 0.16). All neurons (variant) give 0.269 to 0.088 at Pconn 0.4 and "
    "0.424 to 0.424 at 0.2 (p = 0.21) with the strength set anew. Calibration (b) sets no slow-input strength at Pconn "
    "0.4 (smallest KS distance at no input). No reading gives both grand medians within tolerance.")

o = O['model-response-similarity']
o['notes'] = ("Neurons above 0.25 before or after, a line per network through the change in score against the "
    "similarity to the mean rate of the 20 ablated neurons. Under calibration (a), excitatory neurons, the slopes are "
    "negative at Pconn 0.2 (30 of 30, sign test p = 1.9e-09) and show no dependence at Pconn 0.4 (11 of 30 negative, p "
    "= 0.2), the reverse of the claim, which has negative slopes at 0.4 and none at 0.2. All neurons (variant) give "
    "positive slopes at Pconn 0.4 (6 of 30 negative, p = 0.0014) and mostly positive ones at 0.2 (8 of 30, p = 0.016). "
    "The bin-mean fit leans the same way. The excitatory counts (4,058 at Pconn 0.4 and 4,327 at 0.2) are nearer the "
    "paper's 3,466 and 3,779 than those of all neurons (7,078 and 7,815).")

o = O['silent-ablation-size']
old = "the targeting rule was applied by the authors on the data at hand on the day."
assert old in o['notes']
o['notes'] = o['notes'].replace(old, "the paper gives the 0.025 Hz rule for choosing targets, and 12 of the 130 are above it in these pre-ablation data.")

o = O['response-similarity-touch-ablation']
old = ("with it, 8 of 9 touch slopes are negative (p = 0.039) with 2,768 neurons in bins (code cylinder) and the whisking "
       "slopes give p = 0.508 with 1,085 neurons, exactly the paper's values, with the point fit or the bin-mean fit.")
assert old in o['notes'], o['notes']
o['notes'] = o['notes'].replace(old, (
    "with it and the code's cylinder, the bin-mean fit gives 8 of 9 touch slopes negative (p = 0.039) with 2,768 neurons "
    "in bins and whisking slopes with p = 0.508 and 1,085 neurons, exactly the paper's values. The point fit with the "
    "same average and cylinder gives the touch result (8 of 9, p = 0.039, 2,824 neurons) but 4 of 9 whisking slopes "
    "negative (p = 1.000)."))

for f in d['findings']:
    s = f['statement']
    if "77 GB of the 128 GB are ablation logs" in s:
        f['statement'] = s.replace("77 GB of the 128 GB are ablation logs.",
            "the 16 archives hold 120.9 GB compressed, and the JRC ablation logs make up 77.1 GB of the 166.7 GB their members hold uncompressed.")
    if "this attempt adopted the code's rule for the table." in s:
        f['statement'] = s.replace("this attempt adopted the code's rule for the table.",
            "this attempt takes the Methods cylinder as the main reading, as the claims file does, and shows the code's rule as a variant.")
    if s.startswith("Question for the authors, on the network model."):
        f['statement'] = s.replace("or the strength and length of the reset pulse at Pconn 0.44.",
            "the strength and length of the reset pulse at Pconn 0.44, or which neurons enter \"all neurons that met the 0.1 encoding score criteria\" (excitatory neurons only, or inhibitory ones too).")
        assert f['statement'] != s
        f['statement'] = f['statement'].replace("took inhibitory PSPs as -1 mV and calibrated", "took inhibitory PSPs as -1 mV, counted excitatory neurons and calibrated")
assert all("77 GB of the 128" not in f['statement'] for f in d['findings'])
assert all("adopted the code's rule for the table" not in f['statement'] for f in d['findings'])
yaml.safe_dump(d, open(F, 'w'), sort_keys=False, allow_unicode=True, width=100)
PYEOF
python $TMPDIR/rec.py && git diff --stat attempts/
```

```
attempts/peron-2020-01.yaml | 298 ++++++++++++++++++++++++++++----------------
 1 file changed, 192 insertions(+), 106 deletions(-)
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/ver.py <<'PYEOF'
import yaml
F = 'attempts/peron-2020-01.yaml'
d = yaml.safe_load(open(F))
OUT = {o['claim']: o['outcome'] for o in d['outcomes']}
same = "The other 21 are unchanged from round 1 and still agree with the printed numbers."
R = {}
def add(c, agrees, reason, response, outcome=None):
    r = {'claim': c, 'agrees': agrees}
    if outcome is None and agrees:
        outcome = OUT[c]
    if outcome:
        r['outcome'] = outcome
    r['reason'] = reason
    r['response'] = response
    R[c] = r

add('model-amplification-increases', True,
    "Agree. Every 0.4 sweep strength (15-50) is below every 0.2 strength (150-400), so the direction does not depend on "
    "the calibration (cell 74). Reading (c) cannot be tested, as 0.17 is more than the input-recipient share of 200/1,700 "
    "= 0.118, so the criterion's \"under each reading\" is met only for (a) and (b). Reading (a) is weakly set at Pconn "
    "0.2 (0.106 to 0.109 between 200 and 225, two networks per point), which affects how large the amplification is, not "
    "its direction; reading (b) is not determined, its KS minimum sitting at the bottom edge of the sweeps.",
    "No change to the outcome. The sweeps now start at no input: reading (b) sets 75.0 at Pconn 0.2 and no strength at "
    "0.4, where the smallest KS distance is at no input, so the claim holds under (a), the one reading that sets both "
    "strengths. The weak setting of (a) at Pconn 0.2 is stated in the result.")
add('model-equal-connectivity-ablation-increases', False,
    "Do not agree as it stands. The outcome depends on the attempt's own choice to count inhibitory neurons (about 250 "
    "of the 415 neurons per network, cell 80). With excitatory neurons only, scores rise in 30 of 30 networks (p = "
    "1.9e-09), the claimed direction, with values outside tolerance; by the record's own rule for the Pconn 0.4 claim, "
    "that is partially reproduced. The printed counts argue against the all-neuron reading. The paper reports 3,466 and "
    "3,779 neurons above 0.25; all neurons give 7,078 and 7,815, about twice that, and excitatory neurons 4,058 and "
    "4,327 (cell 91).",
    "The assumption is revised: excitatory neurons are the counted population (main) and all neurons a variant, as "
    "the Methods calibrate and ablate excitatory neurons, the in vivo data are of excitatory neurons and the paper's "
    "counts are nearer the excitatory ones. The verified outcome is kept, and partially reproduced is proposed under "
    "`proposed` for a third round (0.546 to 0.562, p = 1.9e-09, values outside tolerance).",
    'partially_reproduced')
add('model-increased-connectivity-ablation-decreases', True,
    "Agree. The decline holds under every reading (cell 80) and no reading gives values within tolerance.",
    "No change to the outcome. The notes now lead with the excitatory neurons (0.356 to 0.231, p = 3.9e-07).")
add('model-all-or-none-robust', True,
    "Agree, with a note. The extrapolation gives -9.8 and -12.0 (cell 74). The negative value comes from this attempt's "
    "calibration, an amplification of 7.7 to 10, which is far above the paper's Fig. 1c. The Methods also omit the "
    "matched strengths and the reset pulse, so the reason given is fair.",
    "No change to the outcome. The notes and the result now say that the negative value follows from this attempt's "
    "calibration and that the Methods omit the matched strengths; with reading (b) no longer setting a strength at "
    "Pconn 0.4, only (a)'s -9.8 remains.")
add('model-more-ablation-larger-decline', False,
    "Not settled. The criterion is met under two readings (cell 85). Calibration (b), a claims-file reading, with all "
    "neurons and the 0-ablation networks left out gives R = -0.678 (p = 2e-13), with the decline growing at each size. "
    "Calibration (a) with excitatory neurons and the 0-ablation networks included gives -0.590. The record sets (b) "
    "aside because its KS minimum is the weakest strength tried; that is a reason to extend the sweep, not to drop the "
    "reading.",
    "The sweeps were extended down to no input. At Pconn 0.4 the smallest KS distance is then at no input (0.514 touch, "
    "0.510 slow), so reading (b) sets no strength there and is not run; 0.66 to 0.75 of the model's excitatory neurons "
    "score exactly 0 at every strength, which keeps the distance near 0.5. With the population revised to excitatory "
    "neurons, calibration (a) meets the criterion (R = -0.590, p = 1.3e-12, a larger decline at each size). The "
    "verified outcome is kept, and reproduced is proposed for a third round.")
add('model-slow-input-sensitive', True,
    "Agree. No reading gives both grand medians within tolerance; the closest is (b) set anew at 0.110 to 0.102 (cell "
    "88).",
    "No change to the outcome. With excitatory neurons and the strength set anew, 0.314 to 0.104 at Pconn 0.4 (post "
    "value within tolerance, pre value not) and a rise at 0.2; calibration (b) now sets no slow-input strength at "
    "Pconn 0.4, so its 0.110 to 0.102 is no longer run.")
add('model-response-similarity', True,
    "Agree. It fails under every reading and population (cell 91).",
    "No change to the outcome; the notes now lead with the excitatory neurons.")
specific = {
 'touch-ablation-size': ("Agree; now partially reproduced, which matches my round-1 outcome. Cell 19, rank rule 79.3 ± "
    "27.1. Cell 18 (markdown) still reads \"(1 when none exceeds it)\" for the percentile; cell 19 gives 0.01 for a "
    "score above all 100 neurons, and only the docstring in cell 19 was changed.",
    "Cell 18 now describes both rules: the criterion's rank and the code's rule, which gives 1/N when no included "
    "neuron exceeds the ablated one or its score is NaN. No change to the outcome."),
 'whisking-ablation-size': ("Agree; now partially reproduced, which matches my round-1 outcome. 4.43% of the touch "
    "neurons per barrel column, and percentiles of 75.4 and 75.8.", "No change."),
 'per-mouse-table': ("Agree; now partially reproduced, which matches my round-1 outcome. Cell 69, 23 of 24 rows match "
    "under the Methods cylinder. The summary's \"outcomes are the same under both [cylinders]\" is false for this claim "
    "(23 of 24 rows under one rule, 24 of 24 under the other), and \"per-ablation score changes equal Extended Data "
    "Table 1\" is too strong, as several rows differ by 0.001-0.002. The record's proximity finding, \"this attempt "
    "adopted the code's rule for the table\", contradicts this outcome and cell 70.",
    "The summary now names per-mouse-table as the exception and says the changes match within 0.005 in 23 of 24 rows "
    "(several differ by 0.001 to 0.002); the finding now says the Methods cylinder is the main reading and the code's "
    "rule a variant. No change to the outcome."),
 'silent-ablation-size': ("Agree. " + same + " Cell 20, \"applied by the authors at targeting time, on other data\": no "
    "output supports \"other data\".",
    "Cell 20 and the notes now say only that the paper gives the 0.025 Hz rule for choosing targets and that 12 of the "
    "130 ablated neurons are above it in these pre-ablation data. No change to the outcome."),
 'touch-ablation-reduces-touch': ("Agree. " + same + " Cell 38, \"about half the paper's\", holds only for the touch "
    "ablations; for whisking ablations it is 0.008 / 0.009 against 0.081 / 0.069 (cell 37), about a tenth.",
    "Cell 38 now gives both: about half for the touch ablations and about a tenth for the whisking ablations. No change "
    "to the outcome."),
 'response-similarity-touch-ablation': ("Agree. " + same + " The record's \"exactly the paper's values, with the point "
    "fit or the bin-mean fit\" holds only for the bin-mean fit; in cell 54, with the right-trial average and the code's "
    "cylinder, the point fit gives 4 of 9 whisking slopes negative with p = 1.000, and 2,824 touch neurons, not 2,768.",
    "The notes now say the paper's values come from the bin-mean fit, and give the point fit's 4 of 9 (p = 1.000) and "
    "2,824 neurons. No change to the outcome."),
}
for o in d['outcomes']:
    c = o['claim']
    if c in R:
        continue
    if c in specific:
        add(c, True, *specific[c])
    else:
        add(c, True, "Agree. " + same, "No change.")
results = [R[o['claim']] for o in d['outcomes']]
d['verifications'].append({
    'date': '2026-11-15',
    'kind': 'agent',
    'by': 'Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
    'reviewed': ("Round 2. The full executed notebook of the revision after round 1, with its conclusions and summary, "
        "the helper modules peron2020.py and peron2020_model.py, the claims file and this record, with the paper. It "
        "took its counts from the record (31 claims, 18 reproduced, 6 partially reproduced, 5 not reproduced, 2 "
        "blocked). It agreed with 29 outcomes, disagreed with model-equal-connectivity-ablation-increases and left "
        "model-more-ablation-larger-decline unsettled, found the counted population (inhibitory neurons included) "
        "contestable and calibration (b) undetermined, and quoted sentences the outputs do not support. It noted that "
        "the round-1 entries for the seven model claims (agrees true, outcome blocked) understate its round-1 reason, "
        "that the block had no allowed reason; those entries are left as recorded. It could not check the "
        "transcription of Extended Data Table 1, having no PDF renderer. In reply the counted population was revised, "
        "the calibration sweeps were extended to no input, two changes of outcome are proposed for a third round, and "
        "the quoted sentences were corrected. Report in transcripts/peron-2020/verifier-2-report.md."),
    'results': results})
yaml.safe_dump(d, open(F, 'w'), sort_keys=False, allow_unicode=True, width=100)
PYEOF
python $TMPDIR/ver.py && python tools/entry.py check entries/peron-2020 2>&1 | tail -5
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  git diff | grep "^+" | grep -n -i "—\|rather" | head; git diff --stat; python tools/entry.py check entries/peron-2020 2>&1 | head; date -u
```

```
attempts/peron-2020-01.yaml                   | 523 ++++++++++++++++++++------
 entries/peron-2020/README.md                  |  10 +-
 entries/peron-2020/reproduce_peron_2020.ipynb | 230 ++++++-----
 3 files changed, 558 insertions(+), 205 deletions(-)
0 error(s)
Sun Nov 15 02:33:27 UTC 2026
```

**Agent calls Bash**

```bash
cd  python tools/entry.py run entries/peron-2020 2>&1 | tail -3
```

```
pass  reproduce_peron_2020.ipynb  (2233 s, reused)
reused the executed copies of 2026-11-15 02:31 UTC: nothing the run reads has changed since (hash e071e55521ef). Nothing was executed and no environment was built; --fresh runs it again.
```

**Agent calls Bash**

```bash
cd  grep -n -A8 "proposed:" attempts/peron-2020-01.yaml | head -30
```

```
127:  proposed:
128-    outcome: partially_reproduced
129-    reason: The verifier (round 2) found the all-neuron count contestable, and the revision adopts excitatory
130-      neurons, as the Methods calibrate and ablate excitatory neurons, the in vivo data are of excitatory
131-      neurons, and the paper's Fig. 3b neuron counts are nearer the excitatory counts. With them the scores
132-      rise in 30 of 30 networks (0.546 to 0.562, p = 1.9e-09), the effect the claim states, while both
133-      grand medians are outside tolerance; the effect is present and the values are not, the rule the
134-      record applies to the Pconn 0.4 claim (notebook, model-equal-connectivity cell).
135-- claim: model-increased-connectivity-ablation-decreases
--
261:  proposed:
262-    outcome: reproduced
263-    reason: With the population revised to excitatory neurons (see model-equal-connectivity-ablation-increases),
264-      the criterion is met under calibration (a), the only calibration that sets both strengths once the
265-      sweeps reach no input; R = -0.590 with the 0-ablation networks (p = 1.3e-12), within -0.65 ± 0.065,
266-      and the median change is more negative at each larger size (0, -0.026, -0.123, -0.209). The margin
267-      is small (the bound is -0.585) (notebook, model-more-ablation-larger-decline cell).
268-- claim: model-slow-input-sensitive
269-  outcome: partially_reproduced
```

**Agent**

I've answered every point in the round-2 report and re-run the entry (`python tools/entry.py all entries/peron-2020`: 0 errors, notebook passes in 2,233 s). `entry.py check` passes after the record was updated. Nothing is committed.

**Outcomes.** All 31 verified outcomes stand as they were. I put two changes under `proposed` for a third verification round:
- **model-equal-connectivity-ablation-increases:** not reproduced → partially reproduced proposed. Counting excitatory neurons only, scores rise in 30 of 30 networks (0.546 to 0.562, p = 1.9e-09), the direction the claim states. Both values are outside tolerance.
- **model-more-ablation-larger-decline:** partially reproduced → reproduced proposed. Under calibration (a) with excitatory neurons, R = -0.590 (p = 1.3e-12), and the decline grows at each larger ablation size. That is inside -0.65 ± 0.065, but only just: the bound is -0.585.

**Assumptions revised in reply to the report:**
- **Which neurons are counted.** The main reading is now excitatory neurons, and all neurons are a variant. The verifier pointed to the neuron counts. The Methods also calibrate the input on excitatory scores and ablate excitatory neurons, and the in vivo data the model stands for are excitatory neurons (Methods, Mice). That is why both changes above are proposed.
- **Calibration (b).** The verifier noted that its minimum was never bracketed, so every sweep now starts at no input. At Pconn 0.4 the smallest KS distance is at no input (0.514 for touch input, 0.510 for slow input), so (b) sets no strength there and its runs are gone. The cause is that 66 to 75% of the model's excitatory neurons score exactly 0 at every strength, while almost no in vivo neuron does. That leaves (a) as the only reading that sets both matched strengths. Amplification stays reproduced under (a), and the record says that (a) is only weakly set at Pconn 0.2.

**Sentences corrected (notebook, README, record):**
- The archives are 120.9 GB compressed, not 128 GB. The streaming time is now given as 11 to 18 minutes: this run took 949 s, an earlier one 1,052 s.
- The ablation-log finding now says 77.1 GB of the 166.7 GB uncompressed.
- The percentile description in cell 18 now gives both rules.
- The unsupported "other data" sentence about the silent ablations is gone.
- The MAD comparison now says about half for touch ablations and about a tenth for whisking ablations.
- The summary now names per-mouse-table as the one claim where the two cylinders differ, and says the table's score changes match within 0.005 in 23 of 24 rows.
- The response-similarity note now says the paper's values come from the bin-mean fit only. The point fit gives 4 of 9 whisking slopes negative (p = 1.000) and 2,824 neurons.
- The proximity finding now says the Methods cylinder is the main reading.
- The "about twice the paper's" sentence now says the grand median of 0.546 is 2.3 times the paper's 0.237.
- For model-all-or-none-robust, the record now says the negative extrapolated strength comes from this attempt's calibration.
- The model question for the authors now also asks which neurons are counted.

**Round 2 is recorded under `verifications`**, all 31 claims with the verifier's reasons in its words:
- It agreed with 29 outcomes.
- It disagreed with model-equal-connectivity, giving partially reproduced.
- It left model-more-ablation unsettled and gave no outcome.

**Not done:**
- **No new reader questions.** The report found no new place where the claims file misreads the paper, so `questions/peron-2020.yaml` is unchanged.
- **Round-1 entries left as they are.** The verifier said `agrees: true` understates its round-1 reason for the seven model claims. Its own round-1 outcome there was blocked, the same as the record, so I didn't edit those entries. The round-2 `reviewed` text records its note.
- **Two open points, still stated as before.** The 50 ms burst rule and the check of the Extended Data Table 1 transcription remain open.

## End of run

53 turns, 97 minutes, $3.93 at API prices, result: success.
