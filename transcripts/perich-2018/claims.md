# 000688 · claims · run 39900668873

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md; ls claims/001453/ paper/ claims/000688 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 170
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-10`. Record this version in the attempt's provenance.
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
18	  claim, and it asks a reader for any method detail the file lacks.
19	- The **verifier** checks the author's work and must not be the author.
20	
[... 150 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml; wc -c paper/10.1016-j.neuron.2018.09.030.txt; head -30 paper/10.1016-j.neuron.2018.09.030.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the full paper text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.09.030.txt",
 "offset": 30,
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.09.030.txt",
 "offset": 430,
 "limit": 500
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.09.030.txt",
 "offset": 930,
 "limit": 600
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "##### Supplement" paper/10.1016-j.neuron.2018.09.030.txt; wc -l paper/10.1016-j.neuron.2018.09.030.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.09.030.txt",
 "offset": 1530,
 "limit": 820
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -rl "000688" --include=*.json --include=*.yaml --include=*.md --include=*.csv . 2>/dev/null | grep -v transcripts | head; ls
```

```
./targets/dandisets.json
./papers/manifest.yaml
./claims/001845/10.1523-jneurosci.0143-26.2026.yaml
LICENSE
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '000688' in json.dumps(x)[:300]: print(json.dumps(x,indent=1)[:3000])
"; grep -n -B2 -A12 "000688" papers/manifest.yaml | head -40
```

```
966-    pdf: false
967-    supplements: 0
968:  000688:
969-  - doi: 10.1016/j.neuron.2018.09.030
970-    status: stored
971-    version: as served by ncbi_pmc
972-    source: ncbi_pmc+crossref (paper-text-fetcher)
973-    pdf: false
974-    supplements: 8
975-  - doi: 10.48550/arxiv.2310.16046
976-    status: stored
977-    version: arXiv version 1
978-    source: arXiv PDF
979-    pdf: true
980-    supplements: 0
```

**Agent calls Bash**

```bash
cd  grep -n -A25 '"000688"' targets/dandisets.json | head -60
```

```
3301:   "dandiset": "000688",
3302-   "name": "Long-term recordings of motor and premotor cortical spiking activity during reaching in monkeys",
3303-   "published_version": "0.250122.1735",
3304-   "asset_count": 111,
3305-   "size_gb": 13.18,
3306-   "data_standards": [
3307-    "Neurodata Without Borders (NWB)"
3308-   ],
3309-   "species": [
3310-    "Macaca mulatta - Rhesus monkey"
3311-   ],
3312-   "approaches": [
3313-    "electrophysiological approach",
3314-    "behavioral approach"
3315-   ],
3316-   "papers": [
3317-    {
3318-     "doi": "10.1016/j.neuron.2018.09.030",
3319-     "title": "A Neural Population Mechanism for Rapid Learning",
3320-     "relation": "IsDescribedBy",
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 3326,3380p targets/dandisets.json
```

```
"title": "A Unified, Scalable Framework for Neural Population Decoding",
     "relation": "IsCitedBy",
     "resource_type": null,
     "preprint": true
    },
    {
     "doi": "10.1007/s00221-017-4997-1",
     "title": "Altered tuning in primary motor cortex does not account for behavioral adaptation during force field learning",
     "relation": "IsCitedBy",
     "resource_type": null,
     "preprint": false
    },
    {
     "doi": "10.1038/s41593-019-0555-4",
     "title": "Long-term stability of cortical population dynamics underlying consistent behavior",
     "relation": "IsCitedBy",
     "resource_type": null,
     "preprint": false
    },
    {
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; sed -n 1,80p tools/claims_check.py
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
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
[... 63 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
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
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:5000])"
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

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.09.030.supp8.pdf",
 "pages": "5"
}
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2018.09.030.supp8.pdf",
 "pages": "7"
}
```

