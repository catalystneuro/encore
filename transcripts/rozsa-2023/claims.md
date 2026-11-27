# rozsa-2023 · claims · run 44569831232

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ tools/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ claims/ tools/
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-16`. Record this version in the attempt's provenance.
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

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml; wc -c paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -c 14000 claims/fouke-2025.yaml; echo; echo ----; tail -c 4000 claims/fouke-2025.yaml
```

```
# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
# from its Results, figure legends and STAR Methods. The version of record is not open access.
#
# When these criteria were written, the author had seen the data check only: the file list,
# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
# the extent of positions. No claim's analysis had been run. The author had also read the
# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
# which include per-stimulus median speeds and angular velocities and its statistics.
#
# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
# use outside data and depend on that claim.
#
# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 305 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-sciadv.ade4511.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text, Methods and supplement are all present, and the paper links no code (it mentions only "custom MATLAB scripts"). Next I'll check the dataset record.

**Agent calls Bash**

```bash
cat papers/datasets/rozsa-2023.yaml 2>/dev/null; grep -rl "000341" --include=*.yaml --include=*.json . 2>/dev/null | grep -v transcripts | head; python tools/claims_check.py -h 2>&1 | head -20
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1126/sciadv.ade4511
title: Temporal disparity of action potentials triggered in axon initial segments and distal axons in
  the neocortex
datasets:
- archive: dandi
  id: '000341'
  relation: primary
./papers/manifest.yaml
./papers/match/000341.yaml
./papers/datasets/rozsa-2023.yaml
./targets/contributors.yaml
./targets/dandisets.json
Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cat papers/match/000341.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for x in (it if isinstance(it,list) else it.values()):
  if '000341' in json.dumps(x)[:200]: print(json.dumps(x,indent=1)[:3000]); break
"; ls schemas/
```

```
# Whether each paper DANDI:000341 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: dandi
  id: '000341'
date: '2026-11-19'
papers:
- doi: 10.1126/sciadv.ade4511
  relation: IsDescribedBy
  checks:
    text: true
    title_in_text: true
    names_this: true
    names_others: []
  verdict: primary
  by: checks
  reason: The paper names DANDI:000341 and no other dataset.
