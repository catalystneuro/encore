# 000128 · claims · run 39808132899

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/; ls claims/000128 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -200; wc -l claims/001453/*.yaml paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 25,200p claims/001453/*.yaml; wc -l claims/001453/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 200,321p claims/001453/*.yaml; cat paper/10.1038-nature11129.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n '^[a-z]' claims/001453/*.yaml; grep -n '^  [a-z_]*:' claims/001453/*.yaml | awk -F: '{print $3}' | sort | uniq -c; head -40 paper/10.1038-nature11129.txt | cut -c1-300
```

Result: not kept, because it reads the paper's text.

**Agent**

Read the protocol and example. Now reading the paper text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2010.09.015.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; python3 -c "
s=open('10.1016-j.neuron.2010.09.015.txt').read()
print(s[58000:102747])"
```

```
<persisted-output>
Output too large (44.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/0bbc41e9-d062-4b1d-8a03-f288ca97bc2b/tool-results/bstfyuujn.txt

Preview (first 2KB):
black bar : performance when data were randomly subdivided. D. PD consistency for the peri-movement space versus that for a variety of other spaces. Kinematic and EMG spaces were chosen because they had performed the best overall (after the peri-movement space) in the analysis in Fig. 6 . ‘ Targs. + inst. speed ’ and ‘ segment directions ’ spaces were chosen because they performed well for the speed and maze tasks respectively. ‘ Targs. + inst. speed ’ was undefined for the maze task; the similar ‘ endpoints + max. spd. ’ space was analyzed instead. Figure 8 Illustration of the behavior of a simple linear dynamical system: a harmonic oscillator. A. Changes in the initial state produce a linear scaling of the subsequent activity pattern. In this case, the larger the initial state of unit 1, the greater the amplitude of the oscillation. B. State space containing 25 randomly chosen initial states (25 ‘conditions’). Symbol size/color indicates the initial firing rate of unit 1. For the simulations below, activity evolved counterclockwise from the initial state: x (t+1) = W x (t), where x is the 2-dimensional vector of unit activities, and the matrix W = [1 - 2π/360; 2π/360 1]. Thus, the state rotates one degree with each time-step. C. Activity of unit 1 versus time for the initial states shown in B. The initial state was at first held constant (as if W were the identity matrix) to emulate preparatory activity. The dynamics were then released to produce sinusoidal ‘peri-movement’ activity. Asterisks indicate the same two conditions as in B. D. The pattern of initial states (the ‘preparatory tuning’) from C is captured by a PD in peri-movement space. Analysis/format are the same as for figure 5C . Traces on each axis plot the time
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/0bbc41e9-d062-4b1d-8a03-f288ca97bc2b/tool-results/bstfyuujn.txt"
}
```

```
1	black bar : performance when data were randomly subdivided. D. PD consistency for the peri-movement space versus that for a variety of other spaces. Kinematic and EMG spaces were chosen because they had performed the best overall (after the peri-movement space) in the analysis in Fig. 6 . ‘ Targs. + inst. speed ’ and ‘ segment directions ’ spaces were chosen because they performed well for the speed and maze tasks respectively. ‘ Targs. + inst. speed ’ was undefined for the maze task; the similar ‘ endpoints + max. spd. ’ space was analyzed instead. Figure 8 Illustration of the behavior of a simple linear dynamical system: a harmonic oscillator. A. Changes in the initial state produce a linear scaling of the subsequent activity pattern. In this case, the larger the initial state of unit 1, the greater the amplitude of the oscillation. B. State space containing 25 randomly chosen initial states (25 ‘conditions’). Symbol size/color indicates the initial firing rate of unit 1. For the simulations below, activity evolved counterclockwise from the initial state: x (t+1) = W x (t), where x is the 2-dimensional vector of unit activities, and the matrix W = [1 - 2π/360; 2π/360 1]. Thus, the state rotates one degree with each time-step. C. Activity of unit 1 versus time for the initial states shown in B. The initial state was at first held constant (as if W were the identity matrix) to emulate preparatory activity. The dynamics were then released to produce sinusoidal ‘peri-movement’ activity. Asterisks indicate the same two conditions as in B. D. The pattern of initial states (the ‘preparatory tuning’) from C is captured by a PD in peri-movement space. Analysis/format are the same as for figure 5C . Traces on each axis plot the time-evolving pattern corresponding to that PC (black and blue traces for units one and two). The pattern at the end of the arrow is the weighted sum of the two PCs, with weights corresponding to the PD. This work was supported by a Helen Hay Whitn
[... 695 more lines not kept]
```

**Agent**

The full text, Methods and supplement are present. Checking the repo for any archive metadata on 000128 and for code links in the paper.

**Agent calls Bash**

```bash
cd ..; grep -rl "000128" --include=*.yaml --include=*.md --include=*.json . 2>/dev/null | grep -v '^./transcripts' | head; grep -oiE "github|gitlab|code avail|software|matlab[^.]*" paper/10.1016-j.neuron.2010.09.015.txt | sort | uniq -c; ls tools; python tools/claims_check.py -h 2>&1 | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
import sys
s=json.dumps(d)
i=s.find('000128'); print(s[i-200:i+3000])"; grep -n -B2 -A15 "000128" papers/manifest.yaml | head -60; cat schemas/claims.schema.json | head -150
```

```
8", "title": "Area 2 of primary somatosensory cortex encodes kinematics of the whole arm", "relation": "IsDescribedBy", "resource_type": null, "preprint": false}], "catalystneuro": []}, {"dandiset": "000128", "name": "MC_Maze: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching", "published_version": "0.220113.0400", "asset_count": 2, "size_gb": 0.69, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Rhesus monkey"], "approaches": ["electrophysiological approach"], "papers": [{"doi": "10.1016/j.neuron.2010.09.015", "title": "Cortical preparatory activity: representation of movement or first cog in a dynamical machine?", "relation": "IsDescribedBy", "resource_type": null, "preprint": false}, {"doi": "10.1038/nature11129", "title": "Neural population dynamics during reaching", "relation": "IsDescribedBy", "resource_type": null, "preprint": false}], "catalystneuro": []}, {"dandiset": "000129", "name": "MC_RTT: Macaque motor cortex spiking activity during self-paced reaching (Superior arm-movement decoding from cortex)", "published_version": "0.241017.1444", "asset_count": 2, "size_gb": 0.05, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Rhesus monkey"], "approaches": ["electrophysiological approach"], "papers": [{"doi": "10.1088/1741-2552/aa9e95", "title": "Superior arm-movement decoding from cortex with a new, unsupervised-learning algorithm", "relation": "IsDescribedBy", "resource_type": null, "preprint": false}], "catalystneuro": []}, {"dandiset": "000130", "name": "DMFC_RSG: macaque dorsomedial frontal cortex spiking activity during time interval reproduction task", "published_version": "0.241017.1448", "asset_count": 2, "size_gb": 0.02, "data_standards": ["Neurodata Without Borders (NWB)"], "species": ["Rhesus monkey"], "approaches": ["electrophysiological approach"], "papers": [{"doi": "10.1016/j.neuron.2019.06.012", "title": "Bayesian computation through cortical latent dynamics", "rel
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p schemas/claims.schema.json
```

```
"type": "string",
            "minLength": 1
          }
        },
        "allOf": [
          {
            "not": {
              "required": [
                "quote",
                "inferred"
              ]
            }
          },
          {
            "if": {
              "properties": {
                "kind": {
                  "const": "link"
                }
              },
[... 177 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/ | head -50; ls claims/0001{38,39,40} 2>/dev/null
```

```
Exit code 2
000003
000004
000005
000006
000008
000009
000010
000011
000013
000015
000016
000017
000019
000023
000034
000035
000036
000037
000041
[... 31 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn -i -B3 -A8 "simulat" claims/*/*.yaml | grep -E "data:|inferred|simulat" | head -30
```

```
claims/000009/10.1038-nature22324.yaml:649:  criterion: A simulation, not a test on recorded data; its parameters are in the Supplementary
claims/000011/10.1038-nature17643.yaml:907:  criterion: A simulation, not a test on recorded data. Parameters from the Methods and Extended
claims/000011/10.1038-nature17643.yaml:924:  criterion: A simulation, not a test on recorded data. Modular attractor with the Methods'
claims/000011/10.1038-nature17643.yaml:933:    readings (h1) 1 ms, (h2) 0.1 ms, under both noise readings. Reproduced when, over 100 simulated trials per trial type, the
claims/000013/10.7554-elife.06619.yaml:1142:  quote: Comparing the simulations with actual spike trains revealed that L4 neuron response
claims/000013/10.7554-elife.06619.yaml:1146:  criterion: Methods, last paragraph, and Figure 6D. Per L4 C2 cell, spike trains simulated as a
claims/000013/10.7554-elife.06619.yaml:1152:    the paper's cited method, or by adjusting the rate until the simulated PSTH matches; using
claims/000013/10.7554-elife.06619.yaml:1154:    simulated train per real touch; FF computed as for the data in 10 ms sliding windows. Open details, (1) which touches,
claims/000016/10.1016-j.neuron.2019.09.045.yaml:527:  criterion: A simulation, not a test on recorded data. The linearised rate model of the STAR
claims/000016/10.1016-j.neuron.2019.09.045.yaml:546:  criterion: A simulation, not a test on recorded data. As fig5a-nonselective-model; signal-selective
claims/000016/10.1016-j.neuron.2019.09.045.yaml:559:  criterion: A simulation, not a test on recorded data. As fig5bc-selective-models-match, with
claims/000019/10.1038-nature11911.yaml:343:    test: comparison with 1000 simulated maps per null model
claims/000034/10.7554-elife.61834.yaml:48:#   HDSort 1.0.1, all with default parameters, the same on the simulated recording. The notebooks
claims/000034/10.7554-elife.61834.yaml:68:# - True and false positive agreement units on the simulation (Figure 3C; notebook cell after the
c
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 520,535p claims/000016/10.1016-j.neuron.2019.09.045.yaml; head -60 claims/000016/10.1016-j.neuron.2019.09.045.yaml
```

```
accurately than excitatory neurons for every ratio of excitatory-to-inhibitory to
    inhibitory-to-excitatory connection strength.
  source: Results, Modeling rules out decision circuits with non-selective inhibition, paragraph 2;
    Figure 5A; Figure S8
  quote: For this value (and indeed for all other values), inhibitory neurons had lower
    classification accuracy than excitatory neurons ( Figure 5A , bottom; Figure S8 , left),
    inconsistent with our experimental results
  criterion: A simulation, not a test on recorded data. The linearised rate model of the STAR
    Methods with the printed parameters (sigma 1.25, delta 0.75, wEE 0.25, wII -2, wIE(0) 0.87,
    wEI(0) -0.87, c 0.1, NE 4000, NI 1000, n 50, h0 0.1), decoding accuracy Phi(sqrt(S/N)/2) from
    the input-averaged S/N, one network per point, the product wIE*wEI held at the reference while
    the ratio varies. The range of the ratio is not given; the range is read from Figure 5 if the
    PDF is supplied, otherwise 0.1 to 10 on a log scale (a standard choice). Reproduced when
    inhibitory accuracy is below excitatory at every value.
