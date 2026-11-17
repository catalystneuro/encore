# zhang-2021 · claims-check · run 42858422927

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i zhang; cat claims/zhang-2021.yaml; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; wc -l claims/zhang-2021.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "Reader" docs/protocol.md | head
```

```
15:  it against the paper. Readers never see the dataset's data.
28:Reader runs are made with the [Paper run](../.github/workflows/papers.yml)
43:## Reader
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
[... 635 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/zhang-2021.yaml"
}
```

```
1	# Claims for Zhang, Gao, Cukur & Gallant (2021), Frontiers in Neuroscience 14:565976,
2	# "Voxel-Based State Space Modeling Recovers Task-Related Cognitive States in Naturalistic fMRI
3	# Experiments", doi:10.3389/fnins.2020.565976, on CRCNS data set vim-4 (doi:10.6080/K0668BDF).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
5	# protocol as stated in docs/protocol.md (Reader), version pilot-14.
6	#
7	# Text read: the version of record (PMC8145286, open access), as JATS XML flattened to text under
8	# paper/: main text, Materials and Methods, figure legends, Table 1, and the supplement
9	# (Data_Sheet_1.DOCX, legends of Supplementary Figures 1 to 5). No PDF was supplied. The
10	# per-subject CSI values of the attention task are printed only inside the images of
11	# Supplementary Figures 1 and 2; they were read from the images in the supplement file (S1
12	# 0.51, 0.79, 0.64; S3 0.70, 0.71, 0.05; S4 0.64, 0.69, 0.47; S5 0.66, 0.74, 0.59; S6 0.60, 0.71,
13	# 0.61, for attend-humans, attend-vehicles and passive). The images of Figures 1 to 4 of the main
14	# text were not available, so the pattern of Figure 3B is not known here. Two inconsistencies of
15	# the paper, noted where they matter. (1) The means of the six per-subject CSIs in Figure 1 and
16	# the supplement (0.64, 0.72, 0.51) are not exactly the means the Results give (0.66, 0.74, 0.53).
17	# (2) The Figure 1 legend says blue is "only humans present" and green "only vehicles present";
18	# the supplement legend and the plotted positions say the reverse (green humans, blue vehicles).
19	# The video game subjects are S1 and S7 in the text and C1 and C2 in the legends of Figure 3 and
20	# Supplementary Figure 4; C1 is S1 (CSI 0.72 in both) and C2 is S7.
[... 393 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/zhang-2021.yaml paper/10.3389-fnins.2020.565976.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the paper text.

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; cat paper/10.3389-fnins.2020.565976.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fnins.2020.565976.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/supp && cd $TMPDIR/supp && unzip -o -q paper/10.3389-fnins.2020.565976.supp.docx && ls -la word/media; ls  | head -30
```

Result: not kept, because it reads the paper's text.

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

Supplement values match the claims file. Now checking whether the linked code can be verified, and what the data description lists.

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 60 git clone -q https://github.com/gallantlab/state-space ss 2>&1 | tail -2; ls ss 2>/dev/null && cd ss && git log -1 --format='%h %ci'
```

```
Example.ipynb
README.md
StateSpace.py
6ffb3c3 2020-09-12 15:42:44 -0700
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ss && cat StateSpace.py; python -c "
import json;nb=json.load(open('Example.ipynb'))
for c in nb['cells']:
  print('----',c['cell_type']); print(''.join(c['source']))
"
```

```
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

[... 254 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat paper/vim-4.data-description.txt | head -250
```

Result: not kept, because it reads the paper's text.

**Agent**

The linked code (commit 6ffb3c3) matches the file's description of it. Next I'll make the edits.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/zhang-2021.yaml",
 "old_string": "  statistics:\n  - test: permutation test\n    p: 1.0e-5\n    p_relation: \"<\"\n    n: 6 subjects, significant in 5\n  depends_on:\n  - att-csi-group\n  expected:\n  - quantity: subjects with passive CSI significantly lower, of six\n    value: 5\n    tolerance: 0\n  criterion: CSIs as in fig1-csi-s2. The paper does not give the form of this test. The\n    readings are (a) passive against each attentive condition, both differences significant;\n    (b) passive against the mean of the two attentive CSIs. The null in either is formed by\n    permuting the attention-condition labels between passive and attentive TRs (the presence\n    labels kept), either (i) refitting the state space each time, as the Methods' \"full analysis\"\n    says, or (ii) keeping the fitted positions and reassigning TRs to conditions; p is one-sided\n    (passive lower), with at least 1000 permutations. The data set holds five of the six\n    subjects. Reproduced when the passive CSI is significantly lower (p < 0.05) in at least 4 of\n    the 5 under a reading, which is what five of six allows; not reproduced otherwise. From the",
 "new_string": "  depends_on:\n  - att-csi-group\n  expected:\n  - quantity: subjects with passive CSI significantly lower, of six\n    value: 5\n    tolerance: 0\n  criterion: CSIs as in fig1-csi-s2. The paper does not give the form of this test. The\n    readings are (a) passive against each attentive condition, both differences significant;\n    (b) passive against the mean of the two attentive CSIs. The null in either is formed by\n    permuting the attention-condition labels between passive and attentive TRs (the presence\n    labels kept), either (i) refitting the state space each time, as the Methods' \"full analysis\"\n    says, or (ii) keeping the fitted positions and reassigning TRs to conditions; p is one-sided\n    (passive lower). A subject counts at the paper's threshold, p < 1e-5, which needs at least\n    1e5 permutations; where fewer can be run (at least 1000), a subject counts when its\n    difference exceeds every null value, the bound reached is reported, and the count at p <\n    0.05 is shown as a variant. The data set holds five of the six subjects. Reproduced when the\n    passive CSI is significantly lower in at least 4 of the 5 under a reading, which is what five\n    of six allows; not reproduced otherwise. From the"
}
```

```
The file claims/zhang-2021.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/zhang-2021.yaml",
 "old_string": "    fitted to the cluster, as for the CSI. Held-out positions z-scored with the training means\n    and standard deviations. The null",
 "new_string": "    fitted to the cluster, as for the CSI. Held-out positions are z-scored with the training\n    means and standard deviations (the code z-scores the positions it fits; a standard choice for\n    held-out data). The null"
}
```

```
The file claims/zhang-2021.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/zhang-2021.yaml",
 "old_string": "    dimension's own state has a positive mean position. Figure 2 thresholds voxels by a semantic\n    encoding model at uncorrected p < 0.05; that threshold is not applied, as the encoding model\n    performance is not given. Per subject and ROI, the mean weight. Reproduced when, in at least\n    4 of the 5 subjects, the mean human-presence weight is positive and above the mean\n    vehicle-presence weight in FFA, OFA and EBA, and the reverse holds in RSC, PPA and OPA,\n    under a reading. The other named regions are reported.",
 "new_string": "    dimension's own state has a positive mean position. Figure 2 and Supplementary Figure 3\n    threshold voxels by the prediction performance of a semantic encoding model at uncorrected p\n    < 0.05. The data set holds the semantic labels and the preprocessed BOLD, so the threshold\n    has two readings, (i) no threshold and (ii) voxels whose cross-validated prediction by the\n    WordNet model of the deconvolution (Methods, Deconvolution, FIR delays 1 to 4, ridge with\n    10-fold CV) is significant at uncorrected p < 0.05; the test of the prediction is open\n    (correlation of predicted and measured responses, against zero or by permutation). Per\n    subject and ROI, the mean weight. Reproduced when, in at least 4 of the 5 subjects, the mean\n    human-presence weight is positive and above the mean vehicle-presence weight in FFA, OFA and\n    EBA, and the reverse holds in RSC, PPA and OPA, under a reading. The other named regions are\n    reported, including those the Figure 2 legend adds (SEF for the human-presence dimension, FO\n    for the vehicle-presence dimension)."
}
```

```
The file claims/zhang-2021.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/zhang-2021.yaml",
 "old_string": "  criterion: State space as in game-csi, each dimension sign-oriented so that its own state's\n    TRs have a positive mean position (the code's plotting orients axes by cluster means). The\n    measure",
 "new_string": "  criterion: State space as in game-csi. The code has no video game analysis, and two details\n    that change the dimensions are open. The sign of each dimension, with readings (a) its own\n    state's TRs have a positive mean position (by analogy with the code's plotting, which flips\n    an axis by cluster means), (b) the diagonal of R made positive, so that the dimension points\n    along the state's denoised weight vector. The order of the nine variables entering the QR,\n    since each column of Q is orthogonalized against the earlier ones, with readings (i) the\n    order of Table 1 (dead, round start, safe explore, unsafe explore, kill, engage close, engage\n    far, flash, run away) and (ii) the order of the columns of the data set's state matrix. The\n    measure"
}
```

```
The file claims/zhang-2021.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/zhang-2021.yaml",
 "old_string": "    on the column state's dimension, oriented as in game-mutual-negative-projection, with a\n    two-sided permutation test as there; Bonferroni over the off-diagonal pairs the subject has\n    (72, or 56 for S7, who has no flash), at 0.01. Reproduced",
 "new_string": "    on the column state's dimension, with the sign and order readings of\n    game-mutual-negative-projection, and a two-sided permutation test as there. The number of\n    tests Bonferroni corrects for is open; readings are (a) the off-diagonal pairs the subject\n    has (72, or 56 for S7, who has no flash) and (b) every cell of the matrix (81, or 64 for S7);\n    corrected threshold 0.01. Reproduced"
}
```

```
The file claims/zhang-2021.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the video game weights claim, whose criterion grouped dimensions by a clustering method the paper does not use.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/zhang-2021.yaml",
 "old_string": "  depends_on:\n  - game-csi\n  criterion: The grouping is tested on the data set alone; the ROI part needs ROI definitions\n    the data set does not list (see att-weights-cortex) and is reported only if the author adopts\n    an outside ROI source. Weights with the readings of att-weights-cortex. Per subject, the\n    Pearson correlation across voxels between the weight maps of every pair of dimensions, and\n    average-linkage clustering on one minus correlation cut into two groups. Reproduced when in\n    both subjects the two groups are the paper's (flash absent in S7), or differ by one state;\n    not reproduced otherwise. Consistency across subjects is the correlation of each dimension's\n    map between subjects on fsaverage, through the data set's mappers; reported, with the\n    claim's consistency part holding when the median over shared dimensions is positive.",
 "new_string": "  data: with_inputs\n  depends_on:\n  - game-csi\n  criterion: The paper groups the dimensions by the regions their weights project onto, read\n    from the maps (Figure 4, Supplementary Figures 4 and 5); it gives no quantitative grouping\n    method. The regions need definitions the data set does not list (see att-weights-cortex);\n    the author decides whether an outside source can be used (functional ROIs for IPS, FEF and\n    SEF; an fsaverage atlas, through the data set's mappers, for TPJ, precuneus, prefrontal,\n    motor, premotor and supplementary motor cortex). Weights with the readings of\n    att-weights-cortex, the Q_S reading also under the order readings of\n    game-mutual-negative-projection. Figure 4 thresholds voxels by \"an encoding model\" at\n    Bonferroni-corrected p < 0.05, the model not named; readings are (i) no threshold and (ii)\n    voxels whose cross-validated prediction by the nine-state OLS model is significant at that\n    level. Per subject, dimension and region, the mean weight. Reproduced when, in both\n    subjects, every dimension of the first group (dead, round start, safe explore, unsafe\n    explore, flash; no flash in S7) has a positive mean weight in TPJ, precuneus and prefrontal\n    cortex and a higher one there than in the second group's regions, and every dimension of the\n    second group (kill, engage close, engage far, run away) the reverse in motor, premotor and\n    supplementary motor cortex, IPS, FEF and SEF, allowing one dimension per subject to fail,\n    under a reading; not reproduced otherwise. As a variant not taken from the paper and not\n    deciding the outcome, the Pearson correlation across voxels between the weight maps of every\n    pair of dimensions, with average-linkage clustering on one minus correlation cut into two\n    groups, is reported. The paper gives no measure of \"largely consistent across the two\n    subjects\"; the correlation of each dimension's map between subjects on fsaverage is\n    reported, and the consistency part is said to hold when its median over shared dimensions is\n    positive, a reading of the reader's, stated as such."
}
```

```
The file claims/zhang-2021.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/zhang-2021.yaml",
 "old_string": "# the cortex; the ROI definitions.",
 "new_string": "# the cortex; the ROI definitions; for the video game, the sign of each dimension and the order\n# of the nine variables in the QR (the code has no video game analysis); the voxel thresholds of\n# Figures 2 and 4."
}
```

```
<tool_use_error>String to replace not found in file.
String: # the cortex; the ROI definitions.</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/zhang-2021.yaml",
 "old_string": "conditions. Video game task (Counter Strike, Source): S1 (six 15-min runs, 90 min) and S7\n# (three runs, 45 min),",
 "new_string": "conditions. Video game task (Counter Strike, Source): S1 and S7, one with six 15-min runs (90\n# min) and the other with three (45 min); the paper says \"one subject\" and \"the second subject\"\n# and does not name which is which,"
}
```

```
The file claims/zhang-2021.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/zhang-2021.yaml",
 "old_string": "# onto the cortex; the ROI definitions.",
 "new_string": "# onto the cortex; the ROI definitions; for the video game, the sign of each dimension and the\n# order of the nine variables in the QR (the code has no video game analysis); the voxel\n# thresholds of Figures 2 and 4."
}
```

```
The file claims/zhang-2021.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the checks entry.

