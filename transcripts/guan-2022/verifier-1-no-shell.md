# 000147 · verifier-1 · run 38473338726

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `CronCreate`, `CronDelete`, `CronList`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `RemoteTrigger`, `ReportFindings`, `ScheduleWakeup`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Workflow`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls docs 2>/dev/null; cat *.y*ml *.json 2>/dev/null | head -100
```

```
Sandbox is required but failed to initialize: Sandbox dependencies not available: socat not installed. Restart to retry.
```

**Agent calls Glob**

```json
{
 "pattern": "**/*"
}
```

```
reproduce_guan_2022.ipynb
10.7554-elife.74478.yaml
ppcfingers.py
.npmrc
.yarnrc.yml
.yarnrc
bunfig.toml
package.json
.gitmodules
package-lock.json
yarn.lock
pnpm-lock.yaml
.env
.env.local
.env.development
.env.development.local
.env.test
.env.test.local
.env.production
.env.production.local
```

**Agent calls Read**

```json
{
 "file_path": "10.7554-elife.74478.yaml"
}
```

```
1	# Claims for Guan, Aflalo et al. (2022) on dandiset 000147.
2	# Source: the paper's Results, figure legends and Methods (open access, eLife and PMC9555862).
3	# Written before the analysis was run.
4	schema_version: 1
5	dandiset: "000147"
6	paper: doi:10.7554/elife.74478
7	claims:
8	- id: recording-counts
9	  statement: Over 10 sessions the recordings yielded 95.8 (SD 6.7) sorted neurons and 408 (SD 40.8)
10	    trials of the main finger task per session.
11	  source: Results, "Intracortical recordings during finger flexion"
12	  expected:
13	    quantity: mean number of sorted units per session
14	    value: 95.8
15	    tolerance: 0.5
16	  criterion: The mean and SD of units per session match 95.8 and 6.7 to one decimal, and the mean
17	    and SD of trials per session match 408 and 40.8 to the nearest trial.
18	- id: fig1b-online-accuracy
19	  statement: Online BCI classification of the cued finger was 86% accurate (SD 4% across sessions,
20	    weighted by trials) over 4016 trials in 10 sessions, against a chance level of 17%. No-Go trials
[... 129 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "ppcfingers.py"
}
```

```
1	"""Data access and analysis helpers for dandiset 000147 (Guan, Aflalo et al. 2022).
2	
3	The dandiset holds the main task of the paper ("finger flexion grid") for its
4	ten sessions of participant NS (subject P1 in the files): sorted units, and a
5	trials table with the cued finger, the finger the online decoder chose, the
6	cue's grid position and the run. The calibration task and the no-movement
7	control task are not included.
8	
9	`load_session` streams one file from the DANDI Archive and reduces it as it
10	loads to spike counts per trial and unit: in the paper's analysis window, and
11	in short bins around the cue for the alignment check.
12	
13	Where parameters come from:
14	
15	- WINDOW, 0.5 to 1.5 s after the cue (the trial start time): the paper's
16	  methods, the window of the online decoder and of the offline analyses.
17	- Cross-validated Mahalanobis (crossnobis) distance with five stratified,
18	  unshuffled folds and a shrinkage (OAS) noise covariance from the residuals
19	  of each fold: the paper's methods, and the authors' code (calc_rdm.py in
20	  github.com/AndersenLab-Caltech/fingers_rsa at the commit archived with the
[... 370 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "reproduce_guan_2022.ipynb"
}
```

