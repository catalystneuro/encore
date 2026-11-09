# 001605 · claims · run 39582788230

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/001605 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -30 paper/10.1038-nn.4390.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4390.txt",
 "limit": 1200
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4390.txt",
 "offset": 1200,
 "limit": 1160
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4390.txt",
 "offset": 1200,
 "limit": 600
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4390.txt",
 "offset": 1799,
 "limit": 560
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls claims/001642/; head -60 claims/001642/*.yaml; grep -n "^  [a-z_]*:" -r claims/*/ -h | sort | uniq -c | sort -rn | head -40
```

```
10.1523-jneurosci.1962-14.2015.yaml
# Claims for Ito & Doya (2015), J Neurosci 35(8):3499-3514, on dandiset 001642.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record, open access, as served by PMC (PMC4339358), stored in
# paper/10.1523-jneurosci.1962-14.2015.txt: abstract, Introduction, Materials and Methods,
# Results, Discussion and the figure legends. The paper has no supplement. No PDF was available.
# The display equations of the Methods (decision-tree probability, normalized likelihood,
# Markov model, DFQ update and choice rule, parameter drift, mutual information, BIC, and the
# regression model (2)) are images on PMC and are missing from the text; only the words around
# them were read. Where a criterion needs one of them, it is named as open with the readings
# the surrounding text allows. Figure panels (such as the windows drawn in Fig. 6A) could not
# be read. The paper links no code, so no code was read.
#
# Data the paper used, as it reports them. Seven male Long-Evans rats. 86 recording sessions,
# 78,107 trials: 12,185 single fixed-choice, 22,234 double fixed-choice, 36,292 free-choice and
# 3505 extinction-test trials. Each trial starts with a start tone; a center-hole poke of
# 500-1000 ms brings one of three cue tones (left tone 900 Hz, right tone 6500 Hz, choice tone
# white noise, 1000-2000 ms); after cue offset the rat pokes the left or right hole and hears
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001605/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:1500])"; curl -s "https://api.dandiarchive.org/api/dandisets/001605/versions/draft/info/" | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('name'));print(d.get('description'));print(d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 60,260p claims/001642/*.yaml; sed -n 1,80p tools/claims_check.py
```

```
# it needs):
#  - O1, MI estimation. The four firing levels and any bias correction are referred to Ito and
#    Doya (2009) and not restated. Readings: (a) levels as quartiles of the neuron's spike
#    counts in that window across the trials used (equal occupancy), no bias correction;
#    (b) the same with the mean MI of the random-event shuffles subtracted. The plug-in
#    estimate from the 4 x 2 table is used in both, divided by the window length for bits/s.
#  - O2, smoothing of EASHs for Fig. 4. The Methods use a 10 ms Gaussian (unit exclusion), the
#    Fig. 3 legend 30 ms. Readings: (a) 10 ms SD; (b) 30 ms SD; (c) none.
#  - O3, trials in EASHs and Fig. 5. "Whole trials" may (a) exclude or (b) include the
#    extinction-test trials; wait-error and error trials have no action and are left out.
#  - O4, chi-square tests of proportions. Readings: 2 x 2 test (a) without or (b) with Yates
#    continuity correction.
#  - O5, "Mann-Whitney U test" for proportions of coding neurons (Figs. 8 and 6). Read as a
#    Mann-Whitney U test on per-neuron 0/1 coding indicators, two-sided.
#  - O6, regression time bins for Fig. 8, "500 ms before and after the seven trial events".
#    Readings: (a) 500 ms windows before and after each event in real time; (b) the
#    same windows on the EASH time axis. Which seven events is not stated either: the Methods
#    define six task events E1 to E6 and the time points E0 and E7, so the readings are
#    (i) E1 to E7, (ii) E0 to E6. The Results refer to phases (Phase 1, first half of
#    Phase 4, Phase 5); a phase result is taken from the windows lying in that phase.
[... 261 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "dataset",
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
   "type": "object",
   "additionalProperties": false,
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm; pdftoppm -r 110 -png -f 2 -l 6 paper/10.1038-nn.4390.pdf pg && pdftoppm -r 110 -png -f 16 -l 16 paper/10.1038-nn.4390.supp.pdf sp; ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import fitz,os
t=os.environ['TMPDIR']
d=fitz.open('paper/10.1038-nn.4390.pdf')
for i in [1,2,4,5]:
    d[i].get_pixmap(dpi=130).save(f'{t}/pg{i+1}.png')
s=fitz.open('paper/10.1038-nn.4390.supp.pdf'); print(len(s))
for i in [7,9,15]:
    s[i].get_pixmap(dpi=110).save(f'{t}/sp{i+1}.png')
"; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.4390.pdf",
 "pages": "2-6"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The PDF reader needs poppler, which isn't installed. I'll try installing PyMuPDF into the temp directory to render the pages.

**Agent calls Bash**

```bash
pip install -q --target $TMPDIR/pylib pymupdf 2>&1 | tail -2; PYTHONPATH=$TMPDIR/pylib python -c "
import fitz,os
t=os.environ['TMPDIR']
d=fitz.open('paper/10.1038-nn.4390.pdf')
for i in [1,2,4,5]:
    d[i].get_pixmap(dpi=130).save(f'{t}/pg{i+1}.png')
s=fitz.open('paper/10.1038-nn.4390.supp.pdf'); print(len(s))
for i in [7,8,10,15]:
    s[i].get_pixmap(dpi=110).save(f'{t}/sp{i+1}.png')
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg2.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg3.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg5.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/sp16.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
grep -rn -B3 -A6 "range" claims/*/*.yaml | grep -A6 "statistics:" | head -60
```

```
claims/000003/10.1016-j.neuron.2016.12.011.yaml-500-  statistics:
claims/000003/10.1016-j.neuron.2016.12.011.yaml-501-  - about: 20 place cells, across types
claims/000003/10.1016-j.neuron.2016.12.011.yaml-502-    test: Kruskal-Wallis test
claims/000003/10.1016-j.neuron.2016.12.011.yaml-503-    p: 1.0e-05
claims/000003/10.1016-j.neuron.2016.12.011.yaml-504-    p_relation: "<"
--
claims/000005/10.1038-nn.4412.yaml-294-    while whisking causes only a small depolarization or hyperpolarization (1.2 +- 2.1 mV).
--
claims/000213/10.1016-j.neuron.2018.04.028.yaml-458-  statistics:
claims/000213/10.1016-j.neuron.2018.04.028.yaml-459-  - test: two-sample t test
claims/000213/10.1016-j.neuron.2018.04.028.yaml-460-    p: 0.001
--
claims/000213/10.1016-j.neuron.2018.04.028.yaml-495-    tolerance: 0.17
claims/000213/10.1016-j.neuron.2018.04.028.yaml-496-    unit: bits/cm
claims/000213/10.1016-j.neuron.2018.04.028.yaml-497-  criterion: Information as in fig1e-phase-info-smaller-scale (7 equal-width levels over the map's
--
claims/000552/10.1038-s41593-022-01138-x.yaml-392-  statistics:
claims/000552/10.1038-s41593-022-01138-x.yaml-393-  - about: wake, across birthdates
claims/000552/10.1038-s41593-022-01138-x.yaml-394-    test: Kruskal–Wallis
claims/000552/10.1038-s41593-022-01138-x.yaml-395-    statistic: H = 63.3868, d.f. = 3
[... 40 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "content": "# Claims for Funamizu, Kuhn & Doya (2016), Nat Neurosci 19(12):1682-1689, on dandiset 001605.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (Nature Neuroscience, December 2016), from the PDF supplied by\n# hand, stored as paper/10.1038-nn.4390.txt: main text, figure legends, Online Methods, and the\n# supplement (41593_2016_BFnn4390_MOESM16_ESM.pdf: Supplementary Figs. 1 to 14 and Supplementary\n# Table 1). The display equations of the Methods are garbled in the text; the words around them\n# were read. PDF pages were rendered only to read Figure 1c, Figure 2c,d, Figure 4 and\n# Supplementary Table 1 (columns), which the text garbles. Code: the paper says its Matlab scripts\n# are \"available from corresponding author upon request\"; it links no code, so none was read.\n# Data availability in the paper points to https://groups.oist.jp/ncu/data.\n#\n# Data the paper used, as it reports them.\n#  - Imaging: eight male C57BL/6N mice, 94 sessions (one per day, one imaging plane), mouse 1 to 8\n#    with 2, 10, 5, 14, 15, 15, 12 and 21 sessions. Areas PPC (LPtA, about 1.7 mm posterior and\n#    1.6 mm lateral of bregma) and PM (V2ML, with some V2MM or MM), right hemisphere, layers 2, 3\n#    and 5. PPC: 17, 15 and 14 sessions in layers 2, 3, 5; PM: 16, 15 and 17. 41,031 active\n#    neurons (PPC 8,371, 7,108, 4,859; PM 7,788, 7,005, 5,900). Two-photon imaging at 30.9 Hz,\n#    GCaMP6f with TurboRFP; signal is the green/red ratio R(t), and dR/R = (R - mean R)/mean R with\n#    the mean over all 150 trials including inter-trial intervals. ROIs drawn by hand; active ROIs\n#    carry a signal beyond 3 sigma in the session.\n#  - Behaviour, simultaneous with imaging: auditory virtual navigation on a spherical treadmill in\n#    darkness. A trial starts with a start tone; the virtual sound source (goal) is 67 to 134 cm\n#    from the start; reward when the mouse passes the goal and licks. Conditions continuous,\n#    intermittent 1 and intermittent 2 at 70, 15 and 15%. Zones are 17 cm long; in intermittent 1\n#    a no-sound zone is centred on the goal, in intermittent 2 a sound zone is; the first 33 cm\n#    from the start always have sound. The figures put zone borders at 8.4, 25.1, 41.9 and 58.6 cm\n#    from the goal, so in intermittent 1 the zones 8.4-0 and 41.9-25.1 cm are silent and 25.1-8.4\n#    and 58.6-41.9 cm have sound; intermittent 2 is the reverse. Variables: goal distance,\n#    locomotion speed, licks, sound on or off, reward.\n#  - Per session, the first 150 trials; trials taking more than 20 s to reward (2.71%) and error\n#    trials (0.142%) excluded. Sessions kept only when the start-to-first-lick distance correlated\n#    positively with start-to-goal distance (P < 0.01; 4 of 100 dropped) and motion correction\n#    sufficed (2 of 100 dropped). First lick means the first lick more than 33 cm from the start.\n#  - Sound-response mapping before each imaging session: the task sound (200 ms) from each of 12\n#    speakers, ten times each, 5 s apart (Supplementary Fig. 4).\n#  - Muscimol: three further mice, bilateral PPC injection of muscimol or PBS on alternate days,\n#    12 sessions, no imaging (Fig. 1d-g, Supplementary Fig. 2). Five more mice for the spread of\n#    fluorescent muscimol (histology only).\n# The archive's description of dandiset 001605 names only the imaging sessions with their\n# behaviour (94 session files); whether the muscimol sessions or the sound-mapping trials are\n# there is for the author to find. No claim uses outside data.\n#\n# Methods fixed by the paper and used throughout (Online Methods unless named):\n#  - Task-relevant neurons: trial traces of dR/R aligned (i) in time to the start tone, (ii) in\n#    time to reaching the goal, (iii) in time to the first lick, (iv) in distance from the start,\n#    (v) in goal distance; averaged over trials, then moving-averaged over 500 ms (time) or\n#    8.37 cm with 0.42 cm steps (distance). Task-relevant when the aligned average is\n#    significantly positive at any point against baseline, one-sided one-sample t-test,\n#    P < 1e-10. Start neurons, significant within 2 s of the start ((i) or (iv)); goal-aligned\n#    ((ii) or (v)) neurons are split by the time of peak activity into before- and after-reaching;\n#    the after-reaching group is split by k-means (two clusters) on the activity of the last\n#    500 ms (16 frames) before the goal into after-reaching (ramping) and reward neurons.\n#    Goal-distance neurons are the before- and after-reaching neurons. A neuron significant in\n#    goal-aligned and lick-aligned activity is assigned to whichever is more significant.\n#    Trials of all conditions are used (Fig. 2c legend, \"Neural activity of all trials was\n#    averaged\"). Traces are shown up to the goal in goal distance and after it in time (Fig. 2c\n#    legend); the before/after split is read on that joined trace.\n#  - Regression of single neurons (equations 1 to 3): unfiltered dR/R on Gaussian basis functions\n#    of goal distance or goal time, lick frequency and locomotion speed, with the centre of each\n#    basis at the value of maximal averaged activity and its width free; 11 variable sets; the\n#    best set by BIC on the sum of squared errors over all frames of the 150 trials.\n#  - After-reaching slopes (equation 5): per neuron, dR/R binned every 0.42 cm of goal distance,\n#    linear regression on distance within each zone.\n#  - Decoder (equations 6 to 10): all goal-distance neurons of a session (sessions with none, 3 of\n#    94, excluded); n is dR/R after a 3-frame (97.1 ms) moving average; tuning from continuous\n#    trials, 4.2 cm distance bins, mean and s.d. of log activity by maximum likelihood, smoothed\n#    with a Gaussian of s.d. 4.2 cm and resampled every 0.84 cm; traces shifted per neuron to be\n#    positive; log-normal likelihood, neurons independent, flat prior. Continuous trials decoded\n#    by leave-one-trial-out; intermittent trials decoded by a decoder trained on all continuous\n#    trials. Outputs per frame: RMSE, the root of the posterior-expected squared deviation from\n#    the actual distance; MAP; uncertainty, the posterior s.d. about the MAP. MAP and uncertainty\n#    slopes: linear regression on goal distance within each zone of each trial (equation 10).\n#    The slope is reported as decrease per cm of approach (Fig. 5 axes, \"MAP decrease per cm\").\n#  - Statistics: two-sided Mann-Whitney U, Wilcoxon signed-rank or Ansari-Bradley tests unless\n#    one-sided is stated; P < 0.01 for the multiple comparisons of Figs. 1c,f and 2d (Bonferroni).\n#    Medians with robust s.e. (1.4826 x MAD / sqrt(n)).\n#\n# Details the paper leaves open. The notebook runs every reading of a method; the outcome is the\n# one they all give, and the claim is blocked as methods_underspecified when they disagree. Where\n# readings are of what a reported number counts, the claim holds under any of them.\n#  - O1, baseline of the task-relevance t-test. Readings (a) zero, the session mean of R that\n#    dR/R is taken against; (b) the neuron's mean dR/R over inter-trial intervals. The t-test is\n#    over trials at each point of the aligned trace.\n#  - O2, extent of the aligned traces. Read from the axes of Fig. 2c: start, -1 to 6 s; goal\n#    time, -3 to 3 s; goal distance, 67 to 0 cm then 0 to 3 s after the goal; first lick, -2 to\n#    3 s. The start-aligned distance window (iv) is given nowhere; readings (a) 0 to 67 cm, the\n#    shortest start-to-goal distance; (b) 0 to 33 cm, the stretch always with sound.\n#  - O3, k-means feature for after-reaching against reward neurons. Readings (a) the 16-frame\n#    trace before the goal of each neuron's trial-averaged activity, normalized 0 to 1 as in\n#    Fig. 2c; (b) the mean of that trace. The cluster with higher pre-goal activity is\n#    after-reaching. Standard k-means with a fixed seed and repeated starts (a standard choice).\n#  - O4, distance preference: the goal distance of peak activity of the distance-aligned trace\n#    (67 to 0 cm), the \"peaks of distance coding\" of Fig. 2d, for every goal-distance neuron.\n#  - O5, per-session proportions against pooled counts, for percentages of neurons. Readings\n#    (a) mean over sessions of per-session proportions of active neurons; (b) pooled counts over\n#    sessions. The tests of proportions are Mann-Whitney U tests over sessions (the Wilcoxon w\n#    values of Fig. 2d, such as 13.5, fit sessions, not neurons).\n#  - O6, frames of the single-neuron regression. \"All frames during all 150 trials\". Readings\n#    (a) start tone to reaching the goal; (b) start tone to 3 s after the goal, with goal\n#    distance and time continuing past zero. The four initial values of each width are not\n#    given; readings (a) 1/8, 1/4, 1/2 and 1 of the variable's range in the session; (b) 1/16,\n#    1/8, 1/4 and 1/2 of it.\n#  - O7, the positive shift of traces for the log-normal likelihood. Readings: each neuron's\n#    trace shifted so its minimum is (a) 0.01 or (b) 0.1 in dR/R units.\n#  - O8, distance range decoded and bins of Figs. 4 and 5. The decoder covers 67 to 0 cm (axes of\n#    Fig. 4). Per-trial values in Fig. 4c-e are means over frames within 4.2-cm goal-distance bins\n#    (the tick spacing of Fig. 4c-e and the decoder's bin width); Supplementary Fig. 11a uses\n#    0.42 cm bins, a second reading for Fig. 4c-e. Fig. 5 zones are 58.6-41.9, 41.9-25.1,\n#    25.1-8.4 and 8.4-0 cm (axis of Fig. 5a); Figs. 5b,d use the last two.\n#  - O9, slow and fast trials (Supplementary Figs. 1 and 13): trials of each session split into\n#    equal halves by locomotion speed. Readings (a) mean speed over the trial; (b) mean speed in\n#    the no-sound zones analysed. Which no-sound zones: readings (a) every no-sound zone between\n#    67 and 0 cm, slopes averaged per trial; (b) the no-sound zone nearest the goal.\n#\n# Paper inconsistencies noted: the Results say uncertainty decreased with sound \"between 25.8 and\n# 0 cm\", where the figures use 25.1 cm. Fig. 4c legend calls RMSE \"the expected squared\n# deviation\", while its name and the Methods take the root.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001605\"\npaper: doi:10.1038/nn.4390\nclaims:\n- id: session-counts\n  statement: Imaging data come from 94 sessions of 8 mice (2, 10, 5, 14, 15, 15, 12 and 21 sessions\n    for mice 1 to 8); PPC layers 2, 3 and 5 were imaged in 17, 15 and 14 sessions and PM layers 2,\n    3 and 5 in 16, 15 and 17.\n  source: Online Methods, Behavioral analysis; Results, Goal-distance representation in PPC and PM,\n    paragraph 2\n  quote: In total, we analyzed data from 94 sessions in 8 mice (mouse 1, 2 sessions; mouse 2, 10\n    sessions; mouse 3, 5 sessions; mouse 4, 14 sessions; mouse 5, 15 sessions; mouse 6, 15\n    sessions; mouse 7, 12 sessions; mouse 8, 21 sessions)\n  expected:\n  - quantity: sessions\n    value: 94\n    tolerance: 0\n  - quantity: mice\n    value: 8\n    tolerance: 0\n  - quantity: PPC layer 2 sessions\n    value: 17\n    tolerance: 0\n  - quantity: PPC layer 3 sessions\n    value: 15\n    tolerance: 0\n  - quantity: PPC layer 5 sessions\n    value: 14\n    tolerance: 0\n  - quantity: PM layer 2 sessions\n    value: 16\n    tolerance: 0\n  - quantity: PM layer 3 sessions\n    value: 15\n    tolerance: 0\n  - quantity: PM layer 5 sessions\n    value: 17\n    tolerance: 0\n  criterion: Counts of named sessions and animals, so the tolerance is 0 for each, and the sessions\n    per mouse must match the list as a multiset (the dataset's subject labels need not follow the\n    paper's numbering). Reproduced when all counts match; partially reproduced when the totals\n    match and at most two per-group counts differ by one.\n- id: neuron-counts\n  statement: 41,031 neurons were imaged, 8,371, 7,108 and 4,859 in PPC layers 2, 3 and 5 and 7,788,\n    7,005 and 5,900 in PM; these are active cells, 99.6% of the manually selected ROIs.\n  source: Results, Goal-distance representation in PPC and PM, paragraph 2; Supplementary Table 1\n  quote: In total, we imaged the activity of 41,031 neurons in 94 sessions (PPC, 8,371, 7,108 and\n    4,859 neurons from 17, 15 and 14 sessions in layers 2, 3 and 5, respectively; PM, 7,788, 7,005\n    and 5,900 neurons from 16, 15 and 17 sessions, respectively)\n  expected:\n  - quantity: neurons, all\n    value: 41031\n    tolerance: 4103.1\n  - quantity: PPC layer 2 neurons\n    value: 8371\n    tolerance: 837.1\n  - quantity: PPC layer 3 neurons\n    value: 7108\n    tolerance: 710.8\n  - quantity: PPC layer 5 neurons\n    value: 4859\n    tolerance: 485.9\n  - quantity: PM layer 2 neurons\n    value: 7788\n    tolerance: 778.8\n  - quantity: PM layer 3 neurons\n    value: 7005\n    tolerance: 700.5\n  - quantity: PM layer 5 neurons\n    value: 5900\n    tolerance: 590\n  criterion: The per-session averages of Supplementary Table 1 (active cells 492, 474, 347, 487,\n    467, 347) times the session counts give these totals, so they count active cells. Readings\n    of what the dataset's ROIs are, (a) all ROIs, (b) ROIs with a dR/R excursion beyond 3 s.d. of\n    the session trace (the paper's \"signal beyond 3σ\"). Reproduced when, under one reading, all\n    seven counts are within tolerance.\n- id: behaviour-timing\n  statement: Mice got the reward 7.4 ± 0.1 s after the trial start and spent 860 ± 10 ms in each\n    no-sound zone of the intermittent conditions (mean ± s.e.m. over 94 sessions).\n  source: Online Methods, Behavioral training, paragraph 4\n  quote: Mice got the reward in 7.4 ± 0.1 s (mean ± s.e.m., n = 94). In intermittent conditions,\n    mice spent 860 ± 10 ms (n = 94) in each no-sound zone.\n  expected:\n  - quantity: time from start to reward, mean over sessions\n    value: 7.4\n    tolerance: 0.1\n    unit: s\n  - quantity: time per no-sound zone, mean over sessions\n    value: 0.86\n    tolerance: 0.01\n    unit: s\n  criterion: Tolerances are the stated s.e.m. Per session, the mean over the analysed trials\n    (first 150, without trials over 20 s or error trials), then the mean over sessions. Which\n    no-sound zones count is not given; readings (a) every complete no-sound zone after the first\n    33 cm and before the goal, (b) every no-sound zone the mouse enters, including the one\n    around the goal in intermittent 1 up to the reward. Reproduced when the reward time and,\n    under one reading, the zone time are within tolerance.\n- id: lick-goal-correlation\n  statement: In every session the start-to-first-lick distance correlated with the start-to-goal\n    distance, with r from 0.258 to 0.822 over the 94 sessions (r = 0.798 in the example session).\n  source: Results, Licking indicates action-dependent distance estimation, paragraph 2; Figure 1b;\n    Online Methods, Behavioral analysis\n  quote: Mice increased licking frequency as they approached the goal (r = 0.798, P = 2.11 × 10−34;\n    Fig. 1b; 94 sessions of 8 mice, r = 0.258 to 0.822, P = 0.00229 to 9.05 × 10−38)\n  statistics:\n  - about: largest P of the 94 sessions (range 0.00229 to 9.05e-38)\n    test: correlation coefficient\n    p: 0.00229\n    n: 94 sessions of 8 mice\n  expected:\n  - quantity: smallest session r\n    value: 0.258\n    tolerance: 0.0258\n  - quantity: largest session r\n    value: 0.822\n    tolerance: 0.0822\n  criterion: The Methods define the correlation used to select sessions as start-to-lick distance\n    against start-to-goal distance, first lick meaning the first lick more than 33 cm from the\n    start, over the analysed trials of all conditions. The coefficient is not named; readings\n    (a) Pearson, (b) Spearman. Reproduced when, under one reading, every session has r > 0 with\n    P < 0.01 and all r lie within 0.232 to 0.904 (the range widened by 10% of each bound).\n- id: fig1c-licking-without-sound\n  statement: Licking increased as mice approached the goal in all conditions, and in the\n    intermittent conditions it increased even in the no-sound zone around the goal.\n  source: Figure 1c; Results, Licking indicates action-dependent distance estimation, paragraph 2\n  quote: In intermittent conditions, anticipatory licking increased even when the sound was omitted\n    (one-sided Wilcoxon signed-rank test, P = 4.87 × 10−8 to 1.22 × 10−15; Fig. 1c)\n  statistics:\n  - about: intermittent 1, the four marked bins (largest P)\n    test: one-sided Wilcoxon signed-rank test\n    statistic: z = 7.91, 8.39, 7.45, 5.33\n    p: 4.87e-8\n    n: 94 sessions\n  - about: continuous, the four marked bins (largest P)\n    test: one-sided Wilcoxon signed-rank test\n    statistic: z = 7.11, 8.32, 8.42, 8.42\n    p: 5.64e-13\n    n: 94 sessions\n  - about: intermittent 2, the four marked bins (largest P)\n    test: one-sided Wilcoxon signed-rank test\n    statistic: z = 2.14, 5.44, 6.19, 8.41\n    p: 0.0160\n    n: 94 sessions\n  criterion: Licks per trial in goal-distance bins, mean per session, for each condition (Fig. 1c).\n    The bins and the pairs compared are not stated. The figure shows boxes about 4.2 cm wide and\n    four marked bins nearest the goal per condition. Bin readings (a) 4.2 cm, (b) 8.4 cm\n    (the half-zones of Fig. 1g); comparison readings (i) each of the four bins nearest the goal\n    against the bin before it, (ii) each against the bin 67 to 62.8 cm from the goal (or 67 to\n    58.6 cm under (a)/(b) respectively), where licking is near zero. One-sided signed-rank test\n    over sessions at the Bonferroni threshold P < 0.01 (Statistics). Reproduced when, under\n    every reading, in intermittent 1 licking rises significantly in every bin between 8.4 and\n    0 cm (the no-sound zone), and in continuous in all four bins.\n- id: supp1-licking-speed\n  statement: During no-sound zones licking rose more steeply in fast-locomotion trials than in slow\n    ones, in both intermittent conditions.\n  source: Supplementary Figure 1; Results, Licking indicates action-dependent distance estimation,\n    paragraph 3\n  quote: Slope of licking (1) was significantly steeper in fast trials than slow trials, suggesting\n    that mice use action-dependent distance estimation\n  statistics:\n  - about: intermittent 1\n    test: Wilcoxon signed-rank test\n    statistic: z = 3.83\n    p: 1.27e-4\n    n: 94 sessions\n  - about: intermittent 2\n    test: Wilcoxon signed-rank test\n    statistic: z = 5.33\n    p: 9.81e-8\n    n: 94 sessions\n  criterion: Per trial, lick frequency in a no-sound zone regressed on time (Lick(t) = b0 + b1 t,\n    Supplementary Fig. 1); trials split into equal slow and fast halves per session (O9); per\n    session, mean slope of slow and of fast trials; signed-rank test over sessions per condition.\n    Reproduced when, under every reading of O9, fast slopes exceed slow with P < 0.01 in both\n    intermittent conditions.\n- id: fig1d-muscimol-correlation\n  statement: Silencing PPC with muscimol lowered the correlation between start-to-lick and\n    start-to-goal distance, making lick initiation more variable.\n  source: Figure 1d; Results, Licking indicates action-dependent distance estimation, paragraph 4\n  quote: Correlation coefficients decreased after muscimol injection, indicating that silencing of\n    PPC made lick initiation more variable (Mann-Whitney U test, P = 3.08 × 10−4, z = 3.61)\n  statistics:\n  - test: Mann-Whitney U test\n    statistic: z = 3.61\n    p: 3.08e-4\n    n: muscimol and PBS sessions of 3 mice (12 sessions)\n  criterion: Session correlations as in lick-goal-correlation, muscimol sessions against PBS\n    sessions (no-injection sessions are shown in Fig. 1d but not tested), two-sided Mann-Whitney U.\n    Reproduced when muscimol correlations are lower with P < 0.05.\n- id: fig1e-muscimol-variance\n  statement: After muscimol the distance between the first lick and the goal was more variable\n    than after PBS, in all three conditions.\n  source: Figure 1e; Results, Licking indicates action-dependent distance estimation, paragraph 4\n  quote: Variance of the distance was compared between PBS and muscimol-injected trials\n  statistics:\n  - about: continuous\n    test: Ansari-Bradley test\n    statistic: w = 15.8\n    p: 4.35e-56\n    n: 1,407 PBS and 1,188 muscimol trials\n  - about: intermittent 1\n    test: Ansari-Bradley test\n    statistic: w = 7.90\n    p: 2.70e-15\n    n: 293 PBS and 240 muscimol trials\n  - about: intermittent 2\n    test: Ansari-Bradley test\n    statistic: w = 10.2\n    p: 2.53e-24\n    n: 259 PBS and 230 muscimol trials\n  criterion: First-lick-to-goal distance per trial, PBS against muscimol trials, Ansari-Bradley\n    test per condition. Reproduced when muscimol trials have the larger spread with P < 1e-14 (the\n    legend's threshold) in all three conditions.\n- id: fig1fg-muscimol-no-sound-licking\n  statement: After muscimol the increase of licking in no-sound zones was lost, while after PBS\n    licking increased toward the goal in every condition.\n  source: Figure 1f,g; Results, Licking indicates action-dependent distance estimation, paragraph 4\n  quote: The effect of PPC silencing was most prominent in intermittent conditions, with no increase\n    in licking in no-sound zones (one-sided Wilcoxon signed-rank test, P = 0.485 to 0.0212; Fig. 1f;\n    Mann-Whitney U-test, P = 0.00761 and 4.84 × 10−6; Fig. 1g)\n  statistics:\n  - about: muscimol, no-sound bins of intermittent conditions (range 0.485 to 0.0212)\n    test: one-sided Wilcoxon signed-rank test\n    p: 0.485\n    n: 12 sessions, 3 mice\n  - about: PBS against muscimol, increase from 25-17 to 17-8.4 cm, intermittent 2\n    test: Mann-Whitney U test\n    statistic: z = 2.67\n    p: 0.00761\n    n: 259 PBS and 230 muscimol trials\n  - about: PBS against muscimol, increase from 17-8.4 to 8.4-0 cm, intermittent 1\n    test: Mann-Whitney U test\n    statistic: z = 4.57\n    p: 4.84e-6\n    n: 293 PBS and 240 muscimol trials\n  criterion: Fig. 1f, licks per trial per bin as in fig1c-licking-without-sound (both bin and\n    comparison readings) over the 50 to 0 cm range, separately for muscimol and PBS sessions,\n    one-sided signed-rank test over sessions, P < 0.01. Fig. 1g, per trial, the increase of lick\n    count between the adjacent bins 25-17 and 17-8.4 cm and between 17-8.4 and 8.4-0 cm, PBS\n    against muscimol trials, Mann-Whitney U, P < 0.01. Reproduced when, under every reading, no\n    no-sound bin of intermittent 1 (8.4-0 cm) or intermittent 2 (25.1-8.4 cm) shows a\n    significant increase after muscimol, and the Fig. 1g increase is larger after PBS with\n    P < 0.01 for intermittent 1 at 17-8.4 to 8.4-0 cm and intermittent 2 at 25-17 to 17-8.4 cm.\n- id: supp2d-muscimol-overrun\n  statement: Silencing PPC increased overrun, the start of licking more than 8.3 cm past the goal,\n    most in the intermittent 1 condition.\n  source: Supplementary Figure 2d; Results, Licking indicates action-dependent distance estimation,\n    paragraph 4\n  quote: Silencing of PPC increased overrun (start licking over 8.3 cm past the goal)\n  statistics:\n  - about: continuous\n    test: Mann-Whitney U-test\n    statistic: z = 4.09\n    p: 4.26e-5\n  - about: intermittent 1\n    test: Mann-Whitney U-test\n    statistic: z = 7.96\n    p: 1.79e-15\n  - about: intermittent 2\n    test: Mann-Whitney U-test\n    statistic: z = 2.29\n    p: 0.0221\n  criterion: Per trial, the distance of the licking for reward acquisition relative to the goal\n    (the first lick at or past the goal), PBS against muscimol trials per condition, Mann-Whitney\n    U. Reproduced when muscimol trials lick farther past the goal with P < 0.01 in continuous and\n    intermittent 1 (the legend's threshold); intermittent 2 (reported P = 0.0221) is shown.\n- id: muscimol-locomotion\n  statement: PPC inactivation lowered locomotion speed and raised anticipatory licking in the\n    continuous condition, but changed neither in the intermittent conditions.\n  source: Online Methods, Muscimol injection, paragraph 2\n  quote: Inactivation of PPC decreased the locomotion speed of mice in the continuous condition\n    (MannWhitney U-test, P = 9.63 × 10−12, z = 6.81), which was most probably caused by increased\n    anticipatory licking (Mann-Whitney U-test, P = 6.92 × 10−11, z = 6.52). In intermittent\n    conditions, inactivation of PPC did not change the locomotion speed (P = 0.106, z = 1.62) and\n    the licking (P = 0.0828, z = 1.73).\n  statistics:\n  - about: speed, continuous\n    test: Mann-Whitney U-test\n    statistic: z = 6.81\n    p: 9.63e-12\n  - about: licking, continuous\n    test: Mann-Whitney U-test\n    statistic: z = 6.52\n    p: 6.92e-11\n  - about: speed, intermittent\n    test: Mann-Whitney U-test\n    statistic: z = 1.62\n    p: 0.106\n  - about: licking, intermittent\n    test: Mann-Whitney U-test\n    statistic: z = 1.73\n    p: 0.0828\n  criterion: Per trial mean locomotion speed and lick count from start to goal, muscimol against\n    PBS trials, Mann-Whitney U (two-sided, Statistics); intermittent 1 and 2 pooled as the text\n    reports one test. The no-change parts are claims of absence, judged at P < 0.05. Reproduced\n    when continuous speed is lower and licking higher after muscimol with P < 0.05, and neither\n    differs with P < 0.05 in intermittent trials.\n- id: sound-responsive-layer3\n  statement: PPC and PM neurons responded to sounds; in layer 3, PM had more sound-responsive\n    neurons than PPC (4.78% against 1.48%).\n  source: Results, Goal-distance representation in PPC and PM, paragraph 3; Supplementary Figure 4b\n  quote: On average, PM had more sound-responsive neurons than PPC in layer 3 (PPC, 1.48%, PM,\n    4.78%; Mann-Whitney U test, P = 0.0402)\n  statistics:\n  - about: layer 3, PPC against PM\n    test: Mann-Whitney U test\n    statistic: z = 2.05\n    p: 0.0402\n    n: 15 PPC and 15 PM sessions\n  expected:\n  - quantity: sound-responsive neurons, PPC layer 3\n    value: 1.48\n    tolerance: 0.148\n    unit: '%'\n  - quantity: sound-responsive neurons, PM layer 3\n    value: 4.78\n    tolerance: 0.478\n    unit: '%'\n  criterion: Sound-mapping trials (Online Methods, Imaging sound responses of neurons). Activity\n    after sound from two adjacent speakers pooled into six azimuths; 500 ms moving average; a\n    neuron is sound responsive when, at some azimuth, activity in the first 1.5 s after sound\n    onset exceeds activity in the 1 s before (one-sided t-test, P < 1e-5). Percentages per field\n    of view, readings of O5. Reproduced when, under one reading, both percentages are within\n    tolerance and the per-session Mann-Whitney U test gives PM higher with P < 0.05.\n- id: neuron-classes\n  statement: Goal-distance neurons numbered 1,116, 1,054 and 483 in PPC layers 2, 3 and 5 and 601,\n    479 and 129 in PM; of these, 744, 854 and 367 in PPC and 193, 204 and 54 in PM were\n    after-reaching neurons; per session, on average 65.6, 70.3 and 34.5 in PPC and 37.6, 31.9 and\n    7.59 in PM were goal-distance neurons.\n  source: Figure 2d; Figure 3c legend; Supplementary Figure 6 legend; Results, Distance prediction\n    with dynamic Bayesian inference, paragraph 3\n  quote: Number of after-reaching neurons in layers 2, 3, 5 was 744, 854, 367 in PPC and 193, 204,\n    54 in PM ... (average number of goal-distance neurons in layers 2, 3 and 5; PPC, 65.6, 70.3\n    and 34.5; PM, 37.6, 31.9 and 7.59)\n  expected:\n  - quantity: goal-distance neurons, PPC layer 2\n    value: 1116\n    tolerance: 111.6\n  - quantity: goal-distance neurons, PPC layer 3\n    value: 1054\n    tolerance: 105.4\n  - quantity: goal-distance neurons, PPC layer 5\n    value: 483\n    tolerance: 48.3\n  - quantity: goal-distance neurons, PM layer 2\n    value: 601\n    tolerance: 60.1\n  - quantity: goal-distance neurons, PM layer 3\n    value: 479\n    tolerance: 47.9\n  - quantity: goal-distance neurons, PM layer 5\n    value: 129\n    tolerance: 12.9\n  - quantity: after-reaching neurons, PPC layer 2\n    value: 744\n    tolerance: 74.4\n  - quantity: after-reaching neurons, PPC layer 3\n    value: 854\n    tolerance: 85.4\n  - quantity: after-reaching neurons, PPC layer 5\n    value: 367\n    tolerance: 36.7\n  - quantity: after-reaching neurons, PM layer 2\n    value: 193\n    tolerance: 19.3\n  - quantity: after-reaching neurons, PM layer 3\n    value: 204\n    tolerance: 20.4\n  - quantity: after-reaching neurons, PM layer 5\n    value: 54\n    tolerance: 5.4\n  criterion: The classification of the opening comment (Online Methods, Task-relevant neurons),\n    under readings O1, O2 and O3. Before-reaching counts follow by subtraction and match\n    Supplementary Fig. 9a (372, 200, 116; 408, 275, 75); the per-session averages are the totals\n    over session counts. This claim selects the neurons other claims use. Reproduced when, under\n    every reading, at least 10 of the 12 counts are within tolerance; partially reproduced when at\n    least 6 are. The counts under each reading are shown.\n- id: fig2d-task-relevant-proportions\n  statement: Task-relevant neurons made up 41.3, 33.8 and 20.0% of active neurons in PPC layers 2,\n    3 and 5 and 19.6, 16.7 and 5.70% in PM, more in PPC than in PM in every layer.\n  source: Results, Goal-distance representation in PPC and PM, paragraph 5; Figure 2d\n  quote: Among active neurons (99.6% of all neurons; Supplementary Table 1), the proportions of\n    task-relevant neurons in layers 2, 3 and 5 were 41.3, 33.8 and 20.0% in PPC, and 19.6, 16.7\n    and 5.70% in PM, indicating that more neurons were recruited to the task in PPC than PM\n  statistics:\n  - about: layer 2\n    test: Mann-Whitney U test\n    statistic: z = 3.58\n    p: 3.38e-4\n  - about: layer 3\n    test: Mann-Whitney U test\n    statistic: z = 2.32\n    p: 0.0202\n  - about: layer 5\n    test: Mann-Whitney U test\n    statistic: z = 3.63\n    p: 2.81e-4\n  expected:\n  - quantity: task-relevant, PPC layer 2\n    value: 41.3\n    tolerance: 4.13\n    unit: '%'\n  - quantity: task-relevant, PPC layer 3\n    value: 33.8\n    tolerance: 3.38\n    unit: '%'\n  - quantity: task-relevant, PPC layer 5\n    value: 20.0\n    tolerance: 2.0\n    unit: '%'\n  - quantity: task-relevant, PM layer 2\n    value: 19.6\n    tolerance: 1.96\n    unit: '%'\n  - quantity: task-relevant, PM layer 3\n    value: 16.7\n    tolerance: 1.67\n    unit: '%'\n  - quantity: task-relevant, PM layer 5\n    value: 5.70\n    tolerance: 0.57\n    unit: '%'\n  depends_on:\n  - neuron-classes\n  criterion: Task relevance as in neuron-classes (O1, O2). Percentages under the two readings of\n    O5 (Fig. 2d shows pooled counts 3,497, 2,376, 1,045 and 1,533, 1,180, 317 task-relevant\n    neurons, which fit reading (b) within 2%). Mann-Whitney U over per-session proportions, PPC\n    against PM per layer. Reproduced when, under one O5 reading, all six values are within\n    tolerance and, under every method reading, PPC exceeds PM with P < 0.05 in all three layers.\n- id: fig2d-goal-distance-ppc-more\n  statement: PPC had more goal-distance neurons than PM in all three layers.\n  source: Results, Goal-distance representation in PPC and PM, paragraph 5; Figure 2d\n  quote: PPC had more goal-distance neurons than PM in all layers (Mann-Whitney U test, P = 0.00415,\n    0.0152 and 4.98 × 10−4, z = 2.87, 2.43 and 3.48, respectively; Fig. 2d)\n  statistics:\n  - about: layer 2\n    test: Mann-Whitney U test\n    statistic: z = 2.87\n    p: 0.00415\n  - about: layer 3\n    test: Mann-Whitney U test\n    statistic: z = 2.43\n    p: 0.0152\n  - about: layer 5\n    test: Mann-Whitney U test\n    statistic: z = 3.48\n    p: 4.98e-4\n  depends_on:\n  - neuron-classes\n  criterion: Per-session proportion of goal-distance neurons among active neurons, PPC against PM\n    per layer, Mann-Whitney U over sessions. Reproduced when, under every reading of O1 to O3,\n    PPC is higher with P < 0.05 in all three layers.\n- id: fig2d-after-vs-before\n  statement: PPC had more after-reaching than before-reaching neurons in every layer, whereas PM\n    tended the other way, significantly in layer 2.\n  source: Results, Goal-distance representation in PPC and PM, paragraph 5; Figure 2d\n  quote: PPC had more after-reaching neurons than before-reaching neurons (Wilcoxon signed-rank\n    test, P = 0.0319, 0.00568 and 0.0176, z = 2.15, w = 13.5 and 9.5), whereas PM had the opposite\n    tendency (P = 0.00771, 0.287 and 0.427, z = 2.66, w = 70 and 57.5)\n  statistics:\n  - about: PPC layer 2\n    test: Wilcoxon signed-rank test\n    statistic: z = 2.15\n    p: 0.0319\n  - about: PPC layer 3\n    test: Wilcoxon signed-rank test\n    statistic: w = 13.5\n    p: 0.00568\n  - about: PPC layer 5\n    test: Wilcoxon signed-rank test\n    statistic: w = 9.5\n    p: 0.0176\n  - about: PM layer 2\n    test: Wilcoxon signed-rank test\n    statistic: z = 2.66\n    p: 0.00771\n  - about: PM layer 3\n    test: Wilcoxon signed-rank test\n    statistic: w = 70\n    p: 0.287\n  - about: PM layer 5\n    test: Wilcoxon signed-rank test\n    statistic: w = 57.5\n    p: 0.427\n  depends_on:\n  - neuron-classes\n  criterion: Per session, counts (or proportions, O5) of after-reaching and before-reaching\n    neurons, paired over sessions, two-sided signed-rank test per area and layer. Reproduced\n    when, under every reading of O1 to O3, after-reaching exceeds before-reaching in all PPC\n    layers with P < 0.05, and in PM before-reaching exceeds after-reaching in layer 2 with\n    P < 0.05 and PM layers 3 and 5 do not show PPC's direction significantly.\n- id: fig2d-layer-distance-preference\n  statement: In both PPC and PM, goal-distance neurons in layers 3 and 5 preferred distances closer\n    to the goal than those in layer 2; layers 3 and 5 did not differ.\n  source: Figure 2d insets and legend; Results, Goal-distance representation in PPC and PM,\n    paragraph 5\n  quote: in both areas, goal-distance neurons in layers 3 and 5 were more tuned to the distance\n    near the goal than those in layer 2 (Mann-Whitney U test, P = 0.00319 to 2.25 × 10−16)\n  statistics:\n  - about: PPC, layer 2 against 3\n    test: Mann-Whitney U test\n    statistic: z = 8.21\n    p: 2.25e-16\n  - about: PPC, layer 2 against 5\n    test: Mann-Whitney U test\n    statistic: z = 4.88\n    p: 1.07e-6\n  - about: PPC, layer 3 against 5\n    test: Mann-Whitney U test\n    statistic: z = 1.43\n    p: 0.154\n  - about: PM, layer 2 against 3\n    test: Mann-Whitney U test\n    statistic: z = 3.18\n    p: 0.00147\n  - about: PM, layer 2 against 5\n    test: Mann-Whitney U test\n    statistic: z = 2.95\n    p: 0.00319\n  - about: PM, layer 3 against 5\n    test: Mann-Whitney U test\n    statistic: z = 1.15\n    p: 0.252\n  depends_on:\n  - neuron-classes\n  criterion: Distance preference per goal-distance neuron (O4), Mann-Whitney U over neurons between\n    layers within each area, Bonferroni threshold P < 0.01 (Statistics, Fig. 2d). Reproduced\n    when, under every reading of O1 to O3, layers 3 and 5 each have smaller preferred distances\n    than layer 2 with P < 0.01 in both areas. The layer 3 against 5 comparisons are shown.\n- id: fig3b-distance-over-time\n  statement: In PPC and PM, more goal-distance neurons were best fit by goal distance than by the\n    time to reach the goal.\n  source: Figure 3b; Results, Goal-distance representation in PPC and PM, paragraph 7\n  quote: More neurons represented the goal distance than the time to goal in PPC and PM (Wilcoxon\n    signed-rank test, P = 0.00348 to 4.33 × 10−4)\n  statistics:\n  - about: PPC layers 2, 3, 5\n    test: Wilcoxon signed-rank test\n    statistic: w = 136, 108.5, 87\n    p: 0.00348\n  - about: PM layers 2, 3, 5\n    test: Wilcoxon signed-rank test\n    statistic: w = 135, 112, 101\n    p: 0.00153\n  depends_on:\n  - neuron-classes\n  criterion: Single-neuron regression with BIC selection over the 11 variable sets (opening\n    comment; O6). A neuron represents distance when its best set contains distance, and time\n    when it contains time. Per session, counts of distance and of time neurons among\n    goal-distance neurons, paired two-sided signed-rank test over sessions per area and layer.\n    Reproduced when, under every reading, distance neurons outnumber time neurons with P < 0.01\n    in all six area-layer groups.\n- id: supp6-distance-not-sound\n  statement: Goal-distance and after-reaching neurons were fit better by goal distance than by a\n    distance held constant during no-sound zones or by the sound intensity.\n  source: Supplementary Figure 6; Results, Goal-distance representation in PPC and PM, paragraph 8\n  quote: RMSE of Distance was significantly smaller than of other variables both in goal-distance\n    neurons and after-reaching neurons, indicating goal distance representation\n  statistics:\n  - about: all comparisons (range 0.0428 to 0)\n    test: Wilcoxon signed-rank test\n    statistic: z = 2.03 to 27.0\n    p: 0.0428\n  depends_on:\n  - neuron-classes\n  criterion: Per neuron, y(t) = b0 + b1 phi(variable(t)) with the Gaussian basis of equation (3),\n    variable Distance, Step (goal distance held at its value on entering each no-sound zone) or\n    Sound (intensity, 100 dB SPL at 25 cm and 6 dB lower per doubling of distance; Online\n    Methods). Intensity during no-sound zones and below 25 cm is not given; readings (a) zero\n    during no-sound zones and the formula below 25 cm with distance floored at 0.42 cm; (b) the\n    same with intensity capped at 100 dB below 25 cm. Frames as O6. RMSE of each fit, paired\n    signed-rank test over neurons, Distance against Step and against Sound, for goal-distance\n    and for after-reaching neurons in each area and layer. Reproduced when, under every reading,\n    Distance has the lower RMSE with P < 0.05 in all 24 comparisons; partially when in at least\n    20.\n- id: tuning-similar-ppc-pm\n  statement: The distance tuning curves of goal-distance neurons, as fitted coefficients, did not\n    differ between PPC and PM.\n  source: Results, Goal-distance representation in PPC and PM, paragraph 8\n  quote: Fitted coefficients for goal-distance representation revealed that the distance tuning\n    curves of neurons were similar between PPC and PM (Online Methods; Mann-Whitney U test, P =\n    0.268 to 0.106, z = 1.11 to 1.62)\n  statistics:\n  - about: PPC against PM, per layer (smallest P of the range)\n    test: Mann-Whitney U test\n    statistic: z = 1.11 to 1.62\n    p: 0.106\n  depends_on:\n  - neuron-classes\n  criterion: A claim of absence. The coefficient compared is not named; the fit is the distance\n    model of equation (2) for goal-distance neurons. Readings (a) the width s of the distance\n    basis; (b) the distance coefficient b1. Mann-Whitney U over neurons, PPC against PM per layer,\n    two-sided. Reproduced when no layer differs with P < 0.05; not reproduced when any does;\n    effect sizes are shown. If the readings disagree the claim is blocked as\n    methods_underspecified.\n- id: fig3c-continuous-ramp\n  statement: In the continuous condition, after-reaching neurons increased their activity as mice\n    approached the goal, in both PPC and PM.\n  source: Figure 3c; Results, PPC represents goal distance estimated from action, paragraph 1\n  quote: Activity in the continuous condition gradually increased in both PPC and PM as mice\n    approached the goal (Wilcoxon signed-rank test, P = 0.00507 to 0, z = 2.80 to 25.0; Fig. 3c,\n    and Supplementary Figs. 7 and 8a)\n  statistics:\n  - about: all area, layer and zone tests (largest P)\n    test: Wilcoxon signed-rank test\n    statistic: z = 2.80 to 25.0\n    p: 0.00507\n  depends_on:\n  - neuron-classes\n  criterion: Per after-reaching neuron, its trial-averaged dR/R in the condition, binned every\n    0.42 cm (equation 5); whether the 8.37 cm moving average of the classification is applied\n    first is not said, readings (a) not applied, (b) applied. Slope of activity against approach\n    in the zones 25.1-8.4 and 8.4-0 cm (Supplementary Fig. 8a), signed-rank test of slopes\n    against zero over neurons per area and layer. Reproduced when, under every reading, the\n    median slope is positive (activity rising toward the goal) with P < 0.01 in all 12 area,\n    layer and zone tests.\n- id: fig3c-ppc-ramp-without-sound\n  statement: In the intermittent conditions, PPC after-reaching neurons in all layers increased\n    activity toward the goal both with and without sound.\n  source: Figure 3c; Supplementary Figure 8a; Results, PPC represents goal distance estimated from\n    action, paragraph 1\n  quote: In intermittent conditions, increased activity was observed with and without sound inputs\n    in all PPC layers (sound zones, P = 1.37 × 10−4 to 0, z = 3.81 to 23.2; no-sound zones, P =\n    1.19 × 10−6 to 0, z = 4.86 to 17.9)\n  statistics:\n  - about: PPC, sound zones (largest P)\n    test: Wilcoxon signed-rank test\n    statistic: z = 3.81 to 23.2\n    p: 1.37e-4\n  - about: PPC, no-sound zones (largest P)\n    test: Wilcoxon signed-rank test\n    statistic: z = 4.86 to 17.9\n    p: 1.19e-6\n  depends_on:\n  - neuron-classes\n  criterion: Slopes as in fig3c-continuous-ramp (both readings), in intermittent 1 and 2 trials,\n    zones 25.1-8.4 and 8.4-0 cm (one with and one without sound in each condition). Reproduced\n    when, under every reading, the median slope is positive with P < 0.01 in all 12 PPC tests\n    (3 layers, 2 conditions, 2 zones).\n- id: supp8a-pm-no-sound\n  statement: In PM, after-reaching neurons showed positive slopes in some no-sound zones, but in\n    the intermittent 1 condition their slopes without sound were not significantly positive.\n  source: Supplementary Figure 8a; Results, PPC represents goal distance estimated from action,\n    paragraph 1\n  quote: Slopes were significantly positive with and without sound in PPC in all conditions, but in\n    PM in intermittent 1 condition they were not significantly positive without sound.\n  statistics:\n  - about: PM, without sound (range 0.497 to 9.97e-10)\n    test: Wilcoxon signed-rank test\n    statistic: z = 0.679 to 6.11\n    p: 0.497\n  depends_on:\n  - neuron-classes\n  criterion: Slopes as in fig3c-continuous-ramp, PM after-reaching neurons, no-sound zones\n    (intermittent 1, 8.4-0 cm; intermittent 2, 25.1-8.4 cm), signed-rank against zero, P < 0.01\n    (the legend's threshold). Reproduced when, under every reading, at least one PM no-sound test\n    is positive with P < 0.01 in intermittent 2, and in intermittent 1 at least one PM layer is\n    not significantly positive. Per layer results are shown.\n- id: supp8b-slopes-lower-without-sound\n  statement: Slopes of after-reaching activity were lower without sound than with sound.\n  source: Supplementary Figure 8b\n  quote: Although slopes were significantly positive even without sound in a, they were less steep\n    than those with sound\n  statistics:\n  - about: PPC, all layers\n    test: Wilcoxon signed-rank test\n    p: 0\n  - about: PM layer 5, largest P\n    test: Wilcoxon signed-rank test\n    statistic: z = 1.56\n    p: 0.118\n  depends_on:\n  - neuron-classes\n  criterion: For each after-reaching neuron and zone (25.1-8.4 and 8.4-0 cm), the slope with sound\n    (from the condition with sound in that zone) against without (the other intermittent\n    condition), paired signed-rank over neurons. Reproduced when, under every reading of\n    fig3c-continuous-ramp, the slope without sound is lower with P < 0.01 in all six PPC\n    comparisons and in at least four of six PM comparisons (the paper reports five).\n- id: supp8c-ppc-steeper-than-pm\n  statement: Without sound, PPC after-reaching neurons in layers 2 and 3 had steeper slopes than\n    PM, while slopes in PM were equal to or lower than in PPC.\n  source: Supplementary Figure 8c; Results, PPC represents goal distance estimated from action,\n    paragraph 1\n  quote: In layers 2 and 3, PPC had steeper slopes than PM without sound\n  statistics:\n  - about: layer 3, 25.1-8.4 cm (intermittent 2)\n    test: Mann-Whitney U-test\n    statistic: z = 7.62\n    p: 2.60e-14\n  - about: layer 3, 8.4-0 cm (intermittent 1)\n    test: Mann-Whitney U-test\n    statistic: z = 4.69\n    p: 2.79e-6\n  - about: layer 2, 8.4-0 cm (intermittent 1)\n    test: Mann-Whitney U-test\n    statistic: z = 2.95\n    p: 0.00320\n  depends_on:\n  - neuron-classes\n  criterion: No-sound slopes per neuron as in supp8b-slopes-lower-without-sound, PPC against PM\n    neurons per layer and zone, Mann-Whitney U. Which of the two P values per zone and layer is\n    with sound is read from the legend order (with, without). Reproduced when, under every\n    reading, PPC no-sound slopes exceed PM with P < 0.05 in layer 3 in both zones and in layer 2\n    in at least one zone, and PM is significantly steeper in no comparison.\n- id: supp9-preserved-representation\n  statement: PPC neurons kept the distance preference they had in the continuous condition in the\n    intermittent conditions, especially near the goal, more than PM neurons did.\n  source: Supplementary Figure 9b; Results, PPC represents goal distance estimated from action,\n    paragraph 2\n  quote: PPC neurons preserved the distance representation, especially near the goal, significantly\n    more than neurons in PM (Mann-Whitney U test, P = 0.0429 to 6.82 × 10−14, z = 2.02 to 7.49)\n  statistics:\n  - about: significant comparisons, range 0.0429 to 6.82e-14\n    test: Mann-Whitney U test\n    statistic: z = 2.02 to 7.49\n    p: 0.0429\n  depends_on:\n  - neuron-classes\n  criterion: Per goal-distance neuron, the absolute difference between its distance preference\n    (O4) in continuous trials and in intermittent 1 (and 2) trials; PPC against PM per layer and\n    neuron group, Mann-Whitney U. Groups as Supplementary Fig. 9a, before-reaching neurons in four\n    groups by continuous preference and after-reaching neurons; the four groups' borders are not\n    given, readings (a) equal 16.75 cm quarters of 67 to 0 cm, (b) the zone borders 58.6, 25.1 and\n    8.4 cm. Reproduced when, under every reading, in intermittent 1 PPC after-reaching neurons\n    have the smaller difference with P < 0.05 in at least one layer, and PM has a significantly\n    smaller difference in no comparison. \"Especially near the goal\" is read as the after-reaching\n    group, the one nearest the goal.\n- id: fig4-above-chance\n  statement: Decoders built from goal-distance neurons estimated goal distance above chance in both\n    PPC and PM.\n  source: Results, Distance prediction with dynamic Bayesian inference, paragraph 3; Figure 4b\n  quote: Both areas estimated the goal distances reliably above chance level (Wilcoxon signed rank\n    test, P = 0, z = 181 to 439)\n  statistics:\n  - test: Wilcoxon signed rank test\n    statistic: z = 181 to 439\n    p: 0\n  depends_on:\n  - neuron-classes\n  criterion: Decoder of the opening comment (O7, O8). Chance level is not defined. The z values\n    imply a paired test over frames. Readings of chance (a) the RMSE of the flat prior over 0 to\n    67 cm at each frame; (b) the RMSE of a decoder whose training trials have their distances\n    permuted across trials. Paired signed-rank test of decoder RMSE against chance over frames,\n    per area, layer and condition. Reproduced when, under every reading, decoder RMSE is lower\n    with P < 0.01 in all 18 settings.\n- id: fig4c-ppc-lower-error\n  statement: The decoding error (RMSE) from layer 2 neurons was lower in PPC than in PM.\n  source: Figure 4c; Results, Distance prediction with dynamic Bayesian inference, paragraph 3\n  quote: the estimation in PPC had significantly less deviation from the actual distance than in PM\n    (Mann-Whitney U-test in layer 2, P = 0.00765 to 0, z = 2.67 to 17.1)\n  statistics:\n  - about: significant bins, layer 2, range 0.00765 to 0\n    test: Mann-Whitney U-test\n    statistic: z = 2.67 to 17.1\n    p: 0.00765\n    n: trials, PPC and PM; continuous 1,785 and 1,721, intermittent 1 398 and 362, intermittent 2\n      367 and 317\n  depends_on:\n  - neuron-classes\n  criterion: Per trial, mean RMSE within each goal-distance bin (O8), PPC trials against PM trials\n    per bin and condition, Mann-Whitney U, P < 0.01 (legend threshold). The legend's ranges\n    (continuous P = 0.893 to 0) show that not every bin differs. Reproduced when, under every\n    reading, in each condition PPC has the lower median RMSE in more than half of the bins and\n    significantly lower RMSE in at least one, and PM is significantly lower in no bin. Layers 3\n    and 5 (Supplementary Fig. 10) are shown.\n- id: fig4d-map-near-goal\n  statement: PPC and PM gave similar MAP estimates, but near the goal PPC estimates were better than\n    PM.\n  source: Figure 4d; Results, Distance prediction with dynamic Bayesian inference, paragraph 3\n  quote: PPC and PM had similar MAP estimates, but the estimations near the goal were better in PPC\n    than in PM (P = 0.00549 to 2.47× 10−11, z = 2.78 to 6.68; Fig. 4d)\n  statistics:\n  - about: significant bins near the goal, range 0.00549 to 2.47e-11\n    test: Mann-Whitney U test\n    statistic: z = 2.78 to 6.68\n    p: 0.00549\n  depends_on:\n  - neuron-classes\n  criterion: Per trial, mean MAP within each bin (O8), PPC against PM, Mann-Whitney U per bin,\n    layer 2, P < 0.01. \"Near the goal\" is read as the bins between 8.4 and 0 cm. Reproduced\n    when, under every reading, in the continuous condition at least one bin in 8.4-0 cm has PPC\n    MAP closer to the actual distance with P < 0.01 and no bin in that range has PM closer with\n    P < 0.01.\n- id: fig4e-ppc-lower-uncertainty\n  statement: The uncertainty (posterior s.d.) of distance estimates was lower in PPC than in PM at\n    every goal distance and in every condition.\n  source: Figure 4e; Results, Distance prediction with dynamic Bayesian inference, paragraph 3\n  quote: uncertainty of distance estimation was significantly less in PPC than PM (P = 1.09 × 10−12\n    to 0, z = 7.12 to 22.9; Fig. 4e)\n  statistics:\n  - about: all bins, largest P\n    test: Mann-Whitney U test\n    statistic: z = 7.12 to 22.9\n    p: 1.09e-12\n  depends_on:\n  - neuron-classes\n  criterion: Per trial, mean posterior s.d. within each bin (O8), PPC against PM per bin and\n    condition, layer 2, Mann-Whitney U. Reproduced when, under every reading, PPC is lower with\n    P < 0.01 in every bin of every condition; partially when in at least 90% of bins. Layers 3\n    and 5 (Supplementary Fig. 10) are shown.\n- id: supp11-sound-reduces-error\n  statement: Decoding errors decreased with sound and increased without it, so RMSE was lower in\n    sound zones than in no-sound zones.\n  source: Supplementary Figure 11c; Results, Distance prediction with dynamic Bayesian inference,\n    paragraph 3\n  quote: Decoding errors decreased with sound and increased without sound (Mann-Whitney U test, P =\n    0.00295 to 1.56 × 10−6, z = 2.97 to 4.80; Supplementary Fig. 11)\n  statistics:\n  - about: PPC layers 2, 3, 5\n    test: Mann-Whitney U-test\n    statistic: z = 4.23, 2.97, 4.80\n    p: 0.00295\n  - about: PM layer 5 (not significant)\n    test: Mann-Whitney U-test\n    statistic: z = 1.32\n    p: 0.188\n  depends_on:\n  - neuron-classes\n  criterion: Supplementary Fig. 11. Per session, the difference of median RMSE between each\n    intermittent condition and the continuous condition in 0.42-cm bins; linear regression of\n    that difference on distance within each zone; slopes of sound zones against no-sound zones,\n    Mann-Whitney U over zones (n = 4 zones per session, as the legend's 68 = 17 x 4). Which four\n    zones: the two zones of Fig. 5b,d in each intermittent condition. Reproduced when, under every\n    reading, RMSE rises more steeply (or falls less) without sound with P < 0.01 in all PPC\n    layers.\n- id: fig5a-map-follows-continuous\n  statement: In the continuous condition, decoded MAP distances followed the actual distance in all\n    layers of PPC and PM.\n  source: Figure 5a; Results, Distance prediction with dynamic Bayesian inference, paragraph 4\n  quote: In the continuous condition, MAPs followed the actual distances in all layers of PPC and PM\n    (Wilcoxon signed-rank test, P = 9.56 × 10−14 to 0, z = 7.45 to 34.1; Fig. 5a)\n  statistics:\n  - about: all zones, largest P\n    test: Wilcoxon signed-rank test\n    statistic: z = 7.45 to 34.1\n    p: 9.56e-14\n  depends_on:\n  - neuron-classes\n  criterion: Per trial and zone (O8, four zones), MAP decrease per cm (equation 10); signed-rank\n    test of slopes against zero over trials. Reproduced when, under every reading, the median\n    slope is positive with P < 0.01 in all 24 area, layer and zone tests.\n- id: fig5a-map-decreases-without-sound\n  statement: In the intermittent conditions, MAPs decreased with and without sound in most zones,\n    and in every zone in PPC layers 3 and 5.\n  source: Figure 5a; Results, Distance prediction with dynamic Bayesian inference, paragraph 4;\n    Discussion, paragraph 3\n  quote: In intermittent conditions, MAPs decreased with and without sound inputs in most distance\n    zones, and especially in all zones in PPC layers 3 and 5 (sound zones, P = 0.00293 to 0, z =\n    2.98 to 14.7; no-sound zones, P = 6.59 × 10−4 to 0, z = 3.41 to 8.56)\n  statistics:\n  - about: sound zones, largest P\n    test: Wilcoxon signed-rank test\n    statistic: z = 2.98 to 14.7\n    p: 0.00293\n  - about: no-sound zones, largest P\n    test: Wilcoxon signed-rank test\n    statistic: z = 3.41 to 8.56\n    p: 6.59e-4\n  depends_on:\n  - neuron-classes\n  criterion: As fig5a-map-follows-continuous, in intermittent 1 and 2 trials. Reproduced when,\n    under every reading, in PPC layers 3 and 5 every zone of both conditions (16 tests) has a\n    positive median slope with P < 0.01, and over all 48 tests more than half do.\n- id: fig5b-map-slope-lower-without-sound\n  statement: MAP slopes were shallower without sound than with sound.\n  source: Figure 5b; Results, Distance prediction with dynamic Bayesian inference, paragraph 4\n  quote: Slopes of MAPs without sound were lower than those with sound (Mann-Whitney U test, P =\n    5.14 × 10−12 to 0; Fig. 5b)\n  statistics:\n  - about: range of the significant comparisons\n    test: Mann-Whitney U test\n    p: 5.14e-12\n  - about: PM layer 5, 25.1-8.4 cm\n    test: Mann-Whitney U test\n    statistic: z = 1.17\n    p: 0.241\n  depends_on:\n  - neuron-classes\n  criterion: Per trial MAP slopes in the zones 25.1-8.4 and 8.4-0 cm; for each zone, trials of the\n    condition with sound there against trials of the one without, Mann-Whitney U (Fig. 5b\n    legend). Reproduced when, under every reading, the no-sound slope is lower with P < 0.01 in\n    all six PPC comparisons and in at least four of six PM comparisons.\n- id: fig5-layer3-steeper-than-layer2\n  statement: In intermittent 1, without sound between 8.4 and 0 cm, MAPs decreased more steeply in\n    PPC layer 3 than layer 2, while the s.d. of the estimates did not differ between these layers.\n  source: Results, Distance prediction with dynamic Bayesian inference, paragraph 4\n  quote: In the intermittent 1 condition, the decrease of MAPs in PPC layer 3 was significantly\n    steeper than that in layer 2 without sound between 8.4 and 0 cm (Mann-Whitney U test, P =\n    0.00685, z = 2.70), whereas the s.d. of distance estimation showed no significant difference\n    (P = 0.247, z = 1.16)\n  statistics:\n  - about: MAP slope, layer 3 against layer 2\n    test: Mann-Whitney U test\n    statistic: z = 2.70\n    p: 0.00685\n  - about: s.d. slope, layer 3 against layer 2\n    test: Mann-Whitney U test\n    statistic: z = 1.16\n    p: 0.247\n  depends_on:\n  - neuron-classes\n  criterion: Per trial MAP slope and s.d. slope (equation 10) in intermittent 1 trials, zone 8.4-0\n    cm, PPC layer 3 trials against layer 2 trials, Mann-Whitney U. The s.d. part is a claim of\n    absence judged at P < 0.05. Reproduced when, under every reading, the layer 3 MAP slope is\n    steeper with P < 0.05 and the s.d. slopes do not differ with P < 0.05.\n- id: supp13-map-speed\n  statement: During no-sound zones, decoded MAPs fell faster in fast-locomotion trials than in slow\n    ones.\n  source: Supplementary Figure 13; Results, Distance prediction with dynamic Bayesian inference,\n    paragraph 4\n  quote: Slopes of MAPs were steeper in fast trials than slow trials, suggesting action-dependent\n    distance prediction of mice\n  statistics:\n  - about: PPC layer 2, intermittent 1 and 2\n    test: Mann-Whitney U-test\n    statistic: z = 3.54, 3.33\n    p: 8.60e-4\n  - about: PPC layer 3, intermittent 1 and 2\n    test: Mann-Whitney U-test\n    statistic: z = 2.98, 3.05\n    p: 0.00284\n  - about: PPC layer 5, intermittent 1 and 2\n    test: Mann-Whitney U-test\n    statistic: z = 1.71, 0.883\n    p: 0.377\n  depends_on:\n  - neuron-classes\n  criterion: Per trial, MAP regressed on time within no-sound zones (y(t) = b0 + b1 t); trials\n    split into slow and fast halves (O9); fast against slow trials per area, layer and condition,\n    Mann-Whitney U. Reproduced when, under every reading, fast trials have the steeper median\n    slope with P < 0.05 in PPC layers 2 and 3 in both conditions; the other eight tests are\n    shown (the paper reports PM significant in intermittent 1 only).\n- id: fig5cd-uncertainty-updating\n  statement: In all PPC layers, between 25.1 and 0 cm, uncertainty of the estimated distance fell\n    more steeply with sound than without, the updating step of dynamic Bayesian inference.\n  source: Figure 5c,d; Results, Distance prediction with dynamic Bayesian inference, paragraph 4;\n    Discussion, paragraph 3\n  quote: Uncertainty of estimated distance decreased with sound inputs compared with no sound in all\n    layers of PPC between 25.8 and 0 cm (P = 0.0153 to 6.92 × 10−11; Fig. 5c,d)\n  statistics:\n  - about: PPC layer 2, 25.1-8.4 and 8.4-0 cm\n    test: Mann-Whitney U test\n    statistic: z = 5.34, 3.29\n    p: 9.92e-4\n  - about: PPC layer 3, 25.1-8.4 and 8.4-0 cm\n    test: Mann-Whitney U test\n    statistic: z = 2.42, 2.86\n    p: 0.0153\n  - about: PPC layer 5, 25.1-8.4 and 8.4-0 cm\n    test: Mann-Whitney U test\n    statistic: z = 6.52, 2.98\n    p: 0.00285\n  depends_on:\n  - neuron-classes\n  criterion: Per trial s.d.-of-posterior slopes (decrease per cm, equation 10) in the zones\n    25.1-8.4 and 8.4-0 cm, sound trials against no-sound trials per zone as in\n    fig5b-map-slope-lower-without-sound, Mann-Whitney U. Reproduced when, under every reading,\n    the decrease is larger with sound with P < 0.05 in all six PPC comparisons. PM results are\n    shown (the paper reports them mixed).\n- id: lognormal-decoder-better\n  statement: The decoder with a log-normal likelihood estimated goal distance better than one with\n    a Gaussian likelihood in 17 of 18 settings, all but PM layer 5 in the continuous condition.\n  source: Online Methods, Probabilistic decoding of goal distance, paragraph 3\n  quote: The decoder with log-normal distribution gave better estimates for goal distance than that\n    with a Gaussian distribution in the 18 settings ... except for layer 5 in PM in continuous\n    condition (P = 0.834, z = 0.209)\n  statistics:\n  - about: 17 settings, largest P\n    test: Wilcoxon signed rank test\n    statistic: z = 2.74 to 31.9\n    p: 0.00609\n  - about: PM layer 5, continuous\n    test: Wilcoxon signed rank test\n    statistic: z = 0.209\n    p: 0.834\n  depends_on:\n  - neuron-classes\n  criterion: The same decoder with a Gaussian likelihood of raw activity (mean and s.d. per bin as\n    for the log-normal). \"Better\" is not defined; readings (a) lower RMSE, (b) lower absolute\n    MAP error, paired over frames (the z values imply frames), signed-rank test per setting\n    (3 layers x 2 areas x 3 conditions). Reproduced when, under every reading, the log-normal\n    decoder is better with P < 0.01 in at least 16 of the 18 settings.\n- id: svm-correlations\n  statement: An SVM decoder trained on recorded data did not estimate distance better than one\n    trained on trial-shuffled data, except in one setting, so ignoring correlations between\n    neurons cost the decoder little.\n  source: Online Methods, Probabilistic decoding of goal distance, paragraph 7\n  quote: Recorded-SVM did not estimate distance better than shuffled-SVM (one-sided Wilcoxon\n    signed-rank test, P = 0.957 to 1, z = 1.71 to 12.5), except in 1 setting (layer 3 in PM in\n    intermittent1 condition, P = 0.00572, z = 2.53)\n  statistics:\n  - about: 17 settings, smallest P\n    test: one-sided Wilcoxon signed-rank test\n    statistic: z = 1.71 to 12.5\n    p: 0.957\n  - about: PM layer 3, intermittent 1\n    test: one-sided Wilcoxon signed-rank test\n    statistic: z = 2.53\n    p: 0.00572\n  depends_on:\n  - neuron-classes\n  criterion: A claim of absence. SVM (Matlab) on goal-distance neurons' activity, trained and\n    validated as the probabilistic decoder; the shuffled set permutes each neuron's activity\n    across training trials at the same goal distance. Kernel, classes and error measure are not\n    given; readings (a) linear multiclass SVM over 4.2-cm distance bins, error the absolute\n    difference of the predicted bin centre from the actual distance; (b) linear SVM regression,\n    absolute error. One-sided signed-rank test (recorded better) over frames per setting.\n    Reproduced when, under every reading, no more than one of the 18 settings shows the recorded\n    SVM better with P < 0.01; not reproduced when more do.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001605/10.1038-nn.4390.yaml paper/10.1038-nn.4390.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001605/10.1038-nn.4390.yaml",
 "old_string": "Which four\n    zones: the two zones",
 "new_string": "The four\n    zones are read as the two zones"
}
```

```
The file claims/001605/10.1038-nn.4390.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -n "[a-z]: [a-z(]" claims/001605/10.1038-nn.4390.yaml | grep -v "^\S*:\s*#" | grep -vE "^[0-9]+:\s*(- )?[a-z_]+: " | head; python tools/claims_check.py claims/001605/10.1038-nn.4390.yaml paper/10.1038-nn.4390.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "Slope of licking" paper/10.1038-nn.4390.txt | cat -A | cut -c1-120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "licking (" paper/10.1038-nn.4390.txt | cat -A | cut -c1-200; grep -n "P = 1.27\|P = 4.26\|2.79 \|3.97 " paper/10.1038-nn.4390.txt | cat -A | cut -c1-200
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
p='claims/001605/10.1038-nn.4390.yaml'
s=open(p).read()
rep=[
("""94 sessions (PPC, 8,371, 7,108 and
    4,859 neurons from 17, 15 and 14 sessions in layers 2, 3 and 5, respectively; PM, 7,788, 7,005
    and 5,900 neurons""","""94 sessions (PPC ... 8,371, 7,108 and
    4,859 neurons from 17, 15 and 14 sessions in layers 2, 3 and 5, respectively; PM ... 7,788,
    7,005 and 5,900 neurons"""),
("""Fig. 1b; 94 sessions of 8 mice, r = 0.258""","""Fig. 1b; 94 sessions of 8 mice ... r = 0.258"""),
("""  quote: Slope of licking (1) was significantly""","""  quote: Slope of licking ... was significantly"""),
("""in all PPC layers (sound zones, P = 1.37 × 10−4 to 0, z = 3.81 to 23.2; no-sound zones, P =
    1.19 × 10−6 to 0, z = 4.86 to 17.9)""","""in all PPC layers (sound zones ... P = 1.37 × 10−4 to 0, z = 3.81 to 23.2; no-sound zones ...
    P = 1.19 × 10−6 to 0, z = 4.86 to 17.9)"""),
("""than in PM
    (Mann-Whitney U-test in layer 2""","""than in PM
    (Mann-Whitney ... U-test in layer 2"""),
("""PPC layers 3 and 5 (sound zones, P = 0.00293 to 0, z =
    2.98 to 14.7; no-sound zones, P = 6.59 × 10−4 to 0, z = 3.41 to 8.56)""","""PPC layers 3 and 5 (sound zones ... P = 0.00293 to 0, z =
    2.98 to 14.7; no-sound zones ... P = 6.59 × 10−4 to 0, z = 3.41 to 8.56)"""),
("""  - about: layer 3, 25.1-8.4 cm (intermittent 2)
    test: Mann-Whitney U-test
    statistic: z = 7.62
    p: 2.60e-14
  - about: layer 3, 8.4-0 cm (intermittent 1)
    test: Mann-Whitney U-test
    statistic: z = 4.69
    p: 2.79e-6
""","""  - about: layer 3, 25.1-8.4 cm, without sound (intermittent 2)
    test: Mann-Whitney U-test
    statistic: z = 2.45
    p: 0.0142
  - about: layer 3, 8.4-0 cm, without sound (intermittent 1)
    test: Mann-Whitney U-test
    statistic: z = 5.19
    p: 2.15e-7
"""),
("""  - about: layer 2, 8.4-0 cm (intermittent 1)""","""  - about: layer 2, 8.4-0 cm, without sound (intermittent 1)"""),
("""Which of the two P values per zone and layer is
    with sound is read from the legend order (with, without). Reproduced""","""The legend gives two P values per zone and layer;
    they are read in the order intermittent 1, intermittent 2, as the other legends list
    conditions, which puts the without-sound value second in 25.1-8.4 cm and first in 8.4-0 cm
    (the only order under which the legend supports the text's layers 2 and 3). Reproduced"""),
]
for a,b in rep:
    assert s.count(a)==1,a[:50]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/001605/10.1038-nn.4390.yaml paper/10.1038-nn.4390.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "—\|rather" claims/001605/10.1038-nn.4390.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/001605/10.1038-nn.4390.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

```
39 39 35 39 7
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
?? claims/001605/
?? scripts
```

**Agent**

I wrote `claims/001605/10.1038-nn.4390.yaml`: 39 claims, every one with a word-for-word quote. Nothing is committed. The quote checker passes every quote. It still lists five supplement p-values as not found, because the supplement prints "×" as an unreadable glyph; I read each of them in the text (1.27e-4, 9.81e-8, 4.26e-5, 2.15e-7, 8.60e-4).

**Text read:** the version of record (Nature Neuroscience, December 2016), with the Online Methods and the supplement (Supplementary Figs. 1 to 14 and Table 1). Nothing the results rest on is missing. I rendered PDF pages only to read Figs. 1c, 2c,d and 4, and the columns of Supplementary Table 1. The paper links no code (Matlab "available from corresponding author upon request"), so I read none.

**Counts:**
- 39 claims, all with quotes and criteria.
- 35 carry statistics, about 76 test entries in all.
- 7 carry expected values: session and mouse counts, neuron counts, behaviour timing, licking correlation range, sound-responsive percentages, neuron-class counts and task-relevant percentages.
- Every claim uses the dataset's own data (`data: dataset`); the paper uses no outside data.
- Six claims are muscimol and sound-mapping experiments. The archive description lists only the 94 imaging sessions, so the author must check whether these are in the dataset.

**Details the paper leaves open, with the readings named (O1 to O9 in the opening comment, plus some per claim):**
- **O1, baseline of the task-relevance t-test:** (a) zero, the session mean the signal is taken against; (b) the neuron's mean during inter-trial intervals.
- **O2, alignment windows:** read from the Fig. 2c axes. The start-aligned distance window is given nowhere: (a) 0 to 67 cm; (b) 0 to 33 cm.
- **O3, k-means feature splitting after-reaching from reward neurons:** (a) the normalized 16-frame trace before the goal; (b) its mean.
- **O4, distance preference:** the peak of the distance-aligned trace (one reading, from Fig. 2d).
- **O5, percentages:** (a) mean of per-session proportions; (b) pooled counts.
- **O6, single-neuron regression:** frames run (a) from start to goal or (b) to 3 s after it. The four initial width values are not given; two sets are named.
- **O7, positive shift before the log-normal likelihood:** the minimum set to (a) 0.01 or (b) 0.1.
- **O8, Fig. 4 bins:** 4.2 cm (tick spacing and decoder bin), or 0.42 cm. The Fig. 5 zones come from the axes.
- **O9, slow/fast split:** by (a) whole-trial or (b) zone speed. Zones analysed: (a) all no-sound zones or (b) the one nearest the goal.
- **Per claim:**
  - Fig. 1c: bin width and which bins are compared.
  - Licking correlation: Pearson or Spearman.
  - Tuning similarity: which fitted coefficient, the width s or b1.
  - Sound-intensity model: silent zones and the cap below 25 cm.
  - Chance level for decoding: flat prior, or labels permuted across trials.
  - Supp. Fig. 9: the four group borders.
  - Log-normal vs Gaussian: the measure of "better".
  - SVM: kernel, classes and error measure.
  - Behaviour timing: which no-sound zones count.

**Inconsistencies noted:**
- The text says "25.8 cm" where the figures use 25.1 cm.
- The Fig. 4c legend calls RMSE an "expected squared deviation", without the root.
- Supplementary Fig. 8c's p-value pairs only support the text when read in the order intermittent 1, then intermittent 2. I recorded that reading in the criterion.

Nothing a claim needed is missing from the paper beyond these open details. The figure pages could not be opened with the PDF reader because poppler isn't installed. I installed PyMuPDF into the temporary directory to render them; nothing in the repository changed.

## End of run

29 turns, 8 minutes, result: success.
