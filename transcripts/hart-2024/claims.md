# 000773 · claims · run 39894274303

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000773/ paper/; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## Author/' docs/protocol.md; ls claims/001453/ claims/000773/ paper/ tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml; wc -c paper/*.txt; head -50 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/f0062680-4f37-46b8-8576-5c3f3646b27a/tool-results/blwjlxrc4.txt",
 "limit": 250
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cd  F=/home/runner/.claude/projects/-home-runner-work-encore-encore/f0062680-4f37-46b8-8576-5c3f3646b27a/tool-results/blwjlxrc4.txt; sed -n 250,420p $F | grep -n "^  [a-z_]*:" | awk '{print $2}' | sort | uniq -c; grep -n "^# \|^[a-z]" $F | sed -n 1,80p | tail -40
```

```
6 quote:
      6 source:
      6 statement:
      6 statistics:
1:# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2:# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3:# from its Results, figure legends and STAR Methods. The version of record is not open access.
5:# When these criteria were written, the author had seen the data check only: the file list,
6:# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7:# the extent of positions. No claim's analysis had been run. The author had also read the
8:# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9:# which include per-stimulus median speeds and angular velocities and its statistics.
11:# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12:# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13:# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14:# use outside data and depend on that claim.
16:# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17:# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18:# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19:# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
[... 22 more lines not kept]
```

**Agent**

Format understood. Now reading the paper text.

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; sed -n 1,200p paper/10.1016-j.cub.2024.05.031.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2024.05.031.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "SUPPLEMENT\|=====\|^---\|Figure S\|Table S1" paper/*.txt | sed -n 1,60p | cut -c1-200
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2024.05.031.txt",
 "offset": 380,
 "limit": 343
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 46,380p paper/*.txt | grep -v "^\[\|^$\|^10\.\|^http\|^PMC\|^[0-9]*$" | cut -c1-200 | head -40; ls paper
```

Result: not kept, because it reads the paper's text.

**Agent**

Text has main body, STAR Methods, and supplement MMC1 (Figs S1–S4, Table S1). Main-figure images are not included. Now checking the linked code on Zenodo and the dandiset description.

**Agent calls Bash**

```bash
cd $TMPDIR; for r in 11151724 11151756; do curl -sL "https://zenodo.org/api/records/$r" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('id'), d['metadata']['title'], d['metadata'].get('version'), d['metadata'].get('related_identifiers')); [print(f['key'], f['size'], f['links']['self']) for f in d['files']]"; done; curl -sL https://api.dandiarchive.org/api/dandisets/000773/ | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d,indent=1)[:1500])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL https://api.dandiarchive.org/api/dandisets/000773/versions/0.261004.1511/info/ | python3 -c "import json,sys; d=json.load(sys.stdin)['metadata']; print(d.get('description')); print(d.get('assetsSummary'))"; for r in 11151724 11151756; do curl -sL -o z$r.zip "https://zenodo.org/api/records/$r/files/Social-Evolution-and-Behavior/Hart_Kronauer$([ $r = 11151724 ] && echo 2023 || echo 2024)-v1.0.0.zip/content"; unzip -o -q z$r.zip -d z$r; done; find z1115* -type f
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; for f in z11151724/*/* z11151756/*/*; do echo "=== $f"; cat "$f"; done
```

```
=== z11151724/Social-Evolution-and-Behavior-Hart_Kronauer2023-72d041a/README.md
# Hart_Kronauer2023
Processing code for calcium imaging data from "Sparse and stereotyped encoding implicates a core glomerulus for ant alarm behavior".

Raw data with .nwb files can be found at https://dandiarchive.org/dandiset/000467

To re-analyze data, first download the archived data at the above link. Next, run the python script "generate_tif_files.py" on the downloaded archive to convert .nwb files to .tif files. Finally, install and run the ImageJ macro script "macro_calcium_imaging.txt". In each case you will need to enter the directory containing the source data into the scripts before running..
=== z11151724/Social-Evolution-and-Behavior-Hart_Kronauer2023-72d041a/generate_tif_files.py
import tifffile as tiff
import os
from pynwb import NWBHDF5IO


# this script reads .nwb files and writes corresponding new .tif files, for analysis in ImageJ. 
# source data: https://dandiarchive.org/dandiset/000467
# written by Taylor Hart
# specify the input and output directories below:


indir_path = "/Volumes/My Passport/test_download/000467/"
[... 595 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; python3 -c "
import fitz
d=fitz.open('paper/10.1016-j.cub.2024.05.031.supp.pdf')
print(len(d))
for i in range(1,7):
    d[i].get_pixmap(dpi=130).save(f'p{i+1}.png')
"; ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cub.2024.05.031.supp.pdf",
 "pages": "2-7"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; pip install -q pymupdf 2>&1 | tail -1; python3 -c "
import fitz
d=fitz.open('paper/10.1016-j.cub.2024.05.031.supp.pdf')
for i in range(1,7):
    d[i].get_pixmap(dpi=150).save(f'p{i+1}.png')
"; ls *.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 -m pip install --target $TMPDIR/py pymupdf 2>&1 | tail -2; PYTHONPATH=$TMPDIR/py python3 -c "
import fitz
d=fitz.open('paper/10.1016-j.cub.2024.05.031.supp.pdf')
for i in range(1,7):
    d[i].get_pixmap(dpi=150).save(f'p{i+1}.png')
"; ls *.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p2.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p3.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p4.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p5.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p6.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p7.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  grep -n "with_labels\|with_inputs\|elsewhere\|kind:" docs/*.md | cut -c1-400 | head -30; sed -n 1,60p tools/claims_check.py
```

