# 001048 · claims · run 39846798701

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls; ls paper claims claims/001453 claims/001048 2>&1; wc -l docs/protocol.md paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md
```

```
1:# Protocol for an attempt
36:## Reader
38:### 1. Get the paper
49:### 2. Read the paper's code
59:### 3. Write the claims file
142:### 4. Data from outside the paper's own recordings
150:### 5. Check
163:### 6. Answer questions
171:## Author
179:### 1. Establish what can be tested
277:### 2. Check the data against its description
292:### 3. Write the entry
341:### 4. Lock, check and run
352:### 5. Record the attempt
399:### 6. Hand over for verification
433:## Repeat attempts
446:## Local and remote datasets
469:## Verifier
473:### Round 1: without the author's conclusions
491:### Round 2: with the author's conclusions
[... 1 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 170
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-10`. Record this version in the attempt's provenance.
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
18	  claim, and it asks a reader for any method detail the file lacks.
19	- The **verifier** checks the author's work and must not be the author.
20	
[... 150 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/001453/10.1016-j.cub.2025.04.027.yaml"
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

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.xcrp.2025.102660.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
s=open('paper/10.1016-j.xcrp.2025.102660.txt').read(); print(s[52400:85000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/73cd39d9-f877-49bb-850c-9e33b94d4ede/tool-results/b877a12x5.txt"
}
```

```
1	ontinued for 250 ms during and about 90 ms after the stimulation, generating 1,200 images per stimulation session. After the first session, the stimulus amplitude was increased if no APs were detected or decreased to find the threshold if multiple APs were evoked. The imaging/stimulation sessions were repeated multiple times with 20–60 s intervals between them, either at escalating voltages or by choosing voltages randomly. In experiments aimed at determining the excitation thresholds ( Figure 2D ), the sine wave amplitude was adjusted up or down in 5%–10% steps until the minimal voltages eliciting 1 and 5 APs were determined. Next, we switched to a different stimulus type (e.g., from a modulated to an unmodulated signal or from 2 to 20 kHz) and repeated the search for the 1- and 5-AP thresholds. The emission intensity over the entire cell soma (F) was quantified using either Fiji ImageJ 1.53C (National Institutes of Health, USA) or MetaMorph 7.7 (Molecular Devices, San Jose, CA). The mean value over a time interval preceding the electrical stimulation was used as a 100% reference ( F 0 ) . Emission change in each frame ( Δ F ) in the sequence was determined as Δ F = 100 % × ( F − F 0 ) ∕ F 0 . APs were readily identifiable as brief emission upticks. For experiments, we selected neurons whose APs peaked at a more than 5% Δ F and lasted about 10 ms (typical values: 11.3% ± 0.9% Δ F and 8 ± 0.7 ms duration, excluding afterhyperpolarization; mean ± SEM, n = 22). Traces of the optical membrane potential were not filtered or modified in any way (except for long recordings in Figure 3C , which were corrected for bleaching by subtracting a trace without APs). The maximum AP firing rate was measured as the inverse of the peak-to-peak time interval between the first two APs evoked in each stimulation session. Traces of the optical membrane potential, as well as other graphs, were generated with Grapher v.16 software (Golden Software, Golden, CO). Pulsed laser fluorescence 
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
s=open('paper/10.1016-j.xcrp.2025.102660.txt').read(); i=s.find('Supplement',85000); print(len(s)); import re
for m in re.finditer(r'(?i)supplement|Table S1|Figure S1',s[85000:]): print(m.start()+85000, s[m.start()+85000-100:m.start()+85100].replace('\n',' '))" | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
s=open('paper/10.1016-j.xcrp.2025.102660.txt').read(); print(s[107400:])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -rl "001048" --include=* . 2>/dev/null | grep -v node_modules | head; ls targets | head
```

```
./targets/dandisets.json
./papers/manifest.yaml
crcns.json
dandisets.json
description_papers.yaml
ebrains.json
pilot.yaml
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
import itertools
for x in (items if isinstance(items,list) else items.values()):
  if '001048' in json.dumps(x)[:300]: print(json.dumps(x,indent=1)[:4000])
"; grep -n -B3 -A10 "001048" papers/manifest.yaml
```

```
1297-    source: ncbi_pmc+crossref (paper-text-fetcher)
1298-    pdf: false
1299-    supplements: 0
1300:  001048:
1301-  - doi: 10.1016/j.xcrp.2025.102660
1302-    status: stored
1303-    version: as served by europe_pmc
1304-    source: europe_pmc+crossref (paper-text-fetcher)
1305-    pdf: false
1306-    supplements: 1
1307-  '001051':
1308-  - doi: 10.1016/j.neuron.2024.06.015
1309-    status: stored
1310-    version: version of record
```

**Agent calls Bash**

```bash
cd  grep -n -B2 -A25 '"001048"' targets/dandisets.json | head -60
```

```
4394-  },
4395-  {
4396:   "dandiset": "001048",
4397-   "name": "Plasma membrane conductance changes in response to supraphysiological hyperpolarization",
4398-   "published_version": "0.250701.1624",
4399-   "asset_count": 7,
4400-   "size_gb": 4.79,
4401-   "data_standards": [
4402-    "Neurodata Without Borders (NWB)"
4403-   ],
4404-   "species": [
4405-    "Homo sapiens - Human"
4406-   ],
4407-   "approaches": [],
4408-   "papers": [
4409-    {
4410-     "doi": "10.1016/j.xcrp.2025.102660",
4411-     "title": "Excitation and polarization of isolated neurons by high-frequency sine waves for temporal interference stimulation",
4412-     "relation": "IsPublishedIn",
4413-     "resource_type": "JournalArticle",
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001048/versions/0.250701.1624/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('name'));print(d.get('description'));print(json.dumps(d.get('relatedResource'),indent=1));print(d.get('keywords'));print(json.dumps(d.get('contributor'),indent=0)[:1500]);print(d.get('dateCreated'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  grep -rli "different study\|not listed\|does not name\|mismatch" claims | head; ls claims/001271 claims/001272; head -30 claims/001271/*.yaml; python tools/claims_check.py --help 2>&1 | head -20
```

```
claims/001276/10.1016-j.bioelechem.2025.109016.yaml
claims/000004/10.1038-s41597-020-0415-9.yaml
claims/000128/10.1016-j.neuron.2010.09.015.yaml
claims/001676/10.1038-s41586-025-10096-w.yaml
claims/001271/10.1016-j.xcrp.2025.102660.yaml
claims/001341/10.1073-pnas.2514107123.yaml
claims/001828/10.1101-2024.12.22.629963.yaml
claims/001425/10.1101-2025.02.03.631599.yaml
claims/001277/10.1016-j.bioelechem.2025.109016.yaml
claims/000023/10.1101-2020.03.31.018820.yaml
claims/001271:
10.1016-j.xcrp.2025.102660.yaml

claims/001272:
10.1016-j.xcrp.2025.102660.yaml
# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,
# on dandiset 001271.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
# docs/protocol.md version pilot-10, as the reader.
#
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l claims/00127*/*.yaml; sed -n 30,80p claims/001271/*.yaml; grep -n "^- id:\|^checks" claims/001271/*.yaml; git log --oneline -3 -- claims/001271
```

```
552 claims/001271/10.1016-j.xcrp.2025.102660.yaml
   518 claims/001272/10.1016-j.xcrp.2025.102660.yaml
   520 claims/001273/10.1016-j.xcrp.2025.102660.yaml
   654 claims/001274/10.1016-j.xcrp.2025.102660.yaml
   536 claims/001276/10.1016-j.bioelechem.2025.109016.yaml
   436 claims/001277/10.1016-j.bioelechem.2025.109016.yaml
  3216 total
# recorded with 250-ms unmodulated or 20-Hz modulated sine waves at 2 and 20 kHz (Figures 1, 2), in
# NaCl (16.4 mS/cm) or sodium gluconate (8.4 mS/cm) solution (Figure 3A, 3B), with 2-s ramped 2-kHz
# sine waves (Figure 3C), with Di-8-ANEPPS on eight neurons (Figure S1) and with 1 uM tetrodotoxin
# (Figure S2). Strobe imaging with 2-us pulses and single sine wave beats measured membrane charging
# (Figures 4 to 6, S3).
#
# This dandiset. Its title and description on DANDI ("Tetrodotoxin Blockade of Sodium Channels
# Abolishes Action Potential Formation During Intense Sinewave Stimulation"; 1 uM TTX "suppressed
# action potentials, as expected, and completely prevented sustained depolarization") match the
# Figure S2 experiment. As the paper reports it, FluoVolt-stained neurons were stimulated by
# unmodulated 250-ms, 2-kHz sine waves at several field strengths (V/cm) in the standard NaCl
# solution, and again about 5 min after the solution was replaced by the same solution with 1 uM
# TTX (Tocris) or without it (vehicle control). The measured variable is the soma emission per
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 80,560p claims/001271/*.yaml
```

```
<persisted-output>
Output too large (30.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/73cd39d9-f877-49bb-850c-9e33b94d4ede/tool-results/bnwlbw11f.txt

Preview (first 2KB):
# (O3) AP detection is given only as "brief emission upticks", in neurons selected for APs above 5%
# dF lasting about 10 ms (typical 11.3% and 8 ms). An AP is a local maximum of dF with width at half
# height between 2 and 20 ms ("about 10 ms"; the bounds are a standard choice) and at least 5 ms
# from a larger maximum (standard choice; the paper's highest rates, 60 to 90 Hz, give intervals
# over 11 ms). Readings of the height (a) above 5% dF (the Methods' selection level), (b) above 5 SD
# of dF before the onset. After TTX, (a) and (b) are applied with the level of the same neuron's
# sessions before the change, so that a drop of the baseline noise cannot create APs.
# (O4) "Sustained depolarization" is not defined by a measure. It is no AP in the last 100 ms of the
# stimulus while the mean dF over that window is above, reading (a) 5 SD of dF before the onset,
# (b) half the median AP height of the neuron before the change. The 100-ms window is a standard
# choice. "Sustained firing" is, as a standard choice, at least three APs with one in the last 50 ms
# of the stimulus.
# (O5) Which session pairs are compared before and after the change is not stated beyond the
# legend's "recorded first ... and again"; readings (a) every field tested both before and after,
# (b) only the highest field tested both before and after.
schema_version: 2
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/73cd39d9-f877-49bb-850c-9e33b94d4ede/tool-results/bnwlbw11f.txt",
 "offset": 120
}
```

```
120	    no vehicle neuron.
121	- id: ap-amplitude-duration
122	  statement: Neurons were selected for APs peaking above 5% dF and lasting about 10 ms; typical APs
123	    were 11.3% dF high and 8 ms long, excluding the afterhyperpolarization.
124	  source: Methods, Recording of the optical APs and data analyses
125	  quote: we selected neurons whose APs peaked at a more than 5% Δ F and lasted about 10 ms (typical
126	    values ... 11.3% ± 0.9% Δ F and 8 ± 0.7 ms duration, excluding afterhyperpolarization ... mean ±
127	    SEM, n = 22)
128	  expected:
129	  - quantity: mean AP peak over neurons
130	    value: 11.3
131	    tolerance: 0.9
132	    unit: percent dF
133	  - quantity: mean AP duration over neurons
134	    value: 8
135	    tolerance: 0.7
136	    unit: ms
137	  criterion: F1 and F2, under O1 to O3, sessions before the change. The paper does not say which 22
138	    neurons these are or which experiments they come from; the neurons of this dataset are tested
139	    as neurons the same selection was applied to, and a mismatch may come from that. Per neuron,
[... 335 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));
c=s['\$defs'] if '\$defs' in s else s.get('definitions');print(json.dumps(c.get('claim',c),indent=1)[:3500])"
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
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));
import re;t=json.dumps(s,indent=1);i=t.find('\"data\"');print(t[i-200:i+1800])"
```

```
cription": "Ids of claims in this file whose result this one uses.",
      "type": "array",
      "items": {
       "type": "string",
       "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"
      }
     },
     "data": {
      "description": "What the claim's test uses: the dataset alone (`dataset`, the default); the dataset with names for its own codes taken from elsewhere (`with_labels`), which counts as the dataset; the dataset with other data from elsewhere (`with_inputs`), which is counted apart; or data the paper deposited in another public archive, which the dataset does not hold (`elsewhere`), counted apart from both. Outside sources that a test uses are listed under `inputs` in the attempt.",
      "enum": [
       "dataset",
       "with_labels",
       "with_inputs",
       "elsewhere"
      ]
     },
     "where": {
      "description": "For a claim with data `elsewhere`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
      "type": "string",
      "minLength": 1
[... 56 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
for x in d:
  if x['dandiset'] in '001030 001031 001032 001033 001034 001035 001271 001272 001273 001274 001048'.split(): print(x['dandiset'],x['name'],x['species'],[p['doi'] for p in x['papers']])"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 4, in <module>
    if x['dandiset'] in '001030 001031 001032 001033 001034 001035 001271 001272 001273 001274 001048'.split(): print(x['dandiset'],x['name'],x['species'],[p['doi'] for p in x['papers']])
       ~^^^^^^^^^^^^
TypeError: string indices must be integers, not 'str'
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
L=[v for v in d.values() if isinstance(v,list)][0]
for x in L:
  if x['dandiset'] in '001030 001031 001032 001033 001034 001035 001271 001272 001273 001274 001048'.split(): print(x['dandiset'],x['name'],x['species'],[p['doi'] for p in x['papers']])"
```

```
001048 Plasma membrane conductance changes in response to supraphysiological hyperpolarization ['Homo sapiens - Human'] ['10.1016/j.xcrp.2025.102660']
001271 Tetrodotoxin Blockade of Sodium Channels Abolishes Action Potential Formation During Intense Sinewave Stimulation ['Rattus norvegicus - Norway rat'] ['10.1016/j.xcrp.2025.102660']
001272 The Use of Di8-ANEPPS to Evaluate Neuronal Sensitivity to Unmodulated Sine Waves ['Rattus norvegicus - Norway rat'] ['10.1016/j.xcrp.2025.102660']
001273 Kinetics of Membrane Charging and Its Dependence on Neuron Shape and Alignment with the Electric Field ['Rattus norvegicus - Norway rat'] ['10.1016/j.xcrp.2025.102660']
001274 Characterization of Plasma Membrane Polarization in Hippocampal Neurons During Sine Wave and Modulated Sine Wave Stimulation ['Rattus norvegicus - Norway rat'] ['10.1016/j.xcrp.2025.102660']
```

**Agent calls Bash**

```bash
for i in 001030 001031 001032 001033 001034 001035; do curl -s https://api.dandiarchive.org/api/dandisets/$i/ | python3 -c "import json,sys;d=json.load(sys.stdin);print('$i',d['most_recent_published_version']['name'] if d.get('most_recent_published_version') else d['draft_version']['name'])"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
for i in 001030 001032 001033 001034 001035 001271 001272 001273 001274; do curl -s https://api.dandiarchive.org/api/dandisets/$i/ | python3 -c "import json,sys;d=json.load(sys.stdin);v=d.get('most_recent_published_version');print('$i',v['version'] if v else 'draft only')"; done
```

Result: the fetched text is not kept.

**Agent calls Write**

```json
{
 "file_path": "claims/001048/10.1016-j.xcrp.2025.102660.yaml",
 "content": "# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,\n# on dandiset 001048.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, under\n# docs/protocol.md version pilot-10, as the reader.\n#\n# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC: main\n# text, figure legends and STAR Methods, with the supplement (NIHMS2098259-supplement-1.pdf, Figures\n# S1 to S4 and Table S1, the Key Resource Table), all in paper/10.1016-j.xcrp.2025.102660.txt. The\n# version of record was not read. There is no PDF of the main text, so Figures 1 to 6 were not seen;\n# no claim needed a figure the text does not describe.\n#\n# Code. The paper states \"This paper does not report original code\". It names the software used:\n# Fiji ImageJ 1.53C or MetaMorph 7.7 for soma emission, Grapher 16 for traces and linear regression,\n# Origin 8.0 for exponential fits and their standard errors, Sim4Life 5.2 for the field, and RStudio\n# in Table S1. No repository was read, so no method detail below is settled by code.\n#\n# This dandiset does not hold the paper's data. Its title and description on DANDI (version\n# 0.250701.1624) are \"Plasma membrane conductance changes in response to supraphysiological\n# hyperpolarization\", a study of membrane lesions made by hyperpolarization in HEK cells (\"diffuse\n# zonal electropermeabilization, focal pores, and high-conductance pores\"), species Homo sapiens. The\n# paper has no HEK cells and no hyperpolarization lesion experiment, and its Data and code\n# availability lists ten dandisets (001030 to 001035 and 001271 to 001274), not 001048. The two share\n# authors and NIH grants (R21EY034258, R21EY034803), which may be why the dandiset names the paper.\n# Every claim below is therefore data elsewhere. The paper does not say which figure is in which\n# dandiset; from their titles on DANDI only, 001030 (2-kHz sine waves, the effect of the field) and\n# 001032 to 001035 (action potential triggering by sine waves at varying frequencies, parts 1 to 4)\n# hold the FluoVolt experiments of Figures 1 to 3, 001271 tetrodotoxin (Figure S2), 001272\n# Di-8-ANEPPS (Figure S1), 001273 the 2-us pulse charging kinetics (Figure 4) and 001274 sine wave\n# polarization (Figures 5, 6 and S3). 001031 (100-kHz bipolar pulses) matches no figure. Versions\n# are those published on DANDI on 2026-10-22.\n#\n# Data the paper used. E18 Sprague-Dawley rat hippocampal neurons (BrainBits), cultured about one\n# week on 12-mm coverslips. One neuron, its soma touching no other cell, centred between the tips of\n# a bipolar tungsten electrode (two 100-um rods, 120-um gap, 45 degrees, 50 um above the coverslip).\n# Optical membrane potential by fast imaging (64 x 64 pixels after 4 x 4 binning, 3,130 or 3,086.4\n# frames/s), 1,200 images per session, 50 ms before, 250 ms during and about 90 ms after the\n# stimulus, sessions 20 to 60 s apart, fields escalated or in a random order. Measured variable is\n# the emission over the entire soma, as dF = 100% (F - F0)/F0. Most neurons were stained with\n# FluoVolt and stimulated with 250-ms unmodulated or 20-Hz modulated sine waves at 2 and 20 kHz\n# (Figures 1, 2), in NaCl (16.4 mS/cm) or sodium gluconate (NaGlu, 8.4 mS/cm) solution at 2 to 20\n# kHz (Figures 3A, 3B), or with a 2-s, 2-kHz wave ramped over 250 ms in NaGlu (Figure 3C); eight\n# neurons with Di-8-ANEPPS (Figure S1); neurons before and about 5 min after 1 uM tetrodotoxin or\n# vehicle (Figure S2). Strobe imaging (6-ns laser flashes, 50-ns steps) of 2-us, 140 V/cm pulses\n# from two orthogonal directions in 19 experiments (Figure 4, three-electrode array 1.4 mm apart),\n# and of 2-us, 257 V/cm pulses and single beats of 2-kHz sine waves modulated at 100 or 154 Hz in\n# 20-us steps in 9 cells (Figures 5, 6, S3), with ROIs over the most de- and hyperpolarized regions.\n#\n# Method details fixed from the paper, used by the criteria.\n# (F1) F is the mean emission over the entire cell soma per frame, F0 its mean over an interval\n# before the stimulus, dF = 100% (F - F0)/F0 (Methods, Recording of the optical APs). FluoVolt\n# emission rises with depolarization; Di-8-ANEPPS traces are inverted (Methods; Figure S1 legend).\n# (F2) Traces are not filtered or modified, except the 2-s recordings of Figure 3C, corrected for\n# bleaching by subtracting a trace without APs (Methods).\n# (F3) The stimulus starts 50 ms into the session and lasts 250 ms (Results; Methods), 2 s for\n# Figure 3C; the dataset's own stimulus record is used where it has one.\n# (F4) The maximum firing rate of a session is the inverse of the peak-to-peak interval between its\n# first two APs (Methods).\n# (F5) A threshold is the minimum field eliciting at least 1 or at least 5 APs during the 250-ms\n# stimulus (Figure 2D and 3B legends), found by 5% to 10% steps (Methods).\n# (F6) The test, where the paper names none, is a two-sided Student's t test, paired or unpaired as\n# appropriate, at p < 0.05 (Methods, Quantification and statistical analysis); error bars are SEM.\n# (F7) Strobe data (Methods, Pulsed laser fluorescence microscopy). F per frame in the de- and\n# hyperpolarized ROIs, scaled to a debris ROI; F0 the mean before the pulse, or for sine waves the\n# mean over the first and last cycles; charging fit dF = dFmax (1 - exp(-t/tau)) over time into the\n# pulse, discharging fit dF = dFmax exp(-t/tau) over time after it. The pulse sensitivity is dF\n# averaged from 1 to 2 us into the pulse, normalized to 1 kV/cm (Results; Figure 6B legend); the sine\n# sensitivity is the regression coefficient of the oscillation, after subtraction of a LOESS fit of\n# the whole-cell response, on the field (Results; Figure 6C legend).\n#\n# Details the paper leaves open, with the readings named. Each criterion that uses one runs every\n# reading; a claim is decided when all readings give its outcome, and blocked as\n# methods_underspecified when they give different outcomes.\n# (O1) The soma outline is not given. ROIs are taken from the dataset when it holds them; otherwise\n# readings (a) the connected component nearest the image centre (the Methods centre the neuron) of\n# an Otsu threshold of the mean pre-stimulus frame, (b) that mask eroded by 2 pixels. Otsu and the 2\n# pixels are standard choices.\n# (O2) The F0 interval is \"a time interval preceding the electrical stimulation\"; readings (a) all\n# frames before the onset, (b) the last 20 ms before it.\n# (O3) AP detection is given only as \"brief emission upticks\", in neurons selected for APs above 5%\n# dF lasting about 10 ms. An AP is a local maximum with width at half height of 2 to 20 ms and at\n# least 5 ms from a larger maximum (standard choices; 60 to 90 Hz gives intervals over 11 ms), with\n# height readings (a) above 5% dF, (b) above 5 SD of dF before the onset.\n# (O4) \"Sustained depolarization\" has no measure. It is no AP in the last 100 ms of the stimulus\n# while the mean dF there is above, reading (a) 5 SD of dF before the onset, (b) half the median AP\n# height of the neuron. The 100-ms window is a standard choice.\n# (O5) Scaling to the debris ROI. The paper processed data with and without it (Methods); readings\n# (a) scaled, (b) unscaled.\n# (O6) The LOESS span of Figure 5 is not given; readings (a) a span of 2 ms, (b) 4 ms (about 4 and 8\n# carrier cycles at 2 kHz), standard choices that follow the envelope but not the carrier.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001048\"\npaper: doi:10.1016/j.xcrp.2025.102660\nclaims:\n- id: ap-selection\n  statement: Neurons were selected for APs peaking above 5% dF and lasting about 10 ms; typical APs\n    were 11.3% dF high and 8 ms long, excluding the afterhyperpolarization (mean of 22).\n  source: Methods, Recording of the optical APs and data analyses\n  quote: we selected neurons whose APs peaked at a more than 5% Δ F and lasted about 10 ms (typical\n    values ... 11.3% ± 0.9% Δ F and 8 ± 0.7 ms duration, excluding afterhyperpolarization; mean ±\n    SEM, n = 22)\n  data: elsewhere\n  where: DANDI:001030 (0.240520.1924) and 001032 to 001035 (0.240527.1431 or 0.240527.1432), assigned\n    from their titles; the paper does not say which 22 neurons these are\n  expected:\n  - quantity: mean AP peak over neurons\n    value: 11.3\n    tolerance: 0.9\n    unit: percent dF\n  - quantity: mean AP duration over neurons\n    value: 8\n    tolerance: 0.7\n    unit: ms\n  criterion: F1 to F3, O1 to O3, FluoVolt sessions with APs. Per neuron, the mean peak dF and\n    duration of its APs, then the mean over neurons. Which APs are measured is not given; readings\n    (a) every AP, (b) the first AP of each session. The duration measure is not given; readings (a)\n    width at half height, (b) time from the rise to the first return to F0 (leaving out the\n    afterhyperpolarization). Reproduced when both means are within the paper's SEM under every\n    reading.\n- id: fig1-pure-sine-excites-all\n  statement: Unmodulated 250-ms sine waves at 2 and 20 kHz excited every neuron tested; near\n    threshold isolated APs came 100 to 200 ms after onset, and stronger fields shortened the delay\n    and evoked sustained firing whose maximum rate rose linearly to a ceiling of 60 to 90 Hz.\n  source: Results, Stimulation by 2- and 20-kHz unmodulated sine waves, paragraph 2; Figures 1A to 1C\n    and inset\n  quote: Pure sine waves at 2 and even 20 kHz excited 100% of neurons ... at near-threshold electric\n    field strengths, isolated APs emerged with a delay of 100–200 ms after the sine wave onset ...\n    Increasing the field strength reduced this delay and evoked sustained firing ... The maximum\n    firing rate increased linearly until reaching a ceiling of 60–90 Hz\n  data: elsewhere\n  where: DANDI:001030 (0.240520.1924) and 001032 to 001035 (0.240527.1431 or 0.240527.1432), assigned\n    from their titles\n  expected:\n  - quantity: fraction of neurons excited, each frequency\n    value: 100\n    tolerance: 10\n    unit: percent\n  criterion: F1 to F5, O1 to O3, FluoVolt sessions with unmodulated waves. A neuron's threshold is\n    its lowest field with at least one AP (F5). Reproduced when, under every reading, at least 90%\n    of neurons are excited at each frequency, the median first-AP latency at threshold lies within\n    90 to 220 ms (100 to 200 ms widened by 10% of each bound), latency falls with field (Spearman\n    rho below 0 over a neuron's sessions with APs, in most neurons), and the median over neurons of\n    the highest maximum firing rate lies within 54 to 99 Hz. Whether the ceiling is meant for the\n    median neuron or for each neuron is open (the inset shows three neurons); readings (a) the\n    median, (b) at least 75% of neurons within 54 to 99 Hz; both are run under the header's rule.\n- id: fig1-excitation-block\n  statement: At the highest fields, unmodulated sine waves merged APs into low-amplitude oscillations\n    on a continuous depolarization, which could flatten and leave the membrane depolarized for the\n    rest of the stimulus (an excitation block), and this depolarization reversed immediately when the\n    stimulus stopped.\n  source: Results, Stimulation by 2- and 20-kHz unmodulated sine waves, paragraph 2; Results,\n    Tetrodotoxin blocks sustained depolarization, paragraph 1; Figure 1\n  quote: At the highest field strengths, multiple APs coalesced into low-amplitude oscillations on top\n    of a continuous depolarization. These oscillations could flatten after several cycles, leaving\n    the membrane depolarized for the rest of the sine wave\n  data: elsewhere\n  where: DANDI:001030 (0.240520.1924) and 001032 to 001035 (0.240527.1431 or 0.240527.1432), assigned\n    from their titles\n  criterion: F1 to F3, O1 to O4. The paper gives no count of neurons that reached the block.\n    Reproduced when, under every reading, most neurons tested at fields above the one giving their\n    highest maximum firing rate show sustained depolarization (O4) at their highest field, and in\n    those sessions the mean dF over the 50 ms after the stimulus ends is below the O4 level. The\n    50-ms window is a standard choice.\n- id: fig1-20khz-needs-twice-the-field\n  statement: All excitation thresholds at 20 kHz were about 2-fold higher than at 2 kHz.\n  source: Results, Excitation thresholds are similar or lower for pure 2- and 20-kHz sine waves than\n    those for modulated sine waves, paragraph 1; Figure 2D\n  quote: All thresholds at 20 kHz were about 2-fold higher than at 2 kHz ( p < 0.0001, two-tailed\n    unpaired t test)\n  statistics:\n  - about: 20 kHz against 2 kHz thresholds\n    test: two-tailed unpaired t test\n    p: 0.0001\n    p_relation: \"<\"\n  data: elsewhere\n  where: DANDI:001032 to 001035 (0.240527.1431 or 0.240527.1432), assigned from their titles\n  expected:\n  - quantity: ratio of mean 20-kHz to mean 2-kHz threshold, for each stimulus type and AP count\n    value: 2\n    tolerance: 0.2\n  criterion: Thresholds (F5) for 1 and 5 APs, modulated and unmodulated, under O1 to O3. The paper\n    gives one p for \"all thresholds\"; readings (a) one test per stimulus type and AP count, each\n    p < 0.0001, (b) one test pooling the four. Reproduced when the four ratios are within tolerance\n    and the test reaches p < 0.0001, under every reading.\n- id: fig2d-5ap-above-1ap\n  statement: All thresholds to elicit 5 APs were higher than those for 1 AP.\n  source: Results, Excitation thresholds are similar or lower for pure 2- and 20-kHz sine waves than\n    those for modulated sine waves, paragraph 1; Figure 2D\n  quote: All thresholds to elicit 5 APs were expectedly higher than those for 1 AP\n  data: elsewhere\n  where: DANDI:001032 to 001035 (0.240527.1431 or 0.240527.1432), assigned from their titles\n  criterion: Thresholds as in fig1-20khz-needs-twice-the-field. The paper reports no test.\n    Reproduced when, for each of the four stimuli (2 and 20 kHz, modulated or not), the mean 5-AP\n    threshold is above the mean 1-AP threshold, under every reading.\n- id: fig2d-modulated-thresholds-higher\n  statement: Thresholds for sine waves modulated at 20 Hz were significantly higher than for pure\n    sine waves at the same carrier frequency for 5 APs at 2 kHz and for 1 and 5 APs at 20 kHz, so\n    modulation did not lower excitation thresholds; the 2-kHz unmodulated AP threshold was 57.7 ±\n    3.6 V/cm.\n  source: Results, Excitation thresholds are similar or lower for pure 2- and 20-kHz sine waves than\n    those for modulated sine waves, paragraph 1; Figure 2D and legend; Results, Asymmetric and\n    less-efficient membrane charging by sine waves compared to pulses, last paragraph\n  quote: thresholds for modulated sine waves, which emulate the TI stimulus at the target, were\n    significantly higher than those for pure sine waves at the same frequency (for 2 kHz, 5 APs ... p\n    = 0.0079; for 20 kHz, 1 and 5 APs, respectively ... p = 0.0142 and p = 0.0037). Thus, modulated\n    sine waves were equally or less efficient than pure ones at eliciting APs\n  statistics:\n  - about: modulated against unmodulated, 2 kHz, 5 APs\n    test: two-tailed unpaired t test\n    p: 0.0079\n  - about: modulated against unmodulated, 20 kHz, 1 AP\n    test: two-tailed unpaired t test\n    p: 0.0142\n  - about: modulated against unmodulated, 20 kHz, 5 APs\n    test: two-tailed unpaired t test\n    p: 0.0037\n  data: elsewhere\n  where: DANDI:001032 to 001035 (0.240527.1431 or 0.240527.1432), assigned from their titles\n  expected:\n  - quantity: mean unmodulated 2-kHz threshold\n    value: 57.7\n    tolerance: 3.6\n    unit: V/cm\n  criterion: Thresholds as in fig1-20khz-needs-twice-the-field; two-tailed unpaired t tests, as the\n    Figure 2D legend names them (the Methods allow paired tests, and the thresholds come from the\n    same neurons; a paired test is shown as a variant). Reproduced when, under every reading, the\n    three modulated thresholds are higher at p < 0.05, the 2-kHz 1-AP thresholds do not differ in the\n    other direction at p < 0.05, and the mean 2-kHz unmodulated threshold is within the paper's SEM.\n    The paper calls 57.7 V/cm \"the AP threshold\" without saying 1 or 5 APs; it is read as the 1-AP\n    threshold, the excitation threshold of Figure 3B, and the 5-AP mean is reported beside it.\n- id: fig2-modulated-locks-to-beats\n  statement: With 20-Hz modulation, firing above threshold locked to the beats, one AP near the peak\n    of each of the five beats and at most two per beat (ten in all), and modulated sine waves\n    triggered no sustained firing or sustained depolarization.\n  source: Results, Stimulation by 2- and 20-kHz sinusoids modulated at 20 Hz, paragraph 1; Figures 2A\n    and 2B\n  quote: single APs emerged near the peak of each beat, so the firing rate equaled the modulation\n    rate ... At the highest field strengths, each beat could elicit a pair of APs, so the maximum\n    number of APs evoked by five beats was limited to ten. Unlike pure sine waves, modulated stimuli\n    did not trigger sustained firing or sustained depolarization\n  data: elsewhere\n  where: DANDI:001032 to 001035 (0.240527.1431 or 0.240527.1432), assigned from their titles\n  criterion: F1 to F3, O1 to O4, modulated sessions only. The 250-ms wave holds five 50-ms beats\n    (Results), and modulated waves start and end at minimal amplitude (Methods, Pulsed laser\n    fluorescence microscopy), so each beat peaks 25 ms into it; the dataset's stimulus record is\n    used when it gives the envelope. \"Near the peak\" is not quantified; as standard choices,\n    reproduced when no session has more than 10 APs, in sessions with at least 5 APs most APs fall\n    12.5 to 37.5 ms into a beat, and no session shows sustained depolarization (O4), under every\n    reading.\n- id: fig2c-pure-more-aps\n  statement: In the same neuron, the threshold was typically lower for unmodulated sine waves, and at\n    the same field strength pure sine waves triggered more APs than modulated ones.\n  source: Results, Stimulation by 2- and 20-kHz sinusoids modulated at 20 Hz, paragraph 2; Figures 2A\n    to 2C\n  quote: When modulated and unmodulated sine waves of the same carrier frequency were tested in the\n    same cell, the threshold was typically lower for unmodulated signals ( Figures 2A - 2C ). At the\n    same field strengths, pure sine waves triggered a larger number of APs\n  data: elsewhere\n  where: DANDI:001032 to 001035 (0.240527.1431 or 0.240527.1432), assigned from their titles\n  criterion: F1 to F3, O1 to O3. Pairs are a neuron's modulated and unmodulated sessions at the same\n    carrier and field. The paper reports no test. Reproduced when, under every reading, the\n    unmodulated AP count is larger in more pairs than the reverse and the unmodulated 1-AP\n    threshold is lower in more neurons than the reverse. A two-sided paired t test of the counts\n    (F6) is reported.\n- id: fig3b-low-conductivity-halves-threshold\n  statement: Replacing NaCl with sodium gluconate, which lowered the solution conductivity from 16.4\n    to 8.4 mS/cm, reversibly lowered excitation thresholds about 2-fold at every sine wave frequency\n    from 2 to 20 kHz.\n  source: Results, Decreased extracellular conductivity lowers excitation thresholds, paragraph 2;\n    Figures 3A and 3B\n  quote: Switching to the NaGlu-based solution reversibly and reproducibly decreased excitation\n    thresholds ~2-fold across all sine wave frequencies tested\n  data: elsewhere\n  where: DANDI:001030 (0.240520.1924) and 001032 to 001035 (0.240527.1431 or 0.240527.1432), assigned\n    from their titles\n  expected:\n  - quantity: ratio of mean NaCl to mean NaGlu 1-AP threshold, each frequency\n    value: 2\n    tolerance: 0.2\n  criterion: 1-AP thresholds (F5) for unmodulated waves per frequency and solution, 4 to 8 neurons\n    per point (Figure 3B legend), O1 to O3. Reproduced when the ratio is within tolerance at every\n    frequency, under every reading. That the threshold returns on switching back to NaCl\n    (reversibly) is reported per neuron where the dataset holds a return; the paper gives no measure\n    of it.\n- id: fig3-extrapolated-threshold\n  statement: Extrapolated to a 2 mS/cm solution, excitation by 2-kHz sine waves would be expected at\n    about 7 V/cm.\n  source: Results, Decreased extracellular conductivity lowers excitation thresholds, paragraph 2\n  quote: Extrapolating this trend to still lower conductivities, excitation by 2-kHz sine waves would\n    be expected at ~7 V/cm in a 2 mS/cm solution\n  data: elsewhere\n  where: DANDI:001030 (0.240520.1924) and 001032 to 001035 (0.240527.1431 or 0.240527.1432), assigned\n    from their titles\n  depends_on:\n  - fig3b-low-conductivity-halves-threshold\n  expected:\n  - quantity: extrapolated 2-kHz threshold at 2 mS/cm\n    value: 7\n    tolerance: 0.7\n    unit: V/cm\n  criterion: From the mean 2-kHz 1-AP thresholds in NaCl and NaGlu of\n    fig3b-low-conductivity-halves-threshold. The paper does not say how it extrapolated (the Figure\n    3B fits are over frequency, not conductivity); readings (a) threshold proportional to\n    conductivity, from the NaCl mean, (b) a straight line through the two conductivities, (c) an\n    exponential through the two. Reproduced when the value is within tolerance under every reading.\n- id: fig3-not-heating\n  statement: Excitation by pure sine waves was not caused by heating; the adiabatic temperature rise\n    was 2.5 C after 250 ms at 63 V/cm in NaCl, at most 1.24 C for the same stimulus in the\n    low-conductivity solution, where it evoked sustained firing, and 4.1 C at 81 V/cm in NaCl.\n  source: Results, Decreased extracellular conductivity lowers excitation thresholds, paragraph 3;\n    Figure 3A\n  quote: the maximum theoretical temperature rise (assuming no heat dissipation 43 ) was 2.5°C after\n    250 ms of near-threshold stimulation at 2 kHz, 63 V/cm, in the NaCl-based solution ( Figure 3A ).\n    The same stimulation in the low-conductance solution elicited sustained neuron firing while the\n    temperature rise would not exceed 1.24°C ... 81 V/cm in the NaCl solution, which would heat by\n    4.1°C in the adiabatic conditions. These observations prove that excitation by pure sine waves\n    was not caused by heating\n  data: elsewhere\n  where: DANDI:001030 (0.240520.1924) or 001032 to 001035 (0.240527.1431 or 0.240527.1432) for the\n    Figure 3A neuron, assigned from their titles; the temperatures are calculated, not measured\n  expected:\n  - quantity: adiabatic rise, 63 V/cm, 250 ms, 16.4 mS/cm\n    value: 2.5\n    tolerance: 0.25\n    unit: degrees C\n  - quantity: adiabatic rise, 63 V/cm, 250 ms, 8.4 mS/cm\n    value: 1.24\n    tolerance: 0.124\n    unit: degrees C\n  - quantity: adiabatic rise, 81 V/cm, 250 ms, 16.4 mS/cm\n    value: 4.1\n    tolerance: 0.41\n    unit: degrees C\n  criterion: The rise is conductivity times E squared times duration over the volumetric heat\n    capacity (no dissipation, reference 43). The paper does not give the heat capacity or whether E\n    is the peak or the RMS field; readings (a) peak, (b) RMS, each with the heat capacity of water\n    (4.18 J per cm3 per K, a standard choice). From the paper's values neither gives 2.5 C (peak\n    about 3.9 C, RMS about 1.95 C), while the ratios 4.1/2.5 and 1.24/2.5 follow the scaling with E\n    squared and conductivity. Reproduced when all three are within tolerance under a reading;\n    blocked as methods_underspecified when none is but both ratios are within 10%; not reproduced\n    when the ratios fail. That the Figure 3A neuron fired in NaGlu at 63 V/cm (O3) and showed\n    firing in NaCl at 81 V/cm like that in NaGlu at 63 V/cm is reported where the dataset holds it.\n- id: fig3c-sustained-firing-2s\n  statement: In the low-conductivity solution, a 2-s unmodulated 2-kHz sine wave ramped up over 250\n    ms evoked firing for its whole duration; the firing rate rose with field until replaced by a\n    firing block with sustained depolarization, which developed before the end of the ramp.\n  source: Results, Decreased extracellular conductivity lowers excitation thresholds, paragraph 4;\n    Figure 3C\n  quote: we observed sustained firing for the entire duration of the sine wave ( Figure 3C ). The rate\n    of firing increased with the electric field strength until it was replaced by a firing block\n    and sustained depolarization. The block had already developed before the end of the 250-ms\n    ramp-up period\n  data: elsewhere\n  where: DANDI:001030 (0.240520.1924), assigned from its title\n  criterion: F1 to F3 (with the bleaching correction of F2), O1 to O3. Reproduced when, under every\n    reading, some field has APs in the last 250 ms of the 2-s stimulus, the AP count rises with field\n    up to some field, and the highest field shows no AP and a mean dF above the O4 level from 250 ms\n    after onset to the end. The windows follow the 250-ms ramp of the legend; the last-250-ms window\n    is a standard choice.\n- id: figs1-di8-same-as-fluovolt\n  statement: With Di-8-ANEPPS in place of FluoVolt, in eight neurons, 2-kHz sine waves near threshold\n    elicited one or a few delayed APs, and stronger fields shortened the delay and induced sustained\n    firing ending in sustained depolarization, as with FluoVolt.\n  source: Results, Sensitivity to unmodulated sine waves was not caused by FluoVolt dye, paragraph 2;\n    Figure S1\n  quote: Experiments were performed on eight neurons using different electric field strengths tested\n    in a random sequence ... Stimulation near the threshold elicited one or a few delayed APs.\n    Increasing the electric field strength reduced the delay and induced sustained firing that\n    culminated in sustained depolarization. Overall, stimulation effects were not different from\n    those observed with FluoVolt dye\n  data: elsewhere\n  where: DANDI:001272 (0.250805.1358), assigned from its title\n  expected:\n  - quantity: neurons tested with Di-8-ANEPPS\n    value: 8\n  criterion: F1 (traces inverted), F2, F3, O1 to O4; O3 reading (a) uses 5% of the inverted trace\n    only if the Di-8-ANEPPS APs reach it, as its traces are noisier (Results), otherwise reading (b)\n    alone. The paper gives no test of \"not different\". Reproduced when eight neurons are found and,\n    under every reading, most show APs at their lowest field with APs, a first-AP latency that falls\n    with field, and sustained firing or sustained depolarization (O4) at higher fields.\n- id: figs2-ttx-blocks-depolarization\n  statement: 1 uM tetrodotoxin abolished both the APs and the sustained depolarization evoked by\n    intense unmodulated 2-kHz sine waves, while the vehicle did not.\n  source: Results, Tetrodotoxin blocks sustained depolarization, paragraph 1; Figure S2 legend\n  quote: the inhibition of sodium channels with 1 μM tetrodotoxin not only abolished the APs but also\n    fully blocked the sustained depolarization\n  data: elsewhere\n  where: DANDI:001271 (0.250805.1352), assigned from its title\n  criterion: F1 to F3, O1 to O4, sessions before and about 5 min after the change of solution (Figure\n    S2 legend). Reproduced when, under every reading, every TTX neuron has APs or sustained\n    depolarization before and neither after at the same fields, and every vehicle neuron keeps APs\n    or sustained depolarization at the same fields. The paper gives no count of neurons or test.\n- id: fig4-pooled-time-constants\n  statement: Membrane charging by 2-us pulses is fast; pooled over 19 experiments, charging and\n    discharging time constants averaged 0.7 and 0.91 us at the cathodic pole and 0.65 and 0.8 us at\n    the anodic pole, so the membrane charges fully within each sine wave cycle up to 100 to 200 kHz.\n  source: Results, Kinetics of membrane charging by pulsed electric fields, the paragraph after the\n    Figure 4 legend; Figures 4D and 4E\n  quote: The time constants pooled together for all cells averaged 0.7 ± 0.08 (charging) and 0.91 ±\n    0.08 (discharging) μs for the cathodic cell pole and 0.65 ± 0.05 and 0.8 ± 0.07 μs for the\n    anodic pole, respectively (mean ± SEM, n = 19)\n  data: elsewhere\n  where: DANDI:001273 (0.250805.1356), assigned from its title\n  expected:\n  - quantity: charging tau, cathodic pole\n    value: 0.7\n    tolerance: 0.08\n    unit: us\n  - quantity: discharging tau, cathodic pole\n    value: 0.91\n    tolerance: 0.08\n    unit: us\n  - quantity: charging tau, anodic pole\n    value: 0.65\n    tolerance: 0.05\n    unit: us\n  - quantity: discharging tau, anodic pole\n    value: 0.8\n    tolerance: 0.07\n    unit: us\n  criterion: F7, O5. Per experiment (a cell in one field direction) and pole, dF averaged over the\n    eight replicates (Results) and fitted by least squares with the charging function from pulse\n    onset to pulse end and the discharging function from pulse end to the last frame; means over\n    the 19 experiments. Where the discharging fit starts and whether dFmax is shared between the two\n    fits are not given; readings (a) separate dFmax per fit, (b) the discharging fit's amplitude\n    fixed to the dF at pulse end. Reproduced when all four means are within the paper's SEM under\n    every reading.\n- id: fig4-orientation-and-poles\n  statement: Aligning elongated cells with the field doubled the time constants compared with the same\n    cells perpendicular to it or with randomly shaped cells; dFmax and the time constants did not\n    differ between the cathode- and anode-facing poles; and discharging was slower than charging\n    except in elongated cells aligned with the field.\n  source: Results, Kinetics of membrane charging by pulsed electric fields, the two paragraphs after\n    the Figure 4 legend; Figures 4D and 4E and legend\n  quote: Δ F max did not differ at the cathodic and anodic cell poles, indicating the lack of\n    rectification of the applied electric field. Charging and discharging time constants did not\n    differ between the two poles either. Aligning elongated cells with the electric field doubled the\n    time constants, as compared to either the same cells oriented perpendicular to the field ( p <\n    0.001, paired t test) or to randomly shaped cells ( p < 0.01, unpaired t test). Interestingly,\n    discharging time constants were always larger than the charging ones in the same cell ( p <\n    0.001, paired t test), with the exception of elongated cells aligned with the field\n  statistics:\n  - about: elongated cells, parallel against perpendicular time constants\n    test: paired t test\n    p: 0.001\n    p_relation: \"<\"\n    n: 3 parallel and 6 perpendicular experiments\n  - about: elongated parallel against random cells\n    test: unpaired t test\n    p: 0.01\n    p_relation: \"<\"\n    n: 3 parallel and 10 random experiments\n  - about: discharging against charging time constants\n    test: paired t test\n    p: 0.001\n    p_relation: \"<\"\n  data: elsewhere\n  where: DANDI:001273 (0.250805.1356), assigned from its title\n  depends_on:\n  - fig4-pooled-time-constants\n  expected:\n  - quantity: ratio of parallel to perpendicular time constants, elongated cells\n    value: 2\n    tolerance: 0.2\n  criterion: Fits of fig4-pooled-time-constants; groups as in the Figure 4D and 4E legend (parallel\n    n = 3, perpendicular n = 6, random n = 10, field orientations pooled for random cells). The Figure\n    4 legend gives other bounds for two of these tests (p < 0.01, paired two-tailed, charging\n    against discharging; p < 0.01, unpaired two-tailed, between orthogonal orientations), and a\n    paired test needs the same cells in both orientations though the groups differ in size; readings\n    (a) the Results' tests, (b) the legend's. Reproduced when, under every reading, parallel time\n    constants are about twice the perpendicular ones (within tolerance) and larger than random at\n    p < 0.05, the pole differences in dFmax and time constants are not significant by paired\n    two-sided t tests (F6, the absence judged on that test), and discharging exceeds charging at\n    p < 0.05 when elongated parallel cells are left out.\n- id: fig5-sine-asymmetry\n  statement: Sine waves polarized the two poles of a cell more asymmetrically than 2-us pulses; in the\n    Figure 5 cell the depolarized ROI was 30% smaller than the hyperpolarized one with the pulse and\n    up to 90% smaller with sine waves, and in the Figure S3 cell 20% smaller with the pulse and 40%\n    with sine waves, the oscillations not migrating to other regions.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraphs 1 to 4; Figures 5 and S3\n  quote: in this cell, the oscillations in ROI 2 were up to 90% smaller than those in ROI 1 (compared\n    to just 30% smaller when the same cell was polarized with the 2-μs pulse) ... With the 2-μs\n    pulse, polarization in ROI 1 was 20% smaller than in ROI 2 ( Figure S3B ); however, with sine\n    waves, it became 40% smaller\n  data: elsewhere\n  where: DANDI:001274 (0.250805.1401), assigned from its title\n  expected:\n  - quantity: Figure 5 cell, pulse asymmetry, depolarized ROI smaller by\n    value: 30\n    tolerance: 3\n    unit: percent\n  - quantity: Figure 5 cell, sine asymmetry, depolarized ROI smaller by, at most\n    value: 90\n    tolerance: 9\n    unit: percent\n  - quantity: Figure S3 cell, pulse asymmetry\n    value: 20\n    tolerance: 2\n    unit: percent\n  - quantity: Figure S3 cell, sine asymmetry\n    value: 40\n    tolerance: 4\n    unit: percent\n  criterion: F7, O5, O6; ROIs 1 and 2 as in the dataset (cells C7 and C8 of Figure 6B). Pulse\n    asymmetry from dF averaged 1 to 2 us into the pulse; sine asymmetry from the oscillation\n    amplitudes after LOESS subtraction. \"Up to 90%\" is the largest per-cycle difference; the 40% is\n    not said to be a maximum, so readings (a) the regression sensitivities of Figure 6C, (b) the\n    largest per-cycle difference; the 100- and 154-Hz waves are both run. Reproduced when the four\n    values are within tolerance under every reading, and the sine asymmetry exceeds the pulse\n    asymmetry in both cells.\n- id: fig6-sine-less-than-pulse\n  statement: Across 9 cells FluoVolt sensitivity to 2-us pulses was 15% to 47% per 1 kV/cm (mean 28%);\n    sensitivity to 2-kHz sine waves, linearly correlated with the field, was 1.5% to 28.4% (mean\n    11.8%), smaller in every ROI, and 42% of the pulse value.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraphs 5 and 6; Figures 6B to 6D\n  quote: The electric field sensitivity of FluoVolt ranged between a 15% and 47% change per 1 kV/cm,\n    with an average value of 28% ± 2.5% across all ROIs in all the cells ... The regression\n    coefficient, which was the FluoVolt sensitivity to sine waves, varied from 1.5% to 28.4% (\n    Figure 6C ). All numbers were invariably smaller than those measured for the same ROIs with the\n    pulse ( Figure 6D ). The electric field sensitivity averaged across all ROIs in all the cells was\n    11.8% ± 1.7% per 1 kV/cm, just 42% of the value for the 2-μs pulses\n  statistics:\n  - about: linear correlation of the sine wave oscillation with the field, each ROI\n    test: linear regression\n    p: 0.0001\n    p_relation: \"<\"\n    n: both ROIs in eight cells\n  data: elsewhere\n  where: DANDI:001274 (0.250805.1401), assigned from its title\n  expected:\n  - quantity: mean pulse sensitivity over the 18 ROIs\n    value: 28\n    tolerance: 2.5\n    unit: percent per kV/cm\n  - quantity: range of pulse sensitivity\n    value: 15\n    tolerance: 1.5\n    unit: percent per kV/cm, lower bound (upper bound 47, tolerance 4.7)\n  - quantity: mean sine sensitivity over the 18 ROIs\n    value: 11.8\n    tolerance: 1.7\n    unit: percent per kV/cm\n  - quantity: range of sine sensitivity\n    value: 1.5\n    tolerance: 0.15\n    unit: percent per kV/cm, lower bound (upper bound 28.4, tolerance 2.84)\n  - quantity: mean sine over mean pulse sensitivity\n    value: 42\n    tolerance: 4.2\n    unit: percent\n  criterion: F7, O5, O6, on the 2-kHz waves modulated at 100 Hz (Figure 6C legend). Pulse sensitivity\n    per ROI is dF averaged over the 21 frames from 1 to 2 us, divided by the field in kV/cm, with\n    sign removed; sine sensitivity per ROI the slope of the oscillation dF on the instantaneous\n    field. Whether the slope is fitted on signed values or on per-cycle amplitudes is not given;\n    readings (a) signed dF on the signed field, sign removed after, (b) per-cycle peak-to-peak\n    amplitude on the cycle's peak field. Reproduced when, under every reading, the means and the\n    ratio are within tolerance, the ranges within the widened bounds, the sine value is below the\n    pulse value in every ROI, and the regression p is below 0.0001 for both ROIs in at least eight\n    cells.\n- id: threshold-depolarization-estimate\n  statement: The 2-kHz AP threshold of 57.7 V/cm times the sine wave sensitivity gives a 0.68%\n    emission change, about 6.8 mV with FluoVolt's calibration, so the threshold depolarization is 5\n    to 15 mV, as with intracellular current injection.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    last paragraph\n  quote: This threshold corresponds to a 0.68% ± 0.11% FluoVolt emission change (11.8 × 57.7/1,000)\n    ... Then, a 0.68% emission change corresponds to a 6.8-mV depolarization at the AP threshold.\n    Considering the calibration factor variability, the threshold TMP depolarization can be\n    conservatively estimated in the range from 5 to 15 mV\n  data: elsewhere\n  where: DANDI:001032 to 001035 (0.240527.1431 or 0.240527.1432) for the threshold and DANDI:001274\n    (0.250805.1401) for the sensitivity, assigned from their titles\n  depends_on:\n  - fig2d-modulated-thresholds-higher\n  - fig6-sine-less-than-pulse\n  expected:\n  - quantity: emission change at the 2-kHz AP threshold\n    value: 0.68\n    tolerance: 0.11\n    unit: percent\n  - quantity: depolarization at the 2-kHz AP threshold\n    value: 6.8\n    tolerance: 1.1\n    unit: mV\n  criterion: The mean sine sensitivity of fig6-sine-less-than-pulse times the mean unmodulated 2-kHz\n    1-AP threshold of fig2d-modulated-thresholds-higher, divided by 1,000, and that times 10 mV per\n    1% (the calibration of reference 47, about 10% per 100 mV, as the paper uses it). Tolerances are\n    the paper's, the second being 0.11% times 10 mV per 1%. Reproduced when both are within\n    tolerance and the depolarization lies within 4.5 to 16.5 mV (5 to 15 mV widened by 10%).\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/001048/10.1016-j.xcrp.2025.102660.yaml paper/10.1016-j.xcrp.2025.102660.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  f=claims/001048/10.1016-j.xcrp.2025.102660.yaml; grep -n "—\|rather" $f; grep -v "^ *#" $f | grep -n "[^ ]: .*: " ; git status --short
```

```
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
?? claims/001048/
?? scripts
```

**Agent**

I wrote the claims file at `claims/001048/10.1016-j.xcrp.2025.102660.yaml`. The quote checker passes it: 19 claims, 19 quotes, 8 statistical values, 0 problems. But this dandiset does not hold this paper's data, so none of the claims can be tested on it.

**The dataset mismatch.** DANDI:001048 (version 0.250701.1624) is titled "Plasma membrane conductance changes in response to supraphysiological hyperpolarization". Its description covers membrane lesions in HEK cells, species human. The paper studies rat hippocampal neurons stimulated by sine waves and has no HEK cell or hyperpolarization experiment. Its Data and code availability section lists ten dandisets (001030–001035 and 001271–001274), and 001048 is not one of them. The two share authors and NIH grants, which may be why the dandiset names the paper. So every claim is marked `data: elsewhere`. Each one points to a dandiset and published version that I matched from DANDI titles only, because the paper doesn't say which figure is in which dandiset.

**Text read.** The NIH author manuscript (NIHMS2098259, PMC12320893) from Europe PMC: main text, figure legends and STAR Methods, plus the supplement (Figures S1–S4 and Table S1). I did not read the version of record, and there is no main-text PDF. The paper says it reports no original code, so no code was read.

**Claims.**
- **What they cover:** the AP selection, firing and the excitation block under unmodulated waves, the 20 kHz versus 2 kHz thresholds, the modulated versus unmodulated thresholds and firing patterns, low conductivity, heating, the 2-s ramp, Di-8-ANEPPS, TTX, the charging time constants, the sine-wave asymmetry, the sine versus pulse sensitivity, and the threshold depolarization estimate.
- **Statistics:** 4 claims carry 8 tests. These are two-tailed unpaired t tests (p < 0.0001, 0.0079, 0.0142, 0.0037), paired and unpaired t tests for Figure 4, and the regression p < 0.0001 (printed in the paper as "<0.01%").
- **Expected values and criteria:** 13 claims have expected values with tolerances, and all 19 have criteria.

**Details the paper leaves open, with the readings named:**
- **Soma region:** (a) Otsu threshold component nearest the centre, (b) that region eroded by 2 pixels.
- **Baseline interval:** (a) all frames before onset, (b) the last 20 ms.
- **AP detection:** (a) peaks above 5% dF, (b) above 5 SD of the baseline.
- **"Sustained depolarization":** (a) mean dF above 5 SD of baseline, (b) above half the median AP height.
- **Debris-ROI scaling:** (a) scaled, (b) unscaled.
- **LOESS span:** (a) 2 ms, (b) 4 ms.
- **AP measures:** (a) every AP or (b) the first per session; duration as (a) half-height width or (b) time back to the baseline.
- **Firing-rate ceiling:** (a) for the median neuron, (b) for at least 75% of neurons.
- **The single p for "all thresholds":** (a) one test per stimulus, (b) one pooled test.
- **Whether 57.7 V/cm is the 1-AP threshold:** read as the 1-AP threshold, with the 5-AP mean reported beside it.
- **Extrapolation to 2 mS/cm:** (a) proportional, (b) linear, (c) exponential.
- **Heating formula:** (a) peak or (b) RMS field, with water's heat capacity.
- **Discharging fit:** (a) free amplitude, (b) amplitude fixed at the end of the pulse.
- **Figure 4 tests:** (a) as in the Results or (b) as in the legend; the two give different p bounds.
- **Asymmetry measure:** (a) regression-based, (b) largest per-cycle difference.
- **Sine sensitivity regression:** (a) signed values, (b) per-cycle amplitudes.
- **Figure 2D:** the legend's unpaired test is followed, with a paired test as a variant, since the thresholds come from the same neurons.

**Missing from the paper.**
- No figure-to-dandiset map.
- No neuron counts for the TTX experiment, the block and Figure 2.
- No heat capacity or field definition for the temperatures: the paper's own numbers give neither 2.5 °C (peak about 3.9 °C, RMS about 1.95 °C), so that claim may end up blocked as `methods_underspecified`.
- No measure of the extrapolation to 2 mS/cm.

Nothing was committed.

## End of run

27 turns, 4 minutes, result: success.
