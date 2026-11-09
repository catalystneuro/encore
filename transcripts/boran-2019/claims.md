# 000574 · claims · run 39940274860

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md | head -c 100000; ls claims/001453/ claims/000574/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md
```

```
## Reader

### 1. Get the paper

The workflow puts the paper's full text, and its PDF where there is one, under
`paper/`: the main text, the Methods, and the supplement. Read the text; open
the PDF only to read a figure or a table the text garbles. If the full text is
not there, or lacks the Methods or a supplement the results rest on, stop:
write no claims, and end with a report that names what is missing, so that it
can be supplied. Never write claims from the abstract. Do not copy figures.
Do not look at the dataset's data: its title and description on the archive
are enough to know which paper and which experiments it is meant to hold.

### 2. Read the paper's code

Read the code the paper links to before writing criteria. Say what it holds,
and record the repository and commit read. Where the Methods leave a choice
open and the code settles it, follow the code and say so. Where they disagree,
follow the Methods for the main result and name the code's choice as a
variant. When more sources disagree (the Methods, the analysis code, the
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/001453/ paper/ claims/000574 2>&1; cat claims/001453/*.yaml | head -250; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '250,400p' claims/001453/*.yaml | grep -n -A40 "^checks\|kind: \|data: elsewhere" | head -80; cat paper/10.1126-sciadv.aav3687.txt | head -c 52000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; fold -s -w 200 10.1126-sciadv.aav3687.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; fold -s -w 200 10.1038-s41597-020-0364-3.txt > $TMPDIR/d.txt; head -c 1500 10.1038-s41597-020-0364-3.txt
```

```
1517 /tmp/claude-1001/p.txt
DOI: 10.1038/s41597-020-0364-3
Version: as served by europe_pmc
Source: europe_pmc+crossref (paper-text-fetcher)
Stored: 2026-10-20
Extracted: as fetched
------------------------------------------------------------------------
2628 sdata Scientific Data Sci Data Nature Publishing Group PMC6972902 6972902 6972902 31964868 10.1038/s41597-020-0364-3 Dataset of human medial temporal lobe neurons, scalp and intracranial EEG during a verbal working memory task Boran Ece 1 Fedele Tommaso 1 2 3 Steiner Adrian 1 Hilfiker Peter 4 Stieglitz Lennart 1 Grunwald Thomas 4 5 Sarnthein Johannes 1 2 ✉ 1 Klinik für Neurochirurgie, UniversitätsSpital und Universität Zürich, 8091 Zürich, Switzerland 2 Neuroscience Center Zurich, ETH Zürich, Zürich, Switzerland 3 Institute for Cognitive Neuroscience, National Research University Higher School of Economics, Moscow, Russian Federation 4 Schweizerisches Epilepsie-Zentrum, 8008 Zürich, Switzerland 5 Klinik für Neurologie, UniversitätsSpital Zürich, 8091 Zürich, Switzerland ✉ Corresponding author. 21 1 2020 7 30 30 28 1 2020 © The Author(s) 2020 Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and indicate if changes were made. The images or other third party mater
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 500
}
```

```
File content (27892 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 500,
 "limit": 1020
}
```

```
500	10.1016/j.neuroimage.2008.08.028
501	18817882
502	journal=Neuroimage&title=Test–retest reliability of EEG spectra during a working memory task&author=M. Näpflin&author=M. Wildi&author=J. 
503	Sarnthein&volume=43&publication_year=2008&pages=687-693&pmid=18817882&doi=10.1016/j.neuroimage.2008.08.028&
504	10.1073/pnas.95.12.7092
505	PMC22750
506	9618544
507	journal=Proc. Natl. Acad. Sci. U.S.A.&title=Synchronization between prefrontal and posterior association cortex during human working memory&author=J. Sarnthein&author=H. Petsche&author=P. 
508	Rappelsberger&author=G. L. Shaw&author=A. von Stein&volume=95&publication_year=1998&pages=7092-7096&pmid=9618544&doi=10.1073/pnas.95.12.7092&
509	10.3758/cabn.3.4.255
510	15040547
511	journal=Cogn. Affect. Behav. Neurosci.&title=Neuroimaging studies of working memory: A meta-analysis&author=T. D. Wager&author=E. E. 
512	Smith&volume=3&publication_year=2003&pages=255-274&pmid=15040547&doi=10.3758/cabn.3.4.255&
513	10.1073/pnas.0732061100
514	PMC164690
515	12792019
516	journal=Proc. Natl. Acad. Sci. U.S.A.&title=Reset of human neocortical oscillations during a working memory task&author=D. S. Rizzuto&author=J. R. Madsen&author=E. B. Bromfield&author=A. 
517	Schulze-Bonhage&author=D. Seelig&volume=100&publication_year=2003&pages=7931-7936&pmid=12792019&doi=10.1073/pnas.0732061100&
518	10.1523/JNEUROSCI.0567-09.2010
519	PMC2835496
[... 999 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 170
}
```

```
1	DOI: 10.1126/sciadv.aav3687
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 1 supplement file(s) from the PMC Open Access cloud data (PMC6436923), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	2850 sciadv Science Advances Sci Adv American Association for the Advancement of Science PMC6436923 6436923 6436923 30944858 10.1126/sciadv.aav3687 Persistent hippocampal neural firing and 
8	hippocampal-cortical coupling predict verbal working memory load Boran Ece 1 Fedele Tommaso 1 2 3 Klaver Peter 2 4 5 Hilfiker Peter 6 Stieglitz Lennart 1 Grunwald Thomas 6 7 Sarnthein Johannes 1 2 * 
9	1 Klinik für Neurochirurgie, UniversitätsSpital und Universität Zürich, 8091 Zürich, Switzerland. 2 Zentrum für Neurowissenschaften Zürich, ETH Zürich, Zürich, Switzerland. 3 Institute for Cognitive 
10	Neuroscience, National Research University Higher School of Economics, Russian Federation. 4 School of Psychology, University of Surrey, Surrey GU2 7XH, UK. 5 University of Applied Sciences in 
11	Special Needs Education, 8050 Zürich, Switzerland. 6 Schweizerisches Epilepsie-Zentrum, 8008 Zürich, Switzerland. 7 Klinik für Neurologie, UniversitätsSpital Zürich, 8091 Zürich, Switzerland. * 
12	Corresponding author. Email: [removed: an e-mail address] 27 3 2019 5 3 eaav3687 eaav3687 3 4 2019 Copyright © 2019 The Authors, some rights reserved; exclusive licensee American Association for the 
13	Advancement of Science. No claim to original U.S. Government Works. Distributed under a Creative Commons Attribution NonCommercial License 4.0 (CC BY-NC). This is an open-access article distributed 
14	under the terms of the Creative Commons Attribution-NonCommercial license , which permits use, distribution, and reproduction in any medium, so long as the resultant use is not for commercial 
15	advantage and provid
[... 155 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 170,
 "limit": 150
}
```

```
170	plotted the maximal PLV in the individual frequency band for all hippocampal contacts ( Fig. 6I ). There was no evidence that the PLV differed between the left and right hippocampus. For the subject 
171	group, there was a gradual increase in the PLV from the anterior end to the posterior end of the hippocampal axis during maintenance ( R 2 = 0.118, P = 0.0467) and the PLV to posterior sites ( y < 
172	−20 mm) was higher than to anterior sites (permutation t test, t = 2.09, P = 0.0405). This posterior preference might be associated with the functional organization proposed for the hippocampal 
173	longitudinal axis ( 26 ). Recordings in the epileptogenic zone In our analysis, we also included electrodes in brain regions that were ultimately resected. Among biomarkers that are thought to 
174	indicate the epileptogenic zone, we analyzed high-frequency oscillations (HFOs) in all patients ( 27 ). The rates of clinically relevant HFOs were not affected by the performance of the task. This 
175	points to a clear dissociation between the ripples observed during cognitive tasks in rodents and the clinically relevant HFOs that are used to predict seizure outcome in the individual patient ( 27 
176	). When comparing hippocampal channels within and outside the seizure onset zone (SOZ) (table S1), the increase in the PLV was not significantly different between the non-SOZ electrodes and SOZ 
177	electrodes. Although epilepsy may have reduced functional connectivity to SOZ channels ( 28 ), we observed task-dependent connectivity, suggesting residual function in the epileptogenic hippocampus. 
178	Spike-field coherence Last, we tested whether the action potentials of maintenance neurons were temporally aligned with the LFP. For this analysis, we included all maintenance neurons that had at 
179	least 100 spikes during both maintenance and encoding. We found significant spike-field coherence to the LFP but not to the iEEG or the scalp EEG. For all frequency bins, the percenta
[... 140 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/d.txt"
}
```

```
1	DOI: 10.1038/s41597-020-0364-3
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched
6	------------------------------------------------------------------------
7	2628 sdata Scientific Data Sci Data Nature Publishing Group PMC6972902 6972902 6972902 31964868 10.1038/s41597-020-0364-3 Dataset of human medial temporal lobe neurons, scalp and intracranial EEG 
8	during a verbal working memory task Boran Ece 1 Fedele Tommaso 1 2 3 Steiner Adrian 1 Hilfiker Peter 4 Stieglitz Lennart 1 Grunwald Thomas 4 5 Sarnthein Johannes 1 2 ✉ 1 Klinik für Neurochirurgie, 
9	UniversitätsSpital und Universität Zürich, 8091 Zürich, Switzerland 2 Neuroscience Center Zurich, ETH Zürich, Zürich, Switzerland 3 Institute for Cognitive Neuroscience, National Research University 
10	Higher School of Economics, Moscow, Russian Federation 4 Schweizerisches Epilepsie-Zentrum, 8008 Zürich, Switzerland 5 Klinik für Neurologie, UniversitätsSpital Zürich, 8091 Zürich, Switzerland ✉ 
11	Corresponding author. 21 1 2020 7 30 30 28 1 2020 © The Author(s) 2020 Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, which permits use, sharing, 
12	adaptation, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons license, and 
13	indicate if changes were made. The images or other third party material in this article are included in the article’s Creative Commons license, unless indicated otherwise in a credit line to the 
14	material. If material is not included in the article’s Creative Commons license and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain 
15	permission directly from the copyright holder. To view a copy of this license, visit http://creativecommons.org/licenses/by/4.0/ . The Creative Commo
[... 333 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-sciadv.aav3687.supp.pdf",
 "pages": "9"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import fitz;d=fitz.open('paper/10.1126-sciadv.aav3687.supp.pdf');p=d[8]
for b in p.get_text('words'): pass
import collections
rows=collections.defaultdict(list)
for w in p.get_text('words'): rows[round(w[1]/4)].append((w[0],w[4]))
for k in sorted(rows): print(' | '.join(t for x,t in sorted(rows[k])))
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "import pdfplumber" 2>&1; python -c "import pypdf;print(pypdf.__version__)" 2>&1; which pdftotext mutool
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfplumber
ModuleNotFoundError: No module named 'pdfplumber'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf;print(pypdf.__version__)
    ^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pypdf'
```

**Agent calls Bash**

```bash
cd  ls tools docs; sed -n 1,80p tools/claims_check.py; grep -rn "kind" docs/*.md | grep -i claim | head -20
```

```
docs:
agents
archives.md
conversion-tracker.md
design.md
encore.md
fixing-conversions.md
pilot-notes
pilot-notes.md
pipeline.md
protocol.md
queue.md

tools:
__pycache__
agent_run.py
archive_transcripts.sh
build_site.py
build_targets.py
claims_check.py
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; ls claims | head; ls claims | wc -l
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
[... 196 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:5000])"; awk '/kind: link/,0' docs/protocol.md | head -0; grep -n "link" docs/protocol.md | head -20
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
[... 92 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 205,240p docs/protocol.md; ls claims/000623 claims/000575 2>/dev/null;
```

```
4. Decide what comes from outside the dataset. Data from elsewhere may be
   used only when the claims file says the paper relies on it, it is public,
   and it is pinned: a DOI, or a repository at a commit. Record each under
   `inputs` in the attempt. A claim whose outside input is not public is
   blocked with `data_missing`, and its notes say where you looked.

   The registry judges the dataset, so claims that use outside data are
   kept apart:
   - Each claim says what its test uses: `data: dataset` (the default),
     `data: with_labels`, `data: with_inputs` or `data: elsewhere`. The
     `with_inputs` and `elsewhere` claims are counted apart, each group on
     its own; the others count towards what is said about the dataset.
   - `with_labels` is for outside sources that only name or map codes the
     dataset already holds, such as stimulus names for its stimulus codes.
     They bring in no measurements. A link claim must confirm the names, and
     the missing names are recorded as a finding (`metadata_insufficient`).
   - When outside data has to be matched to the dataset's cells, sessions
     or subjects, a claim of its own (`kind: link`) tests the link. Link
     claims are the registry's checks, not findings of the paper, so the
     author adds them to the claims file; they are the only claims the
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
head -60 claims/000575/*.yaml; grep -n "criterion" -A12 claims/000575/*.yaml | sed -n 1,60p
```

```
# Claims for Boran, Hilfiker, Stieglitz, Sarnthein & Klaver (2022), NeuroImage 254, 119123, on
# dandiset 000575.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
# protocol pilot-10 as stated in docs/protocol.md.
#
# Text read: the version of record (paper/10.1016-j.neuroimage.2022.119123.txt, extracted from the
# publisher PDF), with its Methods, Results, figure legends and Table 1. The paper has no
# supplement and cites none. Figures 2c, 2d, 3b and 4d were read from the PDF for the per-region
# counts and accuracies that the text does not print.
#
# Code read: the paper's Data and code availability names one repository,
# https://gin.g-node.org/USZ_NCH/Human_MTL_units_visual_WM. GIN did not answer from this run;
# its listing was read from the Internet Archive snapshot of 2026-10-15 (head commit
# 5ccc2377802efec9522e3c3baa0e600419ee4383, data files at commit 798bf013ee). It holds the 16
# session files (Data_Subject_XX_Session_YY.h5, NIX format), a README and a LICENSE. The README
# describes a code_MATLAB folder with a data-loading example script only, and that folder is not
# on master. No analysis code is published, so no method detail below is settled by code. The
# dandiset is a variant form of this GIN repository (its related resources say so).
# The Methods say the recording scheme and non-task-specific analyses are "identical to Boran
# et al. (2019)" and that dPCA methods were adapted from Kaminski et al. (2017). Neither paper is
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
curl -sS -m 20 -o /dev/null -w "%{http_code}\n" https://gin.g-node.org/USZ_NCH/Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM 2>&1; curl -sS -m 20 -o /dev/null -w "%{http_code}\n" "https://doi.org/10.12751/g-node.d76994" 2>&1; curl -sS -m 20 "https://api.dandiarchive.org/api/dandisets/000574/" 2>&1 | head -c 600
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sS -m 20 "https://api.dandiarchive.org/api/dandisets/000574/versions/0.250815.1108/info/" | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('description'));print(d.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sS -m 30 "https://gin.g-node.org/api/v1/repos/USZ_NCH/Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM/contents/" | python -c "import json,sys;[print(x['type'],x['name'],x.get('size')) for x in json.load(sys.stdin)]"; curl -sS -m 30 "https://gin.g-node.org/api/v1/repos/USZ_NCH/Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM/branches" | python -c "import json,sys;[print(b['name'],b['commit']['id']) for b in json.load(sys.stdin)]"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sS -m 30 "https://gin.g-node.org/USZ_NCH/Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM" -o gin.html; python - <<'E'
import re
s=open('gin.html',encoding='utf8',errors='replace').read()
print(sorted(set(re.findall(r'/USZ_NCH/Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM/(?:src|commit)/[^"\s]+',s)))[:60])
E
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://gin.g-node.org/USZ_NCH/Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM; curl -sS -m 30 $B/src/master/code_MATLAB | grep -o 'src/master/code_MATLAB/[^"]*' | sort -u; grep -o 'commit/[0-9a-f]\{40\}' gin.html | head -3; curl -sS -m 30 $B/raw/master/README.md | head -80
```

````
src/master/code_MATLAB/Load_Data_Example_Script.m
commit/0b27b34ecd0da217e4403bdd080b4a0d78f155fd
commit/d8cd7b51391cfb85fa6b58876ddad392ce83e20f
commit/2d5f67bf76b9d6eaf7d0fdf78bfd85cfbb0da917
# Dataset of human medial temporal lobe neurons, scalp and intracranial EEG during a verbal working memory task

## Summary
We present an electrophysiological dataset recorded from nine subjects during a verbal working memory task. Subjects were epilepsy patients undergoing intracranial monitoring for localization of epileptic seizures. Subjects performed a modified Sternberg task in which the encoding of memory items, maintenance, and recall were temporally separated. The dataset includes simultaneously recorded scalp EEG with the 10-20 system, intracranial EEG (iEEG) recorded with depth electrodes, waveforms and spike times of 1526 units recorded in the medial temporal lobe, and the MNI coordinates and anatomical labels of all intracranial electrodes. Subject characteristics and information on sessions (set size, match/mismatch, correct/incorrect, response, response time for each trial) are also provided. This dataset enables the investigation of working memory by providing simultaneous scalp EEG and iEEG recordings, which can be used for connectivity analysis, alongside hard to obtain unit recordings from humans.  

## Downloading the data

### Using gin

Create an account on gin and download the *gin* client as described [here](https://web.gin.g-node.org/G-Node/Info/wiki/gin-cli). On your computer, log in using
```bash
gin login
```

Clone the repository using:
```bash
[... 64 more lines not kept]
````

**Agent calls Bash**

```bash
cd $TMPDIR; B=https://gin.g-node.org/USZ_NCH/Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM; curl -sS -m 30 $B/raw/master/code_MATLAB/Load_Data_Example_Script.m; echo ====; curl -sS -m 30 "$B/commits/master" | grep -o 'commit/[0-9a-f]\{40\}' | head -2; curl -sS -m 30 "$B/commits/master" | grep -o 'datetime="[^"]*"\|data-content="[^"]*"' | head -4
```

```
%% Add nix to path
% Path for the folder 'nix-mx_Win64_1.4.1'
addpath('nix-mx_Win64_1.4.1\')

%% Open NIX file
% Path of the selected file
file_path = 'Data_Subject_01_Session_01.h5';
f = nix.File(file_path,nix.FileMode.ReadOnly);

%% Read metadata
% Display names of all sections
cellfun(@(x) disp(x.name),f.sections)

%% General information
sectionGeneral = f.openSection('General');
% Properties
cellfun(@(x) disp(x.name),sectionGeneral.properties)
% Institution
fprintf(['Institution: ',sectionGeneral.openProperty('Institution').values{1}.value,'\n'])
% Recording location
[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "summary\|^checks\|questions" docs/protocol.md | head; python tools/claims_check.py --help 2>&1 | head -5; sed -n 80,200p tools/claims_check.py | grep -n "p_relation\|warn\|numbers" | head
```

```
28:`author`, `author-answers` when questions were answered, `verifier-1`,
163:### 6. Answer questions
167:file, and marks it answered in `questions/<folder>.yaml`. An answer
226:     records are matched (an identifier, or, where there is none, summary
278:   you find it in the paper. Add a question to `questions/<folder>.yaml`
410:`README.md` and the notebook's summary carry this sentence: "A failure to
418:- the executed notebook with the conclusion cells and the summary removed;
509:2. Check every sentence of the conclusions and the summary against the
515:report or a summary table.
Check a claims file against the full text of its paper.

    python tools/claims_check.py claims/<dandiset>/<doi>.yaml paper/<text>.txt [more texts ...]

Validates the file against schemas/claims.schema.json, checks every quote word for word
```

**Agent calls Write**

```json
{
 "file_path": "claims/000574/10.1126-sciadv.aav3687.yaml",
 "content": "# Claims for Boran, Fedele, Klaver, Hilfiker, Stieglitz, Grunwald & Sarnthein (2019), Science\n# Advances 5, eaav3687, on dandiset 000574.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record as served by Europe PMC (PMC6436923), in\n# paper/10.1126-sciadv.aav3687.txt, with its Results, figure legends and Methods, and the\n# supplement aav3687_SM.pdf (figs. S1 to S6, table S1 and table S2, the statistics checklist)\n# extracted into the same file. Table S1 is garbled by the extraction; it was read by its column\n# order (subject, diagnosis, age, hemisphere of the hippocampal electrode with maximal PLV,\n# tissue SOZ or non-SOZ, scalp electrode with maximal PLV, PLV peak frequency, individual PLV\n# band, maximal PLV, PLV workload dependent and its band, PLV maintenance against encoding,\n# EEG workload dependent, iEEG workload dependent, then the median band limits), and the\n# medians it prints (6.0 to 11.5 Hz, 7.8 to 10.0 Hz) were recomputed from the rows to confirm\n# the reading. The supplement PDF page could not be rendered in this run. Movie S1 was not read.\n# The data descriptor for the deposit (Boran et al. 2020, Sci Data 7, 30,\n# doi:10.1038/s41597-020-0364-3, paper/10.1038-s41597-020-0364-3.txt) was read for the\n# description of the deposited data; it repeats the behavior and spike sorting numbers.\n#\n# Code read: the paper links no analysis code (\"Additional data related to this paper may be\n# requested from the authors\"). It links the task (Presentation,\n# www.neurobs.com/ex_files/expt_view?id=266, not read; stimulus software) and Combinato\n# (spike sorting, run before the data were deposited). The data descriptor names the G-Node\n# deposit doi:10.12751/g-node.d76994\n# (gin.g-node.org/USZ_NCH/Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM, master at commit\n# 0b27b34ecd0da217e4403bdd080b4a0d78f155fd, read 2026-10-23). Its code_MATLAB folder holds one\n# script, Load_Data_Example_Script.m, which only reads and plots the NIX files (metadata, iEEG,\n# scalp EEG, trial events, spike times, waveforms, electrode MNI coordinates). No analysis\n# method below is settled by code. The dandiset's related resources name the GIN deposit as\n# a variant form of it and the conversion code (github.com/janhohenheim/usz-neuro-conversion),\n# which was not read.\n#\n# Data the paper used: nine epilepsy patients (table S1; ages 24, 39, 18, 28, 20, 31, 47, 56\n# and 19 for subjects 1 to 9, which match Table 1 of the data descriptor, so subject numbers\n# are the same in both papers) with depth electrodes in hippocampus, entorhinal cortex and\n# amygdala, each with nine microwires at its tip; 36 sessions in total (up to seven per\n# subject), 50 trials per session. Task: modified Sternberg task. Fixation [-6, -5] s;\n# encoding [-5, -3] s, a string of eight consonants of which the middle 4, 6 or 8 are the\n# memory items (set size; the outer positions are X); maintenance [-3, 0] s; probe letter at\n# 0 s, answered IN or OUT by button press, then acoustic feedback. Times are relative to probe\n# onset throughout the paper. An error trial is always followed by a set size 4 trial.\n# Measured variables: per trial set size, match (IN) or mismatch (OUT), correct or incorrect,\n# response and response time; spike times and mean waveforms of 1526 sorted units (putative\n# neurons) in hippocampus (676), entorhinal cortex (449) and amygdala (401), units seen in more\n# than one session counted once per session; iEEG from the macroelectrodes (recorded at 4 kHz\n# against a common intracranial reference, analysed as one bipolar signal per macroelectrode\n# from its deepest contacts; deposited at 2 kHz per the data descriptor); scalp EEG on the\n# 10-20 system (recorded at 256 Hz, re-referenced to averaged mastoids; deposited at 200 Hz);\n# local field potentials of the microwires (used for spike-field coherence; the data\n# descriptor does not list them among the deposited data); electrode MNI coordinates,\n# anatomical labels and seizure onset zone (SOZ) electrodes. Trials with eye movements or\n# artifacts were removed by visual inspection (the data descriptor lists trial rejection\n# information per trial).\n#\n# Definitions used throughout, from the Methods unless a claim says otherwise:\n# - Unless a claim says otherwise, the neuron analyses use correct trials only (Results,\n#   Single-unit electrophysiology, paragraph 2).\n# - \"Permutation t test\" is the EEGLAB test that mixes values of the two distributions 2000\n#   times and takes P from the resulting t values (Methods, Statistics). Firing rates and power\n#   spectra are compared with cluster-based nonparametric permutation tests as in FieldTrip.\n#   A \"permutation test against scrambled data\" builds a null from n > 200 label-scrambled\n#   repetitions, with minimum P = 1/(n + 1).\n# - High workload is set sizes 6 and 8 pooled and low workload set size 4 for the neuron\n#   analyses (Fig. 2 and Fig. 4E); the EEG, iEEG and PLV analyses compare set size 8 with set\n#   size 4 (Fig. 5 and Fig. 6).\n#\n# Details the paper leaves open and that apply to several claims:\n# - Paired or unpaired permutation t test for comparisons of periods within the same trials.\n#   Readings (a) paired over trials, (b) unpaired. A difference counts in the named direction\n#   when two-sided P < 0.05 and the mean is higher in the named period.\n# - The number of label-scrambled repetitions behind \"permutation test against scrambled\n#   data\". The printed P = 0.002 is the minimum for 499 repetitions (Methods, Statistics),\n#   while table S2 gives 1000 resampling runs for Fig. 2B, 2C and 3E. Both are run; this can\n#   only move a P near 0.05.\n# - Correct trials only, or all artifact-free trials, for the EEG, iEEG and PLV analyses. The\n#   rule \"unless stated otherwise ... only trials with correct responses\" is stated in the\n#   neuron section. Readings (a) correct trials only, (b) all artifact-free trials.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000574\"\npaper: doi:10.1126/sciadv.aav3687\nclaims:\n- id: behavior-accuracy-set-size\n  statement: >-\n    Correct response rates were 90.2 +/- 7.8% for IN and 93.1 +/- 4.3% for OUT trials, and the\n    rate of correct responses decreased with set size, from 98.5% (set size 4) to 90.5% (6) and\n    84.7% (8), a significant effect in a permuted repeated-measures ANOVA over 36 sessions.\n  source: Results, Task and behavior, paragraph 2; Figure 1B\n  quote: >-\n    The average correct response rates were 90.2 ± 7.8% for IN and 93.1 ± 4.3% for OUT. The rate\n    of correct responses decreased with set size from a set size of 4 (98.5% correct responses)\n    to set sizes of 6 (90.5%) and 8 (84.7%)\n  statistics:\n  - test: permuted repeated-measures ANOVA\n    statistic: F(2, 70) = 40.25\n    p: 0.0002\n    n: 36 sessions from nine subjects\n  expected:\n  - quantity: correct rate, IN trials\n    value: 90.2\n    tolerance: 7.8\n    unit: '%'\n  - quantity: correct rate, OUT trials\n    value: 93.1\n    tolerance: 4.3\n    unit: '%'\n  - quantity: correct rate, set size 4\n    value: 98.5\n    tolerance: 9.85\n    unit: '%'\n  - quantity: correct rate, set size 6\n    value: 90.5\n    tolerance: 9.05\n    unit: '%'\n  - quantity: correct rate, set size 8\n    value: 84.7\n    tolerance: 8.47\n    unit: '%'\n  - quantity: ANOVA F value\n    value: 40.25\n    tolerance: 4.03\n  criterion: >-\n    All trials of the 36 sessions. The IN and OUT tolerances are the SD the paper gives;\n    the others are 10%. Open, how percentages are formed; readings (a) the mean of\n    per-session percentages (Fig. 1B shows sessions), (b) trials pooled over sessions. The\n    ANOVA has set size as the within factor and session as the unit (F with 2 and 70 degrees\n    of freedom); its permutation scheme is not given, and the reading is set-size labels\n    shuffled within each session, 4999 permutations (P = 0.0002 as 1/(n + 1), Methods,\n    Statistics). Reproduced when, under one reading, all values are within tolerance, the\n    order 4 above 6 above 8 holds and the ANOVA has P < 0.05.\n- id: behavior-capacity\n  statement: >-\n    Across all sessions the working memory capacity (Cowan's K) averaged 6.8 letters.\n  source: Results, Task and behavior, paragraph 2\n  quote: >-\n    Across all sessions, the capacity averaged 6.8 [Cowan's K , (correct IN rate + correct OUT\n    rate − 1) × set size]\n  expected:\n    quantity: mean Cowan's K over sessions\n    value: 6.8\n    tolerance: 0.68\n  criterion: >-\n    K = (correct IN rate + correct OUT rate - 1) x set size, per session, as the Results define\n    it, averaged over the 36 sessions. Open, which set size and rates enter; readings (a) K at\n    set size 8 from the set size 8 rates, (b) the maximum of K over the three set sizes,\n    (c) the rates pooled over all set sizes multiplied by 8, the largest set size, (d) the mean\n    of K over the three set sizes. Reproduced when one reading is within tolerance.\n- id: behavior-rt-workload\n  statement: >-\n    The mean response time of correct trials (1630 trials) increased with workload, by 48 ms\n    per item, a significant effect in a permuted repeated-measures ANOVA.\n  source: Results, Task and behavior, paragraph 2; Figure 1C\n  quote: >-\n    The mean response time (RT) for the correct trials (1630 trials) increased with workload (48\n    ms per item; permuted repeated-measures ANOVA, F 2,2007 = 21.10, P = 0.0002; Fig. 1C )\n  statistics:\n  - test: permuted repeated-measures ANOVA\n    statistic: F(2, 2007) = 21.10\n    p: 0.0002\n    n: 1630 correct trials\n  expected:\n  - quantity: correct trials\n    value: 1630\n    tolerance: 163\n  - quantity: increase of RT per item\n    value: 48\n    tolerance: 4.8\n    unit: ms\n  - quantity: ANOVA F value\n    value: 21.10\n    tolerance: 2.11\n  criterion: >-\n    RT relative to probe onset (Fig. 1C legend), correct trials. The F has 2007 error degrees of\n    freedom, which fits neither sessions nor the 1630 trials; the ANOVA is run (a) on trials\n    with set size as factor (one-way, permuted set-size labels), (b) on per-session means as in\n    behavior-accuracy-set-size, and its F is reported under both. Open, how 48 ms per item is\n    obtained; readings (i) the slope of a line fit over all correct trials, (ii) the mean over\n    sessions of per-session slopes, (iii) the slope over the three set-size means, (iv) the\n    difference between set sizes 8 and 4 divided by 4. Open, per-session value for the session\n    readings, mean RT (the text) or median RT (Fig. 1C). Reproduced when RT rises with set\n    size, the ANOVA has P < 0.05 under one reading, and under one reading the slope and the\n    trial count are within tolerance. The F value is reported, not judged, since its degrees\n    of freedom cannot be matched to a stated design.\n- id: behavior-rt-correct-incorrect\n  statement: >-\n    Correct IN/OUT decisions were made faster than incorrect ones (1.36 +/- 0.64 s against\n    1.87 +/- 1.21 s).\n  source: Results, Task and behavior, paragraph 2\n  quote: >-\n    Correct IN/OUT decisions were made more rapidly than incorrect decisions (1.36 ± 0.64 s\n    versus 1.87 ± 1.21 s, respectively; permutation t test, t = 5.06, P = 5.0 × 10 −5 )\n  statistics:\n  - test: permutation t test\n    statistic: t = 5.06\n    p: 5.0e-5\n  expected:\n  - quantity: mean RT, correct trials\n    value: 1.36\n    tolerance: 0.136\n    unit: s\n  - quantity: mean RT, incorrect trials\n    value: 1.87\n    tolerance: 0.187\n    unit: s\n  criterion: >-\n    RT relative to probe onset. Readings (a) all trials pooled, mean +/- SD over trials,\n    unpaired permutation t test; (b) per-session means, paired over sessions with at least\n    one error. The permutation t test as in Methods, Statistics (2000 permutations; the\n    printed P implies more, which only moves the minimum P). Reproduced when, under one\n    reading, both means are within tolerance and correct RT is shorter with P < 0.05.\n- id: neurons-recorded\n  statement: >-\n    1526 neurons were recorded (51 +/- 35 per session), 676 in hippocampus, 449 in entorhinal\n    cortex and 401 in amygdala.\n  source: Results, Single-unit electrophysiology, paragraph 1\n  quote: >-\n    We recorded the activity of 1526 (51 ± 35 per session) neurons from the hippocampus ( n =\n    676), entorhinal cortex ( n = 449), and amygdala ( n = 401) across all microelectrodes\n  expected:\n  - quantity: neurons\n    value: 1526\n    tolerance: 0\n  - quantity: hippocampal neurons\n    value: 676\n    tolerance: 0\n  - quantity: entorhinal neurons\n    value: 449\n    tolerance: 0\n  - quantity: amygdala neurons\n    value: 401\n    tolerance: 0\n  - quantity: neurons per session, mean\n    value: 51\n    tolerance: 5.1\n  criterion: >-\n    Counts of sorted units over all sessions, a unit seen in several sessions counted once per\n    session (Results, same paragraph). The counts are exact, since they describe the deposited\n    units; a difference is reported with its size. Hippocampus is the hippocampal head and body\n    electrodes (AH and PH in the data descriptor's Table 1), entorhinal cortex EC, amygdala A.\n    Open, the sessions in the per-session mean (1526 over 36 sessions is 42); readings (a) all\n    36 sessions, (b) sessions with at least one unit.\n- id: spike-sorting-quality\n  statement: >-\n    The mean firing rate of all neurons was 2.55 +/- 3.30 Hz; the percentage of interspike\n    intervals below 3 ms was 1.58 +/- 4.18%, and the ratio of the peak of the mean waveform to\n    the SD of the noise was 3.28 +/- 1.56.\n  source: >-\n    Results, Single-unit electrophysiology, paragraph 1; Methods, Spike detection and\n    single-unit identification; fig. S1\n  quote: >-\n    The percentage of ISI below 3 ms was 1.58 ± 4.18%, and the ratio of the peak amplitude of the\n    mean waveform to the SD of the noise was 3.28 ± 1.56\n  expected:\n  - quantity: mean firing rate over neurons\n    value: 2.55\n    tolerance: 0.255\n    unit: Hz\n  - quantity: percentage of ISI below 3 ms, mean over neurons\n    value: 1.58\n    tolerance: 0.158\n    unit: '%'\n  - quantity: waveform peak SNR, mean over neurons\n    value: 3.28\n    tolerance: 0.328\n  criterion: >-\n    Over all 1526 units. Open, the time base of the firing rate; readings (a) spikes over the\n    total duration of the task trials, (b) over the whole session. Open, the noise SD of the\n    SNR; readings (a) the mean over samples of the deposited waveform SD, (b) the waveform SD\n    at the first samples of the 2 ms window. Reproduced when, under one reading, all three\n    means are within tolerance.\n- id: fig2b-maintenance-neurons-hippocampus\n  statement: >-\n    Neurons with higher firing during maintenance than fixation (maintenance neurons) occurred\n    in all three areas, most frequently in hippocampus, where 20.6% of the recorded neurons\n    were maintenance neurons.\n  source: Results, Single-unit electrophysiology, paragraph 2; Figure 2B; table S2 (Fig. 2b)\n  quote: >-\n    We identified maintenance neurons in all recorded areas ( Fig. 2B ); however, they occurred\n    most frequently within the hippocampus (χ 2 1 = 47.30, P = 6.1 × 10 −12 ), where 20.6% of all\n    recorded neurons were maintenance neurons (permutation test against scrambled data, P =\n    0.002)\n  statistics:\n  - about: hippocampus against the other areas\n    test: chi-square test\n    statistic: chi2(1) = 47.30\n    p: 6.1e-12\n  - about: percentage of maintenance neurons in each area against scrambled data\n    test: permutation test against scrambled data\n    p: 0.002\n    n: 1000 resampling runs (table S2), P = 0.002 for each of the three areas\n  expected:\n  - quantity: maintenance neurons, percentage of hippocampal neurons\n    value: 20.6\n    tolerance: 2.06\n    unit: '%'\n  - quantity: chi-square value\n    value: 47.30\n    tolerance: 4.73\n  criterion: >-\n    Correct trials. A maintenance neuron has a higher firing rate in maintenance (-3 to 0 s)\n    than in fixation (-6 to -5 s) (fig. S2 legend) by a permutation t test (Results; Methods,\n    Statistics), on per-trial rates, paired and unpaired as named in the opening comment,\n    P < 0.05. Per area, the count is compared with a null from shuffling the maintenance and\n    fixation labels within each trial and rerunning the selection (\"permuted labels\", Fig. 2\n    legend), at both numbers of repetitions. The chi-square has 1 degree of freedom; readings\n    (a) a 2 x 2 table of hippocampus against entorhinal cortex and amygdala pooled, without\n    continuity correction, (b) the same with Yates correction. Reproduced when, under one\n    reading of each open detail, the hippocampal percentage is the highest of the three areas\n    and within tolerance, the chi-square has P < 0.05, and the hippocampal count exceeds the\n    null at P < 0.05; partially reproduced when hippocampus is highest and significant but the\n    percentage is outside tolerance.\n- id: fig2c-load-dependent-maintenance-neurons\n  statement: >-\n    During maintenance, 15% of hippocampal maintenance neurons (21 neurons) increased their\n    firing rate with workload (set size 4 against set sizes 6 and 8), a significant percentage\n    against scrambled data; the percentage was not significant in entorhinal cortex or\n    amygdala.\n  source: Results, Single-unit electrophysiology, paragraph 2; Figure 2C; table S2 (Fig. 2c)\n  quote: >-\n    During maintenance, a subset of maintenance neurons in the hippocampus (15%, 21 neurons;\n    permutation test against scrambled data, P = 0.002) increased their firing rates\n    systematically with workload (set size 4 versus set sizes 6 and 8; Fig. 2C )\n  statistics:\n  - about: hippocampus against scrambled data\n    test: permutation test against scrambled data\n    p: 0.002\n  - about: entorhinal cortex and amygdala against scrambled data\n    test: permutation test against scrambled data\n    p: 0.05\n    p_relation: \">\"\n    n: table S2 prints n.s. for both\n  expected:\n  - quantity: load-dependent hippocampal maintenance neurons\n    value: 21\n    tolerance: 2.1\n  - quantity: percentage of hippocampal maintenance neurons\n    value: 15\n    tolerance: 1.5\n    unit: '%'\n  depends_on:\n  - fig2b-maintenance-neurons-hippocampus\n  criterion: >-\n    Maintenance neurons from fig2b-maintenance-neurons-hippocampus, correct trials, maintenance\n    -3 to 0 s. The test of load dependence is not named; readings (a) a permutation t test of\n    per-trial maintenance rates, set size 4 against 6 and 8 (Methods, Statistics, for two\n    distributions), (b) a cluster-based nonparametric permutation test on the firing rate over\n    the maintenance period, 500 ms bins at 20 ms steps (Fig. 2A legend; Methods, Statistics,\n    for firing rates), each at P < 0.05 with the rate higher for 6 and 8. The null shuffles set\n    size labels across trials and reruns the test (\"permuted labels\", Fig. 2 legend), at both\n    numbers of repetitions. Reproduced when, under one reading, the hippocampal count is within\n    tolerance and significant at P < 0.05 and neither other area is significant; partially\n    reproduced when hippocampus is significant but the count is outside tolerance or another\n    area is significant too.\n- id: fig3e-probe-neurons-entorhinal\n  statement: >-\n    Neurons firing specifically after the probe letter (probe neurons) occurred in all areas,\n    most prominently in entorhinal cortex, where 9% of neurons (41) were probe neurons.\n  source: Results, Single-unit electrophysiology, paragraph 3; Figure 3E; table S2 (Fig. 3e)\n  quote: >-\n    We identified probe neurons in all areas and, most prominently, in the entorhinal cortex (χ 2\n    1 = 23.16, P = 1.5 × 10 −6 ; Fig. 3E ), in which 9% of neurons were probe neurons (41\n    neurons; permutation test against scrambled data, P = 0.001)\n  statistics:\n  - about: entorhinal cortex against the other areas\n    test: chi-square test\n    statistic: chi2(1) = 23.16\n    p: 1.5e-6\n  - about: percentage of probe neurons in each area against scrambled data\n    test: permutation test against scrambled data\n    p: 0.001\n    n: 1000 resampling runs (table S2), P = 0.001 for each of the three areas\n  expected:\n  - quantity: entorhinal probe neurons\n    value: 41\n    tolerance: 4.1\n  - quantity: chi-square value\n    value: 23.16\n    tolerance: 2.32\n  criterion: >-\n    Correct trials. A probe neuron has a higher firing rate after the probe than in encoding\n    (-5 to -3 s) and than in maintenance (-3 to 0 s), each by a permutation t test at P < 0.05\n    (Results, same paragraph). The probe window is not given; readings (a) 0 to 1 s after probe\n    onset, (b) probe onset to the button press of each trial, (c) 0 to 0.5 s, the window used\n    for retrieval decoding (Methods, Neural decoding). Paired and unpaired as in the opening\n    comment. Null and chi-square readings as in fig2b-maintenance-neurons-hippocampus, with\n    entorhinal cortex against the other two areas. Reproduced when, under one reading,\n    entorhinal cortex has the highest percentage, its count is within tolerance, the\n    chi-square has P < 0.05 and the entorhinal count exceeds the null at P < 0.05.\n- id: fig3-probe-onset-not-movement\n  statement: >-\n    Peak firing of probe neurons was higher when aligned to probe onset than when aligned to\n    the button press (5.47 +/- 4.97 Hz against 4.28 +/- 4.37 Hz), so their firing reflects the\n    probe stimulus more than movement preparation.\n  source: Results, Single-unit electrophysiology, paragraph 4; Figure 3A and 3B\n  quote: >-\n    Aligning the response with the probe stimulus onset resulted in significantly higher peak\n    firing rates (mean for all probe neurons, 5.47 ± 4.97 Hz versus 4.28 ± 4.37 Hz; permutation t\n    test, t 75 = 4.40, P = 0.0005\n  statistics:\n  - test: permutation t test\n    statistic: t(75) = 4.40\n    p: 0.0005\n    n: 76 probe neurons (from the degrees of freedom)\n  expected:\n  - quantity: mean peak rate, probe aligned\n    value: 5.47\n    tolerance: 0.547\n    unit: Hz\n  - quantity: mean peak rate, button aligned\n    value: 4.28\n    tolerance: 0.428\n    unit: Hz\n  depends_on:\n  - fig3e-probe-neurons-entorhinal\n  criterion: >-\n    All probe neurons of fig3e-probe-neurons-entorhinal (76 by the reported degrees of freedom\n    and by 8 neurons being 10.5%). Per neuron, the maximum of the trial-averaged rate in 200 ms\n    bins at 20 ms steps (Fig. 3 legend) after each alignment; paired permutation t test over\n    neurons (Methods, Statistics). Open, the window of the maximum; readings (a) 0 to 1 s after\n    the alignment event, (b) 1 s before to 1 s after it. Reproduced when, under one reading,\n    the probe-aligned peak is higher with P < 0.05 and both means are within tolerance;\n    partially reproduced when the direction and test hold but a mean is outside tolerance.\n- id: fig3-probe-neurons-few-task-specific\n  statement: >-\n    Only a few probe neurons reflected the decision (8 neurons, 10.5% of probe neurons, IN\n    against OUT), and only one showed workload dependence.\n  source: Results, Single-unit electrophysiology, paragraph 4; Figure 3A to 3D\n  quote: >-\n    However, only a small number of probe neurons (eight neurons, 10.5% of probe neurons)\n    reflected the subject's decision (IN versus OUT; Fig. 3 , A and B), and only one neuron\n    showed workload dependence\n  expected:\n  - quantity: probe neurons with IN/OUT difference\n    value: 8\n    tolerance: 0.8\n  - quantity: percentage of probe neurons with IN/OUT difference\n    value: 10.5\n    tolerance: 1.05\n    unit: '%'\n  - quantity: probe neurons with workload dependence\n    value: 1\n    tolerance: 0\n  depends_on:\n  - fig3e-probe-neurons-entorhinal\n  criterion: >-\n    Probe neurons from fig3e-probe-neurons-entorhinal. IN against OUT, and set size 4 against 6\n    and 8, by a cluster-based nonparametric permutation test at P < 0.05 on the rate in 200 ms\n    bins at 20 ms steps after probe onset (Fig. 3A and 3C legends). The time range tested is\n    not given; readings (a) 0 to 1 s after probe onset, (b) 0 to 2 s. Reproduced when, under\n    one reading, both counts are within tolerance (a count of one may be 0 to 2, as 10% of one\n    neuron cannot be judged); partially reproduced when one holds.\n- id: fig4a-dpca-workload-separation\n  statement: >-\n    The first three demixed principal components of the population firing rates explained\n    44.7% of the variance and separated set sizes 4, 6 and 8, with three angles of 120 degrees\n    in the dPC2-dPC3 plane; the first 15 components explained 79%.\n  source: Results, Attractors in neural population dynamics, paragraph 1; Figure 4A; fig. S3\n  quote: >-\n    We formed a three-dimensional space from the first three demixed principal components (dPCs\n    1, 2, and 3, explaining 44.7% of the variance; Fig. 4A , fig. S3, and movie S1). dPCA\n    distinguished between workloads 4, 6, and 8.\n  expected:\n  - quantity: variance explained by dPCs 1 to 3\n    value: 44.7\n    tolerance: 4.47\n    unit: '%'\n  - quantity: variance explained by the first 15 dPCs\n    value: 79\n    tolerance: 7.9\n    unit: '%'\n  - quantity: angles between set-size trajectories in the dPC2-dPC3 plane, maintenance\n    value: 120\n    tolerance: 12\n    unit: degrees\n  criterion: >-\n    dPCA (Kobak et al. 2016) of all neurons, correct trials, trial-averaged per set size, from\n    spikes in 2 ms bins smoothed with a 1000 ms Gaussian kernel and z-scored to the fixation\n    period (Methods, dPCA of firing rates), with time and set-size marginalizations, components\n    ordered by explained variance. Open, the scale of the z-score; readings (a) mean and SD of\n    the fixation rate, (b) fixation mean and SD over the whole trial. Open, the dPCA\n    regularization; readings (a) the toolbox's cross-validated lambda, (b) none. Angles are\n    those at the centroid between the three set-size points of the dPC2-dPC3 projection,\n    averaged over maintenance. Reproduced when, under one reading, both variances and all three\n    angles are within tolerance; partially reproduced when the set sizes separate (all\n    pairwise maintenance distances exceed those of label-shuffled dPCA runs) but a value is\n    outside tolerance.\n- id: fig4b-speed-lowest-maintenance\n  statement: >-\n    In the dPCA state space, the speed of the population trajectory was highest during\n    encoding and lowest during maintenance, lower than in each other trial period, including\n    fixation.\n  source: Results, Attractors in neural population dynamics, paragraph 2; Figure 4B\n  quote: >-\n    The speed was highest during encoding, when maintenance neurons ramped up their firing. By\n    contrast, speed was lowest during maintenance (permutation t test against the other trial\n    periods, P = 0.0005)\n  statistics:\n  - test: permutation t test against the other trial periods\n    p: 0.0005\n    n: 200 dPCA runs on 20% subsamples (Methods); 2000 permutations (table S2)\n  depends_on:\n  - fig4a-dpca-workload-separation\n  criterion: >-\n    The dPCA of fig4a-dpca-workload-separation, first 15 dPCs (Fig. 4 legend). Speed V(t) as\n    Methods equation 2 with step 20 ms, averaged over set sizes and over each period; 200 runs\n    of dPCA on neural trajectories subsampled at 20% with replacement (Methods). Periods\n    fixation -6 to -5 s, encoding -5 to -3 s, maintenance -3 to 0 s; the retrieval window is\n    not given; readings (a) 0 to 1 s after probe onset, (b) 0 to 2 s. Permutation t test of the\n    200 per-run maintenance speeds against each other period. Reproduced when, under one\n    reading, maintenance speed is below each other period with P < 0.05 and encoding speed is\n    the highest; partially reproduced when maintenance is lowest but encoding is not highest.\n- id: fig4c-distance-largest-maintenance\n  statement: >-\n    The pairwise distance between the trajectories of different set sizes was larger during\n    maintenance than during encoding, and the largest of the trial periods.\n  source: Results, Attractors in neural population dynamics, paragraph 2; Figure 4C\n  quote: >-\n    Analyzing the pairwise distance between trajectories that corresponded to different set\n    sizes, we found that the distances during maintenance were larger than during encoding\n    (permutation t test, P = 0.0005; Fig. 4C )\n  statistics:\n  - test: permutation t test\n    p: 0.0005\n  depends_on:\n  - fig4a-dpca-workload-separation\n  criterion: >-\n    As fig4b-speed-lowest-maintenance, with distance from Methods equation 1 between each of\n    the three pairs of set-size trajectories, averaged over pairs and over each period, 200\n    subsampled runs. Reproduced when, under one reading, maintenance distance exceeds encoding\n    distance with P < 0.05 and is the largest of the four periods; partially reproduced when it\n    exceeds encoding only.\n- id: fig4d-encoding-decodes-correct\n  statement: >-\n    During encoding of high-workload trials (set sizes 6 and 8), hippocampal neurons, but not\n    entorhinal or amygdala neurons, predicted whether the subject would later respond correctly,\n    with a median decoding accuracy of 80%.\n  source: Results, Decoding of information during the trial, paragraph 2; Figure 4D\n  quote: >-\n    For the encoding period (−5 to −3 s), we found that the activity of hippocampal neurons, but\n    not neurons in other areas, could be used to decode whether the subject would later reply\n    correctly or incorrectly in the trial. The median decoding accuracy was 80% (permutation test\n    against scrambled data, P = 0.002; Fig. 4D )\n  statistics:\n  - test: permutation test against scrambled data\n    p: 0.002\n    corrected: Bonferroni over 12 tests, corrected P = 0.024\n    n: 500 decoder runs with scrambled labels\n  expected:\n    quantity: median decoding accuracy, hippocampus, encoding\n    value: 80\n    tolerance: 8\n    unit: '%'\n  criterion: >-\n    Pseudopopulation decoding with a support vector machine as in the NDT toolbox (Methods,\n    Neural decoding): spikes in 1 ms bins smoothed in a 1500 ms window, classified at 250 ms\n    steps, 500 resampling runs, trials of set sizes 6 and 8 (Fig. 4D legend), units from\n    sessions with at least five incorrect responses, five cross-validation splits; null from\n    500 runs with scrambled labels; Bonferroni over 12 tests. Populations hippocampus,\n    entorhinal cortex and amygdala. Open, the smoothing window shape; readings (a) a 1500 ms\n    boxcar (NDT binning), (b) a Gaussian. Open, feature normalization; readings (a) z-score\n    per neuron on training data (NDT's usual preprocessing), (b) none. Open, the SVM kernel;\n    the reading is NDT's default linear kernel. Open, how \"median accuracy\" is taken; readings\n    (a) median over resampling runs of the accuracy averaged over the 250 ms steps inside -5 to\n    -3 s, (b) median over runs and steps together. Reproduced when, under one reading,\n    hippocampus is above the null at corrected P < 0.05 with median within tolerance and\n    neither other area is significant; partially reproduced when hippocampus holds and another\n    area is significant too.\n- id: fig4e-maintenance-decodes-workload\n  statement: >-\n    During maintenance, workload (set size 4 against 6 and 8) could be decoded from hippocampal\n    neurons with a median accuracy of 80%, but not from neurons of the other areas.\n  source: Results, Decoding of information during the trial, paragraph 2; Figure 4E\n  quote: >-\n    For the maintenance period, we found that the workload (set size 4 versus set sizes 6 and 8)\n    of each trial could be decoded from hippocampal neurons but not from neurons in the other\n    areas (permutation test against scrambled data, P = 0.002; Fig. 4E ). The median decoding\n    accuracy was 80%.\n  statistics:\n  - test: permutation test against scrambled data\n    p: 0.002\n    corrected: Bonferroni over 12 tests, corrected P = 0.024\n    n: 500 decoder runs with scrambled labels\n  expected:\n    quantity: median decoding accuracy, hippocampus, maintenance\n    value: 80\n    tolerance: 8\n    unit: '%'\n  criterion: >-\n    As fig4d-encoding-decodes-correct, with correct trials, labels set size 4 against 6 and 8,\n    all units, ten cross-validation splits, and the maintenance period -3 to 0 s. Open, class\n    balance; readings (a) equal numbers of trials per class drawn for each neuron (NDT's\n    requirement), (b) all trials. Reproduced when, under one reading, hippocampus is above the\n    null at corrected P < 0.05 with median within tolerance and neither entorhinal cortex nor\n    amygdala is significant; partially reproduced when hippocampus holds and another area is\n    significant too.\n- id: fig4e-workload-decoding-leave-one-subject-out\n  statement: >-\n    Excluding any one subject changed the hippocampal workload decoding accuracy to a value in\n    the range 71 to 81%.\n  source: Results, Decoding of information during the trial, paragraph 2\n  quote: >-\n    To ensure that some subjects did not drive the results, we performed a leave-one-out\n    analysis. The exclusion of any subject changed the decoding accuracy to a value in the range\n    [71 to 81%].\n  expected:\n  - quantity: lowest leave-one-subject-out accuracy\n    value: 71\n    tolerance: 7.1\n    unit: '%'\n  - quantity: highest leave-one-subject-out accuracy\n    value: 81\n    tolerance: 8.1\n    unit: '%'\n  depends_on:\n  - fig4e-maintenance-decodes-workload\n  criterion: >-\n    The decoder of fig4e-maintenance-decodes-workload rerun nine times, each without the\n    hippocampal units of one subject. Reproduced when all nine accuracies lie in 71 to 81%\n    widened by 10% of each bound (63.9 to 89.1%), under a reading of fig4e that reproduced.\n- id: fig4e-maintenance-neurons-carry-workload\n  statement: >-\n    Workload decoding from hippocampal maintenance neurons alone was little different from\n    decoding from all hippocampal neurons, while excluding the maintenance neurons reduced the\n    accuracy to 71%.\n  source: Results, Decoding of information during the trial, paragraph 2; Figure 4E\n  quote: >-\n    We also performed the same analysis using only maintenance neurons; there was little\n    difference in the decoding accuracy between the use of only maintenance neurons and the use\n    of the whole population of hippocampal neurons. Conversely, the exclusion of maintenance\n    neurons reduced the prediction accuracy to 71%.\n  expected:\n    quantity: accuracy without maintenance neurons\n    value: 71\n    tolerance: 7.1\n    unit: '%'\n  depends_on:\n  - fig2b-maintenance-neurons-hippocampus\n  - fig4e-maintenance-decodes-workload\n  criterion: >-\n    The decoder of fig4e-maintenance-decodes-workload on (i) hippocampal maintenance neurons\n    only and (ii) hippocampal neurons other than maintenance neurons. \"Little difference\" is not\n    quantified; it is judged as the maintenance-neuron median within 8 percentage points (the\n    10% tolerance of the 80% accuracy) of the all-hippocampus median, with (i) significant\n    against its scrambled null (Fig. 4E legend, \"Sufficient decoding was possible\"). Reproduced\n    when both parts hold and (ii) is within tolerance and below the all-hippocampus median.\n- id: fig4e-no-decoding-6-vs-8\n  statement: >-\n    The decoder did not distinguish trials of set size 6 from set size 8.\n  source: Results, Decoding of information during the trial, paragraph 2\n  quote: >-\n    The decoder did not distinguish between trials of set sizes 6 and 8, which points to a\n    ceiling effect\n  depends_on:\n  - fig4e-maintenance-decodes-workload\n  criterion: >-\n    A claim of absence. The paper reports no separate test; the decoding test of the Methods is\n    used, as in fig4e-maintenance-decodes-workload, with labels set size 6 against 8,\n    hippocampal neurons, maintenance period, against 500 scrambled-label runs at P < 0.05\n    (uncorrected, as the strictest reading against absence). Reproduced when the accuracy is\n    not above the null; not reproduced when it is. The median accuracy is reported either way.\n- id: fig4f-retrieval-decodes-response\n  statement: >-\n    During retrieval (500 ms before the button press), neurons in all recorded areas predicted\n    the IN or OUT response; with all neurons the median decoding accuracy reached 90%.\n  source: Results, Decoding of information during the trial, paragraph 2; Figure 4F\n  quote: >-\n    For the retrieval period, we found that neurons from all areas encoded whether the subject\n    would later reply by pressing the IN or OUT button in the trial (permutation test against\n    scrambled data, P = 0.002; Fig. 4F ). The median decoding accuracy reached 90% if firing\n    from all neurons was included\n  statistics:\n  - test: permutation test against scrambled data\n    p: 0.002\n    corrected: Bonferroni over 12 tests, corrected P = 0.024\n  expected:\n    quantity: median decoding accuracy, all neurons, retrieval\n    value: 90\n    tolerance: 9\n    unit: '%'\n  criterion: >-\n    As fig4d-encoding-decodes-correct, with correct trials, labels IN against OUT, a 500 ms\n    window ending at the button press (Fig. 4F legend, -500 to 0 ms; Methods, a narrow 500 ms\n    window), ten cross-validation splits, populations hippocampus, entorhinal cortex, amygdala\n    and all neurons. Reproduced when, under one reading, each of the four populations is above\n    its null at corrected P < 0.05 and the all-neuron median is within tolerance; partially\n    reproduced when some but not all areas are significant.\n- id: figs3d-hippocampus-loadings\n  statement: >-\n    Ranking the first 200 neurons of each region by their dPCA loading, hippocampal neurons had\n    higher loadings than entorhinal neurons at each rank except the first three.\n  source: fig. S3d legend\n  quote: >-\n    For each rank, hippocampus (cyan) had a higher loading than entorhinal cortex (magenta)\n    (paired Wilcoxon test P < 10-33) and amygdala (yellow), except for the first three ranks\n  statistics:\n  - about: hippocampus against entorhinal cortex, rank by rank\n    test: paired Wilcoxon test\n    p: 1.0e-33\n    p_relation: \"<\"\n    n: 400 neurons (table S2)\n  depends_on:\n  - fig4a-dpca-workload-separation\n  criterion: >-\n    The dPCA of fig4a-dpca-workload-separation. The legend names both dPC3 (title) and dPC2\n    (text); readings (a) dPC2, (b) dPC3. Loadings taken as absolute decoder weights. Per region\n    the 200 largest, sorted; paired Wilcoxon signed-rank test of hippocampus against entorhinal\n    cortex over the 200 ranks. Reproduced when, under one reading, hippocampus is higher with\n    P < 0.05 and higher than amygdala at most ranks.\n- id: fig5-subject1-eeg-power-workload\n  statement: >-\n    In subject 1, scalp EEG power during the last 2 s of maintenance was higher for set size 8\n    than for set size 4 at Pz (8.5 to 16 Hz) and at Fz (8 to 12.5 Hz); this workload-dependent\n    power increase did not appear in the other subjects.\n  source: Results, Electrophysiology of cortico-hippocampal functional coupling, paragraph 2; Figure 5B and 5C; fig. S5; table S1\n  quote: >-\n    the scalp EEG power increased during maintenance for a high workload (set size 8), with a\n    peak within the 8- to 12-Hz alpha range over parietal cortex ( Fig. 5 , A and B). This\n    workload-dependent EEG power increase extended to frontal electrode Fz ( Fig. 5C ). While\n    this power increase is known from healthy subjects for the same or similar task ( 5 , 6 ),\n    it did not appear in the other subjects of our study group (fig. S5 and table S1)\n  statistics:\n  - test: cluster-based nonparametric permutation test\n    p: 0.05\n    p_relation: \"<\"\n    n: 61 trials of set sizes 4 and 8 in subject 1 (Fig. 5 legend)\n  criterion: >-\n    Last 2 s of maintenance, scalp EEG re-referenced to averaged mastoids, multitaper spectra\n    (+/- 2 Hz smoothing, seven tapers; Methods, Frequency spectra), trials of set size 8\n    against 4, cluster-based nonparametric permutation test over frequency (P < 0.05). Open,\n    the frequency range tested; readings (a) 4 to 30 Hz (the time-frequency range in Methods),\n    (b) 1 to 40 Hz. Subject 1 reproduced when Pz and Fz each have a significant cluster of\n    higher set size 8 power overlapping 8.5 to 16 Hz and 8 to 12.5 Hz respectively. \"Other\n    subjects\": table S1 gives EEG workload dependence as no for subjects 2 to 8 and decrease\n    for subject 9, on the channels of fig. S5, which are not named in the text (the legend\n    cites table S7, which does not exist); the reading is the scalp electrode of each subject's\n    maximal PLV (table S1). Reproduced when subject 1 holds and at most one other subject has\n    a significant increase.\n- id: fig5-subject1-hippocampal-power-workload\n  statement: >-\n    In subject 1, theta-alpha power (7.5 to 10 Hz) in the left hippocampal iEEG increased with\n    workload during maintenance.\n  source: Figure 5G and 5H; Results, Electrophysiology of cortico-hippocampal functional coupling, paragraph 2\n  quote: >-\n    Theta-alpha power (7.5 to 10.0 Hz) in the left hippocampal iEEG increased with workload\n    during maintenance.\n  statistics:\n  - test: cluster-based nonparametric permutation test\n    p: 0.05\n    p_relation: \"<\"\n  criterion: >-\n    Subject 1, the left hippocampal bipolar channel of the maximal PLV pair (table S1), last 2 s\n    of maintenance, multitaper spectra as in fig5-subject1-eeg-power-workload, normalized to\n    fixation power (Fig. 5H legend), set size 8 against 4, cluster-based test at P < 0.05.\n    Reproduced when a significant cluster of higher set size 8 power overlaps 7.5 to 10 Hz.\n    Table S1 also lists iEEG workload dependence as increase for subjects 1 and 6 and no for\n    the others; this is reported for all subjects.\n- id: fig5-subject1-neurons-workload\n  statement: >-\n    In subject 1, the average firing rate of the five hippocampal maintenance neurons was higher\n    for high workload (set size 8 against 4) during encoding and maintenance.\n  source: Figure 5I; Results, Electrophysiology of cortico-hippocampal functional coupling, paragraph 2\n  quote: >-\n    The average firing rate of maintenance neurons in this subject was higher for a high workload\n    during encoding and maintenance ( n = 5 hippocampal neurons with more than 100 spikes during\n    both encoding and maintenance)\n  statistics:\n  - test: cluster-based nonparametric permutation test\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n    quantity: subject 1 hippocampal maintenance neurons with more than 100 spikes in encoding and in maintenance\n    value: 5\n    tolerance: 0\n  depends_on:\n  - fig2b-maintenance-neurons-hippocampus\n  criterion: >-\n    Subject 1, hippocampal maintenance neurons from fig2b-maintenance-neurons-hippocampus with\n    more than 100 spikes in encoding and in maintenance. Their average rate over time, set size\n    8 against 4, cluster-based nonparametric permutation test at P < 0.05. Open, the unit of\n    the test; readings (a) trials, with the per-trial rate averaged over the five neurons,\n    (b) neuron-trial pairs. Reproduced when, under one reading, the count is 5 and significant\n    clusters of higher set size 8 rate fall in both encoding and maintenance.\n- id: fig5-subject1-plv-hippocampus-pz\n  statement: >-\n    In subject 1, the task increased the phase locking value (PLV) between hippocampal iEEG and\n    scalp EEG at Pz in the alpha band during the last 2 s of maintenance; this PLV was higher\n    for set size 8 than 4 (9.0 to 12.0 Hz) and maximal at occipitoparietal electrodes. The PLV\n    to Fz was also higher for set size 8 (8.5 to 10 Hz).\n  source: Figure 5D, 5E and 5F; Results, Electrophysiology of cortico-hippocampal functional coupling, paragraph 3; fig. S4\n  quote: >-\n    The WM task enhanced the hippocampal-cortical PLV specifically in the 8–10 Hz alpha range and\n    during the maintenance period ( Fig. 5D and fig. S4). The PLV increased with workload ( Fig.\n    5E ) and was highest at occipitoparietal electrode sites ( Fig. 5F ).\n  statistics:\n  - test: randomization test against a null distribution with scrambled labels\n    p: 0.05\n    p_relation: \"<\"\n  depends_on:\n  - fig6-plv-all-subjects\n  criterion: >-\n    The PLV method of fig6-plv-all-subjects for subject 1. Reproduced when the maximal PLV pair\n    is the left hippocampus with Pz, its workload difference (set size 8 minus 4) exceeds the\n    95th percentile of the label-shuffled null in bins overlapping 9.0 to 12.0 Hz, the scalp\n    electrode with the highest alpha PLV to that hippocampal channel is parietal or occipital,\n    and the hippocampus-Fz workload difference is significant in bins overlapping 8.5 to 10 Hz;\n    partially reproduced when the Pz parts hold and the Fz part does not.\n- id: fig6-plv-all-subjects\n  statement: >-\n    All subjects showed a significant hippocampal-scalp PLV peak during maintenance (set size\n    8), with individual frequency bands whose lower bound lay in the theta-alpha range and which\n    extended up to 17.5 Hz (median band limits 6.0 to 11.5 Hz).\n  source: Results, Cortico-hippocampal low-frequency coupling in the group of subjects, paragraph 1; Figure 6A to 6H; table S1\n  quote: >-\n    All subjects showed a significant PLV peak for at least one pair of signals recorded from a\n    scalp electrode and a hippocampal channel (table S1). The frequency band of the maximal\n    significant PLV indicated individual differences\n  statistics:\n  - test: randomization test against a null distribution with scrambled trials\n    p: 0.05\n    p_relation: \"<\"\n    n: nine subjects\n  expected:\n  - quantity: subjects with significant PLV\n    value: 9\n    tolerance: 0\n  - quantity: median lower band limit\n    value: 6.0\n    tolerance: 0.6\n    unit: Hz\n  - quantity: median upper band limit\n    value: 11.5\n    tolerance: 1.15\n    unit: Hz\n  criterion: >-\n    Per subject, every pair of a hippocampal bipolar iEEG channel (deepest contacts of each\n    hippocampal macroelectrode) and a scalp electrode. Last 2 s of maintenance, 2-s epochs,\n    set size 8, multitaper spectra (+/- 2 Hz, seven tapers, the spectra of Methods, Frequency\n    spectra, which the PLV section says it uses), PLV as Methods equation 3. Significance per\n    frequency bin against the 95th percentile of 200 PLVs with trials of one channel permuted\n    (one-tailed). The pair and band of the highest significant PLV are kept (table S1); the\n    individual band is the contiguous run of significant bins around the peak. Open, the\n    frequency range searched; readings (a) 4 to 30 Hz, (b) 1 to 40 Hz. Trials as in the\n    opening comment. Reproduced when, under one reading, all nine subjects have a significant\n    pair and both median band limits are within tolerance; partially reproduced when all nine\n    are significant and the medians are not.\n- id: tables1-plv-per-subject\n  statement: >-\n    Table S1 gives for each subject the scalp electrode of maximal PLV, its peak frequency and\n    the maximal PLV (subject 1 Pz 10.5 Hz 0.72; 2 F3 7 Hz 0.40; 3 F3 12 Hz 0.43; 4 F3 14 Hz\n    0.85; 5 P3 5.5 Hz 0.60; 6 O1 7.5 Hz 0.50; 7 O1 7.5 Hz 0.64; 8 O1 11.5 Hz 0.57; 9 O1 8 Hz\n    0.69), with the hippocampal electrode in the left hemisphere for subjects 1 to 6 and the\n    right for 7 to 9.\n  source: table S1\n  inferred: >-\n    Values only in table S1 (read from its extracted text by column order); no sentence states\n    them.\n  expected:\n  - quantity: maximal PLV, subject 1\n    value: 0.72\n    tolerance: 0.072\n  - quantity: maximal PLV, subject 2\n    value: 0.40\n    tolerance: 0.040\n  - quantity: maximal PLV, subject 3\n    value: 0.43\n    tolerance: 0.043\n  - quantity: maximal PLV, subject 4\n    value: 0.85\n    tolerance: 0.085\n  - quantity: maximal PLV, subject 5\n    value: 0.60\n    tolerance: 0.060\n  - quantity: maximal PLV, subject 6\n    value: 0.50\n    tolerance: 0.050\n  - quantity: maximal PLV, subject 7\n    value: 0.64\n    tolerance: 0.064\n  - quantity: maximal PLV, subject 8\n    value: 0.57\n    tolerance: 0.057\n  - quantity: maximal PLV, subject 9\n    value: 0.69\n    tolerance: 0.069\n  depends_on:\n  - fig6-plv-all-subjects\n  criterion: >-\n    From fig6-plv-all-subjects. Reproduced when, under one reading, at least seven of the nine\n    subjects have the same scalp electrode, hippocampal hemisphere, and maximal PLV within\n    tolerance; partially reproduced for four to six. Peak frequencies are reported against the\n    table.\n- id: fig6-plv-workload-eight-of-nine\n  statement: >-\n    During maintenance, PLV in the individual frequency band was higher for set size 8 than\n    set size 4 in eight of nine subjects (range 5.5 to 16.5 Hz, median band limits 7.8 to\n    10 Hz).\n  source: Results, Cortico-hippocampal low-frequency coupling in the group of subjects, paragraph 2; Figure 6A to 6H; table S1\n  quote: >-\n    During maintenance, the PLV was increased for high workload in eight of nine subjects in the\n    individual frequency band (set size 4 versus set size 8; permutation test, P = 0.05; range,\n    5.5 to 16.5 Hz; median band limits, 7.8 to 10 Hz; Fig. 6 and table S1)\n  statistics:\n  - test: permutation test, randomization against a null distribution with scrambled labels\n    p: 0.05\n    n: nine subjects, 200 permutations each\n  expected:\n  - quantity: subjects with workload-dependent PLV\n    value: 8\n    tolerance: 0\n  - quantity: median lower limit of the workload bands\n    value: 7.8\n    tolerance: 0.78\n    unit: Hz\n  - quantity: median upper limit of the workload bands\n    value: 10\n    tolerance: 1.0\n    unit: Hz\n  depends_on:\n  - fig6-plv-all-subjects\n  criterion: >-\n    The pair of fig6-plv-all-subjects per subject. PLV for set size 8 minus PLV for set size 4,\n    against the 95th percentile of 200 differences with the epochs randomly assigned to the two\n    set sizes (Methods, Phase-locking value). A subject counts when at least one bin inside the\n    individual band is significant. Table S1 lists subject 3 as not significant. Reproduced\n    when, under one reading, eight subjects count (seven or nine is partially reproduced) and\n    both medians and the range (5.5 to 16.5 Hz widened by 10% of each bound) hold.\n- id: fig6-plv-maintenance-over-encoding\n  statement: >-\n    The PLV during the last 2 s of maintenance exceeded the PLV during encoding in eight of nine\n    subjects, so hippocampal-cortical connectivity in the theta-alpha range increased\n    specifically during maintenance.\n  source: Results, Cortico-hippocampal low-frequency coupling in the group of subjects, paragraph 2; Figure 6A to 6H; table S1\n  quote: >-\n    the PLV during maintenance exceeded the PLV during encoding in eight of nine subjects ( Fig. 6\n    and table S1)\n  statistics:\n  - test: randomization test against a null distribution with scrambled labels\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n    quantity: subjects with maintenance PLV above encoding PLV\n    value: 8\n    tolerance: 0\n  depends_on:\n  - fig6-plv-all-subjects\n  criterion: >-\n    The pair of fig6-plv-all-subjects per subject. PLV in the last 2 s of maintenance minus PLV\n    in encoding (-5 to -3 s), against the 95th percentile of 200 differences with epochs\n    randomly assigned to the two periods (Methods). Open, which trials; readings (a) set size 8\n    trials, where the PLV was selected, (b) all set sizes pooled. A subject counts when a bin in\n    the individual band is significant. Table S1 lists subject 4 as not significant. Reproduced\n    when, under one reading, eight subjects count; partially reproduced for seven or nine.\n- id: fig6-power-unchanged-individual-band\n  statement: >-\n    In the majority of subjects, iEEG and EEG power in the individual frequency band did not\n    differ during maintenance, which suggests that the PLV differences came from phase\n    consistency.\n  source: Results, Cortico-hippocampal low-frequency coupling in the group of subjects, paragraph 1; table S1\n  quote: >-\n    In the majority of the subjects, there were no differences in the iEEG or EEG power in the\n    individual frequency band during maintenance, which suggests that the differences in PLV were\n    primarily a result of the differences in phase consistency.\n  depends_on:\n  - fig6-plv-all-subjects\n  criterion: >-\n    A claim of absence. Table S1 reports it as workload dependence (set size 8 against 4) of\n    EEG and of iEEG power, so that is the comparison: per subject, the channels of the\n    maximal PLV pair, last 2 s of maintenance, multitaper spectra as in\n    fig5-subject1-eeg-power-workload, cluster-based permutation test at P < 0.05 over the\n    individual band. Reproduced when at least five of nine subjects show no significant\n    difference for EEG and at least five for iEEG; not reproduced otherwise. Table S1 has two\n    of nine with an EEG difference (subjects 1 and 9) and two with an iEEG difference\n    (subjects 1 and 6); the per-subject results are reported against it.\n- id: fig6i-plv-posterior-gradient\n  statement: >-\n    Across subjects, maximal PLV increased from the anterior to the posterior end of the\n    hippocampal axis (34 electrode pairs, R2 = 0.118), and PLV to posterior sites (y < -20 mm)\n    was higher than to anterior sites.\n  source: Figure 6I; Results, Cortico-hippocampal low-frequency coupling in the group of subjects, paragraph 3\n  quote: >-\n    For the subject group, there was a gradual increase in the PLV from the anterior end to the\n    posterior end of the hippocampal axis during maintenance ( R 2 = 0.118, P = 0.0467) and the\n    PLV to posterior sites ( y < −20 mm) was higher than to anterior sites (permutation t test, t\n    = 2.09, P = 0.0405)\n  statistics:\n  - about: linear fit of maximal PLV on anterior-posterior position\n    test: permutation t test\n    statistic: R2 = 0.118\n    p: 0.0467\n    n: 34 electrode pairs\n  - about: posterior (y < -20 mm) against anterior sites\n    test: permutation t test\n    statistic: t = 2.09\n    p: 0.0405\n  expected:\n  - quantity: R2 of the linear fit\n    value: 0.118\n    tolerance: 0.0118\n  - quantity: electrode pairs\n    value: 34\n    tolerance: 0\n  depends_on:\n  - fig6-plv-all-subjects\n  criterion: >-\n    Per subject, the scalp electrode of the maximal PLV pair, paired with every hippocampal\n    bipolar channel; for each, the maximal PLV in the subject's individual band during\n    maintenance, set size 8 (as in fig6-plv-all-subjects), plotted against the MNI y coordinate\n    of the hippocampal contact (Fig. 6I). Open, the coordinate of a bipolar channel; readings\n    (a) the deepest contact, (b) the midpoint of the two contacts. The fit's P from a\n    permutation of PLV values over positions (2000 permutations; table S2 gives 32 degrees of\n    freedom). Reproduced when, under one reading, the slope is positive (PLV higher\n    posteriorly) with P < 0.05 and posterior sites exceed anterior sites by an unpaired\n    permutation t test at P < 0.05; partially reproduced when one of the two holds.\n- id: fig6i-no-left-right-difference\n  statement: >-\n    There was no evidence that the PLV differed between left and right hippocampus.\n  source: Results, Cortico-hippocampal low-frequency coupling in the group of subjects, paragraph 3; Figure 6I\n  quote: >-\n    There was no evidence that the PLV differed between the left and right hippocampus.\n  depends_on:\n  - fig6i-plv-posterior-gradient\n  criterion: >-\n    A claim of absence. The paper names no test here; Methods, Statistics, give the permutation\n    t test for comparing two distributions, which is used: the 34 maximal PLV values of\n    fig6i-plv-posterior-gradient, left against right channels, unpaired, P < 0.05. Reproduced\n    when the test is not significant; not reproduced when it is. The difference of means is\n    reported either way.\n- id: soz-plv-no-difference\n  statement: >-\n    The increase in PLV did not differ significantly between hippocampal channels inside and\n    outside the seizure onset zone.\n  source: Results, Recordings in the epileptogenic zone, paragraph 1; table S1\n  quote: >-\n    When comparing hippocampal channels within and outside the seizure onset zone (SOZ) (table\n    S1), the increase in the PLV was not significantly different between the non-SOZ electrodes\n    and SOZ electrodes.\n  depends_on:\n  - fig6-plv-all-subjects\n  criterion: >-\n    A claim of absence, with the permutation t test of Methods, Statistics, unpaired, P < 0.05.\n    SOZ membership from the deposited SOZ electrode list (table S1 marks the maximal-PLV\n    hippocampal channel as SOZ in subjects 3 and 4). Open, which increase; readings (a) set\n    size 8 minus set size 4, (b) maintenance minus encoding, each the maximum in the individual\n    band. Open, which channels; readings (a) all hippocampal channels paired with the\n    maximal-PLV scalp electrode, as in Fig. 6I, (b) the nine maximal-PLV pairs. Reproduced when\n    no reading finds a significant difference; not reproduced when a reading does. Effect\n    sizes are reported for every reading.\n- id: hfo-rates-unaffected\n  statement: >-\n    The rates of clinically relevant high-frequency oscillations were not affected by\n    performing the task.\n  source: Results, Recordings in the epileptogenic zone, paragraph 1\n  quote: >-\n    The rates of clinically relevant HFOs were not affected by the performance of the task.\n  criterion: >-\n    A claim of absence for which the paper names neither the HFO detector nor the test nor the\n    comparison. It cites reference 27 (Fedele et al. 2017, Sci Rep 7, 13836) for the detector;\n    that paper is not under paper/ and was not read. Until that method is supplied (a\n    question to a reader), the test is the permutation t test of Methods, Statistics, at\n    P < 0.05, comparing per-channel HFO rates in task periods (encoding and maintenance) with\n    fixation, and the detector is the one reference 27 gives. Reproduced when no channel group\n    (SOZ, non-SOZ) shows a significant difference; not reproduced when one does.\n- id: sfc-maintenance-over-encoding\n  statement: >-\n    Maintenance neurons showed significant spike-field coherence to the local field potential,\n    but not to the iEEG or scalp EEG, and for all frequency bins the percentage of neurons with\n    spike-field coherence was higher during maintenance than during encoding.\n  source: Results, Spike-field coherence, paragraph 1; fig. S6b; Figure 5J\n  quote: >-\n    We found significant spike-field coherence to the LFP but not to the iEEG or the scalp EEG.\n    For all frequency bins, the percentage of neurons with spike-field coherence was higher\n    during maintenance than during encoding (fig. S6).\n  expected:\n    quantity: maintenance neurons with at least 100 spikes in maintenance and in encoding\n    value: 94\n    tolerance: 9.4\n  depends_on:\n  - fig2b-maintenance-neurons-hippocampus\n  criterion: >-\n    Maintenance neurons of fig2b-maintenance-neurons-hippocampus with at least 100 spikes in\n    both periods (fig. S6b legend gives N = 94). Pairwise phase consistency, the P-hat-2\n    estimator of Vinck et al. 2012 (FieldTrip ppc2), between each neuron's spikes and the LFP\n    of the same microwire; maintenance is the last 2 s (fig. S6a), encoding -5 to -3 s.\n    Significance per frequency bin against the 95th percentile of 200 PPCs with the spike\n    trials permuted (Methods, Spike-field coherence). Open, the frequency range; readings\n    (a) 4 to 30 Hz, (b) 1 to 40 Hz. Open, the spectral estimate around each spike; the\n    reading is FieldTrip's spike-triggered spectrum with a window of a fixed number of cycles,\n    and the cycle number is a further open detail, run at 3 and 5 cycles. Reproduced when,\n    under one reading, the maintenance percentage exceeds the encoding percentage in every\n    frequency bin and the percentages for iEEG and scalp EEG are no higher than the 5%\n    expected by chance; partially reproduced when the maintenance percentage is higher in most\n    bins. The LFP of the microwires is not among the data listed by the data descriptor; if\n    the dataset lacks it, the LFP parts are blocked and the iEEG and scalp EEG parts are run.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000574/10.1126-sciadv.aav3687.yaml paper/10.1126-sciadv.aav3687.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/000574 && python - <<'E'
p='10.1126-sciadv.aav3687.yaml'
s=open(p).read()
a="""    hippocampal neurons, maintenance period, against 500 scrambled-label runs at P < 0.05
    (uncorrected, as the strictest reading against absence). Reproduced when the accuracy is"""
b="""    hippocampal neurons, maintenance period, against 500 scrambled-label runs at P < 0.05
    (the Bonferroni correction of the Methods covers the 12 tests of Fig. 4D to 4F, which do
    not include this one). Reproduced when the accuracy is"""
assert a in s; s=s.replace(a,b)
a="""    (text); readings (a) dPC2, (b) dPC3. Loadings taken as absolute decoder weights. Per region"""
b="""    (text); readings (a) dPC2, (b) dPC3. Open, the loading; readings (i) the absolute decoder
    weight of the neuron, (ii) the signed weight. Per region"""
assert a in s; s=s.replace(a,b)
a="""quantified; it is judged as the maintenance-neuron median within 8 percentage points (the
    10% tolerance of the 80% accuracy) of the all-hippocampus median"""
b="""quantified; it is judged with the protocol's default tolerance, the maintenance-neuron
    median within 8 percentage points (10% of the 80% accuracy) of the all-hippocampus median"""
assert a in s; s=s.replace(a,b)
open(p,'w').write(s)
E
cd ../..; python tools/claims_check.py claims/000574/10.1126-sciadv.aav3687.yaml paper/10.1126-sciadv.aav3687.txt; grep -c "—\|rather" claims/000574/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -nE "^\s+[a-z_]+: [^>'\"].*: " claims/000574/*.yaml | head
```

```
(Bash completed with no output)
```

**Agent**

I've written `claims/000574/10.1126-sciadv.aav3687.yaml`, with 35 claims. The quote checker passes except for one flag, which I checked by reading and which needs no change (below). Nothing is committed.

**Text read.** I read the version of record from Europe PMC (PMC6436923), including the Methods and figure legends, and the supplement (figs. S1 to S6, tables S1 and S2). Table S1 came out garbled. I read it by column order and confirmed that reading by recomputing the medians the table prints (6.0 to 11.5 Hz and 7.8 to 10.0 Hz). The PDF page could not be opened as an image here because no PDF renderer is installed. I also read the data descriptor (Sci Data 2020) to describe the deposited data. Movie S1 was not read.

**Code.** The paper links no analysis code. The only code in the G-Node deposit (`USZ_NCH/Human_MTL_units_scalp_EEG_and_iEEG_verbal_WM`, commit `0b27b34e`) is an example MATLAB script that loads the data. So code settles no method detail.

**Counts.**
- **Claims:** 35. 34 have quotes; one (the per-subject values of table S1) has an `inferred` note instead.
- **Statistics:** 26 entries over 22 claims.
- **Criteria:** all 35 claims have one.
- **Checker flag:** the checker reports `5e-05` as not found. The paper prints "P = 5.0 × 10 −5", which is the same value in a form the checker does not recognise.

**Details the paper leaves open, and the readings named:**
- **Permutation t test, paired or unpaired:** both.
- **Number of label-scrambled repetitions:** 499 (implied by P = 0.002) or 1000 (table S2).
- **Trials for the EEG, iEEG and PLV analyses:** correct trials only, or all artifact-free trials.
- **Behavior:**
  - Percentages are the mean over sessions or trials pooled.
  - Cowan's K is taken at set size 8, as the maximum over set sizes, from pooled rates times 8, or as the mean over set sizes.
  - The 48 ms per item comes from one of four slope definitions, using mean or median RT.
  - The ANOVA's F(2, 2007) fits no stated design, so it is run two ways and reported, not judged.
- **Neurons per session:** all 36 sessions, or only sessions with units (1526 / 36 is 42, not 51).
- **Firing-rate time base, and the noise SD in the SNR:** two readings each.
- **Chi-square:** with or without Yates correction.
- **Load-dependence test:** permutation t test, or a cluster-based test.
- **Probe window:** 0 to 1 s, probe to button press, or 0 to 0.5 s.
- **Window for the peak firing rate:** two readings.
- **Time range for the IN/OUT and workload tests on probe neurons:** two readings.
- **dPCA:**
  - The z-score scale and the regularization: two readings each.
  - The retrieval window: 0 to 1 s or 0 to 2 s.
  - Fig. S3d names both dPC2 and dPC3.
  - Loadings are absolute or signed.
- **Decoding:**
  - The smoothing kernel is a boxcar or a Gaussian.
  - Neuron firing rates are z-scored before the classifier, or not.
  - Class balance is equal trials per class, or all trials.
  - "Median accuracy" can be averaged over time steps two ways.
- **Frequency range searched for EEG, PLV and spike-field coherence:** 4 to 30 Hz or 1 to 40 Hz.
- **Trials for PLV maintenance against encoding:** set size 8 or all set sizes.
- **Position of a bipolar channel:** the deepest contact or the midpoint of the two contacts.
- **SOZ comparison:** which increase (workload, or maintenance against encoding) and which channels.
- **Spike-field coherence:** the window of the spike-triggered spectrum, run at 3 and 5 cycles.

**Missing from the paper:**
- **HFO claim:** the paper names no detector, test or comparison. It cites Fedele et al. 2017 (Sci Rep 7, 13836) for the detector, and that paper is not under `paper/`.
- **Channels for the other subjects' EEG power:** the fig. S5 legend cites a "table S7" that does not exist. I used each subject's maximal-PLV electrode instead.
- **Microwire field potentials:** the data descriptor does not list them among the deposited data. If the dataset lacks them, the spike-field coherence claim is blocked for the LFP part.
- **"Little difference" in decoding with maintenance neurons only:** the paper gives no threshold, so I used the protocol's default 10% tolerance.

## End of run

30 turns, 7 minutes, result: success.
