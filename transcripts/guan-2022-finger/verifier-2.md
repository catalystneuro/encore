# 000252 · verifier-2 · run 41841853329

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 428
drwxr-xr-x 6 runner runner    4096 Nov  4 14:02 .
drwxr-xr-x 7 runner runner    4096 Nov  4 14:02 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  4 13:50 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  4 13:50 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  4 14:02 .claude
-rw-r--r-- 1 runner runner       0 Nov  4 14:02 .env
-rw-r--r-- 1 runner runner       0 Nov  4 14:02 .env.development
-rw-r--r-- 1 runner runner       0 Nov  4 14:02 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  4 14:02 .env.local
-rw-r--r-- 1 runner runner       0 Nov  4 14:02 .env.production
-rw-r--r-- 1 runner runner       0 Nov  4 14:02 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  4 14:02 .env.test
-rw-r--r-- 1 runner runner       0 Nov  4 14:02 .env.test.local
drwx------ 2 runner runner      40 Nov  4 14:02 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  4 13:50 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  4 13:50 .github
-rw-r--r-- 1 runner runner       0 Nov  4 14:02 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  4 13:50 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  4 13:50 .mcp.json
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 000252-guan-2022-01.yaml
```

```
<persisted-output>
Output too large (29.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/8b17327f-c5e5-4107-925b-881c27198f3f/tool-results/b06p45t72.txt

Preview (first 2KB):
# Guan et al. (preprint 2022) from dandiset 000252

Tests the findings of [Guan et al. (2022)](https://doi.org/10.1101/2022.12.07.22283227) that can be
tested on [DANDI:000252](https://dandiarchive.org/dandiset/000252/0.230408.2207). The dandiset holds
the ten-finger press task: 10 sessions of participant N (one PPC array) and 2 sessions of
participant J (a PPC and an MC array), with sorted units and trial times. The alternating-cues
task and the BMI sessions of Figures 4 to 6 are not in it.

| Claim | Outcome |
|---|---|
| Neurons per session and sessions in the ten-finger task | Reproduced (counts before the 0.5 Hz exclusion) |
| 1111 N-PPC neurons pooled | Reproduced |
| Most neurons discriminate the ten fingers (66%, 57%, 78%) | Not reproduced |
| Ten-finger decoding accuracy (70%, 66%, 75%) | Reproduced |
| Most errors are adjacent or matching fingers | Reproduced |
| Matching fingers of the two hands are closer than non-matching ones | Reproduced, resting on an assumption |
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1101-2022.12.07.22283227.yaml
```

```
<persisted-output>
Output too large (35.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/8b17327f-c5e5-4107-925b-881c27198f3f/tool-results/bcgf6qbqm.txt

Preview (first 2KB):
# Claims for Guan et al., "Compositional coding of individual finger movements in human posterior
# parietal cortex and motor cortex enables ten-finger decoding", on dandiset 000252.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md (Reader).
#
# Text read. The bioRxiv preprint, version 1 (doi:10.1101/2022.12.07.22283227), full text from
# bioRxiv JATS XML (paper/10.1101-2022.12.07.22283227.txt): main text, Methods, figure legends and
# the supplementary figure legends (Supplementary Figures 1 to 11). The contents of Supplementary
# Table 1 (phase durations) and Supplementary Table 2 (session dates) are not in the text, only
# their legends; no claim here rests on their numbers, since every analysis window is defined from
# a phase onset. The equation of the cross-validated Mahalanobis distance (Methods, Neural distance
# between fingers) is lost in the text; its description in words is used. No PDF was supplied.
#
# Code. The paper links no analysis code. It names two Python libraries: the representational
# similarity analysis toolbox (rsatoolbox, ref 57) for cross-validated Mahalanobis distances, and
# DABEST (ref 53) for Hedges' g with bootstrap confidence intervals.
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/8b17327f-c5e5-4107-925b-881c27198f3f/tool-results/b06p45t72.txt"
}
```

```
1	# Guan et al. (preprint 2022) from dandiset 000252
2	
3	Tests the findings of [Guan et al. (2022)](https://doi.org/10.1101/2022.12.07.22283227) that can be
4	tested on [DANDI:000252](https://dandiarchive.org/dandiset/000252/0.230408.2207). The dandiset holds
5	the ten-finger press task: 10 sessions of participant N (one PPC array) and 2 sessions of
6	participant J (a PPC and an MC array), with sorted units and trial times. The alternating-cues
7	task and the BMI sessions of Figures 4 to 6 are not in it.
8	
9	| Claim | Outcome |
10	|---|---|
11	| Neurons per session and sessions in the ten-finger task | Reproduced (counts before the 0.5 Hz exclusion) |
12	| 1111 N-PPC neurons pooled | Reproduced |
13	| Most neurons discriminate the ten fingers (66%, 57%, 78%) | Not reproduced |
14	| Ten-finger decoding accuracy (70%, 66%, 75%) | Reproduced |
15	| Most errors are adjacent or matching fingers | Reproduced |
16	| Matching fingers of the two hands are closer than non-matching ones | Reproduced, resting on an assumption |
17	| N-PPC index finger distinct from middle and ring in both hands | Reproduced |
18	| Hand decoders generalize across finger types | Reproduced |
19	| Finger-type decoders generalize across hands (N-PPC, J-MC) | Reproduced |
20	| J-PPC finger-type generalization is low (36% against 65%) | Partially reproduced, resting on an assumption |
[... 474 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/8b17327f-c5e5-4107-925b-881c27198f3f/tool-results/bcgf6qbqm.txt"
}
```

```
1	# Claims for Guan et al., "Compositional coding of individual finger movements in human posterior
2	# parietal cortex and motor cortex enables ten-finger decoding", on dandiset 000252.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
4	# protocol pilot-10 as stated in docs/protocol.md (Reader).
5	#
6	# Text read. The bioRxiv preprint, version 1 (doi:10.1101/2022.12.07.22283227), full text from
7	# bioRxiv JATS XML (paper/10.1101-2022.12.07.22283227.txt): main text, Methods, figure legends and
8	# the supplementary figure legends (Supplementary Figures 1 to 11). The contents of Supplementary
9	# Table 1 (phase durations) and Supplementary Table 2 (session dates) are not in the text, only
10	# their legends; no claim here rests on their numbers, since every analysis window is defined from
11	# a phase onset. The equation of the cross-validated Mahalanobis distance (Methods, Neural distance
12	# between fingers) is lost in the text; its description in words is used. No PDF was supplied.
13	#
14	# Code. The paper links no analysis code. It names two Python libraries: the representational
15	# similarity analysis toolbox (rsatoolbox, ref 57) for cross-validated Mahalanobis distances, and
16	# DABEST (ref 53) for Hedges' g with bootstrap confidence intervals.
17	#
18	# Dataset. Its archive title is "Finger_RL: human intracortical recordings during attempted finger
19	# movements of right and left hands", and the paper's Data Availability names dandiset 000252. It is
20	# meant to hold the ten-finger (right and left hand) task; whether it also holds the
[... 622 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_guan_2022.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"===== CELL {i} [{c['cell_type']}] =====")
    if c['cell_type']=='code':
        print(src[:600] + ('...' if len(src)>600 else ''))
        for o in c.get('outputs',[]):
            if o['output_type']=='stream': print('--OUT--\n'+''.join(o['text']))
            elif 'data' in o:
                d=o['data']
                if 'text/plain' in d: print('--DATA--\n'+''.join(d['text/plain'])[:4000])
                elif 'image/png' in d: print('--IMG--')
            elif o['output_type']=='error': print('--ERR--', o['ename'], o['evalue'])
    else:
        print(src)
EOF
```

```
<persisted-output>
Output too large (72.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/8b17327f-c5e5-4107-925b-881c27198f3f/tool-results/ba745qi4u.txt

Preview (first 2KB):
===== CELL 0 [markdown] =====
# Reproducing Guan et al. (preprint 2022) from dandiset 000252

**Paper.** Guan, Aflalo, Kadlec, Gámez de Leon, Rosario, Bari, Pouratian and Andersen, "Compositional coding of individual finger movements in human posterior parietal cortex and motor cortex enables ten-finger decoding", medRxiv/bioRxiv preprint, doi:10.1101/2022.12.07.22283227.

**Dataset.** DANDI:000252, "Finger_RL: human intracortical recordings during attempted finger movements of right and left hands", version **0.230408.2207** (doi:10.48324/dandi.000252/0.230408.2207). The paper cites no version (its Data Availability gives only the dandiset URL), and 0.230408.2207 is the only published version, so it is pinned. The draft was modified later (2023-06-20) but lists the same 12 assets with the same asset identifiers; the check below prints this.

**Text the claims file was written from.** The bioRxiv preprint, version 1, full text with Methods and the supplementary figure legends (claims file `claims/000252/10.1101-2022.12.07.22283227.yaml`). The paper links no analysis code.

**What the dataset holds.** Only the ten-finger press task: 10 sessions of participant N (subject `P1` in the files) and 2 of participant J (subject `N1`). The alternating-cues task (Figures 4 and 5) and the BMI tasks (Figure 6, Supplementary Figures 6 and 7) are not in it.

| Claim | Tested here |
|---|---|
| tenfinger-recording-counts | tested |
| tenfinger-pooled-npcc-neurons | tested |
| tenfinger-discriminative-fraction | tested |
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/8b17327f-c5e5-4107-925b-881c27198f3f/tool-results/ba745qi4u.txt"
}
```

```
1	===== CELL 0 [markdown] =====
2	# Reproducing Guan et al. (preprint 2022) from dandiset 000252
3	
4	**Paper.** Guan, Aflalo, Kadlec, Gámez de Leon, Rosario, Bari, Pouratian and Andersen, "Compositional coding of individual finger movements in human posterior parietal cortex and motor cortex enables ten-finger decoding", medRxiv/bioRxiv preprint, doi:10.1101/2022.12.07.22283227.
5	
6	**Dataset.** DANDI:000252, "Finger_RL: human intracortical recordings during attempted finger movements of right and left hands", version **0.230408.2207** (doi:10.48324/dandi.000252/0.230408.2207). The paper cites no version (its Data Availability gives only the dandiset URL), and 0.230408.2207 is the only published version, so it is pinned. The draft was modified later (2023-06-20) but lists the same 12 assets with the same asset identifiers; the check below prints this.
7	
8	**Text the claims file was written from.** The bioRxiv preprint, version 1, full text with Methods and the supplementary figure legends (claims file `claims/000252/10.1101-2022.12.07.22283227.yaml`). The paper links no analysis code.
9	
10	**What the dataset holds.** Only the ten-finger press task: 10 sessions of participant N (subject `P1` in the files) and 2 of participant J (subject `N1`). The alternating-cues task (Figures 4 and 5) and the BMI tasks (Figure 6, Supplementary Figures 6 and 7) are not in it.
11	
12	| Claim | Tested here |
13	|---|---|
14	| tenfinger-recording-counts | tested |
15	| tenfinger-pooled-npcc-neurons | tested |
16	| tenfinger-discriminative-fraction | tested |
17	| tenfinger-decoding-accuracy | tested |
18	| tenfinger-error-structure | tested |
19	| fig8b-matching-closer | tested |
20	| fig8a-npcc-index-distinct | tested |
[... 556 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/8b17327f-c5e5-4107-925b-881c27198f3f/tool-results/ba745qi4u.txt",
 "offset": 577,
 "limit": 260
}
```

```
577	20  b  b  lda   J-MC  0.861   0.783     0.886       0.955     0.924   0.001     0.001               0                 0           0.500           0.68             0.199             0.38        250       0.972             0.820             0.848
578	21  b  b  svm  N-PPC  0.976   0.927     0.998       0.992     0.992   0.001     0.001               0                 0           0.498           0.72             0.197             0.33        930       0.978             0.935             0.935
579	22  b  b  svm  J-PPC  0.971   0.358     0.978       0.828     0.749   0.001     0.002               0                 1           0.500           0.69             0.200             0.38        312       0.993             0.432             0.478
580	23  b  b  svm   J-MC  0.860   0.745     0.943       0.953     0.948   0.001     0.001               0                 0           0.499           0.70             0.199             0.37        250       0.913             0.781             0.786
581	
582	===== CELL 29 [code] =====
583	# Standard accuracy computed per session (a classifier per session, stratified 8-fold, O2 a, trials pooled
584	# over sessions; Methods, Offline classification), under every O1 x O7. It does not depend on O6, so the same
585	# values join every O6 row of ccgp_df.
586	ps_rows = []
587	for o1 in ["a", "b"]:
588	    for o7 in ["lda", "svm"]:
589	        for arr in F.ARRAYS:
590	            r = {}
591	            for tgt in ["hand", "finger_within", "finger_both"]:
592	                a, n = [], []
593	                for s in sess_of(arr):
594	                    X, y = F.array_data(s, arr, o1)
595	                    a.append(F.standard_accur...
596	--OUT--
[... 238 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -o ".\{300\}\(otherwise specified\|upper bound\|within-hand accuracy\|standard decoding accuracy\|pseudo-population\|separate linear classifier\).\{300\}" *.txt
```

```
273:eneralize to held-out, hypothetically equivalent vectors (Lp-vs-Rp) ( Supplementary Figure 8 ). Consistent with this hypothesis, cross-condition hand-decoding generalization performance (hand CCGP) was significantly above chance (p < 0.001, permutation test). Furthermore, hand CCGP was close to the standard decoding accuracy evaluated using cross-validation without leaving out finger types ( Figure 8e ), which provides an upper bound on hand CCGP. The close match between hand CCGP and decoding accuracy indicated that the laterality dimension robustly generalized across finger-types. Next, we applied cross-decoding to t
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -o ".\{400\}\(otherwise\|pseudo\|CCGP literature\|stacked\|each session\).\{300\}" *.txt | head -20
```

```
183:iers (left vs. right) should generalize when trained on a subset of finger types and evaluated on left-out fingers. Additionally, finger-type classifiers should generalize when trained on one hand and tested on the other hand ( Figure 8e ). This metric is sometimes called cross-condition generalization performance (CCGP) [ 60 , 61 ]. We pooled neurons across sessions (N: 10 sessions; J: 2) into a pseudo-population. We used a permutation test to assess whether CCGP was significantly above chance, shuffling the labels repeatedly (N=1001) to generate a null distribution. Standard, within-condition decoding accuracy provided an upper bound on CCGP. Reaching this upper bound implies perfect composition
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -o ".\{200\}\(500 ms\|500-ms\|0.5 Hz\).\{300\}" *.txt | head
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -o ".\{300\}\(Feature Extraction\|firing rate.\{0,40\}window\).\{500\}" *.txt | head -5
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd paper; grep -n -i "feature extraction\|otherwise specified\|700 ms" *.txt | cut -c1-900
```

```
105:## Feature Extraction
107:Except when otherwise specified, we used a 500-millisecond (ms) window of neural activity to calculate firing rates (counted spikes divided by the window duration). The firing rate was then used as the input features to each analysis or classification model. Neurons with an average firing rate less than 0.5 Hz were excluded from all analyses.
```

**Agent calls Bash**

```bash
cd paper; sed -n 105,125p *.txt | cut -c1-1500
```

```
## Feature Extraction

Except when otherwise specified, we used a 500-millisecond (ms) window of neural activity to calculate firing rates (counted spikes divided by the window duration). The firing rate was then used as the input features to each analysis or classification model. Neurons with an average firing rate less than 0.5 Hz were excluded from all analyses.

Behavioral epochs: the movement execution (“Go” or “move”) analysis window was defined as the 500-ms window starting 200 ms after the Go cue. For applicable tasks, the movement planning (“Delay” or “plan”) analysis window was defined as the 500-ms window starting 200 ms after the Delay screen. The Cue analysis window was defined as the 500-ms window starting 200 ms after the Cue screen. The intertrial interval (ITI) analysis window was defined as the last 500 ms of the ITI phase.

## Single-neuron selectivity for finger movements

In the section “Single-neuron modulation to individual finger presses,” we used a one-way ANOVA to determine whether neurons distinguished firing rates between conditions. A neuron was considered discriminative if p < 0.05 after false discovery rate (FDR) correction for multiple comparisons using the Benjamini–Hochberg procedure; we also denoted this FDR-adjusted p-value as q . We corrected for m = N comparisons, where N is the number of neurons for each participant. Following Cohen’s rules of thumb [ 51 ], we denoted the ANOVA effect size as “large” if η 2 > 0.14. As the ANOVA post hoc test, we used Dunnett’s multiple comparison test [ 52 ] to determine which fingers had significantly different firing rates than the No-Go baseline.

To quantify the effect size of firing-rate changes against the No-Go baseline ( Figure 4a ), we used Hedges’ g, which is similar to Cohen’s d but bias-corrected for small sample sizes. We calculated and visualized Hedges’ g values using the Data Analysis using Bootstrap-Coupled Estimation Python library [ 53 ].

PPC single neurons discriminate betw
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def " fingers.py; python3 - <<'EOF'
import json
nb=json.load(open('reproduce_guan_2022.ipynb'))
for i in (7,22,29):
    print(f"== {i}"); print(''.join(nb['cells'][i]['source']))
EOF
```

```
70:def list_assets() -> list[dict]:
81:def version_metadata() -> dict:
85:def s3_url(asset_id: str) -> str:
106:def _s(x):
110:def load_session(asset: dict) -> Session:
164:def load_all() -> list[Session]:
168:def counts(spikes: list, align: np.ndarray, start: float = OFFSET, dur: float = WINDOW) -> np.ndarray:
177:def rates(sess: Session, window: str = "go", dur: float = WINDOW, start: float = OFFSET) -> np.ndarray:
193:def keep_mask(sess: Session, reading: str) -> np.ndarray:
206:def array_data(sess: Session, array: str, o1: str, window: str = "go", **kw):
222:    def fit(self, X, y):
233:    def decision_function(self, X):
237:    def predict(self, X):
241:def make_decoder(kind: str):
252:def cv_predict(X, y, o2: str = "a", seed: int = 0, decoder: str = "lda", k: int = 8):
263:def error_kinds(true, pred):
279:def anova_eta2(X, y):
295:def fdr_bh(p):
311:def _resid(Xs, ys):
316:def crossnobis_rdm(X, y, o3: str = "shrinkage_diag", o4: str = "a"):
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 378,495p fingers.py
```

```
def pseudo_population(sessions_X: list, sessions_y: list, o6: str, rng=None):
    """Stack neurons of several sessions into pseudo-trials of each condition.
    o6 'a': trials matched by repetition index within condition; 'b': matched at random
    within condition (one draw; callers repeat it)."""
    n_rep = min(min((y == c).sum() for c in CONDITIONS) for y in sessions_y)
    blocks = []
    for X, y in zip(sessions_X, sessions_y):
        rows = []
        for c in CONDITIONS:
            ix = np.flatnonzero(y == c)[:n_rep] if o6 == "a" else rng.permutation(np.flatnonzero(y == c))[:n_rep]
            rows.append(X[ix])
        blocks.append(np.concatenate(rows))
    labels = np.repeat(CONDITIONS, n_rep)
    return np.concatenate(blocks, axis=1), labels


def ccgp_hand(X, cond, decoder="lda"):
    """Left-vs-right decoder trained on 4 finger types, tested on the held-out one; mean of 5 folds."""
    hand = np.array([c[0] for c in cond])
    ft = np.array([c[1] for c in cond])
[... 96 more lines not kept]
```

**Agent**

**Verifier report, round 2: Guan et al. 2022, DANDI:000252 @ 0.230408.2207**

Counts come from the claims file and the attempt record. The claims file has 19 claims. The record has 19 outcomes: 11 tested and 8 blocked (data_missing).

### 1. Outcomes and assumptions

I agree with all 19 outcomes in the record.

| Claim | Outcome | Agree | Note |
|---|---|---|---|
| tenfinger-recording-counts | reproduced | yes | Counted before the exclusion (cell 10), which is one of the criterion's readings, so no assumption is needed. |
| tenfinger-pooled-npcc-neurons | reproduced | yes | 1114 against 1111 ± 111. |
| tenfinger-discriminative-fraction | not_reproduced | yes | Robust. The uncorrected p < 0.05 shares are 56.1 / 46.5 / 68.8% (cell 13). N-PPC and J-PPC are below their bounds (59.4 / 51.3%) even with no correction, so no FDR choice can reach the paper's values. |
| tenfinger-decoding-accuracy | reproduced | yes | |
| tenfinger-error-structure | reproduced | yes | |
| fig8b-matching-closer | reproduced, `assumed: true` | yes | The assumption (precision of the partition mean, ×5) is stated in the deviations, in cell 19 and in the Summary. It is reasonable, because rsatoolbox documents that input for a list of noises. It is also the only reading that matches the paper's magnitudes, and that dependence is disclosed. |
| fig8a-npcc-index-distinct | reproduced | yes | Holds in all 18 readings. |
| fig8e-hand-ccgp | reproduced | yes | The result is the same under both populations for the standard accuracy, so it needs no assumption. |
| fig8e-finger-ccgp | reproduced | yes | Passes under O9 (b), which is a claims-file reading, so it needs no assumption. |
| jppc-finger-ccgp-low | partially_reproduced, `assumed: true` | yes | See below. |
| figs11-jppc-lower-matched-size | reproduced | yes | Now holds in all 8 readings. |
| 8 blocked claims | blocked (data_missing) | yes | Cell 36: every file is the ten-finger task, with no No-Go condition and no decoder-output column. |

**The jppc-finger-ccgp-low assumption** (standard accuracy computed on the same pseudo-population as the CCGP) is stated in the record, in cell 27 and in the Summary.
- **For it:** the Methods say "We pooled neurons across sessions … into a pseudo-population … Standard, within-condition decoding accuracy provided an upper bound on CCGP." Also, the N-PPC CCGP exceeds the per-session accuracy (ratio 1.15–1.31).
- **Against it:** the paper's 65% is matched by the per-session within-hand accuracy (0.680–0.690). The pseudo-population gives 0.828–0.890 (cell 29).
- **My view:** the choice is defensible, but calling it "the better-supported choice" (record and cell 31) is a judgement call. The other population gives "reproduced" (cell 29, row 16), and the record says so.
- **Whichever population is used,** the outcome rests on one reading of eight (O1 b / O6 a / SVM), where p sits at the 1/1002 floor.

### 2. Sentences the printed outputs do not support

- **Record, tenfinger-decoding-accuracy notes:** "with shuffled labels per-session accuracies are 0.07 to 0.17." Cell 7 prints a minimum of 0.04 (P1 2015-08-14) and also 0.06 several times. The range is 0.04–0.17. This does not affect the outcome.
- **Cell 14, and the record's tenfinger-discriminative-fraction notes:** "FDR per session gives no more." Cell 13 shows the per-session FDR mean is slightly higher than pooled FDR in some rows: N-PPC none 40.7 vs 40.4, J-PPC none 37.9 vs 37.6, J-PPC a 38.4 vs 38.1. The J-PPC value of 38.4 also exceeds the stated maximum of 38.1. The differences are at most 0.3 points, and the outcome is unaffected.
- **README:** "It takes about fourteen minutes." Cell 36 prints "notebook run time so far: 8.3 min", and that is the last code cell.
- **Summary (cell 37) and the record's fig6-online-bmi notes and data_missing finding**, on what DANDI:000147 contains ("10 files of subject P1 from 2018 … BCI finger-press task … cites the eLife paper of ref 46"). No notebook cell prints this. Cell 3 prints only the `dcite:Continues DANDI:000147` relation. The statement may be true, but nothing in the notebook backs it.
- **Minor, not a sentence:** cell 21 prints "N-PPC mean RDM range 0.00 to 3.90", but cell 22 and the text give 0.57–3.90. The 0.00 apparently comes from the diagonal. The text uses the correct off-diagonal figure.

I checked every other number in the "**Result:**" cells (11, 14, 18, 23, 26, 31, 34), the Summary, the README table and the record's notes against cells 10, 13, 16, 20–22, 25, 28, 29 and 33. All of them agree. This includes the 1 s window (60.8 / 56.8 / 82.9%), the sweep maxima (47.8 / 43.5 / 72.2%), the RDM ranges, the synthetic ratios (5.17 / 1.03), the null counts (0–37), and the ratio and accuracy ranges.

**The verifications block** states my round-1 reasons accurately. It includes the 5.46× synthetic figure, the window-sweep request, the request for null counts, and the 000147 remark, all as I gave them. Its statement that my round-1 outcomes all agree with the record is correct.

**Claims file:**
- Its readings match the paper, except for one point. The Methods say BH corrects "for m = N … neurons for each participant", but the criterion of tenfinger-discriminative-fraction corrects J-PPC and J-MC separately. Its justification comes from legends of the alternating-cues task. This departs from the Methods' wording, but it cannot change the outcome, because even uncorrected p fails.
- The O4 (a) gap I raised in round 1 is still there: the criterion does not mention the noise scaling.
- O11 (Go window only) is a fair reading of "Except when otherwise specified, … 500-millisecond window".

### 3. Round-1 points

**Resolved:**
- **Problem 2:** the per-session accuracy is now run under every O1 × O7 combination, next to every O6 row (cell 29).
- **Problem 5:** figs11 is now run under O1 b.
- **Problem 6:** the unused `Psh` is removed.
- **Problem 7:** cell 11 now notes that the counts are before the exclusion while the analyses use the excluded units.
- **Section C:**
  - The exact null counts are printed, so p = 1/1002 is confirmed.
  - The window sweep was run.
  - DANDI:000147 was checked according to the record, though the notebook prints none of it.
- **Problem 4:** stated, not fixed. It does not bear on a conclusion.

**Still open, bearing on a conclusion:**
1. **fig8b-matching-closer magnitude (problem 1).** "Reproduced" depends on the ×5 precision-of-the-mean scaling. Without it the result is partially reproduced (N-PPC 0.28–0.36 against 1.56). This is properly flagged as `assumed: true` and as a question for the authors. The paper's text cannot settle it.
2. **jppc-finger-ccgp-low (problems 2 and 3).** The outcome changes with the population used for the standard accuracy: partially reproduced on the pseudo-population, reproduced per session. Under either population, p < 0.001 holds in only one of eight readings, where 0 of 1001 null values reach the CCGP. The other readings have p = 0.002–0.038, so the claimed significance is fragile.
3. **tenfinger-discriminative-fraction.** A 1 s window from the Go cue brings all three arrays within tolerance (cell 13). The outcome correctly stays not_reproduced under O11. Which window and test the paper actually used remains an open question for the authors, and it is the likely explanation of the gap.

## End of run

17 turns, 3 minutes, $1.29 at API prices, result: success.
