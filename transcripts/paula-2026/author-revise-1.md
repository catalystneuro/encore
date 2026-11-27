# paula-2026 · author-revise-1 · run 46015463856

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/paula-2026/verifier-1-report.md; ls entries/paula-2026 entries/paula-2026/*
```

```
Fri Nov 27 14:30:30 UTC 2026
**Verifier report, round 1: de Paula et al. 2026 (doi:10.1103/wndc-k654) on DANDI:000713 0.240702.1725**

The claims file has 38 claims. The notebook tests all 38 and treats none as blocked. My outcomes: 10 reproduced, 6 partially reproduced, 22 not reproduced.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| table1-sample | not_reproduced | 153 sessions under every reading, against 102 (cell 8). With all units, the neuron counts are about 2× Table I. With the quality filter (qc), the window counts match but the populations and neurons do not. |
| fig1c-cv-region-medians | not_reproduced | All units: the medians of DG (0.564) and NB (0.564) fall outside the widened ranges, and the TH, HP and MB extremes miss. qc: the TH maximum (0.414) misses (cell 12). |
| fig1c-cv-above-surrogate | partially_reproduced | Every Mann-Whitney test gives p ≤ 1.5e-73 with empirical higher, and the VIS surrogate medians are 0.225 to 0.243. The HP ratios for POST (1.32) and DG (3.01) fall outside 1.35 to 2.42 under all five seeds (cell 14). This is the claim's partial rule. |
| fig1d-surrogate-abolishes-cv-correlations | not_reproduced | Surrogate \|r\| reaches 0.79 under reading (a) and 0.66 under (b). 115 and 213 pairs exceed 0.2 (cell 16). |
| fig1e-positive-cv-modules | not_reproduced | Reading (a): top value 0.772, above 0.737. Reading (b): low end 0.450, just outside 0.50 ± 0.05. Same-area fractions (66% and 81%) do hold (cell 18). |
| fig1e-dg-ca3-anticorrelation-hubs | not_reproduced | Reading (b): CA3 and DG are the hubs, but the most negative r is −0.178 (expected −0.27 ± 0.027). Reading (a): NB is the hub and the most negative r is −0.496 (cell 20). |
| fig1e-midbrain-weakest-cv-correlations | not_reproduced | Reading (a): MB mean \|r\| (0.186) is above HP (0.179). Reading (b): only 2 of 115 MB pairs are near zero (cell 22). |
| fig2a-vis-cv-by-condition | reproduced | 12/12 medians within tolerance under readings a/a and b/a with all
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
779 docs/protocol.md
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
370:### 2. Check the data against its description
385:### 3. Write the entry
470:### 4. Lock, check and run
490:### 5. Record the attempt
599:### 6. Hand over for verification
637:## Repeat attempts
703:## Local and remote datasets
726:## Verifier
730:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 199,
 "limit": 580
}
```

```
199	## Author
200	
201	The workflow puts the paper under `paper/`, as for the reader. Read it to
202	understand the claims, their data and their figures. The claims file still
203	decides what is tested: do not change a claim's statement, expected values or
204	criterion. A method detail the claims file lacks is taken from the paper
205	(step 6).
206	
207	**Time.** An author run is stopped five hours after it starts, and whatever
208	is not recorded by then is lost. The prompt says when the run started and the
209	time by which to finish. Check the clock (`date -u`) between steps. When that
210	time comes, stop analysing and finish: record each claim not yet tested as
211	blocked, `too_large` where the computation is what stopped it, saying how far
212	it got, then write the attempt record and run the entry's checks. A record
213	with some claims blocked for time is worth more than a run that is cut off.
214	
215	### 1. Establish what can be tested
216	
217	Do this before any analysis.
218	
[... 560 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts/ | grep paula; ls transcripts/paula-2026/ questions/ | grep -i paula; wc -l attempts/paula-2026-01.yaml entries/paula-2026/*; ls executed/paula-2026/ 2>/dev/null; cat entries/paula-2026/entry.yaml
```

```
paula-2026-01.yaml
transcripts/paula-2026/:
   877 attempts/paula-2026-01.yaml
    26 entries/paula-2026/README.md
    23 entries/paula-2026/entry.yaml
   605 entries/paula-2026/paula.py
  2349 entries/paula-2026/reproduce_paula_2026.ipynb
     7 entries/paula-2026/requirements.in
   892 entries/paula-2026/requirements.lock.txt
  4779 total
reproduce_paula_2026.ipynb
result.json
schema_version: 1
name: paula-2026
type: reproduction
title: Statistical complexity of population activity across brain regions (de Paula et al. 2026)
description: Tests the findings of de Paula, Jungmann, Fontenele, Aguiar, Carelli, Matias, Copelli and de
  Vasconcelos (2026) on dandiset 000713, the Allen Institute Visual Behavior Neuropixels dataset. It computes
  the coefficient of variation, permutation entropy and statistical complexity of the population rate of each
  local population in 100-s windows of active behavior, natural images, blank screens and spontaneous activity,
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/paula-2026-01.yaml"
}
```

```
1	schema_version: 3
2	id: paula-2026-01
3	datasets:
4	- archive: dandi
5	  id: '000713'
6	  version: 0.240702.1725
7	  doi: 10.48324/dandi.000713/0.240702.1725
8	  relation: reuses
9	paper: doi:10.1103/wndc-k654
10	date: '2026-11-27'
11	entry: paula-2026
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 858 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/ | grep paula; wc -l claims/paula-2026*; ls paper/; ls questions | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/paula-2026.yaml"
}
```

```
1	# Claims for de Paula, Jungmann, Fontenele, Aguiar, Carelli, Matias, Copelli & de Vasconcelos
2	# (2026), "Revealing Stimulus-Dependent Dynamics Through Statistical Complexity", PRX Life 4,
3	# 023018, doi:10.1103/wndc-k654, tested on DANDI:000713.
4	#
5	# Provenance: written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
6	# Actions"), 2026-11-27, protocol pilot-18 as stated in docs/protocol.md.
7	#
8	# Text read: the version of record (published 22 May 2026, corrected 22 July 2026, the
9	# correction fixing Eq. 9), from paper/10.1103-wndc-k654.txt, which holds the main text
10	# (Methods, Results, figure legends, Table I) and the Supplemental Material (Secs. I to III,
11	# supplementary Figs. 1 to 6, dated April 28, 2026). The PDF pages could not be rendered in
12	# this run, so no figure was read from its image; every value below is from the text and the
13	# legends. The paper links no analysis code: its Data Availability statement cites only the
14	# dataset, and the one URL of the supplement (https://bit.ly/4smMnMj) holds the figures of the
15	# parameter sweep. No code was read.
16	#
17	# Data the paper used (Methods II.A, Results III.A, Table I, legends of Figs. 1 to 5). The
18	# Allen Institute Visual Behavior Neuropixels dataset, cited as DANDI:000713 version
19	# 0.240702.1725 (Ref. 22). Wild-type and transgenic mice, head fixed, recorded with six
20	# Neuropixels 1.0 probes targeting visual cortex. 102 sessions. Measured variables used:
[... 915 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/paula-2026.yaml",
 "offset": 936
}
```

```
936	  source: Results III.D, paragraph 6; Fig. 4f and 4g legends
937	  quote: During active behavior [Fig. 4(f)] and blank screens [Fig. 4(g)], similar patterns
938	    persisted, with visual cortex maintaining distinct complexity distributions from
939	    subcortical structures
940	  depends_on:
941	  - fig4e-js-complexity-natural-images
942	  criterion: Matrices as fig4e. Reproduced when, under one reading, in both conditions most
943	    pairs of a VIS subregion with a TH, HP or MB subregion exceed 0.36 (the legend's 0.4,
944	    widened by 10%), and in active behavior most HP-HP pairs lie in 0.18 to 0.44.
945	
946	- id: fig4h-js-complexity-spontaneous-converges
947	  statement: In spontaneous activity the JS divergences between regions are lower overall, visual
948	    cortex differing less from other regions (JS 0.2 to 0.4) than in visually driven states, and
949	    midbrain divergences stay low in all conditions (below 0.2 within the midbrain group).
950	  source: Results III.D, paragraph 6; Fig. 4h legend
951	  quote: 'Critically, spontaneous activity [Fig. 4(h)] exhibited reduced overall divergences,
952	    with visual cortex showing smaller differences from other regions (JS: 0.2–0.4) compared to
953	    visually driven states ... Midbrain areas showed consistently low divergence across all
954	    conditions (JS <0.2 within MB group)'
955	  depends_on:
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/paula-2026 && python -c "
import json
nb=json.load(open('reproduce_paula_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'),len(src))
    print(src[:300])
"
```

```
<persisted-output>
Output too large (41.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/5df290d5-9df0-4907-b855-07c1c7902ce6/tool-results/bc2u84j1g.txt

Preview (first 2KB):
===== 0 markdown None 3392
# Reproducing de Paula et al. (2026) from DANDI:000713

Paper. E. V. de Paula, R. M. Jungmann, A. J. Fontenele, L. A. A. Aguiar, P. V. Carelli, F. S. Matias, M. Copelli and N. A. P. de Vasconcelos, "Revealing Stimulus-Dependent Dynamics Through Statistical Complexity", PRX Life 4, 023018 (2026), doi
===== 1 code None 556
import os
for v in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ[v] = "1"  # set before numpy loads: the four worker processes each run many small fits
import time, zlib, warnings
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot
===== 2 markdown None 199
## Loading

[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/paula-2026/paula.py"
}
```

```
1	"""Loading and measures for de Paula et al. (2026), PRX Life 4, 023018, on DANDI:000713.
2	
3	The paper analyses the population firing rate of "local populations" (the units of one
4	brain subregion in one session) of the Allen Visual Behavior Neuropixels dataset in 100-s
5	windows of four conditions. This module streams each session's NWB file from the archive
6	(remfile and h5py, nothing written to disk), builds the windows and returns one row per
7	window with every measure the claims use. Sources of each parameter:
8	
9	- Population rate r(t): spike counts of the N units in nonoverlapping 50 ms bins divided by
10	  N times 50 ms (Methods II.B, Eq. 1; nonoverlap from Methods II.C, T = 2000 points per 100 s).
11	- CV: the standard deviation over the mean of r(t) in each nonoverlapping 10-s window, averaged
12	  over the ten (Methods II.B, Eq. 2). A 10-s window with no spike has no CV and is left out of
13	  the mean (a standard choice; it occurs only in near-silent populations).
14	- Bandt and Pompe patterns, D = 6, tau = 1, ties ranked higher for the later element (Methods
15	  II.C: "In cases of equal values (ties), we assigned higher ranks to later-occurring
16	  elements"), done with a stable argsort. H normalised by ln(D!) (Eq. 6). C = Q0 DJS[P, Pe] H
17	  with DJS as in Eq. 9 in natural logs and Q0 the standard MPR constant of Ref. 29 for D!
18	  states (the claims file's reading of "normalization constant").
19	- Surrogate: each neuron's interspike intervals within the window shuffled independently
20	  (Methods II.E); the first spike stays in place (claims file, opening comment; a standard
[... 586 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/paula-2026 && python -c "
import json
nb=json.load(open('reproduce_paula_2026.ipynb'))
for i,c in enumerate(nb['cells'][:12]):
    src=''.join(c['source'])
    print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(src)
"
```

```
Exit code 1
/bin/bash: line 1: cd: entries/paula-2026: No such file or directory
```

**Agent calls Bash**

```bash
python -c "
import json
nb=json.load(open('reproduce_paula_2026.ipynb'))
for i,c in enumerate(nb['cells'][:12]):
    src=''.join(c['source'])
    print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(src)
"
```

```
===== 0 markdown None
# Reproducing de Paula et al. (2026) from DANDI:000713

Paper. E. V. de Paula, R. M. Jungmann, A. J. Fontenele, L. A. A. Aguiar, P. V. Carelli, F. S. Matias, M. Copelli and N. A. P. de Vasconcelos, "Revealing Stimulus-Dependent Dynamics Through Statistical Complexity", PRX Life 4, 023018 (2026), doi:10.1103/wndc-k654.

Dataset. DANDI:000713, "Allen Institute - Visual Behavior - Neuropixels", version 0.240702.1725 (doi:10.48324/dandi.000713/0.240702.1725). This is the version the paper cites (its Ref. 22, as the claims file gives it), and it is the only published version of the dandiset; the draft has the same 4293 assets and was last modified on 2024-07-02, when this version was published. The 153 ecephys session files are streamed from the archive; nothing is written to disk.

Text. The claims file `claims/paula-2026.yaml` was written from the version of record (corrected 22 July 2026) and its Supplemental Material. The paper links no analysis code.

Claims. All 38 claims of the claims file are tested here; none is blocked. Claim `fig3a-reference-systems` uses synthetic series only (`data: elsewhere`, no recordings). The outcomes are in the attempt record and the summary at the end.

| Claim | Tested here |
|---|---|
| table1-sample | tested |
| fig1c-cv-region-medians | tested |
| fig1c-cv-above-surrogate | tested |
| fig1d-surrogate-abolishes-cv-correlations | tested |
| fig1e-positive-cv-modules | tested |
| fig1e-dg-ca3-anticorrelation-hubs | tested |
| fig1e-midbrain-weakest-cv-correlations | tested |
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json
nb=json.load(open('reproduce_paula_2026.ipynb'))
for i,c in enumerate(nb['cells'][12:],12):
    src=''.join(c['source'])
    print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(src)
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt; ls ../../executed/paula-2026/; python -c "
import json;print(json.load(open('../../executed/paula-2026/result.json')))" | head -50
```

```
1063 /tmp/claude-1001/nb.txt
reproduce_paula_2026.ipynb
result.json
{'entry': 'paula-2026', 'python': '3.13', 'results': [{'notebook': 'reproduce_paula_2026.ipynb', 'ok': True, 'seconds': 2175, 'error': None}]}
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	===== 12 markdown None
2	## fig1c-cv-region-medians
3	
4	> During active behavior visual cortex subregions have the highest population CV (medians 0.40 to 0.59), thalamic subregions moderate (0.27 to 0.37), hippocampal subregions high (0.25 to 0.49, dentate gyrus highest at 0.49) and midbrain the lowest (0.16 to 0.45).
5	===== 13 code ['claim:fig1c-cv-region-medians']
6	RANGES_CV = {"VIS": (0.40, 0.59), "TH": (0.27, 0.37), "HP": (0.25, 0.49), "MB": (0.16, 0.45)}
7	IQR_CV = {"VIS": (0.12, 0.18), "TH": (0.10, 0.15), "HP": (0.08, 0.13), "MB": (0.05, 0.23)}
8	
9	def cv_medians(act):
10	    g = act.groupby("region").cv
11	    t = pd.DataFrame({"median": g.median(), "iqr": g.quantile(0.75) - g.quantile(0.25), "windows": g.size()}).reindex(REG_OF(act))
12	    t["area"] = [paula.REGION_AREA[r] for r in t.index]
13	    return t
14	
15	def REG_OF(d):
16	    return [r for r in paula.REGION_ORDER if r in set(d.region)]
17	
18	def judge_fig1c(t, label):
19	    ok_all, ok_iqr = True, True
20	    for a, (lo, hi) in RANGES_CV.items():
[... 541 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 562
}
```

```
562	            r[f"C span {q}"] = tuple(np.round(np.percentile(x.C, [lo, hi]), 3))
563	        if surr:
564	            r["surrogate median C"] = round(x.s_C.median(), 4)
565	            r["empirical median C"] = round(x.C.median(), 4)
566	            for s in SFX:
567	                r["p" + (s or "")] = stats.mannwhitneyu(x.C, x["s_C" + s]).pvalue
568	                r["surr med" + s] = x["s_C" + s].median() if s else r["surrogate median C"]
569	        rows.append(r)
570	    return pd.DataFrame(rows).set_index("area")
571	CH = ch_table(ACT)
572	print(CH.T.to_string())
573	print("\nnatural-image windows:\n", ch_table(IMG, surr=False).T.to_string())
574	
575	def judge_ch(a, q="95"):
576	    (hl, hh), (cl, ch) = SPAN[a]
577	    H0, H1 = CH.loc[a, f"H span {q}"]; C0, C1 = CH.loc[a, f"C span {q}"]
578	    hw, cw = widen(hl, hh), widen(cl, ch)
579	    span_ok = hw[0] <= H0 and H1 <= hw[1] and cw[0] <= C0 and C1 <= cw[1]
580	    test_ok = CH.loc[a, "p"] < 0.001 and CH.loc[a, "empirical median C"] > CH.loc[a, "surrogate median C"]
581	    width = {b: CH.loc[b, f"C span {q}"][1] - CH.loc[b, f"C span {q}"][0] for b in paula.AREAS}
[... 483 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../../executed/paula-2026 && python -c "
import json
nb=json.load(open('reproduce_paula_2026.ipynb'))
for i in [3,4,8,11]:
    c=nb['cells'][i]
    for o in c.get('outputs',[]):
        print(''.join(o.get('text','')))
"
```

```
153 session files of 4293 assets; extraction took 35.4 min

sessions read: 153 failed: 0 []
subjects: 81 | session types: {'EPHYS_1_images_G_3uL_reward': 74, 'EPHYS_1_images_H_3uL_reward': 71, 'EPHYS_1_images_G_5uL_reward': 4, 'EPHYS_1_images_H_5uL_reward': 4}
genotypes: {'Sst-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt': 59, 'wt/wt': 49, 'Vip-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt': 45}
units per session: median 2024.0 range 1103 to 3388
active block length (s): {'count': 153.0, 'mean': 3603.9, 'std': 2.6, 'min': 3599.5, '25%': 3601.5, '50%': 3603.8, '75%': 3606.0, 'max': 3611.4}
active windows per session: {36: 151, 35: 2}
spontaneous epochs after the task (s): {'count': 153.0, 'mean': 289.0, 'std': 0.0, 'min': 289.0, '25%': 289.0, '50%': 289.0, '75%': 289.0, 'max': 289.0}
images per session: {8: 153} | flashes shown per session: median 4623.0 | omitted: median 179.0 | change flashes: median 241.0
length of the series each window is cut from (s):
                      min    50%    max
condition reading                     
active    -        100.0  100.0  100.0
blanks    a        160.0  286.0  528.0
          b        152.5  274.5  513.0
images    -        100.7  143.6  264.3
spont     a        100.0  100.0  100.0
          b        100.0  100.0  100.0
window rows by unit reading and condition:
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  ls ~/.cache 2>/dev/null; which python; python -c "import remfile, h5py; print('ok')"; ls executed/paula-2026/; cat tools/entry.py | head -50
```

```
Fri Nov 27 14:33:29 UTC 2026
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import remfile, h5py; print('ok')
    ^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'remfile'
reproduce_paula_2026.ipynb
result.json
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 devenv && uv pip install -q -p devenv/bin/python -r entries/paula-2026/requirements.lock.txt 2>&1 | tail -3; devenv/bin/python -c "import remfile,h5py,scipy;print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/paula-2026 && cat > $TMPDIR/t1.py <<'EOF'
import time, pickle, resource, sys
import numpy as np, pandas as pd
sys.path.insert(0, ".")
import paula
s, n = paula.list_sessions()
t0 = time.time()
data = paula.read_session(s[0])
t1 = time.time(); print("read", t1 - t0)
pickle.dump(data, open(sys.argv[1], "wb"))
meta, df, cv = paula.compute_session(0, *data)
t2 = time.time(); print("compute", t2 - t1, df.groupby("units").size().to_dict())
print("mem GB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
$TMPDIR/devenv/bin/python $TMPDIR/t1.py $TMPDIR/sess0.pkl
```

```
read 23.781646013259888
compute 26.14022207260132 {'all': 1216, 'qc': 768}
mem GB 1.637104
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t2.py <<'EOF'
import sys; sys.path.insert(0, ".")
import paula, h5py, remfile
s, n = paula.list_sessions()
f = h5py.File(remfile.File(paula.s3_url(s[0])), "r")
def show(g, pre=""):
    for k in g.keys():
        o = g[k]
        if isinstance(o, h5py.Dataset):
            v = o[()] if o.size < 5 else o.shape
            print(pre + k, v)
        else:
            print(pre + k + "/")
show(f["general"], "general/")
show(f["general/subject"], "subject/")
print(list(f["general/extracellular_ephys"].keys()))
print(list(f["units"].keys()))
import numpy as np
print(np.unique(f["units/quality"][:], return_counts=True))
print(list(f["intervals"].keys()))
print(list(f["intervals"][[k for k in f["intervals"] if k.startswith("Natural")][0]].keys()))
EOF
$TMPDIR/devenv/bin/python $TMPDIR/t2.py 2>&1 | head -80
```

```
general/devices/
general/extracellular_ephys/
general/institution b'Allen Institute for Brain Science'
general/keywords [b'visual' b'behavior' b'task']
general/metadata/
general/subject/
general/task_parameters/
subject/age b'P266D'
subject/description b'A visual behavior subject with a LabTracks ID'
subject/genotype b'Vip-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt'
subject/sex b'M'
subject/species b'Mus musculus'
subject/subject_id b'506940'
['electrodes', 'probeA', 'probeB', 'probeC', 'probeD', 'probeE', 'probeF']
['PT_ratio', 'amplitude', 'amplitude_cutoff', 'cluster_id', 'cumulative_drift', 'd_prime', 'firing_rate', 'id', 'isi_violations', 'isolation_distance', 'l_ratio', 'local_index', 'max_drift', 'nn_hit_rate', 'nn_miss_rate', 'peak_channel_id', 'presence_ratio', 'quality', 'recovery_slope', 'repolarization_slope', 'silhouette_score', 'snr', 'spike_amplitudes', 'spike_amplitudes_index', 'spike_times', 'spike_times_index', 'spread', 'velocity_above', 'velocity_below', 'waveform_duration', 'waveform_mean', 'waveform_mean_index']
(array([b'good', b'noise'], dtype=object), array([1830,  377]))
['Natural_Images_Lum_Matched_set_ophys_G_2019_presentations', 'flash_250ms_presentations', 'gabor_20_deg_250ms_presentations', 'spontaneous_presentations', 'trials']
['active', 'duration', 'end_frame', 'flashes_since_change', 'id', 'image_name', 'is_change', 'is_image_novel', 'is_sham_change', 'omitted', 'rewarded', 'start_frame', 'start_time', 'stimulus_block', 'stimulus_index', 'stimulus_name', 'stop_time', 'tags', 'tags_index', 'timeseries', 'timeseries_index', 'trials_id']
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t3.py <<'EOF'
import sys, pickle, time; sys.path.insert(0, ".")
import numpy as np, pandas as pd
import paula
meta, units, stim, sp, spikes = pickle.load(open(sys.argv[1], "rb"))
good = units.quality == "good"
qc95 = (units.isi_violations < 0.5) & (units.amplitude_cutoff < 0.1) & (units.presence_ratio > 0.95)
for name, sel in [("all", pd.Series(True, index=units.index)), ("qc", units.qc), ("good", good), ("qc95", qc95)]:
    rc = units.region[sel].value_counts()
    rc = rc[rc.index.isin(paula.REGION_AREA)]
    rc = rc[rc >= 30]
    print(name, int(sel.sum()), "pops", len(rc), "neurons", int(rc.sum()), rc.to_dict())
print(pd.crosstab(units.quality, units.qc))
print(units.groupby("quality")[["isi_violations","amplitude_cutoff","presence_ratio","firing_rate"]].median())
EOF
$TMPDIR/devenv/bin/python $TMPDIR/t3.py $TMPDIR/sess0.pkl
```

```
all 2207 pops 19 neurons 1922 {'VISp': 231, 'CA1': 181, 'APN': 162, 'VISam': 146, 'VISpm': 141, 'VISal': 135, 'VISl': 125, 'MGv': 117, 'SUB': 112, 'MGm': 87, 'LGd': 86, 'VISrl': 86, 'PIL': 74, 'DG': 54, 'LP': 44, 'MGd': 41, 'MRN': 39, 'CA3': 31, 'POL': 30}
qc 829 pops 12 neurons 605 {'VISam': 78, 'VISp': 67, 'VISal': 56, 'VISpm': 53, 'APN': 51, 'VISl': 51, 'SUB': 48, 'LGd': 46, 'MGv': 46, 'CA1': 45, 'PIL': 33, 'VISrl': 31}
good 1830 pops 15 neurons 1485 {'VISp': 194, 'APN': 137, 'CA1': 134, 'VISam': 134, 'VISpm': 121, 'VISal': 106, 'VISl': 105, 'MGv': 102, 'SUB': 86, 'MGm': 76, 'VISrl': 73, 'PIL': 70, 'LGd': 69, 'LP': 39, 'MGd': 39}
qc95 792 pops 12 neurons 578 {'VISam': 71, 'VISp': 66, 'VISal': 54, 'VISpm': 51, 'APN': 50, 'VISl': 49, 'LGd': 46, 'MGv': 44, 'SUB': 43, 'CA1': 42, 'PIL': 31, 'VISrl': 31}
qc       False  True 
quality              
good      1066    764
noise      312     65
         isi_violations  amplitude_cutoff  presence_ratio  firing_rate
quality                                                               
good           0.105033          0.045143            0.99      3.16343
noise          0.194135          0.286343            0.97      1.58098
```

**Agent calls Bash**

```bash
cat > $TMPDIR/survey.py <<'EOF'
import sys, pickle, time; sys.path.insert(0, ".")
import numpy as np, pandas as pd, h5py, remfile
import paula
from concurrent.futures import ThreadPoolExecutor
def surv(a):
    for t in range(3):
        try:
            f = h5py.File(remfile.File(paula.s3_url(a)), "r")
            e = f["general/extracellular_ephys/electrodes"]
            loc = pd.Series(paula._str(e["location"][:]), index=e["id"][:])
            grp = pd.Series(paula._str(e["group_name"][:]), index=e["id"][:]) if "group_name" in e else None
            u = f["units"]
            pc = u["peak_channel_id"][:]
            d = pd.DataFrame({"region": loc.loc[pc].values, "isi": u["isi_violations"][:], "amp": u["amplitude_cutoff"][:],
                              "pr": u["presence_ratio"][:], "quality": paula._str(u["quality"][:]), "fr": u["firing_rate"][:], "snr": u["snr"][:]})
            if grp is not None: d["probe"] = grp.loc[pc].values
            ni = [k for k in f["intervals"] if k.startswith("Natural")][0]
            nov = f["intervals"][ni]["is_image_novel"][:]
            out = {"path": a["path"], "desc": f["session_description"][()].decode(), "geno": f["general/subject/genotype"][()].decode(),
                   "subject": f["general/subject/subject_id"][()].decode(), "novel": float(np.nanmean(nov.astype(float))), "units": d}
            f.close(); return out
        except Exception as ex:
            err = ex; time.sleep(5)
    return {"path": a["path"], "error": repr(err)}
s, n = paula.list_sessions()
t0 = time.time()
with ThreadPoolExecutor(8) as ex:
    res = list(ex.map(surv, s))
print(time.time() - t0)
pickle.dump(res, open(sys.argv[1], "wb"))
EOF
$TMPDIR/devenv/bin/python $TMPDIR/survey.py $TMPDIR/survey.pkl
```

```
412.2198655605316
```

**Agent calls Bash**

```bash
cat > $TMPDIR/an.py <<'EOF'
import sys, pickle; sys.path.insert(0, ".")
import numpy as np, pandas as pd, paula
res = pickle.load(open(sys.argv[1], "rb"))
print("errors", [r for r in res if "error" in r])
T1 = {"VIS": 53985, "TH": 20541, "HP": 42396, "MB": 17163}
P1 = {"VIS": 586, "TH": 313, "HP": 363, "MB": 175}
filters = {
 "all": lambda d: np.ones(len(d), bool),
 "qc": lambda d: (d.isi < 0.5) & (d.amp < 0.1) & (d.pr > 0.9),
 "qc95": lambda d: (d.isi < 0.5) & (d.amp < 0.1) & (d.pr > 0.95),
 "good": lambda d: d.quality == "good",
 "good+pr95": lambda d: (d.quality == "good") & (d.pr > 0.95),
 "good+qc": lambda d: (d.quality == "good") & (d.isi < 0.5) & (d.amp < 0.1) & (d.pr > 0.9),
 "snr1_isi1_fr0.1": lambda d: (d.snr > 1) & (d.isi < 1) & (d.fr > 0.1),
 "good+fr0.1": lambda d: (d.quality == "good") & (d.fr > 0.1),
}
for name, fn in filters.items():
    rows = []
    for i, r in enumerate(res):
        d = r["units"]; d = d[fn(d).values if hasattr(fn(d), "values") else fn(d)]
        c = d.region.value_counts()
        for reg, n in c.items():
            if reg in paula.REGION_AREA and n >= 30: rows.append((i, reg, n))
    p = pd.DataFrame(rows, columns=["s", "region", "n"])
    ns = p.groupby("region").s.nunique(); keep = ns[ns >= 8].index
    p = p[p.region.isin(keep)]; p["area"] = p.region.map(paula.REGION_AREA)
    g = p.groupby("area").agg(pops=("n", "size"), neurons=("n", "sum"))
    sc = 102 / 153
    out = {a: f"pops {g.loc[a,'pops']} ({g.loc[a,'pops']*sc/P1[a]:.2f}) neur {g.loc[a,'neurons']} scaled ratio {g.loc[a,'neurons']*sc/T1[a]:.2f} per pop {g.loc[a,'neurons']/g.loc[a,'pops']:.0f} vs {T1[a]/P1[a]:.0f}" for a in T1}
    print(name, len(keep), "regions; missing", [r for r in paula.REGION_ORDER if r not in keep])
    for a, v in out.items(): print("   ", a, v)
m = pd.DataFrame([{k: r[k] for k in ["desc", "geno", "subject", "novel"]} | {"probes": r["units"].probe.nunique() if "probe" in r["units"] else -1} for r in res])
print(m.probes.value_counts(), m.novel.round(2).value_counts(), m.desc.value_counts(), m.subject.value_counts().value_counts())
EOF
$TMPDIR/devenv/bin/python $TMPDIR/an.py $TMPDIR/survey.pkl
```

```
errors []
all 26 regions; missing []
    VIS pops 888 (1.01) neur 110527 scaled ratio 1.36 per pop 124 vs 92
    TH pops 551 (1.17) neur 39370 scaled ratio 1.28 per pop 71 vs 66
    HP pops 586 (1.08) neur 91091 scaled ratio 1.43 per pop 155 vs 117
    MB pops 286 (1.09) neur 35256 scaled ratio 1.37 per pop 123 vs 98
qc 25 regions; missing ['NOT']
    VIS pops 754 (0.86) neur 44439 scaled ratio 0.55 per pop 59 vs 92
    TH pops 240 (0.51) neur 11443 scaled ratio 0.37 per pop 48 vs 66
    HP pops 325 (0.60) neur 25359 scaled ratio 0.40 per pop 78 vs 117
    MB pops 158 (0.60) neur 8855 scaled ratio 0.34 per pop 56 vs 98
qc95 23 regions; missing ['POST', 'NB', 'NOT']
    VIS pops 737 (0.84) neur 41454 scaled ratio 0.51 per pop 56 vs 92
    TH pops 234 (0.50) neur 11038 scaled ratio 0.36 per pop 47 vs 66
    HP pops 303 (0.56) neur 23154 scaled ratio 0.36 per pop 76 vs 117
    MB pops 142 (0.54) neur 7892 scaled ratio 0.31 per pop 56 vs 98
good 26 regions; missing []
    VIS pops 883 (1.00) neur 96319 scaled ratio 1.19 per pop 109 vs 92
    TH pops 513 (1.09) neur 34209 scaled ratio 1.11 per pop 67 vs 66
    HP pops 548 (1.01) neur 66217 scaled ratio 1.04 per pop 121 vs 117
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/an2.py <<'EOF'
import sys, pickle; sys.path.insert(0, ".")
import numpy as np, pandas as pd, paula
res = pickle.load(open(sys.argv[1], "rb"))
TABLE1 = {"VISal": 8572, "VISam": 8566, "VISl": 9255, "VISp": 10010, "VISpm": 10250, "VISrl": 7332,
          "LGd": 2169, "LP": 2795, "MGd": 2497, "MGm": 1928, "MGv": 4492, "PIL": 868, "POL": 1298, "PoT": 1461, "SGN": 3033,
          "CA1": 22399, "CA3": 3729, "DG": 7486, "POST": 1367, "ProS": 3067, "SUB": 4348,
          "APN": 10716, "NB": 793, "NOT": 309, "MRN": 3661, "SCig": 1684}
for name, fn in {"vbn": lambda d: (d.snr > 1) & (d.isi < 1) & (d.fr > 0.1), "all": lambda d: d.fr > -1}.items():
    rows = []
    for i, r in enumerate(res):
        d = r["units"]; d = d[fn(d)]
        for reg, n in d.region.value_counts().items():
            if reg in paula.REGION_AREA and n >= 30: rows.append((i, reg, n))
    p = pd.DataFrame(rows, columns=["s", "region", "n"])
    g = p.groupby("region").agg(pops=("n", "size"), neurons=("n", "sum")).reindex(paula.REGION_ORDER)
    g["scaled ratio"] = (g.neurons * 102 / 153 / pd.Series(TABLE1)).round(2)
    print(name); print(g.T.to_string())
EOF
$TMPDIR/devenv/bin/python $TMPDIR/an2.py $TMPDIR/survey.pkl
```

```
vbn
region           VISal    VISam      VISl      VISp     VISpm     VISrl      LGd       LP      MGd      MGm      MGv      PIL      POL      PoT      SGN       CA1      CA3       DG     POST     ProS      SUB       APN      NB     NOT      MRN     SCig
pops            147.00    144.0    144.00    148.00    149.00    143.00    49.00    62.00    58.00    61.00    79.00    30.00    38.00    40.00    69.00    142.00    91.00    126.0    41.00    44.00    82.00    124.00   19.00   11.00    59.00    34.00
neurons       13079.00  12819.0  14602.00  15328.00  14650.00  10660.00  3281.00  4034.00  3251.00  3500.00  6777.00  1377.00  2222.00  2590.00  4426.00  30997.00  5261.00  10083.0  2029.00  3789.00  6742.00  15813.00  939.00  459.00  4839.00  2153.00
scaled ratio      1.02      1.0      1.05      1.02      0.95      0.97     1.01     0.96     0.87     1.21     1.01     1.06     1.14     1.18     0.97      0.92     0.94      0.9     0.99     0.82     1.03      0.98    0.79    0.99     0.88     0.85
all
region           VISal     VISam      VISl      VISp     VISpm     VISrl      LGd       LP      MGd      MGm      MGv      PIL      POL      PoT      SGN       CA1       CA3       DG     POST    ProS      SUB       APN       NB     NOT      MRN     SCig
pops            148.00    147.00    144.00    151.00    150.00    148.00    50.00    68.00    65.00    73.00    82.00    36.00    53.00    53.00    71.00    146.00    114.00    141.0    50.00    49.0    86.00    127.00    27.00   15.00    74.00    43.00
neurons       17442.00  16919.00  19508.00  21567.00  19772.00  15319.00  3552.00  4676.00  3922.00  4752.00  7717.00  2073.00  3624.00  3892.00  5162.00  42687.00  10489.00  22411.0  2820.00  4586.0  8098.00  22257.00  1688.00  678.00  7314.00  3319.00
scaled ratio      1.36      1.32      1.41      1.44      1.29      1.39     1.09     1.12     1.05     1.64     1.15     1.59     1.86     1.78     1.13      1.27      1.88      2.0     1.38     1.0     1.24      1.38    
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s -m 20 "https://api.github.com/search/code?q=snr+isi_violations+firing_rate+repo:AllenInstitute/AllenSDK" | head -20; curl -s -m 20 -o $TMPDIR/q.ipynb -w "%{http_code}\n" https://raw.githubusercontent.com/AllenInstitute/AllenSDK/master/doc_template/examples_root/examples/nb/visual_behavior_neuropixels_quickstart.ipynb
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
grep -o '[^"]*snr[^"]*' $TMPDIR/q.ipynb | head; cd $TMPDIR && git ls-remote https://github.com/AllenInstitute/AllenSDK master 2>/dev/null | head -2
```

```
<persisted-output>
Output too large (52.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/5df290d5-9df0-4907-b855-07c1c7902ce6/tool-results/b06349267.txt

Preview (first 2KB):
good_unit_filter = ((unit_channels['snr']>1)&\n
iVBORw0KGgoAAAANSUhEUgAAA6gAAAJ7CAYAAADunLwdAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjcuNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8WgzjOAAAACXBIWXMAAA9hAAAPYQGoP6dpAACbbklEQVR4nO39Z5gkV2H+f5+qjtOTevLMzuzObE7SapVzAKGIwAQLkTHGiGSTg/3DNgZjbIEB20RjMEkkCYEAoYgQymEVVrvanGbTzE7Oubvq/8LP8+rch6vb0kpV8vfz8t6z1T0VTtWZvuZuLwzD0AAAAAAA8ALzX+g3AAAAAACAMSxQAQAAAAARwQIVAAAAABAJLFABAAAAAJHAAhUAAAAAEAksUAEAAAAAkcACFQAAAAAQCSxQAQAAAACRkCx14Mnv/pLMW27cKfPiyIjMB689W+ZVPUUrm1yUkGNb7+qR+e53LZL5ogfsbRtjzP2//pjMo+YS/+qyxh/9xDky77xR7zfl4NV6X3712m/K/HcT62X+8IfPkPk9v/vrkt/LC+WS5OvLGu+nUzIPw1Dnc3NiI/qc93xP5+m0zIOZGZnfVbxB5lFT7jmfWLVc5sXd+0rexsFPO66bTz0k893fPq3kbRtjzME//0RZ418Irv0+/eozZd5zgT4vF92nz/ly5H75aFnjXe/xwZs++qzfy/Ph8hM+qf9hQN9Lw4kJPX5Vl4z9oXE7TOr5xhT0PTOoq9HbnpiS+W0H9HNDlFx8wT+VNX56UVbmVTc8IvPgvI1WNnBKTo4dW78g89pt+t7S/usjMr9t/xdlHjWXr/q4zGe76mWefeqA3lBdrYyLe+3xiRVLSx5rjDELLzu1rPdy+8B/yjxqznyzPkfy28U8YYwJNm+Xub9xXVnjj6e7ghuf99cs1xWdH5J5OKnnUPmcaIzxMhn9Ag15e+yUfh4sDg7L3K+t1tsuBjK+fehbevyzxCeoAAAAAIBIYIEKAAAAAIgEFqgAAAAAgEhggQoAAAAAiISSS5LSk7r0wsvr0oTBq9fIvH7XrMz7Tq2wso9eqwtd/rXqdTJP6b8xNiOrSv4xI6nwUv1H+snfPyFzVxnSbFeDzPtOt//YumWT/sPsvzTvlvlMq/7j6S6jSx/iwFVMZBK6WCRw/DG7cZQkeUn7vHSVHnkVupijODKmX9N7cf7uyVWG5OIqZVOW/ahP/4PjNVf9xeMyd77HPy/5rbxg9n75LJmv+JAugFnxy/K2r4qMXGVILQ/re0vf2brEo9xSpchZKMg4WNIs88SgnhNMvy5VClrt+X++wb7v/jH+nC5PShV1Hgeu0qNcj35WyT/mKBvsWiLjUbH9ymP6frnial28s3fbKr3tM3SZYVy4iokcZ7YJlrXLPNy0VeaJBrtsKairkmNdZUip3+nnrPie8f+j5seOUq/j+JpRKlR6oQTDen52PeN5OT1Hu0qSwlFxf6zQ2/Dr83ob07pUycvo59Pj5cX5FAsAAAAAiB0WqAAAAACASGCBCgAAAACIBBaoAAAAAIBIYIEKAAAAAIiE0lt8x8vr9nK19c5Xp2Te/vtRK3vrRwfl2K6//LrM33HDe2Te+RtH02lMZLuHZK47H8unGnuTn9SNpjNbOmS+YsMRmSe/Et8GZb+qUubhrG7rDR3NuX7O0Ukomi+99lY5NKjNyTzhOxqFR3RTXFzMX366zCv2D8t8/5
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json,os
nb=json.load(open(os.environ["TMPDIR"]+"/q.ipynb"))
for c in nb["cells"]:
    s="".join(c["source"])
    if "good_unit_filter" in s: print(s[:600]); print("----")
EOF
git ls-remote https://github.com/AllenInstitute/AllenSDK refs/heads/master
```

```
#first let's sort our units by depth
unit_channels = unit_channels.sort_values('probe_vertical_position', ascending=False)

#now we'll filter them
good_unit_filter = ((unit_channels['snr']>1)&
                    (unit_channels['isi_violations']<1)&
                    (unit_channels['firing_rate']>0.1))

good_units = unit_channels.loc[good_unit_filter]
spike_times = session.spike_times
----
a56bd8ea7613a812334602b64746cdd30c325a96	refs/heads/master
```

**Agent calls Bash**

```bash
date -u
```

```
Fri Nov 27 14:43:30 UTC 2026
```

**Agent**

Now editing the helper: three unit readings, the adopted one being the VBN tutorial filter.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/paula-2026/paula.py",
 "old_string": "- Unit readings (claims file): 'all', every unit of the units table; 'qc', ISI violations <\n  0.5, amplitude cutoff < 0.1 and presence ratio > 0.9.",
 "new_string": "- Unit readings: 'all', every unit of the units table, and 'qc', ISI violations < 0.5,\n  amplitude cutoff < 0.1 and presence ratio > 0.9 (the claims file's two readings); 'vbn',\n  snr > 1, ISI violations < 1 and firing rate > 0.1 spikes/s, the \"good_unit_filter\" of the\n  Allen Institute's Visual Behavior Neuropixels quickstart tutorial (AllenSDK, commit\n  a56bd8ea7613a812334602b64746cdd30c325a96, doc_template/examples_root/examples/nb/\n  visual_behavior_neuropixels_quickstart.ipynb). 'vbn' is the adopted reading, an assumption:\n  the paper states no filter, and of the filters tried it is the one whose neuron counts per\n  population match Table I (see the notebook, claim table1-sample). Unit counts per subregion\n  are also kept for 'good' (quality label 'good'), 'qc95' (as 'qc' with presence ratio > 0.95)\n  and 'good_pr95' ('good' with presence ratio > 0.95), for the count comparison only."
}
```

```
The file entries/paula-2026/paula.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/paula-2026/paula.py",
 "old_string": "MIN_UNITS = 30\nMIN_SESSIONS = 8",
 "new_string": "MIN_UNITS = 30\nMIN_SESSIONS = 8\nUNIT_READINGS = [\"vbn\", \"all\", \"qc\"]  # 'vbn' adopted; the surrogate is drawn under five seeds for it only\nMAIN_UNITS = \"vbn\"\nCOUNT_FILTERS = [\"all\", \"qc\", \"vbn\", \"good\", \"qc95\", \"good_pr95\"]\n\n\ndef unit_filters(units):\n    \"\"\"Boolean selections of the unit readings and of the filters used for counts only.\"\"\"\n    q = (units.isi_violations < 0.5) & (units.amplitude_cutoff < 0.1)\n    good = units.quality == \"good\"\n    return {\"all\": pd.Series(True, index=units.index),\n            \"qc\": q & (units.presence_ratio > 0.9),\n            \"vbn\": (units.snr > 1) & (units.isi_violations < 1) & (units.firing_rate > 0.1),\n            \"good\": good,\n            \"qc95\": q & (units.presence_ratio > 0.95),\n            \"good_pr95\": good & (units.presence_ratio > 0.95)}"
}
```

```
The file entries/paula-2026/paula.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/paula-2026/paula.py",
 "old_string": "        \"presence_ratio\": u[\"presence_ratio\"][:], \"quality\": _str(u[\"quality\"][:]),\n        \"firing_rate\": u[\"firing_rate\"][:]})\n    units[\"qc\"] = ((units.isi_violations < 0.5) & (units.amplitude_cutoff < 0.1)\n                   & (units.presence_ratio > 0.9))",
 "new_string": "        \"presence_ratio\": u[\"presence_ratio\"][:], \"quality\": _str(u[\"quality\"][:]),\n        \"firing_rate\": u[\"firing_rate\"][:], \"snr\": u[\"snr\"][:]})\n    pc = u[\"peak_channel_id\"][:]\n    if \"group_name\" in e:\n        meta[\"n_probes\"] = int(pd.Series(_str(e[\"group_name\"][:]), index=e[\"id\"][:]).loc[pc].nunique())\n    else:\n        meta[\"n_probes\"] = -1"
}
```

```
The file entries/paula-2026/paula.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/paula-2026/paula.py",
 "old_string": "                         \"is_change\": ni[\"is_change\"][:]})\n    act_block = stim[stim.active].block.min()",
 "new_string": "                         \"is_change\": ni[\"is_change\"][:], \"novel\": ni[\"is_image_novel\"][:]})\n    act_block = stim[stim.active].block.min()"
}
```

```
The file entries/paula-2026/paula.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/paula-2026/paula.py",
 "old_string": "    counts = units.region.value_counts()\n    cand = counts[counts >= MIN_UNITS].index",
 "new_string": "    counts = units.region.value_counts()  # 'all' holds every other reading, so its counts bound them\n    cand = counts[counts >= MIN_UNITS].index"
}
```

```
The file entries/paula-2026/paula.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/paula-2026/paula.py",
 "old_string": "    meta[\"region_counts_all\"] = units.region.value_counts().to_dict()\n    meta[\"region_counts_qc\"] = units.region[units.qc].value_counts().to_dict()\n    meta[\"n_flashes\"] = int((~stim.omitted).sum())\n    meta[\"n_omitted\"] = int(stim.omitted.sum())\n    meta[\"n_changes\"] = int(np.nansum(stim.is_change.values))\n    meta[\"n_images\"] = int(stim[~stim.omitted].image.nunique())\n    ft = flash_table(stim)",
 "new_string": "    filt = unit_filters(units)\n    for name in COUNT_FILTERS:\n        meta[f\"region_counts_{name}\"] = units.region[filt[name]].value_counts().to_dict()\n    meta[\"n_flashes\"] = int((~stim.omitted).sum())\n    meta[\"n_omitted\"] = int(stim.omitted.sum())\n    meta[\"n_changes\"] = int(np.nansum(stim.is_change.values))\n    meta[\"n_images\"] = int(stim[~stim.omitted].image.nunique())\n    meta[\"novel_fraction\"] = float(np.nanmean(stim.novel.values[~stim.omitted.values].astype(float)))\n    ft = flash_table(stim)\n    shown = ft[~ft.omitted]\n    blk = (shown.bstop - shown.stop).values\n    meta[\"flashes_per_image\"] = shown.image.value_counts().to_dict()\n    meta[\"changes_per_image\"] = shown[shown.is_change.astype(bool)].image.value_counts().to_dict()\n    meta[\"blank_piece_full\"] = int((blk >= 0.5 - 1e-6).sum())\n    meta[\"blank_piece_short\"] = int((blk < 0.5 - 1e-6).sum())\n    meta[\"blank_piece_median\"] = float(np.median(blk))\n    meta[\"gray_after_flash_median\"] = float(np.median((np.r_[ft.start.values[1:], np.nan] - ft.stop.values)[~ft.omitted.values][:-1]))"
}
```

```
The file entries/paula-2026/paula.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/paula-2026/paula.py",
 "old_string": "    for ur in [\"all\", \"qc\"]:\n        sel = units.qc if ur == \"qc\" else pd.Series(True, index=units.index)\n        for region in REGION_ORDER:",
 "new_string": "    for ur in UNIT_READINGS:\n        sel = filt[ur]\n        for region in REGION_ORDER:"
}
```

```
The file entries/paula-2026/paula.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/paula-2026/paula.py",
 "old_string": "                full = ur == \"all\"\n                nseeds = 5 if (cond == \"active\" and full) else 1\n                rngs = [np.random.default_rng([base + off, sess_i, wi, 0 if ur == \"all\" else 1])\n                        for off in SURR_SEED_OFFSETS[:nseeds]]\n                m = window_measures(t, ow, n, rngs, do_corr, full)",
 "new_string": "                nseeds = 5 if (cond == \"active\" and ur == MAIN_UNITS) else 1\n                rngs = [np.random.default_rng([base + off, sess_i, wi, UNIT_READINGS.index(ur)])\n                        for off in SURR_SEED_OFFSETS[:nseeds]]\n                m = window_measures(t, ow, n, rngs, do_corr)"
}
```

```
The file entries/paula-2026/paula.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/paula-2026/paula.py",
 "old_string": "def window_measures(t, own, n_units, surr_rngs, do_corr, full=True):\n    \"\"\"All measures of one 100-s window of a population (t in 0..100 s, own in 0..N-1).\n    With full False, only CV, H, C and the surrogate (the unit-selection variant).\"\"\"",
 "new_string": "def window_measures(t, own, n_units, surr_rngs, do_corr, full=True):\n    \"\"\"All measures of one 100-s window of a population (t in 0..100 s, own in 0..N-1).\n    With full False, only CV, H, C and the surrogate.\"\"\""
}
```

```
The file entries/paula-2026/paula.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/paula-2026 && python - <<'EOF'
p="paula.py"; s=open(p).read()
s=s.replace('shown[shown.is_change.astype(bool)]','shown[np.asarray(shown.is_change, float) > 0]')
open(p,"w").write(s)
EOF
cat > $TMPDIR/t4.py <<'EOF'
import sys, pickle, time, resource; sys.path.insert(0, ".")
import paula
d = pickle.load(open(sys.argv[1], "rb"))
meta, units, stim, sp, spikes = d
units["snr"] = 2.0  # pickle predates snr; time only
t0 = time.time()
meta, df, cv = paula.compute_session(0, meta, units, stim, sp, spikes)
print("compute", time.time() - t0, df.groupby("units").size().to_dict())
print({k: v for k, v in meta.items() if k.startswith(("flashes", "changes", "blank", "gray", "novel", "n_"))})
print(df.columns.tolist())
print("mem GB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
$TMPDIR/devenv/bin/python $TMPDIR/t4.py $TMPDIR/sess0.pkl
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t4.py", line 7, in <module>
    meta, df, cv = paula.compute_session(0, meta, units, stim, sp, spikes)
                   ~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/paula-2026/paula.py", line 478, in compute_session
    meta["novel_fraction"] = float(np.nanmean(stim.novel.values[~stim.omitted.values].astype(float)))
                                              ^^^^^^^^^^
  File "/tmp/claude-1001/devenv/lib/python3.13/site-packages/pandas/core/generic.py", line 6434, in __getattr__
    return object.__getattribute__(self, name)
           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^
AttributeError: 'DataFrame' object has no attribute 'novel'
```

**Agent**

Old pickle lacks the new columns; re-reading one session fresh.

**Agent calls Bash**

```bash
cd entries/paula-2026 && sed -i 's/^units\["snr"\] = 2.0.*$//' $TMPDIR/t4.py && $TMPDIR/devenv/bin/python $TMPDIR/t1.py $TMPDIR/sess0.pkl && $TMPDIR/devenv/bin/python $TMPDIR/t4.py $TMPDIR/sess0.pkl
```

```
read 21.55796527862549
compute 41.34333348274231 {'all': 1216, 'qc': 768, 'vbn': 960}
mem GB 1.65872
compute 38.04408025741577 {'all': 1216, 'qc': 768, 'vbn': 960}
{'n_probes': 6, 'n_units': 2207, 'n_spikes': 117633702, 'n_vis_units_clock': 864, 'n_flashes': 4637, 'n_omitted': 162, 'n_changes': 164, 'n_images': 8, 'novel_fraction': 0.0, 'flashes_per_image': {'im083_r': 753, 'im078_r': 686, 'im115_r': 640, 'im044_r': 638, 'im111_r': 566, 'im012_r': 496, 'im036_r': 439, 'im047_r': 419}, 'changes_per_image': {'im078_r': 21, 'im083_r': 21, 'im012_r': 21, 'im115_r': 21, 'im047_r': 20, 'im111_r': 20, 'im036_r': 20, 'im044_r': 20}, 'blank_piece_full': 4632, 'blank_piece_short': 5, 'blank_piece_median': 0.5, 'gray_after_flash_median': 0.5004176136148999, 'n_active_windows': 36, 'n_spont_windows': 2}
['session', 'subject', 'units', 'region', 'area', 'n', 'condition', 'reading', 'k', 'image', 'series_length', 'cv', 'H', 'C', 'rate', 'C_20_3_4', 'H_20_3_4', 'C_20_5_1', 'H_20_5_1', 'C_20_6_1', 'H_20_6_1', 'C_50_4_2', 'H_50_4_2', 'C_50_5_3', 'H_50_5_3', 'corr50', 'corr20', 's_cv', 's_H', 's_C', 's_cv_s1000', 's_H_s1000', 's_C_s1000', 's_cv_s2000', 's_H_s2000', 's_C_s2000', 's_cv_s3000', 's_H_s3000', 's_C_s3000', 's_cv_s4000', 's_H_s4000', 's_C_s4000']
mem GB 1.3009
```

**Agent calls Bash**

```bash
python - <<'EOF'
p="paula.py"; s=open(p).read()
a=s.index("def survey_session(asset):"); b=s.index("def _safe(args):")
s=s[:a]+s[b:]
open(p,"w").write(s)
EOF
grep -n "survey_session\|units.qc\|full" paula.py; $TMPDIR/devenv/bin/python -c "import nbclient, ipykernel; print('ok')"
```

```
Exit code 1
161:    pe = np.full(nstates, 1.0 / nstates)
262:def window_measures(t, own, n_units, surr_rngs, do_corr, full=True):
264:    With full False, only CV, H, C and the surrogate."""
271:    for bw, d, tau in (ROBUST if full else []):
276:    if do_corr and full:
423:            off = np.full(len(ft), np.nan)
484:    meta["blank_piece_full"] = int((blk >= 0.5 - 1e-6).sum())
501:            o_all = np.concatenate([np.full(len(spikes[k]), j) for j, k in enumerate(ks)])
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import nbclient, ipykernel; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'nbclient'
```

**Agent calls Bash**

```bash
uv pip install -q -p $TMPDIR/devenv/bin/python nbclient ipykernel nbformat 2>&1 | tail -2; cat > $TMPDIR/sub.py <<'EOF'
import sys, pickle, time; sys.path.insert(0, ".")
import paula
s, n = paula.list_sessions()
sub = s[::6][:26]
t0 = time.time()
metas, windows, cv10, failed = paula.run_all(sub, workers=4)
print("took", (time.time() - t0) / 60, "failed", failed, len(metas))
pickle.dump((s, n, metas, windows, cv10, failed), open(sys.argv[1], "wb"))
EOF
$TMPDIR/devenv/bin/python $TMPDIR/sub.py $TMPDIR/subset.pkl
```

```
took 7.925286138057709 failed [] 26
```

**Agent calls Bash**

```bash
date -u; python - <<'EOF'
import json
nb=json.load(open("reproduce_paula_2026.ipynb"))
print(nb["metadata"]); print(nb["nbformat"], nb["nbformat_minor"])
print(nb["cells"][1].keys(), nb["cells"][1]["metadata"])
EOF
```

```
Fri Nov 27 14:55:07 UTC 2026
{'kernelspec': {'display_name': 'Python 3', 'language': 'python', 'name': 'python3'}}
4 5
dict_keys(['cell_type', 'execution_count', 'id', 'metadata', 'outputs', 'source']) {}
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/cells_a.py",
 "content": "C = {}\n\nC[4] = r'''import resource\nprint(\"sessions read:\", len(metas), \"failed:\", len(failed), failed)\nprint(\"subjects:\", metas.subject.nunique(), \"| sessions per subject:\", metas.subject.value_counts().value_counts().to_dict())\nprint(\"session types:\", metas.session_description.value_counts().to_dict())\nprint(\"genotypes:\", metas.genotype.value_counts().to_dict())\nprint(\"probes with units per session:\", metas.n_probes.value_counts().to_dict())\nmetas[\"image_set\"] = np.where(metas.session_description.str.contains(\"_G_\"), \"G\", \"H\")\nmetas[\"novel\"] = metas.novel_fraction > 0\nprint(\"image set by novel images (is_image_novel):\\n\", pd.crosstab(metas.image_set, metas.novel))\nprint(\"no grouping of sessions gives 102: by genotype\", metas.genotype.value_counts().to_dict(), \"| by image set and novelty\",\n      metas.groupby([\"image_set\", \"novel\"]).size().to_dict(), \"| six probes\", int((metas.n_probes == 6).sum()))\nprint(\"units per session: median\", metas.n_units.median(), \"range\", metas.n_units.min(), \"to\", metas.n_units.max())\nprint(\"active block length (s):\", (metas.active_end - metas.active_start).describe().round(1).to_dict())\nprint(\"active windows per session:\", metas.n_active_windows.value_counts().to_dict())\nprint(\"spontaneous epochs after the task (s):\", pd.Series([e[-1][1] - e[-1][0] for e in metas.spont_epochs]).describe().round(1).to_dict())\nprint(\"images per session:\", metas.n_images.value_counts().to_dict(), \"| flashes shown per session: median\", metas.n_flashes.median(),\n      \"| omitted: median\", metas.n_omitted.median(), \"| change flashes: median\", metas.n_changes.median())\n# blanks (Methods II.A gives about 240 s per image): flashes per image, and the gray-screen pieces after them\nfpi = pd.Series([v for d in metas.flashes_per_image for v in d.values()])\ncpi = pd.Series([v for d in metas.changes_per_image for v in d.values()])\nprint(\"shown flashes per image (all sessions):\", fpi.describe().round(1).to_dict())\nprint(\"change flashes per image:\", cpi.describe().round(1).to_dict())\nprint(\"blank pieces of 0.5 s:\", int(metas.blank_piece_full.sum()), \"| shorter (cut by the next onset):\", int(metas.blank_piece_short.sum()),\n      \"| median gray screen after a shown flash (s):\", round(metas.gray_after_flash_median.median(), 4))\nprint(\"blank series per image (s) = 0.5 s x flashes: median\", round(0.5 * fpi.median(), 1), \"| without change flashes\", round(0.5 * (fpi - cpi).median(), 1),\n      \"| flashes per image for 240 s: 480\")\nsl = windows[windows.units == paula.MAIN_UNITS].groupby([\"condition\", \"reading\"]).series_length.describe()[[\"min\", \"50%\", \"max\"]].round(1)\nprint(\"length of the series each window is cut from (s), units=vbn:\\n\", sl)\nprint(\"window rows by unit reading and condition:\\n\", windows.groupby([\"units\", \"condition\", \"reading\"]).size())\nfor col, unit in [(\"cv\", \"\"), (\"H\", \"\"), (\"C\", \"\"), (\"rate\", \"spikes/s per unit\"), (\"corr50\", \"\"), (\"corr20\", \"\")]:\n    x = windows[col]\n    print(f\"{col}: {np.nanmin(x):.3f} to {np.nanmax(x):.3f} {unit}, NaN {int(x.isna().sum())}\")\n# recordings deposited more than once: identical spike-time fingerprints or spike counts\nfp = metas.fingerprint.apply(lambda v: tuple(np.round(v, 6)))\nprint(\"sessions sharing a spike-time fingerprint:\", int(fp.duplicated(keep=False).sum()),\n      \"| sharing a total spike count:\", int(metas.n_spikes.duplicated(keep=False).sum()),\n      \"| sharing subject and start time:\", int(metas.duplicated([\"subject\", \"session_start_time\"], keep=False).sum()))\nprint(\"peak memory of this process (GB):\", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6)\n'''\n\nC[8] = r'''TABLE1 = {\"VISal\": 8572, \"VISam\": 8566, \"VISl\": 9255, \"VISp\": 10010, \"VISpm\": 10250, \"VISrl\": 7332,\n          \"LGd\": 2169, \"LP\": 2795, \"MGd\": 2497, \"MGm\": 1928, \"MGv\": 4492, \"PIL\": 868, \"POL\": 1298, \"PoT\": 1461, \"SGN\": 3033,\n          \"CA1\": 22399, \"CA3\": 3729, \"DG\": 7486, \"POST\": 1367, \"ProS\": 3067, \"SUB\": 4348,\n          \"APN\": 10716, \"NB\": 793, \"NOT\": 309, \"MRN\": 3661, \"SCig\": 1684}\nEXP1 = {\"sessions\": 102, \"VIS populations\": 586, \"TH populations\": 313, \"HP populations\": 363, \"MB populations\": 175,\n        \"VIS neurons\": 53985, \"TH neurons\": 20541, \"HP neurons\": 42396, \"MB neurons\": 17163,\n        \"natural image windows\": 11321, \"active behavior windows\": 51704, \"blank windows\": 11321, \"spontaneous windows\": 2870}\nhas_spont = set(metas.session_index[metas.n_spont_windows >= 2])\nSCALE = 102 / len(metas)\n# 1. every filter, from the unit counts of each session: populations (>= 30 units of one Table I subregion in a session,\n#    the subregion kept when it has such populations in >= 8 sessions) and neurons, as counted and scaled to 102 sessions\nflt = []\nfor f in paula.COUNT_FILTERS:\n    rows = [(m.session_index, r, c) for m in metas.itertuples() for r, c in getattr(m, f\"region_counts_{f}\").items()]\n    rc = pd.DataFrame(rows, columns=[\"session\", \"region\", \"n\"])\n    rc = rc[rc.n >= paula.MIN_UNITS]\n    ns = rc.groupby(\"region\").session.nunique()\n    lab = sorted(ns[ns >= paula.MIN_SESSIONS].index)\n    print(f\"filter {f}: labels kept by the rule {len(lab)}; not in Table I {[l for l in lab if l not in paula.REGION_AREA]}; \"\n          f\"Table I subregions not kept {[r for r in paula.REGION_ORDER if r not in lab]}\")\n    p = rc[rc.region.isin([l for l in lab if l in paula.REGION_AREA])].copy()\n    p[\"area\"] = p.region.map(paula.REGION_AREA)\n    per_reg = p.groupby(\"region\").n.sum().reindex(paula.REGION_ORDER) * SCALE / pd.Series(TABLE1)\n    for a in paula.AREAS:\n        x = p[p.area == a]\n        flt.append({\"filter\": f, \"area\": a, \"populations\": len(x), \"populations x 102/153\": round(len(x) * SCALE),\n                    \"Table I populations\": EXP1[f\"{a} populations\"], \"neurons\": int(x.n.sum()), \"neurons x 102/153\": round(x.n.sum() * SCALE),\n                    \"Table I neurons\": EXP1[f\"{a} neurons\"], \"scaled neuron ratio\": round(x.n.sum() * SCALE / EXP1[f\"{a} neurons\"], 2),\n                    \"neurons per population\": round(x.n.mean(), 1), \"Table I per population\": round(EXP1[f\"{a} neurons\"] / EXP1[f\"{a} populations\"], 1),\n                    \"subregion ratios (scaled)\": f\"{per_reg[[r for r in paula.AREAS[a]]].min():.2f}-{per_reg[[r for r in paula.AREAS[a]]].max():.2f}\"})\nflt = pd.DataFrame(flt)\nprint(flt.to_string())\nfsum = flt.assign(err=lambda d: np.abs(np.log(d[\"scaled neuron ratio\"]))).groupby(\"filter\").err.max()\nprint(\"largest |log ratio| of the scaled area neuron counts to Table I, by filter:\", fsum.round(3).to_dict())\n# 2. the three unit readings run below: counts from the windows themselves, under both session readings\nt1 = {}\nfor ur in paula.UNIT_READINGS:\n    regs = paula.kept_regions(windows, ur)\n    for sr in [\"a\", \"b\"]:\n        w = paula.conditions(windows, ur, \"a\", \"a\")\n        w = w[w.region.isin(regs)]\n        if sr == \"b\":\n            w = w[w.session.isin(has_spont)]\n        pops = w[w.condition == \"active\"].drop_duplicates([\"session\", \"region\"])\n        res = {\"sessions\": pops.session.nunique()}\n        for a in paula.AREAS:\n            res[f\"{a} populations\"] = int((pops.area == a).sum())\n        for a in paula.AREAS:\n            res[f\"{a} neurons\"] = int(pops.loc[pops.area == a, \"n\"].sum())\n        res[\"natural image windows\"] = int((w.condition == \"images\").sum())\n        res[\"active behavior windows\"] = int((w.condition == \"active\").sum())\n        res[\"blank windows\"] = int((w.condition == \"blanks\").sum())\n        res[\"spontaneous windows\"] = int((w.condition == \"spont\").sum())\n        t1[f\"{ur}/{sr}\"] = res\n        if sr == \"a\":\n            per = pops.groupby(\"region\").agg(populations=(\"n\", \"size\"), neurons=(\"n\", \"sum\")).reindex(paula.REGION_ORDER)\n            per[\"Table I neurons\"] = pd.Series(TABLE1)\n            per[\"ratio\"] = (per.neurons / per[\"Table I neurons\"]).round(2)\n            per[\"ratio x 102/153\"] = (per.neurons * SCALE / per[\"Table I neurons\"]).round(2)\n            print(f\"\\nunits={ur}: per subregion (kept regions: {len(regs)})\\n\", per.T.to_string())\ntab = pd.DataFrame(t1)\ntab[\"expected\"] = pd.Series(EXP1)\ntab[\"tolerance\"] = tab[\"expected\"] * 0.1\nfor c in t1:\n    tab[\"within \" + c] = (tab[c] - tab[\"expected\"]).abs() <= tab[\"tolerance\"]\nprint(tab.to_string())\nfor c in t1:\n    print(c, \"all within tolerance:\", bool(tab[\"within \" + c].all()), \"| session and population counts within:\",\n          bool(tab.loc[[\"sessions\"] + [f\"{a} populations\" for a in paula.AREAS], \"within \" + c].all()))\nprint(\"blank windows under reading b:\", int((paula.conditions(windows, paula.MAIN_UNITS, \"b\", \"b\").condition == \"blanks\").sum()))\n'''\n\nC[11] = r'''UNITS = paula.UNIT_READINGS\nMAIN = paula.MAIN_UNITS\nCR = [(\"a\", \"a\"), (\"a\", \"b\"), (\"b\", \"a\"), (\"b\", \"b\")]\nSFX = [\"\", \"_s1000\", \"_s2000\", \"_s3000\", \"_s4000\"]\nVD = [\"images\", \"active\", \"blanks\"]\nREGS, WD, CACHE, OUT = {}, {}, {}, {}\nfor ur in UNITS:\n    REGS[ur] = paula.kept_regions(windows, ur)\n    WD[ur] = {}\n    for b, s in CR:\n        x = paula.conditions(windows, ur, b, s)\n        WD[ur][f\"{b}/{s}\"] = x[x.region.isin(REGS[ur])]\n    CACHE[ur] = {}\n    a = WD[ur][\"a/a\"]\n    print(f\"units={ur}: {len(REGS[ur])} subregions; {a[a.condition == 'active'].drop_duplicates(['session', 'region']).shape[0]} populations; \"\n          f\"active windows {int((a.condition == 'active').sum())}; not kept {[r for r in paula.REGION_ORDER if r not in REGS[ur]]}\")\n\ndef use(ur):\n    \"\"\"Make `ur` the current unit reading: W, ACT, IMG, REG and the per-reading tables computed so far.\"\"\"\n    g = globals()\n    g.update(UR=ur, W=WD[ur], REG=REGS[ur], SFXU=SFX if ur == MAIN else [\"\"])\n    g.update(ACT=W[\"a/a\"][W[\"a/a\"].condition == \"active\"], IMG=W[\"a/a\"][W[\"a/a\"].condition == \"images\"])\n    g.update(VISR=[r for r in REG if paula.REGION_AREA[r] == \"VIS\"], THR=[r for r in REG if paula.REGION_AREA[r] == \"TH\"],\n             HPR=[r for r in REG if paula.REGION_AREA[r] == \"HP\"], MBR=[r for r in REG if paula.REGION_AREA[r] == \"MB\"])\n    g.update(iu=np.triu_indices(len(REG), 1), AREA_OF=np.array([paula.REGION_AREA[r] for r in REG]))\n    g.update(CACHE[ur])\n    print(f\"--- units={ur}\" + (\" (adopted)\" if ur == MAIN else \" (variant)\"))\n\ndef verdict(claim, ur, v):\n    OUT.setdefault(claim, {})[ur] = v\n\ndef within(x, lo, hi):\n    return (x >= lo - 1e-12) & (x <= hi + 1e-12)\n\ndef widen(lo, hi):\n    return lo - 0.1 * abs(lo), hi + 0.1 * abs(hi)\n\ndef tol(x, v, t):\n    return abs(x - v) <= t + 1e-12\n\ndef REG_OF(d):\n    return [r for r in paula.REGION_ORDER if r in set(d.region)]\n'''\n\nC[13] = r'''RANGES_CV = {\"VIS\": (0.40, 0.59), \"TH\": (0.27, 0.37), \"HP\": (0.25, 0.49), \"MB\": (0.16, 0.45)}\nIQR_CV = {\"VIS\": (0.12, 0.18), \"TH\": (0.10, 0.15), \"HP\": (0.08, 0.13), \"MB\": (0.05, 0.23)}\n\ndef cv_medians(act):\n    g = act.groupby(\"region\").cv\n    t = pd.DataFrame({\"median\": g.median(), \"iqr\": g.quantile(0.75) - g.quantile(0.25), \"windows\": g.size()}).reindex(REG_OF(act))\n    t[\"area\"] = [paula.REGION_AREA[r] for r in t.index]\n    return t\n\ndef judge_fig1c(t, label):\n    ok_all, ok_iqr = True, True\n    for a, (lo, hi) in RANGES_CV.items():\n        x = t[t.area == a]\n        wl, wh = widen(lo, hi)\n        inside = within(x[\"median\"], wl, wh)\n        ext = tol(x[\"median\"].min(), lo, 0.1 * lo) and tol(x[\"median\"].max(), hi, 0.1 * hi)\n        il, ih = widen(*IQR_CV[a])\n        iqr_in = within(x[\"iqr\"], il, ih)\n        print(f\"{label} {a}: medians {x['median'].min():.3f} to {x['median'].max():.3f} (expected {lo} to {hi}); inside widened range {int(inside.sum())}/{len(x)}; \"\n              f\"extremes within tolerance {ext}; IQR {x['iqr'].min():.3f} to {x['iqr'].max():.3f}, inside {int(iqr_in.sum())}/{len(x)}\")\n        ok_all &= bool(inside.all()) and ext\n        ok_iqr &= bool(iqr_in.all())\n    hp = t[t.area == \"HP\"][\"median\"]\n    print(f\"{label}: highest hippocampal median is {hp.idxmax()} ({hp.max():.3f}); medians and extremes all match: {ok_all}; IQRs all match: {ok_iqr}\")\n    return ok_all and hp.idxmax() == \"DG\", ok_iqr\n\nfam = set(metas.session_index[metas.image_set == \"G\"])\nfor ur in UNITS:\n    use(ur)\n    t = cv_medians(ACT)\n    print(t.round(3).T.to_string())\n    ok_m, ok_i = judge_fig1c(t, f\"units={ur}\")\n    verdict(\"fig1c-cv-region-medians\", ur, \"reproduced\" if ok_m and ok_i else \"partially_reproduced\" if ok_m else \"not_reproduced\")\n    # by session group: the paper's sessions are not identified, so the result is also given for familiar and novel image sets\n    for name, ss in [(\"image set G\", fam), (\"image set H\", set(metas.session_index) - fam)]:\n        x = ACT[ACT.session.isin(ss)].groupby(\"area\").cv.median()\n        print(name, \"area medians:\", x.round(3).to_dict())\nprint(OUT[\"fig1c-cv-region-medians\"])\n'''\n\nC[16] = r'''RATIO = {\"VIS\": (2, 3), \"TH\": (1.3, 1.6), \"HP\": (1.5, 2.2), \"MB\": (1.3, 1.9)}\n\ndef surrogate_check(act, sfx, verbose):\n    g = act.groupby(\"region\")\n    t = pd.DataFrame({\"emp\": g.cv.median(), \"surr\": g[\"s_cv\" + sfx].median()}).reindex(REG_OF(act))\n    t[\"ratio\"] = t.emp / t.surr\n    t[\"area\"] = [paula.REGION_AREA[r] for r in t.index]\n    p_sub = {r: stats.mannwhitneyu(x.cv.dropna(), x[\"s_cv\" + sfx].dropna()).pvalue for r, x in g}\n    t[\"p\"] = pd.Series(p_sub)\n    ok_ratio = True\n    for a, (lo, hi) in RATIO.items():\n        wl, wh = widen(lo, hi)\n        x = t[t.area == a]\n        ok_ratio &= bool(within(x.ratio, wl, wh).all())\n        if verbose:\n            print(f\"{a}: ratios {x.ratio.min():.2f} to {x.ratio.max():.2f} (expected {lo} to {hi}, widened {wl:.2f} to {wh:.2f}); inside {int(within(x.ratio, wl, wh).sum())}/{len(x)}\")\n    vs = t[t.area == \"VIS\"].surr\n    ok_vs = bool(within(vs, 0.189, 0.264).all())\n    pa = {}\n    for a, x in act.groupby(\"area\"):\n        pa[a] = (stats.mannwhitneyu(x.cv.dropna(), x[\"s_cv\" + sfx].dropna()).pvalue, x.cv.median() > x[\"s_cv\" + sfx].median())\n    ok_sub = bool((t.p < 0.001).all() and (t.emp > t.surr).all())\n    ok_area = all(p < 0.001 and hi for p, hi in pa.values())\n    if verbose:\n        print(t.round(4).T.to_string())\n        print(f\"VIS surrogate medians {vs.min():.3f} to {vs.max():.3f} (0.189 to 0.264): {ok_vs}\")\n        print(\"per area Mann-Whitney:\", {a: (f\"{p:.1e}\", bool(h)) for a, (p, h) in pa.items()})\n        print(f\"tests hold per subregion: {ok_sub}; per area: {ok_area}; all ratios inside: {ok_ratio}; largest subregion p {t.p.max():.1e}\")\n        # windows are not independent: the same comparison on one value per population (its median over windows), Wilcoxon signed-rank\n        pm = act.groupby([\"area\", \"session\", \"region\"])[[\"cv\", \"s_cv\" + sfx]].median()\n        print(\"per-population medians, Wilcoxon signed-rank by area:\",\n              {a: f\"{stats.wilcoxon(x.cv, x['s_cv' + sfx]).pvalue:.1e} (n={len(x)}, empirical higher in {int((x.cv > x['s_cv' + sfx]).sum())})\" for a, x in pm.groupby(level=0)})\n    return t, ok_ratio, ok_vs, ok_sub, ok_area\n\nfor ur in UNITS:\n    use(ur)\n    t_, r_, v_, ps_, pa_ = surrogate_check(ACT, \"\", True)\n    verdict(\"fig1c-cv-above-surrogate\", ur, \"reproduced\" if r_ and v_ and (ps_ or pa_) else \"partially_reproduced\" if (ps_ or pa_) else \"not_reproduced\")\n    if ur == MAIN:\n        print(\"\\nfive seeds (claim seed, +1000, +2000, +3000, +4000):\")\n        for s in SFX:\n            t_, r_, v_, ps_, pa_ = surrogate_check(ACT, s, False)\n            print(f\"seed{s or ' (claim)'}: ratio range {t_.ratio.min():.3f} to {t_.ratio.max():.3f}; VIS surrogate medians {t_[t_.area=='VIS'].surr.min():.4f} to {t_[t_.area=='VIS'].surr.max():.4f}; \"\n                  f\"ratios inside {r_}; VIS surrogates inside {v_}; tests per subregion {ps_}, per area {pa_}; largest p {t_.p.max():.1e}; \"\n                  f\"HP ratios {t_[t_.area=='HP'].ratio.round(2).to_dict()}\")\nprint(OUT[\"fig1c-cv-above-surrogate\"])\n'''\n\nC[19] = r'''CVS = pd.DataFrame(cv10_list).sort_values([\"session\", \"region\", \"k\"])\nCORR = {}\n\ndef corr_mats(series, by_sess, which):\n    n = len(REG)\n    ca, cb, ns = (np.full((n, n), np.nan) for _ in range(3))\n    for i in range(n):\n        for j in range(i + 1, n):\n            xs, ys, rs = [], [], []\n            for s, rr in by_sess.items():\n                if REG[i] in rr and REG[j] in rr:\n                    x, y = series[(s, REG[i])][which], series[(s, REG[j])][which]\n                    ok = np.isfinite(x) & np.isfinite(y)\n                    if ok.sum() > 2 and x[ok].std() > 0 and y[ok].std() > 0:\n                        xs.append(x[ok]); ys.append(y[ok]); rs.append(np.corrcoef(x[ok], y[ok])[0, 1])\n            if xs:\n                ca[i, j] = ca[j, i] = np.corrcoef(np.concatenate(xs), np.concatenate(ys))[0, 1]\n                cb[i, j] = cb[j, i] = np.mean(rs)\n                ns[i, j] = ns[j, i] = len(rs)\n    f = lambda m: pd.DataFrame(m, index=REG, columns=REG)\n    return f(ca), f(cb), f(ns)\n\nfor ur in UNITS:\n    use(ur)\n    cvs = CVS[(CVS.units == ur) & CVS.region.isin(REG)]\n    scols = [\"s_cv10\" + x for x in SFXU]\n    series = {}\n    for (s, r), g in cvs.groupby([\"session\", \"region\"]):\n        series[(s, r)] = [np.concatenate(list(g.cv10))] + [np.concatenate(list(g[c])) for c in scols]\n    by_sess = {}\n    for (s, r) in series:\n        by_sess.setdefault(s, []).append(r)\n    EMP_A, EMP_B, NSH = corr_mats(series, by_sess, 0)\n    SUR_A, SUR_B, _ = corr_mats(series, by_sess, 1)\n    CORR[ur] = {\"EMP_A\": EMP_A, \"EMP_B\": EMP_B, \"SUR_A\": SUR_A, \"SUR_B\": SUR_B}\n    print(\"pairs with at least one shared session:\", int(np.isfinite(EMP_A.values[iu]).sum()), \"of\", len(iu[0]),\n          \"| shared sessions per pair: median\", np.nanmedian(NSH.values[iu]))\n    ok1d = {}\n    for lab, e, s in [(\"a\", EMP_A, SUR_A), (\"b\", EMP_B, SUR_B)]:\n        ev, sv = e.values[iu], s.values[iu]\n        ev, sv = ev[np.isfinite(ev)], sv[np.isfinite(sv)]\n        q = np.percentile(np.abs(sv), [50, 90, 99, 100])\n        ok1d[lab] = (ev.max() >= 0.45) and (np.abs(sv).max() < 0.2)\n        print(f\"reading {lab}: empirical r {ev.min():.3f} to {ev.max():.3f}, pairs >= 0.45: {int((ev >= 0.45).sum())}; \"\n              f\"surrogate |r| median {q[0]:.3f}, 90th {q[1]:.3f}, 99th {q[2]:.3f}, max {q[3]:.3f}; pairs with |r| > 0.2: {int((np.abs(sv) > 0.2).sum())}; passes {ok1d[lab]}\")\n    verdict(\"fig1d-surrogate-abolishes-cv-correlations\", ur, \"reproduced\" if all(ok1d.values()) else \"not_reproduced\")\n    if ur == MAIN:\n        fig, ax = plt.subplots(1, 2, figsize=(13, 5.5))\n        for a_, (lab, e, s) in zip(ax, [(\"a\", EMP_A, SUR_A), (\"b\", EMP_B, SUR_B)]):\n            m = np.tril(e.values, -1) + np.triu(s.values, 1)\n            im = a_.imshow(m, vmin=-0.7, vmax=0.7, cmap=\"RdBu_r\")\n            a_.set_xticks(range(len(REG)), REG, rotation=90, fontsize=7); a_.set_yticks(range(len(REG)), REG, fontsize=7)\n            a_.set_title(f\"reading {lab}: lower empirical, upper surrogate\")\n        plt.colorbar(im, ax=ax); plt.show()\n        print(\"colour scale -0.7 to 0.7; values outside it:\", int((np.abs(np.r_[EMP_A.values[iu], EMP_B.values[iu], SUR_A.values[iu], SUR_B.values[iu]]) > 0.7).sum()))\n        for k, sfx in enumerate(SFX[1:], start=2):\n            sa, sb, _ = corr_mats(series, by_sess, k)\n            va, vb = np.abs(sa.values[iu]), np.abs(sb.values[iu])\n            print(f\"surrogate seed{sfx}: max |r| reading a {np.nanmax(va):.3f} (pairs > 0.2: {int((va > 0.2).sum())}), reading b {np.nanmax(vb):.3f} (pairs > 0.2: {int((vb > 0.2).sum())})\")\nprint(OUT[\"fig1d-surrogate-abolishes-cv-correlations\"])\n'''\n\nC[22] = r'''def pairs_table(m):\n    rows = [(REG[i], REG[j], m.values[i, j]) for i, j in zip(*iu) if np.isfinite(m.values[i, j])]\n    p = pd.DataFrame(rows, columns=[\"r1\", \"r2\", \"r\"])\n    p[\"same_area\"] = [paula.REGION_AREA[a] == paula.REGION_AREA[b] for a, b in zip(p.r1, p.r2)]\n    return p\n\nfor ur in UNITS:\n    use(ur)\n    ok1e = {}\n    for lab in [\"a\", \"b\"]:\n        p = pairs_table(CORR[ur][\"EMP_\" + lab.upper()])\n        top = p.nlargest(int(round(0.1 * len(p))), \"r\")\n        lo_ok, hi_ok = tol(top.r.min(), 0.50, 0.05), tol(top.r.max(), 0.67, 0.067)\n        frac = top.same_area.mean()\n        ok1e[lab] = lo_ok and hi_ok and frac > 0.5\n        print(f\"reading {lab}: top {len(top)} of {len(p)} pairs, r {top.r.min():.4f} to {top.r.max():.4f} (expected 0.50 to 0.67; low end within tolerance {lo_ok}, high end {hi_ok}); \"\n              f\"same major area {int(top.same_area.sum())}/{len(top)} ({frac:.2f}); passes {ok1e[lab]}\")\n        print(\"   \", \"; \".join(f\"{a}-{b} {r:.2f}\" for a, b, r in top[[\"r1\", \"r2\", \"r\"]].values))\n    verdict(\"fig1e-positive-cv-modules\", ur, \"reproduced\" if any(ok1e.values()) else \"not_reproduced\")\nprint(OUT[\"fig1e-positive-cv-modules\"])\n'''\n\nC[25] = r'''for ur in UNITS:\n    use(ur)\n    ok1h = {}\n    for lab in [\"a\", \"b\"]:\n        p = pairs_table(CORR[ur][\"EMP_\" + lab.upper()])\n        neg = p.nsmallest(int(round(0.1 * len(p))), \"r\")\n        cnt = pd.Series(list(neg.r1) + list(neg.r2)).value_counts()\n        top2 = set(cnt.index[:2])\n        tie = cnt.iloc[1] == cnt.iloc[2] if len(cnt) > 2 else False\n        ok1h[lab] = top2 == {\"DG\", \"CA3\"} and tol(neg.r.min(), -0.27, 0.027)\n        print(f\"reading {lab}: {len(neg)} pairs, r {neg.r.min():.3f} to {neg.r.max():.3f} (most negative expected -0.27 +/- 0.027); \"\n              f\"appearances {cnt.head(6).to_dict()}; tie for second place {tie}; passes {ok1h[lab]}\")\n    verdict(\"fig1e-dg-ca3-anticorrelation-hubs\", ur, \"reproduced\" if any(ok1h.values()) else \"not_reproduced\")\nprint(OUT[\"fig1e-dg-ca3-anticorrelation-hubs\"])\n'''\n\nC[28] = r'''lo_n, hi_n = widen(-0.04, 0.03)\nfor ur in UNITS:\n    use(ur)\n    ok1m = {}\n    for lab in [\"a\", \"b\"]:\n        m = CORR[ur][\"EMP_\" + lab.upper()]\n        mm = m.abs().mean(axis=1)\n        area_mean = mm.groupby([paula.REGION_AREA[r] for r in mm.index]).mean()\n        p = pairs_table(m)\n        mbp = p[[paula.REGION_AREA[a] == \"MB\" or paula.REGION_AREA[b] == \"MB\" for a, b in zip(p.r1, p.r2)]]\n        near = within(mbp.r, lo_n, hi_n).mean()\n        ok1m[lab] = area_mean.idxmin() == \"MB\" and near > 0.5\n        print(f\"reading {lab}: mean |r| by area {area_mean.round(3).to_dict()}; per MB subregion {mm[MBR].round(3).to_dict()}; \"\n              f\"MB pairs in {lo_n:.3f} to {hi_n:.3f}: {int(within(mbp.r, lo_n, hi_n).sum())}/{len(mbp)} ({near:.2f}); passes {ok1m[lab]}\")\n    verdict(\"fig1e-midbrain-weakest-cv-correlations\", ur, \"reproduced\" if any(ok1m.values()) else \"not_reproduced\")\nprint(OUT[\"fig1e-midbrain-weakest-cv-correlations\"])\n'''\n"
}
```

```
File created successfully at: /tmp/claude-1001/cells_a.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/cells_b.py",
 "content": "C = {}\n\nC[31] = r'''def med_table(value, Wd):\n    out = {}\n    for k, w in Wd.items():\n        out[k] = w.groupby([\"region\", \"condition\"])[value].median().unstack()[paula.CONDITIONS]\n    return pd.concat(out, axis=1).reindex([r for r in paula.REGION_ORDER if r in set(Wd[\"a/a\"].region)])\n\nfor ur in UNITS:\n    CACHE[ur][\"MED_CV\"] = med_table(\"cv\", WD[ur])\n    CACHE[ur][\"MED_C\"] = med_table(\"C\", WD[ur])\nprint(\"median CV, units=vbn:\\n\", CACHE[MAIN][\"MED_CV\"].round(3).to_string())\nfor ur in UNITS:\n    print(f\"windows per condition (units={ur}, reading a/a):\", WD[ur][\"a/a\"].condition.value_counts().to_dict())\n\ndef check_expected(med, exp, readings=None):\n    \"\"\"exp: list of (label, region, condition(s), kind, value, tolerance); returns per reading the passes.\"\"\"\n    res = {}\n    for rd in (readings or list(med.columns.levels[0])):\n        rows = []\n        for lab, reg, conds, kind, v, t in exp:\n            if reg not in med.index:\n                rows.append((lab, \"not kept\", v, False))\n                continue\n            vals = med.loc[reg, rd][conds] if isinstance(conds, list) else pd.Series({conds: med.loc[reg, (rd, conds)]})\n            if kind == \"each\":\n                ok = bool(all(tol(y, v, t) for y in vals))\n                x = f\"{vals.min():.3f}-{vals.max():.3f}\"\n            else:\n                x = {\"min\": vals.min(), \"max\": vals.max(), \"value\": vals.iloc[0]}[kind]\n                ok = tol(x, v, t)\n                x = round(float(x), 3)\n            rows.append((lab, x, v, ok))\n        res[rd] = rows\n    return res\n\ndef show_expected(res):\n    for rd, rows in res.items():\n        n = sum(r[3] for r in rows)\n        print(f\"reading {rd}: {n}/{len(rows)} within tolerance; \" + \"; \".join(f\"{l} {x} ({v})\" + (\"\" if ok else \" MISS\") for l, x, v, ok in rows))\n    return {rd: all(r[3] for r in rows) for rd, rows in res.items()}\n'''\n\nC[33] = r'''E2A = []\nfor r, vals in {\"VISp\": (0.59, 0.55, 0.29, 0.39), \"VISl\": (0.56, 0.46, 0.30, 0.46), \"VISal\": (0.55, 0.46, 0.30, 0.48)}.items():\n    for c, v in zip([\"active\", \"blanks\", \"spont\", \"images\"], vals):\n        E2A.append((f\"{r} {c}\", r, c, \"value\", v, 0.1 * v))\nfor ur in UNITS:\n    use(ur)\n    full = show_expected(check_expected(MED_CV, E2A))\n    orders = {}\n    for rd in W:\n        m = MED_CV[rd]\n        order = {r: bool(m.loc[r, \"active\"] > m.loc[r, \"images\"] > m.loc[r, \"spont\"] and m.loc[r, \"blanks\"] > m.loc[r, \"spont\"]) for r in [\"VISp\", \"VISl\", \"VISal\"]}\n        orders[rd] = all(order.values())\n        print(f\"reading {rd}: order active > images > spont and blanks > spont: {order}\")\n    verdict(\"fig2a-vis-cv-by-condition\", ur, \"reproduced\" if any(full.values()) else \"partially_reproduced\" if any(orders.values()) else \"not_reproduced\")\nprint(OUT[\"fig2a-vis-cv-by-condition\"])\n'''\n\nC[36] = r'''E2T = [(\"LP active\", \"LP\", \"active\", \"value\", 0.37, 0.037), (\"LP spont\", \"LP\", \"spont\", \"value\", 0.28, 0.028),\n       (\"LGd active\", \"LGd\", \"active\", \"value\", 0.32, 0.032), (\"LGd spont\", \"LGd\", \"spont\", \"value\", 0.23, 0.023)]\nfor ur in UNITS:\n    use(ur)\n    full = show_expected(check_expected(MED_CV, E2T))\n    red = {}\n    for rd in W:\n        d = (MED_CV[rd][\"active\"] - MED_CV[rd][\"spont\"])\n        red[rd] = bool(max(d['LP'], d['LGd']) < min(d['VISp'], d['VISl'], d['VISal']))\n        print(f\"reading {rd}: active minus spontaneous LP {d['LP']:.3f}, LGd {d['LGd']:.3f}; VISp {d['VISp']:.3f}, VISl {d['VISl']:.3f}, VISal {d['VISal']:.3f}; \"\n              f\"smaller in both thalamic nuclei than in all three visual areas: {red[rd]}\")\n    verdict(\"fig2a-thalamus-cv-by-condition\", ur, \"reproduced\" if any(full[rd] and red[rd] for rd in W) else \"not_reproduced\")\nprint(OUT[\"fig2a-thalamus-cv-by-condition\"])\n'''\n\nC[39] = r'''E2H = [(\"DG VD low\", \"DG\", VD, \"min\", 0.48, 0.048), (\"DG VD high\", \"DG\", VD, \"max\", 0.50, 0.05),\n       (\"CA3 VD low\", \"CA3\", VD, \"min\", 0.41, 0.041), (\"CA3 VD high\", \"CA3\", VD, \"max\", 0.42, 0.042),\n       (\"CA1 VD each\", \"CA1\", VD, \"each\", 0.25, 0.025),\n       (\"DG spont\", \"DG\", \"spont\", \"value\", 0.51, 0.051), (\"CA3 spont\", \"CA3\", \"spont\", \"value\", 0.43, 0.043)]\nfor ur in UNITS:\n    use(ur)\n    full = show_expected(check_expected(MED_CV, E2H))\n    up = {}\n    for rd in W:\n        m = MED_CV[rd]\n        up[rd] = bool(m.loc['DG', 'spont'] > m.loc['DG', VD].max() and m.loc['CA3', 'spont'] > m.loc['CA3', VD].max())\n        print(f\"reading {rd}: spontaneous above every visually driven median: DG {bool(m.loc['DG','spont'] > m.loc['DG', VD].max())}, CA3 {bool(m.loc['CA3','spont'] > m.loc['CA3', VD].max())}\")\n    verdict(\"fig2a-hippocampus-cv-stable\", ur, \"reproduced\" if any(full[rd] and up[rd] for rd in W) else \"not_reproduced\")\nprint(OUT[\"fig2a-hippocampus-cv-stable\"])\n'''\n\nC[42] = r'''E2M = [(\"APN each\", \"APN\", paula.CONDITIONS, \"each\", 0.16, 0.016), (\"MRN low\", \"MRN\", paula.CONDITIONS, \"min\", 0.20, 0.02),\n       (\"MRN high\", \"MRN\", paula.CONDITIONS, \"max\", 0.21, 0.021)]\nfor ur in UNITS:\n    use(ur)\n    full = show_expected(check_expected(MED_CV, E2M))\n    print(\"   MRN medians, reading a/a:\", MED_CV[\"a/a\"].loc[\"MRN\"].round(4).to_dict())\n    verdict(\"fig2a-midbrain-cv-invariant\", ur, \"reproduced\" if any(full.values()) else \"not_reproduced\")\nprint(OUT[\"fig2a-midbrain-cv-invariant\"])\n'''\n\nC[45] = r'''LN2 = np.log(2)\ndef js_all(Wd, value, regs):\n    \"\"\"Keys (condition reading, bins, log base): base 2 computed, natural log as bits x ln 2.\"\"\"\n    out = {}\n    for rd, w in Wd.items():\n        for nb in (50, 100):\n            m2 = {c: paula.js_matrix(w[w.condition == c], value, regs, nb) for c in paula.CONDITIONS}\n            out[(rd, nb, \"2\")] = m2\n            out[(rd, nb, \"e\")] = {c: m * LN2 for c, m in m2.items()}\n    return out\n\ndef pct_table(JS):\n    rows = []\n    for (rd, nb, base), mats in JS.items():\n        if base != \"2\":\n            continue  # percentage differences do not depend on the log base\n        for sm in (\"all\", \"adjacent\"):\n            for pm in (\"second\", \"mean\"):\n                for a in paula.AREAS:\n                    s = {c: paula.summed_js(mats[c], a, sm) for c in paula.CONDITIONS}\n                    for c1, c2 in paula.COND_PAIRS:\n                        rows.append({\"reading\": rd, \"bins\": nb, \"sum\": sm, \"pct\": pm, \"area\": a, \"pair\": f\"{c1}-{c2}\",\n                                     \"S1\": s[c1], \"S2\": s[c2], \"diff\": paula.pct_diff(s[c1], s[c2], pm)})\n    return pd.DataFrame(rows)\n\nfor ur in UNITS:\n    CACHE[ur][\"JS_CV\"] = js_all(WD[ur], \"cv\", REGS[ur])\n    CACHE[ur][\"PCT_CV\"] = pct_table(CACHE[ur][\"JS_CV\"])\nP = CACHE[MAIN][\"PCT_CV\"]\nprint(P[(P.reading == \"a/a\") & (P.bins == 50) & (P.pct == \"second\")].pivot_table(index=[\"sum\", \"area\"], columns=\"pair\", values=\"diff\").round(1).to_string())\nprint(\"summed JS (units=vbn, reading a/a, 50 bins, all pairs, bits):\", {a: {c: round(paula.summed_js(CACHE[MAIN][\"JS_CV\"][(\"a/a\", 50, \"2\")][c], a, \"all\"), 2) for c in paula.CONDITIONS} for a in paula.AREAS})\n'''\n\nC[47] = r'''FOUR = [\"images-active\", \"active-spont\", \"images-blanks\", \"blanks-spont\"]\nfor ur in UNITS:\n    use(ur)\n    res2b = []\n    for key, g in PCT_CV[PCT_CV.area == \"VIS\"].groupby([\"reading\", \"bins\", \"sum\", \"pct\"]):\n        d = g.set_index(\"pair\")[\"diff\"]\n        ab = d[\"active-blanks\"]\n        four = d[FOUR]\n        full = 0.5 <= ab <= 1.5 and bool(((four >= 27) & (four <= 33)).all())\n        part = d.idxmin() == \"active-blanks\" and bool((d.drop(\"active-blanks\") > 15).all())\n        res2b.append({\"reading\": key[0], \"bins\": key[1], \"sum\": key[2], \"pct\": key[3], \"active-blanks\": round(ab, 2),\n                      **{p: round(four[p], 1) for p in FOUR}, \"closest pair\": d.idxmin(), \"reproduced\": full, \"partial\": part})\n    res2b = pd.DataFrame(res2b)\n    print(res2b.to_string())\n    print(\"combinations reproduced:\", int(res2b.reproduced.sum()), \"| partial:\", int(res2b.partial.sum()), \"of\", len(res2b))\n    verdict(\"fig2b-vis-summed-js-cv\", ur, \"reproduced\" if res2b.reproduced.any() else \"partially_reproduced\" if res2b.partial.any() else \"not_reproduced\")\nprint(OUT[\"fig2b-vis-summed-js-cv\"])\n'''\n\nC[50] = r'''for ur in UNITS:\n    use(ur)\n    res2h = []\n    for key, g in PCT_CV.groupby([\"reading\", \"bins\", \"sum\", \"pct\"]):\n        t = g.pivot_table(index=\"area\", columns=\"pair\", values=\"diff\")\n        hp = t.loc[\"HP\"]\n        mb_max = t.loc[\"MB\"].max()\n        mb_small = int((t.idxmin(axis=0) == \"MB\").sum())\n        ok = tol(hp[\"active-spont\"], 15, 1.5) and hp.idxmax() == \"active-spont\" and mb_max <= 7.7 and mb_small >= 4\n        res2h.append({\"reading\": key[0], \"bins\": key[1], \"sum\": key[2], \"pct\": key[3], \"HP active-spont\": round(hp[\"active-spont\"], 1),\n                      \"HP largest pair\": hp.idxmax(), \"MB max\": round(mb_max, 1), \"pairs where MB smallest\": mb_small, \"reproduced\": ok})\n    res2h = pd.DataFrame(res2h)\n    print(res2h.to_string())\n    print(\"combinations reproduced:\", int(res2h.reproduced.sum()), \"of\", len(res2h))\n    verdict(\"fig2b-hp-mb-summed-js-cv\", ur, \"reproduced\" if res2h.reproduced.any() else \"not_reproduced\")\nprint(OUT[\"fig2b-hp-mb-summed-js-cv\"])\n'''\n\nC[53] = r'''VDP = [\"images-active\", \"images-blanks\", \"active-blanks\"]\nfor ur in UNITS:\n    use(ur)\n    r = PCT_CV[(PCT_CV.area == \"VIS\") & PCT_CV.pair.isin(VDP)].pivot_table(index=[\"reading\", \"bins\", \"sum\", \"pct\"], columns=\"pair\", values=\"diff\")\n    r[\"n at most 4.4%\"] = (r[VDP] <= 4.4).sum(axis=1)\n    r[\"reproduced\"] = r[\"n at most 4.4%\"] >= 2\n    print(r.round(1).to_string())\n    print(\"combinations reproduced (percentage reading):\", int(r.reproduced.sum()), \"of\", len(r))\n    vi = np.triu_indices(len(VISR), 1)\n    js_pass = []\n    for (rd, nb, base), mats in JS_CV.items():\n        fr = {c: float((mats[c].loc[VISR, VISR].values[vi] <= 0.22).mean()) for c in VD}\n        js_pass.append(all(v > 0.5 for v in fr.values()))\n        print(f\"JS reading, {rd}, {nb} bins, log base {base}: fraction of VIS-VIS pairs at most 0.22: {({k: round(v, 2) for k, v in fr.items()})}; \"\n              f\"VIS-VIS JS range {min(mats[c].loc[VISR, VISR].values[vi].min() for c in VD):.3f} to {max(mats[c].loc[VISR, VISR].values[vi].max() for c in VD):.3f}; passes {js_pass[-1]}\")\n    verdict(\"fig2b-visually-driven-js-cv-low\", ur, \"reproduced\" if r.reproduced.any() else \"partially_reproduced\" if any(js_pass) else \"not_reproduced\")\nprint(OUT[\"fig2b-visually-driven-js-cv-low\"])\n'''\n\nC[56] = r'''for ur in UNITS:\n    use(ur)\n    passes = []\n    for variant, others in [(\"all other subregions\", None), (\"other hippocampal subregions\", HPR)]:\n        for (rd, nb, base), mats in JS_CV.items():\n            med = {}\n            for reg in [\"DG\", \"CA3\"]:\n                for c in paula.CONDITIONS:\n                    row = mats[c].loc[reg].drop(reg)\n                    if others:\n                        row = row[[o for o in others if o != reg]]\n                    med[(reg, c)] = row.median()\n            ok = (tol(med[(\"DG\", \"spont\")], 0.84, 0.084) and tol(med[(\"CA3\", \"spont\")], 0.84, 0.084) and tol(med[(\"DG\", \"blanks\")], 0.63, 0.063)\n                  and tol(med[(\"CA3\", \"blanks\")], 0.63, 0.063)\n                  and all(med[(g, \"spont\")] == max(med[(g, c)] for c in paula.CONDITIONS) for g in [\"DG\", \"CA3\"]))\n            passes.append(ok)\n            print(f\"{variant}, {rd}, {nb} bins, base {base}: \" + \", \".join(f\"{g} {c} {v:.3f}\" for (g, c), v in med.items()) + f\"; passes {ok}\")\n    verdict(\"fig2b-dg-ca3-high-js-cv\", ur, \"reproduced\" if any(passes) else \"not_reproduced\")\nprint(OUT[\"fig2b-dg-ca3-high-js-cv\"])\n'''\n\nC[59] = r'''def legend_values(rd, nb, base):\n    w = W[rd]\n    out = {}\n    for reg in REG:\n        x = w[w.region == reg]\n        out[reg] = {f\"{c1}-{c2}\": paula.js_divergence(x[x.condition == c1].cv, x[x.condition == c2].cv, nb, base=2.0 if base == \"2\" else np.e)\n                    for c1, c2 in paula.COND_PAIRS}\n    a = pd.DataFrame(out).T\n    mats = JS_CV[(rd, nb, base)]\n    b = pd.DataFrame({reg: {f\"{c1}-{c2}\": float((mats[c1].loc[reg].drop(reg) - mats[c2].loc[reg].drop(reg)).abs().mean()) for c1, c2 in paula.COND_PAIRS} for reg in REG}).T\n    return a, b\n\nSVD = [\"images-spont\", \"active-spont\", \"blanks-spont\"]\nfor ur in UNITS:\n    use(ur)\n    res_leg = []\n    for rd in W:\n        for nb in (50, 100):\n            for base in (\"2\", \"e\"):\n                for lab, t in zip([\"a\", \"b\"], legend_values(rd, nb, base)):\n                    sv = t[SVD].mean(axis=1)\n                    dgca3 = t.loc[[\"DG\", \"CA3\"]].values.ravel()\n                    res_leg.append({\"reading\": rd, \"bins\": nb, \"base\": base, \"measure\": lab,\n                                    \"VIS > 0.44\": f\"{int((sv[VISR] > 0.44).sum())}/{len(VISR)}\", \"TH > 0.33\": f\"{int((sv[THR] > 0.33).sum())}/{len(THR)}\",\n                                    \"DG, CA3 range\": f\"{dgca3.min():.3f}-{dgca3.max():.3f}\", \"MB < 0.165\": f\"{int((t.loc[MBR].values < 0.165).sum())}/{t.loc[MBR].size}\",\n                                    \"passes\": bool((sv[VISR] > 0.44).mean() > 0.5 and (sv[THR] > 0.33).mean() > 0.5 and within(dgca3, 0.135, 0.385).all() and (t.loc[MBR].values < 0.165).mean() > 0.5)})\n                    if rd == \"a/a\" and nb == 50 and base == \"2\" and ur == MAIN:\n                        print(f\"measure {lab}, reading a/a, 50 bins:\\n\", t.round(3).T.to_string())\n    res_leg = pd.DataFrame(res_leg)\n    print(res_leg.to_string())\n    verdict(\"fig2b-legend-js-cv\", ur, \"reproduced\" if res_leg.passes.any() else \"not_reproduced\")\nprint(OUT[\"fig2b-legend-js-cv\"])\n'''\n"
}
```

```
File created successfully at: /tmp/claude-1001/cells_b.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/cells_c.py",
 "content": "C = {}\n\nC[62] = r'''rng3 = np.random.default_rng(zlib.crc32(b\"paula-2026/fig3a-reference-systems\"))\nN3, DROP = 100_000, 1_000\ndef logistic(r, n=N3 + DROP, x=0.4):\n    out = np.empty(n)\n    for i in range(n):\n        x = r * x * (1 - x); out[i] = x\n    return out[DROP:]\ndef tent(mu, n=N3 + DROP, x=0.3141):\n    out = np.empty(n)\n    for i in range(n):\n        x = mu * x if x < 0.5 else mu * (1 - x); out[i] = x\n    return out[DROP:]\ndef ikeda(p, u=0.9, n=N3 + DROP):\n    x = y = 0.1; out = np.empty(n)\n    for i in range(n):\n        t = p - 6 / (1 + x * x + y * y)\n        x, y = 1 + u * (x * np.cos(t) - y * np.sin(t)), u * (x * np.sin(t) + y * np.cos(t)); out[i] = x\n    return out[DROP:]\ndef corr_walk(alpha, n=N3):\n    K = int(np.floor(100 * alpha)) + 1\n    w = np.exp(-np.arange(K) / (K * alpha)); w /= w.sum()\n    e = rng3.standard_normal(n + K)\n    return np.cumsum(np.convolve(e, w, mode=\"valid\")[:n])\ndef fk_noise(k, n=N3):\n    f = np.fft.rfftfreq(n); amp = np.zeros_like(f); amp[1:] = f[1:] ** (-k / 2)\n    ph = np.exp(2j * np.pi * rng3.random(len(f)))\n    return np.fft.irfft(amp * ph, n)\nIK_CHAOS = [0.4 + 2 * np.pi, 0.4 + 4 * np.pi]  # the usual chaotic Ikeda parameter 0.4, shifted by the map's period 2 pi into [5, 17]\nSINE_PP = [100, 1000, 10_000]\nref = []\nref.append((\"white noise\", \"\", *paula.bandt_pompe(rng3.standard_normal(N3))))\nfor pp in SINE_PP:\n    ref.append((\"sine\", f\"{pp} points per period\", *paula.bandt_pompe(np.sin(2 * np.pi * np.arange(N3) / pp))))\nref.append((\"Brownian motion\", \"\", *paula.bandt_pompe(np.cumsum(rng3.standard_normal(N3)))))\nfor a in [0.01, 0.05, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0]:\n    ref.append((\"exp. correlated walk\", f\"alpha={a}\", *paula.bandt_pompe(corr_walk(a))))\nfor r in [3.5, 3.6, 3.7, 3.8, 3.9, 4.0]:\n    ref.append((\"logistic\", f\"r={r}\", *paula.bandt_pompe(logistic(r))))\nfor mu in [1.2, 1.4, 1.6, 1.8, 1.9999]:\n    ref.append((\"tent\", f\"mu={mu}\", *paula.bandt_pompe(tent(mu))))\nfor p in [5, 6, 6.5, IK_CHAOS[0], 7, 8, 11, IK_CHAOS[1], 14, 17]:\n    ref.append((\"Ikeda\", f\"p={p:.3f}\", *paula.bandt_pompe(ikeda(p))))\nfor k in [0, 0.5, 1, 1.5, 2, 2.5, 3]:\n    ref.append((\"1/f^k noise\", f\"k={k}\", *paula.bandt_pompe(fk_noise(k))))\nREF = pd.DataFrame(ref, columns=[\"system\", \"parameter\", \"H\", \"C\"])\nprint(REF.round(4).to_string())\ng = lambda s, p: REF[(REF.system == s) & (REF.parameter == p)].iloc[0]\nH_FLOOR = np.log(2) / np.log(720)  # a sine gives at least two ordinal patterns (rising and falling)\nwn = g(\"white noise\", \"\")\nok_wn = wn.H >= 0.9 and wn.C <= 0.05\nprint(f\"white noise H {wn.H:.3f} C {wn.C:.4f}: {ok_wn}\")\nok_sn = {}\nfor pp in SINE_PP:\n    sn = g(\"sine\", f\"{pp} points per period\")\n    ok_sn[pp] = bool(sn.H <= H_FLOOR + 0.05 and within(sn.C, 0.09, 0.11))\n    print(f\"sine, {pp} points per period: H {sn.H:.4f} (floor {H_FLOOR:.4f}; near 0 read as at most floor + 0.05 = {H_FLOOR + 0.05:.3f}), C {sn.C:.4f} (0.09 to 0.11): {ok_sn[pp]}\")\nwalks = REF[REF.system == \"exp. correlated walk\"]\new = walks[within(walks.H, 0.27, 0.66)]\nok_ew = len(ew) > 0 and bool(within(ew.C, 0.27, 0.55).all())\nprint(f\"exp. correlated walk: {len(ew)} of 8 alphas with H in 0.27 to 0.66, their C {ew.C.min():.3f} to {ew.C.max():.3f}, inside 0.27 to 0.55 {int(within(ew.C, 0.27, 0.55).sum())}; \"\n      f\"all walks H {walks.H.min():.3f} to {walks.H.max():.3f}: {ok_ew}\")\nchaos = pd.DataFrame([g(\"logistic\", \"r=4.0\"), g(\"tent\", \"mu=1.9999\"), g(\"Ikeda\", f\"p={IK_CHAOS[0]:.3f}\"), g(\"Ikeda\", f\"p={IK_CHAOS[1]:.3f}\")])\nchaos[\"inside\"] = within(chaos.C, 0.36, 0.55) & within(chaos.H, 0.45, 0.88)\nok_ch = bool(chaos.inside.all())\nprint(\"chaotic maps at chaotic parameters (Ikeda at 0.4 + 2 pi and 0.4 + 4 pi):\\n\", chaos.round(3).to_string(), \"\\n inside C 0.36 to 0.55 and H 0.45 to 0.88:\", ok_ch)\nik = REF[REF.system == \"Ikeda\"]\nprint(\"Ikeda sweep: inside the chaotic range at\", list(ik.parameter[within(ik.C, 0.36, 0.55) & within(ik.H, 0.45, 0.88)]))\nprint(\"parts that hold: white noise\", ok_wn, \"| sine at some sampling\", any(ok_sn.values()), \"| correlated walk\", ok_ew, \"| chaotic maps\", ok_ch)\nOUT[\"fig3a-reference-systems\"] = {\"synthetic\": \"reproduced\" if ok_wn and any(ok_sn.values()) and ok_ew and ok_ch else\n                                  \"partially_reproduced\" if (ok_wn or ok_ch) else \"not_reproduced\"}\nfig, ax = plt.subplots(figsize=(6, 4.5))\nfor s, gg in REF.groupby(\"system\"):\n    ax.plot(gg.H, gg.C, \"o-\" if len(gg) > 1 else \"o\", label=s, ms=4)\nax.set_xlabel(\"H\"); ax.set_ylabel(\"C\"); ax.set_xlim(0, 1); ax.set_ylim(0, 0.55); ax.legend(fontsize=7); plt.show()\nprint(\"plotted H range\", REF.H.min().round(3), REF.H.max().round(3), \"C range\", REF.C.min().round(3), REF.C.max().round(3))\nprint(OUT[\"fig3a-reference-systems\"])\n'''\n\nC[65] = r'''def fig3b(w, label):\n    tc = w.groupby([\"area\", \"k\"]).C.agg([\"mean\", \"sem\", \"size\"]).reset_index()\n    piv = tc.pivot(index=\"k\", columns=\"area\", values=\"mean\")\n    means = piv.mean()\n    ok_v = all(within(means[a], 0.117, 0.165) for a in [\"VIS\", \"HP\"])\n    ok_t, ok_m = tol(means[\"TH\"], 0.11, 0.011), tol(means[\"MB\"], 0.10, 0.01)\n    order = (piv.MB < piv.TH) & (piv.TH < piv.VIS) & (piv.TH < piv.HP)\n    print(f\"{label}: mean over windows {means.round(4).to_dict()}; VIS and HP in 0.117 to 0.165 {ok_v}; TH {ok_t}; MB {ok_m}; \"\n          f\"order MB < TH < VIS and HP at {int(order.sum())} of {len(order)} indices; range over indices {piv.min().round(3).to_dict()} to {piv.max().round(3).to_dict()}; \"\n          f\"largest standard error {tc['sem'].max():.4f}\")\n    return piv, ok_v and ok_t and ok_m and bool(order.all()), ok_v and ok_t and ok_m and order.mean() > 0.5\nfor ur in UNITS:\n    use(ur)\n    piv_a, full_a, part_a = fig3b(ACT, \"reading a (active)\")\n    piv_b, full_b, part_b = fig3b(IMG, \"reading b (images)\")\n    verdict(\"fig3b-complexity-levels-by-region\", ur, \"reproduced\" if full_a or full_b else \"partially_reproduced\" if part_a or part_b else \"not_reproduced\")\n    if ur == MAIN:\n        fig, ax = plt.subplots(figsize=(7, 3.5))\n        for a in paula.AREAS:\n            ax.plot(piv_a.index, piv_a[a], label=a)\n        ax.set_xlabel(\"active window index\"); ax.set_ylabel(\"mean C\"); ax.legend(); plt.show()\nprint(OUT[\"fig3b-complexity-levels-by-region\"])\n'''\n\nC[68] = r'''SPAN = {\"VIS\": ((0.8, 1.0), (0.1, 0.4)), \"TH\": ((0.75, 0.95), (0.05, 0.25)), \"HP\": ((0.85, 1.0), (0.05, 0.4)), \"MB\": ((0.9, 1.0), (0.05, 0.2))}\nNPTS = {\"VIS\": 21084, \"TH\": 11265, \"HP\": 13059, \"MB\": 6296}\ndef ch_table(w, sfxs, surr=True):\n    \"\"\"Spans unrounded (rounded only for printing); Mann-Whitney on windows, and Wilcoxon on per-population medians.\"\"\"\n    rows = []\n    for a in paula.AREAS:\n        x = w[w.area == a]\n        r = {\"area\": a, \"windows\": len(x), \"paper windows\": NPTS[a]}\n        for q, (lo, hi) in [(\"95\", (2.5, 97.5)), (\"100\", (0, 100))]:\n            r[f\"H span {q}\"] = tuple(np.percentile(x.H, [lo, hi]))\n            r[f\"C span {q}\"] = tuple(np.percentile(x.C, [lo, hi]))\n        if surr:\n            r[\"surrogate median C\"] = x.s_C.median()\n            r[\"empirical median C\"] = x.C.median()\n            for s in sfxs:\n                r[\"p\" + s] = stats.mannwhitneyu(x.C, x[\"s_C\" + s]).pvalue\n                r[\"surr med\" + s] = x[\"s_C\" + s].median()\n            pm = x.groupby([\"session\", \"region\"])[[\"C\", \"s_C\"]].median()\n            r[\"p populations (Wilcoxon)\"] = stats.wilcoxon(pm.C, pm.s_C).pvalue\n            r[\"populations\"] = len(pm)\n        rows.append(r)\n    return pd.DataFrame(rows).set_index(\"area\")\ndef show_ch(t):\n    return t.apply(lambda col: col.map(lambda v: tuple(round(float(u), 3) for u in v) if isinstance(v, tuple) else v)).T.to_string()\nfor ur in UNITS:\n    use(ur)\n    CACHE[ur][\"CH\"] = ch_table(ACT, SFXU)\n    print(show_ch(CACHE[ur][\"CH\"]))\n    if ur == MAIN:\n        print(\"\\nnatural-image windows:\\n\", show_ch(ch_table(IMG, SFXU, surr=False)))\n\ndef judge_ch(a, q=\"95\"):\n    (hl, hh), (cl, ch) = SPAN[a]\n    H0, H1 = CH.loc[a, f\"H span {q}\"]; C0, C1 = CH.loc[a, f\"C span {q}\"]\n    hw, cw = widen(hl, hh), widen(cl, ch)\n    span_ok = hw[0] <= H0 and H1 <= hw[1] and cw[0] <= C0 and C1 <= cw[1]\n    test_ok = CH.loc[a, \"p\"] < 0.001 and CH.loc[a, \"empirical median C\"] > CH.loc[a, \"surrogate median C\"]\n    width = {b: CH.loc[b, f\"C span {q}\"][1] - CH.loc[b, f\"C span {q}\"][0] for b in paula.AREAS}\n    print(f\"{a}, span {q}: H {H0:.4f}-{H1:.4f} within {hw[0]:.3f}-{hw[1]:.3f}, C {C0:.4f}-{C1:.4f} within {cw[0]:.3f}-{cw[1]:.3f}: {span_ok}; \"\n          f\"Mann-Whitney p {CH.loc[a, 'p']:.1e} (seeds run: {len(SFXU)}, largest {max(CH.loc[a, 'p' + s] for s in SFXU):.1e}), empirical above surrogate {CH.loc[a, 'empirical median C'] > CH.loc[a, 'surrogate median C']}; \"\n          f\"per-population Wilcoxon p {CH.loc[a, 'p populations (Wilcoxon)']:.1e}; C span widths {({b: round(v, 3) for b, v in width.items()})}\")\n    return span_ok, test_ok, width\n'''\n\nC[70] = r'''for ur in UNITS:\n    use(ur)\n    res = {}\n    for q in [\"95\", \"100\"]:\n        res[q] = judge_ch(\"VIS\", q)\n    sm = [CH.loc[\"VIS\", \"surr med\" + s] for s in SFXU]\n    sm_ok = all(0.09 <= v <= 0.22 for v in sm)\n    print(f\"VIS surrogate median C over the seeds run {min(sm):.4f} to {max(sm):.4f}; inside 0.09 to 0.22: {sm_ok}\")\n    verdict(\"fig3c-vis-ch-plane\", ur, \"reproduced\" if res[\"95\"][0] and res[\"95\"][1] and sm_ok else \"not_reproduced\")\nprint(OUT[\"fig3c-vis-ch-plane\"])\n'''\n\nC[73] = r'''for ur in UNITS:\n    use(ur)\n    for q in [\"95\", \"100\"]:\n        s_ok, t_ok, wd = judge_ch(\"TH\", q)\n        print(f\"  span {q}: TH C span narrower than VIS: {wd['TH'] < wd['VIS']}\")\n        if q == \"95\":\n            verdict(\"fig3d-th-ch-plane\", ur, \"reproduced\" if s_ok and t_ok and wd[\"TH\"] < wd[\"VIS\"] else \"not_reproduced\")\nprint(OUT[\"fig3d-th-ch-plane\"])\n'''\n\nC[76] = r'''for ur in UNITS:\n    use(ur)\n    for q in [\"95\", \"100\"]:\n        s_ok, t_ok, wd = judge_ch(\"HP\", q)\n        print(f\"  span {q}: HP C span widest of the four: {max(wd, key=wd.get) == 'HP'}\")\n        if q == \"95\":\n            verdict(\"fig3e-hp-ch-plane\", ur, \"reproduced\" if s_ok and t_ok and max(wd, key=wd.get) == \"HP\" else \"not_reproduced\")\nprint(OUT[\"fig3e-hp-ch-plane\"])\n'''\n\nC[79] = r'''for ur in UNITS:\n    use(ur)\n    for q in [\"95\", \"100\"]:\n        s_ok, t_ok, wd = judge_ch(\"MB\", q)\n        print(f\"  span {q}: MB C span narrowest of the four: {min(wd, key=wd.get) == 'MB'}\")\n        if q == \"95\":\n            verdict(\"fig3f-mb-ch-plane\", ur, \"reproduced\" if s_ok and t_ok and min(wd, key=wd.get) == \"MB\" else \"not_reproduced\")\n    if ur == MAIN:\n        fig, ax = plt.subplots(1, 4, figsize=(16, 3.5), sharey=True)\n        for a_, a in zip(ax, paula.AREAS):\n            x = ACT[ACT.area == a]\n            a_.plot(x.H, x.C, \".\", ms=1, alpha=0.3); a_.plot(x.s_H, x.s_C, \".\", ms=1, alpha=0.3, color=\"k\")\n            a_.set_title(a); a_.set_xlim(0.5, 1); a_.set_ylim(0, 0.5); a_.set_xlabel(\"H\")\n        ax[0].set_ylabel(\"C\"); plt.show()\n        print(\"windows outside the axes (H < 0.5):\", int((ACT.H < 0.5).sum()), \"| C > 0.5:\", int((ACT.C > 0.5).sum()))\nprint(OUT[\"fig3f-mb-ch-plane\"])\n'''\n\nC[82] = r'''FR = [(\"VIS\", 0.3, 0.4, 0.8), (\"VIS\", 0.0, 0.1, 4.9), (\"TH\", 0.2, 0.3, 0.6), (\"TH\", 0.0, 0.1, 24.6),\n      (\"HP\", 0.3, 0.4, 2.7), (\"HP\", 0.0, 0.1, 9.5), (\"MB\", 0.1, 0.2, 45.4), (\"MB\", 0.0, 0.1, 54.0)]\nfor ur in UNITS:\n    use(ur)\n    best = 0\n    for lab, w in [(\"reading a (active)\", ACT), (\"reading b (images)\", IMG)]:\n        out, n = [], 0\n        for a, lo, hi, v in FR:\n            c = w[w.area == a].C\n            f = 100 * ((c >= lo) & ((c < hi) | ((hi == 0.4) & (c <= hi)))).mean()\n            ok = tol(f, v, 0.1 * v); n += ok\n            out.append(f\"{a} [{lo},{hi}) {f:.2f}% ({v})\" + (\"\" if ok else \" MISS\"))\n        best = max(best, n)\n        print(f\"{lab}: {n}/8 within tolerance; \" + \"; \".join(out))\n    verdict(\"fig3-complexity-range-fractions\", ur, \"reproduced\" if best == 8 else \"partially_reproduced\" if best >= 6 else \"not_reproduced\")\nprint(OUT[\"fig3-complexity-range-fractions\"])\n'''\n"
}
```

```
File created successfully at: /tmp/claude-1001/cells_c.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/cells_d.py",
 "content": "C = {}\n\nC[85] = r'''print(\"median C, units=vbn:\\n\", CACHE[MAIN][\"MED_C\"].round(3).to_string())\n\ndef mw_pairs(w, regs, bonf):\n    rows = []\n    for r in regs:\n        x = w[w.region == r]\n        for c1, c2 in paula.COND_PAIRS:\n            p = stats.mannwhitneyu(x[x.condition == c1].C, x[x.condition == c2].C).pvalue\n            rows.append({\"region\": r, \"pair\": f\"{c1}-{c2}\", \"p\": min(1.0, p * bonf)})\n    return pd.DataFrame(rows)\n'''\n\nC[87] = r'''LEG4A = {\"VISl\": (0.15, 0.26), \"VISal\": (0.15, 0.25), \"VISp\": (0.16, 0.19)}\nfor ur in UNITS:\n    use(ur)\n    full, ordr = False, False\n    for rd in W:\n        m = MED_C[rd].loc[VISR]\n        order = (m.images > m.active) & (m.images > m.blanks) & (m.active > m.spont) & (m.blanks > m.spont)\n        ordr |= bool(order.all())\n        ni = within(m.images, *widen(0.16, 0.26)); sp = within(m.spont, 0.09, 0.11); ab = within(m.active, *widen(0.1, 0.19)) & within(m.blanks, *widen(0.1, 0.19))\n        for name, bonf in [(\"uncorrected\", 1), (\"Bonferroni 36\", 36)]:\n            mw = mw_pairs(W[rd], VISR, bonf)\n            allp = bool((mw.p < 0.001).all())\n            ok = bool(order.all() and ni.all() and sp.all() and ab.all() and allp)\n            full |= ok\n            print(f\"reading {rd}, {name}: order holds in {int(order.sum())}/6 ({list(order[~order].index)} fail); images medians {m.images.min():.3f}-{m.images.max():.3f} inside {int(ni.sum())}/6; \"\n                  f\"spont {m.spont.min():.3f}-{m.spont.max():.3f} inside {int(sp.sum())}/6; active and blanks {min(m.active.min(), m.blanks.min()):.3f}-{max(m.active.max(), m.blanks.max()):.3f} inside {int(ab.sum())}/6; \"\n                  f\"tests p < 0.001 {int((mw.p < 0.001).sum())}/36, largest p {mw.p.max():.1e} ({mw.loc[mw.p.idxmax(), 'region']} {mw.loc[mw.p.idxmax(), 'pair']}); passes {ok}\")\n    verdict(\"fig4a-vis-complexity-by-condition\", ur, \"reproduced\" if full else \"partially_reproduced\" if ordr else \"not_reproduced\")\n    m = MED_C[\"a/a\"].loc[VISR]\n    print(\"medians, reading a/a:\\n\", m.round(3).to_string())\n    iq = W[\"a/a\"][W[\"a/a\"].region.isin(VISR)].groupby([\"region\", \"condition\"]).C.agg(lambda x: x.quantile(0.75) - x.quantile(0.25)).unstack()\n    print(\"IQRs (legend 0.08 to 0.12 in visually driven states):\\n\", iq.round(3).to_string())\n    for r, (lo, hi) in LEG4A.items():\n        vd = m.loc[r, VD]\n        print(f\"legend {r} {lo}-{hi}: visually driven medians {vd.min():.3f}-{vd.max():.3f}, inside widened range {bool(within(vd, *widen(lo, hi)).all())}\")\nprint(OUT[\"fig4a-vis-complexity-by-condition\"])\n'''\n\nC[90] = r'''def thal_tests(w, regs):\n    rows = []\n    for r in regs:\n        x = w[w.region == r]\n        kw = stats.kruskal(*[x[x.condition == c].C for c in paula.CONDITIONS]).pvalue\n        row = {\"region\": r, \"kruskal p\": kw}\n        for c1, c2 in paula.COND_PAIRS:\n            row[f\"{c1}-{c2}\"] = stats.mannwhitneyu(x[x.condition == c1].C, x[x.condition == c2].C).pvalue\n        pw = [row[f\"{c}-spont\"] for c in VD]\n        row[\"largest VD-spont p\"] = max(pw)\n        row[\"smallest VD-spont p\"] = min(pw)\n        row[\"smallest of six p\"] = min(row[f\"{c1}-{c2}\"] for c1, c2 in paula.COND_PAIRS)\n        rows.append(row)\n    return pd.DataFrame(rows).set_index(\"region\")\nfor ur in UNITS:\n    use(ur)\n    passes = {\"i\": False, \"ii\": False}\n    for rd in W:\n        m = MED_C[rd]\n        tt = thal_tests(W[rd], THR)\n        eff_max = m.loc[:, VD].max(axis=1) - m.spont\n        eff_mean = m.loc[:, VD].mean(axis=1) - m.spont\n        res = []\n        for r in [\"LGd\", \"LP\"]:\n            vd = m.loc[r, VD]\n            text_ok = bool(within(vd, *widen(0.14, 0.18)).all()) and within(m.loc[r, \"spont\"], *widen(0.11, 0.12))\n            leg = {\"LP\": ((0.12, 0.14), 0.11), \"LGd\": ((0.12, 0.15), 0.10)}[r]\n            leg_ok = bool(within(vd, *widen(*leg[0])).all()) and tol(m.loc[r, \"spont\"], leg[1], 0.1 * leg[1])\n            test_ok = tt.loc[r, \"kruskal p\"] < 0.001 or tt.loc[r, \"largest VD-spont p\"] < 0.001\n            res.append((r, vd.round(3).to_dict(), round(m.loc[r, \"spont\"], 3), text_ok, leg_ok, bool((vd > m.loc[r, \"spont\"]).all()),\n                        bool(eff_max[r] < eff_max[VISR].min()), bool(eff_mean[r] < eff_mean[VISR].min()), test_ok))\n        for form, k in [(\"i\", 6), (\"ii\", 7)]:\n            passes[form] |= all(x[8] and x[5] and (x[3] or x[4]) and x[k] for x in res)\n        print(f\"reading {rd}:\\n\", tt[[\"kruskal p\", \"largest VD-spont p\"]].to_string(float_format=lambda v: f\"{v:.1e}\"))\n        for x in res:\n            print(f\"  {x[0]}: VD medians {x[1]}, spont {x[2]}; text values {x[3]}; legend values {x[4]}; VD above spont {x[5]}; effect below every visual area (i) {x[6]}, (ii) {x[7]}\")\n        print(f\"  effects (i) VIS {eff_max[VISR].round(3).to_dict()} TH {eff_max[THR].round(3).to_dict()}\")\n        print(f\"  effects (ii) VIS {eff_mean[VISR].round(3).to_dict()} TH {eff_mean[THR].round(3).to_dict()}\")\n    print(f\"passes with effect form (i): {passes['i']}; with form (ii): {passes['ii']}\")\n    verdict(\"fig4b-thalamus-lgd-lp-modulated\", ur, \"reproduced\" if passes[\"i\"] else \"not_reproduced\")\nprint(OUT[\"fig4b-thalamus-lgd-lp-modulated\"])\n'''\n\nC[93] = r'''SEVEN = [\"MGd\", \"PoT\", \"SGN\", \"POL\", \"MGm\", \"MGv\", \"PIL\"]\nfor ur in UNITS:\n    use(ur)\n    seven = [r for r in SEVEN if r in REG]\n    ok_any = {\"Kruskal-Wallis\": False, \"pairwise, any VD-spont pair\": False, \"pairwise, all three VD-spont pairs\": False}\n    for rd in W:\n        m = MED_C[rd].loc[seven]\n        tt = thal_tests(W[rd], seven)\n        rng_ok = bool(within(m.values, 0.09, 0.143).all())\n        mod = {\"Kruskal-Wallis\": list(tt.index[tt[\"kruskal p\"] < 0.001]),\n               \"pairwise, any VD-spont pair\": list(tt.index[tt[\"smallest VD-spont p\"] < 0.001]),\n               \"pairwise, all three VD-spont pairs\": list(tt.index[tt[\"largest VD-spont p\"] < 0.001])}\n        for k, v in mod.items():\n            ok_any[k] |= rng_ok and not v and len(seven) == 7\n        print(f\"reading {rd}: medians {m.values.min():.3f}-{m.values.max():.3f} inside 0.09 to 0.143 {rng_ok}; nuclei found modulated (p < 0.001): {mod}\")\n        print(\"   largest condition difference in median C:\", (m.max(axis=1) - m.min(axis=1)).round(4).to_dict())\n        print(\"   \", tt.to_string(float_format=lambda v: f\"{v:.1e}\").replace(\"\\n\", \"\\n    \"))\n    print(\"reproduced under:\", ok_any)\n    verdict(\"fig4b-other-thalamus-not-modulated\", ur, \"reproduced\" if ok_any[\"pairwise, any VD-spont pair\"] and ok_any[\"Kruskal-Wallis\"] else\n            \"partially_reproduced\" if any(ok_any.values()) else \"not_reproduced\")\nprint(OUT[\"fig4b-other-thalamus-not-modulated\"])\n'''\n\nC[96] = r'''for ur in UNITS:\n    use(ur)\n    passes = {\"text\": False, \"legend\": False}\n    for rd in W:\n        m = MED_C[rd]\n        # (a) text: DG and CA3 inside their range in at least three of four conditions; CA1, POST, ProS, SUB inside 0.11-0.15 in every condition\n        a_dg = int(within(m.loc[\"DG\"], *widen(0.19, 0.27)).sum()); a_ca3 = int(within(m.loc[\"CA3\"], *widen(0.15, 0.21)).sum())\n        rest = m.loc[[\"CA1\", \"POST\", \"ProS\", \"SUB\"]]\n        a_rest = bool(within(rest.values, *widen(0.11, 0.15)).all())\n        peak = all(m.loc[g].idxmax() == \"spont\" for g in [\"DG\", \"CA3\"])\n        # (b) legend: natural images apart\n        b_ok = (tol(m.loc[\"DG\", \"images\"], 0.12, 0.012) and tol(m.loc[\"CA3\", \"images\"], 0.11, 0.011) and tol(m.loc[\"CA1\", \"images\"], 0.10, 0.010)\n                and bool(within(m.loc[\"DG\", [\"active\", \"blanks\", \"spont\"]], *widen(0.19, 0.26)).all())\n                and bool(within(m.loc[\"CA3\", [\"active\", \"blanks\", \"spont\"]], *widen(0.13, 0.18)).all())\n                and bool(within(m.loc[\"CA1\", [\"active\", \"blanks\", \"spont\"]], *widen(0.12, 0.17)).all())\n                and bool(within(m.loc[[\"POST\", \"ProS\", \"SUB\"]].values, *widen(0.10, 0.13)).all()))\n        passes[\"text\"] |= a_dg >= 3 and a_ca3 >= 3 and a_rest and peak\n        passes[\"legend\"] |= b_ok and peak\n        print(f\"reading {rd}: DG {m.loc['DG'].round(4).to_dict()}; CA3 {m.loc['CA3'].round(4).to_dict()}; spontaneous peak {peak}\")\n        print(f\"   text: DG inside in {a_dg}/4, CA3 in {a_ca3}/4, CA1/POST/ProS/SUB all inside {a_rest} (range {rest.values.min():.3f}-{rest.values.max():.3f}); passes {a_dg >= 3 and a_ca3 >= 3 and a_rest and peak}\")\n        print(f\"   legend: passes {b_ok and peak}; CA1 {m.loc['CA1'].round(3).to_dict()}; POST/ProS/SUB {m.loc[['POST','ProS','SUB']].values.min():.3f}-{m.loc[['POST','ProS','SUB']].values.max():.3f}\")\n        peak_any = peak\n    verdict(\"fig4c-dg-ca3-complexity\", ur, \"reproduced\" if any(passes.values()) else \"partially_reproduced\" if peak_any else \"not_reproduced\")\nprint(OUT[\"fig4c-dg-ca3-complexity\"])\n'''\n\nC[99] = r'''LEG4D = {\"NB\": (0.11, 0.12), \"MRN\": (0.10, 0.11), \"SCig\": (0.10, 0.11), \"APN\": (0.09, 0.09)}\nfor ur in UNITS:\n    use(ur)\n    if \"NOT\" not in REG or any(r not in REG for r in LEG4D):\n        print(\"not testable: subregions not kept under this reading:\", [r for r in [\"NOT\"] + list(LEG4D) if r not in REG])\n        verdict(\"fig4d-midbrain-complexity-invariant\", ur, \"not testable (NOT not kept)\")\n        continue\n    passes = False\n    for rd in W:\n        m = MED_C[rd]\n        four = m.loc[[\"NB\", \"MRN\", \"SCig\", \"APN\"]]\n        text_ok = bool(within(four.values, *widen(0.10, 0.12)).all())\n        leg_ok = all(within(m.loc[r], *widen(*v)).all() for r, v in LEG4D.items())\n        rngs = m.loc[MBR].max(axis=1) - m.loc[MBR].min(axis=1)\n        not_largest = rngs.idxmax() == \"NOT\"\n        passes |= (text_ok or leg_ok) and not_largest\n        print(f\"reading {rd}: medians\\n{four.round(3).to_string()}\\n NOT {m.loc['NOT'].round(3).to_dict()}; ranges across conditions {rngs.round(3).to_dict()}; \"\n              f\"text values {text_ok}; legend values {leg_ok}; NOT range largest {not_largest}; passes text {text_ok and not_largest}, legend {leg_ok and not_largest}\")\n    verdict(\"fig4d-midbrain-complexity-invariant\", ur, \"reproduced\" if passes else \"not_reproduced\")\nprint(OUT[\"fig4d-midbrain-complexity-invariant\"])\n'''\n\nC[102] = r'''for ur in UNITS:\n    CACHE[ur][\"JS_C\"] = js_all(WD[ur], \"C\", REGS[ur])\ndef pair_vals(m, a_set, b_set):\n    \"\"\"Values of pairs with one subregion in a_set and the other in b_set (each unordered pair once).\"\"\"\n    out = []\n    for i, j in zip(*iu):\n        ai, aj = AREA_OF[i], AREA_OF[j]\n        if (ai in a_set and aj in b_set) or (aj in a_set and ai in b_set):\n            out.append(m.values[i, j])\n    return np.array(out)\nuse(MAIN)\nprint(\"JS of C (bits), units=vbn, reading a/a, 50 bins, mean by area pair:\")\nfor c in paula.CONDITIONS:\n    m = JS_C[(\"a/a\", 50, \"2\")][c]\n    print(c, {f\"{a}-{b}\": round(float(pair_vals(m, {a}, {b}).mean()), 3) for a in paula.AREAS for b in paula.AREAS if a <= b})\n'''\n\nC[104] = r'''for ur in UNITS:\n    use(ur)\n    passes = []\n    for (rd, nb, base), mats in JS_C.items():\n        m = mats[\"images\"]\n        vv = pair_vals(m, {\"VIS\"}, {\"VIS\"}); vt = pair_vals(m, {\"VIS\"}, {\"TH\"}); vm = pair_vals(m, {\"VIS\"}, {\"MB\"})\n        dg = np.r_[m.loc[\"DG\"].drop(\"DG\").values, m.loc[\"CA3\"].drop([\"CA3\", \"DG\"]).values]\n        ok = (vv < 0.22).mean() > 0.5 and (vt > 0.36).mean() > 0.5 and (vm > 0.36).mean() > 0.5 and within(dg, 0.27, 0.55).mean() > 0.5\n        passes.append(ok)\n        print(f\"{rd}, {nb} bins, base {base}: VIS-VIS below 0.22 {(vv < 0.22).mean():.2f} (range {vv.min():.3f}-{vv.max():.3f}); VIS-TH above 0.36 {(vt > 0.36).mean():.2f} (median {np.median(vt):.3f}); \"\n              f\"VIS-MB above 0.36 {(vm > 0.36).mean():.2f} (median {np.median(vm):.3f}); DG/CA3 pairs in 0.27-0.55 {within(dg, 0.27, 0.55).mean():.2f} (median {np.median(dg):.3f}); passes {ok}\")\n    verdict(\"fig4e-js-complexity-natural-images\", ur, \"reproduced\" if any(passes) else \"not_reproduced\")\nprint(OUT[\"fig4e-js-complexity-natural-images\"])\n'''\n\nC[107] = r'''for ur in UNITS:\n    use(ur)\n    passes = []\n    for (rd, nb, base), mats in JS_C.items():\n        f = {c: pair_vals(mats[c], {\"VIS\"}, {\"TH\", \"HP\", \"MB\"}) for c in [\"active\", \"blanks\"]}\n        hh = pair_vals(mats[\"active\"], {\"HP\"}, {\"HP\"})\n        ok = all((v > 0.36).mean() > 0.5 for v in f.values()) and within(hh, 0.18, 0.44).mean() > 0.5\n        passes.append(ok)\n        print(f\"{rd}, {nb} bins, base {base}: VIS-subcortical above 0.36, active {(f['active'] > 0.36).mean():.2f} (median {np.median(f['active']):.3f}), blanks {(f['blanks'] > 0.36).mean():.2f} (median {np.median(f['blanks']):.3f}); \"\n              f\"HP-HP active in 0.18-0.44 {within(hh, 0.18, 0.44).mean():.2f} (range {hh.min():.3f}-{hh.max():.3f}); passes {ok}\")\n    verdict(\"fig4fg-js-complexity-active-blanks\", ur, \"reproduced\" if any(passes) else \"not_reproduced\")\nprint(OUT[\"fig4fg-js-complexity-active-blanks\"])\n'''\n\nC[110] = r'''for ur in UNITS:\n    use(ur)\n    passes = []\n    for (rd, nb, base), mats in JS_C.items():\n        allm = {c: mats[c].values[iu].mean() for c in paula.CONDITIONS}\n        vn = {c: pair_vals(mats[c], {\"VIS\"}, {\"TH\", \"HP\", \"MB\"}) for c in paula.CONDITIONS}\n        mm = {c: pair_vals(mats[c], {\"MB\"}, {\"MB\"}) for c in paula.CONDITIONS}\n        c1 = all(allm[\"spont\"] < allm[c] for c in VD)\n        c2 = all(vn[\"spont\"].mean() < vn[c].mean() for c in VD) and within(vn[\"spont\"], 0.18, 0.44).mean() > 0.5\n        c3 = all((mm[c] < 0.22).mean() > 0.5 for c in paula.CONDITIONS)\n        passes.append(c1 and c2 and c3)\n        print(f\"{rd}, {nb} bins, base {base}: mean of all pairs {({c: round(v, 3) for c, v in allm.items()})} (spont lowest {c1}); \"\n              f\"mean VIS-other {({c: round(float(v.mean()), 3) for c, v in vn.items()})}, spont pairs in 0.18-0.44 {within(vn['spont'], 0.18, 0.44).mean():.2f} ({c2}); \"\n              f\"MB-MB below 0.22 {({c: round(float((v < 0.22).mean()), 2) for c, v in mm.items()})} ({c3}); passes {c1 and c2 and c3}\")\n    verdict(\"fig4h-js-complexity-spontaneous-converges\", ur, \"reproduced\" if any(passes) else \"not_reproduced\")\nprint(OUT[\"fig4h-js-complexity-spontaneous-converges\"])\n'''\n\nC[113] = r'''print(\"supplement's 20 ms counts: images 11 321, active 51 452, blanks 11 265, spontaneous 2856\")\nfor ur in UNITS:\n    use(ur)\n    w = W[\"a/a\"]\n    print(\"windows per condition (the 20 ms series use the same windows):\", w.condition.value_counts().to_dict())\n    nok = 0\n    for bw, d, tau in paula.ROBUST + [(0.05, 6, 1)]:\n        col = \"C\" if (bw, d, tau) == (0.05, 6, 1) else f\"C_{int(bw*1000)}_{d}_{tau}\"\n        m = w.groupby([\"region\", \"condition\"])[col].median().unstack()\n        vis_ok = bool((m.loc[VISR, \"images\"] > m.loc[VISR, \"spont\"]).all())\n        diff = {a: w[(w.area == a) & w.condition.isin(VD)][col].median() - w[(w.area == a) & (w.condition == \"spont\")][col].median() for a in paula.AREAS}\n        ok = vis_ok and diff[\"VIS\"] > diff[\"MB\"]\n        if col != \"C\":\n            nok += ok\n        print(f\"bin {int(bw*1000)} ms, D={d}, tau={tau}{' (main)' if col == 'C' else ''}: images above spontaneous in {int((m.loc[VISR, 'images'] > m.loc[VISR, 'spont']).sum())}/6 visual areas; \"\n              f\"VD minus spont by area {({a: round(v, 4) for a, v in diff.items()})}; holds {ok}\")\n    print(\"combinations of the supplement where the pattern holds:\", nok, \"of 5\")\n    verdict(\"supp-robustness-parameters\", ur, \"reproduced\" if nok == 5 else \"partially_reproduced\" if nok >= 3 else \"not_reproduced\")\nprint(OUT[\"supp-robustness-parameters\"])\n'''\n"
}
```

```
File created successfully at: /tmp/claude-1001/cells_d.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/cells_e.py",
 "content": "C = {}\n\nC[116] = r'''for ur in UNITS:\n    TRAJ = {}\n    w0 = WD[ur][\"a/a\"]\n    for width in (0.1, 0.05):\n        for mn in (0, 10):\n            for a in paula.AREAS:\n                for c in paula.CONDITIONS:\n                    x = w0[(w0.area == a) & (w0.condition == c)]\n                    t = paula.trajectory(x.cv, x.C, width, mn)\n                    mono = bool((np.diff(t[\"mean\"].values) >= -(t.se.values[1:] + t.se.values[:-1])).all())\n                    rho = stats.spearmanr(x.cv, x.C).statistic\n                    slope = stats.linregress(x.cv, x.C).slope\n                    TRAJ[(width, mn, a, c)] = {\"cv lo\": t.lo.min(), \"cv hi\": t.hi.max(), \"C lo\": t[\"mean\"].min(), \"C hi\": t[\"mean\"].max(),\n                                               \"bins\": len(t), \"monotonic\": mono, \"spearman\": rho, \"slope\": slope, \"table\": t}\n    CACHE[ur][\"TRAJ\"] = TRAJ\n    TR = pd.DataFrame({k: {kk: vv for kk, vv in v.items() if kk != \"table\"} for k, v in TRAJ.items()}).T\n    TR.index.names = [\"width\", \"min\", \"area\", \"condition\"]\n    if ur == MAIN:\n        print(TR.astype({\"cv lo\": float, \"cv hi\": float, \"C lo\": float, \"C hi\": float, \"spearman\": float, \"slope\": float}).round(3).to_string())\nuse(MAIN)\nfig, ax = plt.subplots(1, 4, figsize=(16, 3.5), sharey=True)\nfor a_, c in zip(ax, paula.CONDITIONS):\n    for a in paula.AREAS:\n        t = TRAJ[(0.1, 10, a, c)][\"table\"]\n        a_.errorbar((t.lo + t.hi) / 2, t[\"mean\"], yerr=t.se, label=a, marker=\"o\", ms=3)\n    a_.set_title(c); a_.set_xlabel(\"CV\"); a_.set_xlim(0, 2)\nax[0].set_ylabel(\"mean C\"); ax[0].legend(); plt.show()\nprint(\"bins with CV above the axis (2):\", int(sum((TRAJ[(0.1, 10, a, c)][\"table\"].lo >= 2).sum() for a in paula.AREAS for c in paula.CONDITIONS)))\n\ndef span_ok(x, lo, hi):\n    return tol(x[0], lo, 0.1 * abs(lo)) and tol(x[1], hi, 0.1 * abs(hi))\n'''\n\nC[118] = r'''Q5 = {\"images\": ((0.1, 0.9), (0.08, 0.34)), \"active\": ((0.2, 1.6), (0.10, 0.38)), \"blanks\": ((0.1, 1.2), (0.10, 0.39))}\nfor ur in UNITS:\n    use(ur)\n    passes = []\n    for width in (0.1, 0.05):\n        for mn in (0, 10):\n            oks = []\n            for c, (cvr, cr) in Q5.items():\n                r = TRAJ[(width, mn, \"VIS\", c)]\n                s1, s2 = span_ok((r[\"cv lo\"], r[\"cv hi\"]), *cvr), span_ok((r[\"C lo\"], r[\"C hi\"]), *cr)\n                rise = r[\"monotonic\"] and r[\"spearman\"] > 0\n                oks.append(s1 and s2 and rise)\n                print(f\"width {width}, min {mn}, {c}: CV {r['cv lo']:.2f}-{r['cv hi']:.2f} (quoted {cvr}) {s1}; C {r['C lo']:.3f}-{r['C hi']:.3f} (quoted {cr}) {s2}; \"\n                      f\"monotonic {r['monotonic']}, Spearman {r['spearman']:.3f}\")\n            sp = TRAJ[(width, mn, \"VIS\", \"spont\")]\n            passes.append(all(oks) and sp['C hi'] < 0.165)\n            print(f\"width {width}, min {mn}: spontaneous maximum of bin means {sp['C hi']:.3f} (below 0.165: {sp['C hi'] < 0.165}); passes {passes[-1]}\")\n    verdict(\"fig5-vis-complexity-cv-coupling\", ur, \"reproduced\" if any(passes) else \"not_reproduced\")\nprint(OUT[\"fig5-vis-complexity-cv-coupling\"])\n'''\n\nC[121] = r'''for ur in UNITS:\n    use(ur)\n    passes = []\n    for width in (0.1, 0.05):\n        for mn in (0, 10):\n            oks = []\n            for c in VD:\n                r, v = TRAJ[(width, mn, \"TH\", c)], TRAJ[(width, mn, \"VIS\", c)]\n                s = 0.18 <= r[\"cv lo\"] and r[\"cv hi\"] <= 0.88 and 0.09 <= r[\"C lo\"] and r[\"C hi\"] <= 0.22\n                oks.append(r[\"slope\"] > 0 and r[\"slope\"] < v[\"slope\"] and s)\n                print(f\"width {width}, min {mn}, {c}: TH slope {r['slope']:.4f} vs VIS {v['slope']:.4f}; TH CV {r['cv lo']:.2f}-{r['cv hi']:.2f}, C {r['C lo']:.3f}-{r['C hi']:.3f}; spans inside {s}\")\n            passes.append(all(oks))\n            print(f\"  passes {all(oks)}\")\n    verdict(\"fig5-th-weaker-coupling\", ur, \"reproduced\" if any(passes) else \"not_reproduced\")\nprint(OUT[\"fig5-th-weaker-coupling\"])\n'''\n\nC[124] = r'''for ur in UNITS:\n    use(ur)\n    passes = []\n    for width in (0.1, 0.05):\n        for mn in (0, 10):\n            t = TRAJ[(width, mn, \"HP\", \"spont\")][\"table\"]\n            mid = t[(t.lo >= 0.4 - 1e-9) & (t.hi <= 0.7 + 1e-9)]\n            top = mid[\"mean\"].max() if len(mid) else np.nan\n            vdmax = {c: TRAJ[(width, mn, \"HP\", c)][\"C hi\"] for c in VD}\n            ok = tol(top, 0.25, 0.025) and all(top > v for v in vdmax.values()) and all(tol(v, 0.19, 0.019) for v in vdmax.values())\n            passes.append(ok)\n            print(f\"width {width}, min {mn}: HP spontaneous bin means at CV 0.4-0.7 up to {top:.3f}; HP visually driven maxima {({c: round(v, 3) for c, v in vdmax.items()})}; passes {ok}\")\n    verdict(\"fig5-hp-spontaneous-elevated\", ur, \"reproduced\" if any(passes) else \"not_reproduced\")\nprint(OUT[\"fig5-hp-spontaneous-elevated\"])\n'''\n\nC[127] = r'''for ur in UNITS:\n    use(ur)\n    passes = []\n    for width in (0.1, 0.05):\n        for mn in (0, 10):\n            inside = {c: bool(TRAJ[(width, mn, \"MB\", c)][\"C lo\"] >= 0.09 and TRAJ[(width, mn, \"MB\", c)][\"C hi\"] <= (0.165 if c == \"images\" else 0.143)) for c in paula.CONDITIONS}\n            slopes = {c: {a: abs(TRAJ[(width, mn, a, c)][\"slope\"]) for a in paula.AREAS} for c in paula.CONDITIONS}\n            flat = {c: min(s, key=s.get) == \"MB\" for c, s in slopes.items()}\n            passes.append(all(inside.values()) and all(flat.values()))\n            print(f\"width {width}, min {mn}: MB bin means {({c: (round(TRAJ[(width, mn, 'MB', c)]['C lo'], 3), round(TRAJ[(width, mn, 'MB', c)]['C hi'], 3)) for c in paula.CONDITIONS})}; \"\n                  f\"inside {inside}; MB slope smallest {flat}; |slopes| {({c: {a: round(v, 3) for a, v in s.items()} for c, s in slopes.items()})}; passes {passes[-1]}\")\n    verdict(\"fig5-mb-flat\", ur, \"reproduced\" if any(passes) else \"not_reproduced\")\nprint(OUT[\"fig5-mb-flat\"])\n'''\n\nC[130] = r'''for ur in UNITS:\n    use(ur)\n    passes = []\n    for rd in W:\n        for col in [\"corr50\", \"corr20\"]:\n            m = W[rd].groupby([\"region\", \"condition\"])[col].median().unstack()\n            v = m.loc[VISR]\n            ab = v[[\"active\", \"blanks\"]].values; ns = v[[\"images\", \"spont\"]].values\n            mb = m.loc[MBR]\n            mbr = (mb.max(axis=1) - mb.min(axis=1))\n            ok = bool(within(ab, *widen(0.08, 0.13)).all() and (ns < 0.011).all() and (mbr < 0.02).all())\n            passes.append(ok)\n            print(f\"{rd}, {col}: VIS active/blanks {ab.min():.3f}-{ab.max():.3f} inside 0.072-0.143 {int(within(ab, *widen(0.08, 0.13)).sum())}/12; \"\n                  f\"images/spont {ns.min():.4f}-{ns.max():.4f} below 0.011 {int((ns < 0.011).sum())}/12; MB range across conditions {mbr.round(4).to_dict()}; passes {ok}\")\n            if rd == \"a/a\" and col == \"corr50\" and ur == MAIN:\n                print(m.loc[VISR + MBR].round(4).to_string())\n    verdict(\"supp-fig6-mean-correlation\", ur, \"reproduced\" if any(passes) else \"not_reproduced\")\nprint(OUT[\"supp-fig6-mean-correlation\"])\n'''\n\nC[133] = r'''for ur in UNITS:\n    use(ur)\n    js_any, iqr_any = False, False\n    for rd in W:\n        w = W[rd]\n        for nb in (50, 100):\n            rows = []\n            for r in VISR:\n                x = w[w.region == r]\n                a, b = x[x.condition == \"images\"], x[x.condition == \"spont\"]\n                row = {\"region\": r}\n                for col in [\"C\", \"cv\", \"corr50\"]:\n                    row[f\"JS {col}\"] = paula.js_divergence(a[col], b[col], nb)\n                    qa, qb = a[col].quantile([0.25, 0.75]).values, b[col].quantile([0.25, 0.75]).values\n                    row[f\"IQR overlap {col}\"] = bool(qa[0] <= qb[1] and qb[0] <= qa[1])\n                rows.append(row)\n            t = pd.DataFrame(rows).set_index(\"region\")\n            js_ok = ((t[\"JS C\"] > t[\"JS cv\"]) & (t[\"JS C\"] > t[\"JS corr50\"])).sum()\n            iqr_ok = ((~t[\"IQR overlap C\"]) & t[\"IQR overlap cv\"] & t[\"IQR overlap corr50\"]).sum()\n            js_any |= js_ok > 3\n            iqr_any |= iqr_ok > 3\n            print(f\"{rd}, {nb} bins: complexity separates while CV and correlation do not, JS reading {js_ok}/6, IQR reading {iqr_ok}/6\")\n            if rd == \"a/a\" and nb == 50:\n                print(t.round(3).to_string())\n    verdict(\"complexity-separates-images-from-spontaneous\", ur, \"reproduced\" if js_any or iqr_any else \"not_reproduced\")\nprint(OUT[\"complexity-separates-images-from-spontaneous\"])\n'''\n\nSUMMARY_CODE = r'''# outcome of each claim's criterion under each unit reading, as computed in the claim sections above\nOUT[\"table1-sample\"] = {ur: \"not_reproduced\" for ur in UNITS}  # 153 sessions under every reading (section table1-sample)\nbyur = pd.DataFrame(OUT).T.reindex(columns=UNITS + [\"synthetic\"])\nprint(byur.fillna(\"\").to_string())\ndep = byur[UNITS].dropna()\nprint(\"claims whose criterion gives a different result under the variant readings than under 'vbn':\",\n      list(dep.index[(dep[\"all\"] != dep[\"vbn\"]) | (dep[\"qc\"] != dep[\"vbn\"])]))\n'''\n"
}
```

```
File created successfully at: /tmp/claude-1001/cells_e.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/assemble.py <<'EOF'
import json, sys, os
T = os.environ["TMPDIR"]
C = {}
for f in "abcde":
    ns = {}
    exec(open(f"{T}/cells_{f}.py").read(), ns)
    C.update(ns["C"])
    if "SUMMARY_CODE" in ns: SUMMARY = ns["SUMMARY_CODE"]
C[93] = C[93].replace('''    verdict("fig4b-other-thalamus-not-modulated", ur, "reproduced" if ok_any["pairwise, any VD-spont pair"] and ok_any["Kruskal-Wallis"] else
            "partially_reproduced" if any(ok_any.values()) else "not_reproduced")''',
'''    strict = [ok_any["Kruskal-Wallis"], ok_any["pairwise, any VD-spont pair"]]
    verdict("fig4b-other-thalamus-not-modulated", ur, "reproduced" if all(strict) else "not_reproduced" if not any(strict) else "test readings differ")''')
C[96] = C[96].replace("    passes = {\"text\": False, \"legend\": False}\n", "    passes = {\"text\": False, \"legend\": False}\n    peak_any = False\n").replace("        peak_any = peak\n", "        peak_any |= peak\n")
src = "entries/paula-2026/reproduce_paula_2026.ipynb"
nb = json.load(open(src))
cells = nb["cells"]
for i, s in C.items():
    assert cells[i]["cell_type"] == "code", i
    cells[i]["source"] = s.strip("\n").splitlines(keepends=True)
assert "".join(cells[135]["source"]).startswith("## Summary")
new = {"cell_type": "code", "execution_count": None, "id": "outcomes-by-units", "metadata": {}, "outputs": [], "source": SUMMARY.strip("\n").splitlines(keepends=True)}
hdr = {"cell_type": "markdown", "id": "outcomes-by-units-md", "metadata": {}, "source": ["## Outcome of each criterion under each unit reading\n", "\n", "The verdicts computed in the claim sections, collected in one table, so that the dependence of each outcome on the unit reading can be seen."]}
if not any(c.get("id") == "outcomes-by-units" for c in cells):
    cells[135:135] = [hdr, new]
json.dump(nb, open(src, "w"), indent=1, ensure_ascii=False)
print("ok", len(cells))
EOF
cd  && cp entries/paula-2026/reproduce_paula_2026.ipynb $TMPDIR/nb_orig.ipynb && python $TMPDIR/assemble.py
```

```
ok 138
```

**Agent calls Bash**

```bash
sed -i 's#^src = "entries/paula-2026/reproduce_paula_2026.ipynb"#src = T + "/nb_orig.ipynb"; dst = "entries/paula-2026/reproduce_paula_2026.ipynb"#; s#json.dump(nb, open(src, "w")#json.dump(nb, open(dst, "w")#' $TMPDIR/assemble.py && python $TMPDIR/assemble.py && cat > $TMPDIR/devrun.py <<'EOF'
import json, os, sys, nbformat, time
from nbclient import NotebookClient
T = os.environ["TMPDIR"]
nb = nbformat.read("entries/paula-2026/reproduce_paula_2026.ipynb", as_version=4)
nb.cells[3].source = f'''import pickle
sessions, n_assets, metas, windows, cv10_list, failed = pickle.load(open("{T}/subset.pkl", "rb"))
paula.MIN_SESSIONS = 2
t_extract = 0'''
t0 = time.time()
c = NotebookClient(nb, timeout=1200, kernel_name="python3", resources={"metadata": {"path": "entries/paula-2026"}}, allow_errors=True)
c.execute()
nbformat.write(nb, f"{T}/dev_out.ipynb")
for i, cell in enumerate(nb.cells):
    for o in cell.get("outputs", []):
        if o.output_type == "error":
            print("ERROR in cell", i, o.ename, o.evalue); print("\n".join(o.traceback[-3:])[:2000])
print("took", time.time() - t0)
EOF
$TMPDIR/devenv/bin/python -m ipykernel install --user --name python3 >/dev/null 2>&1; $TMPDIR/devenv/bin/python $TMPDIR/devrun.py 2>&1 | tail -40
```

```
ok 138
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
took 35.25606656074524
```

**Agent calls Bash**

```bash
cat > $TMPDIR/show.py <<'EOF'
import json, sys
nb = json.load(open(sys.argv[1]))
for i in map(int, sys.argv[2:]):
    c = nb["cells"][i]
    print("=== cell", i)
    for o in c.get("outputs", []):
        t = o.get("text") or o.get("data", {}).get("text/plain", "")
        print("".join(t)[:6000])
EOF
python $TMPDIR/show.py $TMPDIR/dev_out.ipynb 4 8 62 136 | cut -c1-400
```

```
=== cell 4
sessions read: 26 failed: 0 []
subjects: 26 | sessions per subject: {1: 26}
session types: {'EPHYS_1_images_G_3uL_reward': 13, 'EPHYS_1_images_H_3uL_reward': 12, 'EPHYS_1_images_G_5uL_reward': 1}
genotypes: {'Sst-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt': 11, 'Vip-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt': 9, 'wt/wt': 6}
probes with units per session: {6: 25, 5: 1}
image set by novel images (is_image_novel):
 novel      False  True 
image_set              
G             10      4
H              0     12
no grouping of sessions gives 102: by genotype {'Sst-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt': 11, 'Vip-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt': 9, 'wt/wt': 6} | by image set and novelty {('G', False): 10, ('G', True): 4, ('H', True): 12} | six probes 25
units per session: median 1865.5 range 1281 to 3033
active block length (s): {'count': 26.0, 'mean': 3604.3, 'std': 3.0, 'min': 3600.1, '25%': 3601.8, '50%': 3603.9, '75%': 3606.8, 'max': 3611.4}
active windows per session: {36: 26}
spontaneous epochs after the task (s): {'count': 26.0, 'mean': 289.0, 'std': 0.0, 'min': 289.0, '25%': 289.0, '50%': 289.0, '75%': 289.0, 'max': 289.0}
images per session: {8: 26} | flashes shown per session: median 4629.5 | omitted: median 173.5 | change flashes: median 238.5
shown flashes per image (all sessions): {'count': 208.0, 'mean': 578.3, 'std': 95.1, 'min': 320.0, '25%': 527.8, '50%': 565.0, '75%': 632.2, 'max': 933.0}
change flashes per image: {'count': 208.0, 'mean': 28.9, 'std': 7.8, 'min': 12.0, '25%': 23.0, '50%': 30.0, '75%': 36.0, 'max': 42.0}
blank pieces of 0.5 s: 120188 | shorter (cut by the next onset): 102 | median gray screen after a shown flash (s): 0.5004
[... 207 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; sed -i 's/  runtime_minutes: 40/  runtime_minutes: 50/' entries/paula-2026/entry.yaml; python tools/entry.py check entries/paula-2026 2>&1 | tail -15
```

```
Fri Nov 27 15:00:49 UTC 2026
0 error(s)
```

**Agent calls Bash**

```bash
python tools/entry.py run entries/paula-2026 2>&1 | tail -15; date -u
```

```
Installed kernelspec registry-paula-2026 in executed/paula-2026/.venv/share/jupyter/kernels/registry-paula-2026
pass  reproduce_paula_2026.ipynb  (2819 s)
Fri Nov 27 15:48:05 UTC 2026
```

**Agent calls Bash**

```bash
cp executed/paula-2026/reproduce_paula_2026.ipynb $TMPDIR/run1.ipynb; python $TMPDIR/show.py $TMPDIR/run1.ipynb 3 4 8 11 136 | cut -c1-330
```

```
=== cell 3
153 session files of 4293 assets; extraction took 45.8 min

=== cell 4
sessions read: 153 failed: 0 []
subjects: 81 | sessions per subject: {2: 72, 1: 9}
session types: {'EPHYS_1_images_G_3uL_reward': 74, 'EPHYS_1_images_H_3uL_reward': 71, 'EPHYS_1_images_G_5uL_reward': 4, 'EPHYS_1_images_H_5uL_reward': 4}
genotypes: {'Sst-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt': 59, 'wt/wt': 49, 'Vip-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt': 45}
probes with units per session: {6: 142, 5: 10, 3: 1}
image set by novel images (is_image_novel):
 novel      False  True 
image_set              
G             68     10
H             10     65
no grouping of sessions gives 102: by genotype {'Sst-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt': 59, 'wt/wt': 49, 'Vip-IRES-Cre/wt;Ai32(RCL-ChR2(H134R)_EYFP)/wt': 45} | by image set and novelty {('G', False): 68, ('G', True): 10, ('H', False): 10, ('H', True): 65} | six probes 142
units per session: median 2024.0 range 1103 to 3388
active block length (s): {'count': 153.0, 'mean': 3603.9, 'std': 2.6, 'min': 3599.5, '25%': 3601.5, '50%': 3603.8, '75%': 3606.0, 'max': 3611.4}
active windows per session: {36: 151, 35: 2}
spontaneous epochs after the task (s): {'count': 153.0, 'mean': 289.0, 'std': 0.0, 'min': 289.0, '25%': 289.0, '50%': 289.0, '75%': 289.0, 'max': 289.0}
images per session: {8: 153} | flashes shown per session: median 4623.0 | omitted: median 179.0 | change flashes: median 241.0
[... 171 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF' > $TMPDIR/run1_out.txt
import json
nb = json.load(open("/tmp/claude-1001/run1.ipynb"))
for i, c in enumerate(nb["cells"]):
    if c["cell_type"] != "code" or i < 12: continue
    print("=== cell", i, c["metadata"].get("tags"))
    for o in c.get("outputs", []):
        t = o.get("text") or o.get("data", {}).get("text/plain", "")
        if "Figure" in "".join(t): continue
        print("".join(t))
EOF
wc -l $TMPDIR/run1_out.txt; grep -n "=== cell" $TMPDIR/run1_out.txt | head -60
```

```
2380 /tmp/claude-1001/run1_out.txt
1:=== cell 13 ['claim:fig1c-cv-region-medians']
46:=== cell 16 ['claim:fig1c-cv-above-surrogate']
109:=== cell 19 ['claim:fig1d-surrogate-abolishes-cv-correlations']
137:=== cell 22 ['claim:fig1e-positive-cv-modules']
155:=== cell 25 ['claim:fig1e-dg-ca3-anticorrelation-hubs']
167:=== cell 28 ['claim:fig1e-midbrain-weakest-cv-correlations']
180:=== cell 31 None
215:=== cell 33 ['claim:fig2a-vis-cv-by-condition']
245:=== cell 36 ['claim:fig2a-thalamus-cv-by-condition']
275:=== cell 39 ['claim:fig2a-hippocampus-cv-stable']
307:=== cell 42 ['claim:fig2a-midbrain-cv-invariant']
329:=== cell 45 None
342:=== cell 47 ['claim:fig2b-vis-summed-js-cv']
450:=== cell 50 ['claim:fig2b-hp-mb-summed-js-cv']
561:=== cell 53 ['claim:fig2b-visually-driven-js-cv-low']
722:=== cell 56 ['claim:fig2b-dg-ca3-high-js-cv']
825:=== cell 59 ['claim:fig2b-legend-js-cv']
950:=== cell 62 ['claim:fig3a-reference-systems']
1011:=== cell 65 ['claim:fig3b-complexity-levels-by-region']
[... 25 more lines not kept]
```

**Agent**

Full run 1 passed (47 min). The VBN tutorial filter matches Table I neuron counts per population almost exactly, so it becomes the adopted unit reading. Now reading the per-claim numbers.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/run1_out.txt",
 "limit": 340
}
```

```
1	=== cell 13 ['claim:fig1c-cv-region-medians']
2	--- units=vbn (adopted)
3	
4	region   VISal  VISam   VISl   VISp  VISpm  VISrl    LGd     LP    MGd    MGm    MGv    PIL    POL    PoT    SGN    CA1    CA3     DG   POST   ProS    SUB    APN     NB    NOT    MRN   SCig
5	median   0.561  0.416  0.577  0.615  0.465  0.428  0.328  0.384  0.374  0.353   0.32  0.281   0.33  0.329  0.329  0.256  0.409  0.491  0.363   0.26  0.268  0.165  0.469  0.377  0.206  0.285
6	iqr      0.203  0.172  0.213  0.184  0.207   0.15  0.122  0.149  0.157   0.14  0.131  0.168  0.179  0.122  0.129  0.082  0.134  0.107  0.143  0.109  0.127  0.061  0.245  0.144    0.1  0.096
7	windows   5290   5182   5182   5326   5362   5146   1763   2232   2087   2196   2843   1080   1368   1440   2484   5110   3274   4534   1475   1583   2951   4463    683    396   2123   1223
8	area       VIS    VIS    VIS    VIS    VIS    VIS     TH     TH     TH     TH     TH     TH     TH     TH     TH     HP     HP     HP     HP     HP     HP     MB     MB     MB     MB     MB
9	units=vbn VIS: medians 0.416 to 0.615 (expected 0.4 to 0.59); inside widened range 6/6; extremes within tolerance True; IQR 0.150 to 0.213, inside 3/6
10	units=vbn TH: medians 0.281 to 0.384 (expected 0.27 to 0.37); inside widened range 9/9; extremes within tolerance True; IQR 0.122 to 0.179, inside 7/9
11	units=vbn HP: medians 0.256 to 0.491 (expected 0.25 to 0.49); inside widened range 6/6; extremes within tolerance True; IQR 0.082 to 0.143, inside 6/6
12	units=vbn MB: medians 0.165 to 0.469 (expected 0.16 to 0.45); inside widened range 5/5; extremes within tolerance True; IQR 0.061 to 0.245, inside 5/5
13	units=vbn: highest hippocampal median is DG (0.491); medians and extremes all match: True; IQRs all match: False
14	image set G area medians: {'HP': 0.326, 'MB': 0.195, 'TH': 0.337, 'VIS': 0.485}
15	image set H area medians: {'HP': 0.36, 'MB': 0.204, 'TH': 0.344, 'VIS': 0.55}
16	--- units=all (variant)
17	
18	region   VISal  VISam   VISl   VIS
[... 322 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/run1_out.txt",
 "offset": 342,
 "limit": 110
}
```

```
342	=== cell 47 ['claim:fig2b-vis-summed-js-cv']
343	--- units=vbn (adopted)
344	   reading  bins       sum     pct  active-blanks  images-active  active-spont  images-blanks  blanks-spont   closest pair  reproduced  partial
345	0      a/a    50  adjacent    mean           6.22           29.2          29.5           35.3          35.6   images-spont       False    False
346	1      a/a    50  adjacent  second           6.03           25.5          34.6           30.0          43.3   images-spont       False    False
347	2      a/a    50       all    mean           3.17           46.4          45.1           49.4          48.1   images-spont       False    False
348	3      a/a    50       all  second           3.12           37.7          58.2           39.6          63.3   images-spont       False    False
349	4      a/a   100  adjacent    mean          11.01           20.6          10.0           31.4          20.9   active-spont       False    False
350	5      a/a   100  adjacent  second          10.44           18.7          10.5           27.2          23.4   images-spont       False    False
351	6      a/a   100       all    mean           8.46           35.0          19.1           43.2          27.5  active-blanks       False     True
352	7      a/a   100       all  second           8.11           29.8          21.1           35.5          31.8  active-blanks       False    False
353	8      a/b    50  adjacent    mean           6.22           29.2          36.7           35.3          42.7  active-blanks       False    False
354	9      a/b    50  adjacent  second           6.03           25.5          45.0           30.0          54.3  active-blanks       False    False
355	10     a/b    50       all    mean           3.17           46.4          48.2           49.4          51.2   images-spont       False    False
356	11     a/b    50       all  second           3.12           37.7          63.5           39.6          68.8   images-spont       False    False
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && awk '/^=== cell/{cell=$0; print; next} /^--- units=/{show = ($0 ~ /vbn/)} show || /^\{.vbn/' run1_out.txt | sed -n '/cell 50/,/cell 62/p' | cut -c1-260 | grep -v "^reading .* bins\b" | head -150
```

```
=== cell 50 ['claim:fig2b-hp-mb-summed-js-cv']
--- units=vbn (adopted)

   reading  bins       sum     pct  HP active-spont HP largest pair  MB max  pairs where MB smallest  reproduced
0      a/a    50  adjacent    mean             69.2    active-spont    36.0                        3       False
1      a/a    50  adjacent  second             51.4    active-spont    30.5                        4       False
2      a/a    50       all    mean             59.4    active-spont    31.4                        3       False
3      a/a    50       all  second             45.8    active-spont    27.2                        3       False
4      a/a   100  adjacent    mean             77.1    active-spont    44.1                        1       False
5      a/a   100  adjacent  second             55.6    active-spont    36.1                        1       False
6      a/a   100       all    mean             66.9    active-spont    40.0                        1       False
7      a/a   100       all  second             50.1    active-spont    33.3                        2       False
8      a/b    50  adjacent    mean             66.9    active-spont    38.3                        3       False
9      a/b    50  adjacent  second             50.2    active-spont    32.1                        4       False
10     a/b    50       all    mean             57.7    active-spont    31.9                        3       False
11     a/b    50       all  second             44.8    active-spont    27.5                        3       False
12     a/b   100  adjacent    mean             77.6    active-spont    48.5                        1       False
13     a/b   100  adjacent  second             55.9    active-spont    39.0                        1       False
14     a/b   100       all    mean             65.8    active-spont    41.9                        1       False
15     a/b   100       all  second             49.5    active-spont    34.6                        2       False
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && awk '/^=== cell/{print; next} /^--- units=/{show = ($0 ~ /vbn/)} show || /^\{.vbn/' run1_out.txt | sed -n '/cell 59/,/cell 85/p' | cut -c1-300 | grep -v "^ *[A-Za-z]*-[a-z]* *0\.\|^measure\|^ *VISal" | head -120
```

```
=== cell 59 ['claim:fig2b-legend-js-cv']
--- units=vbn (adopted)


   reading  bins base measure VIS > 0.44 TH > 0.33 DG, CA3 range MB < 0.165  passes
0      a/a    50    2       a        3/6       0/9   0.002-0.085      18/30   False
1      a/a    50    2       b        0/6       0/9   0.035-0.374      23/30   False
2      a/a    50    e       a        0/6       0/9   0.002-0.059      20/30   False
3      a/a    50    e       b        0/6       0/9   0.024-0.259      26/30   False
4      a/a   100    2       a        3/6       2/9   0.005-0.145      13/30   False
5      a/a   100    2       b        0/6       0/9   0.034-0.416      21/30   False
6      a/a   100    e       a        0/6       0/9   0.004-0.101      19/30   False
7      a/a   100    e       b        0/6       0/9   0.024-0.288      24/30   False
8      a/b    50    2       a        3/6       0/9   0.002-0.074      17/30   False
9      a/b    50    2       b        0/6       0/9   0.035-0.372      23/30   False
10     a/b    50    e       a        0/6       0/9   0.002-0.051      20/30   False
11     a/b    50    e       b        0/6       0/9   0.024-0.258      26/30   False
12     a/b   100    2       a        3/6       1/9   0.005-0.139      13/30   False
13     a/b   100    2       b        0/6       0/9   0.034-0.418      21/30   False
14     a/b   100    e       a        0/6       0/9   0.004-0.097      18/30   False
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && awk '/^=== cell/{print; next} /^--- units=/{show = ($0 ~ /vbn/)} show || /^\{.vbn/' run1_out.txt | sed -n '/cell 87/,/cell 102/p' | cut -c1-420 | head -150
```

```
=== cell 87 ['claim:fig4a-vis-complexity-by-condition']
--- units=vbn (adopted)
reading a/a, uncorrected: order holds in 5/6 (['VISp'] fail); images medians 0.158-0.258 inside 6/6; spont 0.094-0.098 inside 6/6; active and blanks 0.102-0.187 inside 6/6; tests p < 0.001 35/36, largest p 8.3e-01 (VISp images-blanks); passes False

reading a/a, Bonferroni 36: order holds in 5/6 (['VISp'] fail); images medians 0.158-0.258 inside 6/6; spont 0.094-0.098 inside 6/6; active and blanks 0.102-0.187 inside 6/6; tests p < 0.001 35/36, largest p 1.0e+00 (VISp images-blanks); passes False
reading a/b, uncorrected: order holds in 5/6 (['VISp'] fail); images medians 0.158-0.258 inside 6/6; spont 0.094-0.097 inside 6/6; active and blanks 0.102-0.187 inside 6/6; tests p < 0.001 35/36, largest p 8.3e-01 (VISp images-blanks); passes False

reading a/b, Bonferroni 36: order holds in 5/6 (['VISp'] fail); images medians 0.158-0.258 inside 6/6; spont 0.094-0.097 inside 6/6; active and blanks 0.102-0.187 inside 6/6; tests p < 0.001 35/36, largest p 1.0e+00 (VISp images-blanks); passes False
reading b/a, uncorrected: order holds in 5/6 (['VISp'] fail); images medians 0.158-0.258 inside 6/6; spont 0.094-0.098 inside 6/6; active and blanks 0.102-0.187 inside 6/6; tests p < 0.001 35/36, largest p 7.7e-01 (VISp images-blanks); passes False

reading b/a, Bonferroni 36: order holds in 5/6 (['VISp'] fail); images medians 0.158-0.258 inside 6/6; spont 0.094-0.098 inside 6/6; active and blanks 0.102-0.187 inside 6/6; tests p < 0.001 35/36, largest p 1.0e+00 (VISp images-blanks); passes False
reading b/b, uncorrected: order holds in 5/6 (['VISp'] fail); images medians 0.158-0.258 inside 6/6; spont 0.094-0.097 inside 6/6; active and blanks 0.102-0.187 inside 6/6; tests p < 0.001 35/36, largest p 7.7e-01 (VISp images-blanks); passes False

reading b/b, Bonferroni 36: order holds in 5/6 (['VISp'] fail); images medians 0.158-0.258 inside 6/6; spont 0.094-0.097 inside 6/6; active and blanks 0.102-0.187 insi
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && awk '/^=== cell/{print; next} /^--- units=/{show = ($0 ~ /vbn/)} show || /^\{.vbn/' run1_out.txt | sed -n '/cell 96/,/cell 116/p' | cut -c1-420 | head -150
```

```
=== cell 96 ['claim:fig4c-dg-ca3-complexity']
--- units=vbn (adopted)
reading a/a: DG {'images': 0.1161, 'active': 0.2151, 'blanks': 0.1793, 'spont': 0.2494}; CA3 {'images': 0.1067, 'active': 0.1488, 'blanks': 0.1298, 'spont': 0.1875}; spontaneous peak True
   text: DG inside in 3/4, CA3 in 2/4, CA1/POST/ProS/SUB all inside False (range 0.095-0.155); passes False
   legend: passes True; CA1 {'images': 0.095, 'active': 0.133, 'blanks': 0.118, 'spont': 0.155}; POST/ProS/SUB 0.096-0.135
reading a/b: DG {'images': 0.1161, 'active': 0.2151, 'blanks': 0.1793, 'spont': 0.2506}; CA3 {'images': 0.1067, 'active': 0.1488, 'blanks': 0.1298, 'spont': 0.1866}; spontaneous peak True
   text: DG inside in 3/4, CA3 in 2/4, CA1/POST/ProS/SUB all inside False (range 0.095-0.158); passes False
   legend: passes True; CA1 {'images': 0.095, 'active': 0.133, 'blanks': 0.118, 'spont': 0.158}; POST/ProS/SUB 0.096-0.135
reading b/a: DG {'images': 0.1161, 'active': 0.2151, 'blanks': 0.179, 'spont': 0.2494}; CA3 {'images': 0.1067, 'active': 0.1488, 'blanks': 0.1296, 'spont': 0.1875}; spontaneous peak True
   text: DG inside in 3/4, CA3 in 2/4, CA1/POST/ProS/SUB all inside False (range 0.095-0.155); passes False
   legend: passes True; CA1 {'images': 0.095, 'active': 0.133, 'blanks': 0.118, 'spont': 0.155}; POST/ProS/SUB 0.096-0.135
reading b/b: DG {'images': 0.1161, 'active': 0.2151, 'blanks': 0.179, 'spont': 0.2506}; CA3 {'images': 0.1067, 'active': 0.1488, 'blanks': 0.1296, 'spont': 0.1866}; spontaneous peak True
   text: DG inside in 3/4, CA3 in 2/4, CA1/POST/ProS/SUB all inside False (range 0.095-0.158); passes False
   legend: passes True; CA1 {'images': 0.095, 'active': 0.133, 'blanks': 0.118, 'spont': 0.158}; POST/ProS/SUB 0.096-0.135
{'vbn': 'reproduced', 'all': 'reproduced', 'qc': 'reproduced'}
=== cell 99 ['claim:fig4d-midbrain-complexity-invariant']
--- units=vbn (adopted)
reading a/a: medians
condition  images  active  blanks  spont
region                                  
[... 113 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && awk '/^=== cell/{print; next} /^--- units=/{show = ($0 ~ /vbn/)} show || /^\{.vbn/' run1_out.txt | sed -n '/cell 118/,/cell 136/p' | cut -c1-520 | grep -v "^ *VIS\|^ *[A-Z][A-Za-z]* *0\.\|^condition\|^region" | head -90; date -u
```

```
=== cell 118 ['claim:fig5-vis-complexity-cv-coupling']
--- units=vbn (adopted)
width 0.1, min 0, images: CV 0.20-1.40 (quoted (0.1, 0.9)) False; C 0.118-0.329 (quoted (0.08, 0.34)) False; monotonic False, Spearman 0.640
width 0.1, min 0, active: CV 0.20-4.60 (quoted (0.2, 1.6)) False; C 0.095-0.381 (quoted (0.1, 0.38)) True; monotonic False, Spearman 0.844
width 0.1, min 0, blanks: CV 0.10-2.00 (quoted (0.1, 1.2)) False; C 0.089-0.391 (quoted (0.1, 0.39)) False; monotonic False, Spearman 0.836
width 0.1, min 0: spontaneous maximum of bin means 0.337 (below 0.165: False); passes False
width 0.1, min 10, images: CV 0.20-1.00 (quoted (0.1, 0.9)) False; C 0.118-0.316 (quoted (0.08, 0.34)) False; monotonic True, Spearman 0.640
width 0.1, min 10, active: CV 0.20-1.60 (quoted (0.2, 1.6)) True; C 0.095-0.337 (quoted (0.1, 0.38)) False; monotonic True, Spearman 0.844
width 0.1, min 10, blanks: CV 0.20-1.70 (quoted (0.1, 1.2)) False; C 0.095-0.348 (quoted (0.1, 0.39)) False; monotonic False, Spearman 0.836
width 0.1, min 10: spontaneous maximum of bin means 0.153 (below 0.165: True); passes False
width 0.05, min 0, images: CV 0.20-1.35 (quoted (0.1, 0.9)) False; C 0.103-0.331 (quoted (0.08, 0.34)) False; monotonic False, Spearman 0.640
width 0.05, min 0, active: CV 0.20-4.55 (quoted (0.2, 1.6)) False; C 0.094-0.396 (quoted (0.1, 0.38)) True; monotonic False, Spearman 0.844
width 0.05, min 0, blanks: CV 0.15-2.00 (quoted (0.1, 1.2)) False; C 0.089-0.391 (quoted (0.1, 0.39)) False; monotonic False, Spearman 0.836
width 0.05, min 0: spontaneous maximum of bin means 0.350 (below 0.165: False); passes False
width 0.05, min 10, images: CV 0.20-1.00 (quoted (0.1, 0.9)) False; C 0.103-0.316 (quoted (0.08, 0.34)) False; monotonic True, Spearman 0.640
width 0.05, min 10, active: CV 0.20-1.50 (quoted (0.2, 1.6)) True; C 0.094-0.346 (quoted (0.1, 0.38)) True; monotonic True, Spearman 0.844
width 0.05, min 10, blanks: CV 0.20-1.20 (quoted (0.1, 1.2)) False; C 0.093-0.327 (quoted (0.1, 0.3
[... 74 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas/ 2>/dev/null | head; grep -l "verifications:" attempts/*.yaml | head -3; f=$(grep -l "verifications:" attempts/*.yaml | head -1); sed -n '/^verifications:/,$p' $f | head -60; head -30 questions/asari-2009.yaml
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
attempts/amjad-2025-01.yaml
attempts/andrews-2024-01.yaml
attempts/armstrong-2026-01.yaml
verifications:
- date: '2026-10-15'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
    module and the claims file, with the paper's full text (PMC12183687). The verifier read the
    archive's file list and metadata through the DANDI API and tested the helpers on synthetic inputs
    (beta_power, burst_onsets, window_mean, codes_per_trial, rereference, fscv_window_mean, best_lag,
    reward_blocks). It had no attempt record and took the claims from the claims file.
  results:
  - claim: insertion-yield
    agrees: true
    outcome: blocked
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open("schemas/attempt.schema.json"))
def find(o, key, path=""):
    if isinstance(o, dict):
        for k,v in o.items():
            if k==key: print(path+"/"+k, json.dumps(v)[:3000]); 
            find(v,key,path+"/"+k)
    elif isinstance(o,list):
        for i,v in enumerate(o): find(v,key,path+f"[{i}]")
find(s,"verifications")
find(s,"proposed")
EOF
ls questions | grep paula
```

```
/properties/verifications {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["date", "kind", "by", "results"], "properties": {"date": {"type": "string", "format": "date"}, "kind": {"enum": ["agent", "person", "paper_author"]}, "by": {"type": "string"}, "results": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["claim", "agrees"], "properties": {"claim": {"type": "string"}, "agrees": {"type": "boolean"}, "reason": {"description": "The verifier's reason, in its own words.", "type": "string"}, "response": {"description": "What the author changed or replied, kept apart from the verifier's reason.", "type": "string"}, "outcome": {"description": "The outcome the verifier would give.", "enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}}}}, "reviewed": {"description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.", "type": "string"}, "findings": {"description": "From protocol pilot-18, in round 2: what the verifier said of each finding the record rates `critical` (docs/protocol.md, the attempt record).", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["finding", "agrees"], "properties": {"finding": {"description": "The finding's number in this record's `findings`, from 1.", "type": "integer", "minimum": 1}, "agrees": {"description": "Whether the verifier agreed that the outputs show the finding and that it is critical.", "type": "boolean"}, "severity": {"description": "The severity the verifier would give, where it differs.", "enum": ["critical", "major", "minor", "none"]}, "reason": {"description": "The verifier's reason, in its own words.", "type": "string"}, "response": {"description": "What the author changed or replied.", "type": "string"}}}}}}}
/properties/outcomes/items/properties/proposed {"description": "A change of outcome found after the last verification round, held until a further round agr
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python $TMPDIR/show.py $TMPDIR/run1.ipynb 62 | tail -12; cd $TMPDIR && awk '/^=== cell/{print; next} /^--- units=/{show = ($0 ~ /vbn/)} show' run1_out.txt | sed -n '/cell 133/,/cell 136/p' | sed -n '1,14p'
```

```
18  logistic      r=4.0  0.629  0.484    True
23      tent  mu=1.9999  0.630  0.485    True
27     Ikeda    p=6.683  0.811  0.355   False
31     Ikeda   p=12.966  0.810  0.355   False 
 inside C 0.36 to 0.55 and H 0.45 to 0.88: False
Ikeda sweep: inside the chaotic range at ['p=6.500']
parts that hold: white noise True | sine at some sampling True | correlated walk False | chaotic maps False

<Figure size 600x450 with 1 Axes>
plotted H range 0.105 0.999 C range 0.001 0.485
{'synthetic': 'partially_reproduced'}

=== cell 133 ['claim:complexity-separates-images-from-spontaneous']
--- units=vbn (adopted)

a/a, 50 bins: complexity separates while CV and correlation do not, JS reading 6/6, IQR reading 1/6
         JS C  IQR overlap C  JS cv  IQR overlap cv  JS corr50  IQR overlap corr50
region                                                                            
VISal   0.837          False  0.537           False      0.464               False
VISam   0.516          False  0.391           False      0.312                True
[... 7 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/cells_md.py",
 "content": "M = {}\nNOTE_U = \" The outcome rests on the adopted unit reading ('vbn'); the table at the end gives the criterion under 'all' and 'qc'.\"\n\nM[2] = \"\"\"## Loading\n\nOne pass over all ecephys sessions, four sessions at a time in separate processes. Each session's spike times are read up to the end of its spontaneous epoch, and every population is measured under the three unit readings ('vbn', 'all', 'qc'). This takes about 46 minutes.\"\"\"\n\nM[7] = \"\"\"## table1-sample\n\n> The analysis rests on 102 sessions and 1437 local populations (VIS 586, TH 313, HP 363, MB 175), with 53 985 visual cortex, 20 541 thalamic, 42 396 hippocampal and 17 163 midbrain neurons, and 77 216 analysis windows (11 321 natural images, 51 704 active behavior, 11 321 blanks, 2870 spontaneous).\n\nThe claims file names two unit readings, 'all' units and 'qc' (ISI violations < 0.5, amplitude cutoff < 0.1, presence ratio > 0.9), and says that Table I's neuron counts decide between them. The dandiset has 153 sessions against the paper's 102, so totals cannot be compared as they stand: the comparison that can tell filters apart is per population (neurons per population) or after scaling the totals by 102/153. The first table gives that comparison for six filters, from the unit counts of every session: the claims file's two, 'vbn' (snr > 1, ISI violations < 1, firing rate > 0.1 spikes/s, the unit filter of the Allen Institute's Visual Behavior Neuropixels quickstart tutorial, AllenSDK commit a56bd8ea), 'good' (quality label 'good'), 'qc95' ('qc' with presence ratio > 0.95) and 'good_pr95'. The second gives the claim's counts from the windows for the three readings run below, under each session reading ((a) sessions with at least one kept population; (b) those that also have the spontaneous gray-screen epoch).\"\"\"\n\nM[9] = \"\"\"**Result: not reproduced.** Every one of the 153 ecephys sessions has kept populations and the spontaneous epoch, so both session readings give 153 sessions, not 102, under every unit reading, and no reading puts the counts within tolerance. Scaled to 102 sessions, the 'vbn' filter gives area neuron counts 1.00 (VIS), 1.02 (TH), 0.93 (HP) and 0.94 (MB) times Table I's, per-subregion ratios 0.79 to 1.21, and neurons per population 92.7, 64.7, 112.0 and 98.0 against Table I's 92.1, 65.6, 116.8 and 98.1; it keeps all 26 subregions. 'all' gives 1.28 to 1.43 times Table I and 'qc' 0.34 to 0.55 times (qc also drops NOT); 'qc' puts the four window counts within tolerance only because its fewer populations per session (754 VIS against 586 x 153/102 = 879) offset the excess of sessions. 'vbn' is adopted by the other claims as an assumption, the filter closest to Table I by the comparison the claims file names, with 'all' and 'qc' run as variants for every claim.\"\"\"\n\nM[10] = \"\"\"### Readings used below\n\nThe adopted unit reading is 'vbn' (assumption, above); every claim is also run under 'all' and 'qc', and each claim cell prints the criterion's verdict under each unit reading. The surrogate is drawn under five seeds for 'vbn' only. The four condition readings combine the blank reading (a: after every shown flash; b: only after flashes followed by another flash) with the spontaneous reading (a: the first two 100-s windows of the gray screen; b: two windows centred in it). They are written `blanks/spont`, for example `a/b`.\"\"\"\n\nM[14] = \"\"\"**Result: partially reproduced.** Under 'vbn' every subregion median lies in its area's widened range and every extreme is within tolerance (VIS 0.416 to 0.615, TH 0.281 to 0.384, HP 0.256 to 0.491 with DG highest, MB 0.165 to 0.469), but the IQRs miss in 3 of 6 visual subregions (0.150 to 0.213 against 0.108 to 0.198) and 2 of 9 thalamic ones, which the criterion makes partially reproduced. Under 'all' and 'qc' the medians miss (DG 0.564 and NB 0.564 under 'all', LP 0.414 under 'qc').\"\"\"+NOTE_U\n\nM[17] = \"\"\"**Result: partially reproduced.** Empirical CV is above the surrogate CV in every subregion and every area (Mann-Whitney p at most 1.4e-51 per subregion, 0 at printed precision per area; on one median per population, Wilcoxon p at most 3.3e-42, empirical higher in 246 of 247 to 875 of 875 populations), and the visual surrogate medians (0.233 to 0.250) lie in 0.189 to 0.264. Three ratios fall outside their widened ranges: VISam (1.75) and VISrl (1.78) below 1.80, and POST (1.29) below 1.35. All five seeds give the same result (ratios 1.286 to 2.644). 'all' and 'qc' give the same outcome.\"\"\"+NOTE_U\n\nM[20] = \"\"\"**Result: not reproduced.** The empirical correlations are present (largest 0.798 under reading a and 0.679 under b), but the surrogate correlations are not abolished: 147 of 325 pairs (reading a) and 240 (reading b) have |r| above 0.2, largest 0.890 and 0.708, and the other four seeds give the same (0.889 to 0.900 and 0.699 to 0.708). The per-window ISI shuffle keeps each 100-s window's spike counts, so the surrogate CV still follows the rate of each window, and those rates co-vary across regions. Reading a also mixes session-level differences into one correlation. Every unit reading gives the same outcome.\"\"\"\n\nM[23] = \"\"\"**Result: reproduced.** Under reading b (the per-session correlations averaged) the strongest 32 of 325 pairs have r 0.478 to 0.680, inside 0.50 +/- 0.05 to 0.67 +/- 0.067, and 28 of them join subregions of the same major area (visual areas with each other, thalamic nuclei, subicular pairs ProS-SUB and POST-SUB). Under reading a (concatenated) the top value is 0.798, above 0.737, with 21 of 32 within an area. Reading b is adopted as an assumption: concatenating the series of different sessions mixes session-level differences into one correlation, which averaging per session avoids. Under 'all' and 'qc' neither reading passes (for example reading b low end 0.450 under 'all').\"\"\"+NOTE_U\n\nM[26] = \"\"\"**Result: reproduced.** Under reading b, DG (16) and CA3 (14) are the subregions in most of the 32 most negative pairs, and the most negative value, -0.247, is within -0.27 +/- 0.027. Under reading a, CA3 and NB lead (8 each) and the most negative value is -0.436. Reading b is adopted, as for fig1e-positive-cv-modules. Under 'all' the most negative value is -0.178 and under 'qc' -0.359, both outside.\"\"\"+NOTE_U\n\nM[29] = \"\"\"**Result: not reproduced.** The midbrain has the lowest mean |r| under both readings (reading a 0.183 against HP 0.187, TH 0.253, VIS 0.325; reading b 0.210 against 0.252 to 0.360), but its correlations are not near zero: 13 of 115 (reading a) and 3 of 115 (reading b) midbrain pairs lie in -0.044 to 0.033. Every unit reading gives the same outcome.\"\"\"\n\nM[34] = \"\"\"**Result: reproduced.** Under all four condition readings the twelve medians are within tolerance (reading a/a: VISp 0.615, 0.579, 0.299 and 0.399 against 0.59, 0.55, 0.29 and 0.39; VISl 0.577, 0.485, 0.303, 0.475; VISal 0.561, 0.483, 0.304, 0.484), and the order active > images > spontaneous with blanks > spontaneous holds in the three areas. 'all' also gives 12 of 12 (a/a and b/a); 'qc' gives 7 or 8 of 12.\"\"\"+NOTE_U\n\nM[37] = \"\"\"**Result: reproduced.** Under every reading the four medians are within tolerance (LP 0.384 and 0.277 to 0.282, LGd 0.328 and 0.225 to 0.226 against 0.37, 0.28, 0.32 and 0.23), and the active minus spontaneous difference of LP (0.102 to 0.107) and LGd (0.102 to 0.103) is below that of VISp, VISl and VISal (0.256 to 0.316). 'all' gives the same; under 'qc' LP active (0.414) misses.\"\"\"+NOTE_U\n\nM[40] = \"\"\"**Result: reproduced.** Under every condition reading all seven values are within tolerance: DG 0.482 to 0.504 and CA3 0.406 to 0.415 across the visually driven conditions, CA1 0.254 to 0.258, DG spontaneous 0.509 to 0.510 and CA3 spontaneous 0.424 to 0.429, and the spontaneous medians of DG and CA3 exceed their visually driven ones. 'qc' also gives 7 of 7; under 'all' DG is higher (0.555 to 0.580) and misses.\"\"\"+NOTE_U\n\nM[43] = \"\"\"**Result: not reproduced.** The MRN highest median (0.209, natural images) is within 0.21 +/- 0.021, but APN's spontaneous median (0.142) is below 0.16 - 0.016 (its other conditions 0.164 to 0.165), and MRN's lowest (0.171, spontaneous) below 0.18. Under 'all' APN and the MRN low end match and the MRN high end (0.233) misses; under 'qc' all three miss.\"\"\"+NOTE_U\n\nM[48] = \"\"\"**Result: partially reproduced.** No combination of readings meets the full rule. With 100 bins, the sum over all within-area pairs and the percentage over the mean of the two sums (4 of 32 combinations, one per condition reading), active and blank screens are the closest pair (8.46% to 9.05% apart) and the other pairs differ by 19.1% to 43.7%, which meets the partial rule; active against blanks is not within 1 +/- 0.5% in any combination (3.12% to 11.24%). 'all' also meets the partial rule (4 combinations, active against blanks 0.32% to 0.53%); 'qc' meets neither. The outcome depends on the histogram and sum readings.\"\"\"+NOTE_U\n\nM[51] = \"\"\"**Result: not reproduced.** Active against spontaneous is the largest hippocampal difference under every combination, as the paper says, but it is 44.8% to 77.6%, not 15% +/- 1.5%, and the largest midbrain difference is 27.2% to 48.5%, not at most 7.7%; the midbrain has the smallest difference in at most 4 of the 6 pairs. Every unit reading gives the same outcome.\"\"\"\n\nM[54] = \"\"\"**Result: partially reproduced.** Under the statement's percentage form no combination has two of the three pairs at or below 4.4% (active against blanks 3.1% to 11.2%, the pairs with natural images 18.7% to 49.9%). Under the legend's form, most VIS-VIS divergences are at most 0.22 in each visually driven condition (fractions 0.73 to 1.0) under every condition, histogram and log-base reading. The finding holds as the legend states it and not as the text states it, which is partially reproduced. Every unit reading gives the same outcome.\"\"\"\n\nM[57] = \"\"\"**Result: not reproduced.** Against the other 25 subregions (bits, 50 bins, a/a) DG's medians are 0.713 (spontaneous) and 0.345 (blanks) and CA3's 0.443 and 0.216, against 0.84 and 0.63; over all readings DG spontaneous is 0.700 to 0.774 in bits, and the spontaneous median is the largest of the four conditions for both. Against the other hippocampal subregions only, DG spontaneous is 0.736 to 0.791 (within 0.84 +/- 0.084 for 100 bins and the spontaneous reading b, 0.791 at most), but CA3 (0.555 to 0.622) and the blank medians (DG 0.529 to 0.545, CA3 0.333 to 0.356) miss. Natural logs give lower values still. Every unit reading gives the same outcome.\"\"\"\n\nM[60] = \"\"\"**Result: not reproduced.** Under reading a, 3 of 6 visual subregions exceed 0.44 in bits (none in natural logs), at most 2 of 9 thalamic subregions exceed 0.33, and the DG and CA3 values (0.002 to 0.153) lie below 0.135; under reading b no visual or thalamic subregion passes. Most midbrain values are below 0.165 under most readings (13 to 26 of 30). Every unit reading gives the same outcome.\"\"\"\n\nM[61] = \"\"\"## fig3a-reference-systems\n\n> In the C-H plane with D = 6, white noise lies at H near 1 and C near 0, a sine near H 0 and C near 0.1, exponentially correlated Brownian motion at C 0.3 to 0.5 for H 0.3 to 0.6, and chaotic maps (logistic, tent, Ikeda) near maximum complexity, C 0.4 to 0.5 at H 0.5 to 0.8.\n\nSynthetic series as defined in Supplemental Material Sec. I, 10^5 points after 10^3 dropped (claims file). Correlated Gaussian noise: increments from N(0, 1) noise convolved with the normalized kernel w_k = exp(-k / (K alpha)), K = floor(100 alpha) + 1, then summed (Sec. I.A). Near 1 is read as at least 0.9 and near 0 for C as at most 0.05 (10% of 0 is no tolerance). A sine cannot reach H = 0 with D = 6: it gives at least the rising and the falling pattern, so H >= ln 2 / ln 720 = 0.105; \"H near 0\" is read as at most that floor plus 0.05. The sine's sampling is not given, so 100, 1000 and 10 000 points per period are run. The logistic and tent maps are judged at their fully chaotic parameters (r = 4, mu = 1.9999, the tent map at mu = 2 collapsing to 0 in floating point). The Ikeda map's parameter p enters only through cos and sin of p - 6/(1 + x^2 + y^2), so p repeats every 2 pi; it is judged at the usual chaotic value 0.4 shifted into the supplement's [5, 17] (0.4 + 2 pi = 6.683 and 0.4 + 4 pi = 12.966), with a sweep shown.\"\"\"\n\nM[63] = \"\"\"**Result: partially reproduced.** White noise is at H 0.999, C 0.001, and the logistic map (r = 4) and tent map (mu = 1.9999) are at H 0.63, C 0.48, inside the chaotic range. The sine meets its reading at 10 000 points per period (H 0.107, C 0.106) and not at 100 or 1000 (C 0.165 and 0.113). The Ikeda map at its chaotic parameter (p = 6.683 and 12.966) lies at H 0.81, C 0.355, just below C 0.36; of the sweep only p = 6.5 is inside (H 0.794, C 0.367). The exponentially correlated walks with H in 0.27 to 0.66 have C 0.233 to 0.334, two of four below 0.27. The parameters of Fig. 3a are not in the text, so these positions rest on the parameter readings shown.\"\"\"\n\nM[66] = \"\"\"**Result: reproduced.** Under reading a (the 36 active windows), the mean C over windows is 0.158 (VIS), 0.159 (HP), 0.108 (TH) and 0.098 (MB), each within its tolerance, and the order MB < TH < VIS and HP holds at all 36 window indices. Under reading b (natural images) hippocampus falls below thalamus (0.107 against 0.118) and the order holds at none of the 8 indices. Every unit reading gives the same outcome; it rests on reading a.\"\"\"\n\nM[67] = \"\"\"## C-H plane per area (claims of Figs. 3c to 3f)\n\nActive windows (the reading the claims file assigns from the point counts), with natural-image windows shown. Spans are the 2.5th to 97.5th percentiles (and the 0th to 100th, a variant), compared unrounded. The Mann-Whitney test compares C of the windows with C of their surrogates, two-sided, under the five seeds; as windows of one population are not independent, the same comparison is also made on one median per population (Wilcoxon signed-rank).\"\"\"\n\nM[71] = \"\"\"**Result: not reproduced.** The test holds: C of the visual windows is above that of their surrogates (median 0.149 against 0.097, Mann-Whitney p = 0 at printed precision under all five seeds, per-population Wilcoxon p = 1.9e-141), and the surrogate median (0.0965 to 0.0966) lies in 0.09 to 0.22. The 2.5th to 97.5th percentile span of H (0.857 to 0.965) is inside 0.72 to 1.10, but that of C starts at 0.0887, below 0.090, a narrow miss; the 0th to 100th span misses on H (0.454). Under 'qc' the C span starts above 0.090 and the claim passes; 'all' misses as 'vbn' does.\"\"\"+NOTE_U\n\nM[74] = \"\"\"**Result: reproduced.** The thalamic span (H 0.930 to 0.969, C 0.081 to 0.167, 2.5th to 97.5th percentiles) is inside the widened ranges, its C span (0.087) is narrower than that of visual cortex (0.194), and C is above the surrogate's (Mann-Whitney p = 0 at printed precision, all five seeds; per-population Wilcoxon p = 1.1e-43). The 0th to 100th span misses on C (up to 0.344). Every unit reading gives the same outcome; it rests on the percentile reading of a span.\"\"\"\n\nM[77] = \"\"\"**Result: reproduced.** The hippocampal span (H 0.858 to 0.967, C 0.086 to 0.298) is inside the widened ranges, its C span (0.213) is the widest of the four areas, and C is above the surrogate's (p = 0 at printed precision, all five seeds; per-population Wilcoxon p = 7.7e-86). The 0th to 100th span misses on H (0.353) and C (0.441, against 0.440). Every unit reading gives the same outcome; it rests on the percentile reading of a span.\"\"\"\n\nM[80] = \"\"\"**Result: reproduced.** The midbrain span (H 0.938 to 0.971, C 0.075 to 0.150) is inside the widened ranges, its C span (0.074) is the narrowest of the four, and C is above the surrogate's (Mann-Whitney p = 2.1e-166, at most 8.4e-161 over five seeds; per-population Wilcoxon p = 8.9e-23). Under the 0th to 100th span H starts at 0.808, below 0.81, and the C span is not the narrowest. Every unit reading gives the same outcome; it rests on the percentile reading of a span.\"\"\"\n\nM[83] = \"\"\"**Result: not reproduced.** None of the eight fractions is within tolerance on the active windows (for example VIS 10.45% in [0, 0.1) against 4.9%, TH 43.17% against 24.6%, MB 32.03% in [0.1, 0.2) against 45.4%), and none on the natural-image windows. Every unit reading gives the same outcome.\"\"\"\n\nM[84] = \"\"\"## Medians of C by condition (claims of Fig. 4a to 4d)\n\nThe medians of C are computed with those of CV, above, for each unit reading.\"\"\"\n\nM[88] = \"\"\"**Result: not reproduced.** All medians fall in the quoted ranges (natural images 0.158 to 0.258, spontaneous 0.094 to 0.098, active and blanks 0.102 to 0.187), and the legend's narrower ranges for VISl, VISal and VISp are met, but the order fails in VISp, where the natural-image median (0.174) is below the active one (0.187) and close to the blank one (0.175; Mann-Whitney p = 0.77 to 0.83); the other 35 of 36 pairwise tests give p < 0.001. The partial rule needs the order, so the claim is not reproduced. Every unit reading gives the same outcome.\"\"\"\n\nM[89] = \"\"\"## fig4b-thalamus-lgd-lp-modulated\n\n> Of nine thalamic nuclei, only LGd and LP show significant modulation of complexity across conditions (p < 0.001), higher during visually driven states (0.14 to 0.18) than spontaneous activity (0.11 to 0.12), with smaller effects than visual cortex.\n\nThe effect is the visually driven minus spontaneous median, taken (i) as the largest visually driven median minus the spontaneous one and (ii) as the mean of the three visually driven medians minus the spontaneous one; the claims file does not fix it, and both are shown.\"\"\"\n\nM[91] = \"\"\"**Result: not reproduced.** LGd and LP are modulated under both test readings (Kruskal-Wallis p at most 6.4e-66 and 3.3e-64; every visually driven condition against spontaneous p at most 3.2e-21 and 7.4e-20), and their visually driven medians (0.112 to 0.149) exceed the spontaneous ones (0.094 to 0.098). LGd matches the legend's values, but LP's spontaneous median (0.098 under every condition reading) falls just below the legend's 0.11 - 0.011 = 0.099, and neither nucleus matches the text's (LGd active 0.121 and LP active 0.123 below 0.126), so the value part fails. The effects of LGd (0.054 to 0.056) and LP (0.044 to 0.045) are below every visual area's under form (i) (0.062 to 0.163); under form (ii) LGd (0.032 to 0.034) is above VISrl (0.028 to 0.030). Under 'all' and 'qc' LP's spontaneous median is within the legend's range and the claim is reproduced, so the outcome turns on the unit reading.\"\"\"+NOTE_U\n\nM[94] = \"\"\"**Result: not reproduced.** The medians of the seven nuclei are 0.092 to 0.107, inside 0.09 to 0.143, and their largest condition difference is at most 0.0055, but both test readings find modulation: Kruskal-Wallis gives p < 0.001 in MGd, SGN, MGm and MGv (5.7e-08 to 7.3e-04), and the pairwise reading (a nucleus is modulated when any visually driven condition differs from spontaneous at p < 0.001, the reading suited to a claim of absence) finds MGd, SGN and MGv (smallest p 1.6e-07, MGv images against spontaneous). Only the lenient form of the pairwise reading, which counts a nucleus as modulated when all three conditions differ, finds none (or SGN alone under b/a). Every unit reading gives the same outcome.\"\"\"\n\nM[97] = \"\"\"**Result: reproduced.** Under the legend's reading, with every condition reading, DG natural images 0.116, CA3 0.107 and CA1 0.095 match the legend's 0.12, 0.11 and 0.10, DG (0.179 to 0.251), CA3 (0.130 to 0.188) and CA1 (0.118 to 0.158) match their elevated ranges in the other conditions, POST, ProS and SUB lie in 0.096 to 0.135, and DG and CA3 peak in spontaneous activity. The text's reading fails (CA3 inside its range in 2 of 4 conditions; CA1 0.095 in natural images and 0.155 in spontaneous activity outside 0.099 to 0.165). Every unit reading gives the same outcome; it rests on the legend reading.\"\"\"\n\nM[100] = \"\"\"**Result: reproduced.** Under the legend's values every condition median of NB (0.104 to 0.111), MRN (0.094 to 0.101), SCig (0.095 to 0.097) and APN (0.086 to 0.089) lies in its widened range, and NOT has the largest range across conditions (0.055 to 0.057, from 0.101 to 0.159, against at most 0.007). Under the text's values APN falls below 0.09. 'all' gives the same; 'qc' does not keep NOT, so the claim cannot be judged under it. The outcome rests on the legend reading.\"\"\"+NOTE_U\n\nM[101] = \"\"\"## JS divergence matrices of C (claims of Figs. 4e to 4h)\n\nAs for CV: per condition, JS divergence between the C distributions of every pair of subregions, with 50 and 100 histogram bins, in bits and (claims file, variant) in natural logs.\"\"\"\n\nM[44] = \"\"\"## JS divergence matrices of CV (claims of Fig. 2b)\n\nFor each condition, the JS divergence between the CV distributions of every pair of subregions, with 50 and 100 equal histogram bins over the pooled range of each pair, in bits and, as the claims file's variant, in natural logs (the bits value times ln 2). The sums are within each major area: (all) every pair of its block; (adjacent) the first off-diagonal in Table I order. Percentage differences, which do not depend on the log base: (second) |A - B| / B; (mean) |A - B| over the mean of A and B.\"\"\"\n\nM[105] = \"\"\"**Result: not reproduced.** In natural images (bits) all or most VIS-VIS divergences are below 0.22 (0.80 to 1.00) and most VIS-TH (0.70 to 0.72) and VIS-MB (0.73 to 0.77) divergences exceed 0.36, but only 0.18 to 0.20 of the pairs of DG or CA3 with other subregions lie in 0.27 to 0.55 (median 0.199 to 0.217). In natural logs the VIS-TH and VIS-MB parts fail too (0.37 to 0.43). Every unit reading gives the same outcome.\"\"\"\n\nM[108] = \"\"\"**Result: not reproduced.** Fewer than half of the pairs of a visual subregion with a subcortical one exceed 0.36 (0.38 in active behavior, 0.31 to 0.34 in blanks, in bits; medians 0.189 to 0.265), and 0.33 of the hippocampal pairs in active behavior lie in 0.18 to 0.44 (0.13 in natural logs). Every unit reading gives the same outcome.\"\"\"\n\nM[111] = \"\"\"**Result: not reproduced.** The mean visual-to-other divergence is lowest in spontaneous activity (bits: 0.215 to 0.265 against 0.274 to 0.518), as the statement says, but the mean of all pairs is not (0.282 to 0.353 in spontaneous against 0.226 to 0.322 in the others), only 0.26 to 0.40 of the spontaneous visual-to-other pairs lie in 0.18 to 0.44, and midbrain pairs are below 0.22 in all conditions only in some natural-log readings (in bits 0.2 to 0.3 of them in spontaneous activity). No reading meets all three parts. Every unit reading gives the same outcome.\"\"\"\n\nM[114] = \"\"\"**Result: partially reproduced.** The pattern (natural images above spontaneous in every visual area, and a larger visually driven minus spontaneous difference in visual cortex than in midbrain) holds for 4 of the 5 combinations; with bin 20 ms, D = 3, tau = 4 natural images exceed spontaneous in 2 of 6 visual areas and the visual difference is -0.0002. Every unit reading gives the same outcome. It rests on this notebook's form of the area difference.\"\"\"\n\nM[115] = \"\"\"## Complexity against CV (claims of Fig. 5)\n\nPer area and condition, windows binned by CV, the mean C and its standard error per bin. Readings: bin width 0.1 or 0.05, with no minimum count or a minimum of 10 windows per bin. Spans are the occupied bins (lower edge of the first to upper edge of the last) and the range of bin means. Reading a/a of the conditions; the condition readings change the spontaneous and blank windows only slightly (medians above). The table and figure are for 'vbn'.\"\"\"\n\nM[119] = \"\"\"**Result: not reproduced.** Complexity rises with CV in visual cortex in the three visually driven conditions (Spearman 0.640, 0.844 and 0.836; monotonic under bins of 0.05 with at least 10 windows), but no reading matches all spans: the natural-image bins reach CV 1.00 to 1.40 against 0.9 +/- 0.09, and without a minimum count the spontaneous maximum of the bin means is 0.337 to 0.350; with at least 10 windows per bin the spontaneous maximum is 0.153, below 0.165, but the natural-image and blank spans miss. Every unit reading gives the same outcome.\"\"\"\n\nM[122] = \"\"\"**Result: not reproduced.** In each visually driven condition the thalamic slope is positive and below the visual one (0.094 to 0.129 against 0.226 to 0.372), but the thalamic spans are wider than CV 0.18 to 0.88 and C 0.09 to 0.22 under every reading (for example CV from 0.10 or 0.15, and up to 1.05 in active behavior with bins of 0.05 and at least 10 windows). Every unit reading gives the same outcome.\"\"\"\n\nM[125] = \"\"\"**Result: not reproduced.** The hippocampal spontaneous bin means at CV 0.4 to 0.7 reach 0.227 to 0.239, within 0.25 +/- 0.025, but they do not exceed the hippocampal maximum of every visually driven condition (active 0.198 to 0.441), and the visually driven maxima are not all within 0.19 +/- 0.019 (natural images 0.135 with at least 10 windows per bin, 0.336 without). Every unit reading gives the same outcome.\"\"\"\n\nM[128] = \"\"\"**Result: not reproduced.** The midbrain slope of C on CV is the smallest of the four areas in all four conditions, and its bin means lie in range in natural images and spontaneous activity, but in active behavior and blanks they start at 0.084, below 0.09, under every reading. Every unit reading gives the same outcome.\"\"\"\n\nM[131] = \"\"\"**Result: not reproduced.** The visual medians in active behavior and blanks are 0.014 to 0.055 (50 ms) and 0.007 to 0.031 (20 ms), below 0.072, and the natural-image and spontaneous medians are 0.005 to 0.038, half or more of them above 0.011. Midbrain medians vary by less than 0.02 across conditions except NOT (0.023 to 0.024 at 50 ms). Every unit reading gives the same outcome.\"\"\"\n\nM[134] = \"\"\"**Result: reproduced.** Under the JS reading, in all six visual subregions the divergence between natural images and spontaneous activity is larger for complexity (0.437 to 0.837, reading a/a, 50 bins) than for CV (0.249 to 0.537) and mean correlation (0.189 to 0.479), under every condition and histogram reading. Under the IQR reading it holds in 1 or 2 of 6, since the CV and correlation IQRs of the two conditions often do not overlap either. Every unit reading gives the same outcome; it rests on the JS reading.\"\"\"\n"
}
```

```
File created successfully at: /tmp/claude-1001/cells_md.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
p="cells_md.py"; s=open(p).read()
rep = [
("and the DG and CA3 values (0.002 to 0.153) lie below 0.135; under reading b no visual or thalamic subregion passes.",
 "and the DG and CA3 values (0.002 to 0.153) lie mostly below 0.135; under reading b no visual or thalamic subregion passes (DG and CA3 0.024 to 0.418)."),
("(within 0.84 +/- 0.084 for 100 bins and the spontaneous reading b, 0.791 at most)", "(within 0.84 +/- 0.084 with 100 bins, 0.785 to 0.791)"),
("The text's reading fails (CA3 inside its range in 2 of 4 conditions; CA1 0.095 in natural images and 0.155 in spontaneous activity outside 0.099 to 0.165).",
 "The text's reading fails: CA3 is inside its range in 2 of 4 conditions, and CA1 (0.095 in natural images) falls below 0.099."),
("(Kruskal-Wallis p at most 6.4e-66 and 3.3e-64; every visually driven condition against spontaneous p at most 3.2e-21 and 7.4e-20)",
 "(Kruskal-Wallis p at most 6.4e-66 and 3.0e-64; every visually driven condition against spontaneous p at most 3.2e-21 and 2.9e-19)"),
("(H 0.930 to 0.969,", "(H 0.929 to 0.969,"),
]
for a,b in rep:
    assert a in s, a[:40]; s=s.replace(a,b)
open(p,"w").write(s)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent**

Now the header and summary cells.

**Agent calls Bash**

```bash
cat >> $TMPDIR/cells_md.py <<'PYEOF'

OUTC = {
 "table1-sample": "not reproduced", "fig1c-cv-region-medians": "partially reproduced (assumed)", "fig1c-cv-above-surrogate": "partially reproduced (assumed)",
 "fig1d-surrogate-abolishes-cv-correlations": "not reproduced (assumed)", "fig1e-positive-cv-modules": "reproduced (assumed)",
 "fig1e-dg-ca3-anticorrelation-hubs": "reproduced (assumed)", "fig1e-midbrain-weakest-cv-correlations": "not reproduced (assumed)",
 "fig2a-vis-cv-by-condition": "reproduced (assumed)", "fig2a-thalamus-cv-by-condition": "reproduced (assumed)", "fig2a-hippocampus-cv-stable": "reproduced (assumed)",
 "fig2a-midbrain-cv-invariant": "not reproduced (assumed)", "fig2b-vis-summed-js-cv": "partially reproduced (assumed)", "fig2b-hp-mb-summed-js-cv": "not reproduced (assumed)",
 "fig2b-visually-driven-js-cv-low": "partially reproduced (assumed)", "fig2b-dg-ca3-high-js-cv": "not reproduced (assumed)", "fig2b-legend-js-cv": "not reproduced (assumed)",
 "fig3a-reference-systems": "partially reproduced (synthetic series, assumed)", "fig3b-complexity-levels-by-region": "reproduced (assumed)", "fig3c-vis-ch-plane": "not reproduced (assumed)",
 "fig3d-th-ch-plane": "reproduced (assumed)", "fig3e-hp-ch-plane": "reproduced (assumed)", "fig3f-mb-ch-plane": "reproduced (assumed)",
 "fig3-complexity-range-fractions": "not reproduced (assumed)", "fig4a-vis-complexity-by-condition": "not reproduced (assumed)",
 "fig4b-thalamus-lgd-lp-modulated": "not reproduced (assumed)", "fig4b-other-thalamus-not-modulated": "not reproduced (assumed)", "fig4c-dg-ca3-complexity": "reproduced (assumed)",
 "fig4d-midbrain-complexity-invariant": "reproduced (assumed)", "fig4e-js-complexity-natural-images": "not reproduced (assumed)", "fig4fg-js-complexity-active-blanks": "not reproduced (assumed)",
 "fig4h-js-complexity-spontaneous-converges": "not reproduced (assumed)", "supp-robustness-parameters": "partially reproduced (assumed)", "fig5-vis-complexity-cv-coupling": "not reproduced (assumed)",
 "fig5-th-weaker-coupling": "not reproduced (assumed)", "fig5-hp-spontaneous-elevated": "not reproduced (assumed)", "fig5-mb-flat": "not reproduced (assumed)",
 "supp-fig6-mean-correlation": "not reproduced (assumed)", "complexity-separates-images-from-spontaneous": "reproduced (assumed)"}

M[135] = "## Summary\n\n| Claim | Outcome |\n|---|---|\n" + "\n".join(f"| {k} | {v} |" for k, v in OUTC.items()) + """

"Assumed" marks an outcome that rests on a choice the paper does not make; the first of them, for every claim on the recordings, is the unit selection: the 'vbn' filter (snr > 1, ISI violations < 1, firing rate > 0.1 spikes/s, the filter of the Allen Institute's Visual Behavior Neuropixels tutorial), whose neuron counts per population match Table I within 5% in each area. The table before this summary gives each criterion under the claims file's two unit readings too; ten claims (fig1c-cv-region-medians, fig1e-positive-cv-modules, fig1e-dg-ca3-anticorrelation-hubs, fig2a-vis-cv-by-condition, fig2a-thalamus-cv-by-condition, fig2a-hippocampus-cv-stable, fig2b-vis-summed-js-cv, fig3c-vis-ch-plane, fig4b-thalamus-lgd-lp-modulated, fig4d-midbrain-complexity-invariant) come out differently under 'all' or 'qc'.

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method.

How the analysis differs from the paper's. The paper's 102 sessions are not identified, and every one of the 153 ecephys sessions of the dandiset meets both session readings, so all 153 are used; no grouping by genotype, image set, novelty or probe count gives 102, and the populations and windows are about 1.5 times the paper's. The unit filter is not stated; the 'vbn' filter is adopted because it matches Table I's neurons per population. The surrogate of each window is drawn once under the seed of `fig1c-cv-above-surrogate` (and four more) and serves every claim on surrogates. The JS histograms and log base, spans, the blank and spontaneous windows, the test of "modulation", the session combination of Fig. 1d and 1e and several effect sizes are readings named in the claims file or in the claim sections above, each shown. Tests on windows treat windows as independent, as the paper appears to; the C-H and surrogate comparisons are repeated on one median per population.

What was found about the dataset. The 153 sessions (81 mice) each hold an active block of 3599 to 3611 s, a 289-s gray screen after it and eight images; no recording appears twice (no shared spike-time fingerprint, spike count, or subject and start time). The visual cortex responds to every session's flash onsets and not to onsets shifted into the gray screen or to omitted flashes, so the spike times and the stimulus table share a clock in all 153 sessions. An image is shown 320 to 1056 times per session (median 572.5), so its blank series is about 286 s long (median), not the "approximately 240 s" of Methods II.A, which would need 480 flashes; leaving out change flashes gives 271 s. The location labels include generic ones (`TH`, `MB`, `HPF`) for units the atlas did not assign to a subregion. About 17% of units carry the quality label 'noise' in the first session; the units table holds the metrics (snr, ISI violations, firing rate) that the Allen tutorial's filter uses."""

M[0] = """# Reproducing de Paula et al. (2026) from DANDI:000713

Paper. E. V. de Paula, R. M. Jungmann, A. J. Fontenele, L. A. A. Aguiar, P. V. Carelli, F. S. Matias, M. Copelli and N. A. P. de Vasconcelos, "Revealing Stimulus-Dependent Dynamics Through Statistical Complexity", PRX Life 4, 023018 (2026), doi:10.1103/wndc-k654.

Dataset. DANDI:000713, "Allen Institute - Visual Behavior - Neuropixels", version 0.240702.1725 (doi:10.48324/dandi.000713/0.240702.1725). This is the version the paper cites (its Ref. 22, as the claims file gives it), and it is the only published version of the dandiset; the draft has the same 4293 assets and was last modified on 2024-07-02, when this version was published. The 153 ecephys session files are streamed from the archive; nothing is written to disk.

Text. The claims file `claims/paula-2026.yaml` was written from the version of record (corrected 22 July 2026) and its Supplemental Material. The paper links no analysis code.

Claims. All 38 claims of the claims file are tested here; none is blocked. Claim `fig3a-reference-systems` uses synthetic series only (`data: elsewhere`, no recordings). The outcomes are in the attempt record and the summary at the end.

| Claim | Tested here |
|---|---|
""" + "\n".join(f"| {k} | tested" + (" (synthetic series)" if k == "fig3a-reference-systems" else "") + " |" for k in OUTC) + """

Method. The helper module `paula.py` reads each session and computes, for every local population (the units of one subregion in one session with at least 30 units) under each of three unit readings, and every 100-s window of the four conditions, the CV, the permutation entropy H and the statistical complexity C of the population rate, the same for an ISI-shuffled surrogate, the mean pairwise correlation (visual cortex and midbrain), and C and H for the parameter combinations of the supplement. The unit readings are 'vbn' (adopted; the filter of the Allen Institute's Visual Behavior Neuropixels tutorial, which matches Table I's neurons per population), and the claims file's 'all' and 'qc'. Its docstring says where each parameter comes from. Every claim's section below starts from that table and gives the criterion under each unit reading."""
PYEOF
python - <<'EOF'
import os
T=os.environ["TMPDIR"]
s=open(f"{T}/assemble.py").read()
if "cells_md" not in s:
    s=s.replace('json.dump(nb, open(dst, "w")', '''nsm = {}
exec(open(f"{T}/cells_md.py").read(), nsm)
for i, txt in nsm["M"].items():
    assert cells[i]["cell_type"] == "markdown", i
    cells[i]["source"] = txt.strip("\\n").splitlines(keepends=True)
json.dump(nb, open(dst, "w")''')
    # markdown edits must happen before insertion of new cells: move insertion after
    open(f"{T}/assemble.py","w").write(s)
EOF
grep -n "cells\[135:135\]\|nsm\|json.dump" $TMPDIR/assemble.py
```

```
24:    cells[135:135] = [hdr, new]
25:nsm = {}
26:exec(open(f"{T}/cells_md.py").read(), nsm)
27:for i, txt in nsm["M"].items():
30:json.dump(nb, open(dst, "w"), indent=1, ensure_ascii=False)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open("assemble.py").read()
s=s.replace('''for i, txt in nsm["M"].items():
    assert cells[i]["cell_type"] == "markdown", i
    cells[i]["source"]''','''for i, txt in nsm["M"].items():
    i = i + 2 if i >= 135 else i
    assert cells[i]["cell_type"] == "markdown", i
    cells[i]["source"]''')
open("assemble.py","w").write(s)
EOF
cd  && python $TMPDIR/assemble.py && python - <<'EOF'
import json
nb=json.load(open("entries/paula-2026/reproduce_paula_2026.ipynb"))
import re
for i,c in enumerate(nb["cells"]):
    s="".join(c["source"])
    if "—" in s or re.search(r"\brather\b", s): print("bad text in", i)
    if c["cell_type"]=="markdown" and s.startswith("**Result") and "unit-selection assumption" in s: print("stale", i)
print("".join(nb["cells"][137]["source"])[:300])
EOF
grep -n "—\|rather" entries/paula-2026/paula.py | head
```

```
ok 138
## Summary

| Claim | Outcome |
|---|---|
| table1-sample | not reproduced |
| fig1c-cv-region-medians | partially reproduced (assumed) |
| fig1c-cv-above-surrogate | partially reproduced (assumed) |
| fig1d-surrogate-abolishes-cv-correlations | not reproduced (assumed) |
| fig1e-positive-cv-modules
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json,os
nb=json.load(open("entries/paula-2026/reproduce_paula_2026.ipynb"))
for i,c in enumerate(nb["cells"]):
    s="".join(c["source"])
    if c["cell_type"]=="markdown" and not s.startswith("**Result") and not s.startswith("## Summary") and i not in (0,):
        body = s.split("\n>")[0]
        rest = s[len(body):]
        tail = "\n".join(l for l in s.splitlines() if not l.startswith(">") and not l.startswith("##"))
        if tail.strip(): print(i, "|", tail.strip()[:400]); print()
EOF
```

```
2 | One pass over all ecephys sessions, four sessions at a time in separate processes. Each session's spike times are read up to the end of its spontaneous epoch, and every population is measured under the three unit readings ('vbn', 'all', 'qc'). This takes about 46 minutes.

5 | The stimulus table and the spike times must share a clock. For every session the notebook counts the visual cortex spikes 30 to 130 ms after each flash onset minus those in the 100 ms before, for the true onsets and for onsets shifted by 375 ms into the gray screen, and for the omitted flashes (no image appears, so no response is expected).

7 | The claims file names two unit readings, 'all' units and 'qc' (ISI violations < 0.5, amplitude cutoff < 0.1, presence ratio > 0.9), and says that Table I's neuron counts decide between them. The dandiset has 153 sessions against the paper's 102, so totals cannot be compared as they stand: the comparison that can tell filters apart is per population (neurons per population) or after scaling the tot

10 | The adopted unit reading is 'vbn' (assumption, above); every claim is also run under 'all' and 'qc', and each claim cell prints the criterion's verdict under each unit reading. The surrogate is drawn under five seeds for 'vbn' only. The four condition readings combine the blank reading (a: after every shown flash; b: only after flashes followed by another flash) with the spontaneous reading (a: th

15 | One surrogate per active window (Methods II.E). The surrogate is drawn under the seed of this claim, `zlib.crc32(b"paula-2026/fig1c-cv-above-surrogate")`, and under that seed plus 1000, 2000, 3000 and 4000; the same surrogates serve the claims of Figs. 1d and 3 (see the deviations).

18 | Per pair of subregions recorded in the same session, the Pearson correlation of their 10-s CV series over the active windows (360 values per session at most). Reading (a) concatenates the series of all shared sessions; reading (b) averages the per-session correlatio
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/cells_md.py <<'PYEOF'

M[15] = """## fig1c-cv-above-surrogate

> Empirical CV exceeds that of ISI-shuffled surrogates in every brain region (VIS 2 to 3 times, surrogate medians 0.21 to 0.24; TH 1.3 to 1.6; HP 1.5 to 2.2; MB 1.3 to 1.9), with Mann-Whitney p < 0.001 for all regions.

One surrogate per active window (Methods II.E). The surrogate is drawn under the seed of this claim, `zlib.crc32(b"paula-2026/fig1c-cv-above-surrogate")`, and, for the adopted unit reading, under that seed plus 1000, 2000, 3000 and 4000; the same surrogates serve the claims of Figs. 1d and 3 (see the deviations)."""

M[92] = """## fig4b-other-thalamus-not-modulated

> The other seven thalamic nuclei (MGd, PoT, SGN, POL, MGm, MGv, PIL) keep uniformly low complexity (0.10 to 0.13) with no significant stimulus dependence.

Test readings: Kruskal-Wallis across the four conditions, and the pairwise Mann-Whitney tests of each visually driven condition against spontaneous activity. For this claim of absence a nucleus counts as modulated under the pairwise reading when any of its three pairs reaches p < 0.001; the lenient form (all three pairs) is shown too. All six pairwise p-values of each nucleus are printed."""
PYEOF
python $TMPDIR/assemble.py && python tools/entry.py check entries/paula-2026 2>&1 | tail -3; date -u
```

```
ok 138
0 error(s)
Fri Nov 27 15:52:59 UTC 2026
```

**Agent calls Bash**

```bash
cat entries/paula-2026/README.md
```

```
# de Paula, Jungmann, Fontenele, Aguiar, Carelli, Matias, Copelli & de Vasconcelos (2026) from dandiset 000713

Tests the findings of [de Paula et al. (2026)](https://doi.org/10.1103/wndc-k654), "Revealing
Stimulus-Dependent Dynamics Through Statistical Complexity", on
[DANDI:000713](https://dandiarchive.org/dandiset/000713/0.240702.1725), the Allen Institute Visual
Behavior Neuropixels dataset. The notebook streams all 153 ecephys sessions and computes, for every
local population and 100-s window, the CV, permutation entropy and statistical complexity of the
population rate, with ISI-shuffled surrogates, JS divergences between regions, complexity-CV
trajectories and mean pairwise correlations.

| Claims | Outcome |
|---|---|
| CV by condition in visual cortex and thalamus; complexity time course by area; thalamic, hippocampal and midbrain complexity by condition; C-H spans of thalamus, hippocampus and midbrain; complexity separates images from spontaneous activity (13 claims) | Reproduced |
| CV against surrogates; CV correlation modules and hubs; hippocampal and midbrain CV; JS of CV in visual cortex and DG/CA3; reference systems; visual C-H plane; complexity by condition in visual cortex; JS of complexity in natural images; parameter robustness; complexity-CV coupling in visual cortex, thalamus and midbrain (15 claims) | Partially reproduced |
| Table I counts; CV medians by region; surrogate CV correlations; JS of CV in hippocampus and midbrain and in the Fig. 2b legend; complexity range fractions; JS of complexity in active behavior, blanks and spontaneous activity; hippocampal spontaneous complexity; mean pairwise correlation (10 claims) | Not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper's 102 sessions and its unit selection are not stated, and neither reading of them in the
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
p="entries/paula-2026/README.md"; s=open(p).read()
a=s.index("| Claims | Outcome |"); b=s.index("A failure to reproduce")
s=s[:a]+"""| Claims | Outcome |
|---|---|
| CV modules and DG/CA3 hubs of Fig. 1e; CV by condition in visual cortex, thalamus and hippocampus; complexity time course by area; C-H spans of thalamus, hippocampus and midbrain; hippocampal and midbrain complexity by condition; complexity separates images from spontaneous activity (12 claims) | Reproduced |
| CV medians by region; CV against surrogates; summed JS of CV in visual cortex; JS of CV among visually driven conditions; reference systems; parameter robustness (6 claims) | Partially reproduced |
| Table I counts; surrogate CV correlations; midbrain CV correlations; midbrain CV; JS of CV in hippocampus, midbrain, DG/CA3 and the Fig. 2b legend; visual C-H plane; complexity range fractions; complexity by condition in visual cortex and thalamus; JS of complexity in every condition; complexity-CV coupling in every area; mean pairwise correlation (20 claims) | Not reproduced |

"""+s[b:]
a=s.index("The paper's 102 sessions"); 
s=s[:a]+"""The paper's 102 sessions and its unit selection are not stated. All 153 sessions are used. Every
claim is run under three unit selections: the claims file's two (all units, and ISI violations,
amplitude cutoff and presence ratio filters) and the unit filter of the Allen Institute's Visual
Behavior Neuropixels tutorial (snr > 1, ISI violations < 1, firing rate > 0.1 spikes/s). The last is
adopted, as its neurons per population match Table I within 5% in each area; ten outcomes would
differ under one of the other two. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/paula-2026-01.yaml`](../../attempts/paula-2026-01.yaml).

The notebook takes about 47 minutes, most of it reading the spike times from the archive.
"""
open(p,"w").write(s)
p="entries/paula-2026/entry.yaml"; s=open(p).read()
s=s.replace("with ISI-shuffled surrogates, JS divergences between regions, complexity-CV trajectories and mean pairwise correlations,\n  over all 153 ecephys sessions.",
 "with ISI-shuffled surrogates, JS divergences between regions, complexity-CV trajectories and mean pairwise correlations,\n  over all 153 ecephys sessions and under three unit selections.")
open(p,"w").write(s)
EOF
grep -n "three unit" entries/paula-2026/entry.yaml; python tools/entry.py check entries/paula-2026 | tail -1
```

```
0 error(s)
```

**Agent calls Bash**

```bash
sed -i 's/  correlations, over all 153 ecephys sessions\./  correlations, over all 153 ecephys sessions and under three unit selections./' entries/paula-2026/entry.yaml; grep -n "153" entries/paula-2026/entry.yaml
```

```
10:  correlations, over all 153 ecephys sessions and under three unit selections.
```

**Agent**

Notebook, helper, README and entry are final. Starting the second full run (about 47 minutes); I'll write the attempt record and the questions file after it, from its outputs.

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/paula-2026 2>&1 | tail -5; date -u
```

```
Fri Nov 27 15:53:34 UTC 2026
Installed kernelspec registry-paula-2026 in executed/paula-2026/.venv/share/jupyter/kernels/registry-paula-2026
0 error(s)
pass  reproduce_paula_2026.ipynb  (2810 s)
Fri Nov 27 16:40:34 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF' > $TMPDIR/run2_out.txt
import json
nb = json.load(open("executed/paula-2026/reproduce_paula_2026.ipynb"))
for i, c in enumerate(nb["cells"]):
    if c["cell_type"] != "code": continue
    print("=== cell", i, c["metadata"].get("tags"))
    for o in c.get("outputs", []):
        if o.get("output_type") == "error": print("ERROR", o.get("ename"))
        t = o.get("text") or o.get("data", {}).get("text/plain", "")
        if "Figure" in "".join(t): continue
        print("".join(t))
EOF
grep -c ERROR $TMPDIR/run2_out.txt; diff <(sed -n '/=== cell 13/,$p' $TMPDIR/run1_out.txt) <(sed -n '/=== cell 13/,$p' $TMPDIR/run2_out.txt) | head -20; python $TMPDIR/show.py executed/paula-2026/reproduce_paula_2026.ipynb 136 | head -45
```

```
0
320d319
< 
321a321
> 
562a563
> 
600d600
< 
604a605
> 
713a715
> 
717d718
< 
798a800
> 
1049d1050
< 
1057a1059
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
head -5 questions/bech-2026.yaml; grep -n "^[a-z]" questions/bech-2026.yaml | head; ls schemas; grep -rn "questions/" tools/entry.py | head -5
```

```
dandiset: "001847"
paper: doi:10.7554/elife.109717
questions:
- claim: fig2d-auditory-a1-frontal
  asked: 2026-11-04
1:dandiset: "001847"
2:paper: doi:10.7554/elife.109717
3:questions:
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
```

**Agent calls Bash**

```bash
sed -n 1,30p questions/bech-2026.yaml; grep -rln "asked:" questions | head -3; grep -h "^  [a-z_]*:" questions/*.yaml | sed 's/:.*//' | sort | uniq -c
```

```
dandiset: "001847"
paper: doi:10.7554/elife.109717
questions:
- claim: fig2d-auditory-a1-frontal
  asked: 2026-11-04
  question: The opening comment's null (i) for the opto map shuffles the block labels of whole blocks
    and recomputes ΔP(Lick) against the control trials. Under that null the laser trials keep their
    outcomes and only their context labels move, so an effect of the laser that is shared by both
    contexts stays inside the null and gives d' near 0. Can null (i) be a reading of the paper for
    Figures 2C to 2E, whose Results describe effects "similar across contexts" (Figure 2D) and present
    "across both contexts" (Figure 2E)? The same reading decides fig2c-catch-little-effect,
    fig2e-whisker-sensory-premotor-reduction, fig2e-rsc-tjs1-increase-wminus and
    fig2cd-rsc-no-effect-catch-auditory.
  passage: Figure 2C legend, "d' computed between the distribution of ΔP(Lick) in stim trials and a null
    distribution computed by shuffling all trials 1,000 times"; Figure 2 figure supplement 1D legend,
    "a null distribution computed by shuffling all trials 1,000 times"; the Methods (Quantification,
    Figures 2C-E) describe shuffling block labels.
  why: On synthetic data with a laser effect of -0.2 in both contexts the notebook's null (i) has a mean
    of -0.22 and gives d' 0.19, while null (ii) gives d' above 5. In the data null (i) gives d' of at most
    0.57 at every named site, and its null means range from -0.35 to 0.18. Because every criterion
