# cambrainha-2025 · author-revise-2 · run 46008732882

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls entries/cambrainha-2025 transcripts/cambrainha-2025; cat transcripts/cambrainha-2025/verifier-2-report.md
```

```
Fri Nov 27 13:44:11 UTC 2026
entries/cambrainha-2025:
README.md
criticality.py
entry.yaml
reproduce_cambrainha_2025.ipynb
requirements.in
requirements.lock.txt

transcripts/cambrainha-2025:
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
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/protocol.md | head -c 60000
```

```
<persisted-output>
Output too large (46.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/372ace8c-5241-43fb-950d-562997013fa4/tool-results/bssvjdp46.txt

Preview (first 2KB):
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
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/cambrainha-2025/entry.yaml; ls questions/ | grep camb; cat questions/cambrainha-2025.yaml 2>/dev/null | head -100
```

```
schema_version: 1
name: cambrainha-2025
type: reproduction
title: Kurtosis of coarse-grained V1 activity and task performance (Cambrainha et al. 2025)
description: Tests the findings of Cambrainha, Castro, de Vasconcelos, Carelli and Copelli (2025)
  on dandiset 000713, the Allen Institute Visual Behavior Neuropixels data. It computes, per 30-s
  window of V1 spiking, the kurtosis after momentum-space coarse graining and its ISI-shuffled
  surrogate, relates it to the hit rate of the change-detection task, compares the active,
  passive and non-natural image phases, and fits the real-space renormalization exponents.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_cambrainha_2025.ipynb
  title: Reproducing Cambrainha et al. (2025) from dandiset 000713
  runtime_minutes: 30
helpers:
- criticality.py
related:
- id: dandi:000713/0.240702.1725
  relation: uses_data
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/372ace8c-5241-43fb-950d-562997013fa4/tool-results/bssvjdp46.txt; grep -n "^#" $F; ls attempts 2>/dev/null | grep camb; git ls-files | grep cambrainha | head -30
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
370:### 2. Check the data against its description
385:### 3. Write the entry
470:### 4. Lock, check and run
490:### 5. Record the attempt
599:### 6. Hand over for verification
637:## Repeat attempts
703:## Local and remote datasets
726:## Verifier
730:### Round 1: without the author's conclusions
755:### Round 2: with the author's conclusions
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
F=/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/372ace8c-5241-43fb-950d-562997013fa4/tool-results/bssvjdp46.txt; sed -n 199,215p $F; sed -n 470,640p $F; sed -n 755,800p $F
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
[... 193 more lines not kept]
````

**Agent calls Bash**

```bash
cat attempts/cambrainha-2025-01.yaml
```

```
<persisted-output>
Output too large (37.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/372ace8c-5241-43fb-950d-562997013fa4/tool-results/bgp200j62.txt

Preview (first 2KB):
schema_version: 3
id: cambrainha-2025-01
datasets:
- archive: dandi
  id: "000713"
  version: 0.240702.1725
  doi: 10.48324/dandi.000713/0.240702.1725
  relation: primary
paper: doi:10.1103/w49n-2vz8
date: 2026-11-27
entry: cambrainha-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 35 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/cambrainha-2025-01.yaml"
}
```

```
1	schema_version: 3
2	id: cambrainha-2025-01
3	datasets:
4	- archive: dandi
5	  id: "000713"
6	  version: 0.240702.1725
7	  doi: 10.48324/dandi.000713/0.240702.1725
8	  relation: primary
9	paper: doi:10.1103/w49n-2vz8
10	date: 2026-11-27
11	entry: cambrainha-2025
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 572 more lines not kept]
```

**Agent calls Bash**

```bash
ls executed/cambrainha-2025/ 2>/dev/null; python -c "
import json
nb=json.load(open('entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    print(i,c['cell_type'],len(s),s[:100].replace('\n',' | '))
"
```

```
reproduce_cambrainha_2025.ipynb
result.json
0 markdown 2532 # Reproducing Cambrainha et al. (2025) from dandiset 000713 |  | Paper. Cambrainha, Castro, de Vasconcel
1 code 742 import os | os.environ.setdefault("OMP_NUM_THREADS", "1") | os.environ.setdefault("OPENBLAS_NUM_THREADS"
2 markdown 219 ## Survey of the dataset |  | Every session file is opened and its units, electrodes and trials tables a
3 code 809 assets = cr.session_assets() | with ThreadPoolExecutor(12) as ex: |     survey = pd.DataFrame(list(ex.ma
4 markdown 948 ## Processing every session |  | All sessions with at least 128 V1 units (reading (a) of O1, counting bo
5 code 788 proc = survey[survey.visp_all >= cr.MIN_UNITS].reset_index(drop=True) | asset_of = {a["path"]: a for a
6 markdown 13 ## Data check
7 code 4170 ok = [r for r in results if "error" not in r] | sessions_ok = ok | W_all = cr.window_table(ok) | sel_gt = 
8 markdown 1598 The checks above show: |  | - 153 session files from 81 mice, no session deposited twice (identifiers un
9 markdown 375 ## Common definitions |  | The analysis set is the sessions with more than 128 V1 units (O1 (a)). Readin
10 code 2158 W = W_all[(W_all.units == "all") & W_all.path.isin(sel_gt)].copy() | mouse_of = dict(zip(survey.path, 
11 markdown 2932 ## How readings decide |  | The claims file lists readings of details the paper leaves open (O1 to O11).
12 markdown 283 The two poolings of O3 give the same number: psi is normalised to unit variance for every unit (Eq. 
13 code 194 d = W[W.length == 30] | print("largest |kappa_a - kappa_b| over windows:", float(np.abs(d.kappa_a - d.
14 markdown 479 ## The surrogate reference |  | Asked for by the verifier in round 1. Which surrogate windows set kappa_
15 code 3471 S30 = W[(W.length == 30) & W.phase.isin(["active", "passive", "nni_a"])] | cols = ["path", "phase", "t
16 markdown 966 **Surrogate reference.** The largest surrogate kurtosis (34.29, active phase) comes from a window wi
17 markdown 426 ## Trial density |  |
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python -c "
import json
nb=json.load(open('reproduce_cambrainha_2025.ipynb'))
for i in [11,14,16,80,81,82,83]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
"; python -c "
import json
nb=json.load(open('../../executed/cambrainha-2025/reproduce_cambrainha_2025.ipynb'))
for i in [10,15,81]:
    print('=====OUT',i)
    for o in nb['cells'][i].get('outputs',[]):
        print(''.join(o.get('text','')) or o.get('data',{}).get('text/plain',''))
"
```

```
===== 11
## How readings decide

The claims file lists readings of details the paper leaves open (O1 to O11). Following the protocol (reader, step 3; author, step 1.6), two kinds are told apart:

- Readings of which trials, windows or subset a reported number counts (O1, O4, O5, and the two ranges of fig3d-relative-gain-24) decide as the criteria say: the claim is reproduced when the result matches under any of them.
- Readings of a method detail (O2, the CV; O6, kappa_surr_max; O8 to O10) decide only when they all give the same outcome. Where they differ, the reading the paper best supports is adopted as an assumption, and the outcome is marked as resting on it. The adopted readings are O2 (a), the CV of the population count: the Appendix describes the CV exclusion as removing rare artefacts ("such high values are not typically observed in awake mice"), and reading (b) removes 9702 of 11639 active windows (printed in the data check) while (a) removes none and (c) 209. O6 (a) for Figure 3 claims, and (b) for Figures 4A and S8, whose shaded area is one for all phases. O9 (a, a, a) and O10 (a), the first listed.

The adopted reading of O6 (the largest surrogate kurtosis) puts kappa_surr_max at 34.29 in the active phase and 48.34 over all phases, above the plotted ranges, so the criteria's grids are empty. That maximum is set by a few surrogate windows (13 of 28335 above 15), not by windows with few active units (section "The surrogate reference"). For the claims judged on a grid from kappa_surr_max, the criterion is therefore also applied with the grid started at every threshold from 3 up to the top of the plotted range, and at four named starts: the paper's value of about 7 (M4, read from Figures 3C, 3D and 4A), the 99th and 99.9th percentiles of the active surrogate kurtoses, and the maximum over windows with at least 128 active units. Where every start gives the same outcome, that is the outcome, and the start does not matter. Where the starts disagree (figs3-expon
[... 329 more lines not kept]
```

**Agent calls Bash**

```bash
cd ../..; grep -n "proposed\|\"findings\"\|'findings'\|agrees" tools/entry.py | head -50; ls schema* docs | head -30
```

```
288:                n_then, n_now = len(earlier.get("findings") or []), len(attempt.get("findings") or [])
289:                numbers = [f.get("finding") for f in rec.get("findings") or []]
293:                for f in rec.get("findings") or []:
306:            kinds = {f.get("kind") for f in attempt.get("findings") or []}
352:        for n, f in enumerate(attempt.get("findings") or [], 1):
400:        for item in (attempt.get("findings_review") or {}).get("findings") or []:
401:            number, its = item["finding"], attempt.get("findings") or []
410:            for item in rnd.get("findings") or []:
411:                if item["finding"] > len(attempt.get("findings") or []):
413:                                        f"has {len(attempt.get('findings') or [])} findings")
419:                agreed[r["claim"]] = r.get("outcome") if r.get("agrees") else None
439:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
docs:
agents
archives.md
author-responses.md
badges.md
conversion-tracker.md
design.md
encore.md
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 270,300p tools/entry.py; sed -n 405,445p tools/entry.py; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
d=s.get('\$defs',s.get('definitions',{}))
print(json.dumps({k:v for k,v in d.items() if k in ('proposed','verification','verification_finding','result')},indent=1)[:4000])
print(list(d))
"
```

```
attempt = load(report, path)
        if not isinstance(attempt, dict) or attempt.get("entry") != entry["name"]:
            continue
        validate(report, path, "attempt")
        where = path.relative_to(ROOT)
        # The entry streams the versions of its latest attempt; earlier attempts keep the versions they used.
        for used in attempt.get("datasets") or ([attempt["dataset"]] if attempt.get("dataset") else []):
            pinned = versions.get(str(used.get("id")))
            version = used.get("version")
            if pinned and path == mine[-1] and version != pinned:
                report.error(where, f"dataset {used.get('id')} version {version!r} differs from {pinned!r} in entry.yaml")
        # A repeat attempt's reconciliation points into the earlier record's findings and its own by number.
        rec = attempt.get("reconciliation")
        if isinstance(rec, dict):
            earlier = load(Report(), ROOT / "attempts" / f"{rec.get('earlier')}.yaml")
            if not isinstance(earlier, dict):
                report.error(where, f"reconciliation: no attempt record {rec.get('earlier')!r}")
            else:
                n_then, n_now = len(earlier.get("findings") or []), len(attempt.get("findings") or [])
                numbers = [f.get("finding") for f in rec.get("findings") or []]
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
def find(o,path=''):
    if isinstance(o,dict):
        for k,v in o.items():
            if k in ('proposed','verifications'): print(path+'/'+k, json.dumps(v)[:3000]); print()
            find(v,path+'/'+k)
    elif isinstance(o,list):
        for i,v in enumerate(o): find(v,path+f'[{i}]')
find(s)
"
```

```
/properties/outcomes/items/properties/proposed {"description": "A change of outcome found after the last verification round, held until a further round agrees with it.", "type": "object", "additionalProperties": false, "required": ["outcome", "reason"], "properties": {"outcome": {"enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}, "blocked_by": {"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}, "reason": {"type": "string", "minLength": 1}}}

/properties/verifications {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["date", "kind", "by", "results"], "properties": {"date": {"type": "string", "format": "date"}, "kind": {"enum": ["agent", "person", "paper_author"]}, "by": {"type": "string"}, "results": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["claim", "agrees"], "properties": {"claim": {"type": "string"}, "agrees": {"type": "boolean"}, "reason": {"description": "The verifier's reason, in its own words.", "type": "string"}, "response": {"description": "What the author changed or replied, kept apart from the verifier's reason.", "type": "string"}, "outcome": {"description": "The outcome the verifier would give.", "enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}}}}, "reviewed": {"description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.", "type": "string"}, "findings": {"description": "From protocol pilot-18, in round 2: what the verifier said of each finding the record rates `critical` (docs/protocol.md, the attempt record).", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["finding", "agrees"], "properties": {"finding": {"description": "The finding's number in this record's `findings`, from 1.", "type": "inte
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cat executed/cambrainha-2025/result.json | head -30; python -c "
import json
nb=json.load(open('executed/cambrainha-2025/reproduce_cambrainha_2025.ipynb'))
for o in nb['cells'][84].get('outputs',[]): print(o.get('text'))
for o in nb['cells'][66].get('outputs',[]): print(''.join(o.get('text',''))[:1500])
"; grep -n "few active\|every start\|do not depend\|48.34" entries/cambrainha-2025/README.md
```

```
{
 "entry": "cambrainha-2025",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_cambrainha_2025.ipynb",
   "ok": true,
   "seconds": 1819,
   "error": null
  }
 ]
}
['notebook run time: 30.2 min\n']
per-window fits: 64236 in 86 s
windows with a failed fit (NaN), per quantity, real windows:
{'beta_aa': 1, 'alpha_a': 1, 'z_a': 1, 'mu_a': 9, 'beta_ab': 54, 'mu_b': 14, 'beta_ba': 14, 'alpha_b': 14, 'z_b': 14, 'beta_bb': 69, 'mu_c': 9, 'mu_d': 14}
mu windows with r^2 >= 0.85 (real): reading a 0.017, reading b 0.043

session values computed: 192 (109 s)

[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/cambrainha-2025/README.md
```

```
# Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025) from dandiset 000713

Tests the findings of [Cambrainha et al. (2025)](https://doi.org/10.1103/w49n-2vz8), "Criticality
at Work: Scaling in the Mouse Cortex Enhances Performance", on
[DANDI:000713](https://dandiarchive.org/dandiset/000713/0.240702.1725), the Allen Institute Visual
Behavior Neuropixels data. For each 30-s window of V1 spiking it computes the kurtosis after
momentum-space coarse graining and an ISI-shuffled surrogate, relates it to the hit rate of the
change-detection task, compares the active, passive and non-natural image phases, and fits the
real-space renormalization exponents.

| Claim | Outcome |
|---|---|
| 62 sessions (44 mice) have more than 128 V1 units | Not reproduced |
| Kurtosis spans a broad range above the surrogates, lowest surrogates around 6 | Partially reproduced (assumed) |
| Hit rate over scaling windows is higher than over no-scaling windows and the shuffle | Not reproduced (assumed) |
| Hit rate over scaling windows rises with the threshold | Not reproduced (assumed) |
| Relative performance gain reaches 24% | Not reproduced |
| Similar results with 10-s and 60-s windows | Not reproduced |
| Similar results with strictly sorted units (43 sessions) | Not reproduced (assumed) |
| More windows above threshold in active than passive than non-natural images | Not reproduced (assumed) |
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python - <<'EOF'
import json
p='reproduce_cambrainha_2025.ipynb'
nb=json.load(open(p))
c=nb['cells'][81]; s=''.join(c['source'])
old='''            dep = [abs(s_[e].mean() - allv) for s_ in per if len(s_) and s_[e].notna().sum() >= 10]
            worst = max(dep) if dep else 0.0
            rows.append(dict(cv=cv, phase=ph, exponent=e, all_windows=allv, sd_at_lo=sd, points=len(dep),
                             largest_departure=worst, within=bool(len(dep) > 0 and worst <= sd)))'''
new='''            dep = [abs(s_[e].mean() - allv) for s_ in per if len(s_) and s_[e].notna().sum() >= 10]
            most = max([int(s_[e].notna().sum()) for s_ in per if len(s_)] or [0])
            worst = max(dep) if dep else 0.0
            rows.append(dict(cv=cv, phase=ph, exponent=e, all_windows=allv, sd_at_lo=sd, points=len(dep),
                             most_sessions=most, largest_departure=worst,
                             within=bool(len(dep) > 0 and worst <= sd)))'''
assert old in s; s=s.replace(old,new)
old2='''        t = stable_eval(cv, g)
        print(f"cv {cv}, start {name}'''
new2='''        t = stable_eval(cv, g)
        TABLES3[(cv, name)] = t
        print(f"cv {cv}, start {name}'''
assert old2 in s; s=s.replace(old2,new2)
old3='''            t = stable_eval(cv, g)
            print(f"cv {cv}, O6 {sm}'''
new3='''            t = stable_eval(cv, g)
            TABLES3[(cv, f"O6 ({sm})")] = t
            print(f"cv {cv}, O6 {sm}'''
assert old3 in s; s=s.replace(old3,new3)
s=s.replace('rows = []\nfor cv in CVS:\n    for sm in SMAXS:','TABLES3 = {}\nrows = []\nfor cv in CVS:\n    for sm in SMAXS:',1)
assert 'TABLES3 = {}' in s
s=s.replace('VS3 = stable_eval("a", np.arange(4, 12.01, 0.5))','VS3 = stable_eval("a", np.arange(4, 12.01, 0.5))\nTABLES3[("a", "4 to 12")] = VS3')
c['source']=s.splitlines(keepends=True)
new_code='''# Verifier round 2: the criterion read literally. "At every grid point with at least 10 sessions
# contributing" holds vacuously for an exponent with no such point; the verdict above counts that
# exponent as not shown stable. Both conventions, for every grid run above.
rows = []
for (cv, name), t in TABLES3.items():
    v = t.assign(within=(t.points == 0) | (t.largest_departure <= t.sd_at_lo))
    lit, lit_f = stable_verdict(v)
    strict, strict_f = stable_verdict(t)
    rows.append(dict(cv=cv, start=name, verdict_no_point_fails=strict, failing=strict_f,
                     verdict_literal=lit, failing_literal=lit_f,
                     no_point=",".join(f"{r.phase}:{r.exponent}" for r in t.itertuples() if r.points == 0)))
print(pd.DataFrame(rows).to_string(index=False))
print("\\nmost sessions with a mu at any grid point, start 7, cv a:")
print(TABLES3[("a", "paper 7")].query("exponent == 'mu'")[["phase", "points", "most_sessions"]].to_string(index=False))
'''
cell={'cell_type':'code','execution_count':None,'metadata':{},'outputs':[],'source':new_code.splitlines(keepends=True)}
nb['cells'].insert(82,cell)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat .; head -c 300 reproduce_cambrainha_2025.ipynb; git show HEAD:entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb | head -c 300; git show HEAD:entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb | tail -c 100 | od -c | tail -3
```

```
.../reproduce_cambrainha_2025.ipynb                | 30 +++++++++++++++++++++-
 1 file changed, 29 insertions(+), 1 deletion(-)
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ead87ed8",
   "metadata": {},
   "source": [
    "# Reproducing Cambrainha et al. (2025) from dandiset 000713\n",
    "\n",
    "Paper. Cambrainha, Castro, de Vasconcelos, Carelli & Copelli (2025), \"Criticality at Work: Scaling in the Mouse Co{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ead87ed8",
   "metadata": {},
   "source": [
    "# Reproducing Cambrainha et al. (2025) from dandiset 000713\n",
    "\n",
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python - <<'EOF'
import json
p='reproduce_cambrainha_2025.ipynb'
nb=json.load(open(p))
nb['cells'][82]['id']='figs3literal'
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff . | head -80
```

```
diff --git a/entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb b/entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb
index c250efc..fa1752d 100644
--- a/entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb
+++ b/entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb
@@ -2263,9 +2263,11 @@
     "            allv = base[e].mean()\n",
     "            sd = per[0][e].std() if len(g) and len(per[0]) else np.nan\n",
     "            dep = [abs(s_[e].mean() - allv) for s_ in per if len(s_) and s_[e].notna().sum() >= 10]\n",
+    "            most = max([int(s_[e].notna().sum()) for s_ in per if len(s_)] or [0])\n",
     "            worst = max(dep) if dep else 0.0\n",
     "            rows.append(dict(cv=cv, phase=ph, exponent=e, all_windows=allv, sd_at_lo=sd, points=len(dep),\n",
-    "                             largest_departure=worst, within=bool(len(dep) > 0 and worst <= sd)))\n",
+    "                             most_sessions=most, largest_departure=worst,\n",
+    "                             within=bool(len(dep) > 0 and worst <= sd)))\n",
     "    return pd.DataFrame(rows)\n",
     "\n",
     "\n",
@@ -2275,6 +2277,7 @@
     "        \",\".join(ok_e.index[~ok_e])\n",
     "\n",
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python - <<'EOF'
import json
p='reproduce_cambrainha_2025.ipynb'
nb=json.load(open(p))
def rep(i, old, new):
    s=''.join(nb['cells'][i]['source']); assert old in s, (i, old); s=s.replace(old,new)
    nb['cells'][i]['source']=s.splitlines(keepends=True)
rep(11, "That maximum is set by a few surrogate windows (13 of 28335 above 15), not by windows with few active units (section \"The surrogate reference\").",
 "That maximum is set by a few surrogate windows (13 of 28335 above 15) (section \"The surrogate reference\"). The active maximum (34.29) comes from a window with 182 active units. The all-phase maximum (48.34) comes from a passive window of sub-545994 with 87 active units and 84 silent ones, and the next value (36.50) from a window of the same session with 12 active units; with at least 128 active units the all-phase maximum falls to 34.29.")
rep(11, "Where every start gives the same outcome, that is the outcome, and the start does not matter. Where the starts disagree (figs3-exponents-stable-with-threshold), the paper's value of about 7 is adopted as an assumption.",
 "For four of these claims (fig3c-scaling-hit-rate-higher, fig3c-hit-rate-rises-with-threshold, fig4a-active-most-scaling, figs8-halves-and-phase-order) every start gives the same outcome, so the start does not matter. figs3-exponents-stable-with-threshold is run only at the named starts and on a variant grid from 4, and there the starts disagree, so the paper's value of about 7 is adopted as an assumption.")
rep(11, "because the hit rate, phase order and exponent results here do not depend on where the threshold or the grid start is put (for example, under CV (a) the scaling hit rate is below the no-scaling hit rate at every threshold from 3 to 15).",
 "because the hit rate and phase order results here do not depend on where the threshold or the grid start is put (for example, under CV (a) the scaling hit rate is below the no-scaling hit rate at every threshold from 3 to 15). The exponent stability result (figs3-exponents-stable-with-threshold) does depend on the start: from 7 and from the 99th percentile it is not reproduced, from the 99.9th percentile partially reproduced.")
rep(16, "so it is not a window with few units: leaving out windows with fewer than 64 or 128 active units leaves the active maximum at 34.29 (over all phases it falls from 48.34 to 34.29 with at least 128 units).",
 "so the active maximum is not set by a window with few units: leaving out windows with fewer than 64 or 128 active units leaves it at 34.29. The all-phase maximum (48.34, used for fig4a-active-most-scaling and figs8-halves-and-phase-order under O6 (b)) is set by a passive window of sub-545994 with 87 active units, 84 silent ones, a rate of 0.031 and a CV (a) of 3.89, and the next value (36.50) by a window of the same session with 12 active units; with at least 128 active units the all-phase maximum falls to 34.29. These two windows look like the recording dropouts of the data check.")
rep(83, "Two exponents fail, so the claim is not reproduced. Counting an exponent with no evaluable point as passing would leave z alone failing, which gives partially reproduced. The starts disagree: from the 99th percentile (6.51) the outcome is the same, from the 99.9th (10.43) and under CV (b) only mu fails (partially reproduced).",
 "Two exponents fail, so the claim is not reproduced, with an exponent that has no grid point where 10 sessions contribute counted as not shown stable. That is a second assumption. The starts disagree: from the 99th percentile (6.51) the outcome is the same, from the 99.9th (10.43) and under CV (b) only mu fails (partially reproduced).\n\nRead literally, the criterion holds vacuously for an exponent with no grid point where 10 sessions contribute (verifier, round 2). Under that reading the grid from 7 fails for NNI z alone, which gives partially reproduced; from the 99th percentile the same, and from the 99.9th percentile and under CV (b) reproduced (last cell). Passive and NNI mu are then not tested at all, since only 1.7% of windows pass the r^2 rule. The literal reading follows the criterion's wording, so the change to partially reproduced (resting on the start of 7 and CV (a)) is proposed for a third verification round; the verified outcome stays not reproduced until then.")
rep(84, "the claims judged on those grids are judged with the grid started at every threshold below it, and give the same outcome at every start except figs3-exponents-stable-with-threshold, where the paper's value of about 7 is adopted.",
 "four of the claims judged on those grids are judged with the grid started at every threshold below it and give the same outcome at every start; figs3-exponents-stable-with-threshold is judged only at named starts (7, the 99th and 99.9th percentiles) and on a grid from 4, its outcome differs between them, and the paper's value of about 7 is adopted.")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
python -c "
import json
nb=json.load(open('reproduce_cambrainha_2025.ipynb'));print(''.join(nb['cells'][83]['source'])[:300])"
```

```
**Result: not reproduced**, resting on CV (a) and on the grid start of 7, the paper's value of kappa_surr_max (M4), both assumptions. The criterion's grid from kappa_surr_max (34.29) is empty under CV (a) and (c). From 7 to 12 (101 points, every point evaluated), alpha and beta stay within one SD of
```

**Agent calls Bash**

```bash
cd entries/cambrainha-2025; python - <<'EOF'
import json
p='reproduce_cambrainha_2025.ipynb'
nb=json.load(open(p))
s=''.join(nb['cells'][83]['source'])
s=s.replace("counted as not shown stable. That is a second assumption.","counted as not shown stable, a third assumption.")
nb['cells'][83]['source']=s.splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
grep -c "third assumption" reproduce_cambrainha_2025.ipynb; date -u
```

```
1
Fri Nov 27 13:46:17 UTC 2026
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/cambrainha-2025/README.md",
 "old_string": "(34.29), which leaves the threshold ranges of five claims empty; they are judged with the range\nstarted at every threshold below it, which gives the same outcome at every start for four of them,\nand from the paper's value of about 7 for the fifth. Over",
 "new_string": "(34.29), which leaves the threshold ranges of five claims empty. Four of them are judged with the\nrange started at every threshold below it and give the same outcome at every start. The fifth, the\nstability of the exponents, is judged from a few named starts, which disagree, and from the paper's\nvalue of about 7; a change of its outcome to partially reproduced, under a literal reading of its\ncriterion, is proposed for a third verification round. Over"
}
```

```
The file entries/cambrainha-2025/README.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  date -u; time python tools/entry.py all entries/cambrainha-2025 2>&1 | tail -20
```

```
Fri Nov 27 13:46:24 UTC 2026
Installed kernelspec registry-cambrainha-2025 in executed/cambrainha-2025/.venv/share/jupyter/kernels/registry-cambrainha-2025
0 error(s)
pass  reproduce_cambrainha_2025.ipynb  (1893 s)

real	31m45.975s
user	68m20.672s
sys	2m30.088s
```

**Agent calls Bash**

```bash
python -c "
import json
nb=json.load(open('executed/cambrainha-2025/reproduce_cambrainha_2025.ipynb'))
for i in [82]:
    for o in nb['cells'][i].get('outputs',[]): print(''.join(o.get('text','')))
o=''.join(x.get('text','') for x in nb['cells'][81]['outputs']); print(o[-3500:])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 6, in <module>
    o=''.join(x.get('text','') for x in nb['cells'][81]['outputs']); print(o[-3500:])
TypeError: sequence item 0: expected str instance, list found
cv   start verdict_no_point_fails failing      verdict_literal failing_literal                      no_point
 b  O6 (a)   partially_reproduced      mu           reproduced                 active:mu,passive:mu,nni_a:mu
 b  O6 (b)   partially_reproduced      mu           reproduced                 active:mu,passive:mu,nni_a:mu
 a paper 7         not_reproduced    mu,z partially_reproduced               z           passive:mu,nni_a:mu
 a     p99         not_reproduced    mu,z partially_reproduced               z           passive:mu,nni_a:mu
 a   p99.9   partially_reproduced      mu           reproduced                 active:mu,passive:mu,nni_a:mu
 c paper 7         not_reproduced    mu,z partially_reproduced               z           passive:mu,nni_a:mu
 c     p99         not_reproduced    mu,z partially_reproduced               z           passive:mu,nni_a:mu
 c   p99.9   partially_reproduced      mu           reproduced                 active:mu,passive:mu,nni_a:mu
 a 4 to 12         not_reproduced    mu,z partially_reproduced               z                      nni_a:mu

most sessions with a mu at any grid point, start 7, cv a:
  phase  points  most_sessions
 active      64             32
passive       0              7
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json
nb=json.load(open('executed/cambrainha-2025/reproduce_cambrainha_2025.ipynb'))
t=lambda i: ''.join(''.join(x.get('text','')) for x in nb['cells'][i].get('outputs',[]))
print(t(81)[-2600:-1300]); print(t(15)[:900]); print(t(85))
"
```

```
0.031    True
 c   nni_a     beta        0.836     0.060      32             81              0.003    True
 c   nni_a       mu        1.338       NaN       0              1              0.000   False
 c   nni_a        z        0.192     0.149      32             81              0.083    True

verdicts:
cv      start  kappa_start  grid_points              verdict failing
 a     O6 (a)       34.292            0              no grid     NaN
 a     O6 (b)       48.341            0              no grid     NaN
 b     O6 (a)        8.532           70 partially_reproduced      mu
 b     O6 (b)       10.302           34 partially_reproduced      mu
 c     O6 (a)       34.292            0              no grid     NaN
 c     O6 (b)       34.292            0              no grid     NaN
 a    paper 7        7.000          101       not_reproduced    mu,z
 a        p99        6.511          110       not_reproduced    mu,z
 a      p99.9       10.425           32 partially_reproduced      mu
 a max N>=128       34.292            0              no grid     NaN
 c    paper 7        7.000          101       not_reproduced    mu,z
 c        p99        6.511          110       not_reproduced    mu,z
 c      p99.9       10.425           32 partially_reproduced      mu
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/cambrainha-2025-01.yaml'
s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1, old
    s=s.replace(old,new)
rep("""  notes: Under the adopted CV reading (a), and under (c), kappa_surr_max is 34.29 (O6 (a)) or 48.34
    (O6 (b)), so the criterion's grid to 12.5 is empty.""",
"""  notes: Under the adopted CV reading (a) kappa_surr_max is 34.29 (O6 (a)) or 48.34 (O6 (b)), and
    under (c) 34.29 under both, so the criterion's grid to 12.5 is empty.""")
rep("""    partially reproduced (93.8% of 96 points) and the gain at 12 is 66.08% on 4 trials, which would give
    partially reproduced; across the five seeds of the strict surrogate that reading gives
    partially reproduced or reproduced. On""",
"""    partially reproduced (93.8% of 96 points) and the gain at 12 is 66.08% on 4 trials; across the
    five seeds of the strict surrogate that fig3c test gives partially reproduced or reproduced. The
    claim itself is not reproduced under every CV reading, as no session count is within tolerance.
    On""")
rep("""  notes: Under CV (a) and (c) the grid from kappa_surr_max (34.29) to 12 is empty. From the paper's""",
"""  proposed:
    outcome: partially_reproduced
    reason: The criterion asks for stability "at every grid point with at least 10 sessions
      contributing", which holds vacuously for an exponent with no such point; the verified outcome
      counted such an exponent as not shown stable, a convention the criterion does not state. Read
      literally, the grid from 7 (CV (a)) fails for NNI z alone (0.083 against an SD of 0.058), so
      three of four exponents hold, which is partially reproduced (resting on CV (a) and the start of
      7). Passive and NNI mu are then not tested, as no grid point has 10 sessions with a mu (at most
      7 and 6; 1.7% of windows pass the r^2 rule). From the 99th percentile the literal reading gives
      the same, from the 99.9th percentile and under CV (b) reproduced (notebook, the cell after the
      figs3 verdicts). Raised by the verifier in round 2.
  notes: Under CV (a) and (c) the grid from kappa_surr_max (34.29) to 12 is empty. From the paper's""")
rep("""    exponents fail, so not reproduced. Counting an exponent with no evaluable point as passing
    would leave z alone failing (partially reproduced).""",
"""    exponents fail, so not reproduced. Read literally, the criterion holds vacuously for an exponent
    with no evaluable point; that leaves z alone failing (partially reproduced; proposed above). At
    most 7 passive and 6 NNI sessions have a mu at any point from 7, against 32 active.""")
rep("""  - An exponent with no grid point where 10 sessions contribute is counted as not shown stable.""",
"""  - An exponent with no grid point where 10 sessions contribute is counted as not shown stable. This
    is an assumption the outcome rests on; the literal reading of the criterion (the condition holds
    vacuously) gives partially reproduced from 7, and a change to that outcome is proposed.""")
rep("""    above 15), which leaves every plotted threshold range empty. The windows that set it are not
    windows with few active units. Five""",
"""    above 15), which leaves every plotted threshold range empty. The active maximum (34.29) comes from
    a window with 182 active units. The all-phase maximum (48.34) comes from a passive window of
    sub-545994 with 87 active and 84 silent units, and the next value (36.50) from a window of the
    same session with 12 active units; with at least 128 active units the all-phase maximum falls to
    34.29. Five""")
open(p,'w').write(s)
EOF
grep -n "Five claims are judged" -A3 attempts/cambrainha-2025-01.yaml
```

```
Traceback (most recent call last):
  File "<stdin>", line 11, in <module>
  File "<stdin>", line 5, in rep
AssertionError:     partially reproduced (93.8% of 96 points) and the gain at 12 is 66.08% on 4 trials, which would give
    partially reproduced; across the five seeds of the strict surrogate that reading gives
    partially reproduced or reproduced. On
368:    windows with few active units. Five claims are judged with the range started at every threshold
369-    below it. Question for the authors. Is kappa_surr_max the maximum over every surrogate window of
370-    all sessions, one surrogate per window, or another summary?
371-- kind: methods_unavailable
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/cambrainha-2025-01.yaml'
s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1, old
    s=s.replace(old,new)
rep("""  notes: Under the adopted CV reading (a), and under (c), kappa_surr_max is 34.29 (O6 (a)) or 48.34
    (O6 (b)), so the criterion's grid to 12.5 is empty.""",
"""  notes: Under the adopted CV reading (a) kappa_surr_max is 34.29 (O6 (a)) or 48.34 (O6 (b)), and
    under (c) 34.29 under both, so the criterion's grid to 12.5 is empty.""")
rep("""    reproduced (93.8% of 96 points) and the gain at 12 is 66.08% on 4 trials, which would give
    partially reproduced; across the five seeds of the strict surrogate that reading gives
    partially reproduced or reproduced. On""",
"""    reproduced (93.8% of 96 points) and the gain at 12 is 66.08% on 4 trials; across the five seeds
    of the strict surrogate that fig3c test gives partially reproduced or reproduced. The claim
    itself is not reproduced under every CV reading, as no session count is within tolerance. On""")
rep("""  notes: Under CV (a) and (c) the grid from kappa_surr_max (34.29) to 12 is empty. From the paper's""",
"""  proposed:
    outcome: partially_reproduced
    reason: The criterion asks for stability "at every grid point with at least 10 sessions
      contributing", which holds vacuously for an exponent with no such point; the verified outcome
      counted such an exponent as not shown stable, a convention the criterion does not state. Read
      literally, the grid from 7 (CV (a)) fails for NNI z alone (0.083 against an SD of 0.058), so
      three of four exponents hold, which is partially reproduced (resting on CV (a) and the start of
      7). Passive and NNI mu are then not tested, as no grid point has 10 sessions with a mu (at most
      7 and 6; 1.7% of windows pass the r^2 rule). From the 99th percentile the literal reading gives
      the same, from the 99.9th percentile and under CV (b) reproduced (notebook, the cell after the
      figs3 verdicts). Raised by the verifier in round 2.
  notes: Under CV (a) and (c) the grid from kappa_surr_max (34.29) to 12 is empty. From the paper's""")
rep("""    exponents fail, so not reproduced. Counting an exponent with no evaluable point as passing
    would leave z alone failing (partially reproduced).""",
"""    exponents fail, so not reproduced. Read literally, the criterion holds vacuously for an exponent
    with no evaluable point; that leaves z alone failing (partially reproduced; proposed above). At
    most 7 passive and 6 NNI sessions have a mu at any point from 7, against 32 active.""")
rep("""  - An exponent with no grid point where 10 sessions contribute is counted as not shown stable.""",
"""  - An exponent with no grid point where 10 sessions contribute is counted as not shown stable. This
    is an assumption the outcome rests on; the literal reading of the criterion (the condition holds
    vacuously) gives partially reproduced from 7, and a change to that outcome is proposed.""")
rep("""    above 15), which leaves every plotted threshold range empty. The windows that set it are not
    windows with few active units. Five""",
"""    above 15), which leaves every plotted threshold range empty. The active maximum (34.29) comes from
    a window with 182 active units. The all-phase maximum (48.34) comes from a passive window of
    sub-545994 with 87 active and 84 silent units, and the next value (36.50) from a window of the
    same session with 12 active units; with at least 128 active units the all-phase maximum falls to
    34.29. Five""")
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/cambrainha-2025-01.yaml'
s=open(p).read()
old="""    34.29. Five claims are judged with the range started at every threshold
    below it."""
assert old in s
s=s.replace(old,"""    34.29. Four claims are judged with the range started at every threshold
    below it, and a fifth (figs3-exponents-stable-with-threshold) at named starts.""")
open(p,'w').write(s)
EOF
grep -n "Four claims" -B2 -A3 attempts/cambrainha-2025-01.yaml
```

```
383-    sub-545994 with 87 active and 84 silent units, and the next value (36.50) from a window of the
384-    same session with 12 active units; with at least 128 active units the all-phase maximum falls to
385:    34.29. Four claims are judged with the range started at every threshold
386-    below it, and a fifth (figs3-exponents-stable-with-threshold) at named starts. Question for the authors. Is kappa_surr_max the maximum over every surrogate window of
387-    all sessions, one surrogate per window, or another summary?
388-- kind: methods_unavailable
```

**Agent**

Now the round-2 verification record.

**Agent calls Bash**

```bash
cd  cat >> attempts/cambrainha-2025-01.yaml <<'EOF'
- date: 2026-11-27
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the
    notebook)
  reviewed: The full executed notebook after the round-1 revision, the helper module criticality.py,
    the claims file and the attempt record, with the paper's full text. Report in
    transcripts/cambrainha-2025/verifier-2-report.md.
  results:
  - claim: sessions-selected
    agrees: true
    outcome: not_reproduced
    reason: No assumption needed; gives the same verdict under every reading. All analyses run on 97
      sessions from 68 mice, not the paper's 62 from 44, which cannot be resolved from the files.
    response: No change.
  - claim: fig3a-kurtosis-broader-than-surrogate
    agrees: true
    outcome: partially_reproduced
    reason: Rests on CV reading (a); the assumption is stated and is reasonable. Reading (a) drops 0
      of 11,639 active windows, (b) drops 9,702 and (c) drops 209, and the paper calls the exclusion a
      removal of rare artefacts. (a) gives partially reproduced, (c) not reproduced. The surrogate
      median is 3.64 and the minimum 2.80, against the paper's about 6; the correlation-matrix
      variant overshoots instead (surrogate median 15.88). This is stated, and asked of the authors.
    response: No change.
  - claim: fig3c-scaling-hit-rate-higher
    agrees: true
    outcome: not_reproduced
    reason: Rests on CV reading (a), stated and reasonable; the readings disagree only through CV (b).
      Under the claims file's literal rule an empty grid "cannot meet the criterion", so it is not
      reproduced under CV (a) whatever the start. The notes say "Under the adopted CV reading (a),
      and under (c), kappa_surr_max is 34.29 (O6 (a)) or 48.34 (O6 (b))"; under CV (c), O6 (b) gives
      34.29, not 48.34. Trial counting (O5) has no reading that counts aborted trials, the only rule
      that matches the paper's three to five trials per window; under it the outcome stays not
      reproduced (47.7% of points from 7), so this is a claims-file point, not an outcome change.
    response: Corrected the notes (under CV (c) kappa_surr_max is 34.29 under both O6 readings). The
      O5 point is already in the questions file. Outcome unchanged.
  - claim: fig3c-hit-rate-rises-with-threshold
    agrees: true
    outcome: not_reproduced
    reason: Rests on CV reading (a), stated and reasonable; the readings disagree only through CV (b),
      and under the literal rule an empty grid cannot meet the criterion.
    response: No change.
  - claim: fig3d-relative-gain-24
    agrees: true
    outcome: not_reproduced
    reason: No assumption needed; gives the same verdict under every reading. Counting aborted trials
      the outcome stays not reproduced (+11.72% at 8 and -22.40% at 12).
    response: No change.
  - claim: figs1-other-window-lengths
    agrees: true
    outcome: not_reproduced
    reason: No assumption needed; gives the same verdict under every reading.
    response: No change.
  - claim: figs2-strict-units
    agrees: true
    outcome: not_reproduced
    reason: Rests on CV reading (a), stated and reasonable; CV (b) would give partially reproduced.
      The notes say "across the five seeds of the strict surrogate that reading gives partially
      reproduced or reproduced"; this is the verdict of the fig3c sub-test. figs2 itself cannot be
      reproduced, because no session count is within tolerance. The sentence should say so.
    response: Corrected the notes. They now say that the seed verdicts are those of the fig3c test,
      and that the claim is not reproduced under every CV reading, as no session count is within
      tolerance.
  - claim: fig4a-active-most-scaling
    agrees: true
    outcome: not_reproduced
    reason: Rests on CV reading (a), stated and reasonable; the readings disagree only through CV (b).
      The statement that the windows setting kappa_surr_max are not windows with few active units
      holds only for the active-phase maximum (34.29, N = 182). The all-phase maximum used here (O6
      (b)) is 48.34, from a passive window of sub-545994 with 87 active units, 84 silent, a rate of
      0.031 and CV (a) 3.89; the next value, 36.50, comes from a window with 12 active units. With N
      >= 128 it falls to 34.29. No outcome changes, because every start was run.
    response: Corrected the sentence in the notebook ("How readings decide" and "Surrogate reference")
      and in the kappa_surr_max finding, which now give the windows that set the all-phase maximum.
      Outcome unchanged.
  - claim: fig4-exponents-active
    agrees: true
    outcome: not_reproduced
    reason: No assumption needed; gives the same verdict under every reading. Fitting ranks 1 to K/2
      gives mu = 1.06, still outside tolerance.
    response: No change.
  - claim: fig4-exponents-passive
    agrees: true
    outcome: not_reproduced
    reason: No assumption needed; gives the same verdict under every reading.
    response: No change.
  - claim: fig4-exponents-nni
    agrees: true
    outcome: not_reproduced
    reason: No assumption needed; gives the same verdict under every reading.
    response: No change.
  - claim: fig4bc-static-exponents-trend
    agrees: true
    outcome: partially_reproduced
    reason: No assumption needed; gives the same verdict under every reading. The paired Wilcoxon
      test is added.
    response: No change.
  - claim: figs3-exponents-stable-with-threshold
    agrees: false
    outcome: partially_reproduced
    reason: Agrees only in part. The record states the grid start of 7 (M4) as an assumption, but the
      verdict also rests on a second convention, listed only as a deviation, that "an exponent with no
      grid point where 10 sessions contribute is counted as not shown stable". The criterion says the
      condition must hold "at every grid point with at least 10 sessions contributing"; with no such
      point, that is met vacuously. Read literally, the grid from 7 fails only NNI z (0.083 against
      an SD of 0.058), which gives partially reproduced. Passive and NNI mu are not evaluable because
      only 1.7% of windows pass the r^2 rule, so mu was never really tested. The verifier would rate
      it partially reproduced (assumed); at minimum, the convention should be stated as an assumption
      the outcome rests on. The sentence "the hit rate, phase order and exponent results here do not
      depend on where the threshold or the grid start is put" is wrong for the exponents, and the
      summary's "give the same outcome at every start except figs3" overstates, as figs3 was run only
      at the named starts and on the 4 to 12 variant.
    response: In round 2 the outcome may not change, so it stays not reproduced and the change to
      partially reproduced is proposed (`proposed`), for a third round. The convention is now stated
      as an assumption in the deviations and the result cell. A cell gives the verdict under both
      conventions at every start run (literal reading, partially reproduced from 7 and the 99th
      percentile, reproduced from the 99.9th percentile and under CV (b)) and the most sessions with
      a mu at any point (7 passive, 6 NNI). The sentences of "How readings decide", the summary and the
      README now say that the exponent result depends on the start and was run only at named starts.
  - claim: figs4-initial-kurtosis-poor-predictor
    agrees: true
    outcome: reproduced
    reason: No assumption needed; gives the same verdict under every reading.
    response: No change.
  - claim: figs5a-firing-rate-order
    agrees: true
    outcome: reproduced
    reason: Rests on CV reading (a), stated and reasonable; CV (b) would give partially reproduced.
    response: No change.
  - claim: figs5c-hit-rate-firing-rate-nonmonotonic
    agrees: true
    outcome: reproduced
    reason: No assumption needed; gives the same verdict under every reading.
    response: No change.
  - claim: figs7-fatigue-halves
    agrees: true
    outcome: not_reproduced
    reason: Rests on CV reading (a), stated and reasonable; CV (b) would give reproduced.
    response: No change.
  - claim: figs8-halves-and-phase-order
    agrees: true
    outcome: not_reproduced
    reason: Rests on CV reading (a), stated and reasonable; the readings disagree only through CV (b).
      As for fig4a, the all-phase kappa_surr_max (48.34) is set by dropout windows of sub-545994, not
      by windows with many units; no outcome changes, because every start was run.
    response: Corrected the sentences on the all-phase maximum, as for fig4a-active-most-scaling.
      Outcome unchanged.
  findings:
  - finding: 1
    agrees: true
    reason: No finding is rated critical. Finding 1, selection_undocumented, is rightly major. It
      changes the analysis set of every claim.
  - finding: 6
    agrees: true
    reason: Minor is right; the block order is evident from the values.
  - finding: 7
    agrees: true
    reason: Minor is right; the trial density is evident from the values.
  - finding: 8
    agrees: true
    reason: Minor is right. The dropout windows of sub-545994 set the all-phase kappa_surr_max (48.34
      and 36.50), but that is evident from the printed N and rates, so minor is still the right
      rating.
  - finding: 9
    agrees: true
    reason: Severity none is right. No session is deposited twice and the clocks agree.
EOF
date -u; python tools/entry.py check entries/cambrainha-2025 2>&1 | tail -15
```

```
Fri Nov 27 14:19:29 UTC 2026
0 error(s)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/cambrainha-2025-01.yaml'
s=open(p).read()
old="""      As for fig4a, the all-phase kappa_surr_max (48.34) is set by dropout windows of sub-545994, not
      by windows with many units; no outcome changes, because every start was run."""
assert old in s
s=s.replace(old,"""      The all-phase maximum used for fig4a and figs8 (O6 (b)) is 48.34, from a passive window of
      sub-545994 with 87 active units and 84 silent; no outcome changes, because every start was run.""")
open(p,'w').write(s)
EOF
grep -n "—\|rather" attempts/cambrainha-2025-01.yaml entries/cambrainha-2025/README.md; python -c "
import json
nb=json.load(open('entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb'))
import re
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if '—' in s or 'rather' in s: print(i)
"; python tools/entry.py check entries/cambrainha-2025 2>&1 | tail -3; git status --short | grep -v tools/
```

```
0 error(s)
 M attempts/cambrainha-2025-01.yaml
 M entries/cambrainha-2025/README.md
 M entries/cambrainha-2025/reproduce_cambrainha_2025.ipynb
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
?? docs/outside-runs.md
?? scripts
```

**Agent**

I changed no outcomes. The one disagreement is now a proposal for a third verification round. The entry was re-run with `python tools/entry.py all entries/cambrainha-2025`: the notebook passed in 31 min and the checks show 0 errors. The new numbers match the earlier ones, and the conclusions match the printed outputs.

**The disagreement (figs3-exponents-stable-with-threshold)**
- The verified outcome stays not reproduced. I added a `proposed` change to partially_reproduced with its reason. The criterion asks for stability "at every grid point with at least 10 sessions contributing". When no grid point has 10 sessions, that condition holds trivially, so passive and NNI mu cannot fail. Read that way, the grid from 7 fails only for NNI z (0.083 against an SD of 0.058).
- The verdict had also rested on a convention listed only as a deviation: an exponent with no such grid point counted as not shown stable. That convention is now stated as an assumption the outcome rests on.
- A new notebook cell gives the verdict under both conventions at every start that was run. Under the literal reading the starts at 7 and at the 99th percentile give partially reproduced. The 99.9th percentile and CV (b) give reproduced.
- The same cell shows that at most 7 passive and 6 NNI sessions have a mu at any grid point, against 32 active. So mu was in effect not tested in those phases.

**Sentences corrected**
- **Notebook, "How readings decide":** the exponent result does depend on the grid start. That section, the summary and the README now say so, and that figs3 was run only at named starts (7, the 99th and 99.9th percentiles) and on the 4 to 12 grid.
- **The κ_surr_max finding (finding 3) and the "Surrogate reference" cells:** "not windows with few active units" holds only for the active maximum (34.29, 182 units). The all-phase maximum (48.34) comes from a passive dropout window of sub-545994 with 87 active and 84 silent units. The next value (36.50) comes from a window of the same session with 12 active units. With at least 128 active units the all-phase maximum falls to 34.29.
- **fig3c-scaling-hit-rate-higher notes:** under CV (c), κ_surr_max is 34.29 under both O6 readings, not 48.34.
- **figs2-strict-units notes:** the seed verdicts are those of the fig3c sub-test. The claim itself is not reproduced under every reading, because no session count is within tolerance.

**Recorded**
- Round 2 is under `verifications`: all 18 claims (17 agreed, figs3 not, with the verifier giving partially_reproduced), each with the verifier's reason and my response.
- No finding is rated `critical`. The round's `findings` still record that the verifier agreed with the ratings of findings 1 (major), 6 to 8 (minor) and 9 (none). No severity changed, and the findings keep their order.

**Not done, and why**
- **Questions file:** I added no question. The only claims-file point the verifier raised, whether aborted trials count (O5), is already in `questions/cambrainha-2025.yaml`.
- **Session selection:** the analysis still runs on 97 sessions from 68 mice, not the paper's 62 from 44. That cannot be resolved from the files, and it stays a finding.
- **Figures:** the verifier said it has still not compared the results with Figures 3A, 3C, 4A and S8. That is its own pending check, and it asked me for no output.
- **Stray files:** some untracked files appeared in the repo root during the run (`.bashrc`, `.profile`, `.vscode` and others). I did not create them on purpose and left them alone. They should probably not go into the workflow's commit.

Nothing was committed or pushed.

## End of run

28 turns, 36 minutes, $1.35 at API prices, result: success.
