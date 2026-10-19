# 001550 · recorder · run 39196937856

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
python tools/readme_row.py 001550 --write; git diff; ls claims/001550 transcripts/001550; cat attempts/001550-pagan-2025-01.yaml; python -c "import json;d=json.load(open('targets/dandisets.json'));e=[x for x in (d if isinstance(d,list) else d.get('dandisets',d.values())) if '001550' in json.dumps(x)];print(json.dumps(e,indent=1))"
```

```
<persisted-output>
Output too large (222.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/f52251da-00bf-4210-9f19-a2602e1d5fd4/tool-results/bq805xiqv.txt

Preview (first 2KB):
diff --git a/README.md b/README.md
index eaf309e..0f3b914 100644
--- a/README.md
+++ b/README.md
@@ -97,6 +97,7 @@ please [open an issue](https://github.com/catalystneuro/reproduction-registry/is
 | [001172](https://dandiarchive.org/dandiset/001172) | [Lohani et al. 2022](https://doi.org/10.1038/s41593-022-01202-6) | 13 | 7 | 1 | 5 | [`001172-lohani-2022`](entries/001172-lohani-2022) |
 | [001528](https://dandiarchive.org/dandiset/001528) | [Hadjas et al. 2025](https://doi.org/10.1101/2025.06.03.657460) | 12 | 5 | 3 | 5 | [`001528-hadjas-2025`](entries/001528-hadjas-2025) |
 | [001538](https://dandiarchive.org/dandiset/001538) | [Zhai et al. 2025](https://doi.org/10.1126/sciadv.adv8224) | 15 (+1) | 0 (+2) | 3 (+1) | 15 | [`001538-zhai-2025`](entries/001538-zhai-2025) |
+| [001550](https://dandiarchive.org/dandiset/001550) | [Pagan et al. 2025](https://doi.org/10.1038/s41586-024-08433-6) | 11 (+2) | 2 | 0 (+1) | 0 | [`001550-pagan-2025`](entries/001550-pagan-2025) |
 
 Counts are of claims that rest on the dandiset, including those that take
 names for its own codes from elsewhere. Claims that also use data from
claims/001550:
10.1038-s41586-024-08433-6.yaml

transcripts/001550:
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,200p /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/f52251da-00bf-4210-9f19-a2602e1d5fd4/tool-results/bq805xiqv.txt | tail -n +20; grep -n "README" README.md | head -0; sed -n 85,96p README.md
```

```
author-revise-2-report.md
author-revise-2.md
author.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
verifier-2.md
schema_version: 1
id: 001550-pagan-2025-01
dandiset: "001550"
dandiset_version: 0.260916.0811
paper: doi:10.1038/s41586-024-08433-6
date: 2026-10-18
entry: 001550-pagan-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
[... 173 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,420p /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/f52251da-00bf-4210-9f19-a2602e1d5fd4/tool-results/bq805xiqv.txt; sed -n 60,84p README.md
```

```
r = 0.092, p = 0.717; from the paper's saved weights r = 0.094, p = 0.71.
  deviations:
  - The paper gives no test; a two-sided Pearson correlation was chosen before the analysis.
- claim: ed3g-halfsplit
  outcome: reproduced
  notebook: reproduce_pagan_2025.ipynb
  output: claim:ed3g-halfsplit
  measured: 0.552
  notes: Over 24 rats and 48 values r = 0.552 (95% CI 0.318 to 0.723), p = 4.7e-05, within 0.522
    to 0.638. With the fixed penalty r = 0.577, p = 1.8e-05. Location alone r = 0.470, frequency
    alone r = 0.736.
  deviations:
  - The halves use the penalty weight chosen on all of that rat's trials in that context.
- claim: ed4-bilateral-fof-impairs
  outcome: partially_reproduced
  notebook: reproduce_pagan_2025.ipynb
  output: claim:ed4-bilateral-fof-impairs
  notes: Four rats have opto sessions (P116 47, P124 74, P127 4 and P131 88 with at least 100
    valid trials). With bilateral full-trial epochs accuracy is lower than on control trials in
    the same sessions with p < 0.05 in 2 of the 3 rats with most sessions, P116 (0.639 against
[... 226 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 420,700p /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/f52251da-00bf-4210-9f19-a2602e1d5fd4/tool-results/bq805xiqv.txt; grep -n "Reproduced\|^| Dandiset" README.md | head; sed -n '/^Counts are of claims/,/^$/p' README.md
```

```
agree). Outcome unchanged.
  - claim: subjects
    agrees: true
    outcome: partially_reproduced
    reason: 26 subjects, all male, all Long Evans; only 0.913 of selected sessions fall in 5.4 to 26.4 months
      (minimum 3.0, maximum 39.1). 18 rats have selected sessions below 5.4 months, and the date_of_birth
      metadata is never checked for plausibility, for example against the age at the first session.
    response: Added each rat's date of birth and its age at the first session in the dandiset, the first
      TaskSwitch session and the first selected session. 25 rats are 1.6 to 2.7 months old at their first
      session, which supports the young ages; P189 is 14.1 months old at its first session, which falls on
      P187's first day, and its date of birth may be a year early. Conclusion, notes and the finding updated.
      Outcome unchanged.
  - claim: trials-per-session
    agrees: true
    outcome: reproduced
    reason: Valid trials per selected session average 551.8, and per task session 494.2, both inside 487.8 to
      596.2. Readings c and d leave out the 13 unreadable sessions, a negligible effect.
    response: Added readings c and d with the 13 unreadable sessions included (749.1 and 493.8). Outcome
      unchanged.
  - claim: blocks-per-session
[... 267 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^### " docs/pilot-notes.md | tail -6; python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
def walk(x):
    if isinstance(x,dict):
        if any(str(v)=="001550" for v in x.values()): print(json.dumps(x,indent=1)); return
        for v in x.values(): walk(v)
    elif isinstance(x,list):
        for v in x: walk(v)
walk(d)
E
```

```
3328:### 001075, Randi et al. 2023
3423:### 001084, Vu et al. 2024
3523:### 001170, Ling et al. 2023
3633:### 001172, Lohani et al. 2022
3722:### 001528, Hadjas et al. 2025
3803:### 001538, Zhai et al. 2025
{
 "dandiset": "001550",
 "name": "Individual variability of neural computations underlying flexible decisions",
 "published_version": "0.260916.0811",
 "asset_count": 16115,
 "size_gb": 20.94,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Rattus norvegicus - Norway rat"
 ],
 "approaches": [],
 "papers": [
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes.md",
 "offset": 3423
}
```

```
3423	### 001084, Vu et al. 2024
3424	
3425	Ten claims reproduced, ten partially and one blocked on the dandiset, none
3426	not reproduced. With outside data, counted apart: one reproduced. Four claims
3427	on data in other archives are blocked. Round 1 gave its own outcome for each
3428	claim from the notebook with its conclusions removed and agreed with all 26,
3429	giving `data_missing` as the reason for the five blocked claims; the author
3430	kept `other` (not attempted) for the four whose data are on Zenodo, and changed
3431	`figs3-targeting-errors` to `data_missing` after a new data check showed that
3432	no file's fiber table holds a planned target and the paper's code reads the
3433	targets from calibration files in none of the Zenodo archives. After round 1
3434	the author also added variants that rank AP and the response within each mouse
3435	and permute within mice, under which the light amplitude gradient (r = 0.152,
3436	p = 0.013) and the light and tone latency gradients (r = -0.223, p = 0.0014;
3437	r = 0.214, p = 0.003) remain, and a refit of DL18 with its 14 tones of 12 kHz
3438	identified from the paper's published results. Round 2 agreed with all 26 and
3439	nothing was proposed, so there was no third round. The paper records D1 SPN
3440	calcium and dopamine release through micro-fiber arrays across the mouse
3441	striatum, and reports that light and tone evoke dopamine release with distinct
3442	spatial patterns and latency gradients, and that stimulating dopamine axons
[... 459 more lines not kept]
```

**Agent**

The README row is written: 11 (+2) reproduced, 2 partially, 0 (+1) not reproduced, 0 blocked. Now I'll read the reports and the claims file.

**Agent calls Bash**

```bash
cd transcripts/001550; wc -l *-report.md; cat author-report.md
```

```
63 author-report.md
   20 author-revise-1-report.md
   19 author-revise-2-report.md
   55 verifier-1-report.md
   46 verifier-2-report.md
  203 total
I did steps 1 to 6 for dandiset 001550 against Pagan et al. 2025 (doi:10.1038/s41586-024-08433-6). I used the open-access full text (PMC11903320, CC BY), saved under `paper/`. I pinned version 0.260916.0811 because the paper cites no DANDI version and this is the only published one. The entry passes `check` with 0 errors and runs in 642 s; the handover is in `executed/001550-pagan-2025/handover/`. Nothing is committed.

**1. Outcomes**

| Claim | Data | Outcome |
|---|---|---|
| session-link | with inputs | reproduced |
| subjects (26 male Long-Evans, 6–24 months) | dandiset | partially reproduced |
| trials-per-session (542) | dandiset | reproduced (2 of 4 readings) |
| blocks-per-session (14.6) | dandiset | reproduced (2 of 4 readings) |
| session-duration (2–4 h) | dandiset | reproduced |
| block-min-30 | dandiset | reproduced |
| fig1c-20-rats | dandiset | reproduced |
| fig1c-context-selection | dandiset | reproduced |
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001550; for f in verifier-1-report.md author-revise-1-report.md verifier-2-report.md author-revise-2-report.md; do echo "=== $f"; cat $f; done
```

```
=== verifier-1-report.md
**A. Outcome per claim** (23 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| session-link | reproduced | Cells 11–12: 0.9999 of the paper's sessions with valid trials are in the dandiset (one missing, P189 TaskSwitch6-210516a). Valid-trial count and fraction correct are equal in all 15,277 matched sessions. In the 20-session sample, the per-trial fields and position in block agree on 100% of trials and the 10 ms pulse bins on 99.996%. Per-rat counts match `numsessions_all_rats` for 23 of 26 rats; the 3 differences are explained by 6 extra dandiset sessions and 1 session where the selection differs. |
| subjects | partially_reproduced | Cells 3 and 14: 26 subjects, all male, all Long Evans. Only 0.913 of selected sessions fall in 5.4–26.4 months (minimum age 3.0, maximum 39.1), which is ≥0.90 but below "every session". |
| trials-per-session | reproduced | Cell 16: valid trials per selected session average 551.8, and per task session 494.2. Both are inside 487.8–596.2. |
| blocks-per-session | reproduced | Cell 16: blocks over all task sessions average 13.90, and switches over selected sessions 15.98. Both are inside 13.14–16.06. |
| session-duration | reproduced | Cell 16: median 2.50 h (selected) and 2.57 h (all), inside 1.8–4.4 h. Only about 56% of sessions last 2–4 h. |
| block-min-30 | reproduced | Cell 19: 100% of non-final blocks have ≥30 trials when all trials are counted (81.7% when only valid trials are counted). |
| fig1c-20-rats | reproduced | Cell 21: exactly 20 rats have more than 120,000 valid trials in selected sessions. |
| fig1c-context-selection | reproduced | Cell 22: in all 20 rats both relative weights are above 0.5; the lowest is 0.724. |
| ed1e-switch-four-trials | reproduced | Cell 24 (main selection): at position 4 the relevant weight reaches 0.91 of plateau for one switch direction and 0.963 for the other, so both pass the 0.9 threshold. The margin is thin: the 0.91 is the switch from freque
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -nE "^\s*(- )?id:|^\s*data:|corrected" claims/001550/*.yaml | head -60; head -40 claims/001550/*.yaml
```

```
50:- id: session-link
55:  data: with_inputs
67:- id: subjects
79:- id: trials-per-session
90:- id: blocks-per-session
101:- id: session-duration
109:- id: block-min-30
119:- id: fig1c-20-rats
128:- id: fig1c-context-selection
138:- id: ed1e-switch-four-trials
152:- id: ed2g-learning-2-5-months
162:- id: fig4-converging
172:- id: fig4-loc-frq-uncorrelated
182:- id: ed3g-halfsplit
196:- id: ed4-bilateral-fof-impairs
208:- id: neural-link
213:  data: with_inputs
223:- id: units-per-rat
227:  data: elsewhere
244:- id: fig3h-neural-uncorrelated
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -nA4 "statement:" claims/001550/*.yaml | head -150
```

```
51:  statement: The dandiset's sessions can be linked to the paper's published per-session
52-    behavioural tables, and the linked records agree on trial counts, outcomes, evidence and
53-    pulse timing.
54-  source: Data availability; the paper's data/Sessions_trials at GitHub commit 0ea8fdb
55-  data: with_inputs
--
68:  statement: The study used 26 male Long-Evans rats, aged between 6 and 24 months.
69-  source: Methods, Subjects
70-  expected:
71-  - quantity: number of rats
72-    value: 26
--
80:  statement: Rats performed on average 542 trials per session.
81-  source: Methods, Behaviour
82-  expected:
83-    quantity: mean trials per session
84-    value: 542
--
91:  statement: On average, rats switched across 14.6 context blocks per session.
92-  source: Methods, Behaviour
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> docs/pilot-notes.md <<'EOF'

### 001550, Pagan et al. 2025

Eleven claims reproduced and two partially on the dandiset, none not
reproduced or blocked. With outside data, counted apart: two reproduced and
one not reproduced. Seven claims on the paper's neural data and RNNs in its
GitHub repositories: two reproduced, one not reproduced and four blocked.
Round 1 gave its own outcome for each claim from the notebook with its
conclusions removed and agreed with all 23, giving `other` as the reason for
the three blocks the author gave as `not_runnable`; the author kept
`not_runnable` and round 2 accepted it. Round 1 also found that the port of
`ExtDataFigure5ag.m` took the full-space angle, which the code computes first
and overwrites, and not the projected, folded angle the code plots; with the
plotted angle `choice-axes-parallel` went from a mean of 40.34 to 4.73
degrees, still outside 1.44 to 1.76, and its criterion was corrected after
round 1 and again after round 2. Round 2 agreed with all 23 and nothing was
proposed, so there was no third round. The paper studies rats that weigh
pulses by location or by frequency depending on a context that switches in
blocks, and reports that rats switch within about four trials, that their
differential behavioural kernels mostly converge with shapes that vary across
rats, and that behavioural and neural slope indices from FOF and mPFC are
anti-correlated across rats, as in RNNs engineered across the solution space.
The link to the paper's per-session tables, the subjects, trials, blocks and
durations, the 20 rats of Figure 1c and their context selection, switching
and learning times, the behavioural kernels and their half-split reliability,
bilateral FOF silencing, the link of the paper's units to dandiset sessions,
the unit counts, the neural slope indices, the choice axis angle and the
correlation of Figure 5d were tested. `fig1e-choice-axis` is blocked as
`methods_underspecified`, as `Figure1e.m` computes neither 81.3% nor 73.3%,
and the mTDR claim and the two RNN claims as `not_runnable`, as they need
MATLAB or 1,000 trained RNNs. `neural-link` is not reproduced: 2,371 of 3,495
cells (0.678) match one session as a contiguous run, from 110 sessions
against 199. Some outcomes rest on weak ground: `fig5d-behaviour-neural`
gives r = -0.697 against a tolerance of -0.803 to -0.657 and depends on P049
and P059, whose Methods selection keeps 23,014 and 25,847 trials; with those
two rats from the code's selection r = -0.834, and leaving out one rat at a
time gives -0.655 to -0.895, inside the tolerance for 4 of 7; in
`ed1e-switch-four-trials` the switch to location reaches 0.9 of its plateau
at position 4 in 0.678 of bootstrap resamples, while position 5 is firm; and
`trials-per-session`, `blocks-per-session` and `ed2g-learning-2-5-months`
match on two, two and three of four readings. The author used the full text
in PubMed Central (PMC11903320), took method choices from the paper's code at
commit 0ea8fdb and used its fitted per-neuron kernels without refitting them
from spikes.

The dandiset was converted by CatalystNeuro
(https://github.com/catalystneuro/pagan-lab-to-nwb). It holds only the
behaviour; the electrophysiology behind Figures 1d to 1f, 3h and 5d (3,495
units from 7 rats) is public only in the paper's GitHub repository, as one
MATLAB file per unit with binned spike counts, without raw data or spike
sorting output. Nothing links the units to dandiset sessions: matched by
trial sequence, 3,269 units fall in exactly one session when gaps are allowed
(2,371 without), from 112 sessions where the paper reports 199, and 226 match
none; searching every TaskSwitch protocol gives 3,349 units from 115
sessions, and 146 unmatched. The behaviour matches the paper's tables
closely: 15,277 of its 15,278 sessions with valid trials are in the
dandiset, and in the 14,650 with a per-trial record in the paper's tables
the 7,447,692 valid trials agree on every per-trial field, with 0.99996 of
50 ms pulse bins agreeing. The missing session, P189 TaskSwitch6-210516a with
27 valid trials, is listed in the conversion's notes among aborted sessions
left out, and six P187 and P189 sessions are in the dandiset but not in the
paper's tables, five of them passing the selection and adding 1,442 and 609
trials. Relative weights agree to 1e-6 in 0.898 of sessions, 861 more agree
once capped at 1, and 60 differ with both values present, not explained.
Every optogenetic epoch gives a wavelength of 473 nm, where Extended Data
Figure 4 says 450 nm and the conversion's documentation says the value was
corrected to 450, and epochs are present for four rats (P116, P124, P127,
P131) where the paper reports three, with nothing saying which three. The
dates of birth give ages of 3.0 to 39.1 months at the selected sessions (18
rats younger than 5.4 months at some), where the Methods state 6 to 24; they
put 25 rats at 1.6 to 2.7 months at their first session, and P189's
(2018-02-21) puts it at 14.1 months on the day P187, born 2019-02-21, starts,
and may be a year early. Other findings: thirteen task sessions (1 to 3
trials each) lack HistorySection_result_history or a pulse column, and 95 of
the other 15,400 lack HistorySection_hit_history; HistorySection_gammafreq_history,
a signed strength, is stored as uint8 or int16 in 570 files, with no values
lost; the paper's code requires a per-session `good` flag the Methods do not
describe and the dandiset does not hold, caps relative weights at 1, uses a
fixed penalty of 200 on neighbouring weight differences where the Methods
describe ridge regression with a cross-validated regulariser, and uses looser
selections (0.65 correct and 0.6 index) for Figure 5d and Extended Data
Figure 1e; the paper's own angle code on its own per-context kernels gives
1.1 to 8.0 degrees (mean 4.7), not 1.6, and the permutation test the Methods
describe is not in the code; the Methods put 3,495 units in FOF from 5 rats
while the FOF counts sum to 3,285; the main text calls a converging kernel a
slope index above 0, while the Methods and code give it a negative index, as
the data have; and three neural location slope indices are negative (P049
-0.221, P101 -0.045, P095 -0.007) where the Methods say only positive or zero.

The notebook ran in 642 s in the first clean run, 419 s after round 1 and 856
s after round 2. While preparing, listing assets with one URL call each took 8
minutes and was replaced by one paginated listing (4 s), partial remote reads
took 110 minutes because h5py serialises the reads, so each file was read
whole into memory, sessions lacking columns were skipped by the loader, and
the gh CLI had no token, so the repositories were cloned over HTTPS. Round 2
found statements the outputs did not support, among them a one to one link
with identical trial fields, relative weights equal to the paper's, P127 "not
lower" at 0.603 against 0.634, a README run time of about 7 minutes, and that
the Methods describe no test of the angle against 0, and these were
corrected. The author's points on the protocol: a paper repository that
duplicates the dandiset's behaviour, which the data kinds do not foresee;
fitted per-neuron kernels used in place of refitting the GLM from spikes; a
dependent claim that needs only the match of neurons to rats when its link
claim fails on sessions; a link criterion requiring contiguous trials that
proved too strict; the Methods' "ridge" read as the code's neighbour-difference
penalty; whether reading whole files into memory counts as streaming;
criteria written after the data check had shown the answer; whether
`not_runnable` covers MATLAB code that could in principle be ported; and which
value to record when several readings in two dimensions match.
EOF
grep -c "—" docs/pilot-notes.md; tail -c 300 docs/pilot-notes.md | grep -i rather; git status --short
```

```
0
 M README.md
 M docs/pilot-notes.md
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
?? scripts
```

**Agent calls Bash**

```bash
sed -i 's#^(https://github.com/catalystneuro/pagan-lab-to-nwb). It holds only the$#(catalystneuro/pagan-lab-to-nwb). It holds only the#' docs/pilot-notes.md; sed -n '/^### 001550/,$p' docs/pilot-notes.md | grep -ci rather; sed -n '/^### 001550/,$p' docs/pilot-notes.md | sed -n 46,50p
```

```
0
(catalystneuro/pagan-lab-to-nwb). It holds only the
behaviour; the electrophysiology behind Figures 1d to 1f, 3h and 5d (3,495
units from 7 rats) is public only in the paper's GitHub repository, as one
MATLAB file per unit with binned spike counts, without raw data or spike
sorting output. Nothing links the units to dandiset sessions: matched by
```

**Agent**

I ran `tools/readme_row.py 001550 --write`, which added the 001550 row to README.md: 11 (+2) reproduced, 2 partially, 0 (+1) not reproduced, 0 blocked. I also added the subsection below to the end of `docs/pilot-notes.md`. Nothing is committed, and the attempt, claims and entry are unchanged. Some untracked files in the repository root (`.bashrc`, `.idea`, `scripts` and others) were already there; I did not touch them.

### 001550, Pagan et al. 2025

Eleven claims reproduced and two partially on the dandiset, none not
reproduced or blocked. With outside data, counted apart: two reproduced and
one not reproduced. Seven claims on the paper's neural data and RNNs in its
GitHub repositories: two reproduced, one not reproduced and four blocked.
Round 1 gave its own outcome for each claim from the notebook with its
conclusions removed and agreed with all 23, giving `other` as the reason for
the three blocks the author gave as `not_runnable`; the author kept
`not_runnable` and round 2 accepted it. Round 1 also found that the port of
`ExtDataFigure5ag.m` took the full-space angle, which the code computes first
and overwrites, and not the projected, folded angle the code plots; with the
plotted angle `choice-axes-parallel` went from a mean of 40.34 to 4.73
degrees, still outside 1.44 to 1.76, and its criterion was corrected after
round 1 and again after round 2. Round 2 agreed with all 23 and nothing was
proposed, so there was no third round. The paper studies rats that weigh
pulses by location or by frequency depending on a context that switches in
blocks, and reports that rats switch within about four trials, that their
differential behavioural kernels mostly converge with shapes that vary across
rats, and that behavioural and neural slope indices from FOF and mPFC are
anti-correlated across rats, as in RNNs engineered across the solution space.
The link to the paper's per-session tables, the subjects, trials, blocks and
durations, the 20 rats of Figure 1c and their context selection, switching
and learning times, the behavioural kernels and their half-split reliability,
bilateral FOF silencing, the link of the paper's units to dandiset sessions,
the unit counts, the neural slope indices, the choice axis angle and the
correlation of Figure 5d were tested. `fig1e-choice-axis` is blocked as
`methods_underspecified`, as `Figure1e.m` computes neither 81.3% nor 73.3%,
and the mTDR claim and the two RNN claims as `not_runnable`, as they need
MATLAB or 1,000 trained RNNs. `neural-link` is not reproduced: 2,371 of 3,495
cells (0.678) match one session as a contiguous run, from 110 sessions
against 199. Some outcomes rest on weak ground: `fig5d-behaviour-neural`
gives r = -0.697 against a tolerance of -0.803 to -0.657 and depends on P049
and P059, whose Methods selection keeps 23,014 and 25,847 trials; with those
two rats from the code's selection r = -0.834, and leaving out one rat at a
time gives -0.655 to -0.895, inside the tolerance for 4 of 7; in
`ed1e-switch-four-trials` the switch to location reaches 0.9 of its plateau
at position 4 in 0.678 of bootstrap resamples, while position 5 is firm; and
`trials-per-session`, `blocks-per-session` and `ed2g-learning-2-5-months`
match on two, two and three of four readings. The author used the full text
in PubMed Central (PMC11903320), took method choices from the paper's code at
commit 0ea8fdb and used its fitted per-neuron kernels without refitting them
from spikes.

The dandiset was converted by CatalystNeuro
(catalystneuro/pagan-lab-to-nwb). It holds only the
behaviour; the electrophysiology behind Figures 1d to 1f, 3h and 5d (3,495
units from 7 rats) is public only in the paper's GitHub repository, as one
MATLAB file per unit with binned spike counts, without raw data or spike
sorting output. Nothing links the units to dandiset sessions: matched by
trial sequence, 3,269 units fall in exactly one session when gaps are allowed
(2,371 without), from 112 sessions where the paper reports 199, and 226 match
none; searching every TaskSwitch protocol gives 3,349 units from 115
sessions, and 146 unmatched. The behaviour matches the paper's tables
closely: 15,277 of its 15,278 sessions with valid trials are in the
dandiset, and in the 14,650 with a per-trial record in the paper's tables
the 7,447,692 valid trials agree on every per-trial field, with 0.99996 of
50 ms pulse bins agreeing. The missing session, P189 TaskSwitch6-210516a with
27 valid trials, is listed in the conversion's notes among aborted sessions
left out, and six P187 and P189 sessions are in the dandiset but not in the
paper's tables, five of them passing the selection and adding 1,442 and 609
trials. Relative weights agree to 1e-6 in 0.898 of sessions, 861 more agree
once capped at 1, and 60 differ with both values present, not explained.
Every optogenetic epoch gives a wavelength of 473 nm, where Extended Data
Figure 4 says 450 nm and the conversion's documentation says the value was
corrected to 450, and epochs are present for four rats (P116, P124, P127,
P131) where the paper reports three, with nothing saying which three. The
dates of birth give ages of 3.0 to 39.1 months at the selected sessions (18
rats younger than 5.4 months at some), where the Methods state 6 to 24; they
put 25 rats at 1.6 to 2.7 months at their first session, and P189's
(2018-02-21) puts it at 14.1 months on the day P187, born 2019-02-21, starts,
and may be a year early. Other findings: thirteen task sessions (1 to 3
trials each) lack HistorySection_result_history or a pulse column, and 95 of
the other 15,400 lack HistorySection_hit_history; HistorySection_gammafreq_history,
a signed strength, is stored as uint8 or int16 in 570 files, with no values
lost; the paper's code requires a per-session `good` flag the Methods do not
describe and the dandiset does not hold, caps relative weights at 1, uses a
fixed penalty of 200 on neighbouring weight differences where the Methods
describe ridge regression with a cross-validated regulariser, and uses looser
selections (0.65 correct and 0.6 index) for Figure 5d and Extended Data
Figure 1e; the paper's own angle code on its own per-context kernels gives
1.1 to 8.0 degrees (mean 4.7), not 1.6, and the permutation test the Methods
describe is not in the code; the Methods put 3,495 units in FOF from 5 rats
while the FOF counts sum to 3,285; the main text calls a converging kernel a
slope index above 0, while the Methods and code give it a negative index, as
the data have; and three neural location slope indices are negative (P049
-0.221, P101 -0.045, P095 -0.007) where the Methods say only positive or zero.

The notebook ran in 642 s in the first clean run, 419 s after round 1 and 856
s after round 2. While preparing, listing assets with one URL call each took 8
minutes and was replaced by one paginated listing (4 s), partial remote reads
took 110 minutes because h5py serialises the reads, so each file was read
whole into memory, sessions lacking columns were skipped by the loader, and
the gh CLI had no token, so the repositories were cloned over HTTPS. Round 2
found statements the outputs did not support, among them a one to one link
with identical trial fields, relative weights equal to the paper's, P127 "not
lower" at 0.603 against 0.634, a README run time of about 7 minutes, and that
the Methods describe no test of the angle against 0, and these were
corrected. The author's points on the protocol: a paper repository that
duplicates the dandiset's behaviour, which the data kinds do not foresee;
fitted per-neuron kernels used in place of refitting the GLM from spikes; a
dependent claim that needs only the match of neurons to rats when its link
claim fails on sessions; a link criterion requiring contiguous trials that
proved too strict; the Methods' "ridge" read as the code's neighbour-difference
penalty; whether reading whole files into memory counts as streaming;
criteria written after the data check had shown the answer; whether
`not_runnable` covers MATLAB code that could in principle be ported; and which
value to record when several readings in two dimensions match.

## End of run

13 turns, 2 minutes, result: success.
