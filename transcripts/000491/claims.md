# 000491 · claims · run 39947895425

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/000491 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la claims/001453/ paper/ claims/000491 2>&1; wc -c paper/*; head -c 3000 claims/001453/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
tail -c 15000 claims/001453/*.yaml; ls claims/ | head; ls claims/*/ | head -40
```

```
elow 9. The fish cannot be
    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
    the counts per species are compared instead. The sign of the zebrafish turning response
    to codes 9 and 11 is reported, as the code and the protocol file disagree on which of them
    is lateral right.
- id: fig1d-dc-faster-all-codes
  statement: Danionella cerebrum (DC) swim at a higher median velocity than zebrafish (ZF)
    across the visual stimuli.
  source: Results, Larval DC exhibit higher average swimming speeds, paragraph 1; Figure 1D
  quote: DC show a significantly higher median velocity across all stimuli than ZF
  statistics:
  - test: two-way ANOVA, main species effect
    p: 0.05
    p_relation: "<"
  criterion: Tested without stimulus names, over all 21 stimulus codes. For each fish and code
    the median over trials of the trial speed in pixels per second; a two-way ANOVA (type II)
    of these values on species, code and their interaction. Reproduced when the species effect
    has p < 0.05 and the DC median over all fish and code values exceeds the ZF median.
- id: fig1d-median-velocity
  statement: Across the whole-field stimuli DC have a higher median velocity than ZF (9.8
[... 309 more lines not kept]
```

**Agent**

Now the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.21203-rs.3.rs-2587250-v1.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
fold -s -w 200 paper/*.txt | head -c 40000
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/94d4b1b9-0f53-41d8-ba71-f3e02b77be09/tool-results/bqgroxmkz.txt"
}
```

```
1	DOI: 10.21203/rs.3.rs-2587250/v1
2	Version: as served by ncbi_pmc
3	Source: ncbi_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	pmc Res Sq 3885 ressq 101768035 ResearchSquare Research Square 2693-5015 American Journal Experts PMC9949243 PMC9949243.1 9949243 9949243 36824982 10.21203/rs.3.rs-2587250/v1 10.21203/rs.3.rs-2587250 
8	1 preprint 1 Article Sizes and Shapes of Perivascular Spaces Surrounding Murine Pial Arteries Raicevic Nikola 1 Forer Jarod M. 1 Ladrón-de-Guevara Antonio 2 3 Du Ting 2 4 Nedergaard Maiken 2 Kelley 
9	Douglas H. 1 Boster Kimberly 1 * 1 Department of Mechanical Engineering, University of Rochester, Rochester, USA. 2 Center for Translational Neuromedicine and Department of Neuroscience, University 
10	of Rochester Medical Center, Rochester, USA. 3 Department of Biomedical Engineering, University of Rochester, Rochester, USA. 4 School of Pharmacy, China Medical University, China. Authors’ 
11	contributions KASB and DHK conceived the study. ALG and TD performed mouse surgeries and image acquisitions. KASB created the code that performed the segmentation, generates the normal slices, 
12	creates the circle, ellipse, and polynomial fits, and calculates the hydraulic resistance. JF wrote the code that creates spline fit. NR processed all the data, including performing segmentation, 
13	taking normal slices, fitting the idealized geometries, and calculating hydraulic resistance and velocity profile. KASB, NR, JF, and DHK wrote the paper. All authors read and approved the manuscript. 
14	MN and DHK supervised. * Correspondence: [removed: an e-mail address] 17 2 2023 429619 rs.3.rs-2587250 23 02 2023 24 02 2023 13 09 2024 https://creativecommons.org/licenses/by/4.0/ This work is licensed 
15	under a Creative Commons Attribution 4.0 International License , which allows reusers to distribute, remix, adapt, and build upon the material in any medium 
[... 192 more lines not kept]
```

**Agent calls Bash**

```bash
fold -s -w 200 paper/*.txt | tail -c +40000
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/94d4b1b9-0f53-41d8-ba71-f3e02b77be09/tool-results/b42xksjn5.txt"
}
```

```
1	aks at approximately 0.5, indicating that the two PVS sides are typically asymmetric, a feature that results in reduced hydraulic resistance compared to a symmetric shape of the 
2	same area ([ 18 ]). The PVS narrows dramatically further from the vessel. One difference between the polynomial and ellipse fits is highlighted in Figure 9A , where the distributions of heights of 
3	the PVS, H 1 , H 2 , and H 3 , peak at 1.34, 0.792, and 0.307, respectively, indicating that the PVS is larger closer to the vessel and smaller at the ends of the PVS. H 1 , the height of the PVS 
4	close to the vessel, is 4 times larger than H 3 , the height of the PVS far from the vessel, indicating that the PVS is typically thicker close to the vessel and thinner further away from the vessel 
5	and suggesting a dramatic change in height along the length of the PVS, a feature not captured by the ellipse fit. The PVS is often concave. The ratio of the change in heights, ( H 2 − H 3 )/( H 1− H 
6	2) shown in Figure 9F describes the curvature of the bottom edge of the PVS, with values greater than one indicating the PVS is convex, and values less than one indicating the PVS is concave. The 
7	peak of the curvature distribution is 0.108, showing that the PVS is most often concave, rather than convex, as is required by the ellipse fit. This concavity has implications for the resistance to 
8	flow, since the resistance would be larger for a concave shape of the same area than a convex shape, and is a large part of why the ellipse, which is convex, has a smaller resistance than the 
9	segmentation. Optimal model of the PVS Despite having a similar peak in area ratio, the spline fit has a much higher hydraulic resistance, which we attribute to the way the PVS rapidly narrows, 
10	creating a smaller space adjacent to the vessel. The narrow space results in slower speeds ( Figure 7 ) and considerably higher hydraulic resistances ( Figure 6B ). Because of the way spline fit is 
11	defined only with 
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i -B2 -A6 "supplement" docs/pilot-notes.md | head -80; ls tools/; ls code 2>/dev/null
```

```
Exit code 2
260-gave no sign of whether the paper states it at all. Every finding now has
261-either a quote or an `inferred` note saying why the statement is the
262:author's reading, such as numbers that appear only in a supplementary
263-table. Abstract-only papers are quoted from the abstract where it states the
264-finding. Every claim must come from and pertain to its paper, so five
265-claims that the paper's open text does not state were dropped, with their
266-outcomes: four of 001754 taken from the dandiset's description, and one of
267-000691 read from the paper's code (its method is now written out in the
268-claim that referred to it).
269-
270-The full texts of the nine remaining papers were obtained on 2026-10-20 as
271:PDFs (the six abstract-only papers with their supplements where they have
272-one, the Cell paper of 000350, and version 1 of the two preprints), and
273-their claims were quoted from them; the manuscript quotes of 000067 were
274-also checked against the publisher's PDF. Of the 1,280 claims, 24 are
275-links, 1,248 findings are quoted and 8 are inferred; 509 have statistics
276-(1,040 entries). The six papers first written from the abstract had their
277-method choices fixed by the author without the paper's Methods; reviewing
--
[... 58 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000491/ | python -c "import json,sys;d=json.load(sys.stdin);print(d['draft_version']['name']);print(d.get('most_recent_published_version'))"; curl -s https://api.dandiarchive.org/api/dandisets/000491/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('description'));print(d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Grep**

```json
{
 "pattern": "github|gitlab|zenodo|code availab|figshare",
 "path": "paper",
 "-i": true,
 "output_mode": "count"
}
```

```
No matches found

Found 0 total occurrences across 0 files.
```

**Agent calls Bash**

```bash
sed -n 1,60p tools/claims_check.py; ls claims/*/ | grep -c yaml; grep -l "open\b\|readings" claims/*/*.yaml | head -3
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 45 more lines not kept]
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

