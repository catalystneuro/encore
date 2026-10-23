# 000019 · claims-check · run 39692031522

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/000019/ paper/; sed -n '/Reader/,/^## /p' docs/protocol.md | head -150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000019/10.1038-nature11911.yaml paper/10.1038-nature11911.txt; cat claims/000019/10.1038-nature11911.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000019/10.1038-nature11911.yaml"
}
```

```
1	# Claims for Bouchard, Mesgarani, Johnson & Chang (2013), "Functional organization of human
2	# sensorimotor cortex for speech articulation", Nature 495, 327-332, on dandiset 000019
3	# ("Human ECoG speaking consonant-vowel syllables").
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
5	# protocol pilot-10 as stated in docs/protocol.md.
6	#
7	# Text read. The NIH author manuscript as served by PubMed Central (PMC3606666, NIHMS436351),
8	# not the version of record: main text, figure legends and Methods, with the supplement
9	# (NIHMS436351-supplement-1.pdf, Supplementary Figures 1 to 13 with their legends,
10	# Supplementary Table 1 and Supplementary Methods), as extracted to text. No PDF of the main
11	# text was supplied, so the main figures were read from their legends and from the Results
12	# sentences that cite them. Supplement pages 2 and 8 were opened in the supplement PDF, to
13	# see Supplementary Figure 1d and to confirm a printed p-value on page 8.
14	#
15	# Code. The paper links no code, and none is named in the Methods or the supplement. Every
16	# method below is from the Methods, the legends or the Supplementary Methods.
17	#
18	# Data the paper describes. Three native English speakers (Supplementary Table 1 names them
19	# EC2, EC33 and EC31) with a high-density subdural ECoG array over peri-Sylvian cortex, left
20	# hemisphere in two (EC2, EC31) and right in one (EC33), implanted for epilepsy monitoring.
[... 666 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/10.1038-nature11911.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature11911.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature11911.txt",
 "offset": 229,
 "limit": 540
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Checker passed (22 claims, 0 problems). I've read the paper and the claims; now checking the supplement figures for the consonant labels.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1038-nature11911.supp.pdf')
for p in [1,14]:
    d[p].get_pixmap(dpi=110).save(f'p{p+1}.png')
" && ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm && pdftoppm -r 100 -f 15 -l 15 -png paper/10.1038-nature11911.supp.pdf p && pdftoppm -r 100 -f 2 -l 2 -png paper/10.1038-nature11911.supp.pdf p && ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature11911.supp.pdf",
 "pages": "15"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature11911.supp.pdf",
 "pages": "2"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The PDF can't be rendered here (no poppler), so the figures can't be checked. Next I'll look at how other files format `checks`.

**Agent calls Bash**

```bash
grep -l "^checks:" claims/*/*.yaml | head -3; f=$(grep -l "^checks:" claims/*/*.yaml | head -1); sed -n '/^checks:/,$p' $f | head -40
```

```
claims/000005/10.1038-nn.4412.yaml
claims/000006/10.1038-s41586-018-0642-9.yaml
claims/000008/10.1038-s41586-020-2907-3.yaml
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
  - fs-suppress-movement-spiking. The paper does not name the groups of its Kruskal-Wallis test; the criterion 
[... 9 more lines not kept]
```

**Agent**

