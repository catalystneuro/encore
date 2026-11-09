# 002035 · claims · run 42442511828

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls claims/001453 claims/002035 paper 2>&1
```

```
Exit code 2
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
56:### 2. Read the paper's code
66:### 3. Write the claims file
151:### 4. Data from outside the paper's own recordings
159:### 5. Check
172:### 6. Answer questions
185:## Author
201:### 1. Establish what can be tested
328:### 2. Check the data against its description
343:### 3. Write the entry
401:### 4. Lock, check and run
412:### 5. Record the attempt
463:### 6. Hand over for verification
501:## Repeat attempts
543:## Local and remote datasets
566:## Verifier
570:### Round 1: without the author's conclusions
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 185
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10	
11	An attempt has three roles, each a separate run with a separate context:
12	
13	- The **reader** reads the paper and writes the claims file: every finding,
14	  and how each is to be tested, taken from the paper. A second reader checks
15	  it against the paper. Readers never see the dataset's data.
16	- The **author** tests the claims on the dataset. It reads the paper to
17	  understand the claims, but the claims file binds it: it cannot change a
18	  claim's statement, expected values or criterion. A method detail the file
19	  lacks it takes from the paper, citing the passage, and it asks a reader
20	  only when it believes the file misreads the paper.
[... 165 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
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
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; head -30 paper/*.txt; ls paper; ls claims | head; grep -rl "002035" --include=*.yaml . | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat papers/match/002035.yaml; grep -n -B2 -A10 "002035" papers/manifest.yaml
```

```
# Whether each paper DANDI:002035 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: dandi
  id: '002035'
date: '2026-11-06'
papers:
- doi: 10.3233/jad-220538
  relation: IsDescribedBy
  checks:
    text: true
    title_in_text: true
    names_this: false
    names_others: []
  verdict: primary
  by: checks
  reason: The archive says the paper describes the dataset, and the paper names no dataset.
2351-    pdf: false
2352-    supplements: 0
2353:  '002035':
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.3233-jad-220538.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "=== page\|^Table\|^Fig\|Figure" paper/*.txt | sed -n '1,200p' | awk -F: '$1>620'
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3233-jad-220538.txt",
 "offset": 806,
 "limit": 482
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "github\|gitlab\|zenodo\|dandi\|data availab\|code" paper/*.txt | head; ls tools | head -50; grep -rn "002035" --include=*.json --include=*.yaml --include=*.md . 2>/dev/null | grep -v "^./papers/match\|transcripts" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 8260,8300p targets/dandisets.json; sed -n 1,60p tools/claims_check.py
```

```
"relation": "IsDescribedBy",
     "resource_type": "Preprint",
     "preprint": true
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "002035",
   "name": "Amyloid Pathology in the Central Auditory Pathway of 5XFAD Mice Appears First in Auditory Cortex",
   "published_version": "0.261022.1829",
   "asset_count": 24858,
   "size_gb": 23.07,
   "data_standards": [
    "Brain Imaging Data Structure (BIDS)"
   ],
   "species": [],
   "approaches": [],
   "papers": [
    {
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims/002037 2>/dev/null; python -c "
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
cd  python -c "
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

The paper text is complete (author manuscript, Methods present, no supplement, no linked code). Let me look at the Fig. 1 page to see what panel C plots.

**Agent calls Bash**

```bash
cd  python -c "
import fitz;d=fitz.open('paper/10.3233-jad-220538.pdf');print(len(d))
for i in [16,18,19,21,22,23,25]:
  d[i].get_pixmap(dpi=110).save('$TMPDIR/p%d.png'%(i+1))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftoppm; pdftoppm -r 80 -png -f 17 -l 26 paper/10.3233-jad-220538.pdf $TMPDIR/pg && ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3233-jad-220538.pdf",
 "pages": "17-18"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python -m pip install --target $TMPDIR/pm pymupdf -q 2>&1 | tail -2; ls $TMPDIR/pm | head
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
_yaml
bin
fitz
flatbuffers
flatbuffers-25.12.19.dist-info
google
networkx
networkx-3.7.dist-info
numpy
numpy-2.5.4.dist-info
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  PYTHONPATH=$TMPDIR/pm python -c "
import fitz;d=fitz.open('paper/10.3233-jad-220538.pdf');print(len(d))
for i in range(16,27):
  t=d[i].get_text()[:60].replace(chr(10),' ');print(i+1,t, len(d[i].get_images()))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  PYTHONPATH=$TMPDIR/pm python -W ignore -c "
import pymupdf as fitz;d=fitz.open('paper/10.3233-jad-220538.pdf')
for i in [16,18,19,21,22,23,25]:
  d[i].get_pixmap(dpi=130).save('$TMPDIR/p%d.png'%(i+1))
"; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p17.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p19.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p20.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p22.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p23.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p24.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p26.png"
}
```

Result: no output.

**Agent**

Fig. 1C is labelled "all layers", and Fig. 5C is labelled "all ages" while the text says p90-p150. No code is linked, and the paper has no supplement. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/002035/10.3233-jad-220538.yaml",
 "content": "# Claims for Weible & Wehr (2022), J Alzheimers Dis 89(4) 1385-1402, on dandiset 002035.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-08,\n# protocol pilot-13 as stated in docs/protocol.md.\n#\n# Text read: the author manuscript in PubMed Central (NIHMS1886685, PMC10097438), main text,\n# Methods, figure legends and Tables 1 to 6, from paper/10.3233-jad-220538.txt. The figure\n# panels of Figs. 1 to 7 were looked at in the PDF for their axis labels only. The version of\n# record was not read. The paper has no supplement and links no code or data, so no code was read.\n#\n# The data the paper used (Methods, Mice, Sectioning, Immunohistochemistry, Imaging). 5XFAD\n# heterozygous mice (n = 61) and wild-type littermates (n = 25) on a C57BL6/SJL background, at\n# ages p14, p21, p30, p45, p60, p90, p120 and p150; 4 male and 4 female 5XFAD mice per age from\n# p21 to p150, 3 male and 2 female at p14. (The Methods also give 31 females and 30 males, which\n# the per-age numbers do not add up to; 30 females and 31 males would.) Six 30 um coronal sections\n# per brain, 516 sections in all, labelled with anti-Abeta42 (Alexa 488, green) and DAPI (blue),\n# imaged on a Zeiss Imager A.2 at 12.5X to 50X for atlas alignment, 200X for Abeta42 cells and\n# plaques, 100X for DAPI cells, at several focal depths. Regions: primary auditory cortex (A1,\n# eight laminar bins), subiculum, medial geniculate body (MGd, MGv, MGm), inferior colliculus\n# (eIC, dIC, cIC), superior olivary complex (lateral, medial, periolivary), nucleus of the lateral\n# lemniscus, cochlear nuclei, and the caudal pontine reticular nucleus (PRNc). A1, subiculum and\n# MGB were counted in the same coronal section. Measured variables per mouse and region: the\n# number of Abeta42+ cells over the number of DAPI cells (%Abeta42+ cells), plaques per mm2, and\n# DAPI cells per mm2. The dandiset's title is the paper's title and it is a BIDS microscopy\n# dataset, so it is taken to hold these section images.\n#\n# Methods fixed by the paper (Methods, Imaging, boundary determination, and quantification;\n# Statistical analysis), used by every criterion below unless the claim says otherwise.\n#  - Cells and plaques were counted by hand in Canvas X, blind to genotype, sex, age and\n#    boundaries. A labelled cell has a well-defined membrane with processes and/or distinct\n#    nuclear and cytoplasmic compartments, and is distinct from the autofluorescence of control\n#    sections. Dense-core and diffuse plaques are counted together as plaques. Cell types are\n#    not told apart. Any automated detection used in place of counting by eye is a deviation.\n#  - Boundaries and subregions come from an affine alignment of each section to the Allen CCFv3\n#    on DAPI and antibody landmarks. A1 layers by depth from the pia as fractions of cortical\n#    thickness, L1, L2, L3, L4 12.5% each, L5 and L6 25% each, each split into A and B halves, so\n#    eight bins of 12.5%. Areas from a stage-micrometer calibration.\n#  - One value per mouse per region (or per layer or subregion). Non-parametric tests,\n#    Kruskal-Wallis across ages, layers or subregions, Mann-Whitney for post hoc pairs and for\n#    sex, Bonferroni correction where stated, alpha 0.05 (Tables 1 to 6).\n#  - PRNc (Results, Caudal pontine reticular nucleus) counted in an 800 um diameter circle centred\n#    on the region of highest apparent label density in ventrolateral PRNc; Abeta42+ cells over\n#    40 um in diameter taken as putative giant reticulospinal neurons (RSNs).\n#\n# Details the paper leaves open, with the readings it allows (each claim's criterion repeats\n# those that bear on it).\n#  - How DAPI cells were counted in ImageJ. Readings (a) automatic threshold, watershed and\n#    particle count; (b) counting by hand with a point tool. Either is a standard choice.\n#  - How a mouse's value is formed from several images, fields or hemispheres. Readings (a) counts\n#    and areas summed over all images of the region in that mouse, then the ratio; (b) the mean\n#    of per-image values. Which hemisphere, or both, is not said.\n#  - Whether the whole region was imaged at 200X or sampled fields were. Readings (a) the whole\n#    region; (b) the fields available in the dataset for that region.\n#  - Effect sizes are eta-squared computed as in the paper's reference [24] (Lenhard), which is\n#    not given as a formula. The reported values agree with eta2 = (H - k + 1)/(n - k) for\n#    Kruskal-Wallis and eta2 = z2/N for Mann-Whitney, with n near 61 mice for the age tests in\n#    A1, subiculum, MGB, IC and SOC, about 38 mice for PRNc, and 24 mice (p90, p120, p150) for\n#    the p90-p150 tests. This is a reading of the reported numbers, not a statement of the paper.\n#  - The figure numbers in Tables 1 and 2 are off by one panel or one figure (Table 1 \"Cells X\n#    Age (Fig. 1B)\" is Fig. 1C; Table 2 cites Fig. 2B and 2C for the subiculum, Fig. 3B and 3C).\n#    The sources below cite the panels by their content.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"002035\"\npaper: doi:10.3233/jad-220538\nclaims:\n- id: a1-first-in-pathway\n  statement: In 5XFAD mice amyloid pathology in the central auditory pathway appears first in A1,\n    as intracellular Abeta42 in layer 5 neurons by p21, before any label in MGB, IC, SOC, nLL or\n    CN.\n  source: Results, Primary auditory cortex, paragraph 1; Discussion, paragraph 1; Figure 1A\n  quote: Amyloid pathology in the central auditory pathway of Aβ42+ mice appeared first in A1\n  criterion: For each auditory region (A1, MGB, IC, SOC, nLL, CN), the youngest age at which any\n    5XFAD mouse shows an Abeta42+ cell or a plaque, counted as in the opening comment. The paper\n    gives A1 cells at p21 (one cell at p14), IC cells at p30, MGB, IC and A1 plaques at p90, and\n    no age for SOC cells. \"Appeared first\" can be read as (a) the first age with label in any\n    mouse, or (b) the first age with label in most mice of that age. Reproduced when, under one\n    reading, A1 is the earliest region and no other auditory region shows label at an age\n    earlier than A1.\n- id: fig1a-a1-onset-p21\n  statement: At p14 only a single Abeta42+ neuron was seen in A1, in one of five 5XFAD mice; by\n    p21 Abeta42+ neurons were present consistently across mice.\n  source: Results, Primary auditory cortex, paragraph 1; Figure 1A legend\n  quote: At p14, we saw intracellular accumulation of Aβ42 in only a single neuron from one of\n    five 5XFAD+mice examined. By p21, we observed Aβ42+ neurons consistently across mice\n  expected:\n  - quantity: Abeta42+ A1 neurons counted over all p14 5XFAD mice\n    value: 1\n    tolerance: 0.1\n  - quantity: p14 5XFAD mice with any Abeta42+ A1 neuron\n    value: 1\n    tolerance: 0.1\n  criterion: Counts of Abeta42+ cells in A1 by the criteria of the Methods. \"Consistently across\n    mice\" at p21 is read as (a) in every p21 5XFAD mouse, or (b) in most of them (at least 5 of\n    8). Reproduced when the p14 counts match and the p21 condition holds under one reading.\n    Partially reproduced when the p21 condition holds but p14 shows more than one labelled cell\n    or labelled cells in more than one mouse.\n- id: fig1c-a1-cells-age\n  statement: The proportion of Abeta42+ cells in A1, over all layers, varies with age, rising from\n    p21.\n  source: Results, Primary auditory cortex, paragraph 1; Figure 1C (all layers); Table 1, Cells X\n    Age\n  quote: By p21, we observed Aβ42+ neurons consistently across mice, and in numbers that increased\n    with age (Fig. 1C, Table 1)\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: chi2 = 39.7, df = 7, eta2 = 0.62\n    p: 0.0001\n    p_relation: \"<\"\n    n: 5XFAD mice at 8 ages, one value per mouse\n  criterion: Per 5XFAD mouse, Abeta42+ cells over DAPI cells in A1 summed over the eight laminar\n    bins (Fig. 1C is labelled all layers), Kruskal-Wallis across the eight ages (Methods,\n    Statistical analysis). Reproduced when p < 0.05 and the age means rise from p14 to p90.\n- id: fig1d-a1-cells-layer-5a\n  statement: Abeta42+ cells in A1 are restricted predominantly to layer 5A, with a smaller and\n    growing number in layer 5B.\n  source: Results, Primary auditory cortex, paragraph 1; Figure 1D and 1E; Table 1, Cells X Layer\n  quote: Antibody labelling of cortical neurons was restricted predominantly to layer 5A (Fig. 1D,\n    Table 1), though an increasing number of Aβ42+ neurons were also observed in layer 5B as mice\n    aged (Fig. 1E)\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: chi2 = 353.4, df = 7, eta2 = 0.72\n    p: 0.0001\n    p_relation: \"<\"\n    n: 5XFAD mice, one value per mouse and layer, all ages\n  criterion: Per mouse and laminar bin, Abeta42+ cells over DAPI cells, all ages pooled (Fig. 1D\n    is labelled all ages); Kruskal-Wallis across the eight bins. Reproduced when p < 0.05, L5A\n    has the highest mean, L5B the second, and the other six bins together hold less than the\n    L5B mean.\n- id: fig1e-l5a-peak\n  statement: The density of Abeta42+ neurons in L5A peaks at 10.7% at p90 and declines slightly to\n    9.2% at p150; Abeta42+ cells in L5B appear consistently by p30.\n  source: Results, Primary auditory cortex, paragraph 1; Figure 1E\n  quote: Peak density of Aβ42+ neurons in layer 5A was 10.7% at p90, declining slightly to 9.2% at\n    p150\n  expected:\n  - quantity: mean %Abeta42+ cells in L5A at p90\n    value: 10.7\n    tolerance: 1.07\n    unit: \"%\"\n  - quantity: mean %Abeta42+ cells in L5A at p150\n    value: 9.2\n    tolerance: 0.92\n    unit: \"%\"\n  criterion: Per mouse, Abeta42+ cells over DAPI cells in the L5A bin; mean over the mice of each\n    age (Fig. 1E plots mean and S.E.). Reproduced when both values are within tolerance, p90 has\n    the highest L5A mean of the eight ages, and Abeta42+ L5B cells are present in most p30 mice\n    (Fig. 1E legend). Partially reproduced when p90 is the peak but a value is outside tolerance.\n- id: fig1f-l5a-dapi-stable\n  statement: The density of DAPI-labelled cells in L5A does not change with age.\n  source: Results, Primary auditory cortex, paragraph 1; Figure 1F\n  quote: the proportion of DAPI-labelled cells in L5A did not vary as a function of age (Fig. 1F)\n  criterion: A claim of absence. Per 5XFAD mouse, DAPI cells per mm2 in the L5A bin (Fig. 1F axis);\n    Kruskal-Wallis across the eight ages at alpha 0.05, the test the Methods name for comparisons\n    across ages (no statistic is reported for this panel). Reproduced when p >= 0.05; the range\n    of age means is reported either way.\n- id: fig1g-dapi-layers\n  statement: DAPI cell density in A1 varies across layers, with L5A and L5B lower than the other\n    layers except layer 1.\n  source: Results, Primary auditory cortex, paragraph 1; Figure 1G; Table 1, DAPI X Layer\n  quote: The density of DAPI-labelled cells varied as a function of layer (Fig. 1G, Table 1), with\n    densities in L5A and L5B significantly lower than all other layers except for layer 1\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: chi2 = 107.6, df = 7, eta2 = 0.30\n    p: 0.0001\n    p_relation: \"<\"\n  - about: L5A and L5B against each other layer\n    test: Mann-Whitney\n    p: 0.007\n    p_relation: \"<\"\n    corrected: Bonferroni\n  criterion: Per mouse and bin, DAPI cells per mm2, all ages pooled; Kruskal-Wallis across the\n    eight bins, then Mann-Whitney of L5A and of L5B against each other bin at p < 0.007 (the\n    threshold the Results give). Which layers L5A and L5B must be lower than is read as (a) the\n    Results, L2, L3, L4, L6A and L6B, or (b) the Figure 1G legend, L2, L3, L4 and L6B.\n    Reproduced when the Kruskal-Wallis has p < 0.05 and the pairs of one reading are all\n    significant with L5A and L5B lower. The sample is open; the reported eta2 implies about 340\n    mouse-by-layer values, fewer than 61 mice times 8, so (a) all 5XFAD mice and (b) the mice\n    with DAPI counts in every bin are both run.\n- id: fig2b-a1-plaques-age\n  statement: Plaques in A1 first appear at p90 and their density increases with age, to 92.9 ±\n    12.9 plaques/mm2 at p150.\n  source: Results, Primary auditory cortex, paragraph 2; Figure 2B; Table 1, Plaques X Age\n  quote: The first sign of aggregation of Aβ42 into extracellular plaques occurred at p90, and\n    plaque density then increased with age, reaching a mean at p150 of 92.9 ± 12.9 S.E.\n    plaques/mm2 (Fig. 2B, Table 1)\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: chi2 = 49.8, df = 7, eta2 = 0.81\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n    quantity: mean A1 plaque density at p150\n    value: 92.9\n    tolerance: 12.9\n    unit: plaques/mm2\n  criterion: Per 5XFAD mouse, plaques over the area of A1, all layers (Fig. 2B is labelled all\n    layers); Kruskal-Wallis across the eight ages. Reproduced when p < 0.05, no plaques are found\n    before p90, the p150 mean is within tolerance (the paper's S.E.) and the means rise from p90\n    to p150.\n- id: fig2c-a1-plaques-layer\n  statement: From p90 to p150 A1 plaque density varies by layer; layer 1 has more than double the\n    mean density of layers 2 to 4 (17 against 8.0 plaques/mm2), and layer 6A the highest (146.7\n    plaques/mm2).\n  source: Results, Primary auditory cortex, paragraph 2; Figure 2C; Table 1, Plaques X Layer\n  quote: Between p90 and p150, plaque density varied by layer (Fig. 2C; Table 1). The density in\n    layer 1 was more than double the mean density across layers 2–4 (17 ± 5.9 versus 8.0 ± 1.8\n    S.E. plaques/mm2, respectively; Fig. 2C) and was greatest in layer 6A (146.7 ± 24.4 S.E.\n    plaques/mm2)\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: chi2 = 76.0, df = 7, eta2 = 0.39\n    p: 0.0001\n    p_relation: \"<\"\n    n: 5XFAD mice aged p90, p120 and p150, one value per mouse and layer\n  expected:\n  - quantity: mean L1 plaque density, p90 to p150\n    value: 17\n    tolerance: 5.9\n    unit: plaques/mm2\n  - quantity: mean plaque density over layers 2 to 4, p90 to p150\n    value: 8.0\n    tolerance: 1.8\n    unit: plaques/mm2\n  - quantity: mean L6A plaque density, p90 to p150\n    value: 146.7\n    tolerance: 24.4\n    unit: plaques/mm2\n  criterion: Per mouse aged p90, p120 or p150 and per bin, plaques per mm2; Kruskal-Wallis across\n    the eight bins. The mean over layers 2 to 4 is read as (a) each mouse's mean of its three\n    bins, averaged over mice, or (b) plaques over area of the three bins together per mouse,\n    averaged over mice. Reproduced when p < 0.05, L6A has the highest mean, L1 exceeds twice\n    the layer 2 to 4 mean, and the three values are within tolerance (the paper's S.E.) under\n    one reading.\n- id: fig2d-a1-plaques-sex\n  statement: From p90 to p150, A1 plaque density is higher in females than in males, most robustly\n    in L6A, though no single layer differs after correction for multiple comparisons.\n  source: Results, Primary auditory cortex, paragraph 2; Figure 2D; Table 1, Plaques X Sex\n  quote: During this same period (p90-p150), plaque density in females significantly exceeded that\n    seen in males (Table 1), a difference that was most robust in L6A (Fig. 2D, Table 1), though\n    no difference by layer reached significance when correcting for multiple comparisons\n  statistics:\n  - about: females against males, all layers\n    test: Mann-Whitney\n    statistic: eta2 = 0.16\n    p: 0.05\n    p_relation: \"<\"\n  - about: females against males, layer 6A\n    test: Mann-Whitney\n    statistic: eta2 = 0.23\n    p: 0.02\n  criterion: 5XFAD mice aged p90, p120 and p150. The all-layer test is read as (a) one value per\n    mouse, plaques over A1 area (the reported eta2 fits about 24 values), or (b) one value per\n    mouse and layer. Mann-Whitney of females against males at p < 0.05, and per bin at the\n    Bonferroni threshold 0.006 the Results give. Reproduced when the all-layer test is\n    significant with females higher under one reading, L6A has the smallest per-layer p, and no\n    bin reaches p < 0.006. Partially reproduced when the all-layer test holds and a bin passes\n    0.006 or another bin has the smallest p.\n- id: wt-no-label\n  statement: Wild-type control mice show no intracellular or extracellular Abeta42 label in any\n    region at any age.\n  source: Results, Primary auditory cortex, paragraphs 1 and 2; Subiculum; Medial geniculate body;\n    Inferior colliculus; Superior olivary complex, nucleus of the lateral lemniscus, and cochlear\n    nuclei; Caudal pontine reticular nucleus\n  quote: We saw no evidence of ... intracellular antibody label in control mice ... We saw no\n    evidence of extracellular antibody label in control mice at any age\n  criterion: Counts of Abeta42+ cells and plaques, by the Methods' criteria, in every region of\n    every wild-type section. Reproduced when none is found; the number of sections and any\n    labelled sites are reported. Label that is autofluorescence by the Methods' definition does\n    not count.\n- id: fig3a-subiculum-onset\n  statement: In the subiculum Abeta42+ cells are present by p14, in every p14 mouse, and plaques by\n    p60, earlier than anywhere in the central auditory pathway.\n  source: Results, Subiculum, paragraph 1; Figure 3A legend\n  quote: In the subiculum, Aβ42+ cells were present by p14 and extracellular plaques by p60 (Fig.\n    3A)\n  criterion: Counts in the subiculum (CCFv3 boundary, prosubiculum included as the paper does) of\n    each 5XFAD mouse. Reproduced when every p14 mouse has Abeta42+ cells (Figure 3A legend, \"in\n    each p14 mouse\"), plaques are absent before p60 and present at p60 in at least one mouse.\n- id: fig3bc-subiculum-cells-plaques-age\n  statement: In the subiculum the proportion of Abeta42+ cells changes with age, peaking at p30\n    and dropping steeply between p60 and p90 as plaque density rises sharply.\n  source: Results, Subiculum, paragraph 1; Figure 3B and 3C; Table 2\n  quote: the density of Aβ42+ cells in subiculum changed over time (Fig. 3B, Table 2), reaching a\n    peak at p30, then dropping steeply between p60 and p90. This drop coincides with a\n    significant increase in plaque density (Fig. 3C, Table 2)\n  statistics:\n  - about: Abeta42+ cells across ages\n    test: Kruskal-Wallis\n    statistic: chi2 = 51.4, df = 7, eta2 = 0.84\n    p: 0.0001\n    p_relation: \"<\"\n  - about: plaques across ages\n    test: Kruskal-Wallis\n    statistic: chi2 = 55.2, df = 7, eta2 = 0.91\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: Per 5XFAD mouse, subiculum Abeta42+ cells over DAPI cells, and plaques per mm2;\n    Kruskal-Wallis across ages for each. Reproduced when both are significant at p < 0.05, the\n    cell mean peaks at p30, the drop from p60 to p90 is the largest fall between adjacent ages,\n    and plaque density rises from p60 to p90.\n- id: fig3d-subiculum-dapi-stable\n  statement: DAPI cell density in the subiculum does not vary with age.\n  source: Results, Subiculum, paragraph 1; Figure 3D\n  quote: Importantly, the density of DAPI-labelled cells did not vary as a function of age (Fig. 3D)\n  criterion: A claim of absence. Per 5XFAD mouse, DAPI cells per mm2 in the subiculum;\n    Kruskal-Wallis across the eight ages at alpha 0.05 (Methods; no statistic reported).\n    Reproduced when p >= 0.05; the range of age means is reported either way.\n- id: subiculum-no-sex\n  statement: The subiculum shows no sex differences in pathology.\n  source: Results, Subiculum, paragraph 1\n  quote: We observed no sex-linked differences\n  criterion: A claim of absence. Mann-Whitney of females against males (Methods) at alpha 0.05, for\n    %Abeta42+ cells and for plaque density. Which mice is not said; readings (a) all 5XFAD mice,\n    (b) the ages where the measure is non-zero (cells from p14, plaques from p60). Reproduced\n    when no test is significant; not reproduced when one is, under the reading that matches the\n    paper's practice elsewhere (b, as in A1 p90 to p150); both are reported.\n- id: mgb-cells-rare\n  statement: Intracellular Abeta42 in the MGB was seen in only 5 of 61 5XFAD mice, with at most 1\n    or 2 putative Abeta42+ cells in any one mouse.\n  source: Results, Medial geniculate body, paragraph 1\n  quote: Intracellular labelling of Aβ42 ... was observed in only 5 of 61 mice, with no more than\n    1-2 putative Aβ42+ cells seen in any one mouse\n  expected:\n  - quantity: 5XFAD mice with any Abeta42+ MGB cell\n    value: 5\n    tolerance: 0.5\n  - quantity: largest number of Abeta42+ MGB cells in one mouse\n    value: 2\n    tolerance: 0.2\n  criterion: Counts of Abeta42+ cells in the MGB (MGd, MGv, MGm) of each 5XFAD mouse.\n    Reproduced when the counts match. Partially reproduced when no more than 10 of 61 mice have\n    labelled cells and none has more than 2.\n- id: mgb-dapi-subregions\n  statement: The MGB holds on average 1300 DAPI-labelled cells, and cell density is higher in MGv\n    than in MGd and MGm.\n  source: Results, Medial geniculate body, paragraph 1; Table 3, DAPI X Subregion\n  quote: The MGB on average included 1300 ± 34 S.E. DAPI-labelled cells, with cell density in the\n    ventral MGB exceeding that of the dorsal and medial subregions\n  statistics:\n  - about: DAPI density across MGd, MGv and MGm\n    test: Kruskal-Wallis\n    statistic: chi2 = 13.6, df = 2, eta2 = 0.17\n    p: 0.001\n  - about: MGd against MGv\n    test: Mann-Whitney\n    statistic: eta2 = 0.15\n    p: 0.008\n    corrected: Bonferroni, threshold 0.017\n  - about: MGv against MGm\n    test: Mann-Whitney\n    statistic: eta2 = 0.26\n    p: 0.0004\n    corrected: Bonferroni, threshold 0.017\n  expected:\n    quantity: mean number of DAPI cells in the MGB per mouse\n    value: 1300\n    tolerance: 34\n  criterion: Per 5XFAD mouse, DAPI cells in the MGB of its section, and DAPI cells per mm2 per\n    subregion; Kruskal-Wallis across subregions and Mann-Whitney pairs at 0.017 (Table 3).\n    Which mice enter the subregion test is open; the reported eta2 fits about 24 mice, so (a)\n    all 5XFAD mice and (b) those aged p90 to p150 are both run. The count is per mouse as read\n    from the text; tolerance is the paper's S.E. Reproduced when the mean count is within\n    tolerance and, under one reading, MGv is significantly denser than MGd and MGm. Partially\n    reproduced when only the subregion result holds.\n- id: fig4b-mgb-plaques-age\n  statement: MGB plaques first appear at p90 (50.4 plaques/mm2) and increase with age to 180.4\n    plaques/mm2 at p150.\n  source: Results, Medial geniculate body, paragraph 1; Figure 4B; Table 3, Plaques X Age;\n    Discussion, paragraph 3\n  quote: Plaques were first observed at p90, and plaque density increased significantly with age,\n    reaching a mean of 180.4 ± 23.7 S.E. plaques/mm2 by p150 (Fig. 4B, Table 3)\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: chi2 = 53.8, df = 7, eta2 = 0.88\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: mean MGB plaque density at p150\n    value: 180.4\n    tolerance: 23.7\n    unit: plaques/mm2\n  - quantity: mean MGB plaque density at p90 (Discussion, paragraph 3)\n    value: 50.4\n    tolerance: 17.8\n    unit: plaques/mm2\n  criterion: Per 5XFAD mouse, plaques over the area of MGd, MGv and MGm together; Kruskal-Wallis\n    across ages. Reproduced when p < 0.05, no plaques are found before p90, and both means are\n    within tolerance (the paper's S.E.).\n- id: fig4c-mgb-plaques-subregion\n  statement: From p90 to p150 MGB plaque density differs among subregions, with MGd and MGv higher\n    than MGm, but no pair differs after Bonferroni correction.\n  source: Results, Medial geniculate body, paragraph 1; Figure 4C legend; Table 3, Plaques X\n    Subregions\n  quote: Within this timeframe (p90-p150), density varied significantly among subregions (Fig. 4C,\n    Table 3). However, no difference between pairs of subregions reached significance when\n    correcting for multiple comparisons\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: chi2 = 6.1, df = 2, eta2 = 0.06\n    p: 0.05\n    p_relation: \"<\"\n  - about: MGd against MGm\n    test: Mann-Whitney\n    statistic: eta2 = 0.094\n    p: 0.03\n    corrected: Bonferroni, threshold 0.016, not significant\n  - about: MGv against MGm\n    test: Mann-Whitney\n    statistic: eta2 = 0.092\n    p: 0.03\n    corrected: Bonferroni, threshold 0.016, not significant\n  criterion: Per mouse aged p90, p120 or p150 and per subregion, plaques per mm2; Kruskal-Wallis\n    across MGd, MGv and MGm at 0.05, then Mann-Whitney pairs at 0.016 (Results). Reproduced when\n    the Kruskal-Wallis is significant, MGd and MGv means exceed MGm, and no pair passes 0.016.\n    Partially reproduced when the ordering holds and the Kruskal-Wallis is not significant, or\n    a pair passes 0.016.\n- id: mgb-sex-trend\n  statement: No sex difference in MGB plaque load reaches significance, with a trend toward more\n    plaques in females.\n  source: Results, Medial geniculate body, paragraph 1\n  quote: No sex-linked differences reached significance, though we observed a trend toward a\n    higher plaque load in females (p = 0.07, η2 = 0.13, M-W)\n  statistics:\n  - test: Mann-Whitney\n    statistic: eta2 = 0.13\n    p: 0.07\n  criterion: A claim of absence. Mann-Whitney of females against males on per-mouse MGB plaque\n    density, mice aged p90 to p150 (the timeframe of the paragraph; the reported eta2 fits\n    about 24 mice), at alpha 0.05. Reproduced when p >= 0.05; the female and male means and the\n    p-value are reported either way.\n- id: ic-cells-low\n  statement: Abeta42+ cells in the IC are very few, never above 0.5% of DAPI cells at any age, but\n    vary with age, first appearing at p30 and roughly doubling between p90 and p150.\n  source: Results, Inferior colliculus, paragraph 1; Figure 5 legend; Table 4, Cells X Age\n  quote: Aβ42+ cell density was very low but did vary as a function of age (Table 4), with the\n    first cells appearing at p30, and roughly doubling in number between p90 and p150\n  statistics:\n  - about: all subregions\n    test: Kruskal-Wallis\n    statistic: chi2 = 28.9, df = 7, eta2 = 0.41\n    p: 0.0002\n  - about: external IC\n    test: Kruskal-Wallis\n    statistic: chi2 = 30.5, df = 7, eta2 = 0.47\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n    quantity: ratio of mean IC %Abeta42+ cells at p150 to p90\n    value: 2\n    tolerance: 0.2\n  criterion: Per 5XFAD mouse, Abeta42+ cells over DAPI cells in the IC (eIC, dIC, cIC together),\n    and in eIC alone; Kruskal-Wallis across ages for each. \"Did not exceed 0.5% at any age\" is\n    read as (a) every age mean, or (b) every mouse. \"Roughly doubling\" is taken at the 10%\n    tolerance. Reproduced when both tests have p < 0.05, no cells are found before p30, the\n    p150 to p90 ratio is within tolerance and the 0.5% bound holds under one reading. Partially\n    reproduced when the tests and the bound hold but the ratio does not.\n- id: ic-cells-subregion\n  statement: IC Abeta42+ cell density differs among subregions, higher in eIC than in dIC, and\n    higher in eIC than in cIC though that difference does not pass the corrected threshold.\n  source: Results, Inferior colliculus, paragraph 1; Table 4, Cells X Subregion\n  quote: Cell density also varied among subregions (Table 4), with the external cortex (eIC)\n    exhibiting a higher Aβ42+ cell density than both the dorsal cortex (dIC) and central nucleus\n    (cIC; though the latter failed the significance threshold for multiple comparisons of p <\n    0.017\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: chi2 = 14.5, df = 2, eta2 = 0.07\n    p: 0.0007\n  - about: eIC against dIC\n    test: Mann-Whitney\n    statistic: eta2 = 0.08\n    p: 0.0002\n    corrected: Bonferroni, threshold 0.017\n  - about: eIC against cIC\n    test: Mann-Whitney\n    statistic: eta2 = 0.03\n    p: 0.038\n    corrected: Bonferroni, threshold 0.017, not significant\n  criterion: Per 5XFAD mouse and subregion, Abeta42+ cells over DAPI cells, all ages (the\n    reported eta2 fits about 61 mice times 3); Kruskal-Wallis, then Mann-Whitney pairs at 0.017\n    (Table 4). Reproduced when the Kruskal-Wallis is significant, eIC is significantly higher\n    than dIC, and eIC exceeds cIC in mean. The eIC against cIC p-value is reported; its passing\n    0.017 does not count against the claim.\n- id: fig5b-ic-plaques-age\n  statement: IC plaques first appear around p90 and increase with age to 106.2 plaques/mm2 at\n    p150, in each subregion.\n  source: Results, Inferior colliculus, paragraph 1; Figure 5B; Table 4, Plaques X Age\n  quote: Plaque density varied significantly with age, with plaques first appearing around p90 and\n    reaching a peak mean density at p150 of 106.2 ± 16.2 S.E. plaques/mm2 (Fig. 5B, Table 4)\n  statistics:\n  - about: all subregions\n    test: Kruskal-Wallis\n    statistic: chi2 = 54.5, df = 7, eta2 = 0.90\n    p: 0.0001\n    p_relation: \"<\"\n  - about: external IC\n    test: Kruskal-Wallis\n    statistic: chi2 = 51.1, df = 7, eta2 = 0.88\n    p: 0.0001\n    p_relation: \"<\"\n  - about: central IC\n    test: Kruskal-Wallis\n    statistic: chi2 = 53.3, df = 7, eta2 = 0.93\n    p: 0.0001\n    p_relation: \"<\"\n  - about: dorsal IC\n    test: Kruskal-Wallis\n    statistic: chi2 = 48.4, df = 7, eta2 = 0.83\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n    quantity: mean IC plaque density at p150\n    value: 106.2\n    tolerance: 16.2\n    unit: plaques/mm2\n  criterion: Per 5XFAD mouse, plaques per mm2 in the IC as a whole and in each subregion;\n    Kruskal-Wallis across ages for each (Table 4). Reproduced when all four are significant at\n    p < 0.05, no plaques are found before p90 (\"around p90\" allows p60 to be read as onset only\n    if plaques are in a single mouse), p150 is the highest age mean, and the p150 mean is within\n    tolerance (the paper's S.E.).\n- id: fig5c-ic-plaques-subregion\n  statement: IC plaque density differs among subregions, highest in eIC, then dIC, lowest in cIC,\n    with eIC significantly above cIC.\n  source: Results, Inferior colliculus, paragraph 1; Figure 5C; Table 4, Plaques X Subregion;\n    Discussion, paragraph 4\n  quote: During the p90-p150 timeframe, plaque density also varied significantly among eIC, dIC,\n    and cIC (Fig. 5C, Table 4) with the highest density observed in eIC, followed by dIC\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: chi2 = 6.1, df = 2, eta2 = 0.06\n    p: 0.05\n    p_relation: \"<\"\n  - about: eIC against cIC\n    test: Mann-Whitney\n    statistic: eta2 = 0.12\n    p: 0.016\n    corrected: Bonferroni, threshold 0.017\n  criterion: Per mouse and subregion, plaques per mm2; Kruskal-Wallis across eIC, dIC and cIC,\n    then Mann-Whitney pairs at 0.017 (Table 4). The ages are read as (a) p90 to p150 (Results;\n    the reported eta2 fits about 24 mice) or (b) all ages (Figure 5C is labelled all ages).\n    Reproduced when, under one reading, the Kruskal-Wallis is significant, the means order eIC\n    > dIC > cIC, and eIC against cIC passes 0.017. Partially reproduced when the order holds but\n    a test does not. The Table 4 values for this test equal those of the MGB subregion test in\n    Table 3 (chi2 6.1, eta2 0.06); this is noted, not judged.\n- id: ic-no-sex\n  statement: IC plaque density does not differ between the sexes.\n  source: Results, Inferior colliculus, paragraph 1\n  quote: No significant differences in plaque density were detected between the sexes\n  criterion: A claim of absence. Mann-Whitney of females against males on per-mouse IC plaque\n    density at alpha 0.05 (Methods), mice aged p90 to p150 as for the other sex tests on\n    plaques. Reproduced when p >= 0.05; the means and p are reported either way.\n- id: fig6b-soc-cells\n  statement: Abeta42+ cells in the SOC vary in density with age but never exceed 0.5% of DAPI\n    cells in males or females.\n  source: Results, Superior olivary complex, nucleus of the lateral lemniscus, and cochlear nuclei,\n    paragraph 1; Figure 6B; Table 5\n  quote: We observed a sufficient number of Aβ42+ cells in SOC to determine that their density did\n    vary as a function of age (Fig. 6B, Table 5). However, at no age did cell density exceed 0.5%\n    in either males or females\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: chi2 = 14.9, df = 7, eta2 = 0.15\n    p: 0.04\n  criterion: Per 5XFAD mouse, Abeta42+ cells over DAPI cells in the SOC (lateral, medial and\n    periolivary together); Kruskal-Wallis across ages. The 0.5% bound is read as (a) every mean\n    by age and sex, or (b) every mouse. Reproduced when p < 0.05 and the bound holds under one\n    reading. Partially reproduced when the bound holds and the test does not.\n- id: soc-plaques-rare\n  statement: Plaques in the SOC are exceptionally rare, 3 in total in 2 of 61 5XFAD mice, all in\n    the lateral SOC.\n  source: Results, Superior olivary complex, nucleus of the lateral lemniscus, and cochlear nuclei,\n    paragraph 1; Figure 6A inset 1a\n  quote: Plaques in the SOC were exceptionally rare, with only 3 plaques in total observed in 2 of\n    61 mice, all in the lateral SOC\n  expected:\n  - quantity: plaques in the SOC over all 5XFAD mice\n    value: 3\n    tolerance: 0.3\n  - quantity: 5XFAD mice with any SOC plaque\n    value: 2\n    tolerance: 0.2\n  criterion: Plaque counts in the SOC of each 5XFAD mouse. Reproduced when the counts match and\n    every plaque is in the lateral SOC. Partially reproduced when there are no more than 6\n    plaques, in no more than 4 mice.\n- id: fig6cd-nll-cn-none\n  statement: There are no Abeta42+ cells or plaques in the nucleus of the lateral lemniscus or the\n    cochlear nuclei through p150.\n  source: Results, Superior olivary complex, nucleus of the lateral lemniscus, and cochlear nuclei,\n    paragraph 1; Figure 6C and 6D\n  quote: We saw no evidence of Aβ42+ cells or plaques in either the nLL or the CN (Fig. 6C, D)\n  criterion: Counts of Abeta42+ cells and plaques in the nLL and in the dorsal and ventral\n    cochlear nuclei of every 5XFAD mouse. Reproduced when none is found; partially reproduced\n    when isolated sites are found in at most 2 mice; the counts are reported either way.\n- id: fig7b-prnc-cells\n  statement: Intracellular Abeta42 appears in the PRNc, in putative giant reticulospinal neurons\n    and smaller cells, as early as p14 and consistently by p21; the overall Abeta42+ cell density\n    (below 2%) varies with age, with a trend for the RSNs alone.\n  source: Results, Caudal pontine reticular nucleus, paragraph 1; Figure 7B; Table 6\n  quote: We observed intracellular Aβ42 both in putative giant RSNs and other smaller cells in the\n    PRNc as early as p14, and consistently by p21 (Fig. 7B) ... The density of the overall Aβ42+\n    cell population varied with age, with a trend also seen specifically for RSNs (Fig. 7B,\n    Table 6)\n  statistics:\n  - about: all Abeta42+ cells\n    test: Kruskal-Wallis\n    statistic: chi2 = 14.7, df = 7, eta2 = 0.26\n    p: 0.04\n  - about: putative giant RSNs\n    test: Kruskal-Wallis\n    statistic: chi2 = 11.8, df = 7, eta2 = 0.16\n    p: 0.11\n  criterion: Per 5XFAD mouse, in the 800 um circle of the Results, Abeta42+ cells over DAPI cells,\n    and Abeta42+ cells over 40 um diameter over DAPI cells; Kruskal-Wallis across ages for\n    each. The circle's centre (\"region of highest apparent density\") is placed by eye, as the\n    paper did. The reported eta2 fits about 38 mice, so the mice with a PRNc section are used.\n    Reproduced when the all-cell test has p < 0.05, the RSN test has p < 0.2 (a trend), at least\n    one p14 mouse and most p21 mice have Abeta42+ cells, and every age mean is below 2%.\n    Partially reproduced when the onset and bound hold but the all-cell test does not.\n- id: fig7c-prnc-plaques\n  statement: Plaques in the PRNc first appear at p90 and vary in density with age.\n  source: Results, Caudal pontine reticular nucleus, paragraph 1; Figure 7C; Table 6\n  quote: Plaques, first evident at p90, also varied in density with age (Fig. 7C, Table 6)\n  statistics:\n  - test: Kruskal-Wallis\n    statistic: chi2 = 35.9, df = 7, eta2 = 0.96\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: Per 5XFAD mouse, plaques per mm2 in the 800 um circle; Kruskal-Wallis across ages.\n    Reproduced when p < 0.05 and no plaques are found before p90.\n- id: prnc-no-sex\n  statement: PRNc pathology shows no sex differences.\n  source: Results, Caudal pontine reticular nucleus, paragraph 1\n  quote: No sex-linked differences were observed\n  criterion: A claim of absence. Mann-Whitney of females against males (Methods) at alpha 0.05, on\n    per-mouse %Abeta42+ cells (all ages with a PRNc section) and on plaque density (p90 to\n    p150). Reproduced when neither is significant; the means and p-values are reported either\n    way.\n- id: cells-before-plaques\n  statement: In A1, subiculum and IC, Abeta42+ cells are first seen about 2 months before plaques.\n  source: Discussion, paragraph 3\n  quote: In cortex, subiculum, and inferior colliculus, Aβ42+ cells were first observed roughly 2\n    months prior to the appearance of plaques\n  depends_on:\n  - fig1a-a1-onset-p21\n  - fig3a-subiculum-onset\n  - ic-cells-low\n  - fig2b-a1-plaques-age\n  - fig5b-ic-plaques-age\n  expected:\n    quantity: lag from first Abeta42+ cells to first plaques, per region\n    value: 60\n    tolerance: 6\n    unit: days\n  criterion: The first ages of cells and of plaques from the claims named under depends_on. The\n    sampled ages make the lag one of a few values (the paper's own lags are 46 days for\n    subiculum, p14 to p60, 69 for A1, p21 to p90, and 60 for IC, p30 to p90), so the 10%\n    tolerance cannot apply and \"roughly 2 months\" is taken as 45 to 70 days, the span of the\n    paper's own lags. Reproduced when all three regions fall in it.\n- id: l5-pyramidal-fraction\n  statement: At least 24% of L5A and 11% of L5B pyramidal neurons in A1 are Abeta42+ at 5 months\n    of age, an estimate from the Abeta42+ cell densities and the prevalence of pyramidal neurons\n    in L5.\n  source: Discussion, paragraph 3\n  quote: Based on the prevalence of pyramidal ... neurons in L5 [30], we estimate that at least 24%\n    of L5A (and 11% of L5B) pyramidal neurons are Aβ42+ at 5 months of age\n  data: with_inputs\n  depends_on:\n  - fig1e-l5a-peak\n  expected:\n  - quantity: Abeta42+ fraction of L5A pyramidal neurons at p150\n    value: 24\n    tolerance: 2.4\n    unit: \"%\"\n  - quantity: Abeta42+ fraction of L5B pyramidal neurons at p150\n    value: 11\n    tolerance: 1.1\n    unit: \"%\"\n  criterion: The p150 mean %Abeta42+ cells of L5A and L5B divided by the fraction of L5 cells\n    that are pyramidal neurons, taken from the paper's reference [30] (not identified in this\n    file beyond the reference list; the paper does not state the fraction). Whether the\n    fraction is of DAPI cells or of neurons is open; readings (a) pyramidal neurons as a\n    fraction of all cells, (b) as a fraction of neurons, with neurons a fraction of DAPI cells\n    from the same reference. Reproduced when both values are within tolerance under one reading.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Removing a few thresholds I made up, and checking reference [30].

**Agent calls Bash**

```bash
cd  grep -n -A3 "^\[30\]" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/002035/10.3233-jad-220538.yaml'
s=open(p).read()
rep=[
("""    mice" at p21 is read as (a) in every p21 5XFAD mouse, or (b) in most of them (at least 5 of
    8). Reproduced when the p14 counts match and the p21 condition holds under one reading.
    Partially reproduced when the p21 condition holds but p14 shows more than one labelled cell
    or labelled cells in more than one mouse.""",
"""    mice" at p21 is read as (a) in every p21 5XFAD mouse, or (b) in more than half of them.
    Reproduced when the p14 counts match and the p21 condition holds under one reading.
    Partially reproduced when the p21 condition holds and the p14 counts do not match."""),
("""    is labelled all ages); Kruskal-Wallis across the eight bins. Reproduced when p < 0.05, L5A
    has the highest mean, L5B the second, and the other six bins together hold less than the
    L5B mean.""",
"""    is labelled all ages); Kruskal-Wallis across the eight bins. Reproduced when p < 0.05, L5A
    has the highest mean and L5B the second highest. How small the other bins must be for
    "predominantly" the paper does not say; their means are reported."""),
("""    (Fig. 1E legend). Partially""","""    (more than half; Fig. 1E legend). Partially"""),
("""    Kruskal-Wallis across ages for each (Table 4). Reproduced when all four are significant at
    p < 0.05, no plaques are found before p90 ("around p90" allows p60 to be read as onset only
    if plaques are in a single mouse), p150 is the highest age mean, and the p150 mean is within
    tolerance (the paper's S.E.).""",
"""    Kruskal-Wallis across ages for each (Table 4). Reproduced when all four are significant at
    p < 0.05, the first age with plaques is p90 (Figure 5B shows none at p60), p150 is the
    highest age mean, and the p150 mean is within tolerance (the paper's S.E.)."""),
("""    Reproduced when the counts match. Partially reproduced when no more than 10 of 61 mice have
    labelled cells and none has more than 2.""",
"""    Reproduced when the counts match. Partially reproduced when no mouse has more than 2
    labelled cells and the number of mice is outside tolerance."""),
("""    every plaque is in the lateral SOC. Partially reproduced when there are no more than 6
    plaques, in no more than 4 mice.""",
"""    every plaque is in the lateral SOC. Partially reproduced when the counts are outside
    tolerance but every plaque found is in the lateral SOC."""),
("""    cochlear nuclei of every 5XFAD mouse. Reproduced when none is found; partially reproduced
    when isolated sites are found in at most 2 mice; the counts are reported either way.""",
"""    cochlear nuclei of every 5XFAD mouse. Reproduced when none is found, not reproduced when
    any is; the counts are reported either way."""),
("""    Reproduced when the all-cell test has p < 0.05, the RSN test has p < 0.2 (a trend), at least
    one p14 mouse and most p21 mice have Abeta42+ cells, and every age mean is below 2%.
    Partially reproduced when the onset and bound hold but the all-cell test does not.""",
"""    Reproduced when the all-cell test has p < 0.05, at least one p14 mouse and more than half
    the p21 mice have Abeta42+ cells, and every age mean is below 2% (Figure 7B legend). The
    paper sets no threshold for a trend, so the RSN test's p is reported and not judged.
    Partially reproduced when the onset and bound hold but the all-cell test does not."""),
("""    that are pyramidal neurons, taken from the paper's reference [30] (not identified in this
    file beyond the reference list; the paper does not state the fraction). Whether the""",
"""    that are pyramidal neurons, taken from the paper's reference [30] (Ero et al. 2018, A cell
    atlas for the mouse brain, Front Neuroinform 12, 84); the paper does not state the fraction
    or which values of that atlas it used. Whether the"""),
]
for a,b in rep:
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/002035/10.3233-jad-220538.yaml paper/10.3233-jad-220538.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/002035/10.3233-jad-220538.yaml; grep -n "—\|rather" $f; python -c "
import yaml;d=yaml.safe_load(open('$f'));c=d['claims']
print(len(c),sum('quote' in x for x in c),sum('criterion' in x for x in c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('expected' in x for x in c))
for x in c:
  for k,v in x.items():
    if isinstance(v,str) and ': ' in v: print(x['id'],k)
"; git status --short
```

```
33 33 33 18 33 12
 M tools/build_site.py
 M tools/runner/run_requests.py
 M tools/site_assets/app.css
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
?? .zshrc
?? claims/002035/
?? scripts
?? tools/backfill_summaries.py
```

**Agent**

I wrote `claims/002035/10.3233-jad-220538.yaml`, and the quote checker passes it with no problems: all 33 quotes are word for word, and all 33 recorded statistical values were found in the text.

**Text read:** the PubMed Central author manuscript (NIHMS1886685, PMC10097438), from `paper/10.3233-jad-220538.txt`. That covers the main text, Methods, figure legends and Tables 1 to 6. I opened the PDF only to read the axis labels of Figs. 1 to 7. The paper has no supplement and links no code or data, so there was no code to read. I did not read the version of record. Nothing a claim needed was missing.

**Claims:** 33, all with quotes and none marked `inferred`.
- **Statistics:** 18 claims carry 33 entries in total, mostly Kruskal-Wallis across ages, layers or subregions and Mann-Whitney for pairs and sex, with the χ² and η² from the tables.
- **Expected values:** 12 claims have them. The tolerance is the paper's S.E. where it gives one, otherwise 10%. One claim departs from both, and its reason is given: the "roughly 2 months" lag from first cells to first plaques is judged as 45 to 70 days, the span of the paper's own lags.
- **Criteria:** all 33 claims have one. The opening comment sets out the shared method, all from the Methods: counting by eye, the eight 12.5% depth bins in A1, alignment to the Allen atlas (CCFv3), one value per mouse, and the PRNc circle 800 µm across.
- **Data:** one claim (`l5-pyramidal-fraction`) is `with_inputs`. It needs the share of layer 5 cells that are pyramidal neurons, from the paper's reference [30] (Erö et al. 2018, a mouse brain cell atlas). The paper does not state that number.

**Details the paper leaves open, with the readings named:**
- **DAPI counting in ImageJ:** (a) automatic threshold and particle count; (b) counting by hand.
- **One value per mouse from several images or hemispheres:** (a) counts and areas summed, then the ratio; (b) the mean of per-image values. Which hemisphere is not said.
- **What was imaged at 200X:** (a) the whole region; (b) sampled fields.
- **Which layers L5A and L5B are lower than, in DAPI density:** the Results say L2, L3, L4, L6A and L6B; the Fig. 1G legend omits L6A.
- **Which mice enter the DAPI-by-layer test:** the reported η² implies about 340 mouse-by-layer values, fewer than all 61 mice would give. Both all mice and only the mice counted in every layer are run.
- **Ages for the IC plaque-by-subregion test:** p90 to p150 (text) or all ages (Fig. 5C label).
- **Sample for the sex tests:** one value per mouse or per mouse and layer, and all ages or p90 to p150.
- **Thresholds that are words only:** "consistently" (every mouse, or more than half); "did not exceed 0.5%" (age means, or every mouse); "appeared first" (any mouse, or most mice).
- **Pyramidal fraction from reference [30]:** taken of all cells, or of neurons.
- **Effect sizes:** the paper cites a reference for η² but gives no formula. The reported values fit η² = (H − k + 1)/(n − k) for Kruskal-Wallis and z²/N for Mann-Whitney (n is the sample size, k the number of groups). That fit implies about 61 mice for most age tests, about 38 for PRNc and 24 for the p90 to p150 tests. This is my reading of the numbers, labelled as such in the file.

**Inconsistencies in the paper, noted in the file:**
- The Methods give 31 female and 30 male 5XFAD mice, but the per-age numbers add up to 30 and 31.
- The figure references in Tables 1 and 2 are off by one panel or one figure.
- The IC subregion test in Table 4 has the same χ² and η² as the MGB subregion test in Table 3.

**Other:** to read the figures I installed PyMuPDF into the temp directory. New untracked files appeared at the repository root during the run (`.bashrc`, `.vscode`, `scripts` and others). I did not create them on purpose. They fall outside `claims/002035/`, so the workflow will not keep them.

## End of run

30 turns, 6 minutes, $1.93 at API prices, result: success.
