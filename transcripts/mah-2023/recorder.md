# mah-2023 · recorder · run 45634380981

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/mah-2023/; python tools/readme_row.py mah-2023; ls summaries | head
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/andrews-2024-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/asari-2009-01.md
docs/pilot-notes/asari-2009-02.md
attempt-01
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author.md
reconcile-report.md
reconcile.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
verifier-2.md
| [001169](https://dandiarchive.org/dandiset/001169) | [Mah et al. 2023](https://doi.org/10.1038/s41467-023-43250-x) | 24 | 6 | 2 | 0 | [`mah-2023`](entries/mah-2023) |
README.md
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
for f in amjad-2025-01 andrews-2024-01 armstrong-2026-01 asari-2009-01 asari-2009-02 knierim-2000-02; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; grep -n -B2 -A2 "readme_row\|| Dandiset" README.md | head -20; cat summaries/asari-2009-02.md summaries/README.md
```

```
<persisted-output>
Output too large (37.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/981e5faa-4e7e-4733-ae11-f8f19425f09e/tool-results/bg1q2y49r.txt

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

**Agent calls Bash**

```bash
cat attempts/mah-2023-02.yaml; cat claims/mah-2023.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for e in (it if isinstance(it,list) else it.values()):
  if '001169' in json.dumps(e): print(json.dumps(e,indent=1))
"; ls transcripts/mah-2023/attempt-01
```

```
<persisted-output>
Output too large (352.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/981e5faa-4e7e-4733-ae11-f8f19425f09e/tool-results/b0o2twig5.txt

Preview (first 2KB):
schema_version: 3
id: mah-2023-02
datasets:
- archive: dandi
  id: "001169"
  version: 0.261120.1450
  doi: 10.48324/dandi.001169/0.261120.1450
  relation: primary
paper: doi:10.1038/s41467-023-43250-x
date: '2026-11-24'
entry: mah-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 39 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/981e5faa-4e7e-4733-ae11-f8f19425f09e/tool-results/bg1q2y49r.txt"
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
[... 524 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts/ | grep mah; ls docs/pilot-notes | grep mah; ls summaries | grep mah; ls transcripts/mah-2023/attempt-01; wc -c attempts/mah-2023-02.yaml claims/mah-2023.yaml transcripts/mah-2023/*report.md
```

```
mah-2023-01.yaml
mah-2023-02.yaml
mah-2023-01.md
mah-2023-01.md
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
recorder-report.md
recorder.md
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/mah-2023-02.yaml"
}
```

```
1	schema_version: 3
2	id: mah-2023-02
3	datasets:
4	- archive: dandi
5	  id: "001169"
6	  version: 0.261120.1450
7	  doi: 10.48324/dandi.001169/0.261120.1450
8	  relation: primary
9	paper: doi:10.1038/s41467-023-43250-x
10	date: '2026-11-24'
11	entry: mah-2023
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 817 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/mah-2023-02.yaml",
 "offset": 838,
 "limit": 400
}
```

```
838	    agrees: true
839	    outcome: reproduced
840	    reason: I agree with every outcome (section 1).
841	    response: No change of outcome.
842	  - claim: fig1e-wait-time-increases-with-reward
843	    agrees: true
844	    outcome: reproduced
845	    reason: I agree with every outcome (section 1).
846	    response: No change of outcome.
847	  - claim: fig1f-wait-time-block-effect
848	    agrees: true
849	    outcome: reproduced
850	    reason: I agree with every outcome (section 1).
851	    response: No change of outcome.
852	  - claim: fig1i-initiation-block-effect
853	    agrees: true
854	    outcome: reproduced
855	    reason: I agree with every outcome (section 1).
856	    response: No change of outcome.
857	  - claim: suppfig2-initiation-block-effect-after-unrewarded
[... 363 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^| Dandiset\|^|---" README.md | head -3; sed -n 1,60p tools/readme_row.py; python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
def walk(x):
    if isinstance(x,dict):
        if any('001169'==str(v) for v in x.values()): print(json.dumps(x,indent=1)); return
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(d)
E
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
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,40p claims/mah-2023.yaml; grep -n "^- id:\|^  id:\|  location:\|  kind:\|  data:\|  inputs:" claims/mah-2023.yaml | head -120
```

```
# Claims for Mah, Schiereck, Bossio & Constantinople (2023), "Distinct value computations support
# rapid sequential decisions", Nature Communications 14, 7573, doi:10.1038/s41467-023-43250-x,
# tested on DANDI:001169 (primary; the dandiset's title is the paper's and its description is the
# paper's abstract, so it is meant to hold the behavioral data of the 291 rats).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read. paper/10.1038-s41467-023-43250-x.txt, the version of record as served by Europe PMC
# (PMC10663503), with the main text, figure legends, Methods, Data and Code availability, and three
# supplement files extracted from their PDFs. Supplement 1 (MOESM1) is the Supplementary
# Information, Supplementary Figs 1 to 14 with legends; supplement 2 is the peer review file;
# supplement 3 is the reporting summary. No PDF of the main article was supplied; none was needed,
# as the text of every legend and table was legible. Source Data are not in the text read.
#
# Code read. github.com/constantinoplelab/published, folder rat_behavior, at commit b7b68ca8c107
# (HEAD, 2026-09-25; the folder was last changed in commit 87fd4a40b3, 2024-09-20, and its files
# were uploaded in f3cb954ef7, 2023-10-22). It holds MATLAB scripts that redraw each figure
# (Figures/Figure1.m to Figure5.m, FigureS1.m to FigureS14.m), the analyses they call (Analysis/:
# wtcurves, iticurves, waittime_20ul_by_previous_vol, latency_post20ul_by_previous_vol,
# regress_wt_vs_rew, regress_latency_vs_rew, block_dynamics_wt, block_dynamics_latency,
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 40,68p claims/mah-2023.yaml; sed -n 361,405p claims/mah-2023.yaml; sed -n 513,531p claims/mah-2023.yaml; sed -n 553,570p claims/mah-2023.yaml; sed -n 644,666p claims/mah-2023.yaml; sed -n 815,900p claims/mah-2023.yaml
```

```
# alternate around mixed blocks. Catch probability cohorts (Fig. 3c) of N = 3, 183, 61, 151 and 39
# rats for 0.1, 0.15, 0.2, 0.25 and 0.35. A further 16 rats ran a pre-initiation cue task (Fig. 5;
# 12 switched from the standard task, 4 trained only on it). Fig. 4 uses all stage 8 sessions,
# including sessions that fail the inclusion criterion. Whether the dandiset holds the pre-cue rats,
# the excluded sessions and the catch probabilities is the author's to find.
#
# Common method, used by every criterion unless it says otherwise (Methods, Criteria for including
# behavioral data and Statistical analyses, and the code).
# - Sessions. Stage 8 sessions that pass the inclusion criterion (regression of catch-trial wait
#   time on offered reward, after removing wait times above mean + 2 SD in that session; the
#   Methods include sessions with a significantly positive slope that immediately precede another
#   session with a positive slope. utils/screen_perf.m, a variant, asks only for a positive slope,
#   a 7-session moving mean of the slope at or above 0, more than 100 trials and more than 5 catch
#   trials, and keeps a session when the session before it also passed). If the dandiset holds
#   only included sessions, they are used as given.
# - Wait times. Opt-out wait times on catch trials; wait times more than 1 SD above the mean
#   catch-trial wait time pooled over the rat's sessions are removed (Methods, Statistical
#   analyses; parse_data_from_mysql.m:204). Timed-out catch trials (no opt-out within 100 s) are not
#   catch trials (parse_data_from_mysql.m).
# - Trial initiation times. All trials; values above the 99th percentile of the rat's pooled
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/mah-2023; for f in author-report.md author-revise-1-report.md author-revise-2-report.md verifier-1-report.md verifier-2-report.md reconcile-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (35.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/981e5faa-4e7e-4733-ae11-f8f19425f09e/tool-results/b41o1byuf.txt

Preview (first 2KB):
=== author-report.md
I finished the blind repeat attempt on `mah-2023` against DANDI:001169 version 0.261120.1450. All 33 claims were tested and none is blocked. The entry passes its check, both notebooks ran from a clean environment, and the handover was built. I did not verify my own work, and nothing is committed.

### 1. Outcomes

| Claim | Outcome |
|---|---|
| cohort-size, fig1e, fig1f, fig1i, suppfig2, suppfig3, suppfig12, suppfig14 | reproduced |
| fig2a, suppfig5, suppfig6, fig2c-d, fig2e, fig2f, fig2g-h, fig2j | reproduced |
| fig2k, fig2l | reproduced, but only when using the trials the paper's code uses |
| fig3c | reproduced, resting on an assumption |
| bayes-observer, suppfig9 | reproduced |
| fig3j | reproduced, resting on my model-fitting choices |
| suppfig8 | reproduced, resting on my model-fitting choices; depends on the random seed |
| fig3f | not reproduced, resting on my model-fitting choices; depends on the random seed |
| fig3i | partially reproduced, resting on an assumption |
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/981e5faa-4e7e-4733-ae11-f8f19425f09e/tool-results/b41o1byuf.txt"
}
```

```
1	=== author-report.md
2	I finished the blind repeat attempt on `mah-2023` against DANDI:001169 version 0.261120.1450. All 33 claims were tested and none is blocked. The entry passes its check, both notebooks ran from a clean environment, and the handover was built. I did not verify my own work, and nothing is committed.
3	
4	### 1. Outcomes
5	
6	| Claim | Outcome |
7	|---|---|
8	| cohort-size, fig1e, fig1f, fig1i, suppfig2, suppfig3, suppfig12, suppfig14 | reproduced |
9	| fig2a, suppfig5, suppfig6, fig2c-d, fig2e, fig2f, fig2g-h, fig2j | reproduced |
10	| fig2k, fig2l | reproduced, but only when using the trials the paper's code uses |
11	| fig3c | reproduced, resting on an assumption |
12	| bayes-observer, suppfig9 | reproduced |
13	| fig3j | reproduced, resting on my model-fitting choices |
14	| suppfig8 | reproduced, resting on my model-fitting choices; depends on the random seed |
15	| fig3f | not reproduced, resting on my model-fitting choices; depends on the random seed |
16	| fig3i | partially reproduced, resting on an assumption |
17	| fig3l | reproduced under the Results' reading, resting on an assumption |
18	| fig4a | partially reproduced (tested on the paper's Zenodo deposit) |
19	| fig4c, fig4d | reproduced (tested on the Zenodo deposit) |
20	| fig5b, fig5c | reproduced under the code's session reading |
[... 277 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/mah-2023-02.md",
 "content": "# mah-2023, Mah et al. 2023, second attempt\n\nTwenty-four claims reproduced, six partially, two not reproduced and none\nblocked, plus the link claim `pre-cue-session-link`, partially reproduced\n(14 of 16 rats linked). The first verification round agreed with 28 of the\n33 outcomes as they stood, and fig2k, fig2l, fig5b and fig5c moved from\nreproduced to partially reproduced and fig3l to not reproduced; the second\nround agreed with all 33, and nothing was proposed after it, so there was no\nthird round. The attempt pins version 0.261120.1450. The paper, Mah,\nSchiereck, Bossio and Constantinople in Nature Communications (14, 7573),\ntrains 291 rats in a temporal wagering task with hidden blocks of high, low\nand mixed rewards, and reports that wait times on catch trials follow an\ninference of the block while trial initiation times follow recently received\nrewards. Every claim could be tested: the cohort, the block effects and\ntrial-history regressions of Figures 1 and 2, the inferential against\nretrospective model comparison (Fig. 3j) and the pre-cue task of Figure 5\nreproduce, Figure 4 on the paper's Zenodo deposit (A_Structs_all), since\nthe dandiset holds only included sessions. Not reproduced are fig3f, where\nthe fitted inferential model's 20 uL wait times are longer after offers\nbelow 20 uL (+0.048 z, rank-sum p = 3.7e-05, unchanged from 6 starts), and\nfig3l, where neither reading of the wait time difference between the lambda\ngroups holds (C at mixed to low p = 0.337). fig2k, fig2l and fig5c hold only\nunder the code's trials, and only through the trials after violations, on\nwhich the task repeats the offer; fig3i is partial because the alternative\nmodels show overshoots of 0.0002 to 0.0058 z, fig4a because the first\nsession pair's mean wait time ratio (1.187) is not closer to 1 than over\npairs 16-25 (0.936), and fig5b because the Methods' 30-session reading\nrises from 5 to 10 uL. The model fits use the attempt's own bounds and 2\nrandom starts against the paper's 100, so fig3j, suppfig8, fig3f and fig3l\nrest on assumptions, and suppfig8 is seed sensitive (BIC and AIC p = 0.0305\nunder seed +3000, 0.0507 from 6 starts). The reconciliation with\n`mah-2023-01` found the attempt blind and traces the changed outcomes to an\nerror in the earlier attempt for fig2k and fig2l (session-first trials given\nthe previous session's last offer) and for the Figure 4 claims (blocked\nwithout reading the Zenodo deposit), and to readings for fig3j and suppfig8\n(fewer fit starts) and fig5b (where the 99th percentile cut is taken). The\nbehaviour notebook ran in 822 s and the models notebook in 2,766 s, with\npeak memory 9.7 GB; a development run was killed for memory in the Figure 4\ncells and Zenodo rate-limited the author twice. In the last revision the\nbehaviour notebook failed when Zenodo returned a 504 and was re-executed\nalone; the reconciliation's full run passed all four notebooks.\n\nThe dataset was converted by CatalystNeuro (catalystneuro/constantinople-lab-to-nwb).\nIt holds only the sessions that pass the paper's inclusion criterion, and\nnothing in it says so: the trial counter trials_in_stage jumps between\nconsecutive deposited sessions in 2,586 of 22,742 pairs (284 rats), the\nfirst deposited session of a rat starts at a median of 1,543 final-stage\ntrials, and the Zenodo deposit holds a median of 95 final-stage sessions per\nrat against 71 here, so Figure 4 and the pre-cue analyses cannot be run on\nthe dandiset alone. That deposit stops earlier than the dandiset for 49\nrats, with 1,718 dandiset sessions dated after the rat's last session in it.\nThe pre-cue sessions of Figure 5 are marked only by the undescribed task\nargument center_port_cue, True in 762 sessions, all of the 16 rats\nFigure5.m names. wait_time_threshold includes 16,086 timed-out catch trials\nat 100 s; over opt-out catch trials alone it would be lower in all 291 rats,\nby a median of 5.19 s. Catch probability 0.3 occurs in 180,591 trials of 8\nrats, a cohort the paper does not list, and two block transitions go\ndirectly between high and low blocks. No file gives a subject age: 275 rats\nhave a date of birth and the 1,181 files of the other 16 give only P6M/P24M.\nThe counts match the paper exactly (291 rats, 184 male and 107 female, a\nmedian of 33,493 trials and 71 sessions per rat). Of the earlier attempt's\nfindings on the data, the duplicated L011 session, the missing catch\nprobability and the undescribed is_catch flags are fixed in this version.\nIn the paper, the Methods use 20 uL trials for Fig. 2k, 2l and 5c while\nlatency_post20ul_by_previous_vol.m uses all mixed block trials, and without\nthe post-violation trials the population initiates faster after small\noffers; Fig. 2f is reported as r = 0.08, p = 0.18 in the Results and\nr = -0.03, p = 0.53 in the legend; the model fitting code is not public;\nthe Fig. 3c cohort sizes sum to 437 for 291 rats; Equation 6 uses H0 where\nGenerateSynthData_Bayes.m uses H0/2; Figure5.m pairs 16 rats with 20 dates\nand has no 30-session offset; and myTauShuffleTest.m scales the shuffled\ncoefficients by 10 under an amplitude bound of 1. Questions on these are put\nto the paper's authors.\n\nThe author's points on the protocol: the claims have no per-outcome `data`\nfield to mark Figure 4 as using data from elsewhere, so Zenodo was listed\nunder `inputs`; files were fetched whole instead of read with `remfile`;\nZenodo's rate limit was met with a few large range requests; the 60-minute\nlimit forced two notebooks, five seeds of model fits and a single-start\nlambda fit; the fig3i criterion gives no size for an overshoot; the\n`pre-cue-session-link` claim carries text from an earlier attempt, used as\nthe claims file has it; and the models notebook's `runtime_minutes` was\nleft at 35 against a run of 46, since editing it would invalidate the run.\n"
}
```

```
File created successfully at: docs/pilot-notes/mah-2023-02.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/mah-2023-02.md",
 "old_string": "rewards. Every claim could be tested: the cohort, the block effects and\ntrial-history regressions of Figures 1 and 2, the inferential against\nretrospective model comparison (Fig. 3j) and the pre-cue task of Figure 5\nreproduce, Figure 4 on the paper's Zenodo deposit (A_Structs_all), since\nthe dandiset holds only included sessions. Not reproduced",
 "new_string": "rewards. Every claim could be tested, those of Figure 4 on the paper's\nZenodo deposit (A_Structs_all), since the dandiset holds only included\nsessions. The cohort, the block effects of Figure 1, most of the\ntrial-history results of Figure 2, the inferential against retrospective\nmodel comparison (Fig. 3j), fig4c, fig4d and fig5d reproduce. Not reproduced"
}
```

```
The file docs/pilot-notes/mah-2023-02.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/mah-2023-02.md",
 "content": "Most of the paper's main findings held up in this data, and every claim could be tested: wait and trial initiation times both track the hidden reward blocks, initiation times follow recent rewards while wait times do not, and an inferential model fits wait times better than a retrospective one. Slower initiation after small offers held only on trials after violations, where the task repeats the offer; on the trials the Methods name, it reverses. Two model results did not reproduce, the inferential model's insensitivity to the previous offer and wait time differences between rats with good and poor inference, on refits made without the unpublished fitting code. Training effects, tested on the authors' Zenodo deposit, mostly held.\n"
}
```

```
File created successfully at: summaries/mah-2023-02.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/mah-2023-02.md; grep -c "—\|rather" docs/pilot-notes/mah-2023-02.md summaries/mah-2023-02.md; git status --short
```

```
118 summaries/mah-2023-02.md
docs/pilot-notes/mah-2023-02.md:0
summaries/mah-2023-02.md:0
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
?? docs/pilot-notes/mah-2023-02.md
?? scripts
?? summaries/mah-2023-02.md
```

**Agent**

# mah-2023, Mah et al. 2023, second attempt

Twenty-four claims reproduced, six partially, two not reproduced and none
blocked, plus the link claim `pre-cue-session-link`, partially reproduced
(14 of 16 rats linked). The first verification round agreed with 28 of the
33 outcomes as they stood, and fig2k, fig2l, fig5b and fig5c moved from
reproduced to partially reproduced and fig3l to not reproduced; the second
round agreed with all 33, and nothing was proposed after it, so there was no
third round. The attempt pins version 0.261120.1450. The paper, Mah,
Schiereck, Bossio and Constantinople in Nature Communications (14, 7573),
trains 291 rats in a temporal wagering task with hidden blocks of high, low
and mixed rewards, and reports that wait times on catch trials follow an
inference of the block while trial initiation times follow recently received
rewards. Every claim could be tested, those of Figure 4 on the paper's
Zenodo deposit (A_Structs_all), since the dandiset holds only included
sessions. The cohort, the block effects of Figure 1, most of the
trial-history results of Figure 2, the inferential against retrospective
model comparison (Fig. 3j), fig4c, fig4d and fig5d reproduce. Not reproduced are fig3f, where
the fitted inferential model's 20 uL wait times are longer after offers
below 20 uL (+0.048 z, rank-sum p = 3.7e-05, unchanged from 6 starts), and
fig3l, where neither reading of the wait time difference between the lambda
groups holds (C at mixed to low p = 0.337). fig2k, fig2l and fig5c hold only
under the code's trials, and only through the trials after violations, on
which the task repeats the offer; fig3i is partial because the alternative
models show overshoots of 0.0002 to 0.0058 z, fig4a because the first
session pair's mean wait time ratio (1.187) is not closer to 1 than over
pairs 16-25 (0.936), and fig5b because the Methods' 30-session reading
rises from 5 to 10 uL. The model fits use the attempt's own bounds and 2
random starts against the paper's 100, so fig3j, suppfig8, fig3f and fig3l
rest on assumptions, and suppfig8 is seed sensitive (BIC and AIC p = 0.0305
under seed +3000, 0.0507 from 6 starts). The reconciliation with
`mah-2023-01` found the attempt blind and traces the changed outcomes to an
error in the earlier attempt for fig2k and fig2l (session-first trials given
the previous session's last offer) and for the Figure 4 claims (blocked
without reading the Zenodo deposit), and to readings for fig3j and suppfig8
(fewer fit starts) and fig5b (where the 99th percentile cut is taken). The
behaviour notebook ran in 822 s and the models notebook in 2,766 s, with
peak memory 9.7 GB; a development run was killed for memory in the Figure 4
cells and Zenodo rate-limited the author twice. In the last revision the
behaviour notebook failed when Zenodo returned a 504 and was re-executed
alone; the reconciliation's full run passed all four notebooks.

The dataset was converted by CatalystNeuro (catalystneuro/constantinople-lab-to-nwb).
It holds only the sessions that pass the paper's inclusion criterion, and
nothing in it says so: the trial counter trials_in_stage jumps between
consecutive deposited sessions in 2,586 of 22,742 pairs (284 rats), the
first deposited session of a rat starts at a median of 1,543 final-stage
trials, and the Zenodo deposit holds a median of 95 final-stage sessions per
rat against 71 here, so Figure 4 and the pre-cue analyses cannot be run on
the dandiset alone. That deposit stops earlier than the dandiset for 49
rats, with 1,718 dandiset sessions dated after the rat's last session in it.
The pre-cue sessions of Figure 5 are marked only by the undescribed task
argument center_port_cue, True in 762 sessions, all of the 16 rats
Figure5.m names. wait_time_threshold includes 16,086 timed-out catch trials
at 100 s; over opt-out catch trials alone it would be lower in all 291 rats,
by a median of 5.19 s. Catch probability 0.3 occurs in 180,591 trials of 8
rats, a cohort the paper does not list, and two block transitions go
directly between high and low blocks. No file gives a subject age: 275 rats
have a date of birth and the 1,181 files of the other 16 give only P6M/P24M.
The counts match the paper exactly (291 rats, 184 male and 107 female, a
median of 33,493 trials and 71 sessions per rat). Of the earlier attempt's
findings on the data, the duplicated L011 session, the missing catch
probability and the undescribed is_catch flags are fixed in this version.
In the paper, the Methods use 20 uL trials for Fig. 2k, 2l and 5c while
latency_post20ul_by_previous_vol.m uses all mixed block trials, and without
the post-violation trials the population initiates faster after small
offers; Fig. 2f is reported as r = 0.08, p = 0.18 in the Results and
r = -0.03, p = 0.53 in the legend; the model fitting code is not public;
the Fig. 3c cohort sizes sum to 437 for 291 rats; Equation 6 uses H0 where
GenerateSynthData_Bayes.m uses H0/2; Figure5.m pairs 16 rats with 20 dates
and has no 30-session offset; and myTauShuffleTest.m scales the shuffled
coefficients by 10 under an amplitude bound of 1. Questions on these are put
to the paper's authors.

The author's points on the protocol: the claims have no per-outcome `data`
field to mark Figure 4 as using data from elsewhere, so Zenodo was listed
under `inputs`; files were fetched whole instead of read with `remfile`;
Zenodo's rate limit was met with a few large range requests; the 60-minute
limit forced two notebooks, five seeds of model fits and a single-start
lambda fit; the fig3i criterion gives no size for an overshoot; the
`pre-cue-session-link` claim carries text from an earlier attempt, used as
the claims file has it; and the models notebook's `runtime_minutes` was
left at 35 against a run of 46, since editing it would invalidate the run.

---

Most of the paper's main findings held up in this data, and every claim could be tested: wait and trial initiation times both track the hidden reward blocks, initiation times follow recent rewards while wait times do not, and an inferential model fits wait times better than a retrospective one. Slower initiation after small offers held only on trials after violations, where the task repeats the offer; on the trials the Methods name, it reverses. Two model results did not reproduce, the inferential model's insensitivity to the previous offer and wait time differences between rats with good and poor inference, on refits made without the unpublished fitting code. Training effects, tested on the authors' Zenodo deposit, mostly held.

## End of run

17 turns, 2 minutes, $1.16 at API prices, result: success.
