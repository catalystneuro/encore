# 001193 · claims-check · run 39821742953

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001193/ paper/; grep -n "Reader" -A60 docs/protocol.md | head -120
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 96,200p docs/protocol.md; cat claims/001193/*.yaml; python tools/claims_check.py claims/001193/10.1038-s41562-022-01334-6.yaml paper/10.1038-s41562-022-01334-6.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 120,200p docs/protocol.md; python tools/claims_check.py claims/001193/10.1038-s41562-022-01334-6.yaml paper/10.1038-s41562-022-01334-6.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml"
}
```

```
1	# Claims for Zhu, Xu, Lu, Hu et al. (2022), Nature Human Behaviour 6, 1104-1111, on dandiset 001193.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
3	# docs/protocol.md, version pilot-10.
4	#
5	# Text read: the version of record (paper/10.1038-s41562-022-01334-6.txt, from the publisher PDF
6	# supplied by hand), with main text, figure legends, Methods and reporting summary, and the
7	# Supplementary Information PDF (Supplementary Table 1, Supplementary Figures 1 to 10 and the list of
8	# stimulus sentences). The Supplementary Excel file and the Source Data named in the paper were not
9	# supplied; nothing below needs them except where said. Figure panels were not viewed (the PDF could
10	# not be rendered here), so numbers printed only inside panels (the region counts of the Fig. 2b Venn
11	# diagram) are not used.
12	#
13	# Code. The paper links no code: "The completely developed code that operates on the full data set
14	# will be made available from the authors upon reasonable request" (Code availability). No repository
15	# was read. Every method detail below is from the Methods, the figure legends or the supplement.
16	#
17	# Which dataset. The dandiset's title and description say it holds high-gamma (70-150 Hz) ECoG activity
18	# from the paper's syntactic and semantic tasks in the inferior frontal gyrus, in NWB. Claims that need
19	# other frequency bands (Fig. 1b, Supplementary Figs. 3, 4 and 7c) cannot be tested on high-gamma alone.
20	#
[... 518 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41562-022-01334-6.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41562-022-01334-6.txt",
 "offset": 1061,
 "limit": 780
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1038-s41562-022-01334-6.pdf')
d[2].get_pixmap(dpi=150).save('p3.png'); d[5].get_pixmap(dpi=200,clip=fitz.Rect(0,0,300,450)).save('p6.png')
s=fitz.open('paper/10.1038-s41562-022-01334-6.supp.pdf')
s[9].get_pixmap(dpi=150).save('s10.png'); s[8].get_pixmap(dpi=150).save('s9.png')
" && ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm mutool gs magick convert; python -c "import pypdfium2" 2>&1; python -c "import pdfplumber" 2>&1
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdfium2
ModuleNotFoundError: No module named 'pypdfium2'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41562-022-01334-6.pdf",
 "pages": "3"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "#   than 50 ms\" as (a) a run of at least 6 consecutive significant samples, or (b) at least 6\n#   significant samples in total; (V2)",
 "new_string": "#   than 50 ms\" as (a) a run of at least 6 consecutive significant samples, or (b) at least 6\n#   significant samples in total, or (c) a run spanning more than 50 ms from its first to its last\n#   sample (at least 7 consecutive samples); (V2)"
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "  statement: Participants responded fast and accurately in the linguistic task, most response times",
 "new_string": "  statement: Most participants responded fast and accurately in the linguistic task, most response times"
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "  source: Results, paragraph 1; Supplementary Figure 2b legend\n  quote: Most of the responding time is around 0.5-1.0 second.",
 "new_string": "  source: Results, paragraph 2; Supplementary Figure 2b legend\n  quote: Most of the responding time is around 0.5-1.0 second."
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Revert my source change; Results paragraph 1 was correct.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "  source: Results, paragraph 2; Supplementary Figure 2b legend",
 "new_string": "  source: Results, paragraph 1; Supplementary Figure 2b legend"
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "    open, the cross-validation and the features (time samples of the band amplitude in the keyword\n    window); reproduced when, under every classifier, a band with lower bound at or above 70 Hz gives\n    the highest accuracy and it exceeds 0.72 (80% less the tolerance).",
 "new_string": "    open, the cross-validation and the features (time samples of the band amplitude in the keyword\n    window). The paper reports the band accuracies for the SVM (Fig. 1b legend) and for logistic\n    regression (Supplementary Fig. 3a legend) only; reproduced when, under both, a band with lower\n    bound at or above 70 Hz gives the highest accuracy and, for the SVM, it exceeds 0.72 (80% less\n    the tolerance). The kNN result is shown as a variant. The ERP part is judged from the measure of\n    Supplementary Fig. 3d (the peak power during violation against the peak power during CORR, per\n    responding electrode): it holds when the mean difference is largest in the 70 to 150 Hz band."
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "  criterion: For the electrodes of E, the test of V applied to the sentence before the keyword, aligned\n    to the first word, over the words shared by CORR and each violation (words 1 to 3, 0 to 1,500 ms;\n    the SEM verb, word 2, differs, so for SEM words 1 and 3 only, as samples 0 to 500 ms and 1,000 to\n    1,500 ms). The paper gives no count; \"only\" is read as at most as many electrodes passing V before\n    the keyword as the 5% expected by chance at the paper's alpha, relative to the number passing after\n    it (claim fig2b-violation-electrodes). Reproduced when the number of electrode and condition pairs\n    passing before the keyword is no more than 5% of those passing after it. The counts are reported.",
 "new_string": "  criterion: A claim of absence before the keyword, judged on the paper's test, the test of V (the\n    discriminating period of Fig. 1e and the ERP amplitude Methods), applied to the electrodes of E\n    over the sentence before the keyword, aligned to the first word (words 1 to 3, 0 to 1,500 ms).\n    Reproduced when no electrode and condition pair passes V before the keyword; not reproduced when\n    any does. The count of passing pairs, before and after the keyword, is reported either way. The\n    SEM verb (word 2) differs from the CORR verb; the test without SEM samples 500 to 1,000 ms is\n    shown as a variant. The earlier rule (no more than 5% of the after-keyword count) was a threshold\n    the paper does not give."
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "    shown as a variant. The earlier rule (no more than 5% of the after-keyword count) was a threshold\n    the paper does not give.",
 "new_string": "    shown as a variant."
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "    1,000 ms of every responding electrode, concatenated over electrodes; (b) the vector of each\n    electrode's mean HGA over 0 to 1,000 ms; and the \"syntactic to semantic\" distance read as (i) SEM\n    to SYN-P, (ii) SEM to SYN-C, (iii) the mean of the two, or (iv) the linkage height at which SEM\n    joins the SYN-P and SYN-C cluster. Fig. 2c's y axis is a \"relative distance\", so absolute values\n    depend on the vector. Reproduced when, under every reading, SYN-P to SYN-C is the smallest distance\n    and the syntactic to semantic distance is larger; the values are compared with the expected ones\n    under each reading and the matching readings named. Partially reproduced when the order holds\n    under some readings only.",
 "new_string": "    1,000 ms of every responding electrode, concatenated over electrodes; (b) the trial-mean HGA time\n    course from 0 to 1,000 ms averaged over the responding electrodes (the Methods call it a\n    \"time-course similarity\", so a reading without time is not allowed); and the \"syntactic to\n    semantic\" distance read as (i) SEM to SYN-P, (ii) SEM to SYN-C, (iii) the mean of the two, or (iv)\n    the linkage height at which SEM joins the SYN-P and SYN-C cluster. Fig. 2c's y axis is a \"relative\n    distance\", so absolute values depend on the vector. Reproduced when, under every reading, the\n    syntactic to semantic distance is larger than SYN-P to SYN-C, and under at least one reading both\n    values are within tolerance; partially reproduced when the order holds under every reading but no\n    reading matches the values; not reproduced when the order fails under every reading; blocked\n    otherwise. The values under each reading are reported."
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "    Fig. 7a plots F values. Reproduced when both fractions",
 "new_string": "    Fig. 7a plots F values. The two percentages fit 18 and 6 of 23 electrodes (an inference, the\n    paper gives no count), so the 10% tolerance on 26.1% is below one electrode. Reproduced when both fractions"
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "    Fig. 7a plots F values. The two percentages fit 18 and 6 of 23 electrodes (an inference, the\n    paper gives no count), so the 10% tolerance on 26.1% is below one electrode. Reproduced when both fractions",
 "new_string": "    Fig. 7a plots F values. The smallest count the two percentages fit is 18 and 6 of 23 electrodes\n    (an inference; the paper gives no count), so the 10% tolerance on 26.1% is below one electrode\n    there. Reproduced when both fractions"
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "    pairs of conditions with at least three electrodes each. Reproduced when no participant has a pair\n    significant at p < 0.05 uncorrected; partially reproduced when at most one of the testable\n    participants has; not reproduced otherwise.",
 "new_string": "    pairs of conditions with at least three electrodes each (a standard minimum, not the paper's). A\n    claim of absence: reproduced when no participant has a pair significant at p < 0.05 uncorrected;\n    not reproduced otherwise. The number of participants with a significant pair is reported."
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "  criterion: k-nearest neighbours (Supplementary Fig. 9 legend) with the settings of the Methods (5\n    neighbours, Minkowski p = 2, uniform weights), features from the CORR response of each electrode\n    only, onset, offset, peak (L), area and amplitude at T0 (Methods). Open, (a) the electrodes and\n    labels, single-type electrodes of fig2b-single-type labelled by their type, and non-responding\n    electrodes the electrodes of E that pass V for no condition; co-activated electrodes left out;",
 "new_string": "  criterion: k-nearest neighbours (Supplementary Fig. 9 legend) with the settings the Methods give for\n    the frequency decoding (5 neighbours, Minkowski p = 2, uniform weights; the Methods state them\n    for that analysis, and no other kNN settings are given), features from the CORR response of each\n    electrode only, onset, offset, peak (L), area and amplitude at T0 (Methods, Predicting different\n    types of electrodes). Open, (a) the electrodes and labels, single-type electrodes of\n    fig2b-single-type labelled by their type, and non-responding electrodes either (a1) the electrodes\n    of E that pass V for no condition or (a2) the IFG electrodes outside E; co-activated electrodes\n    left out;"
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "    coordinate with its 95% confidence interval (Fig. 3e legend), for onset and peak, each condition,\n    and each axis. The legend calls the axes the x and y coordinates; on MNI152 the anterior-posterior\n    axis is y and the superior-inferior axis z, and both are used. Reproduced",
 "new_string": "    coordinate with its 95% confidence interval (Fig. 3e legend), for onset and peak, each condition,\n    and each axis. The legend calls the axes the x and y coordinates, while the panel names the\n    anterior-posterior and superior-inferior axes; on MNI152 these are y and z. Open, (a) MNI y and z;\n    (b) MNI x and y, as the legend prints. Reproduced"
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "    CI includes zero; not reproduced when any excludes it, under the readings of fig3-latency-values\n    (blocked when they differ).",
 "new_string": "    CI includes zero; not reproduced when any excludes it, under the readings of fig3-latency-values\n    and of the axes (blocked when they differ)."
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "    regression, kNN), classifying CORR, SYN-P, SYN-C and SEM trials from the HGA of the responding\n    electrodes of fig2b-violation-electrodes within each participant at each 10 ms sample (or in 100\n    ms windows), 5-fold stratified cross-validation, accuracy averaged over participants. Reproduced\n    when, under every reading, the time of maximum accuracy lies in 360 to 770 ms (the range widened\n    by 10% of each bound).",
 "new_string": "    regression, kNN), classifying CORR, SYN-P, SYN-C and SEM trials together, or each violation\n    against CORR (the legend says \"classification accuracy of each violation type\"), from the HGA of\n    the responding electrodes of fig2b-violation-electrodes within each participant at each 10 ms\n    sample (or in 100 ms windows), 5-fold stratified cross-validation (a standard choice), accuracy\n    averaged over participants. Reproduced when, under every reading, the time of maximum accuracy\n    lies in 360 to 770 ms (the range widened by 10% of each bound); not reproduced when it lies\n    outside under every reading; blocked otherwise."
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "    Fig. 4b) on the 4 to 10 Hz amplitude and on HGA; reproduced when more electrodes pass at 4 to 10 Hz\n    than in high gamma.",
 "new_string": "    Fig. 4b) on the 4 to 10 Hz amplitude and on HGA; reproduced when more electrodes pass at 4 to 10 Hz\n    than in high gamma. The measure of Supplementary Fig. 4a (peak power during NL-VIO against peak\n    power during NL-CORR, per electrode and band) is shown with it."
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -l "^checks:" claims/*/*.yaml | head -2 | xargs -I{} sh -c 'sed -n "/^checks:/,\$p" {} | head -20'
```

```
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
  - auc-weak-strong. The criterion compared groups on the Fig. 
