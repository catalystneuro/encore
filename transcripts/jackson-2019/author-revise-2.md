# openneuro-ds002778 · author-revise-2 · run 40604048967

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/openneuro-ds002778/verifier-2-report.md; ls entries/openneuro-ds002778-jackson-2019 entries/openneuro-ds002778-jackson-2019/*
```

```
Tue Oct 27 23:47:12 UTC 2026
**Verification report, round 2: Jackson et al. 2019 (eNeuro 0151-19.2019) on OpenNeuro ds002778 v1.0.5**

**Counts.** The claims file has 24 claims and the attempt record gives 24 outcomes: 9 reproduced, 9 partially reproduced, 6 not reproduced, none blocked. These are the outcomes I gave in round 1.

**How I checked this round.**
- I read every printed output of the re-executed notebook (cells 0–84).
- From the printed per-patient values, I recomputed the new variants without pd6 and pd16:
  - Beta sharpness: W 11, p 0.0159, d 0.811.
  - Beta steepness: W 5, p 0.0046, d 0.752.
  - Beta PAC (Methods filters): W 13, p 0.0231, d 0.732.
  - Spearman r on/off with and without the two patients.
  - All match to rounding.
- I recomputed the BH correction for Table 2 from the printed p-values (0.0531 for both steepness tests).
- I checked the Q4 counts in the paper's text (paragraph 90): C3 9, C4 8, both 8, so 9 with at least one. The claims file reads them correctly.

### 1. Outcomes and assumptions

I agree with all 24 outcomes.

[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -60; ls attempts* 2>/dev/null | head; find . -path ./node_modules -prune -o -name "*ds002778*" -print | grep -v "^./.git/" | head -30
```

**Agent calls Bash**

```bash
sed -n 1,400p docs/protocol.md | awk '/^## Author/,0' | head -250
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
[... 16 more lines not kept]
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

[... 200 more lines not kept]
```

**Agent calls Bash**

```bash
awk '/^### 5. Record the attempt/,/^## Repeat attempts/' docs/protocol.md; awk '/^### 4. Lock, check/,/^### 5/' docs/protocol.md
```

```
### 5. Record the attempt

Write `attempts/<entry name>-<nn>.yaml`.

- **One outcome per claim**, including blocked ones. The outcome describes the
  result, not the method:
  - `reproduced`: the result matches the claim.
  - `partially_reproduced`: the effect is present but weaker, or holds only in
    part.
  - `not_reproduced`: the analysis ran and the result differs.
  - `blocked`: the claim could not be tested; give `blocked_by` and say why.
    When the paper states a chance level or false-positive rate for a
    selection, compute it with your procedure. If yours is far from the
    paper's, the procedures differ, and the outcome is `blocked` with
    `methods_underspecified` even though the analysis ran.

  The criterion decides the outcome. Where the claim's statement says more
  than the criterion tests (a p-value, a second condition), the notes say
  whether that part holds.
- **`deviations`**: every way the test differed from the paper's method or
[... 82 more lines not kept]
```

**Agent**

Now the attempt record.

**Agent calls Bash**

```bash
wc -l attempts/openneuro-ds002778-jackson-2019-01.yaml; grep -n "verifications" -A3 attempts/openneuro-ds002778-jackson-2019-01.yaml | head; grep -n "round" attempts/openneuro-ds002778-jackson-2019-01.yaml | head -40
```

```
580 attempts/openneuro-ds002778-jackson-2019-01.yaml
400:verifications:
401-- date: 2026-10-27
402-  kind: agent
403-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
144:    is not reproduced (changed from partially reproduced after verification round 1). The miss
231:    of three, so the claim is not reproduced (changed after verification round 1 from reproduced
253:    claim is not reproduced (changed from partially reproduced after verification round 1).
```

**Agent calls Read**

```json
{
 "file_path": "attempts/openneuro-ds002778-jackson-2019-01.yaml"
}
```

```
1	schema_version: 2
2	id: openneuro-ds002778-jackson-2019-01
3	dataset:
4	  archive: openneuro
5	  id: ds002778
6	  version: 1.0.5
7	  doi: 10.18112/openneuro.ds002778.v1.0.5
8	paper: doi:10.1523/eneuro.0151-19.2019
9	date: 2026-10-27
10	entry: openneuro-ds002778-jackson-2019
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-12
19	  runner:
20	    platform: GitHub Actions
[... 561 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/openneuro-ds002778-jackson-2019; wc -c *; python -c "
import json;nb=json.load(open('reproduce_jackson_2019.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source']); print(i,c['cell_type'],c['metadata'].get('tags'),repr(s[:90]))
"; cat ../../questions/openneuro-ds002778.yaml; ls ../../executed/ 2>/dev/null | head
```

```
2690 README.md
  1004 entry.yaml
 80585 reproduce_jackson_2019.ipynb
    43 requirements.in
  1384 requirements.lock.txt
 20255 waveshape.py
105961 total
0 markdown None '# Reproducing Jackson, Cole, Voytek & Swann (2019) from OpenNeuro ds002778\n\n**Paper.** Jac'
1 code None 'import itertools\nimport time\nimport warnings\nfrom concurrent.futures import ThreadPoolExec'
2 markdown None '## Data check'
3 code ['sanity'] 'kinds = files.index.str.replace(r"sub-(pd|hc)\\d+", "sub-X", regex=True)\nprint("Files by ki'
4 code ['sanity'] 'participants = ws.read_tsv("participants.tsv")\nparticipants["group"] = np.where(participan'
5 markdown None 'The participant counts match the paper (15 patients, 16 controls). The table below checks '
6 code ['sanity'] 'side = {}\nfor r in recs.itertuples():\n    base = f"sub-{r.sub}/ses-{r.ses}/eeg/sub-{r.sub}'
7 markdown None 'Every recording is at 512 Hz, lasts 181 to 292 s (the paper says at least 3 min), and has '
8 code ['sanity'] '# events.tsv against the Status channel: the only time base in the files\nrows = []\nfor i i'
9 markdown None 'The events files hold one trigger per recording (value 1, 1 to 30 s into the file; sub-pd6'
10 code ['sanity'] '# recordings deposited twice: identical raw samples at the start of C3, across all pairs\nh'
11 code ['sanity'] 'beh = {}\nfor r in recs.itertuples():\n    beh[(r.sub, r.ses)] = ws.read_json(f"sub-{r.sub}/'
12 markdown None 'The UPDRS fields have no description in the dataset (the only `beh` sidecar describes a du'
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed 2>&1 | head; cat entries/openneuro-ds002778-jackson-2019/entry.yaml; ls transcripts/openneuro-ds002778/; python -c "
import json;nb=json.load(open('entries/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb'))
for i in [1,14,16,17,19,20,22,23]:
  print('=====',i); print(''.join(nb['cells'][i]['source']))
"
```

```
ls: cannot access 'executed': No such file or directory
schema_version: 1
name: openneuro-ds002778-jackson-2019
type: reproduction
title: Beta waveform shape in Parkinson's disease scalp EEG (Jackson et al. 2019)
description: Tests the findings of Jackson, Cole, Voytek and Swann (2019) on OpenNeuro ds002778,
  which holds the resting EEG of 15 patients with Parkinson's disease off and on medication and 16
  controls. It computes beta and alpha sharpness ratio, steepness ratio and phase-amplitude coupling
  over sensorimotor and temporal electrodes, compares medication states and groups, and classifies
  waveform shape by peak-to-trough and rise-to-fall ratios. The paper's manual artifact marks are
  not in the dataset, so no samples are rejected.
license: Apache-2.0
notebooks:
- path: reproduce_jackson_2019.ipynb
  title: Reproducing Jackson et al. (2019) from OpenNeuro ds002778
  runtime_minutes: 3
helpers:
- waveshape.py
related:
- id: openneuro:ds002778/1.0.5
[... 211 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py all entries/openneuro-ds002778-jackson-2019 2>&1 | tail -15
```

```
Tue Oct 27 23:47:43 UTC 2026
Installed kernelspec registry-openneuro-ds002778-jackson-2019 in executed/openneuro-ds002778-jackson-2019/.venv/share/jupyter/kernels/registry-openneuro-ds002778-jackson-2019
0 error(s)
pass  reproduce_jackson_2019.ipynb  (134 s)

real	2m46.166s
user	5m52.098s
sys	0m9.643s
```

**Agent**

Now let me see the relevant cells with outputs.

**Agent calls Bash**

```bash
cd  ls executed/openneuro-ds002778-jackson-2019/; cat > $TMPDIR/show.py <<'EOF'
import json,sys
nb=json.load(open('executed/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb'))
for i in map(int,sys.argv[1:]):
  c=nb['cells'][i]; print('=====',i); print(''.join(c['source']))
  for o in c.get('outputs',[]):
    if 'text' in o: print('--- out'); print(''.join(o['text']))
EOF
python $TMPDIR/show.py 22 33 34 44 45
```

```
reproduce_jackson_2019.ipynb
result.json
===== 22
rows = []
for reading in ["methods", "code"]:
    c = PAC("beta", reading)
    r = offon_row(c, f"beta PAC, {reading} filters")
    p_ = paired(c)
    r["d_log10"] = ws.cohen_d(np.log10(p_.off), np.log10(p_.on))
    lo, hi = fdr_range(table1[table1.beta_pac == reading], "beta PAC")
    r["p_fdr_min"], r["p_fdr_max"] = lo, hi
    rows.append(r)
print(pd.DataFrame(rows).round(4).to_string(index=False))
show_patients(PAC("beta", "methods"), "Beta PAC, Methods filters (118/123 samples)")
print("Expected: W 15 +/- 1.5 (13.5 to 16.5); d 0.83 +/- 0.083 (0.747 to 0.913)")
print("\nVariants (not the criterion):")
rows = []
for reading in ["methods", "code"]:
    for label, c in [(f"{reading} filters, edges dropped (pacpy rmvedge)", PAC("beta", reading + " trimmed")),
                     (f"{reading} filters, without pd6 and pd16", None)]:
[... 175 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/show.py 73 74 82 83 84
```

```
===== 73
pq = pts[pts.signal.isin(["C3", "C4"]) & pts.group.isin(["off", "on"])]
both = pq.assign(q4=pq.quadrant == "Q4").pivot_table(index="sub", columns=["signal", "ses"], values="q4", aggfunc="first")
meets = pd.DataFrame({"C3": both[("C3", "off")] & both[("C3", "on")], "C4": both[("C4", "off")] & both[("C4", "on")]})
print(meets.astype(int).T.to_string())
n_c3, n_c4 = int(meets.C3.sum()), int(meets.C4.sum())
n_both, n_any = int((meets.C3 & meets.C4).sum()), int((meets.C3 | meets.C4).sum())
print(f"\nPatients meeting the criterion: C3 {n_c3}, C4 {n_c4}, both {n_both}, at least one {n_any}")
print("Expected (+/- 1): C3 9, C4 8, both 8, at least one 9; swapped electrode order C3 8, C4 9")

print("\nPer-patient log10 peak-to-trough (PTR) and rise-to-fall (RDR) ratios at C3 and C4; Q4 is PTR > 0 and RDR < 0")
print(pq.pivot_table(index="sub", columns=["signal", "ses"], values=["PTR", "RDR"]).round(4)
      .loc[meets.index].to_string())
near = pq[(pq.PTR.abs() < 0.01) | (pq.RDR.abs() < 0.01)]
print(f"Points within 0.01 of an axis: {len(near)}")
print(near[["sub", "signal", "ses", "PTR", "RDR", "quadrant"]].round(4).to_string(index=False))
m_ex = excl(meets)
print("Without pd6 and pd16 (13 patients): C3 %d, C4 %d, both %d, at least one %d"
      % (m_ex.C3.sum(), m_ex.C4.sum(), (m_ex.C3 & m_ex.C4).sum(), (m_ex.C3 | m_ex.C4).sum()))

[... 176 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat entries/openneuro-ds002778-jackson-2019/README.md; grep -n "trimmed\|reading" entries/openneuro-ds002778-jackson-2019/waveshape.py | head -30; python $TMPDIR/show.py 25 53 56 59 62 | head -120
```

```
# Jackson, Cole, Voytek & Swann (2019) from OpenNeuro ds002778

Tests the findings of [Jackson et al. (2019)](https://doi.org/10.1523/ENEURO.0151-19.2019) on
[OpenNeuro ds002778](https://openneuro.org/datasets/ds002778/versions/1.0.5), snapshot 1.0.5, which
holds the resting EEG of 15 patients with Parkinson's disease off and on medication and 16 controls.
The paper's manual artifact marks and excluded electrodes are not in the dataset, so the analysis
rejects no samples and keeps all 32 scalp electrodes.

| Claim | Outcome |
|---|---|
| Beta sharpness ratio, steepness ratio and PAC fall with medication (C3/C4) | Partially reproduced (each test holds; one value per claim out of tolerance) |
| The same with a bipolar montage | Reproduced |
| No medication effect at F7/F8 or at T7/T8 | Reproduced |
| Topographies consistent with a sensorimotor origin | Partially reproduced |
| Off against controls: no difference in sharpness ratio or PAC | Reproduced |
| Off against controls: steepness ratio higher | Not reproduced (z and d match, FDR p 0.053) |
| Off against controls: PAC higher with a CSD montage | Not reproduced (p 0.075) |
| UPDRS improves with medication | Reproduced (W 3.5, p 0.0033) |
| Alpha and beta peaks in every group's spectrum | Not reproduced |
| Alpha sharpness and steepness fall with medication | Partially reproduced |
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 335,360p entries/openneuro-ds002778-jackson-2019/waveshape.py; grep -n "def p_adjust\|def fdr_bh" -A3 entries/openneuro-ds002778-jackson-2019/waveshape.py
```

```
for name, y in bip.items():
        m = shape_measures(y, BETA, 118)
        brow.append({"sub": sub, "ses": ses, "signal": name, "band": "beta", "taps": "118", **m})
        for rname, (nlo, nhi) in PAC_BETA.items():
            prow.append({"sub": sub, "ses": ses, "signal": name, "band": "beta", "reading": rname,
                         "PAC": pac_ozkurt(y, BETA, nlo, GAMMA, nhi)})
    shape = pd.concat([shape, pd.DataFrame(brow)], ignore_index=True)

    # beta PAC at C3 and C4 with the filter edges dropped (variant)
    for ch in ("C3", "C4"):
        for rname, (nlo, nhi) in PAC_BETA.items():
            prow.append({"sub": sub, "ses": ses, "signal": ch, "band": "beta", "reading": rname + " trimmed",
                         "PAC": pac_ozkurt(x[SCALP.index(ch)], BETA, nlo, GAMMA, nhi, trim=True)})

    # current source density: main ("m3", signal "CSD C3") and variants ("CSD m4 C3", ...)
    csd_psd = {}
    for vname, (m, lam) in CSD_VARIANTS.items():
        xc = csd(x, m, lam)
        tag = "CSD " if vname == "m3" else f"CSD {vname} "
        for ch in ("C3", "C4"):
[... 15 more lines not kept]
```

**Agent**

Now edit the notebook with a Python script.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/edit1.py <<'EOF'
import json
P='entries/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb'
nb=json.load(open(P))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
def rep(i,a,b):
    s=src(i); assert a in s,(i,a); setsrc(i,s.replace(a,b))

# cell 33: print ties for the smallest p
rep(33,'''    best = t.iloc[0]
''','''    best = t.iloc[0]
    tied = t[np.isclose(t.p, best.p)].electrode.tolist()
''')
rep(33,'''in sensorimotor set: {best.electrode in SENSORI}; "''','''in sensorimotor set: {best.electrode in SENSORI}; "
          f"tied for smallest p: {tied} (in sensorimotor set: {[e in SENSORI for e in tied]}); "''')

# cell 44: direction of the CSD variants off against on
rep(44,'''        r["p_off_on"] = offon_row(c, "")["p"]
''','''        r_on = offon_row(c, "")
        r["p_off_on"], r["off>on"], r["mean_on"] = r_on["p"], r_on["off>on"], r_on["mean_on"]
''')

# cell 73: which near-axis points decide membership
rep(73,'''m_ex = excl(meets)''','''

def q4_status(ptr, rdr):
    return (ptr > 0) & (rdr < 0)


# a point decides membership if moving its near-axis coordinates across zero changes its Q4 status
# and the other session at the same electrode is in Q4
q4 = pq.set_index(["sub", "signal", "ses"])
dec = []
for (s, e, ses), r_ in q4.iterrows():
    near_c = [k for k in ["PTR", "RDR"] if abs(r_[k]) < 0.01]
    other = q4.loc[(s, e, "on" if ses == "off" else "off")]
    if not near_c or not q4_status(other.PTR, other.RDR):
        continue
    now = q4_status(r_.PTR, r_.RDR)
    alts = []
    for k in range(1, len(near_c) + 1):
        for flip in itertools.combinations(near_c, k):
            v = {c_: (-r_[c_] if c_ in flip else r_[c_]) for c_ in ["PTR", "RDR"]}
            alts.append(q4_status(v["PTR"], v["RDR"]))
    if any(a != now for a in alts):
        dec.append({"sub": s, "signal": e, "ses": ses, "PTR": r_.PTR, "RDR": r_.RDR, "in Q4": bool(now)})
dec = pd.DataFrame(dec)
print(f"\\nNear-axis points that decide membership at their electrode: {len(dec)}, patients "
      f"{sorted(dec['sub'].unique(), key=lambda s: int(s[2:]))}")
print(dec.round(4).to_string(index=False))
m_ex = excl(meets)''')

# new sensitivity section before the summary
i_sum = next(i for i,c in enumerate(C) if src(i).startswith('## Summary'))
md = {"cell_type":"markdown","metadata":{},"source":'''## Sensitivity: off against on without sub-pd6 and sub-pd16

The `on` sessions of sub-pd6 and sub-pd16 were exported from preprocessed EEGLAB files (data
check). This variant repeats every off against on test of Table 1, under the 12 combinations of
filter readings with FDR over the six tests, and the three bipolar tests with FDR over the
three, without these two patients. It is not part of any criterion.'''.splitlines(keepends=True)}
code = {"cell_type":"code","metadata":{},"execution_count":None,"outputs":[],"source":'''def offon_row_ex(c, label):
    p = excl(paired(c))
    W, pa = ws.signed_rank(p.off, p.on)
    return {"test": label, "n": len(p), "W": W, "p": pa, "off>on": int((p.off > p.on).sum()), "d": ws.cohen_d(p.off, p.on)}


rows = []
for a_taps, a_pac, b_pac in itertools.product(["192", "118"], ["a192", "b231", "c118"], ["methods", "code"]):
    tests = [offon_row_ex(SHR("alpha", a_taps), "alpha ShR"), offon_row_ex(STR("alpha", a_taps), "alpha StR"),
             offon_row_ex(PAC("alpha", a_pac), "alpha PAC"), offon_row_ex(SHR(), "beta ShR"),
             offon_row_ex(STR(), "beta StR"), offon_row_ex(PAC("beta", b_pac), "beta PAC")]
    for t, qq in zip(tests, ws.fdr_bh([t["p"] for t in tests])):
        rows.append({"alpha_shape_taps": a_taps, "alpha_pac": a_pac, "beta_pac": b_pac, **t, "p_fdr": qq})
t1x = pd.DataFrame(rows)
t1x = t1x.assign(reading=np.select([t1x.test.str.startswith("alpha Sh") | t1x.test.str.startswith("alpha St"),
                                    t1x.test == "alpha PAC", t1x.test == "beta PAC"],
                                   ["alpha shape " + t1x.alpha_shape_taps, "alpha PAC " + t1x.alpha_pac,
                                    "beta PAC " + t1x.beta_pac], "-"))
print("Table 1 without pd6 and pd16, by test and the filter reading it depends on (p_fdr over the readings of the other tests):")
print(t1x.groupby(["test", "reading"], sort=False).agg(n=("n", "first"), W=("W", "first"), p=("p", "first"),
      off_gt_on=("off>on", "first"), d=("d", "first"), p_fdr_min=("p_fdr", "min"), p_fdr_max=("p_fdr", "max"))
      .round(4).to_string())
full = table1.assign(sig=table1.p_fdr < 0.05).groupby("test").sig.agg(["min", "max"])
ex_ = t1x.assign(sig=t1x.p_fdr < 0.05).groupby("test").sig.agg(["min", "max"])
print("\\nSignificant after FDR (under no reading / some / every reading), all patients against without pd6 and pd16:")
lab = lambda r: "every" if r["min"] else ("some" if r["max"] else "none")
print(pd.DataFrame({"all patients": full.apply(lab, axis=1), "without pd6, pd16": ex_.apply(lab, axis=1)}).to_string())

print("\\nBipolar (C3-CP1, C4-CP2) without pd6 and pd16:")
for reading in ["methods", "code"]:
    t = pd.DataFrame([offon_row_ex(SHR(sig=BIP), "bipolar ShR"), offon_row_ex(STR(sig=BIP), "bipolar StR"),
                      offon_row_ex(PAC("beta", reading, BIP), f"bipolar PAC ({reading})")])
    t["p_fdr3"] = ws.fdr_bh(t.p)
    print(t.round(4).to_string(index=False))
'''.splitlines(keepends=True)}
C[i_sum:i_sum]=[md,code]
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
python $TMPDIR/edit1.py && git diff --stat
```

```
.../reproduce_jackson_2019.ipynb                   | 86 +++++++++++++++++++++-
 1 file changed, 85 insertions(+), 1 deletion(-)
```

**Agent calls Bash**

```bash
cd  python tools/entry.py all entries/openneuro-ds002778-jackson-2019 2>&1 | tail -4; python $TMPDIR/show.py 33 44 73 85 | grep -v "^ *$" | sed -n '/--- out/,$p' | head -150
```

```
_validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-openneuro-ds002778-jackson-2019 in executed/openneuro-ds002778-jackson-2019/.venv/share/jupyter/kernels/registry-openneuro-ds002778-jackson-2019
0 error(s)
pass  reproduce_jackson_2019.ipynb  (134 s)
--- out
ShR: smallest p at P8 (p = 0.0064); in sensorimotor set: False; tied for smallest p: ['P8'] (in sensorimotor set: [False]); significant uncorrected: ['P8', 'CP6', 'AF3']; FDR: []
   F7/F8/T7/T8 p: {'T8': 0.233, 'F8': 0.4603, 'T7': 0.4955, 'F7': 0.5701} 
   five smallest: {'P8': 0.0064, 'CP6': 0.0171, 'AF3': 0.0309, 'C3': 0.0995, 'F4': 0.0995}
StR: smallest p at C4 (p = 0.0231); in sensorimotor set: True; tied for smallest p: ['C4'] (in sensorimotor set: [True]); significant uncorrected: ['C4']; FDR: []
   F7/F8/T7/T8 p: {'T7': 0.2115, 'F7': 0.256, 'F8': 0.4265, 'T8': 0.5701} 
   five smallest: {'C4': 0.0231, 'CP6': 0.0691, 'Oz': 0.1118, 'P4': 0.1252, 'Fp2': 0.1556}
PAC methods: smallest p at CP6 (p = 0.0268); in sensorimotor set: True; tied for smallest p: ['CP6'] (in sensorimotor set: [True]); significant uncorrected: ['CP6', 'Fz', 'C3', 'F7', 'C4']; FDR: []
   F7/F8/T7/T8 p: {'F7': 0.0409, 'T8': 0.0783, 'F8': 0.1914, 'T7': 0.5321} 
   five smallest: {'CP6': 0.0268, 'Fz': 0.0309, 'C3': 0.0356, 'F7': 0.0409, 'C4': 0.0409}
PAC code: smallest p at Fz (p = 0.0199); in sensorimotor set: False; tied for smallest p: ['Fz', 'CP6'] (in sensorimotor set: [False, True]); significant uncorrected: ['Fz', 'CP6', 'C3', 'FC5', 'F7']; FDR: []
   F7/F8/T7/T8 p: {'F7': 0.0468, 'T8': 0.0884, 'F8': 0.1728, 'T7': 0.4603} 
   five smallest: {'Fz': 0.0199, 'CP6': 0.0199, 'C3': 0.0268, 'FC5': 0.0356, 'F7': 0.0468}
--- out
-log10 p range plotted: -0.00 to 2.19; nothing outside the axes
===== 44
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python $TMPDIR/show.py 73 86 | sed -n '/Near-axis points that decide membership at their electrode: /,$p' | grep -v "^ *$"; python tools/entry.py check entries/openneuro-ds002778-jackson-2019 2>&1 | tail -5
```

```
print(f"\nNear-axis points that decide membership at their electrode: {len(dec)}, patients "
      f"{sorted(dec['sub'].unique(), key=lambda s: int(s[2:]))}")
print(dec.round(4).to_string(index=False))
m_ex = excl(meets)
print("Without pd6 and pd16 (13 patients): C3 %d, C4 %d, both %d, at least one %d"
      % (m_ex.C3.sum(), m_ex.C4.sum(), (m_ex.C3 & m_ex.C4).sum(), (m_ex.C3 | m_ex.C4).sum()))
--- out
sub  pd11  pd12  pd13  pd14  pd16  pd17  pd19  pd22  pd23  pd26  pd28  pd3  pd5  pd6  pd9
C3      1     0     0     1     0     1     1     1     1     1     0    1    1    1    0
C4      0     1     1     1     0     1     1     0     1     1     1    1    0    1    0
Patients meeting the criterion: C3 10, C4 10, both 7, at least one 13
Expected (+/- 1): C3 9, C4 8, both 8, at least one 9; swapped electrode order C3 8, C4 9
Per-patient log10 peak-to-trough (PTR) and rise-to-fall (RDR) ratios at C3 and C4; Q4 is PTR > 0 and RDR < 0
           PTR                             RDR                        
signal      C3              C4              C3              C4        
ses        off      on     off      on     off      on     off      on
sub                                                                   
pd11    0.0444  0.0287  0.0501 -0.0021 -0.0976 -0.0870 -0.2533 -0.0104
pd12    0.0448 -0.0067  0.0388  0.0236 -0.0277  0.0049 -0.0111 -0.0062
pd13    0.0041  0.0005  0.0472  0.0264  0.0358  0.0579 -0.1524 -0.0357
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json,uuid
P='entries/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb'
nb=json.load(open(P))
print(nb['nbformat'],nb['nbformat_minor'],[('id' in c) for c in nb['cells']][:3])
for c in nb['cells']:
    if 'id' not in c and any('id' in d for d in nb['cells']): c['id']=uuid.uuid4().hex[:8]
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
git diff entries/*/reproduce_jackson_2019.ipynb | head -20; python $TMPDIR/show.py 85 | sed -n '/--- out/,$p'
```

```
4 5 [True, True, True]
diff --git a/entries/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb b/entries/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb
index 042e3714a..5949e9e8b 100644
--- a/entries/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb
+++ b/entries/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb
@@ -737,8 +737,10 @@
     "for m, t in topo.groupby(\"measure\", sort=False):\n",
     "    t = t.sort_values(\"p\")\n",
     "    best = t.iloc[0]\n",
