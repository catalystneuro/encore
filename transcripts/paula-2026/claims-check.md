# paula-2026 · claims-check · run 45977063103

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls paper/; cat claims/paula-2026.yaml; python tools/claims_check.py claims/paula-2026.yaml paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat -n claims/paula-2026.yaml; python tools/claims_check.py claims/paula-2026.yaml paper/10.1103-wndc-k654.txt; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The file is large; I'll read it in pieces.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/495ab7a2-8098-4b93-be76-eb669b54c67f/tool-results/b52egj5un.txt"
}
```

```
1	     1	# Claims for de Paula, Jungmann, Fontenele, Aguiar, Carelli, Matias, Copelli & de Vasconcelos
2	     2	# (2026), "Revealing Stimulus-Dependent Dynamics Through Statistical Complexity", PRX Life 4,
3	     3	# 023018, doi:10.1103/wndc-k654, tested on DANDI:000713.
4	     4	#
5	     5	# Provenance: written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub
6	     6	# Actions"), 2026-11-27, protocol pilot-18 as stated in docs/protocol.md.
7	     7	#
8	     8	# Text read: the version of record (published 22 May 2026, corrected 22 July 2026, the
9	     9	# correction fixing Eq. 9), from paper/10.1103-wndc-k654.txt, which holds the main text
10	    10	# (Methods, Results, figure legends, Table I) and the Supplemental Material (Secs. I to III,
11	    11	# supplementary Figs. 1 to 6, dated April 28, 2026). The PDF pages could not be rendered in
12	    12	# this run, so no figure was read from its image; every value below is from the text and the
13	    13	# legends. The paper links no analysis code: its Data Availability statement cites only the
14	    14	# dataset, and the one URL of the supplement (https://bit.ly/4smMnMj) holds the figures of the
15	    15	# parameter sweep. No code was read.
16	    16	#
17	    17	# Data the paper used (Methods II.A, Results III.A, Table I, legends of Figs. 1 to 5). The
18	    18	# Allen Institute Visual Behavior Neuropixels dataset, cited as DANDI:000713 version
19	    19	# 0.240702.1725 (Ref. 22). Wild-type and transgenic mice, head fixed, recorded with six
20	    20	# Neuropixels 1.0 probes targeting visual cortex. 102 sessions. Measured variables used:
[... 821 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/495ab7a2-8098-4b93-be76-eb669b54c67f/tool-results/b52egj5un.txt",
 "offset": 842
}
```

```
842	   842	    0.15–0.21) with modest conditiondependence ... Intriguingly, these regions exhibited peak
843	   843	    complexity during spontaneous activity, opposite to the pattern observed in visual cortex.
844	   844	    In contrast, CA1, POST, ProS, and SUB maintained more stable, lower complexity values
845	   845	    (0.11–0.15) across states'
846	   846	  expected:
847	   847	  - quantity: DG median C, low end
848	   848	    value: 0.19
849	   849	    tolerance: 0.019
850	   850	  - quantity: DG median C, high end
851	   851	    value: 0.27
852	   852	    tolerance: 0.027
853	   853	  - quantity: CA3 median C, low end
854	   854	    value: 0.15
855	   855	    tolerance: 0.015
856	   856	  - quantity: CA3 median C, high end
857	   857	    value: 0.21
858	   858	    tolerance: 0.021
859	   859	  - quantity: CA1, POST, ProS and SUB median C, low end
860	   860	    value: 0.11
861	   861	    tolerance: 0.011
[... 246 more lines not kept]
```

**Agent**

Checker: 38 claims, 0 problems. Now the paper.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1103-wndc-k654.txt",
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1103-wndc-k654.txt",
 "offset": 700,
 "limit": 500
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1103-wndc-k654.txt",
 "offset": 1200,
 "limit": 481
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && (which pdftoppm mutool; python -c "import fitz; print(fitz.__doc__)") 2>&1 | head
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz; print(fitz.__doc__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1103-wndc-k654.pdf",
 "pages": "6"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I can't render the PDF either. Now the edits.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/paula-2026.yaml",
 "old_string": "    all twelve medians are within tolerance; partially reproduced when the order (active and\n    blank above natural images above spontaneous, per area) holds but some values miss.",
 "new_string": "    all twelve medians are within tolerance; partially reproduced when the order the paper's\n    own values show holds (per area, active above natural images, natural images above\n    spontaneous, blanks above spontaneous) but some values miss. Blanks against natural images\n    is not part of the order, since the paper's VISl values are equal (0.46) and its VISal\n    natural-image median (0.48) exceeds the blank one (0.46)."
}
```

