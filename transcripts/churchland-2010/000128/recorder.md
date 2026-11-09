# 000128 · recorder · run 39842434275

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n '^###' docs/pilot-notes.md | tail -8; wc -l docs/pilot-notes.md; ls claims/000128 transcripts/000128; cat attempts/000128-churchland-2010-01.yaml; python tools/readme_row.py 000128; python -c "
import json;d=json.load(open('targets/dandisets.json'));
d=d if isinstance(d,list) else d.get('dandisets',d)
for e in (d if isinstance(d,list) else d.values()):
  if '000128' in json.dumps(e)[:200]: print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (34.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4cc3d7b4-34fc-4682-81ba-81eb7eb325d5/tool-results/bl4jc2gen.txt

Preview (first 2KB):
5511:### 000010, Li et al. 2015
5628:### 000691, Scherrer et al. 2023, second attempt
5750:### 001636, Pasquereau et al. 2013, second attempt
5857:### 000006, Economo et al. 2018, second attempt
5979:### 000011, Li et al. 2016
6100:### 000013, Hires et al. 2015
6220:### 000015, Chen et al. 2017
6332:### 000019, Bouchard et al. 2013
6435 docs/pilot-notes.md
claims/000128:
10.1016-j.neuron.2010.09.015.yaml

transcripts/000128:
answer-report.md
answer.md
author-answers-report.md
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 5979,6435p docs/pilot-notes.md
```

```
<persisted-output>
Output too large (31.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4cc3d7b4-34fc-4682-81ba-81eb7eb325d5/tool-results/b0xghe3ex.txt

Preview (first 2KB):
### 000011, Li et al. 2016

Six claims reproduced, five partially, nine not reproduced and eighteen
blocked, all on the dandiset. It pins version 0.220126.1907, the only
published version, as the paper cites none. The author put ten questions to a
reader, and nine of the answers were that the paper does not give the detail,
so each open detail became a set of readings under which the outcome must be
the same; the answers changed two outcomes. `cd-captures-selectivity` moved
from not reproduced to blocked as `methods_underspecified`, as the cd values
are within tolerance with all correct control trials (66.2% and 34.6%) and
outside with the training trials (73.7% to 88.0%), and `ed9f-reaction-time`
stayed blocked but moved from `methods_underspecified` to `data_missing`.
Round 1 gave its own outcome for each claim from the notebook with its
conclusions and summary removed and agreed with 34 of 38. `selective-fraction`
and `ed2b-silencing-strength` moved from partially reproduced to not
reproduced, as with lick-early trials dropped only 1 of 4 counts holds in the
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/000128-churchland-2010-01.yaml; python tools/readme_row.py 000128; grep -n -B2 -A12 '"000128"' targets/dandisets.json
```

```
<persisted-output>
Output too large (34.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4cc3d7b4-34fc-4682-81ba-81eb7eb325d5/tool-results/bid2ubq6l.txt

Preview (first 2KB):
schema_version: 2
id: 000128-churchland-2010-01
dataset:
  archive: dandi
  id: "000128"
  version: 0.220113.0400
  doi: 10.48324/dandi.000128/0.220113.0400
paper: doi:10.1016/j.neuron.2010.09.015
date: 2026-10-22
entry: 000128-churchland-2010
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
[... 32 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4cc3d7b4-34fc-4682-81ba-81eb7eb325d5/tool-results/b0xghe3ex.txt"
}
```

```
1	### 000011, Li et al. 2016
2	
3	Six claims reproduced, five partially, nine not reproduced and eighteen
4	blocked, all on the dandiset. It pins version 0.220126.1907, the only
5	published version, as the paper cites none. The author put ten questions to a
6	reader, and nine of the answers were that the paper does not give the detail,
7	so each open detail became a set of readings under which the outcome must be
8	the same; the answers changed two outcomes. `cd-captures-selectivity` moved
9	from not reproduced to blocked as `methods_underspecified`, as the cd values
10	are within tolerance with all correct control trials (66.2% and 34.6%) and
11	outside with the training trials (73.7% to 88.0%), and `ed9f-reaction-time`
12	stayed blocked but moved from `methods_underspecified` to `data_missing`.
13	Round 1 gave its own outcome for each claim from the notebook with its
14	conclusions and summary removed and agreed with 34 of 38. `selective-fraction`
15	and `ed2b-silencing-strength` moved from partially reproduced to not
16	reproduced, as with lick-early trials dropped only 1 of 4 counts holds in the
17	first and with them kept only 1 of 4 parts in the second, and
18	`cd-stable-over-epochs` moved from reproduced to blocked, since taking w from
19	all correct control trials (0.563 and 0.588) was the author's choice and the
20	training subset gives 0.534 to 0.554. The author kept
[... 438 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4cc3d7b4-34fc-4682-81ba-81eb7eb325d5/tool-results/bid2ubq6l.txt"
}
```

```
1	schema_version: 2
2	id: 000128-churchland-2010-01
3	dataset:
4	  archive: dandi
5	  id: "000128"
6	  version: 0.220113.0400
7	  doi: 10.48324/dandi.000128/0.220113.0400
8	paper: doi:10.1016/j.neuron.2010.09.015
9	date: 2026-10-22
10	entry: 000128-churchland-2010
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code (GitHub Actions)
17	    model: claude-opus-5-5
18	    protocol: pilot-10
19	  runner:
20	    platform: GitHub Actions
[... 605 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1129,1150p targets/dandisets.json; head -60 tools/readme_row.py | grep -n -i 'col\|header' ; cd transcripts/000128; wc -w *-report.md; cat author-report.md
```

```
"electrophysiological approach"
   ],
   "papers": [
    {
     "doi": "10.1016/j.neuron.2010.09.015",
     "title": "Cortical preparatory activity: representation of movement or first cog in a dynamical machine?",
     "relation": "IsDescribedBy",
     "resource_type": null,
     "preprint": false
    },
    {
     "doi": "10.1038/nature11129",
     "title": "Neural population dynamics during reaching",
     "relation": "IsDescribedBy",
     "resource_type": null,
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/000128; for f in claims-report.md claims-check-report.md answer-report.md author-answers-report.md verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
<persisted-output>
Output too large (33.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4cc3d7b4-34fc-4682-81ba-81eb7eb325d5/tool-results/bpra4hri4.txt

Preview (first 2KB):
=== claims-report.md
I wrote `claims/000128/10.1016-j.neuron.2010.09.015.yaml`. The quote checker reports 0 problems: 21 claims, 21 quotes, 9 statistical values. Nothing is committed.

**Text read.** I read the accepted author manuscript from PubMed Central (PMC2991102, NIHMS240235): Results, Methods, figure legends, and the one supplement file. That file holds Supplemental Figures 1 to 5, the Supplemental Text and the Supplemental Experimental Procedures. No PDF of the main text was supplied, so I saw only the figure legends, not the figures. The paper links no code (it only says the regressions were done in Matlab), so no code was read, and every method in the file is cited to the Methods, a legend or the supplement.

**Data.** The dataset's title on the archive points to the maze-task array recordings from monkey J ("J-array": 146 units, 108 conditions, no EMG). The claims on the speed task (monkeys A and B), the single-electrode J recordings and EMG are written as the paper reports them, and are blocked if the dataset does not hold those data.

**Counts.**
- **Claims:** 21, all with quotes; none needed `inferred`.
- **Criteria:** all 21 have one; 2 are simulations of the paper's model.
- **Expected numbers:** 8 claims have them.
- **Statistics:** 9 entries in 4 claims:
  - the mean tuning correlation per dataset (p = 0.01, 0.01, 0.12, 0.03);
  - the regression on anterior-posterior (AP) location (four r and p values);
  - the Figure 6E asterisks (p < 0.001).

[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/4cc3d7b4-34fc-4682-81ba-81eb7eb325d5/tool-results/bpra4hri4.txt"
}
```

```
1	=== claims-report.md
2	I wrote `claims/000128/10.1016-j.neuron.2010.09.015.yaml`. The quote checker reports 0 problems: 21 claims, 21 quotes, 9 statistical values. Nothing is committed.
3	
4	**Text read.** I read the accepted author manuscript from PubMed Central (PMC2991102, NIHMS240235): Results, Methods, figure legends, and the one supplement file. That file holds Supplemental Figures 1 to 5, the Supplemental Text and the Supplemental Experimental Procedures. No PDF of the main text was supplied, so I saw only the figure legends, not the figures. The paper links no code (it only says the regressions were done in Matlab), so no code was read, and every method in the file is cited to the Methods, a legend or the supplement.
5	
6	**Data.** The dataset's title on the archive points to the maze-task array recordings from monkey J ("J-array": 146 units, 108 conditions, no EMG). The claims on the speed task (monkeys A and B), the single-electrode J recordings and EMG are written as the paper reports them, and are blocked if the dataset does not hold those data.
7	
8	**Counts.**
9	- **Claims:** 21, all with quotes; none needed `inferred`.
10	- **Criteria:** all 21 have one; 2 are simulations of the paper's model.
11	- **Expected numbers:** 8 claims have them.
12	- **Statistics:** 9 entries in 4 claims:
13	  - the mean tuning correlation per dataset (p = 0.01, 0.01, 0.12, 0.03);
14	  - the regression on anterior-posterior (AP) location (four r and p values);
15	  - the Figure 6E asterisks (p < 0.001).
16	
17	**Details the paper leaves open, with the readings named:**
18	- **Trial selection:** the reference "proto-trial" and how the two velocity components are compared. Readings: the condition-mean velocity with each component at r > 0.9, or the components concatenated.
19	- **Movement onset:** the paper never says how it was detected. The file uses the onset marked in the dataset; if there is none, that step is open.
20	- **"Spikes/s of tuning" for neuron inclusion:** t
[... 266 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -40 claims/000128/*.yaml; grep -n 'title\|journal' claims/000128/*.yaml | head
```

```
# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset
# 000128.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, protocol
# pilot-10 as stated in docs/protocol.md.
#
# Text read: the accepted author manuscript in PubMed Central (PMC2991102, NIHMS240235), full text
# with Results, Methods and figure legends, and its supplement (NIHMS240235-supplement-01.pdf,
# Supplemental Figures 1 to 5 with legends, Supplemental Text and Supplemental Experimental
# Procedures), as extracted under paper/. The version of record and the main figures were not seen,
# only their legends; no PDF of the main text was supplied.
#
# Code: the paper links no code and names no repository (it says only that regressions were done in
# Matlab). No code was read. Every method below is from the Methods, the legends or the supplement.
#
# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
# Procedures). Three adult male rhesus monkeys (A, B, J, about 10 kg) made delayed reaches on a
# fronto-parallel screen; hand tracked optically at 60 Hz (0.35 mm), eye at 240 Hz. A trial is a
# touch-spot hold of at least 400 ms, target onset (the target jitters, 2 mm SD), a delay of about 0
# to 1000 ms, then the go cue (jitter stops, touch spot disappears) and the reach. Four datasets.
# - Monkeys A and B, speed task, single electrodes; 7 directions x 2 distances x 2 instructed speeds
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A3 '^  statement:\|^- id:' claims/000128/*.yaml | head -120
```

```
111:- id: recordings-jarray
112:  statement: The J-array dataset holds 146 single- and multi-unit isolations from two 96-electrode
113-    arrays, recorded on the maze task with 108 conditions, with a mean of 2166 trials per neuron.
114-  source: Results, Behavior and recordings, paragraph 1; Methods, Neural recordings and datasets
115-  quote: (27 and 108 conditions for ‘monkey J’ and ‘monkey J-array’ datasets) ... a pair of implanted
--
133:- id: recordings-single-electrode
134:  statement: The single-electrode datasets hold 64, 74 and 172 single units for monkeys A, B and J,
135-    with means of 311, 492 and 388 trials per neuron.
136-  source: Results, Behavior and recordings, paragraph 1; Supplemental Experimental Procedures, Neural
137-    and EMG recordings
--
162:- id: fig2b-example-concordant-tuning
163:  statement: In the speed task one example neuron keeps its preparatory preference (reaches up and
164-    left) into the peri-movement epoch, with a preparatory to peri-movement tuning correlation of
165-    0.72.
166-  source: Results, Neural responses during preparation and movement, paragraph 2; Figure 2B
--
181:- id: fig2ce-example-opposing-tuning
182:  statement: Three other speed-task neurons with clear preparatory tuning do not keep their
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd  tail -c 300 docs/pilot-notes.md | od -c | tail -3; cat >> docs/pilot-notes.md <<'EOF'

### 000128, Churchland et al. 2010

Eleven claims reproduced, one partially, three not reproduced and seven
blocked, all on the dandiset. It pins version 0.220113.0400, the only
published version, whose draft holds the same two files with identical
contents. The claims were written from the PubMed Central author manuscript
and its supplement, without a PDF of the main text, so the main figures were
read from their legends; the claims check added
`fig4-no-separate-populations`, so the file has 22 claims. The author put three
questions to a reader, and the answers set aside the proto-trial reading T1
(which kept 73.8% of trials with delay over 400 ms and left two conditions
empty) and the tuning measure S2 (which selected no neuron for the correlation
claims), and named two readings of the normalising maximum in
`suppfig1-population-averages`, both already run. The counts moved from 7, 1, 2
and 12 to 11, 1, 3 and 7: `fig3-maze-most-not-maintained`,
`fig6-peri-movement-space-best`, `fig6-each-dimensionality` and
`fig7a-shuffled-space-poor` moved from blocked as `methods_underspecified` to
reproduced, and `fig6-performance-vs-dimensionality` to not reproduced. Round 1
gave its own outcome for each claim from the notebook with its conclusions and
summary removed and agreed with all 22, and round 2 agreed with all 22, so
there was no third round. The paper, "Cortical preparatory activity:
representation of movement or first cog in a dynamical machine?" in Neuron,
records units in PMd and M1 of three monkeys making delayed reaches in a speed
task and a maze task, with single electrodes and, for monkey J, two
96-electrode arrays, and reports that preparatory and peri-movement tuning are
only weakly correlated and that preparatory tuning is best captured by a
preferred direction in the space of the population's peri-movement response.
Only the J-array maze session could be tested: its counts, the tuning
correlations and their time course, the population averages, the PD spaces,
the controls and the two model simulations. The speed task, single-electrode
and EMG claims are blocked as `data_missing`, and the two anterior-posterior
claims as `metadata_insufficient`. `fig4d-mean-correlation-jarray` is not
reproduced because the mean r is 0.051 and the mean Spearman r 0.072 against
0.13 and 0.11, with no test below p = 0.05 (P1 0.47, P2 0.42, P3 0.61),
`fig6-performance-vs-dimensionality` because performance rises to its best at
k = 14 (0.518) and does not decline, and `prep-dimensionality` because 90% of
the variance needs 15 components (N1) or 18 (N2) against 7 to 11; the main
text says "at least 7-10 dimensions", which 15 and 18 would meet, and whether
the claim is a range or a lower bound is asked in a question. Some outcomes
rest on weak ground: the correlation claims use only 17 neurons that pass the
selection, so their tests have little power; fig3 rests on one neuron, unit
1581 (r 0.765), with the next largest r 0.457; the best k in the PD analyses
is the upper end of the tested range, an edge value and not a peak; the
preparatory separation in suppfig1 is positive by construction; and
`fig8-model-weak-correlation` has a criterion that almost any small value
would pass.

The dandiset holds only the J-array session of monkey Jenkins (2009-09-25),
with no speed task, no single-electrode recordings and no EMG, and the paper
names no other archive for them. Every unit's electrode reference points into
the first 96 rows of the electrodes table, labelled PMd, so by the file all
182 units are in PMd although the electrode groups describe one array in M1
and one in PMd; the reference equals the unit id's channel digits minus one,
which suggests the array offset was dropped in conversion. The electrodes have
no coordinates (x, y and z are NaN), and the leading digit of the unit ids (1
for 92 units, 2 for 90), which may be the array, is not documented, so no unit
can be placed on the anterior-posterior axis or on an array; regressing tuning
correlation on that digit, a variant that decides nothing, gives r of
magnitude 0.432 (p 0.084). The dataset holds 182 units where the paper reports
146 and does not record which units or trials the paper used, or that this
session is the paper's. 574 of the session's successful trials are in the test
file as 0.7 s segments around movement onset, without condition labels or
behaviour and with only the 137 held-in units, so they cannot enter a
condition-mean analysis; the test file has a clock of its own and no delay or
success column, and the train file's trial ids are contiguous, so the files do
not record which session trials the packaging dropped. Reading (a) of
`recordings-jarray` gives 2869 trials with the test file and 2295 without it,
and the 182 units fail under every reading. Other findings: 14 trials have a
negative delay (as low as -3 ms), where the go cue precedes the recorded
target onset.

The notebook ran in 152 s in the first run, 81 s after the answers and 121 s
after round 1, and `entry.py all` passed with 0 errors after round 2. A bug
found during development averaged an empty condition as zero rates and had
made fig4d look reproduced (mean r 0.117); with the fix it is not reproduced.
Round 1's points led to a table labelled by reading for `recordings-jarray`, a
per-neuron table for fig4d, the lost fig6-each-dimensionality comparison (the
2-D initial-velocity space, 0.238 against 0.223) printed, and checks of the
test file's clock and the electrode group descriptions. Round 2 withdrew its
round-1 point that the supplement's T-matrix might be a conditions by
(neurons by times) matrix, as the supplement defines it as c by n, so those
variants were removed; it also found statements the outputs did not support,
among them both fig4d means called below half the paper's where the Spearman
mean is 65% of it, the fig8 interval given as its outer envelope, an ambiguous
"91% of trials kept" for T2, and notes quoting T1 and S2 values the notebook
no longer prints, and these were corrected. Untracked dotfiles in the
repository root that the author did not create were left alone. The author's
points on the protocol: it does not cover a reading that selects no units; it
does not say what to do when a trial reading leaves a condition with no
trials; it has no rule for an undocumented substitute such as the unit-id
digit when the claims file's fallback, the array, is wrong in the data; its
check for a selection is written only for chance levels and false-positive
rates, though the paper's "~90% kept" works like one; the `recordings-jarray`
criterion says only when the claim is reproduced, not when it is partial; and
some details the criteria leave open below their stated readings were run both
ways and recorded as deviations.
EOF
grep -c '—\|rather' <(tail -90 docs/pilot-notes.md)
```

```
0000420   p   r   e   -   e   p   o   c   h       l   e   v   e   l   "
0000440       u   n   d   e   f   i   n   e   d   .  \n
0000454
0
```

**Agent**

I added the subsection for 000128 at the end of `docs/pilot-notes.md`. Nothing is committed. The `catalystneuro` field for 000128 is empty, so the second paragraph does not open with the conversion sentence. The run went normally, with no failed step and no third round. The text contains no em dashes and does not use "rather".

### 000128, Churchland et al. 2010

Eleven claims reproduced, one partially, three not reproduced and seven
blocked, all on the dandiset. It pins version 0.220113.0400, the only
published version, whose draft holds the same two files with identical
contents. The claims were written from the PubMed Central author manuscript
and its supplement, without a PDF of the main text, so the main figures were
read from their legends; the claims check added
`fig4-no-separate-populations`, so the file has 22 claims. The author put three
questions to a reader, and the answers set aside the proto-trial reading T1
(which kept 73.8% of trials with delay over 400 ms and left two conditions
empty) and the tuning measure S2 (which selected no neuron for the correlation
claims), and named two readings of the normalising maximum in
`suppfig1-population-averages`, both already run. The counts moved from 7, 1, 2
and 12 to 11, 1, 3 and 7: `fig3-maze-most-not-maintained`,
`fig6-peri-movement-space-best`, `fig6-each-dimensionality` and
`fig7a-shuffled-space-poor` moved from blocked as `methods_underspecified` to
reproduced, and `fig6-performance-vs-dimensionality` to not reproduced. Round 1
gave its own outcome for each claim from the notebook with its conclusions and
summary removed and agreed with all 22, and round 2 agreed with all 22, so
there was no third round. The paper, "Cortical preparatory activity:
representation of movement or first cog in a dynamical machine?" in Neuron,
records units in PMd and M1 of three monkeys making delayed reaches in a speed
task and a maze task, with single electrodes and, for monkey J, two
96-electrode arrays, and reports that preparatory and peri-movement tuning are
only weakly correlated and that preparatory tuning is best captured by a
preferred direction in the space of the population's peri-movement response.
Only the J-array maze session could be tested: its counts, the tuning
correlations and their time course, the population averages, the PD spaces,
the controls and the two model simulations. The speed task, single-electrode
and EMG claims are blocked as `data_missing`, and the two anterior-posterior
claims as `metadata_insufficient`. `fig4d-mean-correlation-jarray` is not
reproduced because the mean r is 0.051 and the mean Spearman r 0.072 against
0.13 and 0.11, with no test below p = 0.05 (P1 0.47, P2 0.42, P3 0.61),
`fig6-performance-vs-dimensionality` because performance rises to its best at
k = 14 (0.518) and does not decline, and `prep-dimensionality` because 90% of
the variance needs 15 components (N1) or 18 (N2) against 7 to 11; the main
text says "at least 7-10 dimensions", which 15 and 18 would meet, and whether
the claim is a range or a lower bound is asked in a question. Some outcomes
rest on weak ground: the correlation claims use only 17 neurons that pass the
selection, so their tests have little power; fig3 rests on one neuron, unit
1581 (r 0.765), with the next largest r 0.457; the best k in the PD analyses
is the upper end of the tested range, an edge value and not a peak; the
preparatory separation in suppfig1 is positive by construction; and
`fig8-model-weak-correlation` has a criterion that almost any small value
would pass.

The dandiset holds only the J-array session of monkey Jenkins (2009-09-25),
with no speed task, no single-electrode recordings and no EMG, and the paper
names no other archive for them. Every unit's electrode reference points into
the first 96 rows of the electrodes table, labelled PMd, so by the file all
182 units are in PMd although the electrode groups describe one array in M1
and one in PMd; the reference equals the unit id's channel digits minus one,
which suggests the array offset was dropped in conversion. The electrodes have
no coordinates (x, y and z are NaN), and the leading digit of the unit ids (1
for 92 units, 2 for 90), which may be the array, is not documented, so no unit
can be placed on the anterior-posterior axis or on an array; regressing tuning
correlation on that digit, a variant that decides nothing, gives r of
magnitude 0.432 (p 0.084). The dataset holds 182 units where the paper reports
146 and does not record which units or trials the paper used, or that this
session is the paper's. 574 of the session's successful trials are in the test
file as 0.7 s segments around movement onset, without condition labels or
behaviour and with only the 137 held-in units, so they cannot enter a
condition-mean analysis; the test file has a clock of its own and no delay or
success column, and the train file's trial ids are contiguous, so the files do
not record which session trials the packaging dropped. Reading (a) of
`recordings-jarray` gives 2869 trials with the test file and 2295 without it,
and the 182 units fail under every reading. Other findings: 14 trials have a
negative delay (as low as -3 ms), where the go cue precedes the recorded
target onset.

The notebook ran in 152 s in the first run, 81 s after the answers and 121 s
after round 1, and `entry.py all` passed with 0 errors after round 2. A bug
found during development averaged an empty condition as zero rates and had
made fig4d look reproduced (mean r 0.117); with the fix it is not reproduced.
Round 1's points led to a table labelled by reading for `recordings-jarray`, a
per-neuron table for fig4d, the lost fig6-each-dimensionality comparison (the
2-D initial-velocity space, 0.238 against 0.223) printed, and checks of the
test file's clock and the electrode group descriptions. Round 2 withdrew its
round-1 point that the supplement's T-matrix might be a conditions by
(neurons by times) matrix, as the supplement defines it as c by n, so those
variants were removed; it also found statements the outputs did not support,
among them both fig4d means called below half the paper's where the Spearman
mean is 65% of it, the fig8 interval given as its outer envelope, an ambiguous
"91% of trials kept" for T2, and notes quoting T1 and S2 values the notebook
no longer prints, and these were corrected. Untracked dotfiles in the
repository root that the author did not create were left alone. The author's
points on the protocol: it does not cover a reading that selects no units; it
does not say what to do when a trial reading leaves a condition with no
trials; it has no rule for an undocumented substitute such as the unit-id
digit when the claims file's fallback, the array, is wrong in the data; its
check for a selection is written only for chance levels and false-positive
rates, though the paper's "~90% kept" works like one; the `recordings-jarray`
criterion says only when the claim is reproduced, not when it is partial; and
some details the criteria leave open below their stated readings were run both
ways and recorded as deviations.

## End of run

12 turns, 1 minutes, result: success.
