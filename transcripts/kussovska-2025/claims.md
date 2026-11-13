# kussovska-2025 · claims · run 42756878666

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "Reader" docs/protocol.md | head; ls paper/ | grep -i kussov; ls claims | head -50; wc -l docs/protocol.md
```

Result: not kept, because it reads the paper's text.

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

**Agent calls Bash**

```bash
cd  ls paper/ | head; ls paper | grep -i kuss; ls paper/kussovska-2025* 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls -la paper/; wc -l paper/*.txt; head -30 paper/*.txt; cat claims/fouke-2025.yaml | head -150; cat papers/datasets/kussovska-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.10.31.684900.txt",
 "offset": 30,
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.10.31.684900.txt",
 "offset": 329,
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.10.31.684900.txt",
 "offset": 329,
 "limit": 150
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.10.31.684900.txt",
 "offset": 479,
 "limit": 250
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -l "Extended Data" claims/*.yaml | head; grep -h -i "extended data.*not\|supplement.*not in\|not in the text" claims/*.yaml | head -20; ls tools; git log --oneline -3 -- claims/kyzar* ; ls claims | grep -i -E "kyzar|daume|kamin"
```

```
claims/azcorra-2023.yaml
claims/berg-2020.yaml
claims/bouabid-2026.yaml
claims/calvigioni-2023.yaml
claims/carcea-2021.yaml
claims/chantranupong-2023.yaml
claims/cody-2024.yaml
claims/daume-2024-phase.yaml
claims/duszkiewicz-2024.yaml
claims/economo-2018.yaml
# legends, Extended Data figure legends and the legends of Extended Data Tables 1 and 2. Not in
    hotspots of Extended Data Figure 2b and 2c are not computed.
    date). The Extended Data Fig. 4a legend measures Ach as the mean minimum z-scored signal, not
    entry), the Extended Data Fig. 11d schematic not being legible in the text. The legend prints
    Supplementary Data 1, which is not in paper/; the claims record the legends' P < 0.05 only.
# in the text read. The Supporting Information was not in the text read: Figures S1 to S9,
  source: Methods 2.8; Figure S2 (not in the text read)
  source: Results 3.1, paragraph 1; Discussion, paragraph 2; Figure S3 (not in the text read)
  source: Results 3.1, paragraph 1; Figure S4A to S4C (not in the text read)
  source: Results 3.1, paragraph 3; Figure S5A and S5B (not in the text read)
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p claims/kyzar-2024.yaml; sed -n 1,60p tools/claims_check.py
```

```
# Claims for Kyzar, Kaminski, Brzezicka, Reed, Chung, Mamelak & Rutishauser (2024), Sci Data 11, 89,
# on dandiset 000469.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23, protocol
# as stated in docs/protocol.md.
#
# Text read: the version of record, as served by Europe PMC (PMC10796636), full text with Methods,
# Technical Validation, figure legends and Tables 1 to 3. The paper is a data descriptor and has
# no supplement. Its Methods are said to be abbreviated from refs 15 and 20 (Kaminski et al. 2017,
# Nat Neurosci; Kaminski et al. 2020, Neuron); those papers were not used here, as the protocol
# takes methods from this paper and the code it links.
#
# Code read: github.com/rutishauserlab/workingmem-release-NWB, branch main at commit f8594e0
# (2024-01-22). Its code is identical to tag v1.0.0 (commit 4a98f46, 2023-07-18); only README.md
# and CITATION.cff differ. A commit of 2024-01-12 (7d7b00f) that rewrote the selectivity code
# for another dataset was reverted the same day (3098793) and is not used. The repository holds
# MATLAB scripts. NWB_SB_import_main.m runs the analysis; NWB_calcSelective_SB.m and
# NWB_calcSelective_SC.m classify concept, maintenance and probe cells; NWB_QA_graphs.m computes
# the behaviour and the spike sorting metrics of Figs 1c,d and 3; NWB_SB_plotCell_Sternberg.m and
# NWB_SB_plotCell_Screening.m list the example units of Figs 4 and 5.
# Where the code and the Methods disagree, the Methods give the main criterion and the code's
[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/dariakussovska/heterogeneitywm && cd heterogeneitywm && git log -3 --format='%H %ad %s' && find . -type f -not -path './.git/*' | head -100
```

```
dabe2cef40532c658d4d3a450ce90322e385dc0c Tue Oct 27 11:42:52 2026 -0400 Update revised_main_4f-k,6c,d.py
802f67d514bfff300ab30c33f644d2f0c37cd596 Fri Oct 23 12:56:11 2026 -0400 Revise README for cell analysis documentation
448738ff3a7fef7fa8d6fa7f41e5a52956e9c9a5 Fri Oct 23 12:54:49 2026 -0400 Update Mean_ACG.m
./07_spectral_clustering.py
./02_trial_info.py
./08_dpca_matrices.py
./data/new_trial_final.xlsx
./data/all_neuron_brain_regions_cleaned.xlsx
./data/electrodes_plotting/CIT168_T1w_1mm_MNI.nii
./data/electrodes_plotting/electrodes_locations.mat
./data/electrodes_plotting/plot_electrodes.m
./data/cell_analysis/compute_acg.m
./data/cell_analysis/Mean_ACG.m
./data/cell_analysis/decay_constant_change.xlsx
./data/cell_analysis/Cell_metrics.xlsx
./data/cell_analysis/validation_data.xlsx
./data/cell_analysis/spikes_struct.mat
./data/cell_analysis/calc_ACG_metrics.m
./data/cell_analysis/fit_ACG.m
./data/cell_analysis/README.md
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/heterogeneitywm && git log --format='%h %ad %s' --date=short | awk '{print $2}' | sort | uniq -c | head -40; git log --format='%h %ad %s' --date=short --before=2025-11-02 | head -5; wc -l *.py */*.py data/cell_analysis/*.m | sort -n | tail -50; cat README.md | head -80
```

```
1 2025-09-23
     55 2025-09-24
     22 2025-09-25
      9 2025-09-26
     16 2025-09-27
     36 2025-09-28
     18 2025-09-29
      2 2025-10-03
     20 2025-10-08
     39 2025-10-09
      2 2025-10-10
     13 2025-10-13
      4 2025-10-14
    143 2025-10-21
     74 2025-10-22
     34 2025-10-23
      1 2025-10-26
      4 2025-11-15
      1 2026-02-17
     16 2026-06-03
[... 151 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q heterogeneitywm hwm-preprint && cd hwm-preprint && git checkout -q 5144fe8 && git log -1 --format='%H %ad' && ls -R | grep -v xlsx | head -80 && pwd
```

```
5144fe80876d14e8aacb4044977c3474c454f14b Sun Oct 26 20:56:07 2025 -0400
.:
01_data_extraction.py
01_task
02_psth_decoding
02_trial_info.py
03_dpca
03_standardization.py
04_bursting
04_concept_cells.py
05_cell_analysis
05_merge_data.py
06_add_category.py
06_cell_specific
07_spectral_clustering.py
08_dpca_matrices.py
DOCUMENTATION.md
README.md
data
requirements.txt
[... 59 more lines not kept]
```

**Agent calls Agent**

```json
{
 "description": "Read code part A: pipeline, task",
 "subagent_type": "general-purpose",
 "prompt": "You are helping write a reproduction claims file for a paper. Read code only; do NOT download or open any dataset/NWB files and do not open the .xlsx/.mat data files except to list their names. Do not write any files.\n\nPaper text: paper/10.1101-2025.10.31.684900.txt (Methods at lines ~414-506; Results ~291-398). Code checkout (commit 5144fe8, 2025-10-26): /tmp/claude-1001/hwm-preprint\n\nRead these files fully: 01_data_extraction.py, 02_trial_info.py, 03_standardization.py, 04_concept_cells.py, 05_merge_data.py, 06_add_category.py, 08_dpca_matrices.py, all of 01_task/*.py, README.md, DOCUMENTATION.md.\n\nReport, with file:line citations for every point, concisely (bullet points):\n1. Which DANDI version and which files/NWB fields are read; how epochs (fixation, encoding 1-3, maintenance, probe) are defined in time; any trial or neuron exclusions; how the 75/96 matched trial sets are built (data/new_trial_info.xlsx etc.), and whether that selection can be reproduced from the dataset alone or only from the shipped xlsx.\n2. Concept cells (04_concept_cells.py): window, which trials, the test exactly (bootstrap? permutation? iterations, two-sided p, threshold), random seed; any differences from the Methods text (\"two top stimulus identities ... bootstrap 1000 ... P<0.05\").\n3. Fig 1c (accuracy by load, Wilcoxon rank-sum P=0.027), 1d (RT), supp_1a: exact computation, per-patient or per-session, which test; and the behaviour numbers (accuracy 88.73% ± 1.25%, RT 1.06 ± 0.28 s; RT in vs out of memory permutation P=0.001; correct vs incorrect P=0.002) — where/how are they computed, if at all.\n4. Fig 1e,f GLM: the predictor (load / RT), which trials (load-matched 96? all? correct only?), epoch window, the spike count, Poisson GLM implementation, permutation (within participant? iterations), per-neuron significance rule, group-level count test, multiple-comparison correction (which family), region definitions. Note any disagreement with Methods lines 437-442.\n5. Fig 1g, 1i,j: what is computed.\n6. 08_dpca_matrices.py: how the dPCA matrices are built (trials, binning, smoothing sigma in ms, z-scoring, truncation).\n7. Anything in the code that disagrees with the Methods, and any hard-coded numbers or random seeds.\nKeep the report under ~1200 words."
}
```

**Subagent prompt**

You are helping write a reproduction claims file for a paper. Read code only; do NOT download or open any dataset/NWB files and do not open the .xlsx/.mat data files except to list their names. Do not write any files.

Paper text: paper/10.1101-2025.10.31.684900.txt (Methods at lines ~414-506; Results ~291-398). Code checkout (commit 5144fe8, 2025-10-26): /tmp/claude-1001/hwm-preprint

Read these files fully: 01_data_extraction.py, 02_trial_info.py, 03_standardization.py, 04_concept_cells.py, 05_merge_data.py, 06_add_category.py, 08_dpca_matrices.py, all of 01_task/*.py, README.md, DOCUMENTATION.md.

Report, with file:line citations for every point, concisely (bullet points):
1. Which DANDI version and which files/NWB fields are read; how epochs (fixation, encoding 1-3, maintenance, probe) are defined in time; any trial or neuron exclusions; how the 75/96 matched trial sets are built (data/new_trial_info.xlsx etc.), and whether that selection can be reproduced from the dataset alone or only from the shipped xlsx.
2. Concept cells (04_concept_cells.py): window, which trials, the test exactly (bootstrap? permutation? iterations, two-sided p, threshold), random seed; any differences from the Methods text ("two top stimulus identities ... bootstrap 1000 ... P<0.05").
3. Fig 1c (accuracy by load, Wilcoxon rank-sum P=0.027), 1d (RT), supp_1a: exact computation, per-patient or per-session, which test; and the behaviour numbers (accuracy 88.73% ± 1.25%, RT 1.06 ± 0.28 s; RT in vs out of memory permutation P=0.001; correct vs incorrect P=0.002) — where/how are they computed, if at all.
4. Fig 1e,f GLM: the predictor (load / RT), which trials (load-matched 96? all? correct only?), epoch window, the spike count, Poisson GLM implementation, permutation (within participant? iterations), per-neuron significance rule, group-level count test, multiple-comparison correction (which family), region definitions. Note any disagreement with Methods lines 437-442.
5. Fig 1g, 1i,j: what is computed.
6. 08_dpca_matrices.py: how the dPCA matrices are built (trials, binning, smoothing sigma in ms, z-scoring, truncation).
7. Anything in the code that disagrees with the Methods, and any hard-coded numbers or random seeds.
Keep the report under ~1200 words.

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint && git log -1 --format='%h %ad' && find . -path ./.git -prune -o -type f -print | head -100 && wc -l *.py 01_task/*.py README.md DOCUMENTATION.md
```

```
5144fe8 Sun Oct 26 20:56:07 2025 -0400
./07_spectral_clustering.py
./02_trial_info.py
./08_dpca_matrices.py
./data/new_trial_final.xlsx
./data/all_neuron_brain_regions_cleaned.xlsx
./data/electrodes_plotting/electrodes_locations.mat
./data/electrodes_plotting/plot_electrodes.m
./data/cell_analysis/Mean_ACG.m
./data/cell_analysis/decay_constant_change.xlsx
./data/cell_analysis/Cell_metrics.xlsx
./data/cell_analysis/validation_data.xlsx
./data/cell_analysis/spikes_struct.mat
./data/cell_analysis/calc_ACG_metrics.m
./data/cell_analysis/fit_ACG.m
./data/cell_analysis/normalize_acg_to_unit.m
./data/cell_analysis/acg.mat
./data/new_trial_info.xlsx
./05_cell_analysis/main_5d-h.py
./05_cell_analysis/main_5a,b.py
[... 52 more lines not kept]
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint && cat -n README.md DOCUMENTATION.md
```

````
<persisted-output>
Output too large (41.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/e576dfb8-0163-451a-9e9a-e3fa5978057c/tool-results/b5l8p3hqq.txt

Preview (first 2KB):
     1	# Neural-heterogeneity-shapes-the-temporal-structure-of-human-working-memory
     2	
     3	This is a repository that includes all the codes necessary to create all main and supplementary figures of the Kussovska et al., 2026 paper. 
     4	There are some notebooks for pre-processing steps, but we have also provided extracted and cleaned data for analysis as part of this repo. 
     5	
     6	# Installing requirements and downloading the dataset
     7	
     8	Clone this repository on your local computer or server by running this line of code in your terminal: 
     9	
    10	```
    11	git clone https://github.com/dariakussovska/heterogeneity_wm/
    12	cd heterogeneity_wm
    13	```
    14	This will create a folder "heterogeneity_wm" which will have all the necessary files and python codes to generate all the figures in the Kussovska et al., 2026 paper. 
    15	
    16	Install the dataset (from https://www.nature.com/articles/s41597-024-02943-8) and put it in a folder on your computer. There are multiple ways of installing this dataset, all of them detailed in the github repository of the Kyzar et al., 2024 paper. 
[... 24 more lines not kept]
````

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint && cat -n 01_data_extraction.py 02_trial_info.py
```

```
1	import pandas as pd
     2	from pynwb import NWBHDF5IO
     3	import matplotlib.pyplot as plt 
     4	import re
     5	import numpy as np
     6	import os
     7	from typing import Tuple, Dict, List
     8	
     9	def extract_subject_id(file_path: str) -> int:
    10	    """Extracts the subject_id from the file path."""
    11	    match = re.search(r'sub-(\d+)', file_path)
    12	    if match:
    13	        return int(match.group(1))
    14	    else:
    15	        raise ValueError(f"Subject ID not found in file path: {file_path}")
    16	
    17	def read_nwb_file(filepath: str):
    18	    """Read NWB file with proper error handling."""
    19	    io = NWBHDF5IO(filepath, mode='r', load_namespaces=True)
    20	    nwbfile = io.read()
[... 547 more lines not kept]
```

**Agent calls Agent**

```json
{
 "description": "Read code part B: decoding, dPCA",
 "subagent_type": "general-purpose",
 "prompt": "You are helping write a reproduction claims file for a paper. Read code only; do NOT download or open any dataset/NWB files and do not open the .xlsx/.mat/.npy data files. Do not write any files.\n\nPaper text: paper/10.1101-2025.10.31.684900.txt (Methods ~lines 437-460; Results ~312-342; Fig 2 and 3 legends lines ~322 and ~340). Code checkout (commit 5144fe8, 2025-10-26): /tmp/claude-1001/hwm-preprint\n\nRead fully: all of 02_psth_decoding/*.py, all of 03_dpca/*.py, and 08_dpca_matrices.py and 03_standardization.py as needed for context.\n\nReport, with file:line citations for every point, concisely (bullet points):\n1. Fig 2c population PSTH: which trials (load 1, preferred vs nonpreferred defined how), normalization, bins, smoothing, the bootstrap test per bin and its correction.\n2. Fig 2d cross-temporal decoding: classifier (sklearn SVC linear? C?), features, z-scoring, window 250 ms step 100 ms, time span, LOOCV, which trials (75 matched? load 1?), labels (which stimulus: first encoding image?), pseudo-population construction (how trials from different participants are aligned into one trial axis), binomial test, FDR, cluster-duration permutation (iterations), seeds.\n3. Fig 2e maintenance decoding AMY / MTL: requirement of >=3 concept cells per participant, which participants, within-participant or pooled, bin 1 s step 250 ms?, features, labels (last image for load 2/3?), LOOCV, permutation test (1000), how accuracy 35.56% / 32.13% would be computed (averaged over participants? over bins?), seeds.\n4. Fig 2f bin-width decoding (250/500/750/1000 ms: 40.00, 56.67, 66.67, 80.00%): number of trials (30? accuracies are multiples of 1/30 or 3.33%), the window placement within maintenance, the pairwise comparison test between bin widths (P=0.026 etc.), FDR family, permutation count, seeds.\n5. dPCA (Fig 3a-h): package (dPCA from Kobak?), regularization, 30 trials 6 per identity, 2 ms bins, Gaussian sigma (60 ms vs \"alpha = 60; bin width = 120 ms\" in Methods), z-scoring, number of components used for distance, how separability score per iteration is computed (mean of pairwise distances? over time?), 100 iterations, Kruskal-Wallis + Dunn with FDR (which package), early/late halves definition, seeds.\n6. Anything in the code that disagrees with the Methods; any hard-coded numbers, random seeds, or preselected trial lists.\nKeep the report under ~1300 words."
}
```

**Subagent prompt**

You are helping write a reproduction claims file for a paper. Read code only; do NOT download or open any dataset/NWB files and do not open the .xlsx/.mat/.npy data files. Do not write any files.

Paper text: paper/10.1101-2025.10.31.684900.txt (Methods ~lines 437-460; Results ~312-342; Fig 2 and 3 legends lines ~322 and ~340). Code checkout (commit 5144fe8, 2025-10-26): /tmp/claude-1001/hwm-preprint

Read fully: all of 02_psth_decoding/*.py, all of 03_dpca/*.py, and 08_dpca_matrices.py and 03_standardization.py as needed for context.

Report, with file:line citations for every point, concisely (bullet points):
1. Fig 2c population PSTH: which trials (load 1, preferred vs nonpreferred defined how), normalization, bins, smoothing, the bootstrap test per bin and its correction.
2. Fig 2d cross-temporal decoding: classifier (sklearn SVC linear? C?), features, z-scoring, window 250 ms step 100 ms, time span, LOOCV, which trials (75 matched? load 1?), labels (which stimulus: first encoding image?), pseudo-population construction (how trials from different participants are aligned into one trial axis), binomial test, FDR, cluster-duration permutation (iterations), seeds.
3. Fig 2e maintenance decoding AMY / MTL: requirement of >=3 concept cells per participant, which participants, within-participant or pooled, bin 1 s step 250 ms?, features, labels (last image for load 2/3?), LOOCV, permutation test (1000), how accuracy 35.56% / 32.13% would be computed (averaged over participants? over bins?), seeds.
4. Fig 2f bin-width decoding (250/500/750/1000 ms: 40.00, 56.67, 66.67, 80.00%): number of trials (30? accuracies are multiples of 1/30 or 3.33%), the window placement within maintenance, the pairwise comparison test between bin widths (P=0.026 etc.), FDR family, permutation count, seeds.
5. dPCA (Fig 3a-h): package (dPCA from Kobak?), regularization, 30 trials 6 per identity, 2 ms bins, Gaussian sigma (60 ms vs "alpha = 60; bin width = 120 ms" in Methods), z-scoring, number of components used for distance, how separability score per iteration is computed (mean of pairwise distances? over time?), 100 iterations, Kruskal-Wallis + Dunn with FDR (which package), early/late halves definition, seeds.
6. Anything in the code that disagrees with the Methods; any hard-coded numbers, random seeds, or preselected trial lists.
Keep the report under ~1300 words.

**Subagent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/e576dfb8-0163-451a-9e9a-e3fa5978057c/tool-results/b5l8p3hqq.txt"
}
```

````
1	     1	# Neural-heterogeneity-shapes-the-temporal-structure-of-human-working-memory
2	     2	
3	     3	This is a repository that includes all the codes necessary to create all main and supplementary figures of the Kussovska et al., 2026 paper. 
4	     4	There are some notebooks for pre-processing steps, but we have also provided extracted and cleaned data for analysis as part of this repo. 
5	     5	
6	     6	# Installing requirements and downloading the dataset
7	     7	
8	     8	Clone this repository on your local computer or server by running this line of code in your terminal: 
9	     9	
10	    10	```
11	    11	git clone https://github.com/dariakussovska/heterogeneity_wm/
12	    12	cd heterogeneity_wm
13	    13	```
14	    14	This will create a folder "heterogeneity_wm" which will have all the necessary files and python codes to generate all the figures in the Kussovska et al., 2026 paper. 
15	    15	
16	    16	Install the dataset (from https://www.nature.com/articles/s41597-024-02943-8) and put it in a folder on your computer. There are multiple ways of installing this dataset, all of them detailed in the github repository of the Kyzar et al., 2024 paper. 
17	    17	
18	    18	One way is to use dandi (install with conda or pip), which is added to the requirements.txt file 
19	    19	
20	    20	```
[... 367 more lines not kept]
````

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint; git log -1 --format='%h %ad'; find . -path ./.git -prune -o -type f -name '*.py' -print | sort; wc -l 02_psth_decoding/*.py 03_dpca/*.py; find . -name '08_dpca_matrices.py' -o -name '03_standardization.py'
```

```
5144fe8 Sun Oct 26 20:56:07 2025 -0400
./01_data_extraction.py
./01_task/main_1c.py
./01_task/main_1d.py
./01_task/main_1e,f.py
./01_task/main_1g.py
./01_task/main_1i,j.py
./01_task/supp_1a.py
./02_psth_decoding/main_2a,b,5i,j.py
./02_psth_decoding/main_2c,5k,l,supp_1b,c.py
./02_psth_decoding/main_2d,supp_1d,e.py
./02_psth_decoding/main_2e,supp_1f.py
./02_psth_decoding/main_2f,supp_1g.py
./02_trial_info.py
./03_dpca/main_3a-c.py
./03_dpca/main_3d,supp_2a,b,i.py
./03_dpca/main_3e-g,supp_2j,k.py
./03_dpca/main_3h,supp_2c,d,l.py
./03_dpca/supp_2e-h.py
./03_standardization.py
[... 31 more lines not kept]
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint && cat -n 03_standardization.py; echo =====; cat -n 04_concept_cells.py
```

```
1	import pandas as pd
     2	import ast
     3	import os
     4	
     5	BASE_DIR = './'
     6	DATA_DIR = './data/'
     7	
     8	filtered_files = {
     9	    'Encoding1': os.path.join(BASE_DIR, 'all_spike_rate_data_encoding1.xlsx'),
    10	    'Encoding2': os.path.join(BASE_DIR, 'all_spike_rate_data_encoding2.xlsx'),
    11	    'Encoding3': os.path.join(BASE_DIR, 'all_spike_rate_data_encoding3.xlsx'),
    12	    'Delay': os.path.join(BASE_DIR, 'all_spike_rate_data_delay.xlsx'),
    13	    'Probe': os.path.join(BASE_DIR, 'all_spike_rate_data_probe.xlsx')
    14	}
    15	
    16	def load_enc1_start_times(enc1_path):
    17	    enc1_df = pd.read_excel(enc1_path)
    18	    return enc1_df[['subject_id', 'trial_id', 'start_time']].drop_duplicates().rename(columns={'start_time': 'start_time_enc1'})
    19	
    20	enc1_start_times = load_enc1_start_times(filtered_files['Encoding1'])
[... 503 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/02_psth_decoding/main_2c,5k,l,supp_1b,c.py"
}
```

```
1	import pandas as pd
2	import numpy as np
3	from ast import literal_eval
4	import matplotlib.pyplot as plt
5	
6	# === Load Data ===
7	fixation_data = pd.read_excel('../clean_data/cleaned_Fixation.xlsx')
8	enc1 = pd.read_excel('../graph_data/graph_encoding1.xlsx')
9	enc2 = pd.read_excel('../graph_data/graph_encoding2.xlsx')
10	enc3 = pd.read_excel('../graph_data/graph_encoding3.xlsx')
11	delay = pd.read_excel('../graph_data/graph_delay.xlsx')
12	probe = pd.read_excel('../graph_data/graph_probe.xlsx')
13	
14	classification_df = pd.read_excel('../data/all_neuron_brain_regions_cleaned.xlsx')
15	classification_df = classification_df[
16	    (classification_df["Signi"] == "Y")] # & (classification_df["Cell_Type_New"] == "IN")]  ### UNCOMMENT TO GET FIG 5L and UNCOMMENT AND CHANGE TO "PY" INSTEAD OF "IN" TO GET FIG5K
17	valid_neuron_ids = classification_df["Neuron_ID_3"].dropna().unique().tolist()
18	
19	# === Time Bins ===
20	time_bins_enc = np.arange(0, 1.2, 0.05)
[... 390 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/02_psth_decoding/main_2d,supp_1d,e.py"
}
```

```
1	import numpy as np
2	import pandas as pd
3	import matplotlib.pyplot as plt
4	from sklearn.svm import SVC
5	from scipy.stats import binom
6	import ast
7	import os
8	from matplotlib.colors import LinearSegmentedColormap
9	from scipy.ndimage import label, find_objects
10	
11	trial_info = pd.read_excel('../data/new_trial_final.xlsx')
12	subject_trials = trial_info[trial_info['subject_id'] == 14][['trial_id_final', 'num_images_presented', 'stimulus_index_enc1', 'stimulus_index_enc2', 'stimulus_index_enc3', 'response_accuracy']]
13	print(subject_trials)
14	
15	y_matrix = subject_trials
16	
17	# ===============================
18	# 1. Load Spike Data from All Periods
19	# ===============================
20	df_enc1 = pd.read_excel('../clean_data/cleaned_Encoding1.xlsx')
[... 174 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/02_psth_decoding/main_2e,supp_1f.py"
}
```

```
1	import pandas as pd
2	import numpy as np
3	import matplotlib.pyplot as plt
4	from sklearn.svm import SVC
5	import ast
6	from statsmodels.stats.multitest import multipletests
7	
8	# Load data
9	df_delay = pd.read_excel('../graph_data/graph_delay.xlsx')
10	df_fixation = pd.read_excel('../clean_data/cleaned_Fixation.xlsx')
11	df_regions = pd.read_excel('../data/all_neuron_brain_regions_cleaned.xlsx')
12	trial_info = pd.read_excel('../trial_info.xlsx')
13	
14	region_groups = {
15	    'amygdala': ['amygdala_left', 'amygdala_right'],
16	    'hippocampus': ['hippocampus_left', 'hippocampus_right'],
17	    'dACC': ['dorsal_anterior_cingulate_cortex_right', 'dorsal_anterior_cingulate_cortex_left'],
18	    'preSMA': ['pre_supplementary_motor_area_left', 'pre_supplementary_motor_area_right'],
19	    'amygdala_hippocampus': ['amygdala_left', 'amygdala_right', 'hippocampus_left', 'hippocampus_right'],
20	    'dACC_preSMA': ['dorsal_anterior_cingulate_cortex_right', 'dorsal_anterior_cingulate_cortex_left',
[... 330 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/02_psth_decoding/main_2f,supp_1g.py"
}
```

```
1	import numpy as np
2	import pandas as pd
3	import matplotlib.pyplot as plt
4	from sklearn.svm import SVC
5	from sklearn.utils import shuffle
6	import ast
7	import os
8	from tqdm import tqdm
9	from statsmodels.stats.multitest import multipletests
10	
11	trial_info = pd.read_excel('../data/new_trial_final.xlsx')
12	subject_trials = trial_info[trial_info['subject_id'] == 14][['trial_id_final', 'num_images_presented', 'stimulus_index_enc1', 'stimulus_index_enc2', 'stimulus_index_enc3', 'response_accuracy']]
13	print(subject_trials)
14	
15	y_matrix = subject_trials
16	df_delay_filtered = pd.read_excel('../graph_data/graph_delay.xlsx')
17	df_fixation = pd.read_excel('../clean_data/cleaned_Fixation.xlsx')
18	
19	y_matrix = y_matrix.reset_index(drop=True)
20	
[... 256 more lines not kept]
```

**Agent calls Agent**

```json
{
 "description": "Read code part C: bursting, cell types",
 "subagent_type": "general-purpose",
 "prompt": "You are helping write a reproduction claims file for a paper. Read code only; do NOT download or open any dataset/NWB files and do not open the .xlsx/.mat data files except to list names (you may note which column names the code reads from them). Do not write any files.\n\nPaper text: paper/10.1101-2025.10.31.684900.txt (Methods ~lines 462-497; Results ~344-398; Fig 4,5,6 legends at ~352, ~372, ~388). Code checkout (commit 5144fe8, 2025-10-26): /tmp/claude-1001/hwm-preprint\n\nRead fully: all of 04_bursting/*.py, 05_cell_analysis/*.py, 06_cell_specific/*.py, 07_spectral_clustering.py, data/cell_analysis/*.m and data/cell_analysis/README.md (if present), DOCUMENTATION.md sections on cell analysis.\n\nReport, with file:line citations for every point, concisely (bullet points):\n1. Burst detection: per participant population spike train construction (concatenation across trials? summed across neurons?), bin 70 ms, Gaussian sigma 40 ms (in bins or ms?), peak finding (scipy find_peaks? distance, prominence), threshold (90th percentile of what: smoothed rate or prominence?), the Poisson surrogates (per-trial rate matched? 100), seeds; what \"burst count\" and \"burst rate\" are, normalization.\n2. Neuron groups: ACG mean amplitude and tau_decay median split within participant; which neurons enter (R2>0.3 fit only? all 902?); exclusion of participants with <5 neurons (and <3 for PY/IN); \"balanced design\" equal neuron counts per participant - how implemented (random subsample? seed?).\n3. Tests in Fig 4c,d (real vs Poisson Wilcoxon), group comparisons (low vs high ACG, short vs long tau), Fig 4f-k epochs Enc, M1-M3 (1 s windows from maintenance onset?), Probe window, Wilcoxon, FDR family; Fig 6a-d same for PY/IN. Note that Results say \"label-shuffled null\" for Fig 6a,b while legend says Poisson.\n4. ACG computation and CellExplorer triple-exponential fit (fit_ACG.m): which spikes, narrow ACG bins, fit bounds, R2 computation, the features tau_rise, tau_decay, mean ACG (normalized how; mean over which lags), firing rate definition, burst index (Royer), CV2.\n5. Spectral clustering (07_spectral_clustering.py): features, scaling, n_clusters=2, affinity, n_neighbors, random_state, how clusters are labelled PY/IN; how 294 neurons arise; Mann-Whitney tests of Fig 5d-h; rodent validation (supp_4a-e) 333/343.\n6. Fig 6e,f GLM for PY/IN, 6g,h CV2 preferred vs nonpreferred encoding vs maintenance (Wilcoxon), 6i,j bin-width decoding for PY (n=11) and IN (n=14) concept cells, 6k,l cross-temporal, supp_5g,h decay constants.\n7. Anything in the code that disagrees with the Methods (e.g., 90th percentile of rate vs prominence; minimum interval 70 ms vs 2 bins 140 ms), any hard-coded numbers, seeds, or results that come from shipped xlsx files (e.g., Cell_metrics.xlsx produced by MATLAB) and so cannot be recomputed from the dataset without running the MATLAB.\nKeep the report under ~1500 words."
}
```

**Subagent prompt**

You are helping write a reproduction claims file for a paper. Read code only; do NOT download or open any dataset/NWB files and do not open the .xlsx/.mat data files except to list names (you may note which column names the code reads from them). Do not write any files.

Paper text: paper/10.1101-2025.10.31.684900.txt (Methods ~lines 462-497; Results ~344-398; Fig 4,5,6 legends at ~352, ~372, ~388). Code checkout (commit 5144fe8, 2025-10-26): /tmp/claude-1001/hwm-preprint

Read fully: all of 04_bursting/*.py, 05_cell_analysis/*.py, 06_cell_specific/*.py, 07_spectral_clustering.py, data/cell_analysis/*.m and data/cell_analysis/README.md (if present), DOCUMENTATION.md sections on cell analysis.

Report, with file:line citations for every point, concisely (bullet points):
1. Burst detection: per participant population spike train construction (concatenation across trials? summed across neurons?), bin 70 ms, Gaussian sigma 40 ms (in bins or ms?), peak finding (scipy find_peaks? distance, prominence), threshold (90th percentile of what: smoothed rate or prominence?), the Poisson surrogates (per-trial rate matched? 100), seeds; what "burst count" and "burst rate" are, normalization.
2. Neuron groups: ACG mean amplitude and tau_decay median split within participant; which neurons enter (R2>0.3 fit only? all 902?); exclusion of participants with <5 neurons (and <3 for PY/IN); "balanced design" equal neuron counts per participant - how implemented (random subsample? seed?).
3. Tests in Fig 4c,d (real vs Poisson Wilcoxon), group comparisons (low vs high ACG, short vs long tau), Fig 4f-k epochs Enc, M1-M3 (1 s windows from maintenance onset?), Probe window, Wilcoxon, FDR family; Fig 6a-d same for PY/IN. Note that Results say "label-shuffled null" for Fig 6a,b while legend says Poisson.
4. ACG computation and CellExplorer triple-exponential fit (fit_ACG.m): which spikes, narrow ACG bins, fit bounds, R2 computation, the features tau_rise, tau_decay, mean ACG (normalized how; mean over which lags), firing rate definition, burst index (Royer), CV2.
5. Spectral clustering (07_spectral_clustering.py): features, scaling, n_clusters=2, affinity, n_neighbors, random_state, how clusters are labelled PY/IN; how 294 neurons arise; Mann-Whitney tests of Fig 5d-h; rodent validation (supp_4a-e) 333/343.
6. Fig 6e,f GLM for PY/IN, 6g,h CV2 preferred vs nonpreferred encoding vs maintenance (Wilcoxon), 6i,j bin-width decoding for PY (n=11) and IN (n=14) concept cells, 6k,l cross-temporal, supp_5g,h decay constants.
7. Anything in the code that disagrees with the Methods (e.g., 90th percentile of rate vs prominence; minimum interval 70 ms vs 2 bins 140 ms), any hard-coded numbers, seeds, or results that come from shipped xlsx files (e.g., Cell_metrics.xlsx produced by MATLAB) and so cannot be recomputed from the dataset without running the MATLAB.
Keep the report under ~1500 words.

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint && cat -n 05_merge_data.py; echo =====; cat -n 06_add_category.py
```

```
1	import pandas as pd
     2	import os
     3	
     4	BASE_DIR = './'
     5	CLEAN_DATA_DIR = os.path.join(BASE_DIR, 'clean_data')
     6	GRAPH_DATA_DIR = os.path.join(BASE_DIR, 'graph_data')
     7	
     8	# Load all source data
     9	significant_neurons_df = pd.read_excel('./Neuron_Check_Significant_All.xlsx')
    10	trial_info_df = pd.read_excel('./trial_info.xlsx')
    11	brain_regions_df = pd.read_excel('./data/all_neuron_brain_regions_cleaned.xlsx')
    12	
    13	# Filter significant neurons to only include Y or N
    14	significant_neurons_filtered = significant_neurons_df[significant_neurons_df['Signi'].isin(['Y', 'N'])]
    15	
    16	# Add all required columns to a single file
    17	def add_all_columns_to_file(file_path, sig_neurons_df, trial_info_df, brain_regions_df):
    18	    """Add Signi, im_cat_1st, num_images_presented, and Location to a single file"""
    19	    
    20	    # Load the file
[... 354 more lines not kept]
```

**Subagent calls Bash**

```bash
cd paper; sed -n '305,345p;430,470p' 10.1101-2025.10.31.684900.txt
```

```
Concept cell definition and criteria

To investigate the neuronal basis of WM, we first identified concept cells. Concept cells were defined as neurons selective for stimulus identity, which have been implicated in WM representations in humans [29, 62–64]. For each neuron, we analyzed spiking activity during the first encoding epoch from all trials (load 1–3), counting spikes in a 200–1000 ms window after stimulus onset. In this window, we identified the two images that elicited the highest mean firing rates. To determine stimulus selectivity, we assessed the difference between these two responses using a bootstrap resampling test (see Methods). Neurons showing a significant difference were categorized as concept cells. For each concept cell, the image eliciting the highest mean firing rate was designated the preferred image.

Concept-cell identification is illustrated (Fig. 1g), and two example concept cells are provided (Fig. 1h). The peristimulus time histogram (PSTH) and raster depict a neuron that responded more strongly to image 3 during encoding, indicating stimulus selectivity (Fig. 1g). This same neuron is classified as a concept cell selective for image 3 (Fig. 1h, top; permutation test, P = 0.026). A second concept cell selective for image 1 is also shown (Fig. 1h, bottom; permutation test, P = 0.031). Of 902 neurons (Fig. 1i), 58 were identified as concept cells (6.4%; 4 ± 4 across participants). Of these 58 concept cells, 70.69% were in the AMY, 18.96% in the HPC, 1.72% in the dACC, 3.45% in the preSMA, and 5.15% in the vmPFC (Fig. 1j).

Persistent activity during maintenance emerges with population pooling and coarse temporal binning

After identifying concept cells, we examined how their activity evolves after encoding of the preferred stimulus and whether it takes the form of persistent activity [29, 65]. Consistent with prior work, we predicted that concept cells represent stimulus-specific information throughout the maintenance interval. We also co
[... 72 more lines not kept]
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint; ls; ls 04_bursting 05_cell_analysis 06_cell_specific data/cell_analysis 2>&1; wc -l 04_bursting/*.py 05_cell_analysis/*.py 06_cell_specific/*.py 07_spectral_clustering.py data/cell_analysis/*.m; grep -n "^#" DOCUMENTATION.md | head -80
```

```
01_data_extraction.py
01_task
02_psth_decoding
02_trial_info.py
03_dpca
03_standardization.py
04_bursting
04_concept_cells.py
05_cell_analysis
05_merge_data.py
06_add_category.py
06_cell_specific
07_spectral_clustering.py
08_dpca_matrices.py
DOCUMENTATION.md
README.md
data
requirements.txt
04_bursting:
main_4a.py
[... 56 more lines not kept]
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint && cat -n 08_dpca_matrices.py
```

```
1	import pandas as pd 
     2	import numpy as np
     3	import ast
     4	from dPCA import dPCA
     5	import matplotlib.pyplot as plt
     6	from ast import literal_eval
     7	from scipy.ndimage import gaussian_filter1d
     8	from dPCA.dPCA import dPCA
     9	from collections import defaultdict
    10	from scipy.spatial.distance import pdist
    11	import scipy.stats as sps
    12	import scikit_posthocs as sp
    13	
    14	trial_info = pd.read_excel('./data/new_trial_info.xlsx')
    15	subject_trials = trial_info[(trial_info['subject_id'] == 14) & (trial_info['num_images_presented'] == 1)][['new_trial_id', 'num_images_presented', 'stimulus_index']]
    16	y_matrix = subject_trials
    17	
    18	target_trials_per_stimulus = 6  # Desired number of trials per stimulus
    19	
    20	# Initialize an empty DataFrame for the balanced y_matrix
[... 226 more lines not kept]
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint/01_task && for f in main_1c.py main_1d.py supp_1a.py main_1g.py main_1i,j.py; do echo "===== $f"; cat -n "$f"; done
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint; wc -l 02_trial_info.py 03_standardization.py 08_dpca_matrices.py 05_merge_data.py; grep -n "14\|trial_id_final\|new_trial_final\|seed\|random\|75\|sample" 02_trial_info.py 03_standardization.py 05_merge_data.py | head -80
```

```
===== main_1c.py
     1	import pandas as pd
     2	import numpy as np
     3	import matplotlib.pyplot as plt
     4	import seaborn as sns
     5	from scipy.stats import kruskal, mannwhitneyu
     6	import itertools
     7	
     8	spike_data_path = "../all_spike_rate_data_probe.xlsx"
     9	trial_info_path = "../trial_info.xlsx"
    10	
    11	df = pd.read_excel(spike_data_path)
    12	trial_info = pd.read_excel(trial_info_path)
    13	df = df.merge(trial_info[['subject_id', 'trial_id', 'num_images_presented']], 
    14	              on=['subject_id', 'trial_id'], how='left')
    15	df = df.dropna(subset=['num_images_presented', 'response_accuracy'])
    16	grouped = df.groupby(['subject_id', 'num_images_presented'])['response_accuracy'].mean().reset_index()
    17	
    18	# Global Kruskal–Wallis across loads ---
    19	groups = [grouped.loc[grouped['num_images_presented'] == L, 'response_accuracy']
[... 326 more lines not kept]
```

```
149 02_trial_info.py
  343 03_standardization.py
  246 08_dpca_matrices.py
  106 05_merge_data.py
  844 total
03_standardization.py:98:trial_info_final = pd.read_excel(os.path.join(DATA_DIR, 'new_trial_final.xlsx'))
03_standardization.py:118:        trial_info_final[['subject_id', 'trial_id', 'trial_id_final']],
03_standardization.py:125:print("new_trial_id and trial_id_final columns added to all standardized DataFrames.")
03_standardization.py:214:        trial_info_final[['subject_id', 'trial_id', 'trial_id_final']],
03_standardization.py:233:    trial_info_final_graph = pd.read_excel(os.path.join(DATA_DIR, 'new_trial_final.xlsx'))
03_standardization.py:258:            trial_info_final_graph[['subject_id', 'trial_id', 'trial_id_final']],
05_merge_data.py:38:            print(f"im_cat_1st sample values: {df['im_cat_1st'].dropna().unique()[:5]}")
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint/01_task && cat -n "main_1e,f.py"
```

```
1	import pandas as pd 
     2	import numpy as np 
     3	import matplotlib.pyplot as plt
     4	from sklearn.linear_model import PoissonRegressor
     5	from tqdm import tqdm
     6	import ast
     7	
     8	trial_info = pd.read_excel('../data/new_trial_info.xlsx')
     9	subject_trials = trial_info[trial_info['subject_id'] == 1][['new_trial_id', 'num_images_presented', 'stimulus_index', 'RT', 'response_accuracy']]
    10	y_matrix = subject_trials
    11	
    12	# 1) Load Your Main Data
    13	
    14	df_delay_filtered = pd.read_excel('../graph_data/graph_delay.xlsx')
    15	y_matrix = y_matrix.reset_index(drop=True)
    16	
    17	# 2) Load Neuron Locations Data (for location-based filtering)
    18	
    19	df_neuron_locations = pd.read_excel('../data/all_neuron_brain_regions_cleaned.xlsx')
    20	
[... 225 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/04_bursting/main_4c,d,6a,b.py"
}
```

```
1	import os
2	import ast
3	import hashlib
4	import numpy as np
5	import pandas as pd
6	import scipy.signal as signal
7	from scipy.signal.windows import gaussian
8	
9	# =========================
10	# Parameters
11	# =========================
12	bin_size = 0.07                    
13	TRIAL_WIN = 1                       # seconds per trial window; CHANGE TO 2.8 FOR MAINTENANCE
14	GLOBAL_SEED = 5
15	sigma_sec = 0.04                    # Gaussian kernel 
16	prominence_threshold_percentile = 90 # percentile on smoothed rate
17	min_inter_burst_interval = 0.14     
18	N_SURROGATES = 100                   # Poisson repetitions per subject
19	PRINT_DEBUG = True
20	
[... 677 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/DOCUMENTATION.md",
 "offset": 228
}
```

```
228	## BURSTING
229	
230	Here, we are performing a bursting analysis in all cells and across subjects to look for alternative methods of carrying memoranda. We are grouping cells into different groups of neurons and determining statistical significance between them. 
231	
232	- The script concatenates spike times of individual neurons across time. You can do that for encoding and for the delay. If you want to do it for the delay, you simply have to change the TRIAL_WIN parameter to 2.8 (duration of the delay in seconds); load the delay spiking data in path_trials and change the Standardized_Spikes_New to Standardized_Spikes_in_Delay. This code also groups neurons based on their ACG features, and also based on their mechanistic properties (pyramidal vs interneurons vs concept cells) and it does it at a subject level. 
233	- The script then visualizes the burst counts for real vs poisson data and determines statistical significance. 
234	- The nect script performs a bursting analysis across task epochs. This code separates the delay period into three parts and measures statistical significance in each group of neurons across subjects. 
235	- It also performs multiple comparisons correction (FDR) and saves all p values in the relevant excel file. The figures generated in this notebook are mostly ones from Figure 4 and Figure S3 in the paper. 
236	
237	**Inputs:**
238	- graph_encoding1.xlsx, graph_encoding2.xlsx, graph_encoding3.xlsx : an Excel file with standardized spikes from Encoding 1, 2, and 3 per subject, trial and neuron, with merged data for brain region, concept vs non-concept cell, preferred image identity of every neuron. 
239	- graph_delay.xlsx : an Excel file with standardized spikes from the Delay (relative to start of the corresponding trial in the Delay) per subject, trial and neuron, with merged data for brain region, concept vs non-concept cell, preferred image identity of every neuron (relative to Encoding 1 period). 
240	- graph_probe.xlsx: an Excel
[... 55 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/03_standardization.py"
}
```

```
1	import pandas as pd
2	import ast
3	import os
4	
5	BASE_DIR = './'
6	DATA_DIR = './data/'
7	
8	filtered_files = {
9	    'Encoding1': os.path.join(BASE_DIR, 'all_spike_rate_data_encoding1.xlsx'),
10	    'Encoding2': os.path.join(BASE_DIR, 'all_spike_rate_data_encoding2.xlsx'),
11	    'Encoding3': os.path.join(BASE_DIR, 'all_spike_rate_data_encoding3.xlsx'),
12	    'Delay': os.path.join(BASE_DIR, 'all_spike_rate_data_delay.xlsx'),
13	    'Probe': os.path.join(BASE_DIR, 'all_spike_rate_data_probe.xlsx')
14	}
15	
16	def load_enc1_start_times(enc1_path):
17	    enc1_df = pd.read_excel(enc1_path)
18	    return enc1_df[['subject_id', 'trial_id', 'start_time']].drop_duplicates().rename(columns={'start_time': 'start_time_enc1'})
19	
20	enc1_start_times = load_enc1_start_times(filtered_files['Encoding1'])
[... 324 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/02_trial_info.py"
}
```

```
1	import numpy as np
2	import pandas as pd
3	import matplotlib.pyplot as plt
4	from pynwb import NWBHDF5IO
5	import os
6	import warnings
7	
8	warnings.filterwarnings("ignore", category=UserWarning, module="hdmf.utils")  # To suppress unnecessary warnings
9	
10	def read_nwb_file(filepath):
11	    """
12	    Reads an NWB file and extracts unit and electrode data as DataFrames.
13	    """
14	    io = NWBHDF5IO(filepath, mode='r', load_namespaces=True)
15	    nwbfile = io.read()
16	
17	    units = nwbfile.units
18	    electrodes = nwbfile.electrodes
19	
20	    units_data = units.to_dataframe()
[... 130 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/04_bursting/main_4f-k,6c,d.py"
}
```

```
1	import numpy as np
2	import pandas as pd
3	import scipy.signal as signal
4	import matplotlib.pyplot as plt
5	from scipy.signal.windows import gaussian
6	from scipy.stats import wilcoxon
7	from statsmodels.stats.multitest import multipletests
8	import seaborn as sns
9	import ast
10	import warnings
11	warnings.filterwarnings('ignore')
12	
13	# =========================
14	# Parameters
15	# =========================
16	bin_size = 0.07                # s
17	sigma = 0.04                   # Gaussian kernel SD (s)
18	prominence_threshold_percentile = 90
19	duration = {
20	    'Encoding 1': 1,
[... 291 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/04_bursting/main_4a.py"
}
```

```
1	import numpy as np
2	import pandas as pd
3	import ast
4	import scipy.signal as signal
5	from scipy.ndimage import gaussian_filter1d
6	import matplotlib.pyplot as plt
7	
8	df_enc1_filtered = pd.read_excel('../graph_data/graph_encoding1.xlsx')
9	
10	subject_id = 14
11	selected_neurons = [11, 13, 14, 15, 16, 17, 19, 20, 24, 26, 27, 34, 38]
12	df_subject = df_enc1_filtered[(df_enc1_filtered['subject_id'] == subject_id) & 
13	                              (df_enc1_filtered['num_images_presented'] == 1)]
14	keep_trials = sorted(df_subject['trial_id'].unique())[:45]
15	df_subject = df_subject[df_subject['trial_id'].isin(keep_trials)]
16	if selected_neurons:
17	    df_subject = df_subject[df_subject['Neuron_ID'].isin(selected_neurons)]
18	
19	TRIAL_DUR = 1
20	N_TRIALS = len(keep_trials)
[... 142 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/04_bursting/main_4e.py"
}
```

```
1	import pandas as pd
2	import matplotlib.pyplot as plt
3	import seaborn as sns
4	
5	# Load the dataset
6	file_path = "../Clustering_3D.xlsx"
7	data = pd.read_excel(file_path)
8	
9	# Clean column names
10	data.columns = data.columns.str.strip()
11	
12	data_filtered = data[(data["R2"] >= 0.3)]
13	
14	# Drop rows where Decay is NaN
15	data_filtered = data.dropna(subset=["Decay"])
16	
17	# Filter again to only keep neurons with defined Cell Type
18	#data_filtered = data_filtered.dropna(subset=["Cell_Type_New"])
19	
20	# === Plot Decay only ===
[... 20 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/04_bursting/supp_3a.py"
}
```

```
1	import pandas as pd
2	import numpy as np
3	import scipy.signal as signal
4	from scipy.signal.windows import gaussian
5	import matplotlib.pyplot as plt
6	import seaborn as sns
7	import ast
8	
9	# Parameters
10	bin_sizes = np.arange(0.05, 0.111, 0.01)  # 50-110 ms in 10 ms steps
11	sigma_values = np.arange(0.01, 0.101, 0.01)  # 10-100 ms in 10 ms steps
12	
13	TRIAL_WIN = 1                       # seconds per trial window (delay epoch length)
14	prominence_threshold_percentile = 90 # percentile on smoothed rate
15	min_inter_burst_interval = 0.14      # seconds (distance between peaks)
16	PRINT_DEBUG = True
17	path_all_meta   = '../data/all_neuron_brain_regions_cleaned.xlsx'
18	path_trials     = '../graph_data/graph_encoding1.xlsx'
19	
20	df_metadata_all_cells = pd.read_excel(path_all_meta)
[... 159 more lines not kept]
```

**Subagent calls Bash**

```bash
cd paper && sed -n '285,400p;410,510p' 10.1101-2025.10.31.684900.txt | cat -n | sed 's/^/L/' | awk '{print}' | head -0; awk 'NR>=285 && NR<=510 {print NR": "$0}' 10.1101-2025.10.31.684900.txt
```

```
<persisted-output>
Output too large (73.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/e576dfb8-0163-451a-9e9a-e3fa5978057c/tool-results/b6ev1bm1d.txt

Preview (first 2KB):
285: Complementary views posit that WM can be maintained through “activity-silent” mechanisms, in which short-term synaptic plasticity stores latent information without continuous spiking [42–44]. In this framework, brief synaptic changes could alter circuit excitability such that stimulus information is expressed through transient, structured bursts rather than uniform persistent firing. Simulations indicate that burst-like activity can optimize information transmission [45]. In nonhuman primates, brief high-frequency spiking accompanies efficient maintenance during visual WM [46]. Experimental and computational work further suggests that balanced excitatory and inhibitory interactions stabilize WM dynamics, underscoring the role of neuronal heterogeneity [47–52]. In rodents, the propensity of pyramidal neurons to burst supports internally generated memory sequences and temporal encoding [53, 54]. In humans, emerging evidence from intracranial recordings is beginning to reveal circuit-level burst dynamics, contributions of distinct cell classes, and functionally defined subpopulations to cognition [55–58]. Yet it remains unknown to what extent single neurons in the human cortex rely on sustained spiking to maintain information over time and how intrinsic properties of distinct cell classes give rise to heterogeneous, temporally structured WM dynamics.
286: 
...
</persisted-output>
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint; grep -rn "new_trial_final\|new_trial_info\|trial_id_final" --include=*.py . | grep -v "^./0[23]_psth\|read_excel" | head; grep -rln "new_trial_final" --include=*.py .; ls; ls data 2>/dev/null | head
```

```
./06_cell_specific/main_6i,j,supp_5i,j.py:12:subject_trials = trial_info[trial_info['subject_id'] == 14][['trial_id_final', 'num_images_presented', 'stimulus_index_enc1', 'stimulus_index_enc2', 'stimulus_index_enc3', 'response_accuracy']]
./06_cell_specific/main_6i,j,supp_5i,j.py:44:    trial_id = row['trial_id_final']
./06_cell_specific/main_6i,j,supp_5i,j.py:47:            (df_delay_filtered['trial_id_final'] == trial_id) &
./06_cell_specific/main_6k,l.py:13:subject_trials = trial_info[trial_info['subject_id'] == 14][['trial_id_final', 'num_images_presented', 'stimulus_index_enc1', 'stimulus_index_enc2', 'stimulus_index_enc3', 'response_accuracy']]
./06_cell_specific/main_6k,l.py:46:    trial_id = row['trial_id_final']
./06_cell_specific/main_6k,l.py:59:            match = df[(df['trial_id_final'] == trial_id) & (df['Neuron_ID_3'] == neuron)]
./03_standardization.py:118:        trial_info_final[['subject_id', 'trial_id', 'trial_id_final']],
./03_standardization.py:125:print("new_trial_id and trial_id_final columns added to all standardized DataFrames.")
./03_standardization.py:214:        trial_info_final[['subject_id', 'trial_id', 'trial_id_final']],
./03_standardization.py:258:            trial_info_final_graph[['subject_id', 'trial_id', 'trial_id_final']],
./06_cell_specific/main_6i,j,supp_5i,j.py
./06_cell_specific/main_6k,l.py
./02_psth_decoding/main_2d,supp_1d,e.py
./02_psth_decoding/main_2f,supp_1g.py
./03_standardization.py
01_data_extraction.py
01_task
02_psth_decoding
02_trial_info.py
03_dpca
[... 18 more lines not kept]
```

**Subagent calls Bash**

```bash
cd paper && awk 'NR>=289 && NR<=300 {print NR": "substr($0,1,3000)}' 10.1101-2025.10.31.684900.txt; echo; awk 'NR>=412 && NR<=445 {print NR": "$0}' 10.1101-2025.10.31.684900.txt
```

```
289: Taken together, our results demonstrate that maintenance of stimulus-specific information in WM does not require sustained spiking and can emerge from interactions among heterogeneous neuronal populations expressed through transient, structured activity. These findings advance mechanistic accounts of WM and underscore the value of single-trial, time-resolved analyses that account for neuronal heterogeneity to uncover the circuit dynamics underlying human cognition.
290: 
291: Results
292: Behavior and single-neuron recordings in a working memory task
293: 
294: To probe circuit dynamics underlying working memory (WM) maintenance, we analyzed single-neuron recordings from patients with epilepsy (n = 21) while they performed a Sternberg WM task ([59]). On each trial, 1–3 images (load 1–3) were presented during an encoding epoch, followed by a maintenance interval and a probe period. Participants indicated whether the probe image had appeared during encoding epoch of the current trial (Fig. 1a). Recordings from the 21 patients yielded 902 well-isolated units (Fig. 1b,i), distributed across the amygdala (AMY; 259 neurons), dorsal anterior cingulate cortex (dACC; 171 neurons), hippocampus (HPC; 190 neurons), presupplementary motor area (preSMA; 250 neurons), and ventromedial prefrontal cortex (vmPFC; 32 neurons).
295: 
296: Download figureOpen in new tab
297: Fig. 1
298: Task, recording sites, behavior and concept cell definition
299: 
300: a, Sternberg working memory (WM) task. Each trial begins with encoding of 1–3 images (load 1–3), followed by a 2.5–2.8 s maintenance interval (“Hold”) and a probe requiring an old/new response. If the probe image was presented during encoding on that trial, the correct response is “yes” (old); otherwise “no” (new). Reaction time is measured from probe onset. b, Recording sites registered to MNI152 space and overlaid on the CIT168 atlas. Regions assessed are amygdala (AMY), dorsal anterior cingulate cortex (dACC), hippocampus (HPC
[... 35 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/07_spectral_clustering.py"
}
```

```
1	import pandas as pd
2	import numpy as np
3	import matplotlib.pyplot as plt
4	import seaborn as sns
5	import os
6	from sklearn.preprocessing import StandardScaler
7	from sklearn.cluster import SpectralClustering
8	from mpl_toolkits.mplot3d import Axes3D
9	import umap.umap_ as umap
10	import warnings
11	warnings.filterwarnings("ignore")
12	
13	# Load and preprocess data
14	df = pd.read_excel("./data/cell_analysis/Cell_metrics.xlsx")
15	
16	df_filtered = df[(df["R2"] >= 0.3)].dropna(subset=["firing_rate", "acg_norm", "tau_rise"]).copy()
17	
18	hex_palette = {  
19	    "Spectral": ['#3254A2', '#941A37']
20	}
[... 88 more lines not kept]
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint; grep -n -i -B2 -A8 "trial_final\|pseudo\|subject 14\|75" README.md DOCUMENTATION.md | head -80; cat requirements.txt
```

```
DOCUMENTATION.md-55-- Run the code 03_standardization.py
DOCUMENTATION.md-56-- This code standardizes the data by the start time of encoding period 1 to the existing Excel. This type of standardization is needed for our cross-temporal decoding analysis, where we run continuous decoding throughout the entire trial (and not only the delay period). 
DOCUMENTATION.md:57:- Make sure that you have downloaded new_trial_info.xlsx and trial_info_final.xlsx, as these are needed for the code. It is important to balance the design matrix and y matrix by the identity of images that are presented. For that, we need the new_trial_final.xlsx excel sheet with our new trial identities. As we will also use the balanced by load trial identities, we also add a new_trial_id column using the new_trial_info.xlsx file. 
DOCUMENTATION.md-58-- This code adds a new neuron id (subject id + 0 + neuron id) for easier pooling of the neurons.
DOCUMENTATION.md-59-- It saves all files in a new clean_data folder.
DOCUMENTATION.md-60-- The code creates another folder: graph_data, used in PSTH graphs. It merges data with trial information and standardizes the spikes, this time, based on the start of the corresponding period (delay standardized with start of delay, etc.)
DOCUMENTATION.md-61-
DOCUMENTATION.md-62-**Inputs:** 
DOCUMENTATION.md-63-
DOCUMENTATION.md-64-- all_spike_rate_data_encoding1.xlsx: Excel file with the following characteristics: subject id (1-21), trial id (1-135), neuron id, stimulus id (0-4), image id (how the people who created the dataset generated the ids), spikes for every trial and neuron, spike rate for every trial and neuron, start and end time of the encoding 1 period of the corresponding trial. 
DOCUMENTATION.md-65-
--
DOCUMENTATION.md-78-- new_trial_info.xlsx: trial identities, ensuring pooling across neurons for GLM encoder. 
DOCUMENTATION.md-79-
DOCUMENTATION.md:80:- new_trial_final.xlsx: new trial identities, ensuring easy pooling across neurons for the decoder. Generate
[... 53 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/05_cell_analysis/main_5d-h.py"
}
```

```
1	import pandas as pd
2	import matplotlib.pyplot as plt
3	import seaborn as sns
4	import numpy as np
5	from scipy.stats import mannwhitneyu
6	from statsmodels.stats.multitest import multipletests
7	
8	# Load data
9	file_path = "../Clustering_3D.xlsx"
10	data = pd.read_excel(file_path)
11	data.columns = data.columns.str.strip()
12	
13	metrics = ["firing_rate", "acg_norm","tau_rise", "Burst", "CV2"]
14	labels = {
15	    "firing_rate": "Firing Rate",
16	    "acg_norm": "ACG (Norm)",
17	    "tau_rise": "τ Rise",
18	    "Burst": "burst",
19	    "CV2": "CV2"
20	}
[... 156 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/05_cell_analysis/supp_4a-e.py"
}
```

```
1	import os
2	import numpy as np
3	import pandas as pd
4	import matplotlib.pyplot as plt
5	import seaborn as sns
6	from math import ceil
7	from sklearn.preprocessing import StandardScaler
8	from sklearn.cluster import SpectralClustering
9	import umap
10	from scipy.stats import mannwhitneyu
11	from statsmodels.stats.multitest import multipletests
12	
13	# ===================== PATHS =====================
14	in_path  = "../data/cell_analysis/validation_data.xlsx"
15	out_excel = "./Validation_clustering.xlsx"
16	fig_dir  = "./"
17	os.makedirs(fig_dir, exist_ok=True)
18	
19	# ===================== LOAD ONCE =====================
20	df = pd.read_excel(in_path)
[... 199 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/05_cell_analysis/main_5a,b.py"
}
```

```
1	import numpy as np
2	import matplotlib.pyplot as plt
3	from scipy.io import loadmat
4	
5	mat_file_path = '../data/cell_analysis/acg.mat'  
6	data = loadmat(mat_file_path)
7	num_neurons = 902
8	acg_narrow = data['acg']['narrow'][0,0]  
9	
10	# Create time axis from -50 ms to 50 ms for 201 points
11	time_axis = np.linspace(-50, 50, 201)
12	
13	start_neuron = 19
14	end_neuron = 38
15	neurons_to_plot = range(start_neuron, end_neuron + 1)
16	num_neurons_to_plot = len(neurons_to_plot)
17	
18	plots_per_row = 5
19	num_rows = (num_neurons_to_plot + plots_per_row - 1) // plots_per_row
20	
[... 23 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/08_dpca_matrices.py"
}
```

```
1	import pandas as pd 
2	import numpy as np
3	import ast
4	from dPCA import dPCA
5	import matplotlib.pyplot as plt
6	from ast import literal_eval
7	from scipy.ndimage import gaussian_filter1d
8	from dPCA.dPCA import dPCA
9	from collections import defaultdict
10	from scipy.spatial.distance import pdist
11	import scipy.stats as sps
12	import scikit_posthocs as sp
13	
14	trial_info = pd.read_excel('./data/new_trial_info.xlsx')
15	subject_trials = trial_info[(trial_info['subject_id'] == 14) & (trial_info['num_images_presented'] == 1)][['new_trial_id', 'num_images_presented', 'stimulus_index']]
16	y_matrix = subject_trials
17	
18	target_trials_per_stimulus = 6  # Desired number of trials per stimulus
19	
20	# Initialize an empty DataFrame for the balanced y_matrix
[... 227 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/03_dpca/main_3a-c.py"
}
```

```
1	import numpy as np
2	import ast
3	from dPCA import dPCA
4	import matplotlib.pyplot as plt
5	from ast import literal_eval
6	from scipy.ndimage import gaussian_filter1d
7	from dPCA.dPCA import dPCA
8	from collections import defaultdict
9	from scipy.spatial.distance import pdist
10	import scipy.stats as sps
11	import scikit_posthocs as sp
12	
13	trialE = np.load(f"../trialE.npy")
14	trialD = np.load(f"../trialD.npy")
15	
16	trialX = trialE
17	
18	n_rep, n_neurons, n_stim, tE = trialE.shape
19	_,      _,           _,     tD = trialD.shape
20	n_train = n_rep // 2
[... 87 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/03_dpca/main_3d,supp_2a,b,i.py"
}
```

```
1	import numpy as np
2	import ast
3	from dPCA import dPCA
4	import matplotlib.pyplot as plt
5	from ast import literal_eval
6	from scipy.ndimage import gaussian_filter1d
7	from dPCA.dPCA import dPCA
8	from collections import defaultdict
9	from scipy.spatial.distance import pdist
10	import scipy.stats as sps
11	import scikit_posthocs as sp
12	
13	trialE = np.load(f"../trialE.npy")
14	trialD = np.load(f"../trialD.npy")
15	
16	trialX = trialE
17	
18	###ENC AND MAINTENANCE
19	
20	#dPCA distance-resampling  (Encoding vs Maintenance)
[... 227 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/data/cell_analysis/fit_ACG.m"
}
```

```
1	function fit_params_out = fit_ACG(acg_narrow,plots)
2	    % This function is part of CellExplorer
3	    % Fits a tripple exponential to the autocorrelogram with 0.5ms bins from -50ms -> 50ms
4	    % This function requires the Curve Fitting Toolbox
5	    %
6	    % By Peter Petersen
7	    % Last edited: 21-09-2021;
8	    
9	    if ~exist('plots','var')
10	        plots = true;
11	    end
12	    
13	    % acg_narrow = cell_metrics.acg.narrow;
14	    acg_narrow(100:102) = 0; % Sets the time-zero bin to zero (-0.5ms -> 0.5ms)
15	    offset = 101;
16	    x = ([1:100]/2)';
17	    
18	    % Variables
19	    a0 = [20, 1, 30, 2, 0.5, 5, 1.5,2];
20	    lb = [1, 0.1, 0, 0, -30, 0,0.1,0];
[... 185 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/data/cell_analysis/calc_ACG_metrics.m"
}
```

```
1	function acg_metrics = calc_ACG_metrics(spikes)
2	    % Inputs:
3	    %   spikes - structure containing 'times' (cell array of spike times) and 'total' (number of spikes)
4	    
5	    % Ensure that spikes.times is a cell array
6	    if ~iscell(spikes.times)
7	        error('spikes.times must be a cell array');
8	    end
9	
10	    numcells = length(spikes.times);  % Number of neurons
11	
12	    % Initialize metrics
13	    ThetaModulationIndex = nan(1, numcells);
14	    BurstIndex_Royer2012 = nan(1, numcells);
15	    BurstIndex_Doublets = nan(1, numcells);
16	
17	    % Define bins for ACG calculation
18	    bins_wide = 1001;   % Total 1001 bins for wide ACG (±500 ms, 1 ms bins)
19	    bins_narrow = 201;  % Total 201 bins for narrow ACG (±50 ms, 0.5 ms bins)
20	
[... 69 more lines not kept]
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint/data/cell_analysis; cat -n Mean_ACG.m normalize_acg_to_unit.m; ls -la; ls ../..; ls ../
```

```
1	% Extract the ACG matrix 
     2	acg_values = spikes.acg.wide_norm;  
     3	
     4	% Compute the mean ACG for each neuron (column-wise mean)
     5	mean_acg_values = mean(acg_values, 1, 'omitnan'); 
     6	
     7	% Display the first few mean ACG values
     8	disp('Mean ACG values for first 5 neurons:');
     9	disp(mean_acg_values(1:5));
    10	function [acg_unit] = normalize_acg_to_unit(acg)
    11	% acg: [numBins x numNeurons] (e.g., acg_wide or acg_narrow). Here, we need acg_wide.
    12	% Returns acg_unit with each column divided by its column max.
    13	% Zero-lag bin is forced to 0 after normalization.
    14	% acg = spikes.acg.acg_wide; You can put that in the command window to extract the acg_wide from each neuron. 
    15	
    16	    acg_unit = acg;                       % copy
    17	    [numBins, ~] = size(acg);
    18	    zeroBin = ceil(numBins/2);            % middle bin (0 lag)
    19	
    20	    % Column-wise max ignoring NaNs
[... 49 more lines not kept]
```

**Subagent calls Bash**

```bash
cd paper && grep -n -o '.\{300\}88\.73.\{600\}' 10.1101-2025.10.31.684900.txt; grep -n -o '.\{200\}75 trials.\{200\}' 10.1101-2025.10.31.684900.txt | head; grep -n -o '.\{200\}within-participant.\{100\}' 10.1101-2025.10.31.684900.txt|head -3; grep -n -i -o '.\{200\}dPCA.\{0,40\}sigma.\{200\}\|.\{150\}σ = .\{150\}' 10.1101-2025.10.31.684900.txt | head
```

```
287:ch that neurons with distinct intrinsic properties differentially reorganize their activity across task epochs to preserve and transform stimulus representations during WM. We performed single-trial, within-participant analyses and applied dimensionality-reduction techniques to move beyond across-trial averaging. We 
326:unt of stimulus-specific information across the maintenance period, irrespective of its temporal stability. We trained a linear support vector machine (SVM) using a coarse temporal bin width (1 s) on within-participant activity from concept cells during the maintenance epoch, separately for load 1, load 2, and load 3
437:ure consistent trial counts across participants and conditions, we constructed pseudo-populations for encoding analyses and population decoding by pooling neurons across participants while preserving within-participant labels [81–83]. Because trial numbers varied across participants, we matched to the minimum common 
332:sis (dPCA) to concept-cell activity from load 1 trials. Spike trains were binned in non-overlapping 2-ms intervals, convolved with a Gaussian kernel (σ = 60 ms), and z-scored relative to the fixation baseline. Encoding and maintenance were analyzed separately, each with its own dPCA fit. For consistency
346:rcentile prominence threshold. To avoid averaging across trials and participants, spikes were concatenated per patient, binned and Gaussian-smoothed (σ = 40 ms), and burst candidates within 70 ms of a previous event were suppressed to prevent fragmentation of single events [58]. Parameters were selected
478:ths using neural data from the encoding period only, comparing burst counts across parameter combinations. The combination Δt = 70 ms (bin width) and σ = 40 ms (Gaussian kernel) maximized the burst count while remaining near the center of the search space, providing a balanced sensitivity-specificity tr
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/03_dpca/main_3h,supp_2c,d,l.py"
}
```

```
1	import numpy as np
2	import ast
3	from dPCA import dPCA
4	import matplotlib.pyplot as plt
5	from ast import literal_eval
6	from scipy.ndimage import gaussian_filter1d
7	from dPCA.dPCA import dPCA
8	from collections import defaultdict
9	from scipy.spatial.distance import pdist
10	import scipy.stats as sps
11	import scikit_posthocs as sp
12	
13	# Same but for Early vs Late maintenance
14	trialE = np.load(f"../trialE.npy")
15	trialD = np.load(f"../trialD.npy")
16	
17	trialX = trialE
18	
19	def run_dpca_distance_resampling_stratified(
20	    trialD,
[... 208 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/03_dpca/main_3e-g,supp_2j,k.py"
}
```

```
1	import numpy as np
2	import matplotlib.pyplot as plt
3	from mpl_toolkits.mplot3d import Axes3D
4	import numpy as np
5	from dPCA import dPCA
6	from ast import literal_eval
7	from scipy.ndimage import gaussian_filter1d
8	from dPCA.dPCA import dPCA
9	
10	trialE = np.load(f"../trialE.npy")
11	trialD = np.load(f"../trialD.npy")
12	
13	trialX = trialE
14	
15	# 1. Split trialD into early and late maintenance
16	trialD_early = trialD[:, :, :, :624]   # shape: (6, 58, 5, 624)
17	trialD_late  = trialD[:, :, :, 624:]   # shape: (6, 58, 5, 625)
18	
19	RD_early = np.mean(trialD_early, axis=0)  
20	RD_late  = np.mean(trialD_late, axis=0)  
[... 94 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/03_dpca/supp_2e-h.py"
}
```

```
1	import numpy as np
2	import matplotlib.pyplot as plt
3	from mpl_toolkits.mplot3d import Axes3D
4	import numpy as np
5	from dPCA import dPCA
6	from ast import literal_eval
7	from scipy.ndimage import gaussian_filter1d
8	from dPCA.dPCA import dPCA
9	
10	trialE = np.load(f"../trialE.npy")
11	trialD = np.load(f"../trialD.npy")
12	
13	trialX = trialE
14	
15	# Trial-averaged data 
16	R_train = np.mean(trialX, axis=0)  # (58, 5, 199)
17	RD_train = np.mean(trialD, axis=0)  # (58, 5, 499)
18	# Compute training mean per neuron
19	R_train_mean = np.mean(R_train.reshape(58, -1), axis=1)[:, None, None]
20	RD_train_mean = np.mean(RD_train.reshape(58, -1), axis=1)[:, None, None]
[... 55 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/06_cell_specific/main_6e,f,supp_e,f.py"
}
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/06_cell_specific/main_6g,h.py"
}
```

```
1	import numpy as np
2	import ast
3	import matplotlib.pyplot as plt
4	
5	def generate_filtered_spike_trains(df_encoding, df_delay, cell_type_map,
6	                                   encoding_col='Standardized_Spikes',
7	                                   delay_col='Standardized_Spikes',
8	                                   trial_col='trial_id',
9	                                   encoding_duration=1,
10	                                   delay_duration=2.5,
11	                                   preferred_col='Category',
12	                                   preferred_label='Preferred'): ### CHANGE TO "Non-Preferred" FOR FIG 6H
13	    """
14	    Returns:
15	    spike_dict[neuron_uid] = {
16	        'subject_id': subject_id,
17	        'cell_type': 'PY' or 'IN',
18	        'encoding': np.array([...]),
19	        'delay':    np.array([...])
20	    }
[... 171 more lines not kept]
```

```
1	import pandas as pd 
2	import numpy as np 
3	import matplotlib.pyplot as plt
4	from sklearn.linear_model import PoissonRegressor
5	from tqdm import tqdm
6	import ast
7	
8	trial_info = pd.read_excel('../data/new_trial_info.xlsx')
9	subject_trials = trial_info[trial_info['subject_id'] == 1][['new_trial_id', 'num_images_presented', 'stimulus_index', 'RT', 'response_accuracy']]
10	y_matrix = subject_trials
11	
12	# 1) Load Your Main Data
13	
14	df_delay_filtered = pd.read_excel('../graph_data/graph_delay.xlsx')
15	y_matrix = y_matrix.reset_index(drop=True)
16	
17	# 2) Load Neuron Locations Data (for location-based filtering)
18	
19	df_neuron_locations = pd.read_excel('../Clustering_3D.xlsx')
20	
[... 228 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/06_cell_specific/main_6i,j,supp_5i,j.py"
}
```

```
1	import numpy as np
2	import pandas as pd
3	import matplotlib.pyplot as plt
4	from sklearn.svm import SVC
5	from sklearn.utils import shuffle
6	import ast
7	import os
8	from tqdm import tqdm
9	from statsmodels.stats.multitest import multipletests
10	
11	trial_info = pd.read_excel('../data/new_trial_final.xlsx')
12	subject_trials = trial_info[trial_info['subject_id'] == 14][['trial_id_final', 'num_images_presented', 'stimulus_index_enc1', 'stimulus_index_enc2', 'stimulus_index_enc3', 'response_accuracy']]
13	print(subject_trials)
14	
15	y_matrix = subject_trials
16	df_clustering = pd.read_excel('../Clustering_3D.xlsx')
17	df_delay_filtered = pd.read_excel('../graph_data/graph_delay.xlsx')
18	df_fixation = pd.read_excel('../clean_data/cleaned_Fixation.xlsx')
19	
20	y_matrix = y_matrix.reset_index(drop=True)
[... 257 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/06_cell_specific/main_6k,l.py"
}
```

```
1	import numpy as np
2	import pandas as pd 
3	import matplotlib.pyplot as plt
4	import os
5	from sklearn.svm import SVC
6	from matplotlib.colors import LinearSegmentedColormap
7	from scipy.stats import binom
8	from scipy.ndimage import label, find_objects
9	import ast
10	
11	trial_info = pd.read_excel('../data/new_trial_final.xlsx')
12	df_clustering = pd.read_excel('../Clustering_3D.xlsx')
13	subject_trials = trial_info[trial_info['subject_id'] == 14][['trial_id_final', 'num_images_presented', 'stimulus_index_enc1', 'stimulus_index_enc2', 'stimulus_index_enc3', 'response_accuracy']]
14	print(subject_trials)
15	
16	y_matrix = subject_trials
17	
18	# 1. Load Spike Data from All Periods
19	# ===============================
20	df_enc1 = pd.read_excel('../clean_data/cleaned_Encoding1.xlsx')
[... 180 more lines not kept]
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/06_cell_specific/supp_5g,h.py"
}
```

```
1	import pandas as pd
2	import matplotlib.pyplot as plt
3	import numpy as np
4	from scipy.stats import ttest_rel
5	
6	# Load feather
7	df = pd.read_excel("../data/cell_analysis/decay_constant_change.xlsx")
8	df.columns = df.columns.str.strip()
9	
10	# Ensure required columns
11	required_cols = ['Cell_Type', 'Nonpref Enc', 'Pref Enc', 'Nonpref D', 'Pref D']
12	assert all(col in df.columns for col in required_cols), "Missing required columns"
13	
14	# Clean cell type strings
15	df['Cell_Type'] = df['Cell_Type'].astype(str).str.strip().str.upper()
16	
17	# Split into cell types
18	df_py = df[df['Cell_Type'].str.startswith("PY")]
19	df_in = df[df['Cell_Type'].str.startswith("IN")]
20	
[... 53 more lines not kept]
```

**Subagent calls Bash**

```bash
cd paper && grep -n -o '.\{0,400\}88\..\{0,700\}' 10.1101-2025.10.31.684900.txt | head -3; grep -n -o '.\{0,300\}σ = 60.\{0,300\}' 10.1101-2025.10.31.684900.txt; grep -n -o '.\{0,200\}dPCA.\{0,300\}' 10.1101-2025.10.31.684900.txt | sed -n '1,4p' | cut -c1-600; awk 'NR>=446 && NR<=462' 10.1101-2025.10.31.684900.txt | grep -n -i 'dpca\|2-ms\|sigma\|σ' | cut -c1-900
```

```
100:10.1152/jn.00188.2002
302:Participants performed well on the task (Extended Data Fig. 1a), with high accuracy (Fig. 1c) and fast reaction time (Fig. 1d). Task accuracy was 88.73% ± 1.25% and was higher for load 1 than for load 3 (Wilcoxon rank-sum, P = 0.027; Fig. 1c). Reaction time for correct trials was 1.06 ± 0.28 s. Reaction time was faster for probes held in memory than for probes not in memory (permutation test, P = 0.001), and correct decisions were faster than incorrect ones (permutation test, P = 0.002). Together, these results indicate that participants performed the task as instructed and exhibited typical WM effects [60, 61].
618:88.↵Astrand, E. et al. Comparison of classifiers for decoding sensory and cognitive information from prefrontal neuronal populations. PloS One 9, e86314 (2014).CrossRefPubMedGoogle Scholar
332:To investigate the transient coding suggested by the bin-width and cross-temporal decoding results, we applied demixed principal component analysis (dPCA) to concept-cell activity from load 1 trials. Spike trains were binned in non-overlapping 2-ms intervals, convolved with a Gaussian kernel (σ = 60 ms), and z-scored relative to the fixation baseline. Encoding and maintenance were analyzed separately, each with its own dPCA fit. For consistency across trials, the maintenance epoch was truncated to 2.5 s. Stimulus separability was quantified as the Euclidean distance between condition-averaged 
332:To investigate the transient coding suggested by the bin-width and cross-temporal decoding results, we applied demixed principal component analysis (dPCA) to concept-cell activity from load 1 trials. Spike trains were binned in non-overlapping 2-ms intervals, convolved with a Gaussian kernel (σ = 60 ms), and z-scored relative to the fixation baseline. Encoding and maintenance were analyzed separately, each with its own dPCA fit. For consistency acro
332:ss trials, the maintenance epoch was truncated to 2.5 s. Stimulus separability was quantif
[... 5 more lines not kept]
```

**Subagent calls Bash**

```bash
sed -n 340,400p paper/10.1101-2025.10.31.684900.txt; echo ======; sed -n 455,500p paper/10.1101-2025.10.31.684900.txt
```

Result: not kept, because it reads the paper's text.

**Subagent calls Bash**

```bash
cd paper; for l in 344 346 348 350 352 354 356 358 360 362 364 366 368 370 372 374 376 378 380 382 384 386 388 390 392 394 396 398; do :; done; awk 'NR>=344 && NR<=398 && length($0)>0' 10.1101-2025.10.31.684900.txt | grep -n -i -E "burst|ACG|tau|decay|poisson|shuffl|spectral|PY|IN |interneur|pyramid|CV2|R2|R²|neurons" | cut -c1-1500 | head -60
```

```
1:Bursting dynamics reorganize spiking activity between encoding and maintenance
2:To characterize the evolving code, we quantified population bursts following recent primate and rodent studies [46, 53, 54]. A burst was defined as a transient increase in population activity within a 70-ms bin exceeding a 90th-percentile prominence threshold. To avoid averaging across trials and participants, spikes were concatenated per patient, binned and Gaussian-smoothed (σ = 40 ms), and burst candidates within 70 ms of a previous event were suppressed to prevent fragmentation of single events [58]. Parameters were selected by a small grid search (Extended Data Fig. 3a) and are consistent with reports that bursts typically span 50–100 ms [69]. Significance was assessed against a Poisson null model (100 surrogate iterations; see Methods) to determine whether observed bursts reflected meaningful neural dynamics rather than random fluctuations (Fig. 4a). Analyses were performed separately for encoding and maintenance to test whether temporal firing patterns differ across epochs. To examine how intrinsic firing properties shape these dynamics, we repeated all analyses in neuron groups stratified by mean autocorrelogram (ACG) amplitude (low vs. high) and ACG decay time constant (τdecay; short vs. long; Fig. 4b). We used a balanced design in which every participant contributed the same number of neurons for each analysis condition.
3:Download figureOpen in new tab
5:Bursting dynamics reorganize from encoding to maintenance.
6:a, Example burst detection in real spike trains compared with simulated Poisson spike trains matched in rate. b, Exponential fits to spike train autocorrelograms (ACGs) illustrating neurons with different decay time constants (τdecay). c, Burst counts during encoding (load 1) in real data compared with Poisson predictions across participants. Deviations from Poisson predictions were observed for all cells (Wilcoxon signed-rank, P = 0.003) and in the Low ACG popula
[... 22 more lines not kept]
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint; grep -n "Category\|Preferred\|im_cat\|def \|read_excel\|to_excel" 06_add_category.py | head -50; wc -l 06_add_category.py
```

```
10:enc1_data = pd.read_excel(os.path.join(CLEAN_DATA_DIR, 'cleaned_Encoding1.xlsx'))
11:enc2_data = pd.read_excel(os.path.join(CLEAN_DATA_DIR, 'cleaned_Encoding2.xlsx'))
12:enc3_data = pd.read_excel(os.path.join(CLEAN_DATA_DIR, 'cleaned_Encoding3.xlsx'))
14:# Add Category to encoding files (both clean and graph)
19:def add_category_to_encoding(df, encoding_name):
20:    """Add Category column to encoding files: Preferred if im_cat_1st == stimulus_index"""
22:    if 'im_cat_1st' in df.columns and 'stimulus_index' in df.columns:
23:        # Create Category column based on your logic
24:        df['Category'] = df.apply(
25:            lambda row: 'Preferred' if row['im_cat_1st'] == row['stimulus_index'] else 'Non-Preferred', 
29:        category_counts = df['Category'].value_counts()
30:        print(f"Category distribution for {encoding_name}: {category_counts.to_dict()}")
35:# Add Category to CLEAN encoding files
41:enc1_data.to_excel(os.path.join(CLEAN_DATA_DIR, 'cleaned_Encoding1.xlsx'))
42:enc2_data.to_excel(os.path.join(CLEAN_DATA_DIR, 'cleaned_Encoding2.xlsx'))
43:enc3_data.to_excel(os.path.join(CLEAN_DATA_DIR, 'cleaned_Encoding3.xlsx'))
45:# Add Category to GRAPH encoding files
47:enc1_graph = pd.read_excel(os.path.join(GRAPH_DATA_DIR, 'graph_encoding1.xlsx'))
48:enc2_graph = pd.read_excel(os.path.join(GRAPH_DATA_DIR, 'graph_encoding2.xlsx'))
49:enc3_graph = pd.read_excel(os.path.join(GRAPH_DATA_DIR, 'graph_encoding3.xlsx'))
[... 31 more lines not kept]
```

**Subagent calls Bash**

```bash
cd paper; awk 'NR>=460 && NR<=498 && length($0)>0' 10.1101-2025.10.31.684900.txt | cut -c1-2500
```

```
For analyses of temporal structure within maintenance, the same procedure was applied to the first (early) and second (late) halves of the maintenance period.
Autocorrelogram-based characterization of single-neuron temporal dynamics
We characterized single-neuron temporal firing dynamics using spike-train autocorrelograms (ACGs). Spike times from all task epochs were aggregated for each of the 902 neurons and processed in MATLAB. For each neuron, we computed pairwise time differences between spikes as Δt = tj − ti, for all i /= j, where ti and tj denote individual spike times. Self-coincidences (Δt = 0) were excluded. These time differences were binned symmetrically around zero lag to produce a histogram of spike coincidences. We computed two ACGs per neuron to capture fine-scale and broader temporal structure:
Narrow ACG: computed within a ± 50 ms window using 0.5 ms bins (201 bins total), capturing short-latency dynamics and burst-related peaks.
Wide ACG: computed within a ± 500 ms window using 1 ms bins (1001 bins total), capturing rhythmic modulation such as theta-range oscillations.
Each ACG was divided by the total number of spikes and the bin width to yield a spike-density histogram. We then normalized each ACG by dividing all bin values by the maximum ACG amplitude for that neuron. This unit normalization rescales every ACG to [0, 1] to preserve temporal structure while enabling direct comparison of relative modulation and burst strength across neurons irrespective of absolute firing rates.
We fit each narrow ACG (using raw amplitudes, not unit-normalized) with bounded nonlinear least squares, using the default initialization in CellExplorer [72]. The resulting ACG-derived features (τrise, τdecay, R2) were used in downstream analyses (e.g., cell-type classification and bursting analyses).
To ensure stable estimation, ACGs with poor fits (R2 < 0.3) were excluded from further analyses.
Burst detection
We identified transient bursts of spiking activity using a 
[... 10 more lines not kept]
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint; grep -n -i -E "cv2|firing_rate|Spikes_rate" 02_trial_info.py | head -30; grep -rn "Cell_metrics\|Clustering_3D\|decay_constant_change\|validation_data" --include=*.py --include=*.md . | grep -v "^./0[4-6]_\|07_" | head; git log --oneline -1
```

```
37:    def calculate_firing_rate(spike_times):
42:    def calculate_cv2(spike_times):
50:        'firing_rate': units_data['spike_times'].apply(calculate_firing_rate),
51:        'CV2': units_data['spike_times'].apply(calculate_cv2),
68:        'Percent of ISI < 3 ms', 'Firing Rate (Hz)', 'CV2',
73:        metrics['ISI_3ms'], metrics['firing_rate'], metrics['CV2'],
./DOCUMENTATION.md:201:- Clustering_3D.xlsx: an Excel file with labels for putative cell-type classification (PY/IN). Use this if you want to achieve analysis across neuronal types. 
./DOCUMENTATION.md:241:- Clustering_3D.xlsx: an Excel file with labels for putative cell-type classification (PY/IN). Use this if you want to achieve analysis across neuronal types. 
./DOCUMENTATION.md:263:- After extracting these values, they can be neatly put in one Excel file. We have provided this under data >> Cell_metrics.xlsx >> Cell_analysis.xlsx
./DOCUMENTATION.md:267:- For our cell classification, we will use the Cell_analysis.xlsx file. We filter cells with an R squared value below 0.3 (less than 30% explained variance) and we run a spectral clustering method on the following metrics – Mean ACG, firing_rate, Tau_rise. We want to see how the cells get separated. We save the spectral clustering labels (0,1) in a new excel file (Clustering_3D.xlsx). The script assigns cell types to the labeled clusters. The cluster that includes cells with higher firing rates is labeled the interneuron cluster, and the other one is labeled the pyramidal cluster. It adds a new column “Cell_Type_New”, with the new identity of each cell, based on the spectral clustering. Then print the number of IN/PY classified neurons and we visualise the UMAP. 
./DOCUMENTATION.md:285:- Clustering_3D.xlsx: an Excel file containing the cell type labels provided by the spectral clustering
5144fe8 Update calc_ACG_metrics.m
```

**Subagent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/hwm-preprint/02_trial_info.py",
 "limit": 60,
 "offset": 20
}
```

```
20	    units_data = units.to_dataframe()
21	    electrodes_data = electrodes.to_dataframe()
22	
23	    io.close()
24	
25	    return units_data, electrodes_data
26	
27	def calculate_metrics(units_data):
28	    """
29	    Calculate metrics for each unit based on spike times and waveform properties.
30	    """
31	    def calculate_isi(spike_times):
32	        if len(spike_times) < 2:
33	            return np.nan
34	        isi = np.diff(spike_times)
35	        return np.sum(isi < 0.003) / len(isi)
36	
37	    def calculate_firing_rate(spike_times):
38	        if len(spike_times) < 2:
39	            return np.nan
[... 40 more lines not kept]
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint && grep -rn "probe_in_out\|response_time\|'RT'" --include=*.py . | grep -v "^./01_data_extraction" ; grep -rn "seed\|random_state" --include=*.py . | grep -v "^./0[2-6]_"
```

```
./01_task/main_1e,f.py:9:subject_trials = trial_info[trial_info['subject_id'] == 1][['new_trial_id', 'num_images_presented', 'stimulus_index', 'RT', 'response_accuracy']]
./01_task/main_1d.py:6:reaction_data['response_time'] = reaction_data['Probe_End_Time'] - reaction_data['Probe_Start_Time']
./01_task/main_1d.py:8:subject_medians = df_correct.groupby(['subject_id', 'num_images_presented'])['response_time'].median().reset_index()
./01_task/main_1d.py:11:sns.boxplot(data=subject_medians, x='num_images_presented', y='response_time', palette='Purples', width=0.6, showfliers=False)
./01_task/main_1d.py:12:sns.stripplot(data=subject_medians, x='num_images_presented', y='response_time',
./01_task/main_1d.py:21:plt.savefig("./response_time_boxes.eps", format="eps", dpi=300)
./06_cell_specific/main_6e,f,supp_e,f.py:9:subject_trials = trial_info[trial_info['subject_id'] == 1][['new_trial_id', 'num_images_presented', 'stimulus_index', 'RT', 'response_accuracy']]
./06_cell_specific/main_6e,f,supp_e,f.py:111:# subject_trials: DataFrame with 'RT' and 'subject_id'
./07_spectral_clustering.py:27:df_filtered["Spectral"] = SpectralClustering(n_clusters=2, affinity='nearest_neighbors', random_state=42).fit_predict(X_scaled)
./07_spectral_clustering.py:30:reducer = umap.UMAP(n_components=3, random_state=42)
./08_dpca_matrices.py:26:    sampled_trials = stimulus_trials.sample(n=target_trials_per_stimulus, random_state=42)  # Set random_state for reproducibility
```

**Subagent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint && sed -n 100,135p "06_cell_specific/main_6e,f,supp_e,f.py"
```

```
neuron_to_region = dict(zip(df_neuron_locations['Neuron_ID_3'].astype(str), df_neuron_locations['Region_Label']))
region_labels = [neuron_to_region.get(nid, 'Unknown') for nid in stripped_ids]

SEED = 17
rng = np.random.default_rng(SEED)

n_iterations = 1000      # bootstrap null iterations
alpha_neuron = 0.05      # per-neuron significance threshold (via null quantile)

# Inputs
# counts_matrix: [n_trials x n_neurons] or [n_trials x n_neurons x timebins]
# subject_trials: DataFrame with 'RT' and 'subject_id'
# region_labels: array-like [n_neurons], region string per neuron

neural_data = counts_matrix
X_raw = subject_trials['num_images_presented'].to_numpy().astype(float) ###CHANGE TO RT FOR FIG S5F and 6F.
cell_type_labels = np.asarray(region_labels)  

if neural_data.ndim == 3:
    y_counts = neural_data.sum(axis=2)
[... 16 more lines not kept]
```

**Subagent**

I read all the requested scripts plus `02_trial_info.py`, `03_standardization.py`, the relevant parts of `06_add_category.py` and `DOCUMENTATION.md`. I opened no data files, so trial counts and participant lists that live in the xlsx files can't be confirmed. Paths below are relative to `/tmp/claude-1001/hwm-preprint`. The biggest finding: several Methods claims (cluster-duration null, pairwise bin-width tests, the "≥3 concept cells" rule, two-sided binomial test) don't match the code, and Fig 2d labels are not the first image for loads 2 and 3.

**1. Fig 2c population PSTH** (`02_psth_decoding/main_2c,5k,l,supp_1b,c.py`)
- **Neurons:** concept cells (`Signi=="Y"`) from `all_neuron_brain_regions_cleaned.xlsx` (:14-17).
- **Trials:** load 1 is selected with `num_images_presented==1` (:103-105).
- **Preferred vs nonpreferred:** taken from the `Category` column, which is "Preferred" when `im_cat_1st == stimulus_index` and "Non-Preferred" otherwise (`06_add_category.py:24-25`). So "nonpreferred" pools all four other images. For delay at loads 2/3, a trial counts as Preferred if any encoded image was preferred (`06_add_category.py:96-125`).
- **Spike alignment:** the `graph_*` files are aligned to each epoch's own onset (`03_standardization.py:288-320`).
- **Bins:** 50 ms. Encoding and probe span 0-1.2 s, delay 0-3 s (:20-22); delay is plotted to 2.5 s (:311).
- **Normalization:** each neuron's trial-mean rate is z-scored with its fixation `Spikes_rate_Fixation` mean and SD (np.std, ddof=0) (:28-47).
- **Smoothing:** `gaussian_filter1d` with sigma = 1 bin, i.e. 50 ms, NaN→0 (:137-151).
- **Bootstrap:** resamples neurons, not trials, using the same paired indices for both conditions. nboot=1000, seed 42. The p-value is 2·min(P(diff>0), P(diff<0)), run on the smoothed data (:196-225, :252).
- **Correction:** a single BH-FDR (`fdrcorrection`, 'indep') over all bins pooled across 9 epoch×load panels plus 3 probe comparisons (pref-nonencoded vs nonpref-nonencoded) (:284-286). Threshold 0.05 (:326).

**2. Fig 2d cross-temporal decoding** (`main_2d,supp_1d,e.py`)
- **Classifier:** `SVC(kernel='linear')` with default C=1 and no seed (:94).
- **Features:** one 250 ms bin across all concept cells (`Signi=='Y'` in cleaned_Encoding1) (:28, :90).
- **Spikes:** enc1, enc2, enc3, delay and probe are concatenated, all aligned to enc1 onset (:44-56; `03_standardization.py:58`).
- **Windows:** 250 ms, stepped by 100 ms, from 0 to 5/6/7 s for loads 1/2/3 (:58-66).
- **z-score:** (spike count per 250 ms − fixation mean rate) / fixation SD of rate (:78-80). This mixes counts and rates; for a linear SVM it amounts to an offset plus a global rescale.
- **CV:** LOOCV for every train/test bin pair (:83-99).
- **Pseudo-population:** subject 14's trial rows (`trial_id_final`) from `new_trial_final.xlsx` serve as the template. Neurons from every participant are matched on `trial_id_final` (:11-12, :53). That realigned trial file is a pre-supplied input with no generating code (`DOCUMENTATION.md:57,80`). The trial count (75?) isn't visible in code.
- **Labels:** load 1 uses `stimulus_index_enc1`, but load 2 uses enc2 and load 3 uses enc3 (:147-152). This contradicts the Methods' "first encoding period".
- **Chance:** 1/number of unique enc1 labels (:130).
- **Binomial test:** one-sided, `1 - binom.cdf(k)`, which is P(X>k) (:160). Methods says two-sided.
- **FDR:** BH over the whole time×time grid (:161-163).
- **No cluster-duration permutation exists.** Instead, contours with more than 13 points are kept, a hard-coded threshold (:175-178). No seeds are set.

**3. Fig 2e maintenance decoding** (`main_2e,supp_1f.py`)
- **Cell threshold:** `if len(neuron_ids) <= 3: continue` (:70) means at least 4 concept cells per participant per region, not "≥3".
- **Participants and regions:** whichever participants pass the threshold (not hard-coded). MTL is the `amygdala_hippocampus` group (:19).
- **Decoding is within-participant,** using that participant's trials from `trial_info.xlsx` with no balancing (:12, :73). This contradicts the Fig 2e legend's "pooled across participants".
- **Bins:** 1 s windows, 250 ms step, over 0-2.5 s of delay, giving 7 bins (:24-27). All bins × neurons are concatenated into one feature vector; this is not per-bin decoding (:115-122).
- **Labels:** the last image (enc1, enc2 or enc3 for loads 1/2/3) (:84-91).
- **Classifier and CV:** LOOCV with `SVC(linear, random_state=42)` (:45-55).
- **Permutation:** 1000 label shuffles from one shared `default_rng(42)` (:28-29, :126). Results therefore depend on loop order.
- **Reported accuracy** (35.56% / 32.13%) is the mean over participants of per-participant LOOCV accuracy (:313, :322).
- **P-value:** (#null-means ≥ real + 1)/1001, where the null is the per-shuffle mean across participants (:314-317). The minimum is about 0.001.
- **FDR:** BH within each load across the 6 region groups (:331-336).

**4. Fig 2f bin-width decoding** (`main_2f,supp_1g.py`)
- **Population:** subject 14 template with `trial_id_final` and all concept cells pooled (:11-12, :29, :46).
- **Bin widths:** 0.25/0.5/0.75/1.0 s with a 25 ms step (:118-119). So "25 ms" is the slide step; widths are not varied in 25 ms increments.
- **Window placement:** sliding bins cover the whole 0-2.5 s delay and are all concatenated × neurons (:120, :129-139).
- **Labels and CV:** last image (:98-109), LOOCV (:67-84).
- **Trial count:** the number of load-1 trials isn't visible in code. Accuracies being multiples of 3.33% suggest N=30 (an inference).
- **SEM** is computed across trials' 0/1 outcomes (:155).
- **Permutation:** 1000, `default_rng(42)` (:86-95). p = (#null ≥ real + 1)/1001 (:188).
- **FDR:** BH over 12 tests (4 widths × 3 loads) (:191-192).
- **No pairwise test between bin widths exists anywhere in the code.** The P=0.026/0.004/0.032 values are not reproducible from the repository.

**5. dPCA (Fig 3)**
- **Package:** Kobak's `from dPCA.dPCA import dPCA`. It is missing from `requirements.txt`.
- **Fit settings:** `labels='st'`, `regularizer='auto'`, `opt_regularizer_flag=True`, so lambda is chosen by built-in CV (`03_dpca/main_3d,supp_2a,b,i.py:119-131`).
- **Inconsistent `protect` setting:** early maintenance uses `protect=['t']` while late uses `[]` (`main_3h,...:115` vs `:124`). Fig 3d uses `[]` for both.
- **Trials:** subject 14's load-1 rows (`new_trial_id`), 6 sampled per stimulus with `random_state=42`, giving 5×6=30 (`08_dpca_matrices.py:14-27`).
- **Bins:** 2 ms. Encoding spans 0-1 s, giving 499 bins (not 1.2 s) (:123). Delay spans 0-2.5 s, giving 1249 bins (:159).
- **Normalization:** rate z-scored with fixation mean/SD (:91-104).
- **Smoothing:** `gaussian_filter1d(sigma=60)` in bin units, so sigma = 120 ms (:105, :124). The Methods wording "α=60; 120 ms" matches; the Results "σ = 60 ms" is wrong.
- **Likely bug in trial matching:** delay trials are selected with `delay_data['trial_id'].isin(new_trial_id values)` (:192), whereas encoding uses `new_trial_id` (:98). Delay and encoding trials may therefore differ.
- **Trial pairing across neurons** goes by row order, and missing trials are zero-filled (:144-151, :221-228).
- **Neuron count:** 58 is hard-coded in some scripts (`main_3e-g...:22`, `supp_2e-h.py:19`).
- **Resampling:** a 3/3 split per stimulus, 100 iterations, with an assertion that splits are unique (`main_3d...:79-83, :143`).
- **Separability score:**
  - Each stimulus trajectory on 's' dPCs 0-4 is averaged over time into a centroid (:65-66).
  - `pdist` then gives 10 pairwise distances.
  - The score per iteration is their mean (:149).
- **Statistics:** `scipy.stats.kruskal` runs across 5 groups, including Enc_train and Maint_train, not just the 3 test conditions (:47-53, :152). This inflates H. Dunn's test uses `scikit_posthocs.posthoc_dunn(p_adjust='fdr_bh')` on all 10 pairs (:158).
- **Seeds:** Fig 3d passes `random_seed=1` (:228). Fig 3h falls back to the default seed 5 (`main_3h...:26`, call at :216 with no seed). Fig 3a-c uses `default_rng(0)` for a single split (`main_3a-c.py:26`). Fig 3e-g uses `np.random.seed(2)` for a single split (`main_3e-g...:36`).
- **Early/late split:** at bin 624 of 1249, about 1.248 s (`main_3h...:22`; `main_3e-g...:16-17`).

**6. Other code–paper disagreements and hard-coded values**
- **Not implemented:** the cluster-duration null (2d), the pairwise bin-width tests (2f), and the Neural Decoding Toolbox/LIBSVM. Everything is sklearn.
- **Thresholds and test sidedness:** concept-cell threshold is >3, not ≥3. The binomial test is one-sided, not two-sided. Fig 2d labels are the last image, not the first.
- **Legend vs Results:** the Fig 2e legend says "pooled", but the code (and the Results text) is within-participant.
- **Hard-coded values:**
  - subject 14 as the trial template, used in 2d, 2f, dPCA, and also 6i-l
  - contour length > 13 (2d)
  - `time_split=624`
  - delay_dur 2.8 s in the 2d epoch lines
  - `durations=2.5`
- **Swapped documentation:** `DOCUMENTATION.md:158-160` attributes the scripts to the wrong figures (main_2d ↔ 2f ↔ 2e).
- **Preselected trial lists:** `new_trial_final.xlsx` and `new_trial_info.xlsx` are supplied inputs with no generating code, so they are effectively preselected.

Result: not kept, because it reads the paper's text.

**Subagent**

I read all the requested files in full; nothing was run or written. Line numbers are file-relative. Overall: the shipped matched-trial and region spreadsheets cannot be rebuilt from the dataset, the concept-cell test has no seed, and the GLM code differs from Methods 437–442 in several places.

**1. Data source, epochs, exclusions, matched trial sets**
- **DANDI version:** README.md:22 downloads `DANDI:000469/0.240123.1806`, but Methods 417 cites `0.231213.2047`.
- **Files read:** only `sub-{1..21}/sub-{i}_ses-2_ecephys+image.nwb`, hard-coded at 01_data_extraction.py:417 and 02_trial_info.py:86. DOCUMENTATION.md:10 says only session 2 (Sternberg) is used, not the "41 sessions" in Methods 417. Missing files are skipped silently (01:364-366).
- **NWB fields read:**
  - `stimulus_template['StimulusTemplates']`; keys are sorted to give stimulus ranks (01:25-41).
  - `stimulus['StimulusPresentation'].data`, indexed as `i*4 + {0,1,2}`, which assumes 4 presentations per trial (01:57, 67-71).
  - `intervals['trials']`: `timestamps_Encoding{1,2,3}`, `timestamps_Encoding{1,2,3}_end`, `start_time`/`stop_time`, `loadsProbe_PicIDs`, `probe_in_out`, `response_accuracy` (01:84-105, 300-313).
  - `acquisition['events']` timestamps and codes (01:182-184).
  - `units['spike_times']` (01:126).
  - 02 also reads `waveforms_peak_snr`, `waveforms_mean_snr`, `waveforms_mean_proj_dist` and `waveforms_isolation_distance` for quality metrics (02:52-56).
- **Epoch definitions:**
  - Encoding k: `[timestamps_EncodingK, timestamps_EncodingK_end)` (01:84-105, 118).
  - Fixation: event code 11 to the next event 1 (01:191).
  - Maintenance: event 6 to event 7 (01:243).
  - Probe: event 7 to event 8, within each trial's start/stop (01:304-309). `Probe_Image_ID = loadsProbe_PicIDs - 1` (01:344).
  - Fixation and delay trial_ids are assigned by order of occurrence, not from the trials table (01:192, 244), so they could misalign if an event pair is missing.
  - Load = 3 minus the number of enc2/enc3 stimulus indices equal to 5, where 5 means a blank (02:108-110; DOCUMENTATION.md:11).
- **Alignment:**
  - `clean_data` spikes are re-referenced to Encoding-1 onset (03:58); fixation is re-referenced to fixation onset (03:182).
  - `graph_data` spikes are re-referenced to each epoch's own onset (03:272-314).
- **Exclusions:** none. No trial or neuron (quality) filter exists anywhere in 01–06; all units are kept.
- **Matched sets:** `new_trial_id` (load-matched, used for the GLM and dPCA) and `trial_id_final` (identity-matched, used for decoding) come only from the shipped `data/new_trial_info.xlsx` and `data/new_trial_final.xlsx`, merged in at 03:97-121 and 232-261.
  - No script generates either file. The README only describes them (README.md:49; DOCUMENTATION.md:57, 78-80).
  - The selection is therefore not reproducible from the dataset alone.
  - README calls the second file "trial_info_final.xlsx", but it is named `new_trial_final.xlsx`.
  - From code usage, new_trial_info has the columns `subject_id`, `trial_id`, `new_trial_id`, `num_images_presented`, `stimulus_index`, `RT` and `response_accuracy` (main_1e,f.py:9).

**2. Concept cells (04_concept_cells.py)**
- **Input and window:** Encoding-1 spikes from `cleaned_Encoding1.xlsx`, counted in the inclusive window [0.2, 1.0] s (04:7, 19-20, 27). Spikes are already cut to the presentation interval (01:118).
- **Trials:** all trials, all loads, no accuracy filter.
- **Top two identities:** chosen by mean rate, starting from mean = 0, so silent neurons get empty groups and end up 'N' (04:36-53).
- **Test:** a bootstrap, not a permutation.
  - 1000 iterations (04:76, 93).
  - Each group is resampled with replacement to `min_len` = the smaller group's n, not to its own n (04:77, 81-82). Methods says the test "accommodates unequal trial counts", so this is a difference.
  - `p = min(2·frac(d>0), frac(d≥0), 2·frac(d<0), frac(d≤0))` (04:86-90). It is roughly the two-sided "twice the smaller tail" in Methods 433, but the extra `1 − x` terms can give a smaller p.
  - Classified as a concept cell if p < 0.05 and both groups have more than one trial (04:105).
- **Seed:** none. It uses unseeded `np.random.choice` (04:81), so the concept-cell set (n = 58 claimed) is not exactly reproducible.
- **Fig 1i,j do not use this output.** main_1i,j.py:4, 27 reads the `Signi` column already present in the shipped `all_neuron_brain_regions_cleaned.xlsx`.

**3. Behaviour (Fig 1c, 1d, supp_1a)**
- **Fig 1c (main_1c.py):**
  - Source is `all_spike_rate_data_probe.xlsx`, which has one row per neuron per trial; these are equal-weight duplicates, so per-subject means are unaffected (1c:8-15).
  - Mean accuracy is taken per subject per load, giving 21 patients from session 2 (1c:16).
  - Tests: Kruskal–Wallis (1c:21), then pairwise two-sided Mann–Whitney (rank-sum) with Bonferroni ×3 (1c:30-36).
  - It prints both raw and adjusted p, so it is unclear which one is the reported P = 0.027.
- **Fig 1d (main_1d.py):** RT = `Probe_End_Time − Probe_Start_Time` (event 7 to 8), correct trials only, median per subject per load. There is no statistical test (1d:6-8).
- **supp_1a:** per-subject accuracy = correct/total, then mean and SEM across subjects (supp_1a:9-17). This is the likely source of 88.73% ± 1.25%.
- **Not computed in the inspected scripts:** RT 1.06 ± 0.28 s, the in- vs out-of-memory RT permutation test (P = 0.001), and the correct vs incorrect test (P = 0.002). A repo-wide grep found no `probe_in_out` analysis.

**4. Fig 1e,f GLM (main_1e,f.py)**
- **Trials:** the trial template is subject 1's rows of new_trial_info (1e,f:9). Every neuron from every subject is joined by `new_trial_id` (1e,f:52-55), forming a pseudo-population. A neuron with no row for a trial gets count 0 (1e,f:56-60).
- **Trial filters:** none for accuracy or load. All loads are included, and only maintenance is analysed. This contradicts Methods 439 ("separately within load 1 encoding and maintenance epochs").
- **Window:** spike count in [0, 2.5) s from delay onset (`graph_delay`) (1e,f:67-75).
- **Predictor:** subject 1's `num_images_presented`, z-scored (1e,f:113, 127).
- **RT (Fig 1f):**
  - It requires a manual edit; DOCUMENTATION.md:194 says "change line 149", which is stale — the predictor is at line 113.
  - It would use subject 1's RT for all neurons, not each neuron's own subject's RT.
- **Model:** sklearn `PoissonRegressor(alpha=0.0)` with an intercept; max_iter is 1000 for the real fit and 500 for the null fits (1e,f:147, 157).
- **Permutation:** `SEED = 17` and 1000 iterations (1e,f:106-109).
  - "Within participant" is not implemented: `subject_trials` has no `subject_id` column, so `blocks = None` and the permutation is global (1e,f:9, 124, 134-135). With a single shared predictor vector, a within-participant permutation would not be possible anyway.
- **Per-neuron rule:** |β| ≥ the 95th percentile of the neuron's |null β| (`method='higher'`) (1e,f:163-168).
- **Group test:** null count of neurons crossing their own thresholds; p = #(null ≥ observed)/1000, with no +1 (1e,f:185-194).
- **Multiple comparisons:** none across the 5 regions or the two predictors.
- **Regions:** left and right merged into amygdala, hippocampus, preSMA, vmPFC and dACC, from the shipped Location column (1e,f:87-104). `desired_locations` is computed but never used (1e,f:28-30). Neurons with no match are labelled 'Unknown' and excluded.
- **Significance stars:** *** means P < 0.005 (1e,f:215).

**5. Fig 1g and 1i,j**
- **Fig 1g (main_1g.py):** single neuron `Neuron_ID_3` 14016, subject 14 (1g:123-124).
  - Encoding-1 spikes, all trials, grouped by stimulus; 0–1 s, 50 ms bins, Gaussian σ = 1 bin with zero padding (1g:33, 84-89).
  - It plots firing rate in Hz, not the z-score described in Methods 429.
  - The CI is a single constant, 1.96 × SEM of all bins flattened (1g:82).
- **Fig 1i,j (main_1i,j.py):** pie charts of all neurons and of `Signi == 'Y'` counts by region, both from the shipped xlsx (main_1i,j.py:4-63). Unmatched locations go to 'Other'.

**6. dPCA matrices (08_dpca_matrices.py)**
- **Trials:** subject 14's load-1 `new_trial_id`s, 6 per stimulus, sampled with `random_state=42` (08:15-26), giving 30 trials.
- **Neurons:** concept cells only (`Signi == 'Y'`) (08:43).
- **Binning:** 2 ms bins, `np.arange(0, 1, .002)` for encoding (499 bins, up to 0.998 s) and `np.arange(0, 2.5, .002)` for delay (1249 bins); this is the 2.5 s truncation (08:123, 159).
- **Z-scoring:** done on the 2 ms rates, before smoothing, using the mean and SD across trials of the fixation-epoch rate (`Spikes_rate_Fixation`) (08:52-57, 104). If SD = 0 the result is all zeros (08:72-73).
- **Smoothing:** `gaussian_filter1d` with σ = 60 bins, which is 120 ms. Results 332 says σ = 60 ms; the Methods text ("α = 60; bin width = 120 ms") matches the code (08:124, 105).
- **Bug in the delay matrix:** it filters `delay_data['trial_id'].isin(new_trial_ids)` (08:192), whereas encoding uses `new_trial_id` (08:98). So the delay trials are likely the wrong ones.
- **Trial-to-sample mapping:** rows are filled by row order, not by trial id, and missing rows are zero-filled (08:144-151, 221-228).
- **Output shapes:** `trialE`/`trialD` are (6, N, 5, T) (08:140, 216, 243-244).

**7. Other code/Methods disagreements and hard-coded values**
- Already covered above: DANDI version; within-participant permutation; load-1-only wording; no correction across regions; z-scored vs Hz PSTH; dPCA σ; min_len bootstrap; no concept-cell seed; matched sets only from shipped xlsx.
- **Hard-coded numbers:** 21 subjects, ses-2 only; 0.2–1.0 s window; 1000 bootstrap iterations; p < 0.05; 2.5 s delay window; SEED 17; random_state 42; subject 1 template (GLM); subject 14 template (dPCA); example neuron 14016; σ = 60 bins; 6 trials per stimulus.
- DOCUMENTATION.md:232 gives the delay as 2.8 s for the bursting analyses, versus 2.5 s here.

Result: not kept, because it reads the paper's text.

**Subagent**

I read every requested file at commit 5144fe8. In the code, burst detection, cell-type labelling and several of the statistics differ materially from what the paper describes. Citations below are file:line, relative to `/tmp/claude-1001/hwm-preprint/`; paper line numbers refer to `paper/10.1101-2025.10.31.684900.txt`.

### 1. Burst detection (`04_bursting/main_4c,d,6a,b.py`)
- **Parameters:** bin 0.07 s (12), sigma 0.04 s (15), 90th percentile (16), minimum interval 0.14 s converted to `ceil(0.14/0.07)` = 2 bins (17, 22), 100 surrogates (18), `GLOBAL_SEED=5` (14).
- **Window and load:** `TRIAL_WIN=1` s for encoding (13). Maintenance needs manual edits: `TRIAL_WIN=2.8` (13) and path `graph_maintenance.xlsx` (30). Only load 1 is analysed (205).
- **Population train:** spikes from all selected neurons are pooled into one list (summed). Each trial is offset by `trial_idx*TRIAL_WIN`, which concatenates trials (224-232). Only the first non-null row per neuron and trial is used (88-93, 229). Spikes are clipped to [0, TRIAL_WIN] (80).
- **Smoothing:** `np.histogram` (244). The kernel is `scipy.signal.windows.gaussian(M=len(counts), std=sigma/bin)` (247). That std is in bins: 0.04/0.07 ≈ 0.57 bins, so smoothing is very slight. The kernel is normalised to sum 1 and convolved with `mode='same'` (248-250).
- **Peaks:** `threshold = np.percentile(smoothed, 90)`, i.e. the 90th percentile of the smoothed counts (251). It is passed as a **prominence** to `find_peaks(smoothed, prominence=threshold, distance=2)` (253-255). There is no height criterion.
- **Poisson surrogates:** each neuron's spike count on each trial gives its rate (263-274). The count is drawn from Poisson(rate·TRIAL_WIN) and spike times are uniform within the trial (286-290). The same bins, kernel and the **real-data threshold** are reused (296-298). The surrogate value is the mean over 100 runs (301). The RNG is `default_rng(sha256(category, subject, "poisson") XOR 5)` (82-86, 276).
- **"Burst count":** the raw number of peaks over the whole concatenated train (256). Nothing is normalised by trial count or duration anywhere. Fig 4f-k "burst rates" are the same raw counts (`main_4f-k,6c,d.py:221`), even though the legend (paper l.352) refers to "rate normalization".
- **Fig 4a (`main_4a.py`):** this differs from the main pipeline. It uses subject 14 only, the first 45 trials and hard-coded `Neuron_ID`s (10-17). Smoothing is `gaussian_filter1d` (59), the threshold is the **95th** percentile (62), there is no `distance`, and the RNG is unseeded (79).
- **Grid search (`supp_3a.py`):** bins 50-110 ms (not 50-150 as Methods say) by sigma 10-100 ms (10-11). It uses All_cells, encoding load 1 only, and averages real burst counts (140-142).

### 2. Neuron groups
- **R² filter:** the ACG and decay groups use rows with `R2 > 0.3` from `Clustering_3D.xlsx` (main_4c,d: 28, 40), which is itself already filtered at R2 ≥ 0.3.
- **No median split:** `_split_low_high_for_subject` sorts on `acg_norm` or `Decay`, with `Neuron_ID_3` as a stable tiebreak. It takes the lowest m and highest m neurons, with m = 10//2 + 1 = **6** (95-120). With exactly 10 neurons, 2 neurons fall in both groups.
- **Participant threshold:** a participant needs ≥ **10** eligible neurons (`PER_SUBJ`, 52, 164-172), not the 5 stated in Methods.
- **"Balanced design":** this is simply the fixed 6 lowest and 6 highest neurons per participant. There is no random subsampling and no seed.
- **Other groups:**
  - Concept cells: `Signi=="Y"`, ≥ 3 per participant (174-176).
  - PY/IN: ≥ 3 per participant (178-181), not balanced.
  - All_cells: all neurons from `all_neuron_brain_regions_cleaned.xlsx`, participants with ≥ 10 neurons (183-185).
- **Inconsistency in 4f-k:** `main_4f-k,6c,d.py` takes All_cells from `Clustering_3D` (47, 150), i.e. only the R²-filtered 294 neurons, not all 902. Its PY/IN groups are not R²-refiltered (148-149).

### 3. Tests
- **Fig 4c,d / 6a,b, real vs Poisson:** paired by subject, `wilcoxon(..., zero_method='pratt', method='asymptotic')` (444). FDR-BH runs across the 8 categories, PY and IN included (459-462). There is an extra pooled omnibus test (465-474).
- **Group comparisons (low vs high ACG, short vs long tau):** all 28 category pairs are compared on real counts with paired Wilcoxon (`zero_method='wilcox'`). It falls back to Mann-Whitney if fewer than 2 subjects overlap (482-507). FDR-BH runs over all 28 pairs (518). A Friedman omnibus is also computed (530-551).
- **No label-shuffled null exists in the code.** Only the Poisson surrogate is implemented, so the Results wording for Fig 6a,b ("label-shuffled null", paper l.~380) contradicts both the code and the legend.
- **Fig 4f-k / 6c,d epochs (`main_4f-k,6c,d.py`):**
  - Durations: Encoding 1 s, Delay **3 s**, Probe 1 s (19-25), versus 2.8 s in 4c,d and 2.5 s in 6e-h.
  - Encoding for load L comes from `graph_encodingL.xlsx`, i.e. the last image (49, 161).
  - **Different detector:** no `distance` argument (212), and all duplicate rows are counted (193-195).
  - **M1-M3:** the 90th-percentile threshold is computed on the whole concatenated delay. Peaks are then assigned to `np.array_split` thirds of the bin index (216-219). Because the delay train is concatenated across trials, these thirds are thirds of the whole recording, not 1 s windows from maintenance onset in each trial.
  - **Statistics:** paired Wilcoxon on all 10 period pairs, run only if the vectors have equal length. Pairing is by list order, not subject ID, because subjects with no spikes are skipped (178-180, 199) (274-285). FDR-BH is applied within each group × load (289).

### 4. ACG and features (MATLAB)
- **Input spikes are not shipped.** `data/cell_analysis/spikes_struct.mat` is 2 bytes, a placeholder.
- **ACGs (`calc_ACG_metrics.m`):**
  - Narrow ACG: ±50 ms, 0.5 ms bins, 201 bins. Wide ACG: ±500 ms, 1 ms bins, 1001 bins (18-35).
  - Self-pairs are removed and lags are binned with `round` (70-83).
  - Each ACG is divided by n_spikes·bin_size (87).
  - Royer burst index = `mean(wide(503:505))/mean(wide(700:800))`, i.e. lags +2..+4 ms over +199..+299 ms (45). A doublet index is also computed (38).
- **Normalisation:** `normalize_acg_to_unit.m` divides each column by its maximum and sets the zero-lag bin to 0 (21-33).
- **Mean ACG (`Mean_ACG.m`):** mean of the max-normalised **wide** ACG over all 1001 lags (2-5).
- **Fit (`fit_ACG.m`):**
  - Bins 100:102 are zeroed (14), and the fit uses positive lags x = 0.5..50 ms (15-16).
  - Equation `max(c(exp(-(x-f)/a) - d·exp(-(x-f)/b)) + h·exp(-(x-f)/g) + e, 0)` (41).
  - Start `a0=[20,1,30,2,0.5,5,1.5,2]`, lower `lb=[1,0.1,0,0,-30,0,0.1,0]`, upper `ub=[500,50,500,15,50,20,5,100]` (19-21).
  - tau_decay = a, tau_rise = b. R² = `gof.rsquare` from the Curve Fitting Toolbox (80-88).
  - The fit runs on the raw narrow ACG, which matches Methods.
- **Firing rate:** n / (last spike − first spike) over the session (`02_trial_info.py:37-40`).
- **"CV2" is actually CV.** `02_trial_info.py:42-46` computes std(ISI)/mean(ISI), not Holt's local CV2. That column is presumably what feeds Fig 5h. True CV2 is computed only in `main_6g,h.py:117-122`.

### 5. Spectral clustering (`07_spectral_clustering.py`)
- **Input and 294:** `Cell_metrics.xlsx`, filtered to `R2 >= 0.3` and non-NaN firing_rate / acg_norm / tau_rise (16). This filter is where the 294 neurons come from.
- **Clustering:** `StandardScaler` (24), then `SpectralClustering(n_clusters=2, affinity='nearest_neighbors', random_state=42)`. `n_neighbors` is not set, so the default of 10 applies (27). UMAP (3D, `random_state=42`) is for display only (30).
- **Labelling is hard-coded:** label 1 → PY, 0 → IN (37-45). It is not assigned from firing rate, contrary to DOCUMENTATION.md:267 and the Results. The result depends on the sklearn version.
- **Output:** writes `./Clustering_3D.xlsx` (104). Downstream scripts read it as `../Clustering_3D.xlsx`.
- **Fig 5d-h (`main_5d-h.py`):** `mannwhitneyu(IN, PY)` two-sided on firing_rate, acg_norm, tau_rise, Burst and CV2 (13, 49), with **FDR-BY** across the 5 metrics (63).
- **Rodent validation (`supp_4a-e.py`):**
  - Reads `validation_data.xlsx`, columns firing_rate, norm_acg, tau_rise, tau_decay, cell_type.
  - Same clustering settings (32-35).
  - Each cluster is labelled by its majority `cell_type`. "Accuracy" = matched/total, which is the claimed 333/343 (43-58).
  - Tests use matched cells only, Mann-Whitney with FDR-BY over 4 metrics (114-136).
  - **Bug:** line 207 prints an undefined `out_feather`, so the script raises NameError after saving.

### 6. Fig 6e-l and Extended Data Fig 5g,h
- **6e,f GLM (`main_6e,f,supp_e,f.py`):**
  - Trial table is from **subject 1 only** (9), matched on `new_trial_id` (60).
  - Neurons: all PY+IN; concept-only by uncommenting (24-32).
  - Spike counts in 0-2.5 s of the delay (74-91).
  - Predictor: z-scored load, or RT by manual edit (115, 129). Model: `PoissonRegressor(alpha=0)` (149).
  - Null: 1000 plain permutations, since `blocks` is None (no subject_id column, 126), with `SEED=17` (103-106).
  - Each neuron is significant if |slope| ≥ the 95% quantile of its own null (165-170). The per-type count p-value = fraction of null counts ≥ observed, with no +1 (196).
- **6g,h CV2 (`main_6g,h.py`):**
  - Concept cells (`Signi=="Y"`) from Clustering_3D (89). Spikes are concatenated over preferred trials; 6h needs a manual switch to `'Non-Preferred'` (12).
  - Encoding 1 s from `graph_encoding1`, delay 2.5 s (9-10). There is no load-1 filter.
  - True CV2 (117-122); encoding vs delay compared with default `wilcoxon` per cell type (138-139).
- **6i,j bin-width decoding (`main_6i,j,supp_5i,j.py`):**
  - Subject 14's trials only (12). Neurons are PY or IN (manual edit, 23) with `Signi=="Y"` (30), but not filtered by subject. Neurons from other subjects would get empty spike arrays, i.e. zero features.
  - The n = 11 and n = 14 counts appear nowhere in the code.
  - Features: sliding windows of 250/500/750/1000 ms, step 25 ms, over 0-2.5 s (119-121). Binned counts are z-scored with the fixation rate in Hz, a unit mismatch (137-139).
  - Decoder: leave-one-out linear SVC (68-85).
  - Labels: `stimulus_index_encL` for load L, so supp 5i,j decodes the second image for load 2 (100-110).
  - Null: 1000 permutations with `rng(42)` (87, 122); p = (k+1)/(n+1) (189); FDR-BH over 12 tests (193).
- **6k,l cross-temporal (`main_6k,l.py`):**
  - PY concept cells hard-coded (29-34); subject 14 trials.
  - Spikes from Enc1-3, Delay and Probe are appended **without time offsets** (50-61).
  - Windows 250 ms, step 100 ms (64-66). Leave-one-out SVC for every train/test pair (89-105).
  - Binomial test against chance 1/5, FDR over the whole matrix (166-169). Contours are drawn only if longer than 13 points (183).
- **Extended Data Fig 5g,h (`supp_5g,h.py`):**
  - Entirely from the shipped `decay_constant_change.xlsx`, columns `Cell_Type`, `Nonpref Enc`, `Pref Enc`, `Nonpref D`, `Pref D` (7-11). No code computes these values.
  - Uses a **paired t-test** (`ttest_rel`, 25-26), whereas the paper says Wilcoxon.

### 7. Code vs Methods discrepancies and fixed inputs
- **Threshold:** a 90th-percentile prominence of the smoothed counts, not the "smoothed rate exceeds 90th percentile" of Methods. Surrogates reuse the real-data threshold.
- **Minimum separation:** 2 bins (140 ms) in 4c,d, matching Methods. Results say 70 ms. 4f-k uses no separation at all.
- **Kernel:** sigma 0.57 bins.
- **Groups:** fixed 6/6 extremes with ≥ 10 neurons required, not a median split with ≥ 5.
- **Fig 4e (`main_4e.py`):** line 15 overwrites the R² filter on line 12. The histogram shows Clustering_3D's 294 neurons, not "all recorded neurons" as the legend says.
- **Delay length:** 2.8, 3 or 2.5 s depending on the script.
- **Manual edits needed:** maintenance in 4c,d, IN vs PY in 6i-l, RT vs load in 6e,f, Non-Preferred in 6h.
- **DOCUMENTATION.md mismatches:** it names the spike column `Standardized_Spikes_New` / `_in_Delay` (232), but the code uses `Standardized_Spikes` throughout. It also states the firing-rate rule for labelling, which the code does not follow.
- **Hard-coded numbers:** subject 14 (4a, 6i-l), subject 1 (6e,f), neuron list (4a), ylim, chance level 20%.
- **Seeds:** 5 (with sha256), 17, 42.
- **Shipped intermediates that cannot be recomputed without MATLAB and spike input:**
  - `Cell_metrics.xlsx`: R2, tau_rise, Decay, acg_norm, Burst, CV2, firing_rate, Signi, subject_id, Neuron_ID_3.
  - `acg.mat`, `validation_data.xlsx`, `decay_constant_change.xlsx`.
  - Because `spikes_struct.mat` is empty, every ACG/R²-dependent result (Fig 4b-k, 5, 6) rests on `Cell_metrics.xlsx` rather than on recomputation from the dataset.

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint; ls -la data/cell_analysis/; cat .gitattributes 2>/dev/null; sed -n 70,110p 04_concept_cells.py; sed -n 240,260p "04_bursting/main_4c,d,6a,b.py"; sed -n 10,50p 07_spectral_clustering.py; sed -n 90,125p "04_bursting/main_4c,d,6a,b.py"
```

```
total 1380
drwxr-xr-x 2 runner runner    4096 Nov 10 04:44 .
drwxr-xr-x 4 runner runner    4096 Nov 10 04:44 ..
-rw-r--r-- 1 runner runner  125207 Nov 10 04:44 Cell_metrics.xlsx
-rw-r--r-- 1 runner runner     288 Nov 10 04:44 Mean_ACG.m
-rw-r--r-- 1 runner runner 1203191 Nov 10 04:44 acg.mat
-rw-r--r-- 1 runner runner    3564 Nov 10 04:44 calc_ACG_metrics.m
-rw-r--r-- 1 runner runner    9424 Nov 10 04:44 decay_constant_change.xlsx
-rw-r--r-- 1 runner runner    8079 Nov 10 04:44 fit_ACG.m
-rw-r--r-- 1 runner runner     988 Nov 10 04:44 normalize_acg_to_unit.m
-rw-r--r-- 1 runner runner       2 Nov 10 04:44 spikes_struct.mat
-rw-r--r-- 1 runner runner   36479 Nov 10 04:44 validation_data.xlsx
                'cat_2nd': res[5]
            })
    return pd.DataFrame(results)

df_top_2 = extract_top_two_categories(df)

def resampling(arr1, arr2, iteration=1000):
    min_len = min(len(arr1), len(arr2))
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
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
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[6000:])"; grep -n "^dataset:\|^paper:" claims/kyzar-2024.yaml claims/daume-2024.yaml | head; head -5 claims/zhong-2026.yaml; grep -n "^[a-z]" claims/zhong-2026.yaml
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
[... 146 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,120p claims/zhong-2026.yaml
```

```
# Claims for Zhong, Katkov & Tsodyks (2026), "Synaptic Theory of Chunking in Working Memory",
# eLife, doi:10.7554/elife.109538, tested on DANDI:000207.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
#
# Text read. paper/10.7554-elife.109538.txt, fetched from eLife's site. Its header says
# "version of record", but the page it holds is the eLife Reviewed Preprint version 1
# (doi:10.7554/eLife.109538.1, 9 January 2026, "Not revised"). It holds the main text, the
# Methods (sections A to E), the legends of Figures 1 to 4 and of the supplementary Figures S1
# to S3, and the Data availability statement. No PDF was supplied. The equations (1) to (15)
# and the values of Table I (simulation parameters) did not survive extraction; Eq. (1) is
# known from the text as M* = 2^(C-1) ("M ∗ = 24−1 = 8" for C = 4, and "M ∗ = 2C−1" in the
# Figure 4 legend, superscripts lost). Figure axes and plotted values could not be read.
#
# Code. The paper links none. Data availability says "The code for simulation will be made
# available in a Github repository at a later stage"; no analysis code for Figure 3 or Figure 4
# is named. No repository or commit was read.
#
# Data the paper used.
# - Figures 1, 2 and S1, S2 are numerical simulations of the rate model of Methods A, with the
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint; grep -n "n_components\|transform\|pdist\|'s'\]\|\[:5\]\|0:5\|range(5)" "03_dpca/main_3d,supp_2a,b,i.py" | head -20; grep -n "kruskal\|posthoc" "03_dpca/main_3d,supp_2a,b,i.py" "03_dpca/main_3h,supp_2c,d,l.py"; sed -n 40,70p "03_dpca/main_3d,supp_2a,b,i.py"
```

```
9:from scipy.spatial.distance import pdist
68:        return pdist(stim_means, metric="euclidean")    
106:        # trial averages (for dPCA fit/transform) 
122:        Z_enc_train = dpca_enc.fit_transform(RD_enc_train, trialX_enc_train)
123:        Z_enc_test  = dpca_enc.transform(RD_enc_test)
124:        Z_maint_test_on_enc = dpca_enc.transform(RD_maint_test)
131:        Z_maint_train = dpca_maint.fit_transform(RD_maint_train, trialX_maint_train)
132:        Z_maint_test  = dpca_maint.transform(RD_maint_test)
03_dpca/main_3d,supp_2a,b,i.py:11:import scikit_posthocs as sp
03_dpca/main_3d,supp_2a,b,i.py:152:    H_kw, kw_p = sps.kruskal(*box_datas)
03_dpca/main_3d,supp_2a,b,i.py:158:        dunn_df = sp.posthoc_dunn(mat, p_adjust="fdr_bh")
03_dpca/main_3h,supp_2c,d,l.py:11:import scikit_posthocs as sp
03_dpca/main_3h,supp_2c,d,l.py:146:    H_kw, kw_p = sps.kruskal(*box_datas)
03_dpca/main_3h,supp_2c,d,l.py:152:        dunn_df = sp.posthoc_dunn(mat, p_adjust="fdr_bh")

    np.random.seed(random_seed)

    n_reps, n_neurons, n_stimuli, _ = trialE.shape
    n_train = n_reps // 2         # e.g. 3
    n_test  = n_reps - n_train     # e.g. 3
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint; grep -n "selected_dpcs\|stim_indices\|n_components\|box_datas\|mean(" "03_dpca/main_3d,supp_2a,b,i.py" | head; grep -n "mean\|median" "05_cell_analysis/main_5d-h.py" | head
```

```
26:        selected_dpcs=(0, 1, 2, 3, 4),
27:        stim_indices=(0, 1, 2, 3, 4),
57:        m = np.mean(x.reshape(x.shape[0], -1), axis=1, keepdims=True)
64:        for s in stim_indices:
65:            traj = Z_epoch["s"][selected_dpcs, s, :]    # (n_dpcs, time)
66:            stim_means.append(np.mean(traj, axis=1))    # (n_dpcs,)
79:        for s in stim_indices:
94:        for s_idx, stim in enumerate(stim_indices):
107:        RD_enc_train   = np.mean(trialX_enc_train,   axis=0)
108:        RD_enc_test    = np.mean(trialX_enc_test,    axis=0)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd /tmp/claude-1001/hwm-preprint; sed -n 140,160p "03_dpca/main_3d,supp_2a,b,i.py"; sed -n 30,70p "05_cell_analysis/main_5d-h.py"
```

```
all_dists["Maint_test"].append(stim_dist(Z_maint_test))
        all_dists["Maint onto Enc"].append(stim_dist(Z_maint_test_on_enc))

    assert len(set(split_signatures)) == n_iter, "Duplicate splits detected!"

    # STATISTICS  (KW + Dunn)
    measure_dict = {k: np.stack(v) for k, v in all_dists.items()}  # (n_iter, n_pairs)

    # one scalar per split/epoch: mean of all pair-wise distances
    box_datas = [measure_dict[ep].mean(axis=1) for ep in epochs]  

    # 1 ) Kruskal-Wallis
    H_kw, kw_p = sps.kruskal(*box_datas)
    print(f"\nKruskal–Wallis  H = {H_kw:.4f},   p = {kw_p:.4g}")

    # 2 ) Dunn post-hoc  (only if omnibus is significant)
    if kw_p < 0.05:
        mat = np.vstack(box_datas)                      
        dunn_df = sp.posthoc_dunn(mat, p_adjust="fdr_bh")
        dunn_df.index = epochs
[... 43 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/kussovska-2025.yaml",
 "content": "# Claims for Kussovska, Kim & Rungratsameetaweemana (2025), \"Neural heterogeneity shapes the\n# temporal structure of human working memory\", bioRxiv, doi:10.1101/2025.10.31.684900, tested on\n# DANDI:000469 (reused; the paper analyses the dataset of Kyzar et al. 2024, ref. 59).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"),\n# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.\n#\n# Text read. paper/10.1101-2025.10.31.684900.txt, the bioRxiv full-text page of the preprint\n# posted 1 November 2025 (its header says \"version of record\"; the page says \"New Results\" and\n# offers a \"current version\", so a later version may exist; it was not read). It holds the\n# abstract, Introduction, Results, legends of Figures 1 to 6, Discussion, Methods, Data and Code\n# availability and references. No PDF was supplied. The Extended Data figures (Extended Data\n# Figs 1 to 5, behind \"Supplementary Material\") and their legends are not in the text read; the\n# Source Data are not either. The main findings are all stated in the main text and legends, so\n# claims were written; claims on Extended Data panels rest on the main-text sentences that cite\n# them, and their sources say \"(not in the text read)\". Several equations of the Methods (the GLM\n# link, the local-peak and prominence formulas of Burst detection) were lost in extraction.\n#\n# Code read. github.com/dariakussovska/heterogeneitywm at commit 5144fe8 (2025-10-26), the last\n# commit before the preprint was posted. Later commits (REVISIONS/ and R2_REVISIONS/, 2026) are\n# for a revised version and were not used. The repository holds Python scripts named by figure\n# panel (01_task, 02_psth_decoding, 03_dpca, 04_bursting, 05_cell_analysis, 06_cell_specific),\n# pipeline scripts 01 to 08 (extraction from the NWB files, standardisation, concept cells,\n# spectral clustering, dPCA matrices), MATLAB functions for the autocorrelograms and the\n# CellExplorer fit (data/cell_analysis/calc_ACG_metrics.m, fit_ACG.m, Mean_ACG.m,\n# normalize_acg_to_unit.m), and shipped intermediate tables. Facts about the code that bear on\n# every claim:\n# - The code reads only the Sternberg file of each subject (sub-<n>/sub-<n>_ses-2_ecephys+image.nwb,\n#   01_data_extraction.py:417), and its README downloads dandiset version 0.240123.1806, while\n#   the paper cites version 0.231213.2047 (Methods, Participants; Data availability).\n# - The matched trial sets of the Methods (96 trials per participant matched on load; 75 per\n#   participant matched on stimulus identity) come only from the shipped tables\n#   data/new_trial_info.xlsx (new_trial_id) and data/new_trial_final.xlsx (trial_id_final),\n#   merged at 03_standardization.py:97-121 and 232-261. No script builds them, and the paper\n#   does not say how the trials were chosen. Pseudo-population analyses align every\n#   participant's neurons on these ids and take the trial labels of one participant (subject 1\n#   for the GLM, main_1e,f.py:9; subject 14 for decoding and dPCA, main_2d,supp_1d,e.py:11-12,\n#   08_dpca_matrices.py:15-26).\n# - The ACG features (R2, tau_rise, tau_decay, mean normalised ACG, burst index) are computed in\n#   MATLAB with CellExplorer; the spike input data/cell_analysis/spikes_struct.mat is an empty\n#   2-byte placeholder, and the Python scripts read the outputs from the shipped\n#   data/cell_analysis/Cell_metrics.xlsx. They can be recomputed from the dataset's spike times\n#   with the MATLAB functions (or a port of them); the shipped table is outside data.\n# - The concept-cell bootstrap (04_concept_cells.py:76-90) has no random seed.\n#\n# Data the paper used (as the paper reports it). 21 patients with intractable epilepsy, 41\n# recording sessions (age 17 to 71), microwires in hybrid depth electrodes; 902 single units\n# sorted with OSort, in amygdala (259), hippocampus (190), dACC (171), preSMA (250) and vmPFC\n# (32). Task: a modified Sternberg task. Each trial is fixation (900 to 1000 ms), encoding of 1\n# to 3 images (load 1 to 3) from a participant-specific set of five images, maintenance of 2.5\n# to 2.8 s (\"hold\"), and a probe with a yes/no (old/new) button response; reaction time is from\n# probe onset to button press. Sixteen participants completed 135 trials and five completed\n# 108. Measured variables used: spike times per unit and the unit's brain area; per trial the\n# load, the image identity of each encoding period and of the probe, whether the probe was in\n# memory, response accuracy, and the timestamps of fixation, encodings, maintenance, probe and\n# response. MTL is amygdala and hippocampus combined (Results, paragraph on Fig. 2e). Unless a\n# claim says otherwise, main-figure analyses use load 1 trials (Methods, Statistical analyses).\n# The rodent validation of the cell-type classifier uses the CellExplorer ground-truth dataset\n# (ref. 72), which is not in DANDI:000469.\nschema_version: 2\npaper: doi:10.1101/2025.10.31.684900\nclaims:\n- id: units-by-region\n  statement: Recordings from the 21 patients yielded 902 well-isolated units, 259 in the amygdala,\n    171 in the dACC, 190 in the hippocampus, 250 in the preSMA and 32 in the vmPFC.\n  source: Results, Behavior and single-neuron recordings in a working memory task, paragraph 1;\n    Figure 1i; Methods, Electrophysiology, paragraph 2\n  quote: Recordings from the 21 patients yielded 902 well-isolated units (Fig. 1b,i), distributed\n    across the amygdala (AMY; 259 neurons), dorsal anterior cingulate cortex (dACC; 171 neurons),\n    hippocampus (HPC; 190 neurons), presupplementary motor area (preSMA; 250 neurons), and\n    ventromedial prefrontal cortex (vmPFC; 32 neurons).\n  expected:\n  - quantity: units\n    value: 902\n    tolerance: 0\n  - quantity: amygdala units\n    value: 259\n    tolerance: 0\n  - quantity: dACC units\n    value: 171\n    tolerance: 0\n  - quantity: hippocampus units\n    value: 190\n    tolerance: 0\n  - quantity: preSMA units\n    value: 250\n    tolerance: 0\n  - quantity: vmPFC units\n    value: 32\n    tolerance: 0\n  - quantity: patients\n    value: 21\n    tolerance: 0\n  criterion: Counted over the units of the 21 Sternberg sessions, left and right hemispheres of\n    each region merged (as main_1e,f.py:87-104 merges the location labels). Counts are exact,\n    so the tolerance is zero.\n- id: behavior-accuracy\n  statement: Task accuracy was 88.73% ± 1.25%.\n  source: Results, Behavior and single-neuron recordings in a working memory task, paragraph 2;\n    Extended Data Fig. 1a (not in the text read)\n  quote: Task accuracy was 88.73% ± 1.25%\n  expected:\n    quantity: task accuracy\n    value: 88.73\n    tolerance: 1.25\n    unit: percent\n  criterion: Accuracy is the fraction of correct responses over all trials of a participant,\n    averaged over the 21 participants, as 01_task/supp_1a.py:9-17 computes it (mean and s.e.m.\n    across subjects). The tolerance is the paper's stated spread. The spread is printed as ±;\n    Methods, Statistical analyses say descriptive values are mean ± s.d., while the code computes\n    s.e.m.; the spread is reported both ways and does not decide the claim. A second reading,\n    correct trials over all trials pooled across participants, is shown as a variant.\n- id: fig1c-accuracy-load1-vs-load3\n  statement: Accuracy was higher for load 1 than for load 3 trials across patients.\n  source: Results, Behavior and single-neuron recordings in a working memory task, paragraph 2;\n    Figure 1c\n  quote: Task accuracy was 88.73% ± 1.25% and was higher for load 1 than for load 3 (Wilcoxon\n    rank-sum, P = 0.027; Fig. 1c).\n  statistics:\n  - test: Wilcoxon rank-sum\n    p: 0.027\n    n: 21 patients\n  criterion: Per patient, the accuracy at each load; load 1 against load 3 with a two-sided\n    Wilcoxon rank-sum (Mann-Whitney) test, as in 01_task/main_1c.py:16-36. The code runs a\n    Kruskal-Wallis test over the three loads and then pairwise rank-sum tests with a Bonferroni\n    factor of 3 and prints both raw and corrected p; the paper does not say which it reports.\n    Readings are (a) the raw p and (b) the Bonferroni-corrected p. Reproduced when load 1\n    accuracy is higher and p < 0.05 under one reading; the value of p under both is reported.\n    A paired signed-rank test across patients is shown as a variant.\n- id: behavior-rt\n  statement: Reaction time for correct trials was 1.06 ± 0.28 s.\n  source: Results, Behavior and single-neuron recordings in a working memory task, paragraph 2;\n    Figure 1d\n  quote: Reaction time for correct trials was 1.06 ± 0.28 s.\n  expected:\n    quantity: reaction time, correct trials\n    value: 1.06\n    tolerance: 0.28\n    unit: s\n  criterion: Reaction time is probe onset to button press (Methods, Psychophysical task), the\n    probe interval of the trials table as in 01_data_extraction.py:304-309 and main_1d.py:6-8.\n    No code computes the reported value, and Methods, Statistical analyses say RTs are reported\n    as median with IQR while the Results print a ±. Readings are (a) the mean across\n    participants of each participant's median RT on correct trials (main_1d.py takes the median\n    per subject); (b) the mean across participants of each participant's mean RT; (c) the median\n    over all correct trials pooled. The tolerance is the paper's stated spread. Reproduced when\n    one reading falls within it; the spread under each reading (s.d., and half the IQR) is\n    reported.\n- id: rt-in-vs-out-memory\n  statement: Reaction time was faster for probes held in memory than for probes not in memory.\n  source: Results, Behavior and single-neuron recordings in a working memory task, paragraph 2\n  quote: Reaction time was faster for probes held in memory than for probes not in memory\n    (permutation test, P = 0.001)\n  statistics:\n  - test: permutation test\n    p: 0.001\n  criterion: No code in the repository computes this test, and the paper names only a\n    permutation test (1,000 shuffles unless stated, Methods, Statistical analyses; two-sided by\n    default). Which trials enter (correct trials, as for the RT above, or all trials) and what\n    is permuted are open. Readings are (a) a paired permutation (sign flips, 1,000) of the\n    per-participant difference in median RT between in-memory and not-in-memory probes; (b) a\n    permutation of the in/out labels over all trials pooled, on the difference in mean RT;\n    each on correct trials and on all trials. Reproduced when in-memory probes are faster and\n    p < 0.05 under one reading.\n- id: rt-correct-vs-incorrect\n  statement: Correct decisions were faster than incorrect ones.\n  source: Results, Behavior and single-neuron recordings in a working memory task, paragraph 2\n  quote: correct decisions were faster than incorrect ones (permutation test, P = 0.002)\n  statistics:\n  - test: permutation test\n    p: 0.002\n  criterion: No code computes this test. Readings are (a) a paired permutation (sign flips,\n    1,000) of the per-participant difference in median RT between correct and incorrect trials,\n    over participants with incorrect trials; (b) a permutation of the correct/incorrect labels\n    over all trials pooled, on the difference in mean RT. Reproduced when correct trials are\n    faster and p < 0.05 under one reading.\n- id: fig1e-load-modulated-neurons\n  statement: During maintenance a significant proportion of neurons in the preSMA (19.6%), vmPFC\n    (18.75%) and dACC (10.53%) was modulated by memory load.\n  source: Results, Behavior and single-neuron recordings in a working memory task, paragraph 3;\n    Figure 1e\n  quote: During the maintenance epoch, the preSMA, vmPFC, and dACC showed a significant\n    proportion of neurons modulated by memory load (preSMA, 19.6%, vmPFC, 18.75%, dACC, 10.53%;\n    permutation test, PpreSMA = 0.001, PvmPFC = 0.009, and PdACC = 0.026; Fig. 1e).\n  statistics:\n  - about: preSMA\n    test: permutation test on the count of significant neurons\n    p: 0.001\n    n: 250 neurons\n  - about: vmPFC\n    test: permutation test on the count of significant neurons\n    p: 0.009\n    n: 32 neurons\n  - about: dACC\n    test: permutation test on the count of significant neurons\n    p: 0.026\n    n: 171 neurons\n  expected:\n  - quantity: preSMA load-modulated neurons\n    value: 19.6\n    tolerance: 1.96\n    unit: percent\n  - quantity: vmPFC load-modulated neurons\n    value: 18.75\n    tolerance: 1.875\n    unit: percent\n  - quantity: dACC load-modulated neurons\n    value: 10.53\n    tolerance: 1.053\n    unit: percent\n  criterion: From the Methods (GLM encoding analysis) and 01_task/main_1e,f.py. For each neuron\n    the spike count in the first 2.5 s of maintenance (main_1e,f.py:67-75) on each trial is the\n    response of a Poisson GLM with log link on z-scored load (sklearn PoissonRegressor, alpha 0,\n    main_1e,f.py:147). A neuron is significant when |beta1| is at or above the 95th percentile\n    of its null from 1,000 permutations of the predictor (seed 17 in the code); a region's p is\n    the fraction of null counts of significant neurons at or above the observed count. Open\n    details, with the readings run. Trials: the Methods say \"96 trials per participant matched\n    on load\" and also \"load 1 encoding and maintenance epochs\", which cannot hold for a load\n    predictor; readings are (a) the code's 96 load-matched trials of data/new_trial_info.xlsx\n    (an input from the code repository), (b) all trials of each participant. Permutation:\n    within participant (Methods) or over the shared trial vector (the code, whose blocks are\n    None, main_1e,f.py:124-135); both are run. Correction: the code applies none across\n    regions; the paper's P values are taken as uncorrected. Reproduced when, under one\n    reading, each of the three regions is within tolerance and has p < 0.05.\n- id: fig1f-rt-modulation-not-significant\n  statement: No region had a significant proportion of neurons whose maintenance firing\n    covaried with reaction time after correction, although the amygdala (5.79%), preSMA (8.00%)\n    and vmPFC (6.25%) showed elevated percentages.\n  source: Results, Behavior and single-neuron recordings in a working memory task, paragraph 3;\n    Figure 1f\n  quote: Although elevated percentages of RT-modulated neurons were observed in the amygdala\n    (5.79%), preSMA (8.00%), and vmPFC (6.25%), none were significant after correction for\n    multiple comparisons (permutation tests, P > 0.05; Fig. 1f).\n  statistics:\n  - test: permutation test on the count of significant neurons\n    p: 0.05\n    p_relation: \">\"\n    corrected: correction for multiple comparisons (FDR, Methods, Statistical analyses)\n  expected:\n  - quantity: amygdala RT-modulated neurons\n    value: 5.79\n    tolerance: 0.579\n    unit: percent\n  - quantity: preSMA RT-modulated neurons\n    value: 8.0\n    tolerance: 0.8\n    unit: percent\n  - quantity: vmPFC RT-modulated neurons\n    value: 6.25\n    tolerance: 0.625\n    unit: percent\n  criterion: A claim of absence, on the paper's test, the GLM and count permutation of\n    fig1e-load-modulated-neurons with RT as the predictor, and Benjamini-Hochberg FDR over the\n    five regions at 0.05 (Methods, Statistical analyses name BH-FDR for multiple comparisons).\n    Reproduced when no region has corrected p < 0.05; not reproduced when one does. RT is each\n    trial's own reaction time in its participant (the code uses subject 1's RT vector for every\n    neuron, main_1e,f.py:113; shown as a variant). The trial readings of\n    fig1e-load-modulated-neurons apply to the expected percentages; uncorrected p values are\n    reported.\n- id: concept-cells-count\n  statement: Of 902 neurons, 58 (6.4%) were concept cells, 4 ± 4 across participants, 70.69% of\n    them in the amygdala, 18.96% in the hippocampus, 1.72% in the dACC, 3.45% in the preSMA and\n    5.15% in the vmPFC.\n  source: Results, Concept cell definition and criteria, paragraphs 1 and 2; Figure 1j; Methods,\n    Identification of concept cells\n  quote: Of 902 neurons (Fig. 1i), 58 were identified as concept cells (6.4%; 4 ± 4 across\n    participants). Of these 58 concept cells, 70.69% were in the AMY, 18.96% in the HPC, 1.72% in\n    the dACC, 3.45% in the preSMA, and 5.15% in the vmPFC (Fig. 1j).\n  expected:\n  - quantity: concept cells\n    value: 58\n    tolerance: 5.8\n  - quantity: concept cells in the amygdala\n    value: 70.69\n    tolerance: 7.069\n    unit: percent\n  - quantity: concept cells in the hippocampus\n    value: 18.96\n    tolerance: 1.896\n    unit: percent\n  criterion: From the Methods (Identification of concept cells) and 04_concept_cells.py. For each\n    neuron, spike counts 200 to 1000 ms after the onset of the first encoding image, on all\n    trials of all loads; the two images with the highest mean rate; a bootstrap of the\n    difference in mean rate between them (1,000 resamples with replacement), two-tailed p as\n    twice the smaller tail; concept cell when p < 0.05 and both images have more than one\n    trial. The code differs from the Methods in two ways, run as readings, (a) the Methods,\n    each image's trials resampled to their own number; (b) the code, both resampled to the\n    smaller number and p as the minimum of the four terms at 04_concept_cells.py:86-90. The\n    code sets no seed, so each reading is run with ten seeds and the range of counts reported.\n    Reproduced when, under one reading, the count is within tolerance and the amygdala is the\n    region with most concept cells, with the two largest shares within tolerance. The small\n    shares (one to three cells) and the per-participant 4 ± 4 are reported without deciding.\n- id: fig2ab-single-cells-not-persistent\n  statement: Examined neuron by neuron, most concept cells did not maintain elevated firing for\n    their preferred image throughout the maintenance epoch.\n  source: Results, Persistent activity during maintenance emerges with population pooling and\n    coarse temporal binning, paragraph 2; Figure 2a,b\n  quote: Neuron-by-neuron examination showed that most concept cells did not maintain elevated\n    firing throughout the maintenance epoch (Fig. 2a–b).\n  depends_on:\n  - concept-cells-count\n  criterion: The paper shows one example cell and gives no rule for \"throughout\". From the\n    Fig. 2a legend and Methods, Electrophysiology, per concept cell, load 1 trials, firing in 50\n    ms bins of maintenance z-scored to fixation and smoothed (Gaussian, sigma one bin), preferred\n    (first encoding image is the preferred image) against nonpreferred trials, with a\n    permutation test per bin at P < 0.05. The rule for \"elevated throughout\" is open; readings\n    are (a) significantly higher on preferred trials in at least half of the bins of the first\n    2.5 s of maintenance; (b) significantly higher spike count on preferred trials in each of\n    the three 1 s windows from maintenance onset (M1 to M3 as in Burst detection; M3 truncated\n    at the end of maintenance), permutation test of counts, P < 0.05. Reproduced when, under one\n    reading, more than half of the concept cells are not persistent; the counts under both are\n    reported.\n- id: fig2c-population-persistence\n  statement: Averaged across the 58 concept cells, firing on preferred trials stayed higher than\n    on nonpreferred trials across the maintenance epoch of load 1 trials, a pattern of persistent\n    activity.\n  source: Results, Persistent activity during maintenance emerges with population pooling and\n    coarse temporal binning, paragraph 2; Figure 2c and legend\n  quote: By contrast, averaging across the concept cell population revealed a clear pattern of\n    persistent activity (n = 58; Fig. 2c).\n  statistics:\n  - test: bootstrap test per time bin\n    p: 0.05\n    p_relation: \"<\"\n    n: 58 concept cells\n  depends_on:\n  - concept-cells-count\n  criterion: From the Fig. 2c legend and 02_psth_decoding/main_2c,5k,l,supp_1b,c.py. Load 1\n    trials; per concept cell the trial-mean rate in 50 ms bins of maintenance (aligned to its\n    onset), z-scored with the cell's fixation mean and s.d. and smoothed (Gaussian, sigma one\n    bin); preferred trials are those whose first encoding image is the cell's preferred image,\n    nonpreferred all others (06_add_category.py:24-25). Per bin, a bootstrap over cells (1,000,\n    paired resampling of cells, seed 42) of the preferred minus nonpreferred mean, two-sided,\n    with BH-FDR over all bins of all panels as in the code (lines 196-286); per-panel FDR is\n    shown as a variant. What counts as persistent is open; readings are (a) significant bins\n    cover at least half of the first 2.5 s of maintenance; (b) every 500 ms segment of the first\n    2.5 s holds a significant bin. Reproduced when the mean preferred trace is above the\n    nonpreferred one and the rule holds under one reading.\n- id: ext1bc-persistence-by-load\n  statement: The population-level persistence of concept cells was robust at loads 1 and 2 and\n    attenuated at load 3.\n  source: Results, Persistent activity during maintenance emerges with population pooling and\n    coarse temporal binning, paragraph 2; Extended Data Fig. 1b,c (not in the text read)\n  quote: This effect was robust at loads 1 and 2, and attenuated at load 3 (Extended Data Fig.\n    1b–c).\n  depends_on:\n  - fig2c-population-persistence\n  criterion: The analysis of fig2c-population-persistence for load 2 and load 3 trials, with a\n    trial preferred when any encoded image is the preferred image (06_add_category.py:96-125).\n    The Extended Data legends are not in the text read, so the measure is open; it is the\n    fraction of maintenance bins (first 2.5 s) with a significant preferred-over-nonpreferred\n    difference. Reproduced when loads 1 and 2 meet a reading of fig2c-population-persistence\n    and load 3 has a smaller fraction of significant bins than either.\n- id: fig2d-cross-temporal-localized\n  statement: In load 1 trials, decoders trained at specific times of encoding or early\n    maintenance classified the image above chance at other times, but cross-time generalization\n    clusters were sparse and temporally localized, so the information was not stably held across\n    maintenance.\n  source: Results, Persistent activity during maintenance emerges with population pooling and\n    coarse temporal binning, paragraph 3; Figure 2d and legend; Methods, Population decoding\n    analysis, paragraph 2\n  quote: However, cross-time generalization clusters were sparse and temporally localized,\n    indicating that the stimulus-specific information was not stably maintained across the\n    maintenance epoch but re-emerged at specific moments (Fig. 2d).\n  statistics:\n  - test: binomial test per train-test bin pair, FDR, cluster-duration permutation null\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - concept-cells-count\n  criterion: From the Methods and 02_psth_decoding/main_2d,supp_1d,e.py. A pseudo-population of\n    all concept cells, trials aligned across participants on the 75 identity-matched trials\n    (data/new_trial_final.xlsx of the code; how they were chosen is not stated), load 1 trials,\n    labels the first encoding image (five classes). Spike counts in 250 ms windows stepped by\n    100 ms from first-encoding onset through encoding, maintenance and probe, z-scored with\n    fixation; a linear SVM (sklearn SVC, linear kernel, C = 1; the Methods name the Neural\n    Decoding Toolbox with LIBSVM) trained at each bin and tested at every bin with LOOCV. Per\n    pair a binomial test against 20% with BH-FDR over the grid. Open, the sidedness of the\n    binomial test (two-sided in Methods, Population decoding; one-sided in Methods, Statistical\n    analyses and in the code) and the cluster rule (a 95th-percentile cluster-duration null from\n    1,000 label shuffles in the Methods; contours longer than 13 points in the code, lines\n    175-178). Both sidedness readings and both cluster rules are run. Reproduced when, under one\n    reading, above-chance clusters exist for training bins in encoding or early maintenance, and\n    no training bin in maintenance generalizes above chance to more than half of the maintenance\n    test bins.\n- id: ext1de-cross-temporal-load23\n  statement: In load 2 and load 3 trials cross-time generalization was minimal.\n  source: Results, Persistent activity during maintenance emerges with population pooling and\n    coarse temporal binning, paragraph 3; Extended Data Fig. 1d,e (not in the text read)\n  quote: In load 2 and load 3 trials, cross-time generalization was minimal, suggesting that\n    higher memory load further fragments or destabilizes these representations (Extended Data\n    Fig. 1d–e).\n  depends_on:\n  - fig2d-cross-temporal-localized\n  criterion: The analysis of fig2d-cross-temporal-localized on load 2 and load 3 trials. The label\n    is the first encoding image (Methods) or the last (the code, main_2d,supp_1d,e.py:147-152);\n    both are run. \"Minimal\" is open; it is read as fewer off-diagonal train-test pairs in\n    surviving clusters than at load 1, under the same cluster rule. Reproduced when both loads\n    have fewer than load 1 under one label reading.\n- id: fig2e-maintenance-decoding-amy-mtl\n  statement: Concept cells in the amygdala and in the MTL carried significant stimulus\n    information during load 1 maintenance (35.56% and 32.13% decoding accuracy, chance 20%).\n  source: Results, Persistent activity during maintenance emerges with population pooling and\n    coarse temporal binning, paragraph 4; Figure 2e\n  quote: concept cells in AMY and in the medial temporal lobe (MTL; AMY and HPC combined) carried\n    significant stimulus-relevant information during load 1 maintenance (AMY, 35.56% decoding\n    accuracy, P = 0.001; MTL, 32.13% decoding accuracy, P = 0.001; permutation test; Fig. 2e).\n  statistics:\n  - about: amygdala\n    test: permutation test\n    p: 0.001\n  - about: MTL\n    test: permutation test\n    p: 0.001\n  expected:\n  - quantity: amygdala decoding accuracy, load 1\n    value: 35.56\n    tolerance: 3.556\n    unit: percent\n  - quantity: MTL decoding accuracy, load 1\n    value: 32.13\n    tolerance: 3.213\n    unit: percent\n  depends_on:\n  - concept-cells-count\n  criterion: From the Results, Methods (Population decoding, paragraph 3) and\n    02_psth_decoding/main_2e,supp_1f.py. Within each participant, the participant's concept\n    cells in the region, all of its load 1 trials, labels the last (for load 1 the only) image;\n    features are spike counts in 1 s windows stepped by 250 ms over the first 2.5 s of\n    maintenance, all windows and cells concatenated (lines 24-27, 115-122); linear SVM, LOOCV;\n    accuracy is the mean over participants. p from 1,000 label shuffles, (count of null means at\n    or above the real + 1) / 1001, BH-FDR within the load over the region groups (lines\n    313-336). Open, the minimum number of concept cells per participant, at least three\n    (Methods) or more than three (the code, line 70); both are run. The Fig. 2e legend says\n    \"pooled across participants\" while the Results and code are within participant; a\n    pseudo-population variant is shown. Reproduced when, under one reading, both accuracies\n    are within tolerance and both p < 0.05.\n- id: ext1f-maintenance-decoding-load2\n  statement: Amygdala and MTL concept cells also carried significant information about the last\n    image during load 2 maintenance (23.56% and 28.89%).\n  source: Results, Persistent activity during maintenance emerges with population pooling and\n    coarse temporal binning, paragraph 4; Extended Data Fig. 1f (not in the text read)\n  quote: The same held for AMY and MTL concept cells at load 2 (AMY, 23.56%, P = 0.031; MTL,\n    28.89%, P = 0.002; permutation test; Extended Data Fig. 1f).\n  statistics:\n  - about: amygdala\n    test: permutation test\n    p: 0.031\n  - about: MTL\n    test: permutation test\n    p: 0.002\n  expected:\n  - quantity: amygdala decoding accuracy, load 2\n    value: 23.56\n    tolerance: 2.356\n    unit: percent\n  - quantity: MTL decoding accuracy, load 2\n    value: 28.89\n    tolerance: 2.889\n    unit: percent\n  depends_on:\n  - fig2e-maintenance-decoding-amy-mtl\n  criterion: As fig2e-maintenance-decoding-amy-mtl on load 2 trials, the label the second\n    encoding image (Results). Reproduced when, under one reading, both accuracies are within\n    tolerance and both p < 0.05.\n- id: fig2f-bin-width-decoding\n  statement: In load 1 trials, pseudo-population decoding of the image during maintenance was\n    above chance at every bin width and rose with bin width (250 ms 40.00%, 500 ms 56.67%, 750\n    ms 66.67%, 1000 ms 80.00%).\n  source: Results, Persistent activity during maintenance emerges with population pooling and\n    coarse temporal binning, paragraph 5; Figure 2f\n  quote: In load 1 trials, accuracy was above chance at all bin widths (250 ms, 40.00%; 500 ms,\n    56.67%; 750 ms, 66.67%; 1000 ms, 80.00%; permutation tests against shuffled controls, Pmax =\n    0.001) and increased nearly twofold as bin width increased.\n  statistics:\n  - test: permutation test against shuffled controls\n    p: 0.001\n    p_relation: \"=\"\n    corrected: FDR within each family (Methods, Population decoding)\n  expected:\n  - quantity: accuracy, 250 ms bins\n    value: 40.0\n    tolerance: 4.0\n    unit: percent\n  - quantity: accuracy, 500 ms bins\n    value: 56.67\n    tolerance: 5.667\n    unit: percent\n  - quantity: accuracy, 750 ms bins\n    value: 66.67\n    tolerance: 6.667\n    unit: percent\n  - quantity: accuracy, 1000 ms bins\n    value: 80.0\n    tolerance: 8.0\n    unit: percent\n  depends_on:\n  - concept-cells-count\n  criterion: From the Methods (Population decoding, paragraph 3) and\n    02_psth_decoding/main_2f,supp_1g.py. A pseudo-population of all concept cells, trials aligned\n    on the identity-matched trial ids, load 1 trials (the reported accuracies are multiples of\n    1/30, consistent with 30 trials), label the image; features are spike counts in windows of\n    the given width slid by 25 ms over the first 2.5 s of maintenance, z-scored with fixation,\n    all windows and cells concatenated (lines 118-139); linear SVM, LOOCV. p from 1,000 label\n    shuffles, (k + 1) / 1001, BH-FDR over the 12 tests of 4 widths and 3 loads (lines 186-192).\n    Open, the trial alignment; readings are (a) the code's data/new_trial_final.xlsx (an input\n    from the code repository), (b) for each participant the first six load 1 trials of each\n    image in trial order, aligned by image and rank (30 trials). Reproduced when, under one\n    reading, every accuracy is within tolerance, each p < 0.05 and accuracy rises from 250 to\n    1000 ms.\n- id: fig2f-bin-width-pairwise\n  statement: Pairwise, accuracy was higher for 750 than 250 ms, for 1000 than 250 ms and for 1000\n    than 500 ms bins, while 500 against 250, 1000 against 750 and 750 against 500 ms did not\n    differ after correction.\n  source: Results, Persistent activity during maintenance emerges with population pooling and\n    coarse temporal binning, paragraph 5; Figure 2f\n  quote: Pairwise comparisons across bin widths confirmed higher accuracies for 750 versus 250 ms\n    (66.67% vs. 40.00%, P = 0.026), 1000 versus 250 ms (80.00% vs. 40.00%, P = 0.004), and 1000\n    versus 500 ms (80.00% vs. 56.67%, P = 0.032), whereas differences for 500 versus 250 ms\n    (56.67% vs. 40.00%, P > 0.05), 1000 versus 750 ms (80.00% vs. 66.67%, P > 0.05), and 750\n    versus 500 ms (66.67% vs. 56.67%, P > 0.05) were not significant after correction\n    (permutation tests).\n  statistics:\n  - about: 750 against 250 ms\n    test: permutation test\n    p: 0.026\n  - about: 1000 against 250 ms\n    test: permutation test\n    p: 0.004\n  - about: 1000 against 500 ms\n    test: permutation test\n    p: 0.032\n  - about: 500 against 250, 1000 against 750, 750 against 500 ms\n    test: permutation test\n    p: 0.05\n    p_relation: \">\"\n    corrected: correction for multiple comparisons (FDR, Methods)\n  depends_on:\n  - fig2f-bin-width-decoding\n  criterion: No code in the repository computes these tests and the paper names only\n    permutation tests with FDR correction. Readings are (a) a paired permutation over trials,\n    swapping each trial's LOOCV correctness between the two widths (1,000 permutations), p\n    two-sided; (b) the observed accuracy difference against the distribution of differences\n    between the two widths' label-shuffled nulls (1,000); each with BH-FDR over the six pairs.\n    Reproduced when, under one reading, the three named pairs have corrected p < 0.05 and the\n    other three do not; partially reproduced when the three named pairs are significant and\n    another is too. The trial readings of fig2f-bin-width-decoding apply.\n- id: ext1g-bin-width-load2\n  statement: Bin width had little effect on decoding of the second image in load 2 trials, and\n    load 2 accuracy was lower than load 1 accuracy.\n  source: Results, Persistent activity during maintenance emerges with population pooling and\n    coarse temporal binning, paragraph 5; Extended Data Fig. 1g (not in the text read)\n  quote: Temporal bin width had little effect on decoding accuracy for the second image in load\n    2 trials. Decoding accuracy in load 2 was also lower than in load 1 (Extended Data Fig. 1g).\n  depends_on:\n  - fig2f-bin-width-decoding\n  criterion: The analysis of fig2f-bin-width-decoding on load 2 trials with the second image as\n    label (main_2f,supp_1g.py:98-109). \"Little effect\" is open; it is read as the range of the\n    four load 2 accuracies being less than half the load 1 range (40.0 points). Reproduced when\n    that holds and each load 2 accuracy is below the load 1 accuracy at the same width, under\n    one trial reading.\n- id: fig3abc-trajectory-complexity\n  statement: dPCA encoding trajectories of load 1 concept-cell activity made a single large\n    excursion in state space, while maintenance trajectories were more complex, with multiple\n    turns and changes in direction.\n  source: Results, Encoding and maintenance occupy distinct neural subspaces, paragraph 2;\n    Figure 3a-c\n  quote: Applying dPCA revealed simple encoding trajectories characterized by a single large\n    excursion in state space ... In contrast, maintenance trajectories were markedly more\n    complex, with multiple turns and changes in direction\n  depends_on:\n  - concept-cells-count\n  criterion: The dPCA fits of fig3d-encoding-vs-maintenance-separability. The paper gives no\n    measure of complexity; the figure is a visual reading. The measure is open; readings are\n    (a) tortuosity, the path length of each held-out stimulus trajectory in the first three\n    stimulus dPCs divided by the largest distance from its start point; (b) the number of\n    reversals of direction (sign changes of the derivative) summed over the first three\n    stimulus dPCs. Reproduced when, under one reading, the median over stimuli and resampling\n    splits is larger for maintenance than for encoding.\n- id: fig3d-encoding-vs-maintenance-separability\n  statement: Stimulus separation in dPCA space was higher during encoding than during\n    maintenance, and higher than maintenance activity projected into the encoding space, while\n    maintenance separation did not differ between its own space and the encoding space.\n  source: Results, Encoding and maintenance occupy distinct neural subspaces, paragraph 2;\n    Figure 3d\n  quote: Stimulus separation, quantified as the mean pairwise Euclidean distance between\n    condition-averaged trajectories in dPCA space, differed significantly across conditions\n    (Kruskal-Wallis, H = 457.217, P = 1.20 × 10−97). Separation in the encoding state space was\n    higher than during maintenance and higher than maintenance activity projected into the\n    encoding state space (Dunn's post hoc test, Penc vs. maint = 2.38 × 10−38, Penc vs.\n    projected maint = 1.25 × 10−29)\n  statistics:\n  - about: across conditions\n    test: Kruskal-Wallis\n    statistic: H = 457.217\n    p: 1.2e-97\n  - about: encoding against maintenance\n    test: Dunn's post hoc test\n    p: 2.38e-38\n    corrected: FDR\n  - about: encoding against maintenance projected into the encoding space\n    test: Dunn's post hoc test\n    p: 1.25e-29\n    corrected: FDR\n  - about: maintenance in its own space against maintenance in the encoding space\n    test: Dunn's post hoc test\n    p: 0.05\n    p_relation: \">\"\n    corrected: FDR\n  expected:\n    quantity: Kruskal-Wallis H\n    value: 457.217\n    tolerance: 45.72\n  depends_on:\n  - concept-cells-count\n  criterion: From the Methods (State-space analysis) and 08_dpca_matrices.py with\n    03_dpca/main_3d,supp_2a,b,i.py. All 58 concept cells, 30 load 1 trials (6 per image), spikes\n    in 2 ms bins, z-scored with fixation and smoothed with a Gaussian of 60 bins (120 ms;\n    Methods \"α = 60; bin width = 120 ms\" and the code agree, the Results \"σ = 60 ms\" is a\n    variant); encoding 0 to 1 s, maintenance 0 to 2.5 s. 100 stratified splits, 3 train and 3\n    test trials per image; dPCA (Kobak) with labels stimulus and time, regularizer chosen by\n    its cross-validation; per split the mean over the 10 image pairs of the Euclidean distance\n    between time-averaged held-out trajectories on the first five stimulus dPCs (lines 26-68).\n    Kruskal-Wallis then Dunn with BH-FDR (scikit-posthocs). Open, the groups of the\n    Kruskal-Wallis; the code has five (the three test conditions and the two training sets),\n    the Methods compare \"conditions\"; H = 457 exceeds what three groups of 100 can give, so the\n    five-group reading is the main one and three groups a variant. Open, the trials; the code\n    draws the 30 from subject 14's load-matched trial ids (random_state 42) and selects\n    maintenance trials by trial_id, not new_trial_id (08_dpca_matrices.py:192); readings are\n    (a) the same 30 trials for both epochs, (b) the code as written. Reproduced when, under one\n    reading, H is within tolerance, encoding is above both maintenance conditions with Dunn\n    corrected p < 0.05, and the two maintenance conditions do not differ (Dunn corrected p at\n    or above 0.05, the paper's test, judged as written).\n- id: fig3h-early-vs-late-maintenance\n  statement: Stimulus separation was higher in the first half of maintenance than in the second\n    half, and higher than second-half activity projected into the first-half space.\n  source: Results, Encoding and maintenance occupy distinct neural subspaces, paragraph 3;\n    Figure 3e-h\n  quote: stimulus separability was significantly higher in the early half than in the late half,\n    and higher than late-maintenance activity projected into the early-maintenance state space\n    (Kruskal-Wallis, H = 417.58, P = 4.43 × 10−89, Dunn's post hoc, Pearly vs. late = 9.70 ×\n    10−12, Pearly vs. late→early = 2.54 × 10−9; Fig. 3g–h)\n  statistics:\n  - about: across conditions\n    test: Kruskal-Wallis\n    statistic: H = 417.58\n    p: 4.43e-89\n  - about: early against late\n    test: Dunn's post hoc test\n    p: 9.7e-12\n    corrected: FDR\n  - about: early against late projected into the early space\n    test: Dunn's post hoc test\n    p: 2.54e-9\n    corrected: FDR\n  expected:\n    quantity: Kruskal-Wallis H\n    value: 417.58\n    tolerance: 41.76\n  depends_on:\n  - fig3d-encoding-vs-maintenance-separability\n  criterion: As fig3d-encoding-vs-maintenance-separability, with maintenance split at bin 624 of\n    1249 (about 1.25 s, 03_dpca/main_3h,supp_2c,d,l.py:22) into early and late halves, each with\n    its own dPCA fit, and late test data also projected into the early space. The code's\n    Kruskal-Wallis again takes five groups (train sets included). The code protects time in the\n    early fit (protect ['t']) and not in the late one (lines 115 and 124); both settings for\n    both halves are run as readings. Reproduced when, under one reading, H is within tolerance\n    and early separation exceeds both late conditions with Dunn corrected p < 0.05.\n- id: fig4c-encoding-bursts-vs-poisson\n  statement: During encoding, population bursting did not exceed a rate-matched Poisson null for\n    most neuronal groups; it differed from the null only for all neurons and for the low mean ACG\n    amplitude group.\n  source: Results, Bursting dynamics reorganize spiking activity between encoding and\n    maintenance, paragraph 2; Figure 4c\n  quote: During encoding, population bursting did not exceed a rate-matched Poisson null\n    (Wilcoxon signed-rank; Fig. 4c) for most neuronal groups. Significant effects were detected\n    for all neurons (W = 9.0, P = 0.003) and for the group with low mean ACG amplitude (W = 0.0,\n    P = 0.012).\n  statistics:\n  - about: all neurons\n    test: Wilcoxon signed-rank\n    statistic: W = 9.0\n    p: 0.003\n    corrected: FDR\n  - about: low mean ACG amplitude\n    test: Wilcoxon signed-rank\n    statistic: W = 0.0\n    p: 0.012\n    corrected: FDR\n  - about: high mean ACG, short and long tau decay, concept cells\n    test: Wilcoxon signed-rank\n    p: 0.05\n    p_relation: \">\"\n    corrected: FDR\n  depends_on:\n  - concept-cells-count\n  - acg-fit-yield\n  criterion: Burst detection from the Methods (Burst detection) and 04_bursting/main_4c,d,6a,b.py.\n    Within each participant and group, load 1 trials, the first encoding image (1 s per trial);\n    the group's spikes pooled and trials concatenated, binned at 70 ms and smoothed with a\n    Gaussian of sigma 40 ms; peaks at least 2 bins (140 ms) apart. Rate-matched Poisson\n    surrogates per neuron and trial (each trial's count as the rate, spike times uniform), 100\n    per participant and group, their mean burst count compared with the real count by a paired\n    two-sided Wilcoxon signed-rank test over participants, BH-FDR over the groups. Open details,\n    with readings run. Peak rule; (a) the smoothed value exceeds the 90th percentile of the\n    epoch's bins (Methods), (b) prominence at or above that percentile (Results, \"a\n    90th-percentile prominence threshold\", and the code, lines 251-255). Surrogate threshold;\n    the real data's (code) or each surrogate's own. Groups; (a) median split within participant\n    on mean ACG amplitude and on tau decay, participants with fewer than 5 neurons in a group\n    left out (Methods), (b) the code's 6 lowest and 6 highest of participants with at least 10\n    neurons (lines 52, 95-120, 164-172); groups use neurons with R2 > 0.3 (acg-fit-yield);\n    \"all neurons\" is all 902 (code, line 183) or the 294 fitted neurons; concept cells need at\n    least 3 per participant (code) or 5 (Methods). Reproduced when, under one reading, all\n    neurons and low ACG differ from the null with corrected p < 0.05 and the other four groups\n    do not; partially reproduced when the two named groups differ and one other does too.\n- id: fig4d-maintenance-bursts-vs-poisson\n  statement: During maintenance, bursting exceeded the Poisson null for all neurons pooled and\n    for the low and high mean ACG and short and long tau decay groups, but not for concept\n    cells.\n  source: Results, Bursting dynamics reorganize spiking activity between encoding and\n    maintenance, paragraph 3; Figure 4d\n  quote: During maintenance, bursting exceeded the Poisson null across most groups (Fig. 4d)\n  statistics:\n  - about: all neurons\n    test: Wilcoxon signed-rank\n    statistic: W = 0.0\n    p: 0.001\n    corrected: FDR\n  - about: low mean ACG\n    test: Wilcoxon signed-rank\n    statistic: W = 0.0\n    p: 0.004\n    corrected: FDR\n  - about: high mean ACG\n    test: Wilcoxon signed-rank\n    statistic: W = 0.0\n    p: 0.004\n    corrected: FDR\n  - about: short tau decay\n    test: Wilcoxon signed-rank\n    statistic: W = 4.0\n    p: 0.011\n    corrected: FDR\n  - about: long tau decay\n    test: Wilcoxon signed-rank\n    statistic: W = 0.0\n    p: 0.004\n    corrected: FDR\n  - about: concept cells\n    test: Wilcoxon signed-rank\n    statistic: W = 10.0\n    p: 0.05\n    p_relation: \">\"\n    corrected: FDR\n  depends_on:\n  - fig4c-encoding-bursts-vs-poisson\n  criterion: The method and readings of fig4c-encoding-bursts-vs-poisson on the maintenance\n    epoch of load 1 trials, each trial's window 2.8 s from maintenance onset (the code's\n    TRIAL_WIN for maintenance, line 13; the maintenance lasts 2.5 to 2.8 s, so the window is\n    also run as each trial's own maintenance). Reproduced when, under one reading, the five\n    named groups have more real than surrogate bursts in most participants with corrected\n    p < 0.05, and concept cells do not differ (the paper's test, judged as written).\n- id: fig4-acg-group-differences\n  statement: The low mean ACG group burst more than the high mean ACG group in both encoding and\n    maintenance, whereas the short tau decay group exceeded the long tau decay group only during\n    encoding.\n  source: Results, Bursting dynamics reorganize spiking activity between encoding and\n    maintenance, paragraph 4\n  quote: Specifically, the low mean ACG group showed greater bursting than the high mean ACG group\n    in both encoding (W = 0.0, P = 0.002) and maintenance (W = 0.0, P = 0.003), whereas the short\n    τdecay group exceeded the long τdecay group only during encoding (W = 3.5, P = 0.015).\n  statistics:\n  - about: low against high mean ACG, encoding\n    test: Wilcoxon signed-rank\n    statistic: W = 0.0\n    p: 0.002\n  - about: low against high mean ACG, maintenance\n    test: Wilcoxon signed-rank\n    statistic: W = 0.0\n    p: 0.003\n  - about: short against long tau decay, encoding\n    test: Wilcoxon signed-rank\n    statistic: W = 3.5\n    p: 0.015\n  depends_on:\n  - fig4c-encoding-bursts-vs-poisson\n  criterion: Real burst counts of fig4c-encoding-bursts-vs-poisson and\n    fig4d-maintenance-bursts-vs-poisson, compared between groups within participant by a paired\n    two-sided Wilcoxon signed-rank test; the code compares all 28 pairs of the 8 groups with\n    BH-FDR over them (main_4c,d,6a,b.py:482-518), shown as given and also with FDR over the four\n    tests named here. Reproduced when, under one reading of fig4c-encoding-bursts-vs-poisson,\n    low ACG exceeds high ACG in both epochs and short exceeds long tau decay in encoding with\n    p < 0.05, and short and long tau decay do not differ in maintenance.\n- id: fig4f-all-cells-epochs\n  statement: At the population level, load 1 burst rates increased from encoding to each of the\n    three 1 s maintenance windows and to the probe.\n  source: Results, Bursting dynamics reorganize spiking activity between encoding and\n    maintenance, paragraph 5; Figure 4f\n  quote: At the population level, burst rates increased from encoding to each maintenance window\n    (load 1; Wilcoxon signed-rank, Enc → M1, W = 1.0, P = 0.007; Enc → M2, W = 0.0, P = 0.005; Enc\n    → M3, W = 0.0, P = 0.005), as well as to probe (load 1; Wilcoxon signed-rank, Enc → Probe, W\n    = 4.0, P = 0.039).\n  statistics:\n  - about: encoding against M1\n    test: Wilcoxon signed-rank\n    statistic: W = 1.0\n    p: 0.007\n    corrected: FDR\n  - about: encoding against M2\n    test: Wilcoxon signed-rank\n    statistic: W = 0.0\n    p: 0.005\n    corrected: FDR\n  - about: encoding against M3\n    test: Wilcoxon signed-rank\n    statistic: W = 0.0\n    p: 0.005\n    corrected: FDR\n  - about: encoding against probe\n    test: Wilcoxon signed-rank\n    statistic: W = 4.0\n    p: 0.039\n    corrected: FDR\n  depends_on:\n  - fig4c-encoding-bursts-vs-poisson\n  criterion: Burst detection of fig4c-encoding-bursts-vs-poisson (its peak-rule readings),\n    within participant, on encoding (1 s), maintenance and probe (1 s, the code's window,\n    04_bursting/main_4f-k,6c,d.py:19-25). Open, how M1 to M3 are formed; readings are (a) the\n    Methods, three consecutive 1 s windows from each trial's maintenance onset, M3 ending at the\n    end of maintenance; (b) the code, peaks of the concatenated 3 s maintenance trains assigned\n    to thirds of the whole train (lines 216-219). Counts are per window; with 1 s windows count\n    and rate agree, and for a shorter M3 the rate per second is also reported. Open, the\n    population; all 902 neurons (as in fig4c) or the 294 fitted neurons (the code here, line 47).\n    Paired two-sided Wilcoxon signed-rank tests over participants with BH-FDR over the 10 pairs\n    of periods (line 289). Reproduced when, under one reading, each of the four comparisons\n    shows more bursts after encoding with corrected p < 0.05.\n- id: fig4hj-group-epochs\n  statement: The increase of bursting from encoding into maintenance was driven by neurons with\n    high mean ACG amplitude (also increasing to the probe) and neurons with a long tau decay,\n    while the low ACG, short tau decay and concept-cell groups showed no change across epochs.\n  source: Results, Bursting dynamics reorganize spiking activity between encoding and\n    maintenance, paragraph 5; Figure 4g-k\n  quote: Neurons with high mean ACG amplitude increased from encoding to maintenance and to the\n    probe period (Fig. 4h; Enc → M1, W = 1.0, P = 0.020; Enc → M2, W = 3.5, P = 0.020; Enc →\n    Probe, W = 1.0, P = 0.020), and and neurons with a long τdecay also increased from encoding to\n    maintenance (Fig. 4j; Enc → M1, W = 2.5, P = 0.033; Enc → M2, W = 2.0, P = 0.033; Enc → M3, W\n    = 3.0, P = 0.033). Other groups showed no change across epochs (Fig. 4g,i,k; Wilcoxon\n    signed-rank, P > 0.05).\n  statistics:\n  - about: high mean ACG, encoding against M1, M2 and probe\n    test: Wilcoxon signed-rank\n    p: 0.02\n    corrected: FDR\n  - about: long tau decay, encoding against M1, M2 and M3\n    test: Wilcoxon signed-rank\n    p: 0.033\n    corrected: FDR\n  - about: low mean ACG, short tau decay and concept cells, all epoch pairs\n    test: Wilcoxon signed-rank\n    p: 0.05\n    p_relation: \">\"\n    corrected: FDR\n  depends_on:\n  - fig4f-all-cells-epochs\n  criterion: The method and readings of fig4f-all-cells-epochs for each group, with the group\n    readings of fig4c-encoding-bursts-vs-poisson. Reproduced when, under one reading, high ACG\n    exceeds encoding at M1, M2 and probe and long tau decay at M1, M2 and M3 with corrected\n    p < 0.05, and the low ACG, short tau decay and concept-cell groups have no epoch pair with\n    corrected p < 0.05 (the paper's test for the absence). Partially reproduced when the\n    increases hold for one of the two groups.\n- id: ext2-bursts-loads23\n  statement: The patterns of burst rates across epochs held for loads 2 and 3.\n  source: Results, Bursting dynamics reorganize spiking activity between encoding and\n    maintenance, paragraph 5; Extended Data Fig. 2b-m (not in the text read)\n  quote: Similar patterns held for load 2 and load 3 (Extended Data Fig. 2b–m)\n  depends_on:\n  - fig4hj-group-epochs\n  criterion: The analyses of fig4f-all-cells-epochs and fig4hj-group-epochs on load 2 and load 3\n    trials, encoding taken from the last encoding image (the code, main_4f-k,6c,d.py:49). The\n    Extended Data legends are not in the text read, so \"similar\" is read as all cells and the\n    high ACG and long tau decay groups showing more bursts in each maintenance window than in\n    encoding, in the median over participants, at each load. Reproduced when that holds at both\n    loads under one reading; the tests are reported.\n- id: acg-fit-yield\n  statement: Fitting CellExplorer's triple-exponential model to each neuron's autocorrelogram and\n    keeping well-fit units (R2 > 0.3) left 294 neurons for cell-type analysis.\n  source: Results, Feature-based classification of putative cell types, paragraph 2; Methods,\n    Autocorrelogram-based characterization of single-neuron temporal dynamics\n  quote: For each neuron, we fit Cell Explorer's triple-exponential model [72] to its spike train\n    and retained well-fit units (R2 > 0.3), yielding 294 neurons for analysis.\n  expected:\n    quantity: neurons with ACG fit R2 above 0.3\n    value: 294\n    tolerance: 29.4\n  criterion: From the Methods and data/cell_analysis/calc_ACG_metrics.m and fit_ACG.m. Spikes of\n    all task epochs of each neuron aggregated; the narrow ACG within ±50 ms in 0.5 ms bins (201\n    bins), self-coincidences removed, divided by spike count and bin width; the raw narrow ACG\n    fitted at positive lags with the CellExplorer triple-exponential, start, lower and upper\n    bounds as in fit_ACG.m:19-21, by bounded nonlinear least squares; R2 the fit's\n    goodness-of-fit. Open, which spikes are \"all task epochs\"; readings are (a) every spike of\n    the unit in the session, (b) only spikes within the trial epochs (fixation to probe end).\n    The threshold is R2 > 0.3 (Results) or R2 >= 0.3 (07_spectral_clustering.py:16); both are\n    reported. Reproduced when the count under one reading is within tolerance.\n- id: fig5c-cell-type-clusters\n  statement: Spectral clustering on firing rate, mean normalised ACG and ACG rise time constant\n    split the 294 neurons into two clusters, 92 putative pyramidal neurons and 202 putative\n    interneurons.\n  source: Results, Feature-based classification of putative cell types, paragraph 3; Figure 5c\n  quote: We labeled this cluster as putative interneurons (IN; n = 202). The remaining neurons,\n    with lower firing rates, lower normalized mean ACG amplitude, and smaller τrise, were labeled\n    as putative pyramidal neurons (PY; n = 92).\n  expected:\n  - quantity: putative pyramidal neurons\n    value: 92\n    tolerance: 9.2\n  - quantity: putative interneurons\n    value: 202\n    tolerance: 20.2\n  depends_on:\n  - acg-fit-yield\n  criterion: From the Methods (Putative cell-type classification) and 07_spectral_clustering.py.\n    Features firing rate (spike count over the time from first to last spike,\n    02_trial_info.py:37-40), mean of the max-normalised wide ACG (±500 ms, 1 ms bins; Mean_ACG.m\n    and normalize_acg_to_unit.m) and tau_rise of the fit; standardised; SpectralClustering with\n    two clusters, nearest-neighbour affinity (10 neighbours, the default), random_state 42. The\n    cluster with higher firing rate, mean ACG and tau_rise is labelled IN (Results; the code\n    instead fixes cluster label 1 as PY, lines 37-45, which depends on the library version).\n    Reproduced when the two counts are within tolerance.\n- id: fig5dfh-cluster-features\n  statement: Putative interneurons had higher firing rates, greater normalised mean ACG amplitude\n    and larger tau_rise than putative pyramidal neurons.\n  source: Results, Feature-based classification of putative cell types, paragraph 3; Figure 5d-f\n  quote: One cluster comprised neurons with higher firing rates (Mann–Whitney U = 17294, P = 1.42\n    × 10−32; Fig. 5d), greater normalized mean ACG amplitude (U = 18522, P = 2.16 × 10−41; Fig. 5e),\n    and larger τrise (U = 13465, P = 2.58 × 10−9; Fig. 5f).\n  statistics:\n  - about: firing rate\n    test: Mann-Whitney U (Wilcoxon rank-sum)\n    statistic: U = 17294\n    p: 1.42e-32\n  - about: normalised mean ACG amplitude\n    test: Mann-Whitney U (Wilcoxon rank-sum)\n    statistic: U = 18522\n    p: 2.16e-41\n  - about: tau_rise\n    test: Mann-Whitney U (Wilcoxon rank-sum)\n    statistic: U = 13465\n    p: 2.58e-9\n  depends_on:\n  - fig5c-cell-type-clusters\n  criterion: Two-sided Mann-Whitney U tests of IN against PY on each feature, with Benjamini-Yekutieli\n    FDR over the five metrics of Fig. 5d-h as in 05_cell_analysis/main_5d-h.py:49-63. Reproduced\n    when IN is higher on all three with corrected p < 0.05. The features are those the clusters\n    were formed on, so the claim follows from fig5c-cell-type-clusters by construction; the\n    U values are reported.\n- id: fig5gh-burst-index-cv2\n  statement: Putative pyramidal neurons had a higher burst index (0.985 against 0.622) and\n    greater spike-train irregularity (CV2 1.673 against 1.319) than putative interneurons.\n  source: Results, Feature-based classification of putative cell types, paragraph 4; Figure 5g,h\n  quote: Putative pyramidal neurons showed higher burst index (PY = 0.985 vs. IN = 0.622; U =\n    6835, P = 6.35 × 10−6; Fig. 5g). They also exhibited greater spike-train irregularity (CV2;\n    PY = 1.673 vs. IN = 1.319; U = 6056, P = 4.84 × 10−4; Fig. 5h)\n  statistics:\n  - about: burst index\n    test: Mann-Whitney U (Wilcoxon rank-sum)\n    statistic: U = 6835\n    p: 6.35e-6\n  - about: CV2\n    test: Mann-Whitney U (Wilcoxon rank-sum)\n    statistic: U = 6056\n    p: 4.84e-4\n  expected:\n  - quantity: burst index, PY\n    value: 0.985\n    tolerance: 0.0985\n  - quantity: burst index, IN\n    value: 0.622\n    tolerance: 0.0622\n  - quantity: CV2, PY\n    value: 1.673\n    tolerance: 0.1673\n  - quantity: CV2, IN\n    value: 1.319\n    tolerance: 0.1319\n  depends_on:\n  - fig5c-cell-type-clusters\n  criterion: Burst index as defined by Royer et al. (ref. 97), computed as in\n    calc_ACG_metrics.m:45, the mean wide ACG at lags +2 to +4 ms over its mean at +199 to +299\n    ms. CV2 is Holt's local coefficient of variation (Methods cite ref. 98) of the session's\n    interspike intervals; the column the code feeds to Fig. 5h is std/mean of the ISIs\n    (02_trial_info.py:42-46), a plain CV; both are run as readings. Whether the printed values\n    are group means or medians is open; both are reported. Two-sided Mann-Whitney U with\n    Benjamini-Yekutieli FDR over the five metrics. Reproduced when PY is higher on both with\n    corrected p < 0.05 and, under one reading of each open detail, the four values are within\n    tolerance.\n- id: supp4-rodent-validation\n  statement: Applied to a labelled rodent dataset of 44 pyramidal neurons and 299 PV and SST\n    interneurons, the spectral-clustering classifier assigned 333 of 343 neurons correctly (97%).\n  source: Results, Feature-based classification of putative cell types, paragraph 4; Methods,\n    Putative cell-type classification, paragraph 4; Extended Data Fig. 4a (not in the text read)\n  quote: Using τrise, normalized mean ACG amplitude, and firing rate as inputs to spectral\n    clustering, 333 of 343 neurons were correctly assigned, with only one pyramidal neuron and\n    nine interneurons (PV or SST) misclassified (Extended Data Fig. 4a).\n  data: elsewhere\n  where: CellExplorer ground-truth reference dataset of Petersen et al. 2021 (Neuron 109, 3594;\n    ref. 72), no archive identifier given in the paper; its features are shipped as\n    data/cell_analysis/validation_data.xlsx in github.com/dariakussovska/heterogeneitywm at\n    commit 5144fe8\n  expected:\n    quantity: neurons correctly assigned\n    value: 333\n    tolerance: 0\n  criterion: Not testable on DANDI:000469. As in 05_cell_analysis/supp_4a-e.py, the three\n    features standardised and clustered as in fig5c-cell-type-clusters; each cluster labelled by\n    its majority ground-truth type (pyramidal or interneuron); accuracy is matched over total.\n    Reproduced when 333 of 343 are matched, with 1 pyramidal and 9 interneurons misassigned;\n    the tolerance is zero as a count from a deterministic clustering of fixed features.\n- id: fig5kl-concept-cell-types\n  statement: Of the classified concept cells, 11 were putative pyramidal and 14 putative\n    interneurons; pyramidal concept cells showed pronounced bursting, interneuron concept cells\n    smoother regular spiking.\n  source: Results, Distinct temporal activity patterns during memory maintenance in interneurons\n    and pyramidal neurons, paragraph 1; Figure 5i-l and legend\n  quote: Pyramidal concept-cell populations showed pronounced bursting (Fig. 5i,k), whereas\n    interneuron populations exhibited smoother regular-spiking activity (Fig. 5j,l).\n  expected:\n  - quantity: pyramidal concept cells\n    value: 11\n    tolerance: 1.1\n  - quantity: interneuron concept cells\n    value: 14\n    tolerance: 1.4\n  depends_on:\n  - concept-cells-count\n  - fig5c-cell-type-clusters\n  criterion: Counts are the concept cells among the PY and IN neurons (Fig. 5k,l legends).\n    \"Pronounced bursting\" and \"smoother\" are read from rasters in the paper; they are judged by\n    the Royer burst index and CV2 of fig5gh-burst-index-cv2 in these concept cells, PY median\n    above IN median for both. Reproduced when the counts are within tolerance and the medians\n    are so ordered; no test is reported for the second part.\n- id: fig6ab-celltype-bursts-vs-null\n  statement: Pyramidal populations showed elevated bursting over a null in both encoding and\n    maintenance, whereas interneurons showed elevated bursting during maintenance but not during\n    encoding.\n  source: Results, Distinct temporal activity patterns during memory maintenance in interneurons\n    and pyramidal neurons, paragraph 2; Figure 6a,b and legend\n  quote: Across participants, pyramidal populations showed elevated bursting during both encoding\n    and maintenance relative to chance (label-shuffled null; Encoding, W = 1.0, P = 0.012;\n    Maintenance, W = 0.0, P = 0.004; Fig. 6a–b). By contrast, interneurons exhibited elevated\n    population bursting during maintenance (W = 5.0, P = 0.001) but not during encoding (W = 41.0,\n    P > 0.05)\n  statistics:\n  - about: PY, encoding\n    test: Wilcoxon signed-rank\n    statistic: W = 1.0\n    p: 0.012\n  - about: PY, maintenance\n    test: Wilcoxon signed-rank\n    statistic: W = 0.0\n    p: 0.004\n  - about: IN, maintenance\n    test: Wilcoxon signed-rank\n    statistic: W = 5.0\n    p: 0.001\n  - about: IN, encoding\n    test: Wilcoxon signed-rank\n    statistic: W = 41.0\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - fig4c-encoding-bursts-vs-poisson\n  - fig5c-cell-type-clusters\n  criterion: The burst method and peak-rule readings of fig4c-encoding-bursts-vs-poisson on the\n    PY and IN groups, all of a participant's PY (or IN) neurons, participants with fewer than 3\n    in the group left out (Methods, Putative cell-type classification; code lines 178-181).\n    The null is open; the Results say \"label-shuffled null\", the Fig. 6a,b legend says\n    rate-matched Poisson surrogates and the code has only the Poisson null; readings are (a)\n    the Poisson surrogates, (b) a null from shuffling the cell-type labels within participant\n    (100 shuffles). BH-FDR over the groups tested together, as in fig4c. Reproduced when, under\n    one reading, PY exceeds the null in both epochs and IN in maintenance with corrected\n    p < 0.05, and IN in encoding does not (the paper's test, judged as written).\n- id: fig6cd-celltype-epochs\n  statement: Pyramidal burst rates stayed stable across task epochs, whereas interneuron burst\n    rates changed from encoding to each maintenance window and to the probe.\n  source: Results, Distinct temporal activity patterns during memory maintenance in interneurons\n    and pyramidal neurons, paragraph 3; Figure 6c,d\n  quote: Pyramidal burst rates remained stable across task epochs and load (Wilcoxon signed-rank,\n    all P > 0.05; Fig. 6c, Extended Data Fig. 5a,c), whereas interneuron burst rates changed\n    across task epochs (load 1; Enc → M1, W = 17.0, P = 0.011; Enc → M2, W = 26.0, P = 0.024; Enc\n    → M3, W = 7.5, P = 0.001; Enc → Probe, W = 18.5, P = 0.003; Fig. 6d).\n  statistics:\n  - about: PY, all epoch pairs and loads\n    test: Wilcoxon signed-rank\n    p: 0.05\n    p_relation: \">\"\n  - about: IN, encoding against M1\n    test: Wilcoxon signed-rank\n    statistic: W = 17.0\n    p: 0.011\n  - about: IN, encoding against M2\n    test: Wilcoxon signed-rank\n    statistic: W = 26.0\n    p: 0.024\n  - about: IN, encoding against M3\n    test: Wilcoxon signed-rank\n    statistic: W = 7.5\n    p: 0.001\n  - about: IN, encoding against probe\n    test: Wilcoxon signed-rank\n    statistic: W = 18.5\n    p: 0.003\n  depends_on:\n  - fig4f-all-cells-epochs\n  - fig5c-cell-type-clusters\n  criterion: The epoch method and readings of fig4f-all-cells-epochs on the PY and IN groups\n    (participants with at least 3 neurons in the group), paired two-sided Wilcoxon signed-rank,\n    BH-FDR within group and load over the 10 period pairs. Reproduced when, under one reading,\n    IN differs from encoding at M1, M2, M3 and probe with corrected p < 0.05 and PY has no pair\n    with corrected p < 0.05 at load 1 (the paper's test for the absence). Loads 2 and 3 for PY\n    are reported. The direction of the IN change is reported; the paper does not state it.\n- id: ext5bd-in-load-dependence\n  statement: Interneuron burst-rate differences across maintenance epochs increased with load.\n  source: Results, Distinct temporal activity patterns during memory maintenance in interneurons\n    and pyramidal neurons, paragraph 3; Extended Data Fig. 5b,d (not in the text read)\n  quote: Interneuron burst-rate differences across maintenance epochs increased with load\n    (Extended Data Fig. 5b,d)\n  depends_on:\n  - fig6cd-celltype-epochs\n  criterion: The analysis of fig6cd-celltype-epochs on IN at loads 1, 2 and 3. The Extended Data\n    legends are not in the text read, so the measure is open; it is read as the median over\n    participants of the absolute difference in bursts between encoding and each of M1 to M3,\n    averaged over the three windows. Reproduced when it rises from load 1 to load 3, under one\n    reading of the epochs.\n- id: fig6e-load-modulation-in\n  statement: A significant portion of interneurons was modulated by memory load during\n    maintenance (14.36%), including interneuron concept cells (21.42%), while pyramidal neurons\n    showed minimal load modulation (5.43%; concept pyramidal 0.00%).\n  source: Results, Distinct temporal activity patterns during memory maintenance in interneurons\n    and pyramidal neurons, paragraph 4; Figure 6e; Extended Data Fig. 5e (not in the text read)\n  quote: A significant portion of interneurons was modulated by memory load during maintenance\n    (14.36%; permutation test, P = 0.002; Fig. 6e), including interneuron concept cells (21.42%;\n    P = 0.032; Extended Data Fig. 5e). By contrast, pyramidal neurons showed minimal load\n    modulation (all PY, 5.43%, P > 0.05; concept PY, 0.00%, P > 0.05; Fig. 6e; Extended Data Fig.\n    5e).\n  statistics:\n  - about: all IN\n    test: permutation test\n    p: 0.002\n    n: 202 interneurons\n  - about: IN concept cells\n    test: permutation test\n    p: 0.032\n    n: 14 interneuron concept cells\n  - about: all PY and PY concept cells\n    test: permutation test\n    p: 0.05\n    p_relation: \">\"\n  expected:\n  - quantity: load-modulated IN\n    value: 14.36\n    tolerance: 1.436\n    unit: percent\n  - quantity: load-modulated IN concept cells\n    value: 21.42\n    tolerance: 2.142\n    unit: percent\n  - quantity: load-modulated PY\n    value: 5.43\n    tolerance: 0.543\n    unit: percent\n  - quantity: load-modulated PY concept cells\n    value: 0.0\n    tolerance: 0\n    unit: percent\n  depends_on:\n  - fig1e-load-modulated-neurons\n  - fig5c-cell-type-clusters\n  criterion: The GLM, permutation and trial readings of fig1e-load-modulated-neurons, with groups\n    PY, IN, PY concept cells and IN concept cells (06_cell_specific/main_6e,f,supp_e,f.py, the\n    concept subsets by its commented option, lines 24-32). The tolerance of PY concept cells is\n    zero, as 10% of 0. Reproduced when, under one reading, the IN and IN concept percentages are\n    within tolerance with p < 0.05, and the PY groups have p at or above 0.05 (the paper's test\n    for the absence); the PY percentages are reported.\n- id: fig6f-rt-modulation-in-concept\n  statement: Interneuron concept cells were modulated by reaction time during maintenance\n    (35.71%), but not all interneurons, and pyramidal neurons showed no significant RT\n    modulation in either the full population or the concept subset.\n  source: Results, Distinct temporal activity patterns during memory maintenance in interneurons\n    and pyramidal neurons, paragraph 4; Figure 6f; Extended Data Fig. 5f (not in the text read)\n  quote: Interneuron concept cells were also modulated by reaction time (RT; 35.71%; P = 0.002),\n    although this effect was not robust across all interneurons (P > 0.05; Fig. 6f; Extended Data\n    Fig. 5f). Pyramidal neurons showed no significant RT modulation in either the full population\n    or the concept-cell subset (permutation tests, all P > 0.05; Fig. 6f; Extended Data Fig. 5f).\n  statistics:\n  - about: IN concept cells\n    test: permutation test\n    p: 0.002\n    n: 14 interneuron concept cells\n  - about: all IN, all PY, PY concept cells\n    test: permutation test\n    p: 0.05\n    p_relation: \">\"\n  expected:\n    quantity: RT-modulated IN concept cells\n    value: 35.71\n    tolerance: 3.571\n    unit: percent\n  depends_on:\n  - fig1f-rt-modulation-not-significant\n  - fig5c-cell-type-clusters\n  criterion: The GLM of fig1e-load-modulated-neurons with RT as predictor, each trial's own RT\n    (fig1f-rt-modulation-not-significant), the groups of fig6e-load-modulation-in. Reproduced\n    when the IN concept percentage is within tolerance with p < 0.05, and all IN, all PY and PY\n    concept cells have p at or above 0.05 (the paper's test for the absence), under one trial\n    reading.\n- id: fig6gh-in-concept-cv2\n  statement: Interneuron concept cells had higher CV2 during maintenance than encoding on\n    preferred load 1 trials but not on nonpreferred trials, while pyramidal concept cells showed\n    stable CV2.\n  source: Results, Distinct temporal activity patterns during memory maintenance in interneurons\n    and pyramidal neurons, paragraph 5; Figure 6g,h\n  quote: By contrast, interneuron concept cells exhibited higher CV2 during maintenance than\n    during encoding on preferred trials (W = 13.0, P = 0.032), but not on nonpreferred trials (W =\n    50.0, P > 0.05; Fig. 6g–h)\n  statistics:\n  - about: IN concept cells, preferred trials\n    test: Wilcoxon signed-rank\n    statistic: W = 13.0\n    p: 0.032\n  - about: IN concept cells, nonpreferred trials\n    test: Wilcoxon signed-rank\n    statistic: W = 50.0\n    p: 0.05\n    p_relation: \">\"\n  - about: PY concept cells, preferred and nonpreferred, encoding and maintenance\n    test: Wilcoxon signed-rank\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - fig5kl-concept-cell-types\n  criterion: From the Results and 06_cell_specific/main_6g,h.py. Per PY or IN concept cell, CV2\n    (Holt's local measure, lines 117-122) of the interspike intervals of spikes concatenated\n    over preferred (or nonpreferred) trials, in encoding (first image, 1 s) and maintenance\n    (2.5 s); encoding against maintenance by a two-sided Wilcoxon signed-rank test over cells.\n    Open, the trials; the Results say load 1 trials, the code uses all loads (no load filter);\n    both are run. Reproduced when, under one reading, IN preferred has maintenance above\n    encoding with p < 0.05, IN nonpreferred does not, and PY has no comparison with p < 0.05\n    (the paper's tests, judged as written).\n- id: ext5gh-py-decay-preferred\n  statement: Pyramidal concept cells showed increased decay time constants on preferred trials\n    during encoding and maintenance, an effect absent in interneurons.\n  source: Results, Distinct temporal activity patterns during memory maintenance in interneurons\n    and pyramidal neurons, paragraph 5; Extended Data Fig. 5g,h (not in the text read)\n  quote: Pyramidal concept cells showed increased decay time constants during encoding and\n    maintenance on preferred trials (Wilcoxon signed-rank, Pmax = 0.029), an effect absent in\n    interneurons (all P > 0.05; Extended Data Fig. 5g–h).\n  statistics:\n  - about: PY concept cells, preferred against nonpreferred, encoding and maintenance\n    test: Wilcoxon signed-rank\n    p: 0.029\n  - about: IN concept cells\n    test: Wilcoxon signed-rank\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - fig5kl-concept-cell-types\n  criterion: No code computes the decay constants per trial type; 06_cell_specific/supp_5g,h.py\n    reads them from the shipped decay_constant_change.xlsx and tests them with a paired t-test,\n    while the paper names a Wilcoxon signed-rank test (the paper's test is used, the t-test is\n    a variant). The decay constant is taken as tau_decay of the ACG fit of acg-fit-yield on the\n    spikes of preferred (or nonpreferred) trials of each epoch; open, the trials (load 1 or all\n    loads), both run. Reproduced when, under one reading, PY tau_decay is larger on preferred\n    than nonpreferred trials in both epochs with p < 0.05 and IN has no comparison with\n    p < 0.05.\n- id: fig6i-py-bin-width-decoding\n  statement: Pyramidal concept cells did not decode the image above chance during load 1\n    maintenance with 250 and 500 ms bins (26.67%, 23.33%) but did with 750 and 1000 ms bins\n    (40.00%, 43.33%).\n  source: Results, Distinct temporal activity patterns during memory maintenance in interneurons\n    and pyramidal neurons, paragraph 6; Figure 6i\n  quote: For pyramidal neurons, decoding accuracy did not exceed chance with short temporal\n    windows (250 ms, 26.67%, permutation test, P > 0.05; 500 ms, 23.33%, P > 0.05) ... Accuracy\n    improved with larger windows (750 ms, 40.00%, P = 0.030; 1000 ms, 43.33%, P = 0.030)\n  statistics:\n  - about: 250 and 500 ms\n    test: permutation test\n    p: 0.05\n    p_relation: \">\"\n  - about: 750 ms\n    test: permutation test\n    p: 0.03\n  - about: 1000 ms\n    test: permutation test\n    p: 0.03\n  expected:\n  - quantity: PY accuracy, 250 ms\n    value: 26.67\n    tolerance: 2.667\n    unit: percent\n  - quantity: PY accuracy, 500 ms\n    value: 23.33\n    tolerance: 2.333\n    unit: percent\n  - quantity: PY accuracy, 750 ms\n    value: 40.0\n    tolerance: 4.0\n    unit: percent\n  - quantity: PY accuracy, 1000 ms\n    value: 43.33\n    tolerance: 4.333\n    unit: percent\n  depends_on:\n  - fig5kl-concept-cell-types\n  - fig2f-bin-width-decoding\n  criterion: The method and trial readings of fig2f-bin-width-decoding with the PY concept cells\n    as the pseudo-population (06_cell_specific/main_6i,j,supp_5i,j.py), BH-FDR over the 12 tests\n    of 4 widths and 3 loads (line 193). Reproduced when, under one reading, the four accuracies\n    are within tolerance, 750 and 1000 ms have corrected p < 0.05 and 250 and 500 ms do not.\n- id: fig6j-in-bin-width-decoding\n  statement: Interneuron concept cells decoded the image above chance during load 1 maintenance\n    at all bin widths (53.33%, 50.00%, 46.67%, 53.33%), less sensitive to bin width than\n    pyramidal cells.\n  source: Results, Distinct temporal activity patterns during memory maintenance in interneurons\n    and pyramidal neurons, paragraph 7; Figure 6j\n  quote: In contrast, interneurons (n = 14) decoded above chance across all window sizes (250 ms,\n    53.33%, P = 0.002; 500 ms, 50.00%, P = 0.002; 750 ms, 46.67%, P = 0.002; 1000 ms, 53.33%, P =\n    0.002; Fig. 6j)\n  statistics:\n  - test: permutation test\n    p: 0.002\n    n: 14 interneuron concept cells\n  expected:\n  - quantity: IN accuracy, 250 ms\n    value: 53.33\n    tolerance: 5.333\n    unit: percent\n  - quantity: IN accuracy, 500 ms\n    value: 50.0\n    tolerance: 5.0\n    unit: percent\n  - quantity: IN accuracy, 750 ms\n    value: 46.67\n    tolerance: 4.667\n    unit: percent\n  - quantity: IN accuracy, 1000 ms\n    value: 53.33\n    tolerance: 5.333\n    unit: percent\n  depends_on:\n  - fig5kl-concept-cell-types\n  - fig2f-bin-width-decoding\n  criterion: As fig6i-py-bin-width-decoding with the IN concept cells. Reproduced when, under one\n    reading, the four accuracies are within tolerance and each has corrected p < 0.05.\n- id: fig6kl-cross-temporal-by-type\n  statement: Cross-temporal decoding showed no above-chance generalization for the 11 pyramidal\n    concept cells, while interneuron concept cells decoded above chance in cross-temporal maps.\n  source: Results, Distinct temporal activity patterns during memory maintenance in interneurons\n    and pyramidal neurons, paragraphs 6 and 7; Figure 6k,l\n  quote: Cross-temporal decoding showed no above-chance generalization across time even for\n    populations of 11 pyramidal concept cells (Fig. 6k)\n  depends_on:\n  - fig5kl-concept-cell-types\n  - fig2d-cross-temporal-localized\n  criterion: The method and readings of fig2d-cross-temporal-localized (06_cell_specific/main_6k,l.py)\n    with PY and with IN concept cells. Reproduced when, under one reading, no off-diagonal\n    train-test pair survives for PY (the paper's test for the absence, the binomial test with\n    FDR and the cluster rule) and at least one cluster survives for IN.\n- id: ext5ij-load2-decoding-by-type\n  statement: Interneuron concept cells also decoded the second image in load 2 trials above\n    chance at all bin widths, while pyramidal concept cells did not.\n  source: Results, Distinct temporal activity patterns during memory maintenance in interneurons\n    and pyramidal neurons, paragraph 7; Extended Data Fig. 5i,j (not in the text read)\n  quote: Interneurons also decoded the second stimulus in load 2 trials above chance across all\n    windows (all P < 0.05), an effect not observed in pyramidal concept cells (all P > 0.05;\n    Extended Data Fig. 5i–j).\n  statistics:\n  - about: IN concept cells, all widths\n    test: permutation test\n    p: 0.05\n    p_relation: \"<\"\n  - about: PY concept cells, all widths\n    test: permutation test\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - fig6j-in-bin-width-decoding\n  criterion: As fig6i-py-bin-width-decoding and fig6j-in-bin-width-decoding on load 2 trials with\n    the second image as label. Reproduced when, under one reading, IN has corrected p < 0.05 at\n    all four widths and PY at none.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/kussovska-2025.yaml paper/10.1101-2025.10.31.684900.txt 2>&1 | tail -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re
for i,l in enumerate(open('claims/kussovska-2025.yaml'),1):
    if l.lstrip().startswith('#'): continue
    s=l.strip()
    s=re.sub(r'^(- )?[a-z_]+: ?','',s) if re.match(r'^(- )?[a-z_]+:( |$)',s) else s
    if ': ' in s or s.endswith(':'): print(i, l.rstrip()[:150])
EOF
```

```
216     details, with the readings run. Trials: the Methods say "96 trials per participant matched
219     (an input from the code repository), (b) all trials of each participant. Permutation:
221     None, main_1e,f.py:124-135); both are run. Correction: the code applies none across
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/kussovska-2025.yaml'
t=open(p).read()
t=t.replace('details, with the readings run. Trials: the Methods say','details, with the readings run. For the trials, the Methods say')
t=t.replace('(b) all trials of each participant. Permutation:\n    within','(b) all trials of each participant. The permutation is\n    within')
t=t.replace('both are run. Correction: the code applies none','both are run. For correction, the code applies none')
open(p,'w').write(t)
EOF
python tools/claims_check.py claims/kussovska-2025.yaml paper/10.1101-2025.10.31.684900.txt 2>&1 | tail -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import re, textwrap
p='claims/kussovska-2025.yaml'
paper=open('paper/10.1101-2025.10.31.684900.txt').read()
def seg(start,end):
    i=paper.index(start); j=paper.index(end,i)+len(end); return paper[i:j]
Q={
'fig1e-load-modulated-neurons':[seg('During the maintenance epoch, the preSMA','Fig. 1e)')],
'fig2e-maintenance-decoding-amy-mtl':[seg('concept cells in AMY and in the medial temporal lobe','Fig. 2e)')],
'ext1f-maintenance-decoding-load2':[seg('The same held for AMY and MTL concept cells at load 2','Extended Data Fig. 1f)')],
'fig2f-bin-width-decoding':[seg('In load 1 trials, accuracy was above chance at all bin widths','increased nearly twofold as bin width increased')],
'fig4f-all-cells-epochs':[seg('At the population level, burst rates increased','Enc → Probe: W = 4.0, P = 0.039)')],
'fig4hj-group-epochs':[seg('Neurons with high mean ACG amplitude increased from encoding','Wilcoxon signed-rank, P > 0.05)')],
'fig6ab-celltype-bursts-vs-null':[seg('Across participants, pyramidal populations showed elevated bursting','(W = 41.0, P > 0.05)')],
'fig6cd-celltype-epochs':[seg('Pyramidal burst rates remained stable','Fig. 6d)')],
'fig6e-load-modulation-in':[seg('A significant portion of interneurons was modulated by memory load','Extended Data Fig. 5e).')],
'fig6i-py-bin-width-decoding':[seg('For pyramidal neurons, decoding accuracy did not exceed chance','500 ms: 23.33%, P > 0.05)'), seg('Accuracy improved with larger windows','1000 ms: 43.33%, P = 0.030)')],
'fig6j-in-bin-width-decoding':[seg('In contrast, interneurons (n = 14) decoded above chance','Fig. 6j)')],
}
lines=open(p).read().split('\n')
out=[];i=0;cur=None
while i<len(lines):
    l=lines[i]
    m=re.match(r'^- id: (\S+)',l)
    if m: cur=m.group(1)
    if cur in Q and l.startswith('  quote:'):
        i+=1
        while i<len(lines) and lines[i].startswith('    '): i+=1
        txt=' ... '.join(Q[cur])
        out.append('  quote: >-')
        out+=textwrap.wrap(txt,width=96,initial_indent='    ',subsequent_indent='    ',break_long_words=False,break_on_hyphens=False)
        continue
    out.append(l); i+=1
open(p,'w').write('\n'.join(out))
EOF
grep -n "9.70" paper/*.txt | head -2; python tools/claims_check.py claims/kussovska-2025.yaml paper/10.1101-2025.10.31.684900.txt 2>&1 | tail -10
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "rather\|—" claims/kussovska-2025.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/kussovska-2025.yaml'));c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

```
45 45 29 45 20
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
?? claims/kussovska-2025.yaml
?? scripts
```

**Agent**

I've written `claims/kussovska-2025.yaml`: 45 claims, every one with a quote. The quote checker passes except for one p-value it can't parse: the paper prints "9.70 × 10−12" (fig3h, Dunn early vs late), which I confirmed by reading. Nothing is committed.

**Text read.** The bioRxiv full-text page of the preprint posted 1 November 2025 (doi:10.1101/2025.10.31.684900). Its header says "version of record", but the page offers a "current version", which I did not read. It holds the main text, the legends of Figs 1 to 6, and the full Methods. No PDF was supplied.

**Missing from the text.** The Extended Data Figs 1 to 5 and their legends, and the Source Data. The main findings are all stated in the main text, so I went ahead. The 9 claims on Extended Data panels rest on the main-text sentences that cite them and are marked "(not in the text read)". A few Methods equations were also lost in extraction (the GLM link, and the peak and prominence formulas for bursts).

**Code read.** github.com/dariakussovska/heterogeneitywm at commit 5144fe8 (2025-10-26), the last commit before the preprint. The later REVISIONS folders (2026) were not used. Three things in it bear on most claims:
- The matched trial sets (96 trials per participant matched on load, 75 matched on image) come only from xlsx files shipped in the repository. No code builds them.
- The autocorrelogram features are computed in MATLAB, but the spike input file is an empty placeholder. Only the output table `Cell_metrics.xlsx` is shipped.
- The README downloads dandiset version 0.240123.1806, while the paper cites 0.231213.2047.

**Counts.**

| Field | Claims |
|---|---|
| Quote | 45 |
| Statistics | 29 (74 values) |
| Expected values | 20 |
| Criterion | 45 |
| Inferred | 0 |

All claims use the dataset except `supp4-rodent-validation`, which is `data: elsewhere`: it uses the CellExplorer ground-truth rodent data, for which the paper gives no archive identifier.

**Details left open, with the readings named:**
- **GLM trials (Fig 1e,f; Fig 6e,f):** the 96 load-matched trials from the code's xlsx, or all trials.
- **GLM permutation:** within participant (Methods) or over the shared trial vector (code).
- **GLM RT predictor:** each trial's own RT, or the subject-1 RT vector the code uses for every neuron.
- **Concept-cell bootstrap:** the Methods version, or the code's (both groups resampled to the smaller size, a different p formula). The code sets no seed, so ten seeds per reading.
- **Behaviour:** RT summary (three readings); which p for Fig 1c (raw or Bonferroni); what is permuted in the two RT tests (no code exists for them).
- **Persistence:** what counts as single-cell and population persistence (two rules each).
- **Cross-temporal decoding:** one- or two-sided binomial; cluster-duration null (Methods) or the code's contours longer than 13 points; first image or last image as label for loads 2 and 3.
- **Maintenance decoding:** at least 3 (Methods) or more than 3 (code) concept cells per participant.
- **Bin-width decoding:** trial alignment, the code's xlsx or rebuilt from the dataset. The pairwise bin-width tests have no code, so two permutation schemes.
- **dPCA:** Kruskal-Wallis over 5 groups (code) or 3. H = 457 is only reachable with 5. The same or the code's trials for maintenance (the code selects them by the wrong id column). Smoothing sigma 120 ms (Methods and code) or 60 ms (Results). The early/late "protect time" setting.
- **Bursts:**
  - Peak rule: smoothed value above the 90th percentile (Methods) or prominence at that percentile (Results and code).
  - Surrogate threshold: the real data's or each surrogate's own.
  - Neuron groups: median split with at least 5 neurons (Methods) or the 6 lowest and 6 highest with at least 10 (code).
  - "All neurons": all 902 or the 294 fitted.
  - M1 to M3: 1 s windows in each trial (Methods) or thirds of the concatenated train (code).
  - The Fig 6a,b null: label-shuffled (Results) or Poisson (legend and code).
- **ACG and cell types:** which spikes enter the autocorrelogram; R2 > or ≥ 0.3; CV2 as Holt's local measure (Methods) or plain CV (code); whether the printed values are means or medians; load 1 or all loads for the CV2 and decay-constant tests.
- **Qualitative claims:** a measure is named for trajectory complexity and for the "minimal", "little effect" and "increased with load" statements in the Extended Data claims.

**Missing for specific claims:**
- **No code for these tests:** the RT tests and the pairwise bin-width tests. The per-trial-type decay constants exist only as a shipped xlsx, tested there with a t-test where the paper names a Wilcoxon test.
- **The trial-selection rule** behind the matched pseudo-population trials is in neither the paper nor the code.
- **No published rule** for the qualitative claims; the measures named above are readings, not the paper's.

## End of run

30 turns, 12 minutes, $5.44 at API prices, result: success.
