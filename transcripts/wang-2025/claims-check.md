# wang-2025 · claims-check · run 44783984367

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i wang; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80; cat claims/wang-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; grep -n "^## Reader" -A60 docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 103,200p docs/protocol.md
```

```
better fit, p < 0.05") is a method, not a result, and is left out.
     Leave the field out when the paper reports no test or interval for the
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
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/wang-2025.yaml paper/10.1038-s41593-025-02114-x.txt; wc -l claims/wang-2025.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/wang-2025.yaml"
}
```

```
1	# Claims for Wang, Kurgyis, Chen, Kang, Chen, Liu, Liu, Svoboda, Li & Druckmann (2025), "Brain-wide
2	# analysis reveals movement encoding structured across and within brain areas", Nature Neuroscience,
3	# doi:10.1038/s41593-025-02114-x, on dandiset 000363 (Mesoscale Activity Map Dataset), which the
4	# paper reuses.
5	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-20,
6	# protocol as stated in docs/protocol.md (pilot-18).
7	#
8	# Text read. The version of record (published 18 November 2025, open access), full text from the
9	# publisher's page: main text, figure legends, Methods, Extended Data Figs. 1 to 10 legends. The
10	# Supplementary Information PDF (41593_2025_2114_MOESM1_ESM.pdf; Supplementary Discussion on the
11	# session-independent autoencoder, Supplementary Table 1 on thalamic nuclei, Supplementary Figs. 1
12	# and 2) was read from its extracted text in the same file. The Reporting Summary and the three
13	# Supplementary Videos were not read; no claim rests on them. Figures were not opened; every
14	# number used below is printed in the text or a legend.
15	#
16	# Code read. github.com/druckmann-lab/MapVideoAnalysis at commit 7d27624 (7d276243db16db5af6da68a48de7720ef77007c2),
17	# the repository the paper links (Zenodo doi:10.5281/zenodo.16740762). It holds the package
18	# VideoAnalysisUtils (ridge prediction and explained variance, functions_for_r2.py; single-neuron
19	# choice and movement AUCs, functions_for_auc.py; area selection, nearest-neighbour and spatial
20	# uniformity tests, functions.py; figure classes and their statistics, plotting_utils.py, where
[... 1034 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-025-02114-x.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker run: 29 claims, 1 problem (edfig6 striatum p 3e-07 not found). Reading the rest of the paper text now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-025-02114-x.txt",
 "offset": 204,
 "limit": 90
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41593-025-02114-x.txt",
 "offset": 204,
 "limit": 50
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk 'NR>=204{print NR": "length($0)}' paper/*.txt | sort -t: -k2 -n -r | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/w; sed -n 242p paper/*.txt | fold -s -w 4000 > $TMPDIR/w/main.txt; wc -l $TMPDIR/w/main.txt; sed -n '204,241p;243,376p' paper/*.txt | cut -c1-300
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,8p $TMPDIR/w/main.txt
```

```
<persisted-output>
Output too large (31.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d9543e3c-6eca-46c0-9b64-bf6f79184f15/tool-results/bpa47z3il.txt

Preview (first 2KB):
Download PDF Subjects Computational neuroscience Motor control Abstract Movement-related activity has been detected across much of the brain, including sensory and motor regions. However, much remains unknown regarding the distribution of movement-related activity across brain regions, and how this activity relates to neural computation. Here we analyzed movement-related activity in brain-wide recordings of more than 50,000 neurons in mice performing a decision-making task. We used multiple machine learning methods to predict neural activity from videography and found that movement-related signals differed across areas, with stronger movement signals close to the motor periphery and in motor-associated subregions. Delineating activity that predicts or follows movement revealed fine-scale structure of sensory and motor encoding across and within brain areas. Through single-trial video-based predictions of behavior, we identified activity modulation by uninstructed movements and their impact on choice-related activity analysis. Our work provides a map of movement encoding across the brain and approaches for linking neural activity, uninstructed movements and decision-making. Similar content being viewed by others A brain-wide map of neural activity during complex behaviour Article Open access 03 September 2025 How distributed is the brain-wide network that is recruited for cognition? Article 04 December 2025 Sensory expectations shape neural population dynamics in motor circuits Article 29 October 2025 Main A standard view of the function of the nervous system is the translation of sensory inputs into action 1 , 2 , 3 . According to this view, the brain is parcellated into sensory and motor areas, with association areas in between 4 . On the other hand, de
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/d9543e3c-6eca-46c0-9b64-bf6f79184f15/tool-results/bpa47z3il.txt"
}
```

```
1	Download PDF Subjects Computational neuroscience Motor control Abstract Movement-related activity has been detected across much of the brain, including sensory and motor regions. However, much remains unknown regarding the distribution of movement-related activity across brain regions, and how this activity relates to neural computation. Here we analyzed movement-related activity in brain-wide recordings of more than 50,000 neurons in mice performing a decision-making task. We used multiple machine learning methods to predict neural activity from videography and found that movement-related signals differed across areas, with stronger movement signals close to the motor periphery and in motor-associated subregions. Delineating activity that predicts or follows movement revealed fine-scale structure of sensory and motor encoding across and within brain areas. Through single-trial video-based predictions of behavior, we identified activity modulation by uninstructed movements and their impact on choice-related activity analysis. Our work provides a map of movement encoding across the brain and approaches for linking neural activity, uninstructed movements and decision-making. Similar content being viewed by others A brain-wide map of neural activity during complex behaviour Article Open access 03 September 2025 How distributed is the brain-wide network that is recruited for cognition? Article 04 December 2025 Sensory expectations shape neural population dynamics in motor circuits Article 29 October 2025 Main A standard view of the function of the nervous system is the translation of sensory inputs into action 1 , 2 , 3 . According to this view, the brain is parcellated into sensory and motor areas, with association areas in between 4 . On the other hand, decades of neurophysiological recordings have found activity related to movement throughout sensory and motor regions of the brain. For example, neurons in visual cortical areas are modulated by eye movement in prima
[... 8 more lines not kept]
```

**Agent**

Main text so far matches the claims closely. Reading the remaining main text, legends and Methods.

**Agent calls Bash**

```bash
cd  sed -n 9,15p $TMPDIR/w/main.txt
```

```
action encoding, in which the task instruction and action are dissociated 3 , 34 , we used trials where the behavioral choice and the choice predicted from the uninstructed movements during the delay epoch were in disagreement to dissociate choice and movement encoding (see Extended Data Fig. 8 for schematic). We analyzed correct trials only and separately divided lick-left (L) and lick-right (R) trials into two groups based on the prediction of the video-based classifier (predicted lick-left (vL) and predicted lick-right (vR) for each trial type; Fig. 7a ), thus obtaining four trial contingencies (L-vL, L-vR, R-vR, R-vL; Methods ). When considering single-neuron tuning properties, in trials where choice and video prediction match (L-vL and R-vR), choice tuning and movement tuning are confounded. In contrast, trials with mismatches between choice and video prediction enable us to potentially distinguish between tuning to choice versus movements (L-vR and R-vL). Fig. 7: Single-trial analysis of movement and spike rate reveals neurons modulated by choice and movement. a , Schematic of analysis. Correct trials were split into lick-left and lick-right trials. Each of these sets of trials corresponding to a choice was further broken into two groups based on the prediction of behavior from video, yielding four groups of trials corresponding to the choice contingency and value of single-trial video prediction ( Methods ). b , Analysis schematic as applied to two example neurons (center, right) and jaw marker (left) within a single session. Left: jaw marker position (height) during entire trial (top) and magnified on the delay epoch (middle). Lines correspond to the mean of jaw height across the four trial groups. Color indicates trial type and line style (solid or dashed) corresponds to the video-prediction-based contingency. Shaded area corresponds to the s.e.m. across trials. Center: same data as in top, magnified on the delay epoch. Bottom: mean jaw height during the de
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 16,23p $TMPDIR/w/main.txt
```

```
the jaw and the nose markers were used as features, and mouse identity was used as cluster labels. We note that we used only sessions where the trial type was predictable from either jaw or nose (AUC equal to or higher than 0.65) and only mice that had two or more of such predictable sessions. Testing against spatial discontinuity with nearest-neighbor explained variance difference distribution To test whether spatially closer neurons have smaller difference in their explained variance than expected by chance within thalamus (Fig. 3e ), we first identified neurons within each nucleus and calculated the cumulative distribution function for the explained variance difference between nearest neighbors. As a control we randomly shuffled the neurons’ explained variance values within each nucleus separately and calculated the cumulative distribution function for the explained variance difference in the shuffled sample. We repeated the shuffle 1,000 times to establish a null-distribution and bootstrap P value. Test against spatial uniformity To test against spatial uniformity (Figs. 3 and 7 and Extended Data Fig. 9 ) of a given scalar statistic (explained variance, single-neuron AUC) given the fixed sampling provided by the CCF coordinates, we split the brain into cubic voxels (0.2 mm cubed for Fig. 3 and 0.5 mm cubed for Fig. 7 and Extended Data Fig. 9 , but the results do not depend on the specific choice of this size) and grouped neurons based on these voxels. We then calculated an F -statistic for this grouping using one-way F -test. As a control we randomly shuffled the scalar statistics of interest (explained variance, single-neuron AUC) across neurons while keeping the CCF coordinates fixed; we used the same cubic voxels as before to group the shuffled neurons and calculated an F -statistic for this shuffle control using one-way F -test. We repeated the shuffle 10,000 times to establish a null-distribution and bootstrap P value. Data pooling The registration of indiv
[... 7 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wang-2025.yaml",
 "old_string": "  - about: medulla against each of midbrain, ALM, striatum and thalamus\n    test: two-tailed Mann-Whitney U test\n    p: 1.04e-11\n    corrected: Bonferroni\n    n: 36, 79, 77, 67 and 62 insertions\n  - about: thalamus against midbrain, ALM and striatum (largest of the three p)\n    test: two-tailed Mann-Whitney U test\n    p: 8.26e-09\n    corrected: Bonferroni",
 "new_string": "  - about: medulla against midbrain\n    test: two-tailed Mann-Whitney U test\n    p: 1.04e-11\n    corrected: Bonferroni\n    n: 36 medulla and 79 midbrain insertions\n  - about: medulla against ALM\n    test: two-tailed Mann-Whitney U test\n    p: 1.24e-13\n    corrected: Bonferroni\n  - about: medulla against striatum\n    test: two-tailed Mann-Whitney U test\n    p: 1.03e-13\n    corrected: Bonferroni\n  - about: medulla against thalamus\n    test: two-tailed Mann-Whitney U test\n    p: 3.31e-15\n    corrected: Bonferroni\n  - about: midbrain against thalamus\n    test: two-tailed Mann-Whitney U test\n    p: 2.47e-11\n    corrected: Bonferroni\n  - about: ALM against thalamus\n    test: two-tailed Mann-Whitney U test\n    p: 2.80e-08\n    corrected: Bonferroni\n  - about: striatum against thalamus\n    test: two-tailed Mann-Whitney U test\n    p: 8.26e-09\n    corrected: Bonferroni"
}
```

```
The file claims/wang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wang-2025.yaml",
 "old_string": "  criterion: Tolerances are the s.e.m. given. Response epoch, single 64-trial test split. Per the\n    code (Figure2.get_method_comparison_stats), neurons with trial-average rate above 2 Hz and\n    explained variance above 0.005 under all three methods; per neuron, improvement = (EV_better -\n    EV_worse) / EV_worse; per session, the mean over its neurons; the mean and s.e.m. over sessions;\n    a Wilcoxon signed-rank test of the session means against zero, one-sided p (two-sided p halved)\n    times 3. The Methods' threshold of 0.01 is the variant. Reproduced when",
 "new_string": "  criterion: Tolerances are the s.e.m. given. Response epoch, single 64-trial test split. Neurons\n    with trial-average rate above 2 Hz and explained variance above 0.01 under all three methods\n    (Methods, Epoch-averaged explained variance; the code, Figure2.get_method_comparison_stats, uses\n    0.005, a variant to be shown); per neuron, improvement = (EV_better - EV_worse) / EV_worse; per\n    session, the mean over its neurons; the mean and s.e.m. over sessions; a Wilcoxon signed-rank\n    test of the session means against zero, one-sided p (two-sided p halved) times 3 (code).\n    Reproduced when"
}
```

```
The file claims/wang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wang-2025.yaml",
 "old_string": "    (threshold set at 100 ... Explained variance based on the embedding method varied significantly\n    among nuclei (Fig. 3c,d,f and see Extended Data Fig. 4 for pairwise statistics).\n  statistics:\n  - test: pairwise two-tailed Mann-Whitney U tests with Bonferroni correction (Extended Data Fig. 4)\n    p: 0.1\n    p_relation: \"<\"\n    corrected: Bonferroni\n  expected:",
 "new_string": "    (threshold set at 100 ... Explained variance based on the embedding method varied significantly\n    among nuclei (Fig. 3c,d,f and see Extended Data Fig. 4 for pairwise statistics).\n  expected:"
}
```

```
The file claims/wang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wang-2025.yaml",
 "old_string": "    variance by two-tailed Mann-Whitney U at Bonferroni-corrected p < 0.05 (21 pairs), with VAL lower\n    than PO, VM and VP as in thalamus-ev-not-rate.",
 "new_string": "    variance by two-tailed Mann-Whitney U at Bonferroni-corrected p < 0.05 (21 pairs; Extended Data\n    Fig. 4 legend). The pairwise p-values are reported."
}
```

```
The file claims/wang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wang-2025.yaml",
 "old_string": "    Figure4.get_barplot_stats). Reproduced when the rate test gives p > 0.1, the explained-variance\n    test gives p < 0.001, and the VAL mean is the lowest of the four. The absence half is judged on\n    the paper's F-test alone.",
 "new_string": "    Figure4.get_barplot_stats). The text does not say whether VAL is above or below the other three;\n    the reading taken from \"differed significantly between VAL and PO/VM/VP\" is that the VAL mean is\n    the highest or the lowest of the four, and its direction is reported. Reproduced when the rate\n    test gives p > 0.1, the explained-variance test gives p < 0.001, and the VAL mean is the highest\n    or the lowest of the four. The absence half is judged on the paper's F-test alone."
}
```

```
The file claims/wang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wang-2025.yaml",
 "old_string": "    over tau at least 1.2 times the mean over tau. Area curves are each neuron's explained variance\n    normalized to its value at zero shift, averaged over neurons. Reproduced",
 "new_string": "    over tau at least 1.2 times the mean over tau. Area curves are each neuron's explained variance\n    normalized to its value at zero shift, averaged over the area's neurons within each session and\n    then over sessions (Fig. 4b legend, \"mean across sessions\"; Methods, Data pooling, uniform\n    weights across sessions); the plain mean over pooled neurons is a variant. Reproduced"
}
```

```
The file claims/wang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wang-2025.yaml",
 "old_string": "  - about: striatum\n    test: Spearman rank correlation\n    statistic: R = 0.15\n    p: 3.0e-07\n    corrected: Bonferroni",
 "new_string": "  - about: striatum\n    test: Spearman rank correlation\n    statistic: R = 0.15\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni"
}
```

```
The file claims/wang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wang-2025.yaml",
 "old_string": "    = 0.22 for medulla), p times 5. The legend prints the striatum p as \"3e7\", read as 3e-7. The\n    claim holds (reproduced) when medulla has corrected p > 0.1 and the other four areas have positive\n    R with corrected p < 0.001; the R values and counts are judged against their tolerances (10%) and\n    reported. A 10% tolerance on an R of 0.06 is narrow; R within 0.03 of the paper's value with the\n    same significance outcome counts as a match, as the paper prints R to two decimals.",
 "new_string": "    = 0.22 for medulla), p times 5. The legend prints the striatum p as \"3e7\", a misprint; the\n    statistics record the main text's P < 0.001 for striatum. Reproduced when medulla has corrected\n    p > 0.1, the other four areas have positive R with corrected p < 0.001 (main text), and the R\n    values and counts are within tolerance; partially reproduced when this pattern of significance\n    holds but some R values or counts fall outside tolerance."
}
```

```
The file claims/wang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wang-2025.yaml",
 "old_string": "  - test: one-sided Mann-Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 870 somatosensory and 1,059 ALM neurons",
 "new_string": "  - test: one-sided Mann-Whitney U test\n    p: 0.0001\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 870 somatosensory and 1,059 ALM neurons"
}
```

```
The file claims/wang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wang-2025.yaml",
 "old_string": "    get_medulla_alm_fraction_stats, which prints medulla 171/142, ALM 710/148, midbrain 678/159).",
 "new_string": "    get_medulla_alm_fraction_stats, which prints medulla 171/142, ALM 710/148, midbrain 678/159).\n    The Methods say \"exceeded 0.65\" and that some neurons pass for both; counting all neurons above\n    0.65 for each AUC (both included) is a variant to be shown."
}
```

```
The file claims/wang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wang-2025.yaml",
 "old_string": "    session-dependent (in the training sessions exp. var. ... difference 12.8% +/- 3.0% sem, n=192\n    recordings, p<0.001)",
 "new_string": "    session-dependent (in the training sessions exp. var. ... difference 3.6% +/- 1.1% sem, n=122\n    recordings, p<0.001. In the hold-out sessions, ... difference 12.8% +/- 3.0% sem, n=192\n    recordings, p<0.001)"
}
```

```
The file claims/wang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/wang-2025.yaml",
 "old_string": "    (movement-) modulated when its choice (movement) AUC is at least 0.65 and the other is below\n    0.65;",
 "new_string": "    (movement-) modulated when its choice (movement) AUC exceeds 0.65 (Methods) and the other does\n    not;"
}
```

```
The file claims/wang-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  grep -l "^checks:" claims/*.yaml | head -3; f=$(grep -l "^checks:" claims/*.yaml | head -1); sed -n '/^checks:/,$p' $f | head -20
```

```
claims/alasfour-2024.yaml
claims/andrews-2024.yaml
claims/armstrong-2026.yaml
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
  - Header O10, anova-roi-band-effects, anova-no-interaction. The ANOVA's observations are not given (Methods 2.2); named fold accuracies and participant means as readings. The absence claim is judged on fold accuracies with type II sums of squares, marked as resting on an assumption, with the others as variants. Said that p < 0.001 for a printed 0 is this file's reading.
  - fig5-pre-postcentral. The criterion cited Discussion paragraph 2 for the alpha sign; that paragraph gives theta and gamma only. The alpha sign is cited to Results 3.1 paragraph 6.
  - fig7-exceeds-group. The comparison of Figure 7 with Figure 2
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat >> claims/wang-2025.yaml <<'EOF'
checks:
- date: 2026-11-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2b-area-ordering. The thalamus entry gave 8.26e-09 as the largest of the three thalamus p-values; the largest is ALM against thalamus, 2.80e-08 (Extended Data Fig. 3 legend). Split the two grouped entries into the seven pairs with their printed p-values.
  - fig2e-method-improvement. The criterion took the code's explained-variance threshold of 0.005 as the main reading and the Methods' 0.01 as the variant; the protocol puts the Methods first (Methods, Epoch-averaged explained variance). Swapped them.
  - fig3f-thalamic-nuclei. Removed the statistics entry p < 0.1; it is the threshold for showing pairs in Extended Data Fig. 4, not a result. Removed the requirement that VAL be lower than PO, VM and VP, which no text or legend states.
  - thalamus-ev-not-rate. The criterion required VAL to have the lowest mean; the text says only that VAL differed from PO/VM/VP. Now VAL must be the highest or the lowest of the four, with the direction reported.
  - fig4b-medulla-leads. Area curves were averaged over pooled neurons; the Fig. 4b legend gives the mean across sessions and the Methods (Data pooling) give uniform weights across sessions. Averaged within sessions, then over sessions, with pooled neurons as a variant.
  - edfig6-offset-ev-correlation. The striatum p was recorded as 3e-07, a reading of the legend's misprinted "3e7" that the checker cannot find; recorded the main text's P < 0.001 instead. Removed the rule that R within 0.03 counts as a match, which the paper does not give and which contradicted the stated 10% tolerances; R and counts outside tolerance now give partially reproduced.
  - fig5a-somatosensory-vs-alm. Added corrected Bonferroni to the statistic; the Fig. 5 legend says all three comparisons were Bonferroni corrected.
  - fig7d-alm-midbrain-vs-medulla. The threshold read "at least 0.65"; the Methods say "exceeded 0.65". Named counting all neurons above threshold (both included) as a variant, since the Methods note that some neurons pass for both.
  - supp-session-independent-autoencoder. The quote's ellipsis joined the training-session clause to the held-out value (12.8%, n=192), misreading as the training result; the quote now gives both clauses (3.6%, n=122 and 12.8%, n=192).
  - Open. The choice decoder of Figs. 6 and 7 is not described in the Methods and its code is not public; the criteria name readings (fig6a-choice-from-video).
  - Open. The direction of the VAL difference in Fig. 3f could not be read; no main-text PDF was supplied, so figures were not seen.
  - Open. Some criteria use this file's rules where the paper gives none (fig5-significant-offsets fallback, edfig10-subtraction-consistent five of six areas, fig4b-medulla-leads highest of five areas); each says so.
EOF
python tools/claims_check.py claims/wang-2025.yaml paper/10.1038-s41593-025-02114-x.txt; grep -n ": .*: " claims/wang-2025.yaml | grep -v '^\s*[0-9]*:\s*#' | sed -n '1,5p'
```

Result: not kept, because it reads the paper's text.

**Agent**

The checker searches for the string "2.8e-08", but the paper prints "2.80e-08". Checking how it matches values:

**Agent calls Bash**

```bash
cd  grep -n "def \|VALUE NOT FOUND\|e-0\|repr\|format" tools/claims_check.py | head -40
```

```
34:def norm(s: str) -> str:
41:def flattenings(raw: str) -> list[str]:
48:def quote_found(quote: str, texts: list[str]) -> bool:
63:def printed_forms(v: float) -> set[str]:
78:def check(claims_path: Path, paper_paths: list[Path]) -> int:
98:                    print("VALUE NOT FOUND (confirm by reading)", c["id"], v)
105:def main() -> int:
```

**Agent calls Read**

```json
{
 "file_path": "tools/claims_check.py",
 "offset": 60,
 "limit": 40
}
```

```
60	    return False
61	
62	
63	def printed_forms(v: float) -> set[str]:
64	    """Ways a paper prints a number: 0.002, .002, 2 × 10-5, 2e-5, 0.00002, 10-10."""
65	    out = {f"{v:g}", f"{v:g}".lstrip("0") if abs(v) < 1 else f"{v:g}"}
66	    if 0 < abs(v) < 1:
67	        m, e = f"{v:.3e}".split("e")
68	        m, e = f"{float(m):g}", str(int(e))
69	        out |= {f"{m}×10{e}", f"{m} × 10{e}", f"{m} x 10{e}", f"{m}x10{e}", f"{m}e{e}"}
70	        if m == "1":
71	            out.add(f"10{e}")
72	    if 0 < abs(v) < 0.001:
73	        plain = f"{v:.12f}".rstrip("0")
74	        out |= {plain, plain.lstrip("0")}
75	    return {f.lower() for f in out}
76	
77	
78	def check(claims_path: Path, paper_paths: list[Path]) -> int:
79	    doc = yaml.safe_load(claims_path.read_text())
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -i 's/^  - Open. Some criteria use this file/  - fig2b-area-ordering. The checker flags 2.8e-08 because it does not try the printed form 2.80e-08; confirmed by reading the Extended Data Fig. 3 legend.\n  - Open. Some criteria use this file/' claims/wang-2025.yaml; python - <<'EOF'
import yaml,re
t=open('claims/wang-2025.yaml').read()
d=yaml.safe_load(t)
for i,l in enumerate(t.splitlines(),1):
    s=l.strip()
    if s.startswith('#'): continue
    body=re.sub(r'^-?\s*[A-Za-z_]+:\s','',s.lstrip('- '))
    if ': ' in body and not body.startswith(('"',"'")): print(i,l)
print(len(d['checks'][-1]['changes']))
EOF
python tools/claims_check.py claims/wang-2025.yaml paper/10.1038-s41593-025-02114-x.txt; git diff --stat
```

Result: not kept, because it reads the paper's text.

**Agent**

I corrected 9 of the 29 claims in `claims/wang-2025.yaml` against the paper and added a check entry. The file is ready for an attempt.

**Checker result:** `claims/wang-2025.yaml: 29 claims, 29 quotes, 44 statistical values, 1 problems`. The one flag is `fig2b-area-ordering 2.8e-08`. The checker writes the number as 2.8e-08 and never tries the paper's printed form "2.80e-08". That value is in the Extended Data Fig. 3 legend. Before my changes the checker also reported one problem, the striatum p in edfig6, which is now fixed.

**Changes, by claim:**
- **fig2b-area-ordering:** the thalamus entry claimed 8.26e-09 was the largest of its three p-values. The largest is ALM against thalamus, 2.80e-08. I split the two grouped entries into the seven pairs, each with its printed p.
- **fig2e-method-improvement:** the criterion used the code's explained-variance threshold (0.005) as the main reading and the Methods' 0.01 as the variant. The protocol puts the Methods first, so I swapped them.
- **fig3f-thalamic-nuclei:** I removed a statistic, "p < 0.1", which is only the cutoff for which pairs Extended Data Fig. 4 displays, not a result. I also removed the requirement that VAL be lower than PO, VM and VP, because no text or legend states it.
- **thalamus-ev-not-rate:** "VAL lowest of the four" became "VAL highest or lowest", with the direction reported. The text says only that VAL differed from PO, VM and VP.
- **fig4b-medulla-leads:** area curves are now averaged within each session, then over sessions, as the Fig. 4b legend and Methods (Data pooling) say. Averaging over all pooled neurons is kept as a variant.
- **edfig6-offset-ev-correlation:** the striatum p is printed in the legend as "3e7", a misprint. I recorded the main text's P < 0.001 in its place. I removed a made-up rule that an R within 0.03 counts as a match. R values and counts outside tolerance now give "partially reproduced".
- **fig5a-somatosensory-vs-alm:** I added the Bonferroni correction, which the Fig. 5 legend states.
- **fig7d-alm-midbrain-vs-medulla:** the threshold now reads "exceeds 0.65", as in the Methods, not "at least 0.65". Counting every neuron above threshold, including those above it for both AUCs, is named as a variant.
- **supp-session-independent-autoencoder:** the quote's "..." joined the training-session clause to the held-out number (12.8%, n=192). It now gives both: training 3.6%, n=122, and held-out 12.8%, n=192.

**Still open:**
- **Choice decoder (Figs. 6 and 7):** the paper does not describe it and its code is not public, so the criteria list possible readings.
- **Direction of the VAL difference in Fig. 3f:** only the supplement PDF was supplied, not the main-text figures, so I could not see it.
- **Rules not from the paper:** a few criteria set thresholds of the file's own where the paper gives none (fig5-significant-offsets, edfig10-subtraction-consistent, fig4b-medulla-leads). Each criterion says so.

Every main finding has a claim, and every claim comes from this paper or its supplement. Nothing was committed.

## End of run

32 turns, 3 minutes, $1.42 at API prices, result: success.