```
docs/design.md:118:  elsewhere. This is the guard against a result that only looks right.
docs/pilot-notes.md:95:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
docs/pilot-notes.md:107:RDMs that are not public, are now marked `with_inputs`, and its attempt
docs/pilot-notes.md:123:  `data: with_labels`, for outside sources that only name or map codes the
docs/pilot-notes.md:162:adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
docs/pilot-notes.md:166:dandiset's claims and from `with_inputs` claims. It is never blocked with
docs/pilot-notes.md:257:link claims of step 6). They now say `kind: link` and are counted apart:
docs/protocol.md:137:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:205:4. Decide what comes from outside the dataset. Data from elsewhere may be
docs/protocol.md:214:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
docs/protocol.md:215:     `with_inputs` and `elsewhere` claims are counted apart, each group on
docs/protocol.md:217:   - `with_labels` is for outside sources that only name or map codes the
docs/protocol.md:222:     or subjects, a claim of its own (`kind: link`) tests the link. Link
docs/protocol.md:239:   - `elsewhere` is for a claim whose data the dataset does not hold at
docs/protocol.md:248:   - The notes of a `with_inputs` claim say which side a difference comes
docs/protocol.md:259:     `data: elsewhere` instead (step 4).
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 195,265p docs/protocol.md; python3 -c "
import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:6000])"
```

```
that names a paper may hold only part of its data. Check for recordings
   deposited more than once (identical traces, frame counts or annotations),
   report each pair, and count each recording once. Where the analysis treats
   a unit as the same across sessions, show that it is, or state it as an
   assumption and also give results per session.
3. Choose the version to pin. Pin the version the paper cites, as the claims
   file gives it. If it cites none, pin the most recent published version,
   unless an earlier one matches the claims file's description better. Say
   why in the notebook's header. If versions differ in content the analysis
   uses, show the difference.
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
   `inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dataset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
[... 256 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))" | head -120
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
cd  sed -n 60,400p tools/claims_check.py
```

```
return False


def printed_forms(v: float) -> set[str]:
    """Ways a paper prints a number: 0.002, .002, 2 × 10-5, 2e-5, 0.00002, 10-10."""
    out = {f"{v:g}", f"{v:g}".lstrip("0") if abs(v) < 1 else f"{v:g}"}
    if 0 < abs(v) < 1:
        m, e = f"{v:.3e}".split("e")
        m, e = f"{float(m):g}", str(int(e))
        out |= {f"{m}×10{e}", f"{m} × 10{e}", f"{m} x 10{e}", f"{m}x10{e}", f"{m}e{e}"}
        if m == "1":
            out.add(f"10{e}")
    if 0 < abs(v) < 0.001:
        plain = f"{v:.12f}".rstrip("0")
        out |= {plain, plain.lstrip("0")}
    return {f.lower() for f in out}


def check(claims_path: Path, paper_paths: list[Path]) -> int:
    doc = yaml.safe_load(claims_path.read_text())
