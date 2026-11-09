# 000023 · verifier-1 · run 39907958889

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null;
```

```
Exit code 2
total 288
drwxr-xr-x 6 runner runner    4096 Oct 23 06:23 .
drwxr-xr-x 7 runner runner    4096 Oct 23 06:23 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 23 05:49 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 23 05:49 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 23 06:23 .claude
-rw-r--r-- 1 runner runner       0 Oct 23 06:23 .env
-rw-r--r-- 1 runner runner       0 Oct 23 06:23 .env.development
-rw-r--r-- 1 runner runner       0 Oct 23 06:23 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 23 06:23 .env.local
-rw-r--r-- 1 runner runner       0 Oct 23 06:23 .env.production
-rw-r--r-- 1 runner runner       0 Oct 23 06:23 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 23 06:23 .env.test
-rw-r--r-- 1 runner runner       0 Oct 23 06:23 .env.test.local
drwx------ 2 runner runner      40 Oct 23 06:23 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 23 05:49 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 23 05:49 .github
-rw-r--r-- 1 runner runner       0 Oct 23 06:23 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 23 05:49 .idea
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1101-2020.03.31.018820.yaml"
}
```

```
1	# Claims for Berg, Sorensen, Ting, Miller et al. (2020), "Human cortical expansion involves
2	# diversification and specialization of supragranular intratelencephalic-projecting neurons",
3	# bioRxiv doi:10.1101/2020.03.31.018820, on dandiset 000023.
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
5	# protocol pilot-10 as stated in docs/protocol.md.
6	#
7	# Text read: the bioRxiv preprint, version 1 (the version the dandiset names), from the bioRxiv
8	# JATS XML flattened to text (paper/10.1101-2020.03.31.018820.txt): main text, Methods, figure
9	# legends, Extended Data figure legends and the legends of Extended Data Tables 1 and 2. Not in
10	# the text: the figures themselves (no PDF was supplied), the contents of Extended Data Table 1
11	# (per-feature cross-species p-values and Cohen's d) and Table 2 (donors), and Supplementary
12	# Data 1 (per-feature depth correlations and ANOVA results). Every claim below rests on numbers
13	# that the main text or a legend states; the per-feature values in those items are not used.
14	# A later version of record exists (Nature 598, 151-158, 2021) and was not read.
15	#
16	# Code read: https://github.com/AllenInstitute/patchseq_human_L23 at commit
17	# 3daf9f0803ea0c220a040ea523f23af5f93c56ac (2021-09-17). It holds R scripts for the
18	# transcriptomic analyses (Code1 to Code5) and soma size and density (Code6 to Code8); Python
19	# notebooks for pathology (pathology_analysis.ipynb, and pathology_analysis_updated.ipynb for
20	# the revision), the per-feature ANOVAs, depth regressions and boxplots
[... 927 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
nb=json.load(open('reproduce_berg_2020.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"===== [{i}] {c['cell_type']}")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT(data)--'); print(''.join(d['text/plain'])[:6000])
        elif o.get('output_type')=='error': print('--ERR--', o.get('ename'), o.get('evalue'))
EOF
```

```
<persisted-output>
Output too large (111.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/2d8326bf-8c9f-4576-a83a-8dea0eb33cde/tool-results/bl3zq7tfl.txt

Preview (first 2KB):
===== [0] markdown
# Berg et al. (2020): human supragranular glutamatergic neurons, from dandiset 000023

- Paper. Berg, Sorensen, Ting, Miller et al. (2020), "Human cortical expansion involves
  diversification and specialization of supragranular intratelencephalic-projecting neurons",
  bioRxiv, doi:10.1101/2020.03.31.018820, version 1.
- Dataset. DANDI:000023, "Patch-seq recordings from human cortex (June 2020)", version
  0.210914.1900 (doi:10.48324/dandi.000023/0.210914.1900). The paper cites no version of the
  dandiset and the claims file gives none. This is the only published version, so it is pinned;
  the draft holds the same files (checked below).
- Claims file. `claims/000023/10.1101-2020.03.31.018820.yaml`, written from the bioRxiv
  preprint, version 1 (main text, Methods, figure and Extended Data legends), and from the paper's
  code, AllenInstitute/patchseq_human_L23 at commit 3daf9f0.
- Outside inputs. The dandiset holds only the human electrophysiology, with no t-type, depth or
  specimen ID. Labels (t-type, normalized L2/3 depth, region), donor pathology scores, the mouse
  features, the morphological features, the gene-depth table and the NeuN section ROIs come from
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/2d8326bf-8c9f-4576-a83a-8dea0eb33cde/tool-results/bl3zq7tfl.txt"
}
```

```
1	===== [0] markdown
2	# Berg et al. (2020): human supragranular glutamatergic neurons, from dandiset 000023
3	
4	- Paper. Berg, Sorensen, Ting, Miller et al. (2020), "Human cortical expansion involves
5	  diversification and specialization of supragranular intratelencephalic-projecting neurons",
6	  bioRxiv, doi:10.1101/2020.03.31.018820, version 1.
7	- Dataset. DANDI:000023, "Patch-seq recordings from human cortex (June 2020)", version
8	  0.210914.1900 (doi:10.48324/dandi.000023/0.210914.1900). The paper cites no version of the
9	  dandiset and the claims file gives none. This is the only published version, so it is pinned;
10	  the draft holds the same files (checked below).
11	- Claims file. `claims/000023/10.1101-2020.03.31.018820.yaml`, written from the bioRxiv
12	  preprint, version 1 (main text, Methods, figure and Extended Data legends), and from the paper's
13	  code, AllenInstitute/patchseq_human_L23 at commit 3daf9f0.
14	- Outside inputs. The dandiset holds only the human electrophysiology, with no t-type, depth or
15	  specimen ID. Labels (t-type, normalized L2/3 depth, region), donor pathology scores, the mouse
16	  features, the morphological features, the gene-depth table and the NeuN section ROIs come from
17	  the code repository at commit 3daf9f0. Questions to the readers, and their answers, are in `questions/000023.yaml`; the claims
18	  they bear on were updated in the claims file, and this notebook follows the updated criteria.
19	
20	| Claim | Data | Tested |
[... 745 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/2d8326bf-8c9f-4576-a83a-8dea0eb33cde/tool-results/bl3zq7tfl.txt",
 "offset": 766,
 "limit": 560
}
```

```
766	print("\nper donor: donors contributing CARM1P1", df[df.tt == "CARM1P1"].donor.nunique(), "| COL22A1",
767	      df[df.tt == "COL22A1"].donor.nunique(), "| depths range", df.nd.min().round(3), "to", df.nd.max().round(3))
768	fig, ax = plt.subplots(figsize=(6, 3))
769	for i, t in enumerate(P.TYPE_ORDER):
770	    y = df.loc[df.tt == t, "nd"].dropna()
771	    ax.scatter(np.full(len(y), i) + rng_for("fig3d-depth-by-type").uniform(-0.2, 0.2, len(y)), y, s=6)
772	ax.axhline(0.575, ls="--", c="k", lw=0.8)
773	ax.axhline(1, c="k", lw=0.8)
774	ax.set_xticks(range(5), P.TYPE_ORDER)
775	ax.invert_yaxis()
776	ax.set_ylabel("normalized L2/3 depth")
777	plt.show()
778	print("all", int(df.nd.notna().sum()), "points are inside the axes")
779	--OUT--
780	cells here with a depth (all, with or without features):
781	           n  median    min    max  share_deeper_0.575  share_deeper_1
782	tt                                                                    
783	LTK       70   0.082  0.001  0.998               0.043           0.000
784	GLP2R     25   0.425  0.036  1.141               0.200           0.040
785	FREM3    146   0.236  0.001  0.992               0.192           0.000
[... 540 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/2d8326bf-8c9f-4576-a83a-8dea0eb33cde/tool-results/bl3zq7tfl.txt",
 "offset": 1325,
 "limit": 500
}
```

```
1325	    g, i = out["GFAP"], out["IBA1"]
1326	    only_rmp = (not g.sig.any()) and i.sig.sum() == 1 and bool(i.set_index("feature").sig["v_baseline"])
1327	    rmp = i.set_index("feature").loc["v_baseline"]
1328	    size = [abs(rmp.median_diff - (-5)) <= 0.5, abs(rmp.mean_diff - (-5)) <= 0.5]
1329	    if not only_rmp:
1330	        return "not_reproduced"
1331	    if all(size):
1332	        return "reproduced"
1333	    return "partially_reproduced" if not any(size) else "methods_underspecified (size)"
1334	
1335	
1336	all18 = df[nmiss == 0]
1337	for name, d in [("(a) temporal", all18[all18.region == "temporal"]), ("(b) all regions", all18)]:
1338	    out = pathology_test(d, d)
1339	    print(f"\n{name}: {len(d)} cells with all 18 features")
1340	    for marker, r in out.items():
1341	        print(f"  {marker}: low {r.n_low.max()} high {r.n_high.max()} cells; significant at 0.05/18: "
1342	              f"{list(r.feature[r.sig])}; smallest p {r.p.min():.2g} ({r.feature[r.p.idxmin()]})")
1343	    rmp = out["IBA1"].set_index("feature").loc["v_baseline"]
1344	    print(f"  RMP, high minus low IBA1: medians {rmp.median_diff:.2f} mV, means {rmp.mean_diff:.2f} mV, p {rmp.p:.2g}")
[... 471 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "patchseq_l23.py"
}
```

```
1	"""Loading and feature extraction for dandiset 000023 (human Patch-seq, Allen Institute, June 2020).
2	
3	The dandiset holds one NWB file per neuron: whole-cell current clamp recorded with MIES, with the
4	Allen pipeline's spike times under processing/spikes. Each file is read whole into memory from the
5	archive's S3 store (no copy on disk) and passed to IPFX, which reads NWB files from a buffer.
6	
7	Where the parameters come from:
8	
9	- The 18 features and their names are those of the paper's code (data/ephys_feature_names.csv at
10	  AllenInstitute/patchseq_human_L23 commit 3daf9f0), as the claims file lists them. IPFX gives the
11	  underlying quantities; how each named feature is read from IPFX's output is in FEATURE_SOURCES.
12	  The code does not hold the step that made its table from IPFX, so this reading follows the names
13	  (`_hero` from the hero sweep, about 50 pA above rheobase; `_rheo` and `_long_square` from the first
14	  spike of the rheobase sweep; `_rel` relative to AP threshold; `adapt_mean` the mean adaptation
15	  over the spiking long squares, which matched the table where the hero sweep's adaptation did
16	  not), and the link claim checks it.
17	- Sweep QC is IPFX's default criteria (ipfx/defaults/qc_criteria.json), whose values are the
18	  Methods' (bridge balance and access below 20 MOhm and 15% of input resistance, bias current
19	  within +/-100 pA, RMS noise below 0.07 and 0.5 mV). Cell QC is computed and reported but not used
20	  to drop cells: the claims file asks for sweep QC only.
[... 503 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -c "^- id:" 10.1101-2020.03.31.018820.yaml; grep -n -i "chance\|shuffl\|permut" paper/*.txt | head -20; python3 -c "import statsmodels, scipy, pandas; print(statsmodels.__version__, scipy.__version__)"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import scipy, numpy as np, pandas
print(scipy.__version__)
from scipy import stats
x=np.arange(10.);y=np.arange(5,20.)
print(stats.mannwhitneyu(x,y,alternative='two-sided',use_continuity=True,method='asymptotic').pvalue/2, stats.mannwhitneyu(x,y,alternative='less').pvalue)
# density_profile binning check
br=-np.arange(20,-1,-1)/20
s=np.array([-1.0,-0.975,-0.95,-0.5,0.0,-0.05])
print(np.clip(np.searchsorted(br,s,side='left')-1,0,len(br)-2))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import scipy, numpy as np, pandas
ModuleNotFoundError: No module named 'scipy'
```

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np
br=-np.arange(20,-1,-1)/20
s=np.array([-1.0,-0.975,-0.95,-0.5,0.0,-0.05,-0.949])
idx=np.clip(np.searchsorted(br,s,side='left')-1,0,len(br)-2); print(idx)
for k in [0,1,9,19]:
  print(k, [(v) for v in s if br[k]<=v<br[k+1]])
"; python3 -c "import pandas" && echo pandas ok
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np
ModuleNotFoundError: No module named 'numpy'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pandas
ModuleNotFoundError: No module named 'pandas'
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000023/versions/0.210914.1900/assets/?page_size=3" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['count']); [print(a['path'],a['asset_id']) for a in d['results']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000023/versions/0.210914.1900/assets/1a93dc97-327d-4f9c-992d-c2149e7810ae/" | python3 -m json.tool | head -120; curl -s "https://api.dandiarchive.org/api/dandisets/000023/versions/0.210914.1900/assets/paths/?path_prefix=" | head -c 600; echo; curl -s "https://api.dandiarchive.org/api/dandisets/000023/versions/0.210914.1900/assets/?page_size=1000" | python3 -c "
import json,sys; d=json.load(sys.stdin); ps=[a['path'] for a in d['results']]
print(len(ps), set(p.split('.')[-1] for p in ps), set(p.split('_')[-1] for p in ps))"
```

Result: the fetched text is not kept.

**Agent**

**A. Outcomes** (all 33 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| features-and-labels-link | reproduced (M2); M1 not reproduced | M1 links 0 files (cell 12). Under M2, 318 files link to 318 distinct cells, and all 283 of the code's cells that have features have a file. The median relative difference is 0 for all 18 features over 282 cells, and a match on features alone picks the M2 cell 282 of 282 times. |
| cohort-cells | not_reproduced | 318 cells, not 385. 283 is not reached under any reading: (a) 307, (b) 256, (c) 306 (cell 16). |
| cohort-donors | not_reproduced | 56 under both readings, not 90 (cell 18). The pathology table has 89 distinct donors in 90 rows. |
| cohort-type-counts | not_reproduced | At most 2 of 6 counts match under any reading (cell 20). The criterion needs at least 3 for partial. |
| fig1a-thickness | reproduced | 1.231 ± 0.155 mm over 5 sections, inside 1.23 ± 0.15 (cell 60). The mouse value is untested, as the criterion says. |
| fig1b-density | partially_reproduced | Human 27.70 ± 4.46, highest in L2 and falling to 0.43× at −0.575 (cell 62). The mouse figure (349.8) comes from a faulty port (problem 2), so the mouse part was not validly tested. |
| fig1c-soma-area | partially_reproduced | Human quartiles 107.5/252.6 and largest soma 886 µm² pass (cell 64). Mouse quartiles 24.4/61.0 fail, but they come from the faulty port; the claims file says Code7 prints 44.7/96.5 from the same files. |
| fig1c-soma-variation | blocked (other) | The ratio is NaN because all 1419 mouse somata sit at scaled depth −1.0 (cell 65). This is a port fault, not missing data, so the claim is testable. |
| fig1f-frem3-heterogeneity | blocked (data_missing) | Not in the archive: it holds only 318 `*_icephys.nwb` files (checked through the API). |
| fig1g-deep-types-de-genes | blocked (data_missing) | Same reason. |
| fig3a-platform-correlation | blocked (data_missing) | Same reason. |
| fig2d-pathology-scores | reproduced | Donor averages run from 0.056 to 1.833, and 86.7% of donors are below 1.0 (cell 45). |
| edfig1-marker-correlation | reproduced | Ki-67 with Nissl (cellularity) has the largest \|r\| of the 15 pairs, 0.391 (cell 46). |
| fig2ef-pathology-ephys | partially_reproduced | Reading (a), temporal cells: only RMP under IBA1 is significant. The difference is −4.10 mV (medians) and −4.08 mV (means), both outside −5 ± 0.5 (cell 43). Reading (b) has 3 significant IBA1 features. Neither reading gives the paper's group sizes (60/125 and 170/15). |
| fig3d-depth-by-type | partially_reproduced | The median order holds and CARM1P1 and COL22A1 are at least 90% deeper than 0.575. No FREM3 cell is deeper than 1 (maximum 0.992), in the linked cells or in the full table (cell 22). |
| fig4e-human-ephys-anova | partially_reproduced | Features with R2 > 0.1 are input resistance, rheobase and first_isi_hero_inv; f-I slope has 0.087. Maximum R2 is 0.141, outside 0.16 ± 0.016 (cell 24). On the code's 283 cells the claim reproduces. |
| fig4e-mouse-ephys-anova | reproduced | Exactly the three named features have R2 > 0.1 at BH p < 0.05. Maximum R2 0.123 is within tolerance and below the human 0.141 (cell 26). |
| fig4f-morph-anova | reproduced | 16 human features (all at FDR < 1e-3) and 12 mouse features (10 at FDR < 0.05) (cell 48). |
| fig4-glp2r-sag | reproduced | GLP2R sag is above LTK (0.061 against 0.026, BH p 0.023). Adaptation does not differ (BH p 0.31) (cell 28). |
| edtable1-species-ephys | reproduced | 17 of 18 features under Student's and under Welch's test; width is the one not significant (cell 30). |
| edfig6-classifier-human-ephys | reproduced | 0.632 over 1000 splits, inside 0.67 ± 0.067. The paper states no chance level. Here the largest class is 0.580 and shuffled labels give 0.451, so the margin over chance is small (cell 33). |
| edfig6-classifier-mouse-ephys | reproduced | 0.571, inside 0.54 ± 0.054, and below the human 0.632. Largest class 0.491, shuffled labels 0.421 (cell 34). |
| edfig6-classifier-morphoelectric | reproduced | Human 0.720 and mouse 0.582 over 250 splits (SE about 0.006), both inside tolerance (cell 54). |
| fig5c-frem3-ephys-depth | partially_reproduced | 10 features at FDR < 0.05, outside 9 ± 0.9; 7 at FDR < 0.01. The top three features and their signs are right, but the upstroke/downstroke ratio has BH p 1.003e-7, not below 1e-7 (cell 36). |
| fig5b-frem3-morph-depth | reproduced | 37 and 28 of the 58 kept features (cell 49). |
| fig5d-frem3-gene-depth | blocked (data_missing) | The repository's table gives 4417 genes at FDR < 0.05. It is the revision's table; the preprint's results are not available anywhere (cell 56). |
| fig6-deep-ephys-anova | partially_reproduced | 15 features at FDR < 0.05 passes. 5 features have R2 > 0.4, against 4 ± 0.4; tau, at 0.412, is the fifth (cell 38). On the code's 283 cells: 14 and 4. |
| fig6c-carm1p1-upstroke-rin | blocked (methods_underspecified) | By upstroke rate, CARM1P1 is above both other types. By upstroke/downstroke ratio it is below COL22A1 (4.58 against 4.83). The criterion makes this part methods_underspecified when the two readings differ. The input resistance part holds (BH p 0.0019) (cell 40). |
| fig6c-col22a1-rin-fi-sag | reproduced | All 3 parts hold (cells 40 and 41). |
| fig6a-deep-dendrites | blocked (methods_underspecified) | Under reading (b) with medians, deep FREM3 has the largest total length (12024 µm, CARM1P1 10447). The other readings hold (cell 52). |
| fig6e-deep-de-genes | blocked (data_missing) | Not in the archive. |
| fig6f-smi32 | blocked (data_missing) | Not in the archive. |

**B. Problems**

1. [affects a conclusion] **Labels for 35 of the 318 files are unverified (cells 12, 14, 16).** M2 links each file to the next SpecimenID above its session id, which by construction links every file. So "files not matched to the table: 0" (cell 16) is circular, and the claims file's "other cells, counted apart" can never be found. The feature check covers only the 282 linked cells that have features in the code's table. The other 35 cells (25 of them with features here) take their t-type and depth from an unchecked match; offsets reach 685 against a median of 34. These cells are in every main analysis. Dropping them changes fig4e-human-ephys-anova from partial to reproduced and fig6-deep-ephys-anova from partial to reproduced (cells 24 and 38).
2. [affects a conclusion] **The mouse NeuN port in `section_tables` / `_layer_matrix` is wrong.** Mouse L2/3 thickness comes out as 32, 133 and 90 µm, against Code7's 281, 223 and 257 µm, which cell 57 itself names as the check. All mouse somata are clipped to scaled depth −1.0, and the pooled mouse quartiles (24.4/61.0) do not match Code7's 44.7/96.5. The soma areas do not depend on the boundary lines, so the soma selection or pixel scale is probably also wrong. This invalidates the mouse parts of fig1b-density and fig1c-soma-area and all of fig1c-soma-variation. Cell 0 blames "mouse section files" for the blocking, which is the wrong reason.
3. [affects a conclusion, possibly] **Cell QC is computed but not applied** (`extract_cell`; cell 10 shows 35 of 318 failing). The paper's Methods require seal, access-resistance and other cell-level QC. The link criterion names only sweep QC, which is an omission in the claims file, not a misreading of the paper. Of the 25 extra cells with features, 5 fail cell QC, and those cells feed problem 1.
4. [does not affect a conclusion] **Bin edges are handled inconsistently in `density_profile`.** Counts use right-closed bins (`searchsorted`), but the area and SD means use a left-closed mask, so somata clipped to exactly 0 are left out of the area and SD statistics. The human density matches Code6, so the effect is small.
5. [does not affect a conclusion] **fig2ef group sizes are not recovered** (cell 43). Under both readings the low/high counts differ from the paper's. The verdict function ignores the counts, which is consistent with how the criterion is written, but the paper's cell set is not reproduced.
6. [does not affect a conclusion] **Possible duplicate donor in the pathology table** (cell 43). It has 90 rows but 89 distinct `donor_id[:10]`. A donor with two rows could be put in both the low and the high group; this is not checked.
7. [does not affect a conclusion] **Fewer classifier splits than the criterion** (cell 54). The morpho-electric classifiers use 250 splits instead of 1000. The standard errors (≤0.007) are far smaller than the distance to the tolerance bounds.
8. [does not affect a conclusion] **fig3d uses a different cell set as its main run** (cell 22). It uses the 318 linked cells, while the criterion names every cell of the code's table. The full-table variant gives the same verdict.
9. [does not affect a conclusion] **Donor metadata mismatches are noted but not followed up** (cell 12). H18.03.318 is female in the file and male in the tables; H18.06.005 differs in age.
10. [does not affect a conclusion] **Tolerances on small counts are effectively exact.** The claims file's 10% tolerances on small integers (4 ± 0.4, 9 ± 0.9) leave no room. This decides fig6-deep-ephys-anova and fig5c-frem3-ephys-depth, but it follows the claims file.

**C. What I could not check, and what would have let me**

- **Helper functions on synthetic inputs.** numpy, scipy and statsmodels are not installed here, so I checked `ols_hc3`, `bh`, `pairwise_mw` and `mw_scipy14` by reading only.
- **Whether the 35 unchecked links are right.** Needed: a per-file table of M2 offset and gap, split by whether the cell is in the code's feature table, plus every main analysis re-run without those 35 cells and with cell QC applied.
- **Why the mouse port fails.** Needed: the per-section boundary-line y positions and line order, and per-case soma counts and area quartiles, set against Code7's printed values.
- **Whether sweep QC worked as the Methods say.** Needed: the reasons sweeps failed QC, and confirmation that the bias-current criterion was used, given that long-square bias currents run from −284 to 195 pA and 1165 sweeps have no value. The IPFX version should also be printed.
- **The archive for the blocked claims.** The API confirms 318 human `icephys.nwb` assets across 56 subjects and no other file types. Asset metadata carry only subject id, session id, sex and age: no SpecimenID, t-type or depth. So none of the archive-blocked claims (fig1f-frem3-heterogeneity, fig1g-deep-types-de-genes, fig3a-platform-correlation, fig5d-frem3-gene-depth, fig6e-deep-de-genes, fig6f-smi32) can be tested from it. fig1c-soma-variation is testable from the code repository once the port is fixed.

## End of run

13 turns, 4 minutes, result: success.
