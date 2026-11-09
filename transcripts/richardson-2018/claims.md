# openneuro-ds000228 · claims · run 40719298792

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls claims/001453 claims/openneuro-ds000228 paper 2>&1; git log --stat -1 | head -30
```

```
1:# Protocol for an attempt
40:## Reader
42:### 1. Get the paper
53:### 2. Read the paper's code
63:### 3. Write the claims file
148:### 4. Data from outside the paper's own recordings
156:### 5. Check
169:### 6. Answer questions
182:## Author
198:### 1. Establish what can be tested
325:### 2. Check the data against its description
340:### 3. Write the entry
398:### 4. Lock, check and run
409:### 5. Record the attempt
460:### 6. Hand over for verification
498:## Repeat attempts
540:## Local and remote datasets
563:## Verifier
567:### Round 1: without the author's conclusions
592:### Round 2: with the author's conclusions
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,181p docs/protocol.md; cat transcripts/openneuro-ds000228/claims-report.md
```

```
# Protocol for an attempt

Version: `pilot-12`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 177 more lines not kept]
```

**Agent**

Now the supplement is present. Let me read the text and example claims file.

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; cat claims/001453/*.yaml | head -150; cat tools/claims_check.py | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-018-03399-2.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-018-03399-2.txt",
 "offset": 1103,
 "limit": 1000
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-018-03399-2.txt",
 "offset": 1103,
 "limit": 500
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "=== \|SUPPLEMENT\|Supplementary" paper/*.txt | sed -n '1,200p' | awk -F: '$1>1700 || 1' | tail -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-018-03399-2.txt",
 "offset": 1760,
 "limit": 340
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Supplementary tables are not in the text. Let me see if the PDF has them as text or images.

**Agent calls Bash**

```bash
cd  python -c "
import fitz
d=fitz.open('paper/10.1038-s41467-018-03399-2.supp.pdf')
for i in range(9,13):
    p=d[i]; print('PAGE',i+1, len(p.get_images()), p.rect); print(p.get_text()[:300])
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftoppm pdftotext; ls .venv* 2>/dev/null | head; uv run --help >/dev/null 2>&1 && echo uv
```

```
uv
```

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/pg; uv run --no-project --with pymupdf python -c "
import fitz,os
d=fitz.open('paper/10.1038-s41467-018-03399-2.supp.pdf')
for i in [5,9,10,11,12]:
    p=d[i]; print('PAGE',i+1, len(p.get_images())); 
    p.get_pixmap(dpi=130).save(os.environ['TMPDIR']+f'/pg/s{i+1}.png')
" 2>&1 | tail -8
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s12.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s11.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s10.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s13.png"
}
```

Result: no output.

**Agent**

Now the schema.

**Agent calls Bash**

```bash
cd  cat schemas/claims.schema.json; grep -n "inferred\|elsewhere\|outside\|kind:" -A3 claims/*/*.yaml | head -60; ls claims
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
[... 607 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls claims/figshare-24639285 claims/dryad-4j0zpc8hz; head -40 claims/figshare-24639285/*.yaml; grep -n -i "openneuro" -A5 docs/archives.md | head -40
```

```
claims/dryad-4j0zpc8hz:
10.1093-plphys-kiad565.yaml

claims/figshare-24639285:
10.1038-s41597-024-03626-0.yaml
# Claims for Tarduno, Cottrell & Zhou (2024), Scientific Data, doi:10.1038/s41597-024-03626-0,
# on Figshare dataset 24639285 (doi:10.6084/m9.figshare.24639285.v1).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
# protocol pilot-12 as stated in docs/protocol.md (Reader).
#
# Text read: the version of record from Europe PMC (PMC11271266, full-text XML converted to text)
# as supplied under paper/, with Background & Summary, Methods, Data Records, Technical
# Validation, the legends of Figures 1 to 3 and Tables 1 and 2. The paper is a Data Descriptor
# and has no supplement; its additional plots are in the Figshare deposit itself. No PDF was
# supplied, so the figures were not seen: the nominal paleointensities printed in Figure 1 and
# the step ranges marked by arrows in Figures 1 and 2 are not recorded. The footnote legends of
# both tables (the marks after "M590 20 uT" and "Max intensity" in Table 1, and the marks after
# the specimen names, after n and after T Range in Table 2) are missing from the text.
# Code: the paper states that no custom code was used. It names PmagPy for looking at the
# directional and paleointensity data during collection and for checking quality factors
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;d=json.load(open('targets/openneuro.json'))
items=d if isinstance(d,list) else d.get('targets',d)
for t in (items if isinstance(items,list) else items.values()):
  if 'ds000228' in json.dumps(t): print(json.dumps({k:v for k,v in t.items() if k not in('files','layout','top_level_files')},indent=1)[:3000])
"
```

```
{
 "id": "ds000228",
 "name": "MRI data of 3-12 year old children and adults during viewing of a short animated film",
 "url": "https://openneuro.org/datasets/ds000228/versions/1.1.1",
 "doi": "10.18112/openneuro.ds000228.v1.1.1",
 "published_version": "1.1.1",
 "git_commit": "11410ae3a012249a68093471c6c95aa6f4d2da41",
 "versions": 4,
 "latest": true,
 "published": "2023-09-27",
 "license": "CC0",
 "bids_version": "1.0.1",
 "modalities": [
  "mri"
 ],
 "subjects": 155,
 "sessions": [],
 "tasks": [
  "pixar"
 ],
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,260p tools/claims_check.py
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

**Agent calls Bash**

```bash
python3 -c "
ev={'T01':('4:00',10,131),'T02':('2:46',16,96),'T03':('1:14',6,46),'T04':('4:42',14,150),'T05':('1:28',8,54),'T06':('3:48',10,124),'T07':('1:50',4,64),
'P01':('3:36',10,118),'P02':('2:06',18,73),'P03':('3:20',12,111),'P04':('1:00',6,39),'P05':('1:34',6,56),'P06':('4:10',10,135),'P07':('5:02',4,160),'P08':('0:42',4,29),'P09':('4:28',4,143),'P10':('1:20',4,49),'P11':('2:30',4,84),'P12':('3:04',4,100)}
for k,(t,d,p) in ev.items():
  m,s=map(int,t.split(':'));s=60*m+s;on=s//2+8;off=on+d//2-1
  print(k,on,off,p,on<=p<=off)
