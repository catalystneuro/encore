# komori-2026 · claims-check · run 45589553579

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls paper/ | grep -i komori; cat claims/komori-2026.yaml; sed -n '/Reader/,/^## /p' docs/protocol.md | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/99e9d45a-2372-4b2a-b745-3ab1e641f093/tool-results/b6di7c5nx.txt"
}
```

```
1	# Claims for Komori, Mizusaki, Tomita, Yoneda, Matoba & Morita (2026), "Mesoscopic cortical
2	# activities associated with pupil-linked perceptions inferred via explainable machine learning",
3	# tested on DANDI:001425.
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-25,
5	# following docs/protocol.md (pilot-18), Reader, steps 1 to 4.
6	#
7	# Text read: the bioRxiv preprint (doi:10.64898/2026.05.27.726399, the version posted June 1,
8	# 2026), as stored in paper/10.64898-2026.05.27.726399.txt. It holds the main text, the Methods,
9	# the legends of Figures 1 to 4 and of Supplementary Figures 1 to 12, and the Data and Code
10	# Availability statements. Supplementary Figures 3, 4, 5 and 6 were read from the images beside
11	# the text (supp-fig-S3 to S6.jpg); the numbers taken from them are marked as read from a figure.
12	# No other figure was seen. No separate supplementary text exists ("Supplementary Fig. 1 to 12").
13	#
14	# Code read: https://github.com/moritalabC201/WF_deep-learning at commit 405a720 (2026-01-22),
15	# the repository the Code Availability names. It holds template notebooks with placeholder paths
16	# for atlas registration, hemodynamic correction, SVD (400 components, fitted on every fifth
17	# session, ca_list[i][::5]) and JADE ICA (top 200 SVD components, ICs kept by hand), pupil
18	# diameter from DeepLabCut, data set construction, GRU training (32 units, sigmoid output,
19	# Adam, binary cross-entropy with label smoothing 0.001, batch 256), ROC and Youden threshold,
20	# Deep SHAP, VIF (statsmodels), permutation importance (3 repeats) and the paired t-tests of
[... 623 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md; ls paper/ | head; python tools/claims_check.py claims/komori-2026.yaml paper/10.64898-2026.05.27.726399.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/datasets/komori-2026.yaml; wc -l paper/*.txt; cat paper/10.64898-2026.05.27.726399.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.05.27.726399.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.05.27.726399.txt",
 "offset": 975,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.05.27.726399.txt",
 "offset": 1675,
 "limit": 460
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.05.27.726399.supp-fig-S5.jpg"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.05.27.726399.supp-fig-S6.jpg"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -l "relation: reuses" papers/datasets/*.yaml | head -5; grep -h "^  data:" claims/*.yaml | sort | uniq -c; sed -n '1,80p' tools/claims_check.py | grep -n -i "data\|checks" | head -30
```

```
papers/datasets/alasfour-2024.yaml
papers/datasets/burman-2023.yaml
papers/datasets/cambrainha-2025.yaml
papers/datasets/clark-2026.yaml
papers/datasets/du-2026.yaml
    288   data: dataset
    707   data: elsewhere
    446   data: with_inputs
    394   data: with_labels
5:Validates the file against schemas/claims.schema.json, checks every quote word for word
18:import unicodedata
35:    s = unicodedata.normalize("NFKC", html.unescape(s))
```

**Agent calls Bash**

```bash
grep -n -A12 '"data"' schemas/claims.schema.json | head -40; grep -n -B2 -A3 "data: elsewhere" claims/cambrainha-2025.yaml claims/du-2026.yaml 2>/dev/null | head -30; grep -n -A12 "^checks" claims/du-2026.yaml | head -30
```

```
138:          "data": {
139-            "description": "What the claim's test uses: the dataset alone (`dataset`, the default); the dataset with names for its own codes taken from elsewhere (`with_labels`), which counts as the dataset; the dataset with other data from elsewhere (`with_inputs`), which is counted apart; or data the paper deposited in another public archive, which the dataset does not hold (`elsewhere`), counted apart from both. Outside sources that a test uses are listed under `inputs` in the attempt.",
140-            "enum": [
141-              "dataset",
142-              "with_labels",
143-              "with_inputs",
144-              "elsewhere"
145-            ]
146-          },
147-          "where": {
148-            "description": "For a claim with data `elsewhere`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
149-            "type": "string",
150-            "minLength": 1
--
192:                "data": {
193-                  "const": "elsewhere"
194-                }
195-              },
196-              "required": [
197:                "data"
[... 55 more lines not kept]
```

**Agent**

Checker passes (23 claims, 0 problems). Now checking the remaining figure image (S4) before editing.

**Agent calls Read**

```json
{
 "file_path": "paper/10.64898-2026.05.27.726399.supp-fig-S4.jpg"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims && python - <<'EOF'
import re
p='komori-2026.yaml'
s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1, old
    s=s.replace(old,new)
rep("""#     F405, subtraction) is described for its own data; the Resting state Methods say only that
#     images were down-sampled and masked, so the paper applied its pipeline to the raw frames.""",
"""#     F405, subtraction) is described for its own data; the Resting state Methods say only that
#     images were down-sampled and masked, which suggests, without stating, that the paper applied
#     its pipeline to the raw frames.""")
rep("""    chance from cortical activity
    low-pass filtered at 2 Hz (the setting that works for sensory-evoked dilation); a 0.1 Hz
    low-pass filter was required for significant decoding.""","""""")
EOF
grep -n "statement: Spontaneous" -A3 komori-2026.yaml
```

```
Traceback (most recent call last):
  File "<stdin>", line 13, in <module>
  File "<stdin>", line 6, in rep
AssertionError:     chance from cortical activity
    low-pass filtered at 2 Hz (the setting that works for sensory-evoked dilation); a 0.1 Hz
    low-pass filter was required for significant decoding.
173:  statement: Spontaneous pupil dilation could not be predicted above chance from cortical activity
174-    low-pass filtered at 2 Hz (the setting that works for sensory-evoked dilation); a 0.1 Hz
175-    low-pass filter was required for significant decoding.
176-  source: Discussion, Spontaneous Pupil Dilation, paragraph 1; Supplementary Figure 5E
```

**Agent**

I'll make the edits with the Edit tool.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/komori-2026.yaml",
 "old_string": "#     images were down-sampled and masked, so the paper applied its pipeline to the raw frames.",
 "new_string": "#     images were down-sampled and masked, which suggests, without stating, that the paper\n#     applied its pipeline to the raw frames."
}
```

```
The file claims/komori-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/komori-2026.yaml",
 "old_string": "    low-pass filter was required for significant decoding.\n  source: Discussion, Spontaneous Pupil Dilation, paragraph 1; Supplementary Figure 5E",
 "new_string": "    low-pass filter was required for significant decoding. The 0.1 Hz AUC did not differ\n    significantly from that at any other cutoff tested (0.05, 0.2, 0.5, 1 and 2 Hz).\n  source: Discussion, Spontaneous Pupil Dilation, paragraph 1; Supplementary Figure 5E"
}
```

```
The file claims/komori-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/komori-2026.yaml",
 "old_string": "  criterion: The pipeline of rest-decoding-above-null with 7, 10 and 13 ICs (ICs added or removed\n    in the order of the R6 reading), and with",
 "new_string": "  criterion: The pipeline of rest-decoding-above-null with 7, 10 and 13 ICs (ICs added or removed\n    in the order of the R6 reading). The Supplementary Figure 5 legend calls these the \"initial\n    number of ICs\", which leaves open whether the count is the number kept as features (reading\n    a) or the number before ICs are removed for VIF (reading b); both are run. Also with"
}
```

```
The file claims/komori-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/komori-2026.yaml",
 "old_string": "    variance_inflation_factor), maximum over features and frames, per model. Reproduced when the\n    maximum over models with 10 ICs is below 10 and within tolerance of 9.0; the 7, 13 and 15 IC\n    comparisons are reported as a variant, as the paper's selection of ICs cannot be repeated\n    exactly (R6). The legend names the test Mann-Whitney U, the same as the Wilcoxon rank-sum.",
 "new_string": "    variance_inflation_factor), maximum over features and frames, per model. The 7, 13 and 15 IC\n    feature sets are formed as in rest-ic-count-and-window; the comparisons use the paper's test,\n    Mann-Whitney U with Holm correction over the three pairs against 10 ICs, 5 models each\n    (Supplementary Figure 6G legend). Reproduced when the maximum over models with 10 ICs is below\n    10 and within tolerance of 9.0, 7 ICs give a significantly lower maximum VIF than 10, and 13\n    and 15 ICs do not differ from 10. Partially reproduced when the 10-IC maximum holds and the\n    comparisons do not, which may follow from the IC selection that cannot be repeated exactly\n    (R6). The Mann-Whitney U test is the same as the Wilcoxon rank-sum."
}
```

```
The file claims/komori-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/komori-2026.yaml",
 "old_string": "    reported\n  statistics:\n  - about: SHAP per IC and time window, model against null\n    test: paired t-test (uncorrected)\n    p: 0.05\n    p_relation: \"<\"\n    n: 5 models\n  depends_on:",
 "new_string": "    reported\n  depends_on:"
}
```

```
The file claims/komori-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/komori-2026.yaml",
 "old_string": "    stimulation (maximum VIF 1954.1), while 20 to 30 ICs from ICA reduce the maximum VIF to 7.8.\n  source: Results, Extraction of independent components of cortical activity; Supplementary Figure\n    6A to 6C",
 "new_string": "    stimulation (maximum VIF 1954.1), while ICA (20 to 30 components) features reduce it to 7.8\n    with 10 ICs kept; 10 ICs give a significantly lower maximum VIF than 12 or 14 ICs.\n  source: Results, Extraction of independent components of cortical activity; Supplementary Figure\n    6A to 6C"
}
```

```
The file claims/komori-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/komori-2026.yaml",
 "old_string": "    stimulation was 1954.1 ... The resulting maximum VIF was 7.8\n  expected:",
 "new_string": "    stimulation was 1954.1 ... The resulting maximum VIF was 7.8\n  statistics:\n  - about: maximum VIF, 10 ICs against 12 and against 14 ICs\n    test: Wilcoxon rank-sum test\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Holm\n    n: 5 models\n  expected:"
}
```

```
The file claims/komori-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/komori-2026.yaml",
 "old_string": "  - quantity: maximum VIF, IC features, somatosensory\n    value: 7.8",
 "new_string": "  - quantity: maximum VIF, 10 IC features, somatosensory (Supplementary Figure 6A title)\n    value: 7.8"
}
```

```
The file claims/komori-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/komori-2026.yaml",
 "old_string": "  - quantity: AUC, unconstrained\n    value: 0.668\n    tolerance: 0.041\n  - quantity: AUC, -0.9 s condition",
 "new_string": "  - quantity: validation AUC over the 5 models, unconstrained (the Figure 1F legend gives median\n      and standard error; the tolerance is the paper's stated spread)\n    value: 0.668\n    tolerance: 0.041\n  - quantity: validation AUC over the 5 models, -0.9 s condition"
}
```

```
The file claims/komori-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/komori-2026.yaml",
 "old_string": "  - quantity: positive labels, -0.9 s\n    value: 35.7\n    tolerance: 3.57\n    unit: \"%\"",
 "new_string": "  - quantity: sessions selected, -0.8 s\n    value: 34.4\n    tolerance: 3.44\n    unit: \"%\"\n  - quantity: positive labels, unconstrained\n    value: 48.2\n    tolerance: 4.82\n    unit: \"%\"\n  - quantity: positive labels, -0.9 s\n    value: 35.7\n    tolerance: 3.57\n    unit: \"%\"\n  - quantity: positive labels, -0.8 s\n    value: 34.7\n    tolerance: 3.47\n    unit: \"%\""
}
```

```
The file claims/komori-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/komori-2026.yaml",
 "old_string": "    −0.5 to 0.0 s windows ... Holm correction ... eliminated statistical significance\n  criterion:",
 "new_string": "    −0.5 to 0.0 s windows ... Holm correction ... eliminated statistical significance\n  statistics:\n  - about: SHAP of IC5 against null, each window from -0.5 to 0.0 s, uncorrected\n    test: paired t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 5 models\n  - about: the same comparisons after Holm correction\n    test: paired t-test\n    p: 0.05\n    p_relation: \">\"\n    corrected: Holm\n    n: 5 models\n  criterion:"
}
```

```
The file claims/komori-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/komori-2026.yaml",
 "old_string": "    dorsal part (ACAd) at −0.1 to 0.0 s (0.002), and IC15 near ACAd and RSP at −0.1 to 0.0 s\n    (0.0015)\n  statistics:",
 "new_string": "    dorsal part (ACAd) at −0.1 to 0.0 s (0.002), and IC15 near ACAd and RSP at −0.1 to 0.0 s\n    (0.0015) ... In the visual contextual stimulation model, IC4 ... showed high contributions at\n    −0.3 to −0.1 s (0.0008) and −0.1 to 0.0 s (0.0030)\n  statistics:"
}
```

```
The file claims/komori-2026.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/komori-2026.yaml",
 "old_string": "    test: paired t-test with Holm correction\n    p: 0.0212\n    n: 5 models\n  criterion:",
 "new_string": "    test: paired t-test with Holm correction\n    p: 0.0212\n    n: 5 models\n  - about: visual pattern and visual contextual, models without the 0.0 s frame against null\n    test: paired t-test\n    p: 0.05\n    p_relation: \">\"\n    corrected: Holm\n    n: 5 models\n  expected:\n  - quantity: AUC gain of top over bottom ICs, somatosensory\n    value: 43.1\n    tolerance: 4.31\n    unit: \"%\"\n  - quantity: AUC gain of top over bottom ICs, visual pattern\n    value: 19.1\n    tolerance: 1.91\n    unit: \"%\"\n  - quantity: AUC gain of top over bottom ICs, visual contextual\n    value: 37.1\n    tolerance: 3.71\n    unit: \"%\"\n  - quantity: AUC gain over null, somatosensory, -1.50 to -0.25 s features\n    value: 23.6\n    tolerance: 2.36\n    unit: \"%\"\n  criterion:"
}
```

```
The file claims/komori-2026.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
tail -5 claims/komori-2026.yaml
```

```
p: 0.05
    p_relation: "<"
    n: 5 models
  criterion: Not testable on DANDI:001425, which holds no stimulation experiments; the paper's
    recordings are not deposited (available on request).
```

**Agent**

Now the new claim and the checks entry.

**Agent calls Bash**

```bash
cat >> claims/komori-2026.yaml <<'EOF'
- id: supp2-session-selection-needed
  statement: In preliminary visual pattern experiments, including sessions in which the pupil
    reached threshold before the pre-peak window, or never reached threshold after stimulation,
    made the decoder fail, its accuracy not distinguishable from the null model; such sessions
    were therefore excluded from all datasets.
  source: Results, Pupil dilation in response to somatosensory stimulation, paragraph 1; Figure
    2G; Supplementary Figure 2E; Discussion, Conditions for Successful Decoding
  quote: Preliminary experiments with visual pattern stimulation showed that including sessions in
    which the pupil reached threshold before a specified pre-peak time window, or sessions in which
    the pupil never reached threshold after stimulation, caused the machine learning model to fail
  criterion: Not testable on DANDI:001425, which holds no visual stimulation; the paper's recordings
    are not deposited (available on request). The Supplementary Figure 2E legend names no test.
checks:
- date: 2026-11-25
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Opening comment, R2. The text said the paper applied its pipeline to the raw resting frames;
    the Methods do not say so, so it is now marked as suggested, not stated.
  - rest-needs-0-1-hz, statement. Added that the 0.1 Hz AUC did not differ significantly from any
    other cutoff (Supplementary Figure 5E, Wilcoxon rank-sum with Holm, all n.s.), which the
    statistics already recorded and the statement left out.
  - rest-ic-count-and-window, criterion. The Supplementary Figure 5 legend says "initial number of
    ICs"; whether that is the count kept or the count before VIF pruning is now named as open,
    with both readings run.
  - rest-vif-below-10, criterion. The statement claims the 7, 13 and 15 IC comparisons but the
    criterion only reported them; they are now judged on the paper's test (Mann-Whitney U, Holm,
    Supplementary Figure 6G), with partial reproduction when only the 10-IC maximum holds.
  - rest-shap-medial-anterior-first, removed the statistics entry. The paper reports no test for
    the precedence of IC7 over IC6 and IC4 (Discussion); the uncorrected paired t-test of the
    Supplementary Figure 9 legend stays as a method in the criterion's reading (a).
  - fig1-roi-vif-vs-ica. The 7.8 is the maximum VIF with 10 ICs (Supplementary Figure 6A title),
    not with 20 to 30 ICs; statement and expected quantity corrected. Added the Supplementary
    Figure 6B result (10 ICs lower than 12 and 14 ICs, Wilcoxon rank-sum with Holm, p < 0.05).
  - fig1-somato-exclusion-window, expected quantities now say validation AUC over 5 models, with
    the Figure 1F legend's median and standard error.
  - fig1-somato-selection-rates, added expected values for 34.4% (-0.8 s sessions), 48.2%
    (unconstrained positives) and 34.7% (-0.8 s positives), which the statement reports.
  - fig4-shap-somato-ic5, added the statistics the text reports (uncorrected paired t-test p <
    0.05, not significant after Holm).
  - fig4-shap-visual-ics, extended the quote to the visual contextual IC4 result the statement
    includes.
  - supp10-top-shap-ics, added the expected percentages (43.1, 19.1, 37.1, 23.6) and the
    Holm-corrected absence for the visual models without the 0.0 s frame (Supplementary Figure
    10F, I legend).
  - Added supp2-session-selection-needed. The finding that sessions with early or absent
    threshold crossings make the decoder fail (Supplementary Figure 2E; Discussion, Conditions for
    Successful Decoding) underlies the abstract's main result and had no claim.
  - Open, not settled. Which mice and resting sessions of DANDI:001425 were used (R1), the
    resting preprocessing (R2), the pupil measure (R3), sample construction (R4), epoch selection
    (R5), the hand selection of ICs (R6), the fold unit (R7), the shuffle scope (R8) and the SHAP
    background (R10) are not fixed by the paper; the criteria name the readings.
  - Open, not settled. Values in rest-decoding-above-null, rest-loss-accuracy-vs-null and
    rest-needs-0-1-hz are read from Supplementary Figure 5 bars, not printed numbers; the 10%
    tolerances rest on that reading.
  - Open, not settled. The paper reports no test of the 2 Hz resting model against null; the
    rest-needs-0-1-hz criterion uses the null-model paired t-test of Supplementary Figure 5D, the
    paper's test of "above chance" for these models.
EOF
cd  && python tools/claims_check.py claims/komori-2026.yaml paper/10.64898-2026.05.27.726399.txt; grep -n "—\|rather" claims/komori-2026.yaml | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^checks:/,$p' claims/komori-2026.yaml | grep -n "[^ ]: " | grep -v "^[0-9]*:  *\(- \)\?[a-z_]*: " ; git status --short
```

```
2:- date: 2026-11-25
 M claims/komori-2026.yaml
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

**Checker:** `claims/komori-2026.yaml: 24 claims, 22 quotes, 31 statistical values, 0 problems`. Before my edits it read 23 claims, 21 quotes, 28 statistical values, 0 problems.

**Changes, by claim**
- **Opening comment, R2:** the file said the paper ran its own processing pipeline on the raw resting frames. The Methods don't say that, so it is now marked as implied but not stated.
- **rest-needs-0-1-hz:** the statement now adds that the 0.1 Hz AUC did not differ significantly from any other cutoff (Supplementary Figure 5E, all n.s.). The file already recorded that test, but the statement left it out.
- **rest-ic-count-and-window:** the Supplementary Figure 5F legend says "initial number of ICs". It's unclear whether that means the ICs kept or the count before ICs were removed to bring VIF under 10. Both readings are now named and run.
- **rest-vif-below-10:** the statement claims the 7, 13 and 15 IC comparisons, but the criterion only reported them. They are now judged on the paper's test (Mann-Whitney U with Holm, Supplementary Figure 6G). It counts as partially reproduced when only the 10-IC maximum of 9.0 holds.
- **rest-shap-medial-anterior-first:** I removed the statistics entry. The paper reports no test for IC7 preceding IC6 and IC4. The test from the Supplementary Figure 9 legend stays in the criterion as a method.
- **fig1-roi-vif-vs-ica:** the 7.8 is the maximum VIF with 10 ICs (Supplementary Figure 6A), not with 20 to 30 ICs. I corrected that and added the Supplementary Figure 6B result: 10 ICs give a lower maximum VIF than 12 or 14 ICs, p < 0.05 with Holm.
- **fig1-somato-exclusion-window:** the expected quantities now say they are validation AUC over the 5 models, reported as median and standard error per the Figure 1F legend.
- **fig1-somato-selection-rates:** added expected values for 34.4%, 48.2% and 34.7%, which the statement reports but the file left out.
- **fig4-shap-somato-ic5:** added the reported statistics: significant by uncorrected paired t-test, not significant after Holm correction.
- **fig4-shap-visual-ics:** extended the quote to cover the visual contextual IC4 result, which the statement includes.
- **supp10-top-shap-ics:** added the expected percentages (43.1, 19.1, 37.1, 23.6). Also added the result that visual models without the 0.0 s frame don't differ from null after Holm correction.
- **New claim, supp2-session-selection-needed:** decoding fails unless sessions with early or absent dilation are excluded (Supplementary Figure 2E and the Discussion). This underlies the abstract's main result and had no claim. Like the file's other own-recording claims, it can't be tested on DANDI:001425.

**Still open** (recorded under `checks`)
- **Resting-state methods:** the paper doesn't fix several details: which mice and sessions, preprocessing, pupil measure, how samples and epochs are built, the hand-picked ICs, fold unit, shuffle scope, and the SHAP background. The criteria name the possible readings (R1 to R10).
- **Values read from bars:** the resting AUC, loss and accuracy values come from Supplementary Figure 5 bar heights, not printed numbers. The 10% tolerances rest on that reading.
- **2 Hz resting model:** the paper reports no test of it against null. The criterion uses the null-model paired t-test from the Supplementary Figure 5D legend.

**Ready:** yes. The last check is marked `ready: true`. Nothing is committed.

## End of run

30 turns, 3 minutes, $1.49 at API prices, result: success.
