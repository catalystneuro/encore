# 001249 · claims · run 39810638521

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/## Reader/,/^## [^R]/p'; ls claims/001453/ claims/001249/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -200; wc -l paper/*.txt claims/001453/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat paper/10.7554-elife.91765.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '1,201p' paper/10.7554-elife.91765.txt | fold -w 4000 | head -c 60000
```

Result: not kept, because it reads the paper's text.

**Agent**

I'll read the saved file in chunks.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.91765.txt",
 "limit": 40
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)}' *.txt | awk -F': ' '$2>2000'; fold -s -w 3000 10.7554-elife.91765.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt
```

```
7: 169106
257 /tmp/claude-1001/p.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 20,
 "offset": 7
}
```

```
7	pmc eLife Elife eLife eLife 2050-084X eLife Sciences Publications, Ltd 11882143 40042245 91765 10.7554/eLife.91765 version of record Research Article Neuroscience Post-ejaculatory inhibition of female sexual drive via heterogeneous neuronal ensembles in the medial preoptic area Ishii Kentaro K https://orcid.org/0000-0002-7956-0806 1 2 Hashikawa Koichi 1 2 Chea Jane 1 2 Yin Shihan 1 2 Fox Rebecca Erin 1 2 Kan Suyang 1 2 Shah Meha 1 2 Zhou Zhe Charles 1 2 Navarrete Jovana 1 3 Murry Alexandria D 1 3 Szelenyi Eric R 1 3 Golden Sam A 1 3 Stuber Garret D https://orcid.org/0000-0003-1730-4855 [removed: an e-mail address] 1 2 4 1 https://ror.org/00cvxb145 Center for the Neurobiology of Addiction, Pain, and Emotion, University of Washington Seattle United States 2 https://ror.org/00cvxb145 Department of Anesthesiology and Pain Medicine, University of Washington Seattle United States 3 https://ror.org/00cvxb145 Department of Biological Structure, University of Washington Seattle United States 4 https://ror.org/00cvxb145 Department of Pharmacology, University of Washington Seattle United States McCarthy Margaret M Reviewing Editor https://ror.org/055yg0521 University of Maryland School of Medicine United States Wassum Kate M Senior Editor https://ror.org/046rm7j60 University of California, Los Angeles United States 05 3 2025 2025 12 RP91765 29 8 2023 This manuscript was published as a preprint. 09 9 2023 This manuscript was published as a reviewed preprint. 14 11 2023 The reviewed preprint was revised. 14 2 2025 © 2023, Ishii et al 2023 Ishii et al https://creativecommons.org/licenses/by/4.0/ This article is distributed under the terms of the Creative Commons Attribution License , which permits unrestricted use and redistribution provided that the original author and source are credited. Male ejaculation acutely suppresses sexual motivation in male mice. In contrast, relatively little is known about how male ejaculation affects sexual motivation and sexual behavior in female mice. How the
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 20,
 "offset": 27
}
```

```
27	before the experiment day. On the experiment day, subjects were injected i.p. with clozapine-N-oxide (CNO) to inhibit TRAP cells, or saline as control. 30 min after the injection, the male partner was placed into the apparatus and the animal behavior was recorded for 2 hr. ( C ) After incubation of the virus, the female subjects were administered with hormones, then received an ejaculation from the male partner. Immediately after, the subjects were administrated with 4-hydroxytamoxifen (4-OHT). ( D ) Raster plots of time spent in the interaction zone the female self-paced mating assay (Post-ejaculatory-eYFP: gray. Post-ejaculatory-hM3Dq: orange). ( E–L ) Number of zone transitions per 10 min ( E ), eYFP, p=0.4375. hM4Di, p=1, average time in isolation zone ( F ), eYFP, p=1. hM4Di, p=1, average time in interaction zone ( G ), eYFP, p=0.3125. hM4Di, p=0.15625, number of female-to-male sniff ( H ), eYFP, p=0.1592. hM4Di, p=0.9917, female self-grooming ( I ), eYFP, p=0.2883. hM4Di, p=1, male mount ( J ), eYFP, p=0.4456. hM4Di, p=1, male intromission ( K ), eYFP, p=0.4456. hM4Di, p=1. and the receptive score (number of mount episodes with intromissions/number of all mount episodes) ( L ), eYFP, P =1. hM4Di, p=0.1094. ( M ) Schematic of pharmaco-genetic inhibition of MPOA neurons during a home cage mating assay. Female subjects were primed with hormone before the experiment day. On the experiment day, subjects were injected i.p. with CNO to activate TRAP cells 30 min before the experiment. Animal behavior was recorded for 90 min. ( N ) The male mating partner was placed into the home cage of the female subject. ( O–R ) Number of female-to-male sniff ( O ), p=0.6969, male mounting ( P ), p=0.4003, male intromission ( Q ) **p=0.0045 and the receptive score (number of mounting episodes with intromissions over all mounting episodes) ( R ) *p=0.01998. All data are shown by thin lines for individual subjects and thick lines for mean. The data were analyzed by Wilcoxon rank s
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '47,257p' $TMPDIR/p.txt | grep -n -i -E "supplementary|figure|source data" | head; ls claims | head -50; ls tools
```

```
9:Washington Seattle United States Fox Rebecca Erin Author University of Washington Seattle United States Kan Suyang Author University of Washington Seattle United States Shah Meha Author University of Washington Seattle United States Zhou Zhe Charles Author University of Washington Seattle United States Navarrete Jovana Author University of Washington Seattle United States Murry Alexandria D Author University of Washington Seattle United States Szelenyi Eric R Author University of Washington Seattle United States Golden Sam Author University of Washington Seattle United States Stuber Garret D Author University of Washington Seattle United States The following is the authors’ response to the original reviews. Public Reviews: Reviewer #1 (Public Review): […] Weaknesses: While there are no glaring weaknesses in this study, it should be noted that a great deal of literature has pinpointed the MPOA (and specifically inhibitory cells in this area) as being critical to sexual behavior, including female mating. However, no study to my knowledge has explored self-paced female mating with such fine control over manipulating and monitoring cellular activity in this region. In addition, this study may act to inspire others to further explore the additional brain regions found to show upregulation of neural activity (Fos) during mating completion in the female using the data sets generated here. Reviewer #2 (Public Review): […] Weaknesses: The authors include an elegant manipulation of ejaculation-activated neurons in the MPOA using DREADD. However, this study was limited to show that activation of previously activated cells was sufficient to reduce approach behavior in a paced mating paradigm and receiving intromissions in a home cage mating paradigm. An inhibition approach using DREADD would have been a great complement to this study as it would have examined if activation of the cells was required. Moreover, additional tests for sexual motivation would have greatly strengthe
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/stuberlab/Ishii-MPOA-Ejaculation-2023 code 2>&1 | tail -3; cd code && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100
```

```
4e98c4369ea0f6dcfc2648c561d43a4a235e5f15 Mon Feb 24 15:50:41 2025 -0800
./README.md
./LICENSE
./Figure S9.ipynb
./Figure S5_Seurat clustering.R
./Figure S5.ipynb
./Figure S2.ipynb
./Figure S11.ipynb
./Figure S10.ipynb
./Figure S1.ipynb
./Figure 6.ipynb
./Figure 5 Spectral clustering.ipynb
./Figure 3, 4, 5, S6, S7, S8.ipynb
./Figure 2.ipynb
./Figure 1.ipynb
Shell cwd was reset to
```

**Agent**

