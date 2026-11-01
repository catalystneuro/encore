# 001277 · verifier-2 · run 41355968714

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 2416
drwxr-xr-x 6 runner runner     4096 Nov  1 22:25 .
drwxr-xr-x 7 runner runner     4096 Nov  1 22:25 ..
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 22:11 .bash_profile
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 22:11 .bashrc
drwxr-xr-x 5 runner runner     4096 Nov  1 22:25 .claude
-rw-r--r-- 1 runner runner        0 Nov  1 22:25 .env
-rw-r--r-- 1 runner runner        0 Nov  1 22:25 .env.development
-rw-r--r-- 1 runner runner        0 Nov  1 22:25 .env.development.local
-rw-r--r-- 1 runner runner        0 Nov  1 22:25 .env.local
-rw-r--r-- 1 runner runner        0 Nov  1 22:25 .env.production
-rw-r--r-- 1 runner runner        0 Nov  1 22:25 .env.production.local
-rw-r--r-- 1 runner runner        0 Nov  1 22:25 .env.test
-rw-r--r-- 1 runner runner        0 Nov  1 22:25 .env.test.local
drwx------ 2 runner runner     4096 Nov  1 22:25 .git
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 22:11 .gitconfig
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 22:11 .github
-rw-r--r-- 1 runner runner        0 Nov  1 22:25 .gitmodules
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 22:11 .idea
crw-rw-rw- 1 nobody nogroup    1, 3 Nov  1 22:11 .mcp.json
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 001277-silkuniene-2025-01.yaml
```

```
# Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025) from dandiset 001277