```
The file claims/paula-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/paula-2026.yaml",
 "old_string": "    of Fig. 3a, the series lengths and the transients dropped are not given in the text (the\n    figure, which could not be read here, shows the parameters); the series length is 10^5\n    points with the first 10^3 dropped, a standard choice, and parameters span the ranges the\n    supplement names (logistic r in [3.5, 4], tent mu in (1, 2]). Reproduced when the\n    positions fall in the ranges quoted, widened by 10% of each bound.",
 "new_string": "    of Fig. 3a, the series lengths and the transients dropped are not given in the text (the\n    figure, which could not be read here, shows the parameters); the series length is 10^5\n    points with the first 10^3 dropped, a standard choice. The supplement gives the tent map\n    slope as mu in (0, 2] and the Ikeda p in [5, 17]; it gives no range for the logistic r or\n    for alpha and k, so these are open, read as logistic r in [3.5, 4], tent mu in (1, 2]\n    (the chaotic part of the stated range, the one the statement concerns), alpha in [0.01,\n    1] and k in [0, 3]. Reproduced when the positions fall in the ranges quoted, widened by\n    10% of each bound."
}
```

```
The file claims/paula-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/paula-2026.yaml",
 "old_string": "    run. Reproduced when every subregion ratio lies inside its area's range widened by 10% of\n    each bound and the Mann-Whitney test gives p < 0.001 with empirical higher in every\n    region under one reading.",
 "new_string": "    run. Reproduced when every subregion ratio lies inside its area's range widened by 10% of\n    each bound, the VIS subregion surrogate medians lie in 0.189 to 0.264 (0.21 to 0.24\n    widened likewise), and the Mann-Whitney test gives p < 0.001 with empirical higher in\n    every region under one reading."
}
```

```
The file claims/paula-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/paula-2026.yaml",
 "old_string": "    (at least two of three) are at most 4.4% (4% widened by 10%). This statement conflicts\n    with the ~30% separation of natural images from active and blank in the same paragraph\n    (fig2b-vis-summed-js-cv); both are tested as written, and the conflict is noted.",
 "new_string": "    (at least two of three) are at most 4.4% (4% widened by 10%). This statement conflicts\n    with the ~30% separation of natural images from active and blank in the same paragraph\n    (fig2b-vis-summed-js-cv); both are tested as written, and the conflict is noted. The\n    Fig. 2b legend states the same finding as JS values, not percentages (\"typically\n    <0.20\"); as a second reading, most JS values among visual subregions in each of the\n    three visually driven conditions are at most 0.22, and both readings are reported."
}
```

```
The file claims/paula-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/paula-2026.yaml",
 "old_string": "    ProS and SUB 0.1–0.13. Readings of the ranges",
 "new_string": "    ProS and SUB 0.1–0.13; the legend thus groups CA1 with DG and CA3, as does the summary\n    of Results III.D (\"some subfields (DG, CA3, CA1) maintaining high complexity that peaks\n    during spontaneous activity\"), while the text range puts CA1 with POST, ProS and SUB.\n    Readings of the ranges"
}
```

```
The file claims/paula-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/paula-2026.yaml",
 "old_string": "    reading, in all four conditions the MB bin means lie in 0.09 to 0.143 and the MB\n    least-squares slope of C on CV is the smallest in absolute value of the four areas.",
 "new_string": "    reading, in all four conditions the MB bin means lie in 0.09 to 0.143 and the MB\n    least-squares slope of C on CV is the smallest in absolute value of the four areas. The\n    Fig. 5 legend gives MB in natural images as C 0.10 to 0.15; bin means up to 0.165 in\n    that condition meet the legend's reading and are reported as such."
}
```

```
The file claims/paula-2026.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
grep -n "^checks\|^[a-z_]*:" claims/paula-2026.yaml; tail -5 claims/paula-2026.yaml; grep -rn "checks:" claims/*.yaml | head -3
```

```
82:schema_version: 2
83:paper: doi:10.1103/wndc-k654
84:claims:
    opening comment); (b) the overlap of the interquartile ranges of the two distributions.
    Reproduced when, under one reading, in most visual subregions complexity separates the
    two conditions (larger JS, or IQRs that do not overlap) while CV and mean correlation do
    not (smaller JS than complexity, or overlapping IQRs). The comparison is reported for
    every subregion.'
claims/alasfour-2024.yaml:645:checks:
claims/andrews-2024.yaml:850:checks:
claims/armstrong-2026.yaml:843:checks:
```

**Agent calls Bash**

```bash
sed -n '645,670p' claims/alasfour-2024.yaml
```