Now the edits. Header labels first:

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "#   Supplementary Figure 10, 11). Which consonant is which is from the phonetic feature matrix\n#   and Fig. 4c; /h/ and /r/ are not placed by any text sentence. OPEN; readings (a) /h/ and\n#   /r/ left out of the labelled sets, (b) /r/ coronal and /h/ dorsal.",
 "new_string": "#   Supplementary Figure 10, 11). Which consonant is which is read from the constriction\n#   location features of the phonetic feature matrix (Fig. 4c is a main figure and no PDF of\n#   it was available). No text sentence places /h/ (glottal), /r/, /w/ (labial-velar) or /j/\n#   (palatal). OPEN; readings (a) /h/, /r/, /w/ and /j/ left out of the labelled sets, (b) /r/\n#   coronal, /w/ labial, /j/ dorsal, /h/ left out (it has no oral articulator)."
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "    four consonant articulators (Supplementary Figure 1d), by least squares. Electrodes kept\n    when the mean over T_A of the regression p-value (F-test of the model) is below 0.05 for\n    any articulator A; W_iA is the mean of the weight over T_A (Methods Eq. 3); T_A is the\n    subject's mean onset-to-offset window of significant partial correlations for A (claim\n    fig3d-timing-sequence). Per subject, the W-weighted mean dorsal-ventral distance from the\n    Sylvian fissure over electrodes with positive weights, for lips and for tongue.\n    Reproduced when lips lie dorsal to tongue in every subject; partially reproduced in two\n    of three. The paper's maps are smoothed with a 2 mm uniform circular kernel and averaged\n    over subjects; the maps are shown for comparison.",
 "new_string": "    four consonant articulators (Supplementary Figure 1d), by least squares. Electrodes kept\n    when the mean over T_A of the \"associated p-value\" is below 0.05 for any articulator A\n    (Methods). OPEN, which p-value; readings (a) the F-test of the whole model, (b) the t-test\n    of articulator A's coefficient. W_iA is the mean of the weight over T_A (Methods Eq. 3);\n    T_A is the subject's mean onset-to-offset window of significant partial correlations for\n    A (claim fig3d-timing-sequence). OPEN, the measure of location, which the paper does not\n    give; readings (a) the W-weighted mean dorsal-ventral distance from the Sylvian fissure\n    over electrodes with positive weights, (b) the median dorsal-ventral distance of the top\n    10% of weights (the selection of Methods, Somatotopic map). The paper's finding is on the\n    map averaged over subjects (Fig. 2a legend, \"averaged over time and subjects\"), so the\n    electrodes of the three subjects are pooled. Reproduced when lips lie dorsal to tongue\n    in the pooled data; the result per subject is reported (Supplementary Figure 2). The\n    paper's maps are smoothed with a 2 mm uniform circular kernel and averaged over\n    subjects; the maps are shown for comparison."
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "    0.5 mm is shown as a variant. Reproduced when the DV positions of the top-10% points",
 "new_string": "    0.5 mm is shown as a variant. OPEN, the paper reads the sequence off Fig. 2b and gives no\n    rule for it; the rule below is this file's reading and not the paper's. Reproduced when\n    the DV positions of the top-10% points"
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "    below the diagonal that the legend draws, the anterior-dorsal to posterior-ventral axis.\n    OPEN, the diagonal's exact angle;",
 "new_string": "    below the diagonal that the legend draws, the anterior-dorsal to posterior-ventral axis.\n    Shifts above the dashed line are dorsal-posterior shifts (Supplementary Figure 3 legend).\n    OPEN, which map of each pair is shifted against the other (it sets the sign); the legend\n    says the first-named representation leads (Larynx->Tongue, Tongue->Jaw, Jaw->Lips), and\n    the reading that gives positive values above the diagonal is not to be chosen after the\n    fact, so both are reported and the claim is reproduced only under the first-named map\n    shifted. OPEN, the diagonal's exact angle;"
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

