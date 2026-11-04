# 001687 · recorder · run 41674257711

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py 001687; ls claims/001687 transcripts/001687; ls docs/pilot-notes | grep 001687
```

```
docs/pilot-notes/001746-liu-2026-01.md
docs/pilot-notes/001676-skromne-carrasco-2026-01.md
docs/pilot-notes/001702-chaunsali-2025-01.md
docs/pilot-notes/001605-funamizu-2016-01.md
docs/pilot-notes/001642-ito-2015-01.md
| [001687](https://dandiarchive.org/dandiset/001687) | [Xiao et al. 2026](https://doi.org/10.1016/j.neuron.2026.05.027) | 12 | 3 | 3 | 22 | [`001687-xiao-2026`](entries/001687-xiao-2026) |
claims/001687:
10.1016-j.neuron.2026.05.027.yaml

transcripts/001687:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author.md
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in 001746-liu-2026-01 001676-skromne-carrasco-2026-01 001702-chaunsali-2025-01 001605-funamizu-2016-01 001642-ito-2015-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; grep -n "^| Dandiset\|^| ---" README.md | head; ls -la --time-style=full-iso transcripts/001687
```

```
<persisted-output>
Output too large (46.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/201fb439-e206-4364-8e35-3755987c0f47/tool-results/bh73ui250.txt

Preview (first 2KB):
=== 001746-liu-2026-01
# 001746, Liu et al. 2026

Four claims reproduced, eight partially (one on an assumption), one not
reproduced and six blocked, three as methods underspecified and three for
missing data; the three claims that also use inputs from outside the dataset
(the code's morphology table and AIS distances, the 10x transcriptomes in GEO)
are counted apart: one reproduced, one not reproduced and one blocked as
methods underspecified. Of the 33 claims, two are link checks, both reproduced,
the cell table's on an assumption, and one of them, `morph-table-link`, was
added by the author; nine have their data in other dandisets or archives and
are blocked as other. The first verification round agreed with 29 of the 33
outcomes as they stood and the second with 30, disagreeing on
`fig3e-phase-peak-index`, `fig3d-saddle-phase-plane` and
`fig4i-peak-index-ais-distance-real`; the author proposed blocking all three,
and a third round, which reviewed only these, agreed with all of them. It pins
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/201fb439-e206-4364-8e35-3755987c0f47/tool-results/bh73ui250.txt"
}
```

```
1	=== 001746-liu-2026-01
2	# 001746, Liu et al. 2026
3	
4	Four claims reproduced, eight partially (one on an assumption), one not
5	reproduced and six blocked, three as methods underspecified and three for
6	missing data; the three claims that also use inputs from outside the dataset
7	(the code's morphology table and AIS distances, the 10x transcriptomes in GEO)
8	are counted apart: one reproduced, one not reproduced and one blocked as
9	methods underspecified. Of the 33 claims, two are link checks, both reproduced,
10	the cell table's on an assumption, and one of them, `morph-table-link`, was
11	added by the author; nine have their data in other dandisets or archives and
12	are blocked as other. The first verification round agreed with 29 of the 33
13	outcomes as they stood and the second with 30, disagreeing on
14	`fig3e-phase-peak-index`, `fig3d-saddle-phase-plane` and
15	`fig4i-peak-index-ais-distance-real`; the author proposed blocking all three,
16	and a third round, which reviewed only these, agreed with all of them. It pins
17	version 0.260825.0222, the only published version; the draft lists the same
18	files, and the paper cites none. The paper, Liu, Huang, Shen, Shao, Jing et
19	al., "An atlas of primate insular cortex reveals a signal-processing strategy
20	in von Economo neurons" in Nature Cell Biology, profiles neurons of the
[... 625 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/001687-xiao-2026-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
import sys
for e in (it if isinstance(it,list) else it.values()):
  if '001687' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))
"; grep -n "001687" README.md; head -30 README.md | grep -n "|"
```

```
<persisted-output>
Output too large (103.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/201fb439-e206-4364-8e35-3755987c0f47/tool-results/b07xem6x2.txt

Preview (first 2KB):
schema_version: 2
id: 001687-xiao-2026-01
dataset:
  archive: dandi
  id: 001687
  version: 0.260821.2126
  doi: 10.48324/dandi.001687/0.260821.2126
paper: doi:10.1016/j.neuron.2026.05.027
date: '2026-11-03'
entry: 001687-xiao-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 32 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/201fb439-e206-4364-8e35-3755987c0f47/tool-results/b07xem6x2.txt"
}
```

```
1	schema_version: 2
2	id: 001687-xiao-2026-01
3	dataset:
4	  archive: dandi
5	  id: 001687
6	  version: 0.260821.2126
7	  doi: 10.48324/dandi.001687/0.260821.2126
8	paper: doi:10.1016/j.neuron.2026.05.027
9	date: '2026-11-03'
10	entry: 001687-xiao-2026
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
[... 770 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/201fb439-e206-4364-8e35-3755987c0f47/tool-results/b07xem6x2.txt",
 "offset": 791,
 "limit": 760
}
```

```
791	  notes: 'No SpVi-TeLC mouse is in the dandiset: all 36 subjects are C57 wild type and no file names TeLC
792	    or vGat-Cre, although the dandiset''s description names long-range internuclear inhibition among its
793	    perturbations. Looked in the asset list and every file''s metadata; the paper names no other archive
794	    for these data.'
795	- claim: fig5e-telc-untuned-ambiguous-unchanged
796	  outcome: blocked
797	  blocked_by: data_missing
798	  notes: 'No SpVi-TeLC mouse is in the dandiset: all 36 subjects are C57 wild type and no file names TeLC
799	    or vGat-Cre, although the dandiset''s description names long-range internuclear inhibition among its
800	    perturbations. Looked in the asset list and every file''s metadata; the paper names no other archive
801	    for these data.'
802	- claim: figs6j-telc-untuned-higher-firing
803	  outcome: blocked
804	  blocked_by: data_missing
805	  notes: 'No SpVi-TeLC mouse is in the dandiset: all 36 subjects are C57 wild type and no file names TeLC
806	    or vGat-Cre, although the dandiset''s description names long-range internuclear inhibition among its
807	    perturbations. Looked in the asset list and every file''s metadata; the paper names no other archive
808	    for these data.'
809	- claim: figs6k-telc-tuned-baseline-similar
810	  outcome: blocked
[... 727 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "assumed" attempts/001687-xiao-2026-01.yaml | head; grep -n -B3 "001746" README.md | head; python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
def walk(x):
    if isinstance(x,dict):
        if any(str(v)=='001687' for v in x.values()): print(json.dumps(x,indent=1)); return
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(d)
E
```

```
88:    SNR below comes from short stretches of raw voltage under an assumed definition); units are the 1,160
118:    SNR below comes from short stretches of raw voltage under an assumed definition); units are the 1,160
263:    SNR below comes from short stretches of raw voltage under an assumed definition); units are the 1,160
298:    SNR below comes from short stretches of raw voltage under an assumed definition); units are the 1,160
339:    SNR below comes from short stretches of raw voltage under an assumed definition); units are the 1,160
369:    SNR below comes from short stretches of raw voltage under an assumed definition); units are the 1,160
420:    SNR below comes from short stretches of raw voltage under an assumed definition); units are the 1,160
470:    SNR below comes from short stretches of raw voltage under an assumed definition); units are the 1,160
514:    SNR below comes from short stretches of raw voltage under an assumed definition); units are the 1,160
558:    SNR below comes from short stretches of raw voltage under an assumed definition); units are the 1,160
{
 "dandiset": "001687",
 "name": "Data related to \"Xiao, Severson, et al. (2026) Peri-Head Distance Coding in the Mouse Brainstem\"",
 "published_version": "0.260821.2126",
 "asset_count": 191,
 "size_gb": 2076.97,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "Reproduced\|Partial" README.md | head -5; sed -n 1,60p tools/readme_row.py; cd transcripts/001687; for f in author-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (40.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/201fb439-e206-4364-8e35-3755987c0f47/tool-results/b3d61qvqp.txt

Preview (first 2KB):
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

[... 37 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/201fb439-e206-4364-8e35-3755987c0f47/tool-results/b3d61qvqp.txt",
 "offset": 55
}
```

```
55	        for outcome in COLUMNS:
56	            mine = [o for o in record["outcomes"] if o["outcome"] == outcome]
57	            n = sum(1 for o in mine if kinds.get(o["claim"], "dataset") in ("dataset", "with_labels"))
58	            m = sum(1 for o in mine if kinds.get(o["claim"]) == "with_inputs")
59	            cells.append(f"{n} (+{m})" if m else str(n))
60	    _, surname, year = entry_dir.name.rsplit("-", 2)
61	=== author-report.md
62	I did steps 1 to 5 of the Author protocol and built the handover with `python tools/entry.py handover`. The entry passes `check` and `run` from a clean environment, and nothing is committed. The new files are `entries/001687-xiao-2026/`, `attempts/001687-xiao-2026-01.yaml` and `questions/001687.yaml`.
63	
64	**The main risk:** the claims file makes the Methods' uncorrected responsiveness test (p < 0.05 at any distance) the main reading. That test cannot give the paper's own counts: it marks 1,061 of 1,160 units responsive, against 768 in the paper. The code's BH-FDR test gives 782, matches the deposit's labels unit for unit, and would turn several outcomes below into reproduced. Every claim is shown under both tests, and the question is filed for a reader.
65	
66	## 1. Outcomes (41 claims)
67	
68	| Claim | Outcome |
69	|---|---|
70	| si-unit-yield | reproduced (1,160 units against 1,141; SNR criterion not applicable) |
71	| fig2-wall-responsive-counts, fig2-distance-tuned-counts, fig2f-tuning-categories | not reproduced under the Methods' test; code's BH-FDR variant reproduces 1 and 3 |
72	| figs4a-baseline-activated-lower, figs4a-baseline-suppressed-similar, figs4c-untuned-no-change | reproduced |
73	| fig2de-preferred-distances-span, figs4ef-crossvalidated-stability, figs4j-ventral-location | reproduced |
74	| fig3a-decoding-above-controls, fig3-overall-decoding-accuracy | reproduced |
[... 296 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/001687/10.1016-j.neuron.2026.05.027.yaml; grep -n "^[a-z_]*:" $f; sed -n 1,80p $f; grep -n "data:\|where:\|kind:" $f | head -20
```

```
105:schema_version: 2
106:dataset:
109:paper: doi:10.1016/j.neuron.2026.05.027
110:claims:
1507:checks:
# Claims for Xiao, Severson et al. (2026), "Peri-head distance coding in the mouse brainstem",
# Neuron, doi:10.1016/j.neuron.2026.05.027, on dandiset 001687.
#
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the accepted author manuscript in PubMed Central (NIHMS2191201, PMC13336321), as
# fetched 2026-10-20 into paper/10.1016-j.neuron.2026.05.027.txt: main text, STAR Methods, the
# legends of Figures 1 to 6, and the supplement file NIHMS2191201-supplement-1.pdf (legends of
# Figures S1 to S6 and Tables S2 to S5). The version of record was not read. Tables S1 (mouse
# sex, age and figure assignments) and S6 (test statistics, degrees of freedom and p-values of
# all analyses) are named in the text but are not in the supplement file read; every number
# used below is in the main text, the legends or Tables S2 to S5. Figures were not opened.
#
# Code read: github.com/wanglab-neuro/2026_Xiao-Severson_Peri-head-distance at commit b1a9f3c
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/001687/10.1016-j.neuron.2026.05.027.yaml; sed -n 80,110p $f; sed -n 1505,1600p $f
```

```
#   (distance d above 7 mm) significant after BH-FDR across the eight (Methods; Figure S4H
#   legend; code). Ambiguous: activated, tuned, preferred at least 9 mm, no significant test.
#   Suppressed-only: tuned, suppressed, never activated. Untuned: wall-responsive and not
#   distance-tuned (Methods; code).
# - Population decoding (Methods; Fig3ABC_Decoder_Accuracy_Time_Confusion_Avg.m): maximum
#   correlation coefficient classifier of the Neural Decoding Toolbox on a pseudo-population;
#   spike counts in 150-ms windows stepped by 50 ms from 0 to 14 s; 15 passes per distance,
#   resampled 5 times; z-score feature normalisation (code; Methods silent); subpopulations of
#   118 units drawn 10 times without replacement (the combined group 36 map and 82 proximity
#   units); a shuffled group from map and proximity units with the passes' distance labels
#   scrambled; accuracy per distance is the true-positive rate, averaged over the time bins
#   starting within 3 to 11 s; overall accuracy is the mean over the nine distances (Table S2,
#   "Average"). Cross-validation is 10-fold in the Methods and 15 splits (one pass per distance
#   held out) in the code: the Methods' 10-fold is the main reading, the code's the variant.
#   Group comparisons per distance are Wilcoxon rank-sum tests on the 10 subsample values,
#   BH-FDR across the nine distances (Methods; Figure 3C legend; code).
#
# Inconsistencies in the paper, noted where they bear on a claim: 472 activated + 213 suppressed
# - 29 both = 656 tuned implies 184 suppressed-only and 112 untuned, but Figure 2F gives 119 and
# 177 (fig2f-tuning-categories); the Figure 4B legend gives 11.58 +/- 2.986 sp/s where the text
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^[a-z_]*:" attempts/001687-xiao-2026-01.yaml; grep -n -i "PrV\b\|principal" claims/001687/*.yaml | head -5; grep -n "^- id:" claims/001687/*.yaml | wc -l
```

```
1:schema_version: 2
2:id: 001687-xiao-2026-01
3:dataset:
8:paper: doi:10.1016/j.neuron.2026.05.027
9:date: '2026-11-03'
10:entry: 001687-xiao-2026
11:provenance:
22:inputs:
27:outcomes:
861:findings:
920:verifications:
19:# (PrV_simulation/simulate_prv.py), and a submodule (Processing, the spike-sorting pipeline;
43:# - PrV GtACR optogenetics (vGat-Cre, N = 2): 112 units; distances 7 to 23 mm in 4-mm steps,
211:    Of 46 tungsten-recorded PrV units from 14 mice, 41 (89.1%) were wall-activated, 3 (6.5%)
213:  source: Results, PrV contains both proximity and map codes, paragraphs 1-2
243:  source: Results, PrV contains both proximity and map codes, paragraph 2; Figure S2D-F
41
```

**Agent**

Now writing the note.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/001687-xiao-2026-01.md",
 "content": "# 001687, Xiao et al. 2026\n\nTwelve claims reproduced, three partially, three not reproduced and 22 blocked,\n16 for missing data and six for insufficient metadata; no outcome rests on an\nassumption. Of the 41 claims, 40 are on the dandiset and one,\n`fig6-model-telc-loses-map`, runs the paper's PrV circuit model from its code\nrepository and is counted apart: reproduced. The first verification round agreed\nwith 38 of the 41 outcomes as they stood and the second with all 41, and nothing\nwas proposed after the second, so there was no third round. It pins version\n0.260821.2126, the latest published version; the paper cites none, and it holds\nthe same 191 assets as 0.260805.1529. The paper, Xiao, Severson et al.,\n\"Peri-head distance coding in the mouse brainstem\" in Neuron, records units in\nPrV of awake head-fixed mice while a wall passes the face at distances of 7 to\n23 mm, and reports the proximity and map units of wild-type silicon-probe\nrecordings (Fig. 2, Figure S4), the decoding of wall distance from them (Fig. 3,\nFigure S5), the effect of cutting all but one whisker (Fig. 4), SpVi-TeLC mice\n(Fig. 5, Fig. 6, Figure S6), GtACR optogenetics (Figure S6), tungsten recordings\n(Figure S2), whisker kinematics from video (Figure S1) and a circuit model (Fig.\n6). The claims were written from the accepted author manuscript in PubMed\nCentral (NIHMS2191201, PMC13336321) and its supplement file, without the version\nof record, Tables S1 and S6 or the figures, and from the paper's code at commit\nb1a9f3c; the check made eleven changes and left three points open, and its first\nchange made the Methods' uncorrected responsiveness test the main reading.\nReproduced are `si-unit-yield` (1,160 units from 36 mice against 1,141),\n`fig2-wall-responsive-counts` (782, 541, 337 and 96 against 768, 532, 333 and\n97), `fig2f-tuning-categories` (271, 120, 87, 122 and 182), the two Figure S4A\nbaseline claims, `figs4c-untuned-no-change`, `fig2de-preferred-distances-span`,\n`figs4j-ventral-location` (median depth 350 against 525 um for unresponsive\nunits), `fig3a-decoding-above-controls`, `fig3-overall-decoding-accuracy` (map\n70.44, combined 60.90, proximity 48.37, suppressed-only 33.69, untuned 16.38 and\nshuffled 11.04%), `fig3c-decoding-error` and `figs5c-single-neuron-decoders`;\nthe model gives 593 and 631 tuned neurons on the nine-bin grid the criterion\nnames and the paper's 590 and 636 exactly on the code's 99-point grid. Partial\nare `figs4b-activated-increase-suppressed-decrease` (activated baseline 5.36 or\n5.40 sp/s against 6.36 +/- 0.704), `figs4l-temporal-windows-map` (offset count\n68 or 42 against 34 +/- 3.4) and `fig3c-decoding-by-distance` (part (a) fails at\n9 mm, proximity at 15 mm 32.0% against 36.29 +/- 3.63). Not reproduced are\n`fig2-distance-tuned-counts` (92 units both activated and suppressed against 29\n+/- 2.9), `figs4ef-crossvalidated-stability` (Spearman 0.815 for activated\nagainst 0.831 for suppressed units, with the ranges over 100 splits\noverlapping) and `figs5de-svm-robust` (combined group 61.87% against 54.43 +/-\n5.44), all three under criteria with no partial rule. The 16 claims on the\nwhisker kinematics, tungsten, GtACR and TeLC recordings are blocked for missing\ndata, and the six whisker-cutting claims for insufficient metadata. The author's\nfirst run judged claims on the uncorrected test and gave 10 reproduced, 6\npartially, 3 not reproduced and 22 blocked. The author asked a reader whether\nthe code's BH-FDR test should be the main reading; the reader answered that it\nshould and changed the claims file, and the author-answers run moved\n`fig2-wall-responsive-counts` and `fig2f-tuning-categories` from not reproduced\nto reproduced, `fig2-distance-tuned-counts` from not reproduced and\n`figs4ef-crossvalidated-stability` from reproduced to partially reproduced, and\n`fig3c-decoding-error` and `figs5c-single-neuron-decoders` from partially\nreproduced to reproduced. Round 1 disagreed with three outcomes, the partial\noutcomes under criteria with no partial rule, and found that the claims file's\nchecks log still named the uncorrected test as main, that the expected 656 and\n29 contradict Figure 2F, that SNR could be approximated from the raw voltage and\nthe Methods' duplicate rule was not applied, that the 1-mm-step sessions were\nnot run the deposit's way and post-cut trials were kept, that the orientation of\n`rel_y` was unchecked, that the model's captured output lines were unlabelled\nand that the cutting claims could be tried on stability subsets; in reply the\nthree outcomes changed to not reproduced, an SNR, the duplicate rule (9 pairs),\ntwo pass-set variants, the depth orientation, the labelled model lines, the\ncutting subsets, the pass-epoch columns and seven other baselines for\n`figs4b` were added, and a question on the Figure 2F values was filed in\n`questions/001687.yaml`. Round 2 agreed with all 41 and found sentences the\noutputs did not support (p 3.85e-25 for 3.48e-25, the window (ii) values, \"a\nfresh random permutation\" of distances, a stale \"not attempted\" sentence in six\ncutting notes, the uncorrected counts in a BH-FDR deviation and an overstated\nSNR point), asked for the probe_site description, a permutation check and the\nraw-pass alignment of two cutting sessions, and noted two misreadings in the\nclaims file (the `fig4b` tolerance of 1.338 where the criterion names 2.986, and\nthe nine-bin grid of the model claim); in reply these were corrected or added and\nboth misreadings were filed as questions for a reader, while the stale checks\nlog was left, as the claims file is the reader's. The author's run took about 1\nh 50 min (08:24 to 10:14 UTC); two development runs failed on code errors (a\npandas column name clash and a name defined after its first use) and were\nfixed; the notebook ran in about 22 minutes at first, 29 minutes after the\nauthor-answers run, about 34 minutes after round 1 and about 30 minutes at the\nend. Untracked dotfiles and a `scripts` folder in the checkout were left alone.\n\nThe dandiset holds only the wild-type silicon-probe recordings (67 sessions, 36\nC57 mice, 1,358 units): the tungsten recordings, the SpVi-TeLC and GtACR mice,\nthe anesthetized and single-row video sessions and all tracked whisker\nkinematics are absent, although its description names the local and long-range\ninhibition perturbations, and the raw files hold only untracked behaviour video\n(57 mp4 files, 1,706 GB), so 16 of the 41 claims cannot be tested. In the 25\nwhisker-cutting sessions the processed files hold only the full-array passes and\ntrial_condition is empty in every file; the post-cut passes are listed only in\nthe raw files' wall_pass_epochs, with start and stop times and no wall distance,\nthe raw wall-actuator line takes the same two levels at every distance, and the\ndistances come in blocks that are permutations in a varying order (1,263 of\n1,279 blocks, and every block in 66 of 67 sessions), so the post-cut distances\ncannot be inferred. The paper's 195 units with stable waveforms from 18 mice\ncannot be identified among the deposit's 445 units from 25 mice (384 passing the\nISI and firing criteria), which have no stability flag; on stand-in subsets the\nbaseline result turns on the threshold (p 0.0141, 0.29 and 0.251), and one\nsubset of 79 units meets the `fig4b-cut-wall-firing-reduced` criterion (12.70\nagainst 8.88 sp/s). The processed files carry no SNR, ISI false-alarm rate,\nisolation flag, waveforms or peak channels, so unit criteria and depths could\nbe recomputed only in part or from the raw voltage; the deposit's\nwall_responsive labels already exclude units that fail isolation, and the 18\nunits that test responsive but are labelled unresponsive have median SNR 4.22\nagainst 7.91, while 75 of the 768 labelled-responsive units are also below 5. In\n20230711_sp_session_1 and 20230608_sp_session_1 the full-array trials are raw\npasses 21 to 220 and 51 to 250 of 400, so 20 and 50 of them come after the gap\nwhere the session notes place the cut; with the distances moved to raw passes 1\nto 200 none of the 18 and 13 units is distance-tuned, against 10 and 9 as\ndeposited. The Methods do not say whether the responsiveness test is corrected,\nwhile the code applies BH-FDR across the nine distances; the paper's counts and\nthe deposit's labels follow the corrected test, and the uncorrected test marks\n1,061 of 1,160 units responsive. In the two 1-mm-step sessions (38 units) the\nstored tuning curves use only the distance nearest each bin centre, where the\nMethods pool all distances in a 2-mm bin; in the other 65 sessions they equal\nthe rates from the spike times except for one unit in each of 10 sessions. In\nFig3ABC_Decoder_Accuracy_Time_Confusion_Avg.m the branch that builds the\ncombined subsamples does not update rand_unit_names, so as published it would\nsave the previous population's units; the mixture drawn here gives 55.29 to\n62.64% against 58.55%. Of the paper itself, the text's 656 distance-tuned units\n(472 + 213 - 29) conflict with Figure 2F, which implies 591, and the data give\n600 tuned and 182 untuned units, with 92 both activated and suppressed against\n29; the Figure 4B legend gives 11.58 +/- 2.986 sp/s where the text gives +/-\n1.338, and the Figure S6J legend prints p = 3.98 x 10^-3 where the text prints\n3.98 x 10^-5. No questions are put to the paper's authors.\n\nThe author's points on the protocol: it puts the Methods first even when their\nreading cannot give the paper's own expected values, so the claims were tested\nas written and the question filed; it does not say what to do when a claim's\npopulation cannot be formed but a larger set can be analysed, so the cutting\nclaims were blocked with the larger set's results in the notes; the suggested\nclock check with shifted labels fails when the shift is the same for every unit,\nas the decoder learns the relabelling (70.0% against 70.6%), so pass times\nshifted by 30 s (11.8%) were used; \"record the first reading the criterion\nlists\" is ambiguous when readings vary on two axes; two criteria have no partial\nrule, and the protocol's general definition of partially reproduced was applied;\nit does not say whether a cut-down version of the paper's method is a deviation\nor a too_large block, and the depth and SVM analyses were run in reduced form as\ndeviations; and it does not say how dependent claims inherit a population when\nthe upstream classification's main reading fails, so both classifications were\nrun throughout.\n"
}
```

```
File created successfully at: docs/pilot-notes/001687-xiao-2026-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -n -i "rather\|—\|\*\*" docs/pilot-notes/001687-xiao-2026-01.md; git status --short
```

```
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
?? docs/pilot-notes/001687-xiao-2026-01.md
?? scripts
```

**Agent**

I wrote `docs/pilot-notes/001687-xiao-2026-01.md` and changed no other file. Nothing is committed. The dotfiles and `scripts` folder that show as untracked were there before this run. Here is the note:

# 001687, Xiao et al. 2026

Twelve claims reproduced, three partially, three not reproduced and 22 blocked, 16 for missing data and six for insufficient metadata; no outcome rests on an assumption. Of the 41 claims, 40 are on the dandiset and one, `fig6-model-telc-loses-map`, runs the paper's PrV circuit model from its code repository and is counted apart: reproduced. The first verification round agreed with 38 of the 41 outcomes as they stood and the second with all 41, and nothing was proposed after the second, so there was no third round. It pins version 0.260821.2126, the latest published version; the paper cites none, and it holds the same 191 assets as 0.260805.1529. The paper, Xiao, Severson et al., "Peri-head distance coding in the mouse brainstem" in Neuron, records units in PrV of awake head-fixed mice while a wall passes the face at distances of 7 to 23 mm, and reports the proximity and map units of wild-type silicon-probe recordings (Fig. 2, Figure S4), the decoding of wall distance from them (Fig. 3, Figure S5), the effect of cutting all but one whisker (Fig. 4), SpVi-TeLC mice (Fig. 5, Fig. 6, Figure S6), GtACR optogenetics (Figure S6), tungsten recordings (Figure S2), whisker kinematics from video (Figure S1) and a circuit model (Fig. 6). The claims were written from the accepted author manuscript in PubMed Central (NIHMS2191201, PMC13336321) and its supplement file, without the version of record, Tables S1 and S6 or the figures, and from the paper's code at commit b1a9f3c; the check made eleven changes and left three points open, and its first change made the Methods' uncorrected responsiveness test the main reading. Reproduced are `si-unit-yield` (1,160 units from 36 mice against 1,141), `fig2-wall-responsive-counts` (782, 541, 337 and 96 against 768, 532, 333 and 97), `fig2f-tuning-categories` (271, 120, 87, 122 and 182), the two Figure S4A baseline claims, `figs4c-untuned-no-change`, `fig2de-preferred-distances-span`, `figs4j-ventral-location` (median depth 350 against 525 um for unresponsive units), `fig3a-decoding-above-controls`, `fig3-overall-decoding-accuracy` (map 70.44, combined 60.90, proximity 48.37, suppressed-only 33.69, untuned 16.38 and shuffled 11.04%), `fig3c-decoding-error` and `figs5c-single-neuron-decoders`; the model gives 593 and 631 tuned neurons on the nine-bin grid the criterion names and the paper's 590 and 636 exactly on the code's 99-point grid. Partial are `figs4b-activated-increase-suppressed-decrease` (activated baseline 5.36 or 5.40 sp/s against 6.36 +/- 0.704), `figs4l-temporal-windows-map` (offset count 68 or 42 against 34 +/- 3.4) and `fig3c-decoding-by-distance` (part (a) fails at 9 mm, proximity at 15 mm 32.0% against 36.29 +/- 3.63). Not reproduced are `fig2-distance-tuned-counts` (92 units both activated and suppressed against 29 +/- 2.9), `figs4ef-crossvalidated-stability` (Spearman 0.815 for activated against 0.831 for suppressed units, with the ranges over 100 splits overlapping) and `figs5de-svm-robust` (combined group 61.87% against 54.43 +/- 5.44), all three under criteria with no partial rule. The 16 claims on the whisker kinematics, tungsten, GtACR and TeLC recordings are blocked for missing data, and the six whisker-cutting claims for insufficient metadata. The author's first run judged claims on the uncorrected test and gave 10 reproduced, 6 partially, 3 not reproduced and 22 blocked. The author asked a reader whether the code's BH-FDR test should be the main reading; the reader answered that it should and changed the claims file, and the author-answers run moved `fig2-wall-responsive-counts` and `fig2f-tuning-categories` from not reproduced to reproduced, `fig2-distance-tuned-counts` from not reproduced and `figs4ef-crossvalidated-stability` from reproduced to partially reproduced, and `fig3c-decoding-error` and `figs5c-single-neuron-decoders` from partially reproduced to reproduced. Round 1 disagreed with three outcomes, the partial outcomes under criteria with no partial rule, and found that the claims file's checks log still named the uncorrected test as main, that the expected 656 and 29 contradict Figure 2F, that SNR could be approximated from the raw voltage and the Methods' duplicate rule was not applied, that the 1-mm-step sessions were not run the deposit's way and post-cut trials were kept, that the orientation of `rel_y` was unchecked, that the model's captured output lines were unlabelled and that the cutting claims could be tried on stability subsets; in reply the three outcomes changed to not reproduced, an SNR, the duplicate rule (9 pairs), two pass-set variants, the depth orientation, the labelled model lines, the cutting subsets, the pass-epoch columns and seven other baselines for `figs4b` were added, and a question on the Figure 2F values was filed in `questions/001687.yaml`. Round 2 agreed with all 41 and found sentences the outputs did not support (p 3.85e-25 for 3.48e-25, the window (ii) values, "a fresh random permutation" of distances, a stale "not attempted" sentence in six cutting notes, the uncorrected counts in a BH-FDR deviation and an overstated SNR point), asked for the probe_site description, a permutation check and the raw-pass alignment of two cutting sessions, and noted two misreadings in the claims file (the `fig4b` tolerance of 1.338 where the criterion names 2.986, and the nine-bin grid of the model claim); in reply these were corrected or added and both misreadings were filed as questions for a reader, while the stale checks log was left, as the claims file is the reader's. The author's run took about 1 h 50 min (08:24 to 10:14 UTC); two development runs failed on code errors (a pandas column name clash and a name defined after its first use) and were fixed; the notebook ran in about 22 minutes at first, 29 minutes after the author-answers run, about 34 minutes after round 1 and about 30 minutes at the end. Untracked dotfiles and a `scripts` folder in the checkout were left alone.

The dandiset holds only the wild-type silicon-probe recordings (67 sessions, 36 C57 mice, 1,358 units): the tungsten recordings, the SpVi-TeLC and GtACR mice, the anesthetized and single-row video sessions and all tracked whisker kinematics are absent, although its description names the local and long-range inhibition perturbations, and the raw files hold only untracked behaviour video (57 mp4 files, 1,706 GB), so 16 of the 41 claims cannot be tested. In the 25 whisker-cutting sessions the processed files hold only the full-array passes and trial_condition is empty in every file; the post-cut passes are listed only in the raw files' wall_pass_epochs, with start and stop times and no wall distance, the raw wall-actuator line takes the same two levels at every distance, and the distances come in blocks that are permutations in a varying order (1,263 of 1,279 blocks, and every block in 66 of 67 sessions), so the post-cut distances cannot be inferred. The paper's 195 units with stable waveforms from 18 mice cannot be identified among the deposit's 445 units from 25 mice (384 passing the ISI and firing criteria), which have no stability flag; on stand-in subsets the baseline result turns on the threshold (p 0.0141, 0.29 and 0.251), and one subset of 79 units meets the `fig4b-cut-wall-firing-reduced` criterion (12.70 against 8.88 sp/s). The processed files carry no SNR, ISI false-alarm rate, isolation flag, waveforms or peak channels, so unit criteria and depths could be recomputed only in part or from the raw voltage; the deposit's wall_responsive labels already exclude units that fail isolation, and the 18 units that test responsive but are labelled unresponsive have median SNR 4.22 against 7.91, while 75 of the 768 labelled-responsive units are also below 5. In 20230711_sp_session_1 and 20230608_sp_session_1 the full-array trials are raw passes 21 to 220 and 51 to 250 of 400, so 20 and 50 of them come after the gap where the session notes place the cut; with the distances moved to raw passes 1 to 200 none of the 18 and 13 units is distance-tuned, against 10 and 9 as deposited. The Methods do not say whether the responsiveness test is corrected, while the code applies BH-FDR across the nine distances; the paper's counts and the deposit's labels follow the corrected test, and the uncorrected test marks 1,061 of 1,160 units responsive. In the two 1-mm-step sessions (38 units) the stored tuning curves use only the distance nearest each bin centre, where the Methods pool all distances in a 2-mm bin; in the other 65 sessions they equal the rates from the spike times except for one unit in each of 10 sessions. In Fig3ABC_Decoder_Accuracy_Time_Confusion_Avg.m the branch that builds the combined subsamples does not update rand_unit_names, so as published it would save the previous population's units; the mixture drawn here gives 55.29 to 62.64% against 58.55%. Of the paper itself, the text's 656 distance-tuned units (472 + 213 - 29) conflict with Figure 2F, which implies 591, and the data give 600 tuned and 182 untuned units, with 92 both activated and suppressed against 29; the Figure 4B legend gives 11.58 +/- 2.986 sp/s where the text gives +/- 1.338, and the Figure S6J legend prints p = 3.98 x 10^-3 where the text prints 3.98 x 10^-5. No questions are put to the paper's authors.

The author's points on the protocol: it puts the Methods first even when their reading cannot give the paper's own expected values, so the claims were tested as written and the question filed; it does not say what to do when a claim's population cannot be formed but a larger set can be analysed, so the cutting claims were blocked with the larger set's results in the notes; the suggested clock check with shifted labels fails when the shift is the same for every unit, as the decoder learns the relabelling (70.0% against 70.6%), so pass times shifted by 30 s (11.8%) were used; "record the first reading the criterion lists" is ambiguous when readings vary on two axes; two criteria have no partial rule, and the protocol's general definition of partially reproduced was applied; it does not say whether a cut-down version of the paper's method is a deviation or a too_large block, and the depth and SVM analyses were run in reduced form as deviations; and it does not say how dependent claims inherit a population when the upstream classification's main reading fails, so both classifications were run throughout.

## End of run

15 turns, 2 minutes, $1.36 at API prices, result: success.