**Agent calls Bash**

```bash
cd  cat >> claims/zhang-2021.yaml <<'EOF'
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Checked the quotes against the text, the per-subject CSIs against the images of Supplementary Figures 1 and 2 (all 15 values and the p bounds agree), and the description of the code against gallantlab/state-space at 6ffb3c3 (it agrees, including the intercept column, PCA denoiser, QR, z-scoring, log2 Monte Carlo JSD and the sign flip of the plotting).
  - att-passive-lower, removed the statistics entry, since the p < 1e-5 is the threshold at which subjects are counted (five of six), a method and not a result (protocol, Reader, step 3).
  - att-passive-lower, the criterion counted subjects at p < 0.05, a threshold the paper does not use; it now counts at the paper's p < 1e-5, with the bound reached and the count at p < 0.05 shown when fewer than 1e5 permutations can be run.
  - att-classification, said that z-scoring held-out positions with the training statistics is a standard choice, following the code's z-scoring of fitted positions; the paper does not fix it.
  - att-weights-cortex, the criterion dropped the semantic-model voxel threshold of Figure 2 on the ground that the model's performance is not given; the data set holds the semantic labels and preprocessed BOLD, so the threshold is computable, and it is now a reading (with no threshold the other); also named the regions the Figure 2 legend adds (SEF, FO).
  - game-mutual-negative-projection, the sign rule was attributed to the code, which has no video game analysis; the sign and the order of the nine variables in the QR (which changes every dimension after the first) are now named as open, with readings.
  - fig3b-state-relations, took the sign and order readings, and named the number of Bonferroni tests (off-diagonal pairs or every cell) as open.
  - game-weights-two-groups, the deciding test was a correlation clustering of weight maps that the paper does not use; the paper groups dimensions by the regions they project onto, so the deciding test is now mean weight per region, with data with_inputs for the region definitions, the Figure 4 voxel threshold named as open, and the clustering kept as a variant that does not decide; the consistency measure is marked as a reading of the reader's.
  - Opening comment, the paper does not say which video game subject played 90 min and which 45 min; the comment had S1 as 90 min; the open details now include the video game sign and order and the voxel thresholds.
  - Open, not settled. The paper's group CSI means (0.66, 0.74, 0.53) do not equal the means of its own per-subject values (0.64, 0.72, 0.51), recorded in att-csi-group. Figure 3B and the main figures could not be read (no PDF), so fig3b-state-relations fixes no per-pair result. The exception subject in att-passive-lower cannot be fixed from the paper; on the figure values S1 or S6 fail reading (a).
  - Main findings, every Results finding has a claim; the descriptive numbers (24 PCs explaining about 70% of variance, voxel counts) are method details and have none.
EOF
python tools/claims_check.py claims/zhang-2021.yaml paper/10.3389-fnins.2020.565976.txt; grep -nP '—|\brather\b' claims/zhang-2021.yaml; python -c "import yaml;d=yaml.safe_load(open('claims/zhang-2021.yaml'));print(len(d['claims']),d['checks'][-1]['ready'])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/zhang-2021.yaml'))
print(all(isinstance(c,str) for c in d['checks'][-1]['changes']))"; grep -n ': .*: ' claims/zhang-2021.yaml | grep -v '^\s*#' | head; git status --short
```

