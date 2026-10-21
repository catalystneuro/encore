# 000009 · claims · run 39499898922

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453 claims/000009 paper/ 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -40 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 30,200p claims/001453/*.yaml; echo ----; grep -n "^checks:" -A40 claims/001453/*.yaml | head -60
```

```
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
    the counts per species are compared instead. The sign of the zebrafish turning response
    to codes 9 and 11 is reported, as the code and the protocol file disagree on which of them
    is lateral right.
- id: fig1d-dc-faster-all-codes
  statement: Danionella cerebrum (DC) swim at a higher median velocity than zebrafish (ZF)
[... 152 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l paper/*.txt; head -30 paper/*.txt; cat tools/claims_check.py | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nature22324.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR; python3 -c "
s=open('paper/10.1038-nature22324.txt').read()
print(s[51900:78000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
s=open('paper/10.1038-nature22324.txt').read()
import re
print(len(s))
for m in re.finditer(r'Figure [1-6] |Fig\. 1 |Supplementary [Ii]nformation|Supplementary Table', s): print(m.start(), s[m.start()-60:m.start()+100].replace('\n',' '))
print(s[-3000:])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls claims/; grep -il "supplement.*not\|not.*supplement" claims/*/*.yaml | head; grep -h -i -m3 "supplement" claims/*/*.yaml | head -30
```

```
000003
000004
000005
000006
000008
000035
000041
000044
000056
000059
000061
000067
000070
000114
000121
000127
000130
000147
000207
000213
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000009/ | python3 -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000009/versions/" | python3 -c "import json,sys; d=json.load(sys.stdin); print([ (v['version'],v['name']) for v in d['results']])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000009/versions/0.220126.1903/ | python3 -c "
import json,sys; d=json.load(sys.stdin)
for k in ['description','keywords','relatedResource','approach','measurementTechnique','variableMeasured','assetsSummary','citation']: print(k, json.dumps(d.get(k),indent=0)[:1500])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python3 -c "
s=open('paper/10.1038-nature22324.txt').read()
print(s[85380:91500])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -40 claims/000006/*.yaml; grep -n "open\|reading" claims/000006/*.yaml | head -20
```

```
# Claims for Economo, Viswanathan, Tasic et al. (2018) on dandiset 000006.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20, protocol
# as stated in docs/protocol.md (pilot-10), Reader steps 1 to 4.
#
# Why this file was rewritten. The earlier file was written from the abstract only and is
# deprecated. Read against the full text on 2026-10-20, its claims pt-lower-late-and-motor and
# pt-types-differ-in-timing were tested with fractions of selective units and a label-shuffle null,
# measures the paper does not use (it uses coding directions, a hierarchical bootstrap and single
# neuron early selectivity), and eleven of the paper's findings on these data had no claim. This
# file is written again from the full text. Ids are kept where the finding is the same:
# pt-types-transcriptomic, pt-types-shared-targets, pt-upper-thalamus-projection,
# pt-lower-medulla-projection, pt-preparatory-activity, pt-upper-early-preparatory,
# pt-upper-persistent, pt-lower-late-and-motor and pt-types-differ-in-timing. All their criteria
# are new; the old shuffle null, McNemar and Fisher tests are gone, as the paper uses none of them.
# pt-lower-late-and-motor now tests selectivity along CDlate and CDgo (Fig. 6b, c; Extended Data
# Fig. 7b); pt-types-differ-in-timing is now the summary of the coding direction claims it
# depends on. The other claims are new.
#
# Text read: the version of record (Nature 563, 79-84, 2018), as the PDF supplied by a person and
# its text extraction (paper/10.1038-s41586-018-0642-9.txt): main text, Methods, Extended Data
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,200p tools/claims_check.py | grep -v "^\s*$" | head -150
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
import yaml
sys.path.insert(0, str(Path(__file__).resolve().parent))
from entry import _plain, schema  # noqa: E402
# Inline markup removed without leaving a space, so that "p<sub>1</sub>" reads "p1".
INLINE = (r"</?(italic|bold|sup|sub|sc|underline|xref|ext-link|named-content|inline-formula|mml:[a-z]+"
[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d,indent=1)[:6000])"
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
[... 185 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('schemas/claims.schema.json'));print(json.dumps(d['\$defs'],indent=1)[:4000])"
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

**Agent**

Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000009/10.1038-nature22324.yaml",
 "content": "# Claims for Guo, Inagaki, Daie, Druckmann, Gerfen & Svoboda (2017) on dandiset 000009.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-20, protocol\n# as stated in docs/protocol.md (pilot-10), Reader steps 1 to 4.\n#\n# Text read: the HHMI author manuscript in PubMed Central (PMC6431254, NIHMS865428), as served by\n# Europe PMC (paper/10.1038-nature22324.txt): main text, Methods, the legends of Figures 1 to 6 and\n# of Extended Data Figures 1 to 10. It is the accepted manuscript, not the version of record. No PDF\n# was supplied, so no figure could be read. Not in the text: the Supplementary Information\n# (supp_info: further whole-cell methods, the model of the latency T3 and the network models of\n# Extended Data Fig. 7c-e, lick-early, no-response and lick-latency rates under photoinhibition) and\n# Supplementary Tables 1 and 2 (animals, coordinates, photostimulus powers, viruses). The claims\n# latency-model-t3 and network-models rest on the Supplementary Information and are written from\n# the main text and Extended Data legends only; no other claim needs it.\n#\n# Code read: none. The paper links no analysis code. It names the data deposit \"CRCNS.ORG in the NWB\n# format (https://doi.org/10.6080/K03F4MH2)\". The dandiset's archive title is the paper's title, and\n# its description (the abstract) says it holds spikes from ALM and thalamus during the task with\n# photoinhibition; its metadata list Units, BehavioralTimeSeries, CurrentClampStimulusSeries and\n# OptogeneticSeries, 31 subjects. Which of the experiments below it holds is for the author to find.\n#\n# The data the paper used, as it reports them (Methods). 71 mice, adult (> P60), male and female.\n# Lines: PV-IRES-Cre x Ai32 (ALM photoinhibition, Fig. 1c, 6, Extended Data Figs 8, 10), VGAT-ChR2-EYFP\n# (thalamus photoinhibition during ALM and thalamic recordings, Fig. 3, 4, 5), Gad2-IRES-Cre with\n# AAV2/10 CAG-flex-ChR2 injected in TRN (thalamus photoinhibition in behaviour, Fig. 1d, and in\n# Extended Data Figs 2c, 5c-h), Olig3-cre x Ai32 (thalamus photoactivation, Extended Data Fig. 6c).\n# Task: a pole in one of two positions (8.58 mm apart, anterior-posterior); sample epoch 1.3 s from\n# the onset of pole movement to 0.1 s after the pole starts to retract; delay epoch 1.2 or 1.3 s; a\n# go cue (3.4 kHz, 0.1 s); then the mouse licks left or right. Trials with licks before the go cue\n# ('lick early') and with no lick within 1.5 s of the go cue ('no response') are excluded from all\n# analyses (Methods, Behavior). Recordings are from the left hemisphere, so 'contra' trials are\n# those whose instructed (correct) lick is to the right, and 'ipsi' trials to the left; for\n# behaviour, contra and ipsi are relative to the manipulated side (Fig. 1a legend; Methods,\n# Behavioral data analysis). Photoinhibition: on 25% of trials (Fig. 1, 3a-f, 6) or 25-50%\n# (Fig. 3g, 4); in cortex 40 Hz sinusoid, 1.5 mW average, 1.3 s including a 100 ms ramp from the\n# start of the delay epoch; in thalamus continuous light through a 200 um fibre, 1.2 to 1.3 s from\n# the start of the delay epoch, 10 mW (Extended Data Fig. 2), or 0.5 mW for the weak photoinhibition\n# of Fig. 5. Units: ALM 1214 units in 57 sessions (10 mice in Results), split by trough-to-peak\n# spike width into putative fast-spiking (< 0.4 ms, 166), putative pyramidal (> 0.6 ms, 1006) and\n# unclassified (42); thalamus 790 units in 73 sessions (11 mice), putative thalamic neurons with\n# width > 0.5 ms (672), VM/VAL units within 0.4 mm of the VM/VAL centre (313 of 790; 295 in the\n# Results); SNr 227 units in 23 sessions, putative GABAergic with width < 0.45 ms (181). Whole-cell\n# recordings in ALM (and M1), Vm sampled at 20 kHz, 350 to 850 um below the pia. Measured\n# variables: spike times, unit position, spike waveform, trial type, licks and outcome,\n# photostimulus timing, membrane potential.\n#\n# Conventions used by the criteria below (all from the Methods unless marked open).\n# E (epochs). Sample: 1.3 s from the onset of pole movement. Delay: from the end of the sample\n#   epoch to the go cue. Response: from the go cue; its length is not given. Open, with readings\n#   (R1) 1.3 s after the go cue, the length of the other epochs, (R2) 1.5 s after the go cue, the\n#   response window that defines 'no response'.\n# S (selectivity, Methods, Electrophysiology data analysis). A unit is selective in an epoch when\n#   its spike counts in the epoch differ between correct contra and correct ipsi trials (two-sided\n#   t-test, P < 0.05); 'selective' means selective in any of the three epochs; 'preparatory\n#   activity' means selective in the sample or delay epoch; 'peri-movement selectivity' means\n#   selective in the response epoch. Contra- or ipsi-preferring is decided by the total spike count\n#   over the three epochs. Selectivity is contra minus ipsi firing rate, correct trials only.\n#   Whether the t-test assumes equal variances is not stated (Student's in the behavioural\n#   analysis); open, readings (a) Student's, (b) Welch's.\n# P (photoinhibition effect). Units with at least 5 photoinhibition trials (Fig. 3, 6) or 25\n#   (Fig. 5). Rate in the window 20 to 120 ms after photostimulus onset (the delay onset), in\n#   photoinhibition trials against control trials in the same window, contra and ipsi trials\n#   pooled. Which outcomes enter is open: the Methods include correct and incorrect trials for\n#   PSTHs \"as photoinhibition reduced neural activity irrespective of the response outcomes\" and\n#   say nothing for the scatter plots; readings (T1) correct and incorrect, (T2) correct only. A\n#   unit is inhibited or activated by the sign of the change, and significantly so by a two-sided\n#   t-test, P < 0.05, on single-trial rates. \"To X% of control\" has readings (Q1) mean over units\n#   of the photoinhibition rate over mean over units of the control rate, (Q2) mean over units of\n#   each unit's ratio, (Q3) median of each unit's ratio.\n# O (onset of inhibition in spikes; Methods, last paragraph of Electrophysiology data analysis).\n#   Population PSTH in 1 ms bins; onset is the time after photostimulus onset when the\n#   photoinhibition PSTH falls more than 3 standard deviations below control, the standard\n#   deviation taken from the control condition during the delay epoch; SEM by resampling units with\n#   replacement, 1000 times. Open: the level the 3 SD are counted from, readings (O1) the control\n#   PSTH in the same bin, (O2) the mean of the control PSTH over the delay epoch. The Methods'\n#   wording (\"the membrane potential passed\") is read as the PSTH, as the paragraph is about\n#   extracellular units.\n# V (membrane potential; Methods, In vivo whole-cell recording). Spikes clipped by the 'kink'\n#   rule (derivative above 3 SD of its value 2.5 to 1.5 ms before the spike peak; -0.5 to 5 ms\n#   around the kink interpolated). Onset of a Vm change is when Vm changes by more than 3 SD from\n#   the baseline, mean and SD taken from 20 ms before to 2 ms after photostimulus onset in\n#   photoinhibition trials; SEM of means and onsets by bootstrapping. Open: onset of the cell-mean\n#   trace with bootstrap SEM over cells (V1), or the mean of per-cell onsets (V2).\n# L (location). VM/VAL units are those within 0.4 mm of the VM/VAL centre, \"determined from\n#   retrograde labeling experiments\". The text gives no coordinate for the centre. Open, readings\n#   (L1) the dataset's own location label for VM/VAL, if it has one; (L2) within 0.4 mm of AP\n#   -1.5, ML 0.85, DV 4.0 mm, the thalALM injection site \"mainly in VM\" (Extended Data Fig. 9\n#   legend). The count 295 (VM/VAL putative thalamic units) checks the reading.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000009\"\npaper: doi:10.1038/nature22324\nclaims:\n- id: task-performance\n  statement: Mice performed the delayed-response task at 77.6% correct on average, with 10.3% lick-early\n    trials and 1.1% no-response trials.\n  source: Results, Thalamus is required for motor preparation, paragraph 1\n  quote: mean percent correct 77.6%; lick-early before ‘go’ cue 10.3%, no response 1.1%\n  expected:\n  - quantity: mean percent correct\n    value: 77.6\n    tolerance: 7.76\n    unit: percent\n  - quantity: lick-early trials\n    value: 10.3\n    tolerance: 1.03\n    unit: percent\n  - quantity: no-response trials\n    value: 1.1\n    tolerance: 0.11\n    unit: percent\n  criterion: The paper does not say over which trials or sessions these are taken. Readings (a) all\n    trials of all sessions pooled; (b) mean over sessions; (c) control (non-photoinhibition) trials\n    only, pooled and per session. Percent correct excludes lick-early and no-response trials\n    (Methods, Behavioral data analysis); lick-early and no-response are fractions of all trials.\n    Reproduced when all three values are within tolerance under one reading.\n- id: fig1c-alm-photoinhibition-bias\n  statement: Unilateral photoinhibition of ALM during the delay epoch biased responses to the\n    ipsilateral side, lowering performance on contra trials and raising it on ipsi trials.\n  source: Results, Thalamus is required for motor preparation, paragraph 1; Figure 1c\n  quote: Unilateral photoinhibition of ALM during the delay epoch produced an ipsilateral response bias\n    ... reducing performance for contralateral trials and increasing performance for ipsilateral trials\n    ( P < 0.001; paired t -test, Fig. 1c )\n  statistics:\n  - test: paired t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 84 behavioural sessions, 11 mice\n  criterion: Per session, fraction correct (lick-early and no-response excluded) on contra and on ipsi\n    trials, in control and in ALM photoinhibition trials (PV-IRES-Cre x Ai32 mice, left ALM; Methods,\n    Photoinhibition). Two-sided paired t-test over sessions of photoinhibition against control,\n    separately for contra and ipsi trials. Reproduced when contra performance is lower and ipsi\n    performance higher under photoinhibition, both at p < 0.001; partially reproduced when the\n    contra decrease holds at p < 0.001 and the ipsi increase does not.\n- id: fig1d-thalamus-photoinhibition-bias\n  statement: Unilateral photoinhibition of thalALM during the delay epoch lowered performance on contra\n    trials and caused a small, non-significant improvement on ipsi trials.\n  source: Results, Thalamus is required for motor preparation, paragraph 3; Figure 1d\n  quote: Similar to ALM, unilateral photoinhibition of thal ALM during the delay epoch reduced\n    performance for contralateral trials and caused a small improvement in performance for ipsilateral\n    trials ( P < 0.001 for contralateral trials, not significant for ipsilateral trials, paired t -test\n  statistics:\n  - about: contra trials, photoinhibition against control\n    test: paired t-test\n    p: 0.001\n    p_relation: \"<\"\n    n: 9 sessions, 4 mice\n  criterion: As fig1c-alm-photoinhibition-bias, for thalamus photoinhibition through an optical fibre\n    over VM/VAL in Gad2-IRES-Cre mice with ChR2 in TRN (Methods, Photoinhibition). Reproduced when\n    contra performance is lower under photoinhibition at p < 0.001 (paired t-test over sessions);\n    the ipsi change and its p-value are reported (the paper finds it not significant, p >= 0.05).\n- id: gad2-thalamus-reduction\n  statement: Photostimulating TRN axons in thalamus of Gad2-IRES-Cre mice reduced thalALM spike rates,\n    recorded near VM/VAL, to 67.8% of control during the delay epoch.\n  source: Results, Thalamus is required for motor preparation, paragraph 3; Extended Data Figure 2c\n  quote: Photostimulating axonal terminals of TRN GABAergic neurons in thalamus reduced spike rates in\n    thal ALM (recorded near VM/VAL, to 67.8% during the delay epoch\n  expected:\n    quantity: photoinhibition rate as a percentage of control\n    value: 67.8\n    tolerance: 6.78\n    unit: percent\n  criterion: Putative thalamic units recorded with the optrode in Gad2-IRES-Cre mice (Extended Data Fig.\n    2c, n = 26, 41 and 17 at 0.6, 0.8 and 1.0 mm from the fibre). The legend gives the measure as \"mean\n    spike rate during photoinhibition divided by mean spike rate during control\". The window is open,\n    readings (W1) the whole photostimulus (delay onset to delay end, as \"during the delay epoch\"\n    says), (W2) 20 to 120 ms after photostimulus onset (convention P). Ratio readings Q1 to Q3 and\n    trial readings T1, T2 of convention P. Reproduced when the value is within tolerance under one\n    reading; the value per distance group is reported.\n- id: vgat-thalamus-reduction\n  statement: In VGAT-ChR2-EYFP mice, thalamus photoinhibition reduced activity 0.5 to 1.1 mm from the\n    fibre tip to 15.9% of control.\n  source: Methods, Photoinhibition, paragraph 3; Extended Data Figure 2d\n  quote: Photoinhibition reduced activity (0.5-1.1 mm from the tip of the optical fiber) to 15.9 ± 9.3%\n  expected:\n    quantity: photoinhibition rate as a percentage of control\n    value: 15.9\n    tolerance: 9.3\n    unit: percent\n  criterion: Tolerance is the paper's stated spread (called SEM in the Methods; the legend of Extended\n    Data Fig. 2d calls its error bars standard deviations). Putative thalamic units recorded with the\n    optrode in VGAT-ChR2-EYFP mice, 0.5 to 1.1 mm from the fibre (Extended Data Fig. 2d, n = 34, 42,\n    38). Measure, windows W1 and W2, and readings as gad2-thalamus-reduction. Reproduced when within\n    tolerance under one reading.\n- id: muscimol-vmval-bias\n  statement: Small doses of muscimol infused near VM/VAL produced an ipsilateral bias in licking\n    responses, while infusions 0.3 to 0.8 mm anterior or 0.2 to 0.5 mm dorsal, even at ten-fold\n    higher doses, did not.\n  source: Results, Thalamus is required for motor preparation, paragraph 3; Extended Data Figure 3\n  quote: Inhibition near VM/VAL produced ipsilateral bias in the licking response ( Extended Data Fig.\n    3a, b ). Inhibition outside of thal ALM (1.1 - 1.6 mm anterior or 1.6-1.9 dorsal to VM/VAL) did not\n    cause ipsilateral bias, even at 10-fold higher doses\n  statistics:\n  - about: performance change near VM/VAL against control\n    test: Student's t-test\n    p: 0.05\n    p_relation: \"<\"\n    n: 6 infusion sites\n  criterion: Performance change is fraction correct over the 100 trials after infusion relative to the\n    100 trials before, separately for contra and ipsi trials, compared with the control condition\n    (buffer, or the pause without infusion) by Student's t-test (Methods, Behavioral data analysis;\n    Extended Data Fig. 3b). The legend does not say which side carries the star; reproduced when the\n    contra change near VM/VAL is lower than control at p < 0.05 and neither anterior (n = 4 sites) nor\n    dorsal (n = 4 sites) infusions differ from control in the ipsi direction at p < 0.05. Open, which\n    control: readings (a) buffer infusions, (b) pauses without infusion, (c) both pooled. The doses\n    differ between Results (1.8 to 5.9 ng) and the legend (1.5 to 5 ng); and the distances outside\n    VM/VAL differ between Results (1.1 to 1.6 mm anterior, 1.6 to 1.9 mm dorsal) and the legends (0.3\n    to 0.8 mm anterior, 0.2 to 0.5 mm dorsal of MD); sites are taken as the dataset labels them.\n- id: alm-unit-classes\n  statement: Of 1214 ALM units, 1006 were putative pyramidal neurons (spike width > 0.6 ms), 166 putative\n    fast-spiking (< 0.4 ms) and 42 unclassified; the spike-width distribution was bimodal.\n  source: Methods, Electrophysiology data analysis, paragraph 2; Extended Data Figure 4b\n  quote: In ALM, 1214 single units were recorded across 57 behavioral sessions. ... units with width <\n    0.4 ms were defined as putative fast-spiking (FS) neurons (166/1214) and units with width > 0.6 ms\n    as putative pyramidal neurons (1006/1214)\n  expected:\n  - quantity: ALM units\n    value: 1214\n    tolerance: 121\n  - quantity: putative pyramidal ALM units\n    value: 1006\n    tolerance: 101\n  - quantity: putative fast-spiking ALM units\n    value: 166\n    tolerance: 17\n  criterion: Spike width is the trough-to-peak interval of the mean waveform (Methods). Bimodality is\n    judged from the histogram, with the counts below 0.4 ms, between 0.4 and 0.6 ms, and above 0.6 ms\n    reported. Reproduced when the three counts are within tolerance.\n- id: fig2e-alm-selectivity\n  statement: Most ALM putative pyramidal neurons (70%, 704/1006) distinguished trial types; 145 had\n    preparatory activity only, 272 peri-movement selectivity only and 287 both.\n  source: Results, Preparatory activity in thalamus, paragraph 1; Figure 2e\n  quote: For a majority of neurons, activity differed across trial types (70%, 704/1006; P < 0.05, t\n    -test; Methods). ... subsets of neurons showed selective preparatory activity ( Fig. 2b , left\n    column; Fig. 2e , 145/1006), selective peri-movement activity during the response epoch ( Fig. 2b ,\n    right column; Fig. 2e , 272/1006), or both ( Fig. 2b , middle column; Fig. 2e , 287/1006)\n  depends_on:\n  - alm-unit-classes\n  expected:\n  - quantity: selective ALM pyramidal neurons\n    value: 704\n    tolerance: 70\n  - quantity: preparatory activity only\n    value: 145\n    tolerance: 15\n  - quantity: peri-movement selectivity only\n    value: 272\n    tolerance: 27\n  - quantity: both\n    value: 287\n    tolerance: 29\n  criterion: Putative pyramidal ALM units; control trials (no photoinhibition) only, as photoinhibition\n    trials change activity (the paper does not say; reading fixed as the only one consistent with\n    comparing to unperturbed activity, with all trials shown as a variant). Selectivity by convention\n    S, under response-epoch readings R1 and R2 and t-test readings (a) and (b). Reproduced when all four\n    counts are within tolerance under one reading.\n- id: fig2e-alm-contra-ipsi-balance\n  statement: Approximately equal numbers of selective ALM neurons preferred contra and ipsi movements.\n  source: Results, Preparatory activity in thalamus, paragraph 1; Figure 2e\n  quote: Approximately equal numbers of neurons preferred contra- or ipsi-lateral movements ( Fig. 2e )\n  depends_on:\n  - fig2e-alm-selectivity\n  criterion: Preference by total spike count over the three epochs (convention S), among the selective\n    neurons of fig2e-alm-selectivity. The paper gives no test or number. Readings (a) a two-sided\n    binomial test of the contra count against one half does not reject at p < 0.05; (b) the contra\n    fraction lies between 0.4 and 0.6. Reproduced when both readings hold, not reproduced when\n    neither holds, methods_underspecified when they differ. The counts are reported.\n- id: thalamus-unit-classes\n  statement: Of 790 thalamic units, 672 were putative thalamic neurons (spike width > 0.5 ms) and 313\n    lay within 0.4 mm of the VM/VAL centre; 295 VM/VAL units were analysed.\n  source: Methods, Electrophysiology data analysis, paragraph 3; Results, Preparatory activity in\n    thalamus, paragraph 2; Extended Data Figure 4e\n  quote: In thalamus, 790 single units were recorded across 73 behavioral sessions. ... Units with spike\n    width > 0.5 ms were selected as putative thalamic neurons (672/790) ... units within 0.4 mm from the\n    VM/VAL center ... were scored as VM/VAL neurons (313/790)\n  expected:\n  - quantity: thalamic units\n    value: 790\n    tolerance: 79\n  - quantity: putative thalamic neurons\n    value: 672\n    tolerance: 67\n  - quantity: units within 0.4 mm of the VM/VAL centre\n    value: 313\n    tolerance: 31\n  - quantity: VM/VAL putative thalamic neurons\n    value: 295\n    tolerance: 30\n  criterion: Width as for alm-unit-classes; location under readings L1 and L2. The 295 of the Results\n    are read as the units that pass both the width and the location rule (the paper does not say; a\n    reading, since 295 is below both 313 and 672). Reproduced when all four counts are within\n    tolerance under one location reading.\n- id: fig2f-vmval-selectivity\n  statement: A majority of VM/VAL neurons (69%, 204/295) distinguished trial types, a fraction\n    indistinguishable from ALM; 43 had preparatory activity only, 82 peri-movement selectivity only\n    and 79 both, a distribution similar to ALM.\n  source: Results, Preparatory activity in thalamus, paragraph 2; Figure 2f\n  quote: A majority of VM/VAL neurons discriminated trial types (69%, 204/295; indistinguishable from\n    ALM, chi-squared test, P = 0.79). ... VM/VAL neurons exhibited similar selectivity and time-course\n    to ALM (chi-squared test, P > 0.5)\n  statistics:\n  - about: fraction selective, VM/VAL against ALM\n    test: chi-squared test\n    p: 0.79\n    n: 295 VM/VAL and 1006 ALM neurons\n  - about: selectivity types, VM/VAL against ALM\n    test: chi-squared test\n    p: 0.5\n    p_relation: \">\"\n  depends_on:\n  - thalamus-unit-classes\n  - fig2e-alm-selectivity\n  expected:\n  - quantity: selective VM/VAL neurons\n    value: 204\n    tolerance: 20\n  - quantity: preparatory activity only\n    value: 43\n    tolerance: 4.3\n  - quantity: peri-movement selectivity only\n    value: 82\n    tolerance: 8.2\n  - quantity: both\n    value: 79\n    tolerance: 7.9\n  criterion: VM/VAL units of thalamus-unit-classes, selectivity as in fig2e-alm-selectivity, same\n    readings. Chi-squared tests (2 x 2 for selective against not; for the types, readings (i) 2 x 4\n    with non-selective as a class, (ii) 2 x 3 among selective neurons). Reproduced when the counts are\n    within tolerance under one reading and neither chi-squared test finds a difference at p < 0.05.\n- id: fig3-alm-collapse\n  statement: Strong photoinhibition of thalALM (VGAT-ChR2-EYFP) decreased ALM activity to 6% of control,\n    inhibiting 309 of 314 neurons (155 significantly) and significantly activating none.\n  source: Results, Thalamus drives ALM preparatory activity, paragraph 1; Figure 3c\n  quote: Thal ALM photoinhibition decreased ALM activity to 6% of control, reducing activity in nearly\n    all neurons ( Fig. 3c , 309/314 inhibited, 3/314 activated, 155/314 significantly inhibited, 0/314\n    significantly activated, t -test, P < 0.05)\n  depends_on:\n  - alm-unit-classes\n  expected:\n  - quantity: ALM activity during photoinhibition as a percentage of control\n    value: 6\n    tolerance: 0.6\n    unit: percent\n  - quantity: neurons analysed\n    value: 314\n    tolerance: 31\n  - quantity: neurons inhibited\n    value: 309\n    tolerance: 31\n  - quantity: neurons activated\n    value: 3\n    tolerance: 0.3\n  - quantity: neurons significantly inhibited\n    value: 155\n    tolerance: 16\n  - quantity: neurons significantly activated\n    value: 0\n    tolerance: 0\n  criterion: ALM putative pyramidal units recorded during ipsilateral thalamus photoinhibition in\n    VGAT-ChR2-EYFP mice, at least 5 photoinhibition trials; window, pooling and tests by convention P,\n    under readings T1, T2 and Q1 to Q3. Reproduced when all values are within tolerance under one\n    reading; partially reproduced when the percentage is at most 20% of control, more than 90% of\n    neurons are inhibited and none significantly activated, but some value is out of tolerance.\n- id: fig3d-all-layers\n  statement: Thalamus photoinhibition reduced ALM activity across all cortical layers.\n  source: Results, Thalamus drives ALM preparatory activity, paragraph 1; Figure 3d\n  quote: across all cortical layers ( Fig. 3d )\n  depends_on:\n  - fig3-alm-collapse\n  criterion: Unit depth as recorded (manipulator reading, Methods). The figure plots the number of\n    modulated neurons by depth; its bins are not given in the text, readings (a) 100 um, (b) 200 um.\n    Reproduced when, under both readings, every depth bin with at least 5 neurons from 0 to the\n    deepest recorded depth has a population rate in the window of convention P below control and holds\n    significantly inhibited neurons. The minimum of 5 neurons is a standard choice for a plotting bin.\n- id: fig3b-selectivity-types-equally-inhibited\n  statement: ALM neurons with preparatory activity, peri-movement selectivity or both were equally\n    inhibited by thalamus photoinhibition.\n  source: Results, Thalamus drives ALM preparatory activity, paragraph 1; Figure 3b\n  quote: neurons showing preparatory activity, peri-movement selectivity or both were equally inhibited;\n    Fig. 3b , P > 0.2, t -test\n  statistics:\n  - test: t-test\n    p: 0.2\n    p_relation: \">\"\n  depends_on:\n  - fig2e-alm-selectivity\n  - fig3-alm-collapse\n  criterion: A claim of absence, judged on the paper's test, two-sided t-tests between each pair of the\n    three groups (preparatory only, peri-movement only, both; convention S) of the neurons of\n    fig3-alm-collapse. The measure of inhibition is not named; readings (a) each neuron's rate under\n    photoinhibition over control, (b) the difference of rates, both in the window of convention P.\n    Reproduced when no pair differs at p < 0.05 under both measures; not reproduced when a pair does\n    under both; methods_underspecified when the measures disagree. Group means and the p-values are\n    reported, and whether they exceed 0.2.\n- id: fig3f-thalamus-silenced\n  statement: Strong photoinhibition in VGAT-ChR2-EYFP mice abolished thalALM activity nearly\n    completely, to 2% of control.\n  source: Results, Thalamus drives ALM preparatory activity, paragraph 1; Figure 3f\n  quote: Photoinhibition abolished thal ALM activity nearly completely (to 2 % of control without\n    photoinhibition) ( Fig. 3f )\n  expected:\n  - quantity: thalamic activity during photoinhibition as a percentage of control\n    value: 2\n    tolerance: 0.2\n    unit: percent\n  - quantity: thalamic neurons\n    value: 148\n    tolerance: 15\n  criterion: Thalamic units recorded during thalamus photoinhibition in VGAT-ChR2-EYFP mice (Fig. 3f,\n    n = 148). Which units are meant is open, readings (a) all putative thalamic units of those\n    recordings, (b) those in VM/VAL (convention L). Window and readings by convention P (the Methods\n    use 20 to 120 ms for Fig. 3). Reproduced when both values are within tolerance under one reading.\n- id: fig3-onset-latencies\n  statement: Photoinhibition reduced thalALM activity 2.5 ms after photostimulus onset, and ALM spike\n    rates were reduced 8.2 ms after onset, a latency difference consistent with direct thalamocortical\n    drive.\n  source: Results, Thalamus drives ALM preparatory activity, paragraph 3; Figure 3e, f\n  quote: Photoinhibition reduced thal ALM activity 2.5 ± 0.8 ms after photostimulus onset (mean ± SEM,\n    activity reduction onset detected by 3 × std, Fig. 3f ). Hyperpolarization of ALM neurons and\n    reduction of ALM spike rates were detected 7.9 ± 1.7 ms and 8.2 ± 1.5ms after photostimulus onset\n  depends_on:\n  - fig3-alm-collapse\n  - fig3f-thalamus-silenced\n  expected:\n  - quantity: onset of thalamic inhibition\n    value: 2.5\n    tolerance: 0.8\n    unit: ms\n  - quantity: onset of ALM spike-rate reduction\n    value: 8.2\n    tolerance: 1.5\n    unit: ms\n  criterion: Onsets by convention O (readings O1, O2) on the populations of fig3f-thalamus-silenced\n    (148) and fig3-alm-collapse (314), trial readings T1 and T2. Tolerances are the paper's SEMs.\n    Reproduced when both onsets are within tolerance under one reading and the ALM onset is later than\n    the thalamic one. The Vm onset (7.9 ms) is tested in wc-thalamus-hyperpolarization.\n- id: wc-near-threshold\n  statement: During the delay epoch the mean membrane potential of ALM neurons was close to spike\n    threshold, 12.7 mV below it on average.\n  source: Results, Thalamus drives ALM preparatory activity, paragraph 2\n  quote: the average membrane potential of ALM neurons was close to the spike threshold during the delay\n    epoch (action potential threshold - mean basal membrane potential = 12.7 ± 0.7 mV; mean ± SEM, n =\n    60 cells)\n  expected:\n  - quantity: threshold minus basal membrane potential\n    value: 12.7\n    tolerance: 0.7\n    unit: mV\n  - quantity: cells\n    value: 60\n    tolerance: 6\n  criterion: Whole-cell ALM recordings with more than 20 behavioural trials (Methods). Threshold is the\n    Vm at the kink of convention V; per cell, mean threshold minus mean basal Vm, then the mean over\n    cells. The basal Vm window differs between Results (\"during the delay epoch\") and Methods (0 to\n    0.5 s before trial onset); readings (a) the Methods window, (b) the delay epoch of control trials,\n    spikes clipped. Reproduced when the value is within tolerance under one reading. Tolerance is the\n    paper's SEM.\n- id: wc-thalamus-hyperpolarization\n  statement: Thalamus photoinhibition hyperpolarized ALM neurons by 18.7 mV, preventing spiking, with\n    an onset 7.9 ms after photostimulus onset.\n  source: Results, Thalamus drives ALM preparatory activity, paragraphs 2 and 3; Figure 3g, 4b, c\n  quote: Thal ALM photoinhibition caused hyperpolarization (Membrane potential, control trials\n    –photoinhibition trials, -18.7 ± 1.1 mV; measured for 100 ms, starting 20 ms after photostimulus\n    onset; mean ± SEM, n = 16 cells), preventing ALM neurons from spiking\n  expected:\n  - quantity: Vm change, photoinhibition minus control\n    value: -18.7\n    tolerance: 1.1\n    unit: mV\n  - quantity: onset of hyperpolarization\n    value: 7.9\n    tolerance: 1.7\n    unit: ms\n  criterion: Whole-cell ALM recordings during thalamus photoinhibition in behaving VGAT-ChR2-EYFP mice\n    (n = 16). Mean Vm (spikes clipped, convention V) 20 to 120 ms after photostimulus onset,\n    photoinhibition trials minus control trials, mean over cells. The text writes \"control trials\n    -photoinhibition trials\" with a negative value; the sign is read as hyperpolarization. Onset by\n    convention V, readings V1 and V2. Reproduced when both values are within tolerance (the paper's\n    SEMs) under one reading.\n- id: wc-loss-of-excitation\n  statement: The hyperpolarization of ALM neurons during thalamus photoinhibition was caused mainly by a\n    loss of excitation, not by an increase in inhibition; it was larger with negative current\n    injection.\n  source: Results, Thalamus drives ALM preparatory activity, paragraph 2; Extended Data Figure 5c-h\n  quote: Manipulating the membrane potential during recording revealed that hyperpolarization was mainly\n    caused by a reduction in excitation, not an increase in inhibition\n  statistics:\n  - about: slope of the regression of the Vm change on baseline Vm\n    test: bootstrap\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: Non-behaving Gad2-IRES-Cre mice with ChR2 in TRN (Extended Data Fig. 5c-h; n = 14 cells\n    without, 9 with negative and 6 with positive current injection). Per cell and current condition,\n    Vm in control and Vm change under photoinhibition, both 100 to 120 ms after light onset; cells\n    with positive and negative injection pooled (cells without injection left out, as the legend\n    does). Linear regression of the change on control Vm; p from a bootstrap of the slope. Resampling\n    unit is open, readings (a) cells, (b) cell-condition points; iterations 1000 or 10000 (Methods,\n    Statistics), a standard choice. Reproduced when the slope is positive with p < 0.0001 under one\n    reading, partially reproduced when positive with p < 0.05.\n- id: wc-m1-small-effect\n  statement: Photoinhibition of M1 during the delay epoch caused only a slight hyperpolarization (3.3\n    mV) and a small drop in spike rate (1.4 spikes per s) in ALM neurons.\n  source: Results, Thalamus drives ALM preparatory activity, paragraph 3; Figure 4d-f\n  quote: direct photoinhibition of M1 during the delay epoch ... caused only a slight hyperpolarization\n    of the membrane potential and spike rates of ALM neurons (-3.3 ± 1.0 mV; -1.4 ± 0.6 spikes per s;\n    mean ± SEM, n = 11 cells)\n  expected:\n  - quantity: Vm change\n    value: -3.3\n    tolerance: 1.0\n    unit: mV\n  - quantity: spike-rate change\n    value: -1.4\n    tolerance: 0.6\n    unit: spikes/s\n  criterion: Whole-cell ALM recordings during M1 photoinhibition (n = 11), as wc-thalamus-hyperpolarization,\n    window 20 to 120 ms after photostimulus onset (Fig. 4c legend, same format for f). Spike rate from\n    the spikes detected in the whole-cell trace. Reproduced when both values are within tolerance (the\n    paper's SEMs).\n- id: wc-contra-alm-small-effect\n  statement: Photoinhibition of contralateral ALM barely changed the membrane potential of ALM neurons\n    (1.4 mV).\n  source: Results, Thalamus drives ALM preparatory activity, paragraph 4; Figure 4g-i\n  quote: photoinhibiting contralateral ALM, the anatomically strongest input to ALM, barely changed\n    membrane potential (-1.4 ± 0.5 mV; mean ± SEM, n = 9 cells)\n  expected:\n    quantity: Vm change\n    value: -1.4\n    tolerance: 0.5\n    unit: mV\n  criterion: As wc-m1-small-effect, for contralateral ALM photoinhibition (n = 9).\n- id: thalamus-stronger-than-cortex\n  statement: thalALM drives ALM more strongly than M1 or contralateral ALM, the other reciprocally\n    connected structures tested.\n  source: Results, Thalamus drives ALM preparatory activity, paragraph 4; Figure 4b vs 4e, h\n  quote: Altogether thal ALM drives ALM directly and more strongly than other reciprocally connected\n    structures (cf. Fig. 4b vs Fig. 4e,h )\n  depends_on:\n  - wc-thalamus-hyperpolarization\n  - wc-m1-small-effect\n  - wc-contra-alm-small-effect\n  criterion: The paper reports no test. Reproduced when the mean Vm change under thalamus\n    photoinhibition is more negative than under M1 and under contralateral ALM photoinhibition, with\n    non-overlapping mean +/- 2 SEM (bootstrap SEMs, Methods); the SEM rule is a reading of the\n    paper's plotted SEMs, and the plain comparison of means is reported as well.\n- id: indirect-pathway-too-slow\n  statement: The latency of ALM hyperpolarization is too short for the thalamus to M1 to ALM pathway;\n    thalamus photoinhibition hyperpolarized M1 neurons after 11.0 ms and M1 photoinhibition\n    hyperpolarized ALM neurons after 13.9 ms, so that pathway would give a latency difference above 14.3\n    ms against the 5.4 ms observed.\n  source: Results, Thalamus drives ALM preparatory activity, paragraph 3; Extended Data Figure 6e-g\n  quote: The thalamus → M1 → ALM pathway would produce a latency difference of > 14.3 ms, too slow by >\n    9 ms to explain the hyperpolarization in ALM\n  depends_on:\n  - wc-thalamus-hyperpolarization\n  - fig3-onset-latencies\n  - fig6e-onset-latencies\n  expected:\n  - quantity: onset of M1 hyperpolarization after thalamus photoinhibition\n    value: 11.0\n    tolerance: 2.4\n    unit: ms\n  - quantity: onset of ALM hyperpolarization after M1 photoinhibition\n    value: 13.9\n    tolerance: 3.2\n    unit: ms\n  criterion: Onsets by convention V (readings V1, V2) for whole-cell M1 neurons during thalamus\n    photoinhibition (n = 9) and ALM neurons during M1 photoinhibition (n = 11), Extended Data Fig. 6e,\n    f; tolerances are the paper's SEMs. The pathway latency difference is (M1 onset minus thalamic\n    silencing onset) plus (ALM onset after M1 photoinhibition minus cortical silencing onset), as\n    Extended Data Fig. 6e, f compute it (8.5 + 5.8 = 14.3 ms). Reproduced when both onsets are within\n    tolerance under one reading and the pathway difference exceeds the direct one (ALM Vm onset minus\n    thalamic silencing onset).\n- id: conduction-delay\n  statement: Photoactivating thalamus in Olig3-cre x Ai32 mice depolarized ALM neurons after 3.6 ms, an\n    estimate of the thalamocortical conduction delay.\n  source: Extended Data Figure 6c\n  quote: The time between photostimulation onset and depolarization onset was 3.6 ± 1.1 ms ( n = 9\n    cells)\n  expected:\n    quantity: depolarization onset\n    value: 3.6\n    tolerance: 1.1\n    unit: ms\n  criterion: Whole-cell ALM recordings in non-behaving Olig3-cre x Ai32 mice during thalamus\n    photoactivation (10 mW), onset of depolarization by convention V (readings V1, V2) as the Methods\n    say (\"a similar procedure\"). Reproduced when within tolerance (the paper's SEM) under one reading.\n- id: latency-model-t3\n  statement: A model ALM neuron with 200 thalamic inputs predicts at least 1.8 ms between full loss of\n    thalamic input and a detectable change in membrane potential.\n  source: Results, Thalamus drives ALM preparatory activity, paragraph 3; Extended Data Figure 6d;\n    Supplementary information\n  quote: Even when 100% of the input neurons were inhibited, we expect to observe latency of 1.8 ± 0.7\n    ms\n  expected:\n    quantity: model latency, all inputs inhibited\n    value: 1.8\n    tolerance: 0.7\n    unit: ms\n  criterion: A simulation, not a test on recorded data; its parameters are in the Supplementary\n    information, which is not in the text read. Cannot be specified from the text; recorded so the\n    finding is covered.\n- id: fig5-weak-photoinhibition-rates\n  statement: Weak thalamus photoinhibition (20-fold weaker, 0.5 mW) significantly changed the spike rate\n    of 83 of 160 ALM neurons, with a mean reduction of 1.2 spikes per s; 39% of the changed neurons\n    (32/83) increased their rate.\n  source: Results, Thalamus contributes to selectivity in ALM, paragraph 1; Figure 5b\n  quote: 83 /160 of ALM neurons showed statistically significant changes in mean spike rate during\n    photoinhibition ( t -test; average reduction of spike rate, 1.2 ± 0.2 spikes per s, mean ± SEM, n =\n    160; Fig. 5a, b ). A substantial fraction of these neurons (39%, 32/83) showed increases in spike\n    rate\n  depends_on:\n  - alm-unit-classes\n  expected:\n  - quantity: neurons analysed\n    value: 160\n    tolerance: 16\n  - quantity: neurons with a significant change\n    value: 83\n    tolerance: 8.3\n  - quantity: mean reduction in spike rate\n    value: 1.2\n    tolerance: 0.2\n    unit: spikes/s\n  - quantity: significantly changed neurons that increased\n    value: 32\n    tolerance: 3.2\n  criterion: ALM putative pyramidal units recorded during weak thalamus photoinhibition (VGAT-ChR2-EYFP,\n    0.5 mW) with at least 25 photoinhibition trials. Rates over 1300 ms from photostimulus onset\n    (Fig. 5b legend), contra and ipsi trials pooled; trial readings T1, T2; significance by two-sided\n    t-test at P < 0.05 (convention P, t-test readings of convention S). Reproduced when all values are\n    within tolerance under one reading (the reduction's tolerance is the paper's SEM).\n- id: fig5c-selectivity-reduced\n  statement: Weak thalamus photoinhibition reduced the selectivity of ALM neurons, both contra- and\n    ipsi-preferring; the change in selectivity was anti-correlated with selectivity (slope -0.33,\n    r = -0.75), even in neurons without a change in mean rate.\n  source: Results, Thalamus contributes to selectivity in ALM, paragraph 1; Figure 5c; Extended Data\n    Figure 7a, b\n  quote: This unequal spike rate change reduced the selectivity of ALM neurons in both contra- and ipsi-\n    preferring neurons ( Fig. 5c, d and Extended Data Fig. 7a, b )\n  statistics:\n  - test: linear regression and Pearson correlation\n    statistic: slope = -0.33, r = -0.75\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - fig5-weak-photoinhibition-rates\n  expected:\n  - quantity: regression slope of selectivity change on selectivity\n    value: -0.33\n    tolerance: 0.033\n  - quantity: Pearson correlation\n    value: -0.75\n    tolerance: 0.075\n  - quantity: neurons above 2 spikes per s in both conditions\n    value: 73\n    tolerance: 7.3\n  criterion: The neurons of fig5-weak-photoinhibition-rates with rates above 2 spikes per s in control\n    and in photoinhibition (Methods, n = 73). Selectivity is contra minus ipsi rate (convention S) over\n    the 1300 ms window, in control; its change is photoinhibition selectivity minus control\n    selectivity; ordinary least squares of change on control selectivity. Trials, open, readings (a)\n    correct only in both conditions (Methods, selectivity), (b) correct only in control and all\n    outcomes under photoinhibition. Reproduced when slope and r are within tolerance under one reading.\n    The p recorded above is not printed in the paper for this panel; it stands for the regression being\n    a result and is recorded as p < 0.05 only as a marker. For Extended Data Fig. 7a, b (contra- and\n    ipsi-preferring defined by a delay-epoch t-test, P < 0.05), the mean absolute selectivity under\n    photoinhibition is lower than in control in each group; reported, and required for reproduced.\n- id: network-models\n  statement: The data are inconsistent with linear network models with specific or non-specific\n    thalamocortical connectivity, but do not exclude non-linear models of either kind.\n  source: Results, Thalamus contributes to selectivity in ALM, paragraph 2; Extended Data Figure 7c-e;\n    Supplementary information\n  quote: Our data are inconsistent with linear models with either specific (like-to-like) or\n    non-specific (all-to-all) thalamocortical connectivity. However, our data do not exclude non-linear\n    models\n  criterion: A modelling result; its equations and parameters are in the Supplementary information,\n    which is not in the text read. Cannot be specified from the text; recorded so the finding is\n    covered.\n- id: fig6c-vmval-reduced\n  statement: ALM photoinhibition decreased the activity of VM/VAL neurons to 25% of control, inhibiting\n    190 of 201 neurons (139 significantly) and significantly activating none.\n  source: Results, ALM drives thalamic preparatory activity, paragraph 1; Figure 6c\n  quote: ALM photoinhibition decreased activity in a majority of VM/VAL neurons (to 25% of control;\n    190/201 inhibited, 11/201 activated, 139/201 significantly inhibited, 0/201 significantly\n    activated, P < 0.05, t -test, Fig. 6c )\n  depends_on:\n  - thalamus-unit-classes\n  expected:\n  - quantity: VM/VAL activity during photoinhibition as a percentage of control\n    value: 25\n    tolerance: 2.5\n    unit: percent\n  - quantity: neurons analysed\n    value: 201\n    tolerance: 20\n  - quantity: neurons inhibited\n    value: 190\n    tolerance: 19\n  - quantity: neurons activated\n    value: 11\n    tolerance: 1.1\n  - quantity: neurons significantly inhibited\n    value: 139\n    tolerance: 14\n  - quantity: neurons significantly activated\n    value: 0\n    tolerance: 0\n  criterion: VM/VAL putative thalamic units (convention L) recorded during ipsilateral ALM\n    photoinhibition (PV-IRES-Cre x Ai32), at least 5 photoinhibition trials; window, pooling and tests\n    by convention P, readings T1, T2, Q1 to Q3 and L1, L2. Reproduced when all values are within\n    tolerance under one reading; partially reproduced when the percentage is at most 50%, more than 80%\n    of neurons are inhibited and none significantly activated, but some value is out of tolerance.\n- id: fig6b-selectivity-types-equally-inhibited\n  statement: VM/VAL neurons selective during the sample, delay or response epochs were equally inhibited\n    by ALM photoinhibition.\n  source: Results, ALM drives thalamic preparatory activity, paragraph 1; Figure 6b\n  quote: VM/VAL neurons selective during sample, delay or response epochs were equally inhibited ( Fig.\n    6b , P > 0.2, t -test)\n  statistics:\n  - test: t-test\n    p: 0.2\n    p_relation: \">\"\n  depends_on:\n  - fig6c-vmval-reduced\n  criterion: As fig3b-selectivity-types-equally-inhibited, on the neurons of fig6c-vmval-reduced. The\n    groups are open, readings (a) preparatory only, peri-movement only and both (convention S, as for\n    ALM); (b) selective in the sample, in the delay and in the response epoch (overlapping groups), as\n    the sentence reads. A claim of absence; reproduced when no pair differs at p < 0.05 under every\n    reading, not reproduced when a pair does under every reading, methods_underspecified otherwise.\n- id: fig6c-unmodulated-less-selective\n  statement: The few VM/VAL neurons not changed by ALM photoinhibition were significantly less selective\n    in the delay epoch, while neurons strongly reduced by it carried trial-type information.\n  source: Results, ALM drives thalamic preparatory activity, paragraph 1; Figure 6c bottom\n  quote: A small fraction of neurons in VM/VAL was not changed by ALM photoinhibition. These neurons also\n    showed significantly less selectivity ( Fig. 6c , P = 0.002, t -test)\n  statistics:\n  - about: delay selectivity, significantly against non-significantly modulated neurons\n    test: t-test\n    p: 0.002\n  - about: change of spike rate against delay selectivity\n    test: linear regression and Pearson correlation\n    statistic: slope = -0.73, r = -0.33\n    p: 0.002\n  depends_on:\n  - fig6c-vmval-reduced\n  expected:\n  - quantity: regression slope\n    value: -0.73\n    tolerance: 0.073\n  - quantity: Pearson correlation\n    value: -0.33\n    tolerance: 0.033\n  criterion: Neurons of fig6c-vmval-reduced, split by the significance of their change (convention P).\n    Delay-epoch selectivity on correct control trials; its form is open, readings (a) absolute\n    contra minus ipsi rate, (b) preferred minus non-preferred rate, preference by total count over the\n    three epochs (convention S). Two-sided t-test of delay selectivity, significantly against not\n    significantly modulated. Regression of selectivity on rate change (photoinhibition minus control,\n    convention P window); the axis order is open, readings (i) selectivity on change, (ii) change on\n    selectivity. Reproduced when, under one reading, the unmodulated group is less selective at p <\n    0.05 and the correlation is negative; the slope and r are compared with tolerance and reported.\n    The second statistics entry records only the figure's statistic; its p is the inset's and is\n    repeated for the schema, not a value for the regression.\n- id: fig6d-localized\n  statement: The reduction of thalamic activity by ALM photoinhibition was mainly limited to VM/VAL;\n    neurons within 1.0 mm of the VM/VAL centre were inhibited to 36% of control, and neurons farther\n    away less.\n  source: Results, ALM drives thalamic preparatory activity, paragraph 1; Methods, Electrophysiology\n    data analysis, paragraph 3; Figure 6d; Extended Data Figure 8b, c\n  quote: neurons within 1.0 mm from VM/VAL center showed robust inhibition (to 36% of control activity\n    during the first 100 ms inhibition\n  depends_on:\n  - thalamus-unit-classes\n  expected:\n  - quantity: activity within 1.0 mm of the VM/VAL centre as a percentage of control\n    value: 36\n    tolerance: 3.6\n    unit: percent\n  - quantity: neurons below 0.5 mm\n    value: 250\n    tolerance: 25\n  - quantity: neurons 0.5 to 1.0 mm\n    value: 160\n    tolerance: 16\n  - quantity: neurons at 1.0 mm or more\n    value: 46\n    tolerance: 4.6\n  criterion: Putative thalamic units recorded during ALM photoinhibition, at least 5 photoinhibition\n    trials, grouped by distance from the VM/VAL centre (Extended Data Fig. 8b; convention L, reading L2,\n    or the dataset's coordinates with any centre it documents). Ratio and trials by convention P.\n    Reproduced when the within-1.0 mm value and the group counts are within tolerance under one\n    reading and the ratio is lower below 0.5 mm than at 1.0 mm or more.\n- id: vm1-photoinhibition-no-effect\n  statement: Photoinhibiting vibrissal M1 did not reduce thalALM activity, unlike ALM photoinhibition in\n    the same neurons.\n  source: Results, ALM drives thalamic preparatory activity, paragraph 2; Extended Data Figure 8f, g\n  quote: photoinhibiting the nearby vibrissal primary motor cortex (vM1), which projects to parts of\n    VA/VL, did not cause a reduction in thal ALM activity ( Extended Data Fig. 8d-g )\n  criterion: VM/VAL units recorded with interleaved ALM and vM1 photoinhibition (Extended Data Fig. 8f,\n    g; n = 46 cells, 3 mice). The paper reports no test; legend says vM1 photoinhibition \"produced less\n    reduction\". Window and ratio by convention P. Reproduced when the population rate under vM1\n    photoinhibition is closer to control than under ALM photoinhibition, by a paired two-sided t-test\n    over neurons on the ratios at p < 0.05, and the vM1 ratio is above 0.75; the 0.75 is a reading of\n    \"did not cause a reduction\" (the paper gives no number), and the ratio is reported.\n- id: fig6e-onset-latencies\n  statement: After ALM photoinhibition onset, ALM pyramidal neurons were silenced after 8.1 ms and VM/VAL\n    activity reduced after 10.9 ms; SNr neurons changed later, after 15.2 ms.\n  source: Figure 6e; Extended Data Figure 6f; Extended Data Figure 10d\n  quote: SNr neurons were affected by ALM photoinhibition with a relatively long latency difference\n    (15.2 ± 4.6 ms, mean ± SEM, P < 0.05, t -test), longer than for reducing thal ALM activity (10.9 ±\n    2.9 ms; Fig. 6e )\n  statistics:\n  - about: SNr against VM/VAL latency\n    test: t-test\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - fig6c-vmval-reduced\n  - snr-photoinhibition\n  expected:\n  - quantity: ALM silencing onset\n    value: 8.1\n    tolerance: 1.2\n    unit: ms\n  - quantity: VM/VAL reduction onset\n    value: 10.9\n    tolerance: 2.9\n    unit: ms\n  - quantity: SNr change onset\n    value: 15.2\n    tolerance: 4.6\n    unit: ms\n  criterion: Onsets by convention O (O1, O2) for ALM putative pyramidal neurons during ALM\n    photoinhibition (n = 256), VM/VAL neurons (n = 201) and the significantly modulated SNr neurons\n    (Extended Data Fig. 10d, 48 inhibited; whether the 23 activated enter, with sign flipped, is open,\n    readings (a) inhibited only, (b) both). Tolerances are the paper's SEMs. The t-test of SNr against\n    VM/VAL onsets is run on the bootstrap distributions (the paper does not say on what; a reading).\n    Reproduced when the three onsets are within tolerance under one reading and SNr is latest.\n- id: snr-photoinhibition\n  statement: ALM photoinhibition changed only a small fraction of SNr GABAergic neurons (48/181\n    significantly inhibited, 23/181 activated), more decreasing than increasing, and reduced SNr\n    activity overall by 3.6 spikes per s (8.3%), which argues against SNr mediating the thalamic\n    reduction.\n  source: Results, ALM drives thalamic preparatory activity, paragraph 2; Extended Data Figure 10c\n  quote: Photoinhibition of ALM changed only a relatively small fraction of SNr neurons (48/181\n    significantly inhibited; 23/181 significantly activated, P < 0.05, t -test,). Moreover, neurons that\n    decreased their activity were more numerous than neurons that increased their activity\n    (bootstrapping over neurons, P < 0.01, Methods). Overall, inhibiting ALM reduced SNr activity by 3.6\n    spikes per second (8.3% of control activity\n  statistics:\n  - about: more down-modulated than up-modulated neurons\n    test: bootstrapping over neurons\n    p: 0.01\n    p_relation: \"<\"\n    n: 181 putative GABAergic SNr neurons\n  expected:\n  - quantity: SNr units\n    value: 227\n    tolerance: 23\n  - quantity: putative GABAergic SNr neurons\n    value: 181\n    tolerance: 18\n  - quantity: significantly inhibited\n    value: 48\n    tolerance: 4.8\n  - quantity: significantly activated\n    value: 23\n    tolerance: 2.3\n  - quantity: reduction of SNr activity\n    value: 3.6\n    tolerance: 0.36\n    unit: spikes/s\n  - quantity: reduction as a percentage of control\n    value: 8.3\n    tolerance: 0.83\n    unit: percent\n  criterion: SNr units with trough-to-peak width below 0.45 ms (Methods); window and tests by convention\n    P (readings T1, T2), all such units (n = 181; the minimum of 5 photoinhibition trials is not stated\n    for SNr, readings (a) none, (b) 5). Bootstrap as the Methods describe, resampling neurons with\n    replacement, 1000 or 10000 rounds, p the fraction of rounds with up-modulated at least as many as\n    down-modulated. Reproduced when the values are within tolerance under one reading and p < 0.01.\n- id: snr-unit-properties\n  statement: Putative GABAergic SNr neurons had high spike rates (40.9 spikes per s) compared with the\n    other SNr units (23.4), and most of them (152/181) were selective for trial type, like ALM and\n    VM/VAL.\n  source: Methods, Electrophysiology data analysis, paragraph 4; Extended Data Figure 4j, 10b\n  quote: These units have high spike rates (40.9 ± 21.5, mean ± SD, n = 181). For comparison, neurons\n    with longer spike widths have lower spikes rates (23.4 ± 17.0, mean ± SD, n = 46)\n  depends_on:\n  - snr-photoinhibition\n  expected:\n  - quantity: mean rate of putative GABAergic SNr neurons\n    value: 40.9\n    tolerance: 4.09\n    unit: spikes/s\n  - quantity: mean rate of other SNr units\n    value: 23.4\n    tolerance: 2.34\n    unit: spikes/s\n  - quantity: selective putative GABAergic SNr neurons\n    value: 152\n    tolerance: 15\n  criterion: Mean rate per unit over the session (the window is not given; readings (a) whole session,\n    (b) all trials from trial start to end), then mean over units. Selectivity by convention S\n    (readings R1, R2). Tolerances are 10% of the values, as the stated SDs describe spread over units,\n    not uncertainty of the mean. Reproduced when all values are within tolerance under one reading.\n- id: anatomy-reciprocal-thalamus\n  statement: ALM is reciprocally connected with ipsilateral thalamic nuclei, most consistently the\n    VM/VAL complex; a retrograde injection into ALM labelled 17375 thalamic neurons, against 38062 in\n    contralateral ALM and 26599 in M1.\n  source: Results, Thalamus is required for motor preparation, paragraph 2; Extended Data Figure 1d, f\n  quote: Within thal ALM , the VM/VAL complex was most extensively and consistently labeled in\n    experiments involving injections of multiple types of anterograde and retrograde tracers into ALM\n  expected:\n  - quantity: retrogradely labelled thalamic neurons\n    value: 17375\n    tolerance: 1738\n  - quantity: retrogradely labelled contralateral ALM neurons\n    value: 38062\n    tolerance: 3806\n  - quantity: retrogradely labelled M1 neurons\n    value: 26599\n    tolerance: 2660\n  criterion: Histology (tracer injections, cell counts registered to the Allen CCF). The dataset is\n    described as electrophysiology, behaviour and optogenetics; whether it holds these images is for\n    the author to find.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Fixing a few criteria where I set thresholds myself, and removing two statistics entries that the paper does not report.

**Agent calls Bash**

```bash
cd claims/000009 && python3 - <<'EOF'
p='10.1038-nature22324.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:60]
    s=s.replace(a,b)
rep("""  statistics:
  - test: linear regression and Pearson correlation
    statistic: slope = -0.33, r = -0.75
    p: 0.05
    p_relation: "<"
  depends_on:
  - fig5-weak-photoinhibition-rates""","""  depends_on:
  - fig5-weak-photoinhibition-rates""")
rep("""    The p recorded above is not printed in the paper for this panel; it stands for the regression being
    a result and is recorded as p < 0.05 only as a marker. For""","""    The paper gives no p-value for this regression. For""")
rep("""  - about: change of spike rate against delay selectivity
    test: linear regression and Pearson correlation
    statistic: slope = -0.73, r = -0.33
    p: 0.002
""","")
rep("""    The second statistics entry records only the figure's statistic; its p is the inset's and is
    repeated for the schema, not a value for the regression.
""","""    The paper gives no p-value for the regression.
""")
rep("""  criterion: Putative pyramidal ALM units; control trials (no photoinhibition) only, as photoinhibition
    trials change activity (the paper does not say; reading fixed as the only one consistent with
    comparing to unperturbed activity, with all trials shown as a variant). Selectivity""","""  criterion: Putative pyramidal ALM units. Whether photoinhibition trials enter is not said; readings
    (a) control trials only, (b) all trials. Selectivity""")
rep("""neurons of fig2e-alm-selectivity. The paper gives no test or number. Readings (a) a two-sided
    binomial test of the contra count against one half does not reject at p < 0.05; (b) the contra
    fraction lies between 0.4 and 0.6. Reproduced when both readings hold, not reproduced when
    neither holds, methods_underspecified when they differ. The counts are reported.""","""neurons of fig2e-alm-selectivity. The paper gives no test or number; "approximately equal" is
    read as no detectable imbalance, by a two-sided binomial test of the contra count against one
    half, the only reading the text suggests. Reproduced when it does not reject at p < 0.05, not
    reproduced when it does. The counts and the contra fraction are reported, under each reading of
    fig2e-alm-selectivity.""")
rep("""reading; partially reproduced when the percentage is at most 20% of control, more than 90% of
    neurons are inhibited and none significantly activated, but some value is out of tolerance.""","""reading; partially reproduced when, under every reading, activity falls, inhibited neurons
    outnumber activated ones and none is significantly activated, but some value is out of tolerance.""")
rep("""tolerance under one reading; partially reproduced when the percentage is at most 50%, more than 80%
    of neurons are inhibited and none significantly activated, but some value is out of tolerance.""","""tolerance under one reading; partially reproduced when, under every reading, activity falls,
    inhibited neurons outnumber activated ones and none is significantly activated, but some value is
    out of tolerance.""")
rep("""  criterion: The paper reports no test. Reproduced when the mean Vm change under thalamus
    photoinhibition is more negative than under M1 and under contralateral ALM photoinhibition, with
    non-overlapping mean +/- 2 SEM (bootstrap SEMs, Methods); the SEM rule is a reading of the
    paper's plotted SEMs, and the plain comparison of means is reported as well.""","""  criterion: The paper reports no test for this comparison ("cf." the figure panels). Readings (a)
    the mean Vm change (20 to 120 ms) under thalamus photoinhibition is more negative than under M1
    and under contralateral ALM photoinhibition; (b) as (a), with each difference significant by a
    two-sided t-test over cells at p < 0.05, the test the paper uses elsewhere. Reproduced when both
    readings hold, not reproduced when neither does, methods_underspecified when they differ.""")
rep("""g; n = 46 cells, 3 mice). The paper reports no test; legend says vM1 photoinhibition "produced less
    reduction". Window and ratio by convention P. Reproduced when the population rate under vM1
    photoinhibition is closer to control than under ALM photoinhibition, by a paired two-sided t-test
    over neurons on the ratios at p < 0.05, and the vM1 ratio is above 0.75; the 0.75 is a reading of
    "did not cause a reduction" (the paper gives no number), and the ratio is reported.""","""g; n = 46 cells, 3 mice). A claim of absence. The paper names no test for it; the test it uses for
    every photoinhibition effect is the two-sided t-test (convention P), applied here to the
    population, paired over neurons, rates under vM1 photoinhibition against control in the window
    of convention P. Reproduced when it finds no reduction at p < 0.05, not reproduced when it does.
    The ratios under vM1 and ALM photoinhibition (Q1 to Q3) are reported either way.""")
rep("""readings (a) inhibited only, (b) both). Tolerances are the paper's SEMs. The t-test of SNr against
    VM/VAL onsets is run on the bootstrap distributions (the paper does not say on what; a reading).
    Reproduced""","""readings (a) inhibited only, (b) both). Tolerances are the paper's SEMs. The paper does not say
    what its t-test of SNr against VM/VAL onsets compares; the onsets and their bootstrap SEMs are
    reported and the outcome does not rest on that test. Reproduced""")
rep("""    say nothing for the scatter plots""","""    say nothing for the scatter plots""")
rep("""    contra change near VM/VAL is lower than control at p < 0.05 and neither anterior (n = 4 sites) nor
    dorsal (n = 4 sites) infusions differ from control in the ipsi direction at p < 0.05.""","""    contra change near VM/VAL is lower than control at p < 0.05, and neither anterior (n = 4 sites) nor
    dorsal (n = 4 sites) infusions lower contra performance against control at p < 0.05.""")
open(p,'w').write(s)
EOF
grep -n -i "rather\|—" 10.1038-nature22324.yaml; cd ../.. && python tools/claims_check.py claims/000009/10.1038-nature22324.yaml paper/10.1038-nature22324.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/000009 && python3 - <<'EOF'
p='10.1038-nature22324.yaml'
s=open(p).read()
s=s.replace("Open, which\n    control: readings","Open, which\n    control, readings")
open(p,'w').write(s)
EOF
python3 -c "
import yaml,re
lines=open('10.1038-nature22324.yaml').read()
yaml.safe_load(lines)
for i,l in enumerate(lines.splitlines(),1):
    if not l.lstrip().startswith('#') and re.search(r'\S: ', l.split(': ',1)[1] if re.match(r'\s*-? ?[a-z_]+: ',l) else l): print(i,l)
"
```

```
(Bash completed with no output)
```

**Agent**

Now rerunning the edits that were lost because of the failed assertion.

**Agent calls Bash**

```bash
grep -c "only as a marker\|non-overlapping\|0.75; the 0.75\|between 0.4 and 0.6" 10.1038-nature22324.yaml
```

```
5
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='10.1038-nature22324.yaml'
s=open(p).read()
def rep(a,b):
    global s
    assert s.count(a)==1, a[:70]
    s=s.replace(a,b)
rep("""  statistics:
  - test: linear regression and Pearson correlation
    statistic: slope = -0.33, r = -0.75
    p: 0.05
    p_relation: "<"
  depends_on:
  - fig5-weak-photoinhibition-rates""","""  depends_on:
  - fig5-weak-photoinhibition-rates""")
rep("""    The p recorded above is not printed in the paper for this panel; it stands for the regression being
    a result and is recorded as p < 0.05 only as a marker. For""","""    The paper gives no p-value for this regression. For""")
rep("""  - about: change of spike rate against delay selectivity
    test: linear regression and Pearson correlation
    statistic: slope = -0.73, r = -0.33
    p: 0.002
""","")
rep("""    The second statistics entry records only the figure's statistic; its p is the inset's and is
    repeated for the schema, not a value for the regression.
""","""    The paper gives no p-value for the regression.
""")
rep("""  criterion: Putative pyramidal ALM units; control trials (no photoinhibition) only, as photoinhibition
    trials change activity (the paper does not say; reading fixed as the only one consistent with
    comparing to unperturbed activity, with all trials shown as a variant). Selectivity""","""  criterion: Putative pyramidal ALM units. Whether photoinhibition trials enter is not said; readings
    (a) control trials only, (b) all trials. Selectivity""")
rep("""neurons of fig2e-alm-selectivity. The paper gives no test or number. Readings (a) a two-sided
    binomial test of the contra count against one half does not reject at p < 0.05; (b) the contra
    fraction lies between 0.4 and 0.6. Reproduced when both readings hold, not reproduced when
    neither holds, methods_underspecified when they differ. The counts are reported.""","""neurons of fig2e-alm-selectivity. The paper gives no test or number; "approximately equal" is
    read as no detectable imbalance, by a two-sided binomial test of the contra count against one
    half, the only reading the text suggests. Reproduced when it does not reject at p < 0.05, not
    reproduced when it does. The counts and the contra fraction are reported, under each reading of
    fig2e-alm-selectivity.""")
rep("""reading; partially reproduced when the percentage is at most 20% of control, more than 90% of
    neurons are inhibited and none significantly activated, but some value is out of tolerance.""","""reading; partially reproduced when, under every reading, activity falls, inhibited neurons
    outnumber activated ones and none is significantly activated, but some value is out of tolerance.""")
rep("""tolerance under one reading; partially reproduced when the percentage is at most 50%, more than 80%
    of neurons are inhibited and none significantly activated, but some value is out of tolerance.""","""tolerance under one reading; partially reproduced when, under every reading, activity falls,
    inhibited neurons outnumber activated ones and none is significantly activated, but some value is
    out of tolerance.""")
rep("""  criterion: The paper reports no test. Reproduced when the mean Vm change under thalamus
    photoinhibition is more negative than under M1 and under contralateral ALM photoinhibition, with
    non-overlapping mean +/- 2 SEM (bootstrap SEMs, Methods); the SEM rule is a reading of the
    paper's plotted SEMs, and the plain comparison of means is reported as well.""","""  criterion: The paper reports no test for this comparison ("cf." the figure panels). Readings (a)
    the mean Vm change (20 to 120 ms) under thalamus photoinhibition is more negative than under M1
    and under contralateral ALM photoinhibition; (b) as (a), with each difference significant by a
    two-sided t-test over cells at p < 0.05, the test the paper uses elsewhere. Reproduced when both
    readings hold, not reproduced when neither does, methods_underspecified when they differ.""")
rep("""g; n = 46 cells, 3 mice). The paper reports no test; legend says vM1 photoinhibition "produced less
    reduction". Window and ratio by convention P. Reproduced when the population rate under vM1
    photoinhibition is closer to control than under ALM photoinhibition, by a paired two-sided t-test
    over neurons on the ratios at p < 0.05, and the vM1 ratio is above 0.75; the 0.75 is a reading of
    "did not cause a reduction" (the paper gives no number), and the ratio is reported.""","""g; n = 46 cells, 3 mice). A claim of absence. The paper names no test for it; the test it uses for
    every photoinhibition effect is the two-sided t-test (convention P), applied here to the
    population, paired over neurons, rates under vM1 photoinhibition against control in the window
    of convention P. Reproduced when it finds no reduction at p < 0.05, not reproduced when it does.
    The ratios under vM1 and ALM photoinhibition (Q1 to Q3) are reported either way.""")
rep("""readings (a) inhibited only, (b) both). Tolerances are the paper's SEMs. The t-test of SNr against
    VM/VAL onsets is run on the bootstrap distributions (the paper does not say on what; a reading).
    Reproduced""","""readings (a) inhibited only, (b) both). Tolerances are the paper's SEMs. The paper does not say
    what its t-test of SNr against VM/VAL onsets compares; the onsets and their bootstrap SEMs are
    reported and the outcome does not rest on that test. Reproduced""")
rep("""    contra change near VM/VAL is lower than control at p < 0.05 and neither anterior (n = 4 sites) nor
    dorsal (n = 4 sites) infusions differ from control in the ipsi direction at p < 0.05.""","""    contra change near VM/VAL is lower than control at p < 0.05, and neither anterior (n = 4 sites) nor
    dorsal (n = 4 sites) infusions lower contra performance against control at p < 0.05.""")
open(p,'w').write(s)
EOF
grep -n -i "rather\|—" 10.1038-nature22324.yaml; cd ../.. && python tools/claims_check.py claims/000009/10.1038-nature22324.yaml paper/10.1038-nature22324.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
import yaml;d=yaml.safe_load(open('claims/000009/10.1038-nature22324.yaml'))
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"; git status --short
```

```
37 10 11 37 26
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
?? claims/000009/
?? scripts
```

**Agent**

I wrote `claims/000009/10.1038-nature22324.yaml`, and the quote checker passes it with no problems.

**What I read.** The HHMI author manuscript in PMC (PMC6431254), as served by Europe PMC. It has the main text, Methods, and the legends of Figures 1 to 6 and Extended Data Figures 1 to 10. It is the accepted manuscript, not the version of record. There is no PDF, so I could not open any figure. The paper links no analysis code, only the CRCNS deposit (doi:10.6080/K03F4MH2), so there was no code to read. From the dataset I looked only at its DANDI title and description, and the summary of what it holds.

**Missing from the paper text.** The Supplementary Information and Supplementary Tables 1 and 2 (animals, coordinates, light powers, viruses) are not there. Following earlier files in the registry, I went ahead instead of stopping. Two claims depend on the Supplementary Information and cannot be specified from the text: `latency-model-t3` (a model latency of 1.8 ms) and `network-models` (linear against non-linear models). Their criteria say so. No other claim needs the supplement.

**Counts.** 37 claims, all 37 with quotes. 10 claims carry statistics, 11 entries in all. 37 have criteria and 26 have expected values. The claims cover behaviour, unit classes, selectivity in ALM and VM/VAL, strong and weak thalamus photoinhibition, whole-cell recordings, onset latencies, ALM photoinhibition of VM/VAL, the vM1 and SNr controls, and anatomy.

**Details the paper leaves open, and the readings named.** Shared conventions sit in the opening comment; claim-specific ones are in the criteria.
- **Response epoch length:** (R1) 1.3 s after the go cue, or (R2) 1.5 s, the response window.
- **t-test variance:** Student's or Welch's.
- **Trials in photoinhibition rates:** (T1) correct and incorrect, or (T2) correct only.
- **"To X% of control":** (Q1) ratio of population means, (Q2) mean of per-unit ratios, or (Q3) median of per-unit ratios.
- **Spike-onset baseline:** (O1) the control PSTH in the same bin, or (O2) the mean control rate over the delay epoch.
- **Membrane-potential onset:** (V1) onset of the mean trace across cells, or (V2) mean of per-cell onsets.
- **VM/VAL centre:** the text gives no coordinate. (L1) the dataset's own location label, or (L2) 0.4 mm around AP -1.5, ML 0.85, DV 4.0 mm, the tracer injection site "mainly in VM" (Extended Data Fig. 9).
- **Gad2 reduction window:** the whole photostimulus, or 20 to 120 ms after onset.
- **Distance from threshold to resting potential:** the resting window is 0 to 0.5 s before the trial in the Methods but "during the delay epoch" in the Results; both are named.
- **Fig. 5c trials:** correct trials only, or all outcomes under photoinhibition.
- **Fig. 6c selectivity:** absolute contra minus ipsi, or preferred minus non-preferred; and which axis the regression is fitted on.
- **Selectivity groups in Fig. 6b:** by type (preparatory, peri-movement, both), or by epoch.
- **Inhibition measure for "equally inhibited":** ratio or difference of rates.
- **Behaviour rates:** pooled over trials, averaged over sessions, or control trials only.
- **Selectivity counts:** whether photoinhibition trials enter.
- **Muscimol control:** buffer infusions, pauses without infusion, or both.
- **SNr:** whether the 5-trial minimum applies; whether activated neurons enter the onset estimate.
- **Bootstrap resampling unit** in Extended Data Fig. 5g: cells or cell-condition points.
- **Fig. 3d depth bins:** 100 µm or 200 µm.

**Choices with no basis in the paper, for the second reader to check.** Where the paper gives no test or threshold, I set one myself:
- **Comparisons with no test given:** "approximately equal" contra and ipsi preference is judged by a binomial test. The vM1 absence and the thalamus-stronger-than-cortex comparison use the paper's t-test, which it never applies to them.
- **Thresholds I set:** a minimum of 5 neurons per depth bin. Partial-reproduction bands for fig1c, fig3, fig6c, wc-loss-of-excitation and fig2f-vmval-selectivity.
- **Fixed readings:** the 295 VM/VAL units are read as passing both the spike-width and the location rule.

**Inconsistencies inside the paper.**
- Muscimol doses differ: 1.8 to 5.9 ng in the Results, 1.5 to 5 ng in the Extended Data Fig. 3b legend.
- The distances of the control infusion sites differ between the Results and the legends.
- The 15.9 ± 9.3% spread is called SEM in the Methods but standard deviation in the Extended Data Fig. 2d legend.
- The −18.7 mV is written as "control − photoinhibition" but given a negative sign.
- VM/VAL counts differ: 313 in the Methods, 295 in the Results.
- Extended Data Fig. 3b does not say which side, contra or ipsi, carries the significance star.

I made no commits.

## End of run

22 turns, 6 minutes, result: success.