"
```

```
T01 128 132 131 True
T02 91 98 96 True
T03 45 47 46 True
T04 149 155 150 True
T05 52 55 54 True
T06 122 126 124 True
T07 63 64 64 True
P01 116 120 118 True
P02 71 79 73 True
P03 108 113 111 True
P04 38 40 39 True
P05 55 57 56 True
P06 133 137 135 True
P07 159 160 160 True
P08 29 30 29 True
P09 142 143 143 True
P10 48 49 49 True
P11 83 84 84 True
P12 100 101 100 True
```

**Agent**

Supplement tables read from the PDF. Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml",
 "content": "# Claims for Richardson, Lisandrelli, Riobueno-Naylor & Saxe (2018), \"Development of the social\n# brain from age three to twelve years\", Nature Communications 9, 1027,\n# doi:10.1038/s41467-018-03399-2, on OpenNeuro dataset ds000228 (\"MRI data of 3-12 year old children\n# and adults during viewing of a short animated film\"), snapshot 1.1.1\n# (doi:10.18112/openneuro.ds000228.v1.1.1).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-10-28,\n# protocol pilot-12 as stated in docs/protocol.md (Reader).\n#\n# Text read: the version of record (Nature Communications, open access, CC BY 4.0) as supplied\n# under paper/ (text extracted from the PDF), with the main text, figure legends, Methods and the\n# Supplementary Information (Supplementary Figures 1 to 8, Tables 1 to 4, Note 1). The four\n# supplementary tables are images in the supplement PDF and are missing from the text; they were\n# read from the PDF (pages 10 to 13), and their numbers are used below. The Peer Review File was\n# not supplied and is not needed.\n# Code: none linked. Code availability says the analysis code \"is available from the\n# corresponding author upon request\", so no repository was read and no open detail is settled by\n# code. The ToM behavioral battery is on OSF (https://osf.io/G5ZPV/, doi:10.17605/OSF.IO/G5ZPV).\n#\n# Data the paper used (Methods, Participants and fMRI sections; Supplementary Table 1).\n# - 122 children aged 3.5 to 12 years (M 6.7, s.d. 2.3; 64 female) and 33 adults aged 18 to 39\n#   (M 24.8, s.d. 5.3; 20 female). Age groups used in figures: 3yo n = 17, 4yo n = 14, 5yo n = 34,\n#   7yo n = 23, 8-12yo n = 34, adults n = 33. Age is a continuous variable in all tests.\n# - One fMRI run per participant (the first run; children under five did two, only the first is\n#   analysed): silent viewing of Pixar's \"Partly Cloudy\" (5.6 min), preceded by 10 s of rest,\n#   168 volumes, TR 2 s, TE 30 ms, 32 near-axial slices, voxel size 3 or 3.13 mm with slice gaps\n#   that differ between participants (Methods, fMRI data acquisition), plus a T1 image (1 mm).\n#   TRs 1 to 10 are rest and opening logos; the movie proper starts at TR 11.\n# - Behavior (children only): ToM score, the proportion correct of 24 matched items of the\n#   explicit ToM battery; for the 65 children aged 3 to 5, a false-belief (FB) composite of six\n#   items giving passers (5-6 correct, n = 30), inconsistent performers (3-4, n = 20) and failers\n#   (0-2, n = 15); DCCS summary score (3- to 5-year-olds analysed, n = 64, one inconsistent\n#   performer missing); nonverbal IQ (WPPSI block design under 5, KBIT-2 matrices from 5).\n# - Motion: the number of artifact timepoints per run (ART toolbox), used as the motion covariate\n#   in every analysis.\n#\n# Shared pipeline, with its source (Methods, fMRI data analysis, paragraphs 1 to 6, unless noted).\n# P1 SPM8; functional images registered to the run's first image, that image to the participant's\n#    anatomical image, the anatomical image normalized to MNI; upsampled to 2 mm isotropic voxels;\n#    5 mm Gaussian smoothing.\n# P2 Artifact timepoints (ART): composite motion > 2 mm relative to the previous timepoint, or a\n#    global-signal change beyond 3 s.d. from the mean global signal. Participants with one third\n#    or more artifact timepoints were dropped (5 children).\n# P3 Group ROIs: 9 mm spheres around the peaks of Supplementary Table 2. ToM: RTPJ [48 -60 30],\n#    LTPJ [-48 -62 30], PC [0 -54 34], DMPFC [-6 54 36], MMPFC [-4 58 16], VMPFC [-4 56 -16].\n#    Pain: RS2 [60 -28 38], LS2 [-62 -32 34], RInsula [42 6 -6], LInsula [-42 -2 -4],\n#    RMFG [50 42 12], LMFG [-46 36 14], AMCC [0 2 42] (DAMCC in Fig. 2). Sizes in voxels: 376, 368,\n#    382, 217, 275, 198; 368, 269, 309, 240, 142, 256, 249. Face: RFFA [38 -42 -22] (1019),\n#    LFFA [-40 -52 -18] (531), group-constrained parcels (Supplementary Fig. 4a). M1 10 mm spheres\n#    at [38 -24 58] and [-38 -20 58]; V1 at [-10 -86 2] and [10 -86 2] (Methods and Supplementary\n#    Fig. 3).\n# P4 Per voxel in each ROI: nearest-neighbour interpolation over artifact timepoints; regression of\n#    nuisance covariates, (1) the artifact timepoints and (2) five CompCor principal components from\n#    the participant's white-matter mask eroded by two voxels, computed on the interpolated data;\n#    for the inter-region correlation (IRC) analyses only, also the raw bilateral M1 timecourse;\n#    high-pass filter at 100 s; average over the ROI's voxels; artifact timepoints set to NaN.\n# P5 IRC: each ROI timecourse correlated with every other, per participant, Fisher z-transformed.\n#    Within-ToM is the mean over ToM ROI pairs, within-Pain over Pain ROI pairs, across-network\n#    over all ToM-Pain pairs (Methods, paragraph 7).\n# P6 Network timecourse for reverse correlation and functional maturity: each ROI timecourse\n#    z-normalized, then averaged over the ROIs of the network (Methods, paragraph 9). Functional\n#    maturity uses the same timecourses before z-normalization, TRs 11 to 168 (paragraph 13).\n# P7 Reverse correlation: in adults, per timepoint from TR 11 on, a one-tailed t-test of the\n#    network values against 0; an event is two or more consecutive significantly positive\n#    timepoints; events ranked by the adult mean at their peak timepoint (T01, P01 highest).\n# P8 Event response magnitude in children: the child's value at the event's peak timepoint, the\n#    timepoint with the highest adult mean (Methods, paragraph 11). Peak TRs (Supplementary\n#    Table 3): T01 131, T02 96, T03 46, T04 150, T05 54, T06 124, T07 64; P01 118, P02 73, P03 111,\n#    P04 39, P05 56, P06 135, P07 160, P08 29, P09 143, P10 49, P11 84, P12 100. Durations (s):\n#    T01 10, T02 16, T03 6, T04 14, T05 8, T06 10, T07 4; P01 10, P02 18, P03 12, P04 6, P05 6,\n#    P06 10, P07 4, P08 to P12 4 each.\n# P9 Motion covariate: number of artifact timepoints. Partial correlations with motion as covariate\n#    are Spearman (age) or Kendall (ToM score); regressions are ordinary linear regressions.\n#\n# Details none of the paper's sources fixes, with the readings named. Each criterion that rests on\n# one refers to it by its label.\n# O1 ROI extent. Supplementary Table 2 gives sizes of 142 to 382 voxels, while a full 9 mm sphere\n#    at 2 mm voxels holds about 380, so some spheres were cut down in a way the paper does not\n#    state. Readings: (a) ROI masks deposited with the paper's data, where they match these sizes;\n#    (b) full 9 mm spheres around the Supplementary Table 2 centers; (c) those spheres restricted\n#    to voxels with data in each participant.\n# O2 Artifact regressors. \"motion artifact timepoints\" as nuisance covariates is read as one\n#    indicator regressor per artifact timepoint (a); (b) a single regressor marking all of them.\n#    ART's composite-motion measure is used with its default definition, a standard choice.\n# O3 TRs in the IRC analysis: (a) all 168; (b) TRs 11 to 168, as in the other timecourse analyses.\n# O4 Scale of regression coefficients. The b values are on a scale the paper does not state; the\n#    adult-child effect of b = -.97 on within-ToM correlation is about one s.d., so (a) outcome and\n#    continuous predictors z-scored; (b) raw units. Criteria judge regressions on t, p and sign,\n#    which do not depend on the scale, and report b under both readings.\n# O5 Reverse-correlation threshold. The alpha of the per-timepoint one-tailed t-test is not given.\n#    Readings: (a) p < .05 uncorrected; (b) p < .01 uncorrected; (c) p < .05 FDR-corrected over\n#    the 158 timepoints. The reading whose events best match Supplementary Table 3 is reported.\n# O6 Span of z-normalization (P6): (a) TRs 11 to 168; (b) all 168 TRs. Artifact timepoints (NaN)\n#    are left out of the mean and s.d.\n# O7 Child event magnitude (P8) taken from (a) the z-normalized network timecourse used in the\n#    reverse correlation, (b) the same timecourse before z-normalization.\n# O8 Partial Kendall tau: computed as the partial rank correlation of Kendall (the formula used\n#    by R's ppcor), a standard choice; its p-value from the normal approximation.\n# O9 Tukey HSD differences in the behavioral results (e.g. Pass-Fail diff = 1.2 for ToM, against\n#    a mean difference of .20) are on a standardized scale: (a) the scores z-scored over the 65\n#    children aged 3 to 5; (b) raw scores. The tests are judged on p, and diffs reported for both.\n#\n# Tolerances. Means given with an s.e. use the s.e. as tolerance (the paper's uncertainty for a\n# mean); other reported numbers use 10% of the value. Counts of participants use 0, as they are\n# counts of the same people. Rule S, used by many criteria: a claim is reproduced when every\n# expected value is within tolerance and every test listed under statistics gives the same sign\n# and meets the paper's p bound; partially reproduced when the tests hold but some value is out of\n# tolerance; not reproduced when a test fails or its sign is reversed.\n#\n# Outside data the paper relies on: the independent adult sample (n = 20, scanned by Evelina\n# Fedorenko and colleagues) that defined the group ROIs and replicated the events (not deposited;\n# only the ROI centers are given); the face and scene group-constrained parcels of Julian et al.\n# 2012 (http://web.mit.edu/bcs/nklab/GSS.shtml); the hand-coded \"mental\", \"social\" and \"pain\"\n# events of Jacoby et al. 2016 (NeuroImage 126, 39-48); Neurosynth for the M1 and V1 centers\n# (coordinates given).\nschema_version: 2\ndataset:\n  archive: openneuro\n  id: ds000228\n  doi: 10.18112/openneuro.ds000228.v1.1.1\npaper: doi:10.1038/s41467-018-03399-2\nclaims:\n- id: participants\n  statement: The sample is 122 children aged 3.5 to 12 years (64 female) and 33 adults aged 18 to 39\n    (20 female); five further children were excluded for excessive motion. By age group there are\n    17, 14, 34, 23 and 34 children aged 3, 4, 5, 7 and 8 to 12 years.\n  source: Methods, Participants; Supplementary Table 1; Figure 2 legend\n  quote: One hundred twenty two 3.5–12-year-old children (M(s.d.) = 6.7 (2.3); 64 females) participated\n    in the study\n  expected:\n  - quantity: children\n    value: 122\n    tolerance: 0\n  - quantity: adults\n    value: 33\n    tolerance: 0\n  - quantity: female children\n    value: 64\n    tolerance: 0\n  - quantity: female adults\n    value: 20\n    tolerance: 0\n  - quantity: children aged 3, 4, 5, 7 and 8 to 12 (five values, in order 17, 14, 34, 23, 34)\n    value: 122\n    tolerance: 0\n  - quantity: mean child age\n    value: 6.7\n    tolerance: 0.67\n    unit: years\n  criterion: Counted over the participants with usable data. The age groups are those of Figure 2\n    and Supplementary Table 1 (3yo 3.52 to 3.99, 4yo 4.06 to 4.86, 5yo 5.01 to 5.99, 7yo 7 to 7.96,\n    8-12yo 8 to 12.3 years). Reproduced when all counts match exactly; partially reproduced when\n    the totals match but a group count or sex count differs.\n- id: supp-table1-behavior-by-age\n  statement: Mean ToM score rises across age groups (3yo .54, 4yo .63, 5yo .73, 7yo .88, 8-12yo .96),\n    and the false-belief groups (pass/inconsistent/fail) are 4/4/9 at 3 years, 3/7/4 at 4 years and\n    23/9/2 at 5 years.\n  source: Supplementary Table 1\n  inferred: Numbers read from Supplementary Table 1, an image in the supplement PDF; no sentence\n    states them.\n  expected:\n  - quantity: mean ToM score, 3yo\n    value: 0.54\n    tolerance: 0.054\n  - quantity: mean ToM score, 4yo\n    value: 0.63\n    tolerance: 0.063\n  - quantity: mean ToM score, 5yo\n    value: 0.73\n    tolerance: 0.073\n  - quantity: mean ToM score, 7yo\n    value: 0.88\n    tolerance: 0.088\n  - quantity: mean ToM score, 8-12yo\n    value: 0.96\n    tolerance: 0.096\n  - quantity: FB passers aged 3, 4, 5 (4, 3, 23); inconsistent (4, 7, 9); failers (9, 4, 2); total passers\n    value: 30\n    tolerance: 0\n  criterion: Rule S on the five means; the nine false-belief group counts by age must match exactly\n    for reproduced, and partially reproduced when the totals 30, 20 and 15 match but the split by\n    age does not.\n- id: beh-tom-age\n  statement: Among children, ToM score (proportion correct) increases with age (Kendall tau = .66).\n  source: Results, Behavioral results, paragraph 1; Figure 1a\n  quote: Performance on the ToM task (proportion correct) and DCCS were both positively correlated with\n    age\n  statistics:\n  - about: ToM score against age\n    test: Kendall tau correlation test\n    statistic: rk(120) = .66\n    p: 0.00001\n    p_relation: <\n    n: 122 children\n  - about: DCCS summary score against age\n    test: Kendall tau correlation test\n    statistic: rk(62) = .20\n    p: 0.049\n    n: 64 children aged 3 to 5\n  expected:\n  - quantity: Kendall tau, ToM score against age\n    value: 0.66\n    tolerance: 0.066\n  - quantity: Kendall tau, DCCS against age\n    value: 0.2\n    tolerance: 0.02\n  criterion: Rule S. Kendall tau-b with its normal-approximation p-value (the paper names the test,\n    not the variant; tau-b handles the ties the Methods mention, a standard choice).\n- id: beh-tom-dccs\n  statement: In 3- to 5-year-olds, ToM and DCCS scores are positively correlated controlling for age\n    (partial Kendall tau = .19).\n  source: Results, Behavioral results, paragraph 1\n  quote: In the 3-year to 5-year-old subset of children who completed both measures, ToM and DCCS scores\n    were positively correlated\n  statistics:\n  - test: partial kendall tau correlation test, controlling for age\n    statistic: rk(61) = .19\n    p: 0.03\n    n: 64 children aged 3 to 5\n  expected:\n    quantity: partial Kendall tau, ToM against DCCS given age\n    value: 0.19\n    tolerance: 0.019\n  criterion: Rule S, partial tau as in O8.\n- id: beh-fb-groups\n  statement: Among the 65 children aged 3 to 5, the false-belief composite gives 30 passers (15\n    female), 20 inconsistent performers (13 female) and 15 failers (6 female).\n  source: Results, Behavioral results, paragraphs 1 and 2; Methods, Explicit ToM task and false-belief\n    composite score\n  quote: categorize these children as false-belief passers (5–6 FB questions correct; n = 30 (15 female)),\n    inconsistent performers (3–4 FB questions correct; n = 20 (13 female)), and false-belief failers\n    (0–2 FB questions correct; n = 15 (6 female))\n  expected:\n  - quantity: passers\n    value: 30\n    tolerance: 0\n  - quantity: inconsistent performers\n    value: 20\n    tolerance: 0\n  - quantity: failers\n    value: 15\n    tolerance: 0\n  criterion: Groups as deposited with the behavioral data, or, if only the six false-belief item\n    scores are deposited, from the cut-offs of the Methods (5-6 pass, 3-4 inconsistent, 0-2 fail).\n    Reproduced when the three counts match exactly and the female counts 15, 13 and 6 match.\n- id: beh-fb-tom\n  statement: False-belief failers and inconsistent performers score lower than passers on the\n    remaining ToM items (means .55, .57 and .75).\n  source: Results, Behavioral results, paragraph 2\n  quote: False-belief task failers and inconsistent performers did worse on the remaining ToM items than\n    passers\n  statistics:\n  - about: Pass against Fail\n    test: Tukey HSD test of ToM*FB-Group ANOVA\n    statistic: diff = 1.2\n    p: 0.00005\n    p_relation: <\n  - about: Pass against Inc\n    test: Tukey HSD test of ToM*FB-Group ANOVA\n    statistic: diff = 1.08\n    p: 0.0001\n    p_relation: <\n  - about: Inc against Fail\n    test: Tukey HSD test of ToM*FB-Group ANOVA\n    statistic: diff = .16\n    p: 0.8\n  - test: Kruskal-Wallis rank sum test\n    statistic: H(2) = 22.96\n    p: 0.0001\n    p_relation: <\n    n: Pass 30, Inc 20, Fail 15\n  expected:\n  - quantity: mean, failers\n    value: 0.55\n    tolerance: 0.04\n  - quantity: mean, inconsistent\n    value: 0.57\n    tolerance: 0.03\n  - quantity: mean, passers\n    value: 0.75\n    tolerance: 0.02\n  - quantity: Kruskal-Wallis H\n    value: 22.96\n    tolerance: 2.3\n  criterion: The paper does not define \"remaining ToM items\". Readings, (a) proportion correct on the\n    18 items of the 24 that are not false-belief items; (b) the full ToM score. Rule S under either\n    reading; the Tukey tests are judged on p, with the diffs reported under both scales of O9; the\n    Inc against Fail test is not significant in the paper and must stay so.\n- id: beh-fb-age\n  statement: False-belief failers are younger than inconsistent performers and passers (mean ages 4.1,\n    4.8 and 5.2 years).\n  source: Results, Behavioral results, paragraph 2\n  quote: False-belief task failers were on average younger than passers and inconsistent performers\n  statistics:\n  - about: Pass against Fail\n    test: Tukey HSD test of Age*FB-Group ANOVA\n    statistic: diff = 1.4\n    p: 0.00001\n    p_relation: <\n  - about: Inc against Fail\n    test: Tukey HSD test of Age*FB-Group ANOVA\n    statistic: diff = .83\n    p: 0.01\n  - about: Pass against Inc\n    test: Tukey HSD test of Age*FB-Group ANOVA\n    statistic: diff = .59\n    p: 0.047\n  expected:\n  - quantity: mean age, failers\n    value: 4.1\n    tolerance: 0.41\n    unit: years\n  - quantity: mean age, inconsistent\n    value: 4.8\n    tolerance: 0.48\n    unit: years\n  - quantity: mean age, passers\n    value: 5.2\n    tolerance: 0.52\n    unit: years\n  criterion: Rule S, Tukey diffs reported under both scales of O9.\n- id: beh-fb-dccs\n  statement: False-belief failers have lower DCCS scores (worse response inhibition) than passers\n    (means 1.73, 2.26, 2.33 for fail, inconsistent, pass).\n  source: Results, Behavioral results, paragraph 2\n  quote: failers demonstrated worse response inhibition than the other two groups\n  statistics:\n  - about: Pass against Fail\n    test: Tukey HSD test of DCCS*FB-Group ANOVA\n    statistic: diff = .88\n    p: 0.01\n  - about: Inc against Fail\n    test: Tukey HSD test of DCCS*FB-Group ANOVA\n    statistic: diff = .78\n    p: 0.052\n  - test: Kruskal-Wallis rank sum test\n    statistic: H(2) = 7.56\n    p: 0.02\n    n: Pass 30, Inc 19, Fail 15\n  expected:\n  - quantity: mean DCCS, failers\n    value: 1.73\n    tolerance: 0.21\n  - quantity: mean DCCS, inconsistent\n    value: 2.26\n    tolerance: 0.17\n  - quantity: mean DCCS, passers\n    value: 2.33\n    tolerance: 0.09\n  criterion: Rule S on the means, the Kruskal-Wallis test and the Pass against Fail Tukey test. The Inc\n    against Fail test was marginal in the paper (p = .052); its p is reported and does not decide\n    the outcome.\n- id: motion-child-adult\n  statement: Children have more artifact timepoints than adults (mean 10.5 against 2.8).\n  source: Methods, fMRI data analysis, paragraph 2; Supplementary Figure 8a\n  quote: Number of artifact timepoints differed significantly between child and adult participants\n  statistics:\n  - test: Welch two-sample t-test\n    statistic: t(137.7) = 6.49\n    p: 0.000001\n    p_relation: <\n    n: 122 children, 33 adults\n  expected:\n  - quantity: mean artifact timepoints, children\n    value: 10.5\n    tolerance: 1.05\n  - quantity: mean artifact timepoints, adults\n    value: 2.8\n    tolerance: 0.28\n  criterion: Artifact timepoints as P2 (and O2 for the composite motion measure). Rule S.\n- id: motion-not-age-tom\n  statement: Among children, the number of artifact timepoints is not correlated with age or with ToM\n    score.\n  source: Methods, fMRI data analysis, paragraph 2\n  quote: Among children, number of motion artifact timepoints was not correlated with age ... or ToM\n    score\n  statistics:\n  - about: artifact timepoints against age\n    test: spearman correlation test\n    statistic: rs(120) = .02\n    p: 0.86\n    n: 122 children\n  - about: artifact timepoints against ToM score\n    test: kendall tau correlation test\n    statistic: rk(120) = -.005\n    p: 0.94\n    n: 122 children\n  criterion: A claim of absence, judged on the paper's tests, a Spearman correlation with age and a\n    Kendall tau correlation with ToM score, each at p < .05. Reproduced when neither is\n    significant; not reproduced when either is. The coefficients are reported.\n- id: motion-not-fb\n  statement: In 3- to 5-year-olds, the number of artifact timepoints does not differ between\n    false-belief passers and failers, nor vary with DCCS score.\n  source: Methods, fMRI data analysis, paragraph 2\n  quote: Number of artifact timepoints did not differ between young (3–5-year old) children based on\n    falsebelief task performance\n  statistics:\n  - about: Pass against Fail\n    test: linear regression, effect of FB-group on number of artifact timepoints\n    statistic: b = -.04, t = -.12\n    p: 0.9\n    n: Pass 30, Fail 15\n  - about: DCCS\n    test: linear regression, effect of DCCS summary score on number of artifact timepoints\n    statistic: b = .16, t = 1.18\n    p: 0.25\n    n: 64 children\n  criterion: A claim of absence, judged on the paper's linear regressions at p < .05. Reproduced when\n    neither effect is significant; not reproduced when either is.\n- id: irc-adult\n  statement: In adults, within-ToM (mean z .48) and within-Pain (.35) correlations are strongly\n    positive and the across-network correlation is negative (-.17), each within-network value\n    exceeding the across-network value.\n  source: Results, Inter-region correlation analysis, paragraph 2; Figure 2\n  quote: In adults, each network exhibited strong positive correlations within-network, and strong\n    negative correlations across network\n  statistics:\n  - about: within-ToM against across-network\n    test: paired sample two-tailed t-test\n    statistic: t(32) = 19.1\n    p: 2.2e-16\n    p_relation: <\n    n: 33 adults\n  - about: within-Pain against across-network\n    test: paired sample two-tailed t-test\n    statistic: t(32) = 23.2\n    p: 2.2e-16\n    p_relation: <\n    n: 33 adults\n  expected:\n  - quantity: mean within-ToM z correlation, adults\n    value: 0.48\n    tolerance: 0.02\n  - quantity: mean within-Pain z correlation, adults\n    value: 0.35\n    tolerance: 0.02\n  - quantity: mean across-network z correlation, adults\n    value: -0.17\n    tolerance: 0.02\n  - quantity: t, within-ToM against across\n    value: 19.1\n    tolerance: 1.91\n  - quantity: t, within-Pain against across\n    value: 23.2\n    tolerance: 2.32\n  criterion: Pipeline P1 to P5, readings O1, O2 and O3. Rule S under any reading.\n- id: irc-age-within\n  statement: Among children, within-ToM and within-Pain correlations increase with age, controlling for\n    motion.\n  source: Results, Inter-region correlation analysis, paragraph 3; Figure 2\n  quote: Among children, within-ToM and within-Pain network correlations increased significantly with\n    age\n  statistics:\n  - about: within-ToM\n    test: Spearman partial correlation test, motion as covariate\n    statistic: rs(119) = .37\n    p: 0.00005\n    p_relation: <\n    n: 122 children\n  - about: within-Pain\n    test: Spearman partial correlation test, motion as covariate\n    statistic: rs(119) = .28\n    p: 0.002\n    n: 122 children\n  expected:\n  - quantity: partial Spearman r, within-ToM against age\n    value: 0.37\n    tolerance: 0.037\n  - quantity: partial Spearman r, within-Pain against age\n    value: 0.28\n    tolerance: 0.028\n  criterion: Pipeline P1 to P5 with M1 regressed out, readings O1 to O3. Rule S under any reading.\n- id: irc-age-across\n  statement: Among children, the across-network correlation decreases with age (becomes more\n    anti-correlated), controlling for motion.\n  source: Results, Inter-region correlation analysis, paragraph 3; Figure 2\n  quote: Across-network correlations decreased significantly with age\n  statistics:\n  - test: Spearman partial correlation test, motion as covariate\n    statistic: rs(119) = -.35\n    p: 0.0001\n    p_relation: <\n    n: 122 children\n  expected:\n    quantity: partial Spearman r, across-network against age\n    value: -0.35\n    tolerance: 0.035\n  depends_on:\n  - irc-age-within\n  criterion: As irc-age-within. Rule S under any reading.\n- id: irc-adult-vs-child\n  statement: Adults have higher within-ToM and within-Pain correlations and a more negative\n    across-network correlation than children, controlling for motion.\n  source: Results, Inter-region correlation analysis, paragraph 3\n  quote: Within and across-network correlations were significantly greater in adults, compared to\n    children\n  statistics:\n  - about: within-ToM, effect of group (child against adult)\n    test: linear regression with age group and motion\n    statistic: b = -.97, t = -5.7\n    p: 6.2e-8\n    p_relation: <\n    n: 122 children, 33 adults\n  - about: within-Pain, effect of group\n    test: linear regression with age group and motion\n    statistic: b = -.75, t = -3.8\n    p: 0.0002\n    n: 122 children, 33 adults\n  - about: across-network, effect of group\n    test: linear regression with age group and motion\n    statistic: b = 1.26, t = 7.2\n    p: 2.2e-11\n    n: 122 children, 33 adults\n  expected:\n  - quantity: t, group effect on within-ToM\n    value: -5.7\n    tolerance: 0.57\n  - quantity: t, group effect on within-Pain\n    value: -3.8\n    tolerance: 0.38\n  - quantity: t, group effect on across-network\n    value: 7.2\n    tolerance: 0.72\n  criterion: Regression of each IRC measure on group (child coded against adult, so that children have\n    the negative within-network effect) and number of artifact timepoints (Methods, paragraph 7).\n    Pipeline readings O1 to O3; b under both scales of O4. Rule S on t and p. The motion effects the\n    paper also reports (within-ToM t = -4.3; within-Pain and across not significant) are reported.\n- id: irc-control-networks\n  statement: Without M1 regression, within-ToM (rs .39), within-Pain (.38), within-Scene (.23) and\n    within-M1 (.30) correlations rise with age in children, within-Face and within-V1 do not, and\n    the across ToM-Pain correlation falls with age (-.26) while across Face-Scene and M1-V1 do not\n    change.\n  source: Supplementary Figure 3 legend; Results, Inter-region correlation analysis, paragraph 3\n  quote: Significant positive age correlations among children (n=122) are present for withinToM (rs=.39,\n    p<.0001), within-Pain (rs=.38, p<.0001), within-Scene (rs=.23, p=.01), and withinM1 regions\n  statistics:\n  - about: within-ToM\n    test: spearman partial correlation test, motion as covariate\n    statistic: rs = .39\n    p: 0.0001\n    p_relation: <\n  - about: within-Pain\n    test: spearman partial correlation test, motion as covariate\n    statistic: rs = .38\n    p: 0.0001\n    p_relation: <\n  - about: within-Scene\n    test: spearman partial correlation test, motion as covariate\n    statistic: rs = .23\n    p: 0.01\n  - about: within-M1\n    test: spearman partial correlation test, motion as covariate\n    statistic: rs = .30\n    p: 0.001\n  - about: within-Face\n    test: spearman partial correlation test, motion as covariate\n    statistic: rs = .06\n    p: 0.53\n  - about: within-V1\n    test: spearman partial correlation test, motion as covariate\n    statistic: rs = -.16\n    p: 0.09\n  - about: across ToM-Pain\n    test: spearman partial correlation test, motion as covariate\n    statistic: rs = -.26\n    p: 0.005\n  - about: across Face-Scene\n    test: spearman partial correlation test, motion as covariate\n    statistic: rs = .02\n    p: 0.8\n  - about: across M1-V1\n    test: spearman partial correlation test, motion as covariate\n    statistic: rs = .18\n    p: 0.05\n  expected:\n  - quantity: rs within-ToM\n    value: 0.39\n    tolerance: 0.039\n  - quantity: rs within-Pain\n    value: 0.38\n    tolerance: 0.038\n  - quantity: rs within-Scene\n    value: 0.23\n    tolerance: 0.023\n  - quantity: rs within-M1\n    value: 0.3\n    tolerance: 0.03\n  - quantity: rs across ToM-Pain\n    value: -0.26\n    tolerance: 0.026\n  data: with_inputs\n  criterion: Pipeline P1 to P5 without the M1 regression (Supplementary Fig. 3 legend). Face regions\n    RSTS, LSTS, ROFA, LOFA, RFFA, LFFA and scene regions RRSC, LRSC, RTOS, LTOS, RPPA, LPPA are the\n    group-constrained parcels of Julian et al. 2012 (outside input); M1 and V1 are 10 mm spheres at\n    the coordinates in P3. Within-Face, within-V1, across Face-Scene and across M1-V1 are judged as\n    absence at p < .05 (across M1-V1 was p = .05 in the paper and counts as not significant).\n    Reproduced when the five expected values are within tolerance with p below the paper's levels\n    and the four absences hold; partially reproduced when the ToM and Pain results hold but a\n    control-network result differs.\n- id: irc-williams\n  statement: The age correlations of within-ToM and within-Pain are stronger than those of within-Face\n    and within-V1, not stronger than within-Scene and within-M1, and the across ToM-Pain decline is\n    stronger than across Face-Scene and across M1-V1.\n  source: Supplementary Figure 3 legend\n  quote: Positive correlations between within-ToM and within-Pain correlations and age were\n    significantly stronger than within-Face and within-V1 correlations, but not significantly stronger\n    than within-Scene and within-M1 correlations\n  statistics:\n  - about: within-Face against within-ToM\n    test: Williams' test of differences in age correlations\n    statistic: z = 2.69\n    p: 0.01\n  - about: within-Face against within-Pain\n    test: Williams' test\n    statistic: z = 2.66\n    p: 0.01\n  - about: within-Scene against within-ToM\n    test: Williams' test\n    statistic: z = 1.33\n    p: 0.18\n  - about: within-Scene against within-Pain\n    test: Williams' test\n    statistic: z = 1.3\n    p: 0.19\n  - about: M1 against within-ToM\n    test: Williams' test\n    statistic: z = .76\n    p: 0.44\n  - about: M1 against within-Pain\n    test: Williams' test\n    statistic: z = .73\n    p: 0.47\n  - about: V1 against within-ToM\n    test: Williams' test\n    statistic: z = 4.35\n    p: 0\n  - about: V1 against within-Pain\n    test: Williams' test\n    statistic: z = 4.32\n    p: 0\n  - about: across ToM-Pain against across Face-Scene\n    test: Williams' test\n    statistic: z(122) = 2.2\n    p: 0.03\n  - about: across ToM-Pain against across M1-V1\n    test: Williams' test\n    statistic: z(122) = 3.39\n    p: 0\n  data: with_inputs\n  depends_on:\n  - irc-control-networks\n  criterion: Williams' test (Steiger's form for dependent correlations sharing age) of the\n    difference between the two partial age correlations of irc-control-networks, with the\n    correlation between the two IRC measures as the third correlation; the paper names the test but\n    not whether it used the partial or raw correlations, and the partial ones are its reported age\n    correlations. Reproduced when the four significant differences (Face and V1 against ToM and Pain)\n    and the two across-network differences are significant at p < .05 in the same direction, and the\n    four Scene and M1 comparisons are not.\n- id: irc-3yo-distinct\n  statement: In 3-year-olds, within-ToM (mean z .21) and within-Pain (.23) correlations are positive and\n    higher than the across-network correlation, so the two networks are already distinct.\n  source: Results, Inter-region correlation analysis, paragraph 4; Figure 2\n  quote: Within-network correlations were higher than the acrossnetwork correlation\n  statistics:\n  - about: within-ToM against across-network\n    test: paired sample two-tailed t-test\n    statistic: t(16) = 6.2\n    p: 0.00005\n    p_relation: <\n    n: 17 three-year-olds\n  - about: within-Pain against across-network\n    test: paired sample two-tailed t-test\n    statistic: t(16) = 6.9\n    p: 0.00001\n    p_relation: <\n    n: 17 three-year-olds\n  expected:\n  - quantity: mean within-ToM z correlation, 3yo (printed \"21(.02)\", read as .21)\n    value: 0.21\n    tolerance: 0.02\n  - quantity: mean within-Pain z correlation, 3yo\n    value: 0.23\n    tolerance: 0.02\n  - quantity: t, within-ToM against across\n    value: 6.2\n    tolerance: 0.62\n  - quantity: t, within-Pain against across\n    value: 6.9\n    tolerance: 0.69\n  criterion: Pipeline as irc-adult, on the 17 children of the 3yo group. Rule S.\n- id: irc-3yo-not-anticorrelated\n  statement: Unlike adults, 3-year-olds show no anti-correlation between the ToM and Pain networks\n    (mean across-network z .05).\n  source: Results, Inter-region correlation analysis, paragraph 4; Figure 2\n  quote: unlike adults, ToM and pain networks were not anti-correlated in 3 year olds\n  expected:\n    quantity: mean across-network z correlation, 3yo\n    value: 0.05\n    tolerance: 0.02\n  criterion: The paper reports the mean and s.e. and no test. Reproduced when the 3yo mean\n    across-network correlation is not negative and is within tolerance; partially reproduced when it\n    is not negative but out of tolerance; not reproduced when it is negative. A one-sample t-test\n    against 0 is shown as a variant.\n- id: irc-3yo-homologous\n  statement: In 3-year-olds the strongest within-network correlations are between homologous regions\n    in opposite hemispheres, such as right and left TPJ and right and left insula.\n  source: Results, Inter-region correlation analysis, paragraphs 4 and 5; Figure 2 (3 years matrix)\n  quote: The strongest within-network correlations in the 3 year olds were between homologous pairs ...\n    of regions in opposite hemispheres, such as right and left TPJ (ToM), and the right and left insula\n    (Pain)\n  criterion: On the 3yo mean z-correlation matrix. \"Such as\" allows two readings, (a) the highest\n    within-ToM pair is RTPJ-LTPJ and the highest within-Pain pair is RInsula-LInsula; (b) the\n    homologous pairs (RTPJ-LTPJ; RS2-LS2, RInsula-LInsula, RMFG-LMFG) are the highest within their\n    network, ranking first among ToM pairs and filling the top three Pain pairs. Reproduced under\n    either reading.\n- id: irc-3yo-nonbilateral\n  statement: In 3-year-olds, within-network correlations excluding bilateral pairs (ToM .20, Pain .17)\n    still exceed the across-network correlation.\n  source: Results, Inter-region correlation analysis, paragraph 5\n  quote: However, the functional separation of the two networks was not fully explained by the strong\n    correlations between bilateral pairs\n  statistics:\n  - about: within-non-bilateral-ToM against across-network\n    test: paired sample two-tailed t-test\n    statistic: t(16) = 5.1\n    p: 0.0001\n    n: 17 three-year-olds\n  - about: within-non-bilateral-Pain against across-network\n    test: paired sample two-tailed t-test\n    statistic: t(16) = 4.4\n    p: 0.0005\n    n: 17 three-year-olds\n  expected:\n  - quantity: mean within-non-bilateral-ToM, 3yo\n    value: 0.2\n    tolerance: 0.02\n  - quantity: mean within-non-bilateral-Pain, 3yo\n    value: 0.17\n    tolerance: 0.02\n  - quantity: t, non-bilateral ToM against across\n    value: 5.1\n    tolerance: 0.51\n  - quantity: t, non-bilateral Pain against across\n    value: 4.4\n    tolerance: 0.44\n  depends_on:\n  - irc-3yo-distinct\n  criterion: The paper does not list the bilateral pairs. Read as the left-right pairs of Supplementary\n    Table 2, RTPJ-LTPJ for ToM and RS2-LS2, RInsula-LInsula, RMFG-LMFG for Pain, dropped from the\n    within-network means; the midline regions (PC, DMPFC, MMPFC, VMPFC, AMCC) have no partner. Rule S.\n- id: irc-tom-behavior\n  statement: Among children, within-ToM correlation rises and across-network correlation falls with\n    ToM score, controlling for motion.\n  source: Results, Inter-region correlation analysis, paragraph 6\n  quote: In children, the strength of inter-region correlations within the ToM network was positively\n    correlated with behavioral performance on the ToM battery outside the scanner\n  statistics:\n  - about: within-ToM against ToM score\n    test: Kendall tau partial correlation test, motion as covariate\n    statistic: rk(119) = .23\n    p: 0.0002\n    n: 122 children\n  - about: across-network against ToM score\n    test: Kendall tau partial correlation test, motion as covariate\n    statistic: rk(119) = -.20\n    p: 0.001\n    n: 122 children\n  expected:\n  - quantity: partial Kendall tau, within-ToM against ToM score\n    value: 0.23\n    tolerance: 0.023\n  - quantity: partial Kendall tau, across-network against ToM score\n    value: -0.2\n    tolerance: 0.02\n  criterion: Pipeline as irc-age-within; partial tau as O8. Rule S.\n- id: irc-tom-behavior-age\n  statement: Controlling for age as well as motion, ToM score has no relation to within-ToM or\n    across-network correlations.\n  source: Results, Inter-region correlation analysis, paragraph 6\n  quote: there was no relationship between within-ToM or across-network correlations and ToM score when\n    controlling for age in addition to motion\n  statistics:\n  - test: linear regressions of within-ToM and across-network correlation on ToM score, age and motion\n    statistic: ts < 1\n    p: 0.3\n    p_relation: '>'\n    n: 122 children\n  depends_on:\n  - irc-tom-behavior\n  criterion: A claim of absence, judged on the paper's two linear regressions at p < .05. Reproduced\n    when the ToM score effect is significant in neither; not reproduced when it is in either. t and\n    b (O4) are reported.\n- id: irc-fb-within\n  statement: Among 3- to 5-year-olds, false-belief passers have a higher within-ToM correlation than\n    failers (.29 against .25), controlling for age and motion.\n  source: Results, Inter-region correlation analysis, paragraph 7; Figure 3a,b\n  quote: There was a significant difference in within-ToM network correlation between explicit\n    false-belief task passers and failers\n  statistics:\n  - test: linear regression, effect of FB-Group (pass vs. fail) with age and motion\n    statistic: b = -.70, t = -2.06\n    p: 0.046\n    n: Pass 30, Fail 15\n  expected:\n  - quantity: mean within-ToM, passers\n    value: 0.29\n    tolerance: 0.02\n  - quantity: mean within-ToM, failers\n    value: 0.25\n    tolerance: 0.03\n  - quantity: t, FB-group effect\n    value: -2.06\n    tolerance: 0.206\n  depends_on:\n  - beh-fb-groups\n  criterion: Pipeline as irc-age-within. The sign of b and t follows the group coding (passers higher\n    gives the paper's negative sign with pass coded 0 and fail 1, or the reverse); the direction is\n    judged on the group means. Rule S, with p < .05.\n- id: irc-fb-within-dccs\n  statement: The passer and failer difference in within-ToM correlation becomes marginal when DCCS is\n    added to the regression.\n  source: Results, Inter-region correlation analysis, paragraph 7; Figure 3 legend\n  quote: This group difference becomes marginal when response inhibition (DCCS summary score) is\n    additionally included in the regression\n  statistics:\n  - about: FB-Group\n    test: linear regression with FB-Group, age, motion and DCCS\n    statistic: b = -.64, t = -1.80\n    p: 0.079\n    n: Pass 30, Fail 15\n  - about: DCCS\n    test: linear regression with FB-Group, age, motion and DCCS\n    statistic: b = -.08, t = -.59\n    p: 0.56\n  expected:\n    quantity: t, FB-group effect with DCCS\n    value: -1.8\n    tolerance: 0.18\n  depends_on:\n  - irc-fb-within\n  criterion: Reproduced when the FB-group effect has .05 <= p < .10 with the same direction as in\n    irc-fb-within and t within tolerance; partially reproduced when p is in that band but t is not;\n    not reproduced otherwise.\n- id: irc-fb-across\n  statement: False-belief passers and failers do not differ in across-network correlation (.04 against\n    .03).\n  source: Results, Inter-region correlation analysis, paragraph 7; Figure 3b\n  quote: There was no difference in across-network correlation between these two groups\n  statistics:\n  - test: linear regression, effect of FB-group (pass vs. fail) with age and motion\n    statistic: b = .51, t = 1.2\n    p: 0.23\n    n: Pass 30, Fail 15\n  depends_on:\n  - beh-fb-groups\n  criterion: A claim of absence, judged on the paper's regression at p < .05. Reproduced when the\n    FB-group effect is not significant; not reproduced when it is. Group means (paper .04 and .03)\n    and t are reported.\n- id: rc-events\n  statement: Reverse correlation on the adult network timecourses finds seven ToM events (68 s, mean\n    length 9.7 s) and twelve pain events (86 s, mean length 7.2 s), at the times of Supplementary\n    Table 3.\n  source: Results, Reverse correlation analysis, paragraph 2; Figure 4a; Supplementary Figure 5;\n    Supplementary Table 3\n  quote: In adults, the reverse correlation analysis produced seven theory of mind events (68 s total,\n    M(s.d.) length 9.7(4.2) s) and twelve pain events (86 s total, M(s.d.) length 7.2(4.7)s)\n  expected:\n  - quantity: ToM events\n    value: 7\n    tolerance: 0\n  - quantity: pain events\n    value: 12\n    tolerance: 0\n  - quantity: ToM event time\n    value: 68\n    tolerance: 6.8\n    unit: s\n  - quantity: pain event time\n    value: 86\n    tolerance: 8.6\n    unit: s\n  criterion: Pipeline P1 to P4 (no M1 regression), P6 and P7 on the 33 adults, readings O1, O2, O5 and\n    O6. Supplementary Table 3 gives stimulus times and peak TRs; for every event, onset TR = stimulus\n    seconds / 2 + 8 makes the peak TR fall inside the event (this mapping is a reading of the table,\n    not stated by the paper), e.g. T04 TRs 149 to 155, P08 TRs 29 to 30. Reproduced when, under one\n    reading of O5 and O6, the counts match, the totals are within tolerance, and each event of\n    Supplementary Table 3 overlaps a found event of the same network; partially reproduced when\n    most events (at least 5 of 7 ToM and 9 of 12 pain) are found.\n- id: rc-overlap\n  statement: ToM and pain events overlap at a single timepoint (the last of T05 and first of P05), less\n    overlap than chance in a permutation test.\n  source: Results, Reverse correlation analysis, paragraph 2; Methods, fMRI data analysis, paragraph 10\n  quote: The timepoints that exceeded baseline for ToM and pain networks were almost entirely\n    non-overlapping, with the exception of a single timepoint (2 s) ... This extent of overlap is\n    significantly less than that that would occur by chance\n  statistics:\n  - test: random timecourse permutations with the same number and duration of events\n    statistic: 5/1000 permutations with at most one timepoint of overlap\n    p: 0.005\n  expected:\n  - quantity: overlapping timepoints\n    value: 1\n    tolerance: 0\n  - quantity: permutation p\n    value: 0.005\n    tolerance: 0.005\n  depends_on:\n  - rc-events\n  criterion: Permutation as Methods, paragraph 10, 1000 permutations of 158-TR timecourses with the\n    found events in random order and random gaps (at least one zero between events of one network).\n    The paper's non-event counts (ToM 125, Pain 116 TRs) do not add up to 158 with its event totals\n    (34 and 43 TRs), so the readings are (a) 158 TRs with 124 and 115 zeros; (b) 125 and 116 zeros as\n    stated (159 TRs). Seed is a standard choice. The tolerance on p is the binomial spread of a count\n    of 5 in 1000, rounded up. Reproduced when one overlapping timepoint is found and p <= .01 under a\n    reading.\n- id: rc-child-adult-timecourse\n  statement: The mean network timecourse of each child age group correlates with the adult mean\n    timecourse, more so with age (ToM r .28, .31, .60, .72, .82; Pain .60, .56, .73, .83, .89 for 3,\n    4, 5, 7 and 8-12 years).\n  source: Results, Reverse correlation analysis, paragraphs 3 and 4; Supplementary Table 4\n  quote: The average timecourse in ToM and pain regions in children was highly correlated with that of\n    adults\n  statistics:\n  - about: ToM, every age bin\n    test: pearson correlation tests, TRs 11:168\n    p: 0.0005\n    p_relation: <\n    corrected: Bonferroni, alpha .01 for five age bins\n  - about: Pain, every age bin\n    test: pearson correlation tests, TRs 11:168\n    p: 1.0e-13\n    p_relation: <\n    corrected: Bonferroni, alpha .01 for five age bins\n  - about: ToM, 3yo\n    test: pearson correlation test\n    statistic: r = .28\n    p: 0.00046\n  - about: Pain, 3yo\n    test: pearson correlation test\n    statistic: r = .60\n    p: 1.0e-15\n    p_relation: <\n  expected:\n  - quantity: r ToM 3yo\n    value: 0.28\n    tolerance: 0.028\n  - quantity: r ToM 4yo\n    value: 0.31\n    tolerance: 0.031\n  - quantity: r ToM 5yo\n    value: 0.6\n    tolerance: 0.06\n  - quantity: r ToM 7yo\n    value: 0.72\n    tolerance: 0.072\n  - quantity: r ToM 8-12yo\n    value: 0.82\n    tolerance: 0.082\n  - quantity: r Pain 3yo\n    value: 0.6\n    tolerance: 0.06\n  - quantity: r Pain 4yo\n    value: 0.56\n    tolerance: 0.056\n  - quantity: r Pain 5yo\n    value: 0.73\n    tolerance: 0.073\n  - quantity: r Pain 7yo\n    value: 0.83\n    tolerance: 0.083\n  - quantity: r Pain 8-12yo\n    value: 0.89\n    tolerance: 0.089\n  criterion: Network timecourses as P6 before z-normalization (Supplementary Table 4 legend), TRs 11\n    to 168, averaged over the children of each age group and over the adults, artifact timepoints\n    left out of the averages. Rule S; partially reproduced when every r is significant and rises\n    from the youngest to the oldest bin but some values are out of tolerance.\n- id: supp-table4-other-networks\n  statement: The age-group mean timecourses of the Face, Scene, V1 and bilateral FFA regions correlate\n    with the adult timecourse in every age group, and M1 does in all but the 3- and 4-year-olds.\n  source: Supplementary Table 4\n  quote: All correlations are significantly positive (ps<.0005) except those shaded in grey (3yo M1\n  statistics:\n  - about: all networks and age groups except 3yo and 4yo M1\n    test: Pearson correlation\n    p: 0.0005\n    p_relation: <\n  - about: M1, 3yo\n    test: Pearson correlation\n    statistic: r = 0.11\n    p: 0.16\n  - about: M1, 4yo\n    test: Pearson correlation\n    statistic: r = 0.06\n    p: 0.46\n  expected:\n  - quantity: r Face 3yo, 4yo, 5yo, 7yo, 8-12yo (.75, .59, .71, .84, .86); listed value is 3yo\n    value: 0.75\n    tolerance: 0.075\n  - quantity: r Scene 3yo (others .67, .77, .80, .85)\n    value: 0.61\n    tolerance: 0.061\n  - quantity: r M1 3yo (others .06, .35, .44, .53)\n    value: 0.11\n    tolerance: 0.011\n  - quantity: r V1 3yo (others .61, .78, .74, .76)\n    value: 0.53\n    tolerance: 0.053\n  - quantity: r Bi-FFA 3yo (others .60, .68, .82, .83)\n    value: 0.72\n    tolerance: 0.072\n  data: with_inputs\n  depends_on:\n  - rc-child-adult-timecourse\n  criterion: As rc-child-adult-timecourse, for the regions of irc-control-networks and the bilateral\n    fusiform ROIs. Every one of the 25 values listed (each to 10%) is compared; reproduced when all\n    are within tolerance and only the two M1 values are not significant; partially reproduced when\n    at least 20 are within tolerance and the significance pattern holds.\n- id: rc-age-events\n  statement: Among children, responses at the peaks of pain events P01, P04 and P08 and ToM events T01\n    and T02 increase with age, controlling for motion, and no other event does at the corrected level.\n  source: Results, Reverse correlation analysis, paragraph 3; Figure 4a; Supplementary Figure 5\n  quote: Among children, three pain events (P01, P04, P08) and two ToM events (T01, T02) evoked\n    significantly greater responses with age\n  statistics:\n  - about: P01, P04, P08\n    test: spearman partial correlation tests, motion as covariate\n    statistic: rss > .29\n    p: 0.002\n    p_relation: <\n    corrected: Bonferroni, alpha .0026 for 19 events\n    n: 122 children\n  - about: T01, T02\n    test: spearman partial correlation tests, motion as covariate\n    statistic: rss > .28\n    p: 0.0026\n    p_relation: <\n    corrected: Bonferroni, alpha .0026 for 19 events\n    n: 122 children\n  depends_on:\n  - rc-events\n  criterion: Magnitudes as P8 at the Supplementary Table 3 peak TRs, ToM events from the ToM network\n    timecourse and pain events from the Pain network timecourse, readings O1, O2, O6 and O7.\n    Reproduced when, under one reading, exactly these five events pass p < .0026 with positive rs\n    above .28; partially reproduced when at least four of the five pass and at most one other event\n    does; not reproduced otherwise.\n- id: rc-t04-tom\n  statement: The ToM-network response at the peak of T04 rises with ToM score, controlling for age and\n    motion.\n  source: Results, Reverse correlation analysis, paragraph 3; Figure 1b\n  quote: Responses in ToM regions during a third ToM event (T04) were significantly positively\n    correlated with ToM score, controlling for age and motion\n  statistics:\n  - test: linear regression of T04 response magnitude on ToM score, age and motion\n    statistic: b = .4, t = 2.98\n    p: 0.0035\n    corrected: alpha .007 for 7 ToM events\n    n: 122 children\n  expected:\n    quantity: t, ToM score effect on T04 magnitude\n    value: 2.98\n    tolerance: 0.298\n  depends_on:\n  - rc-events\n  criterion: Magnitude as rc-age-events at TR 150. Reproduced when the ToM score effect has p < .007\n    and t within tolerance; partially reproduced when p < .007 but t is out of tolerance. Whether any\n    other ToM event passes p < .007 is reported (the paper marks only T04 in Figure 4a).\n- id: rc-fb-no-difference\n  statement: Responses at the seven ToM event peaks do not differ between false-belief passers and\n    failers.\n  source: Results, Reverse correlation analysis, paragraph 3; Figure 3c; Methods, fMRI data analysis,\n    paragraph 11\n  quote: Response magnitude during ToM events did not differ significantly between children who pass\n    and fail explicit falsebelief tasks\n  statistics:\n  - test: linear regressions of response magnitude on FB-Group, age and motion\n    p: 0.08\n    p_relation: '>'\n    n: Pass 30, Fail 15\n  depends_on:\n  - rc-events\n  - beh-fb-groups\n  criterion: A claim of absence, judged on the paper's tests at p < .05, one linear regression per ToM\n    event, and for T03 a permutation test of the group effect (Methods, paragraph 11, R lmPerm).\n    Reproduced when no event shows a significant FB-group effect; not reproduced when any does.\n- id: rc-3yo-events\n  statement: Reverse correlation on the 3-year-olds alone finds 4 of the 12 adult pain events and 1 of\n    the 7 adult ToM events; of its 32 s of pain events 14 s fall in adult pain events and 8 s in\n    adult ToM event T04, and of its 8 s of ToM events 4 s fall in an adult ToM event and 4 s in\n    adult pain event P01.\n  source: Results, Reverse correlation analysis, paragraphs 4 and 5; Figure 4a (dark borders)\n  quote: identified 4 of the 12 pain events and 1 of the 7 ToM events discovered in the ... adult\n    sample. These events correspond to a subset of the timepoints that were identified as ToM or pain\n    events in 3 year olds (Pain 14/32 s, ToM 4/8 s)\n  expected:\n  - quantity: 3yo pain event time\n    value: 32\n    tolerance: 3.2\n    unit: s\n  - quantity: 3yo ToM event time\n    value: 8\n    tolerance: 0.8\n    unit: s\n  - quantity: adult pain events found in 3yo\n    value: 4\n    tolerance: 0\n  - quantity: adult ToM events found in 3yo\n    value: 1\n    tolerance: 0\n  depends_on:\n  - rc-events\n  criterion: P7 run on the 17 three-year-olds with the reading of O5 and O6 that reproduced rc-events.\n    Reproduced when the counts and times match and the 3yo pain events overlap T04 and the 3yo ToM\n    events overlap P01; partially reproduced when the cross-network overlaps (T04 in the pain\n    network, P01 in the ToM network) hold but counts or times differ.\n- id: maturity-across\n  statement: Among children, the maturity (correlation with the adult mean) of each network's\n    timecourse is predicted by stronger across-network anti-correlation, not by within-network\n    correlation, with age and motion in the model.\n  source: Results, Relating functional maturity to inter-region correlations, paragraph 1; Figure 5\n  quote: We found that the maturity of the movie-driven timecourse in both ToM and Pain networks was\n    predicted by the anti-correlation of regions across networks\n  statistics:\n  - about: ToM maturity, across-network effect\n    test: linear regression on across-network, within-network correlation, age and motion\n    statistic: b = -.4, t = -5.5\n    p: 2.2e-7\n    n: 122 children\n  - about: ToM maturity, within-ToM effect\n    test: same regression\n    statistic: b = .1, t = 1.5\n    p: 0.14\n  - about: Pain maturity, across-network effect\n    test: linear regression on across-network, within-network correlation, age and motion\n    statistic: b = -.51, t = -7.4\n    p: 2.8e-11\n    n: 122 children\n  - about: Pain maturity, within-Pain effect\n    test: same regression\n    statistic: b = .13, t = 1.9\n    p: 0.06\n  expected:\n  - quantity: t, across-network effect on ToM maturity\n    value: -5.5\n    tolerance: 0.55\n  - quantity: t, across-network effect on Pain maturity\n    value: -7.4\n    tolerance: 0.74\n  depends_on:\n  - irc-age-within\n  criterion: Maturity is the Pearson r of each child's P6 network timecourse (not z-normalized, TRs 11\n    to 168, artifact timepoints left out) with the mean adult timecourse; IRC measures as\n    irc-age-within. Rule S on the across-network effects, with the within-network effects not\n    significant at p < .05 (as in the paper); b reported under both scales of O4.\n- id: maturity-within\n  statement: Among children, within-network correlations are associated with age but not with timecourse\n    maturity.\n  source: Results, Relating functional maturity to inter-region correlations, paragraph 2\n  quote: Greater within-network correlations were strongly associated with age, but not with timecourse\n    maturity\n  statistics:\n  - about: within-ToM, maturity effect\n    test: linear regression of within-network correlation on maturity, age and motion\n    statistic: b = .05, t = .48\n    p: 0.63\n  - about: within-ToM, age effect\n    test: same regression\n    statistic: b = .3, t = 2.5\n    p: 0.01\n  - about: within-Pain, maturity effect\n    test: linear regression of within-network correlation on maturity, age and motion\n    statistic: b = .07, t = .61\n    p: 0.55\n  - about: within-Pain, age effect\n    test: same regression\n    statistic: b = .2, t = 1.96\n    p: 0.05\n  depends_on:\n  - maturity-across\n  criterion: A claim of absence for the maturity effects, judged on the paper's regressions at p <\n    .05; reproduced when neither maturity effect is significant, not reproduced when either is. The\n    age effects are reported (ToM p = .01, Pain marginal p = .05) and do not decide the outcome.\n- id: maturity-tom-behavior\n  statement: ToM timecourse maturity correlates with ToM score controlling for motion, but not once age\n    is added.\n  source: Results, Relating functional maturity to inter-region correlations, paragraph 2\n  quote: while having an adult-like ToM timecourse was positively correlated with ToM behavior ... this\n    relationship did not remain significant in a regression including age as an additional predictor\n  statistics:\n  - about: maturity against ToM score\n    test: spearman partial correlation test, motion as covariate\n    statistic: rs(119) = .54\n    p: 1.3e-10\n    n: 122 children\n  - about: ToM score effect with age\n    test: linear regression of ToM maturity on age, ToM score and motion\n    statistic: b = .1, t = 1.2\n    p: 0.3\n  - about: age effect\n    test: same regression\n    statistic: b = .5, t = 4.2\n    p: 0.00005\n    p_relation: <\n  expected:\n    quantity: partial Spearman r, ToM maturity against ToM score\n    value: 0.54\n    tolerance: 0.054\n  depends_on:\n  - maturity-across\n  criterion: Reproduced when the partial correlation is within tolerance with p < .05, and in the\n    regression the ToM score effect is not significant (p >= .05) while age is.\n- id: maturity-fb\n  statement: ToM timecourse maturity does not differ between false-belief passers and failers.\n  source: Results, Relating functional maturity to inter-region correlations, paragraph 2\n  quote: Functional maturity of the ToM timecourse did not differ based on explicit false-belief task\n    performance\n  statistics:\n  - test: linear regression, effect of FB-Group (pass vs. fail) with age and motion\n    statistic: b = -.12, t = -.35\n    p: 0.73\n    n: Pass 30, Fail 15\n  depends_on:\n  - maturity-across\n  - beh-fb-groups\n  criterion: A claim of absence, judged on the paper's regression at p < .05. Reproduced when the\n    FB-group effect is not significant; not reproduced when it is.\n- id: face-rc\n  statement: In bilateral fusiform face regions, the children's mean timecourse correlates with the\n    adults' (r .86; 3-year-olds .72), reverse correlation in adults finds 7 face events (88 s) and in\n    3-year-olds 4 events (18 s), and face-event responses do not change with age.\n  source: Supplementary Figure 4; Results, Reverse correlation analysis, paragraph 1\n  quote: 'The average timecourse in bilateral fusiform ROIs in children was highly correlated with that\n    of adults (pearson correlation: r=.86, p<1.0x10-47)'\n  statistics:\n  - about: children against adults\n    test: pearson correlation\n    statistic: r = .86\n    p: 1.0e-47\n    p_relation: <\n  - about: 3-year-olds against adults\n    test: pearson correlation\n    statistic: r = .72\n    p: 1.0e-26\n    p_relation: <\n  - about: age effect on face-event magnitudes\n    test: spearman partial correlation including motion as covariate\n    statistic: '|r|s < .24'\n    p: 0.01\n    p_relation: '>'\n    corrected: Bonferroni, alpha .0071 for 7 events\n  expected:\n  - quantity: r, children against adults\n    value: 0.86\n    tolerance: 0.086\n  - quantity: r, 3yo against adults\n    value: 0.72\n    tolerance: 0.072\n  - quantity: adult face events\n    value: 7\n    tolerance: 0\n  - quantity: adult face event time\n    value: 88\n    tolerance: 8.8\n    unit: s\n  - quantity: 3yo face event time\n    value: 18\n    tolerance: 1.8\n    unit: s\n  data: with_inputs\n  criterion: Fusiform ROIs are the group-constrained face parcels of Julian et al. 2012 (outside input;\n    RFFA 1019 and LFFA 531 voxels, Supplementary Table 2), timecourses as P4 and P6, reverse\n    correlation as P7 with readings O5 and O6. Face events in adults have durations of 16, 4, 5, 7,\n    4, 4 and 4 TRs (Supplementary Note 1). The age test is absence at the paper's alpha .0071.\n    Reproduced when the two r values and event counts and times are within tolerance and no face\n    event changes with age; partially reproduced when the correlations hold but events differ.\n- id: face-overlap\n  statement: The overlap of face events with ToM events (4 TRs) and with pain events (15 TRs) does not\n    differ from chance.\n  source: Supplementary Note 1\n  quote: Thus, the amount of overlap between face and ToM events, and face and pain events, did not\n    differ from that expected by chance\n  statistics:\n  - about: face and ToM\n    test: permutation test, 1000 permutations\n    statistic: 111/1000\n    p: 0.11\n  - about: face and pain\n    test: permutation test, 1000 permutations\n    statistic: 928/1000\n    p: 0.93\n  data: with_inputs\n  depends_on:\n  - face-rc\n  - rc-overlap\n  criterion: Permutation as rc-overlap, with the face events of face-rc. A claim of absence judged at\n    p < .05 for fewer overlaps than chance, as in the paper; reproduced when neither p is below .05.\n    The overlaps (paper 4 and 15 TRs) are reported.\n- id: replication-sample\n  statement: In an independent sample of 20 adults, reverse correlation finds 7 ToM and 9 pain events,\n    all of them also found in the main adult sample; P08, P09 and P11 are not replicated.\n  source: Supplementary Figure 6; Methods, fMRI data analysis, paragraph 3\n  quote: Seven ToM and nine pain events were identified in the reverse correlation analysis of this\n    independent sample of adults\n  data: elsewhere\n  where: Not deposited. The paper names no archive for the 20 adults scanned by Evelina Fedorenko and\n    colleagues.\n  criterion: Not testable on this dataset, which holds the paper's 155 participants only.\n- id: hand-coded-events\n  statement: Of the adult reverse-correlation events, 6 of 7 ToM events but only 2 of 12 pain events\n    fall at least partly within the mental, social or pain events hand-coded in an earlier study.\n  source: Supplementary Figure 7\n  quote: most ToM events identified by the reverse correlation analysis were at least partially included\n    in the original coding (6/7 ToM events labeled as Mental or Social), only two of twelve pain events\n    were included in the coding\n  expected:\n  - quantity: ToM events in the hand coding\n    value: 6\n    tolerance: 0\n  - quantity: pain events in the hand coding\n    value: 2\n    tolerance: 0\n  data: with_inputs\n  depends_on:\n  - rc-events\n  criterion: The hand-coded events are those of Jacoby et al. 2016 (NeuroImage 126, 39-48), an outside\n    input. An event counts as included when any of its TRs falls in a coded event. For ToM, coded\n    Mental or Social events; for pain, the paper says \"included in the coding\", read as (a) coded\n    Pain events, (b) any coded event. Reproduced when both counts match under one reading.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml",
 "old_string": "  quote: identified 4 of the 12 pain events and 1 of the 7 ToM events discovered in the ... adult\n    sample. These events correspond to a subset of the timepoints that were identified as ToM or pain\n    events in 3 year olds (Pain 14/32 s, ToM 4/8 s)",
 "new_string": "  quote: 'identified 4 of the 12 pain events and 1 of the 7 ToM events discovered in the ... adult\n    sample. These events correspond to a subset of the timepoints that were identified as ToM or pain\n    events in 3 year olds (Pain: 14/32 s, ToM: 4/8 s)'"
}
```

