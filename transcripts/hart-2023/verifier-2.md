# 000467 · verifier-2 · run 41086841439

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 1644
drwxr-xr-x 6 runner runner     4096 Oct 30 17:00 .
drwxr-xr-x 7 runner runner     4096 Oct 30 17:00 ..
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 30 16:06 .bash_profile
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 30 16:06 .bashrc
drwxr-xr-x 5 runner runner     4096 Oct 30 17:00 .claude
-rw-r--r-- 1 runner runner        0 Oct 30 17:00 .env
-rw-r--r-- 1 runner runner        0 Oct 30 17:00 .env.development
-rw-r--r-- 1 runner runner        0 Oct 30 17:00 .env.development.local
-rw-r--r-- 1 runner runner        0 Oct 30 17:00 .env.local
-rw-r--r-- 1 runner runner        0 Oct 30 17:00 .env.production
-rw-r--r-- 1 runner runner        0 Oct 30 17:00 .env.production.local
-rw-r--r-- 1 runner runner        0 Oct 30 17:00 .env.test
-rw-r--r-- 1 runner runner        0 Oct 30 17:00 .env.test.local
drwx------ 2 runner runner     4096 Oct 30 17:00 .git
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 30 16:06 .gitconfig
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 30 16:06 .github
-rw-r--r-- 1 runner runner        0 Oct 30 17:00 .gitmodules
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 30 16:06 .idea
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 30 16:06 .mcp.json
[... 88 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 000467-hart-2023-01.yaml
```

```
<persisted-output>
Output too large (49KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/20492192-0165-493c-a18b-f319b1e192c0/tool-results/bazryd01z.txt

Preview (first 2KB):
# Hart, Frank, Lopes et al. (2023) from dandiset 000467

Tests the calcium imaging findings of [Hart et al. (2023)](https://doi.org/10.1016/j.cell.2023.05.025)
that can be tested on [DANDI:000467](https://dandiarchive.org/dandiset/000467/0.261004.1655), which holds
two-photon volumes of the right antennal lobe (AL) of GCaMP6s clonal raider ants: 6 ants given general
odorants, 3 ants imaged bilaterally, and 13 ants given four alarm pheromones at two concentrations.
The behaviour, transgenesis, confocal and genome data of the paper are not in it.

| Claim | Outcome |
|---|---|
| Each general odorant activates a unique combination of glomeruli, similar across ants | Not reproduced |
| 3-hexanone activates the broadest region | Reproduced |
| Responses to 4-methyl-3-hexanol are bilaterally symmetrical | Partially reproduced |
| The vehicle generates no responses | Not reproduced |
| Odors cause no fluorescence decreases | Not reproduced |
| Responses are often 1 to 2-fold and outlast the pulse | Not reproduced |
[... 16 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/20492192-0165-493c-a18b-f319b1e192c0/tool-results/bazryd01z.txt"
}
```

```
1	# Hart, Frank, Lopes et al. (2023) from dandiset 000467
2	
3	Tests the calcium imaging findings of [Hart et al. (2023)](https://doi.org/10.1016/j.cell.2023.05.025)
4	that can be tested on [DANDI:000467](https://dandiarchive.org/dandiset/000467/0.261004.1655), which holds
5	two-photon volumes of the right antennal lobe (AL) of GCaMP6s clonal raider ants: 6 ants given general
6	odorants, 3 ants imaged bilaterally, and 13 ants given four alarm pheromones at two concentrations.
7	The behaviour, transgenesis, confocal and genome data of the paper are not in it.
8	
9	| Claim | Outcome |
10	|---|---|
11	| Each general odorant activates a unique combination of glomeruli, similar across ants | Not reproduced |
12	| 3-hexanone activates the broadest region | Reproduced |
13	| Responses to 4-methyl-3-hexanol are bilaterally symmetrical | Partially reproduced |
14	| The vehicle generates no responses | Not reproduced |
15	| Odors cause no fluorescence decreases | Not reproduced |
16	| Responses are often 1 to 2-fold and outlast the pulse | Not reproduced |
17	| At most a median of 6 glomeruli per pheromone | Reproduced (assumed) |
18	| Higher concentrations recruit a few more glomeruli | Reproduced (assumed) |
19	| One glomerulus (PGb) shared by the three panic pheromones | Not reproduced |
20	| 6MHO rarely shares glomeruli with the others | Reproduced (assumed) |
[... 736 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1016-j.cell.2023.05.025.yaml"
}
```

```
1	# Claims for Hart, Frank, Lopes et al. (2023), Cell, on dandiset 000467.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
3	# under protocol pilot-10 (docs/protocol.md, Reader).
4	#
5	# Text read. The accepted author manuscript in PubMed Central (PMC10334690, NIHMS1904919), not
6	# the version of record: the Results, Discussion, STAR Methods, Key Resources Table and the
7	# legends of Figures 1 to 6, Table 1 and Figures S1 to S7, as served by PMC. The supplement read
8	# is NIHMS1904919-supplement-1.pdf (Tables S1 to S4 and the supplemental references). The two
9	# supplemental videos were not read. No PDF of the main text was supplied, so values shown only
10	# in figures (the medians written on Figure 6, the boxes of Figure S5, the vectors of Figure 5D)
11	# could not be read; every claim below rests on numbers printed in the text.
12	#
13	# Code read. The Key Resources Table links https://github.com/Social-Evolution-and-Behavior/
14	# HartKronauer2023, which returns 404. The same lab's repository Hart_Kronauer2023 (README
15	# "Processing code for calcium imaging data from" this paper, pointing to dandiset 000467) was
16	# read at commit 72d041a85dcec7c1429351a00a210d2353d0c6db (2023-05-09). It holds two files.
17	# generate_tif_files.py reads each NWB file (one z-plane of one trial, acquisition
18	# "TwoPhotonSeries1") and writes a TIFF; it keeps only trials t288, t293, t284 and t290, a
19	# hard-coded filter that no Methods text explains and that an attempt should not copy.
20	# macro_calcium_imaging.txt is the ImageJ macro for the whole-AL peak maps (below). The ROI
[... 762 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"=== cell {i} [{c['cell_type']}] ===")
    if c['cell_type']=='markdown': print(src); continue
    print(src if len(src)<3000 or '--full' in sys.argv else src[:1500]+'\n...[src truncated]')
    for o in c.get('outputs',[]):
        if o['output_type']=='stream': print('--out--'); print(''.join(o['text']))
        elif o['output_type'] in('execute_result','display_data'):
            d=o['data']
            if 'text/plain' in d and 'image/png' not in d: print('--res--'); print(''.join(d['text/plain']))
            elif 'image/png' in d: print('--[image]--')
        elif o['output_type']=='error': print('--ERR--', o['ename'], o['evalue'])
EOF
for f in general_odorants concentration alarm_pheromones; do python3 $TMPDIR/dump.py $f.ipynb > $TMPDIR/$f.txt; wc -l $TMPDIR/$f.txt; done
```

```
472 /tmp/claude-1001/general_odorants.txt
193 /tmp/claude-1001/concentration.txt
1972 /tmp/claude-1001/alarm_pheromones.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/general_odorants.txt"
}
```

```
1	=== cell 0 [markdown] ===
2	# General odorants and bilateral imaging: Hart, Frank, Lopes et al. (2023), dandiset 000467
3	
4	Paper: Hart T, Frank DD, Lopes LE et al. "Sparse and stereotyped encoding implicates a core glomerulus
5	for ant alarm behavior", Cell 186 (2023), doi:10.1016/j.cell.2023.05.025.
6	
7	Dataset: DANDI:000467, version 0.261004.1655 (doi:10.48324/dandi.000467/0.261004.1655). The paper
8	cites the dandiset without a version. This is the only published version (published 2026-10-04,
9	"after adding additional meta data"); the draft has the same 14,685 assets and size, so the most
10	recent published version is pinned, as the protocol says when the paper cites none.
11	
12	Claims file: `claims/000467/10.1016-j.cell.2023.05.025.yaml`, written from the accepted author
13	manuscript in PubMed Central (PMC10334690) with its supplement. Shared methods M1 to M4 are in its
14	opening comment; the helper `al_imaging.py` says where each parameter comes from.
15	
16	This notebook holds the general odorant experiment (6 ants, Figure 3F-G) and the bilateral imaging
17	(3 ants, Figure S4A). The alarm pheromone claims are in `alarm_pheromones.ipynb`.
18	
19	| Claim | Here |
20	|---|---|
[... 453 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/concentration.txt"
}
```

```
1	=== cell 0 [markdown] ===
2	# Alarm pheromones at two concentrations: Hart, Frank, Lopes et al. (2023), dandiset 000467
3	
4	Paper: Hart T, Frank DD, Lopes LE et al. "Sparse and stereotyped encoding implicates a core glomerulus
5	for ant alarm behavior", Cell 186 (2023), doi:10.1016/j.cell.2023.05.025.
6	
7	Dataset: DANDI:000467, version 0.261004.1655 (doi:10.48324/dandi.000467/0.261004.1655), the only
8	published version; the paper cites none (see `alarm_pheromones.ipynb`).
9	
10	Claims file: `claims/000467/10.1016-j.cell.2023.05.025.yaml` (accepted manuscript, PMC10334690).
11	
12	This notebook tests one claim, figs5a-concentration-more-glomeruli, which needs whole-volume maps
13	(M1) of every pheromone trial at both of each ant's concentrations: 312 trials of 33 planes. It is
14	kept apart from `alarm_pheromones.ipynb` so that each notebook stays under the 30-minute limit.
15	
16	| Claim | Here |
17	|---|---|
18	| figs5a-concentration-more-glomeruli | tested |
19	| all other claims | the other notebooks, or blocked (see the attempt record) |
20	=== cell 1 [code] ===
[... 174 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/alarm_pheromones.txt",
 "limit": 700
}
```

```
1	=== cell 0 [markdown] ===
2	# Alarm pheromone imaging: Hart, Frank, Lopes et al. (2023), dandiset 000467
3	
4	Paper: Hart T, Frank DD, Lopes LE et al. "Sparse and stereotyped encoding implicates a core glomerulus
5	for ant alarm behavior", Cell 186 (2023), doi:10.1016/j.cell.2023.05.025.
6	
7	Dataset: DANDI:000467, version 0.261004.1655 (doi:10.48324/dandi.000467/0.261004.1655). The paper
8	cites the dandiset without a version. This is the only published version (published 2026-10-04,
9	"after adding additional meta data"); the draft has the same 14,685 assets and size, so the most
10	recent published version is pinned, as the protocol says when the paper cites none.
11	
12	Claims file: `claims/000467/10.1016-j.cell.2023.05.025.yaml`, written from the accepted author
13	manuscript in PubMed Central (PMC10334690) with its supplement. The shared methods M1 to M4 are in
14	its opening comment; the helper `al_imaging.py` says where each parameter comes from.
15	
16	This notebook holds the unilateral alarm pheromone experiment (13 ants). The general odorant and
17	bilateral experiments are in `general_odorants.ipynb`. Claims tested here:
18	
19	| Claim | Here |
20	|---|---|
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/alarm_pheromones.txt",
 "offset": 700,
 "limit": 650
}
```

```
700	       aiy        higher     1.0                    6 False
701	       aiy           48%     1.0                    4 False
702	      aiix        higher     2.0                    3 False
703	      aiix           48%     2.5                    1 False
704	      aiiy        higher     2.0                    2 False
705	      aiiy           48%     2.0                    1 False
706	       bix        higher     0.0                    4 False
707	       bix           48%     1.0                    4 False
708	       biy        higher     0.0                    5 False
709	       biy           48%     1.0                    5  True
710	      biix        higher     2.0                    3 False
711	      biix           48%     2.0                    2 False
712	      biiy        higher     2.0                    4 False
713	      biiy           48%     2.0                    2 False
714	
715	=== cell 19 [markdown] ===
716	**Result: not reproduced.** Only biy at 48% meets the criterion (median 1, exactly one shared ROI in 5 of 8 ants). Under bix the median is 0 at the higher concentration (exactly one in 4 of 13 ants, none in 8) and 1 at 48% (exactly one in 4 of 8, not more than half). aix and aiy give a median of 1 with exactly one in 5 or 6 of 13 ants, and the readings ii medians of 2 to 2.5. Under bix heptanone and hexanol share an ROI in 9 of 13 ants, so the overlap is partial and the three-way overlap is often missing. Leaving out the flagged trial gives the same.
717	=== cell 20 [markdown] ===
718	## figs5c-mho-rarely-overlaps
719	
[... 630 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/alarm_pheromones.txt",
 "offset": 1350,
 "limit": 650
}
```

```
1350	                    q = stats.t.ppf(0.975, fa.df_resid)
1351	                    row.update({"(a) pred": pa, "(a) lo": pa - q * sa, "(a) hi": pa + q * sa})
1352	                    try:
1353	                        fb = smf.mixedlm("peak ~ lc", d_, groups=d_.ant).fit(reml=True)
1354	                        fe = fb.fe_params; cv = fb.cov_params().loc[fe.index, fe.index].values
1355	                        xb = np.array([1, x48]); pb = float(xb @ fe); sb = float(np.s
1356	...[src truncated]
1357	--out--
1358	fits with fewer than 2 ants (not fitted): 16 of 96 ; mixed-model fits that failed: 0 ; mixed-model fits not converged: 9
1359	ident    roi plane glom      odor  n trials  n ants  (a) pred  (a) lo  (a) hi  (b) pred  (b) lo  (b) hi (b) converged  (a) responds  (a) no response  (b) responds  (b) no response
1360	  bix   disc     a  PGb heptanone        30       5     0.851   0.742   0.960     0.849   0.583   1.115          True          True            False          True            False
1361	  bix   disc     a  PGb  heptanol        30       5     0.678   0.570   0.786     0.676   0.395   0.957          True          True            False          True            False
1362	  bix   disc     a  PGb   hexanol        30       5     0.734   0.653   0.816     0.733   0.453   1.014          True          True            False          True            False
1363	  bix   disc     a  PGb      6MHO        30       5    -0.087  -0.141  -0.032    -0.084  -0.148  -0.021          True         False            False         False            False
1364	  bix   disc     a  PGa heptanone         0       0       NaN     NaN     NaN       NaN     NaN     NaN           NaN         False            False         False            False
1365	  bix   disc     a  PGa  heptanol         0       0       NaN     NaN     NaN       NaN     NaN     NaN           NaN         False            False         False            False
1366	  bix   disc     a  PGa   hexanol         0       0       NaN 
[... 607 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "DISC2|RankFilter|minimum_filter|def draw_rois|recur|overlap|def _split_wide|GLOM_MIN|GLOM_MAX|def band_for|def trial_m3|stabil|phase",
 "path": "al_imaging.py",
 "output_mode": "content"
}
```

```
26:  mean of the baseline frames by phase correlation on 2 x 2 binned images (whole-pixel
28:  stabilization; "max_shift" and "shift" report how far frames moved.
29:- The Minimum filter's footprint is ImageJ's for radius 2 (RankFilters: dx^2 + dy^2 <= r^2 + 1,
35:  threshold) in each trial's map that recur in another trial of the same odor at a concentration
36:  (claims file, drawing (a); `recurring_regions`), merged into connected regions; reading "a"
37:  keeps them all, reading "b" keeps those at least `GLOM_MIN_UM` across (10 um, the lower end of
39:  odorants") and splits those wider than `GLOM_MAX_UM` (20 um) at local maxima at least 10 um
40:  apart. Regions of different odors that overlap are one ROI when their depths (the plane of
50:  file names (M3). Each plane's row band is stabilized as the maps are (`stabilize_band`), as the
51:  claims file's M3 assumes; the unstabilized disc trace is kept for comparison.
89:GLOM_MIN_UM, GLOM_MAX_UM = 10.0, 20.0
210:# ImageJ "Minimum" radius 2: RankFilters takes the pixels with dx^2 + dy^2 <= r^2 + 1, 21 pixels
211:DISC2 = (np.mgrid[-2:3, -2:3] ** 2).sum(0) <= 2 ** 2 + 1
231:    """M1 for one plane of one trial: the stabilized peak fold change map, minimum-filtered (full
244:    mn = ndimage.minimum_filter(dff, footprint=DISC2)
298:def _split_wide(mask: np.ndarray, value: np.ndarray, reading: str, pixel_um: float = PIXEL_UM) -> list[np.ndarray]:
309:        if diam < GLOM_MIN_UM:
311:        if diam <= GLOM_MAX_UM:
315:        size = int(round(GLOM_MIN_UM / pixel_um / BIN))
325:            if 2 * np.sqrt(sub.sum() / np.pi) * pixel_um * BIN >= GLOM_MIN_UM:
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "al_imaging.py",
 "offset": 290,
 "limit": 330
}
```

```
290	    for o in out.values():
291	        o["proj"] = np.clip(o["proj"], *CLIP)
292	        o["argmax"] = o["planes"].argmax(0)
293	    return out
294	
295	
296	# --- ROIs and counts (M2) --------------------------------------------------------------------
297	
298	def _split_wide(mask: np.ndarray, value: np.ndarray, reading: str, pixel_um: float = PIXEL_UM) -> list[np.ndarray]:
299	    """Connected regions of a mask; under reading b, drop those under 10 um across and split those
300	    over 20 um at local maxima at least 10 um apart (watershed on the value map)."""
301	    lab, n = ndimage.label(mask)
302	    regions = []
303	    for k in range(1, n + 1):
304	        reg = lab == k
305	        diam = 2 * np.sqrt(reg.sum() / np.pi) * pixel_um * BIN
306	        if reading == "a":
307	            regions.append(reg)
308	            continue
309	        if diam < GLOM_MIN_UM:
[... 310 more lines not kept]
```

**Agent**

**Verifier report, round 2: Hart et al. 2023 on DANDI:000467 (0.261004.1655)**

The claims file has 32 claims. The attempt record tests 17 and blocks 15.

## 1. Outcomes

**Blocked (15).** I agree with all 15.
- 8 are blocked as data_missing: fig1cd, fig1e, the three fig1f claims, table1, fig2b-s1a and figs2cf.
- 7 are marked `data: elsewhere` in the claims file. The author kept other/not_runnable as their reasons and explained why. I accept that and drop my round-1 data_missing reason.

**Tested (17).** I agree with 15 of them:
- fig3f: not_reproduced
- fig3fg: reproduced (ratio 2.57 after the kernel fix)
- fig4b: not_reproduced
- fig4-no-decreases: not_reproduced (under the reader's rule; the placement points to motion)
- fig4-large-lasting: not_reproduced
- figs5a-sparse: reproduced
- figs5a-concentration: reproduced
- figs5b: not_reproduced
- fig6, imaging half: not_reproduced
- fig5ab: not_reproduced
- fig5d: not_reproduced
- fig5c-s6: partially_reproduced
- fig5c-6g-slow: partially_reproduced
- figs7a: not_reproduced
- figs7c: not_reproduced

I disagree with two:
- **figs5c-mho-rarely-overlaps (reproduced, assumed).** The criterion says "Reproduced when, under each M2 reading…". The four ROI-maximum readings fail: medians 1 to 3, with shared ROIs in 11 of 13 ants (cell 21). By that rule the outcome is not_reproduced. The attempt applies the same "each reading" wording literally for figs5b but not for figs5c. fig6 is not affected, since it is already not reproduced.
- **figs4a-bilateral-symmetry (partially_reproduced).** I still think this is not_reproduced. The criterion needs both parts in every ant, defines no partial outcome, and the count part fails under every reading (cell 14). This is a classification point and the disagreement is recorded.

**Assumptions (`assumed: true`).** All are stated.
- **figs5a-sparse:** reasonable. Its criterion accepts "a reading", so it hardly needs the assumption.
- **figs5a-concentration:** reasonable. 5 of the 8 readings meet it. As the notebook itself says, drawing ROIs at the higher concentration favours the subset part.
- **figs5c:** stated, but it overrides the criterion (above).
- **fig5c-s6, fig5c-6g-slow, figs7c:** the disc ROI is reasonable. These outcomes also rest on the aiiy identification, which uses the ROI maximum and drawing a. That is the reading the attempt sets aside for figs5a and figs5c. PGa comes from 4 ants (3 at 48%). The record states all this, but the inconsistency is not named.
- **fig5c-6g-slow:** the PGa part passes trivially. PGa's hexanol trace peaks at only 0.129 to 0.148, so there is no response to decline. "Partial" is fair.

## 2. Text against printed outputs

Nearly every number checks out. These do not:
- **Alarm notebook, cell 53 (Summary):** "the readings with the ROI's maximum do not [meet the criteria]". For figs5a, biix and biiy meet it (largest median 4, cell 15). The readings that fail are aiy, aiix and aiiy. The paragraph also leaves out figs5a-concentration, which the table marks "(assumed)".
- **Cell 35, and the fig5d deviation in the attempt record:** "PGa anterior and 6G lateral of PGb hold by construction". Cell 36 prints False for these:
  - "PGa anterior in all": aiiy bc, biix bd, biiy bd
  - "6G lateral in all": aiix bd, aiiy ad and bd, aiy ad and bd, biix ac, biiy ac

  The centres are re-estimated after identification, so the condition does not hold by construction. It does not change the outcome. My round-1 point 10 made the same wrong claim.
- **Cell 49, and the figs7a notes:** "One trial returns more than 100 s". Under the region ROI with return reading b, two trials do (105.9 to 110.9 s and 100.7 to 105.7 s, cell 48).
- **figs7c notes:** "All fits converged". Cell 51 prints convergence only for the coefficient-test (c) fits, not for the ML fits behind reading (a).
- **fig3fg notes:** the explanation that "ethylpyrazine's area falls more than 3-hexanone's" compares with round-1 numbers, which no current output shows.
- **README:** the runtimes "about 21 minutes" and "about 17 minutes" do not match the printed 24.6 min (alarm notebook, cell 54) and 20.2 min (concentration notebook, cell 10).

My round-1 reasons are reproduced faithfully in `verifications.results[].reason`, mostly verbatim. Where a sentence was added, it summarises my own numbered problems or notes my data_missing choice. Nothing is misattributed.

## 3. Round-1 points

**Resolved:**
1. Traces under a second identification: aiiy was added. It gives 5 of 5 ants for figs7a.
2. figs7c: the untestable case is now printed ("NOT TESTED", cell 51).
3. Stabilization: the bands are now stabilized. Against the unstabilized traces r = 0.98, and 3 of 129 trials change side of 0.2.
4. Problem 5: vehicle AL fractions are printed, with the exclusion variant.
5. Problem 6: the region ROI was run.
6. Problem 7: the Minimum filter now uses the 21-pixel kernel.
7. Problem 8: per-plane time offsets are applied.
8. Problem 9: the placement of the negative regions is checked.
9. Problem 11: the header count is fixed.

All the outputs I asked for in section C were added. Point 10 is superseded (see section 2).

**Partly resolved:**
- **Point 4 (drawing a).** Drawing a was rebuilt as the claims file describes it, now 8 to 40 ROIs per ant. But 356 of its 436 regions are still under 10 µm across (median 3.9 µm, smallest 1.3 µm; cell 9). It still mostly yields sub-glomerular fragments. That weakens the "both drawings meet it" support for figs5a, figs5a-concentration and figs5c. It also weakens the aiiy identification behind every PGa result. The claims-file issue (no size floor on drawing a) still stands.

**Remaining points that bear on a conclusion:**
- figs5c should be not_reproduced under its own "each M2 reading" criterion.
- figs4a should be not_reproduced (classification).
- The single-glomerulus outcomes (fig5c-s6, fig5c-6g-slow, figs7c) rest on aiiy. That reading uses the ROI maximum and fragment ROIs, against the ROI mean adopted elsewhere. PGa comes from 3 to 4 ants, and 8 to 9 of the 18 PGa disc traces never cross the onset bound.
- For the region ROI, 618 of 1,684 traces fell back to the disc (cell 39). The conclusions do not say so, and it softens the region-ROI comparisons in fig5c-s6, fig5c-6g-slow and figs7a.

## End of run

13 turns, 3 minutes, result: success.