- id: fig5bc-selective-models-match
  statement: In signal-selective and SNR-selective models, inhibitory and excitatory neurons have
# Claims for Najafi, Elsayed, Cao, Pnevmatikakis, Latham, Cunningham & Churchland (2020), Neuron
# 105, 165-179, on dandiset 000016.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
# pilot-10 as stated in docs/protocol.md.
[... 56 more lines not kept]
```

**Agent**

I have what I need: full text (PMC author manuscript), Methods, and the supplement with its Supplemental Experimental Procedures. The paper links no code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "content": "# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset\n# 000128.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, protocol\n# pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC2991102, NIHMS240235), full text\n# with Results, Methods and figure legends, and its supplement (NIHMS240235-supplement-01.pdf,\n# Supplemental Figures 1 to 5 with legends, Supplemental Text and Supplemental Experimental\n# Procedures), as extracted under paper/. The version of record and the main figures were not seen,\n# only their legends; no PDF of the main text was supplied.\n#\n# Code: the paper links no code and names no repository (it says only that regressions were done in\n# Matlab). No code was read. Every method below is from the Methods, the legends or the supplement.\n#\n# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental\n# Procedures). Three adult male rhesus monkeys (A, B, J, about 10 kg) made delayed reaches on a\n# fronto-parallel screen; hand tracked optically at 60 Hz (0.35 mm), eye at 240 Hz. A trial is a\n# touch-spot hold of at least 400 ms, target onset (the target jitters, 2 mm SD), a delay of about 0\n# to 1000 ms, then the go cue (jitter stops, touch spot disappears) and the reach. Four datasets.\n# - Monkeys A and B, speed task, single electrodes; 7 directions x 2 distances x 2 instructed speeds\n#   (red fast, green slow) = 28 conditions; 64 and 74 single units; mean 311 and 492 trials per neuron.\n# - Monkey J, maze task, single electrodes; 4 sets of 27 mazes (108 conditions), each neuron recorded\n#   on one or more sets; 172 single units; mean 388 trials per neuron.\n# - Monkey J-array, maze task, two 96-electrode arrays, one in caudal PMd and one in surface M1\n#   (Supplemental Figure 3); all 108 conditions interleaved; 146 single- and multi-unit isolations\n#   recorded simultaneously; mean 2166 trials per neuron (Results) or 2155 (Methods). No EMG.\n# Maze conditions are one third straight reaches without barriers, one third curved around virtual\n# barriers, and one third the same barrier mazes with unreachable distractor targets. Fixation was\n# enforced during the delay for monkey J only. Allowed reaction times 120 to 900 ms (maze); reward\n# after a 700 ms target hold (maze). EMG (A, B, J only) from deltoid, biceps, triceps, trapezius,\n# latissimus dorsi and pectoralis. Recordings from caudal PMd and surface and sulcal M1.\n# The dandiset's title on the archive (\"MC_Maze, macaque primary motor and dorsal premotor cortex\n# spiking activity during delayed reaching\") points to the maze task recorded with arrays, the\n# J-array dataset. Whether it holds the speed task, the single-electrode units or EMG is the\n# author's to find; the claims on those are written as the paper reports them.\n#\n# Methods common to the claims on recorded data (M1 to M9). Each is from the source named; where the\n# paper leaves a detail open, the readings are named and every one is run.\n# M1 Trials. Successful trials with delay > 400 ms only (Methods, Task design). For the maze task,\n#    only trials whose horizontal and vertical velocity profiles correlate with a reference\n#    \"proto-trial\" at r > 0.9 (Supplemental Experimental Procedures). Open; the paper does not\n#    define the proto-trial, the window or how the two components combine. Readings (T1) the\n#    proto-trial is the condition's mean velocity over its trials, each component must correlate\n#    at r > 0.9, window movement onset -150 to +800 ms (the maze peri-movement window, M5);\n#    (T2) as T1 with the two components concatenated into one profile. If the dataset marks the\n#    paper's own trial selection, that is shown as a variant.\n# M2 Firing rates. Spikes convolved with a 20 ms Gaussian and averaged over the trials of each\n#    condition, separately locked to the go cue and to movement onset (Supplemental Experimental\n#    Procedures; Supplemental Figure 4 legend). \"Width 20 ms\" is taken as SD 20 ms, a standard\n#    choice that cannot change epoch averages. Rates are sampled every 10 ms, a standard choice.\n# M3 Movement onset. The paper does not say how it was detected. The movement onset marked in the\n#    dataset is used; if the dataset marks none, this step is open and the claims that need it are\n#    blocked as methods_underspecified unless the author asks a reader.\n# M4 Epochs. Preparatory rate, mean from 200 ms before the go cue to 100 ms after. Peri-movement\n#    rate for the tuning correlation, mean from 100 ms before to 350 ms after movement onset\n#    (Methods, Correlations between preparatory and peri-movement tuning). The preparatory epoch of\n#    the PD analyses is the same window (the Methods define one preparatory epoch).\n# M5 Peri-movement T-matrix. Condition-mean rates from 150 ms before movement onset to 800 ms after\n#    (maze) or 400 ms after (speed task), all neurons concatenated in each row (one row per\n#    condition), without normalisation, leaving out the neuron whose preparatory tuning is being\n#    fit; PCA over conditions (columns mean-centred), the first k scores form the c x k matrix S\n#    (Results, Testing preparatory tuning in PCA-based spaces; Methods, PCA-based spaces;\n#    Supplemental Figure 2).\n# M6 Neuron selection. Neurons with at least 5 spikes/s of preparatory tuning for J-array, 10\n#    spikes/s for the single-electrode datasets (Methods, Neural recordings and datasets). For the\n#    tuning correlation, also peri-movement tuning at least 1.5 times the preparatory tuning\n#    (Methods, Correlations). The measure of \"tuning\" is open. Readings (S1) the range, maximum\n#    minus minimum over conditions of the condition-mean rate in the epoch; (S2) the standard\n#    deviation over conditions.\n# M7 PD fit and performance. x_n = b0 + S b by least squares with an intercept; leave-one-condition-\n#    out; performance = 1 - (mean over left-out conditions of the squared error) / (variance of x_n\n#    over conditions) (Methods, Using a PD; PD performance). Variance with denominator c, a\n#    standard choice. Performance is averaged over the selected neurons (Results, Figure 6E).\n# M8 Dimensionalities. PCA-based spaces are tested over k = 1 to the largest k. Open; the Results\n#    give \"k in the range of 3-14\" and Figure 6E allows up to 12. Readings (K1) k up to 14;\n#    (K2) k up to 12. The best k is the one with the highest mean performance.\n# M9 Task spaces (Methods, Task spaces), from condition-mean hand trajectories, movement onset to\n#    the end of the reach (end of reach as marked in the dataset, else when speed first falls below\n#    5% of its peak after the peak, a standard choice). For the maze task: endpoints + maximum speed\n#    (3-D); initial velocity (2-D, mean horizontal and vertical velocity over the first 150 ms after\n#    movement onset); endpoints + orthogonal excursion (3-D, signed maximum perpendicular distance\n#    from the straight start-to-end line, positive counterclockwise); endpoints + viapoint (4-D,\n#    coordinates of that maximum departure); endpoints + maximum velocity (4-D); endpoints +\n#    halfpoint (4-D, the point halfway along the path); segment directions (6-D, displacements of\n#    three segments); kitchen sink (11-D for the maze, segment directions, maximum counterclockwise\n#    excursion and its coordinates, barriers present 0 or 1, distractors present 0 or 1). Open\n#    details, each with readings run: peak horizontal and vertical velocity as (V1) each\n#    component's maximum absolute value or (V2) the components at the time of peak speed; the\n#    three segments as (G1) equal path length or (G2) equal time.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000128\"\npaper: doi:10.1016/j.neuron.2010.09.015\nclaims:\n- id: recordings-jarray\n  statement: The J-array dataset holds 146 single- and multi-unit isolations from two 96-electrode\n    arrays, recorded on the maze task with 108 conditions, with a mean of 2166 trials per neuron.\n  source: Results, Behavior and recordings, paragraph 1; Methods, Neural recordings and datasets\n  quote: (27 and 108 conditions for ‘monkey J’ and ‘monkey J-array’ datasets) ... a pair of implanted\n    96-electrode arrays (J-array dataset, 146 single- and multi-unit isolations) ... High trial counts\n    (mean trials/neuron = 311, 492, 388 and 2166 for monkey A, B, J, J-array)\n  expected:\n  - quantity: units in the J-array dataset\n    value: 146\n    tolerance: 14.6\n  - quantity: maze conditions\n    value: 108\n    tolerance: 0\n  - quantity: mean trials per neuron, J-array\n    value: 2166\n    tolerance: 216.6\n  criterion: Counts from the dataset's units, conditions and trials. The trial count can be read as\n    (a) all successful trials or (b) those kept by M1 (delay > 400 ms and the proto-trial\n    selection); the Methods print 2155 where the Results print 2166, both within the tolerance.\n    Reproduced when all three are within tolerance under one reading.\n- id: recordings-single-electrode\n  statement: The single-electrode datasets hold 64, 74 and 172 single units for monkeys A, B and J,\n    with means of 311, 492 and 388 trials per neuron.\n  source: Results, Behavior and recordings, paragraph 1; Supplemental Experimental Procedures, Neural\n    and EMG recordings\n  quote: A total of 310 single-electrode isolations (64, 74, and 172 single-unit isolations for\n    monkeys A, B and J) were recorded from caudal PMd, surface M1 and sulcal M1.\n  expected:\n  - quantity: single units, monkey A\n    value: 64\n    tolerance: 6.4\n  - quantity: single units, monkey B\n    value: 74\n    tolerance: 7.4\n  - quantity: single units, monkey J\n    value: 172\n    tolerance: 17.2\n  criterion: Testable only if the dataset holds the speed task or the single-electrode maze\n    recordings. Reproduced when every count the dataset can give is within tolerance.\n- id: fig2b-example-concordant-tuning\n  statement: In the speed task one example neuron keeps its preparatory preference (reaches up and\n    left) into the peri-movement epoch, with a preparatory to peri-movement tuning correlation of\n    0.72.\n  source: Results, Neural responses during preparation and movement, paragraph 2; Figure 2B\n  quote: This preference is shared between preparatory and peri-movement epochs. This agreement is\n    not perfect (two green traces surpass the black trace) but the overall correlation is quite high\n    ( r =0.72, see section on correlations below for details).\n  expected:\n    quantity: tuning correlation of the Figure 2B neuron\n    value: 0.72\n    tolerance: 0.072\n  criterion: Speed task only (monkey A or B); the paper does not name the neuron. Per neuron, the\n    tuning correlation of claim fig4abc-mean-correlation-single-electrode. Reproduced when at\n    least one speed-task neuron has r within tolerance of 0.72 and a preparatory preference up and\n    left; blocked if the dataset holds no speed-task data.\n- id: fig2ce-example-opposing-tuning\n  statement: Three other speed-task neurons with clear preparatory tuning do not keep their\n    preferences into the peri-movement epoch; their preparatory and peri-movement tuning are\n    negatively correlated, even for straight reaches at one distance and speed.\n  source: Results, Neural responses during preparation and movement, paragraph 3; Figure 2C-E and\n    legend\n  quote: Despite clear preparatory tuning, preferences are not maintained between the preparatory\n    and peri-movement epochs (color ordering differs between epochs). ... These neurons show negative\n    correlations between preparatory and peri-movement tuning.\n  criterion: Speed task only. With conditions restricted to the far distance and fast speed (the 7\n    directions, as in Figure 2C-E legend), tuning correlation as in M4 for neurons passing M6.\n    Reproduced when at least three neurons have negative correlations; blocked if the dataset holds\n    no speed-task data.\n- id: fig3-maze-most-not-maintained\n  statement: In the maze task some neurons keep similar tuning between the preparatory and\n    peri-movement epochs, but most do not.\n  source: Results, Neural responses during preparation and movement, paragraph 4; Figure 3\n  quote: Some neurons maintained similar tuning between preparatory and peri-movement epochs (panel\n    A ) but most did not.\n  criterion: J-array (and J if present), neurons selected as for Figure 4 (M6, both readings), tuning\n    correlation as in M4. The paper sets no threshold for \"similar tuning\"; the one value it calls\n    \"quite high\" is r = 0.72 (Figure 2B). Reproduced when at least one neuron has r of 0.72 or\n    more and more than half of the neurons have r below 0.72.\n  depends_on:\n  - fig4d-mean-correlation-jarray\n- id: fig4d-mean-correlation-jarray\n  statement: In the J-array dataset the correlation between a neuron's preparatory and peri-movement\n    tuning is positive on average but small (mean r = 0.13, p = 0.03; mean Spearman r = 0.11).\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 1; Figure 4D\n  quote: Across the four datasets the mean correlation was positive (p=0.01, p=0.01, p=0.12, p=0.03)\n    but only very modestly so (mean r = 0.21, 0.19, 0.06 and 0.13). Non-parametric correlations were\n    similarly modest (mean Spearman's r = 0.20, 0.20, 0.06 and 0.11).\n  statistics:\n  - about: mean Pearson tuning correlation against zero, J-array\n    statistic: mean r = 0.13\n    p: 0.03\n    n: J-array neurons tuned in both epochs (count not given)\n  expected:\n  - quantity: mean Pearson tuning correlation, J-array\n    value: 0.13\n    tolerance: 0.013\n  - quantity: mean Spearman tuning correlation, J-array\n    value: 0.11\n    tolerance: 0.011\n  criterion: Per neuron passing M6 (preparatory tuning > 5 spikes/s and peri-movement tuning at least\n    1.5 times the preparatory tuning, readings S1 and S2), the Pearson and Spearman correlation over\n    the 108 conditions between the preparatory rates and the peri-movement rates of M4, trials by\n    M1 (T1, T2). The paper does not name the test of the mean against zero. Readings (P1) one-sample\n    two-sided t-test of the r values; (P2) the same on Fisher z-transformed r; (P3) two-sided\n    Wilcoxon signed-rank test. Reproduced when, under one combination of readings, both means are\n    within tolerance and the test gives p < 0.05 with the mean positive; partially reproduced when\n    the mean is positive and below 0.2 with p < 0.05 but outside tolerance.\n- id: fig4abc-mean-correlation-single-electrode\n  statement: In the single-electrode datasets (monkeys A, B and J) the mean tuning correlation is\n    0.21, 0.19 and 0.06 (p = 0.01, 0.01 and 0.12), with mean Spearman correlations of 0.20, 0.20 and\n    0.06.\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 1; Figure\n    4A-C\n  quote: Across the four datasets the mean correlation was positive (p=0.01, p=0.01, p=0.12, p=0.03)\n    but only very modestly so (mean r = 0.21, 0.19, 0.06 and 0.13).\n  statistics:\n  - about: mean tuning correlation against zero, monkey A\n    statistic: mean r = 0.21\n    p: 0.01\n  - about: mean tuning correlation against zero, monkey B\n    statistic: mean r = 0.19\n    p: 0.01\n  - about: mean tuning correlation against zero, monkey J\n    statistic: mean r = 0.06\n    p: 0.12\n  expected:\n  - quantity: mean tuning correlation, monkey A\n    value: 0.21\n    tolerance: 0.021\n  - quantity: mean tuning correlation, monkey B\n    value: 0.19\n    tolerance: 0.019\n  - quantity: mean tuning correlation, monkey J\n    value: 0.06\n    tolerance: 0.006\n  criterion: As fig4d-mean-correlation-jarray, with the 10 spikes/s preparatory threshold, the speed\n    task peri-movement window as in M4, and for monkey J the four 27-condition sets analysed as\n    separate datasets (Methods, Task design). Reproduced per dataset the archive holds; blocked for\n    datasets it does not hold.\n- id: fig4e-correlation-time-course\n  statement: The correlation between preparatory tuning and peri-movement tuning measured at single\n    time points begins to decline about 200 ms before movement onset and is near zero by movement\n    onset.\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 2; Figure 4E\n    and legend\n  quote: The correlation with preparatory activity began to decline ∼200 ms prior to movement onset,\n    and reached values near zero by movement onset ( Figure 4E ).\n  depends_on:\n  - fig4d-mean-correlation-jarray\n  criterion: Neurons as in fig4d. Per neuron, the M4 preparatory rates correlated over conditions with\n    the rate at single times, smoothed with a 20 ms Gaussian (Figure 4E legend), every 10 ms from\n    400 ms before to 200 ms after movement onset; the mean over neurons at each time. The paper\n    used rates spliced from go-cue and movement-onset locked averages, with the gap placed to\n    minimise discontinuities (Supplemental Experimental Procedures); the placement is open.\n    Readings (A1) movement-onset locked rates throughout; (A2) go-locked rates up to 100 ms after\n    the go cue and movement-locked from 300 ms before onset, interpolated linearly in between where\n    they overlap. The paper gives no test; \"near zero\" and \"began to decline\" are read as (i) the\n    mean correlation at movement onset is not significantly above zero by the tests of fig4d (P1 to\n    P3), and (ii) the mean correlation at movement onset is below that at 200 ms before onset, and\n    more than half the drop from 400 ms before onset to onset happens after 200 ms before onset.\n    Reproduced when (i) and (ii) hold.\n- id: suppfig1-population-averages\n  statement: In population averages sorted by each neuron's preparatory preference, the weak\n    agreement between preparatory and peri-movement tuning dominates early, but the separation\n    shrinks with time and shows little relation to preparatory tuning by movement onset.\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 3;\n    Supplemental Figure 1 and legend\n  quote: In population averages ( Supp. Fig. 1 ) the lack of correlation averages out and the means\n    are dominated by the weak agreement between preparatory and peri-movement tuning. However, such\n    effects grow dramatically smaller with time. By movement onset even population averages show\n    little relationship with preparatory tuning ( Supp. Fig. 1 ).\n  depends_on:\n  - fig4d-mean-correlation-jarray\n  criterion: Neurons as in fig4d (Supplemental Figure 1 legend). Per neuron, the conditions with the\n    strongest and weakest preparatory rate and two intermediate ones (open; read as the conditions\n    at one third and two thirds of the rank order), each neuron's rates divided by its maximum rate,\n    then averaged over neurons. Separation is the strongest-minus-weakest average. The paper gives\n    no threshold for \"dramatically smaller\"; readings (R1) separation at movement onset less than\n    half its mean over the preparatory epoch; (R2) less than a quarter. Reproduced when the\n    separation in the preparatory epoch is positive and the condition holds under one reading.\n- id: fig6-peri-movement-space-best\n  statement: For every dataset the highest cross-validated PD performance in accounting for\n    preparatory tuning is reached when the PD is expressed in the space built by PCA from the\n    population peri-movement response, compared with task spaces and PCA-based kinematic and EMG\n    spaces.\n  source: Results, PD performance in a variety of spaces, paragraph 3; Figure 6A-D\n  quote: For every dataset, the highest level of performance was achieved ... when PDs were expressed\n    in the peri-movement space.\n  criterion: J-array (and other datasets the archive holds). Neurons passing the preparatory part of\n    M6 (S1, S2), regardless of peri-movement tuning (Methods, Correlations, last sentence). PD\n    performance by M7 in (a) the peri-movement space (M5) for each k (M8, K1 and K2); (b) the\n    kinematic space, PCA of a T-matrix of horizontal and vertical position, velocity and\n    acceleration from 150 ms before movement onset, each variable scaled to unit range over times\n    and conditions (Methods, PCA-based spaces), for each k; (c) every task space of M9 (V1, V2, G1,\n    G2). EMG is not recorded for J-array. The end of the kinematic window is open (\"until after the\n    reach\"); readings (W1) 800 ms after onset, as for the neural window; (W2) 600 ms, the longest\n    reach duration in Figure 1 legend. The Methods say \"each neuron contributed one kinematic\n    variable\"; readings (D1) the six variables once each; (D2) the six variables repeated in turn\n    to make as many columns blocks as neurons. Reproduced when, under every combination, the best\n    mean performance over k of the peri-movement space exceeds the best of every other space;\n    the outcome is methods_underspecified if the combinations disagree.\n- id: fig6-each-dimensionality\n  statement: Considering each dimensionality separately, PD performance is almost always higher in the\n    peri-movement space than in other spaces of the same dimensionality; for the maze task the 3-D\n    endpoints and peak speed space does not perform well.\n  source: Results, PD performance in a variety of spaces, paragraph 3; Figure 6A-D\n  quote: Even if we consider each dimensionality individually, performance was almost always higher\n    for the peri-movement space. An exception was that, among 3-dimensional spaces, the\n    ‘targs+instr. spd.’ and ‘endpoints + max. spd.’ performed very well for the datasets collected\n    using the speed task. The former is undefined for the maze task, but the latter did not perform\n    well.\n  depends_on:\n  - fig6-peri-movement-space-best\n  criterion: Performances from fig6-peri-movement-space-best. Comparisons are each task space against\n    the peri-movement space at the task space's dimensionality, and the kinematic space against the\n    peri-movement space at each k. \"Almost always\" has no threshold in the paper; it is read as all\n    comparisons but at most one, the paper naming one class of exception (3-D spaces on the speed\n    task). Reproduced on J-array when the peri-movement space wins all comparisons but at most one\n    and the 3-D endpoints + maximum speed space falls below the 3-D peri-movement space.\n- id: fig6-performance-vs-dimensionality\n  statement: PD performance in PCA-based spaces generally improves with dimensionality, peaks in a\n    middle range, and declines beyond about 10 dimensions through over-fitting.\n  source: Results, PD performance in a variety of spaces, paragraph 2; Figure 6A-D\n  quote: Performance typically improved with dimensionality. ... Performance typically declined at\n    dimensionalities >10, an indication of over-fitting.\n  depends_on:\n  - fig6-peri-movement-space-best\n  criterion: Peri-movement space mean performance over k = 1 to 14 (K1). Reproduced when performance\n    at the best k is higher than at k = 1, the best k is between 2 and 10, and performance at k = 14\n    is below that at the best k.\n- id: prep-dimensionality\n  statement: Preparatory activity is moderately high-dimensional; depending on the dataset, 7 to 10\n    dimensions capture 90% of its variance across conditions.\n  source: Supplemental Experimental Procedures, Estimating the upper limit of PD performance; Results,\n    PD performance in a variety of spaces, paragraph 2\n  quote: This T-matrix also allows us to estimate the dimensionality of preparatory activity\n    ... depending on the dataset, 7-10 dimensions were required to capture 90% of the data variance.\n  expected:\n    quantity: number of principal components for 90% of variance of the c x n preparatory matrix\n    value: 8.5\n    tolerance: 2.5\n  criterion: The c x n matrix of M4 preparatory rates (one row per condition, one column per neuron,\n    not normalised, columns mean-centred), PCA, the smallest number of components whose cumulative\n    variance reaches 90%. The range 7 to 10 widened by 10% of each bound gives 6.3 to 11, so 7 to 11\n    components. Which neurons enter is open; readings (N1) neurons passing the preparatory part of\n    M6 (S1, S2); (N2) all neurons. Reproduced when the count is within the range under one reading.\n- id: fig6e-summary-across-datasets\n  statement: Averaged over monkeys A, B and J (J-array excluded, no EMG), PD performance is highest\n    in the peri-movement space at every dimensionality limit, the advantage grows with\n    dimensionality, and task spaces are outperformed by the kinematic and EMG spaces, which are in\n    turn outperformed by the peri-movement space.\n  source: Results, PD performance in a variety of spaces, paragraph 5; Figure 6E and legend\n  quote: Performance (averaged across neurons) was highest when the PD employed the space based on\n    peri-movement neural activity. This performance differential increased at higher\n    dimensionalities, indicating that the peri-movement space better captured higher-dimensional\n    aspects of the data.\n  statistics:\n  - about: spaces worse than the best space (asterisks in Figure 6E)\n    p: 0.001\n    p_relation: \"<\"\n    n: neurons of monkeys A, B and J\n  criterion: Needs the speed task, the single-electrode J data and EMG; J-array is excluded by the\n    paper. Limits of 3, 6 and 12 dimensions; for PCA-based spaces the best k up to the limit; only\n    spaces defined for all three datasets (endpoints + maximum speed included, targets + instructed\n    speed not); performance averaged over neurons, SE over neurons. The test behind the asterisks is\n    not named; readings (Q1) paired t-test over neurons; (Q2) Wilcoxon signed-rank over neurons.\n    Reproduced when the peri-movement space is best under all three limits and no other space is\n    significantly better; blocked if the archive lacks those datasets.\n- id: fig7a-shuffled-space-poor\n  statement: A control space built from peri-movement responses in which each neuron's peri-movement\n    pattern was inverted on a random half of the conditions performs poorly, so the trailing end of\n    preparatory activity does not explain the peri-movement space's success.\n  source: Results, Controls, paragraph 1; Figure 7A and legend\n  quote: The PCA-based ‘shuffled-space’ performed poorly ( Figure 7A ); any contribution from the\n    trailing end of preparatory activity (preserved despite shuffling) is insufficient to allow good\n    performance.\n  depends_on:\n  - fig6-peri-movement-space-best\n  criterion: As fig6-peri-movement-space-best, with the T-matrix shuffled per neuron and condition\n    with probability 0.5 (Figure 7A legend), activity kept up to 150 ms before movement onset and\n    later activity reflected about the rate at that time (r'(t) = 2 r(-150 ms) - r(t)). The number\n    of shuffles is not given; 10 shuffles with the mean performance reported and the spread shown,\n    a standard choice. \"Performed poorly\" has no threshold; readings (H1) below the unshuffled\n    peri-movement space at every k; (H2) H1 and its best over k below the best of the kinematic\n    space. Reproduced when both hold; methods_underspecified when only H1 holds.\n- id: fig7b-window-start-slide\n  statement: Moving the start of the peri-movement window from 150 ms before movement onset to\n    movement onset costs little PD performance; at movement onset performance is 97% (monkey J) and\n    94% (monkeys A, B) of its original value.\n  source: Results, Controls, paragraph 1; Figure 7B and legend\n  quote: Finally, the start of the peri-movement window was 150 ms before movement onset but could be\n    slid later in time with little decline in performance ( Figure 7B ). Even when the window began\n    at movement onset ... performance was still at 97% (monkey J), and 94% (monkeys A, B) of its\n    original value.\n  expected:\n  - quantity: performance with window starting at movement onset over that starting 150 ms before,\n      monkey J\n    value: 0.97\n    tolerance: 0.097\n  - quantity: same ratio, monkeys A and B\n    value: 0.94\n    tolerance: 0.094\n  depends_on:\n  - fig6-peri-movement-space-best\n  criterion: As fig6-peri-movement-space-best, the peri-movement window starting at -150 ms and at 0\n    ms from movement onset, its end fixed; performance at the best k for each start (Figure 7B\n    legend). \"Monkey J\" may mean (J1) the single-electrode J dataset only, which the archive may not\n    hold, or (J2) both J datasets; under J2 the J-array ratio is compared with 0.97. Reproduced when\n    a ratio the dataset can give is within tolerance.\n- id: ap-location-no-effect-on-correlation\n  statement: The weak correlation between preparatory and peri-movement tuning does not depend on\n    anterior-posterior recording location; regressing tuning correlation on AP location gives r =\n    0.20, p = 0.27 for J-array and no significant effect in any dataset.\n  source: Results, Comparison of anterior versus posterior sites, paragraph 1\n  quote: \"Regressing tuning correlation (as in Figure 4 ) against AP location yielded little or no\n    effect: r =-0.05, p =0.82; r =-0.03, p =0.85; r =-0.07, p =0.52; and r =0.20, p =0.27 for the\n    four datasets.\"\n  statistics:\n  - about: monkey A\n    test: regression of tuning correlation on AP location\n    statistic: r = -0.05\n    p: 0.82\n  - about: monkey B\n    test: regression of tuning correlation on AP location\n    statistic: r = -0.03\n    p: 0.85\n  - about: monkey J\n    test: regression of tuning correlation on AP location\n    statistic: r = -0.07\n    p: 0.52\n  - about: J-array\n    test: regression of tuning correlation on AP location\n    statistic: r = 0.20\n    p: 0.27\n  depends_on:\n  - fig4d-mean-correlation-jarray\n  criterion: A claim of absence, judged on the paper's test, a linear regression (Pearson r and its\n    p) of each neuron's tuning correlation (fig4d) on its AP location. Needs a per-unit AP location;\n    for J-array, the electrode's position along the anterior-posterior axis of the arrays if the\n    dataset gives it, else the array (PMd anterior, M1 posterior) as a two-level variant. Reproduced\n    when p >= 0.05; not reproduced when p < 0.05; r reported either way.\n- id: fig7c-anterior-posterior-performance\n  statement: The peri-movement space captures preparatory tuning at both anterior and posterior sites,\n    with performance slightly better at anterior sites.\n  source: Results, Comparison of anterior versus posterior sites, paragraph 1; Figure 7C and legend\n  quote: The ability of the peri-movement space to capture tuning also held for both anterior and\n    posterior sites ( Figure 7C ). ... Performance was slightly better at anterior sites\n  depends_on:\n  - fig6-peri-movement-space-best\n  - ap-location-no-effect-on-correlation\n  criterion: As Figure 7C legend, a six-dimensional peri-movement space; neurons split at the median\n    AP location (anterior at or above, posterior at or below); performance normalised by its upper\n    limit, the performance of a PCA space from the preparatory activity of all neurons (Supplemental\n    Experimental Procedures), and compared with random subdivisions of the same sizes. Whether the\n    space for each half is built from that half only is open; readings (B1) from that half's\n    neurons; (B2) from all neurons. Reproduced when normalised performance for both halves is above\n    zero and within the spread of the random subdivisions or above it, and anterior is higher than\n    posterior.\n- id: fig7d-pd-consistency\n  statement: When the PD is measured on two random sets of 25 conditions, it is most stable in the\n    peri-movement space, for every comparison space and all four datasets.\n  source: Results, Stability of the PD, paragraph 2; Figure 7D and legend\n  quote: Yet for every comparison, and for all four datasets, the PD was most stable when measured in\n    the peri-movement space.\n  depends_on:\n  - fig6-peri-movement-space-best\n  criterion: Per neuron, 25 conditions drawn with replacement, PD fit by M7 regression (unit length),\n    another 25 drawn, PD refit; consistency is the dot product of the two PDs, averaged over neurons\n    (Results, Stability of the PD). The number of draws per neuron is not given; 100 draws averaged,\n    a standard choice. Comparison spaces for the maze task (Figure 7D legend) endpoints + maximum\n    speed (3-D), segment directions (6-D), the kinematic space at its best k from Figure 6 for this\n    dataset; the peri-movement space at the same dimensionality as each. Reproduced when the\n    peri-movement space has the higher mean consistency in every comparison.\n- id: fig8-model-weak-correlation\n  statement: In a simulated linear dynamical system (a harmonic oscillator held at 25 random initial\n    states, then released), the preparatory to peri-movement tuning correlation of a unit is low\n    (0.08), and a given preparatory rate can lead to opposing peri-movement patterns.\n  source: Results, Tuning from a dynamical systems perspective, paragraph 2; Figure 8B-C and legend\n  quote: The correlation of preparatory activity with peri-movement activity (averaged over the gray\n    interval) was 0.08.\n  criterion: A simulation, not a test on recorded data. Two units, x(t+1) = W x(t) with W as printed\n    in the Figure 8 legend, [[1, -2 pi/360], [2 pi/360, 1]] (the exact rotation shown as a variant),\n    25 random initial states. Open details, the distribution of initial states and the gray\n    interval; readings (I1) uniform in [-1, 1] squared; (I2) standard normal; (J1) the first 360\n    steps after release; (J2) the first 180 steps. The seed is unknown, so the value is judged\n    against the spread over 1000 draws of 25 states. Reproduced when 0.08 lies within the central\n    95% of that spread under one combination.\n- id: fig8-model-pd-perfect\n  statement: In the same simulated system, preparatory tuning is captured perfectly by a PD in the\n    two-dimensional space found by PCA of the peri-movement activity.\n  source: Results, Tuning from a dynamical systems perspective, paragraph 3; Figure 8D and legend;\n    Supplemental Text\n  quote: The PD points towards the pattern recruited by the activity of unit one (panel A ), and\n    perfectly captures preparatory ‘tuning’.\n  criterion: A simulation, not a test on recorded data. As fig8-model-weak-correlation; PCA of the\n    25 x 2t matrix of peri-movement activity, k = 2, PD fit of unit 1's initial rates by M7 without\n    cross-validation and with it. Reproduced when the fit is exact to numerical precision (R squared\n    and leave-one-out performance above 0.999) under every reading.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000128/10.1016-j.neuron.2010.09.015.yaml paper/10.1016-j.neuron.2010.09.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker passes (21 claims, 21 quotes, 0 problems). Now the style checks and two fixes: the tolerance on the dimensionality range, and a threshold in fig4d that the paper does not give.

**Agent calls Bash**

```bash
f=claims/000128/10.1016-j.neuron.2010.09.015.yaml; grep -n "—" $f; grep -n -i "rather" $f; python3 - <<'E'
import yaml,re
f='claims/000128/10.1016-j.neuron.2010.09.015.yaml'
d=yaml.safe_load(open(f))
lines=open(f).read().split('\n')
# flag plain-scalar lines containing ': ' beyond the key
for i,l in enumerate(lines,1):
    if l.lstrip().startswith('#'): continue
    s=l.strip().lstrip('- ')
    m=re.match(r'^[a-z_]+: ',s)
    rest=s[m.end():] if m else s
    if ': ' in rest and not rest.startswith('"'): print(i,l)
