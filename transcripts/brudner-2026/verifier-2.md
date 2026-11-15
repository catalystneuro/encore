# brudner-2026 · verifier-2 · run 43177010375

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 324
drwxr-xr-x 6 runner runner    4096 Nov 12 08:05 .
drwxr-xr-x 8 runner runner    4096 Nov 12 08:05 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 07:40 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 07:40 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 12 08:05 .claude
-rw-r--r-- 1 runner runner       0 Nov 12 08:05 .env
-rw-r--r-- 1 runner runner       0 Nov 12 08:05 .env.development
-rw-r--r-- 1 runner runner       0 Nov 12 08:05 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 12 08:05 .env.local
-rw-r--r-- 1 runner runner       0 Nov 12 08:05 .env.production
-rw-r--r-- 1 runner runner       0 Nov 12 08:05 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 12 08:05 .env.test
-rw-r--r-- 1 runner runner       0 Nov 12 08:05 .env.test.local
drwx------ 2 runner runner    4096 Nov 12 08:05 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 07:40 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 07:40 .github
-rw-r--r-- 1 runner runner       0 Nov 12 08:05 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 07:40 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 12 07:40 .mcp.json
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat brudner-2026-01.yaml
```

```
<persisted-output>
Output too large (42.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/9bf8e723-262a-4a7c-8cf4-41bbdfec1f2b/tool-results/bxt4lzvr3.txt

Preview (first 2KB):
# Brudner, Zhou et al. (2026) from dandiset 001871

Tests the findings of [Brudner, Zhou et al. (2026)](https://doi.org/10.1073/pnas.2608896123) that can
be tested on [DANDI:001871](https://dandiarchive.org/dandiset/001871/0.260630.1657). It holds the
walking trajectories and turn events of flies navigating a projected smooth plume (83 trials) and a
complex smoke plume (48 trials, in two sets named smoke-1a and smoke-2a), a 1500-frame window of the
complex plume movie, and three freestream plume windows. The smooth plume movie is not in it.

| Claim | Outcome |
|---|---|
| Fig. 5E, gradient predicts turns in the smooth plume, motion in the complex plume | Not reproduced, resting on an assumption |
| Fig. 5F, cue dominance positive (smooth) and negative (complex) | Partially reproduced, resting on an assumption |
| Fig. S5C, turns of about -34 and +34 degrees | Reproduced, resting on an assumption |
| Fig. 2C, motion predicts the centerline side better than the gradient (complex plume) | Partially reproduced, resting on an assumption |
| Fig. 2E, motion weighted above the gradient (complex plume) | Partially reproduced |
| Fig. S1F-G, cue maps robust to sensor spacing and delay | Not reproduced |
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/9bf8e723-262a-4a7c-8cf4-41bbdfec1f2b/tool-results/bxt4lzvr3.txt"
}
```

```
1	# Brudner, Zhou et al. (2026) from dandiset 001871
2	
3	Tests the findings of [Brudner, Zhou et al. (2026)](https://doi.org/10.1073/pnas.2608896123) that can
4	be tested on [DANDI:001871](https://dandiarchive.org/dandiset/001871/0.260630.1657). It holds the
5	walking trajectories and turn events of flies navigating a projected smooth plume (83 trials) and a
6	complex smoke plume (48 trials, in two sets named smoke-1a and smoke-2a), a 1500-frame window of the
7	complex plume movie, and three freestream plume windows. The smooth plume movie is not in it.
8	
9	| Claim | Outcome |
10	|---|---|
11	| Fig. 5E, gradient predicts turns in the smooth plume, motion in the complex plume | Not reproduced, resting on an assumption |
12	| Fig. 5F, cue dominance positive (smooth) and negative (complex) | Partially reproduced, resting on an assumption |
13	| Fig. S5C, turns of about -34 and +34 degrees | Reproduced, resting on an assumption |
14	| Fig. 2C, motion predicts the centerline side better than the gradient (complex plume) | Partially reproduced, resting on an assumption |
15	| Fig. 2E, motion weighted above the gradient (complex plume) | Partially reproduced |
16	| Fig. S1F-G, cue maps robust to sensor spacing and delay | Not reproduced |
17	| Rightward turning bias with light intensity | Blocked: metadata insufficient |
18	| 15 claims on the smooth plume, the trained networks and the agents | Blocked: the smooth plume (Dryad) could not be read |
19	
20	A failure to reproduce here may be a failure of this attempt, not of the paper: see the
[... 600 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^- id:\|^  id:\|id: " brudner-2026.yaml | head -40; wc -l brudner-2026.yaml
```

```
63:- id: fig1eh-snapshot-organization
89:- id: fig1il-zscore-reliability
114:- id: figs1-antisymmetry-index
146:- id: figs1-temporal-statistics
166:- id: figs1fg-resolution-robustness
188:- id: fig2b-smooth-auc
225:- id: fig2c-complex-auc
250:- id: figs2c-one-frame-delay
265:- id: fig2d-smooth-weights
294:- id: fig2e-complex-weights
316:- id: fig3bc-mnm-filters
347:- id: fig3d-mnm-gradient-response
364:- id: fig3e-mnm-motion-response
388:- id: fig3ij-dnm-specialization
418:- id: fig4ef-agent-success
475:- id: discussion-ten-percent-gain
495:- id: figs4-threshold-robustness
521:- id: fig5e-cue-betas
579:- id: fig5f-cue-dominance
604:- id: methods-intensity-right-bias
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,62p brudner-2026.yaml; sed -n 114,316p brudner-2026.yaml; sed -n 521,694p brudner-2026.yaml
```

```
<persisted-output>
Output too large (33.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/9bf8e723-262a-4a7c-8cf4-41bbdfec1f2b/tool-results/bdm517ble.txt

Preview (first 2KB):
# Claims for Brudner, Zhou, Jayaram, Madeira Santana, Crimaldi, Clark & Emonet, "Fly navigational
# responses exploit plume-specific odor motion and gradient cues", PNAS 123(29) e2608896123 (2026),
# doi:10.1073/pnas.2608896123, on dandiset 001871.
#
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-12,
# under docs/protocol.md version pilot-14 (Reader, steps 1 to 4). Nobody had analysed the dataset's
# data when these criteria were written; the reader saw only the dandiset's title and description.
#
# Text read: the version of record (PDF supplied by a person, published 14 July 2026), as extracted
# to paper/10.1073-pnas.2608896123.txt, with the SI Appendix (pnas.2608896123.sapp.pdf, appended to
# the same text file): Supplementary Methods, the legends of Figures S1 to S5 and of Movies S1 and S2.
# The main Methods section is a short summary that refers to the SI Appendix for every detail. PDF
# pages were opened to read the bar heights of Figures 2, 4 and 5 and the panels of Figure S5, and
# the upwind-turn formula of the SI agent simulations, which the text garbles. It reads
# P_upwind = 1 / (1 + exp(-(-0.49 + 1.5 R sin^2 theta))).
#
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/9bf8e723-262a-4a7c-8cf4-41bbdfec1f2b/tool-results/bdm517ble.txt"
}
```

```
1	# Claims for Brudner, Zhou, Jayaram, Madeira Santana, Crimaldi, Clark & Emonet, "Fly navigational
2	# responses exploit plume-specific odor motion and gradient cues", PNAS 123(29) e2608896123 (2026),
3	# doi:10.1073/pnas.2608896123, on dandiset 001871.
4	#
5	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-12,
6	# under docs/protocol.md version pilot-14 (Reader, steps 1 to 4). Nobody had analysed the dataset's
7	# data when these criteria were written; the reader saw only the dandiset's title and description.
8	#
9	# Text read: the version of record (PDF supplied by a person, published 14 July 2026), as extracted
10	# to paper/10.1073-pnas.2608896123.txt, with the SI Appendix (pnas.2608896123.sapp.pdf, appended to
11	# the same text file): Supplementary Methods, the legends of Figures S1 to S5 and of Movies S1 and S2.
12	# The main Methods section is a short summary that refers to the SI Appendix for every detail. PDF
13	# pages were opened to read the bar heights of Figures 2, 4 and 5 and the panels of Figure S5, and
14	# the upwind-turn formula of the SI agent simulations, which the text garbles. It reads
15	# P_upwind = 1 / (1 + exp(-(-0.49 + 1.5 R sin^2 theta))).
16	#
17	# Code read. The paper links github.com/emonetlab/GradientMotionMultiplePlumes; read at commit
18	# effc7b0317f6d3b62136c2a07bcba3e80e778575 (2026-07-14). It holds
19	#   - the Fig. 5E, 5F and S5D-E analysis (src/gradient_motion_panels/summary_tables.py,
20	#     scripts/generate_published_summary_tables.py, metadata/published_panel_params.json), written
[... 420 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_brudner_2026.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- OUT:\n'+''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data']: print('--- OUT:\n'+''.join(o['data']['text/plain']))
        elif o.get('output_type')=='error': print('--- ERR', o['ename'], o['evalue'])
EOF
wc -l $TMPDIR/nb.txt; grep -n "######## CELL" $TMPDIR/nb.txt
```

```
1646 /tmp/claude-1001/nb.txt
2:######## CELL 0 [markdown]
43:######## CELL 1 [code]
68:######## CELL 2 [markdown]
73:######## CELL 3 [code]
139:######## CELL 4 [markdown]
149:######## CELL 5 [code]
257:######## CELL 6 [markdown]
266:######## CELL 7 [code]
316:######## CELL 8 [markdown]
337:######## CELL 9 [code]
367:######## CELL 10 [markdown]
387:######## CELL 11 [code]
496:######## CELL 12 [code]
540:######## CELL 13 [code]
573:######## CELL 14 [code]
662:######## CELL 15 [markdown]
683:######## CELL 16 [markdown]
690:######## CELL 17 [code]
726:######## CELL 18 [markdown]
[... 27 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "limit": 740
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Brudner, Zhou et al. (2026) from dandiset 001871
4	
5	**Paper.** Brudner S, Zhou B, Jayaram V, Madeira Santana G, Crimaldi J, Clark DA, Emonet T (2026).
6	Fly navigational responses exploit plume-specific odor motion and gradient cues. *PNAS* 123(29)
7	e2608896123. [doi:10.1073/pnas.2608896123](https://doi.org/10.1073/pnas.2608896123). The claims file
8	(`claims/brudner-2026.yaml`) was written from the version of record and its SI Appendix; this attempt
9	read the same text, under `paper/`.
10	
11	**Dandiset.** [DANDI:001871](https://dandiarchive.org/dandiset/001871/0.260630.1657), version
12	0.260630.1657. The paper cites no version. This is the only published version and the one the paper's
13	code (github.com/emonetlab/GradientMotionMultiplePlumes, commit effc7b0, `metadata/published_panel_params.json`)
14	names as the source of its Fig. 5 tables. The draft has the same 136 assets and total size.
15	
16	**What the dandiset holds.** 131 behavior NWB files, one per trial of a fly cohort (83 smooth-plume
17	files, "nagel-smoke"; 24 "smoke-1a" and 24 "smoke-2a" complex-plume files), with per-trajectory
18	position, heading, velocities and the odor intensity, gradient and motion signals at the antennae,
19	and a table of turn events; the complex plume movie window (frames 300 to 1799 of smoke_1a_orig);
20	three freestream plume windows; and a compact asset of Fig. S1 panel inputs. The smooth plume movie
[... 720 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 740,
 "limit": 560
}
```

```
740	
741	pairs = []
742	for g in ["complex_2a", "complex_1a", "complex_both"]:
743	    for _, c in R5[R5.group == g].iterrows():
744	        s = R5[(R5.group == "smooth") & (R5.onset == c.onset) & (R5.margin == c.margin) & (R5.z == c.z)].iloc[0]
745	        pairs.append({"complex files": g, "onset": c.onset, "complex heading": c.heading, "margin": c.margin, "z": c.z,
746	                      "smooth": s.dominance, "complex": c.dominance,
747	                      "signs hold": (s.dominance > 0) and (c.dominance < 0),
748	                      "both within tolerance": abs(s.dominance - 0.946) <= 0.095 and abs(c.dominance + 0.662) <= 0.066})
749	PR = pd.DataFrame(pairs)
750	print("\nPaired readings (expected: smooth 0.946 +/- 0.095, complex -0.662 +/- 0.066):")
751	print(PR.round(3).to_string(index=False))
752	print("\nReadings where the signs hold / both values within tolerance, by complex file set:")
753	print(PR.groupby("complex files")[["signs hold", "both within tolerance"]].agg(["sum", "count"]).to_string())
754	print("\nUnder the code's readings: smooth", round(cs.dominance, 3), ", complex (smoke-2a)", round(cc.dominance, 3))
755	print("Smooth dominance over all readings: range", round(R5[R5.group == 'smooth'].dominance.min(), 3), "to", round(R5[R5.group == 'smooth'].dominance.max(), 3))
756	--- OUT:
757	Mean log-likelihood per turn and dominance, every reading:
758	       group  onset heading  margin              z  turns  ll_full  ll_gradient  ll_motion  ll_base  dominance
759	      smooth rule20 160-200   False           none   2846  -0.5946      -0.5949    -0.6039  -0.6042     0.9367
[... 540 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1300
}
```

```
1300	
1301	
1302	######## CELL 32 [markdown]
1303	The deposited maps scale with the one-pixel cues computed from the windows by the same factor for the
1304	gradient and for motion (printed above), so the two carry the same units of space and time and their
1305	ratio, which the index takes, is on the scale of the cues computed from the complex window. The
1306	deposited maps are of frames smoothed before the cues were taken (their provenance names
1307	"bgsub_gauss3"); the complex window is stored after the same named preprocessing.
1308	
1309	######## CELL 33 [code]
1310	from skimage.filters import threshold_otsu
1311	def fs_index(G, M, mean, center, bias, mode):
1312	    mask = plumes.otsu_mask(mean, bias, mode) & np.isfinite(G) & np.isfinite(M)
1313	    sg, sm = plumes.antisymmetry(np.nan_to_num(G), center, mask), plumes.antisymmetry(np.nan_to_num(M), center, mask)
1314	    return sg, sm, mask.mean()
1315	
1316	AI = []
1317	for code_, d in FS.items():
1318	    c = int(np.argmax(d["mean"][:, :10].mean(1)))
1319	    lo, hi = plumes.hist_percentiles(*d["hist"])
[... 328 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i "20%\|angular displacement\|saccade\|turn onset\|onset" 10.1073-pnas.2608896123.txt | head -40
```

```
910:rotational velocities, we identified saccade-like turning events, 
925:onset to predict turn direction via logistic regression (permitting 
956:the fly’s angular velocity (black), odor gradient (orange), and odor motion (green) over several seconds. Saccade-like turns were detected as peaks in turn speed 
1748:airflow, for 2 minutes prior to experiment onset. Each fly cohort navigated either smooth plume 
1781:dense region in the resulting distribution as exemplary saccade-like turns after inspecting the 
1792:used their values 50ms prior to turn onset (time of crossing 20% turn speed peak height on the 
1826:binarized plume intensities using spatially local thresholds. We then calculated the frequency of onsets in 
1899:Figure S5: Analysis of cue-response relationships. (A-C) Detection and validation of saccade-like turns. 
1906:trajectories associated with left and right saccades. (C) Angular displacement during the identified turn
```

**Agent calls Bash**

```bash
cd paper; sed -n 1772,1800p 10.1073-pnas.2608896123.txt; sed -n 1899,1912p 10.1073-pnas.2608896123.txt
```

```
maximized the correlation, and converting that offset to a velocity-like measure based on 
calibration (mm per pixel) and sampling frequency. These signals were then smoothed using an 
exponential filter (τ= 200ms) and z-scored for subsequent analysis. 
 
Behavioral Analysis 
 
We located candidate turning events by finding local maxima in absolute angular velocity. A 
density-based clustering algorithm (DBSCAN algorithm; eps=0.1, min_samples=900) was 
applied to the joint distribution of log-transformed peak amplitude and peak height. We treated a 
dense region in the resulting distribution as exemplary saccade-like turns after inspecting the 
surrounding trajectories and the associated heading changes (Fig. S5). 
 
For analysis, we retained only turns that met the following conditions: 
1. Upwind orientation: Heading angles within ±20° of directly upwind (160–200°). 
2. Active upwind walking: Positive horizontal velocity as determined via a fourth-order 
Butterworth filter (cutoff=0.2 Hz) applied to vx. 
3. Arena region: Horizontal positions 3cm<x<22cm, with vertical position y contained 
within a 3cm band around the plume center line. 
 
We modeled turn direction (left vs. right) using logistic regression. We used the smoothed and zscored estimates of olfactory cues intensity, gradient, and motion as predictors. Specifically, we 
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "bgsub\|1011\|768" $TMPDIR/nb.txt | head; grep -n "def onset_20pct\|def turn_table" -A40 plumes.py | grep -n "peak\|start\|stop\|20" | head -40
```

```
218:spd|max                   99.898      99.612   99.768
1075:Its provenance names a preprocessing run "bgsub_gauss3_fullslice_p001_p99", so it may differ from the
1307:"bgsub_gauss3"); the complex window is stored after the same named preprocessing.
1:241:def onset_20pct(t: np.ndarray, dtheta: np.ndarray, start: float, stop: float,
3:243-    """SI turn onset: the time rotational speed crosses 20% of the turn's peak on the rising edge.
5:245-    The peak is the largest |dtheta| between the event's start and stop (a standard choice); the
6:246-    onset is the first frame of the run of frames at or above 20% of the peak that contains the
7:247-    peak. With `signed` (the rule used), the run is of the rotation in the turn's own direction,
8:248-    sign(dtheta at the peak) x dtheta, so that it stops where the fly rotates the other way; with
11:251-    time, peak time, peak speed, first and last index of that run).
13:253-    i0, i1 = np.searchsorted(t, [start - 1e-9, stop + 1e-9])
19:259-    peak = s[ip]
21:261-    while j > 0 and s[j - 1] >= 0.2 * peak:
24:264-    while e < len(t) - 1 and s[e + 1] >= 0.2 * peak:
26:266-    return float(t[j]), float(t[ip]), float(peak), j, e
43:296:def turn_table(prepared: pd.DataFrame, turns: pd.DataFrame, onset: str = "rule20",
49:302-    predictors are read at the frame matched to `onset` - 50 ms ("start": the dataset's turn
50:303-    start, as the code; "rule20": the SI's onset), the code's way (`merge_asof`).
67:320-        fps = 1.0 / np.median(np.diff(t))
69:322-            on20, tpk, pk, j0, j1 = onset_20pct(t, dth, r.start_time, r.stop_time)
[... 10 more lines not kept]
```

**Agent**

**Verifier report, brudner-2026, round 2 (DANDI:001871 @ 0.260630.1657)**

I counted from the claims file and the attempt record. The claims file has 22 claims and the attempt record gives 22 outcomes:
- 1 reproduced (figs5c)
- 3 partially reproduced (fig5f, fig2c, fig2e)
- 2 not reproduced (fig5e, figs1fg)
- 16 blocked: 15 `other` and 1 `metadata_insufficient` (methods-intensity-right-bias)

Four outcomes carry `assumed: true`: fig5e, fig5f, figs5c and fig2c.

### 1. Outcomes

| Claim | Agree? | Assumption stated / reasonable |
|---|---|---|
| fig5e-cue-betas, not_reproduced | **Yes** | Stated. The outcome does not actually depend on it. With the SI onset, smoke-1a passes 0/24 readings and smoke-2a passes 16/24. With the event start, smoke-1a passes 8/24 and smoke-2a 0/24. Both sets together pass 0 (cell 14). No file set or onset gives the result in every reading, so the claim is not reproduced under any of them. The "resting on an assumption" label is over-cautious, not wrong. |
| fig5f-cue-dominance, partially_reproduced | **Yes, conditionally** | Stated, and reasonable: the dandiset description, the session descriptions and the match to the published tables (cell 12) all point to smoke-1a. Two other readings would make it reproduced: smoke-2a with the SI onset at 150–210 (0.937 / −0.717), and smoke-1a with the event start at 160–200 (0.879 / −0.701). The evidence that favours smoke-1a (the table match) comes from the event start, and under that onset this claim is reproduced. So the outcome depends on the onset question that was sent to the reader. With smoke-1a and the SI onset the signs hold in only 4 of 6 readings (cell 19), so "signs hold" is not true in every reading. |
| figs5c-turn-angles, reproduced | **Yes, only as conditional on the added reading** | Stated. Under both readings the claims file names, the medians are about ±21°, outside tolerance (cell 22). The outcome rests entirely on the author's bounds: the 20% crossings on the rising and falling edges. The paper's own turn detection (Fig. S5A) measures peak width at half height. Events 5–9 frames long that start a median of 4 frames after the 20% crossing are consistent with half-height bounds. If the deposited events are the paper's turn events, then the ±21° is the paper's own measure and the claim fails. A half-height reading was not tested. The assumption is plausible but chosen after the event bounds failed, so it is weak. |
| fig2c-complex-auc, partially_reproduced | **Yes** | Stated, and reasonable: a sum AUC of exactly 0.5 with SD 0 and a sum weight of 0 point to mirror balancing. Under the two samplings the claims file names, the sum AUC is 0.620–0.663, so the outcome would be not_reproduced (cell 40). The record says so. |
| fig2e-complex-weights, partially_reproduced | **Yes** | No assumption is needed. Every reading gives the ordering; the gradient weight (0.231–0.281) is out of tolerance under every reading. |
| figs1fg-resolution-robustness, not_reproduced | **Yes** | Across all six readings, the lowest motion r over delays 1–4 is 0.729–0.784, below 0.8 (cell 28). |
| methods-intensity-right-bias, blocked (metadata_insufficient) | **Yes** | Both conditional outcomes are now given (cell 17). |
| figs1-antisymmetry-index, figs1-temporal-statistics, blocked | **Yes** | The parts that can be computed are now computed (cells 33, 37). |
| The other 13 blocked claims | **Yes** | — |

**Places where the claims file may misread the paper (reported, not corrected):**
- **figs5c:** the claims file takes "the dataset's detected turn events" as the paper's turns. It does not consider that the deposited event bounds may differ from the paper's. It allows for this for the onset in fig5e but not for the turn bounds here.
- **fig5e:** the claims file says the code "selects smoke-2a" and that the criteria "follow the code". It does not mention the dandiset description, which says the smoke_1a_orig movie was the one analysed.
- **fig5e and fig5f use different rules:** fig5e takes "the outcome all readings give", while fig5f, whose readings are "as fig5e", takes "within tolerance under one reading". Under this mix the two can come out differently on the same turns.

### 2. Statements the printed outputs do not support

- **README:** "under these the complex motion cue does not reach significance." With smoke-1a and the SI onset, the motion p is 0.046 (below 0.05). With per-trajectory z-scoring it is 0.0046 and 0.013, so the 0.0046 case passes the criterion's 0.01 (cell 11). Those readings fail because the smooth motion term becomes significant (p 0.0079), not because the complex term does.
- **README and Summary (cell 44):** the published tables "are matched only by the smoke-1a files with the files' own turn start." smoke-1a with the SI onset at 160–200 is also within 0.45 SE (motion) and 0.09 SE (gradient), with max |ΔLL| 0.0036 (cell 12). "Closest" is supported; "only" is not.
- **Cell 15 and the record's fig5e notes:** "so the two sets do not differ by a flip convention." Cell 13 shows only that the projection-flip label does not reverse the sign within a set. In smoke-2a both the motion and the gradient coefficients have the opposite sign to smoke-1a (cell 11). That pattern is consistent with a sign or mirror convention that differs between the two sets as a whole, and nothing in the outputs rules that out.
- **Summary (cell 44), fig5f row:** "signs hold … with the SI onset." They hold in 4 of 6 readings; at 150–210, as stored or pooled, the complex value is +0.114 (cell 19).
- **Summary (cell 44), fig5e row:** "holds with the dataset's turn start, smoke-1a, at 160 to 200 degrees." It holds there only as stored or pooled; with per-trajectory z-scoring it fails (cell 14).
- **Summary (cell 44):** turn events "end before the turn does." No output shows where events end relative to the falling edge.
- **Summary (cell 44) and record inputs/findings:** the port "gives the code's numbers on the same files, checked in preparation." No output shows this. Cell 12 compares with the published tables only.
- **Cells 26 and 32:** the provenance strings "bgsub_gauss3_fullslice_p001_p99" and "bgsub_gauss3" are not printed anywhere in this notebook. Also in cell 32: "the same factor for the gradient and for motion." The slopes are 0.169–0.172 (gradient) and 0.196–0.221 (motion), and the motion fits have r of only 0.24–0.46 (cell 31). "Similar" would be supported; "the same" is not.
- **Cell 29 and the record's figs1fg notes:** the centered and correlator forms "give the same correlations to three decimals." They differ by 0.001 in several cells at 8 and 15 frames, e.g. 9 px at 8 frames is 0.534 against 0.533 (cell 28).
- **Record, fig5e notes:** "2846 turns, 1011 trajectories." Cell 11 prints 1010.
- **Record, findings:** events "last 5 to 9 frames." 8 events last 10–11 frames (cell 7). Also, the y values "768 to 814 mm": only the maximum (813.6) is printed (cell 5).
- **Record, findings, and cell 8:** the lag scan between `signal` and the movie "found no consistent peak." This was not run in the notebook.
- **Unchanged from round 1:** "Dryad answers 401" is not backed by any output.

All other numbers in the Result cells (15, 20, 23, 29, 38, 41), the Summary, the README and the record's notes match the outputs.

**The verifications block:**
- The round-1 reasons are stated accurately and fairly, mostly close to my wording. Folding problem 9 into the figs1fg reason, and problem 8 into the fig2c reason, is acceptable.
- The `reviewed:` field says the conclusions and summary were removed from the notebook I reviewed. That is inaccurate: in round 1 I reported that cell 26 still held the author's "Result" text (round-1 problem 12).

### 3. Round-1 points

**Resolved:**
- **Problem 1 (complex file set):** smoke-1a was adopted with evidence; fits per projection flip were added; every reading was compared with the published tables.
- **Problem 2 (onset bug):** the rule is now signed. The old rule's run reversed in 0.2% of turns, and no result changed.
- **Problem 3 (fig2c sampling):** the assumption is stated, and the record notes that the claims file's samplings would give not_reproduced.
- **Problem 4 (smoothing for motion):** smoothing was run for motion too; the motion part still fails.
- **Problem 5 (figs1 parts):** the freestream and complex parts were computed.
- **Problem 6 (right bias):** both left/right mappings are evaluated.
- **Problem 7 (centerline row):** the row-571 variant was run.
- **Problem 8 (train/test overlap):** location-split mirror sampling was added and gives the same AUCs.
- **Problem 9 (backward difference):** the centered form is now the main form.
- **Problem 10 (heading and position frames):** documented as the code's behaviour.

**Remaining, bearing on a conclusion:**
1. **fig5f depends on the onset question sent to a reader.** smoke-1a with the event start gives reproduced; smoke-1a with the SI onset gives partially reproduced; smoke-2a with the SI onset gives reproduced. The record states this, but the README's one-line outcome hides it.
2. **Why smoke-1a and smoke-2a differ in sign is still unexplained.** A set-wide sign or mirror convention has not been excluded (see the overstatement in §2). The test I would want is the sign of the gradient and motion signals against the known plume geometry in each set, e.g. the mean `spatial_gradient` as a function of y about the centerline. This decides whether smoke-2a is a mirrored copy, and so which set's outcome stands for the paper.
3. **figs5c rests on the author's turn bounds.** It is not reproduced under the claims file's readings, and the half-height alternative suggested by the paper's own Fig. S5A was not run.
4. **fig2c rests on the mirror-balancing assumption** (stated; the outcome is not_reproduced without it).
5. **The README's significance sentence needs correcting** (§2).

## End of run

14 turns, 3 minutes, $1.58 at API prices, result: success.
