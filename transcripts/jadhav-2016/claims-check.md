# crcns-hc-28 · claims-check · run 42478648902

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls claims/crcns-hc-28/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 100,220p docs/protocol.md; cat claims/crcns-hc-28/*.yaml; python tools/claims_check.py claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml paper/10.1016-j.neuron.2016.02.010.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml paper/10.1016-j.neuron.2016.02.010.txt 2>&1 | tail -30; wc -l claims/crcns-hc-28/*.yaml paper/10.1016-j.neuron.2016.02.010.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml"
}
```

```
1	# Claims for Jadhav, Rothschild, Roumis & Frank (2016), Neuron 90:113-127, on CRCNS data set
2	# hc-28 (doi:10.6080/K02N50G9).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-08,
4	# protocol as stated in docs/protocol.md (version pilot-13, Reader).
5	#
6	# Text read: the version of record with its Supplemental Information, as supplied under paper/
7	# (PyMuPDF text of the journal PDF, 43 pages): Results, Discussion, Experimental Procedures, the
8	# legends of Figures 1 to 8 and S1 to S7, Tables S1 to S3 and the Supplemental Experimental
9	# Procedures. The extracted text prints minus signs and some symbols as a replacement character,
10	# so "p < 10-11" appears as "p < 10?11"; such values were read in context. The PDF could not be
11	# rendered in this run, so no value was read from a figure; values shown only in figures (the
12	# ensemble-size groups of Figure 6E, the bars of Figures 5F, 6E and 8D) are not recorded.
13	#
14	# Code read: none. The paper links no code; it says only that analyses used custom Matlab
15	# routines. Methods details therefore come from the Experimental Procedures and the
16	# Supplemental Experimental Procedures, and the details they leave open are named in each
17	# criterion with the readings the text allows.
18	#
19	# Data the paper used. Six male Long Evans rats, three on a W-track spatial alternation task and
20	# three on a Y-track auditory cue-guided task, 8 to 12 days of training, 2 to 4 run sessions of
[... 962 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 220,400p docs/protocol.md | grep -n -i -B2 -A8 "pooled\|checks\|ready" | head -80
```

```
11-     its own; the others count towards what is said about the dataset.
12-   - `with_labels` is for outside sources that only name or map codes the
13:     dataset already holds, such as stimulus names for its stimulus codes.
14-     They bring in no measurements. A link claim must confirm the names, and
15-     the missing names are recorded as a finding (`metadata_insufficient`).
16-   - When outside data has to be matched to the dataset's cells, sessions
17-     or subjects, a claim of its own (`kind: link`) tests the link. Link
18:     claims are the registry's checks, not findings of the paper, so the
19-     author adds them to the claims file; they are the only claims the
20-     author writes. A link claim says how
21-     records are matched (an identifier, or, where there is none, summary
22-     values the paper or its code published, such as per-condition medians),
23-     what fraction match, and whether the matched records agree on what both
24-     describe, such as counts, layers, or the paper's own per-cell tables. A
25-     dataset that cannot be linked to the data it was published with is a
26-     finding about the dataset. Every claim that needs the match lists the
```

**Agent calls Read**

```json
{
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "offset": 982
}
```

```
982	    tolerance: 0.02
983	  - quantity: r, SWR-inhibited pairs
984	    value: 0.36
985	    tolerance: 0.036
986	  criterion: Spatial correlation is the Pearson correlation of the two cells' linearized rate maps
987	    concatenated over the 4 trajectories (SEP; concatenation is the standard reading, the mean of
988	    per-trajectory correlations a variant). Group difference by the SEP shuffle (mixed
989	    populations of the same sizes, 1000 times). Reproduced when both r > 0 at p < 0.05, the
990	    inhibited r exceeds the excited r at p < 0.05 by the shuffle, and the correlated and
991	    anticorrelated groups differ from uncorrelated as stated at p < 0.05; r by the pooled-value
992	    rule.
993	  depends_on:
994	  - fig6-swr-correlated-pairs
995	  - fig5c-spatial-coverage
996	- id: figs5-matched-selectivity
997	  statement: With PFC cells matched for spatial coverage, excited and inhibited groups show similar
998	    spatial-SWR correlation relations (r = 0.32 and 0.39, not different).
999	  source: Figure S5 legend
1000	  quote: Both CA1-PFC excited pairs (n = 203, r = 0.32, p < 10-4) and CA1-PFC inhibited pairs (n =
1001	    203, r = 0.39, p < 10-4) showed significant correlations and these correlations were not
[... 176 more lines not kept]
```

**Agent**

Checker found 3 values it couldn't match (likely the minus-sign garbling). Now reading the paper against the claims.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.02.010.txt",
 "offset": 1,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.02.010.txt",
 "offset": 700,
 "limit": 450
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.02.010.txt",
 "offset": 1149,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "Supplemental Experimental Procedures|SWR Detection|SWR Modulation|Timing of SWR|Theta Phase Locking|Spatial and Behavioral|Replay analysis|GLM|Task and rest|z = 6|Behavioral Tasks|Data Analysis",
 "path": "paper/10.1016-j.neuron.2016.02.010.txt",
 "output_mode": "content"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.02.010.txt",
 "offset": 2040,
 "limit": 952
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Paper read. Checking Figure 6E in the PDF for the ensemble-size groups, since the claims file says the PDF could not be rendered.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2016.02.010.pdf",
 "pages": "11"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import fitz;d=fitz.open('paper/10.1016-j.neuron.2016.02.010.pdf');p=d[10]
print(p.get_text()[:3000])" 2>&1 | head -80
```

Result: not kept, because it reads the paper's text.

**Agent**

PDF can't be rendered here (no poppler or PyMuPDF), so the Figure 6E groups stay open. Applying the corrections now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    fall within tolerance under one reading of the open details, and excited and inhibited\n    counts are similar (each within 10 percentage points of the other as a fraction of\n    modulated cells). The shuffle",
 "new_string": "    fall within tolerance under one reading of the open details, and excited and inhibited\n    counts are similar. The paper gives no test or threshold for \"approximately equal\"; the\n    threshold used, each within 10 percentage points of the other as a fraction of modulated\n    cells, is a choice not taken from the paper (the paper's own counts differ by 7 points on\n    the W-track and 5 points overall). The shuffle"
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    standard choice. Rank-sum tests. Reproduced when CA1 is earlier than both PFC groups at p <\n    0.05 and excited and inhibited do not differ at p < 0.05, with the means judged by the\n    pooled-value rule.",
 "new_string": "    standard choice. Rank-sum tests. Reproduced when CA1 is earlier than both PFC groups at p <\n    0.05 and excited and inhibited do not differ at p < 0.01 (the paper's threshold for\n    comparisons between SWR-excited, SWR-inhibited and SWR-unmodulated cells, SEP Data\n    Analysis), with the means judged by the pooled-value rule."
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    Reproduced when, under one reading, both PFC groups are later than CA1 at p < 0.05 by\n    rank-sum and excited and inhibited do not differ at p < 0.05.",
 "new_string": "    Reproduced when, under one reading, both PFC groups are later than CA1 at p < 0.05 by\n    rank-sum and excited and inhibited do not differ at p < 0.01 (the paper's threshold for\n    comparisons between PFC SWR categories, SEP Data Analysis)."
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    cross-covariance (SD 16.7 ms) are taken from the SEP as the nearest stated choice. Reproduced\n    when both extrema lie after 0 ms and within tolerance (pooled-value rule).",
 "new_string": "    cross-covariance (SD 16.7 ms) are taken from the SEP as the nearest stated choice. The\n    window for the extremum is not given; -200 to +200 ms, the theta cross-covariance window\n    (SEP), is the nearest stated choice. The text reports the extremum of the mean\n    cross-covariance with a spread (13 +- 7 ms), so how the value and its spread were formed is\n    open; readings are (a) the extremum lag of the mean cross-covariance over pairs, (b) the mean\n    over pairs of each pair's extremum lag. Reproduced when, under one reading, both extrema lie\n    after 0 ms and within tolerance (pooled-value rule)."
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "  criterion: Preferred phase per significantly locked cell is the von Mises mean of its spike\n    phases, theta from the corpus callosum reference tetrode (SEP). The phase convention is not",
 "new_string": "  criterion: Preferred phase per significantly locked cell is the peak of its theta-phase\n    histogram (Figure 4A legend, \"peak theta phase\", \"distribution of peak phases\"), theta from\n    the corpus callosum reference tetrode (SEP); the histogram bin is not given, and the von\n    Mises mean of the spike phases is shown as a variant. The phase convention is not"
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    (0 to 180 degrees) and the modal 45-degree bin of PFC preferred phases contains 180 degrees,\n    with the CA1 mean earlier than the PFC mean.",
 "new_string": "    (0 to 180 degrees) and the modal 45-degree bin of PFC preferred phases contains 180 degrees\n    (the 45-degree bin is a standard choice), with the CA1 mean earlier than the PFC mean."
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "  criterion: Two-sample z tests for proportions. Reproduced when both modulated groups have a\n    higher fraction than unmodulated at p < 0.05 and excited and inhibited do not differ at p <\n    0.05, with fractions judged by the pooled-value rule.",
 "new_string": "  criterion: Two-sample z tests for proportions, at the paper's threshold for comparisons\n    between SWR-excited, SWR-inhibited and SWR-unmodulated cells, 0.01 (SEP, Data Analysis),\n    which the paper's own p = 0.01 for inhibited against unmodulated is taken to meet. Reproduced\n    when both modulated groups have a higher fraction than unmodulated at p <= 0.01 and excited\n    and inhibited do not differ at p < 0.01, with fractions judged by the pooled-value rule."
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    groups, but reports p > 0.1 against inhibited; the statement follows the tests. Reproduced\n    when excited against unmodulated is significant at p < 0.01 and the two other comparisons are\n    not.",
 "new_string": "    groups, but reports p > 0.1 against inhibited; the statement follows the tests. Reproduced\n    when excited against unmodulated is significant at p < 0.01 and the two other comparisons are\n    not significant at p < 0.01 (the paper's threshold for these comparisons, SEP Data\n    Analysis)."
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    modulated groups exceed unmodulated at p < 0.01 and excited and inhibited do not differ;\n    means by the pooled-value rule.",
 "new_string": "    modulated groups exceed unmodulated at p < 0.01 and excited and inhibited do not differ at p\n    < 0.01; means by the pooled-value rule."
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    0.01. Reproduced when excited exceeds both other PFC groups at p < 0.01, inhibited and\n    unmodulated do not differ, and CA1",
 "new_string": "    0.01. Reproduced when excited exceeds both other PFC groups at p < 0.01, inhibited and\n    unmodulated do not differ at p < 0.01, and CA1"
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    is below zero at p < 0.01, and unmodulated does not differ from either at p < 0.05.",
 "new_string": "    is below zero at p < 0.01, and unmodulated does not differ from either at p < 0.01 (the\n    paper's threshold for these three-group comparisons, SEP Data Analysis; it reports p > 0.05,\n    and the result at 0.05 is shown as a variant)."
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    pairs on the same tetrode enter is not stated; both are shown. Reproduced when, under one\n    reading, excited-inhibited pairs are lower than each other category at p < 0.001 by rank-sum;\n    pair counts by the pooled-value rule.",
 "new_string": "    pairs on the same tetrode enter is not stated; both are shown. Reproduced when, under one\n    reading, excited-inhibited pairs are lower than each other category at p < 0.01 by rank-sum\n    (the paper's threshold, SEP Data Analysis; it reports p < 0.001); pair counts by the\n    pooled-value rule."
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "  criterion: Pairs of simultaneously recorded CA1 cells and SWR-modulated PFC cells with at least 5\n    SWRs in which both spike; SWR correlation",
 "new_string": "  criterion: Pairs of simultaneously recorded CA1 cells and SWR-modulated PFC cells with at least 5\n    SWRs in which both spike. Which CA1 cells enter is open; readings are (a) the SWR-modulated\n    CA1 cells (the Figure 3F pairs, built from SWR-modulated CA1 and PFC cells, have the same n of\n    393 and 320), (b) all CA1 cells (the Results speak of \"hippocampal and SWR-modulated PFC\n    neurons\"). SWR correlation"
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    test of the regression slope. The group comparison by the shuffle of the SEP (pairs pooled\n    and split at random into groups of the same sizes, 1000 times). Reproduced",
 "new_string": "    test of the regression slope. The group comparison is a 1000-shuffle test (Results); the SEP\n    describes the shuffle only for the spatial correlation comparison (pairs pooled and split at\n    random into groups of the same sizes, 1000 times), and the same procedure is assumed here.\n    Reproduced"
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "  - about: excited against inhibited\n    test: two-way ANOVA\n    p: 0.29\n    n: 40 excited and 37 inhibited cells",
 "new_string": "  - about: excited against inhibited\n    test: two-way ANOVA\n    p: 0.29\n    n: 40 excited and 37 inhibited cells\n  - about: cell count group, in the two-way ANOVA\n    test: two-way ANOVA\n    p: 1.0e-7\n    p_relation: \"<\""
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    size, (b) three groups of equal size width. Reproduced",
 "new_string": "    size, (b) three groups of equal size width, (c) 1, 2-3 and more than 3 cells, the groups\n    printed on the ensemble-size axis of the reverse model in Figure S4C. Reproduced"
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    the behavior bins. Performance and readings as in fig6e-glm-swr-prediction. Reproduced when\n    theta-trained performance is above chance, modulated exceeds unmodulated at p < 0.05, and\n    theta-to-SWR exceeds SWR-to-theta performance.",
 "new_string": "    the behavior bins. Performance and readings as in fig6e-glm-swr-prediction. Reproduced when\n    theta-trained performance is above chance, rises with ensemble size (cell count group, p <\n    0.05), modulated exceeds unmodulated at p < 0.05 (two-way ANOVA), and theta-to-SWR exceeds\n    SWR-to-theta performance, tested as the paper does by the model type by cell count group\n    interaction in a two-way ANOVA at p < 0.05."
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    category as predictors. Reproduced when modulated ensembles predict better than unmodulated at\n    p < 0.05, performance rises with ensemble size, and excited and inhibited do not differ.",
 "new_string": "    category as predictors. Ensemble-size groups are 1, 2-3 and more than 3 PFC cells (Figure S4C\n    axis). Reproduced when modulated ensembles predict better than unmodulated at p < 0.05\n    (two-way ANOVA), performance rises with ensemble size (one-way ANOVA, p < 0.05), and excited\n    and inhibited do not differ at p < 0.05 (two-way ANOVA)."
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    coverage, in both groups (SEP, Figure S5). The legend's",
 "new_string": "    coverage, in both groups (Figure S5 legend). The legend's"
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml",
 "old_string": "    least 10 significant events; R per cell from the correlation of decoded spatial probability\n    and the PFC rate profile on the replayed trajectory (SEP, Replay analysis). How R is formed\n    across events (spike count against overlap, as Figure S6A orders the raster) is open;\n    readings are (a) Pearson of per-event PFC spike count with per-event overlap, (b) Spearman.",
 "new_string": "    least 10 significant events (SEP, Replay analysis). R is the correlation of the decoded\n    spatial probability (summed across the SWR, Figure S6A legend) with the PFC cell's linear\n    rate profile on the replayed trajectory. The SEP calls R a value \"for each neuron\", while\n    Figure S6A gives an R per replay event and Figure S6B plots, per cell, the \"Correlation\n    between R and SWR response\"; the figures are followed: R per event, and per cell the\n    correlation across events of R with the PFC SWR response. Readings for that correlation are\n    (a) Pearson, (b) Spearman; the SWR response window is not given, and 0-200 ms, the paper's\n    SWR response window elsewhere, is the nearest stated choice."
}
```

```
The file claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml has been updated successfully.
```

**Agent**

Now the `checks` entry. Checking the format used in other claims files first.

**Agent calls Bash**

```bash
cd  grep -l "^checks:" claims/*/*.yaml | head -2 | xargs -I{} sh -c 'echo {}; sed -n "/^checks:/,\$p" {} | head -20'
```

```
claims/000005/10.1038-nn.4412.yaml
checks:
- date: 2026-10-20
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - behavior-touches. The criterion stated that the touch and trial counts come from the 111 cortical cells and from principal-whisker touches; the paper says neither. Named both as open, with readings for the recordings and for the whiskers counted.
  - vpm-whisking. Added that the 13.5 spikes/s "after onset of whisker movement" is read as the whisking-epoch rate of Fig. 5d, since the paper defines no spike window after whisking onset.
  - exc-vm-touch-whisking. The criterion gave the Supplementary Fig. 4 windows as the measure of the 1.2 mV whisking change; the paper does not say how it is measured. Named it open, with readings (a) those windows and (b) whisking-epoch minus nonwhisking mean Vm.
  - ion-cut-exc-whisking. Uses both readings of the whisking change, as exc-vm-touch-whisking now does.
  - exc-inhibition-timing. Removed the requirement that the delay be positive in most neurons, which the paper does not state (its Discussion gives a range of -0.8 to 1.6 ms); the range is now reported against that.
  - exc-thalamus-photoinhibition. Removed latency reading (b), a 3 s.d. threshold on Vm that appears nowhere in the paper. The Methods' touch-latency rule is applied to laser onset, and the criterion says this is an assumption.
  - pv-enphr-suppression. Same change for its latencies; the Methods' dPSTH/dt rule is applied to the laser-onset PSTH, as an assumption.
  - ion-cut-exc-no-touch. The post-touch Vm (Vm at the peak of the average PSP) is undefined without a PSP and biased upward on a flat average. The test now uses the paper's touch epoch (4 to 50 ms) against the 0 to 5 ms pre-touch mean, with the peak-based amplitude as a variant.
  - fs-suppress-movement-spiking. The paper does not name the groups of its Kruskal-Wallis test; the criterion now says the test is reported and does not enter the outcome.
  - auc-weak-strong. The cri
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  f=claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml; cat >> $f <<'EOF'
checks:
- date: 2026-11-08
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig3-pfc-swr-modulation-fractions. The 10-point rule for "approximately equal" numbers of excited and inhibited cells is not in the paper; the criterion now says so and gives the paper's own differences.
  - fig3de-ca1-precedes-pfc-peak. The absence of an excited-inhibited difference was judged at p < 0.05; the paper sets 0.01 for comparisons between SWR-excited, SWR-inhibited and SWR-unmodulated cells (SEP, Data Analysis), and a claim of absence is judged at the paper's threshold.
  - fig3e-onset-later-in-pfc. Same change of the absence threshold to 0.01.
  - fig3f-swr-cross-covariance-lag. Named as open the window for the extremum (nearest stated, -200 to +200 ms) and how the 13 +- 7 ms was formed, with two readings (extremum of the mean, mean of per-pair extrema).
  - fig4a-preferred-phases. The preferred phase was the von Mises mean, which the paper does not use for it; Figure 4A defines it as the peak of each cell's phase histogram. The von Mises mean is now a variant, and the 45-degree bin is labelled a standard choice.
  - fig4-swr-modulated-more-theta-locked. The criterion used p < 0.05; the paper's threshold for these three-group comparisons is 0.01, and its own inhibited-unmodulated p = 0.01 is counted significant, so the criterion now uses p <= 0.01 for the differences and p < 0.01 for the absence.
  - fig4-preferred-phase-concentration. Made explicit that the two absent differences are judged at p < 0.01.
  - fig5b-mean-rates. Added the missing threshold (p < 0.01) for the excited-inhibited absence.
  - fig5c-spatial-coverage. Added the missing threshold (p < 0.01) for the inhibited-unmodulated absence.
  - fig5e-speed-correlation. The absence of an unmodulated difference was judged at p < 0.05; changed to the paper's 0.01 for these comparisons, with 0.05 as a variant.
  - fig5g-ensemble-cofiring. The criterion required p < 0.001, the reported level; changed to the paper's threshold of 0.01.
  - fig6-swr-correlated-pairs. Which CA1 cells enter the 713 pairs was not stated; named as open, with readings SWR-modulated CA1 cells (as for Figure 3F, same n) and all CA1 cells.
  - fig6c-theta-predicts-swr-correlation. The SEP describes its mixed-population shuffle only for the spatial correlation comparison; the criterion now says its use here is an assumption.
  - fig6e-glm-swr-prediction. Added the reported main effect of cell count group in the two-way ANOVA (p < 10-7), and a reading (c) for the ensemble-size groups, 1, 2-3 and more than 3 cells, as printed on the Figure S4C axis.
  - fig6e-theta-trained-glm. The criterion omitted the ensemble-size effect and judged the theta-to-SWR against SWR-to-theta comparison by a test the paper does not use; it now requires the cell count effect and uses the paper's model type by cell count interaction in a two-way ANOVA.
  - figs4c-pfc-predicts-ca1. Added the ensemble-size groups printed on the Figure S4C axis (1, 2-3, more than 3 PFC cells) and the tests and thresholds for each part.
  - figs5-matched-selectivity. The coverage-matching rule is from the Figure S5 legend, not the SEP; citation corrected.
  - figs6-replay-content. The criterion took R as a per-cell value correlated with spike counts; Figure S6A gives R per replay event and Figure S6B correlates R with the SWR response per cell. The criterion now follows the figures and names the SEP's conflicting wording.
  - Open. The checker reports three values not found (1e-11, 1e-07 twice); the text prints the exponents with a replacement character ("10?11", "10?7"), and each was confirmed by reading.
  - Open. The PDF could not be rendered in this run either, so the ensemble-size groups of Figure 6E remain unread and stay open with three readings.
  - Open. Whether the paper's 0.01 threshold (SEP, Data Analysis) also covers comparisons that include CA1 or the GLM ANOVAs is not stated; the paper calls p = 0.02 significant for the GLM, so those criteria keep 0.05.
  - Open. Table S1 sums do not agree exactly (Y-track CA1 48 + 113 + 1 = 162, printed 163; intermediate CA1 69 in Table S1, 70 in the SEP); the W-track numbers used as expected values are unaffected.