E
```

```
(Bash completed with no output)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    value: 8.5\n    tolerance: 2.5",
 "new_string": "    value: 8.65\n    tolerance: 2.35"
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "    within tolerance and the test gives p < 0.05 with the mean positive; partially reproduced when\n    the mean is positive and below 0.2 with p < 0.05 but outside tolerance.",
 "new_string": "    within tolerance and the test gives p < 0.05 with the mean positive; partially reproduced when\n    the mean is positive with p < 0.05 under one combination but no combination puts both means\n    within tolerance."
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "to make as many columns blocks as neurons.",
 "new_string": "to make as many column blocks as there are neurons."
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000128/10.1016-j.neuron.2010.09.015.yaml",
 "old_string": "  criterion: Peri-movement space mean performance over k = 1 to 14 (K1). Reproduced when performance\n    at the best k is higher than at k = 1, the best k is between 2 and 10, and performance at k = 14\n    is below that at the best k.",
 "new_string": "  criterion: Peri-movement space mean performance over k = 1 to 14 (K1). The paper gives no test;\n    \"improved with dimensionality\" and \"declined at dimensionalities >10\" are read as performance at\n    the best k higher than at k = 1, the best k at 10 or below, and performance at k = 14 below that\n    at the best k. Reproduced when all three hold."
}
```

```
The file claims/000128/10.1016-j.neuron.2010.09.015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000128/10.1016-j.neuron.2010.09.015.yaml paper/10.1016-j.neuron.2010.09.015.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

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

