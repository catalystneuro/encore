# wirth-2017 · author-revise-1 · run 43445292475

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/wirth-2017/verifier-1-report.md; ls entries/wirth-2017 entries/wirth-2017/*; ls paper questions | head
```

```
Fri Nov 13 14:49:54 UTC 2026
A. Outcomes for the 28 claims in the claims file

| Claim | Outcome | Reason |
|---|---|---|
| gaze-anticipates-action | reproduced | Cell 23: before right turns the eye signal differs from before left turns in each monkey, in both windows and for every eye choice (500 ms, both eyes: K −0.77 SD, p = 4e-148; S −1.00 SD, p = 4e-146; 39/40 and 20/20 sessions). The direction depends on an assumed sign of the eye signal (cell 24, problem 1). |
| gaze-anticipates-landmarks | partially_reproduced | Cell 26: the eye signal differs between right and left returns in each monkey, p ≤ 1.5e-10 under every reading. The side relative to the turn is not tested independently, because the sign was chosen on the assumption that the eyes deviate toward the side the view rotates to, and that is what this test measures (problem 1). |
| learning-trials | reproduced | Cell 17: S 12.26 (12.3 ± 2), K 16.53 under reading (a) and 15.82 under (b) (14.8 ± 2.4). The curves are the files' own; their column order was checked against `learningtrial` in 66 of 66 sessions (cell 8). |
| learning-to-90 | reproduced | Cell 18: 0.898 of sessions that reach both criteria, 0.803 of all sessions; both fall within 0.89 ± 0.089. |
| probe-transfer | not_reproduced | Cell 20: monkey K, 12 sessions: 28.3% in the first 5 trials (44 ± 4.4) and 58.3% after the new entries (73 ± 7.3); Wilcoxon p = 0.072. Monkey S has no probe session in hc-12 and none in hc-21 (data_missing for that part). |
| probe-faster-criterion | blocked (methods_underspecified) | The criterion needs learning curves recomputed from the introduction with the unnamed method of reference 60. Monkey S also has no probe sessions (data_missing). |
| cells-recorded | partially_reproduced | Cell 14: 186 cells with more than 100 spikes (189 ± 18.9). The archive holds only the 189 deposited cells, so the 270 recorded cells (128 S, 142 K) cannot be checked. |
| responsive-cells | blocked (metadata_insufficient) | The point-of-
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l docs/protocol.md; grep -n "^#" docs/protocol.md
```

```
676 docs/protocol.md
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
345:### 2. Check the data against its description
360:### 3. Write the entry
431:### 4. Lock, check and run
451:### 5. Record the attempt
524:### 6. Hand over for verification
562:## Repeat attempts
604:## Local and remote datasets
627:## Verifier
631:### Round 1: without the author's conclusions
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,42p docs/protocol.md; sed -n 199,676p docs/protocol.md
```

```
<persisted-output>
Output too large (30.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a7a5e708-8061-45a5-9931-0ad0498856a4/tool-results/bm205v5ng.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-15`. Record this version in the attempt's provenance.

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
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a7a5e708-8061-45a5-9931-0ad0498856a4/tool-results/bm205v5ng.txt"
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
[... 501 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep wirth; wc -l attempts/wirth-2017-01.yaml entries/wirth-2017/*; cat entries/wirth-2017/entry.yaml; ls claims 2>/dev/null | grep wirth; ls papers/claims 2>/dev/null | grep wirth; ls executed/wirth-2017 2>/dev/null
```

```
wirth-2017-01.yaml
   390 attempts/wirth-2017-01.yaml
    29 entries/wirth-2017/README.md
    25 entries/wirth-2017/entry.yaml
  1197 entries/wirth-2017/reproduce_wirth_2017.ipynb
     8 entries/wirth-2017/requirements.in
  1666 entries/wirth-2017/requirements.lock.txt
   783 entries/wirth-2017/wirth.py
  4098 total
schema_version: 1
name: wirth-2017
type: reproduction
title: Space in the macaque hippocampus during virtual navigation (Wirth et al. 2017)
description: Tests the findings of Wirth, Baraduc, Plante, Pinede and Duhamel (2017) on CRCNS hc-12,
  which holds 189 hippocampal cells of two macaques navigating a virtual star maze with eye tracking,
  and uses CRCNS hc-21 to check which of its recordings are also in hc-12. It covers learning, gaze
  before turns and on passive returns, information content in position, direction and state space,
  centre and return direction maps, state-space selectivity and the landmark ANOVAs. The point-of-gaze
  analyses need a calibration of the eye signal that the files do not give.
license: Apache-2.0
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/wirth-2017-01.yaml
```

```
schema_version: 3
id: wirth-2017-01
datasets:
- archive: crcns
  id: hc-21
  version: unversioned
  doi: 10.6080/K0GX48R9
  relation: primary
- archive: crcns
  id: hc-12
  version: unversioned
  doi: 10.6080/K0R49NQV
  relation: primary
paper: doi:10.1371/journal.pbio.2001045
date: 2026-11-13
entry: wirth-2017
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
[... 370 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/; cat claims/wirth-2017.yaml | head -600
```

```
<persisted-output>
Output too large (38.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a7a5e708-8061-45a5-9931-0ad0498856a4/tool-results/bqv3xtf2f.txt

Preview (first 2KB):
alasfour-2024.yaml
amjad-2025.yaml
andrews-2024.yaml
armstrong-2026.yaml
asari-2009.yaml
ashworth-2025.yaml
athalye-2023.yaml
azcorra-2023.yaml
bakalar-2023.yaml
bech-2026.yaml
bellvila-2026.yaml
bennett-2024.yaml
berg-2020.yaml
boran-2019.yaml
boran-2022.yaml
bouabid-2026.yaml
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims; python - <<'EOF'
import yaml
d=yaml.safe_load(open('wirth-2017.yaml'))
print({k:v for k,v in d.items() if k!='claims'})
for c in d['claims']:
    if c['id'] in ('gaze-anticipates-action','gaze-anticipates-landmarks','direction-center-vs-periphery','direction-tuning-not-maintained','state-space-ic-higher','spatial-selectivity-fraction','state-space-selectivity','state-space-most-responsive','sparsity-state-vs-position','learning-to-90','probe-transfer','latency-skew','responsive-cells'):
        print(yaml.safe_dump(c,width=120,sort_keys=False))
EOF
```

```
{'schema_version': 2, 'paper': 'doi:10.1371/journal.pbio.2001045', 'checks': [{'date': datetime.date(2026, 11, 10), 'kind': 'agent', 'model': 'claude-opus-5-5', 'ready': True, 'changes': ['Header, Method W, binomial tests. Added that 1 of 42 with p = 0.37 matches the lower tail P(X <= 1) at a chance rate of 0.05 (computed, 0.372); the file had said no reading gives it.', 'path-selectivity. Same correction in the criterion; the chance rate is now 0.05 (reading (a)), and the p = 0.37 is still reported, not judged.', 'gaze-anticipates-action, gaze-anticipates-landmarks. The criteria required p < 0.001 in each monkey, but the Results give one p and do not say the monkeys were tested separately (S2 Fig shows them apart). Named per monkey and pooled as readings.', "probe-faster-criterion. Reading (b), trials to the first correct trial from a new entry, is not the learning criterion (lower bound above 1/4, S3B legend) and was made up. Reading (a), the session's running curve, is in most sessions already past criterion when the new entries come in (S3C legend, trials 37 and 60). Replaced both with learning curves begun at the introduction, on all trials or on new-entry trials only.", 'sparsity-state-vs-position (and through it sparsity-gaze-vs-state). The per-cell significance level for the sparsity difference was fixed at 0.05 without a source; the paper does not state it. Named 0.05 and 0.01 as readings.', 'fields-per-cell, gaze-map-landmarks. The source said paragraph 4 of "What is encoded in hippocampal cell activity"; the sentences are in paragraph 3 (the section has three paragraphs before the Fig 2 legend).', "gaze-map-landmarks. The excess measure (peak near a landmark over mean elsewhere, minus 1) is not the paper's; it is now marked as a standard choice and a deviation.", 'spatial-selectivity-fraction. Added reading (c), position-responsive cells among the 111 responsive cells, which the Discussion\'s "our cells" also allows (Fig 3A gives proportions per space).',
[... 317 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/wirth-2017.yaml'));print(d.get('header') or d.get('methods') or [k for k in d])"; grep -n "Method W" claims/wirth-2017.yaml | head -3
```

```
['schema_version', 'paper', 'claims', 'checks']
21:# read them for the map binning left open in Method W, citing the file.
51:# Method shared by the claims (every claim that says "Method W"). Each part is cited.
111:    move (event codes for rotation), with Method W's trials. Readings (a) 500 ms; (b) 300 ms;
```

**Agent calls Bash**

```bash
sed -n 1,100p claims/wirth-2017.yaml
```

```
# Claims for Wirth, Baraduc, Plante, Pinede & Duhamel (2017), PLoS Biology 15(2), e2001045,
# tested on CRCNS hc-12 and hc-21.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
# protocol pilot-14 as stated in docs/protocol.md.
#
# Text read: the version of record (PMC5328243, open access), full text from Europe PMC JATS
# XML as stored under paper/: Results, Discussion, Materials and Methods, the figure legends of
# Figs 1 to 7 and the legends of S1 to S7 Figs. The supplementary text files S1 Appendix
# (sections A1 to A5: point-of-gaze density maps, gaze before joystick actions, recording
# methods and cell selection, population averages, the control for space dimensionality) and
# S2 Appendix (description of the CRCNS files and scripts) are DOCX files that are not under
# paper/ and were not read. The claims that rest on them say so (gaze-anticipates-action,
# gaze-anticipates-landmarks, dimensionality-control, fields-per-cell). No PDF was read; the
# reference list is absent from the stored text, so reference 60 (the learning curve method)
# is not named.
#
# Code: the paper links no repository. It says some Matlab scripts are hosted with the data on
# CRCNS (Supporting data; S2 Appendix); the hc-12 descriptor lists them (a scripts folder that
# plots position, direction and state-space maps, rasters and learning curves). These are files
# of the dataset and were not read. No criterion below takes a method from code; the author may
[... 80 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/wirth-2017/wirth.py"
}
```

```
1	"""Loading and measures for CRCNS hc-12 (and hc-21), the data of Wirth, Baraduc, Plante,
2	Pinede & Duhamel (2017), PLoS Biology 15(2), e2001045, doi:10.1371/journal.pbio.2001045.
3	
4	The data sets are single tar.gz archives of MATLAB files, one file per cell, in the public S3
5	bucket crcnsarchive. They are streamed: the archive is decompressed as it is read and each
6	member is loaded in memory and reduced to what the analysis needs, one at a time. Nothing is
7	written to disk.
8	
9	File layout (descriptor of hc-12, version 0.7, and the files themselves): spike times
10	(`file.elec`, or `file.newallo.elec` when the top level has none), the trial tables of the new
11	maze (`newallo.codematrix`, `newallo.timematrix`), learning curves, eye positions at 250 Hz
12	with `eye_times`, and `camera_data.time_60`, 60 Hz rows of [time, x, y, camera orientation
13	(deg), curvilinear abscissa on the maze branch (0 centre, 1 arm end), state-space curvilinear
14	abscissa, state-space polar angle, state-space radius, next, previous and current transition
15	tag, composite maze tag]. `time_60` sits under `newallo.camera_data` in some files.
16	
17	Where the parameters come from:
18	
19	- Successful trials only; maps unsmoothed; a bin is valid with at least four successful
20	  trials (Methods, Activity maps) and more than 400 ms of time in successful trials (Methods,
[... 764 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f"=== [{i}] {c['cell_type']} {c.get('metadata',{}).get('tags','')}")
    print(''.join(c['source']))
EOF
```

```
<persisted-output>
Output too large (42.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/a7a5e708-8061-45a5-9931-0ad0498856a4/tool-results/bwgz0pl1l.txt

Preview (first 2KB):
=== [0] markdown 
# Reproducing Wirth et al. (2017) from CRCNS hc-12

Paper. Wirth S, Baraduc P, Plante A, Pinede S, Duhamel JR (2017). Gaze-informed, task-situated
representation of space in primate hippocampus during virtual navigation. PLoS Biology 15(2):
e2001045. [doi:10.1371/journal.pbio.2001045](https://doi.org/10.1371/journal.pbio.2001045).
The claims file (`claims/wirth-2017.yaml`) was written from the version of record (PMC5328243),
Results, Methods and the legends of Figs 1 to 7 and S1 to S7; S1 Appendix was not available.

Datasets. CRCNS [hc-12](https://doi.org/10.6080/K0R49NQV) (189 cells, the new-maze sessions;
every claim rests on it) and CRCNS [hc-21](https://doi.org/10.6080/K0GX48R9) (101 cells, a
familiar and a new maze per file), streamed from the public bucket `crcnsarchive`
(`hc-12/live/data.tar.gz`, `hc-21/live/data.tar.gz`). CRCNS data sets are not versioned; the
version is recorded as `unversioned`, and the MD5 sums from each data set's `checksums.md5`
for the files read are: hc-12 `data.tar.gz` 426c7d00c0358f2cc9873e0dbb331e2f (descriptor
version 0.7, 17 Jan 2017); hc-21 `data.tar.gz` dee5e8aa4a7b3c44b61b8cecfe622a0a (descriptor
[... 14 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/a7a5e708-8061-45a5-9931-0ad0498856a4/tool-results/bwgz0pl1l.txt"
}
```

```
1	=== [0] markdown 
2	# Reproducing Wirth et al. (2017) from CRCNS hc-12
3	
4	Paper. Wirth S, Baraduc P, Plante A, Pinede S, Duhamel JR (2017). Gaze-informed, task-situated
5	representation of space in primate hippocampus during virtual navigation. PLoS Biology 15(2):
6	e2001045. [doi:10.1371/journal.pbio.2001045](https://doi.org/10.1371/journal.pbio.2001045).
7	The claims file (`claims/wirth-2017.yaml`) was written from the version of record (PMC5328243),
8	Results, Methods and the legends of Figs 1 to 7 and S1 to S7; S1 Appendix was not available.
9	
10	Datasets. CRCNS [hc-12](https://doi.org/10.6080/K0R49NQV) (189 cells, the new-maze sessions;
11	every claim rests on it) and CRCNS [hc-21](https://doi.org/10.6080/K0GX48R9) (101 cells, a
12	familiar and a new maze per file), streamed from the public bucket `crcnsarchive`
13	(`hc-12/live/data.tar.gz`, `hc-21/live/data.tar.gz`). CRCNS data sets are not versioned; the
14	version is recorded as `unversioned`, and the MD5 sums from each data set's `checksums.md5`
15	for the files read are: hc-12 `data.tar.gz` 426c7d00c0358f2cc9873e0dbb331e2f (descriptor
16	version 0.7, 17 Jan 2017); hc-21 `data.tar.gz` dee5e8aa4a7b3c44b61b8cecfe622a0a (descriptor
17	version 0.52, 21 Dec 2018). Each data set has one published state (`live/`, with only
18	documentation under `orig/`), so the version pinned is the only one there is, and hc-12 is the
19	deposit the paper cites. hc-21 is read only to check whether it holds recordings that are also
20	in hc-12 and whether it holds the probe sessions hc-12 lacks; no claim rests on it.
[... 667 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "shift|surrogate|shuffl|chunk" 10.1371-journal.pbio.2001045.txt | head -40; wc -c *
```

```
53:We evaluated the four coding spaces using standard measures employed in rodents: the information content per spike (IC) and a sparsity index [ 3 , 6 , 24 ]. The first quantity documents how much spatial information a spike conveys, while the second expresses spatial selectivity. To compare IC across coding spaces, we ensured that the same number of bins was used across cells and spaces and normalized IC with respect to the average IC of 999 surrogate datasets generated by randomly shuffling periods of spiking activity in time (see Materials and Methods ). While this method may be conservative [ 25 ], it is widely used in rodent literature (e.g., [ 1 – 7 ]) as it effectively conveys information relative to the spatial distribution of the cell’s activity [ 26 ].
55:Statistical significance was tested by comparing measures derived from actual data with those in the 999 surrogate datasets. Significant IC ( p < 0.01) was present in at least one of the spaces for 111 out of the 189 cells (59%, responsive cells). The proportion of cells responsive to each space was significantly unequal (chi-squared test, p = 0.014). The state space accounted for the largest number (84 cells, Fig 3A ), and pitting state space against the other three, there were more cells responsive to state space than to point of gaze (chi-squared test, p = 0.012, Bonferroni corrected; the differences between state space and other spaces did not reach statistical significance). Sensitivity to these four variables was not mutually exclusive ( Fig 3B ).
57:Population statistics. A. Proportion of responsive cells (cells with significant information content [IC], above gray line) and proportion of cells significantly coding each of the four spaces (black). Open bars correspond to cells with significant IC in another space. B. Representation of the main intersections amongst each subpopulation of cells represented in A . Most responsive cells carry significant activity in more than one coding space. C. Anal
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; cat hc-12.data-description.txt; grep -n -i -E "S3C|S3 Fig|probe|eastern|western" 10.1371-journal.pbio.2001045.txt | head; date -u
```

```
Data descriptor: of the data set CRCNS:hc-12, not a paper. It describes the data set's files and how they were recorded.
Version: as published by CRCNS.org, https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-12/live/docs/crcns_hc-12_data_description.pdf
Source: the CRCNS data set's documentation (hc-12/live/docs/crcns_hc-12_data_description.pdf)
Stored: 2026-11-06
Extracted: PyMuPDF, dehyphenated, NFKC
------------------------------------------------------------------------
##### hc-12/live/docs/crcns_hc-12_data_description.pdf
Page 1 of 4 
CRCNS.org hc-12 data description 
Version 0.7 (Jan 17, 2017) 
Extracellular recordings from monkey hippocampus 
performing a virtual navigation task 
Summary 
The dataset is made of 189 cells recorded in the hippocampus from two Rhesus 
macaques. Recordings were made extracellularly with either single tungsten electrodes 
or 16 contact u-probes. Activity was recorded as animals were navigating via a joystick 
a virtual maze projected in stereo, searching for a reward.  A file contains the 
timestamps of the action potentials, the X,Y position and camera orientation in virtual 
coordinates, the left and right eye X,Y coordinates, and task relevant event codes. The 
dataset also contains the animal coordinates in the state space graph that was 
[... 160 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls executed/wirth-2017/; python - <<'EOF'
import json
nb=json.load(open('executed/wirth-2017/reproduce_wirth_2017.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    out=''.join(''.join(o.get('text','')) if 'text' in o else ''.join(o.get('data',{}).get('text/plain','')) for o in c.get('outputs',[]))
    print(f"=== [{i}]"); print(out[:6000])
EOF
```

```
reproduce_wirth_2017.ipynb
result.json
=== [1]

=== [3]
hc-12 pass: 1548 s, peak memory 0.98 GB

=== [4]
hc-21 pass: 188 s, 101 files

=== [6]
Files by monkey (ke = monkey K, sn = monkey S):
        files  with_new_maze  sessions
monkey                                
ke         99             99        41
sn         90             88        26

Files without a new-maze (newallo) field: ['sn20121015_HPC_e2_c1a_seg.mat', 'sn20121015_HPC_e2_c1c_seg.mat']

Spike times taken from: {'file.elec': 175, 'newallo.elec': 12}
[... 362 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -rn "verifications" tools/*.py schema* docs/*.md 2>/dev/null | head -30; ls schema* 2>/dev/null; ls attempts | head -3
```

```
tools/build_site.py:25:The trust tier of an attempt is derived from its verifications: the latest
tools/build_site.py:141:    verifications = attempt.get("verifications") or []
tools/build_site.py:142:    if not verifications:
tools/build_site.py:144:    latest = verifications[-1]
tools/build_site.py:282:        verifications = a.get("verifications") or []
tools/build_site.py:283:        disagreed = {r["claim"] for v in verifications for r in v["results"] if not r.get("agrees")}
tools/build_site.py:335:            "verifications": [{
tools/build_site.py:343:            } for v in verifications],
tools/build_site.py:540:            "verifications": [] if tier == "runs" else [{
tools/build_site.py:2955:        if not a["verifications"]:
tools/build_site.py:2960:        for i, v in enumerate(a["verifications"], 1):
tools/entry.py:350:        for rnd in (attempt.get("verifications") or [])[1:]:
schemas/attempt.schema.json:386:    "verifications": {
docs/pipeline.md:19:| 6 | Verification | yes | agents (verifier rounds, revisions), `papers` environment | the record's verifications |
docs/pipeline.md:160:and its verifications, the merge, a deprecation. The runner's queue holds only
docs/protocol.md:544:`verifications`, saying what was reviewed. Give the verifier's reasons in its
docs/queue.md:5:The record stays where it is: claims, attempts, entries and verifications are files in this repository, and each run is a GitHub Actions job ([pipeline.md](pipeline.md)). The queue is how runs are asked for, ordered and reported on.
attempt.schema.json
claims.schema.json
entry.schema.json
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s['properties']['verifications'],indent=1)[:4000])"; grep -l "verifications:" attempts/*.yaml | head -3
```

```
{
 "type": "array",
 "items": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "date",
   "kind",
   "by",
   "results"
  ],
  "properties": {
   "date": {
    "type": "string",
    "format": "date"
   },
   "kind": {
    "enum": [
     "agent",
     "person",
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A14 "^verifications:" attempts/amjad-2025-01.yaml | head -30; sed -n 330,380p tools/entry.py
```

```
287:verifications:
288-- date: '2026-10-15'
289-  kind: agent
290-  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
291-  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
292-    module and the claims file, with the paper's full text (PMC12183687). The verifier read the
293-    archive's file list and metadata through the DANDI API and tested the helpers on synthetic inputs
294-    (beta_power, burst_onsets, window_mean, codes_per_trial, rereference, fscv_window_mean, best_lag,
295-    reward_blocks). It had no attempt record and took the claims from the claims file.
296-  results:
297-  - claim: insertion-yield
298-    agrees: true
299-    outcome: blocked
300-    reason: The archive has 3 assets with sites c8dg, c3bs, c3a and cl3, and nothing about implanted
301-      or failed sensors. Figure 3 names 4 functional Monkey T sites against the paper's "3/14", so
                for d in attempt.get("datasets") or ([attempt["dataset"]] if attempt.get("dataset") else [])]
        # The rule is the protocol's from pilot-15. An attempt made under an earlier version is not held to it: its
        # agents had not been told (a chain under way when the rule reached main ended in a failed check, as
        # hazon-2022 did on 2026-11-12), and the site takes such a finding by its kind.
        version = re.fullmatch(r"pilot-(\d+)", str(((attempt.get("provenance") or {}).get("agent") or {}).get("protocol") or ""))
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "S3 Fig|learning curve|criterion" 10.1371-journal.pbio.2001045.txt | cut -c1-2500 | head -12
```

```
33:To more closely examine the nature of the animal’s spatial representation, we conducted probe sessions (9 sessions for monkey S and 15 sessions for monkey K). In these sessions, animals first started from only one or two entries (northeastern and southeastern entries) and were only later introduced from the new remaining entries (northwest and southwest). We hypothesized that if animals formed a cognitive map of the maze [ 22 ], they would successfully transfer knowledge acquired from the previous entries to the new entries (northwest and southwest). Monkey K was 73% correct after introducing the new entries versus 44% correct at beginning of the sessions; monkey S was 80% versus 55% correct ( S3C Fig , Wilcoxon, p = 0.01). Thus, after having explored the maze from entries facing eastern landmarks, animals were able to deduce goal location when entering new paths facing western landmarks. Further, performances above the learning criterion were reached significantly faster (within 4 trials for monkey K and within 2.7 trials for monkey S, compared to 14.8 and 12.3 trials; Wilcoxon, p = 0.002).
39:Of the 270 cells recorded in the full extent of the right hippocampus (128 cells in monkey S, 142 in monkey K; S4 Fig ), we focused on 189 cells that fired more than 100 spikes per session (approximately > 0.01 Hz; see S1 Appendix A3, S3 Fig , and S4 Fig ). Only successful trials were considered for analysis.
201:For each landmark neighboring the reward (northwest and northeast), we identified the five trajectories for which the landmark appeared in the FOV and computed the firing rate from –400 ms before to 500 ms after that onset with a 10 ms resolution. Then, we selected 42 cells which displayed a significant activity to either the northeastern or northwestern landmark by the following criterion: the activity evoked by the landmark had to exceed the mean baseline activity plus 2.5 times the S.D. calculated on the 400 ms baseline preceding the landmark onset. If that cri
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import re
p='wirth.py'; s=open(p).read()

# docstring updates
s=s.replace('''- Surrogates (Methods, Permutation statistics): the recording time of the new-maze session is
  cut into 5 s chunks that are "randomly shifted". Reading "permute" (claims file, Method W
  (a)): the order of the chunks of the spike train is permuted. Reading "shift" (Method W
  (b)): each chunk is moved by an independent random offset, circularly. The p-value is
  bilateral, twice the smaller tail fraction of the rank among 1,000 (claims file, a standard
  choice); one-tailed fractions are kept for the claims that count each tail.
- Trial windows (claims file, Method W): reading "full", trial start (code 21) to the next
  trial start, so the passive return after the trial belongs to it; reading "toreward",
  trial start to reward (code 11).''','''- Surrogates (Methods, Permutation statistics): the recording time of the new-maze session is
  cut into 5 s chunks that are "randomly shifted", which "decorrelated the spikes from the
  animal's behavior while essentially preserving the structure of spike trains". Reading
  "permute" (claims file, Method W (a)): the order of the chunks of the spike train is
  permuted. Reading "shift" (Method W (b), each chunk displaced by an independent random time
  shift): the spikes of each chunk are shifted circularly within the chunk by an independent
  random offset, so that chunks do not overlap and every frame keeps one source. (Moving each
  chunk by an offset over the whole session, as the first version did, piles chunks on top of
  each other and leaves frames empty; on a train without any coding its surrogates had higher
  IC than the train itself, so it was replaced; an assumption.) The p-value is bilateral,
  twice the smaller tail fraction of the rank among 1,000 (claims file, a standard choice); the
  upper and lower tail fractions are kept as well.
- Trial windows (claims file, Method W): reading "full", trial start (code 21) to the next
  trial start, so the passive return after the trial belongs to it; reading "toreward",
  trial start to reward (code 11), no return; reading "toreward_ret", trial start to reward
  plus the return (tags 5xy) that follows the trial, which drops the time from reward to the
  start of the return (the claims file's reading (b), "from trial start to reward, return
  paths taken from the returns that follow correct trials", read with the returns kept).''')
s=s.replace('''- State-space selectivity (Methods, State-space selectivity): 3.6 degree bins, three move
  types, at least 400 ms in each of at least two types. The three types are read as the 36
  degree alignment (tags 2xy), a 72 degree rotation to the right and one to the left (tags
  3xy, split by the sign of the change of camera orientation); an assumption, as the paper
  does not name them.''','''- State-space selectivity (Methods, State-space selectivity): 3.6 degree bins, three move
  types, at least 400 ms in each of at least two types. The paper does not name the three
  moves; three typings are run (an assumption each): "arc", the 36 degree alignment (tags
  2xy), a 72 degree rotation to the right and one to the left (tags 3xy, split by the sign of
  the change of camera orientation); "align_dir", the 36 degree alignment to the right, to the
  left (2xy split by sign) and the 72 degree rotation (3xy, either way); "tag", each
  transition tag of the state-space graph (2xy or 3xy) as its own move, the edges of Fig 1F
  and Fig 4A ("compared on the different state-space transitions").''')

# surrogate shift
s=s.replace('''            else:  # "shift": each chunk moved by an independent random offset, circularly
                src = np.arange(T)
                ch = np.minimum(src // L, nch)  # the remainder is one more chunk
                offs = rng.integers(0, T, size=nch + 1)
                tgt = (src + offs[ch]) % T
                out[i] = np.bincount(tgt, weights=s, minlength=T)''','''            else:  # "shift": each chunk shifted circularly within itself by its own offset
                out[i] = s[shift_index(T, L, rng)]''')
s=s.replace('''def tail_p(actual, surr):''','''def shift_index(T, L, rng):
    """Source frame of each frame when every L-frame chunk (and the shorter remainder) is
    rotated by an independent random offset within itself."""
    src = np.arange(T)
    ch = src // L
    start = ch * L
    length = np.minimum(L, T - start)
    offs = rng.integers(0, L, size=ch[-1] + 1)
    return start + (src - start + offs[ch]) % length


def tail_p(actual, surr):''')

# frame_table third reading
s=s.replace('''        else:  # "toreward"
            end = tr["t_reward"][i]
            if not np.isfinite(end):
                continue
        trial[(t >= ts[i]) & (t < end)] = i''','''        else:  # "toreward" and "toreward_ret"
            end = tr["t_reward"][i]
            if not np.isfinite(end):
                continue
            if reading == "toreward_ret":
                nxt = ts[i + 1] if i + 1 < n and np.isfinite(ts[i + 1]) else tr["t_end"][i] + 1.0
                tag = c["t60"][:, 10]
                trial[(t >= tr["t_end"][i]) & (t < nxt) & (tag >= 500) & (tag < 600)] = i
        trial[(t >= ts[i]) & (t < end)] = i''')
s=s.replace('''        self.tables = {r: frame_table(c, r) for r in ("full", "toreward")}''','''        self.tables = {r: frame_table(c, r) for r in WINDOWS}''')
s=s.replace('''SHIFTS_S = (-5.0''','''WINDOWS = ("full", "toreward", "toreward_ret")
TYPINGS = ("arc", "align_dir", "tag")
SHIFTS_S = (-5.0''')

# turn types
old_tt=s[s.index('def turn_types(c):'):s.index('class Session:')]
new_tt='''def turn_types(c, typing="arc"):
    """Per frame, the index of the rotational move at the centre (-1 elsewhere) and the number
    of move types. "arc": 0 for a 36 degree alignment (tag 2xy), 1 for a 72 degree rotation to
    the right, 2 to the left (tags 3xy). "align_dir": 0 and 1 for a 36 degree alignment to the
    right and to the left, 2 for a 72 degree rotation. "tag": one type per transition tag (2xy
    and 3xy). The side is the sign of the orientation change over the run of frames carrying
    the tag; a right turn (code 1) lowers the camera orientation, as the notebook shows."""
    tag = c["t60"][:, 10]
    th = c["t60"][:, 3]
    is2 = (tag >= 200) & (tag < 300)
    is3 = (tag >= 300) & (tag < 400)
    out = np.full(len(tag), -1)
    if typing == "tag":
        vals = np.unique(tag[is2 | is3])
        out[is2 | is3] = np.searchsorted(vals, tag[is2 | is3])
        return out, max(len(vals), 1)
    right = np.zeros(len(tag), bool)
    rot = is2 | is3
    if rot.any():
        brk = np.nonzero(np.diff(np.r_[0, rot.astype(int), 0]))[0]
        dth = np.r_[0, (np.diff(th) + 180) % 360 - 180]
        for a, b in zip(brk[::2], brk[1::2]):
            vals = tag[a:b]
            for v in np.unique(vals):  # one run per tag value
                idx = np.arange(a, b)[vals == v]
                right[idx] = dth[idx[1:]].sum() < 0
    if typing == "arc":
        out[is2] = 0
        out[is3] = np.where(right[is3], 1, 2)
    else:  # "align_dir"
        out[is2] = np.where(right[is2], 0, 1)
        out[is3] = 2
    return out, 3


'''
s=s.replace(old_tt,new_tt)

s=s.replace('''        # state-space selectivity layout: 3.6 degree bins x 3 move types, centre frames
        types = turn_types(c)
        nbin = int(round(360 / SSI_BIN_DEG))
        db = np.clip(np.floor(np.mod(self.t60[:, 3], 360) / SSI_BIN_DEG).astype(int), 0, nbin - 1)
        col = np.where(self.center & (types >= 0), db * 3 + np.maximum(types, 0), -1)
        occ = np.bincount(col[col >= 0], minlength=nbin * 3).reshape(nbin, 3) * DT
        self.ssi = {"col": col, "occ": occ, "nbin": nbin}
        self.types = types''','''        # state-space selectivity layout: 3.6 degree bins x move types, centre frames
        nbin = int(round(360 / SSI_BIN_DEG))
        db = np.clip(np.floor(np.mod(self.t60[:, 3], 360) / SSI_BIN_DEG).astype(int), 0, nbin - 1)
        self.ssi = {}
        for ty in TYPINGS:
            types, k = turn_types(c, ty)
            col = np.where(self.center & (types >= 0), db * k + np.maximum(types, 0), -1)
            occ = np.bincount(col[col >= 0], minlength=nbin * k).reshape(nbin, k) * DT
            self.ssi[ty] = {"col": col, "occ": occ, "nbin": nbin, "k": k}''')
s=s.replace('''        good = col >= 0
        self.designs["ssi"] = sparse.csr_matrix(
            (np.ones(good.sum()), (np.nonzero(good)[0], col[good])), shape=(len(col), nbin * 3))''','''        self.ssi_designs = {}
        for ty, sv in self.ssi.items():
            col = sv["col"]
            good = col >= 0
            self.ssi_designs[ty] = sparse.csr_matrix(
                (np.ones(good.sum()), (np.nonzero(good)[0], col[good])), shape=(len(col), nbin * sv["k"]))''')
s=s.replace('''    """SSI over bins with >= 400 ms in each of >= 2 move types (Methods, State-space
    selectivity); counts (..., nbin*3)."""
    nbin = occ.shape[0]
    cnt = counts.reshape(counts.shape[:-1] + (nbin, 3))''','''    """SSI over bins with >= 400 ms in each of >= 2 move types (Methods, State-space
    selectivity); counts (..., nbin*k), occ (nbin, k)."""
    nbin, k = occ.shape
    cnt = counts.reshape(counts.shape[:-1] + (nbin, k))''')

# analyse_cell
s=s.replace('''    act_ssi = s @ sess.designs["ssi"]''','''    act_ssi = {ty: s @ dm for ty, dm in sess.ssi_designs.items()}''')
s=s.replace('''    ssi_a, nb_ssi = ssi_index(act_ssi, sess.ssi["occ"])
    out["ssi"] = float(ssi_a)
    out["ssi_bins"] = nb_ssi''','''    ssi_a = {}
    for ty in TYPINGS:
        a, nb_ssi = ssi_index(act_ssi[ty], sess.ssi[ty]["occ"])
        ssi_a[ty] = float(a)
        out[f"ssi|{ty}"] = float(a)
        out[f"ssi_bins|{ty}"] = nb_ssi''')
s=s.replace('''        surr_cc, surr_ssi = [], []''','''        surr_cc, surr_ssi = [], {ty: [] for ty in TYPINGS}''')
s=s.replace('''            surr_ssi.append((sess.designs["ssi"].T @ St).T)''','''            for ty, dm in sess.ssi_designs.items():
                surr_ssi[ty].append((dm.T @ St).T)''')
s=s.replace('''                out[f"{meas}n|{k}|{sr}"] = float(a - sv.mean()) if len(sv) else np.nan
                out[f"{meas}p|{k}|{sr}"] = float(p2)''','''                out[f"{meas}n|{k}|{sr}"] = float(a - sv.mean()) if len(sv) else np.nan
                out[f"{meas}p|{k}|{sr}"] = float(p2)
                if meas == "ic":
                    out[f"icup|{k}|{sr}"], out[f"iclo|{k}|{sr}"] = float(pu), float(pl)''')
s=s.replace('''        for r in ("full", "toreward"):
            st = (r, "state")''','''        for r in WINDOWS:
            st = (r, "state")''')
s=s.replace('''        ss, _ = ssi_index(np.vstack(surr_ssi), sess.ssi["occ"])
        ss = ss[np.isfinite(ss)]
        if np.isfinite(ssi_a) and len(ss):
            p2, pu, pl = tail_p(ssi_a, ss)
            out[f"ssin|{sr}"] = float(ssi_a - ss.mean())
            out[f"ssi_up|{sr}"], out[f"ssi_lo|{sr}"] = float(pu), float(pl)''','''        for ty in TYPINGS:
            ss, _ = ssi_index(np.vstack(surr_ssi[ty]), sess.ssi[ty]["occ"])
            ss = ss[np.isfinite(ss)]
            if np.isfinite(ssi_a[ty]) and len(ss):
                p2, pu, pl = tail_p(ssi_a[ty], ss)
                out[f"ssin|{ty}|{sr}"] = float(ssi_a[ty] - ss.mean())
                out[f"ssi_up|{ty}|{sr}"], out[f"ssi_lo|{ty}|{sr}"] = float(pu), float(pl)''')

# anova type III
s=s.replace('''        fit = ols("rate ~ C(lm) * C(rd)", data=two).fit()
        tab = sm.stats.anova_lm(fit, typ=2)
    return {"p_lm": tab.loc["C(lm)", "PR(>F)"], "p_rd": tab.loc["C(rd)", "PR(>F)"],
            "p_int": tab.loc["C(lm):C(rd)", "PR(>F)"], "F_int": tab.loc["C(lm):C(rd)", "F"],
            "df_int": tab.loc["C(lm):C(rd)", "df"], "df_res": tab.loc["Residual", "df"],
            "n_lm": int(two.lm.nunique())}''','''        fit = ols("rate ~ C(lm) * C(rd)", data=two).fit()
        tab = sm.stats.anova_lm(fit, typ=2)
        # type III, MATLAB anovan's default, with sum-to-zero contrasts
        fit3 = ols("rate ~ C(lm, Sum) * C(rd, Sum)", data=two).fit()
        tab3 = sm.stats.anova_lm(fit3, typ=3)
    return {"p_lm": tab.loc["C(lm)", "PR(>F)"], "p_rd": tab.loc["C(rd)", "PR(>F)"],
            "p_int": tab.loc["C(lm):C(rd)", "PR(>F)"], "F_int": tab.loc["C(lm):C(rd)", "F"],
            "df_int": tab.loc["C(lm):C(rd)", "df"], "df_res": tab.loc["Residual", "df"],
            "p_lm3": tab3.loc["C(lm, Sum)", "PR(>F)"], "p_rd3": tab3.loc["C(rd, Sum)", "PR(>F)"],
            "p_int3": tab3.loc["C(lm, Sum):C(rd, Sum)", "PR(>F)"],
            "n_lm": int(two.lm.nunique())}''')
s=s.replace('''sex. Rates per lap''','''x''')
open(p,'w').write(s)
EOF
grep -n "anova_two\|landmark_tables(c, s, sess)" wirth.py | head
```

```
633:def anova_two(two):
800:        two, onea, oneb, heads = landmark_tables(c, s, sess)
801:        a2 = anova_two(two) or {}
807:        a2 = anova_two(two) or {}
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; grep -n "sess.types\|\.types\b\|ssi_bins\|\"ssi\"" wirth.py; python - <<'EOF'
p='wirth.py'; s=open(p).read()
s=s.replace('''def return_turns(c):''','''def eye_velocity(c, t0, t1):
    """Median horizontal eye velocity in [t0, t1), raw file units per second, of the mean of
    both eyes; saturated samples dropped. The median of the sample-to-sample velocity follows
    the slow phases of nystagmus and smooth pursuit, as quick phases and saccades are brief."""
    if c["eye"] is None:
        return np.nan
    et = c["eye_t"]
    i0, i1 = np.searchsorted(et, t0), np.searchsorted(et, t1)
    if i1 - i0 < 3:
        return np.nan
    v = np.vstack([c["eye"]["l_hor"][i0:i1], c["eye"]["r_hor"][i0:i1]]).astype(float)
    v = np.where(np.abs(v) < EYE_RAIL * c["eye_rail"], v, np.nan)
    vel = np.diff(v, axis=1) / np.diff(et[i0:i1])
    vel = np.nanmean(vel, 0)
    vel = vel[np.isfinite(vel)]
    return float(np.median(vel)) if len(vel) else np.nan


def return_turns(c):''')
s=s.replace('''            for lag in EYE_LAGS:
                row[f"lag{lag}"] = eye_mean(c, t + lag, t + lag + 0.1)''','''            for lag in EYE_LAGS:
                row[f"lag{lag}"] = eye_mean(c, t + lag, t + lag + 0.1)
            row["vel_0_600ms"] = eye_velocity(c, t, t + 0.6)
            row["vel_pre500"] = eye_velocity(c, t - 0.5, t)''')
s=s.replace('''        for which in ("mean", "l", "r"):
            r[f"eye_{which}"] = eye_mean(c, r["t0"], r["t1"], which)''','''        for which in ("mean", "l", "r"):
            r[f"eye_{which}"] = eye_mean(c, r["t0"], r["t1"], which)
        r["vel"] = eye_velocity(c, r["t0"], r["t1"])''')
s=s.replace('''    return {"monkey": c["monkey"], "session": c["session"], "n_trials": len(c["cm"]),''','''    # position at each trial start (the end of the start arm) and at reward (end of the chosen arm)
    pos = {}
    for nm, tt in (("start", tr["t_start"]), ("reward", tr["t_reward"])):
        i = np.searchsorted(t60[:, 0], np.where(np.isfinite(tt), tt, t60[0, 0]))
        i = np.minimum(i, len(t60) - 1)
        pos[nm] = np.where(np.isfinite(tt)[:, None], t60[i, 1:3], np.nan)
    return {"monkey": c["monkey"], "session": c["session"], "n_trials": len(c["cm"]),
            "pos_start": pos["start"], "pos_reward": pos["reward"],''')
s=s.replace('''    out["t60"] = t60.astype(np.float64)''','''    out["t60_shape_raw"] = t60.shape
    out["t60"] = t60.astype(np.float64)''')
s=s.replace('''    t60 = t60[keep]''','''    out_raw_cols = t60.shape[1]
    t60 = t60[keep]''')
s=s.replace('''                    "abscissa_min": float(np.nanmin(t60[:, 4])), "abscissa_max": float(np.nanmax(t60[:, 4])),''','''                    "abscissa_min": float(np.nanmin(t60[:, 4])), "abscissa_max": float(np.nanmax(t60[:, 4])),
                    "abscissa_over_1": float(np.mean(t60[:, 4] > 1.001)),
                    "t60_cols": int(c["t60_shape_raw"][1]), "t60_rows_raw": int(c["t60_shape_raw"][0]),
                    "ss_angle_min": float(np.nanmin(t60[:, 6])), "ss_angle_max": float(np.nanmax(t60[:, 6])),
                    "ss_radius_min": float(np.nanmin(t60[:, 7])), "ss_radius_max": float(np.nanmax(t60[:, 7])),
                    "tag_next_min": float(np.nanmin(t60[:, 8])), "tag_next_max": float(np.nanmax(t60[:, 8])),
                    "tag_min": float(np.nanmin(t60[:, 10])), "tag_max": float(np.nanmax(t60[:, 10])),
                    "tag_hundreds": tuple(sorted(set((t60[:, 10] // 100).astype(int)))),''')
s=s.replace('''        out["lm1b_p"], out["lm1b_groups"] = anova_one(oneb)''','''        out["lm1b_p"], out["lm1b_groups"] = anova_one(oneb)
        out["n_entry_frames_abscissa_over_1"] = int(np.sum(np.isfinite(c["t60"][:, 4]) & (c["t60"][:, 4] > 1.001)
                                                          & (sess.tag >= 100) & (sess.tag < 200)))''')
open(p,'w').write(s)
EOF
grep -n "out_raw_cols\|t60_shape_raw" wirth.py
```

```
517:        out[f"ssi_bins|{ty}"] = nb_ssi
137:    out_raw_cols = t60.shape[1]
140:    out["t60_shape_raw"] = t60.shape
803:                    "t60_cols": int(c["t60_shape_raw"][1]), "t60_rows_raw": int(c["t60_shape_raw"][0]),
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
p='wirth.py'; s=open(p).read()
s=s.replace('''    out_raw_cols = t60.shape[1]
    t60 = t60[keep]''','''    out["t60_shape_raw"] = t60.shape
    t60 = t60[keep]''')
s=s.replace('''    out["t60_shape_raw"] = t60.shape
    out["t60"] = t60.astype(np.float64)''','''    out["t60"] = t60.astype(np.float64)''')
open(p,'w').write(s)
EOF
sed -n 118,145p wirth.py; ls; cat requirements.in; which python; python -c "import statsmodels, fsspec; print('ok')"
```

```
Exit code 1
    if cd is None:
        cd = _field(mz, "camera_data")
    t60 = np.asarray(cd[0, 0]["time_60"], float)
    cm = np.asarray(mz["codematrix"], float)
    tm = np.asarray(mz["timematrix"], float)
    lc = _field(mz, "learning_curves")
    lt = _field(mz, "learningtrial")
    out = {"name": name, "monkey": name[:2], "session": name.split("_")[0],
           "spikes": np.sort(np.asarray(el, float).ravel()), "spike_src": spike_src,
           "cm": cm, "tm": tm,
           "lc": None if lc is None else np.asarray(lc, float),
           "learningtrial": None if lt is None or lt.size == 0 else float(lt.ravel()[0]),
           "reclocation": None if _field(fl, "reclocation") is None
           else np.asarray(fl["reclocation"], float).ravel()}
    # session window: first trial start to last trial end (as the dataset's scripts do)
    t0 = _code_times(cm, tm, 21)
    t0 = np.nanmin(t0)
    t1 = np.nanmax(np.where(cm[:, 1:] > 0, tm[:, 1:], np.nan))
    keep = (t60[:, 0] >= t0) & (t60[:, 0] <= t1 + 1.0) & np.isfinite(t60[:, 10])
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "venv\|def cmd_run\|def run" tools/entry.py | head -20; ls -a ~/.cache 2>/dev/null | head; ls -d .venv* /tmp/*venv* $TMPDIR/* 2>/dev/null | head
```

```
513:        if any(part in ("__pycache__", ".ipynb_checkpoints", ".venv") or part.endswith(".pyc") for part in rel.parts):
537:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
549:    venv = (output_dir / ".venv").resolve()
550:    python = venv / "bin" / "python"
554:    for cmd in (["uv", "venv", "--quiet", "--clear", "--python", python_of(entry_dir), str(venv)],
557:                [str(python), "-m", "ipykernel", "install", "--prefix", str(venv), "--name", kernel]):
571:            env={**os.environ, "JUPYTER_PATH": str(venv / "share" / "jupyter")})
/tmp/claude-1001/-home-runner-work--temp
/tmp/claude-1001/-home-runner-work-encore-encore
/tmp/claude-1001/bash-edit-diff
```

**Agent calls Bash**

```bash
cd  ls -a executed/wirth-2017/; sed -n 537,600p tools/entry.py
```

```
.
..
.clean-run.json
.venv
reproduce_wirth_2017.ipynb
result.json
def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
    entry = yaml.safe_load((entry_dir / "entry.yaml").read_text())
    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
    if stamp:
        when = time.strftime("%Y-%m-%d %H:%M UTC", time.gmtime(stamp["finished"]))
        for r in stamp["results"]:
            print(f"pass  {r['notebook']}  ({r['seconds']} s, reused)")
        print(f"reused the executed copies of {when}: nothing the run reads has changed since (hash "
              f"{stamp['hash'][:12]}). Nothing was executed and no environment was built; --fresh runs it again.")
        return 0
    (output_dir / STAMP).unlink(missing_ok=True)   # whatever is there is no longer what a run left
    output_dir.mkdir(parents=True, exist_ok=True)
    venv = (output_dir / ".venv").resolve()
    python = venv / "bin" / "python"
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; PY=executed/wirth-2017/.venv/bin/python; date -u; timeout 900 $PY - <<'EOF'
import time, resource, pickle, os
import numpy as np
import wirth
t=time.time()
metas, cells, beh = wirth.collect("hc-12", limit=6, log=print)
print("time", time.time()-t, "maxrss GB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
pickle.dump((metas,cells,beh), open(os.environ["TMPDIR"]+"/sub.pkl","wb"))
import pandas as pd
C=pd.DataFrame(cells); M=pd.DataFrame(metas)
print(M[["file","t60_cols","t60_rows_raw","abscissa_max","abscissa_over_1","theta_min","theta_max","ss_radius_min","ss_radius_max","tag_min","tag_max","tag_hundreds"]].to_string())
print([c for c in C.columns if c.startswith("ssi") or "icup" in c][:20])
print(C[[c for c in C.columns if c.startswith("icp|")]].round(3).to_string())
print(C[[c for c in C.columns if c.startswith("ssi_up") or c.startswith("ssi_bins")]].round(3).to_string())
b=list(beh.values())[0]
T=pd.DataFrame(b["turns"]); print(T.groupby("code")[["vel_0_600ms","vel_pre500"]].median())
R=pd.DataFrame(b["returns"]); print(R.groupby(R.dtheta<0).vel.median())
print(b["pos_start"][:5], b["pos_reward"][:5])
EOF
date -u
```

```
Fri Nov 13 14:54:15 UTC 2026
entries/wirth-2017/wirth.py:607: RuntimeWarning: overflow encountered in multiply
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:607: RuntimeWarning: invalid value encountered in cast
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:607: RuntimeWarning: overflow encountered in multiply
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:607: RuntimeWarning: invalid value encountered in cast
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:607: RuntimeWarning: overflow encountered in multiply
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:607: RuntimeWarning: invalid value encountered in cast
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:607: RuntimeWarning: overflow encountered in multiply
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:607: RuntimeWarning: invalid value encountered in cast
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:607: RuntimeWarning: overflow encountered in multiply
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:607: RuntimeWarning: invalid value encountered in cast
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def setsrc(i, text): cells[i]['source']=text.splitlines(keepends=True)
def code(text, tags=None):
    c={"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":text.splitlines(keepends=True)}
    if tags: c["metadata"]["tags"]=tags
    return c
def md(text):
    return {"cell_type":"markdown","metadata":{},"source":text.splitlines(keepends=True)}
# sanity: layout checks appended to cell 6
assert src(6).startswith('print("Files by monkey')
setsrc(6, src(6) + '''
print("\\nCamera-data layout: columns of time_60 per file:", M.t60_cols.value_counts().to_dict())
print("Transition tag (column 11) over files:", M.tag_min.min(), "to", M.tag_max.max(),
      "; hundreds present per file:", M.tag_hundreds.value_counts().to_dict())
print("Next tag (column 9) over files:", M.tag_next_min.min(), "to", M.tag_next_max.max())
print("State-space radius (column 8) over files:", round(M.ss_radius_min.min(), 3), "to", round(M.ss_radius_max.max(), 3),
      "; polar angle (column 7):", round(M.ss_angle_min.min(), 3), "to", round(M.ss_angle_max.max(), 3))
print("Camera orientation range per file, sessions by (min, max) rounded to 90 deg:",
      M.dropna(subset=["theta_min"]).drop_duplicates("session").apply(
          lambda r: (int(90 * round(r.theta_min / 90)), int(90 * round(r.theta_max / 90))), axis=1).value_counts().to_dict())
odd = M[(M.abscissa_max > 1.001) | ((M.theta_max - M.theta_min) < 300)]
print("\\nFiles with an abscissa above 1 or an orientation range under 300 deg:")
print(odd[["file", "abscissa_max", "abscissa_over_1", "theta_min", "theta_max", "n_trials"]].round(4).to_string())
print("Entry-path frames with abscissa above 1, over the cells of these files:",
      C_all.set_index("name").reindex(odd.file).n_entry_frames_abscissa_over_1.to_dict())
''')
# learning: add ub at crit
s17=src(17)
s17=s17.replace('''                 "t90": (up[0] + 1 - crit) if up else np.nan, "pc": b["correct"].mean()})''','''                 "t90": (up[0] + 1 - crit) if up else np.nan, "pc": b["correct"].mean(),
                 "ub_at_crit": lc[int(crit) - 1, 2] if np.isfinite(crit) else np.nan})''')
setsrc(17,s17)
setsrc(20, src(20)+'''print("\\nSessions where the upper bound is already at 0.9 or above at the criterion trial (0 trials):", int((S.t90 == 0).sum()),
      "; trials to 0.9 per session:", S.t90.value_counts().sort_index().to_dict())
print("Upper bound at the criterion trial, quartiles:", S.ub_at_crit.quantile([0.25, 0.5, 0.75]).round(3).to_dict())
print("Variant with the 0-trial sessions left out:", f"{int(((S.t90 > 0) & (S.t90 < 10)).sum())} of {int((S.t90 > 0).sum())}",
      f"= {((S.t90 > 0) & (S.t90 < 10)).sum() / (S.t90 > 0).sum():.3f}")
''')
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def setsrc(i, text): cells[i]['source']=text.splitlines(keepends=True)
assert 'claim:probe-transfer' in cells[23]['metadata'].get('tags',[])
setsrc(23, '''def arm_angles(b):
    """Angle of each start arm relative to the rewarded arm, degrees, negative = clockwise seen from
    above (x east, y north, as a right turn lowers the camera orientation): with the reward north,
    the eastern entries are at -72 (northeast) and -144 (southeast)."""
    ang = np.degrees(np.arctan2(b["pos_start"][:, 1], b["pos_start"][:, 0]))
    rew = b["pos_reward"][b["correct"]]
    ra = np.degrees(np.arctan2(np.nanmedian(rew[:, 1]), np.nanmedian(rew[:, 0])))
    out = {}
    for a in np.unique(b["start_arm"][np.isfinite(b["start_arm"])]).astype(int):
        m = b["start_arm"] == a
        out[a] = int(round(((np.nanmedian(ang[m]) - ra + 180) % 360) - 180))
    return out


P = S[S.probe].copy()
P["arm_rel_deg"] = [arm_angles(beh[s]) for s in P.session]
P["first_rel"] = [sorted(a[x] for x in f) for a, f in zip(P.arm_rel_deg, P.first_arms)]
P["eastern_first"] = P.first_rel.apply(lambda v: all(-150 <= x <= -60 for x in v))
P["pc_first5"] = [beh[s]["correct"][:5].mean() for s in P.session]
P["pc_after5"] = [beh[s]["correct"][int(i):int(i) + 5].mean() for s, i in zip(P.session, P.intro)]
P["pc_new5"] = [beh[s]["correct"][[k for k in range(int(i), beh[s]["n_trials"]) if beh[s]["start_arm"][k] not in f][:5]].mean()
                for s, i, f in zip(P.session, P.intro, P.first_arms)]
P["starts"] = ["".join(str(int(a)) if np.isfinite(a) else "." for a in beh[s]["start_arm"][:50]) for s in P.session]
print(P[["session", "monkey", "n_trials", "first_arms", "first_rel", "intro", "pc_first5", "pc_after5", "pc_new5"]].to_string())
print("\\nStart arms of the first 50 trials:")
print(P[["session", "starts"]].to_string(index=False))
print("\\nProbe sessions per monkey:", P.groupby("monkey").size().to_dict(), "(paper: 9 for S, 15 for K)")
print("Sessions of monkey S whose first 10 trials use at most two entries:",
      int(((S.monkey == "sn") & S.first_arms.apply(len).le(2)).sum()))
variants = (("(i) all 12, 5 trials from the introduction", P, "pc_after5"),
            ("(ii) all 12, the first 5 trials from a new entry", P, "pc_new5"),
            ("(iii) first entries eastern, 5 trials from the introduction", P[P.eastern_first], "pc_after5"),
            ("(iv) introduction after trial 20, 5 trials from it", P[P.intro >= 20], "pc_after5"))
for nm, d, col in variants:
    w = stats.wilcoxon(d[col], d.pc_first5) if len(d) > 1 else None
    print(f"{nm}: {len(d)} sessions, first 5 {100 * d.pc_first5.mean():.1f}%, after {100 * d[col].mean():.1f}%,",
          f"Wilcoxon signed-rank p = {w.pvalue:.4f}" if w else "")
print("\\nExpected: K 73 +- 7.3 after, 44 +- 4.4 at the start; S 80 +- 8, 55 +- 5.5")
# hc-21: sessions whose first 10 start codes use at most two entries
fp21m["first_arms"] = fp21m.codes_head.apply(lambda c: sorted(set(c)))
p21 = fp21m[fp21m.first_arms.apply(len) <= 2].drop_duplicates("session")
print("hc-21 new-maze sessions whose first 10 trials use at most two entries:", p21.session.tolist())
''')
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def setsrc(i, text): cells[i]['source']=text.splitlines(keepends=True)
def code(text, tags=None):
    c={"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":text.splitlines(keepends=True)}
    if tags: c["metadata"]["tags"]=tags
    return c
s=src(23).replace('''beh[s]["correct"][[k for k in range(int(i), beh[s]["n_trials"]) if beh[s]["start_arm"][k] not in f][:5]].mean()''','''beh[s]["correct"][[k for k in range(int(i), beh[s]["n_trials"])
                                      if np.isfinite(beh[s]["start_arm"][k]) and int(beh[s]["start_arm"][k]) not in f][:5]].mean()''')
setsrc(23,s)
# gaze action: session-level test
s=src(27)
s=s.replace('''                res.append({"trials": trials_used, "window": w[3:] + " ms", "eye": eye, "monkey": mk,
                            "n_right": na, "n_left": nb, "median z right-left": round(diff, 3), "p": p,
                            "sessions right<left": f"{int((sess_diff < 0).sum())}/{len(sess_diff)}"})''','''                res.append({"trials": trials_used, "window": w[3:] + " ms", "eye": eye, "monkey": mk,
                            "n_right": na, "n_left": nb, "median z right-left": round(diff, 3), "p": p,
                            "sessions right<left": f"{int((sess_diff < 0).sum())}/{len(sess_diff)}",
                            "session signed-rank p": stats.wilcoxon(sess_diff).pvalue})''')
setsrc(27,s)
# velocity check cell inserted after 27
vel = code('''# Sign of the eye signal from the slow phases: during a turn the scene flows across the screen
# opposite to the turn, and the slow phases of optokinetic nystagmus and pursuit follow it. The
# median of the sample-to-sample velocity over 0 to 600 ms from the code follows the slow phases.
rows = []
for mk in ("ke", "sn"):
    d = Tc[Tc.monkey == mk].copy()
    for col in ("vel_0_600ms", "vel_pre500"):
        d["zv"] = d[col] / d.groupby("session")[col].transform("std")
        diff, p, na, nb = rank_test(d, "zv", d.code == 1)
        sd = d.groupby("session").apply(lambda g: g[g.code == 1][col].median() - g[g.code == 2][col].median()).dropna()
        rows.append({"monkey": mk, "window": {"vel_0_600ms": "0 to 600 ms after the code", "vel_pre500": "500 ms before"}[col],
                     "median right": round(d[d.code == 1].zv.median(), 3), "median left": round(d[d.code == 2].zv.median(), 3),
                     "p": p, "sessions right>left": f"{int((sd > 0).sum())}/{len(sd)}", "session signed-rank p": stats.wilcoxon(sd).pvalue})
print("Median horizontal eye velocity (session SD units), right (code 1) and left (code 2) turns, successful trials:")
print(pd.DataFrame(rows).to_string())
''')
cells.insert(28, vel)
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
for i,c in enumerate(cells[26:34]): print(i+26, c['cell_type'], ''.join(c['source'])[:80].replace('\n',' | '))
EOF
```

```
26 code T = pd.DataFrame([dict(session=s, monkey=b["monkey"], **t) for s, b in beh.items
27 code res = [] | for trials_used, Tsub in (("successful", T[T.correct]), ("all", T)): |   
28 code # Sign of the eye signal from the slow phases: during a turn the scene flows acr
29 markdown Sign of the eye signal. The files do not say which sign of the horizontal signal
30 markdown ## gaze-anticipates-landmarks |  | > When relocated to a new entry, the monkeys gaze
31 code Rt = pd.DataFrame([dict(session=s, monkey=b["monkey"], **r) for s, b in beh.item
32 markdown **Result: reproduced, resting on the assumed sign of the eye signal.** During pa
33 markdown ## Information content in the coding spaces |  | The point-of-gaze space needs the g
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def setsrc(i, text): cells[i]['source']=text.splitlines(keepends=True)
cells[28]['metadata']['tags']=['claim:gaze-anticipates-action']
s=src(31)
s=s.replace('''            res.append({"returns": trials_used, "eye": eye, "monkey": mk, "n_right": na, "n_left": nb,
                        "median z right-left": round(diff, 3), "p": p, "sessions right<left": f"{int((sd < 0).sum())}/{len(sd)}"})''','''            res.append({"returns": trials_used, "eye": eye, "monkey": mk, "n_right": na, "n_left": nb,
                        "median z right-left": round(diff, 3), "p": p, "sessions right<left": f"{int((sd < 0).sum())}/{len(sd)}",
                        "session signed-rank p": stats.wilcoxon(sd).pvalue})''')
s+='''vrows = []
for mk in ("ke", "sn"):
    d = Rt[Rt.monkey == mk].copy()
    d["zv"] = d.vel / d.groupby("session").vel.transform("std")
    diff, p, na, nb = rank_test(d, "zv", d.dtheta < 0)
    sd = d.groupby("session").apply(lambda g: g[g.dtheta < 0].vel.median() - g[g.dtheta >= 0].vel.median()).dropna()
    vrows.append({"monkey": mk, "median right": round(d[d.dtheta < 0].zv.median(), 3), "median left": round(d[d.dtheta >= 0].zv.median(), 3),
                  "p": p, "sessions right>left": f"{int((sd > 0).sum())}/{len(sd)}"})
print("\\nMedian horizontal eye velocity over the return (session SD units), right- and left-turning returns, all returns:")
print(pd.DataFrame(vrows).to_string())
'''
setsrc(31,s)
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
for i,c in enumerate(cells[33:]): print(i+33, c['cell_type'], c['metadata'].get('tags',''), ''.join(c['source'])[:70].replace('\n',' | '))
EOF
```

```
33 markdown  ## Information content in the coding spaces |  | The point-of-gaze space n
34 code  READINGS = [("full", "permute"), ("full", "shift"), ("toreward", "perm
35 markdown  ## responsive-cells (blocked) and state-space-most-responsive |  | > 111 o
36 code ['claim:state-space-most-responsive'] print("Cells with significant state-space IC (p < 0.01), per reading, 
37 markdown  **Result: not reproduced.** The state-space count is 57 of 186 cells u
38 markdown  ## direction-center-vs-periphery |  | > For direction-selective cells, bot
39 code ['claim:direction-center-vs-periphery'] dir_rows = [] | for sr in ("permute", "shift"): |     for cellset, mask in
40 markdown  **Result: not reproduced.** For the 40 direction-selective cells (read
41 markdown  ## direction-tuning-not-maintained |  | > Direction tuning was not maintai
42 code ['claim:direction-tuning-not-maintained'] rows = [] | for sr in ("permute", "shift"): |     for cellset, mask in (("
43 markdown  **Result: partially reproduced.** Among the 40 direction-selective cel
44 markdown  ## sparsity-state-vs-direction and sparsity-state-vs-position |  | > Spars
45 code  def sparsity_compare(other): |     rows = [] |     for r, sr in READINGS: | 
46 code ['claim:sparsity-state-vs-direction'] print(sparsity_compare("direction").to_string())
47 markdown  **Result: reproduced under the main reading only.** For the 40 cells s
48 code ['claim:sparsity-state-vs-position'] print(sparsity_compare("position").to_string()) | print("Expected: overa
49 markdown  **Result: not reproduced.** Under the main reading state space is sign
50 markdown  ## state-space-selectivity |  | > In the maze center, at the same position
51 code ['claim:state-space-selectivity'] rows = [] | for r, sr in READINGS: |     resp3 = sum(sig(k, r, sr).astype(
52 markdown  **Result: not reproduced.** The paper's responsive set contains the th
[... 10 more lines not kept]
```

**Agent**

Now the IC sections: six readings, tail p, the synthetic surrogate check, state-space-ic-higher, SSI typings, type III ANOVA.

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def setsrc(i, text): cells[i]['source']=text.splitlines(keepends=True)
def code(text, tags=None):
    c={"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":text.splitlines(keepends=True)}
    if tags: c["metadata"]["tags"]=tags
    return c
def md(text):
    return {"cell_type":"markdown","metadata":{},"source":text.splitlines(keepends=True)}

setsrc(33, '''## Information content in the coding spaces

The point-of-gaze space needs the gaze direction in degrees, which the files cannot give (the
eye signal is uncalibrated, data check). Position, direction and state space are computed for
the cells with more than 100 spikes in the new-maze session. Readings: trial window "full"
(start to next start), "toreward" (start to reward, no return) or "toreward_ret" (start to
reward plus the return that follows); surrogates "permute" (chunk order permuted) or "shift"
(each 5 s chunk rotated within itself by its own random offset) (Method W). Significance is the
bilateral surrogate p < 0.01; the upper tail alone is shown as a variant. The responsive set of
the paper needs all four spaces; the set responsive in the three spaces here is contained in
it, and all cells contain it, so counts over these two sets bound the count over the paper's set.

The surrogates are first checked on synthetic spike trains that code nothing: a homogeneous
Poisson train on a smooth random trajectory over 200 bins. A valid surrogate gives about 1% of
such trains p < 0.01. The first version of the "shift" reading, which moved each chunk by an
offset over the whole session so that chunks overlapped, is run alongside for comparison.''')

synth = code('''def shift_overlapping(s, rng, L=300):
    """The first version of the "shift" reading: each chunk moved by an independent offset
    over the whole session, circularly, so that chunks overlap (replaced)."""
    T = len(s)
    src = np.arange(T)
    ch = src // L
    tgt = (src + rng.integers(0, T, size=ch[-1] + 1)[ch]) % T
    return np.bincount(tgt, weights=s, minlength=T)


rng = np.random.default_rng(2017)
T = 60 * 600                                             # 10 min of 60 Hz frames
walk = np.cumsum(rng.normal(0, 1, T))
walk = np.convolve(walk, np.ones(120) / 120, "same")     # a smooth trajectory
b = np.clip(((walk - walk.min()) / np.ptp(walk) * 200).astype(int), 0, 199)
occ = np.bincount(b, minlength=200) * wirth.DT
valid = occ > 0
rows = []
for name in ("permute", "shift", "shift, overlapping chunks (replaced)"):
    ps, ratio = [], []
    for k in range(60):
        s = rng.poisson(2.0 * wirth.DT, T).astype(float)
        a = wirth.skaggs_ic(np.bincount(b, weights=s, minlength=200)[valid], occ[valid])
        if name.startswith("shift, overlapping"):
            surr = np.vstack([shift_overlapping(s, rng) for _ in range(999)])
        else:
            surr = np.vstack(list(wirth.surrogate_counts(s, rng, name)))
        ic_s = wirth.skaggs_ic(np.stack([np.bincount(b, weights=x, minlength=200)[valid] for x in surr]), occ[valid])
        ps.append(wirth.tail_p(a, ic_s)[0])
        ratio.append(ic_s.mean() / a)
    ps = np.array(ps)
    rows.append({"surrogates": name, "trains": len(ps), "mean surrogate IC / actual IC": round(float(np.mean(ratio)), 3),
                 "fraction p < 0.01": float(np.mean(ps < 0.01)), "fraction p < 0.05": float(np.mean(ps < 0.05))})
print("Synthetic Poisson trains (2 Hz, no coding), 999 surrogates each:")
print(pd.DataFrame(rows).to_string())
''', ['sanity'])
cells.insert(34, synth)
# cell 35 is old 34 READINGS
s=src(35)
s=s.replace('''READINGS = [("full", "permute"), ("full", "shift"), ("toreward", "permute"), ("toreward", "shift")]''','''READINGS = [(r, sr) for r in wirth.WINDOWS for sr in ("permute", "shift")]''')
s=s.replace('''def sig(space, r, sr, alpha=0.01):
    return C[f"icp|('{r}', '{space}')|{sr}"] < alpha''','''def sig(space, r, sr, alpha=0.01, tail="two"):
    """IC significant: bilateral surrogate p (tail "two") or upper tail alone ("up")."""
    return C[f"{'icp' if tail == 'two' else 'icup'}|('{r}', '{space}')|{sr}"] < alpha''')
s=s.replace('''                 "cells": len(C)})''','''                 "cells": len(C), "state, upper tail": int(sig("state", r, sr, tail="up").sum()),
                 "any of three, upper tail": int((sum(sig(k, r, sr, tail="up").astype(int) for k in SPACES) > 0).sum()),
                 "state, low side (lower tail < 0.005)": int((C[f"iclo|('{r}', 'state')|{sr}"] < 0.005).sum())})''')
setsrc(35,s)
# state-space-most-responsive cell (37)
s=src(37)
s=s.replace('''print("One-sided variant (upper tail p < 0.01, i.e. bilateral p < 0.02), state space:",
      [int(sig("state", r, sr, 0.02).sum()) for r, sr in READINGS])''','''print("Upper tail alone (p < 0.01), state space:", [int(sig("state", r, sr, tail="up").sum()) for r, sr in READINGS])''')
setsrc(37,s)
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
for i,c in enumerate(cells[33:]): print(i+33, c['cell_type'], c['metadata'].get('tags',''), ''.join(c['source'])[:70].replace('\n',' | '))
EOF
```

```
33 markdown  ## Information content in the coding spaces |  | The point-of-gaze space n
34 code ['sanity'] def shift_overlapping(s, rng, L=300): |     """The first version of the 
35 code  READINGS = [(r, sr) for r in wirth.WINDOWS for sr in ("permute", "shif
36 markdown  ## responsive-cells (blocked) and state-space-most-responsive |  | > 111 o
37 code ['claim:state-space-most-responsive'] print("Cells with significant state-space IC (p < 0.01), per reading, 
38 markdown  **Result: not reproduced.** The state-space count is 57 of 186 cells u
39 markdown  ## direction-center-vs-periphery |  | > For direction-selective cells, bot
40 code ['claim:direction-center-vs-periphery'] dir_rows = [] | for sr in ("permute", "shift"): |     for cellset, mask in
41 markdown  **Result: not reproduced.** For the 40 direction-selective cells (read
42 markdown  ## direction-tuning-not-maintained |  | > Direction tuning was not maintai
43 code ['claim:direction-tuning-not-maintained'] rows = [] | for sr in ("permute", "shift"): |     for cellset, mask in (("
44 markdown  **Result: partially reproduced.** Among the 40 direction-selective cel
45 markdown  ## sparsity-state-vs-direction and sparsity-state-vs-position |  | > Spars
46 code  def sparsity_compare(other): |     rows = [] |     for r, sr in READINGS: | 
47 code ['claim:sparsity-state-vs-direction'] print(sparsity_compare("direction").to_string())
48 markdown  **Result: reproduced under the main reading only.** For the 40 cells s
49 code ['claim:sparsity-state-vs-position'] print(sparsity_compare("position").to_string()) | print("Expected: overa
50 markdown  **Result: not reproduced.** Under the main reading state space is sign
51 markdown  ## state-space-selectivity |  | > In the maze center, at the same position
52 code ['claim:state-space-selectivity'] rows = [] | for r, sr in READINGS: |     resp3 = sum(sig(k, r, sr).astype(
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def setsrc(i, text): cells[i]['source']=text.splitlines(keepends=True)
def code(text, tags=None):
    c={"cell_type":"code","execution_count":None,"metadata":{},"outputs":[],"source":text.splitlines(keepends=True)}
    if tags: c["metadata"]["tags"]=tags
    return c
def md(text):
    return {"cell_type":"markdown","metadata":{},"source":text.splitlines(keepends=True)}
# SSI cell 52
assert 'claim:state-space-selectivity' in cells[52]['metadata']['tags']
setsrc(52, '''rows = []
for ty in wirth.TYPINGS:
    for r, sr in READINGS:
        resp3 = sum(sig(k, r, sr).astype(int) for k in SPACES) > 0
        for cellset, mask in (("three-space responsive", resp3), ("all cells", pd.Series(True, index=C.index))):
            d = C[mask & C[f"ssi_up|{ty}|{sr}"].notna()]
            hi = int((d[f"ssi_up|{ty}|{sr}"] <= 0.05).sum())
            lo = int((d[f"ssi_lo|{ty}|{sr}"] <= 0.05).sum())
            rows.append({"moves": ty, "trials (responsive set)": r, "surrogates": sr, "cells": cellset, "n": len(d), "high": hi, "low": lo,
                         "p binom high": wirth.binom_upper(hi, len(d), 0.05), "p binom low": wirth.binom_upper(lo, len(d), 0.05)})
SSI = pd.DataFrame(rows)
print(SSI.to_string())
for ty in wirth.TYPINGS:
    print(f"Moves {ty}: cells without an SSI {int(C[f'ssi|{ty}'].isna().sum())}, bins entering the SSI, median {C[f'ssi_bins|{ty}'].median()}")
print("Expected: high 12 +- 1.2 (11 to 13) with binomial p < 0.05; low 3 to 5, not significant")
bounds = SSI.pivot_table(index=["moves", "trials (responsive set)", "surrogates"], columns="cells", values=["high", "low"])
bounds["high can be 11 to 13"] = (bounds[("high", "three-space responsive")] <= 13) & (bounds[("high", "all cells")] >= 11)
bounds["low can be 3 to 5"] = (bounds[("low", "three-space responsive")] <= 5) & (bounds[("low", "all cells")] >= 3)
print("\\nCan the counts over the paper's responsive set (between the two rows) meet the criterion?")
print(bounds.to_string())
''')
# LM cell 56: type III
s=src(56)
s=s.replace('''    return {"laps": laps, "n": len(d), "identity": int(lmk.sum()), "distance": int(rd.sum()), "interaction": int(it.sum()),''','''    t3 = {f"{nm}, type III": int((d[f"{k2}_{c}3"] < a).sum()) for nm, c in (("identity", "p_lm"), ("distance", "p_rd"), ("interaction", "p_int"))}
    return {"laps": laps, "n": len(d), "identity": int(lmk.sum()), "distance": int(rd.sum()), "interaction": int(it.sum()), **t3,''')
setsrc(56,s)
# state-space-ic-higher section after cell 50
sec = [md('''## state-space-ic-higher

> Spike information content was systematically higher in state space than in position,
> direction or point-of-gaze space, for cells responsive in both spaces compared.

Cells with significant IC in state space and in the other space; per cell normalized state-space
IC minus the other space's; Wilcoxon signed-rank. The comparison with the point-of-gaze space
cannot be made (no gaze calibration); the other two are shown under every reading.'''),
code('''rows = []
for r, sr in READINGS:
    for other in ("position", "direction"):
        both = sig("state", r, sr) & sig(other, r, sr)
        d = C[both]
        diff = d[f"icn|('{r}', 'state')|{sr}"] - d[f"icn|('{r}', '{other}')|{sr}"]
        w = stats.wilcoxon(diff) if len(diff) > 1 else None
        rows.append({"trials": r, "surrogates": sr, "other space": other, "cells in both": len(d),
                     "median diff": round(diff.median(), 4), "state higher": int((diff > 0).sum()),
                     "p": w.pvalue if w else np.nan})
ICH = pd.DataFrame(rows)
print(ICH.to_string())
print("Criterion: positive with p < 0.01; partially reproduced for two of the three comparisons")
''', ['claim:state-space-ic-higher'])]
cells[51:51]=sec
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
for i,c in enumerate(cells[50:]): print(i+50, c['cell_type'], c['metadata'].get('tags',''), ''.join(c['source'])[:70].replace('\n',' | '))
EOF
```

```
50 markdown  **Result: not reproduced.** Under the main reading state space is sign
51 markdown  ## state-space-ic-higher |  | > Spike information content was systematical
52 code ['claim:state-space-ic-higher'] rows = [] | for r, sr in READINGS: |     for other in ("position", "direct
53 markdown  ## state-space-selectivity |  | > In the maze center, at the same position
54 code ['claim:state-space-selectivity'] rows = [] | for ty in wirth.TYPINGS: |     for r, sr in READINGS: |         
55 markdown  **Result: not reproduced.** The paper's responsive set contains the th
56 markdown  ## landmark-identity-distance and landmark-identity-center |  | > A two-wa
57 markdown  Which laps enter is read two ways. Method W takes successful trials on
58 code  def lm_counts(d, laps): |     a = 0.05 |     k2, k1 = ("lm2", "lm1") if la
59 code ['claim:landmark-identity-distance'] print(LM.drop(columns=["centre one-way (a)", "centre one-way (b)"]).to
60 markdown  **Result: not reproduced.** With successful laps, at most 24 cells (al
61 code ['claim:landmark-identity-center'] print(LM[["responsive set", "laps", "n", "centre one-way (a)", "centre
62 markdown  **Result: blocked (metadata insufficient).** Over the three-space resp
63 markdown  ## Claims blocked by the missing gaze calibration: three-space results
64 code  r, sr = "full", "permute" | resp3 = sum(sig(k, r, sr).astype(int) for k 
65 markdown  ## Summary |  | | Claim | Outcome | | |---|---| | | gaze-anticipates-action |
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
def setsrc(i, text): cells[i]['source']=text.splitlines(keepends=True)
assert ''.join(cells[64]['source']).startswith('r, sr = "full"')
setsrc(64, '''rows = []
for r, sr in READINGS:
    resp3 = sum(sig(k, r, sr).astype(int) for k in SPACES) > 0
    pos = sig("position", r, sr)
    rows.append({"trials": r, "surrogates": sr, "responsive in three spaces": int(resp3.sum()),
                 "two or more spaces": int((sum(sig(k, r, sr).astype(int) for k in SPACES) >= 2).sum()),
                 "position IC p < 0.01": int(pos.sum()), "(a) position cells among all": round(pos.mean(), 3),
                 "(b) responsive among all, at least": round(resp3.mean(), 3),
                 "(c) position among responsive, from": round(pos.sum() / len(C), 3),
                 "(c) to": round(pos.sum() / max(resp3.sum(), 1), 3)})
print(f"{len(C)} cells. spatial-selectivity-fraction expects 0.5 +- 0.05 under one of (a), (b), (c):")
print(pd.DataFrame(rows).to_string())
''')
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
EOF
date -u
```

```
Fri Nov 13 14:56:52 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; mkdir -p $TMPDIR/nbtest; cp wirth.py $TMPDIR/nbtest/; python - <<'EOF'
import json, os
nb=json.load(open('reproduce_wirth_2017.ipynb'))
c3=''.join(nb['cells'][3]['source'])
pre='''import itertools
_orig = wirth.stream_members
def _sub(ds):
    for i, x in enumerate(_orig(ds)):
        if (ds == "hc-12" and i % 6 in (0, 1)) or (ds == "hc-21" and i < 6):
            yield x
wirth.stream_members = _sub
'''
nb['cells'][3]['source']=(pre+c3).splitlines(keepends=True)
# speed: fewer synthetic trains
c34=''.join(nb['cells'][34]['source']).replace('range(60)','range(6)')
nb['cells'][34]['source']=c34.splitlines(keepends=True)
json.dump(nb,open(os.environ['TMPDIR']+'/nbtest/t.ipynb','w'),indent=1)
EOF
cd $TMPDIR/nbtest; date -u; timeout 2400 executed/wirth-2017/.venv/bin/python -m jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=2400 --output out.ipynb t.ipynb 2>&1 | tail -3; date -u
```

```
Fri Nov 13 14:57:06 UTC 2026
  _validate(nbdict, ref, version, version_minor, relax_add_props)
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 122736 bytes to out.ipynb
Fri Nov 13 15:09:46 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/nbtest; python - <<'EOF'
import json
nb=json.load(open('out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    out=''
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error': out+='ERROR '+o['ename']+': '+o['evalue']+'\n'
        elif 'text' in o: out+=''.join(o['text'])
        elif 'data' in o: out+=''.join(o['data'].get('text/plain',''))
    print(f"=== [{i}]"); print(out[:3000])
EOF
```

```
=== [1]

=== [3]
hc-12 pass: 605 s, peak memory 1.16 GB

=== [4]
hc-21 pass: 145 s, 6 files

=== [6]
Files by monkey (ke = monkey K, sn = monkey S):
        files  with_new_maze  sessions
monkey                                
ke         34             34        22
sn         30             28        14

Files without a new-maze (newallo) field: ['sn20121015_HPC_e2_c1a_seg.mat', 'sn20121015_HPC_e2_c1c_seg.mat']

Spike times taken from: {'file.elec': 58, 'newallo.elec': 4}
Top-level field sets: 6 different layouts
Camera frame interval (ms): {'min': 16.667, 'max': 16.667}
[... 336 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
for i in (20,31):
    s=''.join(nb['cells'][i]['source']).splitlines()
    for j,l in enumerate(s[:18]): print(i,j+1,l)
EOF
```

```
20 1 for name, sub in (("(a) all sessions", S), ("(b) not probe sessions", S[~S.probe])):
20 2     reach = sub.t90.notna()
20 3     print(f"{name}: sessions reaching both criteria {int(reach.sum())} of {len(sub)}; "
20 4           f"fewer than 10 trials from lower bound > 1/4 to upper bound >= 0.9: {int((sub.t90 < 10).sum())}, "
20 5           f"fraction of sessions reaching {(sub.t90 < 10).sum() / reach.sum():.3f}, of all sessions {(sub.t90 < 10).mean():.3f}")
20 6 print("Trials from criterion to upper bound 0.9 (sessions reaching):", S.t90.describe()[["min", "50%", "max"]].to_dict())
20 7 print("Expected 0.89 +- 0.089")print("\nSessions where the upper bound is already at 0.9 or above at the criterion trial (0 trials):", int((S.t90 == 0).sum()),
20 8       "; trials to 0.9 per session:", S.t90.value_counts().sort_index().to_dict())
20 9 print("Upper bound at the criterion trial, quartiles:", S.ub_at_crit.quantile([0.25, 0.5, 0.75]).round(3).to_dict())
20 10 print("Variant with the 0-trial sessions left out:", f"{int(((S.t90 > 0) & (S.t90 < 10)).sum())} of {int((S.t90 > 0).sum())}",
20 11       f"= {((S.t90 > 0) & (S.t90 < 10)).sum() / (S.t90 > 0).sum():.3f}")
31 1 Rt = pd.DataFrame([dict(session=s, monkey=b["monkey"], **r) for s, b in beh.items() for r in b["returns"]])
31 2 res = []
31 3 for trials_used, Rsub in (("all", Rt), ("after successful", Rt[Rt.correct])):
31 4     Rsub = Rsub.copy()
31 5     for eye in ("mean", "l", "r"):
31 6         Rsub["z"] = zsess(Rsub, f"eye_{eye}")
31 7         for mk in ("ke", "sn", "both"):
31 8             d = Rsub if mk == "both" else Rsub[Rsub.monkey == mk]
31 9             diff, p, na, nb = rank_test(d, "z", d.dtheta < 0)
[... 9 more lines not kept]
```

**Agent**

Missing newlines where I appended. Fixing those, adding the reward-to-end timing check and a same-side variant for probe entries.

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def setsrc(i, text): cells[i]['source']=text.splitlines(keepends=True)
setsrc(20, src(20).replace('print("Expected 0.89 +- 0.089")print(', 'print("Expected 0.89 +- 0.089")\nprint('))
setsrc(31, src(31).replace('print(pd.DataFrame(res).to_string())vrows = []', 'print(pd.DataFrame(res).to_string())\nvrows = []'))
s=src(23)
s=s.replace('''P["eastern_first"] = P.first_rel.apply(lambda v: all(-150 <= x <= -60 for x in v))''','''P["eastern_first"] = P.first_rel.apply(lambda v: all(-150 <= x <= -60 for x in v))
P["one_side_first"] = P.first_rel.apply(lambda v: all(x < 0 for x in v) or all(x > 0 for x in v))''')
s=s.replace('''            ("(iii) first entries eastern, 5 trials from the introduction", P[P.eastern_first], "pc_after5"),''','''            ("(iii) first entries eastern (clockwise of the reward), 5 trials from the introduction", P[P.eastern_first], "pc_after5"),
            ("(iii') first entries on one side of the reward arm, 5 trials from the introduction", P[P.one_side_first], "pc_after5"),''')
s=s.replace('''("(i) all 12, 5 trials''','''("(i) all, 5 trials''').replace('''("(ii) all 12, the first''','''("(ii) all, the first''')
setsrc(23,s)
s=src(8)
s+='''tim = pd.DataFrame([{"monkey": b["monkey"], **b["timing"]} for b in beh.values()])
print("\\nMedian time per session (s): reward (code 11) to trial end (code 23), and trial end to the next trial start:")
print(tim.groupby("monkey").median().round(2).to_string())
'''
setsrc(8,s)
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
p='wirth.py'; s=open(p).read()
s=s.replace('''    return {"monkey": c["monkey"], "session": c["session"], "n_trials": len(c["cm"]),
            "pos_start"''','''    nxt = np.r_[tr["t_start"][1:], np.nan]
    timing = {"reward_to_end": float(np.nanmedian(tr["t_end"] - tr["t_reward"])),
              "end_to_next_start": float(np.nanmedian(nxt - tr["t_end"]))}
    return {"monkey": c["monkey"], "session": c["session"], "n_trials": len(c["cm"]), "timing": timing,
            "pos_start"''')
open(p,'w').write(s)
EOF
grep -n "timing" wirth.py
```

```
779:    timing = {"reward_to_end": float(np.nanmedian(tr["t_end"] - tr["t_reward"])),
781:    return {"monkey": c["monkey"], "session": c["session"], "n_trials": len(c["cm"]), "timing": timing,
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
p='wirth.py'; s=open(p).read()
s=s.replace('''    oc_c, oc_r = sess.occ_common''','''    for r in WINDOWS:
        out[f"frames|{r}"] = int(sess.tables[r][1].sum())
    oc_c, oc_r = sess.occ_common''')
open(p,'w').write(s)
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
s=''.join(cells[35]['source'])
s+='''print("Analysed frames per cell, median, by trial window:", C[[f"frames|{r}" for r in wirth.WINDOWS]].median().to_dict())
'''
cells[35]['source']=s.splitlines(keepends=True)
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
import os
d=os.environ['TMPDIR']+'/full'; os.makedirs(d,exist_ok=True)
c3=''.join(cells[3]['source'])
c4=''.join(cells[4]['source'])
cells[4]['source']=(c4+'\nimport pickle, os\npickle.dump((metas, cells, beh, fp21), open(os.environ["TMPDIR"] + "/full/data.pkl", "wb"))\n').splitlines(keepends=True)
json.dump(nb,open(d+'/dev.ipynb','w'),indent=1)
EOF
cp wirth.py $TMPDIR/full/; cd $TMPDIR/full; date -u; timeout 3600 executed/wirth-2017/.venv/bin/python -m jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3600 --output out.ipynb dev.ipynb 2>&1 | tail -1; date -u; ls -la
```

```
Fri Nov 13 15:10:27 UTC 2026
[NbConvertApp] Writing 124806 bytes to out.ipynb
Fri Nov 13 15:33:07 UTC 2026
total 9260
drwxr-xr-x 3 runner runner    4096 Nov 13 15:33 .
drwx-----T 7 runner runner    4096 Nov 13 15:33 ..
drwxr-xr-x 2 runner runner    4096 Nov 13 15:10 __pycache__
-rw-r--r-- 1 runner runner 9220769 Nov 13 15:32 data.pkl
-rw-r--r-- 1 runner runner   70201 Nov 13 15:10 dev.ipynb
-rw-r--r-- 1 runner runner  124806 Nov 13 15:33 out.ipynb
-rw-r--r-- 1 runner runner   41724 Nov 13 15:10 wirth.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/full; python - <<'EOF'
import json
nb=json.load(open('out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code' or i==12: continue
    out=''
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error': out+='ERROR '+o['ename']+': '+o['evalue']+'\n'
        elif 'text' in o: out+=''.join(o['text'])
        elif 'data' in o: out+=''.join(o['data'].get('text/plain',''))
    print(f"=== [{i}]"); print(out[:7000])
EOF
```

```
=== [1]

=== [3]
hc-12 pass: 1161 s, peak memory 0.97 GB

=== [4]
hc-21 pass: 143 s, 101 files

=== [6]
Files by monkey (ke = monkey K, sn = monkey S):
        files  with_new_maze  sessions
monkey                                
ke         99             99        41
sn         90             88        26

Files without a new-maze (newallo) field: ['sn20121015_HPC_e2_c1a_seg.mat', 'sn20121015_HPC_e2_c1c_seg.mat']

Spike times taken from: {'file.elec': 175, 'newallo.elec': 12}
Top-level field sets: 7 different layouts
Camera frame interval (ms): {'min': 16.667, 'max': 16.667}
[... 241 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json, os
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
for c in cells:
    if c['cell_type']=='code':
        s=''.join(c['source'])
        import re
        s2=re.sub(r'\)(print\(|tim = |vrows)', r')\n\1', s)
        if s2!=s: print('fixed', s[:40]); c['source']=s2.splitlines(keepends=True)
# ensure cells don't end with newline issue: compile each code cell
import ast
for i,c in enumerate(cells):
    if c['cell_type']=='code':
        try: ast.parse(''.join(c['source']))
        except SyntaxError as e: print('syntax', i, e)
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
# dev copy loading pickle
cells[3]['source']=['import pickle, os\n','metas, cells, beh, fp21 = pickle.load(open(os.environ["TMPDIR"] + "/full/data.pkl", "rb"))\n','M = pd.DataFrame(metas)\n','C_all = pd.DataFrame(cells)\n']
cells[4]['source']=['\n']
s=''.join(cells[34]['source']).replace('range(60)','range(2)')
cells[34]['source']=s.splitlines(keepends=True)
json.dump(nb,open(os.environ['TMPDIR']+'/full/ana.ipynb','w'),indent=1)
EOF
cp wirth.py $TMPDIR/full/; cd $TMPDIR/full; timeout 900 executed/wirth-2017/.venv/bin/python -m jupyter nbconvert --to notebook --execute --allow-errors --output ana_out.ipynb ana.ipynb 2>&1 | tail -1
```

```
fixed B = pd.DataFrame([{k: v for k, v in b.it
fixed READINGS = [(r, sr) for r in wirth.WINDO
[NbConvertApp] Writing 137441 bytes to ana_out.ipynb
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/full; python - <<'EOF'
import json
nb=json.load(open('ana_out.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code' or i in (3,4,6,10,12,14,17,18,20,23,26,27,28,31,34): continue
    out=''
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error': out+='ERROR '+o['ename']+': '+o['evalue']+'\n'
        elif 'text' in o: out+=''.join(o['text'])
        elif 'data' in o: out+=''.join(o['data'].get('text/plain',''))
    print(f"=== [{i}]"); print(out[:9000])
EOF
```

```
=== [1]

=== [8]
Learning curves: column 2 <= column 1 <= column 3 in 187 of 187 files
Field learningtrial equals the first trial with column 2 > 1/4 (or -2 when never): 66 of 66 sessions

Eye signal scale by session: {'+-5000': 36, '+-5': 26, nan: 4}
Fraction of eye samples at the +-5000 / +-5 rail, by session: median 0.0049 max 0.217

Arm chosen on rewarded trials (1-5 = codes 50-54), sessions per value: {(np.int64(4),): 32, (np.int64(5),): 9, (np.int64(1),): 9, (np.int64(2),): 8, (np.int64(3),): 7, (np.int64(2), np.int64(4)): 1}

Camera abscissa (0 centre, 1 arm end) at event times, median over sessions:
start +0s     0.01
start -1s     0.40
start +1s     0.12
center +0s    0.00
center -1s    0.72
center +1s    0.00
reward +0s    1.00
reward -1s    0.21
[... 229 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
p='wirth.py'; s=open(p).read()
s=s.replace('''                    "tag_hundreds": tuple(sorted(set((t60[:, 10] // 100).astype(int)))),''','''                    "tag_hundreds": tuple(sorted(set((t60[:, 10] // 100).astype(int)))),
                    "entry_headings": entry_headings(t60),''')
s=s.replace('''def file_meta(name, d, c):''','''def entry_headings(t60):
    """Circular mean camera orientation (degrees, 0 to 360) on each entry path (tags 10x)."""
    tag, th = t60[:, 10], np.deg2rad(t60[:, 3])
    out = {}
    for x in np.unique(tag[(tag >= 100) & (tag < 200)]).astype(int):
        m = tag == x
        out[x % 100] = int(round(np.rad2deg(np.arctan2(np.sin(th[m]).mean(), np.cos(th[m]).mean())) % 360))
    return out


def file_meta(name, d, c):''')
open(p,'w').write(s)
EOF
cd $TMPDIR/full && cp entries/wirth-2017/wirth.py . && date -u && timeout 1200 executed/wirth-2017/.venv/bin/python - <<'EOF'
import wirth, pandas as pd, numpy as np
rows=[]
for name, d in wirth.stream_members("hc-12"):
    c = wirth.reduce_file(name, d)
    if c is None: continue
    h = wirth.entry_headings(c["t60"])
    rows.append({"file": name, "session": c["session"], "headings": h, "theta_min": c["t60"][:,3].min(), "theta_max": c["t60"][:,3].max()})
R=pd.DataFrame(rows).drop_duplicates("session")
R["spacing"]=R.headings.apply(lambda h: sorted(set(int(round(((b-a)%360))) for a in h.values() for b in h.values() if a!=b)))
print(R[R.file.str.startswith("ke20140207")].to_string())
print(R.headings.apply(lambda h: tuple(sorted(h.values()))).value_counts().head(10))
EOF
date -u
```

```
Fri Nov 13 15:34:11 UTC 2026
                         file     session                        headings  theta_min  theta_max              spacing
57  ke20140207_HPC_c1_seg.mat  ke20140207  {1: 90, 3: 234, 4: 306, 5: 18}     -126.0       90.0  [72, 144, 216, 288]
headings
(18, 90, 162, 234)         28
(90, 162, 234, 306)         9
(18, 90, 234, 306)          8
(18, 90, 162, 306)          7
(18, 162, 234, 306)         7
(18, 90, 162, 234, 306)     3
(18, 90, 162)               1
(18, 162, 234)              1
(90, 162)                   1
(90, 162, 234)              1
Name: count, dtype: int64
Fri Nov 13 15:37:44 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='markdown' and i in (22,25,29,57,63): print(f"=== [{i}]\n"+''.join(c['source']))
EOF
```

```
=== [22]
## probe-transfer

> In probe sessions, performance after the new western entries were introduced was higher than
> at the start of the session (monkey K 73% against 44%, monkey S 80% against 55%).

A probe session is read from the start arms: the first 10 trials use one or two entries and
later trials use others (Results; S3C legend: one entry for 36 trials, or two entries until trial
60). The introduction is the first trial from an entry not used in the first 10.
=== [25]
## gaze-anticipates-action

> During the 500 ms before each joystick action, gaze anticipated the direction of the
> subsequent movement.

Each left (code 2) or right (code 1) joystick move; mean horizontal eye signal in the 500 ms
(reading a) or 300 ms (reading b) before it, for successful trials (Method W) and, as a variant,
all trials. The eye signal is in uncalibrated units on two scales (data check), so values are
standardized within each session (minus the session median, over the session's SD) before
pooling sessions; per-session differences are also counted. Wilcoxon rank-sum, right against
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def setsrc(i, text): cells[i]['source']=text.rstrip('\n').splitlines(keepends=True)
def md(text): return {"cell_type":"markdown","metadata":{},"source":text.rstrip('\n').splitlines(keepends=True)}
def chk(i, start): assert src(i).startswith(start), (i, src(i)[:60])

# cell 6 add headings
chk(6,'print("Files by monkey')
setsrc(6, src(6) + '''print("Mean camera orientation on each entry path (tags 10x), sets of headings per session:",
      M.drop_duplicates("session").entry_headings.dropna().apply(lambda h: tuple(sorted(h.values()))).value_counts().to_dict())
''')
chk(0,'# Reproducing')
s=src(0)
s=s.replace('''| gaze-anticipates-action, gaze-anticipates-landmarks | tested (eye-signal sign assumed) |''','''| gaze-anticipates-action, gaze-anticipates-landmarks | tested (eye-signal sign assumed, checked on the slow phases) |''')
s=s.replace('''| responsive-cells, multi-space-coding, state-space-ic-higher, sparsity-gaze-vs-state, spatial-selectivity-fraction | blocked: the point-of-gaze space cannot be built (no eye calibration); three-space results shown |''','''| responsive-cells, multi-space-coding, sparsity-gaze-vs-state, spatial-selectivity-fraction | blocked: the point-of-gaze space cannot be built (no eye calibration); three-space results shown |
| state-space-ic-higher | tested on two of its three comparisons (the third needs gaze) |''')
setsrc(0,s)
chk(7,'The descriptor (hc-12')
setsrc(7, src(7)+'''

Every file holds the 12-column camera layout of the descriptor (not the 11 columns that
`star_remapped_cell_r.m` documents), with transition tags 101 to 555 and a state-space radius
of 0.81 to 3.0, inside the -3 to 3 grid of the state-space maps. The polar angle is on -pi to pi
in some files and 0 to 2 pi in others; the maps use its cosine and sine. The mean orientation on
each entry path falls on 18, 90, 162, 234 or 306 degrees in every session, the five arms 72
degrees apart. ke20140207 spans only -126 to 90 degrees because its headings (18, 90, 234 and
306, that is -126 and -54) all fall in that range. In sn20110610 3.6% of the frames have an
abscissa up to 1.618, none of them on an entry path, so the landmark ANOVAs do not use them.''')
chk(9,'Checks against the description')
setsrc(9, src(9)+'''
- The trial ends (code 23) at the reward (code 11): the median time between them is 0 s in both
  monkeys, and the return lasts until the next trial start (median 3.6 to 3.8 s).''')
chk(21,'**Result: reproduced.** Of the 59')
setsrc(21,'''**Result: reproduced.** Of the 59 sessions that reach both criteria, 53 need fewer than 10
trials (0.898, expected 0.89 +- 0.089); counted over all 66 sessions the fraction is 0.803, also
inside the tolerance (0.801 to 0.979). Without the probe sessions the fractions are 0.898 and
0.815. Only one session has its upper bound at 0.9 already at the criterion trial (0 trials);
the median is 2 trials, and the upper bound at the criterion trial has a median of 0.835.
Leaving out that session gives 52 of 58 (0.897).''')
chk(22,'## probe-transfer')
setsrc(22,'''## probe-transfer

> In probe sessions, performance after the new western entries were introduced was higher than
> at the start of the session (monkey K 73% against 44%, monkey S 80% against 55%).

A probe session is read from the start arms: the first 10 trials use one or two entries and
later trials use others (Results; S3C legend: one entry for 36 trials, or two entries until trial
60). The introduction is the first trial from an entry not used in the first 10. The side of the
first entries is checked from the arm-end positions, relative to the rewarded arm (north by the
paper's convention). Variants: the first 5 trials from a new entry (ii); sessions whose first
entries lie clockwise of the reward, east if x is east and y north (iii), or on one side of the
rewarded arm whichever side (iii'); sessions whose introduction comes after trial 20 (iv).''')
chk(24,'**Result: not reproduced.**')
setsrc(24,'''**Result: not reproduced.** hc-12 holds 12 probe sessions of monkey K (the paper has 15) and
none of monkey S (the paper has 9); hc-21 adds no other. For K, performance is 28.3% over the
first 5 trials and 58.3% over the 5 trials after the new entries, both below the paper's 44% and
73% by more than the tolerance, and the Wilcoxon signed-rank test gives p = 0.072. The direction
of the effect is the paper's (median gain 0.30). The first entries are not always on one side:
their angles from the rewarded arm are -72 or -144 degrees in 4 sessions, +72 or +144 in 5, and
on both sides in 3. In no variant are both of K's means within tolerance: 60.0% after with the
first 5 new-entry trials (p = 0.057); 15.6% and 62.2% (p = 0.023) over the 9 sessions with the
first entries on one side; 16.0% and 64.0% (p = 0.125) over the 5 sessions introduced after
trial 20.''')
chk(25,'## gaze-anticipates-action')
setsrc(25, src(25)+''' Per-session differences are
also tested across sessions (Wilcoxon signed-rank), as the turns of one session are not
independent.''')
chk(29,'Sign of the eye signal')
setsrc(29,'''Sign of the eye signal. The files do not say which sign of the horizontal signal is rightward.
It is taken from the slow phases. During a turn the scene flows across the screen opposite to
the turn, and the slow phases of optokinetic nystagmus and smooth pursuit follow the scene, so
the eye drifts to the left during a right turn. The median eye velocity from 0 to 600 ms after
the code is positive during right turns and negative during left turns, in 40 of 40 sessions of
K and 20 of 20 of S (session signed-rank p = 1.8e-12 and 1.9e-6). The slow phases are therefore
leftward when the signal increases, and a negative value is rightward. This uses the eye
velocity only, not the eye position that the claim tests. The mean position during the turn
moves the other way, toward the turn (profile above), as the mean eye position does during
optokinetic stimulation. The sign is still an assumption, now supported by this check.

**Result: reproduced, resting on the sign of the eye signal.** Before right turns the
horizontal eye signal lies on the negative (rightward) side of that before left turns in each
monkey, in both windows, for each eye and both eyes, with rank-sum p below 1e-100 (500 ms, both
eyes, successful trials: K median difference -0.77 session SD, p = 4.0e-148; S -1.00,
p = 4.3e-146). Across sessions the difference is negative in 39 of 40 sessions of K and 20 of 20
of S (signed-rank p = 1.3e-11 and 1.9e-6), so the result does not rest on pooling the turns of
a session.''')
chk(32,'**Result: reproduced, resting')
setsrc(32,'''**Result: reproduced, resting on the sign of the eye signal.** During passive returns that
turn right the eye signal lies on the negative (rightward) side of that during returns that turn
left, in each monkey (all returns, both eyes: K -0.56 session SD, p = 6.2e-58, 39 of 41 sessions,
signed-rank across sessions p = 1.3e-9; S -0.56, p = 6.4e-30, 20 of 21 sessions, p = 1.9e-6),
and after successful trials only (p = 4.7e-34 and 1.5e-10). The sign comes from the slow phases
during turns at the centre (above); the eye velocity over the returns gives the same sign
(right-turning returns higher in 40 of 41 sessions of K and 21 of 21 of S). The test measures
where the eyes are during the return, as the claims file's criterion does; whether this is
anticipation or the eye position that goes with any rotation of the view cannot be told apart
here.''')
# after cell 35 (READINGS table), add note
chk(35,'READINGS = ')
cells.insert(36, md('''The corrected "shift" surrogates give 3.3% of the synthetic trains p < 0.01 and 5% p < 0.05
(permuted chunks 0% and 5%), with surrogate IC within 2% of the actual IC on average; the first
version, with overlapping chunks, gave all of them p < 0.01 and surrogate IC twice the actual.
Only 3 cells (permuted chunks) and none (shifted chunks) have state-space IC significantly low,
so the bilateral test adds almost nothing from the low side. The "toreward_ret" window is
almost the "full" one (38,212 against 38,224 analysed frames per cell, median), as the trial
ends at the reward; its counts differ by at most one cell from "full".'''))
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
for i,c in enumerate(nb['cells'][36:]): print(i+36, c['cell_type'], c['metadata'].get('tags',''), ''.join(c['source'])[:60].replace('\n',' | '))
EOF
```

```
36 markdown  The corrected "shift" surrogates give 3.3% of the synthetic 
37 markdown  ## responsive-cells (blocked) and state-space-most-responsiv
38 code ['claim:state-space-most-responsive'] print("Cells with significant state-space IC (p < 0.01), per
39 markdown  **Result: not reproduced.** The state-space count is 57 of 1
40 markdown  ## direction-center-vs-periphery |  | > For direction-selective 
41 code ['claim:direction-center-vs-periphery'] dir_rows = [] | for sr in ("permute", "shift"): |     for cellse
42 markdown  **Result: not reproduced.** For the 40 direction-selective c
43 markdown  ## direction-tuning-not-maintained |  | > Direction tuning was n
44 code ['claim:direction-tuning-not-maintained'] rows = [] | for sr in ("permute", "shift"): |     for cellset, m
45 markdown  **Result: partially reproduced.** Among the 40 direction-sel
46 markdown  ## sparsity-state-vs-direction and sparsity-state-vs-positio
47 code  def sparsity_compare(other): |     rows = [] |     for r, sr in 
48 code ['claim:sparsity-state-vs-direction'] print(sparsity_compare("direction").to_string())
49 markdown  **Result: reproduced under the main reading only.** For the 
50 code ['claim:sparsity-state-vs-position'] print(sparsity_compare("position").to_string()) | print("Expec
51 markdown  **Result: not reproduced.** Under the main reading state spa
52 markdown  ## state-space-ic-higher |  | > Spike information content was sy
53 code ['claim:state-space-ic-higher'] rows = [] | for r, sr in READINGS: |     for other in ("position
54 markdown  ## state-space-selectivity |  | > In the maze center, at the sam
55 code ['claim:state-space-selectivity'] rows = [] | for ty in wirth.TYPINGS: |     for r, sr in READINGS
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def setsrc(i, text): cells[i]['source']=text.rstrip('\n').splitlines(keepends=True)
def md(text): return {"cell_type":"markdown","metadata":{},"source":text.rstrip('\n').splitlines(keepends=True)}
def chk(i, start): assert src(i).startswith(start), (i, src(i)[:60])
s=src(24).replace('''their angles from the rewarded arm are -72 or -144 degrees in 4 sessions, +72 or +144 in 5, and
on both sides in 3.''','''their angles from the rewarded arm are -72 or -144 degrees in 2 sessions, +72 or +144 in 7, and
on both sides in 3, where the paper describes the northeastern and southeastern entries.''')
setsrc(24,s)
s=src(36).replace('''Only 3 cells (permuted chunks) and none (shifted chunks) have state-space IC significantly low,''','''At most 3 cells (permuted chunks) and none (shifted chunks) have state-space IC significantly low,''').replace('''"full" one (38,212 against 38,224 analysed frames per cell, median), as the trial
ends at the reward; its counts differ by at most one cell from "full".''','''"full" one (38,212 against 38,224 analysed frames per cell, median), as the trial
ends at the reward; its bilateral counts differ by at most one cell from those of "full".''').replace('twice the actual','2.1 times the actual')
setsrc(36,s)
chk(39,'**Result: not reproduced.** The state-space count')
setsrc(39,'''**Result: not reproduced.** The state-space count is 57 of 186 cells under full trials with
permuted chunks, and 47, 42, 37, 57 and 47 under the other five readings, all below the expected
75.6 to 92.4. With the upper tail alone the counts are 41 to 58. The count needs no gaze, so the
missing gaze space does not change this; the chi-squared tests across the four spaces could not
be run. State space is still the space with the most significant cells of the three computed
here under every reading but toreward with shifted chunks (57 against 46 and 40 under the main
reading).''')
chk(42,'**Result: not reproduced.** For the 40')
setsrc(42,'''**Result: partially reproduced, resting on the three-space responsive cells standing in for
reading (b).** For the 40 direction-selective cells (reading a, permuted chunks) normalized
sparsity is higher in the centre (median difference 0.020, p = 0.031) but IC is not (0.012,
p = 0.43); with shifted chunks, 28 cells, p = 0.016 and 0.095. Under reading (a) neither the
reproduced level nor the partial level is met. Over the cells responsive in the three spaces
computed here, which stand in for reading (b), IC and sparsity are both higher in the centre
with p = 0.045 and 0.0074 (59 cells, permuted chunks), the criterion's partial level; with
shifted chunks (51 cells) IC is not (p = 0.14, sparsity p = 0.013). No reading reaches
p < 0.001.''')
chk(45,'**Result: partially reproduced.** Among the 40')
setsrc(45,'''**Result: not reproduced.** Among the 40 direction-selective cells (permuted chunks), 15 have
a significantly low centre-return correlation (38%, binomial p = 2.1e-14 at chance 0.025) and 4
a significantly high one (p = 0.017). The proportion of low cells is close to the paper's 36%
and the high count is inside 2 to 4, but 40 cells are tested (expected 56 +- 5.6) and the low
count of 15 is outside 20 +- 2. Over the three-space responsive cells, 59 are tested (inside the
tolerance), 4 are high and 16 low; with shifted chunks 51 are tested, 3 high and 14 low, and over
the 28 direction-selective cells 2 high and 11 low. The low count misses 18 to 22 under every
reading, so the criterion is not met, although more cells than chance have a low correlation
under all of them (binomial p below 1e-10). The minimum of common bins (10 or 2) changes
nothing.''')
chk(49,'**Result: reproduced under the main reading only.**')
setsrc(49,'''**Result: reproduced under the full-trial window, with either surrogate.** For the 40 cells
significant in both state and direction space (full trials, permuted chunks), normalized
sparsity is higher in state space (median difference 0.016, 28 of 40 cells, Wilcoxon
p = 0.0022); with shifted chunks, 27 cells, 0.020, p = 0.0059. With the start-to-reward window it
is not significant (p = 0.92 and 0.98), and the start-to-reward window with the returns gives
the full-trial numbers. The outcome rests on keeping the returns in the maps.''')
chk(51,'**Result: not reproduced.** Under the main reading state space')
setsrc(51,'''**Result: not reproduced.** State space is significantly sparser than position space overall
under every reading (Wilcoxon p = 0.00013 to 0.00043, median difference 0.014 to 0.028), where
the paper finds no significant difference. The individually significant cells number 7 to 11
(level 0.05) or 3 to 5 (level 0.01), against 15 +- 1.5. No reading meets either of these two
parts. The cells that differ individually are sparser in state space (p = 0.001 to 0.016 at
level 0.05), the third part.''')
# state-space-ic-higher conclusion after 53
chk(53,'rows = []')
cells.insert(54, md('''**Result: partially reproduced.** Normalized IC is higher in state space than in position
space (full trials, permuted chunks: 44 cells, median difference 0.014, 35 higher, p = 1.1e-4)
and than in direction space (40 cells, 0.021, 35 higher, p = 2.5e-7), and both comparisons give
p < 0.01 under all six readings (largest p 0.0023). The third comparison, with the point-of-gaze
space, cannot be made without a calibration of the eye signal, so two of the three hold, the
criterion's partial level.'''))
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
EOF
date -u
```

```
Fri Nov 13 15:38:53 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def setsrc(i, text): cells[i]['source']=text.rstrip('\n').splitlines(keepends=True)
def md(text): return {"cell_type":"markdown","metadata":{},"source":text.rstrip('\n').splitlines(keepends=True)}
def chk(i, start): assert src(i).startswith(start), (i, src(i)[:60])
setsrc(39, src(39).replace('''State space is still the space with the most significant cells of the three computed
here under every reading but toreward with shifted chunks (57 against 46 and 40 under the main
reading).''','''State space is the space with the most significant cells of the three computed here
under every reading (57 against 46 and 40 under the main reading).'''))
setsrc(51, src(51).replace('(p = 0.001 to 0.016 at\nlevel 0.05)','(p = 0.00098 to 0.016 at\nlevel 0.05)'))
assert '0.00098' in src(51)
setsrc(54, src(54).replace('(largest p 0.0023)','(largest p 0.0022)'))
chk(55,'## state-space-selectivity')
setsrc(55,'''## state-space-selectivity

> In the maze center, at the same position and direction, 12 of 111 responsive cells (11%)
> showed significantly high state-space selectivity, discriminating the current rotational move,
> more than chance; only 4 showed significantly low selectivity, as expected by chance.

SSI per Methods, State-space selectivity; high or low when in the upper or lower 5% of the
surrogates (binomial chance 0.05, claims file). Counts over the three-space responsive cells
(lower bound) and over all cells (upper bound). The three moves are not named in the paper;
three typings are run: "arc" (36 degree alignment, 72 degree rotation right, 72 degree rotation
left), "align_dir" (36 degree alignment right, left, 72 degree rotation) and "tag" (each
transition tag of the state-space graph as its own move).''')
chk(57,'**Result: not reproduced.** The paper')
setsrc(57,'''**Result: not reproduced under permuted chunks, an assumption; open under shifted chunks.**
The paper's responsive set contains the three-space responsive cells and is contained in all
cells, so its counts lie between the two printed rows. With permuted chunks the low count over
the three-space responsive cells is already 6 or 7 under every move typing and trial window,
above the 3 to 5 the criterion allows, so no responsive set can meet the criterion. With shifted
chunks the bounds include the targets in most combinations (for example arc moves, full trials:
high 13 to 21, low 5 to 8), so the count over the paper's set cannot be decided without the
gaze space. The outcome rests on the permuted reading of the surrogates, which the Results'
"randomly shuffling periods of spiking activity in time" supports, and does not depend on the
move typing.''')
chk(59,'Which laps enter')
setsrc(59, src(59)+''' The ANOVA uses type II sums of squares; type III, the
default of MATLAB's `anovan`, is shown alongside.''')
chk(62,'**Result: not reproduced.** With successful laps')
setsrc(62,'''**Result: not reproduced.** With successful laps, at most 24 cells (all 186 cells) show a main
effect of relative distance, and at most 31 with all laps (27 and 33 with type III sums of
squares), against 64 +- 6.4; this bound holds for any responsive set. The identity count lies
between 15 and 32 (successful laps) or 21 and 47 (all laps), which allows 30, and the
interaction count between 5 and 14 or 8 and 17, but the distance count fails under every
reading, and with it the partial level. All laps give the paper's residual df of 756 in the one
session of 193 trials; none of its three cells has the Fig 5 F values (1.83, 3.19, 1.56 against
4.41 and 2.12).''')
chk(64,'**Result: blocked (metadata insufficient).**')
setsrc(64,'''**Result: blocked (metadata insufficient).** Over the three-space responsive cells and over all
cells the one-way count lies between 7 and 16 (reading a) or 10 and 23 (reading b) with
successful laps, and between 7 and 18 or 10 and 26 with all laps, so it may or may not fall in
11 to 13, and the binomial test depends on the size of the responsive set. Without the
point-of-gaze space the paper's responsive set cannot be formed, and the claim cannot be
decided.''')
chk(65,'## Claims blocked')
setsrc(65,'''## Claims blocked by the missing gaze calibration: three-space results

These numbers do not decide an outcome; they show how far the claims can be followed without
the point-of-gaze space. spatial-selectivity-fraction under reading (a) needs no gaze: the
fraction of cells with significant position IC is 0.129 to 0.247 under the six readings, outside
0.5 +- 0.05. Readings (b) and (c) need the responsive set: (b) is at least 0.253 to 0.317 and
(c) lies between 0.129 and 0.780, both of which allow 0.5. As the criterion is met when one
reading is within tolerance, the claim stays blocked.''')
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
EOF
echo done
```

```
done
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
i=len(cells)-1
assert ''.join(cells[i]['source']).startswith('## Summary')
text='''## Summary

| Claim | Outcome |
|---|---|
| gaze-anticipates-action | reproduced (sign of the eye signal assumed, supported by the slow phases) |
| gaze-anticipates-landmarks | reproduced (same sign) |
| learning-trials | reproduced |
| learning-to-90 | reproduced |
| probe-transfer | not reproduced (monkey K only; no probe session of S in hc-12) |
| probe-faster-criterion | blocked: methods underspecified |
| cells-recorded | partially reproduced (only the 189 analysed cells are deposited) |
| responsive-cells | blocked: metadata insufficient (no gaze calibration) |
| state-space-most-responsive | not reproduced |
| multi-space-coding | blocked: metadata insufficient |
| direction-center-vs-periphery | partially reproduced (three-space responsive cells for reading b, permuted chunks) |
| direction-tuning-not-maintained | not reproduced |
| state-space-ic-higher | partially reproduced (two of three comparisons; the third needs gaze) |
| sparsity-state-vs-direction | reproduced (full-trial window) |
| sparsity-state-vs-position | not reproduced |
| sparsity-gaze-vs-state | blocked: metadata insufficient |
| state-space-selectivity | not reproduced (permuted chunks; open under shifted chunks) |
| landmark-identity-distance | not reproduced |
| landmark-identity-center | blocked: metadata insufficient |
| path-selectivity, gaze-aligned-dynamics, latency-skew, eccentricity-modulation, foveation-selectivity, gaze-map-landmarks | blocked: metadata insufficient |
| fields-per-cell, dimensionality-control | blocked: methods underspecified |
| spatial-selectivity-fraction | blocked: metadata insufficient |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

How the analysis differs from the paper's. The point-of-gaze space is missing, as the eye
signal has no calibration, so the responsive set of the paper cannot be formed; counts over it
are bounded by counts over the three-space responsive cells and over all cells. The map
resolution steps, the surrogate shifting (two readings), the trial windows (three readings), the
move types of the state-space selectivity (three typings), the per-session standardization of
the eye signal and its sign are choices the paper does not fix. The learning-curve method of the
paper's reference 60 is not known, so curves were not recomputed.

What was found about the data. The learning curves' columns are probability, lower and upper
bound, not the order the descriptor gives; eye samples are 200 Hz, not 250 Hz; the eye signal
is on two different scales with no units, sign or calibration; the rewarded arm is not always
code 53; two hc-12 files have no new-maze data; 87 of the 101 hc-21 files hold the same spike
trains as hc-12 files; hc-12 holds 12 of monkey K's 15 probe sessions and none of monkey S's 9,
and in 3 of the 12 the first entries lie on both sides of the rewarded arm.'''
cells[i]['source']=text.splitlines(keepends=True)
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
EOF
cat README.md
```

```
# Wirth, Baraduc, Plante, Pinede & Duhamel (2017) from CRCNS hc-12

Tests the findings of [Wirth et al. (2017)](https://doi.org/10.1371/journal.pbio.2001045) that can be
tested on [CRCNS hc-12](https://doi.org/10.6080/K0R49NQV), which holds the 189 analysed hippocampal
cells of two macaques navigating a virtual star maze, with eye tracking. [CRCNS
hc-21](https://doi.org/10.6080/K0GX48R9) is read to check which of its recordings are also in hc-12.

| Claim | Outcome |
|---|---|
| Gaze anticipates the turn, and the side where landmarks will appear | Reproduced (sign of the eye signal assumed) |
| Learning in about a dozen trials; fewer than 10 more trials to 90% | Reproduced |
| Performance after new entries in probe sessions | Not reproduced (monkey K only) |
| Faster learning after new entries | Blocked: methods underspecified |
| 189 cells analysed of 270 recorded | Partially reproduced |
| State space has the most responsive cells (84) | Not reproduced |
| Direction maps: centre against return paths | IC and sparsity not reproduced; low correlations partially reproduced |
| Sparser in state space than in direction space | Reproduced (main reading) |
| Sparsity, state against position space | Not reproduced |
| State-space selectivity in the centre | Not reproduced |
| Landmark identity and distance (two-way ANOVA) | Not reproduced |
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
p='README.md'; s=open(p).read()
s=s.replace('''| Gaze anticipates the turn, and the side where landmarks will appear | Reproduced (sign of the eye signal assumed) |''','''| Gaze anticipates the turn, and the side where landmarks will appear | Reproduced (sign of the eye signal assumed, supported by the slow phases) |''')
s=s.replace('''| Direction maps: centre against return paths | IC and sparsity not reproduced; low correlations partially reproduced |
| Sparser in state space than in direction space | Reproduced (main reading) |''','''| Direction maps: centre against return paths | IC and sparsity partially reproduced; correlation counts not reproduced |
| Higher information in state space than in position and direction space | Partially reproduced (the gaze comparison cannot be made) |
| Sparser in state space than in direction space | Reproduced (full-trial window) |''')
s=s.replace('''| Claims that need the point-of-gaze space or the paper's responsive set (12 claims) |''','''| Claims that need the point-of-gaze space or the paper's responsive set (11 claims) |''')
open(p,'w').write(s)
EOF
grep -c "metadata_insufficient" attempts/wirth-2017-01.yaml; date -u
```

```
13
Fri Nov 13 15:39:44 UTC 2026
```

**Agent**

Notebook conclusions written. Quick check that the final notebook's analysis cells run cleanly from the saved data, before the full run.

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json, os
nb=json.load(open('reproduce_wirth_2017.ipynb'))
cells=nb['cells']
cells[3]['source']=['import pickle, os\n','metas, cells, beh, fp21 = pickle.load(open(os.environ["TMPDIR"] + "/full/data.pkl", "rb"))\n','M = pd.DataFrame(metas)\n','C_all = pd.DataFrame(cells)\n']
cells[4]['source']=['\n']
s=''.join(cells[34]['source']).replace('range(60)','range(2)')
cells[34]['source']=s.splitlines(keepends=True)
json.dump(nb,open(os.environ['TMPDIR']+'/full/ana2.ipynb','w'),indent=1)
EOF
cp wirth.py $TMPDIR/full/; cd $TMPDIR/full; timeout 900 executed/wirth-2017/.venv/bin/python -m jupyter nbconvert --to notebook --execute --allow-errors --output ana2_out.ipynb ana2.ipynb 2>&1 | tail -1; python - <<'EOF'
import json
nb=json.load(open('ana2_out.ipynb'))
for i,c in enumerate(nb['cells']):
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error': print(i,'ERROR',o['ename'],o['evalue'])
c=nb['cells'][6]
print(''.join(''.join(o.get('text','')) for o in c['outputs'])[-600:])
EOF
```

```
[NbConvertApp] Writing 147588 bytes to ana2_out.ipynb
6 ERROR AttributeError 'DataFrame' object has no attribute 'entry_headings'
 an orientation range under 300 deg:
                             file  abscissa_max  abscissa_over_1  theta_min  theta_max  n_trials
57      ke20140207_HPC_c1_seg.mat         1.000           0.0000  -126.0000    90.0000      80.0
99   sn20110610_hpc_e1_c1_seg.mat         1.618           0.0361  -179.9985   179.9918     198.0
100  sn20110610_hpc_e2_c1_seg.mat         1.618           0.0361  -179.9985   179.9918     198.0
Entry-path frames with abscissa above 1, over the cells of these files: {'ke20140207_HPC_c1_seg.mat': 0, 'sn20110610_hpc_e1_c1_seg.mat': 0, 'sn20110610_hpc_e2_c1_seg.mat': 0}
Shell cwd was reset to
```

**Agent**

Only the expected error (the saved data predate the new heading field). Starting the full clean run now (about 25 min).

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/wirth-2017 2>&1 | tail -30; date -u
```

```
Fri Nov 13 15:40:07 UTC 2026
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-wirth-2017 in executed/wirth-2017/.venv/share/jupyter/kernels/registry-wirth-2017
0 error(s)
pass  reproduce_wirth_2017.ipynb  (1403 s)
Fri Nov 13 16:03:40 UTC 2026
```

**Agent**

Run passed (23 min). Checking the executed outputs against the conclusions.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/wirth-2017/reproduce_wirth_2017.ipynb'))
d=json.load(open(f'/tmp/claude-1001/x.json')) if False else None
import os
ref=json.load(open(os.environ['TMPDIR']+'/full/ana2_out.ipynb'))
def outs(c):
    out=''
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error': out+='ERROR '+o['ename']+': '+o['evalue']+'\n'
        elif 'text' in o: out+=''.join(o['text'])
        elif 'data' in o: out+=''.join(o['data'].get('text/plain',''))
    return out
for i,(a,b) in enumerate(zip(nb['cells'],ref['cells'])):
    if a['cell_type']!='code': continue
    oa, ob = outs(a), outs(b)
    if i in (3,4,6,34) : print(f"=== [{i}]"); print(oa[-1500:]); continue
    if oa!=ob: print(f"=== [{i}] DIFFERS"); print(oa[:1500])
EOF
```

```
=== [3]
hc-12 pass: 1195 s, peak memory 0.97 GB

=== [4]
hc-21 pass: 148 s, 101 files

=== [6]
: 45.7}

Camera-data layout: columns of time_60 per file: {12.0: 187}
Transition tag (column 11) over files: 101.0 to 555.0 ; hundreds present per file: {(np.int64(1), np.int64(2), np.int64(3), np.int64(4), np.int64(5)): 182, (np.int64(1), np.int64(2), np.int64(4), np.int64(5)): 5}
Next tag (column 9) over files: -1111109120.0 to 108888888.0
State-space radius (column 8) over files: 0.809 to 3.0 ; polar angle (column 7): -3.142 to 6.283
Camera orientation range per file, sessions by (min, max) rounded to 90 deg: {(-180, 180): 55, (0, 360): 10, (-90, 90): 1}

Files with an abscissa above 1 or an orientation range under 300 deg:
                             file  abscissa_max  abscissa_over_1  theta_min  theta_max  n_trials
57      ke20140207_HPC_c1_seg.mat         1.000           0.0000  -126.0000    90.0000      80.0
99   sn20110610_hpc_e1_c1_seg.mat         1.618           0.0361  -179.9985   179.9918     198.0
100  sn20110610_hpc_e2_c1_seg.mat         1.618           0.0361  -179.9985   179.9918     198.0
[... 24 more lines not kept]
```

**Agent**

Final outputs match the development run. Now updating the attempt record: outcomes, notes, findings, and the round-1 `verifications` block.

**Agent calls Bash**

```bash
cd  sed -n 1,40p attempts/amjad-2025-01.yaml | head -5; python -c "
import yaml;d=yaml.safe_load(open('attempts/amjad-2025-01.yaml'));v=d['verifications'][0];print(v.keys());print(v['results'][0])"
```

```
schema_version: 3
id: amjad-2025-01
datasets:
- archive: dandi
  id: "002013"
dict_keys(['date', 'kind', 'by', 'reviewed', 'results'])
{'claim': 'insertion-yield', 'agrees': True, 'outcome': 'blocked', 'reason': 'The archive has 3 assets with sites c8dg, c3bs, c3a and cl3, and nothing about implanted or failed sensors. Figure 3 names 4 functional Monkey T sites against the paper\'s "3/14", so "sensor" may mean probe. Neither count can be checked; an implant log of sensors per monkey is not in the archive.', 'response': 'No change.'}
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec.py <<'PYEOF'
import yaml
p='attempts/wirth-2017-01.yaml'
d=yaml.safe_load(open(p))
O={o['claim']:o for o in d['outcomes']}

o=O['gaze-anticipates-action']
o['notes']=('Before right turns (code 1) the horizontal eye signal, standardized within session, lies on the negative '
 'side of that before left turns (code 2) in each monkey, in the 500 and the 300 ms windows, for each eye and both eyes, '
 'successful or all trials, with rank-sum p below 1e-100. 500 ms, both eyes, successful trials, K median difference -0.77 '
 'session SD (p = 4.0e-148, 39 of 40 sessions, signed-rank across sessions p = 1.3e-11), S -1.00 (p = 4.3e-146, 20 of 20 '
 'sessions, p = 1.9e-6). Negative is rightward by the slow phases (deviations), so gaze lies on the side of the coming turn. '
 'Both monkeys, each window and the pooled test agree, so the readings of the criterion give one outcome.')
o['deviations']=[
 'The eye signal has no calibration, units or sign in the files, and is on a +-5000 scale in 36 sessions and a +-5 scale in 26. '
 'Values are standardized within each session (minus the session median, over its SD) before sessions are pooled; per-session '
 'differences are also counted and tested across sessions.',
 'Assumed that a negative horizontal value is rightward, from the slow phases. During a turn the scene flows across the screen '
 'opposite to the turn and the slow phases of optokinetic nystagmus and pursuit follow it; the median eye velocity from 0 to '
 '600 ms after the code is positive during right turns and negative during left turns in 40 of 40 sessions of K and 20 of 20 '
 'of S (signed-rank p = 1.8e-12 and 1.9e-6). This uses the eye velocity only, not the position the claim tests. The mean position '
 'during the turn moves toward the turn, as it does during optokinetic stimulation.',
 'S1 Appendix A2, which holds the paper\'s analysis, was not available; the test is the rank-sum of the claims file.']

o=O['gaze-anticipates-landmarks']
o['notes']=('Passive returns (tags 5xy) turn right when the camera orientation falls over them, as it does after code 1. '
 'During right-turning returns the standardized eye signal lies on the negative (rightward) side in each monkey (all returns, '
 'both eyes, K -0.56 session SD, p = 6.2e-58, 39 of 41 sessions, signed-rank across sessions p = 1.3e-9; S -0.56, p = 6.4e-30, '
 '20 of 21 sessions, p = 1.9e-6) and after successful trials only (p = 4.7e-34 and 1.5e-10). The sign is set by the slow phases '
 'during turns at the centre, which do not use eye position; the eye velocity over the returns gives the same sign (40 of 41 and '
 '21 of 21 sessions). The test measures where the eyes are during the return, as the criterion does; whether this is anticipation '
 'or the eye position that goes with any rotation of the view cannot be told apart here.')
o['deviations']=['The same standardization and sign as gaze-anticipates-action.',
 'The side of a return is taken from the change of camera orientation over it (median absolute change 102.5 degrees); the files '
 'do not say where the landmarks appear.']

o=O['learning-to-90']
o['notes']=('Of the 59 sessions that reach both the lower bound above 1/4 and the upper bound at 0.9, 53 need fewer than 10 '
 'trials between them (0.898). Over all 66 sessions the fraction is 0.803, also within 0.89 +- 0.089, and without the probe '
 'sessions 0.898 and 0.815. One session has its upper bound at 0.9 already at the criterion trial (0 trials); the median is 2 '
 'trials and the upper bound at the criterion trial has a median of 0.835. Without that session the fraction is 52 of 58 (0.897).')

o=O['probe-transfer']
o['notes']=('hc-12 holds 12 probe sessions of monkey K (the paper reports 15) and none of monkey S (the paper reports 9); the 8 '
 'probe-like sessions of hc-21 are among the 12. For K, 28.3% correct over the first 5 trials and 58.3% over the 5 trials after '
 'the new entries, both below the paper\'s 44% and 73% by more than the tolerance; Wilcoxon signed-rank over the 12 sessions '
 'p = 0.072 (median gain 0.30). The first entries lie on one side of the rewarded arm in 9 sessions (clockwise in 2, '
 'counterclockwise in 7) and on both sides in 3, where the paper describes northeastern and southeastern entries. No variant '
 'brings both means within tolerance: the first 5 trials from a new entry give 60.0% (p = 0.057); the 9 one-sided sessions give '
 '15.6% and 62.2% (p = 0.023); the 5 sessions whose introduction comes after trial 20 give 16.0% and 64.0% (p = 0.125). The two '
 'values of monkey S could not be computed; the criterion fails on K\'s values alone.')
o['deviations']=[
 'Probe sessions are found from the start arms (the first 10 trials use one or two entries and later ones others), as the files '
 'do not mark them. The introduction is the first trial from an entry not used in the first 10 (S3C legend); the variants are '
 'shown.',
 'The measured values are monkey K\'s, after and at the start; monkey S has no probe session in the data.']

O['responsive-cells']['notes']=('Responsiveness is defined over four spaces, one of them the point of gaze, which needs the gaze '
 'direction in degrees; the eye signal has no calibration, units or sign in the files. Responsive in the three spaces computed '
 'here are 59 of 186 cells (full trials, permuted chunks; 51, 55, 47, 59 and 52 under the other readings), a lower bound of the '
 'four-space count, which could lie anywhere from 59 to 186.')

o=O['state-space-most-responsive']
o['notes']=('57 of 186 cells have significant state-space IC under the main reading (full trials, permuted chunks) and 47, 42, '
 '37, 57 and 47 under the other five readings (shifted chunks; start to reward; start to reward with the returns), all below 75.6 '
 'to 92.4. With the upper tail alone the counts are 41 to 58. The count needs no gaze, so the missing gaze space does not change '
 'the outcome; the chi-squared tests across the four spaces could not be run. State space has the most cells of the three '
 'spaces computed under every reading (57 against 46 for position and 40 for direction under the main reading).')
o['deviations']=[
 'Map resolution steps (square bins for position and state space, as in the dataset\'s scripts, equal angular bins for '
 'direction), two readings of the surrogate shifting and three of the trial window, as in the claims file (Method W). The start '
 'to reward window with the returns is almost the full one, as the trial ends at the reward (median 0 s from code 11 to 23).',
 'The shift reading rotates each 5 s chunk within itself by its own random offset. The first version moved each chunk over the '
 'whole session, so chunks overlapped; on synthetic trains without coding its surrogates had 2.1 times the actual IC and every '
 'train came out significant. The corrected version gives 3.3% of such trains p < 0.01 (permuted chunks 0%).']

o=O['direction-center-vs-periphery']
o['outcome']='partially_reproduced'
o['assumed']=True
o['notes']=('For the 40 cells with significant direction IC (reading a, permuted chunks) normalized sparsity is higher in the '
 'centre than on return paths (median difference 0.020, 25 of 40, Wilcoxon p = 0.031) and IC is not (0.012, p = 0.43); with '
 'shifted chunks (28 cells) p = 0.016 and 0.095. Reading (a) meets neither level. Over the 59 three-space responsive cells, which '
 'stand in for reading (b), IC and sparsity are both higher with p = 0.045 and 0.0074, the partial level; with shifted chunks (51 '
 'cells) IC is not (p = 0.14, sparsity p = 0.013). No reading reaches p < 0.001. The outcome rests on the stand-in for reading '
 '(b) and on permuted chunks.')
o['deviations']=[
 'Centre and return maps at one common angular resolution per session, chosen so the number of bins valid in both is closest to '
 '200 (median 151 centre and 157.5 return bins valid); the paper does not say how the two maps were binned.',
 'Reading (b), all responsive cells, cannot be formed without the gaze space; the three-space responsive cells, which it '
 'contains, stand in for it, an assumption.']

o=O['direction-tuning-not-maintained']
o['outcome']='not_reproduced'
o['notes']=('Of 40 direction-selective cells (permuted chunks), 15 (38%) have a significantly low centre-return correlation '
 '(binomial p = 2.1e-14 at chance 0.025) and 4 a significantly high one (p = 0.017). The high count is inside 2 to 4, but the '
 'number of cells tested (40, expected 56 +- 5.6) and the low count (15, expected 20 +- 2) are outside the tolerance. Over the '
 '59 three-space responsive cells 16 are low and 4 high; with shifted chunks 11 of 28 and 14 of 51 are low. The low count misses '
 '18 to 22 under every reading, although more cells than chance have a low correlation under all of them (binomial p below '
 '1e-10). The criterion has no partial level.')

o=O['state-space-ic-higher']
o['outcome']='partially_reproduced'
o.pop('blocked_by',None)
o['notebook']='reproduce_wirth_2017.ipynb'
o['output']='claim:state-space-ic-higher'
o['notes']=('Normalized IC is higher in state space than in position space (full trials, permuted chunks: 44 cells, median '
 'difference 0.014, 35 higher, Wilcoxon p = 1.1e-4) and than in direction space (40 cells, 0.021, 35 higher, p = 2.5e-7), with '
 'p < 0.01 under all six readings (largest 0.0022). The comparison with the point-of-gaze space cannot be made, as the eye signal '
 'has no calibration, so two of the three comparisons hold, the criterion\'s partial level.')
o['deviations']=['The cells of each comparison are those significant in both spaces compared, which needs no gaze; the '
 'point-of-gaze comparison is missing.']
# order keys
O['state-space-ic-higher']=o

o=O['sparsity-state-vs-direction']
o['notes']=('For the 40 cells with significant IC in both state and direction space (full trials, permuted chunks), normalized '
 'sparsity is higher in state space (median difference 0.016, 28 of 40 cells, Wilcoxon p = 0.0022); with shifted chunks, 27 '
 'cells, 0.020, p = 0.0059. With the start-to-reward window it is not significant (p = 0.92 and 0.98); the start-to-reward window '
 'with the returns gives the full-trial numbers. The outcome rests on keeping the returns in the maps.')
o['deviations']=['The main reading takes the trial window from start to next start (the state space includes the returns, '
 'Fig 1F legend); the paper does not settle it, and the outcome depends on it (findings). Both surrogate readings agree.']

o=O['sparsity-state-vs-position']
o['notes']=('State space is significantly sparser than position space over the cells responsive in both under every reading '
 '(Wilcoxon p = 0.00013 to 0.00043, median difference 0.014 to 0.028; main reading 44 cells, 0.016, p = 0.00043), where the '
 'paper\'s test finds no significant difference. 7 to 11 cells (per-cell level 0.05) or 3 to 5 (0.01) differ individually, '
 'against 15 +- 1.5 (main reading 9 and 5); those cells are sparser in state space (p = 0.00098 to 0.016 at level 0.05). No '
 'reading meets the first two parts.')

o=O['state-space-selectivity']
o['assumed']=True
o['notes']=('The paper\'s responsive set contains the three-space responsive cells and lies within all cells, so its counts '
 'are bounded by the counts over these two sets. With permuted chunks the low count over the three-space responsive cells is '
 'already 6 or 7 under every move typing and trial window, above the 3 to 5 the criterion allows, so no responsive set can meet '
 'the criterion (main reading, arc moves: high 15 to 23, low 7 to 12). With shifted chunks the bounds include the targets in most '
 'combinations (arc moves, full trials: high 13 to 21, low 5 to 8), so the claim cannot be decided there without the gaze space. '
 'The outcome rests on the permuted reading of the surrogates and does not depend on the move typing.')
o['deviations']=[
 'The three rotational moves are not named in the paper. Three typings are run: the 36 degree alignment (tags 2xy) and the 72 '
 'degree rotations to the right and to the left (tags 3xy, by the sign of the orientation change); the 36 degree alignment right '
 'and left and the 72 degree rotation; each transition tag as its own move. High and low are the upper and lower 5% of the '
 'surrogates, the level implied by the binomial chance rate of the claims file.',
 'The paper\'s responsive set cannot be formed (gaze space); the outcome rests on the bounds.',
 'Assumed that the 5 s chunks were permuted (Results, "randomly shuffling periods of spiking activity in time"); under the '
 'other reading the outcome is open.']

o=O['landmark-identity-distance']
o['notes']=('At most 24 cells (over all 186) show a main effect of relative distance with successful laps, and at most 31 with '
 'all laps (27 and 33 with type III sums of squares), against 64 +- 6.4; this bound holds for any responsive set. The identity '
 'count lies between 15 and 32 (successful laps) or 21 and 47 (all laps) and the interaction count between 5 and 14 or 8 and 17, '
 'but the distance count fails under every reading, and with it the partial level. With all laps the one session of 193 trials '
 '(sn20110624) gives the residual df of Fig 5, 756, and its three cells have interaction F of 1.83, 3.19 and 1.56, not the 4.41 '
 'and 2.12 of Fig 5.')
o['deviations'][1]=('Relative distance from the files\' curvilinear abscissa (0 centre, 1 arm end) in quarters; the landmark '
 'identity is the entry path. Rates per lap and segment, ANOVA with interaction, type II sums of squares, alpha 0.05; type III, '
 'the default of MATLAB\'s anovan, is shown and gives the same outcome.')

O['landmark-identity-center']['notes']=('Over the three-space responsive cells and over all cells the one-way count lies between '
 '7 and 16 (reading a) or 10 and 23 (reading b) with successful laps, and between 7 and 18 or 10 and 26 with all laps, so it may '
 'or may not fall in 11 to 13, and the binomial test depends on the size of the responsive set, which needs the gaze space.')

O['path-selectivity']['notes']=('Cells enter on significant point-of-gaze IC, which needs a calibration of the eye signal that '
 'the files do not give. Landmark entry into the field of view could be computed from the paper\'s geometry (landmarks between '
 'the arms at twice the arm length, 70 degree field of view) and the camera data, but not on the paper\'s cell set.')
O['gaze-aligned-dynamics']['notes']=('Foveation is gaze within 10 degrees of a landmark, which needs the gaze in degrees; the '
 'eye signal has no calibration.')
O['latency-skew']['notes']=('Depends on gaze-aligned-dynamics. The gaze-aligned latencies need foveation and the cells are those '
 'of gaze-aligned-dynamics; the onset-aligned latencies could be computed from the paper\'s landmark geometry, but only on another '
 'cell set, which would not test the claim.')
O['eccentricity-modulation']['notes']=('Depends on gaze-aligned-dynamics; landmark eccentricity relative to gaze needs calibrated gaze.')
O['gaze-map-landmarks']['notes']=('Needs point-of-gaze maps; the eye signal has no calibration.')

O['spatial-selectivity-fraction']['notes']=('Under reading (a) 0.129 to 0.247 of the 186 cells have significant position IC '
 'across the six readings of Method W (46 of 186 under the main one), outside 0.5 +- 0.05. Readings (b) and (c) need the '
 'responsive set: responsive cells among all are at least 0.253 to 0.317, and position cells among responsive lie between 0.129 '
 'and 0.780, both of which include 0.5. The criterion is met when one reading is within tolerance, so the claim cannot be decided.')

# findings
F=d['findings']
F[0]['statement']=F[0]['statement'].replace('which blocks 12 of the 28 claims; the files also give no\n    positions of the landmarks.','')
for f in F:
    if f['kind']=='metadata_insufficient' and 'eye signals' in f['statement']:
        f['statement']=('The horizontal and vertical eye signals have no units, calibration or sign convention. They are on a '
         '+-5000 scale in 36 hc-12 sessions and a +-5 scale in 26, with saturated samples at the bound (up to 22% of a session). '
         'The paper\'s point-of-gaze maps, foveation and landmark eccentricity cannot be computed, which blocks 11 of the 28 claims '
         'and part of a twelfth. The sign used here is inferred from the slow phases during turns.')
    if f['kind']=='methods_unavailable' and f['statement'].startswith('How were the 5 s chunks'):
        f['statement']=('How were the 5 s chunks of recording "randomly shifted" for the surrogates (their order permuted, or '
         'each shifted by its own offset), and did the maps include the passive returns after successful trials? Significant '
         'counts change between these readings (state space 57 or 47 of 186 cells with returns, 42 or 37 without), '
         'sparsity-state-vs-direction holds only with the returns, and state-space-selectivity is decided only with permuted '
         'chunks.')
F.append({'kind':'other','about':'data','datasets':['crcns-hc-12'],
 'statement':('In 3 of the 12 probe sessions of monkey K the first entries lie on both sides of the rewarded arm (for example '
  'ke20140306 starts from arms at -72 and +144 degrees from it), and in the other 9 they lie on one side, clockwise in 2 and '
  'counterclockwise in 7. The paper describes probe sessions as starting from the northeastern and southeastern entries.')})

# verifications
R=[
('gaze-anticipates-action',True,'reproduced',
 'Cell 23: before right turns the eye signal differs from before left turns in each monkey, in both windows and for every eye choice (500 ms, both eyes: K -0.77 SD, p = 4e-148; S -1.00 SD, p = 4e-146; 39/40 and 20/20 sessions). The direction depends on an assumed sign of the eye signal (problem 1): the files do not record it, the argument from where the eyes rest during optokinetic stimulation is reasonable, but the data cannot rule out the opposite sign, under which both gaze claims fail. Problem 9: the rank-sum tests pool turns across sessions; the session-level counts support the same direction.',
 'Added an independent check of the sign from the slow phases: the median eye velocity during turns is positive for right turns and negative for left turns in 40 of 40 sessions of K and 20 of 20 of S, so the slow phases (which follow the scene, opposite to the turn) are leftward when the signal increases, and negative is rightward. It uses eye velocity, not the position the claim tests. Added signed-rank tests of the per-session differences (p = 1.3e-11 and 1.9e-6). Outcome unchanged, still marked assumed.'),
('gaze-anticipates-landmarks',False,'partially_reproduced',
 'Cell 26: the eye signal differs between right and left returns in each monkey, p <= 1.5e-10 under every reading. The side relative to the turn is not tested independently, because the sign was chosen on the assumption that the eyes deviate toward the side the view rotates to, and that is what this test measures (problem 1).',
 'The sign is now set by the slow-phase velocity during turns at the centre, which does not use eye position, so the side relative to the turn is tested independently of the measure; the eye velocity over the returns gives the same sign. Kept reproduced and recorded the disagreement. The notes say that the test cannot tell anticipation from the eye position that goes with a rotation of the view.'),
('learning-trials',True,'reproduced',
 'Cell 17: S 12.26 (12.3 +- 2), K 16.53 under reading (a) and 15.82 under (b) (14.8 +- 2.4). The curves are the files\' own; their column order was checked against learningtrial in 66 of 66 sessions (cell 8).',
 'No change.'),
('learning-to-90',True,'reproduced',
 'Cell 18: 0.898 of sessions that reach both criteria, 0.803 of all sessions; both fall within 0.89 +- 0.089. It asked for the upper confidence bound at the criterion trial, to see how often t90 = 0 is trivial.',
 'Added the upper bound at the criterion trial (median 0.835) and the distribution of trials to 0.9: one session has 0 trials; without it the fraction is 0.897. No change of outcome.'),
('probe-transfer',True,'not_reproduced',
 'Cell 20: monkey K, 12 sessions: 28.3% in the first 5 trials (44 +- 4.4) and 58.3% after the new entries (73 +- 7.3); Wilcoxon p = 0.072. Monkey S has no probe session in hc-12 and none in hc-21 (data_missing for that part). Problem 7: a probe session is defined by its first 10 trials, the introduction falls at trials 10 to 16 in several sessions against 37 and 60 in the S3C examples, and the entries were not checked to be the eastern ones.',
 'Added the start-arm sequences, the side of the first entries relative to the rewarded arm, and variants (first 5 new-entry trials, one-sided first entries, introduction after trial 20). In 3 sessions the first entries lie on both sides of the rewarded arm (new finding). No variant brings both means within tolerance. Outcome unchanged.'),
('probe-faster-criterion',True,'blocked',
 'The criterion needs learning curves recomputed from the introduction with the unnamed method of reference 60. Monkey S also has no probe sessions (data_missing).',
 'No change.'),
('cells-recorded',True,'partially_reproduced',
 'Cell 14: 186 cells with more than 100 spikes (189 +- 18.9). The archive holds only the 189 deposited cells, so the 270 recorded cells (128 S, 142 K) cannot be checked.',
 'No change.'),
('responsive-cells',True,'blocked',
 'The point-of-gaze space needs a calibrated eye signal. The three-space count of 59/186 (cell 30) is only a lower bound.',
 'No change of outcome; counts updated for the corrected shift surrogates and the third trial window.'),
('state-space-most-responsive',True,'not_reproduced',
 'Cell 30: the state-space count is 57, 33, 42 or 24 across the four readings, and 62 at most under the one-sided variant, against 84 +- 8.4. The chi-squared tests could not be run without gaze. Problem 3: tail_p and sig count a cell as responsive when its IC is significantly below the surrogates, and only the two-sided p is stored.',
 'Fixed the shift surrogates (problem 2) and stored the upper and lower tails. The counts are now 57, 47, 42, 37, 57 and 47 over six readings, 41 to 58 with the upper tail alone; at most 3 cells are significant on the low side. Outcome unchanged.'),
('multi-space-coding',True,'blocked',
 '46 of 59 three-space responsive cells code in two or more spaces (cell 28), but the gaze-only cells could change the fraction.',
 'No change.'),
('direction-center-vs-periphery',False,'partially_reproduced',
 'Cell 32, permute surrogates, cell set (b): IC higher in the centre at p = 0.045 and sparsity higher at p = 0.0074. Neither reaches p < 0.001. Set (b) here is the three-space responsive set, standing in for the four-space set.',
 'Changed to partially_reproduced, marked assumed: the criterion is met at the partial level under one reading, with the three-space set standing in for reading (b). With the corrected shift surrogates IC is not significant under (b) (p = 0.14), so the outcome also rests on permuted chunks.'),
('direction-tuning-not-maintained',False,'not_reproduced',
 'Cell 34: the closest reading, (b) with permute, tests n = 59 cells (tolerance met), 4 high (band met), but 16 low against 20 +- 2. Every other reading also misses the low count.',
 'Changed to not_reproduced: the criterion has no partial level and the low count misses 18 to 22 under every reading, also with the corrected shift surrogates (11 and 14).'),
('state-space-ic-higher',False,'partially_reproduced',
 'Cell 47 (full/permute): state minus position, median 0.014, p = 1.1e-4; state minus direction, median 0.021, p = 2.5e-7. These are two of the three comparisons, which the criterion grades as partial. The notebook marks the claim blocked although these two comparisons need no gaze (problem 5); they are also shown only for full/permute.',
 'Changed to partially_reproduced and gave the claim its own section, with both comparisons under all six readings (all p < 0.01, largest 0.0022).'),
('sparsity-state-vs-direction',True,'reproduced',
 'Cell 37, full/permute: median difference +0.016, p = 0.0022. The other three readings fail.',
 'With the corrected shift surrogates the full-trial window also passes with shifted chunks (p = 0.0059); the start-to-reward window fails under both. Outcome unchanged, resting on the trial window.'),
('sparsity-state-vs-position',True,'not_reproduced',
 'Cell 38: the overall test is significant under both permute readings, and under the shift readings the individually significant count is 1 to 6, against 15 +- 1.5. Problem 2: the shift reading of Method W was never validly tested, which weakens the not-reproduced-under-any-reading verdicts.',
 'Re-run with the corrected shift surrogates: the overall test is now significant under every reading (p <= 0.00043) and the individual count is 3 to 11. Outcome unchanged.'),
('sparsity-gaze-vs-state',True,'blocked','Needs the point-of-gaze space.','No change.'),
('state-space-selectivity',True,'not_reproduced',
 'Cell 40: even over the three-space set, which is a lower bound, the low count is 7 to 9 under every reading (needs 3 to 5). The high count is >= 15 under full/permute, 13 under toreward/permute, and at most 8 under shift (needs 11 to 13). Problem 4: the three rotational moves are the author\'s own assumption, and other typings the paper allows were not run.',
 'Ran three move typings. With the corrected shift surrogates the bounds now include the targets in most combinations, so under shifted chunks the claim is open; under permuted chunks the low count over the three-space set is 6 or 7 under every typing and window, so it fails. Kept not_reproduced, now marked assumed on the permuted reading, with the shifted result in the notes.'),
('landmark-identity-distance',True,'not_reproduced',
 'Cell 44: the distance count is at most 31, even over all 186 cells with all laps, against 64 +- 6.4. Problem 8: anova_two uses type II sums of squares, where MATLAB\'s anovan defaults to type III; the gap is far too large for this to matter.',
 'Added type III counts (distance at most 33). Outcome unchanged.'),
('landmark-identity-center',True,'blocked',
 'Cell 45: the bounds straddle the target (for example 9 to 16 for view (a) and 11 to 23 for view (b), successful laps), so the count over the paper\'s responsive set cannot be decided without gaze.',
 'No change of outcome; bounds updated (7 to 16 and 10 to 23).'),
('path-selectivity',True,'blocked','Cell selection needs significant point-of-gaze IC, and there is no calibration.',
 'No change; the notes now say that landmark onsets could be computed from the paper\'s geometry.'),
('gaze-aligned-dynamics',True,'blocked','Foveation is defined as +-10 degrees and needs gaze in degrees.','No change.'),
('latency-skew',True,'blocked',
 'The gaze-aligned latencies and the cell set need gaze. The onset-aligned part might be computable from the camera data and the maze geometry, but only on a substitute cell set.',
 'No change; the notes say so. A substitute cell set would not test the claim, which depends on gaze-aligned-dynamics.'),
('eccentricity-modulation',True,'blocked','Eccentricity relative to gaze needs calibration.','No change.'),
('foveation-selectivity',True,'blocked','Needs foveation.','No change.'),
('fields-per-cell',True,'blocked','The field definition is in S1 Appendix, as the claims file says.','No change.'),
('spatial-selectivity-fraction',True,'blocked',
 'Reading (a) is testable and fails: 46/186 = 0.247 at best (cells 28 and 47). Readings (b) and (c) need the four-space responsive set.',
 'Reading (a) is now shown under all six readings (0.129 to 0.247); outcome unchanged, as the criterion is met under any one reading and (b) and (c) cannot be decided.'),
('gaze-map-landmarks',True,'blocked','Needs point-of-gaze maps.','No change.'),
('dimensionality-control',True,'blocked','The method is in S1 Appendix A5, which is not available.','No change.'),
]
order=[o['claim'] for o in d['outcomes']]
assert set(order)==set(r[0] for r in R), set(order)^set(r[0] for r in R)
res=[]
for cid,ag,out,reason,resp in sorted(R,key=lambda r: order.index(r[0])):
    res.append({'claim':cid,'agrees':ag,'outcome':out,'reason':reason,'response':resp})
d['verifications']=[{'date':'2026-11-13','kind':'agent',
 'by':'Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
 'reviewed':('The first executed notebook with the conclusion cells and the summary removed, the helper module and the claims '
  'file, with the paper\'s full text under paper/. The verifier checked the hc-12 and hc-21 archive listings and scripts for the '
  'blocked claims and tested surrogate_counts on synthetic Poisson trains. Its general problems, with what was changed: (2) the '
  'shift surrogates overlapped chunks and made a train without coding significant; replaced by rotating each chunk within itself, '
  'checked on synthetic trains in the notebook, and every analysis re-run. (3) only the two-sided p was stored; the tails are now '
  'kept and the upper tail shown as a variant. (6) the toreward window dropped the returns; a third window, start to reward plus '
  'the return, was added, and it is almost the full window as the trial ends at the reward. (10) the camera layout was not checked '
  'per file; all 187 files have 12 columns, tags 101 to 555, radius 0.81 to 3.0, and entry headings on the 72 degree grid, which '
  'explains the orientation range of ke20140207; the abscissa of 1.618 in sn20110610 falls on no entry path.'),
 'results':res}]
open(p,'w').write(yaml.safe_dump(d,sort_keys=False,width=100,allow_unicode=True))
PYEOF
python $TMPDIR/rec.py && grep -n "12 of the 28\|blocks 1" attempts/wirth-2017-01.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/entry.py check entries/wirth-2017 2>&1 | tail -5; git diff --stat; grep -n "—\|rather" attempts/wirth-2017-01.yaml entries/wirth-2017/README.md entries/wirth-2017/wirth.py | head; python -c "
import json;nb=json.load(open('entries/wirth-2017/reproduce_wirth_2017.ipynb'))
import re
for c in nb['cells']:
    s=''.join(c['source'])
    if '—' in s or re.search(r'\brather\b',s): print(s[:80])
print(nb['nbformat'],nb['nbformat_minor'], sum('id' not in c for c in nb['cells']))"
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
0 error(s)
 attempts/wirth-2017-01.yaml                   | 660 ++++++++++++++++++--------
 entries/wirth-2017/README.md                  |   9 +-
 entries/wirth-2017/reproduce_wirth_2017.ipynb | 539 ++++++++++++++++-----
 entries/wirth-2017/wirth.py                   | 219 ++++++---
 tools/build_site.py                           | 162 ++++++-
 tools/site_assets/app.css                     |   9 +
 tools/site_assets/list.js                     |  13 +-
 7 files changed, 1215 insertions(+), 396 deletions(-)
4 5 6
```

**Agent**

Checks pass. Six inserted cells lack cell ids (an nbformat warning), and one pandas warning shows in the SSI cell; fixing both, then a final clean run.

**Agent calls Bash**

```bash
cd entries/wirth-2017; python - <<'EOF'
import json, uuid
nb=json.load(open('reproduce_wirth_2017.ipynb'))
used={c.get('id') for c in nb['cells']}
for i,c in enumerate(nb['cells']):
    if 'id' not in c:
        c['id']=uuid.uuid5(uuid.NAMESPACE_URL, f"wirth-2017/{i}/{''.join(c['source'])[:40]}").hex[:8]
    s=''.join(c['source'])
    if 'bounds["high can be 11 to 13"]' in s:
        s=s.replace('bounds["high can be 11 to 13"] =','bounds[("high can be 11 to 13", "")] =').replace('bounds["low can be 3 to 5"] =','bounds[("low can be 3 to 5", "")] =')
        c['source']=s.splitlines(keepends=True)
ids=[c['id'] for c in nb['cells']]; assert len(ids)==len(set(ids))
open('reproduce_wirth_2017.ipynb','w').write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
EOF
cd  date -u; python tools/entry.py all entries/wirth-2017 2>&1 | tail -4; date -u
```

```
Fri Nov 13 16:05:49 UTC 2026
Installed kernelspec registry-wirth-2017 in executed/wirth-2017/.venv/share/jupyter/kernels/registry-wirth-2017
0 error(s)
pass  reproduce_wirth_2017.ipynb  (1461 s)
Fri Nov 13 16:30:20 UTC 2026
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json, os
nb=json.load(open('executed/wirth-2017/reproduce_wirth_2017.ipynb'))
ref=json.load(open(os.environ['TMPDIR']+'/full/ana2_out.ipynb'))
def outs(c):
    out=''
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error': out+='ERROR '+o['ename']+': '+o['evalue']+'\n'
        elif 'text' in o: out+=''.join(o['text'])
        elif 'data' in o: out+=''.join(o['data'].get('text/plain',''))
    return out
for i,(a,b) in enumerate(zip(nb['cells'],ref['cells'])):
    if a['cell_type']!='code' or i in (3,4,6,34): continue
    if outs(a)!=outs(b): print(i,'DIFFERS'); print(outs(a)[-800:])
print(outs(nb['cells'][34])); print(outs(nb['cells'][3]))
EOF
python tools/entry.py check entries/wirth-2017 2>&1 | tail -2; entries=1; grep -n "runtime_minutes" entries/wirth-2017/entry.yaml
```

```
56 DIFFERS
       7.0                False             False
                                  shift           18.0                   11.0       6.0                    4.0                 True              True
          toreward                permute         19.0                   13.0      10.0                    7.0                 True             False
                                  shift           18.0                   10.0       6.0                    3.0                 True              True
          toreward_ret            permute         19.0                   14.0      10.0                    7.0                False             False
                                  shift           18.0                   12.0       6.0                    4.0                 True              True

Synthetic Poisson trains (2 Hz, no coding), 999 surrogates each:
                             surrogates  trains  mean surrogate IC / actual IC  fraction p < 0.01  fraction p < 0.05
0                               permute      60                          1.018           0.000000               0.05
1                                 shift      60                          1.011           0.033333               0.05
2  shift, overlapping chunks (replaced)      60                          2.119           1.000000               1.00

hc-12 pass: 1252 s, peak memory 0.97 GB

0 error(s)
16:  runtime_minutes: 30
```

**Agent**

I've revised the attempt for round 1, re-run the entry from a clean environment with `python tools/entry.py all entries/wirth-2017` (passes in 24 min, peak memory 1 GB), and `entry.py check` reports 0 errors. Nothing is committed.

**Outcomes changed**
- **direction-center-vs-periphery:** not reproduced → partially reproduced, as the verifier proposed. Over the three-space responsive cells, which stand in for the paper's responsive set, IC is higher in the centre at p = 0.045 and sparsity at p = 0.0074. This holds only with permuted chunks, and the outcome is marked as resting on that assumption.
- **direction-tuning-not-maintained:** partially reproduced → not reproduced, as the verifier proposed. The criterion has no partial level, and the count of cells with a low correlation misses 18 to 22 under every reading.
- **state-space-ic-higher:** blocked → partially reproduced, as the verifier proposed. Two of the three comparisons need no gaze, and both give p < 0.01 under all six readings.
- **state-space-selectivity:** stays not reproduced, now marked as resting on the permuted-chunk reading. With the corrected shifted chunks the counts could fall in the target range, so under that reading the claim can't be decided.

**Disagreement kept**
- **gaze-anticipates-landmarks:** I kept it reproduced where the verifier gave partially reproduced, and recorded the disagreement. The sign of the eye signal now comes from a check that doesn't use eye position. During a turn the eyes drift with the scene, which moves opposite to the turn. The median eye velocity is positive in right turns and negative in left turns in 40 of 40 sessions of monkey K and 20 of 20 of monkey S. So a negative value is rightward, the sign the analysis assumed.

**Fixes and added outputs**
- **Shifted-chunk surrogates (the verifier's main bug):** chunks overlapped, so a cell that codes nothing came out significant. Each 5 s chunk is now rotated within itself. On synthetic spike trains that code nothing, 3.3% now come out significant at p < 0.01, against 100% for the old version. Every analysis was re-run with the fix.
- **Tail p-values:** both tails are now stored and the upper tail is shown alone. At most 3 cells are significant on the low side.
- **Third trial window:** start to reward plus the return that follows. It is almost the same as the full trial, because the trial ends at the reward.
- **State-space selectivity:** run under three groupings of the turns at the centre. The outcome does not depend on the grouping.
- **Landmark ANOVA:** the MATLAB default sums of squares (type III) are shown alongside. The distance count is at most 33 against 64 ± 6.4, so the outcome holds.
- **Gaze tests:** per-session signed-rank tests added, so the result does not rest on pooling turns within a session.
- **File layout:** checked per file. All 187 files use the 12-column camera layout. The odd orientation and abscissa ranges in two files are explained in the notebook and don't affect any analysis.
- **Learning:** the upper confidence bound at the criterion trial is added. Only one session reaches 0.9 at the criterion trial itself.
- **Probe sessions:** start-arm sequences and four variants are added. No variant brings monkey K's two means within tolerance.
- **New data finding:** in 3 of the 12 probe sessions the first entries lie on both sides of the rewarded arm. The paper describes them as the northeastern and southeastern entries.

Notes, findings, the notebook conclusions and summary, and the README now match the new numbers. Round 1 is recorded under `verifications` with the verifier's reasons and my responses.

**Not done:**
- The verifier reported no place where the claims file misreads the paper, so I added nothing to `questions/wirth-2017.yaml`.
- I did not try the vertical-channel test the verifier suggested for the eye sign; I used the eye-velocity check above.
- latency-skew stays blocked. A substitute cell set would not test the claim, which depends on gaze-aligned-dynamics.
- `tools/build_site.py` and two `tools/site_assets` files were already modified before this run. I left them alone.

## End of run

57 turns, 101 minutes, $5.43 at API prices, result: success.
