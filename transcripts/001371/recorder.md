# 001371 · recorder · run 41528940855

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  git log --diff-filter=A --name-only --format= -- docs/pilot-notes | head -n 5; python tools/readme_row.py 001371; ls claims/001371/ transcripts/001371/; cat attempts/001371-prince-2025-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for x in (it if isinstance(it,list) else it.values()):
  if '001371' in json.dumps(x)[:300]: print(json.dumps(x,indent=1))
"
```

```
<persisted-output>
Output too large (156.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d28aec04-3e73-4791-8697-6e5847bb0ec9/tool-results/b18rfscnl.txt

Preview (first 2KB):
docs/pilot-notes/001347-kauvar-2025-01.md
docs/pilot-notes/001444-doherty-2025-01.md
docs/pilot-notes/001474-porniece-2025-01.md
docs/pilot-notes/000939-duszkiewicz-2024-01.md
docs/pilot-notes/001350-iram-2024-01.md
| [001371](https://dandiarchive.org/dandiset/001371) | [Prince et al. 2025](https://doi.org/10.1038/s41467-025-60122-8) | 21 | 5 | 7 | 19 | [`001371-prince-2025`](entries/001371-prince-2025) |
claims/001371/:
10.1038-s41467-025-60122-8.yaml

transcripts/001371/:
answer-report.md
answer.md
author-answers-report.md
author-answers.md
author-report.md
author-revise-1-report.md
[... 51 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat docs/pilot-notes/001347-kauvar-2025-01.md docs/pilot-notes/001444-doherty-2025-01.md docs/pilot-notes/001474-porniece-2025-01.md docs/pilot-notes/000939-duszkiewicz-2024-01.md docs/pilot-notes/001350-iram-2024-01.md; cat attempts/001371-prince-2025-01.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else d[0].keys())
"
```

```
<persisted-output>
Output too large (201.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d28aec04-3e73-4791-8697-6e5847bb0ec9/tool-results/bc8uywc1k.txt

Preview (first 2KB):
# 001347, Kauvar et al. 2025

Thirty-one claims reproduced (six on an assumption), four partially, three not
reproduced (one on an assumption) and three blocked, all for missing data; the
five claims that also use inputs from the paper's code record are counted apart
and all reproduced (two on an assumption). The ten claims on the mouse
Neuropixels data in DANDI:001326 are left out of these counts: of them five
reproduced (three on an assumption), three partially (one on an assumption) and
two not reproduced (one on an assumption). The five link claims the author
added, for the labels and scores taken from the code record, all hold. The
first verification round agreed with 56 of the 61 outcomes as they stood and
the second with all 61, and nothing was proposed after the second, so there was
no third round. It pins version 0.250528.0702, the only published version; the
paper cites none. The paper, Kauvar, Richman, Liu et al., "Conserved brain-wide
emergence of emotional response from sensory experience in humans and mice" in
Science, measures reflexive (early) and affective (late) eye closure to
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d28aec04-3e73-4791-8697-6e5847bb0ec9/tool-results/bc8uywc1k.txt",
 "limit": 120
}
```

```
1	# 001347, Kauvar et al. 2025
2	
3	Thirty-one claims reproduced (six on an assumption), four partially, three not
4	reproduced (one on an assumption) and three blocked, all for missing data; the
5	five claims that also use inputs from the paper's code record are counted apart
6	and all reproduced (two on an assumption). The ten claims on the mouse
7	Neuropixels data in DANDI:001326 are left out of these counts: of them five
8	reproduced (three on an assumption), three partially (one on an assumption) and
9	two not reproduced (one on an assumption). The five link claims the author
10	added, for the labels and scores taken from the code record, all hold. The
11	first verification round agreed with 56 of the 61 outcomes as they stood and
12	the second with all 61, and nothing was proposed after the second, so there was
13	no third round. It pins version 0.250528.0702, the only published version; the
14	paper cites none. The paper, Kauvar, Richman, Liu et al., "Conserved brain-wide
15	emergence of emotional response from sensory experience in humans and mice" in
16	Science, measures reflexive (early) and affective (late) eye closure to
17	eyepuffs in 4 non-iEEG adults given saline and ketamine in a blinded crossover,
18	in 7 iEEG epilepsy patients before, during and after ketamine infusion, and in
19	head-fixed mice given ketamine and other drugs, and relates the late response
20	to NMF factors of iEEG spectrograms, Yeo networks, persistent and fast coding
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -w docs/pilot-notes/{001347-kauvar-2025-01,001444-doherty-2025-01,001474-porniece-2025-01,000939-duszkiewicz-2024-01,001350-iram-2024-01}.md; cat docs/pilot-notes/001444-doherty-2025-01.md docs/pilot-notes/001350-iram-2024-01.md
```

```
1573 docs/pilot-notes/001347-kauvar-2025-01.md
 1632 docs/pilot-notes/001444-doherty-2025-01.md
 1643 docs/pilot-notes/001474-porniece-2025-01.md
 1398 docs/pilot-notes/000939-duszkiewicz-2024-01.md
 1535 docs/pilot-notes/001350-iram-2024-01.md
 7781 total
# 001444, Doherty et al. 2025

Eighteen claims reproduced (eight on an assumption), three partially (one on an
assumption), 13 not reproduced (one on an assumption) and six blocked, two for
missing data and four as `methods_underspecified`. All 40 claims are on the
dandiset. The first verification round agreed with 33 of the 40 outcomes as
they stood and the second with 39, and because two changes of outcome were
proposed after the second, for `fig1-network-size` and
`fig2c-control-it23-rate-activated`, a third round reviewed those two claims
alone and agreed with both. It pins version 0.250805.2002, the only published
version; the paper cites none. The paper, Doherty, Chen, Smith, Wichmann, Chu
and Lytton, "Enhanced beta power emerges from simulated parkinsonian primary
motor cortex" in npj Parkinson's Disease, simulates in NetPyNE a 300 um
diameter cylinder of mouse M1 with 10,073 neurons in 15 populations, in four
[... 253 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/001371-prince-2025-01.yaml
```

```
<persisted-output>
Output too large (155.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d28aec04-3e73-4791-8697-6e5847bb0ec9/tool-results/by6mu7mjx.txt

Preview (first 2KB):
schema_version: 2
id: 001371-prince-2025-01
dataset:
  archive: dandi
  id: '001371'
  version: 0.260831.0201
  doi: 10.48324/dandi.001371/0.260831.0201
paper: doi:10.1038/s41467-025-60122-8
date: '2026-11-02'
entry: 001371-prince-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=attempts/001371-prince-2025-01.yaml; wc -l $f; grep -n '^[a-z_]*:' $f; python -c "
import yaml;d=yaml.safe_load(open('$f'))
for o in d['outcomes']: print(o['claim'],o['outcome'],o.get('assumed',''),o.get('reason',''), list(o.keys()))
"; wc -w transcripts/001371/*report.md
```

```
2210 attempts/001371-prince-2025-01.yaml
1:schema_version: 2
2:id: 001371-prince-2025-01
3:dataset:
8:paper: doi:10.1038/s41467-025-60122-8
9:date: '2026-11-02'
10:entry: 001371-prince-2025
11:provenance:
22:inputs:
27:outcomes:
1130:findings:
1190:verifications:
recordings partially_reproduced   ['claim', 'outcome', 'notebook', 'output', 'measured', 'notes']
trial-mix not_reproduced   ['claim', 'outcome', 'notebook', 'output', 'measured', 'notes']
task-timing reproduced   ['claim', 'outcome', 'notebook', 'output', 'measured', 'notes']
fig1b-above-chance reproduced   ['claim', 'outcome', 'notebook', 'output', 'measured', 'notes']
fig1b-window-performance reproduced   ['claim', 'outcome', 'notebook', 'output', 'measured', 'notes', 'deviations']
fig1d-heading-switch reproduced   ['claim', 'outcome', 'notebook', 'output', 'notes', 'deviations']
fig5a-stay-performance reproduced   ['claim', 'outcome', 'notebook', 'output', 'measured', 'notes']
tuning-tiles-track reproduced   ['claim', 'outcome', 'notebook', 'output', 'notes', 'deviations']
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001371; cat author-report.md answer-report.md author-answers-report.md
```

```
I've done steps 1 to 5 of the Author section and run the handover (step 6). The notebook runs from a clean environment in 1474 s (about 25 min). `entry.py check` reports 0 errors and the handover is in `executed/001371-prince-2025/handover/`. Nothing is committed.

## 1. Outcomes (52 claims: 19 reproduced, 6 partially, 8 not reproduced, 19 blocked)

| Claim | Outcome |
|---|---|
| task-timing, fig1b-above-chance, fig1b-window-performance, fig1d-heading-switch, fig5a-stay-performance | Reproduced |
| tuning-tiles-track, decoding-validation | Reproduced |
| fig2e-hpc-goal-increase, fig2e-hpc-arms-equal, sfig2e-goal-bias, sfig3c-retrospective-unchanged, sfig5g-ca1-more-goal-coding | Reproduced |
| fig3b-theta-pre-post, sfig6-theta-switch-over-delay, fig3d-new-arm-theta-modulated | Reproduced |
| sfig10-stay-transient-new-arm, fig6b-hpc-new-lower-incorrect, fig6b-hpc-initial-no-difference, fig6-hpc-pre-cue-initial-higher-incorrect | Reproduced |
| recordings, sfig3ab-original-vs-update-cue, sfig2f-all-trials-encoder, sfig5f-pfc-wider-spread, fig5d-stay-hpc-below-switch, fig7c-hpc-commitment-new-arm | Partially reproduced |
| trial-mix, sfig3c-goals-over-retrospective, fig2g-pfc-no-goal-increase, sfig5e-pfc-windows, fig3c-theta-phase-segregation, fig5d-stay-hpc-like-delay, sfig12-delay-hpc-no-outcome-difference, fig7c-hpc-commitment-initial-arm | Not reproduced |
| fig4a-lstm-choice-estimate and the 18 claims that decode its output | Blocked, `too_large` |

Several of the "not reproduced" results are claims that an effect is absent, where one test lands just under 0.05 (for example p = 0.043 and 0.032).

## 2. Dataset, assumptions, questions

**Version.** I pinned 0.260831.0201, the only published version. The paper cites none.
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001371; cat verifier-1-report.md author-revise-1-report.md
```

```
**Prince et al. 2025 (DANDI:001371) — verifier report, round 1**

The claims file has 52 claims. The notebook tests 33 and blocks 19 (all the LSTM and choice-decoding claims). Under my reading of the outputs: 20 reproduced, 7 partially reproduced, 6 not reproduced, 19 blocked.

### A. Outcomes

| claim | outcome | reason |
|---|---|---|
| recordings | partially_reproduced | 7 animals and 66 sessions match. CA1 has 3545 units (3892 ± 389, within). PFC has 2271 (2557 ± 256, outside). 633 units in 5 sessions have no region label. The all-unit total, 6449, equals the paper's exactly (cells 3, 9). |
| trial-mix | not_reproduced | Pooled fractions are 0.737 / 0.189 / 0.074 and per-session means 0.750 / 0.181 / 0.069, all outside tolerance. The counts 7172 / 1840 / 717 equal the paper's own counts (cell 11). |
| task-timing | reproduced | Under readings (c) all trials and (a) t_delay2 to choice: 10.559, 1.403, 6.020 (switch; 6.06 pooled with stay), 21.00 and 20.88 s, all within tolerance (cell 13). |
| fig1b-above-chance | reproduced | Session reading: W = 125.5 and 48.5 equal the paper's values. p = 6.1e-10 and 3.3e-11. Means 0.649 and 0.745 (cell 15). |
| fig1b-window-performance | reproduced | With 15-trial windows the window counts are 6252 and 1002, exactly the paper's n. Means and medians are 0.678 / 0.667 and 0.775 / 0.800 (cell 17). |
| fig5a-stay-performance | reproduced | 15-trial windows: n = 117, as in the paper; mean 0.921, median 0.933 (cell 19). |
| fig1d-heading-switch | reproduced | On both sides, switch trials point toward the initial side at the cue bin (+0.198, +0.183) and toward the new side in the last bin (−0.318, −0.154). Delay only trials stay toward the initial side (+0.197, +0.217) (cell 21). |
| tuning-tiles-track | reproduced | Every track bin is some unit's peak, with no empty runs, in both regions. The 4 empty bins are the gaps between track segments (cell 25). |
| decoding-validation | reproduced | (a) Error is below the uniform null in 52/5
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd transcripts/001371; cat verifier-2-report.md author-revise-2-report.md; ls
```

```
**Prince et al. 2025 (DANDI:001371): verifier report, round 2**

The claims file has 52 claims and the attempt record gives an outcome for each: 21 reproduced, 5 partially reproduced, 7 not reproduced, 19 blocked (all `too_large`). Correction to my round-1 header: the round-1 table itself gave 6 partially reproduced and 7 not reproduced, not 7 and 6. Three outcomes changed since round 1:
- sfig3c-retrospective-unchanged: reproduced → not reproduced
- fig5d-stay-hpc-below-switch: partially reproduced → reproduced
- fig7c-hpc-commitment-initial-arm: not reproduced → reproduced

### 1. Outcomes

I agree with all 33 tested outcomes under each claim's criterion and the printed outputs. I also agree that the 19 choice-decoding claims are blocked.

- **Fragile outcomes.** Four outcomes turn on choices that are stated in the notes and in the claims file (S1 as amended, S5's code grid):
  - **sfig3c-retrospective-unchanged:** p = 0.036. It is 0.14 under the code's trial count and 0.12 on the round-1 grid. The paper's own p is 0.0513.
  - **sfig12-delay-hpc-no-outcome-difference:** p = 0.043, and 0.096 under the code's count.
  - **fig5d-stay-hpc-below-switch, new arm:** p = 0.0094, and 0.38 on the round-1 grid.
  - **fig7c-hpc-commitment-initial-arm:** p = 0.29, and 0.040 on the round-1 grid.
- **Assumptions.** No outcome in the attempt record is marked `assumed: true`. The choices the outcomes rest on (inclusion rule, time grid, how the arms are split into halves, the spread rule) are stated in the notes and deviations and are reasonable.
- **The 19 blocked claims.** I still think "too_large" is the wrong label for a limit on compute time. The author kept it under a protocol rule that I cannot check from here. The verification block records `agrees: true` for these claims, so my disagreement about the label appears only in the reason text. Blocked is right either way.

### 2. Sentences the printed numbers do not support
[... 85 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/001371-prince-2025-01.yaml",
 "offset": 1128,
 "limit": 90
}
```

```
1128	  notes: Blocked because it decodes the LSTM choice estimate of fig4a-lstm-choice-estimate (S11), which
1129	    is too large to run here (see that claim).
1130	findings:
1131	- kind: metadata_insufficient
1132	  statement: The units tables of five sessions (S20-210517, S28-211114, S29-211104, S29-211105, S34-220617;
1133	    633 units) hold only the phy columns, with no region, cell type, electrodes or electrode group column
1134	    (61 of the 66 units tables have an electrode group). Their ch values (0 to 63) do not say which of
1135	    the two 64-channel probes a unit is on, since ch runs from 0 to 63 on both probes in the labelled
1136	    sessions, so they cannot be assigned to CA1 or PFC. With them, the unit count equals the paper's 6449;
1137	    without them, CA1 has 3545 units and PFC 2271 against 3892 and 2557.
1138	- kind: metadata_error
1139	  statement: Position (processing/behavior/position) is labelled meters, but its values are in virtual
1140	    track units (y from -117 to 286, the code's track ends at 285).
1141	- kind: metadata_error
1142	  statement: View angle is labelled degrees, but its values run from -1.047 to 1.047, radians (plus or
1143	    minus 60 degrees).
1144	- kind: metadata_error
1145	  statement: The theta phase in processing/ecephys/decomposition_phase is labelled degrees, but its values
1146	    run from -pi to pi, radians.
1147	- kind: metadata_error
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json,yaml
d=json.load(open('targets/dandisets.json'))
items = d if isinstance(d,list) else (d.get('dandisets') or list(d.values()))
for x in items:
    if isinstance(x,dict) and str(x.get('id',x.get('identifier','')))=='001371':
        print(json.dumps(x,indent=1)[:3000])
a=yaml.safe_load(open('attempts/001371-prince-2025-01.yaml'))
for v in a['verifications']:
    print({k:v[k] for k in v if k!='claims' and k!='responses'})
    for k in v:
        if isinstance(v[k],list): print(k, len(v[k]), sum(1 for r in v[k] if r.get('agrees')))
E
head -60 claims/001371/*.yaml
```

```
<persisted-output>
Output too large (71.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d28aec04-3e73-4791-8697-6e5847bb0ec9/tool-results/bovkksf1g.txt

Preview (first 2KB):
{'date': '2026-11-02', 'kind': 'agent', 'by': 'Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)', 'reviewed': 'Round 1: the handover of the author-answers run, the executed notebook with the conclusions and summary removed, the helper module and the claims file, with the paper under paper/.', 'results': [{'claim': 'recordings', 'agrees': True, 'outcome': 'partially_reproduced', 'reason': "7 animals and 66 sessions match. CA1 has 3545 units (3892 ± 389, within). PFC has 2271 (2557 ± 256, outside). 633 units in 5 sessions have no region label. The all-unit total, 6449, equals the paper's exactly. Problem 2: the helper never tries the units' electrodes/electrode_group link to electrodes/location; whether the labels are recoverable is unverified.", 'response': 'No change of outcome. The notebook now prints the columns of the five units tables: none has an electrodes or electrode_group column (61 of the 66 tables do), and the phy channel ch runs from 0 to 63 on both probes in the labelled sessions, so it cannot assign a probe. The labels cannot be recovered from the files; notes and the metadata_insufficient finding say so.'}, {'claim': 'trial-mix', 'agrees': True, 'outcome': 'not_reproduced', 'reason': "Pooled fractions are 0.737 / 0.189 / 0.074 and per-session means 0.750 / 0.181 / 0.069, all outside tolerance. The counts 7172 / 1840 / 717 equal the paper's own counts. Problem 12: trial-mix expects programmed probabilities that the paper's own counts do not give.", 'response': "No change of outcome. The verifier's point on the claims file is added to questions/001371.yaml as a question for a reader; the claim was not changed."}, {'claim': 'task-timing', 'agrees': True, 'outcome': 'reproduced', 'reason': 'Un
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json,yaml
a=yaml.safe_load(open('attempts/001371-prince-2025-01.yaml'))
for v in a['verifications']:
    r=v['results']; print(v['reviewed'][:200]); print(len(r), sum(1 for x in r if x.get('agrees')), [x['claim'] for x in r if not x.get('agrees')], set(x.get('outcome') for x in r if 'outcome' in x and False))
for o in a['outcomes']:
    if o['outcome']=='blocked': print(o['claim'], o['blocked_by'])
d=json.load(open('targets/dandisets.json'))
print(type(d))
if isinstance(d,dict): print(list(d.keys())[:5])
E
```

```
Round 1: the handover of the author-answers run, the executed notebook with the conclusions and summary removed, the helper module and the claims file, with the paper under paper/.
52 52 [] set()
Round 2: the full executed notebook of the author-revise-1 run with its conclusions and summary, the helper module, the attempt record and the claims file, with the paper under paper/.
52 52 [] set()
fig4a-lstm-choice-estimate too_large
fig4f-pfc-choice-flips too_large
fig4f-pfc-difference too_large
fig4d-pfc-precedes-movement too_large
sfig7d-pfc-before-motor-single-trials too_large
sfig7e-pfc-pre-update too_large
fig4h-hpc-choice-switches too_large
fig4h-hpc-choices-equal too_large
fig4g-hpc-slower-than-pfc too_large
fig5f-stay-pfc-new-choice too_large
fig5f-stay-pfc-initial-choice too_large
fig5f-stay-pfc-difference too_large
fig6d-pfc-new-lower-incorrect too_large
fig6d-pfc-initial-no-difference too_large
fig6d-pfc-within-trial too_large
sfig12-delay-pfc-outcome-difference too_large
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
t=d['targets']
it = t.values() if isinstance(t,dict) else t
for x in it:
    if '001371' in json.dumps(x)[:200]: print(json.dumps(x,indent=1)[:4000])
E
f=claims/001371/*.yaml; wc -l $f; grep -n '^[a-z_]*:' $f; head -80 $f
```

```
{
 "dandiset": "001371",
 "name": "New information triggers prospective codes to adapt for flexible navigation",
 "published_version": "0.260831.0201",
 "asset_count": 66,
 "size_gb": 14536.77,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Mus musculus - House mouse"
 ],
 "approaches": [
  "electrophysiological approach",
  "behavioral approach"
 ],
 "papers": [
  {
   "doi": "10.1038/s41467-025-60122-8",
   "title": "New information triggers prospective codes to adapt for flexible navigation",
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
a=yaml.safe_load(open('attempts/001371-prince-2025-01.yaml'))
for o in a['outcomes'][:24]:
    print('##',o['claim'],o['outcome'],o.get('measured'))
    print(o['notes'][:900]); print()
E
```

```
## recordings partially_reproduced [7, 66, 3545, 2271]
7 animals and 66 sessions (8, 12, 10, 11, 12, 6 and 7 per animal) match. 3545 CA1 units (within 389.2 of 3892) and 2271 PFC units (outside 255.7 of 2557). The units of five sessions (S20-210517, S28-211114, S29-211104, S29-211105, S34-220617; 633 units) have no region or cell type column, and 3545 + 2271 + 633 = 6449, the paper's total. The per-animal counts of the unlabelled units are 138 (S20), 142 (S28), 242 (S29) and 111 (S34). Their region cannot be recovered from the files: none of the five units tables has an electrodes or electrode_group column (61 of the 66 tables do), and the phy channel ch runs from 0 to 63 on both probes in the labelled sessions, so it does not say which probe a unit is on (data check).

## trial-mix not_reproduced [0.7372, 0.1891, 0.0737]
Final-task trials (maze_id 4): 7172 delay only, 1840 switch and 717 stay, fractions 0.737, 0.189 and 0.074 pooled (reading a) and 0.750, 0.181 and 0.069 averaged over sessions (reading b), outside the tolerances under both readings. The counts equal the paper's Results counts. The 932 warm-up trials (maze_id 3) and the 7172 delay only trials make 8104, the delay count of Supplementary Table 1. The 65/25/10% read as the task's programmed probabilities, as the claims file foresaw.

## task-timing reproduced [10.559, 1.403, 6.02, 21.004, 20.882]
Readings (a) second delay from t_delay2, (c) all final-task trials, (e) switch trials: delay only delay 10.559 +/- 0.067 s (n = 7172), first switch delay 1.403 +/- 0.029 s (n = 1840), second delay 6.020 +/- 0.084 s, trial start to choice 21.004 s (delay only) and 20.882 s (switch); all within tolerance, and the n equal the paper's. Reading (f), switch and stay pooled, gives 6.060 s, also within. Reading (b), update cue onset to choice, gives 9.93 s. On correct trials only (d), the delay only delay is 10.414 s and the first switch delay 1.328 s, outside tolerance.

## fig1b-above-chance reproduced [0.649, 0.745
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import yaml
a=yaml.safe_load(open('attempts/001371-prince-2025-01.yaml'))
for o in a['outcomes'][24:]:
    print('##',o['claim'],o['outcome'],o.get('measured'))
    print(o['notes'][:900] if o['outcome']!='blocked' or o['claim'] in ('fig4a-lstm-choice-estimate','fig6e-predict-outcome') else o['notes'][:150]); print()
E
```

```
## fig4a-lstm-choice-estimate blocked None
Not run. The choice estimate is a per-session LSTM (S10) trained on the unresampled behaviour (about 110 samples per second, trials padded to the longest, up to 3601 samples), with 6-fold cross-validation repeated 3 times, so 18 models of 20 epochs per session. The notebook builds the model as the paper's code does and times one fold on session S25-210906 (119 delay only trials): 2.8 s for the first epoch and 1.6 s for the second, 9.8 min for the session, and 9.9 h for all 66 sessions scaled by their delay only trial counts in one process; with one session per core on the machine's 4 cores, at best 2.5 h. Epoch times vary from run to run, so these figures change when the notebook is re-run. Both are over the notebook's 60 min limit, so, as the protocol says for an estimate over that limit (Author, Develop on a subset), the claim is blocked as too_large and not run. No session was fitted;

## fig4f-pfc-choice-flips blocked None
Blocked because it decodes the LSTM choice estimate of fig4a-lstm-choice-estimate (S11), which is too large to run here (see that claim).

## fig4f-pfc-difference blocked None
Blocked because it decodes the LSTM choice estimate of fig4a-lstm-choice-estimate (S11), which is too large to run here (see that claim).

## fig4d-pfc-precedes-movement blocked None
Blocked because it decodes the LSTM choice estimate of fig4a-lstm-choice-estimate (S11), which is too large to run here (see that claim).

## sfig7d-pfc-before-motor-single-trials blocked None
Blocked because it decodes the LSTM choice estimate of fig4a-lstm-choice-estimate (S11), which is too large to run here (see that claim).

## sfig7e-pfc-pre-update blocked None
Blocked because it decodes the LSTM choice estimate of fig4a-lstm-choice-estimate (S11), which is too large to run here (see that claim).

## fig4h-hpc-choice-switches blocked None
Blocked because it decodes the LSTM choice estimate of fig4a-lstm-choice-estimate (S11), which is too larg
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B3 '001347\]' README.md | head; cat docs/pilot-notes/001754-knierim-2000-02.md | head -20
```

```
# 001754 again, on the fixed draft (2026-10-15)

The first repeat attempt, under the rules added for it (docs/agents/author-again.md).
The conversion was redone (`mcnaughton2000-to-nwb` at commit `7346882`) and
the draft re-uploaded on 2026-10-14, and the attempt pins `draft`. Three
claims reproduced, one not reproduced and three blocked, against two, two
and three before; both rounds agreed with every outcome and nothing was
proposed, so there was no third round.

The one change of outcome, `fd4-abnormal-selectivity` from not reproduced to
reproduced (one-sided p 0.024 against 0.055), comes from the data, not the
analysis: the draft drops every copy of each group of identical rate maps,
which removes three near-empty Rat2 maps the first attempt counted, and a
notebook cell runs the same test on the earlier maps to show it. Dropping
every copy instead of keeping one also removed six maps from the dandiset.
`flight-spatial-code` stays not reproduced (Rat1 10 of 25 significant on
flight day 9, Rat2 2 of 28); the rounds added tests of the shuffle null on
real spike trains cut off from position, which give fewer false positives
than the 0.05 the test assumes, and the record now calls a low fraction weak
evidence against a spatial code, since the test's power is unmeasured.
```

**Agent calls Bash**

```bash
cd  grep -rn 'Reproduced\b.*Partial\|readme_row' README.md tools/readme_row.py | head; sed -n 1,40p tools/readme_row.py
```

```
tools/readme_row.py:3:    python tools/readme_row.py DATASET            # print the row
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

import yaml

ROOT = Path(__file__).resolve().parents[1]
[... 21 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "docs/pilot-notes/001371-prince-2025-01.md",
 "content": "# 001371, Prince et al. 2025\n\nTwenty-one claims reproduced, five partially, seven not reproduced and 19\nblocked, all as `too_large`, with no outcome on an assumption. All 52 claims\nare on the dandiset. The first verification round agreed with all 52 outcomes\nas they stood and the second with all 52, and nothing was proposed after the\nsecond, so there was no third round. It pins version 0.260831.0201, the only\npublished version; the paper cites none. The paper, Prince, Cushing, Yassine,\nKatragadda, Roberts and Singer, \"New information triggers prospective codes to\nadapt for flexible navigation\" in Nature Communications, records dorsal CA1 and\nmedial prefrontal cortex (PFC) with 64-channel probes in 7 mice over 66\nhead-fixed virtual reality sessions of a y-maze task with delay only, switch\nand stay trials, decodes the goal arms from the units by Bayesian decoding of\nposition, splits the decoding by theta phase, and decodes from both regions an\nLSTM estimate of the animal's choice made from its movements. The claims were\nwritten from the version of record served by Europe PMC (PMC12102184) with the\nSupplementary Information and the Peer Review File, without the Source Data\nfile and without reading figures from PDF pages; the paper's code\n(github.com/stephprince/update-project, commit d8557f0) supplies the track\ngraph and arm bounds, the speed threshold, the train/test split, the pseudo\nupdate time, the spread measure, the theta phase source and the LSTM\narchitecture for the timing. Reproduced are the behaviour claims (the counts\nof 7172 delay only, 1840 switch and 717 stay trials, the window counts 6252,\n1002 and 117 of 15-trial windows, and W = 125.5 and 48.5 as the paper prints),\nthe tuning and decoding validation, the CA1 goal arm increase on switch trials\n(ANOVA p = 9.9e-22) with equal arms, the goal bias, the CA1 over PFC goal\ncoding, the theta claims `fig3b-theta-pre-post`, `sfig6-theta-switch-over-delay`\nand `fig3d-new-arm-theta-modulated`, the stay trial claims of Fig. 5d and Supp.\nFig. 10, the three CA1 outcome claims of Fig. 6 and\n`fig7c-hpc-commitment-initial-arm` (p = 0.29). Partial are `recordings` (3545\nCA1 units within tolerance, 2271 PFC units outside it), `sfig3ab-original-vs-update-cue`\n(three of the four contrasts), `sfig2f-all-trials-encoder` (reading b fails for\nthe initial arm), `sfig5f-pfc-wider-spread` (PFC wider, p = 0.0031, but 4.07 and\n4.37 bins against 2.4 and 3.13) and `fig7c-hpc-commitment-new-arm` (rho = +0.077,\np = 0.0067, outside 0.1237 +/- 0.0124). Not reproduced are `trial-mix`\n(fractions 0.737, 0.189 and 0.074 against the 65, 25 and 10%),\n`sfig3c-goals-over-retrospective` (p = 0.84 and 0.43), the absences\n`sfig3c-retrospective-unchanged` (p = 0.036), `fig2g-pfc-no-goal-increase` (two\ntests below 0.05 under each model reading), `sfig5e-pfc-windows` (three windows\nbelow 0.05) and `sfig12-delay-hpc-no-outcome-difference` (p = 0.043), and\n`fig3c-theta-phase-segregation`, where the central zone exceeds both goal arms\nin the first half cycle as well. Several of the failed absences rest on one\ntest just under 0.05. Blocked are `fig4a-lstm-choice-estimate` and the 18\nclaims that decode its output: the per-session LSTM was timed at 9.9 h for all\n66 sessions in one process and at best 2.5 h on 4 cores, against the\nnotebook's 60 min limit, and the CA1 half of `fig6e-predict-outcome`, which\nneeds no LSTM, takes about 1.0 h for the real labels and about 41 days with the\n1000 shuffles of its permutation test. The author's first run gave 19\nreproduced, 6 partially, 8 not reproduced and 19 blocked. The author asked a\nreader whether the 50-trial session rule of shared method S1 counts the\nencoder training trials, as the code does, or the session's trials, as the\nMethods say; the reader amended S1 to count the final-task trials, which gives\n55 CA1 and 46 PFC sessions against the paper's 56 and 47 (47 and 37 before),\nand the author-answers run moved `fig5d-stay-hpc-like-delay` to reproduced (new\narm p = 0.063, where it had been 0.032). Round 1 agreed with every outcome and\nfound that the spread was measured to the outermost bins above threshold where\nthe Methods describe the first crossing, that the helper never tried the\nunits' electrode link for the 633 unlabelled units, that the CA1 half of fig6e\ncould be run, that `too_large` fits a limit on compute time poorly, that the\narm halves of sfig3ab held gap bins with no posterior, that the 0.2 s grid had\none bin centred on the cue and counted after it, and that the tests are Wald\ntests where the paper used Kenward-Roger degrees of freedom; in reply the\ncode's grid was adopted, which moved `sfig3c-retrospective-unchanged` to not\nreproduced (p = 0.036 against 0.12), `fig5d-stay-hpc-below-switch` to\nreproduced (new arm p = 0.0094 against 0.38) and\n`fig7c-hpc-commitment-initial-arm` to reproduced (p = 0.29 against 0.040), the\ncode's spread rule was confirmed at the pinned commit and the first-crossing\nrule added as a variant, the arm halves were split as the code splits them,\nfig6e's CA1 half was timed, the LSTM claims were kept as `too_large` with the\ndisagreement recorded, and reader questions were filed on fig3c's whole central\narm reading and trial-mix's programmed probabilities. Round 2 agreed with all\n52, called four outcomes fragile (`sfig3c-retrospective-unchanged`,\n`sfig12-delay-hpc-no-outcome-difference`, the new arm of\n`fig5d-stay-hpc-below-switch` and `fig7c-hpc-commitment-initial-arm`), still\nheld `too_large` to be the wrong label, asked whether S7's window means should\nweight the bins 3/2/3, and found sentences the outputs did not support (LSTM\nand SVM timings from an earlier run, such as 10.4 h where 8.3 h is printed and\n41 days where 28 days is printed, four outcomes changed by the grid where there\nare three, p < 1e-9 where 9.25e-9 is printed, and the shortfall in each region\nput on the unlabelled units where only the total is shown), all corrected. The\nwindow means needed no change, as the code takes a plain mean of the 0.2 s\nsamples, and a reader question was filed on S7's wording; Kenward-Roger was not\nrun, R not being available, and on a deliberately small number of degrees of\nfreedom `sfig3c-retrospective-unchanged` gives p = 0.050,\n`sfig12-delay-hpc-no-outcome-difference` 0.053 and the new arm front half of\nsfig3ab 0.063, with the outcomes kept. The author's run took about 2 h 05 min\n(07:47 to about 09:53 UTC); a first walk over one file took 23 min over the\nnetwork, and the first extraction failed on the five sessions without a region\ncolumn until the loader was fixed. The notebook ran in 1101 s and 1474 s at\nfirst, about 19 min after the author-answers run, 1437 s for the whole entry\nafter round 1 and 25 min at the end. Markdown was corrected after the last run\nof the author's run and of the first revision without a further run, and in\nthe executed copy one awkward phrase in cell 117 was left. A change to\n`tools/runner/chain.sh`, already there, was left untouched.\n\nThe units tables of five sessions (S20-210517, S28-211114, S29-211104,\nS29-211105, S34-220617; 633 units) hold only the phy columns, with no region,\ncell type, electrodes or electrode group column (61 of the 66 units tables have\nan electrode group), and their ch values (0 to 63) cannot say which of the two\n64-channel probes a unit is on, so they cannot be assigned to CA1 or PFC; with\nthem the unit count equals the paper's 6449, and without them CA1 has 3545\nunits and PFC 2271 against 3892 and 2557, and those five sessions drop out of\nevery decoding test. The trials column turn_type is described as {'right': 1,\n'left': 2}, while correct delay only trials with turn_type 1 all end at\nnegative x (2521 of 2521) and have choice 1, and the paper's code maps\nturn_type 1 to left. Position is labelled meters but is in virtual track units\n(y from -117 to 286), and view angle (-1.047 to 1.047) and the theta phase in\nprocessing/ecephys/decomposition_phase (-pi to pi) are labelled degrees but are\nin radians. Of the paper itself, the Methods and the Figure 1b legend give\n40-trial windows while the reported window counts (6252, 1002 and 117) are\nthose of 15-trial windows, the code's default, 40-trial windows giving 4636,\n239 and none; Supplementary Table 1's 8104 delay trials are the 7172 final-task\ndelay only trials and the 932 warm-up trials; and the Results' 65, 25 and 10%\nare not the fractions of the trials (0.737, 0.189, 0.074). Of the paper and its\ncode, the code counts the encoder training trials for the 50-trial session rule\nwhere the Methods count the session's trials, and the code's count changes two\noutcomes here (sfig3c-retrospective-unchanged, p = 0.14 against 0.036, and\nsfig12-delay-hpc-no-outcome-difference, p = 0.096 against 0.043); the code\nreads the theta phase stored in the file where the Methods describe one from\npeaks and troughs, the two agreeing closely (median 0.975 over 59 sessions)\nwith every theta outcome the same, the one session where they agree least\n(S20-210511, mean cosine -0.49) having pyramidal spikes barely locked to theta;\nand the Methods define the spread of Supplementary Fig. 5f by the first\ncrossing of the threshold where the code takes the outermost bins above it,\ngiving 0.14 and 0.37 bins against 4.07 and 4.37 here and the paper's 2.4 and\n3.13. On the track, 4 of the 50 bins lie wholly in the gaps between track\nsegments, so the tuning criterion that every bin be some unit's peak was judged\non the 46 track bins. The dandiset also names a second paper, \"Goal-specific\nhippocampal inhibition gates learning\". A question is put to the paper's\nauthors: which 0.2 s bins enter the windows after the update cue, since a grid\nwith a bin centred on the cue shifts the windows by 0.1 s and changes three\noutcomes here.\n\nThe author's points on the protocol: shared method S1 follows the code where\nthe Methods differ, which changes two outcomes and sits between a misreading\nand a missing detail, so a reader was asked and both counts were run; the\ntuning-tiles criterion asks every one of 50 bins to be a peak where 4 lie in\nthe track's gaps, and the 46 track bins were judged with a deviation recorded\nand no reader asked; the protocol does not say whether markdown corrected after\nthe last run, with code and outputs unchanged, needs a re-run; the timed\nestimate it asks for may not come from outside the notebook, so the LSTM timing\ncell was put in the notebook, adding TensorFlow (about 1.5 GB) to the\nenvironment; it does not say where checks that apply to every claim belong,\nand they were put in the data check and each claim's printout; and the record\nhas no field for deviations common to the attempt, so the shared ones, such as\nWald tests in place of Kenward-Roger, are repeated on each claim.\n"
}
```

```
File created successfully at: docs/pilot-notes/001371-prince-2025-01.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  f=docs/pilot-notes/001371-prince-2025-01.md; python - <<'E'
p='docs/pilot-notes/001371-prince-2025-01.md'; s=open(p).read()
s=s.replace(", and those five sessions drop out of\nevery decoding test.", ".")
s=s.replace("Markdown was corrected after the last run\nof the author's run and of the first revision without a further run, and in\nthe executed copy one awkward phrase in cell 117 was left.","In the author's run and the first revision, markdown was corrected after the\nlast run without a further run, and in the executed copy one awkward phrase in\ncell 117 was left.")
open(p,'w').write(s)
E
grep -c 'drop out\|Markdown was' $f; grep -n '—\|rather\|\*\*' $f; wc -w $f; git status --short
```

```
0
1751 docs/pilot-notes/001371-prince-2025-01.md
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
?? docs/pilot-notes/001371-prince-2025-01.md
?? scripts
```

**Agent calls Read**

```json
{
 "file_path": "docs/pilot-notes/001371-prince-2025-01.md"
}
```

```
1	# 001371, Prince et al. 2025
2	
3	Twenty-one claims reproduced, five partially, seven not reproduced and 19
4	blocked, all as `too_large`, with no outcome on an assumption. All 52 claims
5	are on the dandiset. The first verification round agreed with all 52 outcomes
6	as they stood and the second with all 52, and nothing was proposed after the
7	second, so there was no third round. It pins version 0.260831.0201, the only
8	published version; the paper cites none. The paper, Prince, Cushing, Yassine,
9	Katragadda, Roberts and Singer, "New information triggers prospective codes to
10	adapt for flexible navigation" in Nature Communications, records dorsal CA1 and
11	medial prefrontal cortex (PFC) with 64-channel probes in 7 mice over 66
12	head-fixed virtual reality sessions of a y-maze task with delay only, switch
13	and stay trials, decodes the goal arms from the units by Bayesian decoding of
14	position, splits the decoding by theta phase, and decodes from both regions an
15	LSTM estimate of the animal's choice made from its movements. The claims were
16	written from the version of record served by Europe PMC (PMC12102184) with the
17	Supplementary Information and the Peer Review File, without the Source Data
18	file and without reading figures from PDF pages; the paper's code
19	(github.com/stephprince/update-project, commit d8557f0) supplies the track
20	graph and arm bounds, the speed threshold, the train/test split, the pseudo
[... 126 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='docs/pilot-notes/001371-prince-2025-01.md'; s=open(p).read()
s=s.replace("""after round 1 and 25 min at the end. In the author's run and the first revision, markdown was corrected after the
last run without a further run, and in the executed copy one awkward phrase in
cell 117 was left. A change to
`tools/runner/chain.sh`, already there, was left untouched.""","""after round 1 and 25 min at the end. In the author's run and the first
revision, markdown was corrected after the last run without a further run, and
in the executed copy one awkward phrase in cell 117 was left. A change to
`tools/runner/chain.sh`, already there, was left untouched.""")
s=s.replace("""units and PFC 2271 against 3892 and 2557. The trials column turn_type is described as {'right': 1,
'left': 2}, while""","""units and PFC 2271 against 3892 and 2557. The trials column turn_type is
described as {'right': 1, 'left': 2}, while""")
open(p,'w').write(s)
E
awk 'length>82' docs/pilot-notes/001371-prince-2025-01.md
```

```
CA1 units within tolerance, 2271 PFC units outside it), `sfig3ab-original-vs-update-cue`
described as {'right': 1, 'left': 2}, while correct delay only trials with turn_type 1 all end at
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='docs/pilot-notes/001371-prince-2025-01.md'; s=open(p).read()
s=s.replace("""described as {'right': 1, 'left': 2}, while correct delay only trials with turn_type 1 all end at
negative x""","""described as {'right': 1, 'left': 2}, while correct delay only trials with
turn_type 1 all end at negative x""")
open(p,'w').write(s)
E
sed -n 100,110p docs/pilot-notes/001371-prince-2025-01.md
```

```
64-channel probes a unit is on, so they cannot be assigned to CA1 or PFC; with
them the unit count equals the paper's 6449, and without them CA1 has 3545
units and PFC 2271 against 3892 and 2557. The trials column turn_type is
described as {'right': 1, 'left': 2}, while correct delay only trials with
turn_type 1 all end at negative x (2521 of 2521) and have choice 1, and the paper's code maps
turn_type 1 to left. Position is labelled meters but is in virtual track units
(y from -117 to 286), and view angle (-1.047 to 1.047) and the theta phase in
processing/ecephys/decomposition_phase (-pi to pi) are labelled degrees but are
in radians. Of the paper itself, the Methods and the Figure 1b legend give
40-trial windows while the reported window counts (6252, 1002 and 117) are
those of 15-trial windows, the code's default, 40-trial windows giving 4636,
```

**Agent**

Cosmetic line length only; I'll leave it as is.

**Agent calls Bash**

```bash
cd  cat docs/pilot-notes/001371-prince-2025-01.md; git status --short docs
```

```
# 001371, Prince et al. 2025

Twenty-one claims reproduced, five partially, seven not reproduced and 19
blocked, all as `too_large`, with no outcome on an assumption. All 52 claims
are on the dandiset. The first verification round agreed with all 52 outcomes
as they stood and the second with all 52, and nothing was proposed after the
second, so there was no third round. It pins version 0.260831.0201, the only
published version; the paper cites none. The paper, Prince, Cushing, Yassine,
Katragadda, Roberts and Singer, "New information triggers prospective codes to
adapt for flexible navigation" in Nature Communications, records dorsal CA1 and
medial prefrontal cortex (PFC) with 64-channel probes in 7 mice over 66
head-fixed virtual reality sessions of a y-maze task with delay only, switch
and stay trials, decodes the goal arms from the units by Bayesian decoding of
position, splits the decoding by theta phase, and decodes from both regions an
LSTM estimate of the animal's choice made from its movements. The claims were
written from the version of record served by Europe PMC (PMC12102184) with the
Supplementary Information and the Peer Review File, without the Source Data
file and without reading figures from PDF pages; the paper's code
(github.com/stephprince/update-project, commit d8557f0) supplies the track
graph and arm bounds, the speed threshold, the train/test split, the pseudo
[... 126 more lines not kept]
```

**Agent**

I wrote the notes as a new file, `docs/pilot-notes/001371-prince-2025-01.md`, and changed nothing else. Nothing is committed. Some untracked dotfiles, `.idea`, `.vscode` and `scripts` were already in the repository root; I left them alone. The `catalystneuro` field for 001371 is empty, so the findings paragraph does not open with the CatalystNeuro sentence. One line in the second paragraph runs past the usual wrap width.

# 001371, Prince et al. 2025

Twenty-one claims reproduced, five partially, seven not reproduced and 19
blocked, all as `too_large`, with no outcome on an assumption. All 52 claims
are on the dandiset. The first verification round agreed with all 52 outcomes
as they stood and the second with all 52, and nothing was proposed after the
second, so there was no third round. It pins version 0.260831.0201, the only
published version; the paper cites none. The paper, Prince, Cushing, Yassine,
Katragadda, Roberts and Singer, "New information triggers prospective codes to
adapt for flexible navigation" in Nature Communications, records dorsal CA1 and
medial prefrontal cortex (PFC) with 64-channel probes in 7 mice over 66
head-fixed virtual reality sessions of a y-maze task with delay only, switch
and stay trials, decodes the goal arms from the units by Bayesian decoding of
position, splits the decoding by theta phase, and decodes from both regions an
LSTM estimate of the animal's choice made from its movements. The claims were
written from the version of record served by Europe PMC (PMC12102184) with the
Supplementary Information and the Peer Review File, without the Source Data
file and without reading figures from PDF pages; the paper's code
(github.com/stephprince/update-project, commit d8557f0) supplies the track
graph and arm bounds, the speed threshold, the train/test split, the pseudo
update time, the spread measure, the theta phase source and the LSTM
architecture for the timing. Reproduced are the behaviour claims (the counts
of 7172 delay only, 1840 switch and 717 stay trials, the window counts 6252,
1002 and 117 of 15-trial windows, and W = 125.5 and 48.5 as the paper prints),
the tuning and decoding validation, the CA1 goal arm increase on switch trials
(ANOVA p = 9.9e-22) with equal arms, the goal bias, the CA1 over PFC goal
coding, the theta claims `fig3b-theta-pre-post`, `sfig6-theta-switch-over-delay`
and `fig3d-new-arm-theta-modulated`, the stay trial claims of Fig. 5d and Supp.
Fig. 10, the three CA1 outcome claims of Fig. 6 and
`fig7c-hpc-commitment-initial-arm` (p = 0.29). Partial are `recordings` (3545
CA1 units within tolerance, 2271 PFC units outside it), `sfig3ab-original-vs-update-cue`
(three of the four contrasts), `sfig2f-all-trials-encoder` (reading b fails for
the initial arm), `sfig5f-pfc-wider-spread` (PFC wider, p = 0.0031, but 4.07 and
4.37 bins against 2.4 and 3.13) and `fig7c-hpc-commitment-new-arm` (rho = +0.077,
p = 0.0067, outside 0.1237 +/- 0.0124). Not reproduced are `trial-mix`
(fractions 0.737, 0.189 and 0.074 against the 65, 25 and 10%),
`sfig3c-goals-over-retrospective` (p = 0.84 and 0.43), the absences
`sfig3c-retrospective-unchanged` (p = 0.036), `fig2g-pfc-no-goal-increase` (two
tests below 0.05 under each model reading), `sfig5e-pfc-windows` (three windows
below 0.05) and `sfig12-delay-hpc-no-outcome-difference` (p = 0.043), and
`fig3c-theta-phase-segregation`, where the central zone exceeds both goal arms
in the first half cycle as well. Several of the failed absences rest on one
test just under 0.05. Blocked are `fig4a-lstm-choice-estimate` and the 18
claims that decode its output: the per-session LSTM was timed at 9.9 h for all
66 sessions in one process and at best 2.5 h on 4 cores, against the
notebook's 60 min limit, and the CA1 half of `fig6e-predict-outcome`, which
needs no LSTM, takes about 1.0 h for the real labels and about 41 days with the
1000 shuffles of its permutation test. The author's first run gave 19
reproduced, 6 partially, 8 not reproduced and 19 blocked. The author asked a
reader whether the 50-trial session rule of shared method S1 counts the
encoder training trials, as the code does, or the session's trials, as the
Methods say; the reader amended S1 to count the final-task trials, which gives
55 CA1 and 46 PFC sessions against the paper's 56 and 47 (47 and 37 before),
and the author-answers run moved `fig5d-stay-hpc-like-delay` to reproduced (new
arm p = 0.063, where it had been 0.032). Round 1 agreed with every outcome and
found that the spread was measured to the outermost bins above threshold where
the Methods describe the first crossing, that the helper never tried the
units' electrode link for the 633 unlabelled units, that the CA1 half of fig6e
could be run, that `too_large` fits a limit on compute time poorly, that the
arm halves of sfig3ab held gap bins with no posterior, that the 0.2 s grid had
one bin centred on the cue and counted after it, and that the tests are Wald
tests where the paper used Kenward-Roger degrees of freedom; in reply the
code's grid was adopted, which moved `sfig3c-retrospective-unchanged` to not
reproduced (p = 0.036 against 0.12), `fig5d-stay-hpc-below-switch` to
reproduced (new arm p = 0.0094 against 0.38) and
`fig7c-hpc-commitment-initial-arm` to reproduced (p = 0.29 against 0.040), the
code's spread rule was confirmed at the pinned commit and the first-crossing
rule added as a variant, the arm halves were split as the code splits them,
fig6e's CA1 half was timed, the LSTM claims were kept as `too_large` with the
disagreement recorded, and reader questions were filed on fig3c's whole central
arm reading and trial-mix's programmed probabilities. Round 2 agreed with all
52, called four outcomes fragile (`sfig3c-retrospective-unchanged`,
`sfig12-delay-hpc-no-outcome-difference`, the new arm of
`fig5d-stay-hpc-below-switch` and `fig7c-hpc-commitment-initial-arm`), still
held `too_large` to be the wrong label, asked whether S7's window means should
weight the bins 3/2/3, and found sentences the outputs did not support (LSTM
and SVM timings from an earlier run, such as 10.4 h where 8.3 h is printed and
41 days where 28 days is printed, four outcomes changed by the grid where there
are three, p < 1e-9 where 9.25e-9 is printed, and the shortfall in each region
put on the unlabelled units where only the total is shown), all corrected. The
window means needed no change, as the code takes a plain mean of the 0.2 s
samples, and a reader question was filed on S7's wording; Kenward-Roger was not
run, R not being available, and on a deliberately small number of degrees of
freedom `sfig3c-retrospective-unchanged` gives p = 0.050,
`sfig12-delay-hpc-no-outcome-difference` 0.053 and the new arm front half of
sfig3ab 0.063, with the outcomes kept. The author's run took about 2 h 05 min
(07:47 to about 09:53 UTC); a first walk over one file took 23 min over the
network, and the first extraction failed on the five sessions without a region
column until the loader was fixed. The notebook ran in 1101 s and 1474 s at
first, about 19 min after the author-answers run, 1437 s for the whole entry
after round 1 and 25 min at the end. In the author's run and the first
revision, markdown was corrected after the last run without a further run, and
in the executed copy one awkward phrase in cell 117 was left. A change to
`tools/runner/chain.sh`, already there, was left untouched.

The units tables of five sessions (S20-210517, S28-211114, S29-211104,
S29-211105, S34-220617; 633 units) hold only the phy columns, with no region,
cell type, electrodes or electrode group column (61 of the 66 units tables have
an electrode group), and their ch values (0 to 63) cannot say which of the two
64-channel probes a unit is on, so they cannot be assigned to CA1 or PFC; with
them the unit count equals the paper's 6449, and without them CA1 has 3545
units and PFC 2271 against 3892 and 2557. The trials column turn_type is
described as {'right': 1, 'left': 2}, while correct delay only trials with
turn_type 1 all end at negative x (2521 of 2521) and have choice 1, and the paper's code maps
turn_type 1 to left. Position is labelled meters but is in virtual track units
(y from -117 to 286), and view angle (-1.047 to 1.047) and the theta phase in
processing/ecephys/decomposition_phase (-pi to pi) are labelled degrees but are
in radians. Of the paper itself, the Methods and the Figure 1b legend give
40-trial windows while the reported window counts (6252, 1002 and 117) are
those of 15-trial windows, the code's default, 40-trial windows giving 4636,
239 and none; Supplementary Table 1's 8104 delay trials are the 7172 final-task
delay only trials and the 932 warm-up trials; and the Results' 65, 25 and 10%
are not the fractions of the trials (0.737, 0.189, 0.074). Of the paper and its
code, the code counts the encoder training trials for the 50-trial session rule
where the Methods count the session's trials, and the code's count changes two
outcomes here (sfig3c-retrospective-unchanged, p = 0.14 against 0.036, and
sfig12-delay-hpc-no-outcome-difference, p = 0.096 against 0.043); the code
reads the theta phase stored in the file where the Methods describe one from
peaks and troughs, the two agreeing closely (median 0.975 over 59 sessions)
with every theta outcome the same, the one session where they agree least
(S20-210511, mean cosine -0.49) having pyramidal spikes barely locked to theta;
and the Methods define the spread of Supplementary Fig. 5f by the first
crossing of the threshold where the code takes the outermost bins above it,
giving 0.14 and 0.37 bins against 4.07 and 4.37 here and the paper's 2.4 and
3.13. On the track, 4 of the 50 bins lie wholly in the gaps between track
segments, so the tuning criterion that every bin be some unit's peak was judged
on the 46 track bins. The dandiset also names a second paper, "Goal-specific
hippocampal inhibition gates learning". A question is put to the paper's
authors: which 0.2 s bins enter the windows after the update cue, since a grid
with a bin centred on the cue shifts the windows by 0.1 s and changes three
outcomes here.

The author's points on the protocol: shared method S1 follows the code where
the Methods differ, which changes two outcomes and sits between a misreading
and a missing detail, so a reader was asked and both counts were run; the
tuning-tiles criterion asks every one of 50 bins to be a peak where 4 lie in
the track's gaps, and the 46 track bins were judged with a deviation recorded
and no reader asked; the protocol does not say whether markdown corrected after
the last run, with code and outputs unchanged, needs a re-run; the timed
estimate it asks for may not come from outside the notebook, so the LSTM timing
cell was put in the notebook, adding TensorFlow (about 1.5 GB) to the
environment; it does not say where checks that apply to every claim belong,
and they were put in the data check and each claim's printout; and the record
has no field for deviations common to the attempt, so the shared ones, such as
Wald tests in place of Kenward-Roger, are repeated on each claim.

## End of run

24 turns, 3 minutes, $1.25 at API prices, result: success.
