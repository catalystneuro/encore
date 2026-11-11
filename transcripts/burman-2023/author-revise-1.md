# burman-2023 · author-revise-1 · run 42786589805

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/burman-2023/verifier-1-report.md; ls entries/burman-2023; sed -n '/## Author/,$p' docs/protocol.md | head -400
```

```
<persisted-output>
Output too large (31.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/22dd0595-7774-404f-a430-b3d0543ef0c9/tool-results/bpv2rznce.txt

Preview (first 2KB):
Tue Nov 10 09:02:59 UTC 2026
**Verifier report, round 1: Burman et al. 2023 on DANDI:000458**

The claims file has 35 claims. Ten are tested: six in `reproduce_burman_2023.ipynb` and four in `network_model.ipynb`. The other 25 are marked "Not testable": 24 patch-clamp claims, plus figs4-intrinsic-properties.

### A. Outcomes

| Claim id | My outcome | Reason |
|---|---|---|
| dataset-sessions-link | reproduced | Cell 13: all 17 gist sessions are assets of 0.230317.0039, each has every units and trials field, and each has both epochs. Cell 4: 16 subjects. |
| fig4c-sample | partially_reproduced | Cell 15, A1F1 (the Methods reading): 721 kept (inside 662 ± 66.2), but 144 excluded (outside 203 ± 20.3). Per-recording minimum is 7 against 1; 17 recordings, 16 mice; the total of 865 matches. Under the variant A1F2 every number matches the paper exactly (662/203, median 34, 1 to 93), so this is a deviation, not a failure of the data. |
| fig4d-synchrony-lower-awake | partially_reproduced | Cell 18, A1F1: awake 0.3188 is just outside 0.320–0.330; isoflurane 0.3862 is inside. Awake is lower, p = 1.45e-32. A1F2 matches exactly (0.3253 / 0.3928). |
| fig4d-entropy-higher-awake | partially_reproduced | Cell 22, A1F1: awake 1.3887 and isoflurane 1.1502 are both outside tolerance. Awake is higher, p = 3.3e-30, n = 656. A1F2 matches exactly (1.3474 / 1.1106). |
| fig4-rate-higher-awake | reproduced | Cell 24, A1F1: 14.0 Hz awake against 7.59 Hz isoflurane, paired t = 12.4, p far below 0.05. Holds under every reading; 15 of 17 recordings go the same way. |
| figs6-rate-regressed | reproduced | Cell 26, A1F1: synchrony is negative and entropy positive under R1, R2 and R3, all p < 1e-10. Same under every variant. |
| fig4f-model-hyperpolarizing-less-activity | reproduced 
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/22dd0595-7774-404f-a430-b3d0543ef0c9/tool-results/bpv2rznce.txt"
}
```

```
1	Tue Nov 10 09:02:59 UTC 2026
2	**Verifier report, round 1: Burman et al. 2023 on DANDI:000458**
3	
4	The claims file has 35 claims. Ten are tested: six in `reproduce_burman_2023.ipynb` and four in `network_model.ipynb`. The other 25 are marked "Not testable": 24 patch-clamp claims, plus figs4-intrinsic-properties.
5	
6	### A. Outcomes
7	
8	| Claim id | My outcome | Reason |
9	|---|---|---|
10	| dataset-sessions-link | reproduced | Cell 13: all 17 gist sessions are assets of 0.230317.0039, each has every units and trials field, and each has both epochs. Cell 4: 16 subjects. |
11	| fig4c-sample | partially_reproduced | Cell 15, A1F1 (the Methods reading): 721 kept (inside 662 ± 66.2), but 144 excluded (outside 203 ± 20.3). Per-recording minimum is 7 against 1; 17 recordings, 16 mice; the total of 865 matches. Under the variant A1F2 every number matches the paper exactly (662/203, median 34, 1 to 93), so this is a deviation, not a failure of the data. |
12	| fig4d-synchrony-lower-awake | partially_reproduced | Cell 18, A1F1: awake 0.3188 is just outside 0.320–0.330; isoflurane 0.3862 is inside. Awake is lower, p = 1.45e-32. A1F2 matches exactly (0.3253 / 0.3928). |
13	| fig4d-entropy-higher-awake | partially_reproduced | Cell 22, A1F1: awake 1.3887 and isoflurane 1.1502 are both outside tolerance. Awake is higher, p = 3.3e-30, n = 656. A1F2 matches exactly (1.3474 / 1.1106). |
14	| fig4-rate-higher-awake | reproduced | Cell 24, A1F1: 14.0 Hz awake against 7.59 Hz isoflurane, paired t = 12.4, p far below 0.05. Holds under every reading; 15 of 17 recordings go the same way. |
15	| figs6-rate-regressed | reproduced | Cell 26, A1F1: synchrony is negative and entropy positive under R1, R2 and R3, all p < 1e-10. Same under every variant. |
16	| fig4f-model-hyperpolarizing-less-activity | reproduced | Model cell 11: 8.785 Hz hyperpolarizing against 19.468 Hz shunting, paired p ≈ 0; lower in 20 of 20 runs. |
17	| fig4h-model-synchrony | partially_reproduced | Model cell 7: s
[... 432 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep burman; ls questions | grep burman; cat attempts/burman-2023-01.yaml | head -150; wc -l attempts/burman-2023-01.yaml
```

```
burman-2023-01.yaml
schema_version: 3
id: burman-2023-01
datasets:
- archive: dandi
  id: "000458"
  version: 0.230317.0039
  doi: 10.48324/dandi.000458/0.230317.0039
  relation: reuses
paper: doi:10.1016/j.neuron.2023.08.005
date: '2026-11-10'
entry: burman-2023
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-14
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^outcomes/,/^deviations/p' attempts/burman-2023-01.yaml | grep -n "claim:\|outcome:\|assumed" | head -80; grep -n "^[a-z_]*:" attempts/burman-2023-01.yaml; cat questions/burman-2023.yaml
```

```
Exit code 1
2:- claim: dataset-sessions-link
3:  outcome: reproduced
5:  output: claim:dataset-sessions-link
12:- claim: fig4c-sample
13:  outcome: partially_reproduced
15:  output: claim:fig4c-sample
42:- claim: fig4d-synchrony-lower-awake
43:  outcome: partially_reproduced
45:  output: claim:fig4d-synchrony-lower-awake
66:- claim: fig4d-entropy-higher-awake
67:  outcome: partially_reproduced
69:  output: claim:fig4d-entropy-higher-awake
90:- claim: fig4-rate-higher-awake
91:  outcome: reproduced
93:  output: claim:fig4-rate-higher-awake
105:- claim: figs6-rate-regressed
106:  outcome: reproduced
108:  output: claim:figs6-rate-regressed
124:- claim: fig4f-model-hyperpolarizing-less-activity
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 124,200p attempts/burman-2023-01.yaml; sed -n 380,404p attempts/burman-2023-01.yaml; ls questions | head; ls papers/claims 2>/dev/null | grep burman; ls transcripts/burman-2023
```

```
notes: Under A1F1 the evoked spike-count rate is 14.00 +- 0.66 Hz awake against 7.59 +- 0.47 Hz under
    isoflurane over 721 units, paired t = 12.36 (p printed as 0, far below 0.05); higher awake in 539
    of 721 units and 15 of 17 recordings. Every reading gives the same direction (gist rate 45.05 against
    24.29). The paper reports no value or test for this in the text read; the test is the claims file's.
  deviations:
  - Trials of all stimulus currents and depths of a session are pooled and times are taken from stop_time,
    as the claims file (N3) gives from the gist; the Methods say only "following an electrical stimulus".
    Timing from start_time, the pulse onset 0.4 ms earlier, is shown as a variant and keeps the direction.
  - The Methods' waveform cut (>= 0.4 ms) and the gist's (> 0.4 ms) select the same units, as no unit
    has a duration of exactly 0.4 ms; readings A1 and A2 also select the same 865 units, as the SSp sessions
    hold only SSp-ll and SSp-tr units.
- claim: figs6-rate-regressed
  outcome: reproduced
  notebook: reproduce_burman_2023.ipynb
  output: claim:figs6-rate-regressed
  notes: Under A1F1, with the evoked rate regressed out, the awake difference keeps its sign with p below
    1e-10 in all six tests. Synchrony R1 -0.0593 (p = 3.3e-26), R2 -0.0619 (p = 1.5e-13), R3 -0.0625 (p
    = 2.8e-24); entropy R1 0.171 (p = 7.1e-17), R2 0.179 (p = 4.2e-11), R3 0.210 (p = 1.1e-20). Every
    other reading gives the same. By recording (R2), the coefficient has the expected sign in 15 of 17
    for each measure. The regression of Figure S6 is in a legend not read; as all three readings the criterion
[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
git log --oneline --all -- questions/burman-2023.yaml | head; cat transcripts/burman-2023/answer-report.md | head -60; cat transcripts/burman-2023/author-answers-report.md | head -40; cat questions/README.md | head -60
```

```
I had no questions to answer, so I changed nothing.

`questions/burman-2023.yaml` does not exist on this branch (`attempt/burman-2023`), and no commit in the repository's history has ever created it. The author's report (`transcripts/burman-2023/author-report.md`, section 2) says the same: "Questions to a reader: none." It adds that the claims file does not misread the paper.

The git history does contain a `questions/000458.yaml`, which shares this paper's dataset ID. It belongs to a different paper on the same dataset: it was renamed to `questions/claar-2023.yaml`, on the `attempt/windolf-2025` branch. It is not this attempt's, so I left it alone.

I made no edits to `claims/burman-2023.yaml` and did not create a questions file. With nothing amended, there were no new quotes to check with `tools/claims_check.py`, so I did not run it.
There were no questions to answer, so I changed nothing and no claim was re-run.

**Questions.** `questions/burman-2023.yaml` doesn't exist, and no commit in the repository's history ever created it. My first author run asked no questions (its report says "Questions to a reader: none"). The reader's answer run found nothing to answer and left `claims/burman-2023.yaml` as it was. Nothing in `claims/`, `attempts/`, `entries/` or `questions/` has changed since the author commit (00af702325). With no amended claim, there were no notes to add and the notebooks, conclusions and attempt record stay as they were.

**Outcomes per claim** (unchanged, so each earlier outcome equals the current one):

| Claim | Earlier | Now |
|---|---|---|
| Dataset holds the 17 files and their fields | reproduced | reproduced |
| Unit counts: 721 kept, 144 excluded, against 662 and 203 | partially reproduced | partially reproduced |
| Synchrony lower awake, 0.3188 against 0.3862 | partially reproduced | partially reproduced |
| Entropy higher awake, 1.389 against 1.150 nats | partially reproduced | partially reproduced |
| Evoked rate higher awake, 14.0 against
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims | grep burman; grep -n "N[0-9]\b\|^  N\|id: fig4h\|id: figs4\|id: fig4c" -A0 claims/burman-2023.yaml | head -40
```

```
burman-2023.yaml
52:# the analysis gist (1). Cited in the criteria as N1 to N8.
53:# N1 Sessions. The 17 sessions listed in the gist (see dataset-sessions-link).
54:# N2 Units. Regular spiking units, waveform duration of 0.4 ms or more (Methods; the gist uses
--
60:# N3 Trials. Electrical stimulus trials with is_valid true, behavioral_epoch "awake" for awake
--
64:# N4 Window. Spikes from 2 to 12 ms after the stimulus (Methods and gist), in 1 ms bins (10
--
67:# N5 Entropy. Per unit and condition, the histogram of its spikes over all trials, normalized
--
70:# N6 Synchrony. Per trial, the histogram of the spikes of all the session's selected units (the
--
75:#    population is the units selected by N2, before the exclusion of N7. The population of kept
--
77:# N7 Evoked firing rate and exclusion. Units with an evoked rate below 0.1 Hz or above 200 Hz in
--
88:# N8 Statistics. Values are mean +- SEM over neurons and awake against anesthetized is a paired
--
410:- id: figs4-intrinsic-properties
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 40,100p claims/burman-2023.yaml; sed -n 405,440p claims/burman-2023.yaml; grep -n "fig4h-model" -A30 claims/burman-2023.yaml | sed -n 1,80p
```

```
# al. (2023), DANDI:000458 (key resources table; claims/claar-2023.yaml describes it): head-fixed
# mice with up to three Neuropixels probes and a bipolar stimulating electrode in layer 2/3 or 5/6
# of SSp or MOs, single electrical pulses delivered awake and under isoflurane. The paper uses 17
# recordings in 16 mice (sub-569073 has two sessions); units are regular spiking units of the
# stimulated area, 662 after exclusion. Measured variables used: unit spike times, waveform
# duration and location; trial times, stimulus type, behavioral epoch, validity and stimulation
# target region.
# Network models (Figures 4E to 4H, S7) are generated by the paper's simulation code (data
# elsewhere, where names the code).
#
# Method for the claims on DANDI:000458, fixed from the Methods ("Pre-processing of Neuropixels
# dataset", "Characterization of stimulus-evoked spiking responses", "Statistical analyses") and
# the analysis gist (1). Cited in the criteria as N1 to N8.
# N1 Sessions. The 17 sessions listed in the gist (see dataset-sessions-link).
# N2 Units. Regular spiking units, waveform duration of 0.4 ms or more (Methods; the gist uses
#    strictly more than 0.4, which is shown as a variant). Area, open between two readings:
#    (A1) the Methods, units whose location annotation is "SSp-ll" or "SSp-tr", or "MOs",
#    whichever area was electrically stimulated in the session; (A2) the gist, units whose
#    location's first three characters are among the session's estim_target_region values of
#    its electrical trials.
[... 157 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/burman-2023; cat README.md entry.yaml requirements.in; wc -l npx.py network.py; python - <<'EOF'
import json
for nb in ['reproduce_burman_2023.ipynb','network_model.ipynb']:
    d=json.load(open(nb))
    print('=====',nb)
    for i,c in enumerate(d['cells']):
        print(f'--- [{i}] {c["cell_type"]} {c.get("metadata",{}).get("tags","")}')
        print(''.join(c['source']))
EOF
```

```
<persisted-output>
Output too large (42.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/22dd0595-7774-404f-a430-b3d0543ef0c9/tool-results/bfdl0257y.txt

Preview (first 2KB):
# Burman, Brodersen, Raimondo, Sen & Akerman (2023) on dandiset 000458

Tests the findings of [Burman et al. (2023)](https://doi.org/10.1016/j.neuron.2023.08.005) that can
be tested on [DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), the Allen
Institute Neuropixels recordings with cortical electrical stimulation, awake and under isoflurane,
that the paper reuses (Figure 4A to 4D, Figure S6), and runs the paper's network model (Figure 4E
to 4H, Figure S7). The paper's gramicidin patch-clamp recordings (Figures 1 to 3) are not in the
dandiset nor deposited anywhere.

| Claim | Outcome |
|---|---|
| The 17 sessions the paper's code reads are in the dandiset with the fields it uses | Reproduced |
| 662 neurons kept and 203 excluded, from 17 recordings in 16 mice | Partially reproduced |
| Synchrony lower awake (0.325 against 0.393) | Partially reproduced |
| Entropy higher awake (1.347 against 1.111 nats) | Partially reproduced |
| Evoked firing rate higher awake | Reproduced |
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/22dd0595-7774-404f-a430-b3d0543ef0c9/tool-results/bfdl0257y.txt"
}
```

```
1	# Burman, Brodersen, Raimondo, Sen & Akerman (2023) on dandiset 000458
2	
3	Tests the findings of [Burman et al. (2023)](https://doi.org/10.1016/j.neuron.2023.08.005) that can
4	be tested on [DANDI:000458](https://dandiarchive.org/dandiset/000458/0.230317.0039), the Allen
5	Institute Neuropixels recordings with cortical electrical stimulation, awake and under isoflurane,
6	that the paper reuses (Figure 4A to 4D, Figure S6), and runs the paper's network model (Figure 4E
7	to 4H, Figure S7). The paper's gramicidin patch-clamp recordings (Figures 1 to 3) are not in the
8	dandiset nor deposited anywhere.
9	
10	| Claim | Outcome |
11	|---|---|
12	| The 17 sessions the paper's code reads are in the dandiset with the fields it uses | Reproduced |
13	| 662 neurons kept and 203 excluded, from 17 recordings in 16 mice | Partially reproduced |
14	| Synchrony lower awake (0.325 against 0.393) | Partially reproduced |
15	| Entropy higher awake (1.347 against 1.111 nats) | Partially reproduced |
16	| Evoked firing rate higher awake | Reproduced |
17	| Synchrony and entropy differences remain with firing rate regressed out | Reproduced |
18	| Model: hyperpolarizing E_GABA gives less activity | Reproduced |
19	| Model: synchrony lower with shunting E_GABA (0.784 against 0.881) | Partially reproduced |
20	| Model: entropy higher with shunting E_GABA (0.451 against 0.197 nats) | Partially reproduced |
[... 718 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -o g1.py https://gist.githubusercontent.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf/raw/43a13d89441b7f56e835e84fa5811d9567917daf/burman_et_al_2023_neuropixel_data_analysis.py; curl -sL -o g2.py https://gist.githubusercontent.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f/raw/f6a05661c10051560aa381e334099efd8521617b/burman_et_al_2023_neuronal_network_simulation.py; wc -l g1.py g2.py; head -5 g1.py; grep -rn "gist" entries/burman-2023/npx.py | head
```

Result: the fetched text is not kept.

**Agent**

Both gists are fetchable. Let me read them.

**Agent calls Bash**

```bash
cat $TMPDIR/g1.py
```

```
#!/usr/bin/env python
# -*- coding: utf-8 -*

""" Extract data from Claar et al. (2023) & compute for each unit its
- evoked firing rate,
- peri-stimulus histogram entropy, and
- synchrony.

The dataset is available at:

https://dandiarchive.org/dandiset/000458/0.230317.0039

Copyright (C) 2023 by Paul Brodersen.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version. This program is distributed in the
hope that it will be useful, but WITHOUT ANY WARRANTY; without even
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
[... 152 more lines not kept]
```

**Agent calls Bash**

```bash
cat $TMPDIR/g2.py; sed -n 1,80p entries/burman-2023/network.py
```

```
#!/usr/bin/env python
# -*- coding: utf-8 -*

"""Simulate a LIF neuronal network with variable EGABA and structured inputs.

Copyright (C) 2023 by Paul Brodersen.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at
your option) any later version. This program is distributed in the
hope that it will be useful, but WITHOUT ANY WARRANTY; without even
the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE.  See the GNU General Public License for more details. You
should have received a copy of the GNU General Public License along
with this program. If not, see <https://www.gnu.org/licenses/.

"""

import time
[... 510 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 80,246p entries/burman-2023/network.py
```

```
stimulus_set_duration = total_stimuli * epoch_duration

    stimulus_duration = 1
    stimulus_magnitude = 500
    total_subepochs = int(epoch_duration / stimulus_duration)
    base_stimuli = np.zeros((total_stimuli * total_subepochs, total_neurons))
    base_stimuli[::total_subepochs] = stimulus_magnitude * np.random.lognormal(
        size=(total_stimuli, total_neurons))
    if periodic:
        # one stimulus set, read periodically (see the module docstring)
        I_stimulus_set = b2.TimedArray(-base_stimuli * b2.pA, dt=stimulus_duration * b2.ms)
        set_duration = stimulus_set_duration * b2.ms
    else:
        # the gist's array for the whole run; t % set_duration then leaves t unchanged
        stimuli_full = np.vstack([base_stimuli] * (total_repeats + 1))
        I_stimulus_set = b2.TimedArray(-stimuli_full * b2.pA, dt=stimulus_duration * b2.ms)
        set_duration = 10 * total_time * b2.ms

    base_stimuli_labels = np.arange(total_stimuli)
    stimuli_labels = np.hstack([base_stimuli_labels] * (total_repeats + 1))
[... 147 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,332p entries/burman-2023/npx.py
```

```
"""Loading DANDI:000458 (Claar et al. 2023) and the per-unit measures of Burman et al. (2023),
Figure 4A to 4D and Figure S6.

Every method choice is the claims file's (claims/burman-2023.yaml, opening comment N1 to N8),
which takes it from the paper's Methods ("Pre-processing of Neuropixels dataset",
"Characterization of stimulus-evoked spiking responses") and the paper's analysis gist,
gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf at revision
43a13d89441b7f56e835e84fa5811d9567917daf (burman_et_al_2023_neuropixel_data_analysis.py):

- SESSIONS: the 17 recordings the gist lists (N1).
- Units (N2): waveform_duration >= 0.4 ms (Methods; the gist's > 0.4 is a variant). Area reading
  A1, the Methods: location "SSp-ll" or "SSp-tr" when SSp was stimulated, "MOs" when MOs was;
  reading A2, the gist: location[:3] among the session's estim_target_region values of its
  electrical trials.
- Trials (N3): stimulus_type "electrical", is_valid true, behavioral_epoch "awake" or
  "isoflurane", all currents and depths pooled, times from stop_time (gist).
- Window (N4): spikes 2 to 12 ms after the stimulus, 1 ms bins.
- Entropy (N5), synchrony (N6) and the evoked rate (N7, readings F1 and F2) as the gist computes
  them; see each function.

[... 313 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper; grep -il "Simulating measurements" -r paper | head; grep -n -i "S4\b\|Figure S4\|multi-compartment\|NEURON" -r paper/*.md 2>/dev/null | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; grep -n -i "Figure S4\|multi-compartment\|NEURON simulation\|Simulating measurements\|github" 10.1016-j.neuron.2023.08.005.txt | head -30
```

```
<persisted-output>
Output too large (68.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/22dd0595-7774-404f-a430-b3d0543ef0c9/tool-results/bq5gvhi84.txt

Preview (first 2KB):
7:pmc Neuron Neuron Neuron 0896-6273 1097-4199 Cell Press 11913778 S0896-6273(23)00586-X 10.1016/j.neuron.2023.08.005 Report Active cortical networks promote shunting fast synaptic inhibition in vivo Burman Richard J. 1 2 4 Brodersen Paul J.N. 1 4 Raimondo Joseph V. 3 Sen Arjune 2 Akerman Colin J. [removed: an e-mail address] 1 5 ∗ 1 Department of Pharmacology, University of Oxford, Oxford, OX1 3QT, UK 2 Oxford Epilepsy Research Group, Nuffield Department of Clinical Neurosciences, University of Oxford, Oxford, OX3 9DU, UK 3 Division of Cell Biology, Department of Human Biology, Neuroscience Institute and Institute of Infectious Diseases and Molecular Medicine, University of Cape Town, Cape Town, 7935, South Africa ∗ Corresponding author [removed: an e-mail address] 4 These authors contributed equally 5 Lead contact 15 11 2023 15 11 2023 111 22 3531 3540.e6 1 3 2023 3 7 2023 4 8 2023 © 2023 The Author(s) 2023 https://creativecommons.org/licenses/by/4.0/ This is an open access article under the CC BY license (http://creativecommons.org/licenses/by/4.0/). Summary Fast synaptic inhibition determines neuronal response properties in the mammalian brain and is mediated by chloride-permeable ionotropic GABA-A receptors (GABA A Rs). Despite their fundamental role, it is still not known how GABA A Rs signal in the intact brain. Here, we use in vivo gramicidin recordings to investigate synaptic GABA A R signaling in mouse cortical pyramidal neurons under conditions that preserve native transmembrane chloride gradients. In anesthetized cortex, synaptic GABA A Rs exert classic hyperpolarizing effects. In contrast, GABA A R-mediated synaptic signaling in awake cortex is found to be predominantly shunting. This is due to more depolarized GABA A R equilibrium potential
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -o -i ".\{300\}Simulating measurements of synaptic.\{1500\}" paper/*.txt | head -3; grep -o -i ".\{400\}Figure S4.\{300\}" paper/*.txt | head -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -i "Activation of GABA A R synap.\{1500\}" paper/*.txt | head -2; sed -n 176,185p attempts/burman-2023-01.yaml; grep -n "methods_unavailable" attempts/burman-2023-01.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "claim: figs4-intrinsic" -A8 attempts/burman-2023-01.yaml; sed -n 340,383p attempts/burman-2023-01.yaml; ls executed/burman-2023/ 2>/dev/null; git log --oneline -3 -- executed | head
```

```
206:- claim: figs4-intrinsic-properties
207-  outcome: blocked
208-  blocked_by: other
209-  notes: 'The claim rests on the paper''s NEURON model of an L2/3 pyramidal neuron and a Matlab analysis
210-    of its simulated ramps (github.com/richardjburman/burman-et-al-2022---Awake-EGABAAR at commit a404c3e:
211-    hoc files and NEURON_Egaba_Analysis.m). The measure and test of Figure S4 are in the supplement, which
212-    was not supplied with the text, and the claims file gives no criterion for them, so there is nothing
213-    fixed to judge; the analysis code is Matlab, which cannot be run in a locked Python environment here
214-    (a transcription was not attempted). Neither part uses the dandiset.'
    for gramicidin, Akerman, Burman and EGABA found no dandiset.
- claim: fig3d-nbqx-fluctuation
  outcome: blocked
  blocked_by: data_missing
  notes: Needs the paper's in vivo gramicidin perforated patch recordings of L2/3 pyramidal neurons in
    V1. DANDI:000458 holds only the Allen Institute Neuropixels and EEG recordings, and the paper deposits
    the patch data nowhere ("available on request to the lead contact"). A search of the DANDI archive
    for gramicidin, Akerman, Burman and EGABA found no dandiset.
- claim: fig3e-nbqx-polarity
  outcome: blocked
  blocked_by: data_missing
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -l "^verifications:" attempts/*.yaml | head -3; f=$(grep -l "^verifications:" attempts/*.yaml | head -1); sed -n '/^verifications:/,$p' $f | head -60; ls schemas 2>/dev/null
```

```
attempts/amjad-2025-01.yaml
attempts/armstrong-2026-01.yaml
attempts/ashworth-2025-01.yaml
verifications:
- date: '2026-10-15'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
    module and the claims file, with the paper's full text (PMC12183687). The verifier read the
    archive's file list and metadata through the DANDI API and tested the helpers on synthetic inputs
    (beta_power, burst_onsets, window_mean, codes_per_trial, rereference, fscv_window_mean, best_lag,
    reward_blocks). It had no attempt record and took the claims from the claims file.
  results:
  - claim: insertion-yield
    agrees: true
    outcome: blocked
    reason: The archive has 3 assets with sites c8dg, c3bs, c3a and cl3, and nothing about implanted
      or failed sensors. Figure 3 names 4 functional Monkey T sites against the paper's "3/14", so
      "sensor" may mean probe. Neither count can be checked; an implant log of sensors per monkey is
      not in the archive.
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -c 2500 transcripts/burman-2023/verifier-1.md; grep -n "verifications" -A40 schemas/attempt.schema.json | grep -n '"[a-z_]*"' | head -30
```

````
# burman-2023 · verifier-1 · run 42780709977

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 360
drwxr-xr-x 6 runner runner    4096 Nov 10 08:51 .
drwxr-xr-x 7 runner runner    4096 Nov 10 08:51 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 08:11 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 10 08:11 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 10 08:51 .claude
-rw-r--r-- 1 runner runner       0 Nov 10 08:51 .env
-rw-r--r-- 1 runner runner       0 Nov 10 08:51 .env.development
[... 62 more lines not kept]
````

**Agent calls Bash**

```bash
cd  sed -n 412,470p schemas/attempt.schema.json; grep -rn "blocked_by" attempts/*.yaml | grep -B0 "^.*:    blocked_by" | head -3
```

```
"results": {
            "type": "array",
            "items": {
              "type": "object",
              "additionalProperties": false,
              "required": [
                "claim",
                "agrees"
              ],
              "properties": {
                "claim": {
                  "type": "string"
                },
                "agrees": {
                  "type": "boolean"
                },
                "reason": {
                  "description": "The verifier's reason, in its own words.",
                  "type": "string"
                },
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/burman-2023; ls ~/.cache 2>/dev/null | head; python -c "import brian2, h5py, remfile; print(brian2.__version__)"; which python
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import brian2, h5py, remfile; print(brian2.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'brian2'
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p tools/entry.py | head -80; ls -d .venv* $TMPDIR/* 2>/dev/null | head
```

```
"""Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
tied to the data:

- every notebook in the directory is listed in entry.yaml, and exists;
- notebooks are committed without outputs;
- the lock file is present and newer requirements are not left unlocked;
- each notebook, or a helper it imports, names the dataset the entry uses (its identifier and version);
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.13 dev && uv pip install -q -p dev/bin/python -r entries/burman-2023/requirements.lock.txt 2>&1 | tail -3; dev/bin/python -c "import brian2; print(brian2.__version__)"
```

```
2.11.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/w && cd $TMPDIR/w && cat > gistcheck.py <<'EOF'
import sys, types, time
sys.path.insert(0, "entries/burman-2023")
import numpy as np, pandas as pd, requests, npx
GIST = ("https://gist.githubusercontent.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf/raw/"
        "43a13d89441b7f56e835e84fa5811d9567917daf/burman_et_al_2023_neuropixel_data_analysis.py")
src = requests.get(GIST, timeout=60).text
assets = npx.assets()
assets["session"] = assets.path.str.split("/").str[1].str.replace("_behavior+ecephys.nwb", "", regex=False)
names = sys.argv[1:] or npx.SESSIONS[:1]
t=time.time()
S = {k: npx.read_session(assets.set_index("session").loc[k, "asset_id"]) for k in names}
print("load", time.time()-t)

class FakeTable:
    def __init__(self, df): self.df = df
    def to_dataframe(self): return self.df.copy()
class FakeNWB:
    def __init__(self, s):
        tr = s["trials"]
        stops = tr.stop_time.to_numpy()
        u = s["units"][["location", "waveform_duration"]].copy()
        # spike times in s rebuilt from the kept peri-stimulus spikes (trial, ms after stop_time)
        u["spike_times"] = [np.sort(stops[a[:, 0].astype(int)] + a[:, 1] / 1000.0) if len(a) else np.array([])
                            for a in (s["spikes"][r] for r in range(len(u)))]
        u.index = pd.Index(np.arange(len(u)), name="id")
        self.units = FakeTable(u)
        self.intervals = {"trials": FakeTable(tr)}
def fake_io(path, mode):
    name = path.name.replace("_behavior+ecephys.nwb", "")
    return types.SimpleNamespace(read=lambda: FakeNWB(S[name]))
out = {}
def capture(self, path, index=False):
    out[path.name.replace("_behavior+ecephys.csv", "")] = self.copy()
sys.modules["pynwb"] = types.SimpleNamespace(NWBHDF5IO=fake_io)
code = src.replace('"sub-', '"sub-')  # unchanged
g = {"__name__": "__main__"}
orig = pd.DataFrame.to_csv
pd.DataFrame.to_csv = capture
import contextlib, io
t=time.time()
try:
    # the gist's datasets list names all 17; run it only on the loaded ones
    g["__builtins__"] = __builtins__
    with contextlib.redirect_stdout(io.StringIO()):
        exec(compile(src, "gist", "exec"), g)
except KeyError as e:
    print("stopped at", e)
finally:
    pd.DataFrame.to_csv = orig
print("gist", time.time()-t, list(out))
for k, G in out.items():
    T = npx.unit_table(S[k], "A2", "gt")
    m = G.merge(T, left_on="id", right_on="row")
    print(k, len(G), len(T), len(m))
    for c, sfx in (("awake", "_aw"), ("isoflurane", "_an")):
        for gcol, ncol in ((f"Firing rate [Hz] ({c})", "rate_F2"), (f"Entropy [nats] ({c})", "entropy"), (f"Synchrony ({c})", "synchrony")):
            a, b = m[gcol].to_numpy(float), m[ncol + sfx].to_numpy(float)
            same = np.isclose(a, b, rtol=1e-9, atol=1e-12) | (np.isnan(a) & np.isnan(b))
            print("  ", gcol, "agree", same.sum(), "/", len(m), "max abs diff", np.nanmax(np.abs(a-b)) if len(m) else None)
EOF
$TMPDIR/dev/bin/python gistcheck.py
```

```
load 3.8895859718322754
stopped at 'sub-551397_ses-20210211'
gist 1.106334924697876 ['sub-546655_ses-20201023']
sub-546655_ses-20201023 18 18 18
   Firing rate [Hz] (awake) agree 18 / 18 max abs diff 2.3106849766918458e-10
   Entropy [nats] (awake) agree 18 / 18 max abs diff 2.220446049250313e-16
   Synchrony (awake) agree 18 / 18 max abs diff 0.0
   Firing rate [Hz] (isoflurane) agree 18 / 18 max abs diff 6.188400902829017e-10
   Entropy [nats] (isoflurane) agree 18 / 18 max abs diff 0.0
   Synchrony (isoflurane) agree 18 / 18 max abs diff 0.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/burman-2023 && python - <<'EOF'
p='npx.py'; s=open(p).read()
s=s.replace('''KEEP = (0.0, 20.0)  # ms after stop_time kept on loading, wider than every window used
''','''KEEP = (0.0, 20.0)  # ms after stop_time kept on loading, wider than every window used
SHIFTS = (-1500.0, 1500.0)  # ms: the clock check's windows away from the pulses (standard choice;
#                            inter-pulse intervals are 3.5 to 4.5 s, so these hold no evoked spikes)
''')
s=s.replace('''    trial's stop_time) for spikes within KEEP of an electrical trial), `n_spikes` (each unit's
    total spike count) and file metadata.
    """''','''    trial's stop_time) for spikes within KEEP of an electrical trial), `n_spikes` (each unit's
    total spike count), `shifted` (for each lag in SHIFTS, arrays (unit row, index into trials)
    of the spikes 2 to 12 ms after stop_time + lag, for the clock check) and file metadata.
    """''')
s=s.replace('''    kept_unit, kept_trial, kept_time = [], [], []
    sorted_ok = True''','''    kept_unit, kept_trial, kept_time = [], [], []
    shift_parts = {lag: ([], []) for lag in SHIFTS}
    sorted_ok = True''')
s=s.replace('''        kept_time.append(rel[m])
''','''        kept_time.append(rel[m])
        for lag in SHIFTS:
            origin = stops * 1000.0 + lag
            j2 = np.searchsorted(origin, t, side="right") - 1
            rel2 = t - origin[np.clip(j2, 0, None)]
            m2 = (j2 >= 0) & (rel2 >= INTERVAL[0]) & (rel2 < INTERVAL[1])
            shift_parts[lag][0].append(unit_of[a:a + chunk][m2])
            shift_parts[lag][1].append(el[j2[m2]])
''')
s=s.replace('''    for r in range(len(units)):
        m = ku == r
        spikes[r] = np.c_[kt[m], kx[m]]
''','''    for r in range(len(units)):
        m = ku == r
        spikes[r] = np.c_[kt[m], kx[m]]
    shifted = {lag: (np.concatenate(us) if us else np.array([], int),
                     np.concatenate(ts) if ts else np.array([], int))
               for lag, (us, ts) in shift_parts.items()}
''')
s=s.replace('''    return dict(trials=trials, units=units, spikes=spikes, meta=meta)


# ----''','''    return dict(trials=trials, units=units, spikes=spikes, shifted=shifted, meta=meta)


# ----''')
open(p,'w').write(s)
EOF
grep -n "shifted" npx.py
```

```
97:    total spike count), `shifted` (for each lag in SHIFTS, arrays (unit row, index into trials)
151:    shifted = {lag: (np.concatenate(us) if us else np.array([], int),
172:    return dict(trials=trials, units=units, spikes=spikes, shifted=shifted, meta=meta)
```

**Agent calls Bash**

```bash
cat >> npx.py <<'EOF'


# ---------------------------------------------------------------- the paper's own code

GIST_URL = ("https://gist.githubusercontent.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf/raw/"
            "43a13d89441b7f56e835e84fa5811d9567917daf/burman_et_al_2023_neuropixel_data_analysis.py")


def run_gist(sessions):
    """Run the paper's analysis gist, unmodified, on sessions loaded by read_session, and return
    the table it writes per session (the CSV it would save), keyed by session name.

    The gist reads each file with pynwb and writes a CSV. Here pynwb's NWBHDF5IO is replaced by
    an object that returns the loaded trials table and a units table (location,
    waveform_duration, spike_times in s, indexed by id), and DataFrame.to_csv is captured. The
    spike times given are the spikes read_session keeps (0 to 20 ms after an electrical
    stop_time, rebuilt as stop_time + latency); the gist uses only spikes 2 to 12 ms after
    valid electrical trials, so its results are the same as with the full trains. The gist's
    list names all 17 sessions; `sessions` must hold them all.
    """
    import contextlib
    import io
    import sys
    import types

    src = requests.get(GIST_URL, timeout=60).text

    class _Table:
        def __init__(self, df):
            self.df = df

        def to_dataframe(self):
            return self.df.copy()

    def _nwb(s):
        stops = s["trials"].stop_time.to_numpy()
        u = s["units"][["location", "waveform_duration"]].copy()
        u["spike_times"] = [np.sort(stops[a[:, 0].astype(int)] + a[:, 1] / 1000.0) if len(a)
                            else np.array([]) for a in (s["spikes"][r] for r in range(len(u)))]
        u.index = pd.Index(np.arange(len(u)), name="id")
        return types.SimpleNamespace(units=_Table(u), intervals={"trials": _Table(s["trials"])})

    def _io(path, mode):
        name = path.name.replace("_behavior+ecephys.nwb", "")
        return types.SimpleNamespace(read=lambda: _nwb(sessions[name]))

    out = {}

    def _capture(self, path, index=False):
        out[path.name.replace("_behavior+ecephys.csv", "")] = self.copy()

    saved_mod, saved_csv = sys.modules.get("pynwb"), pd.DataFrame.to_csv
    sys.modules["pynwb"] = types.SimpleNamespace(NWBHDF5IO=_io)
    pd.DataFrame.to_csv = _capture
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(src, "burman_et_al_2023_neuropixel_data_analysis.py", "exec"),
                 {"__name__": "__main__"})
    finally:
        pd.DataFrame.to_csv = saved_csv
        if saved_mod is None:
            sys.modules.pop("pynwb", None)
        else:
            sys.modules["pynwb"] = saved_mod
    return out
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > t2.py <<'EOF'
import sys, time
sys.path.insert(0, "entries/burman-2023")
import numpy as np, pandas as pd, npx
assets = npx.assets()
assets["session"] = assets.path.str.split("/").str[1].str.replace("_behavior+ecephys.nwb", "", regex=False)
t=time.time()
S = {k: npx.read_session(assets.set_index("session").loc[k, "asset_id"]) for k in npx.SESSIONS}
print("load", time.time()-t)
rows = []
for k, s in S.items():
    sel = npx.select_units(s, "A1", "ge")
    for c in npx.CONDITIONS:
        tr = npx.condition_trials(s["trials"], c)
        u, t_, x = npx.peristimulus(s, sel, tr)
        row = dict(session=k, condition=c, trials=len(tr), evoked=len(x) / len(tr))
        for lag, (uu, tt) in s["shifted"].items():
            row[f"lag {lag/1000:+.1f} s"] = (np.isin(uu, sel) & np.isin(tt, tr)).sum() / len(tr)
        rows.append(row)
cl = pd.DataFrame(rows)
cl["ratio_min"] = cl.evoked / cl[["lag -1.5 s", "lag +1.5 s"]].max(axis=1)
print(cl.round(2).to_string())
t=time.time(); G = npx.run_gist(S); print("gist", time.time()-t, len(G))
EOF
$TMPDIR/dev/bin/python t2.py
```

```
load 121.66068935394287
                    session   condition  trials  evoked  lag -1.5 s  lag +1.5 s  ratio_min
0   sub-546655_ses-20201023       awake     359    1.74        0.40        0.35       4.38
1   sub-546655_ses-20201023  isoflurane     301    0.90        0.05        0.01      16.94
2   sub-551397_ses-20210211       awake     360   12.17        3.70        3.53       3.29
3   sub-551397_ses-20210211  isoflurane     360    6.03        1.40        1.46       4.13
4   sub-551399_ses-20210128       awake     358   14.84        2.22        2.10       6.68
5   sub-551399_ses-20210128  isoflurane     359    5.41        0.09        0.18      29.41
6   sub-569062_ses-20210218       awake     360    8.17        4.45        4.24       1.84
7   sub-569062_ses-20210218  isoflurane     360    2.90        1.01        1.33       2.18
8   sub-569064_ses-20210408       awake     360    2.79        0.51        0.38       5.52
9   sub-569064_ses-20210408  isoflurane     357    0.72        0.11        0.04       6.40
10  sub-569068_ses-20210304       awake     359    7.36        1.67        1.87       3.93
11  sub-569068_ses-20210304  isoflurane     357    2.24        0.79        0.74       2.83
12  sub-569069_ses-20210312       awake     357    1.55        1.53        1.36       1.02
13  sub-569069_ses-20210312  isoflurane     359    0.97        0.39        0.48       2.01
14  sub-569072_ses-20210422       awake     359    9.27        3.84        3.42       2.41
15  sub-569072_ses-20210422  isoflurane     360    6.22        0.82        0.88       7.10
16  sub-569073_ses-20210415       awake     336    3.93        0.87        0.69       4.51
17  sub-569073_ses-20210415  isoflurane     360    1.69        0.36        0.39       4.39
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > clock_cell.py <<'EOF'
# Population spike count per trial 2 to 12 ms after stop_time, against the same window placed
# 1.5 s before and after each pulse (npx.SHIFTS; inter-pulse intervals are 3.5 to 4.5 s), for
# the selected units (reading A1) of all 17 files. read_session counts the shifted windows from
# the full spike trains as it streams them. Per trial, the evoked count is compared with the
# mean of the two shifted counts by a Wilcoxon signed-rank test.
clock = []
for k, s in S.items():
    rows_ = npx.select_units(s, "A1", "ge")
    for c in npx.CONDITIONS:
        tr = npx.condition_trials(s["trials"], c)
        u, pos, x = npx.peristimulus(s, rows_, tr)
        ev = np.bincount(pos, minlength=len(tr))
        row = dict(session=k, condition=c, trials=len(tr), units=len(rows_), evoked=ev.mean())
        sh = []
        for lag, (uu, tt) in s["shifted"].items():
            m = np.isin(uu, rows_) & np.isin(tt, tr)
            where = {t: i for i, t in enumerate(tr)}
            sh.append(np.bincount([where[t] for t in tt[m]], minlength=len(tr)))
            row[f"shift {lag / 1000:+.1f} s"] = sh[-1].mean()
        base = (sh[0] + sh[1]) / 2
        row["evoked / shifted"] = ev.mean() / base.mean() if base.mean() else np.inf
        row["wilcoxon p"] = stats.wilcoxon(ev, base).pvalue
        clock.append(row)
clock = pd.DataFrame(clock)
with pd.option_context("display.float_format", "{:.3g}".format):
    print(clock.to_string())
print("\nconditions with evoked above shifted at p < 0.001: %d of %d"
      % ((clock["wilcoxon p"] < 0.001).sum(), len(clock)))
aw = clock.pivot(index="session", columns="condition", values="evoked")
print("files where the evoked count differs between conditions by more than 10%%: %d of %d"
      % ((abs(aw.awake / aw.isoflurane - 1) > 0.1).sum(), len(aw)))
EOF
cat > t3.py <<'EOF'
import sys, pickle, os
sys.path.insert(0, "entries/burman-2023")
import numpy as np, pandas as pd, npx
from scipy import stats
if os.path.exists("S.pkl"):
    S = pickle.load(open("S.pkl","rb"))
else:
    assets = npx.assets()
    assets["session"] = assets.path.str.split("/").str[1].str.replace("_behavior+ecephys.nwb", "", regex=False)
    S = {k: npx.read_session(assets.set_index("session").loc[k, "asset_id"]) for k in npx.SESSIONS}
    pickle.dump(S, open("S.pkl","wb"))
for f in sys.argv[1:]:
    exec(open(f).read())
EOF
$TMPDIR/dev/bin/python t3.py clock_cell.py
```

```
session   condition  trials  units  evoked  shift -1.5 s  shift +1.5 s  evoked / shifted  wilcoxon p
0   sub-546655_ses-20201023       awake     359     18    1.74         0.398         0.354              4.64    5.31e-43
1   sub-546655_ses-20201023  isoflurane     301     18     0.9        0.0532       0.00664              30.1    2.53e-37
2   sub-551397_ses-20210211       awake     360     84    12.2           3.7          3.53              3.36    5.27e-37
3   sub-551397_ses-20210211  isoflurane     360     84    6.03           1.4          1.46              4.22    1.87e-35
4   sub-551399_ses-20210128       awake     358     89    14.8          2.22           2.1              6.86    2.83e-60
5   sub-551399_ses-20210128  isoflurane     359     89    5.41        0.0947         0.184              38.8    2.27e-57
6   sub-569062_ses-20210218       awake     360    120    8.17          4.45          4.24              1.88    4.88e-14
7   sub-569062_ses-20210218  isoflurane     360    120     2.9          1.01          1.33              2.48    2.76e-15
8   sub-569064_ses-20210408       awake     360     24    2.79         0.506         0.378              6.32    1.91e-49
9   sub-569064_ses-20210408  isoflurane     357     24   0.717         0.112         0.042              9.31    1.98e-33
10  sub-569068_ses-20210304       awake     359     49    7.36          1.67          1.87              4.16    2.34e-42
11  sub-569068_ses-20210304  isoflurane     357     49    2.24         0.793         0.742              2.92    1.05e-12
12  sub-569069_ses-20210312       awake     357     29    1.55          1.53          1.36              1.07       0.591
13  sub-569069_ses-20210312  isoflurane     359     29   0.967          0.39         0.482              2.22    2.13e-12
14  sub-569072_ses-20210422       awake     359     83    9.27          3.84          3.42              2.55    5.64e-53
15  sub-569072_ses-20210422  isoflurane     360     83    6.22         0.819        
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > gist_cell.py <<'EOF'
# The paper's analysis gist, run unmodified on the loaded data (npx.run_gist), against npx's
# measures for the gist's own selection (reading A2, waveform > 0.4 ms) and rate (F2), per unit.
G = npx.run_gist(S)
cols = {"rate_F2": "Firing rate [Hz] ({})", "entropy": "Entropy [nats] ({})", "synchrony": "Synchrony ({})"}
cmp_rows, gist_all = [], []
for k in npx.SESSIONS:
    g, T = G[k], npx.unit_table(S[k], "A2", "gt")
    m = g.merge(T, left_on="id", right_on="row", how="outer", indicator=True)
    row = dict(session=k, gist_units=len(g), npx_units=len(T), matched=int((m._merge == "both").sum()))
    for c, sfx in zip(npx.CONDITIONS, ("_aw", "_an")):
        for ours, theirs in cols.items():
            a, b = m[theirs.format(c)].to_numpy(float), m[ours + sfx].to_numpy(float)
            same = np.isclose(a, b, rtol=1e-8, atol=0) | (np.isnan(a) & np.isnan(b))
            row[f"{ours}{sfx} differ"] = int((~same).sum())
    cmp_rows.append(row)
    gist_all.append(g)
cmp_ = pd.DataFrame(cmp_rows)
print(cmp_.to_string())
print("\nunits in the gist's tables:", int(cmp_.gist_units.sum()), "| matched to npx by id:", int(cmp_.matched.sum()),
      "| values differing (relative tolerance 1e-8):", int(cmp_.filter(like="differ").to_numpy().sum()))
ga = pd.concat(gist_all, ignore_index=True)
fr = ga[["Firing rate [Hz] (awake)", "Firing rate [Hz] (isoflurane)"]]
exc = ((fr < 0.1) | (fr > 200)).any(axis=1)
print("the Methods' exclusion applied to the gist's rate column: %d kept, %d excluded" % ((~exc).sum(), exc.sum()))
EOF
$TMPDIR/dev/bin/python t3.py gist_cell.py
```

```
session  gist_units  npx_units  matched  rate_F2_aw differ  entropy_aw differ  synchrony_aw differ  rate_F2_an differ  entropy_an differ  synchrony_an differ
0   sub-546655_ses-20201023          18         18       18                  0                  0                    0                  0                  0                    0
1   sub-551397_ses-20210211          84         84       84                  0                  0                    0                  0                  0                    0
2   sub-551399_ses-20210128          89         89       89                  0                  0                    0                  0                  0                    0
3   sub-569062_ses-20210218         120        120      120                  0                  0                    0                  0                  0                    0
4   sub-569064_ses-20210408          24         24       24                  0                  0                    0                  0                  0                    0
5   sub-569068_ses-20210304          49         49       49                  0                  0                    0                  0                  0                    0
6   sub-569069_ses-20210312          29         29       29                  0                  0                    0                  0                  0                    0
7   sub-569072_ses-20210422          83         83       83                  0                  0                    0                  0                  0                    0
8   sub-569073_ses-20210415          28         28       28                  0                  0                    0                  0                  0                    0
9   sub-569073_ses-20210416          12         12       12                  0                  0                    0                  0                  0                    0
10  sub-571619_ses-20210319          95         95       95   
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat >> gist_cell.py <<'EOF'
K = ga[~exc]
for m in ("Synchrony", "Entropy [nats]"):
    a, b = K[f"{m} (awake)"], K[f"{m} (isoflurane)"]
    ok = a.notna() & b.notna()
    print(f"{m} of the kept units from the gist's table: awake {a[ok].mean():.4f}, isoflurane {b[ok].mean():.4f} (n = {ok.sum()})")
EOF
$TMPDIR/dev/bin/python t3.py gist_cell.py | tail -3; date -u
```

```
the Methods' exclusion applied to the gist's rate column: 662 kept, 203 excluded
Synchrony of the kept units from the gist's table: awake 0.3253, isoflurane 0.3928 (n = 662)
Entropy [nats] of the kept units from the gist's table: awake 1.3474, isoflurane 1.1106 (n = 597)
Tue Nov 10 09:11:13 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/burman-2023 && CLOCK=$TMPDIR/w/clock_cell.py GISTC=$TMPDIR/w/gist_cell.py python - <<'EOF'
import json, os
p='reproduce_burman_2023.ipynb'; d=json.load(open(p))
C=d['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source'] = s.splitlines(keepends=True)
def md(s, tags=None):
    c={"cell_type":"markdown","metadata":{},"source":s.splitlines(keepends=True)}
    if tags: c['metadata']['tags']=tags
    return c
def code(s, tags=None):
    c={"cell_type":"code","metadata":{},"execution_count":None,"outputs":[],"source":s.splitlines(keepends=True)}
    if tags: c['metadata']['tags']=tags
    return c
assert src(8).startswith("# Population spike count")
setsrc(8, open(os.environ['CLOCK']).read().rstrip('\n'))
assert src(9).startswith("In both files")
setsrc(9, src(9).replace(src(9).split("\n\n")[0], """In 33 of the 34 file and condition pairs, the 2 to 12 ms window after the pulse holds 1.5 to 39
times the spikes of the same window 1.5 s before and after it (Wilcoxon p below 0.001), and in 15
of 17 files the evoked count differs between awake and isoflurane by more than 10%. The exception
is the awake trials of sub-569069_ses-20210312 (1.55 against 1.45 spikes per trial, p = 0.59),
where the selected units barely respond awake; its isoflurane trials, on the same file clock,
pass (2.2 times, p = 2e-12). This is consistent with spikes and trials sharing one clock in all
17 files; for that file it rests on its isoflurane trials."""))
# p formatting
s21=src(21); assert 'var = pd.DataFrame(var).round(4)' in s21
setsrc(21, s21.replace('var = pd.DataFrame(var).round(4)\nvar["p"] = var.p.map(lambda p: f"{p:.2e}")',
 'var = pd.DataFrame(var)\nvar["p"] = var.p.map(lambda p: f"{p:.2e}")  # formatted before rounding, so small p are kept\nvar = var.round(4)'))
s28=src(28); assert 'rt = pd.DataFrame(rows).round(3)\nrt["p"] = rt.p.map(lambda p: f"{p:.2e}")' in s28
setsrc(28, s28.replace('rt = pd.DataFrame(rows).round(3)\nrt["p"] = rt.p.map(lambda p: f"{p:.2e}")',
 'rt = pd.DataFrame(rows)\nrt["p"] = rt.p.map(lambda p: f"{p:.2e}")  # formatted before rounding, so small p are kept\nrt = rt.round(3)'))
# figs4 lines
s0=src(0); old='| figs4-intrinsic-properties | blocked: other (the Figure S4 measure is in the unsupplied supplement; Matlab analysis) |'
assert old in s0
new='| figs4-intrinsic-properties | blocked: methods_underspecified (see below) |'
s0=s0.replace(old,new)
s0 += """

**figs4-intrinsic-properties.** The paper's NEURON model of an L2/3 pyramidal neuron and its
analysis are public (github.com/richardjburman/burman-et-al-2022---Awake-EGABAAR at commit
a404c3e: hoc files and a Matlab analysis, NEURON_Egaba_Analysis.m), and the Methods ("Simulating
measurements of synaptic EGABAAR", Table 2) give its parameters: membrane properties per state,
20 synapses within 75 µm of the soma, E_GABA set from -85 to -35 mV in 5 mV steps, two voltage
ramps before and during GABA_A activation, estimates with 0% or 90% series resistance
correction. A simulation of the ramp estimates under the anesthetized and awake membrane
properties could be run. What it would be judged against is not fixed: the measure Figure S4
shows and the comparison that supports "could not be explained" are in the Figure S4 legend,
which was not in the text read, and the claims file gives no criterion. Any choice (for example,
the estimation error under each state's properties against the measured difference in synaptic
E_GABA of Figure 2H) would be arbitrary, so the claim is blocked as methods_underspecified and
not simulated. The question is for the paper's authors (attempt record, findings)."""
setsrc(0, s0)
s34=src(34); assert old in s34
setsrc(34, s34.replace(old, '| figs4-intrinsic-properties | blocked: methods_underspecified (the NEURON model is public; the Figure S4 measure and comparison are in the unread legend) |'))
# insert gist check after cell 11
assert src(11).startswith("No two files share")
newcells=[md("""**The paper's own code.** The analysis gist (gist a77bcf5e, revision 43a13d89) is run unmodified
on the loaded data: `npx.run_gist` gives it the trials and units through a stand-in for pynwb and
captures the table it would save. Its values are compared per unit with `npx`'s for the gist's
selection (reading A2, waveform > 0.4 ms) and rate (F2)."""),
 code(open(os.environ['GISTC']).read().rstrip('\n'), tags=['sanity']),
 md("""The gist's tables hold the same 865 units as `npx`'s A2 selection, and every rate, entropy and
synchrony value agrees with `npx`'s F2 reading in both conditions (0 differ). Applying the Methods'
exclusion to the gist's rate column keeps 662 units and excludes 203, the paper's numbers, and the
kept units' means are the paper's Figure 4D values (synchrony 0.3253 and 0.3928, entropy 1.3474
and 1.1106 over the 597 units defined in both conditions). So `npx`'s F2 denominator and trial
order are the gist's, and the paper's numbers are what its code gives on this version.""")]
C[12:12]=newcells
json.dump(d, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat
```

```
entries/burman-2023/npx.py                      |  83 ++++++++++++-
 entries/burman-2023/reproduce_burman_2023.ipynb | 158 ++++++++++++++++++------
 2 files changed, 199 insertions(+), 42 deletions(-)
```

**Agent calls Bash**

```bash
git diff reproduce_burman_2023.ipynb | head -30; git diff reproduce_burman_2023.ipynb | tail -15
```

```
diff --git a/entries/burman-2023/reproduce_burman_2023.ipynb b/entries/burman-2023/reproduce_burman_2023.ipynb
index 00ffcfaad1..ca90818440 100644
--- a/entries/burman-2023/reproduce_burman_2023.ipynb
+++ b/entries/burman-2023/reproduce_burman_2023.ipynb
@@ -33,11 +33,25 @@
     "| fig4-rate-higher-awake | tested |\n",
     "| figs6-rate-regressed | tested (regression readings R1 to R3) |\n",
     "| fig4f-model-hyperpolarizing-less-activity, fig4h-model-synchrony, fig4h-model-entropy, figs7-model-decoding | tested in `network_model.ipynb` |\n",
-    "| figs4-intrinsic-properties | blocked: other (the Figure S4 measure is in the unsupplied supplement; Matlab analysis) |\n",
+    "| figs4-intrinsic-properties | blocked: methods_underspecified (see below) |\n",
     "| 24 patch-clamp claims (fig1b to fig3j, rm-*, figs2, figs3, figs5) | blocked: data_missing |\n",
     "\n",
     "Every method is the claims file's (opening comment N1 to N8); where it lacks a detail, the passage\n",
-    "of the paper used is cited in the cell or in `npx.py`."
+    "of the paper used is cited in the cell or in `npx.py`.\n",
+    "\n",
+    "**figs4-intrinsic-properties.** The paper's NEURON model of an L2/3 pyramidal neuron and its\n",
+    "analysis are public (github.com/richardjburman/burman-et-al-2022---Awake-EGABAAR at commit\n",
+    "a404c3e: hoc files and a Matlab analysis, NEURON_Egaba_Analysis.m), and the Methods (\"Simulating\n",
+    "measurements of synaptic EGABAAR\", Table 2) give its parameters: membrane properties per state,\n",
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > gsim.py <<'EOF'
import sys, types, time
sys.path.insert(0, "entries/burman-2023")
import numpy as np, brian2 as b2, network
src = open("../g2.py").read()
seed=7
t=time.time()
a = network.simulate(seed, stimuli=10, repeats=5, periodic=True, spikes=True)
print("ours", time.time()-t)
sys.modules["umap"] = types.SimpleNamespace(UMAP=None)
sys.argv = ["gist", "--stimuli", "10", "--repeats", "5"]
np.random.seed(seed); b2.seed(seed)
g = {"__name__": "__main__"}
t=time.time()
try:
    exec(compile(src, "gist", "exec"), g)
except Exception as e:
    print("gist stopped:", type(e).__name__, e)
print("gist", time.time()-t)
tg = np.asarray(g["spike_monitor"]["exc"].t / b2.ms); ig = np.asarray(g["spike_monitor"]["exc"].i)
ta, ia = a["spikes"]
print(len(ta), len(tg), np.array_equal(ia, ig), np.allclose(ta, tg) if len(ta)==len(tg) else None)
for k in ("entropy","synchrony","firing_rates","accuracy"):
    print(k, k in g)
if "synchrony" in g:
    print(np.allclose(g["synchrony"], a[-80]["synchrony"], equal_nan=True), np.allclose(g["entropy"], a[-80]["entropy"], equal_nan=True), np.allclose(g["firing_rates"], a[-80]["firing_rate"]), g["accuracy"], a[-80]["accuracy"])
EOF
$TMPDIR/dev/bin/python gsim.py 2>&1 | grep -v Warning | tail -12
```

```
ours 50.99659276008606
Time elapsed: 29.11 seconds.
Time elapsed: 1.09 seconds.
gist stopped: TypeError 'coo_matrix' object is not subscriptable
gist 30.42440938949585
19093 19093 True True
entropy False
synchrony False
firing_rates False
accuracy False
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > eta.py <<'EOF'
import brian2 as b2
b2.prefs.codegen.target="numpy"
G = b2.NeuronGroup(2, "v:1")
ns = dict(eta=0.1)
S = b2.Synapses(G, G, model="w:1", on_pre="w += eta", namespace=ns)
S.connect()
net = b2.Network(G, S)
net.run(1*b2.ms, namespace={})
r = S.resolve_all(["eta"], run_namespace={})
print(type(r["eta"]), r["eta"].get_value())
ns["eta"]=0.
r = S.resolve_all(["eta"], run_namespace={})
print(r["eta"].get_value())
# also check the code object of the pre pathway
print([ (k) for k in S.pre.codeobj.variables if 'eta' in k] if S.pre.codeobj else None)
print(S.pre.codeobj.variables.get('eta').get_value() if S.pre.codeobj else None)
EOF
$TMPDIR/dev/bin/python eta.py 2>&1 | tail -5
```

```
File "/tmp/claude-1001/dev/lib/python3.13/site-packages/brian2/synapses/synapses.py", line 1354, in _add_updater
    raise ValueError(
    ...<2 lines>...
    )
ValueError: Source group 'neurongroup' does not define an event 'spike'. Did you forget to set a 'threshold'?
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && sed -i 's/G = b2.NeuronGroup(2, "v:1")/G = b2.NeuronGroup(2, "v:1", threshold="True")/' eta.py && cat >> eta.py <<'EOF'
net.run(1*b2.ms, namespace={})
print("after second run", S.pre.codeobj.variables['eta'].get_value(), S.w[:])
EOF
$TMPDIR/dev/bin/python eta.py 2>&1 | tail -6
```

```
WARNING    The NeuronGroup 'neurongroup' sets a threshold but neither a reset condition nor a refractory condition has been set. Did you forget either of those? If this was intended, set the reset argument to an empty string in order to avoid this warning. [brian2.groups.neurongroup.only_threshold]
<class 'brian2.core.variables.Constant'> 0.1
0.0
['eta']
0.1
after second run 0.0 [1. 1. 1. 1.]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/burman-2023 && python - <<'EOF'
p='network.py'; s=open(p).read()
old='''    timing, w_sums = [], []
    for sim_time, eta in zip((balancing_time, testing_time), (0.1, 0.)):
        syn_ns["eta"] = eta
        tic = time.time()
        net.run(sim_time * b2.ms, namespace={})
        timing.append(time.time() - tic)
        w_sums.append(float(np.sum(synapses[3].w / b2.nsiemens)))
'''
new='''    # eta_used: the value of eta in the compiled code of the plastic synapses' pre and post
    # pathways after each run, i.e. the value Brian 2 used in that run
    timing, w_sums, eta_used = [], [], []
    for sim_time, eta in zip((balancing_time, testing_time), (0.1, 0.)):
        syn_ns["eta"] = eta
        tic = time.time()
        net.run(sim_time * b2.ms, namespace={})
        timing.append(time.time() - tic)
        w_sums.append(float(np.sum(synapses[3].w / b2.nsiemens)))
        eta_used.append([float(getattr(synapses[3], path).codeobj.variables["eta"].get_value())
                         for path in ("pre", "post")])
'''
assert old in s; s=s.replace(old,new)
old='''    out["w_sums"] = [float(len(synapses[3]) * 1.0)] + w_sums
'''
new='''    out["w_sums"] = [float(len(synapses[3]) * 1.0)] + w_sums
    out["eta_used"] = eta_used
'''
assert old in s; s=s.replace(old,new)
s += '''

GIST_URL = ("https://gist.githubusercontent.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f/raw/"
            "f6a05661c10051560aa381e334099efd8521617b/burman_et_al_2023_neuronal_network_simulation.py")


def run_gist(seed, stimuli=10, repeats=5):
    """Run the paper's simulation gist, unmodified, on a small network run, for the check that
    simulate() transcribes it. Returns the gist's module namespace after the run.

    The gist is fetched at its revision and run with its own command-line options (--stimuli,
    --repeats), after np.random.seed(seed) and b2.seed(seed) as in simulate(). Three things
    around it are changed, none in its code: umap, imported for a plot the run does not make, is
    a stand-in; scipy.sparse.coo_matrix returns a CSR matrix while it runs, as the installed
    scipy cannot index a COO matrix (X[:, :50]); and Brian 2's code generation target is cython,
    as in simulate(). Its decoding uses an unseeded shuffle, so its accuracy is not compared.
    """
    import sys
    import types
    import requests
    import scipy.sparse

    src = requests.get(GIST_URL, timeout=60).text
    saved = sys.argv, sys.modules.get("umap"), scipy.sparse.coo_matrix
    coo = scipy.sparse.coo_matrix
    sys.argv = ["burman_et_al_2023_neuronal_network_simulation.py",
                "--stimuli", str(stimuli), "--repeats", str(repeats)]
    sys.modules["umap"] = types.SimpleNamespace(UMAP=None)
    scipy.sparse.coo_matrix = lambda *a, **k: coo(*a, **k).tocsr()
    b2.prefs.codegen.target = "cython"
    np.random.seed(seed)
    b2.seed(seed)
    g = {"__name__": "__main__"}
    try:
        exec(compile(src, "burman_et_al_2023_neuronal_network_simulation.py", "exec"), g)
    finally:
        sys.argv, scipy.sparse.coo_matrix = saved[0], saved[2]
        if saved[1] is None:
            sys.modules.pop("umap", None)
        else:
            sys.modules["umap"] = saved[1]
    return g
'''
open(p,'w').write(s)
EOF
grep -n "Differences from the gist" -A3 network.py | head
```

```
13:Differences from the gist, none of which changes the model:
14-
15-- The gist builds the stimulus as one array for the whole run (502,500 by 1,000 values,
16-  4 GB, copied again when given units), which does not fit the runner's memory with a second
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && cat > gsim_cell.py <<'EOF'
# The paper's simulation gist, run unmodified (network.run_gist) on the same small network run
# and seed as `a` above, against network.simulate spike for spike, and per neuron for the last
# condition the gist analyses (hyperpolarizing, -80 mV), whose arrays its namespace keeps.
g = network.run_gist(7, stimuli=10, repeats=5)
tg = np.asarray(g["spike_monitor"]["exc"].t / network.b2.ms)
ig = np.asarray(g["spike_monitor"]["exc"].i)
print("excitatory spikes, gist:", len(tg), "| network.simulate:", len(ta))
print("identical spike trains:", len(ta) == len(tg) and np.array_equal(ia, ig) and np.allclose(ta, tg))
for theirs, ours in (("spike_counts", "spike_count"), ("firing_rates", "firing_rate"), ("entropy", "entropy"), ("synchrony", "synchrony")):
    x, y = np.asarray(g[theirs], float), a[-80][ours]
    print(f"{theirs} (-80 mV): equal in {int(np.isclose(x, y, rtol=1e-12, atol=0, equal_nan=True).sum())} of {len(y)} neurons")
EOF
cat > t4.py <<'EOF'
import sys
sys.path.insert(0, "entries/burman-2023")
import numpy as np, network
a = network.simulate(7, stimuli=10, repeats=5, periodic=True, spikes=True)
ta, ia = a["spikes"]
print(a["eta_used"], a["w_sums"])
exec(open("gsim_cell.py").read())
EOF
$TMPDIR/dev/bin/python t4.py 2>&1 | grep -v -i warn | tail -10
```

```
[[0.1, 0.1], [0.0, 0.0]] [15905.0, 16646.9122725674, 16646.9122725674]
Time elapsed: 0.31 seconds.
Time elapsed: 0.74 seconds.
excitatory spikes, gist: 19093 | network.simulate: 19093
identical spike trains: True
spike_counts (-80 mV): equal in 800 of 800 neurons
firing_rates (-80 mV): equal in 800 of 800 neurons
entropy (-80 mV): equal in 800 of 800 neurons
synchrony (-80 mV): equal in 800 of 800 neurons
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/burman-2023 && GS=$TMPDIR/w/gsim_cell.py python - <<'EOF'
import json, os
p='network_model.ipynb'; d=json.load(open(p))
C=d['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source'] = s.splitlines(keepends=True)
def md(s): return {"cell_type":"markdown","metadata":{},"source":s.splitlines(keepends=True)}
def code(s, tags=None):
    c={"cell_type":"code","metadata":{},"execution_count":None,"outputs":[],"source":s.splitlines(keepends=True)}
    if tags: c['metadata']['tags']=tags
    return c
# cell 4: eta used
s=src(4); old='''print("\\nweights after balancing equal weights after the test in every run:",
      all(abs(r["w_sums"][1] - r["w_sums"][2]) < 1e-6 for r in runs))'''
assert old in s
setsrc(4, s.replace(old, old + '''
print("eta in the plastic synapses' compiled code (pre, post), balancing run / test run:",
      sorted({str(r["eta_used"]) for r in runs}))'''))
# cells 7 and 10: run-to-run SE
for i, key, exp in ((7, "synchrony", (0.784, 0.881)), (10, "entropy", (0.451, 0.197))):
    s = src(i)
    marker = 'pr.shunting.min(), pr.shunting.max(), pr.hyperpolarizing.min(), pr.hyperpolarizing.max()))\n'
    assert marker in s
    add = f'''# the spread between seeds: standard error of the 20-run mean (SD of the per-run means / sqrt(20)),
# and the distance of each pooled mean from the paper's value in units of it
for cond, mean, paper in (("shunting", {key[:3]}_sh, {exp[0]}), ("hyperpolarizing", {key[:3]}_hy, {exp[1]})):
    se = pr[cond].std(ddof=1) / np.sqrt(len(pr))
    print(f"{{cond}}: run-to-run SE of the mean {{se:.4f}}; pooled mean {{mean:.4f}} is {{abs(mean - paper) / se:.1f}} SE from {{paper}}")
'''
    setsrc(i, s.replace(marker, marker + add, 1))
assert src(3).startswith("a = network.simulate(7")
C[4:4] = [md("""Then a check that `network.py` transcribes the gist: the gist itself, fetched at its revision and
run unmodified with the same small options and seed (`network.run_gist`; its docstring lists what
is changed around it: a stand-in for umap, CSR in place of COO for the installed scipy)."""),
          code(open(os.environ['GS']).read().rstrip('\n'), tags=['sanity'])]
json.dump(d, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
EOF
python -c "
import json;d=json.load(open('network_model.ipynb'))
for i in (5,6,9,12): print(i, ''.join(d['cells'][i]['source'])[-900:]); print('----')"
```

```
Traceback (most recent call last):
  File "<stdin>", line 22, in <module>
AssertionError
5 def pooled(key):
    sh = np.concatenate([r[-60][key] for r in runs])
    hy = np.concatenate([r[-80][key] for r in runs])
    return sh, hy
def paired_report(key, label):
    sh, hy = pooled(key)
    ok = ~np.isnan(sh) & ~np.isnan(hy)
    t = stats.ttest_rel(sh[ok], hy[ok])
    print(f"{label}: neurons {len(sh)}, defined in both conditions {ok.sum()} (dropped {(~ok).sum()})")
    print(f"  shunting {sh[ok].mean():.4f} +- {stats.sem(sh[ok]):.4f} (SEM), hyperpolarizing {hy[ok].mean():.4f} +- {stats.sem(hy[ok]):.4f}")
    print(f"  paired t test t = {t.statistic:.2f}, p = {t.pvalue:.2e}")
    print(f"  range shunting {np.nanmin(sh):.3f} to {np.nanmax(sh):.3f}, hyperpolarizing {np.nanmin(hy):.3f} to {np.nanmax(hy):.3f}")
    return sh[ok].mean(), hy[ok].mean(), t
----
6 ## fig4h-model-synchrony

> Model pyramidal neurons are less synchronous with shunting than with hyperpolarizing E_GABAAR
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
GS=$TMPDIR/w/gsim_cell.py python - <<'EOF'
import json, os
p='network_model.ipynb'; d=json.load(open(p))
C=d['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i, s): C[i]['source'] = s.splitlines(keepends=True)
def md(s): return {"cell_type":"markdown","metadata":{},"source":s.splitlines(keepends=True)}
def code(s, tags=None):
    c={"cell_type":"code","metadata":{},"execution_count":None,"outputs":[],"source":s.splitlines(keepends=True)}
    if tags: c['metadata']['tags']=tags
    return c
s=src(4); old='''print("\\nweights after balancing equal weights after the test in every run:",
      all(abs(r["w_sums"][1] - r["w_sums"][2]) < 1e-6 for r in runs))'''
assert old in s
setsrc(4, s.replace(old, old + '''
print("eta in the plastic synapses' compiled code (pre, post), balancing run / test run:",
      sorted({str(r["eta_used"]) for r in runs}))'''))
for i, key, exp in ((7, "synchrony", (0.784, 0.881)), (10, "entropy", (0.451, 0.197))):
    s = src(i)
    marker = 'pr.shunting.min(), pr.shunting.max(), pr.hyperpolarizing.min(), pr.hyperpolarizing.max()))'
    assert marker in s
    add = f'''
# the spread between seeds: standard error of the 20-run mean (SD of the per-run means / sqrt(20)),
# and the distance of each pooled mean from the paper's value in units of it
for cond, mean, paper in (("shunting", {key[:3]}_sh, {exp[0]}), ("hyperpolarizing", {key[:3]}_hy, {exp[1]})):
    se = pr[cond].std(ddof=1) / np.sqrt(len(pr))
    print(f"{{cond}}: run-to-run SE of the mean {{se:.4f}}; pooled mean {{mean:.4f}} is {{abs(mean - paper) / se:.1f}} SE from {{paper}}")'''
    setsrc(i, s.replace(marker, marker + add, 1))
assert src(3).startswith("a = network.simulate(7")
C[4:4] = [md("""Then a check that `network.py` transcribes the gist: the gist itself, fetched at its revision and
run unmodified with the same small options and seed (`network.run_gist`; its docstring lists what
is changed around it: a stand-in for umap, CSR in place of COO for the installed scipy)."""),
          code(open(os.environ['GS']).read().rstrip('\n'), tags=['sanity'])]
json.dump(d, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
EOF
python -c "
import json;d=json.load(open('network_model.ipynb'))
print(''.join(d['cells'][9]['source']))"
```

```
syn_sh, syn_hy, syn_t = paired_report("synchrony", "synchrony")
print("expected shunting 0.784 +- 0.001, hyperpolarizing 0.881 +- 0.001")
pr = per_run.pivot(index="seed", columns="condition", values="synchrony_mean")
print("runs with lower mean synchrony under shunting: %d of %d; per-run means shunting %.4f to %.4f, hyperpolarizing %.4f to %.4f"
      % ((pr.shunting < pr.hyperpolarizing).sum(), len(pr), pr.shunting.min(), pr.shunting.max(), pr.hyperpolarizing.min(), pr.hyperpolarizing.max()))
# the spread between seeds: standard error of the 20-run mean (SD of the per-run means / sqrt(20)),
# and the distance of each pooled mean from the paper's value in units of it
for cond, mean, paper in (("shunting", syn_sh, 0.784), ("hyperpolarizing", syn_hy, 0.881)):
    se = pr[cond].std(ddof=1) / np.sqrt(len(pr))
    print(f"{cond}: run-to-run SE of the mean {se:.4f}; pooled mean {mean:.4f} is {abs(mean - paper) / se:.1f} SE from {paper}")
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
p='reproduce_burman_2023.ipynb'; d=json.load(open(p)); C=d['cells']
for i,c in enumerate(C):
    s=''.join(c['source'])
    if s.startswith('**Result: partially reproduced.** Under the Methods reading A1F1, 865'):
        old='the paper\'s exclusion matches this rate, not the Methods\' count rate.'
        assert old in s
        s=s.replace(old, old+' The gist itself, run on\nthe same data in the data check, gives the same 662 and 203.')
        c['source']=s.splitlines(keepends=True); print(i)
json.dump(d, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
EOF
sed -i 's/| Multi-compartment model of Figure S4 | Blocked: other |/| Multi-compartment model of Figure S4 | Blocked: methods underspecified |/' README.md; grep -n "Figure S4" README.md; cd  && python tools/entry.py check entries/burman-2023 2>&1 | tail -5; date -u
```

```
21
22:| Multi-compartment model of Figure S4 | Blocked: methods underspecified |
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
0 error(s)
Tue Nov 10 09:14:34 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/burman-2023 && python - <<'EOF'
import json, uuid
for p in ('reproduce_burman_2023.ipynb','network_model.ipynb'):
    d=json.load(open(p)); n=0
    for c in d['cells']:
        if 'id' not in c: c['id']=uuid.uuid4().hex[:8]; n+=1
    print(p, d['nbformat'], d['nbformat_minor'], n)
    json.dump(d, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
EOF
cd ../.. && python tools/entry.py check entries/burman-2023 2>&1 | tail -2
```

```
reproduce_burman_2023.ipynb 4 5 3
network_model.ipynb 4 5 2
0 error(s)
```

**Agent**

Edits are in place; running the full entry now (about 30 minutes, from the earlier run times).

**Agent calls Bash**

```bash
time python tools/entry.py all entries/burman-2023 2>&1 | grep -v MissingID | tail -15
```

```
Installed kernelspec registry-burman-2023 in executed/burman-2023/.venv/share/jupyter/kernels/registry-burman-2023
0 error(s)
pass  reproduce_burman_2023.ipynb  (147 s)
pass  network_model.ipynb  (1091 s)

real	20m45.665s
user	58m24.918s
sys	0m25.587s
```

**Agent calls Bash**

```bash
cd executed/burman-2023 && python - <<'EOF'
import json
for nb, idx in (('network_model.ipynb', None), ('reproduce_burman_2023.ipynb', [8,12,13,22,23,24,30,31,32,33,34])):
    d=json.load(open(nb))
    for i,c in enumerate(d['cells']):
        if c['cell_type']!='code' or (idx and i not in idx): continue
        out=''.join(''.join(o.get('text','')) for o in c['outputs'] if o.get('output_type')=='stream')
        print(f'=== {nb} [{i}]'); print(out[-2500:])
EOF
```

```
=== network_model.ipynb [1]
dataset named for the record: 000458 0.230317.0039 (not used by this notebook)

=== network_model.ipynb [3]
spikes, periodic stimulus: 19093 | gist's whole-run array: 19093
identical spike trains: True
inhibitory-to-excitatory summed weight (nS): start 15905, after balancing 16646.9, after test 16646.9

=== network_model.ipynb [5]
Time elapsed: 8.72 seconds.
Time elapsed: 1.14 seconds.
excitatory spikes, gist: 19093 | network.simulate: 19093
identical spike trains: True
spike_counts (-80 mV): equal in 800 of 800 neurons
firing_rates (-80 mV): equal in 800 of 800 neurons
entropy (-80 mV): equal in 800 of 800 neurons
synchrony (-80 mV): equal in 800 of 800 neurons

=== network_model.ipynb [6]
147          0.8721    0.9361
[... 196 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/burman-2023 && python - <<'EOF'
import json
p='network_model.ipynb'; d=json.load(open(p)); C=d['cells']
def rep(old,new):
    n=0
    for c in C:
        s=''.join(c['source'])
        if old in s:
            c['source']=s.replace(old,new).splitlines(keepends=True); n+=1
    assert n==1, old
rep("The per-run hyperpolarizing means span 0.8661 to 0.8909, so the tolerance, the paper's SEM over pooled neurons, is narrower than the spread between runs with other seeds.",
    "The per-run hyperpolarizing means span 0.8661 to 0.8909, and the standard error of a 20-run mean from that spread is 0.0013, so the tolerance, the paper's SEM over pooled neurons, is narrower than the spread between runs with other seeds: the hyperpolarizing mean is 1.6 of these SEs from 0.881, the shunting mean 1.3 from 0.784.")
rep("Per-run hyperpolarizing means span 0.1798 to 0.2217, wider than the tolerance.",
    "Per-run hyperpolarizing means span 0.1798 to 0.2217, wider than the tolerance; the standard error of a 20-run mean from that spread is 0.0023, and the hyperpolarizing mean is 1.9 of these SEs from 0.197 (the shunting mean 0.4 from 0.451).")
rep("D1 paired t = 16.92, p = 6.52e-13", "D1 paired t = 16.42, p = 1.11e-12")
rep("""The two partial outcomes are means a little outside tolerances that are the SEM over pooled
neurons; the spread of the per-run means is wider, and the paper's seeds are not known.""",
"""The two partial outcomes are means a little outside tolerances that are the SEM over pooled
neurons; the spread of the per-run means is wider (the standard error of a 20-run mean is 0.0013
for synchrony and 0.0023 for entropy, and the misses are 1.6 and 1.9 of these), and the paper's
seeds are not known.""")
rep("""**How the analysis differs from the paper's.** The model is the paper's code, with the stimulus held
as one periodic set to fit in memory (identical spikes, checked above) and seeds fixed, so the 20
runs are other draws of the same model than the paper's.""",
"""**How the analysis differs from the paper's.** The model is the paper's code, with the stimulus held
as one periodic set to fit in memory and seeds fixed, so the 20 runs are other draws of the same
model than the paper's. On a small run with one seed, `network.py` gives the same spikes as its
own whole-run stimulus and as the gist itself run unmodified, and the same per-neuron rate,
entropy and synchrony as the gist; in every full run the learning rate in the compiled synapse
code is 0.1 during balancing and 0 during the test (checked above).""")
json.dump(d, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
p='reproduce_burman_2023.ipynb'; d=json.load(open(p)); C=d['cells']
rep("(paired t test, t = 12.36, p below 0.05, table above)", "(paired t test, t = 12.36, p = 5.75e-32, table above)")
json.dump(d, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
EOF
python -c "
import json;d=json.load(open('network_model.ipynb'))
for c in d['cells']:
  if c['cell_type']=='markdown': print(''.join(c['source'])[:300]); print('--')" | sed -n 1,200p | grep -n "Data check" -A12
```

```
7:## Data check
8-
9-The model's data are its simulated spikes. First a check that the stimulus held as one periodic set (`network.py`) gives the same spikes as the gist's whole-run array, on a small network run (10 patterns, 5 repeats) with one seed.
10---
11-Then a check that `network.py` transcribes the gist: the gist itself, fetched at its revision and
12-run unmodified with the same small options and seed (`network.run_gist`; its docstring lists what
13-is changed around it: a stand-in for umap, CSR in place of COO for the installed scipy).
14---
15-## fig4h-model-synchrony
16-
17-> Model pyramidal neurons are less synchronous with shunting than with hyperpolarizing E_GABAAR
18-> (0.784 against 0.881).
19---
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json, uuid
p='network_model.ipynb'; d=json.load(open(p)); C=d['cells']
assert ''.join(C[6]['source']).startswith('t = time.time()\nwith Pool(4)')
C.insert(7, {"cell_type":"markdown","id":uuid.uuid4().hex[:8],"metadata":{},"source":
"""The gist run unmodified gives the same 19,093 excitatory spikes as `network.simulate` on the
small run, and the same spike count, rate, entropy and synchrony for all 800 excitatory neurons
of its hyperpolarizing condition. In all 20 full runs every excitatory neuron spikes in both
conditions, the summed inhibitory weight is the same after the test as after balancing, and the
compiled code of the plastic synapses used eta = 0.1 during balancing and eta = 0 during the
test, as the gist's loop sets it.""".splitlines(keepends=True)})
json.dump(d, open(p,'w'), indent=1, ensure_ascii=False); open(p,'a').write('\n')
EOF
date -u
```

```
Tue Nov 10 09:35:53 UTC 2026
```

**Agent calls Bash**

```bash
cd  head -30 questions/berg-2020.yaml
```

```
# Questions from attempt berg-2020-01 (author, 2026-10-23) about the claims file
# claims/000023/10.1101-2020.03.31.018820.yaml. Each is asked under docs/protocol.md, Author, step 1.6;
# the attempt runs every reading it can see, or blocks the claim as methods_underspecified until the
# question is answered.
dandiset: "000023"
paper: doi:10.1101/2020.03.31.018820
questions:
- claim: features-and-labels-link
  also: [cohort-cells, cohort-donors, cohort-type-counts, fig3d-depth-by-type, fig4e-human-ephys-anova,
    fig4-glp2r-sag, edtable1-species-ephys, edfig6-classifier-human-ephys, fig5c-frem3-ephys-depth,
    fig6-deep-ephys-anova, fig6c-carm1p1-upstroke-rin, fig6c-col22a1-rin-fi-sag, fig2ef-pathology-ephys]
  asked: 2026-10-23
  question: The criterion matches cells "by the specimen ID (SpecimenID in the code's cell table)", but
    no file carries a SpecimenID. Each file carries the donor (in its cell name, such as
    H17.06.003.11.07.04, and as subject_id) and an ephys session id (session_id, in the file name)
    that is 13 to 685 below one SpecimenID of the same donor in the code's table. Should cells be
    matched (M1) only through a SpecimenID stored in the files, which matches none, or (M2) through
    the SpecimenID recovered from the file, the next id of the same donor in the code's table, with
    the code's per-cell features as the check?
  passage: None in the paper; the Methods name no identifiers. The code joins its tables on SpecimenID
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -o ".\{400\}200 Hz.\{200\}" paper/*.txt; grep -o ".\{300\}0.784 ± 0.001.\{100\}" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o ".\{500\}200 \?Hz.\{200\}" paper/*.txt | head -3; grep -o ".\{200\}0\.784.\{150\}" paper/*.txt | head -2
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -i ".\{300\}0\.1 Hz.\{300\}" paper/*.txt | head -3; grep -o -i ".\{10\}average evoked.\{200\}" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -i ".\{600\}s with an average evoked firing rate below" paper/*.txt | head -1
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the questions file.

**Agent calls Write**

```json
{
 "file_path": "questions/burman-2023.yaml",
 "content": "# Questions from attempt burman-2023-01 (author revision after verifier round 1, 2026-11-10) about\n# the claims file claims/burman-2023.yaml. Both were raised by the verifier as points about the\n# claims file (verifier-1 report, B1 and B2). The attempt tests the claims as the file has them and\n# shows the other reading as a variant; the outcomes stay as tested.\npaper: doi:10.1016/j.neuron.2023.08.005\nquestions:\n- claim: fig4c-sample\n  also: [fig4d-synchrony-lower-awake, fig4d-entropy-higher-awake]\n  asked: 2026-11-10\n  question: >-\n    The opening comment (N7) judges every Neuropixels claim under the Methods reading of the evoked\n    rate (F1, a spike count over trials times 10 ms) and shows the gist's rate (F2, which sums the\n    spikes' latencies in ms) as a variant. The paper's reported numbers are what F2 gives: the\n    analysis gist, run unmodified on version 0.230317.0039, keeps 662 and excludes 203 units and\n    gives synchrony 0.3253 and 0.3928 and entropy 1.3474 and 1.1106, the values of Figure 4C and\n    4D; F1 gives 721 and 144, synchrony 0.3188 and 0.3862, entropy 1.3887 and 1.1502. Should the\n    expected values of these claims be judged under F2, the reading the paper's numbers were\n    computed with, keeping F1 as a variant, or does the Methods' wording take precedence as the\n    file has it?\n  passage: >-\n    Methods, Pre-processing of Neuropixels dataset, \"Neurons with an average evoked firing rate\n    below 0.1 Hz or above 200 Hz in either condition (awake/anesthesia) were excluded from further\n    analysis (203 neurons). The 662 remaining neurons derived from 17 recordings in 16 mice\"; the\n    gist's get_firing_rate (np.sum of spike_times over the trials times 10 ms).\n  why: >-\n    Under F1 the three claims are partially reproduced (excluded 144 against 203 +- 20.3, awake\n    synchrony 0.3188 against 0.320 to 0.330, both entropy means outside tolerance); under F2 every\n    expected value is matched and all three would be reproduced. The direction and the tests hold\n    under both.\n- claim: fig4h-model-synchrony\n  also: [fig4h-model-entropy]\n  asked: 2026-11-10\n  question: >-\n    The tolerances of the model means (0.001 for synchrony, 0.002 for entropy) are the paper's SEM\n    over 16,000 pooled neurons. The criterion reruns the gist with seeds other than the paper's\n    (the gist sets none), so the 20-run mean varies between sets of seeds by its run-to-run\n    standard error, 0.0013 for synchrony and 0.0023 for entropy in the hyperpolarizing condition\n    here, larger than the tolerances. Is the SEM over pooled neurons the intended tolerance for a\n    rerun with other seeds, or should the tolerance allow for the spread between runs (for\n    example the standard error of the 20-run mean, or a multiple of it)?\n  passage: >-\n    Figure 4H legend, \"Neurons in the shunting E GABAAR condition exhibited lower synchrony (Shunt\n    0.784 ± 0.001 vs. Hyperpol 0.881 ± 0.001, p < 0.001, paired t test) and higher entropy (Shunt\n    0.451 ± 0.002 nats vs. Hyperpol 0.197 ± 0.002 nats, p < 0.001, paired t test)\"; Methods,\n    Neuronal network simulations, \"Each simulation was repeated 20 times\".\n  why: >-\n    The hyperpolarizing means here, 0.8789 and 0.2014, miss the tolerances by 0.0011 and 0.0024,\n    1.6 and 1.9 run-to-run standard errors from the paper's values. With a tolerance that allows\n    for seed noise both claims would be reproduced; with the SEM over neurons they are partially\n    reproduced. The direction and the tests hold in all 20 runs.\n"
}
```

```
File created successfully at: questions/burman-2023.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -n "questions" tools/*.py | head; head -8 questions/claar-2023.yaml 2>/dev/null; ls schemas
```

```
tools/agent_run.py:161:               "questions": paper_records.questions_file(key).relative_to(ROOT).as_posix(),
tools/build_site.py:191:    """A kind of record (claims, questions) with the datasets each is about: a paper's own file,
tools/build_site.py:389:    (papers/manifest.yaml), each claims file's last check, and each attempt's open questions."""
tools/build_site.py:392:    checks, questions, items = {}, {}, {}
tools/build_site.py:398:    for path, keys in record_files("questions"):
tools/build_site.py:400:        q = q.get("questions", []) if isinstance(q, dict) else q
tools/build_site.py:402:            questions[key] = sum(1 for x in q if not x.get("answered"))
tools/build_site.py:404:    return {"papers": {key_of_dir(str(k)): v for k, v in papers.items()}, "checks": checks, "questions": questions,
tools/build_site.py:585:                  ("attempt", "Attempt"), ("questions", "Questions"), ("verified", "Verified")]
tools/build_site.py:626:    inputs = data.get("pipeline") or {"papers": {}, "checks": {}, "questions": {}}
dandiset: "000458"
paper: doi:10.7554/elife.84630
questions:
- claim: fig4-unit-counts
  asked: 2026-10-30
  question: Does the Figure 4 legend count each RS unit once per current intensity, so that the
    fractions of Figure 4 and its supplement are taken over unit x intensity? The claims file counts
    units once and lists only the highest and the medium intensity as readings, which leaves this
attempt.schema.json
claims.schema.json
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -i 's/^paper: doi:10.1016\/j.neuron.2023.08.005$/dandiset: "000458"\npaper: doi:10.1016\/j.neuron.2023.08.005/' questions/burman-2023.yaml; python -c "import yaml;d=yaml.safe_load(open('questions/burman-2023.yaml'));print(d.keys(), len(d['questions']))"
```

```
dict_keys(['dandiset', 'paper', 'questions']) 2
```

**Agent calls Bash**

```bash
cd  sed -n 20,32p attempts/burman-2023-01.yaml; grep -n "figs7-model-decoding" -A12 attempts/burman-2023-01.yaml | sed -n 1,14p; grep -n "methods_unavailable\|^- kind" attempts/burman-2023-01.yaml
```

```
runner:
    platform: GitHub Actions
    url: https://github.com/catalystneuro/encore/actions/runs/42760152737
inputs:
- what: 'The paper''s Neuropixels analysis code, burman_et_al_2023_neuropixel_data_analysis.py: the list
    of 17 sessions and the method details the claims file takes from it (stop_time, the area and waveform
    selection, the evoked rate of reading F2, entropy and synchrony). No data.'
  source: https://gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf at revision 43a13d89441b7f56e835e84fa5811d9567917daf
- what: The paper's network simulation, burman_et_al_2023_neuronal_network_simulation.py, transcribed
    in network.py and run 20 times to generate the data of the four model claims (data elsewhere).
  source: https://gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f at revision f6a05661c10051560aa381e334099efd8521617b
outcomes:
- claim: dataset-sessions-link
193:- claim: figs7-model-decoding
194-  outcome: reproduced
195-  notebook: network_model.ipynb
196:  output: claim:figs7-model-decoding
197-  notes: Mean decoding accuracy 0.9848 shunting against 0.9315 hyperpolarizing (chance 0.01). D1, paired
198-    t test of the 20 per-run accuracies, t = 16.92, p = 6.52e-13; D2, shunting higher in 20 of 20 runs.
199-  deviations:
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/burman-2023-01.yaml'; s=open(p).read()
def rep(old,new,count=1):
    global s
    n=s.count(old); assert n==count, (n, old[:60]); s=s.replace(old,new)
rep("""selection, the evoked rate of reading F2, entropy and synchrony). No data.'""",
"""selection, the evoked rate of reading F2, entropy and synchrony). No data. It is also fetched at this
    revision and run unmodified on the loaded data (npx.run_gist), as a check of npx.'""")
rep("""in network.py and run 20 times to generate the data of the four model claims (data elsewhere).""",
"""in network.py and run 20 times to generate the data of the four model claims (data elsewhere). It
    is also fetched at this revision and run unmodified on a small run (network.run_gist), as a check
    of the transcription.""")
# fig4c notes
rep("""    trials times 10 ms, a median 4.50 times the count rate, so its 200 Hz bound drops units whose spike-count
    rate exceeds about 45 Hz (kept units reach 54.2 Hz).""",
"""    trials times 10 ms, a median 4.50 times the count rate, so its 200 Hz bound drops units whose spike-count
    rate exceeds about 45 Hz (kept units reach 54.2 Hz). The gist itself, run unmodified on the loaded
    data, gives the same values as npx for all 865 units and, with the Methods' exclusion applied to its
    rate column, 662 kept and 203 excluded. Whether the claim should be judged under the gist's rate is
    asked of a reader (questions/burman-2023.yaml).""")
rep("""    all selected units (N6). Timed from start_time, 0.3073 against 0.3720.""",
"""    all selected units (N6). Timed from start_time, 0.3073 against 0.3720. The gist itself, run unmodified,
    gives 0.3253 and 0.3928 for its 662 kept units. Whether the claim should be judged under the gist's
    rate is asked of a reader (questions/burman-2023.yaml).""")
rep("""    1.324 and 1.104 there, so the paper's means are over units defined in both conditions, though it gives
    n = 662.""",
"""    1.324 and 1.104 there, so the paper's means are over units defined in both conditions, though it gives
    n = 662. The gist itself, run unmodified, gives 1.3474 and 1.1106 over the 597 such units. Whether
    the claim should be judged under the gist's rate is asked of a reader (questions/burman-2023.yaml).""")
rep("""    isoflurane over 721 units, paired t = 12.36 (p printed as 0, far below 0.05); higher awake""",
"""    isoflurane over 721 units, paired t = 12.36, p = 5.75e-32; higher awake""")
rep("""    partially reproduced. Per-run hyperpolarizing means span 0.8661 to 0.8909, so the tolerance (the paper's
    SEM over pooled neurons) is narrower than the spread between seeds, and the paper's seeds are not
    known.""",
"""    partially reproduced. Per-run hyperpolarizing means span 0.8661 to 0.8909, so the tolerance (the paper's
    SEM over pooled neurons) is narrower than the spread between seeds, and the paper's seeds are not
    known. The standard error of a 20-run mean from that spread is 0.0013 hyperpolarizing (0.0006 shunting),
    and the hyperpolarizing mean is 1.6 of these from 0.881 (the shunting mean 1.3 from 0.784). Whether
    the tolerance should allow for the spread between seeds is asked of a reader (questions/burman-2023.yaml).""")
rep("""    partially reproduced. Per-run hyperpolarizing means span 0.1798 to 0.2217, wider than the tolerance.""",
"""    partially reproduced. Per-run hyperpolarizing means span 0.1798 to 0.2217, wider than the tolerance.
    The standard error of a 20-run mean from that spread is 0.0023 hyperpolarizing (0.0014 shunting), and
    the hyperpolarizing mean is 1.9 of these from 0.197 (the shunting mean 0.4 from 0.451). Whether the
    tolerance should allow for the spread between seeds is asked of a reader (questions/burman-2023.yaml).""")
rep("t test of the 20 per-run accuracies, t = 16.92, p = 6.52e-13;", "t test of the 20 per-run accuracies, t = 16.42, p = 1.11e-12;")
rep("""  - The stimulus is held as one periodic 2,500 ms set instead of the gist's 4 GB whole-run array, to fit
    in memory; a small run with both gives identical spike trains (data check).""",
"""  - The stimulus is held as one periodic 2,500 ms set instead of the gist's 4 GB whole-run array, to fit
    in memory; a small run with both gives identical spike trains, and the gist itself run unmodified on
    that small run gives the same spikes and the same per-neuron rate, entropy and synchrony (data check).""", count=2)
old_f4 = s[s.index("- claim: figs4-intrinsic-properties"):]
old_f4 = old_f4[:old_f4.index("\n- claim:", 5)+1]
new_f4 = """- claim: figs4-intrinsic-properties
  outcome: blocked
  blocked_by: methods_underspecified
  notes: The claim rests on the paper's NEURON model of an L2/3 pyramidal neuron and a Matlab analysis
    of its simulated ramps (github.com/richardjburman/burman-et-al-2022---Awake-EGABAAR at commit a404c3e,
    hoc files and NEURON_Egaba_Analysis.m). The model is public and the Methods ("Simulating measurements
    of synaptic EGABAAR", Table 2) give its membrane properties per state, the synapses, the E_GABA values
    (-85 to -35 mV in 5 mV steps) and the ramp protocol, so the ramp estimates could be simulated under
    the anesthetized and awake properties. What is open is what they would be compared with. The measure
    Figure S4 shows and the comparison behind "could not be explained" are in the Figure S4 legend, which
    was not in the text read, and the claims file gives no criterion; a choice such as the estimation
    error under each state's properties against the measured difference of Figure 2H would be arbitrary.
    So the claim is blocked as methods_underspecified and was not simulated (a further obstacle, the
    analysis is Matlab, and NEURON is not in the entry's environment). The question is for the paper's
    authors (findings, methods_unavailable). Neither part uses the dandiset.
"""
s = s.replace(old_f4, new_f4)
s = s.rstrip('\n') + """
- kind: methods_unavailable
  statement: For the multi-compartment model of Figure S4 (figs4-intrinsic-properties), which measure of
    the simulated ramp estimates of synaptic E_GABAAR, under the anesthetized and awake membrane properties
    of Table 2, is compared with what, and what result shows that the membrane properties "could not
    explain" the measured difference? The Methods give the model and protocol; the comparison is only in
    the Figure S4 legend, not in the text this attempt read.
"""
open(p,'w').write(s)
EOF
grep -n "figs4-intrinsic" -A3 attempts/burman-2023-01.yaml | head; tail -8 attempts/burman-2023-01.yaml
```

```
222:- claim: figs4-intrinsic-properties
223-  outcome: blocked
224-  blocked_by: methods_underspecified
225-  notes: The claim rests on the paper's NEURON model of an L2/3 pyramidal neuron and a Matlab analysis
--
428:  statement: For the multi-compartment model of Figure S4 (figs4-intrinsic-properties), which measure of
429-    the simulated ramp estimates of synaptic E_GABAAR, under the anesthetized and awake membrane properties
430-    of Table 2, is compared with what, and what result shows that the membrane properties "could not
431-    explain" the measured difference? The Methods give the model and protocol; the comparison is only in
    every unit whose location begins with the stimulated region. Neither difference changes the units
    selected in this dataset.
- kind: methods_unavailable
  statement: For the multi-compartment model of Figure S4 (figs4-intrinsic-properties), which measure of
    the simulated ramp estimates of synaptic E_GABAAR, under the anesthetized and awake membrane properties
    of Table 2, is compared with what, and what result shows that the membrane properties "could not
    explain" the measured difference? The Methods give the model and protocol; the comparison is only in
    the Figure S4 legend, not in the text this attempt read.
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/burman-2023-01.yaml'; s=open(p).read()
old="""    selected in this dataset.
- kind: methods_unavailable"""
assert old in s
# dataset-sessions-link note
o2="""    files, six with EEG only and sub-599017 with units and SSp stimulation, which the gist does not read."""
assert s.count(o2)==1
s=s.replace(o2, o2+"""
    The clock check covers all 17 files. In 33 of 34 file and condition pairs, spikes 2 to 12 ms after the
    pulse exceed those of the same window 1.5 s before and after it (1.5 to 39 times, Wilcoxon p below
    0.001); the exception is the awake trials of sub-569069_ses-20210312 (1.55 against 1.45 spikes per
    trial, p = 0.59), whose isoflurane trials, on the same file clock, pass (2.2 times, p = 2e-12).""")
patch = ["fig1b-perforation-rs", "fig1h-vu-egaba", "fig1i-vu-rmp", "fig1j-vu-df", "figs2-ramp-equals-step",
 "figs3-egaba-unrelated-amplitude-rs", "rm-awake-lower", "fig2c-vm-depolarized", "fig2d-subthreshold-fluctuation",
 "fig2f-response-polarity", "fig2h-egaba-depolarized", "fig2i-rmp-depolarized", "fig2j-df-depolarized",
 "fig2j-awake-df-zero", "fig2k-conductance-same", "figs5-within-anesthetized", "rm-nbqx-higher", "fig3c-nbqx-vm",
 "fig3d-nbqx-fluctuation", "fig3e-nbqx-polarity", "fig3g-nbqx-egaba", "fig3h-nbqx-rmp", "fig3i-nbqx-df",
 "fig3j-nbqx-conductance-same"]
v = """verifications:
- date: '2026-11-10'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebooks)
  reviewed: The first executed notebooks (reproduce_burman_2023.ipynb and network_model.ipynb) with the
    conclusion cells and the summaries removed, the helper modules npx.py and network.py and the claims
    file, with the paper's full text (PMC11913778). The verifier queried the archive through the DANDI
    API and tested npx.measures, npx.histogram and read_session on a synthetic two-unit, three-trial
    session. It had no attempt record and could not see the two gists.
  results:
  - claim: dataset-sessions-link
    agrees: true
    outcome: reproduced
    reason: All 17 gist sessions are assets of 0.230317.0039, each has every units and trials field,
      and each has both epochs; 16 subjects. The clock check uses off-pulse windows on only 2 of 17
      files and relies on the evoked-count contrast for the other 15 (B5).
    response: The shifted-window check now runs on all 17 files (read_session counts the shifted windows
      as it streams the spike trains) with a Wilcoxon test per file and condition; 33 of 34 pairs pass
      at p below 0.001, and the one that does not (sub-569069 awake) is named in the notebook and the
      notes. Outcome unchanged.
  - claim: fig4c-sample
    agrees: true
    outcome: partially_reproduced
    reason: Under A1F1, the Methods reading, 721 are kept (inside 662 +- 66.2) but 144 excluded (outside
      203 +- 20.3); under A1F2 every number matches the paper exactly (662/203, median 34, 1 to 93),
      strong evidence that the paper's numbers were made with the gist's summed-latency rate. The
      partial outcome reflects a bug in the paper's own code, not the data, and should be recorded as
      a deviation (B1, a point about the claims file). The verifier could not see the gist, so could
      not confirm that npx's F2 denominator and trial order match it.
    response: The gist is now run unmodified on the loaded data (npx.run_gist, a sanity cell); it gives
      the same rate, entropy and synchrony as npx for all 865 units, and 662 kept and 203 excluded. The
      deviation and the code_mismatch finding were already recorded. The question whether the claim
      should be judged under the gist's rate is added to questions/burman-2023.yaml for a reader. Outcome
      unchanged.
  - claim: fig4d-synchrony-lower-awake
    agrees: true
    outcome: partially_reproduced
    reason: Under A1F1 awake 0.3188 is just outside 0.320 to 0.330 and isoflurane 0.3862 is inside; awake
      is lower, p = 1.45e-32. A1F2 matches exactly (0.3253 / 0.3928). As for fig4c-sample, this reflects
      the paper's code (B1).
    response: The gist run unmodified gives 0.3253 and 0.3928; the question is in questions/burman-2023.yaml.
      The variant table's p values, which printed as 0.00e+00 because they were rounded before formatting
      (B4), are now formatted first. Outcome unchanged.
  - claim: fig4d-entropy-higher-awake
    agrees: true
    outcome: partially_reproduced
    reason: Under A1F1 awake 1.3887 and isoflurane 1.1502 are both outside tolerance; awake is higher,
      p = 3.3e-30, n = 656. A1F2 matches exactly (1.3474 / 1.1106). As for fig4c-sample (B1).
    response: The gist run unmodified gives 1.3474 and 1.1106; the question is in questions/burman-2023.yaml.
      Outcome unchanged.
  - claim: fig4-rate-higher-awake
    agrees: true
    outcome: reproduced
    reason: Under A1F1, 14.0 Hz awake against 7.59 Hz isoflurane, paired t = 12.4, p far below 0.05;
      holds under every reading, and 15 of 17 recordings go the same way. The p values print as 0.00e+00
      because they are rounded before formatting (B4).
    response: The p values are now formatted before rounding (A1F1 p = 5.75e-32), in the notebook and
      the notes. Outcome unchanged.
  - claim: figs6-rate-regressed
    agrees: true
    outcome: reproduced
    reason: Under A1F1 synchrony is negative and entropy positive under R1, R2 and R3, all p < 1e-10,
      and the same under every variant. The Figure S6 legend was not available, so it could not see
      which regression the paper used.
    response: No change.
  - claim: fig4f-model-hyperpolarizing-less-activity
    agrees: true
    outcome: reproduced
    reason: 8.785 Hz hyperpolarizing against 19.468 Hz shunting, paired p about 0; lower in 20 of 20 runs.
      network.py is checked only against its own whole-run-stimulus mode, not against the gist, and that
      Brian 2 rereads eta from the mutated namespace is supported only indirectly by the summed weights.
    response: The gist is now run unmodified on the small run with the same seed (network.run_gist, a
      sanity cell); it gives the same 19,093 excitatory spikes and the same per-neuron rate, entropy and
      synchrony for all 800 neurons. Each full run now records eta from the plastic synapses' compiled
      code after each run, 0.1 for balancing and 0 for the test in all 20. Outcome unchanged.
  - claim: fig4h-model-synchrony
    agrees: true
    outcome: partially_reproduced
    reason: Shunting 0.7833 is inside tolerance; hyperpolarizing 0.8789 is outside (0.880 to 0.882);
      shunting is lower, p about 0, in 20 of 20 runs. The tolerance, the paper's SEM over 16,000 pooled
      neurons, is too tight for runs with different seeds; the run-to-run SE of a 20-run mean is 0.0013,
      and the miss is 1.6 of these, so the partial outcome comes from the criterion, not the model (B2,
      a point about the claims file).
    response: The notebook now prints the run-to-run SE of the 20-run mean and each mean's distance from
      the paper's value in units of it (hyperpolarizing 0.0013, 1.6 SE). The question whether the
      tolerance should allow for seed noise is added to questions/burman-2023.yaml. Outcome unchanged.
  - claim: fig4h-model-entropy
    agrees: true
    outcome: partially_reproduced
    reason: Shunting 0.4516 is inside tolerance; hyperpolarizing 0.2014 is outside (0.195 to 0.199);
      shunting is higher, p about 0, in 20 of 20 runs. The run-to-run SE is 0.0023 and the miss is 1.9
      of these, seed noise (B2).
    response: As for fig4h-model-synchrony (hyperpolarizing SE 0.0023, 1.9 SE); the question is in
      questions/burman-2023.yaml. Outcome unchanged.
  - claim: figs7-model-decoding
    agrees: true
    outcome: reproduced
    reason: Accuracy 0.985 shunting against 0.932 hyperpolarizing. D1 p = 1.1e-12; D2 higher in 20 of
      20 runs. Chance is 0.01 (100 patterns). The Figure S7 legend was not available to see the paper's
      test.
    response: The notes gave t = 16.92 and p = 6.52e-13, which did not match the notebook; they now give
      the printed t = 16.42, p = 1.11e-12. Outcome unchanged.
  - claim: figs4-intrinsic-properties
    agrees: true
    outcome: blocked
    reason: The measure and test are only in the Figure S4 legend, which was not supplied. The notebook
      gives the reason as other; methods_underspecified fits better. The NEURON model (commit a404c3e)
      is linked, so a qualitative partial test may have been possible, and the notebook neither attempts
      nor argues against simulating ramp E_GABA estimates under anesthetized and awake membrane
      properties (B3).
    response: blocked_by changed from other to methods_underspecified. The notebook header and the notes
      now say that the model and its parameters are public and why it is not simulated (the comparison
      that would judge it is only in the unread legend, and the claims file gives no criterion), and a
      methods_unavailable finding asks the paper's authors.
"""
for c in patch:
    v += f"""  - claim: {c}
    agrees: true
    outcome: blocked
    reason: The version has 24 assets, all behavior+ecephys NWB files holding Units, ElectricalSeries, LFP
      and behavior, with no intracellular recordings; a DANDI search for Burman, Akerman and gramicidin
      returns no dandiset. No part can be tested (data_missing).
    response: No change.
"""
s = s.rstrip('\n') + '\n' + v
open(p,'w').write(s)
EOF
python tools/entry.py check entries/burman-2023 2>&1 | grep -v MissingID | tail -5
```

```
0 error(s)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
for p in ('attempts/burman-2023-01.yaml','questions/burman-2023.yaml'):
    d=yaml.safe_load(open(p))
    def walk(x, path=''):
        if isinstance(x, dict):
            for k,v in x.items(): walk(v, path+'.'+str(k))
        elif isinstance(x, list):
            for i,v in enumerate(x): walk(v, path+f'[{i}]')
        elif isinstance(x, str) and (': ' in x or '—' in x or 'rather' in x.lower()):
            print(p, path, x[:100])
    walk(d)
EOF
grep -n "—\|rather" README.md entries/burman-2023/*.ipynb entries/burman-2023/*.py | head
```

```
attempts/burman-2023-01.yaml .inputs[0].what The paper's Neuropixels analysis code, burman_et_al_2023_neuropixel_data_analysis.py: the list of 17
questions/burman-2023.yaml .questions[0].question The opening comment (N7) judges every Neuropixels claim under the Methods reading of the evoked rate
```

**Agent**

Record, questions file and notebooks are updated; re-running the entry so the executed copies carry the final text.

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/burman-2023 2>&1 | grep -v MissingID | tail -4; date -u
```

```
Tue Nov 10 09:37:46 UTC 2026
Installed kernelspec registry-burman-2023 in executed/burman-2023/.venv/share/jupyter/kernels/registry-burman-2023
0 error(s)
pass  reproduce_burman_2023.ipynb  (142 s)
pass  network_model.ipynb  (949 s)
Tue Nov 10 09:56:07 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/burman-2023 && python - <<'EOF'
import json, re
for nb in ('network_model.ipynb','reproduce_burman_2023.ipynb'):
    d=json.load(open(nb))
    for i,c in enumerate(d['cells']):
        if c['cell_type']!='code': continue
        out=''.join(''.join(o.get('text','')) for o in c['outputs'] if o.get('output_type')=='stream')
        for pat in ('D1 paired','run-to-run','eta in','identical spike','values differing','662 kept','conditions with evoked','A1F1 unrounded','units with a higher awake','Synchrony of the kept','Entropy \\[nats\\] of'):
            for line in out.splitlines():
                if re.search(pat, line): print(nb[:8], i, line[:200])
EOF
```

```
network_ 3 identical spike trains: True
network_ 5 identical spike trains: True
network_ 6 eta in the plastic synapses' compiled code (pre, post), balancing run / test run: ['[[0.1, 0.1], [0.0, 0.0]]']
network_ 10 shunting: run-to-run SE of the mean 0.0006; pooled mean 0.7833 is 1.3 SE from 0.784
network_ 10 hyperpolarizing: run-to-run SE of the mean 0.0013; pooled mean 0.8789 is 1.6 SE from 0.881
network_ 13 shunting: run-to-run SE of the mean 0.0014; pooled mean 0.4516 is 0.4 SE from 0.451
network_ 13 hyperpolarizing: run-to-run SE of the mean 0.0023; pooled mean 0.2014 is 1.9 SE from 0.197
network_ 19 D1 paired t = 16.42, p = 1.11e-12
reproduc 8 conditions with evoked above shifted at p < 0.001: 33 of 34
reproduc 13 units in the gist's tables: 865 | matched to npx by id: 865 | values differing (relative tolerance 1e-8): 0
reproduc 13 the Methods' exclusion applied to the gist's rate column: 662 kept, 203 excluded
reproduc 13 Synchrony of the kept units from the gist's table: awake 0.3253, isoflurane 0.3928 (n = 662)
reproduc 13 Entropy [nats] of the kept units from the gist's table: awake 1.3474, isoflurane 1.1106 (n = 597)
reproduc 23 A1F1 unrounded: awake 0.31885, isoflurane 0.38624, p = 1.45e-32
reproduc 31 units with a higher awake rate: 539 of 721
```

**Agent calls Bash**

```bash
cd entries/burman-2023 && sed -i 's/  runtime_minutes: 33/  runtime_minutes: 18/' entry.yaml && sed -i 's/on four processes, about 35 minutes./on four processes, about 20 minutes./' README.md && grep -n "runtime\|minutes" entry.yaml README.md && cd ../.. && python tools/entry.py check entries/burman-2023 2>&1 | tail -1 && git status --short
```

```
entry.yaml:15:  runtime_minutes: 3
entry.yaml:18:  runtime_minutes: 18
README.md:35:- `reproduce_burman_2023.ipynb`: the Neuropixels claims. About two minutes, most of it streaming the
README.md:37:- `network_model.ipynb`: 20 runs of the paper's network model on four processes, about 20 minutes.
0 error(s)
 M attempts/burman-2023-01.yaml
 M entries/burman-2023/README.md
 M entries/burman-2023/entry.yaml
 M entries/burman-2023/network.py
 M entries/burman-2023/network_model.ipynb
 M entries/burman-2023/npx.py
 M entries/burman-2023/reproduce_burman_2023.ipynb
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
[... 4 more lines not kept]
```

**Agent**

No outcome changed. Every outcome the verifier gave is kept except one: figs4-intrinsic-properties stays blocked, but its reason changes from `other` to `methods_underspecified`, as the verifier suggested. The entry re-ran cleanly with `tools/entry.py all`: check 0 errors, the Neuropixels notebook passed in 142 s and the model notebook in 949 s. The printed numbers match the conclusions and the attempt record.

**What I changed, point by point**
- **B1 (partial outcomes come from the paper's own rate code):** this is a point about the claims file, so I added it as a question for a reader in the new `questions/burman-2023.yaml`. The three claims stay partially reproduced. I also settled the verifier's first open check: the paper's analysis gist now runs unmodified on the loaded data. It agrees with `npx` for all 865 units (0 values differ), and with the Methods' exclusion applied to its rate it gives the paper's numbers exactly: 662 kept, 203 excluded, synchrony 0.3253 and 0.3928, entropy 1.3474 and 1.1106.
- **B2 (model tolerances too tight for different seeds):** added as a second question for a reader. The model notebook now prints the run-to-run standard error of the 20-run mean: 0.0013 for synchrony and 0.0023 for entropy in the hyperpolarizing condition. The misses are 1.6 and 1.9 of these. Both claims stay partially reproduced.
- **B3 (figs4):** the notebook header and the notes now say the NEURON model and its parameters are public. They also say why I did not simulate it: what the result would be judged against is only in the Figure S4 legend, which wasn't in the text read, and the claims file gives no criterion. I added a `methods_unavailable` finding asking the paper's authors.
- **B4 (p-values printing as 0):** p is now formatted before rounding. The rate test shows p = 5.75e-32.
- **B5 (clock check on only 2 of 17 files):** it now covers all 17 files, with a Wilcoxon test for each file and condition. 33 of 34 pairs pass at p < 0.001. The exception is the awake trials of sub-569069_ses-20210312 (p = 0.59), where the units barely respond while awake; that file's isoflurane trials pass. This is now in the notes.
- **Simulation gist:** the gist, run unmodified on a small network with the same seed, gives the same 19,093 spikes as `network.py`. It also gives the same rate, entropy and synchrony for all 800 neurons.
- **Brian 2 learning rate:** each run now prints the value used in the compiled synapse code. In all 20 runs it is 0.1 during balancing and 0 during the test.

**Corrected**
- The decoding claim's notes said t = 16.92, p = 6.52e-13, which did not match the notebook's output. They now give the printed t = 16.42, p = 1.11e-12.
- The model notebook's runtime in `entry.yaml` and the README is updated to about 20 minutes.

The round is recorded under `verifications` for all 35 claims, with the verifier's reasons and my response to each.

**Not done**
- I did not simulate the Figure S4 model, for the reason above.
- I did not change the claims file, which the instructions forbid; B1 and B2 wait for a reader's answer.
- Nothing is committed.

## End of run

64 turns, 54 minutes, $3.66 at API prices, result: success.