```
The file claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml",
 "old_string": "  - quantity: children aged 3, 4, 5, 7 and 8 to 12 (five values, in order 17, 14, 34, 23, 34)\n    value: 122\n    tolerance: 0",
 "new_string": "  - quantity: children aged 3\n    value: 17\n    tolerance: 0\n  - quantity: children aged 4\n    value: 14\n    tolerance: 0\n  - quantity: children aged 5\n    value: 34\n    tolerance: 0\n  - quantity: children aged 7\n    value: 23\n    tolerance: 0\n  - quantity: children aged 8 to 12\n    value: 34\n    tolerance: 0"
}
```

```
The file claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml paper/10.1038-s41467-018-03399-2.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml; grep -n -i "rather\|—" $f; python3 -c "
import yaml
d=yaml.safe_load(open('$f'))
def walk(x,p=''):
  if isinstance(x,dict):
    for k,v in x.items(): walk(v,p+'/'+str(k))
  elif isinstance(x,list):
    for i,v in enumerate(x): walk(v,p+'/'+str(i))
  elif isinstance(x,str) and ': ' in x: print(p, x[:80])
walk(d)
print(sum(1 for c in d['claims'] if 'statistics' in c), sum(1 for c in d['claims'] if 'criterion' in c), sum(1 for c in d['claims'] if 'expected' in c))
"
```

