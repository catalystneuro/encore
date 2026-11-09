# 001863 · claims · run 39553421859

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453 paper/ claims/001863 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -c paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2025.07.09.663970.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 150,400p claims/001453/*.yaml; head -60 tools/claims_check.py
```

```
data: with_labels
  depends_on:
  - stimulus-code-link
  criterion: For each fish, the mean of its median angular velocities for the rightward
    stimuli (right, forward right, backward right) minus the mean for the leftward stimuli
    (left, forward left, backward left). Reproduced when this difference is greater than zero
    in each species by a one-sided Wilcoxon signed-rank test at p < 0.05; partially reproduced
    when it holds in one species only. The per-stimulus species medians are reported as well.
- id: fig1h-zf-higher-angular-acceleration
  statement: Across directional stimuli ZF have higher angular acceleration than DC, and the
    distributions of the two species differ for every stimulus.
  source: Results, Optic flow induces angular matching and turns in DC, paragraph 2; Figure 1H
    (Kruskal-Wallis test with Bonferroni correction)
  quote: Across directional stimuli, ZF maintained higher angular acceleration than DC
  statistics:
  - test: Kruskal-Wallis test
    p: 0.05
    p_relation: "<"
    corrected: Bonferroni
  data: with_labels
[... 212 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"; curl -s https://api.dandiarchive.org/api/dandisets/001863/ | head -c 1500; echo; curl -s https://api.dandiarchive.org/api/dandisets/001863/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('name'));print(d.get('description'));print(d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[5000:])" | head -150
```

```
'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
      "type": "string",
      "minLength": 1
     }
    },
    "allOf": [
     {
      "not": {
       "required": [
        "quote",
        "inferred"
       ]
      }
     },
     {
      "if": {
       "properties": {
        "kind": {
         "const": "link"
        }
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/Smear-Lab/Olfactory-search-on-psychedelics repo && cd repo && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -100
```

```
aa80af0a153c6bf099e5668d27c9d88e2bfc033f Thu Aug 6 14:46:47 2026 -0700
./nwb_conversion/convert_session_to_nwb.py
./fmon-bpod/pid_map/pid_traces_1.png
./fmon-bpod/pid_map/pid_heatmap_1.png
./fmon-bpod/pid_map/pid_heatmap.py
./fmon-bpod/pid_map/pid_daq_plot.py
./fmon-bpod/pid_map/fmon_pid.m
./fmon-bpod/pid_map/fmon-pid.bonsai.layout
./fmon-bpod/pid_map/fmon-pid.bonsai
./fmon-bpod/pid_map/disconnect.py
./fmon-bpod/pid_map/connect.py
./fmon-bpod/nidaq_dat_plot.py
./fmon-bpod/legacy/notes_template.txt
./fmon-bpod/legacy/fmos_behavioral_assay2.0.zip
./fmon-bpod/legacy/bpod protocols/MFC_test/MFC_test.m
./fmon-bpod/legacy/bpod protocols/MFC_run/MFC_run.m
./fmon-bpod/legacy/bpod protocols/AvinashProtocols/helpAvinashProtocols.txt
./fmon-bpod/legacy/bpod protocols/AvinashProtocols/WaterCalibration/WaterCalibration.m
./fmon-bpod/legacy/bpod protocols/AvinashProtocols/Try_AOut/Try_AOut.m
./fmon-bpod/legacy/bpod protocols/AvinashProtocols/Sniff_TrigFV/Sniff_TrigFV.m
[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo && wc -l analysis/* README.md nwb_conversion/*; ls analysis/Figure1; cat README.md
```

```
1 analysis/Figure1
  1354 analysis/fig1_cleaned.Rmd
   692 analysis/fig2_cleaned.Rmd
   773 analysis/fig3_cleaned.Rmd
   476 analysis/fig4_cleaned.Rmd
   629 analysis/fig5_cleaned.Rmd
   257 analysis/occupancy_grandmean_gaussian_trimmed.m
    13 README.md
   446 nwb_conversion/convert_session_to_nwb.py
  4641 total
analysis/Figure1
# Olfactory-search-on-psychedelics

Code from Welch, Gonzales-Hess, Tarvin, Connor, Smear, "The impact of a
psychedelic drug on olfactory search behavior by mice," bioRxiv
[2025.07.09.663970](https://www.biorxiv.org/content/10.1101/2025.07.09.663970v1).
`analysis/` contains the figure-generating code (R Markdown and MATLAB);
`nwb_conversion/` contains the script used to convert the raw session
data into NWB format; `fmon-bpod/` contains the Bonsai/Bpod task-control
tooling.
[... 5 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo/analysis && grep -v '^\s*$' fig1_cleaned.Rmd | grep -v '^\s*#\s*$' | head -700
```

````
---
title: "Figure 1"
author: "Amanda Welch"
output: html_document
---
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```
<!--
Figure 1: task accuracy and engagement, DOI vs. saline, all paired by
mouse (one DOI session + one saline session per animal). 1B = odor-trial
accuracy; 1C = accuracy over the first 40 min, 5-min bins; 1D = trials
completed in 40 min; 1E = trial-initiation ("repoke") rate during the ITI.
The dose/session-number/sex lookup tables below (`doi_dose`/`saline_dose`/
`sex`) are re-typed by hand 3 times in this file (once per section) rather
than defined once and reused -- same session list each time, just
duplicated, not a discrepancy.
-->
# Figure 1
```{r}
[... 681 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/repo/analysis && grep -v '^\s*$' fig1_cleaned.Rmd | grep -v '^\s*#\s*$' | sed -n 700,1400p | grep -v -E '^\s*(theme|axis\.|legend\.|plot\.title|text = |size =|stroke|alpha|scale_|labs|geom_point|geom_abline|linetype|color = "|coord_fixed|guides)'
```

````
data_above40trials %>% 
  map(~summarise(group_by(., odor_setting),
                 trials_performed = length(odor_setting),
                 avg_trial_length = mean(trial_length),
                 sd_trial_length = sd(trial_length),
                 avg_iti_length = mean(iti_length, na.rm = TRUE),
                 sd_iti_length = sd(iti_length, na.rm = TRUE),
                 percent_correct = mean(success) * 100)) %>% 
  {. ->> full_stats} # save to its own variable in environment
```
```{r converting from large nested list to 1 df}
# create a list from df of session stats
stats_list <- do.call(rbind.data.frame, 
                      full_stats)
# create column that is row names (directory info)
stats_list <- setDT(stats_list, 
                    keep.rownames = TRUE)[]
```
```{r}
# extract session numbers from file paths for percent_correct_list
[... 406 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/repo/analysis && grep -v '^\s*$' fig2_cleaned.Rmd | grep -v -E '^\s*(#\s*$|theme|axis\.|legend\.|plot\.title|text = |size =|stroke|alpha|scale_|labs|geom_|linetype|color = "|coord_fixed|guides|stats\$id ==|accuracy\$id ==)'
```

````
---
title: "Figure 2"
author: "Amanda Welch"
output: html_document
---
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
library(ggplot2)
library(dplyr)
```
<!--
Figure 2: time spent at the reward port ("drinking" events, from each
session's drinking_data_iti_2.txt / drinking_data_incorrect_trials_iti_2.txt),
DOI vs. saline, split by correct (2A/2B) vs. incorrect (2C/2D) trials.
2A/2C = cumulative distribution of single-event duration, split further
into odor vs. omission trials; 2B/2D = per-mouse median duration, paired
scatter.
-->
```{r import data}
# mouse id, doi session number, and saline session number for each animal
[... 449 more lines not kept]
````

**Agent**

Figures 1 and 2 code read (Rmd files, session lists, tests). Continuing with Figures 3 to 5.

**Agent calls Bash**

```bash
cd $TMPDIR/repo/analysis && grep -v '^\s*$' fig3_cleaned.Rmd | grep -v -E '^\s*(#\s*$|theme|axis\.|legend\.|plot\.title|text = |size =|stroke|alpha|scale_|labs|geom_|linetype|color = "|coord_fixed|guides|stats\$id ==|accuracy\$id ==|c\(22|"F" = |values = c|intercept|shape = 1|inherit\.aes|guide = |x = "|y = "|width|position)'
```

````
---
title: "Figure 3"
author: "Amanda Welch"
output: html_document
---
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
library(gtools)
library(dplyr)
library(purrr)
library(tidyr)
library(stringr)
library(data.table)
library(ggplot2)
```
<!--
Figure 3: trial/ITI duration (3A/3B) and DLC nose-tracking speed (3C/3D),
DOI vs. saline, paired by mouse. 3C/3D depend on a separately-run DLC
tracking pipeline (see "dlc pipeline reference" chunk below, eval=FALSE --
included for reference/reproducibility, not executed by this notebook;
[... 523 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/repo/analysis && grep -v '^\s*$' fig4_cleaned.Rmd | grep -v -E '^\s*(#\s*$|theme|axis\.|legend\.|plot\.title|text = |size =|stroke|alpha|scale_|labs|geom_|linetype|color = "|coord_fixed|guides|"F" = |values = c|intercept|shape = 1|inherit\.aes|guide = |x = "|y = "|width|position)'
```

````
---
title: "Figure 4"
author: "amanda welch"
output: html_document
---
```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
library(R.matlab)
library(gtools)
library(dplyr)
library(stringr)
library(purrr)
library(tidyr)
library(ggplot2)
library(coin)
```
<!--
Figure 4: sniff frequency (from Task sniff params/*.mat, thermistor-derived
inhalation timing), DOI vs. saline. 4A/4B = per-mouse density overlays;
4C = pooled density, mean +/- SEM across mice; 4D = 4C split by trial
[... 321 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR/repo/analysis && grep -v '^\s*$' fig5_cleaned.Rmd | grep -v -E '^\s*(#\s*$|theme|axis\.|legend\.|plot\.title|text = |size =|stroke|alpha|scale_|labs|geom_|linetype|color = "|coord_fixed|guides|"F" = |values = c|intercept|shape = 1|inherit\.aes|guide = |x = "|y = "|width|position)'
```

```
---
title: "Figure 5"
author: "Amanda Welch"
output: html_document
---
this file produces the data (as csvs) and statistics for figure 5
(occupancy and head-twitch response location/rate). plotting is done
separately in occupancy_grandmean_gaussian.mlx (matlab) - this script
only writes the csvs that script reads in, plus runs the reported stats.
r and matlab code are kept in separate files intentionally.
<!--
Two things worth knowing before re-running this file:
- The `write.csv` calls for the occupancy_*.csv files that the MATLAB
  script needs (see "export occupancy csvs" chunk near the end) are
  commented out. A fresh run of this notebook will NOT regenerate those
  CSVs -- they only exist because someone ran that block manually at some
  point. Uncomment before relying on a from-scratch re-run.
- `bin_width` for the HTR grand-mean CSVs (below) is 100 px in this
  version of the file. If you find more than one copy of
  htr_grandmean_iti/htr_grandmean_within on the drive with different bin
[... 466 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/repo && grep -n -i "decision\|quadrant\|drink" -r fmon-bpod/README.md | head; sed -n 1,40p nwb_conversion/convert_session_to_nwb.py | head -40
```

```
#!/usr/bin/env python3
"""
convert_session_to_nwb.py -- Psychedelic_Sniff mission

Converts one session of the DOI-vs-saline olfactory search task dataset
(Welch, Gonzales-Hess, Tarvin, Connor, Smear -- "The impact of a
psychedelic drug on olfactory search behavior by mice," bioRxiv
2025.07.09.663970) into a single NWB file.

Source: /Volumes/TOSHIBA (external drive, read-only from this machine --
never written to). See CLAUDE.md for the full data-format mapping this
implements, and MISSION_NOTES.md for how each piece of that mapping was
verified (and what's still an open assumption).

PROTOTYPE STATUS, 2026-08-06: built and run on two example sessions (one
per cohort) for review. NOT yet run at scale on all 44 sessions -- see
MISSION_NOTES.md before doing that.

Scope, decided 2026-08-06: the 44 sessions listed in DLC_tracked_task
(22 mice x doi/saline), not the full 731-session newmove set.
[... 21 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001863/10.1101-2025.07.09.663970.yaml",
 "content": "# Claims for Welch, Gonzales-Hess, Tarvin, Connor & Smear (2025), \"The impact of a psychedelic\n# drug on olfactory search behavior by mice\", bioRxiv doi:10.1101/2025.07.09.663970, on dandiset\n# 001863.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21, under\n# docs/protocol.md version pilot-10 (Reader, steps 1 to 4). Nobody had analysed the dataset's data\n# when these criteria were written; the reader saw only the dandiset's title and description.\n#\n# Text read: the bioRxiv preprint, version 1, full text flattened from its JATS XML\n# (paper/10.1101-2025.07.09.663970.txt): Results, figure legends, Discussion and Materials and\n# methods. The preprint has no separate supplement file; the legends of its supplemental figures\n# (Figure 2A, 2B, 2C, 2D, 3, 4 and 5 supplemental) are in the text and were read. No PDF was\n# supplied, and none was needed.\n#\n# Code read: github.com/Smear-Lab/Olfactory-search-on-psychedelics at commit\n# aa80af0a153c6bf099e5668d27c9d88e2bfc033f (2026-08-06). The paper itself links only the rig\n# documentation (nghess.github.io/fmon-docs); this repository is the authors' code, named in the\n# dandiset's description and naming the paper in its README. It holds analysis/fig1_cleaned.Rmd to\n# fig5_cleaned.Rmd (the R code of each figure's statistics), a MATLAB plotting script for the\n# occupancy maps, the Bpod/Bonsai task software (fmon-bpod) and the NWB conversion script. The\n# reward-port durations (files drinking_data_iti_2.txt and drinking_data_incorrect_trials_iti_2.txt),\n# the sniff inhalation times (MATLAB \"Task sniff params\" files) and the DLC tracks are read\n# pre-computed by the Rmd files; the code that made them is not in the repository.\n#\n# The data the paper used. 22 C57Bl6/J mice (12 female, 10 male), each with one DOI session (3\n# mg/kg IP, 5 min before the task) and one saline session, crossed over at least a week apart, in\n# a two-alternative olfactory search task (odor, 2-phenylethanol, from the left or right end of the\n# arena; 10% odor omission trials; variable ITI of 1 to 15 s; fixed 40 min sessions). Measured\n# variables: per trial, trial type (odor or omission), odor side, success, start and end time; for\n# the 17 mice after the first cohort of 5, initiation-port pokes in the ITI and reward-port entries\n# and exits; video tracked by DeepLabCut (nose and other keypoints, 80 frames/s in the code);\n# nasal thermistor sniff signals (usable in 14 DOI and 13 saline sessions); manually scored\n# head-twitch response (HTR) onset times in the DOI sessions.\n#\n# The code's mouse and session list (mouse: DOI session, saline session), used in every figure:\n# 2174 57 56; 2181 42 41; 2182 32 31; 2183 34 33; 2185 41 40; 2191 25 21; 2195 17 20; 2196 18 16;\n# 2197 17 19; 2198 17 19; 2200 14 19; 2201 16 21; 2202 19 14; 2203 13 18; 2204 17 22; 2205 12 16;\n# 2208 18 14; 2209 14 18; 2210 17 13; 2211 13 17; 2212 16 13; 2213 14 18. Females are 2174, 2181,\n# 2191, 2200 to 2204 and 2210 to 2213. The first cohort (2174, 2181, 2182, 2183, 2185) lacks\n# reward-port and repoke records (Methods, Figure 1 and Figure 2) and, in the code, has its x\n# coordinate flipped (1200 minus x) to match the later camera setup. In the trial tables,\n# odor_setting 0 is an odor trial and 3 an omission trial.\n#\n# Method details fixed here from the code where the Methods are silent (each criterion cites\n# them): sessions with fewer than 40 trials are dropped (fig1, fig3); ITI duration is the next\n# trial's start minus this trial's end; accuracy is the mean of success over a session's odor\n# trials; speed is the frame-to-frame nose displacement times 80 frames/s times 0.0237 cm per\n# pixel, after DLC points with likelihood below 0.95 or a jump above 8 pixels are interpolated,\n# frames above 160 cm/s dropped, and a frame's time taken as its index over 80 s; a frame or a\n# sniff is within a trial when its time lies between a trial's start and end, and in the ITI\n# otherwise.\n#\n# The paper is not consistent with itself on three points, recorded in the criteria: the Results\n# name the Wilcoxon rank-sum test for the speed comparisons of Figure 3C, 3D and its supplement,\n# while the Methods and the code use the paired signed-rank test; the Methods give the sniff\n# duration limits as \"10 s\" and \"1000 s\"; the Methods say HTRs were marked manually, while the\n# code reads HTR times from a folder it calls automated detection and from a manually scored one.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001863\"\npaper: doi:10.1101/2025.07.09.663970\nclaims:\n- id: fig1b-accuracy-lower-doi\n  statement: Mice are less accurate in the olfactory search task in the DOI session than in the\n    saline session, going more often to the incorrect side.\n  source: Results, DOI alters olfactory search behavior, paragraph 2; Figure 1B\n  quote: Indeed, mice more often navigated to the incorrect side of the arena in the DOI condition\n    ( Figure 1B ; Wilcoxon signed rank test, p = 0.024, n = 22)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.024\n    n: 22 mice\n  expected:\n  - quantity: mice with paired DOI and saline sessions\n    value: 22\n    tolerance: 0\n  criterion: As the Methods (Figure 1) and fig1_cleaned.Rmd define it, accuracy is the percent of\n    a session's odor trials (odor_setting 0) that were correct, sessions with fewer than 40 trials\n    dropped. A two-sided paired Wilcoxon signed-rank test of DOI against saline accuracy over the\n    mice. Reproduced when the median DOI minus saline difference is negative and p < 0.05;\n    partially reproduced when it is negative with 0.05 <= p < 0.1. Omission-trial accuracy, which\n    the code also tests, is reported as a variant.\n- id: fig1c-accuracy-time-bins\n  statement: Over the session, odor-trial accuracy in 5 min bins is higher in the saline condition\n    than the DOI condition after the first 10 min, except in the 30 to 35 min bin, so the effect is\n    spread across the session.\n  source: Results, DOI alters olfactory search behavior, paragraph 2; Figure 1C\n  quote: In odor trials, accuracy was higher in the saline condition after the first 10 min, except\n    for the 30 – 35 min bin ( Figure 1C ; Wilcoxon rank-sum test, p < 0.01 for time points within\n    10 – 25 min, p = 0.039 for 35 – 40 min)\n  statistics:\n  - about: bins 10 to 15, 15 to 20 and 20 to 25 min\n    test: Wilcoxon rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n  - about: bin 35 to 40 min\n    test: Wilcoxon rank-sum test\n    p: 0.039\n  criterion: As in the Methods (Figure 1) and fig1_cleaned.Rmd. Odor trials only; for each trial\n    the rolling accuracy, the percent correct of the session's odor trials up to and including\n    that one; trials binned by start time into 5 min bins from 0 to 40 min; per mouse and bin, the\n    mean rolling accuracy; per bin, a two-sided unpaired Wilcoxon rank-sum test of DOI against\n    saline mouse values, uncorrected (the Methods give the rank-sum test because some mice have no\n    trials in some bins). Reproduced when saline is higher at p < 0.05 in the bins 10 to 15, 15 to\n    20, 20 to 25 and 35 to 40 min, with p < 0.01 in the first three, and the 30 to 35 min bin is\n    not significant; partially reproduced when saline is higher at p < 0.05 in at least two of\n    those four bins. The 0 to 10 min and 25 to 30 min bins, which the text does not state\n    separately, are reported. The per-bin fraction correct (not rolling) is shown as a variant.\n- id: fig1d-fewer-trials\n  statement: Mice complete fewer trials in the 40 min DOI session than in the saline session.\n  source: Results, DOI alters olfactory search behavior, paragraph 3; Figure 1D\n  quote: Mice completed fewer trials in the DOI condition ( Figure 1D ; Wilcoxon signed rank test, p\n    = 0.011, n = 22)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.011\n    n: 22 mice\n  criterion: Trials completed is the number of trials in the session (the Methods, Figure 1, \"the\n    sum of all trials in a session\"). fig1_cleaned.Rmd counts only the odor trials (odor_setting\n    0) for this test, while the Methods' wording counts all trials; both are run, readings (a)\n    odor trials, the code, and (b) all trials, the Methods. A two-sided paired Wilcoxon\n    signed-rank test over the 22 mice. Reproduced when, under a reading, DOI is lower with p <\n    0.05.\n- id: fig1d-fewer-trials-females-only\n  statement: The drop in trials completed under DOI is driven by females; female mice perform fewer\n    trials on DOI than saline, while male mice show no significant difference.\n  source: Results, DOI alters olfactory search behavior, paragraph 3; Figure 1D\n  quote: This effect was driven by female mice; female mice performed fewer trials on DOI compared\n    to saline ( Figure 1D ; Wilcoxon signed rank test, p = 0.011, n = 12), whereas male mice did not\n    show a significant difference ( Figure 1D ; Wilcoxon signed rank test, p = 0.39, n = 10)\n  statistics:\n  - about: females, DOI against saline\n    test: Wilcoxon signed rank test\n    p: 0.011\n    n: 12 female mice\n  - about: males, DOI against saline\n    test: Wilcoxon signed rank test\n    p: 0.39\n    n: 10 male mice\n  depends_on:\n  - fig1d-fewer-trials\n  criterion: The trial counts of fig1d-fewer-trials under both of its readings, split by sex\n    (females as listed in the opening comment, from the code). Two-sided paired Wilcoxon\n    signed-rank tests within each sex, as in fig1_cleaned.Rmd. Reproduced when, under a reading,\n    females are lower on DOI at p < 0.05 and males do not differ at p < 0.05; partially\n    reproduced when only one of the two holds.\n- id: fig1e-repoke-no-difference\n  statement: Mice poke into the initiation port during the ITI at the same rate in the DOI and\n    saline conditions, showing an equivalent motivation to do the task.\n  source: Results, DOI alters olfactory search behavior, paragraph 3; Figure 1E\n  quote: We found that mice poked into the initiation port, but there was not a significant\n    difference between conditions ( Figure 1E ; Wilcoxon signed rank test, p = 0.27, n = 17)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.27\n    n: 17 mice\n  criterion: A claim of absence. As in the Figure 1E legend and fig1_cleaned.Rmd, the repoke rate\n    is the session's number of initiation-port pokes during ITIs divided by the number of ITIs\n    (trials minus one), for the 17 mice after the first cohort. Two-sided paired Wilcoxon\n    signed-rank test, DOI against saline. Reproduced when p >= 0.05, not reproduced when p <\n    0.05; the median difference is reported either way.\n- id: iti-false-report-no-difference\n  statement: Mice rarely enter a reward port during the ITI after a trial-initiation attempt, and\n    DOI does not make them do so more than saline.\n  source: Results, DOI alters olfactory search behavior, paragraph 4\n  quote: Mice rarely entered the reward port during the ITI after trial initiation attempt\n    (Wilcoxon rank sum test, p = 1)\n  statistics:\n  - test: Wilcoxon rank sum test\n    p: 1\n    n: 17 mice\n  criterion: A claim of absence. The Methods (Figure 1) define a false odor report as an\n    initiation-port beam break followed by crossing the decision line during the ITI, for the 17\n    mice after the first cohort; the code in the repository does not compute it (the trial table\n    of the later cohort has a false_alarm column, which is used if the dataset holds it). The\n    per-mouse measure is not fixed; readings (a) the count of false reports per session and (b)\n    that count divided by the number of ITIs. The paper's test, a two-sided unpaired Wilcoxon\n    rank-sum test of DOI against saline sessions. Reproduced when p >= 0.05 under the readings,\n    not reproduced when p < 0.05; the counts per session are reported to show whether they are\n    rare. \"Rarely\" has no threshold in the paper and is not judged.\n- id: fig2a-correct-port-duration-doi-odor\n  statement: After correct trials, mice stay longer in the reward port on DOI odor trials than on\n    saline odor trials and saline omission trials.\n  source: Results, DOI impacts speed and timing, paragraph 1; Figure 2A\n  quote: Reward port duration was increased in the DOI odor trial condition compared to both saline\n    odor and saline odor omission trials ( Figure 2A ; Wilcoxon rank sum test, p < 0.001, n = 17)\n  statistics:\n  - test: Wilcoxon rank sum test, after Kruskal-Wallis, Bonferroni corrected\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 17 mice\n  criterion: Reward-port duration after a correct trial is the time from entering the reward port\n    to exiting it, re-entries not added (Methods, Figure 2), for the 17 mice after the first\n    cohort. Every event is a sample, pooled over mice, in four groups (DOI odor, DOI omission,\n    saline odor, saline omission). As the Methods and fig2_cleaned.Rmd do, a Kruskal-Wallis test\n    over the four groups, then pairwise two-sided Wilcoxon rank-sum tests with Bonferroni\n    adjustment over the six pairs (R pairwise.wilcox.test). Reproduced when DOI odor durations are\n    higher than both saline groups at adjusted p < 0.001; partially reproduced when both hold at\n    adjusted p < 0.05, or only one at p < 0.001. Which port entry counts is not fixed by the paper\n    (the files the code reads are pre-computed); readings (a) the first reward-port entry after the\n    trial's response, (b) the first entry within the 5 s window the Methods give for collecting a\n    reward. The per-mouse medians of fig2b are reported alongside.\n- id: fig2a-supp-no-sex-effect\n  statement: Reward-port duration after correct trials does not depend on sex in either condition.\n  source: Results, DOI impacts speed and timing, paragraph 1; Figure 2A supplemental\n  quote: We did not find a sex effect of condition ( Figure 2A supplemental , p = 1)\n  statistics:\n  - test: not named\n    p: 1\n  depends_on:\n  - fig2a-correct-port-duration-doi-odor\n  criterion: A claim of absence. The events of fig2a, grouped by condition and sex (DOI female,\n    DOI male, saline female, saline male). The paper does not name the test. Readings (a) a\n    Kruskal-Wallis test over the four groups, as fig2_cleaned.Rmd runs it; (b) pairwise two-sided\n    Wilcoxon rank-sum tests with Bonferroni adjustment over the six pairs, as the Methods give for\n    the duration groups and as the Results name for the matching test of Figure 2C, judged on\n    female against male within each condition. Reproduced when no reading finds a sex difference\n    at p < 0.05, not reproduced when every reading does; when they disagree, blocked as\n    methods_underspecified with both results shown. The p-values are reported.\n- id: fig2b-median-port-duration-correct\n  statement: Per mouse, the median reward-port duration after correct trials is longer in the DOI\n    session than in the saline session.\n  source: Results, DOI impacts speed and timing, paragraph 1; Figure 2B\n  quote: When comparing the median duration between conditions, mice in the DOI condition spent\n    longer in the reward port compared to saline ( Figure 2B ; Wilcoxon signed rank test, p = 0.002)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.002\n    n: 17 mice\n  depends_on:\n  - fig2a-correct-port-duration-doi-odor\n  criterion: The correct-trial events of fig2a, odor and omission trials together; per mouse and\n    condition the median duration; a two-sided paired Wilcoxon signed-rank test, DOI against\n    saline, as in fig2_cleaned.Rmd. Reproduced when DOI is higher with p < 0.05.\n- id: fig2b-supp-odor-trials-longer\n  statement: The longer median reward-port duration under DOI is driven by odor trials.\n  source: Results, DOI impacts speed and timing, paragraph 1; Figure 2B supplemental\n  quote: This effect was driven by the odor trial ( Figure 2B supplemental ; Wilcoxon signed rank\n    test, p = 0.001)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.001\n  depends_on:\n  - fig2a-correct-port-duration-doi-odor\n  criterion: As fig2b, with odor trials only, as in fig2_cleaned.Rmd. Reproduced when DOI is\n    higher with p < 0.05.\n- id: fig2b-supp-omission-no-difference\n  statement: After correct omission trials, the median reward-port duration does not differ between\n    DOI and saline.\n  source: Results, DOI impacts speed and timing, paragraph 1\n  quote: as we did not see a difference between median duration after an omission trial (Wilcoxon\n    signed rank test, p = 0.60)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.6\n  depends_on:\n  - fig2a-correct-port-duration-doi-odor\n  criterion: A claim of absence. As fig2b, with omission trials only, mice without events in both\n    conditions dropped, as in fig2_cleaned.Rmd; two-sided paired Wilcoxon signed-rank test.\n    Reproduced when p >= 0.05, not reproduced when p < 0.05; the median difference is reported.\n- id: fig2c-incorrect-port-duration\n  statement: After incorrect (unrewarded) trials, mice stay longest in the reward port on DOI odor\n    trials, longer than on DOI omission, saline odor and saline omission trials, and longer on\n    saline odor than saline omission trials.\n  source: Results, DOI impacts speed and timing, paragraph 2; Figure 2C\n  quote: We found an increased duration in DOI odor trials compared to DOI odor omission trials (\n    Figure 2C ; Wilcoxon rank sum test for all comparisons, p < 0.001), saline odor trials (p =\n    0.030), and saline odor omission trials (p < 0.001). Additionally, there was an increased\n    reward port duration for the saline odor trial compared to the saline odor omission trial (p <\n    0.001)\n  statistics:\n  - about: DOI odor against DOI omission\n    test: Wilcoxon rank sum test, Bonferroni corrected\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  - about: DOI odor against saline odor\n    test: Wilcoxon rank sum test, Bonferroni corrected\n    p: 0.03\n    corrected: Bonferroni\n  - about: DOI odor against saline omission\n    test: Wilcoxon rank sum test, Bonferroni corrected\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  - about: saline odor against saline omission\n    test: Wilcoxon rank sum test, Bonferroni corrected\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  criterion: As fig2a (same duration definition, same port-entry readings, same Kruskal-Wallis and\n    Bonferroni-adjusted pairwise rank-sum tests over the four groups, as in the Methods and\n    fig2_cleaned.Rmd), with the events after incorrect trials. Reproduced when all four stated\n    comparisons go in the stated direction at adjusted p < 0.05; partially reproduced when three\n    of the four do.\n- id: fig2c-supp-no-sex-difference\n  statement: After incorrect trials, reward-port duration does not differ between the sexes within\n    either condition.\n  source: Results, DOI impacts speed and timing, paragraph 2; Figure 2C supplemental\n  quote: Sex differences within each condition were not significant ( Figure 2C supplemental ,\n    Wilcoxon rank sum, p = 1)\n  statistics:\n  - test: Wilcoxon rank sum\n    p: 1\n  depends_on:\n  - fig2c-incorrect-port-duration\n  criterion: A claim of absence, judged on the paper's named test. The incorrect-trial events\n    grouped by condition and sex; pairwise two-sided Wilcoxon rank-sum tests with Bonferroni\n    adjustment over the six pairs of the four groups (the Methods' post hoc test); female against\n    male within DOI and within saline. Reproduced when neither is significant at adjusted p <\n    0.05, not reproduced when either is. The Kruskal-Wallis test over the four groups, which\n    fig2_cleaned.Rmd runs, is shown as a variant.\n- id: fig2d-median-incorrect-no-difference\n  statement: Per mouse, the median reward-port duration after incorrect trials does not differ\n    between DOI and saline.\n  source: Results, DOI impacts speed and timing, paragraph 2; Figure 2D\n  quote: When comparing the median duration between conditions, there was no difference between DOI\n    and saline ( Figure 2D ; Wilcoxon signed rank test, p = 0.21)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.21\n  depends_on:\n  - fig2c-incorrect-port-duration\n  criterion: A claim of absence. Per mouse and condition the median duration over incorrect-trial\n    events, odor and omission together; two-sided paired Wilcoxon signed-rank test, mice without\n    both values dropped, as in fig2_cleaned.Rmd. Reproduced when p >= 0.05, not reproduced when p\n    < 0.05; the median difference is reported.\n- id: fig2d-supp-omission-longer\n  statement: After incorrect omission trials, mice stay longer in the reward port in the DOI\n    condition than in the saline condition.\n  source: Results, DOI impacts speed and timing, paragraph 2; Figure 2D supplemental\n  quote: However, after an odor omission trial, mice spent longer in the reward port in the DOI\n    condition ( Figure 2D supplemental , Wilcoxon signed rank test, p = 0.049)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.049\n  depends_on:\n  - fig2c-incorrect-port-duration\n  criterion: As fig2d, with incorrect omission trials only, mice without both values dropped, as\n    in fig2_cleaned.Rmd. Reproduced when DOI is higher with p < 0.05; partially reproduced when it\n    is higher with 0.05 <= p < 0.1.\n- id: fig3a-odor-trial-duration-longer\n  statement: Mice take longer to complete odor trials in the DOI condition than in the saline\n    condition.\n  source: Results, DOI impacts speed and timing, paragraph 3; Figure 3A\n  quote: In odor trials, mice took longer to complete a trial in the DOI condition compared to the\n    saline condition ( Figure 3A ; Wilcoxon signed rank test, p < 0.001, n = 22)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.001\n    p_relation: \"<\"\n    n: 22 mice\n  criterion: Trial duration is trial end minus trial start; per mouse and condition the mean over\n    odor trials (Methods, Figure 3; fig3_cleaned.Rmd); two-sided paired Wilcoxon signed-rank test.\n    Reproduced when DOI is longer with p < 0.05.\n- id: fig3a-omission-duration-no-difference\n  statement: The duration of omission trials does not differ between DOI and saline.\n  source: Results, DOI impacts speed and timing, paragraph 3\n  quote: In contrast, there was no difference in trial duration in omission trials between DOI and\n    saline (Wilcoxon signed rank test, p = 0.26, n = 22)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.26\n    n: 22 mice\n  criterion: A claim of absence. As fig3a with omission trials. Reproduced when p >= 0.05, not\n    reproduced when p < 0.05; the median difference is reported.\n- id: fig3b-iti-duration-no-difference\n  statement: ITI duration does not differ between DOI and saline.\n  source: Results, DOI impacts speed and timing, paragraph 3; Figure 3B\n  quote: However, there was no difference in ITI duration between conditions ( Figure 3B ; Wilcoxon\n    signed rank test, p = 0.19, n = 22)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.19\n    n: 22 mice\n  criterion: A claim of absence. ITI duration is the next trial's start minus this trial's end\n    (Methods, Figure 3); per mouse and condition the mean over all trials of the session, as in\n    fig3_cleaned.Rmd; two-sided paired Wilcoxon signed-rank test. Reproduced when p >= 0.05, not\n    reproduced when p < 0.05; the median difference is reported.\n- id: fig3c-speed-within-trial-lower\n  statement: DOI lowers movement speed within trials, odor and omission trials pooled, compared with\n    saline.\n  source: Results, DOI impacts speed and timing, paragraph 4; Figure 3C\n  quote: We found that DOI decreased movement speed both within trial ( Figure 3C ; Wilcoxon rank\n    sum test, p = 0.011, pooled trial type)\n  statistics:\n  - test: Wilcoxon rank sum test\n    p: 0.011\n  criterion: Nose-keypoint speed as in the Methods (Figure 3) and fig3_cleaned.Rmd (see the opening\n    comment), per mouse and condition the mean over the frames within any trial. The Results name\n    the rank-sum test; the Methods (\"For trial durations, ITI duration, and overall task speed,\n    Wilcoxon signed rank tests were used\") and the code use the two-sided paired signed-rank test,\n    which decides here, the Methods coming first; the unpaired rank-sum test is shown as a\n    variant. Reproduced when DOI is lower with p < 0.05.\n- id: fig3d-speed-iti-lower\n  statement: DOI lowers movement speed during the ITI compared with saline.\n  source: Results, DOI impacts speed and timing, paragraph 4; Figure 3D\n  quote: and during the ITI ( Figure 3D ; Wilcoxon rank sum test, p = 0.036) compared to saline\n  statistics:\n  - test: Wilcoxon rank sum test\n    p: 0.036\n  criterion: As fig3c, with the frames outside every trial. Reproduced when DOI is lower with p <\n    0.05 under the paired signed-rank test; the rank-sum test is shown as a variant.\n- id: fig3supp-odor-trial-speed-no-difference\n  statement: Within odor trials alone, speed does not differ between DOI and saline sessions.\n  source: Results, DOI impacts speed and timing, paragraph 4; Figure 3 supplemental\n  quote: In odor trials specifically, the speed between DOI and saline sessions were not different (\n    Figure 3 supplemental ; Wilcoxon rank sum test, p = 0.059)\n  statistics:\n  - test: Wilcoxon rank sum test\n    p: 0.059\n  criterion: A claim of absence. As fig3c with the frames of odor trials only. The Results name\n    the rank-sum test; the Methods and fig3_cleaned.Rmd (which runs every pair of the six\n    condition and period means as paired signed-rank tests, uncorrected) use the two-sided paired\n    signed-rank test, which decides, the Methods coming first. Reproduced when p >= 0.05, not\n    reproduced when p < 0.05. The rank-sum result and the median difference are reported.\n- id: fig3supp-doi-iti-slower-than-odor\n  statement: Within the DOI condition, mice move more slowly in the ITI than in odor trials.\n  source: Results, DOI impacts speed and timing, paragraph 4; Figure 3 supplemental\n  quote: Within the DOI condition, speed was decreased in the ITI compared to an odor trial ( Figure\n    3 supplemental ; Wilcoxon signed rank test, p < 0.001)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.001\n    p_relation: \"<\"\n  criterion: Per mouse, DOI session mean speeds over ITI frames and over odor-trial frames (as\n    fig3c); two-sided paired signed-rank test, as in fig3_cleaned.Rmd. Reproduced when ITI is\n    slower with p < 0.05.\n- id: fig3supp-doi-omission-no-difference\n  statement: Within the DOI condition, speed does not differ between odor and omission trials, nor\n    between the ITI and omission trials.\n  source: Results, DOI impacts speed and timing, paragraph 4\n  quote: However, there was no difference in speed between the odor and odor omission trials in the\n    DOI condition (Wilcoxon rank sum test, p = 0.21), nor the ITI and odor omission trials\n    (Wilcoxon rank sum, p = 0.068)\n  statistics:\n  - about: DOI odor against DOI omission\n    test: Wilcoxon rank sum test\n    p: 0.21\n  - about: DOI ITI against DOI omission\n    test: Wilcoxon rank sum\n    p: 0.068\n  criterion: A claim of absence, for two comparisons. Per-mouse DOI session mean speeds over\n    odor-trial, omission-trial and ITI frames (as fig3c); two-sided paired signed-rank tests, the\n    Methods' test and the code's, uncorrected; the rank-sum tests the Results name are shown as\n    variants. Reproduced when neither comparison has p < 0.05; partially reproduced when one does;\n    not reproduced when both do. Effect sizes are reported.\n- id: fig3supp-saline-iti-slower\n  statement: In saline sessions, mice move more slowly in the ITI than in odor trials and in\n    omission trials.\n  source: Results, DOI impacts speed and timing, paragraph 4\n  quote: In comparison, in saline sessions the ITI speed was slower compared to odor (p = 0.002)\n    and odor omission trials (p = 0.017)\n  statistics:\n  - about: saline ITI against saline odor\n    test: not named\n    p: 0.002\n  - about: saline ITI against saline omission\n    test: not named\n    p: 0.017\n  criterion: Per-mouse saline session mean speeds over ITI, odor-trial and omission-trial frames\n    (as fig3c); two-sided paired signed-rank tests, uncorrected, as in fig3_cleaned.Rmd and the\n    Methods; the rank-sum test is shown as a variant. Reproduced when the ITI is slower than both\n    at p < 0.05; partially reproduced when it is slower than one.\n- id: fig3supp-saline-odor-omission-no-difference\n  statement: In saline sessions, speed does not differ between odor and omission trials.\n  source: Results, DOI impacts speed and timing, paragraph 4\n  quote: Speed within the odor and odor omission trials were not different in the saline condition\n    (Wilcoxon rank sum, p = 0.54)\n  statistics:\n  - test: Wilcoxon rank sum\n    p: 0.54\n  criterion: A claim of absence. Per-mouse saline session mean speeds over odor-trial and\n    omission-trial frames (as fig3c); two-sided paired signed-rank test, the Methods' and code's;\n    the rank-sum test is shown as a variant. Reproduced when p >= 0.05, not reproduced when p <\n    0.05; the median difference is reported.\n- id: fig4abc-sniff-frequency-higher\n  statement: Pooling all sessions with a usable sniff signal, sniff frequency is higher in DOI\n    sessions than in saline sessions.\n  source: Results, DOI increases sniff frequency, paragraph 1; Figure 4A to 4C\n  quote: When all sessions with sniff measurement were combined, sniff frequency was higher in DOI\n    sessions ( Figure 4A – C ; Fisher-Pitman Permutation test, Z = 24.9, p < 0.001)\n  statistics:\n  - test: Fisher-Pitman Permutation test\n    statistic: Z = 24.9\n    p: 0.001\n    p_relation: \"<\"\n    n: 14 DOI and 13 saline sessions\n  expected:\n  - quantity: DOI sessions with usable sniff signal\n    value: 14\n    tolerance: 0\n  - quantity: saline sessions with usable sniff signal\n    value: 13\n    tolerance: 0\n  criterion: Sniff frequency is 1000 over the interval in ms between consecutive inhalation times\n    (Methods, Figure 4; fig4_cleaned.Rmd), sniffs with a missing exhalation dropped. Further\n    exclusions from the Methods, applied when the dataset gives raw inhalation times; sniff\n    durations below the 5th or above the 95th percentile, read per session (the code's MATLAB\n    output is per session), and durations outside 10 to 1000, read as ms (the Methods print \"s\",\n    which cannot hold for a sniff). Where the dataset holds only the thermistor signal, the\n    Methods give a 25 ms moving-window smoothing and peak and trough detection, and the detection\n    settings are open; the inhalation times are then a deviation. Sessions are those with a\n    usable signal; the code drops DOI sessions 2195 17 and 2198 17 and saline sessions 2198 19 and\n    2213 18 as faulty, and the counts are compared with 14 and 13. Every sniff is a sample; a\n    two-sample Fisher-Pitman permutation test (coin oneway_test, 10000 resamples) of DOI against\n    saline. Reproduced when the DOI mean frequency is higher with p < 0.05.\n- id: fig4supp-ks-every-mouse\n  statement: Every mouse with matched DOI and saline sniff sessions has a sniff-frequency\n    distribution shifted higher in the DOI condition.\n  source: Results, DOI increases sniff frequency, paragraph 1; Figure 4 supplemental\n  quote: All mice with a matched DOI and saline session had a higher-shifted distribution sniff\n    rates in the DOI condition ( Figure 4 supplemental ; Kolmogorov-Smirnov test, p < 0.001 for 13\n    of 13 mice)\n  statistics:\n  - test: Kolmogorov-Smirnov test\n    p: 0.001\n    p_relation: \"<\"\n    n: 13 mice\n  expected:\n  - quantity: mice with matched sessions and a significant DOI shift\n    value: 13\n    tolerance: 0\n  depends_on:\n  - fig4abc-sniff-frequency-higher\n  criterion: The sniff frequencies of fig4abc; for each mouse with usable DOI and saline sessions,\n    a one-sided two-sample Kolmogorov-Smirnov test that DOI frequencies are stochastically larger\n    (R ks.test(doi, saline, alternative = \"less\"), as in fig4_cleaned.Rmd). Reproduced when every\n    matched mouse has p < 0.001 and their number is within the tolerance; partially reproduced\n    when at least two thirds of them do.\n- id: fig4d-sniff-frequency-by-period\n  statement: Mice sniff faster in the DOI condition in odor trials, in omission trials and during\n    the ITI.\n  source: Results, DOI increases sniff frequency, paragraph 1; Figure 4D\n  quote: 'mice sniffed faster in the DOI condition for each trial type and during the ITI ( Figure\n    4D ; Fisher-Pitman Permutation test for all trial types; Odor trials: Z = 3.38, p < 0.001;\n    Omission trials: Z = 2.71, p= 0.007; ITI: Z = 18.4, p < 0.001)'\n  statistics:\n  - about: odor trials\n    test: Fisher-Pitman Permutation test\n    statistic: Z = 3.38\n    p: 0.001\n    p_relation: \"<\"\n  - about: omission trials\n    test: Fisher-Pitman Permutation test\n    statistic: Z = 2.71\n    p: 0.007\n  - about: ITI\n    test: Fisher-Pitman Permutation test\n    statistic: Z = 18.4\n    p: 0.001\n    p_relation: \"<\"\n  depends_on:\n  - fig4abc-sniff-frequency-higher\n  criterion: The sniffs of fig4abc, each placed by its inhalation time in an odor trial, an\n    omission trial (between a trial's start and end) or the ITI (otherwise), as in\n    fig4_cleaned.Rmd; a Fisher-Pitman permutation test (10000 resamples) of DOI against saline in\n    each period. Reproduced when DOI is higher with p < 0.05 in all three; partially reproduced in\n    two.\n- id: fig4e-median-sniff-no-difference\n  statement: Per-mouse median sniff frequency does not differ between DOI and saline.\n  source: Results, DOI increases sniff frequency, paragraph 1; Figure 4E\n  quote: We did not observe a difference in median sniff frequencies between conditions ( Figure 4E\n    ; Wilcoxon signed rank test; p = 0.11)\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.11\n  depends_on:\n  - fig4abc-sniff-frequency-higher\n  criterion: A claim of absence. Per mouse and condition the median of the sniff frequencies of\n    fig4abc; two-sided paired Wilcoxon signed-rank test over mice with both, as in\n    fig4_cleaned.Rmd. Reproduced when p >= 0.05, not reproduced when p < 0.05; the median\n    difference is reported.\n- id: fig5ab-occupancy-similar\n  statement: Mice occupy the arena similarly in the DOI and saline conditions; DOI does not make\n    them spend more time in task-irrelevant areas such as the corners or spread more evenly.\n  source: Results, Mice occupy allocentric space similarly but head twitch preferentially in\n    proximity to odor ports, paragraph 1; Figure 5A and 5B\n  quote: Contrary to this prediction, mice showed similar occupancy across DOI and saline conditions\n    ( Figure 5A, B )\n  criterion: The paper reports no test. Occupancy is the fraction of a session's tracked frames in\n    each 1 cm bin (48 pixels in fig5_cleaned.Rmd), from the nose keypoint, frames above 160 cm/s\n    dropped, x flipped for the first cohort; the maps are the mean over the 22 mice (Figure 5A\n    legend, Methods Figure 5, code). The measures come from the prediction the paper tested (\"more\n    time in areas irrelevant to the task such as corners of the arena, with a more even\n    distribution\"); per mouse and condition (a) the Shannon entropy of the occupancy map and (b)\n    the fraction of frames in the four arena corners, with the corner size open, read as squares\n    of 5 cm and of 10 cm side (choices, as the paper fixes none). Each is compared DOI against\n    saline with a two-sided paired Wilcoxon signed-rank test, the Methods' paired test.\n    Reproduced when no measure differs at p < 0.05; not reproduced when every one does with DOI\n    higher; otherwise blocked as methods_underspecified with all results shown. The Pearson\n    correlation between the two grand-mean maps is reported as a description.\n- id: fig5supp-htr-within-trial-x-not-y\n  statement: During trials, HTR rate (normalized to occupancy) varies with the X coordinate of the\n    arena but not with the Y coordinate.\n  source: Results, Mice occupy allocentric space similarly but head twitch preferentially in\n    proximity to odor ports, paragraph 2; Figure 5 supplemental A\n  quote: During a trial, HTR rate occurred throughout the arena without spatial predictability on\n    the Y-coordinate ( Figure 5 supplemental ; Permutation test, p = 0.92), but with preference for\n    the X-coordinate ( Figure 5 supplemental ; Permutation test, p = 0.002)\n  statistics:\n  - about: Y coordinate\n    test: Permutation test\n    p: 0.92\n  - about: X coordinate\n    test: Permutation test\n    p: 0.002\n  criterion: DOI sessions with HTR times. As in the Methods (Figure 5) and fig5_cleaned.Rmd; nose\n    position at each frame (x flipped for the first cohort, frames above 160 cm/s dropped); each\n    HTR assigned to the frame nearest its time; the arena in bins of 100 pixels (about 2.5 cm),\n    the last bin column and row (x bin 1200, y bin 700) dropped; per mouse and bin, HTRs within\n    trials over within-trial occupancy, in HTR per min, bins the mouse visited in the session\n    filled with zero where it had no within-trial time. Statistic the Pearson correlation of the\n    per-mouse, per-bin rates with bin x and with bin y; null from 10000 permutations of the bin\n    coordinates; two-sided p as the fraction of permuted absolute correlations at or above the\n    observed one (seed 123 in the code, a choice that cannot change the outcome). Reproduced when\n    p < 0.05 for x and p >= 0.05 for y; partially reproduced when only one holds. The sign of the\n    x correlation is reported, positive meaning toward the odor and reward ports.\n- id: fig5e-htr-combined-x\n  statement: With trial and ITI periods combined, mice head-twitch more often closer to the odor\n    end of the arena, as the X coordinate increases.\n  source: Results, Mice occupy allocentric space similarly but head twitch preferentially in\n    proximity to odor ports, paragraph 2; Figure 5E\n  quote: and when conditions were combined ( Figure 5E ; Permutation test, p < 0.001 for\n    X-coordinates)\n  statistics:\n  - test: Permutation test\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: mice in the HTR rate map\n    value: 22\n    tolerance: 0\n  depends_on:\n  - fig5supp-htr-within-trial-x-not-y\n  criterion: As fig5supp-htr-within-trial-x-not-y with all frames of the DOI session (trial and\n    ITI combined), rows for the bins each mouse occupied, as fig5_cleaned.Rmd does. Reproduced\n    when the x correlation is positive (rate rising toward the odor and reward ports) with p <\n    0.001; partially reproduced when it is positive with p < 0.05.\n- id: fig5supp-htr-iti-x\n  statement: During the ITI, mice head-twitch more often toward the end of the arena past the\n    decision line (as X increases), but not specifically next to the reward ports on the Y\n    coordinate.\n  source: Results, Mice occupy allocentric space similarly but head twitch preferentially in\n    proximity to odor ports, paragraph 2; Figure 5 supplemental B\n  quote: Similarly, during the ITI, we found that mice HTR more frequently closer to the end of the\n    arena after crossing the decision line (as X-coordinate increases), but not immediately next to\n    the reward ports (on the Y-coordinate)\n  criterion: The paper gives no test for the ITI alone and the code runs none; the test of\n    fig5supp-htr-within-trial-x-not-y is applied to ITI frames and ITI HTRs (per-mouse rates over\n    ITI occupancy, the code's htr_normalized_permouse_iti, edge bins dropped), the reading the\n    paper's \"Similarly\" implies. Reproduced when the x correlation is positive with p < 0.05 and\n    the y test has p >= 0.05; partially reproduced when only the x part holds.\n- id: fig5f-htr-rate-trial-vs-iti\n  statement: HTR rate does not differ between time within trials and time in the ITI.\n  source: Results, Mice occupy allocentric space similarly but head twitch preferentially in\n    proximity to odor ports, paragraph 2; Figure 5F\n  quote: We normalized HTR rate based on within trial and ITI duration and found no difference in\n    HTR rate based on whether the mouse was in a trial or ITI ( Figure 5F ; Wilcoxon signed rank,\n    p = 1)\n  statistics:\n  - test: Wilcoxon signed rank\n    p: 1\n  criterion: A claim of absence. As in fig5_cleaned.Rmd; per DOI session, HTRs whose time lies\n    within a trial divided by the summed trial durations, and the other HTRs divided by 2400 s\n    minus the summed trial durations, in HTR per min; two-sided paired Wilcoxon signed-rank test.\n    Reproduced when p >= 0.05, not reproduced when p < 0.05; the median difference is reported.\n- id: fig5supp-htr-no-sex-difference\n  statement: HTR rate over the 40 min DOI session does not differ between male and female mice.\n  source: Results, Mice occupy allocentric space similarly but head twitch preferentially in\n    proximity to odor ports, paragraph 2; Figure 5 supplemental C\n  quote: Additionally, we did not see a sex difference in HTR rate over the 40 m session ( Figure 5\n    supplemental ; Wilcoxon rank sum, p = 0.31)\n  statistics:\n  - test: Wilcoxon rank sum\n    p: 0.31\n  criterion: A claim of absence. Per DOI session the number of HTRs divided by 40 min; a two-sided\n    Wilcoxon rank-sum test (normal approximation, exact = FALSE in fig5_cleaned.Rmd), female\n    against male. Reproduced when p >= 0.05, not reproduced when p < 0.05; the group medians are\n    reported.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001863/10.1101-2025.07.09.663970.yaml paper/10.1101-2025.07.09.663970.txt; grep -n -i "—\|rather" claims/001863/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -E '^\s{4,}[^-#].*: ' claims/001863/*.yaml | grep -v -E '^\S+:\s+(about|test|p|p_relation|n|statistic|corrected|quantity|value|tolerance|unit|statement|source|quote|criterion|inferred):' ; grep -n -E '^  [a-z_]+: .*: ' claims/001863/*.yaml; grep -c "statistics:" claims/001863/*.yaml; grep -c "criterion:" claims/001863/*.yaml
```

```
538:    4D ; Fisher-Pitman Permutation test for all trial types; Odor trials: Z = 3.38, p < 0.001;
539:    Omission trials: Z = 2.71, p= 0.007; ITI: Z = 18.4, p < 0.001)'
33
35
```

**Agent**

I wrote `claims/001863/10.1101-2025.07.09.663970.yaml`. The quote checker reports 35 claims, 35 quotes, 43 statistical values and 0 problems. Nothing is committed.

**Text read:** the bioRxiv preprint, version 1, full text from its JATS XML: Results, figure legends, Discussion and Methods. There is no separate supplement file, but the legends of all the supplemental figures are in the text and I read them. No PDF was supplied and none was needed. Nothing the claims rest on is missing.

**Code read:** github.com/Smear-Lab/Olfactory-search-on-psychedelics at commit aa80af0a. The paper itself links only the rig documentation. This repository is the authors' code: the dandiset description names it, and its README names the paper. It holds R Markdown files with each figure's statistics (`fig1_cleaned.Rmd` to `fig5_cleaned.Rmd`), a MATLAB occupancy plotting script, the task software and the NWB conversion script. Some inputs those files read were made by code that is not in the repository: the reward-port durations, the sniff inhalation times and the DeepLabCut (pose-tracking) tracks. The code fixes the mouse and session list (22 mice, which session was DOI and which saline), the 40-trial minimum per session, the rolling accuracy measure, the speed pipeline (80 fps, 0.0237 cm/pixel, 160 cm/s cutoff) and the head-twitch (HTR) spatial permutation statistic.

**Claims:** 35, all with quotes. 33 have statistics, all 35 have criteria, and 4 have expected values.

**Where the paper disagrees with itself:**
- **Speed tests:** the Results name the Wilcoxon rank-sum test for the speed comparisons (Figure 3C, 3D and supplement). The Methods and the code use the paired signed-rank test. The Methods decide, and rank-sum is shown as a variant.
- **Sniff limits:** the Methods print them as "10 s" and "1000 s". I read them as milliseconds.
- **HTR scoring:** the Methods say HTRs were marked by hand. The code also reads HTR times from a folder it describes as automated detection.

**Details left open, with the readings named:**
- **Trials completed (1D, and 1D by sex):** the code counts odor trials only, the Methods count all trials. Both are named readings.
- **False odor reports in the ITI:** the code does not compute them. The measure is either a count per session or that count divided by the number of ITIs.
- **Which reward-port entry counts (Figure 2):** the first entry after the trial's response, or the first entry within the 5 s reward window.
- **Sex test for Figure 2A:** the test is not named. It is either the code's Kruskal-Wallis test or Bonferroni-corrected pairwise rank-sum tests. If they disagree, the claim is blocked as underspecified.
- **Sniff exclusions:** the 5th and 95th percentile cut is read per session, and the duration limits in milliseconds. If the dataset holds only the raw thermistor signal, the peak-detection settings are open. Which sessions count as usable: the code drops four by name, and the counts are checked against 14 DOI and 13 saline.
- **Occupancy "similar" (Figure 5A, B):** the paper gives no test. I took the measures from the prediction the paper says it tested: the entropy of each mouse's occupancy map, and the fraction of time in the corners. The corner size is not given, so 5 cm and 10 cm squares are named, and both sizes are my own choices. Each is compared with the paired signed-rank test. If the measures disagree, the claim is blocked.
- **HTR position during the ITI:** the paper gives no test and the code runs none. The within-trial permutation test is applied to ITI frames, which is what the paper's "Similarly" implies.
- **Figure 1C bins:** the 0 to 10 min and 25 to 30 min bins are not reported separately in the text. They are reported but not judged.

**Missing from the paper:** no claim lacks something it needs from the paper. The ITI false-report measure, the reward-port duration files and the sniff preprocessing are not in the code, so those claims rest on the Methods text alone.

## End of run

19 turns, 5 minutes, result: success.
