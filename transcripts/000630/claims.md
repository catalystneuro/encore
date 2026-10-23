# 000630 · claims · run 39919299770

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls claims/001453/ paper/ claims/000630 2>&1; ls tools
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
cd paper; wc -l *.txt; head -30 10.1126-science.adf0805.txt; echo ----; head -30 10.1101-2022.10.24.511199.txt; ls -la
```

```
<persisted-output>
Output too large (64.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a3755e17-d35b-4643-a18a-c877f188f904/tool-results/b13zv0r21.txt

Preview (first 2KB):
   174 10.1101-2022.10.24.511199.txt
  1639 10.1126-science.adf0805.txt
  1813 total
DOI: 10.1126/science.adf0805
Version: as served by pmc_playwright
Source: pmc_playwright+crossref (paper-text-fetcher)
Stored: 2026-10-21
Extracted: as fetched; with 1 supplement file(s) from PubMed Central, downloaded in a browser (PMC11864503), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
------------------------------------------------------------------------
Skip to main content

An official website of the United States government

Here's how you know
Search
Log in
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.adf0805.txt",
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.adf0805.txt",
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Main text read. Continuing with the Methods and supplement in the text file.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.adf0805.txt",
 "offset": 200,
 "limit": 250
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; grep -n -i "supplement\|materials and methods\|^Fig\. S\|Data S2\|=====\|-----" 10.1126-science.adf0805.txt | sed -n '1,200p' | cut -c1-200
```

```
5:Extracted: as fetched; with 1 supplement file(s) from PubMed Central, downloaded in a browser (PMC11864503), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6:------------------------------------------------------------------------
49:To guide our analysis of L1 cell types, we used transcriptomic types (t-types) previously defined in reference datasets from human middle temporal gyrus (MTG) and mouse primary visual cortex (VISp)
63:We assigned transcriptomic cell types and subclasses to patch-seq samples using a “tree mapping” classifier, a decision tree based on the transcriptomic taxonomy structure (Materials and Methods) (
65:Since patch-seq sampling was not uniform across cortical layers, we also measured the laminar distribution of L1 t-types using a spatially resolved, robust and reliable single-cell profiling techni
69:Organizing the patch-seq dataset by transcriptomic subclass revealed the exceptionally diverse morphology and physiology of human L1 interneurons. Morphologically, subclasses were distinguished by 
75:(A) Example human morphologies for L1 t-types are displayed by subclass. Neurons are shown aligned to an average cortical template, with histograms to the right of the morphologies displaying avera
89:(A) Examples of NeuN labelling of neurons in human MTG and mouse VISp. (B) Comparisons of mouse versus human L1 thickness, neuron density, soma area and neuron count in 1mm wide ROIs of L1. Metrics
165:Supplementary Material
167:NIHMS2048794-supplement-DataS1.xlsx (29KB, xlsx)
169:NIHMS2048794-supplement-DataS2.xlsx (22.7KB, xlsx)
171:NIHMS2048794-supplement-DataS3.xlsx (56.7KB, xlsx)
173:NIHMS2048794-supplement-DataS4.xlsx (23.6KB, xlsx)
175:NIHMS2048794-supplement-5.pdf (5.3MB, pdf)
304:This section collects any data citations, data availability statements, or supplementary materials included in this article.
306:Supplementary Materials
308:NIHMS2048794-supplement-DataS1.xlsx (29KB, xlsx)
310:NIHMS2048794-supplement-Dat
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.adf0805.txt",
 "offset": 575,
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.adf0805.txt",
 "offset": 975,
 "limit": 665
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -rl "xlsx\|Data S[0-9]" claims | head; grep -rn "xlsx" claims | head -20; ls claims | wc -l; grep -n "Data S\|xlsx\|data table\|Source data" docs/*.md | head -30
```

```
claims/001752/10.1038-s41556-026-02009-4.yaml
claims/001692/10.64898-2026.01.20.700614.yaml
claims/001260/10.1038-s41593-025-02190-z.yaml
claims/000971/10.1016-j.cub.2022.01.055.yaml
claims/001750/10.1038-s41556-026-02009-4.yaml
claims/001887/10.1016-j.cub.2025.01.010.yaml
claims/000981/10.1016-j.cub.2026.08.040.yaml
claims/001266/10.1038-s41467-025-55819-9.yaml
claims/000636/10.1126-science.adf6484.yaml
claims/001751/10.1038-s41556-026-02009-4.yaml
claims/001752/10.1038-s41556-026-02009-4.yaml:19:# per-cell summary tables (ephysio/data_ephy/sPSCs_Fig7ab.xlsx and miniEPSCs_Fig7ab.xlsx give one
claims/001752/10.1038-s41556-026-02009-4.yaml:25:#  - The mEPSC sheet (miniEPSCs_Fig7ab.xlsx, sheet mEPSC_sum) heads its first column "VENs" and
claims/001752/10.1038-s41556-026-02009-4.yaml:300:  where: github.com/RFLiu2021/AIC_proj at commit 44cd8a6, morpho/dataMorph/AIScmp_PCvsVEN_Fig5c.xlsx
claims/001752/10.1038-s41556-026-02009-4.yaml:311:    ephysio/data_ephy/PeakIdx_Fig5e.xlsx
claims/001752/10.1038-s41556-026-02009-4.yaml:422:  where: github.com/RFLiu2021/AIC_proj at commit 44cd8a6, ephysio/data_ephy/sumData_StimWM.xlsx
claims/001752/10.1038-s41556-026-02009-4.yaml:451:  where: github.com/RFLiu2021/AIC_proj at commit 44cd8a6, ephysio/data_ephy/sumData_StimWM.xlsx
claims/001752/10.1038-s41556-026-02009-4.yaml:534:    morpho/dataMorph/unSeqCell_morph/morphFeatTables_PC_VENL_VENS.xlsx
claims/001692/10.64898-2026.01.20.700614.yaml:666:  where: Zenodo doi:10.5281/zenodo.18202873, file Bouabid_Vu (2026)_Source_Data_Fig8.xlsx
claims/001692/10.64898-2026.01.20.700614.yaml:707:  where: Zenodo doi:10.5281/zenodo.18202873, file Bouabid_Vu (2026)_Source_Data_Fig8.xlsx
claims/001692/10.64898-2026.01.20.700614.yaml:738:  where: Zenodo doi:10.5281/zenodo.18202873, file Bouabid_Vu (2026)_Source_Data_Fig8.xlsx
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -60 claims/000636/10.1126-science.adf6484.yaml; grep -n "Data S" claims/000636/10.1126-science.adf6484.yaml | head; ls claims/000020 2>/dev/null; ls transcripts | head -3; ls questions | head -3
```

```
# Claims for Lee, Dalley et al. (2023), Science 382, eadf6484, on dandiset 000636.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md (Reader).
#
# Text read. The author manuscript of the version of record in PubMed Central (PMC12229143,
# NIHMS2006139), as text (paper/10.1126-science.adf6484.txt). It has the structured summary,
# the Results, the Discussion, the Materials and Methods and the legends of Figures 1 to 6. It
# does not have the supplementary materials: the legends of figs. S1 to S9 and Data S1 and S2
# are missing, and no PDF was supplied, so no figure could be read. The bioRxiv preprint
# (doi:10.1101/2022.11.08.515739, paper/10.1101-2022.11.08.515739.txt) was read as well. Its
# Results and legends of Supplementary Figures 1 to 5 (an earlier numbering) give some test
# names that the version of record moves to its supplement; where a quote or a method is taken
# from the preprint the claim says so. The preprint has no human versus mouse section. Claims
# that cite figs. S1 to S9 of the version of record rest on the main text sentence that cites
# them, and the features shown in Figure 2H and fig. S8B are not named in any text read.
#
# Code read. github.com/AllenInstitute/human_patchseq_gaba at commit 5eb357a (2023-11-28),
# linked under Data and materials availability. It holds one R notebook
# (scripts_gene_expression/acute_vs_culture_comparisons_update.Rmd; gene-expression analyses,
# the microglial ("immune") signature, the ion-channel gene test, DBC gene tests and the SST
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -12 paper/10.1101-2022.10.24.511199.txt | cut -c1-300; grep -n -i "sag\|rheobase\|r=0\|Pearson\|accuracy" paper/10.1101-2022.10.24.511199.txt | cut -c1-300 | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/AllenInstitute/patchseq_human_L1 && cd patchseq_human_L1 && git log -1 --format='%H %cd' && find . -path ./.git -prune -o -type f -print | head -100
```

```
7777857c1b89b19735e45fd9c9bd7493cc1d805c Tue May 13 13:45:12 2025 -0700
./transcriptomics_r_scripts/slice_affected_genes.txt
./transcriptomics_r_scripts/sex_genes.rda
./transcriptomics_r_scripts/seurat_umap_mouse.rmd
./transcriptomics_r_scripts/seurat_umap_human.rmd
./transcriptomics_r_scripts/prepare_data_mouse.r
./transcriptomics_r_scripts/prepare_data_human.r
./transcriptomics_r_scripts/prepare_data.r
./transcriptomics_r_scripts/mito_genes.rda
./transcriptomics_r_scripts/gene_violins.rmd
./setup.py
./patchseq_utils/zinb_fit.py
./patchseq_utils/util.py
./patchseq_utils/shiny.py
./patchseq_utils/regressions.py
./patchseq_utils/plotting.py
./patchseq_utils/plot_umap.py
./patchseq_utils/plot/sweeps.py
./patchseq_utils/plot/scalebars.py
./patchseq_utils/plot/morphology.py
[... 55 more lines not kept]
```

**Agent**

Code is at github.com/AllenInstitute/patchseq_human_L1, commit 7777857 (2025-05-13). Reading its loading and statistics code and the notebooks behind Figs 2 to 6.

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1 && cat README.md && cat patchseq_utils/l1_load.py | head -250
```

```
# patchseq_human_L1


[![DOI](https://zenodo.org/badge/522633927.svg)](https://zenodo.org/badge/latestdoi/522633927)


Supporting data and code for human L1 patch-seq manuscript: https://www.science.org/doi/10.1126/science.adf0805

No support is intended, but questions are welcome via email to tom.chartrand AT alleninstitute.org

import pandas as pd
from pathlib import Path
from pandas.api.types import CategoricalDtype
from . import shiny
from .util import *


repo_data = Path("../data/")
# datadir = Path("[removed: a home directory path]/projects/data/u01/")
figdir = projectdir/'figures'
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1 && sed -n 250,400p patchseq_utils/l1_load.py; grep -n "^def \|^    def " patchseq_utils/analysis.py patchseq_utils/util.py patchseq_utils/dprime.py patchseq_utils/classification.py patchseq_utils/clustering.py
```

```
patchseq_utils/analysis.py:12:def ols_model(data, formula_rhs, feature, anova_type=2, cov_type='HC3'):
patchseq_utils/analysis.py:29:def fit_models(data, formulas, features, formula_names=None, feature_names=None, 
patchseq_utils/analysis.py:49:def plot_fit(data, feature, formula, x=None, cluster='cluster', ax=None, legend=False,
patchseq_utils/analysis.py:91:def plot_sig_bars(pvals, pairs_idx, cutoff=0.05, bar=True, label='stars', ax=None, y0=None):
patchseq_utils/analysis.py:103:def plot_sig_bar(pval, y, x_pair, bar=True, label='stars', ax=None):
patchseq_utils/analysis.py:116:def plot_test_bars(data, var, group, test='mannwhitney', group_vals=None, pairs='all', 
patchseq_utils/analysis.py:126:def outline_boxplot(ax):
patchseq_utils/analysis.py:143:def plot_box_cluster_feature(data, y, x='cluster', x_fine=None, label=None, ax=None,
patchseq_utils/analysis.py:223:def plot_boxplot_multiple(data, features, x='cluster', labels=None, horizontal=False, figsize=(4,8),
patchseq_utils/analysis.py:250:def run_cluster_anova(df, features, cluster_var='cluster', pval='pval_cluster', cov_type='HC3', fdr_method='fdr_bh',):
patchseq_utils/analysis.py:264:def plot_feature_effect_sizes(results, pval='pval_cluster', val='rsquared', ylabels=None, 
patchseq_utils/analysis.py:301:def get_skp_results(data, group_col, val_col, method='dunn'):
patchseq_utils/analysis.py:306:def posthoc_results(data, group_col, val_col, group_vals=None, p_adjust=None, cutoff=0.05,
patchseq_utils/analysis.py:335:def posthoc_mw_effects(data, val_col, group_col):
patchseq_utils/analysis.py:351:def pairwise_mde(counts_df):
patchseq_utils/analysis.py:361:def run_kw_dunn(data, features, group_col, fdr_method='fdr_bh', posthoc='dunn', cutoff=0.05):
patchseq_utils/analysis.py:403:def run_anova_pairs(mouse_df, human_df, features, cluster='cluster', cov_type='HC3', fdr_method='fdr_bh',):
patchseq_utils/analysis.py:430:def remove_unused_categories(df: pd.DataFrame):
patchseq_utils/analysis.py:436:def select_distinct(
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1 && sed -n 1,50p patchseq_utils/analysis.py; sed -n 250,430p patchseq_utils/analysis.py; sed -n 525,700p patchseq_utils/analysis.py; sed -n 30,60p patchseq_utils/util.py
```

```
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
from itertools import combinations, permutations
from collections import defaultdict
import statsmodels.formula.api as smf
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.anova import anova_lm

def ols_model(data, formula_rhs, feature, anova_type=2, cov_type='HC3'):
    metrics = ['aic', 'bic', 'fvalue', 'f_pvalue', 'llf', 'rsquared', 'rsquared_adj', 'nobs']
    formula = f"{feature} ~ {formula_rhs}"
    res = smf.ols(formula=formula, data=data).fit(cov_type=cov_type)
    fit_dict = {name: getattr(res, name) for name in metrics}

    if anova_type:
        anova = anova_lm(res, typ=anova_type)
        anova = anova.drop(index=["Residual"])
[... 419 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1/notebooks && cat > $TMPDIR/nbcode.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    if not src.strip(): continue
    print(f"--- [{i}] {c['cell_type']}")
    print(src)
EOF
python $TMPDIR/nbcode.py l1_subclass_distinctness.ipynb | head -400
```

```
--- [0] code
import patchseq_utils.analysis as utils
from patchseq_utils import plotting as plot
import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import os.path
import glob
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
# fix slow autocomplete
%config Completer.use_jedi = False

pd.set_option('use_inf_as_na', True)
pd.options.display.max_columns=300
pd.options.display.max_rows=300
sns.set(style='ticks', context='talk')
[... 315 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1/data && head -1 human_l1_dataset_2023_02_06.csv | tr ',' '\n' | nl | head -80; echo; head -1 aibs_features_E.csv | tr ',' '\n' | wc -l; head -1 aibs_features_E.csv | tr ',' '\n' | tr '\n' ' '
```

```
1	spec_id
     2	exp_component_name
     3	old_layer
     4	batch
     5	cell_name
     6	spec_id
     7	donor
     8	collaborator
     9	gender
    10	collection
    11	medical_conditions
    12	postPatch
    13	postPatch_classification
    14	filldate
    15	rigOperator
    16	rigNumber
    17	cell_depth
    18	sliceHealth
    19	patchseq_roi
    20	roi
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1 && head -1 data/human_l1_dataset_2023_02_06.csv | tr ',' '\n' | nl | sed -n 80,200p | tr '\n' ' '; echo; grep -rn "core_l1_type\|l1_type'\] *=\|'l1_type'" --include=*.py --include=*.ipynb . | cut -c1-250 | head
```

```
80	Tree_first_KL     81	Tree_second_KL     82	Tree_third_KL     83	Tree_first_cor     84	Tree_second_cor     85	Tree_third_cor     86	Tree_call     87	Old_call     88	name     89	created_at     90	pin_z     91	normalized_depth     92	soma_depth_um     93	structure     94	hemisphere     95	donor_name     96	donor_age     97	donor_sex     98	species     99	dendrite_type    100	img_status    101	layer_lims    102	project_code    103	err_id    104	nwb_path    105	nwb_type    106	reconstruction_tag    107	reconstruction_type    108	swc_path    109	t-type    110	slice    111	has_morph    112	ephys_format    113	target_layer    114	tx_qc    115	has_ephys    116	homology_type    117	core_l1_type    118	l1_type 
./notebooks/l1_subclass_distinctness.ipynb:161:    "data = complete_data.query('l1_type')\n",
./notebooks/l1_subclass_distinctness.ipynb:943:    "subset = complete_data.query('core_l1_type').copy()\n",
./notebooks/l1_subclass_distinctness.ipynb:1219:    "data = complete_data.query('l1_type')\n",
./notebooks/l1_subclass_distinctness.ipynb:3026:    "subset = complete_data.query('core_l1_type').copy()\n",
./notebooks/l1_subclass_distinctness.ipynb:3470:    "subset = complete_data.query('core_l1_type').copy()\n",
./notebooks/l1_subclass_distinctness.ipynb:3679:    "data = complete_data.query('l1_type')\n",
./notebooks/l1_subclass_distinctness.ipynb:4986:    "data = complete_data.query('l1_type')\n",
./notebooks/l1_dprime.ipynb:307:    "data = human_df.query(\"core_l1_type & primary_ephys\")\n",
./notebooks/l1_dprime.ipynb:351:    "data = human_df.query('core_l1_type')\n",
./notebooks/l1_dprime.ipynb:352:    "# data = human_df.query('l1_type')\n",
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1/data && python -c "
import pandas as pd
for f in ['human_l1_dataset_2023_02_06.csv','mouse_l1_dataset_2023_02_06.csv']:
    d=pd.read_csv(f,index_col=0,low_memory=False)
    print(f, len(d)); print(pd.crosstab(d['homology_type'].fillna('NA'), [d['core_l1_type'],d['l1_type']]))
    if 'collaborator' in d: print(d['collaborator'].fillna('AIBS').value_counts())
s=pd.read_csv('human_l1_dataset_strict.csv',index_col=0); print('strict human',len(s))
s=pd.read_csv('mouse_l1_dataset_strict.csv',index_col=0); print('strict mouse',len(s))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1/data && python3 - <<'EOF'
import csv,collections
for f in ['human_l1_dataset_2023_02_06.csv','mouse_l1_dataset_2023_02_06.csv']:
    r=list(csv.DictReader(open(f)))
    print(f,len(r))
    c=collections.Counter((x.get('homology_type'),x.get('core_l1_type'),x.get('l1_type')) for x in r)
    for k,v in sorted(c.items(),key=str): print(' ',k,v)
    print(' ',collections.Counter(x.get('collaborator') for x in r))
for f in ['human_l1_dataset_strict.csv','mouse_l1_dataset_strict.csv']:
    print(f, sum(1 for _ in open(f))-1)
EOF
```

```
human_l1_dataset_2023_02_06.csv 419
  ('', 'False', 'False') 22
  ('LAMP5', 'True', 'True') 184
  ('MC4R', 'True', 'True') 67
  ('PAX6', 'True', 'True') 73
  ('VIP', 'True', 'True') 34
  ('other', 'False', 'True') 39
  Counter({'': 283, 'Huib': 69, 'Gabor': 67})
mouse_l1_dataset_2023_02_06.csv 547
  ('LAMP5', 'True', 'True') 419
  ('MC4R', 'True', 'True') 27
  ('PAX6', 'True', 'True') 5
  ('VIP', 'True', 'True') 96
  Counter({None: 547})
human_l1_dataset_strict.csv 272
mouse_l1_dataset_strict.csv 272
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1/notebooks && python3 $TMPDIR/nbcode.py l1_cross_species.ipynb | grep -v "^\s*#" | head -500
```

```
--- [0] markdown
--- [1] code
import patchseq_utils.analysis as utils
from patchseq_utils import plotting as plot
import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
import os.path
import glob
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
%config Completer.use_jedi = False

pd.set_option('use_inf_as_na', True)
pd.options.display.max_columns=300
pd.options.display.max_rows=300
sns.set(style='ticks', context='talk')
[... 481 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1/notebooks && for n in l1_rosehip l1_tnfaip; do echo "=========== $n"; python3 $TMPDIR/nbcode.py $n.ipynb | grep -v "^\s*#" | grep -v "save_plot\|reload\|^import\|^from" ; done | head -400
```

```
=========== l1_rosehip
--- [0] code

pd.set_option('use_inf_as_na', True)
pd.options.display.max_columns=300
pd.options.display.max_rows=300
sns.set(style='ticks', context='talk')
--- [1] code
--- [2] code
--- [3] code
--- [4] code
human_df['axon_branch_freq'] = human_df['axon_num_branches']/human_df['axon_total_length']*100
mouse_df.loc[lambda df: df.sag>0.5, 'sag'] = np.nan
human_ephys = human_df.query("collaborator=='AIBS'")
--- [5] markdown
--- [6] code
df = human_ephys.copy()
df = df.assign(in_type=(df['homology_type']=='MC4R'))
features = ephys_features
res = utils.run_twosamp(df, features, 'in_type')
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1/notebooks && for n in l1_dprime clustering_classification; do echo "=========== $n"; python3 $TMPDIR/nbcode.py $n.ipynb | grep -v "^\s*#" | grep -v "save_plot\|reload\|^import\|^from" ; done | head -500
```

```
=========== l1_dprime
--- [0] code

pd.options.display.max_columns=300
pd.options.display.max_rows=300
sns.set(style='ticks', context='talk')
--- [1] code
--- [2] code
--- [3] code

--- [4] markdown
--- [5] code



--- [6] markdown
--- [7] code
np.sqrt(2) * norm.ppf(0.92)
--- [8] markdown
--- [9] code
[... 481 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1 && python3 $TMPDIR/nbcode.py notebooks/clustering_classification.ipynb | grep -v "^\s*#" | grep -v "save_plot\|reload\|^import\|^from" | sed -n 60,400p; grep -n "def \|cv\b\|cv=\|n_splits\|repeats" patchseq_utils/cluster_pairs.py | head -30; sed -n 1,40p patchseq_utils/clustering.py
```

```
ephys_features, ephys_frac_min=0, cluster_min=0)
--- [17] code
l1_features = subset_features(l1_data, ephys_features, complete_frac=0.6)
set(ephys_features).difference(l1_features)
--- [18] code
l1_data, norm_features = uc.add_norm_features_and_impute(l1_data, l1_features)
other = 'all others'
palette=palette_subclass.copy()
palette[other] = palette['L1 VIP']
l1_data['homology_type'] = l1_data['homology_type'].replace(['other',  'L1 VIP'], other)
l1_data['homology_type'].value_counts(dropna=False)
--- [19] code
data = l1_data
cluster_var = 'homology_type'
keys = l1_data[cluster_var].unique()
cache_dir = "/local1/storage/temp/"
clf = uc.LabeledGMM(n_components=2, init_params='kmeans', n_init=5)
pipe = uc.make_pipeline(clf, memory=cache_dir)
--- [20] code
results = [uc.cluster_combinations_gmm(pipe, data, norm_features, cluster_var, cluster_name) 
[... 262 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1 && python3 $TMPDIR/nbcode.py notebooks/clustering_classification.ipynb | sed -n '/--- \[11\]/,/--- \[17\]/p'; sed -n 39,200p patchseq_utils/clustering.py; sed -n 1,90p patchseq_utils/cluster_pairs.py
```

```
--- [11] code
results = [uc.cluster_combinations_gmm(pipe, data, norm_features, cluster_var, cluster_name) 
                    for cluster_name in keys]
df_all = pd.concat(results, keys=keys, names=['type'])
--- [12] code
top = df_all.reset_index(level=0).loc[lambda df: ~df.features.str.contains(',')].groupby('type').first()
top
--- [13] code
top = df_all.reset_index(level=0).groupby('type').first()
top
--- [14] code
i = 0
fig, axs = plt.subplots(2,2, figsize=(8,8))
axs = np.ravel(axs)
for name, row in top.iterrows():
    features = row['features'].split(', ')
    feature_names = [feature_name(x) for x in features]
    uc.plot_feature_set_gmm(pipe, data, features, cluster_var, name, 
                            feature_names=feature_names, ax=axs[i], palette=palette)
    i+=1
[... 241 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1 && for n in l1_TEA_comparison l1_metadata_effects; do echo "=========== $n"; python3 $TMPDIR/nbcode.py notebooks/$n.ipynb | grep -v "^\s*#" | grep -v "save_plot\|reload\|^import\|^from\|^pd.\|sns.set" ; done | head -300
```

```
=========== l1_TEA_comparison
--- [0] code
warnings.simplefilter(action='ignore', category=FutureWarning)
%config Completer.use_jedi = False

--- [1] code
--- [2] code
--- [3] code
def process_df(shiny, species='mouse'):
    shiny['target_layer'] = shiny.layer.fillna('').apply(get_num)
    shiny.drop(columns=['layer'], inplace=True)

    shiny['layer_ccf'] = shiny['structure'].fillna('').apply(get_num)
    shiny['cortical_area_ccf'] = shiny['structure'].fillna('').apply(not_num)
    shiny['has_morph'] = shiny.swc_path.notna()
    shiny['has_ephys'] = shiny.nwb_path.notna()

    if species=='mouse':
        shiny['tx_qc'] = shiny.apply(lambda df:
                                            (df.Tree_call!='PoorQ') &
[... 281 more lines not kept]
```

**Agent**

Code reading done. Fetching the dandiset's title and description (metadata only) to see which recordings it is meant to hold.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000630/versions/draft/info/ | python3 -c "import json,sys; d=json.load(sys.stdin); m=d.get('metadata',{}); print(m.get('name')); print(m.get('description')); print(m.get('version')); print([a.get('name') for a in m.get('about',[])]); print(m.get('assetsSummary',{}).get('numberOfFiles'), m.get('assetsSummary',{}).get('species'), m.get('assetsSummary',{}).get('approach'))"; curl -s https://api.dandiarchive.org/api/dandisets/000630/ | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('most_recent_published_version',{}).get('version'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  grep -n "with_labels\|with_inputs\|elsewhere" docs/*.md | head -30; sed -n 187,300p docs/protocol.md | grep -n "step 4\|### 4\|outside" ; grep -n "kind: link" -r claims | head -3
```

```
docs/design.md:118:  elsewhere. This is the guard against a result that only looks right.
docs/pilot-notes.md:95:  with outside data (`data: dandiset` or `with_inputs`), and the dashboard
docs/pilot-notes.md:107:RDMs that are not public, are now marked `with_inputs`, and its attempt
docs/pilot-notes.md:123:  `data: with_labels`, for outside sources that only name or map codes the
docs/pilot-notes.md:162:adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
docs/pilot-notes.md:166:dandiset's claims and from `with_inputs` claims. It is never blocked with
docs/protocol.md:137:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
docs/protocol.md:205:4. Decide what comes from outside the dataset. Data from elsewhere may be
docs/protocol.md:214:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
docs/protocol.md:215:     `with_inputs` and `elsewhere` claims are counted apart, each group on
docs/protocol.md:217:   - `with_labels` is for outside sources that only name or map codes the
docs/protocol.md:239:   - `elsewhere` is for a claim whose data the dataset does not hold at
docs/protocol.md:248:   - The notes of a `with_inputs` claim say which side a difference comes
docs/protocol.md:259:     `data: elsewhere` instead (step 4).
19:4. Decide what comes from outside the dataset. Data from elsewhere may be
22:   `inputs` in the attempt. A claim whose outside input is not public is
25:   The registry judges the dataset, so claims that use outside data are
31:   - `with_labels` is for outside sources that only name or map codes the
35:   - When outside data has to be matched to the dataset's cells, sessions
65:     outside labels match the paper's counts.
[... 6 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 205,
 "limit": 80
}
```

```
205	4. Decide what comes from outside the dataset. Data from elsewhere may be
206	   used only when the claims file says the paper relies on it, it is public,
207	   and it is pinned: a DOI, or a repository at a commit. Record each under
208	   `inputs` in the attempt. A claim whose outside input is not public is
209	   blocked with `data_missing`, and its notes say where you looked.
210	
211	   The registry judges the dataset, so claims that use outside data are
212	   kept apart:
213	   - Each claim says what its test uses: `data: dataset` (the default),
214	     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
215	     `with_inputs` and `elsewhere` claims are counted apart, each group on
216	     its own; the others count towards what is said about the dataset.
217	   - `with_labels` is for outside sources that only name or map codes the
218	     dataset already holds, such as stimulus names for its stimulus codes.
219	     They bring in no measurements. A link claim must confirm the names, and
220	     the missing names are recorded as a finding (`metadata_insufficient`).
221	   - When outside data has to be matched to the dataset's cells, sessions
222	     or subjects, a claim of its own (`kind: link`) tests the link. Link
223	     claims are the registry's checks, not findings of the paper, so the
224	     author adds them to the claims file; they are the only claims the
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q --depth 1 https://github.com/AllenInstitute/ipfx && cd ipfx && git log -1 --format='%H %cd' && grep -rn "adapt_ratio\|first_isi_inv\|ir_late\|def irregularity\|sag_depol\|postap_slope\|adp_v" --include=*.py . | grep -v test | head -30
```

```
c607a36e25618a6bb8ba5438c1cd945fb429e659 Wed Dec 10 19:46:32 2025 +0100
./ipfx/feature_extractor.py:51:        "adp_t", "adp_v", "adp_i", "adp_index",
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1 && grep -rn "ir_late\|postap_slope\|adapt_ratio\|first_isi_inv\|irregular" --include=*.py . | head; grep -rln "ateam\|ipfx" . | head
```

```
./patchseq_utils/util.py:59:    if 'adapt_ratio' in feat:
./patchseq_utils/util.py:79:    elif 'ir_late' in feat:
./patchseq_utils/util.py:80:        name = 'irregularity'
./patchseq_utils/util.py:91:    if 'adapt_ratio' in feat:
./patchseq_utils/util.py:113:    elif 'postap_slope' in feat:
./patchseq_utils/util.py:115:    elif 'ir_late' in feat:
./patchseq_utils/l1_load.py:123:human_df.loc[lambda df: df['first_isi_inv_hero']>1000, 'first_isi_inv_hero'] = np.nan
./patchseq_utils/l1_load.py:124:human_df.loc[lambda df: df['first_isi_inv_rheo']>1000, 'first_isi_inv_rheo'] = np.nan
./patchseq_utils/plot/sweeps.py
./notebooks/l1_umaps.ipynb
./notebooks/l1_tnfaip.ipynb
./notebooks/l1_subclass_distinctness.ipynb
./notebooks/l1_rosehip.ipynb
./notebooks/l1_proportions.ipynb
./notebooks/l1_morph_metrics.ipynb
./notebooks/l1_metadata_effects.ipynb
./notebooks/l1_dprime.ipynb
./notebooks/l1_depth_revisions.ipynb
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1 && cat patchseq_utils/pipelines.py | head -60; grep -n "def plot_dprime" -A25 patchseq_utils/cluster_pairs.py | head -40
```

```
from sklearn.neighbors import LocalOutlierFactor
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import RobustScaler, StandardScaler, PowerTransformer
from sklearn.model_selection import cross_val_score, RepeatedStratifiedKFold
import sklearn.metrics as metrics
from itertools import combinations
import numpy as np
import seaborn as sns

class OutlierExtraction(BaseEstimator, TransformerMixin):
    def __init__(self, **kwargs ):
        self.kwargs = kwargs

    def transform(self, X):
        lof = LocalOutlierFactor(**self.kwargs)
        count = 0
        for i in range(X.shape[1]):
            labels = lof.fit_predict(X[:,[i]])
[... 63 more lines not kept]
```

**Agent**

Now drafting the claims. First checking how the quote checker normalises whitespace, since the supplement text has hard line breaks.

**Agent calls Bash**

```bash
cd  sed -n 1,200p tools/claims_check.py | grep -n "def \|normal\|replace\|\\\\s\|lower\|unicode\|dash\|hyphen" | head -40
```

```
18:import unicodedata
34:def norm(s: str) -> str:
35:    s = unicodedata.normalize("NFKC", html.unescape(s))
37:        s = s.replace(a, b)
38:    return re.sub(r"\s+", " ", s).strip().lower()
41:def flattenings(raw: str) -> list[str]:
45:    return [tight, loose, tight.replace(" ", ""), loose.replace(" ", "")]
48:def quote_found(quote: str, texts: list[str]) -> bool:
51:        frags = fragments if " " in text else [f.replace(" ", "") for f in fragments]
63:def printed_forms(v: float) -> set[str]:
75:    return {f.lower() for f in out}
78:def check(claims_path: Path, paper_paths: list[Path]) -> int:
80:    texts = [t for p in paper_paths for t in flattenings(p.read_text(encoding="utf-8", errors="replace"))]
105:def main() -> int:
```

**Agent calls Read**

```json
{
 "file_path": "tools/claims_check.py"
}
```

```
1	"""Check a claims file against the full text of its paper.
2	
3	    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]
4	
5	Validates the file against schemas/claims.schema.json, checks every quote word for word
6	(fragments split on "...", found in order) and looks for every recorded p-value and
7	confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
8	files (a paper and its supplement) are searched together. A value printed in a form the
9	checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
10	confirmed by reading. Exits non-zero on any problem.
11	"""
12	
13	from __future__ import annotations
14	
15	import html
16	import re
17	import sys
18	import unicodedata
19	from pathlib import Path
20	
[... 93 more lines not kept]
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
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:4000])"; curl -s "https://zenodo.org/api/records/8310226" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('metadata',{}).get('title'), d.get('metadata',{}).get('version'), d.get('doi'), [f['key'] for f in d.get('files',[])][:10])"
```

Result: the fetched text is not kept.

**Agent**

Checking the code for the donor-effects tests (Fig. S6A,B) before writing that claim.

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L1 && python3 $TMPDIR/nbcode.py notebooks/l1_metadata_effects.ipynb | grep -v "^\s*#" | sed -n '/--- \[33\]/,$p' | grep -v "save_plot\|^labels\|plt\.\|palette" | head -150
```

```
--- [33] code
feat = ['sag_peak_t', 'downstroke_rheo', 'input_resistance_ss', 'avg_rate_max']
          'input resistance (MΩ)', 'peak mean FR (Hz)']
utils.plot_boxplot_multiple(data, feat, group_col, labels=labels, test='dunn',
                       space=0.3, pad_title=5, figsize=(4,9))
--- [34] code
features = [
    'sag',
    'input_resistance'
]
for f in features:
    utils.plot_box_cluster_feature(data, f, group_col, test='dunn')
--- [35] markdown
--- [36] code
df = human_df.query("l1_type")
group_col = 'structure'
data = subset_data(df, morph_features, cluster=group_col, ephys_frac_min=0, cluster_min=5).query("structure!='TemL'")
data[group_col].value_counts()
--- [37] code
features = morph_features
[... 131 more lines not kept]
```

**Agent**

I have what I need from the paper and code. Writing the claims file now (39 claims).

**Agent calls Write**

```json
{
 "file_path": "claims/000630/10.1126-science.adf0805.yaml",
 "content": "# Claims for Chartrand et al. (2023), Science 382, eadf0805, on dandiset 000630.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md (Reader).\n#\n# Text read. The author manuscript of the version of record in PubMed Central (PMC11864503,\n# NIHMS2048794), as text (paper/10.1126-science.adf0805.txt). It has the main text, the legends\n# of Figures 1 to 6, and the supplementary PDF (NIHMS2048794-supplement-5.pdf) extracted as text:\n# the Materials and Methods, the legends of figs. S1 to S9, and Tables S1 and S2. The four\n# supplementary data tables (Data S1 donors, Data S2 subclass statistics, Data S3 metadata\n# statistics, Data S4 cross-species statistics, all .xlsx) are not under paper/, so no per-feature\n# statistic from them is used here; each claim rests on the sentence or legend it quotes. The\n# code that wrote Data S2 and S4 was read instead (below). No figure was opened. The bioRxiv\n# preprint (doi:10.1101/2022.10.24.511199) is under paper/ but was not used.\n#\n# Code read. github.com/AllenInstitute/patchseq_human_L1 at commit 7777857 (2025-05-13), linked\n# under Data and materials availability and archived as Zenodo doi:10.5281/zenodo.8310226 (v0.2).\n# It holds patchseq_utils (data loading l1_load.py, statistics analysis.py, pairwise d' in\n# cluster_pairs.py and dprime.py, GMM clustering in clustering.py, preprocessing pipelines.py),\n# notebooks for each figure (l1_subclass_distinctness, l1_cross_species, l1_rosehip, l1_tnfaip,\n# l1_dprime, clustering_classification, l1_metadata_effects, l1_TEA_comparison and others), R\n# scripts for the transcriptomic UMAPs, and a data folder: per-cell tables\n# (human_l1_dataset_2023_02_06.csv, 419 human rows with t-type, homology_type, core_l1_type,\n# l1_type, collaborator, layer, structure, donor_age, donor_sex, medical_conditions, nwb_path;\n# mouse_l1_dataset_2023_02_06.csv, 547 rows), the strict L1 cell lists\n# (human_l1_dataset_strict.csv and mouse_l1_dataset_strict.csv, 272 rows each), the IPFX\n# feature tables (aibs_features_E.csv, tamas_features_E.csv, mansvelder_features_E.csv,\n# aibs_mouse_features_E.csv), morphology features, transcriptomes (ps_human.RData,\n# ps_mouse.RData), MERFISH proportions and the cytoarchitecture source data. Only column headers\n# and the label columns of the tables were read, not their feature values. Several features\n# (adaptation ratios, irregularity ratio, initial firing rate, depolarizing sag, post-AP slope)\n# come from custom code the Methods say \"will be released in a future version of IPFX\"; it is\n# not in this repository nor in IPFX at commit c607a36, so their exact definitions are open\n# (see \"Open details\" below). The ZINB regularization file used for the patch-seq transcriptomic\n# d' (zinb_human.h5) and the LIMS donor lookups are on Allen Institute servers, not in the\n# repository.\n#\n# Data the paper used. Human neurosurgical tissue (refractory temporal lobe epilepsy,\n# hydrocephalus or deep tumour), mostly middle temporal gyrus (MTG) with smaller fractions from\n# other temporal and frontal areas, recorded at three sites (Seattle, the primary dataset;\n# Amsterdam and Szeged, a held-out secondary dataset). Acute 350 um slices, whole-cell current\n# clamp at 32 to 34 C with synaptic blockers, Bessel 10 kHz, digitized at 50 kHz, potentials not\n# corrected for the -14 mV junction potential; bias current holds the initial resting potential.\n# Sweep QC: within 2 mV of target, leak 0 +/- 100 pA, rms noise < 0.2 mV (1.5 ms) and < 0.5 mV\n# (500 ms). Stimuli: 1 s long squares (hyperpolarizing -10 to -90 pA, rheobase, rheobase + 40\n# pA up to + 80 pA), 3 ms short squares, a slow ramp, and in a subset a logarithmic chirp; in a\n# subset, nucleated-patch voltage clamp for K+ currents. Features from IPFX: spike threshold,\n# height, width, fast AHP, trough, upstroke, downstroke and ratio; input resistance (all\n# hyperpolarizing sweeps), sag (sweep closest to -100 mV), depolarizing sag (subthreshold sweep\n# closest to rheobase), rheobase, f-I slope; spike-train features on the rheobase sweep and the\n# sweep 40 pA above it (\"hero\" in the code); adaptation ratios between first and third spike on\n# the lowest step with at least 4 spikes. Transcriptomes were mapped by tree mapping to the human\n# MTG and mouse VISp taxonomies; 10 human L1 t-types grouped into four homology subclasses\n# (LAMP5: LAMP5 NMBR, DBP, LCP2; MC4R: SST CHRNA4, ADARB2 MC4R; PAX6: PAX6 CDH12, PAX6\n# TNFAIP8L3; L1 VIP: VIP TSPAN12) and \"other\" (SST BAGE2, VIP PCDH20). Table S2: 250 human cells\n# (194 with electrophysiology, 71 with morphology); by subclass, electrophysiology counts LAMP5\n# 96, MC4R 35, PAX6 33, L1 VIP 15, other 15. Mouse comparison data are 272 L1 patch-seq cells\n# (255 with electrophysiology, 43 with morphology) from VISp (DANDI 000020, version\n# 0.210913.1639) and additional recordings in visual cortex and TEa.\n#\n# Where the data are. The dandiset (\"Human L1 patch-seq electrophysiology\", 210 files, human\n# only; the paper cites version 0.230915.2257) holds the human NWB electrophysiology. Its\n# description points to the code repository for features. Cell labels (t-type, subclass,\n# collaborator, layer, brain region, donor condition, age and sex) come from the code's\n# human_l1_dataset_2023_02_06.csv; claims that need them are `with_labels`. The author adds the\n# link claim that matches the dandiset's files to that table (protocol, author step 4).\n# Mouse electrophysiology (DANDI 000020) is an outside input (`with_inputs`). Morphologies\n# (BIL doi:10.35077/g.606), transcriptomes (NeMO; processed data in the Zenodo archive) and\n# cytoarchitecture images are not in the dandiset (`elsewhere`).\n#\n# Sets used below, from the code.\n#  - Strict L1 set: cells listed in human_l1_dataset_strict.csv, soma in L1 or in L2 within\n#    40 um of the L1/L2 border (Methods, \"border cells\"; l1_cross_species.ipynb cell 5).\n#  - Primary set P: strict L1 set, collaborator AIBS (Seattle) and failed_fx_long_squares\n#    False (l1_load.py, primary_ephys). Table S2 gives 194 such cells.\n#  - Core subclasses: LAMP5, MC4R, PAX6, L1 VIP (core_l1_type True); l1_type adds \"other\".\n#  - Code feature filters: first_isi_inv_rheo and first_isi_inv_hero above 1000 Hz and\n#    input_resistance above 1000 MOhm are set missing (l1_load.py).\n#\n# Open details, and the readings named for each (criteria refer to these).\n#  - O1, custom feature definitions. The Methods define the initial firing rate (inverse of the\n#    first ISI) and the adaptation ratio (ratio of a spike feature between the first and third\n#    spike on the lowest step with at least 4 spikes), but not the order of that ratio, the\n#    irregularity ratio (ir_late_mean), the post-AP slope (postap_slope_rheo, \"ADP slope\" in\n#    Fig. 5B) or the ADP voltage. Readings for the author's recomputation from the NWB files:\n#    (a) the Methods' definitions with IPFX conventions; (b) the paper's own per-cell values in\n#    aibs_features_E.csv, matched by cell, shown as a check of (a). Where (a) cannot be\n#    computed for a feature, the claim that needs it is judged on (b) and the notes say so.\n#  - O2, cross-species two-way ANOVA. The Methods say \"two-way ANOVA on species and subclass\n#    (heteroskedasticity-corrected)\", the Fig. 3D legend says \"2-way ANOVA on ranks\", Data S4's\n#    description says Type II; the code (run_species_subclass_stats) fits OLS with HC3 errors,\n#    Type I sums of squares, no rank transform, species entered first. Readings: (a) ranks,\n#    Type II, HC3 (legend and Data S4); (b) raw values, Type I, HC3 (code).\n#  - O3, classifier preprocessing. The Methods give, for clustering and classification,\n#    exclusion of cells missing more than 60% of features, LocalOutlierFactor < -20 outlier\n#    removal, RobustScaler and KNNImputer; the code applies the outlier step in the d'\n#    pipeline (pipelines.py) but not in the subclass classifier or the GMM search. Readings:\n#    (a) Methods; (b) code.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000630\"\npaper: doi:10.1126/science.adf0805\nclaims:\n- id: patchseq-counts\n  statement: The human L1 patch-seq dataset has 250 cells passing transcriptomic quality, 194 with\n    electrophysiology passing quality control and 71 reconstructed; by subclass, 96 LAMP5, 35\n    MC4R, 33 PAX6, 15 L1 VIP and 15 other cells have electrophysiology.\n  source: Results, L1 patch-seq pipeline and transcriptomic references, paragraph 4; Table S2\n  quote: All cells were filtered for transcriptomic (n=250) and electrophysiological quality\n    (n=194), and a subset of neurons (n=71) with sufficient cell labeling were imaged at high\n    resolution\n  data: with_labels\n  expected:\n  - quantity: human cells with electrophysiology (primary set P)\n    value: 194\n    tolerance: 19.4\n  - quantity: LAMP5 cells with electrophysiology\n    value: 96\n    tolerance: 9.6\n  - quantity: MC4R cells with electrophysiology\n    value: 35\n    tolerance: 3.5\n  - quantity: PAX6 cells with electrophysiology\n    value: 33\n    tolerance: 3.3\n  - quantity: L1 VIP cells with electrophysiology\n    value: 15\n    tolerance: 1.5\n  - quantity: other (SST BAGE2, VIP PCDH20) cells with electrophysiology\n    value: 15\n    tolerance: 1.5\n  criterion: Counts of dandiset cells in the primary set P (strict L1 set, AIBS, long-square\n    features extracted; Table S2's \"ephys cell count\", as summarize() in l1_cross_species.ipynb\n    computes it), overall and by homology_type. Reproduced when every count is within its\n    tolerance. The 250 and 71 counts need transcriptomes and reconstructions and are not\n    tested here; the count of dandiset files not in P is reported.\n- id: fig1a-human-types-separated\n  statement: In transcriptomic reference data, many human L1 t-types form separated clusters while\n    mouse L1 t-types vary more continuously, suggesting stronger transcriptomic specialization in\n    human L1.\n  source: Results, L1 patch-seq pipeline and transcriptomic references, paragraph 1; Figure 1A\n  quote: many human t-types formed separated clusters, with others clustered in groups of related\n    t-types, whereas mouse L1 t-types showed more continuous variability\n  data: elsewhere\n  where: Allen Brain Map RNA-seq portal (human MTG snRNA-seq of Hodge et al. 2019, mouse VISp\n    scRNA-seq of Tasic et al. 2018), as the Methods cite them\n  criterion: The paper shows this with UMAP projections and reports no test. Judged with the\n    paper's own measure of distinctness, the reference d' (Fig. 6C, Methods, Discriminant\n    analysis); reproduced when the median pairwise d' among human L1 t-types exceeds that among\n    mouse L1 t-types.\n- id: fig1b-three-subclasses\n  statement: Ten human and eight mouse L1 t-types are defined from the references; grouping human\n    t-types with d' below 2.2 forms three subclasses, leaving three t-types ungrouped.\n  source: Results, L1 patch-seq pipeline and transcriptomic references, paragraph 1; Figure 1B;\n    Methods, Subclasses and cross-species homology\n  quote: we identified 10 L1 t-types in human and 8 in mouse ... This formed three subclasses, with\n    three t-types remaining ungrouped\n  data: elsewhere\n  where: Allen Brain Map RNA-seq portal (human MTG snRNA-seq, mouse VISp scRNA-seq)\n  expected:\n  - quantity: human L1 t-types\n    value: 10\n    tolerance: 0\n  - quantity: mouse L1 t-types\n    value: 8\n    tolerance: 0\n  - quantity: human subclasses from d' grouping\n    value: 3\n    tolerance: 0\n  criterion: Tolerances are zero because these are counts of categories that define the\n    taxonomy; a 10% tolerance would admit no other integer. L1 t-types are those making up more\n    than 5% of L1 cells or with more than 50% of the type in L1 dissections (Methods); subclasses\n    group t-type pairs with NB-discriminant d' < 2.2 (Methods).\n- id: fig1d-four-homology-subclasses\n  statement: Cross-species matching of mouse t-types to human subclasses gives four\n    homology-driven subclasses; two human L1 t-types (SST BAGE2, VIP PCDH20) are homologous to\n    deeper-layer mouse types and are left out.\n  source: Results, L1 patch-seq pipeline and transcriptomic references, paragraph 3; Figure 1D\n  quote: These matches resulted in four homology-driven subclasses (called subclasses hereafter)\n    with proportions largely comparable across species ... Two additional human L1 t-types (SST\n    BAGE2 and VIP PCDH20) were excluded from cross-species L1 subclasses because of their homology\n    to t-types found in deeper layers, but not L1 of mouse neocortex\n  data: elsewhere\n  where: Allen Brain Map RNA-seq portal references and the integrated coordinates in Zenodo\n    doi:10.5281/zenodo.8310226 (data/scalign_coords.rda)\n- id: fig1e-subclass-proportions\n  statement: Subclass proportions in the L1 patch-seq data differ between human and mouse for every\n    subclass except L1 VIP, PAX6 being the notable difference.\n  source: Figure 1E legend; Results, L1 patch-seq pipeline and transcriptomic references,\n    paragraph 3\n  quote: All cross-species proportion differences (except L1 VIP) significant at FDR-corrected\n    p<0.001, one vs. rest Fisher’s exact tests\n  statistics:\n  - test: one vs. rest Fisher's exact tests\n    p: 0.001\n    p_relation: \"<\"\n    corrected: FDR\n  data: elsewhere\n  where: per-cell t-type tables in Zenodo doi:10.5281/zenodo.8310226 (human and mouse\n    l1_dataset_2023_02_06.csv), from the NeMO transcriptomes\n  criterion: For each category of Fig. 1E, a two-sided Fisher's exact test of species against in\n    category or not, over the strict L1 sets of both species; Benjamini-Hochberg across\n    categories. Reproduced when every category but L1 VIP has FDR p < 0.001 and L1 VIP does not.\n- id: figs2a-patchseq-vs-snrnaseq\n  statement: Compared with snRNA-seq, patch-seq sampled fewer SST BAGE2 and more PAX6 CDH12 and VIP\n    TSPAN12 cells; MERFISH proportions did not differ from patch-seq.\n  source: Results, L1 patch-seq pipeline and transcriptomic references, paragraph 6; Figure S2A\n  quote: patch-seq had fewer SST BAGE2 cells and more PAX6 CDH12 and VIP TSPAN12 compared to\n    snRNA-seq (p<0.05, False discovery rate or FDR-corrected Fisher’s exact test). MERFISH had\n    intermediate proportions of SST BAGE2 with no significant differences compared to patch-seq\n    (p>0.18)\n  statistics:\n  - about: patch-seq against snRNA-seq\n    test: Fisher's exact test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n  - about: MERFISH against patch-seq\n    test: Fisher's exact test\n    p: 0.18\n    p_relation: \">\"\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.8310226 (data/merfish_counts.csv, merfish_proportions.csv and\n    the per-cell tables) and the Allen Brain Map human MTG snRNA-seq reference\n- id: figs1d-marker-correlation\n  statement: Marker gene expression by t-type correlates strongly between patch-seq and the\n    snRNA-seq reference (r = 0.84).\n  source: Figure S1D legend; Results, L1 patch-seq pipeline and transcriptomic references,\n    paragraph 5\n  quote: Correlation of marker gene expression between patch-seq and snRNA-seq reference (r=0.84,\n    p<10-18)\n  statistics:\n  - test: correlation\n    statistic: r = 0.84\n    p: 1.0e-18\n    p_relation: \"<\"\n  expected:\n    quantity: correlation of t-type mean marker expression, patch-seq against snRNA-seq\n    value: 0.84\n    tolerance: 0.084\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.8310226 (data/ps_human.RData) and the Allen Brain Map human MTG\n    snRNA-seq reference\n- id: fig2c-subclass-ephys-differences\n  statement: Human L1 subclasses differ in electrophysiology, notably in sag and initial firing\n    rate (Kruskal-Wallis, FDR-corrected p < 1e-7).\n  source: Results, Morpho-electric diversity in human L1, paragraph 1; Figure 2C\n  quote: Electrophysiologically, subclasses were distinguished by subthreshold properties such as\n    sag ... as well as several suprathreshold properties including firing rate ... Electrophysiological\n    and morphological features distinguishing L1 subclasses (KW test, FDR-corrected p<10−7 for\n    electrophysiology\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 1.0e-7\n    p_relation: \"<\"\n    corrected: FDR (Benjamini-Hochberg)\n    n: 96 LAMP5, 35 MC4R, 33 PAX6 and 15 L1 VIP cells (Table S2)\n  data: with_labels\n  criterion: As l1_subclass_distinctness.ipynb cells 8 and 10 (run_kw_dunn), which wrote Data S2.\n    Cells in P of the four core subclasses; features with more than 40% non-missing values among\n    l1_type cells of P; per feature a Kruskal-Wallis test across subclasses, epsilon2 = H/(n-1),\n    Benjamini-Hochberg across features; Dunn's post hoc tests on significant features, FDR across\n    pairs. Sag is IPFX sag at the hyperpolarizing sweep closest to -100 mV; initial firing rate is\n    first_isi_inv_hero (inverse first ISI at rheobase + 40 pA), as Fig. 2C plots (O1). Reproduced\n    when both have FDR p < 1e-7; partially reproduced when both have FDR p < 0.05 but not both\n    below 1e-7.\n  depends_on:\n  - patchseq-counts\n- id: fig2b-subclass-ephys-profiles\n  statement: LAMP5 cells show small sag and adaptation, PAX6 cells minimal sag and a high initial\n    firing rate, while MC4R and L1 VIP cells show strong sag.\n  source: Results, Morpho-electric diversity in human L1, paragraph 2; Figure 2B and 2C\n  quote: Their electrophysiological phenotype was relatively undistinguished, with firing-rate\n    adaptation and sag present but small ... along with minimal sag and high initial firing rate\n    at the onset of response to depolarizing current injection ... MC4R cells had extremely\n    compact ball-like axonal arbors, along with strong sag ... with a consistent stellate-like\n    dendrite morphology and high sag\n  data: with_labels\n  depends_on:\n  - fig2c-subclass-ephys-differences\n  criterion: On the cells and features of fig2c-subclass-ephys-differences. Reproduced when (i)\n    the median sag of MC4R and of L1 VIP each exceeds that of LAMP5 and of PAX6, (ii) PAX6 has the\n    lowest median sag of the four, and (iii) PAX6 has the highest median first_isi_inv_hero.\n    Not reproduced otherwise. Dunn's FDR-corrected p for each pair is reported; the paper states\n    the ordering in words and reports no pairwise values in the text read.\n- id: figs3a-sag-adaptation\n  statement: Spike adaptation properties are strongly and inversely related to sag across human L1\n    cells (R2 = 0.74).\n  source: Results, Morpho-electric diversity in human L1, paragraph 1; Figure S3A legend\n  quote: Spike adaptation properties showed a strong inverse relationship with sag across the\n    dataset (Fig. S3A)\n  statistics:\n  - test: linear regression\n    statistic: R2 = 0.74\n    p: 1.0e-13\n    p_relation: \"<\"\n  expected:\n    quantity: R2 of upstroke adaptation ratio regressed on sag\n    value: 0.74\n    tolerance: 0.074\n  data: with_labels\n  criterion: As l1_subclass_distinctness.ipynb cells 8, 16 and 17. Cells in P with l1_type (the\n    five groups, other included); OLS of upstroke_adapt_ratio on sag with HC3 errors\n    (run_regressions). Reproduced when R2 is within tolerance and p < 1e-13, and cells with more\n    sag show less change of spike upstroke from the first to the third spike. The ratio's order\n    is open (O1); the direction is judged on the change, whichever order the ratio has, and the\n    slope's sign is reported with the order used.\n- id: fig2c-lamp5-gradient\n  statement: Within the LAMP5 subclass, sag and initial firing rate decrease from the NMBR to the\n    DBP to the LCP2 t-type.\n  source: Results, Morpho-electric diversity in human L1, paragraph 2; Figure 2C\n  quote: Within the LAMP5 subclass, sag and initial firing rate decreased from the NMBR t-type to\n    DBP to LCP2 t-types ... Spearman correlation FDR-corrected p<10−3\n  statistics:\n  - test: Spearman correlation\n    p: 0.001\n    p_relation: \"<\"\n    corrected: FDR\n  data: with_labels\n  criterion: As l1_subclass_distinctness.ipynb cell 59. All LAMP5 cells of the strict L1 set (the\n    code does not restrict to P), t-type coded in the order LCP2, DBP, NMBR; Spearman correlation\n    of each feature whose name has no \"3\" with that code (run_correlations), Benjamini-Hochberg\n    across features. Reproduced when sag and first_isi_inv_hero each have FDR p < 0.001 and both\n    are highest in NMBR and lowest in LCP2. If the dandiset lacks the Amsterdam and Szeged LAMP5\n    cells the code includes, the test runs on what it holds and the notes say so; the same test\n    on P alone is shown as a variant.\n- id: fig2d-subclass-morphology\n  statement: Human L1 subclasses differ morphologically in vertical orientation of axons and\n    dendrites, axon extent and shape, and dendrite branching (Kruskal-Wallis, FDR p < 1e-3).\n  source: Results, Morpho-electric diversity in human L1, paragraph 1; Figure 2D\n  quote: Morphologically, subclasses were distinguished by vertical orientation of axons and\n    dendrites, axon extent and shape, and dendrite branching\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 0.001\n    p_relation: \"<\"\n    corrected: FDR\n  data: elsewhere\n  where: Brain Image Library doi:10.35077/g.606 (reconstructions); morphology features in Zenodo\n    doi:10.5281/zenodo.8310226 (data/RawFeatureWide_human+derivatives.csv)\n- id: figs6-donor-condition-ephys\n  statement: No electrophysiological feature of human L1 cells differs with donor medical\n    condition, sex or age after FDR correction.\n  source: Results, Morpho-electric diversity in human L1, paragraph 3; Figure S6A and S6B legends\n  quote: AP width (upper right) was the only significant electrophysiology feature (MW p=0.03, NS\n    after FDR correction)\n  statistics:\n  - about: AP width, epileptic against non-epileptic donors, before correction\n    test: Mann-Whitney test\n    p: 0.03\n  - about: sex, the only feature before correction\n    test: Mann-Whitney test\n    p: 0.02\n  data: with_labels\n  criterion: A claim of absence, judged on the paper's tests. As l1_metadata_effects.ipynb cells\n    50 and 51 and the Methods (Statistical analysis of variability). Cells of the strict L1 set\n    with l1_type, AIBS and long-square features extracted; features with more than 40%\n    non-missing values. Medical condition as epileptic or not (code's epileptic(), from the\n    medical_conditions column) and sex, each by two-sided exact Mann-Whitney tests; age by\n    Spearman correlation; Benjamini-Hochberg across features within each variable. Reproduced\n    when no feature has FDR p < 0.05 for any of the three; not reproduced when any does. The\n    smallest uncorrected p and its feature are reported for each.\n- id: figs6a-tumor-dendrite-branching\n  statement: Cells from tumor patients have higher dendritic branching than cells from epilepsy\n    patients, not explained by brain area or subclass.\n  source: Results, Morpho-electric diversity in human L1, paragraph 3; Figure S6A\n  quote: with the exception of higher dendritic branching in cells from tumor patients compared to\n    epilepsy patients\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n  data: elsewhere\n  where: Brain Image Library doi:10.35077/g.606; morphology features in Zenodo\n    doi:10.5281/zenodo.8310226\n- id: figs6c-region-ephys\n  statement: Some electrophysiological features of human L1 cells, including input resistance,\n    vary with brain region; sparsely sampled regions either match MTG or have larger input\n    resistance.\n  source: Results, Cross-species differences in L1, paragraph 2; Figure S6C\n  quote: We also explored dependence of L1 interneuron morpho-electric properties on brain region\n    within our human data and found moderate effects on a set of features including dendrite\n    extent and input resistance (Fig. S6C). For these features, more sparsely sampled regions\n    either failed to differ from MTG cells or had smaller dendritic extent and larger input\n    resistance\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n  data: with_labels\n  criterion: As l1_metadata_effects.ipynb cells 29 and 30. Cells of the strict L1 set with\n    l1_type, AIBS and long-square features extracted, in regions ITG, MTG, MFG and SFG (regions\n    with at least 5 cells; TemL left out); features more than 50% non-missing; Kruskal-Wallis by\n    region, Benjamini-Hochberg across features; Dunn's post hoc. Reproduced when\n    input_resistance_ss has FDR p < 0.05 and no other region has a median input resistance below\n    MTG's with Dunn's FDR p < 0.05. The other features of Fig. S6C (sag_peak_t, downstroke_rheo,\n    avg_rate_max) are reported.\n- id: fig3b-l1-cytoarchitecture\n  statement: Human L1 is thicker than mouse L1 but not less dense, with smaller cell bodies.\n  source: Results, Cross-species differences in L1, paragraph 1; Figure 3B and S6D\n  quote: human L1 was thicker but not less dense, with smaller cell bodies compared with several\n    mouse neocortical areas\n  statistics:\n  - test: Kruskal-Wallis test, Dunn's post hoc (MTG against TEa)\n    p: 0.05\n    p_relation: \"<\"\n    n: human MTG 76 ROIs (3016 cells, 16 cases); mouse TEa 29 ROIs (400 cells, 3 animals)\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.8310226 (data/Source data cortical structure L1.csv and\n    Source data cortical structure L1 all areas.csv)\n- id: fig3d-morphology-species\n  statement: Human L1 neurites are more tortuous (smaller contraction ratio) than mouse, mouse\n    dendrites are more branched, and mouse axons rarely extend above the dendrites.\n  source: Results, Cross-species differences in L1, paragraph 1; Figure 3D left\n  quote: Unlike human axons, mouse axons rarely extended above dendrites (Fig. 3D left), perhaps\n    reflecting sublaminar structure found only in the thicker human L1. Human neurites were also\n    structured differently, with smaller contraction ratios (higher tortuosity) compared to the\n    straighter but more heavily branched mouse dendrites\n  statistics:\n  - test: 2-way ANOVA on ranks, species effect\n    p: 1.0e-7\n    p_relation: \"<\"\n    corrected: FDR\n  data: elsewhere\n  where: Brain Image Library doi:10.35077/g.606 and the mouse reconstructions the paper lists\n    (download.brainimagelibrary.org/biccn/zeng/pseq/morph/200526/); features in Zenodo\n    doi:10.5281/zenodo.8310226\n- id: figs3c-size-similar\n  statement: Human L1 neurons are slightly larger than mouse in horizontal extent, with no species\n    difference in vertical dimensions or dendritic diameter.\n  source: Results, Cross-species differences in L1, paragraph 1; Figure S3C\n  quote: Although human neurons across subclasses were slightly larger in horizontal extent, no\n    differences were observed in vertical dimensions or dendritic diameter (Fig. S3C)\n  data: elsewhere\n  where: Brain Image Library doi:10.35077/g.606; features in Zenodo doi:10.5281/zenodo.8310226\n- id: fig3d-ephys-species\n  statement: Mouse L1 cells have less sag, lower spike amplitude and higher rheobase than human,\n    across subclasses and within at least 2 of the 4 matched subclasses.\n  source: Results, Cross-species differences in L1, paragraph 2; Figure 3D right\n  quote: Mouse cells had less sag, lower amplitude spikes, and higher rheobase across types and\n    within at least 2 of 4 matched subclasses\n  statistics:\n  - test: 2-way ANOVA on ranks, species effect\n    p: 1.0e-38\n    p_relation: \"<\"\n    corrected: FDR\n  data: with_inputs\n  criterion: As l1_cross_species.ipynb cells 5, 25 and 38. Human cells of P with soma in L1\n    (layer 1, border cells left out) in the four core subclasses; mouse VISp L1 cells (layer_ccf\n    1, failed_qc False) from DANDI 000020 with the code's mouse labels; features with more than\n    80% non-missing values. Per feature a two-way ANOVA of species and subclass with their\n    interaction, Benjamini-Hochberg across features; where the interaction has FDR p < 0.05,\n    two-sided Mann-Whitney tests of species within each subclass (Methods). The ANOVA follows\n    O2, readings (a) and (b). Features as Fig. 3D plots them, sag, rheobase_i and\n    peak_deltav_ramp (AP height). Reproduced when, under both readings, each of the three has a\n    species effect with FDR p < 1e-38 in the stated direction, and, for each with an interaction,\n    at least 2 of 4 subclasses differ at p < 0.05 in that direction. Partially reproduced when the\n    directions hold with FDR p < 0.05 but not all below 1e-38. When the readings disagree the\n    claim is methods_underspecified with both shown.\n- id: fig3e-tea-validation\n  statement: The human versus mouse electrophysiological differences found against VISp are\n    replicated against mouse TEa, so they are not regional.\n  source: Results, Cross-species differences in L1, paragraph 2; Figure 3E\n  quote: We replicated these findings in a comparison between MTG and a smaller TEa dataset,\n    verifying that cross species differences were not due to regional differences between MTG\n    and VISp\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n  data: with_inputs\n  criterion: As l1_TEA_comparison.ipynb cells 17 to 25. Human cells of P with soma in L1 against\n    mouse VISp L1 and, separately, against mouse TEa L1 cells (Amsterdam recordings and Allen TEa\n    cells with transcriptomic QC and features extracted); features more than 50% non-missing in\n    every mouse area; two-sided exact Mann-Whitney per feature, effect r = 2 AUC - 1,\n    Benjamini-Hochberg. Reproduced when every feature shown against VISp (the distinct top\n    features by r, select_distinct with Spearman threshold 0.8) that has FDR p < 0.05 against\n    VISp also has FDR p < 0.05 against TEa with the same direction; partially reproduced when\n    most do. The paper names no deposit for the mouse TEa electrophysiology; if it is not public\n    the claim is blocked data_missing.\n- id: figs3g-morphology-input-resistance\n  statement: Passive models built on reconstructed morphologies explain input resistance\n    variability in human (R2 = 0.35) but not mouse (R2 = 0.03) LAMP5 cells.\n  source: Results, Cross-species differences in L1, paragraph 3; Figure S3G\n  quote: Simulations of passive biophysical models based on reconstructed morphologies showed that\n    input resistance variability in human but not mouse L1 cells can be explained by morphology\n  statistics:\n  - about: human\n    test: linear regression\n    statistic: R2 = 0.35\n    p: 4.0e-6\n  - about: mouse\n    test: linear regression\n    statistic: R2 = 0.03\n    p: 0.46\n  data: elsewhere\n  where: Brain Image Library doi:10.35077/g.606 (reconstructions) and the Allen Cell Types model\n    for specimen 475585413 (celltypes.brain-map.org)\n- id: figs3e-k-channel-genes\n  statement: Genes for A-type K+ channels (KCND2, KCND3, KCNH7) are more highly expressed in mouse\n    than human L1 neurons and correlate with action potential features.\n  source: Results, Cross-species differences in L1, paragraph 3; Figure S3E\n  quote: the expression of genes (KCND2, KCND3, and KCNH7) associated with fast inactivating, A-type\n    K+ channels ... was higher in mouse neurons and was correlated with several action potential\n    features\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.8310226 (data/ps_human.RData, ps_mouse.RData) and NeMO\n- id: fig3f-a-type-conductance\n  statement: In nucleated patches, mouse L1 neurons have much higher A-type K+ conductance than\n    human, with comparable D-type conductance.\n  source: Results, Cross-species differences in L1, paragraph 3; Figure 3F\n  quote: Compared with human neurons, mouse neurons showed much higher A-type K+ conductance but\n    comparable slow inactivating (D-type) conductance\n  data: with_inputs\n  criterion: The paper reports no test for this panel. Conductance per the Methods (Voltage clamp\n    experiments) from the nucleated-patch sweeps, IKA as total minus current after a step to -20\n    mV, IKD as that current minus the sustained current, conductance with EK = -100 mV, divided\n    by patch surface area. Which step gives each cell's value is not fixed; readings (a) the +70\n    mV step, (b) the maximum over steps. Compared with the paper's cross-species test, two-sided\n    Mann-Whitney (Methods). Reproduced when, under both readings, mouse A-type density is higher\n    at p < 0.05 and D-type does not differ at p < 0.05. Needs the nucleated-patch sweeps in the\n    dandiset, the patch diameters (measured from images, Fig. 3F) and mouse LAMP5 recordings\n    whose deposit the paper does not name; the claim is blocked for whichever is missing.\n- id: fig3g-variability-dimensions\n  statement: Human and mouse L1 subclasses have a similar amount of morpho-electric variability but\n    along different features; sag and spike shape adaptation vary in human but little in mouse,\n    while ISI adaptation and AHP vary in mouse.\n  source: Results, Cross-species differences in L1, paragraph 4; Figure 3G\n  quote: we found that the two species had a similar amount of variability (number of\n    significantly different features and their effect size) but varied along different sets of\n    features (Fig. 3G). The most distinct features in human, like sag and spike shape adaptation,\n    showed little variability in mouse, and unlike in human, mouse subclasses varied\n    physiologically in ISI adaptation and spike after-hyperpolarization (AHP) properties\n  data: with_inputs\n  criterion: Electrophysiology only. As l1_subclass_distinctness.ipynb cells 10 and 37. Human,\n    the set of fig2c-subclass-ephys-differences; mouse, VISp cells of the strict mouse set with\n    l1_type and features more than 40% non-missing; per species a Kruskal-Wallis test per feature\n    across subclasses, epsilon2 = H/(n-1), Benjamini-Hochberg. Reproduced when (i) sag and\n    upstroke_adapt_ratio have FDR p < 0.05 in human and a smaller epsilon2 in mouse, and (ii) at\n    least one ISI adaptation feature (isi_adapt_ratio, adapt_mean or adapt_hero) and one AHP\n    feature (fast_trough_deltav_rheo, fast_trough_deltav_hero, trough_slowdeltav_rheo,\n    trough_slowdeltav_hero or ahp_delay_ratio_hero) have FDR p < 0.05 in mouse and a larger\n    epsilon2 than in human. \"Similar amount\" is not defined by the paper; the count of FDR\n    significant features and their mean epsilon2 are reported for both species and called\n    similar when each mouse value is within 10% of the human one, a reading named here, not\n    part of the outcome.\n- id: fig4b-mc4r-sag-irregularity\n  statement: MC4R (rosehip) cells are distinguished from the rest of human L1 by strong sag and by\n    irregular firing (Mann-Whitney, FDR p < 1e-4).\n  source: Figure 4B legend; Results, Rosehip cells, paragraph 1\n  quote: Electrophysiological and morphological features distinguishing MC4R t-types (FDR-corrected\n    MW test vs. rest of L1, p<10−4)\n  statistics:\n  - test: Mann-Whitney test against rest of L1\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: FDR\n  data: with_labels\n  criterion: As l1_rosehip.ipynb cell 6. AIBS cells of the strict L1 set, in group against all\n    other cells of that set; two-sided exact Mann-Whitney per feature (run_twosamp),\n    Benjamini-Hochberg across all features. Features of Fig. 4B, sag and ir_late_mean\n    (irregularity ratio, O1). The group is read as (a) the MC4R subclass, as the code does, or (b)\n    each MC4R t-type in turn, as the legend's \"MC4R t-types\" allows. Reproduced when, under a\n    reading, both features have FDR p < 1e-4 with the group higher.\n- id: fig4b-adarb2-irregular-firing\n  statement: Both rosehip t-types have strong sag, but only ADARB2 MC4R fires irregularly, with\n    stronger and faster sag than SST CHRNA4.\n  source: Results, Rosehip cells, paragraph 1; Figure 4B\n  quote: Electrophysiologically, both t-types that comprise the MC4R subclass showed strong sag,\n    but only the ADARB2 MC4R t-type showed the distinctive irregular firing (45) and stronger and\n    faster sag\n  statistics:\n  - test: Dunn's test post hoc to Kruskal-Wallis\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n  data: with_labels\n  criterion: As l1_rosehip.ipynb cell 9. Cells of P grouped as LAMP5, SST CHRNA4, ADARB2 MC4R,\n    PAX6, L1 VIP (other left out); Kruskal-Wallis and Dunn's tests on the seven pairs the code\n    lists (each MC4R t-type against LAMP5, PAX6 and L1 VIP, and CHRNA4 against ADARB2),\n    Benjamini-Hochberg across pairs. Reproduced when (i) ADARB2 MC4R has a higher ir_late_mean\n    than SST CHRNA4 with FDR p < 0.05, (ii) SST CHRNA4's ir_late_mean does not exceed LAMP5's,\n    PAX6's or L1 VIP's with FDR p < 0.05, (iii) both MC4R t-types have a higher median sag than\n    LAMP5 and PAX6, and (iv) ADARB2 MC4R has a higher median sag and a shorter median sag_peak_t\n    than SST CHRNA4. The Dunn p for every pair is reported.\n- id: fig4b-mc4r-axon\n  statement: MC4R cells are quantitatively distinct from other L1 types in maximum axonal path\n    distance and axon branch frequency.\n  source: Results, Rosehip cells, paragraph 1; Figure 4B\n  quote: were quantitatively distinct from other L1 types in terms of maximum axonal path distance\n    and branch frequency\n  statistics:\n  - test: Mann-Whitney test against rest of L1\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: FDR\n  data: elsewhere\n  where: Brain Image Library doi:10.35077/g.606; features in Zenodo doi:10.5281/zenodo.8310226\n- id: fig4c-mc4r-genes\n  statement: HTR1F marks the rosehip subclass, and GRM5 and RELN are lower in ADARB2 MC4R than in\n    SST CHRNA4 neurons.\n  source: Results, Rosehip cells, paragraph 1; Figure 4C\n  quote: found markers distinguishing the entire rosehip subclass from the rest of L1, including\n    HTR1F (5HT receptor 1F), along with markers distinguishing the rosehip subtypes ... GRM5\n    (metabotropic glutamate receptor 5) and RELN (Reelin) showed lower expression in ADARB2 MC4R\n    neurons\n  data: elsewhere\n  where: Allen Brain Map human MTG snRNA-seq reference\n- id: fig4d-mouse-no-rosehip-ephys\n  statement: The mouse MC4R subclass has moderate sag but no irregular spiking; irregular spiking\n    occurs only in a subset of mouse LAMP5 cells (mainly Lamp5 Ntn1 Npy2r) without other\n    rosehip features.\n  source: Results, Rosehip cells, paragraph 2; Figure 4D\n  quote: the homologous mouse MC4R subclass had moderate sag but no irregular spiking (Fig. 4D).\n    Irregular spiking resembling the human ADARB2 MC4R rosehip t-type was present only in a\n    subset of LAMP5 cells (primarily Lamp5 Ntn1 Npy2r) that did not have other rosehip-like\n    features\n  data: with_inputs\n  criterion: As l1_rosehip.ipynb cells 4 and 36. Mouse cells of the strict mouse set with\n    primary_ephys (VIS, failed_qc False), sag above 0.5 set missing; Dunn's tests over all\n    subclass pairs. Irregular is ir_late_mean above 0.4, the cut the code uses to list such\n    cells (cells 39 and 42). Reproduced when the mouse MC4R median sag exceeds mouse LAMP5's,\n    no mouse MC4R cell has ir_late_mean above 0.4 or such cells are a minority, and most mouse\n    cells above 0.4 are LAMP5, the largest group Lamp5 Ntn1 Npy2r. Whether \"no irregular\n    spiking\" admits a few cells is open; readings (a) none, (b) a minority; both reported.\n- id: fig5b-tnfaip8l3-ephys\n  statement: PAX6 TNFAIP8L3 cells are distinguished from all other human L1 cells by a high initial\n    firing rate at rheobase and an after-depolarization following the last spike.\n  source: Results, Bursting PAX6 TNFAIP8L3 cells, paragraph 1; Figure 5B\n  quote: Both the initial firing rate at rheobase and the after-depolarization potential (ADP)\n    following the final spike quantitatively distinguished PAX6 TNFAIP8L3 cells from all other L1\n    cells\n  statistics:\n  - test: Mann-Whitney test against rest of L1\n    p: 0.01\n    p_relation: \"<\"\n    corrected: FDR\n    n: 2 PAX6 TNFAIP8L3 cells with electrophysiology (Table S2) against the rest of L1\n  data: with_labels\n  criterion: As l1_tnfaip.ipynb cells 10, 12 and 14. Cells of P, PAX6 TNFAIP8L3 against all\n    others; features more than 50% non-missing among TNFAIP8L3 cells plus adp_deltav\n    (adp_v_last_rheo - threshold_v_rheo); two-sided exact Mann-Whitney per feature,\n    Benjamini-Hochberg. Features of Fig. 5B, first_isi_inv_rheo and postap_slope_rheo (labelled\n    \"ADP slope\", O1); adp_deltav is shown as a variant. Reproduced when both have FDR p < 0.01\n    with TNFAIP8L3 higher. With 2 cells the smallest possible two-sided exact p is about 1e-4,\n    so the threshold can be met.\n- id: fig5b-tnfaip8l3-dendrites\n  statement: PAX6 TNFAIP8L3 cells have more dendritic branches and a horizontal dendritic extent\n    over 550 um wide.\n  source: Results, Bursting PAX6 TNFAIP8L3 cells, paragraph 1; Figure 5B\n  quote: as did the number of dendritic branches and large horizontal dendritic extent, over 550\n    microns wide\n  statistics:\n  - test: Mann-Whitney test against rest of L1\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n  data: elsewhere\n  where: Brain Image Library doi:10.35077/g.606; features in Zenodo doi:10.5281/zenodo.8310226\n- id: fig5d-mouse-pax6-doublets\n  statement: Mouse PAX6 subclass cells (Lamp5 Krt73) fire doublets at stimulus onset and show a\n    depolarizing hump just below rheobase, marking them as alpha7 cells.\n  source: Results, Bursting PAX6 TNFAIP8L3 cells, paragraph 2; Figure 5D\n  quote: In mouse L1, the homologous PAX6 subclass was extremely rare, comprising only a few cells\n    in the Lamp5 Krt73 t-type. These cells tended to fire in doublets at stimulus onset ... Mouse\n    doublet-firing cells also showed a depolarizing ‘hump’ for current injection just below\n    rheobase\n  data: with_inputs\n  criterion: As l1_tnfaip.ipynb cells 20 and 23. Mouse cells with primary_ephys by subclass and\n    t-type; first_isi_inv_hero and sag_depol (depolarizing sag ratio, O1). The paper reports no\n    test; reproduced when the Lamp5 Krt73 cells' median first_isi_inv_hero and median sag_depol\n    both exceed those of every other mouse subclass. The 4 Lamp5 Krt73 cells' values are listed.\n- id: fig5c-cacna1g\n  statement: Both human PAX6 t-types match the alpha7 marker signature and strongly express the\n    T-type calcium channel gene CACNA1G.\n  source: Results, Bursting PAX6 TNFAIP8L3 cells, paragraph 3; Figure 5C\n  quote: and strongly expressed the T-type calcium channel alpha subunit gene CACNA1G\n  data: elsewhere\n  where: Allen Brain Map human MTG snRNA-seq reference\n- id: fig6a-ephys-dprime-subclass-structure\n  statement: Pairwise electrophysiological distinctness (d') of human L1 t-types is smaller within\n    subclasses than between them; the only within-subclass pair with high d' is LAMP5 NMBR\n    against LAMP5 LCP2.\n  source: Results, Cross-modality relationships of L1 subclasses and t-types, paragraph 1;\n    Figure 6A\n  quote: The resulting t-type similarity matrices (Fig. 6A) showed comparable subclass structure in\n    both electrophysiology and transcriptomics, with smaller d’ values within subclass blocks and\n    higher values outside ... The single within-subclass pair with a high d’ was LAMP5 NMBR and\n    LAMP5 LCP2\n  data: with_labels\n  criterion: As l1_dprime.ipynb cells 9 to 13 and cluster_pairs.py. Cells of P; t-types with at\n    least 5 cells (code) or at least 4 (legend, \"Groups with N<4 excluded\"), both run; features\n    more than 80% non-missing; RobustScaler, KNN imputation, per-feature LocalOutlierFactor <\n    -20 set missing, KNN imputation again; for each t-type pair a random forest (scikit-learn\n    defaults, class_weight balanced_subsample) scored by 5-fold stratified cross_val_predict\n    probabilities; d' = sqrt(2) times the inverse normal of the ROC AUC, AUC of 1 replaced by\n    (n-1)/n. Random seeds are a standard choice (unset in the code); the matrix is reported for\n    the seed used. \"High\" is not fixed; readings (a) d' >= 2.2, the Methods' threshold for\n    grouping t-types, (b) d' above the median between-subclass d'. Reproduced when, under both\n    readings, NMBR-LCP2 is the only within-subclass pair that is high and the mean within-subclass\n    d' is below the mean between-subclass d'. Within-subclass pairs are those inside LAMP5, MC4R\n    and PAX6 (other is not a subclass, as get_distances in the code treats it).\n- id: fig6b-dprime-correlation\n  statement: Electrophysiological and transcriptomic d' of human L1 t-type pairs are correlated\n    (Pearson r = 0.59, p = 0.00016).\n  source: Results, Cross-modality relationships of L1 subclasses and t-types, paragraph 1;\n    Figure 6B\n  quote: d’ metrics were highly correlated between modalities, demonstrating that cell types with\n    distinctive transcriptomes have similarly distinctive electrophysiological properties (Pearson\n    r=0.59, p=0.00016\n  statistics:\n  - test: Pearson correlation\n    statistic: r = 0.59\n    p: 0.00016\n  expected:\n    quantity: Pearson r between electrophysiology and transcriptomic t-type pair d'\n    value: 0.59\n    tolerance: 0.059\n  data: with_inputs\n  depends_on:\n  - fig6a-ephys-dprime-subclass-structure\n  criterion: As l1_dprime.ipynb cells 49 to 51 and 83. Electrophysiology d' from\n    fig6a-ephys-dprime-subclass-structure (code reading, at least 5 cells); patch-seq\n    transcriptomic d' from the zero-inflated negative binomial discriminant (Methods) on the human\n    MTG marker genes, 4 folds, over t-types of l1_type cells; Pearson r over the t-type pairs\n    present in both matrices. The input scale is open; readings (a) CPM, as the Methods say for d'\n    analyses, (b) log(CPM+1), as the code passes. Reproduced when, under both readings, r is within\n    tolerance and p < 0.05. The ZINB curve fits (zinb_human.h5) are not public; they are refitted\n    as the Methods describe (phi by spline, pi by sigmoid against the NB mean) and the notes say\n    so.\n- id: fig6c-subclass-distinctness-species\n  statement: Subclasses are more transcriptomically distinct in human than mouse, and in mouse the\n    VIP subclass is highly distinct in all modalities while the others are less so.\n  source: Results, Cross-modality relationships of L1 subclasses and t-types, paragraph 1;\n    Figure 6C\n  quote: These results confirmed the generally higher transcriptomic distinctness of subclasses in\n    human and show that in mouse the VIP subclass was highly distinct in all modalities, with\n    other subclasses generally less distinct\n  data: elsewhere\n  where: Zenodo doi:10.5281/zenodo.8310226 (data/ps_human.RData, ps_mouse.RData), DANDI 000020\n    and Brain Image Library doi:10.35077/g.606\n- id: fig6d-gmm-subclass-f1\n  statement: Two-cluster Gaussian mixtures on the best pair of electrophysiological features\n    recover each subclass with F1 scores of 0.81 (LAMP5), 0.69 (MC4R), 0.89 (PAX6) and 0.5 (all\n    others).\n  source: Results, Cross-modality relationships of L1 subclasses and t-types, paragraph 2;\n    Figure 6D legend\n  quote: F1 scores ... LAMP5 0.81, MC4R 0.69, PAX6 0.89, all others 0.5\n  expected:\n  - quantity: F1, LAMP5\n    value: 0.81\n    tolerance: 0.081\n  - quantity: F1, MC4R\n    value: 0.69\n    tolerance: 0.069\n  - quantity: F1, PAX6\n    value: 0.89\n    tolerance: 0.089\n  - quantity: F1, all others (L1 VIP and ungrouped t-types)\n    value: 0.5\n    tolerance: 0.05\n  data: with_labels\n  criterion: As clustering_classification.ipynb cells 16 to 21 and clustering.py. Cells of P with\n    l1_type and soma in L1; features more than 60% non-missing; Yeo-Johnson power transform and\n    KNN imputation (the legend confirms Yeo-Johnson); L1 VIP and other merged as \"all others\".\n    For each group, every single feature and every pair, a 2-component Gaussian mixture\n    (k-means init, 5 inits) fitted to the unlabelled data, the component holding most of the\n    group's cells taken as the group, F1 against the labels; the best subspace (1 or 2 features)\n    is kept. Preprocessing follows O3; readings (a) and (b). Random seed 0 as the code sets.\n    Reproduced when, under both readings, all four F1 values are within tolerance; partially\n    reproduced when three are.\n- id: figs8a-classifier-cv\n  statement: A multi-class classifier assigns human L1 subclasses from electrophysiology with 82%\n    cross-validated accuracy, balanced across subclasses.\n  source: Results, Cross-modality relationships of L1 subclasses and t-types, paragraph 2;\n    Figure S8A\n  quote: A multi-class classifier evaluated by cross-validation on the primary dataset had 82%\n    accuracy balanced across subclasses\n  expected:\n    quantity: cross-validated subclass accuracy, primary dataset\n    value: 82\n    tolerance: 8.2\n    unit: percent\n  data: with_labels\n  criterion: As clustering_classification.ipynb cells 26 to 35 and 44 to 45, and the Methods\n    (Clustering and classification). Cells of the strict L1 set in the four core subclasses with\n    soma in L1, AIBS and long-square features extracted; logistic regression with balanced class\n    weights after RobustScaler and KNN imputation, preprocessing per O3; repeated stratified\n    5-fold cross-validation (scikit-learn defaults, 10 repeats). The number can be read several\n    ways, each run; features (a) those more than 50% non-missing at every site (cell 45), (b)\n    the site-aligned subset (cell 35, see figs8b-classifier-holdout); score (i) accuracy, as the\n    code prints, (ii) balanced accuracy, the mean diagonal of the row-normalized confusion\n    matrix, as the text's \"balanced across subclasses\" allows. Reproduced when any reading is\n    within tolerance.\n- id: figs8b-classifier-holdout\n  statement: Trained on the primary dataset with site-dependent features excluded, the classifier\n    reaches 81% accuracy on held-out cells recorded at other sites.\n  source: Results, Cross-modality relationships of L1 subclasses and t-types, paragraph 2;\n    Figure S8B\n  quote: After excluding features for which the distributions strongly differed from the primary\n    dataset, we found comparable classification performance (81%, Fig. S8B)\n  expected:\n    quantity: subclass accuracy on held-out Amsterdam and Szeged cells\n    value: 81\n    tolerance: 8.1\n    unit: percent\n  data: with_labels\n  criterion: As clustering_classification.ipynb cells 26 to 38 and the Methods. Features more\n    than 50% non-missing at every site; a one-way ANOVA (OLS, HC3) of each on site (AIBS,\n    Amsterdam, Szeged), features with p < 0.05 or R2 > 0.05 excluded (Methods; the code keeps p >\n    0.05 and R2 < 0.05, the same rule); classifier as figs8a-classifier-cv fitted on all AIBS\n    cells; scored on the Amsterdam and Szeged cells of the four core subclasses with soma in L1.\n    Score readings (i) accuracy, as the code prints, (ii) balanced accuracy. Reproduced when\n    either is within tolerance. The held-out cells are part of the paper's recordings; if the\n    dandiset does not hold them the claim is blocked data_missing.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 tools/claims_check.py claims/000630/10.1126-science.adf0805.yaml paper/10.1126-science.adf0805.txt; grep -n "—\|rather" claims/000630/10.1126-science.adf0805.yaml; grep -nE "^[^#]*[^\"']: [^|>]" claims/000630/10.1126-science.adf0805.yaml | grep -vE "^\s*[0-9]+:\s*-? ?[a-z_]+: " | head
```

Result: not kept, because it reads the paper's text.

**Agent**

All 39 quotes and 24 statistical values check out. Last, a scan of every string value for ": " and for dashes.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/000630/10.1126-science.adf0805.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str):
        if ': ' in x or '—' in x or ' rather' in x: print(p, x[:80])
walk(d)
from collections import Counter
print(Counter(c.get('data','dataset') for c in d['claims']))
print(sum('statistics' in c for c in d['claims']), sum('criterion' in c for c in d['claims']), sum('expected' in c for c in d['claims']))
EOF
git status --short
```

```
Counter({'elsewhere': 18, 'with_labels': 14, 'with_inputs': 7})
21 24 8
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
?? claims/000630/
?? scripts
```

**Agent**

I've written `claims/000630/10.1126-science.adf0805.yaml`: 39 claims. The quote checker finds all 39 quotes and all 24 statistical values, with 0 problems. Nothing is committed.

**Text read.** I used the author manuscript of the version of record from PubMed Central (PMC11864503). It includes the main text, the legends of Figs 1 to 6, and the supplementary PDF: Materials and Methods, legends of Figs S1 to S9, and Tables S1 and S2. I opened no figures and did not use the bioRxiv preprint.

**Missing from the paper.** The four supplementary data tables (Data S1 to S4, .xlsx) are not under `paper/`. They hold the per-feature statistics. Each claim rests on the sentence or legend it quotes, and the code that wrote Data S2 and S4 stands in for them. I went ahead because the results are stated in the text, as an earlier file for a related Allen Institute paper (dandiset 000636) did. The cost is that no per-feature p-values or effect sizes could be recorded.

**Code read.** github.com/AllenInstitute/patchseq_human_L1 at commit 7777857 (archived on Zenodo as 10.5281/zenodo.8310226). It settles the cell selections, feature filters, tests, FDR correction and classifier settings. The opening comment describes what it holds.

**Claims.**
- 39 claims, all with quotes.
- 21 have statistics, 24 have criteria, 8 have expected values.
- By data source:
  - **14 `with_labels`:** human electrophysiology from the dandiset, with cell-type labels from the code's per-cell table.
  - **7 `with_inputs`:** mouse electrophysiology from DANDI 000020, transcriptomes, or nucleated-patch data.
  - **18 `elsewhere`:** morphology at the Brain Image Library, transcriptomics references, MERFISH and cytoarchitecture data.

The dandiset holds human electrophysiology only (210 files). The author still has to write the link claim matching its files to the code's table.

**Details the paper leaves open, with the readings named:**
- **O1, custom feature definitions.** The adaptation ratio's order, the irregularity ratio, the post-AP slope ("ADP slope"), the ADP voltage and depolarizing sag come from unreleased IPFX code. Readings: (a) the Methods' definitions; (b) the paper's own per-cell feature values, used as a check.
- **O2, cross-species ANOVA.** The Fig. 3D legend says ANOVA on ranks and the Data S4 description says Type II. The code uses raw values, Type I. Both are named.
- **O3, classifier and clustering preprocessing.** The Methods include outlier removal and dropping cells missing over 60% of features; the code does neither for the subclass classifier or the clustering search. Both are named.
- **Fig 6A.** Minimum group size: the legend says at least 4 cells, the code 5. "High d′": d′ ≥ 2.2 (the Methods' threshold for grouping t-types) or above the median between-subclass d′.
- **Fig 6B.** Transcriptomic input scale: CPM (Methods) or log(CPM+1) (code).
- **Fig S8A.** The 82% is read four ways: plain or balanced accuracy, crossed with full or site-aligned features. Fig S8B: plain or balanced accuracy.
- **Fig 4B.** The group compared with the rest of L1: the MC4R subclass or each MC4R t-type.
- **Fig 3F.** The voltage step for each cell's conductance: the +70 mV step or the maximum over steps.
- **Fig 4D.** "No irregular spiking": none, or a minority of cells.
- **Fig 3G.** "Similar amount of variability" is reported, not judged, with a 10% reading.
- **Random seeds** are a standard choice.

**Missing data a claim needs:**
- The file used to constrain the transcriptomic d′ fits for Fig 6B (`zinb_human.h5`) is not public; it is to be refitted from the Methods.
- The paper names no deposit for the mouse TEa electrophysiology (Fig 3E) or the mouse nucleated patches (Fig 3F).
- Nucleated-patch areas come from images.
- I could not tell whether the dandiset holds the Amsterdam and Szeged held-out cells needed for Fig S8B and the LAMP5 within-subclass trend (Fig 2C).
- Only 2 PAX6 TNFAIP8L3 cells have electrophysiology. The Fig 5B test can still reach its threshold.

## End of run

43 turns, 10 minutes, result: success.