+    "    tied = t[np.isclose(t.p, best.p)].electrode.tolist()\n",
     "    tem = t[t.electrode.isin(TEMPORAL)]\n",
     "    print(f\"{m}: smallest p at {best.electrode} (p = {best.p:.4f}); in sensorimotor set: {best.electrode in SENSORI}; \"\n",
+    "          f\"tied for smallest p: {tied} (in sensorimotor set: {[e in SENSORI for e in tied]}); \"\n",
     "          f\"significant uncorrected: {t[t.p < 0.05].electrode.tolist()}; FDR: {t[t.p_fdr32 < 0.05].electrode.tolist()}\")\n",
     "    print(\"   F7/F8/T7/T8 p:\", dict(zip(tem.electrode, tem.p.round(4))), \"\\n   five smallest:\",\n",
     "          dict(zip(t.electrode[:5], t.p[:5].round(4))))\n",
@@ -934,7 +936,8 @@
     "    for rd in [\"methods\", \"code\"]:\n",
     "        c = PAC(\"beta\", rd, (tag + \"C3\", tag + \"C4\"))\n",
     "        r = offctrl_row(c, f\"{vname} ({rd})\")\n",
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/edit2.py <<'EOF'
import json
P='entries/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb'
nb=json.load(open(P))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def rep(i,a,b):
    s=src(i); assert a in s,(i,a); C[i]['source']=s.replace(a,b).splitlines(keepends=True)
