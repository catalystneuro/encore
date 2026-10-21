# 000008 · verifier-2 · run 39541904672

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; cat round-1-report.md
```

```
total 568
drwxr-xr-x 6 runner runner    4096 Oct 21 04:27 .
drwxr-xr-x 7 runner runner    4096 Oct 21 04:27 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 21 04:02 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 21 04:02 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 21 04:27 .claude
-rw-r--r-- 1 runner runner       0 Oct 21 04:27 .env
-rw-r--r-- 1 runner runner       0 Oct 21 04:27 .env.development
-rw-r--r-- 1 runner runner       0 Oct 21 04:27 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 21 04:27 .env.local
-rw-r--r-- 1 runner runner       0 Oct 21 04:27 .env.production
-rw-r--r-- 1 runner runner       0 Oct 21 04:27 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 21 04:27 .env.test
-rw-r--r-- 1 runner runner       0 Oct 21 04:27 .env.test.local
drwx------ 2 runner runner      40 Oct 21 04:27 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 21 04:02 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 21 04:02 .github
-rw-r--r-- 1 runner runner       0 Oct 21 04:27 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 21 04:02 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 21 04:02 .mcp.json
[... 96 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md; cat 000008-scala-2021-01.yaml
```

```
<persisted-output>
Output too large (49.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/2bff21e3-6218-49fa-ac05-373e1106562f/tool-results/bqduy4kfe.txt

Preview (first 2KB):
# Scala, Kobak et al. (2021) from dandiset 000008

Tests the findings of [Scala, Kobak et al. (2021)](https://doi.org/10.1038/s41586-020-2907-3) on
[DANDI:000008](https://dandiarchive.org/dandiset/000008/0.211014.0809), which holds the current-clamp
recordings of 1,328 Patch-seq neurons of mouse primary motor cortex, one NWB file per cell, with each
cell's t-type, family, layer and read counts. The paper's gene counts, morphology and reference data are
not in the dandiset; the claims that need them are tested with the paper's own deposits (its code
repository and a Zenodo record) and counted apart.

| Claim | Outcome |
|---|---|
| The dandiset's cells match the paper's metadata table (link) | Reproduced |
| Features extracted from the files match the paper's feature table (link) | Reproduced |
| 1,329 cells from 266 mice | Reproduced |
| Ages of the mice | Reproduced |
| Mice per genotype | Partially reproduced |
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1038-s41586-020-2907-3.yaml
```

```
<persisted-output>
Output too large (61.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/2bff21e3-6218-49fa-ac05-373e1106562f/tool-results/b3p1pnwvr.txt

Preview (first 2KB):
# Claims for Scala, Kobak et al. (2021), "Phenotypic variation of transcriptomic cell types in
# mouse motor cortex", Nature 598:144-150, on dandiset 000008.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record, open access (CC BY), as served by Europe PMC (PMC8113357):
# main text, Methods, figure legends and Extended Data figure legends. Not in the text: the
# Extended Data Tables 1 and 2 (descriptions of the t-types), the Supplementary Files 1 to 3
# (galleries of morphologies and traces, dot plots of all features, the list of morphometric
# statistics) and the figures themselves. No PDF was supplied. No claim below rests on numbers
# that are only in those items; the Extended Data figures are read from their legends only.
#
# Code read: https://github.com/berenslab/mini-atlas at commit
# 3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9. It holds the analysis notebooks (feature extraction
# from the NWB files in preprocess-ephys-files.ipynb with ephys_extractor.py and
# ephys_features.py; t-type assignment; reduced-rank regression with sparseRRR.py; the
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/2bff21e3-6218-49fa-ac05-373e1106562f/tool-results/bqduy4kfe.txt"
}
```

```
1	# Scala, Kobak et al. (2021) from dandiset 000008
2	
3	Tests the findings of [Scala, Kobak et al. (2021)](https://doi.org/10.1038/s41586-020-2907-3) on
4	[DANDI:000008](https://dandiarchive.org/dandiset/000008/0.211014.0809), which holds the current-clamp
5	recordings of 1,328 Patch-seq neurons of mouse primary motor cortex, one NWB file per cell, with each
6	cell's t-type, family, layer and read counts. The paper's gene counts, morphology and reference data are
7	not in the dandiset; the claims that need them are tested with the paper's own deposits (its code
8	repository and a Zenodo record) and counted apart.
9	
10	| Claim | Outcome |
11	|---|---|
12	| The dandiset's cells match the paper's metadata table (link) | Reproduced |
13	| Features extracted from the files match the paper's feature table (link) | Reproduced |
14	| 1,329 cells from 266 mice | Reproduced |
15	| Ages of the mice | Reproduced |
16	| Mice per genotype | Partially reproduced |
17	| Stimulus protocol | Partially reproduced |
18	| 1,284 cells with a soma depth | Reproduced |
19	| Features of the example cell (Extended Data Fig. 4) | Reproduced |
20	| 1,320 cells with all 17 features, 1,219 with a t-type | Reproduced |
[... 845 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -nE "^\s*- id:|^\s*id:" 10.1038-s41586-020-2907-3.yaml | head -60; grep -c "^- claim:" 000008-scala-2021-01.yaml; grep -A1 "^- claim:" 000008-scala-2021-01.yaml | grep outcome | sort | uniq -c; awk '/^outcomes:/,/^findings:/' 000008-scala-2021-01.yaml | grep -E "blocked_by" | sort | uniq -c
```

```
69:  id: "000008"
73:- id: cohort-cells-mice
93:- id: cohort-ages
125:- id: cohort-genotypes
171:- id: stimulus-protocol
191:- id: soma-depth-count
211:- id: ed4-example-cell
317:- id: ephys-feature-count
336:- id: fig2-family-features
356:- id: fig3d-families-ephys
385:- id: ed6-it-et-room-features
404:- id: ed6-physiological-temperature
420:- id: fig1a-ttype-coverage
447:- id: fig1b-depth-layers
463:- id: l45-it1-boundary
481:- id: fig4c-distance-correlation
514:- id: ed7-within-families
537:- id: fig4d-it-depth
559:- id: fig4a-vip-tau
583:- id: fig4b-sst-rebound
[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/2bff21e3-6218-49fa-ac05-373e1106562f/tool-results/b3p1pnwvr.txt"
}
```

```
1	# Claims for Scala, Kobak et al. (2021), "Phenotypic variation of transcriptomic cell types in
2	# mouse motor cortex", Nature 598:144-150, on dandiset 000008.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20,
4	# protocol pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the version of record, open access (CC BY), as served by Europe PMC (PMC8113357):
7	# main text, Methods, figure legends and Extended Data figure legends. Not in the text: the
8	# Extended Data Tables 1 and 2 (descriptions of the t-types), the Supplementary Files 1 to 3
9	# (galleries of morphologies and traces, dot plots of all features, the list of morphometric
10	# statistics) and the figures themselves. No PDF was supplied. No claim below rests on numbers
11	# that are only in those items; the Extended Data figures are read from their legends only.
12	#
13	# Code read: https://github.com/berenslab/mini-atlas at commit
14	# 3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9. It holds the analysis notebooks (feature extraction
15	# from the NWB files in preprocess-ephys-files.ipynb with ephys_extractor.py and
16	# ephys_features.py; t-type assignment; reduced-rank regression with sparseRRR.py; the
17	# t-SNEs, kNN family classifiers, normalized variances and Leiden entropies in
18	# phenotype-tsne.ipynb; the distance correlations of Fig. 4 and Extended Data Fig. 7 in
19	# families.ipynb; Extended Data Fig. 6 in physiological-temperature.ipynb) and the paper's
20	# preprocessed data: per-cell metadata (m1_patchseq_meta_data.csv, 1,329 cells, with t-type,
[... 966 more lines not kept]
```

**Agent**

Read the claims file and attempt record (35 claims; record has 25 reproduced, 4 partial, 1 not reproduced, 5 blocked). Now extracting notebook cells and outputs.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(src)
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--\n'+''.join(o['text']))
        elif 'data' in o and 'text/plain' in o['data']: print('--OUT--\n'+''.join(o['data']['text/plain']))
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
EOF
for n in ephys transcriptomics sequencing; do python3 $TMPDIR/dump.py scala_2021_$n.ipynb > $TMPDIR/$n.txt; wc -l $TMPDIR/$n.txt; done
```

```
1903 /tmp/claude-1001/ephys.txt
979 /tmp/claude-1001/transcriptomics.txt
316 /tmp/claude-1001/sequencing.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/ephys.txt",
 "limit": 700
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Scala, Kobak et al. (2021): electrophysiology and metadata of dandiset 000008
4	
5	Paper. Scala F., Kobak D. et al. (2021) Phenotypic variation of transcriptomic cell types in mouse
6	motor cortex. *Nature* 598:144-150. [doi:10.1038/s41586-020-2907-3](https://doi.org/10.1038/s41586-020-2907-3)
7	
8	Dataset. [DANDI:000008](https://dandiarchive.org/dandiset/000008/0.211014.0809), version
9	0.211014.0809 ([doi:10.48324/dandi.000008/0.211014.0809](https://doi.org/10.48324/dandi.000008/0.211014.0809)):
10	one NWB file per Patch-seq neuron with its current-clamp sweeps and per-cell metadata.
11	
12	Why this version. The paper cites no version (it links the dandiset itself). The dandiset has two
13	published versions, 0.211014.0808 and 0.211014.0809, made a second apart; their asset lists have the same
14	1,328 paths and sizes (checked below). The latest published version, 0.211014.0809, is pinned. The draft
15	was modified later (2026), so it is not used.
16	
17	Text the claims were written from. The version of record (open access, Europe PMC PMC8113357): main
18	text, Methods, figure and Extended Data legends, and the paper's code, mini-atlas at commit
19	3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9. The claims file is `claims/000008/10.1038-s41586-020-2907-3.yaml`.
20	
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/ephys.txt",
 "offset": 700,
 "limit": 650
}
```

```
700	Vip-IRES-Cre/wt; Ai9/wt                    46                    [VIP+, VIP-]
701	Vipr2-IRES2-Cre-D/wt; Ai9/wt                7                [VIPR2+, VIPR2-]
702	wt/wt                                      26                            [WT]
703	--OUT--
704	   line (paper)                    genotype in the files  paper  dandiset  match
705	0     wild type                                    wt/wt     27        26  False
706	1     Viaat-Cre                     Viaat-Cre/wt; Ai9/wt     24        24   True
707	2       Sst-Cre                  Sst-IRES-Cre/wt; Ai9/wt     75        75   True
708	3       Vip-Cre                  Vip-IRES-Cre/wt; Ai9/wt     46        46   True
709	4     Pvalb-Cre                     Pvalb-Cre/wt; Ai9/wt     76        76   True
710	5       Npy-Cre                       Npy-Cre/wt; Ai9/wt      2         2   True
711	6     Vipr2-Cre             Vipr2-IRES2-Cre-D/wt; Ai9/wt      7         7   True
712	7   Slc17a8-Cre           Slc17a8-IRES2-Cre-D/wt; Ai9/wt      6         6   True
713	8      Gnb4-Cre  Gnb4-IRES2-CreER2-D knock-in/wt; Ai9/wt      1         1   True
714	9  Slc17a8-iCre                    Vglut3-Cre/wt; Ai9/wt      2         2   True
715	--OUT--
716	matching lines: 9 of 10 | total mice: 266 | genotypes in the files not in the paper's list: ['Scnn1a-Tg3-Cre/wt; Ai9/wt']
717	
718	
719	######## CELL 27 [markdown]
[... 630 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "def layer_from_depth" -A 22 scala.py; grep -n "layer" scala.py | head -40
```

```
345:def layer_from_depth(nd, fallback):
346-    """Layer from normalized depth with the Nissl boundaries, else the fallback (the code's rule).
347-
348-    The comparisons are those of the code (phenotype-tsne.ipynb cell 3, physiological-temperature.ipynb
349-    cell 2): strict on both sides, so a depth exactly at 0.07, 0.29 or 0.73 keeps the fallback, as
350-    it does in the code. The claims file's opening comment gives the targeted layer as the fallback."""
351-    out = np.array(fallback, dtype=object).copy()
352-    nd = np.asarray(nd, dtype=float)
353-    with np.errstate(invalid="ignore"):
354-        out[nd < 0.07] = "1"
355-        out[(nd > 0.07) & (nd < 0.29)] = "2/3"
356-        out[(nd > 0.29) & (nd < 0.73)] = "5"
357-        out[nd > 0.73] = "6"
358-    return out
359-
360-
361-def duplicate_recordings(meta: pd.DataFrame) -> pd.DataFrame:
362-    """Groups of files whose whole voltage matrix is identical: one row per file in such a group,
363-    with its cell id, mouse, t-type, and whether it is kept. Within a group the cell with the
364-    lowest sample number is kept; which cell the recording belongs to is not known, so this is a
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/ephys.txt",
 "offset": 1349,
 "limit": 560
}
```

```
1349	import io
1350	from sklearn.decomposition import PCA
1351	mf = pd.read_csv(io.StringIO(scala._get(f"{scala.MINI_ATLAS}/data/m1_patchseq_morph_features.csv").text)).set_index("cell id")
1352	mf = mf.iloc[:, :-2].astype(float)   # the code drops the last two columns (normalized layer, cell class)
1353	zp = pd.read_csv(io.StringIO(scala._get(f"{scala.MINI_ATLAS}/data/m1_patchseq_morph_zprofiles.csv").text)).set_index("cell id").astype(float)
1354	print("cells with morphometrics:", len(mf), "| of them in the dandiset:", int(mf.index.isin(t.index).sum()))
1355	
1356	def morph_representation(tt):
1357	    # As phenotype-tsne.ipynb at the pinned commit. Cell 10: cells with any morphometric value, less two cells
1358	    # without all dendritic features. Cell 11: inhibitory or excitatory family and not excluded; per class, the
1359	    # features present in that class, standardized (np.std, ddof 0), 20 PCs scaled by the s.d. of PC1, and 0.25
1360	    # added to the excitatory block. Cell 12: z-profiles, PCs 2 to 5 of a 5-component PCA, scaled by the s.d. of
1361	    # the first kept PC, 0.25 added to the excitatory block. Cell 13: the four blocks in a 48-column matrix,
1362	    # zero outside a cell's own class.
1363	    fam = tt.family.where(~tt.excluded, "low quality")
1364	    q = [c for c in tt.index if c in mf.index and mf.loc[c].notna().any() and c not in ["20180820_sample_1", "20180921_sample_3"]]
1365	    inh = [c for c in q if fam[c] in scala.INHIBITORY]
1366	    exc = [c for c in q if fam[c] in scala.EXCITATORY]
1367	    def block(cs):
1368	        M = mf.loc[cs]
[... 536 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/transcriptomics.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Scala, Kobak et al. (2021): dandiset 000008 with the paper's gene counts and reference data
4	
5	Paper. Scala F., Kobak D. et al. (2021) Phenotypic variation of transcriptomic cell types in mouse
6	motor cortex. *Nature* 598:144-150. [doi:10.1038/s41586-020-2907-3](https://doi.org/10.1038/s41586-020-2907-3)
7	
8	Dataset. [DANDI:000008](https://dandiarchive.org/dandiset/000008/0.211014.0809), version 0.211014.0809,
9	the latest published version (the paper cites none; the earlier version 0.211014.0808 has the same assets,
10	see `scala_2021_ephys.ipynb`).
11	
12	Text the claims were written from. The version of record (Europe PMC PMC8113357) with the paper's code,
13	mini-atlas at commit 3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9.
14	
15	This notebook tests the claims marked `with_inputs` that combine the dandiset's recordings with data
16	from outside it: the paper's Patch-seq gene counts (mini-atlas `data/`), the paper's preprocessed Allen
17	Institute 10x v2 reference (Zenodo record 5118962, doi:10.5281/zenodo.5118962) and its reference t-SNE
18	coordinates (mini-atlas `data/processed/rnaseq/`). The electrophysiological features are extracted again
19	from the dandiset's files with the paper's code, as in `scala_2021_ephys.ipynb`, where the data are
20	checked against their description; the per-cell labels come from the files, and the exclusion of five
[... 960 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,400p $TMPDIR/sequencing.txt | grep -v "^--OUT--$" ; grep -n "normalizeNew\|def map_to_tsne" scala.py | head
```

```
######## CELL 0 [markdown]
# Scala, Kobak et al. (2021): sequencing claims, on the paper's count tables

Paper. Scala F., Kobak D. et al. (2021) Phenotypic variation of transcriptomic cell types in mouse
motor cortex. *Nature* 598:144-150. [doi:10.1038/s41586-020-2907-3](https://doi.org/10.1038/s41586-020-2907-3)

Dataset. [DANDI:000008](https://dandiarchive.org/dandiset/000008/0.211014.0809), version 0.211014.0809
(the latest published version; the paper cites none). The dandiset holds the recordings only. The claims
here are marked `data: elsewhere`: the paper deposited the reads at NeMO and GEO (GSE163764) and the count
tables in its code repository (mini-atlas at commit 3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9, `data/`), and
the reference data it maps to are its preprocessed Allen Institute data (Zenodo record 5118962,
doi:10.5281/zenodo.5118962). The tests run on those count tables, which the claims file names under
`where`; the cells are linked to the dandiset's files by cell id.

Text the claims were written from. The version of record (Europe PMC PMC8113357).

| Claim | Tested here |
|---|---|
| rnaseq-depth | yes |
| ttype-qc-counts | yes |
[... 264 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -o ".\{120\}636.\{80\}" paper/*.txt | head; grep -o ".\{100\}628.\{60\}" paper/*.txt | head -3; grep -n "Hold\|hold time" -i paper/*.txt | head -5
```

Result: not kept, because it reads the paper's text.

**Agent**

**Round 2 verifier report: 000008-scala-2021-01 (Scala, Kobak et al. 2021, DANDI:000008)**

Counts come from the claims file and the attempt record's `outcomes`. There are 35 claims: 25 reproduced, 4 partially reproduced, 1 not reproduced and 5 blocked (4 methods_underspecified, 1 data_unreadable).

## 1. Stated outcomes

I agree with all 35 stated outcomes.

- **Changed since round 1:**
  - **cohort-cells-mice:** now reproduced (1,328 distinct cells, 266 mice; ephys cell 20), which matches my round-1 outcome.
- **Blocked reason:**
  - **ed6-physiological-temperature and fig4e-pvalb-axon-shape:** in round 1 I gave both as blocked for data_missing. I now accept methods_underspecified. Both claims are `data: elsewhere`, and both criteria themselves say the paper gives no measure ("a test would be chosen by an agent"). I could not check the protocol rule the author cites, because docs/protocol.md is not among my materials.
- **Kept, but marginal:**
  - **fig5d-sst-pvalb-calb2-firing:** reproduced, but marginal (see 3).
  - **fig5b-ttype-variability:** reproduced, but fragile.
  - **ed8-leiden-entropy:** not reproduced, also fragile.
  - **fig1a-ttype-coverage:** partially reproduced; this rests on a gap in the claims file, not on the notebook.
- **ed6-it-et-room-features and fig4b-sst-rebound:** now use the layer as the claims file defines it.
  - ed6 still gives the same four features (ephys cell 49).
  - fig4b gives r = 0.339, p = 0.0113 (transcriptomics cell 24).
  - Neither outcome changes.

## 2. Sentences the printed outputs do not support

All "**Result:**" conclusions, the three Summary sections and the record's notes otherwise match the printed numbers.

1. **Ephys cell 7:** "the values run from about -150 to +80 with resting values near -65". Nothing printed shows this.
   - Cell 5 prints min −1,025.4 and max 1,025.7, and per-file baselines of −78.5 to −54.7 (5th–95th percentile).
   - No −150/+80 range is printed.
2. **Sequencing cell 3:** "the exon sums are a few percent higher than `Exon reads` in most cells". Cell 2 prints a median ratio of 1.035 but a 5th–95th percentile range of 0.384 to 3.078. That supports "a median 3.5% higher" but not "most cells".
3. **Ephys cell 74 and the hold-time-yield notes:** both say every entry under `general` was listed and holds no hold time. Cell 6 lists `general` for one file only, and it is a low-quality cell. The DandiIcephysMetadata and subject fields, by contrast, are listed across all files, and they do support the conclusion. The record's own response to round 1 correctly says "of one file".
4. **README table labels:**
   - "1,329 cells from 266 mice | Reproduced" and "1,284 cells with a soma depth | Reproduced" read as though those numbers were reproduced. The dandiset gives 1,328 and 1,283, the values the criteria accept (ephys cells 20 and 32).
   - Smaller: the README says each of the ephys and transcriptomics notebooks takes about 18 min, but the printed run times are 9.0 min (ephys cell 79) and 10.0 min (transcriptomics cell 34).

**My round-1 reasons in the attempt record:** they are stated faithfully and in my own words, for every claim. That includes the two blocked-reason disagreements and the B/C points I attached to claims (B1, B3–B8, B10–B13, and the C items).
- My two general helper points, B2 and B9, are not recorded. Neither is tied to a claim.
- The cell numbers in my reasons are round-1 numbering and no longer match the re-executed notebook (for example, cohort-cells-mice is now cell 20, not 18). They are correct as a record of round 1.

## 3. Round-1 points

**Resolved:**
- **B1:** the layer now comes from the depth, using the Nissl boundaries. Both variants are shown and the outcomes are unchanged (ephys cell 49; transcriptomics cell 24).
- **B2:** the strict boundary rule is now documented as the code's rule (`scala.layer_from_depth`). It is now used in the main readings.
- **B6:** two library-size normalizations were added; both give ρ ≈ 0.02–0.07 (transcriptomics cell 27).
- **B7:** the field lists now cover all files (ephys cell 6), apart from point 3 above.
- **B8:** the comparison is now exact (ephys cell 13).
- **B11:** cells from phenotype-tsne.ipynb are cited. With all cells, 628 cells have both, and the orderings hold (ephys cell 61).
- **B12:** `leiden_entropies` now takes the label as an argument.
- **C items:**
  - the RRR folds are printed (transcriptomics cell 6);
  - the stimulus cross-tabulation is printed: 87 of the 90 cells starting at −100 pA end at 1,480 pA (ephys cell 29);
  - for fig5d, no cell sits at the median of 32.5, which splits the cells 13/13 (transcriptomics cell 30).
- **B9 and B13:** no action was needed.

**What remains that bears on a conclusion:**
- **fig5d (B3):** the outcome of reading (b) depends on the seed.
  - Seed 55 gives an upper bound of 0.0499; seeds 56–60 give upper bounds of 0.0510 to 0.0528, all failing the rule.
  - The exact p is 0.0497.
  - The follow-up question in questions/000008.yaml is still open.
- **fig5b (B4):** the share above the band runs from 22% to 56% across n_init and membership variants, and 2 of the 8 variants fall below 25%. The main reading is 15 of 35 (43%).
- **ed8 (B5):** the outcome flips with membership. The main reading gives p = 0.061; the code's membership with duplicates removed gives p = 0.031. The criterion does not say which handling governs.
- **fig1a (B10):** the claims file does not say whether the allowance for the missing cell covers the t-type it alone represents (76 against 77). The question is open in questions/000008.yaml.
- **morph-reconstructions:** the Brain Image Library still did not answer (ephys cell 76, 2026-10-21), so the blocked outcome cannot be re-checked.
- **fig5c reading (b):** I cannot check the claim that the main transform is the code's `normalizeNew` path, because rnaseqTools is not among my materials. All four transforms agree (ρ from 0.016 to 0.068), so this does not affect the outcome.

## End of run

15 turns, 2 minutes, result: success.
