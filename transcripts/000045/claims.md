# 000045 · claims · run 39725874322

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/000045 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -40 paper/*.txt; ls -la paper
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -c 9000 claims/001453/*.yaml | tail -c 7000; echo ----; wc -l paper/*.txt; ls -la paper; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
wc -l paper/*.txt; ls -la paper; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; fold -s -w 200 paper/10.7554-elife.63711.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent**

I have the paper text (eLife version of record via Europe PMC, with one supplement file merged into it). Reading it now.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 300
}
```

```
1	DOI: 10.7554/elife.63711
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 1 supplement file(s) from the PMC Open Access cloud data (PMC8137147), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	pmc eLife Elife 1894 elife 101579614 eLife eLife 2050-084X eLife Sciences Publications, Ltd PMC8137147 PMC8137147.1 8137147 8137147 34011433 10.7554/eLife.63711 63711 1 Tools and Resources 
8	Neuroscience Standardized and reproducible measurement of decision-making in mice [removed: an e-mail address] The International Brain Laboratory Aguillon-Rodriguez Valeria 1 Angelaki Dora 
9	https://orcid.org/0000-0002-9650-8962 2 Bayer Hannah https://orcid.org/0000-0002-5644-4124 3 Bonacchi Niccolo 4 Carandini Matteo https://orcid.org/0000-0003-4880-7682 5 Cazettes Fanny 
10	https://orcid.org/0000-0002-9648-4761 4 Chapuis Gaelle 6 Churchland Anne K https://orcid.org/0000-0002-3205-3794 1 † Dan Yang https://orcid.org/0000-0002-3818-877X 7 Dewitt Eric 4 Faulkner Mayo 6 
11	Forrest Hamish 5 Haetzel Laura 8 Häusser Michael https://orcid.org/0000-0002-2673-8957 6 Hofer Sonja B 9 Hu Fei https://orcid.org/0000-0001-7827-9548 7 Khanal Anup 
12	https://orcid.org/0000-0002-8929-7984 1 † Krasniak Christopher 1 10 Laranjeira Ines 4 Mainen Zachary F https://orcid.org/0000-0001-7913-9109 4 Meijer Guido 4 Miska Nathaniel J 9 Mrsic-Flogel Thomas D 
13	9 Murakami Masayoshi 4 ‡ Noel Jean-Paul https://orcid.org/0000-0001-5297-3363 2 Pan-Vazquez Alejandro 8 Rossant Cyrille 11 Sanders Joshua 12 Socha Karolina 5 Terry Rebecca 11 Urai Anne E 
14	https://orcid.org/0000-0001-5270-6513 1 13 Vergara Hernando 9 Wells Miles 11 Wilson Christian J 2 Witten Ilana B https://orcid.org/0000-0003-0548-2160 8 Wool Lauren E 11 Zador Anthony M 1 1 Cold 
15	Spring Harbor Laboratory New York United States 2 Center for Neural 
[... 285 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 300,
 "limit": 400
}
```

```
File content (30734 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 300,
 "limit": 250
}
```

```
300	al., 2019 ; Charles et al., 2020 ; Forscher et al., 2020 ; Koscielny et al., 2014 ; Poldrack and Gorgolewski, 2014 ; de Vries et al., 2020 ). Our work benefited from collaborative development of the 
301	behavioral assay, and from frequent and regular meetings where data were reviewed across laboratories ( Figure 6 ). These meetings helped identify problems at the origin, provide immediate feedback, 
302	and find collective solutions. Moreover, our work benefited from constant efforts at standardization. We took great care in standardizing and documenting the behavioral apparatus and the training 
303	protocol (see Appendices), to facilitate implementation across our laboratories and to encourage wider adoption by other laboratories. The protocols, hardware designs and software code are 
304	open-source and modular, allowing adjustments to accommodate a variety of scientific questions. The data are accessible at data.internationalbrainlab.org , and include all >5 million choices made by 
305	the mice. Figure 6. Contribution diagram. The following diagram illustrates the contributions of each author, based on the CRediT taxonomy ( Brand et al., 2015 ). For each type of contribution there 
306	are three levels indicated by color in the diagram: 'support’ (light), ‘equal’ (medium) and ‘lead’ (dark). Another element that might have contributed to success is our choice of behavioral task, 
307	which places substantial requirements on the mice while not being too complex. Previous failures to reproduce mouse behavior across laboratories typically arose in studies of unconstrained behavior 
308	such as responses to pain or stress ( Chesler et al., 2002 ; Crabbe et al., 1999 ; Kafkafi et al., 2018 ; Sorge et al., 2014 ; Tuttle et al., 2018 ). Operant behaviors may be inherently more 
309	reproducible than the assays used in these studies. To be able to study decision making, and in hopes of achieving reproducibility, we designed a task that engages multiple brain proces
[... 240 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -o "Appendix 1[^ ]\{0,10\}\|SUPPLEMENT\|Supplementary\|=====.*\|table 1d\|Criteria to assess" $TMPDIR/p.txt | head -50; grep -n "^-----\|supp" $TMPDIR/p.txt | head
```

```
104:Appendix 1—table
108:Appendix 1—table
120:Appendix 1—table
130:Appendix 1—table
137:Appendix 1—table
342:Appendix 1—table
376:Criteria to assess
594:Appendix 1:
606:Appendix 1
606:Appendix 1—table
755:Supplementary
1003:Appendix 1:
5:Extracted: as fetched; with 1 supplement file(s) from the PMC Open Access cloud data (PMC8137147), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6:------------------------------------------------------------------------
50:pmc-status-released yes pmc-prop-open-access yes pmc-prop-olf no pmc-prop-manuscript no pmc-prop-legally-suppressed no pmc-prop-has-pdf yes pmc-prop-has-supplement yes pmc-prop-pdf-only no 
51:pmc-prop-suppress-copyright no pmc-prop-is-real-version no pmc-prop-is-scanned-article no pmc-prop-preprint no pmc-prop-in-epmc yes pmc-license-ref CC BY Author impact statement A standard for 
66:computations that support decision-making but simple enough for mice to learn, and easily extendable to study further aspects of perception and cognition. Moreover, it can be invaluable to have ready 
94:averaged over a rolling window of 10 trials ( Figure 1—figure supplement 1 ). ( f ) Psychometric curves for those sessions, showing the fraction of trials in which the stimulus on the right was 
96:error bars show ±68% confidence intervals. The training history of this mouse can be explored at this interactive web page. Figure 1—figure supplement 1. Task trial structure. Trials began with an 
99:incorrect trials, there was a noise burst and a 2 s timeout before the next trial. Figure 1—figure supplement 2. Distribution of within-session disengagement criteria. The session ended if one of the 
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 590,
 "limit": 200
}
```

```
590	window on cognition Neuron 80 791 806 10.1016/j.neuron.2013.10.047 24183028 PMC3852636 Smith NJ Hudon C broessli SS Quackenbush P Hudson-Doyle M Humber M Leinweber K Kibirige H Davidson-Pilon C 2018 
591	pydata/patsy Zenodo v0.5.1 10.5281/zenodo.1472929 Sorge RE Martin LJ Isbester KA Sotocinal SG Rosen S Tuttle AH Wieskopf JS Acland EL Dokova A Kadoura B Leger P Mapplebeck JC McPhail M Delaney A 
592	Wigerblad G Schumann AP Quinn T Frasnelli J Svensson CI Sternberg WF Mogil JS 2014 Olfactory exposure to males, including men, causes stress and related analgesia in rodents Nature Methods 11 629 632 
593	10.1038/nmeth.2935 24776635 Tanner WP Swets JA 1954 A decision-making theory of visual detection Psychological Review 61 401 409 10.1037/h0058700 13215690 Terman M Terman JS 1972 Concurrent variation 
594	of response Bias and sensitivity in an operant-psychophysical test Perception & Psychophysics 11 428 432 10.3758/BF03206285 The International Brain Laboratory 2020a Behavior: Appendix 1: IBL Protocol 
595	for Headbar Implant Surgery in Mice figshare 10.6084/m9.figshare.11634726.v4 The International Brain Laboratory 2020b Behavior: Appendix 2: IBL Protocol for Mice Training figshare 
596	10.6084/m9.figshare.11634729.v3 The International Brain Laboratory 2021a Behavior: Appendix 3: IBL Protocol for Setting Up the Behavioral Training Rig figshare 10.6084/m9.figshare.11634732.v6 The 
597	International Brain Laboratory 2021b paper-behavior Software Heritage swh:1:rev:edc453189104a1f76f4b2ab230cd86f2140e3f63 
598	https://archive.softwareheritage.org/swh:1:rev:edc453189104a1f76f4b2ab230cd86f2140e3f63 Tuttle AH Philip VM Chesler EJ Mogil JS 2018 Comparing phenotypic variation between inbred and outbred mice 
599	Nature Methods 15 994 996 10.1038/s41592-018-0224-7 30504873 PMC6518396 Urai AE Braun A Donner TH 2017 Pupil-linked arousal is driven by decision uncertainty and alters serial choice bias Nature 
600	Communications 8 14637 10.1038/ncomms14637 PMC5337963 28256514 U
[... 189 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 790,
 "limit": 300
}
```

```
790	by people who study perceptual decision making, as the reviewers have pointed out. 2. Overall, we believe the authors may have missed a good opportunity. Two out of the three reviewers felt the 
791	manuscript did not sufficiently articulate the value of the approach. A few lines were added to the discussion, but we feel more could have been done. We thank the reviewers for pushing us in this 
792	direction. We have made some edits to the Introduction, where the first three paragraphs explain that (1) Progress in science depends on reproducibility, but neuroscience faces a crisis of 
793	reproducibility; (2) Reproducibility has been a particular concern for measurements of mouse behavior; (3) A difficulty in reproducing mouse behavior across laboratories would be problematic for the 
794	increasing number of studies that investigate decision making in the mouse. Also in Introduction, we have strengthened the point about the value of Open Science approaches. We have also added a 
795	paragraph in Discussion: “A reproducible behavioral task can be invaluable to establish the neural basis of behavior. If different studies use the same task, they can directly compare their findings. 
796	There are indeed illustrious examples of behavioral tasks that serve this role. For studying decision-making in primates, these include the tactile flutter comparison task […] and the random dots 
797	visual discrimination task […]. Both tasks have been used in multiple studies to record from different brain regions while enabling a meaningful comparison of the results. Conversely, without a 
798	standardized behavioral task we face the common situation where different laboratories record from different neurons in different regions in different tasks, likely drawing different conclusions and 
799	likely not sharing their data. In that situation it is not possible to establish which factors determine the different conclusions and come to a collective understanding.” 3. It would be he
[... 291 more lines not kept]
```

**Agent**

Full text, Methods, figure legends and Appendix 1 table are present; the only supplement file is the transparent reporting form. Now the dataset's archive description and the paper's code.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000045/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:3000])"; curl -s "https://api.dandiarchive.org/api/dandisets/000045/versions/" | python -c "import json,sys;d=json.load(sys.stdin);[print(v['version'],v['name'],v.get('asset_count'),v.get('size')) for v in d['results']]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000045/versions/0.211209.1413/ | python -c "import json,sys;d=json.load(sys.stdin);[print(k,':',json.dumps(d.get(k))[:1500]) for k in ['description','relatedResource','citation','assetsSummary','keywords','studyTarget','protocol']]"
```

Result: the fetched text is not kept.

**Agent**

Dataset: 178 subjects, 6615 NWB files, behavior from the IBL task. Now cloning the paper's code at the archived commit.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/int-brain-lab/paper-behavior.git && cd paper-behavior && git checkout -q edc453189104a1f76f4b2ab230cd86f2140e3f63 && git log -1 --format='%H %ad %s' && ls
```

```
edc453189104a1f76f4b2ab230cd86f2140e3f63 Thu Apr 8 15:13:40 2021 +0200 added revision after peer review to contribution table
LICENSE
README.md
__init__.py
authorship
create_csv_data_files.py
dj_env.yml
figure1c_number_of_mice.py
figure1def_training.py
figure2af_learning_curves_all_parameters.py
figure2d_training_probability.py
figure2g_time_to_trained.py
figure3ab_psychfuncs.py
figure3cde_variability_over_labs_basic_&_suppfig3-2.py
figure3f_classifier_lab_membership_basic.py
figure3f_plot_classifier_basic.py
figure4a_block_probabilities.py
figure4de_psychfuncs_biased.py
figure4fghi_variability_over_labs_full.py
figure4i_classifier_lab_membership_full.py
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-behavior && cat README.md && cat paper_behavior_functions.py
```

````
# paper-behavior
This repository contains code to reproduce all figures of the behavior paper by the International Brain Laboratory. If reusing any part of this code please cite the [bioRxiv paper](https://www.biorxiv.org/content/10.1101/2020.01.17.909838v2) in which these figures appear. 

### Installation
These instructions require anaconda (https://www.anaconda.com/distribution/#download-section) for Python 3 and git (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

In an Anaconda prompt window:
1. Clone or download the paper-bahavior repository
2. Install the other dependencies by running `pip install -r requirements.txt`

To call the functions in this repo, either run python from within the `paper-bahavior` folder or
add the folder to your python path: 
```python
import sys
sys.path.extend([r'path/to/paper-behavior'])
```

### Obtain a DataJoint account through IBL JupyterHub
[IBL Jupyterhub](https://jupyterhub.internationalbrainlab.org) provides an online environment to explore the IBL behavior data pipeline.

[... 654 more lines not kept]
````

**Agent**

The code holds one script per figure panel, querying the IBL DataJoint database (or CSVs at a Flatiron zip). Reading the scripts behind each finding.

**Agent calls Bash**

```bash
cd $TMPDIR/paper-behavior && wc -l *.py && cat figure2g_time_to_trained.py "figure3cde_variability_over_labs_basic_&_suppfig3-2.py"
```

```
0 __init__.py
   210 create_csv_data_files.py
    72 figure1c_number_of_mice.py
   245 figure1def_training.py
   257 figure2af_learning_curves_all_parameters.py
   136 figure2d_training_probability.py
   182 figure2g_time_to_trained.py
   142 figure3ab_psychfuncs.py
   203 figure3cde_variability_over_labs_basic_&_suppfig3-2.py
   193 figure3f_classifier_lab_membership_basic.py
   118 figure3f_plot_classifier_basic.py
   119 figure4a_block_probabilities.py
   239 figure4de_psychfuncs_biased.py
   165 figure4fghi_variability_over_labs_full.py
   182 figure4i_classifier_lab_membership_full.py
    51 figure4i_plot_classifier_full.py
   167 figure5_GLM_modelfit.py
   217 figure5_GLM_plot.py
   209 figure5_GLM_simulate.py
   619 paper_behavior_functions.py
[... 403 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-behavior && cat figure3f_classifier_lab_membership_basic.py figure3f_plot_classifier_basic.py | grep -v "^\s*#"
```

```
"""
Decode in which lab a mouse was trained based on its behavioral metrics during the three sessions
of the basic task variant in which the mouse was determined to be trained.

As a positive control, the time zone in which the mouse was trained is included in the dataset
since the timezone provides geographical information. Decoding is performed using leave-one-out
cross-validation. To control for the imbalance in the dataset (some labs have more mice than
others) a fixed number of mice is randomly sub-sampled from each lab. This random sampling is
repeated for a large number of repetitions. A shuffled nul-distribution is obtained by shuffling
the lab labels and decoding again for each iteration.

--------------
Parameters
DECODER:            Which decoder to use: 'bayes', 'forest', or 'regression'
N_MICE:             How many mice per lab to randomly sub-sample
                    (must be lower than the lab with the least mice)
ITERATIONS:         Number of times to randomly sub-sample
METRICS:            List of strings indicating which behavioral metrics to include
                    during decoding of lab membership
METRICS_CONTROL:    List of strings indicating which metrics to use for the positive control
[... 257 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-behavior && cat figure4de_psychfuncs_biased.py figure4fghi_variability_over_labs_full.py | grep -v "^\s*#"
```

```
"""
Psychometric function and choice shifts in the biased task

@author: Anne Urai
15 January 2020
"""

import pandas as pd
import numpy as np
import os
from os.path import join
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
from paper_behavior_functions import (seaborn_style, figpath, group_colors, institution_map,
                                      query_sessions_around_criterion, EXAMPLE_MOUSE,
                                      FIGURE_HEIGHT, FIGURE_WIDTH, QUERY, load_csv,
                                      dj2pandas, plot_psychometric, fit_psychfunc, plot_chronometric,
                                      break_xaxis)
[... 334 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-behavior && cat figure5_GLM_modelfit.py figure5_GLM_plot.py | grep -v "^\s*#"
```

```
"""
Created on 2020-07-20
@author: Anne Urai
"""
from pathlib import Path

import pandas as pd
import numpy as np
from paper_behavior_functions import (query_sessions_around_criterion,
                                      institution_map, dj2pandas, load_csv, datapath)
from ibl_pipeline import behavior, subject, reference
from tqdm.auto import tqdm
from sklearn.model_selection import KFold

import patsy # to build design matrix
import statsmodels.api as sm

tqdm.pandas(desc="model fitting")

query = True
[... 296 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-behavior && cat suppfig_choicevariability_withinacrosslabs.py figure2af_learning_curves_all_parameters.py | grep -v "^\s*#"
```

```
"""
Choice variability across contrasts within each lab and across labs

@author: Anne Urai
2 September 2020
"""

import numpy as np
import seaborn as sns
import os
import pandas as pd
import matplotlib.pyplot as plt
from paper_behavior_functions import (figpath, seaborn_style, group_colors,
                                      query_sessions_around_criterion, institution_map,
                                      FIGURE_HEIGHT, FIGURE_WIDTH, dj2pandas)
from ibl_pipeline import reference, subject, behavior
from sklearn.utils import shuffle

from tqdm.auto import tqdm
tqdm.pandas(desc="computing")
[... 366 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-behavior && cat figure2d_training_probability.py suppfig_variability_over_labs_first_biased.py "suppfig_3-4a-f.py" | grep -v "^\s*#"; grep -n "def \|perform_thres\|query_session_around\|criterion" supp_queries.py create_csv_data_files.py | head -60
```

```
"""
Quantify the variability of the time to trained over labs.

@author: Guido Meijer, Miles Wells
16 Jan 2020
"""
from os.path import join

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import seaborn as sns

from ibl_pipeline import subject
from ibl_pipeline.analyses import behavior as behavior_analysis
from paper_behavior_functions import (seaborn_style, institution_map, query_subjects,
                                      group_colors, figpath, load_csv, CUTOFF_DATE,
                                      FIGURE_HEIGHT, FIGURE_WIDTH, QUERY)
from lifelines import KaplanMeierFitter
[... 465 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-behavior && sed -n 95,200p suppfig_choicevariability_withinacrosslabs.py; grep -n "nfits\|def mle_fit_psycho" -r . | head
```

```
'session_start_time', 'trial_id'])
                         .reset_index())

behav['institution_code'] = behav.institution_short.map(institution_map)
# split the two types of task protocols (remove the pybpod version number)
behav.drop(behav[behav['signed_contrast'].isin([50., -50])].index, inplace=True)
df_basic = behav.groupby(['institution_code', 'subject_nickname', 'signed_contrast']).agg(
    {'choice2': 'mean'}).reset_index().copy()

# query sessions - FULL TASK
use_sessions, _ = query_sessions_around_criterion(criterion='ephys',
                                                  days_from_criterion=[2, 0],
                                                  force_cutoff=True)
use_sessions = use_sessions & 'task_protocol LIKE "%biased%"'  # only get biased sessions

# restrict by list of dicts with uuids for these sessions
b = (use_sessions * subject.Subject * subject.SubjectLab * reference.Lab
     * behavior.TrialSet.Trial)

# reduce the size of the fetch
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-behavior && grep -v "^\s*#" suppfig_history_strategy.py | sed -n 1,140p
```

```
"""
History-dependent choice strategy across tasks
See also https://elifesciences.org/articles/49834

@author: Anne Urai
10 May 2020
"""

from ibl_pipeline import behavior, subject, reference
import matplotlib.pyplot as plt
from paper_behavior_functions import (seaborn_style, figpath, query_sessions_around_criterion,
                                      group_colors, institution_map, FIGURE_WIDTH, FIGURE_HEIGHT,
                                      dj2pandas, plot_psychometric, fit_psychfunc)
import statsmodels.api as sm
from statsmodels.formula.api import ols
import pycircstat
import seaborn as sns
import pandas as pd
import numpy as np
import os
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-behavior && grep -n "corrected\|future_shift\|history_shift\|- \|stay\|switch" suppfig_history_strategy.py | sed -n 1,40p; grep -n "nshuf\|pval\|choice_var'\].mean" suppfig_choicevariability_withinacrosslabs.py | head -20
```

```
80:# PREVIOUS CHOICE - SUMMARY PLOT
151:    pars3['bias_shift'] = pars3.right - pars3.left
163:history_shift = pars2shift(pars, 'previous_choice_name', 'previous_outcome_name')
169:future_shift = pars2shift(pars, 'next_choice_name', 'next_outcome_name')
171:history_shift = history_shift.merge(future_shift, on=['subject_nickname', 'institution_code', 'task'])
172:history_shift['post_correct_corr'] = history_shift['post_correct'] - history_shift['pre_correct']
173:history_shift['post_error_corr'] = history_shift['post_error'] - history_shift['pre_error']
176:num_dp = history_shift.groupby(['subject_nickname'])['post_error'].count().reset_index()
184:which_plots = [['post_correct', 'post_error', 'History strategy, uncorrected'],
185:               ['pre_correct', 'pre_error', 'Future, uncorrected'],
186:               ['post_correct_corr', 'post_error_corr', 'History strategy, corrected']]
196:        sns.kdeplot(data=history_shift[(history_shift.task == task)].dropna(subset=[w[0], w[1]])[w[0]],
197:                    data2=history_shift[(history_shift.task == task)].dropna(subset=[w[0], w[1]])[w[1]],
204:                     data=history_shift[(history_shift.task == task)], marker='o',
208:        mean_perlab = history_shift.drop('subject_nickname', 1).\
217:        ax.arrow(history_shift[(history_shift['task'] == 'traini')][w[0]].mean(),
218:                 history_shift[(history_shift['task'] == 'traini')][w[1]].mean(),
219:                 history_shift[(history_shift['task'] == 'biased')][w[0]].mean() -
220:                 history_shift[(history_shift['task'] == 'traini')][w[0]].mean(),
221:                 history_shift[(history_shift['task'] == 'biased')][w[1]].mean() -
[... 29 more lines not kept]
```

**Agent**

Now the claims schema, to get the fields right.

**Agent calls Bash**

```bash
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1))" | head -250
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
python -c "import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1))"; grep -n "expected:" -A8 claims/001453/*.yaml | head -40; grep -n "ci:\|corrected:\|about:" -A2 claims/*/*.yaml | head -20
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
[... 121 more lines not kept]
```

**Agent**

I've got most of the analysis code. A few more scripts for the remaining reported numbers.

**Agent calls Bash**

```bash
cd $TMPDIR/paper-behavior && grep -n "DECODER =\|METRICS\b\|METRICS =\|METRICS_CONTROL =\|query_session\|days_from" figure4i_classifier_lab_membership_full.py suppfig_classifier_lab_membership_perf.py suppfig_classifier_lab_membership_first_biased.py; grep -rn "quartile\|RandomForest" --include=*.py . | grep -v "figure3f\|figure4i\|suppfig_classifier" | head; grep -v "^\s*#" suppfig_variability_over_time.py | sed -n 1,101p
```

```
figure4i_classifier_lab_membership_full.py:20:METRICS:            List of strings indicating which behavioral metrics to include
figure4i_classifier_lab_membership_full.py:40:DECODER = 'bayes'           # bayes, forest or regression
figure4i_classifier_lab_membership_full.py:43:METRICS = ['threshold_l', 'threshold_r', 'bias_l', 'bias_r', 'lapselow_l', 'lapselow_r',
figure4i_classifier_lab_membership_full.py:45:METRICS_CONTROL = ['threshold_l', 'threshold_r', 'bias_l', 'bias_r', 'lapselow_l', 'lapselow_r',
figure4i_classifier_lab_membership_full.py:64:    from paper_behavior_functions import query_sessions_around_criterion
figure4i_classifier_lab_membership_full.py:66:    use_sessions, _ = query_sessions_around_criterion(criterion='ephys',
figure4i_classifier_lab_membership_full.py:67:                                                      days_from_criterion=[2, 0])
figure4i_classifier_lab_membership_full.py:123:if DECODER == 'forest':
figure4i_classifier_lab_membership_full.py:125:elif DECODER == 'bayes':
figure4i_classifier_lab_membership_full.py:127:elif DECODER == 'regression':
figure4i_classifier_lab_membership_full.py:136:decoding_set = decod[METRICS].values
suppfig_classifier_lab_membership_perf.py:20:METRICS:            List of strings indicating which behavioral metrics to include
suppfig_classifier_lab_membership_perf.py:31:from paper_behavior_functions import (query_session_around_performance, institution_map, QUERY,
suppfig_classifier_lab_membership_perf.py:40:DECODER = 'bayes'           # bayes, forest or regression
suppfig_classifier_lab_membership_perf.py:43:METRICS = ['perf_easy', 'threshold', 'bias']
suppfig_classifier_lab_membership_perf.py:44:METRICS_CONTROL = ['perf_easy', 'threshold', 'bias', 'time_zone']
suppfig_classifier_lab_membership_perf.py:62:    behav = query_session_around_performance()
suppfig_classifier_lab_membership_perf.py:119:if DECODER == 'forest':
suppfig_classifier_lab_membership_perf.py:121:elif DECODER == 'bayes':
suppfig_class
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-behavior && sed -n 1,140p supp_queries.py; sed -n 190,329p supp_queries.py | grep -v "^\s*$"
```

```
"""
This file contains some supplementary queries and statistics for the paper.

@author: Miles Wells
"""
import pandas as pd
import numpy as np
import datajoint as dj
from ibl_pipeline import behavior, acquisition, subject, action
from ibl_pipeline.analyses import behavior as behavior_analysis

from paper_behavior_functions import (
    query_subjects, EXAMPLE_MOUSE, institution_map, CUTOFF_DATE, load_csv
)


############################
# Days to full proficiency #
############################
"""This section prints the mean number of days and trials required to reach full task
[... 245 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/paper-behavior && sed -n 40,80p figure4i_classifier_lab_membership_full.py; sed -n 60,75p suppfig_classifier_lab_membership_first_biased.py; grep -n "def mle_fit_psycho" -A12 $(python -c "import brainbox,os;print(os.path.dirname(brainbox.__file__))" 2>/dev/null)/behavior/pyschofit.py 2>&1 | head -5; python -c "from scipy import stats;print(2*stats.t.sf(4.817,125), 2*stats.t.sf(10.736,125)); print(stats.f.sf(1.345,6,91))"
```

```
Exit code 1
DECODER = 'bayes'           # bayes, forest or regression
N_MICE = 8                  # how many mice per lab to randomply sub-sample
ITERATIONS = 2000           # how often to decode with random sub-samples
METRICS = ['threshold_l', 'threshold_r', 'bias_l', 'bias_r', 'lapselow_l', 'lapselow_r',
           'lapsehigh_l', 'lapsehigh_r']
METRICS_CONTROL = ['threshold_l', 'threshold_r', 'bias_l', 'bias_r', 'lapselow_l', 'lapselow_r',
                   'lapsehigh_l', 'lapsehigh_r', 'time_zone']


# Decoding function with n-fold cross validation
def decoding(data, labels, clf):
    kf = LeaveOneOut()
    y_pred = np.empty(len(labels), dtype='<U5')
    for train_index, test_index in kf.split(data):
        clf.fit(data[train_index], labels[train_index])
        y_pred[test_index] = clf.predict(data[test_index])
    f1 = f1_score(labels, y_pred, average='micro')
    cm = confusion_matrix(labels, y_pred)
    return f1, cm
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import math
def tpdf(x,v): return math.exp(math.lgamma((v+1)/2)-math.lgamma(v/2))/math.sqrt(v*math.pi)*(1+x*x/v)**(-(v+1)/2)
def sf(t,v,N=200000,U=60):
  h=(U-t)/N; s=0
  for i in range(N+1):
    x=t+i*h; w=1 if i in(0,N) else (4 if i%2 else 2); s+=w*tpdf(x,v)
  return s*h/3
print(2*sf(4.817,125), 2*sf(10.736,125))
"
```

```
4.1369823677689344e-06 1.8731585875383932e-19
```

**Agent**

I have what I need from the paper and the code. Writing the claims file now.

**Agent calls Bash**

```bash
mkdir -p claims/000045; grep -o "Mice incorporated block priors[^.]*\.\|The model fit the mouse choices well[^.]*\.\|As expected, visual terms[^.]*\.\|When taking these slow[^.]*\.\|After rewarded trials, choice updating[^.]*\." paper/10.7554-elife.63711.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/000045/10.7554-elife.63711.yaml",
 "content": "# Claims for The International Brain Laboratory (2021), \"Standardized and reproducible measurement\n# of decision-making in mice\", eLife 10:e63711, on dandiset 000045 (\"IBL behavioral data\").\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, under\n# docs/protocol.md version pilot-10.\n#\n# Text read: the version of record (eLife, PMC8137147, as served by Europe PMC), full text with\n# Results, figure legends and figure supplement legends, Materials and methods, Appendix 1 (table 1,\n# standardization and proficiency criteria), the decision letter and author response. The only\n# supplementary file is eLife's transparent reporting form; it holds no results. The Methods refer\n# the psychometric fitting procedure and the full training criteria to \"Protocol 2\" (IBL Protocol\n# for Mice Training, figshare doi:10.6084/m9.figshare.11634729.v3), which is not in paper/ and was\n# not read; the code below settles the fitting procedure.\n#\n# Code read: github.com/int-brain-lab/paper-behavior at commit\n# edc453189104a1f76f4b2ab230cd86f2140e3f63 (the commit the paper archives at Software Heritage).\n# One script per figure panel; each queries the IBL DataJoint pipeline (or CSV extracts of it) and\n# uses paper_behavior_functions.py for the shared selection, trial coding and psychometric fit. The\n# psychometric fit itself is brainbox.behavior.pyschofit (ibllib), which the repository imports.\n# The code for the Random Forest prediction of slow learners (Results, Training succeeded,\n# paragraph 4) and for Figure 5, figure supplement 1c statistics is not in the repository.\n#\n# Data the paper used. Female and male C57BL6/J mice, 3 to 7 months old, trained in seven\n# laboratories in three countries (code lab numbers: UCL Lab 1, CCU/Champalimaud Lab 2, CSHL Lab 3,\n# NYU Lab 4, Princeton Lab 5, SWC Lab 6, Berkeley Lab 7; time zones Europe 0, New York -5,\n# Los Angeles -7 hours in the code). 210 mice entered, 4 were excluded for adverse effects, 206\n# started training, 140 reached basic task proficiency and 98 full task proficiency. Mice are those\n# of project ibl_neuropixel_brainwide_01 that reached the criterion by 2020-03-23, and only\n# sessions up to that date are used (code CUTOFF_DATE); one session\n# (a9fb578a-9d7d-42b4-8dbc-3b419ce9f424) is excluded in the code. One session a day, trials with:\n# signed contrast (left or right, 100, 50, 25, 12.5, 6.25, 0%), the wheel choice (left, right or\n# no response within 60 s), feedback (reward or noise burst), stimulus onset and response times,\n# the block's probability of a left stimulus (50, 20 or 80%; full task only) and the session's\n# start and end times and task protocol (basic \"training\" or full \"biased\"). The dandiset's\n# archive description says its NWB files hold wheel movement, camera footage and trial-by-trial\n# stimulus information for this task, and names the bioRxiv version of this paper.\n#\n# Shared definitions, used by name in the criteria below. All are from the paper's Methods,\n# legends and Appendix 1 unless the code is cited.\n# - Trial coding (code dj2pandas). Signed contrast = right minus left contrast, in %. A no-response\n#   trial counts as incorrect for performance (Results: \"no-response trials ... were labeled as\n#   incorrect trials\") and is left out of the fraction of rightward choices. Performance on easy\n#   trials = % correct on trials with contrast of 50% or more. Trial duration (reaction time) =\n#   response time minus stimulus onset time, no-response trials left out.\n# - Psychometric fit (Methods, Psychometric curves; code fit_psychfunc). P = gamma + (1 - gamma -\n#   lambda) (erf((c - mu)/sigma) + 1)/2, fitted by maximum likelihood to the fraction of rightward\n#   choices per signed contrast; bias mu bounded by the smallest and largest contrast, threshold\n#   sigma in [5, 40], lapses gamma (left) and lambda (right) in [0, 1], start [0, 20, 0.05, 0.05];\n#   no fit (NaN) with fewer than four signed contrasts. The number of random restarts is\n#   psychofit's default (a standard choice, as is the seed).\n# - Basic proficiency (P1). The session at which a mouse first meets the Appendix 1, table 1d\n#   'Trained 1a/1b' criteria over its last three sessions; the code reads it as the first session\n#   with training status trained_1a or trained_1b in the IBL pipeline. Readings: the status the\n#   dataset carries, if any; otherwise recomputed from the trials with the 1a criteria, and with\n#   the 1b criteria from their introduction (Methods: September 2019, no day given).\n# - Basic sessions (S1). The basic (training protocol) sessions of the P1 training day and the two\n#   training days before it (Figure 3 legend \"the three sessions at which mice achieved\n#   proficiency\"; code days_from_criterion [2, 0]). One value per mouse from the pooled trials.\n# - Full proficiency (P2). The first session meeting the Appendix 1, table 1d 'Full task\n#   proficiency' criteria; the code reads it as the first status ready4ephysrig, ready4delay or\n#   ready4recording. Readings as for P1.\n# - Full sessions (S2). The full task (biased protocol) sessions of the P2 training day and the two\n#   days before (code days_from_criterion [2, 0]); n = 98 mice.\n# - First full-task session (P1b). The code's \"biased\" criterion: the first biased-protocol\n#   session with status trained_1b.\n# - Lab test (code figure3cde and others). Each variable is first tested for normality over all\n#   mice (scipy normaltest); the code runs a Kruskal-Wallis test across labs when p < 0.05 and a\n#   one-way ANOVA otherwise. Where the paper names the test, the named test is the main reading and\n#   the code's switch a variant.\n# - Lab classifier (Methods, Classification of laboratory membership; code figure3f). scikit-learn\n#   classifier with default settings, 8 mice drawn at random from each lab without replacement,\n#   2000 times; leave-one-out cross-validation over the 56 mice; accuracy = fraction correctly\n#   classified; a null from shuffling the lab labels in each subsample; positive control adds the\n#   lab's time zone as a feature. Code seed 424242; Random Forest with 100 trees and\n#   random_state 424242; Logistic Regression with solver liblinear.\n#\n# Tolerances. Where the paper gives mean +- s.d. over mice, the s.d. describes the spread across\n# mice and not the uncertainty of the mean, so the mean gets 10% of its value and the s.d. its own\n# 10% entry; other tolerances are 10% unless a claim says why.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000045\"\npaper: doi:10.7554/elife.63711\nclaims:\n- id: cohort-counts\n  statement: >-\n    Of 206 mice that started training, 140 reached proficiency in the basic task and 98 in the\n    full task.\n  source: Results, opening section, paragraph 3\n  quote: >-\n    Out of 206 mice that started training, 140 achieved proficiency in the basic task, and 98 in\n    the full task\n  expected:\n  - quantity: mice that started training\n    value: 206\n    tolerance: 20.6\n  - quantity: mice reaching basic task proficiency (P1)\n    value: 140\n    tolerance: 14\n  - quantity: mice reaching full task proficiency (P2)\n    value: 98\n    tolerance: 9.8\n  criterion: >-\n    Counts of distinct mice under the paper's selection (project mice, criterion reached by\n    2020-03-23, code query_subjects), proficiency as P1 and P2 under each reading. A dataset that\n    holds fewer mice is reported with the counts it holds; the claim is judged on the counts.\n\n- id: fig2g-days-to-proficiency\n  statement: >-\n    Basic task training took 18.4 +- 13.0 days (s.d., n = 140 mice), from 3 days for the fastest\n    mouse to 59 days for the slowest.\n  source: Results, Training succeeded but with different rates across mice and laboratories,\n    paragraph 1; Figure 2g\n  quote: >-\n    The average training took 18.4 ± 13.0 days (s.d., n = 140, Figure 2g )\n  expected:\n  - quantity: mean days to basic proficiency\n    value: 18.4\n    tolerance: 1.84\n    unit: days\n  - quantity: s.d. of days to basic proficiency\n    value: 13.0\n    tolerance: 1.3\n    unit: days\n  - quantity: fastest mouse\n    value: 3\n    tolerance: 0.3\n    unit: days\n  - quantity: slowest mouse\n    value: 59\n    tolerance: 5.9\n    unit: days\n  criterion: >-\n    Per mouse, the number of training days (days with a session in the per-day summary the code\n    reads) up to P1 (code figure2g_time_to_trained.py). The code's query branch counts days up to\n    and including the P1 day, its CSV branch days before it; both readings are run. Mean and s.d.\n    over the 140 mice (or those the dataset holds), and the minimum and maximum.\n\n- id: fig2g-days-differ-across-labs\n  statement: >-\n    The number of days to basic task proficiency differed across laboratories; within-lab\n    interquartile ranges ranged from 8 days (Lab 2) to 22 days (Lab 6).\n  source: Results, Training succeeded but with different rates across mice and laboratories,\n    paragraph 1; Figure 2g\n  quote: >-\n    The number of days needed to achieve basic task proficiency was different across\n    laboratories ( Figure 2g , p<0.001, Kruskal-Wallis nonparametric test followed by a post-hoc\n    Dunn's multiple comparisons test)\n  statistics:\n  - test: Kruskal-Wallis nonparametric test, then post-hoc Dunn's multiple comparisons test\n    p: 0.001\n    p_relation: \"<\"\n    n: 140 mice in 7 laboratories\n  expected:\n  - quantity: Lab 2 interquartile range of days to proficiency\n    value: 8\n    tolerance: 0.8\n    unit: days\n  - quantity: Lab 6 interquartile range of days to proficiency\n    value: 22\n    tolerance: 2.2\n    unit: days\n  depends_on:\n  - fig2g-days-to-proficiency\n  criterion: >-\n    Days per mouse as in fig2g-days-to-proficiency, under both of its readings. Kruskal-Wallis test\n    across the seven labs (the code switches to a one-way ANOVA when the days pass scipy's\n    normality test; shown as a variant). Reproduced when p < 0.001. Interquartile ranges per lab\n    are pandas' default (linear) quantiles, as in the code.\n\n- id: fig2s1-trials-to-proficiency\n  statement: >-\n    Measured in trials, basic task training took 10.8 +- 8.6 thousand trials (s.d., n = 140), from\n    one thousand for the fastest mouse to 43 thousand for the slowest; reaching 80% correct on easy\n    trials took on average about 7.4 thousand trials.\n  source: Results, Training succeeded but with different rates across mice and laboratories,\n    paragraph 2; Figure 2, figure supplement 1\n  quote: >-\n    For mice that learned the task, the average training took 10.8 ± 8.6 thousands of trials\n    (s.d., n = 140) ... The fastest learner met training criteria in one thousand trials, the\n    slowest 43 thousand trials. To reach 80% on easy trials took on average ~7.4 thousand trials.\n  expected:\n  - quantity: mean trials to basic proficiency\n    value: 10800\n    tolerance: 1080\n    unit: trials\n  - quantity: s.d. of trials to basic proficiency\n    value: 8600\n    tolerance: 860\n    unit: trials\n  - quantity: fastest mouse\n    value: 1000\n    tolerance: 100\n    unit: trials\n  - quantity: slowest mouse\n    value: 43000\n    tolerance: 4300\n    unit: trials\n  - quantity: trials to reach 80% correct on easy trials\n    value: 7400\n    tolerance: 740\n    unit: trials\n  depends_on:\n  - fig2g-days-to-proficiency\n  criterion: >-\n    Per mouse, the summed trial counts of the training days counted in fig2g-days-to-proficiency\n    (code figure2g_time_to_trained.py), under both of its readings. The 7.4 thousand trials has no\n    code in the repository; readings (1) the cumulative trial count at which the mean over mice of\n    the easy-trial performance curve (Figure 2, figure supplement 1b, 1000-trial bins as in\n    suppfig_variability_over_time.py) first exceeds 80%, and (2) the mean over mice of each\n    mouse's cumulative trials at its first session above 80% correct on easy trials.\n\n- id: fig2h-proportion-learned-40-days\n  statement: >-\n    About 80% of mice that started training would learn the basic task within the 40 days usually\n    allotted (Kaplan-Meier estimate over all 206 mice).\n  source: Results, Training succeeded but with different rates across mice and laboratories,\n    paragraph 4; Figure 2h\n  quote: >-\n    there was a 80% probability that mice would learn the task within the 40 days that were\n    usually allotted, and when mice were trained for a longer duration, the success rate rose even\n    further ( Figure 2h )\n  expected:\n    quantity: Kaplan-Meier cumulative proportion proficient at training day 40\n    value: 0.8\n    tolerance: 0.08\n  criterion: >-\n    Kaplan-Meier estimate (code figure2d_training_probability.py, lifelines) over all mice that\n    started training, leaving out mice still in training at the cutoff date: time = number of\n    sessions with status in_training or untrainable; event = the mouse's last status is neither.\n    Without status labels in the dataset, time = training days to P1 for proficient mice and\n    their total training days otherwise. Reproduced when the cumulative proportion at day 40 is\n    within the tolerance and higher at the last day than at day 40.\n\n- id: fig2bc-threshold-bias-iqr\n  statement: >-\n    Contrast threshold and bias varied little during training; the threshold interquartile range\n    slightly decreased from 12-29% in the first 10 training days to 11-23% thereafter, and the bias\n    interquartile range went from -5.2 to 7.1% to -5.6 to 6.5%.\n  source: Results, Training succeeded but with different rates across mice and laboratories,\n    paragraph 1; Figure 2b,c\n  quote: >-\n    Estimates of contrast threshold did not vary much during training ( Figure 2b ), with an\n    interquartile range that slightly decreased from 12–29% during the first 10 training days, and\n    11–23% thereafter. Likewise, bias did not vary much, with an interquartile range of −5.2% to\n    7.1% during the first 10 days to −5.6% to 6.5% thereafter ( Figure 2c ).\n  expected:\n  - quantity: threshold 25th percentile, days 1-10\n    value: 12\n    tolerance: 1.2\n    unit: \"%\"\n  - quantity: threshold 75th percentile, days 1-10\n    value: 29\n    tolerance: 2.9\n    unit: \"%\"\n  - quantity: threshold 25th percentile, after day 10\n    value: 11\n    tolerance: 1.1\n    unit: \"%\"\n  - quantity: threshold 75th percentile, after day 10\n    value: 23\n    tolerance: 2.3\n    unit: \"%\"\n  - quantity: bias 25th percentile, days 1-10\n    value: -5.2\n    tolerance: 0.52\n    unit: \"%\"\n  - quantity: bias 75th percentile, days 1-10\n    value: 7.1\n    tolerance: 0.71\n    unit: \"%\"\n  - quantity: bias 25th percentile, after day 10\n    value: -5.6\n    tolerance: 0.56\n    unit: \"%\"\n  - quantity: bias 75th percentile, after day 10\n    value: 6.5\n    tolerance: 0.65\n    unit: \"%\"\n  criterion: >-\n    Per-session psychometric threshold and bias of the 140 proficient mice, as plotted in Figure\n    2b,c (code figure2af_learning_curves_all_parameters.py): 50:50 sessions with more than 100\n    trials, threshold and bias only from sessions with six or more signed contrasts (legend: from\n    the first session with 12% contrast), each mouse's series median-filtered over 3 sessions,\n    training day counted from the mouse's first session. The code does not print the\n    interquartile ranges, so the pooling is open; readings (1) all session values pooled over mice\n    within days 1-10 and after day 10, (2) as (1) without the median filter, each with \"thereafter\"\n    as (a) days 11 to 40 (the plotted range) and (b) all later days. Reproduced when all eight\n    bounds are within tolerance under one reading and the threshold range after day 10 is\n    narrower than in days 1-10.\n\n- id: fig2-abs-bias-threshold-during-training\n  statement: >-\n    During training mice were not systematically biased to one side; absolute bias averaged\n    9.8 +- 12.1 (s.d.), and contrast threshold, which stabilized after about 10 sessions, averaged\n    17.8 +- 11.7%.\n  source: Results, Training succeeded but with different rates across mice and laboratories,\n    paragraph 2; Figure 2b,c\n  quote: >-\n    Mice across laboratories were not systematically biased towards a particular side and the\n    absolute bias was similar across laboratories (9.8 ± 12.1 [s.d.] on average). Likewise,\n    measures of contrast threshold stabilized after the first ~10 sessions, which was on average\n    17.8 ± 11.7% on average across institutions.\n  expected:\n  - quantity: mean absolute bias during training\n    value: 9.8\n    tolerance: 0.98\n    unit: \"%\"\n  - quantity: s.d. of absolute bias\n    value: 12.1\n    tolerance: 1.21\n    unit: \"%\"\n  - quantity: mean contrast threshold after about 10 sessions\n    value: 17.8\n    tolerance: 1.78\n    unit: \"%\"\n  - quantity: s.d. of contrast threshold\n    value: 11.7\n    tolerance: 1.17\n    unit: \"%\"\n  depends_on:\n  - fig2bc-threshold-bias-iqr\n  criterion: >-\n    Same per-session values and readings as fig2bc-threshold-bias-iqr. No code computes these\n    numbers; the averaging is open, with readings (1) mean and s.d. over all session values pooled\n    over mice (absolute bias over all days; threshold after day 10), and (2) mean of the seven lab\n    means (\"on average across institutions\") with the s.d. over pooled values. Reproduced when the\n    two means are within tolerance under one reading.\n\n- id: fig2s2-variability-decreases\n  statement: >-\n    Variability in performance across mice decreased with training but did not disappear; between\n    training days 15 and 40, mean easy-trial performance rose from 80.7% to 91.1% while its s.d.\n    across mice fell from 19.1% to 10.1%.\n  source: Results, Training succeeded but with different rates across mice and laboratories,\n    paragraph 3; Figure 2, figure supplement 2\n  quote: >-\n    For example, between training days 15 and 40, when the average performance on easy trials of\n    the mice increased from 80.7% to 91.1%, the variation across mice (s.d.) of performance on\n    easy trials decreased from 19.1% to 10.1%.\n  expected:\n  - quantity: mean easy-trial performance, day 15\n    value: 80.7\n    tolerance: 8.07\n    unit: \"%\"\n  - quantity: mean easy-trial performance, day 40\n    value: 91.1\n    tolerance: 9.11\n    unit: \"%\"\n  - quantity: s.d. across mice of easy-trial performance, day 15\n    value: 19.1\n    tolerance: 1.91\n    unit: \"%\"\n  - quantity: s.d. across mice of easy-trial performance, day 40\n    value: 10.1\n    tolerance: 1.01\n    unit: \"%\"\n  criterion: >-\n    Easy-trial performance per mouse and training day for the 140 proficient mice. No code prints\n    these four numbers; readings (1) the Figure 2a,d data (code figure2af: 50:50 sessions with more\n    than 100 trials, median-filtered over 3 sessions) at days 15 and 40, (2) the unfiltered\n    per-day performance binned as in suppfig_variability_over_time.py (training_day strictly\n    within 2 days of the bin centre) at days 15 and 39, the nearest bin to 40. Reproduced when the\n    mean rises and the s.d. falls, with all four values within tolerance under one reading.\n\n- id: early-sessions-predict-slow-learners\n  statement: >-\n    A Random Forests decoder applied to the change in easy-trial performance over the first five\n    sessions predicted whether a mouse would be in the bottom quartile of learning speed with 53%\n    accuracy (chance 25%), and misclassified a top-quartile mouse as bottom-quartile only 7% of the\n    time.\n  source: Results, Training succeeded but with different rates across mice and laboratories,\n    paragraph 3\n  quote: >-\n    A Random Forests decoder applied to change in performance (% correct with easy, high-contrast\n    stimuli) in the first five sessions was able to predict whether a mouse would end up in the\n    bottom quartile of learning speed (the slowest learners) with accuracy of 53% (where chance is\n    25%). Conversely, the chance of misclassifying a fast-learning, top quartile mouse as a\n    slow-learning, bottom quartile mouse, was only 7%.\n  expected:\n  - quantity: accuracy for bottom-quartile mice\n    value: 0.53\n    tolerance: 0.053\n  - quantity: top-quartile mice classified as bottom quartile\n    value: 0.07\n    tolerance: 0.007\n  depends_on:\n  - fig2g-days-to-proficiency\n  criterion: >-\n    The repository at the cited commit holds no code for this analysis and the Methods do not\n    describe it. Learning-speed quartiles from days to P1 (fig2g-days-to-proficiency). Open details\n    and the readings the text allows: features (a) the four session-to-session differences in\n    easy-trial performance over sessions 1-5, (b) the five performances; labels the four\n    quartiles (chance 25% implies four classes); scikit-learn Random Forest with default settings\n    and leave-one-out cross-validation, as for the lab classifiers in the Methods; accuracy read\n    as (i) recall of the bottom-quartile class and (ii) overall four-class accuracy. If the\n    readings disagree on whether accuracy is near 53% and well above 25%, the claim is\n    methods_underspecified.\n\n- id: fig3c-easy-errors-basic\n  statement: >-\n    At basic task proficiency, errors on easy (50% and 100%) contrasts were low, 9.5 +- 3.6%, with\n    no significant difference across laboratories.\n  source: Results, Performance in the basic task was indistinguishable across laboratories,\n    paragraph 1; Figure 3c\n  quote: >-\n    The lapse rates (i.e., the errors made in response to easy contrasts of 50% and 100%) were low\n    (9.5 ± 3.6%, Figure 3c ) with no significant difference across laboratories.\n  expected:\n  - quantity: mean error rate on easy trials, S1\n    value: 9.5\n    tolerance: 0.95\n    unit: \"%\"\n  - quantity: s.d. over mice\n    value: 3.6\n    tolerance: 0.36\n    unit: \"%\"\n  criterion: >-\n    Per mouse, 100 minus the easy-trial performance over the pooled S1 trials (code figure3cde,\n    perf_easy); mice with no valid trial duration are dropped, as in the code. Mean and s.d. over\n    mice. The lab comparison is claim fig3cde-no-lab-difference-medians.\n\n- id: fig3de-threshold-bias-basic\n  statement: >-\n    At basic task proficiency the contrast threshold was similar across laboratories at\n    14.3 +- 3.8 (s.d., n = 7 laboratories) and the response bias was small at 0.3 +- 8.4.\n  source: Results, Performance in the basic task was indistinguishable across laboratories,\n    paragraph 1; Figure 3d,e\n  quote: >-\n    The slope of the curves, which measures contrast sensitivity, was also similar across\n    laboratories, at 14.3 ± 3.8 (s.d., n = 7 laboratories, Figure 3d ). Finally, the horizontal\n    displacement of the curve, which measures response bias, was small at 0.3 ± 8.4 (s.d., n = 7,\n    Figure 3e ).\n  expected:\n  - quantity: mean contrast threshold, S1\n    value: 14.3\n    tolerance: 1.43\n    unit: \"%\"\n  - quantity: mean bias, S1\n    value: 0.3\n    tolerance: 3.2\n    unit: \"%\"\n  criterion: >-\n    Per mouse, psychometric threshold and bias fitted to the pooled S1 trials (code figure3cde).\n    The code prints the mean and s.d. over mice (thres_mean, thres_std) while the text says\n    n = 7 laboratories; readings (1) mean and s.d. over mice, (2) mean and s.d. over the seven lab\n    means. The bias tolerance is 8.4/sqrt(7), the paper's s.d. over n = 7, because 10% of a value\n    near zero is below any fitting precision.\n\n- id: fig3cde-no-lab-difference-medians\n  statement: >-\n    At basic task proficiency, easy-trial performance, contrast threshold and bias did not differ\n    in median across laboratories.\n  source: Results, Performance in the basic task was indistinguishable across laboratories,\n    paragraph 1; Figure 3c-e\n  quote: >-\n    None of these measures showed a significant difference across laboratories, either in median\n    (performance: p=0.63, threshold: p=0.81, bias: p=0.81, FDR corrected Kruskal-Wallis test)\n  statistics:\n  - about: performance on easy trials\n    test: Kruskal-Wallis test\n    p: 0.63\n    corrected: FDR\n    n: 140 mice in 7 laboratories\n  - about: contrast threshold\n    test: Kruskal-Wallis test\n    p: 0.81\n    corrected: FDR\n    n: 140 mice in 7 laboratories\n  - about: bias\n    test: Kruskal-Wallis test\n    p: 0.81\n    corrected: FDR\n    n: 140 mice in 7 laboratories\n  depends_on:\n  - fig3c-easy-errors-basic\n  - fig3de-threshold-bias-basic\n  criterion: >-\n    Per-mouse values from S1 as in fig3c-easy-errors-basic and fig3de-threshold-bias-basic.\n    Kruskal-Wallis test across the seven labs for each variable, then Benjamini-Hochberg FDR over\n    the six variables the code tests together (easy-trial performance, trial duration, trials per\n    session, threshold, bias, trials per minute; code figure3cde). Reproduced when all three\n    corrected p >= 0.05, not reproduced when any is below; the effect sizes are reported. The\n    code's switch to ANOVA for normally distributed variables is shown as a variant.\n\n- id: fig3cde-no-lab-difference-variances\n  statement: >-\n    At basic task proficiency, easy-trial performance, contrast threshold and bias did not differ\n    in variance across laboratories.\n  source: Results, Performance in the basic task was indistinguishable across laboratories,\n    paragraph 1; Figure 3c-e\n  quote: >-\n    or in variance (performance: p=0.09, threshold: p=0.57, bias: p=0.57, FDR corrected Levene's\n    test)\n  statistics:\n  - about: performance on easy trials\n    test: Levene's test\n    p: 0.09\n    corrected: FDR\n    n: 140 mice in 7 laboratories\n  - about: contrast threshold\n    test: Levene's test\n    p: 0.57\n    corrected: FDR\n    n: 140 mice in 7 laboratories\n  - about: bias\n    test: Levene's test\n    p: 0.57\n    corrected: FDR\n    n: 140 mice in 7 laboratories\n  depends_on:\n  - fig3cde-no-lab-difference-medians\n  criterion: >-\n    As fig3cde-no-lab-difference-medians, with scipy's Levene test (default, median-centred) and\n    Benjamini-Hochberg FDR over the same six variables (code figure3cde). Reproduced when all three\n    corrected p >= 0.05.\n\n- id: fig3s2a-trial-duration\n  statement: >-\n    At basic task proficiency the median trial duration (stimulus onset to feedback) was\n    468 +- 221 ms, with some differences across laboratories.\n  source: Results, Performance in the basic task was indistinguishable across laboratories,\n    paragraph 4; Figure 3, figure supplement 2a\n  quote: >-\n    The median time from stimulus onset to feedback (trial duration, a coarse measure of reaction\n    time) was 468 ± 221 ms, showing some differences across laboratories ( Figure 3—figure\n    supplement 2a , p=0.004, Kruskal-Wallis nonparametric test)\n  statistics:\n  - test: Kruskal-Wallis nonparametric test\n    p: 0.004\n    n: 140 mice in 7 laboratories\n  expected:\n  - quantity: median over mice of per-mouse median trial duration\n    value: 468\n    tolerance: 46.8\n    unit: ms\n  - quantity: s.d. over mice\n    value: 221\n    tolerance: 22.1\n    unit: ms\n  criterion: >-\n    Per mouse, the median of response time minus stimulus onset time over the pooled S1 trials,\n    no-response trials left out (code figure3cde, reaction_time); the median and s.d. over mice\n    (code rt_median, rt_std). Kruskal-Wallis across labs; the code FDR-corrects this p with the\n    other five variables, the text does not say; readings uncorrected and corrected. Reproduced\n    when the values are within tolerance and p < 0.05 under one reading.\n\n- id: fig3s2b-trials-per-session\n  statement: >-\n    At basic task proficiency mice performed 719 +- 223 trials per session; the difference across\n    laboratories was significant but only in one laboratory relative to the rest.\n  source: Results, Performance in the basic task was indistinguishable across laboratories,\n    paragraph 4; Figure 3, figure supplement 2b\n  quote: >-\n    Mice on average performed 719 ± 223 trials per session ( Figure 3—figure supplement 2b ). This\n    difference was significant (p<10 −6 , one-way ANOVA) but only in one laboratory relative to the\n    rest.\n  statistics:\n  - test: one-way ANOVA\n    p: 1.0e-6\n    p_relation: \"<\"\n    n: 140 mice in 7 laboratories\n  expected:\n  - quantity: mean trials per session, S1\n    value: 719\n    tolerance: 71.9\n    unit: trials\n  - quantity: s.d. over mice\n    value: 223\n    tolerance: 22.3\n    unit: trials\n  criterion: >-\n    Per mouse, the mean number of trials over its S1 sessions (code figure3cde, n_trials); mean\n    and s.d. over mice. One-way ANOVA across labs (code; the FDR correction it applies is a\n    variant), then Tukey post hoc tests as in the code. Reproduced when the values are within\n    tolerance, the ANOVA gives p < 1e-6, and the significant Tukey pairs all involve one lab.\n    Partially reproduced when p < 0.05 but not below 1e-6, or the pairs involve more than one lab.\n\n- id: fig3f-classifier-chance-basic\n  statement: >-\n    A Naive Bayes classifier could not identify a mouse's laboratory from its basic-task\n    performance, threshold and bias; its accuracy was 0.12 +- 0.051 against a chance level of 0.11,\n    and the 95% range of its distribution included chance.\n  source: Results, Performance in the basic task was indistinguishable across laboratories,\n    paragraph 5; Figure 3f\n  quote: >-\n    Its mean accuracy was 0.12 ± 0.051, and a 95th percentile of its distribution included the\n    chance level of 0.11 (mean of the null distribution).\n  expected:\n  - quantity: mean decoding accuracy, mouse behavior\n    value: 0.12\n    tolerance: 0.051\n  - quantity: chance level, mean of shuffled-label accuracy\n    value: 0.11\n    tolerance: 0.011\n  depends_on:\n  - fig3c-easy-errors-basic\n  - fig3de-threshold-bias-basic\n  criterion: >-\n    Lab classifier (shared definition) with scikit-learn GaussianNB on per-mouse easy-trial\n    performance, threshold and bias from S1 (code figure3f_classifier_lab_membership_basic.py).\n    The paper's test, from the code (figure3f_plot_classifier_basic.py), is that the classifier is\n    not above chance when the 2.5th percentile of its 2000 accuracies is at or below the mean\n    shuffled accuracy. Reproduced when that holds, not reproduced when the 2.5th percentile is\n    above chance. The accuracy tolerance is the paper's stated s.d. of the subsample distribution.\n\n- id: fig3f-positive-control\n  statement: >-\n    With the laboratory's time zone added as a feature, the classifier performed above chance and\n    confused labs in the same time zone.\n  source: Results, Performance in the basic task was indistinguishable across laboratories,\n    paragraph 5; Figure 3f; Figure 3, figure supplement 3b\n  quote: >-\n    If the classifier was given this variable during training and testing it performed above\n    chance ( Figure 3f , Positive control ) and the confusion matrix showed clusters of labs\n    located in the same time zone\n  data: with_labels\n  depends_on:\n  - fig3f-classifier-chance-basic\n  criterion: >-\n    As fig3f-classifier-chance-basic with the lab's time zone as a fourth feature (the code's\n    offsets, Europe 0, New York -5, Los Angeles -7, from the lab's location). Reproduced when the\n    2.5th percentile of the control accuracies is above the mean shuffled accuracy (the code also\n    computes a 0.001th percentile, sig_control, shown as a variant) and the mean confusion matrix\n    puts more off-diagonal mass on labs in the same time zone than on labs in others.\n\n- id: fig3s3-other-classifiers\n  statement: >-\n    Random Forest and Logistic Regression classifiers also failed to predict laboratory membership\n    from basic-task behavior.\n  source: Results, Performance in the basic task was indistinguishable across laboratories,\n    paragraph 5; Figure 3, figure supplement 3d-i\n  quote: >-\n    Similar results were obtained with two other classifier algorithms ( Figure 3—figure\n    supplement 3d–i ).\n  depends_on:\n  - fig3f-classifier-chance-basic\n  criterion: >-\n    As fig3f-classifier-chance-basic with scikit-learn RandomForestClassifier (100 trees,\n    random_state 424242) and LogisticRegression (solver liblinear), as in the code. Reproduced when\n    neither is above chance by the same rule.\n\n- id: fig3s1a-choice-consistency-basic\n  statement: >-\n    In the basic task, mouse choices were no more consistent within laboratories than across\n    laboratories.\n  source: Figure 3, figure supplement 1a legend\n  quote: >-\n    This averaged consistency was not significantly higher (p=0.73) than a null distribution\n    generated by randomly shuffling lab assignments between mice and computing the average\n    within-lab choice variability 10,000 times ( violin plot ). Therefore, choices were no more\n    consistent within labs than across labs.\n  statistics:\n  - test: permutation test against 10,000 shuffles of lab labels\n    p: 0.73\n    n: 140 mice in 7 laboratories\n  criterion: >-\n    Per mouse, the fraction of rightward choices at each signed contrast; per lab, the variance\n    across mice at each contrast, its mean over contrasts, and the inverse (consistency); the mean\n    over labs compared with 10,000 shuffles of lab labels across mice; p = fraction of shuffles\n    above the data (legend; code suppfig_choicevariability_withinacrosslabs.py, where 50% contrast\n    trials are dropped). Sessions per the legend, S1 (\"same data as in Figure 3\"); the code instead\n    uses the P1 day and the two days after (days_from_criterion [0, 2]), shown as a variant.\n    Reproduced when p >= 0.05.\n\n- id: fig3s1bc-choice-consistency-full\n  statement: >-\n    In the full task, neither choice fractions nor the bias shift between blocks were more\n    consistent within laboratories than expected by chance.\n  source: Figure 3, figure supplement 1b,c legend; Results, Performance in the full task was\n    indistinguishable across laboratories, paragraph 4\n  quote: >-\n    Within-lab choice consistency on the full task was not higher than expected by chance,\n    p=0.25. ... Within-lab consistency in bias shift was not higher than expected by chance\n    (p=0.31).\n  statistics:\n  - about: choice consistency, full task\n    test: permutation test against 10,000 shuffles of lab labels\n    p: 0.25\n    n: 98 mice in 7 laboratories\n  - about: bias shift consistency\n    test: permutation test against 10,000 shuffles of lab labels\n    p: 0.31\n    n: 98 mice in 7 laboratories\n  depends_on:\n  - fig3s1a-choice-consistency-basic\n  criterion: >-\n    As fig3s1a-choice-consistency-basic on S2 trials (legend \"same data as in Figure 4\"; code),\n    with consistency computed per signed contrast and block before averaging (b), and for the bias\n    shift (c) per mouse and contrast the fraction rightward in 20:80 blocks minus 80:20 blocks.\n    Reproduced when both p >= 0.05.\n\n- id: fig3s4-looser-criterion\n  statement: >-\n    With a looser proficiency criterion (80% correct on easy trials over three sessions, n = 150\n    mice), behavior was again consistent across laboratories; only the number of trials per\n    session differed slightly, and a classifier failed to identify a mouse's laboratory.\n  source: Results, Performance in the basic task was indistinguishable across laboratories,\n    paragraph 6; Figure 3, figure supplement 4\n  quote: >-\n    there was a small but significant difference in the number of trials per session across\n    laboratories. All other measured parameters were similar.\n  expected:\n    quantity: mice meeting the looser criterion\n    value: 150\n    tolerance: 15\n  depends_on:\n  - fig3cde-no-lab-difference-medians\n  - fig3f-classifier-chance-basic\n  criterion: >-\n    Sessions per the code (query_session_around_performance, suppfig_3-4a-f.py): for each mouse,\n    the first three consecutive basic sessions each with more than 80% correct on easy trials;\n    sessions with five or more signed contrasts kept; mice with three such sessions. Lab tests and\n    FDR as in fig3cde-no-lab-difference-medians on the same six variables; Naive Bayes classifier\n    on performance, threshold and bias as in fig3f-classifier-chance-basic\n    (suppfig_classifier_lab_membership_perf.py). Reproduced when trials per session has corrected\n    p < 0.05, the other five have p >= 0.05, and the classifier is not above chance.\n\n- id: fig3s5-first-full-sessions\n  statement: >-\n    In the first three sessions of the full task, bias in each block, contrast threshold in each\n    block and performance on 100% contrast trials did not vary significantly across\n    laboratories, and a classifier could not predict lab membership.\n  source: Figure 3, figure supplement 5 legend; Results, Performance in the basic task was\n    indistinguishable across laboratories, paragraph 6\n  quote: >-\n    Bias for each block prior did not vary significantly over labs (Kruskal-Wallis test, 20:80\n    blocks; p=0.96, 50:50 block; p=0.96, 80:20 block; p=0.89). ( b ) The contrast thresholds also\n    did not vary systematically over labs (Kruskal-Wallis test, 20:80 block; p=0.078, 50:50 block;\n    p=0.12, 80:20 block; p=0.17). ( c ) Performance on 100% contrast trials neither\n    (Kruskal-Wallis test, p=0.15).\n  statistics:\n  - about: bias, 20:80 blocks\n    test: Kruskal-Wallis test\n    p: 0.96\n  - about: bias, 50:50 block\n    test: Kruskal-Wallis test\n    p: 0.96\n  - about: bias, 80:20 block\n    test: Kruskal-Wallis test\n    p: 0.89\n  - about: contrast threshold, 20:80 block\n    test: Kruskal-Wallis test\n    p: 0.078\n  - about: contrast threshold, 50:50 block\n    test: Kruskal-Wallis test\n    p: 0.12\n  - about: contrast threshold, 80:20 block\n    test: Kruskal-Wallis test\n    p: 0.17\n  - about: performance on 100% contrast trials\n    test: Kruskal-Wallis test\n    p: 0.15\n  criterion: >-\n    Per mouse and block, psychometric fits to the pooled trials of the first three full-task\n    sessions, and easy-trial performance. Sessions per the legend, the first three biased sessions;\n    the code (suppfig_variability_over_labs_first_biased.py) takes the biased sessions on training\n    days 1 to 3 after P1b, and its classifier script days -1 to 3; both shown as variants.\n    Kruskal-Wallis across labs for each of the seven variables, as the legend names it (the code\n    corrects the seven p values with statsmodels' default Holm-Sidak method; variant). Naive Bayes\n    classifier on the seven variables as in fig3f-classifier-chance-basic. Reproduced when all\n    seven p >= 0.05 and the classifier is not above chance.\n\n- id: fig3s5a-prior-used-from-first-sessions\n  statement: >-\n    Mice incorporated the block priors into their choices from the first sessions of the full\n    task.\n  source: Results, Performance in the full task was indistinguishable across laboratories,\n    paragraph 2; Figure 3, figure supplement 5a\n  quote: >-\n    Mice incorporated block priors into their choices already from the first sessions in which they\n    were exposed to this full task\n  depends_on:\n  - fig3s5-first-full-sessions\n  criterion: >-\n    Per-mouse bias in 80:20 and 20:80 blocks from the sessions of fig3s5-first-full-sessions\n    (both readings). The paper reports no test for this; the full-task proficiency criterion\n    (Appendix 1, table 1d) defines use of the prior as bias[80:20] - bias[20:80] > 5. Reproduced\n    when the median over mice of that difference exceeds 5 and the Wilcoxon signed-rank test used\n    for Figure 4i (fig4i-bias-shifts-with-block) gives p < 0.05.\n\n- id: full-task-training-time\n  statement: >-\n    Mice that reached full task proficiency took 31.5 +- 16.1 days, or 20,494 +- 10,980 trials\n    (s.d., n = 98), from the start of training; the fastest took 8 days (4691 trials), the slowest\n    81 days (61,316 trials).\n  source: Results, Performance in the full task was indistinguishable across laboratories,\n    paragraph 2\n  quote: >-\n    For mice that reached full task proficiency, the average training from start to finish took\n    31.5 ± 16.1 days, or 20,494 ± 10,980 trials (s.d., n = 98). ... The fastest learner achieved\n    proficiency in 8 days (4691 trials), the slowest 81 days (61,316 trials).\n  expected:\n  - quantity: mean days to full proficiency\n    value: 31.5\n    tolerance: 3.15\n    unit: days\n  - quantity: s.d. of days\n    value: 16.1\n    tolerance: 1.61\n    unit: days\n  - quantity: mean trials to full proficiency\n    value: 20494\n    tolerance: 2049\n    unit: trials\n  - quantity: s.d. of trials\n    value: 10980\n    tolerance: 1098\n    unit: trials\n  - quantity: fastest mouse\n    value: 8\n    tolerance: 0.8\n    unit: days\n  - quantity: slowest mouse\n    value: 81\n    tolerance: 8.1\n    unit: days\n  criterion: >-\n    Per mouse reaching P2, the last training-day number and the summed trials over training days up\n    to and including the P2 day (code supp_queries.py, n_training_days = MAX(training_day),\n    total_trials = SUM(n_trials_date)); mean, s.d., minimum and maximum over mice.\n\n- id: fig4cd-biasshift-largest-at-zero\n  statement: >-\n    Block structure had the greatest effect on choices when sensory evidence was absent; the shift\n    in rightward choices between 20:80 and 80:20 blocks was highest at 0% contrast in every\n    laboratory, averaging 28.5%.\n  source: Results, Performance in the full task was indistinguishable across laboratories,\n    paragraph 2; Figure 4c-e\n  quote: >-\n    The average shift in rightward choices was invariably highest at 0% contrast, where rightward\n    choices in the two blocks differed by an average of 28.5%.\n  expected:\n    quantity: mean over mice of the bias shift at 0% contrast\n    value: 28.5\n    tolerance: 2.85\n    unit: \"%\"\n  criterion: >-\n    Per mouse, psychometric fits to the pooled S2 trials of the 20:80 and 80:20 blocks; the bias\n    shift at each signed contrast is the fitted rightward choice percentage in 20:80 minus 80:20\n    (code figure4de_psychfuncs_biased.py; the Figure 4c legend reads it from the curves). Mean over\n    mice at 0%. Reproduced when the mean is within tolerance and, in each of the seven labs, the\n    lab mean is highest at 0% contrast.\n\n- id: fig4de-biasshift-no-lab-difference\n  statement: >-\n    The bias shift at 0% contrast did not differ across laboratories more than within them.\n  source: Results, Performance in the full task was indistinguishable across laboratories,\n    paragraph 2; Figure 4d,e\n  quote: >-\n    This value did not significantly differ across laboratories any more than it differed within\n    laboratories (one-way ANOVA F(6) = 1.345, p=0.2455, Figure 4d,e ).\n  statistics:\n  - test: one-way ANOVA\n    statistic: F(6) = 1.345\n    p: 0.2455\n    n: 98 mice in 7 laboratories\n  depends_on:\n  - fig4cd-biasshift-largest-at-zero\n  criterion: >-\n    Per-mouse bias shift at 0% from fig4cd-biasshift-largest-at-zero; one-way ANOVA on lab (code,\n    statsmodels ols and type 2 anova_lm). Reproduced when p >= 0.05.\n\n- id: fig4f-threshold-unchanged-by-block\n  statement: >-\n    Block type did not significantly affect the contrast threshold.\n  source: Results, Performance in the full task was indistinguishable across laboratories,\n    paragraph 3; Figure 4f\n  quote: >-\n    Changes in block type did not significantly affect the contrast threshold (Wilcoxon\n    Signed-Rank test, p=0.85, n = 98 mice, Figure 4f ).\n  statistics:\n  - test: Wilcoxon Signed-Rank test\n    p: 0.85\n    n: 98 mice\n  criterion: >-\n    Per mouse, psychometric fits to the pooled S2 trials of 80:20 and of 20:80 blocks (code\n    figure4fghi_variability_over_labs_full.py); scipy Wilcoxon signed-rank test of threshold in\n    the two blocks. Reproduced when p >= 0.05.\n\n- id: fig4gh-lapses-change-with-block\n  statement: >-\n    Block type changed lapse rates, which were higher on the left in 20:80 blocks and higher on\n    the right in 80:20 blocks.\n  source: Results, Performance in the full task was indistinguishable across laboratories,\n    paragraph 3; Figure 4g,h\n  quote: >-\n    However, it did change the lapse rates, which were consistently higher on the left in the\n    20:80 blocks and on the right in the 80:20 blocks\n  statistics:\n  - about: left lapse, 20:80 against 80:20 blocks\n    test: Wilcoxon Signed-Rank test\n    p: 1.0e-6\n    p_relation: \"<\"\n    n: 98 mice\n  - about: right lapse, 20:80 against 80:20 blocks\n    test: Wilcoxon Signed-Rank test\n    p: 1.0e-7\n    p_relation: \"<\"\n    n: 98 mice\n  depends_on:\n  - fig4f-threshold-unchanged-by-block\n  criterion: >-\n    Fits as in fig4f-threshold-unchanged-by-block; left lapse gamma and right lapse lambda per\n    block; Wilcoxon signed-rank tests between blocks. Reproduced when the left lapse is higher in\n    20:80 and the right lapse higher in 80:20 (median of paired differences) with p < 1e-6 and\n    p < 1e-7; partially reproduced when the directions hold with p < 0.05 only.\n\n- id: fig4i-bias-shifts-with-block\n  statement: >-\n    Block type changed the overall bias consistently, with curves shifting left in 20:80 blocks\n    and right in 80:20 blocks.\n  source: Results, Performance in the full task was indistinguishable across laboratories,\n    paragraph 3; Figure 4i\n  quote: >-\n    Finally, as expected there was a highly consistent change in overall bias, with curves shifting\n    to the left in 20:80 trials and to the right in 80:20 trials\n  statistics:\n  - test: Wilcoxon Signed-Rank test\n    p: 1.0e-16\n    p_relation: \"<\"\n    n: 98 mice\n  depends_on:\n  - fig4f-threshold-unchanged-by-block\n  criterion: >-\n    Fits as in fig4f-threshold-unchanged-by-block; Wilcoxon signed-rank test of bias mu between\n    blocks. Reproduced when mu is lower in 20:80 than in 80:20 blocks (median of paired\n    differences) with p < 1e-16; partially reproduced when the direction holds with p < 0.05 only.\n\n- id: fig4fi-no-lab-difference\n  statement: >-\n    Threshold, lapses and bias in each block type showed no significant differences across\n    laboratories.\n  source: Results, Performance in the full task was indistinguishable across laboratories,\n    paragraph 2; Figure 4f-i\n  quote: >-\n    An analysis of the psychometric curves showed highly consistent effects of block type, with no\n    significant differences across laboratories ( Figure 4f–i ).\n  depends_on:\n  - fig4f-threshold-unchanged-by-block\n  criterion: >-\n    The paper gives no test; the code (figure4fghi) runs the lab test (shared definition) on each\n    of the eight per-block values (threshold, left lapse, right lapse, bias, in 80:20 and 20:80)\n    and corrects the eight p values with Benjamini-Hochberg FDR. Reproduced when all eight\n    corrected p >= 0.05.\n\n- id: fig4j-classifier-chance-full\n  statement: >-\n    A classifier trained on the full-task psychometric parameters could not predict the\n    laboratory of individual mice above chance.\n  source: Results, Performance in the full task was indistinguishable across laboratories,\n    paragraph 3; Figure 4j\n  quote: >-\n    Just as in the basic task ( Figure 3 ), a classifier trained on these variables could not\n    predict above chance the origin laboratory of individual mice above chance ( Figure 4j ).\n  depends_on:\n  - fig4f-threshold-unchanged-by-block\n  - fig3f-classifier-chance-basic\n  criterion: >-\n    Lab classifier with GaussianNB on the eight per-block values of fig4fi-no-lab-difference\n    from S2 (code figure4i_classifier_lab_membership_full.py); same rule as\n    fig3f-classifier-chance-basic. Reproduced when not above chance.\n\n- id: fig5cf-glm-weights\n  statement: >-\n    In a logistic choice model fitted to each mouse, visual weights grew with contrast to above 3\n    at 100% contrast, while weights for past choices were much smaller and positive after both\n    rewarded (basic 0.19, full 0.42) and unrewarded (basic 0.33, full 0.46) trials, indicating\n    perseverance.\n  source: Results, A probabilistic model reveals common strategies across mice and laboratories,\n    paragraph 2; Figure 5c,d,f,g\n  quote: >-\n    As expected, visual terms had large weights, which grew with contrast to reach values above 3\n    at 100% contrast. Weights for non-sensory factors were much lower ( Figure 5c,f , note\n    different scale). Weights for past choices were positive for both rewarded (basic 0.19, full\n    0.42) and unrewarded previous trials (basic 0.33, full 0.46)\n  expected:\n  - quantity: mean rewarded past-choice weight, basic task\n    value: 0.19\n    tolerance: 0.019\n  - quantity: mean rewarded past-choice weight, full task\n    value: 0.42\n    tolerance: 0.042\n  - quantity: mean unrewarded past-choice weight, basic task\n    value: 0.33\n    tolerance: 0.033\n  - quantity: mean unrewarded past-choice weight, full task\n    value: 0.46\n    tolerance: 0.046\n  criterion: >-\n    Model per Methods (Probabilistic choice model, equations 2-4): logistic regression of choice\n    (no-response trials left out) on signed indicators per nonzero contrast, the previous choice\n    split by its outcome (r and u), a constant, and in the full task the block (+1 for 20:80, -1\n    for 80:20, 0 for 50:50); design matrix by patsy, fit by statsmodels Logit.fit_regularized with\n    its defaults (code figure5_GLM_modelfit.py), per mouse and task. Sessions per the code:\n    training days P1b-2 to P1b+3, split into basic and full by protocol; the Methods say three\n    sessions per mouse, read as (b) the last three basic sessions before P1b and the first three\n    full sessions. Contrasts per the Methods include 50%; the code drops 50% trials (variant).\n    Means over mice of each weight. Reproduced when the 100% weight's mean exceeds 3 in both tasks,\n    the visual weights increase with contrast, and the four history weights are within tolerance\n    under one reading.\n\n- id: fig5dg-history-weights-higher-full\n  statement: >-\n    Previous choices influenced behavior more strongly in the full task than in the basic task,\n    after both rewarded and unrewarded trials.\n  source: Results, A probabilistic model reveals common strategies across mice and laboratories,\n    paragraph 2; Figure 5d,g\n  quote: >-\n    Indeed, previous choices more strongly influenced behavior in the full task, both after\n    rewarded (t(125) = 10.736, p<10 −6 ) and unrewarded trials (t(125) = 4.817, p<10 −6 ).\n  statistics:\n  - about: rewarded past-choice weight, full against basic\n    test: paired t-test\n    statistic: t(125) = 10.736\n    p: 1.0e-6\n    p_relation: \"<\"\n    n: 126 mice with both fits\n  - about: unrewarded past-choice weight, full against basic\n    test: paired t-test\n    statistic: t(125) = 4.817\n    p: 1.0e-6\n    p_relation: \"<\"\n    n: 126 mice with both fits\n  depends_on:\n  - fig5cf-glm-weights\n  criterion: >-\n    Per-mouse weights from fig5cf-glm-weights, mice with both fits; scipy ttest_rel of full\n    against basic, NaN omitted (code figure5_GLM_plot.py). Reproduced when both t are positive\n    with p < 0.05 (the code's num_star significance level). Note that t(125) = 4.817 gives a\n    two-sided p of about 4e-6, above the printed bound of 1e-6; the t value, not the bound, is the\n    reference.\n\n- id: fig5s2-glm-accuracy\n  statement: >-\n    The model predicted individual mouse choices well, with cross-validated accuracy of\n    81.03 +- 5.1% in the basic task and 82.1 +- 5.8% in the full task, similar across\n    laboratories; mean condition numbers were 2.4 and 3.2.\n  source: Results, A probabilistic model reveals common strategies across mice and laboratories,\n    paragraph 2; Figure 5, figure supplement 2c\n  quote: >-\n    Importantly, fitted weights and the model's predictive accuracy (unbiased: 81.03 + 5.1%,\n    biased 82.1 + 5.8%) ( Figure 5—figure supplement 2 ) were similar across laboratories,\n    suggesting an overall common strategy.\n  expected:\n  - quantity: mean cross-validated accuracy, basic task\n    value: 81.03\n    tolerance: 8.1\n    unit: \"%\"\n  - quantity: mean cross-validated accuracy, full task\n    value: 82.1\n    tolerance: 8.2\n    unit: \"%\"\n  - quantity: mean condition number, basic model\n    value: 2.4\n    tolerance: 0.24\n  - quantity: mean condition number, full model\n    value: 3.2\n    tolerance: 0.32\n  depends_on:\n  - fig5cf-glm-weights\n  criterion: >-\n    Fits as in fig5cf-glm-weights with 5-fold cross-validation, folds shuffled (the code sets no\n    seed; a standard seed is used and the spread over seeds shown). Accuracy readings: (1) the\n    Figure 5, figure supplement 2c legend, the fraction of test trials where the predicted\n    probability of the actual choice exceeds 50%; (2) the code, the mean predicted probability of\n    the actual choice. Condition number of the design matrix (numpy cond), as in the code.\n    \"Similar across laboratories\" is fig5s2-weights-similar-across-labs.\n\n- id: fig5s2-weights-similar-across-labs\n  statement: >-\n    Fitted model weights and predictive accuracy were similar across laboratories.\n  source: Results, A probabilistic model reveals common strategies across mice and laboratories,\n    paragraph 2; Figure 5, figure supplement 2\n  quote: >-\n    The model fit the mouse choices well and captured the relative importance of sensory and\n    non-sensory information across mice and laboratories\n  depends_on:\n  - fig5s2-glm-accuracy\n  criterion: >-\n    The paper reports no test; the code (figure5_GLM_plot.py) runs the lab test (shared\n    definition, uncorrected) on each weight (6.25, 12.5, 25, 100, rewarded, unrewarded, bias, and\n    block in the full task), pseudo-R2 and accuracy, per task. Reproduced when no test gives\n    p < 0.05; partially reproduced when one or two of the up to 20 tests do; the p values are\n    reported.\n\n- id: fig5s1b-win-stay-lose-switch\n  statement: >-\n    After correcting for slow fluctuations in decision bound, most mice used a win-stay\n    lose-switch strategy, in both the basic and full tasks.\n  source: Figure 5, figure supplement 1b legend; Results, A probabilistic model reveals common\n    strategies across mice and laboratories, paragraph 3\n  quote: >-\n    When taking these slow state-changes into account, the majority of animals use a win-stay\n    lose-switch strategy.\n  criterion: >-\n    Code suppfig_history_strategy.py: trials from training days P1b-2 to P1b+3, split by task;\n    signed contrasts with fewer than 100 trials over all mice dropped; per mouse, task, previous\n    choice and previous outcome a psychometric fit; the history shift = fitted rightward % at 0%\n    contrast after a right choice minus after a left choice, separately after rewarded and\n    unrewarded trials, from fits with more than 50 trials; the same with the next trial's choice\n    and outcome; corrected shift = history shift minus next-trial shift (Lak et al., 2020a).\n    Reproduced when, in each task, more than half the mice have a positive corrected post-reward\n    shift and a negative corrected post-error shift.\n\n- id: fig5s1c-updating-by-contrast\n  statement: >-\n    After rewarded trials, choice updating was largest when the previous stimulus had low contrast\n    and much smaller after high-contrast rewarded trials.\n  source: Figure 5, figure supplement 1c legend\n  quote: >-\n    After rewarded trials, choice updating is largest when the visual stimulus was highly uncertain\n    (i.e. had low contrast) but strongly diminished after more certain, rewarded trials.\n  depends_on:\n  - fig5s1b-win-stay-lose-switch\n  criterion: >-\n    Corrected updating as in fig5s1b-win-stay-lose-switch, computed separately by the previous\n    trial's absolute contrast (code suppfig_history_bycontrast.py; read only in outline here).\n    The paper reports no test. Reproduced when, after rewarded trials, the mean corrected updating\n    after 0% and 6.25% contrast exceeds that after 100% contrast in both tasks.\n\n- id: session-end-criteria\n  statement: >-\n    The session-ending criterion was not mandatory; 5,316 of 10,903 sessions ended earlier and\n    5,587 later, the latter continuing for a median of 19 +- 16 extra trials (m.a.d.).\n  source: Results, Training progression in the basic task, paragraph 2; Figure 1, figure\n    supplement 2\n  quote: >-\n    The criterion to end a session was not mandatory: some sessions were ended earlier\n    (5,316/10,903 sessions) and others ended later (5,587/10,903 sessions). The latter sessions\n    typically continued for an extra 19 ± 16 trials (median ±m.a.d., 5,587 sessions) longer.\n  expected:\n  - quantity: sessions in total\n    value: 10903\n    tolerance: 1090\n  - quantity: sessions that met an end criterion\n    value: 5587\n    tolerance: 559\n  - quantity: median extra trials after the end criterion\n    value: 19\n    tolerance: 1.9\n    unit: trials\n  - quantity: m.a.d. of extra trials\n    value: 16\n    tolerance: 1.6\n    unit: trials\n  criterion: >-\n    Code supp_queries.py: all mice that started training; per training day, an end criterion is\n    met when a session that day has an end status (from the pipeline's\n    SessionEndCriteriaImplemented table) or the day's summed session durations reach 90 minutes;\n    extra trials = trials after the end-status trial. Without an end status in the dataset, it is\n    recomputed from the three criteria of the Figure 1, figure supplement 2 legend (fewer than 400\n    trials in 45 min; over 400 trials and 90 min; over 400 trials and median reaction time over\n    the last 20 trials above 5 times the session median), taking the first trial at which one is\n    met.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000045/10.7554-elife.63711.yaml paper/10.7554-elife.63711.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

All 38 quotes check. Last pass for style rules (em dashes outside quotes, "rather", colon-space in plain scalars).

**Agent calls Bash**

```bash
cd claims/000045 && grep -n -i "rather" *.yaml; python3 - <<'E'
import yaml,re
t=open('10.7554-elife.63711.yaml').read()
d=yaml.safe_load(t)
for c in d['claims']:
    for k,v in c.items():
        if k!='quote' and isinstance(v,str) and '—' in v: print('emdash',c['id'],k)
for i,l in enumerate(t.splitlines(),1):
    s=l.strip()
    if '—' in l and not l.startswith('#'): pass
    m=re.match(r'\s*(-\s+)?[a-z_]+:\s+(?![>|"\'])(.*)',l)
    if m and ': ' in m.group(2): print('colon',i,l)
print([l for l in t.splitlines() if l.startswith('#') and '—' in l])
E
```

```
[]
```

**Agent**

I wrote `claims/000045/10.7554-elife.63711.yaml`. The quote checker reports 38 claims, 38 quotes, 26 statistical values and 0 problems. Nothing is committed.

**Text read**
- The eLife version of record (PMC8137147, from Europe PMC): main text, figure and figure-supplement legends, Methods, the Appendix 1 table, and the reviews with the authors' responses.
- The only supplementary file is eLife's transparent reporting form, which holds no results.
- The Methods send the reader to "Protocol 2" (figshare doi:10.6084/m9.figshare.11634729.v3) for the psychometric fitting and the full training criteria. That protocol is not in `paper/` and I did not read it; the code settles the fitting.
- Code: `int-brain-lab/paper-behavior` at commit `edc4531…`, the commit the paper archives. It has one script per figure panel and reads from the IBL DataJoint database.

**Claims**
- All 38 claims have a quote and none needed an `inferred` note.
- 16 claims record statistics (26 values) and 37 have criteria.
- `fig3f-positive-control` is marked `with_labels`, because the lab-to-time-zone mapping comes from the code. All other claims use `dataset`.
- The opening comment defines the shared selections, the psychometric fit, the lab test and the lab classifier, so each criterion can refer to them by name.

**Details the paper leaves open, and the readings named**
- **When a mouse became proficient:** the code reads a training-status label from the IBL database. Readings: use the dataset's own label if it has one; otherwise recompute it from the trials with the 1a criteria, or with the 1b criteria from when they were introduced. The paper says only "September 2019" for that date.
- **Counting days to proficiency:** the code counts up to and including the proficiency day in one branch and up to the day before in the other.
- **Figure 2 interquartile ranges, the absolute bias and threshold during training, and performance at days 15 and 40:** the code does not compute these numbers. Readings cover whether values are median-filtered, what "thereafter" spans, whether means pool all sessions or average lab means, and per-day versus binned values.
- **Threshold 14.3 ± 3.8 (n = 7 laboratories):** spread over mice, or over the seven lab means.
- **Basic-task choice consistency:** the legend says the Figure 3 sessions; the code uses the proficiency day and the two days after it.
- **First three full-task sessions:** the legend says the first three; the code uses days 1 to 3, or −1 to 3 in the classifier script. The code also applies a Holm-Sidak correction the legend does not mention.
- **Trial duration p = 0.004:** with or without the code's FDR correction.
- **The choice model (GLM):** the Methods say three sessions per mouse, while the code uses a window of training days from 2 before to 3 after the first full-task session. The Methods include 50% contrast and the code drops it. For accuracy, the legend counts a prediction as accurate when the actual choice gets more than 50% probability; the code averages the predicted probability. The 5-fold cross-validation has no seed.
- **Random Forest prediction of slow learners (53%, 7%):** there is no code for it and the Methods do not describe it. Readings cover the features and what "accuracy" means; the claim is blocked as `methods_underspecified` if the readings disagree.
- **Win-stay/lose-switch, updating by contrast, and session-end criteria:** these follow the code. If the dataset has no session end status, the session-end claim recomputes it from the legend's three criteria.

**Gaps and inconsistencies in the paper**
- Protocol 2 is missing, as above.
- t(125) = 4.817 gives p ≈ 4×10⁻⁶ (two-sided), which is above the printed "p<10⁻⁶". The criterion uses the t value as the reference.
- Several "similar across labs" findings report no test (Figures 4f–i and 5). Their criteria take the tests the code runs.
- The dataset's archive description cites the bioRxiv preprint of this paper.

## End of run

35 turns, 7 minutes, result: success.