rep(23,"changes PAC by 5% at most in any recording and\nleaves W at 13 and 12.",
       "changes PAC by 5.1% at most in any recording (ratio\n0.949 to 1.043) and leaves W at 13 and 12.")
rep(34,"but with the code's filters the smallest p is at Fz (0.020).",
       "but with the code's filters Fz and CP6 tie for the smallest p (0.020), and Fz is outside the\nsensorimotor set.")
rep(45,"Off against on, CSD PAC is higher off under every variant (p 0.0045 to 0.015).",
       "Off against on, CSD PAC is higher off under every variant (mean off above mean on, 12 or 13\nof 15 patients higher off, p 0.0045 to 0.015).")
rep(74,"""among them points that
decide membership (pd12, pd22, pd26, pd28, pd3 and pd9 on medication), so small differences in
preprocessing can move patients in or out.""",
"""and 10 of them decide
membership at their electrode: moving their near-axis coordinates across zero would change
whether the patient counts there (pd3, pd5, pd11, pd12, pd22, pd26 and pd28; all on medication
except pd22 at C4 off). Small differences in preprocessing can therefore move patients in or
out.""")
i=86; assert src(i).startswith('## Summary')
rep(i,"partially reproduced (d rises for all three; two values above tolerance)",
      "partially reproduced (d rises for all three; Q4 steepness and PAC d above tolerance, and raw PAC all-patient d 0.85 above 0.825)")