**Agent**

Paper text is the Research Square preprint v1 (PMC9949243). It includes the full Methods, but Additional Files 1 to 6 are not in it, and the paper links no code. I'm writing the claims now.

**Agent calls Write**

```json
{
 "file_path": "claims/000491/10.21203-rs.3.rs-2587250-v1.yaml",
 "content": "# Claims for Raicevic, Forer, Ladron-de-Guevara, Du, Nedergaard, Kelley & Boster (2023), \"Sizes\n# and Shapes of Perivascular Spaces Surrounding Murine Pial Arteries\", on dandiset 000491.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read. The Research Square preprint, version 1 (doi:10.21203/rs.3.rs-2587250/v1), full text\n# as served by PubMed Central (PMC9949243): Background, Methods, Results, Discussion, figure\n# legends and Tables 1 to 3. The version of record (Fluids and Barriers of the CNS 20, 56, 2023,\n# doi:10.1186/s12987-023-00454-z) was not read. Additional Files 1 to 6 were not in the text:\n# File 1 is the full description of the segmentation (the main Methods give the approach used),\n# Files 2 to 6 are figures (average images, fits, and per-location distributions of area ratio\n# and resistance). The per-location numbers the claims use are stated in the main Results. The\n# Results cite \"Additional File 3\" for per-location area ratios, which the file list names\n# Additional File 4. No PDF was supplied. The paper links no code (data \"available from the\n# corresponding author upon reasonable request\"; the authors' contributions say the code is\n# MATLAB, written by KASB and JF), so no repository was read and no detail is settled by code.\n#\n# Data the paper used. 14 pial periarterial PVS segments (locations A to N) in 9 wild-type mice\n# (BPN/3J or beta-actin-GFP on C57BL/6, male and female, 8 to 12 weeks), ketamine/xylazine\n# anesthesia, cranial window over the MCA territory, intracisternal BSA-647 or BSA-594 CSF tracer,\n# intravascular FITC-dextran. 3D two-photon stacks, 512 by 512 pixels, 0.648 um per pixel in the\n# transverse plane and 1 um per step in depth, 16 bit. The PVS and vessel were segmented with a\n# depth-varying threshold (Edge Finder, with manual refinement; Mean + Standard Deviation for\n# locations G, I and J, J for the PVS only), small regions removed, the largest vessel region and\n# two largest PVS regions kept, holes filled, branching vessels removed by hand, overlaps resolved\n# by hand. Between 54 and 451 cross sections normal to the vessel centerline per segment, about\n# 0.8 um apart. Measured per cross section: segmented PVS and vessel areas, PVS-to-vessel area\n# ratio, hydraulic resistance per unit length of the segmented PVS and of three fits (ellipse,\n# spline, polynomial) and of the optimal elliptical annulus, and the fit parameters (ellipse R1,\n# R2, R3, Oh, Ov; polynomial R1, H1, H2, H3, HC, WS, WL).\n# The dandiset description says it holds, for the 14 datasets of 9 subjects, the 3D stacks in\n# three channels and the final binary segmentation of PVS and vessel used for the paper, and maps\n# subjects to the paper's mice and locations: sub-BPN-OLD-M2 (mouse 1, A and B), sub-BPN-OLD-M3\n# (mouse 2, C and D), sub-BPN-M4 (mouse 3, E and F), sub-BPN-M6 (mouse 4, G and H), sub-BPN-M7\n# (mouse 5, I and J), sub-21-07-19-b-act (mouse 6, K), sub-21-10-08-b-act (mouse 7, L),\n# sub-21-09-01-b-act (mouse 8, M), sub-21-09-20-b-act (mouse 9, N). The 2D time series used to\n# validate the segmentation are not named in the description.\n#\n# The common pipeline, from the Methods, with the details they leave open and the readings\n# each claim runs where the detail could change its outcome. Start from the deposited final\n# segmentations (the paper's segmentation step includes manual work that cannot be redone).\n# (P1) Resample the masks to isotropic resolution. Open, the target voxel size. Readings\n#   (a) 0.648 um (depth upsampled), (b) 1 um (transverse downsampled).\n# (P2) Vessel centerline from MATLAB bwskel (or an equivalent 3D skeleton), erroneous points\n#   removed by hand. Open, which points were removed. Readings (a) the longest path through the\n#   skeleton, side branches dropped, (b) all skeleton points.\n# (P3) Second-order polynomials fit to the centerline points in the transverse plane and in the\n#   axial plane (XZ or YZ, by vessel orientation); the normal at each center point from the cross\n#   product of vectors perpendicular to the two fits; slices taken with obliqueslice (or an\n#   equivalent oblique resampling) and shifted so the vessel center is at the image center.\n#   Orientation within the slice. \"Top\" in the paper is the brain surface side (the vessel bottom\n#   is the deep side where red blood cells attenuate the signal, Methods, Idealized geometries),\n#   so the slice's vertical axis is the projection of the depth axis, top toward the surface;\n#   left and right follow from a fixed direction along the centerline. This is a reading of the\n#   Methods and Figures 3 and 4; the paper does not state it.\n# (P4) Exclude a cross section when the distance from the vessel center to the edge of the\n#   imaging plane is less than the median width of the PVS divided by 2.5. Open, how the PVS\n#   width is measured and over what the median is taken. Readings (a) the horizontal extent of\n#   the PVS segmentation in each slice, median over the segment's slices, (b) the polynomial-fit\n#   width W (vessel edge to PVS end, Figure 4), median over the segment's slices and both sides.\n#   Open also whether the distance is measured in the slice or in the 3D volume; the slice\n#   reading is used, as the criterion is stated for the imaging plane.\n# (P5) Areas from the segmentation in each slice. The area ratio is PVS area over vessel area.\n#   Open, for the segmentation's ratio, the vessel area. Readings (a) the segmented vessel area\n#   (Figure 5A plots segmented areas), (b) the area of the fitted circle, pi R1^2 (the vessel fit\n#   is used for all fits). For the fits, the vessel is the fitted circle.\n# (P6) Vessel circle fit to edge points of the vessel segmentation, excluding edge points inside\n#   the eroded convex hull of the segmentation. Open, the erosion size and the circle-fitting\n#   method. Readings, erosion by 1, 3 and 5 pixels; algebraic least-squares circle fit (a\n#   standard choice; the paper names none).\n# (P7) Distribution peak (Methods, Defining the distribution peak), the center of the bin of\n#   largest probability density among 20 evenly spaced bins. Open, the range binned. Readings\n#   (a) minimum to maximum of all values, (b) the values left after removing outliers as the\n#   Methods define them (more than 1.5 IQR above the 75th or below the 25th percentile), as the\n#   plotted distributions do. Percentiles from all values.\n# (P8) Hydraulic resistance per unit length, Poiseuille flow, Poisson's equation solved by finite\n#   elements on a triangular mesh (MATLAB solvepde), with no-slip on the PVS boundary, after the\n#   PVS region is eroded by one pixel; mesh refined until the resistance of a circle of the same\n#   area is within 1% of the exact value; viscosity 7.058e-4 Pa s; R = (dP/dn)/Q. Both PVS\n#   lobes form one cross section, Q summed over them (a reading; the paper treats the cross\n#   section as one channel). The pixel size follows P1.\n# (P9) Fits (Methods, Idealized geometries; Figure 4; Table 1). Ellipse, the ellipse with the\n#   centroid and second central moments of the PVS segmentation in the slice (both lobes\n#   together), R2 and R3 its semi-major and semi-minor axes, Oh and Ov the horizontal and\n#   vertical offsets of the vessel center from the ellipse center. Open, the PVS region of the\n#   ellipse fit. Readings (a) the ellipse minus its overlap with the circle, (b) ellipse area\n#   minus circle area. Spline, six control points at horizontal 0, R1, 2R1, 3R1, 4R1, 5R1 from the\n#   vessel center and vertical 1.1111, 0.85, 0.2667, 0.1111, 0.1111, 0.1111 R1 above the PVS\n#   midline, joined by a spline and mirrored about both axes, the vessel center 0.0667 R1 below\n#   the midline (Table 1 and Methods); open, the spline type, reading an interpolating cubic\n#   spline (a standard choice). Polynomial, a line fit by least squares to points on the top\n#   edge of the PVS, and on each side of the vessel a second-order polynomial fit by least squares\n#   to points on the bottom edge. Open, which pixels are edge points and where each side ends.\n#   Reading, per image column crossing the PVS, the topmost PVS pixel for the line and the\n#   bottommost for the polynomial of that side, columns outside the vessel's horizontal extent\n#   for the bottom; each side ends at the outermost PVS column on it. The parameters as the\n#   Figure 4 legend defines them, W from the vessel edge to the end of the PVS (WS and WL the\n#   shorter and longer side), HC from the top of the vessel to the line, H1 the height next to\n#   the vessel, H2 midway, H3 at the end, each height between the line and the polynomial.\n#   The polynomial PVS region is bounded by the line above, the polynomials below, the PVS ends\n#   and the circle.\n# Table 2's 25th and 75th percentiles and IQRs of resistance are garbled in the text (the 75th\n# percentile is printed below the median, exponents appear lost); they are not used. Table 3's\n# dimensional values (R1 peak 64.9 um, median 139 um) disagree with the vessel radius peak of\n# 28 um that the Results and Discussion give and are not used; its ratios are.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000491\"\npaper: doi:10.21203/rs.3.rs-2587250/v1\nclaims:\n- id: cross-section-counts\n  statement: After excluding cross sections near the edge of the imaging volume, each of the 14\n    PVS segments yields between 54 and 451 normal cross sections, about 0.8 um apart.\n  source: Methods, Creating normal cross sections\n  quote: This resulted in between 54 and 451 different cross sections for each of the 14 PVS\n    segments that were included in the subsequent analysis. The average distance between normal\n    planes was approximately 0.8 μ m.\n  expected:\n  - quantity: fewest cross sections in a segment\n    value: 54\n    tolerance: 5.4\n  - quantity: most cross sections in a segment\n    value: 451\n    tolerance: 45.1\n  - quantity: mean distance between normal planes\n    value: 0.8\n    tolerance: 0.08\n    unit: um\n  criterion: Pipeline P1 to P4 of the opening comment, one slice per centerline point. The\n    claim holds under a reading when the fewest and most cross sections per segment lie in\n    the range 54 to 451 widened by 10% of each bound, and the mean spacing is within\n    tolerance. Every combination of readings of P1, P2 and P4 is run.\n- id: segmentation-validation-overlap\n  statement: Where a high signal-to-noise 2D time-averaged image was acquired, the 3D\n    segmentation at the matching depth overlaps the 2D segmentation by at least 70% of the\n    union area, for both PVS and vessel.\n  source: Methods, Image Segmentation, last paragraph; Figure 2 legend\n  quote: To consider the segmentation successful, at least 70% of the area had to overlap in\n    both PVS and vessel ... The 3D segmentation and 2D segmentation match over 70% which gives\n    confidence that 3D segmentation is accurate.\n  expected:\n    quantity: smallest overlap, intersection over union of 2D and 3D segmentations\n    value: 0.7\n    tolerance: 0\n  criterion: Overlap as Equation 1, the area of the intersection over the area of the union of\n    the 2D and 3D segmentations at the depth that minimizes their difference, after aligning the\n    fields of view (the registration of Boster et al., reference 31, is not described here). The\n    2D segmentations must come with the data, since the paper's thresholds for them are not\n    given. Reproduced when every validated segment has overlap of at least 0.70 for both PVS and\n    vessel. The 70% is the paper's acceptance threshold, so no tolerance applies.\n- id: fig5a-pvs-area-scales-with-vessel-area\n  statement: PVS area increases with vessel area only approximately; the least-squares line of\n    PVS area on vessel area over all cross sections has slope 1.05 (95% CI 0.973 to 1.12) and\n    R2 of 0.158.\n  source: Results, Area ratio, paragraph 1; Figure 5A\n  quote: The area of the PVS generally increases with the area of the vessel, but the trend is\n    only approximate, as evidenced by the low R 2 value of the fit line (0.158). The slope of the\n    fit line is 1.05, (95% confidence interval 0.973, 1.12).\n  statistics:\n  - about: slope of PVS area on vessel area\n    test: least-squares fit\n    ci:\n      level: 0.95\n      low: 0.973\n      high: 1.12\n    n: all cross sections of the 14 segments\n  expected:\n  - quantity: slope of PVS area on vessel area\n    value: 1.05\n    tolerance: 0.077\n  - quantity: R2 of the fit\n    value: 0.158\n    tolerance: 0.0158\n  criterion: Pipeline P1 to P5, segmented areas of every retained cross section pooled over the\n    14 segments, ordinary least squares of PVS area on vessel area (Figure 5A legend). The\n    slope tolerance is the larger half-width of the paper's 95% CI; the R2 tolerance is 10%.\n    Open, whether the line has an intercept. Readings (a) with intercept, (b) through the\n    origin (the Results compare the slope with the area ratio). Reproduced when, under one\n    reading, both values are within tolerance.\n- id: fig5e-area-ratio-distribution\n  statement: The PVS-to-vessel area ratio of the segmentation varies widely across cross\n    sections; its distribution peaks at 1.12, its median is 1.88 and its IQR is 1.79 (25th\n    percentile 1.21, 75th 3.00), so the ratio varies by more than 100%.\n  source: Results, Area ratio, paragraph 1; Figure 5E; Table 2\n  quote: There is considerable variation in the area ratio, and the interquartile range of the\n    segmented area ratio is 1.79 ( Table 2 ), a value on the same order as the median value of\n    1.88, meaning that the area ratio varies by more than 100%. The peak value of 1.12\n  expected:\n  - quantity: peak of segmented area ratio distribution\n    value: 1.12\n    tolerance: 0.112\n  - quantity: median segmented area ratio\n    value: 1.88\n    tolerance: 0.188\n  - quantity: IQR of segmented area ratio\n    value: 1.79\n    tolerance: 0.179\n  - quantity: 25th percentile of segmented area ratio\n    value: 1.21\n    tolerance: 0.121\n  - quantity: 75th percentile of segmented area ratio\n    value: 3.0\n    tolerance: 0.3\n  criterion: Pipeline P1 to P5 and P7, the ratio of every retained cross section pooled over the\n    14 segments. Reproduced when, under one combination of the readings of P1, P2, P4, P5, P6\n    (when P5 reading b) and P7, all five values are within tolerance; partially reproduced when\n    the median and IQR are within tolerance but the peak is not.\n- id: fig5bc-area-intersegment-variation\n  statement: Variation in PVS area is much larger between PVS segments than along the length of a\n    single segment.\n  source: Results, Area ratio, paragraph 2; Figure 5B and 5C\n  quote: From Figure 5 , it is clear that the variation in PVS area is much larger between\n    segments of PVS than along the length of a single PVS segment. We quantified this difference\n    by plotting the median PVS area from each segment and the interquartile range of each segment\n  criterion: Pipeline P1 to P4, per segment the median and IQR of segmented PVS area (Figure 5B\n    and 5C). The paper compares these by eye and gives no measure. Readings of \"much larger\"\n    from what the figure shows (a) the IQR of the 14 segment medians is larger than the median\n    of the 14 within-segment IQRs; (b) the range of the 14 segment medians is larger than the\n    largest within-segment IQR. Reproduced when both readings hold, not reproduced when\n    neither holds; otherwise methods_underspecified. All 28 values are shown.\n- id: area-ratio-per-location\n  statement: The peak of the segmented area ratio distribution ranges from 0.6 to 11.43 across\n    the 14 locations, and in all but one location the ratio's variation along the vessel lies\n    within 30% of the peak, so variation between segments dominates.\n  source: Results, Area ratio, paragraph 2; Additional File 3 (Additional File 4 in the list)\n  quote: The peak of the area ratio distribution ranges from 0.6 to 11.43 across the different\n    locations. Although their area ratio varies along the length of each vessel, in all but one\n    case, this variation occurs within 30% of the peak\n  expected:\n  - quantity: smallest per-location peak of area ratio\n    value: 0.6\n    tolerance: 0.06\n  - quantity: largest per-location peak of area ratio\n    value: 11.43\n    tolerance: 1.143\n  - quantity: locations whose variation lies within 30% of the peak\n    value: 13\n    tolerance: 1.3\n  criterion: Pipeline P1 to P5 and P7, applied per location. Open, what \"variation within 30% of\n    the peak\" measures. Readings (a) the 25th and 75th percentiles both lie within 30% of the\n    peak value; (b) the IQR is at most 30% of the peak value; (c) the IQR is at most 60% of the\n    peak value (30% each side). Reproduced when, under one combination of readings, the two\n    peaks and the count are within tolerance.\n- id: fig5d-polynomial-closest-area-ratio\n  statement: Of the three fits, the polynomial fit matches the segmentation's area ratio most\n    closely in 73% of cross sections, the spline fit in 19% and the ellipse fit in 8%, and its\n    distribution matches the segmentation's best.\n  source: Results, Area ratio, paragraph 3; Figure 5D and 5E\n  quote: The distribution of the PVS-to-vessel area ratio in segmentations is matched most\n    closely by the polynomial fit ( Figure 5E ), and the value of the area ratio in segmentations\n    is matched most closely by the polynomial fit in 73% of cases ( Figure 5D ) ... the ellipse\n    fit gives the closest match in only 8% of cases ... The spline fit gives the closest match in\n    19% of the cases\n  expected:\n  - quantity: share of cross sections best matched by the polynomial fit\n    value: 73\n    tolerance: 7.3\n    unit: percent\n  - quantity: share best matched by the spline fit\n    value: 19\n    tolerance: 1.9\n    unit: percent\n  - quantity: share best matched by the ellipse fit\n    value: 8\n    tolerance: 0.8\n    unit: percent\n  criterion: Pipeline P1 to P6 and P9. Per cross section, the fit whose area ratio has the\n    smallest absolute difference from the segmentation's (Figure 5D, \"best predicted\"). Every\n    combination of the readings of P5, P6 and P9 (ellipse region) is run. Reproduced when, under\n    one combination, the three shares are within tolerance; partially reproduced when the\n    polynomial share is the largest and above 50% but the shares are not all within tolerance.\n- id: table2-fit-area-ratio-peaks\n  statement: The area ratio distribution peaks at 1.21 for the polynomial fit (close to the\n    segmentation's 1.12), 2.08 for the ellipse fit, which does not narrow at the ends, and 1.48\n    for the spline fit, whose ratio varies little because it scales with vessel size alone.\n  source: Results, Area ratio, paragraph 3; Table 2; Figure 5E\n  quote: The peak of the area ratio distribution for the polynomial fit is 1.21, similar to the\n    peak of the segmentation distribution of 1.12 ... has a significantly higher peak of 2.08\n    because it does not narrow at the ends. The spline fit gives the closest match in 19% of the\n    cases and has a peak of 1.48\n  expected:\n  - quantity: peak area ratio, polynomial fit\n    value: 1.21\n    tolerance: 0.121\n  - quantity: peak area ratio, ellipse fit\n    value: 2.08\n    tolerance: 0.208\n  - quantity: peak area ratio, spline fit\n    value: 1.48\n    tolerance: 0.148\n  - quantity: median area ratio, polynomial fit\n    value: 2.15\n    tolerance: 0.215\n  - quantity: median area ratio, ellipse fit\n    value: 2.89\n    tolerance: 0.289\n  - quantity: median area ratio, spline fit\n    value: 1.58\n    tolerance: 0.158\n  - quantity: IQR of area ratio, spline fit\n    value: 0.3\n    tolerance: 0.03\n  criterion: Pipeline P1 to P4, P6, P7 and P9, fit areas over pi R1^2. The paper reports no test\n    for \"significantly higher\". Reproduced when, under one combination of readings, all values\n    are within tolerance; partially reproduced when the order of the peaks (ellipse above\n    spline above polynomial) holds and the spline IQR is the smallest of the three.\n- id: fig6a-resistance-power-law\n  statement: The hydraulic resistance per unit length of the segmented PVS is well predicted by\n    a power law in PVS area (R2 = 0.944), with exponent -1.75 (95% CI -1.763 to -1.737), close\n    to the -2 of a shape scaled in size alone.\n  source: Results, Hydraulic Resistance, paragraph 2; Figure 6A\n  quote: The hydraulic resistance can be reasonably predicted with a power-law fit as a function\n    of the PVS area alone (R 2 = 0.944). The exponent in the power law fit is −1.75 (95%\n    confidence interval −1.763, −1.737)\n  statistics:\n  - about: power-law exponent of resistance on PVS area\n    test: power-law fit\n    ci:\n      level: 0.95\n      low: -1.763\n      high: -1.737\n    n: all segmented cross sections of the 14 segments\n  expected:\n  - quantity: power-law exponent\n    value: -1.75\n    tolerance: 0.013\n  - quantity: R2 of the power-law fit\n    value: 0.944\n    tolerance: 0.0944\n  criterion: Pipeline P1 to P4 and P8 on the segmented PVS, area from the segmentation (P5),\n    all retained cross sections pooled. The exponent tolerance is the half-width of the paper's\n    95% CI. Open, how the power law is fit. Readings (a) least squares of log resistance on log\n    area, R2 on the log scale; (b) nonlinear least squares of resistance on area, R2 on the\n    linear scale. Reproduced when, under one combination of readings, both values are within\n    tolerance; partially reproduced when the R2 is within tolerance and the exponent lies\n    between -2 and -1.5.\n- id: fig6b-resistance-segmentation-peak\n  statement: The distribution of segmented PVS hydraulic resistance per unit length over all\n    cross sections peaks at 1.73e15 Pa s/m^4, with a median of 3.84e15 Pa s/m^4.\n  source: Discussion, paragraph 4; Conclusion; Table 2; Figure 6B\n  quote: Here, we report the distribution of hydraulic resistances for thousands of PVS cross\n    sections, with its peak at 1.73×10 15 Pa· s/m 4\n  expected:\n  - quantity: peak of segmented resistance distribution\n    value: 1.73e+15\n    tolerance: 1.73e+14\n    unit: Pa s/m^4\n  - quantity: median segmented resistance (Table 2)\n    value: 3.84e+15\n    tolerance: 3.84e+14\n    unit: Pa s/m^4\n  criterion: Pipeline P1 to P4, P7 and P8. Open, beyond P7, whether the 20 bins are even on a\n    linear or a logarithmic scale of resistance (the paper says evenly spaced and the values\n    span two orders of magnitude). Readings (a) linear, (b) logarithmic. Reproduced when, under\n    one combination of readings, both values are within tolerance; partially reproduced when\n    the median is and the peak is not.\n- id: resistance-per-location\n  statement: Variation in resistance is much larger between locations than along each PVS; the\n    per-location peaks range from 3.23e14 to 1.98e16, and in 65% of vessels all the variation\n    lies within 37% of the peak.\n  source: Results, Hydraulic Resistance, paragraph 2; Figure 6B; Additional File 5\n  quote: it is evident that the variation between locations is much larger than that along the\n    PVS at each location. The peak of hydraulic resistance distributions ranges from 3.23×10 14\n    to 1.98×10 16 across different locations, whereas, in 65% of the vessels, all the variation\n    occurs within 37% of the peak of the distribution\n  expected:\n  - quantity: smallest per-location peak resistance\n    value: 3.23e+14\n    tolerance: 3.23e+13\n    unit: Pa s/m^4\n  - quantity: largest per-location peak resistance\n    value: 1.98e+16\n    tolerance: 1.98e+15\n    unit: Pa s/m^4\n  - quantity: share of locations whose variation lies within 37% of the peak\n    value: 65\n    tolerance: 6.5\n    unit: percent\n  criterion: Pipeline P1 to P4, P7 and P8, per location. Open, what \"all the variation\"\n    measures. Readings (a) the 25th and 75th percentiles lie within 37% of the peak; (b) all\n    non-outlier values (outliers as the Methods define them) lie within 37% of the peak; (c)\n    the IQR is at most 37% of the peak. Reproduced when, under one combination of readings,\n    the two peaks and the share are within tolerance.\n- id: fig5b-polynomial-closest-resistance\n  statement: The distribution of hydraulic resistance of the polynomial fit matches that of the\n    segmentation most closely, followed by the ellipse fit, and the polynomial fit is the best\n    match for the majority of cross sections; the distribution peaks are 1.44e15 (polynomial),\n    7.06e14 (ellipse), 1.07e16 (spline) and 1.32e15 (optimal annulus) Pa s/m^4.\n  source: Results, Hydraulic Resistance, paragraph 2; Figure 6B and 6C; Table 2. The Results\n    sentence cites Figure 5B, which is the resistance distribution of Figure 6B\n  quote: Figure 5B shows that the distribution of hydraulic resistances for the polynomial fit\n    matches that of the segmentation most closely, followed by the ellipse fit\n  expected:\n  - quantity: peak resistance, polynomial fit\n    value: 1.44e+15\n    tolerance: 1.44e+14\n    unit: Pa s/m^4\n  - quantity: peak resistance, ellipse fit\n    value: 7.06e+14\n    tolerance: 7.06e+13\n    unit: Pa s/m^4\n  - quantity: peak resistance, spline fit\n    value: 1.07e+16\n    tolerance: 1.07e+15\n    unit: Pa s/m^4\n  - quantity: peak resistance, optimal elliptical annulus\n    value: 1.32e+15\n    tolerance: 1.32e+14\n    unit: Pa s/m^4\n  criterion: Pipeline P1 to P9. The optimal annulus resistance from Equation 3 with the\n    segmentation's area ratio K and the fitted vessel radius R1; the printed equation is garbled\n    and is read, from Tithof et al. (reference 18) and its units, as R = mu 6.67 K^-1.96 / R1^4.\n    Per cross section the best match is the fit (ellipse, polynomial, spline) with the smallest\n    absolute difference in resistance from the segmentation (Figure 6C). Reproduced when, under\n    one combination of readings, the polynomial fit is the best match for more than half the\n    cross sections and the four peaks are within tolerance; partially reproduced when the\n    polynomial is the best match for the largest share but the peaks are not all within\n    tolerance.\n- id: ellipse-annulus-underestimate\n  statement: The resistance distribution of the optimal elliptical annulus is very similar to\n    that of the ellipse fit, and both tend to underestimate the resistance of the segmented PVS.\n  source: Results, Hydraulic Resistance, paragraph 3; Figure 6B\n  quote: The distribution of resistances for the optimal elliptical annulus is very similar to\n    that of the ellipse fit ... Though both the ellipse fit and annulus tend to underestimate\n    the resistance of the PVS\n  depends_on:\n  - fig5b-polynomial-closest-resistance\n  criterion: As in fig5b-polynomial-closest-resistance. \"Tend to underestimate\" is read as the\n    median of the per-cross-section ratio of fit (or annulus) resistance to segmented\n    resistance being below 1, for each of the two. \"Very similar\" has no measure in the paper;\n    readings (a) the two medians of resistance within 10% of each other, (b) the two peaks\n    within 10% of each other. Note the Optimal model section says the annulus is more similar\n    to the segmentation than the ellipse fit is, and Table 2 gives annulus and ellipse peaks of\n    1.32e15 and 7.06e14. Reproduced when both underestimate and either reading of similarity\n    holds; partially reproduced when only the underestimation holds.\n- id: spline-resistance-five-times\n  statement: The spline fit's resistance is considerably larger than the segmentation's, its\n    distribution peak about 5 times larger, despite a larger area ratio, because the spline PVS\n    narrows rapidly away from the vessel.\n  source: Results, Hydraulic Resistance, paragraph 3; Figure 6B inset\n  quote: The resistance for the spline fit is considerably larger than that of the segmentation\n    (distribution peak is 5 times larger)\n  expected:\n    quantity: ratio of spline peak resistance to segmentation peak resistance\n    value: 5\n    tolerance: 0.5\n  depends_on:\n  - fig6b-resistance-segmentation-peak\n  - fig5b-polynomial-closest-resistance\n  criterion: Peaks as in the claims it depends on. Table 2 gives 1.07e16 over 1.73e15, a ratio\n    of 6.2, which the text calls 5; readings (a) the text's 5 with 10% tolerance, (b) Table 2's\n    6.2 with 10% tolerance. Reproduced when the ratio is within tolerance under one reading and\n    the median spline resistance exceeds the median segmented resistance.\n- id: fig7-velocity-profiles\n  statement: In a representative cross section, the polynomial fit's velocity profile resembles\n    the segmentation's, the ellipse fit gives much higher velocities and the spline fit much\n    lower; these trends are generally consistent across cross sections.\n  source: Results, Hydraulic Resistance, paragraph 4; Figure 7 legend\n  quote: In this example case, the velocity profile for the polynomial fit is similar to the\n    velocity profile in the segmentation, whereas the ellipse fit results in much higher\n    velocities, and the spline fit results in much lower velocities.\n  criterion: Pipeline P1 to P9, velocity from the Poisson solution at a pressure gradient of\n    500 Pa/m (Methods). The representative cross section is not identified, so the claim is\n    tested over all cross sections, as the text's \"generally consistent in all cross sections\"\n    allows. Open, the velocity measure. Readings (a) maximum velocity, (b) mean velocity (flow\n    rate over area). Reproduced when, under one reading, in more than half the cross sections\n    the ellipse fit is faster than the segmentation, the spline fit slower, and the polynomial\n    fit closer to the segmentation than either.\n- id: vessel-radius-peak\n  statement: The fitted vessel radius distribution peaks at 28 um.\n  source: Discussion, paragraph 2; Figure 8A and 9C\n  quote: We approximated the cross-sectional shape of the vessel as a circle and found that the\n    peak of the vessel radius distribution is 28 μ m\n  expected:\n    quantity: peak of vessel radius R1\n    value: 28\n    tolerance: 2.8\n    unit: um\n  criterion: Pipeline P1 to P4, P6 and P7. Reproduced when, under one combination of readings,\n    the peak is within tolerance. Table 3 gives an R1 peak of 64.9 um, which disagrees; it is\n    not used (opening comment).\n- id: fig8-ellipse-parameters\n  statement: The ellipse fit shows an elongated, eccentric PVS with the vessel slightly below its\n    center; R1 peaks at 28 um and R3 at 35 um, R3/R1 at 0.80, R2/R1 at 2.89, R3/R2 at 0.398, the\n    vertical offset Ov at 0.24, and the horizontal offset Oh is centered near zero with a much\n    wider distribution than Ov.\n  source: Results, Characteristics of the typical PVS shape, paragraphs 2 to 5; Figure 8A, 8C,\n    8D, 8E and 8F\n  quote: the distribution of R 1 , the vessel radius, is similar to that of R 3 , the minor axis\n    length (distribution peaks at 28 μ m and 35 μ m, respectively, see Figure 8A ), and the ratio\n    between them ( R 3 / R 1 ) is generally close to 1 (distribution peaks at 0.80, Figure 8E )\n  expected:\n  - quantity: peak of R3\n    value: 35\n    tolerance: 3.5\n    unit: um\n  - quantity: peak of R3/R1\n    value: 0.8\n    tolerance: 0.08\n  - quantity: peak of R2/R1\n    value: 2.89\n    tolerance: 0.289\n  - quantity: peak of R3/R2\n    value: 0.398\n    tolerance: 0.0398\n  - quantity: peak of Ov\n    value: 0.24\n    tolerance: 0.024\n  depends_on:\n  - vessel-radius-peak\n  criterion: Pipeline P1 to P4, P6, P7 and P9 (ellipse). Open, the units of Ov and Oh, printed\n    without units. Readings (a) offsets over R1, (b) over R3, (c) in um. Ov positive when the\n    vessel is below the ellipse center, as the text reads it. Oh \"centered around zero\" and\n    \"much wider\" are read as the median of Oh within one Ov peak value of zero and the IQR of Oh\n    at least twice the IQR of Ov. Reproduced when, under one combination of readings, all\n    values are within tolerance and the Oh conditions hold; partially reproduced when the\n    ratios R3/R1, R2/R1 and R3/R2 are within tolerance and the rest is not.\n- id: fig9c-pvs-two-lobes\n  statement: The PVS usually consists of two mostly or entirely disconnected lobes on either side\n    of the vessel; the polynomial fit's HC (top of PVS above top of vessel) peaks at zero, and\n    when the lobes connect the channel is narrow, usually less than 0.5 R1.\n  source: Results, Characteristics of the typical PVS shape, paragraph 2; Figure 9C; Table 3\n  quote: The distribution peaks at zero ( Figure 9C ), suggesting that the top of the vessel is\n    most often very nearly aligned with the top of the PVS and that the PVS is often separated\n    into two lobes. Even when the two sides are connected, the channel connecting them is quite\n    narrow, usually less than 0.5 R 1 .\n  expected:\n    quantity: peak of HC/R1 (Table 3)\n    value: 0.000689\n    tolerance: 0.1\n  criterion: Pipeline P1 to P4, P6, P7 and P9 (polynomial). A 10% tolerance on a value near zero\n    is meaningless; the tolerance is one tenth of R1 (0.1 in HC/R1), the scale of the paper's\n    0.5 R1 statement; this is a choice and is recorded as a deviation. Reproduced when, under\n    one combination of readings, the peak of HC/R1 is within 0.1 of zero and, among cross\n    sections with HC greater than zero, more than half have HC below 0.5 R1.\n- id: fig9e-pvs-width-asymmetry\n  statement: The PVS is about twice as wide as the vessel radius and asymmetric about the vessel;\n    the short-side width WS/R1 peaks near 1.1, the long-side width WL/R1 near 1.9, and WS/WL near\n    0.5.\n  source: Results, Characteristics of the typical PVS shape, paragraphs 3 and 5; Figure 9E;\n    Table 3\n  quote: The short side is significantly shorter than the long side (distribution peaks of 1.1\n    and 1.9, respectively, Figure 9E ) and for the ratio between them, W S / W L , the\n    distribution peaks at approximately 0.5, indicating that the two PVS sides are typically\n    asymmetric\n  expected:\n  - quantity: peak of WS/R1 (Table 3)\n    value: 1.08\n    tolerance: 0.108\n  - quantity: peak of WL/R1 (Table 3)\n    value: 1.85\n    tolerance: 0.185\n  - quantity: peak of WS/WL (Table 3)\n    value: 0.502\n    tolerance: 0.0502\n  criterion: Pipeline P1 to P4, P6, P7 and P9 (polynomial). The Results also say WS/R1 peaks at\n    1.85, which Table 3 and the sentence quoted give for WL/R1; Table 3 is followed. The paper\n    reports no test for \"significantly shorter\", and WS is by definition no longer than WL.\n    Reproduced when, under one combination of readings, the three peaks are within tolerance.\n- id: left-right-no-difference\n  statement: The PVS widths on the left and right sides of the vessel do not differ\n    significantly.\n  source: Results, Characteristics of the typical PVS shape, paragraph 5\n  quote: Since there was no statistically significant difference between the left and right\n    sides, we report the distribution of the short ( W S ) and long ( W L ) sides of each cross\n    section.\n  criterion: A claim of absence whose test the paper does not name. Widths W of the polynomial\n    fit on each side (P9), left and right fixed by the direction along the centerline (P3).\n    Readings (a) Wilcoxon signed-rank test on paired left and right widths over all cross\n    sections, (b) two-sample Kolmogorov-Smirnov test of the two distributions, (c) Wilcoxon\n    signed-rank test on the per-segment median left and right widths (14 pairs); alpha 0.05.\n    Reproduced when no reading finds a difference, not reproduced when all do, otherwise\n    methods_underspecified. The median difference and its sign are shown for each.\n- id: fig9a-heights-taper\n  statement: The PVS is tallest next to the vessel and narrows far from it; the heights H1/R1,\n    H2/R1 and H3/R1 peak at 1.34, 0.792 and 0.307, so H1 is about 4 times H3.\n  source: Results, Characteristics of the typical PVS shape, paragraph 6; Figure 9A; Table 3\n  quote: the distributions of heights of the PVS, H 1 , H 2 , and H 3 , peak at 1.34, 0.792, and\n    0.307, respectively, indicating that the PVS is larger closer to the vessel and smaller at\n    the ends of the PVS. H 1 , the height of the PVS close to the vessel, is 4 times larger than\n    H 3\n  expected:\n  - quantity: peak of H1/R1\n    value: 1.34\n    tolerance: 0.134\n  - quantity: peak of H2/R1\n    value: 0.792\n    tolerance: 0.0792\n  - quantity: peak of H3/R1\n    value: 0.307\n    tolerance: 0.0307\n  criterion: Pipeline P1 to P4, P6, P7 and P9 (polynomial), heights per side; open, whether each\n    cross section contributes both sides or their mean. Readings (a) both sides pooled, (b)\n    mean of the two sides. Reproduced when, under one combination of readings, the three peaks\n    are within tolerance; partially reproduced when the order H1 above H2 above H3 holds for\n    the peaks and medians but the values are not within tolerance.\n- id: fig9f-pvs-concave\n  statement: The bottom edge of the PVS is most often concave; the distribution of (H2 - H3)/(H1\n    - H2) peaks at 0.108, below the value of 1 that separates concave from convex.\n  source: Results, Characteristics of the typical PVS shape, paragraph 7; Figure 9F\n  quote: The peak of the curvature distribution is 0.108, showing that the PVS is most often\n    concave, rather than convex, as is required by the ellipse fit.\n  expected:\n    quantity: peak of (H2 - H3)/(H1 - H2)\n    value: 0.108\n    tolerance: 0.0108\n  depends_on:\n  - fig9a-heights-taper\n  criterion: As fig9a-heights-taper, with the same readings. Reproduced when, under one\n    combination of readings, the peak is within tolerance and more than half the values are\n    below 1; partially reproduced when only the second holds.\n"
}
```