attempt.schema.json
claims.schema.json
entry.schema.json
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -A12 '"000341"' targets/dandisets.json | head -40; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
2049:   "dandiset": "000341",
2050-   "name": "Temporal disparity of action potentials triggered in axon initial segments and distal axons in the neocortex",
2051-   "published_version": "0.241220.1312",
2052-   "asset_count": 787,
2053-   "size_gb": 711.58,
2054-   "data_standards": [
2055-    "Neurodata Without Borders (NWB)"
2056-   ],
2057-   "species": [
2058-    "Homo sapiens - Human",
2059-    "Rattus norvegicus - Norway rat",
2060-    "Mus musculus - House mouse"
2061-   ],
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "type": "object",
 "additionalProperties": false,
 "required": [
[... 194 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 2061,2080p targets/dandisets.json; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"; ls claims/ | head -0; grep -l "^paper:" claims/*.yaml | head -0; grep -L "^dataset:" claims/*.yaml | head -3
```

```
],
   "approaches": [
    "electrophysiological approach"
   ],
   "papers": [
    {
     "doi": "10.1126/sciadv.ade4511",
     "title": "Temporal disparity of action potentials triggered in axon initial segments and distal axons in the neocortex",
     "relation": "IsDescribedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "000350",
   "name": "Glia Accumulate Evidence that Actions Are Futile and Suppress Unsuccessful Behavior",
   "published_version": "0.240822.1759",
   "asset_count": 12,
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
ls -t claims/*.yaml | head -3; f=$(ls -t claims/*.yaml | head -1); head -60 $f
```

```
claims/zhuang-2025.yaml
claims/zhu-2022.yaml
claims/zhong-2026.yaml
# Claims for Zhuang, Lemak, Sridhar & Nelson (2025), Brain 149:238-251, on dandiset 001177.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol pilot-12 as stated in docs/protocol.md. The writer did not look at the dandiset's data or
# files; only its title and description on the archive were read. Claim fig1fg-delay-discounting
# was added by the check of 2026-10-28.
#
# Text read: the version of record (open access, CC BY), full text as served by Europe PMC
# (PMC12597312), with its one supplement, awaf312_supplementary_data.pdf (Figures S1 to S8 and
# legends, Supplementary Materials and methods, and Table 1, "Experimental analysis and
# statistics"). Figure panels of the main paper were not available as images; values in the main
# figure legends were read from the text. The pie-chart percentages of Figures S5D and S8A-B were
# read from the supplement PDF (pages 7 and 10), as the text holds only the legends.
#
# Code read. The paper links (1) UCSF-Nelson-Lab/ICD-Cognitive-Analysis, tag ICD, commit 5528e22
# (Zenodo doi:10.5281/zenodo.10703139, record 10703140): Python scripts that count task events per
# block of the delay discounting task (delay_discounting_task.py, phase2.py, phase3.py) and
# Summary_Cognitive.m, which averages each mouse's sessions within a condition, fits
[... 43 more lines not kept]
```

**Agent**

The paper has no linked code, so every method comes from the Methods and legends. I'm writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/rozsa-2023.yaml",
 "content": "# Claims for Rozsa, Toth, Olah, Baka, Lakovics, Barzo & Tamas (2023), Sci. Adv. 9, eade4511, on\n# dandiset 000341.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-19,\n# protocol pilot-16 as stated in docs/protocol.md. The writer did not look at the dandiset's data or\n# files; only its title and the species it lists (human, rat, mouse) were read.\n#\n# Text read: the version of record (open access), full text as served by Europe PMC (PMC10569705,\n# JATS XML flattened), with its one supplement, sciadv.ade4511_sm.pdf (Figures S1 to S6 with legends,\n# Table S1). The main figures were not available as images; their values were read from the Results\n# and the legends. The reference list is not in the text read, so the cited sources for the sag\n# fraction (ref. 28) and for the cellular state definition (ref. 38) could not be read.\n#\n# Code read: none. The paper links no code; the Methods say the data were analysed with Fitmaster\n# (HEKA) and custom MATLAB scripts, and phases with the MATLAB Circular Statistics Toolbox (ref. 49).\n#\n# Data the paper used. All recordings are somatic whole-cell current clamp of layer 1 interneurons,\n# filtered at 10 kHz (Bessel) and sampled at 50 kHz in Patchmaster.\n# - Human slices: neocortex resected from 71 patients (41 female, 30 male, 50 +- 20 years; Table S1),\n#   frontal, temporal, occipital and parietal. Rat slices: somatosensory cortex of Wistar rats, P18\n#   to P44. About 36 degrees C, conventional or dual-superfusion chamber.\n# - RAF induction (Figures 1, S1): 100 ms suprathreshold square pulses (50 to 500 pA, at least four\n#   APs per pulse) every 300 ms, stopped when APs appear between pulses, then continuous recording.\n#   Human 385 cells (87 with RAF), rat 259 cells (102 with RAF). Post hoc biocytin morphology: NGFC,\n#   non-NGFC, rosehip.\n# - Dual soma and axonal bleb recordings (Figures 1H-K, 2F-H, S6): human 2 NGFCs and 3 unidentified,\n#   rat 3 NGFCs and 3 unidentified; hyperpolarizing steps alternately in soma and bleb, depolarizing\n#   steps in soma only.\n# - ZD7288 30 uM (Figures 2A-C, S2): human 4 and rat 3 cells. Sag fraction (Figure 2E): human 358,\n#   rat 254 cells. Local puff of ACSF with 5 mM KCl (Figure 2I-L): human 4, rat 7 cells.\n# - Active slices (Figure 3): in vivo-like ACSF (1.2 mM Ca, 1 mM Mg), dual superfusion, 2 uM\n#   carbachol and 10 uM SCH23390. Human 26 cells without LFP; rat 40 cells with a layer 5 LFP. Rat\n#   without carbachol and SCH23390, 90 cells (Figure S3).\n# - In vivo (Figure 4, S4, S5): head-fixed mice, P35 to P180, GAD67-GFP (37), Ai9 (5), C57BL/6J (3)\n#   and vGAT-Ai9 (75), awake or under chloral hydrate or ketamine-xylazine; 242 layer 1 interneurons\n#   at 20 to 120 um depth with a deep layer LFP within about 1000 um.\n#\n# Method shared by the claims, from the Methods (\"Analysis of RAF patterns\", \"Analysis of AP timing\n# related to network oscillations\", \"Statistics\"):\n# - APs detected on unfiltered traces; the threshold is the point where dV/dt first exceeds 5 mV/ms;\n#   the pre-AP ramp slope is the slope of a linear fit to the last 1 ms before threshold. Threshold\n#   and slope separate AIS-APs (higher threshold, steeper ramp) from RA-APs.\n# - An RAF epoch is sporadic when its RAF frequency is below 5 Hz and persistent (tonic) above;\n#   number of RA-APs, RAF duration (first to last RA-AP in the continuous recording), RAF frequency\n#   (RA-APs over duration).\n# - Phase: a 4 s AP-triggered LFP segment per AP, FFT power multiplied by frequency; an AP is kept\n#   when the corrected power in 0.5 to 4 Hz over that in 0.5 to 45 Hz exceeds 0.1. The LFP is\n#   Butterworth band-passed 0.5 to 4 Hz, Hilbert phase on 0 to 360 degrees with the LFP trough at 0\n#   and 360 degrees (up state) and the peak at 180 degrees (down state); the phase at the AP peak is\n#   used. Mean vector direction and length, Rayleigh test, on the APs pooled across cells.\n# - Values are median +- SD unless stated. Each comparison is preceded by a Kolmogorov-Smirnov test\n#   of normality; normal data get a paired or two-sample t test, others a Mann-Whitney U test.\n#   Significance at P < 0.05.\n#\n# Details these sources leave open, with the readings allowed, used by several claims:\n# - AP detection apart from the 5 mV/ms threshold. A standard choice is used, an upstroke crossing\n#   5 mV/ms followed by a peak above 0 mV; a peak at least 30 mV above threshold is the variant. It\n#   is shown both ways where a claim counts APs.\n# - The boundary between AIS-APs and RA-APs. No numbers are given. Readings: (a) labels the\n#   dandiset carries, when it has them; (b) a two-component Gaussian mixture on threshold and pre-AP\n#   slope fitted to the APs of each preparation pooled (human slice, rat slice, mouse in vivo), RA-APs\n#   the component with the lower threshold; (c) in induction recordings only, APs during the current\n#   pulses are AIS-APs and APs in the interstimulus intervals and the continuous recording are\n#   RA-APs. Every claim that classifies APs states which readings apply.\n# - Tolerances. The paper gives medians with the SD of the cells or APs. The SD is the spread of the\n#   sample, not an uncertainty of the median (88 +- 1828 RA-APs), so it is not used as a tolerance;\n#   medians and means get 10% of the value, and the SDs are reported beside them, not judged.\n# - Counts that disagree inside the paper. Human RAF cells are 87 of 385 in the Results and 83 of\n#   358 in the sag analysis; rat RAF cells are 102 of 259 in Figure S1B and 97 of 254 in the sag\n#   analysis. Each claim uses the counts its own passage gives.\n# - Phase method. Butterworth order and whether the filter is zero phase are not given; MATLAB\n#   filtfilt with order 2 is the standard choice, order 4 the variant. Whether the 4 s segment is\n#   centred on the AP is not given; centred (2 s each side) is the standard choice.\nschema_version: 2\npaper: doi:10.1126/sciadv.ade4511\nclaims:\n- id: fig1ab-raf-patterns\n  statement: Human layer 1 interneurons show two forms of retroaxonal firing (RAF) after induction,\n    persistent RAF with barrages of RA-APs at high frequency (median 88 RA-APs, 13.9 Hz; duration\n    median 17.1 s, mean 68.4 s, from 0.18 to 2809 s) and sporadic RAF with a few RA-APs at low\n    frequency (median 8 RA-APs, 0.31 Hz).\n  source: Results, paragraph 1; Figure 1A and 1B\n  quote: 'persistent RAF showed barrages of 88 ± 1828 RA-APs with high frequencies (13.9 ± 17.3 Hz),\n    (RAF duration: min: 0.18 s, max: 2809 s, mean: 68.4 s, and median: 17.1 ± 202.9 s); however,\n    only a few (8 ± 6) individual RA-APs emerged at low frequencies (0.31 ± 1.5 Hz) during sporadic\n    RAF'\n  expected:\n  - quantity: persistent RAF, median number of RA-APs\n    value: 88\n    tolerance: 8.8\n  - quantity: persistent RAF, median RAF frequency\n    value: 13.9\n    tolerance: 1.39\n    unit: Hz\n  - quantity: persistent RAF, median duration\n    value: 17.1\n    tolerance: 1.71\n    unit: s\n  - quantity: persistent RAF, mean duration\n    value: 68.4\n    tolerance: 6.84\n    unit: s\n  - quantity: persistent RAF, minimum duration\n    value: 0.18\n    tolerance: 0.018\n    unit: s\n  - quantity: persistent RAF, maximum duration\n    value: 2809\n    tolerance: 280.9\n    unit: s\n  - quantity: sporadic RAF, median number of RA-APs\n    value: 8\n    tolerance: 0.8\n  - quantity: sporadic RAF, median RAF frequency\n    value: 0.31\n    tolerance: 0.031\n    unit: Hz\n  criterion: Human induction recordings only. RA-APs are the APs of the continuous recording after\n    induction, classed by readings (a) to (c) of the header. Per the Methods, an RAF epoch's\n    duration runs from its first to its last RA-AP, its frequency is RA-APs over duration, and an\n    epoch is persistent above 5 Hz and sporadic below. The Methods do not say how a recording is\n    cut into epochs, nor what duration an epoch of one RA-AP has. Readings are (i) one epoch per\n    cell, all RA-APs after induction; (ii) one epoch per induction run, when a cell was induced\n    more than once (Figure 1E has cells with both patterns). Epochs of a single RA-AP are left\n    out, as their frequency is undefined. Reproduced when, under one reading, at least six of the\n    eight values are within tolerance and the two groups both occur; partially reproduced for four\n    or five. The SDs are reported beside the medians.\n- id: fig1c-ra-lower-threshold-slope\n  statement: RA-APs have a lower somatic threshold potential and a lower pre-AP depolarization\n    slope than AIS-APs, during persistent and during sporadic RAF.\n  source: Results, paragraph 1; Figure 1C\n  quote: RA-APs during persistent RAF had lower somatic AP threshold and lower pre-AP depolarization\n    slope values compared to AIS-APs ( 19 – 22 , 25 ). We confirmed this during sporadic RAF\n  criterion: Human induction recordings, under reading (c) of the header (APs during the current\n    pulses are AIS-APs, APs after induction are RA-APs) and under reading (a) when the dandiset\n    labels APs. Reading (b) is left out here, as it separates the classes by these very measures.\n    Threshold and slope as in the Methods. The paper reports no test for this panel; its general\n    rule is used, a Kolmogorov-Smirnov normality test, then a two-sample t test or a Mann-Whitney U\n    test on the APs pooled, within persistent and within sporadic epochs. Reproduced when the RA-AP\n    median threshold and median slope are both lower than those of AIS-APs with P < 0.05 in both\n    patterns; partially reproduced when this holds in one. The per-cell comparison (each cell's\n    medians) is shown as a variant.\n- id: fig1d-human-raf-proportion\n  statement: About one-fourth of tested human layer 1 interneurons (87 of 385) show RAF.\n  source: Results, paragraph 1; Figure 1D\n  quote: One-fourth of the tested interneurons (87 of 385 cells; Fig. 1D ) in layer 1 of the human\n    neocortex showed RAF\n  expected:\n  - quantity: fraction of human layer 1 interneurons with RAF\n    value: 0.226\n    tolerance: 0.0226\n  criterion: A cell shows RAF when at least one RA-AP occurs after induction, RA-APs classed by\n    readings (a) to (c) of the header. The counts of cells tested and with RAF are reported. The\n    fraction 83 of 358 (0.232) from the sag analysis is the other count the paper gives.\n- id: fig1f-human-raf-ngfc\n  statement: In human layer 1, RAF is predominant in neurogliaform cells (21 of 44 NGFCs) and rarer\n    in other interneurons (9 of 90 non-NGFCs), and cannot be evoked in rosehip cells (0 of 15).\n  source: Results, paragraph 1; Figure 1F\n  quote: We could trigger RAF in 21 of 44 NGFCs and 9 of 90 non-NGFCs ( Fig. 1F ) and found that\n    RAF could not be evoked in rosehip cells ( n = 15)\n  expected:\n  - quantity: fraction of human NGFCs with RAF\n    value: 0.477\n    tolerance: 0.0477\n  - quantity: fraction of human non-NGFCs with RAF\n    value: 0.1\n    tolerance: 0.01\n  - quantity: human rosehip cells with RAF\n    value: 0\n    tolerance: 0\n  depends_on:\n  - fig1d-human-raf-proportion\n  criterion: Needs the post hoc morphological class of each cell (NGFC, non-NGFC, rosehip) as the\n    Methods define it from biocytin fills; the class is taken as the dandiset records it. RAF as in\n    fig1d-human-raf-proportion. Whether the 15 rosehip cells are among the 90 non-NGFCs is not\n    said; both readings are shown (non-NGFC with and without rosehip cells). Reproduced when the\n    three values hold under one reading; partially reproduced when NGFCs have the higher fraction\n    but a value is outside tolerance.\n- id: figs1b-rat-raf-proportion\n  statement: About a third of tested rat layer 1 interneurons (102 of 259) show RAF.\n  source: Figure S1B\n  quote: Approximately a third of the tested cells (102 out of 259) showed RAF.\n  expected:\n    quantity: fraction of rat layer 1 interneurons with RAF\n    value: 0.394\n    tolerance: 0.0394\n  criterion: As in fig1d-human-raf-proportion, on the rat induction recordings. The fraction 97 of\n    254 (0.382) from the sag analysis is the other count the paper gives.\n- id: figs1d-rat-raf-values\n  statement: Rat interneurons show both sporadic RAF (frequency 1 Hz, 7 RA-APs) and tonic RAF\n    (frequency 6.9 Hz, 100 RA-APs).\n  source: Figure S1D\n  quote: 'We observed both sporadic RAF (RAF frequency: 1 ± 1.8 Hz, Number of RA-AP: 7± 2.2) and\n    tonic RAF (RAF Frequency: 6.9 ± 14 Hz, Number of RA-AP: 100 ± 241) in the rodent brain slice\n    preparation.'\n  expected:\n  - quantity: sporadic RAF, median frequency\n    value: 1\n    tolerance: 0.1\n    unit: Hz\n  - quantity: sporadic RAF, median number of RA-APs\n    value: 7\n    tolerance: 0.7\n  - quantity: tonic RAF, median frequency\n    value: 6.9\n    tolerance: 0.69\n    unit: Hz\n  - quantity: tonic RAF, median number of RA-APs\n    value: 100\n    tolerance: 10\n  criterion: As in fig1ab-raf-patterns, on the rat induction recordings, with the same epoch\n    readings. A sporadic median of 1 Hz under a 5 Hz split is allowed by the Methods. Reproduced\n    when, under one reading, at least three of the four values are within tolerance.\n- id: fig1g-rat-raf-ngfc\n  statement: In rat neocortex, RAF is found predominantly in NGFCs (22 NGFC and 10 non-NGFC RAF\n    cells).\n  source: Figure 1G legend; Results, paragraph 1\n  quote: we repeated these experiments in the rat neocortex and confirmed the presence of both\n    sporadic and persistent RAF in interneurons predominantly identified as NGFCs\n  expected:\n  - quantity: rat RAF cells classified as NGFC\n    value: 22\n    tolerance: 2.2\n  - quantity: rat RAF cells classified as non-NGFC\n    value: 10\n    tolerance: 1\n  depends_on:\n  - figs1b-rat-raf-proportion\n  criterion: Counts of rat RAF cells by morphological class as the dandiset records it. The legend\n    gives no RAF-negative counts, so whether the counts are of RAF cells only is a reading; the\n    fractions with RAF in each class are shown as well.\n- id: fig1hk-bleb-initiation-order\n  statement: In dual soma and axonal bleb recordings of human NGFCs, AIS-APs reach the soma first\n    and the bleb second, while RA-APs reach the bleb first, and RA-APs have lower somatic threshold\n    and pre-AP slope.\n  source: Results, paragraph 1; Figure 1H to 1K\n  quote: In response to somatic depolarizing current pulses, AIS-APs were detected first on the\n    somatic electrode and then at the axonal recording site, the order was reversed for RA-APs\n  criterion: Human NGFC dual recordings (n = 2). For each somatic AP, the soma-to-bleb latency is\n    the bleb AP time minus the somatic AP time; the time point is not given, and readings are the\n    threshold crossing (5 mV/ms) and the peak. AIS-APs and RA-APs by readings (a) or (b) of the\n    header, the classes taken on the somatic trace. Reproduced when in each cell the AIS-APs have a\n    positive median latency and the RA-APs a negative one, and RA-APs have the lower median\n    threshold and slope; partially reproduced when this holds in one of the two cells.\n- id: fig2c-zd7288-reduces-raf\n  statement: Blocking HCN channels with ZD7288 (30 uM) reduces the duration of RAF (47.2 to 10.1 s)\n    and the number of RA-APs (624 to 48) in human and rat layer 1 interneurons.\n  source: Results, paragraph 2; Figure 2A to 2C\n  quote: the duration of RAF [from 47.2 ± 36.1 to 10.1 ± 16 (s), paired sample t test, P = 0.008]\n    and the number of RA-APs (from 624 ± 412 to 48 ± 71, paired sample t test, P = 0.007) decreased\n    both in human ( n = 4) and in rodent ( n = 3) layer 1 interneurons\n  statistics:\n  - about: RAF duration, control against ZD7288\n    test: paired-sample t test\n    p: 0.0081\n    n: 7 cells, 4 human and 3 rat\n  - about: number of RA-APs, control against ZD7288\n    test: paired-sample t test\n    p: 0.00706\n    n: 7 cells, 4 human and 3 rat\n  expected:\n  - quantity: RAF duration, control\n    value: 47.2\n    tolerance: 4.72\n    unit: s\n  - quantity: RAF duration, ZD7288\n    value: 10.1\n    tolerance: 1.01\n    unit: s\n  - quantity: number of RA-APs, control\n    value: 624\n    tolerance: 62.4\n  - quantity: number of RA-APs, ZD7288\n    value: 48\n    tolerance: 4.8\n  criterion: Per cell, RAF duration and RA-AP count after induction in control and after ZD7288, as\n    in fig1ab-raf-patterns, the 7 cells pooled. Paired t test as in the legend. Whether the values\n    are medians (the Statistics section) or means (usual with a t test) is not said; both are\n    shown. Reproduced when both decreases hold with P < 0.05 and, under one of the two readings, at\n    least three of the four values are within tolerance; partially reproduced when the decreases\n    hold with P < 0.05 but fewer values match.\n- id: figs2-zd7288-passive-properties\n  statement: ZD7288 increases input resistance (70 to 98 MOhm, P = 0.01), and hyperpolarizes the\n    resting potential (-60 to -67 mV, P = 0.075) and decreases sag fraction (0.04 to 0.017, P =\n    0.057) without reaching significance.\n  source: Figure S2A to S2C\n  quote: '(A) Input resistance (control: 70 ± 96 MOhm, ZD7288: 98 ± 132 MOhm, paired-sample t-test\n    p=0.01).'\n  statistics:\n  - about: input resistance\n    test: paired-sample t-test\n    p: 0.01\n  - about: resting membrane potential\n    test: paired sample t-test\n    p: 0.075\n  - about: sag fraction\n    test: paired sample t-test\n    p: 0.057\n  expected:\n  - quantity: input resistance, control\n    value: 70\n    tolerance: 7\n    unit: MOhm\n  - quantity: input resistance, ZD7288\n    value: 98\n    tolerance: 9.8\n    unit: MOhm\n  - quantity: resting membrane potential, control\n    value: -60\n    tolerance: 6\n    unit: mV\n  - quantity: resting membrane potential, ZD7288\n    value: -67\n    tolerance: 6.7\n    unit: mV\n  - quantity: sag fraction, control\n    value: 0.04\n    tolerance: 0.004\n  - quantity: sag fraction, ZD7288\n    value: 0.017\n    tolerance: 0.0017\n  criterion: The ZD7288 cells of fig2c-zd7288-reduces-raf; the legend gives no n. Input resistance\n    and the current step it is measured from are not defined; the standard choice is the steady\n    voltage deflection over the current of a small hyperpolarizing step. Sag fraction as in\n    fig2e-sag-species. Paired t tests. Reproduced when input resistance rises with P < 0.05 and at\n    least four of the six values are within tolerance.\n- id: fig2e-sag-species\n  statement: Human layer 1 interneurons have a higher somatic sag fraction than rat ones (0.15\n    against 0.04).\n  source: Results, paragraph 2; Figure 2E\n  quote: layer 1 human interneurons ( n = 358, 0.15 ± 0.29, Mann-Whitney test, P < 0.001) showed\n    higher sag fractions compared to those in rat ( n = 254, 0.04 ± 0.4)\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.001\n    p_relation: <\n    n: 358 human and 254 rat cells\n  expected:\n  - quantity: human sag fraction, median\n    value: 0.15\n    tolerance: 0.015\n  - quantity: rat sag fraction, median\n    value: 0.04\n    tolerance: 0.004\n  criterion: The sag fraction is not defined in the text; it cites ref. 28 and Figure 2D marks its\n    components on a hyperpolarizing step. Readings are (a) (peak deflection minus steady-state\n    deflection) over the peak deflection from rest; (b) the same difference over the steady-state\n    deflection. The step used is not given; readings are the most hyperpolarizing step and the\n    step whose peak is nearest -90 mV. Reproduced when, under one reading, both medians are within\n    tolerance and the Mann-Whitney test gives P < 0.001 with human higher; partially reproduced\n    when the test holds and the medians do not.\n- id: fig2e-sag-raf-smaller\n  statement: In both species, interneurons with RAF have smaller somatic sag fractions than those\n    without (human 0.11 against 0.16; rat 0.02 against 0.06).\n  source: Results, paragraph 2; Figure 2E\n  quote: 'human and rat interneurons with RAF showed smaller sag fractions compared to interneurons\n    without RAF ( Fig. 2E ; human RAF: n = 83, 0.11 ± 0.08; no-RAF: n = 275, 0.16 ± 0.16,\n    Mann-Whitney test, P < 0.001; rat RAF: n = 97, 0.02 ± 0.07; no-RAF: n = 157, 0.06 ± 0.11,\n    Mann-Whitney test, P < 0.001'\n  statistics:\n  - about: human, RAF against no-RAF\n    test: Mann-Whitney test\n    p: 0.001\n    p_relation: <\n    n: 83 RAF and 275 no-RAF human cells\n  - about: rat, RAF against no-RAF\n    test: Mann-Whitney test\n    p: 0.001\n    p_relation: <\n    n: 97 RAF and 157 no-RAF rat cells\n  expected:\n  - quantity: human RAF sag fraction\n    value: 0.11\n    tolerance: 0.011\n  - quantity: human no-RAF sag fraction\n    value: 0.16\n    tolerance: 0.016\n  - quantity: rat RAF sag fraction\n    value: 0.02\n    tolerance: 0.002\n  - quantity: rat no-RAF sag fraction\n    value: 0.06\n    tolerance: 0.006\n  depends_on:\n  - fig2e-sag-species\n  - fig1d-human-raf-proportion\n  - figs1b-rat-raf-proportion\n  criterion: Sag fraction readings as in fig2e-sag-species; RAF status as in\n    fig1d-human-raf-proportion. Reproduced when in both species the RAF group is lower with\n    Mann-Whitney P < 0.001 and, under one reading, at least three of the four medians are within\n    tolerance; partially reproduced when this holds in one species.\n- id: fig2h-bleb-sag-higher\n  statement: Axonal blebs show about four times the sag fraction of the soma of the same layer 1\n    interneurons (0.4 against 0.1), at 106 um Euclidean soma-bleb distance.\n  source: Results, paragraph 2; Figure 2F to 2H\n  quote: 'found approximately four times higher sag fractions on the axon (somatic: 0.1 ± 0.05,\n    bleb: 0.4 ± 0.14, two-sample t test, P < 0.001)'\n  statistics:\n  - test: two-sample t test\n    p: 0.001\n    p_relation: <\n    n: 11 cells, human 2 NGFCs and 3 unidentified, rat 3 NGFCs and 3 unidentified\n  expected:\n  - quantity: somatic sag fraction\n    value: 0.1\n    tolerance: 0.01\n  - quantity: bleb sag fraction\n    value: 0.4\n    tolerance: 0.04\n  - quantity: Euclidean soma-bleb distance\n    value: 106\n    tolerance: 10.6\n    unit: um\n  criterion: Sag fraction readings as in fig2e-sag-species, each compartment from the\n    hyperpolarizing step injected into it, as the Methods describe. A two-sample t test as the\n    paper names it, with a paired t test as a variant. Reproduced when the bleb is higher with P <\n    0.001 and both sag values are within tolerance under one reading; partially reproduced when\n    the bleb is higher with P < 0.05. The distance is reported if the dandiset records it.\n- id: fig2il-kcl-induces-ra-aps\n  statement: Local application of ACSF with 5 mM K+ more than 40 um from the cell transiently\n    induces sporadic RA-APs in human (n = 4) and rat (n = 7) layer 1 interneurons.\n  source: Results, paragraph 2; Figure 2I to 2L\n  quote: we injected artificial cerebrospinal fluid (ACSF) with elevated physiological K +\n    concentration (5 mM) ( 32 ) while monitoring the membrane potential of layer 1 interneurons of\n    >40 μm from the injection site and successfully induced sporadic RA-APs transiently in human (\n    n = 4) and rat ( n = 7) layer 1 interneurons\n  criterion: In each KCl recording, APs classed by readings (a) or (b) of the header. Reproduced when\n    RA-APs occur in at least 4 human and 7 rat recordings, their RAF frequency is below 5 Hz, and,\n    where the application time is marked, they fall after it; partially reproduced when this holds\n    in most of them.\n- id: fig3-human-ap-states\n  statement: In active human slices (n = 26 cells), AIS-APs occur only in depolarized up states in\n    all 7 cells with AIS-APs, while spontaneous RA-APs, seen in 6 cells, also occur in hyperpolarized\n    down and transition states.\n  source: Results, paragraph 3; Figure 3B to 3D and 3G\n  quote: 'AIS-APs were restricted to plateaus of depolarized membrane potential (up states) in all\n    recorded cells with AIS-APs ( n = 7); however, when occurred (in n = 6 cells), spontaneous\n    RA-APs were detected when the membrane potential dropped to hyperpolarized down and transition\n    states in addition to up states'\n  expected:\n  - quantity: human active-slice cells with AIS-APs\n    value: 7\n    tolerance: 0\n  - quantity: human active-slice cells with RA-APs\n    value: 6\n    tolerance: 0\n  criterion: Human active-slice recordings without current injection, APs classed by readings (a) or\n    (b) of the header. How up, transition and down states are separated is not given (ref. 38,\n    dashed lines in Figure 3B). Readings are (i) a two-Gaussian fit to each cell's subthreshold\n    membrane potential histogram, down and up states within one SD of each mean and transition\n    between; (ii) the range between the two modes cut in thirds. The state of an AP is that of the\n    membrane potential at its threshold. Counts are exact, as the paper reports whole cells.\n    Reproduced when, under one reading, every cell with AIS-APs has all of them in up states and\n    the RA-APs fall in down or transition states in at least half of the cells with RA-APs;\n    partially reproduced when this holds with at most one exception.\n- id: fig3f-human-pre-ap-fluctuation\n  statement: In active human slices, membrane potential fluctuations (SD) 0 to 50 ms before AIS-APs\n    are larger than before RA-APs (1.49 against 0.78 mV).\n  source: Results, paragraph 3; Figure 3F\n  quote: Membrane potential fluctuations were increased 0 to 50 ms before AIS-APs (1.49 ± 1.76 mV)\n    compared to RA-APs (0.78 ± 1.7 mV, Mann-Whitney test, P < 0.001)\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.001\n    p_relation: <\n  expected:\n  - quantity: SD before AIS-APs\n    value: 1.49\n    tolerance: 0.149\n    unit: mV\n  - quantity: SD before RA-APs\n    value: 0.78\n    tolerance: 0.078\n    unit: mV\n  depends_on:\n  - fig3-human-ap-states\n  criterion: For each AP, the SD of the membrane potential in the 50 ms window before it. Where the\n    window ends is not given; readings are at the threshold and at the AP peak. APs are pooled\n    across cells (the paper gives no n, and P < 0.001 is not reachable with 6 or 7 cells); per-cell\n    medians are a variant. Reproduced when AIS-APs are higher with Mann-Whitney P < 0.001 and both\n    medians are within tolerance under one reading; partially reproduced when the test holds alone.\n- id: fig3i-rat-lfp-rhythm\n  statement: In active rat slices, layer 5 LFP shows rhythmic low-frequency deflections at 1.1 Hz,\n    synchronized to up states of the layer 1 interneurons.\n  source: Results, paragraph 3; Figure 3H and 3I\n  quote: In rat slices, somatic recordings in layer 1 interneurons ( n = 40) were accompanied by\n    layer 5 local field potential (LFP) recordings revealing rhythmic low-frequency (1.1 ± 0.55 Hz)\n    LFP deflections synchronized to single-cell up states\n  expected:\n    quantity: median LFP deflection frequency\n    value: 1.1\n    tolerance: 0.11\n    unit: Hz\n  criterion: How the deflection frequency is measured is not given. Readings are (i) the peak of the\n    LFP power spectrum in 0.5 to 4 Hz per recording; (ii) the rate of LFP troughs found on the 0.5\n    to 4 Hz Butterworth-filtered trace (the Methods' filter). The median over recordings is\n    compared. Reproduced when one reading is within tolerance.\n- id: fig3l-rat-spontaneous-ra-proportion\n  statement: In active rat slices, 13 of 40 layer 1 interneurons fire spontaneous RA-APs, and all\n    recovered ones (n = 5) are NGFCs.\n  source: Results, paragraph 3; Figure 3L\n  quote: Spontaneous RA-APs were observed in 13 interneurons (all recovered cells were NGFCs, n = 5).\n  expected:\n    quantity: rat active-slice cells with spontaneous RA-APs\n    value: 13\n    tolerance: 1.3\n  criterion: Rat active-slice recordings with LFP, APs classed by readings (a) or (b) of the header.\n    The morphology of the recovered cells is reported if the dandiset records it.\n- id: fig3k-rat-pre-ap-fluctuation\n  statement: In active rat slices, AIS-APs occur during up states with larger membrane potential\n    fluctuations before them, and RA-APs during down states with smaller ones.\n  source: Results, paragraph 3; Figure 3J and 3K\n  quote: AIS-APs and RA-APs of rat interneurons were detected with different threshold potentials\n    and pre-AP slopes and occurred during up and down states with higher and lower membrane\n    potential fluctuations, respectively\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.001\n    p_relation: <\n  depends_on:\n  - fig3l-rat-spontaneous-ra-proportion\n  criterion: As in fig3f-human-pre-ap-fluctuation, on the rat active-slice recordings. Reproduced\n    when the AIS-AP SD is higher with Mann-Whitney P < 0.001 under one reading.\n- id: fig3m-rat-ais-phase-coupling\n  statement: In active rat slices, AIS-APs are coupled near the trough of the slow LFP oscillation\n    (mean vector length 0.093, angle 314 degrees).\n  source: Results, paragraph 3; Figure 3M\n  quote: 'we found temporal coupling of AIS-APs to near the trough of slow oscillation (average\n    vector length: 0.093, angle: 314°, P < 0.001, Rayleigh test)'\n  statistics:\n  - test: Rayleigh test\n    p: 0.001\n    p_relation: <\n    n: 534 AIS-APs from 22 cells\n  expected:\n  - quantity: mean vector length, AIS-APs\n    value: 0.093\n    tolerance: 0.0093\n  - quantity: mean phase, AIS-APs\n    value: 314\n    tolerance: 31.4\n    unit: degrees\n  criterion: The phase method of the header, on the rat active-slice recordings with LFP; APs\n    pooled across cells. Which 22 cells form the population (all with both AP types, or all with\n    usable LFP) and whether 534 counts the APs before or after the delta power selection is not\n    said; the counts are reported under each. A 10% tolerance on an angle has no meaning near 0, so\n    the angle is within tolerance when it is within 31.4 degrees of 314 on the circle. Reproduced\n    when the Rayleigh test gives P < 0.001 and the mean phase is within tolerance; the vector\n    length is reported and judged within tolerance as well.\n- id: fig3m-rat-ra-no-phase\n  statement: In active rat slices, RA-APs show no phase preference to the slow LFP oscillation.\n  source: Results, paragraph 3; Figure 3M\n  quote: RA-APs showed no phase preference to network oscillations ( P = 0.07, Rayleigh test; Fig.\n    3M )\n  statistics:\n  - test: Rayleigh test\n    p: 0.071\n    n: 76 RA-APs from 22 cells\n  depends_on:\n  - fig3m-rat-ais-phase-coupling\n  criterion: A claim of absence, judged on the paper's Rayleigh test at P < 0.05 on the RA-APs\n    pooled, phases as in fig3m-rat-ais-phase-coupling. Reproduced when P >= 0.05; not reproduced\n    when P < 0.05. The mean vector length, angle and count of RA-APs are reported either way.\n- id: figs3-no-modulators\n  statement: In rat slices in in vivo-like ACSF without carbachol and SCH23390 (n = 90), elevated\n    network activity with low-frequency up states (0.11 Hz) appears and layer 1 interneurons fire\n    spontaneous RA-APs (4 NGFCs and 5 non-NGFCs).\n  source: Results, paragraph 3; Figure S3A to S3C\n  quote: Recordings from interneurons ( n = 90) in slices maintained without external cholinergic\n    and dopaminergic modulators provided similar results (fig. S3).\n  expected:\n  - quantity: up state frequency on the LFP\n    value: 0.11\n    tolerance: 0.011\n    unit: Hz\n  - quantity: cells with spontaneous RA-APs\n    value: 9\n    tolerance: 0.9\n  criterion: Rat slices without modulators. Up state frequency by the readings of\n    fig3i-rat-lfp-rhythm, in 0.05 to 4 Hz since 0.11 Hz is below the Methods' delta band (an\n    extension made here, the legend giving no method). Cells with RA-APs by readings (a) or (b) of\n    the header; 9 is the sum of the NGFC and non-NGFC counts of Figure S3C, which may count only\n    recovered cells, so the total count is reported as well. Reproduced when both values are within\n    tolerance under one reading; partially reproduced when RA-APs occur but a value is outside.\n- id: fig4b-invivo-ra-proportion\n  statement: In vivo, 75 of 242 (31%) mouse layer 1 interneurons fire spontaneous APs from\n    relatively hyperpolarized potentials, identified as RA-APs.\n  source: Results, paragraph 4; Figure 4B\n  quote: However, in 75 (31%) of the 242 recorded cells, we detected spontaneously occurring APs\n    rising from relatively hyperpolarized membrane potential\n  expected:\n    quantity: fraction of in vivo cells with RA-APs\n    value: 0.31\n    tolerance: 0.031\n  criterion: In vivo recordings, APs classed by readings (a) or (b) of the header; a cell has RAF\n    when it has at least one RA-AP. The counts are reported.\n- id: fig4i-invivo-frequencies\n  statement: In vivo layer 1 interneurons fire sporadically, with AIS-APs at 0.65 Hz and RA-APs at\n    0.004 Hz, AIS-APs being more frequent.\n  source: Results, paragraph 4; Figure 4I\n  quote: Overall, layer 1 interneurons fired sporadically (frequency of AIS-APs, 0.65 ± 2.4 Hz;\n    RA-APs, 0.004 ± 0.4 Hz; Mann-Whitney U test, P < 0.001)\n  statistics:\n  - test: Mann-Whitney U test\n    p: 0.001\n    p_relation: <\n    n: 242 cells\n  expected:\n  - quantity: median AIS-AP frequency\n    value: 0.65\n    tolerance: 0.065\n    unit: Hz\n  - quantity: median RA-AP frequency\n    value: 0.004\n    tolerance: 0.0004\n    unit: Hz\n  depends_on:\n  - fig4b-invivo-ra-proportion\n  criterion: Per cell, APs of each class over the recording duration. A median RA-AP frequency\n    above 0 means the median is not taken over all 242 cells (162 have none); readings are (i) all\n    242 cells; (ii) cells with RA-APs for the RA-AP value and all cells for the AIS-AP value; (iii)\n    cells with any APs. Reproduced when, under one reading, both medians are within tolerance and\n    AIS-APs are higher with Mann-Whitney P < 0.001; partially reproduced when the test holds alone.\n- id: fig4g-invivo-ra-share\n  statement: RA-APs make up 3.4% of all APs recorded in vivo; the RA-AP share ranges from 0 (162\n    cells) to 100% (6 cells), and averages 17% in the 75 cells with RAF.\n  source: Results, paragraph 4; Figure 4G and 4H\n  quote: the proportion of RA-APs represented 3.4% of all in vivo recorded APs in layer 1\n    interneurons. The ratio of RA-APs varied considerably in individual cells from 0 ( n = 162\n    cells) to 100% ( n = 6 cells), and the average contribution of RA-APs in interneurons with RAF\n    ( n = 75) was 17 ± 30%.\n  expected:\n  - quantity: RA-APs as a share of all in vivo APs\n    value: 3.4\n    tolerance: 0.34\n    unit: '%'\n  - quantity: cells with no RA-APs\n    value: 162\n    tolerance: 16.2\n  - quantity: cells with only RA-APs\n    value: 6\n    tolerance: 0.6\n  - quantity: average RA-AP share in cells with RAF\n    value: 17\n    tolerance: 1.7\n    unit: '%'\n  depends_on:\n  - fig4b-invivo-ra-proportion\n  criterion: Classes as in fig4b-invivo-ra-proportion. 242 minus 75 is 167, not 162; one reading is\n    that 5 cells fired no APs and have no ratio, the other that the counts come from different\n    selections; the count of cells with no APs is reported. \"Average\" may be the mean or the median\n    (the Statistics section); both are shown. Reproduced when, under one reading, at least three of\n    the four values are within tolerance.\n- id: fig4f-invivo-pre-ap-fluctuation\n  statement: In vivo, membrane potential fluctuations (SD) 0 to 50 ms before AIS-APs are larger than\n    before RA-APs.\n  source: Figure 4F\n  quote: ( F ) SD of membrane potential 0 to 50 ms before APs (Mann-Whitney test, P < 0.001).\n  statistics:\n  - test: Mann-Whitney test\n    p: 0.001\n    p_relation: <\n  depends_on:\n  - fig4b-invivo-ra-proportion\n  criterion: As in fig3f-human-pre-ap-fluctuation, on the in vivo recordings. The direction is read\n    from the Results, which say AIS-APs fire from up states with barrages of inputs. Reproduced\n    when the AIS-AP SD is higher with Mann-Whitney P < 0.001 under one reading.\n- id: fig4j-invivo-ais-phase-coupling\n  statement: In vivo, AIS-APs are coupled to the trough of the slow (0.5 to 4 Hz) LFP oscillation\n    (mean vector length 0.019, angle 330 degrees).\n  source: Results, paragraph 4; Figure 4J\n  quote: in vivo recorded AIS-APs were coupled to the trough (average vector length = 0.019, angle =\n    330°; P < 0.001, Rayleigh test) of population LFP\n  statistics:\n  - test: Rayleigh test\n    p: 0.001\n    p_relation: <\n  expected:\n  - quantity: mean vector length, AIS-APs\n    value: 0.019\n    tolerance: 0.0019\n  - quantity: mean phase, AIS-APs\n    value: 330\n    tolerance: 33\n    unit: degrees\n  depends_on:\n  - fig4b-invivo-ra-proportion\n  criterion: As in fig3m-rat-ais-phase-coupling, on the in vivo recordings, all cells with LFP and\n    all states (awake and anesthetized) pooled, as the paper reports one population. Reproduced\n    when the Rayleigh test gives P < 0.001 and the mean phase is within 33 degrees of 330 on the\n    circle; the vector length is reported and judged within tolerance as well.\n- id: fig4j-invivo-ra-no-phase\n  statement: In vivo, RA-APs are not significantly coupled to any phase of the slow oscillation.\n  source: Results, paragraph 4; Figure 4J\n  quote: as opposed to RA-APs, which were not significantly coupled to any phase of the slow\n    oscillation ( P = 0.15, Rayleigh test; Fig. 4J )\n  statistics:\n  - test: Rayleigh test\n    p: 0.15\n  depends_on:\n  - fig4j-invivo-ais-phase-coupling\n  criterion: A claim of absence, judged on the paper's Rayleigh test at P < 0.05 on the RA-APs\n    pooled. Reproduced when P >= 0.05; not reproduced when P < 0.05. The mean vector, the angle and\n    the count of RA-APs are reported either way.\n- id: fig4-invivo-up-down-balance\n  statement: In vivo, AIS-APs dominate during up states and RA-APs during down states, so the ratio\n    of the two swings over the slow oscillation.\n  source: Results, paragraph 4; Figure 4D and 4J\n  quote: The ratio of AIS-APs and RA-APs swings during slow population oscillations with dominating\n    AIS-APs and RA-APs in up states and down states, respectively.\n  depends_on:\n  - fig4j-invivo-ais-phase-coupling\n  criterion: The paper reports no measure or test for this sentence. With the Methods' phase\n    convention (trough 0 degrees is the up state, peak 180 degrees the down state), APs are split\n    by phase; readings are (i) halves of the cycle, up from 270 to 90 degrees and down from 90 to\n    270; (ii) quarters centred on 0 and 180 degrees. Reproduced when, under one reading, the share\n    of RA-APs among the APs in the down part exceeds that in the up part and AIS-APs outnumber\n    RA-APs in the up part. The paper's own test for two groups, here a Fisher exact test of the two\n    shares, is reported as support, not judged, as the paper does not name one for this.\n- id: figs4i-ais-ra-frequency-correlation\n  statement: Across in vivo cells, AIS-AP and RA-AP frequencies are weakly positively correlated (R\n    = 0.29).\n  source: Figure S4I and S4J\n  quote: (I) Frequency of AIS-APs and RA-APs (R=0.29, p<0.001)\n  statistics:\n  - test: correlation (type not named)\n    statistic: R = 0.29\n    p: 0.001\n    p_relation: <\n  expected:\n    quantity: correlation of AIS-AP and RA-AP frequency\n    value: 0.29\n    tolerance: 0.029\n  depends_on:\n  - fig4i-invivo-frequencies\n  criterion: Per-cell frequencies as in fig4i-invivo-frequencies. The correlation type and the cells\n    used are not named; readings are Pearson and Spearman, over all 242 cells and over the 75 cells\n    with RA-APs. Reproduced when, under one reading, R is within tolerance with P < 0.001;\n    partially reproduced when R is positive with P < 0.05.\n- id: figs5-not-genotype-or-anesthesia\n  statement: RA-AP occurrence in vivo cannot be explained by mouse genotype or by anesthesia\n    condition.\n  source: Figure S5A to S5D\n  quote: Fig. S5. RA-AP occurrence cannot be explained by genotype or anesthesia.\n  depends_on:\n  - fig4i-invivo-frequencies\n  criterion: A claim of absence for which the paper names no test; it shows per-cell RA-AP and\n    AIS-AP frequencies by genotype (GAD67-GFP, Ai9, C57BL/6J, vGAT-Ai9) and by condition (awake\n    after isoflurane, awake after ketamine-xylazine, under chloral hydrate, under\n    ketamine-xylazine). The paper's general rule names only two-group tests, so readings are (i)\n    Mann-Whitney U tests between every pair of groups, Bonferroni corrected; (ii) a Kruskal-Wallis\n    test across groups. Reproduced when neither reading finds a difference in RA-AP frequency at\n    P < 0.05 for genotype or for condition; not reproduced when both do; otherwise the outcome\n    rests on the reading. Group medians and the fraction of cells with RA-APs per group are\n    reported. Needs genotype and condition per cell from the dandiset's metadata.\n"
}
```

```
File created successfully at: claims/rozsa-2023.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i 's/  quote: we repeated these experiments/  quote: We repeated these experiments/' claims/rozsa-2023.yaml; python tools/claims_check.py claims/rozsa-2023.yaml paper/10.1126-sciadv.ade4511.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -e '—' -e 'rather' claims/rozsa-2023.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/rozsa-2023.yaml'));c=d['claims']
print(sum('criterion' in x for x in c), sum('statistics' in x for x in c), sum('expected' in x for x in c))"; git status --short
```

```
31 14 22
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
?? claims/rozsa-2023.yaml
?? scripts
```

**Agent**

I wrote `claims/rozsa-2023.yaml` with 31 claims. The quote checker passed (`tools/claims_check.py`): 31 quotes, 18 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record, open access (Europe PMC, PMC10569705), with its one supplement (`sciadv.ade4511_sm.pdf`: Figs. S1 to S6 and Table S1). The main figures were not available as images, so their values come from the Results and the legends. The reference list was not in the text, so I could not read refs. 28 (sag fraction) and 38 (cellular states). The paper links no code; it names only Fitmaster and custom MATLAB scripts.

**Claims:**
- 31 claims, all with quotes.
- 14 record the paper's statistics: paired and two-sample t tests, Mann-Whitney tests, Rayleigh tests, and one correlation whose type is not named.
- 22 have expected values. Every claim has a criterion.
- The claims cover RAF patterns and proportions in human and rat, cell-type dependence, soma versus bleb initiation order, ZD7288 effects, sag fraction, the 5 mM KCl puff, AP states and pre-AP fluctuation in slices, phase coupling in slices and in vivo, in vivo frequencies and RA-AP share, and Figs. S3 to S5.
- All claims use `data: dataset`. Two need morphology, genotype or anesthesia labels that the dataset may or may not hold; that is for the author to find.

**Details the paper leaves open, and the readings named:**
- **AIS-AP versus RA-AP boundary** (no numbers given): (a) labels in the dataset, (b) a two-component Gaussian mixture on threshold and pre-AP slope for each preparation, (c) in induction recordings, APs during the current pulses versus APs after them. Fig. 1C is tested without (b), which would be circular.
- **AP detection beyond the 5 mV/ms threshold:** peak above 0 mV as the standard choice, peak at least 30 mV above threshold as the variant.
- **RAF epochs:** one per cell, or one per induction run.
- **Sag fraction definition:** sag divided by the peak deflection, or by the steady-state deflection. The step used is also open: the most hyperpolarizing one, or the one whose peak is nearest -90 mV.
- **Up, transition and down states:** a two-Gaussian fit to the membrane potential histogram, or the range between the two modes cut in thirds.
- **Pre-AP SD window** ends at the threshold or at the AP peak. APs are pooled across cells, with per-cell medians as a variant.
- **Phase method:**
  - Butterworth filter order 2 (standard) or 4.
  - A zero-phase filter is the standard choice.
  - The 4 s window is centred on the AP.
  - Which 22 cells were used, and whether the AP counts are before or after the delta-power selection.
- **Medians or means** for the ZD7288 values and for the "average" 17% RA-AP share.
- **Median RA-AP frequency of 0.004 Hz in vivo:** it cannot be a median over all 242 cells, since 162 have none. Readings are all cells, cells with RA-APs, or cells with any APs.
- **Correlation in Fig. S4I:** Pearson or Spearman, over 242 or 75 cells.
- **Fig. S5 genotype and anesthesia** (no test named): pairwise Mann-Whitney with Bonferroni correction, or Kruskal-Wallis.
- **In vivo up/down balance** (no measure given): the cycle split into halves, or quarters centred on 0 and 180 degrees.
- **Tolerances:** the paper gives SD as spread (for example 88 ± 1828 RA-APs), so the expected values use 10% tolerances and the SDs are reported but not judged.

**Inconsistencies inside the paper, each recorded as alternative readings:**
- Human RAF cells are 87 of 385 in the Results but 83 of 358 in the sag analysis.
- Rat RAF cells are 102 of 259 in Fig. S1B but 97 of 254 in the sag analysis.
- In vivo, 242 minus 75 is 167 cells, but the paper says 162 cells had no RA-APs.

**Missing:** nothing the claims needed is missing from the paper and supplement. The definitions behind refs. 28 and 38 are cited but not stated in the text, so those two details are named as open.

## End of run

16 turns, 5 minutes, $1.45 at API prices, result: success.