```
<cell id="b20ed669"><cell_type>markdown</cell_type># Reproducing Guan, Aflalo et al. (2022) from dandiset 000147

Paper: Guan C, Aflalo T, Zhang CY, Amoruso E, Rosario ER, Pouratian N, Andersen RA (2022).
Stability of motor representations after paralysis. eLife 11:e74478.
[doi:10.7554/eLife.74478](https://doi.org/10.7554/eLife.74478). The paper is open access, and its
full text, figure legends and methods were used (eLife, PMC9555862).

Data: [DANDI:000147](https://dandiarchive.org/dandiset/000147/0.221122.2256), version
0.221122.2256, streamed from the archive. The dandiset has two published versions, 0.220913.2243
and 0.221122.2256, with the same ten assets (same asset IDs and sizes). The later version is used
because its metadata names this paper; the earlier one names the bioRxiv preprint. The authors'
download script pins the earlier version, so the files are the ones the authors analysed.

## What can and cannot be tested

The paper records from a Utah array in the posterior parietal cortex (PC-IP) of one tetraplegic
participant, NS, over ten sessions on nine days, while she attempted to press the cued finger
(thumb T, index I, middle M, ring R, pinky P) or did nothing (No-Go, X). The dandiset holds the
main task of all ten sessions: sorted units, the cued finger, the online decoder's output, the
cue's grid position and the run. It does not hold the calibration task, the no-movement control
[... 693 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json
nb=json.load(open('reproduce_guan_2022.ipynb'))
for i in [5,10,18,20,22,30]:
    print('=== cell',i)
    for o in nb['cells'][i].get('outputs',[]):
        if 'text' in o: print(''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data']: print(''.join(o['data']['text/plain']))
"
```

```
Sandbox is required but failed to initialize: Sandbox dependencies not available: socat not installed. Restart to retry.
```

**Agent calls Grep**

```json
{
 "pattern": "\"name\": \"stdout\"",
 "path": "reproduce_guan_2022.ipynb",
 "output_mode": "content"
}
```

```
122:     "name": "stdout",
182:     "name": "stdout",
261:     "name": "stdout",
375:     "name": "stdout",
419:     "name": "stdout",
441:     "name": "stdout",
530:     "name": "stdout",
603:     "name": "stdout",
673:     "name": "stdout",
762:     "name": "stdout",
879:     "name": "stdout",
964:     "name": "stdout",
1064:     "name": "stdout",
1120:     "name": "stdout",
1182:     "name": "stdout",
1252:     "name": "stdout",
1370:     "name": "stdout",
```

**Agent**

Bash is unavailable here (the sandbox fails to start because `socat` is missing), so I'm reading the notebook's JSON outputs with Grep.

**Agent calls Grep**

```json
{
 "pattern": ".*",
 "path": "reproduce_guan_2022.ipynb",
 "output_mode": "content",
 "offset": 175,
 "head_limit": 110
}
```

```
176:      "2018-10-15    4.11  (0.947, 31.7)\n",
177:      "2018-10-17    6.17  (0.643, 21.2)\n",
178:      "2018-10-22    4.14  (0.529, 54.9)\n"
179:     ]
180:    },
181:    {
182:     "name": "stdout",
183:     "output_type": "stream",
184:     "text": [
185:      "\n",
186:      "Model RDMs from the authors' repository at commit 6915bf863a, pairs ['TI', 'TM', 'TR', 'TP', 'IM', 'IR', 'IP', 'MR', 'MP', 'RP']:\n",
187:      "  Able-bodied (PC-IP): [0.241 0.256 0.248 0.246 0.032 0.106 0.122 0.064 0.149 0.089]\n",
188:      "  Able-bodied (MC): [0.374 0.448 0.513 0.467 0.214 0.353 0.377 0.2   0.294 0.18 ]\n",
189:      "  unstructured: [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]\n"
190:     ]
191:    }
192:   ],
193:   "source": [
194:    "sessions = pf.load_all()\n",
195:    "names = [s.name for s in sessions]\n",
[... 92 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "^      \"",
 "path": "reproduce_guan_2022.ipynb",
 "output_mode": "content",
 "offset": 0,
 "head_limit": 0
}
```