[... 33 more lines not kept]
```

**Agent**

I have what I need: the text is complete (main text, STAR Methods, supplement with Figures S1–S4 and Table S1), and both Zenodo code records are read. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000773/10.1016-j.cub.2024.05.031.yaml",
 "content": "# Claims for Hart, Lopes, Frank & Kronauer (2024), Curr Biol 34, 3233, on dandiset 000773.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol as stated in docs/protocol.md (pilot-10).\n#\n# Text read: the accepted author manuscript (NIHMS1997610, PMC11265976) as served by Europe PMC,\n# main text, figure legends and STAR Methods, with the supplement MMC1 (Figures S1 to S4 and\n# Table S1), from paper/10.1016-j.cub.2024.05.031.txt. The supplement PDF was opened to read the\n# p-values and sample sizes printed inside Figures S1 to S4 and to check Table S1. The images of\n# main Figures 1 to 4 are not part of the text, so p-values printed only inside those panels\n# (Figures 2D, 2E, 3B, 3D and 4) are not known here; where the text says \"significant\" they are\n# recorded as p < 0.05. Data S1 (behavior) and Data S2 (calcium imaging quantifications) are\n# spreadsheets of the paper's supplement and were not read.\n#\n# Code read: the paper's two Zenodo records. doi:10.5281/zenodo.11151724 is GitHub\n# Social-Evolution-and-Behavior/Hart_Kronauer2023 v1.0.0 (commit 72d041a), from Hart et al. 2023\n# and named by this paper for processing calcium imaging: generate_tif_files.py (NWB to TIFF) and\n# macro_calcium_imaging.txt (ImageJ: image stabilization, fold change, peak maps, max\n# Z-projections). doi:10.5281/zenodo.11151756 is Hart_Kronauer2024 v1.0.0 (commit 1aef6bc):\n# Python that computes the proportions of ants outside the nest from Data S1 and plots the curves\n# fitted in GraphPad Prism. No code for the glomerulus ROI quantification, the AUC, the counts of\n# responding ROIs or the statistics (done in R and Prism) is published.\n#\n# Data the paper used.\n# Behavior (Figure 1, Figure S1, Table S1; Data S1, not in the dandiset): wild type clonal line B\n# ants, young 13 to 19 days and old 55 to 60 days post eclosion, in mixed-age colonies of 16 to 24\n# ants (12 of each age set up). Stimuli: 4-methyl-3-heptanone (6 trials), 4-methyl-3-heptanol (7),\n# the 9:1 blend (7) and pentane vehicle; per trial the number of young and old ants outside the\n# nest counted every 10 s; analysis from -10 to 60 s (8 time points per trial, which matches the\n# residual degrees of freedom of Table S1).\n# Confocal (Figure 2A and 2B): anti-SYNORF1 stained brains of young and old GCaMP6s ants, in the\n# Brain Image Library (doi:10.35077/g.1153), not in the dandiset.\n# Calcium imaging (Figures 2C to 4, S2 to S4; this dandiset): GCaMP6s ants (Orco-QF2,\n# 15xQUAS-GCaMP6s, OSN axons), young 15 to 20 days and old 60 to 61 days post eclosion; right AL;\n# 33 planes of 512 x 512 at 5 um steps; 40 volumes per trial; odor valve after a 3 s delay for\n# 5 s. Seven odors (alarm pheromones 4-methyl-3-heptanone and 4-methyl-3-heptanol; general\n# odorants 3-hexanone, isopropanol, ethylpyrazine, ethanol, propionic acid), each ant at one\n# concentration (3% or 48% v/v in paraffin oil), the seven in a randomized order repeated three\n# times (21 trials). Ants (Figure S3B legend): 48%, 7 young and 7 old; 3%, 3 young and 4 old\n# (21 in all, as the dandiset's subject count). Per-glomerulus n (young/old), Figures S2 and S4:\n# PGb 7/7, PGa 7/6, G1 7/7, G2 7/7, G3 7/6 in Figure S2 but 7/5 in Figure S4, G4 7/6.\n# The 90-day-old ants of Figure 3C and 3D are Hart et al. 2023, DANDI 000467, not this dandiset.\n#\n# Shared methods, from the STAR Methods (Image processing) and macro_calcium_imaging.txt.\n# Frames are volumes, numbered from 1 as in ImageJ. Per Z-plane, the time series is stabilized\n# (Image Stabilizer plugin; the macro uses Translation, 1 pyramid level, template update\n# coefficient 0.90, 200 iterations, error tolerance 1e-7); fold change = (F - F0)/F0 with F0 the\n# mean of frames 1 to 5. Peak response map = mean fold change over frames 9 to 14, a 2-pixel\n# minimum filter, a maximum projection through the Z-planes, values clipped to -1 and 4 (clipping\n# commutes with the minimum filter and the projection, so the macro's order and the Methods'\n# order agree). The macro skips the plane named 0 um when projecting (slice_num < 1); the Methods\n# say all Z-planes. The Methods are followed, and the macro's 32-plane projection is a variant.\n# Glomerulus AUC: on the Z-plane through the glomerulus centre, an ROI around it; a maximum\n# projection of that plane and the planes above and below; fold change as above; AUC = sum of\n# fold change over frames 6 to 40. Statistics in R: Welch's t tests (two-sided, R's t.test\n# default) and Wilcoxon tests (R's wilcox.test default, rank-sum between cohorts); no correction\n# for multiple comparisons is stated. Each ant gives one value per odor (the figures plot one\n# point per ant); the paper does not say how its three trials are combined. Figure S4C averages\n# the three trials per ant, so the per-ant value is the mean over its trials.\n# Open details, shared by the claims that use them:\n# - The volume period. The Methods say the volume is scanned every 0.83 s; the macro sets 1.2 s\n#   (periodVal), and 33 planes at 27.5 frames per second take 1.2 s. All windows are in frames,\n#   so this does not change any measure.\n# - ROIs. The whole-AL ROI, the responding-ROI sets and the six focal glomeruli (PGb, PGa,\n#   G1 to G4) were drawn by hand from the images; the paper gives no coordinates, and the focal\n#   glomeruli were matched across ants \"by examining the same region of the AL\" (Figure 3A shows\n#   one young and one old ant). Data S2 holds the paper's per-ant quantifications; matching the\n#   dataset's ants and values to them is the author's link check.\n# - Glomerulus fold change. \"a max Z-projection was generated ... and the fluorescence fold\n#   change was calculated\" allows (a) the ROI mean of the projected raw signal turned into fold\n#   change, or (b) fold change per pixel then the ROI mean. Both are run.\n# - Motion artifacts. \"A small number of trials were excluded\" from the responding-ROI counts,\n#   by eye. Readings: (a) all trials kept; (b) the trials Data S2 leaves out, if it marks them.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000773\"\npaper: doi:10.1016/j.cub.2024.05.031\nclaims:\n- id: fig1c-old-faster-alarm\n  statement: For the pooled alarm pheromone stimuli, separate logistic curves for young and old\n    ants fit better than a single curve, and old ants leave the nest faster.\n  source: Results, paragraph 1; Figure 1C; Table S1, row \"Pooled alarm pheromone stimuli\"\n  quote: For the pooled alarm pheromone stimuli, the preferred model incorporated separate curves\n    for young and old ants, with old ants responding faster\n  statistics:\n  - test: extra sum-of-squares F test, single against separate logistic curves\n    statistic: F(3, 314) = 8.006\n    p: 0.0001\n    p_relation: \"<\"\n    n: 20 trials (6 with 4-methyl-3-heptanone, 7 with 4-methyl-3-heptanol, 7 with the blend)\n  expected:\n  - quantity: YM, young (Table S1; tolerance the wider side of its 95% CI, 0.808 to 0.939)\n    value: 0.858\n    tolerance: 0.081\n  - quantity: YM, old (95% CI 0.883 to 0.947)\n    value: 0.914\n    tolerance: 0.033\n  - quantity: Y0, young (95% CI 0.527 to 0.617)\n    value: 0.571\n    tolerance: 0.046\n  - quantity: Y0, old (95% CI 0.626 to 0.703)\n    value: 0.663\n    tolerance: 0.040\n  - quantity: K, young (95% CI 0.042 to 0.106)\n    value: 0.070\n    tolerance: 0.036\n    unit: 1/s\n  - quantity: K, old (95% CI 0.074 to 0.128)\n    value: 0.099\n    tolerance: 0.029\n    unit: 1/s\n  data: elsewhere\n  where: Data S1, supplemental information of doi:10.1016/j.cub.2024.05.031 (PMC11265976)\n  criterion: From the Methods, Table S1 and alarm_behavior_calculations.py (commit 1aef6bc). For\n    each trial of the three alarm stimuli and each time point from -10 to 60 s in 10 s steps, the\n    proportion of young ants outside the nest (young outside over the colony's young, as the code\n    computes it; the Methods' \"by the total number within the arena\" is settled by the code) and\n    the same for old ants. The logistic Y = YM*Y0/((YM-Y0)*exp(-K*x)+Y0) of Table S1 is fit by\n    least squares to all per-trial points, once shared (3 parameters) and once per age (6), and\n    compared by the extra sum-of-squares F test; the residual degrees of freedom should be 314.\n    Prism's starting values are not given; any start that converges is a standard choice.\n    Reproduced when separate curves are preferred at p < 0.05, old ants are faster, and the six\n    parameters are within tolerance. \"Faster\" is not defined; readings (a) K old above K young,\n    (b) the old curve above the young curve at every time from 0 to 60 s. Partially reproduced\n    when the test and direction hold but a parameter is out of tolerance.\n- id: fig1c-vehicle-single-curve\n  statement: For the vehicle control a single curve for young and old ants is preferred, so the\n    two ages have similar baseline behavior.\n  source: Results, paragraph 1; Figure 1C right; Table S1, row \"Vehicle control\"\n  quote: For the vehicle control, a single curve for young and old ants was the preferred model\n    (extra sum-of-squares F test), indicating similar baseline behavioral patterns\n  statistics:\n  - test: extra sum-of-squares F test, single against separate quadratic curves\n    statistic: F(3, 90) = 2.617\n    p: 0.056\n    n: 6 vehicle trials (from the 90 residual degrees of freedom at 8 time points per age)\n  data: elsewhere\n  where: Data S1, supplemental information of doi:10.1016/j.cub.2024.05.031 (PMC11265976)\n  criterion: A claim of absence, judged on the paper's test. As in fig1c-old-faster-alarm, but on\n    the pentane trials and with the quadratic Y = B0 + B1*X + B2*X^2 the Methods and Table S1\n    give. Reproduced when the extra sum-of-squares F test gives p >= 0.05; not reproduced when\n    p < 0.05. F, p and the fitted parameters are reported either way.\n- id: fig1b-alarm-stimuli-similar\n  statement: The three alarm stimuli (4-methyl-3-heptanone, 4-methyl-3-heptanol and the 9:1\n    blend) make the ants leave the nest in a similar manner; one curve fits all three.\n  source: Results, paragraph 1; Figure 1B; Table S1, row \"Alarm pheromone stimuli, comparing\n    stimuli\"\n  quote: all three alarm pheromone stimuli caused ants to leave the nest in a similar manner, so\n    these samples were pooled for analyzing effects of age\n  statistics:\n  - test: extra sum-of-squares F test, single against separate logistic curves\n    statistic: F(6, 151) = 2.144\n    p: 0.052\n    n: 20 trials (6, 7 and 7)\n  data: elsewhere\n  where: Data S1, supplemental information of doi:10.1016/j.cub.2024.05.031 (PMC11265976)\n  criterion: A claim of absence, judged on the paper's test. Per trial and time point (-10 to\n    60 s), the proportion of all ants outside the nest; the logistic of Table S1 fit shared and\n    per stimulus; extra sum-of-squares F test (residual degrees of freedom 151). Reproduced when\n    p >= 0.05, not reproduced when p < 0.05; F, p and the parameters are reported either way.\n- id: figs1-heptanone-separate-curves\n  statement: For 4-methyl-3-heptanone alone, separate curves for young and old ants are preferred,\n    with old ants above young.\n  source: Figure S1 and legend; Table S1, row \"4-methyl-3-heptanone, comparing age\"\n  quote: For 4-methyl-3-heptanone, a model with separate curves was preferred.\n  statistics:\n  - test: extra sum-of-squares F test, single against separate logistic curves\n    statistic: F(3, 90) = 6.377\n    p: 0.0006\n    n: 6 trials\n  data: elsewhere\n  where: Data S1, supplemental information of doi:10.1016/j.cub.2024.05.031 (PMC11265976)\n  criterion: As fig1c-old-faster-alarm, on the 4-methyl-3-heptanone trials only. Reproduced when\n    separate curves are preferred at p < 0.05 and old ants are faster under either reading.\n- id: figs1-heptanol-blend-single-curve\n  statement: For 4-methyl-3-heptanol and for the blend, single curves for both ages are preferred,\n    though the trends are similar to 4-methyl-3-heptanone.\n  source: Figure S1 and legend; Table S1, rows \"4-methyl-3-heptanol\" and \"Blend, comparing age\"\n  quote: For 4-methyl-3-heptanol and the blend, similar trends were observed, but single curve\n    models were preferred\n  statistics:\n  - about: 4-methyl-3-heptanol, young against old\n    test: extra sum-of-squares F test\n    statistic: F(3, 106) = 1.979\n    p: 0.122\n    n: 7 trials\n  - about: blend, young against old\n    test: extra sum-of-squares F test\n    statistic: F(3, 106) = 2.529\n    p: 0.061\n    n: 7 trials\n  data: elsewhere\n  where: Data S1, supplemental information of doi:10.1016/j.cub.2024.05.031 (PMC11265976)\n  criterion: A claim of absence, judged on the paper's test, as fig1c-old-faster-alarm on each\n    stimulus. Reproduced when both tests give p >= 0.05; not reproduced when either gives\n    p < 0.05. The direction of the fitted curves is reported.\n- id: fig2b-gcamp-baseline-unchanged\n  statement: Total GCaMP6s fluorescence in the AL of dissected brains does not differ between young\n    and old ants.\n  source: Results, paragraph 3; Figure 2A and 2B\n  quote: Total fluorescence intensity did not differ with age, and calcium responses measured by\n    changes in GCaMP6s fluorescence should therefore be comparable between the two age cohorts\n  statistics:\n  - test: Welch's t test\n    p: 0.21\n  data: elsewhere\n  where: Brain Image Library, doi:10.35077/g.1153\n  criterion: A claim of absence, judged on the paper's test. From the Methods (Confocal\n    microscopy), a sum Z-projection of each brain's GCaMP6s channel, a rectangle around each AL,\n    and its integrated intensity (Fiji Measure); Welch's t test of young against old. The ROI\n    rectangles and n are not given (n is printed in Figure 2B only); readings for the sample\n    (a) each AL a value, (b) the mean of a brain's two ALs. Reproduced when p >= 0.05 under the\n    paper's test (the outcome both readings give; if they differ, both are shown and the claim\n    is blocked as methods_underspecified).\n- id: fig2d-whole-al-alarm-no-age-effect\n  statement: The mean calcium response across the entire AL to each alarm pheromone does not\n    differ between young and old ants, at 3% or at 48%.\n  source: Results, paragraph 4; Figure 2C and 2D\n  quote: we observed no effect of age on mean calcium response across the entire AL for either of\n    the two tested concentrations\n  statistics:\n  - test: Welch's t tests, one per pheromone and concentration\n    p: 0.05\n    p_relation: \">\"\n    n: 3 young and 4 old ants at 3%, 7 young and 7 old at 48%\n  criterion: A claim of absence, judged on the paper's test. Peak response maps as in the shared\n    methods; per trial, the mean pixel value inside a single ROI around the AL boundary defined on\n    a max Z-projection of raw fluorescence (Methods); per ant, the mean over its three trials of\n    the odor; Welch's t test young against old for each of the four pheromone and concentration\n    cells. The AL outline was drawn by hand; it is taken from the raw max projection by a\n    threshold, a standard choice, and the result is also shown with the outline shrunk and grown\n    by 5 pixels. Reproduced when all four tests give p >= 0.05; not reproduced when any gives\n    p < 0.05. The cohort means are reported. The 32-plane projection of the macro is a variant.\n- id: fig2e-heptanone-breadth-falls\n  statement: At 48%, 4-methyl-3-heptanone activates a few more glomeruli in young than in old ants\n    (medians of 4 against 2 responding ROIs), while the count for 4-methyl-3-heptanol does not\n    differ with age.\n  source: Results, paragraph 4; Figure 2E\n  quote: While there was no significant difference for 4-methyl-3-heptanol, 4-methyl-3-heptanone\n    activated a few more glomeruli in young ants than in old ants (medians of 4 versus 2\n    responding ROIs)\n  statistics:\n  - about: 4-methyl-3-heptanone, young against old\n    test: Wilcoxon test\n    p: 0.05\n    p_relation: \"<\"\n    n: 7 young and 7 old ants\n  - about: 4-methyl-3-heptanol, young against old\n    test: Wilcoxon test\n    p: 0.05\n    p_relation: \">\"\n    n: 7 young and 7 old ants\n  expected:\n  - quantity: median responding ROIs to 4-methyl-3-heptanone, young ants (counts are integers, so\n      the 10% tolerance means the value itself)\n    value: 4\n    tolerance: 0.4\n  - quantity: median responding ROIs to 4-methyl-3-heptanone, old ants\n    value: 2\n    tolerance: 0.2\n  criterion: From the Methods (Image processing). For each 48% ant, ROIs of the size and shape of\n    single glomeruli that respond in at least two trials, from the peak response maps; per ROI and\n    trial the mean peak fold change; an ROI responds to an odor when its mean over that odor's\n    trials is >= 0.2. The ROIs were drawn by hand; here they are the connected regions of a\n    trial's map at >= 0.2 that recur, overlapping, in at least two trials of any odor, split at\n    glomerulus size, a choice the paper does not fix, so the counts are also compared ant by ant\n    with Data S2. Motion-artifact trials under both readings of the shared open details. Wilcoxon\n    rank-sum test (R defaults) of young against old per pheromone. Reproduced when\n    4-methyl-3-heptanone gives p < 0.05 with young higher and medians within tolerance, and\n    4-methyl-3-heptanol gives p >= 0.05. Partially reproduced when the direction and the\n    4-methyl-3-heptanol result hold but the medians or the significance do not.\n- id: fig2-alarm-sparse\n  statement: Alarm pheromones are represented sparsely at both ages; only a small fraction of the\n    roughly 500 AL glomeruli respond to them.\n  source: Results, paragraphs 4 and 5; Figure 2C and 2E\n  quote: Calcium responses to 4-methyl-3-heptanone and 4-methyl-3-heptanol were sparse at both\n    tested ages ... Out of the ~500 glomeruli in the ant AL, only a small fraction responded to\n    alarm pheromones in young and/or old ants\n  depends_on:\n  - fig2e-heptanone-breadth-falls\n  criterion: The paper gives no threshold for \"sparse\" or \"small fraction\". On the 48% counts of\n    fig2e-heptanone-breadth-falls, readings (a) every ant's count for each alarm pheromone is at\n    most 5% of 500 (25 ROIs), (b) at most 10% (50 ROIs). Reproduced when both readings hold;\n    when they differ the claim is blocked as methods_underspecified, with the counts shown.\n- id: figs2a-mean-six-glomeruli-no-age-effect\n  statement: The alarm pheromone response averaged over the six focal glomeruli does not differ\n    between young and old ants.\n  source: Results, paragraph 5; Figure S2A\n  quote: The mean of responses across these six glomeruli did not differ with age\n  statistics:\n  - test: Welch's t tests, one per pheromone\n    p: 0.05\n    p_relation: \">\"\n    n: 7 young and 7 old ants, 48%\n  criterion: A claim of absence, judged on the paper's test. Per ant and pheromone, the AUC of\n    each focal glomerulus (shared methods, both fold-change readings), the mean over the\n    glomeruli identified in that ant (Figure S2A legend; some ants lack one), Welch's t test of\n    young against old. Reproduced when both tests give p >= 0.05; not reproduced when either gives\n    p < 0.05.\n- id: fig3b-g2-heptanone-weaker-old\n  statement: In glomeruli G1 to G4 alarm pheromone responses tend to weaken with age; the decline\n    is significant only for 4-methyl-3-heptanone in G2.\n  source: Results, paragraph 5; Figure 3B; Figure S2B\n  quote: For G1–G4, we observed a trend toward weaker responses with increasing age, which was\n    statistically significant for responses to 4-methyl-3-heptanone in G2\n  statistics:\n  - about: G2, 4-methyl-3-heptanone, young against old\n    test: Welch's t test\n    p: 0.0068\n    n: 7 young and 7 old ants\n  - about: the other seven glomerulus and pheromone pairs of G1 to G4\n    test: Welch's t tests\n    p: 0.05\n    p_relation: \">\"\n  criterion: Per ant, the AUC of G1 to G4 for each pheromone at 48% (shared methods, both\n    fold-change readings); Welch's t test of young against old for each of the eight pairs.\n    Reproduced when G2 with 4-methyl-3-heptanone gives p < 0.05 with young higher and the other\n    seven give p >= 0.05; partially reproduced when G2 holds and one or more of the others also\n    reaches p < 0.05. The sign of the young minus old mean is reported for all eight, for the\n    trend.\n- id: fig3d-pg-stronger-old\n  statement: PGb and PGa respond significantly more strongly to alarm pheromones in old than in\n    young ants; PGa does not respond to 4-methyl-3-heptanone.\n  source: Results, paragraph 5; Figure 3C and 3D\n  quote: The patterns in PG b and PG a were quite different, with significantly stronger calcium\n    responses in old ants compared to young ants\n  statistics:\n  - test: Welch's t tests\n    p: 0.05\n    p_relation: \"<\"\n    n: PGb 7 young and 7 old ants, PGa 7 young and 6 old\n  criterion: Per ant, the AUC of PGb and PGa for each pheromone at 48% (shared methods, both\n    fold-change readings); Welch's t test of young against old. Which pairs Figure 3D marks\n    significant cannot be read from the text; readings (a) PGb for both pheromones and PGa for\n    4-methyl-3-heptanol, (b) PGb for at least one pheromone and PGa for 4-methyl-3-heptanol.\n    Reproduced when, under a reading, each of its pairs gives p < 0.05 with old higher; not\n    reproduced when no reading holds. PGa's 4-methyl-3-heptanone AUC is reported.\n- id: fig3d-pg-60-vs-90-days-same\n  statement: PGb and PGa responses to alarm pheromones do not differ between 60-day-old ants and\n    the 90-day-old ants of the earlier study, so the change occurs between 14 and 60 days.\n  source: Results, paragraph 6; Figure 3C and 3D\n  quote: We found no significant differences between 60- and 90-day-old ants\n  statistics:\n  - test: Welch's t tests\n    p: 0.05\n    p_relation: \">\"\n  data: with_inputs\n  depends_on:\n  - fig3d-pg-stronger-old\n  criterion: A claim of absence, judged on the paper's test. The 90-day values are the earlier\n    study's data, DANDI 000467 (Hart et al. 2023, Cell 186, 3079), named in the key resources\n    table; this paper does not say which of those ants, odors and concentrations enter Figure 3C\n    and 3D, nor whether their AUC was recomputed. Readings (a) the 000467 ants given the two\n    pheromones at the same 48% concentration, AUC computed here as for 000773; (b) the per-ant\n    values the earlier paper or Data S2 publishes. Welch's t test of 60 against 90 days for PGb\n    with each pheromone and PGa with 4-methyl-3-heptanol. Reproduced when all give p >= 0.05; not\n    reproduced when any gives p < 0.05.\n- id: figs3b-whole-al-general-decline\n  statement: At 48%, 3-hexanone and isopropanol evoke broad AL responses in young but not old ants;\n    mean peak responses across the AL fall more than 9-fold (3-hexanone) and more than 57-fold\n    (isopropanol) with age.\n  source: Results, paragraph 7; Figure S3A and S3B\n  quote: Mean peak calcium responses across the AL declined dramatically with age for 3-hexanone\n    (>9-fold decline) and isopropanol (>57-fold decline)\n  statistics:\n  - about: 3-hexanone, 48%, young against old\n    test: Welch's t test\n    p: 5.1e-6\n    n: 7 young and 7 old ants\n  - about: isopropanol, 48%, young against old\n    test: Welch's t test\n    p: 0.0068\n    n: 7 young and 7 old ants\n  expected:\n  - quantity: young over old cohort mean of whole-AL peak fold change, 3-hexanone, 48% (a lower\n      bound; 10% below it is accepted)\n    value: 9\n    tolerance: 0.9\n  - quantity: young over old cohort mean, isopropanol, 48% (a lower bound)\n    value: 57\n    tolerance: 5.7\n  criterion: Whole-AL mean peak fold change per ant as in fig2d-whole-al-alarm-no-age-effect;\n    Welch's t test of young against old per odor. Reproduced when both tests give p < 0.05 with\n    young higher and the ratios of cohort means exceed 8.1 and 51.3; partially reproduced when\n    the tests hold but a ratio is lower. The ratio is unstable when the old mean is near zero;\n    the cohort means are reported with it.\n- id: figs3b-whole-al-other-no-age-effect\n  statement: The age decline of whole-AL responses is specific to 3-hexanone and isopropanol at\n    48%; ethylpyrazine, ethanol and propionic acid at 48%, and all five general odorants at 3%,\n    show no age effect.\n  source: Results, paragraph 7; Figure S3B\n  quote: an effect that was specific to these two odorants when presented at 48% concentration\n  statistics:\n  - test: Welch's t tests, one per odorant and concentration\n    p: 0.05\n    p_relation: \">\"\n    n: 3 young and 4 old ants at 3%, 7 and 7 at 48%\n  depends_on:\n  - figs3b-whole-al-general-decline\n  criterion: A claim of absence, judged on the paper's test, with the measure of\n    fig2d-whole-al-alarm-no-age-effect. Reproduced when all eight tests give p >= 0.05; not\n    reproduced when any gives p < 0.05.\n- id: figs3c-general-breadth-no-age-effect\n  statement: Age does not change the number of glomeruli activated by ethylpyrazine, ethanol or\n    propionic acid at 48%.\n  source: Results, paragraph 7; Figure S3C\n  quote: we found no effect of age on the number of activated glomeruli for ethylpyrazine,\n    ethanol, or propionic acid\n  statistics:\n  - test: Wilcoxon tests, one per odorant\n    p: 0.05\n    p_relation: \">\"\n    n: 7 young and 7 old ants\n  criterion: A claim of absence, judged on the paper's test. Responding-ROI counts as in\n    fig2e-heptanone-breadth-falls; Wilcoxon rank-sum test (R defaults) per odorant. Reproduced\n    when all three give p >= 0.05; not reproduced when any gives p < 0.05.\n- id: figs4a-general-odorants-in-focal-glomeruli\n  statement: 3-hexanone excites all six focal glomeruli in young ants and PGb, PGa and G4 in old\n    ants; isopropanol excites all but G1 in young ants only; propionic acid excites G4 at both\n    ages; no other general odorant excites a focal glomerulus.\n  source: Results, paragraph 8; Figure S4A\n  quote: We found that 3-hexanone activated all six glomeruli in young ants as well as activating\n    PG b , PG a , and G4 in old ants, while isopropanol activated five of the focal glomeruli (all\n    except G1) in young ants only ... Additionally, propionic acid activated G4 in young and old\n    ants, while none of the other general odorants activated any of the six focal glomeruli\n  statistics:\n  - about: young, PGb, 3-hexanone\n    test: one-sided one-sample Welch's t test against zero\n    p: 4.9e-5\n  - about: young, PGb, isopropanol\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.0063\n  - about: young, PGa, 3-hexanone\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.0025\n  - about: young, PGa, isopropanol\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.0074\n  - about: young, G1, 3-hexanone\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.021\n  - about: young, G2, 3-hexanone\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.00058\n  - about: young, G2, isopropanol\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.0011\n  - about: young, G3, 3-hexanone\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.00011\n  - about: young, G3, isopropanol\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.0036\n  - about: young, G4, 3-hexanone\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.00031\n  - about: young, G4, isopropanol\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.0033\n  - about: young, G4, propionic acid\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.033\n  - about: old, PGb, 3-hexanone\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.00018\n  - about: old, PGa, 3-hexanone\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.011\n  - about: old, G4, 3-hexanone\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.027\n  - about: old, G4, propionic acid\n    test: one-sided one-sample Welch's t test against zero\n    p: 0.023\n  criterion: Per ant, the AUC of each focal glomerulus for each general odorant at 48% (shared\n    methods, both fold-change readings); for each age, glomerulus and odorant (60 cells), a\n    one-sided one-sample t test that the mean AUC exceeds zero (Figure S4A legend), at p < 0.05\n    uncorrected as the figure marks it. Reproduced when exactly the 16 cells above are\n    significant; partially reproduced when the text's pattern for 3-hexanone and isopropanol holds\n    but cells for the other odorants differ; not reproduced otherwise. All mismatches are listed.\n- id: fig4-general-odorants-decline\n  statement: Responses to 3-hexanone and isopropanol decline significantly with age in five of the\n    six focal glomeruli (3-hexanone in all but PGb, isopropanol in all but G1).\n  source: Results, paragraph 9; Figure 4; Figure S4B\n  quote: Directly comparing calcium responses across age cohorts showed that responses to\n    3-hexanone and isopropanol each significantly declined with age in 5 out of 6 glomeruli\n    (3-hexanone, all except PG b ; isopropanol, all except G1)\n  statistics:\n  - about: 3-hexanone, PGa\n    test: Welch's t test\n    p: 0.014\n  - about: 3-hexanone, G1\n    test: Welch's t test\n    p: 0.026\n  - about: 3-hexanone, G2\n    test: Welch's t test\n    p: 0.0012\n  - about: 3-hexanone, G3\n    test: Welch's t test\n    p: 0.00017\n  - about: 3-hexanone, G4\n    test: Welch's t test\n    p: 0.0015\n  - about: isopropanol, PGb\n    test: Welch's t test\n    p: 0.044\n  - about: isopropanol, PGa\n    test: Welch's t test\n    p: 0.011\n  - about: isopropanol, G2\n    test: Welch's t test\n    p: 0.0024\n  - about: isopropanol, G3\n    test: Welch's t test\n    p: 0.0080\n  - about: isopropanol, G4\n    test: Welch's t test\n    p: 0.0084\n  criterion: Per ant, the AUC of each focal glomerulus for 3-hexanone and isopropanol at 48%\n    (shared methods, both fold-change readings); Welch's t test of young against old. Reproduced\n    when the ten pairs above give p < 0.05 with young higher and 3-hexanone in PGb and\n    isopropanol in G1 give p >= 0.05; partially reproduced when at least four of the five\n    glomeruli per odorant decline significantly.\n- id: fig4-propionic-acid-g2-g3\n  statement: In young ants propionic acid gives a very small negative deflection in G2 and G3 that\n    declines in amplitude with age; its responses in G4 tend to fall with age, not significantly.\n  source: Results, paragraph 9; Figure 4; Figure S4B\n  quote: We also found that, in young ants, propionic acid produced a very small negative\n    deflection in G2 and G3 that declined in amplitude with age ... Propionic acid responses in G4\n    also tended to decrease with age, but the difference was not statistically significant\n  statistics:\n  - about: G2, young against old\n    test: Welch's t test\n    p: 0.0052\n  - about: G3, young against old\n    test: Welch's t test\n    p: 0.029\n  - about: G4, young against old\n    test: Welch's t test\n    p: 0.05\n    p_relation: \">\"\n  criterion: Per ant, the AUC for propionic acid at 48% in G2, G3 and G4 (shared methods, both\n    fold-change readings); Welch's t test of young against old. Reproduced when the young mean AUC\n    is below zero in G2 and G3, both tests give p < 0.05 with the old mean nearer zero, and G4\n    gives p >= 0.05 with the old mean below the young.\n- id: figs4d-pgb-hexanone-dynamics\n  statement: In PGb, 3-hexanone responses of old ants have a lower peak but decline more slowly\n    than those of young ants; the AUC over frames 9 to 14 is larger in young ants and over frames\n    35 to 40 larger in old ants.\n  source: Results, paragraph 10; Figure S4C and S4D\n  quote: responses to 3-hexanone in PG b had a lower peak amplitude but then declined more slowly\n    in old versus young ants\n  statistics:\n  - about: frames 9 to 14, young against old\n    test: Welch's t test\n    p: 0.0020\n    n: 7 young and 7 old ants\n  - about: frames 35 to 40, young against old\n    test: Welch's t test\n    p: 0.0098\n    n: 7 young and 7 old ants\n  criterion: Per ant, the PGb fold-change trace for 3-hexanone at 48% (shared methods, both\n    fold-change readings), the mean of its three trials (Figure S4C legend), summed over frames 9\n    to 14 and over frames 35 to 40 (the legend's \"AUC\", whose plotted scale is that of a sum).\n    Reproduced when frames 9 to 14 give young above old and frames 35 to 40 old above young, each\n    by Welch's t test at p < 0.05; partially reproduced when one of the two holds.\n- id: pg-opposite-modulation\n  statement: In PGb and PGa, responses to alarm pheromones rise with age while responses to general\n    odorants fall or stay absent; no general odorant response rises with age in any focal\n    glomerulus.\n  source: Results, paragraph 9; Figures 3, 4 and S4B\n  quote: Whereas alarm pheromone responses increased with age specifically in PG b and PG a ,\n    general odorant responses showed overall similar patterns across all six glomeruli, either with\n    no responses or decreasing responses with age\n  depends_on:\n  - fig3d-pg-stronger-old\n  - fig4-general-odorants-decline\n  criterion: Reproduced when fig3d-pg-stronger-old is reproduced, PGb or PGa has at least one\n    general odorant with a significant decline in fig4-general-odorants-decline, and none of the\n    30 glomerulus and general odorant Welch's t tests at 48% gives p < 0.05 with old higher.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000773/10.1016-j.cub.2024.05.031.yaml paper/10.1016-j.cub.2024.05.031.txt; grep -n ": .*: " claims/000773/*.yaml | grep -v "^\S*:[0-9]*:#" | head
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/000773/10.1016-j.cub.2024.05.031.yaml`. It passes the schema and every quote is found word for word. The checker still reports 28 problems, all of them p-values it could not find in the text: they are printed only inside the panels of supplement Figures S2B, S3B, S4A, S4B and S4D, and I confirmed each one by reading the supplement PDF. Nothing is committed.

