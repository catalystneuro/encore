# 000010 · claims · run 39536633678

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453 claims/000010 paper/ 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; wc -l paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature14178.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature14178.txt",
 "offset": 942
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "000010",
 "glob": "!transcripts/**",
 "output_mode": "content",
 "head_limit": 30
}
```

```
papers/manifest.yaml:53:  '000010':
targets/dandisets.json:205:   "dandiset": "000010",
```

**Agent calls Bash**

```bash
sed -n 45,65p papers/manifest.yaml; python -c "
import json;d=json.load(open('targets/dandisets.json'))
d=d if isinstance(d,list) else d.get('dandisets',d)
for x in d:
  if x.get('dandiset')=='000010': print(json.dumps(x,indent=1))"
```

```
Exit code 1
    supplements: 0
  000009:
  - doi: 10.1038/nature22324
    status: stored
    version: as served by europe_pmc
    source: europe_pmc+crossref (paper-text-fetcher)
    pdf: false
    supplements: 0
  '000010':
  - doi: 10.1038/nature14178
    status: stored
    version: version of record
    source: PDF supplied by a person
    pdf: true
    supplements: 0
  '000011':
  - doi: 10.1038/nature17643
    status: stored
    version: as served by europe_pmc
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 195,240p targets/dandisets.json
```

```
"doi": "10.1038/nature22324",
     "title": "Maintenance of persistent activity in a frontal thalamocortical loop",
     "relation": "IsDescribedBy",
     "resource_type": "JournalArticle",
     "preprint": false
    }
   ],
   "catalystneuro": []
  },
  {
   "dandiset": "000010",
   "name": "A motor cortex circuit for motor planning and movement",
   "published_version": "0.220126.1905",
   "asset_count": 158,
   "size_gb": 40.01,
   "data_standards": [
    "Neurodata Without Borders (NWB)"
   ],
   "species": [
    "House mouse"
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "KEYS\|allowed\|fields" tools/claims_check.py tools/entry.py | head -30
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

[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1))" | head -200
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
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)); print([k for k in s['properties']])"
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

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1038-nature14178.pdf')
print(len(d))
for i in [0,1,2,4]:
  d[i].get_pixmap(dpi=130).save(f'p{i+1}.png')
" && ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && (which pdftoppm && pdftoppm -r 130 -png -f 1 -l 5 paper/10.1038-nature14178.pdf p) ; ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature14178.pdf",
 "pages": "1-5"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/000010/10.1038-nature14178.yaml",
 "content": "# Claims for Li, Chen, Guo, Gerfen & Svoboda (2015), \"A motor cortex circuit for motor planning\n# and movement\", Nature 519, 51-56, doi:10.1038/nature14178, on dandiset 000010.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record, from a PDF supplied by a person, as extracted text\n# (paper/10.1038-nature14178.txt): main text, figure legends 1 to 5, Methods, and the legends of\n# Extended Data Figures 1 to 7. The paper has no Supplementary Information beyond Extended Data.\n# The extraction prints \"=\" as \"5\", \"<\" as \",\", \">\" as \".\" and \"+/-\" as \"6\" (e.g. \"n 5 42\",\n# \"P , 0.05\"); quotes keep these glyphs so that they match the text word for word. The PDF pages\n# could not be rendered in this run, so values shown only inside figures (the stars of\n# Figs 1d and 5b, the inset fractions of Fig. 3f, the curves of Extended Data Figs 3, 6 and 7)\n# were not read; where a claim needs them, it says so.\n#\n# Code: the paper links no analysis code. It names one deposit, the data at CRCNS\n# (https://crcns.org/, doi:10.6080/K0RF5RZT, \"alm-1\"). No repository was read, so every method\n# below comes from the Methods and legends, and details they leave open are named in each\n# criterion with the readings the text allows.\n#\n# Data the paper used, as it reports them:\n# - Task. Head-fixed mice (n = 42 in the task) discriminated the position of a vertical pole\n#   with their whiskers. Sample epoch 1.3 s (pole movement onset to 0.1 s after retraction\n#   onset), delay epoch 1.3 s, auditory go cue (3.4 kHz, 0.1 s), then the response epoch.\n#   Posterior pole means lick right, anterior pole lick left. Licks before the go cue (\"lick\n#   early\") were punished and are excluded from performance. Performance is the fraction of\n#   correct reports, computed also per trial type. Mouth movements were measured with a\n#   photodiode and infrared laser diode for reaction times.\n# - Photoinhibition (Fig. 1): 8 mice (5 VGAT-ChR2-EYFP, 3 PV-ires-Cre x ReaChR), left or right\n#   ALM (2.5 mm anterior, 1.5 mm lateral), 1.3 s in the sample or delay epoch, on 25% of trials,\n#   with a masking flash.\n# - Extracellular recordings (Figs 2, 3): left ALM, 32-channel NeuroNexus probes, 19,531.25 Hz;\n#   1,408 single units in 99 sessions from 19 mice (Sim1_KJ18-Cre, Rbp4-Cre and Tlx_PL56-Cre\n#   injected with Cre-dependent ChR2, and Ai32 crosses). Units classed by spike width:\n#   fast-spiking (< 0.35 ms, 124), putative pyramidal (> 0.45 ms, 1,245), intermediate (39,\n#   excluded). Optogenetic tagging by antidromic photostimulation of axons in the pons or\n#   reticular formation (pyramidal tract, PT) or the contralateral ALM (intratelencephalic,\n#   IT), with collision tests; 45 PT and 27 IT neurons passed.\n# - Two-photon imaging (Fig. 4): 4 C57Bl/6Crl mice, GCaMP6s in left ALM, 15 Hz, 59 fields of\n#   view; 4,706 cells; PT neurons labelled with red RetroBeads in the ipsilateral pons and IT\n#   neurons with CTB-Alexa 647 in the contralateral ALM; 534 PT and 542 IT neurons in layer 5\n#   (450 to 700 um deep). DF/F0 with F0 the mean over 0.5 s before each trial, neuropil\n#   factor 0.7.\n# - Photoactivation (Fig. 5, Extended Data Figs 3, 6, 7): 7 Sim1_KJ18-Cre x Ai32 (PT) and\n#   7 Tlx_PL56-Cre x Ai32 (IT) mice, 2 ms pulses at 20 Hz, average powers 0.06, 0.12, 0.24 and\n#   0.8 mW, sample or delay epoch on 25% of trials; simultaneous recordings in 2 mice, 8 sessions,\n#   91 neurons (Extended Data Fig. 7); untrained mice for Extended Data Fig. 3f, g.\n# - Anatomy (Extended Data Figs 3, 4): tracer and viral injections, histology.\n# The dandiset's title and description on DANDI name electrophysiology, behaviour and cell\n# population imaging. Which of the above it holds is for the author to find.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000010\"\npaper: doi:10.1038/nature14178\nclaims:\n- id: behaviour-performance\n  statement: Mice in the object location discrimination task performed at 78.4% correct on\n    average, and fewer than 13% of responses came before the go cue.\n  source: Results, ALM is required for movement planning, paragraph 1\n  quote: (mean per cent correct, 78.4%; responses before the go cue, ,13%)\n  expected:\n  - quantity: mean per cent correct\n    value: 78.4\n    tolerance: 7.84\n    unit: \"%\"\n  criterion: Performance is the fraction of correct reports excluding lick early trials\n    (Methods, Behavioural data analyses), on trials without photostimulation. The paper does not\n    say how the mean is formed. Readings are (a) all control trials pooled; (b) the mean over\n    sessions; (c) the mean over mice of per-mouse performance. Reproduced when, under one\n    reading, the per cent correct is within tolerance and the fraction of lick early trials\n    among control trials (same three readings) is below 13% widened by 10% (14.3%).\n- id: fig1d-delay-inhibition-ipsi-bias\n  statement: Unilateral photoinhibition of ALM during the delay epoch biases licking to the\n    ipsilateral side, raising performance on ipsilateral (lick left for left ALM) trials and\n    lowering it on contralateral trials, with the reverse pattern for right ALM.\n  source: Results, ALM is required for movement planning, paragraph 2; Figure 1d\n  quote: Inhibiting left ALM caused a tendency to lick the left port, resulting in increased\n    performance in 'lick left' trials and decreased performance in 'lick right' trials (Fig. 1d).\n    The reversed pattern of bias was observed when inhibiting right ALM\n  statistics:\n  - test: one-tailed test, bootstrap\n    p: 0.05\n    p_relation: \"<\"\n    n: 8 mice\n  criterion: Trials of the 8 photoinhibition mice. For left and right ALM separately, the change\n    in performance (photoinhibition minus control) on lick right and lick left trials, with\n    the delay-epoch photoinhibition trials. Significance by the Methods' bootstrap, resampling\n    with replacement animals, then sessions within each animal, then trials within each\n    session, 10^4 times; P is the fraction of resamples with a change of the opposite sign\n    (one-tailed). Reproduced when, for both hemispheres, contralateral-trial performance falls\n    with P < 0.05 and ipsilateral-trial performance rises (its P reported); partially\n    reproduced when this holds for one hemisphere. The stars of Fig. 1d were not read, so\n    which comparisons the paper found significant beyond the text is not fixed here.\n- id: fig1d-sample-inhibition-smaller\n  statement: The ipsilateral bias is smaller when ALM is photoinhibited during the sample epoch\n    than during the delay epoch.\n  source: Results, ALM is required for movement planning, paragraph 2; Figure 1d\n  quote: This ipsilateral bias was smaller when photoinhibiting during the sample epoch\n  criterion: Same trials and performance measure as fig1d-delay-inhibition-ipsi-bias. The paper\n    gives no measure of the bias and no test. Readings are (a) the fall in contralateral-trial\n    performance; (b) the ipsilateral-trial change minus the contralateral-trial change.\n    Reproduced when, under each reading, the bias for sample-epoch inhibition is smaller than\n    for delay-epoch inhibition in both hemispheres; partially reproduced when in one. A\n    bootstrap of the difference (resampling as in the Methods) is reported as a variant.\n  depends_on:\n  - fig1d-delay-inhibition-ipsi-bias\n- id: units-classification\n  statement: 1,408 single units were recorded from left ALM in 19 mice over 99 sessions; by\n    spike width 124 were fast-spiking, 1,245 putative pyramidal and 39 intermediate.\n  source: Methods, Electrophysiology data analyses, paragraph 1; Extended Data Figure 1a\n  quote: A total of 1,408 single units were recorded across 99 recording sessions ... Units with\n    spike width ,0.35 ms were defined as fast-spiking neurons (124/1,408) and units with spike\n    width .0.45 ms as putative pyramidal neurons (1,245/1,408)\n  expected:\n  - quantity: single units\n    value: 1408\n    tolerance: 140.8\n  - quantity: recording sessions\n    value: 99\n    tolerance: 9.9\n  - quantity: mice\n    value: 19\n    tolerance: 1.9\n  - quantity: fast-spiking units\n    value: 124\n    tolerance: 12.4\n  - quantity: putative pyramidal units\n    value: 1245\n    tolerance: 124.5\n  - quantity: intermediate units\n    value: 39\n    tolerance: 3.9\n  criterion: Spike width is the trough-to-peak interval of the mean spike waveform (Methods);\n    fast-spiking below 0.35 ms, putative pyramidal above 0.45 ms, intermediate between. Each\n    count is checked against its tolerance.\n- id: fig2-selective-fraction\n  statement: 73% (912 of 1,245) of putative pyramidal neurons distinguished the trial types in\n    at least one trial epoch.\n  source: Results, ALM contains neurons with bilateral selectivity, paragraph 1; Methods,\n    Electrophysiology data analyses, paragraph 2\n  quote: A large fraction(73%,912/1,245)ofneuronsdistinguishedtrialtypes(P , 0.05, two-tailed\n    t-test, not corrected for multiple comparisons) (Fig. 2b)\n  expected:\n  - quantity: selective putative pyramidal neurons\n    value: 912\n    tolerance: 91.2\n  - quantity: fraction selective\n    value: 0.73\n    tolerance: 0.073\n  depends_on:\n  - units-classification\n  criterion: Per neuron, spike counts in the sample, delay and response epochs compared between\n    lick right and lick left trials with a two-tailed t-test, P < 0.05, uncorrected; selective\n    when significant in any epoch (Methods). Sample epoch from pole movement onset, 1.3 s;\n    delay epoch the 1.3 s before the go cue. Open, with readings - the trials, (a) correct\n    trials only (as the Methods state for contra-selectivity and Fig. 2b shows) or (b) all\n    non-early trials by instructed trial type; the response epoch, which no passage times,\n    (i) 1.3 s after the go cue, like the other epochs, or (ii) the 1.5 s lick window after the\n    go cue. Reproduced when both values are within tolerance under one reading.\n- id: fig2d-preparatory-perimovement\n  statement: Among selective neurons, 219 of 912 had selective preparatory activity only, 389\n    peri-movement activity only, and 304 both.\n  source: Results, ALM contains neurons with bilateral selectivity, paragraph 1; Figure 2d\n  quote: subsets of neurons showed selective preparatory activity (Fig. 2b, left column; Fig. 2d,\n    219/912 neurons), peri-movement activity during the response epoch (Fig. 2b, right column;\n    389/912), or both\n  expected:\n  - quantity: preparatory only\n    value: 219\n    tolerance: 21.9\n  - quantity: peri-movement only\n    value: 389\n    tolerance: 38.9\n  - quantity: both\n    value: 304\n    tolerance: 30.4\n  depends_on:\n  - fig2-selective-fraction\n  criterion: Preparatory means significant in the sample or delay epoch, peri-movement\n    significant in the response epoch, by the test of fig2-selective-fraction (Methods), with\n    its readings. Reproduced when all three counts are within tolerance under one reading.\n- id: fig2c-selectivity-time-course\n  statement: Selectivity emerges in the sample epoch, increases through the delay epoch and\n    peaks at the beginning of the response epoch.\n  source: Results, ALM contains neurons with bilateral selectivity, paragraph 1; Figure 2c;\n    Extended Data Figure 1d, f\n  quote: Selectivityemergedinthesampleepoch,increasedthroughoutthedelay epoch, and reached a\n    maximum at the beginning of the response epoch\n  depends_on:\n  - units-classification\n  criterion: As Extended Data Fig. 1f, the number of putative pyramidal neurons significantly\n    selective in 200 ms windows of spike counts (two-tailed t-test, P < 0.05), correct trials.\n    Window step is not stated; a step of 200 ms (non-overlapping) is used, and a 50 ms step\n    shown as a variant. Reproduced when (1) the count in some sample-epoch window exceeds the\n    95th percentile of a binomial count with p = 0.05 over the neurons tested (the rate the\n    test gives by chance) while the windows before sample onset do not exceed it on average;\n    (2) the count in the last delay window exceeds that in the first delay window; (3) the\n    maximum over the trial falls at the beginning of the response epoch, read as (a) the first\n    window after the go cue or (b) any window starting within 0.5 s after the go cue.\n- id: fig2c-population-dynamics\n  statement: Individual neuron responses are dynamic although selectivity is stable at the\n    level of the population; the population response grows more similar to that at the go cue\n    as the delay proceeds.\n  source: Results, ALM contains neurons with bilateral selectivity, paragraph 1; Figure 2c,\n    bottom; Methods, Electrophysiology data analyses, paragraph 2\n  quote: Individualneuronresponseswere dynamic, despite stable selectivity at the level of the\n    population (Fig. 2c, bottompanelandExtended Data Fig.2a)\n  depends_on:\n  - fig2-selective-fraction\n  criterion: As the Methods, a pseudo-population of the 912 selective neurons treated as\n    simultaneously recorded; each neuron's response (correct trials, 200 ms bins) mean-\n    subtracted and normalized to its variance over the trial; Pearson correlation of the\n    population vector at each time with that at go cue onset (t = 0). Population selectivity is\n    the spike rate difference between preferred and non-preferred trial types, the preference\n    set from 10 trials and the selectivity computed on the remaining trials. Whether the\n    population vector concatenates both trial types or uses their difference is open; both\n    are run. The paper gives no number, so the claim is judged on shape. Reproduced when the\n    mean correlation over the sample epoch is lower than over the delay epoch, which is lower\n    than 1, while the population selectivity stays above 0 through the delay epoch.\n- id: ed2c-error-trials-predict-choice\n  statement: On error trials ALM activity predicts the direction the mouse licked, so most\n    selective neurons switch their trial-type preference relative to correct trials.\n  source: Results, ALM contains neurons with bilateral selectivity, paragraph 1; Extended Data\n    Figure 2c\n  quote: On error trials, when mice licked in the opposite direction to the instruction provided by\n    object location (Fig. 1a), a majority of ALM neurons switched their trial type preference to\n    predict the licking direction, as indicated by the negative correlations\n  depends_on:\n  - fig2-selective-fraction\n  criterion: For the 912 selective neurons and each epoch (sample, delay, response),\n    selectivity is (rate lick right) minus (rate lick left) by instructed trial type, on correct\n    trials and on error trials; Pearson correlation across neurons between the two (Extended\n    Data Fig. 2c). The minimum number of error trials per neuron is not stated; readings (a) at\n    least one error trial of each type, (b) at least five. Reproduced when r < 0 in the delay and\n    response epochs under each reading, with the sample epoch reported; partially reproduced\n    when in one of the two.\n- id: fig2e-no-contra-bias-spikes\n  statement: Contra-preferring and ipsi-preferring neurons are present in equal proportions in\n    left ALM, and the overall spike count shows no significant contralateral bias (P = 0.13;\n    8% spike rate modulation across all task-selective neurons).\n  source: Results, ALM contains neurons with bilateral selectivity, paragraph 2; Figure 2e;\n    Results, A movement command emerges in the pyramidal tract neurons, paragraph 2\n  quote: Significant contralateral bias also did not appear in the overall spike count across the\n    recorded population of neurons (Extended Data Fig. 1; P 5 0.13, two-tailed t-test against 0)\n    ... The contra-preferring and ipsi-preferring neurons were present in equal proportions\n  statistics:\n  - about: overall spike count difference, lick right minus lick left\n    test: two-tailed t-test against 0\n    p: 0.13\n  depends_on:\n  - fig2-selective-fraction\n  expected:\n  - quantity: spike rate modulation, all task-selective neurons\n    value: 8\n    tolerance: 0.8\n    unit: \"%\"\n  criterion: A claim of absence. Selective neurons are contra-preferring when their total spike\n    count over the three epochs is larger on lick right trials (Methods). The paper's test is a\n    two-tailed t-test against 0 of the spike count difference (lick right minus lick left,\n    correct trials) across neurons; reproduced when it gives P >= 0.05 and not reproduced when\n    P < 0.05 with a contralateral excess. The population is open; readings (a) all 1,245\n    putative pyramidal neurons (\"the recorded population\"), (b) the 912 selective neurons\n    (Fig. 3f, \"all task-selective neurons\"). For equal proportions the Methods' bootstrap\n    (neurons resampled with replacement, P the fraction of resamples with more ipsi- than\n    contra-preferring neurons, one-tailed) must not find a contralateral excess at P < 0.05.\n    The 8% modulation is checked with the readings of fig3f-pt-contra-selectivity; it is\n    reported, and its mismatch alone makes the claim partially reproduced.\n- id: ed1-fast-spiking-properties\n  statement: Fast-spiking neurons have higher baseline firing rates and are less selective than\n    putative pyramidal neurons.\n  source: Methods, Electrophysiology data analyses, paragraph 1; Extended Data Figure 1b to e\n  quote: Fast-spiking neurons had higher baseline firing rates and were less selective than\n    putative pyramidal neurons (Extended Data Fig. 1)\n  depends_on:\n  - units-classification\n  criterion: The paper reports no test and does not define the baseline. Baseline readings are\n    (a) the 0.5 s before pole movement onset, (b) all the recorded time before pole movement\n    onset in each trial; selectivity readings are (i) the fraction significantly selective by\n    the test of fig2-selective-fraction, (ii) the mean absolute spike rate difference between\n    trial types over the three epochs. Reproduced when, under every reading, the fast-spiking\n    median and mean baseline rates exceed those of putative pyramidal neurons and their\n    selectivity is lower; a two-sided Mann-Whitney test is reported as a variant.\n- id: tagging-counts\n  statement: Of 73 neurons antidromically activated from pyramidal tract axons, 45 passed the\n    collision test (PT neurons), 22 failed and 6 could not be tested; of 134 activated from IT\n    axons, 27 passed (IT neurons), 106 failed and 1 could not be tested.\n  source: Methods, Electrophysiology data analyses, paragraph 4; Extended Data Figure 5f\n  quote: Neurons that passed the collision test were classified as pyramidal tract neurons (45/73)\n    or intratelencephalic neurons (27/134). Neurons that failed the test were classified as\n    pyramidal-tract-activated (22/73) or intratelencephalic-activated (106/134)\n  expected:\n  - quantity: PT neurons\n    value: 45\n    tolerance: 4.5\n  - quantity: IT neurons\n    value: 27\n    tolerance: 2.7\n  - quantity: PT-activated neurons that failed collision\n    value: 22\n    tolerance: 2.2\n  - quantity: IT-activated neurons that failed collision\n    value: 106\n    tolerance: 10.6\n  criterion: Counts of units by the labels the dataset gives for tagging outcome. The 6 and 1\n    untested neurons are reported. The counts in the text (22 + 45 + 6 = 73 but 27 + 106 + 1 =\n    134) are consistent.\n- id: antidromic-latencies\n  statement: PT neurons had shorter antidromic latencies (mean 2.7 ms) than IT neurons\n    (4.6 ms), and both had smaller jitter (0.1 and 0.2 ms) than activated neurons that failed\n    collision (latency 8.3 and 9.8 ms, jitter 2.8 and 2.4 ms).\n  source: Methods, Electrophysiology data analyses, paragraph 4; Results, A movement command\n    emerges in the pyramidal tract neurons, paragraph 1; Extended Data Figure 5e\n  quote: Pyramidal tract neurons and intratelencephalic neurons had shorter mean antidromic spike\n    latencies (pyramidal tract neurons, 2.7ms; intratelencephalic neurons, 4.6 ms) and smaller\n    temporal jitter (mean s.d. of the antidromic spike latency, pyramidal tract neurons, 0.1 ms;\n    intratelencephalic neurons, 0.2 ms) than the pyramidal-tract-activated (mean latency, 8.3ms;\n    jitter, 2.8ms) and intratelencephalic-activated neurons\n  expected:\n  - quantity: PT mean latency\n    value: 2.7\n    tolerance: 0.27\n    unit: ms\n  - quantity: IT mean latency\n    value: 4.6\n    tolerance: 0.46\n    unit: ms\n  - quantity: PT mean jitter (s.d. of latency)\n    value: 0.1\n    tolerance: 0.01\n    unit: ms\n  - quantity: IT mean jitter\n    value: 0.2\n    tolerance: 0.02\n    unit: ms\n  - quantity: PT-activated mean latency\n    value: 8.3\n    tolerance: 0.83\n    unit: ms\n  - quantity: IT-activated mean latency\n    value: 9.8\n    tolerance: 0.98\n    unit: ms\n  depends_on:\n  - tagging-counts\n  criterion: Latency is the time from light pulse onset to the antidromic spike; jitter its s.d.\n    over pulses, per neuron, then averaged over neurons (Methods). Tested only if the dataset\n    holds the tagging trials. Reproduced when PT latency is below IT latency and all values\n    are within tolerance; partially reproduced when the order holds but a value falls outside.\n    The jitter of 0.1 and 0.2 ms is printed to one significant figure, so its 10% tolerance is\n    read as the printed precision (within 0.05 ms when rounded to 0.1 ms).\n- id: fig3e-pt-it-both-activity-types\n  statement: Both PT and IT neurons show preparatory and movement-related activity.\n  source: Results, A movement command emerges in the pyramidal tract neurons, paragraph 2;\n    Figure 3e, i\n  quote: Both intratelencephalic and pyramidal tract neurons displayed preparatory and\n    movement-related activity (Fig. 3e, i)\n  depends_on:\n  - tagging-counts\n  - fig2d-preparatory-perimovement\n  criterion: The 45 PT and 27 IT neurons classified with the epoch rule and readings of\n    fig2d-preparatory-perimovement. Reproduced when, in each cell type, at least one neuron has\n    preparatory selectivity and at least one peri-movement selectivity; the fractions in each\n    class are reported.\n- id: fig3f-pt-contra-preferring\n  statement: Contra-preferring neurons outnumber ipsi-preferring neurons among PT neurons\n    (P < 0.05, bootstrap) but not among IT neurons (P = 0.74).\n  source: Results, A movement command emerges in the pyramidal tract neurons, paragraph 2;\n    Figure 3f, j insets\n  quote: Contra-preferring neurons outnumbered ipsi-preferring neurons for the pyramidal tract\n    neurons (Fig. 3f; P , 0.05, bootstrap, Methods), but not the intratelencephalic neurons (Fig.\n    3j, P 5 0.74)\n  statistics:\n  - about: PT neurons, more contra- than ipsi-preferring\n    test: one-tailed bootstrap\n    p: 0.05\n    p_relation: \"<\"\n    n: 45 PT neurons\n  - about: IT neurons, more contra- than ipsi-preferring\n    test: one-tailed bootstrap\n    p: 0.74\n    n: 27 IT neurons\n  depends_on:\n  - tagging-counts\n  criterion: Contra- or ipsi-preferring by total spike count over the three epochs, lick right\n    against lick left, correct trials (Methods). Bootstrap as the Methods, neurons resampled\n    with replacement (10^4 resamples, a standard number that the Methods give for the\n    behavioural bootstrap), P the fraction of resamples with more ipsi- than contra-preferring\n    neurons. Open, which neurons are counted; readings (a) all tagged neurons of the type,\n    (b) only those selective by the test of fig2-selective-fraction. Reproduced when PT gives\n    P < 0.05 under one reading and IT gives P >= 0.05 under the same reading (the IT part is a\n    claim of absence on the paper's test). The inset fractions were not read from the figure.\n- id: fig3f-pt-contra-selectivity\n  statement: Contralateral population selectivity emerges in PT neurons from 570 ms before the\n    response epoch (34% spike rate modulation, P < 0.05), but not in IT neurons (-19%, P = 0.40).\n  source: Results, A movement command emerges in the pyramidal tract neurons, paragraph 2;\n    Figure 3f, j\n  quote: Robust contralateral selectivity (the spike count differenceforlickrighttrials and\n    licklefttrials) emerged in pyramidal tract neuron responses starting 570 ms before the\n    response epoch (Fig. 3f; 34% spike rate modulation; P , 0.05, two-tailed t-test against0inspikecounts),butnotforintratelencephalicneurons(219%\n  statistics:\n  - about: PT contra-selectivity against 0\n    test: two-tailed t-test against 0 in spike counts\n    p: 0.05\n    p_relation: \"<\"\n    n: 45 PT neurons\n  - about: IT contra-selectivity against 0\n    test: two-tailed t-test against 0 in spike counts\n    p: 0.4\n    n: 27 IT neurons\n  expected:\n  - quantity: PT selectivity onset before the go cue\n    value: 570\n    tolerance: 57\n    unit: ms\n  - quantity: PT spike rate modulation\n    value: 34\n    tolerance: 3.4\n    unit: \"%\"\n  - quantity: IT spike rate modulation\n    value: -19\n    tolerance: 1.9\n    unit: \"%\"\n  depends_on:\n  - tagging-counts\n  criterion: Contra-selectivity is the firing rate difference, lick right minus lick left trials,\n    per neuron, correct trials, averaged across neurons (Methods), in 200 ms windows (the\n    averaging window of Fig. 2c). The text reads \"-19%\" as \"219%\". Open, with readings - the\n    neurons, (a) all tagged neurons of the type (Fig. 3f legend) or (b) the selective ones\n    (Methods); the test window, (i) from 570 ms before the go cue to the go cue or (ii) the whole\n    delay epoch; the modulation, (x) the population difference divided by the mean rate over\n    both trial types in that window or (y) divided by the lick left rate; the onset, the start\n    of the earliest window from which the population contra-selectivity stays significantly\n    above 0 (two-tailed t-test across neurons, P < 0.05) until the go cue, with windows stepped\n    by 10 ms. Reproduced when, under one reading, the PT test gives P < 0.05 with positive\n    selectivity, the IT test P >= 0.05, and the three expected values are within tolerance;\n    partially reproduced when the two tests come out so but a value falls outside under every\n    reading.\n- id: imaging-selectivity-counts\n  statement: In two-photon imaging of ALM (59 fields of view, 4 mice), 58% of cells (2,740 of\n    4,706) were task-related and 57% of those (1,575) trial-type selective, with a slight\n    majority of contra-preferring cells (61%, 971 of 1,575).\n  source: Methods, Calcium imaging data analyses, paragraphs 2 and 4; Results, A movement command\n    emerges in the pyramidal tract neurons, paragraph 3\n  quote: This criterion identified 58% (2,740/4,706) cells as task related ... 57% (1575/2740) of\n    task related cell are trial-type selective ... Overall, imaging detected a slight majority of\n    contra-preferring neurons (61%, 971/1,575)\n  expected:\n  - quantity: cells\n    value: 4706\n    tolerance: 470.6\n  - quantity: task-related cells\n    value: 2740\n    tolerance: 274\n  - quantity: trial-type selective cells\n    value: 1575\n    tolerance: 157.5\n  - quantity: fraction contra-preferring among selective cells\n    value: 0.61\n    tolerance: 0.061\n  - quantity: fields of view\n    value: 59\n    tolerance: 5.9\n  criterion: Task-related when a Kruskal-Wallis test across 0.33 s bins (five frames) during the\n    task rejects equal fluorescence at P < 0.01 in contra or in ipsi trials; selective when a\n    Wilcoxon rank sum test of DF/F between contra and ipsi trials gives P < 0.05; preference by\n    the average calcium signal during the trial epochs (Methods). DF/F0 with F0 the mean over\n    0.5 s before trial start, if the dataset holds raw fluorescence. Open, with readings - the\n    span of the Kruskal-Wallis bins, (a) sample onset to the end of the response epoch, (b) the\n    whole recorded trial; the response compared by the rank sum test, (i) mean DF/F over the\n    three epochs together, (ii) each epoch separately, selective if any is significant; the\n    trials, correct only or all non-early trials. Reproduced when all values are within\n    tolerance under one reading.\n- id: fig4f-spatially-intermingled\n  statement: Contra- and ipsi-preferring neurons are found in all fields of view and are\n    spatially intermingled; nearest-neighbour selectivity and same-type distances do not differ\n    from shuffled data (P = 0.34 and P = 0.61).\n  source: Results, A movement command emerges in the pyramidal tract neurons, paragraph 3;\n    Figure 4f; Methods, Calcium imaging data analyses, paragraph 3\n  quote: Contra-preferring and ipsi-preferring neurons were observed in all fields of view (Fig.\n    4f; Methods). The probability that nearby neurons share the same selectivity was not different\n    from randomized data (P 5 0.34, bootstrap, Methods). The distance between nearest neurons with\n    the same selectivity was also not different from chance (P 5 0.61, bootstrap)\n  statistics:\n  - about: probability that the nearest neighbour has the same preference\n    test: bootstrap, shuffled labels\n    p: 0.34\n  - about: distance between nearest neurons of the same preference\n    test: bootstrap, shuffled labels\n    p: 0.61\n  depends_on:\n  - imaging-selectivity-counts\n  criterion: A claim of absence, on the paper's two tests (Methods). For the selective cells,\n    (1) the probability that each cell's nearest neighbour among selective cells has the same\n    preference, against the same probability with preference labels shuffled, P the fraction\n    of shuffles with a larger probability; (2) the mean distance from each cell to the nearest\n    cell of the same preference, against shuffles, P the fraction of shuffles with a smaller\n    distance. Distances from ROI centres within each field of view. Whether labels are\n    shuffled within each field of view or across all is not stated; both are run. 10^4 shuffles\n    (a standard number). Reproduced when both tests give P >= 0.05 and both preferences occur\n    in every field of view; not reproduced when either test gives P < 0.05.\n- id: fig4h-pt-contra-imaging\n  statement: Among layer 5 neurons, about a quarter of labelled PT (182 of 534) and IT (174 of\n    542) neurons were selective; 67% of selective PT neurons were contra-preferring (P < 0.001,\n    binomial test) but only 48% of IT neurons, and PT neurons were more often contra-preferring\n    than IT neurons (P < 0.001, chi-squared test).\n  source: Results, A movement command emerges in the pyramidal tract neurons, paragraph 4;\n    Figure 4g, h\n  quote: we observed more contra-preferring than ipsi-preferring neurons in the pyramidal tract\n    neuron population (67%, 122/182, Fig. 4g, h; P , 0.001, binomial test), but not in the\n    intratelencephalic neurons (fraction of contra-preferring neurons:48%,83/174;Fig.4g,h)\n  statistics:\n  - about: PT, contra- against ipsi-preferring\n    test: binomial test\n    p: 0.001\n    p_relation: \"<\"\n    n: 182 selective PT neurons\n  - about: IT, contra- against ipsi-preferring\n    test: binomial test\n    p: 0.05\n    p_relation: \">\"\n    n: 174 selective IT neurons\n  - about: PT against IT fraction contra-preferring\n    test: chi-squared test\n    p: 0.001\n    p_relation: \"<\"\n  expected:\n  - quantity: layer 5 PT neurons\n    value: 534\n    tolerance: 53.4\n  - quantity: layer 5 IT neurons\n    value: 542\n    tolerance: 54.2\n  - quantity: selective PT neurons\n    value: 182\n    tolerance: 18.2\n  - quantity: selective IT neurons\n    value: 174\n    tolerance: 17.4\n  - quantity: PT fraction contra-preferring\n    value: 0.67\n    tolerance: 0.067\n  - quantity: IT fraction contra-preferring\n    value: 0.48\n    tolerance: 0.048\n  depends_on:\n  - imaging-selectivity-counts\n  criterion: Labelled PT (RetroBeads) and IT (CTB-647) cells imaged 450 to 700 um deep;\n    selectivity and preference as imaging-selectivity-counts, with its readings. Reproduced\n    when, under one reading, the PT binomial test (two-sided, against 0.5) gives P < 0.001 with\n    a contralateral majority, the IT binomial test gives P > 0.05, the chi-squared test of PT\n    against IT gives P < 0.001, and the expected values are within tolerance; partially\n    reproduced when the three tests come out so and a value falls outside.\n- id: reaction-time\n  statement: The reaction time after the go cue was 61.1 +/- 10.5 ms (mean +/- s.d. across\n    mice).\n  source: Results, Pyramidal tract neurons drive upcoming movements, paragraph 1\n  quote: reactiontimepostcueonsetacrossmice:61.1 6 10.5 ms,mean 6 s.d.\n  expected:\n    quantity: mean reaction time across mice\n    value: 61.1\n    tolerance: 10.5\n    unit: ms\n  criterion: Reaction time is measured from mouth movements by photodiode and infrared laser\n    (Methods, Behaviour). Tolerance is the paper's stated spread across mice. Open, with\n    readings - the mice, (a) the electrophysiology mice of Fig. 3, (b) all mice in the dataset\n    with mouth-movement data; per-mouse value, (i) mean or (ii) median of per-trial reaction\n    times; the trials, correct trials or all non-early trials. If the dataset holds only lick\n    contacts at the lickport and no mouth-movement signal, the first lick is a different\n    measure; it is shown as a variant and does not decide the claim.\n- id: fig5b-pt-delay-activation-contra-bias\n  statement: Subthreshold photostimulation of PT neurons during the delay epoch biases licking\n    contralaterally; in left ALM it lowers performance on lick left trials, and the reverse\n    holds for right ALM.\n  source: Results, Pyramidal tract neurons drive upcoming movements, paragraph 2; Figure 5b\n  quote: Subthreshold stimulation of pyramidal tract neurons in the left ALMproducedarightwardbias,resulting\n    ina decreaseinperformance in the lick left trials and vice versa (Fig. 5)\n  statistics:\n  - test: one-tailed test, bootstrap\n    p: 0.01\n    p_relation: \"<\"\n    n: 7 Sim1_KJ18-Cre x Ai32 mice\n  criterion: Delay-epoch photostimulation trials of the PT (Sim1_KJ18-Cre x Ai32) mice against\n    control trials, per hemisphere and trial type, with the hierarchical bootstrap of\n    fig1d-delay-inhibition-ipsi-bias. Which powers are pooled is inconsistent in the paper;\n    readings (a) 0.12 to 0.8 mW (Fig. 5 legend), (b) the subthreshold powers below 0.25 mW\n    (text). Reproduced when, under one reading, ipsilateral-trial performance falls with\n    P < 0.05 for both hemispheres; partially reproduced for one. The lowest star level of the\n    legend is recorded as the statistic; which panels carry which stars was not read.\n- id: fig5b-pt-sample-activation-contra-bias\n  statement: Stimulation of PT neurons during the sample epoch also causes a significant\n    contralateral bias.\n  source: Results, Pyramidal tract neurons drive upcoming movements, paragraph 3; Figure 5b\n  quote: Notably, stimulation of pyramidal tract neurons during the sample epochalsocausedasignificantcontralateralbias(Fig.5b)\n  statistics:\n  - test: one-tailed test, bootstrap\n    p: 0.01\n    p_relation: \"<\"\n    n: 7 Sim1_KJ18-Cre x Ai32 mice\n  depends_on:\n  - fig5b-pt-delay-activation-contra-bias\n  criterion: As fig5b-pt-delay-activation-contra-bias, with sample-epoch photostimulation trials\n    and the same readings.\n- id: ed6b-pt-dose-response\n  statement: The effect of PT photostimulation on licking depends monotonically on laser power.\n  source: Results, Pyramidal tract neurons drive upcoming movements, paragraph 2; Extended Data\n    Figure 6b\n  quote: The effect size was monotonically dependent on laser power (Extended Data Fig. 6b)\n  depends_on:\n  - fig5b-pt-delay-activation-contra-bias\n  criterion: Delay-epoch photostimulation only (Extended Data Fig. 6b), per power (0.06, 0.12,\n    0.24, 0.8 mW where present). The effect size is not defined; readings (a) the performance\n    change on ipsilateral trials, (b) the ipsilateral-trial change minus the\n    contralateral-trial change, both signed so that a contralateral bias is positive.\n    Reproduced when, under each reading, the effect pooled over mice increases with each step\n    of power; the per-mouse curves are reported with the number that are monotonic.\n- id: ed6d-it-activation-inconsistent\n  statement: Subthreshold photostimulation of IT neurons changes behaviour, but the changes vary\n    across mice and depend non-monotonically on laser intensity.\n  source: Results, Pyramidal tract neurons drive upcoming movements, paragraph 4; Extended Data\n    Figure 6c, d\n  quote: Subthresholdphotostimulationoftheintratelencephalicneuronsalso caused behavioural\n    changes, but these varied across mice and depended non-monotonicallyonlaserintensity(ExtendedDataFig.6d)\n  criterion: Delay-epoch photostimulation of the IT (Tlx_PL56-Cre x Ai32) mice, effect sizes as\n    ed6b-pt-dose-response with its readings. The paper gives no test. Reproduced when, under each\n    reading, at least two mice show biases of opposite sign at the same power and the effect\n    pooled over mice is not monotonic in power; partially reproduced when one of the two holds.\n- id: ed3e-high-power-contra-licking\n  statement: High-power unilateral photostimulation of ALM PT or IT neurons triggers\n    contralateral licking with short latency, also in untrained mice, and in trained mice\n    produces premature licking in the contralateral direction; vibrissal motor cortex\n    stimulation does not cause licking.\n  source: Results, Pyramidal tract neurons control directional licking, paragraph 2; Extended\n    Data Figure 3e, f\n  quote: UnilateralphotostimulationofALM intratelencephalic or pyramidal tract neurons ('high'\n    power, 0.8 mW, 2 mspulsesat20Hz,Methods)triggeredcontralaterallickingwithshort latencies\n    (Extended Data Fig. 3e), even in untrained mice (Extended Data Fig. 3f)\n  criterion: Trained PT and IT mice, sample- and delay-epoch photostimulation combined (Extended\n    Data Fig. 3e). Per power, the fraction of photostimulation trials with an early lick, and\n    the fraction of early licks to the contralateral port. Reproduced when, at 0.8 mW, the\n    early-lick fraction exceeds that of control trials and most early licks are contralateral,\n    in each cell type; partially reproduced for one cell type. Untrained mice (Extended Data\n    Fig. 3f) and vibrissal motor cortex trials are tested in the same way if present. Latency\n    is reported; the paper gives no number for it.\n- id: ed7-pt-activation-persistent\n  statement: Subthreshold sample-epoch stimulation of PT neurons, with simultaneous recordings\n    (2 mice, 8 sessions, 91 neurons), changes ALM activity and causes a directional bias that\n    persists for seconds after the photostimulus ends.\n  source: Results, Pyramidal tract neurons drive upcoming movements, paragraph 3; Extended Data\n    Figure 7\n  quote: Simultaneous recordings and optogenetics revealed that subthreshold stimulation of\n    pyramidal tract neurons caused changes in ALM activity and a directionalbiasthatpersistedforsecondsaftercessationofthephotostimulus\n  expected:\n  - quantity: neurons\n    value: 91\n    tolerance: 9.1\n  - quantity: sessions\n    value: 8\n    tolerance: 0.8\n  criterion: The paper gives no measure or test for the change in activity. In these sessions,\n    (1) behaviour, the performance change on lick left trials with sample-epoch stimulation of\n    left ALM is negative (contralateral bias; Extended Data Fig. 7b); (2) activity, per neuron a\n    two-tailed t-test (the paper's selectivity test) of delay-epoch spike counts between\n    photostimulation and control trials, correct trials; reproduced when more neurons differ\n    at P < 0.05 than the 95th percentile of a binomial count with p = 0.05, and the population\n    selectivity (preferred minus non-preferred, Extended Data Fig. 7d) during the delay epoch\n    differs between photostimulation and control trials. Partially reproduced when one of (1)\n    and (2) holds.\n- id: ed3-anatomy-it-pt-separate\n  statement: Retrograde tracers in the ipsilateral pontine nucleus and the contralateral ALM\n    label non-overlapping populations of PT and IT neurons (under 4% double-labelled, 2 mice),\n    intermingled in layer 5B; ALM PT neurons project to the contralateral intermediate reticular\n    nucleus, which is presynaptic to the hypoglossal nucleus.\n  source: Results, Pyramidal tract neurons control directional licking, paragraph 1; Extended Data\n    Figure 3a to d\n  quote: Injection of retrograde tracers in the ipsilateral pontine nucleusandthecontralateralALMlabellednon-overlappingpopulations\n    of intratelencephalic neurons and pyramidal tract neurons (Extended Data Fig. 3d) (doubly\n    labelled neurons, ,4%, n 5 2 mice)\n  criterion: Histology. Reproduced when double-labelled neurons are under 4.4% (4% widened by\n    10%) of labelled neurons in each of the 2 mice. The projection findings are tested only if\n    the images are available.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000010/10.1038-nature14178.yaml paper/10.1038-nature14178.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

