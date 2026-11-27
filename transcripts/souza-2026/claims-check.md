# souza-2026 · claims-check · run 44888235458

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i souza; cat claims/souza-2026.yaml; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/ | grep -i 1944695; wc -l claims/souza-2026.yaml paper/10.3389-fnbeh.2026.1944695.txt; python tools/claims_check.py claims/souza-2026.yaml paper/10.3389-fnbeh.2026.1944695.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Let me read the protocol step and the paper.

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
 "file_path": "docs/protocol.md",
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-18`. Record this version in the attempt's provenance.
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
[... 180 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fnbeh.2026.1944695.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.3389-fnbeh.2026.1944695.txt",
 "offset": 1036,
 "limit": 720
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the claims file.

**Agent calls Read**

```json
{
 "file_path": "claims/souza-2026.yaml",
 "limit": 400
}
```

```
1	# Claims for Souza, Vieira, Ventura, de Lima, Arcanjo, de Paula, Sales, Souza, Alvarez-Jacobo,
2	# Fontenele, Aguiar, de Santana, Sousa & de Vasconcelos (2026), "Reward coding across mouse visual
3	# cortical areas", Front. Behav. Neurosci. 20:1944695, doi:10.3389/fnbeh.2026.1944695, on dandiset
4	# 000713 (Allen Institute, Visual Behavior Neuropixels), which the paper reuses.
5	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
6	# protocol as stated in docs/protocol.md (pilot-18).
7	#
8	# Text read. The version of record (Brief Research Report, published 28 October 2026), in
9	# paper/10.3389-fnbeh.2026.1944695.txt: abstract, Introduction, Materials and methods 2.1 to 2.8,
10	# Results 3.1 to 3.4, Discussion, the legends of Figures 1 to 3, and the legend of Supplementary
11	# Figure S1. There is no PDF under paper/, so no figure was opened and no number below is read from a
12	# figure. The display equations are garbled in the text but readable: (1) r_split =
13	# corr(PSTH_odd, PSTH_even); (2) p_split = (1 + sum over b of 1[r_null(b) >= r_split]) / (N_perm + 1);
14	# (3) SI = (A1 - A2) / (|A1| + |A2|); (4) M = (r_post - r_pre) / (r_post + r_pre); (5) n(t) = summed
15	# spike count of the group in [t, t + T), T = 50 ms; (6) CV_i = SD(n) / E(n) over the 50 ms bins of
16	# 10 s window i. The supplement is one figure (Supplementary Figure S1, rank selection for the NMF,
17	# ranks 2 to 8); its image is not under paper/, only its legend. The rank-6 choice is the only result
18	# that rests on it, and no claim below is about rank selection.
19	#
20	# Code. The Data availability statement says "The analysis code is available from the corresponding
[... 380 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/souza-2026.yaml",
 "offset": 400,
 "limit": 380
}
```

```
400	  - quantity: broad cohort units
401	    value: 8716
402	    tolerance: 872
403	  criterion: Each unit's median ISI, then the median over units of each class. The spike span is open;
404	    the readings are (a) the whole recording; (b) the active block (Figure 1O shows ISI separately for
405	    active, replay and peri-reward conditions). Reproduced when the four values are within tolerance
406	    under one reading.
407	- id: fig1gi-waveform-separation
408	  statement: The narrow and broad populations of the cohort separate also in waveform half-width and
409	    in spiking statistics (median ISI, autocorrelogram rise time).
410	  source: Results 3.2, paragraph 3; Figures 1G to 1I
411	  quote: a separation that also held in complementary metrics of waveform shape (half-width) and of
412	    spiking statistics (median inter-spike interval and autocorrelogram rise time; Figures 1G-I, O)
413	  depends_on:
414	  - waveform-ambiguous-band
415	  criterion: The paper reports no test. Half-width as Materials and methods 2.5 defines it (width of
416	    the trough at half its minimum amplitude). Reproduced when narrow cohort units have a lower median
417	    half-width and a lower median ISI than broad units, each by a two-sided Mann-Whitney test at p <
418	    0.05 (a standard test, the paper names none). The autocorrelogram rise time is not defined in the
419	    paper, so it is not judged; the author may show it with a stated definition.
[... 360 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/souza-2026.yaml",
 "offset": 779,
 "limit": 360
}
```

```
779	    value: -0.19
780	    tolerance: 0.019
781	  - quantity: pooled median difference, rate and count matched
782	    value: -0.06
783	    tolerance: 0.006
784	  - quantity: rank-biserial, count matched only, pooled
785	    value: -0.81
786	    tolerance: 0.081
787	  - quantity: rank-biserial, rate and count matched, pooled
788	    value: -0.38
789	    tolerance: 0.038
790	  - quantity: percent of sessions with RW+ below RW-, rate matched
791	    value: 69
792	    tolerance: 6.9
793	    unit: percent
794	  criterion: Rate matching per Materials and methods 2.6, octiles of log10 whole-recording rate over
795	    the union of RW+ and RW-, the same number from each group in every octile (read as the smaller
796	    of the two counts), 20 draws averaged. "Pooled" is read as over all session and area pairs.
797	    Reproduced when, under the fig2c-cv-lower readings, RW+ is lower at p < 0.01 in VISp, VISl, VISal,
798	    VISpm and VISam and the values are within tolerance; partially reproduced when the effect is
[... 338 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "p_relation\|checks\|ready\|changes" tools/claims_check.py | head -40; grep -rn "^checks:" -A12 claims/*.yaml | head -30
```

```
5:Validates the file against schemas/claims.schema.json, checks every quote word for word
claims/alasfour-2024.yaml:645:checks:
claims/alasfour-2024.yaml-646-- date: 2026-11-10
claims/alasfour-2024.yaml-647-  kind: agent
claims/alasfour-2024.yaml-648-  model: claude-opus-5-5
claims/alasfour-2024.yaml-649-  ready: true
claims/alasfour-2024.yaml-650-  changes:
claims/alasfour-2024.yaml-651-  - fig2-rois-three-bands, fig2-inferior-temporal-all-bands, fig2-beta-temporal-only, fig2-single-band-rois. Removed the statistics entries (t-test against finite chance, BH FDR at 0.01); the threshold marks which features count as above chance (Figure 2 legend), a method and not a result. The criteria keep it through M6.
claims/alasfour-2024.yaml-652-  - fig5-gamma-higher-talking, fig5-theta-alpha-lower-talking, fig5-pre-postcentral. Removed the statistics entries (t-test of the mean difference against zero, BH FDR at 0.01); the threshold selects the consistent features whose signs are counted (Figure 5 legend), a method and not a result. The criteria keep it through M8.
claims/alasfour-2024.yaml-653-  - table1-participants. Removed the rule that 13 of the 15 minute values suffice; the paper gives no such threshold, so every value must now be within tolerance.
claims/alasfour-2024.yaml-654-  - fig6-sign-consistency. The tolerance of 0.9 allowed only 9 while the criterion accepted 8 to 10. Set the tolerance to 1 (10% of 9 rounded to a whole combination) and gave the reason.
claims/alasfour-2024.yaml-655-  - Header O4. The SD of the channel was fixed as the whole recording, called a standard choice; it can change which blocks are dropped, so the readings (whole recording, the day's recording) are now named.
claims/alasfour-2024.yaml-656-  - Header O10, anova-roi-band-effects, anova-no-interaction. The ANOVA's observations are not given (Methods 2.2); named fold accuracies and participant means as readings. The absence claim is judged on fold accuracies with type II sums of squares, m
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "p_relation" -A3 schemas/claims.schema.json | head
```

```
304:          "description": "The reported p-value as printed, or its bound when the paper gives one ('p < 0.05' is p 0.05 with p_relation '<'). A paper that prints 'P = 0' (below the precision it reports) is recorded as 0.",
305-          "type": "number",
306-          "minimum": 0,
307-          "maximum": 1
--
309:        "p_relation": {
310-          "description": "How p was reported: exactly (the default) or as a bound.",
311-          "enum": [
312-            "=",
```

**Agent calls Bash**

```bash
cd  sed -n 309,320p schemas/claims.schema.json
```

```
"p_relation": {
          "description": "How p was reported: exactly (the default) or as a bound.",
          "enum": [
            "=",
            "<",
            ">"
          ]
        },
        "corrected": {
          "description": "The correction for multiple comparisons the paper applied, e.g. 'Bonferroni', 'FDR'.",
          "type": "string"
        },
```

**Agent**

The checker reports no problems. My review found several issues, and I'm now fixing them in the file.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/souza-2026.yaml",
 "old_string": "  criterion: Per area, the distribution of observed r_split of cohort units against the pooled null\n    r_split values of the same units. Reproduced when in every area the cohort median r_split exceeds\n    the 95th percentile of the null distribution.",
 "new_string": "  criterion: Per area, the distribution of observed r_split of cohort units against the pooled null\n    r_split values of the same units (Figure 1D legend). The paper gives no measure of \"well above\"\n    or \"exceeds\", so the comparison is open; the readings are (a) the cohort median r_split exceeds\n    the 95th percentile of the pooled null; (b) every cohort unit's r_split exceeds the median of its\n    own null. Reproduced when, in every area, the result holds under one reading; the outcome rests\n    on that reading as an assumption."
}
```

```
The file claims/souza-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/souza-2026.yaml",
 "old_string": "  criterion: Mixture as in Materials and methods 2.5, two components, full covariance, eight\n    initialisations, on trough-to-peak duration of all visual-area units (53,806, units with a\n    waveform); the shorter-mean component is narrow.",
 "new_string": "  criterion: Mixture as in Materials and methods 2.5, two components, full covariance, eight\n    initialisations, on trough-to-peak duration of all visual-area units; the shorter-mean component\n    is narrow. The paper does not say why 53,806 of the 54,039 units enter; the reading is units with\n    a usable mean waveform, an assumption."
}
```

```
The file claims/souza-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/souza-2026.yaml",
 "old_string": "  criterion: Each unit's median ISI, then the median over units of each class. The spike span is open;\n    the readings are (a) the whole recording; (b) the active block (Figure 1O shows ISI separately for\n    active, replay and peri-reward conditions). Reproduced when the four values are within tolerance\n    under one reading.",
 "new_string": "  criterion: Each unit's median ISI, then the median over units of each class. The spike span is open;\n    the readings are (a) the whole recording; (b) the active block (Figure 1O shows ISI separately for\n    active, replay and peri-reward conditions). The class counts are also open. 2,308 plus 8,716 is\n    11,024, more than the 10,805 cohort units left after the 227 ambiguous ones (Materials and methods\n    2.5) are removed. The readings are (a) ambiguous units excluded; (b) every unit given the class of\n    its larger posterior, with no ambiguous band. Reproduced when the four values are within tolerance\n    under one combination of readings."
}
```

```
The file claims/souza-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/souza-2026.yaml",
 "old_string": "  criterion: The paper reports no test. Half-width as Materials and methods 2.5 defines it (width of\n    the trough at half its minimum amplitude). Reproduced when narrow cohort units have a lower median\n    half-width and a lower median ISI than broad units, each by a two-sided Mann-Whitney test at p <\n    0.05 (a standard test, the paper names none).",
 "new_string": "  criterion: The paper reports no test. Half-width as Materials and methods 2.5 defines it (width of\n    the trough at half its minimum amplitude). Reproduced when narrow cohort units have a lower median\n    half-width and a lower median ISI than broad units. A two-sided Mann-Whitney test is shown as a\n    variant only; the paper names none, so it does not decide the outcome."
}
```

```
The file claims/souza-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/souza-2026.yaml",
 "old_string": "  criterion: The paper reports no test of M between classes. Reproduced when the median M of narrow\n    cohort units is below that of broad units and a two-sided Mann-Whitney test (a standard test, the\n    paper names none) gives p < 0.05; partially reproduced when the medians are ordered but the test\n    fails.",
 "new_string": "  criterion: The paper reports no test of M between classes. Reproduced when the median M of narrow\n    cohort units is below that of broad units. A two-sided Mann-Whitney test is shown as a variant\n    only; the paper names none, so it does not decide the outcome."
}
```

```
The file claims/souza-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/souza-2026.yaml",
 "old_string": "  source: Materials and methods 2.5, paragraph 5; Discussion, paragraph 2",
 "new_string": "  source: Materials and methods 2.5, paragraph 4 (beginning \"The pre-reward baseline is deliberately\n    adjacent\"); Discussion, paragraph 2"
}
```

```
The file claims/souza-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/souza-2026.yaml",
 "old_string": "    readings are (a) all other layers pooled; (b) the mean of the supragranular and infragranular\n    fractions. The paper also prints the unmatched excess as +0.148 (claim layer4-controls), which may\n    be a different session set or statistic; a median within tolerance of either +0.116 or +0.148\n    counts. Reproduced",
 "new_string": "    readings are (a) all other layers pooled; (b) the mean of the supragranular and infragranular\n    fractions. The paper also prints an unmatched excess of +0.148 in the rate-matching control\n    (claim layer4-controls); it is judged there, and this claim is judged on +0.116. Reproduced"
}
```

```
The file claims/souza-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/souza-2026.yaml",
 "old_string": "  - quantity: layer 4 excess, rate matched\n    value: 0.178\n    tolerance: 0.0178",
 "new_string": "  - quantity: layer 4 excess, rate matched\n    value: 0.178\n    tolerance: 0.0178\n  - quantity: layer 4 excess, unmatched, in the rate-matching comparison\n    value: 0.148\n    tolerance: 0.0148"
}
```

```
The file claims/souza-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/souza-2026.yaml",
 "old_string": "    testable in both contrasts (claim fig1e-cohort-size). Reproduced when the values are within",
 "new_string": "    testable in both contrasts (claim fig1e-cohort-size). The unmatched +0.148 differs from the\n    +0.116 of layer4-suppression; the paper does not say why, and the readings are (a) the sessions\n    where rate matching is possible; (b) a mean in place of a median. Reproduced when the values are within"
}
```

```
The file claims/souza-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/souza-2026.yaml",
 "old_string": "  - about: each of the 66 pairwise CV(t) correlations\n    test: Pearson correlation, against circular-shift and block-permutation nulls",
 "new_string": "  - about: each of the 66 pairwise CV(t) correlations; p is the largest FDR-corrected p of the 66\n    test: Pearson correlation, against circular-shift and block-permutation nulls"
}
```

```
The file claims/souza-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/souza-2026.yaml",
 "old_string": "RW- pairs is open; both are run. The FDR p values are taken from the null permutations (a\n    standard choice). Reproduced",
 "new_string": "RW- pairs is open; both are run. The source of the FDR p values is not given. With 1,000\n    permutations a permutation p cannot fall below about 1e-3, so the largest p_FDR of 1.0e-12 can\n    only come from the parametric test of each Pearson r; that is the reading, BH over the 66 pairs\n    (Materials and methods 2.8), and the nulls give the z values. Reproduced"
}
```

```
The file claims/souza-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/souza-2026.yaml",
 "old_string": "  - quantity: sessions with false alarms\n    value: 102",
 "new_string": "  - quantity: sessions covered by the hits against false alarms family\n    value: 102"
}
```

```
The file claims/souza-2026.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  sed -i 's/  - quantity: percent of cohort with a layer, VISam$/  - quantity: percent with a layer, VISam (cohort or all units, see criterion)/; s/  - quantity: percent of cohort with a layer, VISrl$/  - quantity: percent with a layer, VISrl (cohort or all units, see criterion)/' claims/souza-2026.yaml; grep -n "with a layer, VIS" claims/souza-2026.yaml; tail -c 200 claims/souza-2026.yaml | od -c | tail -2
```

```
559:  - quantity: percent with a layer, VISam (cohort or all units, see criterion)
563:  - quantity: percent with a layer, VISrl (cohort or all units, see criterion)
0000300   9   7   .   7   %   )   .  \n
0000310
```

**Agent calls Bash**

```bash
cd  cat >> claims/souza-2026.yaml <<'EOF'
checks:
- date: 2026-11-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - fig1d-split-half-above-null. The criterion fixed "cohort median above the 95th percentile of the null" as if from the paper; the paper gives no measure of "well above" (Results 3.1, Figure 1D legend). It is now named as open, with two readings, and the outcome marked as resting on the one used.
  - fig1gi-waveform-separation, fig1m-narrow-stronger-m. A Mann-Whitney test at p < 0.05, which the paper does not report or name, decided the outcome. The claims are now judged on the ordering of medians the paper states, and the test is shown as a variant.
  - fig1h-median-isi-narrow-broad. The legend's n (2,308 plus 8,716, or 11,024) does not fit the 10,805 cohort units left after the 227 ambiguous ones (Materials and methods 2.5). Named the class counts as open, with readings (ambiguous excluded; class by the larger posterior).
  - waveform-ambiguous-band. The criterion said the 53,806 units are those with a waveform; the paper does not say so. Now stated as an assumption.
  - layer4-suppression, layer4-controls. The criterion let a median within tolerance of +0.148 pass for the +0.116 the paper reports for this test; +0.148 is the unmatched excess of the rate-matching control (Results 3.2, paragraph 4). The claim is now judged on +0.116, and +0.148 is an expected value of layer4-controls, with the paper's unexplained gap between the two named as open.
  - m-baseline-sensitivity. Source cited Materials and methods 2.5 paragraph 5, while fig1mn-modulation-index-negative cites paragraph 4 for the same sentence; now paragraph 4 with its first words.
  - fig2d-cv-correlations. The criterion took the FDR p values from the 1,000-permutation nulls, which cannot give the largest p_FDR of 1.0e-12 the Figure 2D legend reports; now read as parametric Pearson p values with BH over the 66 pairs. The statistics entry says p is the largest of the 66.
  - layer-assignment-coverage. The VISam and VISrl expected values were labeled as cohort percentages while the criterion names cohort or all units as open; labels now match the criterion.
  - hits-vs-false-alarms. The 102 was labeled sessions with false alarms; the paper says sessions covered by this family (Discussion, paragraph 6). Relabeled.
  - Open, not settled. Paragraph numbers in Materials and methods 2.5 and Results 3.2 cannot be checked against the layout, as the text extraction loses paragraph breaks and there is no PDF; the quotes locate each finding.
  - Open, not settled. The rate matching across layers (layer4-controls) and the pre and post windows of Figure 2F (fig2f-pre-postcv) are not described in the paper; the readings in those criteria are the file's, taken from the closest Methods passages.
EOF
sed -i 's/fig2f-pre-postcv/fig2f-pre-post-cv/' claims/souza-2026.yaml
python tools/claims_check.py claims/souza-2026.yaml paper/10.3389-fnbeh.2026.1944695.txt; grep -c "—\|rather" claims/souza-2026.yaml; grep -n "—\|rather" claims/souza-2026.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n '/^checks:/,$p' claims/souza-2026.yaml | grep -n ": " | grep -v "^\s*[0-9]*:\s*-\? *\(date\|kind\|model\|ready\|changes\):" ; git diff --stat
```

```
claims/souza-2026.yaml | 74 +++++++++++++++++++++++++++++++++++---------------
 1 file changed, 52 insertions(+), 22 deletions(-)
```

**Agent**

I've reviewed `claims/souza-2026.yaml`, fixed what I could show was wrong from the paper, and added a check entry with `ready: true`. Nothing is committed.

**Checker:** `claims/souza-2026.yaml: 38 claims, 38 quotes, 13 statistical values, 0 problems`. I ran it before and after my edits and got the same line both times.

**Changes, by claim**
- **fig1d-split-half-above-null:** the rule "cohort median above the null's 95th percentile" was not from the paper. The paper gives no measure for "well above", so the criterion now names this as open, with two readings, and marks the outcome as resting on the one used.
- **fig1gi-waveform-separation, fig1m-narrow-stronger-m:** a Mann-Whitney test the paper never reports was deciding the outcome. Both claims are now judged on the ordering of medians, which is what the paper states, and the test is kept only as a variant.
- **fig1h-median-isi-narrow-broad:** the legend's counts (2,308 + 8,716 = 11,024) don't fit the 10,805 cohort units left once the 227 ambiguous ones are removed. I named the class counts as open, with two readings.
- **waveform-ambiguous-band:** the file said the 53,806 units are "units with a waveform". The paper doesn't say why only 53,806 enter, so this is now stated as an assumption.
- **layer4-suppression:** the criterion also accepted +0.148 in place of the reported +0.116. It is now judged on +0.116 only.
- **layer4-controls:** +0.148, which is the unmatched figure in the firing-rate-matching control, is now an expected value here. The paper leaves the gap between +0.148 and +0.116 unexplained, and the criterion names that as open.
- **m-baseline-sensitivity:** its source paragraph number disagreed with fig1mn's for the same sentence. I corrected it and added the paragraph's opening words so it can be found.
- **fig2d-cv-correlations:** the criterion took the false-discovery-rate p values from 1,000 permutations, which can't go below about 1e-3, so they can't produce the reported 1.0e-12. They are now read as parametric Pearson p values, corrected across the 66 pairs.
- **layer-assignment-coverage:** the VISam and VISrl expected values were labelled as cohort percentages, but the criterion says cohort or all units is open. The labels now match the criterion.
- **hits-vs-false-alarms:** "102 sessions with false alarms" is now "102 sessions covered by this family", as the paper says.

**What remains open**
- Paragraph numbers in Methods 2.5 and Results 3.2 can't be confirmed, because the text extraction loses paragraph breaks and there is no PDF. The quotes still locate each finding.
- The paper doesn't describe two methods: the firing-rate matching across layers, and the pre- and post-stimulus windows of Figure 2F. The readings in those criteria are the file's own, taken from the nearest Methods passages.
- No analysis code is available (the paper offers it "upon reasonable request"), so none of these open details can be settled from code.

**Coverage:** every main finding in the abstract and Results has a claim. Every claim comes from this paper.

**Ready:** yes. The file is fit for an attempt.

## End of run

28 turns, 3 minutes, $1.30 at API prices, result: success.