**Text read:** the accepted author manuscript (NIHMS1997610, PMC11265976, from Europe PMC), with its main text, figure legends and STAR Methods, plus supplement MMC1 (Figures S1–S4 and Table S1). I opened supplement PDF pages 2–7 only to read the p-values and sample sizes inside the figures and to check Table S1. Data S1 and S2 are spreadsheets and I did not read them.

**Code read:** two Zenodo records.
- doi:10.5281/zenodo.11151724 (Hart_Kronauer2023 v1.0.0, commit 72d041a): converts the NWB files to TIFF, and an ImageJ macro makes the fold-change maps and Z-projections.
- doi:10.5281/zenodo.11151756 (Hart_Kronauer2024 v1.0.0, commit 1aef6bc): computes the behavior proportions and plots the curves.
- No code is published for the glomerulus ROIs, the area under the curve, the counts of responding ROIs, or the statistics (run in R and Prism).

**Claims:** 21, all with quotes; 20 record statistics (50 values) and 20 have criteria.
- **Data:** 5 behavior claims and 1 confocal claim are `elsewhere` (Data S1; Brain Image Library doi:10.35077/g.1153). The 60- versus 90-day comparison is `with_inputs` (DANDI 000467). The other 14 use this dataset.
- **Expected values:** two claims have them, given with tolerances: the six Table S1 curve parameters (tolerance from their 95% CIs), the medians of 4 and 2 responding ROIs, and the >9-fold and >57-fold declines.