Tests the findings of [Silkuniene et al. (2025)](https://doi.org/10.1016/j.bioelechem.2025.109016)
that can be tested on [DANDI:001277](https://dandiarchive.org/dandiset/001277/0.250701.1610). The
dandiset holds the pulse-duration experiment of Figure 6: whole-well YO-PRO-1, Hoechst and propidium
images of 18 CT26 monolayers exposed to packets of 300-, 600- or 900-ns pulses from a four-electrode
array. The packet-rate, raised-electrode, burst-number and thermometry experiments are not in it.

| Claim | Outcome |
|---|---|
| The central YP peak is highest at 900 ns, without a significant difference | Reproduced (assumption on the wells) |
| Normalized YP declines similarly for the three pulse durations | Not reproduced |
| FWHM falls with pulse duration (p = 0.003) | Blocked: methods underspecified |
| FWHM at 600 and 900 ns each smaller than at 300 ns | Blocked: methods underspecified |
| FWHM at 900 ns is 1.7 mm, 11.1% of the gap | Blocked: methods underspecified (depends on the claim above) |
| Pr fits a Gaussian and YP a Lorentzian better | Blocked: metadata insufficient |
| The YP spot is slightly larger than the Pr spot | Blocked: metadata insufficient |
| Figures 2, 3, 4, 7 and the raised electrodes of Figure 5 (ten claims) | Blocked: data missing |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
[... 435 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1016-j.bioelechem.2025.109016.yaml | head -250
```

```
# Claims for Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025) on dandiset 001277.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
# protocol as stated in docs/protocol.md.
#
# Source: the accepted author manuscript in PubMed Central (PMC12331426, NIHMS2087238), full
# text as served by ncbi_pmc, read from its Methods, Results and figure legends. PMC lists no
# supplement and the text cites none. No PDF was stored, so the figures were not seen; numbers
# shown only in figures could not be read and are not claimed. The paper links no code (its
# Data availability says "Data will be made available on request"); analysis was done in
# MetaMorph 7.8.13, RStudio, Excel and Grapher 16, with no scripts given.
#
# Data the paper reports. Monolayers of CT26 mouse colon carcinoma cells (all experiments) and
# CHO-K1 cells (burst-number experiments only), in 6-well plates. Four hollow needle electrodes
# (2.8 mm outer diameter) in a square with 15.3-mm side-to-side diagonals, touching the dish
# bottom unless raised by 1 or 2 mm (Fig. 5). Each well was stained with Hoechst before
# exposure, exposed in 1 uM YO-PRO-1 (YP), incubated 30 min, rinsed and imaged as one stitched
# whole-well image (4x, FITC cube; Hoechst with DAPI cube). In cell-killing experiments the
# wells were also stained with propidium (Pr) 2 h later and imaged with a Cy3 cube, and
# re-imaged for Hoechst. Measured variable is the background-subtracted fluorescence in
# 325 x 406 um ROIs along the two diagonals (and in one set along lines through the centre
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:\|^  - id:" 10.1016-j.bioelechem.2025.109016.yaml; grep -n "id:\|depends_on" 10.1016-j.bioelechem.2025.109016.yaml
```

```
17
60:  id: "001277"
63:- id: fig6b-peak-900ns-not-significant
80:- id: fig6c-normalized-decline-similar
96:- id: fig6d-longer-pulses-sharper-peak
119:- id: fig6d-600-900-differ-from-300
137:  depends_on:
148:- id: fig6d-900ns-fwhm
154:  depends_on:
170:- id: fig3-cancan-centre-enhancement
185:- id: fig3-lorentzian-decline
200:- id: fig4b-suppression-near-electrodes
220:- id: fig4b-centre-no-rate-effect
232:- id: fig4c-fwhm-falls-with-rate
283:- id: fig5-raised-electrodes-weaker-centre
293:- id: fig5-yp-lorentzian-pr-gaussian
323:- id: fig5-yp-spot-slightly-larger-than-pr
333:- id: fig7be-burst-number-centre
356:- id: fig7-fwhm-burst-number
376:- id: fig7-sharpest-peak-1-burst-ct26
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' > $TMPDIR/nb.txt
import json
nb=json.load(open('reproduce_silkuniene_2025.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"\n======== CELL {i} [{c['cell_type']}] ========")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--- OUT ---\n'+''.join(o['text']))
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d and 'image/png' not in d: print('--- OUT ---\n'+''.join(d['text/plain']))
            elif 'image/png' in d: print('--- [image] ---')
        if o.get('output_type')=='error': print('ERROR', o.get('ename'), o.get('evalue'))
EOF
wc -l $TMPDIR/nb.txt; grep -n "======== CELL" $TMPDIR/nb.txt | wc -l
```

```
1458 /tmp/claude-1001/nb.txt
55
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	
2	======== CELL 0 [markdown] ========
3	# Silkuniene et al. (2025) from dandiset 001277
4	
5	Paper: Silkuniene G, Silkunas M, Pakhomova ON, Semenov I, Pakhomov AG, "MHz compression of pulse
6	packets facilitates remote focusing of electroporation", Bioelectrochemistry 166 (2025) 109016,
7	[doi:10.1016/j.bioelechem.2025.109016](https://doi.org/10.1016/j.bioelechem.2025.109016).
8	
9	Dataset: [DANDI:001277](https://dandiarchive.org/dandiset/001277/0.250701.1610), version
10	`0.250701.1610` ([doi:10.48324/dandi.001277/0.250701.1610](https://doi.org/10.48324/dandi.001277/0.250701.1610)).
11	The paper cites no version (its data statement says data are available on request). This is the
12	only published version, and the draft has the same 49 assets and size and has not been modified
13	since it was published, so the most recent published version is pinned.
14	
15	Claims: `claims/001277/10.1016-j.bioelechem.2025.109016.yaml`, written from the accepted author
16	manuscript in PubMed Central (PMC12331426), Methods, Results and legends; no supplement.
17	
18	The dandiset holds one experiment of the paper: the pulse-duration comparison of Fig. 6 (CT26
19	cells, packets of 300, 600 or 900 ns pulses with no interval, 2 bursts (x4)). It holds 18 wells on
20	three plates, with a Hoechst image before exposure, a YO-PRO-1 (YP) image 30 min after it, and on
[... 599 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 620,
 "limit": 450
}
```

```
620	      % (sum(r["highest"] == 900 for r in res), len(res),
621	         sum(min(r["p_bonf 900v300"], r["p_bonf 900v600"]) < 0.05 for r in res), sum(r["anova p"] < 0.05 for r in res)))
622	--- OUT ---
623	main (5 complete rows)
624	  centre YP mean, s.e., n: {300: (550.7, 125.9, 5), 600: (865.6, 249.2, 5), 900: (899.2, 307.6, 5)}  highest: 900
625	  (a) Bonferroni p: 900v300 0.975, 900v600 1.000, 600v300 0.876; Cohen's d 900v300 0.66, 900v600 0.05
626	  (b) ANOVA F = 0.64, p = 0.543
627	all 7 at 600 ns
628	  centre YP mean, s.e., n: {300: (550.7, 125.9, 5), 600: (829.5, 175.8, 7), 900: (899.2, 307.6, 5)}  highest: 900
629	  (a) Bonferroni p: 900v300 0.975, 900v600 1.000, 600v300 0.791; Cohen's d 900v300 0.66, 900v600 0.12
630	  (b) ANOVA F = 0.70, p = 0.515
631	main, background from all 4 footprints
632	  centre YP mean, s.e., n: {300: (540.9, 124.1, 5), 600: (857.1, 250.1, 5), 900: (890.3, 307.3, 5)}  highest: 900
633	  (a) Bonferroni p: 900v300 0.968, 900v600 1.000, 600v300 0.871; Cohen's d 900v300 0.67, 900v600 0.05
634	  (b) ANOVA F = 0.65, p = 0.541
635	main, centre from Lorentzian a
636	  centre YP mean, s.e., n: {300: (564.4, 133.9, 5), 600: (874.1, 250.1, 5), 900: (905.9, 312.4, 5)}  highest: 900
637	  (a) Bonferroni p: 900v300 1.000, 900v600 1.000, 600v300 0.920; Cohen's d 900v300 0.64, 900v600 0.05
638	  (b) ANOVA F = 0.60, p = 0.565
639	every 5 of 7 at 600 ns: 900 ns highest in 14 of 21; any (a) p < 0.05 in 0; ANOVA p < 0.05 in 0
[... 430 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1069,
 "limit": 400
}
```

```
1069	======== CELL 38 [code] ========
1070	rows = []
1071	for spacing, half, pooling in readings:
1072	    v = np.array([cc.fwhm(meas[w], spacing, half, pooling)["fwhm"] for w in main[900]])
1073	    m, s = cc.mean_se(v)
1074	    rows.append({"spacing": spacing, "half_mm": half, "pooling": pooling, "fwhm_mean": m, "fwhm_se": s,
1075	                 "pct_of_15.3": 100 * m / cc.DIAGONAL_GAP_MM, "pct_se": 100 * s / cc.DIAGONAL_GAP_MM,
1076	                 "fwhm_ok (1.62-1.78)": abs(m - 1.7) <= 0.08 + 1e-12, "pct_ok (10.5-11.7)": abs(100 * m / 15.3 - 11.1) <= 0.6 + 1e-12})
1077	t900 = pd.DataFrame(rows)
1078	print(t900.round(3).to_string())
1079	print("readings with both values within tolerance: %d of %d" % ((t900["fwhm_ok (1.62-1.78)"] & t900["pct_ok (10.5-11.7)"]).sum(), len(t900)))
1080	print("per-well 900-ns FWHM, contiguous, 5 mm:", [round(cc.fwhm(meas[w], "contiguous", 5.0, "avg")["fwhm"], 2) for w in main[900]])
1081	--- OUT ---
1082	       spacing  half_mm pooling  fwhm_mean  fwhm_se  pct_of_15.3  pct_se  fwhm_ok (1.62-1.78)  pct_ok (10.5-11.7)
1083	0          1mm      4.0     avg      1.784    0.097       11.663   0.637                False                True
1084	1          1mm      4.0     all      1.784    0.097       11.663   0.637                False                True
1085	2          1mm      5.0     avg      1.793    0.100       11.718   0.656                False               False
1086	3          1mm      5.0     all      1.793    0.100       11.718   0.656                False               False
1087	4          1mm      6.0     avg      1.799    0.103       11.759   0.671                False               False
1088	5          1mm      6.0     all      1.799    0.103       11.759   0.671                False               False
[... 371 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 283,335p 10.1016-j.bioelechem.2025.109016.yaml
```

```
- id: fig5-raised-electrodes-weaker-centre
  statement: Raising the electrodes 1 or 2 mm above the monolayer weakens electroporation in
    the central spot, with practically no YP staining near electrodes at any height.
  source: Results 3.2, paragraph 1; Figure 5A and 5B
  quote: there was practically no YP staining near electrodes to start with, so the only clear
    effect of raising electrodes was the weakening of electroporation in the central spot
  criterion: Diagonal YP profiles at 0, 1 and 2 mm elevation (n=6-7). Reproduced when mean
    central YP at 0 mm exceeds that at 1 mm and at 2 mm by the Methods' error-bar gap rule.
    The paper sets no threshold for "practically no" staining near electrodes, so YP at 6
    and 7 mm, as percent of the 0-mm centre, is reported and not judged.
- id: fig5-yp-lorentzian-pr-gaussian
  statement: The decline of Pr staining (cell killing) from the centre fits a Gaussian better
    than a Lorentzian (R2 0.96 against 0.92), while YP fits a Lorentzian better (0.98 against
    0.95), fitted from -5 to 5 mm.
  source: Results 3.2, paragraph 3; Figure 5B, left panel
  quote: For Pr data in the left panel of Fig. 5B , the coefficient of determination increased
    from 0.92 for Lorentzian fit to 0.96 for Gaussian fit. YP data showed the opposite trend,
    with the coefficients of 0.98 and 0.95 for Lorentzian and Gaussian fits
  statistics:
  - about: significance of each of the four fits
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i "Fig. 5\|Figure 5\|left panel\|2.4\|Gaussian" paper/*.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import re
t=open('paper/10.1016-j.bioelechem.2025.109016.txt').read()
for pat in ['left panel','Fig. 5B','Fig. 5 ','Fig. 5.','raised','Gaussian']:
    for m in re.finditer(re.escape(pat),t):
        print(pat,'::',t[max(0,m.start()-300):m.end()+300].replace('\n',' '))
        print('---')
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import json,base64,os
nb=json.load(open('reproduce_silkuniene_2025.ipynb'))
for o in nb['cells'][42]['outputs']:
    if 'data' in o and 'image/png' in o['data']:
        open(os.environ['TMPDIR']+'/c42.png','wb').write(base64.b64decode(o['data']['image/png']))
"; ls -la $TMPDIR/c42.png
```

```
-rw-r--r-- 1 runner runner 264048 Nov  1 22:26 /tmp/claude-1001/c42.png
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c42.png"
}
```

Result: no output.

**Agent calls Grep**

```json
{
 "pattern": "checked in the notebook|scaled",
 "path": "cancan.py",
 "output_mode": "content"
}
```

```
326:                      scaled: bool = True) -> tuple[np.ndarray, np.ndarray]:
330:    shape (2, len(x)), one row per diagonal. Distances are scaled to the paper's geometry: a
333:    difference in the stitched image's scale. scaled=False uses the pixel size of the OME
344:        scale = np.hypot(*half) / FOOTPRINT_CENTRE_MM if scaled else 1 / BLOCK_MM  # blocks per mm
```

**Agent**

**Round-2 verification: Silkuniene et al. 2025 (doi:10.1016/j.bioelechem.2025.109016) on DANDI:001277 v0.250701.1610**

The claims file has 17 claims and the attempt record has 17 outcomes, one per claim. Cell numbers below refer to the re-executed notebook. They sit one higher than in round 1 from cell 9 on, because a channel-metadata cell was added.

**1. Outcomes and assumptions**

| Claim | Record | I agree? | Notes |
|---|---|---|---|
| fig6b-peak-900ns-not-significant | reproduced, `assumed: true` | Yes | The assumption (Fig. 6 = the five complete plate rows) is stated in the deviations and is reasonable. Only the "900 ns highest" half depends on it: 900 ns is highest in 14 of 21 subsets (cell 21). No test is significant under any well choice, including the paired variant (cell 23). |
| fig6c-normalized-decline-similar | not_reproduced | Yes | The deviation says the outcome does not rest on the assumption. That is correct: the 300 against 900 ns gap at +2 mm (cell 26) does not involve the 600-ns wells. |
| fig6d-longer-pulses-sharper-peak | blocked, methods_underspecified | Yes | Not reproduced under any well choice except the one that drops both P1 row B wells (cell 31). The notes say this, but the outcome has no `assumed: true`. Under the record's own logic it should carry the flag. |
| fig6d-600-900-differ-from-300 | blocked, methods_underspecified | Yes | Readings differ with the main wells and with all 7 (cell 35: one significant comparison in 12 readings, none in 12, in both sets). It does not rest on the assumption. |
| fig6d-900ns-fwhm | blocked (inherits from parent) | Conditionally | In round 1 I gave reproduced. The claims file does list `depends_on: fig6d-longer-pulses-sharper-peak`. I cannot see docs/protocol.md to check the cited rule (Author, step 1.5). If the rule is as quoted, blocked is correct. The claim's own criterion is met in 6 of 12 readings (cells 38 and 39), and the record says so. The block also inherits the parent's dependence on the well choice, so the missing assumption flag applies here too. |
| fig5-yp-lorentzian-pr-gaussian | blocked, metadata_insufficient | Yes | Now matches my round-1 outcome. |
| fig5-yp-spot-slightly-larger-than-pr | blocked, metadata_insufficient | Yes | Now matches my round-1 outcome. |
| The 10 data_missing claims | blocked, data_missing | Yes | No change from round 1. |

I found no new misreading of the paper in the claims file. My round-1 point 9 still stands as a claims-file comment: the linear trend on the 3 means has 1 degree of freedom, which makes that reading nearly impossible to pass.

**2. Text against the printed outputs**

- **"all 8 readings" in the offset fits.** This appears in cell 44 ("the Gaussian fits the mean Pr profile better than the Lorentzian under all 8 readings"), in the record's fig5-yp-lorentzian-pr-gaussian notes, and in the round-1 response. Cell 43 prints 8 fits, which are 4 readings × 2 functions. The Gaussian is better in all 4 readings.
- **300-ns FWHM range.** Cell 33 and the fig6d-longer notes say "2.11 to 2.13 mm at 300 ns". Cell 30 prints 2.1041 to 2.1352, which is 2.10 to 2.14.
- **1-mm p-value range.** The same text says "10 of 12 with 1-mm steps (p 0.042 to 0.050)". The 10 significant readings run from 0.0419 to 0.0479. The value 0.0504 belongs to the two readings that are not significant.
- **Plate ratio.** Cell 24 and the fig6b notes say "P3 two to four times P1 and P2". Cell 22 gives ratios of 2.1 to 4.6 (at 900 ns, 1630 against 357).
- **Where the fig6c gaps fall.** Cell 28 and the fig6c notes say "The gaps are mostly between 300 and 900 ns at 1 to 2 mm". In cell 26, with the main wells and contiguous ROIs, 8 of the 12 to 14 gaps are 300 against 600 ns, and some gaps lie at 2.4 to 4.9 mm and 6.9 mm. Over all readings, 300 against 900 ns accounts for 52 of 96 gaps.
- **Subsets in fig6c.** Cell 28 lists "every choice of 5 of the 7" among the readings, but cell 26 runs the subsets only for 1-mm steps, ±5 mm and the mean-bar rule. The outcome still holds, because the 300 against 900 ns gap does not depend on the 600-ns wells.
- **Unscaled distances.** The Summary (cell 54) says "unscaled distances give the same outcomes". Cell 39 runs unscaled distances only for the three fig6d claims, not for fig6c or Fig. 5.
- **Cell 0 status table.** It still lists fig6d-900ns-fwhm and both Fig. 5 claims as "tested", which contradicts cells 40, 47, 51 and 54.
- **README overall.**
  - "18 CT26 monolayers exposed to packets of 300-, 600- or 900-ns pulses": cell 4 shows 17 exposed wells and 1 sham.
  - "With those rows the FWHM trend is close to the paper's under most readings": the slope is significant in 28 of 48 readings (cell 30), and p is near 0.003 only in the 12 contiguous readings on individual values.
  - "about ten minutes" and "about 13 GB": no output shows these, and cell 0 says streaming takes about 8 minutes.
- **What checks out.** Every other number in the "**Result:" cells (24, 28, 33, 36, 40, 47, 51), the Summary, the README and the record's notes and findings matches the outputs. I also confirmed from the cell-42 figure that two footprint marks in P1_20240926_B3 fall on no visible footprint, as cell 44 says.
- **My round-1 reasons.** The record states them in my own words and faithfully. For fig6b, fig6d-longer and fig5-yp-lorentzian, points from section B of my report were merged into the outcome reason. The meaning is unchanged.

**3. Round-1 points**

Resolved:
- **Point 1 (Fig. 5 well assumption):** both Fig. 5 claims are now blocked.
- **Point 3 (which channel is Pr):** cell 9 reads the OME metadata: channel 0 is Cy3 (565 nm) in all 5 files.
- **Point 4 (Pr footprints in P1_20240926_B3):** cell 43 adds the rim contrast, and readings that leave that well out are shown.
- **Point 5 (distance scaling):** cell 39 adds the unscaled variant. The fig6d results are unchanged and the 900-ns FWHM is within tolerance in 6 of 12 readings.
- **Point 6 (overlapping contiguous ROIs):** now stated in a deviation and in cell 47.
- **Point 8 (identical pooling readings):** stated in cell 29.
- **Point 10 (plate-row blocking):** cell 23 adds a paired variant, which also finds no difference.
- **Section C:** per-well Pr profiles, fits with an offset and the Pr rim contrast are now shown.

Unchanged, but they do not affect a conclusion:
- Point 7 (the darkest-footprint background).
- Point 9 (claims-file comment, above).
- The pre-exposure Hoechst images are still not used, and plate P3 has no 2-h check that cells were present at the centre.

Remaining issues that bear on a conclusion:
1. **fig6d-longer-pulses-sharper-peak and fig6d-900ns-fwhm** depend on leaving out P1_20240926_B2 and B3. With either well kept, fig6d-longer becomes not reproduced. The notes say this, but neither outcome is marked `assumed: true`.
2. **fig6d-900ns-fwhm** is blocked only through the protocol's dependency rule, which I could not check. If the rule does not apply, its own criterion gives reproduced.
3. **Miscounts and imprecise ranges** listed in section 2 (the "8 readings", the 300-ns FWHM range, the 1-mm p range, the plate ratio, where the fig6c gaps fall, the "same outcomes" claim, the stale cell-0 table). None changes an outcome, but they should be corrected.

## End of run

15 turns, 2 minutes, result: success.