Paper text read; the paper's code repository cloned (commit 4e98c43). Now reading the Figure 2 (whole-brain TRAP) notebook, the analysis the dataset holds.

**Agent calls Bash**

```bash
cd $TMPDIR/code && cat README.md && python3 -c "
import json
nb=json.load(open('Figure 2.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        print('---- cell',i); print(''.join(c['source']))
        for o in c.get('outputs',[]):
            t=''.join(o.get('text',[])) or ''.join(o.get('data',{}).get('text/plain',[]))
            if t: print('>>OUT:', t[:1500])
    else:
        print('---- md',i, ''.join(c['source'])[:500])
"
```

```
These are the codes used for analysis and figure generation in the manuscript "Post-ejaculatory Inhibition of Female Sexual Drive via Heterogeneous Neuronal Ensembles in the Medial Preoptic Area" (Ishii et al. 2023) from the Stuber lab.

The codes require data distributed on figshare https://doi.org/10.6084/m9.figshare.27642768.v1. 
Raw data for the whole brain FosTRAP mapping are distributed on DANDI [https://dandiarchive.org/dandiset/001249](https://dandiarchive.org/dandiset/001249/0.241109.2357). 
---- cell 0
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import tifffile
import matplotlib
#important for text to be detected when importing saved figures into illustrator
matplotlib.rcParams['pdf.fonttype']=42
matplotlib.rcParams['ps.fonttype']=42

---- cell 1
# paths for raw data
# the inscopix data will be saved in the tracefolderpath as trace csv
# the behavior data, in this case manually annotated data, will be 
[... 335 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,321p claims/001453/*.yaml; grep -l "elsewhere" claims/*/*.yaml | head -3; grep -h -A6 "data: elsewhere" claims/*/*.yaml | head -30; grep -h -B2 -A8 "^outside\|external_data\|^sources:" claims/*/*.yaml | head -40
```

```
relatively constant velocity.
  source: Results, Larval DC exhibit higher average swimming speeds, paragraph 1; Figure 1C and
    Figure S1D
  quote: These visually evoked bouts in ZF consist of sharp velocity increases ... followed by
    interbout glides, resulting in characteristic periodic patterns. While DC also match the optic
    flow direction, they swim continuously, maintaining a relatively constant velocity
  criterion: The paper shows this with representative traces and a bout analysis whose bout
    files are not in the dandiset, so a measure is fixed here. Per trial, positions resampled
    to 30 Hz between 3 and 35 s, instantaneous speed, and the ratio of its median to its mean
    (near 1 for steady swimming, low for bursts); per fish, the median over all trials of all
    stimulus codes. Reproduced when the ZF fish have lower ratios than the DC fish by a
    two-sided Mann-Whitney test at p < 0.05.
- id: fig1cef-representative-values
  statement: In representative trials ZF bouts reach a peak velocity of 44.7 mm/s with a median
    of 1.8 mm/s, DC swim at a median of 13.7 mm/s to forward motion; to oblique motion ZF show
    a median angular velocity of 12.0 degrees/s and median peak angular acceleration of 174
    degrees/s2, and DC an average peak of 103 degrees/s2 to rightward motion.
  source: Results, Larval DC exhibit higher average swimming speeds, paragraph 1, and Results, Optic
    flow induces angular matching and turns in DC, paragraph 1; Figure 1C, 1E and 1F
  quote: sharp velocity increases (peak velocity = 44.7 mm/s, median velocity = 1.8 mm/s) ...
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "where\|data\b\|ALLOWED\|kind" tools/claims_check.py | head -40
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

[... 63 more lines not kept]
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
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:4000])"
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
curl -s https://api.dandiarchive.org/api/dandisets/001249/versions/0.241109.2357/info/ | python3 -c "import json,sys;d=json.load(sys.stdin);m=d.get('metadata',d);print(m.get('name'));print(m.get('description'));print(d.get('asset_count'), d.get('size'))"
```

Result: the fetched text is not kept.

**Agent**

Dataset: 14 assets, ~1.4 TB, the FosTRAP whole-brain light-sheet data (Figure 2: 4 + 5 + 5 brains). Checking the other notebooks' tests briefly to cite them in criteria.

**Agent calls Bash**

```bash
cd $TMPDIR/code && for f in "Figure 1.ipynb" "Figure S1.ipynb" "Figure S2.ipynb" "Figure 3, 4, 5, S6, S7, S8.ipynb" "Figure 5 Spectral clustering.ipynb" "Figure 6.ipynb" "Figure S5.ipynb" "Figure S9.ipynb" "Figure S10.ipynb"; do echo "=== $f"; python3 -c "
import json,sys,re
nb=json.load(open(sys.argv[1]))
src='\n'.join(''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code')
for l in src.split('\n'):
    if re.search(r'AnovaRM|tukey|wilcoxon|mannwhitney|ranksums|ttest|chi2|f_oneway|bonferroni|multipletests|\*\s*2|> *2|std|zscore|decay|silhouette|per 10|/ *10|600',l,re.I): print('  ',l.strip()[:160])
" "$f" | sort -u | head -40; done
```

```
=== Figure 1.ipynb
   # Append Tukey HSD results to DataFrame
   # Append the Wilcoxon result to manuscript_statistic_file
   # Perform Two-way Wilcoxon signed-rank test test
   # Plot the duration in the Isolation zone per 10 min
   # Plot the number of mounts per 10 min
   # Plot the number of zone transition per 10 min
   # Run Tukey's HSD test
   # Save the Tukey results to a file
   # Save the Wilcoxon results to a .pickle file
   # plot transition per 10 min
   #perform Two-way Wilcoxon signed-rank test
   'Type of Test': 'Tukey HSD',
   'Type of Test': 'Two-way Wilcoxon signed-rank test',
   ax[0].set_xticklabels(np.linspace(0,30,30//10 +1).astype('int'))
   ax[0].set_xticks(np.linspace(0,1800,1800//600 +1))
   ax[1].set_xticklabels(np.linspace(-110,10,120//10 +1).astype('int'))
   ax[1].set_xticks(np.linspace(-6600,600,7200//600 +1))
   axs.set_xlim(-300,600)
   axs.set_xticks(np.linspace(-300,600,900//300 +1))
[... 230 more lines not kept]
```

**Agent**

The dataset holds only the Figure 2 experiment: whole-brain FosTRAP light-sheet data from 14 brains. I've read the paper and the Figure 2 code. Next I'm writing the claims file.

**Agent calls Bash**

```bash
cd $TMPDIR/code && python3 - <<'EOF'
import json,re
nb=json.load(open('Figure 3, 4, 5, S6, S7, S8.ipynb'))
src='\n'.join(''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code')
for k in ['decay','specific','only','categor','_cell_types','magnitude_zscore']:
    for m in re.finditer(r'.*'+k+r'.*',src):
        print(k,'|',m.group(0).strip()[:200])
EOF
```

