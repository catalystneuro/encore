# 001357 · claims-check · run 39676154582

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001357/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,220p docs/protocol.md
```

```
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
     Methods, the figure legends, the supplement, or the code the paper
     links, and the criterion says which. Search all of them before
     treating a detail as open.
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001357/*.yaml; python tools/claims_check.py claims/001357/10.1523-jneurosci.1893-23.2024.yaml paper/10.1523-jneurosci.1893-23.2024.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/71f6fc30-b987-4a68-838c-1d4ac85785c2/tool-results/bu3zds53d.txt"
}
```

```
1	# Claims for Namima, Kempkes, Zamarashkina, Owen & Pasupathy (2025), "High-Density Recording
2	# Reveals Sparse Clusters (But Not Columns) for Shape and Texture Encoding in Macaque V4",
3	# J Neurosci 45(5) e1893232024, on dandiset 001357.
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21, protocol
5	# pilot-10 as stated in docs/protocol.md.
6	#
7	# Text read: the version of record (PDF supplied by a person, text extracted with PyMuPDF), with
8	# the main text, Materials and Methods, and figure legends. The paper has no supplement. The PDF
9	# was not opened; the text was enough.
10	#
11	# Code: the paper links no analysis code and gives no code or data availability statement. The
12	# only link it gives is the stimulus software, pype (reference Mazer 2013,
13	# github.com/mazerj/pype3, HEAD at 49056d6f7e02bb217b2f044dba6ec7a33173b4ca on 2026-10-21). It
14	# runs the stimuli and the fixation task and holds none of the analyses, so it settles no method
15	# detail here. The analyses were written in MATLAB (fit.m, confint.m, conv2.m, the cortex-lab
16	# Spikes toolbox) by the authors and are not public. The noise-corrected correlation follows
17	# Pospisil and Bair (2021, J Neurosci 41 5638), which the paper cites and does not link; its method
18	# is taken from this paper's Methods alone.
19	#
20	# Data the paper used: two rhesus macaques, M1 (female, 6.0 kg, Neuropixels 1.0) and M2 (male,
[... 832 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; grep -n -i "Materials and Methods\|^Results\|^Discussion\|^References" paper/*.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1893-23.2024.txt",
 "limit": 1000
}
```

Result: not kept, because it reads the paper's text.

**Agent**

I'm reading the rest of the paper now (Results continued, figure legends, Discussion).

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1893-23.2024.txt",
 "offset": 1000,
 "limit": 850
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1523-jneurosci.1893-23.2024.pdf')
for p in (9,11):
    d[p].get_pixmap(dpi=110).save(f'p{p+1}.png')
" && ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1893-23.2024.pdf",
 "pages": "10"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.1893-23.2024.pdf",
 "pages": "12"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Rendering the PDF isn't possible here (no PyMuPDF, no poppler), so I'll work from the text. Making the edits now.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "# Code: the paper links no analysis code and gives no code or data availability statement. The\n# only link it gives is the stimulus software, pype (reference Mazer 2013,\n# github.com/mazerj/pype3, HEAD at 49056d6f7e02bb217b2f044dba6ec7a33173b4ca on 2026-10-21). It",
 "new_string": "# Code: the paper links no analysis code and gives no code or data availability statement. The\n# only software it names for the experiments is the stimulus software, \"Pype2; Mazer, 2013\", with\n# no link; the first reader read pype3 (github.com/mazerj/pype3, HEAD at\n# 49056d6f7e02bb217b2f044dba6ec7a33173b4ca on 2026-10-21), a later version. It"
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "    different from zero (p < 0.05, solid lines) and a negative slope (Ssimilarity)\n  statistics:\n  - about: Isimilarity of neurons 1 to 9, 14 and 17, dark shapes\n    test: 95% confidence interval of the regression intercept\n    p: 0.05\n    p_relation: \"<\"\n    n: 24 neurons\n  expected:",
 "new_string": "    different from zero (p < 0.05, solid lines) and a negative slope (Ssimilarity)\n  expected:"
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "    numbered by depth. Isimilarity with dark shapes as in the opening comment. Reproduced when the\n    expected values hold and at least 7 of neurons 1 to 9 have a significant positive intercept;\n    partially reproduced when the session is found and fewer hold.",
 "new_string": "    numbered by depth (Figure 2A legend). Isimilarity with dark shapes as in the opening comment.\n    Reproduced when the expected values hold, the neurons with a significant positive intercept\n    are neurons 1 to 9, 14 and 17 with at most one neuron added or missing (the count's\n    tolerance), and their slopes are negative; partially reproduced when the session is found and\n    the set or the count does not match."
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "  criterion: Tuning invariance as in the opening comment, over the 120 shapes. Unreliable values\n    count as not above 0.5.",
 "new_string": "  criterion: Tuning invariance as in the opening comment, over the 120 shapes. Unreliable values\n    count as not above 0.5 (the Figure 4F legend plots an unreliable invariance at 0)."
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "    within tolerance. Depth is relative to the most superficial good unit. Needs the LF signal.",
 "new_string": "    within tolerance. Depth is relative to the most superficial good unit. Needs the LF signal.\n    OPEN, \"no other sinks were evident deeper\" in M1p12 has no criterion in the paper (it gives\n    no rule for what counts as a sink); that part is shown as the CSD profile and not judged."
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "    significantly greater than zero\n  statistics:\n  - test: 95% confidence interval of the regression intercept\n    p: 0.05\n    p_relation: \"<\"\n    n: 1,850 neurons, 74 penetrations\n  depends_on:",
 "new_string": "    significantly greater than zero\n  depends_on:"
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "    the pooled percentage over their neurons, under the readings of pop-significant-isimilarity.\n    Reproduced when one reading is within tolerance; partially reproduced when none is but one\n    lies between 10% and 30% (a level far from all-layer clustering, which the statement rests\n    on).",
 "new_string": "    the pooled percentage over their neurons, under the readings of pop-significant-isimilarity.\n    Reproduced when one reading is within tolerance."
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "    given (the paper cites Portilla and Simoncelli 2000 for the filters). The readings are (a)\n    the energy of each subband of a steerable pyramid with 4 orientations and 3 scales summed\n    over the image, and (b) quadrature Gabor energy at 4 orientations and 3 octave-spaced\n    frequencies summed over the image, each fit by least squares; with the contrast readings of",
 "new_string": "    given (the paper cites Portilla and Simoncelli 2000 for the filters and David et al. 2006 for\n    the orientation x SF model). The readings are (a) the energy of each subband of a steerable\n    pyramid with 4 orientations and 3 scales summed over the image, (b) quadrature Gabor energy\n    at 4 orientations and 3 octave-spaced frequencies summed over the image, and (c) the image's\n    Fourier power pooled in 4 orientation x 3 SF bands, as in the spectral model of David et al.\n    2006, each fit by least squares; with the contrast readings of"
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "    contrasts pooled, above 0.5 meaning vertical; averaged over neurons in 100 um depth bins. The\n    examples are M2p6 and M1p5. A penetration is all-one-preference when every occupied bin is on\n    one side of 0.5, and switching when bins on both sides form one change along depth. OPEN",
 "new_string": "    contrasts pooled, above 0.5 meaning vertical; averaged over neurons in 100 um depth bins. The\n    examples are M2p6 and M1p5 (Figure 6C, D). The paper defines neither kind of penetration;\n    the plain readings of \"entirely\" and \"switched\" are used, not taken from the paper: a\n    penetration is all-one-preference when every occupied bin is on one side of 0.5, and\n    switching when occupied bins lie on both sides, each side in a contiguous run of depth. OPEN"
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "    three values are within tolerance under one reading; partially reproduced when the AP\n    correlation is significantly positive and the CV correlation is not, without matching values.",
 "new_string": "    three values are within tolerance under one reading; partially reproduced when the AP\n    correlation is significantly positive and the CV correlation is not significantly positive,\n    without matching values."
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "    dataset to identify them. The paper reports no test of \"consistent\". The readings are (a) a\n    two-sided Mann-Whitney test of per-penetration percentages, the 18 against the other 56,\n    finds no difference at p < 0.05, and (b) the pooled percentage of the 18 penetrations with\n    more than 30 neurons is within the 10 to 30% band of pop-asymptote-20-percent. The 1,500 um\n    restriction recomputes Isimilarity on neurons within 1,500 um of depth zero. Reproduced when\n    both readings hold with and without the restriction.",
 "new_string": "    dataset to identify them. The paper reports no test of \"consistent\"; it compares the 18 by\n    eye with the population of Figure 5C, whose stated result is the ~20% level of\n    pop-asymptote-20-percent. The 18 are judged against that result: over those of the 18 with\n    more than 30 neurons, the percentage of neurons with significant Isimilarity, under the\n    readings of pop-asymptote-20-percent, is within its tolerance. A two-sided Mann-Whitney test\n    of per-penetration percentages, the 18 against the other 56, is shown as a variant and does\n    not decide. The 1,500 um restriction recomputes Isimilarity on neurons within 1,500 um of\n    depth zero. Reproduced when the rule holds with and without the restriction."
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "    taking more than 30 neurons\n    as \"large\", the yield the paper uses for shapes. Readings (a) median of per-penetration\n    percentages and (b) pooled percentage. Reproduced when one reading is within tolerance;\n    partially reproduced when none is but one lies between 10% and 30%.",
 "new_string": "    taking more than 30 neurons\n    as \"large\", the yield the paper uses for shapes. Readings (a) median of per-penetration\n    percentages and (b) pooled percentage. Reproduced when one reading is within tolerance."
}
```

```
<tool_use_error>String to replace not found in file.
String:     taking more than 30 neurons
    as "large", the yield the paper uses for shapes. Readings (a) median of per-penetration
    percentages and (b) pooled percentage. Reproduced when one reading is within tolerance;
    partially reproduced when none is but one lies between 10% and 30%.</tool_use_error>
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "    percentages and (b) pooled percentage. Reproduced when one reading is within tolerance;\n    partially reproduced when none is but one lies between 10% and 30%.",
 "new_string": "    percentages and (b) pooled percentage. Reproduced when one reading is within tolerance."
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "    comment. The reading here, as the paper gives no measure, is Pearson's r between the reliable\n    off-diagonal similarities at each displaced position and at the center. Reproduced when all\n    eight correlations (four positions, two penetrations) are positive with p < 0.05.",
 "new_string": "    comment. OPEN, the paper gives no measure of \"similar across positions\"; neither reading\n    below is taken from the paper. (a) Pearson's r between the reliable off-diagonal similarities\n    at each displaced position and at the center; holds when all eight correlations (four\n    positions, two penetrations) are positive with p < 0.05. (b) The paper's own cluster\n    measure, Isimilarity (opening comment) at each position; holds when M2p9 has two or more\n    neurons with significant positive Isimilarity at every position and M2p28 has at most one\n    at every position (M1p12, with one such neuron, is the paper's example of no cluster).\n    Reproduced when both readings hold; blocked as methods_underspecified when they differ."
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent**

Now the `checks` entry. Checking the format another file uses:

**Agent calls Bash**

```bash
grep -n -A12 "^checks:" claims/001361/*.yaml | head -30
```

```
1422:checks:
1423-- date: 2026-10-21
1424-  kind: agent
1425-  model: claude-opus-5-5
1426-  ready: true
1427-  changes:
1428-  - Header. The switch mice were given as "m2 to m19", but m2 is a fixed-condition mouse (Extended Data Fig. 6d); listed the 11 switch mice as the Extended Data Fig. 7 and 8 legends name them, and noted that m11 was imaged from day 3 only (Methods, 2P imaging).
1429-  - fig6e-rr-prefer-reward. The statement said the median index was positive in 9 of 11 mice; the legend gives positive medians in all 11 and significance at p < 0.0045 in 9. Reworded.
1430-  - ed8k-rr-prefer-reward-after-switch. Added the eleven per-mouse tests from the Extended Data Fig. 8k legend under statistics, as fig6e has them.
1431-  - ed6a-rr-near-reward-stable. The criterion's rank-sum test and 50 cm split are not in the paper, which reports no test; named the comparison as open with two readings and the rule for when they disagree. Added the legend's cell counts (2294 RR, 3408 TR) as expected values, and "and become RR" to the statement, as the quote has it.
1432-  - ed6-across-day-drift. The Results cite panels j-m, which hold two cell sets (followed agnostic of day-B category, or keeping it); named both as readings, and said that the comparison of medians is not the paper's.
1433-  - ed7-no-anatomical-bias. The rule "fewer than half of the mice significant, not all in one direction" is not in the paper; replaced by the paper's own counts (2 ML, 1 AP, 1 depth) plus their tolerance.
1434-  - ed3fg-fields-remap-independently. The paper's tests are two-sided and its finding is "no correlation"; the criterion now counts significant correlations of either sign, not positive only.
```

**Agent calls Bash**

```bash
cat >> claims/001357/10.1523-jneurosci.1893-23.2024.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header. The paper names the stimulus software as "Pype2; Mazer, 2013" and links none; said so, and that the pype3 repository read is a later version.
  - ex-m2p6-cluster. Removed the statistics entry; p < 0.05 on each intercept is the threshold used to count the significant neurons, a method, not a result.
  - ex-m2p6-cluster. The rule "at least 7 of neurons 1 to 9" was not in the paper; the criterion now asks for the paper's set (1 to 9, 14, 17) within the count's tolerance and for their negative slopes, which the statement and quote give.
  - ex-m2p6-invariance. Cited the Figure 4F legend (unreliable invariance plotted at 0) for counting unreliable values as not above 0.5.
  - ex-csd-sinks. The statement's "no other sink deeper" in M1p12 had no criterion and the paper gives none; named it as open and shown, not judged.
  - pop-significant-isimilarity. Removed the statistics entry; p < 0.05 is the threshold used to count the 344 neurons, a method, not a result.
  - pop-asymptote-20-percent. Removed the partial outcome for a 10 to 30% band; the band is not in the paper.
  - texture-asymptote-20-percent. Removed the same 10 to 30% partial band, for the same reason.
  - orientation-sf-isimilarity. Added reading (c), Fourier power in orientation x SF bands, since the paper cites David et al. 2006 for the orientation x SF model.
  - orientation-auc-coarse-clusters. "Switching" was narrowed to one change along depth, which the paper does not say; loosened to bins on both sides in contiguous runs, and said that both definitions are plain readings, not the paper's.
  - apc-example-m2p51. The partial rule said the CV correlation "is not" without saying what; the CV correlation is significantly negative (p = 0.012), so the rule now says "not significantly positive".
  - gyrus-penetrations-consistent. Both readings (a Mann-Whitney test, a 10 to 30% band) were invented; the 18 are now judged against the paper's stated population result, the ~20% level of pop-asymptote-20-percent within its tolerance, and the Mann-Whitney test is a variant only.
  - position-examples-invariant. The only measure was the first reader's own; marked it open, added a second reading from the paper's cluster measure (Isimilarity per position, with M1p12 as the paper's example of no cluster), and the rule for when the readings differ.
  - Open. gyrus-penetrations-consistent rests on a comparison the paper makes only by eye; the rule above is the closest the paper's text allows, and the 18 penetrations can be identified only from the dataset.
  - Open. orientation-auc-coarse-clusters and position-examples-invariant rest on readings the paper does not define; the figures could not be rendered here to see which of Figure 6C and 6D is M2p6 and which M1p5.
  - Open. The penetration names (M2p6, M1p12, M2p9, M2p28, M2p51, M1p5) are not mapped to sessions by the paper; the claims that use them depend on finding them by neuron counts.
  - Open. The abstract says tuning was contrast invariant for texture as for shape; the Results give no texture invariance number, so no claim covers it.
EOF
python tools/claims_check.py claims/001357/10.1523-jneurosci.1893-23.2024.yaml paper/10.1523-jneurosci.1893-23.2024.txt; grep -n "—\|rather" claims/001357/*.yaml | grep -v "quote" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "not taken from the paper: a\n    penetration",
 "new_string": "not taken from the paper. A\n    penetration"
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001357/10.1523-jneurosci.1893-23.2024.yaml paper/10.1523-jneurosci.1893-23.2024.txt; grep -n "—\|rather" claims/001357/*.yaml | head; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001357/10.1523-jneurosci.1893-23.2024.yaml",
 "old_string": "judged against that result: over those",
 "new_string": "judged against that result. Over those"
}
```

```
The file claims/001357/10.1523-jneurosci.1893-23.2024.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
grep -n ": [^ ]" claims/001357/*.yaml | grep -v "^[0-9]*: *#" | grep -vE "^[0-9]+: *(- )?[a-z_]+: " | head; python tools/claims_check.py claims/001357/10.1523-jneurosci.1893-23.2024.yaml paper/10.1523-jneurosci.1893-23.2024.txt 2>&1 | tail -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "—\|rather" claims/001357/*.yaml
```

```
(Bash completed with no output)
```

**Agent**

**Checker result:** `27 claims, 27 quotes, 10 statistical values, 0 problems`. It started at 12 statistical values; I removed two that were thresholds used to count neurons.

**Changes, by claim**
- **Header:** the paper names "Pype2; Mazer, 2013" and gives no link. The header now says that the pype3 repository the first reader read is a later version.
- **ex-m2p6-cluster:** I removed the statistics entry. The p < 0.05 there is the cutoff used to count neurons, not a result. I also replaced the made-up rule "at least 7 of neurons 1 to 9". The criterion now asks for the paper's set (neurons 1 to 9, 14 and 17, with one neuron of slack from the count's tolerance) and for their negative slopes.
- **ex-m2p6-invariance:** the rule that unreliable values count as not above 0.5 now cites the Fig. 4F legend, which plots an unreliable value at 0.
- **ex-csd-sinks:** the paper gives no criterion for "no other sink deeper" in M1p12. That part is now marked open: the CSD profile is shown but not judged.
- **pop-significant-isimilarity:** I removed the statistics entry, because the p < 0.05 is the cutoff behind the 344 count.
- **pop-asymptote-20-percent and texture-asymptote-20-percent:** I removed the "partially reproduced" outcome for a 10 to 30% band, which the paper never gives.
- **orientation-sf-isimilarity:** I added reading (c), Fourier power in orientation × spatial-frequency bands, because the paper cites David et al. 2006 for this model.
- **orientation-auc-coarse-clusters:** "switching" had been narrowed to a single change along depth, which the paper doesn't say. I loosened it and stated that both kinds of penetration are plain readings, not definitions from the paper.
- **apc-example-m2p51:** the partial-outcome rule now says the curvature correlation must be "not significantly positive". It is significantly negative (p = 0.012).
- **gyrus-penetrations-consistent:** both of its tests were invented (a Mann-Whitney test and the 10 to 30% band). The 18 penetrations are now judged against the paper's stated level of about 20%, within that claim's tolerance. The Mann-Whitney test stays only as a variant and does not decide the outcome.
- **position-examples-invariant:** its only measure was the first reader's own. I marked it open and added a second reading from the paper's own cluster measure (Isimilarity at each position). If the two readings disagree, the claim is blocked as `methods_underspecified`.

**Still open** (all recorded under `checks`)
- **gyrus-penetrations-consistent:** the paper compares the 18 penetrations with the rest only by eye. Those 18 can only be identified from the dataset.
- **orientation-auc-coarse-clusters and position-examples-invariant:** both rest on readings the paper doesn't define. I couldn't render the PDF here (no PyMuPDF or poppler), so I can't say whether Fig. 6C is M2p6 or M1p5.
- **Penetration names:** the paper never maps M2p6, M1p12, M2p9, M2p28, M2p51 or M1p5 to sessions. They have to be found by neuron counts.
- **Texture contrast invariance:** the abstract claims it, but the Results report no number for it, so no claim covers it.

**Ready:** yes. I set `ready: true`. Every main finding has a claim, and every remaining gap is named as open with the readings the paper allows. Nothing is committed.

## End of run

32 turns, 3 minutes, result: success.
