# crcns-fcx-3 · author-revise-3 · run 42559616339

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/crcns-fcx-3/verifier-3-report.md; ls entries/crcns-fcx-3-johnson-2019 entries/crcns-fcx-3-johnson-2019/*; grep -n "step 6\|^## \|^### " docs/protocol.md | head -60
```

```
Mon Nov  9 04:07:14 UTC 2026
**Verifier report, round 3: Johnson et al. 2019 (doi:10.3389/fnsys.2018.00065) on CRCNS fcx-3**

The claims file has 17 claims and the attempt record has 17 outcomes. Three of those outcomes carry a `proposed` change: fig4c-alpha-beta-shift, fig5a-spatiotemporal-bidirectional and fig5b-alpha-beta-no-sustained. I reviewed only these three. Cell numbers are 0-based positions in the re-executed notebook. I did not download the data or re-run anything.

All three proposals come from one change: the author now adopts PSI reading (a) wherever the two readings give different outcomes. The reason is calibration, which I asked about in round 2, and it holds up on the printed outputs:

- **Trial-shuffled surrogate (cell 45).** Under (a), z has mean −0.05 and 0.02, SD 1.01 and 1.04, and 6.0% and 6.9% of pairs pass |z| > 1.96. Under (b), delta-theta has mean −0.29, SD 0.60 and a 0.1% pass rate. Its per-subject means in alpha-beta run from −1.25 to 0.52, where the true value is 0.
- **Synthetic independent signals (cell 46).** Reading (b) has mean z of −0.21 to −0.37. Reading (a) has −0.07 to −0.15 with SD near 1. Moving the FFT origin to the segment centre removes (b)'s offset, which supports the explanation in cell 43.
- **No sign of steering toward a result.** The switch lowers two outcomes (fig4c, fig5b) and raises one (fig5a-spatiotemporal), and the reason comes from calibration checks, not from the outcomes.

The three outcomes still rest on the choice of P1 reading, so `assumed: true` should stay on all three.

| Claim | Proposed outcome | Agree? | My outcome if different | Reason |
|---|---|---|---|---|
| fig4c-alpha-beta-shift | not_reproduced | Yes | | **Reading (a), cell 50:** 5 of 7 subjects are below 0 in processing (mean −0.14 ± 0.26). The pair-level model holds (processing higher by 0.11, F = 6.7, p = 0.0097; cell 49), but the partial match needs at least 6 subjects below 0. The per-trial-permutation version of (a) also gives 5 of 7. *
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 473,510p docs/protocol.md; sed -n 617,700p docs/protocol.md; ls attempts 2>/dev/null | grep fcx-3; find . -path ./node_modules -prune -o -name "*crcns-fcx-3-johnson-2019-01*" -print | head
```

```
### 6. Hand over for verification

Do not verify your own attempt. Give the verifier:

- the executed notebook with the conclusion cells and the summary removed;
- the helper module;
- the claims file.

`python tools/entry.py handover entries/<name>` builds these in
`executed/<name>/handover/` from the executed copy. The verifier also gets the
paper, under `paper/`, but checks the analysis against the claims file, and a
method detail the author took from the paper against the passage the author
cites. A place where the claims file misreads the paper is reported; the
revision adds it to `questions/<folder>.yaml` as a question for a reader, as in
step 1.6, and does not change the claim. A reader answers it after the
attempt, in an `answer` run started by hand; the claim's outcome stays as
tested on the claims file, and a later attempt takes up any change.

After the first round, fix what it found, re-run, and hand over the full
executed notebook for the second round. Record each round under
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/crcns-fcx-3-johnson-2019-01.yaml; git diff --stat
```

```
<persisted-output>
Output too large (53.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/079c490e-a415-43e2-b26b-fec05096cfca/tool-results/bls8wx8n9.txt

Preview (first 2KB):
schema_version: 2
id: crcns-fcx-3-johnson-2019-01
dataset:
  archive: crcns
  id: fcx-3
  version: unversioned
  doi: 10.6080/K06971S9
paper: doi:10.3389/fnsys.2018.00065
date: 2026-11-08
entry: crcns-fcx-3-johnson-2019
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd attempts; grep -n "proposed\|^- claim\|^verifications\|^  - round\|round:" crcns-fcx-3-johnson-2019-01.yaml; git diff --stat; git diff | head -50
```

```
23:- claim: table1-electrodes
42:- claim: trial-counts
61:- claim: fig1b-accuracy
81:- claim: fig1b-rt-identity-slower
96:- claim: erp-no-condition-difference
133:- claim: fig2-spatial-power
168:- claim: fig3-temporal-power
189:- claim: power-difficulty-subjects
203:- claim: power-low-frequencies
221:- claim: fig4-maintenance-parietal-led
260:- claim: fig4a-delta-theta-shift
284:- claim: fig4c-alpha-beta-shift
293:    reproduced is proposed. Under reading (b), 6 of 7 subjects have processing alpha-beta PSI z below
305:  proposed:
317:- claim: directional-pairs
335:- claim: fig5a-delta-theta-epochs
356:- claim: fig5a-identity-direction
373:- claim: fig5a-spatiotemporal-bidirectional
379:    is proposed. Under reading (b) the selection leaves one directional pair (S1); its spatial-trial
389:  proposed:
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 284,420p attempts/crcns-fcx-3-johnson-2019-01.yaml
```

```
- claim: fig4c-alpha-beta-shift
  outcome: partially_reproduced
  assumed: true
  notebook: reproduce_johnson_2019.ipynb
  output: claim:fig4c-alpha-beta-shift
  measured:
  - -0.57
  - 97.9
  notes: The outcome is the one round 2 reviewed, under PSI reading (b), and a change to not
    reproduced is proposed. Under reading (b), 6 of 7 subjects have processing alpha-beta PSI z below
    0 (S3 is above, 0.46) and processing exceeds maintenance in the pair-level model (by 0.43,
    F(1,2268) = 97.9, p = 1.2e-22; paper F = 2302.30), the criterion's partial match by the letter.
    Subject means lie between -1.35 and 0.46 (mean -0.57 +- 0.59, recorded; paper -12.60 +- 7.51). On
    the trial-shuffled data reading (b) gives nearly the same subject means (observed minus surrogate
    -0.08 +- 0.09, p = 0.061). Under reading (a), now adopted, 5 of 7 subjects are below 0 (mean -0.14
    +- 0.26), with processing higher by 0.11 (F = 6.7, p = 0.0097). On subject means the interval
    difference is not significant under either reading (paired t(6) p = 0.27 under (b), 0.48 under
    (a)).
  deviations:
  - As fig4a-delta-theta-shift. The outcome rests on PSI reading (b), the reading round 2 reviewed;
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 420,500p attempts/crcns-fcx-3-johnson-2019-01.yaml; echo ----; sed -n 690,900p attempts/crcns-fcx-3-johnson-2019-01.yaml
```

```
counts as partially reproduced. The significant points of reading (b) come from the pair-level
      model on 74 pairs, about as many as trial-shuffled data select (71), 44 of them from S3; a
      paired test on the 6 subjects' means finds none after FDR.
findings:
- kind: metadata_error
  statement: The data set's list of analysed channels (docs/summary_channel_analysis.csv) holds 187
    channels where the paper reports 192 (Table 1). S4 has 5 right parietal channels (RLD6 to RLD8,
    RC10, RC11) where Table 1 gives 10. The list yields 1135 same-hemisphere PFC-parietal pairs,
    where the paper reports 1129; Table 1's counts would give 1165.
- kind: metadata_error
  statement: The description says summary_file_trial.csv holds information about each trial, with
    120 trials per subject. In S6 and S7 it holds only the trials kept after artifact rejection (101
    and 90 rows, numbered up to 120), matching their derived epochs; in S1 to S5 it holds all 120.
    Single-trial accuracy over all 120 trials cannot be rebuilt for S6 and S7 (summary_file.csv gives
    it per condition).
- kind: other
  statement: A timing contrast between trials with 900-ms and 1150-ms delays (70-150 Hz amplitude)
    shows, in S2, S3 and S4, responses in the processing epoch of the 1150-ms trials 0.21 to 0.26 s
    later relative to the trial table's processing column than in the 900-ms trials, and in S4 the
    same shift in the encoding epoch, while the pretrial epochs show shifts of 0.03 s or less. This is
[... 196 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- date\|^  kind\|^  by\|^  round\|^  reviewed\|^  results\|^  [a-z_]*:" attempts/crcns-fcx-3-johnson-2019-01.yaml | sed -n '1,200p' | awk -F: '$1>495'; sed -n 640,660p attempts/crcns-fcx-3-johnson-2019-01.yaml
```

```
498:- date: '2026-11-08'
499:  kind: agent
500:  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
501:  reviewed: Round 1. The first executed notebook with the conclusion cells and the summary removed, the
505:  results:
666:- date: '2026-11-09'
667:  kind: agent
668:  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
669:  reviewed: Round 2. The full executed notebook of the first revision (commit 9e50d4b6e6), the helper
674:  results:
    response: Outcome kept; recomputed with the calibrated null under both spectra readings.
  - claim: fig5a-spatiotemporal-bidirectional
    agrees: true
    outcome: not_reproduced
    reason: Under reading (b), the reading whose pair selection matches directional-pairs, the grand
      mean passes |z| >= 1.96 at 42 and 40 of 91 points (maximum 5.44 and 6.36). Under reading (a)
      every |z| < 1.96, but (a) shows nothing anywhere, including where the paper reports |z| of about
      40, so the absence there is uninformative.
    response: Outcome kept, resting on PSI reading (b). With the calibrated null reading (b) selects
      one pair, whose spatial and temporal z pass 1.96 at 16 and 11 points; the notes say that its
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 666,676p attempts/crcns-fcx-3-johnson-2019-01.yaml; tail -5 attempts/crcns-fcx-3-johnson-2019-01.yaml; ls transcripts/crcns-fcx-3/; git log -3 --format='%h %s' -- transcripts/crcns-fcx-3/verifier-3-report.md
```

```
- date: '2026-11-09'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 2. The full executed notebook of the first revision (commit 9e50d4b6e6), the helper
    module, the claims file and this record, with the paper. It agreed with 16 of the 17 outcomes and
    disagreed with fig4c-alpha-beta-shift; of its round-1 points it found 7 resolved and 3 (the PSI
    null, pairs treated as independent, the timing of the 1150-ms trials) partly resolved and bearing
    on a conclusion. It quoted six passages the outputs do not support.
  results:
  - claim: table1-electrodes
    agrees: true
      subject-level test is shown. Under reading (a) the outcome is partial.
    response: Outcome kept as round 2 does not allow a change, and partially_reproduced proposed for
      a third round under reading (a), now adopted, which finds no FDR-significant point. A paired test
      on subject means at each time point is now printed; under reading (b) it finds no point after
      FDR either (smallest p 0.0029 and 0.0078).
answer-report.md
answer.md
author-answers-report.md
author-answers.md
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('entries/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if any(k in s for k in ['fig4c-alpha-beta-shift','fig5a-spatiotemporal','fig5b-alpha-beta','proposed','Summary','summary','## Conclusion','round 2']):
        print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'));print(s[:3000])
E
```

```
===== 0 markdown None
# Reproducing Johnson et al. (2019) from CRCNS data set fcx-3

**Paper.** Johnson EL, King-Stephens D, Weber PB, Laxer KD, Lin JJ, Knight RT (2019). Spectral
imprints of working memory for everyday associations in the frontoparietal network. *Frontiers in
Systems Neuroscience* 12, 65. [doi:10.3389/fnsys.2018.00065](https://doi.org/10.3389/fnsys.2018.00065).
The claims file was written from the version of record (PMC6333050, open access); the paper has no
supplement.

**Data set.** CRCNS fcx-3, [doi:10.6080/K06971S9](https://doi.org/10.6080/K06971S9), read from the
public bucket `crcnsarchive` under `fcx-3/live/`. CRCNS data sets are not versioned, so the version
is recorded as `unversioned` (docs/archives.md). The paper cites no version; `live/` is the only
copy the bucket holds (there is no `old/`), with its files dated 2026-02-11 and the data
description version 0.5 of 2019-01-04, the original version. The MD5 sums of the files read, from
the data set's `checksums.md5`, are printed below, so that a later change is detectable.

**What the data set holds.** For each of the 7 subjects: the filtered continuous iEEG
(`data_primary.mat`), channel names, electrode positions, the preprocessed epochs
(`data_derived.mat`: pretrial, encoding and maintenance, and processing epochs of every channel
kept, with a per-trial table of accuracy, condition, delay and RT) and a trial table with the epoch
[... 300 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('entries/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb'))
for i in (43,67):
    s=''.join(nb['cells'][i]['source']); print('=====',i); print(s[2500:] if i==43 else s[3000:])
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='markdown' and ('propos' in s or 'third round' in s or 'as verified' in s): print('HIT',i)
E
grep -n "propos\|third\|as verified\|reading (b)" entries/crcns-fcx-3-johnson-2019/README.md; grep -n "^[a-z_]*:" attempts/crcns-fcx-3-johnson-2019-01.yaml
```

```
===== 43
ing; a calibrated z then
exceeds 1.96 in about 5% of pairs. Positive z: PFC leads.

P1 also leaves open whether each shuffle permutes the bins in the same way for all trials (null
reading (a), used above) or with its own permutation per trial (null reading (b)); both are run for
readings (a) and (b) (`a_trial`, `b_trial`).

**Which reading is adopted.** Where the readings give different outcomes, reading (a) with null
reading (a) is adopted: it is the first P1 lists, the measure of Nolte et al. (2008), and the one
whose z is calibrated. On the trial-shuffled data below, its z has mean -0.05 (delta-theta) and
0.02 (alpha-beta), SD 1.01 and 1.04, and passes |z| > 1.96 in 6.0% and 6.9% of pairs. Reading (b)
has mean -0.29 and SD 0.60 in delta-theta (0.1% of pairs pass), and its subject means on the
trial-shuffled data run from -1.25 to 0.52 in alpha-beta, where the true value is 0. On independent
synthetic signals (the cell after the calibration) its mean z is -0.21 to -0.37, where reading (a)
gives -0.07 to -0.15 with SD near 1. Moving the FFT's time origin to the centre of the segment
brings reading (b)'s mean to -0.06 to 0.12, which is consistent with the offset coming from the
phase slope that each trial's spectrum carries from the segment's position in the padded window:
the per-trial phasors of reading (b) keep it, the frequency shuffle breaks it, and the trial-averaged
cross-spectrum of reading (a) cancels it. One permutation per trial does not help reading (b)
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('entries/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb'))
s=''.join(nb['cells'][67]['source']); i=s.find('(4) PSI'); print(repr(s[i:i+900]))
print(type(nb['cells'][67]['source']))
E
sed -n 1,60p entries/crcns-fcx-3-johnson-2019/README.md
```

```
"(4) PSI from trial-averaged cross-spectra (reading (a), Nolte et al. 2008) or per trial\n(reading (b)), each with one permutation for all trials or one per trial: reading (a) with one\npermutation for all trials is now adopted where the readings differ, because its z is calibrated\non trial-shuffled and on synthetic independent data and reading (b)'s is not (its mean is offset\nby up to -1.25 per subject on the trial-shuffled data). Three outcomes verified under reading (b)\nare kept, and the change reading (a) gives is proposed: fig4c-alpha-beta-shift to not reproduced,\nfig5a-spatiotemporal-bidirectional to reproduced (an absence the measure shows in every\ncondition), and fig5b-alpha-beta-no-sustained to partially reproduced. (5) The baseline z-score of power is computed in closed form; it cannot change\nthe condition t-tests. (6) The mixed models are computed as paired tests over pairs, whic"
<class 'list'>
# Johnson, King-Stephens, Weber, Laxer, Lin & Knight (2019) from CRCNS fcx-3

Tests the findings of [Johnson et al. (2019)](https://doi.org/10.3389/fnsys.2018.00065) on CRCNS
data set [fcx-3](https://doi.org/10.6080/K06971S9), which holds intracranial recordings from
prefrontal and parietal cortex of 7 patients doing a visuospatial working memory task, with the
preprocessed epochs and the paper's MATLAB scripts.

| Claim | Outcome |
|---|---|
| 192 analysed electrodes and 1129 pairs (Table 1) | Partially reproduced |
| Trials kept per subject and condition | Reproduced |
| Accuracy 0.63 to 0.98, no effect of condition | Reproduced |
| Identity RT longer than spatial and temporal | Reproduced |
| No ERP difference between conditions | Not reproduced (assumption) |
| Power, identity against spatial (Figure 2) | Partially reproduced |
| Power, identity against temporal (Figure 3) | Partially reproduced |
| Identity > effects in the subjects with lower identity accuracy | Reproduced |
| Power effects at 2-7 and 9-24 Hz | Reproduced (assumption) |
[... 28 more lines not kept]
```

**Agent**

Verifier agreed with all three proposals. Applying them to the notebook first.

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
p='entries/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb'
nb=json.load(open(p))
def setsrc(i,s):
    lines=s.split('\n'); nb['cells'][i]['source']=[l+'\n' for l in lines[:-1]]+[lines[-1]]
def rep(i,old,new):
    s=''.join(nb['cells'][i]['source']); assert old in s,(i,old[:40]); setsrc(i,s.replace(old,new))
rep(43,"""Three
outcomes rested on it (fig4c-alpha-beta-shift, fig5a-spatiotemporal-bidirectional,
fig5b-alpha-beta-no-sustained); they keep the outcome that round reviewed, and the change that
reading (a) gives is proposed for a third round.""","""Three
outcomes rested on it (fig4c-alpha-beta-shift, fig5a-spatiotemporal-bidirectional,
fig5b-alpha-beta-no-sustained); the change that reading (a) gives was proposed for a third round,
whose verifier agreed with all three, and they now rest on reading (a).""")
setsrc(52,"""**Result: not reproduced, resting on PSI reading (a).** Under reading (a), whose z is calibrated
and which is adopted, 5 of 7 subjects have processing alpha-beta PSI z below 0 (mean -0.14 +- 0.26),
fewer than the 6 the partial match needs, and processing is higher than maintenance by 0.11 in the
pair-level model (F = 6.7, p = 0.0097; paper F = 2302.30); one permutation per trial gives the same
5 of 7. Observed minus the trial-shuffled surrogate is -0.01 +- 0.23 (p = 0.93). Under reading (b),
6 of 7 subjects are below 0 (S3 is above, 0.46) and processing exceeds maintenance (by 0.43,
F(1,2268) = 97.9, p = 1.2e-22), which would be the partial match by the letter, but the outputs above
show that this comes from reading (b)'s null. On the trial-shuffled data, which have no trial-locked
coupling, reading (b) gives subject means of -1.17, -0.40, 0.52, -0.55, -0.60, -1.25 and 0.03 (S1 to
S7), close to the observed -1.07, -0.51, 0.46, -0.61, -0.72, -1.35 and -0.18 (observed minus
surrogate -0.08 +- 0.09, paired t(6) p = 0.061), and on synthetic independent signals reading (b)'s
mean z is -0.25 to -0.29 in alpha-beta. The second verification round reviewed partially
reproduced under reading (b); the change was proposed and the third round agreed. Subject means are
-0.49 to 0.19 under (a) and -1.35 to 0.46 under (b), against the paper's -12.60 +- 7.51; on subject
means the interval difference is not significant under either reading (paired t(6) p = 0.48 and
0.27). On the 900-ms-delay trials alone 4 (a) or 6 (b) subjects are below 0.""")
setsrc(63,"""**Result: reproduced, resting on PSI reading (a), and showing little.** Under reading (a), adopted
because its z is calibrated (see the task-induced PSI section and fig4c-alpha-beta-shift), the
selection holds 78 pairs in 7 subjects and the grand means stay at or below 0.87 (spatial) and 1.01
(temporal), under 1.96 at every time point and under the paper's 1.60, which the criterion counts as
reproduced. The absence shows little: under reading (a) the identity-trial grand mean also stays
below 0.99, where the paper reports |z| above 2.35, so this measure shows no direction in any
condition, and the 78 pairs are about as many as the trial-shuffled data select (68). Under reading
(b) the selection leaves one pair (S1); its spatial-trial z reaches |z| = 3.07 (140 ms) and its
temporal-trial z 2.36 (180 ms), with 16 and 11 of 91 time points at |z| >= 1.96, but its
identity-trial z also passes 1.96 at 9 points, so on one pair such excursions are common. The second
verification round reviewed not reproduced under reading (b); the change was proposed and the third
round agreed. With the whole-epoch windows, reading (a) gives 0.37 and 0.56 and reading (b) 2.54 and
3.03.""")
setsrc(66,"""**Result: partially reproduced, resting on PSI reading (a).** Under reading (a), adopted (see
fig4c-alpha-beta-shift; 104 pairs in 7 subjects), no point is significant after FDR in the
pair-level model (smallest p 0.0015 and 0.0027) or in the subject-level test (0.016 and 0.024), under
either spectra reading, the criterion's partial match. Under reading (b) (74 pairs in 6 subjects), 30
(identity against spatial) and 35 (against temporal) of 91 time points differ after FDR in the
pair-level model, and the longest run of one sign lasts 40 ms (whole-epoch windows: 36 and 37 points,
longest 50 and 40 ms). Those points come from the pair-level model alone. The 74 pairs are about as
many as the trial-shuffled data select under the same reading (71), S3 supplies 44 of them, and the
model treats pairs that share electrodes as independent; the paired test on the 6 subjects' means
finds no point after FDR (smallest p 0.0029 and 0.0078). The second verification round reviewed
reproduced under reading (b); the change was proposed and the third round agreed. No reading shows
a sustained run.""")
rep(67,"| fig4c-alpha-beta-shift | partially reproduced (assumption: PSI reading (b)); not reproduced proposed |","| fig4c-alpha-beta-shift | not reproduced (assumption: PSI reading (a)) |")
rep(67,"| fig5a-spatiotemporal-bidirectional | not reproduced (assumption: PSI reading (b)); reproduced proposed |","| fig5a-spatiotemporal-bidirectional | reproduced (assumption: PSI reading (a); the measure shows no direction in any condition) |")
rep(67,"| fig5b-alpha-beta-no-sustained | reproduced (assumption: PSI reading (b)); partially reproduced proposed |","| fig5b-alpha-beta-no-sustained | partially reproduced (assumption: PSI reading (a)) |")
rep(67,"""Three outcomes verified under reading (b)
are kept, and the change reading (a) gives is proposed: fig4c-alpha-beta-shift to not reproduced,
fig5a-spatiotemporal-bidirectional to reproduced (an absence the measure shows in every
condition), and fig5b-alpha-beta-no-sustained to partially reproduced.""","""Three outcomes verified under reading (b)
were changed to what reading (a) gives, after a third verification round agreed:
fig4c-alpha-beta-shift to not reproduced, fig5a-spatiotemporal-bidirectional to reproduced (an
absence the measure shows in every condition), and fig5b-alpha-beta-no-sustained to partially
reproduced.""")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
git diff --stat entries/
```

```
.../reproduce_johnson_2019.ipynb                   | 94 +++++++++++-----------
 1 file changed, 48 insertions(+), 46 deletions(-)
```

**Agent**

Now the README.

**Agent calls Bash**

```bash
cd  python - <<'E'
p='entries/crcns-fcx-3-johnson-2019/README.md'
s=open(p).read()
for o,n in [("| Partially reproduced (assumption); not reproduced proposed |","| Not reproduced (assumption) |"),
 ("| Not reproduced (assumption); reproduced proposed |","| Reproduced (assumption) |"),
 ("| Reproduced (assumption); partially reproduced proposed |","| Partially reproduced (assumption) |"),
 ("""readings differ, since its z is calibrated and that of per-trial PSI is not; three outcomes verified
under the per-trial reading are kept, with the change proposed for a further verification round.""",
 """readings differ, since its z is calibrated and that of per-trial PSI is not; three outcomes first
verified under the per-trial reading were changed to this reading's after a third verification
round agreed. Under it, spatial and temporal PSI show no direction, as the claim says, but neither
does identity PSI, so that match shows little.""")]:
    assert o in s,o; s=s.replace(o,n)
open(p,'w').write(s)
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
date -u
```

```
Mon Nov  9 04:08:12 UTC 2026
```

**Agent**

Now the attempt record's three outcomes.

**Agent calls Bash**

```bash
cd  python - <<'E'
p='attempts/crcns-fcx-3-johnson-2019-01.yaml'
s=open(p).read()
a=s.index('- claim: fig4c-alpha-beta-shift'); b=s.index('- claim: directional-pairs')
s=s[:a]+'''- claim: fig4c-alpha-beta-shift
  outcome: not_reproduced
  assumed: true
  notebook: reproduce_johnson_2019.ipynb
  output: claim:fig4c-alpha-beta-shift
  measured:
  - -0.14
  - 6.7
  notes: Under PSI reading (a), adopted because its z is calibrated, 5 of 7 subjects have processing
    alpha-beta PSI z below 0 (mean -0.14 +- 0.26, recorded; paper -12.60 +- 7.51), fewer than the 6
    the partial match needs; one permutation per trial also gives 5. Processing is higher than
    maintenance by 0.11 in the pair-level model (F = 6.7, recorded, p = 0.0097; paper F = 2302.30).
    Under reading (b), 6 of 7 subjects are below 0 (S3 is above, 0.46; mean -0.57 +- 0.59) and
    processing exceeds maintenance by 0.43 (F(1,2268) = 97.9, p = 1.2e-22), but that reading's
    trial-shuffled surrogate gives nearly the same subject means (-1.17, -0.40, 0.52, -0.55, -0.60,
    -1.25 and 0.03, against the observed -1.07, -0.51, 0.46, -0.61, -0.72, -1.35 and -0.18; observed
    minus surrogate -0.08 +- 0.09, paired t(6) p = 0.061), and on synthetic independent signals its
    mean z is -0.25 to -0.29 in alpha-beta, so its 6 of 7 comes from its null. Under reading (a)
    observed minus surrogate is -0.01 +- 0.23 (p = 0.93). On subject means the interval difference is
    not significant under either reading (paired t(6) p = 0.48 under (a), 0.27 under (b)). Round 2
    reviewed partially reproduced under reading (b); the change to not reproduced was proposed and
    round 3 agreed.
  deviations:
  - As fig4a-delta-theta-shift. The outcome rests on PSI reading (a) (see
    fig4-maintenance-parietal-led).
'''+s[b:]
a=s.index('- claim: fig5a-spatiotemporal-bidirectional'); b=s.index('- claim: fig5b-alpha-beta-no-sustained')
s=s[:a]+'''- claim: fig5a-spatiotemporal-bidirectional
  outcome: reproduced
  assumed: true
  notebook: reproduce_johnson_2019.ipynb
  output: claim:fig5a-spatiotemporal-bidirectional
  notes: Under PSI reading (a), adopted (78 pairs in 7 subjects), the spatial-trial and
    temporal-trial grand means stay at or below 0.87 and 1.01, under 1.96 at every one of the 91 time
    points and under the paper's 1.60, which the criterion counts as reproduced. The match shows
    little. Under this reading the identity-trial grand mean also stays below 0.99, where the paper
    reports |z| above 2.35, and the 78 pairs are about as many as the trial-shuffled data select (68).
    With the whole-epoch windows, reading (a) gives 0.37 and 0.56. Under reading (b) the selection
    leaves one directional pair (S1); its spatial-trial z reaches |z| = 3.07 (140 ms) and its
    temporal-trial z 2.36 (180 ms), with 16 and 11 points at |z| >= 1.96 (whole-epoch windows, 2.54
    and 3.03), but its identity-trial z also passes 1.96 at 9 points, so on one pair such excursions
    are common. Round 2 reviewed not reproduced under reading (b); the change to reproduced was
    proposed and round 3 agreed.
  deviations:
  - The outcome rests on PSI reading (a) (see fig4-maintenance-parietal-led). As
    fig5a-delta-theta-epochs otherwise.
'''+s[b:]
a=s.index('- claim: fig5b-alpha-beta-no-sustained'); b=s.index('findings:')
s=s[:a]+'''- claim: fig5b-alpha-beta-no-sustained
  outcome: partially_reproduced
  assumed: true
  notebook: reproduce_johnson_2019.ipynb
  output: claim:fig5b-alpha-beta-no-sustained
  notes: Under PSI reading (a), adopted (104 pairs in 7 subjects), no time point differs between
    conditions after FDR in the pair-level model (smallest p 0.0015 against spatial, 0.0027 against
    temporal), in the whole-epoch variant or in a paired test on subject means (0.016 and 0.024),
    which the criterion counts as partially reproduced. Under reading (b) (74 pairs in 6 subjects), 30
    (identity against spatial) and 35 (against temporal) of 91 time points differ after FDR in the
    pair-level model (whole-epoch windows, 36 and 37), but the trial-shuffled data select 71 pairs
    under the same reading, S3 supplies 44 of the 74, and a paired test on the 6 subjects' means finds
    no point after FDR (smallest p 0.0029 and 0.0078). No reading shows a sustained run (longest 40 to
    50 ms). Round 2 reviewed reproduced under reading (b); the change to partially reproduced was
    proposed and round 3 agreed.
  deviations:
  - The outcome rests on PSI reading (a) (see fig4-maintenance-parietal-led). As
    fig5a-delta-theta-epochs otherwise.
'''+s[b:]
s=s.rstrip('\n')+'\n'+'''- date: '2026-11-09'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 3. The three proposed changes of outcome (fig4c-alpha-beta-shift,
    fig5a-spatiotemporal-bidirectional, fig5b-alpha-beta-no-sustained) and the analysis behind them in
    the re-executed notebook of the second revision (commit 5d5c03884d), without downloading the data
    or re-running. It agreed with all three, found the switch to PSI reading (a) supported by the
    calibration outputs and not steered by the outcomes (it lowers two and raises one), asked that
    assumed stay on all three, and found no new place where the claims file misreads the paper.
  results:
  - claim: fig4c-alpha-beta-shift
    agrees: true
    outcome: not_reproduced
    reason: Reading (a), cell 50, has 5 of 7 subjects below 0 in processing (mean -0.14 +- 0.26). The
      pair-level model holds (processing higher by 0.11, F = 6.7, p = 0.0097; cell 49), but the partial
      match needs at least 6 subjects below 0, and the per-trial-permutation version of (a) also gives
      5 of 7. Reading (b)'s 6 of 7 is reproduced by its own trial-shuffled surrogate; observed minus
      surrogate is -0.08 +- 0.09 (p = 0.061) under (b) and -0.01 +- 0.23 (p = 0.93) under (a) (cell 50),
      so the 6 of 7 comes from (b)'s offset, not from coupling in the data. Every reading is far from
      the paper's -12.60 and F = 2302. The numbers in the proposed reason match cells 45, 46, 49 and 50.
    response: Outcome changed to not_reproduced and the proposal removed; assumed kept, and the notes,
      notebook conclusion, summary and README now give reading (a)'s values first.
  - claim: fig5a-spatiotemporal-bidirectional
    agrees: true
    outcome: reproduced
    reason: Yes, by the letter. Under reading (a), cell 62, 78 pairs in 7 subjects; the spatial-trial
      and temporal-trial grand means peak at 0.87 and 1.01, so every one of the 91 time points is below
      1.96, the criterion as written, and below the paper's 1.60. The result shows very little, as the
      record says. The identity-trial grand mean under (a) also stays below 0.99 where the paper
      reports |z| > 2.35, the 78 selected pairs are about what the trial-shuffled surrogate selects
      (68; cell 53), and the whole-epoch variant gives 0.37 and 0.56. Reading (b)'s failure rests on a
      single S1 pair whose identity-trial z also passes 1.96 at 9 points, so it is not evidence against
      the claim. Not checked, the surrogate calibration covers the task-induced PSI only, not the
      time-resolved PSI; this does not change the outcome.
    response: Outcome changed to reproduced and the proposal removed; assumed kept. The notes and the
      notebook conclusion say the match shows little and add the surrogate's 68 pairs. The calibration
      of the time-resolved PSI was not checked; that would need a new analysis, left for a later
      attempt.
  - claim: fig5b-alpha-beta-no-sustained
    agrees: true
    outcome: partially_reproduced
    reason: Under reading (a), cell 64, 104 pairs in 7 subjects. No time point is FDR-significant in
      either contrast (smallest p 0.0015 and 0.0027), and none is in the whole-epoch variant; the
      criterion counts that as partially reproduced. The subject-level test, cell 65, finds no point
      under either reading. Reading (b)'s 30 and 35 significant points come only from the pair-level
      model on 74 pairs, about what the surrogate selects (71; cell 53), with S3 supplying 44 of them
      (cell 65). There are no sustained runs under any reading (longest 40 to 50 ms), so the outcome is
      not "not reproduced".
    response: Outcome changed to partially_reproduced and the proposal removed; assumed kept, and the
      notes, notebook conclusion, summary and README updated.
'''
open(p,'w').write(s)
E
python -c "import yaml;d=yaml.safe_load(open('attempts/crcns-fcx-3-johnson-2019-01.yaml'));print([ (o['claim'],o['outcome'],'proposed' in o) for o in d['outcomes'] if o['claim'].startswith(('fig4c','fig5'))], len(d['verifications']))"
```

```
[('fig4c-alpha-beta-shift', 'not_reproduced', False), ('fig5a-delta-theta-epochs', 'not_reproduced', False), ('fig5a-identity-direction', 'not_reproduced', False), ('fig5a-spatiotemporal-bidirectional', 'reproduced', False), ('fig5b-alpha-beta-no-sustained', 'partially_reproduced', False)] 3
```

**Agent calls Bash**

```bash
cd  grep -n "propos\|round 2 reviewed\|as verified" attempts/crcns-fcx-3-johnson-2019-01.yaml | head -30; git diff -U0 attempts/ | grep '^+' | grep -n '[^ ]: ' | grep -v "^\S*+ *[-a-z_]*: \|^\S*+  - [a-z_]*: "
```

```
304:    reviewed partially reproduced under reading (b); the change to not reproduced was proposed and
380:    proposed and round 3 agreed.
398:    proposed and round 3 agreed.
752:    response: Outcome kept as round 2 does not allow a change, and not_reproduced proposed for a third
788:    response: Outcome kept as round 2 does not allow a change, and reproduced proposed for a third
799:    response: Outcome kept as round 2 does not allow a change, and partially_reproduced proposed for
806:  reviewed: Round 3. The three proposed changes of outcome (fig4c-alpha-beta-shift,
822:      the paper's -12.60 and F = 2302. The numbers in the proposed reason match cells 45, 46, 49 and 50.
823:    response: Outcome changed to not_reproduced and the proposal removed; assumed kept, and the notes,
837:    response: Outcome changed to reproduced and the proposal removed; assumed kept. The notes and the
851:    response: Outcome changed to partially_reproduced and the proposal removed; assumed kept, and the
48:+- date: '2026-11-09'
```

**Agent**

Record updated. Now the full re-run (about 43 minutes per the README).

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/crcns-fcx-3-johnson-2019 > $TMPDIR/all.log 2>&1; echo exit $?; date -u; tail -40 $TMPDIR/all.log
```

```
Mon Nov  9 04:08:49 UTC 2026
exit 0
Mon Nov  9 04:49:19 UTC 2026
Installed kernelspec registry-crcns-fcx-3-johnson-2019 in executed/crcns-fcx-3-johnson-2019/.venv/share/jupyter/kernels/registry-crcns-fcx-3-johnson-2019
0 error(s)
pass  reproduce_johnson_2019.ipynb  (2420 s)
```

**Agent**

Run passed. Checking that the re-executed outputs still give the recorded numbers.

**Agent calls Bash**

```bash
cd  ls executed/crcns-fcx-3-johnson-2019/; python - <<'E'
import json,glob
p=[f for f in glob.glob('executed/crcns-fcx-3-johnson-2019/*.ipynb')][0]
nb=json.load(open(p))
for i in (50,62,64,65):
    out=''.join(''.join(o.get('text','')) for o in nb['cells'][i].get('outputs',[]))
    for l in out.splitlines():
        if any(k in l for k in ['reading (a)','(a)','below 0:','smallest','grand','pairs']): print(i,l[:220])
E
```

```
reproduce_johnson_2019.ipynb
result.json
50   (a) trial-averaged coherency: subjects above 0: 0/7 []; mean of 7 -0.17 +- 0.16; mean of those above 0 nan; model effect +0.06, F 2.2, p 0.14
50   (a), one permutation per trial (P1 null (b)): subjects above 0: 0/7 []; mean of 7 -0.21 +- 0.20; mean of those above 0 nan; model effect +0.10, F 4.3, p 0.038
50   (a) trial-averaged coherency: subjects below 0: 5/7; mean -0.14 +- 0.26; model effect +0.11, F 6.7, p 0.00965
50   (b) per-trial PSI averaged: subjects below 0: 6/7; mean -0.57 +- 0.59; model effect +0.43, F 97.9, p 1.24e-22
50   (a), one permutation per trial (P1 null (b)): subjects below 0: 5/7; mean -0.14 +- 0.26; model effect +0.12, F 7.2, p 0.00723
50   (b), one permutation per trial (P1 null (b)): subjects below 0: 6/7; mean -0.76 +- 0.82; model effect +0.66, F 119.1, p 4.57e-27
50   (b) against psianalysis.m's null (variant): subjects below 0: 5/7; mean -1.84 +- 10.36; model effect +8.79, F 115.3, p 2.85e-26
50   deposited code, PFC first (not a reading): subjects below 0: 0/7; mean 71.37 +- 10.61; model effect -7.41, F 47.9, p 5.85e-12
50   deposited code, parietal first, sign reversed (not a reading): subjects below 0: 7/7; mean -73.46 +- 8.79; model effect +5.07, F 21.9, p 2.98e-06
50   (a) trial-averaged coherency: observed {'s1': -0.31, 's2': -0.05, 's3': 0.18, 's4': -0.16, 's5': -0.31, 's6': -0.49, 's7': 0.19}; surrogate {'s1': 0.01, 's2': -0.12, 's3': 0.09, 's4': -0.38, 's5': -0.02, 's6': -0.4, 's
50   (a), one permutation per trial (P1 null (b)): observed {'s1': -0.33, 's2': -0.04, 's3': 0.18, 's4': -0.22, 's5': -0.3, 's6': -0.45, 's7': 0.2}; surrogate {'s1': 0.04, 's2': -0.12, 's3': 0.09, 's4': -0.36, 's5': -0.02, 
50   delta-theta, (a) trial-averaged coherency: above 0 2/7, below 0 5/7; mean -0.14 +- 0.17; {'s1': -0.16, 's2': 0.01, 's3': -0.04, 's4': -0.34, 's5': -0.2, 's6': -0.34, 's7': 0.08}
50   alpha-beta, (a) trial-averaged coherency: above 0 3/7, below 0 4/7; mean -0.14 +- 0.32; {'s1': -0.54, 
[... 34 more lines not kept]
```

**Agent**

All recorded numbers match the new outputs. The run took 2420 s (40.3 min), a bit under the "41 to 43 minutes" the README and notebook give, so I'm updating that range.

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
nb=json.load(open('executed/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb'))
print(''.join(''.join(o.get('text','')) for o in nb['cells'][2]['outputs'])[-60:])
E
```

```
s7: streamed and analysed in 99 s
all subjects in 39.4 min
```

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
p='entries/crcns-fcx-3-johnson-2019/reproduce_johnson_2019.ipynb'
nb=json.load(open(p))
s=''.join(nb['cells'][0]['source']); o="takes nearly the whole run, 40 to 42\nminutes of 41 to 43 in two runs."
assert o in s
s=s.replace(o,"takes nearly the whole run, 39 to 42\nminutes of 40 to 43 in three runs.")
l=s.split('\n'); nb['cells'][0]['source']=[x+'\n' for x in l[:-1]]+[l[-1]]
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
r='entries/crcns-fcx-3-johnson-2019/README.md'; t=open(r).read()
o="It takes 41 to 43 minutes, 40 to 42 of them"; assert o in t
open(r,'w').write(t.replace(o,"It takes 40 to 43 minutes, 39 to 42 of them"))
E
git diff --stat; python tools/entry.py check entries/crcns-fcx-3-johnson-2019 2>&1 | tail -5
```

```
attempts/crcns-fcx-3-johnson-2019-01.yaml          | 163 ++++++++++++---------
 entries/crcns-fcx-3-johnson-2019/README.md         |  14 +-
 .../reproduce_johnson_2019.ipynb                   |  98 +++++++------
 tools/build_site.py                                |   8 +-
 4 files changed, 160 insertions(+), 123 deletions(-)
0 error(s)
```

**Agent**

The round-3 verifier agreed with all three proposed changes, so all three outcomes changed and no proposal is left standing.

**Outcomes changed** (`assumed: true` stays on all three, as the verifier asked):
- **fig4c-alpha-beta-shift**: partially reproduced → not reproduced. Under PSI reading (a), 5 of 7 subjects are below 0, and the partial match needs 6. The recorded values are now reading (a)'s: -0.14 and F = 6.7.
- **fig5a-spatiotemporal-bidirectional**: not reproduced → reproduced. It meets the criterion as written, but shows little. Under reading (a) the identity grand mean also stays below 0.99, where the paper reports more than 2.35. The 78 pairs selected are also about what the trial-shuffled control selects (68).
- **fig5b-alpha-beta-no-sustained**: reproduced → partially reproduced. Under reading (a) no time point is significant after FDR correction.

**Other updates**
- The `proposed` blocks are removed. I rewrote the notes and deviations of those three claims around reading (a) and added round 3 under `verifications`, with the verifier's reasons and my responses.
- The notebook's three conclusion cells, the summary table and item (4), the adopted-reading paragraph, and the README table and PSI paragraph now give the new outcomes.
- One point the verifier said it had not checked: the calibration of the time-resolved PSI. That needs a new analysis, so the record leaves it for a later attempt.

**Run**: `python tools/entry.py all entries/crcns-fcx-3-johnson-2019` passed with 0 errors in 2420 s. Every value cited in the record matches the re-executed outputs. That run was a little faster than the stated range, so I changed the runtime text in the notebook and README to 40 to 43 minutes. `entry.py check` passes again after that edit. The executed copy still has the old runtime sentence in its first markdown cell, which affects no result.

Nothing is committed. The working tree also has a change to `tools/build_site.py` that was there before this run; I didn't touch it.

## End of run

21 turns, 43 minutes, $0.85 at API prices, result: success.
