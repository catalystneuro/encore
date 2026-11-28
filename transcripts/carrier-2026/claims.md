# carrier-2026 · claims · run 45663751456

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ claims/
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
3	Version: `pilot-19`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
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

**Agent calls Read**

```json
{
 "file_path": "claims/fouke-2025.yaml"
}
```

```
1	# Claims for Fouke, He, Loring & Naumann (2025) on dandiset 001453.
2	# Source: the accepted author manuscript in PubMed Central (PMC12218792), full text, read
3	# from its Results, figure legends and STAR Methods. The version of record is not open access.
4	#
5	# When these criteria were written, the author had seen the data check only: the file list,
6	# subject metadata, frame rates, units, trial structure and stimulus codes of every file, and
7	# the extent of positions. No claim's analysis had been run. The author had also read the
8	# outputs printed in the paper's own analysis notebook (Fig1-S1.ipynb, GitLab commit 33a5c29),
9	# which include per-stimulus median speeds and angular velocities and its statistics.
10	#
11	# The dandiset holds only the freely swimming tracking data of Figure 1 and Figure S1. Its
12	# stimulus codes 0 to 20 carry no names. The names come from the paper's code and from the
13	# stimulus software's protocol file (see stimulus-code-link), so the claims that need them
14	# use outside data and depend on that claim.
15	#
16	# Method choices fixed here, from the paper's Fig1-S1.ipynb where the Methods are silent: a
17	# trial is one stim_index; tracked frames only; positions smoothed with a Savitzky-Golay filter
18	# (21 frames, order 2); trials rejected when the absolute cumulative heading change exceeds
19	# 1000 degrees in the first 10 s or 2000 degrees in the first 35 s, or the mean speed exceeds
20	# 100 mm/s; measures taken from 3 s to 35 s after the first frame (the 3 s stationary phase is
[... 302 more lines not kept]
```

**Agent calls Bash**

```bash
cat papers/datasets/carrier-2026.yaml; grep -l "datasets:" claims/*.yaml | head -3; wc -l paper/*.txt; head -30 paper/*.txt; ls tools; ls datasets 2>/dev/null | grep zenodo-17
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -40 claims/du-2026.yaml; grep -n "datasets:" -A3 claims/du-2026.yaml | head -20; ls datasets/ | grep -i zenodo-1779; ls datasets/zenodo-17624449 datasets/zenodo-17794764 2>/dev/null
```

```
Exit code 2
# Claims for Du, Lai, Hu & Ye (2026), "A Context-Conditional Audit of Trial-Pairing-Dependent
# Neural Gain in Motor-Cortex Decoding", bioRxiv doi:10.64898/2026.08.04.742876, tested on
# DANDI:001201 (LINK) and DANDI:000129 (MC_RTT).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-21,
# protocol as stated in docs/protocol.md (version pilot-18, Reader).
#
# Text read. The bioRxiv preprint posted August 10, 2026 (a Journal of Neural Engineering
# submission), full text in paper/10.64898-2026.08.04.742876.txt: main text, figure legends,
# Tables 1 to 3, Methods, Data and Code availability. No PDF was supplied. The paper's
# Supplementary information (formal properties, complete ladder results, replacement
# diagnostics, confirmation details, nonlinear-map seeds, temporal and capacity sensitivities)
# is not under paper/ and is not in the code release; every claim below rests on numbers the
# main text or its tables state. The one main-text sentence that points to supplement values
# (replacement ranks one to five) is a claim judged by sign alone (replacement-ranks-lower).
#
# Code read. github.com/gwkuqgfkqe/neural-decoder-context-audit, tag v1.0-jne-submission,
# commit b042fbe1cda2ca5a353751c693d7c95f45de0456 (Code availability names this release). It
# holds the loaders (src/neural_evidence/link.py, mc_rtt.py, mc_maze.py), the fully nested and
# nonlinear estimators (nested_estimators.py), the synthetic generator (synthetic.py), run
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 40,120p claims/du-2026.yaml | grep -n "^[a-z]" ; grep -n "^[a-z_]*:" claims/du-2026.yaml | head; grep -rl "17624449\|17794764" --include=*.yaml --include=*.json . 2>/dev/null | head
```

```
63:schema_version: 2
64:paper: doi:10.64898/2026.08.04.742876
65:claims:
102:schema_version: 2
103:paper: doi:10.64898/2026.08.04.742876
104:claims:
1071:checks:
./targets/zenodo.json
./papers/match/zenodo-17624449.yaml
./papers/match/zenodo-17794764.yaml
./papers/manifest.yaml
./papers/datasets/carrier-2026.yaml
```

**Agent calls Bash**

```bash
cat papers/match/zenodo-17624449.yaml papers/match/zenodo-17794764.yaml; python -c "
import json;d=json.load(open('targets/zenodo.json'))
items=d if isinstance(d,list) else d.get('targets',d)
for t in (items if isinstance(items,list) else items.values()):
  s=json.dumps(t)
  if '17624449' in s or '17794764' in s: print(s[:3000])
"
```

```
# Whether each paper Zenodo:17624449 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: zenodo
  id: '17624449'
date: '2026-11-25'
papers:
- doi: 10.1152/jn.00294.2025
  relation: given
  checks:
    text: true
    title_in_text: true
    names_this: true
    names_others:
    - Zenodo:17794764
  verdict: partial
  by: agent
  reason: The paper splits its data across two Zenodo records. This one holds all lobster and about half of the crab isolated STNS recordings with the analysis files; the other crab STNS recordings and all in vivo PPG recordings (the in vivo salinity results) are in Zenodo 17794764.
  evidence:
  - source: Data availability
[... 32 more lines not kept]
```

**Agent**

