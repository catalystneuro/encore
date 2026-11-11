# kussovska-2025 · claims-check · run 42758975332

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper | grep -i kuss; python tools/claims_check.py claims/kussovska-2025.yaml paper/kussovska-2025.txt; cat claims/kussovska-2025.yaml; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper | grep -i -E "kuss|684900"; ls paper | head
```

```
10.1101-2025.10.31.684900.txt
10.1101-2025.10.31.684900.txt
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/kussovska-2025.yaml paper/10.1101-2025.10.31.684900.txt; wc -l paper/10.1101-2025.10.31.684900.txt claims/kussovska-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "Reader" docs/protocol.md | head;
```

```
15:  it against the paper. Readers never see the dataset's data.
28:Reader runs are made with the [Paper run](../.github/workflows/papers.yml)
43:## Reader
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.10.31.684900.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.10.31.684900.txt",
 "offset": 384,
 "limit": 340
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker flags one value (9.7e-12, written 9.70 × 10−12 in the paper). Now reading the protocol and claims file.

**Agent calls Bash**

```bash
cd  sed -n 1,200p docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-14`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim's statement, expected values or criterion. A method detail the file
  lacks it takes from the paper, citing the passage, and it asks a reader
  only when it believes the file misreads the paper.
[... 179 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/kussovska-2025.yaml"
}
```

```
1	# Claims for Kussovska, Kim & Rungratsameetaweemana (2025), "Neural heterogeneity shapes the
2	# temporal structure of human working memory", bioRxiv, doi:10.1101/2025.10.31.684900, tested on
3	# DANDI:000469 (reused; the paper analyses the dataset of Kyzar et al. 2024, ref. 59).
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5	# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md.
6	#
7	# Text read. paper/10.1101-2025.10.31.684900.txt, the bioRxiv full-text page of the preprint
8	# posted 1 November 2025 (its header says "version of record"; the page says "New Results" and
9	# offers a "current version", so a later version may exist; it was not read). It holds the
10	# abstract, Introduction, Results, legends of Figures 1 to 6, Discussion, Methods, Data and Code
11	# availability and references. No PDF was supplied. The Extended Data figures (Extended Data
12	# Figs 1 to 5, behind "Supplementary Material") and their legends are not in the text read; the
13	# Source Data are not either. The main findings are all stated in the main text and legends, so
14	# claims were written; claims on Extended Data panels rest on the main-text sentences that cite
15	# them, and their sources say "(not in the text read)". Several equations of the Methods (the GLM
16	# link, the local-peak and prominence formulas of Burst detection) were lost in extraction.
17	#
18	# Code read. github.com/dariakussovska/heterogeneitywm at commit 5144fe8 (2025-10-26), the last
19	# commit before the preprint was posted. Later commits (REVISIONS/ and R2_REVISIONS/, 2026) are
20	# for a revised version and were not used. The repository holds Python scripts named by figure
[... 933 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/kussovska-2025.yaml",
 "offset": 954,
 "limit": 450
}
```

```
954	  depends_on:
955	  - fig5c-cell-type-clusters
956	  criterion: Two-sided Mann-Whitney U tests of IN against PY on each feature, with Benjamini-Yekutieli
957	    FDR over the five metrics of Fig. 5d-h as in 05_cell_analysis/main_5d-h.py:49-63. Reproduced
958	    when IN is higher on all three with corrected p < 0.05. The features are those the clusters
959	    were formed on, so the claim follows from fig5c-cell-type-clusters by construction; the
960	    U values are reported.
961	- id: fig5gh-burst-index-cv2
962	  statement: Putative pyramidal neurons had a higher burst index (0.985 against 0.622) and
963	    greater spike-train irregularity (CV2 1.673 against 1.319) than putative interneurons.
964	  source: Results, Feature-based classification of putative cell types, paragraph 4; Figure 5g,h
965	  quote: Putative pyramidal neurons showed higher burst index (PY = 0.985 vs. IN = 0.622; U =
966	    6835, P = 6.35 × 10−6; Fig. 5g). They also exhibited greater spike-train irregularity (CV2;
967	    PY = 1.673 vs. IN = 1.319; U = 6056, P = 4.84 × 10−4; Fig. 5h)
968	  statistics:
969	  - about: burst index
970	    test: Mann-Whitney U (Wilcoxon rank-sum)
971	    statistic: U = 6835
972	    p: 6.35e-6
973	  - about: CV2
[... 425 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat tools/claims_check.py; grep -rn "p_relation" docs/*.md schema* tools/*.py 2>/dev/null | head
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

[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 295,330p schemas/claims.schema.json; grep -n '"checks"' -A40 schemas/claims.schema.json | head -60; git log --oneline -3 -- claims/; ls claims | head; grep -l "kind: agent" claims/*.yaml | head -2
```

```
"test": {
          "description": "The test as the paper names it, e.g. 'Wilcoxon rank-sum', 'two-tailed t-test'.",
          "type": "string"
        },
        "statistic": {
          "description": "The test statistic as reported, e.g. 't(14) = 3.2', 'F(2, 40) = 5.1', 'r = 0.38'.",
          "type": "string"
        },
        "p": {
          "description": "The reported p-value as printed, or its bound when the paper gives one ('p < 0.05' is p 0.05 with p_relation '<'). A paper that prints 'P = 0' (below the precision it reports) is recorded as 0.",
          "type": "number",
          "minimum": 0,
          "maximum": 1
        },
        "p_relation": {
          "description": "How p was reported: exactly (the default) or as a bound.",
          "enum": [
            "=",
            "<",
            ">"
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/dariakussovska/heterogeneitywm.git hw 2>&1 | tail -2; cd hw && git checkout -q 5144fe8 && git log -1 --format='%h %ad' && ls -R | head -80
```

```
5144fe8 Sun Oct 26 20:56:07 2025 -0400
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
[... 62 more lines not kept]
```

**Agent**

The checker flags only 9.70 × 10−12 (a trailing-zero print form; the value is right). I cloned the paper's code at 5144fe8 to spot-check the criteria's code citations.

**Agent calls Bash**

```bash
cd $TMPDIR/hw; f="04_bursting/main_4c,d,6a,b.py"; sed -n 1,30p "$f"; echo ----; sed -n 40,125p "$f"; echo; grep -n "distance\|prominence\|percentile\|find_peaks\|TRIAL_WIN\|min_cells\|>= 3\|< 3\|902\|fdr\|multipletests" "$f" | head -40
```

```
import os
import ast
import hashlib
import numpy as np
import pandas as pd
import scipy.signal as signal
from scipy.signal.windows import gaussian

# =========================
# Parameters
# =========================
bin_size = 0.07                    
TRIAL_WIN = 1                       # seconds per trial window; CHANGE TO 2.8 FOR MAINTENANCE
GLOBAL_SEED = 5
sigma_sec = 0.04                    # Gaussian kernel 
prominence_threshold_percentile = 90 # percentile on smoothed rate
min_inter_burst_interval = 0.14     
N_SURROGATES = 100                   # Poisson repetitions per subject
PRINT_DEBUG = True

[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hw; f="04_bursting/main_4c,d,6a,b.py"; sed -n 160,200p "$f"; sed -n 440,520p "$f"
```

```
Subjects eligible per category.
    - For ACG/Decay categories: require >= PER_SUBJ neurons with a valid feature value (after R² filter applied upstream).
    - Other categories keep your previous logic (thresholds unchanged unless noted).
    """
    if category in ("Lowest_ACG", "Highest_ACG"):
        eligible = df_metadata_decay_acg.dropna(subset=["acg_norm"])
        counts = eligible.groupby("subject_id")["Neuron_ID_3"].count()
        return counts[counts >= PER_SUBJ].index.tolist()

    if category in ("Lowest_decay", "Highest_decay"):
        eligible = df_metadata_decay_acg.dropna(subset=["Decay"])
        counts = eligible.groupby("subject_id")["Neuron_ID_3"].count()
        return counts[counts >= PER_SUBJ].index.tolist()

    if category == "Concept_cells":
        counts = df_metadata_concept[df_metadata_concept["Signi"] == "Y"]["subject_id"].value_counts()
        return counts[counts >= 3].index.tolist()

    if category in ("Pyramidal", "Interneurons"):
        label = "PY" if category == "Pyramidal" else "IN"
[... 103 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hw; sed -n 60,75p "02_psth_decoding/main_2e,supp_1f.py"; echo ----; sed -n 60,150p "01_task/main_1e,f.py"
```

```
per_subject_obs = []
    per_subject_shuf = []
    per_subject_ids = []

    for subj in all_subject_ids:
        neuron_ids = df_regions[
            (df_regions['Location'].isin(locations)) &
            (df_regions['subject_id'] == subj) &
            (df_regions['Signi'] == 'Y')
        ]['Neuron_ID_3'].unique()
        if len(neuron_ids) <= 3:
            continue

        y_matrix = trial_info[trial_info['subject_id'] == subj][[
            'trial_id', 'num_images_presented', 'stimulus_index_enc1',
            'stimulus_index_enc2', 'stimulus_index_enc3']].reset_index(drop=True)
----
        design_matrix[trial_index, neuron_index] = np.array(spikes_for_this_trial)

df_design_matrix = pd.DataFrame(
[... 89 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hw; grep -n "kruskal\|posthoc_dunn\|624\|protect\|n_components\|\[:5\]\|:5" "03_dpca/main_3h,supp_2c,d,l.py" "03_dpca/main_3d,supp_2a,b,i.py" | head -30; echo ----; grep -n "load\|num_images\|cv2\|CV2" "06_cell_specific/main_6g,h.py" | head -20; echo ----; cat data/cell_analysis/Mean_ACG.m | head -30; grep -n "acg_narrow\|acg_wide\|burst\|Mean_ACG" data/cell_analysis/calc_ACG_metrics.m | head
```

```
03_dpca/main_3h,supp_2c,d,l.py:22:    time_split=624,
03_dpca/main_3h,supp_2c,d,l.py:115:        dpca_early.protect = ['t']
03_dpca/main_3h,supp_2c,d,l.py:124:        dpca_late.protect = []
03_dpca/main_3h,supp_2c,d,l.py:146:    H_kw, kw_p = sps.kruskal(*box_datas)
03_dpca/main_3h,supp_2c,d,l.py:152:        dunn_df = sp.posthoc_dunn(mat, p_adjust="fdr_bh")
03_dpca/main_3h,supp_2c,d,l.py:219:     time_split=624,
03_dpca/main_3h,supp_2c,d,l.py:225:plt.boxplot(explvar_early[:, :5]) # Or explvar_late
03_dpca/main_3d,supp_2a,b,i.py:121:        dpca_enc.protect = []
03_dpca/main_3d,supp_2a,b,i.py:130:        dpca_maint.protect = []
03_dpca/main_3d,supp_2a,b,i.py:152:    H_kw, kw_p = sps.kruskal(*box_datas)
03_dpca/main_3d,supp_2a,b,i.py:158:        dunn_df = sp.posthoc_dunn(mat, p_adjust="fdr_bh")
03_dpca/main_3d,supp_2a,b,i.py:235:ax[0].boxplot(explvar_enc[:, :5]*100)
03_dpca/main_3d,supp_2a,b,i.py:240:ax[1].boxplot(explvar_maint[:, :5]*100)
----
117:def compute_cv2(spike_times):
121:    cv2 = 2 * np.abs(np.diff(isi)) / (isi[:-1] + isi[1:])
122:    return np.mean(cv2)
124:# Collect CV2s for neurons that have values for both Encoding and Delay
125:cv2_data = {'PY': {'encoding': [], 'delay': []},
130:    cv2_enc = compute_cv2(entry['encoding'])
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/hw; sed -n 1,116p "06_cell_specific/main_6g,h.py" | grep -v "^\s*#" | grep -v "^\s*$" | head -80
```

```
import numpy as np
import ast
import matplotlib.pyplot as plt
def generate_filtered_spike_trains(df_encoding, df_delay, cell_type_map,
                                   encoding_col='Standardized_Spikes',
                                   delay_col='Standardized_Spikes',
                                   trial_col='trial_id',
                                   encoding_duration=1,
                                   delay_duration=2.5,
                                   preferred_col='Category',
                                   preferred_label='Preferred'): ### CHANGE TO "Non-Preferred" FOR FIG 6H
    """
    Returns:
    spike_dict[neuron_uid] = {
        'subject_id': subject_id,
        'cell_type': 'PY' or 'IN',
        'encoding': np.array([...]),
        'delay':    np.array([...])
    }
    """
[... 61 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kussovska-2025.yaml",
 "old_string": "    epoch's bins (Methods), (b) prominence at or above that percentile (Results, \"a\n    90th-percentile prominence threshold\", and the code, lines 251-255). Surrogate threshold;",
 "new_string": "    epoch's bins (Methods), (b) prominence at or above that percentile (Results, \"a\n    90th-percentile prominence threshold\", and the code, lines 251-255). Peak spacing; 2 bins\n    (140 ms) in the Methods and the code (line 17) is the main reading; the Results say\n    candidates \"within 70 ms of a previous event were suppressed\", run as a variant with a\n    spacing of 1 bin. Surrogate threshold;"
}
```

```
The file claims/kussovska-2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kussovska-2025.yaml",
 "old_string": "    \"all neurons\" is all 902 (code, line 183) or the 294 fitted neurons; concept cells need at",
 "new_string": "    \"all neurons\" is all 902 (code, line 183; participants with at least 10 neurons, line 185)\n    or the 294 fitted neurons; concept cells need at"
}
```

```
The file claims/kussovska-2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kussovska-2025.yaml",
 "old_string": "  statement: Pyramidal burst rates stayed stable across task epochs, whereas interneuron burst\n    rates changed from encoding to each maintenance window and to the probe.",
 "new_string": "  statement: Pyramidal burst rates stayed stable across task epochs at every load, whereas\n    interneuron burst rates changed from encoding to each maintenance window and to the probe\n    in load 1 trials."
}
```

```
The file claims/kussovska-2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kussovska-2025.yaml",
 "old_string": "    with corrected p < 0.05 at load 1 (the paper's test for the absence). Loads 2 and 3 for PY\n    are reported. The direction of the IN change is reported; the paper does not state it.",
 "new_string": "    with corrected p < 0.05 at load 1, 2 or 3 (the paper's test for the absence; \"all P > 0.05\"\n    covers Fig. 6c and Extended Data Fig. 5a,c). Partially reproduced when this holds at load 1\n    only. The direction of the IN change is reported; the paper does not state it."
}
```

```
The file claims/kussovska-2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kussovska-2025.yaml",
 "old_string": "    both are run. Reproduced when, under one reading, IN preferred has maintenance above\n    encoding with p < 0.05, IN nonpreferred does not, and PY has no comparison with p < 0.05\n    (the paper's tests, judged as written).",
 "new_string": "    both are run. Open, which PY comparisons the Results mean by \"stable CV2 across preferred\n    and nonpreferred trials during both encoding and maintenance\"; readings are (a) encoding\n    against maintenance within preferred and within nonpreferred trials (the code, lines\n    138-139, run once per trial type), (b) preferred against nonpreferred within encoding and\n    within maintenance (paired over cells). Reproduced when, under one reading, IN preferred\n    has maintenance above encoding with p < 0.05, IN nonpreferred does not, and PY has no\n    comparison with p < 0.05 (the paper's tests, judged as written)."
}
```

```
The file claims/kussovska-2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kussovska-2025.yaml",
 "old_string": "    a variant). The decay constant is taken as tau_decay of the ACG fit of acg-fit-yield on the\n    spikes of preferred (or nonpreferred) trials of each epoch; open, the trials (load 1 or all\n    loads), both run.",
 "new_string": "    a variant). The paper does not define the \"decay time constants\" of this test; the reading\n    taken is tau_decay of the ACG fit of acg-fit-yield (the only decay constant the Methods\n    define) on the spikes of preferred (or nonpreferred) trials of each epoch, and the outcome\n    rests on it. Open, the trials (load 1 or all loads), both run."
}
```

```
The file claims/kussovska-2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/kussovska-2025.yaml",
 "old_string": "    of periods (line 289). Reproduced when, under one reading, each of the four comparisons\n    shows more bursts after encoding with corrected p < 0.05.",
 "new_string": "    of periods (line 289). Reproduced when, under one reading, each of the four comparisons\n    shows more bursts after encoding with corrected p < 0.05. The Results also say the rate\n    rose \"across successive maintenance windows\" but report no test of M1 against M2 or M3;\n    those pairs are reported without deciding."
}
```

```
The file claims/kussovska-2025.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd $TMPDIR/hw; grep -n "counts >= 10\|All_cells\":\|== \"All_cells\"\|df_metadata_all_cells\[" "04_bursting/main_4c,d,6a,b.py" | head; grep -n "wilcoxon\|for a, b\|combinations" "04_bursting/main_4f-k,6c,d.py" | head
```

```
128:    elif category == "All_cells":
129:        return df_metadata_all_cells[df_metadata_all_cells['subject_id'] == subject_id]
144:    elif category == "All_cells":
183:    if category == "All_cells":
184:        counts = df_metadata_all_cells["subject_id"].value_counts()
185:        return counts[counts >= 10].index.tolist()
6:from scipy.stats import wilcoxon
280:                            p = wilcoxon(g1, g2, alternative='two-sided',
Shell cwd was reset to
```

**Agent**

Line references confirmed. Adding the check entry and rerunning the checker.

**Agent calls Bash**

```bash
cd  cat >> claims/kussovska-2025.yaml <<'EOF'
checks:
- date: '2026-11-10'
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig4c-encoding-bursts-vs-poisson, criterion. Added the peak spacing, 2 bins (140 ms) from the
    Methods and the code (line 17) as the main reading and the Results' "within 70 ms of a
    previous event" as a variant; the criterion used 140 ms without naming the conflict.
  - fig4c-encoding-bursts-vs-poisson, criterion. Added that the code's "all neurons" group keeps
    participants with at least 10 neurons (main_4c,d,6a,b.py:183-185).
  - fig4f-all-cells-epochs, criterion. The Results also say the rate rose across successive
    maintenance windows, with no test reported; those pairs are now reported without deciding.
  - fig6cd-celltype-epochs, statement and criterion. The paper says pyramidal burst rates were
    stable "across task epochs and load" (all P > 0.05, Fig. 6c and Extended Data Fig. 5a,c);
    the claim covered load 1 only. Loads 2 and 3 now enter the absence test, with partial
    reproduction when only load 1 holds.
  - fig6gh-in-concept-cv2, criterion. Which pyramidal comparisons "stable CV2 across preferred
    and nonpreferred trials during both encoding and maintenance" means was left unstated; both
    readings (epoch within trial type, as the code runs, and trial type within epoch) are named.
  - ext5gh-py-decay-preferred, criterion. The paper does not define the decay constants of this
    test; the criterion took ACG tau_decay as given. It is now named as the reading taken, with
    the outcome resting on it.
  - Not settled. The checker reports fig3h-early-vs-late-maintenance p 9.7e-12 as not found; the
    paper prints "9.70 × 10−12" (Results, Encoding and maintenance occupy distinct neural
    subspaces, paragraph 3), which the checker does not match for the trailing zero. The value is
    right.
  - Not settled. ext2-bursts-loads23 cites Extended Data Fig. 2b-m as the paper does, though the
    dPCA paragraph also assigns Extended Data Fig. 2 to dPCA details; the Extended Data are not in
    the text read, so the panel cannot be confirmed.
  - Not settled. The Extended Data figures and legends are not in the text read; the claims on
    them (ext1bc, ext1de, ext1f, ext1g, ext2, ext5bd, ext5gh, ext5ij, supp4) rest on the main-text
    sentences and name their measures as open.
EOF
python tools/claims_check.py claims/kussovska-2025.yaml paper/10.1101-2025.10.31.684900.txt; python -c "import yaml;yaml.safe_load(open('claims/kussovska-2025.yaml'))" && git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file for kussovska-2025 is ready for an attempt. I made six corrections, and three problems remain open.

**Checker:** `claims/kussovska-2025.yaml: 45 claims, 45 quotes, 74 statistical values, 1 problems`. The one problem is the value 9.7e-12 in `fig3h-early-vs-late-maintenance`. The paper prints it as "9.70 × 10−12", and the checker doesn't match the trailing zero. The value itself is correct. The file passes the schema check, and every quote matches the paper word for word.

**Review:** I checked every claim against the paper. I also cloned the paper's code (github.com/dariakussovska/heterogeneitywm at commit 5144fe8) and spot-checked the code the criteria cite: burst parameters, group splits, the GLM window, the Royer burst index, the dPCA split and its tests, and the CV2 script. The citations I checked are accurate. Statements, statistics and expected values match the paper. Selection thresholds are left out of the statistics, as they should be. Every main finding has a claim, and none comes from another source.

**Changes, by claim:**
- **`fig4c-encoding-bursts-vs-poisson`:**
  - The criterion used a 140 ms minimum gap between bursts without noting a conflict. The Methods and the code say 140 ms, which stays the main reading. The Results say 70 ms, now run as a variant.
  - In the code, the "all neurons" group only keeps participants with at least 10 neurons; the criterion now says so.
- **`fig4f-all-cells-epochs`:** The Results say burst rates rose across successive maintenance windows but report no test for it. Those comparisons are now reported without deciding the claim.
- **`fig6cd-celltype-epochs`:** The paper says pyramidal burst rates were stable "across task epochs and load", but the claim only tested load 1. The statement and criterion now cover loads 2 and 3. Holding at load 1 alone counts as partly reproduced.
- **`fig6gh-in-concept-cv2`:** The paper's sentence on stable pyramidal CV2 can mean two different comparisons. Both are now named: encoding against maintenance within each trial type (what the code runs), and preferred against nonpreferred trials within each epoch.
- **`ext5gh-py-decay-preferred`:** The paper never defines the "decay time constants" in this test. Using the autocorrelogram fit's decay constant is now marked as an assumption the result rests on.

**Still open:**
- The checker flag on 9.7e-12 above; the value is correct.
- `ext2-bursts-loads23` cites Extended Data Fig. 2b–m for bursting results, as the paper does. But the paper also uses Extended Data Fig. 2 for dPCA details, so the citation may be a mislabel in the paper. It can't be confirmed because the Extended Data aren't in the text.
- The Extended Data figures and their legends aren't in the text. The nine claims that rely on them depend only on the main-text sentences that cite them, and they name their measures as open.

I recorded all of this under `checks` in the file. Nothing was committed or pushed.

## End of run

27 turns, 4 minutes, $1.54 at API prices, result: success.
