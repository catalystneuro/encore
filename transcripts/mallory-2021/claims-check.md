# mallory-2021 · claims-check · run 42840666390

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper | grep -i mallory; cat claims/mallory-2021.yaml; grep -n "Reader" -A60 docs/protocol.md | head -150
```

```
<persisted-output>
Output too large (68.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/251794c9-c18d-4091-bc84-32f834f45160/tool-results/bs8s8egvb.txt

Preview (first 2KB):
# Claims for Mallory, Hardcastle, Campbell, Attinger, Low, Raymond & Giocomo (2021), Nat Commun
# 12, 671, tested on DANDI:000053.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol as stated in docs/protocol.md.
#
# Text read. The version of record (paper/10.1038-s41467-021-20936-8.txt, Europe PMC full text
# of PMC7844029), with its Methods, figure legends and the three supplementary files from the
# PMC Open Access set, the Supplementary Information (legends of Supplementary Figures 1 to 12),
# the peer review file (an editorial note only) and the reporting summary. The PDFs of the
# supplement were not opened; no claim needed a number printed only inside a figure.
#
# Code read. The Code availability statement links two MATLAB repositories.
# https://github.com/khardcastle/spline-lnp-model at commit 34b470f (2018-05-10) holds the
# spline LN Poisson model (cardinal spline regressors, spline_1d.m, spline_1d_circ.m,
# spline_2d.m; Poisson likelihood with an L2 penalty of weight 1, glm_model.m; 10-fold
# cross-validation, fit_model_kfold.m and compute_test_train_ind.m; forward search with a
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/251794c9-c18d-4091-bc84-32f834f45160/tool-results/bs8s8egvb.txt"
}
```

```
1	# Claims for Mallory, Hardcastle, Campbell, Attinger, Low, Raymond & Giocomo (2021), Nat Commun
2	# 12, 671, tested on DANDI:000053.
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
4	# 2026-11-10, protocol as stated in docs/protocol.md.
5	#
6	# Text read. The version of record (paper/10.1038-s41467-021-20936-8.txt, Europe PMC full text
7	# of PMC7844029), with its Methods, figure legends and the three supplementary files from the
8	# PMC Open Access set, the Supplementary Information (legends of Supplementary Figures 1 to 12),
9	# the peer review file (an editorial note only) and the reporting summary. The PDFs of the
10	# supplement were not opened; no claim needed a number printed only inside a figure.
11	#
12	# Code read. The Code availability statement links two MATLAB repositories.
13	# https://github.com/khardcastle/spline-lnp-model at commit 34b470f (2018-05-10) holds the
14	# spline LN Poisson model (cardinal spline regressors, spline_1d.m, spline_1d_circ.m,
15	# spline_2d.m; Poisson likelihood with an L2 penalty of weight 1, glm_model.m; 10-fold
16	# cross-validation, fit_model_kfold.m and compute_test_train_ind.m; forward search with a
17	# one-sided signed-rank test at 0.05 and a final signed-rank test of the selected model against
18	# 0, forward_search_kfold.m; log-likelihood increase over a mean rate model in bits per spike,
19	# compute_llh.m; the reduced-model contribution, compute_llh_increase.m) and an example script
20	# for position, head direction and speed (create_glm.m). https://github.com/GiocomoLab/
[... 1021 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/251794c9-c18d-4091-bc84-32f834f45160/tool-results/bs8s8egvb.txt",
 "offset": 1042
}
```

```
1042	    unit: bits per spike
1043	  criterion: As fig3c-freely-moving-model-fit, on the head-fixed cells.
1044	- id: fig7e-eye-no-clustering
1045	  statement: Cells with similar tuning to eye position or velocity do not tend to encode similar
1046	    additional variables.
1047	  source: Results, Entorhinal neurons encode eye movements, paragraph 5; Figure 7e, f;
1048	    Supplementary Figure 11d to f
1049	  quote: As with cells encoding head movements, cells that exhibited similar tuning to eye position
1050	    or velocity did not tend to encode similar additional variables
1051	  depends_on:
1052	  - fig4j-eye-encoding-cells
1053	  criterion: A claim of absence, judged as fig3e-head-no-clustering on the head-fixed variables,
1054	    at the Bonferroni level 0.05/10 the Methods give. Reproduced when no combination and k gives
1055	    P < 0.005.
1056	- id: fig8c-eye-tuning-without-landmarks
1057	  statement: Without visual landmarks, body position tuning degrades or remaps (median
1058	    correlation across tracks 0.02), while tuning to body speed and to all eye movement variables
1059	    is preserved significantly more (medians 0.40 to 0.82).
1060	  source: Results, Encoding of eye position and eye velocity persists in the absence of visual
1061	    landmark features, paragraph 1; Figure 8c, d
[... 331 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 100,260p docs/protocol.md; ls paper; tail -5 claims/mallory-2021.yaml; python tools/claims_check.py claims/mallory-2021.yaml paper/10.1038-s41467-021-20936-8.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  wc -c paper/*.txt; grep -n "" paper/10.1038-s41467-021-20936-8.txt | head -120
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker reports two values not found (2.0e-7 and 8.0e-4). Now reading the paper itself.

**Agent calls Bash**

```bash
cd  awk '{print NR": "length($0)}' paper/10.1038-s41467-021-20936-8.txt | sort -t: -k2 -n -r | head; wc -l paper/10.1038-s41467-021-20936-8.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-021-20936-8.txt",
 "offset": 7,
 "limit": 130
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-021-20936-8.txt",
 "offset": 137,
 "limit": 300
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-021-20936-8.txt",
 "offset": 437,
 "limit": 330
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-021-20936-8.txt",
 "offset": 767,
 "limit": 160
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "Supplementary\|SUPPLEMENTARY\|Peer Review\|Reporting" paper/10.1038-s41467-021-20936-8.txt | awk -F: '$1>900' | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=paper/10.1038-s41467-021-20936-8.txt; for s in 1176 1415 1549 2040 2648 4487 5049 5500 5702 6083 6515 7015; do echo "=== $s"; sed -n "${s},$((s+40))p" $f | tr '\n' ' ' | cut -c1-6000; echo; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "8 bins for pitch\|head velocities; VR\|twice the reported\|10 of 179\|asymmetric cells (10 + 28)\|Similar proportions of asymmetric\|a test chosen here\|Measured by correlation\|statement: Head-fixed mice in VR\|at least five of six\|nonlinear asymmetric cells exceed\|0.96$\|stated direction\|for every variable the falsely" claims/mallory-2021.yaml
```

```
62:# head direction bins, speed bins 5 cm/s wide, 8 bins for pitch, roll and the three head
213:    10 of 179 (twice the reported count), with the exact counts reported.
446:  statement: Similar proportions of asymmetric azimuthal head velocity cells prefer ipsiversive
450:  quote: Similar proportions of asymmetric cells preferred ipsiversive ... versus contraversive head
589:  statement: Head-fixed mice in VR move their eyes considerably; the inner 98% of horizontal eye
620:    mice, with the legend's sem across mice as tolerance. Reproduced when at least five of six
661:    value: 0.96
941:    eye velocity both linear and nonlinear asymmetric cells exceed symmetric cells, for vertical
942:    eye velocity nonlinear asymmetric cells exceed symmetric cells.
971:    value: 0.96
984:    stated direction; partially reproduced when the horizontal or the vertical part holds alone.
1113:    tuning curves by a two-sided Wilcoxon signed-rank test, a test chosen here (the paper names
1251:  statement: Measured by correlation coefficients, contributions follow the same order; in freely
```

**Agent**

Opening comment: pitch and roll velocity bins.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "# head direction bins, speed bins 5 cm/s wide, 8 bins for pitch, roll and the three head\n# velocities; VR 20 position bins, speed bins 5 cm/s, 5 bins for each eye variable. Tension",
 "new_string": "# head direction bins, speed bins 5 cm/s wide, 8 bins for pitch, roll and azimuthal head\n# velocity; the Methods give no bin count for pitch and roll velocity, and 8, as for the other\n# head variables, is a standard choice; VR 20 position bins, speed bins 5 cm/s, 5 bins for\n# each eye variable. Tension"
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "is below one cell, so the claim is judged on \"few\", reproduced when each count is at most\n    10 of 179 (twice the reported count), with the exact counts reported.",
 "new_string": "is below one cell, so the claim is judged on \"few\", reproduced when each count is at most\n    twice its reported count (8 of 179 for pitch velocity, 10 of 179 for roll velocity), with\n    the exact counts reported."
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/mallory-2021.yaml",
 "offset": 284,
 "limit": 10
}
```

```
284	    tolerance: 1.0
285	  - quantity: quadratic roll cells
286	    value: 28
287	    tolerance: 2.8
288	  criterion: Classification as in the opening comment (Methods, Quantifying tuning curve
289	    shape), on the cells of fig1c-pitch-roll-cells, with open detail (4) run under both
290	    readings. Reproduced when, under one reading, linear plus quadratic is the majority of
291	    pitch cells, quadratic is the largest class of roll cells, and at least four of the six
292	    counts are within tolerance; partially reproduced when the two majority statements hold
293	    alone.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "    pitch cells, quadratic is the largest class of roll cells, and at least four",
 "new_string": "    pitch cells, quadratic cells are more than half of roll cells, and at least four"
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/mallory-2021.yaml",
 "offset": 440,
 "limit": 25
}
```

```
440	    tolerance: 2.6
441	  - quantity: symmetric cells increasing with speed
442	    value: 20
443	    tolerance: 2.0
444	  criterion: Classes under open detail (6), run under both readings. Reproduced when, under one
445	    reading, the asymmetric and symmetric counts are within tolerance and the binomial test of
446	    positive against negative symmetric cells gives P < 0.05 with more positive cells;
447	    partially reproduced when the binomial result holds alone.
448	- id: fig2c-asymmetric-direction-similar
449	  statement: Similar proportions of asymmetric azimuthal head velocity cells prefer ipsiversive
450	    and contraversive head rotation (23 of 38 contraversive).
451	  source: Results, Entorhinal neurons encode head movements in three dimensions, paragraph 3;
452	    Figure 2c iii
453	  quote: Similar proportions of asymmetric cells preferred ipsiversive ... versus contraversive head
454	    movements (contraversive-preferring n = 23/38, Z = 1.16, P = 0.26)
455	  statistics:
456	  - test: binomial test
457	    statistic: Z = 1.16
458	    p: 0.26
459	    n: 38 asymmetric cells
[... 5 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "    positive against negative symmetric cells gives P < 0.05 with more positive cells;\n    partially reproduced when the binomial result holds alone.",
 "new_string": "    positive against negative symmetric cells gives P < 0.05 with more positive cells;\n    partially reproduced when the binomial result holds alone. The paper names no test for this\n    Z and P; it is read as the binomial test against one half that the same paragraph uses for\n    pitch and roll preference."
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "    (5). Reproduced when the binomial test against one half gives P >= 0.05.",
 "new_string": "    (5). Reproduced when the binomial test against one half gives P >= 0.05. The paper names\n    no test for this Z and P; it is read as the binomial test of the paragraph's other\n    preference results."
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/mallory-2021.yaml",
 "offset": 594,
 "limit": 35
}
```

```
594	    standard choice. Reproduced when no combination and k gives P < 0.005.
595	- id: fig4f-eye-movement-distributions
596	  statement: Head-fixed mice in VR move their eyes considerably; the inner 98% of horizontal eye
597	    position spans about -3.5 to 5.3% of eye width and of vertical position -2.7 to 1.6%.
598	  source: Results, Entorhinal neurons encode eye movements, paragraph 2; Figure 4c to i legend
599	  quote: On the virtual track with landmarks, head-fixed mice moved their eyes considerably, as
600	    reported previously
601	  expected:
602	  - quantity: horizontal eye position 1st percentile
603	    value: -3.50
604	    tolerance: 0.61
605	    unit: percent of eye width
606	  - quantity: horizontal eye position 99th percentile
607	    value: 5.28
608	    tolerance: 0.87
609	    unit: percent of eye width
610	  - quantity: vertical eye position 1st percentile
611	    value: -2.74
612	    tolerance: 0.64
613	    unit: percent of eye width
[... 15 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "    position spans about -3.5 to 5.3% of eye width and of vertical position -2.7 to 1.6%.\n  source: Results, Entorhinal neurons encode eye movements, paragraph 2; Figure 4c to i legend",
 "new_string": "    position spans about -3.5 to 5.3% of eye width and of vertical position -2.7 to 1.6%; that\n    of horizontal eye velocity -6.2 to 6.9% of eye width per s and of vertical eye velocity -2.8\n    to 3.2% per s.\n  source: Results, Entorhinal neurons encode eye movements, paragraph 2; Figure 4c to i legend"
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "    value: 6.87\n    tolerance: 0.66\n    unit: percent of eye width per s\n  criterion: Percentiles per session, about the mean position, averaged per mouse, mean over 8\n    mice, with the legend's sem across mice as tolerance. Reproduced when at least five of six\n    are within tolerance; partially for three or four.",
 "new_string": "    value: 6.87\n    tolerance: 0.66\n    unit: percent of eye width per s\n  - quantity: vertical eye velocity 1st percentile\n    value: -2.83\n    tolerance: 0.55\n    unit: percent of eye width per s\n  - quantity: vertical eye velocity 99th percentile\n    value: 3.15\n    tolerance: 0.68\n    unit: percent of eye width per s\n  criterion: Percentiles per session, about the mean position, averaged per mouse, mean over 8\n    mice, with the legend's sem across mice as tolerance. Reproduced when at least seven of\n    eight are within tolerance; partially for four to six."
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/mallory-2021.yaml",
 "offset": 985,
 "limit": 15
}
```

```
985	  - fig6-eye-velocity-nonlinear-temporal
986	  expected:
987	  - quantity: median stability, Eh dot linear-asymmetric
988	    value: 0.96
989	    tolerance: 0.096
990	  - quantity: median stability, Eh dot nonlinear-symmetric
991	    value: 0.86
992	    tolerance: 0.086
993	  - quantity: median stability, Ev dot nonlinear-asymmetric
994	    value: 0.85
995	    tolerance: 0.085
996	  - quantity: median stability, Ev dot nonlinear-symmetric
997	    value: 0.38
998	    tolerance: 0.038
999	  criterion: Reproduced when, under one reading of open detail (6), both Kruskal-Wallis tests
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "  - quantity: median stability, Eh dot linear-asymmetric\n    value: 0.96\n    tolerance: 0.096\n  - quantity: median stability, Eh dot nonlinear-symmetric",
 "new_string": "  - quantity: median stability, Eh dot linear-asymmetric\n    value: 0.96\n    tolerance: 0.096\n  - quantity: median stability, Eh dot nonlinear-asymmetric\n    value: 0.94\n    tolerance: 0.094\n  - quantity: median stability, Eh dot nonlinear-symmetric"
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/mallory-2021.yaml",
 "offset": 1000,
 "limit": 8
}
```

```
1000	    value: 0.38
1001	    tolerance: 0.038
1002	  criterion: Reproduced when, under one reading of open detail (6), both Kruskal-Wallis tests
1003	    give P < 0.05 and the three named pairwise comparisons are significant at alpha 0.0167 in the
1004	    stated direction; partially reproduced when the horizontal or the vertical part holds alone.
1005	- id: fig7ab-eye-contributions
1006	  statement: Body position and speed influence MEC spiking more than eye movement signals, and eye
1007	    position contributes more than eye velocity.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "    stated direction; partially reproduced when the horizontal or the vertical part holds alone.\n- id: fig7ab-eye-contributions",
 "new_string": "    stated direction; partially reproduced when the horizontal or the vertical part holds alone.\n    The medians are compared with their tolerances and reported either way.\n- id: fig7ab-eye-contributions"
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/mallory-2021.yaml",
 "offset": 1128,
 "limit": 12
}
```

```
1128	  quote: This effect was observed even in cells that jointly encoded body position and eye position
1129	    (Fig. 8e ).
1130	  depends_on:
1131	  - fig8c-eye-tuning-without-landmarks
1132	  criterion: The paper shows examples and no test. For cells encoding both B and Eh on the landmark
1133	    track, the cross-track correlation of Eh tuning curves is compared with that of their B
1134	    tuning curves by a two-sided Wilcoxon signed-rank test, a test chosen here (the paper names
1135	    none, and this is an assumption). Reproduced when the median Eh correlation exceeds the
1136	    median B correlation with P < 0.05 under one reading of open detail (7).
1137	- id: methods-hemispheres-similar
1138	  statement: The proportion of MEC neurons tuned to eye movement variables does not differ between
1139	    left (mean 0.23) and right (0.43) hemisphere recordings.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "    track, the cross-track correlation of Eh tuning curves is compared with that of their B\n    tuning curves by a two-sided Wilcoxon signed-rank test, a test chosen here (the paper names\n    none, and this is an assumption). Reproduced when the median Eh correlation exceeds the\n    median B correlation with P < 0.05 under one reading of open detail (7).",
 "new_string": "    track, the cross-track correlation of Eh tuning curves is compared with that of their B\n    tuning curves by the test the Figure 8c legend uses for the same comparison over all cells,\n    a two-sided Wilcoxon rank-sum test at alpha 0.0033. Applying it to this subset is a reading\n    (the paper gives no test for Fig. 8e) and an outcome on it rests on that assumption; a\n    paired two-sided Wilcoxon signed-rank test is a variant. Reproduced when the median Eh\n    correlation exceeds the median B correlation with P < 0.0033 under one reading of open\n    detail (7)."
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/mallory-2021.yaml",
 "offset": 1162,
 "limit": 25
}
```

```
1162	- id: supp3-low-false-positives
1163	  statement: Shuffling one variable in time and refitting yields few falsely detected cells for
1164	    each variable, in both datasets (for example 0 of 46 for pitch, 1 of 12 for azimuthal head
1165	    velocity, 5 of 343 for horizontal eye position, 13 of 135 for vertical eye velocity).
1166	  source: Supplementary Figure 3b, c
1167	  quote: Here, we observed a very low chance of false positives for each variable
1168	  depends_on:
1169	  - fig1c-head-direction-cells
1170	  - fig4j-eye-encoding-cells
1171	  expected:
1172	  - quantity: falsely detected vertical eye velocity cells, head-fixed
1173	    value: 13
1174	    tolerance: 1.3
1175	  - quantity: falsely detected horizontal eye velocity cells, head-fixed
1176	    value: 8
1177	    tolerance: 0.8
1178	  criterion: As in the Methods (Identifying rate of falsely detected encoded variables), one
1179	    variable at a time is shuffled across time bins in Cohort 1 and in the head-fixed data and the
1180	    whole LN pipeline is rerun. One shuffle per variable, as the counts imply. Reproduced when for
1181	    every variable the falsely detected count is at most 10% of the normally detected count
[... 5 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "    whole LN pipeline is rerun. One shuffle per variable, as the counts imply. Reproduced when for\n    every variable the falsely detected count",
 "new_string": "    whole LN pipeline is rerun. One shuffle per variable, as the counts imply. The variables are\n    the six the legend reports for each dataset (Cohort 1 B, Bs, Ha, Hp, Hr and azimuthal head\n    velocity; head-fixed B, Bs, Eh, Ev, Eh dot and Ev dot); pitch and roll velocity are not\n    among them. Reproduced when for each of these variables the falsely detected count"
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/mallory-2021.yaml",
 "offset": 1272,
 "limit": 10
}
```

```
1272	    tolerance: 8.2
1273	  criterion: As fig2c-velocity-extrema-near-zero, the half range being halfway between 0 and the
1274	    maximum or minimum velocity of the range. Reproduced when both binomial tests give P < 0.05
1275	    with a majority within half range and both counts are within tolerance.
1276	- id: supp9-correlation-contributions
1277	  statement: Measured by correlation coefficients, contributions follow the same order; in freely
1278	    moving mice body position contributes most (median 0.42) and azimuthal head velocity least
1279	    (0.02), and in head-fixed mice body position and speed exceed the eye variables.
1280	  source: Supplementary Figure 9
1281	  quote: We report the contribution of each variable to the correlation coefficient between a
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "  statement: Measured by correlation coefficients, contributions follow the same order; in freely\n    moving mice body position contributes most (median 0.42) and azimuthal head velocity least\n    (0.02), and in head-fixed mice body position and speed exceed the eye variables.",
 "new_string": "  statement: Measured by correlation coefficients, body position contributes most in freely\n    moving mice (median 0.42) and azimuthal head velocity least (0.02), and in head-fixed mice\n    body position and speed exceed the eye variables."
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Grep**

```json
{
 "pattern": "p: 8.0e-4",
 "path": "claims/mallory-2021.yaml",
 "output_mode": "content",
 "-A": 3
}
```

```
1263:    p: 8.0e-4
1264-  depends_on:
1265-  - fig6-eye-velocity-nonlinear-temporal
1266-  expected:
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "    p: 8.0e-4\n  depends_on:\n  - fig6-eye-velocity-nonlinear-temporal",
 "new_string": "    p: 8.0e-4\n  - about: entropy of peak or valley locations against a uniform distribution, each variable\n    p: 1.0e-4\n  depends_on:\n  - fig6-eye-velocity-nonlinear-temporal"
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  tail -3 claims/mallory-2021.yaml; grep -n "^checks" claims/mallory-2021.yaml; grep -rn "kind: agent" claims/*.yaml | head -3
```

```
sessions and, for each eye variable, the cells detected in the simulated data are at most 10%
    of those in the original (a reading of "not falsely detected"; the Supplementary Fig. 3c
    false positive rates reach this level).
claims/alasfour-2024.yaml:647:  kind: agent
claims/armstrong-2026.yaml:845:  kind: agent
claims/ashworth-2025.yaml:1207:  kind: agent
```

**Agent calls Bash**

```bash
cd  sed -n 640,670p claims/alasfour-2024.yaml
```

```
criterion: Per participant, the band whose Figure 7 curve reaches the highest test accuracy
    (M10, O15), with O5, O7, O8; participant numbers under O1 (a), the only reading in which a
    Participant 3 exists (Participant 5 is Table 1's 8, Participant 3 is Table 1's 4). Reproduced
    when, under one reading, Participant 5's best band is theta and Participant 3's is alpha;
    partially reproduced when one holds.
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2-rois-three-bands, fig2-inferior-temporal-all-bands, fig2-beta-temporal-only, fig2-single-band-rois. Removed the statistics entries (t-test against finite chance, BH FDR at 0.01); the threshold marks which features count as above chance (Figure 2 legend), a method and not a result. The criteria keep it through M6.
  - fig5-gamma-higher-talking, fig5-theta-alpha-lower-talking, fig5-pre-postcentral. Removed the statistics entries (t-test of the mean difference against zero, BH FDR at 0.01); the threshold selects the consistent features whose signs are counted (Figure 5 legend), a method and not a result. The criteria keep it through M8.
  - table1-participants. Removed the rule that 13 of the 15 minute values suffice; the paper gives no such threshold, so every value must now be within tolerance.
  - fig6-sign-consistency. The tolerance of 0.9 allowed only 9 while the criterion accepted 8 to 10. Set the tolerance to 1 (10% of 9 rounded to a whole combination) and gave the reason.
  - Header O4. The SD of the channel was fixed as the whole recording, called a standard choice; it can change which blocks are dropped, so the readings (whole recording, the day's recording) are now named.
  - Header O10, anova-roi-band-effects, anova-no-interaction. The ANOVA's observations are not given (Methods 2.2); named fold accuracies and participant means as readings. The absence claim is judged on fold accuracies with type II sums of squares, marked as resting on an assumpt
[... 6 more lines not kept]
```

**Agent**

Edits done. Adding the `checks` entry and re-running the checker.

**Agent calls Bash**

```bash
cd  cat >> claims/mallory-2021.yaml <<'EOF'
checks:
- date: 2026-11-10
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header, LN pipeline. Said 8 bins for pitch, roll and the three head velocities; the Methods give 8 bins for pitch, roll and azimuthal head velocity only. The pitch and roll velocity bin count is now named as not given, with 8 as a standard choice.
  - fig1c-pitch-roll-velocity-rare. The criterion allowed 10 of 179 for each count, called twice the reported count; twice 4 is 8. The limits are now 8 for pitch velocity and 10 for roll velocity.
  - fig2-pitch-roll-shapes. The criterion asked only that quadratic be the largest roll class; the paper says the majority of roll cells are quadratic (28 of 53). It now asks for more than half.
  - fig2c-symmetric-asymmetric-classes, fig2c-asymmetric-direction-similar. The paper names no test for these Z and P values; the criteria now say the binomial test is read from the paragraph's other preference tests.
  - fig4f-eye-movement-distributions. The vertical eye velocity 1st and 99th percentiles (-2.83 +- 0.55, 3.15 +- 0.68, Figure 4i legend) were left out without reason. Added them and the velocity ranges to the statement; the rule is now seven of eight (partially four to six), as in fig1b.
  - fig6v-asymmetric-more-stable. Added the Eh dot nonlinear-asymmetric median (0.94, Figure 6a v legend), part of the statement, and said the medians are reported against their tolerances, since the criterion did not use them.
  - fig8e-joint-cells-preserve-eye-tuning. The criterion used a signed-rank test chosen by the writer. It now uses the paper's own test for this comparison (Figure 8c legend, two-sided rank-sum at alpha 0.0033) on the joint cells, marked as a reading and an assumption, with the signed-rank test as a variant.
  - supp3-low-false-positives. "Every variable" was unclear; the legend reports six variables per dataset and not pitch or roll velocity. The criterion now lists them.
  - supp7e-eye-velocity-extrema-near-zero. Added the legend's entropy test (both P = 1.0e-4), as fig2c-velocity-extrema-near-zero records its entropy test.
  - supp9-correlation-contributions. The statement said contributions "follow the same order"; the paper does not say so, and the orders differ (Bs and pitch rank below roll by correlation). Removed it.
  - Checker. Flagged P = 2.0e-7 (fig2c-velocity-extrema-near-zero) and 8.0e-4 (supp7e-eye-velocity-extrema-near-zero) as not found; both are printed in the Supplementary Figure 7d and 7e legend. No change.
  - Open. Fold construction, range restriction, the normalization of the contribution, "explored", preference, the symmetric rule, the Fig. 8 tuning curves and pooled P values (header details 1 to 8) stay open with their readings; the paper and the linked code do not settle them.
  - Open. The Methods give eye units as fraction of eye width while the Results and Figure 4 legend use 1/100 of the eye width; the header's choice of percent for the preset bounds is a reading.
  - Open. Whether the 6 sessions of Figure 8 are among the 11 landmark sessions is not stated.
  - Open. Several criteria use thresholds of this file where the paper gives words only ("few" in fig1c-pitch-roll-velocity-rare, "nearly all" as 90% in supp4-ln-conservative, "not falsely detected" as at most 10% in supp12-no-false-eye-detection); each says so.
EOF
python tools/claims_check.py claims/mallory-2021.yaml paper/10.1038-s41467-021-20936-8.txt; grep -n "—\|rather" claims/mallory-2021.yaml | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/mallory-2021.yaml",
 "old_string": "The statement said contributions \"follow the same order\"; the paper does not say so, and the orders differ (Bs and pitch rank below roll by correlation). Removed it.",
 "new_string": "The statement said contributions \"follow the same order\"; the paper does not say so (the medians happen to rank alike, with Bs and pitch tied at 0.07), and the criterion does not test it. Removed it."
}
```

```
The file claims/mallory-2021.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/mallory-2021.yaml paper/10.1038-s41467-021-20936-8.txt | tail -1; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

The file is ready for an attempt (`ready: true`). I made ten corrections, each backed by the paper, and nothing is committed.

**Checker result:** `claims/mallory-2021.yaml: 42 claims, 42 quotes, 54 statistical values, 2 problems`. The two problems are p-values it could not find: P = 2.0e-7 in fig2c-velocity-extrema-near-zero and P = 8.0e-4 in supp7e-eye-velocity-extrema-near-zero. Both are printed in the Supplementary Fig. 7d/e legend, so I left them unchanged. All quotes passed.

**Changes, by claim:**
- **Opening comment:** it said 8 bins for pitch, roll and all three head velocities. The Methods give 8 bins only for pitch, roll and azimuthal head velocity. The bin count for pitch and roll velocity is now marked as not given, with 8 as a standard choice.
- **fig1c-pitch-roll-velocity-rare:** the limit was 10 of 179 for both counts, described as twice the reported count. Twice 4 is 8, so the limits are now 8 (pitch velocity) and 10 (roll velocity).
- **fig2-pitch-roll-shapes:** for roll, the criterion only asked that quadratic be the largest class. The paper says the majority of roll cells are quadratic (28 of 53), so it now asks for more than half.
- **fig2c-symmetric-asymmetric-classes, fig2c-asymmetric-direction-similar:** the paper names no test for these Z and P values. The criteria now say the binomial test is inferred from the other preference tests in the same paragraph.
- **fig4f-eye-movement-distributions:** the vertical eye velocity percentiles (−2.83 ± 0.55 and 3.15 ± 0.68, Fig. 4i legend) had been left out without a reason. I added them, put the velocity ranges in the statement, and changed the rule to seven of eight values (partial for four to six).
- **fig6v-asymmetric-more-stable:** added the horizontal eye velocity nonlinear-asymmetric median (0.94), which the statement covers. The criterion now says the medians are reported against their tolerances.
- **fig8e-joint-cells-preserve-eye-tuning:** the criterion used a signed-rank test the previous writer chose. It now uses the paper's own Fig. 8c test (two-sided rank-sum at α 0.0033) on the cells that encode both position and eye position. That is marked as a reading and an assumption, with signed-rank as a variant.
- **supp3-low-false-positives:** the criterion said "every variable". It now lists the six variables per dataset that the legend reports, which do not include pitch or roll velocity.
- **supp7e-eye-velocity-extrema-near-zero:** added the legend's entropy test (P = 1.0e-4), as the matching head velocity claim already records its entropy test.
- **supp9-correlation-contributions:** removed "follow the same order" from the statement. The paper does not say it and the criterion does not test it.

**Still open** (recorded under `checks`):
- The eight details the opening comment already lists remain unsettled by the paper or its code. They include how folds are built, how the range restriction works, how the contribution is normalised, what "explored" means, cell preference, the symmetric-cell rule, the Fig. 8 tuning curves and pooled P values.
- Eye units: the Methods say "fraction of eye width", while the Results and Fig. 4 legend use 1/100 of eye width. Reading the preset bounds as percent is an interpretation.
- The paper does not say whether the 6 Fig. 8 sessions are among the 11 landmark sessions.
- Three criteria turn words into thresholds of their own: "few", "nearly all" (as 90%) and "not falsely detected" (as at most 10%). Each criterion says so.

The paper's main findings each have a claim, and every claim comes from this paper.

## End of run

41 turns, 4 minutes, $2.12 at API prices, result: success.