EOF
python tools/claims_check.py $f paper/10.1016-j.neuron.2016.02.010.txt 2>&1 | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml; sed -i 's/the figures are followed: R per event, and per cell/the figures are followed, with R per event and, per cell,/' $f; grep -n ': .*: ' $f | grep -v '^\s*[0-9]*:\s*- ' | head; python tools/claims_check.py $f paper/10.1016-j.neuron.2016.02.010.txt 2>&1 | tail -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/crcns-hc-28/10.1016-j.neuron.2016.02.010.yaml; sed -i 's/The checker reports three values not found (1e-11, 1e-07 twice)/The checker reports four values not found (1e-11, and 1e-07 in fig3e, fig6e-glm-swr-prediction and fig6e-theta-trained-glm)/' $f; python tools/claims_check.py $f paper/10.1016-j.neuron.2016.02.010.txt 2>&1 | tail -1; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

The claims file is ready for an attempt. I corrected 18 claims and recorded the changes and the open points under `checks`. Nothing is committed or pushed.

**Checker result:** `39 claims, 39 quotes, 62 statistical values, 4 problems`. All 39 quotes match the text word for word. The 4 problems are p-values the checker could not find: 1e-11 (fig3de-ca1-precedes-pfc-peak) and 1e-7 (fig3e-onset-later-in-pfc, fig6e-glm-swr-prediction, fig6e-theta-trained-glm). The text prints these exponents with a replacement character ("10?11", "10?7"). I read each one in place and all four are correct. The 1e-7 in fig6e-glm-swr-prediction is the value I added.