```
decay | # Plot decay length for Figure 5C
decay | y = 'Ejaculation_decay_length_seconds',x ='Mouse_line' ,ax = axs,palette = ['orangered','limegreen'])
decay | # extract decay length from vgat and vglut2 populations
decay | vgat = analysis_metainfo[(analysis_metainfo.Ejaculation_positive_responding_cells) & (analysis_metainfo.Mouse_line == 'Vgat-Cre')].Ejaculation_decay_length_seconds
decay | vglut2 = analysis_metainfo[(analysis_metainfo.Ejaculation_positive_responding_cells) & (analysis_metainfo.Mouse_line == 'Vglut2-Cre')].Ejaculation_decay_length_seconds
decay | decay_length_ttest = stats.ttest_ind(vgat,vglut2)
decay | print(decay_length_ttest)
decay | pickle.dump(decay_length_ttest, handle, protocol=pickle.HIGHEST_PROTOCOL)
decay | 'statistic': decay_length_ttest[0],
decay | 'p Value': decay_length_ttest[1]
decay | # Plot decay length for cells in each type for Figure 5F
decay | y = 'Ejaculation_decay_length_seconds',ax = axs,palette = ['deeppink','darkred','sienna','yellowgreen','slateblue'])
decay | # First test if there is a difference in the average decay length between the 5 types.
decay | model = ols('Ejaculation_decay_length_seconds ~ C(Ejaculation_long_labels)', data=responding_analysis_metainfo).fit()
decay | tukey_results = pairwise_tukeyhsd(responding_analysis_metainfo['Ejaculation_decay_length_seconds'],\
only | # First plot for cells only responding to Sniff.
only | celltype = sort_key +'_only_cells'
only | == 'Ejaculation_only_cells'].shape[0])\
only | # Plot for cells only responding to Mount.
only | celltype = sort_key +'_only_cells'
[... 56 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001249/10.7554-elife.91765.yaml",
 "content": "# Claims for Ishii et al. (2025), \"Post-ejaculatory inhibition of female sexual drive via\n# heterogeneous neuronal ensembles in the medial preoptic area\", eLife 12, RP91765, on dandiset\n# 001249.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22,\n# protocol as stated in docs/protocol.md.\n#\n# Text read: the version of record (eLife RP91765, published 5 March 2025) as served by Europe\n# PMC: main text, all figure legends and figure supplement legends, Materials and methods, and\n# the authors' response to the reviewed preprint. Supplementary files 1 to 3 (tables of every\n# statistical result; files 2 and 3 hold the per-region ANOVA and Tukey values of Figure 2) are\n# not in the text, so the region-level statistics of Figure 2 are not recorded here.\n# Code read: github.com/stuberlab/Ishii-MPOA-Ejaculation-2023, commit 4e98c43 (2025-02-24). Its\n# notebooks are named by the preprint's figure numbers; \"Figure 2.ipynb\" is the whole-brain\n# analysis of the published Figure 2. It starts from a table of densities (tdTomato_summary.csv,\n# on Figshare) and holds the per-region one-way ANOVA (scipy f_oneway over the three groups),\n# the Benjamini-Hochberg correction (statsmodels fdrcorrection, alpha 0.1 at both atlas levels),\n# and Tukey's HSD (scipy tukey_hsd) for every region. The image processing (ClearMap\n# registration, ilastik cell classifier) is not in the repository.\n#\n# The dandiset (\"FosTRAP dataset used in Ishii et al 2023\", 14 assets) holds the whole-brain\n# activity mapping of Figure 2 only (Data availability). As the paper reports it: TRAP2::Ai14\n# (Fos-2A-iCreERT2 x Rosa26-LSL-tdTomato) females, ovariectomized and primed with estradiol,\n# given 4-OHT (50 mg/kg i.p.) immediately after the male was removed in one of three phases:\n# appetitive (sniffing only, n=4), consummatory (mount or intromission, no ejaculation, n=5),\n# post-ejaculatory (just after male ejaculation, n=5). Two weeks later brains were cleared\n# (SHIELD) and imaged on a SmartSPIM light-sheet microscope (3.6x objective, 4 um z step;\n# 594 nm signal channel, 488 or 647 nm background channel used for registration), downsampled\n# to 3.6 x 3.6 x 4 um, registered to the Unified Anatomical Atlas of the Kim lab (Chon et al.\n# 2019; 20 x 20 x 50 um) with ClearMap, and tdTomato+ cells segmented with an ilastik\n# classifier. The measured variable is the tdTomato+ cell density (cells per mm3) per atlas\n# region per brain, at hierarchy level 4 (Figure 2C) and level 6 (Figure 2H, Figure 2-figure\n# supplement 2).\n# All other experiments (self-paced and home cage mating behavior, HCR in situ, calcium imaging\n# of Vgat-Cre and Vglut2-Cre MPOA neurons, chemogenetics) are on Figshare,\n# doi:10.6084/m9.figshare.27642768.v1, and their claims are marked data elsewhere.\n#\n# Method choices for Figure 2 taken from the code where the Methods are silent: level-4 regions\n# are the ten of the code's level_4_order (CTXpl, CTXsp, STR, PAL, TH, HY, MBsen, MBmot, MBsta,\n# P); the level-6 family is the level-6 regions whose level-4 ancestor is one of these ten; the\n# group mean is np.nanmean over brains; Tukey's HSD is scipy's tukey_hsd on the three groups.\n# Where the Methods and the code disagree the Methods are followed and the code is a variant.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001249\"\n  doi: 10.48324/dandi.001249/0.241109.2357\npaper: doi:10.7554/elife.91765\nclaims:\n- id: fig2-density-link\n  kind: link\n  statement: The tdTomato+ cell densities computed from the dandiset's whole-brain images agree,\n    brain by brain, with the densities in the paper's deposited table (tdTomato_summary.csv on\n    Figshare) that its Figure 2 code reads.\n  source: Data availability; Figure 2.ipynb at GitHub commit 4e98c43, cell 4\n  quote: Whole brain FosTRAP activity mapping data is available on DANDI\n  data: with_inputs\n  criterion: Densities computed here as in fig2c-brain-wide-increase (ClearMap registration to the\n    Unified Anatomical Atlas, ilastik segmentation, count per region over region volume). The\n    trained classifier is not deposited, so it is retrained as the Methods describe (10 random\n    chunks of 1.8 x 1.8 mm x 100 um from four subjects). The link holds (reproduced) when the 14\n    brains fall into groups of 4, 5 and 5 matching the table's Stim labels and, for each brain,\n    the median over level-6 regions of the absolute relative difference from the table's density\n    of the matched subject is within 10% (the protocol's default tolerance). Partially reproduced\n    when the groups match but fewer than 10 of the 14 brains meet the 10% bound. The per-brain\n    correlation over regions is reported. The table is outside data (Figshare\n    doi:10.6084/m9.figshare.27642768.v1).\n- id: fig2c-brain-wide-increase\n  statement: TRAP-labeled (tdTomato+) cell density increases brain-wide when 4-OHT is given after\n    male ejaculation, compared with the appetitive phase.\n  source: Results, Brain-wide mapping of neural response to male ejaculation, paragraph 1; Figure\n    2C and 2D\n  quote: As a result, we found the level of tdTomato expression increased in a brain-wide manner\n    during the post-ejaculatory period when compared to the appetitive phase\n  data: with_inputs\n  criterion: Method from the Methods (Brain-wide analysis) and the Figure 2 legend, with the code\n    where they are silent. Per brain, tdTomato+ cells per atlas region (Unified Anatomical Atlas,\n    Kim lab, outside data; Figure 2.ipynb reads its label table\n    atlas_info_KimRef_FPbasedLabel_v2.9) divided by region volume (cells per mm3), at hierarchy\n    level 4. Per region a one-way ANOVA over the three groups (appetitive n=4, consummatory n=5,\n    post-ejaculatory n=5), Benjamini-Hochberg correction at FDR 0.05 (Methods and legend; the\n    code uses 0.1, shown as a variant), then Tukey's HSD (FWER 0.05) post-ejaculatory against\n    appetitive for regions significant in the ANOVA. Open, and named here because it could change\n    the outcome; (1) the level-4 family is the ten regions of the code or the twelve of the Figure\n    2C legend (adding VERM and HEM); (2) region volume is the atlas volume or the region's volume\n    in each brain's own space; the paper gives neither. Supplementary file 2, which lists which\n    regions were significant, is not in the text read, so \"brain-wide\" is read as follows,\n    stated before analysis. Reproduced when the post-ejaculatory mean exceeds the appetitive mean\n    in at least 80% of the level-4 regions of the family and at least half of the family is\n    significant (ANOVA q < 0.05 and Tukey p < 0.05, post-ejaculatory higher). Partially\n    reproduced when the direction holds in at least 80% but fewer than half are significant. Not\n    reproduced otherwise. Every reading is run; when they give different outcomes the claim is\n    blocked as methods_underspecified.\n- id: fig2ei-social-regions-higher\n  statement: Regions known for social behavior, including the paraventricular hypothalamic areas\n    (PVHd, PVH, PaV), the medial amygdala and the BNST, have significantly higher tdTomato+\n    density in the post-ejaculatory group than in the appetitive group.\n  source: Results, Brain-wide mapping of neural response to male ejaculation, paragraph 1; Figure\n    2E to 2H; Figure 2-figure supplement 2\n  quote: regions well known to be related to social behavior had significantly higher tdTomato\n    density in the post-ejaculatory group compared to appetitive group ... This includes\n    paraventricular hypothalamic areas (PVHd, PVH, PaV) which are important for endocrinological\n    regulations, medial amygdala (MeA) which is critical for olfactory sensory information\n    processing, and the BNST\n  data: with_inputs\n  depends_on:\n  - fig2c-brain-wide-increase\n  criterion: Densities as in fig2c-brain-wide-increase, at hierarchy level 6. Per region a one-way\n    ANOVA over the three groups with Benjamini-Hochberg correction at FDR 0.10 over the level-6\n    family (Methods; Figure 2-figure supplement 2 legend), then Tukey's HSD at FWER 0.05 (Methods;\n    p-values from scipy tukey_hsd as in Figure 2.ipynb). A region is significantly higher when q <\n    0.10, Tukey p < 0.05 and the post-ejaculatory mean is higher. The medial amygdala is the\n    atlas label Me (Figure 2H legend); the other names are matched to atlas acronyms at level 6,\n    or at the nearest level that holds them when level 6 does not (open; named before analysis).\n    The level-6 family is (a) the code's, regions under the ten level-4 regions, or (b) all\n    level-6 regions. Reproduced when all five regions (PVHd, PVH, PaV, Me, BNST) are\n    significantly higher under the readings; partially reproduced for three or four; not\n    reproduced below three. Per-region q and Tukey p are reported.\n- id: fig2-mpn-higher\n  statement: The medial preoptic nucleus (MPN) has significantly higher tdTomato+ density in the\n    post-ejaculatory group than in the appetitive group.\n  source: Results, Brain-wide mapping of neural response to male ejaculation, paragraph 1; Figure\n    2F and 2H\n  quote: The medial preoptic area nucleus (MPN), a subregion of the MPOA, had significantly higher\n    tdTomato density in the post-ejaculatory group compared to the appetitive group\n  data: with_inputs\n  depends_on:\n  - fig2c-brain-wide-increase\n  criterion: As in fig2ei-social-regions-higher, for the atlas region MPN. Reproduced when the\n    level-6 ANOVA q < 0.10 (under both family readings) and Tukey's HSD post-ejaculatory against\n    appetitive p < 0.05 with the post-ejaculatory mean higher. Partially reproduced when Tukey p\n    < 0.05 but q >= 0.10. The density ratio of the two group means is reported.\n- id: fig2f-mpn-fourth-largest\n  statement: The MPN shows the fourth largest difference in mean tdTomato+ density between the\n    post-ejaculatory and appetitive groups among all brain regions.\n  source: Results, Brain-wide mapping of neural response to male ejaculation, paragraph 1; Figure\n    2F\n  quote: The MPN also had the fourth largest difference of density between the post-ejaculatory\n    group and appetitive group among all the brain regions\n  data: with_inputs\n  depends_on:\n  - fig2c-brain-wide-increase\n  expected:\n  - quantity: rank of the MPN by post-ejaculatory minus appetitive mean density\n    value: 4\n    tolerance: 0\n  criterion: Difference is the post-ejaculatory group mean minus the appetitive group mean of\n    density (Figure 2F, \"difference of average tdTomato density\"). The set ranked is open; the\n    readings the text allows are (a) the level-6 family of the code, (b) all level-6 regions,\n    (c) all atlas regions at every level. The rank is a reported count (tolerance 0); the claim\n    is reproduced when the MPN ranks fourth under one reading. The ranks under every reading and\n    the three regions above the MPN are shown.\n- id: fig2gh-consummatory-tendency\n  statement: The consummatory group tends to have higher MPN tdTomato+ density than the appetitive\n    group, without reaching significance.\n  source: Results, Brain-wide mapping of neural response to male ejaculation, paragraph 1; Figure\n    2G and 2H\n  quote: While it was not statistically significant, the consummatory group also tended to have a\n    larger tdTomato density than the appetitive group in the MPN as well\n  data: with_inputs\n  depends_on:\n  - fig2c-brain-wide-increase\n  criterion: For the MPN, Tukey's HSD consummatory against appetitive (FWER 0.05), as in Figure 2G\n    and Figure 2.ipynb. The absence part is judged on that test alone; the claim is reproduced\n    when Tukey p >= 0.05 and the consummatory mean is above the appetitive mean; partially\n    reproduced when p >= 0.05 and the mean is not higher; not reproduced when p < 0.05. The mean\n    difference and p are reported.\n- id: fig2s-dorsal-raphe\n  statement: The whole-brain mapping indicates increased TRAP labeling in the dorsal raphe after\n    male ejaculation.\n  source: Discussion, Neural circuitry for female sexual behavior regulation, last paragraph;\n    Figure 2-figure supplement 1 and 2\n  quote: Our whole brain activity mapping data also indicates increased ... Fos activity in the\n    dorsal raphe\n  data: with_inputs\n  depends_on:\n  - fig2c-brain-wide-increase\n  criterion: For the atlas dorsal raphe region at level 6 (DR, or the label the atlas gives it),\n    as in fig2ei-social-regions-higher. Reproduced when the post-ejaculatory mean exceeds the\n    appetitive mean and the ANOVA q < 0.10 (the significance marked in Figure 2-figure supplement\n    2); partially reproduced when the mean is higher but q >= 0.10.\n- id: fig1gh-transitions-isolation\n  statement: In hormone-primed females, zone transitions decrease and time in the isolation zone\n    increases after male ejaculation, compared with before ejaculation and with the control trial.\n  source: Figure 1G and 1H; Results, Female sexual motivation is suppressed after male\n    ejaculation, paragraph 2\n  quote: we found that there was a significant decrease in the number of zone transitions as well\n    as a significant increase in the time spent in the isolation zone after male ejaculation\n  statistics:\n  - about: transitions per 10 min, three epochs\n    test: RM ANOVA\n    statistic: F(2,16)=10.89\n    p: 0.001035889\n    n: 9 mice\n  - about: transitions, post against pre\n    test: Tukey's HSD\n    p: 0.0142\n    n: 9 mice\n  - about: transitions, control against post\n    test: Tukey's HSD\n    p: 0.0015\n    n: 9 mice\n  - about: time in isolation zone, three epochs\n    test: RM ANOVA\n    statistic: F(2,16)=14.34\n    p: 0.00027\n    n: 9 mice\n  - about: time in isolation zone, post against pre\n    test: Tukey's HSD\n    p: 0.0057\n    n: 9 mice\n  - about: time in isolation zone, control against post\n    test: Tukey's HSD\n    p: 0.0004\n    n: 9 mice\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: As in the Figure 1 legend and Figure 1.ipynb; repeated-measures ANOVA (statsmodels\n    AnovaRM) over control, pre- and post-ejaculation, then Tukey's HSD (FWER 0.05). Reproduced\n    when both ANOVAs have p < 0.05 and post differs from pre and from control in the stated\n    direction at p < 0.05.\n- id: fig1i-latency-return\n  statement: Latency to return to the interaction zone is longest after male ejaculation, longer\n    than after sniffing or mounting.\n  source: Figure 1I; Results, Female sexual motivation is suppressed after male ejaculation,\n    paragraph 2\n  quote: This was the largest after the female experienced male ejaculation when compared to after\n    sniffing or after mounting\n  statistics:\n  - test: RM ANOVA\n    statistic: F(2,16)=11.87\n    p: 0.00069052\n    n: 9 mice\n  - about: ejaculation against sniff\n    test: Tukey's HSD\n    p: 0.0016\n  - about: ejaculation against mount\n    test: Tukey's HSD\n    p: 0.0077\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: RM ANOVA then Tukey's HSD as in the Figure 1 legend. Reproduced when ejaculation\n    latency exceeds both others at p < 0.05.\n- id: fig1jm-behaviors-after-ejaculation\n  statement: After ejaculation, female-to-male sniffing does not change, while mounting and\n    intromission decrease and self-grooming increases (hormone-primed females).\n  source: Figure 1J to 1M; Results, Female sexual motivation is suppressed after male ejaculation,\n    paragraph 2\n  quote: while there was no change in the amount of female-to-male sniffing, there was a\n    significant decrease in the number of mounting and intromission episodes ... There was also a\n    significant increase in the number of self-grooming behavioral episodes\n  statistics:\n  - about: sniffing\n    test: Wilcoxon signed-rank test\n    p: 0.65234375\n    n: 9 mice\n  - about: mounting\n    test: Wilcoxon signed-rank test\n    p: 0.00390625\n    n: 9 mice\n  - about: intromission\n    test: Wilcoxon signed-rank test\n    p: 0.00390625\n    n: 9 mice\n  - about: self-grooming\n    test: Wilcoxon signed-rank test\n    p: 0.025061844\n    n: 9 mice\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: Two-sided Wilcoxon signed-rank test pre against post on counts per 10 min (legend;\n    Figure 1.ipynb, scipy wilcoxon). Reproduced when mounting and intromission decrease and\n    grooming increases at p < 0.05, and sniffing is not significant (the absence judged on this\n    test).\n- id: fig1nt-natural-estrus\n  statement: Naturally cycling estrus females show the same post-ejaculatory changes, with a strong\n    reduction of sniffing and no change in self-grooming.\n  source: Figure 1N to 1T; Results, Female sexual motivation is suppressed after male ejaculation,\n    paragraph 2\n  quote: Animals that were in their natural estrus cycle showed similar behavior changes after\n    experiencing male ejaculation ... showed a strong reduction of sniffing after experiencing\n    male ejaculation but no changes in self-grooming behaviors\n  statistics:\n  - about: transitions\n    test: RM ANOVA\n    statistic: F(2,10) = 7.54\n    p: 0.01007\n    n: 6 mice\n  - about: transitions, post against pre\n    test: Tukey's HSD\n    p: 0.0038\n  - about: time in isolation zone\n    test: RM ANOVA\n    statistic: F(2,10) = 15.71\n    p: 0.00082\n    n: 6 mice\n  - about: latency to return\n    test: RM ANOVA\n    statistic: F(2,10) = 38.36\n    p: 0.00002\n    n: 6 mice\n  - about: sniffing\n    test: Wilcoxon signed-rank test\n    p: 0.03125\n  - about: self-grooming\n    test: Wilcoxon signed-rank test\n    p: 0.3452\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: Tests as in the Figure 1 legend (RM ANOVA and Tukey's HSD for N to P; Wilcoxon\n    signed-rank for Q to T). Reproduced when the three ANOVAs and sniffing are significant at p <\n    0.05 and grooming is not.\n- id: fig1s1-experience\n  statement: Virgin females make fewer entries into, and spend more time in, the isolation zone\n    than sexually experienced females.\n  source: Figure 1-figure supplement 1; Results, Female sexual motivation is suppressed after male\n    ejaculation, paragraph 2\n  quote: the virgin female mice stayed in the isolation zone significantly longer than sexually\n    experienced females\n  statistics:\n  - about: isolation zone entries\n    test: Mann-Whitney U test\n    p: 0.041125541\n    n: 6 virgin and 6 experienced mice\n  - about: time in isolation zone\n    test: Mann-Whitney U test\n    p: 0.025974026\n    n: 6 virgin and 6 experienced mice\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: Two-sided Mann-Whitney U test (legend; Figure S1.ipynb). Reproduced when the time\n    difference is significant at p < 0.05 in the stated direction. The legend does not state the\n    direction of the entries difference, which is reported.\n- id: fig1s2-novel-male\n  statement: The post-ejaculatory reduction in sexual motivation does not depend on the state of\n    the male; with a novel sexually active male after ejaculation, females still make fewer\n    isolation zone entries and spend more time there.\n  source: Figure 1-figure supplement 2; Results, Female sexual motivation is suppressed after male\n    ejaculation, paragraph 2\n  quote: When the female animal was introduced to a novel sexually motivated male animal\n    immediately after they experienced male ejaculation from another mouse, they showed a similar\n    reduction in zone transition and an increase in the time spent in the isolation zone\n  statistics:\n  - about: isolation zone entries\n    test: Wilcoxon signed-rank test\n    p: 0.027281171\n    n: 7 mice\n  - about: time in isolation zone\n    test: Wilcoxon signed-rank test\n    p: 0.027707849\n    n: 7 mice\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: Two-sided Wilcoxon signed-rank test, pre- against post-ejaculation assay (legend;\n    Figure S2.ipynb). Reproduced when both are significant at p < 0.05 in the stated direction.\n- id: fig3d-mpn-fos\n  statement: By HCR, the proportion of Fos+ cells is higher after ejaculation than in the\n    appetitive group in the MPN but not in nearby regions (MPA, BNST, LPO, VLPO).\n  source: Figure 3D; Results, Male ejaculation is represented by both inhibitory and excitatory\n    cell types in the MPOA, paragraph 2\n  quote: we found that the number of Fos + cells in the post-ejaculatory group was significantly\n    higher than the appetitive group in the MPN but not in the nearby regions\n  statistics:\n  - about: MPN\n    test: Student's t-test\n    statistic: t(8)=-4.2709\n    p: 0.0136\n    corrected: Bonferroni\n    n: 5 appetitive and 5 post-ejaculatory mice\n  - about: MPA\n    test: Student's t-test\n    statistic: t(8)=-1.841\n    p: 0.514\n    corrected: Bonferroni\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: Student's t-test with Bonferroni correction over the five regions (legend; Figure\n    S5.ipynb, scipy ttest_ind and multipletests). Reproduced when only the MPN is significant at\n    corrected p < 0.05, higher after ejaculation.\n- id: fig3i-vgat-vglut2-fos\n  statement: In the MPN, both Vglut2+ and Vgat+ cells expressing Fos increase after ejaculation,\n    with a higher proportion of Fos+ cells in the Vgat population.\n  source: Figure 3I; Results, Male ejaculation is represented by both inhibitory and excitatory\n    cell types in the MPOA, paragraph 2\n  quote: Vglut2 and Vgat cells expressing Fos were significantly higher in the post-ejaculatory\n    group than in the appetitive group, suggesting that male ejaculation activates both\n    excitatory and inhibitory neurons ... The proportion of Fos+ cells was higher in the Vgat\n    population\n  statistics:\n  - about: Vglut2\n    test: Student's t-test\n    statistic: t(8)=-3.3885\n    p: 0.019\n    corrected: Bonferroni\n  - about: Vgat\n    test: Student's t-test\n    statistic: t(8)=-3.5361\n    p: 0.0153\n    corrected: Bonferroni\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: As in the Figure 3 legend. Reproduced when both are significant at corrected p < 0.05\n    and the post-ejaculatory Fos+ proportion is higher in Vgat than in Vglut2 cells (no test is\n    reported for the latter, so it is judged on the means).\n- id: fig3jm-cell-types\n  statement: Fos induction after ejaculation is found in Vglut2 cells only when they co-express\n    Calcr, and in Vgat cells co-expressing Calcr, Gal or Prlr; among clusters, the Vglut2, Vgat\n    and Gal types have more Fos+ cells after ejaculation, while the Nts type does not.\n  source: Figure 3J to 3M; Results, Male ejaculation is represented by both inhibitory and\n    excitatory cell types in the MPOA, paragraph 2\n  quote: in the Vglut2 cells, we found that Fos induction was only observed in the cells that\n    co-expressed Calcr ... Type 1 ... and type 3 ... had significantly more Fos+ cells from the\n    post-ejaculatory group compared to the appetitive group ... In contrast, Fos+ cells were not\n    induced in type 4\n  statistics:\n  - about: Vgat+ Calcr+\n    test: Student's t-test\n    statistic: t(8)=-3.6646\n    p: 0.0318\n    corrected: Bonferroni\n  - about: Vgat+ Gal+\n    test: Student's t-test\n    statistic: t(8)=-4.0896\n    p: 0.0174\n    corrected: Bonferroni\n  - about: Vgat+ Prlr+\n    test: Student's t-test\n    p: 0.0212\n    corrected: Bonferroni\n  - about: Vglut2+ Calcr+\n    test: Student's t-test\n    p: 0.0146\n    corrected: Bonferroni\n  - about: cluster Vglut2\n    test: Student's t-test\n    statistic: t(8)=-4.1631\n    p: 0.0189\n    corrected: Bonferroni\n  - about: cluster Vgat\n    test: Student's t-test\n    statistic: t(8)=-5.9018\n    p: 0.0022\n    corrected: Bonferroni\n  - about: cluster Gal\n    test: Student's t-test\n    statistic: t(8)=-3.9208\n    p: 0.0265\n    corrected: Bonferroni\n  - about: cluster Nts\n    test: Student's t-test\n    statistic: t(8)=-2.1595\n    p: 0.377\n    corrected: Bonferroni\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: Student's t-tests with Bonferroni correction as in the Figure 3 legend; clusters from\n    Seurat 3.1.1 as in the Methods and Figure S5_Seurat clustering.R. The legend prints t(8)=-3.9487\n    for every Vglut2 row and for Vgat+ Prlr+, so those statistics are not recorded. Reproduced\n    when the named groups are significant at corrected p < 0.05 and the Nts cluster is not.\n- id: fig4h-response-magnitude\n  statement: Vgat cells show higher average response magnitude than Vglut2 cells after sniffing,\n    self-grooming, male anogenital sniffing and ejaculation, but not after mounting or\n    intromission.\n  source: Figure 4H; Results, A subpopulation of MPOA Vgat cells responds to male ejaculation,\n    paragraph 1\n  quote: Vgat cells showed significantly higher average response magnitude after sniffing,\n    self-grooming, anogenital sniffing, and male ejaculation than the Vglut2 cells\n  statistics:\n  - about: ejaculation\n    test: Student's t-test\n    statistic: t(791)=4.00\n    p: 0.00042\n    corrected: Bonferroni\n    n: 522 Vgat and 271 Vglut2 cells\n  - about: sniff\n    test: Student's t-test\n    statistic: t(791)=6.46\n    p: 1.08e-09\n    corrected: Bonferroni\n  - about: mount\n    test: Student's t-test\n    statistic: t(791)=0.34\n    p: 1\n    corrected: Bonferroni\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: Per cell, z-scored signal (z-scored on the background period) from -5 to +15 s around\n    each onset, averaged over events, baseline (-5 to 0 s) subtracted, magnitude the mean of 0 to\n    +5 s (Methods). The Results say \"for 15 s after behavior onset\"; the Methods' 0 to 5 s is\n    followed. Student's t-test per behavior with Bonferroni correction (legend; Figure 3, 4, 5,\n    S6, S7, S8.ipynb). Grooming has t = -7.25, that is Vgat lower, against the Results sentence;\n    the sign is reported. Reproduced when ejaculation and sniff are significant with Vgat higher\n    and mount and intromission are not.\n- id: fig4i-ejaculation-responders\n  statement: A larger proportion of Vgat than Vglut2 cells respond positively to ejaculation\n    (184/522 against 35/271) and to sniffing (29/522 against 1/271).\n  source: Figure 4I; Results, A subpopulation of MPOA Vgat cells responds to male ejaculation,\n    paragraph 1\n  quote: Vgat cells also contained a significantly higher proportion of cells that positively\n    respond (>2δ) to sniff and male ejaculation onset\n  statistics:\n  - about: ejaculation\n    test: chi-square test\n    p: 1.52e-10\n    corrected: Bonferroni\n    n: 522 Vgat and 271 Vglut2 cells\n  - about: sniff\n    test: chi-square test\n    p: 0.00169\n    corrected: Bonferroni\n  expected:\n  - quantity: Vgat cells responding positively to ejaculation\n    value: 184\n    tolerance: 18.4\n    unit: cells\n  - quantity: Vglut2 cells responding positively to ejaculation\n    value: 35\n    tolerance: 3.5\n    unit: cells\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: Responding when the magnitude of fig4h-response-magnitude exceeds 2 (abs value above\n    2 in the code, sign giving positive or negative). Chi-square test of proportions\n    (statsmodels proportions_chisquare) with Bonferroni correction, as in the code.\n- id: fig5-ejaculation-specific\n  statement: Among cells responding to sniff, mount or ejaculation, ejaculation-specific cells are\n    the most numerous (177, against 46 mount and 12 sniff), and most ejaculation responders are\n    specific (Vgat 80%, Vglut2 82%).\n  source: Results, A subpopulation of MPOA Vgat cells responds to male ejaculation, paragraph 2;\n    Figure 5A to 5D\n  quote: the number of cells that specifically responded was largest to male ejaculation with 177\n    cells, next to mount with 46 cells, and to sniff with 12 cells\n  expected:\n  - quantity: ejaculation-specific cells\n    value: 177\n    tolerance: 17.7\n  - quantity: mount-specific cells\n    value: 46\n    tolerance: 4.6\n  - quantity: sniff-specific cells\n    value: 12\n    tolerance: 1.2\n  - quantity: proportion of Vgat ejaculation responders that are specific\n    value: 0.80\n    tolerance: 0.08\n  - quantity: proportion of Vglut2 ejaculation responders that are specific\n    value: 0.82\n    tolerance: 0.082\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: The Figure 5 legend gives n=48 mount and 178 ejaculation cells, against 46 and 177 in\n    the Results; both are readings. \"Specific\" is read as (a) positive (>2) to that behavior only,\n    among sniff, mount and ejaculation (code columns BEHAVIOR_only_cells), or (b) the\n    magnitude_cell_types class of the legend (\"categorized based on response magnitude\"). The\n    counts hold if they match under one reading.\n- id: fig6c-decay-length\n  statement: Ejaculation-responding Vgat cells have a longer decay length than Vglut2 cells.\n  source: Figure 6C; Results, MPOA Vgat cells display prolonged activity, paragraph 1\n  quote: Vgat cells had significantly longer decay length compared to the Vglut2 cells\n  statistics:\n  - test: Student's t-test\n    statistic: t(217)=3.039653717\n    p: 0.002659548\n    n: 184 Vgat and 35 Vglut2 cells\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: Signal from -5 to +120 s around ejaculation onset, baseline (-5 to 0 s) subtracted\n    (Methods). Decay length is \"the time the z-scored signal was smaller than 0\" (Methods) or\n    \"the time for the increased calcium signal to return to baseline\" (Results); the code reads\n    it precomputed. Readings, (a) time from onset to the first sample below 0, (b) total time\n    below 0 in 0 to 120 s. Student's t-test (scipy ttest_ind). Reproduced when Vgat is longer at p\n    < 0.05 under the readings.\n- id: fig6k-late-cluster-vgat\n  statement: Spectral clustering of ejaculation responses gives five types; the late-response type\n    3 has the longest decay length and contains only Vgat cells, while Vglut2 cells are more\n    often fast responders.\n  source: Figure 6D to 6K; Results, MPOA Vgat cells display prolonged activity, paragraph 1\n  quote: all the cells in type 3 were Vgat cells, suggesting that the increased activity in the\n    MPOA late after the onset of male ejaculation is mediated by inhibitory neurons\n  statistics:\n  - about: type 3\n    test: chi-square test\n    p: 0.018\n    corrected: Bonferroni\n    n: 37/184 Vgat and 0/35 Vglut2 cells\n  - about: type 1\n    test: chi-square test\n    p: 6.80e-05\n    corrected: Bonferroni\n    n: 26/184 Vgat and 16/35 Vglut2 cells\n  expected:\n  - quantity: Vglut2 cells in the late-response cluster\n    value: 0\n    tolerance: 0\n    unit: cells\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: PCA of the -5 to +120 s traces, 4 components, spectral clustering with the number of\n    clusters and nearest neighbours chosen by maximal silhouette score (5 clusters, 55 neighbours,\n    silhouette 0.405, cosine metric in Figure 5 Spectral clustering.ipynb). Reproduced when the\n    cluster with the latest response and longest decay holds no Vglut2 cells and its Vgat\n    proportion differs at corrected p < 0.05.\n- id: fig7fg-activation-suppresses\n  statement: CNO activation of post-ejaculatory TRAP-labeled MPOA neurons reduces zone transitions\n    and increases time in the isolation zone; activation of appetitive or consummatory ensembles\n    and eYFP controls do not.\n  source: Figure 7F and 7G; Results, An activity-defined subset of neurons in the MPOA, paragraph 4\n  quote: only post-ejaculatory-hM3Dq group showed significantly fewer number of transitions and\n    spent more time in the isolation zone on the CNO trial than on the saline trial\n  statistics:\n  - about: transitions, post-ejaculatory-hM3Dq\n    test: Wilcoxon rank sum test\n    p: 0.03125\n    corrected: Bonferroni\n    n: 8 mice\n  - about: isolation time, post-ejaculatory-hM3Dq\n    test: Wilcoxon rank sum test\n    p: 0.03125\n    corrected: Bonferroni\n    n: 8 mice\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: Saline against CNO trial within each group, Bonferroni over the four groups. The\n    legend names a Wilcoxon rank sum test; Figure 6.ipynb runs scipy wilcoxon (paired signed-rank),\n    and 0.03125 is 4 times the smallest two-sided signed-rank p for 8 mice. Methods first; the\n    rank-sum test is the main reading and the signed-rank test is the variant. Reproduced when\n    only post-ejaculatory-hM3Dq is significant at corrected p < 0.05 in both measures.\n- id: fig7kl-activation-intromission\n  statement: Activation of post-ejaculatory TRAP neurons lowers intromissions and receptivity in\n    the self-paced assay; the text also reports fewer self-grooming and mounting episodes, which\n    the legend gives as p = 0.0625.\n  source: Figure 7H to 7L; Results, An activity-defined subset of neurons in the MPOA, paragraph 4\n  quote: post-ejaculatory-hM3Dq group displayed fewer numbers of self-grooming, mounting,\n    intromission and lower receptivity score on the CNO trial than on the saline trial\n  statistics:\n  - about: intromission\n    test: Wilcoxon rank sum test\n    p: 0.03125\n    corrected: Bonferroni\n  - about: receptive score\n    test: Wilcoxon rank sum test\n    p: 0.03125\n    corrected: Bonferroni\n  - about: self-grooming\n    test: Wilcoxon rank sum test\n    p: 0.0625\n    corrected: Bonferroni\n  - about: mount\n    test: Wilcoxon rank sum test\n    p: 0.0625\n    corrected: Bonferroni\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: Tests as in fig7fg-activation-suppresses. Reproduced when intromission and receptive\n    score are lower on CNO at corrected p < 0.05; grooming and mounting are reported.\n- id: fig7s1-mpn-proportion\n  statement: The number of TRAP-labeled cells does not differ between groups, but the proportion\n    located in the MPN is higher in the post-ejaculatory group; most MPN TRAP cells are Vgat (0.76)\n    and few Vglut2 (0.15).\n  source: Figure 7-figure supplement 1B, 1C and 1G; Results, An activity-defined subset of neurons\n    in the MPOA, paragraph 1\n  quote: while the overall number of TRAP-labeled cells had no difference between the\n    post-ejaculatory groups, consummatory group and appetitive group, the proportion of cells\n    located in the MPN was significantly higher in the post-ejaculatory group ... (Vgat\n    0.76±0.16. Vglut2 0.15±0.13)\n  statistics:\n  - about: number of TRAP cells\n    test: one-way ANOVA\n    statistic: F(2,24)=0.3072\n    p: 0.7383\n  - about: proportion in the MPN\n    test: one-way ANOVA\n    statistic: F(2,24)=4.3335\n    p: 0.0247\n  - about: proportion in the MPN, appetitive against post-ejaculatory\n    test: Tukey HSD\n    p: 0.0471\n    n: 7 appetitive and 14 post-ejaculatory mice\n  expected:\n  - quantity: proportion of MPN TRAP cells that are Vgat\n    value: 0.76\n    tolerance: 0.16\n  - quantity: proportion of MPN TRAP cells that are Vglut2\n    value: 0.15\n    tolerance: 0.13\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: One-way ANOVA and Tukey HSD as in the legend (Figure S9.ipynb, pairwise_tukeyhsd).\n    Tolerances are the stated spread. Reproduced when the count ANOVA is not significant and the\n    MPN proportion is, post-ejaculatory above appetitive at p < 0.05.\n- id: fig7s2-home-cage-activation\n  statement: In the home cage, activation of post-ejaculatory TRAP neurons reduces sniffing and\n    intromission compared with post-ejaculatory eYFP controls, without changing mounting; it does\n    not induce place preference or aversion.\n  source: Figure 7-figure supplement 2C to 2J; Results, An activity-defined subset of neurons in the\n    MPOA, paragraphs 3 and 4\n  quote: post-ejaculatory-hM3Dq group but not the appetitive-hM3Dq and consummatory-hM3Dq group\n    showed significantly fewer sniffing events compared to post-ejaculatory-eYFP group ... there\n    were significantly less intromission episodes\n  statistics:\n  - about: sniff\n    test: Mann-Whitney U test\n    p: 0.0072\n    corrected: Bonferroni\n  - about: intromission\n    test: Mann-Whitney U test\n    p: 0.0165\n    corrected: Bonferroni\n  - about: mounting\n    test: Mann-Whitney U test\n    p: 0.4116\n    corrected: Bonferroni\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: Each hM3Dq group against post-ejaculatory-eYFP by Mann-Whitney U test with Bonferroni\n    correction (legend; Figure S10.ipynb). Reproduced when sniff and intromission are significant\n    for post-ejaculatory-hM3Dq only, and mounting and the place preference measures are not.\n- id: fig7s3-inhibition\n  statement: Chemogenetic inhibition of post-ejaculatory TRAP neurons does not change behavior in\n    the self-paced assay, but increases intromission and receptivity in the home cage assay.\n  source: Figure 7-figure supplement 3; Results, An activity-defined subset of neurons in the MPOA,\n    paragraph 5\n  quote: the post-ejaculatory-hM4Di group experienced did not show significant changes in\n    sniffing, self-grooming, or mounting, but showed more intromission and higher sexual\n    receptivity than in the post-ejaculatory-eYFP group\n  statistics:\n  - about: home cage intromission\n    test: Mann-Whitney U test\n    p: 0.0045\n    n: 6 eYFP and 8 hM4Di mice\n  - about: home cage receptive score\n    test: Mann-Whitney U test\n    p: 0.01998\n    n: 6 eYFP and 8 hM4Di mice\n  data: elsewhere\n  where: Figshare doi:10.6084/m9.figshare.27642768.v1\n  criterion: Mann-Whitney U test for the home cage (legend, O to R); for the self-paced assay the\n    test of the legend, Wilcoxon with Bonferroni correction (E to L), with no measure significant.\n    Reproduced when both home cage measures are higher at p < 0.05 and no self-paced measure is\n    significant.\n"
}
```

