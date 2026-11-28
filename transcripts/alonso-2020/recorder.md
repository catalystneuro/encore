# alonso-2020 · recorder · run 46153360540

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/alonso-2020/; python tools/readme_row.py alonso-2020; grep -n -B2 -A12 'm31b1h7' targets/dandisets.json
```

```
docs/pilot-notes/allen-2026-01.md
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/amjad-2025-02.md
docs/pilot-notes/andreassen-2022-01.md
docs/pilot-notes/andrews-2024-01.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author-revise-3-report.md
author-revise-3.md
author.md
claims-check-report.md
claims-check.md
claims-report.md
claims.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -B3 -A12 'alonso\|m31b1h7' targets/dandisets.json | head -60; head -5 README.md | head -3; grep -n '^|' README.md | head -3; cd docs/pilot-notes; for f in allen-2026-01 amjad-2025-01 amjad-2025-02 andreassen-2022-01 andrews-2024-01; do echo "=== $f"; cat $f.md; done
```

```
<persisted-output>
Output too large (30.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c94c7f98-fdf2-4850-838c-31408c695390/tool-results/bloanxbu4.txt

Preview (first 2KB):
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>. The protocol the checks follow, and the `encore` command that runs the same check on your own data, are in [encore-protocol](https://github.com/encorescience/encore-protocol). It is developed by [CatalystNeuro](https://www.catalystneuro.com).
=== allen-2026-01
# allen-2026, Allen et al. 2026

Fifteen claims reproduced on the dataset, one partially, one not reproduced
and four blocked, all four for missing data; the ten transcriptomic claims,
whose reads and assembly are in NCBI SRA and TSA (`data: elsewhere`), are
counted apart, with seven reproduced, two partially and one not reproduced.
One outcome, `fig4a-pca`, rests on an assumption. The first verification round
agreed with 28 of the 31 outcomes and gave `fig2g-attack-willingness` as
reproduced where the record had not reproduced, and
`sfig3-prey-velocity-unchanged` and `rnaseq-assembly` as partially reproduced
where it had reproduced; the author took all three. The second round agreed
with all 31, and nothing was proposed after it, so there was no third round. It
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c94c7f98-fdf2-4850-838c-31408c695390/tool-results/bloanxbu4.txt"
}
```

```
1	# Encore Science: the registry
2	
3	Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>. The protocol the checks follow, and the `encore` command that runs the same check on your own data, are in [encore-protocol](https://github.com/encorescience/encore-protocol). It is developed by [CatalystNeuro](https://www.catalystneuro.com).
4	=== allen-2026-01
5	# allen-2026, Allen et al. 2026
6	
7	Fifteen claims reproduced on the dataset, one partially, one not reproduced
8	and four blocked, all four for missing data; the ten transcriptomic claims,
9	whose reads and assembly are in NCBI SRA and TSA (`data: elsewhere`), are
10	counted apart, with seven reproduced, two partially and one not reproduced.
11	One outcome, `fig4a-pca`, rests on an assumption. The first verification round
12	agreed with 28 of the 31 outcomes and gave `fig2g-attack-willingness` as
13	reproduced where the record had not reproduced, and
14	`sfig3-prey-velocity-unchanged` and `rnaseq-assembly` as partially reproduced
15	where it had reproduced; the author took all three. The second round agreed
16	with all 31, and nothing was proposed after it, so there was no third round. It
17	pins version 439366, the only public version. The paper, Allen, Yan, Kuan et
18	al., "Neurometabolic rewiring in squid (Sepioteuthis lessoniana) optic lobes
19	drives behavioral plasticity and visual integration under environmental
20	acidification" (Communications Biology 9:229), rears bigfin reef squid at pH
[... 412 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c . targets/dandisets.json; grep -n -i 'dryad' targets/dandisets.json | head; cat attempts/alonso-2020-01.yaml
```

```
<persisted-output>
Output too large (57.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c94c7f98-fdf2-4850-838c-31408c695390/tool-results/bsgp6aac0.txt

Preview (first 2KB):
8541
schema_version: 3
id: alonso-2020-01
datasets:
- archive: dryad
  id: m31b1h7
  version: '94811'
  doi: 10.5061/dryad.m31b1h7
  relation: primary
paper: doi:10.7554/elife.55470
date: 2026-11-27
entry: alonso-2020
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
[... 31 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c94c7f98-fdf2-4850-838c-31408c695390/tool-results/bsgp6aac0.txt"
}
```

```
1	8541
2	schema_version: 3
3	id: alonso-2020-01
4	datasets:
5	- archive: dryad
6	  id: m31b1h7
7	  version: '94811'
8	  doi: 10.5061/dryad.m31b1h7
9	  relation: primary
10	paper: doi:10.7554/elife.55470
11	date: 2026-11-27
12	entry: alonso-2020
13	provenance:
14	  kind: agent
15	  accountable:
16	    name: CatalystNeuro
17	  agent:
18	    harness: Claude Code
19	    model: claude-opus-5-5
20	    protocol: pilot-19
[... 842 more lines not kept]
```

**Agent**

Now the claims file, the readme_row tool, and whether the dataset has a targets entry.

**Agent calls Bash**

```bash
cat tools/readme_row.py | head -80; grep -n -i 'alonso\|m31b1h7\|10.7554/elife.55470' targets/dandisets.json; python -c "
import json;d=json.load(open('targets/dandisets.json'));print(type(d), len(d)); x=d if isinstance(d,list) else list(d.values()); print(json.dumps(x[0],indent=1)[:800])"
```

```
"""The README's table row for a paper, from its latest attempt.

    python tools/readme_row.py PAPER              # print the row (a paper key, or a dataset listed for one)

Counts are of the paper's findings on the dandiset, including those that name its codes from
elsewhere (`with_labels`); findings that also use outside data (`with_inputs`) are shown in brackets;
findings on data in other archives (`elsewhere`) and the registry's link checks (`kind: link`) are
left out, as the README says. A deprecated attempt's row has no counts.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'));print(list(d.keys())); [print(k, type(v), len(v) if hasattr(v,'__len__') else v) for k,v in d.items()]"; grep -n -i 'dryad' targets/*.json | head; cat claims/alonso-2020.yaml
```

```
<persisted-output>
Output too large (43.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c94c7f98-fdf2-4850-838c-31408c695390/tool-results/bq6751f3q.txt

Preview (first 2KB):
['schema_version', 'generated', 'source', 'counts', 'targets']
schema_version <class 'int'> 1
generated <class 'str'> 25
source <class 'str'> 32
counts <class 'dict'> 5
targets <class 'list'> 302
targets/dryad.json:3: "archive": "dryad",
targets/dryad.json:5: "source": "https://datadryad.org/api/v2, chosen by hand (tools/build_dryad_targets.py)",
targets/dryad.json:14:   "url": "https://datadryad.org/dataset/doi:10.5061/dryad.bvq83bkk9",
targets/dryad.json:15:   "doi": "10.5061/dryad.bvq83bkk9",
targets/dryad.json:67:   "url": "https://datadryad.org/dataset/doi:10.5061/dryad.tdz08kq5d",
targets/dryad.json:68:   "doi": "10.5061/dryad.tdz08kq5d",
targets/dryad.json:122:   "url": "https://datadryad.org/dataset/doi:10.5061/dryad.4j0zpc8hz",
targets/dryad.json:123:   "doi": "10.5061/dryad.4j0zpc8hz",
targets/dryad.json:136:     "path": "Dryad_Data_PlantPhy_MargauxDidionGency.xlsx",
targets/dryad.json:189:   "url": "https://datadryad.org/dataset/doi:10.5061/dryad.1rn8pk129",
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json
for f in ['targets/dandisets.json','targets/dryad.json']:
  d=json.load(open(f))
  for t in d['targets']:
    if 'm31b1h7' in json.dumps(t): print(f); print(json.dumps({k:v for k,v in t.items() if k!='files'},indent=1)[:1500])
"
```

```
targets/dryad.json
{
 "id": "m31b1h7",
 "name": "Temperature compensation in a small rhythmic circuit",
 "url": "https://datadryad.org/dataset/doi:10.5061/dryad.m31b1h7",
 "doi": "10.5061/dryad.m31b1h7",
 "published_version": "94811",
 "version_number": 2,
 "published": "2020-12-07",
 "license": "https://spdx.org/licenses/CC0-1.0.html",
 "asset_count": 1,
 "size_gb": 0.0001,
 "data_standards": [
  "zip"
 ],
 "readme": false,
 "code": [],
 "species": [],
 "approaches": [],
 "keywords": [],
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/c94c7f98-fdf2-4850-838c-31408c695390/tool-results/bq6751f3q.txt"
}
```

```
1	['schema_version', 'generated', 'source', 'counts', 'targets']
2	schema_version <class 'int'> 1
3	generated <class 'str'> 25
4	source <class 'str'> 32
5	counts <class 'dict'> 5
6	targets <class 'list'> 302
7	targets/dryad.json:3: "archive": "dryad",
8	targets/dryad.json:5: "source": "https://datadryad.org/api/v2, chosen by hand (tools/build_dryad_targets.py)",
9	targets/dryad.json:14:   "url": "https://datadryad.org/dataset/doi:10.5061/dryad.bvq83bkk9",
10	targets/dryad.json:15:   "doi": "10.5061/dryad.bvq83bkk9",
11	targets/dryad.json:67:   "url": "https://datadryad.org/dataset/doi:10.5061/dryad.tdz08kq5d",
12	targets/dryad.json:68:   "doi": "10.5061/dryad.tdz08kq5d",
13	targets/dryad.json:122:   "url": "https://datadryad.org/dataset/doi:10.5061/dryad.4j0zpc8hz",
14	targets/dryad.json:123:   "doi": "10.5061/dryad.4j0zpc8hz",
15	targets/dryad.json:136:     "path": "Dryad_Data_PlantPhy_MargauxDidionGency.xlsx",
16	targets/dryad.json:189:   "url": "https://datadryad.org/dataset/doi:10.5061/dryad.1rn8pk129",
17	# Claims for Alonso & Marder (2020), "Temperature compensation in a small rhythmic circuit",
18	# eLife 9:e55470, tested on Dryad m31b1h7.
19	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
20	# 2026-11-25, protocol pilot-19 (docs/protocol.md, Reader).
[... 550 more lines not kept]
```

**Agent**

Record and claims read: 8 reproduced, 5 partial, 5 not, 4 blocked, with the link claim `deposit-models` (not reproduced) counted apart. Now the reports.

**Agent calls Bash**

```bash
cd transcripts/alonso-2020; wc -w *-report.md; cat author-report.md
```

```
1008 author-report.md
  739 author-revise-1-report.md
  516 author-revise-2-report.md
  267 author-revise-3-report.md
  629 claims-check-report.md
  789 claims-report.md
 2084 verifier-1-report.md
 1473 verifier-2-report.md
  367 verifier-3-report.md
 7872 total
I've finished steps 1 to 5 of the Author section and run the handover (step 6). `entry.py all` passed: 0 check errors and all three notebooks ran in about 58 min. The handover package is in `executed/alonso-2020/handover/`. Nothing is committed.

The dataset is code, not recordings: one zip with the authors' Java model, their Python scripts and one parameter file per model network. So every claim is tested by simulating the deposited models. I ported the Java to Python with numba (`pyloric.py`), and it matches the deposited Java to within 3e-9 mV.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| deposit-models | not reproduced (3 of 38 models within tolerance at 10 °C) |
| fig1c-frequency-q10-phase-constant | partially reproduced (Q10 1.93 to 1.98; LP duty cycle not constant) |
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/alonso-2020; for f in author-revise-1-report.md author-revise-2-report.md author-revise-3-report.md claims-check-report.md claims-report.md; do echo "=== $f"; cat $f; done
```

```
=== author-revise-1-report.md
I re-ran the entry once with `python tools/entry.py all entries/alonso-2020`, and all three notebooks passed: main 31 min, ramps 58 min, voltage 24 min. The checks pass with 0 errors. I wrote the conclusions after the run and copied the same markdown into the executed copies, so the entry's files are newer than the run stamp and the next run will execute fresh.

**Outcome changes**
- **fig2-lp-spike-amplitude-threshold:** now reproduced, marked assumed (was partially reproduced). Threshold reading (b) is now computed, as the upper edge of the densely occupied part of the voltage distribution below -20 mV. At the main setting (5%) it rises from -36.1 to -26.5 mV with Spearman 0.997, and the 2% and 10% settings agree. Amplitude still falls (Spearman -1.0). How to locate that point is my assumption, so I added it to the questions for the paper's authors.
- **fig8-up-down-ramps:** still blocked (too_large). I recorded the verifier's disagreement (it would give not_reproduced). The criterion passes if either ramp reading is within tolerance; the first gives 22 of 38, and the second is untested. The notebook now times the second reading on a subset at 113 min, while that notebook already takes 58 of its 60 min.
- All other outcomes are unchanged.

**Added or corrected, by verifier point**
1. **fig10a/fig10b:** both removal protocols now run. The main one, marked assumed, runs 20 s with every conductance intact first, as the Results do for Fig. 9 and as the deposit's removal script does; removal from t = 0 is the variant.
   - fig10a: 4 of 5 checks hold with the control period first, 3 of 5 from t = 0. Both are partial; measured changed from 3 to 4.
   - fig10b: the H part still fails under every reading and protocol (30 or 31 models, 33 needed).
2. **fig8 second reading:** not run; timed in the notebook (see above).
3. **fig2 threshold reading (b):** computed (see above).
4. **fig4:** added burst bounds at the -50 mV slow-wave crossings. The 
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/alonso-2020; for f in verifier-1-report.md verifier-2-report.md verifier-3-report.md; do echo "=== $f"; cat $f; done
```

```
=== verifier-1-report.md
**Verifier report, round 1: Alonso & Marder 2020 (doi:10.7554/elife.55470), Dryad m31b1h7 v94811**

The claims file has 23 claims. I checked the archive through Dryad's API: version 94811 is the only version and holds one zip of 99,026 bytes, whose MD5 matches the one the notebook checks. I ran the helper functions on synthetic spike trains and voltage traces. `bursts`, `burst_stats`, `classify_cell`, `triphasic`, `cycle_largest_isi`, `shares` and `spike_shapes` all behaved as documented. One gap: continuous irregular spiking with no gap over 200 ms is labelled "other".

**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| deposit-models | not_reproduced | Cell 12: 3 of 38 models are within tolerance, against the 30 needed. The 0.20 variant gives 0 of 38, and mean frequency is 1.25 Hz. Cells 7, 8 and 10: 4 of the 21 named models are absent, the deposit holds 38 models (not 36), and those 38 contain only 27 distinct conductance sets. |
| fig1c-frequency-q10-phase-constant | partially_reproduced | Cell 17: the frequency Q10 of 4X6W66 is 1.93, 1.98 or 1.94 under readings a, b and c, all within 2±0.2. Constancy fails under both readings: the LP duty-cycle range is 0.11 (above 0.1) and its change from 10 °C is 34% (above 20%). |
| fig1s1-three-models | not_reproduced | Cell 19: frequency rises in all three models, but none is constant under either reading. 71G6LA misses reading (i) only on PY offset (range 0.102). |
| all-models-compensated | partially_reproduced | Cell 21: 36 of 38 models are triphasic at all 16 temperatures (35 with the strict order variant). ED50XO fails at 19 and 21 °C; MAXTTP fails at 10 and 14 °C, and MAXTTP is a paper model (Fig. 2–S1), so not every paper model passes. "Multiple Q10 sets for every conductance set" is unsupported: only 9 of the 27 conductance sets carry more than one Q10 set. |
| intermediate-temperature-failures | blocked (data_missing) | Confirmed: the archive is one zip with 38 parameter files a
[... 148 more lines not kept]
```

**Agent**

I have everything I need. Writing the notes file now.

**Agent calls Bash**

```bash
cd  && mkdir -p summaries && python3 - <<'EOF'
import textwrap
head = "# alonso-2020, Alonso et al. 2020"
p1 = ("Eight claims reproduced on the dataset, five partially, five not reproduced "
"and four blocked, three for missing data and one, `fig8-up-down-ramps`, as too "
"large to run; the link claim `deposit-models`, that the deposit holds the "
"paper's models under the names the Methods give and that they give the control "
"rhythm they were fitted to, is counted apart and was not reproduced (3 of 38 "
"models within tolerance at 10 °C, against the criterion's 18). Eight outcomes "
"rest on an assumption, most on the -20 mV spike threshold and the test of "
"firing order, which the paper does not give, and "
"`fig2-lp-spike-amplitude-threshold` on a rule for where the spike region of "
"the voltage distribution begins. The first verification round agreed with 22 "
"of the 23 outcomes and gave `fig8-up-down-ramps` as not reproduced "
"(provisional) where the record had blocked; the author kept blocked, and the "
"second round withdrew the objection on the printed time estimate. The second "
"round agreed with 21 outcomes and held that `fig6s1-crash-mechanisms` should be "
"blocked for missing data, not not reproduced; the author proposed that change, "
"and a third round reviewed that one claim and agreed. It pins version 94811, "
"the only published version. The paper, Alonso and Marder, \"Temperature "
"compensation in a small rhythmic circuit\" (eLife 9:e55470), simulates a "
"three-cell model of the crustacean pyloric network (PD, LP and PY, each with "
"eight currents and temperature sensitivities set by Q10 values) and reports "
"that 36 models keep a triphasic rhythm from 10 to 25 °C, with burst frequency "
"rising at a Q10 near 2 while duty cycles and phases stay approximately "
"constant, that the currents behind this reorganize with temperature, with a "
"tradeoff between the A and KCa currents at burst termination, that the models "
"crash above 25 °C by different mechanisms, that temperature ramps show "
"hysteresis, and that removing a current has different effects at 10 and 25 °C. "
"The claims were written from the version of record without the legends of its "
"figure supplements, and no figure could be rendered. The dataset is code, not "
"recordings: one zip with the authors' Java model, their Python scripts, one "
"initial-condition file and 38 parameter sets, so every claim was tested by "
"simulating the deposited models, with a numba port of the Java that matches "
"its voltages to 3e-9 mV over 3 s at 18 °C and to 0.06 mV at 25 °C. The "
"frequency Q10 of the Figure 1 model is 1.927, but its LP duty cycle changes by "
"up to 34% from its 10 °C value, so `fig1c-frequency-q10-phase-constant` is "
"partial, and none of the three further models of Figure 1, figure supplement 1 "
"meets either reading of constancy. 36 of the 38 models are triphasic at all 16 "
"temperatures, one of the two that fail (MAXTTP) being a model the paper shows. "
"The largest ISI on a ramp, the spike amplitude and threshold of Figure 2, the "
"diverse peak voltages, the dominant currents (in 0.993 of cases), the A to KCa "
"tradeoff in FGFKQS, the 1.94 °C hysteresis of Figure 8A and the KCa removal of "
"Figure 9B reproduce; the duty-cycle claim of Figure 1, figure supplement 3 only "
"on the criterion's 16-temperature variant, with a test that shows little more "
"than that the distributions are not identical. No part of the Figure 4 "
"currentscape criterion holds under any of four readings; in Figure 6 the PD "
"cell of FGFKQS fires 1005 spikes at 30 °C where both models should be "
"quiescent; in Figure 8B H5AIZR returns to regular bursting at 17.08 °C and has "
"a longest ISI of 11.32 s, against 20 and 1; and removing H leaves 30 of 38 "
"models the same and quiescent at both temperatures, against the 33 asked. "
"Figure 3 is partial with a KCa peak ratio of 8.95 against 6, Figure 9A with "
"all three cells irregular at 25 °C, and Figure 10A with four of five grid "
"cells matching. The 2 in 40 failures cannot be tested, as the screened "
"solutions are not deposited; Figure 6, figure supplement 1 and Figure 7 lack "
"one and three of their models, and with them the outcome can be at best "
"partially reproduced; and the second ramp reading of `fig8-up-down-ramps`, "
"the ramp the paper cites, would take 117 min against the 60 min a notebook "
"may take, while the first gives 22 of 38 models against 34. Round 1 found that "
"the removals of Figure 10 started from t = 0 where Figure 9 and the deposit's "
"script remove after a control period, that threshold reading (b) of Figure 2 "
"was not computed, that the leak part of Figure 4 could not hold under spike "
"burst bounds, and that the deposited parameters fall outside the Methods' "
"search space; in reply both removal protocols were run, which moved Figure "
"10A from three to four of five, reading (b) was computed, which moved Figure 2 "
"from partially reproduced to reproduced, slow-wave bounds were added, and the "
"parameters became a new finding. Round 2 found sentences with stale timings "
"and measured values that were not printed, which were corrected, and doubted "
"the rule behind the Figure 2 threshold, which the notes now say the outcome "
"rests on. The author asked a reader no questions. The author's session took "
"about 2 h 45 min, and the official run 13, 32 and 13 min for the three "
"notebooks; the first runs of the main notebook failed on an empty slow-wave "
"crossing list, a numba division by zero and a NaN model mask, all fixed "
"before that run. In the second revision about 40 minutes were lost when an "
"entry run started in the background died, and a separate notebook for the "
"Figure 1, figure supplement 3 ramp on 28 models was run once and removed, its "
"result not used; the ramps notebook took 57.9 of its 60 min.")
p2 = ("Four models the Methods name are not in the deposit (major): Q8FBN1 of "
"Figure 6, figure supplement 1 and G81PUL, G7EOZ8 and SAXT8Y of Figure 7. The "
"deposit holds 38 parameter sets, where the paper and the Dryad description "
"say 36, and nothing marks which 36 the paper studied; the 38 share 27 distinct "
"sets of maximal conductances, 9 of which carry two or three Q10 sets. Three "
"models are filed under other names, 0SHNMD and B7SD0L with the digit 0 for the "
"letter O and KMNLBC with two letters swapped, and the Figure 1 model, printed "
"with an unreadable second character, is 4X6W66. At 10 °C the models burst at "
"1.25 Hz on average (0.99 to 1.63 Hz), and 10 of 38 are within 10% of the 1 Hz "
"target the Methods give. The deposited integrator returns NaN for 6 of the 38 "
"models at some temperatures from 26 to 35 °C (29 of 380 runs), at the same "
"step in the deposited Java, though Figure 7A shows J9U8SQ active at 34 °C. The "
"deposited parameters fall outside the Methods' search space: gNa reaches 1992 "
"uS against a bound of 1000, gA 198.6 and gKd 198.8 against 100, the synaptic "
"conductances 0.993 uS against 0.05, and tau_Ca, as the Java uses it, 18,981 ms "
"against 2000; the files may follow another convention or code version than "
"the Methods describe. The deposit has no ramp code, and its README says "
"nothing about which solutions were kept or discarded. In the paper, the LP and "
"PY target duty cycle is 25% in the Methods and 20% in the Results, and the "
"Figure 8A legend's \"before 600 s\" does not fit the stated ramp. Seven "
"questions are put to the paper's authors: the spike threshold, the test of "
"firing order, how the lag d is formed, how the ramps and the high-temperature "
"states were run, which 36 of the 38 models are the paper's, when the "
"conductance was changed for Figure 10, and how the threshold is read from the "
"voltage distribution of Figure 2.")
p3 = ("The author's points on the protocol: its checks of clocks and trial "
"alignment have nothing to apply to in a deposit of code and parameters, and "
"the port was checked against the deposited Java instead; archives.md asks for "
"the SHA-256 that Dryad's file list gives, which gives only an MD5; the entry's "
"hash covers markdown cells, so writing the conclusions after a run forces "
"another full run of about 60 min; it does not say whether to report the "
"reading that ran or to block when a criterion accepts any reading and one is "
"too large to run; the runner's 4 CPUs gave only about 2 times the "
"single-process throughput, which cut down or left out three analyses; and "
"several claims say all 36 models while the deposit holds 38, all of which "
"were used.")
w = lambda p: textwrap.fill(p, 80, break_long_words=False, break_on_hyphens=False)
open("docs/pilot-notes/alonso-2020-01.md","w").write(head+"\n\n"+w(p1)+"\n\n"+w(p2)+"\n\n"+w(p3)+"\n")
s = ("In simulations of the deposited models, the paper's central result held in part: "
"frequency rose with temperature as stated and 36 of 38 models stayed triphasic, but duty "
"cycles and phases did not stay approximately constant in the example models. The shift from "
"A to KCa current at burst end, hysteresis on temperature ramps and a model's need for KCa "
"only at high temperature reproduced. The reorganized currentscapes, the high-temperature "
"crash with PD silenced, and quiescence at both temperatures after removing H did not, in "
"tests that rest on a spike threshold and burst bounds the paper does not give. Slow time "
"scales in crashed networks could not be tested, as three of their five models are not in "
"the deposit.")
open("summaries/alonso-2020-01.md","w").write(s+"\n")
EOF
wc -w summaries/alonso-2020-01.md; grep -c '—\|rather' docs/pilot-notes/alonso-2020-01.md summaries/alonso-2020-01.md; ls summaries | head -3; git status --short
```

```
121 summaries/alonso-2020-01.md
docs/pilot-notes/alonso-2020-01.md:0
summaries/alonso-2020-01.md:0
README.md
allen-2026-01.md
alonso-2020-01.md
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
?? docs/pilot-notes/alonso-2020-01.md
?? scripts
?? summaries/alonso-2020-01.md
```

**Agent**

The summary came out at 121 words, so I'll trim it below 120.

**Agent calls Bash**

```bash
sed -i 's/in tests that rest on/in tests resting on/; s/in the example models/in example models/' summaries/alonso-2020-01.md && wc -w summaries/alonso-2020-01.md && cat summaries/alonso-2020-01.md && cat docs/pilot-notes/alonso-2020-01.md
```

```
119 summaries/alonso-2020-01.md
In simulations of the deposited models, the paper's central result held in part: frequency rose with temperature as stated and 36 of 38 models stayed triphasic, but duty cycles and phases did not stay approximately constant in example models. The shift from A to KCa current at burst end, hysteresis on temperature ramps and a model's need for KCa only at high temperature reproduced. The reorganized currentscapes, the high-temperature crash with PD silenced, and quiescence at both temperatures after removing H did not, in tests resting on a spike threshold and burst bounds the paper does not give. Slow time scales in crashed networks could not be tested, as three of their five models are not in the deposit.
# alonso-2020, Alonso et al. 2020

Eight claims reproduced on the dataset, five partially, five not reproduced and
four blocked, three for missing data and one, `fig8-up-down-ramps`, as too large
to run; the link claim `deposit-models`, that the deposit holds the paper's
models under the names the Methods give and that they give the control rhythm
they were fitted to, is counted apart and was not reproduced (3 of 38 models
within tolerance at 10 °C, against the criterion's 18). Eight outcomes rest on
an assumption, most on the -20 mV spike threshold and the test of firing order,
which the paper does not give, and `fig2-lp-spike-amplitude-threshold` on a rule
for where the spike region of the voltage distribution begins. The first
verification round agreed with 22 of the 23 outcomes and gave
`fig8-up-down-ramps` as not reproduced (provisional) where the record had
blocked; the author kept blocked, and the second round withdrew the objection on
the printed time estimate. The second round agreed with 21 outcomes and held
that `fig6s1-crash-mechanisms` should be blocked for missing data, not not
reproduced; the author proposed that change, and a third round reviewed that one
claim and agreed. It pins version 94811, the only published ver
[... 92 more lines not kept]
```

**Agent**

One awkward phrase ("not not reproduced") to fix in the notes.

**Agent calls Bash**

```bash
python3 - <<'EOF'
import textwrap
f="docs/pilot-notes/alonso-2020-01.md"
t=open(f).read()
paras=t.rstrip("\n").split("\n\n")
p=" ".join(paras[1].split("\n"))
old="should be blocked for missing data, not not reproduced;"
assert old in p
p=p.replace(old,"should be blocked for missing data where the record had not reproduced;")
paras[1]=textwrap.fill(p,80,break_long_words=False,break_on_hyphens=False)
open(f,"w").write("\n\n".join(paras)+"\n")
EOF
grep -n -A1 'should be' docs/pilot-notes/alonso-2020-01.md; git status --short docs summaries
```

```
16:that `fig6s1-crash-mechanisms` should be blocked for missing data where the
17-record had not reproduced; the author proposed that change, and a third round
--
47:spikes at 30 °C where both models should be quiescent; in Figure 8B H5AIZR
48-returns to regular bursting at 17.08 °C and has a longest ISI of 11.32 s,
?? docs/pilot-notes/alonso-2020-01.md
?? summaries/alonso-2020-01.md
```

**Agent**

# alonso-2020, Alonso et al. 2020

Eight claims reproduced on the dataset, five partially, five not reproduced and four blocked, three for missing data and one, `fig8-up-down-ramps`, as too large to run; the link claim `deposit-models`, that the deposit holds the paper's models under the names the Methods give and that they give the control rhythm they were fitted to, is counted apart and was not reproduced (3 of 38 models within tolerance at 10 °C, against the criterion's 18). Eight outcomes rest on an assumption, most on the -20 mV spike threshold and the test of firing order, which the paper does not give, and `fig2-lp-spike-amplitude-threshold` on a rule for where the spike region of the voltage distribution begins. The first verification round agreed with 22 of the 23 outcomes and gave `fig8-up-down-ramps` as not reproduced (provisional) where the record had blocked; the author kept blocked, and the second round withdrew the objection on the printed time estimate. The second round agreed with 21 outcomes and held that `fig6s1-crash-mechanisms` should be blocked for missing data where the record had not reproduced; the author proposed that change, and a third round reviewed that one claim and agreed. It pins version 94811, the only published version. The paper, Alonso and Marder, "Temperature compensation in a small rhythmic circuit" (eLife 9:e55470), simulates a three-cell model of the crustacean pyloric network (PD, LP and PY, each with eight currents and temperature sensitivities set by Q10 values) and reports that 36 models keep a triphasic rhythm from 10 to 25 °C, with burst frequency rising at a Q10 near 2 while duty cycles and phases stay approximately constant, that the currents behind this reorganize with temperature, with a tradeoff between the A and KCa currents at burst termination, that the models crash above 25 °C by different mechanisms, that temperature ramps show hysteresis, and that removing a current has different effects at 10 and 25 °C. The claims were written from the version of record without the legends of its figure supplements, and no figure could be rendered. The dataset is code, not recordings: one zip with the authors' Java model, their Python scripts, one initial-condition file and 38 parameter sets, so every claim was tested by simulating the deposited models, with a numba port of the Java that matches its voltages to 3e-9 mV over 3 s at 18 °C and to 0.06 mV at 25 °C. The frequency Q10 of the Figure 1 model is 1.927, but its LP duty cycle changes by up to 34% from its 10 °C value, so `fig1c-frequency-q10-phase-constant` is partial, and none of the three further models of Figure 1, figure supplement 1 meets either reading of constancy. 36 of the 38 models are triphasic at all 16 temperatures, one of the two that fail (MAXTTP) being a model the paper shows. The largest ISI on a ramp, the spike amplitude and threshold of Figure 2, the diverse peak voltages, the dominant currents (in 0.993 of cases), the A to KCa tradeoff in FGFKQS, the 1.94 °C hysteresis of Figure 8A and the KCa removal of Figure 9B reproduce; the duty-cycle claim of Figure 1, figure supplement 3 only on the criterion's 16-temperature variant, with a test that shows little more than that the distributions are not identical. No part of the Figure 4 currentscape criterion holds under any of four readings; in Figure 6 the PD cell of FGFKQS fires 1005 spikes at 30 °C where both models should be quiescent; in Figure 8B H5AIZR returns to regular bursting at 17.08 °C and has a longest ISI of 11.32 s, against 20 and 1; and removing H leaves 30 of 38 models the same and quiescent at both temperatures, against the 33 asked. Figure 3 is partial with a KCa peak ratio of 8.95 against 6, Figure 9A with all three cells irregular at 25 °C, and Figure 10A with four of five grid cells matching. The 2 in 40 failures cannot be tested, as the screened solutions are not deposited; Figure 6, figure supplement 1 and Figure 7 lack one and three of their models, and with them the outcome can be at best partially reproduced; and the second ramp reading of `fig8-up-down-ramps`, the ramp the paper cites, would take 117 min against the 60 min a notebook may take, while the first gives 22 of 38 models against 34. Round 1 found that the removals of Figure 10 started from t = 0 where Figure 9 and the deposit's script remove after a control period, that threshold reading (b) of Figure 2 was not computed, that the leak part of Figure 4 could not hold under spike burst bounds, and that the deposited parameters fall outside the Methods' search space; in reply both removal protocols were run, which moved Figure 10A from three to four of five, reading (b) was computed, which moved Figure 2 from partially reproduced to reproduced, slow-wave bounds were added, and the parameters became a new finding. Round 2 found sentences with stale timings and measured values that were not printed, which were corrected, and doubted the rule behind the Figure 2 threshold, which the notes now say the outcome rests on. The author asked a reader no questions. The author's session took about 2 h 45 min, and the official run 13, 32 and 13 min for the three notebooks; the first runs of the main notebook failed on an empty slow-wave crossing list, a numba division by zero and a NaN model mask, all fixed before that run. In the second revision about 40 minutes were lost when an entry run started in the background died, and a separate notebook for the Figure 1, figure supplement 3 ramp on 28 models was run once and removed, its result not used; the ramps notebook took 57.9 of its 60 min.

Four models the Methods name are not in the deposit (major): Q8FBN1 of Figure 6, figure supplement 1 and G81PUL, G7EOZ8 and SAXT8Y of Figure 7. The deposit holds 38 parameter sets, where the paper and the Dryad description say 36, and nothing marks which 36 the paper studied; the 38 share 27 distinct sets of maximal conductances, 9 of which carry two or three Q10 sets. Three models are filed under other names, 0SHNMD and B7SD0L with the digit 0 for the letter O and KMNLBC with two letters swapped, and the Figure 1 model, printed with an unreadable second character, is 4X6W66. At 10 °C the models burst at 1.25 Hz on average (0.99 to 1.63 Hz), and 10 of 38 are within 10% of the 1 Hz target the Methods give. The deposited integrator returns NaN for 6 of the 38 models at some temperatures from 26 to 35 °C (29 of 380 runs), at the same step in the deposited Java, though Figure 7A shows J9U8SQ active at 34 °C. The deposited parameters fall outside the Methods' search space: gNa reaches 1992 uS against a bound of 1000, gA 198.6 and gKd 198.8 against 100, the synaptic conductances 0.993 uS against 0.05, and tau_Ca, as the Java uses it, 18,981 ms against 2000; the files may follow another convention or code version than the Methods describe. The deposit has no ramp code, and its README says nothing about which solutions were kept or discarded. In the paper, the LP and PY target duty cycle is 25% in the Methods and 20% in the Results, and the Figure 8A legend's "before 600 s" does not fit the stated ramp. Seven questions are put to the paper's authors: the spike threshold, the test of firing order, how the lag d is formed, how the ramps and the high-temperature states were run, which 36 of the 38 models are the paper's, when the conductance was changed for Figure 10, and how the threshold is read from the voltage distribution of Figure 2.

The author's points on the protocol: its checks of clocks and trial alignment have nothing to apply to in a deposit of code and parameters, and the port was checked against the deposited Java instead; archives.md asks for the SHA-256 that Dryad's file list gives, which gives only an MD5; the entry's hash covers markdown cells, so writing the conclusions after a run forces another full run of about 60 min; it does not say whether to report the reading that ran or to block when a criterion accepts any reading and one is too large to run; the runner's 4 CPUs gave only about 2 times the single-process throughput, which cut down or left out three analyses; and several claims say all 36 models while the deposit holds 38, all of which were used.

---

In simulations of the deposited models, the paper's central result held in part: frequency rose with temperature as stated and 36 of 38 models stayed triphasic, but duty cycles and phases did not stay approximately constant in example models. The shift from A to KCa current at burst end, hysteresis on temperature ramps and a model's need for KCa only at high temperature reproduced. The reorganized currentscapes, the high-temperature crash with PD silenced, and quiescence at both temperatures after removing H did not, in tests resting on a spike threshold and burst bounds the paper does not give. Slow time scales in crashed networks could not be tested, as three of their five models are not in the deposit.

---

The notes are in `docs/pilot-notes/alonso-2020-01.md` and the summary is in `summaries/alonso-2020-01.md` (119 words). This dataset has no entry in `targets/dandisets.json`. Its entry is in `targets/dryad.json`, and the `catalystneuro` field there is empty, so the notes have no conversion sentence. Nothing is committed. The untracked dotfiles in the repository root were already there; I did not create them.

## End of run

16 turns, 3 minutes, $1.33 at API prices, result: success.