```
File created successfully at: claims/000491/10.21203-rs.3.rs-2587250-v1.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000491/10.21203-rs.3.rs-2587250-v1.yaml paper/10.21203-rs.3.rs-2587250-v1.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/000491 && grep -n -i "rather\|—" *.yaml; grep -n ": .*: " *.yaml | grep -v "^\S*#" | head
```

```
603:    concave, rather than convex, as is required by the ellipse fit.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000491/10.21203-rs.3.rs-2587250-v1.yaml",
 "old_string": "  quote: The peak of the curvature distribution is 0.108, showing that the PVS is most often\n    concave, rather than convex, as is required by the ellipse fit.",
 "new_string": "  quote: The peak of the curvature distribution is 0.108, showing that the PVS is most often\n    concave"
}
```

```
The file claims/000491/10.21203-rs.3.rs-2587250-v1.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  && python tools/claims_check.py claims/000491/10.21203-rs.3.rs-2587250-v1.yaml paper/10.21203-rs.3.rs-2587250-v1.txt && git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote the claims file `claims/000491/10.21203-rs.3.rs-2587250-v1.yaml`. The quote checker passes: 22 claims, 22 quotes, 4 statistical values, 0 problems. Nothing is committed.

**Text read.** I read the Research Square preprint, version 1, as served by PubMed Central (PMC9949243). It has the full Methods, Results, Discussion, figure legends and Tables 1 to 3. I did not read the version of record (Fluids and Barriers of the CNS, 2023). Additional Files 1 to 6 were not supplied:
- **Additional File 1** is the full description of the segmentation. The main Methods describe the approach, and the dandiset holds the final segmentations, so the claims start from those.
- **Additional Files 2 to 6** are figures. The per-location numbers the claims use are stated in the main text.

The paper links no code, so no repository was read and no detail is settled by code. The dandiset's description (14 datasets from 9 subjects, raw stacks plus final segmentations) maps its subjects to the paper's mice 1 to 9 and locations A to N. That mapping is in the opening comment.

**Claims.** All 22 are findings and all 22 have quotes; none is `inferred`.
- **Statistics:** 2 claims have them, both 95% confidence intervals: the slope of PVS area on vessel area (0.973 to 1.12), and the power-law exponent of resistance on area (−1.763 to −1.737). The paper reports no p-values.
- **Criteria:** all 22 have one, and 18 also have expected values.

**Details the paper leaves open, and the readings named.** The ones shared by many claims are written once, as steps P1 to P9 of a pipeline in the opening comment:
- **Isotropic voxel size:** 0.648 µm or 1 µm.
- **Centerline points removed by hand:** the longest skeleton path, or all skeleton points.
- **"Median PVS width" in the edge-exclusion rule:** the horizontal extent of the PVS segmentation, or the polynomial-fit width W.
- **Vessel area in the segmentation's area ratio:** the segmented vessel area, or the fitted circle's area.
- **Erosion of the convex hull in the circle fit:** 1, 3 or 5 pixels. The circle-fitting method is not named; I used a standard least-squares fit.
- **Range of the 20 bins for a distribution peak:** all values, or values after removing outliers. For resistance, also linear or logarithmic bins.
- **Ellipse-fit PVS region:** the ellipse minus its overlap with the circle, or ellipse area minus circle area.
- **Spline type** (cubic interpolating used as a standard choice), and **which pixels count as polynomial-fit edge points** (one reading given).
- **Slice orientation:** top toward the brain surface. This is my reading of the figures; the paper does not state it.
- **Per-claim details:**
  - Whether the area-on-area fit has an intercept.
  - Whether the power law is fit on log or linear scales.
  - What "within 30% / 37% of the peak" measures (three readings each).
  - What "much larger between segments" means (two readings).
  - The units of the offsets Ov and Oh (over R1, over R3, or µm).
  - Whether velocity means maximum or mean.
  - Which test showed no left/right width difference (three named tests).
  - Whether the heights pool both sides or average them.
  - What "very similar" means for the annulus and ellipse.
  - The representative cross section of Figure 7, which is not identified, so that claim is tested over all cross sections.
- **My own choice:** the tolerance on HC/R1, whose peak is near zero (0.1, the scale of the paper's 0.5 R1 statement). It is marked as a deviation.

**Problems in the paper itself.**
- **Table 2:** the 25th and 75th percentiles and IQRs of resistance are garbled in the text (the 75th percentile is printed below the median), and no PDF was supplied to check them. They are not used.
- **Table 3:** its dimensional values (R1 peak 64.9 µm) conflict with the 28 µm vessel radius peak given in the Results and Discussion. Only its ratios are used.
- **Width ratios:** one Results sentence says WS/R1 peaks at 1.85, but Table 3 gives that value for WL/R1. Table 3 is followed.
- **Spline resistance:** the text says the spline peak is 5 times the segmentation's, while Table 2 gives a ratio of 6.2. Both are named as readings.
- **Annulus formula (Equation 3):** garbled in the text. It is read from the cited Tithof et al. paper and the units.
- **Units:** the abstract gives resistance in Pa·s/m⁵, the tables in Pa·s/m⁴. The claims use m⁴.

**Missing data.** The segmentation-validation claim (at least 70% overlap with the 2D time-averaged images) needs the 2D images and their segmentations. The dataset description does not mention them, and the paper does not give the alignment method (it cites reference 31).

## End of run

21 turns, 4 minutes, result: success.