rep(i,"""the off against on tests keep their direction and significance and
the correlation of steepness ratio with PAC falls within tolerance off and on; the Q4 counts become
9, 9, 6 and 12. Dropping the filtered edges from PAC, as pacpy does, changes no test.""",
"""the six off against on tests of Table 1 and the three bipolar tests keep their
direction, and those significant after FDR correction under every reading stay so (corrected p
0.017 to 0.033). Alpha PAC, significant after correction under one of three phase filter readings
with all patients (0.036), is not significant under any without them (0.064 to 0.087). The
correlation of steepness ratio with PAC falls within tolerance off and on, and the Q4 counts become
9, 9, 6 and 12. Dropping the filtered edges from PAC, as pacpy does, was run for the beta off
against on test at C3 and C4 only, and leaves W at 13 and 12.""")
rep(i,"""controls (9 female, 63.5) the paper describes, each recording once,""",
"""controls (9 female, 63.5) the paper describes, patients recorded off and on medication and
controls once, with no recording deposited twice,""")
rep(i,"""The UPDRS fields carry no description. Without artifact rejection the main off against on
results hold, with statistics close to the paper's.""",
"""The UPDRS fields carry no description. Without artifact rejection the three main off against
on tests at C3 and C4 hold after FDR correction, but each has one value outside tolerance
(sharpness d 0.73 against 0.86, steepness W 16 against 9, PAC W 13 against 15).""")
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
python $TMPDIR/edit2.py && python $TMPDIR/show.py 4 10 | grep -i "ses\|twice\|identical" | head
```

```
pd_subs = sorted(recs[recs.ses == "off"]["sub"], key=lambda s: int(s[2:]))
print("Patients with both off and on:", len(set(recs[recs.ses == "off"]["sub"]) & set(recs[recs.ses == "on"]["sub"])))
      sub-hc21                                        Subject was missing reading glasses