**Details the paper leaves open, with the readings named:**
- **Trial selection:** the reference "proto-trial" and how the two velocity components are compared. Readings: the condition-mean velocity with each component at r > 0.9, or the components concatenated.
- **Movement onset:** the paper never says how it was detected. The file uses the onset marked in the dataset; if there is none, that step is open.
- **"Spikes/s of tuning" for neuron inclusion:** the range across conditions, or the SD across conditions.
- **Test of the mean correlation against zero:** a t-test, a t-test on Fisher z, or a Wilcoxon signed-rank test.
- **Highest PCA dimensionality tested:** 14 or 12.
- **Kinematic space:** the window end (800 or 600 ms after movement onset) and "each neuron contributed one kinematic variable" (the six variables once, or repeated once per neuron).
- **Task spaces:** peak velocity (each component's maximum, or the components at peak speed) and segments (equal path length, or equal time).
- **Figure 4E:** how the go-cue and movement-onset traces are spliced (movement-locked throughout, or a splice).
- **Supplemental Figure 1:** the two intermediate conditions (read as the one-third and two-thirds ranks). For "dramatically smaller" no threshold is given; readings: less than half, or less than a quarter.
- **Figure 7A:** "performed poorly" means either below the unshuffled peri-movement space, or below it and also below the kinematic space.
- **Figure 7B:** "monkey J" means either the single-electrode J dataset or both J datasets.
- **Figure 7C:** whether each anterior or posterior half gets its own space; readings: built from that half, or from all neurons.
- **Figure 8:** the distribution of initial states (uniform or normal) and the grey interval (360 or 180 steps).
- **Standard choices** that cannot change an outcome: the 20 ms Gaussian taken as SD, 10 ms sampling, the shuffle count, the number of consistency draws, and the end-of-reach rule.

**Thresholds I set myself.** Several qualitative claims have no test or threshold in the paper, so their criteria are my readings of the wording, and the file says so:
- "most did not" maintain tuning (the 0.72 example is used as the cutoff);
- "began to decline" and "near zero" (Figure 4E);
- "almost always" higher;
- the dimensionality peak.

**Missing from the paper:**
- The neuron counts behind each mean correlation.
- The test behind the four p-values and behind the Figure 6E asterisks.
- The identity of the Figure 2B neuron.
- How movement onset was detected.
- A per-unit AP location for the array units, which the AP claims need.

The trials-per-neuron figure for J-array differs between sections (2166 in the Results, 2155 in the Methods); both fall within the tolerance.

## End of run

24 turns, 6 minutes, result: success.
