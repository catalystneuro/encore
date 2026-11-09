# 000637 · claims · run 39908630774

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/ claims/000637 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  awk '/^## Reader/,/^## Author/' docs/protocol.md; ls claims/001453/ paper/ claims/000637 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/001453/*.yaml | head -150; wc -c paper/*.txt
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.2218-24.2025.txt"
}
```

Result: not kept, because it reads the paper's text.

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1523-jneurosci.2218-24.2025.txt",
 "offset": 326
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 150,400p claims/001453/*.yaml; cat tools/claims_check.py | head -80
```

```
data: with_labels
  depends_on:
  - stimulus-code-link
  criterion: For each fish, the mean of its median angular velocities for the rightward
    stimuli (right, forward right, backward right) minus the mean for the leftward stimuli
    (left, forward left, backward left). Reproduced when this difference is greater than zero
    in each species by a one-sided Wilcoxon signed-rank test at p < 0.05; partially reproduced
    when it holds in one species only. The per-stimulus species medians are reported as well.
- id: fig1h-zf-higher-angular-acceleration
  statement: Across directional stimuli ZF have higher angular acceleration than DC, and the
    distributions of the two species differ for every stimulus.
  source: Results, Optic flow induces angular matching and turns in DC, paragraph 2; Figure 1H
    (Kruskal-Wallis test with Bonferroni correction)
  quote: Across directional stimuli, ZF maintained higher angular acceleration than DC
  statistics:
  - test: Kruskal-Wallis test
    p: 0.05
    p_relation: "<"
    corrected: Bonferroni
  data: with_labels
[... 232 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rl "000637" --include=* . 2>/dev/null | grep -v "^./.git/" | head; grep -n -i "github\|code avail\|supplement\|extended data" paper/*.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'E'
import json
d=json.load(open('targets/dandisets.json'))
items = d if isinstance(d,list) else d.get('dandisets', d)
if isinstance(items,dict):
    for k,v in items.items():
        if '000637' in k: print(k, json.dumps(v,indent=1)[:4000])
else:
    for v in items:
        if '000637' in json.dumps(v): print(json.dumps(v,indent=1)[:4000])
E
grep -n -B3 -A12 "000637" targets/description_papers.yaml papers/manifest.yaml
```

```
targets/description_papers.yaml-46-    - doi: 10.1101/2022.11.08.515739
targets/description_papers.yaml-47-      title: "Signature morpho-electric properties of diverse GABAergic interneurons in the human neocortex"
targets/description_papers.yaml-48-      note: The description says the data accompany this manuscript.
targets/description_papers.yaml:49:  "000637":
targets/description_papers.yaml-50-    - doi: 10.1523/jneurosci.2218-24.2025
targets/description_papers.yaml-51-      title: "Transcranial Focused Ultrasound Modulates Feedforward and Feedback Cortico-Thalamo-Cortical Pathways by Selectively Activating Excitatory Neurons"
targets/description_papers.yaml-52-      note: The description says the dataset is described in this paper.
targets/description_papers.yaml-53-  "000894":
targets/description_papers.yaml-54-    - doi: 10.1016/j.cell.2021.05.026
targets/description_papers.yaml-55-      title: "Modularity and robustness of frontal cortical networks"
targets/description_papers.yaml-56-      note: The description says part of the experiments are described in this paper.
targets/description_papers.yaml-57-  "000897":
targets/description_papers.yaml-58-    - doi: 10.1038/s41586-024-07557-z
targets/description_papers.yaml-59-      title: "Mental navigation in the primate entorhinal cortex"
targets/description_papers.yaml-60-      note: Named in the description of DANDI:001275, which says the paper's entorhinal cortex data are in this dandiset.
targets/description_papers.yaml-61-  "000943":
--
papers/manifest.yaml-937-    source: ncbi_pmc+crossref (paper-text-fetcher)
papers/manifest.yaml-938-    pdf: false
papers/manifest.yaml-939-    supplements: 0
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A25 '"000637"' targets/dandisets.json | head -60
```

```
3193:   "dandiset": "000637",
3194-   "name": "Neural Spike Time Response Data in Anesthetized Rats in the Primary Somatosensory Cortex with Phased Ultrasound Array Stimulation",
3195-   "published_version": "0.250829.1249",
3196-   "asset_count": 292,
3197-   "size_gb": 1.16,
3198-   "data_standards": [
3199-    "Neurodata Without Borders (NWB)"
3200-   ],
3201-   "species": [
3202-    "Rattus norvegicus - Norway rat"
3203-   ],
3204-   "approaches": [
3205-    "electrophysiological approach"
3206-   ],
3207-   "papers": [
3208-    {
3209-     "doi": "10.1523/jneurosci.2218-24.2025",
3210-     "title": "Transcranial Focused Ultrasound Modulates Feedforward and Feedback Cortico-Thalamo-Cortical Pathways by Selectively Activating Excitatory Neurons",
3211-     "relation": "IsDescribedBy",
3212-     "resource_type": null,
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000637/versions/0.250829.1249/info/ | python -c "import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m.get('description')); print(m.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  cat schemas/claims.schema.json | head -200
```

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "Claims proposed for one target (a dataset and one of its papers)",
  "description": "Draft. To be revised after the pilot.",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "schema_version",
    "dataset",
    "paper",
    "claims"
  ],
  "properties": {
    "schema_version": {
      "const": 2
    },
    "dataset": {
      "description": "The dataset the claims are tested on: the archive and the dataset's identifier there.",
      "type": "object",
      "additionalProperties": false,
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,320p schemas/claims.schema.json
```

```
}
    },
    "checks": {
      "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "date",
          "kind",
          "ready"
        ],
        "properties": {
          "date": {
            "type": "string",
            "format": "date"
          },
          "kind": {
            "enum": [
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p claims/000637; echo $TMPDIR
```

```
/tmp/claude-1001
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/gen.py",
 "content": "import yaml\n\nHEADER = \"\"\"\\\n# Claims for Gao, Ramachandran, Yu & He (2025), J Neurosci 45(23):e2218242025, on dandiset 000637.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record as served by PubMed Central (PMC12139594), full text with\n# Materials and Methods, Results, figure legends and Discussion (paper/10.1523-jneurosci.2218-24.2025.txt).\n# The paper has no supplement. No PDF was supplied. The equation defining the directional spike time\n# tiling coefficient (dSTTC) is lost in the text (\"The definition for dSTTC is as follows:\" is followed\n# by the prose that defines its terms, without the formula); its form is treated as open below.\n# The paper links no analysis code (no repository and no code availability statement in the text),\n# so no code was read.\n#\n# Data the paper used (Materials and Methods). Male Wistar rats (Hsd WI), 250 to 350 g, 3 to 6 months,\n# under 2% isoflurane. Group 1 (N = 16): two 32-channel NeuroNexus probes, one in S1 (AP -2, ML 2.5,\n# 40 degrees, 1 to 1.3 mm deep, layers III to V) and one in POm (AP -4.5, ML 2.6, 20 degrees, 5.8 mm).\n# Group 2 (N = 12, auditory confound): probes in S1 and auditory cortex (AC; AP -4.5, ML 6.5).\n# tFUS from a 128-element random array (H276, 1.5 MHz) steered to S1; ultrasound duration (UD) 67 ms;\n# intersonication interval 2.5 s with 10% jitter; 500 trials per parameter; condition order randomized.\n# Conditions: PRF 30, 300, 1500, 3000 and 4500 Hz at constant 200 us pulse duration (which gives DC 0.6,\n# 6, 30, 60 and 90%); DC 0.6, 6, 30, 60 and 90% at 3000 Hz and at 30 Hz PRF; PRFs at constant 60% DC;\n# sham sessions without tFUS; control sessions with tFUS steered to cingulate cortex (CG1, AP 3, ML 0).\n# Recorded with a TDT system, band-passed 300 Hz to 5 kHz, sorted in Plexon Offline Sorter (threshold\n# -3.5 SD, k-means). Measured variables: spike times and waveforms of sorted units, and stimulus onset\n# times. The paper says all its data are in DANDI:000946 (Data acquisition and preprocessing). The\n# description of dandiset 000637 lists S1 recordings with a 32-channel array, PRFs 30 to 4500 Hz and\n# pulse durations of 100, 200 and 400 us (called UDs there), 500 trials per recording, spike times and\n# trial event times. Which of the paper's groups and conditions it holds (POm, AC, sham, CG1, the DC\n# series) is the author's to find; the claims below cover all the paper's findings.\n#\n# Shared methods, cited to the paper. Criteria refer to them by name.\n#\n# Method S (spiking responses). Units: sorted units with more than 2,000 spikes in the session\n# (Methods, Neuronal type classification). Cell type: the initial phase (IP, onset to recrossing of\n# baseline) and afterhyperpolarization period (AHP, end of IP to its recrossing of baseline) of the\n# waveform, clustered by k-means into two clusters; the cluster with the shorter, narrower waveforms is\n# FSU (Methods, citing Bartho et al. 2004), the other RSU. Open, could change the outcome: (K1) k-means\n# over all units of one recording area pooled across sessions, or (K2) over all units of all areas\n# pooled; IP and AHP are taken from each unit's mean waveform (the paper measures them \"for each\n# identified spike\"; a per-unit median of per-spike values is a variant). The k-means seed is a standard\n# choice. A unit is counted once per session it was recorded in (the n per condition in Figures 4 and 6\n# to 9 differ by condition, so units are counted per session). Windows are 67 ms long aligned to tFUS\n# onset, as the Results name them: pre-stimulus -67 to 0 ms (Methods), during sonication 0 to 67 ms,\n# then 67 to 134, 134 to 201 and 201 to 268 ms; \"delayed\" or \"postsonication\" means 201 to 268 ms from\n# Figure 6 on (Results, tFUS parameters, paragraph 1). Normalized spiking rate: a unit's rate in the\n# window normalized to the 67 ms before each stimulation (Methods), in percent. Open, could change the\n# outcome: (N1) the unit's spike count in the window summed over trials divided by its count in the\n# pre-stimulus window summed over trials; (N2) the mean over trials of the per-trial ratio, trials\n# without a pre-stimulus spike left out. Tests (Methods, Statistical analysis; Figure 4 legend):\n# Kruskal-Wallis H test across conditions (or windows) of units' normalized rates; post hoc one-tailed\n# two-sample Wilcoxon tests with Bonferroni correction; significance at 0.01 for spiking. The reported\n# p-values are taken to be Bonferroni-corrected (several are printed as p = 1.0). Open, could change the\n# outcome: the two samples of a test against baseline are (W1) units' rates in the window against units'\n# rates in the pre-stimulus window, Wilcoxon rank-sum, or (W2) the same pairs per unit, Wilcoxon\n# signed-rank; the Bonferroni count is (M1) the number of conditions or windows in the panel each tested\n# against baseline, or (M2) the number of all pairs among them and baseline. The tail is the direction\n# the claim states. Under these readings a claim is reproduced when every reading gives its outcome; when\n# readings give different outcomes it is blocked as methods_underspecified, with all results shown.\n#\n# Method D (directional correlation). dSTTC between a unit A and a unit B recorded in the same session,\n# \"A to B\" meaning that A's spikes precede B's (Methods, Directional spike time tiling coefficient):\n# PA is the fraction of A's spikes within dt = 20 ms before a spike of B, TB the fraction of time\n# covered by the 20 ms before each spike of B, PB the fraction of B's spikes within 20 ms after a spike\n# of A, TA the fraction of time covered by the 20 ms after each spike of A. The formula is missing from\n# the text read. Reading taken from the terms and from the STTC it modifies (Cutts and Eglen 2014),\n# dSTTC = 1/2 [(PA - TB) / (1 - PA TB) + (PB - TA) / (1 - PB TA)]; if the PDF shows another form, that\n# form replaces it. dSTTC is computed trial by trial (Methods) in the 67 ms windows of Method S, with time\n# fractions taken within the window; a trial where either unit has no spike in the window gives no value.\n# Normalized dSTTC (Methods; formula not given) is open: (D1) the window's dSTTC minus the pre-stimulus\n# dSTTC, or (D2) that difference divided by the absolute pre-stimulus dSTTC, per pair, from the means\n# over trials. Tests: Kruskal-Wallis H across windows or parameters and post hoc one-tailed two-sample\n# Wilcoxon tests against the pre-stimulus window, significance 0.05 (Methods; Figure 10 legend, \"compared\n# with prestimulation correlation\"); W1 and W2 as in Method S. No Bonferroni correction is stated for\n# dSTTC. Cell types and units as in Method S.\n#\n# Method T (traditional STTC, Figure 10C to F). STTC of Cutts and Eglen (2014), dt = 20 ms, between S1\n# RSUs and POm RSUs of the same session (Results, tFUS elicited correlation change, paragraph 2), trial\n# by trial in the pre-stimulus and during-sonication windows; the change is during minus pre-stimulus\n# (D1) or that divided by the absolute pre-stimulus value (D2), per pair; Kruskal-Wallis across the five\n# parameter levels and post hoc one-tailed two-sample Wilcoxon tests, significance 0.05.\n\"\"\"\n\ndef C(**kw):\n    return kw\n\nS = \"Method S (opening comment)\"\nclaims = [\nC(id=\"unit-counts\",\n  statement=\"The analyses of PRF at constant 200 us pulse duration rest on 1,050 S1 RSUs, 247 S1 FSUs, 913 POm \"\n  \"RSUs and 106 POm FSUs, and the 3000 Hz and 30 Hz sessions of Figure 4 on 312 and 148 S1 RSUs, 54 and 61 S1 \"\n  \"FSUs, 233 and 189 POm RSUs, and 17 and 43 POm FSUs.\",\n  source=\"Figure 4 legend; Figure 6 legend\",\n  quote=\"There are 312 RSUs and 54 FSUs recorded from S1, 233 RSUs and 17 FSUs recorded from POm for PRF 3,000 Hz. \"\n  \"There are 148 RSUs and 61 FSUs recorded from S1 and189 RSUs and 43 FSUs recorded from POm for PRF 30 Hz\",\n  expected=[\n    dict(quantity=\"S1 RSUs, PRF series at 200 us pulse duration, all PRFs\", value=1050, tolerance=105, unit=\"units\"),\n    dict(quantity=\"S1 FSUs, PRF series, all PRFs\", value=247, tolerance=24.7, unit=\"units\"),\n    dict(quantity=\"POm RSUs, PRF series, all PRFs\", value=913, tolerance=91.3, unit=\"units\"),\n    dict(quantity=\"POm FSUs, PRF series, all PRFs\", value=106, tolerance=10.6, unit=\"units\"),\n    dict(quantity=\"S1 RSUs, 3000 Hz 60% DC\", value=312, tolerance=31.2, unit=\"units\"),\n    dict(quantity=\"S1 FSUs, 3000 Hz 60% DC\", value=54, tolerance=5.4, unit=\"units\"),\n    dict(quantity=\"POm RSUs, 3000 Hz 60% DC\", value=233, tolerance=23.3, unit=\"units\"),\n    dict(quantity=\"POm FSUs, 3000 Hz 60% DC\", value=17, tolerance=1.7, unit=\"units\"),\n    dict(quantity=\"S1 RSUs, 30 Hz 0.6% DC\", value=148, tolerance=14.8, unit=\"units\"),\n    dict(quantity=\"S1 FSUs, 30 Hz 0.6% DC\", value=61, tolerance=6.1, unit=\"units\"),\n    dict(quantity=\"POm RSUs, 30 Hz 0.6% DC\", value=189, tolerance=18.9, unit=\"units\"),\n    dict(quantity=\"POm FSUs, 30 Hz 0.6% DC\", value=43, tolerance=4.3, unit=\"units\"),\n  ],\n  criterion=\"Units and cell types by \" + S + \", readings K1 and K2, counted per session and condition. Each count \"\n  \"is matched when it is within tolerance under one reading. Reproduced when at least 10 of the 12 counts match, \"\n  \"partially reproduced for 6 to 9, not reproduced below 6. The per-condition counts the Results give for \"\n  \"Figures 6 to 9 are reported alongside. This claim checks the selection that the other claims use.\"),\n\nC(id=\"fig4-s1-rsu-timelocked-3000\",\n  statement=\"With tFUS at 3000 Hz PRF and 60% DC targeting S1, S1 RSUs increase their firing during sonication.\",\n  source=\"Results, Synchronizing neuronal responses to tFUS in CTC pathway, paragraph 1; Figure 4A\",\n  quote=\"RSUs from S1 (n = 312, p = 3.13 × 10−7) and POm (n = 233, p = 0.0003) were both activated during 3,000 Hz PRF sonication\",\n  statistics=[dict(test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon test against baseline\", p=3.13e-7,\n                   corrected=\"Bonferroni\", n=\"312 S1 RSUs\")],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", S1 RSUs of the 3000 Hz 60% DC sessions. Kruskal-Wallis across the pre-stimulus and the \"\n  \"post-onset 67 ms windows to 268 ms, then the 0 to 67 ms window against baseline, one-tailed for an increase. \"\n  \"Reproduced when the post hoc test gives corrected p < 0.01 under every reading.\"),\n\nC(id=\"fig4-pom-rsu-timelocked-3000\",\n  statement=\"With 3000 Hz PRF tFUS on S1, POm RSUs are activated during sonication, synchronized with S1 RSUs.\",\n  source=\"Results, Synchronizing neuronal responses to tFUS in CTC pathway, paragraph 1; Figure 4B\",\n  quote=\"RSUs from S1 (n = 312, p = 3.13 × 10−7) and POm (n = 233, p = 0.0003) were both activated during 3,000 Hz PRF sonication\",\n  statistics=[dict(test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon test against baseline\", p=0.0003,\n                   corrected=\"Bonferroni\", n=\"233 POm RSUs\")],\n  depends_on=[\"unit-counts\"],\n  criterion=\"As fig4-s1-rsu-timelocked-3000, for POm RSUs of the same sessions. Reproduced when the 0 to 67 ms \"\n  \"window is significantly above baseline (corrected p < 0.01) under every reading.\"),\n\nC(id=\"fig4-post-3000\",\n  statement=\"After 3000 Hz PRF sonication, S1 RSUs, POm RSUs and S1 FSUs show delayed activation from about 134 ms.\",\n  source=\"Results, Synchronizing neuronal responses to tFUS in CTC pathway, paragraph 1; Figure 4A and 4B\",\n  quote=\"Postsonication activations were presented for S1 RSUs (p = 5 × 10−18), POm RSUs (p = 0.0007), and S1 FSUs (n = 54, p = 4.03 × 10−8) from 134 ms\",\n  statistics=[\n    dict(about=\"S1 RSUs, postsonication against baseline\", test=\"post hoc one-tail two-sample Wilcoxon\", p=5e-18, corrected=\"Bonferroni\", n=\"312 S1 RSUs\"),\n    dict(about=\"POm RSUs, postsonication against baseline\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.0007, corrected=\"Bonferroni\", n=\"233 POm RSUs\"),\n    dict(about=\"S1 FSUs, postsonication against baseline\", test=\"post hoc one-tail two-sample Wilcoxon\", p=4.03e-8, corrected=\"Bonferroni\", n=\"54 S1 FSUs\"),\n  ],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", 3000 Hz 60% DC sessions. The paper says the activations start from 134 ms but not which window \"\n  \"its p-values come from; the readings are the 134 to 201 ms window and the 201 to 268 ms window. Reproduced \"\n  \"when, under one of these windows and every reading of Method S, each of the three groups is significantly \"\n  \"above baseline (one-tailed, corrected p < 0.01); partially reproduced when two of the three are.\"),\n\nC(id=\"fig4-30hz-s1-rsu-inhibition\",\n  statement=\"With 30 Hz PRF and 0.6% DC, S1 RSUs show an inhibitory response just after sonication (67 to 134 ms).\",\n  source=\"Results, Synchronizing neuronal responses to tFUS in CTC pathway, paragraph 1; Figure 4A, right\",\n  quote=\"At 30 Hz PRF, the S1 RSUs showed an inhibitory response after sonication (67–134 ms, n = 148, p = 0.0029)\",\n  statistics=[dict(test=\"post hoc one-tail two-sample Wilcoxon test against baseline\", p=0.0029, corrected=\"Bonferroni\", n=\"148 S1 RSUs\")],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", S1 RSUs of the 30 Hz 0.6% DC sessions, window 67 to 134 ms against baseline, one-tailed for a \"\n  \"decrease. Reproduced when corrected p < 0.01 under every reading.\"),\n\nC(id=\"fig4-30hz-pom-rsu-delayed\",\n  statement=\"With 30 Hz PRF, POm RSUs show delayed excitatory activity at 134 to 268 ms.\",\n  source=\"Results, Synchronizing neuronal responses to tFUS in CTC pathway, paragraph 1; Figure 4B legend\",\n  quote=\"POm RSUs expressed delayed excitatory activities (n = 189, p = 2 × 10−9)\",\n  statistics=[dict(test=\"post hoc one-tail two-sample Wilcoxon test against baseline\", p=2e-9, corrected=\"Bonferroni\", n=\"189 POm RSUs\")],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", POm RSUs of the 30 Hz 0.6% DC sessions. The legend places the activity at 134 to 268 ms; the \"\n  \"readings are the 134 to 201 ms window, the 201 to 268 ms window, and one 134 ms window from 134 to 268 ms. \"\n  \"Reproduced when, under one window and every reading of Method S, the increase over baseline has corrected \"\n  \"p < 0.01.\"),\n\nC(id=\"fig4-fsu-no-change\",\n  statement=\"S1 FSUs show no time-locked response to 3000 Hz PRF, and S1 FSUs at 30 Hz and POm FSUs at both PRFs \"\n  \"show no activity change.\",\n  source=\"Results, Synchronizing neuronal responses to tFUS in CTC pathway, paragraph 1; Figure 4\",\n  quote=\"There was no activity change among S1 FSUs (n = 61) to 30 Hz PRF and POm FSUs to both PRFs (3,000 Hz, n = 17; 30 Hz, n = 43)\",\n  depends_on=[\"unit-counts\"],\n  criterion=\"A claim of absence, judged on the paper's test, \" + S + \": the post hoc one-tailed Wilcoxon test against \"\n  \"baseline at corrected p < 0.01 in each 67 ms window from 0 to 268 ms (for S1 FSUs at 3000 Hz, the 0 to 67 ms \"\n  \"window only, as the Results limit it to time-locked responses), testing both an increase and a decrease. \"\n  \"Reproduced when no window is significant for S1 FSUs at 30 Hz, POm FSUs at 3000 Hz, POm FSUs at 30 Hz, and S1 \"\n  \"FSUs at 3000 Hz during sonication; not reproduced when any is. The mean normalized rates are reported either way. \"\n  \"The readings of Method S apply as in the other claims.\"),\n\nC(id=\"fig5-sham-no-response\",\n  statement=\"In sham sessions without tFUS, S1 and POm RSUs and FSUs show no time-locked and no delayed (201 to 268 ms) change.\",\n  source=\"Results, Synchronizing neuronal responses to tFUS in CTC pathway, paragraph 2; Figure 5A\",\n  quote=\"In sham condition (no tFUS), S1 neurons and POm neurons showed no time-locked (S1 RSUs: n = 31, p = 1.0; S1 FSUs: n = 53, p = 0.55; POm RSUs: n = 67, p = 1.0; POm FSUs: n = 67, p = 1.0) and delayed\",\n  statistics=[\n    dict(about=\"S1 RSUs, time-locked\", test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon\", p=1.0, corrected=\"Bonferroni\", n=\"31 S1 RSUs\"),\n    dict(about=\"S1 FSUs, time-locked\", test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon\", p=0.55, corrected=\"Bonferroni\", n=\"53 S1 FSUs\"),\n    dict(about=\"POm RSUs, time-locked\", test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon\", p=1.0, corrected=\"Bonferroni\", n=\"67 POm RSUs\"),\n    dict(about=\"POm FSUs, time-locked\", test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon\", p=1.0, corrected=\"Bonferroni\", n=\"67 POm FSUs\"),\n  ],\n  expected=[\n    dict(quantity=\"S1 RSUs, sham\", value=31, tolerance=3.1, unit=\"units\"),\n    dict(quantity=\"S1 FSUs, sham\", value=53, tolerance=5.3, unit=\"units\"),\n    dict(quantity=\"POm RSUs, sham\", value=67, tolerance=6.7, unit=\"units\"),\n    dict(quantity=\"POm FSUs, sham\", value=67, tolerance=6.7, unit=\"units\"),\n  ],\n  criterion=\"A claim of absence, judged on the paper's test, \" + S + \", sham sessions aligned on their trial event \"\n  \"times: one-tailed post hoc Wilcoxon test for an increase against baseline at corrected p < 0.01 in the 0 to 67 ms \"\n  \"and 201 to 268 ms windows, for the four groups. Reproduced when none of the eight tests is significant; not \"\n  \"reproduced when any is. The unit counts are reported against the expected values; they do not decide the claim.\"),\n\nC(id=\"fig5-cg1-control-no-response\",\n  statement=\"With tFUS steered to the cingulate cortex (CG1) at 3000 Hz PRF, S1 and POm RSUs and FSUs show no \"\n  \"time-locked and no delayed (201 to 268 ms) change.\",\n  source=\"Results, Synchronizing neuronal responses to tFUS in CTC pathway, paragraph 2; Figure 5B\",\n  quote=\"In control condition (tFUS targeted at CG1), S1 neurons and POm neurons showed no time-locked (S1 RSUs: n = 12, p = 1.0; S1 FSUs: n = 34, p = 1.0; POm RSUs: n = 55, p = 1.0; POm FSUs: n = 42, p = 0.33) and delayed responses\",\n  statistics=[\n    dict(about=\"POm FSUs, time-locked\", test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon\", p=0.33, corrected=\"Bonferroni\", n=\"42 POm FSUs\"),\n    dict(about=\"S1 FSUs, delayed 201 to 268 ms\", test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon\", p=0.1, corrected=\"Bonferroni\", n=\"34 S1 FSUs\"),\n    dict(about=\"POm RSUs, delayed 201 to 268 ms\", test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon\", p=0.32, corrected=\"Bonferroni\", n=\"55 POm RSUs\"),\n  ],\n  expected=[\n    dict(quantity=\"S1 RSUs, CG1 control\", value=12, tolerance=1.2, unit=\"units\"),\n    dict(quantity=\"S1 FSUs, CG1 control\", value=34, tolerance=3.4, unit=\"units\"),\n    dict(quantity=\"POm RSUs, CG1 control\", value=55, tolerance=5.5, unit=\"units\"),\n    dict(quantity=\"POm FSUs, CG1 control\", value=42, tolerance=4.2, unit=\"units\"),\n  ],\n  criterion=\"A claim of absence, judged as fig5-sham-no-response on the CG1 control sessions. Reproduced when none \"\n  \"of the eight tests is significant at corrected p < 0.01; not reproduced when any is.\"),\n\nC(id=\"fig6a-s1-rsu-timelocked-high-prf\",\n  statement=\"At constant 200 us pulse duration, time-locked responses of S1 RSUs are elicited only by the high PRFs \"\n  \"(1500, 3000 and 4500 Hz), with the highest level at 1500 Hz (123.34 +/- 4.3%), and S1 RSU responses during \"\n  \"sonication differ across PRFs.\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 1; Figure 6A\",\n  quote=\"time-locked S1 RSUs’ responses could only be elicited from high PRFs: 1,500 Hz (n = 284, p = 2.74 × 10−6 compared with baseline), 3,000 Hz (n = 312, p = 3.13 × 10−7), and 4,500 Hz (n = 152, p = 0.0028), among which 1,500 Hz evoked highest response level of 123.34 ± 4.3%\",\n  statistics=[\n    dict(about=\"across PRFs, 0 to 67 ms\", test=\"Kruskal-Wallis\", p=1.49e-15, n=\"1,050 S1 RSUs\"),\n    dict(about=\"1500 Hz against baseline\", test=\"post hoc one-tail two-sample Wilcoxon\", p=2.74e-6, corrected=\"Bonferroni\", n=\"284 S1 RSUs\"),\n    dict(about=\"3000 Hz against baseline\", test=\"post hoc one-tail two-sample Wilcoxon\", p=3.13e-7, corrected=\"Bonferroni\", n=\"312 S1 RSUs\"),\n    dict(about=\"4500 Hz against baseline\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.0028, corrected=\"Bonferroni\", n=\"152 S1 RSUs\"),\n  ],\n  expected=[dict(quantity=\"mean normalized rate of S1 RSUs at 1500 Hz, 0 to 67 ms\", value=123.34, tolerance=4.3, unit=\"%\")],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", S1 RSUs of the five PRF sessions at 200 us pulse duration, window 0 to 67 ms. Kruskal-Wallis \"\n  \"across the five PRFs at p < 0.01; one-tailed post hoc tests against baseline for an increase at corrected \"\n  \"p < 0.01. Tolerance on the mean is the paper's stated SEM. Reproduced when, under every reading, the \"\n  \"Kruskal-Wallis test is significant, 1500, 3000 and 4500 Hz are significant and 30 and 300 Hz are not, and the \"\n  \"highest mean is at 1500 Hz; partially reproduced when the significance pattern holds but the highest mean is \"\n  \"elsewhere or out of tolerance.\"),\n\nC(id=\"fig6a-s1-rsu-delayed\",\n  statement=\"Delayed responses (201 to 268 ms) of S1 RSUs appear at PRFs above 30 Hz and are highest at 4500 Hz \"\n  \"(148.39 +/- 5.41%), and differ across PRFs.\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 1; Figure 6A legend\",\n  quote=\"The delayed responses (201–268 ms) of RSUs could be observed at PRFs higher than 30 Hz and the highest response occurred at 4,500 Hz (148.39 ± 5.41%)\",\n  statistics=[dict(about=\"across PRFs, postsonication\", test=\"Kruskal-Wallis\", p=5.14e-13, n=\"1,050 S1 RSUs\")],\n  expected=[dict(quantity=\"mean normalized rate of S1 RSUs at 4500 Hz, 201 to 268 ms\", value=148.39, tolerance=5.41, unit=\"%\")],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", as fig6a-s1-rsu-timelocked-high-prf, window 201 to 268 ms. Reproduced when, under every \"\n  \"reading, the Kruskal-Wallis test across PRFs has p < 0.01, 300, 1500, 3000 and 4500 Hz are significantly above \"\n  \"baseline and 30 Hz is not, and the highest mean, at 4500 Hz, is within tolerance; partially reproduced when \"\n  \"the significance pattern holds and the mean does not.\"),\n\nC(id=\"fig6b-s1-fsu\",\n  statement=\"S1 FSUs show no time-locked response to any PRF, and delayed responses only at PRFs higher than \"\n  \"1500 Hz, highest at 4500 Hz (158.75 +/- 10.75%).\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 1; Figure 6B\",\n  quote=\"FSUs did not show time-locked responses to any PRFs and only presented delayed responses at PRFs higher than 1,500 Hz, with the highest response level at 4,500 Hz (158.75 ± 10.75%)\",\n  statistics=[dict(about=\"across PRFs, postsonication\", test=\"Kruskal-Wallis\", p=5.19e-13, n=\"247 S1 FSUs\")],\n  expected=[dict(quantity=\"mean normalized rate of S1 FSUs at 4500 Hz, 201 to 268 ms\", value=158.75, tolerance=10.75, unit=\"%\")],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", S1 FSUs of the PRF sessions at 200 us pulse duration. \\\"Higher than 1,500 Hz\\\" can be read as \"\n  \"(a) 3000 and 4500 Hz or (b) 1500 Hz and above. Reproduced when, under every reading of Method S, no PRF is \"\n  \"significantly above baseline at 0 to 67 ms, the delayed responses at 201 to 268 ms are significant for exactly \"\n  \"the PRFs of (a) or of (b), the Kruskal-Wallis across PRFs at 201 to 268 ms has p < 0.01, and the 4500 Hz mean \"\n  \"is the highest and within tolerance; partially reproduced when all but the mean hold.\"),\n\nC(id=\"fig6c-pom-rsu-timelocked\",\n  statement=\"Time-locked responses of POm RSUs are elicited by 1500 and 3000 Hz PRFs, and POm RSU responses during \"\n  \"sonication differ across PRFs.\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 1; Figure 6C\",\n  quote=\"time-locked responses (Fig. 6B) from POm RSUs could be elicited by 1,500 Hz (n = 153, p = 0.003) and 3,000 Hz PRFs (n = 233, p = 0.0003)\",\n  statistics=[\n    dict(about=\"across PRFs, 0 to 67 ms\", test=\"Kruskal-Wallis\", p=2.09e-21, n=\"913 POm RSUs\"),\n    dict(about=\"1500 Hz against baseline\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.003, corrected=\"Bonferroni\", n=\"153 POm RSUs\"),\n    dict(about=\"3000 Hz against baseline\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.0003, corrected=\"Bonferroni\", n=\"233 POm RSUs\"),\n  ],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", POm RSUs of the PRF sessions at 200 us pulse duration, window 0 to 67 ms. Reproduced when, under \"\n  \"every reading, the Kruskal-Wallis across PRFs has p < 0.01 and 1500 and 3000 Hz are significantly above \"\n  \"baseline while 30, 300 and 4500 Hz are not; partially reproduced when 1500 and 3000 Hz are significant and \"\n  \"another PRF is too.\"),\n\nC(id=\"fig6c-pom-rsu-delayed\",\n  statement=\"Delayed responses (201 to 268 ms) of POm RSUs are induced by PRFs from 1500 Hz up and are highest at \"\n  \"1500 Hz (141.68 +/- 2.38%).\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 1; Figure 6C legend\",\n  quote=\"the delayed responses (201–268 ms) of POm RSUs were induced by PRFs higher than 1,500 Hz and were highest (141.68 ± 2.38%) at 1,500 Hz\",\n  statistics=[dict(about=\"across PRFs, postsonication\", test=\"Kruskal-Wallis\", p=6.03e-17, n=\"913 POm RSUs\")],\n  expected=[dict(quantity=\"mean normalized rate of POm RSUs at 1500 Hz, 201 to 268 ms\", value=141.68, tolerance=2.38, unit=\"%\")],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", POm RSUs, window 201 to 268 ms. The sentence says \\\"higher than 1,500 Hz\\\" and that the highest \"\n  \"response is at 1500 Hz, so the reading taken is 1500 Hz and above (the paper's Discussion paragraph on parameters \"\n  \"says POm delayed activity is inclined to 1500 Hz); 3000 and 4500 Hz alone is shown as a variant. Reproduced \"\n  \"when, under every reading of Method S, the Kruskal-Wallis across PRFs has p < 0.01, 1500, 3000 and 4500 Hz \"\n  \"are significantly above baseline, and the highest mean is at 1500 Hz within tolerance; partially reproduced \"\n  \"when the significance pattern holds and the mean does not.\"),\n\nC(id=\"fig6d-pom-fsu\",\n  statement=\"POm FSUs show no time-locked response to any PRF relative to baseline, and delayed responses only to \"\n  \"4500 Hz.\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 1; Figure 6D legend\",\n  quote=\"The FSUs did not show any time-locked responses and only expressed the delayed responses to 4,500 Hz (n = 26, p = 4.2 × 10−6)\",\n  statistics=[\n    dict(about=\"4500 Hz against baseline, 201 to 268 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=4.2e-6, corrected=\"Bonferroni\", n=\"26 POm FSUs\"),\n    dict(about=\"30 against 1500 Hz, 0 to 67 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.004, corrected=\"Bonferroni\"),\n    dict(about=\"across PRFs, postsonication\", test=\"Kruskal-Wallis\", p=3.99e-4, n=\"106 POm FSUs\"),\n  ],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", POm FSUs of the PRF sessions at 200 us pulse duration. Reproduced when, under every reading, no \"\n  \"PRF is significantly above baseline at 0 to 67 ms, only 4500 Hz is significantly above baseline at 201 to 268 \"\n  \"ms, and the Kruskal-Wallis across PRFs at 201 to 268 ms has p < 0.01. The 30 against 1500 Hz comparison during \"\n  \"sonication is reported.\"),\n\nC(id=\"fig7a-s1-rsu-dc-3000\",\n  statement=\"At 3000 Hz PRF, S1 RSU time-locked responses depend on DC and are elicited at 30% and 60% DC; delayed \"\n  \"responses appear at 6, 30 and 60% DC.\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 4; Figure 7A\",\n  quote=\"with 3,000 Hz PRF, the time-locked responses of S1 RSUs were dependent on DCs which can be elicited with DC of 30% (n = 194, p = 3.38 × 10−6) and 60% (n = 312, p = 5.96 × 10−6). Delayed activities of RSUs were found at 6% (n = 56, p = 0.001), 30% (n = 194, p = 9.64 × 10−32), and 60% (n = 312, p = 1.38 × 10−15)\",\n  statistics=[\n    dict(about=\"across DCs, 0 to 67 ms\", test=\"Kruskal-Wallis\", p=1.34e-11, n=\"645 S1 RSUs\"),\n    dict(about=\"across DCs, 201 to 268 ms\", test=\"Kruskal-Wallis\", p=2.52e-29, n=\"645 S1 RSUs\"),\n    dict(about=\"30% DC against baseline, 0 to 67 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=3.38e-6, corrected=\"Bonferroni\", n=\"194 S1 RSUs\"),\n    dict(about=\"60% DC against baseline, 0 to 67 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=5.96e-6, corrected=\"Bonferroni\", n=\"312 S1 RSUs\"),\n    dict(about=\"6% DC against baseline, 201 to 268 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.001, corrected=\"Bonferroni\", n=\"56 S1 RSUs\"),\n    dict(about=\"30% DC against baseline, 201 to 268 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=9.64e-32, corrected=\"Bonferroni\", n=\"194 S1 RSUs\"),\n    dict(about=\"60% DC against baseline, 201 to 268 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=1.38e-15, corrected=\"Bonferroni\", n=\"312 S1 RSUs\"),\n  ],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", S1 RSUs of the 3000 Hz sessions at DC 0.6, 6, 30, 60 and 90% (pulse durations 2, 20, 100, 200 \"\n  \"and 300 us). Reproduced when, under every reading, both Kruskal-Wallis tests have p < 0.01, exactly 30 and 60% \"\n  \"are significantly above baseline at 0 to 67 ms, and exactly 6, 30 and 60% at 201 to 268 ms; partially \"\n  \"reproduced when the Kruskal-Wallis tests hold and the significant DCs include those named with at most one other.\"),\n\nC(id=\"fig7b-s1-fsu-dc-3000\",\n  statement=\"At 3000 Hz PRF, delayed responses of S1 FSUs are elicited by 6, 30 and 60% DC, the same range as S1 RSUs.\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 4; Figure 7B\",\n  quote=\"Delayed responses of FSUs could be elicited by 6% (n = 22, p = 1.29 × 10−8), 30% (n = 49, p = 2.32 × 10−11), and 60% (n = 54, p = 2.38 × 10−8) DCs (Fig. 7B), which were the same range of S1 RSUs\",\n  statistics=[\n    dict(about=\"6% DC against baseline\", test=\"post hoc one-tail two-sample Wilcoxon\", p=1.29e-8, corrected=\"Bonferroni\", n=\"22 S1 FSUs\"),\n    dict(about=\"30% DC against baseline\", test=\"post hoc one-tail two-sample Wilcoxon\", p=2.32e-11, corrected=\"Bonferroni\", n=\"49 S1 FSUs\"),\n    dict(about=\"60% DC against baseline\", test=\"post hoc one-tail two-sample Wilcoxon\", p=2.38e-8, corrected=\"Bonferroni\", n=\"54 S1 FSUs\"),\n    dict(about=\"0.6% against 30% DC, postsonication\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.002, corrected=\"Bonferroni\", n=\"171 S1 FSUs\"),\n  ],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", S1 FSUs of the 3000 Hz DC sessions, window 201 to 268 ms. Reproduced when, under every reading, \"\n  \"exactly 6, 30 and 60% DC are significantly above baseline; partially reproduced when these three are and one \"\n  \"other DC is too. The 0.6 against 30% comparison is reported.\"),\n\nC(id=\"fig7c-pom-rsu-dc-3000\",\n  statement=\"At 3000 Hz PRF, POm RSU time-locked responses do not depend on DC and are highest at 60% (106 +/- \"\n  \"0.77%); their delayed responses depend on DC and are activated at DCs of 6% and above.\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 4; Figure 7C legend\",\n  quote=\"The POm RSUs’ time-locked responses did not show DC dependence and were highest at 60% (106 ± 0.77%; Fig. 7C). Delayed responses could be activated by DC higher than 6% (6%, n = 22, p = 1.55 × 10−6; n = 7, p = 0.001; 60%, n = 233, p = 1.28 × 10−6; 90%, n = 18, p = 0.006)\",\n  statistics=[\n    dict(about=\"across DCs, 201 to 268 ms\", test=\"Kruskal-Wallis\", p=3.61e-4, n=\"286 POm RSUs\"),\n    dict(about=\"6% DC against baseline, delayed\", test=\"post hoc one-tail two-sample Wilcoxon\", p=1.55e-6, corrected=\"Bonferroni\", n=\"22 POm RSUs\"),\n    dict(about=\"unlabelled DC (30% by position) against baseline, delayed\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.001, corrected=\"Bonferroni\", n=\"7 POm RSUs\"),\n    dict(about=\"60% DC against baseline, delayed\", test=\"post hoc one-tail two-sample Wilcoxon\", p=1.28e-6, corrected=\"Bonferroni\", n=\"233 POm RSUs\"),\n    dict(about=\"90% DC against baseline, delayed\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.006, corrected=\"Bonferroni\", n=\"18 POm RSUs\"),\n  ],\n  expected=[dict(quantity=\"mean normalized rate of POm RSUs at 60% DC, 0 to 67 ms\", value=106, tolerance=0.77, unit=\"%\")],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", POm RSUs of the 3000 Hz DC sessions. The sentence lists 6% under \\\"higher than 6%\\\" and gives one \"\n  \"entry without its DC (n = 7), which by its place is read as 30%; the reading taken is 6, 30, 60 and 90% \"\n  \"significant. Reproduced when, under every reading of Method S, the Kruskal-Wallis across DCs at 0 to 67 ms has \"\n  \"p >= 0.01 and at 201 to 268 ms p < 0.01, the 60% mean at 0 to 67 ms is the highest and within tolerance, and \"\n  \"6, 30, 60 and 90% are significantly above baseline at 201 to 268 ms; partially reproduced when the two \"\n  \"Kruskal-Wallis results hold and the rest does not in full.\"),\n\nC(id=\"fig7d-pom-fsu-dc-3000\",\n  statement=\"At 3000 Hz PRF, POm FSUs show no time-locked response against baseline but higher activity at 30% DC \"\n  \"than at 0.6% and 6% during sonication, and delayed responses at 30, 60 and 90% DC.\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 4; Figure 7D\",\n  quote=\"There was no time-locked responses of POm FSUs compared with baseline while 30% DC showed higher activities compared with 0.6% (p = 0.0001) and 6% DC (p = 0.0003). The delayed activities of POm FSUs occurred at 30% (n = 18, p = 0.003), 60% (n = 17, p = 0.005), and 90% (n = 52, p = 6.8 × 10−5) DCs\",\n  statistics=[\n    dict(about=\"across DCs, 0 to 67 ms\", test=\"Kruskal-Wallis\", p=3.32e-4, n=\"129 POm FSUs\"),\n    dict(about=\"30% against 0.6% DC, 0 to 67 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.0001, corrected=\"Bonferroni\"),\n    dict(about=\"30% against 6% DC, 0 to 67 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.0003, corrected=\"Bonferroni\"),\n    dict(about=\"30% DC against baseline, delayed\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.003, corrected=\"Bonferroni\", n=\"18 POm FSUs\"),\n    dict(about=\"60% DC against baseline, delayed\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.005, corrected=\"Bonferroni\", n=\"17 POm FSUs\"),\n    dict(about=\"90% DC against baseline, delayed\", test=\"post hoc one-tail two-sample Wilcoxon\", p=6.8e-5, corrected=\"Bonferroni\", n=\"52 POm FSUs\"),\n  ],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", POm FSUs of the 3000 Hz DC sessions; between-DC post hoc tests are one-tailed two-sample Wilcoxon \"\n  \"tests on units' normalized rates (W1 only, as units differ between sessions). Reproduced when, under every \"\n  \"reading, no DC is significantly above baseline at 0 to 67 ms, 30% exceeds 0.6% and 6% there, and 30, 60 and \"\n  \"90% are significantly above baseline at 201 to 268 ms; partially reproduced when two of these three parts hold.\"),\n\nC(id=\"fig8a-s1-rsu-dc-30\",\n  statement=\"At 30 Hz PRF, S1 RSUs show time-locked responses to 6, 30 and 90% DC and delayed responses to 90% DC, \"\n  \"with DC-dependent activity during and after sonication.\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 4; Figure 8A\",\n  quote=\"With 30 Hz PRF stimulation (Fig. 8A), the S1 RSUs showed time-locked responses to DC of 6% (n = 81, p = 1.19 × 10−8), 30% (n = 61, p = 0.001), and 90% (n = 66, p = 2.17 × 10−6) and delayed responses to 90% DC (n = 66, p = 1.5 × 10−24)\",\n  statistics=[\n    dict(about=\"across DCs, during\", test=\"Kruskal-Wallis\", p=6.98e-12, n=\"442 S1 RSUs\"),\n    dict(about=\"across DCs, postsonication\", test=\"Kruskal-Wallis\", p=1.02e-27, n=\"442 S1 RSUs\"),\n    dict(about=\"6% DC against baseline, 0 to 67 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=1.19e-8, corrected=\"Bonferroni\", n=\"81 S1 RSUs\"),\n    dict(about=\"30% DC against baseline, 0 to 67 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.001, corrected=\"Bonferroni\", n=\"61 S1 RSUs\"),\n    dict(about=\"90% DC against baseline, 0 to 67 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=2.17e-6, corrected=\"Bonferroni\", n=\"66 S1 RSUs\"),\n    dict(about=\"90% DC against baseline, 201 to 268 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=1.5e-24, corrected=\"Bonferroni\", n=\"66 S1 RSUs\"),\n  ],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", S1 RSUs of the 30 Hz sessions at DC 0.6, 6, 30, 60 and 90% (pulse durations 0.2, 2, 10, 20 and \"\n  \"30 ms). Reproduced when, under every reading, both Kruskal-Wallis tests have p < 0.01, exactly 6, 30 and 90% \"\n  \"are significantly above baseline at 0 to 67 ms and exactly 90% at 201 to 268 ms; partially reproduced when the \"\n  \"Kruskal-Wallis tests hold and the significant DCs include those named with at most one other.\"),\n\nC(id=\"fig8b-s1-fsu-dc-30\",\n  statement=\"At 30 Hz PRF, 90% DC induces a time-locked increase in S1 FSUs, and S1 FSUs show delayed responses only \"\n  \"to 90% DC; their responses depend on DC during sonication but not after.\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 4; Figure 8B legend\",\n  quote=\"90% DC with 30 Hz PRF induced positive time-locked response in S1 FSUs (Fig. 8B; n = 28, p = 4.57 × 10−11). Like S1 RSUs, S1 FSUs only showed delayed responses to 90% DC (n = 28, p = 0.007) with 30 Hz PRF\",\n  statistics=[\n    dict(about=\"90% DC against baseline, 0 to 67 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=4.57e-11, corrected=\"Bonferroni\", n=\"28 S1 FSUs\"),\n    dict(about=\"90% DC against baseline, 201 to 268 ms\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.007, corrected=\"Bonferroni\", n=\"28 S1 FSUs\"),\n    dict(about=\"across DCs, during\", test=\"Kruskal-Wallis\", p=1.89e-8, n=\"147 S1 FSUs\"),\n  ],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", S1 FSUs of the 30 Hz DC sessions. Reproduced when, under every reading, 90% DC is significantly \"\n  \"above baseline at 0 to 67 ms and is the only DC significantly above baseline at 201 to 268 ms, and the \"\n  \"Kruskal-Wallis across DCs has p < 0.01 at 0 to 67 ms and p >= 0.01 at 201 to 268 ms (the legend's \\\"no \"\n  \"difference\\\", judged on the paper's test); partially reproduced when the two 90% results hold and a \"\n  \"Kruskal-Wallis result does not.\"),\n\nC(id=\"fig9a-s1-rsu-60dc\",\n  statement=\"At constant 60% DC, only 30 Hz PRF differs from the other PRFs in its effect on S1 RSUs during \"\n  \"sonication, while postsonication activity is highest at 4500 Hz.\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 4; Figure 9A\",\n  quote=\"only 30 Hz PRF showed different effects to other PRFs (300 Hz, p = 0.008; 1,500 Hz, p = 0.006; 3,000 Hz, p = 0.007; 4,500 Hz, p = 0.0003) on S1 RSUs during sonication, while postsonication activities preferred 4,500 Hz\",\n  statistics=[\n    dict(about=\"across PRFs, during\", test=\"Kruskal-Wallis\", p=2.47e-4, n=\"759 S1 RSUs\"),\n    dict(about=\"across PRFs, postsonication\", test=\"Kruskal-Wallis\", p=1.65e-25, n=\"759 S1 RSUs\"),\n    dict(about=\"30 against 300 Hz, during\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.008, corrected=\"Bonferroni\"),\n    dict(about=\"30 against 1500 Hz, during\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.006, corrected=\"Bonferroni\"),\n    dict(about=\"30 against 3000 Hz, during\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.007, corrected=\"Bonferroni\"),\n    dict(about=\"30 against 4500 Hz, during\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.0003, corrected=\"Bonferroni\"),\n  ],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", S1 RSUs of the 60% DC sessions at the five PRFs (pulse durations 20 ms, 2 ms, 400, 200 and 133 us). \"\n  \"Between-PRF post hoc tests are one-tailed two-sample Wilcoxon tests on units' normalized rates, Bonferroni over \"\n  \"the 10 pairs. The direction of the 30 Hz difference is not stated; both tails are reported and the one the \"\n  \"data show is used. Reproduced when, under every reading of N1, N2 and K1, K2, both Kruskal-Wallis tests have \"\n  \"p < 0.01, 30 Hz differs from each other PRF at corrected p < 0.01 at 0 to 67 ms while no pair of the other four \"\n  \"does, and the 4500 Hz mean at 201 to 268 ms is the highest; partially reproduced when 30 Hz differs from at \"\n  \"least three of the four.\"),\n\nC(id=\"fig9b-s1-fsu-60dc\",\n  statement=\"At constant 60% DC, S1 FSUs respond to 1500 Hz PRF during sonication and prefer 4500 Hz postsonication.\",\n  source=\"Results, tFUS parameters on affecting neuronal activities of CTC pathway, paragraph 4; Figure 9B\",\n  quote=\"S1 FSUs responded to 1,500 Hz PRF (n = 48, p = 3.35 ×10−6) during sonication and preferred 4,500 Hz post sonication (n = 18, p = 5.84 × 10−10; Fig. 9B)\",\n  statistics=[\n    dict(about=\"1500 Hz against baseline, during\", test=\"post hoc one-tail two-sample Wilcoxon\", p=3.35e-6, corrected=\"Bonferroni\", n=\"48 S1 FSUs\"),\n    dict(about=\"4500 Hz against baseline, postsonication\", test=\"post hoc one-tail two-sample Wilcoxon\", p=5.84e-10, corrected=\"Bonferroni\", n=\"18 S1 FSUs\"),\n    dict(about=\"across PRFs, during\", test=\"Kruskal-Wallis\", p=0.0079, n=\"151 S1 FSUs\"),\n    dict(about=\"across PRFs, postsonication\", test=\"Kruskal-Wallis\", p=4.996e-5, n=\"151 S1 FSUs\"),\n  ],\n  depends_on=[\"unit-counts\"],\n  criterion=S + \", S1 FSUs of the 60% DC sessions. Reproduced when, under every reading, 1500 Hz is significantly \"\n  \"above baseline at 0 to 67 ms, 4500 Hz is significantly above baseline at 201 to 268 ms with the highest mean \"\n  \"there, and both Kruskal-Wallis tests have p < 0.01; partially reproduced when the two significant responses hold \"\n  \"and the rest does not.\"),\n\nC(id=\"fig10a-dsttc-3000\",\n  statement=\"With 3000 Hz PRF and 60% DC, the directional correlation from S1 RSUs to POm RSUs and from POm RSUs to \"\n  \"S1 FSUs increases during sonication; postsonication, the correlation from S1 RSUs to POm FSUs and from POm RSUs \"\n  \"to S1 RSUs decreases.\",\n  source=\"Results, tFUS elicited correlation change in CTC pathway, paragraph 1; Figure 10A\",\n  quote=\"When 3,000 Hz PRF was applied, S1 RSUs showed an increased correlation to POm RSUs during sonication (p = 0.01). At the same period, POm RSUs showed enhanced correlation to S1 FSUs (p = 0.02)\",\n  statistics=[\n    dict(about=\"S1 RSU to POm RSU, during against prestimulation\", test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon\", p=0.01),\n    dict(about=\"POm RSU to S1 FSU, during against prestimulation\", test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon\", p=0.02),\n  ],\n  depends_on=[\"unit-counts\"],\n  criterion=\"Method D (opening comment), pairs within the 3000 Hz 60% DC sessions, four directions (S1 RSU to POm \"\n  \"RSU, S1 RSU to POm FSU, POm RSU to S1 RSU, POm RSU to S1 FSU). The postsonication window is not given; the \"\n  \"readings are each 67 ms window from 67 to 268 ms. Reproduced when, under every reading of Method D and of the \"\n  \"cell types, S1 RSU to POm RSU and POm RSU to S1 FSU are significantly above prestimulation at 0 to 67 ms \"\n  \"(one-tailed, p < 0.05) and the other two directions are not, and, in one postsonication window, S1 RSU to POm \"\n  \"FSU and POm RSU to S1 RSU are significantly below prestimulation; partially reproduced when the during-sonication \"\n  \"part holds alone. The numbers of pairs are reported.\"),\n\nC(id=\"fig10b-dsttc-30\",\n  statement=\"With 30 Hz PRF, the directional correlation from S1 RSUs to POm FSUs increases and that from POm RSUs to \"\n  \"S1 FSUs decreases during sonication.\",\n  source=\"Results, tFUS elicited correlation change in CTC pathway, paragraph 1; Figure 10B legend\",\n  quote=\"When delivering 30 Hz ultrasound, S1 RSUs to POm FSUs higher correlated (p = 0.0058), while POm RSUs showed decreased correlation to S1 FSUs during sonication (p = 0.0058)\",\n  statistics=[\n    dict(about=\"S1 RSU to POm FSU, increase\", test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon\", p=0.0058),\n    dict(about=\"POm RSU to S1 FSU, decrease\", test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon\", p=0.0058),\n  ],\n  depends_on=[\"unit-counts\"],\n  criterion=\"Method D, pairs within the 30 Hz 0.6% DC sessions, window 0 to 67 ms against prestimulation. Reproduced \"\n  \"when, under every reading, S1 RSU to POm FSU is significantly higher and POm RSU to S1 FSU significantly lower \"\n  \"(one-tailed, p < 0.05); partially reproduced when one of the two holds.\"),\n\nC(id=\"fig10c-sttc-constant-pd\",\n  statement=\"At constant 200 us pulse duration, the S1 RSU to POm RSU correlation change during sonication does not \"\n  \"depend on PRF, though 1500 Hz gives a higher change than 30 Hz.\",\n  source=\"Results, tFUS elicited correlation change in CTC pathway, paragraph 2; Figure 10C\",\n  quote=\"When applying tFUS with constant 200 μs PD, varying the DC and PRF, the correlation did not show PRF-dependent change. A total of 1,500 Hz PRF did show a higher correlation change compared with 30 Hz PRF (Fig. 10C; p = 0.02)\",\n  statistics=[dict(about=\"1500 against 30 Hz\", test=\"post hoc one-tail two-sample Wilcoxon\", p=0.02)],\n  depends_on=[\"unit-counts\"],\n  criterion=\"Method T (opening comment), S1 RSU and POm RSU pairs of the five PRF sessions at 200 us pulse duration. \"\n  \"The absence of PRF dependence is judged on the paper's test: reproduced in that part when the Kruskal-Wallis \"\n  \"across PRFs has p >= 0.05. The 1500 against 30 Hz part holds when the one-tailed Wilcoxon test (W1, as pairs \"\n  \"differ between sessions) gives p < 0.05 with 1500 Hz higher. Reproduced when both parts hold under D1 and D2 \"\n  \"and K1 and K2; partially reproduced when one does.\"),\n\nC(id=\"fig10d-sttc-60dc\",\n  statement=\"At constant 60% DC, the S1 RSU to POm RSU correlation change during sonication depends on PRF, with a \"\n  \"preference for 1500 and 3000 Hz.\",\n  source=\"Results, tFUS elicited correlation change in CTC pathway, paragraph 2; Figure 10D\",\n  quote=\"Then we fixed the DC to 60% and varied PRF. Unlike the neuronal responses (Fig. 9), the correlation showed the preference to 1,500 and 3,000 Hz\",\n  statistics=[dict(test=\"Kruskal-Wallis\", p=0.0012)],\n  depends_on=[\"unit-counts\"],\n  criterion=\"Method T, S1 RSU and POm RSU pairs of the 60% DC sessions at the five PRFs. Reproduced when, under D1 \"\n  \"and D2 and K1 and K2, the Kruskal-Wallis across PRFs has p < 0.05 and the two largest median changes are at \"\n  \"1500 and 3000 Hz; partially reproduced when the test holds and only one of the two is among the two largest.\"),\n\nC(id=\"fig10ef-sttc-dc\",\n  statement=\"The S1 RSU to POm RSU correlation change depends on DC at 30 Hz PRF, changing most at middle DCs (6, 30, \"\n  \"60%), and does not depend on DC at 3000 Hz PRF.\",\n  source=\"Results, tFUS elicited correlation change in CTC pathway, paragraph 2; Figure 10E and 10F\",\n  quote=\"For 30 Hz PRF (Fig. 10E), the correlation tended to change most at a middle range (6, 30, 60%) and respond less to lower (e.g., 0.6%) and higher DC (e.g., 90%). For 3,000 Hz PRF, the pathway correlation showed DC independence (Fig. 10F)\",\n  statistics=[dict(about=\"across DCs at 30 Hz PRF\", test=\"Kruskal-Wallis\", p=0.0054)],\n  depends_on=[\"unit-counts\"],\n  criterion=\"Method T, S1 RSU and POm RSU pairs of the 30 Hz and of the 3000 Hz DC sessions. Reproduced when, under \"\n  \"D1 and D2 and K1 and K2, the Kruskal-Wallis across DCs at 30 Hz has p < 0.05 with the median changes at 6, 30 \"\n  \"and 60% each above those at 0.6 and 90%, and the Kruskal-Wallis across DCs at 3000 Hz has p >= 0.05 (the \"\n  \"absence judged on the paper's test); partially reproduced when one PRF's result holds.\"),\n\nC(id=\"fig11b-ac-responses\",\n  statement=\"Auditory cortex neurons respond to tFUS on S1 in a PRF-dependent way, time-locked to 1500 and 3000 Hz \"\n  \"and postsonication to 30, 1500, 3000 and 4500 Hz, with the least response to 300 Hz.\",\n  source=\"Results, Auditory confound on CTC pathway modulation using tFUS, paragraph 1; Figure 11B (legend labels it C)\",\n  quote=\"During sonication, the AC neurons showed time-locked responses to 1,500 Hz (n = 107, p = 9.9 × 10−5) and 3,000 Hz PRF (n = 104, p = 1.98 × 10−7). Postsonication, neuronal responses were activated by 30 Hz (n = 83, p = 1.77 × 10−20), 1,500 Hz, (n = 107, p = 1.36 × 10−5), 3,000 Hz (n = 104, p = 4.47 × 10−13), and 4,500 Hz (n = 100, p = 1.66 × 10−40)\",\n  statistics=[\n    dict(about=\"across PRFs, during\", test=\"Kruskal-Wallis\", p=3.18e-4, n=\"453 AC neurons\"),\n    dict(about=\"across PRFs, postsonication\", test=\"Kruskal-Wallis\", p=2.67e-43, n=\"453 AC neurons\"),\n    dict(about=\"1500 Hz, during\", test=\"post hoc one-tail two-sample Wilcoxon\", p=9.9e-5, corrected=\"Bonferroni\", n=\"107 AC neurons\"),\n    dict(about=\"3000 Hz, during\", test=\"post hoc one-tail two-sample Wilcoxon\", p=1.98e-7, corrected=\"Bonferroni\", n=\"104 AC neurons\"),\n    dict(about=\"30 Hz, postsonication\", test=\"post hoc one-tail two-sample Wilcoxon\", p=1.77e-20, corrected=\"Bonferroni\", n=\"83 AC neurons\"),\n    dict(about=\"1500 Hz, postsonication\", test=\"post hoc one-tail two-sample Wilcoxon\", p=1.36e-5, corrected=\"Bonferroni\", n=\"107 AC neurons\"),\n    dict(about=\"3000 Hz, postsonication\", test=\"post hoc one-tail two-sample Wilcoxon\", p=4.47e-13, corrected=\"Bonferroni\", n=\"104 AC neurons\"),\n    dict(about=\"4500 Hz, postsonication\", test=\"post hoc one-tail two-sample Wilcoxon\", p=1.66e-40, corrected=\"Bonferroni\", n=\"100 AC neurons\"),\n  ],\n  criterion=S + \", AC units of the auditory-confound group (S1 and AC probes), all cell types together as the paper \"\n  \"reports AC neurons without a split. The paper does not say which DC goes with each PRF here (\\\"varying \"\n  \"combination of PRFs and DCs\\\"); the readings are the 200 us pulse duration series and the 60% DC series. \"\n  \"Reproduced when, under one series and every reading of Method S, both Kruskal-Wallis tests have p < 0.01, \"\n  \"exactly 1500 and 3000 Hz are significantly above baseline at 0 to 67 ms, and exactly 30, 1500, 3000 and 4500 Hz \"\n  \"at 201 to 268 ms; partially reproduced when the Kruskal-Wallis tests hold and at least four of the six named \"\n  \"responses are significant. The PRF with the lowest mean postsonication response is reported (the legend names \"\n  \"300 Hz).\"),\n\nC(id=\"fig11c-ac-s1-dsttc-30\",\n  statement=\"With 30 Hz PRF on S1, the directional correlation from AC neurons to S1 RSUs increases during \"\n  \"sonication and lasts about 150 to 200 ms, and the correlation from AC neurons to S1 FSUs changes too.\",\n  source=\"Results, Auditory confound on CTC pathway modulation using tFUS, paragraph 2; Figure 11C legend\",\n  quote=\"During tFUS sonication with 30 Hz PRF, the correlation from 878 paired AC neurons to S1 RSUs significantly increased (p = 0.0014) which lasting for ∼150 ms (left)\",\n  statistics=[dict(about=\"AC to S1 RSU, during against prestimulation\", test=\"Kruskal-Wallis, post hoc one-tail two-sample Wilcoxon\", p=0.0014, n=\"878 pairs\")],\n  expected=[dict(quantity=\"AC neuron and S1 RSU pairs, 30 Hz sessions\", value=878, tolerance=87.8, unit=\"pairs\")],\n  criterion=\"Method D, AC units to S1 RSUs and to S1 FSUs of the 30 Hz sessions of the auditory-confound group. The \"\n  \"legend says the increase lasts about 150 ms and the Results about 200 ms; it holds when the windows from 0 ms up \"\n  \"to 134 ms or up to 201 ms are each above prestimulation. The paper is self-contradictory on AC to S1 FSUs (the \"\n  \"legend says it decreased during and right after sonication, the Results that the same synchronization is found), \"\n  \"so that part is reported and does not decide. Reproduced when, under every reading of Method D, AC to S1 RSU is \"\n  \"significantly above prestimulation (one-tailed, p < 0.05) at 0 to 67 ms and in the next window; partially \"\n  \"reproduced when only the 0 to 67 ms window is. The legend's 1,421 pairs (all sessions) and 878 pairs are reported.\"),\n\nC(id=\"fig11d-ac-s1-dsttc-3000\",\n  statement=\"With 3000 Hz PRF on S1, the directional correlation between AC neurons and S1 RSUs does not change, and \"\n  \"AC neurons and S1 FSUs show only a postsonication change at about 200 to 300 ms.\",\n  source=\"Results, Auditory confound on CTC pathway modulation using tFUS, paragraph 2; Figure 11D legend\",\n  quote=\"However, when delivering 3,000 Hz PRF ultrasound energy to S1, auditory neurons did not show directional correlation change with S1 RSUs. The correlation change of AC neurons with S1 FSUs only occurred ∼200–300 ms\",\n  criterion=\"Method D, AC units and S1 RSUs and FSUs of the 3000 Hz sessions of the auditory-confound group. The \"\n  \"absence for S1 RSUs is judged on the paper's test: no 67 ms window from 0 to 268 ms differs from \"\n  \"prestimulation at one-tailed p < 0.05 in either direction, for AC to S1 RSU. The S1 FSU part holds when AC to \"\n  \"S1 FSU (or S1 FSU to AC, as the legend calls the change bidirectional) differs from prestimulation in the 201 \"\n  \"to 268 ms window or the 268 to 335 ms window and in no window before 201 ms. Reproduced when both parts hold \"\n  \"under every reading; partially reproduced when the S1 RSU part holds alone. The legend's 1,714 and 1,016 pairs \"\n  \"are reported.\"),\n]\n\nout = HEADER + yaml.safe_dump(dict(schema_version=2, dataset=dict(archive=\"dandi\", id=\"000637\"),\n                                   paper=\"doi:10.1523/jneurosci.2218-24.2025\", claims=claims),\n                              sort_keys=False, allow_unicode=True, width=110)\nopen(\"claims/000637/10.1523-jneurosci.2218-24.2025.yaml\", \"w\").write(out)\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i "s/The legend's 1,421 pairs (all sessions) and 878 pairs are reported./The legend's 1,421 AC and S1 RSU pairs, and the 878 pairs, are reported against the counts found./" $TMPDIR/gen.py && python $TMPDIR/gen.py && python tools/claims_check.py claims/000637/10.1523-jneurosci.2218-24.2025.yaml paper/10.1523-jneurosci.2218-24.2025.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Next I'll check the style rules (no em dashes, no "rather", no colon-space in plain scalars).

**Agent calls Bash**

```bash
cd  f=claims/000637/10.1523-jneurosci.2218-24.2025.yaml; grep -c "—" $f; grep -ci "rather" $f; python - <<'E'
import yaml
f='claims/000637/10.1523-jneurosci.2218-24.2025.yaml'
# find plain scalars with ': '
for ev in yaml.parse(open(f)):
    if isinstance(ev, yaml.ScalarEvent) and ev.style is None and ': ' in ev.value:
        print('PLAIN', ev.value[:80])
d=yaml.safe_load(open(f))
print(sum('criterion' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('expected' in c for c in d['claims']))
E
```

```
0
0
31 28 9
```

**Agent calls Bash**

```bash
cd  sed -n 95,130p claims/000637/*.yaml; git status --short
```

```
value: 1050
    tolerance: 105
    unit: units
  - quantity: S1 FSUs, PRF series, all PRFs
    value: 247
    tolerance: 24.7
    unit: units
  - quantity: POm RSUs, PRF series, all PRFs
    value: 913
    tolerance: 91.3
    unit: units
  - quantity: POm FSUs, PRF series, all PRFs
    value: 106
    tolerance: 10.6
    unit: units
  - quantity: S1 RSUs, 3000 Hz 60% DC
    value: 312
    tolerance: 31.2
    unit: units
  - quantity: S1 FSUs, 3000 Hz 60% DC
[... 28 more lines not kept]
```

**Agent**

I wrote `claims/000637/10.1523-jneurosci.2218-24.2025.yaml`. The quote checker passes: 31 claims, 31 quotes, 84 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record from PubMed Central (PMC12139594), with Methods, Results, figure legends and Discussion. The paper has no supplement and no PDF was supplied. It links no code, so no code was read.

**Counts:**
- **Quotes:** all 31 claims have one, so none needed an `inferred` note.
- **Statistics:** 28 claims carry them.
- **Criteria:** all 31 have one.
- **Expected values:** 9 claims have them. These are unit counts with a 10% tolerance, and mean normalized rates with the paper's stated SEM as the tolerance.
- **Scope:** the claims cover Figures 4 to 11: spiking responses in S1, POm and auditory cortex across PRF and duty-cycle series, sham and CG1 control (absence claims judged on the paper's test), and the correlation analyses (dSTTC and STTC).

**Shared methods:** the opening comment defines three shared methods, which the criteria refer to by name. Method S covers spiking, Method D directional correlation (dSTTC) and Method T plain correlation (STTC). Each part is cited to the Methods, Results or legends.

**Details the paper leaves open, and the readings named:**
- **Cell-type clustering:** k-means over the units of one area pooled across sessions (K1), or over all areas pooled (K2).
- **Normalized rate:** the ratio of summed counts in the window to summed counts before stimulation (N1), or the mean of per-trial ratios (N2).
- **The "two-sample Wilcoxon" test against baseline:** rank-sum (W1) or paired signed-rank (W2).
- **Bonferroni count:** comparisons with baseline only (M1), or all pairs (M2). I took the reported p-values as already corrected, since several are printed as 1.0.
- **Windows:**
  - Fig. 4 post-sonication from 134 ms: 134–201 ms or 201–268 ms.
  - POm at 30 Hz: 134–201, 201–268, or the whole of 134–268 ms.
  - Fig. 10A post-sonication: each 67 ms window from 67 to 268 ms.
- **dSTTC formula:** the equation is lost from the text. I wrote it in the Cutts & Eglen STTC form, built from the terms the text defines.
- **Normalized dSTTC:** the difference from pre-stimulus (D1) or that difference divided by the pre-stimulus value (D2). The 67 ms windows, with time fractions taken inside the window, are also my reading.
- **Inconsistencies in the paper:**
  - "Higher than 1,500 Hz" for S1 FSUs: read as 3000 and 4500 Hz, or as 1500 Hz and above.
  - For POm RSUs the same phrase sits beside "highest at 1500 Hz": I took 1500 Hz and above, with 3000 and 4500 Hz as a variant.
  - Fig. 7C lists 6% under "higher than 6%", and one entry (n = 7) has no duty cycle; by its position I read it as 30%.
  - The Fig. 11C AC-to-S1 correlation is said to last about 150 ms (legend) and about 200 ms (Results).
  - AC-to-S1 FSU is said to decrease (legend) and to show the same synchronization (Results). This part is reported and does not decide the claim.
  - The duty cycle used with each PRF in the Fig. 11 auditory series is not given: the 200 µs pulse-duration series or the 60% duty-cycle series.
- **Fig. 9A:** the direction of the 30 Hz difference is not stated, so both tails are reported.

**Missing from the paper:**
- **dSTTC equation:** absent from the text, and there was no PDF to read it from. Supplying the PDF would settle the formula used by claims fig10a, fig10b, fig11c and fig11d.
- **Analysis code:** none is linked, so nothing in the Methods could be settled from code.
- **Data location:** the paper says all its data are in DANDI:000946, not 000637. The 000637 description lists S1 recordings only, with pulse durations of 100, 200 and 400 µs. The POm, auditory cortex, sham, CG1 and duty-cycle claims may therefore not be testable on this dandiset; finding out is the author's job, and the opening comment says so.

## End of run

18 turns, 6 minutes, result: success.