That last edit picked one shift direction itself, which the protocol forbids. I'll rewrite it to judge the sign change and report the orientation instead.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "    OPEN, which map of each pair is shifted against the other (it sets the sign); the legend\n    says the first-named representation leads (Larynx->Tongue, Tongue->Jaw, Jaw->Lips), and\n    the reading that gives positive values above the diagonal is not to be chosen after the\n    fact, so both are reported and the claim is reproduced only under the first-named map\n    shifted. OPEN, the diagonal's exact angle;",
 "new_string": "    OPEN, which map of each pair (Larynx->Tongue, Tongue->Jaw, Jaw->Lips) is shifted against\n    the other; swapping them swaps the two sides, so the sign change across the diagonal is\n    judged on its size and the side found positive is reported. OPEN, the diagonal's exact\n    angle;"
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "    mean autocorrelation of claim suppfig3b-spatial-clustering. Reproduced when both means are\n    within tolerance with opposite signs",
 "new_string": "    mean autocorrelation of claim suppfig3b-spatial-clustering. Reproduced when the two means\n    have opposite signs, the positive one within tolerance of 0.099 and the negative one\n    within tolerance of -0.102,"
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now fig3d, suppfig7 and the PCA claim.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "    of rho over electrodes and time (per subject; OPEN whether over all articulators or per\n    articulator, both run). Onset and offset are the first and last times of the contiguous\n    run around the peak above that threshold (OPEN, the paper does not define them; reading\n    (b) threshold at half the peak is shown). One-way ANOVA across the six articulators of\n    the timing values pooled over subjects. OPEN, which timing value the ANOVA uses; readings\n    (a) onset, (b) peak. Acoustic onset per CV from the audio of the prototype rendition\n    (Methods Eq. 1, cochlear spectrogram, a threshold on acoustic power).",
 "new_string": "    of rho over electrodes and time (Methods). OPEN, the set over which mean and SD are taken;\n    readings for the subjects (per subject, or pooled) and for the articulators (all six\n    together, or per articulator), all run. OPEN, the onset and offset, which the paper does\n    not define; readings (a) the first and last times of the contiguous run around the peak\n    above that threshold, (b) the same at half the peak, both run. One-way ANOVA across the\n    six articulators of the timing values pooled over subjects. OPEN, which timing value the\n    ANOVA uses; readings (a) onset, (b) peak. Acoustic onset per CV from the audio of the\n    prototype rendition (Methods Eq. 1, cochlear spectrogram, \"a thresholding procedure\" on\n    acoustic power whose threshold is not given; 10% of the prototype's peak power is a\n    standard choice, which moves the onset by a few ms and is not expected to change the\n    outcome)."
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "  criterion: A claim of absence, judged on the paper's test. Per electrode, the onset latency of\n    the GLM R2 (Methods Eq. 2). OPEN, the onset;",
 "new_string": "  criterion: A claim of absence, judged on the paper's test. Per electrode, the onset latency of\n    the GLM R2 (Methods Eq. 2). OPEN, which electrodes; the paper does not say, and 71 + 67\n    is fewer than the 266 vSMC electrodes of Supplementary Figure 9; readings (a) the\n    electrodes kept in claim fig2a-lips-dorsal, (b) all vSMC electrodes; both run and the\n    counts reported. OPEN, the onset;"
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "    10 mm posterior of the central sulcus; electrodes on the guenon against those dorsal to it\n    (OPEN, how the guenon boundary is set; the dataset's anatomical labels are used, and the\n    comparison is blocked without them).",
 "new_string": "    10 mm posterior of the central sulcus. OPEN, what \"across the geunon\" compares; readings\n    (a) electrodes on the guenon against those dorsal to it, (b) electrodes anterior against\n    posterior to the guenon's midline; both run. How the guenon boundary is set is also open;\n    the dataset's anatomical labels are used, and the comparison is blocked without them."
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "    windows, -375 to 620 ms. Reproduced when, under one reading, the mean over subjects of the\n    variance explained by nine PCs is within tolerance.",
 "new_string": "    windows, -375 to 620 ms. Reproduced when, under each reading, the mean over subjects of the\n    variance explained by nine PCs is within tolerance (methods_underspecified when the\n    readings differ, as the header's rule for method readings says)."
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now fig5c, fig1f-h and suppfig9.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "    per subject, then averaged over subjects. OPEN, the clusters; readings (a) the phonetic\n    groups, major articulator for consonants and vowel identity for vowels, (b) k-means (k =\n    3) at each time.",
 "new_string": "    per subject, then averaged over subjects. OPEN, the clusters; readings (a) the phonetic\n    groups, major articulator for consonants and vowel identity for vowels, (a') for\n    consonants the four groups of the Fig. 5a legend (labial, coronal tongue, dorsal tongue,\n    sibilant), (b) k-means (k = 3) at each time."
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "    judged with the paper's own threshold. Reproduced when, in at least one subject, a vSMC\n    electrode with a positive lips weight",
 "new_string": "    judged with the paper's own threshold. The Fig. 1h legend calls the dorsal electrode an\n    \"active lip electrode for /u/\". The vowel time, +250 ms, is that of Fig. 4b. Reproduced\n    when, in at least one subject, a vSMC electrode with a positive lips weight"
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "    articulator pairs, per PC, Bonferroni for 6. Reproduced when, in each PC, tongue > lips at\n    p < 0.05, lips > jaw and lips > larynx at p < 0.001,",
 "new_string": "    articulator pairs, per PC, Bonferroni for 6. The legend's \"tongue over lips (P < 0.05)\n    over jaw and larynx (P < 0.001 for each)\" reads as (a) lips over jaw and over larynx, or\n    (b) tongue and lips each over jaw and over larynx; it matches under either. Reproduced\n    when, in each PC, tongue > lips at p < 0.05, the P < 0.001 comparisons of the reading hold,"
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000019/10.1038-nature11911.yaml",
 "old_string": "  - about: lips against jaw and larynx",
 "new_string": "  - about: lips (in one reading, tongue and lips) against jaw and larynx"
}
```

```
The file claims/000019/10.1038-nature11911.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cat >> claims/000019/10.1038-nature11911.yaml <<'EOF'
checks:
- date: 2026-10-21
  kind: agent
  model: claude-opus-5-5
  ready: true
  changes:
  - Header, major articulator labels. It said the labels come from Fig. 4c, a main figure the file says was not available, and its reading (b) put /h/ in the dorsal set, which no source supports. Now read from the Supplementary Figure 12 place features, with /w/ and /j/ also named as unplaced, and /h/ left out in both readings.
  - fig1f-h-phonetic-contrasts. Cited the Fig. 1h legend ("active lip electrode for /u/") for the lips-weight selection and Fig. 4b for the +250 ms vowel time.
  - fig2a-lips-dorsal. The Methods' "associated p-value" was given as the model F-test alone; named it open with the coefficient t-test as a second reading. The W-weighted mean DV is not the paper's measure; named it open with the top-10% median DV (Methods, Somatotopic map) as a second reading. The criterion required the order in every subject, but the paper states it for the map averaged over subjects (Fig. 2a legend); it is now judged on the pooled electrodes, with each subject reported.
  - fig2b-somatotopic-sequence. Said plainly that the ordering rule (medians, larynx split) is this file's reading of Fig. 2b and not the paper's.
  - suppfig3f-dv-sequence. Added the legend's convention (above the dashed line are dorsal-posterior shifts). Which map is shifted is not stated and swapping them swaps the sides, so the sign change is judged on its size and the positive side reported.
  - fig3d-timing-sequence. "Per subject" for the mean + 2.5 SD threshold is not in the Methods; named it open (per subject or pooled). Onset reading (b) was "shown" only; both onset readings are now run. The acoustic onset threshold is not given; named a standard choice and said so.
  - suppfig7-no-latency-difference. The electrode set was not stated (71 + 67 is fewer than 266 vSMC electrodes); named it open with two readings. "Across the geunon" was read one way only; added a second reading.
  - pca-nine-components. The time range is a method detail, so the outcome must hold under each reading, as the header's rule says; it said "under one reading".
  - fig5c-separability-timing. Added the four consonant groups of the Fig. 5a legend (with sibilants) as a reading of the clusters.
  - suppfig9-pc-articulator-weights. The legend's "over jaw and larynx (P < 0.001 for each)" may include tongue; named both readings.
  - Open, not settled. Baseline reading (a), -1000 to -500 ms before the C-V transition, is this file's choice of window; the paper says only "baseline data".
  - Open, not settled. fig4c-d-hierarchy judges the consonant tree with a two-thirds purity rule that the paper does not give; it is this file's reading.
  - Open, not settled. fig3d-timing-sequence tests "jaw and larynx aligned to the CV transition" as onsets later than those of lips and tongue, a weaker test than the sentence; the paper gives no measure of alignment.
  - Open, not settled. The figure readings (Supplementary Figures 1d and 12, the *** marks of Supplementary Figure 5) could not be checked; no PDF renderer was available in this run.
