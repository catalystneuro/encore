# gao-2018 · claims · run 42837978671

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ | grep -i gao; cat claims/fouke-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ | grep -i gao
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
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
ls paper/ | head; ls paper | wc -l; ls paper | grep -i -e gao -e 0633
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/fouke-2025.yaml | head -150; wc -l claims/fouke-2025.yaml; cat papers/datasets/gao-2018.yaml; ls claims | head -40
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
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,321p claims/fouke-2025.yaml; ls claims | grep -i -e gao -e li-20 -e economo -e inagaki
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
[... 160 more lines not kept]
```

**Agent**

Now the paper text.

**Agent calls Bash**

```bash
wc -c paper/*.txt; cat paper/10.1038-s41586-018-0633-x.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/0122b085-b824-4512-a4be-066aeccb98f2/tool-results/bz1rb7iq2.txt"
}
```

```
1	118312 paper/10.1038-s41586-018-0633-x.txt
2	DOI: 10.1038/s41586-018-0633-x
3	Version: as served by europe_pmc
4	Source: europe_pmc+crossref (paper-text-fetcher)
5	Stored: 2026-10-20
6	Extracted: as fetched; with 2 supplement file(s) from the PMC Open Access cloud data (PMC6212318), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
7	------------------------------------------------------------------------
8	Nature Nature 319 nihpa 0410462 Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC6212318 PMC6212318.1 6212318 6212318 NIHMS1504009 30333626 10.1038/s41586-018-0633-x NIHMS1504009 NIHPA1504009 1 Article A cortico-cerebellar loop for motor planning Gao Zhenyu 1 Davis Courtney 2 Thomas Alyse M. 2 Economo Michael N. 3 Abrego Amada M. 2 Svoboda Karel 3 De Zeeuw Chris I. 1 4 Li Nuo 2 3 1 Department of Neuroscience, Erasmus MC, Rotterdam, the Netherlands 2 Department of Neuroscience, Baylor College of Medicine, Houston TX 77030 3 Janelia Research Campus, Ashburn VA 20147 4 Netherlands Institute for Neuroscience, Amsterdam, the Netherlands Author Contributions N.L., K.S., C.I.D.Z., and Z.G. conceived the project. Z.G., N.L., and C.I.D.Z. performed pilot experiments. N.L., Z.G., C.D., A.M.T., and A.M.A. performed behavioral and recording experiments. Z.G. performed anatomy experiments. M.N.E. contributed brain alignment software. N.L., Z.G., K.S., and C.I.D.Z. analyzed the data. N.L., Z.G., C.I.D.Z., and K.S. wrote the manuscript with inputs from all authors. Correspondence: Nuo Li, Baylor College of Medicine, One Baylor Plaza, Houston, TX 77030, [removed: an e-mail address] 17 10 2018 11 2018 563 7729 323263 113 116 16 08 2018 17 04 2019 17 04 2019 03 11 2018 18 06 2024 Users may view, print, copy, and download text and data-mine the content in such documents, for the purposes of academic research, subject always to the full Conditions of use: http://www.nature.com/authors/editorial_policies/license.html#
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41586-018-0633-x.txt').read(); print(t[52000:85000])"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python3 -c "
t=open('paper/10.1038-s41586-018-0633-x.txt').read()
import textwrap
s=t[52000:]
open('$TMPDIR/rest.txt','w').write('\n'.join(textwrap.wrap(s,2000)))"; wc -l $TMPDIR/rest.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/rest.txt",
 "limit": 12
}
```

```
1	 experimenters were blind to conditions. Statistical comparisons using t-tests and bootstrap are described in detail in sections above. Code availability Software used for data analysis is available from the corresponding author upon reasonable request. Data availability Raw and processed data are available from the corresponding author upon reasonable request. Extended Data Extended Data Figure 1. Histology and behavioral data. a. Coronal sections showing CN lesion sites for all mice. Fastigial lesion, n=4; dentate lesion, n=4. b. Licking movement is not affected by fastigial lesion. Individual licks are shown as dots (blue, lick right; red, lick left). Licks are aligned to the onset of the ‘go’ cue (vertical line). c. Average lick rate within a lick bout and the duration of lick bouts are not affected by fastigial lesion. A lick bout is defined as a sequence of licks with inter-lick-interval less than 500 ms. Data from the fastigial-lesion mice only (n=4). Data are grouped by licking direction relative to the lesioned hemisphere: contralesional licking (blue) or ipsilesional licking (red). d. Coronal sections showing ChR2-EYFP expression in the fastigial and dentate nucleus. 9 mice were used for various fastigial ChR2 photo-activation experiments, and 10 mice were used for dentate ChR2 photo-activation experiments. In 1 of the fastigial photo-activation mice, the injection of ChR2 virus missed the CN (not shown) and its data were excluded. 2 of the dentate photo-activation mice were subsequently used for lesion experiments (not shown). See Supplemental Table 1 for the list of mice and manipulated hemispheres in individual experiments. e. CN photo-activation during specific behavioral epochs. Top , experiment timeline. Photostimulation was for the entire task epoch (1.3 s). Bottom , behavioral performance. Left , fastigial photo-activation (n=6); right , dentate photo-activation (n=8). For fastigial photo-activation, average behavioral performance for control and
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n -o -E "(Figure [1-4]\. |Supplementary|SUPPLEMENT|Supplemental Table|=====|----- )" rest.txt | sort | uniq -c | head -40; grep -n -b -o -E "Figure 1\. " rest.txt
```

```
1 11:Supplementary
      1 16:Figure 1. 
      1 17:Figure 2. 
      1 17:Figure 3. 
      2 17:Supplemental Table
      1 18:Figure 4. 
      1 1:Figure 1. 
      1 1:Supplemental Table
      1 27:Supplemental Table
      1 2:Figure 2. 
      1 2:Supplemental Table
      2 33:Supplemental Table
      1 4:Figure 3. 
      1 4:Supplemental Table
      1 5:Figure 4. 
1:392:Figure 1. 
16:30537:Figure 1.
Shell cwd was reset to
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/rest.txt",
 "offset": 16,
 "limit": 17
}
```

```
16	reference atlas: A digital color brain atlas of the C57Bl/6J male mouse ( John Wiley & Sons Inc , 2008 ). 38 Oh SW A mesoscale connectome of the mouse brain. Nature 508 , 207 – 214 ( 2014 ). 24695228 10.1038/nature13186 PMC5102064 39 Rueckert D Nonrigid registration using free-form deformations: application to breast MR images. IEEE Trans Med Imaging 18 , 712 – 721 , 10.1109/42.796284 ( 1999 ). 10534053 Figure 1. Cerebellar involvement in motor planning and movement initiation. a. Mouse reporting the location of a pole by directional licking. b. ALM-cerebellar loop. c. Fastigial or dentate lesion. Bottom , example lesion. d. Behavioral performance (session mean ± s.e.m., n=75–256 trials). Mouse 1–2, left fastigial lesion; mouse 3–4, right fastigial; mouse 5, left dentate; mouse 6–8, right dentate. “Lick left” and “lick right” trials are grouped by instructed licking direction relative to the lesioned hemisphere. Blue, contralesional; red, ipsilesional. ***, p<0.001, one-sided test, pre- versus post lesion, bootstrap (Methods). e. Top , lick rate during contra- and ipsilesional licking bouts after fastigial lesion. Lick times are aligned to the first lick (t=0). Bottom , time of the first lick to the contra- and ipsilesional direction after the ‘go’ cue onset. Lines, individual mice (n=4). ***, p<0.001, one-sided test, bootstrap. f. Fastigial or dentate photo-activation. Laser power, 0.5–1.5 mW. Bottom , example ChR2 expression. g. Fastigial or dentate photo-activation during the delay epoch. Behavioral performance. “Lick left” and “lick right” trials are pooled. Chance is 50% (dashed line). Lines, individual mice (fastigial, n=6; dentate, n=8). Bars, mean. ***, p<0.001, one-sided test, bootstrap. h. Fastigial photo-activation during specific epochs. Behavioral performance for each trial type. “Lick left” and “lick right” trials are grouped by instructed licking direction relative to the manipulated hemisphere. Blue, contralateral; red, ipsilateral. Both hemispher
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rl "000007" --include=*.yaml --include=*.md --include=*.json . 2>/dev/null | grep -v transcripts | head; ls paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat papers/match/000007.yaml; python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
it=d if isinstance(d,list) else d.get('dandisets',d)
for x in (it if isinstance(it,list) else it.values()):
  if '000007' in json.dumps(x)[:200]: print(json.dumps(x,indent=1)[:3000])
"
```

```
# Whether each paper DANDI:000007 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: dandi
  id: '000007'
date: '2026-11-10'
papers:
- doi: 10.1038/s41586-018-0633-x
  relation: IsDescribedBy
  checks:
    text: true
    title_in_text: true
    names_this: false
    names_others: []
  verdict: primary
  by: checks
  reason: The archive says the paper describes the dataset, and the paper names no dataset.
```

**Agent calls Bash**

```bash
grep -n -A15 '"000007"' targets/dandisets.json | head -40
```

```
126:   "dandiset": "000007",
127-   "name": "A cortico-cerebellar loop for motor planning",
128-   "published_version": "0.220126.1903",
129-   "asset_count": 54,
130-   "size_gb": 0.2,
131-   "data_standards": [
132-    "Neurodata Without Borders (NWB)"
133-   ],
134-   "species": [
135-    "House mouse"
136-   ],
137-   "approaches": [
138-    "electrophysiological approach"
139-   ],
140-   "papers": [
141-    {
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000007/versions/0.220126.1903/ | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('name'));print(d.get('description'));print(d.get('assetsSummary'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
head -40 claims/gao-2026.yaml; grep -l "claude-opus-5-5" claims/*.yaml | head -3
```

```
# Claims for Gao, Frake, Durand and He (2026), "Transcranial Focused Ultrasound Stimulation
# Targeting White Matter Inhibits Seizures in a Rat Model of Epilepsy", IEEE Trans Neural Syst
# Rehabil Eng 34, doi:10.1109/tnsre.2025.3644273, on dandiset 001683 (same title on the archive;
# its description says the dataset is described in this paper).
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-21,
# protocol as stated in docs/protocol.md (version pilot-10).
#
# Text read: the NIH author manuscript (PMC12848950) as served by Europe PMC, stored under paper/:
# abstract, Introduction, Methods, Results, Discussion, Data Availability and the legends of Figs. 1
# to 6; and the supplement (supp1-3644273.pdf, 8 pages: ex-vivo scanning, target confirmation, Figs.
# S1 to S7). There is no PDF of the main paper, so values and significance marks drawn only inside
# Figs. 2 to 6 were not read; Figs. S4, S5 and S7 were viewed in the supplement PDF. The paper links
# no code; the only repository it names is the dandiset. No code was read.
#
# Data the paper used, as it reports them (Methods A to E, supplement):
#  - Rats. 16 adult male Sprague-Dawley rats in the epilepsy study, 10 tFUS (experimental) and 6
#    sham; 7 more in a mechanism study, 23 in all. The wild-type analysis (Fig. 5) uses all 23
#    (Fig. 5B, N = 23 per group). Isoflurane anesthesia throughout.
#  - Recordings. A 32-channel skull EEG probe (NeuroNexus HC32), aligned with bregma, and a
#    64-channel intracranial array in left S1 (AP -2, ML -2.5, DV -1.5 mm). Tucker-Davis system at
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,60p tools/claims_check.py; grep -n "kind" docs/*.md | head -20
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

[... 55 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s,indent=1)[:6000])"
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
import json;s=json.load(open('schemas/claims.schema.json'))
print(json.dumps(s['\$defs'],indent=1)[:5000]); print([k for k in s['properties']])"; grep -n "^[a-z_]*:" claims/alasfour-2024.yaml | head
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
[... 87 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/gao-2018.yaml",
 "content": "# Claims for Gao, Davis, Thomas, Economo, Abrego, Svoboda, De Zeeuw and Li (2018), \"A\n# cortico-cerebellar loop for motor planning\", Nature 563, 113-116, doi:10.1038/s41586-018-0633-x,\n# tested on DANDI:000007 (same title on the archive; its description reads \"Extracellular recording\n# in ALM\").\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol as stated in docs/protocol.md (version pilot-14).\n#\n# Text read: the NIH author manuscript (PMC6212318, NIHMS1504009) as served by Europe PMC, stored\n# under paper/: main text, Methods, the legends of Figs. 1 to 4 and Extended Data Figs. 1 to 10;\n# supplement 1 (Supplementary Information, 5 pages: Extended Data Fig. 10 discussion, cerebellar\n# circuitry discussion, Supplemental Table 1 listing mice and hemispheres) and supplement 2 (the\n# Nature reporting summary). There is no PDF of the main paper, so values and significance marks\n# drawn only inside the figures could not be read; claims rest on the text and legends.\n# Code: the paper links none. Its Code availability says \"Software used for data analysis is\n# available from the corresponding author upon reasonable request\"; the reporting summary says\n# scripts \"will be deposited on CRCNS.org\" but gives no identifier. No code was read, so every\n# method detail below is from the Methods, legends or supplement, or is named as open.\n#\n# Data the paper used, as it reports them (Methods; Supplemental Table 1):\n#  - Task. Head-fixed mice report the location of a pole (anterior or posterior) by licking left or\n#    right. Sample epoch 1.3 s (pole movement onset to 0.1 s after retraction onset), delay epoch\n#    1.3 s, auditory go cue (3.4 kHz, 0.1 s), then the response. Lick early trials (alarm, timeout)\n#    and no-lick trials (no lick within 1.5 s of the go cue) are excluded from performance.\n#    Reaction time is from go cue onset to the first lickport contact.\n#  - Mice. 70 in all (Supplemental Table 1). ALM recordings: 1309 single units in 10 mice over 39\n#    sessions during behavior with CN ChR2 photo-activation (Fig. 2, Fig. 4); 1194 putative\n#    pyramidal (trough-to-peak spike width > 0.45 ms), 82 fast-spiking (< 0.35 ms), 33\n#    intermediate excluded. 9 of these 10 mice received CN photo-activation during the recordings\n#    (912 pyramidal neurons; 446 with fastigial, 466 with dentate photo-activation, Fig. 4f, 4g);\n#    one mouse was excluded because the virus missed the CN. Supplemental Table 1 lists 6 mice\n#    for fastigial (CD06, NL15, AN105, AN107, AN108, AN109) and 3 for dentate (NL12, NL14, AN106)\n#    photo-activation during ALM recording. ALM recordings during CN photo-inhibition in L7-cre x\n#    Ai32 mice: 490 units in 4 mice (CD08, CD12, CD13, CD14) over 19 sessions, 454 pyramidal.\n#    The Methods say recordings were from left ALM in 10 mice and right ALM in 2; the table lists\n#    13 ALM-recorded mice, 2 of them in right ALM (AN107, CD14). ALM was always recorded\n#    contralateral to the manipulated CN.\n#  - CN recordings: 878 units in 18 mice over 169 sessions (10 wild-type, 8 VGAT-ChR2-EYFP with\n#    ALM photo-inhibition); 268 fastigial, 139 interposed, 157 dentate, 314 outside the CN. The\n#    dandiset description names ALM recordings only; the CN claims are kept, as the paper's\n#    findings, for the author to find whether the data are there.\n#  - Photostimuli. CN photo-activation (AAV ChR2): 5 ms pulses at 20 Hz, average 0.5, 1 or 1.5 mW,\n#    from the start of an epoch for 0.455 s (10 pulses) or 1.255 s (26 pulses), on 25% of\n#    behavioral trials and 33% during ALM recordings. CN photo-inhibition (Purkinje cell ChR2): 40\n#    Hz sinusoid, 0.5, 1.5 or 4.5 mW, 0.5 or 1.3 s with a 100 to 200 ms offset ramp; during ALM\n#    recordings it starts at delay onset and lasts 1.3 s (1.5 or 4.5 mW). ALM photo-inhibition\n#    (VGAT-ChR2): bilateral, 1.3 s from delay onset, 1.5 mW per site.\n#  - Measured variables. Spike times of sorted units, trial events (pole, go cue, licks),\n#    instructed trial type, lick direction and outcome, photostimulation condition.\n#\n# Shared methods, cited by the criteria below.\n#  B1 Behavioral performance (Methods, Behavioral data analysis). Fraction of correct choices,\n#     excluding lick early and no lick trials; also computed separately for \"lick left\" and\n#     \"lick right\" trials, grouped by instructed direction relative to the manipulated hemisphere.\n#     Significance by a hierarchical bootstrap, resampling with replacement mice, then sessions\n#     of each mouse, then trials of each session, 10,000 times; the one-tailed p-value is the\n#     fraction of resamples whose performance change has the sign opposite to the observed one.\n#  E1 Units (Methods, Electrophysiology data analysis). ALM analyses use putative pyramidal\n#     neurons (spike width > 0.45 ms); CN units are not classified by spike shape.\n#  E2 Trial-type selectivity. A two-tailed t-test (p < 0.05) on spike counts of \"lick left\"\n#     against \"lick right\" trials in the sample, delay or response epoch; selective when any\n#     epoch is significant. The response epoch's window is not given (open; readings (a) 1.3 s\n#     from go cue onset, the length of the other epochs and of the response epoch photostimulus;\n#     (b) 0 to 1.5 s after the go cue, the answer window). Which trials form \"lick left\" and\n#     \"lick right\" here is not stated (open; readings (a) correct trials, as in the example\n#     neurons of Fig. 2a; (b) all trials with a lick, grouped by instructed direction).\n#  E3 Population selectivity (Methods; Fig. 2c legend). Each neuron's preferred trial type is\n#     fixed from a subset of trials (10 for ALM, 20 for CN) and selectivity is the spike rate\n#     difference between preferred and non-preferred trial types on the remaining trials,\n#     averaged over neurons with mean and s.e.m. by bootstrap over neurons; averaging window 200\n#     ms. Whether the subset is 10 trials in all or per trial type, and which epoch fixes the\n#     preference, are open; the paper says the epoch choice gave qualitatively similar results.\n#     For photostimulation effects, all trials (correct and incorrect) grouped by instructed type\n#     are used, and only selective neurons tested on > 3 trials in all conditions.\n#  E4 Photostimulation effect on a neuron (Methods). \"Lick left\" and \"lick right\" trials pooled;\n#     two-tailed t-test on spike counts, control against photostimulation trials, at p < 0.01, in\n#     the whole delay epoch (Fig. 3, Extended Data Fig. 5) or in 400 ms bins in 50 ms steps (Fig.\n#     4f). Whether correct trials only or all trials enter is not stated (open; readings all\n#     trials and correct trials only).\n#  E5 Latency (Extended Data Fig. 9a legend). Among significantly modulated neurons, firing rate\n#     change (photostimulation minus control) with the sign flipped for suppressed neurons, in 10\n#     ms bins in 1 ms steps; onset is the first bin where the population change differs from 0 by\n#     a two-tailed t-test at p < 0.01; neurons resampled with replacement 10,000 times and the\n#     mean onset reported. The window that decides \"significantly modulated\" for this analysis is\n#     not given (open; readings (a) the photostimulation period, (b) the whole delay epoch).\n#  E6 Coding direction (Methods, Analysis of ALM population dynamics). Sessions with > 5\n#     simultaneously recorded neurons and > 5 trials per condition (28 of 39). Spike counts in\n#     400 ms windows in 10 ms steps; cd_t is the mean \"lick right\" minus mean \"lick left\" response\n#     vector, averaged over the delay epoch to one cd, from correct control trials only. Projections\n#     cd'x use control and photostimulation trials independent of those that estimated the cd,\n#     correct and incorrect, grouped by instructed type; each session is offset by its mean\n#     projection over all trials and times (from the cd-estimating trials); s.e.m. by bootstrap\n#     over sessions. How trials are split into the cd-estimating and the independent sets is not\n#     given; a random half split of control trials is used, a standard choice.\nschema_version: 2\npaper: doi:10.1038/s41586-018-0633-x\nclaims:\n- id: fig1d-fastigial-lesion-contra-choice\n  statement: Fastigial nucleus lesions impair contralesional licking choices, measured as lower\n    performance on trials instructing contralesional licking after the lesion than before.\n  source: Results, paragraph 2; Figure 1d\n  quote: Fastigial lesions impaired initiation of contralesional licking ( Fig 1d )\n  statistics:\n  - test: one-sided bootstrap, pre- versus post lesion\n    p: 0.001\n    p_relation: \"<\"\n    n: 4 fastigial lesion mice\n  criterion: Performance as in B1 for contralesional and ipsilesional trials, before against\n    after the lesion, in the 4 fastigial lesion mice (Supplemental Table 1). Reproduced when the\n    contralesional performance drops after the lesion with a hierarchical bootstrap p < 0.001\n    (one-sided, B1). The legend marks significance per mouse and session means (n = 75 to 256\n    trials); the per-mouse drops are reported as well.\n- id: fig1e-fastigial-lesion-slow-initiation\n  statement: After fastigial lesion, the first lick to the contralesional side comes later after\n    the go cue than the first lick to the ipsilesional side, while lick rate within bouts is\n    unchanged.\n  source: Results, paragraph 2; Figure 1e; Extended Data Figure 1b and 1c\n  quote: slowed initiation of contralesional licking following the 'go' cue ( Fig 1e ). After\n    movement initiation licking was unaffected\n  statistics:\n  - about: time of first lick, contralesional against ipsilesional\n    test: one-sided bootstrap\n    p: 0.001\n    p_relation: \"<\"\n    n: 4 fastigial lesion mice\n  criterion: Time of the first lick after go cue onset (Methods, reaction time), per trial,\n    contralesional against ipsilesional licking, in the fastigial lesion mice after the lesion;\n    one-sided hierarchical bootstrap as in B1. Reproduced when contralesional first licks are\n    later at p < 0.001. For the second part, a lick bout is a sequence of licks with\n    inter-lick intervals under 500 ms (Extended Data Fig. 1c legend); lick rate within bouts and\n    bout duration are compared between contra- and ipsilesional bouts. The paper reports no test\n    for this absence; the bootstrap of B1 (two-sided at p < 0.05) is used and named as a choice.\n- id: fig1d-dentate-lesion-no-effect\n  statement: Dentate nucleus lesions do not change behavioral choice or movement execution.\n  source: Results, paragraph 2; Figure 1d\n  quote: Dentate lesions (~1.5 mm away) did not change behavioral choice and movement execution\n  criterion: A claim of absence. Performance as in B1 for contralesional and ipsilesional trials,\n    pre against post lesion, in the 4 dentate lesion mice, tested with the one-sided bootstrap of\n    B1 at p < 0.05 (the paper's lowest marked threshold). Reproduced when neither trial type\n    changes significantly; the size of each change is reported.\n- id: fig1g-fastigial-activation-early-sample-no-effect\n  statement: Fastigial photo-activation during the early sample epoch does not affect behavioral\n    choice for either trial type.\n  source: Results, paragraph 3\n  quote: Fastigial photo-activation during the early sample epoch had no effect on behavioral\n    choice (p>0.05 for either trial type, bootstrap, Methods)\n  statistics:\n  - test: bootstrap\n    p: 0.05\n    p_relation: \">\"\n    n: 6 mice\n  criterion: A claim of absence, judged on the paper's test. Performance per trial type (B1) in\n    control against early sample photo-activation trials (0.455 s from sample onset), one-sided\n    bootstrap of B1; reproduced when p > 0.05 for both trial types.\n- id: fig1g-fastigial-activation-delay-errors\n  statement: Fastigial photo-activation during the early delay epoch lowers behavioral\n    performance, even though the photostimulus ends 800 ms before the movement.\n  source: Results, paragraph 3; Figure 1g\n  quote: Photo-activation during the delay and response epochs both resulted in incorrect choices\n    ( Fig 1g–h ). Incorrect choices were induced even when the photostimuli ceased 800 ms before\n    the movement\n  statistics:\n  - test: one-sided bootstrap\n    p: 0.001\n    p_relation: \"<\"\n    n: 6 mice\n  criterion: Performance with \"lick left\" and \"lick right\" trials pooled (B1), control against\n    early delay photo-activation (0.455 s from delay onset) in the 6 mice of Supplemental Table\n    1. Reproduced when performance drops with a one-sided bootstrap p < 0.001.\n- id: fig1h-fastigial-activation-delay-bias\n  statement: Fastigial photo-activation during the delay epoch biases future movements toward\n    either the contralateral or the ipsilateral direction, depending on the mouse.\n  source: Results, paragraph 3; Figure 1h; Extended Data Figure 1e\n  quote: Photo-activation during the delay epoch biased future movements to either the\n    contralateral or ipsilateral direction in individual mice\n  criterion: Per mouse, the change in performance with delay photo-activation for contralateral\n    and ipsilateral trials (B1). Reproduced when at least one mouse shows a larger drop on\n    contralateral trials and at least one a larger drop on ipsilateral trials, each with a\n    one-sided bootstrap (B1, trials and sessions of that mouse) p < 0.05.\n- id: fig1h-fastigial-activation-response-contra-bias\n  statement: Fastigial photo-activation during the response epoch produces a contralateral bias,\n    opposite to the bias of fastigial lesions.\n  source: Results, paragraph 3; Figure 1h\n  quote: Photo-activation immediately before movement onset (response epoch) produced a\n    contralateral bias ( Fig 1h ), opposite from the directional bias induced by fastigial\n    lesions\n  statistics:\n  - test: one-sided bootstrap\n    p: 0.05\n    p_relation: \"<\"\n    n: 6 mice\n  criterion: Response epoch photo-activation (1.255 s from go cue onset) in the 6 mice of the\n    1.3 s experiment. A contralateral bias is lower performance on ipsilateral trials (more\n    contralateral licks) with contralateral performance not lowered. Reproduced when the\n    ipsilateral performance drops with a one-sided bootstrap p < 0.05 (B1) and the contralateral\n    drop, if any, is smaller and not significant. The legend gives p < 0.05 and p < 0.001 marks\n    without the figure to say which bar carries which; the weaker bound is used.\n- id: fig1i-fastigial-activation-licking-unaffected\n  statement: Fastigial photo-activation does not block or change the frequency and duration of\n    licking after a lick bout starts, and photo-activation in the delay does not evoke early\n    licks.\n  source: Results, paragraph 3; Figure 1i; Extended Data Figure 1f\n  quote: Fastigial photo-activation did not block or perturb the frequency and duration of licking\n    movements after initiation of licking bouts ( Fig 1i ). Fastigial photo-activation during the\n    delay epoch did not evoke early licks\n  criterion: A claim of absence; the paper reports no test. Lick rate within bouts and bout\n    duration (bouts as in Extended Data Fig. 1c, inter-lick interval < 500 ms) in control against\n    response epoch photo-activation trials, and the early lick rate in control against delay\n    photo-activation trials, per mouse (n = 6). The bootstrap of B1, two-sided at p < 0.05, is\n    used and named as a choice; reproduced when none of the three differs. Sizes are reported.\n- id: fig1g-dentate-activation-little-effect\n  statement: Dentate photo-activation produces little effect on behavioral choice.\n  source: Results, paragraph 3; Figure 1g\n  quote: Dentate photo-activation produced little effect on behavioral choice ( Fig 1g , p=0.06,\n    bootstrap\n  statistics:\n  - test: bootstrap\n    p: 0.06\n    n: 8 mice\n  expected:\n  - quantity: bootstrap p-value, performance change with early delay dentate photo-activation\n    value: 0.06\n    tolerance: 0.006\n  criterion: Pooled performance (B1), control against early delay dentate photo-activation, in\n    the 8 dentate mice. A claim of absence judged on the paper's test, the one-sided bootstrap\n    of B1 at p < 0.05; reproduced when it does not find a drop. The p-value and the size of the\n    change are reported; a bootstrap p-value varies with the resampling, so the expected value\n    is a guide and not the test.\n- id: fig1j-photoinhibition-silences-fastigial\n  statement: Photostimulating Purkinje cells in L7-cre x Ai32 mice silences fastigial nucleus\n    neurons, while photostimulation over the inferior colliculus does not.\n  source: Figure 1j; Extended Data Figure 2c and 2d; Methods, CN photo-inhibition\n  quote: Photostimulation of the cerebellar cortex silenced fastigial activity whereas\n    photostimulation of the inferior colliculus did not\n  criterion: Fastigial units (n = 26, 2 mice, non-behaving), spike rate in the 500 ms before\n    against the 1.2 s during photo-inhibition (Extended Data Fig. 2d). Reproduced when most\n    fastigial units decrease with a two-tailed t-test at p < 0.01 under cerebellar cortex\n    photostimulation and few or none do under inferior colliculus photostimulation.\n- id: fig1k-inhibition-early-sample-no-effect\n  statement: Fastigial photo-inhibition during the early sample epoch does not affect behavioral\n    choice.\n  source: Results, paragraph 4; Figure 1k\n  quote: Photo-inhibition during the early sample epoch did not affect behavioral choice ( Fig 1k ,\n    p>0.05 for either trial type, bootstrap, Methods)\n  statistics:\n  - test: bootstrap\n    p: 0.05\n    p_relation: \">\"\n    n: 7 mice\n  criterion: A claim of absence, judged on the paper's test. Performance per trial type (B1),\n    control against 0.5 s early sample photo-inhibition, 7 mice; reproduced when the one-sided\n    bootstrap of B1 gives p > 0.05 for both trial types.\n- id: fig1k-inhibition-late-sample-delay-errors\n  statement: Fastigial photo-inhibition during the late sample and the delay epochs causes\n    incorrect choices, with a larger effect in the delay epoch.\n  source: Results, paragraph 4; Figure 1k; Extended Data Figure 2g and 2h\n  quote: Photo-inhibition during the late sample and delay epochs resulted in incorrect behavioral\n    choices, with a larger effect induced in the delay epoch\n  statistics:\n  - about: sub-epoch photo-inhibition, the weaker effect marked\n    test: one-sided bootstrap\n    p: 0.04\n    n: 7 mice\n  - about: sub-epoch photo-inhibition, the stronger effect marked\n    test: one-sided bootstrap\n    p: 0.0002\n    n: 7 mice\n  criterion: Performance (B1) in control against 0.5 s photo-inhibition in the early sample, late\n    sample, early delay and late delay sub-epochs (Extended Data Fig. 2h, 7 mice). Reproduced\n    when late sample and at least one delay sub-epoch lower performance with one-sided bootstrap\n    p < 0.05, and the larger of the delay drops exceeds the late sample drop. The legend gives\n    p = 0.04 and p = 0.0002 without naming which panel bar carries which; both are reported.\n- id: fig1k-inhibition-delay-bias\n  statement: Fastigial photo-inhibition during the delay epoch biases future movements to the\n    contralateral or the ipsilateral direction, depending on the mouse.\n  source: Results, paragraph 4; Extended Data Figure 2g and 2h\n  quote: Photo-inhibition during the delay epoch biased future movements to either the\n    contralateral or ipsilateral direction in individual mice\n  criterion: As fig1h-fastigial-activation-delay-bias, on the delay photo-inhibition trials of\n    the 7 L7-cre x Ai32 mice.\n- id: fig1k-inhibition-response-ipsi-bias\n  statement: Fastigial photo-inhibition during the response epoch produces an ipsilateral bias,\n    as fastigial lesions do and opposite to photo-activation.\n  source: Results, paragraph 4; Figure 1k\n  quote: Photo-inhibition during movement initiation (response epoch) produced an ipsilateral\n    bias ( Fig 1k ), consistent with fastigial lesions, and opposite from the bias induced by\n    fastigial photo-activation\n  criterion: Response epoch photo-inhibition (1.3 s from go cue onset) in the 3 mice of the 1.3 s\n    experiment. An ipsilateral bias is lower performance on contralateral trials with\n    ipsilateral performance not lowered. Reproduced when the contralateral drop has a one-sided\n    bootstrap p < 0.05 (B1) and the ipsilateral drop, if any, is smaller and not significant.\n- id: fig1l-inhibition-execution-unaffected\n  statement: Fastigial photo-inhibition minimally affects movement execution, and at the\n    intensities of the task evokes no consistent movement.\n  source: Results, paragraph 4; Figure 1l; Extended Data Figure 2e, 2f and 2i; Methods, CN\n    photo-inhibition and effects on movement\n  quote: Photo-inhibition minimally affected movement execution ( Fig 1l ). No other movements\n    were consistently evoked during photo-inhibition\n  criterion: A claim of absence; the paper reports no test. Lick rate within bouts in control\n    against response epoch photo-inhibition trials (3 mice), and early lick rate in control\n    against delay photo-inhibition trials (7 mice), with the bootstrap of B1, two-sided at p <\n    0.05, named as a choice. The video scoring and jaw tracking of Extended Data Fig. 2e and 2f\n    come from 6 other mice not in Supplemental Table 1 and are reported as not tested when the\n    dataset lacks them.\n- id: ed10-vgat-fastigial-perturbation-performance\n  statement: In VGAT-ChR2-EYFP mice, fastigial photostimulation in the early delay reduces\n    performance on both trial types (contra lick 74.5% to 58.5%, ipsi lick 67.8% to 57.0%).\n  source: Methods, ALM photo-inhibition after a fastigial perturbation, paragraph 2\n  quote: fastigial perturbations during the early delay epoch reduced behavioral performance for\n    both trial types (control ... 74.5% correct, \"ipsi lick\" trials, 67.8%; photostimulation ...\n    58.5% and 57.0%; p<0.05 for both trial types, bootstrap)\n  statistics:\n  - test: bootstrap\n    p: 0.05\n    p_relation: \"<\"\n    n: 4 VGAT-ChR2-EYFP mice\n  expected:\n  - quantity: control performance, contra lick trials\n    value: 74.5\n    tolerance: 7.45\n    unit: \"%\"\n  - quantity: control performance, ipsi lick trials\n    value: 67.8\n    tolerance: 6.78\n    unit: \"%\"\n  - quantity: fastigial perturbation performance, contra lick trials\n    value: 58.5\n    tolerance: 5.85\n    unit: \"%\"\n  - quantity: fastigial perturbation performance, ipsi lick trials\n    value: 57.0\n    tolerance: 5.7\n    unit: \"%\"\n  criterion: Performance per trial type (B1) on fastigial-only trials (40 Hz, 1.5 mW, 500 ms from\n    delay onset) against control trials. Whether the percentages are pooled over trials or\n    averaged over mice is not stated (open; readings (a) pooled over all trials, (b) mean of\n    per-mouse values). Reproduced when under one reading all four values are within tolerance\n    and both drops have one-sided bootstrap p < 0.05.\n- id: fig2-alm-selective-fraction\n  statement: Most ALM putative pyramidal neurons (980 of 1194) distinguish \"lick left\" from\n    \"lick right\" trials in their spike counts.\n  source: Results, paragraph 5; Methods, Electrophysiology data analysis\n  quote: Most ALM pyramidal neurons distinguished \"lick left\" and \"lick right\" trials in spike\n    counts (980/1194, p<0.05, two-tailed t-test, Methods)\n  expected:\n  - quantity: ALM putative pyramidal neurons\n    value: 1194\n    tolerance: 119.4\n  - quantity: selective ALM pyramidal neurons\n    value: 980\n    tolerance: 98\n  - quantity: fraction selective\n    value: 0.82\n    tolerance: 0.082\n  criterion: Units as E1, selectivity test as E2. The counts rest on the 39 sessions of 10 mice;\n    if the dataset holds fewer, the fraction is judged and the counts are reported. Reproduced\n    when, under one of the readings of E2 (response window (a) or (b), trials (a) or (b)), the\n    fraction is within tolerance; where the dataset holds all units, the counts must be as well.\n- id: fig2-cn-selective-fraction\n  statement: A proportion of CN neurons similar to ALM (416 of 564) shows trial-type selectivity.\n  source: Results, paragraph 5\n  quote: A similar proportion of CN neurons showed trial-type selectivity (416/564)\n  expected:\n  - quantity: CN neurons\n    value: 564\n    tolerance: 56.4\n  - quantity: selective CN neurons\n    value: 416\n    tolerance: 41.6\n  - quantity: fraction selective\n    value: 0.74\n    tolerance: 0.074\n  criterion: CN units are those located in the fastigial, interposed or dentate nucleus (268 +\n    139 + 157 = 564; Methods). Selectivity as E2. Reproduced when under one reading of E2 the\n    fraction is within tolerance.\n- id: fig2-preparatory-more-in-alm\n  statement: Preparatory activity (selectivity before the response epoch) is more prevalent in ALM\n    (59% of neurons) than in the CN (35%).\n  source: Results, paragraph 5\n  quote: Preparatory activity (selectivity before the response epoch) was more prevalent in ALM\n    (ALM, 59% of neurons, CN, 35%; p<0.001, chi-square test)\n  statistics:\n  - test: chi-square test\n    p: 0.001\n    p_relation: \"<\"\n    n: 1194 ALM and 564 CN neurons\n  expected:\n  - quantity: fraction of ALM neurons with preparatory activity\n    value: 0.59\n    tolerance: 0.059\n  - quantity: fraction of CN neurons with preparatory activity\n    value: 0.35\n    tolerance: 0.035\n  criterion: A neuron has preparatory activity when the E2 test is significant in the sample or\n    the delay epoch. The denominator is open (readings (a) all neurons, 1194 and 564; (b) the\n    selective neurons, 980 and 416). Trials as the readings of E2. Reproduced when under one\n    reading both fractions are within tolerance and a chi-square test of the two proportions has\n    p < 0.001 with ALM higher.\n- id: fig2-peri-movement-equal\n  statement: Peri-movement activity (selectivity in the response epoch) is equally prevalent in\n    ALM (67%) and the CN (66%).\n  source: Results, paragraph 5\n  quote: Peri-movement activity (selectivity during response epoch) was equally prevalent in both\n    regions (ALM, 67%, CN, 66%)\n  expected:\n  - quantity: fraction of ALM neurons with peri-movement selectivity\n    value: 0.67\n    tolerance: 0.067\n  - quantity: fraction of CN neurons with peri-movement selectivity\n    value: 0.66\n    tolerance: 0.066\n  criterion: A neuron has peri-movement activity when the E2 test is significant in the response\n    epoch, under the response window readings of E2. Denominator as in\n    fig2-preparatory-more-in-alm (open, same readings). Reproduced when under one reading both\n    fractions are within tolerance; a chi-square test of the two proportions is reported (the\n    paper gives none).\n- id: ed4-lick-modulated-few\n  statement: In both ALM and the CN, a similar small proportion of neurons (under 10%) modulates\n    its spike rate during individual licks.\n  source: Results, paragraph 5; Extended Data Figure 4a to 4c\n  quote: In both regions, a similar proportion (<10%) of neurons modulated their spike rates\n    during individual licks\n  expected:\n  - quantity: upper bound on the fraction of lick-modulated neurons, ALM and each CN nucleus\n    value: 0.1\n    tolerance: 0.01\n  criterion: As Extended Data Fig. 4a, for each lick, spike counts in two adjacent 50 ms windows\n    starting 20 ms from the lick detection time; across all licks and trials, a two-tailed t-test\n    between the two windows at p < 0.01 marks a neuron as lick-modulated. Whether the test is\n    paired across licks is not stated (open; readings paired and unpaired). Reproduced when under\n    one reading the fraction in ALM and in each CN nucleus is below 0.11.\n- id: fig2cd-selectivity-emerges-gradually\n  statement: Selectivity for \"lick left\" and \"lick right\" trials emerges gradually in both the\n    ALM and the CN population averages, starting during the sample epoch and peaking in the\n    response epoch.\n  source: Results, paragraph 6; Figure 2c and 2d\n  quote: Selectivity for \"lick left\" and \"lick right\" trials emerged gradually in both ALM and CN\n    population averages ( Fig 2c–d ), starting during the sample epoch and reaching a maximum at\n    the response epoch\n  criterion: Population selectivity as E3 in 200 ms windows over the selective neurons (ALM n =\n    980, CN n = 197 as the Fig. 2d legend gives; why 197 and not 416 is not said, so CN is run on\n    the selective neurons under both readings, (a) all 416 selective, (b) those with significant\n    sample or delay selectivity). Reproduced in a region when the bootstrap 95% interval over\n    neurons excludes zero in at least one window of the sample epoch, the mean over the delay\n    epoch exceeds the mean over the sample epoch, and the maximum of the time course lies in the\n    response epoch.\n- id: ed4e-cn-predicts-movement\n  statement: Most CN neurons with delay selectivity predict the upcoming licking direction, not\n    object location (67%), switching their preference on error trials.\n  source: Results, paragraph 6; Extended Data Figure 4e\n  quote: However, most CN neurons predicted the upcoming licking direction (67%, Extended Data Fig\n    4 ), similar to ALM\n  expected:\n  quantity: fraction of CN neurons with a negative error-to-correct selectivity ratio\n    value: 0.67\n    tolerance: 0.067\n  criterion: CN neurons with significant delay selectivity (E2) tested on > 3 error trials (n = 73\n    in the paper). For each, the ratio of delay selectivity (spike rate difference by instructed\n    trial type) on error trials to that on correct trials; a negative ratio means the neuron\n    follows the movement. Reproduced when the fraction with a negative ratio is within\n    tolerance.\n- id: ed4g-fastigial-contra-late-delay\n  statement: In the fastigial nucleus, equal numbers of neurons prefer contralateral and\n    ipsilateral movement in the early delay, and a population preference for contralateral\n    movement develops just before movement initiation.\n  source: Results, paragraph 7; Extended Data Figure 4g\n  quote: equal numbers of neurons preferred either contralateral or ipsilateral movement during the\n    early delay, and a population-level preference for contralateral movement developed right\n    before movement initiation\n  statistics:\n  - test: one-sided bootstrap\n    p: 0.0001\n    n: 15 mice (fastigial)\n  criterion: Per neuron, the preferred direction from spike counts in the first 500 ms and in the\n    last 500 ms of the delay, among neurons selective in that window (E2 test on that window, as\n    the legend implies; open whether selectivity is from that window or from E2 over epochs, both\n    run). Reproduced when the contra-preferring fraction in the last 500 ms exceeds one half with\n    a one-sided bootstrap over mice (B1 resampling scheme) p < 0.001 and the first 500 ms\n    fraction does not differ from one half at p < 0.05.\n- id: fig3-cn-altered-by-alm-inhibition\n  statement: Bilateral ALM photo-inhibition during the delay rapidly alters the activity of many\n    CN neurons (185 of 389), with a latency of 10.7 plus or minus 4.0 ms.\n  source: Results, paragraph 8; Figure 3a and 3b; Extended Data Figure 5a\n  quote: Activity of many CN neurons was rapidly altered by ALM photo-inhibition (185/389, p<0.01,\n    two-tailed t-test; latency, 10.7 ± 4.0 ms, mean ± s.e.m.)\n  expected:\n  - quantity: CN neurons recorded during ALM photo-inhibition\n    value: 389\n    tolerance: 38.9\n  - quantity: CN neurons significantly modulated\n    value: 185\n    tolerance: 18.5\n  - quantity: latency\n    value: 10.7\n    tolerance: 4.0\n    unit: ms\n  criterion: Modulated as E4 on the whole delay epoch; latency as E5 (both readings). Reproduced\n    when under one reading of E4 and E5 the count (or the fraction 0.48 where the dataset holds\n    fewer neurons) and the latency are within tolerance.\n- id: fig3b-cn-net-disinhibition\n  statement: ALM photo-inhibition makes more CN neurons increase than decrease their activity\n    (123 against 62 of 185), a net disinhibition of the CN.\n  source: Results, paragraph 8; Figure 3b\n  quote: Photo-inhibiting ALM caused a greater proportion of CN neurons to increase their activity,\n    resulting in net disinhibition of CN ( Fig 3b , 123/185 increase, 62/185 decrease, p<0.001,\n    binomial test)\n  statistics:\n  - test: binomial test\n    p: 0.001\n    p_relation: \"<\"\n    n: 185 modulated CN neurons\n  expected:\n  - quantity: modulated CN neurons that increase\n    value: 123\n    tolerance: 12.3\n  - quantity: modulated CN neurons that decrease\n    value: 62\n    tolerance: 6.2\n  depends_on:\n  - fig3-cn-altered-by-alm-inhibition\n  criterion: Among the neurons modulated in fig3-cn-altered-by-alm-inhibition, the sign of the\n    delay epoch rate change. Reproduced when the counts are within tolerance (or the increase\n    fraction 0.66 within 10%, where the dataset holds fewer neurons) and a two-sided binomial\n    test against one half gives p < 0.001.\n- id: fig3c-cn-selectivity-abolished\n  statement: ALM photo-inhibition abolishes CN selectivity for \"lick left\" and \"lick right\"\n    trials.\n  source: Results, paragraph 8; Figure 3c; Extended Data Figure 5b to 5d\n  quote: CN selectivity for \"lick left\" and \"lick right\" trials was abolished by photo-inhibiting\n    ALM\n  criterion: Population selectivity as E3 over selective CN neurons tested on > 3 trials in all\n    conditions (n = 157), control against photo-inhibition trials. The window is open (readings\n    (a) the whole delay epoch, the photo-inhibition period; (b) the last 500 ms of the delay, as\n    in Extended Data Fig. 9b). Reproduced when under one reading the control selectivity is above\n    zero (bootstrap 95% interval over neurons) and the photo-inhibition selectivity is not\n    distinguishable from zero (its interval includes zero).\n- id: ed6-cn-selectivity-both-alm-hemispheres\n  statement: Photo-inhibiting either hemisphere of ALM reduces CN preparatory activity, and\n    photo-inhibiting motor cortex posterior to ALM has less effect.\n  source: Results, paragraph 8; Extended Data Figure 6a to 6e\n  quote: Photo-inhibiting either side of ALM reduced CN preparatory activity ( Extended Data Fig 6a–d\n    ). Photo-inhibiting motor cortex regions posterior to ALM produced less effect on CN\n    preparatory activity\n  criterion: Population selectivity as E3 over the n = 157 neurons, delay window readings as in\n    fig3c-cn-selectivity-abolished, in control, contralateral and ipsilateral unilateral ALM\n    photo-inhibition trials. Reproduced when both unilateral conditions lower selectivity below\n    control (bootstrap 95% interval of the difference over neurons excludes zero). The M1\n    comparison is shown only with example neurons in the paper; it is reported, with the same\n    measure on neurons tested with M1 photo-inhibition, but does not decide the outcome.\n- id: fig3d-alm-altered-by-cn-inhibition\n  statement: CN photo-inhibition during the delay rapidly alters the activity of many ALM neurons\n    (197 of 454), with a latency of 7.1 plus or minus 3.8 ms.\n  source: Results, paragraph 9; Figure 3d and 3e; Extended Data Figure 5e\n  quote: Activity of many ALM neurons was rapidly altered by CN photo-inhibition (197/454, p<0.01,\n    two-tailed t-test, Extended Data Fig 5e ; latency, 7.1 ± 3.8 ms)\n  expected:\n  - quantity: ALM pyramidal neurons recorded during CN photo-inhibition\n    value: 454\n    tolerance: 45.4\n  - quantity: ALM neurons significantly modulated\n    value: 197\n    tolerance: 19.7\n  - quantity: latency\n    value: 7.1\n    tolerance: 3.8\n    unit: ms\n  criterion: ALM recordings during contralateral CN photo-inhibition in the 4 L7-cre x Ai32 mice\n    (19 sessions); units as E1; photo-inhibition 1.3 s from delay onset, both powers pooled (the\n    Fig. 3d legend gives 1.5 to 4.5 mW). Modulated as E4 on the whole delay epoch; latency as E5\n    (both readings). Reproduced when under one reading the count (or the fraction 0.43 where the\n    dataset holds fewer neurons) and the latency are within tolerance.\n- id: fig3e-alm-mean-rate-unchanged\n  statement: Despite the changes in individual neurons, the average ALM spike rate is nearly\n    unchanged by CN photo-inhibition (4.15 against 4.39 spikes/s).\n  source: Results, paragraph 9\n  quote: 'However, the average spike rate was nearly unchanged (control: 4.15 spikes/s;\n    photo-inhibition: 4.39 spikes/s; p=0.58, two-tailed t-test)'\n  statistics:\n  - test: two-tailed t-test\n    p: 0.58\n  expected:\n  - quantity: mean ALM spike rate, control\n    value: 4.15\n    tolerance: 0.415\n    unit: spikes/s\n  - quantity: mean ALM spike rate, CN photo-inhibition\n    value: 4.39\n    tolerance: 0.439\n    unit: spikes/s\n  criterion: A claim of absence, judged on the paper's two-tailed t-test at p < 0.05. Mean delay\n    epoch spike rate per neuron in control and photo-inhibition trials (E4 trials). Open, and run\n    under each reading, are the neurons averaged ((a) all 454 pyramidal neurons, (b) the 197\n    modulated) and whether the t-test is paired over neurons or unpaired. Reproduced when the\n    rates are within tolerance under one reading of the neurons and the t-test finds no\n    difference; the outcome is marked as resting on the reading when paired and unpaired\n    disagree. The rate change is reported.\n- id: fig3e-alm-increase-decrease\n  statement: Among ALM neurons modulated by CN photo-inhibition, 108 increase and 89 decrease\n    their responses.\n  source: Results, paragraph 9; Figure 3e\n  quote: Individual ALM neurons increased (108/197) or decreased (89/197) their responses during CN\n    photo-inhibition\n  expected:\n  - quantity: modulated ALM neurons that increase\n    value: 108\n    tolerance: 10.8\n  - quantity: modulated ALM neurons that decrease\n    value: 89\n    tolerance: 8.9\n  depends_on:\n  - fig3d-alm-altered-by-cn-inhibition\n  criterion: Sign of the delay epoch rate change among the neurons of\n    fig3d-alm-altered-by-cn-inhibition. Reproduced when both counts are within tolerance, or,\n    where the dataset holds fewer neurons, the increase fraction (0.55) is within 10%.\n- id: fig3f-alm-selectivity-abolished-by-cn-inhibition\n  statement: CN photo-inhibition abolishes ALM trial-type selectivity.\n  source: Results, paragraph 9; Figure 3f\n  quote: ALM trial-type selectivity was abolished by CN photo-inhibition ( Fig 3f )\n  expected:\n    quantity: selective ALM neurons tested on more than 3 trials in all conditions\n    value: 329\n    tolerance: 32.9\n  criterion: Population selectivity as E3 (preferred type from 10 trials) over selective ALM\n    neurons tested on > 3 trials in all conditions (n = 329, Fig. 3f legend), control against CN\n    photo-inhibition trials, all trials grouped by instructed type. Window readings as in\n    fig3c-cn-selectivity-abolished. Reproduced when under one reading the control selectivity is\n    above zero (bootstrap 95% interval over neurons) and the photo-inhibition selectivity is not\n    distinguishable from zero. The neuron count is reported against its expected value.\n- id: fig4bc-fastigial-targets-alm-thalamus\n  statement: Fastigial projections overlap ALM-projecting thalamus (VM and parts of VAL) more than\n    dentate projections, which target a more dorsal and lateral region.\n  source: Results, paragraph 10; Figure 4b and 4c; Extended Data Figure 7d to 7f\n  quote: Fastigial projections mostly overlapped with parts of the thalamus that project to ALM\n    (i.e., ventral medial nucleus, VM, and parts of anterior-lateral nucleus, VAL), whereas\n    dentate projections targeted an adjacent region that was more dorsal and lateral\n  criterion: Anatomy (6 fastigial, 4 dentate and 8 ALM injections). Area fraction overlap per\n    coronal section after CCF alignment and thresholding near the 89th percentile (Methods,\n    Anatomy, analysis). The paper reports no test; reproduced when the fastigial overlap is\n    higher than the dentate overlap in sections from the same brains. The dandiset is described\n    as ALM recordings, so these data are likely not in it.\n- id: ed8-snr-sc-converge\n  statement: ALM-projecting thalamus receives inputs from the SNr and the lateral superior\n    colliculus with overlaps comparable to the fastigial nucleus, while dentate overlap is lower.\n  source: Extended Data Figure 8b\n  quote: Fastigial, SNr, and superior colliculus labeling show comparable amount of overlaps with\n    ALM-projecting thalamus. Dentate labeling show less overlap\n  criterion: Area fraction overlap as in fig4bc-fastigial-targets-alm-thalamus, per source area.\n    No test reported; reproduced when the SNr and superior colliculus overlaps lie within the\n    range of the fastigial overlaps and the dentate overlaps lie below it.\n- id: fig4-fastigial-activation-alm-latency\n  statement: Fastigial photo-activation changes ALM activity rapidly (latency 4.5 plus or minus\n    2.6 ms), consistent with a disynaptic pathway through the thalamus.\n  source: Results, paragraph 11; Extended Data Figure 9a\n  quote: Fastigial photo-activation induced rapid changes in ALM activity (latency, 4.5 ± 2.6 ms;\n    Extended Data Fig 9a ), consistent with a disynaptic pathway through the thalamus\n  expected:\n  - quantity: latency of the ALM response to fastigial photo-activation\n    value: 4.5\n    tolerance: 2.6\n    unit: ms\n  - quantity: ALM neurons significantly modulated by fastigial photo-activation\n    value: 227\n    tolerance: 22.7\n  criterion: ALM pyramidal neurons in the fastigial photo-activation sessions (n = 446), early\n    delay photo-activation (0.455 s from delay onset; powers 0.5 to 1.5 mW pooled, as the Fig.\n    4d legend gives). Modulated as E4 at p < 0.01; latency as E5 (both readings). Reproduced\n    when under one reading the latency and the count (or the fraction 0.51) are within\n    tolerance.\n- id: fig4e-fastigial-activation-abolishes-alm-selectivity\n  statement: Fastigial photo-activation abolishes selective persistent and ramping activity in\n    most ALM neurons, while in a minority it creates new preparatory activity.\n  source: Results, paragraph 11; Figure 4e; Extended Data Figure 9c\n  quote: Selective persistent and ramping activity was abolished in most ALM neurons ( Fig 4e , top).\n    In a minority of neurons, photo-activation created new preparatory activity\n  expected:\n    quantity: selective ALM neurons tested on more than 3 trials in all conditions, fastigial\n      sessions\n    value: 328\n    tolerance: 32.8\n  criterion: Population selectivity as E3 over the selective ALM neurons tested on > 3 trials in\n    all conditions (n = 328, Extended Data Fig. 9c), control against fastigial photo-activation\n    trials, in the delay after the photostimulus (readings (a) from photostimulus offset to the\n    go cue, (b) the last 500 ms of the delay). Per neuron, abolished means delay selectivity\n    significant in control (E2 test on that window) and not in photo-activation trials; new\n    means the reverse. Reproduced when under one reading the population selectivity is lower in\n    photo-activation trials (bootstrap 95% interval of the difference excludes zero), more than\n    half of the control-selective neurons lose significance, and the neurons gaining it are\n    fewer than those losing it.\n- id: fig4f-fastigial-effect-persists\n  statement: Transient fastigial photo-activation alters ALM preparatory activity long (more than\n    1 s) after the photostimulus ends.\n  source: Results, paragraph 11; Figure 4f; Extended Data Figure 9b\n  quote: Transient photo-activation of the fastigial nucleus altered ALM preparatory activity long\n    (>1 s) after cessation of the photostimulus\n  criterion: For each of the 446 ALM neurons, E4 in 400 ms bins in 50 ms steps (Fig. 4f) gives the\n    fraction with a significant change (p < 0.01). What the fraction is compared with is not\n    given (open; readings (a) the 1% expected by chance at p < 0.01, (b) the fraction in the\n    bins before photostimulus onset). Reproduced when under one reading the fraction in bins\n    starting 1 s or more after photostimulus offset (and ending before the go cue or within the\n    response epoch) exceeds the comparison, by a one-sided binomial test at p < 0.05 for reading\n    (a) or a one-sided test of two proportions for reading (b).\n- id: fig4g-dentate-effect-recovers\n  statement: Dentate photo-activation also changes ALM responses (latency 8.3 plus or minus 5.0\n    ms), but ALM activity recovers quickly after it.\n  source: Results, paragraph 11; Figure 4g; Extended Data Figure 9a\n  quote: Dentate photo-activation also induced ALM response changes ( Fig 4g ; latency, 8.3 ± 5.0\n    ms). Importantly, activity quickly recovered after dentate photo-activation\n  expected:\n  - quantity: latency of the ALM response to dentate photo-activation\n    value: 8.3\n    tolerance: 5.0\n    unit: ms\n  - quantity: ALM neurons significantly modulated by dentate photo-activation\n    value: 163\n    tolerance: 16.3\n  depends_on:\n  - fig4f-fastigial-effect-persists\n  criterion: As fig4-fastigial-activation-alm-latency and fig4f-fastigial-effect-persists on the\n    466 neurons of the dentate sessions. Reproduced when under one reading the latency and count\n    (or fraction 0.35) are within tolerance and the fraction of significant neurons in bins\n    starting 1 s or more after photostimulus offset is not above the comparison of\n    fig4f-fastigial-effect-persists (same test, p >= 0.05) and is lower than the fastigial\n    fraction in the same bins.\n- id: fig4i-cd-control-separation\n  statement: In control trials, ALM activity trajectories for \"lick left\" and \"lick right\"\n    diverge along the coding direction during the sample epoch and stay separated through the\n    delay epoch.\n  source: Results, paragraph 12; Figure 4h and 4i\n  quote: In control trials, activity trajectories from \"lick left\" and \"lick right\" trials diverged\n    from each other along the cd during the sample epoch and remained separated throughout the\n    delay epoch\n  criterion: Coding direction and projections as E6, over the 28 sessions. Separation is the\n    \"lick right\" minus \"lick left\" projection of control trials, averaged across sessions, with a\n    bootstrap over sessions. Reproduced when the 95% interval excludes zero at some time in the\n    sample epoch and at every 400 ms window centred within the delay epoch.\n- id: fig4i-fastigial-collapses-cd\n  statement: Fastigial photo-activation collapses ALM activity trajectories along the coding\n    direction, while dentate photo-activation minimally affects them.\n  source: Results, paragraph 12; Figure 4i; Extended Data Figure 9c\n  quote: Fastigial photo-activation resulted in a collapse of activity trajectories ... In\n    contrast, dentate photo-activation minimally impacted activity trajectories along the cd ,\n    despite having an impact on ALM neuron responses\n  depends_on:\n  - fig4i-cd-control-separation\n  criterion: Separation along the cd as in fig4i-cd-control-separation, in control, fastigial and\n    dentate photo-activation trials, in the last 400 ms of the delay (the window of Extended Data\n    Fig. 10c) and averaged from photostimulus offset to the go cue. \"Collapse\" is open (readings\n    (a) fastigial separation not distinguishable from zero; (b) fastigial separation lower than\n    control, the bootstrap interval of the difference over sessions excluding zero). Reproduced\n    when under one reading and one window the fastigial separation collapses and, in the same\n    window, the dentate separation does not differ from its control (interval of the difference\n    includes zero).\n- id: cd-captures-selectivity\n  statement: The projection along the coding direction captures 64.1% of ALM population\n    selectivity over the sample and delay epochs and 27.0% of the total variance in task-related\n    activity.\n  source: Methods, Analysis of ALM population dynamics in the activity space, paragraph 1\n  quote: The projection along the cd captured 64.1±3.4% of the population selectivity for \"lick\n    left\" and \"lick right\" trials over the sample and delay epochs (root mean square, RMS, of the\n    spike rate difference between \"lick right\" and \"lick left\" trials), and 27.0±4.2% of the total\n    variance in ALM task-related activity\n  expected:\n  - quantity: fraction of population selectivity captured by the cd\n    value: 64.1\n    tolerance: 3.4\n    unit: \"%\"\n  - quantity: fraction of task-related variance captured by the cd\n    value: 27.0\n    tolerance: 4.2\n    unit: \"%\"\n  criterion: Per session (E6), on control trials over the sample and delay epochs. Selectivity is\n    the RMS of the \"lick right\" minus \"lick left\" rate difference; variance is the RMS of the\n    baseline-subtracted activity. How the captured fraction is formed is open (readings (a) the\n    ratio of the RMS along the unit cd to the RMS over all neurons; (b) the ratio of their squares,\n    a fraction of variance); the baseline window is not given (reading the 500 ms before sample\n    onset, a standard choice). The spread is read as s.e.m. across sessions. Reproduced when under\n    one reading both means are within tolerance.\n- id: ed10c-alm-inhibition-endpoints-predict\n  statement: After bilateral ALM photo-inhibition in the early delay, the distance of ALM\n    trajectories to the endpoints along the coding direction still predicts the future movement,\n    though performance is near chance.\n  source: Supplementary Information, page 1, paragraph 1; Extended Data Figure 10b and 10c\n  quote: But in a trial-by-trial analysis movement direction could still be predicted based on the\n    distance of the perturbed activity trajectories to the endpoints on the cd\n  statistics:\n  - about: performance drop with bilateral ALM photo-inhibition\n    test: one-sided bootstrap\n    p: 0.001\n    p_relation: \"<\"\n    n: 7 mice\n  criterion: The paper does not say which mice or sessions carried bilateral ALM photo-inhibition\n    during ALM recording (n = 690 trials; ALM photo-inhibition needs VGAT-ChR2 mice, which\n    Supplemental Table 1 does not list for ALM recordings). Where the dataset holds such trials,\n    the projection cd'x in the last 400 ms of the delay (E6, cd from independent correct control\n    trials) is binned and the probability of licking right is computed per bin, pooled over\n    sessions. Reproduced when that probability rises with the projection, by a logistic\n    regression of lick direction on the projection with slope p < 0.05 (a standard test named\n    here, the paper gives none).\n- id: ed10d-fastigial-endpoints-no-prediction\n  statement: After fastigial photo-activation, the distance of ALM trajectories to the endpoints\n    along the coding direction no longer predicts future movements.\n  source: Supplementary Information, page 1, paragraph 1; Extended Data Figure 10d\n  quote: After fastigial photo-activation, the distance of the perturbed trajectories to these\n    endpoints no longer predicted future movements\n  statistics:\n  - about: performance drop with fastigial photo-activation\n    test: one-sided bootstrap\n    p: 0.001\n    p_relation: \"<\"\n    n: 6 mice\n  criterion: A claim of absence; the paper shows a binned curve (n = 337 fastigial photo-activation\n    trials) and names no test. As ed10c-alm-inhibition-endpoints-predict on the fastigial\n    photo-activation trials, with the logistic regression named there at p < 0.05. Reproduced\n    when the slope is not significant; the slope and its interval are reported, with the slope\n    on control trials for comparison.\n- id: ed10ef-alm-drives-licking-after-fastigial\n  statement: Unilateral ALM photo-inhibition before the go cue biases licking ipsilaterally\n    whether or not a fastigial perturbation preceded it, and bilateral ALM photo-inhibition\n    during movement initiation raises the no-lick rate even after a fastigial perturbation.\n  source: Supplementary Information, page 1, paragraph 2; Extended Data Figure 10e to 10g\n  quote: Unilateral ALM photo-inhibition before movement initiation biased upcoming movements to the\n    ipsilateral direction regardless of a preceding fastigial perturbation (Extended Data Fig\n    10e-f). Bilateral ALM photo-inhibition during movement initiation led to an increased no lick\n    rate even after a preceding fastigial perturbation\n  statistics:\n  - about: unilateral ALM photo-inhibition alone, performance on contralateral trials\n    test: one-sided bootstrap\n    p: 0.0002\n    n: 4 mice\n  - about: unilateral ALM photo-inhibition after fastigial perturbation, weaker mark\n    test: one-sided bootstrap\n    p: 0.04\n    n: 4 mice\n  - about: unilateral ALM photo-inhibition after fastigial perturbation, stronger mark\n    test: one-sided bootstrap\n    p: 0.008\n    n: 4 mice\n  - about: no lick rate, bilateral ALM photo-inhibition, weaker mark\n    test: one-sided bootstrap\n    p: 0.002\n    n: 3 mice\n  - about: no lick rate, bilateral ALM photo-inhibition, stronger mark\n    test: one-sided bootstrap\n    p: 0.0002\n    n: 3 mice\n  criterion: VGAT-ChR2-EYFP behavior (Methods, ALM photo-inhibition after a fastigial\n    perturbation). Unilateral ALM photo-inhibition from 800 ms after delay onset to the go cue;\n    performance per trial type (B1) with trials grouped by licking direction relative to the\n    inhibited ALM. Reproduced when, both alone and after the fastigial perturbation,\n    performance on trials instructing contralateral licking drops with a one-sided bootstrap p <\n    0.05, and when the no-lick rate with bilateral ALM photo-inhibition (1.3 s from the go cue)\n    after the perturbation exceeds that with the perturbation alone, one-sided bootstrap p <\n    0.05. These are behavioral data, likely not in a dataset of ALM recordings.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/gao-2018.yaml paper/10.1038-s41586-018-0633-x.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims && python3 - <<'EOF'
p='gao-2018.yaml'; t=open(p).read()
t=t.replace("""  expected:
  quantity: fraction of CN neurons with a negative error-to-correct selectivity ratio
    value: 0.67
    tolerance: 0.067""","""  expected:
  - quantity: fraction of CN neurons with a negative error-to-correct selectivity ratio
    value: 0.67
    tolerance: 0.067""")
t=t.replace("""  expected:
    quantity: selective ALM neurons tested on more than 3 trials in all conditions
    value: 329""","""  expected:
  - quantity: selective ALM neurons tested on more than 3 trials in all conditions
    value: 329""")
t=t.replace("""  expected:
    quantity: selective ALM neurons tested on more than 3 trials in all conditions, fastigial
      sessions""","""  expected:
  - quantity: selective ALM neurons tested on more than 3 trials in all conditions, fastigial
      sessions""")
open(p,'w').write(t)
EOF
cd .. && python tools/claims_check.py claims/gao-2018.yaml paper/10.1038-s41586-018-0633-x.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -e "—" -e "rather" claims/gao-2018.yaml; python3 -c "
import yaml;d=yaml.safe_load(open('claims/gao-2018.yaml'))
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"
```

```
44 16 44 18
```

**Agent**

I've written `claims/gao-2018.yaml` with 44 claims. The quote checker passes with 0 problems; nothing was committed.

**Text read**
- **Main paper:** the NIH author manuscript (PMC6212318) from Europe PMC: main text, Methods, and the legends of Figs. 1–4 and Extended Data Figs. 1–10.
- **Supplement 1:** the Supplementary Information, including Supplemental Table 1, which lists the mice and manipulated hemispheres.
- **Supplement 2:** the reporting summary.
- **No PDF of the main paper**, so anything shown only inside the figures (values, which bar a significance mark belongs to) could not be read. Claims rest on the text and legends.
- **No code:** the paper links none. It says code is "available ... upon reasonable request" and "will be deposited on CRCNS.org", with no identifier.
- **Dataset:** its archive description reads "Extracellular recording in ALM".

**Counts**
- All 44 claims have quotes; none needed `inferred`.
- 16 claims carry statistics (21 values), 18 have expected values with tolerances, and all 44 have criteria.
- The claims cover lesions, photo-activation and photo-inhibition behavior, ALM and CN selectivity, the cross-area perturbations, anatomy, coding-direction analyses and the Extended Data Fig. 10 experiments.

**Details the paper leaves open, with the readings named**
- **Response epoch window:** 1.3 s from the go cue, or the 1.5 s answer window.
- **Trials in the selectivity test:** correct trials only, or all trials grouped by instructed direction.
- **Preferred trial type:** whether the 10 or 20 trials that fix it are counted in total or per type, and which epoch fixes it.
- **Trials in photostimulation tests:** all trials, or correct trials only.
- **Neurons entering the latency estimate:** modulated during the photostimulus, or over the whole delay.
- **Denominator for 59%/35% preparatory and 67%/66% peri-movement:** all neurons, or selective neurons.
- **CN n = 197 in Fig. 2d:** all 416 selective neurons, or only those with sample or delay selectivity.
- **Window for "selectivity abolished":** the whole delay, or the last 500 ms. "Collapse" along the coding direction is read as either indistinguishable from zero or lower than control.
- **Fig. 4f "persists >1 s":** compared against the 1% chance level, or against the fraction before the photostimulus.
- **Mean rate of 4.15 vs 4.39 spikes/s:** over all 454 neurons or the 197 modulated ones, and with a paired or unpaired t-test.
- **Lick-modulation t-test:** paired or unpaired.
- **"Captured fraction" of selectivity:** a ratio of RMS values or of their squares. The baseline window is also not given.
- **VGAT performance percentages:** pooled over trials, or averaged over mice.

**Choices I made where the paper gives none**
- Several absence claims have no test in the paper (licking unaffected, Extended Data Fig. 10d). I used the Methods' hierarchical bootstrap or a logistic regression and labelled each as a choice in the criterion.
- How trials are split for the coding direction is not given. I used a random half split as a standard choice.

**Gaps that affect claims**
- Two legends give p-values without the figure to show which bar each belongs to (Extended Data Fig. 2h: p = 0.04 and 0.0002; Extended Data Fig. 10f–g). Both values are recorded.
- It is not clear which mice carried bilateral ALM photo-inhibition during ALM recording (Extended Data Fig. 10c, n = 690 trials). Supplemental Table 1 lists no such mice.
- The number of ALM-recorded mice disagrees: the Methods add up to 12 (10 left, 2 right) but the table lists 13.
- The CN, anatomy and behavior-only claims are kept as findings, but the dataset described as ALM recordings likely does not hold their data.

Nothing the claims needed was missing from the text itself.

## End of run

26 turns, 5 minutes, $1.88 at API prices, result: success.
