# peyrache-2015 · claims · run 43706930662

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ tools/
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
3	Version: `pilot-15`. Record this version in the attempt's provenance.
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
cat claims/peyrache-2015.yaml; echo ----; cat claims/fouke-2025.yaml | head -150
```

```
# Claims for Peyrache, Lacroix, Petersen & Buzsaki (2015) on dandiset 000056.
# Source: the NIH author manuscript in PubMed Central (PMC4376557), full text, read from its
# Results, figure legends and Methods. The supplementary files (Supplementary Table 1 and
# Figures) could not be downloaded, as PMC served a browser check in their place.
#
# When these criteria were written, the author had seen the data check only: the file list
# and metadata of both published versions, the contents of every file (the units table holds
# spike times alone, with no electrode, shank, region or waveform), unit and spike counts per
# file, the sleep-state tables, the electrode groups, the annotation series, and the position
# traces used to find the open-field epoch. No claim's analysis had been run, and the number
# of head-direction (HD) cells had not been computed.
#
# The dandiset gives no brain region for any unit, so every claim that separates the
# antero-dorsal thalamic nucleus (ADn) from the post-subiculum (PoS) is blocked. The claims
# tested here pool the HD cells of each session, whatever their region.
#
# Method choices fixed here where the paper leaves them open (no analysis code is linked by
# the paper or the dandiset).
# - Waking is the open-field exploration. The files do not mark it (their "Awake" state also
#   covers waking in the home cage), so it is found from position as the first period of at
[... 481 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*; head -c 3000 paper/10.1038-nn.3968.txt; grep -n "supp\|Supplementary Table\|github\|code" -i paper/10.1038-nn.3968.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.3968.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-nn.3968.txt').read()
print(t[52400:75000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-nn.3968.txt').read()
print(t[75000:])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "def \|KEYS\|allowed\|fields" tools/claims_check.py | head -40; ls papers/datasets/ | grep peyr; cat papers/datasets/peyrache-2015.yaml
```

```
"""Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
(fragments split on "...", found in order) and looks for every recorded p-value and
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
"""

from __future__ import annotations

import html
import re
import sys
import unicodedata
from pathlib import Path

[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"
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
  "paper",
  "claims"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "dataset": {
   "description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
   "type": "object",
   "additionalProperties": false,
   "required": [
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)); print(list(s['properties']))"
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

**Agent**

The full text, Methods and all three supplements are present; the paper links no code (its reporting checklist says N/A). Let me check how a current-protocol claims file looks.

**Agent calls Bash**

```bash
cd claims; for f in $(ls -t *.yaml | head -40); do grep -L "^dataset:" $f; done | head;
```

```
zhong-2026.yaml
zhang-2021.yaml
zandvakili-2015.yaml
yang-2025.yaml
wright-2019.yaml
wirtshafter-2020.yaml
wirth-2017.yaml
watson-2016.yaml
wang-2014.yaml
wakhloo-2026.yaml
```

**Agent calls Bash**

```bash
head -60 claims/zandvakili-2015.yaml; grep -n "open\|readings" claims/zandvakili-2015.yaml | head
```

```
# Claims for Zandvakili & Kohn (2015), Neuron 87, 827-839, "Coordinated Neuronal Activity Enhances
# Corticocortical Communication" (doi:10.1016/j.neuron.2015.07.026), on CRCNS data set v1v2-1.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
# protocol as stated in docs/protocol.md (Reader), version pilot-14.
#
# Text read. The version of record as supplied under paper/ (PyMuPDF text of the journal PDF, with
# the Supplemental Information appended): Results, Discussion, figure legends, Experimental
# Procedures, and the supplement (Figures S1 to S6 with their texts, Supplemental Experimental
# Procedures). The PDF pages could not be rendered in this run, so no figure was read from the
# image; every value below is from the text. The extracted text prints the degree sign as a
# replacement glyph and a few dashes oddly; one such case is named in figS5-middle-layer-relay.
#
# Code. The paper links no analysis code and names no repository. No code was read; every
# method below is from the Experimental Procedures, the Results, the figure legends or the
# supplement, and details none of them fixes are named as open.
#
# Data the paper used. Nine hemispheres of seven anesthetized (sufentanil), paralyzed adult male
# Macaca fascicularis. V1 recorded with a 10 x 10 Utah array (1 mm electrodes, 400 um spacing,
# layers 2/3 and 4B), RFs 2 to 4 deg from the fovea; 10 array implants, V1 populations of 61 to 160
# units (average 98). V2 recorded with seven moveable electrodes and tetrodes (300 um spacing) in
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
t=open('paper/10.1038-nn.3968.txt').read()
for k in ['Pearson’s test, n = 907','5 hours','p < 10 –10 , Mann','10 –9','10 –5 ,','p < 10 –6 for all','3×10 −6','Wilcoxon’s signed rank test, n = 86','(p < 10–7)','p < 10–10, Mann','p < 10 –5 )']:
    i=t.find(k); print(repr(t[i-80:i+60]) if i>=0 else 'MISSING '+k)
EOF
```

Result: not kept, because it reads the paper's text.

**Agent**

Now writing the claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/peyrache-2015.yaml",
 "content": "# Claims for Peyrache, Lacroix, Petersen & Buzsaki (2015), Nature Neuroscience 18, 569-575,\n# \"Internally organized mechanisms of the head direction sense\" (doi:10.1038/nn.3968), on dandiset\n# 000056.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-15,\n# protocol as stated in docs/protocol.md (Reader), version pilot-15.\n#\n# Text read. The NIH author manuscript (PMC4376557) as served by Europe PMC, under paper/: Results,\n# Discussion, Methods and figure legends, with its three supplements from the PMC Open Access\n# files: Supplementary Figures 1 to 8 (legends), Supplementary Table 1 (recordings by animal), and\n# the Nature Neuroscience reporting checklist, which gives exact p-values and sample sizes per\n# test. The checklist numbers figures as in an earlier draft (its \"1e\", \"1f\" are Supplementary\n# Fig. 2b,c, its \"4b\" is Fig. 5b, its \"4f\" is Fig. 5d,e); the Methods also cite Fig. 4f,g and\n# \"readout windows in Fig. 4\" for what the published legends show in Fig. 5d,e. The main figures\n# themselves are not under paper/ (no PDF of the article), so values printed only inside figures\n# (the r values of the Fig. 2a,b insets, the Fig. 4d errors) could not be read.\n#\n# Code. The paper links no analysis code, and its checklist answers N/A for custom software. No\n# code was read. Every method below is from the Methods, the Results, the figure legends or the\n# supplement, and details none of them fixes are named as open.\n#\n# This file replaces one written after its author had seen the dataset's data check, whose\n# methods (finding the open field from the position traces, pooling the two regions, handling of\n# missing LED frames) came from the data. It was rewritten from the paper alone. Ids are kept\n# where the finding is the same. fig5e-adn-predicts-pos now holds the asymmetry alone; the readout\n# windows, the reliability of the ADn to PoS prediction, and twelve findings without a claim before\n# (recording-sample, supptable1-per-animal, hd-fraction-hd-shanks, supfig2a-unimodality,\n# supfig5-rate-independent, fig4d-ole-near-bayesian, fig5b-sleep-tuning-similar,\n# fig5d-adn-predicts-pos-reliably, fig5e-readout-windows, fig6a-fast-oscillation,\n# fig7e-interneurons-no-difference, fig2e-decoded-speed) are new claims.\n#\n# Data the paper used. Seven adult mice (five male, two female, 27 to 50 g; aged 3 to 12 months,\n# reporting checklist), animals m12, m17, m20, m24, m25, m28 and m32 (Supplementary Table 1).\n# Silicon probes (4, 6 or 8 shanks, 200 um apart, 8 or 10 sites per shank) in the left anterior\n# thalamus of all seven, aimed at the antero-dorsal nucleus (ADn), and in the post-subiculum (PoS)\n# of three (m24, m25, m28); CA1 wires for sleep scoring in the four thalamus-only mice (m12, m17,\n# m20, m32). Signals at 20 kHz, LFP downsampled to 1.25 kHz; spike sorting with KlustaKwik and\n# Klusters. Two LEDs (5 cm apart, blue and red) on the headstage, filmed at 30 frames/s and\n# resampled at 39 Hz (the first frame misaligned by 0 to 60 ms). Each session is an open-field\n# exploration (\"wake\", foraging for food for 30 to 45 min in a 53 x 46 cm arena with two visual\n# cues), in 41 of 42 sessions preceded and followed by about 2 h of sleep in the home cage; in one\n# session a radial maze after the second sleep counts as wake and no sleep followed. 42 sessions,\n# 21 of them with ADn and PoS recorded together in 3 mice. Sleep is scored as SWS or REM from CA1 or\n# PoS LFP spectrograms and movement, by an automatic Bayesian clustering checked by hand. Sessions\n# separated by less than three days without moving the thalamic probe were discarded. Three mice\n# expressed channelrhodopsin, which is not part of the study. Measured variables are spike times\n# and waveforms of sorted units with their probe (ADn or PoS) and shank, LFP, LED positions, and\n# sleep states. Supplementary Table 1 lists sessions as 5, 9, 5, (2, 4), (3, 10), (3, 7) and 2 per\n# animal, which sum to 50, not 42; the table is read as given and the difference is named in\n# recording-sample. The dandiset, by its title and description, holds recordings of the ADn and\n# PoS of mice across wake and sleep from this lab, the data of this paper.\n#\n# Shared methods, from the Methods (\"Head direction cells\", \"Bayesian reconstruction\", \"Information\n# measures\", \"Classification of PoS neurons\") unless said otherwise.\n# - Waking is the open-field (\"wake\") phase of each session; SWS and REM are the scored sleep\n#   stages. Head direction is the orientation of the blue and red LEDs; times when either LED is\n#   not detected are excluded.\n# - Tuning curve (HD field) in 1 degree bins, spike counts over time spent, smoothed with a 6\n#   degree s.d. Gaussian, in waking. Preferred direction is the circular mean of the von Mises fit.\n#   HD cell when the von Mises concentration exceeds 1, the peak rate exceeds 1 Hz and the Rayleigh\n#   test of uniformity has p < 0.001. Open (hd), how the fit is made, which the Methods give only as\n#   fitting \"the distributions of angular values making the HD fields\"; readings (hd-a) the maximum\n#   likelihood von Mises fit to the tuning curve taken as a distribution of angles, with the\n#   Rayleigh test on the same distribution weighted by spike count, or (hd-b) a least-squares fit\n#   of a von Mises function (with peak rate as amplitude) to the tuning curve, with the Rayleigh\n#   test on the head directions at spike times. Whether the peak rate is the fitted amplitude or the\n#   tuning curve maximum goes with the reading.\n# - Rate threshold (Methods, Head direction cells, paragraph 2). \"In all cross-correlation\n#   analyses, only cells firing at least at 0.5 Hz in any of the three brain states were included.\"\n#   Open (rate), readings (rate-a) at least 0.5 Hz in each of waking, SWS and REM, or (rate-b) in\n#   at least one of them.\n# - Pair correlations (Figure 3a legend) are Pearson correlations of binned spike counts, 300 ms\n#   bins in waking and REM and 50 ms bins in SWS, for pairs recorded in the same session. Whether\n#   pairs on the same shank are kept is not stated for these analyses; kept here, a standard\n#   choice, with same-shank pairs left out shown as a variant.\n# - Bayesian decoding (following Zhang et al. 1998, ref 56). 10 ms bins, counts smoothed with a\n#   Gaussian of 300 ms s.d. in waking and REM and 50 ms in SWS, Poisson likelihood from waking\n#   tuning curves, decoded HD as the maximum of the posterior; used only when at least 6 HD cells\n#   are recorded in the structure. The prior is not given; a flat prior is used, the standard\n#   choice of ref 56's basic method.\n# - Information (bits per spike). Cross-validated log-likelihood ratio of the spike train under\n#   an intensity function against a homogeneous rate at the training mean, normalised by the\n#   firing rate; 10 segments, each tested against the 9 others. HD information uses the training\n#   tuning curve read at the test head direction.\n# - PoS cell types from the waveform (Supplementary Fig. 6). Putative interneuron for duration\n#   below 0.9 ms and trough-to-peak below 0.42 ms; putative pyramidal for duration above 0.95 ms\n#   and trough-to-peak above 0.42 ms; duration is the inverse of the frequency of maximum power of\n#   the waveform's wavelet spectrum. Other cells are undetermined.\n# - Statistics. All tests two-tailed, non-parametric (Mann-Whitney U, Wilcoxon signed-rank,\n#   Kruskal-Wallis), correlations by Pearson's coefficient, no correction for multiple\n#   comparisons (Methods, Statistical Analysis; reporting checklist).\nschema_version: 2\npaper: doi:10.1038/nn.3968\nclaims:\n- id: recording-sample\n  statement: HD cell ensembles were recorded in 7 mice over 42 open-field sessions with home-cage\n    sleep, with ADn and PoS recorded simultaneously in 3 mice over 21 sessions.\n  source: Results, paragraph 1; Methods, Recording sessions and behavioral paradigm\n  quote: in 7 mice foraging for food in an open environment (42 sessions) and in their home cages\n    during sleep ... In 3 mice (21 sessions) ADn and PoS recordings were performed simultaneously.\n  expected:\n  - quantity: mice\n    value: 7\n    tolerance: 0\n    unit: mice\n  - quantity: sessions\n    value: 42\n    tolerance: 4.2\n    unit: sessions\n  - quantity: sessions with ADn and PoS recorded together\n    value: 21\n    tolerance: 2.1\n    unit: sessions\n  - quantity: mice with ADn and PoS recorded together\n    value: 3\n    tolerance: 0\n    unit: mice\n  criterion: Counts of mice and sessions with an open-field epoch and spikes. Mice are counted\n    exactly (zero tolerance, as they are whole animals named in Supplementary Table 1). Supplementary\n    Table 1 lists 50 sessions in all (29 ADn only, 21 with both), against 42 in the text, and the\n    paper does not say which sessions the 42 are; readings (a) all sessions, (b) sessions with\n    sleep before and after the open field (41 of 42 in the text). Reproduced when all four values\n    are within tolerance under one reading, or the total matches the table's 50; the difference\n    from 42 is reported.\n- id: supptable1-per-animal\n  statement: Per animal, the ADn HD cells (of recorded cells) are 63 (217) in m12, 52 (245) in m17,\n    15 (49) in m20, 17 (22) in m24, 23 (27) in m25, 37 (55) in m28 and 35 (105) in m32, and the PoS\n    HD cells are 9 (48) in m24, 53 (135) in m25 and 49 (174) in m28.\n  source: Supplementary Table 1\n  inferred: Numbers from Supplementary Table 1; no sentence states them.\n  depends_on:\n  - hd-cell-fraction\n  expected:\n  - quantity: ADn HD cells, m12\n    value: 63\n    tolerance: 6.3\n  - quantity: ADn HD cells, m17\n    value: 52\n    tolerance: 5.2\n  - quantity: ADn HD cells, m20\n    value: 15\n    tolerance: 1.5\n  - quantity: ADn HD cells, m24\n    value: 17\n    tolerance: 1.7\n  - quantity: ADn HD cells, m25\n    value: 23\n    tolerance: 2.3\n  - quantity: ADn HD cells, m28\n    value: 37\n    tolerance: 3.7\n  - quantity: ADn HD cells, m32\n    value: 35\n    tolerance: 3.5\n  - quantity: PoS HD cells, m24\n    value: 9\n    tolerance: 0.9\n  - quantity: PoS HD cells, m25\n    value: 53\n    tolerance: 5.3\n  - quantity: PoS HD cells, m28\n    value: 49\n    tolerance: 4.9\n  criterion: HD cells classified as in the opening comment, under readings (hd-a) and (hd-b),\n    counted per animal and structure; recorded cells per animal are reported beside them.\n    Reproduced when at least 8 of the 10 HD counts are within tolerance under one reading;\n    partially reproduced for 5 to 7. The threshold of 8 of 10 is fixed here, as the paper states no\n    rule for a table.\n- id: hd-cell-fraction\n  statement: Of the recorded cells, 242 of 720 in the anterior thalamus (41% on average) and 111 of\n    357 in the PoS (31%) were classified as HD cells.\n  source: Methods, Head direction cells, paragraph 2\n  quote: 242 out of 720 recorded cells (41% on average) in the anterior thalamus, and 111 out of 357\n    (31%) cells in the PoS were classified as HD cells.\n  expected:\n  - quantity: thalamic HD cells\n    value: 242\n    tolerance: 24.2\n    unit: cells\n  - quantity: thalamic recorded cells\n    value: 720\n    tolerance: 72\n    unit: cells\n  - quantity: average fraction of thalamic cells classified as HD cells\n    value: 0.41\n    tolerance: 0.041\n  - quantity: PoS HD cells\n    value: 111\n    tolerance: 11.1\n    unit: cells\n  - quantity: PoS recorded cells\n    value: 357\n    tolerance: 35.7\n    unit: cells\n  - quantity: fraction of PoS cells classified as HD cells\n    value: 0.31\n    tolerance: 0.031\n  criterion: HD cells by the rule of the opening comment, readings (hd-a) and (hd-b), in the\n    waking epoch of each session kept by the Methods. The pooled thalamic fraction is 242/720 =\n    34%, so \"41% on average\" is an average over units of the sample; readings (a) the mean over\n    sessions, (b) the mean over animals of the per-animal fractions. Reproduced when the four counts\n    and both fractions are within tolerance under one combination of readings; partially\n    reproduced when the counts are and a fraction is not.\n- id: hd-fraction-hd-shanks\n  statement: In the thalamus, on shanks where at least one HD cell was detected, 71% of the cells\n    were HD cells on average.\n  source: Methods, Head direction cells, paragraph 2\n  quote: In the thalamus, when considering only cell ensembles recorded on silicon probe shanks\n    where at least one HD cell was detected, the average proportion of HD cells was 71%\n  depends_on:\n  - hd-cell-fraction\n  expected:\n    quantity: average fraction of HD cells on thalamic shanks with at least one HD cell\n    value: 0.71\n    tolerance: 0.071\n  criterion: For each session and thalamic shank with at least one HD cell, the fraction of its\n    cells that are HD cells. The average is open; readings (a) the mean over shank-sessions, (b)\n    the pooled fraction over those shanks. Reproduced when the value is within tolerance under one\n    reading and HD reading.\n- id: ensemble-sizes\n  statement: Ensembles of 8.4 plus or minus 5.1 (s.d.) units per session were recorded in the ADn\n    and 5 plus or minus 2.8 in the PoS.\n  source: Results, paragraph 1\n  quote: Ensembles of HD neurons from ADn (8.4 ± 5.1 s.d. units per session) and PoS (5 ± 2.8 s.d.)\n    were recorded by multi-site silicon probes\n  depends_on:\n  - hd-cell-fraction\n  expected:\n  - quantity: ADn units per session, mean\n    value: 8.4\n    tolerance: 0.84\n  - quantity: ADn units per session, s.d.\n    value: 5.1\n    tolerance: 0.51\n  - quantity: PoS units per session, mean\n    value: 5\n    tolerance: 0.5\n  - quantity: PoS units per session, s.d.\n    value: 2.8\n    tolerance: 0.28\n  criterion: The tolerance is 10% of each mean and s.d., not the s.d. itself, because the s.d. is\n    the spread across sessions and not an uncertainty of the mean. The unit counted is open;\n    readings (a) HD cells per session among sessions with that structure recorded, (b) HD cells per\n    session among sessions with at least one HD cell in it, (c) HD cells per session among sessions\n    kept for Bayesian decoding. 242 HD cells over the 50 sessions of Supplementary Table 1 average\n    4.8, so the sessions meant are a subset. Reproduced when both means and both s.d. are within\n    tolerance under one reading; partially reproduced when both means are.\n- id: adn-pos-peak-rate\n  statement: ADn HD cells have peak rates almost three times those of PoS HD cells.\n  source: Results, paragraph 1; Supplementary Figure 2b\n  quote: ADn neurons exhibited peak rates almost three times higher than PoS cells ( Supplementary\n    Fig. 2b ; p < 10 –10 , Mann-Whitney U-test, n = 242 ADn and n = 111 PoS HD cells)\n  statistics:\n  - test: Mann-Whitney U-test\n    p: 1.0e-10\n    p_relation: \"<\"\n    n: 242 ADn and 111 PoS HD cells\n  depends_on:\n  - hd-cell-fraction\n  expected:\n    quantity: ratio of ADn to PoS peak rate\n    value: 3\n    tolerance: 0.3\n  criterion: Peak rate of each HD cell per reading (hd-a) or (hd-b). \"Almost three times\" is\n    compared as a ratio of the two medians or of the two means (the paper does not say which; the\n    Mann-Whitney test compares distributions), so readings (a) medians, (b) means. Reproduced when\n    a two-sided Mann-Whitney U-test gives ADn higher with p < 1e-10 and the ratio is within\n    tolerance under one reading, or between 2.5 and 3 (as \"almost\" allows a value below 3);\n    partially reproduced when the test holds and the ratio is outside.\n- id: adn-pos-hd-information\n  statement: ADn HD cells convey 30% more head-direction information than PoS HD cells, 1.44\n    against 1.11 bits per spike.\n  source: Results, paragraph 1; Supplementary Figure 2c\n  quote: conveyed 30% more head-direction information than PoS cells (1.44 bit per spike vs. 1.11\n    bit per spike; see Methods ; Supplementary Fig. 2c ; p < 10 –6 , Mann-Whitney U-test)\n  statistics:\n  - about: text\n    test: Mann-Whitney U-test\n    p: 1.0e-6\n    p_relation: \"<\"\n    n: 242 ADn and 111 PoS HD cells\n  - about: exact value in the reporting checklist\n    test: Mann-Whitney U-test\n    p: 1.4e-7\n    n: 242 ADn and 111 PoS HD cells\n  depends_on:\n  - hd-cell-fraction\n  expected:\n  - quantity: ADn HD information\n    value: 1.44\n    tolerance: 0.144\n    unit: bit/spike\n  - quantity: PoS HD information\n    value: 1.11\n    tolerance: 0.111\n    unit: bit/spike\n  criterion: Cross-validated HD information of each HD cell (Methods, Information measures; 10\n    segments of the waking epoch). Whether 1.44 and 1.11 are medians or means is not stated;\n    readings (a) medians, (b) means. Reproduced when both values are within tolerance under one\n    reading and a two-sided Mann-Whitney U-test gives ADn higher with p < 1e-6; partially\n    reproduced when the test holds and a value is outside.\n- id: supfig2a-unimodality\n  statement: 12% of ADn HD cells and 32% of PoS HD cells were not unimodal, having a second tuning\n    curve peak of at least 50% of the maximal peak rate.\n  source: Supplementary Figure 2a legend\n  quote: \"12% of ADn HD cells and 32% of PoS HD cells were not unimodal: their tuning curve showed\n    at least one other peak that was 50% or more than the maximal peak firing rate.\"\n  depends_on:\n  - hd-cell-fraction\n  expected:\n  - quantity: fraction of ADn HD cells not unimodal\n    value: 0.12\n    tolerance: 0.012\n  - quantity: fraction of PoS HD cells not unimodal\n    value: 0.32\n    tolerance: 0.032\n  criterion: A peak is a local maximum of the smoothed tuning curve. What separates two peaks is\n    not given; readings (a) any other local maximum of 50% or more of the maximum, (b) such a\n    maximum separated from the main peak by a trough below 50% of the maximum. Reproduced when both\n    fractions are within tolerance under one reading; partially reproduced when one is.\n- id: fig2a-rates-preserved\n  statement: The firing rates of HD neurons are strongly correlated between waking and SWS and\n    between waking and REM sleep, in the ADn and in the PoS.\n  source: Results, paragraph 3; Figure 2a (ADn n = 215, PoS n = 62 cells)\n  quote: First, the firing rates of HD neurons remained strongly correlated across brain states (\n    Fig. 2a ).\n  depends_on:\n  - hd-cell-fraction\n  expected:\n  - quantity: ADn HD cells in the comparison\n    value: 215\n    tolerance: 21.5\n    unit: cells\n  - quantity: PoS HD cells in the comparison\n    value: 62\n    tolerance: 6.2\n    unit: cells\n  criterion: For each HD cell in a session with SWS and REM, the mean rate in waking, SWS and REM;\n    Pearson's r across cells of waking against SWS and of waking against REM, per structure. The\n    figure legend gives the r values only in insets, which could not be read (no article PDF), so\n    \"strongly\" is open; readings (a) r of at least 0.7, (b) r of at least 0.5. The cells included\n    (215 and 62 of 242 and 111) are open; readings (a) HD cells in sessions with both sleep stages,\n    (b) those passing the rate threshold under (rate-a) or (rate-b). Reproduced when all four r\n    pass under one threshold reading with Pearson p < 0.05; partially reproduced when all four are\n    positive with p < 0.05 and some fall below 0.5. Cell counts are reported against the expected\n    values and do not decide the outcome.\n- id: fig2b-pair-correlations-preserved\n  statement: The pairwise correlations between HD neuron pairs, within and across structures, are\n    similar across waking, SWS and REM.\n  source: Results, paragraph 3; Figure 2b (ADn pairs n = 970, PoS pairs n = 92)\n  quote: Second, the pairwise correlations between HD neuron pairs both within and across\n    structures were robustly similar across states ( Fig. 2b )\n  depends_on:\n  - hd-cell-fraction\n  expected:\n  - quantity: ADn HD cell pairs\n    value: 970\n    tolerance: 97\n    unit: pairs\n  - quantity: PoS HD cell pairs\n    value: 92\n    tolerance: 9.2\n    unit: pairs\n  criterion: Pair correlations as in the opening comment (Figure 3a bins), pairs of HD cells passing\n    the rate threshold under (rate-a) or (rate-b). Pearson's r across pairs of the waking\n    correlations against the SWS and against the REM correlations, for ADn-ADn, PoS-PoS and\n    ADn-PoS pairs. The legend says \"Same as a\", so r values are again only in insets; \"robustly\n    similar\" is read with the thresholds of fig2a-rates-preserved, (a) 0.7 and (b) 0.5. Fig. 2b\n    gives 970 ADn pairs and Fig. 3a 907; both are reported. Reproduced when all r pass under one\n    threshold reading with p < 0.05; partially reproduced when all are positive with p < 0.05 and\n    some fall below 0.5.\n- id: fig2f-sws-tenfold-faster\n  statement: The angular velocity of the internal HD signal, estimated from the temporal profile of\n    pairwise cross-correlograms, is about tenfold faster during SWS than during waking.\n  source: Results, paragraph 3; Figure 2e,f; Methods, Estimation of angular velocity\n  quote: The angular velocity of the internal HD signal, either estimated by a Bayesian decoder or\n    from the temporal profile of pairwise cross-correlograms ... was approximately tenfold faster\n    during SWS than during waking ( Fig. 2e,f )\n  depends_on:\n  - hd-cell-fraction\n  expected:\n    quantity: median ratio of SWS to waking angular velocity over HD cell pairs\n    value: 10\n    tolerance: 1\n  criterion: Method of the Methods (Estimation of angular velocity) and Supplementary Fig. 4. For\n    each pair, the angular correlation of the two waking tuning curves as a function of angular\n    offset, normalized so that 1 is chance (Supplementary Fig. 4 legend); the speed distribution a\n    chi-squared distribution with 3 degrees of freedom scaled to mean v; the expected\n    cross-correlogram at lag tau the mean over speeds of the angular correlation at speed times\n    tau; v found by minimizing the sum of squared differences from the observed cross-correlogram\n    (normalized with 1 as chance, Fig. 2c legend), first on a coarse grid, then by an unconstrained\n    derivative-free search (Nelder-Mead, Matlab's standard such method, the paper's software). Open,\n    and named, (v-a) the cross-correlogram bin and lag range, none given; 10 ms bins (the bin of the\n    other cross-correlation analyses) to lags of plus or minus 2 s in waking and REM and 0.5 s in\n    SWS used here, a standard choice; (v-b) whether turning in both directions enters the average\n    (readings, speeds only, so offsets at plus and minus v tau averaged, or signed, the same\n    thing for a symmetric angular correlation); (v-c) the coarse grid, a standard choice that does\n    not change the minimum. Pairs are ADn-ADn and PoS-PoS HD cell pairs (Fig. 2f), rate threshold\n    (rate-a) or (rate-b). Reproduced when the median over pairs of the SWS to waking ratio is\n    within tolerance in ADn-ADn pairs and in PoS-PoS pairs under one reading; partially reproduced\n    when it is within tolerance in one of them, or above 5 in both with SWS faster in most pairs\n    (two-sided Wilcoxon signed-rank test of the log ratio, p < 0.05).\n- id: fig2e-decoded-speed\n  statement: The angular speed of the Bayesian decoded HD signal is about tenfold faster in SWS than\n    in waking, and similar in REM and waking.\n  source: Results, paragraph 3; Figure 2e legend (top histograms)\n  quote: The angular velocity of the internal HD signal, either estimated by a Bayesian decoder or\n    from the temporal profile of pairwise cross-correlograms ... was approximately tenfold faster\n    during SWS than during waking\n  depends_on:\n  - hd-cell-fraction\n  expected:\n    quantity: ratio of median decoded angular speed, SWS to waking\n    value: 10\n    tolerance: 1\n  criterion: Bayesian decoding as in the opening comment, in each session with at least 6 HD cells\n    in a structure, per structure. Angular speed is the absolute circular difference of\n    successive decoded angles over the bin time. The step over which speed is taken is not given;\n    readings (a) successive 10 ms bins, (b) the decoded angle subsampled at the smoothing window\n    (300 ms in waking and REM, 50 ms in SWS). Reproduced when, under one reading, the SWS to waking\n    ratio of median speeds is within tolerance and the REM to waking ratio lies between 0.67 and\n    1.5 (a band fixed here, as the paper gives no number for \"similar\"); partially reproduced when\n    one of the two holds.\n- id: fig2f-rem-similar-to-wake\n  statement: The angular velocity of the internal HD signal estimated from cross-correlograms is\n    similar during REM sleep and waking.\n  source: Results, paragraph 3; Figure 2e,f\n  quote: Angular velocity of the internal HD signal was similar during waking and REM ( Fig. 2e,f ).\n  depends_on:\n  - fig2f-sws-tenfold-faster\n  criterion: With the pairs and fits of fig2f-sws-tenfold-faster. The paper names no test or band\n    for \"similar\", so the readings are (a) the median REM to waking ratio over pairs lies between\n    0.67 and 1.5, (b) a two-sided Wilcoxon signed-rank test (the Methods' paired test) of the log\n    ratio against 0 does not reach p < 0.05. Reproduced when the result holds in ADn-ADn and\n    PoS-PoS pairs under one reading; the median ratio and the test are reported either way.\n- id: fig3a-packet-60-degrees\n  statement: The zero-lag correlation between HD cell pairs falls with the offset of their\n    preferred directions, positive below 60 degrees, negative above it and near zero at about 60\n    degrees, within and across structures, in waking, REM and SWS.\n  source: Results, paragraph 4; Figure 3a\n  quote: Pairs of neurons with <60° offset showed positive correlations, pairs with >60° offset\n    showed negative correlations, and pairs with approximately 60° offset were uncorrelated ( Fig.\n    3a ). The relationship between the 0-lag correlation and the preferred angular direction was\n    preserved across brain states\n  statistics:\n  - about: text, all states and pair types\n    test: Pearson's test\n    p: 1.0e-6\n    p_relation: \"<\"\n    n: 907 ADn-ADn, 512 ADn-PoS and 92 PoS-PoS pairs\n  - about: PoS-PoS pairs, SWS (reporting checklist)\n    test: Pearson's test\n    p: 1.0e-8\n    n: 92 PoS-PoS pairs\n  - about: PoS-PoS pairs, REM (reporting checklist)\n    test: Pearson's test\n    p: 1.2e-8\n    n: 92 PoS-PoS pairs\n  depends_on:\n  - hd-cell-fraction\n  expected:\n  - quantity: offset of preferred directions at which the correlation crosses zero\n    value: 60\n    tolerance: 6\n    unit: degrees\n  - quantity: ADn-ADn pairs\n    value: 907\n    tolerance: 90.7\n    unit: pairs\n  - quantity: ADn-PoS pairs\n    value: 512\n    tolerance: 51.2\n    unit: pairs\n  - quantity: PoS-PoS pairs\n    value: 92\n    tolerance: 9.2\n    unit: pairs\n  criterion: Pair correlations as in the opening comment (300 ms bins in waking and REM, 50 ms in\n    SWS), preferred directions from waking, rate threshold (rate-a) or (rate-b). What the Pearson\n    test correlates with is not given; readings (a) the absolute offset (0 to 180 degrees), (b) the\n    cosine of the offset. The zero crossing is read from the mean correlation in bins of absolute\n    offset, by linear interpolation at the first change of sign; the bin width is open and could\n    move the crossing by a few degrees, so (c) 10 degree and (d) 20 degree bins are both run.\n    Reproduced when, in all three states and all three pair types, the Pearson test is significant\n    at p < 1e-6 in the direction of falling correlation and the crossing is within tolerance, under\n    one combination of readings; partially reproduced when the Pearson tests hold everywhere and the\n    crossing is within tolerance in some states or pair types only.\n- id: fig3a-adn-stronger-than-pos\n  statement: Pairwise correlations of HD cells closer than 60 degrees are stronger in the ADn than\n    in the PoS in every brain state, independently of firing rate differences.\n  source: Results, paragraph 4; Figure 3a; Supplementary Figure 5\n  quote: HD signal was more strongly preserved in the ADn than in the PoS as shown by the stronger\n    pairwise correlations in any brain state (p < 10 –5 , Mann-Whitney U-test for all pairs closer\n    than 60° in all brain states, n = 345 ADn-ADn pairs; n = 55 PoS-PoS pairs)\n  statistics:\n  - about: text, all states\n    test: Mann-Whitney U-test\n    p: 1.0e-5\n    p_relation: \"<\"\n    n: 345 ADn-ADn and 55 PoS-PoS pairs closer than 60 degrees\n  - about: wake (reporting checklist)\n    test: Mann-Whitney U-test\n    p: 1.9e-6\n    n: 345 ADn-ADn and 55 PoS-PoS pairs\n  - about: SWS (reporting checklist)\n    test: Mann-Whitney U-test\n    p: 3.6e-5\n    n: 345 ADn-ADn and 55 PoS-PoS pairs\n  - about: REM (reporting checklist)\n    test: Mann-Whitney U-test\n    p: 9.2e-7\n    n: 345 ADn-ADn and 55 PoS-PoS pairs\n  depends_on:\n  - fig3a-packet-60-degrees\n  expected:\n  - quantity: ADn-ADn pairs closer than 60 degrees\n    value: 345\n    tolerance: 34.5\n    unit: pairs\n  - quantity: PoS-PoS pairs closer than 60 degrees\n    value: 55\n    tolerance: 5.5\n    unit: pairs\n  criterion: Pairs of fig3a-packet-60-degrees with absolute offset below 60 degrees, per state.\n    Reproduced when a two-sided Mann-Whitney U-test gives ADn-ADn correlations higher than PoS-PoS\n    with p < 0.05 in each state; the text's bound (p < 1e-5) is reported against, and its failure\n    in a state with p < 0.05 makes the claim partially reproduced (the checklist's SWS value, 3.6e-5,\n    itself exceeds the text's bound). The firing rate independence is claim supfig5-rate-independent.\n- id: supfig5-rate-independent\n  statement: The stronger correlations in the ADn than in the PoS do not depend on firing rate; in a\n    two-way ANOVA the region effect is significant and the firing rate group effect is not.\n  source: Supplementary Figure 5 legend\n  quote: The brain areas comparison effect was significant (p < 10–7) but the firing rate group\n    effect was not (p > 0.05, two-way ANOVA).\n  statistics:\n  - about: region effect\n    test: two-way ANOVA\n    p: 1.0e-7\n    p_relation: \"<\"\n  - about: firing rate group effect\n    test: two-way ANOVA\n    p: 0.05\n    p_relation: \">\"\n  depends_on:\n  - fig3a-adn-stronger-than-pos\n  criterion: Pairs of ADn-ADn and PoS-PoS HD cells, grouped by the mean firing rate of the pair\n    below 5 Hz or between 5 and 10 Hz (Supplementary Fig. 5, right); a two-way ANOVA of pair\n    correlation on region and rate group. Not given, and named; (s-a) which pairs, all pairs or\n    those closer than 60 degrees as in the text's test (both run); (s-b) the state, each state\n    separately or the three pooled (both run); (s-c) the rate, the geometric mean of the two peak\n    rates (left panels) or the mean of the two mean rates (right panel, \"firing rate mean\"), both\n    run. The rate effect is a claim of absence judged on the paper's test, the two-way ANOVA at\n    0.05. Reproduced when the region effect has p < 1e-7 and the rate group effect has p > 0.05;\n    not reproduced when the rate effect is significant. Since several readings are run, the outcome\n    is the one they share; where they differ every result is shown.\n- id: fig3b-packet-coherence\n  statement: The activity packets in the ADn and the PoS are coherent with the packet expected from\n    the Bayesian decoded HD, in waking, REM and SWS.\n  source: Results, paragraph 4; Figure 3b; Methods, Ensemble coherence\n  quote: The actual activity packets, both in the ADn and the PoS, and across brain states, were\n    highly similar to the predictions given by the signal decoded from a Bayesian estimator ( Fig.\n    3b ) in waking, REM and SWS\n  depends_on:\n  - hd-cell-fraction\n  criterion: Method of the Methods (Ensemble coherence, after Johnson et al. 2005, ref 34). The\n    actual packet at each time is the sum of normalized tuning curves weighted by instantaneous\n    rates; the expected packet is the one at the decoded angle; for each degree, 5000 waking\n    population vectors at that angle form the reference distribution; coherence is the probability\n    that the two packets are similar, as against that distribution, significant above 0.05. Open,\n    and named; (c-a) the distance between packets, not given, readings the Euclidean distance or\n    one minus the correlation; (c-b) how the 5000 vectors at a degree are chosen (bins whose decoded\n    or actual HD is at that degree), readings both; (c-c) the smoothing windows, which Fig. 3b\n    varies without listing; 50 to 1000 ms run here. Reproduced when, in both structures and all\n    three states, the median coherence over time bins exceeds 0.05 at the decoder's own windows\n    (300 ms in waking and REM, 50 ms in SWS) under one reading; partially reproduced when it does\n    in some structures or states.\n- id: fig4b-noise-correlations\n  statement: During waking, the observed correlations of HD cell pairs exceed those expected from\n    independent rate-coded neurons for pairs with overlapping fields (0 plus or minus 15 degrees),\n    fall below them for pairs at 60 plus or minus 15 degrees, and match them only at larger\n    offsets.\n  source: Results, paragraph 5; Figure 4a,b; Methods, Cross-correlation under the hypothesis of\n    independent firing rate coding scheme\n  quote: However, correlations expected from independent rate-coded neurons could not fully account\n    for the observed pairwise correlations of HD cells ( Fig. 4a ). ... were observed for neuron\n    pairs with overlapping fields (0±15°), with a marked negative signal correlation at 60±15°\n    offset ( Fig. 4b,c ) and the expected correlations became similar to the observed ones only for\n    pairs with larger angular differences.\n  depends_on:\n  - hd-cell-fraction\n  criterion: Waking, following the Methods. For each cell the intensity function f(t) = h(theta(t)),\n    its waking tuning curve read at the head direction, in 10 ms bins; for each pair the\n    cross-correlation of the two intensity functions and of the two binned spike trains, both as\n    1/N times the sum of products at each lag; the noise correlation is their difference (spike\n    trains minus intensities). Open, and named; (n-a) the lag, the Methods average from -50 to +50\n    ms and the Fig. 4b legend says \"at 0-timelag\" (both run); (n-b) the scale, the formula as\n    written or divided by the product of the two mean rates so that 1 is chance (Supplementary Fig.\n    4 says all correlations are so normalized), both run; (n-c) whether the tuning curve is\n    cross-validated, not said, so the tuning curve from the whole waking epoch is used, as the\n    Methods describe it. The paper gives no test of the sign at 0 and 60 degrees; a two-sided\n    Wilcoxon signed-rank test against 0 (the Methods' one-sample test) at p < 0.05 is used. Pairs\n    within each structure and across, rate threshold (rate-a) or (rate-b). Reproduced when, under\n    one reading, the noise correlation is above 0 for pairs at 0 plus or minus 15 degrees and below\n    0 for pairs at 60 plus or minus 15 degrees, in ADn-ADn pairs and in pooled pairs; partially\n    reproduced when one of the two holds. The mean noise correlation beyond 90 degrees is reported.\n- id: fig4c-noise-adn-vs-pos\n  statement: The correlation excess at 0 degrees and deficit at 60 degrees are stronger for ADn\n    pairs than for PoS pairs.\n  source: Results, paragraph 5; Figure 4c\n  quote: These signal correlations were stronger for ADn than PoS neurons (p < 10 –9 , Kruskal-Wallis\n    one-way analysis of variance; ADn-ADn pairs\n  statistics:\n  - about: text\n    test: Kruskal-Wallis one-way analysis of variance\n    p: 1.0e-9\n    p_relation: \"<\"\n    n: ADn-ADn 96 and 200, ADn-PoS 77 and 157, PoS-PoS 29 and 57 pairs, at 0 and 60 degrees\n  - about: 0 plus or minus 15 degrees (reporting checklist)\n    test: Kruskal-Wallis one-way analysis of variance\n    p: 1.0e-10\n    p_relation: \"<\"\n    n: 96 ADn-ADn, 77 ADn-PoS and 29 PoS-PoS pairs\n  - about: 60 plus or minus 15 degrees (reporting checklist)\n    test: Kruskal-Wallis one-way analysis of variance\n    p: 1.9e-6\n    n: 200 ADn-ADn, 157 ADn-PoS and 57 PoS-PoS pairs\n  depends_on:\n  - fig4b-noise-correlations\n  expected:\n  - quantity: ADn-ADn pairs at 0 plus or minus 15 degrees\n    value: 96\n    tolerance: 9.6\n  - quantity: ADn-ADn pairs at 60 plus or minus 15 degrees\n    value: 200\n    tolerance: 20\n  - quantity: ADn-PoS pairs at 0 plus or minus 15 degrees\n    value: 77\n    tolerance: 7.7\n  - quantity: ADn-PoS pairs at 60 plus or minus 15 degrees\n    value: 157\n    tolerance: 15.7\n  - quantity: PoS-PoS pairs at 0 plus or minus 15 degrees\n    value: 29\n    tolerance: 2.9\n  - quantity: PoS-PoS pairs at 60 plus or minus 15 degrees\n    value: 57\n    tolerance: 5.7\n  criterion: The noise correlations of fig4b-noise-correlations, under its readings, for the three\n    pair types at 0 plus or minus 15 and at 60 plus or minus 15 degrees. A Kruskal-Wallis test\n    across the three pair types in each offset group (as the checklist reports one p per group).\n    \"Stronger\" means a larger excess at 0 and a deeper deficit at 60 degrees, so the test is run on\n    the values as signed. Reproduced when both tests give p < 0.05 with ADn-ADn pairs the most\n    extreme in each group, under one reading; partially reproduced when one does. Pair counts are\n    reported against the expected values and do not decide the outcome.\n- id: fig4d-ole-near-bayesian\n  statement: Optimal linear estimates of HD are better when based on spike train covariances than on\n    tuning curve covariances, and the covariance-based estimate almost reaches the performance of a\n    Bayesian decoder.\n  source: Results, paragraph 5; Figure 4d\n  quote: Optimal linear estimates (OLE, see Methods ) of the head-direction were enhanced when using\n    spike train covariances (i.e., including noise correlation) instead of the tuning curve\n    covariances (i.e., signal correlation only). Estimate of HD based solely on the actual\n    covariance of the spike trains almost reached the performance of a non-linear Bayesian decoder\n  depends_on:\n  - hd-cell-fraction\n  criterion: The Results refer to the Methods for the OLE, but the Methods have no OLE section, so\n    the estimator is not defined by the paper. Taken here as the standard OLE of Salinas and Abbott\n    (1994), the population vector weights D = Q^-1 L, with Q the cell by cell correlation matrix of\n    smoothed counts and L the correlation of counts with the HD basis (cos, sin), decoded HD the\n    angle of the estimate. Readings for Q, the paper's own two, (signal) from the tuning curves read\n    at the head direction and (cov) from the actual spike trains. Cross-validated waking median\n    absolute error (10 segments, as in the information measures), counts in 10 ms bins smoothed by\n    Gaussian windows from 10 to 1000 ms (the Fig. 4d axis is not readable here). Sessions with 6 or\n    more HD cells in a structure (checklist, 20 ADn and 8 PoS). Reproduced when, in each structure,\n    the minimum error over windows of the covariance OLE is below that of the signal OLE (two-sided\n    Wilcoxon signed-rank test over ensembles, p < 0.05) and within 25% of the Bayesian decoder's\n    minimum (\"almost reached\", a margin fixed here); partially reproduced when the first holds. The\n    claim rests on an estimator the paper does not define.\n- id: fig4e-ole-covariance\n  statement: In the ADn the covariance-based OLE is about 50% better than the signal-based OLE, and\n    the gain is significantly larger than in the PoS.\n  source: Results, paragraph 5; Figure 4d,e\n  quote: In the ADn, where noise correlations were highest for overlapping HD cells, the\n    covariance-based OLE was approximately 50% better than the signal-based OLE ( Fig. 4d,e ), and\n    significantly stronger than in the PoS ( Fig. 4e ; p < 0.05; Mann-Whitney’s U-test; n = 20 ADn\n    and 8 PoS cell ensembles, respectively)\n  statistics:\n  - about: text\n    test: Mann-Whitney's U-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 20 ADn and 8 PoS cell ensembles\n  - about: Figure 4e legend\n    test: Mann-Whitney's U-test\n    p: 0.009\n    n: 20 ADn and 8 PoS cell ensembles\n  - about: reporting checklist\n    test: Mann-Whitney U test\n    p: 0.0088\n    n: 20 ADn and 8 PoS sessions with 6 or more HD cells\n  depends_on:\n  - fig4d-ole-near-bayesian\n  expected:\n  - quantity: ADn ensembles\n    value: 20\n    tolerance: 2\n  - quantity: PoS ensembles\n    value: 8\n    tolerance: 0.8\n  criterion: The ratio of the minimum (over windows) median absolute error of the covariance OLE to\n    that of the signal OLE (Fig. 4e legend), per ensemble, with the OLE of fig4d-ole-near-bayesian.\n    \"50% better\" is open; readings (a) a median ratio of 0.5 (error halved), (b) a median ratio of\n    0.67 (signal error 1.5 times the covariance error), each with a tolerance of 10% of the ratio.\n    Reproduced when the ADn median ratio is within tolerance under one reading and a two-sided\n    Mann-Whitney U-test gives ADn ratios lower than PoS with p < 0.05; partially reproduced when one\n    of the two holds. The claim rests on an estimator the paper does not define.\n- id: decoding-tracks-hd\n  statement: The HD signal decoded with a Bayesian decoder from HD cells faithfully tracks the head\n    direction of the waking mouse.\n  source: Methods, Bayesian reconstruction of Head-Direction; Figure 1c\n  quote: These estimates faithfully tracked the head position in the waking mouse.\n  depends_on:\n  - hd-cell-fraction\n  criterion: Bayesian decoding as in the opening comment, per structure, in sessions with at least 6\n    HD cells in it, waking. The paper gives no number for \"faithfully\" and does not say whether the\n    tuning curves are cross-validated for this (they are for Fig. 4d, \"cross-validated median\n    absolute error\"); readings (a) tuning curves from the whole waking epoch, (b) 10-segment\n    cross-validation. A median absolute error of 30 degrees or less (a third of the 90 degrees\n    expected by chance) is the threshold, fixed here. Reproduced when the median over ensembles of\n    the median absolute error is 30 degrees or less in each structure under one reading; partially\n    reproduced when it is in one structure.\n- id: fig5b-sleep-tuning-similar\n  statement: Tuning curves of HD cells computed during sleep from the HD signal decoded from the\n    other structure are remarkably similar to their waking tuning curves.\n  source: Results, paragraph 6; Figure 5a,b\n  quote: tuning curves were remarkably similar during sleep to that of waking ( Fig. 5a,b ;\n  depends_on:\n  - hd-cell-fraction\n  criterion: In sessions with ADn and PoS recorded together and at least 6 HD cells in the decoding\n    structure, the HD decoded from one structure (opening comment) in waking, REM and SWS, and the\n    tuning curve of each HD cell of the other structure against the decoded HD (1 degree bins, 6\n    degree smoothing, as for waking tuning curves); its Pearson correlation with the cell's waking\n    tuning curve against actual head direction. The paper gives no threshold for \"remarkably\n    similar\"; fixed here as a median correlation of 0.5 or more in each state. Reproduced when that\n    holds in all three states for PoS cells decoded from ADn; partially reproduced in one or two\n    states. The decoded-HD bins used are open; readings (a) the 10 ms bins of the decoder, (b) bins\n    at the smoothing window.\n- id: fig5b-adn-decoded-tuning\n  statement: The HD signal decoded from ADn assemblies gives tuning curves of PoS HD cells more\n    similar to their waking tuning curves than the signal decoded from PoS assemblies does for ADn\n    HD cells, in all brain states.\n  source: Results, paragraph 6; Figure 5a,b\n  quote: However, the HD signal extracted from ADn assemblies resulted in tuning curves more similar\n    to actual HD fields than the HD signal decoded from PoS assemblies, in all brain states\n  statistics:\n  - about: wake\n    test: Mann-Whitney U test\n    p: 1.0e-10\n    p_relation: \"<\"\n    n: 86 PoS and 92 ADn HD cells\n  - about: SWS\n    test: Mann-Whitney U test\n    p: 0.018\n    n: 86 PoS and 92 ADn HD cells\n  - about: REM\n    test: Mann-Whitney U test\n    p: 3.0e-6\n    n: 86 PoS and 92 ADn HD cells\n  depends_on:\n  - fig5b-sleep-tuning-similar\n  expected:\n  - quantity: PoS HD cells with ADn decoded tuning curves\n    value: 86\n    tolerance: 8.6\n  - quantity: ADn HD cells with PoS decoded tuning curves\n    value: 92\n    tolerance: 9.2\n  criterion: The correlations of fig5b-sleep-tuning-similar for PoS HD cells (ADn decoded) and ADn\n    HD cells (PoS decoded). Reproduced when a two-sided Mann-Whitney U-test gives PoS cells higher\n    with p < 0.05 in each of waking, SWS and REM; partially reproduced in one or two states. The\n    p-values are reported against the paper's.\n- id: fig5d-adn-predicts-pos-reliably\n  statement: ADn assemblies predict PoS spike trains reliably in all brain states.\n  source: Results, paragraph 6; Figure 5d,e\n  quote: ADn assemblies predicted PoS spike trains reliably in all brain states ( Fig. 5d,e ; p < 10\n    –10 in all brain states, Wilcoxon’s signed rank test, n = 86)\n  statistics:\n  - test: Wilcoxon's signed rank test\n    p: 1.0e-10\n    p_relation: \"<\"\n    n: 86 PoS cells\n  depends_on:\n  - hd-cell-fraction\n  expected:\n    quantity: PoS cells predicted from ADn assemblies\n    value: 86\n    tolerance: 8.6\n  criterion: Method of the Methods (Information measures). For each target cell, a rate r(t) as a\n    weighted sum of the activity of the cells of the other structure's assembly in 10 ms bins\n    convolved with Gaussian readout windows, intensity g(r) with g a modified exponential, linear\n    for positive arguments; weights fit by a derivative-free search maximizing the likelihood on\n    9 of 10 segments of the state's epoch, tested on the tenth; predictability in bits per spike.\n    Targets kept when positively predicted for at least one readout window. Open, and named; (g-a)\n    g, given only in words; read as exp(x) for x below 0 and 1 + x above, the form of ref 36, which\n    the Methods cite for it; (g-b) the assembly, readings all simultaneously recorded cells of the\n    other structure, or its HD cells (Fig. 5d says \"PoS HD cell assembly\" and Fig. 5e \"ADn HD cell\n    assemblies\"); (g-c) the targets, all cells of the structure or its HD cells (5b counts HD\n    cells, 5d does not say); (g-d) the readout windows, not listed; 10 to 1000 ms on a log scale\n    used here. Reproduced when the information at the best window is above 0 by a two-sided\n    Wilcoxon signed-rank test with p < 1e-10 in each state, under one reading; partially reproduced\n    when p < 0.05 in each state and not below 1e-10.\n- id: fig5e-readout-windows\n  statement: The optimal readout windows of the ADn to PoS prediction are similar in waking and REM,\n    median 123 ms and 133 ms, and shorter in SWS, median 79 ms.\n  source: Results, paragraph 6; Figure 5d,e\n  quote: \"Optimal readout windows were similar between waking and REM (median: 123 ms and 133 ms\n    respectively) and shorter during SWS (median: 79 ms).\"\n  depends_on:\n  - fig5d-adn-predicts-pos-reliably\n  expected:\n  - quantity: median optimal readout window, waking\n    value: 123\n    tolerance: 12.3\n    unit: ms\n  - quantity: median optimal readout window, REM\n    value: 133\n    tolerance: 13.3\n    unit: ms\n  - quantity: median optimal readout window, SWS\n    value: 79\n    tolerance: 7.9\n    unit: ms\n  criterion: The window giving the highest information for each PoS target in\n    fig5d-adn-predicts-pos-reliably, its median over targets per state. Whether the window is the\n    Gaussian's s.d. or its full width is not said; readings (a) s.d., (b) full width at half\n    maximum. The window grid limits the precision; a grid of at least 20 windows per decade near\n    50 to 200 ms is used, a standard choice. Reproduced when all three medians are within tolerance\n    under one reading; partially reproduced when the SWS median is below both others and some\n    medians are outside.\n- id: fig5e-adn-predicts-pos\n  statement: PoS assemblies predict ADn spike trains more weakly than ADn assemblies predict PoS\n    spike trains, in all brain states and especially during SWS.\n  source: Results, paragraph 6; Figure 5d,e\n  quote: In the reverse direction, PoS cell assemblies predicted spike trains of ADn neurons more\n    weakly, especially during SWS\n  statistics:\n  - about: wake\n    test: Mann-Whitney U test\n    p: 3.0e-5\n    n: 86 PoS and 62 ADn neurons\n  - about: SWS\n    test: Mann-Whitney U test\n    p: 1.0e-10\n    p_relation: \"<\"\n    n: 86 PoS and 62 ADn neurons\n  - about: REM\n    test: Mann-Whitney U test\n    p: 1.1e-6\n    n: 86 PoS and 62 ADn neurons\n  - about: Figure 5e legend, all states\n    p: 1.0e-5\n    p_relation: \"<\"\n  depends_on:\n  - fig5d-adn-predicts-pos-reliably\n  expected:\n    quantity: ADn cells predicted from PoS assemblies\n    value: 62\n    tolerance: 6.2\n  criterion: The information at the best window for PoS targets (ADn assemblies) and ADn targets\n    (PoS assemblies), under the readings of fig5d-adn-predicts-pos-reliably. Reproduced when a\n    two-sided Mann-Whitney U-test gives PoS targets higher with p < 0.05 in each state and the gap\n    (difference of medians, relative to the PoS median) is largest in SWS; partially reproduced\n    when the test holds in each state and the gap is not largest in SWS, or the test holds in one\n    or two states.\n- id: fig6a-fast-oscillation\n  statement: Cross-correlograms between ADn HD cell pairs show fast oscillatory synchrony, with\n    periods of about 1 to 5 ms (130 to 160 Hz), in all brain states.\n  source: Results, paragraph 7; Figure 6a,c; Supplementary Figure 7a; Discussion, paragraph 4\n  quote: Spectral analysis of cross-correlation functions between pairs of HD cells in the ADn\n    revealed strong oscillatory spiking dynamics activity in windows of approximately 1–5 ms\n  depends_on:\n  - hd-cell-fraction\n  expected:\n  - quantity: frequency of the cross-correlogram oscillation, low end\n    value: 130\n    tolerance: 13\n    unit: Hz\n  - quantity: frequency of the cross-correlogram oscillation, high end\n    value: 160\n    tolerance: 16\n    unit: Hz\n  criterion: Method of the Fig. 6a legend. For each pair of ADn HD cells, the spike\n    cross-correlogram z-scored against 100 cross-correlograms of spike trains jittered uniformly\n    in plus or minus 10 ms windows, then wavelet transformed; average power across pairs per state\n    (Fig. 6c). The Discussion gives the band, 130 to 160 Hz. Open, and named; (o-a) the\n    cross-correlogram bin, not given for Fig. 6; 0.5 ms (the bin of the Methods' monosynaptic\n    analysis) used here, a standard choice; (o-b) the lag range, plus or minus 50 ms used here; (o-c)\n    the wavelet, a complex Morlet, a standard choice; (o-d) pairs on the same shank, left out here\n    as the Fig. 6a examples are on different shanks (an example, not a rule; kept as a variant).\n    Reproduced when, in each state, the frequency of peak average power above 80 Hz lies in the\n    range 117 to 176 Hz (130 to 160 Hz widened by 10% of each bound); partially reproduced in one\n    or two states.\n- id: fig6b-adn-synchrony\n  statement: Fast synchrony between ADn HD cell pairs decreases with the difference of their\n    preferred directions, in all brain states.\n  source: Results, paragraph 7; Figure 6b,c; Supplementary Figure 7a\n  quote: The degree of synchrony decreased with the magnitude of difference between the preferred\n    head directions of the neurons ( Fig. 6b ; p < 10 –10 ; Kruskal-Wallis test, n = 970 ADn HD cell\n    pairs) in all brain states\n  statistics:\n  - test: Kruskal-Wallis test\n    p: 1.0e-10\n    p_relation: \"<\"\n    n: 970 ADn HD cell pairs\n  depends_on:\n  - fig6a-fast-oscillation\n  expected:\n    quantity: ADn HD cell pairs\n    value: 970\n    tolerance: 97\n    unit: pairs\n  criterion: Amplitude of synchrony is the z-scored cross-correlogram of fig6a-fast-oscillation\n    (Fig. 6b legend, \"in z-values from baseline\"), under its readings. Open, and named; (y-a) the\n    amplitude, readings the peak z within plus or minus 5 ms of zero lag (the \"approximately 1-5 ms\"\n    windows) or the z of the zero-lag bin; (y-b) the offset groups for the Kruskal-Wallis test, not\n    given; 30 degree bins of absolute offset (six groups) used here, a standard choice. Reproduced\n    when the Kruskal-Wallis test across offset groups gives p < 1e-10 in waking with the mean\n    falling from the smallest to the largest offset group, and p < 0.05 with the same fall in SWS\n    and REM, under one reading; partially reproduced when it holds in waking only or at p < 0.05\n    only.\n- id: fig7-adn-pos-connections\n  statement: Putative monosynaptic connections were found in 4.45% of 6960 ADn to PoS pairs and in\n    0.35% from PoS to ADn; among ADn and PoS pyramidal cell pairs (3394), feed-forward ADn to PoS\n    connections were twice as likely as PoS to ADn (0.41% against 0.18%).\n  source: Results, paragraph 7; Figure 7a,b; Supplementary Figure 7b; Methods, Detection of\n    mono-synaptic connections\n  quote: cross-correlation analyses between pairs of ADn-PoS neurons revealed putative synaptic\n    connections in a fraction of the pairs (4.45% of 6960 pairs from ADn to PoS, 0.35% from PoS to\n    ADn ... When only ADn and PoS pyramidal cell pairs were considered (3394 pairs), we found\n    putative synaptic connections in both directions ( Supplementary Fig. 7b ) but the probability\n    of feed-forward connections from the ADn to the PoS was twice as high as the PoS to ADn\n    feedback direction (0.41% ADn-PoS pairs versus 0.18% PoS-ADn pairs; p = 0.014, binomial test)\n  statistics:\n  - about: ADn to PoS against PoS to ADn, pyramidal pairs\n    test: binomial test\n    p: 0.014\n    n: 3394 ADn HD cell and PoS pyramidal cell pairs, 14 and 6 connected (reporting checklist)\n  expected:\n  - quantity: pairs tested\n    value: 6960\n    tolerance: 696\n    unit: pairs\n  - quantity: fraction of pairs connected ADn to PoS\n    value: 0.0445\n    tolerance: 0.00445\n  - quantity: fraction of pairs connected PoS to ADn\n    value: 0.0035\n    tolerance: 0.00035\n  - quantity: ADn and PoS pyramidal pairs\n    value: 3394\n    tolerance: 339.4\n    unit: pairs\n  - quantity: fraction of pyramidal pairs connected ADn to PoS\n    value: 0.0041\n    tolerance: 0.00041\n  - quantity: fraction of pyramidal pairs connected PoS to ADn\n    value: 0.0018\n    tolerance: 0.00018\n  criterion: Method of the Methods (Detection of mono-synaptic connections). Cross-correlograms in\n    0.5 ms bins; baseline as the cross-correlogram convolved with a 10 ms s.d. Gaussian; a bin is\n    an outlier above the 99.9th percentile of the Poisson distribution at the baseline rate; a\n    putative excitatory connection when at least two consecutive bins at lags of 1 to 10 ms pass,\n    positive lags ADn to PoS and negative lags PoS to ADn. PoS pyramidal cells by the waveform\n    rule of the opening comment. Open, and named; (m-a) the pairs in 6960, readings all ADn cells\n    by all PoS cells, or ADn HD cells by all PoS cells (the checklist's 3394 are pairs of ADn HD\n    cells with PoS pyramidal cells), in sessions with both structures; (m-b) whether the bins\n    tested at lag 0 enter the convolution (a hollowed baseline, as in ref 58, or not), both run;\n    (m-c) the binomial test, readings 14 of 20 connections against one half, or the ADn to PoS count\n    against the PoS to ADn proportion over 3394 pairs (neither is stated, and the first gives a\n    two-sided p near 0.12, not 0.014). Reproduced when the four fractions are within tolerance and\n    the ADn to PoS fraction exceeds the PoS to ADn fraction in pyramidal pairs with a binomial p\n    < 0.05 under one reading; partially reproduced when the overall fractions are within tolerance\n    and the pyramidal ones are not. Each fraction rests on few connections (about 14 and 6), so the\n    counts are reported.\n- id: fig7c-adn-triggered-pos-lfp\n  statement: ADn HD cell spikes are associated with high-frequency oscillations of the PoS LFP.\n  source: Results, paragraph 7; Figure 7c\n  quote: ADn cell spiking was associated with high frequency LFP oscillations in the PoS ( Fig. 7c )\n  depends_on:\n  - hd-cell-fraction\n  criterion: Method of the Fig. 7c legend. The PoS wideband LFP (0 to 1250 Hz) averaged around the\n    spikes of each ADn HD cell (all spikes of ADn HD cells in each session), its average spectrum in\n    dB, and the average band-passed (80 to 250 Hz) trace. The paper gives no test; one is fixed\n    here. Open, and named; (l-a) the control, readings the same average at spike times jittered by\n    plus or minus 10 ms (the jitter of Fig. 7a), or at random times in the same state; (l-b) the\n    channel, the PoS channel with largest 80 to 250 Hz power, a standard choice; (l-c) the window,\n    plus or minus 20 ms around the spike. Reproduced when, under one reading, the power of the\n    80 to 250 Hz triggered average within plus or minus 5 ms of the spike exceeds the control in\n    most sessions with both structures and a two-sided Wilcoxon signed-rank test over ADn HD cells\n    gives p < 0.05; partially reproduced when the test holds and fewer than half the sessions\n    agree.\n- id: fig7d-same-preferred-direction\n  statement: PoS HD cells postsynaptic to ADn HD cells share the preferred direction of their\n    presynaptic cell.\n  source: Results, paragraph 7; Figure 7d\n  quote: Furthermore, PoS HD cells that were post-synaptic to ADn HD cells shared the same preferred\n    direction as their presynaptic neuron ( Fig. 7d , p = 0.68, Rayleigh test followed by\n    Wilcoxon’s signed rank test, n = 12)\n  statistics:\n  - about: difference of preferred directions against 0\n    test: Rayleigh test followed by Wilcoxon's signed rank test\n    p: 0.68\n    n: 12 ADn to PoS HD cell pairs\n  - about: unimodality of the differences (reporting checklist)\n    test: Rayleigh test\n    p: 2.4e-4\n    n: 12 ADn to PoS HD cell pairs\n  depends_on:\n  - fig7-adn-pos-connections\n  expected:\n    quantity: connected ADn to PoS HD cell pairs\n    value: 12\n    tolerance: 1.2\n    unit: pairs\n  criterion: For each connected ADn HD to PoS HD cell pair of fig7-adn-pos-connections, the circular\n    difference of the waking preferred directions. A claim of absence, judged on the paper's test.\n    The differences must be unimodal by a Rayleigh test (p < 0.05), and the Wilcoxon signed-rank\n    test of the differences against 0 (two-sided, at 0.05) must not find a shift. Reproduced when\n    the Rayleigh test has p < 0.05 and the Wilcoxon test p > 0.05; not reproduced when the Wilcoxon\n    test finds a shift or the differences are not unimodal. The median difference is reported.\n- id: fig7e-driven-pos-hd-information\n  statement: PoS pyramidal neurons driven by ADn HD cells convey more HD information than PoS\n    pyramidal neurons for which no presynaptic cell was identified.\n  source: Results, paragraph 7; Figure 7e\n  quote: Pyramidal neurons in PoS that were synaptically driven by ADn HD cells conveyed more HD\n    information than PoS neurons for which a presynaptic cell could not be identified ( Fig. 7e ; p =\n    0.011, Mann-Whitney U-test)\n  statistics:\n  - test: Mann-Whitney U-test\n    p: 0.011\n    n: 11 connected and 170 unconnected PoS pyramidal cells (reporting checklist)\n  depends_on:\n  - fig7-adn-pos-connections\n  - adn-pos-hd-information\n  expected:\n  - quantity: PoS pyramidal cells postsynaptic to an ADn HD cell\n    value: 11\n    tolerance: 1.1\n  - quantity: PoS pyramidal cells not connected\n    value: 170\n    tolerance: 17\n  criterion: HD information of each PoS putative pyramidal cell (opening comment), split by whether\n    it is postsynaptic to a recorded ADn HD cell in fig7-adn-pos-connections; only sessions with\n    both structures. Reproduced when a two-sided Mann-Whitney U-test gives the connected cells\n    higher with p < 0.05.\n- id: fig7e-interneurons-no-difference\n  statement: Putative PoS interneurons driven by ADn HD cells do not differ in HD information from\n    those for which no presynaptic cell was identified.\n  source: Results, paragraph 7; Figure 7e\n  quote: No such difference in HD information was observed between ADn neurons and putative\n    interneurons in PoS ( Fig. 7e ; p = 0.38).\n  statistics:\n  - test: Mann-Whitney U-test\n    p: 0.38\n    n: 13 connected and 79 unconnected PoS putative interneurons (reporting checklist)\n  depends_on:\n  - fig7-adn-pos-connections\n  - adn-pos-hd-information\n  expected:\n  - quantity: PoS putative interneurons postsynaptic to an ADn HD cell\n    value: 13\n    tolerance: 1.3\n  - quantity: PoS putative interneurons not connected\n    value: 79\n    tolerance: 7.9\n  criterion: As fig7e-driven-pos-hd-information, for PoS putative interneurons. The sentence's\n    \"between ADn neurons and putative interneurons\" is read through the checklist, which compares\n    connected with unconnected interneurons. A claim of absence, judged on the paper's test, a\n    two-sided Mann-Whitney U-test at 0.05. Reproduced when it does not find a difference; not\n    reproduced when it does. The difference of medians is reported either way.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/peyrache-2015.yaml paper/10.1038-nn.3968.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

The one problem is the checklist's garbled "p=1xe-8". I'll drop that entry, since the text's bound covers it, and note the value in prose. I'll also fix the change summary in the header.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/peyrache-2015.yaml",
 "old_string": "  - about: PoS-PoS pairs, SWS (reporting checklist)\n    test: Pearson's test\n    p: 1.0e-8\n    n: 92 PoS-PoS pairs\n  - about: PoS-PoS pairs, REM (reporting checklist)",
 "new_string": "  - about: PoS-PoS pairs, REM (reporting checklist; its SWS value is printed garbled, \"p=1xe-8\")"
}
```

```
The file claims/peyrache-2015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/peyrache-2015.yaml",
 "old_string": "# where the finding is the same. fig5e-adn-predicts-pos now holds the asymmetry alone; the readout\n# windows, the reliability of the ADn to PoS prediction, and twelve findings without a claim before\n# (recording-sample, supptable1-per-animal, hd-fraction-hd-shanks, supfig2a-unimodality,\n# supfig5-rate-independent, fig4d-ole-near-bayesian, fig5b-sleep-tuning-similar,\n# fig5d-adn-predicts-pos-reliably, fig5e-readout-windows, fig6a-fast-oscillation,\n# fig7e-interneurons-no-difference, fig2e-decoded-speed) are new claims.",
 "new_string": "# where the finding is the same (21 ids kept, criteria rewritten, regions kept apart as in the\n# paper). Two old claims are split. fig5e-adn-predicts-pos now holds the asymmetry alone, with the\n# readout windows in fig5e-readout-windows. fig7d-same-preferred-direction now holds the preferred\n# directions alone, with the HD information of driven PoS cells in\n# fig7e-driven-pos-hd-information. New claims for findings without one before are\n# recording-sample, supptable1-per-animal, hd-fraction-hd-shanks, supfig2a-unimodality,\n# supfig5-rate-independent, fig2e-decoded-speed, fig4d-ole-near-bayesian,\n# fig5b-sleep-tuning-similar, fig5d-adn-predicts-pos-reliably, fig6a-fast-oscillation and\n# fig7e-interneurons-no-difference."
}
```

```
The file claims/peyrache-2015.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/peyrache-2015.yaml paper/10.1038-nn.3968.txt; grep -n "—\|rather" claims/peyrache-2015.yaml; python3 - <<'EOF'
import yaml,re
d=yaml.safe_load(open('claims/peyrache-2015.yaml'))
c=d['claims']
print(len(c), sum('quote' in x for x in c), sum('inferred' in x for x in c), sum('statistics' in x for x in c), sum(len(x.get('statistics',[])) for x in c), sum('criterion' in x for x in c))
ids={x['id'] for x in c}
for x in c:
  for dpn in x.get('depends_on',[]): assert dpn in ids, dpn
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
git status --short
```

```
M claims/peyrache-2015.yaml
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

I rewrote `claims/peyrache-2015.yaml` from the paper alone, and the quote checker passes it with 0 problems.

**What I read.** The NIH author manuscript (PMC4376557) from Europe PMC: Results, Discussion, Methods and figure legends. Its three supplements were there too: the legends of Supplementary Figures 1 to 8, Supplementary Table 1 (recordings by animal), and the Nature Neuroscience reporting checklist, which gives exact p-values and sample sizes per test. The checklist numbers figures as in an earlier draft. There is no PDF of the article itself, so values printed only inside figures could not be read. The paper links no code, and the checklist answers N/A for custom software.

**What changed.** The old file was written after its author had seen the dataset's files. Several of its methods came from the data: finding the open field from position, pooling the two brain regions, how missing LED frames were handled. All of that is gone.
- **Kept:** 21 ids, with every criterion rewritten from the paper. The thalamic nucleus (ADn) and the post-subiculum (PoS) are now kept apart, as the paper does.
- **Split:** the readout windows moved out of `fig5e-adn-predicts-pos` into `fig5e-readout-windows`. The HD information of driven PoS cells moved out of `fig7d-same-preferred-direction` into `fig7e-driven-pos-hd-information`.
- **New, for findings that had no claim:** `recording-sample`, `supptable1-per-animal`, `hd-fraction-hd-shanks`, `supfig2a-unimodality`, `supfig5-rate-independent`, `fig2e-decoded-speed`, `fig4d-ole-near-bayesian`, `fig5b-sleep-tuning-similar`, `fig5d-adn-predicts-pos-reliably`, `fig6a-fast-oscillation`, `fig7e-interneurons-no-difference`.

**Counts.** 34 claims: 33 with quotes and 1 inferred (the Supplementary Table 1 counts). 15 claims carry statistics, 31 entries in all. All 34 have a criterion.

**Details the paper leaves open, with the readings named:**
- **HD cell rule:**
  - How the von Mises fit is made: a maximum-likelihood fit of the tuning curve taken as a distribution of angles, or a least-squares fit of a curve.
  - What sample the Rayleigh test uses.
  - Whether the peak rate is the fitted one or the tuning-curve maximum.
- **0.5 Hz rate threshold:** "in any of the three brain states" can mean in each state or in at least one.
- **Averages and counts:**
  - "41% on average" is an average over sessions or over animals; the pooled fraction is 34%.
  - Which sessions the "8.4 units per session" counts.
  - Which sessions make up the 42 in the text.
  - Which cells the 215/62 (Fig. 2a) and the 970/907 pairs (Fig. 2b against Fig. 3a) are.
- **Thresholds the paper never gives** for "strongly correlated", "similar", "faithfully", "remarkably similar" and "almost reached": I named readings or fixed a threshold, and said so in each criterion.
- **Angular-velocity fit:** the cross-correlogram bin and lag range, how the two directions of turning enter, and the coarse search grid.
- **Noise correlation:**
  - Lag: averaged over −50 to +50 ms (Methods), or at lag 0 (legend).
  - Scale: as the formula is written, or with 1 as chance (Supplementary Fig. 4).
  - The test of the sign at 0 and 60 degrees.
- **Packet coherence:** the distance between packets, how the reference vectors are drawn, and the smoothing windows.
- **Spike prediction model:**
  - The link function, read from the paper's ref 36.
  - Whether the predicting assemblies and the target cells are all cells or HD cells only.
  - The readout-window grid, and whether a window is the Gaussian's s.d. or its full width.
- **Fast synchrony:** the cross-correlogram bin and lag range, the wavelet, the amplitude measure (peak z or zero-lag z), and the offset groups.
- **Monosynaptic connections:**
  - Which pairs make up the 6960.
  - Whether the baseline is hollowed.
  - How the binomial test is set up: 14 of 20 against one half gives p near 0.12, not the reported 0.014.
- **PoS LFP triggered by ADn spikes:** the paper gives no test, so the control, the channel and the window are open.

**Missing from the paper:**
- **No OLE method.** The Results point to the Methods for the optimal linear estimator, but the Methods have no OLE section. `fig4d-ole-near-bayesian` and `fig4e-ole-covariance` use the standard Salinas and Abbott estimator, and both are marked as resting on that.
- **Session totals disagree.** Supplementary Table 1 sums to 50 sessions against 42 in the text.
- **Unreadable figure values.** The r values of the Fig. 2a,b insets and the errors of Fig. 4d are only inside figures, which are not available.
- **One garbled checklist value.** Its "p=1xe-8" was left out of the statistics and named in the file.

## End of run

21 turns, 8 minutes, $2.03 at API prices, result: success.