```
<persisted-output>
Output too large (20.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/223c65c1-32e8-4dc6-b826-b730c57a7973/tool-results/toolu_019kY5pwjHGk6qWCWPVT56fi.txt

Preview (first 2KB):
125:      "Dandiset 000147, version 0.221122.2256: 10 files\n",
126:      "Subjects: ['P1']\n",
127:      "Session descriptions: ['individual-finger press, main task']\n",
128:      "session_id matches the file name in every file: True\n",
129:      "             units  electrodes_with_units  trials  runs trials_per_run decoder_outputs cue_locations\n",
130:      "2018-09-10     100                     74     384     8           [48]           IMPRT     1-12 (12)\n",
131:      "2018-09-17a     93                     73     384     8           [48]          IMPRTX     1-12 (12)\n",
132:      "2018-09-17b     88                     67     336     7           [48]          IMPRTX     1-12 (12)\n",
133:      "2018-09-24     110                     75     480    10           [48]          IMPRTX     1-12 (12)\n",
134:      "2018-09-26      95                     74     432     9           [48]          IMPRTX     1-12 (12)\n",
135:      "2018-10-01      90                     68     432     9           [48]          IMPRTX     1-12 (12)\n",
136:      "2018-10-12     100                     75     432     9           [48]          IMPRTX     1-12 (12)\n",
137:      "2018-10-15      89                     69     432     9           [48]          IMPRTX     1-12 (12)\n",
138:      "2018-10-17      99                     73     384     8           [48]          IMPRTX     1-12 (12)\n",
139:      "2018-10-22      94                     72     384     8           [48]          IMPRTX     1-12 (12)\n",
140:      "\n",
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/223c65c1-32e8-4dc6-b826-b730c57a7973/tool-results/toolu_019kY5pwjHGk6qWCWPVT56fi.txt",
 "offset": 60
}
```

```
60	264:      "             pre_start_mean  pre_start_max  first_centre_above_0.4   peak  peak_centre\n",
61	265:      "2018-09-10            0.176          0.214                     0.6  0.839          1.1\n",
62	266:      "2018-09-17a           0.177          0.224                     0.6  0.833          1.1\n",
63	267:      "2018-09-17b           0.152          0.202                     0.6  0.783          1.0\n",
64	268:      "2018-09-24            0.182          0.210                     0.6  0.850          1.1\n",
65	269:      "2018-09-26            0.173          0.204                     0.6  0.833          1.2\n",
66	270:      "2018-10-01            0.192          0.225                     0.6  0.822          1.1\n",
67	271:      "2018-10-12            0.189          0.248                     0.6  0.824          1.2\n",
68	272:      "2018-10-15            0.182          0.215                     0.6  0.824          1.1\n",
69	273:      "2018-10-17            0.168          0.201                     0.6  0.771          1.5\n",
70	274:      "2018-10-22            0.192          0.219                     0.6  0.789          1.2\n",
71	275:      "\n",
72	276:      "Plotted accuracies range from 0.119 to 0.850; none is off the axes.\n"
73	281:[Omitted long matching line]
74	282:      "text/plain": [
75	378:      "Units per session: mean 95.8, SD 6.7, range 88 to 110, total 958\n",
76	379:      "Trials per session: mean 408.0, SD 40.8, range 336 to 480, total 4080\n"
77	422:      "             trials  accuracy\n",
78	423:      "session                      \n",
79	424:      "2018-09-10      320     0.838\n",
[... 204 more lines not kept]
```

**Agent**

I have all the notebook outputs. Next I'll fetch the paper's methods to check windows, the statistics and the blocked claims.

**Agent calls ToolSearch**

```json
{
 "query": "select:WebFetch",
 "max_results": 1
}
```

Result: no output.

**Agent calls WebFetch**

```json
{
 "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9555862/",
 "prompt": "Quote verbatim (do not paraphrase) every passage about: number of neurons and trials per session; online accuracy and chance level; No-Go trials excluded in first session (how many); the 70% middle-ring/ring-pinky error statement; offline classification (window, classifier, cross-validation, 92%); calibration task accuracy; tuning analysis (t-test, FDR, 0.1 Hz, 89%); gaze/cue location controls (Figure 1-figure supplement 6 legend, including chance levels and how cue location coordinates were defined); RDM computation (crossnobis, folds, noise covariance, window); WUC, noise ceiling, bootstrap t-test p=5.7e-5 and p=1.9e-6; RDM consistency r=0.90; Figure 3a linear model session x model interaction t(6); Figure 3b/3-supplement 1 regression on session and run (t(8), t(82), Cohen's f2, BF); Methods 'Measuring changes in the representational structure'; Figure 4 muscle/somatotopy models and where these model RDMs come from; L-ratio. Also the Data availability statement."
}
```

Result: the fetched text is not kept.

**Agent calls WebFetch**