Result: not kept, because it reads the paper's text.

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "import fitz;print(fitz.__doc__)"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz;print(fitz.__doc__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
cd  ls .venv 2>/dev/null; which uv pip python3; python3 -c "import pypdf" 2>&1; uv run --no-project --with pymupdf python -c "import fitz;print('ok')" 2>&1 | tail -2
```

```
/opt/hostedtoolcache/Python/3.13.16/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.16/x64/bin/pip
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python3
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
  warnings.warn(
ok
```

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/pg; uv run --no-project --with pymupdf python -c "
import fitz,os
t=os.environ['TMPDIR']+'/pg/'
d=fitz.open('paper/10.1016-j.neuron.2018.09.030.supp8.pdf')
for i in [4,6]: d[i].get_pixmap(dpi=130).save(t+f's8p{i+1}.png')
for k in [3,4,5,6,7]:
  d=fitz.open(f'paper/10.1016-j.neuron.2018.09.030.supp{k}.pdf'); d[0].get_pixmap(dpi=110).save(t+f's{k}.png')
" 2>&1 | grep -v warn; ls $TMPDIR/pg
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
echo $TMPDIR
```

```
/tmp/claude-1001
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s8p5.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s8p7.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s3.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s4.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s6.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s7.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s5.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  uv run --no-project --with pymupdf python -c "
import fitz,os
t=os.environ['TMPDIR']+'/pg/'
d=fitz.open('paper/10.1016-j.neuron.2018.09.030.supp8.pdf'); d[5].get_pixmap(dpi=120).save(t+'s8p6.png')
d=fitz.open('paper/10.1016-j.neuron.2018.09.030.supp2.pdf'); d[0].get_pixmap(dpi=100).save(t+'s2.png')
" 2>/dev/null
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s8p6.png"
}
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pg/s2.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

Result: no output.

**Agent calls Write**

```json
{
 "file_path": "claims/000688/10.1016-j.neuron.2018.09.030.yaml",
 "content": "# Claims for Perich, Gallego & Miller (2018), \"A Neural Population Mechanism for Rapid Learning\",\n# Neuron 100, 964-976, on dandiset 000688.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23, protocol\n# pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC6250582, NIHMS1507895), as served\n# by ncbi_pmc, not the version of record: main text, figure legends 1 to 7 and STAR Methods, with\n# its eight supplement files (NIHMS1507895-supplement-1 to -8). Supplements 1 to 7 are the main\n# Figures 1 to 7 as images; supplement 8 holds Figures S1 to S7 with their legends. Figure panels\n# and the p-values printed inside them (Figures 3E, S5F, S7A, S7D) were read from the PDFs. The\n# figure letters of the manuscript do not all agree with the Results: the Results cite Figure 3E,F,G\n# and 4E where the legends call the same panels 3E, 3F, 3G and 4D; Figure 6 has two panels \"d\" in\n# its legend (the lag histogram is panel C in the image). Sources below give both where they differ.\n#\n# Code: the paper links no code. Data and Software Availability says \"Custom code was used to\n# process the neural and kinematic data ... This code may be shared upon reasonable request\", and\n# names the MATLAB functions used (cov, pca, factoran, glmfit, mahal). No repository was read. Every\n# method below is from the STAR Methods, the legends or the Results.\n#\n# Dataset: dandiset 000688, \"Long-term recordings of motor and premotor cortical spiking activity\n# during reaching in monkeys\", lists this paper and Glaser et al. 2018 (Nat. Commun.) as\n# IsDescribedBy. Whether it holds the curl field and visuomotor rotation sessions this paper\n# analyses is the author's to find; the data were not looked at.\n#\n# Data the paper used, as it reports them:\n# - Subjects: two male rhesus macaques, Monkey C (11.7 kg) and Monkey M (10.5 kg), with 96-channel\n#   Utah arrays in M1 and PMd (Blackrock Cerebus), spikes sorted offline (Plexon Offline Sorter)\n#   over all three epochs of a session together.\n# - Task: instructed-delay center-out reaching with a 2-D planar manipulandum, eight targets on a\n#   circle of 8 cm (6 cm in Monkey C's first three sessions), 2 cm square targets; hold 0.5 to 1.5\n#   s, instructed delay 0.5 to 1.5 s, auditory go cue, 1 s to reach, 0.5 s target hold. Handle\n#   position at 1 kHz.\n# - Sessions: each has a Baseline epoch, a perturbation epoch and a Washout epoch. Curl field (CF)\n#   sessions: 85 degree velocity-dependent field, k = 0.15 N s/cm, CW or CCW; Baseline 170 to 225\n#   rewards, Force 201 to 337, Washout 153 to 404. Monkey C three CW and two CCW, Monkey M four\n#   CCW (9 sessions). Visuomotor rotation (VR) sessions: 30 degree rotation of the cursor, CW or\n#   CCW; Baseline 154 to 217 successful trials, Rotation 219 to 316, Washout 162 to 348. Monkey C\n#   two CW and two CCW, Monkey M three CCW (7 sessions). The Methods and Figure 6 legend count 9 CF\n#   and 7 VR, 16 sessions in all; the Figure 2C legend shows two CW and five CCW CF sessions and the\n#   Figure 7 legend one CW and four CCW VR sessions, which do not add up to these counts.\n# - Neurons: 137 to 256 PMd and 55 to 93 M1 per session in Monkey C, 66 to 121 PMd and 26 to 51 M1\n#   in Monkey M. Cells with high coincidence across channels excluded. GLM analyses use neurons\n#   above 5 Hz trial-averaged rate (918 M1, 2221 PMd pooled over all sessions); the covariance\n#   analysis uses neurons above 1 Hz.\n# - Measured variables: spike times of sorted units, handle position (and its derivatives), trial\n#   events (target onset, go cue, movement onset, reward), the perturbation type and direction,\n#   the epoch of each trial.\n#\n# Shared methods, from the STAR Methods unless said otherwise. Claims cite these as M1 to M8.\n# M1 Behavioral error: angular deviation of the hand from the target direction 150 ms after\n#    movement onset, minus the mean deviation for that target in Baseline; CW sessions sign-flipped\n#    and all sessions pooled (Behavioral adaptation analysis).\n# M2 Latent activity: spikes counted in 50 ms bins, square-root transformed, convolved with a\n#    non-causal Gaussian kernel of width 100 ms; PCA per area per session, with the PCA axes found on\n#    Baseline trials only; 8 components for M1 and 16 for PMd (Dimensionality reduction;\n#    Output-potent and output-null subspaces; Results, Models to study ..., paragraph 3).\n# M3 Subspaces: a linear map W from the 16 PMd latent dimensions to the 8 M1 latent dimensions\n#    (M = W P), fit on Baseline trials; SVD W = U S V'; the rows of V' give the output-potent and\n#    output-null axes. PMd latent activity is projected on each to give potent and null activity.\n# M4 GLMs: Poisson GLMs with exponential link fit with glmfit (no regularization) on 50 ms bins.\n#    Kinematic covariates, in every model: endpoint position, velocity and acceleration,\n#    downsampled to 20 Hz, shifted by three bins (150 ms) and convolved with raised cosine bases\n#    centered at 0 and 100 ms. Basic model = kinematics only; Full model = kinematics plus neural\n#    inputs. Full models: M1-M1 and PMd-PMd (latent activity of the same area recomputed without the\n#    predicted neuron), PC-M1 (all PMd latent activity, called PMd-M1 in places), Pot-M1 and Null-M1\n#    (PMd potent or null activity predicting M1 neurons), and the single-neuron controls M1sn-M1,\n#    PMdsn-PMd, PMdsn-M1. Only neurons above 5 Hz.\n# M5 Performance: pseudo-R2 (pR2, Equation 9) and relative pseudo-R2 of Full against Basic (rpR2,\n#    Equation 12) from Poisson log-likelihoods; 95% bounds by bootstrap with 1000 resamples.\n# M6 Training and testing: models trained on the last 50% of the Force or Rotation epoch, reward\n#    trials only, with ten-fold cross-validation; tested on single trials from the start of the\n#    same epoch. For Washout (Figures 5, 7F) models are trained on Baseline and tested on Washout.\n#    Neurons kept when the Basic pR2 and the rpR2 lower bounds are above zero in all ten folds\n#    (Selecting cells with significant GLM predictions).\n# M7 Model error: on each test trial the rpR2 minus the rpR2 of a fixed Late block of eight\n#    consecutive trials (around 70 trials from the start of the epoch), divided by the\n#    cross-validated training rpR2, in percent; zero in Late by construction (Calculating GLM\n#    error). Early is the block starting at the first perturbation trial (Figure 3C legend).\n# M8 Tests: GLM comparisons at p = 0.01 (Results, Curl field adaptation is not associated ...,\n#    paragraph 1); Kolmogorov-Smirnov test on rpR2 values for Figures 3E and S5F; two-sample t-test\n#    on the normalized change in rpR2 (model error) for Early against Late; all tests two-sided\n#    (Quantification and statistical analysis).\n#\n# Details none of the sources fixes, with the readings the text allows. Each criterion that uses\n# one says so; the notebook runs every reading, and when they disagree the claim is blocked as\n# methods_underspecified.\n# O1 Early and Late blocks in Force and Rotation. Early begins at the first perturbation trial;\n#    its length is not given for these epochs (eight trials in Washout, Figure 5 legend). Late is\n#    eight consecutive trials \"around 70 trials from the start\". Readings: Early = first 8 trials;\n#    Late = trials 66 to 73 or trials 70 to 77; trials counted (a) over reward trials only, as\n#    for training, or (b) over all trials.\n# O2 Washout blocks: Early = first eight Washout trials; Late = \"eight trials taken later in\n#    Washout\", closer in time than in Force, position not given. Readings: Late Washout = trials\n#    21 to 28, 31 to 38 or 41 to 48 of Washout.\n# O3 The part of each trial used for PCA, the subspaces and the GLMs is not given. Readings: (a)\n#    target presentation to target acquisition, as in the covariance analysis; (b) the whole\n#    trial, start to end.\n# O4 Gaussian kernel \"width 100 ms\": readings (a) standard deviation 100 ms; (b) full width at half\n#    maximum 100 ms. Not expected to change an outcome.\n# O5 Unit of the model-error t-test (M7, M8). Late is zero by construction for the block mean, yet\n#    Figures 3G, 4D, 5B and 7E show spread in Late. Readings: (a) single-trial model errors of all\n#    neurons in the block, pooled across sessions, Early against Late, two-sample t-test; (b) one\n#    value per neuron per block (mean over the block's trials), Early against Late, two-sample\n#    t-test, with the one-sample t-test of Early against zero shown as a variant.\n# O6 Raised cosine bases: widths not given (the paper adapts Pillow et al. 2008, \"bases further back\n#    in history become wider\"). Standard choice: Pillow-form raised cosines with peaks at 0 and\n#    100 ms and spacing 100 ms. The 150 ms shift is read as kinematics lagging neural activity\n#    (neural activity at time t paired with kinematics at t + 150 ms), as \"transmission delays\n#    between cortical activity and the motor output\" implies.\n# O7 Subspace rows. The Methods text says the first N rows of V' are potent and the remaining R - N\n#    null, with N = 16 PMd and R = 8 M1 dimensions, which cannot be; the reading is first R = 8 rows\n#    potent, last N - R = 8 null (the only one consistent with \"equal dimensionality\", Results).\n#    W is fit by ordinary least squares at zero lag (not stated; standard choice).\n# O8 rpR2 bootstrap resampling unit not given. Readings: (a) time bins; (b) trials.\n# O9 Dimensionality (Figure 3B). Readings for the threshold: (a) the number of principal components\n#    whose variance exceeds the 99th percentile of the matching noise eigenvalue (Results wording);\n#    (b) the number of components needed to explain 95% of the variance left after subtracting\n#    the noise variance (Methods wording). Data: trial-averaged rates per target in Baseline\n#    (the noise is \"across targets\"), window as O3.\n# O10 Movement onset (M1) not defined. Readings: hand speed first crossing (a) 10%, (b) 20% or\n#    (c) 30% of the trial's peak speed after the go cue.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000688\"\npaper: doi:10.1016/j.neuron.2018.09.030\nclaims:\n- id: methods-neuron-counts\n  statement: Per session, 137 to 256 PMd and 55 to 93 M1 neurons were isolated in Monkey C and 66\n    to 121 PMd and 26 to 51 M1 neurons in Monkey M; neurons above 5 Hz, pooled over all CF and VR\n    sessions, number 918 in M1 and 2221 in PMd.\n  source: STAR Methods, Neural recordings, paragraph 2\n  quote: Across all sessions, we isolated between 137 - 256 PMd and 55 - 93 M1 neurons for Monkey\n    C, and 66 - 121 PMd and 26 - 51 M1 neurons for Monkey M ... Pooled across all monkeys and CF and\n    VR sessions, this gave a population of 918 M1 and 2221 PMd neurons\n  expected:\n  - quantity: PMd neurons per session, Monkey C, range 137 to 256 (lower bound)\n    value: 137\n    tolerance: 13.7\n  - quantity: PMd neurons per session, Monkey C, range 137 to 256 (upper bound)\n    value: 256\n    tolerance: 25.6\n  - quantity: M1 neurons per session, Monkey C, range 55 to 93 (lower bound)\n    value: 55\n    tolerance: 5.5\n  - quantity: M1 neurons per session, Monkey C, range 55 to 93 (upper bound)\n    value: 93\n    tolerance: 9.3\n  - quantity: PMd neurons per session, Monkey M, range 66 to 121 (lower bound)\n    value: 66\n    tolerance: 6.6\n  - quantity: PMd neurons per session, Monkey M, range 66 to 121 (upper bound)\n    value: 121\n    tolerance: 12.1\n  - quantity: M1 neurons per session, Monkey M, range 26 to 51 (lower bound)\n    value: 26\n    tolerance: 2.6\n  - quantity: M1 neurons per session, Monkey M, range 26 to 51 (upper bound)\n    value: 51\n    tolerance: 5.1\n  - quantity: M1 neurons above 5 Hz, all CF and VR sessions pooled\n    value: 918\n    tolerance: 91.8\n  - quantity: PMd neurons above 5 Hz, all CF and VR sessions pooled\n    value: 2221\n    tolerance: 222.1\n  criterion: Units as sorted in the data, per area and session, for the 9 CF and 7 VR sessions.\n    Each per-session count must lie in its monkey's range widened by 10% of each bound. The 5 Hz\n    rule is the trial-averaged mean rate over all trials of the session (Methods do not say which\n    trials; reading as stated). Reproduced when all ranges and both pooled counts hold; partially\n    reproduced when the ranges hold and a pooled count does not.\n- id: fig2d-cf-behavioral-adaptation\n  statement: On exposure to the curl field the monkeys made large reach direction errors that\n    shrank gradually until behavior stabilized, and mirror-image after-effects appeared at the\n    start of Washout.\n  source: Results, Curl field adaptation involves widespread ..., paragraph 1; Figure 2C and 2D\n  quote: Within each session, the monkeys exhibited large errors upon exposure to the CF, which were\n    gradually reduced until behavior stabilized ... Further evidence of adaptation was revealed by\n    behavioral after-effects (mirror image errors) that occurred upon return to normal reaching\n    during the Washout epoch\n  criterion: Error as M1 (movement onset per O10), CW sessions sign-flipped. The paper gives no\n    test. Per session, the mean error of the Early block, of the Late block (O1 readings) and of\n    the first eight Washout trials (Figure 5 legend). Reproduced when, across the 9 CF sessions,\n    the Early mean exceeds the Late mean in at least 8 sessions and is greater by a two-sided\n    paired t-test at p < 0.05, and the first eight Washout trials have a mean error of opposite\n    sign to the Early Force error in at least 8 sessions. The thresholds of 8 of 9 sessions and the\n    t-test are the reader's operational reading of \"large errors ... gradually reduced\" and are\n    recorded as a deviation; the session medians are shown.\n- id: fig7bc-vr-behavior-similar\n  statement: In VR sessions behavioral errors were similar in magnitude and time course to those of\n    CF sessions, with large initial errors in Rotation and strong after-effects in Washout.\n  source: Results, PMd to M1 mapping is unchanged throughout adaptation to a visuomotor rotation,\n    paragraph 2; Figure 7B and 7C\n  quote: In many respects, adaptation during the CF and VR sessions was quite similar. Behavioral\n    errors were similar in magnitude and time course\n  depends_on:\n  - fig2d-cf-behavioral-adaptation\n  criterion: As fig2d-cf-behavioral-adaptation for the 7 VR sessions (Rotation in place of Force).\n    Reproduced when the VR sessions meet the same rule and a two-sided two-sample t-test of\n    per-session Early errors, VR against CF, gives p >= 0.05 (no test is given by the paper for\n    \"similar\"; this reading is recorded as a deviation and the medians of both are shown).\n- id: figs2-covariance-preserved-example\n  statement: In a representative CF session, the pairwise covariance of neurons in the Force and\n    Washout blocks correlated with Baseline values at r of at least 0.85 in M1 and at least 0.93 in\n    PMd.\n  source: Results, Models to study adaptation-related changes ..., paragraph 2; Figure S2E\n  quote: for a representative session - Pearson's correlation with Baseline values r >= 0.85 for M1\n    and r >= 0.93 for PMd\n  expected:\n  - quantity: minimum r with Baseline over blocks, M1, representative session\n    value: 0.85\n    tolerance: 0.085\n  - quantity: minimum r with Baseline over blocks, PMd, representative session\n    value: 0.93\n    tolerance: 0.093\n  criterion: Method from STAR Methods, Single neuron covariance. Neurons above 1 Hz; spikes in 10 ms\n    bins from target presentation to target acquisition; five blocks (Baseline split in two, Force\n    split in two, Washout); in each block trials averaged per target; covariance between all pairs\n    of neurons; Pearson r between each block's covariances and the Baseline covariances (Figure S2D\n    legend, the two Baseline halves compared with each other and the Force and Washout blocks with\n    the full Baseline). The representative session is the Monkey C session of Figures S2 and S6A,\n    which the paper does not name; every CF session is computed. Open (deviation) whether the\n    diagonal (variances) enters the correlation; both are run. Reproduced when at least one CF\n    session has all its block r values at or above 0.85 - 0.085 in M1 and 0.93 - 0.093 in PMd.\n- id: figs3a-covariance-like-baseline-split\n  statement: Across all CF sessions the similarity of the covariance between Baseline and the Force\n    and Washout blocks resembled that between random subsamples of Baseline, so the covariance\n    structure did not change with adaptation.\n  source: Results, Models to study adaptation-related changes ..., paragraph 2; Figure S3A\n  quote: Across all sessions, the differences in covariance strongly resembled those obtained from\n    random subsamples of Baseline data for which the covariance structure should be unchanged\n  depends_on:\n  - figs2-covariance-preserved-example\n  criterion: Covariance as figs2-covariance-preserved-example; the reference distribution from\n    random subsamples of Baseline trials, compared with each other, 100 times per session (STAR\n    Methods, Single neuron covariance; subsample size not given, readings half and half of\n    Baseline). The paper gives no test. Reading recorded as a deviation; reproduced when, in each\n    area, the median over sessions of the Force 1, Force 2 and Washout r values lies inside the\n    range of the pooled Baseline-split r values, and partially reproduced when that holds for one\n    area only. The distributions are shown.\n- id: figs3b-covariance-preserved-vr\n  statement: In VR sessions as well, the changes in neural activity preserved the population\n    covariance structure.\n  source: Results, PMd to M1 mapping is unchanged throughout adaptation to a visuomotor rotation,\n    paragraph 2; Figure S3B\n  quote: Additionally, changes in neural activity preserved the population covariance structure\n  depends_on:\n  - figs3a-covariance-like-baseline-split\n  criterion: As figs3a-covariance-like-baseline-split for the 7 VR sessions (Rotation blocks in\n    place of Force).\n- id: fig3b-pmd-higher-dimensional\n  statement: In every session the PMd manifold had more dimensions than the M1 manifold (median 14\n    against 8.5).\n  source: Results, Models to study adaptation-related changes ..., paragraph 3; Figure 3B\n  quote: In all sessions, the PMd manifold contained more dimensions than did the M1 manifold ...\n    M1 median, 8.5; PMd median, 14\n  expected:\n  - quantity: median M1 dimensionality across sessions\n    value: 8.5\n    tolerance: 0.85\n  - quantity: median PMd dimensionality across sessions\n    value: 14\n    tolerance: 1.4\n  criterion: Dimensionality by the method adapted from Machens et al. 2010 (STAR Methods,\n    Dimensionality reduction, paragraph 2) on rates as M2; noise from differences between random\n    pairs of trials to the same target, 1000 repetitions, 99% limit of each noise eigenvalue;\n    threshold rule and data as O9, window as O3. Over all 16 sessions (Figure 3B legend, \"all\n    sessions from both monkeys\"). Reproduced when, under one reading, PMd exceeds M1 in every\n    session and both medians are within tolerance; partially reproduced when PMd exceeds M1 in\n    every session and a median is outside tolerance.\n- id: figs4d-dimensionality-robust-to-size\n  statement: With random subsamples of equal, fixed numbers of neurons, estimated dimensionality\n    fell for small samples but PMd stayed higher-dimensional than M1 for every neuron count tested.\n  source: Figure S4D legend; STAR Methods, Dimensionality reduction, paragraph 2\n  quote: With decreasing neuron counts, we began to underestimate the apparent dimensionality.\n    However, critically, PMd (red) was consistently higher dimensional than M1 (black) for all\n    tested neuron counts\n  depends_on:\n  - fig3b-pmd-higher-dimensional\n  criterion: As fig3b-pmd-higher-dimensional, on random subsamples of 40, 50, 60 and 70 neurons per\n    area and all neurons (the counts on the Figure S4D axis), mean over sessions. Number of\n    subsamples per size not given; standard choice of 100 (cannot change the sign of the\n    comparison in expectation). Sessions with fewer neurons than a size are left out of that size\n    (open; deviation). Reproduced when the PMd mean exceeds the M1 mean at every size.\n- id: figs4c-null-potent-index-centered\n  statement: Single neurons contributed to both output-potent and output-null subspaces; the\n    null/potent index was centered on zero with virtually no neurons near -1 or 1.\n  source: Figure S4C legend; STAR Methods, Output-potent and output-null subspaces, paragraph 3\n  quote: The distribution of neurons was centered around zero and virtually no neurons had a\n    null/potent index close to -1 / 1, indicating that the output-potent and output-null subspaces\n    captured population-wide features\n  criterion: Index per PMd neuron from the product of the PCA loading matrix and V (M2, M3, O7) as\n    (sum of absolute potent weights - sum of absolute null weights) / (sum of both). \"Magnitude\"\n    is read as the sum of absolute values; the sum of squares is the second reading. Reproduced when\n    the mean index over neurons lies between -0.1 and 0.1 and fewer than 1% of neurons have an\n    absolute index above 0.9 (the reader's reading of \"centered\" and \"virtually no\", recorded as a\n    deviation); the shuffled control is shown.\n- id: figs5e-glm-cell-counts\n  statement: In the CF sessions pooled, the number of M1 or PMd neurons with significant GLM fits\n    was 214 for M1-M1, 338 for PMd-PMd, 170 for PC-M1, 144 for Pot-M1 and 97 for Null-M1; the\n    Basic model was significant for 522 of 918 M1 and 612 of 2221 PMd neurons.\n  source: Figures 3C and S5E (cell counts in the panels); STAR Methods, Selecting cells with\n    significant GLM predictions\n  quote: This reduced the pool of candidate cells to 522 of 918 (57%) in M1 and 612 of 2221 (28%)\n    in PMd\n  expected:\n  - quantity: M1 neurons with significant Basic pR2 (all sessions)\n    value: 522\n    tolerance: 52.2\n  - quantity: PMd neurons with significant Basic pR2 (all sessions)\n    value: 612\n    tolerance: 61.2\n  - quantity: M1-M1 significant cells, CF sessions\n    value: 214\n    tolerance: 21.4\n  - quantity: PMd-PMd significant cells, CF sessions\n    value: 338\n    tolerance: 33.8\n  - quantity: PC-M1 significant cells, CF sessions\n    value: 170\n    tolerance: 17\n  - quantity: Pot-M1 significant cells, CF sessions\n    value: 144\n    tolerance: 14.4\n  - quantity: Null-M1 significant cells, CF sessions\n    value: 97\n    tolerance: 9.7\n  criterion: Selection as M6 with M2 to M5; readings O3, O6, O8. The Basic counts are read as over\n    all CF and VR sessions (the denominators 918 and 2221 are the pooled counts); the per-model\n    counts are over the nine CF sessions (Figure 3C legend, \"pooled across nine sessions\").\n    Reproduced when, under one reading, all seven counts are within tolerance; partially\n    reproduced when at least four are.\n- id: figs5e-pot-null-similar-training\n  statement: Pot-M1 and Null-M1 had similar cross-validated accuracy within the end-of-Force\n    training trials.\n  source: Results, Output-potent activity in PMd consistently predicts M1 neurons ..., paragraph 2;\n    Figure S5E\n  quote: Both models had similar accuracy when evaluated within the end-of-Force training trials\n    using ten-fold crossvalidation\n  depends_on:\n  - figs5e-glm-cell-counts\n  criterion: Cross-validated rpR2 of the selected cells for Pot-M1 and Null-M1 in the CF sessions\n    (M6). The paper gives no test for \"similar\"; the test it uses for rpR2 distributions is the\n    two-sided Kolmogorov-Smirnov test at p = 0.01 (M8), taken here. A claim of absence;\n    reproduced when that test does not find a difference, with medians of both shown.\n- id: fig3e-local-rpr2-unchanged\n  statement: The rpR2 distributions of the within-area models M1-M1 and PMd-PMd did not differ\n    between Early and Late Force trials (Kolmogorov-Smirnov p = 0.72 and p = 0.19).\n  source: Figure 3E (p-values in the panel); Results, Curl field adaptation is not associated ...,\n    paragraph 2\n  quote: M1-M1 and PMd-PMd had similar distributions during Early and Late\n  statistics:\n  - about: M1-M1, Early against Late Force rpR2\n    test: Kolmogorov-Smirnov test\n    p: 0.72\n    n: 214 M1 cells, nine CF sessions\n  - about: PMd-PMd, Early against Late Force rpR2\n    test: Kolmogorov-Smirnov test\n    p: 0.19\n    n: 338 PMd cells, nine CF sessions\n  depends_on:\n  - figs5e-glm-cell-counts\n  criterion: Per selected cell, rpR2 of the trained model (M6) on the Early and on the Late block\n    (O1; rpR2 computed over the block's bins together), pooled over the nine CF sessions; two-sided\n    two-sample Kolmogorov-Smirnov test (M8) at p = 0.01. A claim of absence: reproduced when the\n    test is not significant for both models under every reading, not reproduced when it is\n    significant for either; p-values and medians shown.\n- id: fig3g-local-models-generalize\n  statement: Model error of M1-M1 and PMd-PMd did not differ between Early and Late Force; the\n    local models generalized throughout CF adaptation.\n  source: Figure 3G (legend \"No effects were significant (two-sample t-test)\"); Results, Curl field\n    adaptation is not associated ..., paragraph 2\n  quote: We found that both within-area models ( M1 -M1, PMd -PMd) generalized well, predicting the\n    adaptation-related changes in single-neuron spiking nearly equally well in both blocks\n  statistics:\n  - test: two-sample t-test\n    p: 0.01\n    p_relation: \">\"\n    n: 214 M1-M1 and 338 PMd-PMd cells, nine CF sessions\n  depends_on:\n  - figs5e-glm-cell-counts\n  criterion: Model error as M7 (O1, O5), Early against Late, two-sided two-sample t-test at p =\n    0.01 (M8), per model. A claim of absence, judged on this test; reproduced when neither model\n    differs, not reproduced when either does; the mean errors are shown.\n- id: fig4d-null-m1-fails-early\n  statement: Null-M1 generalized significantly worse in Early than in Late Force, while Pot-M1\n    generalized well in both blocks.\n  source: Figure 4D legend (Results cite it as Figure 4E); Results, Output-potent activity in PMd\n    consistently predicts M1 neurons ..., paragraph 2\n  quote: The Pot -M1 model generalized well throughout learning, making accurate predictions in\n    Early Force as well as Late Force ... However, the Null -M1 model generalized significantly\n    worse in the Early block than in the Late block\n  statistics:\n  - about: Null-M1, Early against Late Force model error\n    test: two-sample t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 97 M1 cells, nine CF sessions\n  depends_on:\n  - figs5e-glm-cell-counts\n  criterion: Model error as M7 (O1, O5), Early against Late, two-sided two-sample t-test at p = 0.01\n    (M8), with subspaces from M3 (O7). Reproduced when, under every reading, Null-M1 has a\n    significantly larger Early error and Pot-M1 has no significant difference; partially\n    reproduced when the Null-M1 effect holds and Pot-M1 also differs; not reproduced when Null-M1\n    does not differ. Readings that disagree block the claim.\n- id: fig4c-null-tracks-behavior\n  statement: The Null-M1 model error changed over Force trials with a time course similar to that\n    of behavioral adaptation, while Pot-M1 stayed near zero.\n  source: Figure 4C; Results, Output-potent activity in PMd consistently predicts M1 neurons ...,\n    paragraph 2\n  quote: Interestingly, the Null-M1 error alone paralleled the time course of behavior\n  depends_on:\n  - fig4d-null-m1-fails-early\n  criterion: Single-trial model errors (M7) averaged over cells and smoothed with a 30-trial moving\n    average, with the start padded with NaNs of half the window (STAR Methods, Evaluating GLM\n    performance, paragraph 3); behavioral error (M1) smoothed the same way. The paper compares\n    the curves by eye. Reading recorded as a deviation; reproduced when the Pearson correlation\n    across Force trials between the smoothed behavioral error and the Null-M1 curve is positive\n    and larger than that for Pot-M1, and partially reproduced when only the first holds.\n- id: figs6-pc-m1-fails\n  statement: PC-M1, with all PMd latent activity as input, also failed to generalize during CF\n    adaptation, its accuracy changing with a time course like that of behavior.\n  source: Results, Output-potent activity in PMd consistently predicts M1 neurons ..., paragraph 3;\n    Figure S6 (pink)\n  quote: Since PC- M1 contained all of the output-potent and output-null subspace activity, we\n    expected that, similarly to Null -M1, it would fail to generalize during adaptation. Indeed, its\n    accuracy changed progressively during adaptation\n  depends_on:\n  - figs5e-glm-cell-counts\n  criterion: As fig4d-null-m1-fails-early for PC-M1. Reproduced when the Early model error is\n    significantly larger than Late at p = 0.01.\n- id: figs6de-per-monkey\n  statement: In each monkey separately, only Null-M1 and PC-M1 had significantly larger model error\n    in Early than in Late Force; M1-M1, PMd-PMd and Pot-M1 did not.\n  source: Figure S6D and S6E (asterisks)\n  inferred: Read from the asterisks of Figure S6D and S6E, whose legend says asterisks mark Early\n    against Late differences at p < 0.01 (two-sample t-test); no sentence names the models.\n  statistics:\n  - about: Null-M1 and PC-M1, Early against Late, each monkey\n    test: two-sample t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: Monkey C five CF sessions, Monkey M four CF sessions\n  depends_on:\n  - fig4d-null-m1-fails-early\n  criterion: As fig4d-null-m1-fails-early, run for each monkey's CF sessions apart, five models.\n    Reproduced when, in both monkeys, Null-M1 and PC-M1 are significant at p = 0.01 and the other\n    three are not; partially reproduced when that holds in one monkey.\n- id: figs5f-rpr2-distributions\n  statement: Of the unnormalized rpR2 distributions of the five models in Early against Late CF\n    trials, only Null-M1 (p = 0.04) and PC-M1 (p = 0.01) changed; Pot-M1 (p = 0.40), M1-M1 (p =\n    0.72) and PMd-PMd (p = 0.19) did not.\n  source: Figure S5F (legend and p-values in the panel)\n  quote: Distribution of unprocessed rpR2 values for all predicted neurons for the five GLM models\n    during Early and Late CF adaptation. Only Null-M1 and PMd-M1 were significantly changed between\n    the two periods\n  statistics:\n  - about: Null-M1\n    test: Kolmogorov-Smirnov test\n    p: 0.04\n    n: 97 cells\n  - about: PC-M1 (PMd-M1)\n    test: Kolmogorov-Smirnov test\n    p: 0.01\n    n: 170 cells\n  - about: Pot-M1\n    test: Kolmogorov-Smirnov test\n    p: 0.4\n    n: 144 cells\n  depends_on:\n  - fig3e-local-rpr2-unchanged\n  criterion: As fig3e-local-rpr2-unchanged for the five models. The legend calls Null-M1\n    significant at p = 0.04, above the paper's own threshold of 0.01 (M8); the criterion uses p <\n    0.05 for this panel, the level at which the legend's statement holds, and also reports the\n    outcome at 0.01. Reproduced when Null-M1 and PC-M1 differ at p < 0.05 and Pot-M1, M1-M1 and\n    PMd-PMd do not; partially reproduced when PC-M1 and Null-M1 differ and one other model also\n    does.\n- id: figs7a-unnormalized-change\n  statement: Without normalization by cross-validated performance, the change in rpR2 between\n    Early and Late CF was significant only for Null-M1 (p = 0.01) and PC-M1 (p = 0.00); in VR no\n    model changed (p from 0.28 to 0.80).\n  source: Figure S7A and S7B (legend and p-values in the panels)\n  quote: The distributions of change in rpR2 for the curl field sessions, but without the\n    normalization by the cross-validated performance. Asterisks indicate significance at p < 0.01.\n    (B) Same as Panel A, but for the visuomotor rotation sessions. There were no significant\n    differences in the models\n  statistics:\n  - about: CF, M1-M1\n    p: 0.13\n  - about: CF, PMd-PMd\n    p: 0.44\n  - about: CF, Pot-M1\n    p: 0.54\n  - about: CF, Null-M1\n    p: 0.01\n  - about: CF, PC-M1\n    p: 0\n  - about: VR, M1-M1\n    p: 0.33\n  - about: VR, PMd-PMd\n    p: 0.62\n  - about: VR, Pot-M1\n    p: 0.28\n  - about: VR, Null-M1\n    p: 0.72\n  - about: VR, PC-M1\n    p: 0.8\n  depends_on:\n  - fig3g-local-models-generalize\n  criterion: As M7 without dividing by the cross-validated rpR2 (O1, O5), Early against Late,\n    two-sided two-sample t-test (the test M8 gives for model-error comparisons; the panel does not\n    name it). The panel marks Null-M1 at p = 0.01 as significant at \"p < 0.01\"; read as p <= 0.01.\n    Reproduced when, in CF, Null-M1 and PC-M1 are significant and the other three are not, and in\n    VR none is; partially reproduced when the CF pattern holds and a VR model is significant.\n- id: figs7e-dimensionality-range\n  statement: The Null-M1 failure and Pot-M1 generalization held for M1 dimensionalities from 7 to\n    20 (PMd twice that); Null-M1 was significant at all tested values except 9, Pot-M1 at none.\n  source: Figure S7E; STAR Methods, Controls for the output-potent and output-null subspaces;\n    Results, Output-potent activity in PMd consistently predicts M1 neurons ..., paragraph 3\n  quote: Our primary effect that Pot-M1, and not Null-M1, generalizes to early CF trials held for a\n    wide range of dimensionalities\n  statistics:\n  - test: two-sample t-test\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - fig4d-null-m1-fails-early\n  criterion: As fig4d-null-m1-fails-early with M1 dimensionality 7, 8, 9, 10, 11, 12, 15 and 20\n    and PMd twice that (the values on the Figure S7E axis; the Methods say 5 to 20). Reproduced when\n    Null-M1 is significant at p = 0.01 for at least six of the eight values and Pot-M1 for none;\n    partially reproduced when Null-M1 is significant for at least four (the figure shows seven of\n    eight; the thresholds are the reader's reading of \"a wide range\", a deviation).\n- id: figs7f-factor-analysis\n  statement: The main result held with Factor Analysis in place of PCA; in CF only Null-M1 and PC-M1\n    had larger Early error, and in VR no model did.\n  source: Figure S7F; Results, Output-potent activity in PMd consistently predicts M1 neurons ...,\n    paragraph 3\n  quote: We thus replicated these main results using Factor Analysis, another common method for\n    dimensionality reduction of neural data, instead of PCA\n  depends_on:\n  - fig4d-null-m1-fails-early\n  criterion: As fig4d-null-m1-fails-early and fig7de-vr-all-generalize, with latent activity from\n    Factor Analysis (factoran, 8 M1 and 16 PMd factors; STAR Methods, Dimensionality reduction)\n    in place of PCA. Reproduced when in CF Null-M1 and PC-M1 are significant at p = 0.01 and\n    M1-M1, PMd-PMd and Pot-M1 are not, and in VR none is.\n- id: figs7cd-single-neuron-models\n  statement: With single-neuron spiking as inputs, M1sn-M1 and PMdsn-PMd generalized well through\n    CF adaptation while PMdsn-M1 did not, in each monkey; in Washout, PMdsn-M1 alone showed\n    de-adaptation in CF (p = 0.00), and no model changed in VR.\n  source: Figure S7C and S7D; Results, Output-potent activity in PMd consistently predicts M1\n    neurons ..., paragraph 3\n  quote: Indeed, the local models ( M1sn -M1, PMdsn PMd) generalized well throughout adaptation,\n    while the between area model ( PMdsn -M1) did not\n  statistics:\n  - about: Washout CF, M1sn-M1\n    p: 0.25\n  - about: Washout CF, PMdsn-PMd\n    p: 0.15\n  - about: Washout CF, PMdsn-M1\n    p: 0\n  - about: Washout VR, M1sn-M1\n    p: 0.07\n  - about: Washout VR, PMdsn-PMd\n    p: 0.64\n  - about: Washout VR, PMdsn-M1\n    p: 0.6\n  depends_on:\n  - fig4d-null-m1-fails-early\n  - fig5-washout-null-m1\n  criterion: Models as M4 with all other single neurons of the area as inputs (M1sn-M1, PMdsn-PMd)\n    or all PMd neurons (PMdsn-M1); Force as fig4d-null-m1-fails-early per monkey, Washout as\n    fig5-washout-null-m1. Reproduced when PMdsn-M1 alone is significant at p = 0.01 in Force in\n    both monkeys and in CF Washout, and no model is in VR Washout; partially reproduced when the\n    Force result holds and the Washout result does not.\n- id: fig5-washout-null-m1\n  statement: Models trained on Baseline predicted the first eight Washout trials worse than later\n    Washout trials for Null-M1 only; Pot-M1 predicted both blocks well.\n  source: Figure 5B; Results, Output-potent activity in PMd consistently predicts M1 neurons ...,\n    paragraph 4\n  quote: We found that Null -M1 generalized poorly in the earliest trials, then rapidly improved\n    with de-adaptation as output-null activity began to return to Baseline. There was no such effect\n    for the Pot -M1 model, which accurately predicted both early and late Washout trials\n  statistics:\n  - about: Null-M1, Early against Late Washout model error\n    test: two-sample t-test\n    p: 0.01\n    p_relation: \"<\"\n  criterion: Models trained on Baseline trials (M6), tested on Washout; model error as M7 with the\n    Washout blocks of O2; cells selected as M6 on the Baseline training data. Two-sided two-sample\n    t-test at p = 0.01, O5 readings. Reproduced when Null-M1 Early error is significantly larger\n    and Pot-M1 does not differ, under every reading.\n- id: fig6c-null-leads-potent\n  statement: In Baseline, output-null activity preceded output-potent activity by 35 ms on average\n    across the 16 sessions, a lag significantly below zero (t-test, p = 0.02), and output-null also\n    led at the end of Force.\n  source: Figure 6B and 6C (legend's first \"d\"); Results, Evolving changes in PMd output-null\n    planning activity ..., paragraph 1\n  quote: Output-null activity preceded output-potent by 35 ms on average, and the distribution was\n    significantly negative (t-test; p = 0.02)\n  statistics:\n  - test: t-test\n    p: 0.02\n    n: 16 CF and VR sessions\n  expected:\n  - quantity: mean lag of output-potent relative to output-null, Baseline\n    value: -35\n    tolerance: 3.5\n    unit: ms\n  criterion: Method from STAR Methods, Calculating the lag. Baseline trials, a 700 ms window\n    after target presentation, potent and null activity (M3, O7) shifted relative to each other\n    by -350 to 350 ms in 10 ms steps, CCA at each lag, the lag of maximum first canonical\n    correlation per session. Open (deviations) - the time resolution (readings (a) latent activity\n    from 10 ms bins, smoothed as M2; (b) 50 ms latent activity interpolated to 10 ms) and trials\n    concatenated within a session. The t-test is read as one-sample against zero, two-sided.\n    Reproduced when, under one reading, the mean lag is negative with p < 0.05 and within 3.5 ms\n    of -35 ms; partially reproduced when the lag is significantly negative and outside tolerance.\n    The end-of-Force lags (9 CF sessions) are reported, with their mean sign.\n- id: fig6e-planning-change-in-null\n  statement: Changes in preparatory (planning) activity from Baseline were largely confined to the\n    output-null subspace and grew significantly from Early to Late Force; in the movement window,\n    M1 activity changed significantly more in Late Force.\n  source: Figure 6D and 6E; Results, Evolving changes in PMd output-null planning activity ...,\n    paragraph 2\n  quote: Changes in preparatory activity were largely confined to the output-null subspace.\n    Furthermore, the amount of this altered preparatory activity increased significantly between\n    Early and Late adaptation\n  statistics:\n  - about: Null subspace, planning window, Early against Late Force\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Method from STAR Methods, Quantifying changes in neural state space activity. Trials\n    aligned on go cue, latent activity in 20 ms bins for M1 (8 dimensions) and PMd potent and null\n    subspaces; at each time point the Mahalanobis distance (MATLAB mahal) of each Force trial from\n    all Baseline reaches to the same target; normalized by subtracting the value at a reference\n    point and dividing by the maximum over the adaptation period. Open (deviations) - the reference\n    point (readings the first bin of the window, 0.5 s before go cue, or the go cue); the planning\n    and movement windows, not given in the text (read from the bars of Figure 6D, about -0.15 to\n    0 s and 0.25 to 0.45 s from go cue); the blocks, labeled Force 1 and Force 4 in the panel\n    (read as the first and last quarter of Force; the O1 Early and Late blocks as the second\n    reading); the test, not named (two-sided two-sample t-test over trials, session values as a\n    second reading). Reproduced when, under every reading, the null planning change is larger in\n    Force 4 at p < 0.05 and exceeds the potent and M1 planning changes in Force 4.\n- id: fig7de-vr-all-generalize\n  statement: During VR adaptation all four GLM models, including Null-M1, generalized to Early and\n    Late Rotation trials, with no significant change in model error.\n  source: Figure 7D and 7E; Results, PMd to M1 mapping is unchanged ..., paragraph 2\n  quote: However, all GLM models, including Null -M1, accurately generalized throughout Rotation\n  statistics:\n  - test: two-sample t-test\n    p: 0.01\n    p_relation: \">\"\n    n: seven VR sessions\n  criterion: As fig3g-local-models-generalize and fig4d-null-m1-fails-early for the seven VR\n    sessions (Rotation epoch), M1-M1, PMd-PMd, Pot-M1 and Null-M1. A claim of absence, judged on\n    the paper's test (two-sided two-sample t-test at p = 0.01); reproduced when no model differs\n    between Early and Late, not reproduced when any does.\n- id: fig7f-vr-washout-unchanged\n  statement: In VR Washout neither Pot-M1 nor Null-M1 showed a change in performance during\n    de-adaptation, despite behavioral after-effects.\n  source: Figure 7F; Results, PMd to M1 mapping is unchanged ..., paragraph 2\n  quote: Furthermore, we did not see any effect of de-adaptation in the neural predictions during\n    Washout, despite the presence of behavioral after-effects\n  depends_on:\n  - fig5-washout-null-m1\n  criterion: As fig5-washout-null-m1 for the seven VR sessions. A claim of absence; reproduced when\n    neither model differs at p = 0.01, not reproduced when either does.\n- id: cf-vr-dissociation\n  statement: The Null-M1 failure to generalize is specific to CF adaptation; it is absent in VR\n    adaptation of similar behavioral magnitude, so it is not a necessary consequence of changing\n    behavior.\n  source: Results, PMd to M1 mapping is unchanged ..., paragraph 2; Discussion, Visuomotor rotation\n    and curl field likely employ distinct adaptive processes\n  quote: This result highlights a fundamental difference in the neural adaptation to these two\n    perturbations\n  depends_on:\n  - fig4d-null-m1-fails-early\n  - fig5-washout-null-m1\n  - fig7de-vr-all-generalize\n  - fig7f-vr-washout-unchanged\n  - fig7bc-vr-behavior-similar\n  criterion: Reproduced when fig4d-null-m1-fails-early and fig7de-vr-all-generalize are both\n    reproduced; partially reproduced when they are and fig7bc-vr-behavior-similar is not.\n"
}
```

```
File created successfully at: claims/000688/10.1016-j.neuron.2018.09.030.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000688/10.1016-j.neuron.2018.09.030.yaml paper/10.1016-j.neuron.2018.09.030.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/000688/10.1016-j.neuron.2018.09.030.yaml; grep -n "[^ ]: " $f | grep -v "^[0-9]*:#" | grep -vE "^[0-9]+: *(- )?[a-z_]+: "
```

```
366:    two-sample Kolmogorov-Smirnov test (M8) at p = 0.01. A claim of absence: reproduced when the
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000688/10.1016-j.neuron.2018.09.030.yaml",
 "old_string": "A claim of absence: reproduced when the",
 "new_string": "A claim of absence; reproduced when the"
}
```

```
The file claims/000688/10.1016-j.neuron.2018.09.030.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000688/10.1016-j.neuron.2018.09.030.yaml paper/10.1016-j.neuron.2018.09.030.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/000688/10.1016-j.neuron.2018.09.030.yaml; python3 - <<'EOF'
p='claims/000688/10.1016-j.neuron.2018.09.030.yaml'
s=open(p).read()
s=s.replace("r >= 0.85 for M1\n    and r >= 0.93 for PMd","r ≥ 0.85 for M1\n    and r ≥ 0.93 for PMd")
s=s.replace("""  quote: Distribution of unprocessed rpR2 values for all predicted neurons for the five GLM models
    during Early and Late CF adaptation. Only Null-M1 and PMd-M1 were significantly changed between
    the two periods""","""  quote: values for all predicted neurons for the five GLM models during Early and Late CF
    adaptation. Only Null-M1 and PMd-M1 were significantly changed between the two periods""")
s=s.replace("""  quote: The distributions of change in rpR2 for the curl field sessions, but without the
    normalization by the cross-validated performance. Asterisks""","""  quote: The distributions of change in rpR2 for the curl field sessions, but without the
    normalization by the cross-val- ... performance. Asterisks""")
open(p,'w').write(s)
EOF
python tools/claims_check.py $f paper/10.1016-j.neuron.2018.09.030.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/000688/10.1016-j.neuron.2018.09.030.yaml; python3 - <<'EOF'
p='claims/000688/10.1016-j.neuron.2018.09.030.yaml'
s=open(p).read()
s=s.replace("quote: for a representative session - Pearson's","quote: representative session ... Pearson's")
open(p,'w').write(s)
EOF
python tools/claims_check.py $f paper/10.1016-j.neuron.2018.09.030.txt; grep -n -i "rather\|—" $f
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('claims/000688/10.1016-j.neuron.2018.09.030.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

```
28 27 12 29 28 5
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
?? claims/000688/
?? scripts
```

**Agent**

I wrote `claims/000688/10.1016-j.neuron.2018.09.030.yaml`, and the quote checker passes with no problems. Nothing the claims needed was missing, so I wrote the claims.

**Text read:** the accepted author manuscript in PubMed Central (PMC6250582), not the version of record. That covers the main text, legends, STAR Methods and all eight supplement files: files 1 to 7 are the main figures as images, and file 8 holds Figures S1 to S7 with their legends. I opened the PDFs only to read p-values and asterisks printed inside panels (Figures 3E, 4D, 5B, 6C/E, S5F, S6D/E, S7A/D/E). The paper links no code ("may be shared upon reasonable request"), so every method comes from the Methods, legends or Results.

**Claims:**
- **Count:** 28 claims, all 28 with a criterion and 27 with a quote. The one without (per-monkey asterisks in Figure S6D/E) has an `inferred` note.
- **Statistics:** 29 entries across 12 claims.
- **Expected values:** 5 claims. These are neuron counts, GLM cell counts, the dimensionality medians (8.5 and 14), the covariance r values (0.85 and 0.93) and the 35 ms null-leads-potent lag.
- **Data:** every claim uses `dataset`. Whether dandiset 000688 holds the curl field and rotation sessions is for the author to find.

**Details the paper leaves open, with the readings named** (listed as O1 to O10 in the opening comment):
- **O1, Early and Late blocks in Force/Rotation:** Early is the first 8 trials. Late is trials 66 to 73 or 70 to 77. Trials are counted over reward trials only or over all trials.
- **O2, Late Washout block:** Washout trials 21 to 28, 31 to 38 or 41 to 48.
- **O3, part of the trial used for PCA and the GLMs:** target onset to target acquisition, or the whole trial.
- **O4, the 100 ms Gaussian kernel:** read as SD or as full width at half maximum.
- **O5, unit of the model-error t-test:** pooled single-trial values, or one mean per neuron (with a one-sample test against zero as a variant).
- **O6, raised-cosine widths and the 150 ms shift:** standard choices, named as such.
- **O7, subspace rows:** the Methods swap N and R. I read the first 8 rows of V' as potent and the last 8 as null; W is fit by least squares.
- **O8, bootstrap unit:** time bins or trials.
- **O9, dimensionality threshold:** the Results wording (eigenvalues above the noise) or the Methods wording (95% of the variance left after the noise).
- **O10, movement onset:** speed crossing 10%, 20% or 30% of peak.
- **Per-claim open points:** the Figure 6E reference point, windows (read off the figure bars), blocks and test (the test is not named); the CCA time resolution; whether the covariance diagonal is included; and the subsample size for the Baseline-split covariance comparison.
- **Wording claims with no test in the paper:** where the paper only says "similar", "resembled" or "paralleled" (behavior, covariance, Figure 4C time course, Figures S4C, S7E), I wrote thresholds myself and marked each as a deviation.

**Gaps and inconsistencies in the paper:**
- **Session counts:** the Figure 2C and Figure 7 legends show 7 curl field and 5 rotation sessions, but the Methods count 9 and 7.
- **Figure S5F:** the legend calls Null-M1 significant at p = 0.04, above the paper's own 0.01 threshold. That claim reports the outcome at both 0.05 and 0.01.
- **Figure lettering:** the Results' panel letters disagree with the legends (3E/F/G, 4E against 4D, two panels "d" in Figure 6). Each source gives both.
- **No code:** without it, none of the open details above can be settled.

## End of run

40 turns, 6 minutes, result: success.
