# kaku-2025 · recorder · run 44182106411

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py kaku-2025; ls transcripts/kaku-2025/; wc -c attempts/kaku-2025-01.yaml claims/kaku-2025.yaml transcripts/kaku-2025/*; ls summaries | head
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/ashworth-2025-01.md
| [001619](https://dandiarchive.org/dandiset/001619) | [Kaku et al. 2025](https://doi.org/10.1101/2025.01.27.635041) | 12 | 3 | 7 | 23 (+1) | [`kaku-2025`](entries/kaku-2025) |
answer-report.md
answer.md
author-answers-report.md
author-answers.md
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
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 ashworth-2025-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; echo "--- summary"; cat summaries/$f.md; done; head -5 docs/pilot-notes/knierim-2000-02.md; cat summaries/README.md
```

```
<persisted-output>
Output too large (41.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/dc35d623-1a46-40f9-9af5-e20efea8fb8c/tool-results/brgghetua.txt

Preview (first 2KB):
=== amjad-2025-01
# 002013, Amjad et al. 2025

Seven claims reproduced, one partially and five blocked on the dandiset,
plus one claim linking the dandiset to the paper's Zenodo deposit,
reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
agreed with every outcome. The paper describes microinvasive probes for
recording dopamine and electrical activity in monkeys; the beta burst,
reward and unit isolation claims reproduce, the dopamine reward effect
weakly (p = 0.023, and not in the stored trial-aligned `da`).

The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
the same conversion as 002014), and many findings are the same: each event
is stored about five times, once per overlapping trial window; trial
conditions are not in the trials table; the FSCV table columns carry no
units and the raw FSCV current is labelled amperes with values in the
[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/dc35d623-1a46-40f9-9af5-e20efea8fb8c/tool-results/brgghetua.txt"
}
```

```
1	=== amjad-2025-01
2	# 002013, Amjad et al. 2025
3	
4	Seven claims reproduced, one partially and five blocked on the dandiset,
5	plus one claim linking the dandiset to the paper's Zenodo deposit,
6	reproduced (trial lists agree for 99.8 to 100% of trials); both rounds
7	agreed with every outcome. The paper describes microinvasive probes for
8	recording dopamine and electrical activity in monkeys; the beta burst,
9	reward and unit isolation claims reproduce, the dopamine reward effect
10	weakly (p = 0.023, and not in the stored trial-aligned `da`).
11	
12	The dandiset was converted by CatalystNeuro (catalystneuro/schwerdt-lab-to-nwb,
13	the same conversion as 002014), and many findings are the same: each event
14	is stored about five times, once per overlapping trial window; trial
15	conditions are not in the trials table; the FSCV table columns carry no
16	units and the raw FSCV current is labelled amperes with values in the
17	thousands; the bipolar LFP is stored in volts with a conversion factor that
18	makes it picovolts; and the raw ephys of one session and the spike times of
19	Monkey P are on different clocks from the rest of the file, by 9831.35 s and
20	6800.666 s, with nothing saying so. In addition, one session's trial-aligned
[... 529 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/kaku-2025-01.yaml"
}
```

```
1	schema_version: 3
2	id: kaku-2025-01
3	datasets:
4	- archive: dandi
5	  id: 001619
6	  version: 0.251027.1953
7	  doi: 10.48324/dandi.001619/0.251027.1953
8	  relation: primary
9	paper: doi:10.1101/2025.01.27.635041
10	date: '2026-11-05'
11	entry: kaku-2025
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-14
20	  runner:
[... 809 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/kaku-2025-01.yaml",
 "offset": 830,
 "limit": 440
}
```

```
830	    outcome: blocked
831	    reason: No Phox2b mice and no fibre-site data.
832	    response: No change.
833	  - claim: ed10-site-classes
834	    agrees: true
835	    outcome: blocked
836	    reason: Same reason as fig3dfh.
837	    response: No change.
838	  - claim: fig4b-artificial-licking-keeps-lick-timing
839	    agrees: true
840	    outcome: blocked
841	    reason: The cued task with ALM photostimulation is absent.
842	    response: No change.
843	  - claim: fig4c-artificial-licking-breath-timing
844	    agrees: true
845	    outcome: blocked
846	    reason: Same reason as fig4b.
847	    response: No change.
848	  - claim: ed11b-alm-breathing-rate
849	    agrees: true
[... 414 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat tools/readme_row.py | head -80; grep -n "^| Dandiset\|^| Data" README.md | head
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
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
c=yaml.safe_load(open('claims/kaku-2025.yaml'))
for k,v in c.items():
    if k!='claims': print(k, str(v)[:3000])
for x in c['claims']:
    print(x['id'], x.get('kind'), x.get('data'), '|', x.get('figure') or x.get('location') or x.get('source'), '|', str(x.get('statement'))[:300])
print(list(c['claims'][0].keys()))
E
```

```
schema_version 2
dataset {'archive': 'dandi', 'id': '001619'}
paper doi:10.1101/2025.01.27.635041
checks [{'date': datetime.date(2026, 10, 21), 'kind': 'agent', 'model': 'claude-opus-5-5', 'ready': True, 'changes': ['Opening comment. Added the rule for readings. Readings of a method (V2 to V4, O1, O3, O6 to O9, named tests, regions, shuffles) must all give the outcome, else methods_underspecified (protocol, Reader step 3). "Under one reading" is kept only for readings of what a number counts (O4, O5, denominators, units of a test).', 'fig2-licking-breathing-tuned-counts, fig2-swallow-modulated-counts, fig2f-breathing-units-location, fig2h-swallow-units-location, ed7h-prebotc-exception, ed8bc-prebotc-inspiration-phase, ed8i-ipsilateral-lick-selectivity, fig3b-licking-units-in-premotor-regions, fig4d-simultaneous-recordings, fig4g-licking-breathing-pairs-correlated, fig4g-symmetric-lags, ed12c-correlation-without-licking, fig4h-fewer-correlations-outside-oscillator, fig5c-preemptive-breath-adjustment and fig5f-artificial-licking-late-breath-adjustment. Changed "under one reading" of method readings to "under every reading", by the rule above.', 'fig2-licking-breathing-tuned-counts. The 10% and 25% partial thresholds were attributed to the Methods, which say only that the proportions were robust; now named as a standard choice. Added readings (i) and (ii), since the text does not say whether 3551 and 1015 include the 182 units tuned to both.', 'ed1-unidirectional-models-fail and fig1k-rhythms-follow-swallow-at-fixed-latency. The statements said "so" where the paper says "suggest"; now "suggesting". ed1 also now names the fixed latency, the cycle count and the p >= 0.05 test as choices, since the paper gives none.', 'ed7-glm-separate-clusters. The criterion asked whether two sets assigned by largest weight "overlap", but such sets cannot overlap, and it set a posterior position the paper does not give. Rewritten from Extended Data Fig 7c-d (airflow weights around and be
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -c 6000 claims/kaku-2025.yaml; echo; python -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '001619' in json.dumps(x)[:200]: print(json.dumps(x,indent=1))
"
```

```
# Claims for Kaku, Liu et al. (2025), "A brainstem map of orofacial rhythms", bioRxiv
# doi:10.1101/2025.01.27.635041, on dandiset 001619.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the bioRxiv preprint, version 1 (posted January 27, 2025), as served on its web
# page, stored in paper/10.1101-2025.01.27.635041.txt: main text, legends of Figures 1 to 5,
# Methods and references, and the supplement "Extended Data Figures" (the legends of Extended
# Data Figures 1 to 12, from the supplement PDF, extracted to text). The display equations of
# the Methods (the circular Gaussian tuning curve and the VAF) are missing from the text; the
# words around them name every term. The Figure 5 legend stops at panel f, although the
# Results cite a Figure 5g. No later version was read. Data the dandiset description names: its
# title and description only (no data or file was looked at).
#
# Code read: github.com/NuoLiLabBCM/KakuEtAl2025 at commit fbc0abe (2026-06-18). The preprint
# says "Code used for analyses will be deposited upon publication"; this repository is the one
# the dandiset description names as "the corresponding analysis code", and its README points
# at the preprint v1 and at dandiset 001619. It holds process_mat.py (unit quality filter,
# trial filter, tongue and inspiration onsets, lick bouts, licking and breathing phase tuning
# and modulation index, the lick-to-breath and breath-to-lick timing analyses of Figs 1f-i and
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B2 -A20 '"001619"' targets/dandisets.json | head -60
```

```
6816-  },
6817-  {
6818:   "dandiset": "001619",
6819-   "name": "A brainstem map of orofacial rhythms",
6820-   "published_version": "0.251027.1953",
6821-   "asset_count": 335,
6822-   "size_gb": 130.08,
6823-   "data_standards": [
6824-    "Neurodata Without Borders (NWB)"
6825-   ],
6826-   "species": [
6827-    "Mus musculus - House mouse"
6828-   ],
6829-   "approaches": [
6830-    "behavioral approach",
6831-    "electrophysiological approach"
6832-   ],
6833-   "papers": [
6834-    {
6835-     "doi": "10.1101/2025.01.27.635041",
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 6838,6870p targets/dandisets.json; cd transcripts/kaku-2025; for f in author-report.md author-revise-1-report.md author-revise-2-report.md author-revise-3-report.md answer-report.md author-answers-report.md claims-report.md claims-check-report.md verifier-3-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (29.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/dc35d623-1a46-40f9-9af5-e20efea8fb8c/tool-results/bq30fhigt.txt

Preview (first 2KB):
     "resource_type": null,
     "preprint": true,
     "source": "description"
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "001632",
   "name": "Duration between rewards controls the rate of behavioral and dopaminergic learning",
   "published_version": null,
   "asset_count": 1222,
   "size_gb": 4.11,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
[... 30 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/dc35d623-1a46-40f9-9af5-e20efea8fb8c/tool-results/bq30fhigt.txt",
 "offset": 40
}
```

```
40	|---|---|
41	| Reproduced (16) | code-dataset-link, fig1i, ed1 (unidirectional models), fig1k, fig1l-lick-cycle-prolonged (33.36 ms against 33.3), fig1n-breath-interval-preserved (P = 0.26), fig1n-breath-cycle-prolonged (48.13 ms against 48.0), fig2f, fig2g, ed6e, ed8e, ed4c, fig4e (assumed), fig4f (assumed) |
42	| Partially reproduced (7) | units-count, region-spike-rates, fig1g, fig1f-licking-mode-switch, fig2 tuned counts, fig2h (assumed) |
43	| Not reproduced (8) | fig1d, fig1f-inspiration-between-licks, ed1bc, fig1l-lick-interval-preserved, fig2 swallow counts, ed8bc, fig4d |
44	| Blocked, data missing (15) | ed2 (rats), ed7g, ed7h, fig3b, fig3ce, fig3dfh, ed10, fig4b, fig4c, ed11b, fig5b, fig5c, fig5e, fig5f, ed12c |
45	| Blocked, other (4) | fig4g, fig4g lags, fig4h (under the claims file's own selection only 1 or 2 recordings qualify, not 43); fig3a (no pinned source for the premotor neurons) |
46	| Blocked, metadata insufficient (1) | ed8i (lick direction) |
47	| Blocked, too large (1) | ed7 (GLM, about 2.7 million fits) |
48	
49	The fig2 tuned counts match under the Methods' and the code's significance scheme: 3,517 / 1,021 / 177 against 3,551 / 1,015 / 182. Under the claims file's other reading, V3(b), they do not (2,757 / 602 / 69). The criterion asks for every reading, so the claim is partially reproduced.
50	
51	## 2. What was found about the dataset
52	- **Spike index:** in all 335 files `spike_times_index` holds where each unit starts, not where it ends, so pynwb gives every unit the previous unit's spikes. I read spikes by the per-trial count table instead.
53	- **Histology rows:** 19 files have more histology rows than units, so regions and CCF positions cannot be matched to units with certainty. The code and I take them by position.
54	- **Duplicates:** in all 162 two-probe sessions the airflow and tracking are the same recording deposited twice. I counted each once.
55	- **No session clock:** every trial starts at 0, so trials cannot be placed
[... 243 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/kaku-2025; head -c 1500 verifier-1-report.md; echo; echo ====; head -c 3000 verifier-2-report.md; grep -n -i "clock\|DL004\|DL020" verifier-1-report.md verifier-2-report.md | head
```

```
**Verification report, round 1: Kaku, Liu et al. 2025 (doi:10.1101/2025.01.27.635041) on DANDI:001619 v0.251027.1953**

The claims file has 48 claims. I checked the archive through the API. It holds 335 files, all `*_behavior+core.nwb`, and the draft version is the same. All 31 subjects are VGAT-ChR2-EYFP mice, and no other species or genotype appears. Notebook cell 5 shows the files have no cue or photostimulation times and no videos.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| code-dataset-link | reproduced | Every input exists. 20,109 units pass get_good_units, 0.9% below 20,300 (cell 13). |
| fig1d-lick-breath-frequencies | not_reproduced | Mean lick frequency is 26.96 Hz under (a) and 8.06 Hz under (b), against 6.23 ± 0.62. Breathing is within tolerance under (a). The value under (b) is distorted by the defect in B2. |
| fig1f-inspiration-between-licks | not_reproduced | Pooled, 30.4% of in-bout inspirations fall inside a protrusion; no session has none (cell 20). Unchecked alignment, B6. |
| fig1g-lick-delayed-before-slow-breath | partially_reproduced | Over sessions: +22.0 ms, p = 4.5e-4, n = 71. Only 16 of 20 mice are positive, and over mice p = 0.18 (cell 21). |
| fig1f-licking-mode-switch | not_reproduced | The inter-breath interval rises with lick count in 116 of 117 sessions. The latency from last lick to next inspiration differs by 62.5% across groups (133, 92, 82 ms); the limit is 20% (cell 22). |
| fig1i-breath-delayed-before-slow-lick | rep
====
**Verification report, round 2: Kaku, Liu et al. 2025 (doi:10.1101/2025.01.27.635041) on DANDI:001619 v0.251027.1953**

The claims file has 48 claims and the attempt record has 48 outcomes, with matching IDs:
- reproduced: 15
- partially reproduced: 4
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml;a=yaml.safe_load(open('attempts/kaku-2025-01.yaml'))
for v in a['verifications']: print(len(v['results']), sum(r['agrees'] for r in v['results']))
"
```

```
48 39
48 45
3 3
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/kaku-2025-01.md",
 "content": "# kaku-2025, Kaku et al. 2025\n\nTwelve claims reproduced, three partially, seven not reproduced and 23\nblocked, with one more blocked that also uses outside inputs,\n`fig3b-licking-units-in-premotor-regions`; the link claim `code-dataset-link`\nreproduced and `fig3a-premotor-regions` (`data: elsewhere`) is blocked, both\ncounted apart. The first verification round agreed with 39 of the 48 outcomes\nas they stood and the second with 45; the second's three disagreements were\nproposed as changes, so a third round reviewed those three and agreed with all\nof them. It pins version 0.251027.1953, the only published version; the paper\ncites none. The paper, Kaku, Liu et al., \"A brainstem map of orofacial\nrhythms\" (bioRxiv preprint, version 1), records Neuropixels units in the\nbrainstem and cerebellum of 31 VGAT-ChR2-EYFP mice in a multi-directional\nlicking task, with airflow and DeepLabCut tracking, and reports that licking\nand breathing are coupled in both directions, that swallowing interrupts both\nrhythms, maps of licking, breathing and swallowing units, a licking premotor\nnetwork that generates rhythm under photostimulation, and descending control\nof both rhythms at lick onset in a cued task. The claims were written from the\npreprint with its Extended Data legends and from the analysis code the dandiset\nnames (NuoLiLabBCM/KakuEtAl2025 at fbc0abe), which holds no statistical test;\nthe claims check corrected 17 claims and left three points open. Reproduced\nare, among others, the delay of breaths before slower licks (10.5 ms over\nsessions, p = 1.5e-9), the fixed latencies of both rhythms after a swallow,\nthe prolonged lick and breath cycles at a swallow (33.31 and 48.02 ms against\n33.3 and 48.0), the preserved inter-breath interval, the licking units in XII,\nV and IRN, the swallow latencies, the protrusion phase of licking units, the\nsorting control (2,366 units above 500 uV) and Figs 4e and 4f, where most of\nthe Fig 4e difference is an artefact of the slow half's later window\n(random-split null 47.5 to 54.7 ms). Partial are fig1d (licking 6.07 Hz and\nbreathing 4.19 Hz within one bout, the breathing bounds outside tolerance),\nfig1g (22.0 ms over sessions, p = 4.5e-4, but p = 0.18 over mice) and the\nlicking and breathing tuned counts (3,517, 1,023 and 178 under the code's test,\nnot under the other reading). Not reproduced are the unit counts (335\ninsertions against 339, pons 3,021 and medulla 8,992 below tolerance), the\nregion spike rates (vestibular nuclei 27.2 against 38 +- 3.8), inspiration\nbetween licks (30.4% of in-bout inspirations fall inside a protrusion), the\nlicking mode switch, the lick pause at swallows, the preserved inter-lick\ninterval (119.5 ms under the code's selection) and the swallow-modulated\ncounts. Of the blocked claims, 18 lack data, fig2f, fig2h and ed8bc are\n`methods_underspecified` because two readings of the preBotzinger region or of\nthe swallow normalisation disagree, ed7 (the GLM) is too large (about 12.6 CPU\nhours for one reading), ed8i lacks the axes of the 3D tracking, and fig3a and\nfig3b are `other`: the premotor coordinates are public as eLife 10:e67291\nFigure 5 source data 1, found after round 1 and not analysed. The author asked\na reader nothing at first, so the answer and author-answers runs changed\nnothing. Round 1 found that the within-bout reading of fig1d counted 13,498\nonset pairs lying in two bouts, that the later slow-half windows of Figs 1g\nand 4e give a positive difference with no effect, that the preBotzinger region\nwas built from 87 AMB-labelled units, that the airflow alignment was unchecked\nand that the GLM block had no cost estimate; in reply the regions were built\nfrom the Allen CCFv3 annotation, random-split nulls and a timed GLM fit were\nadded, three questions went to a reader in `questions/kaku-2025.yaml`, and\nnine outcomes changed. Round 2 found that the lags of DL029 to DL034, called\nsimilar, are later than the others', and recommended blocking fig2f and ed8bc\nbecause their two region readings disagree; round 3 agreed with those two and\nwith units-count moving from partially to not reproduced. The re-run for round\n2, on another runner, moved some numbers slightly and the random-split nulls\nmore, with no outcome changing, and took 70.8 minutes, over the 60-minute\nlimit, so the entry run reported a failure after the cell timeout was raised\nto 7200 s. The author's run took about 2 h 40 min (07:37 to 10:18 UTC), with a\n75-minute development extraction; the notebook ran in 42 min at first and in\n2,973 s at the end.\n\nThe dandiset holds only the multi-directional licking task (335 insertions,\nwhere the paper reports 339): the cued licking task, the ALM, latSC and\nbrainstem photostimulation experiments, the rat recordings, the raw videos used\nby the autoencoder and the premotor tracing data are not in it, the paper names\nno other deposit, and 18 of the 48 claims are blocked for missing data. In all\n335 files `units/spike_times_index` holds the offset where each unit's spikes\nstart, not where they end, so pynwb gives every unit the spikes of the unit\nbefore it; the per-trial spike counts agree with the start-offset reading. In\n19 files the histology table has more rows than the units (680 against 613 in\nDL034 session 20220205 probe p2), so regions and CCF positions are matched to\nunits by position. Every trial starts at 0, with spikes, tracking and airflow\nstored relative to it, so trials cannot be placed on one session clock and the\ninter-trial periods are absent. In every two-probe session (162) the airflow\nand DLC tracking of the two files are the same recording deposited twice; the\n3D tracking holds one trial fewer than the trial table in 211 files, the\nside-camera DLC rows differ from trials x 1471 in 25 files, and the 3D idx\nfield matches the DLC trial number in 154 of 173 sessions and the trial number\nminus one in 19. The 3D tracking has no stated axes, origin or units and the\ntrial tables no target position, so lick direction cannot be computed, and the\nleft/right hemisphere text puts 99.3% of units on the side opposite to the one\nccf_x gives, with the CCF axes not named. The subject age reads P210W to P303W\nin every file, and general/stimulus says 'photostim' though no file holds\nphotostimulation or cue data. In DL029 to DL034 the airflow-tongue\ncross-correlation peaks 20 to 30 ms later than in the other subjects (median\n103.7 against 78.2 ms) and fewer in-bout inspirations fall inside a protrusion,\nand the files do not say how the airflow and video clocks were aligned. The\nMethods list a drift metric < 0.5 and a 4-pole Butterworth filter, where the\ncode applies no drift filter and a 5th-order filter; the code's filter gives\n20,109 units, close to the paper's 20,300, and the drift metric 16,957.\nQuestions are put to the paper's authors: which test gives the significance of\nthe licking and breathing modulation index; how the swallow index is\nnormalised and swallow-only units defined; how units near the preBotzinger\ncomplex and in posterior-dorsal IRN/PARN were selected and which 43 recordings\nform Fig 4d; and whether the slow-minus-fast differences of Figs 1g and 4e were\ncompared with a random split or with equal windows.\n\nThe author's points on the protocol: the claims file's rule that disagreeing\nreadings block a claim conflicts with the step that lets the author adopt the\nbest-supported reading; a 130 GB dataset needs about 40 minutes for one pass,\nclose to the 60-minute limit, and nothing covers splitting notebooks or\ncaching; \"run on the whole dataset once\" did not fit, as a full development run\nwas needed; no block reason fits a claim not run in the time available, and\n`too_large` and `other` were used; a `data: elsewhere` claim with no identifier\ncannot be blocked as `data_missing`, so `other` was used; the clock check\nassumes a session timeline, and with trials starting at 0 each trial's spikes\nwere paired with the next trial's phases; and `archives.md` does not say that\nh5py's global lock stops threaded streaming.\n"
}
```

```
File created successfully at: docs/pilot-notes/kaku-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/kaku-2025-01.md",
 "content": "The paper's findings on licking and breathing held in part in this data, and its photostimulation, cued-task and paired-recording findings could not be tested, as the dandiset holds only the licking-task recordings. Breaths were delayed before slower licks, both rhythms resumed at fixed latencies after swallows, and licking units clustered in the hypoglossal and trigeminal nuclei and the IRN. Inspirations did not fall only between licks (30.4% came during a tongue protrusion), and the lick interval was not preserved across swallows. Licks were delayed before slower breaths over sessions but not over mice, and whether breathing units cluster near the preBötzinger complex could not be decided, as the paper does not define that region.\n"
}
```

```
File created successfully at: summaries/kaku-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/kaku-2025-01.md; grep -c "—\|rather" summaries/kaku-2025-01.md docs/pilot-notes/kaku-2025-01.md; git status --short
```

```
114 summaries/kaku-2025-01.md
summaries/kaku-2025-01.md:0
docs/pilot-notes/kaku-2025-01.md:0
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
?? docs/pilot-notes/kaku-2025-01.md
?? scripts
?? summaries/kaku-2025-01.md
```

**Agent**

The two new files are `docs/pilot-notes/kaku-2025-01.md` and `summaries/kaku-2025-01.md`. No other file was changed, and nothing is committed. The summary is four sentences and 114 words.

The `catalystneuro` field for 001619 is empty, so the findings paragraph does not open with the CatalystNeuro sentence.

The author's first-run report gives category totals that don't match the claims it lists: 16 reproduced, for example, but 14 claims named. I left the first run's counts out of the notes.

The dotfiles and `scripts` that show as untracked were there before this run. The author's report says so too, and I left them alone.

---

# kaku-2025, Kaku et al. 2025

Twelve claims reproduced, three partially, seven not reproduced and 23 blocked, with one more blocked that also uses outside inputs, `fig3b-licking-units-in-premotor-regions`; the link claim `code-dataset-link` reproduced and `fig3a-premotor-regions` (`data: elsewhere`) is blocked, both counted apart. The first verification round agreed with 39 of the 48 outcomes as they stood and the second with 45; the second's three disagreements were proposed as changes, so a third round reviewed those three and agreed with all of them. It pins version 0.251027.1953, the only published version; the paper cites none. The paper, Kaku, Liu et al., "A brainstem map of orofacial rhythms" (bioRxiv preprint, version 1), records Neuropixels units in the brainstem and cerebellum of 31 VGAT-ChR2-EYFP mice in a multi-directional licking task, with airflow and DeepLabCut tracking, and reports that licking and breathing are coupled in both directions, that swallowing interrupts both rhythms, maps of licking, breathing and swallowing units, a licking premotor network that generates rhythm under photostimulation, and descending control of both rhythms at lick onset in a cued task. The claims were written from the preprint with its Extended Data legends and from the analysis code the dandiset names (NuoLiLabBCM/KakuEtAl2025 at fbc0abe), which holds no statistical test; the claims check corrected 17 claims and left three points open. Reproduced are, among others, the delay of breaths before slower licks (10.5 ms over sessions, p = 1.5e-9), the fixed latencies of both rhythms after a swallow, the prolonged lick and breath cycles at a swallow (33.31 and 48.02 ms against 33.3 and 48.0), the preserved inter-breath interval, the licking units in XII, V and IRN, the swallow latencies, the protrusion phase of licking units, the sorting control (2,366 units above 500 uV) and Figs 4e and 4f, where most of the Fig 4e difference is an artefact of the slow half's later window (random-split null 47.5 to 54.7 ms). Partial are fig1d (licking 6.07 Hz and breathing 4.19 Hz within one bout, the breathing bounds outside tolerance), fig1g (22.0 ms over sessions, p = 4.5e-4, but p = 0.18 over mice) and the licking and breathing tuned counts (3,517, 1,023 and 178 under the code's test, not under the other reading). Not reproduced are the unit counts (335 insertions against 339, pons 3,021 and medulla 8,992 below tolerance), the region spike rates (vestibular nuclei 27.2 against 38 +- 3.8), inspiration between licks (30.4% of in-bout inspirations fall inside a protrusion), the licking mode switch, the lick pause at swallows, the preserved inter-lick interval (119.5 ms under the code's selection) and the swallow-modulated counts. Of the blocked claims, 18 lack data, fig2f, fig2h and ed8bc are `methods_underspecified` because two readings of the preBotzinger region or of the swallow normalisation disagree, ed7 (the GLM) is too large (about 12.6 CPU hours for one reading), ed8i lacks the axes of the 3D tracking, and fig3a and fig3b are `other`: the premotor coordinates are public as eLife 10:e67291 Figure 5 source data 1, found after round 1 and not analysed. The author asked a reader nothing at first, so the answer and author-answers runs changed nothing. Round 1 found that the within-bout reading of fig1d counted 13,498 onset pairs lying in two bouts, that the later slow-half windows of Figs 1g and 4e give a positive difference with no effect, that the preBotzinger region was built from 87 AMB-labelled units, that the airflow alignment was unchecked and that the GLM block had no cost estimate; in reply the regions were built from the Allen CCFv3 annotation, random-split nulls and a timed GLM fit were added, three questions went to a reader in `questions/kaku-2025.yaml`, and nine outcomes changed. Round 2 found that the lags of DL029 to DL034, called similar, are later than the others', and recommended blocking fig2f and ed8bc because their two region readings disagree; round 3 agreed with those two and with units-count moving from partially to not reproduced. The re-run for round 2, on another runner, moved some numbers slightly and the random-split nulls more, with no outcome changing, and took 70.8 minutes, over the 60-minute limit, so the entry run reported a failure after the cell timeout was raised to 7200 s. The author's run took about 2 h 40 min (07:37 to 10:18 UTC), with a 75-minute development extraction; the notebook ran in 42 min at first and in 2,973 s at the end.

The dandiset holds only the multi-directional licking task (335 insertions, where the paper reports 339): the cued licking task, the ALM, latSC and brainstem photostimulation experiments, the rat recordings, the raw videos used by the autoencoder and the premotor tracing data are not in it, the paper names no other deposit, and 18 of the 48 claims are blocked for missing data. In all 335 files `units/spike_times_index` holds the offset where each unit's spikes start, not where they end, so pynwb gives every unit the spikes of the unit before it; the per-trial spike counts agree with the start-offset reading. In 19 files the histology table has more rows than the units (680 against 613 in DL034 session 20220205 probe p2), so regions and CCF positions are matched to units by position. Every trial starts at 0, with spikes, tracking and airflow stored relative to it, so trials cannot be placed on one session clock and the inter-trial periods are absent. In every two-probe session (162) the airflow and DLC tracking of the two files are the same recording deposited twice; the 3D tracking holds one trial fewer than the trial table in 211 files, the side-camera DLC rows differ from trials x 1471 in 25 files, and the 3D idx field matches the DLC trial number in 154 of 173 sessions and the trial number minus one in 19. The 3D tracking has no stated axes, origin or units and the trial tables no target position, so lick direction cannot be computed, and the left/right hemisphere text puts 99.3% of units on the side opposite to the one ccf_x gives, with the CCF axes not named. The subject age reads P210W to P303W in every file, and general/stimulus says 'photostim' though no file holds photostimulation or cue data. In DL029 to DL034 the airflow-tongue cross-correlation peaks 20 to 30 ms later than in the other subjects (median 103.7 against 78.2 ms) and fewer in-bout inspirations fall inside a protrusion, and the files do not say how the airflow and video clocks were aligned. The Methods list a drift metric < 0.5 and a 4-pole Butterworth filter, where the code applies no drift filter and a 5th-order filter; the code's filter gives 20,109 units, close to the paper's 20,300, and the drift metric 16,957. Questions are put to the paper's authors: which test gives the significance of the licking and breathing modulation index; how the swallow index is normalised and swallow-only units defined; how units near the preBotzinger complex and in posterior-dorsal IRN/PARN were selected and which 43 recordings form Fig 4d; and whether the slow-minus-fast differences of Figs 1g and 4e were compared with a random split or with equal windows.

The author's points on the protocol: the claims file's rule that disagreeing readings block a claim conflicts with the step that lets the author adopt the best-supported reading; a 130 GB dataset needs about 40 minutes for one pass, close to the 60-minute limit, and nothing covers splitting notebooks or caching; "run on the whole dataset once" did not fit, as a full development run was needed; no block reason fits a claim not run in the time available, and `too_large` and `other` were used; a `data: elsewhere` claim with no identifier cannot be blocked as `data_missing`, so `other` was used; the clock check assumes a session timeline, and with trials starting at 0 each trial's spikes were paired with the next trial's phases; and `archives.md` does not say that h5py's global lock stops threaded streaming.

---

The paper's findings on licking and breathing held in part in this data, and its photostimulation, cued-task and paired-recording findings could not be tested, as the dandiset holds only the licking-task recordings. Breaths were delayed before slower licks, both rhythms resumed at fixed latencies after swallows, and licking units clustered in the hypoglossal and trigeminal nuclei and the IRN. Inspirations did not fall only between licks (30.4% came during a tongue protrusion), and the lick interval was not preserved across swallows. Licks were delayed before slower breaths over sessions but not over mice, and whether breathing units cluster near the preBötzinger complex could not be decided, as the paper does not define that region.

## End of run

17 turns, 2 minutes, $1.29 at API prices, result: success.
