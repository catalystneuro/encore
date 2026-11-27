# lakshminarasimhan-2024 · claims · run 44916849510

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/; ls claims | head -50; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md
```

```
1:# Protocol for an attempt
43:## Reader
45:### 1. Get the paper
59:### 2. Read the paper's code
69:### 3. Write the claims file
165:### 4. Data from outside the paper's own recordings
173:### 5. Check
186:### 6. Answer questions
199:## Author
215:### 1. Establish what can be tested
370:### 2. Check the data against its description
385:### 3. Write the entry
470:### 4. Lock, check and run
490:### 5. Record the attempt
599:### 6. Hand over for verification
637:## Repeat attempts
703:## Local and remote datasets
726:## Verifier
730:### Round 1: without the author's conclusions
755:### Round 2: with the author's conclusions
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la paper/; ls claims | wc -l
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
3	Version: `pilot-18`. Record this version in the attempt's provenance.
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
cat claims/fouke-2025.yaml; cat papers/datasets/lakshminarasimhan-2024.yaml 2>/dev/null; ls papers/
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
[... 317 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2024.114059.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2024.114059.txt",
 "offset": 589,
 "limit": 600
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1189,1907p paper/10.1016-j.celrep.2024.114059.txt | grep -v '^10\.' | grep -v '^$' | head -100
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1189,1907p paper/10.1016-j.celrep.2024.114059.txt | grep -v '^10\.' | grep -v '^$' | awk 'length($0)>40'
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "Figure S6: Cortico\|Table S1\. Sim\|Figure S3\|S2:" paper/10.1016-j.celrep.2024.114059.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2024.114059.txt",
 "offset": 1640,
 "limit": 270
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/kaushik-l/tc-learning && cd tc-learning && git log -1 --format='%H %ad' && find . -type f -not -path './.git/*' | head -100
```

```
2aa94dd5fb381ffb30a56962a3be20b96f63868b Sun Oct 6 22:14:38 2024 -0400
./rflo.py
./thalamocortical__reaching.py
./train_bptt.py
./bptt__reaching.pt
./README.md
./plot.py
./thalamocortical__motor.py
./model.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/tc-learning && cat README.md && wc -l *.py && grep -il "dandi\|nwb\|thalam.*data\|spike\|neural data" *.py
```

```
# tc-learning

Code for implementing thalamocortical learning models described in the following paper:

[**Specific connectivity optimizes learning in thalamocortical loops**](https://www.biorxiv.org/content/10.1101/2022.09.27.509618v1)  
Lakshminarasimhan, Xie, Cohen, Sauerbrei, Hantman, Litwin-Kumar, Escola

For simulating the reaching task, you will need to download *bptt__reaching.pt*, which is a pre-trained rnn model used to generate the target function for training the thalamocortical model. Alternatively, you can generate this file locally by running *train_bptt.py* to train this rnn model from scratch. Feel free to reach out to me at [removed: an e-mail address] if you have questions.
  147 model.py
  152 plot.py
  134 rflo.py
  161 thalamocortical__motor.py
  227 thalamocortical__reaching.py
  114 train_bptt.py
  935 total
```

**Agent calls Bash**

```bash
grep -rn "000009" papers/*.yaml | head; ls claims | grep -i "guo\|lakshmi"; grep -rln "000009" claims | head
```

```
papers/manifest.yaml:46:  000009:
papers/renamed.yaml:11:  000009-guo-2017-01: guo-2017-01
papers/renamed.yaml:265:  000009-guo-2017: guo-2017
papers/renamed.yaml:512:  000009: guo-2017
guo-2017.yaml
claims/guo-2017.yaml
```

**Agent calls Bash**

```bash
sed -n 40,60p papers/manifest.yaml; head -40 claims/guo-2017.yaml
```

```
- doi: 10.1038/s41586-020-2907-3
    status: stored
    version: as served by europe_pmc
    source: europe_pmc+crossref (paper-text-fetcher)
    pdf: false
    supplements: 0
  000009:
  - doi: 10.1038/nature22324
    status: stored
    version: as served by europe_pmc
    source: europe_pmc+crossref (paper-text-fetcher)
    pdf: false
    supplements: 1
  - doi: 10.1016/j.celrep.2024.114059
    status: stored
    version: version of record
    source: find_reuse cache
    pdf: false
    supplements: 1
  '000010':
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper && python -c "
import pypdf;r=pypdf.PdfReader('10.1016-j.celrep.2024.114059.supp-mmc2.pdf');print(len(r.pages))
for i,p in enumerate(r.pages):
  t=p.extract_text() or ''
  if 'Figure 6' in t or 'Figure S6' in t: print(i+1, t[:120].replace('\n',' '))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import pypdf;r=pypdf.PdfReader('10.1016-j.celrep.2024.114059.supp-mmc2.pdf');print(len(r.pages))
    ^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pypdf'
```

**Agent calls Bash**

```bash
cd paper && which pdftotext pdfinfo; pdfinfo *.pdf | grep Pages; for i in $(seq 1 32); do t=$(pdftotext -f $i -l $i *.pdf - 2>/dev/null | tr '\n' ' '); case "$t" in *"Figure 6"*|*"Figure S6"*) echo "$i: ${t:0:100}";; esac; done
```

```
/bin/bash: line 1: pdfinfo: command not found
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2024.114059.supp-mmc2.pdf",
 "pages": "10-13"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "import fitz" 2>&1; python -c "import pdfplumber" 2>&1; pip list 2>/dev/null | grep -i -E "pdf|mupdf|poppler"
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz
ModuleNotFoundError: No module named 'fitz'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2024.114059.txt",
 "offset": 1560,
 "limit": 80
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  && grep -rn -B2 -A3 "simulat" claims/*.yaml | grep -n "data:" | head -20; grep -rn "kind:" claims/*.yaml | awk '{print $NF}' | sort | uniq -c; grep -n "data\b\|kind\|elsewhere\|simulation\|model" docs/schema* docs/*.md 2>/dev/null | grep -i "simulat\|kind" | head -20
```

```
119:claims/brudner-2026.yaml-435-  data: with_inputs
292:claims/burman-2023.yaml-766-  data: elsewhere
301:claims/burman-2023.yaml-792-  data: elsewhere
315:claims/burman-2023.yaml-822-  data: elsewhere
329:claims/burman-2023.yaml-850-  data: elsewhere
766:claims/duszkiewicz-2024.yaml-490-  data: elsewhere
790:claims/duszkiewicz-2024.yaml-527-  data: elsewhere
884:claims/elliott-2026.yaml-734-  data: elsewhere
997:claims/hazon-2022.yaml-835-  data: elsewhere
1015:claims/hazon-2022.yaml-853-  data: elsewhere
1346:claims/kutschireiter-2023.yaml-244-  data: elsewhere
1407:claims/laquitaine-2024.yaml-130-  data: with_inputs
1431:claims/laquitaine-2024.yaml-205-  data: with_inputs
1442:claims/laquitaine-2024.yaml-218-  data: with_inputs
1468:claims/laquitaine-2024.yaml-301-  data: with_inputs
1489:claims/laquitaine-2024.yaml-330-  data: with_inputs
1504:claims/laquitaine-2024.yaml-346-  data: with_inputs
1516:claims/laquitaine-2024.yaml-360-  data: with_inputs
1556:claims/laquitaine-2024.yaml-409-  data: with_inputs
1598:claims/laquitaine-2024.yaml-466-  data: with_inputs
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,175p docs/pilot-notes.md; grep -n -B3 -A12 "data: elsewhere" claims/kutschireiter-2023.yaml | head -40; ls tools/ schema* 2>/dev/null; grep -rn "simulation\|model.*elsewhere" docs/protocol.md | head
```

```
- [000130, Sohn, Narain, Meirhaeghe and Jazayeri 2019](pilot-notes/sohn-2019-01.md)
- [001616, Gerken et al. 2025](pilot-notes/gerken-2025-01.md)
- [001754 again, on the fixed draft (2026-10-15)](pilot-notes/knierim-2000-02.md)
- [002014, Choi et al. 2025](pilot-notes/choi-2025-01.md)
- [001933, Chen et al. 2026](pilot-notes/chen-2026-01.md)

## Protocol pilot-7 (2026-10-15): data in other archives

001933 showed that a blocked claim can mean two different things. Eight of
its claims rest on imaging, proteomics and blots that the paper deposited
in the BioImage Archive, PRIDE and Zenodo; they were blocked with
`data_missing`, the same reason as data that are public nowhere. pilot-7
adds a fourth data kind, `elsewhere`, for a claim whose data the dandiset
does not hold because the paper put them in another public archive. The
claim names the archive and a pinned identifier under `where`, is tested on
those data like any other claim, and is counted on its own, apart from the
dandiset's claims and from `with_inputs` claims. It is never blocked with
`data_missing`; if it cannot be tested here, the reason is the one that
applies, such as `too_large` or `not_runnable`. `data_missing` now means
public nowhere. The README table leaves these claims out, and each
[... 93 more lines not kept]
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
grep -l "relation: reuses" papers/datasets/*.yaml | head -20 | xargs -n1 basename | sed 's/.yaml//' | while read k; do [ -f claims/$k.yaml ] && echo $k; done | head; grep -rn -i "not public\|public nowhere\|not deposited\|no deposit" claims/*.yaml | head
```

```
alasfour-2024
burman-2023
du-2026
elliott-2026
fritsche-2022
jarzebowski-2026
kussovska-2025
claims/berg-2020.yaml:923:  where: The mFISH and SMI-32 images are not deposited in any archive the paper or the code names;
claims/brudner-2026.yaml:28:#     checkpoints of Figs. 2 and 3 were not deposited and names where the code and the SI disagree;
claims/brudner-2026.yaml:200:    not deposited (code, REPRODUCE_FIGURES_1_3.md)
claims/brudner-2026.yaml:328:    paper's training arrays and checkpoints were not deposited
claims/burman-2023.yaml:113:    the paper's patch-clamp recordings are not deposited (available on request). Were the data available,
claims/burman-2023.yaml:137:    the paper's patch-clamp recordings are not deposited (available on request). Were the data available,
claims/burman-2023.yaml:158:    the paper''s patch-clamp recordings are not deposited (available on request). A claim of absence:
claims/burman-2023.yaml:181:    the paper's patch-clamp recordings are not deposited (available on request).
claims/burman-2023.yaml:190:    the paper's patch-clamp recordings are not deposited (available on request). The test and numbers
claims/burman-2023.yaml:200:    the paper's patch-clamp recordings are not deposited (available on request). A claim of absence whose
```

**Agent calls Bash**

```bash
sed -n 1,60p claims/burman-2023.yaml; sed -n 100,140p claims/burman-2023.yaml; sed -n 755,800p claims/burman-2023.yaml
```

```
# Claims for Burman, Brodersen, Raimondo, Sen & Akerman (2023), Neuron 111, 3531-3540,
# "Active cortical networks promote shunting fast synaptic inhibition in vivo", on dandiset 000458.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
# 2026-11-10, protocol pilot-14 as stated in docs/protocol.md (Reader, steps 1 to 4).
#
# Text read. The version of record (open access, CC BY), full text from Europe PMC (PMC11913778),
# in paper/10.1016-j.neuron.2023.08.005.txt: Summary, Introduction, Results, the legends of
# Figures 1 to 4, Discussion, STAR Methods with Tables 1 and 2, and Data and code availability.
# The supplement (Document S1, Figures S1 to S7 and their legends) is not in the text, and no PDF
# was supplied. No claim on the dandiset needs it except figs6-rate-regressed, whose method is
# only in the Figure S6 legend; that claim names readings. The claims on Figures S2 to S5 and S7
# rest on the main-text sentences that cite them, and their tests are not known here.
#
# Code read. (1) gist.github.com/paulbrodersen/a77bcf5e06ae27fa96923cb313a02ccf, revision
# 43a13d89441b7f56e835e84fa5811d9567917daf, burman_et_al_2023_neuropixel_data_analysis.py: reads
# the 17 NWB sessions of DANDI:000458 (version 0.230317.0039, named in its docstring) and writes,
# per unit, evoked firing rate, peri-stimulus histogram entropy and synchrony for the awake and
# isoflurane epochs. It does not hold the exclusion step, the statistics or the plots.
# (2) gist.github.com/paulbrodersen/2ce61e4e57c7659b727d30e3e1e0128f, revision
# f6a05661c10051560aa381e334099efd8521617b, burman_et_al_2023_neuronal_network_simulation.py: the
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/tc-learning && cat thalamocortical__motor.py && sed -n 1,147p model.py && grep -n "def \|argparse\|meta\|ctype\|strategy\|'pc'\|readout" rflo.py thalamocortical__reaching.py plot.py | head -60
```

```
import numpy as np
import numpy.random as npr
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA
from scipy.stats.stats import pearsonr

# thalamocortical model for motor learning

# seed
npr.seed(1)


# non-linearity
def f(x):
    return np.tanh(x)


# derivative of non-linearity
def df(x):
    return 1 - np.tanh(x) ** 2
[... 304 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py
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

[... 61 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/lakshminarasimhan-2024.yaml",
 "content": "# Claims for Lakshminarasimhan, Xie, Cohen, Sauerbrei, Hantman, Litwin-Kumar & Escola (2024), Cell\n# Reports 43, 114059, \"Specific connectivity optimizes learning in thalamocortical loops\", on\n# dandiset 000009.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-21,\n# protocol pilot-18 as stated in docs/protocol.md (Reader, steps 1 to 4).\n#\n# Text read. paper/10.1016-j.celrep.2024.114059.txt. Its header says \"version of record\", but the\n# body is the NIH author manuscript in PubMed Central (PMC11104520, NIHMS1988710): Summary,\n# Introduction, Results, Discussion, STAR Methods, the legends of Figures 1 to 6 and the key\n# resources table. The supplement (mmc2.pdf, pages 22 to 32) is appended to the same file: the\n# legends of Figures S1 to S6 and Table S1, with the figure labels as loose text. The PDF\n# (paper/...supp-mmc2.pdf) could not be rendered here (no PDF renderer in the environment), so no\n# figure was read; numbers shown only in figures are taken from the text labels where noted.\n#\n# Code read. github.com/kaushik-l/tc-learning, commit 2aa94dd5fb381ffb30a56962a3be20b96f63868b\n# (2024-10-06), the repository the key resources table names. It holds simulation code only:\n# thalamocortical__motor.py (the motor control task with RFLO and corticothalamic weights\n# 'random', 'readout' or 'pc', one run, seed 1), thalamocortical__reaching.py with model.py,\n# train_bptt.py and bptt__reaching.pt (the reaching task of Figure 5), rflo.py, plot.py. It has no\n# working memory task, no meta-learning, and no analysis of the neural data. Where the code and\n# the Methods differ, the Methods are followed and the code is a variant: the code's readout-\n# aligned update uses rate 0.01 (Methods beta = 1), its PC-aligned update uses rate 0.01/i^2 for\n# the i-th thalamic unit (Methods beta = 0.01), its feedback weights B are N(0, 1/R) (Methods\n# U(0, 2/N)) and its corticothalamic weights start at g N(0, 1/N) (Methods N(0, 1/N)).\n#\n# Data the paper used, as it reports them (STAR Methods, Neural datasets; Figure 6; Figure S6).\n# The paper records no data (\"The study did not generate any new data\").\n# (1) Motor control: Sauerbrei et al. 2020 (ref. 14), simultaneous recordings in motor cortex and\n# motor thalamus while mice reach to grasp a food pellet after an acoustic cue; one session each\n# from 3 mice; 53 +/- 9 cortical and 33 +/- 5 thalamic units per session (101 thalamic neurons in\n# Figure 6E); hand position in three axes. The paper names no deposit for these data (the key\n# resources table lists only DANDI:000009), and DANDI:000009 does not hold them. Their claims are\n# kept and cannot be tested on this dandiset.\n# (2) Working memory: Guo et al. 2017 (ref. 10), DANDI:000009 (key resources table, \"ALM and\n# thalamus data\"). Recordings \"in separate sessions\" in ALM and in thalamus (VM and VAL) while a\n# mouse reports the anterior or posterior pole location by licking left or right after a delay of\n# about 1.3 s. \"The dataset includes 5 behavioral sessions from one mouse. The total number of\n# cortical and thalamic units was 151 and 72 respectively.\" Variables used: spike times of ALM and\n# thalamic units, trial epochs (delay onset), the choice (lick direction) and its correctness.\n# The dandiset's archive title is the Guo et al. 2017 title; its description says it holds ALM and\n# thalamus spikes during the delayed response task with photoinhibition. Which mouse and sessions\n# the paper used is for the author to find (claim wm-sessions-link).\n# (3) Model simulations (Figures 1 to 5, S1 to S5): generated by the paper's models, not deposited;\n# data elsewhere, where names the code.\n#\n# Method for the claims on DANDI:000009, from STAR Methods (Neural datasets, Estimation of readout\n# weights, Analysis of corticothalamic communication, Alignment between weights), the Results\n# (Data are consistent with model predictions) and the legends of Figures 6 and S6. The paper's\n# code holds none of it. Cited in the criteria as W1 to W10.\n# W1 Sessions and units. Five sessions from one mouse with 151 ALM and 72 thalamic (VM/VAL) units\n#    in total (Methods). Which units count (all sorted units, or the single units Guo et al.\n#    label as well isolated) is open; the reading that gives 151 and 72 in the five sessions is\n#    used, and if none does, the closest is used and the difference reported.\n# W2 Trials. Correct trials only, grouped by choice, left and right (Methods). The paper does not\n#    say whether photoinhibition trials are left out; readings (T1) correct trials without\n#    photostimulation; (T2) all correct trials.\n# W3 Alignment and window. Spike trains aligned to the onset of the delay epoch (Methods, Figure 6B\n#    legend); analyses restricted to the delay period (Results), from delay onset to the go cue.\n#    The time bin is not given; 10 ms (the model's dt) is a standard choice and cannot change the\n#    outcome beyond the smoothing.\n# W4 Smoothing. Spike trains convolved with a Gaussian of width sigma chosen by cross-validation on\n#    the validation trials (Methods). The grid of sigma is not given; 10, 25, 50, 100 and 200 ms is\n#    a standard choice, and the chosen sigma is reported.\n# W5 Split. Trials split at random into 80% training, 10% validation and 10% test (Methods),\n#    within each choice. Variance explained is computed on the test-set averages. The seed is a\n#    standard choice; results are reported as the mean over 10 random splits as well as for one.\n# W6 Activity. Per choice, the trial-averaged smoothed rates over the window, left and right\n#    concatenated in time, h(t) = [h_l(t) h_r(t)] for ALM and r(t) likewise for each thalamic unit\n#    (Methods; Figure S6B legend).\n# W7 Readout. Ordinary least squares of c(t), -1 for every bin of left trials and +1 for right,\n#    on h(t) (Methods). An intercept is included (standard). Figure 6C gives n = 5 sessions, so the\n#    readout and its PC alignment are computed per session from that session's ALM units, and\n#    averaged over sessions.\n# W8 PCs. Eigendecomposition of the covariance of the training-set h(t) (mean-subtracted), top\n#    k = 16 eigenvectors (Methods). Readout in the PC basis w_PC = w U_1:16, taken in absolute\n#    value as for the motor task (Methods, Estimation of readout weights); the alignment of the\n#    readout with PC i is |w . u_i| / ||w|| (Methods, Alignment between weights).\n# W9 Cortical population for the thalamic analyses. The Methods regress each thalamic unit on\n#    cortical activity, and the Figure S6 legend says \"in all analysis, the ALM cortical population\n#    (n=151) was subsampled to match the dataset from motor cortex (n=53 +/- 9)\". Readings\n#    (P1) the 151 ALM units pooled over the five sessions as one trial-averaged population,\n#    subsampled at random to 53 units, the result averaged over 20 subsamples; (P2) the same\n#    without subsampling; (P3) each thalamic unit with the ALM units of its own session.\n# W10 Thalamic regression. For each thalamic unit, OLS of r(t) on the projections h_k(t) =\n#    h(t) U_1:k, k = 1 to 16, and on all cortical units; R2 on the test set, R2(k) = 1 -\n#    Var[r - w_k h_k] / Var[r] (Methods). Normalization of R2(k), open between the Methods and the\n#    Results: (N1) R2(k)/R2(16) (Methods); (N2) R2(k)/R2 with R2 from all cortical units\n#    (Results); (N3) each unit's curve rescaled to run from 0 to 1 (Figure 6D legend). Summary\n#    over the 72 units, mean +/- SEM (Figure 6E legend, \"standard errors in mean\").\nschema_version: 2\npaper: doi:10.1016/j.celrep.2024.114059\nclaims:\n- id: wm-sessions-link\n  kind: link\n  statement: The dandiset holds the working memory data the paper reanalyzed, five sessions from one\n    mouse with 151 ALM units and 72 thalamic units in total.\n  source: STAR Methods, Neural datasets; key resources table\n  quote: The dataset includes 5 behavioral sessions from one mouse. The total number of cortical and\n    thalamic units was 151 and 72 respectively\n  expected:\n  - quantity: sessions from one mouse\n    value: 5\n    tolerance: 0\n  - quantity: ALM units over the five sessions\n    value: 151\n    tolerance: 15\n  - quantity: thalamic (VM/VAL) units over the five sessions\n    value: 72\n    tolerance: 7\n  criterion: Among the mice of DANDI:000009 with ALM and thalamic (VM or VAL) units, find one with\n    five sessions whose unit totals, under a reading of W1, are within tolerance of 151 ALM and 72\n    thalamic units. Reproduced when exactly one mouse fits; when several fit, the one with the\n    closest counts is used and the others are reported; not reproduced when none does. The\n    session list found is used by every claim on DANDI:000009.\n- id: fig1c-tc-learning-improves-with-thalamus\n  statement: With RFLO plasticity in thalamocortical synapses, task performance (1 - R2 on the motor\n    control target) improves with the number of thalamic neurons.\n  source: Results, Thalamocortical learning rule, paragraph 2; Figure 1C (green)\n  quote: We found that the performance improves with the number of thalamic neurons, suggesting that\n    local plasticity at thalamo-cortical synapses ( W C T ) facilitates learning\n  data: elsewhere\n  where: Not deposited; generated by the paper's model, github.com/kaushik-l/tc-learning at commit\n    2aa94dd (thalamocortical__motor.py with tc_type 'random')\n  criterion: The model of STAR Methods (N = 256, g = 1.5, dt = 0.1 tau, RFLO with eta = 0.1 on\n    thalamocortical and readout weights, random fixed corticothalamic weights, 10,000 trials), on\n    the basic motor control task, for M = 1, 2, 4, ..., 128 (Figure 1 legend), 40 initializations\n    each (Quantification). Reproduced when the median 1 - R2 decreases from M = 1 to M = 128 and\n    the Spearman correlation between M and the medians is negative.\n- id: fig1d-cortical-feedback-alignment\n  statement: The alignment between feedback weights B and readout weights W_O in cortical neurons\n    rises as learning performance improves, a sign of credit assignment in thalamocortical synapses.\n  source: Results, Thalamocortical learning rule, paragraph 2; Figure 1D (green)\n  quote: This improvement in learning performance is accompanied by an increase in the alignment\n    between weights in the feedback pathway B (which communicate error signals to post-synaptic\n    neurons) and readout weights W O\n  data: elsewhere\n  where: Not deposited; generated by the paper's model, github.com/kaushik-l/tc-learning at commit\n    2aa94dd (thalamocortical__motor.py)\n  criterion: Same simulations as fig1c-tc-learning-improves-with-thalamus. Alignment is the\n    normalized dot product of B and W_O (STAR Methods, Alignment between weights), normalized as\n    (beta - beta_0)/(1 - beta_0) with beta_0 the alignment with a random direction (Figure 1\n    legend). Reproduced when the median normalized alignment at the end of learning increases with\n    M (Spearman correlation positive).\n  depends_on:\n  - fig1c-tc-learning-improves-with-thalamus\n- id: fig1cd-corticothalamic-plasticity-fails\n  statement: Local plasticity at corticothalamic as well as thalamocortical synapses gives no gain\n    over thalamocortical learning with fixed random corticothalamic weights, and feedback alignment\n    in thalamic neurons is no greater than chance.\n  source: Results, Thalamocortical learning rule, paragraphs 3 and 4; Figure 1C (gray) and 1D\n    (black); Figure S1B and S1C\n  quote: local plasticity operating simultaneously at thalamocortical and corticothalamic synapses\n    does not yield any improvement in learning performance over what is obtained from learning only\n    thalamocortical synapses with fixed random corticothalamic connections ... the alignment is no\n    greater than chance in thalamic neurons\n  data: elsewhere\n  where: Not deposited; the paper's code at commit 2aa94dd has no corticothalamic RFLO; written from\n    STAR Methods, Equation 6\n  criterion: The model of fig1c-tc-learning-improves-with-thalamus with corticothalamic weights also\n    updated by Equation 6 (B' from U(0, 2/M)); the corticothalamic learning rate was set by\n    hyperparameter optimization (Methods), whose search the paper does not give, so the rate with\n    the lowest median error over 1e-4, 1e-3, 1e-2 and 1e-1 is used. The paper gives no test. For\n    each M, the median 1 - R2 of the two-site model is compared with the thalamocortical-only model\n    by a two-sided Wilcoxon rank-sum test over the 40 runs. Reproduced when for no M the two-site\n    model is better at p < 0.05, and the median normalized thalamic alignment (B' against\n    W_CT phi'(u) W_O) is within its bootstrap standard error of 0 for every M.\n- id: figs1d-small-initial-weights\n  statement: Corticothalamic plasticity can be made to work when thalamocortical weights start small,\n    of order 1/N variance, so that the thalamus barely affects the cortex before learning.\n  source: Results, Thalamocortical learning rule, paragraph 4; Figure S1D\n  quote: One way to overcome this challenge is to initialize thalamocortical weights to have small (\n    ~ O ( 1 / N ) variance such that thalamic influence on cortical activity is minimal prior to\n    learning\n  data: elsewhere\n  where: Not deposited; written from STAR Methods and the Figure S1D legend\n  criterion: As fig1cd-corticothalamic-plasticity-fails, with initial weights of variance 1/N (the\n    paper says \"~O(1/N)\" and gives no constant). Reproduced when the median normalized thalamic\n    feedback alignment exceeds its bootstrap standard error above 0 for most M and the two-site\n    model has lower median 1 - R2 than the thalamocortical-only model for most M.\n- id: fig2d-metalearned-error-reduction\n  statement: Meta-learned corticothalamic weights reduce the error of thalamocortical learning\n    severalfold compared with random corticothalamic weights, by a median factor of 5.8 in motor\n    control and 5.1 in working memory.\n  source: Results, Optimal corticothalamic connectivity improves learning performance, paragraph 3;\n    Figure 2D\n  quote: The error dropped severalfold across both tasks when thalamocortical learning was performed\n    using optimized corticothalamic weights as opposed to random corticothalamic weights ( Figure 2D\n    ; median factor of reduction in error: motor control, 5.8; working memory, 5.1)\n  data: elsewhere\n  where: Not deposited; the paper's code at commit 2aa94dd has no meta-learning; written from STAR\n    Methods, Meta-learning\n  expected:\n  - quantity: median error reduction factor, motor control\n    value: 5.8\n    tolerance: 0.58\n  - quantity: median error reduction factor, working memory\n    value: 5.1\n    tolerance: 0.51\n  criterion: Meta-learning as in STAR Methods (N = 256, M = 32, corticothalamic weights onto one\n    thalamic unit optimized by BPTT with Adam, rate 1e-4, 10,000 epochs of 200 RFLO trials,\n    thalamocortical weights reset each epoch, B^T = W_O, other weights fixed), then thalamocortical\n    learning with the optimized and with random corticothalamic weights over 40 initializations.\n    The factor is read as (R1) the median over runs of the ratio of errors, run by run, or (R2) the\n    ratio of the median errors. Reproduced when both factors are within tolerance under one\n    reading.\n- id: figs2a-random-feedback\n  statement: The gain from meta-learned corticothalamic weights holds when learning uses random\n    error-feedback weights B and readout weights are learned.\n  source: Results, Optimal corticothalamic connectivity improves learning performance, paragraph 3;\n    Figure S2A\n  quote: We found qualitatively similar results when learning in the presence of random\n    error-feedback weights, B ( STAR Methods ; Figure S2A ), showing that the improvement in\n    learning performance cannot be attributed to feedback alignment used in the meta-learning\n    procedure\n  data: elsewhere\n  where: Not deposited; written from STAR Methods, Meta-learning, and the Figure S2A legend\n  criterion: As fig2d-metalearned-error-reduction, with random B and readout weights updated by the\n    delta rule (Table S1, S2A). Reproduced when the median error with optimized weights is lower\n    than with random weights in both tasks by a two-sided Wilcoxon rank-sum test at p < 0.05 over\n    the 40 runs (the paper names no test).\n  depends_on:\n  - fig2d-metalearned-error-reduction\n- id: fig2e-alignment-task-dependent\n  statement: Meta-learned corticothalamic weights align more with the readout direction than with the\n    leading PC in the motor control task, and more with the leading PC in the working memory task.\n  source: Results, Optimal corticothalamic connectivity improves learning performance, paragraph 4;\n    Figure 2E\n  quote: Whereas alignment with the readout direction was significantly greater than the alignment\n    with the leading PC in the motor control task ... this pattern was inverted for the working\n    memory task where in fact the corticothalamic weights were more strongly aligned with the\n    direction of the leading PC\n  statistics:\n  - about: motor control, readout against leading PC alignment\n    test: paired t test\n    p: 0.00016\n  - about: working memory, leading PC against readout alignment\n    test: paired t test\n    p: 0.0028\n  data: elsewhere\n  where: Not deposited; written from STAR Methods, Meta-learning and Alignment between weights\n  criterion: The meta-learned weights of fig2d-metalearned-error-reduction, one per initialization\n    (40); alignment of the optimized weight vector with W_O and with the leading eigenvector of the\n    cortical covariance, normalized by beta_0 (Results). Two-sided paired t test over runs in each\n    task. Reproduced when readout alignment exceeds PC alignment in motor control and PC exceeds\n    readout in working memory, each at p < 0.05.\n  depends_on:\n  - fig2d-metalearned-error-reduction\n- id: fig3ab-single-thalamic-neuron\n  statement: With one thalamic neuron, readout-aligned corticothalamic weights give the best learning\n    of motor control and PC-aligned weights the best learning of working memory.\n  source: Results, Subspace-aligned corticothalamic connectivity outperforms random corticothalamic\n    projection, paragraph 2; Figure 3A and 3B\n  quote: For autonomous control, aligning corticothalamic connectivity with the readout direction\n    yielded a substantial improvement over other strategies ( Figure 3A ). In contrast, the working\n    memory task benefited from aligning corticothalamic connectivity to the leading PC of cortical\n    activity\n  data: elsewhere\n  where: Not deposited; generated by the paper's model, github.com/kaushik-l/tc-learning at commit\n    2aa94dd (thalamocortical__motor.py, tc_type 'random', 'readout', 'pc', M = 1); the working memory\n    task written from STAR Methods\n  criterion: Models of STAR Methods, Subspace aligned models (random, PC with beta = 0.01, readout\n    with beta = 1), M = 1, N = 256, 40 initializations, basic tasks (motor c = 2, T = 20 tau;\n    working memory P = 8). Reproduced when the median 1 - R2 is lowest for readout in motor control\n    and lowest for PC in working memory. The code's update rates are run as a variant.\n- id: fig3cd-advantage-persists-with-m\n  statement: Performance improves with the number of thalamic neurons for all structures, and the\n    advantage of readout alignment (motor control) or PC alignment (working memory) persists for\n    relatively large M.\n  source: Results, Subspace-aligned corticothalamic connectivity outperforms random corticothalamic\n    projection, paragraph 3; Figure 3C and 3D\n  quote: Nonetheless, the advantage of aligning corticothalamic projections with the readout\n    direction (for autonomous control; Figure 3C ) or PC directions (for working memory; Figure 3D )\n    persists even when M is relatively large\n  data: elsewhere\n  where: Not deposited; generated by the paper's model (code at commit 2aa94dd for motor control);\n    the working memory task written from STAR Methods\n  criterion: As fig3ab-single-thalamic-neuron for M = 1, 2, 4, ..., 256 (Methods). \"Relatively large\"\n    is not defined; readings (a) up to M = 32 (the meta-learning model), (b) up to M = 128.\n    Reproduced when, under one reading, the predicted structure has the lowest median 1 - R2 at\n    every M up to the bound in both tasks, and the median of every structure falls with M.\n  depends_on:\n  - fig3ab-single-thalamic-neuron\n- id: fig3ef-task-type-not-complexity\n  statement: The best corticothalamic structure depends on the type of task and not on its\n    complexity; for the simplest tasks both structured models beat random by large factors (motor\n    2.6 PC, 2.7 readout; working memory 3.8 x 10^3 PC, 6.1 x 10^4 readout).\n  source: Results, Subspace-aligned corticothalamic connectivity outperforms random corticothalamic\n    projection, paragraph 4; Figure 3E and 3F\n  quote: We found that the choice of corticothalamic structure that maximized learning depends only\n    on the type of task being learned and not on task complexity ... median factor of reduction in\n    error relative to random connectivity\n  data: elsewhere\n  where: Not deposited; generated by the paper's model; written from STAR Methods, Task description\n  expected:\n  - quantity: simplest motor task, PC-aligned reduction factor\n    value: 2.6\n    tolerance: 0.26\n  - quantity: simplest motor task, readout-aligned reduction factor\n    value: 2.7\n    tolerance: 0.27\n  - quantity: simplest working memory task, PC-aligned reduction factor\n    value: 3800\n    tolerance: 380\n  - quantity: simplest working memory task, readout-aligned reduction factor\n    value: 61000\n    tolerance: 6100\n  criterion: Complexity varied as in STAR Methods (motor c = 1 to 5; working memory P = 1 to 16 on a\n    log scale, read as 1, 2, 4, 8, 16), M as in Figure 3A and 3B (M = 1, an assumption, as the\n    legend gives none), 40 runs. The simplest task is c = 1 and P = 1. Reproduced when the predicted\n    structure is best at every level above the simplest and the four factors (read as in\n    fig2d-metalearned-error-reduction) are within tolerance; partially reproduced when the ordering\n    holds but the factors do not.\n- id: fig4ab-network-size-compression\n  statement: The benefit of aligned corticothalamic weights is stable across cortical sizes up to\n    N = 2,048, and lowering the compression ratio from 100 to 10 gives only a modest drop in the\n    benefit.\n  source: Results, Subspace-aligned corticothalamic connectivity outperforms random corticothalamic\n    projection, paragraph 6; Figure 4A and 4B\n  quote: We found that the performance benefit of learning by preferentially aligning the\n    corticothalamic projections with the directions identified above was stable across different\n    sizes of the cortical network\n  data: elsewhere\n  where: Not deposited; written from STAR Methods, Models of distributed thalamic representation\n  criterion: N = 64 to 2,048 (powers of two), M = ceil(N/100) and ceil(N/10), rho = 1, readout\n    alignment for motor control and PC alignment for working memory, 40 runs; benefit (1 -\n    R0^2)/(1 - R2) (Figure 4 legend). Reproduced when the median benefit exceeds 1 at every N for\n    both ratios and both tasks.\n- id: fig4cd-partial-alignment\n  statement: Corticothalamic weights that carry only a fraction of the variance in the readout\n    direction or the leading PC still improve learning.\n  source: Results, Subspace-aligned corticothalamic connectivity outperforms random corticothalamic\n    projection, paragraph 6; Figure 4C and 4D\n  quote: we found that corticothalamic connectivity that communicates a fraction of variance in the\n    activity from the cortical subspaces identified above was sufficient to produce an improvement\n    in learning performance\n  data: elsewhere\n  where: Not deposited; written from STAR Methods, Models of distributed thalamic representation\n  criterion: N = 2,048, rho^2 varied from 0 to 1 (the grid is not given; 0, 0.1, 0.25, 0.5, 0.75, 1\n    used as a standard choice), compression ratio as in Figure 4C and 4D (not stated; 100 and 10\n    both run). Reproduced when the median 1 - R2 at some rho^2 below 1 is lower than at rho^2 = 0\n    in both tasks.\n- id: fig4ef-model-pcs-and-thalamus\n  statement: In the model the leading cortical PCs align with the readout in working memory, while in\n    motor control the readout aligns with low-variance PCs, so fewer cortical PCs explain thalamic\n    activity in working memory than in motor control.\n  source: Results, Subspace-aligned corticothalamic connectivity outperforms random corticothalamic\n    projection, paragraph 7; Figure 4E and 4F\n  quote: Accordingly, the leading PCs are substantially aligned with the readout direction in the\n    model trained on this task ( Figure 4E , blue). In contrast, the readout direction in the model\n    trained on motor control is mostly aligned with cortical PCs characterized by high frequency\n    fluctuations, which have low variance\n  data: elsewhere\n  where: Not deposited; written from STAR Methods and the Figure 4 legend\n  criterion: The trained models of fig4ab-network-size-compression at compression 100 (Figure 4\n    legend; N not stated, 2,048 used as in Figure 4C and 4D). Reproduced when the PC with the\n    largest alignment to the readout has a lower index in working memory than in motor control, and\n    the cumulative variance of thalamic activity explained by the top 5 PCs is higher in working\n    memory.\n  depends_on:\n  - fig4ab-network-size-compression\n- id: figs4ab-needs-thalamocortical-learning\n  statement: Structured corticothalamic weights give no benefit unless thalamocortical synapses are\n    learned.\n  source: Results, Subspace-aligned corticothalamic connectivity outperforms random corticothalamic\n    projection, paragraph 8; Figure S4A and S4B\n  quote: The benefits of optimized corticothalamic connectivity are not observed unless\n    thalamocortical synapses are learned\n  data: elsewhere\n  where: Not deposited; written from STAR Methods and the Figure S4 legend\n  criterion: A claim of absence with no test named. Models of fig3ab-single-thalamic-neuron with\n    thalamocortical weights fixed and readout weights learned (Figure S4 legend). Reproduced when\n    the structured and random models do not differ by a two-sided Wilcoxon rank-sum test at\n    p < 0.05 over the 40 runs, while with thalamocortical learning they do; the effect size is\n    reported.\n- id: figs4ef-noise-robustness\n  statement: The model with thalamocortical learning is more robust to noise in the initial cortical\n    state than a reservoir network that learns only readout weights.\n  source: Results, Subspace-aligned corticothalamic connectivity outperforms random corticothalamic\n    projection, paragraph 8; Figure S4E and S4F\n  quote: in contrast to a reservoir network where learning is limited to readout weights, the model\n    with thalamocortical learning is more robust to noise in the initial activity state of the\n    cortex\n  data: elsewhere\n  where: Not deposited; written from the Figure S4E and S4F legend\n  criterion: Initial state noise from U[-eps, +eps] (Figure S4 legend; the eps values are not given,\n    0.01, 0.1, 0.5 and 1 used). Reproduced when the median 1 - R2 of the thalamocortical model is\n    lower than that of the readout-only model at the largest eps in both tasks.\n- id: figs5ab-bptt-structure-irrelevant\n  statement: When thalamocortical synapses learn by BPTT instead of RFLO, the structure of\n    corticothalamic weights does not change performance much.\n  source: Results, Subspace-aligned corticothalamic connectivity outperforms random corticothalamic\n    projection, paragraph 9; Figure S5A and S5B\n  quote: when plasticity in thalamocortical synapses is implemented by BPTT instead of a three-factor\n    rule (RFLO), the structure of corticothalamic weights does not influence the learning\n    performance substantially\n  data: elsewhere\n  where: Not deposited; written from STAR Methods and the Figure S5 legend\n  criterion: The paper gives no threshold for \"substantially\". Reproduced when, with BPTT, the ratio\n    of median 1 - R2 between random and best structured weights is smaller than the same ratio with\n    RFLO, in both tasks.\n- id: figs5cd-thalamic-recurrence\n  statement: Recurrent excitation between thalamic neurons dampens the benefit of corticothalamic\n    structure.\n  source: Results, Subspace-aligned corticothalamic connectivity outperforms random corticothalamic\n    projection, paragraph 9; Figure S5C and S5D\n  quote: the benefit of corticothalamic structure is dampened in the presence of recurrent excitatory\n    connections between thalamic neurons\n  data: elsewhere\n  where: Not deposited; the paper does not give the model with thalamic recurrence beyond the Figure\n    S5 legend (f_thal, the fraction of thalamic neurons without recurrent input)\n  criterion: The recurrent thalamic weights are not specified in the paper; this claim cannot be\n    tested without choosing them, which the author records as methods_underspecified unless a\n    choice is defensible. If run, reproduced when the benefit (random over structured median error)\n    falls as f_thal decreases.\n- id: figs5ef-bptt-corticothalamic\n  statement: Models whose corticothalamic weights are updated by BPTT outperform models with fixed\n    corticothalamic weights of any structure.\n  source: Results, Subspace-aligned corticothalamic connectivity outperforms random corticothalamic\n    projection, paragraph 9; Figure S5E and S5F\n  quote: models in which corticothalamic weights are updated using BPTT outperform other models\n  data: elsewhere\n  where: Not deposited; written from the Figure S5 legend\n  criterion: Reproduced when the BPTT-corticothalamic model has the lowest median 1 - R2 in both\n    tasks.\n- id: figs5gh-corticocortical-learning\n  statement: Structured corticothalamic weights still beat random ones when corticocortical weights\n    also learn, provided corticocortical learning is slow relative to thalamocortical learning.\n  source: Results, Subspace-aligned corticothalamic connectivity outperforms random corticothalamic\n    projection, paragraph 9; Figure S5G and S5H\n  quote: models with structured corticothalamic weights outperform random models even in the\n    presence of corticocortical learning provided the latter is slow relative to thalamocortical\n    learning\n  data: elsewhere\n  where: Not deposited; written from the Figure S5 legend and Table S1\n  criterion: Corticocortical weights updated by RFLO (Table S1) at rates of 0.01, 0.1 and 1 times the\n    thalamocortical rate (the paper gives none). Reproduced when the normalized error (structured\n    over random) is below 1 at the slowest rate in both tasks.\n- id: fig5b-reaching-pc-prep-readout-exec\n  statement: In the delayed reaching task, the best model sends PCs to the thalamic nucleus active\n    during preparation and the readout to the nucleus active during execution, and it reaches all\n    targets well.\n  source: Results, Findings generalize to composite motor/memory task, paragraph 3; Figure 5B and 5C;\n    Figure S5J\n  quote: maximal performance was obtained in a model that conveyed PCs and readout signals to the\n    thalamic nucleus that engaged in learning during preparation and execution, respectively\n  data: elsewhere\n  where: Not deposited; generated by the paper's model, github.com/kaushik-l/tc-learning at commit\n    2aa94dd (thalamocortical__reaching.py with bptt__reaching.pt)\n  criterion: The reaching model of STAR Methods and the code (two thalamic modules of M = 2, eight\n    targets, go cue between 5 and 20 tau), the nine combinations of random, PC and readout for the\n    preparatory and execution modules, 40 runs each. Reproduced when PC (prep) with readout (exec)\n    has the lowest median 1 - R2 of the nine.\n- id: fig6-wm-choice-r2\n  statement: In the working memory task, ALM population activity explains the animal's choice well\n    (R2 = 0.97).\n  source: Results, Data are consistent with model predictions, paragraph 3\n  quote: We found that behavior was well explained by cortical activity in both tasks\n  expected:\n    quantity: test-set R2 of choice decoded from ALM activity\n    value: 0.97\n    tolerance: 0.097\n  criterion: Methods W1 to W7. R2 of the test-set c(t) predicted from the test-set h(t) with the\n    training-set weights, per session, and the mean over the five sessions; trial readings T1 and\n    T2. Reproduced when the value is within tolerance under one reading (the upper bound is 1).\n  depends_on:\n  - wm-sessions-link\n- id: fig6-motor-hand-r2\n  statement: In the reach-to-grasp task, motor cortex activity explains hand acceleration well\n    (R2 = 0.93).\n  source: Results, Data are consistent with model predictions, paragraph 3\n  quote: We found that behavior was well explained by cortical activity in both tasks\n  expected:\n    quantity: test-set R2 of hand acceleration decoded from motor cortex\n    value: 0.93\n    tolerance: 0.093\n  criterion: Not testable on DANDI:000009, which holds only the Guo et al. 2017 ALM and thalamus\n    recordings; the Sauerbrei et al. 2020 data are not deposited in any archive the paper names.\n- id: fig6c-wm-leading-pcs-drive-choice\n  statement: In the working memory task, the leading PCs of ALM activity have a large influence on the\n    readout of choice.\n  source: Results, Data are consistent with model predictions, paragraph 3; Figure 6C (blue)\n  quote: In mice performing the working memory task, leading PCs of the frontal cortex activity had a\n    large influence on the animal's behavioral choice\n  criterion: Methods W1 to W8; alignment of the readout with each of PCs 1 to 16 per session, mean\n    over the five sessions (Figure 6C, n = 5). The paper gives no threshold for \"leading\" or \"large\";\n    readings (a) the PC with the largest mean alignment is PC 1 or 2; (b) the mean alignment over\n    PCs 1 to 3 exceeds the mean over PCs 4 to 16. Reproduced when both hold under one trial reading,\n    partially reproduced when one holds.\n  depends_on:\n  - wm-sessions-link\n- id: fig6c-motor-low-variance-pcs\n  statement: In the reach-to-grasp task, hand movements are mainly driven by lower-variance PCs of\n    motor cortex activity, unlike the working memory task.\n  source: Results, Data are consistent with model predictions, paragraph 3; Figure 6C (red) and\n    Figure S6C\n  quote: In contrast, hand movements during the motor task were primarily influenced by PCs of lower\n    variance in the motor cortex\n  criterion: Not testable on DANDI:000009; the motor cortex data (Sauerbrei et al. 2020) are not\n    deposited in any archive the paper names.\n- id: figs6d-wm-thalamic-r2\n  statement: ALM activity explains 0.70 +/- 0.01 of the variance of VM/VAL thalamic neurons in the\n    working memory task.\n  source: Results, Data are consistent with model predictions, paragraph 5; Figure S6D\n  quote: We found that we could capture a substantial fraction of thalamic variance in both tasks,\n    although the fraction was higher in the working memory task\n  expected:\n    quantity: mean test-set R2 of thalamic units decoded from all ALM units\n    value: 0.70\n    tolerance: 0.01\n  criterion: Methods W1 to W6, W9 and W10, R2 from all cortical units of the reading of W9 (in P1,\n    53 units); mean over the 72 thalamic units. The tolerance is the paper's stated spread (taken as\n    the SEM). Reproduced when the mean is within tolerance under one combination of the T and P\n    readings; partially reproduced when the mean is between 0.6 and 0.8 under one.\n  depends_on:\n  - wm-sessions-link\n- id: figs6d-motor-thalamic-r2\n  statement: Motor cortex activity explains 0.46 +/- 0.01 of the variance of motor thalamus neurons\n    in the reach-to-grasp task.\n  source: Results, Data are consistent with model predictions, paragraph 5; Figure S6D\n  quote: We found that we could capture a substantial fraction of thalamic variance in both tasks\n  expected:\n    quantity: mean R2 of motor thalamus units decoded from motor cortex\n    value: 0.46\n    tolerance: 0.01\n  criterion: Not testable on DANDI:000009; the Sauerbrei et al. 2020 data are not deposited in any\n    archive the paper names.\n- id: fig6d-wm-top5-pcs\n  statement: In the working memory task, the top 5 ALM PCs capture 0.63 +/- 0.04 of the explainable\n    variance of thalamic neurons.\n  source: Results, Data are consistent with model predictions, paragraph 5; Figure 6D (blue)\n  quote: The fraction of explainable variance in thalamus captured by the top 5 cortical PCs was\n    significantly greater during the working memory task than motor control\n  expected:\n    quantity: mean normalized R2(5) over thalamic units, working memory\n    value: 0.63\n    tolerance: 0.04\n  criterion: Methods W1 to W6, W9 and W10, with k = 5; mean over the 72 thalamic units. The\n    tolerance is the paper's stated spread. Reproduced when the mean is within tolerance under one\n    combination of the T, P and N readings; the values under every combination are shown.\n  depends_on:\n  - wm-sessions-link\n- id: fig6d-motor-top5-pcs\n  statement: In the reach-to-grasp task, the top 5 motor cortex PCs capture 0.29 +/- 0.02 of the\n    explainable variance of motor thalamus neurons.\n  source: Results, Data are consistent with model predictions, paragraph 5; Figure 6D (red)\n  quote: The fraction of explainable variance in thalamus captured by the top 5 cortical PCs was\n    significantly greater during the working memory task than motor control\n  expected:\n    quantity: mean normalized R2(5) over thalamic units, motor control\n    value: 0.29\n    tolerance: 0.02\n  criterion: Not testable on DANDI:000009; the Sauerbrei et al. 2020 data are not deposited in any\n    archive the paper names.\n- id: fig6d-more-pcs-in-motor-task\n  statement: More cortical PCs are needed to explain thalamic activity in the motor control task than\n    in the working memory task, as the model predicts.\n  source: Results, Data are consistent with model predictions, paragraph 5; Figure 6D, Figure S6E\n    and S6F\n  quote: Consistent with the model prediction ( Figures 4E and 4F ), we found that more PCs are\n    needed to explain thalamic activity during the motor control task than in working memory task\n  criterion: Needs both datasets; the motor data are not deposited in any archive the paper names,\n    so this comparison cannot be tested on DANDI:000009. The paper calls the top-5 difference\n    significant but names no test. The working memory half is tested in fig6d-wm-top5-pcs.\n  depends_on:\n  - fig6d-wm-top5-pcs\n  - fig6d-motor-top5-pcs\n- id: fig6e-motor-single-trial\n  statement: In the motor task, thalamic activity on a trial is better predicted by cortical activity\n    from the same trial than by shuffled trials, and corticothalamic weights fit to single trials are\n    better aligned with the readout than those fit to trial averages, suggesting the motor thalamus\n    receives an efference copy.\n  source: Results, Data are consistent with model predictions, paragraph 6; Figure 6E\n  quote: We found that thalamic activity on any given trial was substantially better predicted by\n    cortical activity in the same trial ... corticothalamic weights that capture trial-by-trial\n    activity in thalamic neurons were better aligned with the readout weights than those that\n    capture only trial-averaged thalamic activity\n  criterion: Not testable on DANDI:000009; the Sauerbrei et al. 2020 simultaneous recordings are not\n    deposited in any archive the paper names.\n- id: figs6f-ct-alignment-not-significant\n  statement: For individual thalamic neurons, the difference between the alignment of corticothalamic\n    weights with the leading cortical PC and with the readout direction is not significant in either\n    dataset (one-sided paired t tests, p = 0.09 and p = 0.17).\n  source: Figure S6F\n  inferred: The legend says only that statistics of a one-sided paired t-test are shown; the values\n    P=0.09 and P=0.17 are figure labels in the supplement text, and the figure could not be rendered\n    to see which task each belongs to (the label order suggests 0.09 for motor control and 0.17 for\n    working memory).\n  statistics:\n  - about: one task (label order suggests motor control)\n    test: one-sided paired t test\n    p: 0.09\n  - about: the other task (label order suggests working memory)\n    test: one-sided paired t test\n    p: 0.17\n  criterion: A claim of absence, judged on the paper's test for the working memory data. Methods W1\n    to W10; corticothalamic weights of each thalamic unit from the regression on all 16 PCs, mapped\n    back to unit space (w U_1:16^T); alignment with PC 1 and with the session-averaged readout\n    direction as |cos| (Methods, Alignment between weights). The paper does not state the direction\n    of the one-sided test; it is taken as PC greater than readout, the model's prediction for working\n    memory (Results). Reproduced when the one-sided paired t test over the 72 units gives p >= 0.05;\n    the p-value and the mean difference are reported, and compared with 0.17 and 0.09.\n  depends_on:\n  - wm-sessions-link\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/lakshminarasimhan-2024.yaml",
 "old_string": "alignment with PC 1 and with the session-averaged readout\n    direction as |cos|",
 "new_string": "alignment with PC 1 and with the readout direction (W7)\n    estimated on the same cortical population, as |cos|"
}
```

```
The file claims/lakshminarasimhan-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/lakshminarasimhan-2024.yaml paper/10.1016-j.celrep.2024.114059.txt; echo EXIT $?; grep -nE '^\s+[a-z_]+: .*[^"]: ' claims/lakshminarasimhan-2024.yaml | grep -v "^\s*#" | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/lakshminarasimhan-2024.yaml",
 "old_string": "    ; median factor of reduction in error: motor control, 5.8; working memory, 5.1)",
 "new_string": "    ; median factor of reduction in error ... motor control, 5.8; working memory, 5.1)"
}
```

```
The file claims/lakshminarasimhan-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/lakshminarasimhan-2024.yaml paper/10.1016-j.celrep.2024.114059.txt; echo EXIT $?
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/lakshminarasimhan-2024.yaml",
 "old_string": "    large influence on the animal's behavioral choice",
 "new_string": "    large influence on the animal ... behavioral choice"
}
```

```
The file claims/lakshminarasimhan-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/lakshminarasimhan-2024.yaml paper/10.1016-j.celrep.2024.114059.txt; echo EXIT $?
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/lakshminarasimhan-2024.yaml",
 "old_string": "# figure was read; numbers shown only in figures are taken from the text labels where noted.",
 "new_string": "# figure was read; numbers shown only in figures are taken from the text labels where noted. The\n# p-values of fig2e-alignment-task-dependent are printed with garbled glyphs (\"1.6 √ó 10 ‚àí4\" and\n# \"2.8 √ó 10 ‚àí3\"), so the quote checker does not find them; they were confirmed by reading."
}
```

```
The file claims/lakshminarasimhan-2024.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/lakshminarasimhan-2024.yaml paper/10.1016-j.celrep.2024.114059.txt | tail -1; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/lakshminarasimhan-2024.yaml`. The quote checker passes every quote. It still reports two problems, both p-values whose printed form is garbled; I checked them by reading the text. Nothing is committed.

**Text read**
- The header calls the text the "version of record", but the body is the NIH author manuscript in PubMed Central (PMC11104520, NIHMS1988710). It includes the main text, STAR Methods, the Figure 1 to 6 legends and the key resources table.
- The supplement is appended to the same file (mmc2.pdf, pages 22 to 32): the Figure S1 to S6 legends and Table S1.
- I could not open the PDF because no PDF renderer is installed here, so I read no figures. The two Figure S6F p-values come from the figure labels that survive in the extracted text.
- Code: github.com/kaushik-l/tc-learning at commit 2aa94dd. It only holds simulation code for the motor and reaching tasks. There is no working-memory task, no meta-learning and no analysis of the neural data. Where the code differs from the Methods (update rates, how feedback weights are set up), the claims follow the Methods and treat the code's choice as a variant.

**Counts**
- 32 claims: one link claim and 31 findings. 31 have quotes; one has an `inferred` note.
- 30 claims have criteria. 9 have expected values. Two record statistics, four values in all: the Figure 2E paired t tests (p = 1.6e-4 and 2.8e-3) and the Figure S6F one-sided paired t tests (p = 0.09 and 0.17).
- Data:
  - **Model simulations, 20 claims:** marked `elsewhere`, with the code repository and commit as the source.
  - **Testable on DANDI:000009, 6 claims:** the session link, choice R² (0.97), leading PCs driving the choice readout, thalamic R² (0.70 ± 0.01), top-5 PC fraction (0.63 ± 0.04), and the Figure S6F alignment test.
  - **Not testable, 6 claims:** they rest on the Sauerbrei et al. 2020 motor data.

**Details the paper leaves open, and the readings named**
- **Which units count:** all sorted units, or Guo et al.'s well-isolated single units. Use whichever gives 151 ALM and 72 thalamic units in five sessions from one mouse.
- **Photoinhibition trials:** (T1) correct trials without photostimulation; (T2) all correct trials.
- **Cortical population for the thalamic regressions:** (P1) the 151 ALM units pooled, then subsampled to 53, as the Figure S6 legend says; (P2) pooled, no subsampling; (P3) only the ALM units from the thalamic unit's own session.
- **How R²(k) is normalized:** (N1) R²(k)/R²(16), as in the Methods; (N2) R²(k) over the R² from all cortical units, as in the Results; (N3) each neuron's curve rescaled to 0 to 1, as in the Figure 6D legend.
- **Fixed as standard choices:** the time bin, the grid for the smoothing width σ, and the random seed for the 80/10/10 split. Since the split seed may affect results, the criteria also ask for the mean over 10 splits.
- **"Leading PCs have a large influence" (Figure 6C):** no threshold is given. (a) The best-aligned PC is PC 1 or 2; (b) the mean alignment of PCs 1 to 3 exceeds that of PCs 4 to 16.
- **Figure S6F:** the direction of the one-sided test and which p-value goes with which task are not stated. The label order suggests 0.09 is motor and 0.17 is working memory.
- **Meta-learned error-reduction factors:** the median of the per-run ratios, or the ratio of the medians.
- **Unstated simulation settings:** the corticothalamic learning rate, the noise ε values, the ρ² grid, the corticocortical rates, and the M used for the task-complexity runs. Standard values are named in the criteria.
- **Thalamic recurrent weights (Figure S5C and S5D):** not specified anywhere. That claim may have to be blocked as `methods_underspecified`.

**Missing from the paper**
- The paper names no deposit for the Sauerbrei et al. 2020 motor cortex and motor thalamus data. The six claims on them cannot be tested, including the cross-task comparison in Figure 6D.
- No simulation outputs are deposited, and the linked code has no working-memory or meta-learning code. Those claims have to be rebuilt from the Methods.

## End of run

37 turns, 5 minutes, $2.16 at API prices, result: success.