```
True
 M claims/zhang-2021.yaml
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
?? scripts
```

**Agent**

I checked `claims/zhang-2021.yaml`, corrected six claims and the opening comment, and the file is ready for an attempt. Nothing is committed.

**Checker:** `claims/zhang-2021.yaml: 11 claims, 11 quotes, 8 statistical values, 0 problems`. It reported 9 statistical values before my edits; the count dropped because I removed one entry (see att-passive-lower).

**What already held up:**
- The 15 per-subject CSIs in the file match the images of Supplementary Figures 1 and 2, and so do their p bounds.
- I cloned the paper's code (gallantlab/state-space, commit 6ffb3c3). It matches what the file says about it: the intercept column, the 24-component PCA denoising, the QR step, the z-scoring, the JSD estimate and the axis sign flip in the plots.

**Changes, by claim:**
- **att-passive-lower:** I removed the statistics entry. The paper's p < 1e-5 is the threshold at which it counts subjects ("five out of six"), so it is a method, not a result. The criterion counted subjects at p < 0.05, which the paper never uses; it now counts at p < 1e-5. If fewer than 1e5 permutations can be run, the bound reached is reported, with the p < 0.05 count shown as a variant.
- **att-classification:** z-scoring the held-out TRs with the training statistics is now labelled a standard choice. It follows the code; the paper does not fix it.
- **att-weights-cortex:** the file had dropped the voxel threshold from the semantic encoding model in Figure 2, saying the model's performance was not given. The data set holds the semantic labels and the preprocessed BOLD, so the threshold can be computed. It is now one reading, with no threshold as the other. I also added the regions the Figure 2 legend names on top of the Results (SEF for humans, FO for vehicles).
- **game-mutual-negative-projection:** the file credited its sign rule to the code, but the code has no video game analysis. Two open details are now named, with readings:
  - the sign of each dimension;
  - the order of the nine variables going into the QR step, which changes every dimension after the first.