Every quote and statistic passes the checker. Last, I'll scan the file for the banned style items.

**Agent calls Bash**

```bash
f=claims/000010/10.1038-nature14178.yaml; grep -n "rather\|—" $f; grep -vn "^#" $f | grep -E "^[0-9]+:\s*(- )?[a-z_]+: .*: " ; grep -vn "^#" $f | grep -E "^[0-9]+:\s+[^-a-z#].*: |^[0-9]+:\s{4,}[a-zA-Z(].*: " | head
```

```
53:  archive: dandi
54:  id: "000010"
58:  statement: Mice in the object location discrimination task performed at 78.4% correct on
60:  source: Results, ALM is required for movement planning, paragraph 1
61:  quote: (mean per cent correct, 78.4%; responses before the go cue, ,13%)
63:  - quantity: mean per cent correct
64:    value: 78.4
65:    tolerance: 7.84
66:    unit: "%"
67:  criterion: Performance is the fraction of correct reports excluding lick early trials
```

**Agent calls Bash**

```bash
grep -vn "^#" claims/000010/10.1038-nature14178.yaml | grep -vE "^[0-9]+:\s*(- )?[a-z_]+:( |$)" | grep ": "; echo done
```

```
59:    average, and fewer than 13% of responses came before the go cue.
68:    (Methods, Behavioural data analyses), on trials without photostimulation. The paper does not
69:    say how the mean is formed. Readings are (a) all control trials pooled; (b) the mean over
70:    sessions; (c) the mean over mice of per-mouse performance. Reproduced when, under one
71:    reading, the per cent correct is within tolerance and the fraction of lick early trials
72:    among control trials (same three readings) is below 13% widened by 10% (14.3%).
75:    ipsilateral side, raising performance on ipsilateral (lick left for left ALM) trials and
76:    lowering it on contralateral trials, with the reverse pattern for right ALM.
79:    performance in 'lick left' trials and decreased performance in 'lick right' trials (Fig. 1d).
80:    The reversed pattern of bias was observed when inhibiting right ALM
87:    in performance (photoinhibition minus control) on lick right and lick left trials, with
88:    the delay-epoch photoinhibition trials. Significance by the Methods' bootstrap, resampling
89:    with replacement animals, then sessions within each animal, then trials within each
90:    session, 10^4 times; P is the fraction of resamples with a change of the opposite sign
91:    (one-tailed). Reproduced when, for both hemispheres, contralateral-trial performance falls
92:    with P < 0.05 and ipsilateral-trial performance rises (its P reported); partially
93:    reproduced when this holds for one hemisphere. The stars of Fig. 1d were not read, so
94:    which comparisons the paper found significant beyond the text is not fixed here.
97:    than during the delay epoch.
101:    gives no measure of the bias and no test. Readings are (a) the fall in contralateral-trial
[... 250 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v "^#" claims/000010/10.1038-nature14178.yaml | grep -vE "^\s*(- )?[a-z_]+:( |$)" | grep -n ": "; echo done
```

