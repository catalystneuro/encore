# pasquereau-2013 · author-revise-3 · run 45889581517

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/pasquereau-2013/verifier-3-report.md; ls entries/pasquereau-2013; grep -n "step 6\|^## \|^### " docs/protocol.md | head -60
```

```
Thu Nov 26 20:20:32 UTC 2026
## Round 3 verifier report: proposed changes of outcome

I took the claims and outcomes from `pasquereau-2013.yaml` and `pasquereau-2013-03.yaml`. The attempt record has `proposed` on four outcomes: kinematic-latency-unchanged, emg-duration-longer, emg-onset-unchanged and emg-m1-weak. I agree with none of the four and would keep every outcome as verified in round 2. Cell indices below refer to the re-executed notebook.

| Claim | Proposed outcome | Agree | My outcome | Reason |
|---|---|---|---|---|
| kinematic-latency-unchanged | reproduced | No | not_reproduced (unchanged) | The criterion is applied to the session means over all perturbations: MPTP F = 709.5, p = 1.5e-102 (cell 68). The proposal decides instead on an equal-pulse subset the claims file does not define, from cell 65. That subset has 4 pre-MPTP sessions per direction at 175 to 185 units and 15 post-MPTP flexion sessions at 85 to 95 units, which is little power for an absence claim. The subset results also depend on the filter. With the claims file's onset, p = 0.16 and 0.98. With the causal filter, p = 0.0027 at 85 to 95 units, which by the criterion is not reproduced. In round 2 the author showed the claims file's onset is the measure that suffers the filter artifact. The numbers in cell 65 derive from the data as stated. |
| emg-duration-longer | not_reproduced | No | partially_reproduced (unchanged) | As written, the criterion is met at partial over all channel-sessions: 22.2 against 51.5 ms, KS p = 5.2e-33, with both means outside tolerance (cell 78). The proposal rests on the subsets in cell 75. These have 14 post-MPTP channel-sessions at 85 to 95 units and 5 pre-MPTP at 175 to 185 units. A non-significant result on so few cannot overturn the comparison the criterion specifies. The cell 75 numbers (32.4 against 24.1 ms, p = 0.32; 27.0 against 46.7 ms, p = 0.087) match the record. |
| emg-onset-unchanged | reproduced | No | not_reproduced (unchanged) | The criterion c
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 502,670p docs/protocol.md; sed -n 805,880p docs/protocol.md; ls attempts 2>/dev/null | head; find . -name "pasquereau-2013-03.yaml"
```

```
### 5. Record the attempt

Write `attempts/<paper>-<nn>.yaml`, numbered after the paper's earlier attempts.

- **`datasets`**: every dataset the attempt used, each with `archive`, `id`,
  the pinned `version`, its `doi` where the archive gives one, and
  `relation` as `papers/datasets/<paper>.yaml` gives it (`primary` or
  `reuses`). Use as many of the paper's datasets as can be loaded.
- **`missing_datasets`**: each dataset the paper's claims rest on that this
  attempt could not use, with `archive` and `id` where it has them, and
  `why` (not in any open archive, not yet converted, unreadable). A missing
  dataset does not stop the attempt: test what the others allow, and block
  each claim that needs a missing one with `dataset_missing`. The site flags
  the attempt, so that a later one can add the dataset.

- **One outcome per claim**, including blocked ones. The outcome describes the
  result, not the method:
  - `reproduced`: the result matches the claim.
  - `partially_reproduced`: the effect is present but weaker, or holds only in
    part.