```
/claims/33/quote identified 4 of the 12 pain events and 1 of the 7 ToM events discovered in the .
/claims/38/quote The average timecourse in bilateral fusiform ROIs in children was highly correla
33 42 30
```

**Agent**

I wrote the claims file at `claims/openneuro-ds000228/10.1038-s41467-018-03399-2.yaml`. The quote checker reports 42 claims, 41 quotes, 85 statistical values and 0 problems.

**Text read.** The version of record (Nature Communications, CC BY), main text, Methods and the full Supplementary Information: Supplementary Figs. 1 to 8, Tables 1 to 4 and Note 1. The four supplementary tables are images, so they are missing from the `.txt`. I read them from the supplement PDF:
- Table 1: demographics by age group.
- Table 2: ROI centers and sizes.
- Table 3: event times, durations and peak TRs.
- Table 4: correlations between each age group's timecourse and the adults'.

The earlier run stopped because the supplement was missing; it is now there. No code is linked: the paper says it is "available from the corresponding author upon request", so code settles nothing.

**Counts.** 42 claims: 41 with quotes and 1 inferred (Supplementary Table 1). 33 have statistics, 30 have expected values, and all 42 have criteria. Ten are claims of absence, each judged on the paper's own test.
- Three need outside inputs: the face and scene parcels of Julian et al. 2012, and the hand-coded events of Jacoby et al. 2016.
- One is untestable here: the replication sample of 20 adults was never deposited (`data: elsewhere`).

