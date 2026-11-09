# 000483 · verifier-2 · run 41136696282

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 680
drwxr-xr-x 6 runner runner    4096 Oct 30 23:43 .
drwxr-xr-x 7 runner runner    4096 Oct 30 23:43 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 22:11 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 22:11 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 30 23:43 .claude
-rw-r--r-- 1 runner runner       0 Oct 30 23:43 .env
-rw-r--r-- 1 runner runner       0 Oct 30 23:43 .env.development
-rw-r--r-- 1 runner runner       0 Oct 30 23:43 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 30 23:43 .env.local
-rw-r--r-- 1 runner runner       0 Oct 30 23:43 .env.production
-rw-r--r-- 1 runner runner       0 Oct 30 23:43 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 30 23:43 .env.test
-rw-r--r-- 1 runner runner       0 Oct 30 23:43 .env.test.local
drwx------ 2 runner runner    4096 Oct 30 23:43 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 22:11 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 22:11 .github
-rw-r--r-- 1 runner runner       0 Oct 30 23:43 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 22:11 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 22:11 .mcp.json
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 000483-sit-2023-01.yaml
```

```
<persisted-output>
Output too large (55.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/55c66149-ad44-4fae-809e-995d6b9207e6/tool-results/bj7965s0h.txt

Preview (first 2KB):
# Sit & Goard (2023) from dandiset 000483

Tests the findings of [Sit and Goard (2023)](https://doi.org/10.1038/s41467-023-37704-5),
"Coregistration of heading to visual cues in retrosplenial cortex", on
[DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321). The dandiset holds two-photon
recordings of retrosplenial somata and of ADN and visual cortical axons in RSC, made in a floating
chamber rotated by a motor, by the mouse or with the head rotated. The files hold raw ROI
fluorescence and chamber heading, with no neuropil trace, dF/F or inferred spikes; the notebooks
compute them.

| Claim | Outcome |
|---|---|
| 14.0% heading cells in the free chamber (Fig. 1D, E) | Blocked: data missing |
| 14.2% heading cells with motor rotation (Fig. 1G) | Reproduced (rests on an assumption) |
| No cell passes the test on pre-shuffled data | Not reproduced (rests on an assumption) |
| Preferred headings tile the chamber (Fig. 1H) | Partially reproduced (rests on an assumption) |
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md | tail -n +25; echo ======; sed -n 1,400p 000483-sit-2023-01.yaml
```

```
<persisted-output>
Output too large (29.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/55c66149-ad44-4fae-809e-995d6b9207e6/tool-results/bomvkieer.txt

Preview (first 2KB):
| Landmark and alignment flip scores drop in the dark (Fig. 5G, H) | Partially reproduced |
| Axons within the soma clusters (Fig. 5I) | Partially reproduced |
| Visual-cue-only rotation (Fig. 5K) | Blocked: metadata insufficient |
| Diversity persists across rotation direction (Fig. S5) | Reproduced |
| Diversity persists with animal or motor control (Fig. S6) | Not reproduced (rests on an assumption) |
| Decoding from all tuned cells, light-on (Fig. 6A) | Not reproduced |
| Decoding from all tuned cells, light-off (Fig. 6A) | Partially reproduced (rests on an assumption) |
| Decoding from heading cells (Fig. 6B) | Partially reproduced (rests on an assumption) |
| Decoding from landmark cells (Fig. 6B) | Partially reproduced (rests on an assumption) |
| Decoding from alignment cells (Fig. 6B) | Not reproduced |
| 180 degree errors of landmark, not heading, cells (Fig. 6B) | Reproduced (rests on an assumption) |
| Heading cells decode worse than all tuned cells (Fig. 6B) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

[... 18 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "000483-sit-2023-01.yaml"
}
```

```
1	schema_version: 2
2	id: 000483-sit-2023-01
3	dataset:
4	  archive: dandi
5	  id: 000483
6	  version: 0.230421.2321
7	  doi: 10.48324/dandi.000483/0.230421.2321
8	paper: doi:10.1038/s41467-023-37704-5
9	date: 2026-10-30
10	entry: 000483-sit-2023
11	provenance:
12	  kind: agent
13	  accountable:
14	    name: CatalystNeuro
15	  agent:
16	    harness: Claude Code
17	    model: claude-opus-5-5
18	    protocol: pilot-12
19	  runner:
20	    platform: GitHub Actions
[... 712 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1038-s41467-023-37704-5.yaml"
}
```

```
1	# Claims for Sit & Goard (2023), Nature Communications 14:1992, on dandiset 000483.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record (publisher's PDF supplied by a person, extracted to text):
6	# main text, figure legends, Methods and Statistical information. The Supplementary Information
7	# (Figures S1 to S7 and Table S1) was not in the paper store and was not read. The main
8	# findings and their statistics are all stated in the main text; the supplement holds the
9	# detail of three of them (Figure S5, Figure S6 and Table S1), and the claims that rest on it
10	# say so. The figures could not be opened (no PDF renderer), so no number below is read from a
11	# figure.
12	#
13	# Code read: the repository the paper links, given there as
14	# github.com/ucsb-goard-lab/Neurotar-HDExperiments; the repository is in fact
15	# github.com/ucsb-goard-lab/Neurotar-HD-Experiments, commit c6344f5 (2023-03-14). It holds
16	# MATLAB classes, not figure scripts: Cue.m (tuning curves, preferred direction, flip score,
17	# Gaussian fits), ControlledRotation.m (trial segmentation and the heading-selection test),
18	# FreelyMoving.m (the Rayleigh-vector test), LightDarkExperiment.m and its subclasses (light and
19	# dark segmentation), Separator.m, and _ReviewerCode/reviewer_reclassify_attempt.m (a GMM
20	# clustering run). No code for the V-tests, the coherent-remapping offsets, the flip-score
[... 701 more lines not kept]
```

**Agent**

Read the attempt record (24 outcomes) and claims file (24 claims). Now dumping the notebooks' conclusions and outputs to check numbers.

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/nb; python3 - <<'EOF'
import json,os
d=os.environ['TMPDIR']+'/nb'
for nb in ['single_cue','rotation_remapping','axons','somata','directions','decoding']:
    j=json.load(open(nb+'.ipynb'))
    out=[]
    for i,c in enumerate(j['cells']):
        src=''.join(c['source'])
        out.append(f"\n##### CELL {i} [{c['cell_type']}]\n{src}")
        if c['cell_type']=='code':
            for o in c.get('outputs',[]):
                if 'text' in o: out.append("--- OUT:\n"+''.join(o['text']))
                elif 'data' in o and 'text/plain' in o['data']: out.append("--- OUT:\n"+''.join(o['data']['text/plain']))
                elif o.get('output_type')=='error': out.append("--- ERR "+o['ename'])
    open(f"{d}/{nb}.txt",'w').write('\n'.join(out))
    print(nb,len(j['cells']),sum(len(x) for x in out))
EOF
```

```
single_cue 27 36781
rotation_remapping 15 36319
axons 14 25364
somata 25 42803
directions 15 22428
decoding 34 44076
```

**Agent calls Bash**

```bash
cat $TMPDIR/nb/single_cue.txt
```

```
<persisted-output>
Output too large (36KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/55c66149-ad44-4fae-809e-995d6b9207e6/tool-results/butx6xzlt.txt

Preview (first 2KB):
##### CELL 0 [markdown]
# Sit & Goard (2023) on dandiset 000483: single-cue rotation (Figure 1)

**Paper.** Sit KK, Goard MJ (2023). Coregistration of heading to visual cues in retrosplenial
cortex. *Nature Communications* 14:1992.
[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5). The claims file
(`claims/000483/10.1038-s41467-023-37704-5.yaml`) was written from the version of record (main
text, legends, Methods; the Supplementary Information was not available).

**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
0.230421.2321. The paper cites no version of the dandiset (it cites a Dryad deposit and the
dandiset by its description), so the most recent published version is pinned, and the only one:
the draft has the same 128 assets and size and was last modified two months later, on metadata.

This notebook covers the single-cue controlled-rotation experiments (Figure 1). The head-rotation
and remapping claims are in `rotation_remapping.ipynb`, the dual-cue claims in
[... 28 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/single_cue.txt"
}
```

```
1	
2	##### CELL 0 [markdown]
3	# Sit & Goard (2023) on dandiset 000483: single-cue rotation (Figure 1)
4	
5	**Paper.** Sit KK, Goard MJ (2023). Coregistration of heading to visual cues in retrosplenial
6	cortex. *Nature Communications* 14:1992.
7	[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5). The claims file
8	(`claims/000483/10.1038-s41467-023-37704-5.yaml`) was written from the version of record (main
9	text, legends, Methods; the Supplementary Information was not available).
10	
11	**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
12	0.230421.2321. The paper cites no version of the dandiset (it cites a Dryad deposit and the
13	dandiset by its description), so the most recent published version is pinned, and the only one:
14	the draft has the same 128 assets and size and was last modified two months later, on metadata.
15	
16	This notebook covers the single-cue controlled-rotation experiments (Figure 1). The head-rotation
17	and remapping claims are in `rotation_remapping.ipynb`, the dual-cue claims in
18	`axons.ipynb` and `somata.ipynb`, the decoding of Figure 6 in `decoding.ipynb`, and Figures S5 and S6 and the visual-cue-only files of Figure 5K in `directions.ipynb`.
19	
20	| Claim | Here |
[... 514 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/rotation_remapping.txt"
}
```

```
1	
2	##### CELL 0 [markdown]
3	# Sit & Goard (2023) on dandiset 000483: head rotation and remapping (Figures 2 and 3)
4	
5	**Paper.** Sit KK, Goard MJ (2023), *Nature Communications* 14:1992,
6	[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5); claims file
7	written from the version of record without its supplement.
8	
9	**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
10	0.230421.2321, the only published version (the paper cites none). See `single_cue.ipynb` for the
11	data check of all files.
12	
13	| Claim | Here |
14	|---|---|
15	| fig2f-head-chamber-same-preference | tested |
16	| fig3c-coherent-remapping | tested |
17	
18	Activity is inferred spikes computed from the raw fluorescence (no neuropil correction; see
19	`rsc.py`). Cells are selected by the heading-selection test with the centred fit, the reading
20	adopted in `single_cue.ipynb` (the code's uncentred fit only passes cells whose peak lies near
[... 455 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/axons.txt"
}
```

```
1	
2	##### CELL 0 [markdown]
3	# Sit & Goard (2023) on dandiset 000483: ADN and visual axons, light and dark (Figure 4)
4	
5	**Paper.** Sit KK, Goard MJ (2023), *Nature Communications* 14:1992,
6	[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5); claims file
7	written from the version of record without its supplement.
8	
9	**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
10	0.230421.2321, the only published version (the paper cites none). See `single_cue.ipynb` for the
11	data check of all files.
12	
13	| Claim | Here |
14	|---|---|
15	| fig4-axons-light-on-shape | tested |
16	| fig4-axons-light-off | tested |
17	| fig5-three-classes | tested |
18	| fig5-class-proportions | tested |
19	| fig5e-alignment-peaks-coregistered | tested |
20	| fig5f-heading-flip-unchanged | tested |
[... 342 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/somata.txt"
}
```

```
1	
2	##### CELL 0 [markdown]
3	# Sit & Goard (2023) on dandiset 000483: RSC somata with dual cues, light and dark (Figure 5)
4	
5	**Paper.** Sit KK, Goard MJ (2023), *Nature Communications* 14:1992,
6	[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5); claims file
7	written from the version of record without its supplement.
8	
9	**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
10	0.230421.2321, the only published version (the paper cites none). See `single_cue.ipynb` for the
11	data check of all files.
12	
13	| Claim | Here |
14	|---|---|
15	| fig4-axons-light-on-shape | tested |
16	| fig4-axons-light-off | tested |
17	| fig5-three-classes | tested |
18	| fig5-class-proportions | tested |
19	| fig5e-alignment-peaks-coregistered | tested |
20	| fig5f-heading-flip-unchanged | tested |
[... 600 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/directions.txt"
}
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb/decoding.txt"
}
```

```
1	
2	##### CELL 0 [markdown]
3	# Sit & Goard (2023) on dandiset 000483: rotation direction and arena control (Figures S5, S6)
4	
5	**Paper.** Sit KK, Goard MJ (2023), *Nature Communications* 14:1992,
6	[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5); claims file
7	written from the version of record without its supplement, so Figures S5 and S6 were not read.
8	
9	**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
10	0.230421.2321, the only published version (the paper cites none). See `single_cue.ipynb` for the
11	data check of all files.
12	
13	| Claim | Here |
14	|---|---|
15	| figs5-rotation-direction | tested |
16	| figs6-arena-control | tested |
17	| fig5k-visual-cue-only | blocked: no recording shares the visual-only files' ROIs (structure shown below) |
18	
19	The claims file gives two readings of what the bootstrapped KS test compares: (a) differences in
20	preferred heading between the two conditions for heading-selective cells, against the same
[... 312 more lines not kept]
```

```
1	
2	##### CELL 0 [markdown]
3	# Sit & Goard (2023) on dandiset 000483: decoding heading from RSC somata (Figure 6)
4	
5	**Paper.** Sit KK, Goard MJ (2023), *Nature Communications* 14:1992,
6	[doi:10.1038/s41467-023-37704-5](https://doi.org/10.1038/s41467-023-37704-5); claims file
7	written from the version of record without its supplement.
8	
9	**Dataset.** [DANDI:000483](https://dandiarchive.org/dandiset/000483/0.230421.2321), version
10	0.230421.2321, the only published version (the paper cites none). See `single_cue.ipynb` for the
11	data check of all files.
12	
13	| Claim | Here |
14	|---|---|
15	| fig6a-population-light-on | tested |
16	| fig6a-population-light-off | tested |
17	| fig6b-heading-cells | tested |
18	| fig6b-landmark-cells | tested |
19	| fig6b-alignment-cells | tested |
20	| fig6b-180-errors | tested |
[... 599 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -c 1500 README.md | tail -c 900; echo; grep -n "Decoding from all tuned cells, light-on" -A3 README.md | head -3; wc -l README.md
```

```
them.

| Claim | Outcome |
|---|---|
| 14.0% heading cells in the free chamber (Fig. 1D, E) | Blocked: data missing |
| 14.2% heading cells with motor rotation (Fig. 1G) | Reproduced (rests on an assumption) |
| No cell passes the test on pre-shuffled data | Not reproduced (rests on an assumption) |
| Preferred headings tile the chamber (Fig. 1H) | Partially reproduced (rests on an assumption) |
| Same preference under head and chamber rotation (Fig. 2F) | Partially reproduced (rests on assumptions) |
| Coherent remapping (Fig. 3C) | Partially reproduced (rests on an assumption) |
| ADN axons unimodal, visual axons bimodal in light (Fig. 4) | Reproduced |
| ADN axons keep tuning in the dark, visual axons lose it (Fig. 4) | Partially reproduced |
| Three classes by clustering (Fig. 5B) | Not reproduced |
| Class proportions (Fig. 5C to E) | Not reproduced |
| Alignment cells' dark peak at
30:| Decoding from all tuned cells, light-on (Fig. 6A) | Not reproduced |
31-| Decoding from all tuned cells, light-off (Fig. 6A) | Partially reproduced (rests on an assumption) |
32-| Decoding from heading cells (Fig. 6B) | Partially reproduced (rests on an assumption) |
51 README.md
```

**Agent calls Grep**

```json
{
 "pattern": "prctile|smoothdata|abs\\(p|percentile\\(",
 "path": "rsc.py",
 "output_mode": "content",
 "-C": 2
}
```

```
25-  at the wraps of heading and at rests (more than 20 consecutive frames with a change under 0.5
26-  degree); segments under 50 frames dropped, and segments dropped where
27:  `any(90 - abs(prctile(heading, [25, 75])) > 50)`, that is, where the 25th or 75th heading
28-  percentile lies within 40 degrees of 0 (the code's rule, ControlledRotation.m line 224 at
29-  c6344f5; the claims file paraphrases it as "more than 50 degrees from +-90"). Wraps are found as the code finds them: peaks of
--
49-  circular shift that puts that peak at bin 15 (claims, opening comment; Methods).
50-- Flip score: code Cue.calculateFlipScore (Methods, eq. 5): circular autocorrelation of the
51:  tuning curve smoothed with MATLAB's smoothdata default, CC at 180 minus the mean of CC at 90 and
52:  270 degrees. smoothdata picks its default window heuristically from the data; a moving mean a
53-  quarter of the curve's length wide (15 bins) stands in for it (an assumption that cannot be
54-  checked without MATLAB; on synthetic curves the score is about -0.2 for one peak and 2 for two).
--
260-        if len(s) == 0:
261-            continue
262:        p = np.percentile(h[s], [25, 75])
263:        if not np.any(90 - np.abs(p) > 50):
264-            keep.append(s)
265-    return keep
--
[... 21 more lines not kept]
```

**Agent**

**Verifier report, round 2: Sit & Goard (2023) on DANDI:000483 (attempt 000483-sit-2023-01)**

The claims file has 24 claims and the attempt record has 24 outcomes: 2 blocked, 5 reproduced, 11 partially reproduced, 6 not reproduced. Ten of them rest on an assumption.

The main new problem is that most of the written conclusions don't match the notebooks they sit in. The printed outputs of `single_cue`, `axons`, `somata`, `directions` and `decoding` reproduce my round-1 numbers exactly: 485 selected cells, 165 passing the shuffled control, 202/67/1150 cells per class, V = 743.5 for fig5e. The "**Result:" cells, the Summaries and the attempt record instead quote another run that I haven't been given: 486, 166, 194/75/1150, V = 743.2. The record says the re-run differs only slightly, between machines. In most places that is true, and no outcome changes. In two places, though, the text states the opposite of what the notebook prints (part 2a).

**1. Outcomes**

| Claim | Outcome in the record | Agree? | Assumption stated and reasonable? |
|---|---|---|---|
| fig1-free-heading-fraction | blocked (data_missing) | Yes | n/a |
| fig1g-rotation-heading-fraction | reproduced | Yes: the printed 485 / 15.26% is within tolerance | Centred fit: yes |
| selection-shuffled-control | not_reproduced | Yes: the printed 5.19% is above the 1% limit | Trials shifted once before the test: yes |
| fig1h-preferred-headings-tile | partially_reproduced | Yes | Centred fit, and the cue position is unknown: yes |
| fig2f-head-chamber-same-preference | partially_reproduced | Yes, though generously: matched ROIs are no closer than random pairs in any pair (cell 9) | Mirroring the chamber-rotation heading and using 5 of 7 pairs: stated, not checked against data |
| fig3c-coherent-remapping | partially_reproduced | Yes | Centred fit: yes |
| fig4-axons-light-on-shape | reproduced | Yes (reading b) | n/a |
| fig4-axons-light-off | partially_reproduced | Yes | n/a |
| figs5-rotation-direction | reproduced | Yes, but fragile: by mouse only SKKS125 passes (p = 0.044), and the pooled random pairs cross files | n/a |
| figs6-arena-control | not_reproduced | Yes, which changes my round-1 view. Without the 6-bin pair p = 0.9, and no pair passes alone (p 0.781 to 1). The pooled pass comes from mixing files. | Leaving that pair out: yes |
| fig5-three-classes | not_reproduced | Yes. The printed variant does peak at k = 3, but the criterion only reports the variant. | n/a |
| fig5-class-proportions | not_reproduced | Yes | n/a |
| fig5e-alignment-peaks-coregistered | partially_reproduced | I now accept this instead of not_reproduced. Against the random-pairing null a small excess remains (share 0.002; 29.2% vs 26.2% within 18°). "Always" fails. | n/a |
| fig5f-heading-flip-unchanged | partially_reproduced | Yes (printed p = 0.141) | n/a |
| fig5gh-landmark-alignment-flip-drop | partially_reproduced | Yes | n/a |
| fig5i-axons-in-clusters | partially_reproduced | Yes | n/a |
| fig5k-visual-cue-only | blocked (metadata_insufficient) | Yes. No other file shares the ROI count, and the blocks differ only in direction (directions cell 12). data_missing could equally be argued. | n/a |
| fig6a-population-light-on | not_reproduced | Yes | n/a |
| fig6a-population-light-off | partially_reproduced | Yes: 0.569 is outside 0.44 ± 0.10 | Bayes decoder: stated; reasonable but weak (see part 3) |
| fig6b-heading-cells | partially_reproduced | Yes | Bayes decoder: as above |
| fig6b-landmark-cells | partially_reproduced | Yes | Bayes decoder: as above |
| fig6b-alignment-cells | not_reproduced | Yes. For dF/F the paired p is 0.011 but the unpaired p is 0.053; the "between the other classes" condition fails anyway. | n/a |
| fig6b-180-errors | reproduced | Yes, under Bayes | Bayes decoder: as above |
| fig6-heading-below-population | reproduced | Yes | n/a |

**Places where the claims file misreads its sources (reported, not corrected):**
- **Trial rule:** the opening comment paraphrases the code's rule `any(90 - abs(prctile(h,[25,75])) > 50)`, which drops segments with |p| < 40, as "more than 50 degrees from ±90". That wording would also drop |p| > 140. `rsc.py` follows the code.
- **selection-shuffled-control:** the criterion names both "before the test" and `calculateHeadDirection_shuff`, which re-shuffles in every iteration. Those are two different procedures, and the second cannot fail.

**2. Sentences the printed numbers don't support**

**(a) Statements that contradict the printed output:**
- **somata cell 11, attempt record fig5-three-classes (notes and response):** "The reviewer-code variant … has none either (selective 0.450, 0.036, 0.007)". The printed values are {2: 0.1136, 3: 0.3926, 4: 0.0043} (cell 10), which is a local maximum at 3.
- **decoding cell 23, attempt record fig6b-landmark-cells:** "The light-off intervals exclude 0.18 (by 0.001 for spikes)". The printed spikes interval is [0.175, 0.199], which includes 0.18 (cell 22). The outcome is unaffected, because light-on fails anyway.
- **Attempt record, fig6a-population-light-off:** "HeadingDecoder … intervals including chance". The printed intervals are [0.101, 0.178] and [0.112, 0.176] (cell 16), which include neither 0.10 nor 0.18.
- **somata cell 17:** the heading-like and landmark-like random-pairing shares are given as "0.368 and 0.510". Printed: 0.677 and 0.230 (cell 16).
- **axons cell 12:** reading (a) is given as "medians 0.143 … Mann-Whitney p = 0.074 … 40 of 135 … Fisher p = 2.8e-07". Printed: 0.134, p = 0.15, 39/135, Fisher p = 5.4e-07 (cell 11). Reading (b) is given as "p = 0.3 … 94 of 1084 … Fisher p = 0.026". Printed: 0.35, 93, 0.035.

**(b) Other numbers that don't match the printed outputs** (no outcome changes):
- **single_cue:**
  - Cell 17: 486 / 15.29% (printed 485 / 15.26%); 394 / 12.39% (printed 393 / 12.36%); 5.22% (printed 5.19%).
  - Cell 21: 166 / 5.22%, 481 reliable (printed 165, 5.19%, 478).
  - Cell 25: 486; 40.5% (printed 0.404); Rayleigh p = 1.7e-05 (printed 2e-05); 40.1% (printed 0.400). "SKKS090 and SKKS091 peak near +90 to +120": SKKS091 peaks at +60 to +90 (cell 23).
- **rotation_remapping cell 10:** "0.21 to 0.998" (printed minimum 0.222); "53 to 83%" (printed 52%); "12 degrees in a chamber-rotation file": one chamber-rotation file shifts 1° (cell 9).
- **axons cell 9:** −0.206 (printed −0.207).
- **somata:**
  - Cell 11: silhouettes 0.274/0.023/0.039 and 0.189/0.143/−0.054 (printed 0.272/0.019/0.032 and 0.190/0.120/−0.052).
  - Cell 14: 12.4/8.8/78.9%, 12.2/8.6/75.3%, and counts 194/75 (printed 13.5/7.6/78.9, 13.3/7.4/75.3, and 202/67).
  - Cell 17: 743.2, 669.4, 706.9, 727.7, 29.1% (printed 743.5, 669.5, 707.2, 728.4, 29.2%).
  - Cell 20: n = 194, 0.374/0.282, F(1,386) = 1.8, p = 0.18, variant p = 0.14; landmark n = 75, F(1,148) = 47.3, p = 6.0e-12 (printed n = 202, 0.378/0.279, F(1,402) = 2.2, p = 0.141, variant p = 0.116; n = 67, F(1,132) = 44.3, p = 2.8e-11).
  - Cell 23: 88.9/86.8%, 71.9/61.9%, 84.8 to 96.2%, 79.8 to 91.5%, LDA 83.7% (printed 88.1/83.0, 72.4/55.5, 84.3 to 96.2, 81.0 to 92.5, 85.2).
- **directions:**
  - Cell 7: 0.211/0.122, p = 0.165, 0.046/0.114/0.697 (printed 0.210/0.118, 0.16, 0.044/0.119/0.699).
  - Cells 10 and 14: n = 382, median 0.026 vs −0.031, p = 0.034, (a) p = 0.912; without the pair n = 270, p = 0.969/0.903, 0.090 vs 0.104 (printed 381, 0.027 vs −0.011, 0.026, 0.889; 269, 0.973/0.9, 0.093 vs 0.086).
- **decoding:**
  - Cell 20: 175 cells used, 0.425/0.372, 0.407/0.344, p 0.31 to 0.97, HeadingDecoder 0.127 to 0.148 (printed 179; 0.429/0.377; 0.415/0.341; 0.170 to 0.964; 0.130 to 0.146).
  - Cell 23: 54 cells used; 0.210 [0.195, 0.223]; 0.192 [0.181, 0.205]; light-on 0.397/0.395; HeadingDecoder 0.207 (printed 50; 0.207 [0.192, 0.220]; 0.187 [0.175, 0.199]; 0.396/0.383; 0.201).
  - Cell 26: 0.721/0.579, 0.712/0.579, heading-like 0.425/0.407, landmark-like 0.397/0.395, p = 0.010.
  - Cell 29: 11.9/13.7%, 7.1%, 0.105, range 0.105 to 0.158 (printed 0.120/0.136, 0.070, 0.104, 0.104 to 0.159).
  - Cell 32: the heading-like intervals.
  - Cells 14 and 17: spikes intervals [0.677, 0.745] and 0.571 [0.537, 0.606] (printed [0.678, 0.746] and 0.572 [0.535, 0.608]).
- **Attempt record:**
  - `measured` values: fig1g (15.29, 486), fig5-class-proportions (8.8, 12.4), fig6b-heading/landmark/alignment.
  - The notes and responses for fig1g, selection-shuffled-control, fig4-axons-light-off, figs5, figs6, fig5-three-classes, fig5-class-proportions, fig5e, fig5f, fig5gh and fig5i repeat the run that isn't shown.
  - The selection-shuffled-control finding says "5.22%", while the centring finding says "15.26%", the printed value. The record therefore mixes the two runs.
- **Stale cell 0 tables:** `axons.ipynb` lists the fig5 claims and says fig5k and Figure 6 are "recorded in the attempt record". `somata.ipynb` lists the fig4 claims.
- **Checked and found consistent:** the README outcome table matches the attempt record.

**(c) Do the round-1 reasons appear in my own words?** Yes. All 24 `reason` entries summarise my round-1 points faithfully.

**3. Round-1 points**

**Resolved:**
- **B2:** the outcome is now not_reproduced under the "once" reading.
- **B3:** both nulls added; I accept the partial outcome.
- **B5 and B6:** acknowledged; the outcomes that inherit the classes are downgraded.
- **B8:** reading (a) added.
- **B10:** run without the 6-bin pair shown; outcome changed.
- **B11:** `rsc.py` matches the code.
- **B12:** stated as an assumption.
- **B14:** that pair enters only the "either" readings.
- **B15:** recorded as a finding.
- **fig5k and fig6:** now tested.

**Remaining, and bearing on a conclusion:**
1. **Which run the conclusions describe (new).** The conclusions, Summaries and attempt record describe a run whose outputs aren't in the notebooks. Two statements are reversed by the printed output (somata cell 11; decoding cell 23 and the fig6a-light-off note). The notebooks need re-executing on the machine that produced the text, or the text rewriting from the printed outputs.
2. **B1, the selection test passes noise.** This is now quantified (4.7% of synthetic untuned cells; 5.19% of shuffled real cells) but not fixed. About a third of the selected cells could pass by chance, and every downstream claim inherits this.
3. **B4 and B7, fig2f.** Derotation artefacts are not excluded: head-rotation files show 52 to 83% selective cells and up to 3.19 spikes/s. The timing alignment of heading and activity is not established: the lag is −6 in one of the four files. Matched ROIs do no better than random pairs. The outcome rests on mirroring the chamber-rotation heading and using 5 of 7 pairs, neither checked against data. A further oddity: SKKS112-PlatformRotation-002 barely rotates (median step 0.12°/frame).
4. **Decoder choice.** The Bayes reading, on which 4 outcomes rest, is chosen partly because the reimplemented HeadingDecoder "decodes near chance". In fact its light-on accuracy is 0.20 to 0.22, twice chance, with intervals that exclude 0.10. The lab's own decoder performing this poorly points more to a reimplementation problem than to the decoder being the wrong reading, and that isn't checked.
   - Separately, training on even and testing on odd heading-resampled bins, about 1.8° apart and interpolated from the same frames, risks leakage between training and test data. That would inflate the Bayes accuracies.
5. **B9, fig1h.** The cue's position in the heading frame is still unknown, so the overrepresentation part of the claim cannot be judged.

## End of run

16 turns, 4 minutes, result: success.