```
File created successfully at: claims/001249/10.7554-elife.91765.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001249/10.7554-elife.91765.yaml paper/10.7554-elife.91765.txt; grep -n -E "—|rather" claims/001249/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

The five values not found are printed in the text as I recorded them (e.g. "p=0.001035889", "6.80E-05"); the checker's number formatting just doesn't produce those forms. Fixing the one quote.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001249/10.7554-elife.91765.yaml",
 "old_string": "  quote: while the overall number of TRAP-labeled cells had no difference between the\n    post-ejaculatory groups, consummatory group and appetitive group, the proportion of cells\n    located in the MPN was significantly higher in the post-ejaculatory group ... (Vgat\n    0.76±0.16. Vglut2 0.15±0.13)",
 "new_string": "  quote: \"while the overall number of TRAP-labeled cells had no difference between the\n    post-ejaculatory groups, consummatory group and appetitive group, the proportion of cells\n    located in the MPN was significantly higher in the post-ejaculatory group ... most\n    TRAP-labeled cells in the MPN were Vgat (Vgat: 0.76±0.16. Vglut2: 0.15±0.13)\""
}
```

```
The file claims/001249/10.7554-elife.91765.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001249/10.7554-elife.91765.yaml paper/10.7554-elife.91765.txt; grep -c -E "0.001035889|0.65234375|0.027281171|0.002659548|6.80E-05" paper/10.7554-elife.91765.txt; grep -o -E "p=0.001035889|p=0.65234375|p=0.027281171|p=0.002659548|p=6.80E-05" paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/001249/10.7554-elife.91765.yaml` and nothing is committed. The checker validates the file and finds all 26 quotes word for word. It flags 5 p-values it can't find, but I confirmed by reading that each is in the text as recorded (for example "p=0.001035889" and "p=6.80E-05"); the checker just doesn't generate those number formats.

