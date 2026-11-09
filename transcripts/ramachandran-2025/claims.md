# 000945 · claims · run 39873597931

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | sed -n '/Reader/,$p' | head -300; ls claims/001453/ paper/; ls claims/000945 2>/dev/null
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md | sed -n '60,400p'
```

```
finding.
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
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -250; wc -l paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 25,200p claims/001453/*.yaml
```

```
# pmc.ncbi.nlm.nih.gov).
schema_version: 2
dataset:
  archive: dandi
  id: "001453"
paper: doi:10.1016/j.cub.2025.04.027
claims:
- id: stimulus-code-link
  kind: link
  statement: The dandiset's stimulus codes can be linked to the stimuli the paper names, using
    the paper's analysis code and the protocol file of its stimulus software, and the values
    computed through that link agree with those the paper's code printed.
  source: Data and Code Availability; the paper's Fig1-S1.ipynb at GitLab commit 33a5c29
  data: with_labels
  criterion: Records are matched by the integer stimulus code. The link holds (reproduced) when
    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the
    species' median speeds for the nine whole-field stimuli computed here are within 10% of the
    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is
    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be
    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
[... 156 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^[a-z_]*:\|^  [a-z_]*:\|^- id\|^#" claims/001453/*.yaml | awk -F: '{print $2":"$3}' | sort | uniq -c | sort -rn | head -40; tail -40 claims/001453/*.yaml; cat tools/claims_check.py | head -60
```

```
13   statistics:
      8   data: with_labels
      7   depends_on:
      3 #:
      3   source: Results, Larval DC exhibit higher average swimming speeds, paragraph 1; Figure 1D
      2   expected:
      1 schema_version: 2
      1 paper: doi
      1 dataset:
      1 claims:
      1 - id: stimulus-code-link
      1 - id: figs1e-dc-respond-less-monocular
      1 - id: fig4hi-vspn-lateralized
      1 - id: fig4f-longer-on-duration
      1 - id: fig3e-longer-swims
      1 - id: fig3cd-zf-turn-more
      1 - id: fig2l-bi-ratio
      1 - id: fig2k-more-monocular
      1 - id: fig2h-fewer-motion-responsive
      1 - id: fig2g-dsi-similar
[... 120 more lines not kept]
```

**Agent**

Now the paper.

**Agent calls Bash**

```bash
wc -l paper/*.txt; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/f3028486-a29c-44cc-b7c0-265ff569404c/tool-results/b84b4l100.txt"
}
```

```
1	159 paper/10.1088-1741-2552-adbb1f.txt
2	DOI: 10.1088/1741-2552/adbb1f
3	Version: as served by europe_pmc
4	Source: europe_pmc+crossref (paper-text-fetcher)
5	Stored: 2026-10-20
6	Extracted: as fetched
7	------------------------------------------------------------------------
8	pmc J Neural Eng J Neural Eng jne JNEOBH Journal of Neural Engineering 1741-2560 1741-2552 IOP Publishing 11920894 40014879 jneadbb1f 10.1088/1741-2552/adbb1f adbb1f JNE-108412.R2 Paper Parameter-dependent cell-type specific effects of transcranial focused ultrasound stimulation in an awake head-fixed rodent model Ramachandran Sandhya 1 https://orcid.org/0000-0003-0860-2033 Gao Huan 1 Yttri Eric 2 3 https://orcid.org/0000-0002-4778-4389 Yu Kai 1 https://orcid.org/0000-0003-2944-8602 He Bin 1 2 * [removed: an e-mail address] 1 Department of Biomedical Engineering, Carnegie Mellon University , Pittsburgh, PA, United States of America 2 Neuroscience Institute, Carnegie Mellon University , Pittsburgh, PA, United States of America 3 Department of Biological Sciences, Carnegie Mellon University , Pittsburgh, PA, United States of America * Author to whom any correspondence should be addressed. 01 4 2025 19 3 2025 22 2 026022 06 12 2024 13 2 2025 27 2 2025 22 1 2025 19 3 2025 © 2025 The Author(s). Published by IOP Publishing Ltd 2025 https://creativecommons.org/licenses/by/4.0/ Original content from this work may be used under the terms of the Creative Commons Attribution 4.0 license . Any further distribution of this work must maintain attribution to the author(s) and the title of the work, journal citation and DOI. Abstract Objective. Transcranial focused ultrasound (tFUS) is a promising neuromodulation technique able to target shallow and deep brain structures with high precision. Previous studies have demonstrated that tFUS stimulation responses are cell-type specific, and specifically tFUS can elicit time-locked neural activity in regular spiking units (RSUs) that is sensitive to increases in pulse rep
[... 86 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/f3028486-a29c-44cc-b7c0-265ff569404c/tool-results/b84b4l100.txt",
 "offset": 95
}
```

```
95	10.1088/1741-2552/AC889F
96	
97	10.1016/J.BRS.2014.06.011
98	
99	10.1073/pnas.2206828119
100	
101	10.1523/JNEUROSCI.1020-12.2012
102	
103	10.1093/CERCOR/BHQ105
104	
105	10.1182/BLOOD.2023023718
106	
107	10.1016/J.BRS.2023.11.014
108	
109	10.1002/ADVS.202202345
110	
111	10.1038/s41467-024-46461-y
112	
113	10.1109/EMBC.2017.8036802
114	
[... 47 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rl "000945" --include=*.yaml --include=*.md --include=*.json . 2>/dev/null | head; ls; ls schemas
```

```
./transcripts/000130/author.md
./targets/dandisets.json
./targets/description_papers.yaml
./papers/manifest.yaml
LICENSE
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
    if '000945' in json.dumps(x): print(json.dumps(x,indent=1)[:3000])
E
grep -n -B2 -A12 "000945" papers/manifest.yaml targets/description_papers.yaml | head -60
```

```
[
 {
  "dandiset": "000003",
  "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
  "published_version": "0.260218.2052",
  "asset_count": 101,
  "size_gb": 2559.25,
  "data_standards": [
   "Neurodata Without Borders (NWB)"
  ],
  "species": [
   "House mouse"
  ],
  "approaches": [
   "electrophysiological approach",
   "behavioral approach"
  ],
  "papers": [
   {
    "doi": "10.1016/j.neuron.2016.12.011",
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'E'
import json
for x in json.load(open('targets/dandisets.json')):
    if x['dandiset']=='000945': print(json.dumps(x,indent=1))
E
ls claims/000946; sed -n 1,80p claims/000946/*.yaml
```

```
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
TypeError: string indices must be integers, not 'str'
10.1523-jneurosci.2218-24.2025.yaml
# Claims for Gao, Ramachandran, Yu & He (2025) on dandiset 000946.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
# protocol pilot-10 as stated in docs/protocol.md.
# Source: the version of record (J Neurosci 45(23) e2218242025, PMC12139594), full text as served
# by PMC: Abstract, Introduction, Materials and Methods, Results, figure legends and Discussion.
# The paper has no supplement (no Extended Data is cited). No PDF was supplied. The equation that
# defines the directional spike time tiling coefficient (dSTTC) is missing from the text read; only
# its description in words survives (Methods, Directional spike time tiling coefficient), and the
# symbols in that description are stripped. The paper links no analysis code, so no code was read.
#
# Data the paper used, as it reports them. Male Wistar rats under isoflurane (2%). Group 1 (N = 16):
# two 32-channel NeuroNexus probes, one in S1 (AP -2, ML 2.5, 1 to 1.3 mm deep, layers III to V)
# and one in POm (AP -4.5, ML 2.6, 5.8 mm). Group 2 (N = 12): S1 and auditory cortex (AC, AP -4.5,
# ML 6.5). tFUS from a 128-element array (1.5 MHz) aimed at S1, about 88 kPa in situ. Each session
# is one parameter set: 500 trials, ultrasound duration (UD) 67 ms, intersonication interval 2.5 s
# with 10% jitter, order of conditions randomized. PRFs 30, 300, 1500, 3000, 4500 Hz; duty cycles
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 80,200p claims/000946/*.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'));print(type(d), list(d)[:5] if isinstance(d,dict) else '')
"
```

```
#    no correction (the Methods name none for dSTTC). The STTC (Figs. 10C to F) is the STTC of
#    Cutts and Eglen without direction, between S1 RSUs and POm RSUs; its Delta t is not stated
#    and is taken as the dSTTC's 20 ms, and A1/A2, W1/W2 and S1/S2 apply to it as well. The STTC
#    values stored in the dandiset's STTC folders are shown as a variant.
#  - Group summaries of the STTC change (Figs. 10C to F): the legends do not say whether mean or
#    median is shown; M1, the mean, and M2, the median, are both readings wherever a criterion
#    ranks parameters by their change.
#  - The paper's p-values are reported for comparison; a claim's outcome rests on significance at
#    the paper's level and on the direction, plus the numbers under expected.
schema_version: 2
dataset:
  archive: dandi
  id: "000946"
paper: doi:10.1523/jneurosci.2218-24.2025
claims:
- id: fig4-unit-counts
  statement: In the 3000 Hz PRF (60% DC) sessions 312 RSUs and 54 FSUs were recorded from S1 and
    233 RSUs and 17 FSUs from POm; in the 30 Hz PRF (0.6% DC) sessions 148 RSUs and 61 FSUs from
    S1 and 189 RSUs and 43 FSUs from POm.
  source: Figure 4 legend
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
for x in d['targets']:
  if x.get('dandiset')=='000945': print(json.dumps(x,indent=1))
"; python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"
```

```
{
 "dandiset": "000945",
 "name": "Neural Spiking Data in the Awake Rat Somatosensory Cortex Responding to Trials of Transcranial Focused Ultrasound Stimulation",
 "published_version": "0.250829.1250",
 "asset_count": 75,
 "size_gb": 0.52,
 "data_standards": [
  "Neurodata Without Borders (NWB)"
 ],
 "species": [
  "Rattus norvegicus - Norway rat"
 ],
 "approaches": [
  "electrophysiological approach"
 ],
 "papers": [
  {
   "doi": "10.1088/1741-2552/adbb1f",
   "title": "Parameter-dependent cell-type specific effects of transcranial focused ultrasound stimulation in an awake head-fixed rodent model",
   "relation": "IsDescribedBy",
[... 156 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:4000]); print(list(s['properties']['claims']['items']['properties']))"
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
[... 83 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/000945/10.1088-1741-2552-adbb1f.yaml",
 "content": "# Claims for Ramachandran, Gao, Yttri, Yu & He (2025) on dandiset 000945.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22,\n# protocol as stated in docs/protocol.md.\n# Source: the version of record (J Neural Eng 22(2) 026022, PMC11920894), full text as served by\n# Europe PMC: Abstract, Introduction, Methods, Results, figure legends and Discussion. No PDF was\n# supplied. The supplementary materials (headpiece design, surgery, training, hydrophone scanning,\n# supplementary figures 2 and 4, supplementary table 1 of ISPTA values) were not supplied. No\n# claim rests on them: the analysis methods and the ISPTA of each PRF condition are given in the\n# main text (Methods 2.3 to 2.6). The paper links no analysis code (it names \"custom code\" in\n# MATLAB R2019a with FieldTrip), so no code was read.\n#\n# Data the paper used, as it reports them. Adult male Wistar rats, awake and head-fixed, with a\n# chronic 32-channel micro-electrode array in S1; tFUS from a 128-element array (f0 1.5 MHz,\n# 114 kPa peak-to-peak in situ at 15 V), ultrasound duration 67 ms, one trial every 2.5 s with\n# 10% jitter, 505 trials per parameter set, the first 5 cut (500 used). TDT recordings at 24 kHz,\n# bandpass 300 Hz to 5 kHz, units sorted in Offline Sorter. Batch 1 (10 rats): awake PRF series\n# at 30, 300, 1500, 3000 and 4500 Hz with 200 us tone-burst duration (TBD), at about 7 months;\n# the same PRF series under isoflurane at 9 months; awake DC series at 1500 Hz with TBD 40, 200\n# and 400 us (DC 6, 30 and 60%) at 10 months. Batch 2 (5 rats, 7 months): awake and anesthetized\n# recordings at a low PRF and 1500 Hz with 200 us TBD, and a sham at 1500 Hz aimed off target at\n# the front of the skull. The low PRF of batch 2 is given as 30 Hz in Methods 2.3 and as 300 Hz\n# in the next sentences and in Results 3.2; the author takes the PRF the dataset records. ISPTA\n# of the PRF series is 0.6, 6.03, 30.13, 60.26 and 90.39 mW/cm2. Measured variables are sorted\n# units' spike times and waveforms and the ultrasound trigger times. The dandiset is titled\n# \"Neural Spiking Data in the Awake Rat Somatosensory Cortex Responding to Trials of\n# Transcranial Focused Ultrasound Stimulation\" (reference 50 of the paper).\n#\n# Methods shared by the claims, from Methods 2.4 to 2.6 and the figure legends. Where the paper\n# leaves a detail open, the readings it allows are named with a label; a criterion that says\n# \"under every reading\" means every combination. A reading that could change an outcome is run\n# in all its forms; the outcome is the one they all give, and when they differ the claim is\n# blocked as methods_underspecified with every result shown.\n#  - Units. Every sorted unit of a session is one observation of that session's condition; the n\n#    of a test is the number of neurons in each group across all animals (Methods 2.6). Units are\n#    not selected for responsiveness (Methods 2.4). Methods 2.4 excludes \"PSTHs with visibly\n#    fluctuating baseline periods\" and manually ignores movement episodes; neither is defined.\n#    E1, no exclusion; E2, if the dataset marks excluded units or invalid intervals, they are\n#    left out. A unit with no spike in the baseline window cannot be normalized and is left out\n#    (a standard choice, reported with its count).\n#  - Cell type (Methods 2.5; Figure 3B, 3C). Features are the initial phase (onset to first\n#    baseline crossing) and after-hyperpolarization phase (first crossing to recrossing) of the\n#    unit's action potential; k-means with two clusters; the cluster of shorter durations is FSU,\n#    the other RSU. The paper sorts ambiguous units by spike rate by hand, with no rule. K0, if\n#    the dataset carries the paper's RSU/FSU labels, those are used and K1/K2 are variants. K1,\n#    k-means per animal over its units (Figure 3B clusters \"one animal's recordings\"); K2,\n#    k-means over all units pooled. Features from the unit's mean waveform.\n#  - Trials. T1, trials 6 to 505 (Methods 2.4, \"500 after 5 are cut from the beginning\");\n#    T2, all 505 trials (legends of Figures 4 to 7, \"over 505 trials\").\n#  - Normalized rate (Methods 2.4). Time 0 is the ultrasound trigger. The PSTH runs from -0.5 to\n#    1.5 s, bin 35.7 ms (Figure 4 legend), with a bin edge at 0, divided by the number of trials.\n#    Baseline is the mean rate in [-0.5, 0) s. The response is the mean rate in a window as a\n#    percent of baseline. Windows (Figure 5 to 7 legends): time-locked 0 to 67 ms; delayed 0.5 to\n#    1 s in awake recordings and 0.2 to 0.7 s in anesthetized ones. Whether \"percent of baseline\"\n#    is the ratio or the percent change does not change any rank test; group means are reported\n#    as the ratio in percent.\n#  - Group tests (Methods 2.6; Figure 5 to 7 legends). Kruskal-Wallis across the conditions of a\n#    panel, then two-sided Wilcoxon rank-sum tests between conditions (the groups hold different\n#    sessions, so a paired test does not apply), Bonferroni-corrected. Open, the groups: G1, the\n#    parameter levels of the panel; G2, the levels plus the sham sessions of the same state and\n#    window (the Results compare levels with sham). Bonferroni family: all pairs among the\n#    groups of the Kruskal-Wallis. The significance level is not stated; 0.05 after correction\n#    is used, the level the paper calls significant in Results 3.2 paragraph 3; whether each\n#    corrected p is also below the bound the paper prints is reported.\n#  - Two-way ANOVA (Results 3.2). Factors anesthesia (awake, anesthetized) and PRF (five levels)\n#    on the batch 1 PRF series, unit normalized rates, each state's own window. The model is not\n#    given. A1, both main effects and their interaction, type II sums of squares; A2, main\n#    effects only.\n#  - Delayed-response latency (Methods 2.4; Figure 4H, 4I). A unit has a significant delayed\n#    response when at least three consecutive PSTH bins are at or above baseline plus one SEM;\n#    its latency is the time of the first of them. Open, the SEM: S1, the SEM over the 14\n#    baseline bins of the trial-averaged PSTH; S2, the SEM over trials of the per-trial baseline\n#    rate, in spikes per bin. Open, the first bin allowed (\"any response after the ultrasound\n#    duration\"): D1, bins starting at or after 67 ms; D2, bins ending after 67 ms. Open, the time\n#    of a bin: L1, its start; L2, its centre. Sessions: FSU at 1500 Hz PRF, 200 us TBD (Figure 4H).\n#    Q1, the batch 1 PRF series sessions of each state; Q2, every on-target 1500 Hz, 200 us\n#    session of each state (adding the awake 30% DC sessions and batch 2).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000945\"\npaper: doi:10.1088/1741-2552/adbb1f\nclaims:\n- id: fig3-cell-type-sorting\n  statement: Units are sorted into fast spiking units (FSU) and regular spiking units (RSU) by\n    k-means clustering of the initial phase and after-hyperpolarization phase durations of their\n    action potentials; in one animal's recordings this gave 28 FSU and 32 RSU, 60 in total.\n  source: Figure 3B and 3C; Methods 2.5\n  quote: K -means clustering of detected neurons from one animal's recordings, showing 28 fast\n    spiking units (FSU) and 32 regular spiking units (RSU), for 60 total.\n  expected:\n  - quantity: FSU in the example animal\n    value: 28\n    tolerance: 2.8\n  - quantity: RSU in the example animal\n    value: 32\n    tolerance: 3.2\n  - quantity: units in the example animal\n    value: 60\n    tolerance: 6\n  criterion: The header's cell type method. The paper does not name the animal, nor whether its\n    \"recordings\" are one session or all of its sessions; the readings are R1, the units of one\n    session, and R2, the units of all of one animal's sessions in one series. Reproduced when,\n    under one reading, some animal gives all three counts within tolerance and the two clusters\n    separate on both features (the FSU cluster has the shorter median initial phase and\n    after-hyperpolarization phase). Partially reproduced when the clusters separate as stated\n    but no animal matches the counts. When the dataset carries the paper's labels (K0), the\n    agreement of K1 and K2 with them is reported.\n- id: fig4-rsu-time-locked-both-states\n  statement: RSUs show time-locked responses to tFUS, an increase in firing rate during the 67 ms\n    of stimulation, in both awake and anesthetized recordings.\n  source: Results 3.1, paragraph 1; Figure 4C and 4E\n  quote: We observed time-locked responses from RSU in both awake and anesthetized recordings, with\n    an observable increase in firing rate during tFUS stimulation\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: Figure 4 shows single examples at 1500 Hz PRF, 30% DC and reports no group test. The\n    paper's group test of a time-locked response is the comparison with sham (Results 3.2 and\n    3.3), so the claim is judged on it. RSU time-locked responses (0 to 67 ms) of the 1500 Hz,\n    200 us sessions against the sham sessions of the same state, two-sided Wilcoxon rank-sum, p\n    < 0.05, with the 1500 Hz mean above the sham mean and above 100%. Reproduced when this holds\n    in both states under every reading; partially reproduced when in one state only. The units\n    whose PSTH rises in 0 to 67 ms are counted per state.\n- id: fig4hi-fsu-delayed-latency\n  statement: FSU delayed responses to tFUS at 1500 Hz PRF begin later in awake rats (mean onset\n    0.51 s, spread 0.14 s) than under anesthesia (0.24 s, spread 0.08 s), and the onset\n    distributions differ significantly by a Wilcoxon rank-sum test.\n  source: Results 3.1, paragraph 1; Figure 4H and 4I\n  quote: In the anesthetized model, these delayed responses had an average onset latency of 0.24 s\n    ± 0.08 s, while in the awake model they had an average onset latency of 0.51 s ± 0.14 s ...\n    Comparing the distributions using the Wilcoxon rank-sum test, we found that delayed response\n    onset times varied significantly between awake and anesthetized models\n  statistics:\n  - test: Wilcoxon rank-sum test\n    p: 0.001\n    p_relation: \"<\"\n    n: FSU with a significant delayed response at 1500 Hz PRF, awake and anesthetized (counts\n      not given)\n  - about: as printed in the Figure 4 legend\n    test: Wilcoxon rank sum test\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: mean FSU delayed onset latency, anesthetized\n    value: 0.24\n    tolerance: 0.08\n    unit: s\n  - quantity: mean FSU delayed onset latency, awake\n    value: 0.51\n    tolerance: 0.14\n    unit: s\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: The header's latency method (readings S1/S2, D1/D2, L1/L2, Q1/Q2, T1/T2), FSU only.\n    The paper does not say whether the spread is an SD or an SEM; it is used as the tolerance.\n    Reproduced when, under every reading, both means are within tolerance and a two-sided\n    rank-sum test of awake against anesthetized latencies gives p < 0.001 with the awake values\n    later. Partially reproduced when the test holds with the awake values later but a mean is\n    outside tolerance. Not reproduced when the test fails or the direction is reversed.\n- id: fig4h-awake-latency-wider\n  statement: Awake FSU delayed-response onset latencies have a wider spread than anesthetized ones\n    and appear to have two peaks.\n  source: Results 3.1, paragraph 1; Figure 4H\n  quote: The awake model had a wider variance of onset latencies, and appears to have two peaks\n  depends_on:\n  - fig4hi-fsu-delayed-latency\n  criterion: Latencies as in fig4hi-fsu-delayed-latency. Reproduced when the SD of the awake\n    latencies exceeds that of the anesthetized latencies under every reading. The paper gives no\n    test of bimodality (\"appears to have two peaks\"), so the peaks do not decide the outcome; the\n    histogram in the paper's 35.7 ms bins and its local maxima are shown.\n- id: fig5a-rsu-time-locked-prf-awake\n  statement: In awake rats PRF is a significant factor for RSU time-locked responses; 30 Hz and\n    300 Hz PRF give lower responses than every higher PRF, 1500, 3000 and 4500 Hz do not differ,\n    and sham differs from every PRF but 30 Hz.\n  source: Results 3.2, paragraph 1; Figure 5A\n  quote: Examining the time-locked response from RSU in the awake model using Kruskal–Wallis ANOVA,\n    we find that PRF is a significant factor ... Post hoc tests show that 30 Hz and 300 Hz PRF\n    induced responses lower than all higher PRFs ... The sham condition was significantly different\n    than all but the 30 Hz condition ... 1500 Hz, 3000 Hz, and 4500 Hz showed no significant\n    differences\n  statistics:\n  - about: PRF as a factor\n    test: Kruskal-Wallis\n    p: 0.001\n    p_relation: \"<\"\n  - about: 30 and 300 Hz against each higher PRF\n    test: post hoc Wilcoxon\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  - about: sham against 300, 1500, 3000 and 4500 Hz\n    test: post hoc Wilcoxon\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: The header's group test, awake batch 1 PRF series, RSU, 0 to 67 ms; the sham is\n    the awake batch 2 sham. Six parts, each at corrected p < 0.05 - (1) the Kruskal-Wallis is\n    significant; (2) 30 Hz is below each of 1500, 3000 and 4500 Hz; (3) 300 Hz is below each of\n    them; (4) no pair among 1500, 3000 and 4500 Hz differs; (5) sham differs from 300, 1500, 3000\n    and 4500 Hz; (6) sham does not differ from 30 Hz. Reproduced when all six hold under every\n    reading; partially reproduced when (1) and at least four others hold; not reproduced\n    otherwise. Whether 30 Hz and 300 Hz differ is reported, as it separates this claim from\n    fig5c-rsu-time-locked-prf-anesth.\n- id: fig5c-rsu-time-locked-prf-anesth\n  statement: Under anesthesia RSU time-locked responses depend on PRF as in the awake model, the\n    only difference being that 30 Hz and 300 Hz do not differ significantly.\n  source: Results 3.2, paragraph 1; Figure 5C\n  quote: The anesthetized model had similar statistical results, with the only difference being\n    that no significant difference was observed between 30 Hz and 300 Hz PRF levels\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: As fig5a-rsu-time-locked-prf-awake, on the anesthetized batch 1 PRF series with the\n    anesthetized batch 2 sham, with part (3) read as 300 Hz below each of 1500, 3000 and 4500 Hz,\n    and a seventh part, that 30 Hz and 300 Hz do not differ (corrected p >= 0.05). Reproduced\n    when all parts hold under every reading; partially reproduced when the Kruskal-Wallis and at\n    least five others hold; not reproduced otherwise.\n- id: rsu-time-locked-anesthesia-factor\n  statement: Anesthesia is a significant factor in the RSU time-locked response by two-way ANOVA,\n    and it lowers the average magnitude of RSU responses.\n  source: Results 3.2, paragraph 1; Discussion, paragraph 5\n  quote: Two-way ANOVA additionally finds that anesthesia is a significant factor in the time-locked\n    response from RSU ... Anesthesia was observed to decrease the average magnitude of RSU responses\n  statistics:\n  - test: two-way ANOVA, anesthesia factor\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: The header's two-way ANOVA (A1 and A2) on RSU time-locked responses of the batch 1\n    PRF series. Reproduced when the anesthesia effect has p < 0.01 and the anesthetized mean,\n    over all PRF levels, is below the awake mean, under every reading. Partially reproduced when\n    the effect has 0.01 <= p < 0.05 with that direction. Per-PRF means of each state are shown.\n- id: fig5bd-fsu-time-locked-no-prf\n  statement: FSU time-locked responses show no significant differences across PRF levels, in\n    either the awake or the anesthetized model.\n  source: Results 3.2, paragraph 1; Figure 5B and 5D\n  quote: FSU in both the awake and the anesthetized model show no significant differences due to PRF\n    levels\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: A claim of absence, judged on the paper's test, the header's Kruskal-Wallis on FSU\n    time-locked responses (0 to 67 ms) across the five PRF levels of the batch 1 series (G1), in\n    each state at 0.05, with post hoc rank-sum tests at Bonferroni-corrected 0.05. Reproduced\n    when no Kruskal-Wallis and no post hoc pair is significant in either state; not reproduced\n    when any is. The effect sizes (the range of group medians) and the G2 test are shown.\n- id: fig5e-rsu-delayed-prf-awake\n  statement: Awake RSU delayed responses (0.5 to 1 s) depend on PRF, are highest at 1500 Hz and\n    3000 Hz with lower responses at both lower and higher PRFs, and every PRF is significantly\n    higher than sham.\n  source: Results 3.2, paragraph 2; Figure 5E\n  quote: RSUs in the awake rats had highest responses to 1500 Hz and 3000 Hz ... with a decrease at\n    both higher and lower frequencies, and all conditions found to be significantly higher than\n    sham\n  statistics:\n  - about: 1500 and 3000 Hz highest\n    test: post hoc Wilcoxon\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  - about: each PRF against sham\n    test: post hoc Wilcoxon\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: The header's group test, awake batch 1 PRF series and awake sham, RSU, 0.5 to 1 s.\n    Parts at corrected p < 0.05 - (1) the Kruskal-Wallis is significant; (2) each of 1500 and\n    3000 Hz is higher than each of 30, 300 and 4500 Hz; (3) each PRF is higher than sham. The\n    paper does not say whether 1500 and 3000 Hz must each beat every other level, so (2) is\n    also read as R2, the two highest means are those of 1500 and 3000 Hz and each is\n    significantly above 30 Hz and 4500 Hz. Reproduced when (1), (3) and (2) hold under one of\n    the readings of (2), under every other reading; partially reproduced when (1) and (3) hold\n    without (2), or (1) and (2) without (3).\n- id: fig5f-fsu-delayed-prf-awake\n  statement: Awake FSU delayed responses depend on PRF, are strongest at 4500 Hz, differ between\n    30 Hz and the three highest PRFs and between 300 Hz and the two highest, and at 30 Hz and\n    300 Hz are not significantly higher than sham.\n  source: Results 3.2, paragraph 2; Figure 5F\n  quote: FSUs in the awake model show the strongest responses to 4500 Hz PRF, with significant\n    differences between 30 Hz and the highest three PRFs, and 300 Hz and the highest two PRFs ...\n    30 Hz and 300 Hz were not found to be significantly higher than sham\n  statistics:\n  - test: post hoc Wilcoxon\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: The header's group test, awake batch 1 PRF series and awake sham, FSU, 0.5 to 1 s.\n    Parts - (1) the Kruskal-Wallis is significant; (2) the 4500 Hz mean is the highest; (3) 30\n    Hz differs from 1500, 3000 and 4500 Hz; (4) 300 Hz differs from 3000 and 4500 Hz; (5)\n    neither 30 Hz nor 300 Hz is significantly higher than sham. Significance at corrected p <\n    0.05. Reproduced when all hold under every reading; partially reproduced when (1) holds with\n    at least three of the others; not reproduced otherwise.\n- id: fig5gh-delayed-prf-anesth\n  statement: Under anesthesia PRF is a significant factor for the delayed responses (0.2 to 0.7 s)\n    of both RSUs and FSUs, which broadly prefer higher PRFs.\n  source: Results 3.2, paragraph 2; Figure 5G and 5H\n  quote: PRF was found to be a significant factor for RSU and FSU in both awake and anesthetized\n    settings ... Both RSUs and FSUs in the anesthetized rats had similar sensitivity as their\n    time-locked responses, broadly preferring higher PRFs\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: The header's Kruskal-Wallis on the anesthetized batch 1 PRF series, 0.2 to 0.7 s,\n    for RSU and FSU separately (G1). \"Broadly preferring higher PRFs\" is read as the mean of\n    1500, 3000 and 4500 Hz pooled exceeding that of 30 and 300 Hz pooled, the split the paper\n    uses for time-locked responses (Results 3.2 paragraph 1). Reproduced when, for both cell\n    types, the Kruskal-Wallis has p < 0.05 and the higher PRFs have the higher mean, under every\n    reading; partially reproduced when this holds for one cell type.\n- id: delayed-anesthesia-factor\n  statement: Anesthesia is a significant factor in the delayed response for both RSUs and FSUs by\n    two-way ANOVA, and it lowers the average response magnitude.\n  source: Results 3.2, paragraph 2; Discussion, paragraph 5\n  quote: Using two-way ANOVA, we found that anesthesia is a significant factor in the delayed\n    response for both RSU ... and FSU\n  statistics:\n  - about: RSU\n    test: two-way ANOVA, anesthesia factor\n    p: 0.001\n    p_relation: \"<\"\n  - about: FSU\n    test: two-way ANOVA, anesthesia factor\n    p: 0.01\n    p_relation: \"<\"\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: The header's two-way ANOVA (A1 and A2) on delayed responses of the batch 1 PRF\n    series, each state's own window. Reproduced when, under every reading, the anesthesia effect\n    has p < 0.001 for RSU and p < 0.01 for FSU, and in each cell type the anesthetized mean over\n    all PRF levels is below the awake mean (Discussion, paragraph 5, \"an average decrease in\n    response magnitude\" for FSU). Partially reproduced when both effects have p < 0.05 with\n    that direction but a bound is missed, or when one cell type holds.\n- id: fig6ad-time-adjacent-batch\n  statement: In the five rats recorded awake and anesthetized in the same week, time-locked\n    responses to the low PRF and 1500 Hz differ significantly in both states, with a reduced\n    response under anesthesia.\n  source: Results 3.2, paragraph 3; Figure 6A to 6D\n  quote: In analysis of the time locked responses, we observed significant differences in response\n    to 300 Hz PRF and 1500 Hz PRF stimulation in both awake and anesthetized conditions ... but with\n    a reduced response under anesthesia\n  statistics:\n  - test: Kruskal-Wallis with post hoc Wilcoxon\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Bonferroni\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: Batch 2 on-target sessions; the low PRF is the one the dataset records (30 Hz in\n    Methods 2.3, 300 Hz here). The text does not name the cell type; the Figure 6 legend says\n    panels A to D repeat Figure 5A, 5B, 5E and 5F, and the time-locked RSU panel is the one where\n    the Figure 5 PRF effect holds, so the claim is judged on RSU, 0 to 67 ms; FSU and the\n    delayed windows are shown as variants. In each state, low PRF against 1500 Hz by two-sided\n    rank-sum, Bonferroni-corrected over the pairs of the groups (G1, the two PRFs; G2, with the\n    sham). Reduced under anesthesia is judged, as no test is named, by the anesthetized mean at\n    1500 Hz being below the awake mean, with the rank-sum p shown. Reproduced when the PRF\n    difference has corrected p < 0.05 in both states and the reduction holds, under every\n    reading; partially reproduced when the PRF difference holds in one state.\n- id: fig6ef-rsu-ispta-rise-then-fall\n  statement: Awake RSU mean responses, time-locked and delayed, rise with ISPTA up to around 60\n    mW/cm2 and then decline.\n  source: Results 3.2, paragraph 4; Figure 6E and 6G\n  quote: We observe that RSU's in both their time-locked and delayed responses initially increase\n    till around 60 mW cm −2 , after which the response declines.\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: Means of the awake batch 1 PRF series RSU responses (Figure 5A and 5E values)\n    against the ISPTA of each PRF given in Methods 2.3. Results 3.2 paragraph 4 also says the\n    1500 Hz (30.13 mW/cm2) mean is the highest time-locked one, so the peak is read as the mean\n    at 1500 or 3000 Hz. Reproduced when, for both windows, the highest mean is at 1500 or 3000\n    Hz, the means rise from 30 Hz to that peak, and the 4500 Hz mean is below the peak, under\n    every reading. Partially reproduced when this holds for one window. No test is reported;\n    the SEM of each mean is shown.\n- id: fig6fh-fsu-ispta\n  statement: Awake FSUs show no time-locked response, and their delayed response increases almost\n    linearly with ISPTA.\n  source: Results 3.2, paragraph 4; Figure 6F and 6H\n  quote: FSU's show no time-locked response, and their delayed response increases almost linearly\n    with I SPTA .\n  depends_on:\n  - fig3-cell-type-sorting\n  - fig5bd-fsu-time-locked-no-prf\n  criterion: Means of the awake batch 1 PRF series FSU responses against ISPTA. The paper gives\n    no measure of \"no time-locked response\" beyond the absence of a PRF effect, so that part\n    takes the outcome of fig5bd-fsu-time-locked-no-prf for the awake state. The delayed part\n    holds when the five delayed means increase with ISPTA (Spearman rho = 1 over the five\n    points); \"almost linearly\" has no threshold in the paper, so the Pearson r of the means\n    against ISPTA is reported and does not decide. Reproduced when both parts hold under every\n    reading; partially reproduced when one does.\n- id: fig5a-1500-highest-time-locked-mean\n  statement: Among PRFs, 1500 Hz gives the highest mean RSU time-locked response in awake rats,\n    although not significantly above 3000 and 4500 Hz.\n  source: Results 3.2, paragraph 4; Figure 5A\n  quote: Although it is not statistically significant, we found that 1500 Hz produces the highest\n    mean time-locked response\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: Means of awake batch 1 PRF series RSU responses, 0 to 67 ms. Reproduced when the\n    1500 Hz mean is the highest of the five under every reading; the corrected rank-sum p of\n    1500 Hz against 3000 and 4500 Hz is shown.\n- id: fig7a-rsu-time-locked-dc\n  statement: Awake RSU time-locked responses at 1500 Hz PRF are significantly lower at 6% DC than\n    at 60% DC, and every DC is significantly higher than sham.\n  source: Results 3.3, paragraph 1; Figure 7A\n  quote: Time-locked responses from RSUs showed a significantly lower response to 6% DC than those\n    to 60%, with all conditions significantly higher than sham\n  statistics:\n  - test: Kruskal-Wallis with post hoc Wilcoxon\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: The header's group test on the awake batch 1 DC series (6, 30, 60%) with the awake\n    sham, RSU, 0 to 67 ms. Parts at corrected p < 0.05 - (1) the Kruskal-Wallis is significant;\n    (2) 6% is below 60%; (3) each DC is above sham. Reproduced when all hold under every reading;\n    partially reproduced when (1) and one of (2) and (3) hold. The Figure 7A legend also says 6%\n    is lower than 30%; that pair is reported and does not decide.\n- id: fig7a-60-highest-time-locked-mean\n  statement: By mean values 60% DC gives the strongest RSU time-locked response, though it is only\n    significantly higher than 6%.\n  source: Results 3.3, paragraph 1; Figure 7A\n  quote: Based on mean values, 60% DC appears to produce the strongest time-locked response,\n    although it is only statistically significantly higher than the 6% condition.\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: Means of awake DC series RSU responses, 0 to 67 ms. Reproduced when the 60% mean is\n    the highest of the three under every reading; the corrected rank-sum p of 60% against 30%\n    is shown.\n- id: fig7b-fsu-time-locked-dc\n  statement: FSUs show no time-locked response across DC levels; no significant differences are\n    observed.\n  source: Results 3.3, paragraph 1; Figure 7B\n  quote: no time-locked response was observed as in the PRF study\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: A claim of absence, judged on the paper's test, the header's Kruskal-Wallis on FSU\n    time-locked responses across 6, 30 and 60% DC (G1) at 0.05, with post hoc rank-sum tests at\n    Bonferroni-corrected 0.05. Reproduced when none is significant; not reproduced when any is.\n    The group medians and the G2 test are shown.\n- id: fig7c-rsu-delayed-dc\n  statement: Awake RSU delayed responses prefer 30% DC over 6% and 60%, and at 60% DC they do not\n    differ from sham.\n  source: Results 3.3, paragraph 1; Figure 7C\n  quote: Delayed responses however preferred 30% DC over 6% and 60% ... and 60% DC showed no\n    significant difference from sham\n  statistics:\n  - test: Kruskal-Wallis with post hoc Wilcoxon\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: The header's group test on the awake DC series with the awake sham, RSU, 0.5 to 1\n    s. Parts - (1) the Kruskal-Wallis is significant; (2) 30% is above 6% and above 60%; (3)\n    60% does not differ from sham. Significance at corrected p < 0.05. Reproduced when all hold\n    under every reading; partially reproduced when (1) and (2) hold without (3), or (1) and (3)\n    with 30% above one of the two. The Figure 7C legend's \"between all DCs\" (6% against 60%) is\n    reported.\n- id: fig7d-fsu-delayed-dc\n  statement: Awake FSU delayed responses are significantly higher at 60% DC than at 6%, and at 6%\n    DC they do not differ from sham.\n  source: Results 3.3, paragraph 1; Figure 7D\n  quote: Delayed responses from FSUs showed a significantly higher response to 60% DC over 6% ...\n    with 6% DC found to be not significantly different from sham\n  statistics:\n  - test: Kruskal-Wallis with post hoc Wilcoxon\n    p: 0.001\n    p_relation: \"<\"\n    corrected: Bonferroni\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: The header's group test on the awake DC series with the awake sham, FSU, 0.5 to 1\n    s. Parts - (1) the Kruskal-Wallis is significant; (2) 60% is above 6% at corrected p <\n    0.05; (3) 6% does not differ from sham. Reproduced when all hold under every reading;\n    partially reproduced when (1) and (2) hold without (3).\n- id: sham-no-auditory-response\n  statement: The off-target sham at 1500 Hz PRF produced no significant response, so the\n    activation is not attributed to an auditory or skull-conduction confound.\n  source: Discussion, paragraph 9; Methods 2.3\n  quote: In this study we additionally performed a sham condition delivering ultrasound off target\n    to the front of the skull, and did not observe any significant response.\n  depends_on:\n  - fig3-cell-type-sorting\n  criterion: A claim of absence. The paper names no test of the sham against baseline; its only\n    tests involving sham compare it with on-target conditions (Results 3.2, 3.3), and those are\n    judged in their own claims. The Methods tests (Kruskal-Wallis with post hoc rank-sum) have\n    no baseline group, so the claim is blocked as methods_underspecified unless the author\n    finds the paper's test in a later answer; the sham's mean normalized rates for RSU and FSU\n    in each window and state are shown.\n"
}
```

```
File created successfully at: claims/000945/10.1088-1741-2552-adbb1f.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd claims/000945 && f=10.1088-1741-2552-adbb1f.yaml && sed -i "s/Discussion, paragraph 5/Discussion, paragraph beginning 'Although these results demonstrate'/; s/(Discussion, paragraph 5, \"an average/(Discussion, \"an average/; s/source: Discussion, paragraph 9; Methods 2.3/source: Discussion, paragraph beginning 'One potential confound'; Methods 2.3/" $f && grep -n "Discussion" $f
```

```
5:# Europe PMC: Abstract, Introduction, Methods, Results, figure legends and Discussion. No PDF was
221:  source: Results 3.2, paragraph 1; Discussion, paragraph beginning 'Although these results demonstrate'
315:  source: Results 3.2, paragraph 2; Discussion, paragraph beginning 'Although these results demonstrate'
332:    all PRF levels is below the awake mean (Discussion, paragraph beginning 'Although these results demonstrate', "an average decrease in
481:  source: Discussion, paragraph beginning 'One potential confound'; Methods 2.3
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000945/10.1088-1741-2552-adbb1f.yaml",
 "old_string": "(Discussion, paragraph beginning 'Although these results demonstrate', \"an average decrease in",
 "new_string": "(Discussion, \"an average decrease in"
}
```

```
The file claims/000945/10.1088-1741-2552-adbb1f.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000945/10.1088-1741-2552-adbb1f.yaml",
 "old_string": "    judged in their own claims. The Methods tests (Kruskal-Wallis with post hoc rank-sum) have\n    no baseline group, so the claim is blocked as methods_underspecified unless the author\n    finds the paper's test in a later answer; the sham's mean normalized rates for RSU and FSU\n    in each window and state are shown.",
 "new_string": "    judged in their own claims. The Methods tests (Kruskal-Wallis with post hoc rank-sum) have\n    no baseline group. What the sham is compared with is therefore open, and this file names\n    no reading the text supports; the sham's mean normalized rates for RSU and FSU in each\n    window and state are to be shown."
}
```

```
The file claims/000945/10.1088-1741-2552-adbb1f.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
cd  && python tools/claims_check.py claims/000945/10.1088-1741-2552-adbb1f.yaml paper/10.1088-1741-2552-adbb1f.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "—\|rather" claims/000945/*.yaml; python -c "
import yaml;d=yaml.safe_load(open('claims/000945/10.1088-1741-2552-adbb1f.yaml'))
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"
```

```
22 10 22 2
```

**Agent**

I wrote `claims/000945/10.1088-1741-2552-adbb1f.yaml`. The quote checker reports 22 claims, 22 quotes, 15 statistical values and 0 problems. Nothing is committed.

**Text read:** the version of record (J Neural Eng 22(2) 026022, PMC11920894), as served by Europe PMC. It has the main text, Methods, figure legends and Discussion. There was no PDF and no supplement. The supplement holds the headpiece, surgery, training and beam-scan details and Supplementary Table 1 (ISPTA values). No claim rests on it, because the analysis methods and the ISPTA of each PRF condition are in the main text, so I went ahead. The paper links no code (only "custom code" in MATLAB with FieldTrip), so I read no code.

**Claims:** 22, all with quotes. 10 carry statistics (Kruskal-Wallis with Bonferroni-corrected post hoc Wilcoxon, two-way ANOVA, and the rank-sum test on latencies). All 22 have criteria, and 2 have expected values: the Fig 3B unit counts (28 FSU, 32 RSU, 60 in total) and the latencies (0.24 ± 0.08 s anesthetized, 0.51 ± 0.14 s awake). The claims cover cell-type sorting, the PRF and DC effects on RSU and FSU in the time-locked and delayed windows, both two-way ANOVA anesthesia effects, the batch of five rats, the response curves against ISPTA, and the sham.

**Details the paper leaves open, and the readings named:**
- **Excluded units:** "visibly fluctuating" baselines and movement periods were removed by hand. E1: no exclusion. E2: use the dataset's marks, if it has any.
- **Cell type:** K0 uses the paper's labels if the dataset has them. Otherwise k-means per animal (K1) or over all units pooled (K2). The paper's hand sorting of unclear units by spike rate has no rule.
- **Trials:** 500 after cutting the first 5 (T1, from the Methods) or all 505 (T2, from the legends).
- **Groups in the Kruskal-Wallis:** the parameter levels alone (G1) or with sham added (G2). The significance level is never stated; I used corrected 0.05.
- **Two-way ANOVA:** with interaction, type II (A1), or main effects only (A2).
- **Latency:**
  - What the SEM is taken over: the baseline bins (S1) or the trials (S2).
  - Which bin may come first after 67 ms: D1 or D2.
  - Whether a bin's time is its start or its centre: L1 or L2.
  - Which sessions: the PRF series only (Q1) or every on-target 1500 Hz session (Q2).
  - Whether "±" is an SD or an SEM. I used it as the tolerance.
- **Fig 3B example:** the animal is not named, nor whether the count is from one session or all of its sessions (R1 or R2).
- **Delayed RSU peak (Fig 5E):** whether 1500 and 3000 Hz must each beat every other level (strict) or only be the two highest means (R2).
- **Fig 6A–D:** the text does not name the cell type. The claim is judged on time-locked RSU, and the other panels are shown as variants.

**Missing from the paper:**
- **Sham claim (Discussion):** the paper names no test of sham against baseline. Its criterion says this is open and names no reading.
- **Fig 4 time-locked RSU response:** there is no group test of it. It is judged by the paper's own comparison with sham.
- **Fig 4H "two peaks" and Fig 6 "almost linearly":** the paper gives no test or threshold for either. They are shown but do not decide the outcome.
- **Contradictions inside the paper:**
  - The low PRF of the five-rat batch is 30 Hz in the Methods and 300 Hz in the next sentences and the Results. The author takes the PRF the dataset records.
  - Fig 7A: the Results say 6% DC is lower than 60%; the legend adds lower than 30%.
  - Fig 7C: the legend says "all DCs" differ, which the Results do not state.
  - Fig 6A–D: the legend says the panels are 0–67 ms but also that they repeat Fig 5's delayed panels.
  - Latency: the Results give p < 0.001, the legend p < 0.0001.

  In each case the claim follows the Results text and the other version is reported without deciding the outcome.

## End of run

21 turns, 4 minutes, result: success.
