# mallory-2021 · claims · run 42838174567

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/## Reader/,/^## [^R]/p'; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls -la paper/; cat claims/fouke-2025.yaml | head -150; cat papers/datasets/mallory-2021.yaml 2>/dev/null; ls claims | grep -i mallory
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 150,400p claims/fouke-2025.yaml | grep -n -E "^[a-z]|^- id|  [a-z_]+:" | head -60; wc -l paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat tools/claims_check.py | head -120
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

[... 93 more lines not kept]
```

**Agent**

Let me make a readable copy with the LaTeX blocks collapsed.

**Agent calls Bash**

```bash
python3 - <<'EOF'
import re,os
t=open('paper/10.1038-s41467-021-20936-8.txt').read()
t=re.sub(r'\\documentclass.*?\\end\{document\}','',t,flags=re.S)
t=re.sub(r'[ \t]+',' ',t)
# split long lines into sentences-ish
out=os.environ['TMPDIR']+'/m.txt'
open(out,'w').write(t)
print(len(t))
EOF
fold -s -w 200 $TMPDIR/m.txt > $TMPDIR/mf.txt; wc -l $TMPDIR/mf.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/mf.txt",
 "limit": 400
}
```

```
File content (29918 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/mf.txt",
 "limit": 250
}
```

```
1	DOI: 10.1038/s41467-021-20936-8
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 3 supplement file(s) from the PMC Open Access cloud data (PMC7844029), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	Nat Commun Nat Commun 2873 ncomms 101528555 Nature Communications 2041-1723 Nature Publishing Group PMC7844029 PMC7844029.1 7844029 7844029 33510164 10.1038/s41467-021-20936-8 20936 1 Article Mouse 
8	entorhinal cortex encodes a diverse repertoire of self-motion signals Mallory Caitlin S. http://orcid.org/0000-0002-2337-9290 Hardcastle Kiah Campbell Malcolm G. Attinger Alexander Low Isabel I. C. 
9	http://orcid.org/0000-0002-8145-747X Raymond Jennifer L. http://orcid.org/0000-0003-0416-2528 Giocomo Lisa M. [removed: an e-mail address] grid.168010.e 0000000419368956 Department of Neurobiology, Stanford 
10	University School of Medicine, Stanford, CA USA 28 1 2021 2021 12 372028 671 9 11 2020 31 12 2020 28 01 2021 08 02 2021 17 02 2026 © The Author(s) 2021 https://creativecommons.org/licenses/by/4.0/ 
11	Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as 
12	long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party 
13	material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative 
14	Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of 
1
[... 235 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/mf.txt",
 "offset": 250,
 "limit": 250
}
```

```
250	pinpoint the specific role of entorhinal eye signals in navigation-based computations. Our findings reveal new potential homologies in the navigational coding schemes used between species. First, the 
251	observed coding of 3D head movement in mice is consistent with that in the presubiculum of bats 14 . However, in rodent MEC, we observed a greater degree of conjunctive coding, including cells that 
252	simultaneously encode position and velocity of the head about multiple axes alongside body position and body speed. Second, the coding of eye position in rodents bears similarities to the coding of 
253	eye (or gaze) position observed in the MEC of head-fixed non-human primates. Yet primate gaze signals have been interpreted as playing a role in exploration of visual space analogous to the role of 
254	body position signals in rodent exploration of physical space 18 . Hence, the observation that rodent MEC simultaneously represents both body position and eye position raises the possibility that 
255	primate and rodent eye-movement signals serve distinct functions. The joint coding of body position with eye or head position (Figs. 3 d, 6d ) is reminiscent of a coding scheme observed in primate 
256	posterior parietal cortex, wherein eye or head position modulates the amplitude of a cell’s response within its visual receptive field (i.e. “gain fields”) 43 , 44 . Since their discovery in primate 
257	parietal cortex, eye position gain fields have been reported widely throughout the brain, particularly in regions processing visuomotor information, including frontal cortex 44 , 45 , visual cortex 
258	46 , 47 , and premotor cortex 48 . Gain modulation has been theorized to support transformations between relevant reference frames 49 , 50 . For example, posterior parietal eye position gain fields 
259	may support the transformation of visual representations from retinotopic-centered coordinates to body-centered coordinates downstream 49 , 50 . Whereas spatial represen
[... 240 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/mf.txt",
 "offset": 500,
 "limit": 120
}
```

```
500	with significance being achieved by P = 0.05/10. Reporting summary Further information on research design is available in the Nature Research Reporting Summary linked to this article. Supplementary 
501	information Supplementary Information Peer Review File Reporting Summary Peer review information Nature Communications thanks the anonymous reviewers for their contribution to the peer review of this 
502	work. Publisher’s note Springer Nature remains neutral with regard to jurisdictional claims in published maps and institutional affiliations. These authors contributed equally: Caitlin S. Mallory, 
503	Kiah Hardcastle. These authors jointly supervised this work: Jennifer L. Raymond, Lisa M. Giocomo. Supplementary information Supplementary information is available for this paper at 
504	10.1038/s41467-021-20936-8. Acknowledgements This work was supported by an NSF Graduate Research Fellowship awarded to C.M., a Stanford Interdisciplinary Graduate Fellowship to K.H., an NSF Graduate 
505	Research Fellowship and Baxter Fellowship awarded to M.G.C., the SNSF (P2BSP3_181743) awarded to A.A., a Stanford Interdisciplinary Graduate Fellowship to I.L., NIH R21 EY026152, R01 DC04154, R01 
506	NS072406 and Simons Collaboration on the Global Brain 543031 awarded to J.L.R., and NIMH R56MH106475, James S McDonnell Foundation, Office of Naval Research Young Investigator Program N000141812690, 
507	the Vallee Foundation and Simons Collaboration on the Global Brain 542987SPI awarded to L.M.G. We thank R Munn for assistance in behavioral data collection, A Diaz for histology assistance and H 
508	Payne and A Shakhawat for assistance with the eye movement measurement technique and analyses. Author contributions C.M., K.H., L.M.G., and J.L.R. conceptualized the experiments and analyses. C.M. 
509	and K.H. collected and analyzed the data from freely moving mice. M.G.C. and A.A. collected and processed the data from head-fixed mice and C.M. and K.H. analyzed the data from head-fixed 
[... 110 more lines not kept]
```

**Agent**

Now the supplement part.

**Agent calls Bash**

```bash
grep -n -E "^=+|SUPPLEMENT|supp[123]|Supplementary Fig(ure)?\.? ?[0-9]+ ?\|?" $TMPDIR/mf.txt | awk -F: '$1>619' | head -60
```

```
741:=== page 1 ===
744:Supplementary Fig 1
856:=== page 2 ===
857:Supplementary Figure 1. Histology for representative animals from each cohort in the study 
881:=== page 3 ===
967:= A(t)
1072:Supplementary Fig 2
1095:=== page 4 ===
1096:Supplementary Figure 2: Description of LN model fitting procedure. ai, Schematic of 
1122:=== page 5 ===
1227:Supplementary Fig 3
1229:=== page 6 ===
1230:Supplementary Figure 3. Identifying the rate of false positives in the LN-model. In order to 
1251:=== page 7 ===
1707:Supplementary Fig 4
1720:=== page 8 ===
1721:Supplementary Figure 4. Comparison between LN-model and shuffle identification of cells 
1741:=== page 9 ===
2313:Supplementary Fig 5
2328:=== page 10 ===
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; for r in 735,744 857,880 1096,1121 1230,1250 1721,1740 2329,2340 4168,4188 4730,4756 5181,5192 5383,5407 5764,5775 6196,6221 6696,6814; do sed -n "${r}p" mf.txt; echo ----; done
```

```
e85269 (2014). 10.1371/journal.pone.0085269

[62] Pasquet, M. O. et al. Wireless inertial measurement of head kinematics in freely-moving rats. Sci. Rep. 6, 35689 (2016). 10.1038/srep35689

##### Supplement: 41467_2021_20936_MOESM1_ESM.pdf

=== page 1 ===
1 mm
a
Supplementary Fig 1
----
Supplementary Figure 1. Histology for representative animals from each cohort in the study 
and example waveforms. a-b, Nissl stained brain sections showing the final tetrode 
placements in four mice from the freely-moving datasets without (a) and with (b) 
accelerometers sensors. Black arrows mark the final tetrode placement. Tetrodes placements 
were similarly confirmed in the remaining 22 tetrode-implanted mice. c, Dapi stained brain 
sections showing the placement of the Neuropixels probe (red, yellow or blue, DiD, DiI, DiO,), 
in four mice used for head-fixed eye tracking experiments. Neuropixels probe placements 
were similarly confirmed in the remaining 4 Neuropixels probes-implanted mice. d, Left: 
Example raw tuning curves for cells encoding pitch, roll, or azimuthal head velocity. Right: The 
[... 349 more lines not kept]
```

**Agent calls Bash**

```bash
git show --stat HEAD | head -20; grep -rl "000053" --include=*.yaml --include=*.md --include=*.json . 2>/dev/null | grep -v "^./paper" | head
```

```
commit 73497b03e46d4b99a5c2b397084d733cee305e06
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Tue Nov 10 09:50:12 2026 -0500

    Paper match for DANDI:000053: matched
    
    From attempt/000053 (docs/pipeline.md, step 1).

 papers/datasets/mallory-2021.yaml |  8 ++++++++
 papers/match/000053.yaml          | 17 +++++++++++++++++
 2 files changed, 25 insertions(+)
./transcripts/li-2016/000011/author.md
./transcripts/xu-2022/author.md
./transcripts/ibl-2021/recorder.md
./transcripts/berg-2020/claims.md
./transcripts/li-2022/author-revise-1.md
./transcripts/tian-2025/author-revise-1.md
./transcripts/rodgers-2014/author.md
./claims/berg-2020.yaml
./targets/dandisets.json
```

**Agent calls Bash**

```bash
cat papers/match/000053.yaml; python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for x in (it if isinstance(it,list) else it.values()):
    if '000053' in json.dumps(x)[:200]: print(json.dumps(x,indent=1)[:3000])
"
```

```
# Whether each paper DANDI:000053 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: dandi
  id: '000053'
date: '2026-11-10'
papers:
- doi: 10.1038/s41467-021-20936-8
  relation: IsDescribedBy
  checks:
    text: true
    title_in_text: true
    names_this: false
    names_others: []
  verdict: primary
  by: checks
  reason: The archive says the paper describes the dataset, and the paper names no dataset.