[... 21 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "questions/paula-2026.yaml",
 "content": "dandiset: \"000713\"\npaper: doi:10.1103/wndc-k654\nquestions:\n- claim: table1-sample\n  asked: 2026-11-27\n  attempt: paula-2026-01\n  question: The opening comment gives unit reading (b) as \"the Allen default filters for this dataset\n    (ISI violations < 0.5, amplitude cutoff < 0.1, presence ratio > 0.9)\". The verifier of attempt\n    paula-2026-01 reports that the AllenSDK default presence-ratio cutoff is 0.95, not 0.9, and the\n    claims file's own check says the defaults were not verified. The Allen Institute's Visual Behavior\n    Neuropixels quickstart tutorial filters units by snr > 1, ISI violations < 1 and firing rate > 0.1\n    spikes/s instead. Should reading (b) give the defaults that apply to this dataset, and should the\n    tutorial's filter be a reading of its own?\n  passage: Methods II.A, \"local neuronal populations from each brain region with at least 30 recorded\n    neurons sampled across a minimum of eight recording sessions\"; Table I, \"Neurons analyzed\". The\n    paper states no unit filter.\n  why: The criterion decides between the unit readings by Table I's neuron counts. Scaled to the paper's\n    102 sessions, all units give 1.28 to 1.43 times Table I's area counts and reading (b) 0.34 to 0.55\n    times (0.31 to 0.51 with presence ratio > 0.95), while the tutorial's filter gives 0.93 to 1.02\n    times, with neurons per population within 5% of Table I's in each area. The attempt adopts the\n    tutorial's filter as an assumption and runs both of the claims file's readings as variants; ten\n    claims come out differently under one of them.\n- claim: fig3a-reference-systems\n  asked: 2026-11-27\n  attempt: paula-2026-01\n  question: The criterion places the sine \"near H 0\" and asks that the positions fall in the quoted\n    ranges widened by 10% of each bound. With D = 6 a sine gives at least two ordinal patterns (rising\n    and falling), so its H cannot be below ln 2 / ln 720 = 0.105, and a range around 0 widened by 10% of\n    0 cannot be met. How should \"H near 0\" be read for the sine?\n  passage: Results III.C, paragraph 2, \"deterministic periodic signals (sine wave) exhibit minimum\n    entropy (H ≈0) and low complexity (C ≈0.1)\"\n  why: The attempt reads \"near 0\" as at most the floor plus 0.05 (0.155); under that reading the sine\n    matches at 10 000 points per period (H 0.107, C 0.106) and not at 1000 or 100 (C 0.113 and 0.165).\n    The claim is partially reproduced in either case, because the Ikeda map and some correlated walks\n    miss, but the sine's part of the outcome depends on this reading.\n"
}
```

```
File created successfully at: questions/paula-2026.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
s=json.load(open("schemas/attempt.schema.json"))
print(json.dumps(s["properties"]["inputs"])[:800])
o=s["properties"]["outcomes"]["items"]
print(list(o["properties"].keys()), o.get("required"))
print(json.dumps(s["properties"]["findings"]["items"])[:1500])
EOF
```

```
{"description": "Everything the attempt used that is not in the dataset.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["what", "source"], "properties": {"what": {"type": "string", "minLength": 1}, "source": {"description": "A DOI, or a repository URL with the commit read.", "type": "string", "minLength": 1}}}}
['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'seed_sensitive', 'proposed'] ['claim', 'outcome']
{"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}, "statement": {"type": "string", "minLength": 1}, "found": {"description": "How the finding was found. Unset: by the attempt itself. `on_prompt`: by the reconcile step of a repeat attempt, which checked a finding of the earlier attempt that this one, made blind, did not report (docs/protocol.md, \"Repeat attempts\").", "enum": ["on_prompt"]}, "about": {"description": "What the finding is about. `data`: the dataset's files or metadata, including where they differ from what the paper says they hold. `paper`: the paper, its methods or its published code, with nothing wrong in the files. Unset: by its kind (docs/protocol.md): `methods_unavailable`, `code_mismatch` and `paper_inconsistency` are about the paper, the other kinds about the data. `other` and `selection_undocumented` must say.", "enum": ["data", "paper"]}, "severity": {"description": "For a finding about the data: how much it harms someone who uses the dataset (docs/protocol.md, the attempt record). `critical`: the data are wrong and nothing shows it, so an analysis gives a wrong result. `major`: a main analysis is blocked or changed, and the user would notice. `minor`: evident from the values or eas
[... 1 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/record.py",
 "content": "import yaml\n\nP = \"attempts/paula-2026-01.yaml\"\nrec = yaml.safe_load(open(P))\nold = {o[\"claim\"]: o for o in rec[\"outcomes\"]}\n\nU = (\"Unit selection assumed (author, step 1.6): the unit filter of the Allen Institute's Visual Behavior Neuropixels \"\n     \"quickstart tutorial (snr > 1, ISI violations < 1, firing rate > 0.1 spikes/s; AllenSDK commit a56bd8ea). The paper \"\n     \"states no unit filter. Scaled to the paper's 102 sessions this filter gives 0.93 to 1.02 times Table I's area neuron \"\n     \"counts and neurons per population within 5% of Table I's, against 1.28 to 1.43 times with all units and 0.34 to 0.55 \"\n     \"times with 'qc' (the claims file's two readings), which are run as variants for every claim.\")\nS = (\"All 153 ecephys sessions are used, against the paper's 102; the paper does not say how its sessions were chosen, every \"\n     \"session meets both session readings of the claims file, and no grouping by genotype, image set, novelty or probe count \"\n     \"gives 102.\")\nSURR = (\"The surrogates are drawn once per active window under the seed of fig1c-cv-above-surrogate (and, for the adopted unit \"\n        \"reading, that seed plus 1000 to 4000, combined with the session and window indices), and the same surrogates serve \"\n        \"the claims of Figs. 1c, 1d and 3c to 3f, so this claim does not have a generator of its own.\")\nFIG1E = (\"Assumed (step 1.6): of the claims file's two session combinations, reading b (per-session correlations averaged) is \"\n         \"adopted, as concatenating the series of different sessions (reading a) mixes session-level differences in CV into one \"\n         \"correlation, as the verifier noted. Reading a is shown.\")\nVAR_SAME = \" 'all' and 'qc' give the same outcome.\"\n\n\ndef oc(claim, outcome, notes, measured=None, extra=(), assumed=True, seed=None, base=True):\n    o = {\"claim\": claim, \"outcome\": outcome, \"notebook\": \"reproduce_paula_2026.ipynb\", \"output\": f\"claim:{claim}\"}\n    if measured is not None:\n        o[\"measured\"] = measured\n    o[\"notes\"] = notes\n    o[\"deviations\"] = ([U, S] if base else []) + list(extra)\n    if assumed:\n        o[\"assumed\"] = True\n    if seed is not None:\n        o[\"seed_sensitive\"] = seed\n    return o\n\n\nO = []\nO.append(oc(\"table1-sample\", \"not_reproduced\",\n    \"Under every unit reading and either session reading there are 153 sessions, not 102, since all 153 sessions have kept \"\n    \"populations and the 289-s spontaneous epoch. Measured values are for 'vbn' (adopted) and session reading a: populations \"\n    \"VIS 875, TH 486, HP 526, MB 247; neurons 81 138, 31 458, 58 901, 24 203; windows 16 764 natural images, 76 796 active, \"\n    \"17 072 blanks, 4268 spontaneous. Scaled by 102/153, 'vbn' gives area neuron counts 1.00, 1.02, 0.93 and 0.94 times \"\n    \"Table I's, subregion ratios 0.79 to 1.21, populations 583, 324, 351 and 165 (Table I 586, 313, 363, 175) and neurons per \"\n    \"population 92.7, 64.7, 112.0 and 98.0 against 92.1, 65.6, 116.8 and 98.1. All units give 1.28 to 1.43 times and 'qc' \"\n    \"0.34 to 0.55 times (qc drops NOT); 'qc' puts the four window counts within tolerance (11 613, 53 151, 11 816, 2954) \"\n    \"because its fewer populations per session offset the excess of sessions. Of the count-only filters, 'good' gives 1.04 \"\n    \"to 1.19 times and 'good' with presence ratio > 0.95 0.73 to 0.96 times.\",\n    [153, 875, 486, 526, 247, 81138, 31458, 58901, 24203, 16764, 76796, 17072, 4268],\n    extra=[], base=False, assumed=False))\nO[-1][\"deviations\"] = [S, \"The selection rule is applied to Table I's 26 subregions; other location labels that pass it (HPF, MB, TH, ZI under 'vbn') are not used.\"]\nO.append(oc(\"fig1c-cv-region-medians\", \"partially_reproduced\",\n    \"Active-behavior medians under 'vbn': VIS 0.416 (VISam) to 0.615 (VISp), TH 0.281 (PIL) to 0.384 (LP), HP 0.256 (CA1) to \"\n    \"0.491 (DG, the highest), MB 0.165 (APN) to 0.469 (NB); every median inside its widened range and every extreme within \"\n    \"tolerance. IQRs miss in 3 of 6 visual subregions (0.150 to 0.213 against 0.108 to 0.198) and 2 of 9 thalamic ones, which \"\n    \"the criterion makes partially reproduced. Under 'all' the medians miss (DG 0.564, NB 0.564, PIL 0.306); under 'qc' LP \"\n    \"0.414 misses; both not reproduced.\",\n    [0.416, 0.615, 0.281, 0.384, 0.256, 0.491, 0.165, 0.469]))\nO.append(oc(\"fig1c-cv-above-surrogate\", \"partially_reproduced\",\n    \"Under 'vbn' empirical median CV exceeds the surrogate median in all 26 subregions; Mann-Whitney p at most 1.4e-51 per \"\n    \"subregion and 0 at printed precision per area; on one median per population (Wilcoxon signed-rank) p at most 3.3e-42, \"\n    \"empirical higher in 246 of 247 to 875 of 875 populations. VIS surrogate medians 0.233 to 0.250, inside 0.189 to 0.264. \"\n    \"Ratios VIS 1.75 to 2.64 (VISam 1.75 and VISrl 1.78 below 1.80), TH 1.29 to 1.60, HP 1.29 to 2.22 (POST 1.29 below \"\n    \"1.35), MB 1.33 to 1.69. Over the five seeds the ratios range 1.286 to 2.644, VIS surrogate medians 0.2325 to 0.2501, \"\n    \"largest p 1.9e-51; the outcome is the same under all five. 'all' and 'qc' are partially reproduced too.\",\n    [1.75, 2.64, 0.233, 0.25, 1.29, 1.6, 1.29, 2.22, 1.33, 1.69],\n    extra=[\"The Mann-Whitney test is two-sided (claims file).\"], seed=False))\nO.append(oc(\"fig1d-surrogate-abolishes-cv-correlations\", \"not_reproduced\",\n    \"Under 'vbn' all 325 subregion pairs share at least one session (median 35). Empirical correlations reach 0.798 (reading \"\n    \"a) and 0.679 (reading b). Surrogate |r| exceeds 0.2 in 147 pairs (a) and 240 pairs (b), largest 0.890 and 0.708; over \"\n    \"the other four seeds the largest |r| is 0.889 to 0.900 (a) and 0.699 to 0.708 (b), with 143 and 235 to 241 pairs above \"\n    \"0.2. The per-window ISI shuffle keeps each 100-s window's spike counts, so surrogate CV follows the population rate, \"\n    \"which co-varies across regions; a shuffle over the whole recording is not tested here.\" + VAR_SAME,\n    extra=[SURR, \"The 0.2 bound is the claims file's, not the paper's.\"], seed=False))\nO.append(oc(\"fig1e-positive-cv-modules\", \"reproduced\",\n    \"Top 10% (32 of 325 pairs) under 'vbn'. Reading b, r 0.478 to 0.680, inside 0.50 +/- 0.05 to 0.67 +/- 0.067, 28 of 32 \"\n    \"within one major area (visual pairs, thalamic nuclei, ProS-SUB and POST-SUB). Reading a, r 0.469 to 0.798 (high end \"\n    \"outside), 21 of 32 within an area. Under 'all' (reading b low end 0.450) and 'qc' (0.572 to 0.777) neither reading \"\n    \"passes.\", [0.478, 0.68], extra=[FIG1E]))\nO.append(oc(\"fig1e-dg-ca3-anticorrelation-hubs\", \"reproduced\",\n    \"Most negative 10% (32 pairs) under 'vbn'. Reading b, DG is in 16 and CA3 in 14 of them, the two most frequent, and the \"\n    \"most negative value is -0.247, within -0.27 +/- 0.027. Reading a, CA3 and NB lead (8 each) and the most negative value \"\n    \"is -0.436. Under 'all' (reading b, -0.178) and 'qc' (-0.359) the value misses.\", [-0.247], extra=[FIG1E]))\nO.append(oc(\"fig1e-midbrain-weakest-cv-correlations\", \"not_reproduced\",\n    \"Mean |r| by area under 'vbn', reading a MB 0.183, HP 0.187, TH 0.253, VIS 0.325; reading b MB 0.210, HP 0.252, TH 0.313, \"\n    \"VIS 0.360; the midbrain is lowest under both, but only 13 (a) and 3 (b) of its 115 pairs lie in -0.044 to 0.033.\" + VAR_SAME))\nO.append(oc(\"fig2a-vis-cv-by-condition\", \"reproduced\",\n    \"Under 'vbn' all four condition readings put all twelve medians within tolerance; a/a VISp 0.615 active, 0.579 blanks, \"\n    \"0.299 spontaneous, 0.399 images; VISl 0.577, 0.485, 0.303, 0.475; VISal 0.561, 0.483, 0.304, 0.484. The order active > \"\n    \"images > spontaneous and blanks > spontaneous holds in the three areas under every reading. 'all' is reproduced (12 of \"\n    \"12 under a/a and b/a); under 'qc' 7 or 8 of 12 are within tolerance (partially reproduced).\",\n    [0.615, 0.579, 0.299, 0.399, 0.577, 0.485, 0.303, 0.475, 0.561, 0.483, 0.304, 0.484],\n    extra=[\"Blank pieces are [stop, min(stop + 0.5 s, next onset)) of each shown flash (reading a) or of flashes followed by a \"\n           \"shown flash (b); spontaneous windows are the first two 100-s windows of the 289-s gray screen (a) or two centred in \"\n           \"it (b), as the claims file lists.\"]))\nO.append(oc(\"fig2a-thalamus-cv-by-condition\", \"reproduced\",\n    \"Under 'vbn' LP 0.384 active and 0.277 to 0.282 spontaneous, LGd 0.328 and 0.225 to 0.226, within tolerance under every \"\n    \"reading. Active minus spontaneous is 0.102 to 0.107 (LP) and 0.102 to 0.103 (LGd), below VISp, VISl and VISal (0.256 to \"\n    \"0.316). 'all' is reproduced; under 'qc' LP active 0.414 misses.\", [0.384, 0.277, 0.328, 0.225]))\nO.append(oc(\"fig2a-hippocampus-cv-stable\", \"reproduced\",\n    \"Under 'vbn' and every condition reading, DG 0.482 to 0.504 and CA3 0.406 to 0.415 across the visually driven conditions, \"\n    \"CA1 0.254 to 0.258, DG spontaneous 0.509 to 0.510 and CA3 spontaneous 0.424 to 0.429, all within tolerance, and the \"\n    \"spontaneous medians of DG and CA3 exceed their visually driven ones. Measured values for a/a (CA1 the value furthest from \"\n    \"0.25). 'qc' is reproduced too; under 'all' DG (0.555 to 0.580) misses.\",\n    [0.482, 0.504, 0.406, 0.415, 0.258, 0.51, 0.424]))\nO.append(oc(\"fig2a-midbrain-cv-invariant\", \"not_reproduced\",\n    \"Under 'vbn' APN 0.164 to 0.165 in the visually driven conditions and 0.142 in spontaneous activity, below 0.144; MRN \"\n    \"lowest 0.171 (spontaneous), below 0.18, highest 0.209 (images), within tolerance. Measured values APN lowest, MRN lowest \"\n    \"and highest. Under 'all' the MRN high end (0.233) misses and under 'qc' all three miss.\", [0.142, 0.171, 0.209]))\nO.append(oc(\"fig2b-vis-summed-js-cv\", \"partially_reproduced\",\n    \"32 combinations (4 condition readings, 50 or 100 bins, all-pair or adjacent sum, two percentage forms). None meets the \"\n    \"full rule; active against blanks is 3.12% to 11.24% in every combination. Four meet the partial rule (100 bins, all-pair \"\n    \"sum, |A - B| over the mean, each condition reading): active against blanks 8.46% to 9.05%, the closest pair, and the \"\n    \"other pairs 19.1% to 43.7%. Measured values for a/a in that combination (active against blanks, and the lowest of the \"\n    \"four pairs against images or spontaneous). 'all' also meets the partial rule (active against blanks 0.32% to 0.53%); \"\n    \"'qc' does not.\", [8.46, 19.1],\n    extra=[\"JS divergences in bits from equal-width histograms over the pooled range of each pair (claims file); percentages do not depend on the log base.\"]))\nO.append(oc(\"fig2b-hp-mb-summed-js-cv\", \"not_reproduced\",\n    \"Under 'vbn' active against spontaneous is the largest hippocampal difference in every combination, as stated, but 44.8% \"\n    \"to 77.6% against 15% +/- 1.5%. The largest midbrain difference is 27.2% to 48.5%, against at most 7.7%, and the midbrain \"\n    \"has the smallest difference in at most 4 of 6 pairs. Measured values for a/a, 50 bins, all pairs, |A - B| / B.\" + VAR_SAME,\n    [45.8, 27.2]))\nO.append(oc(\"fig2b-visually-driven-js-cv-low\", \"partially_reproduced\",\n    \"Under the statement's percentage form no combination has two of three pairs at or below 4.4% (active against blanks 3.1% \"\n    \"to 11.2%, pairs with natural images 18.7% to 49.9%). Under the legend's JS-value form the fraction of VIS-VIS divergences \"\n    \"at most 0.22 is 1.0 (images), 0.73 to 0.87 (active) and 0.73 to 0.93 (blanks) under every condition, histogram and \"\n    \"log-base reading. The finding holds in the legend's form only. The percentage form conflicts with the ~30% separation \"\n    \"of fig2b-vis-summed-js-cv, as the claims file notes.\" + VAR_SAME))\nO.append(oc(\"fig2b-dg-ca3-high-js-cv\", \"not_reproduced\",\n    \"Median divergence from the other 25 subregions under 'vbn', a/a, 50 bins, bits (measured): DG spontaneous 0.713, CA3 \"\n    \"spontaneous 0.443, DG blanks 0.345, CA3 blanks 0.216; over the readings DG spontaneous 0.700 to 0.774 and CA3 0.422 to \"\n    \"0.540 in bits, lower in natural logs. Spontaneous activity gives the largest median for both. Against the other \"\n    \"hippocampal subregions only, DG spontaneous 0.736 to 0.791 (within tolerance with 100 bins), CA3 0.555 to 0.622, blanks \"\n    \"DG 0.529 to 0.545 and CA3 0.333 to 0.356, not within tolerance.\" + VAR_SAME,\n    [0.713, 0.443, 0.345, 0.216],\n    extra=[\"JS in bits, with natural logs as the claims file's variant (bits times ln 2).\"]))\nO.append(oc(\"fig2b-legend-js-cv\", \"not_reproduced\",\n    \"Under 'vbn', reading a (a subregion's own CV distributions between conditions): 3 of 6 visual subregions exceed 0.44 in \"\n    \"bits (0 in natural logs), at most 2 of 9 thalamic subregions exceed 0.33, DG and CA3 values 0.002 to 0.153, mostly below \"\n    \"0.135; midbrain below 0.165 in 13 to 21 of 30. Reading b (row differences of the region-pair matrices): no visual or \"\n    \"thalamic subregion passes; DG and CA3 0.024 to 0.418; midbrain 21 to 26 of 30 below 0.165.\" + VAR_SAME,\n    extra=[\"Reading b of the claims file ('comparing a region's row') is made operational as the mean absolute difference \"\n           \"between a subregion's row in spontaneous activity and in a visually driven condition; the value for spontaneous \"\n           \"against visually driven is the mean over the three visually driven conditions. Neither is fixed by the claims \"\n           \"file or the paper.\", \"JS in bits, with natural logs as the claims file's variant.\"]))\nO.append(oc(\"fig3a-reference-systems\", \"partially_reproduced\",\n    \"D = 6, tau = 1, 10^5 points. White noise H 0.999, C 0.001; logistic r = 4 H 0.629, C 0.484; tent mu = 1.9999 H 0.630, C \"\n    \"0.485, inside C 0.36 to 0.55 and H 0.45 to 0.88. Sine at 10 000 points per period H 0.107, C 0.106, inside its reading; \"\n    \"at 1000 and 100 points C 0.113 and 0.165, outside. Ikeda (u = 0.9) at its chaotic parameter 0.4 shifted by the map's \"\n    \"2 pi period (p = 6.683 and 12.966) H 0.81, C 0.355, just below 0.36; of the sweep p 5 to 17 only p = 6.5 is inside (H \"\n    \"0.794, C 0.367). Exponentially correlated walks with H in 0.27 to 0.66 (alpha 0.2 to 0.7, 4 of 8) have C 0.233 to 0.334, \"\n    \"two of them below 0.27. Fig. 3a's parameter values could not be read from the text.\",\n    base=False,\n    extra=[\"Synthetic series only, from the definitions of Supplemental Material Sec. I; no recordings.\",\n           \"Assumed (step 1.6): near 1 is read as at least 0.9 and C near 0 as at most 0.05 (10% of 0 gives no tolerance); a \"\n           \"sine cannot have H below ln 2 / ln 720 = 0.105 at D = 6, so H near 0 is read as at most 0.155 (the floor plus \"\n           \"0.05), and the sine is sampled at 100, 1000 and 10 000 points per period, the paper giving no sampling; the \"\n           \"logistic and tent maps are judged at r = 4 and mu = 1.9999 (the tent map at mu = 2 collapsing to 0 in floating \"\n           \"point); the Ikeda map, whose p repeats every 2 pi, at 0.4 + 2 pi and 0.4 + 4 pi; the 1/f^k noise is spectral \"\n           \"synthesis with random phases. The reading of H near 0 is asked of a reader (questions/paula-2026.yaml).\"]))\nO.append(oc(\"fig3b-complexity-levels-by-region\", \"reproduced\",\n    \"Reading a (36 active windows) under 'vbn': mean C over windows VIS 0.158, HP 0.159, TH 0.108, MB 0.098, each within \"\n    \"tolerance; the order MB < TH < VIS and HP holds at all 36 indices. Reading b (natural images, 8 indices): VIS 0.204, HP \"\n    \"0.107 and TH 0.118, the order at 0 of 8. Reading a is the one the claims file points to (point counts summing to the \"\n    \"active count). Measured values VIS and HP low and high, TH, MB.\" + VAR_SAME, [0.158, 0.159, 0.108, 0.098]))\nCH_DEV = [SURR, \"Spans are the 2.5th to 97.5th percentiles (claims file, a standard reading), compared unrounded, the 0th to 100th shown.\"]\nO.append(oc(\"fig3c-vis-ch-plane\", \"not_reproduced\",\n    \"31 488 active VIS windows under 'vbn' (paper 21 084). 2.5th to 97.5th percentiles, H 0.857 to 0.965 (inside 0.72 to \"\n    \"1.10), C 0.0887 to 0.283, the low end below 0.090, a narrow miss. Empirical median C 0.149 against surrogate 0.097, \"\n    \"Mann-Whitney p 0 at printed precision under all five seeds; on one median per population Wilcoxon p 1.9e-141; surrogate \"\n    \"median 0.0965 to 0.0966 over the seeds, inside 0.09 to 0.22. The 0th to 100th span misses on H (0.454). Under 'qc' the \"\n    \"C span starts above 0.090 and the claim is reproduced; 'all' misses as 'vbn' does.\", extra=CH_DEV, seed=False))\nO.append(oc(\"fig3d-th-ch-plane\", \"reproduced\",\n    \"17 493 TH windows under 'vbn' (paper 11 265). H 0.929 to 0.969, C 0.081 to 0.167 (2.5th to 97.5th), inside the widened \"\n    \"ranges; C span 0.087 against VIS 0.194; Mann-Whitney p 0 at printed precision, five seeds; per-population Wilcoxon p \"\n    \"1.1e-43. Under the 0th to 100th span, C reaches 0.344, outside.\" + VAR_SAME, extra=CH_DEV, seed=False))\nO.append(oc(\"fig3e-hp-ch-plane\", \"reproduced\",\n    \"18 927 HP windows under 'vbn' (paper 13 059). H 0.858 to 0.967, C 0.086 to 0.298, inside the widened ranges; C span \"\n    \"0.213, the widest (VIS 0.194, TH 0.087, MB 0.074); Mann-Whitney p 0 at printed precision, five seeds; per-population \"\n    \"Wilcoxon p 7.7e-86. The 0th to 100th span misses (H from 0.353, C to 0.441).\" + VAR_SAME, extra=CH_DEV, seed=False))\nO.append(oc(\"fig3f-mb-ch-plane\", \"reproduced\",\n    \"8888 MB windows under 'vbn' (paper 6296). H 0.938 to 0.971, C 0.075 to 0.150, inside the widened ranges; C span 0.074, \"\n    \"the narrowest; Mann-Whitney p 2.1e-166, at most 8.4e-161 over the five seeds; per-population Wilcoxon p 8.9e-23; \"\n    \"empirical median C 0.093 against surrogate 0.088. Under the 0th to 100th span H starts at 0.808 and the C span is not \"\n    \"the narrowest.\" + VAR_SAME, extra=CH_DEV, seed=False))\nO.append(oc(\"fig3-complexity-range-fractions\", \"not_reproduced\",\n    \"Active windows under 'vbn', 0 of 8 within tolerance; VIS [0.3, 0.4] 1.54% and [0, 0.1) 10.45%, TH [0.2, 0.3) 0.44% and \"\n    \"[0, 0.1) 43.17%, HP 2.25% and 14.84%, MB [0.1, 0.2) 32.03% and [0, 0.1) 67.29%. Natural-image windows, 0 of 8.\" + VAR_SAME,\n    [1.54, 10.45, 0.44, 43.17, 2.25, 14.84, 32.03, 67.29]))\nO.append(oc(\"fig4a-vis-complexity-by-condition\", \"not_reproduced\",\n    \"Medians under 'vbn', reading a/a: natural images 0.158 to 0.258, spontaneous 0.094 to 0.098, active and blanks 0.102 to \"\n    \"0.187, all inside the widened ranges under every reading. The order fails in VISp (images 0.174 below active 0.187, and \"\n    \"close to blanks 0.175, Mann-Whitney p 0.77 to 0.83); the other five areas hold it and the other 35 of 36 pairwise tests \"\n    \"give p < 0.001. The partial rule needs the order, so the claim is not reproduced. The legend's ranges for VISl, VISal and \"\n    \"VISp are met. IQRs in visually driven states 0.024 to 0.118, against the legend's 0.08 to 0.12.\" + VAR_SAME,\n    [0.158, 0.258, 0.094, 0.102, 0.187]))\nO.append(oc(\"fig4b-thalamus-lgd-lp-modulated\", \"not_reproduced\",\n    \"Under 'vbn' LGd and LP are modulated: Kruskal-Wallis p at most 6.4e-66 and 3.0e-64; each visually driven condition \"\n    \"against spontaneous p at most 3.2e-21 and 2.9e-19; visually driven medians 0.112 to 0.149 above spontaneous 0.094 to \"\n    \"0.098. LGd matches the legend's values; LP's spontaneous median (0.098 under every condition reading) falls just below \"\n    \"the legend's 0.11 - 0.011, and neither matches the text's (LGd active 0.121, LP active 0.123, below 0.126), so the value \"\n    \"part fails. Effects, form (i) LGd 0.054 to 0.056 and LP 0.044 to 0.045, below every visual area (0.062 to 0.163); form \"\n    \"(ii) LGd 0.032 to 0.034 above VISrl 0.028 to 0.030. Under 'all' and 'qc' LP's spontaneous median is within the legend's \"\n    \"range and the claim is reproduced, so the outcome turns on the unit reading. 'Only LGd and LP' does not hold under \"\n    \"either test: MGd, SGN, MGm and MGv reach p < 0.001 under Kruskal-Wallis (claim fig4b-other-thalamus-not-modulated).\",\n    [0.112, 0.149, 0.094, 0.098],\n    extra=[\"Assumed (step 1.6): the effect compared with visual cortex is the largest visually driven median minus the \"\n           \"spontaneous median, as the paper states the effect (the top of the visually driven range against spontaneous); the \"\n           \"mean-based form is shown. The outcome does not depend on it, as the value part fails.\"]))\nO.append(oc(\"fig4b-other-thalamus-not-modulated\", \"not_reproduced\",\n    \"Under 'vbn' the medians of the seven nuclei are 0.092 to 0.107, inside 0.09 to 0.143, and the largest condition \"\n    \"difference per nucleus 0.002 to 0.006. Both test readings find modulation: Kruskal-Wallis p < 0.001 in MGd, SGN, MGm \"\n    \"and MGv (5.7e-08 to 7.3e-04); pairwise Mann-Whitney, a nucleus counted as modulated when any visually driven condition \"\n    \"differs from spontaneous at p < 0.001, in MGd, SGN and MGv (smallest p 1.6e-07, MGv images against spontaneous). The \"\n    \"lenient pairwise form (all three conditions significant) finds none, or SGN alone under b/a. All six pairwise p-values \"\n    \"per nucleus are printed.\" + VAR_SAME, [0.092, 0.107],\n    extra=[\"Assumed (step 1.6): for this claim of absence the pairwise reading counts a nucleus as modulated when any of its \"\n           \"three visually driven conditions differs from spontaneous at p < 0.001, the verifier having found the form that \"\n           \"needs all three too lenient; the lenient form is shown.\"]))\nO.append(oc(\"fig4c-dg-ca3-complexity\", \"reproduced\",\n    \"Legend reading under 'vbn', every condition reading: DG images 0.116, CA3 0.107, CA1 0.095 match the legend's 0.12, 0.11 \"\n    \"and 0.10; in the other conditions DG 0.179 to 0.251, CA3 0.130 to 0.188, CA1 0.118 to 0.158, inside the legend's widened \"\n    \"ranges; POST, ProS and SUB 0.096 to 0.135, inside 0.09 to 0.143; DG and CA3 peak in spontaneous activity. The text's \"\n    \"reading fails (CA3 inside its range in 2 of 4 conditions, CA1 0.095 below 0.099 in natural images). Measured values: \"\n    \"DG, CA3 (natural images apart) and CA1, POST, ProS, SUB (all conditions), reading a/a.\" + VAR_SAME,\n    [0.179, 0.249, 0.13, 0.188, 0.095, 0.155]))\nO.append(oc(\"fig4d-midbrain-complexity-invariant\", \"reproduced\",\n    \"Legend values under 'vbn': NB 0.104 to 0.111, MRN 0.094 to 0.101, SCig 0.095 to 0.097, APN 0.086 to 0.089, each inside \"\n    \"its widened range; NOT 0.101 to 0.159 across conditions, the largest range (0.055 to 0.057 against at most 0.007). Text \"\n    \"values fail on APN (below 0.09). 'all' is reproduced; 'qc' drops NOT, so the claim cannot be judged under it.\",\n    [0.086, 0.111, 0.159, 0.101]))\nO.append(oc(\"fig4e-js-complexity-natural-images\", \"not_reproduced\",\n    \"Natural images under 'vbn', bits: VIS-VIS pairs below 0.22, 0.80 to 1.00; VIS-TH above 0.36, 0.70 to 0.72 (median 0.454 \"\n    \"to 0.462); VIS-MB above 0.36, 0.73 to 0.77 (median 0.456 to 0.469). Pairs of DG or CA3 with other subregions in 0.27 to \"\n    \"0.55, 0.18 to 0.20 (median 0.199 to 0.217). In natural logs the VIS-TH and VIS-MB parts fail too (0.37 to 0.43).\" + VAR_SAME,\n    extra=[\"JS in bits, with natural logs as the claims file's variant.\"]))\nO.append(oc(\"fig4fg-js-complexity-active-blanks\", \"not_reproduced\",\n    \"Under 'vbn', bits: pairs of a visual and a subcortical subregion above 0.36, 0.38 in active behavior (median 0.259 to \"\n    \"0.265) and 0.31 to 0.34 in blanks (median 0.189 to 0.209); HP-HP pairs in active behavior within 0.18 to 0.44, 0.33 \"\n    \"(0.13 in natural logs).\" + VAR_SAME, extra=[\"JS in bits, with natural logs as the claims file's variant.\"]))\nO.append(oc(\"fig4h-js-complexity-spontaneous-converges\", \"not_reproduced\",\n    \"Under 'vbn', bits: mean of all pairs, spontaneous 0.282 to 0.353 against images 0.298 to 0.322, active 0.252 to 0.260, \"\n    \"blanks 0.226 to 0.258, so not lowest. Mean VIS-to-other divergence is lowest in spontaneous activity (0.215 to 0.265 \"\n    \"against 0.274 to 0.518), but 0.26 to 0.40 of those pairs lie in 0.18 to 0.44. MB-MB pairs below 0.22 in 0.2 to 0.3 of \"\n    \"them in spontaneous activity in bits; in natural logs with 50 bins they are below 0.22 in most pairs in every condition, \"\n    \"but the other two parts still fail.\" + VAR_SAME, extra=[\"JS in bits, with natural logs as the claims file's variant.\"]))\nO.append(oc(\"supp-robustness-parameters\", \"partially_reproduced\",\n    \"Under 'vbn' the pattern holds for 4 of 5 combinations (20 ms with D 5 tau 1 and D 6 tau 1; 50 ms with D 4 tau 2 and D 5 \"\n    \"tau 3). With 20 ms, D 3, tau 4, natural images exceed spontaneous in 2 of 6 visual areas and the visual difference is \"\n    \"-0.0002. Window counts are those of the 50 ms analysis (images 16 764, active 76 796, blanks 17 072, spontaneous 4268) \"\n    \"against the supplement's 20 ms counts 11 321, 51 452, 11 265 and 2856.\" + VAR_SAME,\n    extra=[\"The visually driven minus spontaneous difference of an area is the median C over its visually driven windows minus that over its spontaneous windows; the claims file does not fix the form.\"]))\nO.append(oc(\"fig5-vis-complexity-cv-coupling\", \"not_reproduced\",\n    \"Under 'vbn' C rises with CV in the three visually driven conditions (Spearman 0.640, 0.844, 0.836; monotonic under bins \"\n    \"of 0.05 with at least 10 windows). Spans, bins of 0.1 without minimum (measured): images CV 0.20 to 1.40 and C to 0.329; \"\n    \"active CV to 4.60, C to 0.381; blanks CV to 2.00, C to 0.391; spontaneous maximum 0.337. With at least 10 windows per \"\n    \"bin the spontaneous maximum is 0.153, below 0.165, but the natural-image and blank spans miss (images CV to 1.00, blanks \"\n    \"C to 0.327 to 0.348). No reading matches all spans.\" + VAR_SAME,\n    [0.329, 4.6, 0.381, 2.0, 0.391, 0.337]))\nO.append(oc(\"fig5-th-weaker-coupling\", \"not_reproduced\",\n    \"Under 'vbn' least-squares slopes of C on CV, TH 0.129, 0.104 and 0.094 (images, active, blanks) against VIS 0.372, 0.226 \"\n    \"and 0.246, positive and shallower as stated. The TH spans exceed CV 0.18 to 0.88 and C 0.09 to 0.22 under every reading \"\n    \"(CV from 0.10 or 0.15; active behavior up to CV 1.05 to 1.50 and C 0.193 to 0.306).\" + VAR_SAME))\nO.append(oc(\"fig5-hp-spontaneous-elevated\", \"not_reproduced\",\n    \"Under 'vbn' HP spontaneous bin means at CV 0.4 to 0.7 reach 0.227 to 0.239, within 0.25 +/- 0.025, but the HP maxima of \"\n    \"the visually driven conditions are higher in active behavior (0.198 to 0.441) and not all within 0.19 +/- 0.019 (images \"\n    \"0.135 to 0.336, blanks 0.169 to 0.380). Measured values for bins of 0.1 without minimum (the visually driven maximum is \"\n    \"the active one).\" + VAR_SAME, [0.227, 0.42]))\nO.append(oc(\"fig5-mb-flat\", \"not_reproduced\",\n    \"Under 'vbn' the MB slope is the smallest in absolute value of the four areas in all four conditions. Its bin means stay \"\n    \"inside the bounds in natural images (0.090 to 0.135) and spontaneous activity (0.092 to 0.136), but in active behavior \"\n    \"and blanks they start at 0.084, below 0.09, under every reading (high ends 0.126 to 0.245).\" + VAR_SAME))\nO.append(oc(\"supp-fig6-mean-correlation\", \"not_reproduced\",\n    \"Under 'vbn' VIS medians of the mean pairwise correlation, active and blanks 0.014 to 0.055 (50 ms) and 0.007 to 0.031 \"\n    \"(20 ms), below 0.072; images and spontaneous 0.009 to 0.038 (50 ms) and 0.005 to 0.023 (20 ms), 1 to 2 and 6 of 12 below \"\n    \"0.011. Midbrain medians vary across conditions by at most 0.009 except NOT (0.023 to 0.024 at 50 ms, 0.013 to 0.014 at \"\n    \"20 ms). Measured values: active and blanks low and high, images and spontaneous high (50 ms, a/a).\" + VAR_SAME,\n    [0.014, 0.055, 0.038],\n    extra=[\"Units without spikes in a window are left out (claims file). Correlations are computed for visual cortex and midbrain populations only.\"]))\nO.append(oc(\"complexity-separates-images-from-spontaneous\", \"reproduced\",\n    \"JS reading under 'vbn': in all six visual subregions the natural-image against spontaneous divergence is larger for C \"\n    \"(0.437 to 0.837, a/a, 50 bins) than for CV (0.249 to 0.537) and mean correlation (0.189 to 0.479), under every condition \"\n    \"and histogram reading. IQR reading: 1 or 2 of 6, since the CV and correlation IQRs of the two conditions often do not \"\n    \"overlap either. The CV medians do differ between the two conditions (VISp 0.399 against 0.299).\" + VAR_SAME))\n\nassert len(O) == 38 and [o[\"claim\"] for o in O] == [o[\"claim\"] for o in rec[\"outcomes\"]]\nrec[\"outcomes\"] = O\n\nrec[\"inputs\"].append({\"what\": \"The unit filter of the Allen Institute's Visual Behavior Neuropixels quickstart tutorial (snr > 1, \"\n                      \"isi_violations < 1, firing_rate > 0.1), used as the adopted unit selection; no data.\",\n                      \"source\": \"https://github.com/AllenInstitute/AllenSDK at commit a56bd8ea7613a812334602b64746cdd30c325a96, \"\n                      \"doc_template/examples_root/examples/nb/visual_behavior_neuropixels_quickstart.ipynb\"})\n\nF = rec[\"findings\"]\nF[0][\"statement\"] = (\"The paper analyses 102 sessions and 1437 populations without saying how the sessions were chosen. The \"\n    \"dandiset holds 153 ecephys sessions of 81 mice, every one with populations that pass the paper's rule (at least 30 \"\n    \"units, subregion in at least eight sessions) and with the gray-screen epoch, and no grouping by genotype (59, 49, 45), \"\n    \"image set and novelty (68, 10, 10, 65) or probe count (142 with six probes) gives 102, so the paper's selection cannot \"\n    \"be rebuilt; population and window counts here are about 1.5 times the paper's. Which 102 sessions were used?\")\nF[1][\"statement\"] = (\"No unit selection is stated. Scaled to 102 sessions, all units give 1.28 to 1.43 times Table I's area \"\n    \"neuron counts, and the Allen quality filters (ISI violations < 0.5, amplitude cutoff < 0.1, presence ratio > 0.9) 0.34 \"\n    \"to 0.55 times, dropping NOT. The filter of the Allen Institute's Visual Behavior Neuropixels tutorial (snr > 1, ISI \"\n    \"violations < 1, firing rate > 0.1 spikes/s) gives 0.93 to 1.02 times, with neurons per population within 5% of Table \"\n    \"I's, and is adopted here; ten outcomes differ under one of the other two. Which units form a population?\")\nF[6][\"statement\"] = (\"Methods II.A gives the blank series as about 240 s per image, which needs about 480 flashes per image. \"\n    \"The flash tables show each image 320 to 1056 times per session (median 572.5), so the series is about 286 s (median; 271 \"\n    \"s without change flashes, 275 s when only gray screens followed by another flash are kept). How were the blank intervals \"\n    \"chosen (change flashes, omitted flashes, licks)?\")\n\nR = [\n (\"table1-sample\", True, \"not_reproduced\", \"153 sessions under every reading (session reading b changes nothing, because all 153 sessions have the spontaneous epoch), against 102. With all units, the neuron counts are about 2 times Table I. With the quality filter (qc), the window counts match but the populations and neurons do not. Nothing in the asset list picks out the paper's 102 sessions.\",\n  \"Neuron counts are now compared per population and scaled to 102 sessions for six filters, as asked, including quality 'good' and presence ratio > 0.95. The Allen tutorial filter (snr > 1, ISI violations < 1, firing rate > 0.1) matches Table I (0.93 to 1.02 times, neurons per population within 5%) and is adopted; all units and qc are run as variants for every claim. Sessions are broken down by genotype, image set, novelty and probe count; none gives 102. Outcome unchanged.\"),\n (\"fig1c-cv-region-medians\", True, \"not_reproduced\", \"All units: the medians of DG (0.564) and NB (0.564) fall outside the widened ranges, and the TH, HP and MB extremes miss. qc: the TH maximum (0.414) misses.\",\n  \"Under the adopted 'vbn' filter every median and extreme matches and only the IQRs miss in 5 subregions, which the criterion makes partially reproduced. Outcome changed to partially_reproduced; all units and qc stay not reproduced.\"),\n (\"fig1c-cv-above-surrogate\", True, \"partially_reproduced\", \"Every Mann-Whitney test gives p at most 1.5e-73 with empirical higher, and the VIS surrogate medians are 0.225 to 0.243. The HP ratios for POST (1.32) and DG (3.01) fall outside 1.35 to 2.42 under all five seeds. This is the claim's partial rule.\",\n  \"Under 'vbn' VISam (1.75), VISrl (1.78) and POST (1.29) fall outside; a per-population Wilcoxon test is added for the pseudo-replication point. Outcome unchanged.\"),\n (\"fig1d-surrogate-abolishes-cv-correlations\", True, \"not_reproduced\", \"Surrogate |r| reaches 0.79 under reading (a) and 0.66 under (b). 115 and 213 pairs exceed 0.2.\",\n  \"Under 'vbn' 147 and 240 pairs exceed 0.2 (largest 0.890 and 0.708). The confound of reading (a) the verifier describes is noted. Outcome unchanged.\"),\n (\"fig1e-positive-cv-modules\", False, \"not_reproduced\", \"Reading (a): top value 0.772, above 0.737. Reading (b): low end 0.450, just outside 0.50 +/- 0.05. Same-area fractions (66% and 81%) do hold.\",\n  \"The claim has no partial rule, so a miss is not reproduced, as the verifier says. Under the adopted 'vbn' filter reading (b) gives 0.478 to 0.680 with 28 of 32 pairs within an area, and reading (b) is adopted because reading (a) mixes session-level differences (the verifier's point B8); the outcome is reproduced, resting on both assumptions. All units and qc are not reproduced.\"),\n (\"fig1e-dg-ca3-anticorrelation-hubs\", False, \"not_reproduced\", \"Reading (b): CA3 and DG are the hubs, but the most negative r is -0.178 (expected -0.27 +/- 0.027). Reading (a): NB is the hub and the most negative r is -0.496.\",\n  \"No partial rule, so a miss is not reproduced. Under 'vbn', reading (b) gives DG 16 and CA3 14 of 32 pairs and a most negative r of -0.247, within tolerance; reproduced, resting on the unit and session-combination readings. All units and qc are not reproduced.\"),\n (\"fig1e-midbrain-weakest-cv-correlations\", False, \"not_reproduced\", \"Reading (a): MB mean |r| (0.186) is above HP (0.179). Reading (b): only 2 of 115 MB pairs are near zero.\",\n  \"Changed to not_reproduced, as the claim has no partial rule. Under 'vbn' MB is lowest under both readings but only 13 and 3 of 115 pairs are near zero.\"),\n (\"fig2a-vis-cv-by-condition\", True, \"reproduced\", \"12/12 medians within tolerance under readings a/a and b/a with all units. The values sit near the upper edge of tolerance, and with qc only 8/12 are within.\",\n  \"Under 'vbn' 12 of 12 are within tolerance under all four condition readings; qc gives 7 or 8 of 12 and is shown. Outcome unchanged.\"),\n (\"fig2a-thalamus-cv-by-condition\", True, \"reproduced\", \"4/4 values within tolerance under every reading, and the LP and LGd effects are smaller than in VISp, VISl and VISal.\",\n  \"Holds under 'vbn' and all units; under qc LP active misses, shown. Outcome unchanged.\"),\n (\"fig2a-hippocampus-cv-stable\", False, \"not_reproduced\", \"DG medians are 0.555 to 0.580, against 0.48 to 0.51 +/- 10%. This was not run with qc, where DG active is 0.481.\",\n  \"Run under every unit reading. Under 'vbn' (and qc) all seven values are within tolerance and the spontaneous medians are highest; outcome changed to reproduced, resting on the unit reading. All units are not reproduced, as the verifier found.\"),\n (\"fig2a-midbrain-cv-invariant\", False, \"not_reproduced\", \"MRN maximum is 0.233, against the limit of 0.231.\",\n  \"Changed to not_reproduced (no partial rule). Under 'vbn' APN spontaneous (0.142) and MRN low (0.171) miss.\"),\n (\"fig2b-vis-summed-js-cv\", True, \"partially_reproduced\", \"No combination is fully reproduced. Four of 32 meet the partial rule: active and blanks are the closest pair and every other pair differs by more than 15%. Active against blanks is 0.32 to 0.53%, below the 0.5% lower bound.\",\n  \"Under 'vbn' four other combinations (100 bins) meet the partial rule; no combination is fully reproduced. Outcome unchanged.\"),\n (\"fig2b-hp-mb-summed-js-cv\", True, \"not_reproduced\", \"HP active against spontaneous is 41 to 71%, and the MB maximum is 22 to 41%.\", \"Same under 'vbn' (44.8% to 77.6%, 27.2% to 48.5%). Outcome unchanged.\"),\n (\"fig2b-visually-driven-js-cv-low\", False, \"partially_reproduced\", \"The percentage form, which is the claim's statement, holds in 0/32 combinations. The legend's JS-value form holds in all 8.\",\n  \"Changed to partially_reproduced, as the verifier gives: the statement's form fails and only the legend's holds.\"),\n (\"fig2b-dg-ca3-high-js-cv\", False, \"not_reproduced\", \"CA3 spontaneous median is at most 0.638 and CA3 blanks at most 0.419, against 0.84 and 0.63.\",\n  \"Changed to not_reproduced (no partial rule). Natural-log JS added as asked; it gives lower values.\"),\n (\"fig2b-legend-js-cv\", True, \"not_reproduced\", \"TH > 0.33 in at most 1/9 subregions and VIS > 0.44 in at most 3/6, under both readings.\", \"Same under 'vbn' (at most 2 of 9, 3 of 6), with natural logs added. Outcome unchanged.\"),\n (\"fig3a-reference-systems\", True, \"partially_reproduced\", \"White noise, logistic (r = 4) and tent (mu about 2) fit, and so does the correlated walk at alpha 0.2 to 0.3. The walk at alpha 0.5 to 0.7 has C 0.23 to 0.26, below range. The other two failures come from the notebook's own choices: the Ikeda map judged at p = 6 without a source, while p repeats every 2 pi and the textbook value 0.4 sits at about 6.683 or 12.966; and the sine rule H at most 0.05, which cannot be met, as any sine gives H at least ln 2 / ln 720 = 0.105.\",\n  \"The Ikeda map is now judged at 0.4 + 2 pi and 0.4 + 4 pi (H 0.81, C 0.355, just below 0.36; p = 6.5 is inside), and the sine reading is H at most the floor plus 0.05, at 100, 1000 and 10 000 points per period (it matches at 10 000). The reading of H near 0 is asked of a reader. Outcome unchanged.\"),\n (\"fig3b-complexity-levels-by-region\", True, \"reproduced\", \"Reading (a): VIS 0.161, HP 0.163, TH 0.109, MB 0.101, and the order holds at 36/36 window indices. It also holds with qc.\", \"Same under 'vbn' (0.158, 0.159, 0.108, 0.098). Outcome unchanged.\"),\n (\"fig3c-vis-ch-plane\", False, \"not_reproduced\", \"The C 2.5th percentile is 0.089, below the 0.090 bound, and the 0-100 span has H down to 0.462. The test (p about 0) and the surrogate median (0.0955) pass. It is a narrow miss.\",\n  \"Changed to not_reproduced (no partial rule). Spans are now compared unrounded; under 'vbn' the C 2.5th percentile is 0.0887. Under qc the claim passes, shown.\"),\n (\"fig3d-th-ch-plane\", True, \"reproduced\", \"The 95% span is inside the range, narrower than VIS, and p < 0.001.\", \"Same under every unit reading. Outcome unchanged.\"),\n (\"fig3e-hp-ch-plane\", True, \"reproduced\", \"The 95% span is inside, it is the widest of the four areas, and p < 0.001.\", \"Same under every unit reading. Outcome unchanged.\"),\n (\"fig3f-mb-ch-plane\", True, \"reproduced\", \"The 95% span is inside, it is the narrowest, and p = 2e-194. The 0-100 variant fails.\", \"Same under every unit reading. Outcome unchanged.\"),\n (\"fig3-complexity-range-fractions\", True, \"not_reproduced\", \"0/8 within tolerance on active windows, 1/8 on image windows.\", \"0 of 8 on both under 'vbn'. Outcome unchanged.\"),\n (\"fig4a-vis-complexity-by-condition\", False, \"not_reproduced\", \"In VISp, natural images (0.178) are not above active (0.190), and images against blanks gives p = 0.53. So the order fails, and the partial rule needs the order.\",\n  \"Changed to not_reproduced, as the verifier reads the partial rule.\"),\n (\"fig4b-thalamus-lgd-lp-modulated\", True, \"reproduced\", \"Kruskal-Wallis p at most 3e-63, the visually driven medians are above spontaneous, and the values match the legend's. The effect is smaller than in every VIS area only under effect form (i); form (ii) fails for LGd against VISrl. The effect definition is the notebook's own; both forms were run and the outcome rests on (i).\",\n  \"Under the adopted 'vbn' filter LP's spontaneous median (0.098) falls just below the legend's range, so the outcome changes to not_reproduced; under all units and qc it is reproduced, so the outcome turns on the unit reading. The effect forms are kept, both shown.\"),\n (\"fig4b-other-thalamus-not-modulated\", False, \"partially_reproduced\", \"Medians are 0.093 to 0.108, inside the range. Kruskal-Wallis finds p < 0.001 in MGd, SGN, MGm and MGv. The pairwise reading passes only as implemented: a nucleus counts as modulated only if all three visually driven conditions differ from spontaneous, which for a claim of absence is too lenient, and the smallest pairwise p is not printed.\",\n  \"All six pairwise p-values per nucleus are now printed. The pairwise reading counts a nucleus as modulated when any visually driven condition differs from spontaneous; it then finds MGd, SGN and MGv (smallest p 1.6e-07), and Kruskal-Wallis finds four, so both readings find modulation and the criterion gives not reproduced. Outcome changed to not_reproduced, against the verifier's partially_reproduced, as the criterion says not reproduced when the test finds modulation in any nucleus.\"),\n (\"fig4c-dg-ca3-complexity\", True, \"reproduced\", \"Holds on the legend reading with spontaneous reading b (a/b, b/b), with the peak in spontaneous activity. The text reading fails because CA1 reaches 0.162. Under a/a, CA3 spontaneous (0.198) sits right at its bound.\",\n  \"Under 'vbn' the legend reading holds under all four condition readings (CA3 spontaneous 0.187 to 0.188). Outcome unchanged.\"),\n (\"fig4d-midbrain-complexity-invariant\", True, \"reproduced\", \"Legend values hold and NOT has the largest range across conditions. The text values fail (APN 0.086).\", \"Same under 'vbn'; qc drops NOT. Outcome unchanged.\"),\n (\"fig4e-js-complexity-natural-images\", False, \"not_reproduced\", \"VIS-VIS, VIS-TH and VIS-MB hold. Only 20% of DG/CA3 pairs lie in 0.27 to 0.55 (median 0.16).\",\n  \"Changed to not_reproduced (no partial rule).\"),\n (\"fig4fg-js-complexity-active-blanks\", True, \"not_reproduced\", \"VIS against subcortical pairs above 0.36: 29 to 38%. HP-HP pairs in range: 27 to 33%.\", \"Same under 'vbn', with natural logs added. Outcome unchanged.\"),\n (\"fig4h-js-complexity-spontaneous-converges\", True, \"not_reproduced\", \"The mean of all spontaneous pairs is not the lowest (0.264 to 0.332 against 0.218 to 0.255 for blanks).\", \"Same under 'vbn', with natural logs added. Outcome unchanged.\"),\n (\"supp-robustness-parameters\", True, \"partially_reproduced\", \"The pattern holds in 4 of 5 combinations; bin 20 ms with D 3, tau 4 fails. This is the claim's partial rule.\", \"Same under 'vbn'. Outcome unchanged.\"),\n (\"fig5-vis-complexity-cv-coupling\", False, \"not_reproduced\", \"The CV spans exceed the quoted ones, and the spontaneous maximum is at least 0.180, against < 0.165.\",\n  \"Changed to not_reproduced (no partial rule). Under 'vbn' the spontaneous maximum is 0.153 with at least 10 windows per bin, but the spans still miss.\"),\n (\"fig5-th-weaker-coupling\", False, \"not_reproduced\", \"The slopes are positive and below VIS, but the spans exceed CV 0.88 or C 0.22 under every reading.\", \"Changed to not_reproduced (no partial rule).\"),\n (\"fig5-hp-spontaneous-elevated\", True, \"not_reproduced\", \"The spontaneous peak is 0.238 to 0.244, but the visually driven maxima are 0.17 to 0.41, not about 0.19, and spontaneous does not exceed them.\", \"Same under 'vbn'. Outcome unchanged.\"),\n (\"fig5-mb-flat\", False, \"not_reproduced\", \"MB bin means reach 0.17 to 0.35 in active and blanks; only the slope part holds.\", \"Changed to not_reproduced (no partial rule).\"),\n (\"supp-fig6-mean-correlation\", True, \"not_reproduced\", \"VIS active and blank medians are 0.007 to 0.052, against 0.08 to 0.13.\", \"Same under 'vbn' (0.007 to 0.055). Outcome unchanged.\"),\n (\"complexity-separates-images-from-spontaneous\", True, \"reproduced\", \"JS reading: complexity has the larger JS in 6/6 VIS subregions under every reading. The IQR reading holds in only 1 to 2 of 6.\", \"Same under 'vbn'. Outcome unchanged.\"),\n]\nassert [r[0] for r in R] == [o[\"claim\"] for o in O]\nfor (c, ag, vo, reason, resp), o in zip(R, O):\n    assert ag == (vo == old[c][\"outcome\"]), c\nrec[\"verifications\"] = [{\n    \"date\": \"2026-11-27\", \"kind\": \"agent\",\n    \"by\": \"Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)\",\n    \"reviewed\": (\"The first executed notebook with the conclusion cells and the summary removed, the helper module and the claims \"\n                 \"file, with the paper's full text. The verifier queried the archive's asset list itself (4293 assets, 153 ecephys \"\n                 \"session files, 81 subjects) and tested the helpers on synthetic inputs (bandt_pompe, js_divergence, shuffle_isi, \"\n                 \"concat_windows, mean_corr and the Q0 constant). It had no attempt record.\"),\n    \"results\": [{\"claim\": c, \"agrees\": ag, \"outcome\": vo, \"reason\": reason, \"response\": resp} for c, ag, vo, reason, resp in R]}]\n\nclass D(yaml.SafeDumper):\n    pass\ndef str_rep(d, s):\n    return d.represent_scalar(\"tag:yaml.org,2002:str\", s)\nD.add_representer(str, str_rep)\ntxt = yaml.dump(rec, Dumper=D, sort_keys=False, allow_unicode=True, width=118)\nopen(P, \"w\").write(txt)\nprint(\"written\", len(txt))\n"
}
```

```
File created successfully at: /tmp/claude-1001/record.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cp attempts/paula-2026-01.yaml $TMPDIR/attempt_orig.yaml; $TMPDIR/devenv/bin/python -c "import yaml" 2>/dev/null && PY=$TMPDIR/devenv/bin/python || PY=python; $PY $TMPDIR/record.py && python tools/entry.py check entries/paula-2026 2>&1 | tail -5; grep -n "—\|rather" attempts/paula-2026-01.yaml questions/paula-2026.yaml | head
```

```
written 85587
0 error(s)
```

**Agent calls Bash**

```bash
sed -n 1,60p attempts/paula-2026-01.yaml; grep -c "\\\\" attempts/paula-2026-01.yaml
```

```
schema_version: 3
id: paula-2026-01
datasets:
- archive: dandi
  id: '000713'
  version: 0.240702.1725
  doi: 10.48324/dandi.000713/0.240702.1725
  relation: reuses
paper: doi:10.1103/wndc-k654
date: '2026-11-27'
entry: paula-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-18
  runner:
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> $TMPDIR/record.py <<'EOF'

rec = yaml.safe_load(open(P))
F = rec["findings"]
assert F[2]["statement"].startswith("The ISI-shuffled surrogate") and F[5]["statement"].startswith("The Fig. 5 trajectories")
F[2]["statement"] = ("The ISI-shuffled surrogate is defined per analyzed window (Methods II.E). Shuffled within each 100-s window, "
    "surrogate CV series stay correlated across regions (up to |r| 0.90, 143 to 241 of 325 pairs above 0.2), because each "
    "window keeps its spike count; the paper says shuffling abolishes these correlations. Were the 10-s CV series of Fig. 1d "
    "computed from surrogates shuffled over a longer span, and where does the shuffled train start?")
F[5]["statement"] = ("The Fig. 5 trajectories give no CV bin width or minimum count per bin, and the Fig. 3a reference systems "
    "give no series length, sampling or parameter values in the text (the sine's position depends on its sampling; the Ikeda "
    "map with u = 0.9 lies at C 0.355 at its usual chaotic parameter shifted into [5, 17], and inside the quoted range only "
    "near p = 6.5). What were they?")
if not any(f["statement"].startswith("Fig. 1d and 1e do not say") for f in F):
    F.append({"kind": "methods_unavailable", "statement": ("Fig. 1d and 1e do not say how the CV correlations of a region pair "
        "are combined over the sessions that record both. Concatenating the series gives a top-10% range of 0.469 to 0.798 and "
        "NB as the leading anticorrelation hub; averaging the per-session correlations gives 0.478 to 0.680 with DG and CA3 as "
        "the hubs, which matches the paper and is adopted here. Which was used?")})
yaml.dump(rec, open(P, "w"), Dumper=D, sort_keys=False, allow_unicode=True, width=118)
print("findings", len(F))
EOF
python - <<'EOF'
# rerun only the appended part: restore original first, since the script rewrites outcomes from the original anyway
EOF
cp $TMPDIR/attempt_orig.yaml attempts/paula-2026-01.yaml && $PY $TMPDIR/record.py 2>&1 | tail -2 || true
```

```
/bin/bash: line 25: /tmp/claude-1001/record.py: Permission denied
```

**Agent calls Bash**

```bash
cp $TMPDIR/attempt_orig.yaml attempts/paula-2026-01.yaml && python $TMPDIR/record.py && python tools/entry.py check entries/paula-2026 2>&1 | tail -3; date -u
```

```
written 85587
findings 10
0 error(s)
Fri Nov 27 16:44:33 UTC 2026
```

**Agent calls Bash**

```bash
timeout 120 python tools/entry.py run entries/paula-2026 2>&1 | tail -3; git status --short | head -20
```

```
pass  reproduce_paula_2026.ipynb  (2810 s, reused)
reused the executed copies of 2026-11-27 16:40 UTC: nothing the run reads has changed since (hash 9a1c9a0fb267). Nothing was executed and no environment was built; --fresh runs it again.
 M attempts/paula-2026-01.yaml
 M entries/paula-2026/README.md
 M entries/paula-2026/entry.yaml
 M entries/paula-2026/paula.py
 M entries/paula-2026/reproduce_paula_2026.ipynb
 M tools/agent_run.py
 M tools/author_notes.py
 M tools/blind.sh
 M tools/build_site.py
 M tools/colab.py
 M tools/conversion_issue.py
 M tools/entry.py
 M tools/get_papers.sh
 M tools/notify.py
 M tools/paper_match.py
 M tools/papers_manifest.py
 M tools/runner/chain.sh
 M tools/runner/cutover_paper_first.py
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open("cells_a.py").read()
a='print("units per session: median", metas.n_units.median(), "range", metas.n_units.min(), "to", metas.n_units.max())\n'
assert a in s
s=s.replace(a, a+'''n_all = sum(sum(d.values()) for d in metas.region_counts_all); n_good = sum(sum(d.values()) for d in metas.region_counts_good)
print(f"units with quality label 'good': {n_good} of {n_all} ({100 * n_good / n_all:.1f}%); the rest are labelled 'noise'")
''')
open("cells_a.py","w").write(s)
m=open("cells_md.py").read()
reps=[("only because its fewer populations per session (754 VIS against 586 x 153/102 = 879) offset the excess of sessions.",
       "only because its fewer populations per session (754 VIS populations, 503 when scaled to 102 sessions, against 586) offset the excess of sessions."),
      (" Reading a also mixes session-level differences into one correlation. Every unit reading", " Every unit reading"),
      ("About 17% of units carry the quality label 'noise' in the first session; the units table holds", "Part of the units carry the quality label 'noise' (the share is printed in the data check); the units table holds")]
for a,b in reps:
    assert a in m, a[:30]; m=m.replace(a,b)
open("cells_md.py","w").write(m)
EOF
cd  && python $TMPDIR/assemble.py && python tools/entry.py check entries/paula-2026 | tail -1
```

```
ok 138
0 error(s)
```

**Agent calls Bash**

```bash
$TMPDIR/devenv/bin/python $TMPDIR/devrun.py 2>&1 | grep -v WARNING | tail -3; python $TMPDIR/show.py $TMPDIR/dev_out.ipynb 4 | grep "quality label"
```

```
took 33.14812970161438
units with quality label 'good': 42552 of 51759 (82.2%); the rest are labelled 'noise'
```

**Agent**

Subset run passes. Starting the final full run (about 47 minutes).

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/paula-2026 2>&1 | tail -3; date -u
```

```
Fri Nov 27 16:45:50 UTC 2026
Installed kernelspec registry-paula-2026 in executed/paula-2026/.venv/share/jupyter/kernels/registry-paula-2026
0 error(s)
pass  reproduce_paula_2026.ipynb  (2785 s)
Fri Nov 27 17:32:26 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF' > $TMPDIR/run3_out.txt
import json
nb = json.load(open("executed/paula-2026/reproduce_paula_2026.ipynb"))
for i, c in enumerate(nb["cells"]):
    if c["cell_type"] != "code": continue
    print("=== cell", i)
    for o in c.get("outputs", []):
        if o.get("output_type") == "error": print("ERROR", o.get("ename"))
        t = o.get("text") or o.get("data", {}).get("text/plain", "")
        if "Figure" in "".join(t): continue
        print("".join(t))
EOF
grep -c ERROR $TMPDIR/run3_out.txt; grep "quality label" $TMPDIR/run3_out.txt; diff <(sed -n '/=== cell 13/,$p' $TMPDIR/run2_out.txt | grep -v "^$" | sed 's/ \[.*\]$//') <(sed -n '/=== cell 13/,$p' $TMPDIR/run3_out.txt | grep -v "^$") | head; python tools/entry.py check entries/paula-2026 | tail -1
```

```
0
units with quality label 'good': 262177 of 319013 (82.2%); the rest are labelled 'noise'
153c153
< === cell 31 None
---
> === cell 31
294c294
< === cell 45 None
---
> === cell 45
954c954
< Ikeda sweep: inside the chaotic range at
0 error(s)
```

**Agent calls Bash**

```bash
diff <(sed -n '/=== cell 13/,$p' $TMPDIR/run2_out.txt | grep -v "^$" | sed 's/ \[.*\]$//; s/ None$//') <(sed -n '/=== cell 13/,$p' $TMPDIR/run3_out.txt | grep -v "^$") | head
```

```
954c954
< Ikeda sweep: inside the chaotic range at
---
> Ikeda sweep: inside the chaotic range at ['p=6.500']
1677c1677
< not testable: subregions not kept under this reading:
---
> not testable: subregions not kept under this reading: ['NOT']
2219c2219
< claims whose criterion gives a different result under the variant readings than under 'vbn':
```

**Agent**

I've finished the round-1 revision. The entry ran cleanly from a fresh environment in 46 minutes, `entry.py check` reports no errors, and every conclusion and note matches the final run. Nothing is committed.

**Main change: which units are used.** The report was right that choosing all units went against the claims file's own test (Table I's neuron counts). The paper's 102 sessions can't be found among the dataset's 153, so I compared counts per population and scaled to 102 sessions, for six filters. The filter from the Allen Institute's Visual Behavior Neuropixels tutorial (snr > 1, ISI violations < 1, firing rate > 0.1) matches Table I almost exactly: 0.93 to 1.02 times the paper's neuron counts per area, and neurons per population within 5%. All units come out 1.28 to 1.43 times too high and the claims file's quality filter 0.34 to 0.55 times too low. I adopted the tutorial filter as an assumption, citing the AllenSDK file at a pinned commit. Every claim now also runs under the claims file's two filters. Ten claims would come out differently under one of them, and a table at the end of the notebook shows this.

**Outcomes now:** 12 reproduced, 6 partially reproduced, 20 not reproduced (before: 13, 15, 10).
- **To reproduced:**
  - `fig2a-hippocampus-cv-stable`: under the new filter all seven values are within tolerance.
  - `fig1e-positive-cv-modules` and `fig1e-dg-ca3-anticorrelation-hubs`: these hold when the per-session correlations are averaged. I adopted that combination because joining sessions' series mixes in differences between sessions, as the verifier noted.
- **To partially reproduced:**
  - `fig1c-cv-region-medians`: all medians match and only the spreads (IQRs) miss.
  - `fig2b-visually-driven-js-cv-low`: the verifier's outcome.
- **To not reproduced:**
  - `fig4b-thalamus-lgd-lp-modulated`: LP's spontaneous median of 0.098 sits just below the legend's 0.099. Under the other two filters this claim is reproduced, so it depends on the unit filter.
  - `fig4b-other-thalamus-not-modulated`: I now count a nucleus as modulated if any one condition differs from spontaneous, since "all three" was too lenient for a claim of absence. Both tests then find modulation in three or four nuclei. The verifier gave partially reproduced; I recorded that disagreement.
  - Ten more, because their claims have no partial rule, as the verifier read them: `fig1e-midbrain-weakest-cv-correlations`, `fig2a-midbrain-cv-invariant`, `fig2b-dg-ca3-high-js-cv`, `fig3c-vis-ch-plane`, `fig4a-vis-complexity-by-condition`, `fig4e-js-complexity-natural-images` and the three Fig. 5 coupling claims (visual cortex, thalamus, midbrain).

**Other report points:**
- **Fig. 3a reference systems:** the Ikeda map is now judged at its usual chaotic value shifted into the paper's range. It lands just below the range (C 0.355 against 0.36). "H near 0" for the sine is now read against the lowest value a sine can reach (0.105), at three samplings. The claim stays partially reproduced.
- **Added outputs the verifier asked for:**
  - all six pairwise p-values per thalamic nucleus;
  - a session breakdown (no grouping by genotype, image set, novelty or probe count gives 102);
  - flashes per image and blank-piece durations (median 286 s against the paper's 240 s);
  - JS divergence in natural logs;
  - one-value-per-population tests alongside the window-level ones;
  - C-H spans compared before rounding.
- **No changes needed:** points 5, 7, 8 and 10 didn't affect any outcome. The effect forms and readings are kept and shown.

**Record and questions:**
- Round 1 is recorded under `verifications`, claim by claim, with the verifier's reasons and my responses.
- I updated four findings with the new numbers and added one at the end asking how the paper combines sessions for Fig. 1d and 1e. The others keep their order.
- I created `questions/paula-2026.yaml` with two questions for a reader. One asks about the claims file's presence-ratio cutoff (0.9 against the 0.95 the verifier cites) and whether the tutorial filter should be a reading of its own. The other asks how "H near 0" should be read for the sine.

**Not done:** I didn't read the figures (the PDF still couldn't be rendered) and didn't add a third way of combining sessions for Fig. 1d.

## End of run

91 turns, 183 minutes, $10.01 at API prices, result: success.