[... 169 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l attempts/pasquereau-2013-03.yaml; grep -n "proposed\|^verifications\|^  - round\|round:" attempts/pasquereau-2013-03.yaml
```

```
923 attempts/pasquereau-2013-03.yaml
316:  proposed:
337:    and no change is proposed. The background differs between states: the median single-trial baseline SD
362:  proposed:
382:  proposed:
405:  proposed:
492:verifications:
864:    response: Outcome kept as verified (not_reproduced); a change to reproduced is proposed. The conclusion and
869:      under 1 ms, and p = 0.69 at 175 to 185. Since the paper applied one torque, the proposed outcome is reproduced;
870:      see proposed on the outcome.
880:    response: No change of outcome and none proposed. The README and summary no longer call the 60 to 250 range
889:    response: Outcome kept as verified (partially_reproduced); a change to not_reproduced is proposed. At equal
891:      27.0 against 46.7 ms, p = 0.087); see proposed on the outcome.
896:    response: Outcome kept as verified (not_reproduced); a change to reproduced is proposed. At equal pulses the
898:      against 24.9 ms, p = 0.057); see proposed on the outcome.
906:    response: Outcome kept as verified (partially_reproduced); a change to reproduced is proposed. The conclusion
908:      96.3% and 85.7%; 175 to 185 units 80.0% and 95.2%); see proposed on the outcome.
923:      and EMG claims are compared there as variants, and four outcome changes are proposed from them.
```

**Agent calls Bash**

```bash
sed -n 290,420p attempts/pasquereau-2013-03.yaml; sed -n 492,520p attempts/pasquereau-2013-03.yaml; sed -n 800,923p attempts/pasquereau-2013-03.yaml
```

```
units) are shown, not deciding.
- claim: kinematic-latency-unchanged
  outcome: not_reproduced
  notebook: reproduce_pasquereau_2013.ipynb
  output: claim:kinematic-latency-unchanged
  notes: 'Movement onset latency is shorter after MPTP (pre 9.65 and 10.86 ms, post 3.05 and 5.99 ms for flexion
    and extension), MPTP F = 709.5 on 1 and 577 df, p = 1.5e-102; the MPTP by direction interaction is F =
    16.1 (the paper''s F > 94). The forwards-backwards filter moves onsets early after MPTP: 6.7% of post-MPTP
    onsets are at 0 ms with the velocity already above 5 deg/s (0.1% before). The variant with the velocity
    at or below threshold over the 20 ms before onset removes these but not the filter''s spread (pre 10.87
    and 9.65, post 6.13 and 3.38 ms for extension and flexion, F = 596.5; the post-MPTP flexion mean is still
    before the command leaves rest at 4 ms). Only the causal 25 Hz filter avoids both; it also gives shorter
    latencies after MPTP (pre 21.44 and 20.33, post 18.18 and 15.62 ms, F = 422.5), with a smaller difference
    (3.3 and 4.7 ms against 4.9 and 6.6 ms), so the forwards-backwards filter enlarges the difference. The unfiltered
    mean velocity at 10 and 12 ms is 1.7 and 4.0 deg/s before and 5.1 and 13.2 after MPTP. At command pulses
    of 60 to 250 units, still about twofold apart, F = 214.3 and 146.2. At equal pulses the MPTP effect is
    absent with the claims file''s onset (85 to 95 units F = 2.0, p = 0.16; 175 to 185 units F = 0.0, p = 0.98);
    the causal filter gives F = 9.3, p = 0.0027 at 85 to 95 units, with post-MPTP latencies longer by under
    1 ms, and F = 0.2, p = 0.69 at 175 to 185 units.'
  deviations:
