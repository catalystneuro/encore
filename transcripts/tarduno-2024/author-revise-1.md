# figshare-24639285 · author-revise-1 · run 40578691883

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/figshare-24639285/verifier-1-report.md; ls entries/figshare-24639285-tarduno-2024 entries/figshare-24639285-tarduno-2024/*
```

```
Tue Oct 27 20:34:13 UTC 2026
**Verifier report, round 1: Tarduno, Cottrell & Zhou 2024 (FIGSHARE:24639285 v1)**

The claims file has 17 claims. The notebook tests 16 and treats `interpretation-impact-no-dynamo` as blocked. I checked the archive through the Figshare API: version 1 is the only version, and its 16 files (13 xlsx, 3 pdf) have the same IDs and MD5s as notebook cell 1.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| glass-specimen-set | reproduced | Cell 8: 22 of 22 Table 2 glass specimens and 12 of 12 Table 1 crystals are present with step, moment, Dec and Inc. 10 glass specimens have AF steps, the same set as the Table 2 marks. Four of the glass sheets are not real replicate measurements (problem 1). |
| glass-success-rate | reproduced | Cell 10: 3/(3+22) = 12.0%. Without AF: 12+1 = 13; with AF: 10+2 = 12, which matches Methods paragraph 2. |
| table2-fit-statistics | partially_reproduced | Cells 12–13: n matches for all nine. With replicates averaged, 23 of 29 values match (79%), just under the 80% bar. The misses are ss10 MAD (33.3 vs 42.9), R2 for ss9, ss10 and ss34, and pTRM checks for ss19 at 250 °C and ss30 at 450 °C. Using only the first measurement gives 38%. Holding a single pTRM reading fixed gives about 66% (19/29), so the outcome is partial either way. |
| table2-no-fit | reproduced | Cell 16: 11 of 11 are irregular under reading (a) and 9 of 11 under (b). ss36 and ss39 grow away from the origin over their last step (1.77→6.00 and 2.31→9.67 ×1e-9 emu). Reading (b) passes exactly at the threshold, and 3 of its 9 are synthetic sheets (problem 1). |
| fig1-linear-components | reproduced | Cell 19, averaged replicates, free-line MAD: ss43 MAD 10.3 vs 10.0 and R2 0.902 vs 0.90; ss19 MAD 30.1 vs 30.1 and R2 0.956 vs 0.94. Nominal paleointensities are 9.6 and 23.0 µT (8.5 and 23.7 µT with first measurements). They cannot be compared with Figure 1 because the figure was not seen. |
| fig2-changing-field | reproduced | Cell 21, average
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -80; cat entries/figshare-24639285-tarduno-2024/entry.yaml; ls attempts* 2>/dev/null | head; git ls-files | grep -i 24639285
```

```
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
53:### 2. Read the paper's code
63:### 3. Write the claims file
148:### 4. Data from outside the paper's own recordings
156:### 5. Check
169:### 6. Answer questions
182:## Author
198:### 1. Establish what can be tested
325:### 2. Check the data against its description
340:### 3. Write the entry
398:### 4. Lock, check and run
409:### 5. Record the attempt
460:### 6. Hand over for verification
498:## Repeat attempts
540:## Local and remote datasets
563:## Verifier
567:### Round 1: without the author's conclusions
592:### Round 2: with the author's conclusions
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 182,200p docs/protocol.md; sed -n 398,500p docs/protocol.md; sed -n 590,640p docs/protocol.md
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
### 4. Lock, check and run
[... 125 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/figshare-24639285-tarduno-2024-01.yaml
```

```
schema_version: 2
id: figshare-24639285-tarduno-2024-01
dataset:
  archive: figshare
  id: "24639285"
  version: "1"
  doi: 10.6084/m9.figshare.24639285.v1
paper: doi:10.1038/s41597-024-03626-0
date: 2026-10-27
entry: figshare-24639285-tarduno-2024
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-12
  runner:
    platform: GitHub Actions
[... 307 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "example-14053g1" -A40 claims/figshare-24639285/*.yaml | head -60; ls questions/ | grep 2463; cat questions/figshare-24639285.yaml 2>/dev/null
```

```
Exit code 1
347:- id: example-14053g1-threshold
348-  statement: For crystal 14053g1, the threshold field detection limit computed from the
349-    magnetometer sensitivity (8e-14 A m2) and a TRM at 590 C of 8e-12 A m2 in a 20 uT field is
350-    0.2 uT.
351-  source: Technical Validation, Example of threshhold detection limit
352-  quote: Threshold field detection = Magnetometer sensitivity (8 × 10−14 A m2) / TRM590o (8 × 10−12
353-    A m2) × Lab Field (20 μT) = 0.2 μT
354-  expected:
355-  - quantity: 14053g1 TRM at 590 C in 20 uT
356-    value: 8.0e-12
357-    tolerance: 8.0e-13
358-    unit: A m2
359-  - quantity: 14053g1 threshold field
360-    value: 0.2
361-    tolerance: 0.02
362-    unit: uT
363-  criterion: The example conflicts with Table 1, which gives 14053g1 3.203E-09 emu and 0.51 uT.
364-    Readings (a) the example as written, for 14053g1; (b) a misprint of the crystal name, the
365-    numbers belonging to 12040g1 (8.002E-09 emu, 0.20 uT in Table 1). TRM computed as in
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "verifications:" attempts/*.yaml | head -3; f=$(grep -l "verifications:" attempts/*.yaml | head -1); sed -n '/^verifications:/,$p' $f | head -60; grep -n "verifications" -A40 schemas/*attempt* 2>/dev/null | head -80; ls schemas 2>/dev/null
```

```
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
    outcome: partially_reproduced
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024; python -c "
import json;nb=json.load(open('reproduce_tarduno_2024.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source']); print('=====',i,c['cell_type'],len(s)); print(s[:600])
"; wc -l apollo.py; grep -n "^def " apollo.py
```

```
===== 0 markdown 1880
# Replicate Apollo sample magnetizations (Tarduno, Cottrell & Zhou 2024) on Figshare 24639285

Paper: J. A. Tarduno, R. D. Cottrell, T. Zhou, "Dataset of replicate Apollo sample magnetizations
bearing on impacts and absence of a long-lived lunar dynamo", Scientific Data (2024),
doi:10.1038/s41597-024-03626-0.

Dataset: Figshare item 24639285, version 1, doi:10.6084/m9.figshare.24639285.v1. Version 1 is the
only published version (the API lists no other), and it is the one the paper cites (ref. 26) and the
claims file names, so it is pinned. The cell below prints the MD5 (`computed_md5`) of eve
===== 1 code 409
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import apollo as A

pd.set_option("display.width", 200)
pd.set_option("display.max_rows", 200)

[... 521 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls questions | head; f=$(ls questions/*.yaml | head -1); head -40 $f; grep -n "questions" docs/protocol.md | head; grep -n "no-alteration-recording-efficiency" -A25 claims/figshare-24639285/*.yaml | head -30
```

```
000005.yaml
000006.yaml
000008.yaml
000009.yaml
000010.yaml
000011.yaml
000013.yaml
000015.yaml
000019.yaml
000023.yaml
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
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls questions | grep -v "^0"; head -5 questions/$(ls questions | grep -v "^0" | head -1) 2>/dev/null; sed -n 300,324p docs/protocol.md; sed -n 169,181p docs/protocol.md
```

```
README.md
crcns-ret-1.yaml
dryad-4j0zpc8hz.yaml
dryad-tdz08kq5d.yaml
ebrains-q0fg-1x8.yaml
# Questions

`<dandiset>.yaml` holds an attempt's questions to a reader: places where the author or a verifier
believes the claims file misreads the paper (docs/protocol.md, "Author", step 1.6, and "Hand over for
verification"), and the reader's answers ("Reader", step 6), which say whether the claims file was
     methods it cites, the code it links and the field's standard practice.
     Record it as an assumption: a deviation that says what was assumed and
     why, and `assumed: true` on the outcome. The notebook still shows the
     result under every plausible reading, so that the outcome's dependence
     on the choice can be seen. The outcome stands, marked as resting on the
     assumption.
   - Only when there is no defensible basis for a choice, so that any choice
     would be arbitrary, is the claim blocked as `methods_underspecified`,
     with the result of every reading that was run.
   - In either case the question is for the paper's authors, not a reader,
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -12 questions/dryad-4j0zpc8hz.yaml; grep -n "figshare\|folder" questions/README.md | head
```

```
# Questions from attempt dryad-4j0zpc8hz-didion-gency-2024-01 (author, 2026-10-27) about the claims file
# claims/dryad-4j0zpc8hz/10.1093-plphys-kiad565.yaml, asked under docs/protocol.md, Author, step 1.6. The
# attempt runs every reading it can see and blocks, as methods_underspecified, the claims whose outcome
# depends on the answer.
dataset: DRYAD:4j0zpc8hz
paper: doi:10.1093/plphys/kiad565
questions:
- claim: fig4-beech-warming-none
  asked: 2026-10-27
  question: How is the square root taken for starch, sugar and Asat when some values are negative? The
    claims file names readings S1 (untransformed) and S2 (square root after adding the constant that
    brings the minimum to zero) only for negative increments, but the dataset also has negative starch
```

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024; python -c "
import json;nb=json.load(open('reproduce_tarduno_2024.ipynb'))
for i in (14,15,16,17,26,27,42,50,51,53,54):
  if i<len(nb['cells']): print('=====',i);print(''.join(nb['cells'][i]['source']))
"; sed -n 150,320p apollo.py
```

```
===== 14
T2 = {  # Table 2: n, T range, MAD, R2, pTRM checks {T: %}, failure criteria
    "ss19": (4, 175, 450, 30.1, 0.94, {250: 30, 450: 9}, "pTRM, MAD, n"),
    "ss43": (3, 250, 400, 10.0, 0.90, {250: 85}, "pTRM, n"),
    "ss22": (4, 250, 500, 35.4, 0.38, {250: 22, 450: 13}, "pTRM, MAD, R2"),
    "ss41": (3, 500, 580, 24.0, 0.38, {250: 4, 400: 24}, "pTRM, MAD, R2, n"),
    "ss6": (3, 175, 360, 21.0, 0.91, {}, "MAD, R2, n, no pTRM"),
    "ss9": (4, 250, 550, 37.6, 0.74, {250: 21}, "pTRM, MAD, R2"),
    "ss10": (3, 360, 550, 42.9, 0.15, {250: 83}, "pTRM, MAD, R2, n"),
    "ss30": (4, 175, 500, 12.5, 0.59, {450: 10}, "R2"),
    "ss34": (5, 100, 450, 12.1, 0.06, {250: 9}, "R2"),
}
TOL_MAD = {"ss19": 3.0, "ss43": 1.0, "ss22": 3.5, "ss41": 2.4, "ss6": 2.1, "ss9": 3.8, "ss10": 4.3, "ss30": 1.25, "ss34": 1.2}

def fit_stats(how):
    rows, checks = [], []
    for s, (n, t0, t1, mad, rr, pt, fail) in T2.items():
        df = glass[s]["data"]
        a = A.in_range(A.arai(df, how), t0, t1)
        m = A.mads(df, t0, t1, how)
[... 336 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed/ 2>/dev/null | head; python -c "import pandas, openpyxl, numpy; print('ok')"; grep -n "venv\|cache" tools/entry.py | head -20
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pandas, openpyxl, numpy; print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pandas'
323:    venv = (output_dir / ".venv").resolve()
324:    python = venv / "bin" / "python"
328:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", PYTHON_VERSION, str(venv)],
331:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
345:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
```

**Agent**

Let me run the entry once as it stands, to get the environment and a baseline executed copy.

**Agent calls Bash**

```bash
cd  time python tools/entry.py all entries/figshare-24639285-tarduno-2024 2>&1 | tail -15; ls executed/figshare-24639285-tarduno-2024/
```

```
Installed kernelspec registry-figshare-24639285-tarduno-2024 in executed/figshare-24639285-tarduno-2024/.venv/share/jupyter/kernels/registry-figshare-24639285-tarduno-2024
0 error(s)
pass  reproduce_tarduno_2024.ipynb  (26 s)

real	0m46.299s
user	0m30.045s
sys	0m1.909s
reproduce_tarduno_2024.ipynb
result.json
```

**Agent**

Baseline runs in 46 s. Now I'll prototype the outputs the verifier asked for.

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024; cat > $TMPDIR/proto.py <<'EOF'
import numpy as np, pandas as pd
import apollo as A
files, glass, crystals = A.load_all()
# per-step replicate scatter
def step_scatter(df, steps=None):
    rows=[]
    for step,g in df.groupby("step",sort=False):
        X=A.to_xyz(g.moment,g.dec,g.inc); m=X.mean(axis=0)
        ang=[A.angle(x,m) for x in X] if len(X)>1 else [np.nan]
        mom=np.linalg.norm(X,axis=1)
        rows.append({"step":step,"n":len(g),"mean moment":np.linalg.norm(m),"moment sd/mean":mom.std(ddof=1)/mom.mean() if len(X)>1 else np.nan,
          "max angle to mean":max(ang),"resultant/n":np.linalg.norm(m)/mom.mean()})
    return pd.DataFrame(rows)
for s in ("ss9","ss10","ss6"):
    print(s); print(step_scatter(glass[s]["data"]).round(3).to_string(index=False))
# two clusters
def two_clusters(X):
    u=X/np.linalg.norm(X,axis=1,keepdims=True)
    c=u@u.T; i,j=np.unravel_index(np.argmin(c),c.shape)
    lab=(u@u[j]>u@u[i]).astype(int)
    for _ in range(10):
        cen=[u[lab==k].sum(0) for k in (0,1)]
        cen=[x/np.linalg.norm(x) for x in cen]
        lab=(u@cen[1]>u@cen[0]).astype(int)
    sep=A.angle(cen[0],cen[1])
    within=max(max(A.angle(x,cen[k]) for x in u[lab==k]) for k in (0,1))
    return int((lab==0).sum()),int((lab==1).sum()),sep,within
out=[]
for s,v in glass.items():
    for step,g in v["data"].groupby("step",sort=False):
        if len(g)<4: continue
        n0,n1,sep,w=two_clusters(A.to_xyz(g.moment,g.dec,g.inc))
        if min(n0,n1)>=2 and sep>30 and w<sep/2:
            out.append((s,step,len(g),n0,n1,round(sep,1),round(w,1)))
print(out)
EOF
../../executed/figshare-24639285-tarduno-2024/.venv/bin/python $TMPDIR/proto.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/proto.py", line 2, in <module>
    import apollo as A
ModuleNotFoundError: No module named 'apollo'
```

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024; PYTHONPATH=. ../../executed/figshare-24639285-tarduno-2024/.venv/bin/python $TMPDIR/proto.py
```

```
ss9
 step  n  mean moment  moment sd/mean  max angle to mean  resultant/n
    0  5          0.0           0.002              0.145        1.000
  100  9          0.0           0.048              4.366        0.999
100.1 10          0.0           0.013              1.061        1.000
  175 10          0.0           0.088              6.324        0.997
175.1 10          0.0           0.011              0.523        1.000
  250  6          0.0           0.049             16.813        0.988
250.1  5          0.0           0.009              0.765        1.000
  360 11          0.0           0.087             56.939        0.954
360.1  5          0.0           0.006              0.498        1.000
  450 10          0.0           0.085              9.377        0.996
250.2  6          0.0           0.004              4.568        0.999
450.1 10          0.0           0.010              1.203        1.000
  550 13          0.0           0.103             30.054        0.969
550.1  6          0.0           0.006              0.583        1.000
ss10
 step  n  mean moment  moment sd/mean  max angle to mean  resultant/n
    0  5          0.0           0.010              0.759        1.000
  100 10          0.0           0.098             24.677        0.971
[... 24 more lines not kept]
```

**Agent**

Several glass steps besides ss6 250.1 show two direction clusters, some of them inside the Table 2 fit ranges. I'll write the new cells into the notebook.

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024; cat > $TMPDIR/edit.py <<'PYEOF'
import json
p="reproduce_tarduno_2024.ipynb"
nb=json.load(open(p))
def code(s): return {"cell_type":"code","metadata":{},"execution_count":None,"outputs":[],"source":s.strip("\n").splitlines(True)}
def md(s): return {"cell_type":"markdown","metadata":{},"source":s.strip("\n").splitlines(True)}
src=lambda i: "".join(nb["cells"][i]["source"])
assert src(16).startswith("# Failure criteria")
assert src(26).startswith('for how in ("mean", "first"):\n    for s in ("ss41"')
assert src(50).startswith("rows = []\nfor name in T1:")

A_cell = r'''
# Scatter of the repeated measurements of each step for the specimens whose MAD or R2 differ from
# Table 2 (ss9, ss10) and for ss6: moments in 1e-9 emu, the relative spread of the moments, the largest
# angle of a replicate from the step's mean direction, and the resultant length over n (1 when all agree)
def step_scatter(df):
    rows = []
    for step, g in df.groupby("step", sort=False):
        X = A.to_xyz(g.moment, g.dec, g.inc)
        m, mom = X.mean(axis=0), np.linalg.norm(X, axis=1)
        rows.append({"step": step, "n": len(g), "mean vector (1e-9 emu)": np.linalg.norm(m) * 1e9,
                     "moment sd/mean": mom.std(ddof=1) / mom.mean() if len(g) > 1 else np.nan,
                     "max angle to mean": max(A.angle(x, m) for x in X), "R/n": np.linalg.norm(X / mom[:, None], axis=0).sum() and
                     np.linalg.norm((X / mom[:, None]).sum(axis=0)) / len(g)})
    return pd.DataFrame(rows)

for s in ("ss9", "ss10", "ss6"):
    print(f"{s} (Table 2 range {T2[s][1]} to {T2[s][2]} C)")
    print(step_scatter(glass[s]["data"]).round(3).to_string(index=False))

# The score with one pTRM reading held fixed (MAD and R2 as above), and with ss6 counted as a miss
f, c = fits["mean"], chks["mean"]
base = int(f.MAD_ok_any.sum()) + int(f.R2_ok.sum())
for k in ("a_i", "a_ii", "b_i", "b_ii"):
    tot = base + int(c[f"ok_{k}"].sum())
    print(f"pTRM reading {k} fixed: {tot}/29 = {100 * tot / 29:.0f}%")
tot = base + int(c.ok_any.sum()) - int(f.set_index("specimen").loc["ss6", "R2_ok"])
print(f"ss6's R2 counted as a miss: {tot}/29 = {100 * tot / 29:.0f}%")
print("Synthetic sheets among the nine:", [s for s in T2 if s in ("g2", "ss8", "ss39", "ss48")] or "none, so the score is the same without them")
'''

B_cell = r'''
# Steps of the glass sheets whose repeated measurements fall in two groups of directions, like ss6
# 250.1. Each step with 4 or more rows is split in two by the angle to the two most distant rows
# (then 10 rounds of reassignment to the group means); listed when both groups have 2 or more rows,
# their means are more than 45 deg apart and every row is within a third of that angle of its group's mean.
def two_groups(X):
    u = X / np.linalg.norm(X, axis=1, keepdims=True)
    i, j = np.unravel_index(np.argmin(u @ u.T), (len(u), len(u)))
    lab = (u @ u[j] > u @ u[i]).astype(int)
    for _ in range(10):
        cen = [u[lab == k].sum(axis=0) for k in (0, 1)]
        lab = (u @ cen[1] / np.linalg.norm(cen[1]) > u @ cen[0] / np.linalg.norm(cen[0])).astype(int)
    sep = A.angle(cen[0], cen[1])
    within = max(A.angle(x, cen[k]) for k in (0, 1) for x in u[lab == k])
    return int((lab == 0).sum()), int((lab == 1).sum()), sep, within

rows = []
for n in TABLE2:
    s = SHEET[n]
    t0, t1 = (T2.get(n) or NOFIT[n])[1:3] if n in T2 or n in NOFIT else (None, None)
    for step, g in glass[s]["data"].groupby("step", sort=False):
        if len(g) < 4:
            continue
        n0, n1, sep, within = two_groups(A.to_xyz(g.moment, g.dec, g.inc))
        if min(n0, n1) >= 2 and sep > 45 and within < sep / 3:
            kind, t = A.step_kind(step)
            rows.append({"specimen": n, "step": step, "rows": len(g), "groups": f"{n0}+{n1}", "apart (deg)": round(sep, 1),
                         "largest spread in a group (deg)": round(within, 1), "synthetic sheet": n in SYNTH,
                         "in Table 2 range": t is not None and kind in ("off", "on") and t0 <= t <= t1})
print(pd.DataFrame(rows).to_string(index=False))
'''

C_cell = r'''
# Curvature of the NRM lost against TRM gained plots, which the criterion does not test. A circle is
# fit by least squares (Kasa's algebraic fit) to the points of each Table 2 range, with NRM and TRM
# gained divided by the NRM of the first point; curvature is 1 / radius, positive when the points
# sag below the line through the first and last point. With three points (ss41, ss43) the circle is
# exact. ss19 and ss43 are given for comparison.
def curvature(x, y):
    M = np.column_stack([x, y, np.ones_like(x)])
    a, b, c = np.linalg.lstsq(M, x ** 2 + y ** 2, rcond=None)[0]
    cx, cy = a / 2, b / 2
    r = np.sqrt(c + cx ** 2 + cy ** 2)
    mid = len(x) // 2
    chord_y = y[0] + (y[-1] - y[0]) * (x[mid] - x[0]) / (x[-1] - x[0])
    return np.sign(chord_y - y[mid]) / r

for s in ("ss41", "ss22", "ss43", "ss19"):
    a = A.in_range(A.arai(glass[s]["data"], "mean"), *T2[s][1:3])
    x, y = (a.trm / a.nrm.iloc[0]).to_numpy(), (a.nrm / a.nrm.iloc[0]).to_numpy()
    print(f"{s}: steps {list(a.t.astype(int))}, NRM {list(y.round(3))}, TRM gained {list(x.round(3))}, "
          f"curvature {curvature(x, y):.2f}, R2 {A.r2(a.trm, a.nrm):.3f}")

# How often readings (a) and (b) hold when there is no changing field: (1) directions drawn at random,
# (2) points along one line toward the origin with isotropic noise; n points as for ss41 (3) and ss22
# (4, with the starting NRM or AF vector: the sequence above has 4 and 5 vectors).
rng = np.random.default_rng(2201)
for npts in (4, 5):
    res = {"random": [], "noisy line": []}
    for _ in range(5000):
        R = rng.normal(size=(npts, 3)) * rng.uniform(0.3, 1, size=(npts, 1))
        d = rng.normal(size=3); d /= np.linalg.norm(d)
        L = np.linspace(1, 0.3, npts)[:, None] * d + rng.normal(scale=0.15, size=(npts, 3))
        for k, X in (("random", R), ("noisy line", L)):
            lf = A.mad_line(X)
            res[k].append((A.angle(X[0], X[-1]) > lf, A.mad_plane(X) < lf, lf))
    for k, v in res.items():
        v = np.array(v)
        print(f"{npts} vectors, {k}: (a) holds {100 * v[:, 0].mean():.0f}%, (b) {100 * v[:, 1].mean():.0f}%, "
              f"median line MAD {np.median(v[:, 2]):.1f} deg")
'''
D_extra = r'''

# The ratio without the factor of two, and the cutoff of 2 on it, which the claims file does not use
x = alt[alt.replicates == "i"].assign(**{"TRM40/TRM20": lambda d: (2 * d["TRM40/(2 TRM20)"]).round(2)})
print(x[["crystal", "TRM40/TRM20"]].to_string(index=False))
print(f"TRM40/TRM20 above 2: {list(x.crystal[x['TRM40/TRM20'] > 2])}")
# Scatter of the 590.0 replicate moments, against the 8e-11 emu threshold
sd = {n: np.linalg.norm(grp(n, "590"), axis=1) for n in T1}
print("590.0 replicate moments, 1e-11 emu (sd):", {n: (list((v * 1e11).round(1)), round(v.std(ddof=1) * 1e11, 1)) for n, v in sd.items()})
'''
nb["cells"][50]["source"] = (src(50) + D_extra).splitlines(True)
nb["cells"].insert(27, code(C_cell))
nb["cells"].insert(17, code(B_cell))
nb["cells"].insert(17, code(A_cell))
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
PYEOF
git diff --stat .; python $TMPDIR/edit.py; git diff --stat .
```

```
.../reproduce_tarduno_2024.ipynb                   | 127 ++++++++++++++++++++-
 1 file changed, 126 insertions(+), 1 deletion(-)
```

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024; python - <<'EOF'
import json
p="reproduce_tarduno_2024.ipynb"; nb=json.load(open(p))
c=nb["cells"]
s=lambda i:"".join(c[i]["source"])
A=s(17)
A=A.replace('''"max angle to mean": max(A.angle(x, m) for x in X), "R/n": np.linalg.norm(X / mom[:, None], axis=0).sum() and
                     np.linalg.norm((X / mom[:, None]).sum(axis=0)) / len(g)})''','''"max angle to mean": max(A.angle(x, m) for x in X),
                     "R/n": np.linalg.norm((X / mom[:, None]).sum(axis=0)) / len(g)})''')
c[17]["source"]=A.splitlines(True)
B=c.pop(18)
assert "two groups" in "".join(B["source"])
i=[k for k in range(len(c)) if s(k).startswith("# A null for the irregularity")][0]
c.insert(i+1,B)
for k in range(14,32): print(k, c[k]["cell_type"], s(k)[:70].replace("\n"," | "))
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
EOF
```

```
14 code T2 = {  # Table 2: n, T range, MAD, R2, pTRM checks {T: %}, failure cr
15 code def score(how): |     f, c = fits[how], chks[how] |     n_ok = (f.n == f.n
16 code # Failure criteria against the stated thresholds (n >= 4, pTRM within 
17 code # Scatter of the repeated measurements of each step for the specimens 
18 markdown **Result: partially reproduced, resting on the assumption that repeate
19 markdown ## table2-no-fit |  | > The other thirteen failed glass specimens (g2, ss8
20 code NOFIT = {"g2": (4, 100, 400, {}), "ss8": (5, 100, 450, {}), "s11": (6,
21 code # A null for the irregularity counts: how often 'irregular' arises fro
22 code # Steps of the glass sheets whose repeated measurements fall in two gr
23 markdown **Result: reproduced.** Under reading (a), all 11 specimens marked "no
24 markdown ## fig1-linear-components |  | > Glass subsamples ss43 and ss19, which fai
25 code for how in ("mean", "first"): |     f = fits[how].set_index("specimen") | 
26 markdown **Result: reproduced, resting on the averaging assumption.** With aver
27 markdown ## fig2-changing-field |  | > Glass subsamples ss41 and ss22 show field-of
28 code for how in ("mean", "first"): |     for s in ("ss41", "ss22"): |         t
29 code # Curvature of the NRM lost against TRM gained plots, which the criter
30 markdown **Result: reproduced, resting on the averaging assumption.** For both 
31 markdown ## glass-directions-not-random |  | > The field-off directions of the fail
```

**Agent calls Bash**

```bash
cd  python tools/entry.py all entries/figshare-24639285-tarduno-2024 2>&1 | tail -5; cd executed/figshare-24639285-tarduno-2024; python -c "
import json;nb=json.load(open('reproduce_tarduno_2024.ipynb'))
for i in (17,22,29,54):
  c=nb['cells'][i]; print('=====',i)
  for o in c.get('outputs',[]): print(o.get('text','') if isinstance(o.get('text'),str) else ''.join(o.get('text',o.get('traceback',''))))
"
```

```
/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-figshare-24639285-tarduno-2024 in executed/figshare-24639285-tarduno-2024/.venv/share/jupyter/kernels/registry-figshare-24639285-tarduno-2024
0 error(s)
pass  reproduce_tarduno_2024.ipynb  (26 s)
===== 17
ss9 (Table 2 range 250 to 550 C)
 step  n  mean vector (1e-9 emu)  moment sd/mean  max angle to mean   R/n
    0  5                 602.619           0.002              0.145 1.000
  100  9                   7.555           0.048              4.366 0.999
100.1 10                  57.861           0.013              1.061 1.000
  175 10                   5.459           0.088              6.324 0.998
175.1 10                  53.126           0.011              0.523 1.000
  250  6                   7.329           0.049             16.813 0.988
250.1  5                  56.712           0.009              0.765 1.000
  360 11                   4.344           0.087             56.939 0.951
360.1  5                  69.110           0.006              0.498 1.000
  450 10                   4.355           0.085              9.377 0.997
250.2  6                  65.502           0.004              4.568 0.999
450.1 10                  76.590           0.010              1.203 1.000
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024; python - <<'EOF'
import json
p="reproduce_tarduno_2024.ipynb"; nb=json.load(open(p))
c=nb["cells"][29]; s="".join(c["source"])
s=s.replace("NRM {list(y.round(3))}, TRM gained {list(x.round(3))}","NRM {y.round(3).tolist()}, TRM gained {x.round(3).tolist()}")
c["source"]=s.splitlines(True)
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
EOF
cd ../../executed/figshare-24639285-tarduno-2024; python -c "
import json;nb=json.load(open('reproduce_tarduno_2024.ipynb'))
for i in (53,):
  c=nb['cells'][i]; print('=====',i, ''.join(c['source'])[:50])
  for o in c.get('outputs',[]): print(''.join(o.get('text','')))
"
```

```
===== 53 rows = []
for name in T1:
    on, off, alt, on40 =
crystal replicates  590.3 - 590.0 moment (1e-11 emu)  a_moment_ok  a_dirs_inconsistent  TRM40/(2 TRM20)  b_ok  a_ok
12021g2          i                               5.9         True                 True            0.952  True  True
12021g2         ii                               5.7         True                 True            0.932  True  True
12021g3          i                              -7.9         True                 True            0.910  True  True
12021g3         ii                              -6.7         True                 True            0.865  True  True
12040g1          i                               7.3         True                 True            0.781  True  True
12040g1         ii                               7.8         True                 True            0.788  True  True
12040g2          i                              -2.7         True                 True            0.947  True  True
12040g2         ii                              -1.1         True                 True            0.927  True  True
12040g3          i                               2.7         True                 True            0.770  True  True
12040g3         ii                               1.0         True                 True            0.796  True  True
12053g1          i                               5.4         True                 True            1.174  True  True
12053g1         ii                               5.6         True                 True            1.141  True  True
12053g2          i                              -7.9         True                 True            1.028  True  True
12053g2         ii                              -5.6         True                 True            1.018  True  True
14053g1          i                              12.1        False                 True            0.935  True False
14053g1         ii                               9.8        False                 Tr
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024; python - <<'EOF'
import json
p="reproduce_tarduno_2024.ipynb"; nb=json.load(open(p))
c=nb["cells"][53]; s="".join(c["source"])
old='''sd = {n: np.linalg.norm(grp(n, "590"), axis=1) for n in T1}
print("590.0 replicate moments, 1e-11 emu (sd):", {n: (list((v * 1e11).round(1)), round(v.std(ddof=1) * 1e11, 1)) for n, v in sd.items()})'''
assert old in s
s=s.replace(old,'''mom = {n: np.linalg.norm(grp(n, "590"), axis=1) * 1e11 for n in T1}
print(pd.DataFrame([{"crystal": n, "590.0 moments (1e-11 emu)": v.round(1).tolist(), "sd": round(v.std(ddof=1), 1)}
                    for n, v in mom.items()]).to_string(index=False))''')
c["source"]=s.splitlines(True)
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
EOF
date -u
```

```
Tue Oct 27 20:38:16 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024; python -c "
import json;nb=json.load(open('reproduce_tarduno_2024.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source'])
  if c['cell_type']=='markdown' and ('Result' in s or 'Summary' in s or i==0): print('=====',i);print(s)
" | sed -n 1,400p; cat README.md
```

```
===== 0
# Replicate Apollo sample magnetizations (Tarduno, Cottrell & Zhou 2024) on Figshare 24639285

Paper: J. A. Tarduno, R. D. Cottrell, T. Zhou, "Dataset of replicate Apollo sample magnetizations
bearing on impacts and absence of a long-lived lunar dynamo", Scientific Data (2024),
doi:10.1038/s41597-024-03626-0.

Dataset: Figshare item 24639285, version 1, doi:10.6084/m9.figshare.24639285.v1. Version 1 is the
only published version (the API lists no other), and it is the one the paper cites (ref. 26) and the
claims file names, so it is pinned. The cell below prints the MD5 (`computed_md5`) of every file read.
The files are streamed from Figshare's download service into memory; nothing is written to disk.

Claims: `claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml`, written from the version of
record (Europe PMC PMC11271266, full text with Methods, Technical Validation, figure legends and
Tables 1 and 2; the paper has no supplement and no PDF was supplied).

| Claim | Tested here |
|---|---|
| glass-specimen-set (link) | tested |
| glass-success-rate | tested |
[... 185 more lines not kept]
```

**Agent**

I'm changing example-14053g1-threshold to partially reproduced, as the verifier suggested. Next I'll update the conclusion cells, the summary and the README.

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024; python - <<'EOF'
import json
p="reproduce_tarduno_2024.ipynb"; nb=json.load(open(p))
C=nb["cells"]
def rep(i, old, new):
    s="".join(C[i]["source"]); assert old in s, (i, old); C[i]["source"]=s.replace(old,new).splitlines(True)
rep(18, """rows), which lowers its R2 under the mean.""", """rows), which lowers its R2 under the mean; counted as a miss, the score is 22 of 29 (76%). Holding one pTRM
reading fixed gives 14 to 19 of 29 (48 to 66%), so the outcome is partial or lower under any single
pTRM definition, and none of the nine is a synthetic sheet. The replicate tables above show where
ss9 and ss10 differ: ss10's steps from 100 to 360 C and at 450 and 550 C scatter by 20 to 113 deg
within a step (resultant over n 0.80 to 0.97), and ss9's 360 and 550 C steps by 57 and 30 deg, so
how such steps are combined moves its MAD and R2. Eleven steps of nine sheets, eight of them inside
the specimen's Table 2 range, hold two groups of directions more than 45 deg apart, as ss6's 250.1
does (table in table2-no-fit); averaging such a step gives a vector without physical meaning.""")
rep(30, """With first measurements ss41's R2
is 0.16.""", """With first measurements ss41's R2
is 0.16 and ss22's 0.44, outside the tolerance. Both readings are weak tests: for sequences of 4 and 5
vectors with no changing field, reading (a) holds for 93 to 96% of random directions and 61 to 66%
of points along one line with noise (median line MAD 24 to 27 deg, near those of ss41 and ss22), and
reading (b) for 51 to 57%. The "curved" part of the statement is not in the criterion. The circle
fit gives curvature -0.41 for ss41 and -1.12 for ss22, but -2.59 for ss19 and 0.67 for ss43, which
the paper presents as linear, so with 3 or 4 points it does not separate these specimens; ss22's NRM
does not fall monotonically over its range (1.00, 0.65, 0.82, 0.28).""")
rep(45, """**Result: reproduced under the misprint reading (b).** For 14053g1 the data give a TRM of 3.2e-12 A m2
and 0.50 uT, not the example's numbers; for 12040g1 they give 8.0e-12 A m2 and 0.200 uT, the example's
numbers. The example's crystal name is a misprint for 12040g1.""", """**Result: partially reproduced.** As written, for 14053g1, the example does not match: the data give
a TRM of 3.2e-12 A m2 and 0.50 uT. Under the misprint reading (b) it matches: 12040g1 gives 8.0e-12
A m2 and 0.200 uT, the example's numbers. The criterion calls the claim reproduced as written only
when reading (a) matches, so a match under (b) alone is recorded as partial: the calculation holds,
for a crystal other than the one named.""")
rep(54, """above the 8e-11 emu allowance.""", """above the 8e-11 emu allowance. The cutoff is loose: without the factor of two, TRM40/TRM20 is 1.54
to 2.35, and three crystals (12053g1 2.35, 14053g3 2.08, 12053g2 2.06) are above 2, so a cutoff of 2
on that ratio would fail them and no reading would pass every crystal. The paper's own words are
"apparent recording efficiencies >> 100%", and the largest here is 117% of linear recording, so the
substance holds; the cutoff is asked of a reader (questions/figshare-24639285.yaml). The 590.0
replicate moments of a crystal differ by 0.6e-11 to 6.3e-11 emu (sd), but their size, 1.0e-10 to
6.0e-10 emu with random directions, is the level a null state reaches here, several times the 8e-11
emu threshold, which reading (a) uses as its allowance.""")
rep(56, "| example-14053g1-threshold | reproduced under the misprint reading |", "| example-14053g1-threshold | partially reproduced (matches only as a misprint for 12040g1) |")
rep(56, """- The number of repeated measurements varies from 2 to 19 per step, ss6's 250.1 step holds two groups
  of directions, and the deposit does not say how repeated measurements were combined.""", """- The number of repeated measurements varies from 2 to 19 per step, eleven steps of nine sheets
  (ss6's 250.1 among them) hold two groups of directions more than 45 deg apart, and the deposit does
  not say how repeated measurements were combined.""")
rep(56, """- The crystals' 590 C zero-field moments are all above the 8e-11 emu threshold the paper uses.""", """- The crystals' 590 C zero-field moments are all above the 8e-11 emu threshold the paper uses, so
  the Table 1 maximum intensities rest on a threshold below the level the null state reaches.""")
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
EOF
python - <<'EOF'
p="README.md"; s=open(p).read()
s=s.replace("| Technical Validation example for 14053g1 | Reproduced under the misprint reading (the numbers are 12040g1's) |","| Technical Validation example for 14053g1 | Partially reproduced (the numbers are 12040g1's) |")
open(p,"w").write(s)
EOF
grep -n "Partially reproduced (the" README.md
```

```
21:| Technical Validation example for 14053g1 | Partially reproduced (the numbers are 12040g1's) |
```

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024; python - <<'EOF'
import json
p="reproduce_tarduno_2024.ipynb"; nb=json.load(open(p))
C=nb["cells"]
def rep(i, old, new):
    s="".join(C[i]["source"]); assert old in s, (i, old); C[i]["source"]=s.replace(old,new).splitlines(True)
rep(18, """ss10's steps from 100 to 360 C and at 450 and 550 C scatter by 20 to 113 deg
within a step (resultant over n 0.80 to 0.97)""", """all of ss10's field-off steps and its 100, 175 and 250 C field-on steps
scatter by 20 to 113 deg within a step (resultant over n 0.79 to 0.98)""")
rep(18, """Eleven steps of nine sheets, eight of them inside
the specimen's Table 2 range,""", """Eleven steps of seven sheets, nine of them inside
the specimen's Table 2 range,""")
rep(56, "eleven steps of nine sheets", "eleven steps of seven sheets")
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
EOF
```

```
(Bash completed with no output)
```

**Agent**

Now the question for a reader about the no-alteration cutoff.

**Agent calls Bash**

```bash
cd  sed -n 1,30p questions/README.md; sed -n 12,40p questions/dryad-4j0zpc8hz.yaml
```

```
# Questions

`<dandiset>.yaml` holds an attempt's questions to a reader: places where the author or a verifier
believes the claims file misreads the paper (docs/protocol.md, "Author", step 1.6, and "Hand over for
verification"), and the reader's answers ("Reader", step 6), which say whether the claims file was
amended and why. Each question has `claim`, `question`, `passage`, `why` (how the misreading could
change the outcome), and, once answered, `answer` and `answered` (a date). Method details the claims
file lacks are not asked here: the author takes them from the paper, and a detail the paper does not
settle is a question for the paper's authors, recorded in the claim's notes and as a
`methods_unavailable` finding in the attempt. Files from before protocol `pilot-11` also hold
questions about method details, asked under the earlier rule.
    brings the minimum to zero) only for negative increments, but the dataset also has negative starch
    (77 tree-campaign rows), sugar (3) and Asat (5) values, and Table S1 marks starch, sugar and Asat as
    square-root transformed. Tested here with S1 and S2 applied to these three traits as well. The same
    question applies to every claim that uses the treatment or interaction test on starch, sugar or Asat
    (disc-oak-warming-no-carbon-change, fig4-beech-mr, fig4-oak-mr, fig4-beech-wmr, fig4-oak-wmr,
    fig4-wmr-same-as-mr, disc-nsc-unchanged-drier-soil, tables6-no-seasonal-variation and the claims on
    Supplemental Table S3).
  passage: Supplemental Tables S1 and S3, the footnote to the starred traits, "square root transformation
    has been used."
[... 20 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "questions/figshare-24639285.yaml",
 "content": "# Questions from attempt figshare-24639285-tarduno-2024-01 (author, revision after verifier round 1,\n# 2026-10-27) about the claims file claims/figshare-24639285/10.1038-s41597-024-03626-0.yaml, asked\n# under docs/protocol.md, \"Hand over for verification\". The claim is tested as the file has it.\ndataset: FIGSHARE:24639285\npaper: doi:10.1038/s41597-024-03626-0\nquestions:\n- claim: no-alteration-recording-efficiency\n  asked: 2026-10-27\n  question: Reading (b) says the 590.4 TRM (40 uT) should be \"no more than about twice\" the 590.1 TRM\n    (20 uT), but its cutoff fails a crystal only when the ratio of the 590.4 TRM to twice the 590.1\n    TRM is above 2, that is when the 40 uT TRM exceeds four times the 20 uT TRM. Is the cutoff meant\n    to be on TRM40/TRM20 (fail above 2, matching \"about twice\") or on TRM40/(2 TRM20) as written?\n    The verifier of round 1 raised this.\n  passage: If alteration had resulted in the formation of new magnetic minerals, apparent recording\n    efficiencies ≫ 100% should have be observed (but these were not), and alteration checks should\n    fail (Background & Summary, paragraph 5).\n  why: TRM40/TRM20 is 1.54 to 2.35 over the twelve crystals, and three (12053g1 2.35, 14053g3 2.08,\n    12053g2 2.06) are above 2. With a cutoff of 2 on TRM40/TRM20 reading (b) would fail three crystals\n    and reading (a) fails one or two, so the claim would not pass under either reading. As written,\n    TRM40/(2 TRM20) is 0.77 to 1.17 and every crystal passes, so the claim is reproduced.\n"
}
```

```
File created successfully at: questions/figshare-24639285.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/entry.py all entries/figshare-24639285-tarduno-2024 2>&1 | tail -3; cd executed/figshare-24639285-tarduno-2024; python -c "
import json;nb=json.load(open('reproduce_tarduno_2024.ipynb'))
for i in (17,22,29,53):
  c=nb['cells'][i]; print('=====',i)
  for o in c.get('outputs',[]): print(''.join(o.get('text',''))[-1500:])
"
```

```
Installed kernelspec registry-figshare-24639285-tarduno-2024 in executed/figshare-24639285-tarduno-2024/.venv/share/jupyter/kernels/registry-figshare-24639285-tarduno-2024
0 error(s)
pass  reproduce_tarduno_2024.ipynb  (25 s)
===== 17
       52.591 0.821
360.1  5                   5.667           0.013              6.620 0.998
  450 11                   2.224           0.244             40.129 0.958
250.2  4                   5.937           0.063              5.713 0.997
450.1  6                   3.434           0.107             16.788 0.979
  550 11                   2.119           0.095             71.053 0.915
550.1  5                  10.878           0.045              0.719 1.000
ss6 (Table 2 range 175 to 360 C)
 step  n  mean vector (1e-9 emu)  moment sd/mean  max angle to mean   R/n
    0  9                 107.032           0.003              0.428 1.000
  100 10                   5.688           0.043             12.238 0.993
100.1 10                  10.719           0.031              3.181 0.999
  175 10                   4.130           0.050             16.460 0.994
175.1 10                  10.893           0.038              3.739 0.999
  250 10                   3.996           0.053             12.337 0.988
250.1 19                  10.912           0.027             47.492 0.738
[... 70 more lines not kept]
```

**Agent**

Outputs check out against the text. Now the attempt record.

**Agent calls Bash**

```bash
cd  sed -n 370,420p schemas/attempt.schema.json
```

```
"claim": {
                  "type": "string"
                },
                "agrees": {
                  "type": "boolean"
                },
                "reason": {
                  "description": "The verifier's reason, in its own words.",
                  "type": "string"
                },
                "response": {
                  "description": "What the author changed or replied, kept apart from the verifier's reason.",
                  "type": "string"
                },
                "outcome": {
                  "description": "The outcome the verifier would give.",
                  "enum": [
                    "reproduced",
                    "partially_reproduced",
                    "not_reproduced",
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p="attempts/figshare-24639285-tarduno-2024-01.yaml"; s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1, old; s=s.replace(old,new)
rep("""    failure "R2" says; ss6 has R2 0.89 here, so its listed R2 failure follows here.
""","""    failure "R2" says; ss6 has R2 0.89 here, so its listed R2 failure follows here. Counting ss6's R2
    as a miss, since its 250.1 step averages two groups of directions, gives 22 of 29 (76%). With one
    pTRM reading held fixed the score is 17, 16, 19 and 14 of 29 (readings a_i, a_ii, b_i, b_ii; 48
    to 66%), partial or lower under every fixed reading. None of the nine is a synthetic sheet. Within
    a step, ss10's field-off steps and its 100, 175 and 250 C field-on steps scatter by 20 to 113 deg
    (resultant over n 0.79 to 0.98), and ss9's 360 and 550 C steps by 57 and 30 deg, so how these
    steps are combined moves the MAD and R2 that miss.
""")
rep("""  - ss6's 250.1 step holds 19 rows in two groups of directions (inclination near 71 and near -13
    deg); all are averaged, as for every step.
""","""  - ss6's 250.1 step holds 19 rows in two groups of directions (inclination near 71 and near -13
    deg); all are averaged, as for every step. Ten other steps of six glass sheets also hold two groups
    of directions more than 45 deg apart (s11 360.1, 550 and 550.1, ss10 250 and 360, ss18 100, ss24
    NRM and 550, ss29 175.1, ss36 450.1) and are averaged the same way.
""")
rep("""    Both readings hold for both specimens, also with first measurements. R2 is 0.384 and 0.378
    (0.38 plus or minus 0.038); with first measurements it is 0.16 and 0.44, outside tolerance.
""","""    Both readings hold for both specimens, also with first measurements. R2 is 0.384 and 0.378
    (0.38 plus or minus 0.038); with first measurements it is 0.16 and 0.44, outside tolerance. Both
    readings are weak tests. For sequences of 4 and 5 vectors with no changing field, reading (a)
    holds for 93 to 96% of random directions and 61 to 66% of points along one line with noise (median
    line MAD 24 to 27 deg), and reading (b) for 51 to 57%. The curved Arai plot in the statement is
    not in the criterion and is not judged. A circle fit to the normalized points gives curvature
    -0.41 for ss41 and -1.12 for ss22, against -2.59 for ss19 and 0.67 for ss43, which the paper
    shows as linear, so with 3 or 4 points it does not separate them; ss22's NRM does not fall
    monotonically over its range (1.00, 0.65, 0.82, 0.28 of the first).
""")
rep("""- claim: example-14053g1-threshold
  outcome: reproduced
""","""- claim: example-14053g1-threshold
  outcome: partially_reproduced
""")
rep("""  notes: Matches under reading (b) only, the misprint reading the criterion names. For 14053g1 the
    data give a TRM at 590 C of 3.203e-12 A m2 and 0.500 uT, not the example's 8e-12 and 0.2; for
    12040g1 they give 8.002e-12 A m2 and 0.200 uT, the example's numbers. The values recorded are
    12040g1's.
""","""  notes: Matches under reading (b) only, the misprint reading the criterion names. For 14053g1 the
    data give a TRM at 590 C of 3.203e-12 A m2 and 0.500 uT, not the example's 8e-12 and 0.2; for
    12040g1 they give 8.002e-12 A m2 and 0.200 uT, the example's numbers. The values recorded are
    12040g1's. The criterion calls the claim reproduced as written only when reading (a) matches, so
    a match under (b) alone is recorded as partially reproduced (changed from reproduced after
    verifier round 1).
""")
rep("""  - The cutoff of 2 on the ratio is the claims file's, not the paper's; the largest ratio, 1.17, is
    far from it.
""","""  - The cutoff of 2 on the ratio is the claims file's, not the paper's; the largest ratio, 1.17, is
    far from it. The cutoff fails a crystal only when the 40 uT TRM exceeds four times the 20 uT TRM,
    although the criterion's text says "about twice". Without the factor of two, TRM40/TRM20 is 1.54
    to 2.35 and three crystals are above 2 (12053g1 2.35, 14053g3 2.08, 12053g2 2.06), so a cutoff
    of 2 on that ratio would fail reading (b) for them and no reading would pass every crystal. This
    is asked of a reader in questions/figshare-24639285.yaml; the claim is tested as the file has it.
""")
rep("""    reading (a) 11 of 12 pass with first replicates and 10 of 12 with means; 14053g1's 590.3 moment
    exceeds its 590.0 moment by 9.8e-11 to 1.21e-10 emu, and 14053g3's by 9.9e-11 with means.
""","""    reading (a) 11 of 12 pass with first replicates and 10 of 12 with means; 14053g1's 590.3 moment
    exceeds its 590.0 moment by 9.8e-11 to 1.21e-10 emu, and 14053g3's by 9.9e-11 with means. The
    paper's words are recording efficiencies far above 100%; the largest here is 117% of linear
    recording. Reading (a)'s allowance of 8e-11 emu is below the level of the null state, 590.0
    moments of 1.0e-10 to 6.0e-10 emu with random directions, though the 590.0 replicates of one
    crystal differ in moment by only 0.6e-11 to 6.3e-11 emu (sd).
""")
rep("""    reproduces most of Table 2; the first measurement does not. Sheet ss6's 250.1 step holds 19 rows
    in two groups of directions (inclination near 71 deg and near -13 deg). NRM is labelled both 0
    and 0.0 in ss27 and ss38.""","""    reproduces most of Table 2; the first measurement does not. Eleven steps of seven glass sheets
    hold two groups of directions more than 45 deg apart, nine of them inside the specimen's Table 2
    range; sheet ss6's 250.1 step holds 19 rows in two groups (inclination near 71 deg and near -13
    deg). NRM is labelled both 0 and 0.0 in ss27 and ss38.""")
open(p,"w").write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  cat >> attempts/figshare-24639285-tarduno-2024-01.yaml <<'EOF'
verifications:
- date: '2026-10-27'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the
    helper module and the claims file, with the paper. The verifier checked the archive through the
    Figshare API and tested the helper functions on synthetic inputs. Its report gave its own outcome
    for each claim; 16 of 17 agree with the record, and example-14053g1-threshold does not.
  results:
  - claim: glass-specimen-set
    agrees: true
    outcome: reproduced
    reason: 22 of 22 Table 2 glass specimens and 12 of 12 Table 1 crystals are present with step,
      moment, Dec and Inc. 10 glass specimens have AF steps, the same set as the Table 2 marks. In g2,
      ss8, ss39 and ss48 every step's replicates are one row multiplied by factors of 0.95 to 1.03, so
      the deposit does not hold real replicate measurements for 4 of the 22 glass specimens; that
      should be reported alongside glass-specimen-set (problem 1).
    response: No change needed; the notes and the result cell already report the four synthetic sheets,
      and a finding describes them.
  - claim: glass-success-rate
    agrees: true
    outcome: reproduced
    reason: 3/(3+22) = 12.0%. Without AF 12+1 = 13; with AF 10+2 = 12, which matches Methods paragraph 2.
    response: No change needed.
  - claim: table2-fit-statistics
    agrees: true
    outcome: partially_reproduced
    reason: n matches for all nine. With replicates averaged, 23 of 29 values match (79%), just under
      the 80% bar. Using only the first measurement gives 38%. Holding a single pTRM reading fixed gives
      about 66% (19/29), so the outcome is partial either way. Averaging replicates is an assumption the
      data support (problem 2). ss6 step 250.1 has 19 rows in two direction clusters whose mean has no
      physical meaning; counting it as a miss gives 22/29 (76%), still partial (problem 3). Matching pTRM
      checks on any one of four readings is permissive; no single reading matches more than 5 of 11
      (problem 8). It asked for per-step replicate tables for ss9, ss10 and ss6, the score with a fixed
      pTRM reading and without the synthetic sheets, and a check for other two-cluster steps.
    response: Added the per-step replicate scatter of ss9, ss10 and ss6, the score under each fixed pTRM
      reading (14 to 19 of 29), the score with ss6 counted as a miss (22 of 29) and a note that none of
      the nine is a synthetic sheet. Added a scan of all glass steps for two groups of directions; eleven
      steps of seven sheets have them, nine inside a Table 2 range. Recorded in the notes, the deviation
      and a finding. Outcome kept.
  - claim: table2-no-fit
    agrees: true
    outcome: reproduced
    reason: 11 of 11 are irregular under reading (a) and 9 of 11 under (b). ss36 and ss39 grow away from
      the origin over their last step. Reading (b) passes exactly at the threshold, and 3 of its 9 are
      synthetic sheets. ss39 is one of the two specimens the trend out of origin condition depends on.
    response: No change needed; the counts without the synthetic sheets were already in the notes.
  - claim: fig1-linear-components
    agrees: true
    outcome: reproduced
    reason: Averaged replicates, free-line MAD; ss43 MAD 10.3 vs 10.0 and R2 0.902 vs 0.90; ss19 MAD
      30.1 vs 30.1 and R2 0.956 vs 0.94. The nominal paleointensities cannot be compared with Figure 1
      because the figure was not seen. With first measurements ss43 R2 is 0.99, outside tolerance.
    response: No change needed.
  - claim: fig2-changing-field
    agrees: true
    outcome: reproduced
    reason: Both specimens pass readings (a) and (b), and R2 is 0.384 and 0.378 against 0.38. Both
      readings are weak tests; random 3-point sets pass reading (b) 58% of the time and a single noisy
      line passes (a) 38% and (b) 30% of the time (problem 6). The curved Arai plot part of the statement
      is not tested. It asked for an Arai-curvature measure for ss41 and ss22.
    response: Added the rates at which readings (a) and (b) hold with no changing field (a 61 to 96%,
      b 51 to 57%, for random directions and a noisy line), and a circle-fit curvature for ss41 and
      ss22 with ss19 and ss43 for comparison; it does not separate them with 3 or 4 points. Recorded in
      the notes and the result cell. Outcome kept, as the criterion is met.
  - claim: glass-directions-not-random
    agrees: true
    outcome: partially_reproduced
    reason: 8 of 22 specimens reject randomness with averaged replicates and 9 of 22 with first
      measurements; inside the Table 2 ranges 8 and 7 of 22. Every count falls in the claim's
      quarter-to-half band. Dropping the synthetic sheets gives 7/18.
    response: No change needed.
  - claim: glass-af-no-change
    agrees: true
    outcome: reproduced
    reason: 8 of 10 show no significant change under readings (a) and (b), which is the allowed maximum
      of two exceptions. The exceptions are ss38 (moment ratio 0.49) and ss48, a synthetic sheet.
    response: No change needed.
  - claim: table1-max-intensity
    agrees: true
    outcome: reproduced
    reason: 24 of 24 values match under readings a_ii, b_i and b_ii. Table 1's M590 equals the plain
      magnitude of the 590.1 measurement; the Methods define TRM as the field-on minus field-off vector,
      a discrepancy in the paper that the claims file's reading (b) covers (problem 4). The 8e-11 emu
      threshold is well below the measurement noise, so the max intensity values understate what the
      data can exclude (problem 5).
    response: Added the 590.0 replicate moments of each crystal to the no-alteration cell; the
      summary and the finding on the 590 C moments now say the threshold is below the level the null
      state reaches. Outcome kept, as the criterion is arithmetic on the stated threshold.
  - claim: baseline-range
    agrees: true
    outcome: reproduced
    reason: The values run from 0.200 uT (12040g1) to 0.500 uT (14053g1), inside 0.18 to 0.22 and 0.45
      to 0.55.
    response: No change needed.
  - claim: example-14053g1-threshold
    agrees: false
    outcome: partially_reproduced
    reason: For 14053g1 the TRM is 3.2e-12 A m2 and the threshold 0.50 uT, so the example as written
      fails. For 12040g1 the numbers are 8.0e-12 A m2 and 0.20 uT, so it matches only if the crystal
      name is a misprint.
    response: Outcome changed to partially_reproduced. The criterion calls the claim reproduced as
      written only when reading (a) matches; a match under the misprint reading alone is a match in
      part. Notes, result cell, summary and README updated.
  - claim: fig3-nrm-consistent
    agrees: true
    outcome: reproduced
    reason: NRM replicates are consistent for 10 of 12 crystals under reading (a) and 8 of 12 under (b),
      including 12040g1 and 14053g2. Most crystals have only n = 2 NRM measurements.
    response: No change needed.
  - claim: fig3-590-inconsistent
    agrees: true
    outcome: reproduced
    reason: 590.0 replicates are inconsistent for 12 of 12 under reading (b) and 10 of 12 under (a),
      including both named crystals.
    response: No change needed.
  - claim: fig3-alteration-check-inconsistent
    agrees: true
    outcome: reproduced
    reason: 590.3 replicates are inconsistent for 12 of 12 under reading (b).
    response: No change needed.
  - claim: crystal-14053g1-400c-stable
    agrees: true
    outcome: reproduced
    reason: The three 400 C replicates give k 78 and Watson p 0.0003; 590.0 gives k 1.0 and p 0.785.
      Reading (a) holds. Reading (b) fails (9.3 deg from the NRM mean against an alpha95 of 4 deg), but
      the criterion needs only one.
    response: No change needed.
  - claim: no-alteration-recording-efficiency
    agrees: true
    outcome: reproduced
    reason: All 12 pass reading (b), with TRM40/(2 TRM20) between 0.77 and 1.17. Reading (a) passes only
      11 of 12 or 10 of 12. The claims file's reading (b) fails only when TRM40 exceeds 4 x TRM20,
      although its own text says no more than about twice; under a cutoff of TRM40/TRM20 above 2, three
      crystals would fail (12053g1 2.35, 14053g3 2.08, 12053g2 2.06) and no reading would pass every
      crystal. The paper's claim is far above 100%, and the largest apparent efficiency here is 117%,
      so the substance holds (problem 7). Reading (a) compares moment differences with 8e-11 emu, below
      the replicate scatter (problem 5). It asked for TRM40/TRM20 without the factor of 2.
    response: Added TRM40/TRM20 without the factor of two and the 590.0 replicate moments. The cutoff
      is asked of a reader in questions/figshare-24639285.yaml; the claim is tested as the file has it.
      Notes, deviation and result cell updated. Outcome kept.
  - claim: interpretation-impact-no-dynamo
    agrees: true
    outcome: blocked
    reason: The claims file marks it as an interpretation resting on ref. 1 and impact-plasma models.
      Nothing in the deposit can test it beyond the four claims it depends on.
    response: No change needed.
EOF
python tools/entry.py check entries/figshare-24639285-tarduno-2024 2>&1 | tail -5; date -u
```

```
/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
0 error(s)
Tue Oct 27 20:40:58 UTC 2026
```

**Agent**

The check passes, but the new notebook cells have no ids. I'll add them.

**Agent calls Bash**

```bash
cd entries/figshare-24639285-tarduno-2024; python - <<'EOF'
import json, uuid
p="reproduce_tarduno_2024.ipynb"; nb=json.load(open(p))
print(nb.get("nbformat"), nb.get("nbformat_minor"), [("id" in c) for c in nb["cells"]][:5])
n=0
for c in nb["cells"]:
    if "id" not in c and nb.get("nbformat_minor",0)>=5:
        c["id"]=uuid.uuid4().hex[:8]; n+=1
print(n)
json.dump(nb, open(p, "w"), indent=1, ensure_ascii=False); open(p,"a").write("\n")
EOF
git diff --stat; cd  python tools/entry.py all entries/figshare-24639285-tarduno-2024 2>&1 | grep -v kernelspec | tail -4; python tools/entry.py check entries/figshare-24639285-tarduno-2024 2>&1|tail -2
```

```
4 5 [True, True, True, True, True]
3
 attempts/figshare-24639285-tarduno-2024-01.yaml    | 193 +++++++++++++++++++--
 entries/figshare-24639285-tarduno-2024/README.md   |   2 +-
 .../reproduce_tarduno_2024.ipynb                   | 175 +++++++++++++++++--
 3 files changed, 348 insertions(+), 22 deletions(-)
0 error(s)
pass  reproduce_tarduno_2024.ipynb  (25 s)
0 error(s)
```

**Agent calls Bash**

```bash
cd  git diff -U0 | grep "^+" | grep -n "—\|rather" ; python -c "
import json;nb=json.load(open('entries/figshare-24639285-tarduno-2024/reproduce_tarduno_2024.ipynb'));print(sum(len(c.get('outputs',[])) for c in nb['cells']))
import yaml;d=yaml.safe_load(open('questions/figshare-24639285.yaml'));print(len(d['questions']))"; git status --short
```

```
0
1
 M attempts/figshare-24639285-tarduno-2024-01.yaml
 M entries/figshare-24639285-tarduno-2024/README.md
 M entries/figshare-24639285-tarduno-2024/reproduce_tarduno_2024.ipynb
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
?? questions/figshare-24639285.yaml
?? scripts
?? tools/archives/openneuro.py
?? tools/build_openneuro_targets.py
```

**Agent calls Bash**

```bash
cd  ls -la .bash_profile .bashrc .gitconfig .profile .ripgreprc .zprofile .zshrc .mcp.json; ls -la .idea .vscode scripts | head -20
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 20:30 .bash_profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 20:30 .bashrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 20:30 .gitconfig
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 20:30 .mcp.json
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 20:30 .profile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 20:30 .ripgreprc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 20:30 .zprofile
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 20:30 .zshrc
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 20:30 .idea
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 20:30 .vscode
crw-rw-rw- 1 nobody nogroup 1, 3 Oct 27 20:30 scripts
```

**Agent**

I've finished the round-1 revision. The entry re-runs cleanly (`tools/entry.py all`: 0 errors, notebook passes in 25 s), and `tools/entry.py check` passes on the final versions.

**Outcome change**
- **example-14053g1-threshold:** changed from reproduced to partially reproduced, as the verifier suggested. The criterion counts the claim as reproduced only when the example matches for 14053g1 as written. Here it matches only if the crystal name is a misprint for 12040g1, so I recorded it as a partial match. I updated the notes, the result cell, the summary and the README.
- All other outcomes stay as they were, and the verifier agreed with each of them.

**Outputs added to the notebook (the verifier asked for all of these)**
- **table2-fit-statistics:**
  - Per-step replicate scatter for ss9, ss10 and ss6.
  - The score with one pTRM reading held fixed: 14 to 19 of 29 (48 to 66%), partial or lower under every reading.
  - The score with ss6 counted as a miss: 22 of 29 (76%).
  - None of the nine specimens is from a synthetic sheet, so dropping those sheets changes nothing here.
- **Two-cluster steps:** a scan of every glass step found 11 steps in 7 sheets whose replicates fall in two direction groups more than 45° apart, the way ss6 250.1 does. Nine of them are inside a Table 2 range. This is now in the deviations and a finding.
- **fig2-changing-field:**
  - How often readings (a) and (b) hold when there is no changing field: (a) 61 to 96%, (b) 51 to 57%. Both are weak tests.
  - An Arai curvature from a circle fit. It does not tell ss41 and ss22 apart from ss19 and ss43, which the paper presents as linear. The "curved" part of the claim is reported but not judged.
- **no-alteration-recording-efficiency:**
  - TRM40/TRM20 without the factor of 2: it ranges from 1.54 to 2.35, and three crystals are above 2.
  - The 590.0 replicate moments per crystal, which show the null state sits above the 8e-11 emu threshold.

**Other corrections**
- I updated the notes and deviations for table2-fit-statistics, fig2-changing-field and no-alteration-recording-efficiency.
- I added the two-cluster steps to the finding on repeated measurements.
- The summary now says the Table 1 maximum intensities rest on a threshold that is below the null level.
- Round 1 is recorded under `verifications`. All 17 claims are listed with the verifier's reasons in its own words and my responses.

**Question for a reader**
I created `questions/figshare-24639285.yaml` with one question on no-alteration-recording-efficiency. The criterion's text says the 40 µT TRM should be "about twice" the 20 µT TRM. But its cutoff only fails a crystal when the 40 µT TRM is more than four times the 20 µT TRM. With a cutoff of 2 on TRM40/TRM20, three crystals fail and the claim would not pass under either reading. I left the claim unchanged and tested it as the claims file has it.

**Not done**
- I kept the outcomes for problems 2 to 8, since the verifier said none of them affects a conclusion. Their analysis is now in the record.
- Comparing against Figures 1 to 3 and the deposit's supplementary PDFs is still out of reach: no figure PDF was supplied, and the PDFs were not read in this revision.
- `git status` shows untracked `.bashrc`, `.idea`, `scripts` and similar entries in the repo root. They are `/dev/null` device mounts from the sandbox, not files I created, and I left them alone.

## End of run

33 turns, 8 minutes, result: success.