```
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
  - fig7-exceeds-group. The comparison of Figure 7 with Figure 2 was fixed one way; the paper does not say which values are compared. Added a 
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> claims/paula-2026.yaml <<'EOF'
checks:
- date: 2026-11-27
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig2a-vis-cv-by-condition. The partial rule asked for blanks above natural images, which the paper's own medians contradict (VISl 0.46 and 0.46, VISal 0.48 natural images against 0.46 blanks); the order now holds only the relations the paper's values show.
  - fig3a-reference-systems. The criterion gave the supplement's tent map range as mu in (1, 2]; Supplemental Sec. I.D gives (0, 2]. It also gave logistic r in [3.5, 4] as the supplement's, which names no range. Both are now stated as the supplement gives them, with the chaotic ranges and alpha and k ranges named as open readings.
  - fig1c-cv-above-surrogate. The expected VIS surrogate medians (0.21 to 0.24) were not used by the criterion; they are now part of the rule.
  - fig2b-visually-driven-js-cv-low. Added the Fig. 2b legend's form of the same finding (JS values typically below 0.20) as a second reading next to the text's percentage form.
  - fig4c-dg-ca3-complexity. Noted that the legend and the Results III.D summary group CA1 with DG and CA3, while the text range groups it with POST, ProS and SUB.
  - fig5-mb-flat. Noted the Fig. 5 legend's midbrain range in natural images (C 0.10 to 0.15), wider than the text's 0.10 to 0.13.
  - Open. The PDF could not be rendered in this check either, so the figures (Fig. 3a parameters, boxplots, matrices, C-CV trajectories) were not read; claims rest on text and legends.
  - Open. Unit selection reading (b) cites Allen default quality filters (ISI violations below 0.5, amplitude cutoff below 0.1, presence ratio above 0.9); these are not from the paper and the exact defaults for DANDI:000713 were not verified here. Table I counts are meant to decide between readings.
  - Open. Several criteria use this file's own operational bounds where the paper gives none (surrogate correlations below 0.2 in fig1d, midbrain medians varying by less than 0.02 in supp-fig6, "most" as more than half); each says so.
  - Open. The paper's text and legends conflict in several places (thalamic and hippocampal complexity ranges in Fig. 4, DG and CA3 JS values in Fig. 2b, VIS ~30% against <4%); the claims test both where they conflict, and the paper does not settle which is right.
EOF
python tools/claims_check.py claims/paula-2026.yaml paper/10.1103-wndc-k654.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked `claims/paula-2026.yaml` against the paper and its supplement. The file is ready for an attempt (`ready: true`). I made six corrections, and four questions remain open.

**Checker result** (before and after my edits): `claims/paula-2026.yaml: 38 claims, 37 quotes, 7 statistical values, 0 problems`

**Changes, by claim**
- **fig2a-vis-cv-by-condition**: The rule for "partially reproduced" required blank-screen CV above natural-image CV. The paper's own medians contradict that: VISl is 0.46 in both, and VISal is 0.48 for natural images against 0.46 for blanks. The rule now keeps only the orderings the paper's numbers show.
- **fig3a-reference-systems**: The criterion misquoted the supplement. The supplement gives the tent map slope as (0, 2], not (1, 2]. It gives no range at all for the logistic map's r, for alpha or for k. Those three are now marked as open, each with a stated reading.
- **fig1c-cv-above-surrogate**: The paper's surrogate medians for visual cortex (0.21 to 0.24) were listed as expected values but never used in the criterion. They are now part of the test.
- **fig2b-visually-driven-js-cv-low**: The Fig. 2b legend states this finding as JS values (typically below 0.20), while the text gives percentages (below 4%). The legend's version is added as a second reading.
- **fig4c-dg-ca3-complexity**: The criterion now notes a conflict over CA1. The Fig. 4 legend and the Results III.D summary group it with DG and CA3, while the text's ranges group it with POST, ProS and SUB.
- **fig5-mb-flat**: The Fig. 5 legend gives a wider midbrain range for natural images (0.10 to 0.15) than the text (0.10 to 0.13). The criterion now notes this.

**Still open**
- I could not render the PDF either, so no figure images were read, including the Fig. 3a parameter values. Every claim rests on the text and the legends.
- One way of selecting units uses the Allen Institute's default quality filters. These do not come from the paper, and I did not confirm the exact defaults for this dataset. The paper's Table I neuron counts are meant to decide between this reading and using all units.
- Some criteria use cut-offs the file sets itself where the paper gives none, for example surrogate correlations below 0.2, and "most" taken as more than half. Each criterion says so.
- In several places the text and the legends disagree, and the paper does not say which is right. The claims test both versions.

I found no main finding without a claim, and every claim comes from this paper. Nothing was committed or pushed.

## End of run

19 turns, 2 minutes, $1.13 at API prices, result: success.