[... 24 more lines not kept]
```

**Agent**

Now add the missing SYN-C variability claim and the checks entry.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "- id: fig3e-latency-not-location",
 "new_string": "- id: fig3-sync-latency-variability\n  statement: Onset and peak latencies vary more across electrodes for SYN-C than for SYN-P.\n  source: Results, paragraph 10; Figure 3c and 3d\n  quote: This possibility may help explain the results that relatively later (and also greater\n    variations of) onset and peak were observed for SYN-C than SYN-P.\n  depends_on:\n  - fig3-latency-values\n  criterion: The paper gives no measure or test of the variation. Electrodes and latencies under the\n    readings of fig3-latency-values; the spread is the standard deviation of the latencies across\n    electrodes (a standard choice; the interquartile range, which Fig. 3a's boxes show, as a variant).\n    Reproduced when the SYN-C spread exceeds the SYN-P spread for both onset and peak under every\n    reading; not reproduced when it does for neither under every reading; blocked otherwise.\n- id: fig3e-latency-not-location"
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat >> claims/001193/10.1038-s41562-022-01334-6.yaml <<'EOF'
checks:
- date: 2026-10-22
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header, V1. Added reading (c), a run spanning more than 50 ms from first to last sample (at least 7 consecutive samples), which the words "for more than 50 ms" also allow at 10 ms samples.
  - behaviour-response-time. Statement said participants responded fast and accurately; the paper says most participants did.
  - fig1b-high-gamma-best-band. The criterion required the best band under every classifier, kNN included; the paper reports band accuracies for the SVM (Fig. 1b) and logistic regression (Supplementary Fig. 3a) only, and the 80% figure from Fig. 1b. kNN is now a variant. Added a test for the ERP part of the statement, from the Supplementary Fig. 3d measure.
  - fig1d-only-after-keyword. The criterion judged "only after the keywords" with a 5% threshold the paper does not give. It is now a claim of absence on the paper's test (V before the keyword, no passing pair), with the SEM verb exclusion as a variant, since the paper's statement covers the whole pre-keyword sentence.
  - fig2c-euclidean-similarity. Reading (b), each electrode's mean HGA without time, is not allowed by the Methods ("time-course similarities"); replaced by the time course averaged over electrodes. The criterion decided on the order alone and ignored the expected values; it now needs the values within tolerance under at least one reading, with a partial outcome for order alone, and says when it is not reproduced or blocked.
  - suppfig7a-com-overlap. Noted that 78.3% and 26.1% fit 18 and 6 of 23 electrodes at the smallest, so the tolerance on 26.1% is below one electrode.
  - suppfig8b-individual-no-separation. Removed the partial outcome, which a claim of absence does not have, and marked the three-electrode minimum as a standard choice.
  - suppfig9-predict-from-corr. Said the kNN settings are the ones the Methods give for frequency decoding; added the reading of non-responding electrodes as IFG electrodes outside E.
  - fig3e-latency-not-location. The criterion said "both are used" without naming the readings of the legend's x and y coordinates; now names (a) MNI y and z and (b) MNI x and y.
  - suppfig10a-separable-400-700. Added the reading of each violation against CORR (the legend's "each violation type"), marked the cross-validation as a standard choice, and said when the claim is not reproduced or blocked.
  - nl-low-frequency. Added the Supplementary Fig. 4a measure to the criterion.
  - Added claim fig3-sync-latency-variability, the main-text result that SYN-C onsets and peaks vary more than SYN-P's, which had no claim.
  - Open. The Venn region counts of Fig. 2b, Supplementary Fig. 6 and Supplementary Fig. 7 could not be read (no PDF renderer here). The text layer of Fig. 2b holds the numbers 21, 6, 20, 2, 1 and 8, which sum to 58 and split into 49 single-type and 9 co-activated, but their regions cannot be assigned from text; per-type counts are therefore not expected values.
  - Open. suppfig7b-not-nonlinguistic keeps a 5% ceiling for "almost completely not", which the paper does not quantify; the Supplementary Fig. 7b Venn count, once read, should replace it.
  - Open. fig2b-violation-electrodes and the claims built on it treat the E and V readings as readings of a reported number (any reading may match), not as open method details (all must agree). The protocol allows the first for "which subset is meant"; the attempt should report every combination.
  - Open. fig2f-circuit-diameter. The Methods formula is garbled in the text layer; r = 0.5 mm / p is the only reading that gives the paper's ~3.25 mm from 9 of 58, but the formula as printed could not be checked against the PDF.
EOF
python tools/claims_check.py claims/001193/10.1038-s41562-022-01334-6.yaml paper/10.1038-s41562-022-01334-6.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "    responding electrode): it holds when",
 "new_string": "    responding electrode), and holds when"
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001193/10.1038-s41562-022-01334-6.yaml paper/10.1038-s41562-022-01334-6.txt; grep -nP "\w: " claims/001193/*.yaml | grep -vP "^\d+:\s*(- )?\{?[a-z_]+: " | grep -v "^[0-9]*:#" | head; grep -c "—\|rather" claims/001193/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "old_string": "    claim of absence: reproduced when",
 "new_string": "    claim of absence, reproduced when"
}
```

