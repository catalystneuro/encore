# du-2026 · recorder · run 44973146102

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/du-2026/; python tools/readme_row.py du-2026; grep -n -B2 -A12 '"001201"\|"000129"' targets/dandisets.json
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/asari-2009-02.md
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
verifier-1-report.md
verifier-1.md
verifier-2-report.md
verifier-2.md
| [001201](https://dandiarchive.org/dandiset/001201), [000129](https://dandiarchive.org/dandiset/000129) | [Du et al. 2026](https://doi.org/10.64898/2026.08.04.742876) | 28 | 0 | 0 | 0 | [`du-2026`](entries/du-2026) |
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1170,1185p targets/dandisets.json; sed -n 5060,5075p targets/dandisets.json; grep -n -m3 '^| Dandiset\|^| Data' README.md; for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 asari-2009-02; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; ls summaries | head;
```

```
<persisted-output>
Output too large (35.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/af82f327-1755-452c-af44-bef0e7a7269a/tool-results/bkrzyv6dn.txt

Preview (first 2KB):
   ],
   "papers": [
    {
     "doi": "10.1088/1741-2552/aa9e95",
     "title": "Superior arm-movement decoding from cortex with a new, unsupervised-learning algorithm",
     "relation": "IsDescribedBy",
     "resource_type": null,
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "000130",
   "name": "DMFC_RSG: macaque dorsomedial frontal cortex spiking activity during time interval reproduction task",
   "published_version": "0.241017.1448",
[... 33 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/af82f327-1755-452c-af44-bef0e7a7269a/tool-results/bkrzyv6dn.txt"
}
```

```
1	   ],
2	   "papers": [
3	    {
4	     "doi": "10.1088/1741-2552/aa9e95",
5	     "title": "Superior arm-movement decoding from cortex with a new, unsupervised-learning algorithm",
6	     "relation": "IsDescribedBy",
7	     "resource_type": null,
8	     "preprint": false
9	    }
10	   ],
11	   "catalystneuro": []
12	  },
13	  {
14	   "dandiset": "000130",
15	   "name": "DMFC_RSG: macaque dorsomedial frontal cortex spiking activity during time interval reproduction task",
16	   "published_version": "0.241017.1448",
17	   ],
18	   "papers": [
19	    {
20	     "doi": "10.52202/085713-4642",
[... 521 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -m2 '^| Dandiset\|^| *Data' README.md; sed -n 5075,5090p targets/dandisets.json; cat summaries/asari-2009-02.md summaries/armstrong-2026-01.md; wc -l attempts/du-2026-01.yaml claims/du-2026.yaml transcripts/du-2026/*-report.md
```

```
}
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "001203",
   "name": "Data supporting \"Amygdalostriatal transition zone neurons encode sustained cue responses to guide defensive behaviors\" (Mills, et al, 2026)",
   "published_version": "0.261103.1719",
   "asset_count": 706,
   "size_gb": 1802.07,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "Mus musculus - House mouse"
   ],
The paper's central finding held in this data: A1 responses depend on the preceding sound for seconds, the context-dependent power decaying with a time constant of about 1 s as reported, while in the thalamus (MGB) the effect fades fast. Fewer probes showed significant context dependence than reported, the bound on short-window models rose more slowly, and longer STRF windows did improve predictions, under a fold averaging the paper does not describe. Amplitude and frequency changes outlasted modulation and higher-order changes, but the proportions did not match, on stimulus groupings rebuilt because the paper does not list them. The synaptic conductance findings could not be tested, as the data set holds no voltage-clamp recordings.
None of the paper's main findings could be confirmed in this data, and most could not be tested. The staged spiking modulation and its ramp could not be tested, because the spike times are not on the trial clock and the files hold no synchronisation signal. The whisker and wall findings could not be tested, because only 2 of the 19 animals are present and the files hold no whisker tracking. Where tests ran, the population baseline rate was about 7 Hz against the reported 2 Hz, and the turn success rate was 0.61 to 0.69 against 0.95. The drift diffusion fit only partly held, since its nondecision time missed 0.12 s.
   986 attempts/du-2026-01.yaml
  1104 claims/du-2026.yaml
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -m3 'Reproduced\|reproduced |' README.md | head; cat transcripts/du-2026/author-report.md transcripts/du-2026/author-revise-1-report.md transcripts/du-2026/author-revise-2-report.md transcripts/du-2026/verifier-1-report.md transcripts/du-2026/verifier-2-report.md
```

```
I finished steps 1 to 6 by 18:01 UTC. The entry is locked, its check passes with 0 errors, all six notebooks run cleanly from a fresh environment, and the handover package is built in `executed/du-2026/handover/`. Of the 33 claims, 31 are reproduced and 2 are blocked; none is partially or not reproduced. Nearly every value matches the paper exactly at its printed precision.

## 1. Outcomes

| Claim | Outcome |
|---|---|
| synthetic-template-null, synthetic-signal-ordering, synthetic-pair-breaking | reproduced |
| link-development-sample, link-neural-only-r2, link-context-ladder-gain, link-context-only-r2, link-phase-only-replacement, link-task-contrast-by-context | reproduced |
| nested-geometry-gain, nested-history-gain | reproduced |
| nested-replacement-negative | reproduced, `seed_sensitive` |
| replacement-source-diagnostics, permutation-negative, replacement-penalty-distance, replacement-ranks-lower, practical-mse-reduction | reproduced |
| representative-trial | reproduced, but only on one of the two readings of the session tie rule (the one the paper's code uses) |
| split-seed-stability | reproduced |
| rff-link | reproduced on reading (a); reading (b) misses by 0.0001 |
| estimator-family-link | reproduced (nonlinear context only at the setting in the paper's code) |
| temporal-offset, context-capacity-contrast | reproduced with both candidate estimators |
| confirm-geometry-gain, confirm-history-contraction, confirm-replacement, confirm-table1-values | reproduced, all `seed_sensitive` |
| rtt-data, rtt-gain, rff-rtt | reproduced |
| estimator-family-nlb | reproduced for the MC_RTT part, which is what the criterion tests; the MC_Maze part was not tested |
| maze-gain, rff-maze | blocked (`other`): DANDI:000139 was not read |
[... 223 more lines not kept]
```

**Agent**

Reports read. Next I'm checking how `readme_row.py` counts the outcomes (it prints 28, while the record has 33 reproduced) and reading the attempt record.

**Agent calls Bash**

```bash
grep -n -B3 -A3 '^| Dandiset\|---|---|' README.md | head -20; sed -n 1,80p tools/readme_row.py
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

**Agent calls Read**

```json
{
 "file_path": "attempts/du-2026-01.yaml"
}
```

```
1	schema_version: 3
2	id: du-2026-01
3	datasets:
4	- archive: dandi
5	  id: "001201"
6	  version: 0.251023.2336
7	  doi: 10.48324/dandi.001201/0.251023.2336
8	  relation: reuses
9	- archive: dandi
10	  id: "000129"
11	  version: 0.241017.1444
12	  doi: 10.48324/dandi.000129/0.241017.1444
13	  relation: reuses
14	paper: doi:10.64898/2026.08.04.742876
15	date: 2026-11-21
16	entry: du-2026
17	provenance:
18	  kind: agent
19	  accountable:
20	    name: CatalystNeuro
[... 967 more lines not kept]
```

**Agent**

The 28 counts the 33 reproduced claims minus five run on data held elsewhere (three synthetic, two MC_Maze). Now the claims file.

**Agent calls Bash**

```bash
sed -n 1,60p claims/du-2026.yaml; grep -n '^  - id:\|^- id:\|    data:\|  data:\|figure:\|  where:\|source:' claims/du-2026.yaml | head -150
```

```
# Claims for Du, Lai, Hu & Ye (2026), "A Context-Conditional Audit of Trial-Pairing-Dependent
# Neural Gain in Motor-Cortex Decoding", bioRxiv doi:10.64898/2026.08.04.742876, tested on
# DANDI:001201 (LINK) and DANDI:000129 (MC_RTT).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
# protocol as stated in docs/protocol.md (version pilot-18, Reader).
#
# Text read. The bioRxiv preprint posted August 10, 2026 (a Journal of Neural Engineering
# submission), full text in paper/10.64898-2026.08.04.742876.txt: main text, figure legends,
# Tables 1 to 3, Methods, Data and Code availability. No PDF was supplied. The paper's
# Supplementary information (formal properties, complete ladder results, replacement
# diagnostics, confirmation details, nonlinear-map seeds, temporal and capacity sensitivities)
# is not under paper/ and is not in the code release; every claim below rests on numbers the
# main text or its tables state. The one main-text sentence that points to supplement values
# (replacement ranks one to five) is a claim judged by sign alone (replacement-ranks-lower).
#
# Code read. github.com/gwkuqgfkqe/neural-decoder-context-audit, tag v1.0-jne-submission,
# commit b042fbe1cda2ca5a353751c693d7c95f45de0456 (Code availability names this release). It
# holds the loaders (src/neural_evidence/link.py, mc_rtt.py, mc_maze.py), the fully nested and
# nonlinear estimators (nested_estimators.py), the synthetic generator (synthetic.py), run
# scripts for the synthetic calibration, the primary analyses, the LINK context ladder, the
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,104p claims/du-2026.yaml; for l in 105 205 231 357 448 630 690 765 941; do sed -n "$l,$((l+6))p" claims/du-2026.yaml; done
```

```
# - LINK contexts (Methods 4.4; link.py). Phase basis 1, sin(r pi tau), cos(r pi tau), r = 1 to 4,
#   tau the within-window phase in [0, 1). Direction is the octant of target minus initial
#   position (code floor(((atan2(dy, dx) + pi) / 2 pi) 8) mod 8). Ladder: phase only (9 features);
#   direction by phase plus phase (81); plus additive target, initial position and displacement
#   (87); plus geometry by phase (141, "geometry by phase", the primary context); plus five past
#   bins of two-dimensional measured finger position ending at the same bin as the neural
#   history (151, "measured-output history"). Quadratic sensitivities add the 21 second-order
#   products of the six geometry variables and their phase interactions (351 and 361 features).
# - MC_RTT (Methods 4.3 and 4.4; mc_rtt.py). Behavior averaged from 1 kHz samples into 20 ms bins,
#   spikes histogrammed on the same grid; five 20 ms spike-count bins over 130 units (650
#   predictors) ending 80 ms before each behavior bin. Headline context is target plus five
#   cursor-position history bins ending at the same 80 ms boundary plus target minus the last
#   history cursor position. Direction octant of the block's mean target error is used for
#   stratification and replacement matching. Blocks use all bins after the warm-up (code; 21
#   bins per block in Table 2).
# - Fully nested estimator (Methods 4.5; nested_estimators.py, evaluate_fully_nested_audit).
#   Ridge with predictors standardized on each training scope, penalty grid 0.1, 1, 10, 100, 1e3,
#   1e4, 1e5. LINK outer split 70/30 whole trials stratified by direction (code random_state
#   20260726 for the primary results); NLB uses the release labels. Five condition-stratified
#   nuisance folds; in each, separate context-to-behavior and context-to-neural penalties from an
[... 88 more lines not kept]
```

**Agent**

I have what I need. Both Dandiset entries have an empty `catalystneuro` field, so the notes won't include a conversion sentence. Writing both files now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/du-2026-01.md",
 "content": "# du-2026, Du et al. 2026\n\nTwenty-eight claims reproduced on the dandisets, none partially, none not\nreproduced and none blocked; five more, on data held elsewhere, reproduced\nand are counted apart: the three synthetic calibration claims, run on data\nfrom a port of the paper's generator, and `maze-gain` and `rff-maze`, run on\nMC_Maze-medium in DANDI:000139. `maze-gain` rests on an assumption, and\nseven outcomes are marked seed sensitive. The first verification round\nagreed with all 33 outcomes as they stood and the second with all 33, and\nnothing was proposed after the second, so there was no third round. The\nrecord pins the versions the paper cites, 001201 at 0.251023.2336 and 000129\nat 0.241017.1444; two later versions of 001201 list the same 312 paths with\nthe same sizes. The paper, Du, Lai, Hu and Ye, \"A Context-Conditional Audit\nof Trial-Pairing-Dependent Neural Gain in Motor-Cortex Decoding\" (a bioRxiv\npreprint submitted to the Journal of Neural Engineering), asks how much\nmotor-cortex activity adds to decoding finger or hand velocity beyond task\ncontext (phase, target geometry and measured-output history), measured with\na fully nested Ridge estimator, and whether that gain depends on the correct\npairing of neural and behavioural trials. It reports that in LINK the gain\nfalls along a context ladder but stays positive (0.02009 for spiking-band\npower, 18 of 18 sessions), that nearest same-condition replacement makes it\nnegative, and that both hold in 20 untouched confirmation sessions and in\nthe MC_RTT and MC_Maze benchmarks. The claims were written from the\npreprint's full text without its supplement, and the attempt ports the\npaper's released code (commit b042fbe); nearly every value matches the paper\nat its printed precision. Every claim could be tested, though reading (b)\nof the nonlinear context in `estimator-family-link`, the 27 settings of\nMethods 4.6, was not run (estimated about 9 h), and the MC_Maze part of\n`estimator-family-nlb` does not bear on its outcome. The author's first run\ngave 31 reproduced and 2 blocked, the MC_Maze claims as `other` because\nDANDI:000139 had not been read for lack of time; round 1 agreed with\nblocking them, as data missing, and in reply the author tested both on\n000139 in a new notebook, citing the protocol's rule that a data elsewhere\nclaim is tested on the archive that holds its data, ran the release's own\nestimator functions next to the ports with identical values, and computed\nthe reading (c) position and feature counts that had been hard-coded or\nwrong. Round 2 asked that `maze-gain` be marked assumed, since its criterion\ngives no reproduction rule and the rule of `rtt-gain` was borrowed, noted\nthat its replacement tolerance is narrower than the rounding of the paper's\nprinted -0.00004, which went to a reader in `questions/du-2026.yaml`, and\nfound sentences the outputs did not support (velocity called exactly the\nforward difference in all 18 sessions, two seeds putting both SBP\nreplacement values outside, overgeneralized statements on seed sensitivity\nand a solver comparison with no printed output), all corrected. The first\n`entry.py all` failed because a HEAD request to `/download/` returns 403\nunder Python 3.13, and asset URLs were then taken from `contentUrl`. The\nestimator-family notebook took 58 minutes with the paper's lsqr solver, so\nthe block Ridge was solved by Cholesky as a deviation; on one session both\nchoose the same penalties and give gains of 0.0261224 and 0.0261222, and a\nfull lsqr run on all 18 sessions, tried in the round-2 revision, exceeded\nthe one-hour cell limit and cost about two hours. The author's final run\ntook 68 minutes, with peak memory under 1 GB per process.\n\nThe LINK velocity series are the forward first difference of the released\nposition, velocity[t] = position[t+1] - position[t] (correlation 1.000 and\nSD ratio 1.00 for both components in 17 of the 18 development sessions, and\n1.000 and 0.987 in 2021-10-15 CO), so each velocity bin uses the position of\nthe next bin; the files do not say so, and the paper states the\ndifferentiation recipe could not be verified. ThresholdCrossings is stored\nin volts but holds integer counts per 20 ms bin (0 to 11), and\nSpikingBandPower, also in volts, holds values of about 0.04 to 341. The\n20 ms timestamps of 2021-10-15 CO contain one gap of 1094 ms, where the\nother 17 development sessions step by 19 to 21 ms, though all 375 of its\ntrials are usable. The MC_RTT training file's behaviour series hold 15\nmissing 20 ms bins that no description mentions, none inside the 1,080\nanalysis blocks. The checks passed: LINK holds nine dates with a CO and an\nRD session, 375 trials each, one subject and no session deposited twice, its\nstreams share one clock (velocity decoding from SBP peaks at lag 0 in 16 of\n18 sessions and at 2 bins in 2), the paper's confirmation rule re-run on the\narchive's metadata gives the 20 sessions of its frozen manifest, and MC_RTT\nholds 1,080 blocks, 130 units and the 810/270 split. On the paper, its\nstatement that the NLB velocity unit fields and descriptions disagree does\nnot hold once the stored conversion of 0.001 is applied; its values are\nmatched at printed precision except the date-clustered intervals of\n`nested-geometry-gain` (0.02401 against 0.02404, 0.00711 to 0.01591 against\n0.00709 to 0.01594), reading (b) of `rff-link`, one of the two session tie\nreadings of `representative-trial` and RD-change reading (a) of\n`temporal-offset` under the fully nested estimator; and the exact values\nrest on one split or seed: under four other split seeds the confirmation\ngeometry-by-phase mean is 0.0148 to 0.0207 and the history mean 0.0034 to\n0.0082, and under four other estimator seeds the MC_Maze gain is -0.00014\nto 0.00053 and the replacement gain -0.0027 to 0.00003, while the\nqualitative pattern holds. No question is put to the paper's authors.\n\nThe author's points on the protocol: claims that fix the paper's own seeds\nsit against the five-seed rule, and the seeds were varied by +1000 to +4000\nfor only some fits because of the cost; data generated by the paper's code\nare marked `data: elsewhere` though the protocol assumes another archive,\nand the ported generator was run with the code listed under inputs; there\nis no block reason for an untested data elsewhere claim, and `other` was\nused; the protocol does not say whether porting the paper's code is\nallowed; `archives.md` does not say how to get an asset's S3 address, and\nthe HEAD request fails under Python 3.13; conclusions in markdown cells\nchange the entry hash and force a second full run of about 70 minutes; and\nthe 60-minute notebook limit forced the change of solver.\n"
}
```

```
File created successfully at: docs/pilot-notes/du-2026-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/du-2026-01.md",
 "content": "The paper's main findings held up in this data. In the LINK finger-task sessions, motor-cortex spiking-band power improved velocity decoding beyond task phase, target geometry and recent finger position (mean gain 0.02009, positive in all 18 sessions), and pairing each trial with the neural activity of the closest matched trial turned the gain negative. Both results held in the 20 held-out confirmation sessions and in the MC_RTT and MC_Maze reaching datasets. The exact confirmation and MC_Maze values match only under the paper's own random split and seed, and many move outside tolerance under others, while the pattern holds. The synthetic calibration, alternative estimators and timing and capacity checks also reproduced.\n"
}
```

```
File created successfully at: summaries/du-2026-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -c '—\|rather' docs/pilot-notes/du-2026-01.md summaries/du-2026-01.md; wc -w summaries/du-2026-01.md; git status --short
```

```
docs/pilot-notes/du-2026-01.md:0
summaries/du-2026-01.md:0
110 summaries/du-2026-01.md
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
?? docs/pilot-notes/du-2026-01.md
?? scripts
?? summaries/du-2026-01.md
```

**Agent**

I wrote the two new files and changed nothing else; nothing is committed. The untracked dotfiles and `scripts` in the repository root were there before this run, and I left them alone. Neither Dandiset entry has anything in its `catalystneuro` field, so the notes have no conversion sentence. The summary is 110 words.

# du-2026, Du et al. 2026

Twenty-eight claims reproduced on the dandisets, none partially, none not reproduced and none blocked; five more, on data held elsewhere, reproduced and are counted apart: the three synthetic calibration claims, run on data from a port of the paper's generator, and `maze-gain` and `rff-maze`, run on MC_Maze-medium in DANDI:000139. `maze-gain` rests on an assumption, and seven outcomes are marked seed sensitive. The first verification round agreed with all 33 outcomes as they stood and the second with all 33, and nothing was proposed after the second, so there was no third round. The record pins the versions the paper cites, 001201 at 0.251023.2336 and 000129 at 0.241017.1444; two later versions of 001201 list the same 312 paths with the same sizes. The paper, Du, Lai, Hu and Ye, "A Context-Conditional Audit of Trial-Pairing-Dependent Neural Gain in Motor-Cortex Decoding" (a bioRxiv preprint submitted to the Journal of Neural Engineering), asks how much motor-cortex activity adds to decoding finger or hand velocity beyond task context (phase, target geometry and measured-output history), measured with a fully nested Ridge estimator, and whether that gain depends on the correct pairing of neural and behavioural trials. It reports that in LINK the gain falls along a context ladder but stays positive (0.02009 for spiking-band power, 18 of 18 sessions), that nearest same-condition replacement makes it negative, and that both hold in 20 untouched confirmation sessions and in the MC_RTT and MC_Maze benchmarks. The claims were written from the preprint's full text without its supplement, and the attempt ports the paper's released code (commit b042fbe); nearly every value matches the paper at its printed precision. Every claim could be tested, though reading (b) of the nonlinear context in `estimator-family-link`, the 27 settings of Methods 4.6, was not run (estimated about 9 h), and the MC_Maze part of `estimator-family-nlb` does not bear on its outcome. The author's first run gave 31 reproduced and 2 blocked, the MC_Maze claims as `other` because DANDI:000139 had not been read for lack of time; round 1 agreed with blocking them, as data missing, and in reply the author tested both on 000139 in a new notebook, citing the protocol's rule that a data elsewhere claim is tested on the archive that holds its data, ran the release's own estimator functions next to the ports with identical values, and computed the reading (c) position and feature counts that had been hard-coded or wrong. Round 2 asked that `maze-gain` be marked assumed, since its criterion gives no reproduction rule and the rule of `rtt-gain` was borrowed, noted that its replacement tolerance is narrower than the rounding of the paper's printed -0.00004, which went to a reader in `questions/du-2026.yaml`, and found sentences the outputs did not support (velocity called exactly the forward difference in all 18 sessions, two seeds putting both SBP replacement values outside, overgeneralized statements on seed sensitivity and a solver comparison with no printed output), all corrected. The first `entry.py all` failed because a HEAD request to `/download/` returns 403 under Python 3.13, and asset URLs were then taken from `contentUrl`. The estimator-family notebook took 58 minutes with the paper's lsqr solver, so the block Ridge was solved by Cholesky as a deviation; on one session both choose the same penalties and give gains of 0.0261224 and 0.0261222, and a full lsqr run on all 18 sessions, tried in the round-2 revision, exceeded the one-hour cell limit and cost about two hours. The author's final run took 68 minutes, with peak memory under 1 GB per process.

The LINK velocity series are the forward first difference of the released position, velocity[t] = position[t+1] - position[t] (correlation 1.000 and SD ratio 1.00 for both components in 17 of the 18 development sessions, and 1.000 and 0.987 in 2021-10-15 CO), so each velocity bin uses the position of the next bin; the files do not say so, and the paper states the differentiation recipe could not be verified. ThresholdCrossings is stored in volts but holds integer counts per 20 ms bin (0 to 11), and SpikingBandPower, also in volts, holds values of about 0.04 to 341. The 20 ms timestamps of 2021-10-15 CO contain one gap of 1094 ms, where the other 17 development sessions step by 19 to 21 ms, though all 375 of its trials are usable. The MC_RTT training file's behaviour series hold 15 missing 20 ms bins that no description mentions, none inside the 1,080 analysis blocks. The checks passed: LINK holds nine dates with a CO and an RD session, 375 trials each, one subject and no session deposited twice, its streams share one clock (velocity decoding from SBP peaks at lag 0 in 16 of 18 sessions and at 2 bins in 2), the paper's confirmation rule re-run on the archive's metadata gives the 20 sessions of its frozen manifest, and MC_RTT holds 1,080 blocks, 130 units and the 810/270 split. On the paper, its statement that the NLB velocity unit fields and descriptions disagree does not hold once the stored conversion of 0.001 is applied; its values are matched at printed precision except the date-clustered intervals of `nested-geometry-gain` (0.02401 against 0.02404, 0.00711 to 0.01591 against 0.00709 to 0.01594), reading (b) of `rff-link`, one of the two session tie readings of `representative-trial` and RD-change reading (a) of `temporal-offset` under the fully nested estimator; and the exact values rest on one split or seed: under four other split seeds the confirmation geometry-by-phase mean is 0.0148 to 0.0207 and the history mean 0.0034 to 0.0082, and under four other estimator seeds the MC_Maze gain is -0.00014 to 0.00053 and the replacement gain -0.0027 to 0.00003, while the qualitative pattern holds. No question is put to the paper's authors.

The author's points on the protocol: claims that fix the paper's own seeds sit against the five-seed rule, and the seeds were varied by +1000 to +4000 for only some fits because of the cost; data generated by the paper's code are marked `data: elsewhere` though the protocol assumes another archive, and the ported generator was run with the code listed under inputs; there is no block reason for an untested data elsewhere claim, and `other` was used; the protocol does not say whether porting the paper's code is allowed; `archives.md` does not say how to get an asset's S3 address, and the HEAD request fails under Python 3.13; conclusions in markdown cells change the entry hash and force a second full run of about 70 minutes; and the 60-minute notebook limit forced the change of solver.

---

The paper's main findings held up in this data. In the LINK finger-task sessions, motor-cortex spiking-band power improved velocity decoding beyond task phase, target geometry and recent finger position (mean gain 0.02009, positive in all 18 sessions), and pairing each trial with the neural activity of the closest matched trial turned the gain negative. Both results held in the 20 held-out confirmation sessions and in the MC_RTT and MC_Maze reaching datasets. The exact confirmation and MC_Maze values match only under the paper's own random split and seed, and many move outside tolerance under others, while the pattern holds. The synthetic calibration, alternative estimators and timing and capacity checks also reproduced.

## End of run

13 turns, 2 minutes, $0.93 at API prices, result: success.
