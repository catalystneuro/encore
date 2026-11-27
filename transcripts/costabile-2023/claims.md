# costabile-2023 · claims · run 45716919499

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper claims; cat claims/fouke-2025.yaml
```

```
<persisted-output>
Output too large (71.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/5482824a-ef3c-4bb6-bfcb-59ff227bafc9/tool-results/bce1kkmp1.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-19`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -60; ls paper claims
```

```
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
165:### 4. Data from outside the paper's own recordings
173:### 5. Check
186:### 6. Answer questions
199:## Author
215:### 1. Establish what can be tested
374:### 2. Check the data against its description
397:### 3. Write the entry
482:### 4. Lock, check and run
502:### 5. Record the attempt
633:### 6. Hand over for verification
671:## Repeat attempts
737:## Local and remote datasets
760:## Verifier
764:### Round 1: without the author's conclusions
789:### Round 2: with the author's conclusions
[... 347 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-19`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/datasets/costabile-2023.yaml; ls claims/costabile* 2>/dev/null; git diff --stat; git log --oneline -3; ls transcripts/costabile-2023 2>/dev/null
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.7554/elife.83289
title: Model discovery to link neural activity to behavioral tasks
datasets:
- archive: dandi
  id: '000235'
  relation: primary
- archive: dandi
  id: '000236'
  relation: primary
- archive: dandi
  id: '000237'
  relation: primary
- archive: dandi
  id: 000238
  relation: primary
 tools/runner/chain.sh | 5 ++++-
 1 file changed, 4 insertions(+), 1 deletion(-)
cc032dc Agent run on costabile-2023: author (success)
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
ls datasets 2>/dev/null | grep -E "00023[5-8]"; ls 000235 000236 000237 000238 2>/dev/null | head; grep -rl "000235\|000236" --include=*.yaml --include=*.md . 2>/dev/null | grep -v transcripts | head
```

```
./targets/description_papers.yaml
./targets/reuse.yaml
./papers/match/000238.yaml
./papers/match/000236.yaml
./papers/match/000237.yaml
./papers/match/000235.yaml
./papers/manifest.yaml
./papers/datasets/costabile-2023.yaml
```

**Agent calls Bash**

```bash
for f in papers/match/00023[5-8].yaml; do echo "== $f"; head -30 $f; done; grep -n -A8 "00023[5-8]" targets/description_papers.yaml | head -60
```

```
== papers/match/000235.yaml
# Whether each paper DANDI:000235 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: dandi
  id: '000235'
date: '2026-11-25'
papers:
- doi: 10.7554/elife.83289
  relation: IsDescribedBy
  checks:
    text: true
    title_in_text: true
    names_this: true
    names_others:
    - DANDI:000236
    - DANDI:000238
    - Zenodo:7737788
    - Zenodo:7738603
  verdict: partial
[... 128 more lines not kept]
```

**Agent**

Context is set: four dandisets (forebrain, midbrain, hindbrain imaging, plus the backfill control). Now reading the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.83289.txt",
 "offset": 30,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.83289.txt",
 "offset": 730,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.83289.txt",
 "offset": 1430,
 "limit": 650
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.83289.txt",
 "offset": 2080,
 "limit": 970
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.83289.txt",
 "offset": 2080,
 "limit": 480
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.83289.txt",
 "offset": 2560,
 "limit": 490
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -il "figure supplement" claims/*.yaml | head; grep -ih -B2 -A3 "supplement legends\|figure supplements are\|figure supplement legends" claims/*.yaml | head -40
```

```
claims/bech-2026.yaml
claims/brinke-2017.yaml
claims/bruno-2017.yaml
claims/buccino-2020.yaml
claims/claar-2023.yaml
claims/clark-2024.yaml
claims/dana-2016.yaml
claims/dimakopoulos-2022.yaml
claims/guan-2022.yaml
claims/hernandez-perez-2020.yaml
#
# Text read: the version of record (PMC5760204, Europe PMC full-text XML, flattened), with its
# Results, figure legends and figure supplement legends, Materials and methods, and Supplementary
# file 1 (elife-28132-supp1-v2.docx, the linear mixed model summaries). No PDF was supplied; no
# figure was read, and every value below is printed in the text, a legend or Supplementary file 1.
#
--
#
# Text read: the version of record, full text from Europe PMC (PMC7704107): main text, figure and
# figure-supplement legends, Materials and methods, the decision letter and author response. The
[... 30 more lines not kept]
```

**Agent**

Paper read in full. Note: this PDF-derived text has no figure-supplement legends (eLife puts those online only); the Results text still states those findings. Next, the paper's code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/haesemeyer/mine_pub && cd mine_pub && git log -1 --format="%H %cd" && ls
```

```
48c8789739121d84295a833e01ffc6326b7a6cdb Wed Apr 17 12:59:31 2024 -0400
AnatomyClustering.py
LICENSE
README.md
cnn_fit_test.py
cnn_nonlin_test.py
cnn_sta_test.py
environment_utf8.yml
example_train_trajectory.py
experiment.py
mine.py
mine_edf.py
model.py
perf_nlc_nonlin.py
plotMusall.py
processMusall.py
rspinal_build_main.py
rspinal_plot_panels.py
rwave_build_main.py
rwave_create_cmtk_commands.py
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && git log --oneline | head -20 && git checkout -q 368d75650a1de92d9dd6c7dd1aadff24be6ba379 && git log -1 --format="%H %cd" && wc -l *.py && cat README.md
```

```
48c8789 Added missing dependency
368d756 Updated README.md to reflect the publication of the manuscript in eLife
327b8a5 Fixed annoying/stupid performance bottleneck in training loop
f7a9788 BioRxiv Version 3 - ELife resubmission. Major code changes. Update of nonlinearity analysis, receptive field analysis, anatomical plotting, fit model saving
eaea5d9 BioRxiv Version 2 - added spike triggered analysis comparison.
2fe99b9 BioRxiv Version 1
368d75650a1de92d9dd6c7dd1aadff24be6ba379 Thu Jun 8 15:38:07 2023 -0400
   160 AnatomyClustering.py
   417 cnn_fit_test.py
   558 cnn_nonlin_test.py
   527 cnn_sta_test.py
   133 example_train_trajectory.py
   516 experiment.py
   250 mine.py
   231 mine_edf.py
   230 model.py
   116 perf_nlc_nonlin.py
   343 plotMusall.py
   263 processMusall.py
   294 rspinal_build_main.py
[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && cat rwave_data_fit.py
```

```
"""
Script for identifying stimulus and behavior related neurons in random-wave experiment data
"""

import model
import numpy as np
import utilities
import h5py
from scipy.ndimage import gaussian_filter1d
import os
from os import path
from experiment import Experiment2P
from numba import njit
from multiprocessing import Pool
import multiprocessing as mp
from typing import Union, Any, List, Tuple, Optional
import argparse
import pandas as pd
from sklearn.linear_model import Ridge, LinearRegression
from collections import Counter
[... 415 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && cat rwave_decompose.py && sed -n 1,230p model.py
```

```
"""
Script for performing decomposition to compute predictor contributions and nonlinearity metrics
"""

import os
from os import path

import utilities
from taylorDecomp import taylor_decompose, d2ca_dr2, complexity_scores
import h5py
import numpy as np
from multiprocessing import Pool
import multiprocessing as mp
from typing import Optional, Dict, List, Any
import model
from utilities import create_overwrite, Data
import argparse


class CheckArgs(argparse.Action):
[... 505 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && cat rwave_build_main.py
```

```
<persisted-output>
Output too large (36.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/5482824a-ef3c-4bb6-bfcb-59ff227bafc9/tool-results/bwz3qyi06.txt

Preview (first 2KB):
"""
Script to build main file of analyzed data

Intended file information:

I Fit Neurons - only for neurons which were fit by the ann
<Neuron ID> <is lm id> <ZBrain Coords> <Barcode> <Jacobian> <Jac-cluster> <Complexity> <is vglut>

II Neuron list - where neurons come from and where they are for all neurons
<Neuron ID> <Exp-ID> <plane> <ZBrain Coords> <is ann fit> <is vglut>

III Stimuli
<Exp-ID> <plane> <temperatures>

IV Behaviors
<Exp-ID> <plane> <behaviors (separated by predictor)>
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && grep -n "barcode\|Barcode\|taylor_cutoff\|1.26\|norm.ppf\|0.1\b\|n_fit\|bonferroni\|Bonferroni\|cluster\|0.8\|0.5\|sqrt" rwave_build_main.py | head -80
```

```
8:<Neuron ID> <is lm id> <ZBrain Coords> <Barcode> <Jacobian> <Jac-cluster> <Complexity> <is vglut>
80:    keys = ["neuron_id", "is_lm_fit", "zbrain_coords", "barcode", "jacobian",
81:            "jac_cluster", "complexity", "is_vglut", "zbrain_pixels"]
86:                     barcodes: np.ndarray, jacobians: np.ndarray, jac_clusters: np.ndarray, complexities: np.ndarray,
88:    if not check_arg_sizes(neuron_ids, abt_lm, centroids, barcodes, jacobians, jac_clusters, complexities, is_vglut):
94:    grp.create_dataset("barcode", data=barcodes)
96:    grp.create_dataset("jac_cluster", data=jac_clusters)
108:    keys = ["neuron_id", "experiment_id", "plane", "zbrain_coords", "is_ann_fit", "is_vglut", "zbrain_pixels"]
121:    grp.create_dataset("is_ann_fit", data=abt_ann)
141:            "ann_train_corr", "taylor_r2", "is_ann_fit", "is_lm_fit"]
161:    grp.create_dataset("is_ann_fit", data=abt_ann)
419:def build_zbrain_region_barcodes(cent_px: np.ndarray, region_names: List[str], zbr_file_path: str,
422:    For each pixel centroid get a barcode of which zbrain regions it belongs to
427:    :return: n x len(region_names) array of 0/1 barcodes indicating whether a centroid lies within a region (1) or not
635:    ann_fit_is_lm_fit = above_thresh_lm[above_thresh_ann]
636:    ann_fit_neuron_ids = np.arange(all_test_corrs.size)[above_thresh_ann]
649:    # extract barcode labels
659:    barcode = np.c_[is_nonlinear[:, None], ats_abt > 0]
666:    # perform jacobian (receptive field) based subclustering on sensory neurons - -1 will mean sensory but not
667:    # subclustered while -2 will identify neurons for which no clustering has been performed
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && sed -n 470,766p rwave_build_main.py
```

```
[5]: n long vector of glutamate channel brightness
        [6]: n long vector of linear model test correlations
        [7]: n x (n_timepointsxn_predictors) matrix of all jacobians at the data mean => linear receptive fields
        [8]: n long vector of data mean expansion scores
        [9]: n long vector of the planes each neuron came frome
        [10]: n long vector of ann training correlations
        [11]: n long vector of full taylor R2
    """
    datafile_path = path.join(base_folder, path.join(e_folder, f"{e_folder}_ANN_analysis.hdf5"))
    centroidfile_path = path.join(base_folder, path.join("CellCoordinates",
                                                         f"{e_folder.replace('_shuffle','')}_transformed_zbrain.csv"))
    glut_channel = []
    plane_ids = []
    with h5py.File(datafile_path, 'r') as dfile:
        jacobian = dfile["jacobian"][()]
        test_corrs = dfile["correlations_test"][()]
        train_corrs = dfile["correlations_trained"][()]
        lm_test_corrs = dfile["lm_correlations_test"][()]
        taylor_scores = dfile["taylor_by_pred"][()]
        linear_model_scores = dfile["linear_model_score"][()]
[... 278 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && grep -n "def \|Figure\|fig\b\|# Panel\|panel\|Panel" rwave_plot_panels.py | head -120
```

```
2:Script to plot paper figure panels from main analysis file generated via rwave_build_main.py
31:    def __init__(self, option_strings, dest, nargs=None, **kwargs):
36:    def __call__(self, parser, namespace, values: Any, option_string=None):
47:def plot_region_enrichment(c_of_interest: np.ndarray, population: np.ndarray, masks: h5py.Group,
112:    figure.savefig(path.join(plot_dir, f"ZBrainRegions_Fraction_{name}Neurons.{ext}"), dpi=300)
115:def plot_autocorrelations(in_mat: np.ndarray, lags: int, name: str) -> None:
136:    sns.despine(fig)
137:    figure.savefig(path.join(plot_dir, f"Autocorrelation_{name}.{ext}"), dpi=300)
140:def boot_complexity(all_scores: np.ndarray, subset_size: int, ci: float, n_boot: int):
161:def get_neuron_model_weights(neuron_id: int, neuronlist: DataFrame, experimentlist: DataFrame,
190:def get_neuron_model(neuron_id: int, neuronlist: DataFrame, experimentlist: DataFrame,
209:def get_drive_outputs(netw: model.ActivityPredictor, netw_j: np.ndarray, ix_i1: int, ix_i2: int, drive_min: float,
241:def plot_drive_response(drive_mat):
247:    dfig, (ax1, ax2) = pl.subplots(ncols=2)
253:    return dfig
259:    a_parser = argparse.ArgumentParser(prog="rwave_plot_panels",
260:                                       description="Will plot all RandomWave experiment figure panels")
278:    plot_dir = path.join(data_folder, f"{base_name}_figure_panels")
314:        fig = pl.figure()
318:        fig.savefig(path.join(plot_dir, f"ANN_LM_Venn.{ext}"), dpi=300)
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && sed -n 40,160p rwave_plot_panels.py && sed -n 280,760p rwave_plot_panels.py
```

```
<persisted-output>
Output too large (31.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/5482824a-ef3c-4bb6-bfcb-59ff227bafc9/tool-results/b0ijo18bl.txt

Preview (first 2KB):
            if not path.isfile(values):
                raise argparse.ArgumentError(self, f"The destination {values} is not a file")
            setattr(namespace, self.dest, values)
        else:
            raise Exception("Parser was asked to check unknown argument")


def plot_region_enrichment(c_of_interest: np.ndarray, population: np.ndarray, masks: h5py.Group,
                           outline_top: np.ndarray, outline_side: np.ndarray, name: str,
                           region_list: List[str], r_memship: np.ndarray) -> None:
    """
    For a given cluster plot its prevalence in brain regions and maps of the top-five regions
    :param c_of_interest: n_fit long boolean vector marking membership in the class of interest
    :param population: n_fit long boolean vector marking membership in all classes that are considered
    :param masks: hdf5 object that contains mask outlines
    :param outline_top: Overall brain or region outline to draw in the background, top projection
[... 22 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/5482824a-ef3c-4bb6-bfcb-59ff227bafc9/tool-results/b0ijo18bl.txt"
}
```

```
1	            if not path.isfile(values):
2	                raise argparse.ArgumentError(self, f"The destination {values} is not a file")
3	            setattr(namespace, self.dest, values)
4	        else:
5	            raise Exception("Parser was asked to check unknown argument")
6	
7	
8	def plot_region_enrichment(c_of_interest: np.ndarray, population: np.ndarray, masks: h5py.Group,
9	                           outline_top: np.ndarray, outline_side: np.ndarray, name: str,
10	                           region_list: List[str], r_memship: np.ndarray) -> None:
11	    """
12	    For a given cluster plot its prevalence in brain regions and maps of the top-five regions
13	    :param c_of_interest: n_fit long boolean vector marking membership in the class of interest
14	    :param population: n_fit long boolean vector marking membership in all classes that are considered
15	    :param masks: hdf5 object that contains mask outlines
16	    :param outline_top: Overall brain or region outline to draw in the background, top projection
17	    :param outline_side: Overall brain or region outline to draw in the background, side projection
18	    :param name: Name of the group to add to plot saves
19	    :param region_list: The list of all regions to consider
20	    :param r_memship: n_fit x len(region_list) matrix marking membership in regions for each neuron
[... 583 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && sed -n 760,1086p rwave_plot_panels.py
```

```
validation_dir = path.join(plot_dir, "validation")
        if not path.exists(validation_dir):
            os.makedirs(validation_dir)
        valid = np.logical_not(np.isnan(all_test_corrs))
        all_centroids = np.vstack(df_neuron_list["zbrain_coords"])
        centroids_bg: np.ndarray = all_centroids[valid, :]
        exp_id_bg = np.hstack(df_neuron_list["experiment_id"])[valid]
        sel_random = np.random.rand(centroids_bg.shape[0]) < 0.05
        for i in range(len(experiment_names)):
            fig = pl.figure()
            pl.scatter(centroids_bg[sel_random, 1], centroids_bg[sel_random, 2], s=2, alpha=0.1, color='k')
            pl.scatter(centroids_bg[exp_id_bg == i, 1], centroids_bg[exp_id_bg == i, 2], s=2, alpha=0.1, color='C1')
            pl.title(f"Centroids of experiment {experiment_names[i]}")
            pl.gca().invert_yaxis()
            pl.axis("equal")
            fig.savefig(path.join(validation_dir, f"{experiment_names[i]}_Neurons_Side.png"), dpi=300)
            pl.close(fig)

            fig = pl.figure()
            pl.scatter(centroids_bg[sel_random, 0], centroids_bg[sel_random, 1], s=2, alpha=0.1, color='k')
[... 308 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && grep -n "def greedy_cosine_cluster" -A60 utilities.py | head -80; grep -n "def bootstrap_fractional_r2loss" -A25 utilities.py; grep -n "def modified_gram_schmidt\|def safe_standardize" -A15 utilities.py | head -40
```

```
60:def greedy_cosine_cluster(traces: np.ndarray, c_size_cut: int, min_sim: float, min_auto_merge=0.98) -> np.ndarray:
61-    """
62-    Performs clustering similar to Bianco 2015. Clusters are formed by pairwise correlations adding highest correlated
63-    pairs into clusters.
64-    :param traces: n_samples x n_features matrix of activity data
65-    :param c_size_cut: Clusters with a size below this size will be dropped
66-    :param min_sim: The minimal cosine similarity for merging units to a cluster / other units
67-    :param min_auto_merge: The minimum correlation for merging without recalculating cluster averages (default ~10 deg)
68-    :return: n_samples long vector of cluster assignments
69-    """
70-    def make_cos_mat(t: np.ndarray):
71-        """
72-        Creates a cosine similarity matrix that can be easily processed by our algorithm
73-        Assumes that all entries in t are unit length, n_samplesxn_features
74-        """
75-        cm = t @ t.T
76-        np.fill_diagonal(cm, -np.inf)
77-        cm[np.isnan(cm)] = -np.inf
78-        return cm
79-
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && cat rspinal_plot_panels.py; grep -n "def main" -A80 rspinal_build_main.py | grep -v "^\s*$" | head -100
```

```
"""
Script to plot paper figure panels from reticulospinal backfill analysis file generated via rspinal_build_main.py
"""

import argparse
import os
from os import path
from typing import Any
import h5py
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as pl
from pandas import DataFrame

import rspinal_build_main as rbm
import upsetplot as ups


class CheckArgs(argparse.Action):
    """
[... 168 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && sed -n 237,294p rspinal_build_main.py; sed -n 1,156p rspinal_build_main.py | grep -n "seg\|mask\|rspinal" | head -30
```

```
# extract barcode labels
    # load taylor metric names from file and prepend "Nonlin"
    labels = [b"Nonlin"]
    datafile_path = path.join(folder, path.join(sub_folder_list[0], f"{sub_folder_list[0]}_ANN_analysis.hdf5"))
    with h5py.File(datafile_path, 'r') as dfile:
        taylor_names = dfile["taylor_names"][()]
        labels += [tn[0] for tn in taylor_names]

    # perform barcoding
    ats_abt = all_taylor_scores[above_thresh_ann]
    barcode = np.c_[is_nonlinear[:, None], ats_abt > 0]

    # extract names of behavior predictors from labels
    with h5py.File(datafile_path, 'r') as dfile:
        predictor_names = dfile["predictor_names"][()]
    behavior_names = predictor_names[1:]

    with h5py.File(os.path.join(folder, outfile), "w") as main_file:
        main_file.create_dataset("ANN test correlation threshold", data=c_thresh)
        main_file.create_dataset("Taylor threshold", data=sig_thresh)
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "with_labels\|with_inputs\|elsewhere" docs/protocol.md | head -30
```

```
149:     `with_labels`, `with_inputs` or `elsewhere` (step 4, and author, step
156:     rests on it. A claim on data in none of them is `data: elsewhere`, or
161:     recordings of its own, or on other data, are `data: elsewhere` when they
237:4. Decide what comes from outside the dataset. Data from elsewhere may be
246:     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
247:     `with_inputs` and `elsewhere` claims are counted apart, each group on
249:   - `with_labels` is for outside sources that only name or map codes the
279:   - `elsewhere` is for a claim whose data the dataset does not hold at
288:   - The notes of a `with_inputs` claim say which side a difference comes
299:     `data: elsewhere` instead (step 4).
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 215,
 "limit": 160
}
```

```
215	### 1. Establish what can be tested
216	
217	Do this before any analysis.
218	
219	1. List the dataset's files and read its metadata from the archive. Open a
220	   file and list everything it holds, including every column of every table.
221	2. Work out which of the subjects, sessions, conditions and measured
222	   variables that the claims file describes are in the dataset. A dataset
223	   that names a paper may hold only part of its data. Check for recordings
224	   deposited more than once (identical traces, frame counts or annotations),
225	   report each pair, and count each recording once. Where the analysis treats
226	   a unit as the same across sessions, show that it is, or state it as an
227	   assumption and also give results per session.
228	3. Choose the version to pin. Pin the version the paper cites, as the claims
229	   file gives it. If it cites none, pin the most recent published version,
230	   unless an earlier one matches the claims file's description better. Say
231	   why in the notebook's header. If versions differ in content the analysis
232	   uses, show the difference. When the version you pin is not the newest
233	   published one, look for each problem you find in the data in the newest
234	   version too, and record which versions have it (step 5, `findings`): a
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
grep -h -B3 -A3 "where:" claims/*.yaml | head -60; grep -l "kind: link" claims/*.yaml | head -3
```

```
Bowtie2 v2.5.3)68. The output showed that the highest 78% of expressed transcripts had an N50
    of 2038 bp, and that the in-total N50 of the assembled transcripts is 476 bp
  data: elsewhere
  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000
  expected:
  - quantity: transcripts in the assembly
    value: 902413
--
  quote: acute-OA samples remained near controls along PC1 (35% variance), while chronic-OA samples
    showed significant divergence along both PC1 and PC2 axes (15% variance)
  data: elsewhere
  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000
  expected:
  - quantity: variance explained by PC1
    value: 35
--
  quote: An initial analysis after batch-effect removal showed that acute-OA samples clustered closer
    to controls than chronic-OA samples
  data: elsewhere
  where: NCBI SRA BioProject PRJNA1204452; NCBI TSA GLBY01000000
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
grep -h -B12 "data: elsewhere" claims/*.yaml | grep -i -A12 "simulat\|model network\|synthetic" | grep -E "where:|data:" | sort | uniq -c | head; grep -h "where:" claims/*.yaml | grep -i "code\|github\|simulat" | head
```

```
45   data: elsewhere
      1   data: with_inputs
      1   where: Brain Image Library doi:10.35077/g.606 (reconstructions) and the Allen Cell Types model
      1   where: Figshare doi:10.6084/m9.figshare.14024495.v1.
      1   where: GitHub alejoe91/multimodalfitting at commit 24e8e61, cell_models/hay_ais/fitting
      2   where: MEArec simulations generated with github.com/cwindolf/mearec_drift_simulations.
      2   where: Not deposited; generated by the paper's simulation code, github.com/pablotano8/multi_timescale_RL
      2   where: Rabbit (Bartos et al. 2017) and mouse (Morotti et al. 2014) ventricular myocyte models in
      1   where: none deposited; a simulation, and the paper links no simulation code
  where: GitHub braingeneers/AndrewsGengVoitiukEtAl_SourceCode at commit 6865bf68cc3c8ea36a9b4f853b9248288fa1e52b,
  where: NeuN section measurements in GitHub AllenInstitute/patchseq_human_L23 data/cell_sizes at
  where: NeuN section measurements in GitHub AllenInstitute/patchseq_human_L23 data/cell_sizes at
  where: NeuN ROI measurements in GitHub AllenInstitute/patchseq_human_L23 data/cell_sizes at
  where: NeuN ROI measurements in GitHub AllenInstitute/patchseq_human_L23 data/cell_sizes at
  where: GitHub AllenInstitute/patchseq_human_L23 data/pathology_scoring.csv at commit
  where: GitHub AllenInstitute/patchseq_human_L23 data/pathology_scoring.csv at commit
  where: Morphological features in GitHub AllenInstitute/patchseq_human_L23
  where: Morphological features in GitHub AllenInstitute/patchseq_human_L23
  where: Morphological features in GitHub AllenInstitute/patchseq_human_L23
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "datasets:" -A3 claims/*.yaml | head -20
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

[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,40p claims/du-2026.yaml; python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
# Claims for Du, Lai, Hu & Ye (2026), "A Context-Conditional Audit of Trial-Pairing-Dependent
# Neural Gain in Motor-Cortex Decoding", bioRxiv doi:10.64898/2026.08.04.742876, tested on
# DANDI:001201 (LINK) and DANDI:000129 (MC_RTT).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
# protocol as stated in docs/protocol.md (version pilot-18, Reader).
#
# Text read. The bioRxiv preprint posted August 10, 2026 (a Journal of Neural Engineering
# submission), full text in paper/10.64898-2026.08.04.742876.txt: main text, figure legends,
# Tables 1 to 3, Methods, Data and Code availability. No PDF was supplied. The paper's
# Supplementary information (formal properties, complete ladder results, replacement
# diagnostics, confirmation details, nonlinear-map seeds, temporal and capacity sensitivities)
# is not under paper/ and is not in the code release; every claim below rests on numbers the
# main text or its tables state. The one main-text sentence that points to supplement values
# (replacement ranks one to five) is a claim judged by sign alone (replacement-ranks-lower).
#
# Code read. github.com/gwkuqgfkqe/neural-decoder-context-audit, tag v1.0-jne-submission,
# commit b042fbe1cda2ca5a353751c693d7c95f45de0456 (Code availability names this release). It
# holds the loaders (src/neural_evidence/link.py, mc_rtt.py, mc_maze.py), the fully nested and
# nonlinear estimators (nested_estimators.py), the synthetic generator (synthetic.py), run
# scripts for the synthetic calibration, the primary analyses, the LINK context ladder, the
[... 221 more lines not kept]
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

Code read (mine_pub at the archived commit 368d756). It settles many thresholds the Methods leave implicit. Now I'll look at the Figure 6 page to read panel F values.

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -c "
import fitz
d=fitz.open('paper/10.7554-elife.83289.pdf')
p=d[12]; p.get_pixmap(dpi=150).save('p13.png')
p=d[14]; p.get_pixmap(dpi=150).save('p15.png')
p=d[9]; p.get_pixmap(dpi=150).save('p10.png')
" && ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm && pdftoppm -f 13 -l 13 -r 130 -png paper/10.7554-elife.83289.pdf p && ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.83289.pdf",
 "pages": "13"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && pip install -q --target $TMPDIR/pylib pymupdf 2>&1 | tail -2; PYTHONPATH=$TMPDIR/pylib python3 -c "
import fitz
d=fitz.open('paper/10.7554-elife.83289.pdf')
for i in (9,12,14): d[i].get_pixmap(dpi=140).save(f'p{i+1}.png')
"; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p13.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p15.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && grep -rn "is_lm_fit\|lm_fit" --include=*.py . | grep -v "def \|create_dataset\|keys" | head -20; git log --all --oneline | head -3; git show 48c8789 --stat | head
```

```
./rwave_plot_panels.py:307:        above_threshl_lm = np.hstack(df_raw["is_lm_fit"])
./rwave_plot_panels.py:694:        fit_lm_fit = np.hstack(df_fit["is_lm_fit"])
./rwave_plot_panels.py:700:            lm_abt = fit_lm_fit[this_exp]
./rwave_build_main.py:141:            "ann_train_corr", "taylor_r2", "is_ann_fit", "is_lm_fit"]
./rwave_build_main.py:635:    ann_fit_is_lm_fit = above_thresh_lm[above_thresh_ann]
./rwave_build_main.py:718:        save_fit_neurons(main_file, ann_fit_neuron_ids, ann_fit_is_lm_fit, all_centroids[above_thresh_ann, :], barcode,
48c8789 Added missing dependency
368d756 Updated README.md to reflect the publication of the manuscript in eLife
327b8a5 Fixed annoying/stupid performance bottleneck in training loop
commit 48c8789739121d84295a833e01ffc6326b7a6cdb
Author: Martin Haesemeyer <[removed: an e-mail address]>
Date:   Wed Apr 17 12:59:31 2024 -0400

    Added missing dependency

 sta_utils.py | 52 ++++++++++++++++++++++++++++++++++++++++++++++++++++
 1 file changed, 52 insertions(+)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && sed -n 1,263p processMusall.py | grep -v "^\s*#\?\s*$" | sed -n 1,400p | grep -n "Mine(\|shift\|frame\|corr\|0\.1\|sessions\|mice\|predictor\|hz\|Hz\|history\|thresh" | head -50
```

```
35:def extract_predictor_labels(org_regdata_mat: h5py.File) -> List[str]:
39:    :return: List of all predictor labels (recLabels)
42:def collate_unique_predictors(org_regdata_mat: h5py.File) -> Tuple[np.ndarray, List[str]]:
44:    Creates an n_predictors x n_timepoints matrix of unique (non-timeshifted) predictors excluding video
47:        [0]: n_predictors x n_timepoints matrix of predictors
48:        [1]: n_predictors long list of corresponding labels
50:    # Not all predictors are used/present for all sessions. We therefore need to find the existing ones from
52:    # get all *possible* predictor labels
53:    all_labels = extract_predictor_labels(org_regdata_mat)
54:    # this indicator is 1 for all skipped *possible* predictor columns
56:    # this variable uses MATLAB 1-based indexing to index from all *possible* predictor columns into the labels
58:    # this variable contains the full set of possibly time-shifted predictors
63:    # every entry in used_idx contains the predictor label index for each row in full_r
65:    # NOTE: We need to take care of the nature of the shifts used in the fullR design matrix
67:    #   prevMod, water] the first index will give us the 0-shift predictor
69:    #   face, body] the first index will give us the analog predictor which we want to use
72:    #   the 0-shift predictor
96:    Creates a train/test data object from the predictor and response data of one session
99:        [0]: List of individual n_timepoints long predictors that apply to the entire session
101:        [2]: The names of the predictors
[... 22 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/mine_pub && grep -n "0.1\|0.8\|n_sigma\|significan\|quantile\|top\|percentile\|SpectralClustering\|n_clusters\|argmax\|> 0" plotMusall.py | head -40
```

```
126:    def cluster_jacobian_map(self, predictor_label: str, n_clusters: int, taylor_percentile=90.0) -> [np.ndarray,
129:        Cluster jacobians in pixel space for pixels that are in the top percentile of being related to the predictor
131:        :param n_clusters: The number of clusters
132:        :param taylor_percentile: The threshold which pixels have to cross for their taylor metric to be included
140:        map_valid = tay_map > np.nanpercentile(tay_map, taylor_percentile)
142:        clust_ids = utilities.spectral_cluster(jac_map, n_clusters, 0.8)
204:        pl.plot([min_c, max_c], [0.1, 0.1], 'C3--')
210:        print(f"{np.sum(all_test_corrs >= 0.1)} out of {all_test_corrs.size} components were successfully fit.")
211:        per_sess_fit = np.hstack([np.sum(stc > 0.1) / stc.size for stc in session_test_corrs])
230:        print(f"Fraction of nonlinear neurons: {np.sum(all_linapx_scores<0.8)/np.sum(np.isfinite(all_linapx_scores))}")
242:        sig = (all_taylor_raw - 3 * all_taylor_se) > 0
246:        print(f"{np.sum(all_taylor_scores[:, 22:] > 0)} significant interaction terms found")
249:        all_taylor_scores_sorted = all_taylor_scores[np.argsort(np.argmax(all_taylor_scores, 1))]
286:        # 5) Set non-significant pixels (as above) to 0
308:        axes[0].plot([0, 0], [-0.0001, 0.0003], 'k--')
Shell cwd was reset to
```

**Agent**

I have what I need from the paper and code. Writing the claims file now.

**Agent calls Bash**

```bash
grep -n "rather" paper/10.7554-elife.83289.txt | head; grep -c "‍" paper/10.7554-elife.83289.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/costabile-2023.yaml",
 "content": "# Claims for Costabile, Balakrishnan, Schwinn & Haesemeyer (2023), \"Model discovery to link neural\n# activity to behavioral tasks\", eLife 12:e83289, tested on DANDI:000235, 000236, 000237 and 000238.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-25,\n# protocol as stated in docs/protocol.md (version pilot-19, Reader).\n#\n# Text read. The version of record (eLife, published 6 June 2023), paper/10.7554-elife.83289.txt,\n# extracted from the publisher PDF (also under paper/): main text, the legends of Figures 1 to 7,\n# Table 1, Methods, Data availability. The PDF was opened only to read Figure 6 (panels F and G)\n# and Figure 7 (panel E), whose values the text does not give. eLife's figure supplements\n# (Figure 1, 2, 3, 4, 5, 6 and 7, figure supplement 1) are online only: neither their panels nor\n# their legends are in the PDF or the text. The Results state what each of them shows, and the\n# claims that rest on them (region enrichments, Figure 6, figure supplement 1D, E, G to I;\n# Figure 7, figure supplement 1A to E) are written from those Results sentences and from the\n# code that draws them. Supplementary file 1 (Z-Brain region abbreviations) and the MDAR checklist\n# are not under paper/; neither holds results.\n#\n# Code read. github.com/haesemeyer/mine_pub at commit 368d75650a1de92d9dd6c7dd1aadff24be6ba379,\n# the revision the paper archives (Software Heritage, Haesemeyer 2023). It holds the CNN\n# (model.py), the Taylor routines (taylorDecomp.py), the MINE interface (mine.py), the simulation\n# scripts for Figures 1 to 4 (cnn_fit_test.py, cnn_nonlin_test.py, cnn_sta_test.py, mine_edf.py,\n# perf_nlc_nonlin.py), the mouse analysis (processMusall.py, plotMusall.py), the zebrafish fitting\n# (rwave_data_fit.py), decomposition (rwave_decompose.py), classification (rwave_build_main.py)\n# and figure code (rwave_plot_panels.py), the backfill analysis (rspinal_build_main.py,\n# rspinal_plot_panels.py), anatomical clustering (AnatomyClustering.py) and helpers\n# (utilities.py). It reads the lab's own hdf5 experiment files (experiment.py), not the NWB files\n# on DANDI. The tail-processing code (bitbucket.org/jcostabile/2p) and CaImAn pipeline\n# (github.com/haesemeyer/imaging_pipeline) were not read.\n#\n# Zebrafish method fixed by the code where the Methods are silent (cited in the criteria as\n# \"code\"). Calcium signal, CaImAn's denoised trace (all_c), interpolated to 5 Hz, z-scored per\n# neuron and smoothed with a Gaussian of sigma 2.5 frames (rwave_data_fit.py); components with\n# average brightness below 0.1 skipped. Predictors at 5 Hz, in this order: temperature (laser\n# command converted to power and then to temperature with the heating model, alpha 0.8787 K/J,\n# beta 0.0356 per s, baseline 22 C), swim starts (bout count per bin), vigor and direction (the\n# tail metrics summed over each bout, placed at its start bin); the three behavior predictors\n# mean-subtracted, orthogonalized by modified Gram-Schmidt in that order, then each z-scored.\n# CNN as get_standard_model, 50 timepoints (10 s), 80 linear filters, two 64-unit swish layers,\n# dropout 0.5, L1 1e-3, Adam at 1e-3, batch 256, 100 epochs; trained on the first two-thirds of\n# each plane's frames and tested on the last third. Fit when the test correlation is at least\n# sqrt(0.5). Taylor metrics from expansions every 5 frames predicting 25 frames ahead, each with\n# 1000 bootstrap resamples of the timepoints; a metric counts when its bootstrap mean minus n\n# bootstrap SDs exceeds 0.1, where n is the smallest whole number of SDs whose two-sided normal\n# coverage exceeds 1 - 0.05/(number of fit neurons); a \"behavior\" metric removes all behavior\n# terms and behavior-behavior interactions together. Linearity and complexity from the expansion\n# at the mean of the training inputs, scored every 5 frames. The comparison linear model is a\n# Ridge regression (alpha 1e-4) on the four predictors shifted by 0 to 49 frames, fit on the same\n# training frames, identified at the same test correlation sqrt(0.5).\n#\n# Data the paper used, as it reports them. Zebrafish (Methods, Zebrafish experiments and\n# Processing of zebrafish data). 25 larval zebrafish, 5 to 7 days post fertilization, mitfa -/-;\n# elavl3-H2B:GCaMP6s +/-; vglut2a-mCherry, imaged on a two-photon microscope at 2.5 Hz,\n# 0.78 um per pixel, 30 planes 5 um apart per fish (750 planes). The brain was split into six\n# overlapping regions (two dorsoventral by three anterior-posterior). Each plane received 495 s of\n# a \"random wave\" heat stimulus (sine waves with periods of 13 to 200 s, 22 to 30 C) from a laser;\n# the code splits each plane's recording into three trials and rotates by one trial for the\n# control. The tail was tracked at 250 Hz; swim starts, vigor (summed absolute angular derivative\n# over a bout) and direction (summed tail-tip angle over a bout) were extracted. CaImAn found\n# 706,543 components, 432,882 after excluding dim ones. All stacks except the backfill ones were\n# registered to the Z-Brain atlas (CMTK to an internal reference, then ANTs). Excluded before\n# analysis: five fish died, eight could not be registered, six had failed tail tracking, four had\n# imaging artifacts. The paper's data list names DANDI:000235 \"Thermoregulatory Responses\n# Forebrain\", 000236 \"Midbrain\" and 000237 \"Hindbrain\", which together hold the 25 fish, and\n# 000238 \"Thermoregulatory Responses Reticulospinal system\", six fish (mitfa -/-;\n# elavl3-H2B:GCaMP6s) whose reticulospinal neurons were backfilled with Texas-Red dextran and\n# annotated by hand; these were not registered.\n#\n# Data outside the four dandisets. The simulations of Figures 1 to 4 are generated by the code\n# (data elsewhere). The mouse analysis of Figure 5 uses the widefield dataset of Musall et al.\n# 2019, CSHL repository doi:10.14224/1.38599, one session from each of 13 mice (data elsewhere).\n# The anatomical claims need the Z-Brain atlas masks (Randlett et al. 2015) and each neuron's\n# registered position; the paper deposits its processed data, which hold the Z-Brain centroids,\n# on Zenodo doi:10.5281/zenodo.7737788, and the fit CNN weights on doi:10.5281/zenodo.7738603 and\n# doi:10.5281/zenodo.7741542 (data with_inputs).\nschema_version: 2\npaper: doi:10.7554/elife.83289\nclaims:\n- id: fig1f-mine-fits-ground-truth\n  statement: On simulated ground-truth responses MINE's CNN predicts held-out data for every\n    response type, while a simple linear regression fails in most types and an expanded linear\n    model (calcium-kernel convolution and pairwise interactions) fails on the time derivative of\n    an input and on some nonlinear transformations.\n  source: Results, A model discovery approach to identify task-relevant neurons, paragraphs 2 and\n    3; Figure 1F\n  quote: a simple linear regression model fails to explain activity in most cases ... the expanded\n    linear model is poor in capturing some nonlinear transformations of predictors and fails to\n    capture responses that relate to the time derivative of an input\n  data: elsewhere\n  where: Not deposited; generated by the paper's simulation code, github.com/haesemeyer/mine_pub\n    at commit 368d756, cnn_fit_test.py\n  criterion: As in cnn_fit_test.py (Methods, Ground-truth datasets), 20 simulations per response\n    type, first two-thirds for training, last third for test, squared correlation to test data.\n    The paper gives no number for \"fails\" or \"poor\"; it is read against MINE. Reproduced when (a)\n    for every response type MINE's mean test r2 is at least that of both linear models minus the\n    SD across the 20 runs, (b) the simple model's mean r2 is below MINE's by more than 0.2 in more\n    than half of the types, and (c) the expanded model's mean r2 for dS1/dt and for at least one\n    nonlinear type (|S1| or T(S2)) is below MINE's by more than 0.2. The 0.2 margin is set here\n    and is not the paper's; results at margins 0.1 and 0.3 are shown too.\n- id: fig2bcd-complexity-scores\n  statement: Mixing a nonlinear function (tanh squared of x cubed) into a response lowers both the\n    linear and the second-order Taylor approximation scores; mixing in the derivative lowers\n    neither; mixing in a rectified version lowers the linear score but not the second-order score.\n  source: Results, MINE characterizes computational complexity, paragraph 3; Figure 2B to 2D\n  quote: Increasing the contribution of an arbitrary nonlinear function ... leads to a marked\n    decrease in both of these ... increasing the contribution of a derivative of the predictor\n    indeed does not decrease either ... When increasing the contribution of a rectified linear\n    version of the predictor, the amount of variance explained by the linear truncation drops while\n    this is not the case for the truncation after the second-order term\n  data: elsewhere\n  where: Not deposited; generated by the paper's simulation code, github.com/haesemeyer/mine_pub\n    at commit 368d756, cnn_nonlin_test.py\n  criterion: As in cnn_nonlin_test.py, linear (LAS) and second-order (SOS) scores of the\n    expansion at the data mean (Methods, equations 3 and 4) across the mixing fractions of each\n    series. Reproduced when, from the smallest to the largest mixing fraction, the tanh series\n    drops in both scores, the derivative series stays at or above 0.8 in both, and the softplus\n    series drops below 0.8 in LAS while SOS stays at or above 0.8. The 0.8 level is the paper's\n    linearity cutoff, used here also for SOS as the paper gives no level for \"drops\".\n- id: fig2e-linearity-roc\n  statement: As a classifier of nonlinear transformations, the linear approximation score ranks a\n    nonlinear transformation below a linear one in 99% of cases (AUC 0.99), and a cutoff of 0.8\n    gives false-positive and false-negative rates below 0.05.\n  source: Results, MINE characterizes computational complexity, paragraph 4; Figure 2E\n  quote: This analysis revealed that the ... value ranks a nonlinear transformation lower than a\n    linear one in 99% of cases (Figure 2E). Importantly, this metric allows disambiguating linear\n    and nonlinear processing with acceptable false-positive and false-negative rates\n  data: elsewhere\n  where: Not deposited; generated by the paper's simulation code, github.com/haesemeyer/mine_pub\n    at commit 368d756, cnn_nonlin_test.py\n  expected:\n  - quantity: ROC AUC of the linear approximation score over 500 sets of linear and nonlinear\n      transformations\n    value: 0.99\n    tolerance: 0.099\n  - quantity: false-positive and false-negative rate at a linear score cutoff of 0.8 (each below)\n    value: 0.05\n    tolerance: 0.005\n  criterion: As in cnn_nonlin_test.py (Methods, Ground-truth datasets), 500 sets of five random\n    stimuli, two linear and two nonlinear responses each. Reproduced when the AUC is within\n    tolerance and both error rates at 0.8 are at most 0.055.\n- id: fig3-receptive-fields-slow-stimuli\n  statement: With slowly varying stimuli MINE recovers a linear and a nonlinear receptive field\n    well, ordinary least-squares fits of the Volterra kernels fail, Ridge fits with high penalties\n    come close, and MINE's model predicts test data slightly better than the best Volterra fit.\n  source: Results, MINE characterizes neural receptive fields, paragraphs 2 and 3; Figure 3B, 3C,\n    3E and 3F\n  quote: Under these more naturalistic conditions, MINE still yielded well-fitting receptive fields\n    ... An ordinary regression fit of the Volterra kernels, on the other hand, failed to recover the\n    receptive fields ... for high penalties, the direct fit of the Volterra kernels yielded\n    receptive fields of almost comparable quality to MINE ... The CNN model fit by MINE also had\n    slightly higher predictive power compared to the best-fit Volterra model\n  data: elsewhere\n  where: Not deposited; generated by the paper's simulation code, github.com/haesemeyer/mine_pub\n    at commit 368d756, cnn_sta_test.py\n  criterion: As in cnn_sta_test.py, 100 simulations per filter set, the best cosine similarity of\n    the eigenvectors of Q with the three largest eigenvalues to each true filter (Methods,\n    equation 17). Reproduced, for each of the two filter sets, when MINE's median similarity\n    exceeds the OLS fit's for both filters, the best Ridge penalty's median is within 0.1 of\n    MINE's or below it, and MINE's median test correlation is at least that of every Volterra\n    fit. The 0.1 margin for \"almost comparable\" is set here.\n- id: fig3-effective-degrees-of-freedom\n  statement: Although the CNN has nearly 14,000 parameters, its effective degrees of freedom are\n    below 50, close to those of the Ridge models that recover the receptive fields.\n  source: Results, MINE characterizes neural receptive fields, paragraph 5; Figure 3, figure\n    supplement 1K\n  quote: in spite of having nearly 14,000 parameters, the effective degrees of freedom of the CNN\n    model are <50\n  data: elsewhere\n  where: Not deposited; generated by the paper's simulation code, github.com/haesemeyer/mine_pub\n    at commit 368d756, mine_edf.py\n  expected:\n  - quantity: CNN parameters for one predictor and 50 timepoints\n    value: 14000\n    tolerance: 1400\n  criterion: Effective degrees of freedom of the CNN by equation 22 (Methods), estimated by\n    simulation as in mine_edf.py. Reproduced when the estimate is below 50 and the parameter\n    count is within tolerance.\n- id: fig4-taylor-metric-ranks-predictors\n  statement: On ground-truth data the full Taylor expansion predicts the change in network output\n    well, and the Taylor metric ranks the predictors and interactions that generate a response\n    above those that do not.\n  source: Results, Taylor analysis identifies predictors driving the response, paragraphs 2 and 3;\n    Figure 4B to 4E\n  quote: Sorting individual terms by this metric consistently ranks those that we expect to\n    contribute (Figure 4C–E, red bars) higher than those that should not\n  data: elsewhere\n  where: Not deposited; generated by the paper's simulation code, github.com/haesemeyer/mine_pub\n    at commit 368d756, cnn_fit_test.py\n  criterion: Taylor metrics as in Methods, Identifying contributing predictors by Taylor\n    decomposition (equations 23 to 34), 20 simulations per response type. Reproduced when, for the\n    M2, R(S1) x R(S2) and |S1| response types, every expected term's mean metric exceeds every\n    unexpected term's mean metric.\n- id: fig5c-cortex-components-fit\n  statement: On the mouse widefield data, with a test correlation cutoff of 0.1, MINE fits more\n    than 91% of the temporal components per session on average.\n  source: Results, MINE characterizes cortical sensorimotor processing, paragraph 2; Figure 5B and 5C\n  quote: On average, this led to the identification of >91% of all components per session\n  data: elsewhere\n  where: CSHL repository doi:10.14224/1.38599 (Musall et al. 2019), one session from each of 13\n    mice; the paper's results are on Zenodo doi:10.5281/zenodo.7737788\n  expected:\n    quantity: mean over 13 sessions of the fraction of 200 components with test correlation of at\n      least 0.1\n    value: 0.91\n    tolerance: 0.091\n  criterion: As in processMusall.py and plotMusall.py, predictors shifted by 5 s, MINE with the\n    first two-thirds of each session for training. Reproduced when the mean fraction is at least\n    0.819 (the reported bound less 10%).\n- id: fig5d-cortex-largely-linear\n  statement: Only 3% of the fit cortical components have a linear approximation score below 0.8,\n    so the relationships between predictors and widefield activity are largely linear.\n  source: Results, MINE characterizes cortical sensorimotor processing, paragraph 2; Figure 5D\n  quote: only 3% of fit components have a linear approximation score <0.8\n  data: elsewhere\n  where: CSHL repository doi:10.14224/1.38599 (Musall et al. 2019), one session from each of 13\n    mice\n  depends_on:\n  - fig5c-cortex-components-fit\n  expected:\n    quantity: fraction of fit components with a linear approximation score below 0.8\n    value: 0.03\n    tolerance: 0.005\n  criterion: The tolerance is the rounding of a whole percent (2.5 to 3.5%), wider than 10%.\n    Fraction over all fit components of all 13 sessions, as plotMusall.py prints it.\n- id: fig5e-uninstructed-movements-dominate\n  statement: Across sessions, uninstructed movements have the largest Taylor metric in more than\n    half of the fit cortical components.\n  source: Results, MINE characterizes cortical sensorimotor processing, paragraph 3; Figure 5E\n  quote: uninstructed movements appear overrepresented sporting the largest Taylor metric in more\n    than half of the fit components\n  data: elsewhere\n  where: CSHL repository doi:10.14224/1.38599 (Musall et al. 2019), one session from each of 13\n    mice\n  depends_on:\n  - fig5c-cortex-components-fit\n  criterion: Taylor metrics significant when the bootstrap mean minus 3 standard errors exceeds 0\n    (plotMusall.py; the zebrafish cutoff of 0.1 is not used for the mouse data in the code).\n    Uninstructed movements are the predictors Figure 5E groups so (Piezo, Whisk, Nose, Pupil,\n    Face, Body). Reproduced when the predictor with the largest significant metric is one of them\n    in more than half of the fit components.\n- id: fig5fh-cortex-maps\n  statement: Per-pixel Taylor metrics place visual stimuli in visual cortex with a left-right\n    asymmetry, whisking in regions matching Musall et al., and instructed left and right grabs in\n    motor cortex with a left-right asymmetry, though not every session shows clear grab regions.\n  source: Results, MINE characterizes cortical sensorimotor processing, paragraph 3; Figure 5F to\n    5H and Figure 5, figure supplement 1\n  quote: visual stimuli are shown to contribute most strongly to responses in visual cortical areas\n    with the expected left–right asymmetry ... instructed left and right grab events largely\n    contribute to motor cortical regions, again with the expected left–right asymmetry\n  data: elsewhere\n  where: CSHL repository doi:10.14224/1.38599 (Musall et al. 2019), with the dataset's Allen CCF\n    alignment\n  depends_on:\n  - fig5c-cortex-components-fit\n  criterion: For the example session (the one plotMusall.py draws), maps of lVisStim minus\n    rVisStim and of lGrab minus rGrab per-pixel Taylor metrics. Reproduced when the visual\n    difference map has its positive and negative extremes in opposite posterior (visual) cortices\n    and the grab difference map has them in opposite anterior (motor) cortices. Which hemisphere\n    carries which sign is read from the figure, contralateral to the stimulus or limb.\n- id: fig5i-cortex-receptive-fields\n  statement: Receptive fields of visual pixels are biphasic and lie entirely in the past, with\n    excitation stronger than inhibition, while grab receptive fields are sharper and extend up to\n    100 ms into the future, indicating preparatory activity.\n  source: Results, MINE characterizes cortical sensorimotor processing, paragraph 4; Figure 5I\n  quote: The visual receptive fields have essentially zero weight after the current time ... the\n    grab-related receptive fields contain coefficients different from baseline for up to 100 ms\n    into the future\n  data: elsewhere\n  where: CSHL repository doi:10.14224/1.38599 (Musall et al. 2019)\n  depends_on:\n  - fig5fh-cortex-maps\n  criterion: As in plotMusall.py (cluster_jacobian_map), pixels in the top 10% of the Taylor\n    metric for the visual or grab predictors, receptive fields split into two clusters by\n    spectral clustering. Reproduced when the excitatory visual cluster averages have weights\n    after time 0 below 10% of their peak, and the excitatory grab cluster averages depart from\n    baseline (by more than 10% of their peak) at a lag after 0 of at most 0.2 s. The 10% levels\n    are set here; the paper reads the figure by eye.\n- id: data-zebrafish-coverage\n  statement: The zebrafish dataset holds 750 imaging planes from 25 larvae, with 706,543 CaImAn\n    components of which 432,882 pass the brightness criterion.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 3; Methods,\n    Processing of zebrafish data, paragraph 2\n  quote: We imaged a total of 750 planes across 25 larval zebrafish ... The number of analyzed\n    components was thereby reduced from 706,543 to 432,882\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  expected:\n  - quantity: larvae\n    value: 25\n    tolerance: 0\n  - quantity: imaging planes\n    value: 750\n    tolerance: 0\n  - quantity: CaImAn components before the brightness criterion\n    value: 706543\n    tolerance: 70654\n  - quantity: components analyzed (average brightness at least 0.1)\n    value: 432882\n    tolerance: 43288\n  criterion: Counts over the three dandisets together. Fish and planes are counts of recordings\n    and must match exactly. The component counts depend on the segmentation the dandisets hold;\n    if they hold CaImAn's components, they are counted as stored.\n- id: figs6-shuffle-enrichment\n  statement: At the fit cutoff, real data yield 93 times more fit neurons than cyclically rotated\n    control data.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 4; Figure 6,\n    figure supplement 1D\n  quote: Using cyclic permutations of the data as a control revealed that this cutoff corresponds to\n    a 93-fold enrichment over control data\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  expected:\n    quantity: neurons with test correlation of at least sqrt(0.5), real over rotated\n    value: 93\n    tolerance: 9.3\n  criterion: Calcium traces rotated forward by a third of each plane's length with wrap-around\n    (Methods; rwave_data_fit.py, shuffle), CNNs fit to the rotated data as to the real data, ratio\n    of the counts at the cutoff (rwave_plot_panels.py).\n- id: fig6d-mine-identifies-more-than-lm\n  statement: Of the 432,882 active neurons, about 42,000 are identified by MINE or by the linear\n    comparison model; 40% only by MINE, 54% by both and 6% only by the linear model.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 5; Figure 6D\n  quote: At the designated cutoff, a total of ... neurons were identified using either MINE or\n    regression. 40% of these neurons, however, were exclusively identified by MINE\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  expected:\n  - quantity: neurons identified by MINE or the linear model\n    value: 42229\n    tolerance: 4223\n  - quantity: fraction identified only by MINE\n    value: 0.40\n    tolerance: 0.04\n  - quantity: fraction identified by both\n    value: 0.54\n    tolerance: 0.054\n  - quantity: fraction identified only by the linear model\n    value: 0.06\n    tolerance: 0.006\n  criterion: Both models fit per neuron as described in the opening comment (rwave_data_fit.py),\n    each counted as identifying a neuron at a test correlation of at least sqrt(0.5); fractions of\n    the union, as the Venn diagram in rwave_plot_panels.py.\n- id: figs6-mine-more-at-every-cutoff\n  statement: MINE identifies more neurons than the linear model whatever test-correlation cutoff\n    is used.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 5; Figure 6,\n    figure supplement 1E\n  quote: In fact, MINE consistently identifies more neurons regardless of the cutoff imposed on test\n    data\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig6d-mine-identifies-more-than-lm\n  criterion: Counts of neurons with test correlation at or above each cutoff from 0 to 1 in steps\n    of 0.01, as in rwave_plot_panels.py. Reproduced when MINE's count is at least the linear\n    model's at every cutoff where either count is above zero.\n- id: figs6-train-test-uncorrelated\n  statement: Because stimulus and behavior are random, test and training data are largely\n    uncorrelated.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 4; Figure 6,\n    figure supplement 1B\n  quote: due to the random nature of both our stimulus and the elicited behavior, test and training\n    data were largely uncorrelated\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  criterion: As rwave_plot_panels.py, each plane's temperature, swim-start, vigor and direction\n    traces split into three equal trials, and the Pearson correlation of every pair of trials.\n    The paper gives no level for \"largely uncorrelated\"; the readings are (a) the median of each\n    predictor's inter-trial correlations below 0.2 in absolute value, (b) below 0.1. Reproduced\n    when all four predictors meet a reading; the distributions are shown.\n- id: fig6e-functional-classes\n  statement: Taylor analysis sorts the MINE-fit neurons into 33 functional classes, each found in\n    several fish.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 6; Figure 6E\n  quote: In total, we identified 33 functional neuron classes all of which were identified across\n    multiple fish\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig6d-mine-identifies-more-than-lm\n  expected:\n    quantity: functional classes\n    value: 33\n    tolerance: 3.3\n  criterion: Each fit neuron gets six flags, nonlinear (linear approximation score below 0.8) and\n    a significant Taylor metric (above 0.1 at the corrected level, Methods) for temperature, the\n    combined behavior term, swim start, vigor and direction; interaction terms are left out\n    (Results). A class is a combination of flags held by at least 10 neurons (the UpSet plot's\n    minimum in rwave_plot_panels.py). The significance level is open between two readings, (a)\n    the code's whole number of bootstrap SDs (5 for about 40,000 fit neurons) and (b) the exact\n    one-sided normal quantile for p = 0.05 divided by the number of fit neurons. Classes with no\n    significant predictor (the gray bars) are counted, as the figure does; the count without them\n    is shown. Reproduced when the count is within tolerance under a reading and every class\n    counted is present in at least two fish.\n- id: fig6e-mixed-selectivity-exists\n  statement: Several functional classes have mixed selectivity, their activity driven jointly by\n    the temperature stimulus and behavior.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 6; Figure 6E\n    (blue bars)\n  quote: Across the brain, we identified multiple functional classes of neurons with mixed\n    selectivity, that is, neurons with activity jointly driven by the temperature stimulus and\n    behavioral outputs\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig6e-functional-classes\n  criterion: Classes as in fig6e-functional-classes. Reproduced when at least two classes with at\n    least 10 neurons each have both the temperature flag and a behavior flag, each found in more\n    than one fish.\n- id: fig6g-linear-model-bias\n  statement: Of the neuron types MINE identifies, the linear comparison model finds behavior\n    neurons most often and stimulus and mixed-selectivity neurons least often, a bias towards\n    behavior-related, low-complexity activity.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 6; Figure 6G\n  quote: Analyzing the success of the linear comparison model according to functional class revealed\n    a bias toward the identification of behavior-related activity ... Stimulus or mixed-selectivity\n    neurons, on the other hand, were underrepresented in the pool identified by the linear model\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig6d-mine-identifies-more-than-lm\n  - fig6e-functional-classes\n  criterion: As rwave_plot_panels.py, for each fish the fraction of MINE-fit neurons of a type that\n    the linear model also identifies, averaged over the 25 fish (bootstrap standard errors).\n    Types are all fit neurons, nonlinear, complexity 2, stimulus (temperature only, no behavior\n    and no interaction term), behavior (behavior only, no temperature and no interaction), mixed\n    (temperature and behavior, or any significant interaction, as the code defines it). The\n    figure shows about 0.51 for all, 0.58 for behavior and 0.26 to 0.28 for stimulus, mixed and\n    complexity 2 (read from the PDF). Reproduced when behavior has the highest mean fraction and\n    stimulus and mixed are each below the all-neuron fraction by more than their bootstrap\n    standard errors.\n- id: fig6f-reticulospinal-behavior\n  statement: Reticulospinal neurons labeled by spinal backfills in six fish are classified by MINE\n    as driven by behavioral features in the vast majority.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 6; Figure 6F\n  quote: As a control, we labeled reticulospinal neurons in six fish via spinal backfills and as\n    expected the vast majority of these neurons were classified by MINE to be driven by behavioral\n    features\n  datasets:\n  - \"000238\"\n  expected:\n    quantity: fraction of fit reticulospinal neurons in the behavior-only class\n    value: 0.86\n    tolerance: 0.086\n  criterion: The value is read from the bars of Figure 6F (about 390 behavior, 45 temperature, 10\n    mixed and 8 with neither); no sentence gives it. Fitting and Taylor analysis as for the\n    whole-brain data, with the Bonferroni count over the fit neurons of the six backfill fish\n    (rspinal_build_main.py). A neuron is reticulospinal when at least half of it lies in the\n    hand-annotated backfill mask (code). Behavior is any significant behavior metric (the Results);\n    rspinal_plot_panels.py, through an overwritten line, counts only the combined behavior term or\n    swim start, and is shown as a variant. Reproduced when the behavior-only fraction is within\n    tolerance under the Results reading, or at least 0.75 of the classified neurons are\n    behavior-driven (behavior-only or mixed) and behavior-only is the largest class.\n- id: figs6-stimulus-neuron-regions\n  statement: Stimulus-driven neurons are enriched in telencephalic regions, the habenula and the\n    interpeduncular nucleus, and temperature-sensitive neurons are found in a medial zone of the\n    olfactory epithelium.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 7; Figure 6,\n    figure supplement 1G and 1I\n  quote: We found stimulus-driven neurons to be enriched in telencephalic regions, as well as the\n    habenula and its output region the interpeduncular nucleus ... with the exception of the\n    olfactory epithelium where we found temperature-sensitive neurons in a medial zone\n  data: with_inputs\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig6e-functional-classes\n  criterion: Needs each neuron's Z-Brain region (Z-Brain masks, Randlett et al. 2015, and the\n    registered centroids on Zenodo doi:10.5281/zenodo.7737788, or a re-registration). Enrichment\n    as Methods, Processing of zebrafish data, paragraph 6, with the code's details\n    (plot_region_enrichment) of regions holding at least 50 neurons of the population, 5000\n    simulated draws at the overall fraction, enriched when the region's fraction is above the\n    97.5th percentile. The population is open, (a) stimulus, behavior and mixed neurons together\n    (Methods) or (b) all fit neurons (code). Reproduced when, under one reading, at least one\n    telencephalic region (pallium, subpallium or telencephalic migrated area 4), the habenula and\n    the interpeduncular nucleus are enriched for stimulus neurons, and the olfactory epithelium\n    mask holds stimulus neurons.\n- id: figs6-behavior-neuron-regions\n  statement: Behavior-driven neurons are enriched in hindbrain regions and in the nucleus of the\n    medial longitudinal fasciculus.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 7; Figure 6,\n    figure supplement 1H; Figure 6H\n  quote: As expected, behavior-driven neurons are enriched in hindbrain regions and the midbrain\n    nucleus of the medial longitudinal fasciculus\n  data: with_inputs\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig6e-functional-classes\n  criterion: Enrichment as in figs6-stimulus-neuron-regions, for behavior neurons. Reproduced when,\n    under one reading, the nucMLF and at least half of the rhombencephalic regions tested are\n    enriched.\n- id: figs6-mixed-neuron-regions\n  statement: Mixed-selectivity neurons are enriched in telencephalic area M4 and the\n    interpeduncular nucleus, shared with stimulus neurons, and strongly in the superior raphe, the\n    caudal hypothalamus and the torus longitudinalis.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 7; Figure 6,\n    figure supplement 1I\n  quote: Mixed-selectivity neurons occupy some regions shared with stimulus-driven neurons such as\n    telencephalic area M4 and the interpeduncular nucleus but are also strongly enriched in the\n    raphe superior as well as the caudal hypothalamus and the torus longitudinalis\n  data: with_inputs\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig6e-functional-classes\n  criterion: Enrichment as in figs6-stimulus-neuron-regions, for mixed neurons. Reproduced when,\n    under one reading, at least four of the five named regions are enriched; partially reproduced\n    for two or three.\n- id: fig7a-behavior-feature-regions\n  statement: Swim-start neurons are enriched in the dorsal thalamus and medial hindbrain, vigor\n    neurons in the ventral thalamus, forebrain and locus coeruleus, and turning neurons in mid- and\n    hindbrain regions.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 8 and\n    Computational features of thermoregulatory circuits, paragraph 1; Figure 7A and Figure 7,\n    figure supplement 1A to 1C\n  quote: Swim start neurons are enriched in the dorsal thalamus as well as the medial hindbrain,\n    while the ventral thalamus, the forebrain, and the locus coeruleus preferentially encode swim\n    speed ... encode turning are enriched in mid- and hindbrain regions\n  data: with_inputs\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig6e-functional-classes\n  criterion: Neurons with a significant vigor, direction or swim-start metric, made exclusive as\n    the code does (vigor first, then direction, then swim start); the population is the three\n    together (Methods, and code). Enrichment otherwise as in figs6-stimulus-neuron-regions.\n    \"Medial hindbrain\" and \"forebrain\" name no Z-Brain region; they are read as any rhombomere 1\n    to 7 or medial hindbrain stripe, and any telencephalic region. Reproduced when at least five\n    of the seven named sites are enriched for their type (dorsal thalamus and medial hindbrain\n    for swim start; ventral thalamus, forebrain and locus coeruleus for vigor; a mesencephalic\n    and a rhombencephalic region for direction); partially reproduced for three or four.\n- id: fig7b-receptive-field-clusters\n  statement: Clustering the temperature receptive fields of stimulus-driven neurons by cosine\n    similarity yields 15 clusters, each with neurons from at least 15 fish.\n  source: Results, Computational features of thermoregulatory circuits, paragraph 2; Figure 7B\n  quote: A clustering approach based on the cosine similarity of receptive fields (see ‘Methods’)\n    resulted in 15 clusters. For each of these clusters, neurons came from at least 15 fish across\n    our dataset\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig6e-functional-classes\n  expected:\n  - quantity: receptive field clusters\n    value: 15\n    tolerance: 1.5\n  - quantity: fish contributing to the smallest-fish cluster (at least)\n    value: 15\n    tolerance: 1.5\n  criterion: Receptive field is the temperature part of the Jacobian at the data mean (Methods,\n    equation 35) of pure stimulus neurons, clustered by the greedy cosine method of Methods,\n    Clustering of neurons according to receptive field, at a similarity of 0.8, with clusters below\n    25 neurons dropped (rwave_build_main.py; the Methods give no size cut). Reproduced when the\n    count is within tolerance and every cluster has neurons from at least 14 fish.\n- id: fig7c-receptive-field-types\n  statement: Receptive field clusters differ in the temperature feature they extract and in where\n    they lie; clusters responding to slow heating and to slow cooling are enriched in the\n    forebrain, a cluster computing the rate of heating over short timescales lies almost only in\n    the hindbrain, and a cluster with only negative weights (excited by cold) lies mainly in hind-\n    and midbrain.\n  source: Results, Computational features of thermoregulatory circuits, paragraph 2; Figure 7B and\n    7C\n  quote: Clusters 1 and 4 are enriched in the forebrain (Figure 7B, right), and their receptive\n    fields suggest that they are most responsive to heating and cooling stimuli over slow\n    timescales ... Cluster 3, on the other hand, computes the rate of heating over shorter\n    timescales (Figure 7C) and is almost exclusively localized to the hindbrain ... Cluster 12\n    represents neurons that are excited by colder temperatures since the receptive field\n    exclusively has negative coefficients\n  data: with_inputs\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig7b-receptive-field-clusters\n  expected:\n  - quantity: neurons in the slow-heating cluster (cluster 1)\n    value: 1691\n    tolerance: 169\n  - quantity: neurons in the slow-cooling cluster (cluster 4)\n    value: 1675\n    tolerance: 168\n  - quantity: neurons in the fast heating-rate cluster (cluster 3)\n    value: 362\n    tolerance: 36\n  - quantity: neurons in the all-negative cluster (cluster 12)\n    value: 112\n    tolerance: 11\n  criterion: Cluster numbers depend on the order of the greedy method, so clusters are matched to\n    the paper's by the shape of their normalized mean receptive field (Figure 7C), one zero\n    crossing rising to positive weights near time 0 (1), one zero crossing falling to negative\n    weights (4), two zero crossings with a positive peak near time 0 (3), no crossing and all\n    negative (12). Fraction of each cluster in telencephalon, diencephalon, mesencephalon and\n    rhombencephalon as in rwave_plot_panels.py. Reproduced when the four shapes are found, the\n    two slow clusters have their largest telencephalic fraction among the four, the fast heating\n    cluster has more than 0.8 of its neurons in the rhombencephalon (\"almost exclusively\", level\n    set here), and the cold cluster has more than half in mesencephalon and rhombencephalon\n    together; the sizes are compared with the expected values.\n- id: fig7d-mixed-integration-modes\n  statement: Nonlinear neurons driven by both swim starts and temperature integrate the two in\n    diverse ways, some adding behavioral and thermosensory drive and others gated, their sensory\n    responsiveness scaled by swim drive.\n  source: Results, Computational features of thermoregulatory circuits, paragraph 3; Figure 7D and\n    Figure 7, figure supplement 1E\n  quote: Clustering neurons according to these response landscapes ... revealed diverse modes of\n    integration across 10 clusters. Some neurons appear to add behavioral inputs linearly with\n    thermosensory inputs ... Other neurons, however, show gating\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig6e-functional-classes\n  criterion: Neurons with significant temperature and swim-start metrics and classed nonlinear;\n    response landscapes from unit-norm receptive fields scaled from -10 to 10 in 100 steps, fed to\n    each neuron's CNN; similarity the maximum of the normalized 2D circular cross-correlation;\n    spectral clustering into 10 clusters (Methods; rwave_plot_panels.py). The number 10 is set in\n    the code, not found. The paper defines additive and gating by eye. Read here as, for each\n    cluster's mean landscape (and its exemplar, as in the figure), the response range across\n    sensory drive at swim drive +5 divided by that at -5; near 1 with a shifted curve is\n    additive, far from 1 is gating. Levels open, (a) additive within 0.8 to 1.25 and gating\n    outside 0.5 to 2, (b) within 0.67 to 1.5 and outside 0.33 to 3. Reproduced when under a\n    reading at least one cluster is additive and at least one is gating.\n- id: fig7e-complexity-by-cluster\n  statement: Computational complexity maps onto receptive field type; three clusters have lower\n    average complexity than expected, and one (cluster 6) has an average complexity above 1.\n  source: Results, Computational features of thermoregulatory circuits, paragraph 4; Figure 7E\n  quote: averaging the complexity score for different receptive field clusters reveals that three of\n    these clusters have lower complexity than expected ... One cluster (cluster 6) had an average\n    complexity score >1\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig7b-receptive-field-clusters\n  expected:\n  - quantity: clusters with average complexity below the bootstrap 95% interval\n    value: 3\n    tolerance: 0\n  - quantity: clusters with average complexity above 1\n    value: 1\n    tolerance: 0\n  criterion: Complexity 0 when the linear score is at least 0.8, 1 when it is below 0.8 and the\n    second-order score is at least 0.5, 2 otherwise (Methods). Interval per cluster as\n    boot_complexity in rwave_plot_panels.py, 1000 draws with replacement of the cluster's size\n    from all stimulus neurons' scores, 2.5th to 97.5th percentile. Counts are small integers, so\n    no tolerance; reproduced when exactly three clusters fall below their interval and exactly\n    one has a mean above 1 (the figure shows clusters 1, 2 and 9 below and cluster 6 at about\n    1.4); partially reproduced when two or four fall below and one or two exceed 1.\n- id: fig7f-complexity-anatomy\n  statement: Complexity classes are generally intermingled but regionalized; complexity 2 neurons\n    lie medially in rhombomeres 1 and 2, in the habenula and in the dorsal telencephalon, while\n    linear neurons are enriched in the posterior and medial hindbrain.\n  source: Results, Computational features of thermoregulatory circuits, paragraph 4; Figure 7F\n  quote: Within the hindbrain, neurons of complexity class 2 are found medially in rhombomeres 1 and\n    2 ... Prominent clusters of complexity 2 neurons can also be found in the habenula and dorsal\n    telencephalon ... Linear neurons, on the other hand, are enriched in the posterior and medial\n    hindbrain\n  data: with_inputs\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig7e-complexity-by-cluster\n  criterion: The paper shows this by anatomical clustering (5 um radius, connected components,\n    clusters of 10 or more plotted) and reports no test. Read here with the enrichment method of\n    figs6-stimulus-neuron-regions over all fit neurons, complexity 2 against the rest and\n    complexity 0 against the rest. Reproduced when complexity 2 is enriched in rhombomere 1 or 2,\n    the habenula and the pallium, and complexity 0 is enriched in at least one of rhombomeres 5 to\n    7; the anatomical cluster maps are shown.\n- id: lm-recovers-fewer-clusters\n  statement: The linear model identifies neurons in every receptive field cluster, but fewer than\n    five in four clusters, and clustering only the neurons it identifies recovers 4 of the 15\n    receptive field clusters.\n  source: Discussion, Novel insight into biological circuits, paragraph 4; Figure 7, figure\n    supplement 1D\n  quote: in four clusters the linear model identified less than five neurons ... applying our\n    clustering on the neurons identified by the linear model only recovers 4 instead of the 15\n    unique receptive field clusters that are obtained with MINE\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig7b-receptive-field-clusters\n  expected:\n  - quantity: receptive field clusters with fewer than five linear-model neurons\n    value: 4\n    tolerance: 0\n  - quantity: clusters recovered when clustering only linear-model neurons\n    value: 4\n    tolerance: 0\n  criterion: The code at the cited commit does not hold this analysis. For the first count, the\n    neurons of each MINE cluster that the linear model also identifies. For the second, the\n    readings are (a) the greedy clustering (similarity 0.8, minimum 25 neurons) run on the MINE\n    receptive fields of the stimulus neurons the linear model also identifies, counting clusters\n    that match a MINE cluster at cosine similarity of at least 0.8, and (b) the number of MINE\n    clusters holding at least 25 linear-model neurons, the size cut of the clustering. Reproduced\n    when the first count is exactly 4 and the second is 4 under one reading; partially reproduced\n    when one of the two holds or the counts are 3 or 5.\n- id: temperature-nonlinear-behavior-linear\n  statement: Most temperature-driven neurons are classified as nonlinear while most behavior-driven\n    neurons are classified as linear.\n  source: Discussion, Characterizing the model implemented by the CNN, paragraph 2\n  quote: In our zebrafish dataset, the majority of temperature-driven neurons were classified as\n    nonlinear while most behavior-driven neurons were classified as linear\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig6e-functional-classes\n  criterion: Temperature-driven read as (a) pure stimulus neurons or (b) all neurons with a\n    significant temperature metric; behavior-driven as (a) pure behavior neurons or (b) all with a\n    significant behavior metric. Reproduced when, under a reading, more than half of the\n    temperature-driven neurons have a linear score below 0.8 and more than half of the\n    behavior-driven neurons have one of at least 0.8.\n- id: interaction-terms-small\n  statement: Interaction terms between predictors have very small Taylor metrics in the zebrafish\n    data, so there is little evidence of multiplicative interactions.\n  source: Results, Functional characterization of thermoregulatory circuits, paragraph 6; Discussion,\n    Characterizing the model implemented by the CNN, paragraph 1\n  quote: Since interaction terms had very small Taylor metrics, we ignored them for neuron\n    classification purposes ... we found little evidence of multiplicative interactions in the\n    biological data\n  datasets:\n  - \"000235\"\n  - \"000236\"\n  - \"000237\"\n  depends_on:\n  - fig6d-mine-identifies-more-than-lm\n  criterion: The paper gives no number. Over MINE-fit neurons, the Taylor metrics of the six\n    pairwise interaction terms. Reproduced when the median of every interaction metric is below\n    the 0.1 cutoff for a contributing predictor (Methods) and below the median of the\n    temperature and the combined behavior metrics, and fewer than 5% of fit neurons have any\n    interaction metric significant at the corrected level; the 5% level is set here and the\n    fraction is reported.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/costabile-2023.yaml paper/10.7554-elife.83289.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/costabile-2023.yaml",
 "old_string": "  quote: In total, we identified 33 functional neuron classes all of which were identified across\n    multiple fish",
 "new_string": "  quote: In total, we identified 33 functional neuron classes all of which were identified ... across\n    multiple fish (Figure 6E)"
}
```

```
The file claims/costabile-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/costabile-2023.yaml paper/10.7554-elife.83289.txt; grep -n "—\|rather" claims/costabile-2023.yaml; python3 - <<'EOF'
import yaml,re
d=yaml.safe_load(open('claims/costabile-2023.yaml'))
print(len(d['claims']), sum('criterion' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('expected' in c for c in d['claims']))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -nE "^\s{4,}[^-#].*: " claims/costabile-2023.yaml | head; grep -nE "^  [a-z_]+: .*: " claims/costabile-2023.yaml | head; git status --short
```

```
131:    value: 0.99
132:    tolerance: 0.099
134:    value: 0.05
135:    tolerance: 0.005
171:    value: 14000
172:    tolerance: 1400
200:    quantity: mean over 13 sessions of the fraction of 200 components with test correlation of at
202:    value: 0.91
203:    tolerance: 0.091
218:    quantity: fraction of fit components with a linear approximation score below 0.8
 M tools/runner/chain.sh
?? .bash_profile
?? .bashrc
?? .gitconfig
?? .idea
?? .mcp.json
?? .profile
?? .ripgreprc
?? .vscode
?? .zprofile
[... 3 more lines not kept]
```

**Agent**

I wrote `claims/costabile-2023.yaml`. The quote checker passes with 32 claims, 32 quotes and 0 problems. Nothing is committed.

**What I read**
- **Paper:** the eLife version of record (6 June 2023), taken from the publisher PDF: main text, the legends of Figures 1 to 7, Table 1, Methods and Data availability. I opened the PDF only to read values from Figure 6F, 6G and 7E.
- **Code:** github.com/haesemeyer/mine_pub at commit 368d756, the revision the paper archives. It fixes many details the Methods leave out, such as the calcium smoothing, the order the behavior variables are orthogonalized in, how many bootstrap SDs count as significant, the 25-neuron minimum cluster size, the 10-neuron minimum class size, and the region-enrichment rules.
- **Not read:** the tail-tracking repository and the CaImAn pipeline repository.

**What is missing from the paper**
eLife's figure supplements are online only, so neither their panels nor their legends are in the PDF or the text. The claims that rest on them (the region enrichments in Figure 6, figure supplement 1D, E, G to I, and Figure 7, figure supplement 1A to E) are written from the Results sentences and the code that draws those panels. I went ahead rather than stopping because the Results state each of these findings. If you count the figure-supplement legends as part of a supplement the results rest on, these legends should be supplied.

**Claims**
- **Counts:** 32 claims, all with quotes and criteria; 13 have expected values. None has statistics, because the paper reports no tests for its findings. The Bonferroni-corrected Taylor significance is a selection threshold, so it is not recorded as a result.
- **Simulations (Figures 1 to 4):** 6 claims. These are `data: elsewhere`, generated by the paper's code.
- **Mouse data (Figure 5):** 5 claims. These are `data: elsewhere`, on the Musall et al. dataset (CSHL doi:10.14224/1.38599).
- **Zebrafish:** 20 claims rest on 000235, 000236 and 000237 together; 6 of them are `with_inputs` because they need Z-Brain registration (the atlas masks, plus the registered centroids on Zenodo 7737788).
- **Backfill control (Figure 6F):** 1 claim on 000238.

**Details the paper leaves open, and the readings named**
- **Taylor significance level** (affects the 33 classes and everything that depends on them): the code's whole 5 SDs, or the exact one-sided normal quantile for 0.05 divided by the number of fit neurons.
- **Whether the 33 classes include classes with no significant predictor** (the gray bars): counted with them, as the figure does, and also shown without.
- **Population for region enrichment:** stimulus, behavior and mixed neurons together (Methods), or all fit neurons (code).
- **Figure 6F behavior class:** any significant behavior metric (Results), or the code's narrower set, which comes from an overwritten line; the code's version is a variant.
- **Clustering only the linear model's neurons ("4 of 15 clusters"):** the code doesn't contain this analysis. Readings are re-clustering those neurons, or counting MINE clusters that hold at least 25 of them.
- **"Largely uncorrelated" train and test data:** the median inter-trial correlation below 0.2, or below 0.1.
- **Additive versus gated mixed neurons:** two sets of thresholds on the ratio of response ranges.
- **Temperature- and behavior-driven neurons:** pure-type neurons, or any neuron with that significant metric.
- **Thresholds I set myself:** some vague words ("fails", "almost comparable", "almost exclusively", "very small") have no number in the paper, so I chose a level and say in each criterion that it is mine.

**Values read from figures rather than text**
- The Figure 6F fraction (about 0.86 behavior-only), noted in the claim.
- The Figure 6G and 7E bars, used only to describe what the figure shows.
- The cluster sizes in Figure 7C, which the extracted text also printed.

The working tree also has untracked dotfiles, `.idea`, `.vscode` and `scripts/` that I didn't create.

## End of run

51 turns, 7 minutes, $3.92 at API prices, result: success.
