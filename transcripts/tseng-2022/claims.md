# 000579 · claims · run 39933538892

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/000579 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## Author/' docs/protocol.md; ls claims/001453/ paper/ claims/000579 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml | head -150; wc -c paper/*; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 30,200p claims/001453/*.yaml; wc -c paper/*; head -20 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -lc paper/*; head -c 1500 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Reading the paper text now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2022.05.012.txt",
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '{print NR": "length($0)}' paper/*.txt | sort -t: -k2 -n -r | head;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 7p paper/*.txt | fold -s -w 200 > $TMPDIR/main.txt; wc -l $TMPDIR/main.txt; sed -n 8,40p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "supplement\|S1\b\|Figure S\|-----\|Table S" paper/*.txt | cut -c1-200 | tail -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "limit": 300
}
```

```
1	pmc Neuron Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC9357051 PMC9357051.1 9357051 9357051 NIHMS1810369 35679861 
2	10.1016/j.neuron.2022.05.012 NIHMS1810369 NIHPA1810369 1 Article Shared and specialized coding across posterior cortical areas for dynamic navigation decisions Tseng Shih-Yi 1 2 Chettih Selmaan N. 1 
3	2 Arlt Charlotte 1 Barroso-Luque Roberto 1 Harvey Christopher D. 1 3 * 1 Department of Neurobiology, Harvard Medical School, Boston, MA 02115, USA 2 These authors contributed equally 3 Lead contact 
4	Author Contributions S.-Y.T., S.N.C., and C.D.H. conceived of the project. S.N.C. developed the behavioral task. S.-Y.T. and S.N.C. performed the behavior and imaging experiments. C.A. and R.B.L. 
5	performed the photoinhibition experiments. S.-Y.T. and S.N.C. analyzed the data. C.D.H. provided input on all aspects of the project and obtained funding for the project. S.-Y.T., S.N.C., and C.D.H. 
6	wrote the manuscript with input from C.A. * Correspondence: [removed: an e-mail address] 03 8 2022 08 6 2022 110 15 414107 2484 2502.e16 15 06 2022 03 08 2023 03 08 2023 08 08 2022 12 08 2025 This file is 
7	available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Summary Animals adaptively integrate sensation, planning, and action to navigate 
8	toward goal locations in ever-changing environments, but the functional organization of cortex supporting these processes remains unclear. We characterized encoding in approximately 90,000 neurons 
9	across mouse posterior cortex during a virtual-navigation task with rule-switching. The encoding of task and behavioral variables was highly distributed across cortical areas but differed in 
10	magnitude, resulting in three spatial gradients encoding visual cue, spatial position plus dynamics of choice formation, and locomotion, with peaks respectively in visual, retrosplenial, and pari
[... 290 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 300,
 "limit": 300
}
```

```
300	mm-diameter inner coverslips and one 4.0 mm-diameter outer coverslip (#1 thickness, Warner Instruments) bonded together using optical adhesive (Norland Optics NOA 65) was inserted and sealed with 
301	dental cement. Mice were then put on behavioral training. After they learned to reliably perform the task, they were anesthetized again for injection of adeno-associated virus (AAV) after one day of 
302	free access to water. The dental cement around the window and the glass plug were removed, and 60–100 nL of AAV2/1-synapsin-GCaMP6s-WPRE-SV40 (U. Penn Vector Core, cat. no. AV-1-PV2824) diluted in 
303	phosphate-buffered saline (1/10 dilution with final titer ~4 × 10 12 gc/ml) was injected into layer 2/3 and layer 5 (250 μm and 500 μm below the pia surface, respectively). Injections were targeted 
304	to 7–9 sites spaced evenly across areas of interest, including primary visual cortex (V1), posteromedial (PM), anteromedial (AM), mediomedial (MM), retrosplenial cortex (RSC), and anterior (A). 
305	Gradual and continuous injections were made using a glass pipette and a custom air-pressure system over 2–3 min per depth per site, and the pipette was left in place for an additional 3–5 min. A new 
306	glass plug was then inserted and sealed with dental cement. Before the headplate implantation, mice were also injected with two retrogradely transported AAVs (AAV2retro-Syn-mTagBFP2 undiluted with 
307	concentration ~1.5 × 10 13 gc/ml and AAV2retro-Syn-mScarlet 1/5 dilution in PBS with final concentration ~5 × 10 11 gc/ml, both obtained from Boston Children’s Hospital Viral Core) in projection 
308	target areas of posterior cortex. Mice were injected with AAVretro-mTagBFP2 and mScarlet into one of the two sets of targets through craniotomies on the left hemisphere: (1) anterior ACC/M2 (3 sites: 
309	1 mm anterior, 0.5 mm lateral, 0.3 and 1.0 mm in depth; 1 mm anterior, 0.8 mm lateral, 0.4 mm in depth; 300 nl AAVretro-mTagBFP2 per site) and dorsomedial striatum (3 sites: 1 
[... 290 more lines not kept]
```

**Agent**

The full text, Methods, and supplement figure legends are all there. I'm reading the rest of the Methods now.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 600,
 "limit": 292
}
```

```
600	nearest neighbor of the mean normalized mutual information based on the normalized mutual information vs. random fraction or jitter curve. The selection procedure for epoch-specific active neurons 
601	resulted in 47% of neurons active during stem traversal (total 20,202 neurons; V1: 3641, PM: 2313, AM: 3350, MM: 1855, RSC: 5720, A: 3323) and 30% of neurons active in feedback period/ITI (total 
602	12,719 neurons; V1: 2441, PM: 1208, AM: 1756, MM: 1040, RSC: 2341, A: 3933). Besides the mutual information-based methods, we also performed a complementary approach to quantify the degree of 
603	distributedness based on decoding with discretized area labels. For each of the selected variables, we first identified the area with the highest average encoding strength, e.g. V1 for cue and area A 
604	for movement, and used logistic regression to decode neurons residing in this area from neurons in all other 5 areas based on the encoding strength of that variable, which we called “max vs. others” 
605	decoding ( Figure S6D ). Separately, we constructed 15 pairwise decoders that distinguished neurons from each pair of areas. Decoding was done using the LogisticRegression function from Scikit-learn 
606	with leave-one-mouse-out cross validation, and we reported the area under ROC on held-out data as an alternative measurement of the degree of distributedness. The auROC would equal 1 for the fully 
607	modular case and 0.5 for the fully distributed one. We subsampled 1000 neurons from each area for this analysis and repeated it 1000 times to compute mean and standard error. Decoding anatomical 
608	locations from single-neuron encoding profiles These analyses refer to Figure 6A , 6B and Figure S6E , S6F . To relate a neuron’s encoding properties to its anatomical location in the cortical space, 
609	we decoded each neuron’s cortical location from its GLM-derived encoding profile ( Figure 6A ). For each neuron, we computed the encoding profile as the mean fraction explained 
[... 282 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=paper/*.txt; sed -n '517,600p;844,907p' $f
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/*.txt; sed -n '1323,1364p;1826,1935p' $f | grep -v '^[0-9. -]*$'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/*.txt; sed -n '2271,2403p;2614,2816p' $f | grep -v '^[0-9. -]*$' | awk 'length($0)>40'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/*.txt; sed -n '2985,3192p;3378,3447p' $f | grep -v '^[0-9. -]*$' | awk 'length($0)>30'
```

Result: not kept, because it reads the paper's text.

**Agent**

Paper, Methods and supplement legends are all present. Next: the dataset's archive description and the linked GLM code (Zenodo badge 491659726).

**Agent calls Bash**

```bash
cd  grep -rl "000579" --include=*.json --include=*.yaml --include=*.md --include=*.csv . 2>/dev/null | head; curl -s https://api.github.com/repositories/491659726 | head -c 1500
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '000579' in json.dumps(x): print(json.dumps(x,indent=1)[:3000])
"; grep -n -B2 -A12 "000579" papers/manifest.yaml | head -40; cd $TMPDIR && git clone -q https://github.com/sytseng/GLM_Tensorflow && cd GLM_Tensorflow && git log -1 --format='%H %ad' && ls -R | head -30
```

```
[
 {
  "dandiset": "000003",
  "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
  "published_version": "0.260218.2052",
  "asset_count": 101,
  "size_gb": 2559.25,
  "data_standards": [
   "Neurodata Without Borders (NWB)"
  ],
  "species": [
   "House mouse"
  ],
  "approaches": [
   "electrophysiological approach",
   "behavioral approach"
  ],
  "papers": [
   {
    "doi": "10.1016/j.neuron.2016.12.011",
[... 124 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
for x in d:
  if x['dandiset']=='000579': print(json.dumps(x,indent=1))
"; cd $TMPDIR/GLM_Tensorflow; cat README.md; git log --format='%h %ad %s' | head; wc -l glm_code/*; grep -n "def \|lambda\|log_poisson\|group" glm_code/glm_core_functions.py | head -80
```

```
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    if x['dandiset']=='000579': print(json.dumps(x,indent=1))
       ~^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
# GLM_Tensorflow
This repository contains code used in Tseng et al. 2022 for fitting generalized linear models (GLM) in Tensorflow 1. 

For an updated version of the code in Tensorflow 2 and tutorials for using it and fitting GLMs to real calcium imaging data, please visit the repository [**GLM_Tensorflow_2**](https://github.com/sytseng/GLM_Tensorflow_2). 

## Software requirements for this version of code:
- numpy 1.16.2
- tensorflow 1.13.1
- scipy 1.5.2
- statesmodels 0.11.1
- matplotlib 3.0.3

## References:
Tseng, S.-Y., Chettih, S.N., Arlt, C., Barroso-Luque, R., and Harvey, C.D. (2022). Shared and specialized coding across posterior cortical areas for dynamic navigation decisions. Neuron 110, 2484–2502.e16. [[link]](https://www.sciencedirect.com/science/article/pii/S0896627322004536) 
75a1314 Wed Sep 7 16:57:29 2022 -0400 Update README.md
[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/GLM_Tensorflow; sed -n 410,740p glm_code/glm_core_functions.py
```

```
return w_series_dict, lambda_series, loss_trace_dict, lambda_trace_dict, all_prediction, all_deviance


# In[4]:


def stable(x):
    return x + 10 * np.finfo(x.dtype).tiny


# In[5]:


def deviance(mu, y, loss_type = 'poisson'):
    """Calculate Poisson-devinace-explained between pairs of columns from the matrices mu and y.
    See MATLAB getDeviance.m
    The version here has improved numerical stability.
    """
    assert (mu.shape == y.shape), "Shapes " + str(mu.shape) + " and " + str(y.shape) + " don't match!"

[... 312 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
print(type(d), list(d)[:5] if isinstance(d,dict) else '')
items = d['dandisets'] if 'dandisets' in d else d
for x in items:
  if isinstance(x,dict) and x.get('dandiset')=='000579': print(json.dumps(x,indent=1))
"
```

```
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
```

**Agent calls Bash**

```bash
cd  grep -n "make_prior_matrix\|^import\|^from\|se_fraction" $TMPDIR/GLM_Tensorflow/glm_code/glm_core_functions.py | head; sed -n 60,100p $TMPDIR/GLM_Tensorflow/glm_code/glm_core_functions.py; python3 -c "
import json;d=json.load(open('targets/dandisets.json'))['targets']
for x in (d if isinstance(d,list) else d.values()):
  if '000579' in json.dumps(x): print(json.dumps(x,indent=1)[:3000])
"
```

```
7:import numpy as np
8:import tensorflow as tf
9:from time import time
10:import matplotlib
11:import matplotlib.pyplot as plt
47:        prior, grouping_mat, feature_group_size, _, _ = make_prior_matrix(pred_name_list)
232:        prior, grouping_mat, feature_group_size, _, _ = make_prior_matrix(pred_name_list)
660:def select_model_cv(w_series_dict, lambda_series, all_deviance, n_folds, se_fraction, 
687:        threshold = min_deviance + this_se * se_fraction
        lam = tf.placeholder(tf.float32, name='lambda')

        # weights
        w0 = tf.Variable(tf.zeros((1, n_roi), dtype=tf.float32), name='intercept')
        initial_w = np.zeros((n_features, n_roi), np.float32) + 1e-5  # The gradient is not defined at zero so initialize with small number
        w = tf.Variable(tf.convert_to_tensor(initial_w), name='weight')

        # model definition
        Y_hat = tf.matmul(X, w) + w0
            
        if activation == 'exp':
[... 57 more lines not kept]
```

**Agent**

Code read: `sytseng/GLM_Tensorflow` at 75a1314 holds only the GLM fitting functions. Now checking the claims file schema and the checker.

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py; grep -n "^[a-z_]*:\|^  [a-z_]*:\|^- \|^  - [a-z]\|^    [a-z_]*:" claims/001453/*.yaml | awk -F: '{print $3}' | sort | uniq -c | sort -rn | head -40
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

[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1))" | head -250
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
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"; grep -n -A30 "id: fig1d-median-velocity" claims/001453/*.yaml | head -45
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
[... 113 more lines not kept]
```

**Agent**

I have what I need: the full text (PMC author manuscript) with Methods, the supplement legends S1 to S8, and the GLM code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000579/10.1016-j.neuron.2022.05.012.yaml",
 "content": "# Claims for Tseng, Chettih, Arlt, Barroso-Luque & Harvey (2022), Neuron 110, 2484-2502, on\n# dandiset 000579 (\"Two-photon calcium imaging of mouse posterior cortical areas during dynamic\n# navigation decisions (Tseng et al., 2022, Neuron)\").\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the accepted author manuscript in PubMed Central (PMC9357051, NIHMS1810369), full\n# text with Results, figure legends and STAR Methods, and its one supplement file (Figures S1 to\n# S8 with legends), as stored in paper/10.1016-j.neuron.2022.05.012.txt. The version of record\n# was not read. No main-text PDF was available, so Figures 1 to 8 were read from their legends\n# and the Results only.\n#\n# Code read: github.com/sytseng/GLM_Tensorflow at commit 75a1314 (the repository behind the\n# paper's Zenodo badge 491659726). It holds glm_core_functions.py only, the Tensorflow 1 GLM\n# fitting functions (Poisson loss with group lasso or elastic net, cross-validated fits over a\n# lambda series, deviance and model selection). It does not hold make_prior_matrix (the\n# predictor grouping it calls), the design matrix, the analyses or the figures; the paper says\n# the other code is shared on request. Where it is used below it is cited.\n#\n# Data the paper used, as it reports them.\n# - Imaging and behavior. Eight male C57BL/6J mice, two-photon imaging of GCaMP6s through a\n#   cranial window over left posterior cortex while running a virtual Y-maze with rule switches\n#   (rule A black-left/white-right, rule B the reverse, blocks of 100 to 175 trials, 350 to 450\n#   trials and 2 to 3 switches per session). Volumes at 30 Hz in four planes, 6 Hz per plane.\n#   278,155 sources from 300 sessions; the neural analyses use 93,881 layer 2/3 neurons from\n#   141 sessions with task performance above 65% correct. All behavioral sessions are used for\n#   behavior; task performance figures use sessions above 0.5 correct (253 sessions) and the\n#   later behavioral analyses sessions above 0.65 (216 sessions in the S1 and S2 legends).\n#   Visually guided trials (0 to 20%) are excluded from all analyses. Measured variables are\n#   treadmill pitch, roll and yaw velocity, maze position, cue, choice, outcome, trial epochs\n#   (stem, arms, delay, feedback, reward/ITI), deconvolved activity of each neuron, and each\n#   neuron's location in the Allen CCF and area label (V1, PM, AM, MM, RSC, A).\n# - Photoinhibition. Seven male VGAT-ChR2-YFP mice, 164 sessions, bilateral light on PPC, RSC\n#   (3 spots), S1 or a control site, in blocks of 50 trials, on a smaller maze with bar cues.\n#   The dandiset's title names imaging only; whether it holds these sessions is for the author.\n#\n# Shared method, from the STAR Methods unless said otherwise; criteria below refer to it.\n# - Strategy variables (rule belief, choice bias, probability of actual choice, rule- and\n#   bias-following) come from a per-mouse LSTM (16 units, inputs current cue and previous\n#   cue, choice, outcome and the visually guided arm), leave-one-session-out, Adam, batch 1,\n#   learning rate 0.1, L2 0.0123. Dynamic choice (P left) and cue-biased running (P black) come\n#   from a per-session LSTM (10 units) on the three velocities and forward position, 6-fold\n#   cross-validation repeated 6 times and averaged, Adam, batch 100, learning rate 0.1, L2 0.1,\n#   extended 5 s into the feedback period/ITI. Random seeds are a standard choice.\n# - GLM. Poisson GLM on deconvolved activity, with the predictors of the Methods (27 task\n#   variables on 20 position and 16 temporal raised-cosine bases, 336 movement predictors from\n#   rank-transformed velocities and accelerations on 7-df b-splines, and drift terms), z-scored.\n#   Fit with Adam (learning rate 0.001), Poisson loss and group lasso (the code's fit_glm_cv),\n#   trials split 80% train and 20% test, 5-fold cross-validation on the training trials over 21\n#   log-spaced lambda values from 1e-5 to 1e-1 (the code's default series, 30 values from 1e-1\n#   to 1e-8, differs; the Methods are followed). Neurons with more than 10% of null deviance\n#   explained by the drift terms are excluded. Well-fit neurons have test fraction deviance\n#   explained above 0.2 (42,998 neurons).\n# - Open in the GLM, named here once for every claim that uses it. (1) How lambda is chosen.\n#   The Methods say the mean CV deviance is \"compared across all lambda values to select the\n#   optimal one\", read as (a) the lambda of minimum mean CV deviance; the code's\n#   select_model_cv takes (b) the largest lambda whose mean CV deviance is within se_fraction\n#   standard errors of the minimum, with se_fraction not given, read as 1. Reading (a) is the\n#   main one; (b) is run as a variant. (2) The grouping of predictors for the penalty is not in\n#   the code; the Methods' rule (all basis functions of one variable form one group) is\n#   followed. (3) Whether the drift exclusion is applied before or after the 93,881 count is\n#   not said; both are shown where a count depends on it.\n# - Encoding strength is the fraction explained deviance without re-fitting (Figure S3G),\n#   computed on the CV held-out data in 36 trial-phase bins and normalized by the full model's\n#   explained deviance; an epoch's value is the mean over the bins in that epoch. The stem\n#   epoch is maze traversal before the Y-intersection (200 of 250 cm); whether the bins that\n#   straddle the intersection count is not said, so the readings are bins wholly in the stem\n#   and bins with their centre in the stem. Encoding correlations (Figure 7) use the fraction\n#   null deviance with re-fitting (Figure S3H), as the Methods say.\n# - Statistics. Hierarchical bootstrap, mice then neurons (or decoders, sessions, switches,\n#   trials), 1,000 samples for neural and 10,000 for behavioral quantities; two-tailed p as\n#   twice the smaller tail; Benjamini-Hochberg at FDR 0.05 where several tests are run at once.\n#   \"p < 10-3\" from 1,000 samples means no bootstrap sample crossed zero.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000579\"\npaper: doi:10.1016/j.neuron.2022.05.012\nclaims:\n- id: neuron-counts\n  statement: The neural analyses use 93,881 layer 2/3 neurons from 141 sessions of 8 mice,\n    parcellated into V1 (14,373), PM (9,564), AM (14,974), MM (9,885), RSC (23,036) and A\n    (22,049).\n  source: Results, Calcium imaging of neural activity across posterior cortex, paragraph 1;\n    STAR Methods, Area parcellation\n  quote: assigned coordinates to 93,881 layer 2/3 neurons imaged from 141 sessions of 8 mice ...\n    we obtained 14,373 neurons in V1, 9,564 neurons in PM, 14,974 neurons in AM, 9,885 neurons in\n    MM, 23,036 neurons in RSC, and 22,049 neurons in area A\n  expected:\n  - quantity: layer 2/3 neurons analysed\n    value: 93881\n    tolerance: 9388\n  - quantity: sessions\n    value: 141\n    tolerance: 14\n  - quantity: mice\n    value: 8\n    tolerance: 0\n  - quantity: neurons in V1\n    value: 14373\n    tolerance: 1437\n  - quantity: neurons in PM\n    value: 9564\n    tolerance: 956\n  - quantity: neurons in AM\n    value: 14974\n    tolerance: 1497\n  - quantity: neurons in MM\n    value: 9885\n    tolerance: 989\n  - quantity: neurons in RSC\n    value: 23036\n    tolerance: 2304\n  - quantity: neurons in A\n    value: 22049\n    tolerance: 2205\n  criterion: Counted over layer 2/3 cell-body sources in sessions above 65% correct (STAR\n    Methods, Classification of the sources), with area labels from the paper's parcellation\n    (STAR Methods, Area parcellation). The number of mice is exact (tolerance 0, a count of\n    subjects); the others take the default 10%. If the dataset gives no area labels the area\n    counts are untestable and the claim is judged on the totals.\n- id: fig1d-switch-performance\n  statement: Performance is high before a rule switch, typically falls below chance after it,\n    and recovers gradually to high accuracy by the end of the block.\n  source: Results, Mice learned flexible cue-choice associations, paragraph 2; Figure 1D;\n    Figure S1B\n  quote: Their behavioral performance was high before rule switches and typically dropped below\n    chance after switches before gradually recovering to high accuracy by the end of a block,\n    without signs of anticipating rule switches\n  criterion: From the STAR Methods, Task performance analysis, on sessions with overall\n    fraction correct above 0.5 and visually guided trials excluded. Each block's outcomes are\n    fit with the sigmoid of the Methods (reward rate as L over one plus exp of minus (t - t0)\n    over k, plus b) by minimizing cross-entropy; initial and end performance are the fitted\n    values at the first and last trial. The parameter constraints are not given; a standard\n    choice (L and b keeping the rate within 0 to 1, k positive) is used, which should not change\n    the outcome. Reproduced when, over switches (hierarchical bootstrap, mice then switches),\n    the mean fitted initial performance after a switch is below 0.5 and the mean fitted end\n    performance is above 0.7 and above the initial performance (two-tailed p < 0.05).\n    Partially reproduced when the fall and recovery hold but the initial value is not below\n    0.5.\n- id: lstm-choice-accuracy\n  statement: The strategy LSTM predicts the mouse's choices in held-out sessions with 80.2% ±\n    5.1% accuracy (mean ± SD).\n  source: Results, Decision-making strategy varied, paragraph 1; STAR Methods, LSTM model\n  quote: The LSTM accurately predicted a mouse's choices in held-out sessions (80.2% ± 5.1%, mean\n    ± SD)\n  expected:\n  - quantity: held-out choice prediction accuracy, mean\n    value: 0.802\n    tolerance: 0.051\n  criterion: The LSTM of the STAR Methods (16 units, leave-one-session-out per mouse), with its\n    stated hyperparameters. A choice is predicted correct when the model's probability for the\n    actual cue gives more than 0.5 to the actual choice. The tolerance is the reported SD, the\n    paper's stated spread. Open, with readings run in turn. (a) The SD is over sessions or (b)\n    over mice; (c) sessions are all behavioral sessions or (d) those above 0.65 correct, which\n    the Methods use for the later analyses. Reproduced when the mean is within tolerance under\n    any reading.\n- id: figs1h-lstm-beats-rl\n  statement: The LSTM predicts choices better (higher log likelihood) than the best\n    reinforcement learning model (model 4, separate learning rates for rewarded and unrewarded\n    trials).\n  source: Figure S1H\n  quote: Log likelihood of the LSTM was greater than the RL model (p = 5.95 × 10-22, Wilcoxon\n    signed rank test)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 5.95e-22\n    n: 216 sessions\n  criterion: Session-averaged held-out log likelihood (log base 2) of the LSTM and of RL model\n    4 of the STAR Methods (Q learning with decay, separate learning rates for rewarded and\n    unrewarded trials, choice perseverance, bias and lapse), both leave-one-session-out per\n    mouse, on the 216 sessions. Reproduced when the LSTM is higher with a Wilcoxon signed-rank p\n    < 0.05. The form of the lapse term is garbled in the text; the standard mixture (one minus\n    lambda times the softmax plus lambda over two) is used.\n- id: fig1i-strategy-after-switch\n  statement: Before a switch mice show little choice bias and follow the rule; after a switch\n    the probability of the actual choice falls near chance, bias-following rises moderately, and\n    rule-following then recovers gradually.\n  source: Results, Decision-making strategy varied, paragraph 2; Figure 1I\n  quote: On average, prior to a rule switch, mice performed with little choice bias and followed\n    the correct rule ... After a rule switch, the randomness of choices increased rapidly, as seen\n    by near chance levels of the model's probability of the actual choice, and bias-following\n    increased moderately. Then, rule-following recovered gradually for the new rule belief\n  criterion: Strategy variables from the LSTM (shared method), aligned to switches, on the 265\n    switches of Figure 1I (switches with end performance above 70%, sessions above 0.65\n    correct). The windows are not given; the readings are the 10 and the 20 trials before and\n    after the switch (20 is the window the Methods use for trajectory correlation). Reproduced\n    when, under every reading, (1) rule-following before the switch is above zero, (2)\n    probability of actual choice in the first window after the switch is lower than before and\n    within 0.1 of 0.5 at its minimum, (3) bias-following after is higher than before, and (4)\n    rule-following after the first window rises toward its pre-switch level by the end of the\n    block; each comparison by hierarchical bootstrap (mice then switches), two-tailed p < 0.05.\n    The 0.1 margin for near chance is a choice of this file, as the paper gives none; the\n    value is reported.\n- id: visually-guided-rule-update\n  statement: Visually guided trials do not update rule belief more than normal trials in the\n    30 trials after a switch (0.013 ± 0.0055 against 0.0080 ± 0.0023; p = 0.34).\n  source: STAR Methods, Decision-making strategy variables, last paragraph\n  quote: The rule update per trial was 0.013 ± 0.0055 for visually guided trials and 0.0080 ±\n    0.0023 for normal trials (difference = 0.0052 ± 0.0057, p = 0.34, hierarchical bootstrap mean\n    ± SEM, n = 265 switches)\n  statistics:\n  - about: visually guided against normal trials, all trials\n    test: hierarchical bootstrap\n    p: 0.34\n    n: 265 switches\n  - about: visually guided against normal trials, correct trials only\n    test: hierarchical bootstrap\n    p: 0.89\n    n: 265 switches\n  expected:\n  - quantity: rule update per trial, visually guided\n    value: 0.013\n    tolerance: 0.0055\n  - quantity: rule update per trial, normal\n    value: 0.008\n    tolerance: 0.0023\n  criterion: Delta rule belief per trial toward the current rule (signed so that positive is\n    toward the new rule), averaged over the 30 trials after each switch, compared by\n    hierarchical bootstrap (mice then switches), two-tailed. A claim of absence. Reproduced when\n    p >= 0.05, as the paper's test found; not reproduced when p < 0.05. The difference is\n    reported either way. Tolerances are the reported SEMs.\n- id: fig1l-photoinhibition-performance\n  statement: Inhibiting RSC or PPC lowers task performance compared with control trials and\n    with S1 inhibition; RSC and PPC do not differ.\n  source: Results, Photoinhibition of posterior cortical areas, paragraph 1; Figure 1L\n  quote: Inhibiting either RSC or PPC led to markedly lower task performance compared to control\n    trials or trials in which part of primary somatosensory cortex (S1) was inhibited\n  statistics:\n  - about: control against RSC or PPC\n    test: hierarchical bootstrap\n    p: 0.0001\n    p_relation: \"<\"\n    n: 164 sessions from 7 mice\n  - about: control against S1\n    test: hierarchical bootstrap\n    p: 0.0002\n    n: 164 sessions from 7 mice\n  - about: S1 against RSC or PPC\n    test: hierarchical bootstrap\n    p: 0.0001\n    p_relation: \"<\"\n    n: 164 sessions from 7 mice\n  - about: RSC against PPC\n    test: hierarchical bootstrap\n    p: 0.058\n    n: 164 sessions from 7 mice\n  criterion: STAR Methods, Analysis of photoinhibition experiments. Fraction correct on target\n    trials against control trials within session, by the modified hierarchical bootstrap\n    (10,000 samples of session means, mice then sessions, averaged within mouse then across\n    mice). Reproduced when RSC and PPC are each below control and below S1 with two-tailed p <\n    0.05. The RSC against PPC difference is reported.\n- id: fig1m-rule-following-decrease\n  statement: Inhibition of PPC and RSC decreases rule-following compared with control trials\n    and with S1 inhibition; bias-following increases, strongly in a subset of mice.\n  source: Results, Photoinhibition of posterior cortical areas, paragraph 2; Figure 1M; Figure\n    S1K\n  quote: PPC and RSC inhibition decreased rule-following compared to control trials and S1\n    inhibition\n  statistics:\n  - about: rule-following, each target against control\n    test: hierarchical bootstrap\n    p: 0.0001\n    p_relation: \"<\"\n    n: 164 sessions from 7 mice\n  - about: rule-following, RSC and PPC against S1\n    test: hierarchical bootstrap\n    p: 0.0001\n    p_relation: \"<\"\n    n: 164 sessions from 7 mice\n  - about: bias-following, S1 against control\n    test: hierarchical bootstrap\n    p: 0.025\n    n: 164 sessions from 7 mice\n  - about: bias-following, RSC against control\n    test: hierarchical bootstrap\n    p: 0.018\n    n: 164 sessions from 7 mice\n  - about: bias-following, PPC against control\n    test: hierarchical bootstrap\n    p: 0.0001\n    p_relation: \"<\"\n    n: 164 sessions from 7 mice\n  criterion: The strategy LSTM with one input per inhibition target (STAR Methods, LSTM model),\n    target trials against control trials within session by the modified hierarchical bootstrap\n    of the photoinhibition Methods. Reproduced when rule-following is lower than control for\n    RSC and PPC and lower than for S1, each with two-tailed p < 0.05. Bias-following changes\n    are reported, with the number of mice whose increase exceeds 0.2 (the paper finds 3 for RSC\n    and 1 for PPC).\n- id: figs1m-rule-bias-uncorrelated\n  statement: Across sessions, the change in rule-following under RSC or PPC inhibition is not\n    correlated with the change in bias-following.\n  source: Figure S1M\n  quote: Pearson correlation 0.18 (p = 0.10 vs. zero) for RSC and -0.03 (p = 0.74) for PPC\n  statistics:\n  - about: RSC\n    test: Pearson correlation against zero\n    statistic: r = 0.18\n    p: 0.1\n    n: 164 sessions from 7 mice\n  - about: PPC\n    test: Pearson correlation against zero\n    statistic: r = -0.03\n    p: 0.74\n    n: 164 sessions from 7 mice\n  depends_on:\n  - fig1m-rule-following-decrease\n  criterion: Per session, target minus control for rule-following and for bias-following; the\n    Pearson correlation across sessions tested against zero. A claim of absence. Reproduced\n    when p >= 0.05 for both RSC and PPC; not reproduced when either is p < 0.05. The r values\n    are reported.\n- id: fig2c-running-variability-after-switch\n  statement: Running trajectories of choice-matched trials become less correlated with one\n    another after a rule switch.\n  source: Results, Running trajectories reflected the within-trial dynamics, paragraph 1;\n    Figure 2C\n  quote: This variability in running trajectories increased following a rule switch\n  criterion: STAR Methods, Running trajectory correlation analysis. Velocities binned on a grid\n    of maze positions, Pearson correlation of each pair of choice-matched trials averaged over\n    the three velocities, each trial's mean against the session's mean over all choice-matched\n    pairs, aligned to switches; mean over the 20 trials before against the 20 trials after.\n    The position grid is not given; the readings are 20 and 11 equal bins of the maze (the\n    counts the paper uses for its position bases and decoders). Reproduced when, under both,\n    Delta trajectory correlation is lower after than before with a hierarchical bootstrap\n    (mice then switches, 10,000 samples) two-tailed p < 0.05; the paper reports no test, and\n    this is its default.\n- id: fig2f-latency-strategy\n  statement: Dynamic choice crosses threshold sooner on trials with higher rule-following or\n    bias-following.\n  source: Results, Running trajectories reflected the within-trial dynamics, paragraph 3;\n    Figure 2F\n  quote: As expected, the latency to dynamic choice crossing a threshold was shorter on trials\n    with higher rule- or bias-following\n  expected:\n  - quantity: session-averaged trial duration, mean\n    value: 8.95\n    tolerance: 2.04\n    unit: s\n  criterion: Latency is the time from trial onset at which dynamic choice reaches 0.9 on left\n    trials or 0.1 on right trials, divided by the session's mean trial duration (STAR Methods,\n    Modeling of dynamic choice); n = 85,463 trials in the paper. The strategy bins of the\n    figure are not given in the text; the readings are 5 and 10 quantile bins of each strategy\n    variable, and the Spearman correlation over trials. Reproduced when latency falls with\n    rule-following and with bias-following under every reading (Spearman rho below zero, and\n    the highest bin shorter than the lowest by hierarchical bootstrap, mice then trials,\n    two-tailed p < 0.05). The duration tolerance is the reported SD.\n- id: fig2g-choice-commitment\n  statement: With high rule-following, choice commitment starts near chance and rises during\n    the maze; with low rule-following it stays low until late; with high bias-following it is\n    high from trial onset.\n  source: Results, Running trajectories reflected the within-trial dynamics, paragraph 3;\n    Figure 2G; Figure S2L\n  quote: On trials with high rule-following, choice commitment started near chance but increased\n    rapidly during maze traversal ... when rule-following was low, choice commitment was low until\n    late in the trial ... when mice followed a bias, choice commitment was high at trial onset\n  criterion: Choice commitment is the log likelihood (base 2) of the reported choice under\n    dynamic choice at each position (STAR Methods, Modeling of dynamic choice). Tested as in\n    Figure S2L (its Methods are in the legend). Per session, choice commitment at each maze\n    position bin is regressed on rule-following, bias-following and local reward rate (fraction\n    correct over the adjacent 9 trials); coefficients are averaged by hierarchical bootstrap\n    over 216 sessions. Reproduced when the bias-following coefficient is above zero in the\n    first position bin and the rule-following coefficient is not (two-tailed p >= 0.05 or\n    smaller than a tenth of the bias coefficient), and the rule-following coefficient in the\n    last stem bin is above zero and above its first-bin value (p < 0.05). The number of position\n    bins is not given; 11 equal bins (the paper's decoder bins) and 20 are both run.\n- id: cue-biased-running-uncorrelated\n  statement: Cue-biased running varies across mice and sessions and is not correlated with task\n    performance.\n  source: Results, Running trajectories reflected the within-trial dynamics, paragraph 2;\n    Figure S2H, S2I, S2K\n  quote: this behavior was variable across mice and sessions and was uncorrelated with task\n    performance and the time course of dynamic choice\n  criterion: Strength of cue-biased running is the session-averaged log likelihood of the cue\n    under cue-biased running (STAR Methods, Modeling of dynamic choice). The paper reports no\n    test; Figure S2I shows per-mouse regression lines. A claim of absence, with the readings\n    (a) Pearson correlation of session cue decoding against session fraction correct, pooled\n    over sessions, and (b) the per-mouse regression slopes tested against zero across mice.\n    Reproduced when neither finds a correlation at p < 0.05; mixed results are reported as such.\n    The sign of the roll-velocity coefficient of the logistic cue decoder (first 25% of the\n    stem, 10-fold) is reported per session to show the variation of Figure S2K.\n- id: fig3i-glm-fit\n  statement: The GLM explains a fraction 0.25 ± 0.17 (mean ± SD) of the Poisson deviance of\n    single neurons on held-out test data.\n  source: Results, Calcium imaging of neural activity, paragraph 2; Figure 3I; Figure S3E\n  quote: >-\n    The GLM explained a substantial amount of moment-to-moment variability in a neuron's\n    activity (fraction of Poisson deviance explained: 0.25 ± 0.17, mean ± SD\n  expected:\n  - quantity: test fraction deviance explained, mean over neurons\n    value: 0.25\n    tolerance: 0.025\n  - quantity: test fraction deviance explained, SD over neurons\n    value: 0.17\n    tolerance: 0.017\n  criterion: GLM as in the opening comment, over the 93,881 neurons, test data (20% of trials).\n    The tolerances are 10%. The SD is the spread over neurons, not the uncertainty of the mean,\n    so it is not used as the mean's tolerance.\n- id: well-fit-neurons\n  statement: 42,998 neurons have test fraction deviance explained above 0.2 (V1 7,775, PM\n    4,934, AM 6,878, MM 3,991, RSC 10,329, A 9,091); 68,532 pass a threshold of 0.1.\n  source: STAR Methods, Generalized Linear Models, Fitting procedure; Figure S3D\n  quote: 42,998 neurons were selected, including 7,775 neurons in V1, 4,934 neurons in PM, 6,878\n    neurons in AM, 3,991 neurons in MM, 10,329 neurons in RSC, and 9,091 neurons in area A\n  expected:\n  - quantity: well-fit neurons (above 0.2)\n    value: 42998\n    tolerance: 4300\n  - quantity: well-fit neurons in V1\n    value: 7775\n    tolerance: 778\n  - quantity: well-fit neurons in PM\n    value: 4934\n    tolerance: 493\n  - quantity: well-fit neurons in AM\n    value: 6878\n    tolerance: 688\n  - quantity: well-fit neurons in MM\n    value: 3991\n    tolerance: 399\n  - quantity: well-fit neurons in RSC\n    value: 10329\n    tolerance: 1033\n  - quantity: well-fit neurons in A\n    value: 9091\n    tolerance: 909\n  - quantity: neurons above 0.1\n    value: 68532\n    tolerance: 6853\n  depends_on:\n  - neuron-counts\n  - fig3i-glm-fit\n  criterion: Counted from the GLM fits of fig3i-glm-fit, under both lambda readings and both\n    orders of the drift exclusion (opening comment).\n- id: glm-cv-vs-test\n  statement: Fraction explained deviance on the CV held-out data differs very little from that\n    on the test data (0.0010 ± 0.0006, mean ± SEM), so encoding measured on CV held-out data is\n    not inflated by overfitting.\n  source: STAR Methods, Quantification of fraction explained deviance (without re-fitting);\n    Figure S3E\n  quote: We confirmed that the difference in the fraction explained deviance evaluated on the CV\n    held-out data and test data was sufficiently small (0.0010 ± 0.0006, mean ± SEM\n  expected:\n  - quantity: CV held-out minus test fraction deviance explained\n    value: 0.001\n    tolerance: 0.0006\n  depends_on:\n  - fig3i-glm-fit\n  criterion: Mean over neurons of the CV held-out minus the test fraction deviance explained;\n    SEM over neurons. The tolerance is the reported SEM. Which neurons enter (all 93,881 or the\n    42,998 well-fit) is not said; both are reported, and the claim is reproduced when either\n    is within tolerance.\n- id: fig3m-movement-task-gradient\n  statement: Area A has higher encoding of instantaneous movement and lower encoding of task\n    variables than every other area, and V1 has higher task-variable encoding than every other\n    area.\n  source: Results, Distinct encoding gradients, paragraph 1; Figure 3M\n  quote: the encoding of task variables exhibited an anterior-posterior gradient with highest\n    strength in V1, intermediate in RSC, and lowest in area A, whereas movement encoding strength\n    exhibited a gradient in the opposite direction\n  statistics:\n  - about: A against every other area, movement (higher) and task variables (lower)\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n    n: 42,998 well-fit neurons from 8 mice\n  - about: V1 against every other area, task variables\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n    n: 42,998 well-fit neurons from 8 mice\n  depends_on:\n  - well-fit-neurons\n  criterion: Encoding strength (opening comment) of the group of all movement variables and the\n    group of all task variables over the whole trial, per well-fit neuron, averaged per area by\n    hierarchical bootstrap (mice then neurons, 1,000 samples). Reproduced when A is above every\n    other area for movement and below every other area for task variables, and V1 above every\n    other area for task variables, each with two-tailed p < 0.05 after Benjamini-Hochberg over\n    the area pairs. Partially reproduced when the ordering holds but some pair is not\n    significant. The same test at the 0.1 fit threshold (Figure S8K) is shown as a variant.\n- id: fig3o-cue-gradient\n  statement: Cue encoding during stem traversal is strongest in V1 (higher than every other\n    area), strong in AM and PM, weaker in RSC and weakest in A (lower than every other area).\n  source: Results, Distinct encoding gradients, paragraph 2; Figure 3O; Figure S4K\n  quote: Encoding of the visual cue identity was strongest in V1 and neighboring areas AM and PM,\n    weaker in RSC, and weakest in area A\n  statistics:\n  - about: V1 higher than every other area\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n  - about: A lower than every other area\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - well-fit-neurons\n  criterion: Encoding strength of cue in the stem epoch per well-fit neuron, area means by\n    hierarchical bootstrap. Reproduced when V1 is above and A below every other area (two-tailed\n    p < 0.05, Benjamini-Hochberg over pairs), and the means of AM and PM exceed that of RSC.\n- id: fig3q-cue-decoding\n  statement: Cue decoded from populations of about 100 nearby neurons follows the same\n    gradient as single-neuron cue encoding.\n  source: Results, Distinct encoding gradients, paragraph 2; Figure 3Q\n  quote: which was corroborated with decoding of these variables from the activity of ~100\n    simultaneously recorded neurons\n  criterion: STAR Methods, Trial phase-specific logistic decoders. Simultaneously imaged\n    neurons split into spatially adjacent, non-overlapping groups of about 100 (all layer 2/3\n    neurons, no fit selection), PCA to 90% variance, logistic regression with elastic net (10%\n    L1) in 11 position bins with 5-fold CV, performance as log likelihood (base 2); 974 decoders\n    in the paper. How the elastic net strength is chosen is not said; the readings are the\n    lambda of minimum CV deviance and the one-SE lambda (the two that MATLAB lassoglm returns).\n    How groups of about 100 are formed is not said; the readings are k-means on neuron\n    positions with k equal to the session's neurons over 100, and a grid of equal-count\n    tiles. Reproduced when, under every reading, the decoder means per area (by centroid) rank\n    V1 highest and A lowest, with V1 above A at two-tailed p < 0.05 (hierarchical bootstrap,\n    mice then decoders).\n- id: figs4l-strategy-distributed\n  statement: Encoding of decision-making strategy variables, with their interactions, is\n    moderate and does not differ between areas, except AM against A.\n  source: Results, Distinct encoding gradients, paragraph 3; Figure 3R; Figure S4L\n  quote: Variables related to the decision-making strategy, including their interactions with\n    other task variables, collectively exhibited a moderate encoding strength distributed evenly\n    across posterior cortex\n  statistics:\n  - about: all area pairs except AM against A\n    test: hierarchical bootstrap\n    p: 0.03\n    p_relation: \">\"\n    corrected: Benjamini-Hochberg (not significant after correction)\n  - about: AM against A\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - well-fit-neurons\n  criterion: Encoding strength of the group of all strategy variables and their interactions\n    over the full trial, area means by hierarchical bootstrap, two-tailed tests for the 15 area\n    pairs with Benjamini-Hochberg at FDR 0.05, as the legend states. A claim of absence for 14\n    pairs. Reproduced when no pair other than AM against A is significant after correction;\n    not reproduced when any other pair is. The AM against A result and all differences are\n    reported.\n- id: figs4p-previous-outcome\n  statement: The previous trial's outcome is encoded much more strongly than its cue or choice,\n    and evenly over space.\n  source: Results, Distinct encoding gradients, paragraph 3; Figure S4P to S4S\n  quote: The previous trial's outcome was much more strongly encoded than the previous trial's\n    cue or choice\n  depends_on:\n  - well-fit-neurons\n  criterion: Encoding strength of previous outcome, previous cue and previous choice in the\n    stem epoch per well-fit neuron. The paper reports no test. Reproduced when the mean over\n    neurons of previous outcome exceeds both others with hierarchical bootstrap two-tailed p <\n    0.05 (the Methods' default test), in every area. Evenness is reported as the area means;\n    it is not judged, as the paper gives no test for it.\n- id: fig4b-dynamic-choice-stem\n  statement: During stem traversal, dynamic choice is encoded more than reported choice in all\n    areas, most in RSC (above V1, PM and A, not different from AM and MM), while reported choice\n    encoding is not above zero.\n  source: Results, Encoding of dynamic choice was enriched in RSC, paragraph 1; Figure 4A, 4B\n  quote: during traversal of the maze stem, encoding of dynamic choice was distributed across all\n    areas but enriched in RSC and adjacent medial areas, accounting for a substantial amount of\n    neural activity compared to near-zero encoding of reported choice\n  statistics:\n  - about: dynamic against reported choice, each area\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n  - about: dynamic choice, RSC against V1, PM or A\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n  - about: dynamic choice, RSC against AM or MM\n    test: hierarchical bootstrap\n    p: 0.05\n    p_relation: \">\"\n  - about: reported choice, each area against zero\n    test: hierarchical bootstrap\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - well-fit-neurons\n  criterion: Encoding strength of dynamic choice and of reported choice in the stem epoch, area\n    means by hierarchical bootstrap. Reproduced when (1) dynamic exceeds reported in all six\n    areas, (2) RSC exceeds V1, PM and A, each two-tailed p < 0.05 after Benjamini-Hochberg, and\n    (3) reported choice is not above zero in any area at p < 0.05 (a claim of absence, on the\n    paper's bootstrap test). RSC against AM and MM is reported.\n- id: fig4c-reported-choice-feedback\n  statement: In the feedback period/ITI, reported choice is encoded more than dynamic choice in\n    all areas, and RSC encodes reported choice more than every other area.\n  source: Results, Encoding of dynamic choice was enriched in RSC, paragraph 1; Figure 4C\n  quote: In contrast, during the feedback and ITI periods, we observed greater encoding of\n    reported choice than dynamic choice\n  statistics:\n  - about: reported against dynamic choice, each area\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n  - about: reported choice, RSC against each other area\n    test: hierarchical bootstrap\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - well-fit-neurons\n  criterion: Encoding strength in the feedback period/ITI epoch (the 16 temporal bins after the\n    maze end), area means by hierarchical bootstrap. Reproduced when reported exceeds dynamic in\n    all six areas and RSC exceeds each other area for reported choice, two-tailed p < 0.05 after\n    Benjamini-Hochberg.\n- id: fig4d-partial-correlation\n  statement: Population decoders trained on reported choice are more related to dynamic choice\n    (partial correlation 0.35 ± 0.02) than to reported choice (0.14 ± 0.02), a difference of\n    0.21 ± 0.02.\n  source: Results, Encoding of dynamic choice was enriched in RSC, paragraph 2; Figure 4D\n  quote: Partial correlations were greater for dynamic choice than reported choice, revealing\n    that even decoders trained to predict reported choice were more closely related to dynamic\n    choice\n  statistics:\n  - about: difference of the two partial correlations against zero\n    test: bootstrap\n    p: 0.001\n    p_relation: \"<\"\n    n: 974 decoders\n  expected:\n  - quantity: partial Spearman correlation of decoded reported choice with dynamic choice, given\n      reported choice\n    value: 0.35\n    tolerance: 0.02\n  - quantity: partial Spearman correlation of decoded reported choice with reported choice, given\n      dynamic choice\n    value: 0.14\n    tolerance: 0.02\n  - quantity: difference\n    value: 0.21\n    tolerance: 0.02\n  depends_on:\n  - fig3q-cue-decoding\n  criterion: Reported-choice decoders as in fig3q-cue-decoding (same decoder readings), stem\n    traversal frames, held-out predictions; partial Spearman correlations per decoder;\n    bootstrap over decoders (hierarchical, mice then decoders). Tolerances are the reported\n    SEMs. Reproduced when the difference is above zero with p < 0.05 and the three values are\n    within tolerance under a reading; partially reproduced when only the sign and test hold.\n- id: figs5f-dynamic-choice-decoding\n  statement: From populations of about 100 neurons, dynamic choice is decoded better (Spearman\n    0.59 ± 0.02) than reported choice (0.26 ± 0.02), both above chance.\n  source: Figure S5F\n  quote: Decoding of both dynamic and reported choice was above chance (p < 10-3, bootstrap), but\n    decoding of reported choice was less accurate than dynamic choice\n  statistics:\n  - about: each decoder type against chance\n    test: bootstrap\n    p: 0.001\n    p_relation: \"<\"\n    n: 974 decoders\n  - about: dynamic minus reported choice decoding\n    test: bootstrap\n    p: 0.001\n    p_relation: \"<\"\n    n: 974 decoders\n  expected:\n  - quantity: dynamic choice decoding, Spearman correlation\n    value: 0.59\n    tolerance: 0.02\n  - quantity: reported choice decoding, Spearman correlation\n    value: 0.26\n    tolerance: 0.02\n  - quantity: difference\n    value: 0.33\n    tolerance: 0.13\n  depends_on:\n  - fig3q-cue-decoding\n  criterion: Decoders as in fig3q-cue-decoding; Spearman correlation of held-out predictions\n    with true values over stem frames. Tolerances are the reported SEMs. Reproduced when both\n    exceed zero and dynamic exceeds reported (p < 0.05) and the values are within tolerance under\n    a reading.\n- id: figs5i-dynamic-choice-over-roll\n  statement: In all areas except V1 and A, dynamic choice is encoded more than roll velocity\n    during stem traversal.\n  source: Figure S5I\n  quote: >-\n    For all areas except V1 and area A, the mean fraction explained deviance for dynamic choice\n    was greater than roll velocity, which controls left-right movements in the maze (AM: p =\n    0.006; PM, MM and RSC: p < 10-3)\n  statistics:\n  - about: AM\n    test: hierarchical bootstrap\n    p: 0.006\n  - about: PM, MM and RSC\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - well-fit-neurons\n  criterion: Encoding strength in the stem epoch of dynamic choice and of roll velocity (its\n    linear term; reading two adds its pairwise interactions with the other velocities), paired\n    per neuron, area means by hierarchical bootstrap. Reproduced when dynamic choice exceeds roll\n    velocity in PM, AM, MM and RSC at two-tailed p < 0.05. V1 and A are reported.\n- id: figs5m-movement-history-control\n  statement: With past and upcoming movement added to the GLM, dynamic choice encoding drops\n    but stays above zero in all areas and higher in RSC than in V1, PM and A.\n  source: Results, Encoding of dynamic choice was enriched in RSC, paragraph 3; Figure S5M\n  quote: Encoding of dynamic choice in models with movement history was significantly greater\n    than zero in all 6 areas (p < 10-3), and was higher in RSC compared to V1, PM and area A (p <\n    10-3)\n  statistics:\n  - about: with against without movement history, each area\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n  - about: each area against zero\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n  - about: RSC against V1, PM and A\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - well-fit-neurons\n  criterion: The alternative GLM of the Methods (Design matrix) with velocities and\n    accelerations on 5-df b-splines shifted every 1/3 s over 2 s past and future, no pairwise\n    movement interactions. Reproduced when dynamic choice encoding in the stem is lower than in\n    the main model in all areas, above zero in all areas, and higher in RSC than V1, PM and A,\n    each two-tailed p < 0.05 by hierarchical bootstrap.\n- id: fig4g-position-rsc\n  statement: Maze position is encoded in all areas, most strongly in RSC (above V1, PM and A,\n    not different from AM and MM).\n  source: Results, Encoding of dynamic choice was enriched in RSC, paragraph 4; Figure 4F, 4G\n  quote: Encoding of maze position was present in all areas, but strongest in RSC, with a similar\n    medial-to-lateral gradient as choice encoding\n  statistics:\n  - about: RSC against V1, PM or A\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n  - about: RSC against AM or MM\n    test: hierarchical bootstrap\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - well-fit-neurons\n  criterion: Encoding strength of trial phase (maze position) in the stem epoch, area means by\n    hierarchical bootstrap. Reproduced when every area is above zero and RSC exceeds V1, PM and\n    A at two-tailed p < 0.05 after Benjamini-Hochberg. RSC against AM and MM is reported.\n- id: fig4h-activity-by-epoch\n  statement: RSC is most active in the maze stem and least active in the feedback period/ITI,\n    when area A is more active.\n  source: Results, Encoding of dynamic choice was enriched in RSC, paragraph 4; Figure 4H\n  quote: RSC was also most active in the maze stem and least active during feedback and ITI\n    periods, when area A was more active\n  criterion: Deconvolved activity z-scored per neuron over the session, averaged per neuron in\n    each epoch (Figure 4H). Which neurons enter is not said; the readings are all 93,881 and\n    the well-fit 42,998. Reproduced when, under both, RSC's area mean in the stem exceeds every\n    other area's and in the feedback period/ITI is below A's, with hierarchical bootstrap\n    two-tailed p < 0.05 (the Methods' default test; the legend gives none).\n- id: fig5e-cue-movement-distributed\n  statement: Cue and movement have the highest mutual information between encoding strength\n    and area, yet their equivalent random fractions are above 0.75 and equivalent jitters near\n    0.6, closer to fully distributed than fully modular.\n  source: Results, Encoding of most variables is highly distributed, paragraph 2; Figure 5E,\n    5F; Figure S6A\n  quote: Cue and movement were the two variables with the highest mutual information between\n    encoding strength and posterior cortical area. However, their equivalent random fractions were\n    greater than 0.75 ... Similarly, their equivalent jitters were near 0.6\n  expected:\n  - quantity: equivalent jitter, cue and movement\n    value: 0.6\n    tolerance: 0.06\n  depends_on:\n  - well-fit-neurons\n  criterion: STAR Methods, Quantification of distributedness. Active neurons per epoch\n    (epoch-averaged null deviance above trial-averaged null deviance), 1,000 sampled per area,\n    encoding strength ranked, mutual information with area label (scikit-learn\n    mutual_info_classif) normalized by the fully modular model, repeated 1,000 times; the\n    equivalent random fraction and jitter are the nearest neighbours on the model curves (100\n    values from 0.01 to 1; 491 values from 0.1 to 5; 100 simulations each). Epochs are stem\n    for cue, whole trial for movement. Reproduced when cue and movement have the two highest\n    normalized MI of the variables tested, both random fractions exceed 0.75 and both jitters\n    are within 10% of 0.6. Whether the active-neuron pool is the well-fit neurons or all neurons\n    is not said; the counts (20,202 stem, 12,719 feedback) match the well-fit pool, which is\n    used, with all neurons as a variant.\n- id: fig5e-position-choice-strategy-distributed\n  statement: Maze position and choice are even more distributed (equivalent random fraction near\n    0.9), and decision-making strategy is the most distributed (near 1).\n  source: Results, Encoding of most variables is highly distributed, paragraph 2; Figure 5E\n  quote: The encoding of maze position and choice were even more distributed than cue and\n    movement, with equivalent random fractions near 0.9. All other variables were also highly\n    distributed, with decision-making strategy being the most distributed (random fraction near\n    one)\n  expected:\n  - quantity: equivalent random fraction, maze position and choice\n    value: 0.9\n    tolerance: 0.09\n  - quantity: equivalent random fraction, strategy\n    value: 1\n    tolerance: 0.1\n  - quantity: active neurons, stem\n    value: 20202\n    tolerance: 2020\n  - quantity: active neurons, feedback period/ITI\n    value: 12719\n    tolerance: 1272\n  depends_on:\n  - fig5e-cue-movement-distributed\n  criterion: As fig5e-cue-movement-distributed; maze position and dynamic choice in the stem,\n    reported choice and outcome in the feedback period/ITI, strategy over the whole trial (the\n    Methods name stem for position and dynamic choice, feedback for reported choice and\n    outcome; the strategy epoch is not named, so stem and whole trial are both run). Which\n    \"choice\" the sentence means is not fixed; dynamic choice (stem) and reported choice\n    (feedback) are both reported, and the claim holds when either is within tolerance and\n    above cue and movement. Reproduced when the values are within tolerance and strategy has the\n    highest random fraction.\n- id: fig6b-location-from-profiles\n  statement: Neurons in V1, A and RSC are typically decoded to their own areas from their\n    encoding profiles, while neurons in AM and MM are decoded across all of posterior cortex.\n  source: Results, Single-neuron encoding profiles confirm functional gradients, paragraph 1;\n    Figure 6A, 6B\n  quote: Neurons in V1, A, and RSC were typically predicted to reside in their actual areas of\n    origin, indicating that these neurons had distinctive encoding profiles, in contrast to neurons\n    from AM and MM that were predicted to reside in all sites across posterior cortex\n  depends_on:\n  - well-fit-neurons\n  criterion: STAR Methods, Decoding anatomical locations. Encoding profile is the mean fraction\n    explained deviance of the 11 variable groups over 6 epochs; 241 logistic decoders on a 0.15\n    mm grid, Gaussian targets (sigma 0.15 mm), Tensorflow, Adam (0.01), L2, leave-one-mouse-out;\n    outputs divided by sampling density and normalized per neuron. The L2 strength is not given;\n    the readings are the values of the GLM's lambda grid chosen by leave-one-mouse-out loss, and\n    the grid's middle value 1e-3. For each area, the average decoded distribution over its\n    neurons; the measure is the fraction of its mass inside the area's own territory divided\n    by the fraction of decoder sites inside it. Reproduced when, under every reading, V1, A and\n    RSC each have a higher ratio than both AM and MM.\n- id: fig6d-three-gradients\n  statement: Non-negative factorization of the decoded locations is dominated by three factors\n    (reconstruction error 33.8% ± 3.1% with three, 55% with one), forming spatial gradients\n    peaking in V1, RSC and A.\n  source: Results, Single-neuron encoding profiles confirm functional gradients, paragraph 2;\n    Figure 6D; Figure S6I; STAR Methods, Non-negative matrix factorization\n  quote: Strikingly, these factors formed three distinct spatial gradients that dominated the\n    anatomical organization of encoding with peaks in V1, RSC and A, respectively\n  expected:\n  - quantity: normalized reconstruction error, three factors\n    value: 0.338\n    tolerance: 0.031\n  - quantity: normalized reconstruction error, one factor\n    value: 0.55\n    tolerance: 0.055\n  depends_on:\n  - fig6b-location-from-profiles\n  criterion: scikit-learn NMF of the 42,998 by 241 prediction matrix for k = 1 to 10;\n    reconstruction error is the Frobenius norm of the residual over that of the data. The\n    tolerance for three factors is the reported bootstrap SEM. Reproduced when the errors are\n    within tolerance, the improvement flattens from four factors (the gain from 3 to 4 is\n    smaller than from 2 to 3), and the three factors' decoder scores peak inside V1, RSC and A,\n    one each. NMF initialization is a standard choice (scikit-learn default).\n- id: figs6g-factor-profiles\n  statement: Cue weighs most in factor 1, maze position and choice in factor 2, and movement in\n    factor 3.\n  source: Results, Single-neuron encoding profiles confirm functional gradients, paragraph 2;\n    Figure S6G\n  quote: cue was greatest in factor 1, maze position and choice were greatest in factor 2, and\n    movement was greatest in factor 3\n  depends_on:\n  - fig6d-three-gradients\n  criterion: Each factor's profile is the score-weighted mean of the location decoders'\n    coefficients (STAR Methods, Non-negative matrix factorization). Factors are numbered by\n    their peak (V1, RSC, A). Reproduced when, across the three factors, cue's weight is highest\n    in the V1 factor, position's and dynamic choice's in the RSC factor, and movement's in the\n    A factor, in the stem epoch.\n- id: encoding-dimensionality\n  statement: The number of principal components needed for 70% of variance is 8, 6 and 3 for\n    GLM coefficients, encoding strengths and decoded locations, and 35, 23 and 16 for 95%.\n  source: STAR Methods, Analysis of dimensionality of encoding across neurons versus encoding\n    across cortical space\n  quote: The number of principal components needed to explain 70% of the variance in the three\n    matrices was 8, 6, and 3, respectively, and further, 35, 23, and 16 principal components were\n    needed to explain 95% of the variance\n  expected:\n  - quantity: PCs for 70%, GLM coefficients\n    value: 8\n    tolerance: 0.8\n  - quantity: PCs for 70%, encoding strengths\n    value: 6\n    tolerance: 0.6\n  - quantity: PCs for 70%, decoded locations\n    value: 3\n    tolerance: 0.3\n  - quantity: PCs for 95%, GLM coefficients\n    value: 35\n    tolerance: 3.5\n  - quantity: PCs for 95%, encoding strengths\n    value: 23\n    tolerance: 2.3\n  - quantity: PCs for 95%, decoded locations\n    value: 16\n    tolerance: 1.6\n  depends_on:\n  - fig6b-location-from-profiles\n  criterion: PCA of the three matrices of the Methods over the well-fit neurons. Whether\n    columns are standardized first is not said; centred only and z-scored are both run. The\n    claim is reproduced when every count is within tolerance under a reading, and partially\n    when the ordering (coefficients > strengths > locations) holds at both levels.\n- id: fig7def-encoding-correlations\n  statement: Correlations in single-neuron encoding strength between cue, dynamic choice and\n    movement are similar across areas and close to zero; only A differs for cue against\n    movement.\n  source: Results, Conjunctive structure of encoding, paragraph 2; Figure 7D to 7F\n  quote: Strikingly, the correlations in encoding between pairs of cue, choice, and movement\n    variables were similar across areas, despite major differences in the encoding strengths of\n    these variables between areas ... In addition, the correlation coefficients were close to zero\n  statistics:\n  - about: cue and dynamic choice, all area pairs\n    test: bootstrap\n    p: 0.05\n    p_relation: \">\"\n  - about: cue and movement, A against each other area\n    test: bootstrap\n    p: 0.013\n    p_relation: \"<\"\n  - about: cue and movement, pairs among the other 5 areas\n    test: bootstrap\n    p: 0.05\n    p_relation: \">\"\n  - about: dynamic choice and movement, all area pairs\n    test: bootstrap\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - well-fit-neurons\n  criterion: STAR Methods, Correlation between encoding of pairs of variables. Fraction null\n    deviance (re-fitting) in the stem, local spatial mean subtracted (smoothed map, SD 150 um),\n    active neurons only, Pearson correlation per area, bootstrap (mice then neurons). A claim\n    of absence, judged on the paper's test as written, a two-tailed comparison of two unpaired\n    bootstrap samples per area pair at p > 0.05 (no correction is stated; Benjamini-Hochberg is\n    shown as a variant). Reproduced when no pair differs for cue and dynamic choice or for\n    dynamic choice and movement, and for cue and movement only pairs involving A differ; every\n    r is reported, and near zero is judged as |r| < 0.2, a bound this file sets, as the paper\n    gives none.\n- id: fig7g-area-decoding-strength-vs-correlation\n  statement: A neuron's area is decoded well from encoding strengths, poorly from encoding\n    correlations, and barely better from both than from strengths alone.\n  source: Results, Conjunctive structure of encoding, paragraph 3; Figure 7G, 7H\n  quote: Although decoding based on encoding correlations allowed above-chance performance, it\n    was poor relative to decoding from encoding strengths alone. Further, decoding with both\n    encoding correlations and encoding strengths was barely improved from decoding with encoding\n    strengths alone\n  statistics:\n  - about: strengths only against correlations only, all areas except AM\n    test: Wilcoxon signed-rank test\n    p: 0.05\n    p_relation: \"<\"\n  - about: strengths only against strengths plus correlations, all areas\n    test: Wilcoxon signed-rank test\n    p: 0.03\n    p_relation: \">\"\n    corrected: not significant after multiple comparison correction\n  depends_on:\n  - fig7def-encoding-correlations\n  criterion: STAR Methods, Decoding of area. Spatial-mean-subtracted, z-scored encoding\n    strengths of 11 variables for active neurons in the stem; interaction terms are their\n    pairwise products; one-against-others scikit-learn LogisticRegression, leave-one-mouse-out,\n    auROC on held-out mice; Wilcoxon signed-rank over the 8 held-out mice. No parameters are\n    given for LogisticRegression; its defaults (L2, C = 1) are the reading. Reproduced when\n    strengths beat correlations in at least five of six areas (p < 0.05) and strengths plus\n    correlations is not better than strengths after Benjamini-Hochberg in any area.\n- id: fig8cd-position-specific-decoders\n  statement: Cue and choice decoders trained at one maze position lose accuracy when tested at\n    other positions.\n  source: Results, Flexible, high-dimensional representations, paragraph 1; Figure 8C, 8D\n  quote: decoders trained to predict cue or choice at one maze position degraded in accuracy when\n    tested at other maze positions\n  depends_on:\n  - fig3q-cue-decoding\n  criterion: Decoders of fig3q-cue-decoding, one per position bin, tested at every other bin;\n    cue on sessions with cue offset at 0.76 of the maze, positions with cue present (698\n    decoders in the paper), dynamic choice on 974 decoders. Reproduced when performance\n    falls with train-test distance (mean at the largest distance below that at zero distance,\n    hierarchical bootstrap two-tailed p < 0.05) for both variables in every area.\n- id: fig8g-shattering-dimensionality\n  statement: Shattering dimensionality for conjunctions of cue, choice, position, movement and\n    rule belief is well above chance and similar across areas, and equal to that of\n    populations drawn from all areas.\n  source: Results, Flexible, high-dimensional representations, paragraph 2; Figure 8F, 8G;\n    Figure S8A to S8C\n  quote: Shattering dimensionality for all conjunctions in all areas was well above chance, and\n    interestingly, shattering dimensionality for each conjunction was similar across posterior\n    cortex ... Almost all differences between areas were not statistically significant and fell\n    within a range of < 10% classification accuracy for each conjunction\n  statistics:\n  - about: all pairs among all-area and the 6 areas, Figure 8G\n    test: hierarchical bootstrap\n    p: 0.01\n    p_relation: \">\"\n    corrected: not significant after multiple comparison correction\n  - about: cue, dynamic choice and position, RSC against A (Figure S8B)\n    test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n  criterion: STAR Methods, Quantification of shattering dimensionality. Pseudo-populations of\n    1,000 neurons per area by hierarchical bootstrap (1,000 samples), all layer 2/3 neurons,\n    stem frames, trial samples split 50-50 (test capped at 30), standardized on training data,\n    linear SVC on every marginally balanced dichotomy, 10 splits, with the bins and C values of\n    the Methods (C = 1.0 for cue and position, 0.1 otherwise). Conjunctions as listed in the\n    Methods (cue or choice by 10 position bins, cue by 3 rule-belief bins by 6 position bins,\n    cue by choice by 4 position bins, 6 quantile bins per velocity axis); the exact set in\n    Figure 8G is shown only in the figure. Whether \"choice\" is dynamic choice (binned in 2) or\n    reported choice is not fixed except for Figure S8A (dynamic); both are run. Reproduced when\n    every conjunction in every area is above 0.5, the spread of area means per conjunction is\n    under 0.10, and no area pair differs after Benjamini-Hochberg except RSC against A for cue\n    by dynamic choice by position (a claim of absence on the paper's test).\n- id: figs8d-l2-vs-group-lasso\n  statement: GLMs fit with L2 regularization perform slightly worse on test data than with\n    group lasso (difference -0.0175 ± 0.0052), and the main encoding results hold with L2.\n  source: STAR Methods, Quantification of fraction explained deviance (without re-fitting);\n    Figure S8D to S8J\n  quote: The performance of the models on test data was worse on average than those with group\n    lasso (difference in fraction of explained deviance\n  statistics:\n  - test: hierarchical bootstrap\n    p: 0.001\n    p_relation: \"<\"\n    n: 93,881 neurons\n  expected:\n  - quantity: L2 minus group lasso test fraction deviance explained\n    value: -0.0175\n    tolerance: 0.0052\n  depends_on:\n  - fig3i-glm-fit\n  criterion: The GLM refit with an L2 penalty in place of group lasso (the code's elastic_net\n    with l1_ratio 0), lambda chosen as in the main fit. The Methods print -0.0175 and the\n    legend 0.018 for the same difference; the Methods' signed value is used. Tolerance is the\n    reported SEM. Reproduced when the difference is within tolerance and below zero at p <\n    0.05, and the gradients of fig3m-movement-task-gradient and fig3o-cue-gradient keep their\n    ordering with L2.\n- id: figs8k-robust-to-threshold\n  statement: With a looser fit threshold (fraction deviance explained above 0.1, 68,532\n    neurons), the area differences in movement, task, cue, choice, position and strategy encoding\n    are the same.\n  source: Results, Calcium imaging of neural activity, paragraph 2; Figure S8K to S8O\n  quote: for subsequent analyses, we focused on well fit neurons although results were robust to\n    this criterion\n  depends_on:\n  - fig3m-movement-task-gradient\n  - fig3o-cue-gradient\n  - fig4b-dynamic-choice-stem\n  - fig4g-position-rsc\n  - figs4l-strategy-distributed\n  criterion: The tests of the claims it depends on, repeated on neurons above 0.1. Reproduced\n    when each of them gives the same outcome as on the 42,998 neurons; the legend of Figure\n    S8N reports RSC above V1, PM and A at p < 0.05 for position, and S8O strategy pairs at p >\n    0.04, not significant after correction.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000579/10.1016-j.neuron.2022.05.012.yaml paper/10.1016-j.neuron.2022.05.012.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

All quotes check out. Now the style checks: colon-space in plain scalars, em dashes, and the word "rather".

**Agent calls Bash**

```bash
cd  f=claims/000579/10.1016-j.neuron.2022.05.012.yaml; grep -n "—\|rather" $f; python3 - <<'E'
import yaml
f='claims/000579/10.1016-j.neuron.2022.05.012.yaml'
# find plain scalars with ': ' using the yaml event stream
for ev in yaml.parse(open(f)):
    if isinstance(ev, yaml.ScalarEvent) and ev.style is None and ': ' in ev.value:
        print(ev.start_mark.line+1, ev.value[:80])
E
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('claims/000579/10.1016-j.neuron.2022.05.012.yaml'))['claims']
print(len(d), sum('quote' in c for c in d), sum('statistics' in c for c in d), sum(len(c.get('statistics',[])) for c in d), sum('criterion' in c for c in d), sum('expected' in c for c in d))"; git status --short
```

```
41 41 19 45 41 14
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
?? claims/000579/
?? scripts
```

**Agent**

I wrote `claims/000579/10.1016-j.neuron.2022.05.012.yaml`. `tools/claims_check.py` reports 41 claims, 41 quotes, 45 statistical values and 0 problems. The file has no em dashes, no "rather", and no plain scalars containing ": ". Nothing was committed.

**Text read**
- **Version:** the PMC accepted author manuscript (PMC9357051), not the version of record. It includes the Results, figure legends and STAR Methods.
- **Supplement:** the one supplement file, with the legends of Figures S1 to S8.
- **No main-text PDF:** Figures 1 to 8 were read from their legends and the Results only.
- **Code:** `github.com/sytseng/GLM_Tensorflow` at commit 75a1314, the repository behind the paper's Zenodo link. It holds only the GLM fitting functions. Its `make_prior_matrix`, which groups the predictors for the penalty, is called but not included. The paper says its other analysis code is shared on request.

**Claims**
- 41 claims, all with quotes and none `inferred`.
- 19 claims carry statistics (45 entries), 14 carry expected values, and all 41 have criteria.
- All are `data: dataset`. The paper uses no outside data apart from the Allen CCF and field-sign maps it registers neurons to.
- They cover the behaviour and models (Fig 1, S1), photoinhibition (Fig 1L–M, S1M), dynamic choice (Fig 2, S2L), neuron counts and GLM fit (Fig 3I, S3), the encoding gradients (Fig 3M/O/Q, 4B/C/G/H, S4, S5), distributedness (Fig 5), location decoding and NMF (Fig 6), encoding correlations (Fig 7) and shattering dimensionality (Fig 8). Robustness checks are included: L2 regularization in place of group lasso, and a looser fit threshold.

**Details left open, with the readings named**
- **How the GLM's penalty strength (lambda) is chosen:**
  - (a) the minimum mean cross-validated deviance, as the Methods word it (main reading);
  - (b) the code's rule, the largest lambda within a number of standard errors of the minimum. The code does not give that number, so 1 is used (run as a variant).
  - The code's default lambda grid differs from the Methods; the Methods are followed.
- **Drift exclusion:** whether it is applied before or after the 93,881-neuron count is not said; both orders are shown.
- **Stem epoch edge:** bins wholly in the stem, or bins whose centre is in the stem.
- **LSTM accuracy SD:** taken over sessions or over mice, and on all sessions or only those above 0.65 correct.
- **Windows and bins:**
  - switch windows of 10 or 20 trials;
  - position grids of 11 or 20 bins;
  - strategy bins as 5 or 10 quantiles, or a Spearman correlation.
- **Population decoders:** the elastic-net strength (the minimum-deviance or the one-SE choice that MATLAB's `lassoglm` returns), and how groups of about 100 neurons are formed (k-means on positions, or equal-count tiles).
- **Location decoders:** the L2 strength (chosen by leave-one-mouse-out loss, or fixed at 1e-3).
- **Other choices:**
  - PCA standardization (centred only, or z-scored);
  - which neurons enter the epoch activity maps and the active-neuron pool;
  - whether "choice" means dynamic or reported choice in Fig 5 and Fig 8;
  - the epoch used for strategy in Fig 5;
  - scikit-learn default settings for `LogisticRegression`.
- **Choices the file sets itself**, because the paper gives none:
  - |r| < 0.2 as "near zero" for the encoding correlations;
  - 0.1 from 0.5 as "near chance" after a switch;
  - a standard lapse form for the reinforcement-learning model, whose formula is garbled in the text.

**Missing from the paper**
- **Exact conjunctions of Fig 8G:** they appear only in the figure; the Methods' list is used.
- **Photoinhibition sessions:** the 7 VGAT mice and 164 sessions may not be in the dandiset, whose title names imaging only. That is for the author to check.
- **Value conflict:** the L2 against group-lasso fit difference is printed as −0.0175 in the Methods and 0.018 in the S8D legend. The Methods' value is used.
- **Tests the paper does not report:** six claims (Fig 2C, 2F, 4H, S4P, the cue-biased running claim, and Fig 8C/D) report no test. They use the Methods' default, a two-tailed hierarchical bootstrap, which the criteria say.

## End of run

30 turns, 7 minutes, result: success.
