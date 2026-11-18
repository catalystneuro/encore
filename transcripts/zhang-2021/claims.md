# zhang-2021 · claims · run 42856578115

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls -la paper/; wc -c claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 43,
 "limit": 156
}
```

```
43	## Reader
44	
45	### 1. Get the paper
46	
47	The workflow puts the paper's full text, and its PDF where there is one, under
48	`paper/`: the main text, the Methods, and the supplement. Read the text; open
49	the PDF only to read a figure or a table the text garbles. If the full text is
50	not there, or lacks the Methods or a supplement the results rest on, stop:
51	write no claims, and end with a report that names what is missing, so that it
52	can be supplied. Never write claims from the abstract. Do not copy figures.
53	Do not look at the dataset's data: its title and description on the archive
54	are enough to know which paper and which experiments it is meant to hold. A
55	data descriptor under `paper/` (`<id>.data-description.txt`, the dataset's own
56	documentation) is a longer description, to be read for that alone; it is not
57	the paper, and no claim comes from it.
58	
59	### 2. Read the paper's code
60	
61	Read the code the paper links to before writing criteria. Say what it holds,
62	and record the repository and commit read. Where the Methods leave a choice
[... 136 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
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

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fnins.2020.565976.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/vim-4.data-description.txt | head -150; cd $TMPDIR && git clone -q https://github.com/gallantlab/state-space && cd state-space && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -50
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper text and supplement are complete. I'm reading the paper's code (gallantlab/state-space, commit 6ffb3c3) next.

**Agent calls Bash**

```bash
cd $TMPDIR/state-space && cat README.md StateSpace.py; python3 -c "
import json;nb=json.load(open('Example.ipynb'))
for c in nb['cells']:
  print('----',c['cell_type']);print(''.join(c['source']))
  for o in c.get('outputs',[]):
    if 'text' in o: print('OUT:',''.join(o['text'])[:1500])
    elif 'data' in o and 'text/plain' in o['data']: print('OUT:',''.join(o['data']['text/plain'])[:800])
"
```

```
code for Zhang et al. 2020
import numpy
from scipy import stats, signal
from sklearn.linear_model import RidgeCV
from sklearn.decomposition import PCA
from matplotlib.pyplot import figure as Figure


def make_delays(matrix, delays = range(5), fill = 0):
	"""
	Makes a version of the a matrix with delays
	:param matrix:
	:param delays:
	:param fill:
	:return:
	"""
	if (matrix.ndim == 1):
		matrix = matrix[...,None]
	out = numpy.ones((matrix.shape[0], matrix.shape[1] * len(delays)),
					 dtype = matrix.dtype) * fill
[... 266 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && mkdir -p supp && cd supp && unzip -o -q paper/10.3389-fnins.2020.565976.supp.docx && ls -la word/media; python3 -c "import PIL; print(PIL.__version__)"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude/supp/word/media/image1.png"
}
```

```
File does not exist. Note: your current working directory is
```

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
 "file_path": "/tmp/claude-1001/supp/word/media/image1.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp/word/media/image2.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp/word/media/image6.jpeg"
}
```

Result: no output.

**Agent**

I've read the per-subject CSIs from Supplementary Figures 1 and 2. Next I'm checking the registry's dataset entry for this paper, then I'll write the file.

**Agent calls Bash**

```bash
cat papers/datasets/zhang-2021.yaml 2>/dev/null; ls claims | head -40; grep -l "kind:" claims/*.yaml | head; grep -h "^  kind:\|^  data:" claims/*.yaml | sort | uniq -c
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.3389/fnins.2020.565976
title: Voxel-Based State Space Modeling Recovers Task-Related Cognitive States in Naturalistic fMRI Experiments
datasets:
- archive: crcns
  id: vim-4
  relation: primary
alasfour-2024.yaml
amjad-2025.yaml
andrews-2024.yaml
armstrong-2026.yaml
asari-2009.yaml
ashworth-2025.yaml
athalye-2023.yaml
azcorra-2023.yaml
bakalar-2023.yaml
bech-2026.yaml
bellvila-2026.yaml
bennett-2024.yaml
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "archive: crcns" claims/*.yaml | head -3; f=$(grep -l "archive: crcns" claims/*.yaml | head -1); sed -n 1,60p $f; sed -n 1,40p tools/claims_check.py
```

```
claims/bruno-2017.yaml
claims/deweese-2004.yaml
claims/eyherabide-2008.yaml
# Claims for Bruno, Frost & Humphries (2017), eLife 6:e27342, "A spiral attractor network drives
# rhythmic locomotion", doi:10.7554/elife.27342, on CRCNS data set apl-1 (doi:10.6080/K0SN074B).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
# protocol as stated in docs/protocol.md (Reader), version pilot-13.
#
# Text read: the version of record (PMC5546814, open access), as JATS XML flattened to text under
# paper/: main text, Materials and methods, and the legends of Figures 1 to 8 and of all twelve
# figure supplements. The paper has no other supplementary file. No PDF of the paper was supplied,
# and none was needed: no claim rests on a number shown only in a figure. The extraction garbles
# some formulas: the Gaussian width reads "σ = {median ISI in population}/12" (a square root may be
# lost) and the rotation period reads "ω = 2πbΔt"; the code settles the second (see below).
# The data set's description (paper/apl-1.data-description.txt) was read only to know what it
# holds; no claim comes from it.
#
# Code read: https://github.com/mdhumphries/AplysiaAttractorAnalysis, commit e5f28e98 (2018-07-11),
# MATLAB, linked from the paper's Data and code availability. Analysis/DataSet_Properties.m builds
# the spike-density functions and the PCA; Analysis/Classify_attractors/ holds the recurrence
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
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
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:])"
```

```
required": [
        "where"
       ]
      }
     }
    ]
   }
  },
  "checks": {
   "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
   "type": "array",
   "items": {
    "type": "object",
    "additionalProperties": false,
    "required": [
     "date",
     "kind",
     "ready"
    ],
    "properties": {
[... 133 more lines not kept]
```

**Agent**

Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/zhang-2021.yaml",
 "content": "# Claims for Zhang, Gao, Cukur & Gallant (2021), Frontiers in Neuroscience 14:565976,\n# \"Voxel-Based State Space Modeling Recovers Task-Related Cognitive States in Naturalistic fMRI\n# Experiments\", doi:10.3389/fnins.2020.565976, on CRCNS data set vim-4 (doi:10.6080/K0668BDF).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol as stated in docs/protocol.md (Reader), version pilot-14.\n#\n# Text read: the version of record (PMC8145286, open access), as JATS XML flattened to text under\n# paper/: main text, Materials and Methods, figure legends, Table 1, and the supplement\n# (Data_Sheet_1.DOCX, legends of Supplementary Figures 1 to 5). No PDF was supplied. The\n# per-subject CSI values of the attention task are printed only inside the images of\n# Supplementary Figures 1 and 2; they were read from the images in the supplement file (S1\n# 0.51, 0.79, 0.64; S3 0.70, 0.71, 0.05; S4 0.64, 0.69, 0.47; S5 0.66, 0.74, 0.59; S6 0.60, 0.71,\n# 0.61, for attend-humans, attend-vehicles and passive). The images of Figures 1 to 4 of the main\n# text were not available, so the pattern of Figure 3B is not known here. Two inconsistencies of\n# the paper, noted where they matter. (1) The means of the six per-subject CSIs in Figure 1 and\n# the supplement (0.64, 0.72, 0.51) are not exactly the means the Results give (0.66, 0.74, 0.53).\n# (2) The Figure 1 legend says blue is \"only humans present\" and green \"only vehicles present\";\n# the supplement legend and the plotted positions say the reverse (green humans, blue vehicles).\n# The video game subjects are S1 and S7 in the text and C1 and C2 in the legends of Figure 3 and\n# Supplementary Figure 4; C1 is S1 (CSI 0.72 in both) and C2 is S7.\n# The data set's description (paper/vim-4.data-description.txt) was read only to know what it\n# holds; no claim comes from it. It says subject S4 of the attention task is not in the data set\n# (no consent for release), so attention-task claims over subjects are tested on S1, S2, S3, S5\n# and S6.\n#\n# Code read: https://github.com/gallantlab/state-space, commit 6ffb3c30 (2020-09-12), linked from\n# the paper's Data Availability Statement. StateSpace.py holds the HRF deconvolution\n# (estimate_devonvolved_response, RidgeCV on delayed features, weights averaged over delays,\n# z-scored), the state space (extract_state_space_positions), the passive-data subsampling, a\n# Monte Carlo JSD between two multivariate normals, and plotting; Example.ipynb fits the state\n# space of the attention task for S1 from the data set's deconvolved data. The code has no CSI\n# averaging, no classifier, no permutation test and no video game analysis.\n#\n# Method choices the code settles where the Methods are silent, used in the criteria below:\n# the OLS regression includes an intercept column (pinv of the normal equations); PCA is\n# scikit-learn PCA (mean-centred) with 24 components fitted on the [TR x voxel] responses; the\n# denoised weights are U U^T B^T for the task variables; the state directions are the first\n# (number of variables) columns of Q from the QR of the denoised [voxel x variable] weights (a\n# reduced QR gives the same columns; the code warns that QR can flip signs); positions are the\n# responses times these directions, then z-scored per dimension over all TRs analysed. For the\n# attention task the state space is fitted once per subject on the passive, attend-human and\n# attend-vehicle TRs stacked (900 each in the data set's deconvolved files, passive already\n# subsampled to the attentive movies), with the three columns of the data set's state labels as\n# task variables. The JSD between two fitted normals is estimated from 1000 samples of each, in\n# log base 2 (so bounded by 1). In plots the human and vehicle axes are sign-oriented so that the\n# \"both present\" mean lies above the \"neither\" mean.\n#\n# Data the paper used. Visual attention task: six subjects (S1 to S6) watching natural movies\n# while fixating, in attend-humans, attend-vehicles (three 10-min runs each) and passive viewing\n# sessions; 3T, TR 2 s, 2.24 x 2.24 x 3.5 mm voxels, cortical voxels only (48,673 +/- 4,382 per\n# subject); detrended (240-s third-order Savitzky-Golay), z-scored, then HRF-deconvolved with a\n# WordNet-label voxelwise model (FIR delays 1 to 4 TRs, ridge with 10-fold CV, weights averaged\n# over delays). Task variables per TR are human presence, vehicle presence and attention\n# condition; the 12 classification labels are the four presence combinations by three\n# conditions. Video game task (Counter Strike, Source): S1 (six 15-min runs, 90 min) and S7\n# (three runs, 45 min), BOLD not deconvolved, nine non-exclusive behavioural states labelled per\n# TR by two observers (dead, round start, safe explore, unsafe explore, kill, engage close,\n# engage far, flash, run away); S7 had no flash events. The data set's description lists\n# preprocessed and deconvolved attention data, semantic and state labels, video game data and\n# per-TR state labels, and fsaverage mappers; it lists no functional localizer or ROI data.\n#\n# Details the paper and code leave open, named in the claims they touch: the number of\n# permutations and how labels are permuted; how the 10 folds are formed; the distance used to\n# assign a held-out TR to the nearest cluster; how z-scoring is applied to held-out TRs; how TRs\n# with several or no video game states enter the clusters and the classifier; the clusters of\n# the video game CSI; the form of the passive-against-attentive test; which weights are mapped\n# onto the cortex; the ROI definitions.\nschema_version: 2\npaper: doi:10.3389/fnins.2020.565976\nclaims:\n- id: fig1-csi-s2\n  statement: In subject S2 the four presence states (neither, humans only, vehicles only, both)\n    are significantly separated in the attention-task state space, with a cluster separation\n    index of 0.75 for attend-humans, 0.69 for attend-vehicles and 0.67 for passive viewing.\n  source: Figure 1 legend\n  quote: The cluster separation index (CSI) is 0.75 for attend-humans, 0.69 for attend-vehicles,\n    and 0.67 for passive ( p < 1e-5, permutation test), all indicating significant separation of\n    the clusters\n  statistics:\n  - test: permutation test\n    p: 1.0e-5\n    p_relation: \"<\"\n    n: subject S2, each attention condition\n  expected:\n  - quantity: CSI, S2, attend-humans\n    value: 0.75\n    tolerance: 0.075\n  - quantity: CSI, S2, attend-vehicles\n    value: 0.69\n    tolerance: 0.069\n  - quantity: CSI, S2, passive\n    value: 0.67\n    tolerance: 0.067\n  criterion: State space as in the code (see the opening comment), fitted on S2's three\n    conditions stacked. For each condition, the CSI as the Methods define it (Quantification of\n    State Space Results, paragraph 1), a multivariate normal (sample mean and covariance) fitted\n    to the TRs of each of the four presence states in the 3-dimensional state space, the JSD of\n    every pair estimated as in the code's JSD function, and the CSI the mean of the six JSDs.\n    Significance by permutation as in the Methods (paragraph 2), \"permuting the state labels,\n    and performing the full analysis using the permuted labels\". The number of permutations is\n    open (a p below 1e-5 needs at least 1e5); use at least 1000 and report p as (k+1)/(n+1).\n    Which labels are permuted is open; the readings are (a) the human and vehicle presence labels\n    shuffled together across TRs, the state space refitted each time, and (b) the same with the\n    labels circularly shifted within each condition, which keeps their autocorrelation.\n    Reproduced when all three CSIs are within tolerance and each exceeds every null value under\n    a reading. The Monte Carlo JSD varies with the seed; report the mean over 10 seeds.\n- id: att-csi-group\n  statement: Across subjects the presence states are distinctly and significantly separated in\n    the attention-task state space, with CSI 0.66 +/- 0.09 for attend-humans, 0.74 +/- 0.03 for\n    attend-vehicles and 0.53 +/- 0.24 for passive viewing (mean +/- std).\n  source: Results, The Voxel-Based State Space Method Recovers a State Space for Variables in\n    the Attention Task, paragraph 2\n  quote: The states are distinctly separated with a CSI of 0.66 ± 0.09 (mean ± std across\n    subjects) for attend-humans, 0.74 ± 0.03 for attend-vehicles, and 0.53 ± 0.24 for passive\n    viewing ( p < 1e-5; permutation test)\n  statistics:\n  - test: permutation test\n    p: 1.0e-5\n    p_relation: \"<\"\n    n: 6 subjects\n  depends_on:\n  - fig1-csi-s2\n  expected:\n  - quantity: mean CSI across subjects, attend-humans\n    value: 0.66\n    tolerance: 0.09\n  - quantity: mean CSI across subjects, attend-vehicles\n    value: 0.74\n    tolerance: 0.03\n  - quantity: mean CSI across subjects, passive\n    value: 0.53\n    tolerance: 0.24\n  criterion: Tolerances are the paper's stated spread across subjects. The CSI and permutation\n    test as in fig1-csi-s2, per subject, on the five subjects the data set holds (S4 is not\n    released); the mean and standard deviation are taken over them. The paper does not say how\n    the group p is formed; the readings are (a) every subject's CSI significant and (b) the mean\n    CSI exceeding the mean of the subjects' null CSIs at every permutation. Reproduced when the\n    three means are within tolerance and the CSIs are significant under a reading. The means\n    over the same five subjects from the per-subject figure values (0.64, 0.73, 0.51) are\n    reported as a second reference, since the paper's own per-subject values do not average to\n    the printed means.\n- id: supp-csi-per-subject\n  statement: In each subject and each attention condition the CSI is significant, with the\n    values printed in Supplementary Figures 1 and 2.\n  source: Supplementary Figures 1 and 2 (panels and legend)\n  quote: CSIs are shows for each condition in each subject and are significant (p < 1e-2 or less,\n    permutation test)\n  statistics:\n  - test: permutation test\n    p: 0.01\n    p_relation: \"<\"\n    n: each of subjects S1, S3, S4, S5 and S6 and each condition\n  depends_on:\n  - fig1-csi-s2\n  expected:\n  - quantity: CSI, S1, attend-humans\n    value: 0.51\n    tolerance: 0.051\n  - quantity: CSI, S1, attend-vehicles\n    value: 0.79\n    tolerance: 0.079\n  - quantity: CSI, S1, passive\n    value: 0.64\n    tolerance: 0.064\n  - quantity: CSI, S3, attend-humans\n    value: 0.70\n    tolerance: 0.07\n  - quantity: CSI, S3, attend-vehicles\n    value: 0.71\n    tolerance: 0.071\n  - quantity: CSI, S3, passive\n    value: 0.05\n    tolerance: 0.005\n  - quantity: CSI, S5, attend-humans\n    value: 0.66\n    tolerance: 0.066\n  - quantity: CSI, S5, attend-vehicles\n    value: 0.74\n    tolerance: 0.074\n  - quantity: CSI, S5, passive\n    value: 0.59\n    tolerance: 0.059\n  - quantity: CSI, S6, attend-humans\n    value: 0.60\n    tolerance: 0.06\n  - quantity: CSI, S6, attend-vehicles\n    value: 0.71\n    tolerance: 0.071\n  - quantity: CSI, S6, passive\n    value: 0.61\n    tolerance: 0.061\n  criterion: The values are read from the panels of Supplementary Figures 1 and 2 (S4, 0.64,\n    0.69 and 0.47, is not in the data set and is left out). CSI and permutation test as in\n    fig1-csi-s2. Reproduced when at least 10 of the 12 values are within tolerance and every CSI\n    exceeds its null at p < 0.01; partially reproduced for 7 to 9 values; not reproduced below\n    7. The S3 passive value, 0.05, is near the floor of the Monte Carlo JSD; its estimate over\n    10 seeds is reported with its spread.\n- id: att-passive-lower\n  statement: Attention increases state separation; the CSI under passive viewing is\n    significantly lower than under the attentive conditions in five of the six subjects.\n  source: Results, The Voxel-Based State Space Method Recovers a State Space for Variables in\n    the Attention Task, paragraph 2; Figure 1 legend; Discussion, paragraph 2\n  quote: Furthermore, we found that the CSI in the passive condition was significantly lower than\n    the CSI in the attentive conditions for five out of the six subjects ( p < 1e-5; permutation\n    test)\n  statistics:\n  - test: permutation test\n    p: 1.0e-5\n    p_relation: \"<\"\n    n: 6 subjects, significant in 5\n  depends_on:\n  - att-csi-group\n  expected:\n  - quantity: subjects with passive CSI significantly lower, of six\n    value: 5\n    tolerance: 0\n  criterion: CSIs as in fig1-csi-s2. The paper does not give the form of this test. The\n    readings are (a) passive against each attentive condition, both differences significant;\n    (b) passive against the mean of the two attentive CSIs. The null in either is formed by\n    permuting the attention-condition labels between passive and attentive TRs (the presence\n    labels kept), either (i) refitting the state space each time, as the Methods' \"full analysis\"\n    says, or (ii) keeping the fitted positions and reassigning TRs to conditions; p is one-sided\n    (passive lower), with at least 1000 permutations. The data set holds five of the six\n    subjects. Reproduced when the passive CSI is significantly lower (p < 0.05) in at least 4 of\n    the 5 under a reading, which is what five of six allows; not reproduced otherwise. From the\n    figure values, S1 (passive 0.64 against attend-humans 0.51) and S6 (0.61 against 0.60) fail\n    reading (a) on the raw values, so the per-reading counts are reported.\n- id: att-classification\n  statement: Held-out TRs of the attention task are classified into the 12 labels (four presence\n    states by three attention conditions) from their position in the learned state space at\n    48.4 +/- 7.6% across subjects, well above the chance of 8.3%.\n  source: Results, The Voxel-Based State Space Method Recovers a State Space for Variables in\n    the Attention Task, paragraph 3\n  quote: Average performance across subjects is 48.4 ± 7.6% ( p < 1e-5, permutation test, chance =\n    8.3%)\n  statistics:\n  - test: permutation test\n    p: 1.0e-5\n    p_relation: \"<\"\n    n: 6 subjects, 10-fold cross-validation each\n  expected:\n  - quantity: mean classification accuracy across subjects, 12 labels\n    value: 48.4\n    tolerance: 7.6\n    unit: percent\n  criterion: Tolerance is the paper's stated spread across subjects. As in the Methods\n    (Quantification of State Space Results, paragraph 2), per subject, 10-fold cross-validation\n    over the stacked TRs of the three conditions; in each fold the state space (code's method)\n    is fitted on the training 90%, the held-out TRs are projected onto its directions, and each\n    is assigned to the nearest of the 12 training clusters; accuracy is averaged over folds and\n    then over the five subjects in the data set. Open, with readings run each. Folds as (a)\n    contiguous tenths of the stacked series, or (b) random TRs. Nearest cluster by (a) Euclidean\n    distance to the cluster mean, or (b) the highest density under the multivariate normal\n    fitted to the cluster, as for the CSI. Held-out positions z-scored with the training means\n    and standard deviations. The null permutes the 12 labels of the training TRs and repeats the\n    full analysis, at least 1000 times. Reproduced when the mean is within tolerance and above\n    every null mean under a reading; partially reproduced when it is significant but outside\n    tolerance under all readings.\n- id: att-weights-cortex\n  statement: The human-presence dimension of the attention-task state space has its weights in\n    face and body areas (FFA, OFA, EBA), MT+, LO, the frontal operculum and the inferior frontal\n    sulcus; the vehicle-presence dimension in RSC, PPA, OPA, IPS, FEF and around the inferior\n    frontal sulcus.\n  source: Results, The Voxel-Based State Space Method Recovers a State Space for Variables in\n    the Attention Task, paragraph 4; Figure 2; Supplementary Figure 3\n  quote: The “human presence” dimension projects heavily onto FFA ( Kanwisher et al., 1997 ), OFA (\n    Gauthier et al., 2000 ), and EBA ( Downing et al., 2001 ) ... In contrast, the “vehicle\n    presence” dimension projects strongly onto RSC ( Maguire, 2001 ; Epstein, 2008 ), PPA (\n    Epstein et al., 1999 ), and OPA ( Dilks et al., 2013 )\n  data: with_inputs\n  criterion: The ROIs were delineated per subject from functional localizer and retinotopic\n    mapping data (Methods, Preprocessing and Visualization, paragraph 2), which the paper does\n    not deposit and the data set's description does not list; the author decides whether an\n    outside ROI source (for example an fsaverage atlas through the data set's mappers) can be\n    used. Which weights are mapped is open; the readings are (a) the OLS weights B, (b) the\n    denoised weights B_L, and (c) the state directions Q_S, each sign-oriented so that the\n    dimension's own state has a positive mean position. Figure 2 thresholds voxels by a semantic\n    encoding model at uncorrected p < 0.05; that threshold is not applied, as the encoding model\n    performance is not given. Per subject and ROI, the mean weight. Reproduced when, in at least\n    4 of the 5 subjects, the mean human-presence weight is positive and above the mean\n    vehicle-presence weight in FFA, OFA and EBA, and the reverse holds in RSC, PPA and OPA,\n    under a reading. The other named regions are reported.\n- id: game-csi\n  statement: In the video game task the behavioural states are distinctly and significantly\n    separated in the 9-dimensional state space, with CSI 0.72 in subject S1 and 0.62 in S7.\n  source: Results, The Voxel-Based State Space Method Recovers a Behavioral State Space for the\n    Open-Ended Video Game Task, paragraph 2; Figure 3A\n  quote: The states are distinctly separated with a CSI of 0.72 in subject S1 and 0.62 in subject\n    S7 ( p < 1e-5, permutation test)\n  statistics:\n  - test: permutation test\n    p: 1.0e-5\n    p_relation: \"<\"\n    n: subjects S1 and S7\n  expected:\n  - quantity: CSI, S1, video game\n    value: 0.72\n    tolerance: 0.072\n  - quantity: CSI, S7, video game\n    value: 0.62\n    tolerance: 0.062\n  criterion: State space by the code's method on each subject's BOLD data (no deconvolution, as\n    the Methods say) with the nine state columns as task variables. CSI as in fig1-csi-s2, in\n    the 9-dimensional space. The clusters are open, and the states are not exclusive. Readings\n    are (a) one cluster per state, a TR entering the cluster of every state it has; (b) one\n    cluster per state from TRs with exactly one state; (c) the three groups of Figure 3A (safe\n    explore, engage close, all other TRs). A state with no TRs (flash in S7) or too few to fit\n    a covariance is left out and the count reported. Permutations as in fig1-csi-s2, shuffling\n    the rows of the state matrix. Reproduced when both CSIs are within tolerance and above every\n    null value under a reading.\n- id: game-mutual-negative-projection\n  statement: The mutually exclusive states engage close and safe explore each project negatively\n    onto the other's dimension of the video game state space.\n  source: Results, The Voxel-Based State Space Method Recovers a Behavioral State Space for the\n    Open-Ended Video Game Task, paragraph 3; Figure 3A legend\n  quote: For example, “engaging close” and “safe explore” each project negatively to the dimension\n    associated with the other state ( Figure 3A ) ( p < 1e-5, permutation test)\n  statistics:\n  - test: permutation test\n    p: 1.0e-5\n    p_relation: \"<\"\n    n: subjects S1 and S7\n  depends_on:\n  - game-csi\n  criterion: State space as in game-csi, each dimension sign-oriented so that its own state's\n    TRs have a positive mean position (the code's plotting orients axes by cluster means). The\n    measure is the mean position of engage-close TRs on the safe-explore dimension and of\n    safe-explore TRs on the engage-close dimension. The null permutes the rows of the state\n    matrix and refits, at least 1000 times, one-sided for a negative mean. Reproduced when both\n    means are negative and significant at p < 0.05 in both subjects; partially reproduced in one\n    subject.\n- id: fig3b-state-relations\n  statement: States of the video game project at significant non-zero positions on other states'\n    dimensions, an asymmetric pattern found in both subjects that differs between them.\n  source: Figure 3B and its legend; Results, The Voxel-Based State Space Method Recovers a\n    Behavioral State Space for the Open-Ended Video Game Task, paragraph 3\n  quote: Relationships between states are reflected in non-zero projections of states on to other\n    state dimensions ... Colors indicate Bonferroni-corrected significance ( p < 0.01, permutation\n    test)\n  statistics:\n  - test: permutation test\n    p: 0.01\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: subjects S1 and S7\n  depends_on:\n  - game-mutual-negative-projection\n  criterion: The figure's matrix was not available to this reader, so no per-pair result is\n    fixed. For each ordered pair of different states, the mean position of the row state's TRs\n    on the column state's dimension, oriented as in game-mutual-negative-projection, with a\n    two-sided permutation test as there; Bonferroni over the off-diagonal pairs the subject has\n    (72, or 56 for S7, who has no flash), at 0.01. Reproduced when each subject has significant\n    off-diagonal pairs, the matrix is asymmetric in at least one pair, and the two subjects'\n    sets of significant pairs differ. The full matrices are reported for comparison with the\n    figure.\n- id: game-classification\n  statement: Held-out TRs of the video game task are classified into the nine behavioural states\n    from their position in the learned state space with balanced accuracy 32.8 +/- 3.8% in S1\n    and 30.4 +/- 4.2% in S7, above the chance of 11%.\n  source: Results, The Voxel-Based State Space Method Recovers a Behavioral State Space for the\n    Open-Ended Video Game Task, paragraph 4\n  quote: Average balanced accuracy across 10 cross-validation folds in the subject is 32.8 ± 3.8%\n    in subject S1 and 30.4 ± 4.2% in subject S7 ( p < 1e-5, permutation test, chance = 11%)\n  statistics:\n  - test: permutation test\n    p: 1.0e-5\n    p_relation: \"<\"\n    n: subjects S1 and S7, 10 folds each\n  depends_on:\n  - game-csi\n  expected:\n  - quantity: balanced accuracy, S1\n    value: 32.8\n    tolerance: 3.8\n    unit: percent\n  - quantity: balanced accuracy, S7\n    value: 30.4\n    tolerance: 4.2\n    unit: percent\n  criterion: Tolerances are the paper's stated spread across folds. Cross-validation as in\n    att-classification, with the nine state clusters, and balanced accuracy (mean recall over\n    classes, Brodersen et al. 2010) averaged over folds. Folds and nearest-cluster distance have\n    the readings of att-classification. How a TR with several states or none is labelled is\n    open; readings are (a) TRs with exactly one state only; (b) every labelled TR, a prediction\n    counted correct for each of its states that it names and recall computed per state over the\n    TRs that have it. Classes with no TRs (flash in S7) are left out. Null as in\n    att-classification. Reproduced when both values are within tolerance and above every null\n    value under a reading; partially reproduced when significant but outside tolerance.\n- id: game-weights-two-groups\n  statement: The video game state dimensions fall into two groups, dead, round start, safe\n    explore, unsafe explore and flash in TPJ, precuneus and prefrontal cortex (default-mode\n    areas), and kill, engage close, engage far and run away in motor, premotor and\n    supplementary motor areas, IPS, FEF and SEF; the weights are largely consistent across the\n    two subjects.\n  source: Results, The Voxel-Based State Space Method Recovers a Behavioral State Space for the\n    Open-Ended Video Game Task, paragraph 5; Figure 4; Supplementary Figures 4 and 5\n  quote: They appear to fall into two general categories. The dimensions for “safe explore,”\n    “round start,” “flash,” “dead,” and “unsafe explore” project on to the TPJ, precuneus, and\n    prefrontal cortex. The dimensions for “run away,” “engage close,” “kill,” and “engage far”\n    project on to the motor, pre-motor, and supplementary motors areas, and also in IPS, FEF, and\n    SEF ... The weights for each dimension are largely consistent across the two subjects\n  depends_on:\n  - game-csi\n  criterion: The grouping is tested on the data set alone; the ROI part needs ROI definitions\n    the data set does not list (see att-weights-cortex) and is reported only if the author adopts\n    an outside ROI source. Weights with the readings of att-weights-cortex. Per subject, the\n    Pearson correlation across voxels between the weight maps of every pair of dimensions, and\n    average-linkage clustering on one minus correlation cut into two groups. Reproduced when in\n    both subjects the two groups are the paper's (flash absent in S7), or differ by one state;\n    not reproduced otherwise. Consistency across subjects is the correlation of each dimension's\n    map between subjects on fsaverage, through the data set's mappers; reported, with the\n    claim's consistency part holding when the median over shared dimensions is positive.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/zhang-2021.yaml paper/10.3389-fnins.2020.565976.txt; grep -nE "^[^#]*[^\"']: [^\"'|>]" claims/zhang-2021.yaml | grep -vE "^\s*[0-9]+:\s*-?\s*[a-z_]+: " | head; grep -n "—\|rather" claims/zhang-2021.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import yaml
d=yaml.safe_load(open('claims/zhang-2021.yaml'))
def w(x,p=''):
  if isinstance(x,dict): [w(v,p+'.'+k) for k,v in x.items()]
  elif isinstance(x,list): [w(v,p+'[%d]'%i) for i,v in enumerate(x)]
  elif isinstance(x,str) and ': ' in x: print(p)
w(d)"; git status --short
```

```
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
?? claims/zhang-2021.yaml
?? scripts
```

**Agent**

I've written `claims/zhang-2021.yaml`. The quote checker passes it: 11 claims, 11 quotes, 9 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record (PMC8145286), full text with Methods, figure legends and Table 1. The supplement (Data_Sheet_1.DOCX) has the legends of Supplementary Figures 1 to 5. No PDF was supplied. The per-subject CSIs for the attention task are printed only inside the images of Supplementary Figures 1 and 2, so I read them from those images. The code is gallantlab/state-space at commit 6ffb3c30. It covers the state space, the HRF deconvolution and the JSD, but has no CSI averaging, no classifier, no permutation tests and no video game analysis.

**Claims:** all 11 have quotes and none uses `inferred`.
- 9 have statistics. All are permutation tests: seven at p < 1e-5, one at p < 0.01, and Figure 3B at p < 0.01 with Bonferroni correction.
- 7 have expected values: the S2 CSIs, the group CSIs, the per-subject CSIs from the supplement, the "5 of 6 subjects" count, attention classification, the video game CSIs and video game balanced accuracy.
- All 11 have criteria.
- The cortical-weights claim for the attention task is `with_inputs`, because it needs ROIs (regions of interest). The paper drew them from localizer data that it does not deposit and that the dataset's description does not list.

**Details the paper leaves open, with the readings named:**
- **Permutations:** the number is not given (p < 1e-5 needs at least 1e5); I set at least 1000. Labels are either shuffled freely or circularly shifted within each condition.
- **Group p for the CSIs:** either every subject is significant, or the mean CSI is compared against the mean of the null CSIs.
- **Passive against attentive test:** passive is compared against each attentive condition or against their mean. The null either refits the state space each time or keeps it fixed and reassigns TRs to conditions.
- **Cross-validation folds:** contiguous tenths of the data or random TRs. Held-out positions are z-scored with the training statistics.
- **Nearest cluster:** Euclidean distance to the cluster mean, or the highest density under the fitted normal distribution.
- **Video game clusters for the CSI:** one cluster per state with TRs in every state they have, one per state using only TRs with a single state, or the three groups of Figure 3A.
- **Video game classification labels:** TRs with exactly one state only, or every labelled TR counted correct for each of its states.
- **Weights mapped onto the cortex:** the regression weights B, the denoised weights B_L, or the state directions Q_S.
- **Video game grouping:** the paper gives no measure, so I fixed one: correlations between weight maps with two-group clustering.

**Things missing or inconsistent that claims needed:**
- **Figure 3B:** the main-text figure images were not available, so the pattern of significant state relations is unknown. That claim's criterion is structural only.
- **ROI definitions:** not deposited. The ROI parts of both cortical-weights claims depend on an outside source the author has to choose.
- **Subject S4:** not in the dataset, so the attention-task claims across subjects are tested on 5 of 6 subjects.
- **Group means:** the per-subject CSIs in the figures average to 0.64, 0.72 and 0.51, not the 0.66, 0.74 and 0.53 the Results print.
- **Figure 1 colours:** the legend swaps blue and green compared with the supplement legend and the plotted positions.
- **"Five of six" count:** on the raw figure values, S1 and S6 do not have a passive CSI below both attentive ones. The test the paper used is unstated.

## End of run

21 turns, 4 minutes, $1.27 at API prices, result: success.
