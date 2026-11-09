# 001791 · claims-check · run 39559379172

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001791/ paper/ | head -50; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; cat claims/001791/*.yaml; python tools/claims_check.py claims/001791/10.1101-2023.05.25.542363.yaml paper/10.1101-2023.05.25.542363.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/da3dfd81-7ee1-4d9a-ba68-8cbed4e62e37/tool-results/b5no3qwz5.txt"
}
```

```
1	   - `expected`: each reported number the claim rests on, with a tolerance.
2	     Use the paper's own uncertainty when it gives one (a confidence
3	     interval, or the stated spread); otherwise 10% of the reported value.
4	     For a reported range ("2 to 13%"), the claim holds inside the range
5	     widened by 10% of each bound. Give the reason for any other tolerance.
6	   - `criterion`: how the claim will be judged, for any claim that is not
7	     settled by its expected values alone ("similar", "many", "tended to").
8	     It is written from the paper alone, before anyone analyses the data.
9	   - When a reported number can be read in more than one way (which trials
10	     form the denominator, which subset is meant), list in the criterion the
11	     readings the paper's text plausibly allows, before the analysis. The
12	     claim is reproduced if the result matches under any of them. The
13	     notebook shows every reading, the notes say which ones match, and the
14	     ambiguity is recorded as a deviation.
15	   - Methods come from the paper, never from the author. Every part of a
16	     criterion's method (the selection, the measure, the test, windows,
17	     bins, thresholds, what a measure is compared with) is taken from the
18	     Methods, the figure legends, the supplement, or the code the paper
19	     links, and the criterion says which. Search all of them before
20	     treating a detail as open.
[... 475 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/da3dfd81-7ee1-4d9a-ba68-8cbed4e62e37/tool-results/bihh0fg41.txt"
}
```

```
1	64260 paper/10.1101-2023.05.25.542363.txt
2	DOI: 10.1101/2023.05.25.542363
3	Version: preprint, version 1
4	Source: bioRxiv JATS XML (api.biorxiv.org)
5	Stored: 2026-10-20
6	Extracted: JATS XML flattened
7	------------------------------------------------------------------------
8	Voltage dynamics of dendritic integration and back-propagation in vivo
9	
10	## Abstract
11	
12	Neurons integrate synaptic inputs within their dendrites and produce spiking outputs, which then propagate down the axon and back into the dendrites where they contribute to plasticity. Mapping the voltage dynamics in dendritic arbors of live animals is crucial for understanding neuronal computation and plasticity rules. Here we combine patterned channelrhodopsin activation with dual-plane structured illumination voltage imaging, for simultaneous perturbation and monitoring of dendritic and somatic voltage in Layer 2/3 pyramidal neurons in anesthetized and awake mice. We examined the integration of synaptic inputs and compared the dynamics of optogenetically evoked, spontaneous, and sensory-evoked back-propagating action potentials (bAPs). Our measurements revealed a broadly shared membrane voltage throughout the dendritic arbor, and few signatures of electrical compartmentalization among synaptic inputs. However, we observed spike rate acceleration-dependent propagation of bAPs into distal dendrites. We propose that this dendritic filtering of bAPs may play a critical role in activity-dependent plasticity.
13	
14	## Introduction
15	
16	Neuronal information processing is governed by a complex interplay among diverse voltage-dependent ion channels distributed throughout the dendritic tree, soma, and axon 1 , 2 , 3 , 4 . Dendrites perform two qualitatively distinct information-processing tasks: they integrate synaptic inputs to determine spike times; and they integrate spikes and synaptic inputs to mediate synaptic plasticity 5 . Broadly, these processes involve information flow in opposite direc
[... 264 more lines not kept]
```

**Agent**

Checker passes (18 claims, 0 problems). Now checking the protocol on readings and the schema before editing.

**Agent calls Bash**

```bash
grep -n "any of them\|under one reading\|all give\|methods_underspecified" docs/*.md | head -20; ls tools; grep -n "statistics\|'p'\|\"p\"\|required" tools/claims_check.py | head -40; grep -l "checks:" claims/*/*.yaml | head -3
```

```
docs/design.md:65:    `data_missing`, `metadata_insufficient`, `methods_underspecified`,
docs/pilot-notes.md:175:  `methods_underspecified` may describe this better than `not_reproduced`.
docs/pilot-notes.md:218:   cell-count claims became `blocked`, `methods_underspecified`.
docs/pilot-notes.md:230:  differ, and the outcome is `blocked` with `methods_underspecified` even
docs/pilot-notes.md:380:  beforehand, a match under any of them counts as reproduced, and the
docs/pilot-notes.md:835:blocked as `methods_underspecified`. The decoding claims with the paper's
docs/pilot-notes.md:1077:17 claims are blocked as `methods_underspecified`, because the response
docs/pilot-notes.md:1205:Awake epochs. Six claims are blocked as `methods_underspecified`, because
docs/pilot-notes.md:1254:`methods_underspecified` though that reason is defined for a procedure
docs/pilot-notes.md:1354:`methods_underspecified`, because the fixed test calls 56.1% of cells
docs/pilot-notes.md:1469:tolerance under one reading and states no partial case; the author changed it
docs/pilot-notes.md:1600:`methods_underspecified`, because the calibration the verifier asked for
docs/pilot-notes.md:1918:`methods_underspecified`, the maze rotation of Figure S6 as
docs/pilot-notes.md:1998:`methods_underspecified`, and the model and two per-session claims, which have
docs/pilot-notes.md:2245:`methods_underspecified`. Some outcomes rest on weak ground:
docs/pilot-notes.md:2316:`fig2dg-nmf-components` to `methods_underspecified` and `fig1k`, `fig1f`,
docs/pilot-notes.md:2327:`methods_underspecified`, the L-MO and NE-MO claims, the probe, replay and
docs/pilot-notes.md:2416:`data_missing`; the two single-cell claims as `methods_underspecified`,
docs/pilot-notes.md:2499:`methods_underspecified`, and found a bug in the running rate, where a
docs/pilot-notes.md:2516:`methods_underspecified`, since the Methods' connection test as implemented
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 370,390p docs/pilot-notes.md; sed -n 222,235p docs/pilot-notes.md; ls schemas 2>/dev/null; grep -rn "statistics" schemas/*.json 2>/dev/null | head; grep -n -A12 '"statistics"' schemas/claims*.json 2>/dev/null | head -50
```

```
recorded. The Methods decide the main result and the code's choice is shown
  as a variant when they disagree (000207 notes; 000147 point 12).
- **Outside inputs** are allowed only when the paper itself compares with
  them, they are public and pinned, and they are listed under a new `inputs`
  field (000147 points 1 and 2).
- **Tolerances** default to the paper's own uncertainty, else 10% of the
  value, and `expected` may hold several numbers (000207 notes).
- **Criteria** are written before each claim's analysis, after the data check
  if need be, with what had been seen stated (000207 notes).
- **Several readings** of a number: the criterion lists the plausible readings
  beforehand, a match under any of them counts as reproduced, and the
  notebook shows all of them (000147 point 3). Decided after review: being
  generous here is preferred to letting the paper's wording turn a result
  into a partial one.
- **Claims of absence** are judged by the paper's own test (000147 point 5).
- **Criterion against statement**: the criterion decides; the notes say
  whether the rest of the statement holds (000147 point 4).
- **Dependent claims** are declared with `depends_on` and inherit a blocking
  reason (000207 notes).
- **Blocking categories** are defined, with one main reason and others in
[... 32 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A40 '"statistic": {' schemas/claims.schema.json | head -60; grep -n -B2 -A20 '"checks"' schemas/claims.schema.json | head -50
```

```
268:    "statistic": {
269-      "type": "object",
270-      "additionalProperties": false,
271-      "anyOf": [
272-        {
273-          "required": [
274-            "p"
275-          ]
276-        },
277-        {
278-          "required": [
279-            "ci"
280-          ]
281-        }
282-      ],
283-      "properties": {
284-        "about": {
285-          "description": "What the test compares or the interval bounds, when the claim has more than one, e.g. 'GPi against VLa onset times'.",
286-          "type": "string"
287-        },
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 60,140p tools/claims_check.py; grep -n -B3 -A8 "ci:" claims/*/*.yaml | grep -B3 -A8 "±" | head -30
```

```
return False