[... 264 more lines not kept]
```

**Agent calls Bash**

```bash
grep -ln "Round 3" attempts/*.yaml | head; f=$(grep -ln "Round 3" attempts/*.yaml | head -1); grep -n "Round 3" -A30 $f | head -60; grep -n "proposed" -A8 $f | head -40
```

```
attempts/andrews-2024-01.yaml
attempts/asari-2009-02.yaml
attempts/bech-2026-01.yaml
attempts/bennett-2024-01.yaml
attempts/brudner-2026-01.yaml
attempts/bruno-2017-01.yaml
attempts/chantranupong-2023-01.yaml
attempts/chartrand-2023-01.yaml
attempts/cody-2024-01.yaml
attempts/danish-2017-01.yaml
763:  reviewed: Round 3. The proposed change of outcome for simulation-dampening and the analysis behind it
764-    (cells 27 to 30 of the executed notebook of the final revision), with the script at commit 6865bf6
765-    read by the verifier.
766-  results:
767-  - claim: simulation-dampening
768-    agrees: true
769-    outcome: reproduced
770-    reason: 'Cell 28 builds NEST 3.4 from conda-forge, as the published environment.yml asks, with NESTML
771-      5.3.0, and prints every build step with its exit code. Both changes, odetoolbox pinned to 2.5
772-      and nest-config patched to name the compiler, are to the environment, not the model or the
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
for f in $(grep -ln "Round 3" attempts/*.yaml); do awk '/Round 3/{p=1} p&&/agrees: false/{print FILENAME; exit}' $f; done | head -3
```

```
attempts/gabriel-2025-01.yaml
attempts/grosmark-2016-02.yaml
attempts/prakash-2022-01.yaml
```

**Agent calls Bash**

```bash
sed -n 1,60p entries/pasquereau-2013/entry.yaml | head -30; grep -n -i "propos\|equal pulse\|175 to 185" entries/pasquereau-2013/README.md; python - <<'E'
import json
nb=json.load(open('entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='markdown' and ('ropos' in s or 'equal pulse' in s.lower() or 'Summary' in s):
        print('=====',i,c['metadata'].get('tags'));print(s[:3000])
E
```

```
schema_version: 1
name: pasquereau-2013
type: reproduction
title: Motor cortex responses to muscle stretch in the parkinsonian monkey (Pasquereau & Turner 2013)
description: Tests the findings of Pasquereau and Turner (2013) on dandiset 001636, which holds the
  single-unit recordings from primary motor cortex of two macaques before and after MPTP, with the
  torque perturbations, elbow angle and EMG of monkey V. It counts the cells studied, compares
  baseline rates and antidromic latencies, checks the false-positive rate of the response detection,
  and tests the behavioural and EMG effects of MPTP on the torque-evoked stretch. The monkey L files
  mark no perturbations.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_pasquereau_2013.ipynb
  title: Reproducing Pasquereau & Turner (2013) from dandiset 001636
  runtime_minutes: 11
helpers:
- pasq.py
related:
- id: dandi:001636/0.261124.1906
[... 144 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 25,50p entries/pasquereau-2013/README.md; grep -n -i "propos" attempts/pasquereau-2013-03.yaml | grep -v "^3[0-9][0-9]:\|^40[0-9]:"; awk '/Round 3/{p=1} p' attempts/gabriel-2025-01.yaml | head -30
```

```
A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The response detection the claims file specifies crosses its threshold in 23% of cell-directions
at a pseudo onset, about 20 times the paper's stated 1%, so the claims that rest on the selection
of responses are blocked; their results are shown in the notebook. The torque command's pulses are
larger after MPTP than before (mean 174.7 against 58.4 units, about three times; median 181.6
against 45.7, about four times), and the evoked displacements are faster and larger after MPTP,
the reverse of the paper's; the angle's scale agrees with the task's 20 degree targets and with
the files' own velocity series, so this is in the data. Over all perturbations the evoked movement
starts earlier after MPTP with a causal filter as well as with the claims file's. The two states
share two pulse sizes, near 90 and near 180 units. Compared there, the latency of the evoked
movement and the onset of the EMG response do not change after MPTP, the EMG response is not
longer, and m1 is much smaller than m2 in both states. The record keeps the verified outcomes and
proposes these four changes for a further round of verification. The attempt record, with the
reasons and the differences from the paper's method, is
[`attempts/pasquereau-2013-03.yaml`](../../attempts/pasquereau-2013-03.yaml).

- `reproduce_pasquereau_2013.ipynb`: the analysis. It takes about eleven minutes, most of it
  streaming the files.
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^[a-z_]*:" attempts/pasquereau-2013-03.yaml; grep -n -i "four\|equal pulse" attempts/pasquereau-2013-03.yaml | head -30
```

```
1:schema_version: 3
2:id: pasquereau-2013-03
3:datasets:
9:paper: doi:10.3389/fnsys.2013.00098
10:date: '2026-11-26'
11:entry: pasquereau-2013
12:provenance:
23:outcomes:
420:findings:
492:verifications:
93:    38, p = 0.019). All four means are within tolerance and the PTN test holds, but the CSN test does not reach
196:    are shorter after MPTP in all four comparisons (KS p 0.0077 to 0.010); means M1 flexion 40.9 and 35.5,
243:    of baseline rate across the four categories F = 1.21, p = 0.31. Under the trial_sd reading (three categories
276:    size is not excluded. At equal pulses the displacements are not slower and smaller after MPTP either: at
280:    p = 0.0055). The outcome is the same at equal pulses. Mean displacements are 2.4 to 3.8 degrees, where
289:  - Variants restricted to command pulses of 60 to 250 units and to equal pulses (85 to 95 and 175 to 185
305:    of 60 to 250 units, still about twofold apart, F = 214.3 and 146.2. At equal pulses the MPTP effect is
314:  - Variants restricted to command pulses of 60 to 250 units and to equal pulses (85 to 95 and 175 to 185
319:      pulse is about three to four times the pre-MPTP pulse (finding 3), so the comparison over all perturbations
334:    equal pulses of 85 to 95 units m2 is larger after MPTP in triceps longus 1 (60.6 and 89.3, p = 0.016) and
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 440,465p attempts/pasquereau-2013-03.yaml; sed -n 12,22p attempts/pasquereau-2013-03.yaml
```

```
are faster (+28%) and larger (+15%), where the paper reports them slower (-16.2%) and smaller (-6.6%).
    The angle''s scale is not the cause: voluntary movements to 20 degree targets measure 19.9 and 18.1 degrees,
    and the files'' ElbowVelocity agrees with the derivative of the angle.'
- kind: other
  about: data
  severity: major
  notebook: reproduce_pasquereau_2013.ipynb
  output: finding-torque-command-levels
  statement: The torque command's pulse is larger after MPTP than before (mean 174.7 against 58.4 units, about
    three times; median 181.6 against 45.7, about four times; 125 of 137 post-MPTP sessions have a median
    pulse of 120 to 250 units, 3 of 151 before), where the paper describes one 0.1 Nm pulse throughout. The
    units have no conversion to newton-metres, so whether the applied torque changed cannot be told; the ElbowTorque
    description notes the varying levels. The two states share only two pulse sizes, near 90 units (483 pre-MPTP
    and 227 post-MPTP perturbations) and near 180 units (41 and 1540), so comparisons of evoked movements and
    EMG before and after MPTP over all perturbations cannot separate the torque from the effect of MPTP.
- kind: other
  about: data
  severity: none
  notebook: reproduce_pasquereau_2013.ipynb
  output: sanity
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd attempts && python - <<'E'
p='pasquereau-2013-03.yaml'
s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1,old
    s=s.replace(old,new)
rep("""      longer by under 1 ms (p = 0.0027), not shorter. Notebook, second cell under kinematics-slower.
""","""      longer by under 1 ms (p = 0.0027), not shorter. Notebook, second cell under kinematics-slower. The round-3
      verifier did not agree and keeps not_reproduced. The criterion is applied to the session means over all
      perturbations (F = 709.5, p = 1.5e-102); the equal-pulse subset is not defined by the claims file and
      has 4 pre-MPTP sessions per direction at 175 to 185 units and 15 post-MPTP flexion sessions at 85 to
      95 units, little power for an absence claim; and with the causal filter p = 0.0027 at 85 to 95 units,
      which by the criterion is not reproduced.
""")
rep("""      at 175 to 185). Notebook, cell tagged for the four EMG claims under EMG claims at other torque commands.
""","""      at 175 to 185). Notebook, cell tagged for the four EMG claims under EMG claims at other torque commands.
      The round-3 verifier did not agree and keeps partially_reproduced. Over all channel-sessions, the comparison
      the criterion specifies, it is met at partial (22.2 against 51.5 ms, KS p = 5.2e-33), and a non-significant
      result on 14 and 5 channel-sessions cannot overturn it.
""")
rep("""      earlier after MPTP with p just above 0.05. Notebook, cell tagged for the four EMG claims under EMG claims
      at other torque commands.
""","""      earlier after MPTP with p just above 0.05. Notebook, cell tagged for the four EMG claims under EMG claims
      at other torque commands. The round-3 verifier did not agree and keeps not_reproduced. The criterion compares
      all the responses (44.2 against 25.0 ms, KS p = 5.8e-22), and at 175 to 185 units the onset is 12.5 ms
      earlier after MPTP with p = 0.057 on 5 pre-MPTP channel-sessions, a low-powered near-miss in the direction
      of the effect, not evidence of absence.
""")
rep("""      Few channel-sessions enter in one state at each size (14 post-MPTP, 5 pre-MPTP). Notebook, cell tagged
      for the four EMG claims under EMG claims at other torque commands.
""","""      Few channel-sessions enter in one state at each size (14 post-MPTP, 5 pre-MPTP). Notebook, cell tagged
      for the four EMG claims under EMG claims at other torque commands. The round-3 verifier did not agree and
      keeps partially_reproduced. The small-pulse sessions are the majority of pre-MPTP sessions (105 of 151
      have a median pulse of 30 to 60 units) and belong to the population the claims file fixes, so leaving
      them out departs from the criterion.
""")
rep("""    units in 80.0% (5, 0.19) and 95.2% (186, 0.32). The pre-MPTP shortfall comes from sessions with small pulses.
""","""    units in 80.0% (5, 0.19) and 95.2% (186, 0.32). The pre-MPTP shortfall comes from sessions with small pulses,
    which are most pre-MPTP sessions (105 of 151 have a median pulse of 30 to 60 units).
""")
open(p,'w').write(s)
E
```

```
(Bash completed with no output)
```

**Agent**

Now the round-3 verification record.

**Agent calls Bash**

```bash
cd  && sed -n 1,8p attempts/pasquereau-2013-03.yaml && grep -n "^- date\|kind: agent\|^  by:" attempts/pasquereau-2013-03.yaml | tail -4 && tail -3 attempts/pasquereau-2013-03.yaml
```

```
schema_version: 3
id: pasquereau-2013-03
datasets:
- archive: dandi
  id: '001636'
  version: 0.261124.1906
  doi: 10.48324/dandi.001636/0.261124.1906
  relation: primary
510:  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
729:- date: '2026-11-26'
730:  kind: agent
731:  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
    response: Severity changed to major. The states do share two pulse sizes, near 90 units (483 pre-MPTP and 227
      post-MPTP perturbations) and near 180 units (41 and 1540), now printed in the finding's cell; the kinematic
      and EMG claims are compared there as variants, and four outcome changes are proposed from them.
```

**Agent calls Bash**

```bash
cat >> attempts/pasquereau-2013-03.yaml <<'E'
- date: '2026-11-26'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: Round 3. Only the four changes of outcome proposed after round 2 (kinematic-latency-unchanged, emg-duration-longer,
    emg-onset-unchanged and emg-m1-weak) and the analysis behind them in the re-executed notebook (cells 21, 63
    to 68 and 73 to 82), with the claims file and the paper. Report in transcripts/pasquereau-2013/verifier-3-report.md.
  results:
  - claim: kinematic-latency-unchanged
    agrees: false
    outcome: not_reproduced
    reason: 'The criterion is applied to the session means over all perturbations: MPTP F = 709.5, p = 1.5e-102
      (cell 68). The proposal decides instead on an equal-pulse subset the claims file does not define, from cell
      65. That subset has 4 pre-MPTP sessions per direction at 175 to 185 units and 15 post-MPTP flexion sessions
      at 85 to 95 units, which is little power for an absence claim. The subset results also depend on the filter.
      With the claims file''s onset, p = 0.16 and 0.98. With the causal filter, p = 0.0027 at 85 to 95 units, which
      by the criterion is not reproduced. In round 2 the author showed the claims file''s onset is the measure that
      suffers the filter artifact. The numbers in cell 65 derive from the data as stated.'
    response: Outcome kept as not_reproduced; the proposal stays with the verifier's view added to its reason. The
      conclusion, summary and README now say the verifier did not agree.
  - claim: emg-duration-longer
    agrees: false
    outcome: partially_reproduced
    reason: 'As written, the criterion is met at partial over all channel-sessions: 22.2 against 51.5 ms, KS p = 5.2e-33,
      with both means outside tolerance (cell 78). The proposal rests on the subsets in cell 75. These have 14 post-MPTP
      channel-sessions at 85 to 95 units and 5 pre-MPTP at 175 to 185 units. A non-significant result on so few
      cannot overturn the comparison the criterion specifies. The cell 75 numbers (32.4 against 24.1 ms, p = 0.32;
      27.0 against 46.7 ms, p = 0.087) match the record.'
    response: Outcome kept as partially_reproduced; the proposal stays with the verifier's view added to its reason.
      The conclusion, summary and README now say the verifier did not agree.
  - claim: emg-onset-unchanged
    agrees: false
    outcome: not_reproduced
    reason: The criterion compares all the responses used for emg-duration-longer and gives 44.2 against 25.0 ms,
      KS p = 5.8e-22 (cell 80), so it is not reproduced. The proposal's "no difference" comes from the cell 75 subsets.
      At 175 to 185 units the onset is 12.5 ms earlier after MPTP with p = 0.057 on 5 pre-MPTP channel-sessions.
      That is a low-powered near-miss in the direction of the effect, not evidence of absence. At 85 to 95 units,
      14 post-MPTP channel-sessions enter.
    response: Outcome kept as not_reproduced; the proposal stays with the verifier's view added to its reason. The
      conclusion, summary and README now say the verifier did not agree.
  - claim: emg-m1-weak
    agrees: false
    outcome: partially_reproduced
    reason: 'Over all channel-sessions, pre-MPTP m2 exceeds m1 in 151 of 204 (74.0%) under the main rule and in 74.3%
      under the other rule, short of the 75% the criterion asks (cell 82). The proposal says the shortfall comes from
      small-pulse sessions. Those are the majority of pre-MPTP sessions: 105 of 151 have a median pulse of 30 to 60
      units (cell 21), and they belong to the population the claims file fixes. Leaving them out departs from the
      criterion. The subsets meet it on 5 pre-MPTP channel-sessions at 175 to 185 units (80.0%, which is 4 of 5)
      and 14 post-MPTP at 85 to 95 units (cell 75).'
    response: Outcome kept as partially_reproduced; the proposal stays with the verifier's view added to its reason.
      The notes now say the small-pulse sessions are most pre-MPTP sessions, and the conclusion, summary and README
      say the verifier did not agree.
E
python -c "import yaml;d=yaml.safe_load(open('attempts/pasquereau-2013-03.yaml'));print(len(d['verifications']))"
```

```
3
```

**Agent**

Now the notebook conclusions, summary and README.

**Agent calls Bash**

```bash
cd entries/pasquereau-2013 && python - <<'E'
import json
p='reproduce_pasquereau_2013.ipynb'
nb=json.load(open(p))
def rep(i,old,new):
    c=nb['cells'][i]; s=''.join(c['source'])
    assert s.count(old)==1,(i,old)
    s=s.replace(old,new)
    c['source']=s.splitlines(keepends=True)
rep(69,"""shorter latency over all perturbations goes with the larger post-MPTP pulse; a change to
reproduced is proposed in the record.""","""shorter latency over all perturbations goes with the larger post-MPTP pulse. A change to
reproduced was proposed; the round-3 verifier did not agree, since the criterion is applied over
all perturbations, the equal-pulse subsets are small, and the causal filter gives p = 0.0027 at 85
to 95 units. The outcome stays not reproduced.""")
rep(79,"""p = 0.32; 175 to 185 units, 27.0 against 46.7 ms, KS p = 0.087, 5 pre-MPTP channel-sessions). A
change to not reproduced is proposed in the record.""","""p = 0.32; 175 to 185 units, 27.0 against 46.7 ms, KS p = 0.087, 5 pre-MPTP channel-sessions). A
change to not reproduced was proposed; the round-3 verifier did not agree, since the criterion
compares all channel-sessions and a non-significant result on 14 and 5 channel-sessions cannot
overturn it. The outcome stays partially reproduced.""")
rep(81,"""over all perturbations goes with the larger post-MPTP pulse; a change to reproduced is proposed in
the record.""","""over all perturbations goes with the larger post-MPTP pulse. A change to reproduced was proposed;
the round-3 verifier did not agree, since the criterion compares all responses and p = 0.057 on 5
pre-MPTP channel-sessions, with the onset earlier after MPTP, is not evidence of no difference. The
outcome stays not reproduced.""")
rep(83,"""0.19) and 95.2% (186, 0.32). The criterion is met in both states at equal pulses, so the pre-MPTP
shortfall comes from sessions with small pulses. A change to reproduced is proposed in the record.""","""0.19) and 95.2% (186, 0.32). The criterion is met in both states at equal pulses, so the pre-MPTP
shortfall comes from sessions with small pulses, which are most pre-MPTP sessions (105 of 151 have
a median pulse of 30 to 60 units). A change to reproduced was proposed; the round-3 verifier did
not agree, since those sessions belong to the population the criterion fixes. The outcome stays
partially reproduced.""")
rep(87,"""emg-duration-longer (not reproduced); these changes are proposed in the attempt record, not
applied, and rest on few post-MPTP sessions at 85 to 95 units and few pre-MPTP sessions at 175
to 185.""","""emg-duration-longer (not reproduced). These four changes were proposed in the attempt record; the
round-3 verifier agreed with none of them, since each criterion compares all sessions or
channel-sessions and the equal-pulse subsets rest on few post-MPTP sessions at 85 to 95 units and
few pre-MPTP sessions at 175 to 185. The verified outcomes stand, and the pulse-size difference is
recorded as a finding about the data.""")
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
E
python - <<'E'
p='entries/pasquereau-2013/README.md'
s=open(p).read()
old="""longer, and m1 is much smaller than m2 in both states. The record keeps the verified outcomes and
proposes these four changes for a further round of verification. The attempt record, with the"""
new="""longer, and m1 is much smaller than m2 in both states. These four changes of outcome were proposed
for a third round of verification, and the verifier agreed with none of them: each criterion
compares all sessions or channel-sessions, and the equal-pulse subsets are small. The verified
outcomes stand, and the pulse-size difference is recorded as a finding about the data. The attempt record, with the"""
assert s.count(old)==1; open(p,'w').write(s.replace(old,new))
E
cd  git diff --stat 2>/dev/null | tail -2; date -u
```

```
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'entries/pasquereau-2013/README.md'
Thu Nov 26 20:21:34 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'E'
p='entries/pasquereau-2013/README.md'
s=open(p).read()
old="""longer, and m1 is much smaller than m2 in both states. The record keeps the verified outcomes and
proposes these four changes for a further round of verification. The attempt record, with the"""
new="""longer, and m1 is much smaller than m2 in both states. These four changes of outcome were proposed
for a third round of verification, and the verifier agreed with none of them: each criterion
compares all sessions or channel-sessions, and the equal-pulse subsets are small. The verified
outcomes stand, and the pulse-size difference is recorded as a finding about the data. The attempt
record, with the"""
assert s.count(old)==1; open(p,'w').write(s.replace(old,new))
E
grep -n "Compared there" -A10 entries/pasquereau-2013/README.md; sed -n 1,40p tools/entry.py | grep -n "all\|def " | head
```

```
36:share two pulse sizes, near 90 and near 180 units. Compared there, the latency of the evoked
37-movement and the onset of the EMG response do not change after MPTP, the EMG response is not
38-longer, and m1 is much smaller than m2 in both states. These four changes of outcome were proposed
39-for a third round of verification, and the verifier agreed with none of them: each criterion
40-compares all sessions or channel-sessions, and the equal-pulse subsets are small. The verified
41-outcomes stand, and the pulse-size difference is recorded as a finding about the data. The attempt
42-record, with the
43-reasons and the differences from the paper's method, is
44-[`attempts/pasquereau-2013-03.yaml`](../../attempts/pasquereau-2013-03.yaml).
45-
46-- `reproduce_pasquereau_2013.ipynb`: the analysis. It takes about eleven minutes, most of it
7:    python tools/entry.py all   entries/<name>   # check, then run
26:notebook through a Jupyter kernel installed in that environment, in the entry
33:so, without executing anything; --fresh executes all the same.
```

**Agent calls Bash**

```bash
python - <<'E'
p='entries/pasquereau-2013/README.md'
s=open(p).read()
old=s[s.index("longer, and m1 is much smaller than m2 in both states. These"):s.index("[`attempts/pasquereau-2013-03.yaml`]")]
new="""longer, and m1 is much smaller than m2 in both states. Applied there, the criteria would change
four outcomes. These changes were proposed for a third round of verification, and the verifier
agreed with none of them: each criterion compares all sessions or channel-sessions, and the
equal-pulse subsets are small. The verified outcomes stand, and the pulse-size difference is
recorded as a finding about the data. The attempt record, with the reasons and the differences
from the paper's method, is
"""
open(p,'w').write(s.replace(old,new))
E
sed -n 30,46p entries/pasquereau-2013/README.md; git status --short 2>/dev/null | head
```

```
of responses are blocked; their results are shown in the notebook. The torque command's pulses are
larger after MPTP than before (mean 174.7 against 58.4 units, about three times; median 181.6
against 45.7, about four times), and the evoked displacements are faster and larger after MPTP,
the reverse of the paper's; the angle's scale agrees with the task's 20 degree targets and with
the files' own velocity series, so this is in the data. Over all perturbations the evoked movement
starts earlier after MPTP with a causal filter as well as with the claims file's. The two states
share two pulse sizes, near 90 and near 180 units. Compared there, the latency of the evoked
movement and the onset of the EMG response do not change after MPTP, the EMG response is not
longer, and m1 is much smaller than m2 in both states. Applied there, the criteria would change
four outcomes. These changes were proposed for a third round of verification, and the verifier
agreed with none of them: each criterion compares all sessions or channel-sessions, and the
equal-pulse subsets are small. The verified outcomes stand, and the pulse-size difference is
recorded as a finding about the data. The attempt record, with the reasons and the differences
from the paper's method, is
[`attempts/pasquereau-2013-03.yaml`](../../attempts/pasquereau-2013-03.yaml).

- `reproduce_pasquereau_2013.ipynb`: the analysis. It takes about eleven minutes, most of it
```

**Agent calls Bash**

```bash
python - <<'E'
p='entries/pasquereau-2013/README.md'
s=open(p).read()
old="""Compared there, the latency of the evoked
movement and the onset"""
new="""Compared there, the latency of the evoked
movement (by the claims file's onset; the causal filter gives a difference under 1 ms, p =
0.0027, at 85 to 95 units) and the onset"""
assert s.count(old)==1; open(p,'w').write(s.replace(old,new))
E
date -u; timeout 3000 python tools/entry.py all entries/pasquereau-2013 2>&1 | tail -30; date -u
```

```
Thu Nov 26 20:21:47 UTC 2026
Installed kernelspec registry-pasquereau-2013 in executed/pasquereau-2013/.venv/share/jupyter/kernels/registry-pasquereau-2013
0 error(s)
pass  reproduce_pasquereau_2013.ipynb  (570 s)
Thu Nov 26 20:31:32 UTC 2026
```

**Agent calls Bash**

```bash
python -c "
import yaml;d=yaml.safe_load(open('attempts/pasquereau-2013-03.yaml'))
for o in d['outcomes']:
  if o['claim'] in ('kinematic-latency-unchanged','emg-duration-longer','emg-onset-unchanged','emg-m1-weak'): print(o['claim'],o['outcome'],o['proposed']['outcome'])
"; grep -c "1.5e-102\|5.2e-33\|5.8e-22\|74.0%" executed/pasquereau-2013/*.ipynb 2>/dev/null
```

```
kinematic-latency-unchanged not_reproduced reproduced
emg-duration-longer partially_reproduced not_reproduced
emg-onset-unchanged not_reproduced reproduced
emg-m1-weak partially_reproduced reproduced
6
```

**Agent**

No outcomes changed. The round-3 verifier disagreed with all four proposals, so all four stay open in the record with the verifier's view added to each reason.

| Claim | Outcome (kept) | Proposed (still stands) |
|---|---|---|
| kinematic-latency-unchanged | not_reproduced | reproduced |
| emg-duration-longer | partially_reproduced | not_reproduced |
| emg-onset-unchanged | not_reproduced | reproduced |
| emg-m1-weak | partially_reproduced | reproduced |

The verifier's reasons, in short:
- **Wrong comparison:** each criterion compares all sessions or channel-sessions. Restricting to equal pulses is a choice made after the all-perturbation results were known.
- **Too few sessions:** the equal-pulse subsets are small (5 pre-MPTP channel-sessions near 180 units, 14 post-MPTP near 90 units). That is too little to show that an effect is absent.
- **Filter dependence:** for the movement latency, the causal filter gives p = 0.0027 at 85 to 95 units, which by the criterion is not reproduced.
- **Small-pulse sessions:** for emg-m1-weak, these are most pre-MPTP sessions (105 of 151), and the claims file includes them.

The verifier agreed the pulse-size difference is real. It belongs in finding 3 (already rated major), not in the outcomes.

What I updated:
- **Attempt record:** the four proposal reasons now carry the verifier's view. The emg-m1-weak notes now say most pre-MPTP sessions have small pulses. Round 3 is recorded under `verifications` with one `agrees: false` result per claim, the verifier's reasons in its own words, and my response.
- **Notebook:** the four conclusion cells and the summary now say the proposals were reviewed and not accepted.
- **README:** says the same. It also notes that the "unchanged latency" at equal pulses holds only for the claims file's onset measure.

`python tools/entry.py all entries/pasquereau-2013` gave 0 errors, and the notebook passed in 570 s. Nothing is committed.

## End of run

19 turns, 11 minutes, $0.68 at API prices, result: success.