```

**Agent calls Bash**

```bash
grep -n "000053" targets/dandisets.json | head; python3 -c "
import json;d=json.load(open('targets/dandisets.json'));print(type(d), list(d)[:5] if isinstance(d,dict) else d[0].keys())"
```

```
692:   "dandiset": "000053",
<class 'dict'> ['schema_version', 'generated', 'source', 'counts', 'targets']
```

**Agent calls Bash**

```bash
sed -n 685,730p targets/dandisets.json
```

```
"resource_type": null,
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "000053",
   "name": "Recordings from medial entorhinal cortex during linear track and open exploration",
   "published_version": "0.210819.0345",
   "asset_count": 359,
   "size_gb": 1393.13,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "House mouse"
   ],
   "approaches": [
    "behavioral approach",
[... 26 more lines not kept]
```

**Agent**

Paper text, Methods and supplement are all present. Now fetching the dataset description and the linked code.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000053/versions/0.210819.0345/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('name'));print(d.get('description'))"; cd $TMPDIR && git clone -q https://github.com/GiocomoLab/ln-model-of-mec-neurons && git clone -q https://github.com/khardcastle/spline-lnp-model; for r in ln-model-of-mec-neurons spline-lnp-model; do (cd $r; echo $r; git log -1 --format='%H %ad'; find . -type f -not -path './.git/*' | head -40); done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/spline-lnp-model; cat README.md forward_search_kfold.m fit_model_kfold.m compute_test_train_ind.m glm_model.m spline_1d.m compute_llh_increase.m compute_llh.m create_glm.m
```

```
# spline-lnp-model
function [allModelFits, allModelTrainFits, bestModels, bestModelFits, parameters, pvals, final_pval] = forward_search_kfold(A,spiketrain,train_ind,test_ind)

% do the forward search

num_var = length(A); % number of variables to search over

% do the forward-search method to identify variables encoded:

% var_vec = list of variables to add in
% variables = the variables currently in the model
% num_var = total number of variables to search over
% allModelFits = the model fit for every variable, on every iteration
% through the forward search procedure
% bestModelFits = the model fit for the best model (for every iteration)
% parameters = parameters of the best model for each iteration
% pvals = the pvalue of the model comparison for each model

numFolds = length(test_ind);

[... 449 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ln-model-of-mec-neurons; cat README.md select_best_model.m fit_model.m; sed -n 1,80p fit_all_ln_models.m; grep -n "numFolds\|numPts\|sections\|beta\|alpha" *.m | head -30
```

```
# ln-model-of-mec-neurons
Code implements the LN model used to describe spike trains of MEC neurons based on the animal's position, head direction, speed, and theta phase information. Used in [Hardcastle et al., 2017.](http://www.cell.com/neuron/fulltext/S0896-6273(17)30237-4)

Run_me.m is the main script. This will load the data from a single cell, fit the 15 LN models (as described in Hardcastle et al., 2017), select the best model according to a forward search procedure, and then plot the results. Details for each step can be found in run_me.m, and the scripts listed within run_me.m. 

Updated versions of this code using splines can be found at https://github.com/GiocomoLab/spline-lnp-model. This version will implement an automated variable-fitting procedure, and will generally run faster with higher model fits. However, this version might be less user-friendly than the code in this repo.

Note - small updates and bug fixes have been made to the code. Questions can be directed to [removed: an e-mail address]
%% Description
% This code will implement forward feature selection in order to determine
% the simplest model that best describes neural spiking. First, the
% highest-performing single-variable model is identified. Then, the
% highest-perfmoring double-variable model that includes the
% single-variable model is identified. This continues until the full model
% is identified. Next, statistical tests are applied to see if including
% extra variables significantly improves model performance. The first time
% that including variable does NOT signficantly improve performance, the
% procedure is stopped and the model at that point is recorded as the
% selected model.

[... 302 more lines not kept]
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
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)); print(json.dumps(s['claims'] if 'claims' in s else '',indent=0)[:0])"; python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print([k for k in s['properties']])"; tail -30 claims/fouke-2025.yaml
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
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
head -60 claims/starkweather-2018.yaml
```

```
# Claims for Starkweather, Gershman & Uchida (2018), Neuron 98, 616-629, tested on CRCNS vta-1.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read: the version of record (paper/10.1016-j.neuron.2018.03.036.txt, supplied by a
# person), with its STAR Methods and the Supplemental Information (legends of Figures S1 to
# S8). The PDF could not be rendered here, so numbers printed only inside figures were read
# from the extracted text; the claims that rest on them say so.
#
# Code read: https://github.com/cstarkweather/Starkweather2018 at commit d667730 (the
# "GitHub link" of Code Availability points to the account; this is its repository for the
# paper). It holds only the belief state TD model (training, simulation, plotting, MATLAB).
# No analysis code for the recordings is linked, so every method for the recorded data comes
# from the Methods and legends. The code differs from the Methods in two settings of the
# simulation script (allSimulations_Saline_SalB.m) as committed, 10 simulations where the
# legends say 50, and every simulation intact (belief_impaired_dist all zeros) where the text
# says 60% impaired; the Methods are followed and the code's settings are variants.
#
# Data the paper used. 12 male DAT-Cre mice. Dopamine recordings in the left VTA of 8
# KORD-expressing mice, 4 trained on task 1 (odors A to C rewarded in 100% of trials) and 4 on
[... 40 more lines not kept]
```

**Agent**

The paper, Methods and supplement are complete, and both linked repositories are read. Writing the claims file now.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -o "Few cells encoded angular velocity along the.\{0,400\}" paper/*.txt | head -c 1500; echo; grep -c documentclass paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/mallory-2021.yaml",
 "content": "# Claims for Mallory, Hardcastle, Campbell, Attinger, Low, Raymond & Giocomo (2021), Nat Commun\n# 12, 671, tested on DANDI:000053.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-10, protocol as stated in docs/protocol.md.\n#\n# Text read. The version of record (paper/10.1038-s41467-021-20936-8.txt, Europe PMC full text\n# of PMC7844029), with its Methods, figure legends and the three supplementary files from the\n# PMC Open Access set, the Supplementary Information (legends of Supplementary Figures 1 to 12),\n# the peer review file (an editorial note only) and the reporting summary. The PDFs of the\n# supplement were not opened; no claim needed a number printed only inside a figure.\n#\n# Code read. The Code availability statement links two MATLAB repositories.\n# https://github.com/khardcastle/spline-lnp-model at commit 34b470f (2018-05-10) holds the\n# spline LN Poisson model (cardinal spline regressors, spline_1d.m, spline_1d_circ.m,\n# spline_2d.m; Poisson likelihood with an L2 penalty of weight 1, glm_model.m; 10-fold\n# cross-validation, fit_model_kfold.m and compute_test_train_ind.m; forward search with a\n# one-sided signed-rank test at 0.05 and a final signed-rank test of the selected model against\n# 0, forward_search_kfold.m; log-likelihood increase over a mean rate model in bits per spike,\n# compute_llh.m; the reduced-model contribution, compute_llh_increase.m) and an example script\n# for position, head direction and speed (create_glm.m). https://github.com/GiocomoLab/\n# ln-model-of-mec-neurons at commit 643386b (2022-06-20) is the older one-hot model of Hardcastle\n# et al. 2017 (fixed 15 models, roughness penalty), which this paper's Methods do not use; it was\n# read and is not followed. Neither repository holds the pitch, roll or eye variables, the\n# tuning curve classification, the stability measure or the PCA clustering; for those every\n# method comes from the Methods and legends. Where the code and the Methods differ, the Methods\n# are followed. create_glm.m uses 3-s chunks for the folds (the Methods say 10-s sections),\n# position bins of box size x 10/100 (the Methods say 15/100) and 12 head direction control\n# points (the Methods say 10 bins); these code settings are variants only.\n#\n# Data the paper used. Freely moving dataset, tetrodes in MEC layers II/III, 20 ms bins (50 Hz\n# tracking), mice foraging for 20 to 60 min in square or rectangular arenas (100 x 100, 50 x 50,\n# 70 x 70 or 70 x 35 cm), sessions kept when 70% or more of the arena was covered. Cohort 1,\n# 6 C57BL/6 mice (4 female, 2 male), right MEC, 179 cells, two headstage LEDs (body position B,\n# body speed Bs, azimuthal head direction Ha, azimuthal head velocity) and an IMU accelerometer\n# (pitch Hp, roll Hr, pitch and roll velocity), calibrated each session by brief head fixation\n# at pitch and roll 0. Cohort 2, 20 mice, 1021 cells, right (7) or left (13) MEC, LEDs only\n# (B, Bs, Ha, azimuthal head velocity); it includes 228 unpublished cells and cells from three\n# earlier papers (Campbell et al. 2018, 122 cells; Eggink et al. 2014, 389 cells; Munn et al.\n# 2020, 282 cells). Head-fixed dataset, 8 female C57BL/6 mice in virtual reality on a 400 cm\n# linear track with a checkered floor and five landmark towers, water reward at one tower;\n# Neuropixels 1.0 recordings in left (4 recordings, 3 mice) or right (7 recordings, 7 mice)\n# MEC, 11 recordings, 2861 units (Kilosort2 and Phy); VR position and running speed resampled\n# to 50 Hz; right eye video, pupil centre minus corneal reflection, high-pass filtered,\n# extreme 1% removed, projected on the eye's horizontal (nasal-temporal) and vertical axes and\n# divided by eye width, giving horizontal and vertical eye position (Eh, Ev) and velocity (Eh\n# dot, Ev dot), smoothed with Gaussians (about 10 ms for position, 140 ms for velocity). A second\n# head-fixed dataset, 6 sessions in 6 mice, 1621 cells, alternates blocks of the landmark track\n# and a track of the same length without landmarks (Figure 8); the paper does not say whether\n# these sessions are among the 11. The raw data are said to be at\n# https://figshare.com/authors/Lisa_Giocomo/9864194 (Data availability). The DANDI:000053\n# description lists tetrode recordings in MEC during open field navigation with inertial head\n# measurements, and Neuropixels recordings during a virtual linear track with eye measurements.\n# Whether it holds Cohort 2 (no IMU), the no-landmark sessions, spike-sorted units, the\n# calibrated pitch and roll, and the processed eye traces is the author's to find.\n#\n# Method details fixed here from the Methods (LN model framework) and the spline code, the\n# \"LN pipeline\" the criteria refer to. Time bins 20 ms. Epochs kept only where behaviour lies\n# in the inner 95% (2.5th to 97.5th percentile, freely moving) or inner 98% (1st to 99th,\n# head-fixed) of the session's distribution. Variables as cardinal spline regressors\n# (spline_1d.m), head direction circular (spline_1d_circ.m), position 2D in the open field\n# (spline_2d.m); control points, open field position (arena side in cm) x 15/100 per axis, 10\n# head direction bins, speed bins 5 cm/s wide, 8 bins for pitch, roll and the three head\n# velocities; VR 20 position bins, speed bins 5 cm/s, 5 bins for each eye variable. Tension\n# s = 0.5 (the code's value; the Methods give 0.5 to 0.7 and call results insensitive; 0.7 is a\n# variant). Poisson log-likelihood with L2 penalty beta = 1, fitted with fminunc. Performance\n# is the log-likelihood increase over a mean rate model on held-out data, 10-fold\n# cross-validation. Forward search, as in forward_search_kfold.m, adds the best variable while\n# a one-sided Wilcoxon signed-rank test over the 10 folds gives P < 0.05, and a cell encodes the\n# variables of the selected model when that model's fold values exceed 0 by a one-sided\n# signed-rank test (P < 0.05). Variables searched, Cohort 1 B, Bs, Ha, Hp, Hr and the azimuthal,\n# pitch and roll head velocities; Cohort 2 B, Bs, Ha and azimuthal head velocity; head-fixed B,\n# Bs, Eh, Ev, Eh dot, Ev dot. Model-derived tuning curves by Methods equation 10 (M = 200 bins),\n# shown and compared over the ranges of \"Visualizing tuning curves\" (the larger of the 2.5th\n# percentile and -50 deg for pitch and roll, -100 deg/s for azimuthal head velocity, and the\n# matching upper bounds; eye variables the larger of the 1st percentile and -3 units for Eh and\n# Eh dot, -2 for Ev and Ev dot, and the matching upper bounds). Stability is the Pearson\n# correlation of model-derived tuning curves from LN models refitted on the first and second\n# halves of the session with the full session's selected variables, on the overlapping range,\n# the shorter curve up-sampled. Tuning curve class is the lowest polynomial order (1 to 5)\n# whose fraction of error explained over a flat line exceeds 0.9, on range-normalized curves,\n# pitch and roll curves first smoothed (smoothdata, width 20); classified only when the animal\n# explored 50% (head) or 80% (eye) of the range. Binomial tests are against one half,\n# two-sided. Kruskal-Wallis tests are followed by two-sided Wilcoxon rank-sum tests at the\n# Bonferroni level given in each legend.\n#\n# Open, and named in the claims it bears on. (1) Fold construction. The Methods say each fold\n# is 10% of the data \"chosen from 10-s sections\" with no overlap; readings, (a) consecutive 10-s\n# sections assigned to folds 1 to 10 in turn (compute_test_train_ind.m with 10-s sections),\n# (b) 10-s sections assigned to folds at random; create_glm.m's 3-s sections are a variant.\n# (2) Range restriction. Readings, (a) only time bins where every variable lies within its\n# inner range are kept, (b) each variable is clipped to its own inner range and all bins kept.\n# (3) Contribution to model performance. The Methods say the difference between the selected\n# and the reduced model's performance, \"normalized by the model performance for the selected\n# model and subtracted from 1\"; readings, (a) (full - reduced) / full, the reading under which\n# body position is the largest contributor as the paper reports, (b) 1 - (full - reduced) /\n# full, the literal wording; performance is the mean over the 10 folds, or (c) one held-out\n# section as in compute_llh_increase.m. (4) \"Explored\" for shape classification; readings, (a)\n# the fraction of the preset range covered between the behavioural percentile limits, (b) the\n# fraction of tuning curve bins with any occupancy. (5) Preference of a cell (upward or\n# downward, nasal or temporal, ipsiversive or contraversive); readings, (a) the sign of the\n# slope for linear cells and the side of the tuning curve maximum for the others, (b) the side\n# with the larger absolute slope of lines fitted on either side of 0 (Methods, Quantifying head\n# and eye velocity tuning curves). (6) Asymmetric against symmetric velocity cells. The paper\n# compares slopes below and above 0 and gives no rule; readings, (a) symmetric when the two\n# slopes have opposite signs (V or inverted V), asymmetric otherwise, (b) the rule of the\n# Methods' shuffle comparison, symmetric when the correlation below 0 and the one above 0 fall\n# beyond the 5th and 95th percentiles of a 500-shift shuffle in opposite directions. (7) Fig. 8\n# tuning curves across tracks; readings, (a) model-derived curves from LN models fitted on each\n# track with the variables selected on the landmark track, (b) raw tuning curves (20 bins,\n# occupancy-normalized). (8) Which values a pairwise P stands for when one P is printed for\n# several pairs (\"H a versus remaining variables, P = 3.5e-4\"); read as the largest P of those\n# pairs. Eye units for the preset bounds are fixed as % of eye width, since the Results define\n# 1 unit as 1/100 of the eye width and Fig. 4f-i use % of eye width; a fraction of eye width\n# would put the bounds beyond the eye.\nschema_version: 2\npaper: doi:10.1038/s41467-021-20936-8\nclaims:\n- id: fig1b-head-posture-distributions\n  statement: Across Cohort 1 mice the median head pitch is 11.5 deg (inner 95% from -23.0 to\n    55.6 deg) and the median roll -0.8 deg (-50.9 to 43.6 deg); azimuthal head velocity has a\n    median near 0 deg/s and an inner 95% from -389.9 to 385.1 deg/s across 25 mice of both\n    cohorts.\n  source: Figure 1b legend\n  quote: pitch ... 2.5th percentile = −23.0 ± 4.5° ... median = 11.5 ± 4.1° ... 97.5th percentile =\n    55.6 ± 4.1° ( n = 6 mice); roll ... 2.5th percentile = −50.9 ± 3.6° ... median = −0.8 ± 7.6°\n  expected:\n  - quantity: pitch median, mean over mice\n    value: 11.5\n    tolerance: 4.1\n    unit: deg\n  - quantity: pitch 2.5th percentile, mean over mice\n    value: -23.0\n    tolerance: 4.5\n    unit: deg\n  - quantity: pitch 97.5th percentile, mean over mice\n    value: 55.6\n    tolerance: 4.1\n    unit: deg\n  - quantity: roll median, mean over mice\n    value: -0.8\n    tolerance: 7.6\n    unit: deg\n  - quantity: roll 2.5th percentile, mean over mice\n    value: -50.9\n    tolerance: 3.6\n    unit: deg\n  - quantity: roll 97.5th percentile, mean over mice\n    value: 43.6\n    tolerance: 4.0\n    unit: deg\n  - quantity: azimuthal head velocity 2.5th percentile, mean over mice\n    value: -389.9\n    tolerance: 34.7\n    unit: deg/s\n  - quantity: azimuthal head velocity 97.5th percentile, mean over mice\n    value: 385.1\n    tolerance: 34.7\n    unit: deg/s\n  criterion: As the legend says, percentiles are taken per session, averaged over a mouse's\n    sessions, then the mean over mice is compared, with the legend's sem across mice as the\n    tolerance. Reproduced when at least seven of the eight values are within tolerance,\n    partially reproduced for four to six.\n- id: fig1c-head-direction-cells\n  statement: In Cohort 1, 63 of 179 MEC cells (35%) encode azimuthal head direction.\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 1;\n    Figure 1c\n  quote: a large fraction of the 179 MEC neurons recorded encoded azimuthal head direction ( n =\n    63 cells, 35%)\n  expected:\n  - quantity: Cohort 1 cells encoding Ha\n    value: 63\n    tolerance: 6.3\n  - quantity: fraction of Cohort 1 cells encoding Ha\n    value: 0.35\n    tolerance: 0.035\n  criterion: Cells are counted as encoding a variable when it is in the model selected by the\n    LN pipeline (opening comment) over the eight Cohort 1 variables. Open details (1) and (2)\n    are run under both readings; reproduced when a reading puts the count within tolerance.\n- id: fig1c-pitch-roll-cells\n  statement: In Cohort 1, 46 MEC cells (26%) encode head pitch and 53 (30%) encode head roll.\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 1;\n    Figure 1c\n  quote: In addition, 46 neurons [26%] encoded head pitch position and 53 [30%] encoded head roll\n    position.\n  depends_on:\n  - fig1c-head-direction-cells\n  expected:\n  - quantity: Cohort 1 cells encoding pitch\n    value: 46\n    tolerance: 4.6\n  - quantity: Cohort 1 cells encoding roll\n    value: 53\n    tolerance: 5.3\n  criterion: Same LN pipeline and readings as fig1c-head-direction-cells. Reproduced when both\n    counts are within tolerance under one reading; partially reproduced when one is.\n- id: fig1c-pitch-roll-velocity-rare\n  statement: Few Cohort 1 cells encode angular velocity about the pitch (4 of 179) or roll (5 of\n    179) axes.\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 1\n  quote: Few cells encoded angular velocity along the pitch or roll axes ... and were not examined\n    further\n  depends_on:\n  - fig1c-head-direction-cells\n  expected:\n  - quantity: Cohort 1 cells encoding pitch velocity\n    value: 4\n    tolerance: 0.4\n  - quantity: Cohort 1 cells encoding roll velocity\n    value: 5\n    tolerance: 0.5\n  criterion: Same LN pipeline as fig1c-head-direction-cells. A 10% tolerance on counts this small\n    is below one cell, so the claim is judged on \"few\", reproduced when each count is at most\n    10 of 179 (twice the reported count), with the exact counts reported.\n- id: fig1c-azimuthal-velocity-cells\n  statement: A small population of Cohort 1 cells (12 of 179, 7%) encodes azimuthal head\n    velocity, and this is verified in Cohort 2, where 55 of 1021 cells (5%) do.\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 1\n  quote: A small population of neurons encoded azimuthal head velocity ... Tuning of neurons to\n    azimuthal head velocity was verified in an additional dataset in which head movements were\n    only measured in the azimuthal plane ( n = 55/1021 cells, 5%; Methods)\n  depends_on:\n  - fig1c-head-direction-cells\n  expected:\n  - quantity: Cohort 1 cells encoding azimuthal head velocity\n    value: 12\n    tolerance: 1.2\n  - quantity: Cohort 2 cells encoding azimuthal head velocity\n    value: 55\n    tolerance: 5.5\n  criterion: LN pipeline over the Cohort 1 variables, and over B, Bs, Ha and azimuthal head\n    velocity for Cohort 2. Reproduced when both counts are within tolerance under one reading\n    of open details (1) and (2); partially reproduced when one is.\n- id: fig1d-conjunctive-head\n  statement: Individual Cohort 1 cells commonly encode more than one variable (95 of 179); few\n    encode body speed, head direction, pitch, roll or azimuthal head velocity alone (2%, 5%,\n    1%, 5% and 0%), while 15% encode body position alone.\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 1;\n    Figure 1d legend\n  quote: Individual neurons commonly encoded information about multiple variables corresponding to\n    head or body movement (95/179 cells encoded > 1 variable)\n  depends_on:\n  - fig1c-head-direction-cells\n  expected:\n  - quantity: Cohort 1 cells encoding more than one variable\n    value: 95\n    tolerance: 9.5\n  - quantity: fraction of Cohort 1 cells encoding body position alone\n    value: 0.15\n    tolerance: 0.015\n  criterion: From the same selected models as fig1c-head-direction-cells. Reproduced when both\n    expected values are within tolerance under one reading and each of the five single-variable\n    fractions the legend gives for Bs, Ha, Hp, Hr and azimuthal head velocity is at most 5%;\n    partially reproduced when the count of conjunctive cells alone is within tolerance.\n- id: fig2-pitch-roll-shapes\n  statement: Nearly all pitch (44 of 46) and roll (52 of 53) tuning curves are fit by a\n    polynomial of order 5 or lower; most pitch cells are linear (17) or quadratic (16), and most\n    roll cells are quadratic (28, with 10 linear).\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 2;\n    Figure 2a iii, 2b iii\n  quote: The majority of cells encoding pitch exhibited either linear or quadratic relationships\n    between firing rate and pitch position (linear n = 17/46, quadratic n = 16/46 cells, Fig. 2 a\n    iii ), while the majority of cells encoding roll exhibited quadratic relationships between\n    firing rate and roll position (linear n = 10/53, quadratic n = 28/53 cells\n  depends_on:\n  - fig1c-pitch-roll-cells\n  expected:\n  - quantity: pitch cells well fit\n    value: 44\n    tolerance: 4.4\n  - quantity: roll cells well fit\n    value: 52\n    tolerance: 5.2\n  - quantity: linear pitch cells\n    value: 17\n    tolerance: 1.7\n  - quantity: quadratic pitch cells\n    value: 16\n    tolerance: 1.6\n  - quantity: linear roll cells\n    value: 10\n    tolerance: 1.0\n  - quantity: quadratic roll cells\n    value: 28\n    tolerance: 2.8\n  criterion: Classification as in the opening comment (Methods, Quantifying tuning curve\n    shape), on the cells of fig1c-pitch-roll-cells, with open detail (4) run under both\n    readings. Reproduced when, under one reading, linear plus quadratic is the majority of\n    pitch cells, quadratic is the largest class of roll cells, and at least four of the six\n    counts are within tolerance; partially reproduced when the two majority statements hold\n    alone.\n- id: fig2a-pitch-up-down-similar\n  statement: Similar proportions of pitch cells prefer upward and downward head tilts (26 of 44\n    upward).\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 2;\n    Figure 2a iii, iv\n  quote: Similar proportions of pitch-encoding cells were maximally activated by upward or downward\n    tilts of the head (upward-preferring n = 26/44 cells, Z = 1.06, P = 0.29, binomial test\n  statistics:\n  - test: binomial test\n    statistic: Z = 1.06\n    p: 0.29\n    n: 44 pitch cells\n  depends_on:\n  - fig2-pitch-roll-shapes\n  criterion: A claim of absence. Preference under open detail (5), on the well-fit pitch cells;\n    the binomial test against one half at P < 0.05. Reproduced when the test does not find a\n    preference; the proportion upward is given either way.\n- id: fig2b-roll-left-right-similar\n  statement: Similar proportions of roll cells prefer leftward (contraversive) and rightward\n    (ipsiversive) tilts (30 of 52 leftward).\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 2;\n    Figure 2b iii, iv\n  quote: similar proportions of roll-encoding cells preferred leftward (contraversive) and rightward\n    (ipsiversive) tilts (leftward-preferring n = 30/52 cells, Z = 0.82, P = 0.41\n  statistics:\n  - test: binomial test\n    statistic: Z = 0.82\n    p: 0.41\n    n: 52 roll cells\n  depends_on:\n  - fig2-pitch-roll-shapes\n  criterion: A claim of absence, judged as fig2a-pitch-up-down-similar on the well-fit roll\n    cells.\n- id: fig2-pitch-roll-stability\n  statement: Tuning to pitch (median 0.67) and roll (0.54) is about as stable across session\n    halves as tuning to azimuthal head direction (0.65).\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 2;\n    Figure 2a v, 2b v\n  quote: The stability of tuning to pitch or roll ... was comparable to that of azimuthal head\n    direction (median [1st–3rd quartile]; pitch = 0.67 [0.35–0.80], n = 44; roll = 0.54\n    [0.23–0.74], n = 52; azimuthal head direction = 0.65 [0.47–0.81], n = 63; Χ 2 = 4.26, P = 0.12,\n    df = 2, Kruskal–Wallis test\n  statistics:\n  - test: Kruskal-Wallis test\n    statistic: chi2 = 4.26, df = 2\n    p: 0.12\n    n: 44 pitch, 52 roll and 63 head direction cells\n  depends_on:\n  - fig2-pitch-roll-shapes\n  - fig1c-head-direction-cells\n  expected:\n  - quantity: median stability, pitch\n    value: 0.67\n    tolerance: 0.067\n  - quantity: median stability, roll\n    value: 0.54\n    tolerance: 0.054\n  - quantity: median stability, head direction\n    value: 0.65\n    tolerance: 0.065\n  criterion: A claim of absence. Stability as in the opening comment on the well-fit pitch and\n    roll cells and all head direction cells; reproduced when the Kruskal-Wallis test across\n    the three groups gives P >= 0.05, not reproduced when P < 0.05; the medians are compared\n    with their tolerances and reported either way.\n- id: fig2c-azimuthal-velocity-shapes\n  statement: Of 67 azimuthal head velocity cells pooled from both cohorts, 64 are fit by a\n    polynomial of order 5 or lower; 10 are linear (linear-asymmetric) and most are fit by higher\n    orders (30 quadratic, 8 cubic, 16 quartic).\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 3;\n    Figure 2c i to iii\n  quote: A subpopulation of neurons linearly increased or decreased their firing with azimuthal\n    head velocity ... However, most tuning curves were best fit by higher order polynomials\n    (quadratic n = 30/67, cubic n = 8/67, quartic n = 16/67 cells)\n  depends_on:\n  - fig1c-azimuthal-velocity-cells\n  expected:\n  - quantity: azimuthal head velocity cells well fit\n    value: 64\n    tolerance: 6.4\n  - quantity: linear cells\n    value: 10\n    tolerance: 1.0\n  - quantity: quadratic cells\n    value: 30\n    tolerance: 3.0\n  - quantity: cubic cells\n    value: 8\n    tolerance: 0.8\n  - quantity: quartic cells\n    value: 16\n    tolerance: 1.6\n  criterion: Classification as in fig2-pitch-roll-shapes (no smoothing for this variable), on\n    the cells of fig1c-azimuthal-velocity-cells from both cohorts. Reproduced when, under one\n    reading of open detail (4), higher orders hold the majority and at least three of the five\n    counts are within tolerance; partially reproduced when the majority holds alone.\n- id: fig2c-velocity-extrema-near-zero\n  statement: Maxima and minima of nonlinear azimuthal head velocity tuning curves cluster near 0\n    deg/s; their median does not differ from 0, and 52 of 63 lie within 50 deg/s.\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 3;\n    Supplementary Figure 7d\n  quote: Maxima and minima of these curves clustered near 0°/s\n  statistics:\n  - about: median peak or valley location against 0\n    test: two-sided Wilcoxon signed rank test\n    statistic: Z = 1.52\n    p: 0.13\n  - about: peaks or valleys within 50 deg/s against beyond\n    test: binomial test\n    statistic: Z = 5.04\n    p: 2.0e-7\n    n: 63 peaks or valleys\n  - about: entropy of peak or valley locations against a uniform distribution\n    p: 0.0020\n  depends_on:\n  - fig2c-azimuthal-velocity-shapes\n  expected:\n  - quantity: peaks or valleys with absolute velocity below 50 deg/s\n    value: 52\n    tolerance: 5.2\n  criterion: Peaks and valleys found with findpeaks on the nonlinear curves, keeping those that\n    take the curve's maximum or minimum (Methods, Quantifying head and eye velocity tuning\n    curves). Reproduced when the count below 50 deg/s is within tolerance, the binomial test\n    gives P < 0.05 and the signed rank test of the median against 0 gives P >= 0.05.\n- id: fig2c-symmetric-asymmetric-classes\n  statement: About half of nonlinear azimuthal head velocity cells are asymmetric (28 of 64) and\n    half symmetric (26 of 64); most symmetric cells increase firing with head speed (20 of 26),\n    significantly more than fire most when the head is still (6 of 26).\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 3;\n    Figure 2c iii, iv\n  quote: Whereas the majority of symmetric cells increased their firing rates with increasing head\n    speeds [NL s-pos ] ( n = 20/26), others fired maximally when the head was stationary [NL s-neg\n    ] ( n = 6/26, Z = 2.55, P = 0.009)\n  statistics:\n  - about: positive against negative symmetric cells\n    test: binomial test\n    statistic: Z = 2.55\n    p: 0.009\n    n: 26 symmetric cells\n  depends_on:\n  - fig2c-azimuthal-velocity-shapes\n  expected:\n  - quantity: nonlinear-asymmetric cells\n    value: 28\n    tolerance: 2.8\n  - quantity: nonlinear-symmetric cells\n    value: 26\n    tolerance: 2.6\n  - quantity: symmetric cells increasing with speed\n    value: 20\n    tolerance: 2.0\n  criterion: Classes under open detail (6), run under both readings. Reproduced when, under one\n    reading, the asymmetric and symmetric counts are within tolerance and the binomial test of\n    positive against negative symmetric cells gives P < 0.05 with more positive cells;\n    partially reproduced when the binomial result holds alone.\n- id: fig2c-asymmetric-direction-similar\n  statement: Similar proportions of asymmetric azimuthal head velocity cells prefer ipsiversive\n    and contraversive head rotation (23 of 38 contraversive).\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 3;\n    Figure 2c iii\n  quote: Similar proportions of asymmetric cells preferred ipsiversive ... versus contraversive head\n    movements (contraversive-preferring n = 23/38, Z = 1.16, P = 0.26)\n  statistics:\n  - test: binomial test\n    statistic: Z = 1.16\n    p: 0.26\n    n: 38 asymmetric cells\n  depends_on:\n  - fig2c-symmetric-asymmetric-classes\n  criterion: A claim of absence. The 38 cells are the linear and nonlinear asymmetric cells\n    (10 + 28); direction is relative to the recorded hemisphere, preference under open detail\n    (5). Reproduced when the binomial test against one half gives P >= 0.05.\n- id: fig2c-velocity-stability\n  statement: Tuning to azimuthal head velocity is highly stable across session halves (median\n    0.91), comparable to tuning to body speed (0.86).\n  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 3;\n    Figure 2c v\n  quote: Tuning to azimuthal head velocity was highly stable across the first and second half of\n    the recording session (median [1st–3rd quartile]; 0.91 [0.74–0.96], n = 64; Fig. 2 c v ), and\n    comparable to the stability of tuning to body speed (0.86 [0.63–0.95], n = 52; Z = 1.66, P =\n    0.097, Wilcoxon rank-sum test)\n  statistics:\n  - test: Wilcoxon rank-sum test\n    statistic: Z = 1.66\n    p: 0.097\n    n: 64 azimuthal head velocity and 52 body speed cells\n  depends_on:\n  - fig2c-azimuthal-velocity-shapes\n  expected:\n  - quantity: median stability, azimuthal head velocity\n    value: 0.91\n    tolerance: 0.091\n  - quantity: median stability, body speed\n    value: 0.86\n    tolerance: 0.086\n  criterion: A claim of absence. The 52 body speed cells are not identified; read as the Cohort\n    1 body speed cells (52 of 179, the count Supplementary Fig. 3b gives). Reproduced when the\n    rank-sum test gives P >= 0.05; medians reported against their tolerances.\n- id: fig3ab-head-contributions\n  statement: Body position contributes most to MEC spiking, then azimuthal head direction; pitch\n    and roll each contribute less than head direction but on par with body speed, and azimuthal\n    head velocity contributes least.\n  source: Results, Conjunctive coding of head movements and other navigation-related variables,\n    paragraph 1; Figure 3a, b\n  quote: we observed that body position was the strongest predictor of MEC spiking, followed by\n    azimuthal head direction ... head pitch and roll position each contributed less to MEC spiking\n    than azimuthal head direction ( P = 3.7e−7), but were on par with body speed\n  statistics:\n  - about: all six variables\n    test: Kruskal-Wallis test\n    statistic: chi2 = 410.3, df = 5\n    p: 1.7e-86\n  - about: B against Ha\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 1.3e-26\n    corrected: Bonferroni, alpha 0.0033\n  - about: Ha against the remaining variables\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 3.5e-4\n    corrected: Bonferroni, alpha 0.0033\n  - about: pitch and roll against Ha\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 3.7e-7\n    corrected: Bonferroni, alpha 0.0033\n  - about: pitch and roll against body speed\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 0.38\n    corrected: Bonferroni, alpha 0.0033\n  depends_on:\n  - fig1c-azimuthal-velocity-cells\n  expected:\n  - quantity: median contribution, B (n = 394)\n    value: 0.64\n    tolerance: 0.064\n  - quantity: median contribution, Ha (n = 327)\n    value: 0.32\n    tolerance: 0.032\n  - quantity: median contribution, Bs (n = 332)\n    value: 0.15\n    tolerance: 0.015\n  - quantity: median contribution, pitch (n = 44)\n    value: 0.13\n    tolerance: 0.013\n  - quantity: median contribution, roll (n = 44)\n    value: 0.17\n    tolerance: 0.017\n  - quantity: median contribution, azimuthal head velocity (n = 64)\n    value: 0.06\n    tolerance: 0.006\n  criterion: Contribution under open detail (3), for cells of both cohorts that encode the\n    variable and at least one other (Figure 3a legend). Kruskal-Wallis over the six variables\n    and post hoc rank-sum tests at alpha 0.0033, with open detail (8) for the pooled pairs.\n    Reproduced when, under one reading, the order B > Ha > (pitch, roll, Bs) > azimuthal head\n    velocity of medians holds, B against Ha, Ha against each of Bs, pitch and roll, and pitch and\n    roll against Ha are significant, pitch and roll against Bs are not, and at least four of\n    the six medians are within tolerance. Partially reproduced when the order and tests hold\n    but fewer medians are in tolerance.\n- id: fig3c-freely-moving-model-fit\n  statement: Over 869 freely moving cells that encode at least one variable, the\n    spike-normalized held-out log-likelihood increase has median 0.11.\n  source: Figure 3c legend\n  quote: The spike-normalized average log-likelihood increase in information across 10 folds of\n    held-out data for all cells significantly encoding at least one variable (median [1st–3rd\n    quartile]; 0.11 [0.04–0.26], n = 869)\n  depends_on:\n  - fig1c-azimuthal-velocity-cells\n  expected:\n  - quantity: cells encoding at least one variable, both cohorts\n    value: 869\n    tolerance: 86.9\n  - quantity: median log-likelihood increase\n    value: 0.11\n    tolerance: 0.011\n    unit: bits per spike\n  criterion: Fold mean of the selected model's log-likelihood increase in bits per spike\n    (compute_llh.m). Reproduced when both values are within tolerance under one reading of open\n    details (1) and (2).\n- id: fig3e-head-no-clustering\n  statement: Cells with similar tuning to a head or body variable do not tend to encode the same\n    additional variables; no combination shows clustering of labels in tuning curve profile\n    space.\n  source: Results, Conjunctive coding of head movements and other navigation-related variables,\n    paragraph 2; Figure 3e; Supplementary Figure 11a to c\n  quote: Across all possible combinations, we did not observe any clustering in the assigned\n    labels (all Bonferroni corrected P > 0.005; Methods; Supplementary Fig. 11 )\n  statistics:\n  - test: k-nearest-neighbour distance against label-scrambled null\n    p: 0.005\n    p_relation: \">\"\n    corrected: Bonferroni, over k = 1 to 10\n  depends_on:\n  - fig1c-azimuthal-velocity-cells\n  criterion: A claim of absence. For each primary variable, model-derived tuning curves (50 bins,\n    Methods) are mean-subtracted and scaled to unit range, projected on two principal components;\n    for each secondary variable, the mean distance from each labelled cell to its k nearest\n    labelled neighbours, k from 1 to 10, is compared with a label-scrambled null, P the fraction\n    of null distances smaller than observed. The number of scrambles is not given; 1000 is a\n    standard choice. Reproduced when no combination and k gives P < 0.005.\n- id: fig4f-eye-movement-distributions\n  statement: Head-fixed mice in VR move their eyes considerably; the inner 98% of horizontal eye\n    position spans about -3.5 to 5.3% of eye width and of vertical position -2.7 to 1.6%.\n  source: Results, Entorhinal neurons encode eye movements, paragraph 2; Figure 4c to i legend\n  quote: On the virtual track with landmarks, head-fixed mice moved their eyes considerably, as\n    reported previously\n  expected:\n  - quantity: horizontal eye position 1st percentile\n    value: -3.50\n    tolerance: 0.61\n    unit: percent of eye width\n  - quantity: horizontal eye position 99th percentile\n    value: 5.28\n    tolerance: 0.87\n    unit: percent of eye width\n  - quantity: vertical eye position 1st percentile\n    value: -2.74\n    tolerance: 0.64\n    unit: percent of eye width\n  - quantity: vertical eye position 99th percentile\n    value: 1.60\n    tolerance: 0.21\n    unit: percent of eye width\n  - quantity: horizontal eye velocity 1st percentile\n    value: -6.19\n    tolerance: 0.74\n    unit: percent of eye width per s\n  - quantity: horizontal eye velocity 99th percentile\n    value: 6.87\n    tolerance: 0.66\n    unit: percent of eye width per s\n  criterion: Percentiles per session, about the mean position, averaged per mouse, mean over 8\n    mice, with the legend's sem across mice as tolerance. Reproduced when at least five of six\n    are within tolerance; partially for three or four.\n- id: fig4j-eye-encoding-cells\n  statement: Of 2861 MEC cells in head-fixed mice, 711 (25%) carry eye movement signals; 343\n    (12%) encode horizontal eye position, 234 (9%) vertical eye position, 244 (9%) horizontal\n    eye velocity and 135 (5%) vertical eye velocity.\n  source: Results, Entorhinal neurons encode eye movements, paragraph 2; Figure 4j\n  quote: 711/2861 MEC cells [25%] carried signals related to eye movements ... 343 cells [12%]\n    encoded horizontal eye position, 234 cells [9%] encoded vertical eye position, 244 cells [9%]\n    cells encoded horizontal eye velocity, and 135 cells [5%] encoded vertical eye velocity.\n  expected:\n  - quantity: cells encoding any eye variable\n    value: 711\n    tolerance: 71.1\n  - quantity: cells encoding Eh\n    value: 343\n    tolerance: 34.3\n  - quantity: cells encoding Ev\n    value: 234\n    tolerance: 23.4\n  - quantity: cells encoding Eh dot\n    value: 244\n    tolerance: 24.4\n  - quantity: cells encoding Ev dot\n    value: 135\n    tolerance: 13.5\n  criterion: LN pipeline over B, Bs, Eh, Ev, Eh dot and Ev dot for the 11 recordings on the\n    landmark track, with open details (1) and (2) under both readings. Reproduced when, under\n    one reading, the count of eye-encoding cells and at least three of the four per-variable\n    counts are within tolerance; partially reproduced when the total alone is.\n- id: fig4k-eye-conjunctive\n  statement: Most eye movement cells (96%) also encode body position or speed, 28% encode more\n    than one eye parameter, and few cells encode an eye variable alone; 23% of cells encode body\n    position alone.\n  source: Results, Entorhinal neurons encode eye movements, paragraph 2; Figure 4j, k legend\n  quote: The majority of cells encoding eye movements conjunctively encoded body position or speed\n    (96%), and a subset of cells encoded multiple parameters of eye movements (28%, Fig. 4j, k )\n  depends_on:\n  - fig4j-eye-encoding-cells\n  expected:\n  - quantity: fraction of eye cells also encoding B or Bs\n    value: 0.96\n    tolerance: 0.096\n  - quantity: fraction of eye cells encoding more than one eye variable\n    value: 0.28\n    tolerance: 0.028\n  - quantity: fraction of all cells encoding B alone\n    value: 0.23\n    tolerance: 0.023\n  criterion: From the selected models of fig4j-eye-encoding-cells. Reproduced when all three are\n    within tolerance under one reading; partially for two. A tolerance of 0.096 on 0.96 is\n    capped at 1.\n- id: fig5a-eh-nasal-temporal-similar\n  statement: Among horizontal eye position cells, similar proportions fire most for nasal and\n    temporal positions (170 of 343 nasal), also in each hemisphere.\n  source: Results, Entorhinal neurons encode eye movements, paragraph 3; Figure 5a iii\n  quote: Of the cells encoding horizontal eye position, a similar proportion fired maximally for\n    nasal versus temporal eye positions (nasal-preferring n = 170/343, Z = 0.11, P = 0.91\n  statistics:\n  - about: all cells\n    test: binomial test\n    statistic: Z = 0.11\n    p: 0.91\n    n: 343 cells\n  - about: ipsilateral hemisphere\n    test: binomial test\n    statistic: Z = 1.07\n    p: 0.28\n    n: 87 cells\n  - about: contralateral hemisphere\n    test: binomial test\n    statistic: Z = 0.43\n    p: 0.66\n    n: 256 cells\n  depends_on:\n  - fig4j-eye-encoding-cells\n  criterion: A claim of absence. Preference under open detail (5) on all Eh cells (343 of 343\n    are classified); recordings in the right MEC are ipsilateral to the tracked right eye.\n    Reproduced when none of the three binomial tests gives P < 0.05.\n- id: fig5b-ev-up-down-similar\n  statement: Of 234 vertical eye position cells 177 are classified by shape, and similar\n    proportions of them fire most for upward and downward positions (88 of 177 upward).\n  source: Results, Entorhinal neurons encode eye movements, paragraph 3; Figure 5b iii\n  quote: of cells encoding vertical eye position, similar proportions fired maximally for upward\n    versus downward eye positions (upward-preferring n = 88/177, Z = 0, P = 1\n  statistics:\n  - test: binomial test\n    statistic: Z = 0\n    p: 1\n    n: 177 cells\n  depends_on:\n  - fig4j-eye-encoding-cells\n  expected:\n  - quantity: Ev cells classified by shape\n    value: 177\n    tolerance: 17.7\n  criterion: A claim of absence. Classification and preference as in the opening comment and\n    open details (4) and (5). Reproduced when the binomial test gives P >= 0.05; the count\n    classified is compared with its tolerance.\n- id: fig5-eye-position-stability\n  statement: Tuning to eye position is stable across session halves; horizontal eye position\n    (median 0.87) is significantly more stable than virtual body position (0.71), and vertical\n    eye position (0.72) is similar to body position.\n  source: Results, Entorhinal neurons encode eye movements, paragraph 3; Figure 5a v, 5b v\n  quote: with tuning to horizontal eye position significantly more stable than tuning to virtual\n    body position, and tuning to vertical eye position similar to that of virtual body position\n  statistics:\n  - about: Eh, Ev and B\n    test: Kruskal-Wallis test\n    statistic: chi2 = 103.51, df = 2\n    p: 3.3e-23\n  - about: Eh against B\n    test: Wilcoxon rank-sum, pairwise\n    p: 8.6e-25\n  - about: Ev against B\n    test: Wilcoxon rank-sum, pairwise\n    p: 0.91\n  depends_on:\n  - fig5b-ev-up-down-similar\n  expected:\n  - quantity: median stability, Eh (n = 343)\n    value: 0.87\n    tolerance: 0.087\n  - quantity: median stability, Ev (n = 177)\n    value: 0.72\n    tolerance: 0.072\n  - quantity: median stability, B (n = 1968)\n    value: 0.71\n    tolerance: 0.071\n  criterion: Stability as in the opening comment for all Eh cells, the classified Ev cells and\n    all B cells. The Kruskal-Wallis P is printed \"3.3–23\" and is read as 3.3e-23. The pairwise\n    alpha is not stated for this test; 0.0167 (Bonferroni over three pairs, as in the Figure 5\n    legends) is used. Reproduced when Eh is significantly more stable than B, Ev against B is not\n    significant, and the three medians are within tolerance; partially reproduced when the tests\n    hold but a median is out of tolerance.\n- id: fig5av-eh-linear-most-stable\n  statement: Linearly tuned horizontal eye position cells are more stable than those with\n    greater curvature (medians 0.93, 0.87 and 0.66 for linear, quadratic and higher order).\n  source: Figure 5a v legend\n  quote: linearly tuned cells were significantly more stable than those exhibiting greater\n    curvature (median [1st–3rd quartile]; 1° = 0.93 [0.85–0.98]; 2° = 0.87 [0.71–0.95]; >2° = 0.66\n    [0.15–0.83]; Χ 2 = 69.59, P = 7.7e−16, df = 2\n  statistics:\n  - about: three classes\n    test: Kruskal-Wallis test\n    statistic: chi2 = 69.59, df = 2\n    p: 7.7e-16\n  - about: linear against quadratic\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 2.6e-5\n    corrected: Bonferroni, alpha 0.0167\n  - about: linear against higher order\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 1.8e-15\n    corrected: Bonferroni, alpha 0.0167\n  - about: quadratic against higher order\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 4.1e-8\n    corrected: Bonferroni, alpha 0.0167\n  depends_on:\n  - fig5-eye-position-stability\n  expected:\n  - quantity: median stability, linear Eh cells\n    value: 0.93\n    tolerance: 0.093\n  - quantity: median stability, quadratic Eh cells\n    value: 0.87\n    tolerance: 0.087\n  - quantity: median stability, higher order Eh cells\n    value: 0.66\n    tolerance: 0.066\n  criterion: Reproduced when the Kruskal-Wallis test gives P < 0.05, linear cells are\n    significantly more stable than both other classes at alpha 0.0167, and at least two medians\n    are within tolerance, under one reading of open detail (4).\n- id: fig5bv-ev-low-order-more-stable\n  statement: Linearly or quadratically tuned vertical eye position cells are more stable than\n    those with greater curvature.\n  source: Figure 5b v legend\n  quote: linearly or quadratically tuned cells were significantly more stable than those\n    exhibiting greater curvature\n  statistics:\n  - about: three classes\n    test: Kruskal-Wallis test\n    statistic: chi2 = 17.17, df = 2\n    p: 1.9e-4\n  - about: linear against higher order\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 0.012\n    corrected: Bonferroni, alpha 0.0167\n  - about: quadratic against higher order\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 0.0001\n    corrected: Bonferroni, alpha 0.0167\n  - about: linear against quadratic\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 0.87\n    corrected: Bonferroni, alpha 0.0167\n  depends_on:\n  - fig5b-ev-up-down-similar\n  expected:\n  - quantity: median stability, linear Ev cells\n    value: 0.86\n    tolerance: 0.086\n  - quantity: median stability, quadratic Ev cells\n    value: 0.86\n    tolerance: 0.086\n  - quantity: median stability, higher order Ev cells\n    value: 0.56\n    tolerance: 0.056\n  criterion: Reproduced when the Kruskal-Wallis test gives P < 0.05, linear and quadratic cells\n    are each significantly more stable than higher order cells at alpha 0.0167, and at least two\n    medians are within tolerance, under one reading of open detail (4).\n- id: fig6-eye-velocity-linear-nasal\n  statement: A small subpopulation of eye velocity cells is linear (43 of 244 horizontal, 29 of\n    131 vertical); linear horizontal cells prefer nasal-directed movement (30 of 43), and linear\n    vertical cells show no up or down preference (16 of 29 upward).\n  source: Results, Entorhinal neurons encode eye movements, paragraph 4; Figure 6a iii, iv and\n    6b iii, iv\n  quote: Linear-asymmetric cells encoding horizontal eye velocity showed a preference for\n    nasal-directed movements (nasal-preferring n = 30/43, Z = 2.44, P = 0.014)\n  statistics:\n  - about: linear Eh dot cells, nasal against temporal\n    test: binomial test\n    statistic: Z = 2.44\n    p: 0.014\n    n: 43 cells\n  - about: linear Ev dot cells, upward against downward\n    test: binomial test\n    statistic: Z = 0.37\n    p: 0.71\n    n: 29 cells\n  depends_on:\n  - fig4j-eye-encoding-cells\n  expected:\n  - quantity: linear Eh dot cells\n    value: 43\n    tolerance: 4.3\n  - quantity: linear Ev dot cells\n    value: 29\n    tolerance: 2.9\n  - quantity: nasal-preferring linear Eh dot cells\n    value: 30\n    tolerance: 3.0\n  criterion: Classification as in the opening comment; preference is the sign of the linear fit.\n    Reproduced when, under one reading of open detail (4), the horizontal binomial test gives\n    P < 0.05 with a nasal majority, the vertical test gives P >= 0.05, and the two linear counts\n    are within tolerance; partially reproduced when the tests hold alone.\n- id: fig6-eye-velocity-nonlinear-temporal\n  statement: Most eye velocity cells are nonlinear (201 of 244 horizontal, 102 of 131 vertical),\n    split into asymmetric (147 and 68) and symmetric (54 and 34) cells; asymmetric horizontal\n    cells prefer temporal movement (87 of 147) and asymmetric vertical cells show no preference.\n  source: Results, Entorhinal neurons encode eye movements, paragraph 4; Figure 6a iii, iv and\n    6b iii, iv\n  quote: Nonlinear-asymmetric cells encoding horizontal movement preferred temporal-directed\n    movements ... temporal-preferring n = 87/147, Z = 2.22, P = 0.026\n  statistics:\n  - about: nonlinear-asymmetric Eh dot cells, temporal against nasal\n    test: binomial test\n    statistic: Z = 2.22\n    p: 0.026\n    n: 147 cells\n  - about: nonlinear-asymmetric Ev dot cells, downward against upward\n    test: binomial test\n    statistic: Z = -0.61\n    p: 0.54\n    n: 68 cells\n  depends_on:\n  - fig4j-eye-encoding-cells\n  expected:\n  - quantity: nonlinear-asymmetric Eh dot cells\n    value: 147\n    tolerance: 14.7\n  - quantity: nonlinear-symmetric Eh dot cells\n    value: 54\n    tolerance: 5.4\n  - quantity: nonlinear-asymmetric Ev dot cells\n    value: 68\n    tolerance: 6.8\n  - quantity: nonlinear-symmetric Ev dot cells\n    value: 34\n    tolerance: 3.4\n  criterion: Classes under open detail (6), preference under open detail (5), both run under\n    each reading. Reproduced when, under one combination, the horizontal binomial test gives\n    P < 0.05 with a temporal majority, the vertical one gives P >= 0.05, and at least three of the\n    four counts are within tolerance; partially reproduced when the tests hold alone.\n- id: fig6-eye-velocity-stability\n  statement: Tuning to horizontal eye velocity (median 0.93) is significantly more stable than\n    tuning to virtual body speed (0.84), and tuning to vertical eye velocity (0.74) is\n    significantly less stable.\n  source: Results, Entorhinal neurons encode eye movements, paragraph 4; Figure 6a v, 6b v\n  quote: Tuning to horizontal eye velocity was significantly more stable than that to virtual body\n    speed, while tuning to vertical eye velocity was significantly less stable\n  statistics:\n  - about: Eh dot, Ev dot and Bs\n    test: Kruskal-Wallis test\n    statistic: chi2 = 90.78, df = 2\n    p: 1.9e-20\n  - about: Eh dot against Bs\n    test: Wilcoxon rank-sum, pairwise\n    p: 6.5e-18\n  - about: Ev dot against Bs\n    test: Wilcoxon rank-sum, pairwise\n    p: 0.00061\n  depends_on:\n  - fig4j-eye-encoding-cells\n  expected:\n  - quantity: median stability, Eh dot (n = 244)\n    value: 0.93\n    tolerance: 0.093\n  - quantity: median stability, Ev dot (n = 131)\n    value: 0.74\n    tolerance: 0.074\n  - quantity: median stability, Bs (n = 1321)\n    value: 0.84\n    tolerance: 0.084\n  criterion: The Kruskal-Wallis P is printed \"1.9–20\" and is read as 1.9e-20; pairwise alpha\n    0.0167 as in fig5-eye-position-stability. Reproduced when Eh dot is significantly more and\n    Ev dot significantly less stable than Bs and the medians are within tolerance; partially\n    reproduced when the tests hold but a median is out of tolerance.\n- id: fig6v-asymmetric-more-stable\n  statement: Asymmetric eye velocity cells are more stable than symmetric ones; for horizontal\n    eye velocity both linear and nonlinear asymmetric cells exceed symmetric cells, for vertical\n    eye velocity nonlinear asymmetric cells exceed symmetric cells.\n  source: Figure 6a v and 6b v legends\n  quote: linear-asymmetric and nonlinear-asymmetric cells were significantly more stable than\n    nonlinear-symmetric cells\n  statistics:\n  - about: Eh dot classes\n    test: Kruskal-Wallis test\n    statistic: chi2 = 19.30, df = 2\n    p: 6.4e-5\n  - about: Eh dot, linear-asymmetric against symmetric\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 0.00028\n    corrected: Bonferroni, alpha 0.0167\n  - about: Eh dot, nonlinear-asymmetric against symmetric\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 0.00012\n    corrected: Bonferroni, alpha 0.0167\n  - about: Ev dot classes\n    test: Kruskal-Wallis test\n    statistic: chi2 = 11.37, df = 2\n    p: 0.0034\n  - about: Ev dot, nonlinear-asymmetric against symmetric\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 0.0014\n    corrected: Bonferroni, alpha 0.0167\n  depends_on:\n  - fig6-eye-velocity-nonlinear-temporal\n  expected:\n  - quantity: median stability, Eh dot linear-asymmetric\n    value: 0.96\n    tolerance: 0.096\n  - quantity: median stability, Eh dot nonlinear-symmetric\n    value: 0.86\n    tolerance: 0.086\n  - quantity: median stability, Ev dot nonlinear-asymmetric\n    value: 0.85\n    tolerance: 0.085\n  - quantity: median stability, Ev dot nonlinear-symmetric\n    value: 0.38\n    tolerance: 0.038\n  criterion: Reproduced when, under one reading of open detail (6), both Kruskal-Wallis tests\n    give P < 0.05 and the three named pairwise comparisons are significant at alpha 0.0167 in the\n    stated direction; partially reproduced when the horizontal or the vertical part holds alone.\n- id: fig7ab-eye-contributions\n  statement: Body position and speed influence MEC spiking more than eye movement signals, and eye\n    position contributes more than eye velocity.\n  source: Results, Entorhinal neurons encode eye movements, paragraph 5; Figure 7a, b\n  quote: body position and speed influenced MEC spiking more strongly than eye movement-related\n    signals ... The contributions of horizontal and vertical eye position were greater than those\n    of horizontal and vertical eye velocity ( P = 1.9e–10)\n  statistics:\n  - about: all six variables\n    test: Kruskal-Wallis test\n    statistic: chi2 = 1.3e3, df = 5\n    p: 5.5e-276\n  - about: eye position against eye velocity\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 1.9e-10\n    corrected: Bonferroni, alpha 0.0033\n  depends_on:\n  - fig4j-eye-encoding-cells\n  expected:\n  - quantity: median contribution, B (n = 1319)\n    value: 0.65\n    tolerance: 0.065\n  - quantity: median contribution, Bs (n = 1187)\n    value: 0.26\n    tolerance: 0.026\n  - quantity: median contribution, Eh (n = 335)\n    value: 0.10\n    tolerance: 0.010\n  - quantity: median contribution, Ev (n = 231)\n    value: 0.14\n    tolerance: 0.014\n  - quantity: median contribution, Eh dot (n = 237)\n    value: 0.05\n    tolerance: 0.005\n  - quantity: median contribution, Ev dot (n = 132)\n    value: 0.04\n    tolerance: 0.004\n  criterion: Contribution under open detail (3) for cells encoding the variable and at least one\n    other. Reproduced when, under one reading, B and Bs each exceed every eye variable and Eh and\n    Ev each exceed Eh dot and Ev dot by post hoc rank-sum tests at alpha 0.0033, and at least\n    four of the six medians are within tolerance; partially reproduced when the tests hold alone.\n- id: fig7c-head-fixed-model-fit\n  statement: Over 2191 head-fixed cells that encode at least one variable, the held-out\n    log-likelihood increase has median 0.05 bits per spike.\n  source: Figure 7c legend\n  quote: The spike-normalized average log-likelihood increase in information across 10 folds of\n    held-out data for all cells significantly encoding at least one variable (median [1st–3rd\n    quartile]; 0.05 [0.02–0.11], n = 2191)\n  depends_on:\n  - fig4j-eye-encoding-cells\n  expected:\n  - quantity: cells encoding at least one variable, head-fixed\n    value: 2191\n    tolerance: 219.1\n  - quantity: median log-likelihood increase\n    value: 0.05\n    tolerance: 0.005\n    unit: bits per spike\n  criterion: As fig3c-freely-moving-model-fit, on the head-fixed cells.\n- id: fig7e-eye-no-clustering\n  statement: Cells with similar tuning to eye position or velocity do not tend to encode similar\n    additional variables.\n  source: Results, Entorhinal neurons encode eye movements, paragraph 5; Figure 7e, f;\n    Supplementary Figure 11d to f\n  quote: As with cells encoding head movements, cells that exhibited similar tuning to eye position\n    or velocity did not tend to encode similar additional variables\n  depends_on:\n  - fig4j-eye-encoding-cells\n  criterion: A claim of absence, judged as fig3e-head-no-clustering on the head-fixed variables,\n    at the Bonferroni level 0.05/10 the Methods give. Reproduced when no combination and k gives\n    P < 0.005.\n- id: fig8c-eye-tuning-without-landmarks\n  statement: Without visual landmarks, body position tuning degrades or remaps (median\n    correlation across tracks 0.02), while tuning to body speed and to all eye movement variables\n    is preserved significantly more (medians 0.40 to 0.82).\n  source: Results, Encoding of eye position and eye velocity persists in the absence of visual\n    landmark features, paragraph 1; Figure 8c, d\n  quote: Position tuning curves were nearly uncorrelated between the tracks (median [1st–3rd\n    quartile], B = 0.02 [−0.19–0.25], whereas the tuning curves for cells encoding all eye\n    movement-related variables and body speed were preserved to a significantly greater extent\n  statistics:\n  - about: six variables\n    test: Kruskal-Wallis test\n    statistic: chi2 = 748.27, df = 5\n    p: 1.8e-159\n  - about: B against each other variable\n    test: two-sided Wilcoxon rank-sum, post hoc\n    p: 0.00024\n    p_relation: \"<\"\n    corrected: Bonferroni, alpha 0.0033\n    n: 1621 cells from 6 sessions in 6 mice\n  expected:\n  - quantity: median correlation, B\n    value: 0.02\n    tolerance: 0.1\n  - quantity: median correlation, Bs\n    value: 0.82\n    tolerance: 0.082\n  - quantity: median correlation, Eh\n    value: 0.69\n    tolerance: 0.069\n  - quantity: median correlation, Ev\n    value: 0.54\n    tolerance: 0.054\n  - quantity: median correlation, Eh dot\n    value: 0.73\n    tolerance: 0.073\n  - quantity: median correlation, Ev dot\n    value: 0.40\n    tolerance: 0.040\n  criterion: Cells are those encoding each variable on the landmark track (LN pipeline on the\n    landmark blocks), the correlation between their tuning curves in the two tracks under open\n    detail (7). The B tolerance is 0.1, as 10% of 0.02 is below any meaningful resolution of a\n    correlation; 0.1 is a tenth of the scale. Reproduced when, under one reading, the\n    Kruskal-Wallis test gives P < 0.05, B is lower than each other variable at alpha 0.0033, and\n    at least four of the six medians are within tolerance; partially reproduced when the tests\n    hold alone.\n- id: fig8e-joint-cells-preserve-eye-tuning\n  statement: Eye position tuning is preserved across tracks even in cells that jointly encode\n    body position and eye position.\n  source: Results, Encoding of eye position and eye velocity persists in the absence of visual\n    landmark features, paragraph 1; Figure 8e\n  quote: This effect was observed even in cells that jointly encode body position and eye position\n    (Fig. 8e ).\n  depends_on:\n  - fig8c-eye-tuning-without-landmarks\n  criterion: The paper shows examples and no test. For cells encoding both B and Eh on the landmark\n    track, the cross-track correlation of Eh tuning curves is compared with that of their B\n    tuning curves by a two-sided Wilcoxon signed-rank test, a test chosen here (the paper names\n    none, and this is an assumption). Reproduced when the median Eh correlation exceeds the\n    median B correlation with P < 0.05 under one reading of open detail (7).\n- id: methods-hemispheres-similar\n  statement: The proportion of MEC neurons tuned to eye movement variables does not differ between\n    left (mean 0.23) and right (0.43) hemisphere recordings.\n  source: Methods, Head-fixed dataset, Data collection\n  quote: We did not observe a difference in the proportions of MEC neurons encoding eye\n    movement-related variables across the left and right hemispheres\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.23\n    n: 4 left and 7 right recordings\n  depends_on:\n  - fig4j-eye-encoding-cells\n  expected:\n  - quantity: mean proportion, left hemisphere\n    value: 0.23\n    tolerance: 0.083\n  - quantity: mean proportion, right hemisphere\n    value: 0.43\n    tolerance: 0.083\n  criterion: A claim of absence. Per recording, the fraction of cells encoding one or more eye\n    variable; reproduced when the rank-sum test over recordings gives P >= 0.05. Means compared\n    with the sem the paper gives as tolerance.\n- id: supp3-low-false-positives\n  statement: Shuffling one variable in time and refitting yields few falsely detected cells for\n    each variable, in both datasets (for example 0 of 46 for pitch, 1 of 12 for azimuthal head\n    velocity, 5 of 343 for horizontal eye position, 13 of 135 for vertical eye velocity).\n  source: Supplementary Figure 3b, c\n  quote: Here, we observed a very low chance of false positives for each variable\n  depends_on:\n  - fig1c-head-direction-cells\n  - fig4j-eye-encoding-cells\n  expected:\n  - quantity: falsely detected vertical eye velocity cells, head-fixed\n    value: 13\n    tolerance: 1.3\n  - quantity: falsely detected horizontal eye velocity cells, head-fixed\n    value: 8\n    tolerance: 0.8\n  criterion: As in the Methods (Identifying rate of falsely detected encoded variables), one\n    variable at a time is shuffled across time bins in Cohort 1 and in the head-fixed data and the\n    whole LN pipeline is rerun. One shuffle per variable, as the counts imply. Reproduced when for\n    every variable the falsely detected count is at most 10% of the normally detected count\n    (the largest the paper reports is 13 of 135), with the counts reported; the expected values\n    are given for reference, a shuffle being random.\n- id: supp4-ln-conservative\n  statement: Shuffle-based significance tests (within-cell and pooled) identify far more cells\n    than the LN model, and nearly all LN model cells are also found by shuffling, so the LN model\n    is a conservative estimate.\n  source: Supplementary Figure 4d\n  quote: note that nearly all of the cells identified by the LN-model were also identified by\n    shuffling\n  depends_on:\n  - fig1c-head-direction-cells\n  - fig4j-eye-encoding-cells\n  criterion: Shuffling as in the Methods (Comparison between LN and shuffling-based methods),\n    Pearson correlation of instantaneous behaviour and firing rate against 500 spike train shifts\n    of more than 20 s, 2.5th and 97.5th percentiles (5th and 95th for the symmetric velocity\n    test). \"Linearly encoding\" cells are read as the LN cells of the variable, all classes.\n    Reproduced when, for each of pitch, roll, azimuthal head velocity and the four eye variables,\n    each shuffle method finds more cells than the LN model and at least 90% of LN cells are\n    found by within-cell shuffling (a reading of \"nearly all\").\n- id: supp5-model-raw-tuning-agree\n  statement: Model-derived and raw tuning curves are highly correlated (median 0.85 to 0.94\n    across the seven head and eye variables).\n  source: Supplementary Figure 5b\n  quote: Overall, we found the model-derived and firing rate-derived tuning curves for a given\n    variable to be highly correlated\n  depends_on:\n  - fig1c-pitch-roll-cells\n  - fig4j-eye-encoding-cells\n  expected:\n  - quantity: median correlation, pitch\n    value: 0.94\n    tolerance: 0.094\n  - quantity: median correlation, roll\n    value: 0.93\n    tolerance: 0.093\n  - quantity: median correlation, azimuthal head velocity\n    value: 0.90\n    tolerance: 0.090\n  - quantity: median correlation, Eh\n    value: 0.90\n    tolerance: 0.090\n  - quantity: median correlation, Ev\n    value: 0.85\n    tolerance: 0.085\n  - quantity: median correlation, Eh dot\n    value: 0.85\n    tolerance: 0.085\n  - quantity: median correlation, Ev dot\n    value: 0.87\n    tolerance: 0.087\n  criterion: Raw tuning curves from 20 bins, spikes over occupancy, smoothed with rlowess over 7\n    bins, on the visualizing ranges (Methods, Raw tuning curves); Pearson correlation with the\n    model-derived curve resampled to the same 20 bins (the resampling is not stated; a standard\n    choice). Reproduced when at least six of seven medians are within tolerance.\n- id: supp7e-eye-velocity-extrema-near-zero\n  statement: Peaks and valleys of nonlinear eye velocity tuning curves lie mostly near 0 (170 of\n    224 horizontal, 82 of 138 vertical within half the range), although their medians differ\n    from 0.\n  source: Supplementary Figure 7e\n  quote: Distribution of peaks/valleys for horizontal eye velocity (top) and vertical eye velocity\n    (bottom) tuning curves are centered on 0 eye position units/sec\n  statistics:\n  - about: horizontal, within against outside half range\n    test: binomial test\n    statistic: Z = 7.68\n    p: 1.0e-8\n    n: 224 peaks or valleys\n  - about: vertical, within against outside half range\n    test: binomial test\n    statistic: Z = 2.13\n    p: 0.03\n    n: 138 peaks or valleys\n  - about: horizontal median against 0\n    test: two-sided Wilcoxon signed rank test\n    statistic: Z = 2.63\n    p: 0.0080\n  - about: vertical median against 0\n    test: two-sided Wilcoxon signed rank test\n    statistic: Z = 3.34\n    p: 8.0e-4\n  depends_on:\n  - fig6-eye-velocity-nonlinear-temporal\n  expected:\n  - quantity: horizontal peaks or valleys within half range\n    value: 170\n    tolerance: 17\n  - quantity: vertical peaks or valleys within half range\n    value: 82\n    tolerance: 8.2\n  criterion: As fig2c-velocity-extrema-near-zero, the half range being halfway between 0 and the\n    maximum or minimum velocity of the range. Reproduced when both binomial tests give P < 0.05\n    with a majority within half range and both counts are within tolerance.\n- id: supp9-correlation-contributions\n  statement: Measured by correlation coefficients, contributions follow the same order; in freely\n    moving mice body position contributes most (median 0.42) and azimuthal head velocity least\n    (0.02), and in head-fixed mice body position and speed exceed the eye variables.\n  source: Supplementary Figure 9\n  quote: We report the contribution of each variable to the correlation coefficient between a\n    cell’s smoothed spiketrain and the model-predicted firing rate\n  statistics:\n  - about: freely moving, six variables\n    test: Kruskal-Wallis test\n    statistic: chi2 = 488.5, df = 5\n    p: 2.4e-103\n  - about: head-fixed, six variables\n    test: Kruskal-Wallis test\n    statistic: chi2 = 1.4e3, df = 5\n    p: 5.4e-292\n  depends_on:\n  - fig3ab-head-contributions\n  - fig7ab-eye-contributions\n  expected:\n  - quantity: freely moving median contribution, B\n    value: 0.42\n    tolerance: 0.042\n  - quantity: freely moving median contribution, Ha\n    value: 0.17\n    tolerance: 0.017\n  - quantity: head-fixed median contribution, B\n    value: 0.38\n    tolerance: 0.038\n  - quantity: head-fixed median contribution, Bs\n    value: 0.13\n    tolerance: 0.013\n  criterion: Contribution as in fig3ab-head-contributions with the Pearson correlation of the\n    spike train smoothed by gausswin over 20 bins and the model rate as performance (Methods,\n    Computing contribution to model performance). Reproduced when both Kruskal-Wallis tests give\n    P < 0.05, B is the largest contributor in both datasets, azimuthal head velocity the smallest\n    in the freely moving one, B and Bs exceed every eye variable, and at least three of the four\n    medians are within tolerance.\n- id: supp12-no-false-eye-detection\n  statement: Eye variables share information with body position and speed, yet when eye-related\n    contributions are deleted from simulated spike trains, the LN model does not falsely detect\n    eye tuning.\n  source: Supplementary Figure 12e to g\n  quote: Note that eye variables were not falsely detected.\n  depends_on:\n  - fig4j-eye-encoding-cells\n  criterion: As in the Methods (Generating simulated data without eye-encoded information),\n    spike trains are drawn from each cell's fitted model with eye terms removed and the LN\n    pipeline rerun. Mutual information between each eye variable and B or Bs against 100\n    shuffles (legend). Reproduced when the data mutual information exceeds all shuffles in most\n    sessions and, for each eye variable, the cells detected in the simulated data are at most 10%\n    of those in the original (a reading of \"not falsely detected\"; the Supplementary Fig. 3c\n    false positive rates reach this level).\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/mallory-2021.yaml paper/10.1038-s41467-021-20936-8.txt; grep -n "—\|rather" claims/mallory-2021.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/quote: This effect was observed even in cells that jointly encode body position and eye position/quote: This effect was observed even in cells that jointly encoded body position and eye position/' claims/mallory-2021.yaml && python tools/claims_check.py claims/mallory-2021.yaml paper/10.1038-s41467-021-20936-8.txt; grep -o "3.3.23\|P = 2.0e.7\|P = 8.0e.4" paper/*.txt; python3 -c "
import yaml;d=yaml.safe_load(open('claims/mallory-2021.yaml'))
import re
for c in d['claims']:
  for k,v in c.items():
    if isinstance(v,str) and ': ' in v: print(c['id'],k)
print(sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']), sum('expected' in c for c in d['claims']))"
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/mallory-2021.yaml` and did not commit it. The quote checker passes every quote. It still flags two p-values, which I confirmed by reading: P = 2.0e-7 and P = 8.0e-4 in the Supplementary Fig. 7 legend. The checker does not recognise the trailing ".0" in how they are printed.

**Text read**
- **Paper:** the version of record (Europe PMC full text, PMC7844029), with Methods and figure legends.
- **Supplement:** the three PMC supplementary files. These are the Supplementary Information (legends of Supplementary Figs. 1 to 12), the peer review file (only an editorial note) and the reporting summary.
- **PDFs:** not opened. No claim needed a number that appears only inside a figure.
- **Code:** `khardcastle/spline-lnp-model` at commit 34b470f is the spline LN model with forward search. `GiocomoLab/ln-model-of-mec-neurons` at commit 643386b is the older 2017 model; I read it and did not follow it. Neither repository holds the pitch, roll or eye analyses, tuning-curve shapes, stability or PCA clustering, so those methods come from the Methods and legends. Where the code differs from the Methods (3-s fold sections, position bins of box × 10/100, 12 head-direction points), I followed the Methods and recorded the code's settings as variants.

**Claims:** 42 in all, every one with a quote. 23 have statistics (53 values), 33 have expected values with tolerances, and all 42 have a criterion. All are `data: dataset`.

**Details the paper leaves open, with the readings named for each:**
1. **How the cross-validation folds are built** ("10-s sections"): consecutive sections assigned to folds in turn, or assigned at random. The code's 3-s sections are a variant.
2. **Restricting behaviour to its inner 95% or 98%:** keep only time bins where every variable is in range, or clip each variable separately.
3. **Contribution to model performance:** (full − reduced) / full, which gives the paper's ranking with body position strongest; or 1 minus that, which is the literal wording. Performance is the mean over the 10 folds, or a single held-out section as in the code.
4. **"Explored" range for classifying tuning-curve shape:** the share of the preset range covered between the behavioural percentiles, or the share of bins with any occupancy.
5. **A cell's preferred direction:** slope sign for linear cells and the side of the curve's maximum for the rest, or the side with the larger slope.
6. **Asymmetric versus symmetric velocity cells:** the two slopes have opposite signs, or the rule from the Methods' shuffle comparison.
7. **Tuning curves compared across the tracks with and without landmarks:** model-derived curves refitted on each track, or raw curves.
8. **One P printed for several pairs:** read as the largest P of those pairs.

**Choices I made, where the paper's wording forced one:**
- Eye units for the preset bounds are fixed as % of eye width. A fraction of eye width would put the bounds beyond the eye.
- "P = 3.3–23" and "P = 1.9–20" are read as 3.3e-23 and 1.9e-20.
- The 52 body-speed cells in the azimuthal head velocity stability comparison are read as the Cohort 1 body-speed cells, the count Supplementary Fig. 3b gives.
- The spline tension is set to 0.5, the code's value; the Methods allow 0.5 to 0.7, and 0.7 is run as a variant.

**Missing from the paper for some claims:**
- **Fig. 8e** (eye tuning preserved in cells that encode both body and eye position) has examples only and no test. Its criterion uses a signed-rank test chosen here and is marked as resting on that assumption.
- **Smaller unstated settings:** the number of label scrambles for the clustering tests (1000 used, a standard choice), the pairwise alpha for the eye-stability comparisons (0.0167 used, as in the Fig. 5 legends), and the resampling for model-versus-raw tuning-curve correlations.
- **The no-landmark sessions** (Fig. 8, 6 sessions in 6 mice): the paper does not say whether they are among the 11 main head-fixed recordings.
- **Cohort 2** includes recordings from three earlier papers and has no head-tilt sensor (IMU). The raw data are said to be on figshare. Whether DANDI:000053 holds Cohort 2 and the no-landmark sessions is for the author to check.

## End of run

26 turns, 6 minutes, $2.38 at API prices, result: success.
