# niknam-2019 · recorder · run 42976904913

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/niknam-2019/; python tools/readme_row.py niknam-2019; grep -n -B2 -A12 'mt-3' targets/dandisets.json
```

```
docs/pilot-notes/simmons-2026-01.md
docs/pilot-notes/starkweather-2018-01.md
docs/pilot-notes/plitt-2021-01.md
docs/pilot-notes/gonzalez-cabrera-2026-01.md
docs/pilot-notes/kussovska-2025-01.md
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
verifier-1-report.md
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -B3 -A12 'mt-3\|niknam' targets/dandisets.json | head -40; head -5 README.md; grep -n 'readme\|columns\|Reproduced' tools/readme_row.py | head; for f in docs/pilot-notes/{simmons-2026-01,starkweather-2018-01,plitt-2021-01,gonzalez-cabrera-2026-01,kussovska-2025-01}.md; do echo "== $f"; cat $f; done
```

```
<persisted-output>
Output too large (44.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5a567266-e5f0-4c82-a03d-7ce388563451/tool-results/bjn7a30n5.txt

Preview (first 2KB):
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
3:    python tools/readme_row.py PAPER              # print the row (a paper key, or a dataset listed for one)
== docs/pilot-notes/simmons-2026-01.md
# simmons-2026, Simmons et al. 2026

Thirteen claims reproduced, two partially, four not reproduced and 18 blocked, 16
for missing data and two for insufficient metadata;
`fig6d-gat1-enriched-aldh1a1` and `figs5-gat-expression-in-snc`, on data outside
the dandiset (`data: elsewhere`), are counted apart and blocked as other, as
Dopabase has no pinned version and neither source was attempted in the time. Two
outcomes rest on an assumption, `fig3b-gabazine-increases-rate` and
`fig7d-astrocyte-gi-increases-rate`. The first verification round agreed with 37
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; wc -w simmons-2026-01.md starkweather-2018-01.md plitt-2021-01.md gonzalez-cabrera-2026-01.md kussovska-2025-01.md; cat starkweather-2018-01.md plitt-2021-01.md kussovska-2025-01.md; cd ../..; grep -n -i 'mt-3\|niknam' targets/dandisets.json
```

```
1525 simmons-2026-01.md
 1187 starkweather-2018-01.md
 1601 plitt-2021-01.md
 1285 gonzalez-cabrera-2026-01.md
 1701 kussovska-2025-01.md
 7299 total
# starkweather-2018, Starkweather et al. 2018

Twenty claims reproduced and twelve blocked, all twelve for missing data; two
outcomes rest on an assumption, `fig5e-task1-significant-slopes-unchanged` and
`fig5f-task2-significant-slopes-shift`. The first verification round agreed with
all 32 outcomes, and so did the second; nothing was proposed after the second, so
there was no third round. CRCNS vta-1 is unversioned and is pinned by the MD5 of
data.zip. The paper, Starkweather, Gershman and Uchida in Neuron (98, 616-629),
records light-identified VTA dopamine neurons in mice trained on odor tasks in
which odor A is followed by reward after a delay of 1.2 to 2.8 s, rewarded in
100% of trials in task 1 and 90% in task 2, and inactivates the mPFC with KORD
and SalB. It reports that under saline post-reward responses decrease with the
delay in task 1 and increase in task 2, that SalB flattens the task 2 increase
and leaves task 1 unchanged, that omission responses survive SalB, and it
[... 354 more lines not kept]
```

**Agent calls Bash**

```bash
grep -c '' targets/dandisets.json; grep -n -i 'crcns\|mt-' targets/dandisets.json | head -20; cat attempts/niknam-2019-01.yaml
```

```
<persisted-output>
Output too large (121.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5a567266-e5f0-4c82-a03d-7ce388563451/tool-results/bvrljhn8u.txt

Preview (first 2KB):
8339
schema_version: 3
id: niknam-2019-01
datasets:
- archive: crcns
  id: mt-3
  version: unversioned
  doi: 10.6080/K0FB514J
  relation: primary
paper: doi:10.1371/journal.pcbi.1007275
date: '2026-11-11'
entry: niknam-2019
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
print(type(d), (list(d)[:3] if isinstance(d,dict) else d[0]))
items = d if isinstance(d,list) else (d.get('dandisets') or list(d.values()))
for x in (items if isinstance(items,list) else []):
    if 'mt-3' in json.dumps(x) or 'niknam' in json.dumps(x).lower(): print(json.dumps(x,indent=1))
E
```

```
<class 'dict'> ['schema_version', 'generated', 'source']
```

**Agent calls Bash**

```bash
python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
print(list(d))
for k,v in d.items():
    if isinstance(v,(list,dict)):
        s=v if isinstance(v,list) else list(v.values())
        for x in s:
            if 'mt-3' in json.dumps(x) or 'niknam' in json.dumps(x).lower(): print(k, json.dumps(x,indent=1))
E
```

```
['schema_version', 'generated', 'source', 'counts', 'targets']
```

**Agent**

The dataset (CRCNS mt-3) has no entry in `targets/dandisets.json`, so there is no `catalystneuro` field to report. Reading the record now.

**Agent calls Bash**

```bash
sed -n 20,400p attempts/niknam-2019-01.yaml
```

```
runner:
    platform: GitHub Actions
    url: https://github.com/catalystneuro/encore/actions/runs/42964393998
inputs:
- what: RF, FF and ST probe of each neuron (probe_list of assets/data/main_lists.mat); the file's other, undocumented
    tables (nuron_list, nsglm_list, twobm_list, gauss_list, aggat_list) are shown for reference and decide no outcome.
    The repository's copies of the neuron files are compared with the CRCNS files.
  source: https://github.com/nnategh/SFA-Models at commit 1438dde9dd3207348ec0df1e5c4dd2a7b014e68e
outcomes:
- claim: probe-locations-link
  outcome: reproduced
  notebook: reproduce_niknam_2019.ipynb
  output: claim:probe-locations-link
  notes: All 41 files match a probe_list row by session and channel, and all 41 rows have a file. The RF recomputed
    by D1 with onsets is the listed RF for 38 neurons and a neighbour for the other 3 (41 of 41; also 41 with every-ms
    presentations). FF minus RF offsets are (-3, 0) for 26 neurons, (-2, 0) for 1 and (2, 0) for 14, giving 27 leftward
    and 14 rightward neurons. The neuron files in the code repository are identical to the CRCNS files in all four
    variables.
- claim: methods-neuron-counts
  outcome: reproduced
[... 361 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,700p attempts/niknam-2019-01.yaml | grep -v '^    \(parameters\|11.5\|of the 41\|notebook limit\|and the other\|the S-model ten\|Not run\|per neuron\|took 2.2\|port, not\|run. A fully\|CPU hours\|4 CPUs) for\|run beyond\|and 58,125\|fits per neuron\|for the selection\)'
```

```
of this attempt, 345 to 1,040 hours on 4 CPUs for the selection step of the 41 neurons, far over the 60 minute
- claim: fig6-example-neuron-predictions
  outcome: blocked
  blocked_by: too_large
  notebook: reproduce_niknam_2019.ipynb
  output: claim:fig5a-s-model-perisaccadic-better
  notes: 'Needs the S-model fitted per neuron (D4) ten times, and the F- and A-models, with 1000 simulated sequences.
    The notebook ports the parameter selection of select_bases.m and times it on one neuron and probe: 290,628 stimulus-basis
    of this attempt, 345 to 1,040 hours on 4 CPUs for the selection step of the 41 neurons, far over the 60 minute
- claim: fig7-prevalence-maps-correlate
  outcome: blocked
  blocked_by: too_large
  notebook: reproduce_niknam_2019.ipynb
  output: claim:fig5a-s-model-perisaccadic-better
  notes: 'Needs the S-model fitted per neuron (D4) ten times, and the A-model predictions. The notebook ports the
    parameter selection of select_bases.m and times it on one neuron and probe: 290,628 stimulus-basis parameters
    345 to 1,040 hours on 4 CPUs for the selection step of the 41 neurons, far over the 60 minute notebook limit
    and the five hours of an author run. A fully batched port, not written here, would need at least 11.5 to 27.5
    models the claim needs. The A-model fits the S-model ten times per neuron (Methods, A-model, "fitting the S-model
    ten times as explained earlier"), which multiplies that bound by ten, 29 to 69 hours on 4 CPUs. Not run beyond
[... 248 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -m3 '^| ' README.md; wc -w transcripts/niknam-2019/*-report.md; cat transcripts/niknam-2019/author-report.md
```

```
143 transcripts/niknam-2019/answer-report.md
  298 transcripts/niknam-2019/author-answers-report.md
  827 transcripts/niknam-2019/author-report.md
  691 transcripts/niknam-2019/author-revise-1-report.md
  562 transcripts/niknam-2019/author-revise-2-report.md
  478 transcripts/niknam-2019/claims-check-report.md
  751 transcripts/niknam-2019/claims-report.md
 1422 transcripts/niknam-2019/verifier-1-report.md
 1412 transcripts/niknam-2019/verifier-2-report.md
 6584 total
I've finished the author steps for niknam-2019 (steps 1 to 6). `python tools/entry.py all entries/niknam-2019` reports 0 errors, the notebook runs in 49 s, and the handover package is in `executed/niknam-2019/handover/`. Nothing is committed. Of the 34 claims, 8 were tested and 26 are blocked; most of the blocked ones need the paper's models, which can't be fitted within the run's limits.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| probe-locations-link | reproduced |
| methods-neuron-counts | reproduced |
| fig1b-saccadic-suppression | reproduced (8 neurons; 2.24 → 1.24 against the paper's 2.53 → 1.51) |
| fig1c-ff-remapping | not reproduced (8 neurons against 23) |
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/readme_row.py; grep -n -B3 'Reproduced\|reproduced |' README.md | head -20
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
python - <<'E'
import yaml
d=yaml.safe_load(open('claims/niknam-2019.yaml'))
print([k for k in d if k!='claims'])
for k,v in d.items():
    if k!='claims': print(k, ':', v if len(str(v))<3000 else str(v)[:3000])
for c in d['claims']:
    print(c['id'], c.get('data'), c.get('kind'), '|', str(c.get('source', c.get('location','')))[:80])
E
```

```
['schema_version', 'paper', 'checks']
schema_version : 2
paper : doi:10.1371/journal.pcbi.1007275
checks : [{'date': datetime.date(2026, 11, 11), 'kind': 'agent', 'model': 'claude-opus-5-5', 'ready': True, 'changes': ['fig1c-ff-remapping. The statement said the FF response comes "at a longer latency than the RF response" and called the 0.90 to 1.30 values the "late" response; the quoted sentence says neither, and its criterion does not test latency, which fig1-remapping-longer-latency holds. Removed both.', 'O1 (opening comment), and through it fig1b to fig1e, fig1-example-neurons and the fig5b and fig6 claims. Reading (c), an unpaired rank-sum test, is not the test the Methods name for recorded responses (one-sided signed-rank). It is now a variant that is shown and does not decide an outcome.', 'fig5a-n-model-no-perisaccadic-gain. The criterion called the paper\'s test two-sided; the paper gives only "the Wilcoxon signed-rank test". Now says sidedness is not stated, uses two-sided as a standard choice and shows the one-sided p.', 'fig5c-f-higher-ratio-than-s. Same for sidedness. Added that the paper does not say how neurons with fixation Delta LL per spike at or below zero enter the per-neuron ratio; both ways are shown.', 'fig8c-example-neuron-detectability. Restricting the candidates to neurons with both remapping effects in response and model is not in the paper; marked as an assumption, with all 41 neurons as a reported variant.', 'fig8e-population-ff-detectability (and fig8e-population-st-detectability, which follows it). Centres taken relative to the FF probe are not in the Methods, which say only that the variables were normalized by the probe distance; marked as an assumption.', 'Checked, unchanged. Every quoted number, SE used as tolerance, p-value and count against the Results, Methods and legends; the percent changes of fig5c-percent-changes agree with the slopes by the Methods formulas to rounding. The code settings in the opening comment (get_info.m t
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/niknam-2019; for f in claims-report.md claims-check-report.md answer-report.md author-answers-report.md; do echo "=== $f"; cat $f; done
```

```
=== claims-report.md
I wrote `claims/niknam-2019.yaml`. It passes the quote checker (34 claims, 33 quotes, 0 problems) and the claims schema. Nothing is committed.

**Text read.** The version of record (PMC6759185, Europe PMC full-text XML) was used. It includes the Methods, all figure legends, and the legends for S1–S6 Fig and S1–S3 Movie. There was no PDF, so no figure could be read. The supplement figures exist only as legends, but every number the claims use is in the Results or a legend.

**Code read.** github.com/nnategh/SFA-Models at commit 1438dde. It contains the S-, F- and A-model fits, the ΔLL/spk calculation, and `main_lists.mat`, which lists each neuron's RF, FF and ST probe. It has no code for the N-model, any statistical test, the partial models, the prevalence maps or the ROC detectability analysis.

**Claims.**
- **34 claims:** 1 link claim (the code's RF/FF/ST probe list checked against the dataset) and 33 findings. All 33 findings have quotes.
- **12 claims have statistics**, 28 entries in total: Wilcoxon signed-rank and rank-sum tests, one-tailed mid-P McNemar tests, and Pearson correlations.
- **All 34 have a criterion.** 30 have expected values; the tolerance is the paper's SE where it gives one and 10% otherwise.
- **Coverage:** Fig 1 (effect counts and normalized responses, latency, example neurons), Fig 3, Fig 5A–C, Fig 6A–D plus its example neurons, Fig 7 (two claims), Fig 8C/D/E, S1, S4 and S5, and the neuron counts from the Methods.
- **Data:** most claims are `with_labels`, because they need the RF/FF/ST probes from the code repository. The S1 claim (RF centres in dva) is `with_inputs`, because it needs each session's grid geometry, which the dataset description does not list.

**Open details and the readings named for each.** These are O1–O8 in the opening comment, plus a few within single claims.
- **O1, pairing for the signed-rank test on recorded data:** per trial, per condition, or an unpaired rank-sum test.
- **O2, what counts as a
[... 74 more lines not kept]
```

**Agent**

Read the claims and answer reports; no reader questions came up. Now the verification rounds and revisions.

**Agent calls Bash**

```bash
cd  head -c 5000 claims/niknam-2019.yaml; echo; for f in verifier-1-report.md author-revise-1-report.md; do echo "=== $f"; cat transcripts/niknam-2019/$f; done
```

```
# Claims for Niknam, Akbarian, Clark, Zamani, Noudoost & Nategh (2019), "Characterizing and
# dissociating multiple time-varying modulatory computations influencing neuronal activity",
# PLoS Comput Biol, doi:10.1371/journal.pcbi.1007275, tested on CRCNS:mt-3.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-11, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read. paper/10.1371-journal.pcbi.1007275.txt, the version of record (PMC6759185, open
# access, Europe PMC full-text XML flattened). It holds the abstract, Introduction, Results,
# Discussion, Methods, the legends of Figures 1 to 8, the legends of S1 to S6 Fig and S1 to S3
# Movie, and the Data Availability statement. No PDF was supplied, so no figure could be read.
# The supplement figures themselves are not in the text, only their legends; the numbers the
# results rest on are in the Results text and the legends, so the supplement's absence does not
# block a claim. Lost in extraction: every displayed equation (Eqs 1 to 14, including the
# parameter-selection threshold, Eq 10; the classification measures of the dichotomous analysis;
# the prevalence-map indicator m(t, tau); the maximum-detectability definition) and the whole
# reference list, so ref [48] (the N-model), ref [49] (the McNemar mid-P test) and ref [73]
# (Chen et al., algorithm 2) are known only by number.
#
# Code. https://github.com/nnategh/SFA-Models, commit 1438dde9dd3207348ec0df1e5c4dd2a7b014e68e
# (2019-12-20), linked in Methods (A-model framework) and Data Availability. MATLAB. It holds
[... 114 more lines not kept]
```

**Agent**

Round 1 agreed with all 34 outcomes. Reading round 2.

**Agent calls Bash**

```bash
cd transcripts/niknam-2019; cat verifier-2-report.md author-revise-2-report.md
```

```
**Verifier report, round 2: niknam-2019-01**

The claims file has 34 claims, and the attempt record has 34 outcomes:
- 5 reproduced
- 1 partially reproduced
- 3 not reproduced
- 25 blocked: 24 too_large, 1 methods_underspecified (fig5a-n-model-no-perisaccadic-gain), 1 metadata_insufficient (figs1-rf-centres)

No outcome in the attempt record carries `assumed: true`.

**1. Outcomes**

| Claim | Outcome | Agree | Basis (this notebook) |
|---|---|---|---|
| probe-locations-link | reproduced | yes | Cell 9: 41/41 files matched to a probe_list row, 0 rows without a file. The recomputed RF is the listed probe for 38 neurons and the listed probe or a neighbour for 41 (threshold 37). FF minus RF gives 27 left and 14 right. |
| methods-neuron-counts | reproduced | yes | Cell 12: 41 neurons, 11 sessions, 27 leftward neurons in 9 sessions, 14 rightward in 2. |
| fig1b-saccadic-suppression | reproduced | yes | Cell 18, (b, i): count 8, 2.235 and 1.239, all within tolerance. Both values sit near the lower edge of tolerance. 5 of the 8 neurons are in nuron_list (cell 40: 35/41 agree). |
| fig1c-ff-remapping | not_reproduced | yes, under the claims file | Cell 21: 8 neurons, 0.792 to 1.609. 0 of 3 numbers in tolerance. |
| fig1d-st-remapping | not_reproduced | yes, under the claims file | Cell 24: 11 neurons, 0.749 to 1.629. 0 of 3 numbers in tolerance. |
| fig1e-ff-and-st-remapping | not_reproduced | yes, under the claims file | Cell 27: 6 neurons, 0 of 5 numbers in tolerance. |
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml
d=yaml.safe_load(open('attempts/niknam-2019-01.yaml'))
for v in d['verifications']:
    print(v['reviewed'][:300]); print([r['agrees'] for r in v['results']].count(True), len(v['results']))
print(d.keys())
"
```

```
Round 1. The handover of the author run (commit 2650729e; author-answers changed no entry file): the executed notebook with the conclusion cells and the summary removed, the helper module and the claims file, with the paper. The verifier also listed the archive and tested the helper functions on syn
34 34
Round 2. The full executed notebook of the round-1 revision (commit efe8fb23), with the conclusion cells and the summary, the README, the attempt record, the helper module, the claims file and the paper, with the round-1 report. In reply, besides the per-claim responses: the probe timing in the summ
34 34
dict_keys(['schema_version', 'id', 'datasets', 'paper', 'date', 'entry', 'provenance', 'inputs', 'outcomes', 'findings', 'verifications'])
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml
d=yaml.safe_load(open('claims/niknam-2019.yaml'))
for c in d['claims']:
    print(c['id'], '::', c.get('statement'))
"
```

```
probe-locations-link :: The RF, FF and ST probe of each neuron listed in the code repository's main_lists.mat correspond to the dataset's neurons, and the RF probe recomputed from the dataset by the Methods' definition matches the listed one.
methods-neuron-counts :: Of 49 well-isolated MT neurons, 41 responded to the probes and were analysed; they come from 11 sessions, 27 neurons from 9 sessions with leftward saccades and 14 from 2 sessions with rightward saccades.
fig1b-saccadic-suppression :: Eight neurons show significant saccadic suppression; for them the average normalized response to an RF probe drops from 2.53 to 1.51 when the probe appears just before the saccade.
fig1c-ff-remapping :: Twenty-three neurons show significant FF-remapping; for them the average normalized response to an FF probe rises from 0.90 during fixation to 1.30 just before the saccade.
fig1d-st-remapping :: Thirty-seven neurons show significant ST-remapping; for them the average normalized late response to a probe near the saccade target rises from 0.83 during fixation to 1.35 just before the saccade.
fig1e-ff-and-st-remapping :: Twenty-two neurons show both FF- and ST-remapping; for them the normalized FF response rises from 0.90 to 1.32 and the normalized ST response from 0.80 to 1.46.
fig1-remapping-longer-latency :: Perisaccadic FF and ST responses come at a longer latency (80-150 ms after the probe) than RF responses (50-75 ms).
fig1-example-neurons :: In example neurons the RF response falls from 60.89 to 40.49 spk/s before the saccade; the late FF response rises from 7.90 to 18.42 spk/s; the late ST response rises from 23.80 to 64.64 spk/s; and in a neuron with both effects FF rises from 15.83 to 39.10 and ST from 16.15 to 36.17 spk/s, each with p < 0.001.
fig3-example-trial-predictions :: In example test trials of three neurons the S- and F-models follow the recorded firing rate, with Delta LL per spike up to 1.12 bits/spk for the S-model and 0.81 for the F-model in the best tri
[... 25 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/niknam-2019-01.md",
 "content": "# niknam-2019, Niknam et al. 2019\n\nThree claims reproduced on the dataset, one partially, three not reproduced and\n25 blocked, 24 as too large and `fig5a-n-model-no-perisaccadic-gain` for\nunderspecified methods; `figs1-rf-centres`, which needs the probe grid's geometry\nfrom outside the dataset (`data: with_inputs`), is counted apart and blocked for\ninsufficient metadata, and the link claim `probe-locations-link` reproduced. No\noutcome rests on an assumption. The first verification round agreed with all 34\noutcomes, and so did the second; nothing was proposed after the second, so there\nwas no third round. CRCNS mt-3 is unversioned and is pinned by the MD5 of\ndata.zip, which the notebook checks against checksums.md5. The paper, Niknam,\nAkbarian, Clark, Zamani, Noudoost and Nategh, \"Characterizing and dissociating\nmultiple time-varying modulatory computations influencing neuronal activity\"\n(PLoS Comput Biol, doi:10.1371/journal.pcbi.1007275), records 41 MT neurons in\ntwo rhesus monkeys making visually guided saccades while 7 ms probes flash one at\na time on a 9 x 9 grid. It reports that before a saccade responses to probes in\nthe receptive field (RF) are suppressed in 8 neurons, while late responses to\nprobes at the future field (FF) rise in 23 and near the saccade target (ST) in\n37, and it fits a time-varying point-process model (the S-model) with reduced F-\nand A-models, which it compares with an N-model and uses for prevalence maps and\nthe detectability of probes around the saccade. The claims were written from the\nversion of record without a PDF, its displayed equations and reference list lost\nin extraction, and from the paper's code (SFA-Models at commit 1438dde), which\nholds the S-, F- and A-model fits and main_lists.mat with each neuron's RF, FF\nand ST probe, but no code for the N-model or any statistical test; the claims\ncheck made six corrections and left four points open, for 34 claims. Reproduced\nare the neuron counts (41 neurons in 11 sessions, 27 leftward and 14 rightward),\n`fig1b-saccadic-suppression` (8 neurons, 2.235 to 1.239 against 2.53 to 1.51,\nnear the lower edge of tolerance, 5 of the 8 among the code's own list) and\n`fig1-remapping-longer-latency` (RF peak 62 ms, FF 108 ms, ST 99 ms), where only\nthe RF peak does not depend on how the remapping neurons are selected.\n`fig1-example-neurons` is partial, three of four examples matched with\nperisaccadic rates equal to the paper's to the second decimal and no neuron\nmatching the RF example. Not reproduced are `fig1c-ff-remapping` (8 neurons\nagainst 23), `fig1d-st-remapping` (11 against 37) and `fig1e-ff-and-st-remapping`\n(6 against 22), under pairing by condition; a signed-rank test over the 1 ms bins\nof the smoothed curves gives 34 ST neurons with all three numbers within\ntolerance, but the Methods exclude it and the verifier found it\nanti-conservative, so it does not decide. Every model claim of Figures 3 and 5 to\n8 and S4 and S5 is blocked: the notebook's port of the parameter selection needs\n58,125,600 single-parameter fits per neuron, 345 to 1,040 hours on 4 CPUs for\nthe 41 neurons, and a fully batched port, not written, at least 2.9 to 6.9 hours,\nbefore the full fits, the ten A-model fits and the simulations. The answer and\nauthor-answers runs found no questions and changed nothing. Round 1 held that\npairing by trial gives no pairs and was reported as counts of 0, that the\nclaims file's pairings may not be the paper's, that the example neurons'\nfixation rates are off while their perisaccadic rates match, that the\nsuppression count may match partly by chance, that the remapped latencies follow\nfrom the selection, that the limits behind too_large were not stated, and that\nthe probe order did not form blocks of 81; in reply pairing by trial was marked\nnot testable, two pairings over time bins were added as variants and the\nquestion went to `questions/niknam-2019.yaml`, a fixation-window scan and a\nper-neuron table against the code's list were added, and the probe order was\nexplained. Round 2 found that the cost figures in the text did not match the\nrun, that the batched bound of that run (2.9 h on 4 CPUs) was under the five\nhours of an author run, and that the probe timing was stated too narrowly; the\ncost was restated as the range across runs and resting on the port as it\nexists, the timing was widened, and a second question asks whether the examples\nmust meet the paper's p < 0.001, under which 1 of 4 would match. After round 2\nthe author identified ref [48] as Akbarian et al. (2018, doi:10.1109/TBME.2017.2762687),\nwhich describes the N-model but publishes no code; the claim stays blocked as\nthis attempt did not implement it. The author's run took about 25 minutes; the\nnotebook ran in 49 s with peak memory 1.35 GB, 46 s after the author-answers\nrun and 71 s after rounds 1 and 2, and nothing failed.\n\nThe Methods test each effect with a one-sided Wilcoxon signed-rank test but do\nnot say what is paired, and the choice decides the remapping counts: pairing by\ntrial is impossible in these data, as a probe returns only after a pass through\nthe whole order (median 562 to 604 ms between repeats), pairing by condition\ngives 8, 8 and 11 neurons against the paper's 8, 23 and 37, an unpaired test on\nevery millisecond a probe is on gives 12, 17 and 31, and the smoothed time-bin\ntest 15, 19 and 34. The dataset does not give the saccade direction of each\nsession, each neuron's RF, FF and ST probe, the position and spacing of the\nprobe grid, or which monkey each session comes from; the probes are only in\nmain_lists.mat of the code repository, and the grid geometry is nowhere in the\narchive, so the RF centres of S1 Fig cannot be computed. The paper and the\ndescriptor give 7 ms probes, one on screen at a time, in complete sequences of\n81, while in the files 91.5% of probe runs last 7 ms, 5.6% last 6 ms, most\nothers 14 or 21 ms and a few 8 to 28 ms, with gaps of 7 to 28 ms with no probe;\nthe order holds 75 codes in session 20150511 and 80 in 20150927 and 20150929,\nrestarts 35 to 296 ms after saccade onset in most trials of every session but\n20150717, and the arrays are 3000 ms long with probes until 1468 to 2371 ms,\nwhere the paper gives trials of 2100 to 2300 ms. main_lists.mat holds five more\n41 x 6 tables that no code reads and nothing documents, whose column sums match\nthe paper's counts (nuron_list 8, 23, 23 and 37), so they appear to be the\npaper's per-neuron classifications. The example neurons' fixation rates differ\nfrom the paper's while their perisaccadic rates match (RF example 56.94 against\n60.89 spk/s, the others 0.07 to 0.19 spk/s lower), and no fixation window\nbetween -560 to -440 ms and -160 to -40 ms matches them all, so the fixation set\nof Figure 1 is not identified. The 41 neurons and their per-session counts match\nthe descriptor, the 8 discarded units are not deposited, and the files are\nidentical to the copies in the code repository. The RF response peaks 58 ms\nafter probe onset and disappears when the stimulus codes are shifted by 300 ms.\nQuestions are put to the paper's authors: which presentations, pairs and test\nproduced the classification of Figure 1, and whether there is code for the\nN-model as fitted.\n\nThe author's points on the protocol: reading O1(a) of the claims file cannot be\nrun on these data; `too_large` and `not_runnable` overlap for a computation that\nexceeds the time limit; an estimate measured on a port depends on how efficient\nthe port is; a model defined only by an unidentified reference could be\n`methods_underspecified` or `not_runnable`; there is no category for the paper's\nown per-neuron results found in its code repository; results are to be broken\ndown by animal where no animal identifier exists; and blocked model claims have\nno cell of their own, so their `output` points to a shared benchmark cell.\n"
}
```

```
File created successfully at: docs/pilot-notes/niknam-2019-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/niknam-2019-01.md",
 "old_string": "at least 2.9 to 6.9 hours,",
 "new_string": "at least 2.9 to 6.9 hours on 4 CPUs,"
}
```

```
The file docs/pilot-notes/niknam-2019-01.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/niknam-2019-01.md",
 "content": "Saccadic suppression in MT held up in this data, with the paper's count of suppressed neurons, but far fewer neurons showed remapping of responses to the future field and the saccade target (11 against the paper's 37 for the saccade target). The Methods do not say what the signed-rank test pairs, and that choice decides the remapping counts; a pairing the Methods exclude comes close to the paper's. The time-varying encoding models, the paper's main contribution, could not be tested: fitting them was far beyond this run's compute limits, and the comparison N-model is described only in an earlier paper. The minor claims on neuron counts and response latency held, and most example neurons matched.\n"
}
```

```
File created successfully at: summaries/niknam-2019-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/niknam-2019-01.md docs/pilot-notes/niknam-2019-01.md; grep -n -i '—\|rather' summaries/niknam-2019-01.md docs/pilot-notes/niknam-2019-01.md; git status --short
```

```
115 summaries/niknam-2019-01.md
1343 docs/pilot-notes/niknam-2019-01.md
1458 total
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
?? docs/pilot-notes/niknam-2019-01.md
?? scripts
?? summaries/niknam-2019-01.md
```

**Agent**

I wrote the notes in `docs/pilot-notes/niknam-2019-01.md` (1,343 words) and the summary in `summaries/niknam-2019-01.md` (115 words, four sentences). No other file changed and nothing is committed. CRCNS mt-3 has no entry in `targets/dandisets.json`, so the notes say nothing about a CatalystNeuro conversion. The untracked dotfiles and `scripts` folder at the repository root were there before this run, and I left them alone.

# niknam-2019, Niknam et al. 2019

Three claims reproduced on the dataset, one partially, three not reproduced and 25 blocked, 24 as too large and `fig5a-n-model-no-perisaccadic-gain` for underspecified methods; `figs1-rf-centres`, which needs the probe grid's geometry from outside the dataset (`data: with_inputs`), is counted apart and blocked for insufficient metadata, and the link claim `probe-locations-link` reproduced. No outcome rests on an assumption. The first verification round agreed with all 34 outcomes, and so did the second; nothing was proposed after the second, so there was no third round. CRCNS mt-3 is unversioned and is pinned by the MD5 of data.zip, which the notebook checks against checksums.md5. The paper, Niknam, Akbarian, Clark, Zamani, Noudoost and Nategh, "Characterizing and dissociating multiple time-varying modulatory computations influencing neuronal activity" (PLoS Comput Biol, doi:10.1371/journal.pcbi.1007275), records 41 MT neurons in two rhesus monkeys making visually guided saccades while 7 ms probes flash one at a time on a 9 x 9 grid. It reports that before a saccade responses to probes in the receptive field (RF) are suppressed in 8 neurons, while late responses to probes at the future field (FF) rise in 23 and near the saccade target (ST) in 37, and it fits a time-varying point-process model (the S-model) with reduced F- and A-models, which it compares with an N-model and uses for prevalence maps and the detectability of probes around the saccade. The claims were written from the version of record without a PDF, its displayed equations and reference list lost in extraction, and from the paper's code (SFA-Models at commit 1438dde), which holds the S-, F- and A-model fits and main_lists.mat with each neuron's RF, FF and ST probe, but no code for the N-model or any statistical test; the claims check made six corrections and left four points open, for 34 claims. Reproduced are the neuron counts (41 neurons in 11 sessions, 27 leftward and 14 rightward), `fig1b-saccadic-suppression` (8 neurons, 2.235 to 1.239 against 2.53 to 1.51, near the lower edge of tolerance, 5 of the 8 among the code's own list) and `fig1-remapping-longer-latency` (RF peak 62 ms, FF 108 ms, ST 99 ms), where only the RF peak does not depend on how the remapping neurons are selected. `fig1-example-neurons` is partial, three of four examples matched with perisaccadic rates equal to the paper's to the second decimal and no neuron matching the RF example. Not reproduced are `fig1c-ff-remapping` (8 neurons against 23), `fig1d-st-remapping` (11 against 37) and `fig1e-ff-and-st-remapping` (6 against 22), under pairing by condition; a signed-rank test over the 1 ms bins of the smoothed curves gives 34 ST neurons with all three numbers within tolerance, but the Methods exclude it and the verifier found it anti-conservative, so it does not decide. Every model claim of Figures 3 and 5 to 8 and S4 and S5 is blocked: the notebook's port of the parameter selection needs 58,125,600 single-parameter fits per neuron, 345 to 1,040 hours on 4 CPUs for the 41 neurons, and a fully batched port, not written, at least 2.9 to 6.9 hours on 4 CPUs, before the full fits, the ten A-model fits and the simulations. The answer and author-answers runs found no questions and changed nothing. Round 1 held that pairing by trial gives no pairs and was reported as counts of 0, that the claims file's pairings may not be the paper's, that the example neurons' fixation rates are off while their perisaccadic rates match, that the suppression count may match partly by chance, that the remapped latencies follow from the selection, that the limits behind too_large were not stated, and that the probe order did not form blocks of 81; in reply pairing by trial was marked not testable, two pairings over time bins were added as variants and the question went to `questions/niknam-2019.yaml`, a fixation-window scan and a per-neuron table against the code's list were added, and the probe order was explained. Round 2 found that the cost figures in the text did not match the run, that the batched bound of that run (2.9 h on 4 CPUs) was under the five hours of an author run, and that the probe timing was stated too narrowly; the cost was restated as the range across runs and resting on the port as it exists, the timing was widened, and a second question asks whether the examples must meet the paper's p < 0.001, under which 1 of 4 would match. After round 2 the author identified ref [48] as Akbarian et al. (2018, doi:10.1109/TBME.2017.2762687), which describes the N-model but publishes no code; the claim stays blocked as this attempt did not implement it. The author's run took about 25 minutes; the notebook ran in 49 s with peak memory 1.35 GB, 46 s after the author-answers run and 71 s after rounds 1 and 2, and nothing failed.

The Methods test each effect with a one-sided Wilcoxon signed-rank test but do not say what is paired, and the choice decides the remapping counts: pairing by trial is impossible in these data, as a probe returns only after a pass through the whole order (median 562 to 604 ms between repeats), pairing by condition gives 8, 8 and 11 neurons against the paper's 8, 23 and 37, an unpaired test on every millisecond a probe is on gives 12, 17 and 31, and the smoothed time-bin test 15, 19 and 34. The dataset does not give the saccade direction of each session, each neuron's RF, FF and ST probe, the position and spacing of the probe grid, or which monkey each session comes from; the probes are only in main_lists.mat of the code repository, and the grid geometry is nowhere in the archive, so the RF centres of S1 Fig cannot be computed. The paper and the descriptor give 7 ms probes, one on screen at a time, in complete sequences of 81, while in the files 91.5% of probe runs last 7 ms, 5.6% last 6 ms, most others 14 or 21 ms and a few 8 to 28 ms, with gaps of 7 to 28 ms with no probe; the order holds 75 codes in session 20150511 and 80 in 20150927 and 20150929, restarts 35 to 296 ms after saccade onset in most trials of every session but 20150717, and the arrays are 3000 ms long with probes until 1468 to 2371 ms, where the paper gives trials of 2100 to 2300 ms. main_lists.mat holds five more 41 x 6 tables that no code reads and nothing documents, whose column sums match the paper's counts (nuron_list 8, 23, 23 and 37), so they appear to be the paper's per-neuron classifications. The example neurons' fixation rates differ from the paper's while their perisaccadic rates match (RF example 56.94 against 60.89 spk/s, the others 0.07 to 0.19 spk/s lower), and no fixation window between -560 to -440 ms and -160 to -40 ms matches them all, so the fixation set of Figure 1 is not identified. The 41 neurons and their per-session counts match the descriptor, the 8 discarded units are not deposited, and the files are identical to the copies in the code repository. The RF response peaks 58 ms after probe onset and disappears when the stimulus codes are shifted by 300 ms. Questions are put to the paper's authors: which presentations, pairs and test produced the classification of Figure 1, and whether there is code for the N-model as fitted.

The author's points on the protocol: reading O1(a) of the claims file cannot be run on these data; `too_large` and `not_runnable` overlap for a computation that exceeds the time limit; an estimate measured on a port depends on how efficient the port is; a model defined only by an unidentified reference could be `methods_underspecified` or `not_runnable`; there is no category for the paper's own per-neuron results found in its code repository; results are to be broken down by animal where no animal identifier exists; and blocked model claims have no cell of their own, so their `output` points to a shared benchmark cell.

---

Saccadic suppression in MT held up in this data, with the paper's count of suppressed neurons, but far fewer neurons showed remapping of responses to the future field and the saccade target (11 against the paper's 37 for the saccade target). The Methods do not say what the signed-rank test pairs, and that choice decides the remapping counts; a pairing the Methods exclude comes close to the paper's. The time-varying encoding models, the paper's main contribution, could not be tested: fitting them was far beyond this run's compute limits, and the comparison N-model is described only in an earlier paper. The minor claims on neuron counts and response latency held, and most example neurons matched.

## End of run

21 turns, 2 minutes, $1.06 at API prices, result: success.
