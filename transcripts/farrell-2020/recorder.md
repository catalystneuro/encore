# crcns-ear-1 · recorder · run 42313574234

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/crcns-ear-1/ claims/crcns-ear-1/; python tools/readme_row.py crcns-ear-1; cat attempts/crcns-ear-1-farrell-2020-01.yaml
```

```
<persisted-output>
Output too large (123.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/77c25275-feef-45b4-8cac-56405ac4f8a5/tool-results/bnrtih909.txt

Preview (first 2KB):
docs/pilot-notes/crcns-pag-2-moaddab-2020-01.md
docs/pilot-notes/crcns-ssc-7-yu-2016-01.md
docs/pilot-notes/crcns-stc-1-gu-2011-01.md
docs/pilot-notes/001960-qi-2026-01.md
docs/pilot-notes/crcns-pfc-1-rodgers-2014-01.md
claims/crcns-ear-1/:
10.1085-jgp.201912447.yaml

transcripts/crcns-ear-1/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in crcns-pag-2-moaddab-2020-01 crcns-ssc-7-yu-2016-01 crcns-stc-1-gu-2011-01 001960-qi-2026-01 crcns-pfc-1-rodgers-2014-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; cat docs/pilot-notes/001754-knierim-2000-02.md | head -3
```

```
<persisted-output>
Output too large (44.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/77c25275-feef-45b4-8cac-56405ac4f8a5/tool-results/b1a73oyp7.txt

Preview (first 2KB):
=== crcns-pag-2-moaddab-2020-01
# crcns-pag-2, Moaddab et al. 2020

Thirteen claims reproduced (one on an assumption), four partially, one not
reproduced and two blocked, both for missing data. The first verification round
agreed with 19 of the 20 outcomes as they stood and the second with all 20;
nothing was proposed after the second, so there was no third round. CRCNS does
not version data sets, so the version is recorded as unversioned with the data
set's DOI (10.6080/K0833Q7F), and the zip's ETag matches `checksums.md5`. The
paper, Moaddab, Wright and McDannald in Scientific Reports (10, 18035), compares
12 female Long Evans rats given early adolescent adversity (EAA) with 8 Controls
in fear discrimination, where danger, uncertainty and safety cues predict foot
shock with probability 1.00, 0.375 and 0.00 while the rats nose poke for food,
and records 151 Control and 203 EAA single units in vlPAG/DR; the data set is
one `data.zip` holding the 354 unit files, the authors' cube built from them,
their script `vlpagAnalysis.m` and three cue sounds. The claims were written
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/77c25275-feef-45b4-8cac-56405ac4f8a5/tool-results/b1a73oyp7.txt"
}
```

```
1	=== crcns-pag-2-moaddab-2020-01
2	# crcns-pag-2, Moaddab et al. 2020
3	
4	Thirteen claims reproduced (one on an assumption), four partially, one not
5	reproduced and two blocked, both for missing data. The first verification round
6	agreed with 19 of the 20 outcomes as they stood and the second with all 20;
7	nothing was proposed after the second, so there was no third round. CRCNS does
8	not version data sets, so the version is recorded as unversioned with the data
9	set's DOI (10.6080/K0833Q7F), and the zip's ETag matches `checksums.md5`. The
10	paper, Moaddab, Wright and McDannald in Scientific Reports (10, 18035), compares
11	12 female Long Evans rats given early adolescent adversity (EAA) with 8 Controls
12	in fear discrimination, where danger, uncertainty and safety cues predict foot
13	shock with probability 1.00, 0.375 and 0.00 while the rats nose poke for food,
14	and records 151 Control and 203 EAA single units in vlPAG/DR; the data set is
15	one `data.zip` holding the 354 unit files, the authors' cube built from them,
16	their script `vlpagAnalysis.m` and three cue sounds. The claims were written
17	from the flattened JATS text of the version of record, without the supplement,
18	and without code, as the lab page the paper names returned 404. The behaviour,
19	cue-responsive selection, population firing, regression and correlation claims
20	could be tested; the body weights of Fig. 1B, C and the pre-surgery
[... 607 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/crcns-ear-1-farrell-2020-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
import sys
items = d if isinstance(d,list) else d.get('dandisets', d)
for x in (items if isinstance(items,list) else items.values()):
    if 'ear-1' in json.dumps(x): print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (122.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/77c25275-feef-45b4-8cac-56405ac4f8a5/tool-results/bz0nk8dsu.txt

Preview (first 2KB):
schema_version: 2
id: crcns-ear-1-farrell-2020-01
dataset:
  archive: crcns
  id: ear-1
  version: unversioned
  doi: 10.6080/K0571975
paper: doi:10.1085/jgp.201912447
date: '2026-11-06'
entry: crcns-ear-1-farrell-2020
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 42 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/77c25275-feef-45b4-8cac-56405ac4f8a5/tool-results/bz0nk8dsu.txt"
}
```

```
1	schema_version: 2
2	id: crcns-ear-1-farrell-2020-01
3	dataset:
4	  archive: crcns
5	  id: ear-1
6	  version: unversioned
7	  doi: 10.6080/K0571975
8	paper: doi:10.1085/jgp.201912447
9	date: '2026-11-06'
10	entry: crcns-ear-1-farrell-2020
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
[... 730 more lines not kept]
```

**Agent**

Still reading the attempt record (it is about 1,900 lines); then the reports.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/77c25275-feef-45b4-8cac-56405ac4f8a5/tool-results/bz0nk8dsu.txt",
 "offset": 750,
 "limit": 600
}
```

```
750	    slopes found in the claims it depends on), so the outcome stays not_reproduced. With edges e-b for
751	    all three fits (weighted, `first2`, dC > 5 pF kept), the reading under which fig3a-eq3a-fit is reproduced,
752	    the mean is -0.432, within tolerance. Keeping all bins (y-0), as before the round 1 verification,
753	    the mean was -0.150. Under L-c with y-1 it is -0.515, within.
754	  deviations:
755	  - Each slope is the first reading of its claim (edges at multiples of 5 pF, weighted unconstrained fit;
756	    XE991 cells with 144 mM chloride; CLn by `first2` with dC > 5 pF kept). Assumed, as the paper does
757	    not say how each slope was fitted; the readings change the outcome (7 of 16 combinations give a mean
758	    within tolerance), and all are shown.
759	  - CLW is CL - CNLW with CNLW = CSB + root per cell, reading L-b of the claims file's shared method as
760	    amended after the question in questions/crcns-ear-1.yaml; the data set stores no CLW, CNLW or CSB,
761	    so reading L-a cannot be used. CSB follows the method the paper cites ("We determined C N L W by calculating
762	    the capacitance of the stereocilia bundle and plotting ... Q T m ... as a function of C L - C S B
763	    to find the root", Expressions used to determine the experimental parameters, paragraph 2; Corbitt
764	    et al. 2012, doi:10.1016/j.bpj.2012.04.054, Methods), bundle area min(0.07 AM, 140 um2) times 0.0075
765	    pF/um2 with AM the stored cell surface area. This rule is assumed, as the paper does not state it;
766	    it gives the Fig. S1 cell CLW 18.30 pF, within the claims file's admissibility bound (18.56 +/- 1.856
767	    pF). The 6 cells without an area take the median CSB of their turn (assumed). The root, 5.104 pF,
768	    is that of QTm on ln(CL - CSB) over all 89 cells. CL - 4.82 pF (reading L-c) is shown for comparison
769	    and decides nothing.
[... 580 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/77c25275-feef-45b4-8cac-56405ac4f8a5/tool-results/bz0nk8dsu.txt",
 "offset": 1350,
 "limit": 560
}
```

```
1350	  - claim: v05-not-correlated-voltage-drop
1351	    agrees: true
1352	    outcome: reproduced
1353	    reason: All four Pearson tests p >= 0.065. One Spearman variant gives p = 0.038.
1354	    response: No change of outcome.
1355	  - claim: fig3a-eq3a-fit
1356	    agrees: true
1357	    outcome: reproduced
1358	    reason: Bin edges from the smallest CLW (e-b), weighted unconstrained fit (u-a), Vd 0.0311, R2 0.931,
1359	      slope -0.4245, R2 0.948, all four pass. Under edges at multiples of 5 pF (e-a), the slope misses
1360	      by 0.0001.
1361	    response: No change of outcome. The dVmin limit adopted for the other fits (y-1) leaves out no bin
1362	      of this fit, so its values are unchanged; y-2 (cells outside the range dropped before binning) is
1363	      shown and moves Vd to 0.0299 V.
1364	  - claim: fig3a-xe991-fit
1365	    agrees: true
1366	    outcome: not_reproduced
1367	    reason: Under L-b, no reading passes any value (Vd 0.077 to 0.085 V, R2 around -43). One 2-cell XE991
1368	      bin (file 57, CL 5.93 pF, CLW 0.475 pF, dVmin 1.33 V; bin mean 0.80 V) causes this. Refitted without
1369	      that bin, Vd 0.0505 V, R2 0.844, slope -0.376, R2 0.920, all within tolerance, so the paper's Fig.
[... 537 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml,collections
a=yaml.safe_load(open('attempts/crcns-ear-1-farrell-2020-01.yaml'))
o=a['outcomes'];print(len(o))
c=collections.Counter((x['outcome'],x.get('assumed',False),x.get('blocked_by')) for x in o);print(c)
for v in a['verifications']:print(sum(r['agrees'] for r in v['results']),len(v['results']))
E
grep -n "ear-1" -A12 targets/dandisets.json | head -40; grep -n "readme_row\|| Dataset\|Reproduced" README.md | head; sed -n 1,60p tools/readme_row.py
```

```
48
Counter({('reproduced', True, None): 13, ('reproduced', False, None): 10, ('not_reproduced', True, None): 9, ('blocked', False, 'other'): 5, ('partially_reproduced', True, None): 4, ('partially_reproduced', False, None): 3, ('blocked', False, 'data_missing'): 2, ('not_reproduced', False, None): 2})
45 48
48 48
"""The README's table row for a dataset, from its latest attempt.

    python tools/readme_row.py DATASET            # print the row

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
c=yaml.safe_load(open('claims/crcns-ear-1/10.1085-jgp.201912447.yaml'))
print({k:v for k,v in c.items() if k!='claims'})
a=yaml.safe_load(open('attempts/crcns-ear-1-farrell-2020-01.yaml'))
oc={o['claim']:o['outcome'] for o in a['outcomes']}
for x in c['claims']:
    print(x['id'], x.get('data','dataset'), x.get('kind'), oc.get(x['id']))
E
grep -n -i "ear" targets/dandisets.json | head; python -c "
import json;d=json.load(open('targets/dandisets.json'));print(type(d), list(d)[:5] if isinstance(d,dict) else d[0])"
```

```
{'schema_version': 2, 'dataset': {'archive': 'crcns', 'id': 'ear-1', 'doi': '10.6080/K0571975'}, 'paper': 'doi:10.1085/jgp.201912447', 'checks': [{'date': datetime.date(2026, 11, 6), 'kind': 'agent', 'model': 'claude-opus-5-5', 'ready': True, 'changes': ["Opening comment, Eq. 7. The signs were reversed. The Theoretical model says the negative sign gives the activation and the positive sign the deactivation, and only that assignment gives Table 3's 2.68 (forward) and 0.125 (reverse) kB T from its inputs.", 'Opening comment, region readings. The cell-count argument for reading (r-a) was circular. Restated it with the Fig. 1 count (86 cells with 144 mM chloride, at most 85 of known turn) against the 84 cells in Table 1.', 'nlw-capacitance. Marked the form of Eq. 8c (CNLW = CSB + root) as rebuilt from prose. The criterion fixed the cells as 144 mM chloride, which the paper does not say, so this is now named open with two readings.', 'fig1-charge-not-linear. Added the scale on which the adjusted R2 is taken (QTm^2 against CLW^2, or QTm against CLW) as an open reading.', 'alpha-gradient-pigmented. The criterion said these values times four are Table 1 rows (b) and (c). That holds for (b) only, since the albino values times four are 31.0 and 30.4 against 31.3 and 30.5. Corrected and noted.', 'table1-xe991-no-effect-alpha. Added reading (x-c), a one-way ANOVA on XE991, because the footnote does not give the model of its effect test.', 'fig2b-v05-vs-clw. Marked the p < 0.05 slope test as a choice made here, because the paper reports no slope test.', 'xe991-voltage-clamp. Marked the comparison of medians for "twofold improvement" as a choice made here, with the means as a variant.', "table2-xe991-v05-shift. Tolerance widened from 0.002 to 0.010 V, with the reason in the criterion. Table 2's own means give shifts of 0.019 to 0.029 V, so the 10% default would have failed the paper's own numbers.", 'fig3a-eq3a-fit. The criterion made the unconstrained fit weighted. The legend st
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
t=d['targets']
it = t if isinstance(t,list) else list(t.values())
for x in it:
    s=json.dumps(x)
    if 'ear-1' in s or 'K0571975' in s or 'jgp.201912447' in s: print(json.dumps(x,indent=1))
print(type(t), len(t))
E
```

```
<class 'list'> 295
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
t=d['targets']
print(json.dumps(t[0],indent=1)[:1500])
print([x.get('id') or x.get('dandiset') for x in t if 'crcns' in json.dumps(x).lower()][:50])
E
grep -rn "ear-1" targets/ | head
```

```
{
 "dandiset": "000003",
 "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
 "published_version": "0.260218.2052",
 "asset_count": 101,
 "size_gb": 2448.74,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "House mouse",
  "Mus musculus - House mouse"
 ],
 "approaches": [
  "electrophysiological approach",
  "behavioral approach"
 ],
 "papers": [
  {
   "doi": "10.1016/j.neuron.2016.12.011",
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 695,740p targets/crcns.json
```

```
"resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "id": "ear-1",
   "name": "Data collection curated with an application ontology describes the methods and  results upon performing an ex-vivo voltage-clamp assay on outer hair cells of the mammalian cochlea.",
   "url": "http://crcns.org/data-sets/ear/ear-1",
   "doi": "10.6080/K0571975",
   "published_version": null,
   "asset_count": 9,
   "size_gb": 0.2,
   "data_standards": [
    "compressed archives"
   ],
   "species": [
    "Guinea pig"
   ],
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/crcns-ear-1; wc -c *-report.md; cat author-report.md
```

```
2052 answer-report.md
 4270 author-answers-report.md
 4989 author-report.md
 3975 author-revise-1-report.md
 3612 author-revise-2-report.md
 3749 claims-check-report.md
 3688 claims-report.md
13533 verifier-1-report.md
 7248 verifier-2-report.md
47116 total
I've done steps 1 to 5 of the Author section on CRCNS ear-1 and built the handover (step 6). The entry is `entries/crcns-ear-1-farrell-2020/`, the record `attempts/crcns-ear-1-farrell-2020-01.yaml`, and one question for a reader is in `questions/crcns-ear-1.yaml`. `entry.py all` passes from a clean environment (0 errors, notebook 32 s). Nothing is committed.

**(1) Outcomes** (48 claims: 19 reproduced, 9 partially reproduced, 13 not reproduced, 7 blocked)

| Outcome | Claims |
|---|---|
| Reproduced | cohort, figs1-example-cell, clw-by-turn, fig1-two-state-bounds, alpha-pigmented-vs-albino, alpha-gradient-pigmented, table1-albino-no-gradient, figs2-alphab-vs-clw*, v05-by-turn, table2-xe991-v05-shift, table2-pigmented-xe991, table2-pigmented-no-xe991, table2-albino, v05-not-correlated-voltage-drop*, tables3-by-region, figs5-specific-capacitance*, fig4e-sensor-charge, table3-pathway-energies, recording-time* |
| Partially reproduced | fig1-charge-not-linear, table1-pigmented-xe991, table1-pigmented-no-xe991, table1-xe991-no-effect-alpha, fig2b-v05-vs-clw, xe991-voltage-clamp, capacitance-asymmetry*, fig4a-vh-rises-vd-constant, two-hyperpolarized-states* |
| Not reproduced | nlw-capacitance, fig2b-no-phenotype-difference, v05-gradient-length, fig3a-eq3a-fit, fig3a-xe991-fit, fig3a-high-density-deviation*, figs4-fine-bins, fig3b-negative-clw-fit*, mean-slope-half*, fig4d-cleq-two-limits, fig4c-sensor-area, alternative-limit, low-chloride-similar |
| Blocked, data missing | splice-isoform-x1, molecular-model |
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/crcns-ear-1; for f in claims-report claims-check-report answer-report author-answers-report; do echo "=== $f"; cat $f.md; done
```

```
=== claims-report
I wrote `claims/crcns-ear-1/10.1085-jgp.201912447.yaml`, and the quote checker passes it with 0 problems.

**Text read:** the version of record (PMC7335013, Europe PMC XML flattened to text). It has the Introduction, the model, the Methods, Results, Discussion, the legends of Figs. 1 to 5 and S1 to S7, and Tables 1 to 3. There is no PDF. The paper links no code. The MATLAB scripts and the GitHub repository (gaviganet/OHC_curation) are named only by the data set's own description, so I did not read them.

**Missing from the text:**
- **All displayed equations (Eqs. 1 to 9).** The flattening dropped them. I rebuilt Eqs. 2c, 3a/3b, 5, 6a/6b, 7 and 8d from the surrounding prose, and checked each against the paper's own numbers; for example, Eq. 6a and Eq. 7 give back every energy in Table 3. Each is marked in the file as a reconstruction. Eqs. 8b and 8c, for the non-lateral-wall capacitance, can only be partly rebuilt.
- **The contents of Tables S1 to S4.** Only their captions are in the text. The claims `tables3-by-region` and `recording-time` cannot be compared to numbers, and Table S4's charges are absent.

The main findings rest on Figs. 1 to 4 and Tables 1 to 3, so I wrote the claims. Supplying the PDF and the supplementary tables would close both gaps.

**Counts:**

| | Number |
|---|---|
| Claims | 48 (1 `link` claim for the cohort, 47 findings) |
| With a quote | 42 |
| Marked `inferred` | 6 (rows of Tables 1 and 2 that no sentence states) |
| With statistics | 9 claims, 9 entries |
| With a criterion | all 48 |
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/crcns-ear-1; for f in verifier-1-report author-revise-1-report verifier-2-report author-revise-2-report; do echo "=== $f"; cat $f.md; done
```

```
=== verifier-1-report
**Verifier report, round 1: Farrell et al. 2020 (doi:10.1085/jgp.201912447) on CRCNS ear-1**

The claims file has 48 claims. The notebook tests 41 and treats 7 as blocked. Every outcome that uses CLW, dVmin or C_Leq rests on the notebook's reading L-b. Under L-b, the stereocilia capacitance CSB comes from the Corbitt et al. (2012) rule, which the notebook states as an assumption. That rule passes the Fig. S1 admissibility test: CLW 18.30 pF against 18.56 ± 1.856 pF.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| cohort | reproduced | All 8 group counts match. Totals 89, 42 albino and 47 pigmented. Also 3 cells at 10 mM chloride, 81 with Rs < 10 MOhm, recording times 47–182 min (cell 5). |
| figs1-example-cell | reproduced | All 6 recomputed values are within tolerance, and so are the stored ones (cell 7). |
| nlw-capacitance | reproduced | Root 5.104 pF is within 4.82 ± 0.482 (reading n-ii). Pigmented/albino and adult/juvenile 95% intervals overlap (cell 9). This holds only with the Corbitt CSB assumption: with CSB = 0 (n-c) the root is 5.44 pF and fails. |
| clw-by-turn | reproduced | Turn 1: 5.04 pF (SD 2.34). Turn 4: 17.79 pF (SD 2.74). Both means and both SDs within tolerance (cell 11). |
| fig1-charge-not-linear | reproduced | Fit through the origin, centred R2: 0.539, within 0.516 ± 0.052. CLW < 10 pF slope is 2.0× the other, with disjoint intervals (cell 13). Only 1 of 6 R2 readings passes. |
| fig1-two-state-bounds | not_reproduced | Reading b-a: 86% of cells in the band, below the 90% needed. Reading b-b: the CLW ≥ 10 pF median is 0.167 V against 0.129 ± 0.013 V (cell 55). |
| alpha-pigmented-vs-albino | reproduced | Means 9.00 and 7.81 V⁻¹, ANOVA p = 0.00008 (cell 15). |
| alpha-gradient-pigmented | reproduced | Region reading r-a: all four means within tolerance. Pigmented p = 0.00097; albino p = 0.586 (cell 17). |
| table1-pigmented-xe991 | partially_reproduced | Means and z within tolerance, p = 0.0027. But the coun
[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; grep -l "outside data\|with_inputs\|other papers" *.md | head; grep -h -o "[^.]*with_inputs[^.]*\.\|[^.]*use outside data[^.]*\." *.md | head -8; grep -h -o "^[A-Z][^.]*blocked[^.]*\." *.md | head -20
```

```
000008-scala-2021-01.md
000035-scala-2021-01.md
000138-churchland-2010-01.md
000226-severson-2017-01.md
000249-schiavo-2020-01.md
000294-buccino-2024-01.md
000402-microns-2025-01.md
000489-kim-2022-01.md
000541-yemini-2021-01.md
000552-huszar-2022-01.md
the claims file marks `with_inputs`, is counted apart and reproduced.
tested claims are `with_inputs`, and the dandiset is judged on two.
Outcome: four claims reproduced, two partially, four blocked.
J dataset and EMG, are blocked as `data_missing`.
Five claims reproduced, seven partially, one not reproduced and none blocked.
Twelve claims reproduced, two partially and eleven blocked on the dandiset.
Nine claims reproduced, seven partially, two not reproduced and 14 blocked.
Nine claims reproduced, eight partially, 14 not reproduced and ten blocked.
Five claims reproduced, 11 partially, six not reproduced and two blocked.
Ten claims reproduced, four partially, one not reproduced and 28 blocked.
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; grep -h -B1 -A3 "(+[0-9]\|six more\|use outside\|counted apart" *.md | head -40
```

```
Outcome, on the dandiset alone: three claims reproduced, one partially and
nine blocked. With outside data, counted apart: two reproduced, one
partially and one blocked. No outcome changed through either round. See
[`attempts/000035-scala-2021-01.yaml`](../../attempts/000035-scala-2021-01.yaml)
and [`transcripts/000035/`](../../transcripts/000035).
--
with the stimulus side following it. session_start_time is stated in UTC
(+00:00) but holds local clock times, as all seven labs, from London to
Berkeley, have median start hours between 11.0 and 14.4 h, so the start times
cannot confirm the time zones `fig3f-positive-control` takes from the code.
Other findings: in 807 files the wheel position data and its timestamps
--
the dataset; `fig4-task-similar`, which needs monkey C's data from elsewhere,
is counted apart and blocked as `other`, as those data are named only by a
preprint with no archive identifier to pin. It pins version 0.241017.1444, its
only published version; the draft holds the same two assets and differs only
in its title. The paper, Makin, O'Doherty, Cardoso and Sabes in the Journal of
--
the dataset; `fig8-oscillator-model`, a simulation with no recorded data that
the claims file marks `with_inputs`, is counted apart and reproduced. It pins
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -c 5000 claims/crcns-ear-1/10.1085-jgp.201912447.yaml; grep -n -i "guinea\|prestin\|outer hair" claims/crcns-ear-1/10.1085-jgp.201912447.yaml | head -20
```

```
# Claims for Farrell, Skidmore, Rajasekharan & Brownell (2020), J Gen Physiol 152(7), "A novel
# theoretical framework reveals more than one voltage-sensing pathway in the lateral membrane of
# outer hair cells", doi:10.1085/jgp.201912447, on CRCNS data set ear-1 (doi:10.6080/K0571975).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-06,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record (PMC7335013, open access), as supplied under paper/ (Europe PMC
# JATS XML flattened to text): Introduction, Theoretical model, the section on expressions for the
# experimental parameters, Materials and methods, Results, Discussion, the legends of Figures 1 to 5
# and S1 to S7, and Tables 1 to 3. No PDF was supplied.
# Missing from the text. (1) Every displayed equation (Eqs. 1 to 9) is lost in the flattening; only
# the prose around them is there. The forms used below were rebuilt from that prose and checked
# against the paper's own numbers, and each is marked as a reconstruction where a criterion uses it.
#   Eq. 2c, the charge density, dVmin_exp = QTm / CLW (prose; Fig. S1 legend gives QTm 3.02 pC and
#     CLW 18.56 pF, 0.163 V).
#   Eq. 3a, V0.5 = Vd - dVmin_exp / 2 (prose; slope -1/2, intercept Vd, "Vd was the only free
#     parameter"); with Eq. 3b, Vh = V0.5 - dVmin_exp / 2 and Vd = V0.5 + dVmin_exp / 2.
#   Eq. 5, z = n delta = alphaB kB T / e0 (Table 1, alphaB 37.3 and z 0.96 at 24 C).
#   Eq. 8d, alphaB = 4 alpha(V0.5) (Results, 9.32 and 8.08 V-1 against Table 1, 37.3 and 32.3 V-1).
#   Eq. 6a, lambda = q^2 / (2 C_Leq), and Eq. 6b, QTm^2 = (2 lambda / C_Leq) CLW^2 (gives 3.95 and
[... 58 more lines not kept]
```

**Agent**

I have everything I need. Writing the note now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/crcns-ear-1-farrell-2020-01.md",
 "content": "# crcns-ear-1, Farrell et al. 2020\n\nTwenty-two claims reproduced (13 on an assumption), seven partially (four on an\nassumption), 11 not reproduced (nine on an assumption) and one blocked, for\nmissing data; the six claims that need values from other papers or a protein\nmodel the paper does not deposit (`with_inputs`) are counted apart and blocked,\nfive as `other` and one for missing data, and the link claim `cohort`,\nreproduced, is counted apart too. The first verification round agreed with 45\nof the 48 outcomes as they stood and the second with all 48; nothing was\nproposed after the second, so there was no third round. CRCNS does not version\ndata sets, so the version is recorded as unversioned with the data set's DOI\n(10.6080/K0571975); the author pinned `ear-1/live/data_and_scripts.zip` by its\nMD5, the copy the file list names, and did not read the copy under `old/ver1`.\nThe paper, Farrell, Skidmore, Rajasekharan and Brownell, \"A novel theoretical\nframework reveals more than one voltage-sensing pathway in the lateral membrane\nof outer hair cells\" in the Journal of General Physiology (152(7)), records the\nvoltage-dependent capacitance of 89 outer hair cells from guinea pigs of a\npigmented and an albino colony by whole-cell voltage clamp, some with XE991 in\nthe bath, relates the prestin sensor's V0.5 to the charge density dVmin (QTm\nover the lateral wall capacitance CLW) and infers two configurational states of\nthe sensor and the energies of two pathways; the data set is one zip of 120\nmembers holding the 89 cells as MATLAB and HDF5 files, analysis scripts and an\nontology. The claims were written from the version of record (PMC7335013)\nflattened from Europe PMC XML, which lost every displayed equation (Eqs. 1 to 9,\nrebuilt from the prose and checked against the paper's numbers) and the\ncontents of Tables S1 to S4, and without code, as the paper links none; the\nclaims check made 19 corrections, among them the signs of the rebuilt Eq. 7 and\na tolerance widened from 0.002 to 0.010 V for `table2-xe991-v05-shift`. The\ncohort, Tables 1 to 3, the V0.5 and charge density fits of Figs. 1 to 4 and S4,\nthe capacitance asymmetry and the specific capacitance could be tested; the\nprestin sequencing, the protein model and the claims resting on rat, mouse,\nhearing-loss and temperature correction values from other papers could not.\nEvery outcome that uses CLW, dVmin or C_Leq rests on the stereocilia bundle\ncapacitance rule of Corbitt et al. (2012), listed under `inputs`, and several\non a dVmin limit (reading y-1) that leaves out bins and groups whose mean dVmin\nis not in (0, 0.4] V, taken from the Fig. S4 legend and the Discussion.\nReproduced are, among others, `nlw-capacitance` (root 5.104 pF, within 4.82 +/-\n0.482 pF; 5.44 pF with no bundle capacitance), `alpha-pigmented-vs-albino`\n(9.00 and 7.81 V-1, p = 0.00008), `table2-albino` (p = 0.0697, the paper's\nvalue), `fig3a-eq3a-fit` (Vd 0.0311 V and slope -0.4245, with bin edges from\nthe smallest CLW), `fig3a-xe991-fit` (Vd 0.0505 V, under the dVmin limit) and\n`table3-pathway-energies` (all six values within tolerance). Partial are, among\nothers, `table1-pigmented-xe991` (5 basal and 12 apical cells where the table\nhas 4 and 11), `table1-pigmented-no-xe991` (p = 0.0010, not < 0.0001),\n`fig2b-v05-vs-clw` (albino adjusted R2 0.175, outside 0.2 +/- 0.02),\n`figs4-fine-bins` (the XE991 R2 0.605 against 0.737 +/- 0.074),\n`low-chloride-similar` (two of three cells) and `two-hyperpolarized-states`,\nkept partial as a judgement since under y-1 no tier of its criterion fits. Not\nreproduced are, among others, `fig1-two-state-bounds` (86.0% of cells in the\nband, short of 90%), `fig2b-no-phenotype-difference` (the slopes differ, p =\n0.039), `v05-gradient-length` (0.46 um/mV against 0.63 to 0.77),\n`xe991-voltage-clamp` (a ratio of medians of 1.52, not twofold),\n`capacitance-asymmetry` (basal share of CLW 36.1% against 21 +/- 2.1%),\n`fig4a-vh-rises-vd-constant` (Vh rises 2.67-fold, below 2.7), `mean-slope-half`\n(-0.407 against -0.48 +/- 0.048, though -0.432 under the bin edges that\nreproduce Fig. 3a) and `fig4d-cleq-two-limits` (lower limit 0.6496 aF, outside\n0.584 +/- 0.065 by 0.0006 aF). The author's first run had 19 reproduced, 9\npartially, 13 not reproduced and 7 blocked, taking CLW as CL - 4.82 pF as the\nclaims file did. The author asked a reader whether CLW should take a per-cell\nnon-lateral-wall capacitance, as the Fig. S1 legend implies 5.89 pF; the reader\namended the shared method to CNLW = CSB + root per cell, and in the\nauthor-answers run, with the Corbitt rule on the stored cell area, the counts\nbecame 22, 10, 9 and 7, with `nlw-capacitance`, `fig1-charge-not-linear`,\n`fig3a-eq3a-fit` and `fig3a-high-density-deviation` reproduced and\n`fig1-two-state-bounds` not reproduced. Round 1 disagreed on\n`xe991-voltage-clamp`, `capacitance-asymmetry` and `fig4a-vh-rises-vd-constant`\n(not reproduced, as none of their criteria has a partial tier), and found that\none XE991 bin of two cells (file 57, CLW 0.475 pF) decided several outcomes,\nthat the bins of Fig. 3b were not shown, that an end-to-end length gradient was\nnot run and that the CLn readings were chosen to match the paper's numbers; in\nreply the dVmin limit was adopted for every fit and grouping, which made\n`fig3a-xe991-fit` and `table3-pathway-energies` reproduced,\n`low-chloride-similar` partial and `fig4d-cleq-two-limits` not reproduced, the\nthree disputed claims became not reproduced, the positive Fig. 3b slope was\ntraced to one cell (file 18, dC -5.0 pF), and the end-to-end gradient was run\n(0.95 to 1.43 um/mV, also outside) and asked of a reader in\n`questions/crcns-ear-1.yaml` after the answer run, so it is unanswered. Round 2\nagreed with all 48 outcomes, noted that the dVmin limit is not in the claims\nfile and decides four outcomes while its cell-level form would fail\n`fig3a-eq3a-fit` (Vd 0.0299 V), and found text the outputs did not support,\namong them \"17 against 15 or 16 pigmented XE991 cells\" and an upper C_Leq limit\nsaid to include one single-cell group where two of its three groups are single\ncells; in reply the text was corrected and the cells behind each limit were\nprinted, and no outcome changed. The author's run went from 11:49 to 12:19 UTC;\nthe notebook ran in 32 s at first, 38 s after the author-answers run and 44 s\nafter round 1. Two steps failed during the author's run and were fixed: ramp\ndetection broke on file 52, which holds at +0.06 V, and the first handover\nfailed because a test venv was still active. The untracked dotfiles in the\nrepository root and an empty `.claude/` folder in the entry were left alone.\n\nThe data set stores CL, QTm, V0.5 and alphaB per cell but not the lateral wall\ncapacitance CLW, the stereocilia bundle capacitance CSB or the non-lateral-wall\ncapacitance CNLW of Eq. 8a, so the paper's CLW and charge density cannot be\ntaken from it; with the Corbitt et al. (2012) rule, CLW reproduces the Fig. S1\nlegend (18.30 against 18.56 pF), but the XE991 fits, the band of Fig. 1 and the\nlower C_Leq limit turn on the CLW of the smallest cells, which the rule makes\nas small as 0.48 pF. The linear capacitance at negative voltages, CLn, and the\nrule for when it could be estimated are not stored, nor are the linear-region\nindices the MATLAB files keep as indposit_ramplin. The cells behind the paper's\ntables are not marked: the data set gives 27 pigmented cells without XE991 with\n144 mM chloride (paper 28), 17 pigmented XE991 cells split 5 and 12 by region\n(Table 1 row a, 4 and 11), 69 Fig. 2 cells (legend 70) and 46 cells for Fig. 3b\nby the rule used (legend 44). In every HDF5 file with DC steps (19 cells),\n`I_mean` has shape (N, 2) but stores its values in MATLAB column order, so read\nas given the means and SDs are interleaved. File sensory_cell_#52.h5 holds the\nmembrane at +0.06 V before and after the ramp where the stimulus description\nsays -0.06 V. `cell_surface_area` follows 2 pi r l for 34 cells and 2 pi r LW +\n2 pi r^2 for 50 without saying so, and the cell length is stored for 35 cells\nand the lateral wall length for 83, with nothing saying which the paper used.\nThe MATLAB field `toxins` labels 15 of the 20 XE991 cells `XE991` and 5 `yes`,\nthe HDF5 files store 60 uM for all 20 while the Methods give 30 to 60 uM, and\nthe HDF5 maturity `juvenile` (10 males) was read as prepubertal from the MATLAB\nfiles. The `original cell number` is not unique, 13 numbers being used by two\ncells each, while the paper names cells by it (Fig. S1, cell 99). The largest\nconductance at V0.5 among XE991 cells is 8.5 nS from the DC steps and 7.0 nS\nfrom the admittance, about 25 times the 335 pS the paper reports. Questions are\nput to the paper's authors: how CLn was taken and what counted as reaching the\nhyperpolarized plateau, so that 62 cells qualify; whether the per-cell CSB of\nEq. 8 followed the Corbitt et al. (2012) rule and which area it used; and\nwhether bins or groups with a large charge density were left out of the Fig. 3a\nfits and the Fig. 4 groups, as the Fig. S4 fit leaves out dVmin of 0.4 V and\nabove.\n\nThe author's points on the protocol: no `blocked_by` fits values that are\npublic in published papers but not supplied to the run, so `other` was used\nwith the reason given; several criteria have no partial tier and\n`two-hyperpolarized-states` fits none of its tiers, so the closest tier was\npicked and said so in the notes; the same-clock check assumes trial tables, so\nfor these voltage ramps the capacitance peak was checked against the stored\nV0.5 (79 of 89 within one ramp step); `docs/archives.md` does not say which of\ntwo copies of a CRCNS data set to pin, so the live copy was chosen with the\nreason in the header; and the protocol does not say whether analysis scripts\ndeposited inside a data set count as the paper's code, so they were cited only\nto explain how the stored values were computed and no method was taken from\nthem.\n"
}
```

```
File created successfully at: docs/pilot-notes/crcns-ear-1-farrell-2020-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -n -c "—\|rather\|\*\*" docs/pilot-notes/crcns-ear-1-farrell-2020-01.md; git status --short
```

```
0
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
?? docs/pilot-notes/crcns-ear-1-farrell-2020-01.md
?? scripts
```

**Agent**

I wrote `docs/pilot-notes/crcns-ear-1-farrell-2020-01.md` and changed no other file. The untracked dotfiles and `scripts/` in the repository root were already there, and I left them alone. Nothing is committed.

Neither target file says CatalystNeuro converted ear-1. `targets/dandisets.json` has no entry for this dataset, and its entry in `targets/crcns.json` has an empty `catalystneuro` field. So the second paragraph does not open with the CatalystNeuro sentence.

# crcns-ear-1, Farrell et al. 2020

Twenty-two claims reproduced (13 on an assumption), seven partially (four on an assumption), 11 not reproduced (nine on an assumption) and one blocked, for missing data; the six claims that need values from other papers or a protein model the paper does not deposit (`with_inputs`) are counted apart and blocked, five as `other` and one for missing data, and the link claim `cohort`, reproduced, is counted apart too. The first verification round agreed with 45 of the 48 outcomes as they stood and the second with all 48; nothing was proposed after the second, so there was no third round. CRCNS does not version data sets, so the version is recorded as unversioned with the data set's DOI (10.6080/K0571975); the author pinned `ear-1/live/data_and_scripts.zip` by its MD5, the copy the file list names, and did not read the copy under `old/ver1`. The paper, Farrell, Skidmore, Rajasekharan and Brownell, "A novel theoretical framework reveals more than one voltage-sensing pathway in the lateral membrane of outer hair cells" in the Journal of General Physiology (152(7)), records the voltage-dependent capacitance of 89 outer hair cells from guinea pigs of a pigmented and an albino colony by whole-cell voltage clamp, some with XE991 in the bath, relates the prestin sensor's V0.5 to the charge density dVmin (QTm over the lateral wall capacitance CLW) and infers two configurational states of the sensor and the energies of two pathways; the data set is one zip of 120 members holding the 89 cells as MATLAB and HDF5 files, analysis scripts and an ontology. The claims were written from the version of record (PMC7335013) flattened from Europe PMC XML, which lost every displayed equation (Eqs. 1 to 9, rebuilt from the prose and checked against the paper's numbers) and the contents of Tables S1 to S4, and without code, as the paper links none; the claims check made 19 corrections, among them the signs of the rebuilt Eq. 7 and a tolerance widened from 0.002 to 0.010 V for `table2-xe991-v05-shift`. The cohort, Tables 1 to 3, the V0.5 and charge density fits of Figs. 1 to 4 and S4, the capacitance asymmetry and the specific capacitance could be tested; the prestin sequencing, the protein model and the claims resting on rat, mouse, hearing-loss and temperature correction values from other papers could not. Every outcome that uses CLW, dVmin or C_Leq rests on the stereocilia bundle capacitance rule of Corbitt et al. (2012), listed under `inputs`, and several on a dVmin limit (reading y-1) that leaves out bins and groups whose mean dVmin is not in (0, 0.4] V, taken from the Fig. S4 legend and the Discussion. Reproduced are, among others, `nlw-capacitance` (root 5.104 pF, within 4.82 +/- 0.482 pF; 5.44 pF with no bundle capacitance), `alpha-pigmented-vs-albino` (9.00 and 7.81 V-1, p = 0.00008), `table2-albino` (p = 0.0697, the paper's value), `fig3a-eq3a-fit` (Vd 0.0311 V and slope -0.4245, with bin edges from the smallest CLW), `fig3a-xe991-fit` (Vd 0.0505 V, under the dVmin limit) and `table3-pathway-energies` (all six values within tolerance). Partial are, among others, `table1-pigmented-xe991` (5 basal and 12 apical cells where the table has 4 and 11), `table1-pigmented-no-xe991` (p = 0.0010, not < 0.0001), `fig2b-v05-vs-clw` (albino adjusted R2 0.175, outside 0.2 +/- 0.02), `figs4-fine-bins` (the XE991 R2 0.605 against 0.737 +/- 0.074), `low-chloride-similar` (two of three cells) and `two-hyperpolarized-states`, kept partial as a judgement since under y-1 no tier of its criterion fits. Not reproduced are, among others, `fig1-two-state-bounds` (86.0% of cells in the band, short of 90%), `fig2b-no-phenotype-difference` (the slopes differ, p = 0.039), `v05-gradient-length` (0.46 um/mV against 0.63 to 0.77), `xe991-voltage-clamp` (a ratio of medians of 1.52, not twofold), `capacitance-asymmetry` (basal share of CLW 36.1% against 21 +/- 2.1%), `fig4a-vh-rises-vd-constant` (Vh rises 2.67-fold, below 2.7), `mean-slope-half` (-0.407 against -0.48 +/- 0.048, though -0.432 under the bin edges that reproduce Fig. 3a) and `fig4d-cleq-two-limits` (lower limit 0.6496 aF, outside 0.584 +/- 0.065 by 0.0006 aF). The author's first run had 19 reproduced, 9 partially, 13 not reproduced and 7 blocked, taking CLW as CL - 4.82 pF as the claims file did. The author asked a reader whether CLW should take a per-cell non-lateral-wall capacitance, as the Fig. S1 legend implies 5.89 pF; the reader amended the shared method to CNLW = CSB + root per cell, and in the author-answers run, with the Corbitt rule on the stored cell area, the counts became 22, 10, 9 and 7, with `nlw-capacitance`, `fig1-charge-not-linear`, `fig3a-eq3a-fit` and `fig3a-high-density-deviation` reproduced and `fig1-two-state-bounds` not reproduced. Round 1 disagreed on `xe991-voltage-clamp`, `capacitance-asymmetry` and `fig4a-vh-rises-vd-constant` (not reproduced, as none of their criteria has a partial tier), and found that one XE991 bin of two cells (file 57, CLW 0.475 pF) decided several outcomes, that the bins of Fig. 3b were not shown, that an end-to-end length gradient was not run and that the CLn readings were chosen to match the paper's numbers; in reply the dVmin limit was adopted for every fit and grouping, which made `fig3a-xe991-fit` and `table3-pathway-energies` reproduced, `low-chloride-similar` partial and `fig4d-cleq-two-limits` not reproduced, the three disputed claims became not reproduced, the positive Fig. 3b slope was traced to one cell (file 18, dC -5.0 pF), and the end-to-end gradient was run (0.95 to 1.43 um/mV, also outside) and asked of a reader in `questions/crcns-ear-1.yaml` after the answer run, so it is unanswered. Round 2 agreed with all 48 outcomes, noted that the dVmin limit is not in the claims file and decides four outcomes while its cell-level form would fail `fig3a-eq3a-fit` (Vd 0.0299 V), and found text the outputs did not support, among them "17 against 15 or 16 pigmented XE991 cells" and an upper C_Leq limit said to include one single-cell group where two of its three groups are single cells; in reply the text was corrected and the cells behind each limit were printed, and no outcome changed. The author's run went from 11:49 to 12:19 UTC; the notebook ran in 32 s at first, 38 s after the author-answers run and 44 s after round 1. Two steps failed during the author's run and were fixed: ramp detection broke on file 52, which holds at +0.06 V, and the first handover failed because a test venv was still active. The untracked dotfiles in the repository root and an empty `.claude/` folder in the entry were left alone.

The data set stores CL, QTm, V0.5 and alphaB per cell but not the lateral wall capacitance CLW, the stereocilia bundle capacitance CSB or the non-lateral-wall capacitance CNLW of Eq. 8a, so the paper's CLW and charge density cannot be taken from it; with the Corbitt et al. (2012) rule, CLW reproduces the Fig. S1 legend (18.30 against 18.56 pF), but the XE991 fits, the band of Fig. 1 and the lower C_Leq limit turn on the CLW of the smallest cells, which the rule makes as small as 0.48 pF. The linear capacitance at negative voltages, CLn, and the rule for when it could be estimated are not stored, nor are the linear-region indices the MATLAB files keep as indposit_ramplin. The cells behind the paper's tables are not marked: the data set gives 27 pigmented cells without XE991 with 144 mM chloride (paper 28), 17 pigmented XE991 cells split 5 and 12 by region (Table 1 row a, 4 and 11), 69 Fig. 2 cells (legend 70) and 46 cells for Fig. 3b by the rule used (legend 44). In every HDF5 file with DC steps (19 cells), `I_mean` has shape (N, 2) but stores its values in MATLAB column order, so read as given the means and SDs are interleaved. File sensory_cell_#52.h5 holds the membrane at +0.06 V before and after the ramp where the stimulus description says -0.06 V. `cell_surface_area` follows 2 pi r l for 34 cells and 2 pi r LW + 2 pi r^2 for 50 without saying so, and the cell length is stored for 35 cells and the lateral wall length for 83, with nothing saying which the paper used. The MATLAB field `toxins` labels 15 of the 20 XE991 cells `XE991` and 5 `yes`, the HDF5 files store 60 uM for all 20 while the Methods give 30 to 60 uM, and the HDF5 maturity `juvenile` (10 males) was read as prepubertal from the MATLAB files. The `original cell number` is not unique, 13 numbers being used by two cells each, while the paper names cells by it (Fig. S1, cell 99). The largest conductance at V0.5 among XE991 cells is 8.5 nS from the DC steps and 7.0 nS from the admittance, about 25 times the 335 pS the paper reports. Questions are put to the paper's authors: how CLn was taken and what counted as reaching the hyperpolarized plateau, so that 62 cells qualify; whether the per-cell CSB of Eq. 8 followed the Corbitt et al. (2012) rule and which area it used; and whether bins or groups with a large charge density were left out of the Fig. 3a fits and the Fig. 4 groups, as the Fig. S4 fit leaves out dVmin of 0.4 V and above.

The author's points on the protocol: no `blocked_by` fits values that are public in published papers but not supplied to the run, so `other` was used with the reason given; several criteria have no partial tier and `two-hyperpolarized-states` fits none of its tiers, so the closest tier was picked and said so in the notes; the same-clock check assumes trial tables, so for these voltage ramps the capacitance peak was checked against the stored V0.5 (79 of 89 within one ramp step); `docs/archives.md` does not say which of two copies of a CRCNS data set to pin, so the live copy was chosen with the reason in the header; and the protocol does not say whether analysis scripts deposited inside a data set count as the paper's code, so they were cited only to explain how the stored values were computed and no method was taken from them.

## End of run

21 turns, 3 minutes, $1.31 at API prices, result: success.