def printed_forms(v: float) -> set[str]:
    """Ways a paper prints a number: 0.002, .002, 2 × 10-5, 2e-5, 0.00002, 10-10."""
    out = {f"{v:g}", f"{v:g}".lstrip("0") if abs(v) < 1 else f"{v:g}"}
    if 0 < abs(v) < 1:
        m, e = f"{v:.3e}".split("e")
        m, e = f"{float(m):g}", str(int(e))
        out |= {f"{m}×10{e}", f"{m} × 10{e}", f"{m} x 10{e}", f"{m}x10{e}", f"{m}e{e}"}
        if m == "1":
            out.add(f"10{e}")
    if 0 < abs(v) < 0.001:
        plain = f"{v:.12f}".rstrip("0")
        out |= {plain, plain.lstrip("0")}
    return {f.lower() for f in out}


def check(claims_path: Path, paper_paths: list[Path]) -> int:
    doc = yaml.safe_load(claims_path.read_text())
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn -B6 -A4 "ci:" claims/*/*.yaml | grep -i -B6 -A4 "±\|level" | head -60
```

```
claims/000006/10.1038-s41586-018-0642-9.yaml-635-  source: Results, Movement commands, paragraph 2; Fig. 6c legend; Methods, Videography
claims/000006/10.1038-s41586-018-0642-9.yaml-636-  quote: "The onset of the first detectable movement occurred approximately 50 ms after the go cue onset (99%
claims/000006/10.1038-s41586-018-0642-9.yaml-637-    confidence interval: 38–56 ms)."
claims/000006/10.1038-s41586-018-0642-9.yaml-638-  statistics:
claims/000006/10.1038-s41586-018-0642-9.yaml-639-  - test: bootstrap of session means across mice and sessions
claims/000006/10.1038-s41586-018-0642-9.yaml:640:    ci:
claims/000006/10.1038-s41586-018-0642-9.yaml-641-      level: 0.99
claims/000006/10.1038-s41586-018-0642-9.yaml-642-      low: 38
claims/000006/10.1038-s41586-018-0642-9.yaml-643-      high: 56
claims/000006/10.1038-s41586-018-0642-9.yaml-644-      unit: ms
--
--
claims/000041/10.1016-j.neuron.2016.03.036.yaml-170-  - about: correlation of nonREM and WAKE rates
claims/000041/10.1016-j.neuron.2016.03.036.yaml-171-    statistic: R = 0.82
claims/000041/10.1016-j.neuron.2016.03.036.yaml-172-    p: 1.0e-10
claims/000041/10.1016-j.neuron.2016.03.036.yaml-173-    p_relation: "<"
claims/000041/10.1016-j.neuron.2016.03.036.yaml-174-  - about: slope of the nonREM against WAKE rate relation
claims/000041/10.1016-j.neuron.2016.03.036.yaml:175:    ci:
claims/000041/10.1016-j.neuron.2016.03.036.yaml-176-      level: 0.95
claims/000041/10.1016-j.neuron.2016.03.036.yaml-177-      low: 0.66
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn "claims_check" .github tools docs | grep -v "^tools/claims_check.py" | head
```

```
docs/agents/claims-check.md:5:1. Run `python tools/claims_check.py claims/{folder}/<file>.yaml paper/<text>.txt`: it validates the file and checks every quote word for word and every recorded p-value and interval against the text.
docs/agents/answer.md:5:For each question not yet answered: find the answer in the Methods, legends, supplement or the paper's code. Where the paper gives it, put it into the claim's criterion, with the source, and quote the passage briefly in the question's `answer`. Where the paper does not give it, say so in `answer`, and name in the criterion the readings the paper allows. Set `answered: {date}` on each question. Do not change a claim's statement or expected values unless the question shows they are wrong about the paper; then say so in the answer. Check quotes with `python tools/claims_check.py`.
docs/agents/claims.md:7:Write the claims file as steps 1 to 4 of the Reader section say. Every part of every criterion's method comes from the paper or its code, cited; a detail none of them fixes is named as open, with the readings the paper allows. Check every quote with `python tools/claims_check.py claims/{folder}/<file>.yaml paper/<text>.txt` and fix the quote, never the checker. Do not commit or push: the workflow commits your changes. Only files under `claims/{folder}/` are kept.
docs/protocol.md:154:quote is word for word (the quote checker, `tools/claims_check.py`, does this
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001791/10.1101-2023.05.25.542363.yaml",
 "old_string": "    (95% C.I., n = 30 recording sites, 5 neurons, 5 mice, Fig. 2e ).\n  expected:",
 "new_string": "    (95% C.I., n = 30 recording sites, 5 neurons, 5 mice, Fig. 2e ).\n  statistics:\n  - about: contour distance at which bAP amplitude falls to 50%, printed as 242 ± 30 μm\n    ci:\n      level: 0.95\n      low: 212\n      high: 272\n      unit: μm\n    n: 30 recording sites, 5 neurons, 5 mice\n  expected:"
}
```

```
The file claims/001791/10.1101-2023.05.25.542363.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001791/10.1101-2023.05.25.542363.yaml",
 "old_string": "    mice), consistent with prior theoretical predictions\n  expected:",
 "new_string": "    mice), consistent with prior theoretical predictions\n  statistics:\n  - about: bAP conduction speed beyond 50 μm, printed as 0.09 ± 0.02 m/s\n    ci:\n      level: 0.95\n      low: 0.07\n      high: 0.11\n      unit: m/s\n    n: 30 recording sites, 5 neurons, 5 mice\n  expected:"
}
```

```
The file claims/001791/10.1101-2023.05.25.542363.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001791/10.1101-2023.05.25.542363.yaml",
 "old_string": "  criterion: Tolerance 0, as the number is a count of trials. A trial is one strong\n    dendrite-targeted stimulus with soma and dendrite recorded. The paper gives no detection\n    rule for spikes or dendritic spikes; readings for an event, (a) a peak above 5 and (b) above\n    4 robust s.d. of the trace, the standard choices used in fig1d-light-intensity-spike-rate.\n    Reproduced when, under one reading, 40 trials are found and 1 to 3 of them have a dendritic\n    event with no somatic spike within 10 ms before it; the exact count is reported.",
 "new_string": "  criterion: Tolerance 0, since the 10% default (0.2 trials) admits no count but 2. A trial is\n    one strong dendrite-targeted stimulus with soma and dendrite recorded (anesthetized). The\n    paper does not say what the 40 trials are; readings, (i) all strong dendrite-targeted\n    stimuli, including those that evoked only subthreshold events (Fig. S11e), and (ii) only the\n    trials in which a spike was detected at the soma or the dendrite. The paper gives no\n    detection rule for spikes or dendritic spikes; readings for an event, (a) a peak above 5 and\n    (b) above 4 robust s.d. of the trace, the standard choices used in\n    fig1d-light-intensity-spike-rate. A dendritic spike with no somatic spike is one with no\n    somatic spike in the 10 ms before it (a window not in the paper). Reproduced when, under one\n    reading, 40 trials are found, exactly 2 of them have a dendritic spike with no somatic spike,\n    and in most trials with a dendritic spike a somatic spike precedes it (\"usually\"); the counts\n    of every reading are reported."
}
```

```
The file claims/001791/10.1101-2023.05.25.542363.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001791/10.1101-2023.05.25.542363.yaml",
 "old_string": "    paired over the 10 branches. The bAP amplitude window is that of fig4bc-doublet-first-fails,\n    both readings. Reproduced when, under every reading, accelerating trios show third >\n    second and decelerating trios third < second (or, in (b), accelerating ratio above\n    decelerating), at p < 0.05 by the Wilcoxon signed-rank test (the conventional threshold).",
 "new_string": "    paired over the 10 branches; (c) as the Methods word it (\"The amplitude of the third spike\n    in each triplet was determined and was classified\"), the normalized third-spike amplitude in\n    each class against the per-compartment mean of 1, by signed-rank test. The bAP amplitude\n    window is that of fig4bc-doublet-first-fails, both readings. Reproduced when, under every\n    reading, accelerating trios show third > second and decelerating trios third < second (in\n    (b), accelerating ratio above decelerating; in (c), accelerating third above 1 and\n    decelerating third below 1), at p < 0.05 by the Wilcoxon signed-rank test (the conventional\n    threshold)."
}
```

```
The file claims/001791/10.1101-2023.05.25.542363.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001791/10.1101-2023.05.25.542363.yaml",
 "old_string": "  criterion: The paper reports no test. For the sustained-pulse recordings, bAP amplitudes\n    normalized per dendrite by the mean bAP amplitude 200 to 400 ms after stimulus onset\n    (Methods, Analysis of bAP failures during optogenetic stimulation). Reproduced when, in\n    electrotonically distal dendrites (delay > 3 ms, Methods), the median normalized amplitude\n    of the first bAP of each train is below that of the second and later bAPs in the first\n    150 ms, and below 1, with the windows of fig4bc-doublet-first-fails.",
 "new_string": "  criterion: The paper reports no test. Fig. 4g shows one neuron (n = 10 trials); the claim is\n    tested over all sustained-pulse recordings (16 trials, 7 neurons, Fig. 4h legend), and for\n    the Fig. 4g neuron alone where it can be identified. The statement compares the dendrite with\n    the soma, which the Methods' normalization does not; readings, (a) bAP amplitudes normalized\n    per dendrite by the mean bAP amplitude 200 to 400 ms after stimulus onset (Methods, Analysis\n    of bAP failures during optogenetic stimulation); (b) per spike, the dendritic bAP amplitude\n    divided by the somatic spike amplitude of the same spike, normalized by the same ratio's\n    200 to 400 ms mean. Reproduced when, under both readings, in electrotonically distal\n    dendrites (delay > 3 ms, Methods), the median normalized value of the first bAP of each\n    train is below that of the second and later bAPs in the first 150 ms (a window not in the\n    paper, the end of the Results' 50 to 150 ms window), and below 1, with the windows of\n    fig4bc-doublet-first-fails."
}
```

```
The file claims/001791/10.1101-2023.05.25.542363.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001791/10.1101-2023.05.25.542363.yaml",
 "old_string": "    mean of the subsequent bAPs of the burst in the average and in at least 9 of the 13 trials,\n    and no dendritic event (spike detection as in fig1d) precedes the first somatic spike.",
 "new_string": "    mean of the subsequent bAPs of the burst in the average and in at least 9 of the 13 trials\n    (a bound not in the paper, for \"typically\"), and every dendritic spike detected in the\n    air-puff trials (spike detection as in fig1d, both readings) follows a somatic spike within\n    the bAP windows of fig4bc-doublet-first-fails (\"all detected dendritic spikes initiating as\n    bAPs from the soma\")."
}
```

```
The file claims/001791/10.1101-2023.05.25.542363.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cat >> claims/001791/10.1101-2023.05.25.542363.yaml <<'EOF'
- id: figs12-spontaneous-failures-both-states
  statement: During spontaneous activity, bAP failures occur in both anesthetized and awake
    recordings.
  source: Figure S12 legend
  quote: We observe bAP failures in both anesthetized and awake recordings.
  criterion: The paper reports no test and shows example traces only. Spontaneous recordings
    with soma and dendrite, split by state (anesthetized, awake). A failure is a somatic spike
    whose dendritic bAP amplitude, in the windows of fig4bc-doublet-first-fails, is below 2 s.d.
    of the dendrite's baseline noise (the failure reading (b) of fig2c-no-trial-variation; the
    paper gives no rule). Spike detection as in fig1d-light-intensity-spike-rate, both readings.
    Reproduced when, under every reading, failures are found in at least one recording of each
    state; their fraction per state is reported.
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2e-half-amplitude-distance, added the paper's 95% C.I. (242 ± 30 μm, as 212 to 272) under statistics, which the file had left out; the checker cannot find the bounds as printed since the paper prints them as ± 30, and they were confirmed by reading.
  - fig2f-conduction-speed, added the paper's 95% C.I. (0.09 ± 0.02 m/s, as 0.07 to 0.11) under statistics, for the same reason and with the same note.
  - figs11-dendritic-spikes-rare, the criterion accepted 1 to 3 trials while expected has tolerance 0; it now requires exactly 2, names the two readings of what the 40 trials are (all strong stimuli, Fig. S11e, or only those with a spike), marks the 10 ms window as not in the paper, and tests the "usually corresponded to bAPs" part of the statement, which it had left out.
  - fig4d-accelerating-amplifies, added reading (c), the Methods' wording (third-spike amplitude, normalized by the compartment mean, classified by trio type), since the Methods allow it and the paired quantity of the figure's signed-rank test is not stated.
  - fig4fg-opto-first-bap-attenuated, the statement says attenuated relative to the soma and the criterion did not compare with the soma; added reading (b), the dendrite to soma amplitude ratio, noted that Fig. 4g is one neuron (n = 10 trials), and marked the 150 ms window as not in the paper.
  - fig4ijk-sensory-first-fails, the criterion only checked that no dendritic event precedes the first somatic spike, while the paper says all detected dendritic spikes start as bAPs; it now requires every detected dendritic spike to follow a somatic spike, and marks 9 of 13 as a bound not in the paper.
  - figs12-spontaneous-failures-both-states, new claim; the Fig. S12 finding of spontaneous bAP failures in both states had no claim.
  - Open, fig2c-no-trial-variation, the paper says "at any of the recording sites" and gives no measure or test; the 90% of sites, 1.5 times and 10% bounds are not in the paper and the author must report the values with them.
  - Open, figs throughout, the spike detection thresholds (5 and 4 robust s.d.), the bAP amplitude windows (0 to 5 and 0 to 8 ms), and the bounds for "most" and "typically" (70% of branches, 9 of 13 trials) are not in the paper; they are named as readings or bounds in each criterion. No PDF was available, so the bins and p-values printed only in Figs. 3i, 4d and 4h remain open.
EOF
python tools/claims_check.py claims/001791/10.1101-2023.05.25.542363.yaml paper/10.1101-2023.05.25.542363.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/  - Open, figs throughout, the spike/  - Open, several claims, the spike/' claims/001791/10.1101-2023.05.25.542363.yaml && python tools/claims_check.py claims/001791/10.1101-2023.05.25.542363.yaml paper/10.1101-2023.05.25.542363.txt; grep -c "—\|rather" claims/001791/*.yaml; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file is ready for an attempt. I made seven changes to it and left two problems open, both recorded in the file.

**Checker result**
- Before my changes: `18 claims, 18 quotes, 0 statistical values, 0 problems`.
- After: `19 claims, 19 quotes, 4 statistical values, 2 problems`. The two problems are the lower bounds of the confidence intervals I added (212 μm and 0.07 m/s). The checker can't find them because the paper prints the intervals as "± 30" and "± 0.02". I confirmed both by reading. The schema validates and all quotes match word for word.

**Changes, by claim**
- **fig2e-half-amplitude-distance**: added the paper's 95% confidence interval for the 50% decay distance (242 ± 30 μm, recorded as 212 to 272) under `statistics`. The file had left it out.
- **fig2f-conduction-speed**: added the paper's 95% confidence interval for conduction speed (0.09 ± 0.02 m/s, recorded as 0.07 to 0.11) under `statistics`, for the same reason.
- **figs11-dendritic-spikes-rare**:
  - The criterion accepted 1 to 3 trials but the expected count had tolerance 0; it now requires exactly 2.
  - It names two readings of what the 40 trials are: all strong stimuli (Fig. S11e shows ones that evoked only subthreshold events), or only the trials with a spike.
  - It now tests the "usually corresponded to bAPs" part of the statement.
  - It says the 10 ms window is not in the paper.
- **fig4d-accelerating-amplifies**: added a third reading taken from the Methods' wording (the normalized amplitude of the third spike, compared with the compartment mean). The paper does not say which quantity its signed-rank test pairs.
- **fig4fg-opto-first-bap-attenuated**: the paper says the first bAP is attenuated "relative to the soma", but the criterion never compared with the soma. I added a reading based on the dendrite-to-soma amplitude ratio. I also noted that Fig. 4g shows one neuron (10 trials), and that the 150 ms window is not in the paper.
- **fig4ijk-sensory-first-fails**: the paper says all detected dendritic spikes start as bAPs from the soma. The criterion only checked the first spike; it now requires every detected dendritic spike to follow a somatic spike. I also marked "9 of 13 trials" as a bound the paper does not give.
- **figs12-spontaneous-failures-both-states** (new claim): the Fig. S12 finding, spontaneous bAP failures in both anesthetized and awake recordings, had no claim.

**What remains open**
- **fig2c-no-trial-variation**: the paper says "at any of the recording sites" but defines no measure or test. The bounds in the criterion (90% of sites, 1.5 times the baseline variation, failures under 10%) are not from the paper.
- **Several claims**: these parts are not in the paper; each criterion names them as readings or bounds:
  - the spike detection thresholds (5 and 4 robust standard deviations);
  - the bAP amplitude windows (0 to 5 and 0 to 8 ms);
  - the bounds standing in for "most" and "typically".
- **Figs. 3i, 4d and 4h**: no PDF was available, so the distance and time bins and the p-values printed only inside these figures could not be read.

All other claims match the paper. Every main finding has a claim, and none draws on another paper. Nothing was committed or pushed.

## End of run

20 turns, 3 minutes, result: success.
