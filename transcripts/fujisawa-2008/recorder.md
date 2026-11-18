# fujisawa-2008 · recorder · run 43829976980

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/fujisawa-2008/; python tools/readme_row.py fujisawa-2008; ls docs/pilot-notes | head -50; ls summaries | head
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/ashworth-2025-01.md
000067
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
claims-check-report.md
claims-check.md
claims-report.md
claims.md
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -m3 -B2 "^| \[0" README.md | head -5; for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 ashworth-2025-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; cat docs/pilot-notes/knierim-2000-02.md | head -3; ls docs/pilot-notes | grep fujisawa; ls attempts | grep fujisawa; cat summaries/asari-2009-01.md summaries/amjad-2025-01.md
```

```
<persisted-output>
Output too large (38.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/390c5410-d179-4481-af71-34c95d118834/tool-results/baedlvr7u.txt

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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/390c5410-d179-4481-af71-34c95d118834/tool-results/baedlvr7u.txt"
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
[... 521 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -5 docs/pilot-notes/knierim-2000-02.md; echo; cat docs/pilot-notes/fujisawa-2008-0*.md; ls summaries | grep -E "fujisawa|knierim"; cat docs/pilot-notes/README.md | head -60
```

```
# 001754 again, on the fixed draft (2026-10-15)

The first repeat attempt, under the rules added for it (docs/agents/author-again.md).
The conversion was redone (`mcnaughton2000-to-nwb` at commit `7346882`) and
the draft re-uploaded on 2026-10-14, and the attempt pins `draft`. Three

# 000067, Fujisawa et al. 2008

No claims reproduced, five partially, seven not reproduced and four blocked,
all on the dandiset. Round 1 gave its own outcome for each claim from the
notebook with its conclusions removed and agreed with all 16. The author then
changed `fig4-position-dependence` from not reproduced to blocked as
`methods_underspecified`, because the calibration the verifier asked for
showed that the criterion's test flags 30.0% and 75.0% of synthetic pairs
with constant efficacy, and wrote a criterion for `traj-diverge` that moved
it from blocked to partially reproduced; round 2 disagreed with that change,
the author proposed blocked as `data_missing`, and a third round agreed. The
paper reports the firing of neurons in the medial prefrontal cortex of rats
during an odor-place matching task on a maze, and the monosynaptic
connections between them. The channel map, the counts of rats and units, the
[... 187 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -m2 "^| Data" README.md; grep -n -m1 "^| Dandiset\|^| Dataset" README.md; cat tools/readme_row.py | head -80; cat attempts/fujisawa-2008-03.yaml
```

```
<persisted-output>
Output too large (82.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/390c5410-d179-4481-af71-34c95d118834/tool-results/bwadqo0lr.txt

Preview (first 2KB):
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
[... 39 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c attempts/fujisawa-2008-03.yaml claims/fujisawa-2008.yaml transcripts/fujisawa-2008/*-report.md; python -c "import json;d=json.load(open('targets/dandisets.json'));print(type(d))"; grep -n -A15 '"000067"' targets/dandisets.json | head -30
```

```
81457 attempts/fujisawa-2008-03.yaml
 62539 claims/fujisawa-2008.yaml
  1243 transcripts/fujisawa-2008/answer-report.md
  1896 transcripts/fujisawa-2008/author-answers-report.md
  6745 transcripts/fujisawa-2008/author-report.md
  4100 transcripts/fujisawa-2008/author-revise-1-report.md
  3435 transcripts/fujisawa-2008/author-revise-2-report.md
  3111 transcripts/fujisawa-2008/claims-check-report.md
  4617 transcripts/fujisawa-2008/claims-report.md
  5101 transcripts/fujisawa-2008/reconcile-report.md
 12143 transcripts/fujisawa-2008/verifier-1-report.md
  6745 transcripts/fujisawa-2008/verifier-2-report.md
193132 total
<class 'dict'>
902:   "dandiset": "000067",
903-   "name": "Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex",
904-   "published_version": "0.261106.2004",
905-   "asset_count": 31,
906-   "size_gb": 126.14,
907-   "data_standards": [
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 917,940p targets/dandisets.json; cat attempts/fujisawa-2008-03.yaml | head -400
```

```
"papers": [
    {
     "doi": "10.1038/nn.2134",
     "title": "Behavior-dependent short-term assembly dynamics in the medial prefrontal cortex",
     "relation": "IsDescribedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": [
    "conversion code at https://github.com/catalystneuro/buzsaki-lab-to-nwb",
    "contributor Baker, Cody of CatalystNeuro"
   ]
  },
  {
   "dandiset": "000070",
   "name": "Neural population dynamics during reaching",
   "published_version": "0.260528.0919",
   "asset_count": 10,
   "size_gb": 53.34,
[... 404 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 400,900p attempts/fujisawa-2008-03.yaml
```

```
<persisted-output>
Output too large (31.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/390c5410-d179-4481-af71-34c95d118834/tool-results/bh3f2uooz.txt

Preview (first 2KB):
  assumed: true
  notebook: reproduce_fujisawa_2008.ipynb
  output: claim:fig4-position-dependence
  measured: 6.4
  notes: Of 472 excitatory connections (B-a, W-a), trials (a) 30 (6.4%) show position-dependent excess coincidences under
    both (i) and (ii); trials (b) 34 (7.2%) and 33 (7.0%). All are below 19.5 +/- 1.95% and above the null rates (2% for
    (a), binomial p = 4.9e-08; 1% for (b), p = 1.2e-18). Most come from EE.188 (8 of 119) and EE.196 (12 of 84).
  deviations:
  - M = 5,000 jitter surrogates (an assumption; the section gives no number); with 1,000 the global band at level 0.01 cannot
    be broken in 17 of 23 connections checked, as the discrete stepping procedure settles on the outermost band.
  - Coincident events are placed at the presynaptic spike, a standard choice.
- claim: fig5a-session-selective-connections
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_fujisawa_2008.ipynb
  output: claim:fig5a-session-selective-connections
[... 21 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/390c5410-d179-4481-af71-34c95d118834/tool-results/bh3f2uooz.txt",
 "offset": 25
}
```

```
25	  - As fig4-position-dependence (M = 5,000).
26	- claim: fig4-pair-156-136
27	  outcome: not_reproduced
28	  assumed: true
29	  notebook: reproduce_fujisawa_2008.ipynb
30	  output: claim:fig4-pair-156-136
31	  measured:
32	  - 0.34
33	  - 0.64
34	  notes: Cells 156 and 136 of EE.188 are on shanks 5 and 4 (different, as Figure 4a) and connected (excitatory here and
35	    in the lab's list). On left trials the only significant region runs from 0.34 to 0.64 (58 coincident events); the end
36	    is within 0.6 +/- 0.06, the start outside 0.4 +/- 0.04. Cell 156's left-trial rate between 0.2 and 0.5 varies by 49%
37	    of its maximum, cell 136's by 61%, so 136 is not steady by the criterion. With jitter of the presynaptic cell only the
38	    region is 0.35 to 0.64. The lab's example file labels 136 as unknown, not as an interneuron.
39	  deviations:
40	  - As fig4-position-dependence (M = 5,000). Cell numbers are the CRCNS numbers, which the example file shares with the
41	    paper's figures (pair 156-136 on shanks 5 and 4, as Figure 4a).
42	- claim: fig5b-example-pairs
43	  outcome: not_reproduced
44	  assumed: true
[... 458 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/390c5410-d179-4481-af71-34c95d118834/tool-results/bh3f2uooz.txt",
 "offset": 501
}
```

```
501	  - claim: fig6b-convergent-examples
502
```

**Agent calls Bash**

```bash
cd  sed -n 900,2000p attempts/fujisawa-2008-03.yaml
```

```
- claim: fig6b-convergent-examples
    agrees: true
    outcome: partially_reproduced
    reason: 'By the literal criterion: 197 has first > later, but p >= 0.26. 186 has later > first with p = 0.064 or 0.034
      (cell 75). The sign for 197 carries no information (B3).'
    response: With the shared jitter and the tail labelling, 186 is facilitating and significant under three readings (p
      = 0.016 to 0.060) and 197 depressing under one reading, not significantly (p = 0.875); the literal sign is printed
      too. Partial under both labellings; outcome unchanged.
  - claim: fig7-supralinear
    agrees: true
    outcome: not_reproduced
    reason: S-b gives 14 satellites, but the excess over linear at 5 ms is negative in every reading (cell 77).
    response: No change.
- date: '2026-11-16'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: 'The full executed notebook of the first revision, with its conclusions and summary, the README, the helper
    module, the claims file and the attempt record, with the paper''s full text under paper/. Its general points not tied
    to one claim: findings with no printed output behind them (the NWB cell_type and lab_cell_number columns, DANDI''s use
    of EE.188''s 105-cell list, cells 32 and 72 coded interneurons and presynaptic in pairs_all), and the finding that spike
[... 339 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/fujisawa-2008; for f in author-report answer-report author-answers-report verifier-1-report; do echo "=== $f"; cat $f.md; done
```

```
=== author-report
I've finished the attempt. All 33 claims were run on both datasets except `task-performance`, which is blocked: 4 reproduced, 1 reproduced resting on an assumption, 12 partially reproduced, 15 not reproduced. The entry is in `entries/fujisawa-2008/`, the record is `attempts/fujisawa-2008-03.yaml`, and `entry.py check` reports 0 errors. The run passed in 29 min with 9.0 GB peak memory, and the handover package is built. Nothing is committed. I did not come across any earlier attempt's results.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| channel-region-link | not reproduced |
| rats-and-units | partially reproduced |
| task-performance | blocked (data_missing) |
| fig2-population-uniform | not reproduced |
| fig2c-active-fraction | partially reproduced |
| fig2-field-size | reproduced |
| population-vector-width | not reproduced (assumed) |
| fig2d-layer-rates | partially reproduced |
| fig2e-layer-discrimination | not reproduced |
| traj-diverge | partially reproduced (assumed) |
| side-arm-selectivity-by-layer | partially reproduced |
| central-arm-selectivity | partially reproduced |
| odor-nosepoke | not reproduced |
[... 190 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/fujisawa-2008; for f in author-revise-1-report verifier-2-report author-revise-2-report reconcile-report; do echo "=== $f"; cat $f.md; done
```

```
=== author-revise-1-report
I've worked through every point in the round-1 report and re-run the entry. The final run passed in 42 min with 10.0 GB peak memory, and `entry.py check` reports 0 errors. Nothing is committed.

## Outcomes
- **population-vector-width** changed from not reproduced to **partially reproduced**, still marked as resting on an assumption. This is the verifier's outcome. With each neuron's rate normalised to its peak, layer 5 is within tolerance and layer 2/3 is 0.268 against a limit of 0.267.
- **central-arm-selectivity** stays partially reproduced but is now marked as resting on the unit list. If every NWB unit is counted, both values fall within tolerance under one rat reading.
- **fig2c-active-fraction** stays partially reproduced. The verifier says not reproduced; I kept partial because one of the two values, the layer difference and the constancy hold. The disagreement is recorded under `verifications`.
- **No other outcome changed.** The new outcomes are 5 reproduced, 12 partially reproduced, 15 not reproduced and 1 blocked; 8 rest on an assumption.

## Fixes and added output, by report point
- **B1, unit lists.** I compared the lab's cell lists with `spikeph` and the NWB units. The files have no "Cells" variable. The lab's lists look like the description's 1 Hz list: 98.9% of listed units reach 1 Hz in the trials, against 28.7% of those left out. I kept them as the paper's units, stated as an assumption, because they total 627 against the paper's 633, while every NWB unit totals 1,373. That larger list is now run as a variant for the unit-count, fraction, active-fraction and rate claims. No rat has 222 units and no session has 142 units in either list. A new finding records that the lab's lists are undocumented.
- **B2, peak positions.** Peaks now use both rate readings. Results are unchanged.
- **B3 and B4, facilitation and depression.**
  - The test now jitters both cells with 1,000 surrogates, as the claims file says.
  - A pair is ca
[... 143 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -1 docs/pilot-notes/churchland-2010-0*.md docs/pilot-notes/knierim-2000-0*.md docs/pilot-notes/chen-2026-02.md; grep -l "again\|repeat\|third attempt" docs/pilot-notes/*.md | head; grep -rn "^# .*again\|^# .*attempt" docs/pilot-notes/ | head
```

```
==> docs/pilot-notes/churchland-2010-01.md <==
# 000128, Churchland et al. 2010

==> docs/pilot-notes/churchland-2010-02.md <==
# 000138, Churchland et al. 2010

==> docs/pilot-notes/churchland-2010-03.md <==
# 000139, Churchland et al. 2010

==> docs/pilot-notes/churchland-2010-04.md <==
# 000140, Churchland et al. 2010

==> docs/pilot-notes/knierim-2000-01.md <==
# 001754, Knierim, McNaughton and Poe 2000

==> docs/pilot-notes/knierim-2000-02.md <==
# 001754 again, on the fixed draft (2026-10-15)

==> docs/pilot-notes/knierim-2000-03.md <==
# 001754, Knierim et al. 2000, third attempt
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -20 docs/pilot-notes/park-2019-02.md; echo; head -40 claims/fujisawa-2008.yaml; grep -nE "^  - id:|^- id:|^    statement:|figure|^    source" claims/fujisawa-2008.yaml | head -150
```

```
# park-2019, Park et al. 2019, second attempt

Nine claims reproduced (five on an assumption), five partially (one on an
assumption), three not reproduced (two on an assumption) and five blocked for
missing data. Round 1 agreed with 21 of the 22 outcomes as they stood, and
`fig4c-arena-registration-short-lived` moved from partially to not reproduced
as it proposed; round 2 agreed with 19 as they stood and asked that
`fig1d-instability`, `figs3-no-head-direction-bias` and fig4c state the
readings they rest on, which was done with no change of outcome, so there was
no third round. CRCNS hc-20 has no versions, so the record pins `unversioned`
and the notebook checks the MD5 of data.zip. The paper, Park, Keeley, Savin,
Ranck and Fenton in Neuron, records head-direction cells in the medial
entorhinal cortex (MEC) of rats doing place avoidance in a stable, a rotating
(arena at 1 rpm) and a second stable trial, and reports that directional
tuning degrades during rotation, alternating between the room and arena frames
with the rat's proximity to the two shock zones, while the temporal coupling of
cell pairs and their internally referenced tuning are preserved. The dataset
holds the 115 head-direction cells and their 30 Hz tracks; the learning
curves, the LFP and the claims on all MEC cells and the Gaussian process model
(Figures S4 to S6) are blocked. Reproduced are `hd-cell-rate` (1.392 AP/s
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 40,130p claims/fujisawa-2008.yaml; grep -nE "^  (location|source|where|figure|section):" claims/fujisawa-2008.yaml | head -50; sed -n 990,1030p claims/fujisawa-2008.yaml
```

```
# of 142 neurons (Figure 2a legend, "in two rats").
#
# Rats and layers (open). The datasets name three rats EE, FF and GG; the paper names four, E to
# H, and never links its names to the files. Readings: R-a, the datasets' EE, FF and GG are the
# paper's rats E, F and G, so FF is the layer 5 rat and layer 2/3 rat H is not in the data; R-b,
# the names are not linked, each dataset rat may be either layer, with at most one in layer 5.
# Every claim with values by layer is run under both.
#
# Shared method, from the Methods unless stated.
# - Trials and positions. A trial runs from the end of nose poking (position 0; Supplementary
#   Figure 6 legend, "The onset of the maze trial is defined as the end of nose-poking") to the
#   reward area (position 1; Results, Figure 1b). Where in the reward area position 1 is set is
#   not said (open; readings E-a the arrival at the end of the goal arm, E-b the start of reward
#   consumption), nor which poke ends nose poking when a rat pokes more than once (open; readings
#   N-a the last poke before leaving the start box, N-b the first). Whether error trials enter
#   any analysis is not said (open; readings T-a correct trials only, T-b all trials).
# - Firing-rate differences (LEFT against RIGHT, or any two trial labels). Spikes are placed at
#   the normalised position where they occur; the PSTH per condition is the sum of Gaussian
#   kernels (bandwidth 0.05 normalised length) over the condition's spikes divided by its number
#   of trials. Statistic D0(x) = left PSTH minus right PSTH. Labels are permuted M times;
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
r=yaml.safe_load(open('attempts/fujisawa-2008-03.yaml'))
from collections import Counter
print(Counter((o['outcome'],bool(o.get('assumed'))) for o in r['outcomes']))
print(len(r['findings']))
E
ls questions/ | grep fujisawa; git log --oneline -3 -- questions/fujisawa-2008.yaml
```

```
Counter({('not_reproduced', False): 12, ('partially_reproduced', False): 7, ('partially_reproduced', True): 5, ('reproduced', False): 4, ('not_reproduced', True): 3, ('blocked', False): 1, ('reproduced', True): 1})
22
fujisawa-2008.yaml
49e6b63 Merge main into attempt/fujisawa-2008
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/fujisawa-2008-03.md",
 "content": "# fujisawa-2008, Fujisawa et al. 2008, third attempt\n\nFive claims reproduced (one on an assumption), 12 partially (five on an\nassumption), 14 not reproduced (three on an assumption) and one blocked for\nmissing data, plus the link claim `channel-region-link`, not reproduced, as\nthe CRCNS channel map does not fit the nose-poke sensors of rat GG. The first\nverification round agreed with 31 of the 33 outcomes as they stood and the\nsecond with all 33; nothing was proposed after the second, so there was no\nthird round. It is the first attempt on both datasets, under the pilot-14 rule\nthat records are filed by paper, with one claims file of 33 claims that\nreplaces the two per-dataset files of fujisawa-2008-01 (DANDI:000067) and\nfujisawa-2008-02 (CRCNS pfc-2). DANDI:000067 is pinned at 0.261106.2004, the\nmost recent published version, which the paper does not cite; CRCNS pfc-2 is\nunversioned, with the MD5 sums printed in the notebook. The paper, Fujisawa,\nAmarasingham, Harrison and Buzsaki in Nature Neuroscience (11, 823-833),\nrecords units with one 8-shank, 64-site silicon probe per rat in anterior\ncingulate and dorsal prelimbic cortex of four rats in an odor-based delayed\nmatching-to-sample task on a figure-eight T-maze, three in layer 2/3 and one\nin layer 5, and reports trajectory-specific firing along the maze, putative\nmonosynaptic connections found from cross-correlograms with a jitter test,\ntransmission that depends on the rat's position, depression and facilitation\nwith spike repetition, and a supralinear effect of coincident inputs. The\nclaims were written from the version of record and its supplement, opening\nthe PDF pages only for figures the text garbles; the paper links no analysis\ncode. Spike times were taken from the NWB files, matched to the lab's cells by\nshank and cluster, and trials, positions and cell lists from CRCNS, with\n`EE188_example.mat`, the paper's 117-cell session, streamed from inside\n`EE.188.tar.gz`. Reproduced are `fig2-field-size` (0.241 +/- 0.169),\n`retrospective-coding-rare` (4.3% of EE.188 cells), `speed-not-correlated`\n(median -0.022), `no-spatial-clustering` (in the layer 2/3 session only) and\n`thinning-preserves-dependence` (7 of 34 pairs, on M = 5,000 surrogates).\nPartial are, among others, `rats-and-units` (627 units in three rats, within\n633 +/- 63.3, but no rat holds 222), `side-arm-selectivity-by-layer` (61.0% and\n52.6% against 40% and 22%, layer 5 higher at p = 0.046), `central-arm-selectivity`\n(30.4% and 29.5% against 16% and 18%), `traj-diverge` (the path at 0.30, head\ndirection from 0.02), `fig4-position-dependence` (6.4% against 19.5%, above\nthe null rates) and `population-vector-width` (layer 2/3 0.282 against the\nlimit 0.267 with peak-normalised rates; z-scored rates would reproduce it).\nNot reproduced are, among others, `fig3-connection-rates` (1.449% connected and\n1.173% excitatory, the excitatory rate 1.6 to 2.1 times the paper's),\n`fig3-cell-classes` (23 interneurons, 3.7%), `fig3d-hub` (86 of 117 cells\nagainst 39), `fig3b-session-connections`, `fig5a-session-selective-connections`,\n`fig6-facilitation-depression` (facilitation above the 5% null level and\ndepression in no combination, under either labelling) and `fig7-supralinear`\n(transmission below the linear prediction in every satellite). The outcomes of\n`rats-and-units` and `central-arm-selectivity` rest on taking the lab's cell\nlists as the paper's units: with every NWB mPFC unit (1,373) the first would be\nnot reproduced and the second would have both values within tolerance under\none rat reading. Round 1 disagreed on `fig2c-active-fraction`, which it gave\nas not reproduced, and on `population-vector-width`, which moved to partially\nreproduced as it proposed, and asked for the NWB unit variant, peaks under both\nrate readings, the shared jitter and a tail labelling in the facilitation and\ndepression test, a check of head direction and the one-cell jitter, all done;\na question on the claims file's literal \"first above later\" went to a reader\nin `questions/fujisawa-2008.yaml`, written after the answer run, so it is\nunanswered. Round 2 agreed with all 33, withdrew its fig2c disagreement and\nasked that `rats-and-units` be marked assumed and that the literal labelling be\nrun with the shared jitter, which gives the same outcome; it also found\nsentences the outputs did not support, which were corrected, though one unit\nvariant moves by one unit between the verifier's copy and the author's runs of\nthe same seeded code (409 against 408 of 1,211), a cause not confirmed. The\nreconciliation with fujisawa-2008-02, run blind, finds all 12 of its findings\nstill present and 7 of the 19 shared claims with a changed outcome, three from\npartial outcomes the merged claims file adds, two from differences in method\n(`task-performance` was tested there from the sensor channels of one session),\none from a different way of building the rate curves and one,\n`fig4-pair-156-136`, graded differently on nearly the same numbers. The\nauthor's run took about 3 h 36 min; two full runs failed, one on a variable\nname reused across cells and one on an array reshape, both fixed, and peak\nmemory was brought from 12.1 to 9.0 GB with identical results. The notebook\nran in 29 min at first, 42 min after round 1, 40 min after round 2 and 2117 s\nafter the reconciliation, whose own notebook ran in 108 s.\n\nThe dataset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb).\nOnly correct trials are listed, in SessionNP, the whl trial numbers and the NWB\ntrials tables, so task performance and any analysis of error trials cannot be\nmade from either dataset. Neither dataset gives the layer of each rat's probe\nor links the rats EE, FF and GG to the paper's E to H, no rat holds the paper's\n222 layer 5 units and no session the 142 cells of the layer 5 session of\nFigure 2a and Supplementary Figure 11. The CRCNS description documents a 1 Hz\n'Cells' list that the files do not hold and does not describe CellsInfo, the\nper-session cell list (627 units with EE.188's example file, against 1,373\nsorted mPFC units); CellsInfo is consistent with the 1 Hz rule (98.9% of listed\nunits reach 1 Hz in the trials, 28.7% of those left out), and neither dataset\nmarks the paper's well-isolated units. In 11 of 13 working memory sessions of\nDANDI:000067 every unit has cell_type 'not classified in the source' and\nlab_cell_number -1, so the NWB units can be linked to the lab's cells only\nthrough shank and cluster_id, and then their spike times are identical for 615\nof the 627 used. The EE.088 file has no wideband signal, and EE.188 and EE.210\nhave no trials table or linearised position, though CRCNS holds them. In the\nthree GG sessions channels 97 and 98, the nose-poke sensors in the CRCNS\ndescription, carry no poke signal, nor does any channel from 97 to 101, which\nthe NWB files label 'neural'; the FF files have 104 channels labelled as rat\nEE's layout, where the description gives FF 101. The two CRCNS lists of\nEE.188's cells disagree (105 cells, 87 pyramidal and 18 interneurons, against\n117, 33 pyramidal, 15 interneurons and 69 unknown, with types agreeing for 42\nof the 105 common cells), and DANDI:000067 uses the 105-cell list; the example\nfile codes cells 32 and 72 as interneurons, though Figure 7a names them\npresynaptic pyramidal cells, and cell 136, the interneuron of Figure 4, as\nunknown. Its pairs_all list holds 43 connections, against the paper's 48 and\n30 for the session, and its largest component is the 39-cell circuit of Figure\n3d; which selection it is, is not said. Ten of the 13 sessions track a single\nLED, so head direction exists only for EE.152, EE.165 and EE.188. The\nlinearised position is nonzero through each trial's nose poke, and the spikes'\ntrial labels and positions start at the first nose-poke while the description\ndefines the trial start as the end of the last (269071 of 676892 labelled\nspikes fall between the two). `EE188_example.mat` is not in folder EE0708 or\nin filelist.txt but is member 62 of 75 of EE.188.tar.gz, 1.99 GB into the 2.41\nGB gzip stream. The trial table of EE.188 leaves out 3 trials that the sensor\nchannels and the position file show as correct and 1 error trial. Questions\nare put to the paper's authors: how the rates enter the population vectors,\nhow many permutations or jitter surrogates each test used, how Figure 7\ndefines coincident events and the transmission window, which rat is layer 5\nand which units make the 633, whether the global band of the jitter test was\nthe minimal band or 1% on each side and whether the cross-correlograms were\nbinned at 1 or 0.5 ms (1.449% and 1.091% of directed pairs connected here,\nagainst 0.79%), and how the connections of Figure 3d were chosen.\n\nThe author's points on the protocol: the claims file says the number of\npermutations should not change the outcome, but at level 0.01 it does, so more\nwere used and the claims marked assumed; no rule says how to combine two\ndatasets for one claim, and spikes were taken from DANDI and trials and cell\nlists from CRCNS; `entry.py check` asks for an `inputs` entry for a\n`with_labels` claim even when the labels come from the dataset's own\ndescription; the `fig2c-active-fraction` criterion defines only reproduced,\nand partial was used; the data fix some of the claims file's open readings,\nrecorded as a deviation; small members were cached on disk during\ndevelopment, against \"do not download to disk\", and deleted afterwards; and\nthe blinded checkout still held the old per-dataset claims files and reader\ntranscripts, which were not read.\n"
}
```

```
File created successfully at: docs/pilot-notes/fujisawa-2008-03.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/fujisawa-2008-03.md",
 "old_string": "partial outcomes the merged claims file adds, two from differences in method\n(`task-performance` was tested there from the sensor channels of one session),\none from a different way of building the rate curves and one,",
 "new_string": "partial outcomes the merged claims file adds, three from differences in\nmethod (`task-performance` was tested there from the sensor channels of one\nsession, and `population-vector-width` used rate curves built differently) and\none,"
}
```

```
The file docs/pilot-notes/fujisawa-2008-03.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/fujisawa-2008-03.md",
 "old_string": "`fig6-facilitation-depression` (facilitation above the 5% null level and\ndepression in no combination, under either labelling)",
 "new_string": "`fig6-facilitation-depression` (no combination with both fractions above 5%,\nunder either labelling)"
}
```

```
The file docs/pilot-notes/fujisawa-2008-03.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/fujisawa-2008-03.md",
 "content": "In this data the paper's trajectory-specific firing held in part: many prefrontal neurons fire differently on left and right trials, but in larger fractions than reported. Its monosynaptic connection results did not reproduce, as the jitter test here found far more excitatory connections and far fewer interneurons, with a bin width and test band the paper does not give. Position-dependent transmission was above chance but in 6.4% of connections against 19.5%, and the split into depressing and facilitating connections and the supralinear effect of coincident inputs did not reproduce. Task performance could not be tested, as only correct trials are deposited. Smaller results on field size, retrospective coding, running speed and spatial clustering reproduced.\n"
}
```

```
File created successfully at: summaries/fujisawa-2008-03.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/fujisawa-2008-03.md docs/pilot-notes/fujisawa-2008-03.md; grep -nE "—|rather|\*\*" summaries/fujisawa-2008-03.md docs/pilot-notes/fujisawa-2008-03.md; git status --short
```

```
114 summaries/fujisawa-2008-03.md
 1525 docs/pilot-notes/fujisawa-2008-03.md
 1639 total
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
?? docs/pilot-notes/fujisawa-2008-03.md
?? scripts
?? summaries/fujisawa-2008-03.md
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes/fujisawa-2008-03.md"
}
```

```
1	# fujisawa-2008, Fujisawa et al. 2008, third attempt
2	
3	Five claims reproduced (one on an assumption), 12 partially (five on an
4	assumption), 14 not reproduced (three on an assumption) and one blocked for
5	missing data, plus the link claim `channel-region-link`, not reproduced, as
6	the CRCNS channel map does not fit the nose-poke sensors of rat GG. The first
7	verification round agreed with 31 of the 33 outcomes as they stood and the
8	second with all 33; nothing was proposed after the second, so there was no
9	third round. It is the first attempt on both datasets, under the pilot-14 rule
10	that records are filed by paper, with one claims file of 33 claims that
11	replaces the two per-dataset files of fujisawa-2008-01 (DANDI:000067) and
12	fujisawa-2008-02 (CRCNS pfc-2). DANDI:000067 is pinned at 0.261106.2004, the
13	most recent published version, which the paper does not cite; CRCNS pfc-2 is
14	unversioned, with the MD5 sums printed in the notebook. The paper, Fujisawa,
15	Amarasingham, Harrison and Buzsaki in Nature Neuroscience (11, 823-833),
16	records units with one 8-shank, 64-site silicon probe per rat in anterior
17	cingulate and dorsal prelimbic cortex of four rats in an odor-based delayed
18	matching-to-sample task on a figure-eight T-maze, three in layer 2/3 and one
19	in layer 5, and reports trajectory-specific firing along the maze, putative
20	monosynaptic connections found from cross-correlograms with a jitter test,
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='docs/pilot-notes/fujisawa-2008-03.md'
s=open(p).read()
s=s.replace("""It is the first attempt on both datasets, under the pilot-14 rule
that records are filed by paper, with one claims file of 33 claims that
replaces the two per-dataset files of fujisawa-2008-01 (DANDI:000067) and
fujisawa-2008-02 (CRCNS pfc-2).""","""It uses both datasets, under the pilot-14 rule that records are
filed by paper, with one claims file of 33 claims that replaces the two
per-dataset files; fujisawa-2008-02 used CRCNS pfc-2 alone.""")
s=s.replace("""under either labelling) and `fig7-supralinear`
(transmission""","""under either labelling) and `fig7-supralinear` (transmission""")
s=s.replace("""(transmission below the linear prediction in every satellite). The outcomes of""","""below the linear prediction in every satellite). The outcomes of""")
s=s.replace("""session, and `population-vector-width` used rate curves built differently) and
one,
`fig4-pair-156-136`, graded""","""session, and `population-vector-width` used rate curves built differently)
and one, `fig4-pair-156-136`, graded""")
open(p,'w').write(s)
E
sed -n 9,14p docs/pilot-notes/fujisawa-2008-03.md; sed -n 40,46p docs/pilot-notes/fujisawa-2008-03.md; sed -n 60,68p docs/pilot-notes/fujisawa-2008-03.md
```

```
third round. It uses both datasets, under the pilot-14 rule that records are
filed by paper, with one claims file of 33 claims that replaces the two
per-dataset files; fujisawa-2008-02 used CRCNS pfc-2 alone. DANDI:000067 is pinned at 0.261106.2004, the
most recent published version, which the paper does not cite; CRCNS pfc-2 is
unversioned, with the MD5 sums printed in the notebook. The paper, Fujisawa,
Amarasingham, Harrison and Buzsaki in Nature Neuroscience (11, 823-833),
`fig3-cell-classes` (23 interneurons, 3.7%), `fig3d-hub` (86 of 117 cells
against 39), `fig3b-session-connections`, `fig5a-session-selective-connections`,
`fig6-facilitation-depression` (no combination with both fractions above 5%,
under either labelling) and `fig7-supralinear` below the linear prediction in every satellite). The outcomes of
`rats-and-units` and `central-arm-selectivity` rest on taking the lab's cell
lists as the paper's units: with every NWB mPFC unit (1,373) the first would be
not reproduced and the second would have both values within tolerance under
reconciliation with fujisawa-2008-02, run blind, finds all 12 of its findings
still present and 7 of the 19 shared claims with a changed outcome, three from
partial outcomes the merged claims file adds, three from differences in
method (`task-performance` was tested there from the sensor channels of one
session, and `population-vector-width` used rate curves built differently)
and one, `fig4-pair-156-136`, graded differently on nearly the same numbers. The
author's run took about 3 h 36 min; two full runs failed, one on a variable
[... 2 more lines not kept]
```

**Agent**

My second replace dropped "(transmission"; fixing that and the long lines.

**Agent calls Bash**

```bash
cd  python - <<'E'
p='docs/pilot-notes/fujisawa-2008-03.md'
s=open(p).read()
s=s.replace("""per-dataset files; fujisawa-2008-02 used CRCNS pfc-2 alone. DANDI:000067 is pinned at 0.261106.2004, the
most recent published version, which the paper does not cite; CRCNS pfc-2 is
unversioned, with the MD5 sums printed in the notebook.""","""per-dataset files; fujisawa-2008-02 used CRCNS pfc-2 alone. DANDI:000067 is
pinned at 0.261106.2004, the most recent published version, which the paper
does not cite; CRCNS pfc-2 is unversioned, with the MD5 sums printed in the
notebook.""")
s=s.replace("""under either labelling) and `fig7-supralinear` below the linear prediction in every satellite). The outcomes of
`rats-and-units`""","""under either labelling) and `fig7-supralinear` (transmission below the linear
prediction in every satellite). The outcomes of `rats-and-units`""")
open(p,'w').write(s)
E
awk 'length>82' docs/pilot-notes/fujisawa-2008-03.md; sed -n 40,48p docs/pilot-notes/fujisawa-2008-03.md
```

```
prediction in every satellite). The outcomes of `rats-and-units` and `central-arm-selectivity` rest on taking the lab's cell
1.173% excitatory, the excitatory rate 1.6 to 2.1 times the paper's),
`fig3-cell-classes` (23 interneurons, 3.7%), `fig3d-hub` (86 of 117 cells
against 39), `fig3b-session-connections`, `fig5a-session-selective-connections`,
`fig6-facilitation-depression` (no combination with both fractions above 5%,
under either labelling) and `fig7-supralinear` (transmission below the linear
prediction in every satellite). The outcomes of `rats-and-units` and `central-arm-selectivity` rest on taking the lab's cell
lists as the paper's units: with every NWB mPFC unit (1,373) the first would be
not reproduced and the second would have both values within tolerance under
one rat reading. Round 1 disagreed on `fig2c-active-fraction`, which it gave
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/fujisawa-2008-03.md",
 "old_string": "prediction in every satellite). The outcomes of `rats-and-units` and `central-arm-selectivity` rest on taking the lab's cell\nlists as the paper's units:",
 "new_string": "prediction in every satellite). The outcomes of `rats-and-units` and\n`central-arm-selectivity` rest on taking the lab's cell lists as the paper's\nunits:"
}
```

```
The file docs/pilot-notes/fujisawa-2008-03.md has been updated successfully. (note: the file had been modified on disk since you last read it — the edit applied cleanly, but the file contains other changes not in your context. Read it before edits that depend on surrounding content.)
```

**Agent calls Bash**

```bash
cd  cat docs/pilot-notes/fujisawa-2008-03.md; git status --short | grep -v '^?? \.'
```

```
# fujisawa-2008, Fujisawa et al. 2008, third attempt

Five claims reproduced (one on an assumption), 12 partially (five on an
assumption), 14 not reproduced (three on an assumption) and one blocked for
missing data, plus the link claim `channel-region-link`, not reproduced, as
the CRCNS channel map does not fit the nose-poke sensors of rat GG. The first
verification round agreed with 31 of the 33 outcomes as they stood and the
second with all 33; nothing was proposed after the second, so there was no
third round. It uses both datasets, under the pilot-14 rule that records are
filed by paper, with one claims file of 33 claims that replaces the two
per-dataset files; fujisawa-2008-02 used CRCNS pfc-2 alone. DANDI:000067 is
pinned at 0.261106.2004, the most recent published version, which the paper
does not cite; CRCNS pfc-2 is unversioned, with the MD5 sums printed in the
notebook. The paper, Fujisawa,
Amarasingham, Harrison and Buzsaki in Nature Neuroscience (11, 823-833),
records units with one 8-shank, 64-site silicon probe per rat in anterior
cingulate and dorsal prelimbic cortex of four rats in an odor-based delayed
matching-to-sample task on a figure-eight T-maze, three in layer 2/3 and one
in layer 5, and reports trajectory-specific firing along the maze, putative
monosynaptic connections found from cross-correlograms with a jitter test,
[... 113 more lines not kept]
```

**Agent**

I've written both files and changed nothing else; nothing is committed. In the notes I only had to choose how to name the repeat: the heading says "third attempt", as the `knierim-2000-03.md` heading does.

# fujisawa-2008, Fujisawa et al. 2008, third attempt

Five claims reproduced (one on an assumption), 12 partially (five on an assumption), 14 not reproduced (three on an assumption) and one blocked for missing data, plus the link claim `channel-region-link`, not reproduced, as the CRCNS channel map does not fit the nose-poke sensors of rat GG. The first verification round agreed with 31 of the 33 outcomes as they stood and the second with all 33; nothing was proposed after the second, so there was no third round. It uses both datasets, under the pilot-14 rule that records are filed by paper, with one claims file of 33 claims that replaces the two per-dataset files; fujisawa-2008-02 used CRCNS pfc-2 alone. DANDI:000067 is pinned at 0.261106.2004, the most recent published version, which the paper does not cite; CRCNS pfc-2 is unversioned, with the MD5 sums printed in the notebook. The paper, Fujisawa, Amarasingham, Harrison and Buzsaki in Nature Neuroscience (11, 823-833), records units with one 8-shank, 64-site silicon probe per rat in anterior cingulate and dorsal prelimbic cortex of four rats in an odor-based delayed matching-to-sample task on a figure-eight T-maze, three in layer 2/3 and one in layer 5. It reports trajectory-specific firing along the maze, putative monosynaptic connections found from cross-correlograms with a jitter test, transmission that depends on the rat's position, depression and facilitation with spike repetition, and a supralinear effect of coincident inputs. The claims were written from the version of record and its supplement, opening the PDF pages only for figures the text garbles; the paper links no analysis code. Spike times were taken from the NWB files, matched to the lab's cells by shank and cluster, and trials, positions and cell lists from CRCNS, with `EE188_example.mat`, the paper's 117-cell session, streamed from inside `EE.188.tar.gz`. Reproduced are `fig2-field-size` (0.241 +/- 0.169), `retrospective-coding-rare` (4.3% of EE.188 cells), `speed-not-correlated` (median -0.022), `no-spatial-clustering` (in the layer 2/3 session only) and `thinning-preserves-dependence` (7 of 34 pairs, on M = 5,000 surrogates). Partial are, among others, `rats-and-units` (627 units in three rats, within 633 +/- 63.3, but no rat holds 222), `side-arm-selectivity-by-layer` (61.0% and 52.6% against 40% and 22%, layer 5 higher at p = 0.046), `central-arm-selectivity` (30.4% and 29.5% against 16% and 18%), `traj-diverge` (the path at 0.30, head direction from 0.02), `fig4-position-dependence` (6.4% against 19.5%, above the null rates) and `population-vector-width` (layer 2/3 0.282 against the limit 0.267 with peak-normalised rates; z-scored rates would reproduce it). Not reproduced are, among others, `fig3-connection-rates` (1.449% connected and 1.173% excitatory, the excitatory rate 1.6 to 2.1 times the paper's), `fig3-cell-classes` (23 interneurons, 3.7%), `fig3d-hub` (86 of 117 cells against 39), `fig3b-session-connections`, `fig5a-session-selective-connections`, `fig6-facilitation-depression` (no combination with both fractions above 5%, under either labelling) and `fig7-supralinear` (transmission below the linear prediction in every satellite). The outcomes of `rats-and-units` and `central-arm-selectivity` rest on taking the lab's cell lists as the paper's units: with every NWB mPFC unit (1,373) the first would be not reproduced and the second would have both values within tolerance under one rat reading. Round 1 disagreed on `fig2c-active-fraction`, which it gave as not reproduced, and on `population-vector-width`, which moved to partially reproduced as it proposed. It asked for the NWB unit variant, peaks under both rate readings, the shared jitter and a tail labelling in the facilitation and depression test, a check of head direction and the one-cell jitter, all done. A question on the claims file's literal "first above later" went to a reader in `questions/fujisawa-2008.yaml`, written after the answer run, so it is unanswered. Round 2 agreed with all 33, withdrew its fig2c disagreement, and asked that `rats-and-units` be marked assumed and that the literal labelling be run with the shared jitter, which gives the same outcome. It also found sentences the outputs did not support, which were corrected, though one unit variant moves by one unit between the verifier's copy and the author's runs of the same seeded code (409 against 408 of 1,211), a cause not confirmed. The reconciliation with fujisawa-2008-02, run blind, finds all 12 of its findings still present and 7 of the 19 shared claims with a changed outcome: three from partial outcomes the merged claims file adds, three from differences in method (`task-performance` was tested there from the sensor channels of one session, and `population-vector-width` used rate curves built differently) and one, `fig4-pair-156-136`, graded differently on nearly the same numbers. The author's run took about 3 h 36 min; two full runs failed, one on a variable name reused across cells and one on an array reshape, both fixed, and peak memory was brought from 12.1 to 9.0 GB with identical results. The notebook ran in 29 min at first, 42 min after round 1, 40 min after round 2 and 2117 s after the reconciliation, whose own notebook ran in 108 s.

The dataset was converted by CatalystNeuro (catalystneuro/buzsaki-lab-to-nwb). Only correct trials are listed, in SessionNP, the whl trial numbers and the NWB trials tables, so task performance and any analysis of error trials cannot be made from either dataset. Neither dataset gives the layer of each rat's probe or links the rats EE, FF and GG to the paper's E to H, no rat holds the paper's 222 layer 5 units and no session the 142 cells of the layer 5 session of Figure 2a and Supplementary Figure 11. The CRCNS description documents a 1 Hz 'Cells' list that the files do not hold and does not describe CellsInfo, the per-session cell list (627 units with EE.188's example file, against 1,373 sorted mPFC units). CellsInfo is consistent with the 1 Hz rule (98.9% of listed units reach 1 Hz in the trials, 28.7% of those left out), and neither dataset marks the paper's well-isolated units. In 11 of 13 working memory sessions of DANDI:000067 every unit has cell_type 'not classified in the source' and lab_cell_number -1, so the NWB units can be linked to the lab's cells only through shank and cluster_id, and then their spike times are identical for 615 of the 627 used. The EE.088 file has no wideband signal, and EE.188 and EE.210 have no trials table or linearised position, though CRCNS holds them. In the three GG sessions channels 97 and 98, the nose-poke sensors in the CRCNS description, carry no poke signal, nor does any channel from 97 to 101, which the NWB files label 'neural'; the FF files have 104 channels labelled as rat EE's layout, where the description gives FF 101. The two CRCNS lists of EE.188's cells disagree (105 cells, 87 pyramidal and 18 interneurons, against 117, 33 pyramidal, 15 interneurons and 69 unknown, with types agreeing for 42 of the 105 common cells), and DANDI:000067 uses the 105-cell list. The example file codes cells 32 and 72 as interneurons, though Figure 7a names them presynaptic pyramidal cells, and cell 136, the interneuron of Figure 4, as unknown. Its pairs_all list holds 43 connections, against the paper's 48 and 30 for the session, and its largest component is the 39-cell circuit of Figure 3d; which selection it is, is not said. Ten of the 13 sessions track a single LED, so head direction exists only for EE.152, EE.165 and EE.188. The linearised position is nonzero through each trial's nose poke, and the spikes' trial labels and positions start at the first nose-poke while the description defines the trial start as the end of the last (269071 of 676892 labelled spikes fall between the two). `EE188_example.mat` is not in folder EE0708 or in filelist.txt but is member 62 of 75 of EE.188.tar.gz, 1.99 GB into the 2.41 GB gzip stream. The trial table of EE.188 leaves out 3 trials that the sensor channels and the position file show as correct and 1 error trial. Questions are put to the paper's authors: how the rates enter the population vectors, how many permutations or jitter surrogates each test used, how Figure 7 defines coincident events and the transmission window, which rat is layer 5 and which units make the 633, whether the global band of the jitter test was the minimal band or 1% on each side and whether the cross-correlograms were binned at 1 or 0.5 ms (1.449% and 1.091% of directed pairs connected here, against 0.79%), and how the connections of Figure 3d were chosen.

The author's points on the protocol: the claims file says the number of permutations should not change the outcome, but at level 0.01 it does, so more were used and the claims marked assumed; no rule says how to combine two datasets for one claim, and spikes were taken from DANDI and trials and cell lists from CRCNS; `entry.py check` asks for an `inputs` entry for a `with_labels` claim even when the labels come from the dataset's own description; the `fig2c-active-fraction` criterion defines only reproduced, and partial was used; the data fix some of the claims file's open readings, recorded as a deviation; small members were cached on disk during development, against "do not download to disk", and deleted afterwards; and the blinded checkout still held the old per-dataset claims files and reader transcripts, which were not read.

---

In this data the paper's trajectory-specific firing held in part: many prefrontal neurons fire differently on left and right trials, but in larger fractions than reported. Its monosynaptic connection results did not reproduce, as the jitter test here found far more excitatory connections and far fewer interneurons, with a bin width and test band the paper does not give. Position-dependent transmission was above chance but in 6.4% of connections against 19.5%, and the split into depressing and facilitating connections and the supralinear effect of coincident inputs did not reproduce. Task performance could not be tested, as only correct trials are deposited. Smaller results on field size, retrospective coding, running speed and spatial clustering reproduced.

## End of run

28 turns, 3 minutes, $1.70 at API prices, result: success.
