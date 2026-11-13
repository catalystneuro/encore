# park-2019 · recorder · run 43392870785

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; ls transcripts/park-2019/; python tools/readme_row.py park-2019; ls docs/pilot-notes | grep park
```

```
docs/pilot-notes/amjad-2025-01.md
docs/pilot-notes/armstrong-2026-01.md
docs/pilot-notes/ashworth-2025-01.md
docs/pilot-notes/athalye-2023-01.md
docs/pilot-notes/azcorra-2023-01.md
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
claims-report.md
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd docs/pilot-notes; for f in amjad-2025-01 armstrong-2026-01 ashworth-2025-01 athalye-2023-01 azcorra-2023-01 knierim-2000-02 park-2019-01; do echo "=== $f"; cat $f.md; done; cd ../..; grep -n -B3 "readme_row\|^| Dataset\|^|---" README.md | head -20; ls summaries | head
```

```
<persisted-output>
Output too large (44.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7a96dc10-e4ee-468f-bf97-d95620e31f3e/tool-results/bzft0lt9i.txt

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
cat attempts/park-2019-02.yaml; cat claims/park-2019.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
import sys
items = d if isinstance(d,list) else d.get('dandisets', d)
for x in (items if isinstance(items,list) else items.values()):
    if 'hc-20' in json.dumps(x): print(json.dumps(x,indent=1))
"; cat summaries/park-2019-01.md 2>/dev/null
```

```
<persisted-output>
Output too large (106.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7a96dc10-e4ee-468f-bf97-d95620e31f3e/tool-results/bw3v0pe8u.txt

Preview (first 2KB):
schema_version: 3
id: park-2019-02
datasets:
- archive: crcns
  id: hc-20
  version: unversioned
  doi: 10.6080/K0SF2TDN
  relation: primary
paper: doi:10.1016/j.neuron.2018.11.019
date: 2026-11-13
entry: park-2019
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 33 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7a96dc10-e4ee-468f-bf97-d95620e31f3e/tool-results/bzft0lt9i.txt"
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
[... 633 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7a96dc10-e4ee-468f-bf97-d95620e31f3e/tool-results/bw3v0pe8u.txt"
}
```

```
1	schema_version: 3
2	id: park-2019-02
3	datasets:
4	- archive: crcns
5	  id: hc-20
6	  version: unversioned
7	  doi: 10.6080/K0SF2TDN
8	  relation: primary
9	paper: doi:10.1016/j.neuron.2018.11.019
10	date: 2026-11-13
11	entry: park-2019
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-14
20	  runner:
[... 838 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7a96dc10-e4ee-468f-bf97-d95620e31f3e/tool-results/bw3v0pe8u.txt",
 "offset": 859,
 "limit": 300
}
```

```
859	    reason: Agrees as it stands.
860	    response: No change.
861	  - claim: no-angular-velocity-tuning
862	    agrees: true
863	    outcome: not_reproduced
864	    reason: The claims file's test, now with shift controls, is stated and reasonable; the shift
865	      tests keep the excess, so it does not come from treating samples as independent.
866	    response: No change.
867	  - claim: fig4-internal-tuning-preserved
868	    agrees: true
869	    outcome: not_reproduced
870	    reason: Agrees as it stands. Round-1 point resolved, the rescaled KLD variant was added and the
871	      (b) reading still passes, instability p = 0.052. The README says the notebook takes about
872	      seven minutes, four and a half of them for the internally referenced tuning; cell 59 prints
873	      306 s (5.1 min), and the notebook prints no total runtime.
874	    response: The notebook now prints its total run time at the end, and the README gives the times
875	      of recent runs (6.1 to 7.3 min in total, 270 to 313 s for the internally referenced tuning) as
876	      six to eight minutes, about five of them for that step.
877	  - claim: fig4c-arena-registration-short-lived
878	    agrees: false
[... 280 more lines not kept]
```

**Agent**

Read the record and claims. Now checking the target entry, the column meaning, and the reports.

**Agent calls Bash**

```bash
sed -n 1,60p tools/readme_row.py; python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
s=json.dumps(d)
i=s.find('hc-20'); print(s[max(0,i-800):i+800])
E
cd transcripts/park-2019; ls -la --time-style=full-iso; git log --format='%h %ad %s' --date=iso -- . | head -20; head -5 *-report.md
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
[... 161 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "hc-20" targets/dandisets.json; cd transcripts/park-2019; for f in author answer author-answers verifier-1 author-revise-1 verifier-2 author-revise-2 reconcile; do echo "=== $f"; cat $f-report.md; done
```

```
<persisted-output>
Output too large (39.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/7a96dc10-e4ee-468f-bf97-d95620e31f3e/tool-results/b60y5b9br.txt

Preview (first 2KB):
0
=== author
I've finished the attempt and run `tools/entry.py handover`. The entry is at `entries/park-2019/` (`reproduce_park_2019.ipynb` and `hd20.py`), the record at `attempts/park-2019-02.yaml`, and `tools/entry.py all` passes with 0 errors. I didn't verify it myself, and I didn't come across any earlier attempt's results.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| cell-counts | partially reproduced: 115 head-direction units from 13 rats as in the paper; the 353 MEC cells and 556 pairs are not in the data |
| hd-cell-rate | reproduced (1.392 AP/s) |
| fig1a-avoidance-learning | blocked, data_missing |
| fig1c-speed | reproduced |
| fig1c-lfp-power | blocked, data_missing |
| fig1c-firing-rate | reproduced (F(1.35, 154.10) = 1.76, p = 0.18) |
| fig1c-directionality | partially reproduced: rotating room frame not below stable2 at p < 0.01 (p = 0.055) |
| fig1d-preference-change | partially reproduced: stable1-arena change is the largest, where the legend puts it lowest |
[... 17 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/7a96dc10-e4ee-468f-bf97-d95620e31f3e/tool-results/b60y5b9br.txt"
}
```

```
1	0
2	=== author
3	I've finished the attempt and run `tools/entry.py handover`. The entry is at `entries/park-2019/` (`reproduce_park_2019.ipynb` and `hd20.py`), the record at `attempts/park-2019-02.yaml`, and `tools/entry.py all` passes with 0 errors. I didn't verify it myself, and I didn't come across any earlier attempt's results.
4	
5	**(1) Outcomes**
6	
7	| Claim | Outcome |
8	|---|---|
9	| cell-counts | partially reproduced: 115 head-direction units from 13 rats as in the paper; the 353 MEC cells and 556 pairs are not in the data |
10	| hd-cell-rate | reproduced (1.392 AP/s) |
11	| fig1a-avoidance-learning | blocked, data_missing |
12	| fig1c-speed | reproduced |
13	| fig1c-lfp-power | blocked, data_missing |
14	| fig1c-firing-rate | reproduced (F(1.35, 154.10) = 1.76, p = 0.18) |
15	| fig1c-directionality | partially reproduced: rotating room frame not below stable2 at p < 0.01 (p = 0.055) |
16	| fig1d-preference-change | partially reproduced: stable1-arena change is the largest, where the legend puts it lowest |
17	| fig1d-instability | partially reproduced: 2 of 3 trial pairs exceed the stable1 halves |
18	| fig2-decoding-stable-vs-rotating | reproduced (assumed) |
19	| figs2-frame-preference | reproduced under 1 of 16 readings (assumed) |
20	| fig2c-proximity-anticorrelation | partially reproduced: mean r −0.05 to −0.09, against −0.141 |
[... 325 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/park-2019.yaml'))
for c in d['claims']: print(c['id'],'|',c['statement'],'|',c['source'][:80]);print()
"
```

```
cell-counts | The paper analyses 115 dorsal MEC head-direction cells from 13 rats, among 353 MEC cells forming 556 cell pairs (Table S1), out of 1594 MEC single units recorded. | Results, Degraded Directional Tuning, paragraph 1; STAR Methods, Electrophysiolo

hd-cell-rate | The head-direction cells have long-duration spikes and a mean firing rate of 1.41 ± 0.20 AP/s. | STAR Methods, Data Analysis, paragraph 2

fig1a-avoidance-learning | The 13 recorded rats learned the place avoidance task, with performance improving over trials in the stable (baseline) and the rotating (challenge) conditions and no trial by frame interaction in the rotating condition. | Figure 1A legend; Results, Degraded Directional Tuning, paragraph 1

fig1c-speed | Rotation did not change locomotor speed relative to stable1, measured in either frame, but speed was lower in stable2 than in the other conditions. | Figure 1C, top left, and its legend

fig1c-lfp-power | Power in the MEC local field potential did not differ across conditions. | Figure 1C, top right, and its legend; Results, Degraded Directional Tuning, para

fig1c-firing-rate | Firing rates of the head-direction cells were maintained across stable1, rotating and stable2. | Figure 1C, bottom left, and its legend

fig1c-directionality | Directional tuning of head-direction cells was strongly degraded during rotation in both frames, more in the arena frame than in the room frame, and returned in stable2 (stable1 = stable2 > rotating room frame > rotating arena frame). | Figure 1C, bottom right, and its legend; Results, Degraded Directional Tuning, p

fig1d-preference-change | The change in preferred direction differs across trial pairs (stable1-stable2 = stable1-rotating room frame > stable1-rotating arena frame), and is greater for every trial pair than between the two halves of stable1. | Figure 1D, left, and its legend; Results, Degraded Directional Tuning, paragraph

fig1d-instability | Directional instability (the KLD between tuni
[... 26 more lines not kept]
```

**Agent**

Writing the notes file now.

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/park-2019-02.md",
 "content": "# park-2019, Park et al. 2019, second attempt\n\nNine claims reproduced (five on an assumption), five partially (one on an\nassumption), three not reproduced (two on an assumption) and five blocked for\nmissing data. Round 1 agreed with 21 of the 22 outcomes as they stood, and\n`fig4c-arena-registration-short-lived` moved from partially to not reproduced\nas it proposed; round 2 agreed with 19 as they stood and asked that\n`fig1d-instability`, `figs3-no-head-direction-bias` and fig4c state the\nreadings they rest on, which was done with no change of outcome, so there was\nno third round. CRCNS hc-20 has no versions, so the record pins `unversioned`\nand the notebook checks the MD5 of data.zip. The paper, Park, Keeley, Savin,\nRanck and Fenton in Neuron, records head-direction cells in the medial\nentorhinal cortex (MEC) of rats doing place avoidance in a stable, a rotating\n(arena at 1 rpm) and a second stable trial, and reports that directional\ntuning degrades during rotation, alternating between the room and arena frames\nwith the rat's proximity to the two shock zones, while the temporal coupling of\ncell pairs and their internally referenced tuning are preserved. The dataset\nholds the 115 head-direction cells and their 30 Hz tracks; the learning\ncurves, the LFP and the claims on all MEC cells and the Gaussian process model\n(Figures S4 to S6) are blocked. Reproduced are `hd-cell-rate` (1.392 AP/s\nagainst 1.41 ± 0.20), `fig1c-speed`, `fig1c-firing-rate` (p = 0.184, though log\nrates give p = 0.0015) and `fig3-hd-pair-correlations-preserved` (146 pairs, p\n= 0.907, 0.72 and 0.617 at 40, 250 and 1000 ms), and on an assumption\n`fig1c-directionality` (Tukey HSD on the repeated-measures error term; between\ngroups stable2 against room gives p = 0.055), `fig2-decoding-stable-vs-rotating`\n(4 of 7 ensembles, the claims file's majority rule), `figs2-frame-preference`\n(4 room and 2 arena under 1 of 16 readings), `figs3-no-head-direction-bias`\n(average r 0.166 and no test of 14 significant with n the sum of the weights)\nand `fig5c-error-minima-at-cues` (105 and 345 degrees under 1 of 32\ncombinations, which the record calls weak support). Not reproduced are\n`fig4-internal-tuning-preserved` (instability differs across trial pairs, p =\n5.3e-05), fig4c (the conditions differ at 10 s under some readings and the\narena frame falls below the others only from 50 or 60 s; read as any interval\nbeyond 10 s it would be partial) and `no-angular-velocity-tuning` (12 of 115\ncells, binomial p = 0.013, with correlations of at most 0.068). Partial are\n`cell-counts`, the two Figure 1D claims, `fig2c-proximity-anticorrelation`\n(mean r -0.043 to -0.087 over 24 readings, none within tolerance) and\n`fig5-error-inhomogeneous` (the tests hold in 75 of 80 combinations, at most\ntwo of four r within tolerance). The author's first run gave nine reproduced,\neight partially, one not reproduced and five blocked, with no question to a\nreader; the answer run found the questions file missing from the branch,\ncopied it from main and answered park-2019-01's two questions, amending the\nfig5 criterion to three readings, which left that outcome partial, and leaving\nfigs3 as it stood. Round 1 also led to a Tukey test on the repeated-measures\nerror term, which moved `fig1c-directionality` from partially reproduced to\nreproduced, to edge and angle distances for fig2c and shift controls for the\nangular velocity test, and to a reader question on the order in the Figure 1D\nlegend. In the second revision the author found that window directions on a\n10 degree bin edge fell in different bins between runs and fixed it by\nrounding; no outcome changed. The attempt was not blind: the copied questions\nfile and the first attempt's transcripts, left in `transcripts/park-2019/`,\nshowed it park-2019-01's results, and the second revision read that attempt's\nround 3 report. Against park-2019-01 only figs3 changed, from not reproduced,\nas the two take a different n for the weighted Rayleigh test (both find one of\n14 tests below 0.05 with n the number of bins), and all twelve earlier\nfindings are still present. The author's run took about 57 minutes, and the\nnotebook ran in about 350 s at first, 257 s after the answer and 427 s after\nround 1.\n\nThe dataset holds only the 115 head-direction cells: the other MEC cells (353\ncells and 556 pairs in Table S1, 921 modelled cells in Figures S5 and S6), the\nLFP, the waveforms and the pretraining and training sessions are not in it. In\nsessions 1009R029, 1015R029, 1023R029 and 1025R029 the room-frame and\narena-frame tracks of the rotating trial disagree in distance from the arena\ncentre (median 6.85 to 13.49 px at the best constant lag, against 0.31 px for\nthe .dat files) and fall behind the room .dat track by 705 to at least 1500\nsamples in the room frame and 354 to 828 in the arena frame at sample 48000,\nso the spikes cannot be aligned with both frames. Stable2 of 1015R029 and\n1025R029, and the room-frame rotating trial of 1211R039 and 1212R039, carry\nidentical tracking with different spikes, and the stable1 file of unit\n1024R157-P9C1 holds the same 2919 spikes as its rotating files.\nFileNameList.xlsx shifts the stable2 column of 1121R157 by one row for five\nunits; the header of 1017SA2R035-cl.P11C2Rm states 2000 samples/s and a first\ntimestamp of 5; the stable2 file 1121SA2R157-cl1.P11C2Rm holds 26,954 samples\n(15 min); the spike times of 1020RAR157-cl.P11C1 decrease once, by 1.5 ms; and\none tracker file is named for R024 in a session of R027. The data descriptor\ndoes not describe untracked samples (direction 4294967295, 4 to 73% of a\nfile's samples) or the y-up convention of the shock zone angles, nor that\nspike times run ahead of the nominal sample times by up to about 3 s within a\ntrial. Per rat the counts match Table S1 except R029 (40 against 41) and R523\n(2 against 1), two units fire above the paper's 10 AP/s limit (13.8 and 11.9\nAP/s), and the units form 146 pairs against the paper's 142. The paper gives a\n660 ms decoding window in the STAR Methods and 133 ms in the Figure 2 legend,\nand an arena-frame error z of 289.63 in the Results against 153.24 and 230.58\nin the Figure 5 legend. Questions are put to the paper's authors on how Idir,\nthe 2 SD rule and the no-preference margin are defined, how relative proximity\nis defined, what n the Figure S3 Rayleigh test uses, which error term the\nTukey-Kramer tests use, which normalisation, strength measure and window side\nthe internally referenced tuning uses, and which windows Figure 5 pools.\n\nThe author's points on the protocol: for a claim of absence it says to judge\non the paper's test alone, while the figs3 criterion lists two readings of\nthat test, handled as an assumption under step 1.6; criteria that reproduce\n\"under any reading\" can pass on 1 of 16 or 1 of 32 readings (figs2, fig5c),\nwhich were marked assumed with the counts given; some results fit neither a\ncriterion's full nor its partial form and were recorded as partially\nreproduced; the schema requires `deviations` on every assumed outcome, which\nthe protocol does not say; and `measured` cannot hold values for counts the\ndataset lacks, so the counts it holds were given.\n"
}
```

```
File created successfully at: docs/pilot-notes/park-2019-02.md (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/park-2019-02.md",
 "old_string": "gave nine reproduced,\neight partially, one not reproduced and five blocked",
 "new_string": "gave eight reproduced,\nseven partially, two not reproduced and five blocked"
}
```

```
The file docs/pilot-notes/park-2019-02.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "docs/pilot-notes/park-2019-02.md",
 "old_string": "257 s after the answer and 427 s after\nround 1.",
 "new_string": "257 s in the author-answers run and 427 s\nafter round 1."
}
```

```
The file docs/pilot-notes/park-2019-02.md has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "summaries/park-2019-02.md",
 "content": "In this data the paper's core result holds: head-direction tuning in medial entorhinal cortex degrades during arena rotation, while firing rates and the sub-second coupling of cell pairs are preserved. The preservation of internally referenced tuning in cell pairs did not reproduce, nor did its short-lived registration to the arena frame; the Methods and the paper's code normalise this tuning differently, and the record asks which was used. The link between frame-specific directional information and proximity to the shock zones, and the structure of decoding errors, were weaker than reported. Learning, LFP and the analyses of all MEC cells could not be tested, as only the 115 head-direction cells are deposited.\n"
}
```

```
File created successfully at: summaries/park-2019-02.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
wc -w summaries/park-2019-02.md docs/pilot-notes/park-2019-02.md; grep -c "—\|rather" summaries/park-2019-02.md docs/pilot-notes/park-2019-02.md; git status --short
```

```
111 summaries/park-2019-02.md
1184 docs/pilot-notes/park-2019-02.md
1295 total
summaries/park-2019-02.md:0
docs/pilot-notes/park-2019-02.md:0
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
?? docs/pilot-notes/park-2019-02.md
?? scripts
?? summaries/park-2019-02.md
```

**Agent**

I wrote both files and committed nothing. The summary is 111 words. Several untracked files were already in the repository root (`.bashrc`, `.idea`, `scripts` and others); I did not create them and left them alone. `targets/dandisets.json` has no entry for CRCNS hc-20, so the notes do not open with a CatalystNeuro sentence.

`docs/pilot-notes/park-2019-02.md`:

# park-2019, Park et al. 2019, second attempt

Nine claims reproduced (five on an assumption), five partially (one on an assumption), three not reproduced (two on an assumption) and five blocked for missing data. Round 1 agreed with 21 of the 22 outcomes as they stood, and `fig4c-arena-registration-short-lived` moved from partially to not reproduced as it proposed; round 2 agreed with 19 as they stood and asked that `fig1d-instability`, `figs3-no-head-direction-bias` and fig4c state the readings they rest on, which was done with no change of outcome, so there was no third round. CRCNS hc-20 has no versions, so the record pins `unversioned` and the notebook checks the MD5 of data.zip. The paper, Park, Keeley, Savin, Ranck and Fenton in Neuron, records head-direction cells in the medial entorhinal cortex (MEC) of rats doing place avoidance in a stable, a rotating (arena at 1 rpm) and a second stable trial, and reports that directional tuning degrades during rotation, alternating between the room and arena frames with the rat's proximity to the two shock zones, while the temporal coupling of cell pairs and their internally referenced tuning are preserved. The dataset holds the 115 head-direction cells and their 30 Hz tracks; the learning curves, the LFP and the claims on all MEC cells and the Gaussian process model (Figures S4 to S6) are blocked. Reproduced are `hd-cell-rate` (1.392 AP/s against 1.41 ± 0.20), `fig1c-speed`, `fig1c-firing-rate` (p = 0.184, though log rates give p = 0.0015) and `fig3-hd-pair-correlations-preserved` (146 pairs, p = 0.907, 0.72 and 0.617 at 40, 250 and 1000 ms), and on an assumption `fig1c-directionality` (Tukey HSD on the repeated-measures error term; between groups stable2 against room gives p = 0.055), `fig2-decoding-stable-vs-rotating` (4 of 7 ensembles, the claims file's majority rule), `figs2-frame-preference` (4 room and 2 arena under 1 of 16 readings), `figs3-no-head-direction-bias` (average r 0.166 and no test of 14 significant with n the sum of the weights) and `fig5c-error-minima-at-cues` (105 and 345 degrees under 1 of 32 combinations, which the record calls weak support). Not reproduced are `fig4-internal-tuning-preserved` (instability differs across trial pairs, p = 5.3e-05), fig4c (the conditions differ at 10 s under some readings and the arena frame falls below the others only from 50 or 60 s; read as any interval beyond 10 s it would be partial) and `no-angular-velocity-tuning` (12 of 115 cells, binomial p = 0.013, with correlations of at most 0.068). Partial are `cell-counts`, the two Figure 1D claims, `fig2c-proximity-anticorrelation` (mean r -0.043 to -0.087 over 24 readings, none within tolerance) and `fig5-error-inhomogeneous` (the tests hold in 75 of 80 combinations, at most two of four r within tolerance). The author's first run gave eight reproduced, seven partially, two not reproduced and five blocked, with no question to a reader; the answer run found the questions file missing from the branch, copied it from main and answered park-2019-01's two questions, amending the fig5 criterion to three readings, which left that outcome partial, and leaving figs3 as it stood. Round 1 also led to a Tukey test on the repeated-measures error term, which moved `fig1c-directionality` from partially reproduced to reproduced, to edge and angle distances for fig2c and shift controls for the angular velocity test, and to a reader question on the order in the Figure 1D legend. In the second revision the author found that window directions on a 10 degree bin edge fell in different bins between runs and fixed it by rounding; no outcome changed. The attempt was not blind: the copied questions file and the first attempt's transcripts, left in `transcripts/park-2019/`, showed it park-2019-01's results, and the second revision read that attempt's round 3 report. Against park-2019-01 only figs3 changed, from not reproduced, as the two take a different n for the weighted Rayleigh test (both find one of 14 tests below 0.05 with n the number of bins), and all twelve earlier findings are still present. The author's run took about 57 minutes, and the notebook ran in about 350 s at first, 257 s in the author-answers run and 427 s after round 1.

The dataset holds only the 115 head-direction cells: the other MEC cells (353 cells and 556 pairs in Table S1, 921 modelled cells in Figures S5 and S6), the LFP, the waveforms and the pretraining and training sessions are not in it. In sessions 1009R029, 1015R029, 1023R029 and 1025R029 the room-frame and arena-frame tracks of the rotating trial disagree in distance from the arena centre (median 6.85 to 13.49 px at the best constant lag, against 0.31 px for the .dat files) and fall behind the room .dat track by 705 to at least 1500 samples in the room frame and 354 to 828 in the arena frame at sample 48000, so the spikes cannot be aligned with both frames. Stable2 of 1015R029 and 1025R029, and the room-frame rotating trial of 1211R039 and 1212R039, carry identical tracking with different spikes, and the stable1 file of unit 1024R157-P9C1 holds the same 2919 spikes as its rotating files. FileNameList.xlsx shifts the stable2 column of 1121R157 by one row for five units; the header of 1017SA2R035-cl.P11C2Rm states 2000 samples/s and a first timestamp of 5; the stable2 file 1121SA2R157-cl1.P11C2Rm holds 26,954 samples (15 min); the spike times of 1020RAR157-cl.P11C1 decrease once, by 1.5 ms; and one tracker file is named for R024 in a session of R027. The data descriptor does not describe untracked samples (direction 4294967295, 4 to 73% of a file's samples) or the y-up convention of the shock zone angles, nor that spike times run ahead of the nominal sample times by up to about 3 s within a trial. Per rat the counts match Table S1 except R029 (40 against 41) and R523 (2 against 1), two units fire above the paper's 10 AP/s limit (13.8 and 11.9 AP/s), and the units form 146 pairs against the paper's 142. The paper gives a 660 ms decoding window in the STAR Methods and 133 ms in the Figure 2 legend, and an arena-frame error z of 289.63 in the Results against 153.24 and 230.58 in the Figure 5 legend. Questions are put to the paper's authors on how Idir, the 2 SD rule and the no-preference margin are defined, how relative proximity is defined, what n the Figure S3 Rayleigh test uses, which error term the Tukey-Kramer tests use, which normalisation, strength measure and window side the internally referenced tuning uses, and which windows Figure 5 pools.

The author's points on the protocol: for a claim of absence it says to judge on the paper's test alone, while the figs3 criterion lists two readings of that test, handled as an assumption under step 1.6; criteria that reproduce "under any reading" can pass on 1 of 16 or 1 of 32 readings (figs2, fig5c), which were marked assumed with the counts given; some results fit neither a criterion's full nor its partial form and were recorded as partially reproduced; the schema requires `deviations` on every assumed outcome, which the protocol does not say; and `measured` cannot hold values for counts the dataset lacks, so the counts it holds were given.

`summaries/park-2019-02.md`:

In this data the paper's core result holds: head-direction tuning in medial entorhinal cortex degrades during arena rotation, while firing rates and the sub-second coupling of cell pairs are preserved. The preservation of internally referenced tuning in cell pairs did not reproduce, nor did its short-lived registration to the arena frame; the Methods and the paper's code normalise this tuning differently, and the record asks which was used. The link between frame-specific directional information and proximity to the shock zones, and the structure of decoding errors, were weaker than reported. Learning, LFP and the analyses of all MEC cells could not be tested, as only the 115 head-direction cells are deposited.

## End of run

16 turns, 2 minutes, $1.17 at API prices, result: success.