```json
{
 "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9555862/",
 "prompt": "Return verbatim, complete text of these Methods subsections and legends: (1) 'Finger classification' methods; (2) 'Single-unit tuning to finger flexion' methods; (3) 'Measuring changes in the representational structure' methods in full, including the regression equations and how the runs/sessions are indexed and degrees of freedom; (4) Figure 1—figure supplement 6 legend in full (gaze controls: regression of screen coordinates, LDA classification of cue location, control task); (5) 'Model fitting' / 'Representational dynamics' methods describing the muscle, somatotopy and hand-usage model RDMs and where they come from (e.g. Ejaz et al. 2015 data); (6) the noise covariance estimation sentence in the crossnobis methods; (7) Figure 3 legend and Figure 3—figure supplement 1 legend; (8) Data availability / code availability statement (look near end, 'Data availability')."
}
```

Result: the fetched text is not kept.

**Agent calls WebFetch**

```json
{
 "url": "https://api.dandiarchive.org/api/dandisets/000147/versions/0.221122.2256/assets/?page_size=100",
 "prompt": "List every asset path, size, and asset_id verbatim. Report the total count."
}
```

**Agent calls WebFetch**

```json
{
 "url": "https://github.com/AndersenLab-Caltech/fingers_rsa/tree/6915bf863ad1339e6fc8c6886032cd0f70fd8b10/models",
 "prompt": "List every file name in this directory verbatim."
}
```

**Agent calls WebFetch**

```json
{
 "url": "https://api.dandiarchive.org/api/dandisets/000147/versions/0.221122.2256/",
 "prompt": "Quote verbatim: description, assetsSummary (including variableMeasured, dataStandard, approach, measurementTechnique, numberOfFiles, numberOfBytes), relatedResource, and any mention of calibration task, control task, passive viewing, L-ratio, waveforms, or eye tracking/gaze."
}
```

Result: the fetched text is not kept.

Result: the fetched text is not kept.

Result: the fetched text is not kept.

**Agent calls WebFetch**

```json
{
 "url": "https://github.com/AndersenLab-Caltech/fingers_rsa/tree/6915bf863ad1339e6fc8c6886032cd0f70fd8b10",
 "prompt": "List all top-level files and directories verbatim, and quote the README sections on data, models, Ejaz, muscle, somatotopy, or usage models and where they are obtained."
}
```

Result: the fetched text is not kept.

**Agent calls Write**