```
The file claims/001193/10.1038-s41562-022-01334-6.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001193/10.1038-s41562-022-01334-6.yaml paper/10.1038-s41562-022-01334-6.txt 2>&1 | tail -3; grep -n "[a-z)]: [a-z]" claims/001193/*.yaml | grep -v "^[0-9]*:#" | grep -vP "^\d+:\s*(- )?[a-z_]+: "
```

Result: not kept, because it reads the paper's text.

**Agent**

I checked the claims file for DANDI:001193 against the paper, corrected 11 claims, added one, and recorded everything under `checks`. The file is ready for an attempt, with four open problems listed below.

**Checker result:** `claims/001193/10.1038-s41562-022-01334-6.yaml: 25 claims, 25 quotes, 9 statistical values, 0 problems`. The first run, before my edits, gave 24 claims and 0 problems.

**Changes, by claim:**
- **Shared rule for "more than 50 ms" (V1):** added a third reading the words allow, a run of at least 7 consecutive 10 ms samples (spanning more than 50 ms from first to last).
- **behaviour-response-time:** the statement said participants responded fast and accurately; the paper says "most participants" did.
- **fig1b-high-gamma-best-band:** the criterion required high gamma to win under every classifier, kNN included. The paper reports band accuracies only for the SVM (Fig. 1b) and logistic regression (Supp. Fig. 3a), so kNN is now a variant. I also added a test for the ERP part of the statement, using the Supp. Fig. 3d measure.
- **fig1d-only-after-keyword:** the 5% threshold was not from the paper. It is now a claim of absence on the paper's own test: no electrode and condition pair may pass before the keyword. Leaving out the SEM verb period is a variant.
- **fig2c-euclidean-similarity:** reading (b) dropped time, which the Methods' "time-course similarities" does not allow; it is now the time course averaged over electrodes. The criterion judged on the order of distances alone; the expected values must now match under at least one reading.
- **suppfig7a-com-overlap:** noted that 78.3% and 26.1% fit 18 and 6 of 23 electrodes at the smallest, so the tolerance on 26.1% is below one electrode.
- **suppfig8b-individual-no-separation:** removed the "partially reproduced" outcome, which a claim of absence cannot have. The three-electrode minimum is now marked as a standard choice, not the paper's.
- **suppfig9-predict-from-corr:** noted that the kNN settings come from the Methods' frequency-decoding section. Added a second reading of "non-responding electrodes": IFG electrodes outside the responsive set.
- **fig3e-latency-not-location:** named the two readings of the legend's coordinates: MNI y and z, or MNI x and y as printed.
- **suppfig10a-separable-400-700:** added the reading of each violation classified against CORR. Marked the cross-validation as a standard choice, and added the "not reproduced" and "blocked" outcomes.
- **nl-low-frequency:** added the Supp. Fig. 4a measure to the criterion.
- **New claim, fig3-sync-latency-variability:** the main text reports greater variation in SYN-C onsets and peaks than in SYN-P's, and no claim covered it.

**Still open:**
- I could not read the counts in the Venn diagrams (Fig. 2b, Supp. Figs. 6 and 7) because no PDF renderer is available here. The text layer of Fig. 2b holds 21, 6, 20, 2, 1 and 8, which add up to 58 and split into 49 single-type and 9 co-activated, but I can't tell which region each belongs to.
- suppfig7b-not-nonlinguistic still uses a 5% ceiling for "almost completely not", which the paper never puts a number on. Once read, the Supp. Fig. 7b Venn count should replace it.
- fig2b-violation-electrodes and the claims built on it let any reading of the electrode selection and violation tests match, instead of requiring all readings to agree. The protocol allows this when the question is which subset a reported number means. The attempt should report every combination.
- The circuit-size formula in the Methods is garbled in the text layer, and I could not check it against the PDF. r = 0.5 mm / p is the only reading that gives the paper's ~3.25 mm from 9 of 58.

Nothing was committed or pushed.

## End of run

34 turns, 4 minutes, result: success.