**Text read**
- **Paper:** the eLife version of record (RP91765, 5 March 2025) from Europe PMC: main text, all figure and figure-supplement legends, Methods, and the authors' response to reviewers. Supplementary files 1 to 3, the tables of statistical results, are not in it.
- **Code:** github.com/stuberlab/Ishii-MPOA-Ejaculation-2023 at commit 4e98c43. The notebooks use the preprint's figure numbers; `Figure 2.ipynb` is the whole-brain analysis. It starts from densities already computed (`tdTomato_summary.csv` on Figshare). The image registration and cell-segmentation steps are not in the repository.
- **Dataset:** it holds only the Figure 2 whole-brain FosTRAP mapping: 14 brains, 4 appetitive, 5 consummatory and 5 post-ejaculatory. Everything else is on Figshare (doi:10.6084/m9.figshare.27642768.v1), so 19 claims are marked `elsewhere`.

**Counts**
- 26 claims: 1 link and 25 findings. The link checks that densities computed from the dandiset match the deposited `tdTomato_summary.csv`.
- All 26 have quotes and criteria, 18 have statistics (57 values), and 5 have expected values.
- The 7 claims on Figure 2 data are marked `with_inputs`, because they need the Kim lab Unified Anatomical Atlas (Chon et al. 2019) and the deposited density table, which come from outside the dandiset.

