# gao-2018 · recorder · run 42900553240

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py gao-2018; ls transcripts/gao-2018/; ls summaries | head
```

```
docs/pilot-notes/mah-2023-01.md
docs/pilot-notes/patel-2026-01.md
docs/pilot-notes/keles-2024-01.md
docs/pilot-notes/mehrotra-2024-01.md
docs/pilot-notes/burman-2023-01.md
| [000007](https://dandiarchive.org/dandiset/000007) | [Gao et al. 2018](https://doi.org/10.1038/s41586-018-0633-x) | 10 | 6 | 3 | 26 | [`gao-2018`](entries/gao-2018) |
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
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for f in mah-2023-01 patel-2026-01 keles-2024-01 mehrotra-2024-01 burman-2023-01; do echo "=== $f"; cat docs/pilot-notes/$f.md; done; head -5 docs/pilot-notes/knierim-2000-02.md; grep -n "| Dandiset\|^| ---\|Paper |" README.md | head; for f in keles-2024-01 mah-2023-01; do echo "== $f"; cat summaries/$f.md; done
```

```
<persisted-output>
Output too large (41.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/13de435c-0e1c-4cb5-828a-6bbc06364c68/tool-results/bqpuwdqk6.txt

Preview (first 2KB):
=== mah-2023-01
# mah-2023, Mah et al. 2023

Twenty-three claims reproduced, two partially, two not reproduced and five
blocked, three for missing data and two as too large; the link claim the author
added, `pre-cue-session-link`, is partially reproduced and not counted. Five
outcomes rest on an assumption, `fig3i-retrospective-model-captures-initiation`,
`fig3f-inferential-model-not-sensitive-to-previous-offer`,
`suppfig9-wait-times-reflect-misinferences`,
`fig3l-lambda-groups-wait-time-dynamics` and
`fig5c-pre-cue-initiation-still-sensitive-to-previous-reward`. The first
verification round agreed with 32 of the 33 outcomes and disagreed on fig5c,
which it held partial, and the second agreed with all 33; nothing was proposed
after the second, so there was no third round. The paper, Mah, Schiereck,
Bossio and Constantinople in Nature Communications (14, 7573), trains 291 rats
in a temporal wagering task with hidden blocks of high, low and mixed reward
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/13de435c-0e1c-4cb5-828a-6bbc06364c68/tool-results/bqpuwdqk6.txt"
}
```

```
1	=== mah-2023-01
2	# mah-2023, Mah et al. 2023
3	
4	Twenty-three claims reproduced, two partially, two not reproduced and five
5	blocked, three for missing data and two as too large; the link claim the author
6	added, `pre-cue-session-link`, is partially reproduced and not counted. Five
7	outcomes rest on an assumption, `fig3i-retrospective-model-captures-initiation`,
8	`fig3f-inferential-model-not-sensitive-to-previous-offer`,
9	`suppfig9-wait-times-reflect-misinferences`,
10	`fig3l-lambda-groups-wait-time-dynamics` and
11	`fig5c-pre-cue-initiation-still-sensitive-to-previous-reward`. The first
12	verification round agreed with 32 of the 33 outcomes and disagreed on fig5c,
13	which it held partial, and the second agreed with all 33; nothing was proposed
14	after the second, so there was no third round. The paper, Mah, Schiereck,
15	Bossio and Constantinople in Nature Communications (14, 7573), trains 291 rats
16	in a temporal wagering task with hidden blocks of high, low and mixed reward
17	offers, and reports that wait times on catch trials follow the block through
18	inference of the hidden state while trial initiation times follow recent
19	rewards retrospectively, that the two have distinct dynamics at block
20	transitions and on previous offers, that an inferential model fits wait times
[... 546 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/gao-2018-01.yaml; wc -c claims/gao-2018.yaml transcripts/gao-2018/*-report.md; ls -la --time-style=full-iso transcripts/gao-2018/; git log --format='%h %ad %s' --date=iso -- transcripts/gao-2018 | head -20
```

```
<persisted-output>
Output too large (82.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/13de435c-0e1c-4cb5-828a-6bbc06364c68/tool-results/b49n9xhgl.txt

Preview (first 2KB):
schema_version: 3
id: gao-2018-01
datasets:
- archive: dandi
  id: '000007'
  version: 0.220126.1903
  doi: 10.48324/dandi.000007/0.220126.1903
  relation: primary
paper: doi:10.1038/s41586-018-0633-x
date: '2026-11-10'
entry: gao-2018
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 34 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/13de435c-0e1c-4cb5-828a-6bbc06364c68/tool-results/b49n9xhgl.txt"
}
```

```
1	schema_version: 3
2	id: gao-2018-01
3	datasets:
4	- archive: dandi
5	  id: '000007'
6	  version: 0.220126.1903
7	  doi: 10.48324/dandi.000007/0.220126.1903
8	  relation: primary
9	paper: doi:10.1038/s41586-018-0633-x
10	date: '2026-11-10'
11	entry: gao-2018
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-14
20	  runner:
[... 818 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/13de435c-0e1c-4cb5-828a-6bbc06364c68/tool-results/b49n9xhgl.txt",
 "offset": 839,
 "limit": 490
}
```

```
839	    response: No change of outcome. The CN recordings are not in the dataset.
840	  - claim: fig3b-cn-net-disinhibition
841	    agrees: true
842	    outcome: blocked
843	    reason: CN.
844	    response: No change of outcome. The CN recordings are not in the dataset.
845	  - claim: fig3c-cn-selectivity-abolished
846	    agrees: true
847	    outcome: blocked
848	    reason: CN.
849	    response: No change of outcome. The CN recordings are not in the dataset.
850	  - claim: ed6-cn-selectivity-both-alm-hemispheres
851	    agrees: true
852	    outcome: blocked
853	    reason: CN.
854	    response: No change of outcome. The CN recordings are not in the dataset.
855	  - claim: fig3d-alm-altered-by-cn-inhibition
856	    agrees: false
857	    outcome: not_reproduced
858	    reason: 'Cell 32: latency 14.7-22.1 ms (bootstrap mean, any bin label or trial set), outside 3.3-10.9 ms.
[... 462 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cd transcripts/gao-2018; for f in author-report answer-report author-answers-report verifier-1-report author-revise-1-report verifier-2-report author-revise-2-report; do echo "=== $f"; cat $f.md; done; cd ../..; python -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for e in (items if isinstance(items,list) else items.values()):
    if '000007' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))
" | head -60
```

```
<persisted-output>
Output too large (36.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/13de435c-0e1c-4cb5-828a-6bbc06364c68/tool-results/bv8miw7nl.txt

Preview (first 2KB):
=== author-report
I finished steps 1 to 5 and ran `handover`. Of the 45 claims, 18 were tested and 27 are blocked. The entry check passes with 0 errors and the notebook runs from a clean environment in 465 s (about 7.8 min). Nothing is committed.

## 1. Outcomes

| claim | outcome |
|---|---|
| fig1g-fastigial-activation-early-sample-no-effect | reproduced |
| fig1g-fastigial-activation-delay-errors | reproduced (0.873 to 0.630, p < 0.0001) |
| fig1h-fastigial-activation-delay-bias | reproduced (reading a; 2 mice biased contra, 3 ipsi) |
| fig1g-dentate-activation-little-effect | reproduced (p = 0.108; 3 of the paper's 8 mice) |
| fig1k-inhibition-delay-bias | partially reproduced (CD12 and CD13 are biased the same way) |
| fig2-alm-selective-fraction | reproduced (0.739 and 0.753, at the edge of the tolerance) |
| fig2cd-selectivity-emerges-gradually | blocked, methods_underspecified |
| fig3d-alm-altered-by-cn-inhibition | partially reproduced (fraction 0.395 matches; latency 15 to 23 ms against 7.1) |
| fig3e-alm-mean-rate-unchanged | partially reproduced (rates 22% below the paper's; paired and unpaired tests disagree) |
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/13de435c-0e1c-4cb5-828a-6bbc06364c68/tool-results/bv8miw7nl.txt"
}
```

```
1	=== author-report
2	I finished steps 1 to 5 and ran `handover`. Of the 45 claims, 18 were tested and 27 are blocked. The entry check passes with 0 errors and the notebook runs from a clean environment in 465 s (about 7.8 min). Nothing is committed.
3	
4	## 1. Outcomes
5	
6	| claim | outcome |
7	|---|---|
8	| fig1g-fastigial-activation-early-sample-no-effect | reproduced |
9	| fig1g-fastigial-activation-delay-errors | reproduced (0.873 to 0.630, p < 0.0001) |
10	| fig1h-fastigial-activation-delay-bias | reproduced (reading a; 2 mice biased contra, 3 ipsi) |
11	| fig1g-dentate-activation-little-effect | reproduced (p = 0.108; 3 of the paper's 8 mice) |
12	| fig1k-inhibition-delay-bias | partially reproduced (CD12 and CD13 are biased the same way) |
13	| fig2-alm-selective-fraction | reproduced (0.739 and 0.753, at the edge of the tolerance) |
14	| fig2cd-selectivity-emerges-gradually | blocked, methods_underspecified |
15	| fig3d-alm-altered-by-cn-inhibition | partially reproduced (fraction 0.395 matches; latency 15 to 23 ms against 7.1) |
16	| fig3e-alm-mean-rate-unchanged | partially reproduced (rates 22% below the paper's; paired and unpaired tests disagree) |
17	| fig3e-alm-increase-decrease | reproduced (increase fraction 0.592) |
18	| fig3f-alm-selectivity-abolished-by-cn-inhibition | reproduced, `assumed` |
19	| fig4-fastigial-activation-alm-latency | partially reproduced (latency 2.1 to 5.6 ms matches; fraction modulated 0.29 against 0.51) |
20	| fig4e-fastigial-activation-abolishes-alm-selectivity | reproduced |
[... 284 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B2 -A25 '"000007"' targets/dandisets.json | head -50; head -80 claims/gao-2018.yaml; grep -n "alm-4\|crcns\|CRCNS" claims/gao-2018.yaml attempts/gao-2018-01.yaml | head
```

```
124-  },
125-  {
126:   "dandiset": "000007",
127-   "name": "A cortico-cerebellar loop for motor planning",
128-   "published_version": "0.220126.1903",
129-   "asset_count": 54,
130-   "size_gb": 0.2,
131-   "data_standards": [
132-    "Neurodata Without Borders (NWB)"
133-   ],
134-   "species": [
135-    "House mouse"
136-   ],
137-   "approaches": [
138-    "electrophysiological approach"
139-   ],
140-   "papers": [
141-    {
142-     "doi": "10.1038/s41586-018-0633-x",
143-     "title": "A cortico-cerebellar loop for motor planning",
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^# \|^-\? *id:\|^  - id:\|^- id:" claims/gao-2018.yaml | sed -n '80,200p'; cat transcripts/gao-2018/claims-check-report.md
```

```
83:#     a two-tailed t-test at p < 0.01; neurons resampled with replacement 10,000 times and the
84:#     mean onset reported. The window that decides "significantly modulated" for this analysis is
85:#     not given (open; readings (a) the photostimulation period, (b) the whole delay epoch). The
86:#     paper describes this method only for CN photo-activation (Extended Data Fig. 9a); its use
87:#     for the latencies of Fig. 3 (ALM and CN photo-inhibition) is assumed, as it gives no other.
88:#  E6 Coding direction (Methods, Analysis of ALM population dynamics). Sessions with > 5
89:#     simultaneously recorded neurons and > 5 trials per condition (28 of 39). Spike counts in
90:#     400 ms windows in 10 ms steps; cd_t is the mean "lick right" minus mean "lick left" response
91:#     vector, averaged over the delay epoch to one cd, from correct control trials only. Projections
92:#     cd'x use control and photostimulation trials independent of those that estimated the cd,
93:#     correct and incorrect, grouped by instructed type; each session is offset by its mean
94:#     projection over all trials and times (from the cd-estimating trials); s.e.m. by bootstrap
95:#     over sessions. How trials are split into the cd-estimating and the independent sets is not
96:#     given; a random half split of control trials is used, a standard choice.
100:- id: fig1d-fastigial-lesion-contra-choice
118:- id: fig1e-fastigial-lesion-slow-initiation
142:- id: fig1d-dentate-lesion-no-effect
156:- id: fig1g-fastigial-activation-early-sample-no-effect
170:- id: fig1g-fastigial-activation-delay-errors
185:- id: fig1h-fastigial-activation-delay-bias
[... 63 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/gao-2018-01.md",
 "content": "# gao-2018, Gao et al. 2018\n\nTen claims reproduced, six partially, three not reproduced and 26 blocked, all\n26 for missing data; two outcomes rest on an assumption,\n`fig3e-alm-mean-rate-unchanged` and `cd-captures-selectivity`. The first\nverification round agreed with 39 of the 45 outcomes as they then stood and\ndisagreed on `fig2cd-selectivity-emerges-gradually`, which it held partial where\nthe record had it blocked for methods underspecified, on\n`fig3d-alm-altered-by-cn-inhibition`, `fig3e-alm-increase-decrease` and\n`cd-captures-selectivity`, which it held one step lower, and on fig3e-alm-mean-rate\nand `fig4-fastigial-activation-alm-latency`, which it held not reproduced; the\nauthor took the first four and kept the last two partial, and the second round\naccepted both and agreed with 44 of 45, the exception being that the record\nstill gave cd-captures-selectivity as reproduced, which the second revision\ncorrected. Nothing was proposed after the second round, so there was no third.\nThe dandiset is pinned at 0.220126.1903, its only published version. The paper,\nGao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw and Li in Nature (563,\n113-116), trains head-fixed mice to report a pole's location by licking left or\nright after a delay, and reports that fastigial lesions and photo-activation and\nPurkinje cell photo-inhibition of the cerebellar nuclei (CN) disrupt the choice,\nthat CN neurons carry preparatory activity, that photo-inhibiting the CN alters\nALM activity and abolishes its selectivity, and that fastigial photo-activation\ncollapses ALM preparatory activity along the coding direction (cd) with a\nlasting effect, while dentate photo-activation's effect recovers. The claims\nwere written from the NIH author manuscript (PMC6212318) as Europe PMC text with\nthe legends and two supplement files, without a PDF, so values drawn only in the\nfigures could not be read; the paper links no code. Of 45 claims only those on\nALM and on behaviour in the recording sessions could be tested. Reproduced are\n`fig1g-fastigial-activation-delay-errors` (0.873 against 0.630, p < 0.0001), the\nearly sample and dentate no-effect claims (dentate p = 0.108, on 3 of the\npaper's 8 mice), `fig1h-fastigial-activation-delay-bias`,\n`fig2-alm-selective-fraction` (800 of 1082, 0.739, at the edge of 0.738 to\n0.902), `fig3f-alm-selectivity-abolished-by-cn-inhibition` (in 15 of 20 draws of\nthe preference trials in the last 500 ms), `fig4e-fastigial-activation-abolishes-alm-selectivity`,\n`fig4f-fastigial-effect-persists` (13.1% against 1% by chance),\n`fig4i-cd-control-separation` and `fig4i-fastigial-collapses-cd` (reading (b),\ndifference -8.119). Partial are `fig1k-inhibition-delay-bias`, where CD12 and\nCD13 drop on the same trial type and CD16 is not in the dataset; fig2cd, whose\nresponse epoch maximum appears only when the response epoch fixes the\npreference; fig3e-alm-mean-rate, where the absence of a change holds by the\nunpaired test (p = 0.214, paired p = 0.022) and the rates miss; fig3e-alm-increase-decrease\n(158 and 112 against 108 and 89, fraction 0.585); fig4 latency (2.07 ms by bin\nstart, 162 of 557 modulated against 227); and cd-captures-selectivity (62.1% of\nthe selectivity, 34.2% of the variance against 27.0 +/- 4.2). Not reproduced\nare fig3d (676 neurons, 270 modulated against 197 +/- 19.7, latency 14.37 ms\nagainst 7.1 +/- 3.8), `fig4g-dentate-effect-recovers` (3.4% to 5.3% of neurons\nstay significant from 1 s after offset) and\n`ed10d-fastigial-endpoints-no-prediction` (slope 0.420, p = 0.0049). The\nauthor's first run had 12 reproduced, 4 partially, 2 not reproduced and 27\nblocked. The author asked no questions of a reader, so the answer and\nauthor-answers runs changed nothing. Round 1 held that the files hold more\nputative pyramidal units than the paper, that fig3f passed on one random draw,\nthat the cd-captures outcome rested on a variant, that fig2cd selected and\nmeasured neurons on the same trials, and that five sessions failing the clock\ncheck were kept; in reply the units table columns and file groups were printed,\nfig3f was repeated over 20 draws, a split-half variant was added to fig2cd, a\nrun without the five sessions changed no outcome, and a bug was found: 120\ntrials of BAYLORCD8 20171020 lie after its recording ends and had counted as\nsilent. Round 2 found the two record errors on cd-captures-selectivity and the\nmissing assumption on fig3e-alm-mean-rate, loose numbers in the photo_stim_id\nfinding, two findings without printed output, and that the claims file's E3\nparaphrase drops \"preparatory activity\", which went to\n`questions/gao-2018.yaml`. The notebook ran in 465 s at first, with peak memory\nabout 0.5 GB and the run taking about 50 of its 300 minutes, 320 s after the\nauthor-answers run and round 1 and 7.3 min after round 2; nothing failed.\n\nThe dandiset holds only the ALM recordings, 54 sessions in 13 mice: the CN\nrecordings (878 units in 18 mice and 60 units in 2 L7-cre x Ai32 mice), lick\ntimes, the behaviour-only sessions (lesions, 1.3 s and response epoch\nphoto-activation, 0.5 s and response epoch photo-inhibition), the\nVGAT-ChR2-EYFP experiments and the anatomy are not in it, so 26 of the 45\nclaims cannot be tested. photo_stim_id has no description and the files hold no\nlaser trace; from the ALM response codes 1 and 3 are read as early sample and 2\nand 4 as early delay photo-activation, 5 and 6 as delay photo-inhibition, and\nwhich of 5 and 6 is 1.5 mW and which 4.5 mW cannot be told, nor when the\nphotostimulus starts relative to pole_out_time. The files hold 1082 putative\npyramidal neurons in the 9 photo-activation mice (557 fastigial, 525 dentate)\nagainst the paper's 912 (446 and 466), and 676 in 20 sessions of the 4\nphoto-inhibition mice against 454 in 19; the units table has no quality or\nisolation field, nothing says which units or session the paper left out, and\n195 of the 676 fire under 0.5 spikes/s in the delay, so the counts and rate\nlevels of fig3d, fig3e and fig4 depend on a selection the files do not record.\nThe descriptions of pole_in_time, pole_out_time and cue_time say they are\nrelative to the trial start, while the values are on the session clock. The\nfiles place the manipulated CN of CD12 and CD13 on the left, the side of the\nrecorded ALM, where Supplemental Table 1 gives the right CN and the Methods say\nALM was always recorded contralaterally, and CD14 is recorded in the left ALM in\nthe files and the right in the table. Subjects anm00314746, anm00314756,\nanm00314757, anm00314758 and anm00314760 are AN105 to AN109 in the paper, and\nonly anm00314756 (AN106) and anm00314757 (AN107) can be matched by site; the\nwild-type genotype is \"unknown\" and session_description is empty. The cell_type\ncolumn labels 60 units \"pyramidal\" whose waveform is narrower than the paper's\n0.45 ms (33 under 0.35 ms), and the waveforms are stated at 20 kHz in every file,\nincluding the 34 sessions with the 32-channel probe, which the Methods say were\nsampled at 25 kHz. In 5 of 54 sessions the response to delay photostimulation\ncould not be shown to be locked to the trial events. In BAYLORCD8 20171020 the\nunits' observation intervals end at 7221.8 s and the last 127 of 462 trials,\nfrom 7223.1 to 8481.4 s, hold no spike, which obs_intervals records. Questions\nare put to the paper's authors: which epoch and how many trials fix each\nneuron's preferred trial type in Fig. 2c, how a latency bin is labelled and\nwhether a pre-onset baseline is subtracted, and how the fractions captured by\nthe cd are computed, as only one combination of the readings matches both\nnumbers.\n\nThe author's points on the protocol: it does not say how to judge a claim only\nhalf of whose data exist, as fig2cd covers ALM and CN; its rule to judge the\nfraction where the dataset holds fewer neurons does not cover a dataset that\nholds more; a shared method that names a detail as open falls between the rule\nfor readings a criterion lists and the rule for readings of a method detail;\nlink claims cover only outside data, so it has no form for inferring\nundocumented codes such as photo_stim_id from the data; and it does not say\nwhether recording sessions may stand in for the paper's behaviour sessions.\n"
}
```

```
File created successfully at: docs/pilot-notes/gao-2018-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/gao-2018-01.md",
 "content": "In this data the paper's central ALM findings held up: fastigial photo-activation during the delay caused errors and collapsed ALM preparatory activity along its coding direction, and photo-inhibiting the cerebellar nuclei abolished late-delay ALM selectivity. The recordings from the cerebellar nuclei, the lesions, licking and the anatomy could not be tested, as the dataset holds only the ALM sessions. That ALM recovers after dentate photo-activation did not reproduce, as a few percent of neurons stayed altered more than 1 s later. Counts of modulated neurons and firing rate levels mostly missed, as the files hold more neurons than the paper reports and do not say which it excluded.\n"
}
```

```
File created successfully at: summaries/gao-2018-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  wc -w summaries/gao-2018-01.md; grep -c "—\|rather\|\*\*" docs/pilot-notes/gao-2018-01.md summaries/gao-2018-01.md; git status --short
```

```
108 summaries/gao-2018-01.md
docs/pilot-notes/gao-2018-01.md:0
summaries/gao-2018-01.md:0
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
?? docs/pilot-notes/gao-2018-01.md
?? scripts
?? summaries/gao-2018-01.md
```

**Agent**

I wrote both files and changed nothing else. Nothing is committed. The summary is 108 words in four sentences. The `catalystneuro` field for 000007 is empty, so the notes don't open with the conversion sentence. The sources don't mention CRCNS:alm-4, so it isn't in either file. The other untracked files in the repository root (dotfiles, `.idea`, `.vscode`, `scripts`) were there before I started, and I left them alone.

**docs/pilot-notes/gao-2018-01.md**

# gao-2018, Gao et al. 2018

Ten claims reproduced, six partially, three not reproduced and 26 blocked, all 26 for missing data; two outcomes rest on an assumption, `fig3e-alm-mean-rate-unchanged` and `cd-captures-selectivity`. The first verification round agreed with 39 of the 45 outcomes as they then stood and disagreed on `fig2cd-selectivity-emerges-gradually`, which it held partial where the record had it blocked for methods underspecified, on `fig3d-alm-altered-by-cn-inhibition`, `fig3e-alm-increase-decrease` and `cd-captures-selectivity`, which it held one step lower, and on fig3e-alm-mean-rate and `fig4-fastigial-activation-alm-latency`, which it held not reproduced; the author took the first four and kept the last two partial, and the second round accepted both and agreed with 44 of 45, the exception being that the record still gave cd-captures-selectivity as reproduced, which the second revision corrected. Nothing was proposed after the second round, so there was no third. The dandiset is pinned at 0.220126.1903, its only published version. The paper, Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw and Li in Nature (563, 113-116), trains head-fixed mice to report a pole's location by licking left or right after a delay, and reports that fastigial lesions and photo-activation and Purkinje cell photo-inhibition of the cerebellar nuclei (CN) disrupt the choice, that CN neurons carry preparatory activity, that photo-inhibiting the CN alters ALM activity and abolishes its selectivity, and that fastigial photo-activation collapses ALM preparatory activity along the coding direction (cd) with a lasting effect, while dentate photo-activation's effect recovers. The claims were written from the NIH author manuscript (PMC6212318) as Europe PMC text with the legends and two supplement files, without a PDF, so values drawn only in the figures could not be read; the paper links no code. Of 45 claims only those on ALM and on behaviour in the recording sessions could be tested. Reproduced are `fig1g-fastigial-activation-delay-errors` (0.873 against 0.630, p < 0.0001), the early sample and dentate no-effect claims (dentate p = 0.108, on 3 of the paper's 8 mice), `fig1h-fastigial-activation-delay-bias`, `fig2-alm-selective-fraction` (800 of 1082, 0.739, at the edge of 0.738 to 0.902), `fig3f-alm-selectivity-abolished-by-cn-inhibition` (in 15 of 20 draws of the preference trials in the last 500 ms), `fig4e-fastigial-activation-abolishes-alm-selectivity`, `fig4f-fastigial-effect-persists` (13.1% against 1% by chance), `fig4i-cd-control-separation` and `fig4i-fastigial-collapses-cd` (reading (b), difference -8.119). Partial are `fig1k-inhibition-delay-bias`, where CD12 and CD13 drop on the same trial type and CD16 is not in the dataset; fig2cd, whose response epoch maximum appears only when the response epoch fixes the preference; fig3e-alm-mean-rate, where the absence of a change holds by the unpaired test (p = 0.214, paired p = 0.022) and the rates miss; fig3e-alm-increase-decrease (158 and 112 against 108 and 89, fraction 0.585); fig4 latency (2.07 ms by bin start, 162 of 557 modulated against 227); and cd-captures-selectivity (62.1% of the selectivity, 34.2% of the variance against 27.0 +/- 4.2). Not reproduced are fig3d (676 neurons, 270 modulated against 197 +/- 19.7, latency 14.37 ms against 7.1 +/- 3.8), `fig4g-dentate-effect-recovers` (3.4% to 5.3% of neurons stay significant from 1 s after offset) and `ed10d-fastigial-endpoints-no-prediction` (slope 0.420, p = 0.0049). The author's first run had 12 reproduced, 4 partially, 2 not reproduced and 27 blocked. The author asked no questions of a reader, so the answer and author-answers runs changed nothing. Round 1 held that the files hold more putative pyramidal units than the paper, that fig3f passed on one random draw, that the cd-captures outcome rested on a variant, that fig2cd selected and measured neurons on the same trials, and that five sessions failing the clock check were kept; in reply the units table columns and file groups were printed, fig3f was repeated over 20 draws, a split-half variant was added to fig2cd, a run without the five sessions changed no outcome, and a bug was found: 120 trials of BAYLORCD8 20171020 lie after its recording ends and had counted as silent. Round 2 found the two record errors on cd-captures-selectivity and the missing assumption on fig3e-alm-mean-rate, loose numbers in the photo_stim_id finding, two findings without printed output, and that the claims file's E3 paraphrase drops "preparatory activity", which went to `questions/gao-2018.yaml`. The notebook ran in 465 s at first, with peak memory about 0.5 GB and the run taking about 50 of its 300 minutes, 320 s after the author-answers run and round 1 and 7.3 min after round 2; nothing failed.

The dandiset holds only the ALM recordings, 54 sessions in 13 mice: the CN recordings (878 units in 18 mice and 60 units in 2 L7-cre x Ai32 mice), lick times, the behaviour-only sessions (lesions, 1.3 s and response epoch photo-activation, 0.5 s and response epoch photo-inhibition), the VGAT-ChR2-EYFP experiments and the anatomy are not in it, so 26 of the 45 claims cannot be tested. photo_stim_id has no description and the files hold no laser trace; from the ALM response codes 1 and 3 are read as early sample and 2 and 4 as early delay photo-activation, 5 and 6 as delay photo-inhibition, and which of 5 and 6 is 1.5 mW and which 4.5 mW cannot be told, nor when the photostimulus starts relative to pole_out_time. The files hold 1082 putative pyramidal neurons in the 9 photo-activation mice (557 fastigial, 525 dentate) against the paper's 912 (446 and 466), and 676 in 20 sessions of the 4 photo-inhibition mice against 454 in 19; the units table has no quality or isolation field, nothing says which units or session the paper left out, and 195 of the 676 fire under 0.5 spikes/s in the delay, so the counts and rate levels of fig3d, fig3e and fig4 depend on a selection the files do not record. The descriptions of pole_in_time, pole_out_time and cue_time say they are relative to the trial start, while the values are on the session clock. The files place the manipulated CN of CD12 and CD13 on the left, the side of the recorded ALM, where Supplemental Table 1 gives the right CN and the Methods say ALM was always recorded contralaterally, and CD14 is recorded in the left ALM in the files and the right in the table. Subjects anm00314746, anm00314756, anm00314757, anm00314758 and anm00314760 are AN105 to AN109 in the paper, and only anm00314756 (AN106) and anm00314757 (AN107) can be matched by site; the wild-type genotype is "unknown" and session_description is empty. The cell_type column labels 60 units "pyramidal" whose waveform is narrower than the paper's 0.45 ms (33 under 0.35 ms), and the waveforms are stated at 20 kHz in every file, including the 34 sessions with the 32-channel probe, which the Methods say were sampled at 25 kHz. In 5 of 54 sessions the response to delay photostimulation could not be shown to be locked to the trial events. In BAYLORCD8 20171020 the units' observation intervals end at 7221.8 s and the last 127 of 462 trials, from 7223.1 to 8481.4 s, hold no spike, which obs_intervals records. Questions are put to the paper's authors: which epoch and how many trials fix each neuron's preferred trial type in Fig. 2c, how a latency bin is labelled and whether a pre-onset baseline is subtracted, and how the fractions captured by the cd are computed, as only one combination of the readings matches both numbers.

The author's points on the protocol: it does not say how to judge a claim only half of whose data exist, as fig2cd covers ALM and CN; its rule to judge the fraction where the dataset holds fewer neurons does not cover a dataset that holds more; a shared method that names a detail as open falls between the rule for readings a criterion lists and the rule for readings of a method detail; link claims cover only outside data, so it has no form for inferring undocumented codes such as photo_stim_id from the data; and it does not say whether recording sessions may stand in for the paper's behaviour sessions.

**summaries/gao-2018-01.md**

In this data the paper's central ALM findings held up: fastigial photo-activation during the delay caused errors and collapsed ALM preparatory activity along its coding direction, and photo-inhibiting the cerebellar nuclei abolished late-delay ALM selectivity. The recordings from the cerebellar nuclei, the lesions, licking and the anatomy could not be tested, as the dataset holds only the ALM sessions. That ALM recovers after dentate photo-activation did not reproduce, as a few percent of neurons stayed altered more than 1 s later. Counts of modulated neurons and firing rate levels mostly missed, as the files hold more neurons than the paper reports and do not say which it excluded.

## End of run

14 turns, 2 minutes, $1.19 at API prices, result: success.
