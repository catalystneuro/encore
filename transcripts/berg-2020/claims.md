# 000023 · claims · run 39697791658

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000023 paper/;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md | sed -n '60,400p'
```

```
finding.
   - `expected`: each reported number the claim rests on, with a tolerance.
     Use the paper's own uncertainty when it gives one (a confidence
     interval, or the stated spread); otherwise 10% of the reported value.
     For a reported range ("2 to 13%"), the claim holds inside the range
     widened by 10% of each bound. Give the reason for any other tolerance.
   - `criterion`: how the claim will be judged, for any claim that is not
     settled by its expected values alone ("similar", "many", "tended to").
     It is written from the paper alone, before anyone analyses the data.
   - When a reported number can be read in more than one way (which trials
     form the denominator, which subset is meant), list in the criterion the
     readings the paper's text plausibly allows, before the analysis. The
     claim is reproduced if the result matches under any of them. The
     notebook shows every reading, the notes say which ones match, and the
     ambiguity is recorded as a deviation.
   - Methods come from the paper, never from the author. Every part of a
     criterion's method (the selection, the measure, the test, windows,
     bins, thresholds, what a measure is compared with) is taken from the
     Methods, the figure legends, the supplement, or the code the paper
     links, and the criterion says which. Search all of them before
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md | sed -n '1,60p'; cat claims/001453/*.yaml | head -250; wc -l claims/001453/*.yaml paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

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
wc -l paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2020.03.31.018820.txt",
 "offset": 41,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2020.03.31.018820.txt",
 "offset": 160,
 "limit": 200
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i -B2 -A5 "supplement" docs/pilot-notes.md | head -80; ls claims/; ls tools/
```

```
940-on the dandiset, plus one claim using outside data, not reproduced; both
941-rounds agreed with every outcome. The dandiset holds only the fiber
942:photometry of Figure 6 and Supplementary Figures 7 and 8; the imaging,
943-proteomics and blots behind Figures 1 to 5 are in other archives, so those
944-eight claims are blocked. The paper's source data and analysis code are
945-public, and the author used the source data in one link claim that checks
946-the dandiset against the published traces.
947-
--
1118-block that follows from treating it as one spreads to latency results that
1119-match the paper; no rule for how to compute a false-positive rate; "the
1120:stated spread" for a mean and SD over cells; supplementary material and a
1121-dandiset that holds one of two subjects; counting each recording once
1122-against matching counts that include duplicated units; a stimulus that
1123-differs between conditions, which fits no finding kind; absence claims with
1124-many tests; and no field in the attempt schema for the code repository and
1125-commit read.
--
1141-paper reports that LRRK2 impairs the release sites of dopamine axons
1142-vulnerable in Parkinson's disease, in G2019S mice. The ten photometry claims of Figure 6 and
[... 202 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rn "000023" docs/*.md targets* 2>/dev/null | head; ls; curl -s https://api.dandiarchive.org/api/dandisets/000023/ | head -c 1500
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 390,420p targets/dandisets.json; curl -s https://api.dandiarchive.org/api/dandisets/000023/versions/0.210914.1900/info/ | python3 -c "import json,sys; d=json.load(sys.stdin)['metadata']; print(d.get('description')); print(d.get('relatedResource')); print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent**

Now the paper's code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/AllenInstitute/patchseq_human_L23 && cd patchseq_human_L23 && git log -3 --format='%H %ad %s' && find . -type f -not -path './.git/*' | head -100 && cat README* | head -60
```

```
3daf9f0803ea0c220a040ea523f23af5f93c56ac Fri Sep 17 21:44:26 2021 -0700 Update codes 4 and 5
a7d2b59895c69bdc9eb0e653b958627790945845 Fri Sep 17 21:24:49 2021 -0700 Update all of the R scripts
0d6f96229650d4fdcbcbc5fdf354d64ea56aa089 Fri Sep 17 21:23:52 2021 -0700 Update README.md
./scripts/README.md
./scripts/Code8_cortical_depth_code_mouse_TEa.r
./scripts/Code7_cortical_depth_code_mouse.r
./scripts/Code6_cortical_depth_code_human.r
./scripts/Code5_human_patchseq_mapping_L23exc.nb.html
./scripts/Code5_human_patchseq_mapping_L23exc.Rmd
./scripts/Code4_mouse_patchseq_visualization_L23exc.nb.html
./scripts/Code4_mouse_patchseq_visualization_L23exc.Rmd
./scripts/Code3_FREM3_crossSpeciesComparisons.nb.html
./scripts/Code3_FREM3_crossSpeciesComparisons.Rmd
./scripts/Code2_prepare_data_L23exc.nb.html
./scripts/Code2_prepare_data_L23exc.Rmd
./scripts/Code1_prepareComparisonDataSets.nb.html
./scripts/Code1_prepareComparisonDataSets.Rmd
./python_scripts/requirements.txt
./python_scripts/pathology_analysis_updated.ipynb
./python_scripts/pathology_analysis.ipynb
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L23 && cat scripts/README.md python_scripts/README.md python_scripts/requirements.txt; cat python_scripts/hivscc_data.py
```

```
# Overview
This folder contains the analysis scripts.  Prior to running these scripts, download all of them into your **main working directory** (*not* a scripts subdirector).  Then run the scripts in order and follow any additional directions indicated below or within the scripts.  

# List of scripts

This document is divided into two sections based on which programming language was used for the scripts.  The R scripts should be run prior to running the python scripts, as the python scripts required cluster calls for the human Patch-seq cells (which are geenrated using R).  If only the Python scripts are to be run, we provide cluster calls for Patch-seq cells in the `data` directory.

## R scripts

To replicate the figures in the paper, please use the code below:  

1. **Code 1. Download and prepare the dissociation data** [(LINK TO SCRIPT)](http://htmlpreview.github.io/?https://github.com/AllenInstitute/patchseq_human_L23/blob/master/scripts/Code1_prepareComparisonDataSets.nb.html)  This script converts RNA-seq data downloaded from the [Allen Institute Cell Types Database](http://celltypes.brain-map.org/rnaseq) into a format compatible for use as comparison data to human and mouse Patch-seq.  
2. **Code 2. Complete preparation for dissociation and Patch-seq data** [(LINK TO SCRIPT)](http://htmlpreview.github.io/?https://github.com/AllenInstitute/patchseq_human_L23/blob/master/scripts/Code2_prepare_data_L23exc.nb.html).  This script prepares the data for comparing mouse VISp and ALM to human MTG using dissociated and Patch-seq in superficial cortical layers, and outputs the results as R objects for remaining R scripts, **and outputs feather files for python scripts**.  
3. **Code 3. Re-analysis and visualization of FACS data** [(LINK TO SCRIPT)](http://htmlpreview.github.io/?https://github.com/AllenInstitute/patchseq_human_L23/blob/master/scripts/Code3_FREM3_crossSpeciesComparisons.nb.html).  This script performs some statistical analyses and makes some UMAP plots
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L23/python_scripts && cat hivscc_analysis.py; for f in *.ipynb; do echo "=== $f"; python3 -c "
import json,sys
nb=json.load(open('$f'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print('--- cell',i,c['cell_type'])
    print(src[:3000])
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain')
            if t: print('>>OUT:', ''.join(t)[:1500])
"; done > $TMPDIR/nbs.txt; wc -l $TMPDIR/nbs.txt
```

```
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import mannwhitneyu
from itertools import combinations
import statsmodels.formula.api as smf
import statsmodels.api as sm
from statsmodels.stats.multitest import multipletests
from statsmodels.stats.anova import anova_lm

def ols_model(data, formula_rhs, feature, anova_type=2, cov_type='HC3'):
    metrics = ['aic', 'bic', 'fvalue', 'f_pvalue', 'llf', 'rsquared', 'rsquared_adj', 'nobs']
    formula = f"{feature} ~ {formula_rhs}"
    res = smf.ols(formula=formula, data=data).fit(cov_type=cov_type)
    fit_dict = {name: getattr(res, name) for name in metrics}

    if anova_type:
        anova = anova_lm(res, typ=anova_type)
        pvals = anova["PR(>F)"].dropna().rename(lambda x: f"pval_{x}")
[... 315 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nbs.txt",
 "limit": 1200
}
```

```
1	=== classifier_and_species_analysis.ipynb
2	--- cell 0 markdown
3	# Import libraries
4	--- cell 1 code
5	
6	# load basic libraries
7	import pandas as pd
8	import numpy as np
9	from scipy import stats
10	import matplotlib.pyplot as plt
11	import matplotlib
12	# vizualisation library
13	import seaborn as sns
14	# add simple stat methods
15	from statistics import mean, stdev
16	import statsmodels.stats.multitest as multitest
17	from math import sqrt
18	# sklearn tools
19	#from sklearn.preprocessing import Imputer
20	from sklearn import preprocessing
[... 1180 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^=== " $TMPDIR/nbs.txt; sed -n '1200,1500p' $TMPDIR/nbs.txt | grep -v "^Random forest\|^>>OUT: <Figure\|^$"
```

```
1:=== classifier_and_species_analysis.ipynb
1322:=== gene_depth_analysis.ipynb
1443:=== morpho_electro_feature_analysis.ipynb
2711:=== morpho_electro_feature_projections.ipynb
3084:=== pathology_analysis.ipynb
3965:=== pathology_analysis_updated.ipynb
--- cell 66 code
print('Classifier precision: ' + str(np.mean(prec_all)))
print('Random precision: ' + str(np.mean(rand_all)))
>>OUT: Classifier precision: 0.4866666666666667
Random precision: 0.3266666666666667
--- cell 67 markdown
### Run the classifier on morpho-ephys of mouse
--- cell 68 code
random_forest_plot(mouse_morpho_ephys, mouse_morpho_ephys_labels, 'Mouse', feature_list, num_class, use_resampling=False)
#plt.savefig('Mouse_morpho_electro_3.pdf',format='pdf')
>>OUT: Random forest precision: 0.6666666666666666
>>OUT: (0.6666666666666666, 0.3333333333333333)
--- cell 69 code
prec_all=[]
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '1500,2711p' $TMPDIR/nbs.txt | grep -v "^>>OUT: <Figure\|^$"
```

```
<persisted-output>
Output too large (55.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/87a9a6ed-b70e-4fe4-8280-c647d944d1b8/tool-results/b3dauny89.txt

Preview (first 2KB):
    fig, ax = plt.subplots(figsize=(4, 3))
    utils.plot_box_cluster_feature(human_df, y=y, x='cluster', label=label, ax=ax, palette=palette, 
                                   invert_y=True, label_yaxis=True, label_color=True,)
#     plt.savefig(f'[removed: a home directory path]/figs/revision/final_plots_tc/boxplots_{y}.pdf', bbox_inches='tight', pad_inches=0)
    
sns.set(font_scale=1, style='ticks', context='notebook')
--- cell 8 code
features = [
    'L23_depth_normalized',
    'depth_from_pia_microns',
]
labels = [
    'normalized L2-3 depth',
    'depth from pia (μm)'
]
df = human_df.loc[lambda df: df[features].notna().all(axis=1)]
[... 32 more lines not kept]
```

**Agent**

I've read the paper (preprint v1, main text, Methods, Extended Data legends) and cloned the linked code; now reading the main feature-analysis notebook.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/87a9a6ed-b70e-4fe4-8280-c647d944d1b8/tool-results/b3dauny89.txt",
 "offset": 30,
 "limit": 700
}
```

```
30	    'normalized L2-3 depth',
31	    'depth from pia (μm)'
32	]
33	utils.plot_boxplot_multiple(human_df, features, labels=labels, figsize=(4,6), invert_y=True, label_yaxis=True, palette=palette,
34	                           pairs_sets=['all'])
35	# plt.savefig(f'[removed: a home directory path]/figs/revision/Figure 3/depth_boxplots.pdf', bbox_inches='tight', pad_inches=0)
36	--- cell 11 markdown
37	# Fig 4
38	--- cell 12 code
39	def f4_plot(y, label):
40	    fig, ax = plt.subplots(figsize=(3, 3))
41	    utils.plot_box_cluster_feature(human_df, y=y, x='cluster', label=label, ax=ax, palette=palette, pairs_sets=['all'])
42	--- cell 13 markdown
43	### Features ranked by number of significant pairwise cluster differences
44	--- cell 14 code
45	from statsmodels.stats import multitest
46	def mw_pair_count(df, features, cluster='cluster'):
47	    df = df.dropna(subset=[cluster])
48	    flat_pvals = []
49	    thresh = 0.05
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/87a9a6ed-b70e-4fe4-8280-c647d944d1b8/tool-results/b3dauny89.txt",
 "offset": 729,
 "limit": 600
}
```

```
729	feature                                                     
730	input resistance            73.0      3.263478e-12  0.615442
731	AP width                    73.0      1.337962e-09  0.524601
732	AP downstroke rate          73.0      1.555603e-08  0.471647
733	rheobase                    73.0      9.769518e-08  0.441945
734	time constant τ             73.0      3.599266e-07  0.400162
735	--- cell 78 code
736	data = mouse_df
737	data.cluster.cat.remove_unused_categories(inplace=True)
738	features = morph_df.columns
739	results = run_regressions(data, features, "cluster").rename(index=mfeat_dict)
740	# results.to_csv('[removed: a home directory path]/figs/supp_mouse_clusters_morph.csv')
741	results.head()
742	>>OUT: /local1/storage/envs/ipfx3/lib/python3.7/site-packages/statsmodels/regression/linear_model.py:903: RuntimeWarning: divide by zero encountered in log
743	  llf = -nobs2*np.log(2*np.pi) - nobs2*np.log(ssr / nobs) - nobs2
744	/local1/storage/envs/ipfx3/lib/python3.7/site-packages/statsmodels/base/model.py:1834: ValueWarning: covariance of constraints does not have full rank. The number of constraints is 2, but rank is 0
745	  'rank is %d' % (J, J_), ValueWarning)
746	/local1/storage/envs/ipfx3/lib/python3.7/site-packages/statsmodels/base/model.py:1850: RuntimeWarning: invalid value encountered in true_divide
747	  F /= J
748	/local1/storage/envs/ipfx3/lib/python3.7/site-packages/statsmodels/regression/linear_model.py:1715: RuntimeWarning: invalid value encountered in double_scalars
[... 366 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '2711,3084p' $TMPDIR/nbs.txt | grep -v "^>>OUT: <Figure\|^$\|FutureWarning\|isnaobj_old" | head -150
```

```
=== morpho_electro_feature_projections.ipynb
--- cell 0 code
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import RobustScaler, StandardScaler
from sklearn.decomposition import PCA, SparsePCA
from umap import UMAP
sns.set(style='ticks', context='notebook')
--- cell 1 code
from hivscc_data import load_data
import hivscc_analysis as utils
human_df, mouse_df, ephys_df, morph_df = load_data()
drop_neg = [
    'input_resistance',
    'fi_fit_slope',
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '3084,4807p' $TMPDIR/nbs.txt | grep -v "^>>OUT: <Figure\|^$\|FutureWarning\|isnaobj_old" | head -400
```

```
=== pathology_analysis.ipynb
--- cell 0 markdown
# Import 
--- cell 1 code
# load basic libraries
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib
# vizualisation libraries
import seaborn as sns
# csv
import csv
# pandas
import pandas as pd
# add simple stat methods
from statistics import mean, stdev
from math import sqrt
from scipy.stats import norm
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '3084,4807p' $TMPDIR/nbs.txt | grep -v "^>>OUT: <Figure\|^$\|FutureWarning\|isnaobj_old" | sed -n '400,1200p' | grep -v "^axs\|^n, bins\|^(mu\|^y = norm\|^data=" | head -400
```

```
# remove Na
>>OUT: (0.0, 3.0)
--- cell 28 markdown
# UMAP: pathological and normal cells
--- cell 29 code
# fix the random seed
np.random.seed=42
X = ephys_human_array
# create the embedding
reducer = umap.UMAP()
# create the embedding shape
embedding = reducer.fit_transform(X)
print('This is the UMAP shape')
embedding.shape
# plot the results
fig, ax = plt.subplots()
idx=np.argwhere(path_labels=='Epilepsy')
plt.scatter(embedding[idx, 0], embedding[idx, 1], c='green', s=[100])
idx=np.argwhere(path_labels=='Tumor')
plt.scatter(embedding[idx, 0], embedding[idx, 1], c='black', s = [100])
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '3965,4807p' $TMPDIR/nbs.txt | grep -v "^>>OUT: <Figure\|^$\|FutureWarning\|isnaobj_old\|warn" | grep -n "OUT\|provide_cell_ids(\|def \|thr\|dropna\|isin(\[\|cell_types\|Bonferroni\|FDR\|mannwhit" | head -80
```

```
31:def box_stripe_plot(feature_1,feature_2,label_1,label_2,title):
42:def box_stripe_plot_2(f1,f2,f3,f4,l1,l2,l3,l4,title,feature_units):
62:def compute_p_values(feature_names,cell_group,ephys_MET,norm_cell_ids,path_cell_ids,alpha_level=0.05,plot=True,save_plot=False):
92:                d,p=stats.mannwhitneyu(feature_1,feature_2)
115:def provide_cell_ids(path_info,my_data_MET_ephys,path_type,low_thr,high_thr):
118:    norm_donor_values=path_info.loc[path_info[path_type] <= low_thr ]['donor_id'].values
120:    path_donor_values=path_info.loc[path_info[path_type] > high_thr ]['donor_id'].values
143:>>OUT: [removed: a home directory path]/anaconda2/envs/hivscc/lib/python3.7/site-packages/pandas/core/indexing.py:190: SettingWithCopyWarning: 
147:>>OUT:      donor_id  GFAP Cortex  GFAP ctx ABC  Iba1 Cortex  SMI32 Cortex  Ki67  \
169:ephys_human=ephys_human.dropna(axis=0)
173:#cell_types=['Exc L2-3 LINC00507 FREM3','Exc L2 LAMP5 LTK','Exc L2-4 LINC00507 GLP2R']
174:#data_human=data_human.loc[data_human['SeuratMapping'].isin(cell_types)]
183:>>OUT: These are features being used
187: 'sag' 'tau' 'threshold_v_long_square' 'trough_v_long_square_rel'
201:>>OUT:     SpecimenID            sample_id    batch       donor collaborator  gender  \
281:>>OUT: Text(0.5, 15.0, 'Pathology score')
299:>>OUT: Max path score
372:>>OUT: (0.0, 3.0)
396:>>OUT: [removed: a home directory path]/anaconda2/envs/hivscc/lib/python3.7/site-packages/umap/umap_.py:328: NumbaWarning: 
399:def fuzzy_simplicial_set(
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L23/data && head -c 600 human_IVSCC_excitatory_L23_consolidated_0131.csv; echo; python3 -c "
import pandas as pd
h=pd.read_csv('human_IVSCC_excitatory_L23_consolidated_0131.csv',index_col=0)
print(h.shape); print(list(h.columns)); print(h.SeuratMapping.value_counts()); print(h.donor.nunique() if 'donor' in h else '')
e=pd.read_csv('human_mouse_ephys_all_0127.csv',index_col=0); print(e.shape, list(e.columns))
print(len(set(e.index)&set(h.index)))
"; head -3 ephys_feature_names.csv; cat ephys_feature_names.csv | wc -l
```

```
SpecimenID,sample_id,batch,donor,collaborator,gender,medical_conditions,region,hemisphere,age,ethnicity,depth_from_pia_microns,total_cortical_depth,L23_cell_depth,L23_total_thickness,L23_depth_normalized,flag,isTCX,postPatch,rna_amplification_call,marker_sum_norm,quality_score,contam_sum,contaminationType,SeuratMapping,SeuratMappingScore,Is_deep_FREM3
539733464,P0S4_160816_729_A01,285-813,H16.06.011,Lein,female,Epilepsy,temporal,right,24,Caucasian,NA,NA,NA,NA,NA,No,TRUE,nucleus_present,Pass,0.810416843,0.373486373,1.465320117,Astrocyte,Exc L2-3 LINC00507 FREM3,0.998843269,FALSE
539735184,P0S
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
raw_name,short_name,full_name,units_name
adapt_mean,adaptation,adaptation,adaptation
avg_rate_hero,mean rate,mean firing rate,mean firing rate (Hz)
19
Shell cwd was reset to
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L23/data && python3 -c "
import csv,collections
r=list(csv.DictReader(open('human_IVSCC_excitatory_L23_consolidated_0131.csv')))
print(len(r)); print(collections.Counter(x['SeuratMapping'] for x in r)); print(len(set(x['donor'] for x in r)))
print(collections.Counter(x['region'] for x in r)); print(collections.Counter(x['medical_conditions'] for x in r))
e=list(csv.DictReader(open('human_mouse_ephys_all_0127.csv'))); print(len(e), list(e[0].keys()))
ids=set(x['SpecimenID'] for x in r); print(sum(1 for x in e if x[list(e[0].keys())[0]] in ids))
print(sum(1 for x in r if x['L23_depth_normalized'] not in ('NA','')))
"; cat ephys_feature_names.csv
```

```
385
Counter({'Exc L2-3 LINC00507 FREM3': 205, 'Exc L2 LAMP5 LTK': 88, 'Exc L3-5 RORB COL22A1': 42, 'Exc L2-4 LINC00507 GLP2R': 30, 'Exc L3-4 RORB CARM1P1': 20})
82
Counter({'temporal': 329, 'frontal': 43, 'parietal': 9, 'occipital': 4})
Counter({'Epilepsy': 282, 'Tumor': 82, 'Both': 13, 'Hydrocephalus': 7, 'Other': 1})
447 ['specimen_id', 'adapt_mean', 'avg_rate_hero', 'downstroke_long_square', 'fast_trough_v_long_square_rel', 'fi_fit_slope', 'first_isi_hero_inv', 'input_resistance', 'latency_rheo', 'peak_v_long_square_rel', 'rheobase_i', 'sag', 'tau', 'threshold_v_long_square', 'trough_v_long_square_rel', 'upstroke_downstroke_ratio_long_square', 'upstroke_long_square', 'v_baseline', 'width_long_square']
316
304
raw_name,short_name,full_name,units_name
adapt_mean,adaptation,adaptation,adaptation
avg_rate_hero,mean rate,mean firing rate,mean firing rate (Hz)
downstroke_long_square,AP down,AP downstroke rate,AP downstroke rate (mV/ms)
fast_trough_v_long_square_rel,AHP,AP fast AHP,AP fast AHP (mV)
fi_fit_slope,f-I slope,f-I slope,f-I slope (Hz/pA)
first_isi_hero_inv,init rate,initial firing rate,initial firing rate (Hz)
input_resistance,Rin,input resistance,input resistance (MΩ)
latency_rheo,latency,latency,latency (sec)
peak_v_long_square_rel,AP height,AP height,AP height (mV)
rheobase_i,rheobase,rheobase,rheobase (pA)
sag,sag,sag,sag ratio
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
ls schemas; python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:9000])" 2>/dev/null || ls schemas
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
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
[... 329 more lines not kept]
```

**Agent calls Bash**

```bash
grep -il "patch-seq\|patchseq" claims/*/*.yaml; grep -h "^  data:" claims/*/*.yaml | sort | uniq -c
```

```
claims/000008/10.1038-s41586-020-2907-3.yaml
claims/000035/10.1038-s41586-020-2907-3.yaml
claims/001746/10.1038-s41556-026-02009-4.yaml
claims/001750/10.1038-s41556-026-02009-4.yaml
claims/001751/10.1038-s41556-026-02009-4.yaml
claims/001752/10.1038-s41556-026-02009-4.yaml
     44   data: dataset
    230   data: elsewhere
    147   data: with_inputs
     92   data: with_labels
```

**Agent calls Bash**

```bash
sed -n 1,140p claims/000008/10.1038-s41586-020-2907-3.yaml
```

```
# Claims for Scala, Kobak et al. (2021), "Phenotypic variation of transcriptomic cell types in
# mouse motor cortex", Nature 598:144-150, on dandiset 000008.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record, open access (CC BY), as served by Europe PMC (PMC8113357):
# main text, Methods, figure legends and Extended Data figure legends. Not in the text: the
# Extended Data Tables 1 and 2 (descriptions of the t-types), the Supplementary Files 1 to 3
# (galleries of morphologies and traces, dot plots of all features, the list of morphometric
# statistics) and the figures themselves. No PDF was supplied. No claim below rests on numbers
# that are only in those items; the Extended Data figures are read from their legends only.
#
# Code read: https://github.com/berenslab/mini-atlas at commit
# 3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9. It holds the analysis notebooks (feature extraction
# from the NWB files in preprocess-ephys-files.ipynb with ephys_extractor.py and
# ephys_features.py; t-type assignment; reduced-rank regression with sparseRRR.py; the
# t-SNEs, kNN family classifiers, normalized variances and Leiden entropies in
# phenotype-tsne.ipynb; the distance correlations of Fig. 4 and Extended Data Fig. 7 in
# families.ipynb; Extended Data Fig. 6 in physiological-temperature.ipynb) and the paper's
# preprocessed data: per-cell metadata (m1_patchseq_meta_data.csv, 1,329 cells, with t-type,
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A3 "data: elsewhere\|data: with_inputs" claims/000008/10.1038-s41586-020-2907-3.yaml | head -40; grep -c "^- id" claims/000008/10.1038-s41586-020-2907-3.yaml; python3 tools/claims_check.py --help 2>&1 | head -20
```

```
413:  data: elsewhere
414-  where: DANDI dandiset 000035 (physiological temperature recordings); features and metadata in
415-    mini-atlas data/m1_patchseq_phys_temp_* at commit 3bf98a524b8e48aa8647e1b9ae8f2351d9c712c9
416-  criterion: Recorded for coverage. The 34 degree recordings (185 neurons from 8 mice; Methods)
--
488:  data: with_inputs
489-  expected:
490-  - quantity: Pearson r over within-family pairs
491-    value: 0.60
--
520:  data: with_inputs
521-  criterion: As the code does it (families.ipynb, the loop over families) and the Extended Data
522-    Fig. 7 legend says. For each of the families Pvalb, Sst, Vip, Lamp5, IT and CT, t-types with
523-    at least 5 cells, Sst Chodl and Pvalb Vipr2_2 left out; transcriptomic distance over the 500
--
543:  data: with_inputs
544-  expected:
545-  - quantity: Pearson r
546-    value: 0.70
--
[... 31 more lines not kept]
```

**Agent**

I have what I need from the paper and the code. Writing the claims file now.

**Agent calls Bash**

```bash
cd $TMPDIR/patchseq_human_L23/data && python3 -c "
import csv,collections
r=list(csv.DictReader(open('human_IVSCC_excitatory_L23_consolidated_0131.csv')))
print(collections.Counter(x['hemisphere'] for x in r)); ages=[float(x['age']) for x in r if x['age'] not in ('NA','')]; print(min(ages),max(ages))
print(collections.Counter(x['gender'] for x in r))
" ; head -3 pathology_scoring.csv; wc -l pathology_scoring.csv
```

```
Counter({'right': 259, 'left': 126})
19.0 69.0
Counter({'male': 223, 'unknown': 83, 'female': 79})
donor_id,GFAP Cortex,GFAP ctx ABC,Iba1 Cortex,SMI32 Cortex,Ki67,NeuN Orientation Layering,Cellularity,Pvalb
H15.03.006.01.02,1.33333333333333,NA,0.666666666666667,0,3,0,1.33333333333333,1.33
H15.06.016.01.14,0.666666666666667,NA,0,0,0,0,0.666666666666667,3.00
91 pathology_scoring.csv
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "claims/000023/10.1101-2020.03.31.018820.yaml",
 "content": "# Claims for Berg, Sorensen, Ting, Miller et al. (2020), \"Human cortical expansion involves\n# diversification and specialization of supragranular intratelencephalic-projecting neurons\",\n# bioRxiv doi:10.1101/2020.03.31.018820, on dandiset 000023.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the bioRxiv preprint, version 1 (the version the dandiset names), from the bioRxiv\n# JATS XML flattened to text (paper/10.1101-2020.03.31.018820.txt): main text, Methods, figure\n# legends, Extended Data figure legends and the legends of Extended Data Tables 1 and 2. Not in\n# the text: the figures themselves (no PDF was supplied), the contents of Extended Data Table 1\n# (per-feature cross-species p-values and Cohen's d) and Table 2 (donors), and Supplementary\n# Data 1 (per-feature depth correlations and ANOVA results). Every claim below rests on numbers\n# that the main text or a legend states; the per-feature values in those items are not used.\n# A later version of record exists (Nature 598, 151-158, 2021) and was not read.\n#\n# Code read: https://github.com/AllenInstitute/patchseq_human_L23 at commit\n# 3daf9f0803ea0c220a040ea523f23af5f93c56ac (2021-09-17). It holds R scripts for the\n# transcriptomic analyses (Code1 to Code5) and soma size and density (Code6 to Code8); Python\n# notebooks for pathology (pathology_analysis.ipynb, and pathology_analysis_updated.ipynb for\n# the revision), the per-feature ANOVAs, depth regressions and boxplots\n# (morpho_electro_feature_analysis.ipynb with hivscc_analysis.py and hivscc_data.py), the\n# feature projections, and the random forest classifier and cross-species comparison\n# (classifier_and_species_analysis.ipynb); and data tables. The tables are a per-cell table of\n# the 385 human Patch-seq cells (data/human_IVSCC_excitatory_L23_consolidated_0131.csv, with\n# specimen ID, donor, region, medical condition, depth from pia, normalized L2/3 depth and the\n# Seurat t-type), the 18 electrophysiological features of human and mouse cells\n# (data/human_mouse_ephys_all_0127.csv), a mouse cell table, morphological features, donor\n# pathology scores (data/pathology_scoring.csv, 90 donors), FREM3 gene-depth results and the\n# soma size images' measurements. The repository was last updated for the Nature revision.\n# Several of its outputs differ from the preprint (316 human cells in the feature table against\n# the preprint's 283; homologous-type ANOVAs run on superficial FREM3 only; 2 of 18 pathology\n# comparisons significant in the updated notebook against 1 in the original). Where the\n# preprint's Methods and the code disagree, the criteria follow the Methods and name the\n# code's choice as a variant. Where the Methods are silent and the code settles a choice, the\n# criteria cite \"the code\".\n#\n# The data the paper used. Human neurosurgical tissue resected to reach deeper pathology\n# (mostly epilepsy and tumor cases; middle temporal gyrus for most cells, some frontal) from\n# donors listed in Extended Data Table 2, 90 donors per the Discussion. Acute slices of 350 um\n# were recorded at 32 to 34 degrees C in whole-cell current clamp (MIES, ITC-18, Bessel 10 kHz,\n# 50 kHz digitization, liquid junction potential of -14 mV not corrected; bias current held the\n# initial resting potential). Stimuli were short (3 ms) current pulses and long (1 s) current\n# steps. Cell QC was a seal above 1 GOhm, initial access resistance below 20 MOhm and below 15%\n# of input resistance; sweep QC was bridge balance below 20 MOhm and 15% of input resistance,\n# bias current within 0 +/- 100 pA, and RMS noise below 0.07 mV (1.5 ms window) and 0.5 mV\n# (500 ms window) (Methods, Patch-clamp recording). Each neuron was filled with biocytin and its\n# nucleus extracted for RNA-seq. Measured variables per cell are the voltage responses, from\n# which 18 features are computed with IPFX (Methods, Electrophysiology feature analysis); soma\n# depth from pia and normalized L2/3 depth (0 at the L1/L2 border, 1 at the L3/L4 border); the\n# transcriptome, from which each cell gets one of five t-types (LTK, GLP2R, FREM3, CARM1P1,\n# COL22A1) by Seurat mapping; and for 109 cells a dendritic reconstruction. Cell counts are 385\n# cells mapped to the five t-types, 283 with electrophysiological features, 109 reconstructed\n# (Results, Patch-seq pipeline). The mouse comparison uses 120 VISp L2/3 neurons from the same\n# platform (ref. 32), not in this dandiset. Histology (NeuN, Nissl, GFAP, IBA1, SMI-32, Ki-67)\n# and mFISH are on other tissue.\n#\n# The 18 features, as named in the code (data/ephys_feature_names.csv), are adapt_mean\n# (adaptation), avg_rate_hero (mean firing rate), downstroke_long_square (AP downstroke rate),\n# fast_trough_v_long_square_rel (AP fast AHP), fi_fit_slope (f-I slope), first_isi_hero_inv\n# (initial firing rate), input_resistance, latency_rheo (latency at rheobase),\n# peak_v_long_square_rel (AP height), rheobase_i, sag, tau, threshold_v_long_square,\n# trough_v_long_square_rel, upstroke_downstroke_ratio_long_square, upstroke_long_square,\n# v_baseline (resting membrane potential, RMP) and width_long_square. The Methods define them\n# (AP features from long steps, f-I slope and latency and initial rate at rheobase, mean rate\n# and adaptation at about 50 pA above rheobase, sag at about -100 pA, tau from short pulses,\n# input resistance from hyperpolarizing long steps). The code sets input resistance, f-I slope\n# and sag to missing where they are not positive (hivscc_data.load_data). The IPFX version is\n# not given; a current release is the standard choice, and the code's feature table is the\n# check (link claim features-and-labels-link).\n#\n# What is where. The dandiset is described as Patch-seq recordings from human cortex (June\n# 2020) and names this preprint; it is meant to hold the electrophysiology. The t-type and depth\n# of each cell are part of the paper's record of the cell; whether the files carry them or they\n# must come from the code's cell table by specimen ID is for the author to find, through the\n# link claim, so the claims that need them are marked `with_labels`. Claims that also need the\n# donor pathology scores or the mouse recordings are `with_inputs`. Transcriptomes,\n# morphologies, histology and mFISH are not in the dandiset: the Methods name the Allen Brain Map\n# RNA-seq portal for the reference data and the code's README names the Human Patch-seq L2/3\n# project at the Allen Brain Map; those claims are `elsewhere`.\n#\n# Common method, used by several criteria. \"The analysis cells\" are the cells of the code's\n# 385-cell table with the feature needed (a statsmodels formula drops missing values per\n# feature, as the code does). \"Deep FREM3\" is FREM3 with normalized L2/3 depth above 0.575, the\n# density minimum (Results, Deep L3 human glutamatergic t-types, paragraph 2; Methods,\n# Quantification of soma size, which prints the boundary as -0.575 in its sign convention; the\n# code uses depth > 0.575). \"The t-type ANOVA\" is, per feature, an ordinary least squares fit\n# of the feature on t-type (statsmodels), with R2 its explained variance and p the\n# heteroscedasticity-robust (HC3) F test, Benjamini-Hochberg corrected across the features of\n# one modality (Methods, Analysis of features by t-type and species; code\n# hivscc_analysis.run_cluster_anova). \"The depth regression\" is the same with normalized L2/3\n# depth as the regressor (Methods, Analysis of features by depth for FREM3 t-type). \"The\n# pairwise test\" is a two-sided Mann-Whitney test between pairs of t-types, Benjamini-Hochberg\n# corrected across the pairs of one feature (figure legends; code hivscc_analysis.pairwise_mw\n# and plot_mw_bars).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000023\"\npaper: doi:10.1101/2020.03.31.018820\nclaims:\n# --- Link and cohort -------------------------------------------------------------------------\n- id: features-and-labels-link\n  kind: link\n  statement: The dandiset's recordings can be matched to the paper's per-cell table (t-type and\n    depth) by specimen ID, and the 18 features computed from them agree with the paper's feature\n    table.\n  source: Methods, Electrophysiology feature analysis; code data/human_IVSCC_excitatory_L23_consolidated_0131.csv\n    and data/human_mouse_ephys_all_0127.csv at commit 3daf9f0\n  data: with_labels\n  criterion: Cells are matched by the specimen ID (SpecimenID in the code's cell table). The 18\n    features are computed from each matched recording with IPFX, after the sweep QC of the\n    Methods. For each feature, the median over matched cells of the absolute difference from the\n    code's table relative to the table's absolute value is taken (10%, the protocol's default\n    tolerance, as the bound). Reproduced when at least 283 of the 385 cells match and all 18\n    features are within 10%; partially reproduced when cells match and 9 to 17 features are\n    within 10%; not reproduced otherwise. The number of matched cells, and how many of them\n    carry a t-type or depth in the files themselves, is reported. The code's table is from the\n    revision (316 human cells), so cells beyond the preprint's 283 are expected.\n- id: cohort-cells\n  statement: 385 Patch-seq neurons passing transcriptomic QC mapped to the five supragranular\n    glutamatergic t-types, and 283 of them had recordings complete enough to compute\n    electrophysiological features.\n  source: Results, Patch-seq pipeline for human neurosurgical tissue analysis, paragraph 2\n  quote: A total of 385 neurons that passed transcriptomic data QC mapped with higher confidence to\n    the five supragranular human glutamatergic t-types than to any other neuron type. ... Most\n    neurons (283) also had sufficiently complete recordings to calculate electrophysiological\n    features.\n  data: with_labels\n  depends_on:\n  - features-and-labels-link\n  expected:\n  - quantity: neurons mapped to the five t-types\n    value: 385\n    tolerance: 0\n  - quantity: neurons with electrophysiological features\n    value: 283\n    tolerance: 0\n  criterion: Counts are records, so the tolerance is zero. The 385 is counted as the cells of\n    the code's table that have a recording in the dandiset; the 283 as those whose recordings\n    give the 18 features with IPFX (the paper does not say how many features may be missing;\n    readings are (a) at least one feature, (b) all 18, (c) no more than 3 of 18 missing, the\n    rule the Methods give for the projections). Reproduced when both counts match under one\n    reading; partially reproduced when one does. The dandiset may hold other cells; they are\n    counted and reported apart.\n- id: cohort-donors\n  statement: The neurons came from neurosurgical specimens of 90 tissue donors.\n  source: Discussion, paragraph 2\n  quote: across human neurosurgical specimens from 90 different tissue donors\n  data: with_labels\n  depends_on:\n  - features-and-labels-link\n  expected:\n    quantity: donors\n    value: 90\n    tolerance: 0\n  criterion: Donors are counted as distinct subjects. The paper allows two readings, (a) all\n    subjects in the dandiset, or (b) the donors of the 385 cells of the code's table that are in\n    the dandiset. Reproduced when either gives 90. The code's pathology table also lists 90\n    donors, which is reported.\n- id: cohort-type-counts\n  statement: The electrophysiology figures show 66 LTK, 25 GLP2R and 136 FREM3 neurons, and 21\n    deep FREM3, 17 CARM1P1 and 37 COL22A1 neurons.\n  source: Figure 4a legend; Figure 6b legend\n  quote: Bottom panels compare the intrinsic electrophysiological responses for 66 LTK, 25 GLP2R\n    and 136 FREM3 neurons. ... Electrophysiological description of the intrinsic electrophysiology\n    responses of 21 deep FREM3, 17 CARM1P1 and 37 COL22A1 neurons.\n  data: with_labels\n  depends_on:\n  - features-and-labels-link\n  expected:\n  - quantity: LTK neurons with electrophysiology\n    value: 66\n    tolerance: 0\n  - quantity: GLP2R neurons with electrophysiology\n    value: 25\n    tolerance: 0\n  - quantity: FREM3 neurons with electrophysiology\n    value: 136\n    tolerance: 0\n  - quantity: deep FREM3 neurons with electrophysiology\n    value: 21\n    tolerance: 0\n  - quantity: CARM1P1 neurons with electrophysiology\n    value: 17\n    tolerance: 0\n  - quantity: COL22A1 neurons with electrophysiology\n    value: 37\n    tolerance: 0\n  criterion: Counts per t-type of the cells with features, under the readings of cohort-cells\n    for which cells have features; deep FREM3 also needs a normalized depth above 0.575.\n    Reproduced when all six match under one reading; partially reproduced when at least three\n    do.\n# --- Histology and transcriptomics (not in the dandiset) ----------------------------------\n- id: fig1a-thickness\n  statement: Human L2 and L3 together (1.23 +/- 0.15 mm) are on average 1.16 times thicker than\n    the whole mouse cortex (1.06 +/- 0.01 mm).\n  source: Results, Human supragranular cortex is more diverse than in mouse, paragraph 1; Figure 1a\n  quote: The combined thickness of the relatively thin L2 and very thick L3 in human cortex (1.23 ±\n    0.15 mm) is on average 1.16 times greater than the thickness of the entire mouse cortex (1.06 ±\n    0.01 mm; Fig. 1a ).\n  data: elsewhere\n  where: NeuN section measurements in GitHub AllenInstitute/patchseq_human_L23 data/cell_sizes at\n    commit 3daf9f0803ea0c220a040ea523f23af5f93c56ac (Code6 and Code7)\n  expected:\n  - quantity: human L2 plus L3 thickness\n    value: 1.23\n    tolerance: 0.15\n    unit: mm\n  - quantity: mouse cortical thickness\n    value: 1.06\n    tolerance: 0.01\n    unit: mm\n  criterion: Tolerances are the reported spreads (SD across donors). Not tested on the dandiset.\n- id: fig1b-density\n  statement: Human supragranular neuron density is 27.7 +/- 4.5 thousand cells/mm3, highest in L2\n    and halving to a minimum in mid L3, while mouse VISp L2/3 has about 6 times that density\n    (165 +/- 24.9 thousand cells/mm3), uniform with depth.\n  source: Results, Human supragranular cortex is more diverse than in mouse, paragraph 1; Figure 1b\n  quote: the average density of human neurons was 27.7 ± 4.5 thousand cells/mm 3 ( Fig. 1b ; left).\n    This distribution is not homogeneous, with higher density in L2 that decreases by half to reach a\n    low point in mid L3 ( Fig. 1b ; right). In contrast, supragranular layers of mouse VISp show 6\n    times the neuronal density of human (165 ± 24.9 thousand cells/mm 3 ) with a homogeneous\n    distribution across cortical depth.\n  data: elsewhere\n  where: NeuN section measurements in GitHub AllenInstitute/patchseq_human_L23 data/cell_sizes at\n    commit 3daf9f0803ea0c220a040ea523f23af5f93c56ac (Code6 and Code7)\n  expected:\n  - quantity: human neuron density\n    value: 27.7\n    tolerance: 4.5\n    unit: thousand cells/mm3\n  - quantity: mouse neuron density\n    value: 165\n    tolerance: 24.9\n    unit: thousand cells/mm3\n  criterion: Tolerances are the reported spreads. Method per the Methods (20 bins over L2/3,\n    first and last dropped, one section per donor). Not tested on the dandiset.\n- id: fig1c-soma-area\n  statement: Mean soma area doubles from L2 to deep L3 in human but is uniform across mouse L2/3;\n    the interquartile ranges are 44 to 96 um2 in mouse and 107 to 253 um2 in human, and the\n    largest human somata exceed 850 um2.\n  source: Results, Human supragranular cortex is more diverse than in mouse, paragraph 1; Figure 1c\n  quote: the average cross-sectional area of neuron somata doubles from L2 to deep L3 in human\n    supragranular cortex in a graded fashion but in mouse is remarkably uniform across the depth of\n    supraganular cortex ( Fig. 1c , left). The interquartile range of mouse and human somata were 44\n    - 96μm 2 and 107 - 253μm 2 , respectively, with the largest human somata exceeding 850μm 2 .\n  data: elsewhere\n  where: NeuN ROI measurements in GitHub AllenInstitute/patchseq_human_L23 data/cell_sizes at\n    commit 3daf9f0803ea0c220a040ea523f23af5f93c56ac (Code6 and Code7)\n  expected:\n  - quantity: mouse soma area, first quartile\n    value: 44\n    tolerance: 4.4\n    unit: um2\n  - quantity: mouse soma area, third quartile\n    value: 96\n    tolerance: 9.6\n    unit: um2\n  - quantity: human soma area, first quartile\n    value: 107\n    tolerance: 10.7\n    unit: um2\n  - quantity: human soma area, third quartile\n    value: 253\n    tolerance: 25.3\n    unit: um2\n  criterion: Not tested on the dandiset.\n- id: fig1c-soma-variation\n  statement: The variation of soma size in deep L3 is four times higher in human than in mouse.\n  source: Results, Human supragranular cortex is more diverse than in mouse, paragraph 1; Figure 1c\n    right\n  quote: variation in deep L3 neuron soma size is four-fold higher in human compared to mouse ( Fig.\n    1c , right)\n  data: elsewhere\n  where: NeuN ROI measurements in GitHub AllenInstitute/patchseq_human_L23 data/cell_sizes at\n    commit 3daf9f0803ea0c220a040ea523f23af5f93c56ac (Code6 and Code7)\n  expected:\n    quantity: ratio of human to mouse SD of soma area in deep L3\n    value: 4\n    tolerance: 0.4\n  criterion: Not tested on the dandiset. The bins that make up deep L3 are not stated.\n- id: fig1f-frem3-heterogeneity\n  statement: The human FREM3 t-type has more within-type transcriptomic heterogeneity (variance\n    explained by PC1 above permuted data) than any other human or mouse supragranular t-type,\n    which are similar to one another.\n  source: Results, Human supragranular cortex is more diverse than in mouse, paragraph 3; Figure 1f\n  quote: This analysis confirms high heterogeneity in FREM3 , with lower, generally similar, values\n    for all other human and mouse t-types ( Fig. 1f ).\n  data: elsewhere\n  where: Allen Brain Map RNA-seq data (https://portal.brain-map.org/atlases-and-data/rnaseq), human\n    MTG nuclei and mouse VISp cells, as the Methods name them; not pinned\n  criterion: Method per the Methods (80 cells per type, 80 most variable genes, 100 repeats\n    against gene-shuffled data). Not tested on the dandiset.\n- id: fig1g-deep-types-de-genes\n  statement: CARM1P1 and COL22A1 have many more differentially expressed genes against the\n    homologous types than the homologous types have against one another, in either species.\n  source: Results, Human supragranular cortex is more diverse than in mouse, paragraph 3; Figure 1g\n  quote: Homologous types are similarly discrete from one another in both mouse in human, whereas\n    the deep L3 CARM1P1 and COL22A1 t-types had many more DE genes when compared to the homologous\n    t-types ( Fig. 1g ).\n  data: elsewhere\n  where: Allen Brain Map RNA-seq data (https://portal.brain-map.org/atlases-and-data/rnaseq), as the\n    Methods name them; not pinned\n  criterion: Not tested on the dandiset.\n- id: fig3a-platform-correlation\n  statement: Human Patch-seq cells and dissociated nuclei of matched t-types are highly correlated\n    in gene expression (R = 0.85), more than mouse cells and human nuclei (R = 0.57); 177 genes are\n    enriched in nuclei and 2,670 at least four-fold in Patch-seq.\n  source: Results, High-confidence Patch-seq neuron t-type mapping, paragraph 2; Figure 3a\n  quote: Expression data from dissociated mouse whole cells and human nuclei were moderately\n    correlated (R=0.57, p~0, Fig. 3a , left), ... dissociated nuclei and Patch-seq cells from matched\n    human t-types were highly correlated (R=0.85, p~0, Fig. 3a , right). Relatively few genes (177\n    genome-wide) showed enriched expression in dissociated nuclei relative to Patch-seq cells ... we\n    identified 2,670 genes with at least four-fold enrichment in Patch-seq\n  statistics:\n  - about: mouse cells against human nuclei, printed p~0\n    statistic: R = 0.57\n    p: 0\n  - about: human nuclei against human Patch-seq cells, printed p~0\n    statistic: R = 0.85\n    p: 0\n  data: elsewhere\n  where: Allen Brain Map RNA-seq data and the Human Patch-seq L2/3 project at the Allen Brain Map\n    (https://knowledge.brain-map.org/data/0R94W5U07IHCMVJ4TVK/summary), as the code's README\n    names them; not pinned\n  expected:\n  - quantity: correlation, nuclei against Patch-seq\n    value: 0.85\n    tolerance: 0.085\n  - quantity: correlation, mouse cells against human nuclei\n    value: 0.57\n    tolerance: 0.057\n  criterion: Not tested on the dandiset.\n# --- Pathology ------------------------------------------------------------------------------\n- id: fig2d-pathology-scores\n  statement: Average pathology scores over six markers ranged from 0.06 to 1.83 across donors, and\n    most cases had averages below 1.0, a range not considered overtly pathological.\n  source: Results, Detailed histological assessment of human surgical tissue, paragraph 2; Figure\n    2c and 2d\n  quote: images from the case with the lowest average score (mean of 6 marker scores = 0.06) are\n    contrasted with images from the case with the highest average score (mean of 6 marker scores =\n    1.83) ( Fig. 2c ). ... However, this was rare, and most cases had average scores <1.0 ( Fig. 2d )\n  data: elsewhere\n  where: GitHub AllenInstitute/patchseq_human_L23 data/pathology_scoring.csv at commit\n    3daf9f0803ea0c220a040ea523f23af5f93c56ac\n  expected:\n  - quantity: lowest donor average score\n    value: 0.06\n    tolerance: 0.006\n  - quantity: highest donor average score\n    value: 1.83\n    tolerance: 0.183\n  criterion: The average is of GFAP, IBA1, Ki-67, SMI-32, NeuN and Nissl (cellularity) scores, as\n    the code's pathology_analysis.ipynb sums them. \"Most\" is read as more than half of the donors\n    with all six scores. Not tested on the dandiset.\n- id: edfig1-marker-correlation\n  statement: The six pathology markers are very weakly correlated with one another across donors,\n    with only Ki-67 and Nissl (cellularity) modestly correlated.\n  source: Results, Detailed histological assessment of human surgical tissue, paragraph 2; Extended\n    Data Figure 1\n  quote: we found very low correlation of the 6 cellular markers with each other, with only Ki-67\n    and Nissl (cellularity) being modestly correlated ( Extended Data Fig. 1 )\n  data: elsewhere\n  where: GitHub AllenInstitute/patchseq_human_L23 data/pathology_scoring.csv at commit\n    3daf9f0803ea0c220a040ea523f23af5f93c56ac\n  criterion: Pearson correlation across donors (Extended Data Fig. 1 legend). The paper gives no\n    threshold for \"modest\"; reproduced when the Ki-67 and Nissl pair has the largest absolute\n    correlation of the 15 pairs. Not tested on the dandiset.\n- id: fig2ef-pathology-ephys\n  statement: Of 18 electrophysiological features compared between neurons from donors with low\n    (0 to 1) and high (1 to 3) GFAP or IBA1 scores, only resting membrane potential under IBA1\n    differs, neurons from high-IBA1 donors being about 5 mV more hyperpolarized; the other 17 IBA1\n    and all 18 GFAP comparisons do not differ.\n  source: Results, Detailed histological assessment of human surgical tissue, paragraph 3; Figure 2e\n    and 2f\n  quote: Among the 18 electrophysiological features analyzed for GFAP and IBA1, only one feature\n    (resting membrane potential, RMP) related to IBA1 was significantly different between low versus\n    high groups. Neurons in the high IBA1 group were approximately 5 mV more hyperpolarized at rest\n    than neurons in the low IBA1 group ( Fig. 2f ). The remaining 17/18 features for IBA1 and all 18\n    features for GFAP were not statistically different between low and high groups\n  statistics:\n  - about: RMP, low against high IBA1\n    test: Mann-Whitney (named in the code; the paper does not name the test)\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: GFAP low 60 and high 125 neurons; IBA1 low 170 and high 15 neurons\n  data: with_inputs\n  depends_on:\n  - features-and-labels-link\n  expected:\n  - quantity: RMP difference, high minus low IBA1\n    value: -5\n    tolerance: 0.5\n    unit: mV\n  - quantity: GFAP low neurons\n    value: 60\n    tolerance: 0\n  - quantity: GFAP high neurons\n    value: 125\n    tolerance: 0\n  - quantity: IBA1 low neurons\n    value: 170\n    tolerance: 0\n  - quantity: IBA1 high neurons\n    value: 15\n    tolerance: 0\n  criterion: Partly a claim of absence, judged on the paper's test. Cells are the supragranular\n    glutamatergic neurons (the code's 385-cell table) with all 18 features defined (the code\n    drops cells with any missing feature). The paper's text says \"all supragranular glutamatergic\n    neurons\"; the original pathology notebook also keeps only temporal cortex cells of the\n    hIVSCC-MET project, from a table not in the repository. So the readings are (a) temporal\n    cells only (region temporal in the code's cell table), (b) all regions; the group counts\n    above say which the paper used. Each donor's GFAP and IBA1 scores are the columns GFAP Cortex\n    and Iba1 Cortex of the code's data/pathology_scoring.csv (the mean of three\n    neuropathologists), low being at most 1 and high above 1 (the code; the text gives 0-1 and\n    1-3). The test is the code's, scipy's Mann-Whitney U with its default of scipy 1.4 (the\n    pinned version), whose p is half the two-sided p, at the Bonferroni level 0.05/18 per marker\n    (Figure 2f legend and the code). Reproduced when, under one reading, RMP under IBA1 is the only\n    significant comparison of the 36, with the high group more hyperpolarized and the difference\n    of group medians or of group means (the paper does not say which; both are shown) within\n    tolerance; partially reproduced when the significance pattern holds but the size is outside\n    tolerance; not reproduced when any other comparison is significant or RMP under IBA1 is not.\n    The two-sided Mann-Whitney test is shown as a variant, as is the updated notebook's result.\n# --- Depth by t-type ------------------------------------------------------------------------\n- id: fig3d-depth-by-type\n  statement: LTK neurons lie mainly in L2 and at the L2/L3 border, GLP2R mainly in upper L3,\n    FREM3 span L2 and L3 and continue into L4, and CARM1P1 and COL22A1 lie almost entirely in deep\n    L3 and along the L3/L4 border.\n  source: Results, High-confidence Patch-seq neuron t-type mapping, paragraph 4; Figure 3d\n  quote: Human LTK neurons were found primarily in L2 and in the border region of L2 and L3. GLP2R\n    neurons were found primarily in upper L3, with some neurons found in L2. FREM3 neurons spanned L2\n    and L3, continuing into L4, consistent with their heterogeneous gene expression profile. CARM1P1\n    and COL22A1 were found almost entirely in deep L3 and along the L3/L4 border.\n  data: with_labels\n  depends_on:\n  - features-and-labels-link\n  criterion: Normalized L2/3 depth per cell (0 at the L1/L2 border, 1 at the L3/L4 border; Figure\n    3d legend and Figure 1 legend). The L2/L3 border is not recorded per cell, so L2 is judged\n    by order. Deep L3 is depth above 0.575 (the paper's density minimum) and L4 depth above 1.\n    Reproduced when all of these hold; the median depth of LTK is below that of GLP2R; the GLP2R\n    median is below 0.575; FREM3 includes cells shallower than the LTK median and cells deeper\n    than 1; and, for CARM1P1 and COL22A1 each, \"almost entirely\" holds. The paper gives no number\n    for \"almost entirely\"; the readings are (a) at least 90% and (b) at least 80% of cells deeper\n    than 0.575. Partially reproduced when the order of medians holds but not the rest. All cells\n    of the code's table with a depth are used, whether or not they have features.\n# --- Homologous types ----------------------------------------------------------------------\n- id: fig4e-human-ephys-anova\n  statement: Among the three human homologous t-types (LTK, GLP2R, FREM3), 3 of 18\n    electrophysiological features explain more than 10% of variance by t-type (input resistance,\n    f-I slope and rheobase), at FDR below 1e-5, with a maximum R2 of 0.16.\n  source: Results, Increased morpho-electric specialization in human L2-3 t-types, paragraph 5;\n    Figure 4e\n  quote: For electrophysiological features ( Fig. 4e ), 3/18 showed differences between t-types that\n    explained >10% of feature variance ( R 2 >0.1) for both human and mouse (FDR<0.05 for mouse\n    features, <10 −5 for human). ... while the human types showed distinct firing properties (f-I\n    slope and rheobase) in addition to input resistance, with a maximum R 2 =0.16.\n  statistics:\n  - test: one-way ANOVA, heteroscedasticity-robust (HC3) F test\n    p: 0.00001\n    p_relation: \"<\"\n    corrected: FDR (Benjamini-Hochberg)\n    n: 66 LTK, 25 GLP2R and 136 FREM3 neurons\n  data: with_labels\n  depends_on:\n  - features-and-labels-link\n  expected:\n  - quantity: maximum R2 over the 18 features\n    value: 0.16\n    tolerance: 0.016\n  - quantity: features with R2 above 0.1\n    value: 3\n    tolerance: 0\n  criterion: The t-type ANOVA on LTK, GLP2R and all FREM3 cells (the preprint's Methods say the\n    three homologous t-types; the code's revision uses superficial FREM3 only, depth below\n    0.575, shown as a variant). Reproduced when exactly the three features named have R2 above\n    0.1, each at FDR below 1e-5, and the maximum R2 is within tolerance; partially reproduced\n    when at least two of the three named features have R2 above 0.1 at FDR below 0.05.\n- id: fig4e-mouse-ephys-anova\n  statement: Among the three mouse L2/3 t-types, 3 of 18 electrophysiological features explain\n    more than 10% of variance (input resistance, AP width and AP downstroke rate), at FDR below\n    0.05, with a maximum R2 of 0.12, below the human maximum.\n  source: Results, Increased morpho-electric specialization in human L2-3 t-types, paragraph 5;\n    Figure 4e\n  quote: However, the mouse types were distinct in input resistance and two related AP shape\n    features (width and downstroke) with a maximum R 2 =0.12\n  statistics:\n  - test: one-way ANOVA, heteroscedasticity-robust (HC3) F test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR (Benjamini-Hochberg)\n    n: 9 Adamts2, 43 Rrad and 55 Agmat neurons (Figure 4b legend); 120 mouse neurons in the text\n  data: with_inputs\n  depends_on:\n  - fig4e-human-ephys-anova\n  expected:\n  - quantity: maximum R2 over the 18 features, mouse\n    value: 0.12\n    tolerance: 0.012\n  - quantity: features with R2 above 0.1, mouse\n    value: 3\n    tolerance: 0\n  criterion: The t-type ANOVA on the mouse Adamts2, Rrad and Agmat cells. The mouse recordings are\n    not in this dandiset and the paper does not say where they are (ref. 32 is the mouse\n    Patch-seq study); the code's feature and cell tables hold their features and t-types.\n    Reproduced when exactly the three features named have R2 above 0.1 at FDR below 0.05, the\n    maximum R2 is within tolerance and is below the human maximum of fig4e-human-ephys-anova;\n    partially reproduced when two of the three hold.\n- id: fig4f-morph-anova\n  statement: 16 of 60 morphological features have R2 above 0.15 between the human homologous\n    t-types (FDR below 1e-3), against 12 of 60 for mouse (10 of them at FDR below 0.05).\n  source: Results, Increased morpho-electric specialization in human L2-3 t-types, paragraph 5;\n    Figure 4f\n  quote: For morphological features ( Fig. 4f ), 16/60 features had R 2 >0.15 between the human\n    t-types (FDR<10 −3 ), compared to 12/60 for the mouse t-types (with 10/12 significant at FDR<0.05).\n  statistics:\n  - about: human features with R2 above 0.15\n    test: one-way ANOVA, heteroscedasticity-robust (HC3) F test\n    p: 0.001\n    p_relation: \"<\"\n    corrected: FDR (Benjamini-Hochberg)\n  data: elsewhere\n  where: Reconstructions at the Allen Brain Map Human Patch-seq L2/3 project; morphological features\n    in GitHub AllenInstitute/patchseq_human_L23 data/All_L23_Lockdown_all_raw_features.csv and\n    data/All_Mouse_Cells_Lockdown_All_raw_features.csv at commit 3daf9f0803ea0c220a040ea523f23af5f93c56ac\n  expected:\n  - quantity: human morphological features with R2 above 0.15\n    value: 16\n    tolerance: 1.6\n  - quantity: mouse morphological features with R2 above 0.15\n    value: 12\n    tolerance: 1.2\n  criterion: The t-type ANOVA on morphological features. Not tested on the dandiset.\n- id: fig4-glp2r-sag\n  statement: GLP2R neurons, like LTK neurons, lack firing rate adaptation, but unlike LTK neurons\n    (which have no sag) they have pronounced sag.\n  source: Results, Increased morpho-electric specialization in human L2-3 t-types, paragraphs 1 and\n    2; Figure 4a\n  quote: Electrophysiologically, GLP2R neurons exhibited LTK -like electrophysiology, lacking\n    adaptation and higher input resistance, but differed from LTK neurons in that they had\n    pronounced sag.\n  data: with_labels\n  depends_on:\n  - features-and-labels-link\n  criterion: Sag (sag ratio at about -100 pA) and adaptation (adapt_mean) compared between LTK and\n    GLP2R with the pairwise test over the three homologous types (the paper's post hoc test for\n    Figure 4e; the paper shows this finding only as traces). Reproduced when GLP2R sag is\n    significantly higher than LTK sag (FDR below 0.05) and adaptation does not differ between\n    them; partially reproduced when sag is higher but adaptation also differs.\n- id: edtable1-species-ephys\n  statement: Between human and mouse homologous t-types, 17 of 18 electrophysiological features\n    differ at FDR below 0.05.\n  source: Extended Data Table 1 legend\n  quote: For homologous t-types, results are shown for unpaired t-tests across species for each\n    feature: FDR-corrected p-values as well as Cohen’s d effect size (positive if human values are\n    larger). 17out of 18 features are significant at FDR<0.05.\n  statistics:\n  - test: unpaired t-test per feature\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n  data: with_inputs\n  depends_on:\n  - features-and-labels-link\n  expected:\n    quantity: features differing between species\n    value: 17\n    tolerance: 0\n  criterion: Human LTK, GLP2R and FREM3 cells against mouse Adamts2, Rrad and Agmat cells (mouse\n    features from the code's table), one test per feature, Benjamini-Hochberg over 18. The\n    legend does not say whether the t-test assumes equal variances; readings are (a) Student's\n    and (b) Welch's. Reproduced when either gives 17. The code's test (scipy's Mann-Whitney with\n    the scipy 1.4 default, on cells with all 18 features; AP width the one feature not\n    significant) is shown as a variant, as is Cohen's d per feature.\n- id: edfig6-classifier-human-ephys\n  statement: A random forest predicts the homologous human t-type from electrophysiological\n    features with 67% accuracy.\n  source: Results, Increased morpho-electric specialization in human L2-3 t-types, paragraph 6;\n    Extended Data Figure 6\n  quote: Homologous human t-types were predicted with 67% accuracy using electrophysiological\n    features, while mouse t-types were predicted with 54% accuracy.\n  data: with_labels\n  depends_on:\n  - features-and-labels-link\n  expected:\n    quantity: test accuracy, human homologous types\n    value: 0.67\n    tolerance: 0.067\n  criterion: As the Methods (Analysis of features by t-type and species, paragraph 3) and the code\n    (classifier_and_species_analysis.ipynb). LTK, GLP2R and FREM3 cells with all 18 features (the\n    code drops any cell with a missing feature), features standardized over all cells, 1000\n    stratified random splits into 70% training and 30% test, a random forest of 600 trees\n    (sklearn, with the code's settings class_weight balanced, max_features sqrt, min_samples_leaf\n    2), accuracy on the test set averaged over the splits. Reproduced when the mean accuracy is\n    within tolerance. Accuracy with shuffled t-type labels (Methods) is reported for comparison.\n- id: edfig6-classifier-mouse-ephys\n  statement: The same classifier predicts mouse L2/3 t-types from electrophysiological features\n    with 54% accuracy, lower than for human.\n  source: Results, Increased morpho-electric specialization in human L2-3 t-types, paragraph 6;\n    Extended Data Figure 6\n  quote: Homologous human t-types were predicted with 67% accuracy using electrophysiological\n    features, while mouse t-types were predicted with 54% accuracy.\n  data: with_inputs\n  depends_on:\n  - edfig6-classifier-human-ephys\n  expected:\n    quantity: test accuracy, mouse types\n    value: 0.54\n    tolerance: 0.054\n  criterion: As edfig6-classifier-human-ephys, on mouse Adamts2, Rrad and Agmat cells (features\n    from the code's table). Reproduced when the mean accuracy is within tolerance and below the\n    human accuracy.\n- id: edfig6-classifier-morphoelectric\n  statement: Combining morphological and electrophysiological features raises accuracy slightly,\n    to 69% for human and 60% for mouse neurons.\n  source: Results, Increased morpho-electric specialization in human L2-3 t-types, paragraph 6;\n    Extended Data Figure 6\n  quote: Classifying based on morphological and electrophysiological features combined resulted in\n    slightly improved performance of 69% for human neurons and 60% for mouse neurons\n  data: elsewhere\n  where: Morphological features in GitHub AllenInstitute/patchseq_human_L23\n    data/All_L23_Lockdown_all_raw_features.csv and data/All_Mouse_Cells_Lockdown_All_raw_features.csv\n    at commit 3daf9f0803ea0c220a040ea523f23af5f93c56ac\n  expected:\n  - quantity: test accuracy, human, combined features\n    value: 0.69\n    tolerance: 0.069\n  - quantity: test accuracy, mouse, combined features\n    value: 0.60\n    tolerance: 0.06\n  criterion: Not tested on the dandiset alone; it needs the morphological features.\n# --- FREM3 depth ------------------------------------------------------------------------------\n- id: fig5c-frem3-ephys-depth\n  statement: In FREM3 neurons, 9 of 18 electrophysiological features correlate with normalized\n    depth at FDR below 0.05 (7 at FDR below 0.01); the strongest are increasing sag, increasing AP\n    upstroke/downstroke ratio and decreasing latency at rheobase.\n  source: Results, Human FREM3 t-type exhibits depth-dependent morpho-electro-transcriptomic\n    variation, paragraph 2; Figure 5c\n  quote: Nine out of 18 physiological features were significantly correlated with depth (FDR<0.05,\n    7/18 FDR<0.01; Supplementary Data 1). The three strongest electrophysiology correlations with\n    depth were the increase in sag and AP (Action Potential) upstroke / downstroke ratio and the\n    decrease in AP latency at rheobase ( Fig. 5c ).\n  statistics:\n  - about: features correlated with depth\n    test: linear regression on normalized L2/3 depth, heteroscedasticity-robust (HC3) F test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR (Benjamini-Hochberg)\n  - about: the three regressions shown in Figure 5c\n    test: linear regression, HC3 F test\n    p: 0.0000001\n    p_relation: \"<\"\n    corrected: FDR\n    n: 124 FREM3 neurons for sag; 141 for rheobase traces\n  data: with_labels\n  depends_on:\n  - features-and-labels-link\n  expected:\n  - quantity: features correlated with depth at FDR below 0.05\n    value: 9\n    tolerance: 0.9\n  - quantity: features correlated with depth at FDR below 0.01\n    value: 7\n    tolerance: 0.7\n  criterion: The depth regression on all FREM3 cells with a normalized depth, per feature, BH over\n    the 18. \"Strongest\" is read as the largest R2, the measure the Methods report. Reproduced when\n    both counts are within tolerance and the three features with the largest R2 are sag and\n    upstroke/downstroke ratio (positive slope) and latency (negative slope), each at FDR below\n    1e-7; partially reproduced when those three are significant at FDR below 0.05 with those signs\n    but the counts or the ranking differ.\n- id: fig5b-frem3-morph-depth\n  statement: In FREM3 neurons, 37 of 58 morphological features correlate with depth at FDR below\n    0.05 (28 at FDR below 0.01), including apical height, maximum basal dendrite length and soma\n    radius.\n  source: Results, Human FREM3 t-type exhibits depth-dependent morpho-electro-transcriptomic\n    variation, paragraph 2; Figure 5b\n  quote: 37 out of 58 morphological features were correlated with depth (FDR<0.05, 28/58 FDR<0.01).\n  statistics:\n  - test: linear regression on normalized L2/3 depth, HC3 F test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR (Benjamini-Hochberg)\n  data: elsewhere\n  where: Morphological features in GitHub AllenInstitute/patchseq_human_L23\n    data/All_L23_Lockdown_all_raw_features.csv at commit 3daf9f0803ea0c220a040ea523f23af5f93c56ac\n  expected:\n  - quantity: morphological features correlated with depth at FDR below 0.05\n    value: 37\n    tolerance: 3.7\n  - quantity: morphological features correlated with depth at FDR below 0.01\n    value: 28\n    tolerance: 2.8\n  criterion: Not tested on the dandiset.\n- id: fig5d-frem3-gene-depth\n  statement: FREM3 gene expression varies with soma depth; 790 genes correlate with depth at FDR\n    below 0.05, enriched for synaptic transmission, cell migration and neuron projection\n    morphogenesis.\n  source: Results, Human FREM3 t-type exhibits depth-dependent morpho-electro-transcriptomic\n    variation, paragraphs 1 and 2; Figure 5a and 5d\n  quote: 790 genes were correlated with depth (FDR<0.05) and GO (gene ontology) enrichment analysis\n    on this gene set revealed a variety of significantly enriched functional categories ( Fig. 5d ,\n    Supplementary Data 1)\n  statistics:\n  - test: linear regression on normalized L2/3 depth, HC3 F test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR (Benjamini-Hochberg)\n  data: elsewhere\n  where: Patch-seq transcriptomes at the Allen Brain Map Human Patch-seq L2/3 project; per-gene\n    results in GitHub AllenInstitute/patchseq_human_L23 data/frem_genes_depth.csv at commit\n    3daf9f0803ea0c220a040ea523f23af5f93c56ac\n  expected:\n    quantity: genes correlated with depth\n    value: 790\n    tolerance: 79\n  criterion: Not tested on the dandiset. The code's gene_depth_analysis.ipynb counts 1917 genes at\n    FDR below 0.01 from its revision's results, so its table is not the preprint's.\n# --- Deep L3 types ----------------------------------------------------------------------------\n- id: fig6-deep-ephys-anova\n  statement: The three deep L3 types (deep FREM3, CARM1P1, COL22A1) differ in 15 of 18\n    electrophysiological features (FDR below 0.05), with R2 above 0.4 for 4 of them, while no\n    feature reaches R2 0.4 among the three homologous types.\n  source: Results, Deep L3 human glutamatergic t-types are morpho-electrically distinct, paragraph 4\n  quote: ANOVA differences were seen in 15 out of 18 electrophysiological features and 24 out of 60\n    morphological features (FDR<0.05) (Supplementary Data 1). Many of these features showed very\n    large effect sizes, with the variance explained by type surpassing 40% ( R 2 >0.4) for 4\n    electrophysiological and 20 morphological features, while no features met this threshold for the\n    three homologous types (maximum R 2 =0.26).\n  statistics:\n  - test: one-way ANOVA, heteroscedasticity-robust (HC3) F test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR (Benjamini-Hochberg)\n    n: 21 deep FREM3, 17 CARM1P1 and 37 COL22A1 neurons (Figure 6b legend)\n  data: with_labels\n  depends_on:\n  - features-and-labels-link\n  - fig4e-human-ephys-anova\n  expected:\n  - quantity: electrophysiological features differing among deep types\n    value: 15\n    tolerance: 1.5\n  - quantity: electrophysiological features with R2 above 0.4\n    value: 4\n    tolerance: 0.4\n  criterion: The t-type ANOVA on deep FREM3, CARM1P1 and COL22A1 cells. Reproduced when both counts\n    are within tolerance and no electrophysiological feature has R2 above 0.4 in\n    fig4e-human-ephys-anova; partially reproduced when one count is within tolerance. The\n    maximum R2 of 0.26 for the homologous types is not tested, as the text does not say which\n    modality gives it and the electrophysiological maximum is 0.16.\n- id: fig6-deep-morph-anova\n  statement: The deep L3 types differ in 24 of 60 morphological features (FDR below 0.05), with R2\n    above 0.4 for 20 of them.\n  source: Results, Deep L3 human glutamatergic t-types are morpho-electrically distinct, paragraph\n    4; Figure 6d\n  quote: ANOVA differences were seen in 15 out of 18 electrophysiological features and 24 out of 60\n    morphological features (FDR<0.05)\n  data: elsewhere\n  where: Morphological features in GitHub AllenInstitute/patchseq_human_L23\n    data/All_L23_Lockdown_all_raw_features.csv at commit 3daf9f0803ea0c220a040ea523f23af5f93c56ac\n  expected:\n  - quantity: morphological features differing among deep types\n    value: 24\n    tolerance: 2.4\n  - quantity: morphological features with R2 above 0.4\n    value: 20\n    tolerance: 2\n  criterion: Not tested on the dandiset.\n- id: fig6c-carm1p1-upstroke-rin\n  statement: CARM1P1 neurons have a faster AP upstroke than deep FREM3 and COL22A1 neurons, and a\n    higher input resistance than deep FREM3 neurons.\n  source: Results, Deep L3 human glutamatergic t-types are morpho-electrically distinct, paragraph\n    2; Figure 6c\n  quote: Electrophysiologically, CARM1P1 neurons exhibited a faster action potential upstroke than\n    the other deep types ( Fig. 6c ). This extensive dendritic branching did not predict a lower\n    input resistance, which was higher than deep FREM3 neurons ( Fig. 6c ).\n  statistics:\n  - test: Mann-Whitney, pairwise\n    p: 0.05\n    p_relation: \"<\"\n    corrected: FDR\n  data: with_labels\n  depends_on:\n  - features-and-labels-link\n  criterion: The pairwise test over the three deep types (Figure 6c legend; BH over the three pairs\n    of a feature, as the code's plot_mw_bars). \"Faster upstroke\" is read as (a) the AP upstroke\n    rate (upstroke_long_square) or (b) the upstroke/downstroke ratio, the feature the code plots\n    for the deep types; both are run. Reproduced when, under one reading, CARM1P1 is significantly\n    higher than both deep FREM3 and COL22A1, and CARM1P1 input resistance is significantly higher\n    than deep FREM3; partially reproduced when one of the two parts holds.\n- id: fig6c-col22a1-rin-fi-sag\n  statement: COL22A1 neurons have very high input resistance and a steeper f-I gain than the other\n    deep L3 types, and less sag than CARM1P1 neurons.\n  source: Results, Deep L3 human glutamatergic t-types are morpho-electrically distinct, paragraph\n    3; Figure 6b and 6c\n  quote: COL22A1 neurons exhibited very high input resistance ( Fig. 6c ) and thus were the most\n    responsive to current injection, displaying a steeper firing frequency to current input gain\n    relative to the other deep L3 t-types. Interestingly, COL22A1 neurons showed a smaller amount of\n    sag than CARM1P1 neurons ( Fig. 6b )\n  data: with_labels\n  depends_on:\n  - features-and-labels-link\n  criterion: The pairwise test over the three deep types, for input resistance, f-I slope and sag.\n    The sag finding is shown in the paper only as traces (Figure 6b); the Figure 6c test is used\n    for it too. Reproduced when COL22A1 input resistance and f-I slope are each significantly\n    higher than both deep FREM3 and CARM1P1, and COL22A1 sag is significantly lower than CARM1P1\n    sag; partially reproduced when at least two of the three features hold.\n- id: fig6a-deep-dendrites\n  statement: CARM1P1 neurons have the largest total dendritic length of the L2 and L3 t-types, with\n    extensive proximal oblique and basal branching, while COL22A1 neurons have very sparse\n    branching.\n  source: Results, Deep L3 human glutamatergic t-types are morpho-electrically distinct, paragraphs\n    2 and 3; Figure 6a\n  quote: CARM1P1 neurons had the largest total dendritic length of all the L2 and L3 t-types,\n    despite having a shorter apical dendrite length on average. ... COL22A1 had very sparse dendritic\n    branching ( Fig. 6a ).\n  data: elsewhere\n  where: Morphological features in GitHub AllenInstitute/patchseq_human_L23\n    data/All_L23_Lockdown_all_raw_features.csv at commit 3daf9f0803ea0c220a040ea523f23af5f93c56ac\n  criterion: Not tested on the dandiset.\n- id: fig6e-deep-de-genes\n  statement: 219 marker genes distinguish deep FREM3, CARM1P1 and COL22A1, 77 of them also found in\n    Patch-seq cells, enriched for axon, synapse, calcium ion binding and extracellular matrix terms.\n  source: Results, Deep L3 human glutamatergic t-types are morpho-electrically distinct, paragraphs\n    5 and 6; Figure 6e; Extended Data Figure 9\n  quote: we used genesorteR 44 with slightly relaxed parameters (quant = 0.7) to identify DE genes\n    selective for one or two of these three t-type sets, and found 219 such marker genes ( Extended\n    Data Fig. 9 ). ... Furthermore, 77 of these 219 marker genes (including four genes shown in Fig.\n    6e ) were also defined as marker genes by Patch-seq\n  statistics:\n  - about: GO term axon\n    test: ToppGene enrichment\n    p: 0.0000035\n    corrected: Bonferroni\n  - about: GO term synapse\n    test: ToppGene enrichment\n    p: 0.000053\n    corrected: Bonferroni\n  - about: GO term calcium ion binding\n    test: ToppGene enrichment\n    p: 0.008\n    corrected: Bonferroni\n  - about: GO term extracellular matrix organization\n    test: ToppGene enrichment\n    p: 0.00002\n    corrected: Bonferroni\n  data: elsewhere\n  where: Allen Brain Map RNA-seq data (https://portal.brain-map.org/atlases-and-data/rnaseq), as the\n    Methods name them; not pinned\n  expected:\n  - quantity: marker genes among deep types\n    value: 219\n    tolerance: 21.9\n  - quantity: of them also Patch-seq markers\n    value: 77\n    tolerance: 7.7\n  criterion: Not tested on the dandiset.\n- id: fig6f-smi32\n  statement: Large FREM3 and CARM1P1 neurons in deep L3 are SMI-32 immunoreactive while COL22A1\n    neurons are not, and NEFH, the gene coding the SMI-32 epitope, is higher in deep FREM3 and\n    CARM1P1 than in COL22A1 and the superficial types.\n  source: Results, Deep L3 human glutamatergic t-types are morpho-electrically distinct, paragraph\n    7; Figure 6e and 6f\n  quote: The large FREM3 and CARM1P1 neurons were SMI-32ir, while COL22A1 neurons were not SMI-32ir.\n    Furthermore, the gene coding SMI-32, NEFH, also shows increased expression in deep FREM3 and\n    CARM1P1 relative to COL22A1 and all the superficial glutamatergic t-types ( Fig. 6e ).\n  data: elsewhere\n  where: The mFISH and SMI-32 images are not deposited in any archive the paper or the code names;\n    NEFH expression from the Allen Brain Map RNA-seq data, not pinned\n  criterion: Not tested on the dandiset. The paper gives no counts of labelled cells.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 tools/claims_check.py claims/000023/10.1101-2020.03.31.018820.yaml paper/10.1101-2020.03.31.018820.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/000023 && python3 - <<'EOF'
p='10.1101-2020.03.31.018820.yaml'
s=open(p).read()
s=s.replace("""  quote: For homologous t-types, results are shown for unpaired t-tests across species for each
    feature: FDR-corrected p-values as well as Cohen’s d effect size (positive if human values are
    larger). 17out of 18 features are significant at FDR<0.05.""","""  quote: For homologous t-types, results are shown for unpaired t-tests across species for each
    feature ... 17out of 18 features are significant at FDR<0.05.""")
open(p,'w').write(s)
import re
for i,l in enumerate(s.splitlines(),1):
    if not l.lstrip().startswith('#') and re.search(r'\S: ', l.split(':',1)[1] if ':' in l else ''):
        print(i,l)
for w in ['—','rather']:
    print(w, w in s)
EOF
cd ../.. && python3 tools/claims_check.py claims/000023/10.1101-2020.03.31.018820.yaml paper/10.1101-2020.03.31.018820.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I've written `claims/000023/10.1101-2020.03.31.018820.yaml`. The quote checker passes except for two values it can't parse: the GO p-values printed as "p=3.5 10 −6" and "p=5.3 10 −5". I read them in the text and they are correct. Nothing is committed.

**Text read:** the bioRxiv preprint, version 1 (the version the dandiset names), from the JATS XML: main text, Methods, figure legends, and the legends of the Extended Data figures and tables. There is no PDF, so none of the figures could be read.

**Code read:** `AllenInstitute/patchseq_human_L23` at commit `3daf9f0803ea0c220a040ea523f23af5f93c56ac`. That commit was updated for the later Nature version, so some of its outputs differ from the preprint. In those places the criteria follow the preprint's Methods and run the code's choice as a variant:
- its feature table has 316 human cells, against the preprint's 283;
- its comparison of the three homologous types uses only the superficial FREM3 cells;
- the updated pathology notebook finds 2 significant comparisons out of 18, against 1 in the original.

**Counts:** 33 claims (1 link check, 32 findings). 32 have quotes; the link has none and needs none. 17 statistical values, and every claim has a criterion or expected values.
- 13 can be tested on the dandiset once each cell's t-type and depth are attached: 12 `with_labels` (cell counts, depth by type, the type ANOVAs, FREM3 depth correlations, the human classifier, pairwise deep-type tests) plus the link.
- 4 are `with_inputs`: pathology against electrophysiology, the mouse ANOVA, the mouse classifier, and the human against mouse comparison.
- 16 are `elsewhere`: histology, transcriptomics, morphology and SMI-32.

**Details the paper leaves open, and the readings named:**
- **Which cells have features:** at least one feature, all 18, or no more than 3 of 18 missing.
- **Donor count of 90:** all subjects in the dandiset, or the donors of the paper's 385 cells.
- **Cells in the pathology comparison:** temporal cortex only, as the code does, or all regions, as the text says. The paper doesn't name the test; the code settles it as a Mann-Whitney test whose p is half the two-sided value (the scipy 1.4 default), at Bonferroni 0.05/18. The two-sided test is run as a variant.
- **"About 5 mV more hyperpolarized":** difference of medians or of means.
- **"Almost entirely in deep L3":** at least 90% or at least 80% of cells deeper than 0.575.
- **The cross-species t-test:** Student's or Welch's. The code's Mann-Whitney test is a variant.
- **"Faster AP upstroke" in CARM1P1:** the upstroke rate or the upstroke/downstroke ratio.
- **Version of the feature software (IPFX):** not given. A current release is used as a standard choice, checked against the code's feature table by the link claim.
- **"Most cases below 1.0":** read as more than half of donors.
- **"Strongest" depth correlations:** read as the largest explained variance.

**Missing from the text:**
- The contents of Extended Data Table 1 (cross-species values per feature) and Table 2 (donors).
- Supplementary Data 1 (results per feature).
- The figure images.

No claim depends on numbers that appear only in those. Two gaps did leave parts untested:
- **Deep-type ANOVA:** the text doesn't say whether its "maximum R² = 0.26" for the homologous types is electrophysiology or morphology, so that number isn't tested.
- **Mouse recordings:** the paper doesn't say where they are deposited. The mouse claims rely on the code's tables.

## End of run

33 turns, 8 minutes, result: success.