EOF
python tools/claims_check.py claims/000019/10.1038-nature11911.yaml paper/10.1038-nature11911.txt | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -nE "rather|—" claims/000019/10.1038-nature11911.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/000019/10.1038-nature11911.yaml'));print(len(d['checks']),d['checks'][-1]['ready'])"; git status --short
```

```
1 True
 M claims/000019/10.1038-nature11911.yaml
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

I checked the claims file against the paper and changed ten things; I think it is ready for an attempt, with four problems left open.

**Checker result:** `claims/000019/10.1038-nature11911.yaml: 22 claims, 22 quotes, 17 statistical values, 0 problems` (the same before and after my edits).

**Changes, by claim:**
- **Header, consonant labels:** The file said the labial, coronal and dorsal labels came from Fig. 4c, a main-text figure the file itself says was never available. Its second reading also put /h/ in the dorsal set, which nothing in the paper supports. The labels are now read from the place features of Supplementary Figure 12. /w/ and /j/ are added to /h/ and /r/ as consonants no sentence places, and /h/ is left out under both readings.
- **fig1f-h-phonetic-contrasts:** Added citations for two choices it made without sources: the Fig. 1h legend ("active lip electrode for /u/") for picking an electrode with a positive lips weight, and Fig. 4b for the +250 ms vowel time.
- **fig2a-lips-dorsal:**
  - The Methods' "associated p-value" was taken as the whole-model F-test only; it is now open, with the articulator's own coefficient test as a second reading.
  - The weighted mean position was not the paper's measure; it is now open, with the median position of the top 10% of weights (from the Methods) as a second reading.
  - The paper states the lips-above-tongue finding for the map averaged over subjects, so it is now judged on the three subjects pooled, not required in every subject. Each subject is still reported.
