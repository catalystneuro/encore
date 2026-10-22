# 001250 · claims-check · run 39809137640

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001250/ paper/; grep -n -A60 '"Reader"\|## Reader\|Reader' docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; cat claims/001250/*.yaml; python tools/claims_check.py claims/001250/10.1101-2024.12.04.626805.yaml paper/10.1101-2024.12.04.626805.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 120,200p docs/protocol.md; python tools/claims_check.py claims/001250/10.1101-2024.12.04.626805.yaml paper/10.1101-2024.12.04.626805.txt | tail -30; wc -l claims/001250/*.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2024.12.04.626805.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml"
}
```

```
1	# Claims for Laquitaine, Imbeni, Tharayil, Isbister & Reimann, "Spike sorting biases and
2	# information loss in a detailed cortical model", bioRxiv doi:10.1101/2024.12.04.626805, on
3	# dandiset 001250.
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
5	# protocol as stated in docs/protocol.md (pilot-10), Reader steps 1 to 4.
6	#
7	# Text read: paper/10.1101-2024.12.04.626805.txt, from the bioRxiv JATS XML (header "preprint,
8	# version 1", stored 2026-10-20): main text, Methods, Discussion and the legends of the
9	# supplementary figures, which are part of the preprint. There is no separate supplement. No PDF
10	# was stored, so figures could not be read; every claim rests on the text and legends. The
11	# equations of the Methods (agreement score, chance score, line and point source) were lost in
12	# the extraction; the code settles the agreement and chance scores (below). Version caution: the
13	# abstract of this text ("about 15% of neurons") differs from the abstracts the bioRxiv API gives
14	# for versions 1 and 2 ("about 10%"), so the text may be a later revision than its header says.
15	# The supplementary figures are numbered inconsistently in the text (the Methods cite the
16	# delta-time figure as "Supplementary Fig. 3A"; the Results cite the sorted against true firing
17	# rate figure as Supplementary Fig. 6); sources below name the legend title as well.
18	#
19	# Code read: the paper says only "The codebase for the analyses is available on GitHub"; the link
20	# was lost in the text. It is github.com/steevelaquitaine/spikebias (README cites this DOI), commit
[... 787 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2024.12.04.626805.txt",
 "offset": 142,
 "limit": 100
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "offset": 806
}
```

```
806	- id: fig6c-f-accuracy-predictors
807	  statement: A fractional regression of Kilosort4 sorting accuracy on 21 neuron features fits the data
808	    (R2 = 0.42 spontaneous, 0.34 evoked) and finds seven significant features in both regimes; accuracy
809	    rises with firing rate and spike spatial extent, is higher for pyramidal cells and in layer 5, and
810	    falls with distance to the nearest electrode.
811	  source: Results, Biological factors of sorting failures, paragraph 4; Figure 6c-f
812	  quote: The model provided a good fit to the data ( Fig. 6 , R 2 = 0.42 and R 2 = 0.34 in the
813	    spontaneous (c) and evoked (d) regimes respectively) and identified seven significantly predictive
814	    features out of 21 in both regimes. Accuracy improved as neuronal firing rates increased and spike
815	    spatial extent (or ‘footprint’ [ 6 ]) expanded. It was also higher for pyramidal cells compared to
816	    interneurons and in layer 5 compared to other cortical layers. Sorting accuracy decreased when
817	    neuron’s distance to the nearest electrode increased
818	  expected:
819	  - quantity: R2, spontaneous
820	    value: 0.42
821	    tolerance: 0.042
822	  - quantity: R2, evoked
823	    value: 0.34
824	    tolerance: 0.034
825	  - quantity: significant features per regime
[... 239 more lines not kept]
```

**Agent**

The checker passes (39 claims, 0 problems). I've read the Results and the first half of the Methods; now reading the rest of the Methods and the supplementary legends.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1101-2024.12.04.626805.txt",
 "offset": 241,
 "limit": 150
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The paper's own counts settle two points in the Fig. 5a claims, so I'm correcting those now and then making smaller fixes.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "    multi-unit counts in the same five; (c) as (b) on M, H, NS, E and DS. \"On average 41%\" is read as\n    the fraction for NS (the sentence names it) and, as a variant, the mean of NS and NS-2X. Reproduced\n    when the fraction is within tolerance and the test has p < 0.001 under one reading.",
 "new_string": "    multi-unit counts in the same five; (c) as (b) on M, H, NS, E and DS. \"On average 41%\" is read three\n    ways - (i) the fraction for NS (the sentence names it); (ii) the mean of NS and NS-2X; (iii) the mean\n    of the M, NS and NS-2X fractions. The paper's own counts favour (iii) - the unit totals it prints\n    (M 200, NS 504, H 358, DS 562, Results paragraph 4, checked against its N values) and N = 1,212 for M,\n    NS and NS-2X give NS-2X 508 units, so NS is 182 / 504 = 36%, NS-2X 193 / 508 = 38% and M 96 / 200 =\n    48%, whose mean is 40.7%; reading (iii) also reproduces the paper's chi2 = 2.0 of\n    fig5a-single-unit-counts. Reproduced when the fraction is within tolerance and the test has p < 0.001\n    under one reading."
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "  - quantity: Kilosort4 single units, synthetic\n    value: 377\n    tolerance: 37.7\n  criterion: The text prints \"S 377 vs 163\"; 163 is not the M single-unit count elsewhere in the paper\n    (96), so the comparison count is open. Kilosort4, first 10 minutes. Reproduced when S has more\n    than half single units, about four times M's count (ratio within 3.6 to 4.4, under either 96 or\n    the M total of units read as the comparison), and the code's goodness-of-fit chi-square of the\n    single-unit percentages of M and S (fig5_A_yield, cell 14) has p < 0.05.",
 "new_string": "  - quantity: Kilosort4 single units, synthetic\n    value: 377\n    tolerance: 37.7\n  - quantity: Kilosort4 multi-units, synthetic\n    value: 163\n    tolerance: 16.3\n  criterion: In \"S 377 vs. 163\", 163 is S's multi-unit count - N = 740 is S's 540 units (377 + 163) plus\n    M's 200 units (96 single, 104 multi, Results paragraphs 2 and 4), and the goodness-of-fit chi-square\n    of the single-unit percentages (S 69.8%, M 48.0%) against equal values gives 4.0, the printed value.\n    \"Four times more than in vivo\" is S's 377 single units against M's 96 (3.9). Kilosort4, first 10\n    minutes. Reproduced when the two S counts are within tolerance, S has more than half single units,\n    S's single units are 3.6 to 4.4 times M's (four widened by 10%), and the goodness-of-fit chi-square\n    of the single-unit percentages of M and S (code fig5_A_yield, cell 14) has p < 0.05."
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "    p: 0.9\n  data: with_inputs\n  criterion: Kilosort4, first 10 minutes, cortical units, dense probe counts summed over the three\n    depths.",
 "new_string": "    p: 0.9\n  data: with_inputs\n  expected:\n  - quantity: Kilosort4 multi-units, Marques-Smith\n    value: 104\n    tolerance: 10.4\n  - quantity: Kilosort4 multi-units, Horvath (three depths summed)\n    value: 265\n    tolerance: 26.5\n  criterion: Kilosort4, first 10 minutes, cortical units, dense probe counts summed over the three\n    depths. The unit totals are M 200, H 358, NS 504 and DS 562 (\"358 vs 200 units and 562 vs. 504\n    units respectively\", which the N values 558 = 200 + 358 and 1066 = 504 + 562 confirm)."
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "    Reproduced when NS and M each give six clusters under the code's choice or the 1.5 variant, with\n    six, three or six electrodes; every count is reported.",
 "new_string": "    Reproduced when NS and M each give six clusters under the code's choice or the 1.5 variant, with\n    six (Methods) or three (legend) electrodes; every count is reported."
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "Model - Binomial GLM with logit link (statsmodels). The legend says lasso\n    without a penalty; the Methods and the code fit it unpenalised, which is followed.",
 "new_string": "Model - Binomial GLM with logit link (statsmodels). The Figure 5 legend calls\n    it lasso-regularized but gives no penalty; the Methods (Logistic regression model) describe a GLM\n    with no penalty and the code fits it unpenalised, which is followed."
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent**

Next: the Kilosort3 panel ambiguity, the missing `data` on fig6ab, and the t-value inconsistencies in Fig. 7.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "    on the paper's test - reproduced when no layer's Mann-Whitney U test of Kilosort3 medians against\n    M has p <= 0.15 (the code's notebooks supp_fig4_ABC_ks3 run the same per-layer test).",
 "new_string": "    on the paper's test - reproduced when no layer's Mann-Whitney U test of Kilosort3 against M has\n    p <= 0.15 (the code's notebooks supp_fig4_ABC_ks3 run the same per-layer test). Which quantity the\n    p > 0.15 refers to is open - the Results call panel b the medians (and c the variances), while the\n    supplementary legend calls panel a the rate statistics and panel b the variances; both medians and\n    bootstrapped variances are run, and the outcome is the one both give."
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "    p: 0.43\n  expected:\n  - quantity: well-sorted proportion of ground truth neurons within 50 um, average over sorters",
 "new_string": "    p: 0.43\n  data: with_inputs\n  expected:\n  - quantity: well-sorted proportion of ground truth neurons within 50 um, average over sorters"
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "    Reproduced when the type test has p < 0.001 for every sorter, good units are below the ground truth",
 "new_string": "    The paper's printed range includes t(199) = -0.31, which gives p of about 0.76, so its \"all p <\n    0.001\" and its t range disagree; the per-sorter t and p are reported and the disagreement is a\n    deviation. Reproduced when the type test has p < 0.001 for every sorter, good units are below the ground truth"
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "    fig7b-sorting-halves-capacity, relative to the ground truth's. Whether the averages include the",
 "new_string": "    fig7b-sorting-halves-capacity, relative to the ground truth's. The printed radius range includes\n    t(199) = 0.18, which cannot give p < 0.001, so \"all p < 0.001\" and the t range disagree; per-sorter\n    t and p are reported. Whether the averages include the"
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "    exc_mini_frequency and dynamics_holding_current, z-scored. Model - Binomial GLM, logit link,\n    statsmodels fit_regularized elastic_net with L1_wt 1, maxiter 100, cnvrg_tol 1e-10 (Methods). The\n    lasso penalty is not given anywhere; the code passes none, so statsmodels' alpha 0 applies, which\n    is followed.",
 "new_string": "    exc_mini_frequency and dynamics_holding_current, z-scored. Model - Binomial GLM, logit link,\n    statsmodels fit_regularized elastic_net with L1_wt 1, maxiter 100, cnvrg_tol 1e-10 (Methods). The\n    lasso penalty strength is not given anywhere; the code passes none, so statsmodels' alpha 0\n    applies, which is followed. With alpha 0 no weight is set to zero, which does not match the\n    Methods' account of the lasso selecting features; this is recorded as a deviation, and a penalised\n    fit cannot be run from the paper."
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
grep -rn -A8 "^checks:" claims/ | head -30
```

```
claims/001750/10.1038-s41556-026-02009-4.yaml:735:checks:
claims/001750/10.1038-s41556-026-02009-4.yaml-736-- date: 2026-10-21
claims/001750/10.1038-s41556-026-02009-4.yaml-737-  kind: agent
claims/001750/10.1038-s41556-026-02009-4.yaml-738-  model: claude-opus-5-5
claims/001750/10.1038-s41556-026-02009-4.yaml-739-  ready: true
claims/001750/10.1038-s41556-026-02009-4.yaml-740-  changes:
claims/001750/10.1038-s41556-026-02009-4.yaml-741-  - fig4d-sodium-current-lower, reading (a2) restated to match Fig4d_plotNaCurrent.m, which subtracts the mean of the first 100 samples of a cut starting 2 ms before onset (2 ms at 50 kHz, 1 ms at 100 kHz), not the 2 ms before onset.
claims/001750/10.1038-s41556-026-02009-4.yaml-742-  - model-sd-na-density, statement said the 55 to 80 pS/um2 range was set by the recordings; the Extended Data Fig. 7c legend says it was defined by experimental data and previous publications.
claims/001750/10.1038-s41556-026-02009-4.yaml-743-  - model-na-ratio, criterion now notes the Extended Data Fig. 7c legend, by which 55 pS/um2 may not be the recorded ratio alone.
--
claims/001749/10.1038-s41586-022-04507-5.yaml:1145:checks:
claims/001749/10.1038-s41586-022-04507-5.yaml-1146-- date: 2026-10-21
claims/001749/10.1038-s41586-022-04507-5.yaml-1147-  kind: agent
claims/001749/10.1038-s41586-022-04507-5.yaml-1148-  model: "claude-opus-5-5"
claims/001749/10.1038-s41586-022-04507-5.yaml-1149-  ready: true
claims/001749/10.1038-s41586-022-04507-5.yaml-1150-  changes:
claims/001749/10.1038-s41586-022-04507-5.yaml-1151-  - fig1b-dominants-more-rewards; removed "rank 1 mice won the largest share of competitions" from the statement and criterion, as no sentence of the paper states it (the Figure 1b legend only names the panel).
claims/001749/10.1038-s41586-022-04507-5.yaml-1152-  - ed1g-distance-by-outcome-not-rank; dropped the "win closer" direction from the criterion, as the legend gives no direction for trial type.
claims/001749/10.1038-s41586-022-04507-5.ya
[... 11 more lines not kept]
```

**Agent calls Grep**

```json
{
 "pattern": "one reading|under either|holds under",
 "path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "output_mode": "content"
}
```

```
149:    Reproduced when, under one reading, the three values are within tolerance.
246:    1 to 6 with at most one inversion between neighbours, under one reading of AP power; partially
348:    under either. With 0 units in layer 4 the ratio is infinite and holds.
380:    within tolerance under one reading. Which evoked simulation is open, as in
481:    under one reading.
560:    both are run, and the claim holds under either.
638:    biophysical models' Kilosort4 yields are lower by an order of magnitude under one reading.
696:    when all four values are within tolerance under one reading.
726:    tolerance and is the largest in magnitude among the metrics under one reading, and the weights of
781:    Reproduced when, under one reading, both values are within tolerance and a majority of the six
807:    over sorters is within tolerance under one reading and the chi-square has p >= 0.05 (the paper's
824:    neurons per sorter; reproduced when both values are within tolerance under one reading of
918:    one reading, for a majority of sorters, the excitatory types of layer 5 have ratios of 1.5 or more
970:    lower with p < 0.001, and the mean decrease is within tolerance under one reading.
1047:    at p < 0.001 for every sorter with a mean decrease within tolerance under one reading of a decrease,
```

**Agent calls Read**

```json
{
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "offset": 238,
 "limit": 12
}
```

```
238	    p_relation: "<"
239	  data: with_inputs
240	  criterion: AP power per site is the PSD power in 0.3 to 2 kHz (Results, paragraph 3); the code's
241	    revised notebook uses the median PSD in 0.3 to 1 kHz (fig2_R_AP_power_npx_revised), shown as a
242	    variant. Both the median PSD value in the band and the summed power in the band are read, since
243	    the text says "median power" and "power". The slope alpha is from the 0.3 to 6 kHz fit of
244	    fig2r-power-law-spiking-band. For each model (NS, E, DS), a Kruskal-Wallis test across layers.
245	    Reproduced when both measures have p < 0.001 in every model, with layer medians rising from layer
246	    1 to 6 with at most one inversion between neighbours, under one reading of AP power; partially
247	    reproduced when this holds for one measure or some models. Whether the DS values lie within the
248	    range of H's site values is reported.
249	- id: supp2-no-slow-oscillations
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "    Reproduced when both measures have p < 0.001 in every model, with layer medians rising from layer\n    1 to 6 with at most one inversion between neighbours, under one reading of AP power; partially\n    reproduced when this holds for one measure or some models.",
 "new_string": "    Reproduced when both measures (AP power and alpha) have p < 0.001 in every model, with layer\n    medians rising from layer 1 to 6 with at most one inversion between neighbours; for AP power in\n    0.3 to 2 kHz the median and summed readings are both run and the outcome is the one both give\n    (methods_underspecified when they differ); the 0.3 to 1 kHz band is a variant, not used for the\n    outcome. Partially reproduced when this holds for one measure or some models."
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "offset": 688,
 "limit": 12
}
```

```
688	    (Methods, Logistic regression). Features - the quality metrics of ref. 16 named by the code
689	    (src/nodes/models/Flc), amplitude_cutoff, firing_range, firing_rate, isi_violations_ratio,
690	    rp_contamination, rp_violations, sd_ratio, snr, silhouette and mad_ratio (presence_ratio dropped
691	    as constant), z-scored. Model - Binomial GLM with logit link (statsmodels). The Figure 5 legend calls
692	    it lasso-regularized but gives no penalty; the Methods (Logistic regression model) describe a GLM
693	    with no penalty and the code fits it unpenalised, which is followed. A unit is
694	    predicted good when its probability is 0.8 or more (code; the paper is silent). Splits are open -
695	    (a) 80% train and 20% test (Methods), (b) 75% and 25% (legend "25% test units", code
696	    split_ratio 0.75); 100 random splits each. The value is the median over splits; the CI is 1.96
697	    SD / sqrt(100) (code get_metrics_stats). Which evoked recording is open; both are run. Reproduced
698	    when all four values are within tolerance under one reading.
699	  depends_on:
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "    SD / sqrt(100) (code get_metrics_stats). Which evoked recording is open; both are run. Reproduced\n    when all four values are within tolerance under one reading.",
 "new_string": "    SD / sqrt(100) (code get_metrics_stats). The split is a method detail on which the Methods and the\n    legend disagree, so both are run and the outcome is the one both give (methods_underspecified when\n    they differ). Which evoked recording is meant is a reading of the reported number; both are run\n    and either may match. Reproduced when all four values are within tolerance under both splits."
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "offset": 772,
 "limit": 40
}
```

```
772	    neurons with accuracies ranging from 50% for herdingspikes to 99% for Kilosort2
773	  data: with_inputs
774	  expected:
775	  - quantity: well-sorted fraction of the 250 synthetic neurons, herdingspikes
776	    value: 0.50
777	    tolerance: 0.05
778	  - quantity: well-sorted fraction of the 250 synthetic neurons, Kilosort2
779	    value: 0.99
780	    tolerance: 0.099
781	  criterion: The ground truth of S is its 250 units. Accuracy per neuron and the 0.8 rule as in the
782	    opening comment; the fraction of neurons with accuracy of 0.8 or more per sorter (Figure 6a legend).
783	    Which sorted units enter the best match is open - (a) all units (Methods, Sorting accuracy); (b)
784	    single units for Kilosort 2 to 4 and all units for Kilosort and herdingspikes (code get_accuracy).
785	    Reproduced when, under one reading, both values are within tolerance and a majority of the six
786	    sorters have a fraction above 0.5.
787	- id: fig6ab-biophysical-accuracy-15-percent
788	  statement: For the biophysical models the sorters well-sort similarly low proportions of ground truth
789	    neurons, on average 15% of the neurons within 50 um of the electrodes.
790	  source: Results, Biological factors of sorting failures, paragraph 2; Figure 6a, b
791	  quote: However, the sorters produced similarly low proportions of well-sorted ground truth neurons for
[... 20 more lines not kept]
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "    Which sorted units enter the best match is open - (a) all units (Methods, Sorting accuracy); (b)\n    single units for Kilosort 2 to 4 and all units for Kilosort and herdingspikes (code get_accuracy).\n    Reproduced when, under one reading, both values are within tolerance and a majority of the six\n    sorters have a fraction above 0.5.",
 "new_string": "    Which sorted units enter the best match - the Methods (Sorting accuracy) say only \"its\n    best-matching sorted unit\", and the code settles it - single units for Kilosort 2 to 4 and all\n    units for Kilosort and herdingspikes (code get_accuracy), which decides; all units for every sorter\n    is shown as a variant. Reproduced when both values are within tolerance and a majority of the six\n    sorters have a fraction above 0.5."
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "    Best-match readings as in fig6a-synthetic-accuracy-range.",
 "new_string": "    Best-match units as in fig6a-synthetic-accuracy-range (the code's choice decides)."
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Read**

```json
{
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "offset": 811,
 "limit": 20
}
```

```
811	    chi-square of well-sorted against other neurons per sorter is a variant. Reproduced when the mean
812	    over sorters is within tolerance under one reading and the chi-square has p >= 0.05 (the paper's
813	    "similarly", on its test).
814	- id: fig6-dense-probe-lower-accuracy
815	  statement: The dense probe gives five times fewer neurons sorted with above 80% accuracy than the
816	    Neuropixels probe, on average 3% against 15% across sorters.
817	  source: Results, Biological factors of sorting failures, paragraph 3; Figure 6a, b
818	  quote: We found that the dense probe produced five times fewer neurons sorted with above 80% accuracy
819	    across spike sorters than the Neuropixels probe (on average 3% vs. 15%)
820	  expected:
821	  - quantity: well-sorted proportion, dense probe, average over sorters
822	    value: 0.03
823	    tolerance: 0.003
824	  - quantity: well-sorted proportion, Neuropixels, average over sorters
825	    value: 0.15
826	    tolerance: 0.015
827	  criterion: DS depths pooled (Figure 6b legend), well-sorted neurons divided by ground truth neurons
828	    within 50 um. The 10% default tolerance on 3% is below the resolution of a sum over a few hundred
829	    neurons per sorter; reproduced when both values are within tolerance under one reading of
830	    fig6ab-biophysical-accuracy-15-percent, or when the Neuropixels value is within tolerance and the
```

**Agent calls Read**

```json
{
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "offset": 910,
 "limit": 18
}
```

```
910	  - quantity: largest over-representation ratio of a rare interneuron type
911	    value: 8.1
912	    tolerance: 0.81
913	  criterion: The 1-hour evoked simulation at 20 kHz (Figure 6 legend). Types are synapse class, layer and
914	    electrical type. Ground truth - all neurons within 50 um. Sorted - single units of Kilosort 2 to 4,
915	    all units of Kilosort and herdingspikes, each given the synapse class and electrical type of its
916	    best-matching neuron (Results). Its layer is open - (a) the matched neuron's layer (Results,
917	    "assigned ... the biophysical features of its best-matched ground truth neuron"); (b) the unit's
918	    site layer, as the code does (fig6_G_H_selection_bias, get_feature_data_for). Which sorting
919	    duration is open; the code's table is named "1h" but its generator sorts 600 s; both are run where
920	    possible. Ratio - share of a type among sorted units / its share in the ground truth. Test - per
921	    type and sorter, two-sided Fisher's exact test on [[ground truth of the type, sorted of the type],
922	    [ground truth others, sorted others]] (code cell 18), p < 0.05, uncorrected. Reproduced when, under
923	    one reading, for a majority of sorters, the excitatory types of layer 5 have ratios of 1.5 or more
924	    and those of the other layers ratios of 0.67 or less, with p < 0.05 for those that differ; and the
925	    largest ratio of an interneuron type is within 2.6 to 8.9 for at least one of Kilosort, 2 or 2.5.
926	    Partially reproduced when only the excitatory part holds.
927	- id: fig7a-ring-manifold
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "best-matching neuron (Results). Its layer is open - (a) the matched neuron's layer (Results,\n    \"assigned ... the biophysical features of its best-matched ground truth neuron\"); (b) the unit's\n    site layer, as the code does (fig6_G_H_selection_bias, get_feature_data_for). Which sorting\n    duration is open; the code's table is named \"1h\" but its generator sorts 600 s; both are run where\n    possible.",
 "new_string": "best-matching neuron (Results). Its layer is the matched neuron's layer, as the Results and the\n    Figure 6h legend say (\"assigned the biophysical features of its best ground truth match\"), which\n    decides; the code's site layer (fig6_G_H_selection_bias, get_feature_data_for) disagrees with them\n    and is a variant. Which sorting duration is open; the code's table is named \"1h\" but its generator\n    sorts 600 s; both are run where possible, and the outcome is the one both give\n    (methods_underspecified when they differ)."
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "p < 0.05, uncorrected. Reproduced when, under\n    one reading, for a majority of sorters,",
 "new_string": "p < 0.05, uncorrected. Reproduced when, for a\n    majority of sorters,"
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001250/10.1101-2024.12.04.626805.yaml",
 "old_string": "    Reproduced when NS and M each give six clusters under the code's choice or the 1.5 variant, with\n    six (Methods) or three (legend) electrodes; every count is reported.",
 "new_string": "    Reproduced when NS and M each give six clusters with six electrodes (Methods) and the code's\n    resolution choice, which decide; the 1.5 resolution and the three electrodes of the legend (a\n    display choice) are variants, reported and not used for the outcome."
}
```

```
The file claims/001250/10.1101-2024.12.04.626805.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cat >> claims/001250/10.1101-2024.12.04.626805.yaml <<'EOF'
checks:
- date: 2026-10-22
  kind: agent
  model: "claude-opus-5-5"
  ready: true
  changes:
  - fig5a-synthetic-mostly-single-units, the criterion treated 163 as an open comparison count. The paper's numbers settle it - 163 is S's multi-unit count (N = 740 = 377 + 163 + M's 200 units), the goodness-of-fit chi-square of 69.8% against 48.0% gives the printed 4.0, and "four times" is 377 against M's 96. Criterion rewritten, S multi-units 163 added to expected.
  - fig5a-single-unit-fraction-differs, added reading (iii), the mean of the M, NS and NS-2X single-unit fractions (40.7% from the paper's own counts and N values). NS alone is 182 / 504 = 36%, so reading (i) disagrees with the paper's printed counts.
  - fig5a-dense-probe-more-multi-units, added the reported multi-unit counts (M 104, H 265) to expected and the unit totals (M 200, H 358, NS 504, DS 562) to the criterion, checked against the printed N values.
  - fig6ab-biophysical-accuracy-15-percent, added data with_inputs, since the main reading sums Buccino's synthetic simulation (outside data) into N = 3,190.
  - fig6a-synthetic-accuracy-range and fig6ab-biophysical-accuracy-15-percent, which sorted units enter the best match was settled by "under one reading" of two options. The Methods leave it open and the code settles it, so the code's choice now decides and the all-units version is a variant.
  - fig6gh-selection-bias-layer5-pyramidal, a sorted unit's layer was open between the matched neuron's layer and the code's site layer, decided under one reading. The Results and the Figure 6h legend give the matched neuron's features, so that decides and the code's choice is a variant. The sorting duration is now judged by the outcome both durations give.
  - fig5ef-curation-precision-recall, the train and test split (80/20 in the Methods, 75/25 in the legend and code) is a method detail. The claim was decided under one reading, so both splits must now give the outcome, or the claim is methods_underspecified. Also corrected the description of the legend, which calls the model lasso-regularized with no penalty given.
  - fig2s-v-ap-power-and-scaling-increase-with-depth, the median and summed AP power readings were decided under one reading. Both must now agree. The code's 0.3 to 1 kHz band, from a later revision, is a variant not used for the outcome.
  - fig3fg-wavemap-six-profiles, fixed "six, three or six electrodes". Six electrodes (Methods) and the code's resolution now decide. Three electrodes (a legend display choice) and resolution 1.5 are variants.
  - supp4-other-sorters-firing-rates, named as open whether "b, p > 0.15" concerns medians or variances. The Results call panel b the medians, and the supplementary legend calls panel b the variances. Both are run and must agree.
  - fig6c-f-accuracy-predictors, noted that the code's alpha 0 sets no weight to zero, against the Methods' lasso feature selection. Recorded as a deviation, since no source gives the penalty.
  - fig7g-assignment-bias-capacity and fig7h-j-manifold-geometry, noted that the printed t ranges (-0.31 and 0.18 with df 199) contradict "all p < 0.001". Per-sorter t and p are to be reported.
  - Open, not settled - several criteria judge words the paper leaves without a measure, using thresholds chosen in the criterion and not taken from the paper. These are the layer ordering with at most one inversion (fig2m, fig2np, fig2s-v), R2 of 0.9 or more (fig2r), a factor of 2 in low-frequency power share (supp2), Shapiro-Wilk on log rates (fig4a-lognormal), ratios of 1.5 and 0.67 for "about a factor of 2" (fig6gh), cyclic centroid order (fig7a), the 10% widened range limits (fig2q) and a majority of units tagged merged (fig5cd). Each is labelled as such in its criterion. Their outcomes rest on these choices, so they should be read as such.
  - Open, not settled - which five experiments enter the chi2(4, N = 5,241) test of fig5a-single-unit-fraction-differs cannot be fixed from the text without the evoked unit total.
  - Open, not settled - the code repository and commit cited in the opening comment were not re-read in this check. Code-based details are taken as the previous reader recorded them.
EOF
python tools/claims_check.py claims/001250/10.1101-2024.12.04.626805.yaml paper/10.1101-2024.12.04.626805.txt | tail -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^checks:/,$p' claims/001250/*.yaml | grep -n -e '—' -e 'rather' -e ': .*: ' ; python -c "import yaml;d=yaml.safe_load(open('claims/001250/10.1101-2024.12.04.626805.yaml'));print(len(d['checks'][0]['changes']))"; git status --short
```

```
15
 M claims/001250/10.1101-2024.12.04.626805.yaml
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
?? scripts
```

**Agent**

The claims file for DANDI:001250 is fit for an attempt after my corrections, and I marked it `ready: true`. Only `claims/001250/10.1101-2024.12.04.626805.yaml` changed; nothing is committed.

**Checker:** `39 claims, 39 quotes, 26 statistical values, 0 problems`, both before and after my edits.

**Changes, by claim:**
- **fig5a-synthetic-mostly-single-units:** the criterion left "S 377 vs. 163" as an open comparison. The paper's own numbers settle it:
  - 163 is the synthetic simulation's multi-unit count: N = 740 is its 540 units plus Marques-Smith's 200.
  - The test is the code's chi-square on single-unit percentages, which gives the printed 4.0.
  - "Four times" is 377 against Marques-Smith's 96.
  
  I rewrote the criterion and added 163 to the expected values.
- **fig5a-single-unit-fraction-differs:** I added a third reading of "on average 41%": the mean of the Marques-Smith, NS and NS-2X fractions (48%, 36%, 38%, mean 40.7%). It also reproduces the paper's chi-square of 2.0. The NS fraction alone is 182/504 = 36%, which does not match 41%.
- **fig5a-dense-probe-more-multi-units:** added the multi-unit counts (Marques-Smith 104, Horvath 265) to the expected values, and the unit totals (200, 358, 504, 562), checked against the printed N values.
- **fig6ab-biophysical-accuracy-15-percent:** added `data: with_inputs`, because N = 3,190 includes the synthetic simulation, which is outside data.
- **fig6a and fig6ab:** the Methods leave open which sorted units enter the best match, and the code settles it, so the code's choice now decides. The all-units version is a variant.
- **fig6gh-selection-bias-layer5-pyramidal:** a unit's layer is now the matched neuron's layer, as the Results and the Fig. 6h legend say; the code's site layer is a variant. The two sorting durations must now agree.
- **Method details that had been decided "under one reading"** now need all readings to agree, or the claim is blocked as `methods_underspecified`. The protocol only allows "any reading" for ambiguity in a reported number.
  - fig5ef: the train/test split, 80/20 in the Methods against 75/25 in the legend and code.
  - fig2s-v: median against summed AP power.
- **fig3fg-wavemap-six-profiles:** fixed the "six, three or six electrodes" typo. Six electrodes (Methods) and the code's resolution now decide; the rest are variants.
- **supp4-other-sorters-firing-rates:** named as open whether "b, p > 0.15" refers to medians or variances. The Results and the supplementary legend label panel b differently, so both are run.
- **fig6c-f-accuracy-predictors:** noted that the code runs no penalty at all, while the Methods describe a lasso that selects features. Recorded as a deviation.
- **fig7g and fig7h-j:** noted that printed t values of -0.31 and 0.18 contradict "all p < 0.001".

**Still open (recorded in the checks entry):**
- Several criteria judge vague words with thresholds the earlier reader chose, not the paper. Examples: "rising with depth" allows at most one inversion, a power law needs a fit of R² ≥ 0.9, and log-normal is tested with Shapiro-Wilk. Others are in fig6gh, fig7a, fig2q, fig5cd and supp2. Each is labelled as a choice, but the outcomes rest on them.
- Which five experiments enter the chi2(4, N = 5,241) test can't be fixed without the evoked unit total.
- I did not re-read the code repository. Details taken from the code are as the previous reader recorded them.

The main findings each have a claim, and every claim comes from this paper.

## End of run

35 turns, 4 minutes, result: success.