- **fig3b-state-relations:** now uses those sign and order readings. The number of tests the Bonferroni correction covers is named as open: the off-diagonal pairs (72, or 56 for S7) or every cell (81, or 64).
- **game-weights-two-groups:** the deciding test was a correlation clustering of the weight maps, which the paper never uses. The paper groups dimensions by the regions they project onto, so the test is now the mean weight per region, marked `data: with_inputs` because the regions need an outside definition.
  - The Figure 4 voxel threshold is named as open.
  - The clustering stays as a variant that does not decide the outcome.
  - The measure for "largely consistent across subjects" is marked as the earlier reader's own choice.
- **Opening comment:** the paper does not say which video game subject played 90 minutes and which 45; the comment had assigned 90 to S1. I also added the new open details to its list.

**Still open:**
- The paper's group CSI means (0.66, 0.74, 0.53) are not the means of its own per-subject values (0.64, 0.72, 0.51). The paper disagrees with itself here; att-csi-group already notes this.
- There is no PDF, so Figure 3B and the main-text figures could not be read. fig3b-state-relations therefore fixes no per-pair result.
- In att-passive-lower, the paper does not say which subject is the exception. On the figure values, S1 or S6 fails the passive-against-each-condition reading.

Every main finding has a claim, and no claim comes from anywhere but this paper.

**Ready:** yes (`ready: true` in the new `checks` entry).

## End of run

27 turns, 3 minutes, $1.32 at API prices, result: success.