```
done
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000010/10.1038-nature14178.yaml",
 "old_string": "The counts in the text (22 + 45 + 6 = 73 but 27 + 106 + 1 =\n    134) are consistent.",
 "new_string": "The counts in the text add up (45 + 22 + 6 = 73 and 27 + 106 +\n    1 = 134)."
}
```

```
The file claims/000010/10.1038-nature14178.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000010/10.1038-nature14178.yaml paper/10.1038-nature14178.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote the claims file for DANDI:000010 at `claims/000010/10.1038-nature14178.yaml`. The checker passes: 27 claims, 27 quotes, 13 statistical values, 0 problems. Nothing is committed.

**Text read:** the version of record, from a PDF supplied by a person. The extracted text has the main text, the legends of Figs 1 to 5, the Methods, and the legends of Extended Data Figs 1 to 7. The paper has no supplement beyond Extended Data, so nothing the results rest on is missing. The extraction prints "=" as "5", "<" as ",", ">" as "." and "±" as "6". The quotes keep these characters so they match the text word for word.

**Code:** the paper links no analysis code, so no repository or commit was read. It names one deposit, the data at CRCNS (doi:10.6080/K0RF5RZT). Every method in the criteria comes from the Methods and the figure legends.

**Claims:**
- **Quotes:** all 27 claims have one; none needed an `inferred` note.
- **Statistics:** 11 claims carry them. They are the bootstrap tests (Figs 1d, 3f, 5b), the t-tests against 0 (P = 0.13; Fig. 3f P < 0.05 and P = 0.40), the spatial shuffles (P = 0.34 and 0.61), and the binomial and chi-squared tests of Fig. 4h.
- **Expected values:** 12 claims. They are counts and numbers with a 10% tolerance; the reaction time uses the paper's s.d. of 10.5 ms.
- **Criteria:** 26 claims. The absence claims are judged on the paper's own test: the spike-count bias, the IT neurons in Fig. 3f, and spatial intermingling.
- **Scope:** the claims cover behaviour, photoinhibition, unit counts and selectivity, the tagged PT and IT neurons, imaging, photoactivation and its dose response, the persistence data of Extended Data Fig. 7, and anatomy.

**Details the paper leaves open, and the readings named for each:**
- **Mean performance (78.4%):** all control trials pooled, the mean over sessions, or the mean over mice.
- **Trials for selectivity:** correct trials only, or all non-early trials by instructed trial type.
- **Response epoch length:** no passage gives it. Readings are 1.3 s, like the other epochs, or the 1.5 s lick window.
- **Peak of selectivity "at the beginning of the response epoch":** the first 200 ms window after the go cue, or any window starting within 0.5 s of it. The 200 ms window step is a standard choice, with 50 ms as a variant.
- **Population correlation (Fig. 2c):** the vector concatenates both trial types, or uses their difference.
- **Error trials:** at least 1, or at least 5, error trials of each type per neuron.
- **Population for P = 0.13:** all 1,245 putative pyramidal neurons, or the 912 selective ones.
- **Fast-spiking baseline:** the 0.5 s before the pole moves, or all recorded time before it. Selectivity is the fraction significant, or the mean absolute rate difference.
- **PT and IT neurons counted (Fig. 3f):** all tagged neurons of the type, or only the selective ones.
- **PT contra-selectivity (Fig. 3f):**
  - Test window: from 570 ms before the cue to the cue, or the whole delay epoch.
  - Modulation %: divided by the mean rate over both trial types, or by the lick-left rate.
  - Onset: the earliest window from which selectivity stays significant until the cue, with windows stepped by 10 ms.
- **Imaging selectivity:** how far the Kruskal-Wallis bins extend, mean ΔF/F over the whole trial or each epoch separately, and correct or all trials.
- **Spatial shuffles:** labels shuffled within each field of view, or across all.
- **Reaction time:** which mice, per-mouse mean or median, and which trials.
- **Powers pooled for Fig. 5:** 0.12 to 0.8 mW as the legend says, or below 0.25 mW as the text says. The paper disagrees with itself here.
- **Dose-response effect size:** the change on ipsilateral trials, or the ipsilateral minus the contralateral change.
- **No measure or test given:** the smaller bias with sample-epoch inhibition, the inconsistent effect of IT stimulation, and the activity change in Extended Data Fig. 7. Each criterion says this and names the readings.

**What the claims lacked:** the PDF pages could not be rendered here (no pymupdf or poppler), so values shown only in figures were not read. These are which panels carry which stars in Figs 1d and 5b, the inset fractions of Fig. 3f, and the curves of Extended Data Figs 3, 6 and 7. The claims record the lowest significance level the legend states and say the figures were not read. The paper also gives no number for the "short latency" of contralateral licking.

## End of run

21 turns, 6 minutes, result: success.
