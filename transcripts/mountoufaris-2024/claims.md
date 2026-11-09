# 001131 · claims · run 39834080406

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/001131 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 25,140p claims/001453/*.yaml; echo ----; grep -n "^- id\|^  [a-z_]*:" claims/001453/*.yaml | awk '{print $2}' | sort | uniq -c; tail -60 claims/001453/*.yaml
```

```
# pmc.ncbi.nlm.nih.gov).
schema_version: 2
dataset:
  archive: dandi
  id: "001453"
paper: doi:10.1016/j.cub.2025.04.027
claims:
- id: stimulus-code-link
  kind: link
  statement: The dandiset's stimulus codes can be linked to the stimuli the paper names, using
    the paper's analysis code and the protocol file of its stimulus software, and the values
    computed through that link agree with those the paper's code printed.
  source: Data and Code Availability; the paper's Fig1-S1.ipynb at GitLab commit 33a5c29
  data: with_labels
  criterion: Records are matched by the integer stimulus code. The link holds (reproduced) when
    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the
    species' median speeds for the nine whole-field stimuli computed here are within 10% of the
    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is
    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be
    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; head -30 paper/*.txt; cat tools/claims_check.py | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.cell.2024.08.015.txt",
 "offset": 7,
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)}' *.txt | awk -F': ' '$2>3000'; grep -n "^Supplement\|^=====\|^---" *.txt | head
```

```
7: 122977
6:------------------------------------------------------------------------
```

**Agent calls Bash**

```bash
cd  sed -n 7p paper/*.txt | fold -s -w 2000 > $TMPDIR/main.txt; wc -l $TMPDIR/main.txt; echo $TMPDIR; sed -n 8,30p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "Supplement\|SUPPLEMENT\|supp" paper/*.txt | head; grep -n "^\[1[0-9][0-9]\]" paper/*.txt | tail -2
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "limit": 20
}
```

```
1	pmc Cell Cell 319 nihpa 0413066 Cell 0092-8674 1097-4172 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC11490375 PMC11490375.1 11490375 11490375 NIHMS2020595 39191257 10.1016/j.cell.2024.08.015 NIHMS2020595 NIHPA2020595 1 Article A LINE ATTRACTOR ENCODING A PERSISTENT INTERNAL STATE REQUIRES NEUROPEPTIDE SIGNALING Mountoufaris George 1 3 Nair Aditya 1 2 3 Yang Bin 5 Kim Dong-Wook 6 Vinograd Amit 1 3 Kim Sam 1 3 Linderman Scott W. 7 8 Anderson David J. 1 3 4 * 1 Division of Biology and Biological Engineering, California Institute of Technology, Pasadena, CA 91001 2 Program in Computation and Neural Systems, California Institute of Technology, Pasadena, CA 91001 3 Tianqiao and Chrissy Chen Institute for Neuroscience, California Institute of Technology, Pasadena, CA 91001 4 Howard Hughes Medical Institute, Pasadena, CA 91001 5 Present address: Johns Hopkins University School of Medicine 6 Present address: Allen Institute for Brain Science 7 Department of Statistics, Stanford University, Stanford, CA 94305, USA 8 Wu Tsai Neurosciences Institute, Stanford University, Stanford, CA 94305, USA AUTHOR CONTRIBUTIONS G.M and D.J.A conceived the project. G.M and D.J.A. wrote and prepared the manuscript, with input from A.N. G.M performed all the experiments, with the occasional help from B.Y for the miniscope imaging or D.K and S.K. with the two-photon slice imaging. A.V. helped with the revision. G.M and A.N performed quantitative measurements of behavior and microendoscope imaging data. A.N., under the supervision of S.W.L. performed the dynamical system modeling and decoder analyses. * Lead contact: [removed: an e-mail address] , [removed: an e-mail address] 17 10 2024 26 8 2024 187 21 473130 5998 6015.e18 05 09 2024 17 10 2025 17 10 2025 21 10 2024 18 10 2025 This file is available for text mining. It may also be used consistent with the principles of fair use under the copyright law. Neuropeptide Signaling is Required to Implement a Line Attractor Encoding a 
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 21,
 "limit": 21
}
```

```
21	male-female interactions. These female-tuned units are largely distinct from the units active during male-male interactions 66 , 82 . Consistent with this, a line attractor observed during male mounting of females 21 was not perturbed by co-editing of Oxtr and Avpr1a and there was no deficit in male-female mating behavior. Together, these data argue that the effect of the Oxtr/Avpr1a perturbation on neural dynamics is unlikely due to indiscriminate changes in VMH cytoarchitecture or function. A line attractor dependent on neuropeptide signaling Most theoretical studies of attractor dynamics to date have assumed that they reflect recurrent fast synaptic connectivity 17 – 19 , as seen in the Drosophila ring attractor system 24 , 29 . Our finding that neuropeptide signaling is required for line attractor dynamics and persistent activity is consistent with recurrent neural network (RNN) modeling of persistent activity in VMH circuits, which indicated that only models incorporating both recurrence and slow neuromodulation were accounted for the experimental observervations 12 , 65 . OXT can cause increased excitability in anterior VMHvl neurons 91 ; it could also strengthen recurrent connectivity within this nucleus 12 , 92 or between interconnected regions 93 . We note, however, that neither OXT nor AVP are synthesized by VMHvl Esr1 neurons; therefore, their source(s) must be extrinsic to this nucleus 91 . A role for neuropeptides in implementing slow attractor dynamics that control innate behaviors is appealing for several reasons. First, it it may overcome the dependence of purely glutamatergic attractor networks on fine-tuned synaptic connectivity 17 , 18 , 27 . This requirement for fine-tuning makes attractors very “fragile”, i.e., highly sensitive to experimental or physiological disruption (but see 94 , 95 ). RNN modeling has indicated that VMHvl networks incorporating slow neuromodulatory transmission can reproduce observed network time-constants over a much 

[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 42,
 "limit": 21
}
```

```
42	was performed, corrected with Dunn’s multiple comparison during time points 0s-1000s. *p≤0.05 **p≤0.01 ***p≤0.001 ACKNOWLEDGEMENTS We thank H. Inagaki, A. Kennedy, B. Weissbourd, M. Schnitzer for comments on this manuscript, C. Chiu for laboratory management, G. Mancuso and L. Chavarria for administrative assistance, and members of the Anderson lab for helpful comments on this project. We also thank Y. Li, L. Geng and H. Wang for sharing their OXT-GRAB sensor in advance of publication. G.M. has been supported by post-doctoral fellowships from the Tianqio and Chrissy Chen Institute for Neuroscience, the Helen Hay Whitney Foundation and the Della Martin Foundation. A.N. is supported by a National Science Scholarship from the Agency of Science, Technology and Research, Singapore. This work was supported in part by NIH grants NS123916, MH1223612, and MH070053. D.J.A. is an Investigator of the Howard Hughes Medical Institute. The content of this paper is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health. We support inclusive, diverse, and equitable conduct of research. We acknowledge that this research was conducted at Caltech, which is located on the unceded land of the Indigenous Tongva people. This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain. DECLARATION OF INTERESTS The authors declare no competing interests. REFERENCES 1. Sternson SM ( 2013 ). Hypothalamic survival circuits: blueprints for purposive behaviors . Neuron 77 , 810 – 824 . 10.1016/j.neuron.2013.02.018 . 23473313 

[... 20 more lines not kept]
```

**Agent**

Main text and STAR Methods read (PMC author manuscript, with supplementary figure legends inline). Now checking the rest of the text file and the supplement PDF.

**Agent calls Bash**

```bash
cd  awk 'NR>7 && length($0)>0 && $0 !~ /^\[[0-9]+\]/' paper/*.txt | cut -c1-200 | head -80; python -c "import fitz" 2>&1; python - <<'E'
import fitz
d=fitz.open('paper/10.1016-j.cell.2024.08.015.supp.pdf'); print(d.page_count)
for p in d: print(p.get_text()[:600]); print('=====')
E
```

Result: not kept, because it reads the paper's text.

**Agent**

The supplement is figure pages only; its legends are in the main text, so the full text is complete. Next, the linked code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/DJALab/VMHvl_MPOA_dynamics 2>&1 | tail -2; cd VMHvl_MPOA_dynamics && git log -1 --format='%H %ci' && find . -type f -not -path './.git/*' | head -50
```

```
ed83c418aa0e4dab9389ef6c4464d626752e3ea3 2023-11-28 13:19:13 -0800
./code/Fig3_flowfield_3d_landscape_visualization.ipynb
./README.md
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/VMHvl_MPOA_dynamics; cat README.md; python3 -c "
import json;nb=json.load(open('code/Fig3_flowfield_3d_landscape_visualization.ipynb'))
for c in nb['cells']: print('---',c['cell_type']); print(''.join(c['source']))
"
```

```
# Dynamical systems analysis in VMHvl and MPOA

This is a repository of code for analyses of fit dynamical systems and to generate figures associated with the paper "An approximate line attractor in the hypothalamus that encodes an aggressive internal state" by Nair et al.

For questions about the code, please contact adi.nair AT caltech DOT edu.
For general questions about the paper, contact wuwei AT caltech DOT edu or ann.kennedy AT northwestern DOT edu

Code and notebooks for fitting models is available in the Linderman lab's repository at: https://github.com/lindermanlab/ssm/blob/master/notebooks/4-Recurrent-SLDS.ipynb
--- markdown
#### Generating flow fields and dynamic velocity landscapes using fit dynamical systems
Aditya Nair, 2022, Caltech

The following code can reproduce panels from Fig 3 of Nair et al., and provides functions and code to generate flow fields and 3d landscapes from low dimensional dynamical systems
--- code
## Helper Functions 

import autograd.numpy as np
import autograd.numpy.random as npr
npr.seed(0)

[... 186 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q --depth 1 https://github.com/lindermanlab/ssm 2>&1|tail -1; cd ssm && git log -1 --format='%H %ci'; python3 -c "
import json;nb=json.load(open('notebooks/4-Recurrent-SLDS.ipynb'))
for c in nb['cells']:
  s=''.join(c['source'])
  if 'fit(' in s or 'SLDS(' in s: print(s); print('---')
"
```

```
eb6c8aa33e5311d3564075807dec340759dd8081 2025-05-09 09:43:13 -0700
# Simulate the "nascar" data
def make_nascar_model():
    As = [random_rotation(D_latent, np.pi/24.),
      random_rotation(D_latent, np.pi/48.)]

    # Set the center points for each system
    centers = [np.array([+2.0, 0.]),
           np.array([-2.0, 0.])]
    bs = [-(A - np.eye(D_latent)).dot(center) for A, center in zip(As, centers)]

    # Add a "right" state
    As.append(np.eye(D_latent))
    bs.append(np.array([+0.1, 0.]))

    # Add a "right" state
    As.append(np.eye(D_latent))
    bs.append(np.array([-0.25, 0.]))

    # Construct multinomial regression to divvy up the space
[... 131 more lines not kept]
```

**Agent**

Code read: the DJALab repo holds only a synthetic flow-field demo; ssm is the general library. Now the dataset's title and description from the archive.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001131/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(json.dumps({k:d.get(k) for k in ['identifier','created','draft_version','most_recent_published_version']},indent=1))"; curl -s https://api.dandiarchive.org/api/dandisets/001131/versions/draft/info/ | python3 -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m['name']);print(m.get('description'));print(m.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
which pdftotext pdftoppm mutool; python3 -c "import pypdf" 2>&1; python3 -c "import pdfplumber" 2>&1
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent calls Bash**

```bash
cd  grep -n "=== page" paper/*.txt; n=$(grep -n "=== page 6 ===" paper/*.txt | cut -d: -f1); sed -n "$n,\$p" paper/*.txt | tr '\n' '|' | cut -c1-6000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,200p tools/claims_check.py
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

I have what I need: full text with Methods and supplementary legends, and the linked code (a flow-field demo plus the ssm library). Writing the claims file now.

**Agent calls Bash**

```bash
cd $TMPDIR/ssm; git log -1 --format=%H; grep -n "def most_likely\|single_subspace" ssm/lds.py | head -5
```

```
eb6c8aa33e5311d3564075807dec340759dd8081
40:                 single_subspace=True,
135:                single_subspace=single_subspace, **emission_kwargs)
281:    def most_likely_states(self, variational_mean, data, input=None, mask=None, tag=None):
418:            if not self.emissions.single_subspace:
901:                single_subspace=True, **emission_kwargs)
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "claims/001131/10.1016-j.cell.2024.08.015.yaml",
 "content": "# Claims for Mountoufaris, Nair, Yang, Kim, Vinograd, Kim, Linderman & Anderson (2024), Cell 187,\n# 5998-6015, on dandiset 001131.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, under\n# docs/protocol.md version pilot-10.\n#\n# Source: the accepted author manuscript in PubMed Central (PMC11490375, NIHMS2020595), full text\n# as served by PMC: Results, Discussion, STAR Methods, main and supplementary figure legends. The\n# supplement (NIHMS2020595-supplement-1.pdf) holds the images of Figures S1 to S7 only; their\n# legends are in the main text. The version of record was not read. The main figures are not in\n# the files read, so the star level of each main-figure panel could not be read; where the text\n# says \"significantly\" and the panel's stars are not readable, the statistics record p < 0.05,\n# the paper's lowest level (\"* P < 0.05\", STAR Methods, Statistical analysis). Stars read from the\n# supplement images are recorded as read.\n#\n# Code read. The paper links https://github.com/DJALab/VMHvl_MPOA_dynamics (commit ed83c41,\n# 2023-11-28) and https://github.com/lindermanlab/ssm (commit eb6c8aa, 2025-05-09). The DJALab\n# repository holds one notebook that draws flow fields and dynamic velocity landscapes for two\n# synthetic 2-dimensional linear systems (from Nair et al. 2023, Fig 3); it holds no code for this\n# paper's data. Its README points to ssm's notebooks/4-Recurrent-SLDS.ipynb for fitting, which\n# fits an rSLDS with ssm.SLDS(transitions=\"recurrent_only\", dynamics=\"diagonal_gaussian\",\n# emissions=\"gaussian_orthog\", single_subspace=True), method=\"laplace_em\",\n# variational_posterior=\"structured_meanfield\", num_iters=100. These are the code's settings for\n# the rSLDS claims where the Methods are silent. No code is given for activity measures,\n# selectivity, choice probability, decoders or ACHW.\n#\n# Data the paper used, as it reports them.\n# - Miniscope imaging (\"CRISPRoscopy\", Figures 4 to 7, S4 to S7A-B). Esr1-Cre males, socially and\n#   sexually experienced, injected unilaterally in VMHvl with a Cre-dependent Cas9 AAV and a\n#   Cre-dependent AAV carrying four gRNAs against Oxtr and Avpr1a (experimental, \"OARs gRNAs\") or\n#   scrambled gRNA (control, \"Scr gRNAs\"), both with GCaMP8s. STAR Methods give 585 units from 5\n#   control mice and 546 units from 7 experimental mice. The Results say \"n=4 control and n=7\n#   experimental\" for Figure 4E-F, while the Figure 4 and S4 legends say n=5 control; the rSLDS\n#   analyses use mice with at least 31 units, n=4 control and n=7 experimental (male intruders)\n#   and n=4 control and n=6 experimental (female intruders). Sessions lasted about 1 h, 20-25 min\n#   per intruder sex; a male intruder came first and a female second, on the same day during\n#   CRISPRoscopy, after a 5-min baseline alone in the home cage. Imaging at 30 Hz, motion\n#   corrected, temporally downsampled to 10 Hz; units extracted and deconvolved with CNMF-E.\n#   Traces were z-scored, or expressed in units of sigma relative to the pre-intruder baseline\n#   (\"during 7sec or more\" before the first trial). Behavior video at 30 Hz, annotated\n#   frame by frame (MARS classifier, corrected by hand) for sniff, attack and mount towards male\n#   or female intruders; Figure 6 also names dominance mounting of males.\n# - Behavior of separate cohorts (Figures 2 and 3, S2, S3): bilateral LV gRNA plus Cas9 AAV in\n#   wild-type C57BL/6N males (n=11 per group), and bilateral Cre-dependent AAVs in Esr1-Cre males\n#   (n=16 control, 13 experimental with males; 15 and 13 with females); 15-20 min of male-male and\n#   10 min of male-female interaction scored.\n# - Fiber photometry (Figure 3E-H, S3E-F), n=5 mice per group with males.\n# - Two-photon imaging of acute VMH slices perfused with OXT and AVP (Figures 1F, 2E, S1F-G, S3B,\n#   S7C-L), at about 1.2 Hz.\n# - Single-cell RNA-seq of VMHvl from an outside atlas (Kim et al. 2019, doi:10.1016/j.cell.2019.09.020)\n#   for Figure 1B-E.\n# The dandiset's description says it holds \"GCaMP traces, behavioural annotation (timing of\n# behaviour) and other metadata\"; which of the experiments above it holds is the author's to find.\n#\n# Details the paper leaves open, used by several claims (each claim's criterion names its own).\n# - \"Nested\" Mann-Whitney and \"nested\" Kolmogorov-Smirnov tests are not defined. Readings (a) the\n#   test on all units pooled across mice; (b) Mann-Whitney on per-mouse means (for KS claims, on\n#   per-mouse medians).\n# - Activity in units of sigma: (activity minus the mean of the pre-intruder baseline) divided by\n#   the baseline standard deviation, per unit (STAR Methods, Micro-endoscopic data extraction).\n#   The baseline is \"during 7sec or more\" before the first trial. Readings (a) the whole\n#   pre-intruder period of the session; (b) the 7 s before the first intruder enters.\n# - Which mice: readings (a) all 5 control and 7 experimental mice; (b) the 4 control mice named\n#   in the Results for Figure 4E-F, if the dataset marks which control mouse is left out.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001131\"\npaper: doi:10.1016/j.cell.2024.08.015\nclaims:\n- id: fig1e-oxtr-avpr1a-coexpression\n  statement: About 78% of Esr1+ VMHvl cells express Oxtr mRNA, and about 61% of these also express\n    Avpr1a mRNA, in a single-cell RNA-seq atlas of VMHvl.\n  source: Results, Most Esr1+ neurons co-express Oxytocin and Vasopressin receptors, paragraph 1;\n    Figure 1E\n  quote: Overall, ~78% of Esr1 + cells in VMHvl expressed Oxtr mRNA, and ~61% of these cells also\n    expressed Avpr1a mRNAs\n  data: with_inputs\n  expected:\n  - quantity: fraction of Esr1+ VMHvl cells expressing Oxtr\n    value: 78\n    tolerance: 7.8\n    unit: percent\n  - quantity: fraction of Oxtr+ Esr1+ cells also expressing Avpr1a\n    value: 61\n    tolerance: 6.1\n    unit: percent\n  criterion: Uses the outside atlas of Kim et al. 2019 (doi:10.1016/j.cell.2019.09.020), analysed\n    \"as described previously\" (STAR Methods, Transcriptomic analysis); the expression threshold\n    is not given. Reproduced when both fractions are within tolerance.\n- id: fig1f-peptides-activate-slices\n  statement: Bath application of OXT plus AVP (400 nM each), or of either peptide alone, evokes\n    strong calcium responses (dF/F about 500-600%) in VMHvl Esr1 neurons in acute slices.\n  source: Results, Most Esr1+ neurons co-express Oxytocin and Vasopressin receptors, paragraph 2;\n    Figure 1F, S1F-G\n  quote: Perfusing a mixture of 400nM (each) OXT plus AVP or individually administering these\n    peptides elicited strong (ΔF/F ~500–600%) responses in VMHvl Esr1 cells\n  statistics:\n  - about: responses to OXT plus AVP\n    test: Mann-Whitney test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 124 cells from 4 mice\n  expected:\n    quantity: peak dF/F of Esr1 cells to OXT plus AVP\n    value: 550\n    tolerance: 105\n    unit: percent\n  criterion: The paper reports a range, 500 to 600%; the claim holds inside the range widened by\n    10% of each bound (450 to 660%), for the mean response of the 124 cells of Figure 1F. Which\n    measure of the response (peak of the mean trace, or mean of per-cell peaks) is not given;\n    either reading counts.\n- id: fig2e-editing-reduces-slice-responses\n  statement: In slices from mice with Cre-dependent Oxtr/Avpr1a gRNAs, the fraction of\n    GCaMP8s-expressing cells responsive to OXT plus AVP is reduced from 42.6 +/- 3% (scrambled\n    gRNA) to 13 +/- 3.3%.\n  source: Results, Altered VMHvl Esr1 neural activity during social interactions, paragraph 1;\n    Figure 2E\n  quote: The fraction of GCaMP8s-expressing cells responsive to mixed AVP and OXT peptides was\n    reduced from 42.6± 3% in Scr gRNAs controls to 13± 3.3% (~70% reduction) in Oxtr/Avpr1a gRNAs\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.01\n    p_relation: \"<\"\n    n: brain slices from 2 control and 3 experimental mice\n  expected:\n  - quantity: responsive fraction, control slices\n    value: 42.6\n    tolerance: 3\n    unit: percent\n  - quantity: responsive fraction, experimental slices\n    value: 13\n    tolerance: 3.3\n    unit: percent\n  criterion: The criterion for a responsive cell is not given in the Methods. Reproduced when both\n    fractions are within tolerance (the paper's stated spread) and the Mann-Whitney test across\n    slices gives p < 0.01, the level printed in the Figure 2 legend.\n- id: fig2g-bilateral-editing-reduces-aggression\n  statement: Bilateral co-editing of Oxtr and Avpr1a in VMH (LV gRNAs plus Cas9 AAV) reduces\n    attack towards male intruders (number, probability, total time and bout duration of attacks)\n    and lengthens the latency to the first attack.\n  source: Results, Oxtr/Avpr1a-mediated neuropeptidergic signaling in VMH is required for male\n    territorial aggression, paragraph 3; Figure 2G, S2B-C\n  quote: Experimental mice displayed a notable reduction in aggression towards male intruders, as\n    evidenced by significant decreases in the number and time-varying probability of attack bouts,\n    the total time spent attacking and the average duration of each attack bout; in addition, the\n    latency to the 1st attack bout was significantly increased\n  statistics:\n  - test: Mann-Whitney test (nested Mann-Whitney in S2)\n    p: 0.05\n    p_relation: \"<\"\n    n: 11 mice per group\n  criterion: Per mouse, over the first 15 min of the male-male assay (STAR Methods, Behavior\n    annotations), the number of attack bouts, total attack time, mean attack bout duration and\n    latency to the first attack, compared between groups with a Mann-Whitney test. Reproduced\n    when each measure differs in the stated direction with p < 0.05; partially reproduced when\n    some do.\n- id: fig2-bilateral-editing-spares-sniff-and-mating\n  statement: Bilateral co-editing does not change time spent sniffing male intruders, nor\n    sniffing or mounting of female intruders.\n  source: Results, Oxtr/Avpr1a-mediated neuropeptidergic signaling in VMH is required for male\n    territorial aggression, paragraph 3; Figure 2G-H, S2D\n  quote: the time spent in close investigation (sniffing) of male intruders did not differ\n    significantly between experimental and control male residents ... Experimental males also did\n    not differ significantly from controls in their sniffing or mounting behavior towards female\n    intruders\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.05\n    p_relation: \">\"\n    n: 11 mice per group\n  criterion: A claim of absence, judged on the paper's test, the Mann-Whitney test between groups\n    per mouse (n=11 each) on male-directed sniff time, female-directed sniff time and the mounting\n    measures of S2D. Reproduced when none gives p < 0.05; the effect sizes are reported either way.\n- id: fig3c-cre-editing-reduces-aggression\n  statement: Bilateral Cre-dependent co-editing in VMHvl Esr1 neurons reduces most measures of\n    aggression towards males, less strongly than the constitutive system, while sniffing duration\n    is unaffected.\n  source: Results, Altered VMHvl Esr1 neural activity during social interactions, paragraph 2;\n    Figure 3C, S3C\n  quote: Bilateral co-disruption of Oxtr/Avpr1a in VMHvl Esr1 neurons significantly reduced most\n    metrics of aggression towards male intruder compared to control mice, although to a somewhat\n    lower extent than observed with the Cre-independent system\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.05\n    p_relation: \"<\"\n    n: 16 control and 13 experimental mice\n  criterion: Per mouse, over 15-20 min of male-male interaction, the attack measures of Figure 3C\n    and S3C (percent attacking, attack bout duration, latency, inter-bout interval, number and\n    probability of attack bouts) and sniff duration, Mann-Whitney between groups. Reproduced when\n    more than half of the attack measures are significantly lower (or latency longer) at p < 0.05\n    and sniff duration is not significantly different.\n- id: fig3fh-photometry-reduced\n  statement: Bulk calcium activity of VMHvl Esr1 neurons during male-directed sniffing and attack\n    is reduced in mice with bilateral Cre-dependent co-editing.\n  source: Results, Altered VMHvl Esr1 neural activity during social interactions, paragraph 2;\n    Figure 3E-H\n  quote: we observed a significant reduction in overall VMHvl Esr1 neuronal activity during the\n    infrequent attack bouts exhibited by experimental mice ... A reduction in VMHvl Esr1 activity\n    during sniffing episodes was also observed in these mice\n  statistics:\n  - test: Mann-Whitney test, AUC and peak of the behavior-triggered average\n    p: 0.05\n    p_relation: \"<\"\n    n: 5 mice per group; data points are bouts\n  criterion: From the STAR Methods (Fiberphotometry recordings and analysis), the 470 nm signal\n    corrected by a least-squares fit of the 405 nm signal, dF/F = (F470 - F405)/F405, normalized\n    to a 2-s pre-bout baseline (mean and SD); AUC and peak over 10 s after bout onset, per bout;\n    for sniffing, the first 1 min of sniffing after intruder entry. Mann-Whitney on bouts between\n    groups. Reproduced when AUC and peak are lower in experimental mice at p < 0.05 for both\n    sniffing and attack.\n- id: figs3ef-photometry-female-unchanged\n  statement: During interactions with females, bulk calcium activity during sniffing and mounting\n    does not differ between experimental and control males.\n  source: Results, Altered VMHvl Esr1 neural activity during social interactions, paragraph 2;\n    Figure S3E-F\n  quote: during male-female interactions, calcium signals in experimental males were not\n    significantly different from controls\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.05\n    p_relation: \">\"\n    n: 4 control and 5 experimental mice (sniffing), 3 and 4 (mounting)\n  criterion: A claim of absence, judged on the paper's test, Mann-Whitney between groups on the\n    AUC of the z-scored behavior-triggered average for female-directed sniffing (1 min) and\n    mounting, computed as in fig3fh-photometry-reduced. Reproduced when neither gives p < 0.05.\n- id: figs4a-unilateral-no-behavior-deficit\n  statement: Mice with unilateral editing and imaging (the CRISPRoscopy mice) show no deficit in\n    sniffing or aggression compared with controls.\n  source: Results, Single cell CRISPRoscopy imaging, paragraph 1; Figure S4A\n  quote: Indeed, unilateral injected experimental animals displayed no deficits in sniffing or\n    aggression compared to controls\n  statistics:\n  - test: not named in the S4 legend for panel A\n    p: 0.05\n    p_relation: \">\"\n    n: 5 control and 7 experimental mice\n  criterion: A claim of absence. The S4 legend names no test for panel A; the paper's test for the\n    same measures in Figures 2, 3 and S3 is the Mann-Whitney test, used here. Per mouse, total\n    sniff time, sniff bout duration, total attack time, attack bout duration, latency to first\n    attack, inter-attack interval and attack probability, during the male-intruder period.\n    Reproduced when none differs at p < 0.05.\n- id: methods-unit-counts\n  statement: CRISPRoscopy recorded 585 units from 5 control mice and 546 units from 7 experimental\n    mice.\n  source: STAR Methods, Micro-endoscopic data extraction, last sentence\n  quote: A total of 585 units (n=5 mice) from control and 546 units (n=7 mice) from experimental\n    mice were recorded\n  expected:\n  - quantity: control units\n    value: 585\n    tolerance: 0\n  - quantity: experimental units\n    value: 546\n    tolerance: 0\n  - quantity: control mice\n    value: 5\n    tolerance: 0\n  - quantity: experimental mice\n    value: 7\n    tolerance: 0\n  criterion: Counts are exact; tolerance 0 because they are counts of recorded units and mice, not\n    measurements. A difference is reported per mouse.\n- id: fig4ef-male-activity-slightly-lower\n  statement: During interactions with a male intruder, the activity of all VMHvl Esr1 units\n    (sigma above pre-intruder baseline, and z-scored) is slightly but significantly lower in\n    experimental than in control mice.\n  source: Results, Effect of Oxtr/Avpr1a co-editing on VMHvl Esr1 activity and intruder sex\n    representations, paragraph 1; Figure 4Ei, 4Fi, S4Di\n  quote: During interactions with a male intruder, the experimental cumulative distribution\n    function (ECDF) and mean activity of all units (pooled from n=4 control and n=7 experimental\n    animals) were slightly but significantly decreased in experimental mice\n  statistics:\n  - about: mean activity (Figure 4E)\n    test: nested Mann-Whitney test\n    p: 0.05\n    p_relation: \"<\"\n  - about: cumulative distributions (Figure 4F, S4D)\n    test: Kolmogorov-Smirnov test (nested in S4D)\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Per unit, the mean activity in units of sigma above the pre-intruder baseline over\n    the first part of the first male interaction, and the same for z-scored traces (z relative to\n    the cell's mean over the whole recording). The window is open; the Results say \"the first two\n    minutes\" and the Figure 4E-F legend \"1 minute of interaction\" (S4D also 1 min); readings 1 min\n    and 2 min. Tests as named, under the file-level readings of \"nested\" and of the baseline.\n    Reproduced when, under a reading, experimental activity is lower than control at p < 0.05 by\n    both the Mann-Whitney and the KS test for sigma-normalized activity.\n- id: fig4ef-female-activity-unchanged\n  statement: During interactions with females, activity in units of sigma above baseline does not\n    differ between experimental and control mice, while z-scored activity is slightly but\n    significantly higher in experimental mice.\n  source: Results, Effect of Oxtr/Avpr1a co-editing on VMHvl Esr1 activity and intruder sex\n    representations, paragraph 1; Figure 4Eii, 4Fii, S4Dii\n  quote: During interactions with females there was no significant difference in activity (measured\n    in σ above baseline) between experimental and control animals ... although z-scored activity\n    showed a slight but significant increase\n  statistics:\n  - about: sigma-normalized activity\n    test: nested Mann-Whitney and Kolmogorov-Smirnov tests\n    p: 0.05\n    p_relation: \">\"\n  - about: z-scored activity\n    test: nested Kolmogorov-Smirnov test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: As in fig4ef-male-activity-slightly-lower, for the first female interaction. The\n    absence part is judged on the paper's tests (Mann-Whitney on mean activity, KS on the\n    distribution, sigma-normalized). Reproduced when neither finds a difference at p < 0.05 and the\n    KS test on z-scored activity finds experimental higher at p < 0.05. Under several readings of\n    window and nesting, the outcome is the one they all give.\n- id: figs4e-active-units-unchanged\n  statement: Among male-responsive units (at least 2 sigma above baseline), mean activity does not\n    differ between control and experimental mice.\n  source: Results, Effect of Oxtr/Avpr1a co-editing on VMHvl Esr1 activity and intruder sex\n    representations, paragraph 1; Figure S4E\n  quote: However, the mean activity among cells considered as “active” (≥ 2σ above baseline 66 ) did\n    not differ between control and experimental mice\n  statistics:\n  - test: nested Mann-Whitney test\n    p: 0.05\n    p_relation: \">\"\n  criterion: A claim of absence. Units with mean activity of at least 2 sigma above the\n    pre-intruder baseline during the male interaction window (readings as in\n    fig4ef-male-activity-slightly-lower); nested Mann-Whitney between groups under the file-level\n    readings. Reproduced when the test finds no difference at p < 0.05.\n  depends_on:\n  - fig4ef-male-activity-slightly-lower\n- id: fig4g-male-selective-reduced\n  statement: The fraction of male-activated units (selective or mixed) is slightly smaller in\n    experimental than in control mice (34.6% against 38.3%), and male-selective units are reduced\n    by about 56% (6.3 +/- 2% against 14.4 +/- 4%).\n  source: Results, Effect of Oxtr/Avpr1a co-editing on VMHvl Esr1 activity and intruder sex\n    representations, paragraph 2; Figure 4G, S4F\n  quote: The percentage of all male-activated neurons (selective or mixed) was slightly smaller in\n    experimental than control mice (34.6% vs. 38.3%, respectively ... while there was a ~56%\n    reduction in the small fraction of male-selective neurons (6.3 ± 2% vs. 14.4 ± 4%, respectively\n  expected:\n  - quantity: male-activated units, experimental\n    value: 34.6\n    tolerance: 3.46\n    unit: percent\n  - quantity: male-activated units, control\n    value: 38.3\n    tolerance: 3.83\n    unit: percent\n  - quantity: male-selective units, experimental\n    value: 6.3\n    tolerance: 2\n    unit: percent\n  - quantity: male-selective units, control\n    value: 14.4\n    tolerance: 4\n    unit: percent\n  criterion: A unit is male-selective when its activity is at least 2 sigma above the pre-intruder\n    baseline during the male interaction and below 2 sigma during the female interaction, and\n    mixed when at least 2 sigma during both (Results; Figure 4G legend). Window and baseline as in\n    fig4ef-male-activity-slightly-lower. The percentages can be read as (a) pooled over units of\n    all mice of the group, or (b) the mean over mice (the +/- values suggest b for the selective\n    fractions). Reproduced when, under a reading, all four values are within tolerance; partially\n    when the experimental male-selective fraction is lower than control but values fall outside.\n  depends_on:\n  - fig4ef-male-activity-slightly-lower\n- id: fig4g-female-selective-and-mixed-increased\n  statement: During female interactions the fractions of female-selective and of mixed-selectivity\n    units are increased by about 4% and 44% in experimental mice.\n  source: Results, Effect of Oxtr/Avpr1a co-editing on VMHvl Esr1 activity and intruder sex\n    representations, paragraph 2; Figure 4G, S4F\n  quote: Conversely, during female interactions the fraction of female-selective and mixed\n    selectivity neurons was increased by ~4% and ~44%, respectively, in experimental mice\n  expected:\n  - quantity: relative increase of female-selective fraction, experimental over control\n    value: 4\n    tolerance: 0.4\n    unit: percent\n  - quantity: relative increase of mixed-selectivity fraction, experimental over control\n    value: 44\n    tolerance: 4.4\n    unit: percent\n  criterion: Fractions defined as in fig4g-male-selective-reduced. \"Increased by\" can be read as\n    (a) a relative change, (experimental - control) / control, or (b) a difference in percentage\n    points; and the fractions as pooled or per-mouse means. Reproduced when, under one reading,\n    both increases are within tolerance; partially when both fractions are higher in experimental\n    mice but outside tolerance.\n  depends_on:\n  - fig4g-male-selective-reduced\n- id: fig4d-sex-decoding-intact\n  statement: Linear SVM decoders trained on VMHvl Esr1 activity from either control or\n    experimental mice predict intruder sex with virtually 100% accuracy.\n  source: Results, Effect of Oxtr/Avpr1a co-editing on VMHvl Esr1 activity and intruder sex\n    representations, paragraph 3; Figure 4D\n  quote: linear SVM decoders trained on imaging data from either control or experimental mice\n    correctly predicted intruder sex with virtually 100% accuracy\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.05\n    p_relation: \"<\"\n    about: decoder accuracy against shuffled decoders (Figure 4D)\n  expected:\n    quantity: mean decoder accuracy per group\n    value: 100\n    tolerance: 10\n    unit: percent\n  criterion: From the STAR Methods (Decoding intruder sex), per mouse, frame-wise linear SVM on\n    N-unit population vectors from all frames of social interaction, equal numbers of male and\n    female frames, stratified five-fold cross-validation, repeated 100 times, accuracy averaged per\n    mouse; shuffle control with labels assigned at random to each behavior bout, 500 repeats.\n    Reproduced when the mean accuracy of each group is at least 90% and above the shuffled\n    accuracy at p < 0.05 (Mann-Whitney across mice). The SVM regularization is not given; the\n    scikit-learn default (C = 1) is a standard choice, and the result at C = 0.1 and 10 is shown.\n- id: fig4c-pls-sex-separation\n  statement: Partial least-squares regression of population activity against intruder sex\n    separates responses to males and females in both control and experimental mice.\n  source: Results, Effect of Oxtr/Avpr1a co-editing on VMHvl Esr1 activity and intruder sex\n    representations, paragraph 3; Figure 4C, S4B-C\n  quote: This analysis revealed a clear separation of responses during encounters with males vs.\n    females in both control and experimental animals\n  criterion: From the STAR Methods (Dimensionality reduction), per mouse, PLS of all unit traces\n    against a vector that is -1 with a male intruder present, 1 with a female, 0 otherwise. The\n    paper gives no measure of separation. Readings (a) the mean PLS1 score differs in sign between\n    male and female frames; (b) the PLS1 scores of male and female frames overlap by less than\n    half (area under the ROC curve above 0.75 or below 0.25). Reproduced when, under both\n    readings, every mouse of both groups separates; the PLS1 variance explained per group (S4C) is\n    reported.\n- id: fig5ac-behavior-activity-male-lower\n  statement: Single-unit activity during male-directed sniffing and attack is slightly but\n    significantly lower in experimental than in control mice, while activity during\n    female-directed sniffing and mounting is similar.\n  source: Results, Effect of Oxtr/Avpr1a co-editing on behavior representation in VMHvl,\n    paragraph 1; Figure 5A, 5C, S5A-B\n  quote: The ECDF and average single unit activity during male-directed sniffing or attack was\n    slightly but significantly lower in experimental than in control mice ... In contrast, during\n    social interactions with females, activity during sniffing and mounting was similar\n  statistics:\n  - about: cumulative distributions (Figure 5A, S5B)\n    test: nested Kolmogorov-Smirnov test\n    p: 0.05\n    p_relation: \"<\"\n  - about: mean single-unit activity (Figure 5C)\n    test: nested Mann-Whitney test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: Per unit, mean activity (sigma above pre-intruder baseline; z-scored in S5) over all\n    frames annotated as each behavior. Tests as named under the file-level readings. Reproduced\n    when male-directed sniffing and attack are both lower in experimental mice at p < 0.05 and,\n    for female-directed sniffing and mounting, the paper's tests on sigma-normalized activity find\n    no difference at p < 0.05.\n- id: figs5c-peth-activity\n  statement: Mean bout-triggered activity is slightly but significantly lower in experimental mice\n    during male-directed sniffing and attack, higher during female-directed sniffing, and unchanged\n    during mounting.\n  source: Results, Effect of Oxtr/Avpr1a co-editing on behavior representation in VMHvl,\n    paragraph 1; Figure S5C\n  quote: The mean activity during male-directed sniffing or attack was slightly but significantly\n    lower in experimental than in control mice ... while it was significantly higher during\n    female-directed sniffing, but unchanged during mounting\n  statistics:\n  - test: nested Mann-Whitney test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: From the STAR Methods (Micro-endoscopic data extraction), for each unit and bout, the\n    z-scored trace minus the mean of a 2-3 s pre-bout baseline, averaged over 15 s after onset.\n    The baseline length is open; readings 2 s and 3 s. Nested Mann-Whitney under the file-level\n    readings. Reproduced when all four directions hold (male sniff and attack lower at p < 0.05,\n    female sniff higher at p < 0.05, mounting not different at p < 0.05).\n- id: fig5bd-behavior-selective-units-reduced\n  statement: During male interactions, sniff-selective units are reduced from 8.9 +/- 3% to 3.9 +/-\n    2% and attack-selective units from 6 +/- 0.9% to 1.8 +/- 0.7% in experimental mice; the\n    mixed-selectivity fraction is reduced by about 22%, and units active during male-directed\n    behaviors fall from 36.2% to 22.4%; female-directed selective fractions are similar.\n  source: Results, Effect of Oxtr/Avpr1a co-editing on behavior representation in VMHvl,\n    paragraph 2; Figure 5B, 5D\n  quote: In experimental mice, during male interactions the fraction of sniff-selective units was\n    reduced by ~40% relative to controls (3.9 ± 2% in OARs gRNAs mice vs. 8.9 ± 3% in Scr gRNAs\n    mice) while the small proportion of attack-selective units was reduced by ~70% (1.8 ± 0.7% vs.\n    6 ± 0.9% ... The fraction of neurons exhibiting mixed behavioral selectivity (i.e., active\n    during both behaviors) was moderately reduced (~22% ... Overall, there was a ~38% reduction in\n    the fraction of active units during all male-directed behaviors (from 36.2% in control to 22.4%\n    in experimental mice). In contrast, the fraction of female-directed sniffing- or\n    mount-selective units was similar between control and experimental males\n  expected:\n  - quantity: sniff-selective, experimental\n    value: 3.9\n    tolerance: 2\n    unit: percent\n  - quantity: sniff-selective, control\n    value: 8.9\n    tolerance: 3\n    unit: percent\n  - quantity: attack-selective, experimental\n    value: 1.8\n    tolerance: 0.7\n    unit: percent\n  - quantity: attack-selective, control\n    value: 6\n    tolerance: 0.9\n    unit: percent\n  - quantity: active during male-directed behaviors, control\n    value: 36.2\n    tolerance: 3.62\n    unit: percent\n  - quantity: active during male-directed behaviors, experimental\n    value: 22.4\n    tolerance: 2.24\n    unit: percent\n  - quantity: relative reduction of mixed-selectivity fraction\n    value: 22\n    tolerance: 2.2\n    unit: percent\n  criterion: Per unit, mean activity in sigma above the pre-intruder baseline over all frames of\n    each behavior; selective for sniff when at least 2 sigma during sniffing and below 2 sigma\n    during attack, and conversely; mixed when at least 2 sigma during both (Results; Figure 5B\n    legend). \"Active during all male-directed behaviors\" read as (a) at least 2 sigma during\n    sniffing or attack, or (b) the sum of the selective and mixed fractions as plotted in 5Di.\n    Fractions as (a) pooled or (b) per-mouse means. Reproduced when, under one reading, all\n    expected values are within tolerance; partially when the directions hold for sniff- and\n    attack-selective and active fractions but some values fall outside. Female-directed selective\n    fractions are reported with a Mann-Whitney test across mice; the text gives no test for them.\n- id: fig5e-cp-tuning-shift\n  statement: By choice probability, the percentages of attack- and sniff-tuned units during\n    male-male interactions are reduced by about 80% and 70% in experimental mice, mixed-selectivity\n    units increase by about 18%, and units tuned to sniffing females against sniffing males rise\n    from 28.8 +/- 3% to 41.1 +/- 3%.\n  source: Results, Effect of Oxtr/Avpr1a co-editing on behavior representation in VMHvl,\n    paragraph 3; Figure 5E, S5D\n  quote: We observed an ~80% and ~70% reduction in the percentage of attack- and sniff-tuned units,\n    respectively, in experimental vs. control mice during male-male interactions ... with a\n    concomitant ~18% increase in the fraction of units exhibiting mixed selectivity ... In\n    contrast, the percentage of units tuned to sniffing females (vs. sniffing males) was increased\n    in experimental mice (28.8 ± 3% vs. 41.1 ± 3%\n  expected:\n  - quantity: relative reduction of attack-tuned units (attack vs sniff male)\n    value: 80\n    tolerance: 8\n    unit: percent\n  - quantity: relative reduction of sniff-tuned units (attack vs sniff male)\n    value: 70\n    tolerance: 7\n    unit: percent\n  - quantity: relative increase of mixed-selectivity units (CP sniff vs attack at most 0.7)\n    value: 18\n    tolerance: 1.8\n    unit: percent\n  - quantity: units tuned to sniff female vs sniff male, control\n    value: 28.8\n    tolerance: 3\n    unit: percent\n  - quantity: units tuned to sniff female vs sniff male, experimental\n    value: 41.1\n    tolerance: 3\n    unit: percent\n  criterion: From the STAR Methods (Choice probability), per unit and pair of behaviors, the area\n    under the ROC curve built from histograms of the unit's dF/F values in frames of each behavior;\n    shuffled 100 times by shuffling behavior bout timings; tuned when CP > 0.7 and more than 2\n    shuffled SDs above the shuffled mean (the Results print \"p < 0.5\"; the Methods' 2-SD rule is\n    used). Open details and their readings. Direction, (a) CP(A vs B) > 0.7 means tuned to A and\n    CP(B vs A) > 0.7 tuned to B, (b) only CP(A vs B) is computed and tuned to B means CP < 0.3\n    with the mirrored shuffle test. Bout shuffling, (a) circular shift of the bout sequence by a\n    random offset, (b) random reassignment of bout onsets within the interaction period. The trace\n    used for \"dF/F\", (a) the sigma-normalized trace, (b) the z-scored trace. Fractions as pooled or\n    per-mouse means, and \"reduction\" or \"increase\" as relative change. Every combination is run;\n    reproduced when all the expected values are within tolerance under one combination and the\n    direction of each change holds under all; blocked as methods_underspecified when the\n    directions differ between combinations.\n- id: figs5e-behavior-decoding-intact\n  statement: Linear decoders distinguish attack from sniffing equally well in control and\n    experimental mice.\n  source: Results, Effect of Oxtr/Avpr1a co-editing on behavior representation in VMHvl,\n    paragraph 3; Figure S5E\n  quote: there was no significant difference between control and experimental mice in the\n    performance of linear decoders trained to distinguish attack from sniffing based on VMHvl\n    Esr1 activity\n  statistics:\n  - test: nested Mann-Whitney test\n    p: 0.05\n    p_relation: \">\"\n  criterion: A claim of absence, judged on the paper's test. From the STAR Methods (Decoding\n    behavior from neural activity), per mouse, frame-wise linear SVM on attack against sniffing\n    frames towards male intruders, equal numbers of frames of each, 20 repeats, accuracy averaged\n    per mouse; the cross-validation scheme is not given for this decoder, and the stratified\n    five-fold scheme of the sex decoder is used as the paper's nearest stated choice. The Methods\n    say frames are \"sampled at 15 Hz\" while traces are at 10 Hz; the data's own rate is used.\n    Reproduced when the Mann-Whitney test across mice finds no difference between groups at p <\n    0.05; both groups' accuracy against shuffled decoders is reported.\n- id: fig6-rslds-fit-quality\n  statement: rSLDS models with 5 latent dimensions and 3 discrete states, fit to each mouse with at\n    least 31 units, capture about 85% of the variance, with similar performance in control and\n    experimental mice; attack occurs within a single rSLDS state in both groups.\n  source: Results, VMHvl Esr1 line attractor dynamics require Oxtr/Avpr1a-mediated signaling,\n    paragraph 2; Figure S6D\n  quote: In both the control and experimental groups, the fit models reduced the dimensionality of\n    the data to 5 latent factors and three states (S1-S3) capturing ~85% of the observed variance\n    in neural activity. Model performance (cvR 2) was similar between control and experimental mice\n    ... During male-male interactions, attack behavior occurred during a single rSLDS state in both\n    control and experimental males\n  statistics:\n  - about: model performance, control against experimental\n    test: Mann-Whitney test\n    p: 0.05\n    p_relation: \">\"\n    n: 4 control and 7 experimental mice\n  expected:\n    quantity: variance explained by the rSLDS fit\n    value: 85\n    tolerance: 8.5\n    unit: percent\n  criterion: The rSLDS settings for all claims below are these. From the Results, one model per\n    mouse with at least 31 units, 5 latent dimensions, 3 discrete states. From the ssm notebook the\n    paper's code links, transitions recurrent_only, dynamics diagonal_gaussian, emissions\n    gaussian_orthog, single subspace, Laplace-EM with a structured mean-field posterior, 100\n    iterations. Time bins of 0.1 s (traces downsampled to 10 Hz, STAR Methods). Open details and\n    their readings. Which frames are fit, (a) the whole male-intruder part of the session from\n    intruder entry to removal plus the post-intruder period, (b) the whole session (STAR Methods\n    say the model relates \"the activity of recorded neurons (y) during male directed behavior\n    (sniffing, dominant mounting and attack)\"). The trace, (a) z-scored, (b) sigma-normalized.\n    Seeds and restarts are not given; seed 0 (the DJALab notebook's npr.seed(0)) is used and three\n    further seeds are shown. Performance is the forward-simulation score of the STAR Methods\n    (normalized MSE of predictions over a short horizon, computed on held-out folds), with the\n    horizon and folds not given (readings 1 s and 5 s; five folds over time); variance explained\n    as the R2 of the emissions reconstruction. Reproduced when variance explained is within\n    tolerance in both groups, performance does not differ at p < 0.05 (Mann-Whitney), and in\n    each mouse at least 90% of attack frames fall in one discrete state.\n- id: fig6a-control-tau1-greater\n  statement: In control mice, the time constant of the first rSLDS dimension (about 100-120 s) is\n    significantly larger than that of the second (about 40 s).\n  source: Results, VMHvl Esr1 line attractor dynamics require Oxtr/Avpr1a-mediated signaling,\n    paragraph 2; Figure 6A\n  quote: In control mice, the time constant (τ) of the 1 st rSLDS dimension (derived from the\n    first eigenvalue of the fit dynamics matrix; see Methods ) was significantly higher than that\n    of the 2 nd dimension (~100–120s vs. ~40s\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 0.05\n    p_relation: \"<\"\n    n: 4 control mice\n  expected:\n  - quantity: tau of dimension 1, control\n    value: 110\n    tolerance: 22\n    unit: s\n  - quantity: tau of dimension 2, control\n    value: 40\n    tolerance: 4\n    unit: s\n  criterion: tau = |1 / log(|lambda|)| for each eigenvalue lambda of the dynamics matrix, in time\n    bins, times 0.1 s (STAR Methods, Estimation of time constants), sorted in decreasing order.\n    Which dynamics matrix is open; readings (a) the matrix of the discrete state in which attack\n    occurs, (b) the mean of tau over the three states' matrices. rSLDS settings and readings as in\n    fig6-rslds-fit-quality. Tau 1 reproduces inside the reported range widened by 10% of each bound\n    (90 to 132 s); tau 2 within 10% of 40 s. Reproduced when, under a reading, the group means are\n    within tolerance and the Kruskal-Wallis test across the five dimensions' tau values (mice as\n    samples), followed by the comparison of dimension 1 with dimension 2, gives p < 0.05. With 4\n    mice a pairwise test may be unable to reach p < 0.05; the attainable minimum p is reported.\n  depends_on:\n  - fig6-rslds-fit-quality\n- id: fig6c-experimental-tau-indistinguishable\n  statement: In experimental mice the first two rSLDS dimensions have statistically\n    indistinguishable time constants (below 50 s), because the first dimension's time constant is\n    reduced relative to controls.\n  source: Results, VMHvl Esr1 line attractor dynamics require Oxtr/Avpr1a-mediated signaling,\n    paragraph 2; Figure 6C, S6E\n  quote: In contrast, in experimental mice the first two rSLDS dimensions had statistically\n    indistinguishable τ values (<50s; Figure 6C ) due to a reduced 1 st dimension τ\n  statistics:\n  - about: tau 1 against tau 2, experimental mice (Figure 6C)\n    test: Kruskal-Wallis test\n    p: 0.05\n    p_relation: \">\"\n    n: 7 experimental mice\n  - about: tau 1, control against experimental (Figure S6E)\n    test: Mann-Whitney test\n    p: 0.01\n    p_relation: \"<\"\n    n: 4 control and 7 experimental mice\n  expected:\n    quantity: upper bound of tau 1 and tau 2, experimental\n    value: 50\n    tolerance: 5\n    unit: s\n  criterion: Tau and readings as in fig6a-control-tau1-greater. Reproduced when, under a reading,\n    the experimental mean tau 1 and tau 2 are below 55 s (50 s plus 10%), the test of tau 1 against\n    tau 2 in experimental mice finds no difference at p < 0.05 (the absence is judged on the\n    paper's Kruskal-Wallis test), and tau 1 is lower in experimental than in control mice at p <\n    0.01 by Mann-Whitney (the S6E image shows two stars).\n  depends_on:\n  - fig6a-control-tau1-greater\n- id: fig6f-line-attractor-score\n  statement: The line attractor score, log2 of the ratio of the two largest time constants, is\n    about 1.6 in control mice and close to zero in experimental mice.\n  source: Results, VMHvl Esr1 line attractor dynamics require Oxtr/Avpr1a-mediated signaling,\n    paragraph 2; Figure 6F\n  quote: This yielded a line attractor score (calculated as the log 2 of the ratio of the τ ‘s of\n    the 1 st and 2 nd dimensions) of ~1.6 ... and consequently a line attractor score close to zero\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.05\n    p_relation: \"<\"\n    n: 4 control and 7 experimental mice\n  expected:\n    quantity: mean line attractor score, control\n    value: 1.6\n    tolerance: 0.16\n  criterion: Score = log2(tau_n / tau_n-1), the two largest time constants (STAR Methods), per\n    mouse; tau and readings as in fig6a-control-tau1-greater. \"Close to zero\" is judged by the\n    Methods' own reading, a score below 1 (the Methods say it \"is greater than one for systems that\n    possess a line attractor\"). Reproduced when, under a reading, the control mean is within\n    tolerance, the experimental mean is below 1, and Mann-Whitney finds control higher at p < 0.05.\n  depends_on:\n  - fig6-rslds-fit-quality\n- id: figs6f-mating-attractor-intact\n  statement: During mounting of female intruders, co-editing does not significantly reduce the\n    first-dimension time constant or the line attractor score.\n  source: Results, VMHvl Esr1 line attractor dynamics require Oxtr/Avpr1a-mediated signaling,\n    paragraph 2; Figure S6F\n  quote: during mounting behavior towards female intruders, co-perturbation of Oxtr/Avpr1a-mediated\n    signaling did not significantly reduce the 1st dimension τ values or the line attractor score\n    in experimental mice compared to controls\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.05\n    p_relation: \">\"\n    n: 4 control and 6 experimental mice\n  criterion: A claim of absence, judged on the paper's Mann-Whitney test. rSLDS fit to the\n    female-intruder part of each session (readings for the frames as in fig6-rslds-fit-quality,\n    with female-directed behavior in place of male-directed), mice with at least 31 units; tau 1\n    and score as in fig6a-control-tau1-greater and fig6f-line-attractor-score, with the state in\n    which mounting occurs in place of attack for reading (a). Reproduced when neither tau 1 nor the\n    score is lower in experimental mice at p < 0.05.\n  depends_on:\n  - fig6-rslds-fit-quality\n- id: fig6g-flow-field-line-vs-point\n  statement: Flow fields of the fit rSLDS in the plane of the first two principal components show\n    a line attractor (a roughly linear region of low flow) in control mice and a point attractor in\n    experimental mice.\n  source: Results, VMHvl Esr1 line attractor dynamics require Oxtr/Avpr1a-mediated signaling,\n    paragraph 3; Figure 6G-H, S6C\n  quote: The 2D flow field of control mice (Scr gRNAs) revealed a roughly linear region of low\n    vector flow constituting the line attractor ... In contrast, in experimental mice (OARs gRNAs)\n    this line attractor was absent and was replaced by a point attractor\n  criterion: The flow field is drawn from the fit dynamics as in the DJALab notebook (dx = A x + b\n    on a grid, speed = norm of dx, the 3D landscape its height), in the plane of the first two\n    principal components of the latent trajectories. The paper gives no measure of \"roughly\n    linear\"; the Methods' rule that a line attractor has a score above 1 is the measure used,\n    which makes this claim the visual counterpart of fig6f-line-attractor-score. Reproduced when\n    the claim fig6f-line-attractor-score is reproduced and the low-speed region (speed below its\n    10th percentile over the visited region) is elongated (ratio of principal axes above 3) in a\n    majority of control mice and not in a majority of experimental mice. The 10th percentile and\n    ratio 3 are standard choices; results at the 5th and 20th percentiles are shown.\n  depends_on:\n  - fig6f-line-attractor-score\n- id: fig6e-integration-dimension-persistence\n  statement: In control mice the activity of the first rSLDS dimension ramps up during sniffing and\n    attack and stays elevated after the intruder is removed; in experimental mice it decays rapidly\n    between attack bouts and is significantly lower in the post-intruder interval.\n  source: Results, VMHvl Esr1 line attractor dynamics require Oxtr/Avpr1a-mediated signaling,\n    paragraph 4; Figure 6B, 6D, 6E, S6A-B\n  quote: in control mice this activity ramped up during the progression from male-directed sniffing\n    to attack, eventually reaching a plateau where it decayed slowly between attack bouts towards a\n    single intruder and remained elevated between sequential trials with different intruders ...\n    In contrast, in experimental mice 1 st dimension neural activity decayed rapidly between attack\n    bouts, displaying a “sawtooth” profile, and was significantly lower during the post-intruder\n    (i.e., inter-trial) interval\n  statistics:\n  - about: during bouts against post-intruder, within each group (Figure 6E)\n    test: paired t-test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: The weighted average of unit activity on dimension 1 (the latent x1 of the fit,\n    equivalently the emission-weighted projection), normalized to 0-1 per mouse; rSLDS readings as\n    in fig6-rslds-fit-quality. Per mouse, its mean over all frames of male-directed behavior bouts\n    and over the post-intruder period. The post-intruder window is not given; readings (a) from\n    removal of the intruder to the next intruder's entry or the end of the male part, (b) the first\n    60 s after removal. Reproduced when, under a reading, the paired t-test across experimental\n    mice finds post-intruder lower than during bouts at p < 0.05 and the same test across control\n    mice does not; partially when the experimental drop is significant and the control drop is\n    also significant but smaller.\n  depends_on:\n  - fig6-rslds-fit-quality\n- id: fig7b-achw-first-dimension\n  statement: The mean autocorrelation half-width of units weighted on the first rSLDS dimension,\n    over the entire male-male interaction, is shorter in experimental (9.86 +/- 1 s) than in\n    control mice (28.6 +/- 1.23 s); the reduction is about 66%, against about 61% for\n    second-dimension units.\n  source: Results, Oxtr/Avp1ra-mediating signaling controls VMHvl Esr1 persistent neural activity,\n    paragraph 1; Figure 7B, S7A\n  quote: The mean ACHW of these neurons across the entire social interaction was significantly\n    shorter in experimental (9.86 ± 1 s) than in control mice (28.6 ± 1.23 s), by ~20 seconds ... A\n    reduction in the average ACHW was also observed among 2 nd rSLDS dimension cells\n  statistics:\n  - about: first-dimension units (Figure 7Bi)\n    test: nested Mann-Whitney test\n    p: 0.05\n    p_relation: \"<\"\n    n: 4 control and 7 experimental mice\n  - about: second-dimension units, cumulative distributions (Figure 7Bii)\n    test: Kolmogorov-Smirnov test\n    p: 0.05\n    p_relation: \"<\"\n    n: 4 control and 7 experimental mice\n  expected:\n  - quantity: mean ACHW of first-dimension units, experimental\n    value: 9.86\n    tolerance: 1\n    unit: s\n  - quantity: mean ACHW of first-dimension units, control\n    value: 28.6\n    tolerance: 1.23\n    unit: s\n  - quantity: relative reduction of mean ACHW, second-dimension units\n    value: 61\n    tolerance: 6.1\n    unit: percent\n  criterion: ACHW per unit is the lag at which the unit's autocorrelation first falls to half its\n    zero-lag value, in seconds (an \"approximate measure of the decay constant\", Results; the\n    computation is cited to Remedios et al. 2017 and not given here). Open details and their\n    readings. The trace, (a) z-scored, (b) sigma-normalized. Which units are \"weighted on\" a\n    dimension, (a) each unit assigned to the dimension of its largest absolute emission weight,\n    (b) the units in the top 25% by absolute weight on that dimension (the Results' \"~20–25%\" of\n    units). \"Average\" ACHW per unit, (a) one autocorrelation over the whole male-intruder period,\n    (b) the mean over intruder trials. rSLDS readings as in fig6-rslds-fit-quality. Every\n    combination is run; reproduced when, under one, the three expected values are within tolerance\n    and the paper's tests (under the file-level readings of \"nested\") give p < 0.05 with\n    experimental shorter; blocked as methods_underspecified if combinations disagree on the\n    direction or significance.\n  depends_on:\n  - fig6-rslds-fit-quality\n- id: fig7c-achw-all-units\n  statement: Across all VMHvl Esr1 units, the mean ACHW during the first 1-2 minutes of male-male\n    interaction is reduced in experimental mice (by about 50.9%), less than for first-dimension\n    units.\n  source: Results, Oxtr/Avp1ra-mediating signaling controls VMHvl Esr1 persistent neural activity,\n    paragraph 1; Figure 7C\n  quote: A reduction in the average ACHW was also observed among 2 nd rSLDS dimension cells, as well\n    as in the VMHvl Esr1 population as a whole ... the difference in mean ACHW between experimental\n    and control animals was larger for 1 st dimension-weighted units (~66%) than for 2 nd dimension\n    and total Esr1 + neurons (~61% and 50.9%, respectively\n  statistics:\n  - test: nested Mann-Whitney test (mean) and Kolmogorov-Smirnov test (distribution)\n    p: 0.05\n    p_relation: \"<\"\n    n: 5 control and 7 experimental mice\n  expected:\n    quantity: relative reduction of mean ACHW, all units\n    value: 50.9\n    tolerance: 5.09\n    unit: percent\n  criterion: ACHW and its readings as in fig7b-achw-first-dimension, all units of each mouse, over\n    the first part of the first male interaction; the window is \"the first 1–2 minutes\" (Figure 7C\n    legend), readings 1 min and 2 min. Reproduced when, under a reading, the reduction is within\n    tolerance and the experimental mean is lower at p < 0.05 by the paper's tests.\n- id: figs7b-achw-female-slight\n  statement: During male-female interactions, the mean ACHW of all VMHvl Esr1 units is only\n    slightly reduced in experimental mice (by about 22%).\n  source: Results, Oxtr/Avp1ra-mediating signaling controls VMHvl Esr1 persistent neural activity,\n    paragraph 1; Figure S7B\n  quote: In contrast, the average and cumulative distribution of ACHWs among all VMHvl Esr1 neurons\n    were only slightly reduced (by ~22%) during male-female interactions\n  statistics:\n  - test: nested Mann-Whitney test and Kolmogorov-Smirnov test\n    p: 0.05\n    p_relation: \"<\"\n    n: 5 control and 7 experimental mice\n  expected:\n    quantity: relative reduction of mean ACHW, all units, female interaction\n    value: 22\n    tolerance: 2.2\n    unit: percent\n  criterion: As fig7c-achw-all-units, for the first 1-2 minutes of the first female interaction\n    (S7B legend). The S7B image shows one and two stars; the legend does not say which test each\n    belongs to, and p < 0.05 is recorded. Reproduced when, under a reading, the reduction is within\n    tolerance.\n- id: figs7cd-slice-rslds\n  statement: An rSLDS fit to slice calcium responses to OXT plus AVP captures 85% of the variance,\n    with a first-dimension time constant (about 90 s) 8-9 times that of the second (about 15 s).\n  source: Results, OXT and AVP evoke persistent responses in VMHvl Esr1 neurons ex vivo,\n    paragraph 1; Figure S7C-D\n  quote: This fit model captured 85% of the observed variance in neural activity. The time constant\n    of dimension x1 (~90s) was ~8–9 -fold greater than that of x2 (~15s\n  expected:\n  - quantity: variance explained\n    value: 85\n    tolerance: 8.5\n    unit: percent\n  - quantity: tau x1\n    value: 90\n    tolerance: 9\n    unit: s\n  - quantity: tau x2\n    value: 15\n    tolerance: 1.5\n    unit: s\n  criterion: rSLDS settings as in fig6-rslds-fit-quality; the number of latent dimensions and\n    states for the slice fit is not given (Figure S7D shows two dimensions), and the frame rate is\n    about 1.2 Hz (STAR Methods). Readings (a) 2 latent dimensions, (b) 5 latent dimensions with\n    the two largest tau reported; the number of states read as 1 and 3. Reproduced when, under one\n    reading, all three values are within tolerance.\n- id: figs7k-persistent-and-transient-slice-responses\n  statement: Slice responses to OXT plus AVP fall into persistent responses that outlast the\n    perfusion window and transient responses that decay within it.\n  source: Results, OXT and AVP evoke persistent responses in VMHvl Esr1 neurons ex vivo,\n    paragraph 1; Figure S7F-K\n  quote: Plotting the time-varying weighted average activity of x1 and x2 neurons revealed that the\n    former exhibited slowly decaying responses to OXT+AVP application, while the latter exhibited\n    more transient responses\n  criterion: From the Figure S7K legend, a cell is transient when its response decays to 20% of the\n    peak within the peptide perfusion window and persistent when it decays to 20% after the\n    window. Reproduced when both classes contain cells and the x1-weighted cells (largest absolute\n    weight on x1) are mostly persistent while x2-weighted cells are mostly transient.\n  depends_on:\n  - figs7cd-slice-rslds\n"
}
```

```
File created successfully at: claims/001131/10.1016-j.cell.2024.08.015.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/001131/10.1016-j.cell.2024.08.015.yaml paper/10.1016-j.cell.2024.08.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

One quote mismatch ("Scr gRNA" in the text). Fixing it, plus a few criteria where I had put my own thresholds instead of readings from the paper.

**Agent calls Bash**

```bash
cd  f=claims/001131/10.1016-j.cell.2024.08.015.yaml; python3 - "$f" <<'E'
import sys
p=sys.argv[1]; s=open(p).read()
def r(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
r("reduced from 42.6± 3% in Scr gRNAs controls","reduced from 42.6± 3% in Scr gRNA controls")
r("""    value: 550
    tolerance: 105""","""    value: 555
    tolerance: 105""")
r("""    quantity: tau of dimension 1, control
    value: 110
    tolerance: 22""","""    quantity: tau of dimension 1, control
    value: 111
    tolerance: 21""")
r("""    accuracy at p < 0.05 (Mann-Whitney across mice). The SVM regularization is not given; the
    scikit-learn default (C = 1) is a standard choice, and the result at C = 0.1 and 10 is shown.""",
"""    accuracy at p < 0.05 (Mann-Whitney across mice). The SVM regularization is not given;
    readings C = 0.1, 1 and 10, and the outcome is the one they all give.""")
r("""    paper gives no measure of separation. Readings (a) the mean PLS1 score differs in sign between
    male and female frames; (b) the PLS1 scores of male and female frames overlap by less than
    half (area under the ROC curve above 0.75 or below 0.25). Reproduced when, under both
    readings, every mouse of both groups separates; the PLS1 variance explained per group (S4C) is
    reported.""","""    paper gives no measure of "clear separation". Readings of it (a) the mean PLS1 score differs
    in sign between male and female frames; (b) the area under the ROC curve of PLS1 scores,
    male against female frames, is above 0.75 or below 0.25. Reproduced when, under both
    readings, every mouse of both groups separates; blocked as methods_underspecified when the
    readings disagree. The PLS1 variance explained per group (S4C) is reported.""")
r("""    Seeds and restarts are not given; seed 0 (the DJALab notebook's npr.seed(0)) is used and three
    further seeds are shown.""","""    Seeds and restarts are not given; fits are run with seeds 0 (the DJALab notebook's
    npr.seed(0)) to 3, and each claim's outcome is the one all seeds give.""")
r("""    tolerance in both groups, performance does not differ at p < 0.05 (Mann-Whitney), and in
    each mouse at least 90% of attack frames fall in one discrete state.""","""    tolerance in both groups, performance does not differ at p < 0.05 (Mann-Whitney), and in
    each mouse attack "occurred during a single rSLDS state", read as (a) a majority of attack
    frames fall in one state, (b) at least 90% do.""")
r("""    principal components of the latent trajectories. The paper gives no measure of "roughly
    linear"; the Methods' rule that a line attractor has a score above 1 is the measure used,
    which makes this claim the visual counterpart of fig6f-line-attractor-score. Reproduced when
    the claim fig6f-line-attractor-score is reproduced and the low-speed region (speed below its
    10th percentile over the visited region) is elongated (ratio of principal axes above 3) in a
    majority of control mice and not in a majority of experimental mice. The 10th percentile and
    ratio 3 are standard choices; results at the 5th and 20th percentiles are shown.""","""    principal components of the latent trajectories. The paper gives no measure of the shape of
    the low-flow region; its only measure of a line against a point attractor is the line
    attractor score (STAR Methods, score above 1 for a line attractor, near 0 for a point
    attractor). The outcome is that of fig6f-line-attractor-score, judged per mouse here, with
    reproduced when the score is above 1 in a majority of control mice and below 1 in a majority
    of experimental mice. The flow field and landscape of every mouse are shown and described, and
    do not decide the outcome.""")
open(p,'w').write(s)
E
python tools/claims_check.py $f paper/10.1016-j.cell.2024.08.015.txt; grep -nE "^[^#].*[^\"']: [^ ].*: " $f | grep -v "quote:\|statement:\|criterion:\|inferred:" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/001131/10.1016-j.cell.2024.08.015.yaml; grep -n "tau of dimension 1, control" -A3 $f
```

```
637:  - quantity: tau of dimension 1, control
638-    value: 110
639-    tolerance: 22
640-    unit: s
```

**Agent calls Bash**

```bash
cd  f=claims/001131/10.1016-j.cell.2024.08.015.yaml; sed -i '638s/value: 110/value: 111/;639s/tolerance: 22/tolerance: 21/' $f; python3 - "$f" <<'E'
import sys
p=sys.argv[1]; s=open(p).read()
def r(a,b):
    global s
    assert s.count(a)==1, a
    s=s.replace(a,b)
r("reduced from 42.6± 3% in Scr gRNAs controls","reduced from 42.6± 3% in Scr gRNA controls")
r("""    value: 550
    tolerance: 105""","""    value: 555
    tolerance: 105""")
r("""    accuracy at p < 0.05 (Mann-Whitney across mice). The SVM regularization is not given; the
    scikit-learn default (C = 1) is a standard choice, and the result at C = 0.1 and 10 is shown.""",
"""    accuracy at p < 0.05 (Mann-Whitney across mice). The SVM regularization is not given;
    readings C = 0.1, 1 and 10, and the outcome is the one they all give.""")
r("""    paper gives no measure of separation. Readings (a) the mean PLS1 score differs in sign between
    male and female frames; (b) the PLS1 scores of male and female frames overlap by less than
    half (area under the ROC curve above 0.75 or below 0.25). Reproduced when, under both
    readings, every mouse of both groups separates; the PLS1 variance explained per group (S4C) is
    reported.""","""    paper gives no measure of "clear separation". Readings of it (a) the mean PLS1 score differs
    in sign between male and female frames; (b) the area under the ROC curve of PLS1 scores,
    male against female frames, is above 0.75 or below 0.25. Reproduced when, under both
    readings, every mouse of both groups separates; blocked as methods_underspecified when the
    readings disagree. The PLS1 variance explained per group (S4C) is reported.""")
r("""    Seeds and restarts are not given; seed 0 (the DJALab notebook's npr.seed(0)) is used and three
    further seeds are shown.""","""    Seeds and restarts are not given; fits are run with seeds 0 (the DJALab notebook's
    npr.seed(0)) to 3, and each claim's outcome is the one all seeds give.""")
r("""    tolerance in both groups, performance does not differ at p < 0.05 (Mann-Whitney), and in
    each mouse at least 90% of attack frames fall in one discrete state.""","""    tolerance in both groups, performance does not differ at p < 0.05 (Mann-Whitney), and in
    each mouse attack "occurred during a single rSLDS state", read as (a) a majority of attack
    frames fall in one state, (b) at least 90% do.""")
r("""    principal components of the latent trajectories. The paper gives no measure of "roughly
    linear"; the Methods' rule that a line attractor has a score above 1 is the measure used,
    which makes this claim the visual counterpart of fig6f-line-attractor-score. Reproduced when
    the claim fig6f-line-attractor-score is reproduced and the low-speed region (speed below its
    10th percentile over the visited region) is elongated (ratio of principal axes above 3) in a
    majority of control mice and not in a majority of experimental mice. The 10th percentile and
    ratio 3 are standard choices; results at the 5th and 20th percentiles are shown.""","""    principal components of the latent trajectories. The paper gives no measure of the shape of
    the low-flow region; its only measure of a line against a point attractor is the line
    attractor score (STAR Methods, score above 1 for a line attractor, near 0 for a point
    attractor). Judged per mouse, reproduced when the score is above 1 in a majority of control
    mice and below 1 in a majority of experimental mice. The flow field and landscape of every
    mouse are shown and described, and do not decide the outcome.""")
open(p,'w').write(s)
E
python tools/claims_check.py $f paper/10.1016-j.cell.2024.08.015.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/001131/10.1016-j.cell.2024.08.015.yaml; grep -nc "—" $f; grep -ni "rather" $f; grep -c "^- id" $f; grep -c "statistics:" $f; grep -c "criterion:" $f; git status --short
```

```
0
34
24
34
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
?? claims/001131/
?? scripts
```

**Agent**

I wrote the claims file at `claims/001131/10.1016-j.cell.2024.08.015.yaml`. The quote checker passes it with 0 problems.

**Text read.** I read the accepted author manuscript from PubMed Central (PMC11490375), not the version of record. It has the Results, Discussion, STAR Methods, and the legends for both the main and supplementary figures. The supplement PDF holds only the images of Figures S1 to S7, so I could read the star levels for the supplementary panels. The main figures are not in the files I was given.

**Code read.**
- DJALab/VMHvl_MPOA_dynamics at commit ed83c41 holds one notebook that draws flow fields for synthetic linear systems. It has no code for this paper's data.
- Its README points to the rSLDS notebook in lindermanlab/ssm (commit eb6c8aa). I took the rSLDS fitting settings from that notebook.

**Claims.** There are 34, all with quotes. 24 have statistics (29 p-values) and all 34 have criteria. One claim, the RNA-seq co-expression figures, uses outside data, from the Kim et al. 2019 atlas. The claims cover the RNA-seq atlas, slice imaging, behaviour, fiber photometry, the miniscope single-unit analyses, the rSLDS time constants and line attractor score, the activity on the first rSLDS dimension, autocorrelation half-width (ACHW), and the rSLDS fit to slice data.

**Details the paper leaves open, and the readings named for each:**
- **"Nested" Mann-Whitney and KS tests:** (a) on all units pooled; (b) on per-mouse means or medians.
- **Sigma baseline:** (a) the whole pre-intruder period; (b) the 7 s before the first intruder.
- **Analysis window:** the Results say the first 2 minutes and the Figure 4 legend says 1 minute; both are named. The same 1 or 2 minutes apply to the "first 1–2 minutes" ACHW windows.
- **Number of control mice:** the Results say 4, while the legends and Methods say 5. Both are named.
- **Fractions:** pooled over units, or the mean over mice. "Increase" or "reduction" as a relative change, or as percentage points.
- **rSLDS fit:** which frames are fit (the male-intruder part, or the whole session); z-scored or sigma-normalised traces; seeds 0 to 3, with the outcome the one all seeds give.
- **Which dynamics matrix gives the time constant:** (a) that of the state in which attack occurs; (b) the mean over the three states.
- **"Attack in a single state":** a majority of attack frames, or at least 90%.
- **Fit-quality horizon:** forward-simulation score at 1 s or 5 s.
- **Choice probability:** how the direction is computed, how bouts are shuffled, and which trace is used. Every combination is run.
- **ACHW:** which units count as weighted on a dimension (by largest weight, or the top 25%); one autocorrelation, or the mean over trials.
- **Other details:**
  - SVM regularisation: C = 0.1, 1 and 10.
  - "Clear separation" in the PLS plot: two measures named.
  - Post-intruder window: until the next intruder, or the first 60 s.
  - Pre-bout baseline for the bout-triggered averages: 2 s or 3 s.
  - Rate of the behaviour decoder: the Methods say 15 Hz against 10 Hz traces; the data's own rate is used.
  - Slice rSLDS: 2 or 5 dimensions, 1 or 3 states.

**Missing from the paper that some claims needed:**
- Which significance stars go with each main-figure panel. Where those were unreadable I recorded p < 0.05, the paper's lowest level.
- The rule for a responsive cell in the slice data.
- The expression threshold for the atlas.
- How ACHW is computed, which the paper cites to Remedios et al. 2017.
- How the rSLDS was fit, which it cites to Nair et al. 2023 and which the code fixes only in part.
- The test for Figure S4A. I used Mann-Whitney, the paper's test for the same measures elsewhere.
- Any measure of the flow-field shape. That claim is judged on the line attractor score instead.

Nothing is committed.

## End of run

29 turns, 6 minutes, result: success.
