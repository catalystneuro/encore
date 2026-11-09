# 001193 · claims · run 39820388025

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/; ls claims/001193 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md
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
cat claims/001453/*.yaml; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41562-022-01334-6.txt",
 "offset": 30,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41562-022-01334-6.txt",
 "offset": 729,
 "limit": 1110
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls claims/ | head -50; ls claims/001195 claims/001199; sed -n 1,60p claims/001199/*.yaml; curl -s https://api.dandiarchive.org/api/dandisets/001193/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m['name']);print(m.get('description'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 60,200p claims/001199/*.yaml; sed -n 1,40p tools/claims_check.py
```

```
#   averaged over each unit's spikes ("For each identified spike"), and whether k-means runs on all
#   units pooled or per area. If the dataset holds the authors' RSU and FSU labels, those are the
#   paper's classification and are used, with the re-clustering under each reading of U2 as a variant.
#   AC neurons are not split by type in the paper (Fig. 11A, 11B).
# R, normalized spiking rate. Rate in a window divided by the rate in the 67 ms before sonication onset,
#   in percent (Methods; Statistical analysis). Open, (R1) per unit, the trial-averaged rate in the
#   window over the trial-averaged prestimulus rate; (R2) per trial, window over prestimulus rate, then
#   averaged over trials, trials with no prestimulus spike left out. Units with no prestimulus spike in
#   any trial are left out under both. Group values are mean +/- SEM over units (Fig. 4, 5 legends).
# W, windows. During sonication 0 to 67 ms; postsonication 201 to 268 ms (Results, tFUS parameters,
#   paragraph 1; Fig. 6 to 9 legends). Fig. 4 reports windows of 67 ms after onset (67–134 ms, 134–268
#   ms, "from 134 ms"); the readings for Fig. 4 are consecutive 67 ms windows from 0 ms, the claim
#   holding when the effect is found in at least one window inside the range the paper names. PSTH bins
#   of 50 ms are for display only (Fig. 3).
# T, response test. Kruskal-Wallis H test across the groups of a panel, then post hoc one-tailed
#   two-sample Wilcoxon (rank-sum) tests with Bonferroni correction, significance at 0.01 for spiking
#   (Methods, Statistical analysis; Fig. 4 and 5 legends). A response "compared with baseline" is a
#   one-tailed rank-sum test of the window against the prestimulus window, in the direction stated
#   (above baseline for an activation, below for an inhibition). Open, (T1) the two samples are the
#   units' window rates and prestimulus rates in spikes/s; (T2) the two samples are the units'
[... 159 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/claims.schema.json'));import pprint;c=s['properties']['claims']['items'] if 'items' in s['properties']['claims'] else s;print(json.dumps(c,indent=0)[:3000])"; grep -n '"\$defs"\|"definitions"' schemas/claims.schema.json
```

```
{
"type": "object",
"additionalProperties": false,
"required": [
"id",
"statement",
"source"
],
"properties": {
"id": {
"description": "Stable within the file, e.g. fig2b.",
"type": "string",
"pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"
},
"statement": {
"description": "The finding in one or two sentences, in words. Not a copy of the figure.",
"type": "string",
"minLength": 1
},
"source": {
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=0)[:2500])"
```

```
{
"expected": {
"type": "object",
"additionalProperties": false,
"required": [
"quantity",
"value"
],
"properties": {
"quantity": {
"type": "string"
},
"value": {
"type": "number"
},
"tolerance": {
"type": "number",
"minimum": 0
},
"unit": {
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1038-s41562-022-01334-6.pdf')
for i in [2,4]:
    d[i].get_pixmap(dpi=130).save(f'p{i+1}.png')
s=fitz.open('paper/10.1038-s41562-022-01334-6.supp.pdf')
for i in [8,9,11,12]:
    s[i].get_pixmap(dpi=90).save(f's{i+1}.png')
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41562-022-01334-6.pdf",
 "pages": "3"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/001193/10.1038-s41562-022-01334-6.yaml",
 "content": "# Claims for Zhu, Xu, Lu, Hu et al. (2022), Nature Human Behaviour 6, 1104-1111, on dandiset 001193.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, under\n# docs/protocol.md, version pilot-10.\n#\n# Text read: the version of record (paper/10.1038-s41562-022-01334-6.txt, from the publisher PDF\n# supplied by hand), with main text, figure legends, Methods and reporting summary, and the\n# Supplementary Information PDF (Supplementary Table 1, Supplementary Figures 1 to 10 and the list of\n# stimulus sentences). The Supplementary Excel file and the Source Data named in the paper were not\n# supplied; nothing below needs them except where said. Figure panels were not viewed (the PDF could\n# not be rendered here), so numbers printed only inside panels (the region counts of the Fig. 2b Venn\n# diagram) are not used.\n#\n# Code. The paper links no code: \"The completely developed code that operates on the full data set\n# will be made available from the authors upon reasonable request\" (Code availability). No repository\n# was read. Every method detail below is from the Methods, the figure legends or the supplement.\n#\n# Which dataset. The dandiset's title and description say it holds high-gamma (70-150 Hz) ECoG activity\n# from the paper's syntactic and semantic tasks in the inferior frontal gyrus, in NWB. Claims that need\n# other frequency bands (Fig. 1b, Supplementary Figs. 3, 4 and 7c) cannot be tested on high-gamma alone.\n#\n# Data the paper used (Results, paragraph 1; Methods, Participants, Stimuli design, Neural data\n# acquisition; Supplementary Table 1).\n# - Subjects. Ten native Mandarin speakers (4 male, 6 female, 19 to 50 years) in awake brain tumour\n#   surgery at Huashan Hospital. Two 128-channel high-density grids each (256 electrodes), over the\n#   left IFG and the left MFG or STG. Analyses use IFG electrodes only.\n# - Task. Written Chinese sentences, one word at a time: 800 ms fixation, 500 ms blank, each word 400 ms\n#   with a 100 ms interval; then a correctness judgement by button press (up to 3 s). Four blocks,\n#   each sentence shown once in random order. Conditions, 32 sentences each (supplement list): CORR\n#   (correct, 6 words), SYN-P (degree adverb before the object noun, 7 words), SYN-C (object noun\n#   replaced by an adjective, 6 words), SEM (verb's selectional restriction violated, 6 words), all ten\n#   participants. COM (SYN-P and SEM combined, 7 words), participants given in the text only as \"five\n#   participants\". NL, the other five: sequences of geometric shapes, changed (NL-VIO) or not (NL-CORR),\n#   with the number of shapes matched to the number of words. The keyword is the first object noun\n#   (the adjective in SYN-C): word 4 in CORR, SYN-C and SEM, word 5 in SYN-P and COM.\n# - Signals. TDT recording at 3,052 Hz, reference on the skull at Cz; bad channels and bad intervals\n#   excluded; downsampled to 400 Hz, notch at 50, 100, 150 Hz, common average reference per bank of 64\n#   channels. High-gamma activity (HGA), the first principal component of Hilbert amplitudes in eight\n#   bands from 70 to 150 Hz, downsampled to 100 Hz and z-scored within each block. Electrode\n#   coordinates on the MNI152 template and FreeSurfer anatomical labels.\n# - Behaviour. Button responses and response times (Supplementary Fig. 2b, 2d).\n#\n# Shared method. Criteria refer to these by letter. Each detail is from the place cited; a detail the\n# paper does not fix is named as open, with the readings its text allows, and the criterion holds when\n# all readings give the same outcome (otherwise the claim is blocked as methods_underspecified).\n# H, signal. The dataset's HGA. If it is not already z-scored within each block, z-score it so\n#   (Methods, Frequency component extraction, paragraph 2). Trials are aligned to keyword onset as T0\n#   (Methods, ERP amplitude), from the event times the dataset gives.\n# E, responsive IFG electrodes. Electrodes labelled pars opercularis or pars triangularis (FreeSurfer\n#   labels) whose response differs between resting state and stimuli by a one-way ANOVA (scipy\n#   f_oneway) at p < 0.01 (Methods, Electrode selection). Fig. 3d also includes precentral electrodes\n#   (\"n = 106, electrodes in pars opercularis, pars triangularis and precentral\"); E+ is E with the\n#   precentral gyrus added. Open, (E1) what \"resting state\" is: (a) the 800 ms fixation before the\n#   sentence, or (b) the fixation and the 500 ms blank (1,300 ms); the stimulus period is the sentence's\n#   word presentation. (E2) what is compared: per trial the mean HGA in the rest period against per\n#   trial the mean HGA in the stimulus period, the trials of all linguistic conditions pooled (the NL\n#   task for NL electrodes). No uncorrected or corrected alternative is named; p < 0.01 as printed.\n# V, violation electrodes. An electrode of E is a SYN-P, SYN-C or SEM (or COM) electrode when its HGA\n#   for that violation is reliably higher than for CORR: at each 10 ms sample after T0, a one-way ANOVA\n#   (f_oneway) over trials of the violation against CORR, two-tailed, p < 0.05/256 (Bonferroni for the\n#   256 electrodes of a participant), significant for more than 50 ms, with amplitude above 0.55 z\n#   (Methods, Electrode selection, paragraph 3; ERP amplitude; Results, paragraph 5). The violation\n#   mean must be above the CORR mean at the significant samples (\"reliably higher\"). Open, (V1) \"more\n#   than 50 ms\" as (a) a run of at least 6 consecutive significant samples, or (b) at least 6\n#   significant samples in total; (V2) \"> 0.55 z score in amplitude\" as (a) the violation's mean HGA\n#   above 0.55 z at some significant sample, or (b) the violation minus CORR difference above 0.55 z at\n#   some significant sample. The window is 0 to 1,000 ms after T0, the extent of every keyword-locked\n#   figure (Fig. 1e, 2a, 3b, 3c); the paper names no other.\n# F, F value. The F statistic of the one-way ANOVA of the violation against CORR for an electrode\n#   (Fig. 2b legend). An electrode \"strongly responded\" to a violation when F > 4 (Results, paragraph\n#   5). Open, (F1) the maximum F over samples 0 to 1,000 ms; (F2) the mean F over the electrode's\n#   significant samples; (F3) the F of the trial-wise mean HGA over 0 to 1,000 ms.\n# L, latencies. Onset, peak and offset are the times at which 10%, 50% and 90% of the area of the\n#   keyword-locked mean response is reached (fractional area latency; Methods, ERP amplitude). Open,\n#   (L1) the response is (a) the violation's trial-mean HGA or (b) the violation minus CORR difference;\n#   (L2) the area is taken over (a) 0 to 1,000 ms or (b) the electrode's discriminating period (its\n#   significant samples under V, first to last); (L3) negative values are (a) set to zero or (b) kept.\n#\n# Data. Every claim uses the dataset alone unless it says otherwise. The paper uses no outside data,\n# except the word frequency corpus of the stimulus check (lingua.mtsu.edu/chinese-computing).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001193\"\npaper: doi:10.1038/s41562-022-01334-6\nclaims:\n- id: participants\n  statement: Ten participants (four male, six female, 19 to 50 years) were recorded with two\n    128-electrode grids each; all ten did the CORR, SYN-P, SYN-C and SEM conditions, five of them the\n    combined violation (COM) and the other five the non-linguistic task (NL).\n  source: Methods, Participants, paragraph 1, and The Chinese language and stimuli design, paragraph 3;\n    Supplementary Table 1\n  quote: This study included ten participants (age range, 19–50 years; four males, six females) ...\n    All the ten participants performed under CORR, SYN-P, SYN-C and SEM conditions. Five participants\n    performed under COM and the other five performed under NL conditions.\n  expected:\n  - {quantity: participants, value: 10, tolerance: 0}\n  - {quantity: male participants, value: 4, tolerance: 0}\n  - {quantity: female participants, value: 6, tolerance: 0}\n  - {quantity: participants with COM, value: 5, tolerance: 0}\n  - {quantity: participants with NL, value: 5, tolerance: 0}\n  - {quantity: electrodes per participant, value: 256, tolerance: 0}\n  criterion: Counts of distinct subjects in the dataset, their sex, and the tasks each has. Tolerance\n    zero, as these are counts the paper gives exactly. Reproduced when all match; partially reproduced\n    when the dataset holds a subset of the participants with matching metadata. Ages are compared with\n    Supplementary Table 1 (30, 39, 19, 30, 50, 34, 42, 36, 40, 31 for participants 1 to 10) where the\n    dataset gives them.\n- id: task-structure\n  statement: Each of the CORR, SYN-P, SYN-C, SEM and COM conditions has 32 sentences, with six words per\n    sentence in CORR, SYN-C and SEM and seven in SYN-P and COM, each word shown for 400 ms with a 100 ms\n    interval after an 800 ms fixation and a 500 ms blank.\n  source: Methods, The Chinese language and stimuli design, paragraph 4; Supplementary Information,\n    stimulus sentence lists\n  quote: Each trial started with an 800 ms fixation followed by a 500 ms blank screen, and then each\n    word of the sentence (or geometric shape) was displayed for 400 ms, with a 100 ms interstimulus\n    interval. There were six words per sentence in the CORR, SYN-C and SEM conditions and seven words\n    in the SYN-P and COM conditions.\n  expected:\n  - {quantity: sentences per condition, value: 32, tolerance: 0}\n  - {quantity: words per sentence in CORR, SYN-C and SEM, value: 6, tolerance: 0}\n  - {quantity: words per sentence in SYN-P and COM, value: 7, tolerance: 0}\n  - {quantity: word duration, value: 400, tolerance: 10, unit: ms}\n  - {quantity: word onset to next word onset, value: 500, tolerance: 10, unit: ms}\n  criterion: The 32 sentences per condition are read from the numbered lists in the supplement (no\n    sentence of the text gives the count). Per participant, the number of trials of each condition\n    (before bad-interval exclusion, where the dataset says which were excluded) and the word timing\n    from the event times. The timing tolerance of 10 ms is one sample of the 100 Hz HGA. Reproduced\n    when every count matches and the timings are within tolerance in every participant; partially\n    reproduced when they do in some.\n- id: behaviour-response-time\n  statement: Participants responded fast and accurately in the linguistic task, most response times\n    lying around 0.5 to 1.0 s.\n  source: Results, paragraph 1; Supplementary Figure 2b legend\n  quote: Most of the responding time is around 0.5-1.0 second.\n  expected:\n  - {quantity: lower bound of the usual response time, value: 0.5, tolerance: 0.05, unit: s}\n  - {quantity: upper bound of the usual response time, value: 1.0, tolerance: 0.1, unit: s}\n  criterion: Response times of the linguistic trials of all ten participants pooled, measured from the\n    onset of the question as the dataset times it. The paper gives no measure of \"most\"; the reading\n    taken is that more than half of the response times lie in the range widened by 10% of each bound\n    (0.45 to 1.1 s), and no other is named in the text. Accuracy is reported (proportion of correct\n    judgements per participant) but has no number to match. Reproduced when more than half lie in the\n    range.\n- id: fig1b-high-gamma-best-band\n  statement: High-gamma components above 70 Hz classify the linguistic conditions with the highest\n    accuracy (above 80%), and the evoked responses are more prominent in the 70 to 150 Hz band than in\n    other bands.\n  source: Results, paragraph 3; Figure 1b; Supplementary Figure 3a to 3e\n  quote: Results showed that high-gamma (HG) components (>70 Hz) discriminated conditions with the\n    highest accuracy (>80%, Fig. 1b and Supplementary Fig. 3a) and ERPs were more prominent in the HG\n    band (70–150 Hz) compared with other frequency bands\n  expected:\n  - {quantity: best classification accuracy, value: 0.8, tolerance: 0.08}\n  criterion: Needs the broadband signal, from which the analytic amplitude of bands from 0 to 150 Hz in\n    10 Hz steps is taken as the first principal component across band-passes, and classified with the\n    SVM, logistic regression and k-nearest-neighbour settings of the Methods (Frequency component\n    extraction) into correct, syntactic violation, semantic violation and resting state. If the dataset\n    holds only high-gamma activity, as its description says, the claim cannot be tested. Otherwise,\n    open, the cross-validation and the features (time samples of the band amplitude in the keyword\n    window); reproduced when, under every classifier, a band with lower bound at or above 70 Hz gives\n    the highest accuracy and it exceeds 0.72 (80% less the tolerance).\n- id: fig1c-responsive-in-ifg\n  statement: Most electrodes showing enhanced activity to linguistic stimuli lie in the IFG.\n  source: Results, paragraph 3; Figure 1c; Supplementary Figure 3f\n  quote: Most of the electrodes showing enhanced activities to linguistic stimuli were located in the\n    IFG\n  criterion: The rest against stimulus test of E (with readings E1a and E1b) applied to every electrode\n    of every participant, regardless of location, with HGA higher during stimuli. Reproduced when more\n    than half of the responsive electrodes carry an IFG label. Open, which labels form the IFG, (a)\n    pars opercularis and pars triangularis, the labels of E, or (b) these and pars orbitalis.\n- id: fig1d-only-after-keyword\n  statement: The enhanced activity for violation conditions relative to CORR appears only after the\n    keyword.\n  source: Results, paragraph 3; Figure 1d\n  quote: In the linguistic task, the enhanced activity of violation conditions relative to CORR was only\n    observed after the keywords, indicating that the responses were highly linked to the violation\n    manipulations (Fig. 1d).\n  depends_on:\n  - fig2b-violation-electrodes\n  criterion: For the electrodes of E, the test of V applied to the sentence before the keyword, aligned\n    to the first word, over the words shared by CORR and each violation (words 1 to 3, 0 to 1,500 ms;\n    the SEM verb, word 2, differs, so for SEM words 1 and 3 only, as samples 0 to 500 ms and 1,000 to\n    1,500 ms). The paper gives no count; \"only\" is read as at most as many electrodes passing V before\n    the keyword as the 5% expected by chance at the paper's alpha, relative to the number passing after\n    it (claim fig2b-violation-electrodes). Reproduced when the number of electrode and condition pairs\n    passing before the keyword is no more than 5% of those passing after it. The counts are reported.\n- id: fig2b-violation-electrodes\n  statement: 58 IFG electrodes respond to at least one violation type more strongly than to correct\n    sentences.\n  source: Results, paragraph 5; Figure 2b\n  quote: we defined a significant effect in each electrode if its response to a certain type of\n    violation was reliably enhanced compared with the CORR condition for more than 50 ms (P < 0.05,\n    ANOVA, two tailed, Bonferroni correction for the number of electrodes, n = 256 for each\n    participant); there were 58 electrodes satisfying this criterion\n  expected:\n  - {quantity: electrodes passing V for SYN-P, SYN-C or SEM, value: 58, tolerance: 5.8}\n  criterion: Electrodes of E (readings E1a, E1b) passing V (readings V1a, V1b, V2a, V2b) for at least\n    one of SYN-P, SYN-C and SEM, over the ten participants. Reproduced when the count is within\n    tolerance under at least one combination of readings (a count that a reading can move is a\n    reported number read in more than one way, so any reading may match); not reproduced when none\n    is. The count under every combination is reported.\n- id: fig2b-single-type\n  statement: Most responding electrodes (49 of 58) respond strongly to only one violation type; few (9\n    of 58) are co-activated by two types, mainly SYN-P and SYN-C.\n  source: Results, paragraph 5; Figure 2b\n  quote: We found that most of the electrodes (49 of 58) strongly responded to only one type of\n    violation (Fig. 2b, one-way ANOVA F statistic > 4). Only a few electrodes were co-activated by two\n    violation types (9 of 58) and were mainly co-activated by SYN-P and SYN-C\n  expected:\n  - {quantity: electrodes strongly responding to one type, value: 49, tolerance: 4.9}\n  - {quantity: electrodes co-activated by two types, value: 9, tolerance: 0.9}\n  depends_on:\n  - fig2b-violation-electrodes\n  criterion: Among the electrodes of fig2b-violation-electrodes, an electrode strongly responds to a\n    violation when its F (readings F1, F2, F3) exceeds 4. Counts of electrodes strongly responding to\n    exactly one, and to two, of the three types. Reproduced when, under one combination of readings,\n    both counts are within tolerance and the SYN-P and SYN-C pair is the most frequent pair among the\n    co-activated electrodes; partially reproduced when the single-type electrodes are a majority and\n    SYN-P with SYN-C is the most frequent pair, but the counts are outside tolerance under every\n    reading. The 10% tolerance on 9 is below one electrode, so the second count must match exactly.\n- id: suppfig6a-half-split\n  statement: When half of the sentences select the responding electrodes and the other half are\n    analysed, most electrodes (46 of 62) still respond to one violation type only and 16 of 62 to two,\n    mainly SYN-P and SYN-C.\n  source: Results, paragraph 5; Supplementary Figure 6a legend\n  quote: We used first half sentences to identify the linguistic responding electrodes and used the\n    remaining sentences for further analysis, to resolve non-independence issue. We found that most of\n    the electrodes (46/62) strongly responded to only one type of violation (below figure). Only a few\n    electrodes were co-activated by two violation types (16/62) and were mainly co-activated by SYN-P\n    and SYN-C\n  expected:\n  - {quantity: responding electrodes, value: 62, tolerance: 6.2}\n  - {quantity: electrodes responding to one type, value: 46, tolerance: 4.6}\n  - {quantity: electrodes co-activated by two types, value: 16, tolerance: 1.6}\n  criterion: As fig2b-violation-electrodes and fig2b-single-type, with E and V computed on the trials of\n    the first half of the sentences and F on the remaining trials. Open, (a) \"first half\" as sentences\n    1 to 16 of each condition's list, or (b) the first half of each condition's trials in presentation\n    order. Reproduced when, under one combination of readings, all three counts are within tolerance and\n    SYN-P with SYN-C is the most frequent pair; partially reproduced when the single-type electrodes are\n    a majority and the pair is the most frequent, with counts outside tolerance.\n- id: suppfig6b-duration-metric\n  statement: When the length of the period differing from CORR is used in place of amplitude, most\n    electrodes (61 of 79) respond to one violation type only and 18 of 79 to two, mainly SYN-P and SYN-C.\n  source: Results, paragraph 5; Supplementary Figure 6b legend\n  quote: We found that most of the electrodes (61/ 79) strongly responded to only one type of violation\n    (below figure). Only a few electrodes were co-activated by two violation types (18/79) and were\n    mainly co-activated by SYN-P and SYN-C\n  expected:\n  - {quantity: responding electrodes, value: 79, tolerance: 7.9}\n  - {quantity: electrodes responding to one type, value: 61, tolerance: 6.1}\n  - {quantity: electrodes co-activated by two types, value: 18, tolerance: 1.8}\n  criterion: The paper does not say how 79 electrodes are selected or what length counts as a response.\n    Readings, (a) electrodes of E with a significant period (V, without the amplitude rule V2) of more\n    than 50 ms for a violation count as responding to it; (b) as (a) with the amplitude rule kept. The\n    length of an electrode's significant period is the number of significant samples times 10 ms.\n    Reproduced when, under one reading (crossed with V1a and V1b), all three counts are within\n    tolerance and SYN-P with SYN-C is the most frequent pair; partially reproduced when the single-type\n    electrodes are a majority and the pair is the most frequent, with counts outside tolerance.\n- id: fig2c-euclidean-similarity\n  statement: The response time courses of SYN-P and SYN-C are more similar (Euclidean distance 48.43)\n    than those of the syntactic and semantic conditions (62.17).\n  source: Results, paragraphs 5 and 6; Figure 2c\n  quote: the similarity between SYN-P and SYN-C (Euclidean distance, 48.43) was greater than that\n    between syntactic and semantic conditions (Fig. 2c, Euclidean distance, 62.17)\n  expected:\n  - {quantity: Euclidean distance SYN-P to SYN-C, value: 48.43, tolerance: 4.843}\n  - {quantity: Euclidean distance syntactic to semantic, value: 62.17, tolerance: 6.217}\n  depends_on:\n  - fig2b-violation-electrodes\n  criterion: Distances computed with scipy's hierarchical clustering on Euclidean distance (Methods,\n    Electrode selection, paragraph 3), between condition vectors built from the responding electrodes\n    of fig2b-violation-electrodes. Open, (a) each condition's vector is the trial-mean HGA from 0 to\n    1,000 ms of every responding electrode, concatenated over electrodes; (b) the vector of each\n    electrode's mean HGA over 0 to 1,000 ms; and the \"syntactic to semantic\" distance read as (i) SEM\n    to SYN-P, (ii) SEM to SYN-C, (iii) the mean of the two, or (iv) the linkage height at which SEM\n    joins the SYN-P and SYN-C cluster. Fig. 2c's y axis is a \"relative distance\", so absolute values\n    depend on the vector. Reproduced when, under every reading, SYN-P to SYN-C is the smallest distance\n    and the syntactic to semantic distance is larger; the values are compared with the expected ones\n    under each reading and the matching readings named. Partially reproduced when the order holds\n    under some readings only.\n- id: suppfig7a-com-overlap\n  statement: Of the electrodes responding to the combined violation (COM), 78.3% also respond to SYN-P\n    but only 26.1% to SEM.\n  source: Results, paragraph 6; Supplementary Figure 7a\n  quote: for the electrodes responding to the combined violation condition (COM), 78.3% of them also\n    showed enhanced activity to the syntactic violation (SYN-P), but only 26.1% of them responded to the\n    semantic violation (SEM)\n  expected:\n  - {quantity: COM electrodes also responding to SYN-P, value: 0.783, tolerance: 0.0783}\n  - {quantity: COM electrodes also responding to SEM, value: 0.261, tolerance: 0.0261}\n  criterion: In the five participants with COM, electrodes of E passing V for COM against CORR (COM\n    keyword at word 5, as in SYN-P). Fractions of those that also pass V for SYN-P, and for SEM. Open,\n    whether \"responded\" to SYN-P and SEM means passing V or having F > 4 (F1 to F3), as Supplementary\n    Fig. 7a plots F values. Reproduced when both fractions are within tolerance under one reading;\n    partially reproduced when, under every reading, the SYN-P fraction exceeds the SEM fraction but\n    the values are outside tolerance.\n- id: suppfig7b-not-nonlinguistic\n  statement: The electrodes responding to linguistic violations do not respond to the non-linguistic\n    violation in the high-gamma band.\n  source: Results, paragraph 6; Supplementary Figure 7b and 7c legend\n  quote: at 70 -150 Hz, the linguistic responding electrodes were almost completely not responding to\n    the non-linguistic task\n  depends_on:\n  - fig2b-violation-electrodes\n  criterion: A claim of absence. In the five NL participants, the electrodes of fig2b-violation-electrodes\n    tested for NL-VIO against NL-CORR with the test of V, NL trials aligned to the onset of the shape\n    in the keyword's position. The paper's NL test is a one-way ANOVA at P < 0.01, corrected\n    (Supplementary Fig. 4b); the threshold read is 0.01/256 per sample, with 0.05/256 (the linguistic\n    test) as a variant. \"Almost completely not\" is read as at most 5% of those electrodes passing, the\n    rate a test at the paper's alpha allows. Reproduced when no more than 5% pass; not reproduced\n    otherwise. The count and the electrodes' NL-VIO minus NL-CORR differences are reported either way.\n- id: fig2de-no-spatial-separation\n  statement: Across participants, the activation centres and epicentres of the SYN-P, SYN-C and SEM\n    electrodes are not spatially separated in the IFG.\n  source: Results, paragraph 7; Figure 2d and 2e; Supplementary Figure 8a\n  quote: Unlike the result at the electrode level, we failed to observe a tendency of spatial\n    separation for the activation centre of syntactic and semantic conditions. Likewise, the epicentre\n    of these responses failed to show separations using a permutation test of the clusters of electrodes\n    (Fig. 2e).\n  depends_on:\n  - fig2b-violation-electrodes\n  criterion: A claim of absence, judged on the paper's test, a non-parametric permutation test of the\n    spatial segregation among SYN-P, SYN-C and SEM electrodes on the MNI152 template (Methods, Spatial\n    organization). The Methods do not give the statistic or the permutation scheme. Readings, (a) for\n    each pair of conditions, the distance between the mean MNI coordinates of their electrodes; (b)\n    the distance between the peaks of their kernel density estimates (bandwidth 20, as the Methods\n    give, in mm); in both, condition labels permuted among the electrodes of the pair 1,000 times (the\n    permutation count the Methods give for ALE), two-sided, p < 0.05. Co-activated electrodes count in\n    each of their conditions. Reproduced when no pair is significant under every reading; not\n    reproduced when a pair is under every reading; blocked otherwise. The distances are reported. The\n    ALE analysis (GingerALE) is not repeated.\n- id: suppfig8b-individual-no-separation\n  statement: Even within individual participants the SYN-P, SYN-C and SEM electrodes show no clear\n    spatial separation.\n  source: Results, paragraph 7; Supplementary Figure 8b\n  quote: However, even at the individual level, we were unable to obtain a clear separation pattern\n    (Supplementary Fig. 8b).\n  depends_on:\n  - fig2b-violation-electrodes\n  criterion: The paper shows one representative participant and reports no test. The test of\n    fig2de-no-spatial-separation, reading (a), run per participant on native or MNI coordinates, for\n    pairs of conditions with at least three electrodes each. Reproduced when no participant has a pair\n    significant at p < 0.05 uncorrected; partially reproduced when at most one of the testable\n    participants has; not reproduced otherwise.\n- id: fig2f-circuit-diameter\n  statement: From the fraction of co-activated electrodes, the diameter of the functional circuits is\n    estimated as no greater than about 3.25 mm.\n  source: Results, paragraph 8; Figure 2f; Methods, Functional circuit size estimation\n  quote: The results showed that the diameter of functional circuits was no greater than ~3.25 mm (Fig.\n    2f)\n  expected:\n  - {quantity: functional circuit diameter, value: 3.25, tolerance: 0.325, unit: mm}\n  depends_on:\n  - fig2b-single-type\n  criterion: The Methods give p(co-activation) = 1 - (r - 0.5 mm)/r for an electrode of radius 0.5 mm\n    and a circuit of diameter r, so r = 0.5 mm / p. p is the fraction of co-activated electrodes from\n    fig2b-single-type (9 of 58 gives 3.22 mm, matching the paper's 15.6% and 3.25 mm on Fig. 2f).\n    Reproduced when r from the dataset's fraction is within tolerance under a reading that also\n    reproduces fig2b-single-type, or under any reading if none does.\n- id: suppfig9-predict-from-corr\n  statement: Electrode types (SYN-P, SYN-C, SEM, non-responding) can be predicted from responses to\n    correct sentences above the 25% chance level, with accuracies of 45.6%, 73.0%, 69.3% and 38.4%.\n  source: Results, paragraph 9; Supplementary Figure 9 legend; Methods, Predicting different types of\n    electrodes\n  quote: our data showed the predicted electrode types with accuracies significantly higher than chance\n    level (SYN-P 45.6%, SYP-C 73.0%, SEM 69.3%, and not-responding electrodes 38.4%; all P < 0.0001\n    relative to chance level 25%, Supplementary Fig. 9)\n  statistics:\n  - about: each class accuracy against chance level 25%\n    test: two-sided t-test\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - {quantity: SYN-P accuracy, value: 0.456, tolerance: 0.0456}\n  - {quantity: SYN-C accuracy, value: 0.73, tolerance: 0.073}\n  - {quantity: SEM accuracy, value: 0.693, tolerance: 0.0693}\n  - {quantity: non-responding accuracy, value: 0.384, tolerance: 0.0384}\n  depends_on:\n  - fig2b-single-type\n  criterion: k-nearest neighbours (Supplementary Fig. 9 legend) with the settings of the Methods (5\n    neighbours, Minkowski p = 2, uniform weights), features from the CORR response of each electrode\n    only, onset, offset, peak (L), area and amplitude at T0 (Methods). Open, (a) the electrodes and\n    labels, single-type electrodes of fig2b-single-type labelled by their type, and non-responding\n    electrodes the electrodes of E that pass V for no condition; co-activated electrodes left out;\n    (b) the cross-validation, (i) stratified 5-fold repeated 100 times with the t-test over repeats,\n    or (ii) leave-one-out with the t-test over electrodes of each class (correct as 1, wrong as 0);\n    (c) features standardized or raw; (d) L readings. Accuracy per class is the fraction of that class's\n    electrodes predicted correctly. Reproduced when, under one combination of readings, all four\n    accuracies are within tolerance and each exceeds 25% with two-sided t-test p < 0.0001; partially\n    reproduced when, under every combination, all four exceed chance at p < 0.0001 but the values miss\n    tolerance; not reproduced when any class fails to exceed chance under every combination.\n- id: fig3-latency-values\n  statement: SYN-P responses start and peak earliest (onset 113 ms, peak 480 ms), then SEM (122 ms,\n    524 ms) and SYN-C (283 ms, 579 ms).\n  source: Results, paragraph 10; Figure 3c, 3d and 3f\n  quote: The results suggested that the SYN-P (onset, 113 ms and peak, 480 ms) occurred earlier than SEM\n    (122 ms and 524 ms) and SYN-C (283 ms and 579 ms) in terms of both onset and peak of the response,\n    respectively.\n  expected:\n  - {quantity: SYN-P onset, value: 113, tolerance: 11.3, unit: ms}\n  - {quantity: SYN-P peak, value: 480, tolerance: 48, unit: ms}\n  - {quantity: SEM onset, value: 122, tolerance: 12.2, unit: ms}\n  - {quantity: SEM peak, value: 524, tolerance: 52.4, unit: ms}\n  - {quantity: SYN-C onset, value: 283, tolerance: 28.3, unit: ms}\n  - {quantity: SYN-C peak, value: 579, tolerance: 57.9, unit: ms}\n  depends_on:\n  - fig2b-violation-electrodes\n  criterion: Latencies L per electrode and condition, averaged (mean, as Fig. 3a's box centre is the\n    mean) over electrodes. Open, the electrodes, (a) for each condition the electrodes passing V for it;\n    (b) the electrodes of E+ (pars opercularis, pars triangularis and precentral, the set of the Fig. 3d\n    legend, n = 106), each giving latencies for all three conditions; with L1, L2, L3 and the readings\n    of E and V. Reproduced when, under one combination, all six values are within tolerance and SYN-P\n    precedes SEM and SYN-C in both onset and peak; partially reproduced when the order holds under\n    every combination but no combination puts all six within tolerance. The n of each reading is\n    reported against 106.\n- id: fig3d-latency-differences\n  statement: Onset and peak latencies differ significantly between each pair of SYN-P, SYN-C and SEM.\n  source: Results, paragraph 10; Figure 3d legend\n  quote: we estimated the latency differences based on ANOVA (Fig. 3d, P < 0.001, one-way ANOVA, two\n    tailed, Bonferroni, corrected for ten participants.\n  statistics:\n  - about: SEM onset against SYN-P onset\n    test: one-way ANOVA, two tailed\n    p: 1.83e-5\n    corrected: Bonferroni, for ten participants\n    n: 106 electrodes in pars opercularis, pars triangularis and precentral\n  - about: SEM onset against SYN-C onset\n    test: one-way ANOVA, two tailed\n    p: 1.93e-14\n    corrected: Bonferroni, for ten participants\n  - about: SYN-C onset against SYN-P onset\n    test: one-way ANOVA, two tailed\n    p: 5.85e-30\n    corrected: Bonferroni, for ten participants\n  - about: SEM peak against SYN-P peak\n    test: one-way ANOVA, two tailed\n    p: 3.26e-13\n    corrected: Bonferroni, for ten participants\n  - about: SEM peak against SYN-C peak\n    test: one-way ANOVA, two tailed\n    p: 1.02e-5\n    corrected: Bonferroni, for ten participants\n  - about: SYN-C peak against SYN-P peak\n    test: one-way ANOVA, two tailed\n    p: 9.3e-27\n    corrected: Bonferroni, for ten participants\n  depends_on:\n  - fig3-latency-values\n  criterion: For each pair of conditions and for onset and peak, a one-way ANOVA (f_oneway) of the\n    electrodes' latencies of the two conditions, p multiplied by 10 (Bonferroni \"for ten participants\",\n    as printed). Electrodes and latencies under the readings of fig3-latency-values. Reproduced when,\n    under every combination of readings, all six corrected p are below 0.001; partially reproduced\n    when at least four are under every combination; not reproduced when fewer than four are under\n    every combination; blocked otherwise. The paper's p for SEM against SYN-P onset (1.83e-5) with\n    means 9 ms apart is noted as surprising; it is matched as printed.\n- id: fig3e-latency-not-location\n  statement: Response latencies do not depend on the location of the electrodes along the\n    anterior-posterior or superior-inferior axis, or across pars opercularis, pars triangularis and\n    precentral gyrus.\n  source: Results, paragraph 11; Figure 3e; Supplementary Figure 10c and 10d\n  quote: Moreover, response latencies did not depend on the spatial location of the electrodes (Fig. 3e\n    and Supplementary Fig. 10c,d).\n  depends_on:\n  - fig3-latency-values\n  criterion: A claim of absence, judged on the paper's test, a linear regression of latency on electrode\n    coordinate with its 95% confidence interval (Fig. 3e legend), for onset and peak, each condition,\n    and each axis. The legend calls the axes the x and y coordinates; on MNI152 the anterior-posterior\n    axis is y and the superior-inferior axis z, and both are used. Reproduced when every slope's 95%\n    CI includes zero; not reproduced when any excludes it, under the readings of fig3-latency-values\n    (blocked when they differ). Slopes are reported in ms per mm. The comparison across the three areas\n    (Supplementary Fig. 10c) has no test in the paper; a one-way ANOVA of latency on area at p < 0.05\n    is shown as a variant.\n- id: suppfig10a-separable-400-700\n  statement: The accuracy of classifying the conditions after the keyword peaks about 400 to 700 ms\n    after keyword onset.\n  source: Results, paragraph 10; Supplementary Figure 10a legend\n  quote: The accuracies for classifying different conditions peaked at about 400–700 ms after the\n    keywords, which indicated they were most separable in this time frame\n  expected:\n  - {quantity: start of peak accuracy window, value: 400, tolerance: 40, unit: ms}\n  - {quantity: end of peak accuracy window, value: 700, tolerance: 70, unit: ms}\n  criterion: The paper does not name the classifier, features, time resolution or cross-validation of\n    this panel. Readings, each of the three classifiers with the Methods settings (SVM, logistic\n    regression, kNN), classifying CORR, SYN-P, SYN-C and SEM trials from the HGA of the responding\n    electrodes of fig2b-violation-electrodes within each participant at each 10 ms sample (or in 100\n    ms windows), 5-fold stratified cross-validation, accuracy averaged over participants. Reproduced\n    when, under every reading, the time of maximum accuracy lies in 360 to 770 ms (the range widened\n    by 10% of each bound).\n- id: suppfig10b-duration-differs\n  statement: The total length of the significant difference from CORR differs between SYN-P, SYN-C and\n    SEM electrodes.\n  source: Results, paragraph 11; Supplementary Figure 10b legend\n  quote: The discrepancy in terms of the total length of the significant difference between respect\n    violation and correct sentence of each electrode (ANOVA). This also indicated temporal differences\n    in processing each linguistic component\n  statistics:\n  - test: one-way ANOVA, two tailed\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  depends_on:\n  - fig2b-violation-electrodes\n  criterion: For each electrode and each violation it passes V for, the total length of significant\n    samples (times 10 ms). One-way ANOVA of these lengths across SYN-P, SYN-C and SEM, and pairwise\n    one-way ANOVAs Bonferroni-corrected for three pairs (the paper does not say what is corrected;\n    the three pairs are read). Reproduced when the three-group ANOVA has p < 0.001 and at least one\n    corrected pair has p < 0.001 under every reading of E and V; the group medians are reported.\n- id: nl-low-frequency\n  statement: In the non-linguistic task, the violation enhances activity mainly at lower frequencies\n    (4 to 10 Hz), where many electrodes respond to both linguistic and non-linguistic tasks, unlike\n    the high-gamma band.\n  source: Results, paragraph 3; Supplementary Figures 4 and 7c\n  quote: In contrast, in the NL task, the violation condition showed an enhanced activity mainly at the\n    lower frequency (Supplementary Fig. 4), indicating that neural oscillations during linguistic and NL\n    tasks may arise in different frequency bands.\n  criterion: Needs the 4 to 10 Hz amplitude, which a high-gamma dataset does not hold. If the broadband\n    signal is present, the test of V for NL-VIO against NL-CORR at P < 0.01 corrected (Supplementary\n    Fig. 4b) on the 4 to 10 Hz amplitude and on HGA; reproduced when more electrodes pass at 4 to 10 Hz\n    than in high gamma.\n- id: stimuli-word-frequency\n  statement: Keyword frequencies are matched between CORR (shared by SYN-P and SEM; mean 31.88 per\n    million) and SYN-C (30.25 per million).\n  source: Methods, The Chinese language and stimuli design, paragraph 3\n  quote: the word frequencies were matched between CORR (same in SYN-P and SEM, mean frequency = 31.88\n    per million, s.d. = 35.14) and SYN-C (mean frequency = 30.25 per million, s.d. = 73.58) (t(62) =\n    0.11, P = 0.91)\n  data: with_inputs\n  statistics:\n  - test: t-test\n    statistic: t(62) = 0.11\n    p: 0.91\n    n: 32 CORR and 32 SYN-C keywords\n  expected:\n  - {quantity: CORR keyword mean frequency, value: 31.88, tolerance: 3.188, unit: per million}\n  - {quantity: SYN-C keyword mean frequency, value: 30.25, tolerance: 3.025, unit: per million}\n  criterion: Keywords from the supplement's sentence lists (word 4 of CORR and SYN-C), frequencies from\n    the corpus the paper names (lingua.mtsu.edu/chinese-computing, the Modern Chinese word frequency\n    list). Reproduced when both means are within tolerance and an independent two-sample t-test gives\n    p > 0.05.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001193/10.1038-s41562-022-01334-6.yaml paper/10.1038-s41562-022-01334-6.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/001193 && f=10.1038-s41562-022-01334-6.yaml && python - <<'EOF'
f='10.1038-s41562-022-01334-6.yaml'
s=open(f).read()
s=s.replace("{quantity: words per sentence in CORR, SYN-C and SEM,","{quantity: words per sentence in CORR SYN-C and SEM,")
s=s.replace("{quantity: electrodes passing V for SYN-P, SYN-C or SEM,","{quantity: electrodes passing V for any of SYN-P SYN-C and SEM,")
s=s.replace("""the electrodes (46/62) strongly responded to only one type of violation (below figure). Only a few
    electrodes were co-activated by two violation types (16/62) and were mainly co-activated by SYN-P
    and SYN-C""","""the electrodes (46/62) strongly responded to only one type of violation (below figure). Only a few
    electrodes were ... by two violation types (16/62) and were mainly ... by SYN-P and SYN-C""")
s=s.replace("""(below figure). Only a few electrodes were co-activated by two violation types (18/79) and were
    mainly co-activated by SYN-P and SYN-C""","""(below figure). Only a few electrodes were ... by two violation types (18/79) and were
    mainly ... by SYN-P and SYN-C""")
open(f,'w').write(s)
EOF
cd ../.. && python tools/claims_check.py claims/001193/10.1038-s41562-022-01334-6.yaml paper/10.1038-s41562-022-01334-6.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "—\|rather" claims/001193/*.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/001193/10.1038-s41562-022-01334-6.yaml'))
print(len(d['claims']),sum('criterion' in c for c in d['claims']),sum(len(c.get('statistics',[])) for c in d['claims']),sum('statistics' in c for c in d['claims']))"; grep -n "[a-z]: [a-z]" claims/001193/*.yaml | grep -v "^\S*:[0-9]*:\s*[-a-z_]*:" | head
```

```
24 24 9 4
5:# Text read: the version of record (paper/10.1038-s41562-022-01334-6.txt, from the publisher PDF
32:#   participants". NL, the other five: sequences of geometric shapes, changed (NL-VIO) or not (NL-CORR),
54:#   word presentation. (E2) what is compared: per trial the mean HGA in the rest period against per
82:  archive: dandi
84:paper: doi:10.1038/s41562-022-01334-6
86:- id: participants
96:  - {quantity: participants, value: 10, tolerance: 0}
97:  - {quantity: male participants, value: 4, tolerance: 0}
98:  - {quantity: female participants, value: 6, tolerance: 0}
99:  - {quantity: participants with COM, value: 5, tolerance: 0}
```

**Agent**

I wrote `claims/001193/10.1038-s41562-022-01334-6.yaml`. The quote checker passes with 0 problems (24 claims, 24 quotes, 9 statistical values). Nothing is committed.

**Text read.** The version of record (Nature Human Behaviour 6, 1104–1111): main text, figure legends, Methods, reporting summary, and the Supplementary Information PDF (Table 1, Figs. 1–10, the stimulus sentence lists). The paper links no code; it is "available from the authors upon reasonable request", so no repository was read. The PDF could not be rendered here because poppler is not installed. So numbers printed only inside figure panels, such as the region counts of the Fig. 2b Venn diagram, are not used.

**Claims.** There are 24, all with quotes and all with a criterion. The task-structure count of 32 sentences per condition comes from the supplement's lists; no sentence of the text gives it, and the criterion says so.
- **Statistics:** 9 entries on 4 claims: the six pairwise latency p-values of Fig. 3d, the t-test against 25% chance in Suppl. Fig. 9, the ANOVA in Suppl. Fig. 10b, and the word-frequency t-test.
- **Coverage:** participants and task structure, behaviour, frequency band, IFG localisation, effects only after the keyword, the 58 violation electrodes, 49 single-type and 9 co-activated electrodes, the half-split and duration robustness checks, Euclidean similarity, the COM overlap, the non-linguistic control, absence of spatial separation (pooled and per participant), the 3.25 mm circuit diameter, prediction from correct sentences, latency values and their tests, latency not depending on location, the 400–700 ms classification peak, the duration differences, the low-frequency effect in the non-linguistic task, and keyword frequency matching.
- **Data:** one claim (word frequency) is `with_inputs`, using the corpus the paper names. The rest are `dataset`. The dandiset's description says it holds high-gamma activity only, so the band-comparison and low-frequency claims (Fig. 1b, Suppl. Figs. 3, 4, 7c) are likely untestable.

**Details the paper leaves open, and the readings named:**
- **Resting state (E1):** the 800 ms fixation, or fixation plus the 500 ms blank (1,300 ms).
- **"More than 50 ms" (V1):** consecutive samples, or total samples.
- **"> 0.55 z" (V2):** the violation's own amplitude, or its difference from correct sentences.
- **The F value (F1–F3):** maximum over samples, mean over significant samples, or the F of the time-averaged amplitude.
- **Fractional-area latency (L1–L3):** the violation response or its difference from correct sentences; area over 0–1,000 ms or over the discriminating period; negative values set to zero or kept.
- **Latency electrode set:** per-condition violation electrodes, or responsive electrodes in pars opercularis, pars triangularis and precentral gyrus. The paper's n = 106 cannot be derived from anything stated.
- **Euclidean distance:** what the condition vectors are, and which pair "syntactic to semantic" means.
- **Half-split:** which half of the sentences is "first".
- **Duration-metric electrode selection (79 electrodes):** with or without the amplitude rule.
- **COM "responded":** passing the violation test, or F > 4.
- **Non-linguistic threshold:** 0.01/256, with 0.05/256 as a variant.
- **Permutation test for spatial separation:** centroid distance or KDE-peak distance.
- **kNN prediction:** which electrodes count as non-responding, the cross-validation scheme, and feature scaling.
- **Time-resolved classifier:** the paper does not name it; each of the three Methods classifiers is a reading.
- **IFG labels:** with or without pars orbitalis.
- **Fig. 3e axes:** the legend says "x or y"; both MNI axes are used.

**Missing from the paper:**
- the analysis code;
- the equation of the circuit-size estimate is garbled in the text; it was read as p = 1 − (r − 0.5)/r, which matches the figure's 15.6% and 3.25 mm;
- the non-linguistic correction factor;
- how the 106 electrodes of Fig. 3d were selected;
- the Supplementary Excel file and Source Data were not supplied, but no claim needs them.

The p-value printed for SEM against SYN-P onset (1.83 × 10⁻⁵, for means only 9 ms apart) looks surprising. It is matched as printed.

## End of run

16 turns, 5 minutes, result: success.