**Details the paper leaves open, with the readings named:**
- **O1, ROI extent:** Table 2 sizes are 142 to 382 voxels, smaller than a full 9 mm sphere for some regions. Readings: (a) deposited ROI masks, (b) full spheres, (c) spheres limited to voxels with data.
- **O2, artifact regressors:** (a) one indicator per artifact timepoint, (b) a single regressor.
- **O3, TRs used for inter-region correlation:** (a) all 168, (b) TRs 11 to 168.
- **O4, scale of regression b values:** (a) z-scored, (b) raw units. Criteria judge regressions on t, p and sign, so this does not change outcomes.
- **O5, per-timepoint threshold in the reverse correlation:** (a) p < .05 uncorrected, (b) p < .01 uncorrected, (c) FDR-corrected.
- **O6, span of z-normalization:** (a) TRs 11 to 168, (b) all 168.
- **O7, child event magnitude:** taken from the z-normalized timecourse or from the timecourse before normalization.
- **O8, partial Kendall tau:** the ppcor form, a standard choice.
- **O9, Tukey HSD diffs:** they are on a standardized scale (for example 1.2 against a raw mean difference of .20). Readings: z-scored over the 3- to 5-year-olds, or raw. Judged on p.
- **Claim-specific readings:**
  - "Remaining ToM items" means either the 18 items that are not false-belief items or the full score.
  - "Such as" in the claim that homologous pairs correlate most strongly in 3-year-olds: the top pair in each network, or the homologous pairs ranking highest.
  - Which pairs count as bilateral.
  - For the overlap permutation, the stated non-event counts (125 and 116 TRs) do not add up to 158 TRs with the event totals. Readings: (a) 158 TRs with 124 and 115 non-event TRs, (b) 125 and 116 as stated (159 TRs).
  - For the hand-coded events: included in coded Pain events, or in any coded event.
- **My own inference:** Table 3 gives stimulus times and peak TRs but no rule linking them. With onset TR = stimulus seconds / 2 + 8, every event's peak falls inside its event. The file labels this as a reading of the table, not a statement of the paper.

**Missing from the paper:** the replication adults (n = 20) are not deposited and no archive is named, so `replication-sample` cannot be tested. The 3-year-olds' mean within-ToM correlation is printed "21(.02)"; I recorded it as .21. The paper reports no test for the 3-year-olds' lack of anti-correlation, so that claim is judged on the reported mean, with a one-sample t-test shown as a variant.

## End of run

26 turns, 7 minutes, result: success.