**Open details and the readings named**
- **Level-4 region set (Figure 2C):** the code uses 10 regions; the legend lists 12 (adding VERM and HEM).
- **Level-6 region set:** the code's (the regions under those 10), or all level-6 regions.
- **FDR threshold at level 4:** the Methods and legend say 0.05; the code uses 0.1. I followed the Methods and kept the code's value as a variant.
- **Tukey's test:** the Methods run it only on regions that pass the ANOVA; the code runs it on all. The p-values are the same, so significance requires both.
- **Region volume used for density:** the atlas volume, or each brain's own region volume.
- **Cell classifier:** the trained ilastik classifier is not deposited, so it has to be retrained as the Methods describe.
- **"Brain-wide" (Figure 2C):** Supplementary file 2, which lists the significant regions, is missing. The criterion sets the bar at the post-ejaculatory mean being higher in at least 80% of level-4 regions, with at least half significant. That threshold is my reading, not the paper's.
- **"Fourth largest difference" for the MPN:** ranked among the code's level-6 set, all level-6 regions, or all regions at every level.
- **Atlas names:** matching PVHd, PVH, PaV and MeA (atlas label "Me") to atlas regions, at the nearest level that holds them.
- **Other experiments:**
  - Decay length: time to first fall below 0, or total time below 0.
  - Response window: the Results say 15 s; the Methods average 0 to 5 s, which I followed.
  - Specific-cell counts: 177 and 46 in the Results, 178 and 48 in the legend; and two definitions of "specific".
  - The Figure 7 test: the legend says Wilcoxon rank sum; the code runs a paired signed-rank test. Rank sum is the main reading and signed-rank the variant.

**Missing from the paper**
- Supplementary files 1 to 3, so the per-region ANOVA and Tukey statistics for Figure 2 are not recorded.
- The image-processing pipeline and trained classifier are not in the paper or its code.
- The Figure 3J legend prints t(8)=-3.9487 for every Vglut2 row and for Vgat+ Prlr+, so I left those statistics out.

## End of run

23 turns, 5 minutes, result: success.