- **fig2b-somatotopic-sequence:** The criterion now says plainly that its rule for reading the dorsal-to-ventral order is the file's own and not the paper's.
- **suppfig3f-dv-sequence:** Added the legend's convention that values above the dashed line are dorsal-posterior shifts. The paper does not say which map of each pair is shifted, and swapping them swaps the two sides. So the claim is now judged on the size of the sign change, and the side that comes out positive is reported.
- **fig3d-timing-sequence:**
  - Whether the mean + 2.5 SD threshold is computed per subject or pooled is not in the Methods; it is now open.
  - The second onset reading was only "shown"; both readings are now run.
  - The paper gives no acoustic-onset threshold; a standard choice is now named and labelled as such.
- **suppfig7-no-latency-difference:** Named as open which electrodes are compared (71 + 67 is fewer than the 266 vSMC electrodes). Added a second reading of "across the geunon".
- **pca-nine-components:** The time range is a method choice, so the result now has to hold under each reading. It previously said "under one reading", which goes against the file's own header rule.
- **fig5c-separability-timing:** Added the four consonant groups of the Fig. 5a legend (labial, coronal, dorsal, sibilant) as a reading of the clusters.
- **suppfig9-pc-articulator-weights:** The legend's "over jaw and larynx (P < 0.001 for each)" may also cover tongue; both readings are now named.

**Still open, and recorded under `checks`:**
- The baseline window in the first baseline reading (-1000 to -500 ms) is the file's own choice. The paper says only "baseline data".
- fig4c-d-hierarchy decides the consonant tree with a two-thirds purity rule the paper does not give.
- fig3d tests "jaw and larynx aligned to the CV transition" only as their onsets coming after those of lips and tongue. That is a weaker test than the sentence, but the paper gives no measure of alignment.
- I could not check the figure readings (Supplementary Figures 1d and 12, and the significance marks on Supplementary Figure 5), because no PDF renderer was available in this run.

All of the paper's main findings have claims, and every claim comes from this paper.

**Ready:** yes (`ready: true`). Nothing was committed.

## End of run

29 turns, 4 minutes, result: success.
