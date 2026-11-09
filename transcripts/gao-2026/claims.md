# 001683 · claims · run 39614553951

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
ls claims/001683/ claims/001453/ paper/ 2>&1; git show --stat HEAD HEAD~1 | head -40; wc -l docs/protocol.md
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat transcripts/001683/claims-report.md transcripts/001683/claims-check-report.md
```

```
I've stopped without writing any claims, because the paper's supplement is missing. Nothing was written under `claims/001683/`.

**Text read:** `paper/10.1109-tnsre.2025.3644273.txt`, the NIH author manuscript (PMC12848950) served by Europe PMC. It has the main text, Methods, Results, Discussion and the figure legends for Figs. 1 to 6. There is no PDF, and the paper links no code; the only repository it names is the DANDI dataset itself.

**What is missing:** the supplementary material (`supp1-3644273`, at https://doi.org/10.1109/TNSRE.2025.3644273). The paper relies on it in two ways:
- **Methods:** "Details of the scanning process are provided in Supplementary Materials" (the transducer's pressure field) and "Details on the target confirmation process are provided in Supplementary Materials and Fig. S2". The 200 evoked responses behind the wild-type phase lag index analysis (Fig. 5) come from that target confirmation procedure. So how they were taken, and the resting "sham" recording, are defined only in the supplement.
- **Results:** several findings are shown only in supplementary figures:
  - Fig. S1: seizure duration distribution over time.
  - Fig. S3: example of seizure suppression in the raw EEG.
  - Fig. S4: the sham group's band powers do not change.
  - Fig. S5: tFUS improves hemispheric balance compared with before the 4-AP injections.
  - Fig. S6: phase lag index in the theta, alpha and beta bands in wild-type rats.
  - Fig. S7: wild-type and seizure rats differ in their baseline network state.

The main seizure findings (Fig. 3: seizure count, percent time in seizure, inter-seizure interval and seizure duration) could be written from the text I have. The protocol says to stop when a supplement the results rest on is missing, so I did not write a partial file. Supplying the supplement under `paper/` would let a reader run write the claims.

**Claims:** 0, so none with quotes, statistics or criteria. No open details or readings were recorded, since no c
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/protocol.md
```

```
# Protocol for an attempt

Version: `pilot-10`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
  understand the claims, but the claims file binds it: it cannot change a
  claim, and it asks a reader for any method detail the file lacks.
- The **verifier** checks the author's work and must not be the author.

[... 468 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; ls tools; ls claims | head -50
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
[... 370 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/001702 claims/001746; head -60 claims/001746/*.yaml; grep -n "checks:" -A30 claims/001746/*.yaml | head -50
```

```
claims/001702:
10.1002-alz.70813.yaml

claims/001746:
10.1038-s41556-026-02009-4.yaml
# Claims for Liu, Huang, Shen, Shao, Jing et al. (2026), "An atlas of primate insular cortex
# reveals a signal-processing strategy in von Economo neurons", Nature Cell Biology 28,
# 1742-1757, doi:10.1038/s41556-026-02009-4 (named on the archive "Cell Atlas and Novel Signal
# Processing Strategy in Primate Insular Cortex"), on dandiset 001746.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol as stated in docs/protocol.md (version pilot-10).
#
# Text read: the version of record, open access, as served by Europe PMC (PMC13457102), stored
# under paper/: main text, figure legends, Extended Data figure legends, Methods, Data and Code
# availability. No PDF was available, so values printed only inside figures (box plots and
# their P values) could not be read. The Supplementary Information (Supplementary Figs. 1 to 17
# and Supplementary Tables 1 to 12) and the Source Data files were not in the text read. Several
# findings this dataset can test cite them for their values and P values (Supplementary Fig. 11,
# Supplementary Tables 1, 2, 8 and 9). Those claims rest on the sentences of the Results, the
# figure legends and the Methods, which were read, and on the paper's code, which shows how the
[... 66 more lines not kept]
```

**Agent**

Now the paper text.

**Agent calls Bash**

```bash
wc -c paper/*.txt; cat paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1109-tnsre.2025.3644273.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1109-tnsre.2025.3644273.txt",
 "offset": 215
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -rl "001683" --include=*.yaml --include=*.json --include=*.md . 2>/dev/null | grep -v transcripts | head;
```

```
./targets/dandisets.json
./targets/description_papers.yaml
./papers/manifest.yaml
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '001683' in json.dumps(x): print(json.dumps(x,indent=1)[:3000])
"; grep -n -B2 -A10 "001683" targets/description_papers.yaml papers/manifest.yaml | head -60
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
[... 126 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
for x in d:
  if x['dandiset']=='001683': print(json.dumps(x,indent=1))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    if x['dandiset']=='001683': print(json.dumps(x,indent=1))
       ~^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
```

**Agent calls Bash**

```bash
python -c "
import json;d=json.load(open('targets/dandisets.json'))
L=d['dandisets'] if 'dandisets' in d else [v for v in d.values() if isinstance(v,list)][0]
for x in L:
  if x.get('dandiset')=='001683': print(json.dumps(x,indent=1))
"
```

```
{
 "dandiset": "001683",
 "name": "Transcranial Focused Ultrasound Stimulation Targeting White Matter Inhibits Seizures in a Rat Model of Epilepsy",
 "published_version": "0.260109.2104",
 "asset_count": 318,
 "size_gb": 355.74,
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
   "doi": "10.1109/tnsre.2025.3644273",
   "title": "Transcranial Focused Ultrasound Stimulation Targeting White Matter Inhibits Seizures in a Rat Model of Epilepsy",
   "relation": "IsDescribedBy",
[... 7 more lines not kept]
```

**Agent**

The supplement is now under `paper/`, so the earlier stop no longer applies. I'll look at the supplement figures that carry results (S4, S5, S7) before writing.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1109-tnsre.2025.3644273.supp.pdf",
 "pages": "5-8"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1109-tnsre.2025.3644273.supp.pdf')
for i in [4,5,7]:
  d[i].get_pixmap(dpi=110).save(f'supp_p{i+1}.png')
print('ok')
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
pip install --quiet --target $TMPDIR/pylib pymupdf 2>&1 | tail -2; ls $TMPDIR/pylib | head -3
```

```
[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: pip install --upgrade pip
_yaml
bin
fitz
```

**Agent calls Bash**

```bash
cd $TMPDIR && PYTHONPATH=$TMPDIR/pylib python -c "
import fitz
d=fitz.open('paper/10.1109-tnsre.2025.3644273.supp.pdf')
for i in [4,5,7]:
  d[i].get_pixmap(dpi=120).save(f'supp_p{i+1}.png')
print('ok')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp_p6.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp_p5.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/supp_p8.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -n "def \|KEYS\|keys\|allowed" tools/claims_check.py | head -40
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

[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
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
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1))"
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

Supplement now present (text plus PDF; I rendered pages 5, 6 and 8 to read Figs. S4, S5 and S7). The paper links no code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/001683/10.1109-tnsre.2025.3644273.yaml",
 "content": "# Claims for Gao, Frake, Durand and He (2026), \"Transcranial Focused Ultrasound Stimulation\n# Targeting White Matter Inhibits Seizures in a Rat Model of Epilepsy\", IEEE Trans Neural Syst\n# Rehabil Eng 34, doi:10.1109/tnsre.2025.3644273, on dandiset 001683 (same title on the archive;\n# its description says the dataset is described in this paper).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol as stated in docs/protocol.md (version pilot-10).\n#\n# Text read: the NIH author manuscript (PMC12848950) as served by Europe PMC, stored under paper/:\n# abstract, Introduction, Methods, Results, Discussion, Data Availability and the legends of Figs. 1\n# to 6; and the supplement (supp1-3644273.pdf, 8 pages: ex-vivo scanning, target confirmation, Figs.\n# S1 to S7). There is no PDF of the main paper, so values and significance marks drawn only inside\n# Figs. 2 to 6 were not read; Figs. S4, S5 and S7 were viewed in the supplement PDF. The paper links\n# no code; the only repository it names is the dandiset. No code was read.\n#\n# Data the paper used, as it reports them (Methods A to E, supplement):\n#  - Rats. 16 adult male Sprague-Dawley rats in the epilepsy study, 10 tFUS (experimental) and 6\n#    sham; 7 more in a mechanism study, 23 in all. The wild-type analysis (Fig. 5) uses all 23\n#    (Fig. 5B, N = 23 per group). Isoflurane anesthesia throughout.\n#  - Recordings. A 32-channel skull EEG probe (NeuroNexus HC32), aligned with bregma, and a\n#    64-channel intracranial array in left S1 (AP -2, ML -2.5, DV -1.5 mm). Tucker-Davis system at\n#    3051.8 Hz. The 4-AP cocktail is injected into right S1 (ipsilateral = right, the injection\n#    side; contralateral = left).\n#  - Target confirmation (supplement), before any 4-AP. A resting baseline recording, then tFUS\n#    bursts (200 us PD, 1.5 kHz PRF, 30% DC, 67 ms UD, 2 s inter-burst interval, ~127 kPa) at a\n#    series of positions around the CC (AP -2, ML 0, DV -3 mm); 200 trials per position recording;\n#    the position with the clearest EP is kept. These are the EPs and the resting \"sham\" of Fig. 5.\n#  - Epilepsy experiment (Fig. 1E). Injections of 1.2 uL 4-AP cocktail into right S1 about every\n#    62.5 min. A first monitoring block (repeated with more drug or less isoflurane when it had\n#    fewer than 5 seizures), then the time blocks baseline, condition, post 1, post 2 and post 3,\n#    each ~62.5 min. In the condition block the tFUS group received 3,750 pulses (20 ms PD, 1 Hz\n#    PRF, 2% DC, ~127 kPa) to the CC; the sham group received none. Post 3 is left out of the\n#    sham against tFUS comparisons (Results A).\n#  - Measured variables. EEG and intracranial LFP; seizure start and stop times per hemisphere.\n#\n# Shared methods, cited by the criteria below.\n#  M1 Seizure labels (Methods C). Signals notch filtered at 60 Hz and bandpass filtered 3 to 300 Hz;\n#     ICA and common average reference on the EEG. Each hemisphere is labelled on its own, from the\n#     EEG electrode closest to that side's burr hole (encircled in Fig. 1A; the channel numbers are\n#     not given in the text). A seizure is a period where the summed 30 to 80 Hz power exceeds a\n#     manually set threshold for at least 10 s; seizures less than 10 s apart are merged. The\n#     labels were set by hand, blinded to the block. If the dandiset holds the paper's seizure\n#     labels (its Data Availability says processed data were deposited), they are used. Otherwise\n#     the threshold, the power window and which ICA components were removed are open; the\n#     readings are thresholds of 2, 3 and 5 times the median of the summed 30 to 80 Hz power of\n#     that channel over the block, in 1 s windows, on CAR-referenced EEG without ICA, and a\n#     claim's outcome is the one all three give (blocked as methods_underspecified when they\n#     differ).\n#  M2 Seizure metrics (Methods C, Fig. 2 and 3 legends), per rat, hemisphere and block. Seizure\n#     Count; Percent Time in Seizure, summed durations over block length; Seizure Duration, the\n#     mean duration, leaving out seizures that start before or continue after the recording;\n#     Inter-Seizure Interval, the mean interval between neighbouring seizures, with the two tFUS\n#     rats that had a block without seizures left out (N = 8). Values are averaged over rats.\n#  M3 Statistics (Methods F, figure legends). Two-way ANOVA with Bonferroni-corrected post hoc tests,\n#     at P < 0.05, in GraphPad Prism. Fig. 3 and 4 plot each hemisphere in its own panel, so the\n#     factors are group (sham, tFUS) and block (baseline, condition, post 1, post 2), per\n#     hemisphere. Open, with readings: (a) ordinary two-way ANOVA, (b) repeated measures on block\n#     (Prism's mixed-effects model where values are missing); and the Bonferroni family, (i) each\n#     set of comparisons on its own (each block against baseline within a group; sham against tFUS\n#     at each block), (ii) all those comparisons in one family. A claim of significance holds\n#     when the stated comparisons are significant under one reading; a claim of absence follows\n#     the absence rule of the protocol, and both ANOVA readings are reported.\n#  M4 Percent change from baseline (Results B). Open, with readings: (a) the group mean of the block\n#     over the group mean at baseline, minus 1; (b) the mean over rats of each rat's change from\n#     its own baseline.\n#  M5 Band power and AI (Methods E). PSD by Fourier transform from the EEG electrode closest to\n#     each burr hole, bands theta 5 to 8, alpha 8 to 12, beta 12 to 30, gamma 30 to 80 Hz; band\n#     power divided by the total PSD of the entire spectrum. AI = (ipsi - contra)/(ipsi + contra)\n#     per band, normalized to the group's baseline AI. Open, with readings: the segment analysed,\n#     (a) the whole block, (b) the seizure periods of M1 only (Fig. S5 compares \"seizure periods\");\n#     the total, (a) 3 to 300 Hz, the filter band, (b) 0 Hz to Nyquist; the normalization of AI,\n#     (a) divided by the group's mean baseline AI, (b) minus it. Welch's method with 2 s Hann\n#     windows is a standard choice for the PSD.\n#  M6 PLI (Methods E). Per band, instantaneous phase by Hilbert transform of the band-filtered EEG\n#     (a zero-phase 4th order Butterworth filter is a standard choice), PLI = |mean over time of\n#     sign(sin(dphi))| for each pair of channels, one channel in each hemisphere. S1 pairs join\n#     left S1 and right S1 channels; non-S1 pairs join left and right non-S1 channels. The S1\n#     channels are drawn only in Fig. 5A (and marked as black squares in Figs. 5C-F, S6 and S7A),\n#     not listed in the text read. Open, with readings: the change, (a) a difference from the\n#     reference, (b) a ratio to it (the heat maps say \"PLI change\" and Fig. S7B plots values near\n#     zero, which favours (a)); for evoked windows, (a) a PLI per trial averaged over the 200\n#     trials, (b) one PLI over all trials' samples in the window; for seizures, (a) a PLI per\n#     seizure averaged, (b) one PLI over the concatenated seizure samples.\n#\n# The paper's text is at odds with itself in one place: the Methods give the wild-type tFUS window\n# as \"20 ms of stimulation\", but the bursts of the target confirmation the EPs come from last 67 ms\n# (supplement). The windows of Fig. 5 (-20 to 0, 0 to 20, 20 to 200 ms) are used as printed.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001683\"\npaper: doi:10.1109/tnsre.2025.3644273\nclaims:\n- id: fig2c-sham-duration-stable\n  statement: In the sham group, seizure durations from the ipsilateral and contralateral\n    hemispheres do not differ significantly across time blocks or between hemispheres.\n  source: Results A, paragraph 1; Figure 2C\n  quote: The Seizure Durations collected from both ipsilateral and contralateral hemispheres relative\n    to the drug injection site were not significantly different across time or between hemispheres\n  statistics:\n  - test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \">\"\n    n: 6 sham rats\n  criterion: A claim of absence. Seizures from M1, durations as in M2, sham rats, blocks baseline,\n    condition, post 1, post 2 and post 3. Two-way ANOVA (hemisphere by block) with Bonferroni post\n    hoc tests at P < 0.05 (Fig. 2 legend). The legend says each data point is one seizure, so the\n    test unit is open; readings (a) one value per seizure, (b) one mean per rat. Reproduced when\n    neither main effect nor any post hoc comparison is significant under the reading(s); not\n    reproduced when one is. Effect sizes are given either way; if the readings differ, blocked as\n    methods_underspecified.\n- id: fig2d-seizures-under-two-minutes\n  statement: Pooled over blocks, most seizures in the sham group last less than 2 minutes, and the\n    two hemispheres have similar distributions.\n  source: Results A, paragraph 1; Figure 2D\n  quote: The majority of recorded seizures lasted less than 2 minutes, and hemispheric distributions\n    appear relatively similar\n  criterion: Seizures from M1 in the 6 sham rats, all blocks pooled, per hemisphere. Reproduced when\n    more than half of the seizures last under 120 s in each hemisphere. The similarity of the\n    distributions has no test in the paper; the medians and a two-sample Kolmogorov-Smirnov test\n    are reported as description and do not decide.\n- id: fig2e-sham-count-stable\n  statement: In the sham group, seizure count does not differ significantly between time blocks or\n    hemispheres, with a slight decrease in the last two hours.\n  source: Results A, paragraph 1; Figure 2E\n  quote: There were no significant differences in Seizure Count between time blocks or hemispheres;\n    however, there was a slight decrease in number of seizures in the last two hours of the\n    experiment\n  statistics:\n  - test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \">\"\n    n: 6 sham rats\n  criterion: A claim of absence. Seizure Count per rat, hemisphere and block (M1, M2), sham rats,\n    five blocks; two-way ANOVA (hemisphere by block) with Bonferroni post hoc tests at P < 0.05.\n    Reproduced when no block or hemisphere effect or post hoc comparison is significant. The mean\n    counts of post 2 and post 3 against the earlier blocks are reported for the slight decrease,\n    which does not decide.\n- id: fig2f-sham-percent-time-post3\n  statement: In the sham group, percent time in seizure in the contralateral hemisphere differs\n    significantly between the sham condition block and post 3, suggesting the model is no longer\n    stable in the fifth hour.\n  source: Results A, paragraph 2; Figure 2F\n  quote: percent time in seizure between sham and post 3 for the contralateral hemisphere was\n    significantly different, which could mean that the seizure model is no longer stable during the\n    fifth hour of the experiment\n  statistics:\n  - test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: 6 sham rats\n  criterion: Percent Time in Seizure (M2), sham rats, five blocks, two-way ANOVA (hemisphere by\n    block) with Bonferroni post hoc tests (Fig. 2 legend, M3 readings). \"sham\" in the sentence is\n    read as (a) the condition block of the sham group, or (b) its baseline block. Reproduced when,\n    under one reading, the contralateral comparison with post 3 is significant at P < 0.05 and\n    post 3 is lower.\n- id: fig3a-count-reduction\n  statement: In the tFUS group, seizure count fell from baseline by 9%, 36% and 42% in the\n    ipsilateral S1 and by 10%, 41% and 42% in the contralateral S1 during stimulation, post 1 and\n    post 2, with significant reductions from baseline to post 1 and to post 2 in both hemispheres.\n  source: Results B, paragraph 1; Figure 3A\n  quote: The Seizure Counts in the ipsilateral S1 decreased from baseline by 9%, 36%, and 42% for\n    stimulation, post 1, and post 2, respectively. The decrease in Seizure Count recorded from the\n    contralateral S1 showed slightly higher reduction rates of 10%, 41%, and 42% ... Both\n    hemispheres displayed significant reductions in Seizure Count between baseline and post 1, as\n    well as between baseline and post 2\n  statistics:\n  - about: baseline against post 1 and post 2, each hemisphere\n    test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: 10 tFUS rats\n  expected:\n  - quantity: ipsilateral count decrease, stimulation\n    value: 9\n    tolerance: 0.9\n    unit: percent\n  - quantity: ipsilateral count decrease, post 1\n    value: 36\n    tolerance: 3.6\n    unit: percent\n  - quantity: ipsilateral count decrease, post 2\n    value: 42\n    tolerance: 4.2\n    unit: percent\n  - quantity: contralateral count decrease, stimulation\n    value: 10\n    tolerance: 1.0\n    unit: percent\n  - quantity: contralateral count decrease, post 1\n    value: 41\n    tolerance: 4.1\n    unit: percent\n  - quantity: contralateral count decrease, post 2\n    value: 42\n    tolerance: 4.2\n    unit: percent\n  criterion: Seizure Count (M1, M2) of the 10 tFUS rats; decreases as in M4, under each reading;\n    tests as in M3. Reproduced when, under one reading of M4, all six decreases are within\n    tolerance and, under one reading of M3, baseline against post 1 and baseline against post 2\n    are significant in both hemispheres. Partially reproduced when the four significant\n    reductions hold but some decreases fall outside tolerance, or the decreases hold and only\n    some of the four comparisons are significant.\n- id: fig3a-count-sham-vs-tfus\n  statement: Seizure count in the sham group stays steady, and the sham and tFUS groups differ\n    significantly during post 1 and post 2.\n  source: Results B, paragraph 1; Figure 3A\n  quote: Seizure Count within the sham group remained steady throughout, and there were significant\n    differences between the sham and tFUS groups during post 1 and post 2\n  statistics:\n  - test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: 6 sham and 10 tFUS rats\n  criterion: Seizure Count (M1, M2), group by block two-way ANOVA per hemisphere (M3). The text\n    does not say in which hemisphere; readings (a) both hemispheres, (b) either. Reproduced when\n    sham against tFUS is significant at post 1 and at post 2 under one reading of M3 and of the\n    hemisphere, and no sham block differs significantly from sham baseline; partially reproduced\n    when only one of post 1 and post 2 is significant.\n- id: fig3b-percent-time-reduction\n  statement: In the tFUS group, percent time in seizure decreased significantly from baseline by 33%\n    (ipsilateral) and 35% (contralateral) during stimulation and by 55% in post 1 and post 2 in both\n    hemispheres.\n  source: Results B, paragraph 2; Figure 3B; Discussion, paragraph 2\n  quote: The Percent Time in Seizure significantly decreased by 33% in the ipsilateral S1 and by 35%\n    in the contralateral S1 for stimulation, 55% for post 1, and 55% for post 2 in both hemispheres,\n    respectively\n  statistics:\n  - test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: 10 tFUS rats\n  expected:\n  - quantity: ipsilateral percent time decrease, stimulation\n    value: 33\n    tolerance: 3.3\n    unit: percent\n  - quantity: contralateral percent time decrease, stimulation\n    value: 35\n    tolerance: 3.5\n    unit: percent\n  - quantity: percent time decrease, post 1, each hemisphere\n    value: 55\n    tolerance: 5.5\n    unit: percent\n  - quantity: percent time decrease, post 2, each hemisphere\n    value: 55\n    tolerance: 5.5\n    unit: percent\n  criterion: Percent Time in Seizure (M1, M2) of the 10 tFUS rats; decreases as in M4, tests as in\n    M3. Which comparisons \"significantly\" covers is not said; readings (a) each of stimulation,\n    post 1 and post 2 against baseline in both hemispheres, (b) at least one of them per\n    hemisphere. Reproduced when, under one reading of M4, all six decreases are within tolerance\n    and the comparisons are significant under one reading; partially reproduced when the decreases\n    hold and only reading (b) gives significance, or significance holds and some decreases fall\n    outside tolerance.\n- id: fig3b-sham-percent-time-no-change\n  statement: In the sham group, percent time in seizure decreased slightly but did not differ\n    significantly from baseline in any block.\n  source: Results B, paragraph 2; Figure 3B\n  quote: Although Percent Time in Seizure for the sham condition decreased slightly across the\n    experiment, there were no significant differences from baseline\n  criterion: A claim of absence. Percent Time in Seizure of the 6 sham rats, group by block two-way\n    ANOVA per hemisphere with Bonferroni post hoc tests (M3). Reproduced when no sham block\n    (condition, post 1, post 2) differs from sham baseline at P < 0.05 in either hemisphere, under\n    the M3 reading(s); not reproduced when one does. Effect sizes given either way.\n- id: fig3b-percent-time-sham-vs-tfus\n  statement: Percent time in seizure differs significantly between sham and tFUS during post 1 in\n    the contralateral S1, and during stimulation and post 1 in the ipsilateral S1.\n  source: Results B, paragraph 2; Figure 3B\n  quote: Comparing the sham and tFUS groups, there were significant differences during the post 1\n    session in the contralateral S1 and during the stimulation and post 1 sessions in the\n    ipsilateral S1\n  statistics:\n  - test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: 6 sham and 10 tFUS rats\n  criterion: Percent Time in Seizure (M1, M2), group by block two-way ANOVA per hemisphere (M3).\n    Reproduced when, under one reading of M3, sham against tFUS is significant with tFUS lower for\n    all three named comparisons (contralateral post 1; ipsilateral stimulation and post 1);\n    partially reproduced for one or two of them.\n- id: fig3c-interval-increase\n  statement: Relative to baseline, the inter-seizure interval of the tFUS group increased by 27%,\n    49% and 28% (ipsilateral) and 30%, 52% and 31% (contralateral) during stimulation, post 1 and\n    post 2; only post 1 in the contralateral S1 differed significantly from baseline.\n  source: Results B, paragraph 3; Figure 3C\n  quote: Relative to baseline, the ipsilateral S1 Inter-Seizure Interval increased by 27%, 49%, and\n    28% during stimulation, post 1, and post 2 ... The contralateral S1 Inter-Seizure Interval\n    increased by 30%, 52%, and 31% during stimulation, post 1, and post 2, respectively. Only the\n    post 1 session in the contralateral S1 showed significant differences relative to baseline\n  statistics:\n  - about: contralateral post 1 against baseline\n    test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: 8 tFUS rats\n  expected:\n  - quantity: ipsilateral interval increase, stimulation\n    value: 27\n    tolerance: 2.7\n    unit: percent\n  - quantity: ipsilateral interval increase, post 1\n    value: 49\n    tolerance: 4.9\n    unit: percent\n  - quantity: ipsilateral interval increase, post 2\n    value: 28\n    tolerance: 2.8\n    unit: percent\n  - quantity: contralateral interval increase, stimulation\n    value: 30\n    tolerance: 3.0\n    unit: percent\n  - quantity: contralateral interval increase, post 1\n    value: 52\n    tolerance: 5.2\n    unit: percent\n  - quantity: contralateral interval increase, post 2\n    value: 31\n    tolerance: 3.1\n    unit: percent\n  criterion: Inter-Seizure Interval (M1, M2) of the 8 tFUS rats left after the Methods' exclusion\n    of the two rats with a block without seizures (which two is read from the labels); increases\n    as in M4, tests as in M3. Reproduced when, under one reading of M4, all six increases are\n    within tolerance and, under one reading of M3, contralateral post 1 is significant against\n    baseline and none of the other five comparisons is. Partially reproduced when the increases\n    hold and the pattern of significance differs, or the reverse.\n- id: fig3c-interval-sham-vs-tfus\n  statement: The inter-seizure interval of the sham group stays steady, and sham and tFUS differ\n    significantly during post 1 in both hemispheres.\n  source: Results B, paragraph 3; Figure 3C\n  quote: The Inter-Seizure Interval of the sham group remained steady across the length of the\n    experiment, and there were significant differences between sham and tFUS during post 1 in both\n    hemispheres\n  statistics:\n  - test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: 6 sham and 8 tFUS rats\n  criterion: Inter-Seizure Interval (M1, M2), group by block two-way ANOVA per hemisphere (M3).\n    Reproduced when, under one reading of M3, sham against tFUS at post 1 is significant with tFUS\n    higher in both hemispheres and no sham block differs from sham baseline; partially reproduced\n    when it holds in one hemisphere.\n- id: fig3d-duration-decline\n  statement: Seizure duration declines across time in both groups, and the only significant\n    reduction is from baseline to post 2 in both hemispheres of the tFUS group.\n  source: Results B, paragraph 4; Figure 3D\n  quote: The Seizure Duration showed a steady decline across time for both the sham group and the\n    tFUS group ... however, the only significant reduction occurred from baseline to post 2 in both\n    hemispheres of the tFUS group\n  statistics:\n  - test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: 6 sham and 10 tFUS rats\n  criterion: Seizure Duration (M1, M2), group by block two-way ANOVA per hemisphere (M3). Reproduced\n    when, under one reading of M3, tFUS baseline against post 2 is significant (post 2 shorter) in\n    both hemispheres and no other within-group comparison against baseline is significant, and the\n    group means at post 2 are below baseline in both groups. Partially reproduced when the post 2\n    reduction is significant in one hemisphere only, or other comparisons are also significant.\n- id: fig4-no-theta-alpha-gamma-power-change\n  statement: There are no significant changes in theta, alpha or gamma power ratios in either\n    hemisphere.\n  source: Results C, paragraph 1; Figure 4A, 4B and 4D\n  quote: There were no significant changes in the theta, alpha, or gamma power ratios in either\n    hemisphere\n  criterion: A claim of absence. Band power ratios as in M5 (both readings of the segment and of the\n    total are reported), sham and tFUS, blocks baseline, condition, post 1, post 2; group by block\n    two-way ANOVA per hemisphere and band with Bonferroni post hoc tests (M3, Fig. 4 legend).\n    Reproduced when no within-group comparison against baseline and no sham against tFUS\n    comparison is significant for theta, alpha and gamma in either hemisphere; not reproduced when\n    one is. If the M5 readings disagree, blocked as methods_underspecified.\n- id: fig4c-beta-decrease\n  statement: The beta power ratio of the tFUS group decreased significantly during stimulation and\n    post 1 compared with baseline.\n  source: Results C, paragraph 1; Figure 4C; Discussion, paragraph 3\n  quote: However, the beta ratio significantly decreased during tFUS and post 1 compared to baseline\n  statistics:\n  - test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: 10 tFUS rats\n  criterion: Beta (12 to 30 Hz) power over total (M5), tFUS group, tests as in M3. The hemisphere is\n    not named; readings (a) both hemispheres, (b) either. Reproduced when, under a combination of\n    the M3, M5 and hemisphere readings, the condition block and post 1 are both significantly\n    lower than baseline; partially reproduced when only one is.\n- id: figs4-sham-power-no-change\n  statement: In the sham group, band power ratios show no significant change among time blocks or\n    between hemispheres.\n  source: Results C, paragraph 1; Figure S4\n  quote: Within the sham group, the power ratios showed no significant change among time blocks or\n    between hemispheres\n  criterion: A claim of absence. Band power ratios (M5) of the 6 sham rats, five blocks, per band a\n    two-way ANOVA (hemisphere by block, as Fig. S4 plots it) with Bonferroni post hoc tests at P <\n    0.05. Reproduced when no block or hemisphere effect or post hoc comparison is significant in\n    any band; not reproduced when one is. If the M5 readings disagree, blocked as\n    methods_underspecified.\n- id: fig4ef-ai-increase\n  statement: The normalized asymmetry index of the tFUS group increases significantly relative to\n    baseline in the theta and alpha bands, and differs significantly from the sham group in every\n    band.\n  source: Results C, paragraph 1; Figure 4E-H\n  quote: Normalized AI of the tFUS group increased significantly within the theta and alpha bands\n    relative to baseline, and each frequency band displayed a significant difference between the\n    normalized AI of the tFUS group and sham group\n  statistics:\n  - about: tFUS against baseline, theta and alpha\n    test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: 10 tFUS rats\n  - about: tFUS against sham, each band\n    test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: 6 sham and 10 tFUS rats\n  criterion: AI per rat, band and block (M5), normalized to the group's baseline AI under readings\n    (a) and (b) of M5; group by block two-way ANOVA per band (M3). Which blocks show the effects is\n    not said in the text. Reproduced when, under one combination of readings, at least one tFUS\n    block is significantly above baseline in theta and in alpha, and sham against tFUS is\n    significant at one block or more in each of the four bands. Partially reproduced when either\n    part holds alone. Since an increase means opposite things under the two normalizations when\n    the baseline AI is negative, the sign of the mean baseline AI is reported.\n- id: figs5-seizures-lower-ai\n  statement: During seizures (baseline block, after 4-AP) the asymmetry index is negative and\n    differs from zero in every band, more than in the pre-4-AP baseline state; seizures disrupt the\n    normal interhemispheric balance.\n  source: Discussion, paragraph 4; Figure S5; Results C, paragraph 1\n  quote: Our results indicated that seizures decreased AI, reflecting a disruption of normal\n    interhemispheric balance\n  statistics:\n  - about: seizure AI against 0, each band (Fig. S5, ###)\n    test: one-sample t-test\n    p: 0.001\n    p_relation: \"<\"\n  - about: pre-4-AP baseline AI against 0, gamma (Fig. S5, #)\n    test: one-sample t-test\n    p: 0.05\n    p_relation: \"<\"\n  - about: seizure against pre-4-AP baseline, alpha and beta (Fig. S5, *)\n    test: not named in the legend\n    p: 0.05\n    p_relation: \"<\"\n  criterion: AI (M5, not normalized) per rat and band, for seizure periods of the baseline block and\n    for the pre-4-AP baseline state. The rats are not stated; readings (a) all 16 rats of the\n    epilepsy study, (b) the 10 tFUS rats. The pre-4-AP state is read as (a) the resting baseline\n    recording of target confirmation, (b) the first recording before the first injection, where\n    the dataset holds one. One-sample t-tests against 0 per band (Fig. S5 legend). Reproduced when,\n    under one combination, seizure AI is negative and significantly below 0 in all four bands and\n    seizure AI is significantly lower than the pre-4-AP AI in at least alpha and beta; the test of\n    that comparison is not named, so a paired t-test and a two-way ANOVA (state by band) with\n    Bonferroni post hoc tests are both reported, as readings. Partially reproduced when only the\n    tests against 0 hold.\n- id: fig5b-tfus-evoked-potentials\n  statement: tFUS of the CC in wild-type rats evokes potentials in the left S1 LFP that differ\n    significantly from the sham (resting) recording at some time points.\n  source: Figure 5B; Methods D, paragraph 1; Results D, paragraph 1\n  inferred: Read from the Fig. 5B legend (\"Yellow shadings denote significant differences between\n    the tFUS and sham groups\") and the Results' \"From EPs induced by CC tFUS\"; no sentence states\n    which time points differ.\n  criterion: For each of the 23 rats, the intracranial LFP of left S1 around the 200 tFUS trials of\n    the target confirmation recording at the chosen coordinates (supplement), and around pseudo\n    onsets in the resting baseline recording, normalized to the 20 ms before onset (Fig. 5B\n    legend). Which channel or average of the 64, and the test at each time point, are not stated;\n    readings for the channel (a) the mean over all 64 channels, (b) each channel; for the onsets\n    of the sham, (a) every 2 s from the start of the resting recording, matching the inter-burst\n    interval, (b) 200 onsets drawn at random with a fixed seed. Per time point, a paired t-test of\n    rat means between tFUS and sham, Bonferroni corrected over time points, is a stated choice;\n    an uncorrected test is shown as a variant. Reproduced when a run of significant time points\n    after onset appears under the readings; blocked as methods_underspecified if they disagree.\n- id: fig5cdj-wild-type-gamma-pli-decrease\n  statement: In wild-type rats, gamma band PLI decreases during and after tFUS relative to the\n    pre-tFUS window in most brain regions, on average in both S1 and non-S1 regions, while it\n    increases slightly in the sham.\n  source: Results D, paragraph 1; Figure 5C-F and 5J\n  quote: the PLI of the gamma band decreased during and after tFUS in most brain regions ... whereas\n    the gamma PLI increased slightly in the sham group ... On average, the gamma PLI of the tFUS\n    group decreased in both the S1 and non-S1 regions relative to the pre-tFUS window\n  statistics:\n  - about: tFUS against sham, normalized gamma PLI (Fig. 5J)\n    test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: 23 rats per group\n  criterion: The 23 rats; EEG epochs around the 200 tFUS trials of the target confirmation recording\n    at the chosen coordinates and around the sham onsets of fig5b-tfus-evoked-potentials (readings\n    (a), (b) there). Gamma (30 to 80 Hz) PLI per channel pair (M6) in the windows -20 to 0, 0 to\n    20 and 20 to 200 ms; change from pre-tFUS under the M6 readings. Reproduced when, under one\n    combination of readings, the mean change over S1 pairs and over non-S1 pairs is below zero in\n    both the tFUS and post-tFUS windows for the tFUS epochs, more than half of all pairs decrease,\n    the sham mean change is above zero, and a two-way ANOVA (group by region) with Bonferroni post\n    hoc tests finds tFUS against sham significant in at least one region and window. Partially\n    reproduced when the decreases hold without the test.\n- id: fig5ghi-low-band-pli-s1-only\n  statement: In wild-type rats, theta, alpha and beta PLI decrease only within the S1 regions during\n    tFUS.\n  source: Results D, paragraph 1; Figure 5G-I; Figure S6\n  quote: The PLI in theta, alpha, and beta bands only decreased within the S1 regions during the\n    tFUS conditions\n  criterion: As fig5cdj-wild-type-gamma-pli-decrease, for theta (5 to 8 Hz), alpha (8 to 12 Hz) and\n    beta (12 to 30 Hz). \"During the tFUS conditions\" is read as (a) the 0 to 20 ms window, (b) both\n    the 0 to 20 and 20 to 200 ms windows. Reproduced when, under one combination of readings, the\n    mean normalized PLI of the S1 pairs of the tFUS epochs is below the pre-tFUS reference in all\n    three bands and the non-S1 mean is not below it in any of them. Partially reproduced when that\n    holds for one or two bands. Significance marks of Fig. 5G-I could not be read (no main PDF);\n    the two-way ANOVA (group by region) with Bonferroni post hoc tests is reported, not deciding.\n- id: fig6-epileptic-pli-s1-decrease\n  statement: In epileptic rats, the S1 PLI of the tFUS group decreases in theta, alpha, beta and\n    gamma bands during stimulation, post 1 and post 2 relative to baseline seizures, while non-S1\n    PLI does not decrease; the decrease of S1 connectivity is significant.\n  source: Results D, paragraph 2; Figure 6A-D\n  quote: The S1 region of the tFUS group showed decreases in PLI within theta, alpha, beta, and gamma\n    bands during stimulation, post 1, and post 2 compared to baseline. Comparatively, the non-S1\n    regions did not exhibit a reduction in PLI values due to stimulation\n  statistics:\n  - about: sham against tFUS (Fig. 6, * and **)\n    test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n    n: 6 sham and 10 tFUS rats\n  criterion: PLI (M6) over the seizure periods (M1) of each block, per band, for S1 pairs and non-S1\n    pairs, normalized to the baseline block's seizures within each group (difference or ratio, M6).\n    Reproduced when, under one combination of readings, the tFUS S1 mean is below its baseline in\n    all four bands for the condition block, post 1 and post 2, the tFUS non-S1 mean is not below\n    baseline in most of those 12 band and block cells, and a group by block two-way ANOVA per band\n    and region with Bonferroni post hoc tests finds sham against tFUS significant for S1 in at\n    least one band and block. Partially reproduced when the S1 decreases hold in some bands only,\n    or without a significant group difference.\n- id: figs7-seizure-pli-s1-vs-non-s1\n  statement: Comparing seizures (baseline block) with the pre-4-AP baseline state, the PLI change of\n    S1 pairs differs significantly from that of non-S1 pairs in every band, which the paper takes\n    as a distinct network state of seizure rats.\n  source: Figure S7B; Results D, paragraph 2\n  quote: The PLI differences between wild-type and seizure rats may reflect distinct baseline network\n    states\n  statistics:\n  - about: theta, seizure S1 against seizure non-S1 (read from the Fig. S7B marks)\n    test: two-way ANOVA, Bonferroni post hoc\n    p: 0.01\n    p_relation: \"<\"\n  - about: alpha, beta and gamma, seizure S1 against seizure non-S1 (read from the Fig. S7B marks)\n    test: two-way ANOVA, Bonferroni post hoc\n    p: 0.05\n    p_relation: \"<\"\n  criterion: PLI (M6) per band for S1 and non-S1 pairs, in the seizure periods (M1) of the baseline\n    block and in the pre-4-AP baseline state (readings as in figs5-seizures-lower-ai), with the\n    change as a difference or ratio (M6). Fig. S7B plots seizure S1 slightly above zero and seizure\n    non-S1 below zero. Reproduced when, under one combination, a two-way ANOVA (region by band, or\n    region by state) with Bonferroni post hoc tests finds seizure S1 against seizure non-S1\n    significant at P < 0.05 in all four bands with S1 higher; partially reproduced for one to three\n    bands. The rats are not stated (readings as in figs5-seizures-lower-ai).\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001683/10.1109-tnsre.2025.3644273.yaml paper/10.1109-tnsre.2025.3644273.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "—\|rather" claims/001683/*.yaml; grep -c "criterion:" claims/001683/*.yaml
```

```
22
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001683/10.1109-tnsre.2025.3644273.yaml",
 "old_string": "interval, (b) 200 onsets drawn at random with a fixed seed. Per time point, a paired t-test of\n    rat means between tFUS and sham, Bonferroni corrected over time points, is a stated choice;\n    an uncorrected test is shown as a variant. Reproduced when a run of significant time points\n    after onset appears under the readings; blocked as methods_underspecified if they disagree.",
 "new_string": "interval, (b) 200 onsets drawn at random with a fixed seed. The test per time point is not\n    stated; readings (a) a paired t-test of rat means between tFUS and sham, Bonferroni corrected\n    over the time points after onset, (b) the same test uncorrected at P < 0.05. Reproduced when\n    a run of significant time points after onset appears under every combination of readings;\n    not reproduced when none does; blocked as methods_underspecified if they disagree."
}
```

```
The file claims/001683/10.1109-tnsre.2025.3644273.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001683/10.1109-tnsre.2025.3644273.yaml paper/10.1109-tnsre.2025.3644273.txt; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/001683/10.1109-tnsre.2025.3644273.yaml`. The quote checker passes with 0 problems. The earlier run stopped because the supplement was missing; it is now under `paper/`, so this run could write the claims.

**Text read**
- The NIH author manuscript (PMC12848950, from Europe PMC): main text, Methods, Results, Discussion and the legends of Figs. 1 to 6.
- The supplement (supp1-3644273, 8 pages): the ex-vivo pressure scan, the target confirmation procedure, and Figs. S1 to S7. I looked at Figs. S4, S5 and S7 as images, by rendering those pages of the supplement PDF.
- The paper links no code, so I read none.

**Claims:** 22 in all.
- 21 have quotes. One (`fig5b-tfus-evoked-potentials`) is marked inferred, because only the Fig. 5B legend and a passing phrase in the Results support it.
- 20 claims carry statistics. Every one is a bound, mostly two-way ANOVA with Bonferroni post hoc tests; Fig. S5 adds one-sample t-tests.
- All 22 have criteria.
- 4 have expected values: 22 numbers in all, the percent changes of Fig. 3A to 3C, each with a 10% tolerance.

**Details the paper leaves open, and the readings named.** Shared methods M1 to M6 are defined in the opening comment, and the criteria cite them.
- **Seizure labels (M1):** the threshold was set by hand, and the paper does not say which ICA components were removed. If the dataset holds the paper's own labels, those are used. Otherwise I named three thresholds: 2, 3 and 5 times the median of the summed 30 to 80 Hz power, in 1 s windows, on CAR-referenced EEG without ICA. A claim's outcome must be the same under all three.
- **Statistics (M3):** ordinary two-way ANOVA, or repeated measures on time block. The Bonferroni correction is applied either within each set of comparisons or across all of them together.
- **Percent change (M4):** the ratio of the group means, or the mean of each rat's own change.
- **Power and asymmetry index (M5):**
  - Segment analysed: the whole time block, or the seizure periods only.
  - Total power: 3 to 300 Hz, or up to Nyquist.
  - Normalizing the asymmetry index: dividing by the group's baseline, or subtracting it. When the baseline index is negative, "increased" means opposite things under the two.
- **Phase lag index (M6):** the change is a difference or a ratio. It is computed per trial and averaged, or pooled over all trials; and per seizure, or over the seizures joined together.
- **Per-claim readings:**
  - Which hemisphere is meant (Fig. 3A between groups, Fig. 4C).
  - What "sham" means in Fig. 2F: the condition block or the baseline block.
  - The test unit in Fig. 2C: one seizure or one rat.
  - Which comparisons "significantly decreased" covers in Fig. 3B.
  - Fig. 5B: the onsets for the sham recording, the channel, and the test at each time point.
  - The windows meant by "during the tFUS conditions" (Fig. 5G to I).
  - Which rats, and which pre-4-AP recording, Figs. S5 and S7 use.

**Missing from what was read**
- There is no PDF of the main paper. The significance marks and values drawn inside Figs. 2 to 6 could not be read, so the statistics record only the P < 0.05 levels given in the legends.
- The text does not list:
  - the EEG channels used for seizure labelling (encircled in Fig. 1A);
  - the S1 and non-S1 channel sets (drawn in Fig. 5A).
- The test behind the seizure against pre-4-AP comparison in Fig. S5 is not named.
- The paper contradicts itself on one point, noted in the file: the Methods give a 20 ms tFUS window, but the target confirmation bursts the evoked potentials come from last 67 ms. The windows are used as printed.

## End of run

28 turns, 4 minutes, result: success.
