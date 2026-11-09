# crcns-apl-1 · author-revise-2 · run 42510155596

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/crcns-apl-1/verifier-2-report.md; ls entries/crcns-apl-1-bruno-2017 entries/crcns-apl-1-bruno-2017/*
```

```
Sun Nov  8 18:33:21 UTC 2026
# Verifier report, round 2: Bruno, Frost & Humphries 2017 (eLife 27342) on CRCNS apl-1

The claims file has 30 claims, and the attempt record has 30 outcomes: 22 reproduced, 5 partially reproduced, 2 not reproduced and 1 blocked. Three outcomes are marked `assumed: true`: fig3h, fig4c and fig7gh. I found no place where the claims file misreads the paper.

## 1. Outcomes

I agree with 29 of the 30 outcomes. I disagree with one.

**Disagreement: fig6d-decode-p10.** The record says partially reproduced; I say not reproduced.
- The criterion requires mean forecast R − 2 s.e.m. > 0 "in each of the nine responses", and it has no partial rule. The paper's statement is specifically "in all nine".
- Cell 79 shows preparation 4, bout 1 failing under all four readings, with histories up to 100 ms, and with the code's windowing (mean R −0.060 to −0.127).
- The failure therefore does not depend on the reading. Eight of nine is a failure of exactly what the claim says, not a partial match.

**Outcomes where my round-1 view has changed**
- **fig4c (reproduced, assumed): I now agree.** The criterion judges only the mean, 10 ± 1 s, and says consistency is "reported", not judged. Under the adopted reading the mean is 10.45 s (cell 61). In round 1 I judged consistency, which the criterion does not ask for.
- **fig3h (partially reproduced, assumed): I accept it.** The criterion holds under own/le80 (18 kept and 16 returned; 19 and 17) and fails under the adopted reading (16 and 15), and the record says so. Two caveats:
  - The criterion's text gives no partial outcome. Strictly, under the adopted reading it gives not reproduced.
  - An unreported fact bears on this; see point 2 below.
- **fig7gh (partially reproduced, assumed): I agree, as I did in round 1.** The result is split by reading: one slope of two is significant under own/min80 and under own/le80 with recurrent points, and none under either pooled reading (cell 100). The same strictness caveat as 
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -80; ls transcripts/crcns-apl-1 questions; find . -path ./paper -prune -o -name "*crcns-apl-1*" -print | grep -v transcripts | head
```

```
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
56:### 2. Read the paper's code
66:### 3. Write the claims file
151:### 4. Data from outside the paper's own recordings
159:### 5. Check
172:### 6. Answer questions
185:## Author
201:### 1. Establish what can be tested
328:### 2. Check the data against its description
343:### 3. Write the entry
411:### 4. Lock, check and run
422:### 5. Record the attempt
473:### 6. Hand over for verification
511:## Repeat attempts
553:## Local and remote datasets
576:## Verifier
580:### Round 1: without the author's conclusions
605:### Round 2: with the author's conclusions
[... 162 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 185,200p docs/protocol.md; sed -n 343,520p docs/protocol.md; sed -n 600,640p docs/protocol.md
```

**Agent calls Bash**

```bash
cat attempts/crcns-apl-1-bruno-2017-01.yaml; cat entries/crcns-apl-1-bruno-2017/entry.yaml; cat entries/crcns-apl-1-bruno-2017/README.md
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

### 3. Write the entry

An entry is a directory `entries/<folder>-<first author>-<year>/` holding
`entry.yaml`, `requirements.in`, one or more notebooks, and usually a helper
[... 200 more lines not kept]
```

```
Exit code 1
bwrap: Can't find source path .git/config.worktree.lock: No such file or directory
```

**Agent calls Bash**

```bash
wc -l attempts/crcns-apl-1-bruno-2017-01.yaml entries/crcns-apl-1-bruno-2017/*
```

```
716 attempts/crcns-apl-1-bruno-2017-01.yaml
    55 entries/crcns-apl-1-bruno-2017/README.md
  1005 entries/crcns-apl-1-bruno-2017/apl.py
    22 entries/crcns-apl-1-bruno-2017/entry.yaml
  2387 entries/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb
     8 entries/crcns-apl-1-bruno-2017/requirements.in
    97 entries/crcns-apl-1-bruno-2017/requirements.lock.txt
  4290 total
```

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-apl-1-bruno-2017-01.yaml"
}
```

```
1	schema_version: 2
2	id: crcns-apl-1-bruno-2017-01
3	dataset:
4	  archive: crcns
5	  id: apl-1
6	  version: unversioned
7	  doi: 10.6080/K0SN074B
8	paper: doi:10.7554/elife.27342
9	date: 2026-11-08
10	entry: crcns-apl-1-bruno-2017
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-13
19	  runner:
20	    platform: GitHub Actions
[... 697 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/crcns-apl-1; cat questions/crcns-apl-1.yaml 2>/dev/null | head -50; grep -n "fig3h\|fig6d\|fig7gh\|fig4c" -A40 claims/crcns-apl-1/*.yaml | grep -v "^\s*$" | head -250
```

```
10.7554-elife.27342.yaml
306:- id: fig3h-perturbations-return
307-  statement: Of 19 spontaneous divergences from the trajectory, 17 (90%) returned to a recurrent
308-    state; the two that did not were consistent with the end of the evoked locomotion.
309-  source: Results, Joint population activity meets the conditions for a periodic attractor,
310-    paragraph 7; Materials and methods, Testing return to the same manifold after perturbation;
311-    Figure 3H
312-  quote: For the remaining 19 divergent periods, we then determined if the population activity
313-    returned to a recurrent state after the divergent point; that is, whether the density of
314-    recurrence returned above 90% or not. The majority (17/19) did
315-  expected:
316-  - quantity: divergent periods
317-    value: 19
318-    tolerance: 1.9
319-  - quantity: divergent periods that returned to above 90% recurrence
320-    value: 17
321-    tolerance: 1.7
322-  criterion: As the Methods and recurrence_point_results_Viz.m with
323-    Are_jumps_perturbations_or_transitions2.m. After coalescence, a divergent period is a run of
324-    5 s windows with recurrence density below 90% that falls below 50% at least once; its
[... 222 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper; grep -rn -i "two oscillation cycles\|two cycles\|end of the recording" paper/* | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls executed/ 2>/dev/null | head; ls executed/crcns-apl-1-bruno-2017 2>/dev/null; cat tools/entry.py | head -60
```

```
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:

- every notebook in the directory is listed in entry.yaml, and exists;
- notebooks are committed without outputs;
- the lock file is present and newer requirements are not left unlocked;
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-apl-1-bruno-2017 && python -c "
import nbformat
nb=nbformat.read('reproduce_bruno_2017.ipynb',4)
for i,c in enumerate(nb.cells):
    s=c.source.replace('\n',' ')
    print(i,c.cell_type,c.metadata.get('tags',''),s[:150])
"
```

```
0 markdown  # Reproducing Bruno, Frost & Humphries (2017) from CRCNS data set apl-1  **Paper.** Bruno AM, Frost WN, Humphries MD (2017). A spiral attractor networ
1 code  import os os.environ.setdefault("OMP_NUM_THREADS", "1") os.environ.setdefault("OPENBLAS_NUM_THREADS", "1") import time import resource import warnings
2 markdown  ## Data check  Each check of the description against the values is stated under its output.
3 code ['sanity'] print("MD5 of each file read, against the data set's checksums.md5:") for name, h in D["md5"].items():     print(f"  {name:24s} {h}  {'matches' if D['
4 markdown  The data set holds 30 recordings, three bouts in each of 10 preparations, in the order of FileTable.mat, which the description says is the paper's num
5 code ['sanity'] # Units, ranges, the clock of the stimulus, and recordings deposited twice. rows = [] for r in recs:     t = r["t"]     pre = np.sum((t >= 25) & (t < 
6 code ['sanity'] # Is the P10 nerve on the clock of the population? Cross-correlation of 1 s binned rates after the # stimulus, against the same with the P10 series sh
7 code ['sanity'] # Coordinates: units and ranges, against the 501 x 501 diode template (plot_maps.m plots x*10, y*10) for c, p in zip(D["coords"], preps):     print(f"
8 markdown  **Checks of the description against the data.** Consistent with the description: 30 recordings, three per preparation; 75 to 160 neurons per preparati
9 markdown  ## dataset-size  > Three bouts of fictive locomotion were evoked in each of 10 isolated preparations (30 population > responses); each recorded popula
10 code ['claim:dataset-size'] n_preps = info.prep.nunique() n_recs = len(info) per_prep = info.groupby("prep").neurons.first() print("preparations", n_preps, "| recordings", n_recs
11 markdown  **Result: partially reproduced.** The counts match: 10 preparations, 30 recordings and 1131 neurons. The range does not: recordings hold 75 to 160 neu
12 markdown  ## fig1d-slow-oscillation  > After stimulation the
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('reproduce_bruno_2017.ipynb',4)
for i in [0,21,22,53,62,81,84,101,108]:
    print('=====',i); print(nb.cells[i].source)
"
```

```
===== 0
# Reproducing Bruno, Frost & Humphries (2017) from CRCNS data set apl-1

**Paper.** Bruno AM, Frost WN, Humphries MD (2017). A spiral attractor network drives rhythmic
locomotion. *eLife* 6:e27342. [doi:10.7554/elife.27342](https://doi.org/10.7554/elife.27342). The
claims file was written from the version of record (PMC5546814): main text, Materials and methods
and all figure legends and supplement legends.

**Data set.** CRCNS apl-1, [doi:10.6080/K0SN074B](https://doi.org/10.6080/K0SN074B), streamed from
the public bucket `crcnsarchive` under `apl-1/live/`. Version: `unversioned`. CRCNS data sets carry
no versions (docs/archives.md), and the bucket holds one copy of the processed files (`live/`; the
`orig/` folder holds only one raw optical file). That copy is pinned by the MD5 sums printed in the
data check, which match the data set's `checksums.md5`. The paper cites the data set's DOI and no
version. Files read: FileTable.mat, SpikeData.mat, ExtracellularData.mat, Coordinates.mat and
diode_template.mat; the 6.9 GB raw optical archive is not needed.

**Method.** The claims file decides what is tested. Where it leaves a detail open, the detail is
taken from the paper's Methods or from its code (github.com/mdhumphries/AplysiaAttractorAnalysis at
commit e5f28e98), cited in `apl.py`. Two details recur in almost every claim: the width of the
Gaussian kernel and the rule for the number of PCs. Each is run under every reading the criteria
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('reproduce_bruno_2017.ipynb',4)
for i in [52,79,100]:
    print('=====',i); print(nb.cells[i].source)
"
```

```
===== 52
DIV = {}
rows = []
for k in ["own/min80", "own/le80", "pooled/min80", "pooled/le80"]:
    for stat in ["period_mean", "period_median"]:
        allv = []
        for o, s in zip(RUNS[k], SUM[k].itertuples()):
            for d in apl.divergences(o, getattr(s, stat)):
                d.update(prep=o["prep"], bout=o["bout"])
                allv.append(d)
        V = pd.DataFrame(allv)
        DIV[(k, stat)] = V
        kept = V[~V.near_end]
        code_kept = V[V.returned | ~V.near_end]
        rows.append({"reading": k, "period": stat, "all_periods": len(V), "kept": len(kept),
                     "returned": int(kept.returned.sum()), "fraction": round(kept.returned.mean(), 3),
                     "code_rule_kept": len(code_kept), "code_rule_returned": int(code_kept.returned.sum())})
print(pd.DataFrame(rows).to_string(index=False))
V = DIV[(ADOPT, "period_mean")]
print("\nadopted reading, mean period:")
[... 92 more lines not kept]
```

**Agent**

Running the entry once now to get the current outputs; I'll edit the conclusions against them and then run it again for the final copy.

**Agent calls Bash**

```bash
cd  && date -u && python tools/entry.py all entries/crcns-apl-1-bruno-2017 > $TMPDIR/run1.log 2>&1; echo exit $?; date -u; tail -20 $TMPDIR/run1.log
```

```
Sun Nov  8 18:34:51 UTC 2026
exit 0
Sun Nov  8 19:14:45 UTC 2026
Installed kernelspec registry-crcns-apl-1-bruno-2017 in executed/crcns-apl-1-bruno-2017/.venv/share/jupyter/kernels/registry-crcns-apl-1-bruno-2017
0 error(s)
pass  reproduce_bruno_2017.ipynb  (2384 s)
```

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('executed/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb',4)
for i in [20,52,61,79,83,100,109]:
    print('=====',i)
    for o in nb.cells[i].outputs:
        if 'text' in o: print(o['text'][:6000])
"
```

```
===== 20
Gaussian SD (s) by reading:  {'sqrt12': (np.float64(0.069), np.float64(0.125)), 'twelve': (np.float64(0.02), np.float64(0.036)), 'own': (np.float64(0.238), np.float64(0.432)), 'pooled': (np.float64(0.298), np.float64(0.374))}

PCA under every reading in 9 s
    sd count  min  max  in_3.6_to_8.8  min_neurons_over_dims  ratio_over_10
sqrt12 min80   22   41              0                    2.7              0
sqrt12  le80   21   40              0                    2.8              0
twelve min80   34   76              0                    1.8              0
twelve  le80   33   75              0                    1.8              0
   own min80    4    8             30                    9.4             29
   own  le80    3    7             28                   10.7             30
pooled min80    4    9             29                    9.4             29
pooled  le80    3    8             28                   10.7             30

counts per recording (min80 | le80) for the code's width (own median ISI):
            file  own_min80  own_le80  pooled_min80  pooled_le80  neurons
 Jun0214da01.mat          7         6             7            6      136
 Jun0214da02.mat          7         6             7            6      136
 Jun0214da03.mat          8         7             8            7      136
Jun0414Bda01.mat          4         3             5            4      105
[... 224 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/crcns-apl-1-bruno-2017 && grep -n "def run_decoding\|def decode_program\|def _irls\|def glm\|Pool\|concurrent\|warm\|def fit_poisson" -A3 apl.py | head -80
```

```
385:    from concurrent.futures import ProcessPoolExecutor
386-    import multiprocessing as mp
387-    jobs = [(r, float(s), rule, lld) for r, s in zip(recs, sds)]
388:    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as ex:
389-        return list(ex.map(analyse_program, jobs))
390-
391-
--
597:    from concurrent.futures import ProcessPoolExecutor
598-    import multiprocessing as mp
599-    jobs = []
600-    for prep in sorted({r["prep"] for r in recs}):
--
604:    with ProcessPoolExecutor(workers, mp_context=mp.get_context("fork")) as ex:
605-        return list(ex.map(manifold_prep, jobs))
606-
607-
--
743:        b = poisson_glm(X, y, beta=b)     # warm start from the previous window
744-        fit = np.exp(np.clip(X @ b, -30, 30))
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 680,790p apl.py; git -C  log --oneline -3 -- entries/crcns-apl-1-bruno-2017/apl.py
```

```
return best, int(ts.size)


def poisson_glm(X, y, iters=25, tol=1e-6, beta=None):
    """Poisson GLM with log link by iteratively reweighted least squares (as MATLAB glmfit);
    X includes the intercept column. y may be non-integer, as the code fits a rate. Stops when
    the deviance changes by less than ``tol`` relatively, or after ``iters`` iterations (a
    standard choice; the forecasts agree to three decimals with 100 iterations)."""
    if beta is None:
        beta = np.zeros(X.shape[1])
        beta[0] = np.log(max(y.mean(), 1e-6))
    else:
        beta = beta.copy()
    dev_old = np.inf
    for _ in range(iters):
        eta = np.clip(X @ beta, -30, 30)
        mu = np.exp(eta)
        z = eta + (y - mu) / mu
        W = mu
        XtW = X.T * W
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('reproduce_bruno_2017.ipynb',4)
print(nb.cells[1].source)
print(nb.cells[83].source)
"; ls executed/crcns-apl-1-bruno-2017/
```

```
import os
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("OPENBLAS_NUM_THREADS", "1")
import time
import resource
import warnings

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from scipy import stats

import apl

warnings.filterwarnings("ignore", category=RuntimeWarning)
pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_rows", 200)
started = time.time()
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/diag.py <<'EOF'
import os, time
os.environ["OMP_NUM_THREADS"]="1"; os.environ["OPENBLAS_NUM_THREADS"]="1"
import numpy as np, apl
t0=time.time()
D=apl.load(); recs=D["recs"]
sds=apl.gaussian_sds(recs)
q=next(q for q in D["p10"] if q["prep"]==4 and q["bout"]==1)
i=next(i for i,r in enumerate(recs) if r["prep"]==4 and r["bout"]==1)
P=apl.Program(recs[i], float(sds["own"][i]), "min80")
for frac in [0.8,0.9]:
    d=apl.n_pcs(P.ev,frac,"min80"); pcs=P.proj[:,:d]
    rate=apl.sdf_matrix([q["t"]], float(sds["own"][i]), P.t_end)[P.ix_stim,0]
    for h in [5,15]:
        o=apl.decode_p10(pcs,rate,P.stimbins,h,step_s=0.2,train_frac=0.5)
        M=np.array([w["MAE"] for w in o])
        print(frac,d,h,len(o),"meanMAE %.4g medMAE %.4g maxMAE %.4g n>1000 %d"%(M.mean(),np.median(M),M.max(),(M>1000).sum()), "rate max %.1f"%rate.max(), f"{time.time()-t0:.0f}s")
EOF
python $TMPDIR/diag.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/diag.py", line 3, in <module>
    import numpy as np, apl
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
executed/crcns-apl-1-bruno-2017/.venv/bin/python $TMPDIR/diag.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/diag.py", line 3, in <module>
    import numpy as np, apl
ModuleNotFoundError: No module named 'apl'
```

**Agent calls Bash**

```bash
PYTHONPATH=. executed/crcns-apl-1-bruno-2017/.venv/bin/python $TMPDIR/diag.py
```

```
0.8 5 5 174 meanMAE 13.28 medMAE 12.22 maxMAE 28.02 n>1000 0 rate max 654.5 4s
0.8 5 15 174 meanMAE 5.27e+11 medMAE 14.51 maxMAE 1.069e+13 n>1000 65 rate max 654.5 12s
0.9 11 5 174 meanMAE 50.88 medMAE 14.55 maxMAE 6003 n>1000 1 rate max 654.5 17s
0.9 11 15 174 meanMAE 9.12e+11 medMAE 1.354e+10 maxMAE 1.069e+13 n>1000 116 rate max 654.5 50s
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='apl.py'
s=open(p).read()
s=s.replace('''            out.append({"t": s0, "R": np.corrcoef(yf, fc)[0, 1], "MAE": np.median(np.abs(yf - fc)),
                        "R_train": np.corrcoef(y, fit)[0, 1], "MAE_train": np.median(np.abs(y - fit))})''','''            out.append({"t": s0, "R": np.corrcoef(yf, fc)[0, 1], "MAE": np.median(np.abs(yf - fc)),
                        "R_train": np.corrcoef(y, fit)[0, 1], "MAE_train": np.median(np.abs(y - fit)),
                        "fc_max": float(fc.max())})''')
s=s.replace('''    return {"file": rec["file"], "prep": rec["prep"], "bout": rec["bout"], "d": d, "best": best,
            "windows": res[best],''','''    # fc_max_by_history: the largest forecast of each window, to count forecasts that diverge
    # (reported, not judged; the clip of the linear predictor at 30 caps them at about 1e13).
    return {"file": rec["file"], "prep": rec["prep"], "bout": rec["bout"], "d": d, "best": best,
            "rate_max": float(rate.max()),
            "fc_max_by_history": {h: np.array([w["fc_max"] for w in v]) for h, v in res.items()},
            "windows": res[best],''')
open(p,'w').write(s)
EOF
grep -n "fc_max" apl.py
```

```
752:                        "fc_max": float(fc.max())})
780:    # fc_max_by_history: the largest forecast of each window, to count forecasts that diverge
784:            "fc_max_by_history": {h: np.array([w["fc_max"] for w in v]) for h, v in res.items()},
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p='reproduce_bruno_2017.ipynb'
nb=nbformat.read(p,4)
src1='''# Diverging forecasts: windows whose largest forecast exceeds 10 times the response's largest P10
# rate (reported, not judged). The linear predictor is clipped at 30, so a diverging forecast reaches
# about 1e13 spikes/s, and a few such windows dominate a mean MAE over windows.
def diverging(res, frac_label):
    rows = []
    for o in res:
        lim = 10 * o["rate_max"]
        allh = np.concatenate(list(o["fc_max_by_history"].values()))
        sel = o["fc_max_by_history"][o["best"]]
        rows.append({"model": frac_label, "prep": o["prep"], "bout": o["bout"], "history_ms": o["best"] * 10,
                     "diverging_selected": int((sel > lim).sum()), "windows": sel.size,
                     "largest_forecast_selected": sel.max(), "diverging_all_histories": int((allh > lim).sum()),
                     "windows_all_histories": allh.size})
    return pd.DataFrame(rows)
rows = []
for key, res in DEC.items():
    T = diverging(res, "/".join(key))
    rows.append({"reading": key[0], "variance": key[1], "windowing": key[2],
                 "responses_with_diverging_selected": int((T.diverging_selected > 0).sum()),
                 "diverging_selected": int(T.diverging_selected.sum()), "windows_selected": int(T.windows.sum()),
                 "largest_forecast_selected": T.largest_forecast_selected.max(),
                 "diverging_all_histories": int(T.diverging_all_histories.sum()),
                 "windows_all_histories": int(T.windows_all_histories.sum())})
print("windows with a forecast above 10 times the response's largest P10 rate, per decoding run:")
print(pd.DataFrame(rows).to_string(index=False))
print("\nown/min80, code windowing, 80%, per response:")
print(diverging(DEC[("own/min80", "80", "code")], "code").to_string(index=False))

# Sensitivity to rounding: preparation 4, bout 1, own/min80, code windowing, with the PCs perturbed
# by Gaussian noise of 1e-9 times their SD (seeded).
rng_div = np.random.default_rng(611)
i41 = next(i for i, r in enumerate(recs) if r["prep"] == 4 and r["bout"] == 1)
q41 = next(q for q in D["p10"] if q["prep"] == 4 and q["bout"] == 1)
P41 = apl.Program(recs[i41], float(sds["own"][i41]), "min80")
pcs41 = P41.proj[:, :apl.n_pcs(P41.ev, 0.8, "min80")]
rate41 = apl.sdf_matrix([q41["t"]], float(sds["own"][i41]), P41.t_end)[P41.ix_stim, 0]
rows = []
for h in [5, 15]:
    for name, X in [("as computed", pcs41), ("perturbed 1e-9 SD", pcs41 + 1e-9 * pcs41.std(0) * rng_div.standard_normal(pcs41.shape))]:
        o = apl.decode_p10(X, rate41, P41.stimbins, h, step_s=0.2, train_frac=0.5)
        M = np.array([w["MAE"] for w in o]); R = np.array([w["R"] for w in o]); F = np.array([w["fc_max"] for w in o])
        rows.append({"history_ms": h * 10, "pcs": name, "mean_MAE": M.mean(), "median_MAE": np.median(M),
                     "mean_R": np.nanmean(R), "diverging": int((F > 10 * rate41.max()).sum()), "windows": len(o)})
print("\npreparation 4, bout 1, own/min80, code windowing, sensitivity to a perturbation of the PCs:")
print(pd.DataFrame(rows).to_string(index=False))'''
c=nbformat.v4.new_code_cell(src1, metadata={"tags":["claim:fig6d-decode-p10"]})
nb.cells.insert(81,c)
nbformat.write(nb,p)
EOF
python -c "
import nbformat
nb=nbformat.read('reproduce_bruno_2017.ipynb',4)
for i in range(78,86): print(i, nb.cells[i].cell_type, nb.cells[i].metadata.get('tags'), nb.cells[i].source[:60].replace(chr(10),' '))"
```

```
78 markdown None ## fig6d-decode-p10  > P10 nerve activity can be fitted and 
79 code ['claim:fig6d-decode-p10'] t0 = time.time() def p10_jobs(frac, windowing, hists, mode="
80 code ['claim:fig6d-decode-p10'] # Preparation 4, bout 1 against a response that decodes well
81 code ['claim:fig6d-decode-p10'] # Diverging forecasts: windows whose largest forecast exceed
82 markdown None **Result: partially reproduced.** With the Methods' windowin
83 markdown None ## fig6s2-dimensions-p10  > The nine recordings with P10 act
84 code ['claim:fig6s2-dimensions-p10'] p10_idx = [next(i for i, r in enumerate(recs) if r["prep"] =
85 markdown None **Result: reproduced, under own/le80.** Under the readings w
```

**Agent calls Bash**

```bash
cat > $TMPDIR/t2.py <<'EOF'
import os, time, json
os.environ["OMP_NUM_THREADS"]="1"
import numpy as np, pandas as pd, apl
pd.set_option("display.width", 220)
t0=time.time()
D=apl.load(); recs=D["recs"]; sds=apl.gaussian_sds(recs)
qs=[q for q in D["p10"] if q["prep"]==4][:2]
def jobs(frac,win,h):
    J=[]
    for q in qs:
        i=next(i for i,r in enumerate(recs) if r["prep"]==q["prep"] and r["bout"]==q["bout"])
        J.append((recs[i],q["t"],float(sds["own"][i]),frac,win,h,"min80"))
    return J
DEC={("own/min80","80","code"):apl.run_decoding(jobs(0.8,"code",[5,15])),("own/min80","80","methods"):apl.run_decoding(jobs(0.8,"methods",[5]))}
nb=json.load(open("reproduce_bruno_2017.ipynb"))
exec("".join(nb["cells"][81]["source"]))
print(time.time()-t0)
EOF
PYTHONPATH=. executed/crcns-apl-1-bruno-2017/.venv/bin/python $TMPDIR/t2.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/t2.py", line 16, in <module>
    exec("".join(nb["cells"][81]["source"]))
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<string>", line 26
    print("
          ^
SyntaxError: unterminated string literal (detected at line 26)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p='reproduce_bruno_2017.ipynb'
nb=nbformat.read(p,4)
c=nb.cells[81]
c.source=c.source.replace('print("\n','print("\\n')
nbformat.write(nb,p)
print(c.source.count('\\n'))
EOF
PYTHONPATH=. executed/crcns-apl-1-bruno-2017/.venv/bin/python $TMPDIR/t2.py
```

```
2
windows with a forecast above 10 times the response's largest P10 rate, per decoding run:
  reading variance windowing  responses_with_diverging_selected  diverging_selected  windows_selected  largest_forecast_selected  diverging_all_histories  windows_all_histories
own/min80       80      code                                  0                   0               348                 338.748717                       74                    696
own/min80       80   methods                                  0                   0                80                 608.617604                        0                     80

own/min80, code windowing, 80%, per response:
model  prep  bout  history_ms  diverging_selected  windows  largest_forecast_selected  diverging_all_histories  windows_all_histories
 code     4     1          50                   0      174                 103.354928                       67                    348
 code     4     2          50                   0      174                 338.748717                        7                    348

preparation 4, bout 1, own/min80, code windowing, sensitivity to a perturbation of the PCs:
 history_ms               pcs     mean_MAE  median_MAE    mean_R  diverging  windows
         50       as computed 1.327534e+01   12.215633 -0.101612          0      174
         50 perturbed 1e-9 SD 1.325761e+01   12.205132 -0.102160          0      174
        150       as computed 5.270273e+11   14.513114 -0.045879         67      174
        150 perturbed 1e-9 SD 2.825161e+11   14.393777 -0.046503         65      174
34.16639590263367
```

**Agent calls Bash**

```bash
cat README.md entry.yaml
```

```
# Bruno, Frost & Humphries (2017) from CRCNS apl-1

Tests the findings of [Bruno, Frost & Humphries (2017)](https://doi.org/10.7554/elife.27342),
"A spiral attractor network drives rhythmic locomotion", on CRCNS data set
[apl-1](https://doi.org/10.6080/K0SN074B): spike times of 30 voltage-sensitive dye recordings of the
Aplysia pedal ganglion (three evoked bouts in each of 10 preparations), P10 nerve spikes for nine of
them, and neuron positions on the photodiode array.

| Claim | Outcome |
|---|---|
| Counts of preparations, recordings and neurons; 120 to 180 neurons per recording | Partially reproduced |
| Slow (at most 0.1 Hz) oscillation in the spectra | Reproduced |
| Decaying population rate | Reproduced |
| 4 to 8 dimensions for 80% of the variance | Reproduced (under the code's count rule) |
| Periodic recurrence at 10 to 15 s in many responses | Reproduced |
| A single dominant orbit | Reproduced |
| Periods robust to the recurrence threshold | Reproduced |
| Coalescence within one period of stimulation | Not reproduced |
| Same manifold across bouts (two axis choices) | Reproduced (2 claims) |
| Different initial conditions | Reproduced |
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p='reproduce_bruno_2017.ipynb'
nb=nbformat.read(p,4)
C=nb.cells
def rep(i, old, new):
    assert old in C[i].source, (i, old)
    C[i].source = C[i].source.replace(old, new)
# header
rep(0, "for.\n\n| Claim |", """for.

**Revision after verification round 2.** Text the numbers did not support was corrected (the
dimension ranges of the printed widths, the consistency of fig4c's means, the exclusion rule in
fig7gh); the code's removal rule of fig3h under the adopted reading is now stated; a printout of the
decoding forecasts that diverge was added, with a test of their sensitivity to rounding. The record
proposes a change of fig6d's outcome to not reproduced, for a third verification round.

| Claim |""")
rep(21, """The Methods' printed width (median
ISI / 12, or / sqrt(12)) gives 22 to 76 dimensions""", """The Methods' printed width gives 21 to 76
dimensions (median ISI / sqrt(12), 21 to 41; median ISI / 12, 33 to 76)""")
rep(22, "the two narrow widths give 22 to 75\ndimensions", "the two narrow widths give 21 to 76\ndimensions")
rep(53, """The code's rule (dropping only the periods that never return) keeps 17 to 21. The counts meet
the criterion only under own/le80""", """The code's rule (dropping only the periods within two cycles of the end that never return) keeps
17 to 21 over the readings, and under the adopted reading it keeps 19 periods of which 18 return
(0.947), with either period, which meets both tolerances and matches the paper's 19. The criterion
states the Methods' rule ("We removed all such divergent periods whose divergent point fell within
two oscillation cycles of the end of the recording", Testing return to the same manifold after
perturbation), so the code's rule is reported, not judged. Under the Methods' rule the counts meet
the criterion only under own/le80""")
rep(53, """decides.""", """decides. The criterion has no partial outcome; it is recorded as partially reproduced because
the returned fraction holds and the two counts miss their tolerances by 1.1 and 0.3.""")
rep(62, """so the statement's "consistent with" holds for the means only (10.45 s against
a median recurrence period of 12.73 s). The criterion judges the mean against 10 s and reports the
correlation; the statement's "consistent with" is therefore reported, not judged, and holds only for
the means.""", """and the means do not agree within the claim's tolerance either: 10.45 s against a median
recurrence period of 12.73 s, 2.3 s apart where the tolerance is 1 s. The criterion judges the mean
against 10 s and reports the correlation, so the statement's "consistent with" is reported, not
judged; neither the correlation nor the means support it.""")
open('/dev/null','w')
nbformat.write(nb,p)
for i in [0,21,22,53,62]: print(i, C[i].source[-700:], '\n')
EOF
```

```
0 ons, fig3f-pairwise-similarity | tested |
| fig3h-perturbations-return, fig3i-same-manifold-after | tested |
| fig4bc-stable-spiral, fig4c-orbital-period, fig4s1a-contracting-dimensions, fig4s1b-rotation-dominant | tested |
| fig5b-period-changes, fig5c-no-relation-contraction | tested |
| fig6s1-no-p10-motorneurons, fig6d-decode-p10, fig6s2-dimensions-p10 | tested |
| fig7a-long-tailed-participation, fig7f-strongly-variable-neurons, halving-participation, fig7s1-rate-synchrony, fig7gh-robust-to-participation | tested |
| fig7s2-no-invariant-core | tested (Python port of the code's ensemble toolbox) |
| fig8-caudolateral | blocked: metadata insufficient (orientation of the array not given) | 

21 
28 of 30 counts lie in 3.6 to 8.8 (3 to 7) and the number of neurons divided by the count exceeds
10 in all 30 (lowest 10.7); pooled/le80 gives the same. With the Methods' count (smallest number
reaching 80%) the counts are 4 to 8 for own/min80, the paper's range, all 30 in 3.6 to 8.8, but the
ratio exceeds 10 in 29 of 30 (lowest 9.4, 75 neurons and 8 PCs). The Methods' printed width gives 21 to 76
dimensions (median ISI / sqrt(12), 21 to 41; median ISI / 12, 33 to 76) and ratios of 1.8 to 2.8 at the lowest; it
cannot give the paper's counts. The adopted reading of the later claims (own/min80) is therefore one
under which this claim fails, by one response; its counts are the paper's 4 to 8. 

22  The adopted reading, used where one reading has to be chosen, is
`own/min80`: the median ISI of the recording (the width the code uses; the Methods compute it
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('reproduce_bruno_2017.ipynb',4)
s=nb.cells[0].source; i=s.find('round 2'); print(s[i-30:i+600])"
```

```
**Revision after verification round 2.** Text the numbers did not support was corrected (the
dimension ranges of the printed widths, the consistency of fig4c's means, the exclusion rule in
fig7gh); the code's removal rule of fig3h under the adopted reading is now stated; a printout of the
decoding forecasts that diverge was added, with a test of their sensitivity to rounding. The record
proposes a change of fig6d's outcome to not reproduced, for a third verification round.

| Claim | Tested or blocked |
|---|---|
| dataset-size, fig1d-slow-oscillation, fig1e-decaying-rate, fig2b-dimensions | tested |
| fig2ef-periodic-recu
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p='reproduce_bruno_2017.ipynb'
nb=nbformat.read(p,4)
C=nb.cells
def rep(i, old, new):
    assert old in C[i].source, (i, old)
    C[i].source = C[i].source.replace(old, new)
assert C[103].source.startswith("**Result: partially reproduced, resting on the adopted")
rep(103, """no slope is significant (lowest p 0.085
and 0.069). The outcome depends on the reading.""", """no slope is significant with the legend's exclusion (lowest p 0.085
and 0.069). With the code's exclusion (pairs with normalised distance below 1, 29 pairs with the
recurrent points), pooled/min80 has a significant total-change slope with the recurrent points
(p = 0.028 and 0.029, participation readings (a) and (b)), and pooled/le80 has none (lowest p 0.069).
The outcome depends on the reading, and under pooled/min80 on the exclusion rule.""")
i=110
assert C[i].source.startswith("## Summary")
rep(i, "| fig6d-decode-p10 | partially reproduced |", "| fig6d-decode-p10 | partially reproduced (not reproduced proposed) |")
rep(i, "| fig7gh-robust-to-participation | one slope of two significant | one slope with recurrent points | no slope | no slope |",
       "| fig7gh-robust-to-participation | one slope of two significant | one slope with recurrent points | no slope (one with the code's exclusion) | no slope |")
rep(i, """The Methods' kernel
width as printed (median ISI / 12) gives 22 to 76 dimensions,""", """The Methods' kernel
width as printed gives 21 to 76 dimensions (33 to 76 with median ISI / 12, 21 to 41 with / sqrt(12)),""")
nbformat.write(nb,p)
EOF
grep -n "fig6d-decode-p10 | 8 of 9" -n reproduce_bruno_2017.ipynb
```

```
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
AssertionError
2408:    "| fig6d-decode-p10 | 8 of 9 | 8 of 9 | 8 of 9 | 8 of 9 |\n",
```

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('reproduce_bruno_2017.ipynb',4)
for i in range(100,113): print(i, nb.cells[i].cell_type, nb.cells[i].source[:70].replace(chr(10),' '))"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    for i in range(100,113): print(i, nb.cells[i].cell_type, nb.cells[i].source[:70].replace(chr(10),' '))
                                      ~~~~~~~~^^^
IndexError: list index out of range
100 markdown ## fig7gh-robust-to-participation  > The distance between a pair of re
101 code # Participation under each reading of width and count: (a) the program
102 markdown **Result: partially reproduced, resting on the adopted reading.** Unde
103 markdown ## fig7s2-no-invariant-core  > No small invariant core of strongly par
104 code t0 = time.time() TYPES = {(mode, seed): apl.run_types(recs, sds[mode],
105 markdown **Result: reproduced.** With the port of the code's ensemble toolbox, 
106 markdown ## fig8-caudolateral  > Neurons with strong participation across the t
107 code rows = [] for side, group in [("left", [1, 2, 4, 10]), ("right", [3, 5
108 markdown **Result: blocked, metadata insufficient** (see the header). Shown for
109 markdown ## Summary  | Claim | Outcome | |---|---| | dataset-size | partially r
110 code print(f"notebook run time {(time.time() - started) / 60:.1f} min; peak
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p='reproduce_bruno_2017.ipynb'
nb=nbformat.read(p,4)
C=nb.cells
def rep(i, old, new):
    assert old in C[i].source, (i, old)
    C[i].source = C[i].source.replace(old, new)
rep(102, """no slope is significant (lowest p 0.085
and 0.069). The outcome depends on the reading.""", """no slope is significant with the legend's exclusion (lowest p 0.085
and 0.069). With the code's exclusion (pairs with normalised distance below 1, 29 pairs with the
recurrent points), pooled/min80 has a significant total-change slope with the recurrent points
(p = 0.028 and 0.029, participation readings (a) and (b)), and pooled/le80 has none (lowest p 0.069).
The outcome depends on the reading, and under pooled/min80 on the exclusion rule.""")
i=109
rep(i, "| fig6d-decode-p10 | partially reproduced |", "| fig6d-decode-p10 | partially reproduced (not reproduced proposed) |")
rep(i, "| fig7gh-robust-to-participation | one slope of two significant | one slope with recurrent points | no slope | no slope |",
       "| fig7gh-robust-to-participation | one slope of two significant | one slope with recurrent points | no slope (one with the code's exclusion) | no slope |")
rep(i, """The Methods' kernel
width as printed (median ISI / 12) gives 22 to 76 dimensions,""", """The Methods' kernel
width as printed gives 21 to 76 dimensions (33 to 76 with median ISI / 12, 21 to 41 with / sqrt(12)),""")
nbformat.write(nb,p)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  && date -u && python tools/entry.py all entries/crcns-apl-1-bruno-2017 > $TMPDIR/run2.log 2>&1; echo exit $?; date -u; tail -5 $TMPDIR/run2.log
```

```
Sun Nov  8 19:19:23 UTC 2026
exit 0
Sun Nov  8 19:58:09 UTC 2026
Installed kernelspec registry-crcns-apl-1-bruno-2017 in executed/crcns-apl-1-bruno-2017/.venv/share/jupyter/kernels/registry-crcns-apl-1-bruno-2017
0 error(s)
pass  reproduce_bruno_2017.ipynb  (2317 s)
```

**Agent calls Bash**

```bash
python -c "
import nbformat
nb=nbformat.read('executed/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb',4)
for i in [79,81,84,110]:
    print('=====',i)
    for o in nb.cells[i].outputs:
        if 'text' in o: print(o['text'][-4500:])
"
```

```
===== 79
  2     1     4          50       40            0   0.362              0.198    0.393     8.400    0.937
    2     2     5         120       40            0   0.373              0.239    0.313    27.791    0.948
    2     3     5         170       40            0   0.806              0.756    0.675    15.155    0.968
    4     1     5          50       40            0  -0.060             -0.127    0.048    19.462    0.941
    4     2     4         130       40            0   0.894              0.875    0.803    19.840    0.961
    4     3     5         200       40            0   0.605              0.505    0.464    29.461    0.929
    5     1     5          50       40            0   0.873              0.849    0.768     4.364    0.925
    5     2     5         170       40            0   0.828              0.790    0.700     6.643    0.911
    5     3     6          50       40            0   0.890              0.871    0.795    11.839    0.947

own/min80, variant: histories up to 100 ms: responses with mean R - 2 s.e.m. > 0: 8 of 9; windows in all 360
 prep  bout  dims  history_ms  windows  undefined_R  mean_R  mean_R_minus_2sem  mean_R2  mean_MAE  train_R
    2     1     4          50       40            0   0.362              0.198    0.393     8.400      NaN
    2     2     5         100       40            0   0.373              0.239    0.313    28.019      NaN
    2     3     5          90       40            0   0.810              0.761    0.679    15.339      NaN
    4     1     5          50       40            0  -0.060             -0.127    0.048    19.462      NaN
    4     2     4         100       40            0   0.893              0.873    0.801    20.139      NaN
    4     3     5         100       40            0   0.625              0.530    0.478    29.749      NaN
    5     1     5          50       40            0   0.873              0.849    0.768     4.364      NaN
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p='entries/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb'
nb=nbformat.read(p,4)
C=nb.cells
assert C[82].source.startswith("**Result: partially reproduced.** With the Methods")
C[82].source = """**Result: partially reproduced as verified; a change to not reproduced is proposed.** With the
Methods' windowing, 8 of 9 responses have mean forecast R minus 2 s.e.m. above 0 under every reading
of width and count (adopted: mean R 0.36 to 0.89). Response 1 of preparation 4 fails under all four
readings (mean R -0.060, -0.119, -0.075 and -0.124; bounds -0.127 to -0.204), with histories up to
100 ms and with the code's windowing (mean R -0.102). Its training fits are as good as the others'
(mean training R 0.94; 0.91 to 0.97 in all nine), but its forecasts fail: in the four windows
plotted the forecast R is -0.59 to 0.27, and the first forecast runs at 55 to 140 spikes/s against
a P10 rate of 0 to 24 spikes/s, while response 2 of the same preparation gives 0.81 to 0.94. The
decoding holds in eight of nine responses. The criterion requires it in each of the nine, the
statement says "in all nine", and the one failure holds under every reading, history range and
windowing run here, so the result is a failure of what the claim says; the record keeps the
verified outcome and proposes not reproduced. The Methods' windowing gives 40 forecast windows per
response (360 in all), the code's 174 per response (1566); the paper's N = 173 is close to the
code's count per response. Preparation 4's first response is the one the paper describes as
apparently chaotic (Figure 3, figure supplement 1B).

Forecasts diverge in some windows of the longer histories. Over all histories, 195 to 277 of 5760
windows (80% models, Methods windowing, the four readings) and 770 of 7830 (code windowing) have a
forecast above 10 times the response's largest P10 rate, up to the clip of the linear predictor
(about 1e13 spikes/s). The histories selected have no such window in any 80% run (largest forecast
329 to 609 spikes/s). For preparation 4, bout 1 with the code's windowing, perturbing the PCs by
1e-9 of their SD leaves the 50 ms model nearly unchanged (mean MAE 13.28 and 13.26, mean R -0.102
both times) but changes the 150 ms model's mean MAE from 5.3e11 to 2.8e11 (67 and 65 diverging
windows of 174). A mean MAE over windows with diverging forecasts therefore depends on rounding, and
so can the history selected; the executed copy reviewed in verification round 2 (not run here) gave
a mean MAE of 7.6e6 for this response. The forecast R of the selected models, on which the criterion
rests, is not affected here."""
assert C[85].source.startswith("**Result: reproduced, under own/le80.**")
C[85].source = """**Result: reproduced, under own/le80.** Under the readings with the code's count rule the nine
80% counts lie in 3 to 5 (own/le80: 3 to 5; pooled/le80: 3 to 5), and the 90% counts are at least
twice them in each. Under own/le80, with the full history grid for both, the 90% models are not
better: mean MAE lower with 90% in 6 of 9 (two-sided Wilcoxon p = 0.50, median difference -0.44) and
mean R-squared higher in 4 of 9 (p = 0.50, median difference -0.007). So one reading shows both parts.
Under pooled/le80 (four histories) the 90% models are not better either (p = 0.73 and 0.82). Under
the adopted reading (own/min80) the counts are 4 to 6, and one (6) is outside 2.7 to 5.5; there the
90% models are worse in MAE (p = 0.027, 7 of 9 worse, median +1.56 with the full grid; p = 0.020 with
four histories for both) and do not differ in R-squared (p = 0.16). No test finds the 90% models
better at p < 0.05 in any of the five comparisons. Of the selected 90% models only one window has a
diverging forecast (pooled/le80, largest forecast 6521 spikes/s), but over all histories 457 and 610
of 5760 windows diverge under own/le80 and own/min80 (fig6d's printout), so the mean MAEs and these
p-values depend on rounding through the history selected: the executed copy reviewed in verification
round 2 (not run here) gave p = 0.91 for MAE under own/le80, with the same conclusion."""
nbformat.write(nb,p)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/crcns-apl-1-bruno-2017 && python - <<'EOF'
import nbformat
p='reproduce_bruno_2017.ipynb'
nb=nbformat.read(p,4)
C=nb.cells
C[82].source=C[82].source.replace("(adopted: mean R 0.36 to 0.89)","(adopted: mean R of the other eight 0.36 to 0.89)")
nbformat.write(nb,p)
nb=nbformat.read('../../executed/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb',4)
for o in nb.cells[80].outputs:
    if 'text' in o: print(o['text'][:3000])
EOF
sed -i 's/about 36 minutes on 4 CPUs/about 39 minutes on 4 CPUs/' README.md; sed -i 's/runtime_minutes: 36/runtime_minutes: 39/' entry.yaml; grep -n "39" README.md entry.yaml
```

```
prep 4 bout 1, window from 33 s: forecast R 0.272; P10 rate range 0.0 to 23.5, forecast range 55.4 to 137.6 spikes/s
prep 4 bout 1, window from 43 s: forecast R -0.588; P10 rate range 0.0 to 39.3, forecast range 3.3 to 14.8 spikes/s
prep 4 bout 1, window from 53 s: forecast R -0.106; P10 rate range 0.2 to 81.5, forecast range 4.1 to 16.5 spikes/s
prep 4 bout 1, window from 63 s: forecast R 0.070; P10 rate range 0.1 to 90.0, forecast range 6.1 to 36.4 spikes/s
prep 4 bout 2, window from 33 s: forecast R 0.934; P10 rate range 0.1 to 215.0, forecast range 36.6 to 233.0 spikes/s

prep 4 bout 2, window from 43 s: forecast R 0.903; P10 rate range 0.0 to 215.0, forecast range 24.0 to 234.7 spikes/s
prep 4 bout 2, window from 53 s: forecast R 0.931; P10 rate range 34.5 to 235.8, forecast range 32.2 to 288.6 spikes/s
prep 4 bout 2, window from 63 s: forecast R 0.817; P10 rate range 0.0 to 73.2, forecast range 16.5 to 76.2 spikes/s

README.md:49:- `reproduce_bruno_2017.ipynb`: the analysis, about 39 minutes on 4 CPUs (the recurrence analysis
entry.yaml:15:  runtime_minutes: 39
```

**Agent calls Bash**

```bash
sed -i 's/| P10 decoded in all nine responses | Partially reproduced |/| P10 decoded in all nine responses | Partially reproduced (change to not reproduced proposed) |/' README.md; grep -n "P10 decoded" README.md; python -c "
import nbformat
nb=nbformat.read('../../executed/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb',4)
for i in [70,73,104]:
    print('=====',i)
    for o in nb.cells[i].outputs:
        if 'text' in o: print(o['text'][-2500:])
print(nb.cells[71].source); print(nb.cells[105].source)
"
```

```
31:| P10 decoded in all nine responses | Partially reproduced (change to not reproduced proposed) |
===== 70
permutation tests in 121 s
     reading  slowing_p<0.01  speeding_p<0.01  no_change  windows_min  windows_max
   own/min80              12                4         14           31           73
 pooled/le80              11                6         13           31           73
    own/le80              14                5         11           27           73
pooled/min80              10                5         15           29           72

adopted reading; p from 10000 permutations of the delays (two-sided), p_code from the code's 100000 pooled permutations (one-sided):
 prep  bout     rho      p  n_windows  p_code
    1     1  0.4389 0.0006         63  0.0020
    1     2  0.6211 0.0001         58  0.0000
    1     3  0.1638 0.3218         56  0.1604
    2     1  0.6202 0.0001         66  0.0015
    2     2  0.4103 0.0260         62  0.0140
    2     3  0.6447 0.0001         67  0.0000
    3     1 -0.5273 0.0011         50  0.0019
    3     2 -0.6177 0.0001         60  0.0008
    3     3  0.7709 0.0001         57  0.0000
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas 2>/dev/null; grep -rn "proposed" -A25 schemas/attempt* 2>/dev/null | head -60; grep -rln "proposed:" attempts | head -3
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
252:          "proposed": {
253-            "description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
254-            "type": "object",
255-            "additionalProperties": false,
256-            "required": [
257-              "outcome",
258-              "reason"
259-            ],
260-            "properties": {
261-              "outcome": {
262-                "enum": [
263-                  "reproduced",
264-                  "partially_reproduced",
265-                  "not_reproduced",
266-                  "blocked"
267-                ]
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n '"verifications"' -A80 schemas/attempt.schema.json | head -100; grep -n "proposed:" -B3 -A6 attempts/000491-raicevic-2023-01.yaml | head -30
```

```
334:    "verifications": {
335-      "type": "array",
336-      "items": {
337-        "type": "object",
338-        "additionalProperties": false,
339-        "required": [
340-          "date",
341-          "kind",
342-          "by",
343-          "results"
344-        ],
345-        "properties": {
346-          "date": {
347-            "type": "string",
348-            "format": "date"
349-          },
350-          "kind": {
351-            "enum": [
352-              "agent",
353-              "person",
[... 71 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/crcns-apl-1-bruno-2017-01.yaml",
 "old_string": "    evidence. The code's rule, removing only periods that never return, keeps 17 to 21.",
 "new_string": "    evidence. The code's rule, removing only the periods within two cycles of the end that never return,\n    keeps 17 to 21 over the readings; under the adopted reading it keeps 19 of which 18 return (0.947),\n    with either period, which meets both tolerances and matches the paper's 19. The criterion states\n    the Methods' rule (\"We removed all such divergent periods whose divergent point fell within two oscillation\n    cycles of the end of the recording\"), so the code's rule is reported, not judged. The criterion has\n    no partial outcome; partially reproduced is kept because the returned fraction holds and the two counts\n    miss their tolerances by 1.1 and 0.3."
}
```

```
The file attempts/crcns-apl-1-bruno-2017-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/crcns-apl-1-bruno-2017-01.yaml",
 "old_string": "    periods (Pearson r = -0.063, p = 0.74; -0.12 to 0.03 under the other readings), so consistency holds\n    only for the means (10.45 s against a median recurrence period of 12.73 s). The criterion judges the\n    mean and reports the correlation, so \"consistent with\" is reported, not judged.",
 "new_string": "    periods (Pearson r = -0.063, p = 0.74; -0.12 to 0.03 under the other readings), and the means do not\n    agree within the claim's tolerance either (10.45 s against a median recurrence period of 12.73 s,\n    2.3 s apart where the tolerance is 1 s). The criterion judges the mean and reports the correlation,\n    so \"consistent with\" is reported, not judged; neither the correlation nor the means support it."
}
```

```
The file attempts/crcns-apl-1-bruno-2017-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/crcns-apl-1-bruno-2017-01.yaml",
 "old_string": "  notes: Methods' windowing, mean forecast R minus 2 s.e.m. above 0 in 8 of 9 responses under every reading\n    of width and count (adopted mean R 0.36 to 0.89). Response 1 of preparation 4 fails under all four\n    (mean R -0.060, -0.127, -0.060 and -0.119; bounds -0.128 to -0.206), with histories up to 100 ms,\n    and with the code's windowing (mean R -0.101). Its training fit is good (mean training R 0.94; 0.91\n    to 0.97 in all nine) but its forecasts are not, forecast R -0.59 to 0.27 in four windows plotted,\n    against 0.81 to 0.94 for response 2 of the same preparation. The decoding holds in eight of nine,\n    so the claim holds in part. Forecast windows, 40 per response with the Methods' windowing (360), 174\n    per response with the code's (1566); the paper's N = 173 is close to the code's count per response.\n    The failing response is the one the paper describes as apparently chaotic.",
 "new_string": "  notes: Methods' windowing, mean forecast R minus 2 s.e.m. above 0 in 8 of 9 responses under every reading\n    of width and count (adopted, mean R of the other eight 0.36 to 0.89). Response 1 of preparation 4\n    fails under all four (mean R -0.060, -0.119, -0.075 and -0.124 for own/min80, own/le80, pooled/min80\n    and pooled/le80; bounds -0.127 to -0.204), with histories up to 100 ms, and with the code's windowing\n    (mean R -0.102). Its training fit is good (mean training R 0.94; 0.91 to 0.97 in all nine) but its\n    forecasts are not, forecast R -0.59 to 0.27 in four windows plotted, against 0.82 to 0.93 for response\n    2 of the same preparation. The decoding holds in eight of nine. Forecast windows, 40 per response\n    with the Methods' windowing (360), 174 per response with the code's (1566); the paper's N = 173 is\n    close to the code's count per response. The failing response is the one the paper describes as apparently\n    chaotic. Forecasts diverge in some windows of the longer histories (195 to 277 of 5760 windows over\n    all histories with the Methods' windowing, 770 of 7830 with the code's, above 10 times the response's\n    largest P10 rate, up to about 1e13 spikes/s at the clip of the linear predictor); the selected histories\n    have none in any 80% run. A perturbation of the PCs by 1e-9 of their SD changes the mean MAE of preparation\n    4, bout 1 at 150 ms from 5.3e11 to 2.8e11 and leaves the 50 ms model nearly unchanged, so mean MAEs\n    with diverging windows, and the history selected from them, depend on rounding; the forecast R on\n    which the criterion rests is not affected here."
}
```

```
The file attempts/crcns-apl-1-bruno-2017-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
p='entries/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb'
nb=nbformat.read(p,4)
s=nb.cells[82].source
assert "gives 0.81 to 0.94" in s
nb.cells[82].source=s.replace("gives 0.81 to 0.94","gives 0.82 to 0.93")
nbformat.write(nb,p)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/crcns-apl-1-bruno-2017-01.yaml",
 "old_string": "  output: claim:fig6d-decode-p10\n  notes:",
 "new_string": "  output: claim:fig6d-decode-p10\n  proposed:\n    outcome: not_reproduced\n    reason: The criterion is met only when the mean forecast R minus 2 s.e.m. is above 0 in each of the\n      nine responses, and it has no partial rule; the statement says \"in all nine\". Response 1 of preparation\n      4 fails under all four readings of width and count (mean R -0.060 to -0.124, bounds -0.127 to -0.204),\n      with histories up to 100 ms and with the code's windowing (mean R -0.102), so the failure does not\n      depend on a reading. Eight of nine is a failure of what the claim says, not a weaker effect, as the\n      verifier of round 2 found. The analysis is in the fig6d section of the notebook (the decoding table\n      under every reading, the plot of that response and the printout of diverging forecasts).\n  notes:"
}
```

```
The file attempts/crcns-apl-1-bruno-2017-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now fig6s2, fig7gh, fig7s2 in the record.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/crcns-apl-1-bruno-2017-01.yaml",
 "old_string": "    and pooled/le80, and the 90% counts at least double them in each. Under own/le80 with the full history\n    grid for both, the 90% models are not better, mean MAE lower in 5 of 9 (two-sided Wilcoxon p = 0.91,\n    median difference -0.13) and mean R-squared higher in 4 of 9 (p = 0.50). Under pooled/le80 (four histories)\n    p = 0.65 and 0.91. Under the adopted reading (own/min80) the counts are 4 to 6 and one (6) is outside\n    2.7 to 5.5; there the 90% models are worse in MAE (p = 0.027, 7 of 9 worse, full grid; p = 0.039 with\n    four histories for both) and do not differ in R-squared (p = 0.13). No comparison finds the 90% models\n    better at p < 0.05.",
 "new_string": "    and pooled/le80, and the 90% counts at least double them in each. Under own/le80 with the full history\n    grid for both, the 90% models are not better, mean MAE lower in 6 of 9 (two-sided Wilcoxon p = 0.50,\n    median difference -0.44) and mean R-squared higher in 4 of 9 (p = 0.50). Under pooled/le80 (four histories)\n    p = 0.73 and 0.82. Under the adopted reading (own/min80) the counts are 4 to 6 and one (6) is outside\n    2.7 to 5.5; there the 90% models are worse in MAE (p = 0.027, 7 of 9 worse, full grid; p = 0.020 with\n    four histories for both) and do not differ in R-squared (p = 0.16). No comparison finds the 90% models\n    better at p < 0.05. Over all histories 457 (own/le80) and 610 (own/min80) of 5760 windows of the 90%\n    models have diverging forecasts, so the mean MAEs and these p-values depend on rounding through the\n    history selected; the executed copy reviewed in round 2 gave p = 0.91 for MAE under own/le80, with\n    the same conclusion."
}
```

```
The file attempts/crcns-apl-1-bruno-2017-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/crcns-apl-1-bruno-2017-01.yaml",
 "old_string": "    no slope is significant (lowest p 0.085 and 0.069). The robust fits",
 "new_string": "    no slope is significant with the legend's exclusion (lowest p 0.085 and 0.069). With the code's exclusion\n    (pairs with normalised distance below 1), pooled/min80 has a significant total-change slope with the\n    recurrent points (p = 0.028 and 0.029, participation readings (a) and (b)) and pooled/le80 has none\n    (lowest p 0.069). The robust fits"
}
```

```
The file attempts/crcns-apl-1-bruno-2017-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/crcns-apl-1-bruno-2017-01.yaml",
 "old_string": "  - Assumed, the adopted reading of width and count (own/min80); under the pooled readings the claim is\n    reproduced. Participation",
 "new_string": "  - Assumed, the adopted reading of width and count (own/min80). Under the pooled readings the claim is\n    reproduced with the legend's exclusion; with the code's exclusion pooled/min80 has one significant\n    slope (total change, recurrent points). Participation"
}
```

```
The file attempts/crcns-apl-1-bruno-2017-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/crcns-apl-1-bruno-2017-01.yaml",
 "old_string": "- claim: fig7s2-no-invariant-core\n  outcome: reproduced\n  notes:",
 "new_string": "- claim: fig7s2-no-invariant-core\n  outcome: reproduced\n  notebook: reproduce_bruno_2017.ipynb\n  output: claim:fig7s2-no-invariant-core\n  notes:"
}
```

```
The file attempts/crcns-apl-1-bruno-2017-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/crcns-apl-1-bruno-2017-01.yaml",
 "old_string": "      with the recurrence periods (r = -0.06, p = 0.74), so consistent with is not supported. B.11: on\n      a toy orbit the mean-imaginary-part period came out about 2 times the true period, because real\n      maximum eigenvalues contribute b = 0; this is inherent to the criterion''s method, and in the real\n      data p_complex1 is high, so the effect is smaller.'",
 "new_string": "      with the recurrence periods (r = -0.06, p = 0.74), so consistent with is not supported.'"
}
```

```
The file attempts/crcns-apl-1-bruno-2017-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat > $TMPDIR/v2.py <<'EOF'
import yaml
A="Agrees with the stated outcome; the Result sentences match the printed outputs."
N="No change needed."
R=[]
def add(c,ag,o,reason,resp=N): R.append({"claim":c,"agrees":ag,"outcome":o,"reason":reason,"response":resp})
add("dataset-size",True,"partially_reproduced",A)
add("fig1d-slow-oscillation",True,"reproduced","Agrees with the stated outcome. B.10 is resolved: the detrended spectrum was added.")
add("fig1e-decaying-rate",True,"reproduced",A)
add("fig2b-dimensions",True,"reproduced","Agrees with the stated outcome. B.1 is resolved, disclosed in cells 21 and 22 and in the Summary table. Cell 21 says the Methods' printed width (median ISI / 12, or / sqrt(12)) gives 22 to 76 dimensions; cell 20 gives 21 (sqrt12/le80) to 76, and the record's 21 to 76 is correct. Remaining: no single reading of width and count makes fig2b, fig3h, fig4c, fig6s2 and fig7gh all hold, and fig2b fails under the adopted reading; this is now disclosed, but every assumed outcome rests on it.",
    "Corrected cell 21 to 21 to 76 dimensions (21 to 41 with median ISI / sqrt(12), 33 to 76 with / 12). The absence of a consistent reading stays disclosed in the header, the recurrence section and the Summary; the adopted reading is kept, as the protocol puts the Methods' count first. Outcome kept.")
add("fig2ef-periodic-recurrence",True,"reproduced",A)
add("fig2e-single-dominant-orbit",True,"reproduced",A)
add("fig2s2-threshold-robust",True,"reproduced",A)
add("fig3a-coalescence",True,"not_reproduced","Agrees with the stated outcome. B.7 is resolved (windows now count at at least 90%), and the coalescence densities asked for were added.")
add("fig3c-same-manifold",True,"reproduced",A)
add("fig3s1a-common-axes",True,"reproduced",A)
add("fig3d-initial-conditions",True,"reproduced",A)
add("fig3f-pairwise-similarity",True,"reproduced",A)
add("fig3h-perturbations-return",True,"partially_reproduced","Accepts it. The criterion holds under own/le80 (18 kept and 16 returned; 19 and 17) and fails under the adopted reading (16 and 15), and the record says so. The criterion's text gives no partial outcome; strictly, under the adopted reading it gives not reproduced. Cell 53 and the notes say the code's rule keeps 17 to 21, which is true but leaves out that under the adopted reading the code's rule keeps 19 periods and 18 return (0.947, cell 52), which meets both tolerances and matches the paper's 19.",
    "Added to the conclusion and the notes that the code's rule under the adopted reading keeps 19 with 18 returned (0.947), meeting both tolerances, and that it is reported, not judged, because the criterion states the Methods' rule (\"We removed all such divergent periods whose divergent point fell within two oscillation cycles of the end of the recording\"). Added that the criterion has no partial outcome and why partially reproduced is kept (the fraction holds, the counts miss by 1.1 and 0.3). Outcome kept, as the verifier accepts it.")
add("fig3i-same-manifold-after",True,"reproduced","Agrees with the stated outcome. B.4 is resolved: the weak-evidence wording is now in fig3h and fig3i.")
add("fig4bc-stable-spiral",True,"reproduced" if False else "partially_reproduced","Agrees with the stated outcome. The neighbour counts asked for were added.")
add("fig4c-orbital-period",True,"reproduced","Now agrees. The criterion judges only the mean, 10 plus or minus 1 s, and says consistency is reported, not judged; under the adopted reading the mean is 10.45 s (cell 61). In round 1 it judged consistency, which the criterion does not ask for. Cell 62 and the notes say consistency holds only for the means (10.45 s against a median recurrence period of 12.73 s); the two differ by 2.3 s, more than twice the tolerance of 1 s, so the means are not shown consistent either. The record attached the round-1 B.11 toy-orbit note to fig4c as a reason, but B.11 was marked as not affecting a conclusion; the round-1 reasons were the le80 failure and the missing correlation.",
    "Corrected cell 62 and the notes: the means are 2.3 s apart where the tolerance is 1 s, so neither the correlation nor the means support \"consistent with\", which is reported, not judged. Removed the B.11 note from the round-1 reason for this claim. Outcome kept.")
add("fig4s1a-contracting-dimensions",True,"not_reproduced",A)
add("fig4s1b-rotation-dominant",True,"reproduced",A)
add("fig5b-period-changes",True,"reproduced",A)
add("fig5c-no-relation-contraction",True,"reproduced",A)
add("fig6s1-no-p10-motorneurons",True,"reproduced",A)
add("fig6d-decode-p10",False,"not_reproduced","The criterion requires mean forecast R minus 2 s.e.m. above 0 in each of the nine responses, and it has no partial rule; the paper's statement is specifically in all nine. Cell 79 shows preparation 4, bout 1 failing under all four readings, with histories up to 100 ms, and with the code's windowing (mean R -0.060 to -0.127), so the failure does not depend on the reading. Eight of nine is a failure of exactly what the claim says, not a partial match. In cells 79 and 83 (not discussed anywhere) the mean MAE for preparation 4, bout 1 reaches 7.6e6 with the code's windowing, which points to exploding forecasts in some windows.",
    "Agreed. In round 2 the outcome may not change, so the verified outcome, partially reproduced, is kept and not reproduced is proposed under proposed, with the reason. The conclusion now says so. Added a printout of the forecasts that diverge (above 10 times the largest P10 rate, up to the clip at about 1e13): many windows of the longer histories, none in the selected 80% models, and a perturbation test showing that a mean MAE with diverging windows depends on rounding (5.3e11 against 2.8e11 at 150 ms). In this run the code-windowing mean MAE of that response is 13.3 and its mean R -0.102; the pass counts are unchanged.")
add("fig6s2-dimensions-p10",True,"reproduced","Agrees. Under own/le80 the counts are 3 to 5 and the 90% counts at least double them; the 90% models are not better (MAE p = 0.91, R-squared p = 0.50, full history grid for both, cell 83). B.5 and B.6 are resolved. For preparation 4, bout 1 the mean MAE reaches 6.6e7 (90%, own/min80) and 3.1e9 (90%, own/le80), which points to exploding forecasts in some windows; it does not change the outcome, since the 90% models only look worse.",
    "Added the count of diverging forecasts for the 90% models (457 and 610 of 5760 windows over all histories under own/le80 and own/min80, one window in the selected models). The decoding is sensitive to rounding through these windows, and the re-run gives different numbers from the copy reviewed: under own/le80 MAE lower with 90% in 6 of 9, p = 0.50, R-squared p = 0.50; under own/min80 MAE p = 0.027, R-squared p = 0.16; pooled/le80 p = 0.73 and 0.82. The conclusion and notes now give these numbers and say so. No comparison finds the 90% models better, as before. Outcome kept.")
add("fig7a-long-tailed-participation",True,"reproduced",A)
add("fig7f-strongly-variable-neurons",True,"reproduced",A)
add("halving-participation",True,"reproduced",A)
add("fig7s1-rate-synchrony",True,"reproduced",A)
add("fig7gh-robust-to-participation",True,"partially_reproduced","Agrees, as in round 1. The result is split by reading: one slope of two is significant under own/min80, and under own/le80 with recurrent points, and none under either pooled reading (cell 100). The same strictness caveat as fig3h applies. The deviation says under the pooled readings the claim is reproduced; that is true with the legend's exclusion, the main reading, but with the code's exclusion pooled/min80 has a significant total-change slope with recurrent points (p = 0.028 and 0.029, cell 100), and this is not mentioned.",
    "Corrected the deviation, the notes and the conclusion: with the code's exclusion pooled/min80 has a significant total-change slope with the recurrent points (p = 0.028 and 0.029), pooled/le80 none. Outcome kept.")
add("fig7s2-no-invariant-core",True,"reproduced","Agrees. Cell 103 gives 0 or 1 of 10 preparations with a core, across both widths, both seeds and both participation readings. The outcome rests on a port of random clustering that was not checked against MATLAB, as the record says; it is stable across seeds and widths. The record's fig7s2 entry has no notebook or output fields, although cell 103 is tagged claim:fig7s2-no-invariant-core.",
    "Added the notebook and output fields. The port could not be checked against MATLAB output here, as no MATLAB run is available; this stays stated in the deviation. Outcome kept.")
add("fig8-caudolateral",True,"blocked",A)
v={"date":"2026-11-08","kind":"agent","by":"Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)",
   "reviewed":"Round 2. The full executed notebook of the first revision, with its conclusions and summary, the helper module, the attempt record and the claims file, with the paper. The verifier found no place where the claims file misreads the paper and agreed with 29 of the 30 outcomes. It also noted that the README gives about 36 minutes where the notebook printed 33.8 min (now about 39 minutes, from this run).",
   "results":R}
s=yaml.safe_dump([v],sort_keys=False,width=100,allow_unicode=True)
s="\n".join(l for l in s.splitlines())
open("attempts/crcns-apl-1-bruno-2017-01.yaml","a").write(s+"\n")
EOF
cd  && python $TMPDIR/v2.py && tail -30 attempts/crcns-apl-1-bruno-2017-01.yaml && python -c "import yaml;d=yaml.safe_load(open('attempts/crcns-apl-1-bruno-2017-01.yaml'));print(len(d['verifications']), len(d['verifications'][1]['results']))"
```

```
agrees: true
    outcome: reproduced
    reason: Agrees with the stated outcome; the Result sentences match the printed outputs.
    response: No change needed.
  - claim: fig7gh-robust-to-participation
    agrees: true
    outcome: partially_reproduced
    reason: 'Agrees, as in round 1. The result is split by reading: one slope of two is significant under
      own/min80, and under own/le80 with recurrent points, and none under either pooled reading (cell
      100). The same strictness caveat as fig3h applies. The deviation says under the pooled readings
      the claim is reproduced; that is true with the legend''s exclusion, the main reading, but with the
      code''s exclusion pooled/min80 has a significant total-change slope with recurrent points (p = 0.028
      and 0.029, cell 100), and this is not mentioned.'
    response: 'Corrected the deviation, the notes and the conclusion: with the code''s exclusion pooled/min80
      has a significant total-change slope with the recurrent points (p = 0.028 and 0.029), pooled/le80
      none. Outcome kept.'
  - claim: fig7s2-no-invariant-core
    agrees: true
    outcome: reproduced
    reason: Agrees. Cell 103 gives 0 or 1 of 10 preparations with a core, across both widths, both seeds
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "—\|rather" attempts/crcns-apl-1-bruno-2017-01.yaml entries/crcns-apl-1-bruno-2017/README.md entries/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb | head; python tools/entry.py check entries/crcns-apl-1-bruno-2017 2>&1 | tail -5; date -u
```

```
0 error(s)
Sun Nov  8 20:00:50 UTC 2026
```

**Agent**

The record and notebook are edited and the check passes. Running the entry a final time with the finished notebook.

**Agent calls Bash**

```bash
python tools/entry.py all entries/crcns-apl-1-bruno-2017 > $TMPDIR/run3.log 2>&1; echo exit $?; date -u; tail -3 $TMPDIR/run3.log
```

```
exit 0
Sun Nov  8 20:40:49 UTC 2026
Installed kernelspec registry-crcns-apl-1-bruno-2017 in executed/crcns-apl-1-bruno-2017/.venv/share/jupyter/kernels/registry-crcns-apl-1-bruno-2017
0 error(s)
pass  reproduce_bruno_2017.ipynb  (2387 s)
```

**Agent**

Checking that this run's numbers match the ones the text now cites.

**Agent calls Bash**

```bash
python - <<'EOF'
import nbformat
nb=nbformat.read('executed/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb',4)
want={52:["19                  18","0.938"],79:["-0.102","-0.124             -0.204","-0.075"],81:["195","770","5.270273e+11","2.825161e+11","1.325761e+01","457","610","6520.74"],
      84:["0.0273","0.4961            6          -0.4371 0.4961","0.7344","0.8203","0.1641","0.0195"],101:["0.0276","0.0292"],110:["min"]}
for i,ks in want.items():
    t="".join(o.get('text','') for o in nb.cells[i].outputs)
    print(i,[k in t for k in ks])
print([o['text'] for o in nb.cells[110].outputs if 'text' in o])
EOF
git status --short
```

```
52 [True, True]
79 [True, True, True]
81 [True, True, True, True, True, True, True, True]
84 [True, True, True, True, True, True]
101 [True, True]
110 [True]
['notebook run time 39.6 min; peak memory 2.45 GB (main process)\n']
 M attempts/crcns-apl-1-bruno-2017-01.yaml
 M entries/crcns-apl-1-bruno-2017/README.md
 M entries/crcns-apl-1-bruno-2017/apl.py
 M entries/crcns-apl-1-bruno-2017/entry.yaml
 M entries/crcns-apl-1-bruno-2017/reproduce_bruno_2017.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
sed -i 's/about 39 minutes on 4 CPUs/about 40 minutes on 4 CPUs/' entries/crcns-apl-1-bruno-2017/README.md; sed -i 's/runtime_minutes: 39/runtime_minutes: 40/' entries/crcns-apl-1-bruno-2017/entry.yaml; sed -i 's/(now about 39 minutes, from this run)/(now about 40 minutes, from this run, which printed 39.6 min)/' attempts/crcns-apl-1-bruno-2017-01.yaml; grep -n "39.6" attempts/crcns-apl-1-bruno-2017-01.yaml | head -2; python tools/entry.py check entries/crcns-apl-1-bruno-2017 2>&1 | tail -2
```

```
0 error(s)
```

**Agent calls Bash**

```bash
grep -n "now about" attempts/crcns-apl-1-bruno-2017-01.yaml
```

```
752:    the README gives about 36 minutes where the notebook printed 33.8 min (now about 39 minutes, from
```

**Agent calls Read**

```json
{
 "file_path": "attempts/crcns-apl-1-bruno-2017-01.yaml",
 "offset": 748,
 "limit": 6
}
```

```
748	  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
749	  reviewed: Round 2. The full executed notebook of the first revision, with its conclusions and summary,
750	    the helper module, the attempt record and the claims file, with the paper. The verifier found no place
751	    where the claims file misreads the paper and agreed with 29 of the 30 outcomes. It also noted that
752	    the README gives about 36 minutes where the notebook printed 33.8 min (now about 39 minutes, from
753	    this run).
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/crcns-apl-1-bruno-2017-01.yaml",
 "old_string": "(now about 39 minutes, from\n    this run).",
 "new_string": "(now about 40 minutes; this\n    revision's run printed 39.6 min)."
}
```

```
The file attempts/crcns-apl-1-bruno-2017-01.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/crcns-apl-1-bruno-2017 2>&1 | tail -1; date -u
```

```
0 error(s)
Sun Nov  8 20:41:29 UTC 2026
```

**Agent**

I've handled every point in the round-2 report, re-run the entry with `python tools/entry.py all` (it passes, 39.6 min), and recorded round 2 under `verifications`. Nothing is committed.

**Outcomes.** None changed, as round 2 requires.
- **fig6d-decode-p10:** I agree with the verifier that this should be not reproduced. The criterion and the paper both require all nine responses, and preparation 4, bout 1 fails under every reading, history range and windowing. The record keeps partially reproduced and adds a `proposed` change to `not_reproduced` with the reason, so a third verification round is needed for this one claim.
- **fig3h and fig7gh:** the verifier accepted partially reproduced for both, so both stay.

**Something new the re-run showed.** The P10 decoding gives different numbers on different runs.
- With longer histories, the forecasts blow up in many windows, up to about 1e13 spikes/s, the cap set by clipping the model's log-rate at 30.
- A mean of the per-window errors that includes those windows depends on tiny rounding differences. Nudging the inputs by one part in a billion halved one such mean, from 5.3e11 to 2.8e11.
- So the error figures, and the history picked from them, can shift. For preparation 4, bout 1, the verifier's copy had a mean error of 7.6e6 and this run gives 13.3. The fig6s2 test for own/le80 moved from p = 0.91 to 0.50.
- The conclusions hold in both runs: 8 of 9 responses pass for fig6d, and for fig6s2 the 90% models are never better.
- Runs on this machine repeat exactly: three runs gave identical numbers. If the workflow runs on other hardware, the decoding numbers may differ again.
- I added a notebook cell that counts these windows and runs the rounding test. The fig6d and fig6s2 conclusions and notes now use this run's numbers and say they are sensitive. `apl.py` only gained a stored maximum forecast per window; the fitting itself is unchanged.

**Other corrections:**
- **fig3h:** now states that the code's removal rule under the adopted reading keeps 19 periods with 18 returning, which meets the criterion. It is reported, not judged, because the criterion uses the Methods' rule, which I quote. It also says the criterion has no partial outcome and why partial is kept.
- **fig4c:** the "consistent with" sentence is fixed. The two means are 2.3 s apart against a 1 s tolerance, so neither the means nor the correlation support it.
- **fig7gh:** says that with the code's exclusion rule, pooled/min80 has a significant slope (p = 0.028 and 0.029).
- **Dimension ranges:** fixed in cells 21 and 22 and the Summary: 21 to 76 overall, 21 to 41 with / sqrt(12), 33 to 76 with / 12.
- **Small fixes:**
  - the fig7s2 record entry now has `notebook` and `output` fields;
  - the README runtime now says about 40 minutes;
  - the round-1 fig4c reason no longer cites the B.11 note the verifier had not given as a reason;
  - the README and Summary tables and the notebook header mention the proposed change.

**Not done:**
- No questions were added, since the verifier found no place where the claims file misreads the paper.
- The fig7s2 ensemble port still isn't checked against MATLAB, because MATLAB isn't available here; the record says so.
- I didn't make the decoding stable, for example by changing how the model is fitted. That would change the method in a round where outcomes are frozen, so I only reported the problem.

There are untracked dotfiles and folders in the repository root (`.bashrc`, `.idea`, `scripts` and others) that I didn't create; I left them alone.

## End of run

57 turns, 129 minutes, $2.75 at API prices, result: success.