**Changes, by claim:**
- **fig3-pfc-swr-modulation-fractions:** the "within 10 points" rule for "approximately equal" excited and inhibited counts is not in the paper. The criterion now says it is a choice made here.
- **Thresholds for "no difference" and group differences:** the paper sets p < 0.01 for comparisons between SWR-excited, SWR-inhibited and SWR-unmodulated cells (supplemental methods, Data Analysis). The file had used p < 0.05, or no threshold at all. I applied 0.01 in:
  - fig3de-ca1-precedes-pfc-peak and fig3e-onset-later-in-pfc (excited against inhibited)
  - fig4-swr-modulated-more-theta-locked (≤ 0.01, since the paper counts its own p = 0.01 as significant)
  - fig4-preferred-phase-concentration (made explicit)
  - fig5b-mean-rates and fig5c-spatial-coverage (threshold was missing)
  - fig5e-speed-correlation (0.05 kept as a variant)
  - fig5g-ensemble-cofiring (the file required p < 0.001, the reported level, not the threshold)
- **fig3f-swr-cross-covariance-lag:** two details are now named as open. One is the window for the peak or trough. The other is how the "13 ± 7 ms" was formed: the extreme of the mean curve, or the mean of each pair's extreme.
- **fig4a-preferred-phases:** the preferred phase was taken as the von Mises mean, but the Figure 4A legend defines it as the peak of each cell's phase histogram. The von Mises mean is now a variant.
- **fig6-swr-correlated-pairs:** which CA1 cells enter the 713 pairs is now open, with two readings: SWR-modulated CA1 cells only, or all CA1 cells.
- **fig6c-theta-predicts-swr-correlation:** the supplement describes its shuffle test only for spatial correlations. Using it here is now marked as an assumption.
- **fig6e-glm-swr-prediction:** added the reported cell-count effect (p < 10⁻⁷). Added a third reading for the ensemble-size groups (1, 2–3 and more than 3 cells, as on the Figure S4C axis).
- **fig6e-theta-trained-glm:** the criterion now requires that prediction improves with ensemble size. The comparison between the two model types now uses the paper's own test, a two-way ANOVA interaction.
- **figs4c-pfc-predicts-ca1:** added the ensemble-size groups from the Figure S4C axis, and the test and threshold for each part.
- **figs5-matched-selectivity:** the matching rule comes from the Figure S5 legend, not the supplemental methods. Citation corrected.
- **figs6-replay-content:** R is now defined per replay event, and each cell's measure is the correlation of R with its SWR response, as Figures S6A and S6B show. The supplemental methods call R a value per neuron; that conflict is recorded.

**Still open:**
- The PDF could not be rendered here, so the ensemble-size groups of Figure 6E are still unread. Three readings remain.
- The paper does not say whether its 0.01 threshold also covers comparisons with CA1 cells or the GLM ANOVAs. It calls p = 0.02 significant for the GLM, so those criteria keep 0.05.
- Table S1 has small inconsistencies: Y-track CA1 prints 163 where the rows sum to 162, and intermediate CA1 is 69 in Table S1 but 70 in the supplemental methods. The W-track numbers used as expected values are not affected.

Every main finding has a claim, and all claims come from this paper.

## End of run

38 turns, 4 minutes, $1.80 at API prices, result: success.
