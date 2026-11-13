# laboy-juarez-2019 · author-revise-2 · run 43325911019

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/laboy-juarez-2019/verifier-2-report.md; ls entries/laboy-juarez-2019 entries/laboy-juarez-2019/*; git diff --stat
```

```
Thu Nov 12 23:11:37 UTC 2026
## Round 2 verification: Laboy-Juarez et al. 2019 (CRCNS ssc-9)

The claims file has 50 claims and the attempt record has 50 outcomes: 29 reproduced, 13 partially reproduced, 7 not reproduced and 1 blocked. The README table matches these counts (10/31/9 claims by experiment).

### 1. Outcomes and assumptions

I agree with all 50 stated outcomes. The ones that changed or that I disputed in round 1:

- **fig1e: reproduced (assumed).** I agree. Same-direction sequences give 0.694, 0.851 and 0.456 (cell 33), and sham reading (b) also passes. The assumption is stated and reasonable: the Methods' 261 stimuli are 9 singles plus 36 × 7 sequences, and the experiment 3 stimuli, called identical, are same-direction only. Cell 7 shows the opposite-direction trials are real stimuli with distinct timings, not a coding flip.
- **exp1-cw-sw-comparable-firing, supp4 and fig4c: partially reproduced.** I now agree, and withdraw my round-1 "not reproduced". In round 1 I already gave "partially reproduced" to fig7b, fig7c, fig7e and supp6. Their criteria also name no partial rule, and in each one part holds and another fails. The same standard applies to these three:
  - exp1: spontaneous rates hold, maximal evoked firing fails in the claims file's unit.
  - supp4: the peak test holds, the counts fail.
  - fig4c (reading b): SW-tuned beats CW-tuned at every size; CW-tuned is not above chance at N = 150.
- **fig3g: partially reproduced (assumed).** I agree. Cell 138 gives 0.633 at N = 10 and 0.857 at N = 100, which meets the criterion's partial rule. It is fragile: 0.003 above the band edge, with an s.d. over refits of 0.010.
- **fig7a: partially reproduced (assumed).** I agree. Leaving out sets with a constant best curve is stated and reasonable, since they have no best dt.
- **fig8c: not reproduced.** I agree. Cell 177 gives p = 0.0021, and the criterion's partial rule needs the test to hold.
- **supp8: not reproduced (assumed).** I agree. The mean over fiv
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -80; wc -l docs/protocol.md
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
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cat questions/laboy-juarez-2019.yaml 2>/dev/null | head -100; ls questions | head
```

```
# Questions from attempt laboy-juarez-2019-01 (author-revise, 2026-11-12) about the claims file
# claims/laboy-juarez-2019.yaml. Raised by the round-1 verifier and asked under docs/protocol.md,
# "Hand over for verification"; the claim is tested as written.
questions:
- claim: exp1-cw-sw-comparable-firing
  asked: 2026-11-12
  question: >-
    The claims file takes the paper's maximal evoked firing (4.8 +- 0.48 and 4.56 +- 0.64) in
    spikes per stimulus in the 125 ms window, as the text prints it, and names two readings of
    "maximal" in that unit. Should the expected values instead be read as a rate in Hz over the
    125 ms window (count / 0.125 s), the unit of the spontaneous rates in the same sentence?
  passage: >-
    Results, "Single-whisker receptive fields in each S1 column": "CW-tuned and SW-tuned neurons
    had comparable spontaneous activity (1.28 ± 0.24 Hz and 2.08 ± 0.4 Hz, respectively) and
    maximal evoked firing (4.8 ± 0.48 spikes per stimulus and 4.56 ± 0.64 spikes per stimulus,
    respectively)". The round-1 verifier reports that the axes of Fig. 1d, which plots best
    single-whisker against best-sequence responses in spikes per stimulus, end near 4, so a mean
    over units of 4.8 spikes per stimulus would not fit that figure.
  why: >-
    In spikes per stimulus the attempt measures 0.58 and 0.60 (best single whisker) and 0.86 and
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 199,215p docs/protocol.md; sed -n 431,676p docs/protocol.md
```

````
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
### 4. Lock, check and run

```bash
[... 243 more lines not kept]
````

**Agent calls Bash**

```bash
ls attempts | grep laboy; wc -l attempts/laboy-juarez-2019-01.yaml; grep -n "^[a-z]" attempts/laboy-juarez-2019-01.yaml; grep -n "verifications" -A60 attempts/laboy-juarez-2019-01.yaml | head -120
```

```
laboy-juarez-2019-01.yaml
1296 attempts/laboy-juarez-2019-01.yaml
1:schema_version: 3
2:id: laboy-juarez-2019-01
3:datasets:
9:paper: doi:10.1038/s41593-019-0448-6
10:date: '2026-11-12'
11:entry: laboy-juarez-2019
12:provenance:
23:outcomes:
888:findings:
946:verifications:
946:verifications:
947-- date: '2026-11-12'
948-  kind: agent
949-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
950-  reviewed: 'Round 1: the first executed notebook with the conclusion cells and the summary removed, the
951-    helper module and the claims file, with the paper''s full text. The verifier checked the archive''s
952-    S3 listing and filelist.txt, and tested the shuffle test, the dt smoothing and the decoder helpers
953-    on synthetic Poisson units. It had no attempt record.'
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^- date\|  reviewed\|  results\|  problems\|  remaining\|^  [a-z_]*:" attempts/laboy-juarez-2019-01.yaml | sed -n 1,200p | awk -F: '$1>880'; sed -n 1240,1296p attempts/laboy-juarez-2019-01.yaml
```

```
reason: 0.581 and 0.570 at N = 100, against a bound of 0.585. The selective-set miss (0.004) is within
      Monte Carlo error (s.e. about 0.0065), so this outcome is fragile (B6).
    response: 'Now the mean of five refits with 10,000 ensembles each: 0.584 (refits 0.580 to 0.589),
      still below 0.585. Outcome kept as not reproduced, with the notes saying it is fragile; on the 187
      sets with the smallest p it is 0.595, within tolerance, so the outcome is marked as resting on the
      selective group.'
  - claim: exp3-units-cw-tuned
    agrees: true
    outcome: reproduced
    reason: 81 units, 74 responsive, 46 CW-tuned; mean single-whisker tuning is largest at the CW.
    response: No change.
  - claim: fig8c-awake-cw-stronger
    agrees: false
    outcome: not_reproduced
    reason: Ratio 1.71 is within tolerance and the awake tuning is sharper, but t-test p = 0.0021, not
      < 0.001.
    response: 'Changed to not reproduced: the criterion''s partial rule needs the test to hold, which
      it does not.'
  - claim: fig8d-awake-best-sequence
    agrees: true
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
ls tools; grep -rn "verifications" tools/*.py | head -20
```

```
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
entry.py
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 320,400p tools/entry.py; ls schemas 2>/dev/null; grep -rln "proposed" schemas tools/*.py 2>/dev/null
```

```
for claim in sorted(known - set(recorded)):
            if not reread:
                report.error(where, f"claim {claim!r} has no outcome; give every claim one, blocked included")
        for claim in sorted({c for c in recorded if recorded.count(c) > 1}):
            report.error(where, f"claim {claim!r} has more than one outcome")
        # A finding is about the data (its dataset's page) or the paper (the paper's page). Its kind says which,
        # except for these two kinds, which must say; and in an attempt on several datasets a finding about the data
        # names the datasets it is about (docs/protocol.md, the attempt record).
        import datasets as archive_datasets
        used = [archive_datasets.folder(archive_datasets.key_of(d["archive"], str(d["id"])))
                for d in attempt.get("datasets") or ([attempt["dataset"]] if attempt.get("dataset") else [])]
        for n, f in enumerate(attempt.get("findings") or [], 1):
            if f.get("kind") in ("other", "selection_undocumented") and not f.get("about"):
                report.error(where, f"finding {n} ({f.get('kind')}): say what it is about, `about: data` or `about: paper`")
            about = f.get("about") or ("paper" if f.get("kind") in ("methods_unavailable", "code_mismatch",
                                                                   "paper_inconsistency") else "data")
            if about == "data" and len(used) > 1 and not f.get("datasets"):
                report.error(where, f"finding {n}: the attempt used {len(used)} datasets; name the ones it is about "
                                    f"(`datasets:`, from {', '.join(used)})")
            for d in f.get("datasets") or []:
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
def find(o,k,p=''):
  if isinstance(o,dict):
    for kk,v in o.items():
      if kk==k: print(p+'/'+kk, json.dumps(v)[:1500])
      find(v,k,p+'/'+kk)
  elif isinstance(o,list):
    for i,v in enumerate(o): find(v,k,p+f'[{i}]')
find(s,'verifications');find(s,'proposed')"
```

```
/properties/verifications {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["date", "kind", "by", "results"], "properties": {"date": {"type": "string", "format": "date"}, "kind": {"enum": ["agent", "person", "paper_author"]}, "by": {"type": "string"}, "results": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["claim", "agrees"], "properties": {"claim": {"type": "string"}, "agrees": {"type": "boolean"}, "reason": {"description": "The verifier's reason, in its own words.", "type": "string"}, "response": {"description": "What the author changed or replied, kept apart from the verifier's reason.", "type": "string"}, "outcome": {"description": "The outcome the verifier would give.", "enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}}}}, "reviewed": {"description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.", "type": "string"}}}}
/properties/outcomes/items/properties/proposed {"description": "A change of outcome found after the last verification round, held until a further round agrees with it.", "type": "object", "additionalProperties": false, "required": ["outcome", "reason"], "properties": {"outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}, "reason": {"type": "string", "minLength": 1}}}
```

**Agent calls Bash**

```bash
ls -la executed/laboy-juarez-2019/ 2>/dev/null; cat executed/laboy-juarez-2019/*.json 2>/dev/null | head -30; wc -l entries/laboy-juarez-2019/lj2019.py; cat entries/laboy-juarez-2019/entry.yaml
```

```
total 276
drwxr-xr-x 3 runner runner   4096 Nov 12 22:58 .
drwxr-xr-x 3 runner runner   4096 Nov 12 23:11 ..
-rw-r--r-- 1 runner runner    329 Nov 12 22:58 .clean-run.json
drwxr-xr-x 5 runner runner   4096 Nov 12 22:26 .venv
-rw-r--r-- 1 runner runner 258195 Nov 12 22:58 reproduce_laboy_juarez_2019.ipynb
-rw-r--r-- 1 runner runner    183 Nov 12 22:58 result.json
{
 "entry": "laboy-juarez-2019",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_laboy_juarez_2019.ipynb",
   "ok": true,
   "seconds": 1929,
   "error": null
  }
 ]
}
565 entries/laboy-juarez-2019/lj2019.py
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; python - <<'E'
import nbformat
nb=nbformat.read('../../executed/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb',4)
for i,c in enumerate(nb.cells):
    if 140<=i<=200:
        src=c.source
        print(f'=== {i} {c.cell_type} {c.metadata.get("tags",[])}'); print(src[:1500])
        if c.cell_type=='code':
            for o in c.get('outputs',[]):
                t=o.get('text') or o.get('data',{}).get('text/plain','')
                print('--> ',t[:1500])
E
```

```
<persisted-output>
Output too large (44.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/db400862-4b2f-4757-9d59-5ea9df2863bd/tool-results/btmo61vvd.txt

Preview (first 2KB):
=== 140 markdown []
### fig4c-sw-tuned-decoding

> Combination identity was decoded from SW-tuned units more accurately and efficiently than from CW-tuned units, and decoding from CW-tuned units was still above chance.
=== 141 code ['claim:fig4c-sw-tuned-decoding']
def run_fig4c_sw_tuned_decoding(M2):
    rng_4c = np.random.default_rng(4)
    rows = []
    for lab, base in [("(a) selective", M2.sel.to_numpy()), ("(b) all", np.ones(len(M2), bool))]:
        for grp, gm in [("SW-tuned", ~M2.cw_tuned_a.to_numpy()), ("CW-tuned", M2.cw_tuned_a.to_numpy())]:
            idx = members(base & gm)
            r_ = dict(units=lab, group=grp, n=len(idx))
            for N in [10, 25, 50, 100, 150]:
                acc = POOL.accuracy(N, 2500, rng_4c, idx).mean(1)
                r_[f"N{N}"] = acc.mean()
                if N == 150:
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/db400862-4b2f-4757-9d59-5ea9df2863bd/tool-results/btmo61vvd.txt"
}
```

```
1	=== 140 markdown []
2	### fig4c-sw-tuned-decoding
3	
4	> Combination identity was decoded from SW-tuned units more accurately and efficiently than from CW-tuned units, and decoding from CW-tuned units was still above chance.
5	=== 141 code ['claim:fig4c-sw-tuned-decoding']
6	def run_fig4c_sw_tuned_decoding(M2):
7	    rng_4c = np.random.default_rng(4)
8	    rows = []
9	    for lab, base in [("(a) selective", M2.sel.to_numpy()), ("(b) all", np.ones(len(M2), bool))]:
10	        for grp, gm in [("SW-tuned", ~M2.cw_tuned_a.to_numpy()), ("CW-tuned", M2.cw_tuned_a.to_numpy())]:
11	            idx = members(base & gm)
12	            r_ = dict(units=lab, group=grp, n=len(idx))
13	            for N in [10, 25, 50, 100, 150]:
14	                acc = POOL.accuracy(N, 2500, rng_4c, idx).mean(1)
15	                r_[f"N{N}"] = acc.mean()
16	                if N == 150:
17	                    r_["sd150"] = acc.std()
18	            rows.append(r_)
19	    print(pd.DataFrame(rows).to_string(index=False, float_format=fmt))
20	
[... 629 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; python - <<'E'
import nbformat,re
nb=nbformat.read('../../executed/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb',4)
for i,c in enumerate(nb.cells):
    txt=c.source+''.join((o.get('text') or '') for o in c.get('outputs',[]))
    if re.search(r'M2v|162|calibrat|null', txt):
        print(f'=== {i} {c.cell_type}'); print(c.source[:2500])
        for o in c.get('outputs',[]):
            print('--> ',(o.get('text') or '')[:2000])
E
```

```
<persisted-output>
Output too large (35.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/db400862-4b2f-4757-9d59-5ea9df2863bd/tool-results/bj93j17uz.txt

Preview (first 2KB):
=== 4 code
from scipy import stats
import matplotlib.pyplot as plt
pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 30)
for e, (U, T) in {1: (U1, T1), 2: (U2, T2), 3: (U3, T3)}.items():
    print(f"=== Experiment {e}: {U.file.nunique()} files, {len(T)} recordings (distinct trial sequences), {len(U)} units")
    rows = []
    for rec, tab in T.items():
        kc = tab.kind.value_counts()
        rows.append(dict(recording=rec, units=int((U.recording == rec).sum()), trials=len(tab),
                         single=kc.get("single", 0), cwsw=kc.get("cwsw", 0), swsw=kc.get("swsw", 0),
                         triple=kc.get("triple", 0), sham=kc.get("sham", 0),
                         dt_values=tab.loc[tab.kind == "cwsw", "dt"].nunique(),
                         dt_min=tab.loc[tab.kind == "cwsw", "dt"].min(), dt_max=tab.loc[tab.kind == "cwsw", "dt"].max(),
                         trial_ms=L.trial_length(U, rec) if e != 3 else np.nan))
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^=== \|calibrat\|M2v\|162" /home/runner/.claude/projects/-home-runner-work-encore-encore/db400862-4b2f-4757-9d59-5ea9df2863bd/tool-results/bj93j17uz.txt | head -80
```

```
1:=== 4 code
32:20170515:486086     14   25999    2340  5162 18367       0   130          7   -50.0    50.0     500.0
41:=== Experiment 2: 12 files, 16 recordings (distinct trial sequences), 247 units
55:20160829:6066e9      8   54247    5396 16263  8015   24273   300        101   -50.0    50.0     600.0
61:=== 11 code
96:   2 20160803:233bcd     13    2162        0.119       0.162         0.160
107:=== 58 markdown
108:Calibration of the test on the real data (the verifier's request). For each responsive set, the counts are permuted across the eight combinations within each dt, which removes combination tuning and keeps everything else, and the whole test is run on the result: kernels chosen again by cross-validation on the permuted counts, then the shuffles (1000 here, to keep the run short) and the Mahalanobis p-value. A calibrated test gives p < 0.05 for about 5% of these sets. The measured p-values are then calibrated on this null distribution (the share of null p-values at or below each), and a group of the paper's size, the 187 sets with the smallest p, is defined for the variant section below.
109:=== 59 code
125:print(f"measured p calibrated on the null p: calibrated p < 0.05 for {int(np.sum(p_cal < 0.05))} sets; selective after FDR: {int(L.bh(p_cal).sum())} "
126:      f"(the null's floor of 1/1001 limits how small a calibrated p can be)")
137:measured p calibrated on the null p: calibrated p < 0.05 for 219 sets; selective after FDR: 162 (the null's floor of 1/1001 limits how small a calibrated p can be)
140:=== 60 markdown
141:**Result: not reproduced.** The shuffle test finds 318 of 463 responsive sets combination-selective (FDR over all sets; 312 with the two sets apart), in 189 of 246 cells (0.768), against 187 sets and 129 cells (0.52). The fractions are 0.641 and 0.733 of the responsive correlated and anti-correlated sets, or 0.602 and 0.691 of all cells, against 0.35 and 0.46. The test is not calibrated here: on the real-data null it gives p < 0.05 f
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 105,180p /home/runner/.claude/projects/-home-runner-work-encore-encore/db400862-4b2f-4757-9d59-5ea9df2863bd/tool-results/bj93j17uz.txt
```

```
3 20181114:be5c61     14     770        0.122       0.230         0.156
   3 20190123:4f1cce     11     641        0.123  
=== 58 markdown
Calibration of the test on the real data (the verifier's request). For each responsive set, the counts are permuted across the eight combinations within each dt, which removes combination tuning and keeps everything else, and the whole test is run on the result: kernels chosen again by cross-validation on the permuted counts, then the shuffles (1000 here, to keep the run short) and the Mahalanobis p-value. A calibrated test gives p < 0.05 for about 5% of these sets. The measured p-values are then calibrated on this null distribution (the share of null p-values at or below each), and a group of the paper's size, the 187 sets with the smallest p, is defined for the variant section below.
=== 59 code
t0 = time.time()
rng_null = np.random.default_rng(20190804)
p_null = []
for _, r in R2.iterrows():
    d = CUR[(r.unit, r.set)]
    y0 = L.permute_within_dt(d["y"], d["comb"], d["dti"], rng_null)
    p_null.append(L.shuffle_test(y0, d["comb"], d["dti"], rng_null, KER, n_shuf=1000)[0])
p_null = np.array(p_null)
print(f"real-data null, {len(p_null)} sets ({time.time() - t0:.0f} s): p < 0.05 for {np.mean(p_null < 0.05):.3f}, p < 0.01 for {np.mean(p_null < 0.01):.3f}, "
      f"p at its floor (1/1001) for {np.mean(p_null <= 1 / 1001):.3f}; selective after FDR: {int(L.bh(p_null).sum())}")
edges = [0, 0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0001]
print("histogram of p by bin", [f"{a}-{b:.3g}" for a, b in zip(edges[:-1], edges[1:])])
print("   measured:", np.histogram(R2.p_shuffle, edges)[0].tolist())
print("   null:    ", np.histogram(p_null, edges)[0].tolist())
p_cal = np.array([(1 + np.sum(p_null <= p)) / (1 + len(p_null)) for p in R2.p_shuffle])
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; python - <<'E'
import nbformat
nb=nbformat.read('reproduce_laboy_juarez_2019.ipynb',4)
print(len(nb.cells))
for i in [59,60,62,149,169,170,195]:
    print('===',i,nb.cells[i].cell_type, nb.cells[i].metadata); print(nb.cells[i].source[-3000:])
E
```

```
196
=== 59 code {'tags': ['claim:exp2-combination-selective-prevalence']}
t0 = time.time()
rng_null = np.random.default_rng(20190804)
p_null = []
for _, r in R2.iterrows():
    d = CUR[(r.unit, r.set)]
    y0 = L.permute_within_dt(d["y"], d["comb"], d["dti"], rng_null)
    p_null.append(L.shuffle_test(y0, d["comb"], d["dti"], rng_null, KER, n_shuf=1000)[0])
p_null = np.array(p_null)
print(f"real-data null, {len(p_null)} sets ({time.time() - t0:.0f} s): p < 0.05 for {np.mean(p_null < 0.05):.3f}, p < 0.01 for {np.mean(p_null < 0.01):.3f}, "
      f"p at its floor (1/1001) for {np.mean(p_null <= 1 / 1001):.3f}; selective after FDR: {int(L.bh(p_null).sum())}")
edges = [0, 0.001, 0.01, 0.05, 0.1, 0.2, 0.5, 1.0001]
print("histogram of p by bin", [f"{a}-{b:.3g}" for a, b in zip(edges[:-1], edges[1:])])
print("   measured:", np.histogram(R2.p_shuffle, edges)[0].tolist())
print("   null:    ", np.histogram(p_null, edges)[0].tolist())
p_cal = np.array([(1 + np.sum(p_null <= p)) / (1 + len(p_null)) for p in R2.p_shuffle])
print(f"measured p calibrated on the null p: calibrated p < 0.05 for {int(np.sum(p_cal < 0.05))} sets; selective after FDR: {int(L.bh(p_cal).sum())} "
      f"(the null's floor of 1/1001 limits how small a calibrated p can be)")
order = np.lexsort((-R2.maha.to_numpy(), R2.p_shuffle.to_numpy()))
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; python - <<'E'
import nbformat,datetime as D
nb=nbformat.read('../../executed/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb',4)
def t(c):
    m=c.metadata.get('execution',{})
    a,b=m.get('iopub.execute_input'),m.get('shell.execute_reply')
    if a and b: return (D.datetime.fromisoformat(b.replace('Z',''))-D.datetime.fromisoformat(a.replace('Z',''))).total_seconds()
tot=0
for i in range(150,170):
    s=t(nb.cells[i]); tot+=s or 0; print(i,s)
print(tot)
E
```

```
150 0.286444
151 0.008911
152 0.021901
153 0.013735
154 0.004601
155 0.008931
156 1.08184
157 0.024077
158 0.075422
159 0.021118
160 0.029266
161 0.041342
162 0.033912
163 0.013725
164 0.032482
165 0.716445
166 13.715239
167 1.199523
168 27.578178
169 11.578381
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "237 to 240\|236\|mostly reproduce\|fragile\|band edge" attempts/laboy-juarez-2019-01.yaml entries/laboy-juarez-2019/README.md; python - <<'E'
import nbformat
nb=nbformat.read('entries/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb',4)
for i,c in enumerate(nb.cells):
    if '237 to 240' in c.source or 'fragile' in c.source or 'mostly reproduce' in c.source: print(i, c.source[:1500]); print()
E
```

```
attempts/laboy-juarez-2019-01.yaml:238:    and 232 to anti-correlated stimuli under O2 (a) and sham (a), and 237 to 240 under the other readings,
attempts/laboy-juarez-2019-01.yaml:464:    band''s edge with an s.d. over refits of 0.010, so the outcome is fragile. On the 187 sets with the
attempts/laboy-juarez-2019-01.yaml:583:    at the lower edge of 0.08 +- 0.008, so the outcome is fragile; over all 463 sets 0.093, and under
attempts/laboy-juarez-2019-01.yaml:773:    band by 0.001, so the outcome is fragile. On the 187 sets with the smallest p it is 0.595, within
attempts/laboy-juarez-2019-01.yaml:1128:      to 0.77, s.d. over refits 0.010) and N = 100 0.857 (above 0.81, not 0.9). The outcome is fragile
attempts/laboy-juarez-2019-01.yaml:1241:      Monte Carlo error (s.e. about 0.0065), so this outcome is fragile (B6).
attempts/laboy-juarez-2019-01.yaml:1243:      still below 0.585. Outcome kept as not reproduced, with the notes saying it is fragile; on the 187
entries/laboy-juarez-2019/README.md:20:preference and the awake results mostly reproduce. The shuffle test of combination selectivity
51 **Result: reproduced.** The files hold 247 units in 12 mice (246 after dropping a duplicated unit); under direction reading (a) and sham reading (a), 231 are responsive to correlated and 232 to anti-correlated stimuli, within tolerance of 224 and 227; the other three readings give 237 to 240, also within tolerance.

139 **Result: partially reproduced.** Averaged over three refits of the held-out probabilities with 10,000 ensembles each, the best-against-suboptimal decoder over the selective sets reaches 0.633 (reading a) and 0.628 (reading b) at N = 10, and 0.857 and 0.832 at N = 100; over all sets 0.607 and 0.601 at N = 10. Under readings (a) and (c), accuracy at N = 10 is within the tolerance band (0.63 to 0.77) and accuracy at N = 100 is above 0.81 but not above 0.9. The N = 10 value is 0.003 above the band's edge, with an s.d. over refits of 0.010, so the outcome is fra
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; python - <<'E'
import nbformat
nb=nbformat.read('reproduce_laboy_juarez_2019.ipynb',4)
print(nb.cells[138].source)
for i in [35,36,37,38,100,101,102,103]:
    pass
E
grep -n "frac_supralinear\|def run_supralinear" -n reproduce_laboy_juarez_2019.ipynb | head
```

```
def binary_pool(rows_, mode, rng):
    probs, labs = [], []
    for i, r in rows_.iterrows():
        x, y = unit_trials(r)
        best = y == r.c_best
        if mode == "a":  # suboptimal trials pooled over the seven, as many as best trials
            sub = rng.choice(np.where(~best)[0], best.sum(), replace=best.sum() > (~best).sum())
        else:  # one suboptimal combination drawn at random
            c2 = rng.choice([c for c in range(8) if c != r.c_best])
            sub = np.where(y == c2)[0]
        ii = np.r_[np.where(best)[0], sub]
        lab = np.r_[np.ones(best.sum(), int), np.zeros(len(sub), int)]
        P = L.heldout_prob_rows(x[ii], lab, 2, rng)
        probs.append(P); labs.append(lab)
    return L.Pool(probs, labs, 2)
def run_fig3g_binary_decoder(M2):
    rng_3g = np.random.default_rng(32)
    rows = []
    for units_lab, rows_ in [("(c) selective", M2[M2.sel]), ("(d) all", M2)]:
        for mode in "ab":
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; python - <<'E'
import nbformat
nb=nbformat.read('reproduce_laboy_juarez_2019.ipynb',4)
for i in [136,137,139,146]: print('===',i,nb.cells[i].cell_type,nb.cells[i].metadata);print(nb.cells[i].source[:800])
E
```

```
=== 136 markdown {}
**Result: not reproduced.** The summed-probability decoder reaches 0.145 at N = 187 selective sets (chance 0.125), against 0.42; it reports the rostral within-row combination for nearly every stimulus (accuracy 0.987 for that combination, 0 to 0.059 for the others, against 0.82 and 0.23 to 0.28 for the dorsal row). The linear-prediction decoder is lower by 0.013, less than the sum of the two s.d. (0.096).
=== 137 markdown {}
### fig3g-binary-decoder

> A binary decoder discriminating each unit's best CW-SW combination from suboptimal combinations reached 70% accuracy for 10 neurons and over 90% for 100.
=== 139 markdown {}
**Result: partially reproduced.** Averaged over three refits of the held-out probabilities with 10,000 ensembles each, the best-against-suboptimal decoder over the selective sets reaches 0.633 (reading a) and 0.628 (reading b) at N = 10, and 0.857 and 0.832 at N = 100; over all sets 0.607 and 0.601 at N = 10. Under readings (a) and (c), accuracy at N = 10 is within the tolerance band (0.63 to 0.77) and accuracy at N = 100 is above 0.81 but not above 0.9. The N = 10 value is 0.003 above the band's edge, with an s.d. over refits of 0.010, so the outcome is fragile; over the 187 sets with the smallest p (variant section) the decoder reaches 0.670 and 0.914.
=== 146 markdown {}
### supp8-order-decoding

> A population decoder of sequence order (dt in -50 to -10 against +10 to +50 ms) from best-combination responses was about 65% correct for 100 units, against chance of 50%.
```

**Agent**

Now the notebook edits: the calibrated group, a new section running every selective-group claim on it, and a band-edge check with more refits.

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; python - <<'E'
import nbformat
p='reproduce_laboy_juarez_2019.ipynb'
nb=nbformat.read(p,4)
c=nb.cells
# calibrated group
old='''order = np.lexsort('''
assert old in c[59].source
c[59].source=c[59].source.replace(old,'''CAL = L.bh(p_cal)  # the calibrated group: FDR on the calibrated p-values
print(f"calibrated group: {int(CAL.sum())} sets, correlated {int((R2.set[CAL] == 'corr').sum())}, anti-correlated {int((R2.set[CAL] == 'anti').sum())}, "
      f"cells {R2.unit[CAL].nunique()}; in the uncalibrated selective group {int((CAL & SEL).sum())}")
order = np.lexsort(''',1)
old='M2v = M2.assign(sel=TOP187)  # the variant group of the paper\'s size\n'
assert old in c[62].source
c[62].source=c[62].source.replace(old, old+'M2c = M2.assign(sel=CAL)  # the calibrated group, from the real-data null\n')
# supp8: factor out the pool so the band-edge check can reuse it (same draws as before)
s=c[147].source
old='''            probs, labs = [], []
            for i, r in rows_.iterrows():
                d = CUR[(r.unit, r.set)]
                dt_ = d["dti"] - 50
                m = (d["comb"] == r.c_best) & (np.abs(dt_) >= 10)
                lab_ = (dt_[m] > 0).astype(int)
                probs.append(L.heldout_prob_rows(d["y"][m], lab_, 2, rng_s8)); labs.append(lab_)
            pool = L.Pool(probs, labs, 2)
'''
assert old in s
s=s.replace(old,'''            pool = order_pool(rows_, rng_s8)
''')
s='''def order_pool(rows_, rng):
    probs, labs = [], []
    for i, r in rows_.iterrows():
        d = CUR[(r.unit, r.set)]
        dt_ = d["dti"] - 50
        m = (d["comb"] == r.c_best) & (np.abs(dt_) >= 10)
        lab_ = (dt_[m] > 0).astype(int)
        probs.append(L.heldout_prob_rows(d["y"][m], lab_, 2, rng)); labs.append(lab_)
    return L.Pool(probs, labs, 2)
'''+s
c[147].source=s
# calibrated-group section after cell 170
names=[]
for i in range(150,170):
    src=c[i].source.splitlines()[1]
    names.append((src.split('(')[0], c[i].metadata['tags'][0]))
new=[nbformat.v4.new_markdown_cell('''## Selective-group claims on the calibrated group

The round-2 verifier asked for the selective-group claims on the group that the calibration gives, which does not fix its size at the paper's. Here the selective group is the 162 sets selected by FDR on the p-values calibrated on the real-data null (`M2c`, see exp2-combination-selective-prevalence); the nonselective group is the other 301. The code is that of each claim's section above.''')]
for fn, tag in names:
    claim=tag.split(':',1)[1]
    new.append(nbformat.v4.new_code_cell(f'print("{claim}, the calibrated group of 162 sets:")\n{fn}(M2c)', metadata={'tags':[tag]}))
new.append(nbformat.v4.new_markdown_cell('**Result of the calibrated-group section.** TO BE WRITTEN'))
# band-edge check
new.append(nbformat.v4.new_markdown_cell('''## Band-edge checks with more refits

Two decoder outcomes lie within one s.d. over refits of a band edge: fig3g-binary-decoder (0.633 at N = 10 against a lower bound of 0.63) and supp8-order-decoding (0.584 at N = 100 against 0.585). Each is run here again on the selective sets with 20 refits of the held-out probabilities (new random draws, 10,000 ensembles each), so that the mean has a standard error near 0.002. fig3g uses reading (a) at N = 10; supp8 uses N = 100.'''))
new.append(nbformat.v4.new_code_cell('''rng_edge = np.random.default_rng(2020)
for claim, make, N, edge in [("fig3g-binary-decoder, reading (a), N = 10", lambda: binary_pool(M2[M2.sel], "a", rng_edge), 10, 0.63),
                             ("supp8-order-decoding, N = 100", lambda: order_pool(M2[M2.sel], rng_edge), 100, 0.585)]:
    reps = np.array([make().accuracy(N, 10000, rng_edge).mean(1).mean() for _ in range(20)])
    se = reps.std(ddof=1) / np.sqrt(len(reps))
    print(f"{claim}: mean over 20 refits {reps.mean():.4f} (s.e. {se:.4f}, range {reps.min():.3f} to {reps.max():.3f}); "
          f"band edge {edge}, difference {reps.mean() - edge:+.4f} = {(reps.mean() - edge) / se:+.1f} s.e.")''', metadata={'tags':['claim:fig3g-binary-decoder','claim:supp8-order-decoding']}))
new.append(nbformat.v4.new_markdown_cell('**Result of the band-edge checks.** TO BE WRITTEN'))
nb.cells=c[:171]+new+c[171:]
nbformat.write(nb,p)
print(names)
E
```

```
[('run_fig2f_shuffle_abolishes_tuning', 'claim:fig2f-shuffle-abolishes-tuning'), ('run_fig2f_most_selective_lower_firing', 'claim:fig2f-most-selective-lower-firing'), ('run_supp4_selectivity_at_high_rates', 'claim:supp4-selectivity-at-high-rates'), ('run_fig3b_sharper_in_both_groups', 'claim:fig3b-sharper-in-both-groups'), ('run_fig3b_linear_sharper_in_selective', 'claim:fig3b-linear-sharper-in-selective'), ('run_supp6_layers', 'claim:supp6-layers'), ('run_supralinear_best_8_percent', 'claim:supralinear-best-8-percent'), ('run_fig6b_best_above_worst_below_scaled', 'claim:fig6b-best-above-worst-below-scaled'), ('run_fig6b_enhancement_not_different', 'claim:fig6b-enhancement-not-different'), ('run_fig6b_suppression_greater_selective', 'claim:fig6b-suppression-greater-selective'), ('run_fig6c_enhancement_strongest_sw', 'claim:fig6c-enhancement-strongest-sw'), ('run_fig7a_dt_half_width', 'claim:fig7a-dt-half-width'), ('run_fig7b_inbound_best_outbound_suboptimal', 'claim:fig7b-inbound-best-outbound-suboptimal'), ('run_fig7e_pc1_best_suboptimal', 'claim:fig7e-pc1-best-suboptimal'), ('run_fig7f_inbound_sharper', 'claim:fig7f-inbound-sharper'), ('run_fig3e_identity_decoder', 'claim:fig3e-identity-decoder'), ('run_fig3g_binary_decoder', 'claim:fig3g-binary-decoder'), ('run_fig4c_sw_tuned_decoding', 'claim:fig4c-sw-tuned-decoding'), ('run_fig7g_inbound_decoding', 'claim:fig7g-inbound-decoding'), ('run_supp8_order_decoding', 'claim:supp8-order-decoding')]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; python - <<'E'
import nbformat
nb=nbformat.read('reproduce_laboy_juarez_2019.ipynb',4)
for i,c in enumerate(nb.cells[:62]):
    if 'SEL =' in c.source or 'SEL=' in c.source: print(i)
E
sed -n 10,30p README.md
```

```
57
|---|---|---|---|---|---|
| 1, anesthetized survey | 10 | 9 | 1 | 0 | 0 |
| 2, dense dt mapping | 31 | 14 | 11 | 6 | 0 |
| 3, awake mice | 9 | 6 | 1 | 1 | 1 |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The unit counts of all three experiments match the paper. Single-whisker tuning, the preference
for CW-SW sequences, sublinear integration with near-linear best combinations, the inbound order
preference and the awake results mostly reproduce. The shuffle test of combination selectivity
finds more selective response sets than the paper (318 of 463, against 187 of 451) and, on a
null built from the real data, gives p < 0.05 for a quarter of the sets; every claim on the
selective group is also run on the 187 sets with the smallest p, which changes the outcome
of four claims, and of a fifth under one reading.
The dt smoothing classifies curves differently, and the population decoders of combination identity
and order fall short of the paper's accuracies. The paper's analysis code is available only on
request, so these methods rest on the Methods text. The behavioral claim is blocked: the files
hold no lick times.
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; python - <<'E'
import nbformat
p='reproduce_laboy_juarez_2019.ipynb'
nb=nbformat.read(p,4)
c=nb.cells
a='the other three readings give 237 to 240'
assert a in c[51].source
c[51].source=c[51].source.replace(a,'the other three readings give 236 to 240')
s=c[-1].source
a='| fig1e-best-combination-includes-cw | reproduced (assumption: caudal singles) |'
assert a in s
c[-1].source=s.replace(a,'| fig1e-best-combination-includes-cw | reproduced (assumption: same-direction sequences) |')
nbformat.write(nb,p)
E
date -u; cd  && timeout 7000 python tools/entry.py all entries/laboy-juarez-2019 2>&1 | tail -20; date -u
```

```
Thu Nov 12 23:13:19 UTC 2026
Installed kernelspec registry-laboy-juarez-2019 in executed/laboy-juarez-2019/.venv/share/jupyter/kernels/registry-laboy-juarez-2019
0 error(s)
pass  reproduce_laboy_juarez_2019.ipynb  (2033 s)
Thu Nov 12 23:47:25 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import nbformat
nb=nbformat.read('executed/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb',4)
for i in [59,62,138,147]+list(range(171,196)):
    c=nb.cells[i]
    if c.cell_type!='code': continue
    print('===',i,c.source.splitlines()[0][:80])
    for o in c.get('outputs',[]):
        print((o.get('text') or o.get('data',{}).get('text/plain',''))[:2500])
E
```

```
=== 59 t0 = time.time()
real-data null, 463 sets (306 s): p < 0.05 for 0.246, p < 0.01 for 0.076, p at its floor (1/1001) for 0.013; selective after FDR: 0
histogram of p by bin ['0-0.001', '0.001-0.01', '0.01-0.05', '0.05-0.1', '0.1-0.2', '0.2-0.5', '0.5-1']
   measured: [147, 92, 101, 32, 40, 46, 5]
   null:     [6, 29, 79, 83, 105, 129, 32]
measured p calibrated on the null p: calibrated p < 0.05 for 219 sets; selective after FDR: 162 (the null's floor of 1/1001 limits how small a calibrated p can be)
calibrated group: 162 sets, correlated 68, anti-correlated 94, cells 111; in the uncalibrated selective group 162
variant group of the paper's size: the 187 sets with the smallest p (ties broken by the larger Mahalanobis distance); largest p in it 0.0032; sets at the smallest p (0.00020): 106; correlated 74, anti-correlated 113, cells 130

=== 62 def derive(R):
463 sets; 318 selective; 90 with a constant best-combination curve

=== 138 def binary_pool(rows_, mode, rng):
        units suboptimal  n_units    N10  N10_sd_over_refits   N100  N100_sd_over_refits
(c) selective          a      318 0.6332            0.009615  0.857              0.01522
(c) selective          b      318 0.6283             0.01044 0.8324              0.01699
      (d) all          a      463 0.6065            0.003062 0.7985              0.01203
      (d) all          b      463 0.6007            0.003573 0.7746             0.008154
Monte Carlo s.e. of one mean over 10,000 ensembles is about s.d. / 100 (the s.d. over ensembles is about 0.3 at N = 10)

[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
c=yaml.safe_load(open('claims/laboy-juarez-2019.yaml'))
cl=c['claims']
want=['supp4-selectivity-at-high-rates','fig7a-dt-half-width','fig3g-binary-decoder','supp8-order-decoding','fig6b-enhancement-not-different','supralinear-best-8-percent','fig4c-sw-tuned-decoding','supp6-layers','fig7f-inbound-sharper','fig2f-shuffle-abolishes-tuning','fig7e-pc1-best-suboptimal','fig7b-inbound-best-outbound-suboptimal','fig6b-suppression-greater-selective']
for x in cl:
    if x['id'] in want:
        print('#####',x['id']); print(yaml.safe_dump({k:v for k,v in x.items() if k in ('statement','expected','criterion','tolerance')},width=150,sort_keys=False))
E
```

```
##### fig2f-shuffle-abolishes-tuning
statement: Average peak-aligned combination tuning of combination-selective units was sharp, and shuffling spike counts across stimuli and trials abolished
  it.
criterion: For each of the 187 selective units, the eight responses at the best dt (O3), rotated so the best combination is first, averaged over units;
  the same for one shuffle per unit (counts shuffled across combinations within dt, as in the shuffle test). How the shuffled curves are aligned is not
  stated (Fig. 2f legend); readings are (a) to the unit's measured best combination, (b) to the shuffled curve's own peak. Reproduced when, under one reading,
  the CSI of the mean measured curve exceeds that of the mean shuffled curve, and, under reading (a), the shuffled curve's first point lies within its s.e.m.
  of its mean over the other seven combinations (under (b) a peak arises from the alignment itself, so the CSI comparison alone decides).

##### supp4-selectivity-at-high-rates
statement: Substantial combination selectivity was present among the most responsive combination-selective units and after subtracting spontaneous activity.
expected:
- quantity: selective units with best-combination response below 0.81 spikes per stimulus
  value: 95
  tolerance: 9.5
- quantity: selective units at or above 0.81 spikes per stimulus
  value: 92
  tolerance: 9.2
- quantity: nonselective units at or above 0.81 spikes per stimulus
  value: 91
[... 126 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
a=yaml.safe_load(open('attempts/laboy-juarez-2019-01.yaml'))
for o in a['outcomes']:
    if o['claim'] in ['supp4-selectivity-at-high-rates','fig7a-dt-half-width','fig3g-binary-decoder','supp8-order-decoding','fig6b-enhancement-not-different','supralinear-best-8-percent','fig7e-pc1-best-suboptimal','exp2-units','methods-dt-modulation']:
        print(yaml.safe_dump(o,width=150,sort_keys=False))
print(a['outcomes'][0].keys())
E
```

```
claim: exp2-units
outcome: reproduced
notebook: reproduce_laboy_juarez_2019.ipynb
output: claim:exp2-units
measured:
- 247
- 231
- 232
notes: 247 units in 12 files (12 mice), 246 after dropping a duplicate; 231 responsive to correlated and 232 to anti-correlated stimuli under O2 (a) and
  sham (a), and 237 to 240 under the other readings, all within tolerance. Layer counts (correlated/anti) are 52/51 L2/3, 79/80 L4, 73/74 L5 and 26/27 L6,
  against 54/54, 78/79, 71/70 and 21/24. Two recordings without sham trials are tested on the nine whiskers alone.
deviations:
- One of two experiment 2 units with identical spike trains (20160909) is dropped, so experiment 2 has 246 cells and 463 responsive sets under the main
  readings (O2 a, sham a).
- Responsiveness in the two recordings without sham trials (20160225, 20160316) is tested across the nine whiskers alone.

claim: methods-dt-modulation
outcome: not_reproduced
notebook: reproduce_laboy_juarez_2019.ipynb
output: claim:methods-dt-modulation
[... 146 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; grep -n "def half_width" -A25 lj2019.py | head -40
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; grep -n -i "half" lj2019.py | head; python -c "
import nbformat
nb=nbformat.read('reproduce_laboy_juarez_2019.ipynb',4)
for c in nb.cells:
    if 'def run_fig7a' in c.source or 'def halfwidth' in c.source or 'def half' in c.source: print(c.source[:2500])
"
```

```
lags = np.arange(-100, 101)
def aligned(g):
    best, sub = [], []
    for _, r in g.iterrows():
        cv = CUR[(r.unit, r.set)]["curves"] / CUR[(r.unit, r.set)]["curves"].max()
        A = np.full((8, len(lags)), np.nan)
        A[:, 100 - r.j_best: 100 - r.j_best + 101] = cv
        best.append(A[r.c_best]); sub.extend(np.delete(A, r.c_best, axis=0))
    return np.array(best), np.array(sub)
def halfwidth(curve, mode):
    c = curve[np.isfinite(curve)] if False else curve
    pk = c[100]
    lvl = (pk + np.nanmin(c)) / 2 if mode == "halfway" else pk / 2
    left = np.where(np.isfinite(c[:100]) & (c[:100] <= lvl))[0]
    right = np.where(np.isfinite(c[101:]) & (c[101:] <= lvl))[0]
    if not len(left) or not len(right):
        return np.nan
    return ((100 - left.max()) + (right.min() + 1)) / 2
def run_fig7a_dt_half_width(M2):
    for lab, g in [("selective, all", M2[M2.sel]), ("selective, best curve dt-modulated", M2[M2.sel & ~M2.best_const])]:
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; python - <<'E'
import nbformat
nb=nbformat.read('reproduce_laboy_juarez_2019.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type=='markdown' and ('Result' in c.source) and any(k in c.source for k in ['supralinear','0.072','half-width of 11.5','enhancement','178, 140']):
        print('===',i); print(c.source)
s=nb.cells[-1].source
print(s[s.find('| fig4c'):s.find('How the')])
E
```

```
=== 42
**Result: reproduced.** The CW-SW sparseness of SW-tuned units is above that of CW-tuned units at all 55 values of N (0.136 against 0.072 at N = 56).
=== 104
**Result: reproduced.** Under O3 (a), 0.072 of the 318 selective sets (reading d) are significantly supralinear for their best combination, inside the tolerance band (0.072 to 0.088) at its lower edge, by either reference distribution; over all 463 sets the fraction is 0.093, and O3 (b) gives 0.129 and 0.151. The outcome sits on the band's edge. Over the 187 sets with the smallest shuffle p (variant section), O3 (b) gives 0.080, within tolerance, and O3 (a) 0.032.
=== 110
**Result: not reproduced.** The rank-1 enhancement is 0.157 in selective and 0.112 spikes per stimulus in nonselective sets, a difference of 0.045 that the two-sample t-test finds (p = 0.0096); the variants give p = 0.047 and 0.004.
=== 119
**Result: partially reproduced (resting on an assumption).** Over the 248 selective sets whose best-combination curve is dt-modulated, the mean aligned curve falls halfway from its peak to its minimum at a half-width of 11.5 ms (reading a), within 10 +- 2 ms, and the suboptimal mean is lower at the best dt (0.605 against 1.000); but the suboptimal mean does not fall to that level on both sides within +-100 ms, so its half-width is undefined and the criterion's comparison of half-widths cannot be made. Including the 70 sets whose best curve is constant, and so has no best dt, gives 16.5 ms (suboptimal 24.5 ms); the per-unit reading (b) gives 14.9 ms, averaged over only the 74 sets with a defined value; reading (c) is undefined because the mean curve stays above half its peak.
=== 170
**Result of the variant section.** On the 187 sets with the smallest shuffle p, compared with the outcomes above on the 318 sets:

- Same outcome: fig2f-shuffle-abolishes-tuning (CSI 0.039 against 0.000; first shuffled point 0.020 above the others, s.e.m. 0.037), fig2f-most-selective-lower-firing (p = 3e-9 and 1e-5), fig3
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; python - <<'E'
import nbformat
p='reproduce_laboy_juarez_2019.ipynb'
nb=nbformat.read(p,4)
c=nb.cells
assert c[192].source.startswith('**Result of the calibrated-group section.** TO BE')
c[192].source='''**Result of the calibrated-group section.** The 162 calibrated sets are all among the 318 of the main analysis; they lie in 111 cells and are 68 correlated and 94 anti-correlated sets. Compared with the outcomes above on the 318 sets:

- Same outcome: fig2f-shuffle-abolishes-tuning (CSI 0.041 against 0.000; first shuffled point 0.009 above the others, s.e.m. 0.039), fig2f-most-selective-lower-firing (p = 8e-9 and 3e-5), fig3b-sharper-in-both-groups (p = 2e-10 and 1e-15), fig3b-linear-sharper-in-selective (p = 4.4e-7), supp6-layers (selective sets p = 0.014, L2/3 and L4 above L5 and L6; L6 count unchanged), fig6b-best-above-worst-below-scaled (all p < 1e-15), fig6b-suppression-greater-selective (Bonferroni over eight p = 0.0009 and 0.0001), fig6c-enhancement-strongest-sw (selective p = 1e-15, nonselective p = 0.35), fig7b-inbound-best-outbound-suboptimal (best peak -44 ms, suboptimal +42 ms, minima 2, -6 and 1 ms), fig7e-pc1-best-suboptimal (p = 1.6e-7, nonselective ratio 0.43; the selective suboptimal mean is negative, -0.65, as it also is on the 187 sets), fig7f-inbound-sharper (under reading c alignment differs, p = 0.019, and CSI does not, p = 0.26), fig3e-identity-decoder (0.167 at N = 162), fig4c-sw-tuned-decoding (reading a: CW-tuned above SW-tuned at N = 100 and 150, 0.195 against 0.167 with 27 CW-tuned sets; reading b as above), fig7g-inbound-decoding (differences -0.001 to 0.018 against s.d. 0.058 to 0.076), supp4-selectivity-at-high-rates (74, 88 and 80 under O3 a, 74, 88 and 93 under O3 b, so the first count misses 95 +- 9.5; peak 19.7 times its s.e.m.; partially reproduced) and fig7a-dt-half-width (12.0 ms over the 114 dt-modulated sets, at the edge of 10 +- 2, suboptimal lower at the best dt, 0.580, but with a narrower half-width of 7.0 ms; partially reproduced).
- fig6b-enhancement-not-different is not reproduced under O3 (a) (p = 0.0125) and would be reproduced under O3 (b) (p = 0.073), as on the 187 sets.
- Different outcome: fig3g-binary-decoder (0.681 at N = 10 and 0.929 at N = 100, reading a; reproduced), supp8-order-decoding (0.598 at N = 100, within the band; reproduced) and supralinear-best-8-percent (0.031 of selective sets under O3 a and 0.093 under O3 b, and 0.093 and 0.151 of all sets, all outside 0.072 to 0.088; not reproduced).

So fig3g and supp8 would be reproduced on either smaller group, and supp4 and fig7a only on the 187 sets. supralinear-best-8-percent is reproduced on the 318 sets (O3 a) and the 187 sets (O3 b) and not on the 162 calibrated sets, so its outcome also rests on the selective group.'''
assert 'TO BE' in c[195].source
c[195].source='''**Result of the band-edge checks.** With 20 refits, fig3g-binary-decoder reaches 0.6329 at N = 10 (s.e. 0.0012), 2.4 s.e. above the band's lower edge of 0.63, so its partial outcome holds within the Monte Carlo error. supp8-order-decoding reaches 0.5840 at N = 100 (s.e. 0.0008), 1.2 s.e. below the band's lower edge of 0.585: its expected accuracy lies within about 0.002 of the edge, and the outcome (not reproduced) would flip with a change of that size. supralinear-best-8-percent is a count, 23 of 318 sets (0.0723), with no Monte Carlo error; one set fewer would put it below the band.'''
old='The outcomes of these four claims, and of fig6b-enhancement-not-different, depend on which selective group is used, and are marked as resting on the assumption that the selective group is the one the shuffle test of the Methods gives.'
assert old in c[170].source
c[170].source=c[170].source.replace(old,'The outcomes of these four claims, and of fig6b-enhancement-not-different, depend on which selective group is used, and are marked as resting on the assumption that the selective group is the one the shuffle test of the Methods gives. The next section runs the same claims on the calibrated group.')
s=c[104].source
c[104].source=s+' On the 162 calibrated sets (calibrated-group section) no reading is within tolerance (0.031 and 0.093 of selective sets), so the outcome also rests on the selective group. The fraction is a count, 23 of 318 sets: one set fewer would put it below the band.'
s=c[139].source
old='over the 187 sets with the smallest p (variant section) the decoder reaches 0.670 and 0.914.'
assert old in s
c[139].source=s.replace(old,'over the 187 sets with the smallest p (variant section) the decoder reaches 0.670 and 0.914, and over the 162 calibrated sets 0.681 and 0.929. With 20 further refits (band-edge checks) the N = 10 mean is 0.6329 with an s.e. of 0.0012, 2.4 s.e. above the edge.')
s=c[148].source
old='over the 187 sets with the smallest p (variant section) the decoder reaches 0.595, within the band.'
assert old in s
c[148].source=s.replace(old,'over the 187 sets with the smallest p (variant section) the decoder reaches 0.595 and over the 162 calibrated sets 0.598, both within the band. With 20 further refits (band-edge checks) the selective mean is 0.5840 with an s.e. of 0.0008, 1.2 s.e. below the edge, so the expected accuracy is within about 0.002 of it.')
# summary
s=c[-1].source
old='| supralinear-best-8-percent | reproduced |'
assert old in s
s=s.replace(old,'| supralinear-best-8-percent | reproduced (assumption: the selective group of the shuffle test) |')
old='every selective-group claim is also run on the 187 sets with the smallest p, which changes the outcome of four claims (supp4, fig7a, fig3g, supp8) and of fig6b-enhancement-not-different under one reading.'
assert old in s
s=s.replace(old,'every selective-group claim is also run on the 187 sets with the smallest p, which changes the outcome of four claims (supp4, fig7a, fig3g, supp8) and of fig6b-enhancement-not-different under one reading, and on the 162 sets that FDR selects from p-values calibrated on that null, which changes the outcome of fig3g, supp8 and supralinear-best-8-percent and of fig6b-enhancement-not-different under one reading.')
c[-1].source=s
nbformat.write(nb,p)
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd entries/laboy-juarez-2019; python - <<'E'
p='README.md'
s=open(p).read()
old='''The unit counts of all three experiments match the paper. Single-whisker tuning, the preference
for CW-SW sequences, sublinear integration with near-linear best combinations, the inbound order
preference and the awake results mostly reproduce. The shuffle test of combination selectivity
finds more selective response sets than the paper (318 of 463, against 187 of 451) and, on a
null built from the real data, gives p < 0.05 for a quarter of the sets; every claim on the
selective group is also run on the 187 sets with the smallest p, which changes the outcome
of four claims, and of a fifth under one reading.'''
assert old in s
new='''The unit counts of all three experiments match the paper. Single-whisker tuning, the preference
for CW-SW sequences and sublinear integration with near-linear best combinations mostly
reproduce, as do six of the eight testable awake claims. Of the experiment 2 claims on sequence
order, the dt tuning and the PCA claims are partially reproduced, and the order decoders are not
reproduced. The shuffle test of combination selectivity finds more selective response sets than
the paper (318 of 463, against 187 of 451) and, on a null built from the real data, gives
p < 0.05 for a quarter of the sets. Every claim on the selective group is also run on the 187
sets with the smallest p, which changes the outcome of four claims, and of a fifth under one
reading, and on the 162 sets selected after calibrating the p-values on that null, which changes
the outcome of three claims, and of a fourth under one reading.'''
open(p,'w').write(s.replace(old,new))
E
sed -n 1,14p README.md
```

```
# Laboy-Juarez, Langberg, Ahn & Feldman (2019) from CRCNS ssc-9

Tests the findings of [Laboy-Juarez et al. (2019)](https://doi.org/10.1038/s41593-019-0448-6) on
[CRCNS ssc-9](https://doi.org/10.6080/K0FJ2F13), which holds the spike times of single units in
mouse barrel cortex during single- and two-whisker stimulation in the paper's three experiments:
a survey of all two-whisker combinations in anesthetized mice (Figure 1), dense dt mapping of
CW-SW sequences in anesthetized mice (Figures 2 to 7) and a replication in awake mice (Figure 8).

| Experiment | Claims | Reproduced | Partially | Not reproduced | Blocked |
|---|---|---|---|---|---|
| 1, anesthetized survey | 10 | 9 | 1 | 0 | 0 |
| 2, dense dt mapping | 31 | 14 | 11 | 6 | 0 |
| 3, awake mice | 9 | 6 | 1 | 1 | 1 |
```

**Agent calls Bash**

```bash
cd  ls transcripts/laboy-juarez-2019/; grep -n "B10" -A6 transcripts/laboy-juarez-2019/verifier-1-report.md | head -30
```

```
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
claims.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
verifier-2.md
```

**Agent calls Bash**

```bash
cd  grep -n -i "sham trials\|lick" transcripts/laboy-juarez-2019/verifier-1-report.md | head; grep -n "^\*\*\|^#\|^[0-9]*\. \*\*\|^- \*\*B" transcripts/laboy-juarez-2019/verifier-1-report.md | head -50
```

```
54:| fig8b-awake-behavior | blocked (data_missing) | I checked the archive: the S3 listing and filelist.txt hold only data.zip, checksums and the descriptor. The zip holds only 23 per-session .mat files, and the descriptor documents no lick or Go/No-go fields. No part is testable. |
88:10. **[does not affect a conclusion]** Two recordings in experiment 2 have no sham trials, so their units are tested on the nine whiskers alone. Experiment 3 cannot apply the lick exclusion. Both are stated in the notebook.
97:- **Experiment 3 field names:** printing `u._fieldnames` for one experiment 3 unit, which would confirm there are no lick or trial-type fields. The descriptor does not document `DeltaT` or `experiment`, nor the spikes up to 424 s after epoch onset.
1:## A. Outcomes (50 claims in the claims file; the notebook tests 49 and treats 1 as blocked)
58:## B. Problems
60:1. **[affects a conclusion]** The shuffle selectivity test is anti-conservative (cell 36; `L.fast_dt_smooth`, `L.shuffle_csi`, `L.mahalanobis_p`), and the notebook never checks its calibration.
66:2. **[affects a conclusion]** `derive` (cell 45): when the best combination's curve is constant (90 sets, 70 of them selective), `argmax` breaks the tie at dt = −50 ms. The markdown flags this, but most analyses still use it:
71:3. **[affects a conclusion]** methods-dt-modulation (cell 40, `fast_dt_smooth`): "unsmoothed" never wins (0%). In my synthetic runs at λ = 1, where the 1e-3 floor rarely binds, it also never won. So the paper's 23% likely comes from a scoring choice the notebook does not explore. The zero-padding reading (1.1%) shows the outcome is very sensitive to these details.
74:4. **[affects a conclusion]** exp1-cw-sw-comparable-firing: this is a claims-file issue, copied from the paper. The paper's "4.8 ± 0.48 spikes per stimulus" cannot be a per-stimulus mean: the Fig. 1d axis tops out near 4 spikes per stimulus. The notebook's values in Hz (0.581/0.125 = 4.65; 0.601/0.125 = 4.80) match all four
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "claim: exp2-units$\|claim: exp3-units-cw-tuned$" -A8 attempts/laboy-juarez-2019-01.yaml | sed -n 1,60p; grep -n "^  - claim: supralinear-best-8-percent" -A3 attempts/laboy-juarez-2019-01.yaml; python -c "import ruamel.yaml" 2>&1
```

```
Exit code 1
229:- claim: exp2-units
230-  outcome: reproduced
231-  notebook: reproduce_laboy_juarez_2019.ipynb
232-  output: claim:exp2-units
233-  measured:
234-  - 247
235-  - 231
236-  - 232
237-  notes: 247 units in 12 files (12 mice), 246 after dropping a duplicate; 231 responsive to correlated
--
786:- claim: exp3-units-cw-tuned
787-  outcome: reproduced
788-  notebook: reproduce_laboy_juarez_2019.ipynb
789-  output: claim:exp3-units-cw-tuned
790-  measured:
791-  - 81
792-  - 74
793-  - 46
794-  notes: 81 units, 74 responsive (sham a), 46 CW-tuned (0.62); the CW has the largest mean single-whisker
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/laboy-juarez-2019-01.yaml'
s=open(p).read()
reps=[
("""    reason: 247 units in the files (246 after dropping a duplicate). Under O2 (a) and sham (a), 231 correlated
      and 232 anti-correlated sets are responsive; all within tolerance.
    response: No change.""",
"""    reason: 247 units in the files (246 after dropping a duplicate). Under O2 (a) and sham (a), 231 correlated
      and 232 anti-correlated sets are responsive; all within tolerance. Two recordings in experiment 2
      have no sham trials, so their units are tested on the nine whiskers alone; this is stated in the
      notebook and does not affect a conclusion (B10).
    response: No change."""),
("""    reason: 81 units, 74 responsive, 46 CW-tuned; mean single-whisker tuning is largest at the CW.
    response: No change.""",
"""    reason: 81 units, 74 responsive, 46 CW-tuned; mean single-whisker tuning is largest at the CW. Experiment
      3 cannot apply the lick exclusion; this is stated in the notebook and does not affect a conclusion
      (B10).
    response: No change."""),
("and 237 to 240 under the other readings","and 236 to 240 under the other readings"),
]
for a,b in reps:
    assert s.count(a)==1,a
    s=s.replace(a,b)
open(p,'w').write(s)
E
grep -n "236 to 240" -B2 -A3 attempts/laboy-juarez-2019-01.yaml
```

```
236-  - 232
237-  notes: 247 units in 12 files (12 mice), 246 after dropping a duplicate; 231 responsive to correlated
238:    and 232 to anti-correlated stimuli under O2 (a) and sham (a), and 236 to 240 under the other readings,
239-    all within tolerance. Layer counts (correlated/anti) are 52/51 L2/3, 79/80 L4, 73/74 L5 and 26/27
240-    L6, against 54/54, 78/79, 71/70 and 21/24. Two recordings without sham trials are tested on the nine
241-    whiskers alone.
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
p='attempts/laboy-juarez-2019-01.yaml'
s=open(p).read()
d=yaml.safe_load(s)
for w in [100,105,110]:
    o=yaml.safe_dump(d,sort_keys=False,allow_unicode=True,width=w)
    import difflib
    n=sum(1 for l in difflib.unified_diff(s.splitlines(),o.splitlines(),lineterm='') if l.startswith(('+','-')))
    print(w,n)
E
```

```
100 6
105 1338
110 1382
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
p='attempts/laboy-juarez-2019-01.yaml'
d=yaml.safe_load(open(p))
O={o['claim']:o for o in d['outcomes']}
print([ (k, d['verifications'][0].keys()) for k in [0]])
print(d['verifications'][0]['by'])
old_dev="The claim is also run on the 187 sets with the smallest shuffle p (notebook, variant section)."
n=0
for o in d['outcomes']:
    for i,x in enumerate(o.get('deviations',[])):
        if old_dev in x: n+=1
print(n)
print([o['claim'] for o in d['outcomes'] if any(old_dev in x for x in o.get('deviations',[]))])
print(O['exp2-combination-selective-prevalence']['notes'])
E
```

```
[(0, dict_keys(['date', 'kind', 'by', 'reviewed', 'results']))]
Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
19
['fig2f-shuffle-abolishes-tuning', 'fig2f-most-selective-lower-firing', 'supp4-selectivity-at-high-rates', 'fig3b-sharper-in-both-groups', 'fig3b-linear-sharper-in-selective', 'fig3e-identity-decoder', 'fig3g-binary-decoder', 'fig4c-sw-tuned-decoding', 'supralinear-best-8-percent', 'fig6b-best-above-worst-below-scaled', 'fig6b-enhancement-not-different', 'fig6b-suppression-greater-selective', 'fig6c-enhancement-strongest-sw', 'fig7a-dt-half-width', 'fig7b-inbound-best-outbound-suboptimal', 'fig7e-pc1-best-suboptimal', 'fig7f-inbound-sharper', 'fig7g-inbound-decoding', 'supp8-order-decoding']
318 of 463 responsive sets are selective with FDR over all sets (312 with the two sets apart), in 189 of 246 cells (0.768), against 187 sets and 129 cells (0.52). Fractions are 0.641 and 0.733 of responsive correlated and anti-correlated sets, or 0.602 and 0.691 of all cells, against 0.35 and 0.46. 340 sets have uncorrected p < 0.05. The paper states no false-positive rate for the test. On a real-data null (counts permuted across combinations within each dt, kernels chosen again, 1000 shuffles) the test gives p < 0.05 for 0.246 of sets and p < 0.01 for 0.076, so it is anti-conservative here, though FDR control selects none of the null sets; measured p below 0.001 for 147 sets against 6 in the null. Calibrated on the null, the measured p-values give 162 selective sets after FDR. The 187 sets with the smallest p lie in 130 cells (74 correlated, 113 anti-correlated); their count is fixed at the paper's.
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/edit.py <<'E'
import yaml
p='attempts/laboy-juarez-2019-01.yaml'
d=yaml.safe_load(open(p))
O={o['claim']:o for o in d['outcomes']}
old_dev="The claim is also run on the 187 sets with the smallest shuffle p (notebook, variant section)."
new_dev=("The claim is also run on the 187 sets with the smallest shuffle p and on the 162 sets that FDR selects "
         "from p-values calibrated on the real-data null (notebook, variant and calibrated-group sections).")
for o in d['outcomes']:
    o['deviations']=[x.replace(old_dev,new_dev) for x in o.get('deviations',[])]
def add(c, text):
    O[c]['notes']=O[c]['notes'].rstrip()+' '+text
add('exp2-combination-selective-prevalence','The 162 calibrated sets are all among the 318, lie in 111 cells and are 68 correlated and 94 anti-correlated sets; every selective-group claim is also run on them.')
add('supp4-selectivity-at-high-rates','On the 162 calibrated sets the counts are 74, 88 and 80 (O3 b, 74, 88 and 93), so the first misses 95 +- 9.5, and the peak is 19.7 times its s.e.m., which would be partially reproduced, as on the 318 sets.')
add('fig3g-binary-decoder','On the 162 calibrated sets, 0.681 and 0.929 (reading a), which would reproduce the claim. With 20 further refits on new draws (band-edge checks), the N = 10 mean over the 318 selective sets is 0.6329 with an s.e. of 0.0012, 2.4 s.e. above the edge.')
add('supp8-order-decoding','On the 162 calibrated sets it is 0.598, which would also reproduce the claim. With 20 further refits on new draws (band-edge checks), the selective mean is 0.5840 with an s.e. of 0.0008, 1.2 s.e. below 0.585, so the expected accuracy lies within about 0.002 of the edge.')
add('fig6b-enhancement-not-different','On the 162 calibrated sets, p = 0.0125 under O3 (a) and 0.073 under O3 (b), as on the 187 sets.')
add('fig7a-dt-half-width','On the 162 calibrated sets, 12.0 ms over the 114 dt-modulated sets, at the edge of tolerance, with the suboptimal mean lower at the best dt (0.580) but with a narrower half-width (7.0 ms), which would be partially reproduced, as on the 318 sets.')
add('supralinear-best-8-percent','On the 162 calibrated sets no reading is within tolerance (selective 0.031 under O3 a and 0.093 under O3 b; all sets 0.093 and 0.151), which would not reproduce the claim. The fraction is a count, 23 of 318 sets, so one set fewer would put it below the band.')
O['supralinear-best-8-percent']['deviations'].append(
    "Assumption. The selective group is the one the shuffle test of the Methods (Combination selectivity) gives here, 318 sets. "
    "On a real-data null that test gives p < 0.05 for 0.246 of sets, and on the 162 calibrated sets this claim has a different "
    "outcome (notes); the Methods' procedure is kept as the main reading because it is the one the paper describes.")
O['supralinear-best-8-percent']['assumed']=True
add('fig4c-sw-tuned-decoding','On the 162 calibrated sets, reading (a) has CW-tuned above SW-tuned decoders at N = 100 and 150 (0.195 against 0.167 at N = 150, 27 CW-tuned sets); reading (b) is unchanged.') if 'fig4c-sw-tuned-decoding' in O else None
add('fig7e-pc1-best-suboptimal','On the 162 calibrated sets, p = 1.6e-7 and ratio 0.43; there, as on the 187 sets, the selective suboptimal mean is negative (-0.65 and -0.44).')

ALL="I agree with all 50 stated outcomes."
SELRESP="No change of outcome. The claim is now also run on the 162 calibrated sets (calibrated-group section), with the same outcome."
SELCLAIMS=['fig2f-shuffle-abolishes-tuning','fig2f-most-selective-lower-firing','fig3b-sharper-in-both-groups','fig3b-linear-sharper-in-selective','supp6-layers','fig6b-best-above-worst-below-scaled','fig6b-suppression-greater-selective','fig6c-enhancement-strongest-sw','fig7b-inbound-best-outbound-suboptimal','fig7e-pc1-best-suboptimal','fig7f-inbound-sharper','fig3e-identity-decoder','fig4c-sw-tuned-decoding','fig7g-inbound-decoding']
README_R=("The README's 'the inbound order preference and the awake results mostly reproduce' is not supported: no experiment 2 order claim is reproduced; "
          "fig7b, fig7e and fig7f are partially reproduced, fig7g and supp8 are not reproduced, and only the awake fig8j is reproduced.")
README_RESP="The README now says that the dt tuning and PCA claims are partially reproduced and the order decoders are not reproduced."
B1=("B1, the selective group: the main analyses still use the uncalibrated test, 318 sets with 24.6% false positives on the real-data null. "
    "Five outcomes depend on which group is used, and all are marked. The variant group fixes its size at the paper's 187; no claim was run on the "
    "calibrated group of 162 sets, which would be the less arbitrary alternative.")
B1RESP=("Every selective-group claim is now run on the 162 calibrated sets (calibrated-group section). ")
R={
'exp1-units':("Stated and reasonable (assumed: caudal singles). Pooling both directions breaks the counts (cell 15).","No change."),
'exp1-cw-tuned-fraction':("Stated and reasonable (assumed: caudal singles). Pooling both directions breaks the counts (cell 15).","No change."),
'exp1-cw-sw-comparable-firing':("I now agree, and withdraw my round-1 'not reproduced'. The criterion names no partial rule; spontaneous rates hold, maximal evoked firing fails in the claims file's unit. B4 is a gap in the claims file: it carries the paper's '4.8 spikes per stimulus' without noting that the value is most likely in Hz. The outcome correctly uses the claims file's unit.",
    "No change. The question whether the expected values are in Hz is already in questions/laboy-juarez-2019.yaml for a reader."),
'fig1e-best-combination-includes-cw':("I agree. Same-direction sequences give 0.694, 0.851 and 0.456 (cell 33), and sham reading (b) also passes. The assumption is stated and reasonable: the Methods' 261 stimuli are 9 singles plus 36 x 7 sequences, and the experiment 3 stimuli, called identical, are same-direction only. Cell 7 shows the opposite-direction trials are real stimuli with distinct timings, not a coding flip. The Summary table (cell 195) labels the wrong assumption, 'caudal singles': the outcome rests on the same-direction sequence reading, as variant (ii) gives 0.421, which fails (cell 44), while pooling both single directions (i) still passes.",
    "The Summary table now labels the assumption 'same-direction sequences'. No change of outcome."),
'exp2-units':("I agree. Cell 51 and the record's exp2-units notes say 'the other three readings give 237 to 240'; cell 50 prints anti-correlated = 236 under O2 (a), sham (b), so the range is 236 to 240. All values are still within tolerance, so the outcome is unaffected.",
    "Corrected to 236 to 240 in cell 51 and the notes. No change of outcome."),
'methods-dt-modulation':("I agree. B3: not reproduced, and no reason has been found. Two more scoring readings were run, still with no unsmoothed curve; this is now an open question to the authors.",
    "No change. No further scoring reading that the Methods allow was found to run, so the reason stays open."),
'exp2-combination-selective-prevalence':(ALL+" "+B1, B1RESP+"They are all among the 318 and lie in 111 cells; the test itself is unchanged, so this outcome is unchanged."),
'supp4-selectivity-at-high-rates':("I now agree, and withdraw my round-1 'not reproduced': the peak test holds, the counts fail, and the same standard as for fig7b, fig7c, fig7e and supp6 applies. The selective-group assumption is stated in the outcome and checked against the 187-set variant. "+B1,
    B1RESP+"There the counts are 74, 88 and 80 (O3 b, 74, 88 and 93) and the peak test holds, so the outcome would be the same; it is reproduced only on the 187 sets. No change of outcome."),
'fig3g-binary-decoder':("I agree. Cell 138 gives 0.633 at N = 10 and 0.857 at N = 100, which meets the criterion's partial rule. It is fragile: 0.003 above the band edge, with an s.d. over refits of 0.010, and it could flip within noise (B6). The outcome depends on the selective group (B1).",
    "Added a band-edge check with 20 further refits: 0.6329, s.e. 0.0012, 2.4 s.e. above 0.63, so the partial outcome holds within the Monte Carlo error. "+B1RESP+"There the decoder reaches 0.681 and 0.929, which would reproduce the claim, as on the 187 sets. The outcome is kept, not proposed for change: the verifier found the selective-group assumption stated and reasonable, and the main reading is the test the Methods describe."),
'fig4c-sw-tuned-decoding':("I now agree, and withdraw my round-1 'not reproduced'. In reading (b) SW-tuned beats CW-tuned at every size; CW-tuned is not above chance at N = 150. Part holds and another fails, the same standard as for fig7b, fig7c, fig7e and supp6.",
    "No change of outcome. On the 162 calibrated sets reading (a) fails (CW-tuned above SW-tuned at N = 100 and 150) and reading (b) is unchanged, so the outcome would be the same."),
'supralinear-best-8-percent':("I agree. On the 187 sets the main reading O3 (a) gives 0.032 and only O3 (b) passes (0.080, cell 156); the criterion accepts any combination of readings, so cell 170's 'same outcome' is correct as written. Both groups pass only at a band edge and under different readings, which leaves this outcome weak; 0.0723 against a lower bound of 0.072 could flip within noise (B6).",
    "On the 162 calibrated sets no reading is within tolerance (0.031 and 0.093), so the outcome now also rests on the selective group: it is marked assumed, with the assumption stated as for the other selective-group claims. The notes and cell 104 say that the fraction is a count, 23 of 318, with no Monte Carlo error, and that one set fewer would put it below the band. No change of outcome."),
'fig6b-enhancement-not-different':("I agree. The selective-group assumption is stated in the outcome and checked against the 187-set variant; the outcome depends on which group is used, under O3 (b). "+B1,
    B1RESP+"There p = 0.0125 under O3 (a) and 0.073 under O3 (b), as on the 187 sets. No change of outcome."),
'fig7a-dt-half-width':("I agree. Leaving out sets with a constant best curve is stated and reasonable, since they have no best dt. The selective-group assumption is stated and checked against the 187-set variant. "+B1,
    B1RESP+"There the half-width is 12.0 ms, at the edge of tolerance, and the suboptimal half-width is narrower (7.0 ms), so the outcome would be the same. No change of outcome."),
'fig8c-awake-cw-stronger':("I agree. Cell 177 gives p = 0.0021, and the criterion's partial rule needs the test to hold.","No change."),
'supp8-order-decoding':("I agree. The mean over five refits is 0.584 against a lower bound of 0.585, with a Monte Carlo s.e. of 0.003 (cell 147). It is fragile and could flip within noise (B6). The selective-group assumption is stated and checked against the 187-set variant. "+README_R,
    "Added a band-edge check with 20 further refits: 0.5840, s.e. 0.0008, 1.2 s.e. below 0.585, so the expected accuracy lies within about 0.002 of the edge. "+B1RESP+"There it is 0.598, which would reproduce the claim, as on the 187 sets. The outcome is kept, not proposed for change: the verifier found the selective-group assumption stated and reasonable, and the main reading is the test the Methods describe. "+README_RESP),
}
for c in ['fig7b-inbound-best-outbound-suboptimal','fig7e-pc1-best-suboptimal','fig7f-inbound-sharper','fig7g-inbound-decoding']:
    R[c]=(ALL+" "+README_R, SELRESP+" "+README_RESP)
results=[]
for o in d['outcomes']:
    c=o['claim']
    if c in R: reason,resp=R[c]
    elif c in SELCLAIMS: reason,resp=ALL,SELRESP
    else: reason,resp=ALL,"No change."
    results.append(dict(claim=c,agrees=True,outcome=o['outcome'],reason=reason,response=resp))
d['verifications'].append(dict(date='2026-11-12',kind='agent',by=d['verifications'][0]['by'],
    reviewed=("Round 2: the full executed notebook with its conclusion cells and summary, the helper module, the claims file, "
              "the attempt record and the README, with the paper's full text."),
    results=results))
open(p,'w').write(yaml.safe_dump(d,sort_keys=False,allow_unicode=True,width=100))
E
python $TMPDIR/edit.py && git diff --stat attempts/
```

```
attempts/laboy-juarez-2019-01.yaml | 461 ++++++++++++++++++++++++++++++++++---
 1 file changed, 432 insertions(+), 29 deletions(-)
```

**Agent calls Bash**

```bash
cd  date -u; grep -n "—\|rather" attempts/laboy-juarez-2019-01.yaml entries/laboy-juarez-2019/README.md | head; python - <<'E'
import nbformat
nb=nbformat.read('entries/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb',4)
for i,c in enumerate(nb.cells):
    if '—' in c.source or 'rather' in c.source: print(i)
E
python tools/entry.py check entries/laboy-juarez-2019 2>&1 | tail -5
```

```
Thu Nov 12 23:50:41 UTC 2026
0 error(s)
```

**Agent**

Text and record updated; now the final re-run of the entry (about 34 minutes).

**Agent calls Bash**

```bash
cd  timeout 7000 python tools/entry.py all entries/laboy-juarez-2019 2>&1 | tail -5; date -u
```

```
Installed kernelspec registry-laboy-juarez-2019 in executed/laboy-juarez-2019/.venv/share/jupyter/kernels/registry-laboy-juarez-2019
0 error(s)
pass  reproduce_laboy_juarez_2019.ipynb  (2024 s)
Fri Nov 13 00:24:43 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import nbformat
nb=nbformat.read('executed/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb',4)
def out(i): return ''.join((o.get('text') or '') for o in nb.cells[i].get('outputs',[]))
for i in [50,59,104-1,138,147,178,180,183,188,191,194]:
    print('==',i, nb.cells[i].source[:60].replace('\n',' ')); print(out(i)[-700:])
E
```

```
== 50 print(f"units in the files: {len(U2)} in {U2.file.nunique()}
63
         a    b   238   236   474
         b    a   237   237   474
         b    b   240   240   480
layers of responsive sets (O2 a, sham a): {'anti': {'L2/3': 51.0, 'L4': 80.0, 'L5': 74.0, 'L6': 27.0, 'outside': nan}, 'corr': {'L2/3': 52.0, 'L4': 79.0, 'L5': 73.0, 'L6': 26.0, 'outside': 1.0}}
expected layer counts corr/anti: L2/3 54/54, L4 78/79, L5 71/70, L6 21/24
responsive sets per mouse: {'20160225': 15, '20160316': 4, '20160325': 28, '20160406': 42, '20160504': 64, '20160506': 7, '20160803': 74, '20160808': 24, '20160817': 52, '20160829': 16, '20160909': 27, '20160914': 110}
recordings without sham trials (tested on the nine whiskers alone): ['20160225:10da10', '20160316:2dc362']

== 59 t0 = time.time() rng_null = np.random.default_rng(20190804) 
R: 0
histogram of p by bin ['0-0.001', '0.001-0.01', '0.01-0.05', '0.05-0.1', '0.1-0.2', '0.2-0.5', '0.5-1']
   measured: [147, 92, 101, 32, 40, 46, 5]
   null:     [6, 29, 79, 83, 105, 129, 32]
measured p calibrated on the null p: calibrated p < 0.05 for 219 sets; selective after FDR: 162 (the null's floor of 1/1001 limits how small a calibrated p can be)
calibrated group: 162 sets, correlated 68, anti-correlated 94, cells 111; in the uncalibrated selective group 162
variant group of the paper's size: the 187 sets with the smallest p (ties broken by the larger Mahalanobis distance); largest p in it 0.0032; sets at the smallest p (0.00020): 106; correlated 74, anti-correlated 113, cells 130

== 103 def run_supralinear_best_8_percent(M2):     rows = []     fo
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/laboy-juarez-2019 2>&1 | tail -2; git status --short
```

```
0 error(s)
 M attempts/laboy-juarez-2019-01.yaml
 M entries/laboy-juarez-2019/README.md
 M entries/laboy-juarez-2019/reproduce_laboy_juarez_2019.ipynb
 M tools/site_assets/list.js
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
```

**Agent**

No outcome changed and I proposed no changes. The counts are still 29 reproduced, 13 partially reproduced, 7 not reproduced and 1 blocked. The verifier agreed with all 50 outcomes, and the round is recorded as `verifications` round 2 in `attempts/laboy-juarez-2019-01.yaml`. The entry re-ran cleanly with `python tools/entry.py all entries/laboy-juarez-2019` (2024 s), the earlier main-analysis numbers came out the same, and `check` reports 0 errors.

**Text corrections the verifier asked for**
- **exp2-units:** the range of the other readings is now "236 to 240", in both cell 51 and the record's notes.
- **Summary table:** fig1e's assumption is now "same-direction sequences".
- **README:** the claim that the inbound order preference "mostly reproduces" is gone. It now says the experiment 2 dt tuning and PCA claims are partially reproduced and the order decoders are not reproduced.
- **Round-1 record:** the verifier's point B10 (two recordings without sham trials, no lick exclusion) was missing from the reasons. It is now under exp2-units and exp3-units-cw-tuned.

**Outputs added**
- **Calibrated group (B1).** Every selective-group claim now also runs on the 162 sets that FDR selects from the calibrated p-values. All 162 are among the 318 of the main analysis. Compared with the 318:
  - Three claims would get a different outcome:
    - fig3g would be reproduced (0.681 at N = 10, 0.929 at N = 100).
    - supp8 would be reproduced (0.598).
    - supralinear would not be reproduced (0.031 and 0.093).
  - fig6b-enhancement-not-different would be reproduced under O3 (b) only (p = 0.073).
  - supp4 and fig7a stay partially reproduced.

  supralinear's outcome now also depends on which selective group is used, so I marked it `assumed: true` and added that assumption as a deviation. I did not propose changing these outcomes. The verifier called the selective-group assumption stated and reasonable, and the main analysis uses the test the Methods describe.
- **Band-edge checks (B6).** I re-ran the two decoders near a band edge with 20 more refits each:
  - fig3g: 0.6329 (s.e. 0.0012), 2.4 s.e. above the 0.63 edge, so partially reproduced holds.
  - supp8: 0.5840 (s.e. 0.0008), 1.2 s.e. below the 0.585 edge. The expected accuracy is within about 0.002 of the edge, and the notes say so.
  - supralinear is a count, 23 of 318 sets, with no sampling error: one set fewer would put it below the band.

**Not done**
- **B3 (methods-dt-modulation):** still not reproduced, and I found no other scoring reading in the Methods to try. It stays an open question to the authors.
- **B4:** the question whether the expected values are in Hz was already in `questions/laboy-juarez-2019.yaml`, so I added nothing.
- **Unrelated file:** the existing change to `tools/site_assets/list.js` was there before this run and I left it alone.

Nothing is committed.

## End of run

43 turns, 73 minutes, $2.34 at API prices, result: success.