**Details the paper leaves open, with the readings named:**
- **How an ant's three trials are combined:** the mean, taken from the Figure S4C legend.
- **Glomerulus fold change:** (a) the ROI mean of the projected signal, then fold change; (b) fold change per pixel, then the ROI mean.
- **Trials with motion artifacts:** (a) all trials kept; (b) the trials Data S2 leaves out, if it marks them.
- **Hand-drawn ROIs** (whole-AL outline, responding-ROI sets, the six focal glomeruli): no coordinates are given. The criteria use a standard, sensitivity-bracketed choice and check the counts against Data S2.
- **Confocal sample unit:** (a) each AL; (b) the mean of a brain's two ALs.
- **"Faster" behavior:** (a) the old ants' rate K is higher; (b) the old ants' curve is above the young ants' from 0 to 60 s.
- **"Sparse":** (a) at most 5% of about 500 glomeruli; (b) at most 10%.
- **Which pairs in Figure 3D are significant:** (a) PGb for both pheromones and PGa for 4-methyl-3-heptanol; (b) PGb for at least one pheromone and PGa for 4-methyl-3-heptanol.
- **The 90-day data:** (a) the 000467 ants given 48% pheromone, with the area under the curve recomputed here; (b) the published per-ant values.
- **The Methods and code disagree in two places:**
  - Proportion of ants outside the nest: the code settles it as divided by the number of ants of that age.
  - Z-projection: the macro skips the 0 µm plane; the Methods are followed and the macro's version is a variant.
- **Volume period:** the Methods say 0.83 s and the code says 1.2 s. All windows are in frames, so this changes nothing.

**Missing from the paper:**
- **p-values in the main figures:** the images of Figures 1–4 are not in the text, so p-values printed only in Figures 2D, 2E, 3B, 3D and 4 are recorded as bounds (p < 0.05 or > 0.05). The confocal n (Figure 2B) and the 90-day n are also unknown.
- **Inconsistencies:**
  - G3's young/old n is 7/6 in Figure S2 but 7/5 in Figure S4.
  - Two Table S1 entries are inconsistent: the blend's young Y0 confidence interval, and one K value for the stimulus comparison that falls outside its own interval.

## End of run

30 turns, 6 minutes, result: success.