```json
{
 "file_path": "paper/guan2022_excerpts.md",
 "content": "Excerpts of Guan et al. (2022) eLife 11:e74478, PMC9555862, as returned by a web fetch of\nhttps://pmc.ncbi.nlm.nih.gov/articles/PMC9555862/ on 2026-10-13 (text only, no figures).\n\nResults:\n- \"95.8 ± standard deviation [SD] 6.7 neurons per session over 10 sessions\"; \"408 ± SD 40.8 trials/session over 10 sessions\"\n- \"High classification accuracy during online control (86% ± SD 4% over 10 sessions; chance = 17%)\"\n- \"The majority (70%) of the online classification errors were middle-ring or ring-pinky confusions\"\n- \"Offline cross-validated classification (92% ± SD 2%)\"\n- \"89% neurons were significantly tuned to individual finger-press movements (significance threshold: p < 0.05, FDR-corrected)\"\n- \"p = 5.7 × 10–5, two-tailed t-test\"; \"p = 1.9 × 10–6; two-tailed t-test\"\n- \"average pairwise correlation, excluding the diagonal: r = 0.90 ± SD 0.04\"\n- Figure 3a: \"t(6) = 0.50, one-tailed t-test p = 0.32\"; Figure 3b: \"t(8) = −4.5\", \"t(82) = −0.45\"\n- Well-isolated units: \"L-ratio < 10−1.1\" (\"33% quantile\")\n\nMethods, Finger classification:\n\"To classify finger movements from firing rate vectors, we used linear discriminant analysis (LDA) with diagonal covariance matrices ... During online control of the finger flexion grid task, input features were similarly constructed by counting the threshold crossings from each electrode in a 1-s time window. This time window was fixed to [0.5, 1.5] s after cue presentation. ... The online classifier was occasionally retrained using data from this main task, usually every four run blocks.\nOffline classification accuracy was computed using leave-one-out cross-validation (within each session). We used features from the same time window as the online-control task. However, offline analyses used firing rates after spike-sorting, instead of raw threshold crossings.\nIn the Results, reported classification accuracies aggregate trials over all sessions ... Reported SDs indicate variability across sessions, weighted by the number of trials in each session. ...\nIn the first session (2018-09-10), the No-Go condition (X) was not cued in the calibration task, so the classifier did not output No-Go predictions during that session. However, No-Go was cued in the main task; these 84 No-Go trials were thus excluded from the online-control accuracy metrics, but they were included in the offline cross-validated confusion matrix.\"\n\nMethods, Single-unit tuning:\n\"We calculated the firing rate for each neuron in the window [0.5, 1.5] s after cue presentation. ... two-tailed t-test comparing each movement's firing rate to the No-Go firing rate. A neuron was considered significantly tuned to a movement if p < 0.05 (after FDR correction). ... In Figure 1—figure supplement 5, neurons were pooled across all 10 sessions. Neurons with mean firing rates less than 0.1 Hz were excluded to minimize sensitivity to discrete spike counting.\"\n\nMethods, Measuring changes in the representational structure:\n\"We first subdivided each session's dataset into individual runs and calculated separate RDMs for each (session, run) index. We then used linear regression to predict each RDM's (squared) inter-finger distances from the session index, run index, and finger pair: djk² = βjk + βsession·s + βrun·r + β0 ... For t-tests, we conservatively estimated the degrees-of-freedom as the number of RDMs, because the individual elements of each RDM covary and thus are not independent. The effect sizes for the session-index predictor and the run-index predictor were quantified using Cohen's f2, comparing against the finger-pair-only model as a baseline. ...\"\n\nCrossnobis: \"five non-overlapping subsets\"; \"The noise covariance Σ was regularized to guarantee invertibility.\"\n\nFigure 1—figure supplement 6 legend:\n\"(a) Linear regression could not decode target location [x, y] coordinates from the neural activity during the attempted-movement period. Violin plot shows that cross-validated regression r² values are close to 0 across sessions ... (b) A linear classifier (diagonal linear discriminant analysis [LDA]) could not classify the gaze location from neural activity during the attempted-movement period. Confusion matrix depicts cross-validated classifications of cue location. (c) ... a linear classifier (diagonal LDA) could not classify finger movements from neural activity during passive observation (orange) of the finger press task. Sliding bin width: 200 ms. ... (six sessions passive viewing, 10 sessions attempted flexion).\"\n\nRepresentational dynamics: \"we decomposed the data RDMs into model RDMs borrowed from Ejaz et al., 2015. The hand-usage model was constructed using the velocity time series of each finger's MCP joint during everyday tasks. The muscle activity model was constructed using EMG activity during single- and multi-finger tasks. The somatotopic model is based on a cortical sheet analogy ...\"\n\nFigure 3—figure supplement 1 legend: \"Inter-finger distances instead decreased slightly (across sessions: t(8) = −4.0, two tailed t-test p = 0.004; across runs within sessions: t(82) = −2.4, two-tailed t-test p = 0.019), although the effect size was very small (across sessions: Cohen's f2 = 0.008; across runs within sessions: = 0.005).\"\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

# Verifier report, round 1: Guan, Aflalo et al. 2022 (eLife 74478), dandiset 000147 version 0.221122.2256

Bash would not start in this session (the sandbox needs `socat`, which is not installed). So I read the notebook's outputs from its JSON with Grep, and I did not run any helper on synthetic inputs. I saved the paper excerpts to `paper/guan2022_excerpts.md`, taken from PMC9555862.

## A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| recording-counts | reproduced | Cell 9: units 95.8 (SD 6.7), trials 408.0 (SD 40.8), total 4080. All match the claim exactly. |
| fig1b-online-accuracy | reproduced | Cell 10: 0.8596 (trial-weighted SD 0.036) over 4016 trials, against 0.86 ± 0.01. Chance from shuffling is 0.169 and 1/6 is 0.167, which matches the paper's 17%. The data have 64 No-Go trials in the first session where the paper says 84, but 4080 − 64 = 4016 agrees with the paper's own total. |
| fig1b-errors-middle-ring-pinky | partially_reproduced | Cell 12: 0.697 only when errors involving No-Go are dropped from the denominator. Over all online errors the fraction is 0.468, and over errors on finger trials it is 0.592. The paper does not define the denominator, and the denominator that matches was picked after seeing the numbers. |
| fig1s4a-offline-accuracy | reproduced | Cell 14: diagonal LDA with leave-one-out gives 0.934 (weighted SD 0.016) over 4080 trials, against 0.92 ± 0.02. It sits 0.014 above the paper. The authors' 8-fold pipeline gives 0.924. |
| fig1s4b-calibration-accuracy | blocked (data_missing) | Checked in the archive: the 10 assets are all main-task files ("individual-finger press, main task"), and the dandiset metadata mentions no calibration task. |
| fig1s5-tuned-fraction | reproduced | Cell 16: 0.879 with FDR over all pooled tests, against 0.89 ± 0.05. The other FDR families give 0.875 and 0.839, also within tolerance. No unit falls below 0.1 Hz. |
| fig1s6a-gaze-regression | blocked (metadata_insufficient) | `cue_location` is an index from 1 to 12 with no description and no map to screen coordinates. The paper's legend asks for [x, y] coordinates. The test could be run under an assumed row-major 3×4 layout, but the notebook did not do this. |
| fig1s6b-gaze-classification | not_reproduced | Cell 18: pooled location accuracy is 0.1154, outside the shuffled 95% range (0.0755 to 0.0944, maximum 0.0998), with 0 of 500 shuffles reaching it. It stays above chance within-finger (0.117) and with the authors' pipeline (0.112). The finger half of the criterion holds (0.934 against 0.155 to 0.181). The effect is small (chance is 0.083) and 6 of 10 sessions are individually significant. One caveat is in B2. |
| fig1s6c-control-task | blocked (data_missing) | Checked in the archive: there is no control or passive-viewing task in any of the 10 assets or in the metadata. |
| fig2d-rdm-structure | reproduced | Cell 20: in the mean RDM the largest middle/ring/pinky distance is 0.482 and the smallest thumb distance is 0.641, so the criterion holds. It also holds in 9 of 10 individual sessions. |
| fig2f-able-bodied-over-unstructured | reproduced | Cell 22: the WUC difference is 0.0998 with bootstrap 95% CI 0.074 to 0.127. All 10 sessions favour the PC-IP model, and the bootstrap p of 4.4e-5 compares with the paper's 5.7e-5. The model RDM comes from the authors' repository, not the dandiset. |
| fig2s5-mc-over-pcip | reproduced | Cell 24: MC minus PC-IP is 0.088 with CI 0.060 to 0.112. Mean WUC with MC is 0.9686, which is at or above the lower ceiling minus 0.05 (0.9838 − 0.05 = 0.934). The p-value is 7.9e-5 here against 1.9e-6 in the paper, and only 1 of 10 sessions reaches its own lower ceiling. |
| fig2-typical-among-individuals | blocked (data_missing) | Checked: the individual fMRI RDMs are in neither the dandiset nor the authors' repository `models/` folder at commit 6915bf8, which holds only the MC, PC-IP and unstructured models. |
| rdm-consistency | reproduced | Cell 26: mean r 0.928 (SD 0.041, min 0.817, max 0.990), against 0.90 ± 0.03. This is at the edge of the tolerance and runs high. |
| fig3a-no-trend-to-unstructured | reproduced | Cell 28: interaction t(16) = 1.47, one-tailed p = 0.080, so the criterion (p > 0.05) holds. This is weaker than the paper's t(6) = 0.50, p = 0.32. The PC-IP WUC itself falls over sessions (slope −0.009, p = 0.038), which the paper does not report. |
| fig3b-confused-pairs-no-increase | reproduced | Cell 30: the session and run coefficients are negative in all six variants, with one-tailed p for an increase between 0.73 and 0.996. |
| fig3s1-all-pairs-small-decrease | reproduced | Cell 32: the session coefficient is −0.049 and the run coefficient −0.075, both negative. Cohen's f2 is 0.0064 and 0.0119, both below 0.02. In the primary variant the session decrease is not significant (t(8) = −2.28, p = 0.052, against the paper's −4.0, p = 0.004). It is significant in the shared-noise variant (p = 0.0055). |
| fig4e-muscle-before-somatotopy | blocked (data_missing) | Checked: the Ejaz et al. 2015 muscle and somatotopy RDMs are in neither the dandiset nor the repository `models/` folder. The neural side could be tested, since the files carry spike times that the notebook already bins in 50 ms steps. |
| fig4s1-model-selection | blocked (data_missing) | Same reason: the component model RDMs are not available. |
| fig4s4-well-isolated-units | blocked (data_missing) | The dandiset metadata lists only Units and ElectrodeGroup, with no L-ratio or waveforms. I did not inspect the units columns myself. The notebook's statement rests on its own reading of the files. |

## B. Problems

1. [affects a conclusion] Cell 12: the 70% figure matches only under the denominator "errors between two fingers", and that choice was made after seeing all three results. Over all errors the fraction is 47%.
2. [affects a conclusion] Cell 18, `diag_lda_cv` with `folds=8` and no `rng`: the folds are unshuffled, so each one is a block of time. Both nulls permute labels across the whole session. If cue locations are unevenly ordered across runs, slow drift could raise location accuracy, and these nulls would not control for that. A null that permutes within run, or a check that cue locations are balanced per run, is missing. The not_reproduced verdict holds by the criterion, but its cause is not established.
3. [affects a conclusion] `run_rdms`, cells 30 and 32: per-run crossnobis distances with per-fold OAS covariances average 5.06, against 0.68 for the session RDMs. The notebook explains this by folds holding only one or two trials per finger. The primary session t-values depend on this inflation: −2.28 against −3.76 with the shared covariance. The fig3s1 significance claim depends on which variant is taken as primary.
4. [does not affect a conclusion] Cells 30 and 32: the regressions use the file's `Run` values directly as the run index. The notebook never prints them, so it is unclear whether they restart at 1 in each session or are contiguous. The data hold 85 run RDMs, while the paper's t(82) implies 84 or fewer. The df of n − 2 is also an interpretation, since the paper says the df is "the number of RDMs".
5. [does not affect a conclusion] Cell 28: OLS treats the 20 WUC values as independent even though they come in pairs from the same sessions, so df = 16. The paper reports t(6), which suggests a different model.
6. [does not affect a conclusion] `load_model_rdm`: the condition-order assert runs only if `pattern_descriptors/condition` exists in the file. The notebook does not show that it ran, so the T,I,M,R,P order of the model vectors may be assumed. The printed vectors look plausible (largest distances involve the thumb, and I–M is smallest).
7. [does not affect a conclusion] `crossnobis_rdm` uses OAS shrinkage where the paper names Ledoit-Wolf (disclosed in the module docstring). Each fold pair's precision comes from the same two folds whose means it whitens. This is a minor departure, with no train/test leakage.
8. [does not affect a conclusion] Cell 24: the bootstrap p (7.9e-5) is about 40 times the paper's 1.9e-6. The paper's exact bootstrap t-test is underspecified, and the claim criterion does not depend on the p-value.
9. [does not affect a conclusion] Data checks (cells 3, 5 and 7) are sound. The decoding curve stays at chance before t = 0 and rises from about 0.6 s, which confirms that `start_time` is the cue. Unsorted spike times are sorted before counting, and no analysed trial window touches an unsorted span. The `diag_lda_fit`/`predict` code, the window counting in `load_session`, and `weighted_sd` (matching DescrStatsW with ddof=1) read correctly. I checked these by reading the code, not by running it.

## C. What I could not check, and what output would settle it

- I could not test the helper functions on synthetic inputs. A notebook cell that recovers known distances with `crossnobis_rdm`, and known accuracies with `diag_lda_cv`, on simulated Gaussian data would settle this.
- Cue-location balance over time (B2). The fix is a run × cue_location count table per session, plus location accuracy against a null that permutes within run.
- Run numbering (B4). The fix is to print `sorted(set(trials.run))` for each session.
- Model condition order (B6). The fix is to print whether `pattern_descriptors/condition` exists in each model file, and its contents.
- Units table columns for fig4s4. The fix is to print the keys of `f["units"]` to show that no L-ratio or waveform field exists.
- The fig1s6a regression under an assumed grid layout. Printing cross-validated r² per session for a row-major 3×4 mapping would make that claim at least conditionally testable.
- The paper's exact denominator for the 70% error claim, and its bootstrap test. The paper text I fetched gives neither.

## End of run

19 turns, 3 minutes, result: success.