Now reading the paper text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00294.2025.txt",
 "offset": 30,
 "limit": 520
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00294.2025.txt",
 "offset": 550,
 "limit": 560
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00294.2025.txt",
 "offset": 1109,
 "limit": 60
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -in "supplement" paper/*.txt | head; python -c "
import json;d=json.load(open('targets/zenodo.json'))
items=d if isinstance(d,list) else d.get('targets',d)
for t in (items if isinstance(items,list) else items.values()):
  if t.get('id') in ('17624449','17794764'):
    print(t['id'],[ (f['path'],f['size']) for f in t['files']], t.get('code'))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1152-jn.00294.2025.pdf')
for p in (9,14):
  d[p].get_pixmap(dpi=110).save(f'p{p+1}.png')
print('ok')"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && (which pdftoppm && pdftoppm -f 10 -l 10 -r 100 -png paper/10.1152-jn.00294.2025.pdf p && pdftoppm -f 15 -l 15 -r 100 -png paper/10.1152-jn.00294.2025.pdf p; ls)
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1152-jn.00294.2025.pdf",
 "pages": "15"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -rn -B2 -A2 "± SD\|the stated SD\|SD as" claims/*.yaml | grep -i "tolerance\|reason" | head -15
```

```
claims/armstrong-2026.yaml-282-  - {quantity: running speed, value: 21, tolerance: 4, unit: cm/s}
claims/armstrong-2026.yaml-373-  - {quantity: whisking frequency, value: 15, tolerance: 2, unit: Hz}
claims/armstrong-2026.yaml-394-  - {quantity: mean first touch time, value: 0.06, tolerance: 0.03, unit: s}
claims/armstrong-2026.yaml-677-  - {quantity: mean ramp slope over animals, value: 13.05, tolerance: 4.59}
claims/armstrong-2026.yaml-760-  - {quantity: mean streak index, value: 0.06, tolerance: 1.36}
claims/asari-2009.yaml-156-    tolerance: 0.08
claims/asari-2009.yaml:157:  criterion: Tolerances are the stated SDs, as the paper gives them as the spread of the values
claims/bellvila-2026.yaml-967-    tolerance: 3.05e-05
claims/bellvila-2026.yaml:969:    in 1-min windows every 10 min of the sham recording; tolerances the stated SD. Open
claims/daume-2024.yaml:164:    tolerances are the standard errors of the mean (the stated SD over the square root of 46), since
claims/daume-2024.yaml:793:  - Open, behaviour-overall-accuracy and ltm-rt-confidence. Tolerances are the SEM derived from the stated SD and n, with a reason given, where the protocol names the stated spread; kept, since these are means of the same sessions, but a reviewer may prefer the SD.
claims/elie-2019.yaml-190-    tolerance: 1.6
claims/elie-2019.yaml:192:  criterion: Tolerances on the two percentages are the stated SDs (protocol). Coherence, per unit
claims/guo-2017.yaml:966:    (readings R1, R2). Tolerances are 10% of the values, as the stated SDs describe spread over units,
claims/guo-2017.yaml-967-    not uncertainty of the mean. Reproduced when all values are within tolerance under one reading.
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

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps({k:v for k,v in s['properties'].items()},indent=0)[:2500])
c=s.get('\$defs',s.get('definitions',{}))
print(list(c))
"
```

```
{
"schema_version": {
"const": 2
},
"dataset": {
"description": "Before the cutover to paper-first records, the dataset a per-dataset claims file was read for. A paper's own claims file (claims/<paper>.yaml) leaves it out.",
"type": "object",
"additionalProperties": false,
"required": [
"archive",
"id"
],
"properties": {
"archive": {
"description": "The archive that holds the dataset, in lower case: dandi, ebrains, openneuro, dryad, zenodo, figshare and so on.",
"type": "string",
"pattern": "^[a-z][a-z0-9-]*$"
},
"id": {
"description": "The dataset's identifier in that archive, e.g. 000003 on DANDI.",
[... 71 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'))
p=s['properties']['claims']['items']['properties']
for k,v in p.items(): print(k, v.get('type'), v.get('enum',''), (v.get('items') or {}).get('pattern',''))
print(json.dumps(s['\$defs'],indent=0)[:2500])
print([k for k in s['properties']])
"
```

```
id string  
statement string  
source string  
kind None ['finding', 'link'] 
quote string  
inferred string  
expected None  
statistics array  
criterion string  
depends_on array  ^[a-z0-9]+(-[a-z0-9]+)*$
data None ['dataset', 'with_labels', 'with_inputs', 'elsewhere'] 
where string  
datasets array  
{
"expected": {
"type": "object",
"additionalProperties": false,
"required": [
"quantity",
"value"
[... 96 more lines not kept]
```

**Agent**

I have the full text (version of record, no supplement referenced, no separate code repository). Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/carrier-2026.yaml",
 "content": "# Claims for Carrier, Romano, Scaria, Palmer, O'Leary, Marder & Powell (2026), \"The combined\n# effects of temperature and salinity on the stomatogastric nervous system of two species of\n# decapod crustacea\", J Neurophysiol 135: 797-814, doi:10.1152/jn.00294.2025, tested on\n# Zenodo:17624449 (Part I, folder zenodo-17624449) and Zenodo:17794764 (Part II, folder\n# zenodo-17794764).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-25,\n# protocol as stated in docs/protocol.md (version pilot-19, Reader).\n#\n# Text read. The version of record (J Neurophysiol PDF, CC-BY 4.0), full text in\n# paper/10.1152-jn.00294.2025.txt: main text, Methods, figure legends 1 to 9, Table 1, Data\n# availability. The paper has no supplement and cites none. The PDF could not be rendered in this\n# run, so the bar heights of Figures 1E, 4E and 9 (percentages) were not read; only the numbers\n# the text states are used.\n#\n# Code read. None. The paper links no code repository; Data availability says \"All data and\n# custom analysis scripts\" are in the two Zenodo records. The archive's file lists show no\n# separate script files, so any scripts sit inside the data archives, which a reader does not\n# open. Burst detection, frequency and phase were computed with \"custom Spike2 (CED) or MATLAB\n# (MathWorks) scripts\" (Methods, Data Analysis and Statistics); regressions and t tests in\n# GraphPad Prism; mixed-effects models of frequency in R (lme4, lmerTest); in vivo spectrograms\n# with MATLAB scripts by Ekaterina Morozova (ref. 56). None of these scripts is given in the paper.\n#\n# The datasets, from their archive descriptions. Part I (zenodo-17624449) holds the raw data from\n# all dissected lobster (H. americanus) nervous systems and half of the crab (C. borealis)\n# nervous systems, with \"meta data used to create the plots and graphs\" (Excel, Prism, MATLAB and\n# CSV files). Part II (zenodo-17794764) holds the other half of the crab nervous systems and all\n# in vivo recordings of both species. So claims on isolated crab STNS rest on both folders, claims\n# on isolated lobster STNS on zenodo-17624449, claims comparing the two species on both, and in\n# vivo claims on zenodo-17794764.\n#\n# Data the paper used, as it reports them.\n# - Animals. Adult male C. borealis (Jonah crab), August 2022 to February 2024, kept at about\n#   11 C. Adult male and female H. americanus (American lobster), Summer 2021 to April 2024, kept\n#   at about 10 C. n is one animal or one nervous system.\n# - Isolated STNS, extracellular recordings of the lvn (PD, LP, PY), pdn (PD) and pyn (PY),\n#   digitised at 10 kHz (Micro 1401 with Spike2, or Digidata 1440 with pClamp).\n# - Salinity series at 10 C. 30 min baseline in 1x saline, then sequential 15-min applications of\n#   1.25x, 1.5x, 1.75x (increasing) or 0.75x, 0.5x, 0.25x (decreasing), stopping at the first\n#   crash. 0.25x only in initial experiments (n = 3). Crab preparations received both series\n#   (with 1 h of 1x between); lobster preparations one series each (separate sets).\n# - Temperature ramps. From 10 C in 2 C steps every 2 min until crash, then cooled. Combined\n#   experiments: 15 min at 10 C in 1x, 15 min in 0.75x or 1.25x, ramp; 15 min recovery at 10 C,\n#   then the other altered saline; order counterbalanced. Within-preparation 1x ramps serve as\n#   controls.\n# - Measured variables. PD burst frequency (pyloric frequency) from the final 30 s of each saline\n#   application or each 2-min temperature step; crash temperature of the rhythm (two of three\n#   pyloric neurons no longer bursting) and of each neuron; phases of PD off, LP on and off, PY on\n#   and off over ten cycles per step (lobster only).\n# - In vivo. PPG sensor (AMP03) over the pylorus, digitised at 5 kHz (Digidata 1440, pClamp).\n#   Animals moved from 1x artificial seawater (30-34 ppt, 10-12 C) to 0.75x, 0.5x, 0.25x, 1.25x,\n#   1.5x or 1.75x for 1 h; also 2.5 h (n = 6, not shown) and 15 h (n = 5) exposures with mortality\n#   counted.\n#\n# Method details used throughout, from the Methods.\n# - Q10. Pyloric frequency F against temperature T on a semi-log plot, m = dlogF/dT from a\n#   \"nonlinear regression\" in Prism, Q10 = 10^(10m), with a 95% CI. Slopes of two groups compared\n#   with Fisher's extra-sum-of-squares F test; a single group compared with zero slope. Open, and\n#   named in each Q10 claim: (Q-a) a least-squares fit of the semi-log (exponential) model\n#   F = 10^(mT + b) on untransformed frequency, as Prism's semi-log nonlinear model does, or\n#   (Q-b) a linear fit of log10 F on T; and whether the extra-sum-of-squares test shares only the\n#   slope (separate intercepts, the usual Prism comparison) or slope and intercept. The degrees of\n#   freedom the paper prints (for example F(1,171) with n = 11 over 10 to 24 C) fit a regression on\n#   every preparation's value at every step, not on step means, except Fig. 3B (F(1,8)).\n# - Crash. \"the point at which two of the three pyloric motor neurons failed to rhythmically\n#   burst\" (Methods); a neuron's crash is the loss of its bursts in the extracellular recording.\n#   The crash temperature is the ramp step at which this is seen (Fig. 2A, \"At 26 C, this\n#   preparation crashed\"). The burst detection criteria are not given (open); the analysis files\n#   the Part I description lists may hold the authors' per-preparation values.\n# - Frequency. PD burst frequency over the final 30 s of the step. Whether it is the mean of\n#   1/period over cycles or the number of bursts over 30 s is not given (open; a standard choice,\n#   mean of 1/period, both shown).\n# - Two-sample tests. Shapiro-Wilk normality, then paired or Welch t test, or Wilcoxon signed-rank\n#   or Mann-Whitney U (alpha 0.05), as each claim names.\n# - Tolerances. Means are reported as mean plus or minus SD across preparations. The SD is the\n#   spread of preparations, not the uncertainty of the mean, so tolerances on means are the SEM\n#   computed from the stated SD and n (rounded up to two decimals). Q10 tolerances are half the\n#   width of the paper's 95% CI, and a Q10 also holds when it falls inside the printed CI.\n#\n# Inconsistencies in the text, named in the claims they touch: Fig. 4B legend n = 8, Results\n# n = 9; Fig. 4D legend says \"1x and 0.75x\" for the 1.25x comparison and P = 0.8, Results P = 0.9;\n# Fig. 3C legend says PY-off phase changed with temperature, Results and Table 1 say PY-on; Fig. 9\n# legend puts crabs in panel A, the Results put lobsters in 9A; the Fig. 2 summary paragraph says\n# 1.25x saline decreased pyloric frequency (Fig. 2F), the paragraph above says frequency rose\n# similarly; crab crash temperatures in 1x saline are given as 29.3 (n = 11), 31.3 (n = 9) and\n# 30.21 C (n = 21) for different sets.\nschema_version: 2\npaper: doi:10.1152/jn.00294.2025\nclaims:\n- id: fig1b-cb-075-frequency-unchanged\n  statement: In the isolated C. borealis STNS at 10 C, lowering saline from 1x to 0.75x does not\n    change pyloric frequency (1.18 against 1.18 Hz, paired t test P = 0.8, n = 10).\n  source: Results, The C. borealis Pyloric Rhythm Is Maintained across a Range of Salinity,\n    paragraph 2; Figure 1B\n  quote: B:\\ the pyloric rhythm frequency was similar in 1\n  inferred: placeholder\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/carrier-2026.yaml",
 "content": "# Claims for Carrier, Romano, Scaria, Palmer, O'Leary, Marder & Powell (2026), \"The combined\n# effects of temperature and salinity on the stomatogastric nervous system of two species of\n# decapod crustacea\", J Neurophysiol 135: 797-814, doi:10.1152/jn.00294.2025, tested on\n# Zenodo:17624449 (Part I, folder zenodo-17624449) and Zenodo:17794764 (Part II, folder\n# zenodo-17794764).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-25,\n# protocol as stated in docs/protocol.md (version pilot-19, Reader).\n#\n# Text read. The version of record (J Neurophysiol PDF, CC-BY 4.0), full text in\n# paper/10.1152-jn.00294.2025.txt: main text, Methods, figure legends 1 to 9, Table 1, Data\n# availability. The paper has no supplement and cites none. The PDF could not be rendered in this\n# run, so the bar heights of Figures 1E, 4E and 9 (percentages) were not read; only the numbers\n# the text states are used.\n#\n# Code read. None. The paper links no code repository; Data availability says \"All data and\n# custom analysis scripts\" are in the two Zenodo records. The archives' file lists show no\n# separate script files, so any scripts sit inside the data archives, which a reader does not\n# open. Burst detection, frequency and phase were computed with \"custom Spike2 (CED) or MATLAB\n# (MathWorks) scripts\" (Methods, Data Analysis and Statistics); regressions and two-sample tests\n# in GraphPad Prism; mixed-effects models of frequency in R (lme4, lmerTest); in vivo spectrograms\n# with MATLAB scripts by Ekaterina Morozova (ref. 56). The paper gives none of these scripts.\n#\n# The datasets, from their archive descriptions. Part I (zenodo-17624449) holds the raw data from\n# all dissected lobster (H. americanus) nervous systems and half of the crab (C. borealis)\n# nervous systems, with \"meta data used to create the plots and graphs\" (Excel, Prism, MATLAB and\n# CSV files). Part II (zenodo-17794764) holds the other half of the crab nervous systems and all\n# in vivo recordings of both species. So claims on isolated crab STNS rest on both folders, claims\n# on isolated lobster STNS on zenodo-17624449, claims comparing the two species on both, and in\n# vivo claims on zenodo-17794764.\n#\n# Data the paper used, as it reports them.\n# - Animals. Adult male C. borealis (Jonah crab), August 2022 to February 2024, kept at about\n#   11 C. Adult male and female H. americanus (American lobster), Summer 2021 to April 2024, kept\n#   at about 10 C. n is one animal or one nervous system.\n# - Isolated STNS, extracellular recordings of the lvn (PD, LP, PY), pdn (PD) and pyn (PY),\n#   digitised at 10 kHz (Micro 1401 with Spike2, or Digidata 1440 with pClamp).\n# - Salinity series at 10 C. 30 min baseline in 1x saline, then sequential 15-min applications of\n#   1.25x, 1.5x, 1.75x (increasing) or 0.75x, 0.5x, 0.25x (decreasing), stopping at the first\n#   crash. 0.25x only in initial experiments (n = 3). Crab preparations received both series\n#   (with 1 h of 1x between); lobster preparations one series each (separate sets).\n# - Temperature ramps. From 10 C in 2 C steps every 2 min until crash, then cooled. Combined\n#   experiments: 15 min at 10 C in 1x, 15 min in 0.75x or 1.25x, ramp; 15 min recovery at 10 C,\n#   then the other altered saline; order counterbalanced. Within-preparation 1x ramps serve as\n#   controls.\n# - Measured variables. PD burst frequency (pyloric frequency) from the final 30 s of each saline\n#   application or each 2-min temperature step; crash temperature of the rhythm and of each\n#   neuron; phases of PD off, LP on and off, PY on and off over ten cycles per step (lobster\n#   only).\n# - In vivo. PPG sensor (AMP03) over the pylorus, digitised at 5 kHz (Digidata 1440, pClamp).\n#   Animals moved from 1x artificial seawater (30 to 34 ppt, 10 to 12 C) to 0.75x, 0.5x, 0.25x,\n#   1.25x, 1.5x or 1.75x for 1 h; also 2.5 h (n = 6, not shown) and 15 h (n = 5) exposures, with\n#   deaths counted after 15 h.\n#\n# Method details used throughout, from the Methods.\n# - Q10. Pyloric frequency F against temperature T on a semi-log plot, m = dlogF/dT from a\n#   \"nonlinear regression\" in Prism, Q10 = 10^(10m), with a 95% CI. Slopes of two groups compared\n#   with Fisher's extra-sum-of-squares F test; a single group compared with zero slope. Open, and\n#   named in each Q10 claim: (Q-a) a least-squares fit of the semi-log model F = 10^(mT + b) on\n#   untransformed frequency, as Prism's semi-log nonlinear model does, or (Q-b) a linear fit of\n#   log10 F on T. The F test compares a model with one shared slope (separate intercepts) against\n#   separate slopes; the paper says it compares slopes, so the intercepts are left free. The\n#   degrees of freedom printed (for example F(1,171) with n = 11 over 10 to 24 C) fit a regression\n#   on every preparation's value at every step, not on step means; Fig. 3B (F(1,8)) is the\n#   exception, named in its claim.\n# - Crash. \"the point at which two of the three pyloric motor neurons failed to rhythmically\n#   burst\" (Methods); a neuron's crash is the loss of its bursts in the extracellular recording.\n#   The crash temperature is the ramp step at which this is seen (Fig. 2A, \"At 26 C, this\n#   preparation crashed\"). The burst detection criteria are not given (open); the analysis files\n#   the Part I description lists may hold the authors' per-preparation values, which are the\n#   paper's own reading of the recordings.\n# - Frequency. PD burst frequency over the final 30 s of the step. Whether it is the mean of\n#   1/period over the cycles or the number of PD bursts over 30 s is not given (open; it cannot\n#   change a mean by much, so mean of 1/period is the standard choice and the count is shown).\n# - Two-sample tests as each claim names (Shapiro-Wilk first, then paired or Welch t test,\n#   Wilcoxon signed-rank or Mann-Whitney U, alpha 0.05).\n# - Tolerances. Means are printed as mean plus or minus SD across preparations. The SD is the\n#   spread of preparations, not the uncertainty of the mean, so tolerances on means are the SEM\n#   computed from the stated SD and n, rounded up to two decimals. Q10 tolerances are half the\n#   width of the paper's 95% CI, and a Q10 also holds when it falls inside the printed CI.\n#\n# Inconsistencies in the text, named in the claims they touch: Fig. 4B legend n = 8, Results\n# n = 9; Fig. 4D legend labels the 1.25x comparison \"1x and 0.75x\" and gives P = 0.8, Results\n# P = 0.9; Fig. 3C legend says the PY-off phase changed with temperature, Results and Table 1 say\n# PY-on; the Fig. 9 legend puts crabs in panel A, the Results put lobsters in 9A; the Fig. 2\n# summary paragraph says 1.25x saline decreased pyloric frequency (Fig. 2F), the paragraph that\n# presents Fig. 2F says frequency rose similarly; crab crash temperatures in 1x are given as 29.3\n# (n = 11), 31.3 (n = 9) and 30.21 C (n = 21), for different sets of preparations; lobster 0.75x\n# ramps are n = 10 in Fig. 5C and n = 14 in Fig. 7A and 7D.\nschema_version: 2\npaper: doi:10.1152/jn.00294.2025\nclaims:\n- id: fig1b-cb-075-frequency-unchanged\n  statement: In the isolated C. borealis STNS at 10 C, lowering saline from 1x to 0.75x does not\n    change pyloric frequency (1.18 plus or minus 0.2 Hz in both, paired t test P = 0.8, n = 10).\n  source: Results, The C. borealis Pyloric Rhythm Is Maintained across a Range of Salinity,\n    paragraph 2; Figure 1B\n  quote: the frequency of the pyloric rhythm was not affected by decreasing the saline\n    concentration\n  statistics:\n  - test: paired Student's t test\n    p: 0.8\n    n: 10 C. borealis preparations\n  expected:\n  - quantity: C. borealis pyloric frequency in 1x saline, 10 C\n    value: 1.18\n    tolerance: 0.07\n    unit: Hz\n  - quantity: C. borealis pyloric frequency in 0.75x saline, 10 C\n    value: 1.18\n    tolerance: 0.07\n    unit: Hz\n  criterion: A claim of absence, judged on the paper's test. Per preparation, PD burst frequency\n    over the final 30 s of the 15-min 1x baseline and of the 15-min 0.75x application (Methods,\n    Data Analysis and Statistics); a two-sided paired t test at alpha 0.05. Reproduced when P >\n    0.05 and the two means are within tolerance; the mean difference is reported either way.\n    Which 1x segment is the baseline (end of the 30-min baseline or the 1x period just before\n    the series) is not stated; both are shown.\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig1d-cb-125-frequency-unchanged\n  statement: In the isolated C. borealis STNS at 10 C, raising saline from 1x to 1.25x does not\n    change pyloric frequency (1.2 plus or minus 0.1 Hz in both, paired t test P = 0.7, n = 10).\n  source: Results, The C. borealis Pyloric Rhythm Is Maintained across a Range of Salinity,\n    paragraph 3; Figure 1D\n  quote: Figure 1D shows that, similar to the application of the 0.75 ... saline did not alter the\n    pyloric frequency\n  statistics:\n  - test: paired Student's t test\n    p: 0.7\n    n: 10 C. borealis preparations\n  expected:\n  - quantity: C. borealis pyloric frequency in 1x saline, 10 C\n    value: 1.2\n    tolerance: 0.04\n    unit: Hz\n  - quantity: C. borealis pyloric frequency in 1.25x saline, 10 C\n    value: 1.2\n    tolerance: 0.04\n    unit: Hz\n  criterion: A claim of absence, judged on the paper's test, as in fig1b-cb-075-frequency-unchanged\n    with the 1.25x application. Reproduced when the paired t test gives P > 0.05 and both means are\n    within tolerance.\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig1e-cb-salinity-crash-fractions\n  statement: At 10 C every C. borealis preparation kept its pyloric rhythm in 0.75x and 1.25x\n    saline, all crashed in 0.5x, all but one kept it in 1.5x, and all crashed in 1.75x; crashes\n    were reversible on return to 1x.\n  source: Results, The C. borealis Pyloric Rhythm Is Maintained across a Range of Salinity,\n    paragraph 4; Figure 1E\n  quote: All preparations in decreased saline concentrations maintained a regular pyloric rhythm in\n    0.75 ... but not in 0.5 ... All preparations withstood an increase in 1.25 ... and all but one\n    maintained rhythmicity in 1.5 ... All preparations crashed in 1.75\n  expected:\n  - quantity: fraction of C. borealis preparations crashed in 0.75x\n    value: 0\n    tolerance: 0\n  - quantity: fraction crashed in 0.5x\n    value: 1\n    tolerance: 0\n  - quantity: fraction crashed in 1.25x\n    value: 0\n    tolerance: 0\n  - quantity: preparations crashed in 1.5x\n    value: 1\n    tolerance: 0\n  - quantity: fraction crashed in 1.75x\n    value: 1\n    tolerance: 0\n  criterion: Counts, so exact. Crash as the Methods define it (two of the three pyloric neurons no\n    longer bursting) within the 15-min application. Denominators n = 10 at every salinity except\n    1.75x, n = 9 (Fig. 1E legend). Reproduced when every count matches; partially reproduced when\n    all but one salinity match.\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig2b-cb-crash-temp-075-unchanged\n  statement: In C. borealis, 0.75x saline does not change the crash temperature of the pyloric\n    rhythm (1x 29.3 plus or minus 4.5 C, 0.75x 30.6 plus or minus 2.5 C, Wilcoxon signed-rank P =\n    0.4, n = 11), though it lowers its variance (Levene's test P = 0.05).\n  source: Results, Changes in Salinity Affect the Temperature Dependence of the Pyloric Cycle\n    Period, paragraph 2; Figure 2B\n  quote: There was no difference in crash temperatures between 1 ... and 0.75 ... applications\n    across preparations ... It did decrease the variance in crash temperature; Levene's test\n  statistics:\n  - about: crash temperature, 1x against 0.75x\n    test: Wilcoxon Mann-Whitney sign-rank test\n    p: 0.4\n    n: 11 C. borealis preparations\n  - about: variance of crash temperature, 1x against 0.75x\n    test: Levene's test\n    p: 0.05\n  expected:\n  - quantity: mean crash temperature in 1x\n    value: 29.3\n    tolerance: 1.36\n    unit: C\n  - quantity: mean crash temperature in 0.75x\n    value: 30.6\n    tolerance: 0.76\n    unit: C\n  criterion: A claim of absence for the means, judged on the paper's test, a two-sided Wilcoxon\n    signed-rank test on paired crash temperatures at alpha 0.05; reproduced when P > 0.05 and both\n    means are within tolerance. For the variance, Levene's test on the two sets; the paper prints P\n    = 0.05 as significant, so P <= 0.05 with the 0.75x SD lower is reproduced, and P up to 0.1\n    with the 0.75x SD lower is partially reproduced. Which centre Levene's test uses (mean, as in\n    Levene's original, or median, the Brown-Forsythe form) is not stated; both are shown.\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig2e-cb-crash-temp-125-lower\n  statement: In C. borealis, the pyloric rhythm crashes at a lower temperature in 1.25x than in\n    1x saline (31.3 plus or minus 4.3 against 26.2 plus or minus 3.1 C, paired t test P = 0.008,\n    n = 9), in every preparation tested.\n  source: Results, Changes in Salinity Affect the Temperature Dependence of the Pyloric Cycle\n    Period, paragraph 4; Figure 2D and 2E\n  quote: the pyloric rhythm crashed at a lower temperature in 1.25 ... saline compared with 1 ...\n    This trend was observed for all preparations tested\n  statistics:\n  - test: paired Student's t test\n    p: 0.008\n    n: 9 C. borealis preparations\n  expected:\n  - quantity: mean crash temperature in 1x\n    value: 31.3\n    tolerance: 1.44\n    unit: C\n  - quantity: mean crash temperature in 1.25x\n    value: 26.2\n    tolerance: 1.04\n    unit: C\n  - quantity: preparations with a lower crash temperature in 1.25x than in 1x\n    value: 9\n    tolerance: 0\n  criterion: Per preparation, the crash temperature (ramp step of the crash) in the 1x and the\n    1.25x ramp; a two-sided paired t test. Reproduced when P < 0.05 with 1.25x lower and both means\n    within tolerance; partially reproduced when the test holds but a mean or the count of 9 of 9\n    does not.\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig2f-cb-125-frequency-rises\n  statement: In C. borealis, pyloric frequency rises with temperature in 1.25x saline much as in\n    1x saline, despite the earlier crash.\n  source: Results, Changes in Salinity Affect the Temperature Dependence of the Pyloric Cycle\n    Period, paragraph 4; Figure 2F\n  quote: Despite crashing at a lower temperature, the pyloric frequency showed a similar increase\n    in frequency as temperature was increased\n  criterion: The paper shows this as a plot (Fig. 2F) and supports it with the Q10 comparison of\n    fig2h-cb-q10-125-unchanged, so it is judged by that claim's test over 10 to 24 C. Reproduced\n    when the 1.25x Q10 is above 1 (frequency rises) and the extra-sum-of-squares test finds no\n    difference from 1x. The Results summary paragraph says instead that 1.25x brought \"a decrease\n    in the pyloric frequency (Fig. 2F)\"; the mean frequency in 1.25x and in 1x at each step from\n    10 C to the 1.25x crash is shown so that both readings can be seen.\n  depends_on:\n  - fig2h-cb-q10-125-unchanged\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig2g-cb-q10-075-unchanged\n  statement: In C. borealis between 10 and 24 C the Q10 of pyloric frequency is the same in 1x\n    and 0.75x saline (1.72 against 1.71; F(1,171) = 0.007, P = 0.94, n = 11).\n  source: Results, Changes in Salinity Affect the Temperature Dependence of the Pyloric Cycle\n    Period, paragraph 5; Figure 2G\n  quote: We did not observe differences in the temperature dependencies between either 1 ... and\n    0.75\n  statistics:\n  - about: Q10 in 1x\n    ci:\n      level: 0.95\n      low: 1.54\n      high: 1.94\n  - about: Q10 in 0.75x\n    ci:\n      level: 0.95\n      low: 1.55\n      high: 1.89\n  - about: slope, 1x against 0.75x\n    test: Fisher's extra-sum-of-squares F test\n    statistic: F(1,171) = 0.007\n    p: 0.94\n    n: 11 C. borealis preparations\n  expected:\n  - quantity: Q10 of pyloric frequency, 1x, 10 to 24 C\n    value: 1.72\n    tolerance: 0.2\n  - quantity: Q10 of pyloric frequency, 0.75x, 10 to 24 C\n    value: 1.71\n    tolerance: 0.17\n  criterion: A claim of absence, judged on the paper's test. All preparations' frequencies at each\n    step from 10 to 24 C (Results, \"we selected a limited range of temperature (10 C-24 C)\"),\n    semi-log fit and Q10 = 10^(10m) as in the opening comment under readings Q-a and Q-b;\n    extra-sum-of-squares F test of a shared slope at alpha 0.05. Reproduced when P > 0.05 and both\n    Q10s are within tolerance under a reading; the denominator degrees of freedom are reported to\n    show the number of points used (171 + 4 = 175).\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig2h-cb-q10-125-unchanged\n  statement: In C. borealis between 10 and 24 C the Q10 of pyloric frequency is the same in 1x\n    and 1.25x saline (1.67 against 1.70; F(1,148) = 0.087, P = 0.77, n = 9).\n  source: Results, Changes in Salinity Affect the Temperature Dependence of the Pyloric Cycle\n    Period, paragraph 5; Figure 2H\n  quote: We did not observe differences in the temperature dependencies between either 1 ... or 1\n    ... 1.25\n  statistics:\n  - about: Q10 in 1x\n    ci:\n      level: 0.95\n      low: 1.56\n      high: 1.8\n  - about: Q10 in 1.25x\n    ci:\n      level: 0.95\n      low: 1.54\n      high: 1.89\n  - about: slope, 1x against 1.25x\n    test: Fisher's extra-sum-of-squares F test\n    statistic: F(1,148) = 0.087\n    p: 0.77\n    n: 9 C. borealis preparations\n  expected:\n  - quantity: Q10 of pyloric frequency, 1x, 10 to 24 C\n    value: 1.67\n    tolerance: 0.12\n  - quantity: Q10 of pyloric frequency, 1.25x, 10 to 24 C\n    value: 1.7\n    tolerance: 0.18\n  criterion: A claim of absence, judged on the paper's test, as in fig2g-cb-q10-075-unchanged with\n    the 1.25x ramps and their paired 1x ramps. Reproduced when P > 0.05 and both Q10s are within\n    tolerance under reading Q-a or Q-b.\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig2f-cb-mixed-model\n  statement: Over the full temperature range, a mixed-effects model of C. borealis pyloric\n    frequency finds an effect of temperature and of the temperature by salinity interaction, and\n    no effect of salinity alone.\n  source: Results, Changes in Salinity Affect the Temperature Dependence of the Pyloric Cycle\n    Period, paragraph 6; Figure 2F legend\n  quote: This statistical model revealed an influence of temperature as well as a combined effect\n    of temperature and salinity on the pyloric frequency of C. borealis. Nonetheless, there was not\n    an effect of salinity alone on pyloric frequency\n  statistics:\n  - about: temperature\n    test: REML mixed-effects model, F test\n    statistic: F(1,21.82) = 43.92\n    p: 0.0001\n    p_relation: \"<\"\n    n: 11 C. borealis preparations\n  - about: temperature by salinity\n    test: REML mixed-effects model, F test\n    statistic: F(1,19.58) = 5.86\n    p: 0.025\n  - about: salinity\n    test: REML mixed-effects model, F test\n    statistic: F(1,18.61) = 2.04\n    p: 0.17\n  criterion: From the Methods, a linear mixed model (lme4) of pyloric frequency on temperature,\n    salinity and their interaction, random intercepts per animal, random slopes chosen by AIC,\n    BIC and Bayes factor, F tests with lmerTest (Satterthwaite degrees of freedom, the lmerTest\n    default, which the fractional df printed fit). Over every step up to each ramp's crash. Open,\n    with readings the paper allows. Which salinities enter (the legend sits under Fig. 2F, the\n    1.25x data, but n = 11 is the 0.75x set): (S-a) 1x and 1.25x ramps; (S-b) 1x and 0.75x ramps;\n    (S-c) all three. Salinity enters with one degree of freedom, so as a number (0.75, 1, 1.25) or\n    a two-level factor. Response as frequency (F-a) or log frequency (F-b). Random slope candidates\n    are temperature, salinity or both. Reproduced when, under one reading, temperature and the\n    interaction have P < 0.05 and salinity P > 0.05; partially reproduced when two of the three\n    hold.\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig2i-cb-neuron-crash-counts\n  statement: In C. borealis in 1x saline all three pyloric neurons crashed at the same temperature\n    in 9 of 20 preparations, PY crashed in 14 of 20 and LP in all; in 0.75x PD crashed in 4 of 11\n    and LP and PY in all; in 1.25x PY crashed in 5 of 9, PD in 6 of 9 and LP in all.\n  source: Results, Changes in Salinity Affect the Temperature Dependence of the Pyloric Cycle\n    Period, paragraph 7; Figure 2I to 2K\n  quote: in 9 of 20 preparations all three neurons crashed at the same temperature, and in 14 of 20\n    preparations, the PY neurons crashed. The LP neuron always crashed ... the PD neurons only\n    crashed in 4 of 11 preparations, whereas the LP and PY neurons crashed in all experiments ... in\n    5 of 9 preparations the PY neurons crashed and 6 of those 9 experiments included a loss of PD.\n    LP crashed in all experiments\n  expected:\n  - quantity: 1x preparations with all three neurons crashing at one temperature, of 20\n    value: 9\n    tolerance: 0\n  - quantity: 1x preparations with a PY crash, of 20\n    value: 14\n    tolerance: 0\n  - quantity: 1x preparations with a PD crash, of 20\n    value: 15\n    tolerance: 0\n  - quantity: 0.75x preparations with a PD crash, of 11\n    value: 4\n    tolerance: 0\n  - quantity: 1.25x preparations with a PY crash, of 9\n    value: 5\n    tolerance: 0\n  - quantity: 1.25x preparations with a PD crash, of 9\n    value: 6\n    tolerance: 0\n  criterion: Per ramp, each neuron's crash is the step at which its bursts stop in the lvn, pdn or\n    pyn recording (Methods); a neuron that bursts at the rhythm's crash step has not crashed. The\n    PD count in 1x (15) is the n of Fig. 2I. Reproduced when every count matches; partially\n    reproduced when each is within one. The 20 preparations in 1x pool the 1x ramps of both\n    combined sets (11 and 9).\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig2i-cb-neuron-crash-temps-similar\n  statement: In C. borealis the LP, PY and PD neurons crash at similar temperatures in 1x, 0.75x\n    and 1.25x saline, with no consistent crash order.\n  source: Results, Changes in Salinity Affect the Temperature Dependence of the Pyloric Cycle\n    Period, paragraph 7; Figure 2I to 2K\n  quote: We did not observe a difference in neuron crash temperature in 1 ... we did not observe\n    any difference in neuron crash temperature in either 0.75\n  statistics:\n  - about: 1x\n    test: REML mixed-effects model\n    statistic: F(0.57,7.67) = 1.14\n    p: 0.27\n    n: 20 LP, 14 PY, 15 PD\n  - about: 0.75x\n    test: REML mixed-effects model\n    statistic: F(1.71,11.28) = 2.68\n    p: 0.12\n    n: 11 LP, 11 PY, 4 PD\n  - about: 1.25x\n    test: REML mixed-effects model\n    statistic: F(1.25,5.62) = 1.61\n    p: 0.27\n    n: 9 LP, 5 PY, 6 PD\n  criterion: A claim of absence, judged on the paper's test. Per salinity, crash temperatures of\n    LP, PY and PD (those that crashed) in Prism's REML mixed-effects model for repeated measures\n    with missing values (neuron as the within-preparation factor, Geisser-Greenhouse correction,\n    which the fractional df printed show). Reproduced when P > 0.05 at all three salinities; not\n    reproduced when any is below 0.05. The mean crash temperature of each neuron is reported.\n  depends_on:\n  - fig2i-cb-neuron-crash-counts\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig3b-ha-frequency-q10\n  statement: In the isolated H. americanus STNS in 1x saline, pyloric frequency rises with\n    temperature between 10 and 28 C with a Q10 of 1.43, a slope different from zero.\n  source: Results, Increased Temperature Affects the Pyloric Rhythm in the H. americanus STNS,\n    paragraph 1; Figure 3B\n  quote: The pyloric frequency increased with increased temperature\n  statistics:\n  - about: Q10, 10 to 28 C\n    ci:\n      level: 0.95\n      low: 1.24\n      high: 1.66\n  - about: slope against zero\n    test: Fisher's F test\n    statistic: F(1,8) = 35.72\n    p: 0.0003\n  expected:\n  - quantity: Q10 of H. americanus pyloric frequency in 1x, 10 to 28 C\n    value: 1.43\n    tolerance: 0.21\n  criterion: Semi-log fit and Q10 as in the opening comment (readings Q-a and Q-b), 10 to 28 C,\n    the slope compared with zero by an extra-sum-of-squares F test. Open, which points are fitted.\n    F(1,8) fits ten points, the step means of Fig. 3B (10 to 28 C in 2 C steps), reading (P-a);\n    the Results later give the same Q10 with CI 1.30 to 1.59 over n = 19 (Fig. 7B), which fits all\n    preparations' points, reading (P-b). Reproduced when, under one reading, the slope differs\n    from zero at P < 0.05 and the Q10 is within tolerance.\n  datasets:\n  - zenodo-17624449\n- id: species-frequency-at-10c\n  statement: At 10 C in 1x saline the H. americanus pyloric rhythm is slower than the C. borealis\n    rhythm (0.56 against 1.21 Hz, Welch's t test P < 0.0001, n = 15 and 19).\n  source: Results, Increased Temperature Affects the Pyloric Rhythm in the H. americanus STNS,\n    paragraph 2\n  quote: the pyloric frequency of H. americanus was slower than that of C. borealis\n  statistics:\n  - test: Welch's t test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 19 C. borealis and 15 H. americanus preparations\n  expected:\n  - quantity: C. borealis pyloric frequency at 10 C\n    value: 1.21\n    tolerance: 0.03\n    unit: Hz\n  - quantity: H. americanus pyloric frequency at 10 C\n    value: 0.56\n    tolerance: 0.03\n    unit: Hz\n  criterion: One value per preparation, the PD burst frequency at 10 C in 1x saline; two-sided\n    Welch's t test. Open, which 10 C recording and which preparations (the n of 19 and 15 matches\n    no other set the paper names). Readings (R-a) the first 10 C step of each preparation's first\n    1x ramp; (R-b) the 10 C baseline of the salinity series. Reproduced when, under one reading,\n    P < 0.05 with H. americanus slower and both means within tolerance; partially reproduced when\n    the test holds and the means do not.\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig3c-ha-phase-constant\n  statement: In H. americanus between 10 and 18 C the phases of PD off, LP on, LP off and PY off\n    do not change with temperature (Q10 near 1); only the PY-on phase changes (Q10 1.233, P =\n    0.02).\n  source: Results, Increased Temperature Affects the Pyloric Rhythm in the H. americanus STNS,\n    paragraph 3; Table 1; Figure 3C\n  quote: Except for the PY-on phase, we did not observe any changes in the pyloric neuron phase\n    relationships between 10\n  statistics:\n  - about: PY-on phase slope against zero\n    test: extra-sum-of-squares F test\n    p: 0.02\n    n: 7 H. americanus preparations (6 at 16 C, 5 at 18 C)\n  expected:\n  - quantity: Q10 of PD-off phase\n    value: 0.887\n    tolerance: 0.08\n  - quantity: Q10 of LP-on phase\n    value: 0.971\n    tolerance: 0.12\n  - quantity: Q10 of LP-off phase\n    value: 1.03\n    tolerance: 0.15\n  - quantity: Q10 of PY-on phase\n    value: 1.233\n    tolerance: 0.19\n  - quantity: Q10 of PY-off phase\n    value: 1.004\n    tolerance: 0.08\n  criterion: Phases from ten cycles per step, each event's delay from the preceding PD onset over\n    that cycle's period (Methods), averaged per preparation and step, 10 to 18 C; semi-log fit and\n    Q10 as in the opening comment (Q-a, Q-b), each slope compared with zero by an extra-sum-of-\n    squares F test at alpha 0.05. Tolerances are Table 1's \"95% CI\" column, read as the CI\n    half-width; whether it is a half-width or a standard error is not stated. Which event is the\n    exception is inconsistent in the paper (Table 1 and Results say PY on, the Fig. 3C legend says\n    PY off); Table 1 is followed. Reproduced when only PY on has P < 0.05 and the Q10s are within\n    tolerance; partially reproduced when PY on alone differs from zero and some Q10s miss.\n  datasets:\n  - zenodo-17624449\n- id: fig4b-ha-075-frequency-unchanged\n  statement: In the isolated H. americanus STNS at 10 C, 0.75x saline does not change pyloric\n    frequency (0.72 plus or minus 0.1 Hz in both, paired t test P = 0.9).\n  source: Results, The Effects of Altered Salinity on the H. americanus Pyloric Rhythm, paragraph\n    1; Figure 4B\n  quote: Similar to what we observed in C. borealis, the H. americanus pyloric frequency was not\n    altered by this concentration\n  statistics:\n  - test: paired Student's t test\n    p: 0.9\n    n: 9 H. americanus preparations (Results); 8 in the Fig. 4B legend\n  expected:\n  - quantity: H. americanus pyloric frequency in 1x, 10 C\n    value: 0.72\n    tolerance: 0.04\n    unit: Hz\n  - quantity: H. americanus pyloric frequency in 0.75x, 10 C\n    value: 0.72\n    tolerance: 0.04\n    unit: Hz\n  criterion: A claim of absence, judged on the paper's test, a two-sided paired t test at alpha\n    0.05 on the final 30 s of 1x and of the 0.75x application, over the decreasing-salinity\n    preparations (n = 9 in the Results, 8 in the legend; all that reached 0.75x are used and the\n    count reported). Reproduced when P > 0.05 and both means are within tolerance.\n  datasets:\n  - zenodo-17624449\n- id: fig4d-ha-125-frequency-unchanged\n  statement: In the isolated H. americanus STNS at 10 C, 1.25x saline does not change pyloric\n    frequency (0.73 plus or minus 0.1 Hz in both, paired t test, n = 8).\n  source: Results, The Effects of Altered Salinity on the H. americanus Pyloric Rhythm, paragraph\n    2; Figure 4D\n  quote: Similarly to C. borealis, the H. americanus pyloric frequency was unchanged in 1.25\n  statistics:\n  - test: paired Student's t test\n    p: 0.9\n    n: 8 H. americanus preparations (the Fig. 4D legend prints P = 0.8)\n  expected:\n  - quantity: H. americanus pyloric frequency in 1x, 10 C\n    value: 0.73\n    tolerance: 0.04\n    unit: Hz\n  - quantity: H. americanus pyloric frequency in 1.25x, 10 C\n    value: 0.73\n    tolerance: 0.04\n    unit: Hz\n  criterion: A claim of absence, judged on the paper's test, as in fig4b-ha-075-frequency-unchanged\n    over the increasing-salinity preparations. Reproduced when P > 0.05 and both means are within\n    tolerance.\n  datasets:\n  - zenodo-17624449\n- id: fig4e-ha-salinity-crash-fractions\n  statement: At 10 C all H. americanus preparations kept a pyloric rhythm in 0.75x saline, a third\n    kept it in 0.5x, 1.5x crashed the rhythm in 1 of 8, and 0.25x was lethal in all.\n  source: Results, The Effects of Altered Salinity on the H. americanus Pyloric Rhythm, paragraphs\n    1 to 3; Figure 4E\n  quote: a third of preparations maintained a pyloric rhythm at this salinity ... all preparations\n    tested maintained a regular pyloric rhythm in 0.75 ... this concentration only completely\n    crashed the rhythm in 1 of 8 experiments\n  expected:\n  - quantity: fraction of preparations crashed in 0.75x, of 9\n    value: 0\n    tolerance: 0\n  - quantity: preparations crashed in 0.5x, of 9\n    value: 6\n    tolerance: 0\n  - quantity: preparations crashed in 1.5x, of 8\n    value: 1\n    tolerance: 0\n  - quantity: fraction crashed in 0.25x, of 3\n    value: 1\n    tolerance: 0\n  criterion: Counts, so exact; denominators from the Fig. 4E legend (0.25x n = 3, 0.5x n = 9, 0.75x\n    n = 9, 1.25x n = 8, 1.5x n = 8, 1.75x n = 7). Six of nine in 0.5x is the paper's \"a third ...\n    maintained\". The fractions at 1.25x and 1.75x are shown in the bar graph only, not read here,\n    and are reported. Reproduced when the four counts match; partially reproduced when three do.\n  datasets:\n  - zenodo-17624449\n- id: fig5b-ha-lp-crashes-before-py\n  statement: In H. americanus the LP neuron crashes at a lower temperature than the PY neurons in\n    each salinity (0.75x 25.6 against 30.4 C; 1x 21.9 against 27.8 C; 1.25x 19.9 against 25.0 C).\n  source: Results, The Effects of Combined Manipulations of Temperature and Salinity on the H.\n    americanus Pyloric Circuit, paragraph 2; Figure 5B\n  quote: At each salinity, the LP neuron crashed at a lower temperature than the PY neurons\n  statistics:\n  - about: 0.75x\n    test: paired Student's t test\n    p: 0.015\n    n: 13 H. americanus preparations\n  - about: 1x\n    test: paired Student's t test\n    p: 0.0006\n    n: 18 H. americanus preparations\n  - about: 1.25x\n    test: Wilcoxon signed-rank test\n    p: 0.002\n    n: 12 H. americanus preparations\n  expected:\n  - quantity: LP crash temperature, 0.75x\n    value: 25.6\n    tolerance: 1.56\n    unit: C\n  - quantity: PY crash temperature, 0.75x\n    value: 30.4\n    tolerance: 0.67\n    unit: C\n  - quantity: LP crash temperature, 1x\n    value: 21.9\n    tolerance: 0.95\n    unit: C\n  - quantity: PY crash temperature, 1x\n    value: 27.8\n    tolerance: 0.92\n    unit: C\n  - quantity: LP crash temperature, 1.25x\n    value: 19.9\n    tolerance: 0.9\n    unit: C\n  - quantity: PY crash temperature, 1.25x\n    value: 25\n    tolerance: 1.36\n    unit: C\n  criterion: Per ramp, the step at which LP bursts stop and the step at which PY bursts stop\n    (Methods). Per salinity, a two-sided paired t test (0.75x, 1x) or Wilcoxon signed-rank test\n    (1.25x) on preparations where both crashed. Reproduced when all three tests give P < 0.05 with\n    LP lower; partially reproduced for two of three. Means are reported against tolerance.\n  datasets:\n  - zenodo-17624449\n- id: fig5c-ha-mixed-model\n  statement: A mixed-effects model of H. americanus pyloric frequency over the full temperature\n    range finds effects of temperature, salinity and their interaction.\n  source: Results, The Effects of Combined Manipulations of Temperature and Salinity on the H.\n    americanus Pyloric Circuit, paragraph 4; Figure 5C\n  quote: The model revealed that each perturbation, as well as the combination, had an impact on\n    the H. americanus pyloric frequency\n  statistics:\n  - about: temperature\n    test: REML mixed-effects model, F test\n    statistic: F(1,78.45) = 53.27\n    p: 0.0001\n    p_relation: \"<\"\n    n: 10 (0.75x), 14 (1x), 8 (1.25x) H. americanus preparations\n  - about: salinity\n    test: REML mixed-effects model, F test\n    statistic: F(1,90.31) = 10.93\n    p: 0.001\n  - about: temperature by salinity\n    test: REML mixed-effects model, F test\n    statistic: F(1,114.53) = 30.68\n    p: 0.0001\n    p_relation: \"<\"\n  criterion: As in fig2f-cb-mixed-model (lme4, random intercepts per animal, random slopes chosen\n    by AIC, BIC and Bayes factor, lmerTest F tests), over every step to each ramp's crash, with\n    the three salinities. Open, salinity as a number (one df, as printed) or a factor, and\n    response as frequency (F-a) or log frequency (F-b). Reproduced when, under one reading, all\n    three terms have P < 0.05; partially reproduced for two.\n  datasets:\n  - zenodo-17624449\n- id: fig5d-ha-q10-salinity-unchanged\n  statement: In H. americanus the Q10 of pyloric frequency over the rising range does not differ\n    between 0.75x and its 1x controls (1.85 against 1.61, P = 0.063) or between 1.25x and its 1x\n    controls (1.48 against 1.87, P = 0.055).\n  source: Results, The Effects of Combined Manipulations of Temperature and Salinity on the H.\n    americanus Pyloric Circuit, paragraph 5; Figure 5D\n  quote: The Q10s were not different between each altered salinity compared with the 1\n  statistics:\n  - about: 1x against 0.75x\n    test: Fisher's extra-sum-of-squares F test\n    statistic: F(1,209) = 3.495\n    p: 0.063\n    n: 14 H. americanus preparations\n  - about: 1x against 1.25x\n    test: Fisher's extra-sum-of-squares F test\n    statistic: F(1,171) = 3.725\n    p: 0.055\n    n: 14 H. americanus preparations\n  - about: Q10, 1x controls of the 0.75x set\n    ci:\n      level: 0.95\n      low: 1.43\n      high: 1.82\n  - about: Q10, 0.75x\n    ci:\n      level: 0.95\n      low: 1.69\n      high: 2.05\n  - about: Q10, 1x controls of the 1.25x set\n    ci:\n      level: 0.95\n      low: 1.62\n      high: 2.18\n  - about: Q10, 1.25x\n    ci:\n      level: 0.95\n      low: 1.23\n      high: 1.8\n  expected:\n  - quantity: Q10, 1x controls of the 0.75x set\n    value: 1.61\n    tolerance: 0.2\n  - quantity: Q10, 0.75x\n    value: 1.85\n    tolerance: 0.18\n  - quantity: Q10, 1x controls of the 1.25x set\n    value: 1.87\n    tolerance: 0.28\n  - quantity: Q10, 1.25x\n    value: 1.48\n    tolerance: 0.29\n  criterion: A claim of absence, judged on the paper's test. Ranges from the Results, frequency\n    falls above 24 C in 0.75x and above 22 C in 1.25x, so fits run from 10 to 24 C (0.75x set) and\n    10 to 22 C (1.25x set), the within-preparation 1x controls over the same range (Results,\n    \"across this limited temperature range\"). Semi-log fit and Q10 as in the opening comment (Q-a,\n    Q-b); extra-sum-of-squares F test of a shared slope at alpha 0.05. Reproduced when both tests\n    give P > 0.05 and the four Q10s are within tolerance under a reading. Both printed P values\n    are near 0.05, so a result just below 0.05 is reported as not reproduced, with the size of\n    the difference.\n  datasets:\n  - zenodo-17624449\n- id: fig6a-ha-py-crash-temp-salinity\n  statement: H. americanus PY neurons crash at higher temperatures in 0.75x and lower temperatures\n    in 1.25x than in 1x saline (30.9, 27.7 and 24.5 C), each pair differing.\n  source: Results, The Effects of Combined Manipulations of Temperature and Salinity on the H.\n    americanus Pyloric Circuit, paragraph 6; Figure 6A\n  quote: We found that both neurons crashed at higher temperatures in 0.75 ... saline and crashed\n    at lower temperatures in 1.25 ... saline compared ... with 1 ... saline and compared with each\n    other\n  statistics:\n  - about: salinity effect\n    test: mixed-effects model\n    statistic: F(1.59,20.67) = 21.22\n    p: 0.0001\n    p_relation: \"<\"\n  - about: 0.75x against 1x\n    test: Holm-Sidak post hoc\n    p: 0.011\n    corrected: Holm-Sidak\n    n: 14 and 14\n  - about: 1x against 1.25x\n    test: Holm-Sidak post hoc\n    p: 0.004\n    corrected: Holm-Sidak\n    n: 14 and 14\n  - about: 0.75x against 1.25x\n    test: Holm-Sidak post hoc\n    p: 0.004\n    corrected: Holm-Sidak\n    n: 9 and 9\n  expected:\n  - quantity: PY crash temperature, 0.75x\n    value: 30.9\n    tolerance: 0.73\n    unit: C\n  - quantity: PY crash temperature, 1x\n    value: 27.7\n    tolerance: 1.07\n    unit: C\n  - quantity: PY crash temperature, 1.25x\n    value: 24.5\n    tolerance: 1.26\n    unit: C\n  criterion: Per preparation and salinity the PY crash temperature; Prism's REML mixed-effects\n    model with salinity as the repeated factor and Geisser-Greenhouse correction (fractional df as\n    printed), then Holm-Sidak comparisons of the three pairs (Methods, Data Analysis and\n    Statistics). Tolerances use n = 14 for each salinity (the pairwise n). Reproduced when the\n    model gives P < 0.05 and all three pairs differ at P < 0.05 in the stated direction; partially\n    reproduced when the model and two pairs hold.\n  depends_on:\n  - fig5b-ha-lp-crashes-before-py\n  datasets:\n  - zenodo-17624449\n- id: fig6b-ha-lp-crash-temp-salinity\n  statement: H. americanus LP neurons crash at higher temperatures in 0.75x and lower temperatures\n    in 1.25x than in 1x saline (25.6, 22.2 and 20.0 C), each pair differing.\n  source: Results, The Effects of Combined Manipulations of Temperature and Salinity on the H.\n    americanus Pyloric Circuit, paragraph 6; Figure 6B\n  quote: Similarly, the LP neuron temperature tolerance decreased as salinity was increased\n  statistics:\n  - about: salinity effect\n    test: mixed-effects model\n    statistic: F(1.566,27.40) = 12.24\n    p: 0.0004\n  - about: 0.75x against 1x\n    test: Holm-Sidak post hoc\n    p: 0.04\n    corrected: Holm-Sidak\n    n: 18 and 18\n  - about: 1x against 1.25x\n    test: Holm-Sidak post hoc\n    p: 0.013\n    corrected: Holm-Sidak\n    n: 19 and 19\n  - about: 0.75x against 1.25x\n    test: Holm-Sidak post hoc\n    p: 0.01\n    corrected: Holm-Sidak\n    n: 11 and 11\n  expected:\n  - quantity: LP crash temperature, 0.75x\n    value: 25.6\n    tolerance: 1.42\n    unit: C\n  - quantity: LP crash temperature, 1x\n    value: 22.2\n    tolerance: 0.97\n    unit: C\n  - quantity: LP crash temperature, 1.25x\n    value: 20\n    tolerance: 0.79\n    unit: C\n  criterion: As fig6a-ha-py-crash-temp-salinity, for LP. Tolerances use n = 18 for 0.75x and 1x\n    and n = 19 for 1.25x (the pairwise n).\n  depends_on:\n  - fig5b-ha-lp-crashes-before-py\n  datasets:\n  - zenodo-17624449\n- id: fig7a-species-q10-075\n  statement: In 0.75x saline between 10 and 30 C the Q10 of pyloric frequency is lower in H.\n    americanus than in C. borealis (1.40 against 1.72, F(1,250) = 12.18, P = 0.0006).\n  source: Results, Comparing Temperature Dependencies across Species at Each Salinity, paragraph\n    1; Figure 7A\n  quote: the H. americanus pyloric frequency had a lower Q10 compared with the change in pyloric\n    frequency in C. borealis\n  statistics:\n  - about: C. borealis Q10\n    ci:\n      level: 0.95\n      low: 1.6\n      high: 1.84\n  - about: H. americanus Q10\n    ci:\n      level: 0.95\n      low: 1.29\n      high: 1.53\n  - about: slope, C. borealis against H. americanus\n    test: Fisher's extra-sum-of-squares F test\n    statistic: F(1,250) = 12.18\n    p: 0.0006\n    n: 11 C. borealis and 14 H. americanus preparations\n  expected:\n  - quantity: C. borealis Q10 in 0.75x, 10 to 30 C\n    value: 1.72\n    tolerance: 0.12\n  - quantity: H. americanus Q10 in 0.75x, 10 to 30 C\n    value: 1.4\n    tolerance: 0.12\n  criterion: All preparations' 0.75x frequencies from 10 to 30 C (Results), semi-log fit and Q10 as\n    in the opening comment (Q-a, Q-b), extra-sum-of-squares F test of a shared slope. Reproduced\n    when P < 0.05 with H. americanus lower and both Q10s within tolerance under a reading;\n    partially reproduced when the test holds and a Q10 misses. The H. americanus n of 14 differs\n    from the 10 of Fig. 5C; all lobster 0.75x ramps are used and the count reported.\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig7b-species-q10-1x-similar\n  statement: In 1x saline between 10 and 28 C the Q10 of pyloric frequency does not differ between\n    C. borealis and H. americanus (1.60 against 1.43, F(1,353) = 3.04, P = 0.082).\n  source: Results, Comparing Temperature Dependencies across Species at Each Salinity, paragraph\n    1; Figure 7B; Results, Increased Temperature Affects the Pyloric Rhythm in the H. americanus\n    STNS, paragraph 2\n  quote: Although we did not see a difference in the change in pyloric frequency between species\n    between 10\n  statistics:\n  - about: C. borealis Q10\n    ci:\n      level: 0.95\n      low: 1.52\n      high: 1.69\n  - about: H. americanus Q10\n    ci:\n      level: 0.95\n      low: 1.3\n      high: 1.59\n  - about: slope, C. borealis against H. americanus\n    test: Fisher's extra-sum-of-squares F test\n    statistic: F(1,353) = 3.04\n    p: 0.082\n    n: 21 C. borealis and 19 H. americanus preparations\n  expected:\n  - quantity: C. borealis Q10 in 1x, 10 to 28 C\n    value: 1.6\n    tolerance: 0.09\n  - quantity: H. americanus Q10 in 1x, 10 to 28 C\n    value: 1.43\n    tolerance: 0.15\n  criterion: A claim of absence, judged on the paper's test. All preparations' 1x frequencies from\n    10 to 28 C, semi-log fit and Q10 as in the opening comment (Q-a, Q-b), extra-sum-of-squares F\n    test of a shared slope at alpha 0.05. Reproduced when P > 0.05 and both Q10s are within\n    tolerance under a reading. Which 1x ramp counts when a preparation has two (one per combined\n    set) is not stated; n = 21 for C. borealis exceeds the 20 of Fig. 2I, so readings are (A-a)\n    every 1x ramp, (A-b) the first 1x ramp per preparation.\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig7c-species-q10-125\n  statement: In 1.25x saline the Q10 of pyloric frequency is lower in H. americanus than in C.\n    borealis (1.25 against 1.61, F(1,175) = 9.371, P = 0.0026).\n  source: Results, Comparing Temperature Dependencies across Species at Each Salinity, paragraph\n    1; Figure 7C\n  quote: we did observe a difference in 1.25\n  statistics:\n  - about: C. borealis Q10\n    ci:\n      level: 0.95\n      low: 1.48\n      high: 1.76\n  - about: H. americanus Q10\n    ci:\n      level: 0.95\n      low: 1.1\n      high: 1.43\n  - about: slope, C. borealis against H. americanus\n    test: Fisher's extra-sum-of-squares F test\n    statistic: F(1,175) = 9.371\n    p: 0.0026\n    n: 10 C. borealis and 14 H. americanus preparations\n  expected:\n  - quantity: C. borealis Q10 in 1.25x\n    value: 1.61\n    tolerance: 0.14\n  - quantity: H. americanus Q10 in 1.25x\n    value: 1.25\n    tolerance: 0.17\n  criterion: Semi-log fit and Q10 as in the opening comment (Q-a, Q-b), extra-sum-of-squares F\n    test of a shared slope. The temperature range is not stated for 1.25x (Fig. 7 legend, \"a\n    limited temperature range\"). Readings (T-a) 10 to 22 C, the range the Results give for\n    lobster 1.25x (Fig. 5D); (T-b) 10 to 24 C, the crab range of Fig. 2H; (T-c) 10 to 28 C, as in\n    Fig. 7B. Reproduced when, under one reading, P < 0.05 with H. americanus lower and both Q10s\n    within tolerance; partially reproduced when the test holds and a Q10 misses.\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig7e-species-crash-temp-1x\n  statement: In 1x saline the C. borealis pyloric rhythm crashes at a higher temperature than the\n    H. americanus rhythm (30.21 against 27.62 C, Welch's t test P = 0.047, n = 21 and 19).\n  source: Results, Comparing Temperature Dependencies across Species at Each Salinity, paragraph\n    1; Figure 7E\n  quote: we only observed a difference in crash temperature in 1\n  statistics:\n  - test: Welch's t test\n    p: 0.047\n    n: 21 C. borealis and 19 H. americanus preparations\n  expected:\n  - quantity: C. borealis crash temperature in 1x\n    value: 30.21\n    tolerance: 0.97\n    unit: C\n  - quantity: H. americanus crash temperature in 1x\n    value: 27.62\n    tolerance: 0.9\n    unit: C\n  criterion: One crash temperature per preparation in 1x (rhythm crash, Methods), two-sided Welch's\n    t test. Readings for preparations with two 1x ramps as in fig7b-species-q10-1x-similar (A-a,\n    A-b). Reproduced when, under one reading, P < 0.05 with C. borealis higher and both means\n    within tolerance; partially reproduced when the test holds and a mean misses.\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig7df-species-crash-temp-075-125-similar\n  statement: In 0.75x and in 1.25x saline the two species' pyloric rhythms crash at similar\n    temperatures (0.75x 30.62 against 31.07 C, P = 0.99; 1.25x 27.28 against 24.26 C, P = 0.08).\n  source: Results, Comparing Temperature Dependencies across Species at Each Salinity, paragraph\n    1; Figure 7D and 7F\n  quote: we only observed a difference in crash temperature in 1\n  statistics:\n  - about: 0.75x\n    test: Wilcoxon Mann-Whitney U test\n    p: 0.99\n    n: 11 C. borealis and 14 H. americanus preparations\n  - about: 1.25x\n    test: Welch's t test\n    p: 0.08\n    n: 10 C. borealis and 14 H. americanus preparations\n  expected:\n  - quantity: C. borealis crash temperature in 0.75x\n    value: 30.62\n    tolerance: 0.76\n    unit: C\n  - quantity: H. americanus crash temperature in 0.75x\n    value: 31.07\n    tolerance: 0.7\n    unit: C\n  - quantity: C. borealis crash temperature in 1.25x\n    value: 27.28\n    tolerance: 1.43\n    unit: C\n  - quantity: H. americanus crash temperature in 1.25x\n    value: 24.26\n    tolerance: 1.29\n    unit: C\n  criterion: A claim of absence, judged on the paper's tests, a two-sided Mann-Whitney U test\n    (0.75x) and a two-sided Welch's t test (1.25x) at alpha 0.05. Reproduced when both give P >\n    0.05; not reproduced when either is below. Means are reported against tolerance and the\n    differences given either way.\n  datasets:\n  - zenodo-17624449\n  - zenodo-17794764\n- id: fig8-invivo-rhythm-maintained\n  statement: In intact animals of both species the pyloric rhythm, recorded by PPG, does not crash\n    during 1-h exposures to any seawater salinity from 0.25x to 1.75x, including those that crash\n    the isolated STNS.\n  source: Results, In Vivo, Both Species Withstand a Greater Salinity Range than the Isolated\n    Nervous System, paragraph 1; Figure 8A to 8D\n  quote: Importantly, we did not observe crashes in the pyloric rhythm in either species at either\n    increased or decreased salinity during these 1-h changes in saline concentration\n  expected:\n  - quantity: 1-h in vivo exposures with a crashed rhythm\n    value: 0\n    tolerance: 0\n  criterion: Per animal and exposure, a short-time Fourier transform spectrogram of the PPG signal\n    over 0 to 3 Hz (Methods); the rhythm is present when a distinct high-power band stands out in\n    the pyloric range, and crashed when no band is present (Results, Fig. 8 description). Samples\n    n = 6 crab and 5 lobster for decreased salinities, 6 and 5 for increased (Fig. 8 legend). Open,\n    with no parameter in the paper or a linked script, the STFT window and overlap (a standard\n    choice, 10-s windows with 50% overlap, cannot change whether a band exists), and when a band\n    counts as present. Readings (B-a) the peak power between 0.3 and 3 Hz exceeds three times the\n    median power of the same window in at least half the windows of the hour; (B-b) the same\n    measured over the first 30 min, the span Fig. 8 shows. Reproduced when every exposure keeps the\n    rhythm under both readings; partially reproduced when all but one do; the results of each\n    reading are shown.\n  datasets:\n  - zenodo-17794764\n- id: fig9-15h-mortality\n  statement: In 15-h exposures, crabs died only at 0.25x and 1.75x, while lobsters died at 0.25x,\n    1.5x and 1.75x and at higher rates, so C. borealis tolerates the salinity extremes better.\n  source: Results, In Vivo, Both Species Withstand a Greater Salinity Range than the Isolated\n    Nervous System, paragraph 2; Figure 9A and 9B\n  quote: Interestingly, C. borealis exhibited a greater tolerance than H. americanus to the\n    salinity extremes tested here\n  criterion: Per species and salinity, the fraction of the 5 animals that died during the 15-h\n    exposure (Fig. 9 legend). Reproduced when crab deaths occur only at 0.25x and 1.75x, lobster\n    deaths occur at 0.25x, 1.5x and 1.75x, and the lobster fraction is at least the crab fraction\n    at 0.25x and 1.75x with a higher total. The bar heights were not read; the Fig. 9 legend\n    names crabs in panel A and the Results name lobsters, and the legend text that describes each\n    panel's mortalities is followed. Whether survival records are in the dataset is for the author\n    to find; the deposit describes in vivo recordings.\n  datasets:\n  - zenodo-17794764\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/carrier-2026.yaml paper/10.1152-jn.00294.2025.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -nE "^\s+[^#].*\S: " claims/carrier-2026.yaml | grep -vE "^\s*[0-9]+:\s+(- )?[a-z_]+: [^:]*$"
```

```
366:    1.25x data, but n = 11 is the 0.75x set): (S-a) 1x and 1.25x ramps; (S-b) 1x and 0.75x ramps;
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/carrier-2026.yaml",
 "old_string": "is the 0.75x set): (S-a)",
 "new_string": "is the 0.75x set) are (S-a)"
}
```

```
The file claims/carrier-2026.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/carrier-2026.yaml paper/10.1152-jn.00294.2025.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -nE "—|rather" claims/carrier-2026.yaml; grep -c "criterion:" claims/carrier-2026.yaml; grep -c "statistics:" claims/carrier-2026.yaml; git status --short
```

```
29
23
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
?? claims/carrier-2026.yaml
?? scripts
```

**Agent**

I wrote `claims/carrier-2026.yaml`. The quote checker reports 29 claims, 29 quotes, 70 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the version of record (J Neurophysiol 135: 797–814, 2026): main text, Methods, all nine figure legends, Table 1 and Data availability. The paper has no supplement and cites none. It links no code repository. It says its scripts are in the two Zenodo records, but the archive file lists show no separate script files, so any scripts are inside the data zips, which I did not open. So no code was read.

**Claims.**
- **Totals:** 29 claims, all with quotes. 23 report statistics and 29 have criteria.
- **Crab, isolated nervous system (both datasets):** salinity at 10 °C (Fig. 1B, 1D, 1E); crash temperature in 0.75x and 1.25x saline (Fig. 2B, 2E); temperature sensitivity (Q10) in 0.75x and 1.25x (Fig. 2G, 2H); the frequency rise in 1.25x (Fig. 2F); the mixed-effects model; neuron crash counts and crash temperatures (Fig. 2I–K).
- **Lobster, isolated nervous system (`zenodo-17624449`):** Q10 (Fig. 3B); phase relationships (Table 1); salinity at 10 °C (Fig. 4B, 4D, 4E); LP crashing before PY (Fig. 5B); the mixed-effects model (Fig. 5C); Q10 across salinities (Fig. 5D); PY and LP crash temperatures across salinities (Fig. 6A, 6B).
- **Comparing the species (both datasets):** frequency at 10 °C; Q10 in each saline (Fig. 7A–C); crash temperatures (Fig. 7D–F).
- **Live animals (`zenodo-17794764`):** the rhythm holding during 1-hour salinity exposures (Fig. 8) and deaths after 15-hour exposures (Fig. 9).
- **Tolerances:** for means I used the standard error worked out from the stated SD and n, because the SD is the spread across preparations. This departs from the protocol's "stated spread" default, and the file gives the reason. For Q10 values I used half the width of the paper's 95% CI.

**Details the paper leaves open, with the readings named:**
- **Q10 fit:** a least-squares fit of the exponential model on raw frequency, or a linear fit of log frequency on temperature.
- **Fig. 3B points:** the fit uses either the step means (its F(1,8) implies about 10 points) or every preparation's values (the same Q10 appears again with a different CI and n = 19).
- **Crab mixed model:**
  - Which salinities are in it: 1x with 1.25x, 1x with 0.75x, or all three. The legend sits under the 1.25x figure, but n = 11 is the 0.75x set.
  - Whether salinity is a number or a factor, and whether the response is frequency or log frequency.
  - The random-slope candidates.
- **Lobster mixed model:** salinity as a number or a factor, and frequency or log frequency.
- **Fig. 7C temperature range:** 10–22, 10–24 or 10–28 °C.
- **Preparations with two 1x ramps (Fig. 7B, 7E):** use every ramp or only the first.
- **Frequency at 10 °C, n = 19 and 15:** taken from the first ramp step or from the baseline of the salinity series.
- **1x baseline segment for the salinity tests:** the end of the 30-minute baseline, or the 1x period just before the series.
- **Levene's test:** centred on the mean or the median.
- **Table 1 "95% CI" column:** I read it as the half-width; it could be a standard error.
- **Live-animal spectrograms:** the window settings are a standard choice that cannot change the outcome. Whether a frequency band counts as present has two readings: a peak-power rule over the full hour, or over the first 30 minutes.
- **Throughout:**
  - Burst detection criteria are not given.
  - Whether frequency is the mean of 1/period or a burst count is not given.

**Inconsistencies in the paper, recorded in the file:**
- The Fig. 4B legend gives n = 8 and the text n = 9.
- The Fig. 4D legend labels the 1.25x comparison as "0.75x" and gives P = 0.8 against 0.9 in the text.
- The Fig. 3C legend says PY-off changed with temperature; the text and Table 1 say PY-on. I followed Table 1.
- The Fig. 9 legend puts crabs in panel A; the text puts lobsters there.
- The Fig. 2 summary says 1.25x saline lowered frequency; the paragraph presenting Fig. 2F says it rose similarly.
- Crab 1x crash temperatures appear as three different means for different sets of preparations.
- The lobster 0.75x n is 10 in Fig. 5C and 14 in Fig. 7.

**Missing:**
- **Bar-graph percentages:** the PDF could not be rendered in this run, so I did not read the percentages in Figs. 1E, 4E and 9. Those claims use only the counts the text states, and the 15-hour mortality claim has no expected values.
- **Survival records:** the archive description does not say whether the 15-hour survival records are in the deposit.

## End of run

27 turns, 6 minutes, $2.05 at API prices, result: success.