# recordings deposited twice: identical raw samples at the start of C3, across all pairs
heads = {(i.sub, i.ses): i.raw_c3_head for i in info.itertuples()}
print("Pairs of recordings with identical (or r > 0.99) first 4 s of raw C3:", dupes)
Pairs of recordings with identical (or r > 0.99) first 4 s of raw C3: []
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
P='entries/openneuro-ds002778-jackson-2019/reproduce_jackson_2019.ipynb'
nb=json.load(open(P)); c=nb['cells'][86]; s=''.join(c['source'])
a="""stay so (corrected p
0.017 to 0.033)."""
assert a in s
c['source']=s.replace(a,"""stay so (corrected p
0.017 to 0.033 for Table 1, 0.011 to 0.019 for the bipolar tests).""").splitlines(keepends=True)
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
date -u
```

```
Tue Oct 27 23:55:18 UTC 2026
```

**Agent calls Bash**

```bash
cd  ls claims/openneuro-ds002778/; grep -n "id: pac-beta-larger-than-alpha" -A30 claims/openneuro-ds002778/*.yaml | head -45
```

```
10.1523-eneuro.0151-19.2019.yaml
452:- id: pac-beta-larger-than-alpha
453-  statement: The off against on medication difference in PAC is larger in the beta band than in the
454-    mu/alpha band.
455-  source: Results, Waveform metrics differentiate PD medication state, paragraph 4
456-  quote: for PAC, the difference between off medication and on medication in β was significantly larger
457-    than the difference in μ/α for the same comparison (Wilcoxon signed rank test statistic = 11, p =
458-    0.005)
459-  statistics:
460-  - test: Wilcoxon signed rank
461-    statistic: signed rank = 11
462-    p: 0.005
463-    n: 15 patients
464-  expected:
465-    quantity: signed rank statistic, beta against alpha off-on PAC difference
466-    value: 11
467-    tolerance: 1.1
468-  depends_on:
469-  - fig2-pac-off-on
470-  - table1-alpha-pac-null
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -i 's/^# Questions from attempt openneuro-ds002778-jackson-2019-01 (author, revision after verifier round 1)$/# Questions from attempt openneuro-ds002778-jackson-2019-01 (author, revisions after verifier rounds 1 and 2)/' questions/openneuro-ds002778.yaml; head -2 questions/openneuro-ds002778.yaml; cat >> questions/openneuro-ds002778.yaml <<'EOF'
- claim: pac-beta-larger-than-alpha
  attempt: openneuro-ds002778-jackson-2019-01
  asked: 2026-10-27
  question: The criterion says when the claim is reproduced (p < 0.05 with the beta difference larger
    and the statistic within tolerance) but has no clause for a partial outcome. Is the claim
    partially reproduced, or not reproduced, when the test holds with the beta difference larger
    but the statistic is outside tolerance?
  passage: Results, Waveform metrics differentiate PD medication state, paragraph 4 ("for PAC, the
    difference between off medication and on medication in beta was significantly larger than the
    difference in mu/alpha for the same comparison (Wilcoxon signed rank test statistic = 11, p =
    0.005)").
  why: Here, on raw PAC, the beta difference is larger in 12 or 13 of 15 patients and p = 0.015 to
    0.017 under every filter reading, but W is 17 or 18, outside 11 +/- 1.1. The attempt records
    partially reproduced, by the protocol's general definition (the effect is present but weaker);
    the verifier of round 2 agreed with that outcome but noted that the claims file does not define
    it. A criterion that treats the statistic as required would give not reproduced.
EOF
python -c "import yaml;print(len(yaml.safe_load(open('questions/openneuro-ds002778.yaml'))['questions']))"
```

```
# Questions from attempt openneuro-ds002778-jackson-2019-01 (author, revisions after verifier rounds 1 and 2)
# about claims/openneuro-ds002778/10.1523-eneuro.0151-19.2019.yaml.
2
```

**Agent calls Bash**

```bash
cd  python tools/entry.py all entries/openneuro-ds002778-jackson-2019 2>&1 | tail -3; python $TMPDIR/show.py 23 34 45 74 86 | grep -v "^$" | head -40
```

```
Installed kernelspec registry-openneuro-ds002778-jackson-2019 in executed/openneuro-ds002778-jackson-2019/.venv/share/jupyter/kernels/registry-openneuro-ds002778-jackson-2019
0 error(s)
pass  reproduce_jackson_2019.ipynb  (133 s)
===== 23
**Result: partially reproduced.** PAC is higher off than on (p = 0.0076 with the Methods'
filters and 0.0064 with the code's, FDR corrected 0.0228), and d on raw PAC is 0.85 and 0.86,
within 0.83 +/- 0.083 (on log10 PAC 0.73 and 0.86). The signed rank statistic is 13 and 12,
outside 15 +/- 1.5 under both filter readings. The criterion's first sentence ("As for
fig2-sharpness-off-on") asks for the statistic and d within tolerance, its last sentence for
the test and d only; the stricter reading is applied, and the question is put to a reader.
Dropping the filtered edges, as pacpy does, changes PAC by 5.1% at most in any recording (ratio
0.949 to 1.043) and leaves W at 13 and 12. Without sub-pd6 and sub-pd16, W = 13 and 12, p = 0.023 and 0.019,
d = 0.73 and 0.75.
===== 34
**Result: partially reproduced.** Steepness ratio meets the criterion: the smallest p is at
C4 (0.023) and none of F7, F8, T7, T8 is significant. PAC meets it with the Methods' filters
under the FDR reading (smallest p at CP6, 0.027; F7 has p = 0.041 uncorrected, so not under
the uncorrected reading), but with the code's filters Fz and CP6 tie for the smallest p (0.020), and Fz is outside the
sensorimotor set.
Sharpness ratio does not: its smallest p is at P8 (0.0064), then CP6 and AF3. No electrode
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
P='attempts/openneuro-ds002778-jackson-2019-01.yaml'
s=open(P).read()
def rep(a,b):
    global s; assert s.count(a)==1,a; s=s.replace(a,b)
rep("changes PAC by at most 5% in any recording and leaves W at 13 and 12.",
    "changes PAC by at most 5.1% in any recording (ratio 0.949 to 1.043) and leaves W at 13 and 12.")
rep("with the code's filters the smallest p is at Fz (0.020).",
    "with the code's filters Fz and CP6 tie for the smallest p (0.020), and Fz is outside the\n    sensorimotor set.")
rep("The CSD montage increases the off against on difference (d = 1.20, p = 0.0106).",
    "The CSD montage increases the off against on difference (d = 1.20, p = 0.0106); every CSD\n    variant gives a higher mean off than on, with 12 or 13 of 15 patients higher off (p 0.0045 to\n    0.015).")
rep("""Of the 60 points, 16 lie
    within 0.01 of an axis (log10 ratios), several of which decide a patient's membership; the
    per-patient values are printed.""",
"""Of the 60 points, 16 lie
    within 0.01 of an axis (log10 ratios), and 10 of them decide membership at their electrode
    (moving their near-axis coordinates across zero would change whether the patient counts
    there), in pd3, pd5, pd11, pd12, pd22, pd26 and pd28; the per-patient values are printed.""")
rep("""Without sub-pd6 and sub-pd16 the
    uncorrected p is 0.064 to 0.087.""",
"""Without sub-pd6 and sub-pd16 (a
    variant) the uncorrected p is 0.064 to 0.087 and the null holds after FDR correction under all
    three readings.""")
rep("""    40 to 54, p = 0.26 to 0.73.
""","""    40 to 54, p = 0.26 to 0.73. The criterion has no partial clause; partially reproduced follows
    the protocol's definition (the effect is present but weaker), and the question is asked of a
    reader (questions/openneuro-ds002778.yaml).
""")
open(P,'w').write(s)
EOF
grep -n "W = 13 (expected" attempts/openneuro-ds002778-jackson-2019-01.yaml
```

```
31:    signed rank W = 13 (expected 12 +/- 1.2), p = 0.0076 (exact 0.0054), FDR corrected over the
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
P='attempts/openneuro-ds002778-jackson-2019-01.yaml'
ALL="I agree with all 24 outcomes."
NO="No change of outcome."
outcomes={}
import yaml
rec=yaml.safe_load(open(P))
for o in rec['outcomes']: outcomes[o['claim']]=o['outcome']
R={
"fig2-sharpness-off-on":(ALL+" Section 2, item 1 says the summary's \"statistics close to the paper's\" overstates the match, as sharpness d is 0.73 against 0.86.",
  NO+" The summary now says that each of the three main tests holds after FDR correction but has one value outside tolerance, and names them."),
"fig2-steepness-off-on":(ALL+" Section 2, item 1 says steepness W is 16 against the paper's 9, so \"close\" overstates the match.",
  NO+" The summary sentence was corrected as for fig2-sharpness-off-on."),
"fig2-pac-off-on":("Applies the stricter reading of a criterion that contradicts itself; the record says so and puts the question to a reader. The outcome is partially reproduced or reproduced depending on which sentence governs, and it now waits on a reader. Edge-dropping changes PAC by at most 5.1% per recording (ratio 0.9487), not \"5% at most\" as cell 23 and the record say.",
  NO+" Corrected the text to 5.1% (ratio 0.949 to 1.043) and said that the edge-dropping variant was run for the beta test at C3 and C4 only. The question to a reader stands."),
"bipolar-off-on":(ALL+" The summary's claim that the off against on tests keep their significance without sub-pd6 and sub-pd16 is not shown for the bipolar tests.",
  NO+" Added a sensitivity section that runs the three bipolar tests without sub-pd6 and sub-pd16 (FDR corrected p 0.011 to 0.019, all higher off)."),
"temporalis-f7f8-null":(ALL,"No change."),
"temporalis-t7t8-null":(ALL,"No change."),
"fig2c-topography-sensorimotor":("I agree with all 24 outcomes. Cell 34 and the record say that with the code's filters the smallest p is at Fz (0.020), but cell 33 prints Fz and CP6 tied at 0.0199, and CP6 is in the sensorimotor set. The outcome does not change, since sharpness fails either way.",
  NO+" The cell now prints the electrodes tied for the smallest p, and the conclusion and notes say that Fz and CP6 tie."),
"offctrl-sharpness-null":(ALL,"No change."),
"offctrl-steepness":("Now not reproduced, which follows from its criterion. Both non-failing outcomes of the Table 2 claims need the average-reference result to survive FDR correction, and it gives 0.0531 under every reading; Holm, Bonferroni and BY are further from 0.05. The misses are not an artefact of BH.",
  "No change."),
"offctrl-pac-null":(ALL,"No change."),
"offctrl-pac-csd":("The spline variants all miss (p 0.105 to 0.30), but MNE has not been compared with the CSD toolbox. CSD roughly doubles the ratio of 50 to 150 Hz power to beta power at C3/C4, which raises gamma, and the toolbox's output may behave differently. Cell 45 says CSD PAC is \"higher off under every variant\", but the variant rows print p only, so the direction is shown for the main m = 3 CSD only.",
  NO+" The variant table now prints the mean on and the number of patients higher off (12 or 13 of 15, mean off above mean on in every variant), and the conclusion cites them. A comparison with the CSD toolbox was not run: it needs MATLAB, which the locked environment does not hold."),
"updrs-improvement":("I agree with all 24 outcomes. \"Total UPDRS\" read as Part III is a stated judgement and reasonable.","No change."),
"fig1c-beta-alpha-peaks":(ALL,"No change."),
"table1-alpha-shape-off-on":(ALL+" The summary's claim about the variant without sub-pd6 and sub-pd16 is not shown for alpha shape.",
  NO+" The sensitivity section now runs both alpha shape tests without sub-pd6 and sub-pd16 (FDR corrected 0.017 to 0.033, higher off)."),
"table1-alpha-pac-null":("Now not reproduced, which follows from its criterion. The alpha PAC readings disagree (a192 0.0609, b231 0.0783, c118 0.0356; cell 56), and the criterion takes the outcome that all readings give. Under reading c alpha PAC is significant after correction (0.0356) but has uncorrected p 0.064 without the two patients, so not every test keeps its significance, as the summary says.",
  NO+" The summary now says that alpha PAC, significant after correction under one reading with all patients, is not significant under any reading without sub-pd6 and sub-pd16 (0.064 to 0.087), and the notes report it as a variant."),
"table2-alpha-offctrl":("Now not reproduced, which follows from its criterion: the average-reference result gives 0.0531 under every reading, and Holm, Bonferroni and BY are further from 0.05.","No change."),
"pac-beta-larger-than-alpha":("Marked partially reproduced, but its criterion has no partial clause. Partial is a reasonable default (test holds, W 17 to 18 against 9.9 to 12.1), but the claims file does not define it, and should.",
  NO+" Added the missing partial clause as a question for a reader in questions/openneuro-ds002778.yaml and said so in the notes."),
"fig3-sharpness-pac-correlation":(ALL,"No change."),
"fig3-steepness-pac-correlation":("I agree with all 24 outcomes. The exclusion variants show that the steepness-PAC on-medication miss rests on pd6 and pd16.","No change."),
"fig4a-sensorimotor-q4":(ALL,"No change."),
"q4-patient-counts":("I agree with all 24 outcomes; the claims file reads the paper's Q4 counts correctly (C3 9, C4 8, both 8, so 9 with at least one). Artifact rejection remains the likely cause of the Q4 count gap, as 16 of 60 points lie within 0.01 of an axis. Cell 74 lists pd9 among the points that decide membership, but its near-axis points do not; pd5 (C3 on, C4 on) and pd11 (C4 on) do and are not listed.",
  NO+" The cell now finds the near-axis points that decide membership (moving their near-axis coordinates across zero changes whether the patient counts at that electrode): 10 points in pd3, pd5, pd11, pd12, pd22, pd26 and pd28. The conclusion and notes use this list."),
"fig4b-temporalis-variable-shape":(ALL,"No change."),
"controls-q4":(ALL,"No change."),
"table3-q4-effect-size":("I agree with all 24 outcomes. The summary row says \"two values above tolerance\"; that holds under log10 PAC with the Methods' filters, but under raw PAC the all-patient PAC d (0.85, above 0.825) is a third.",
  NO+" The summary row now names the Q4 steepness and PAC d and the raw all-patient PAC d of 0.85 as above tolerance."),
}
assert set(R)==set(outcomes),set(outcomes)^set(R)
def q(t):  # double-quoted YAML scalar
    return '"'+t.replace('\\','\\\\').replace('"','\\"')+'"'
import textwrap
lines=["- date: 2026-10-27","  kind: agent",
"  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)",
"  reviewed: "+q("The full executed notebook of the revised run (cells 0 to 84), the helper module, the claims file and the attempt record, with the paper's full text. The verifier read every printed output, recomputed from the printed per-patient values the variants without pd6 and pd16 (beta sharpness, steepness and PAC, and the Spearman r on and off), recomputed the BH correction for Table 2 from the printed p-values, and checked the Q4 counts in the paper's text. Report in transcripts/openneuro-ds002778/verifier-2-report.md."),
"  results:"]
for o in rec['outcomes']:
    c=o['claim']; r,resp=R[c]
    lines += [f"  - claim: {c}","    agrees: true",f"    outcome: {outcomes[c]}",
              "    reason: "+q(r),"    response: "+q(resp)]
s=open(P).read().rstrip('\n')+'\n'+'\n'.join(lines)+'\n'
open(P,'w').write(s)
d=yaml.safe_load(open(P)); print(len(d['verifications']), len(d['verifications'][1]['results']))
EOF
python tools/entry.py check entries/openneuro-ds002778-jackson-2019 2>&1 | tail -3
```

```
2 24
0 error(s)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re,textwrap,yaml
P='attempts/openneuro-ds002778-jackson-2019-01.yaml'
before=yaml.safe_load(open(P))
out=[]
for line in open(P).read().split('\n'):
    m=re.match(r'^(\s*)(reason|response|reviewed): (".*")$',line)
    if m and len(line)>100:
        ind,key,val=m.groups()
        w=textwrap.wrap(val,width=98-len(ind)-2,break_long_words=False,break_on_hyphens=False)
        out.append(f"{ind}{key}: {w[0]}")
        out += [ind+'  '+x for x in w[1:]]
    else: out.append(line)
open(P,'w').write('\n'.join(out))
assert yaml.safe_load(open(P))==before
print("ok")
EOF
python tools/entry.py check entries/openneuro-ds002778-jackson-2019 2>&1 | tail -1; tail -30 attempts/openneuro-ds002778-jackson-2019-01.yaml; git status --short
```

```
ok
0 error(s)
  - claim: q4-patient-counts
    agrees: true
    outcome: not_reproduced
    reason: "I agree with all 24 outcomes; the claims file reads the paper's Q4 counts correctly (C3 9,
      C4 8, both 8, so 9 with at least one). Artifact rejection remains the likely cause of the Q4
      count gap, as 16 of 60 points lie within 0.01 of an axis. Cell 74 lists pd9 among the points
      that decide membership, but its near-axis points do not; pd5 (C3 on, C4 on) and pd11 (C4 on)
      do and are not listed."
    response: "No change of outcome. The cell now finds the near-axis points that decide membership
      (moving their near-axis coordinates across zero changes whether the patient counts at that
      electrode): 10 points in pd3, pd5, pd11, pd12, pd22, pd26 and pd28. The conclusion and notes
      use this list."
  - claim: fig4b-temporalis-variable-shape
    agrees: true
    outcome: reproduced
    reason: "I agree with all 24 outcomes."
    response: "No change."
  - claim: controls-q4
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd  git diff | grep "^+" | grep -n "—\|rather" ; date -u
```

```
Wed Oct 28 00:00:08 UTC 2026
```

**Agent**

No outcome changed and nothing is proposed. The verifier agreed with all 24 outcomes (9 reproduced, 9 partially reproduced, 6 not reproduced), and I found no reason to propose a change. I re-ran the entry with `python tools/entry.py all`: no errors, the notebook passes in 133 s, and every number is the same as before. `entry.py check` also passes. Nothing is committed.

**Added to the notebook**
- **New sensitivity section before the Summary.** It runs all six off-against-on tests of Table 1, under every filter reading, and the three bipolar tests, each without sub-pd6 and sub-pd16, uncorrected and after FDR correction.
  - Every test keeps its direction.
  - The tests that were significant under every reading stay significant: corrected p 0.017 to 0.033 for Table 1 and 0.011 to 0.019 for the bipolar tests.
  - Alpha PAC is not significant under any reading without the two patients (0.064 to 0.087). With all patients it was significant under one reading (0.036).
- **Topography cell (fig2c):** it now prints electrodes tied for the smallest p. With the code's filters, Fz and CP6 tie at 0.020.
- **CSD variant table:** it now shows the mean on and how many patients are higher off. Every variant is higher off, in 12 or 13 of 15 patients.
- **Q4 cell:** it now works out which near-axis points decide whether a patient counts. There are 10, in pd3, pd5, pd11, pd12, pd22, pd26 and pd28. pd9 is no longer listed, and pd5 and pd11 are added.

**Text corrected**
- **Summary, about the dataset:** it no longer says the statistics are "close to the paper's". It now says each of the three main tests holds but has one value out of tolerance, and names the three values.
- **"Each recording once"** is replaced by: patients recorded off and on, controls once, no recording deposited twice.
- **Summary, Sensitivity paragraph:** it now matches the new outputs. It says the edge-dropping variant was run only for the beta test at C3 and C4.
- **Smaller corrections:**
  - "5%" is now 5.1%.
  - The CSD direction sentence now cites the new numbers.
  - The table3 summary row names the third out-of-tolerance value (raw all-patient PAC d 0.85).
- **Attempt record:** the notes for fig2-pac, fig2c, offctrl-pac-csd, q4-patient-counts, table1-alpha-pac-null and pac-beta-larger-than-alpha were updated to match.

**Recorded**
- Round 2 is under `verifications` in the attempt record, with all 24 claims marked as agreed, the verifier's reasons from the report, and a response for each.
- `questions/openneuro-ds002778.yaml` has a new question for a reader: the criterion for pac-beta-larger-than-alpha has no clause for a partial outcome. The earlier fig2-pac-off-on question is still open.

**Not done**
- **CSD toolbox comparison (offctrl-pac-csd):** not run, because the toolbox needs MATLAB and the locked environment does not have it. The record says so.
- **Artifact rejection:** not possible, because the paper's artifact marks and excluded electrodes are not in the dataset. This is already recorded as a finding.

## End of run

27 turns, 13 minutes, result: success.
