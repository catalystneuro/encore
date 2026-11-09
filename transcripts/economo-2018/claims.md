# 000006 · claims · run 39469889024

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls claims/001453 claims/000006 paper/; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

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
6	result. It is written from the pilot attempts
7	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
8	
9	An attempt has three roles, each a separate run with a separate context:
10	
11	- The **reader** reads the paper and writes the claims file: every finding,
12	  and how each is to be tested, taken from the paper. A second reader checks
13	  it against the paper. Readers never see the dandiset's data.
14	- The **author** tests the claims on the dandiset. It reads the paper to
15	  understand the claims, but the claims file binds it: it cannot change a
16	  claim, and it asks a reader for any method detail the file lacks.
17	- The **verifier** checks the author's work and must not be the author.
18	
19	So every claim and its method are fixed from the paper before anyone analyses
20	the data, and no method is chosen by the agent that runs the analysis.
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
 "file_path": "claims/000006/10.1038-s41586-018-0642-9.yaml"
}
```

```
1	# Claims for Economo, Viswanathan, Tasic et al. (2018) on dandiset 000006.
2	# Source: the abstract only. The paper is not open access (Nature, no copy in PubMed Central);
3	# its public Data availability statement was read to find the linked data and code. The
4	# claims are therefore at the level of the abstract's sentences and carry no reported numbers.
5	#
6	# When these criteria were written, the author had seen the data check only: the file list,
7	# the dandiset metadata, every column of the trial, unit and electrode tables, the unit labels
8	# (cell_type PTupper or PTlower for tagged units, unidentified for the rest) and their counts
9	# per file, the trial outcome codes, and the absence of duplicate trial tables and spike trains.
10	# No selectivity or other claim analysis had been run, and no unit had been passed through the
11	# inclusion rule below.
12	#
13	# The author had also read the analysis code the paper links to: the MATLAB scripts in Ephys.zip
14	# of the Figshare record doi:10.25378/janelia.7007846 (version 1). The method choices below
15	# follow that code where the abstract is silent:
16	# - PTupper is the thalamus-projecting type and PTlower the medulla-projecting type. The code
17	#   calls the animals with PTlower labels "MP" (medulla-projecting) and the others "TP"
18	#   (thalamus-projecting); the abstract names the types by projection only.
19	# - Times are relative to the go cue (cue_start_time). Epochs: sample -2.5 to -2.1 s, delay
20	#   -1.3 to 0 s, late delay -0.4 to 0 s, response 0 to 0.4 s, baseline -3.1 to -2.7 s.
[... 137 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-018-0642-9.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-018-0642-9.txt",
 "offset": 938,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s -m 30 https://api.figshare.com/v2/articles/7007846 | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('title'),d.get('version'));[print(f['name'],f['size'],f['download_url']) for f in d['files']]"; python tools/claims_check.py --help 2>&1 | head -20
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL -m 600 -o Ephys.zip https://ndownloader.figshare.com/files/13292708 && unzip -l Ephys.zip | grep -v -i "\.mat$" | head -60; unzip -l Ephys.zip | tail -1
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && unzip -o -q Ephys.zip 'Code/*.m' && rm Ephys.zip && sha256sum Code/*.m | head -3; cat Code/defineDataset.m Code/loadAndProcessData.m
```

```
7b100ef11924de0732773b8e6fc8e1e579a959ca3159177def9d206d62269a94  Code/CDCorrelation.m
b23e5adcc7fe2fd89f8288f84638a666a28414816177e08e0942d120a3e9e033  Code/MySmooth.m
26f8b70e8f51a55569029baeac26f03f6e91820d665373466d32e5ca2f8535c0  Code/Projections.m
function [tag, parent] = defineDataset()
global tLine 

tLine = [0 -1.3 -1.5 -2.5 -2.7];

set(0, 'DefaultAxesFontSize', 14);

parent = fullfile(cd, 'ProcessedData');

tag.group.fn = {};
tag.group.num = [];

tag.group.fn{end+1} = 'data_structure_anm369962_WR29_psth.mat';  tag.group.num(end+1) = 1;
tag.group.fn{end+1} = 'data_structure_anm369963_WR30_psth.mat';  tag.group.num(end+1) = 1;
tag.group.fn{end+1} = 'data_structure_anm369964_WR31_psth.mat';  tag.group.num(end+1) = 1;
tag.group.fn{end+1} = 'data_structure_anm372794_WR43_psth.mat';  tag.group.num(end+1) = 1;

[... 487 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Code && cat Projections.m MySmooth.m doROC.m decodingAccuracy.m
```

```
function Projections()
%Generate the plots used for Fig. 5a,b, Fig. 6a-c, EDFig. 7a,b and EDFig 10a,b.

global sm minCorrect maxTrials bootiter minError

sm = 19;
minCorrect = 50;
maxTrials = 50;
bootiter = 100;
minError = -1;

[tag, parent] = defineDataset();
tag = loadAndProcessData(parent, tag);

param.ttplot = [1 2];
param.selZwid = 1.545;
param.projZwid = 1;
param.pol = 0;
param.gr = [1 2];
param.filter = ones(tag.N.cells, 1);
[... 625 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Code && cat simplePlots.m CDCorrelation.m
```

```
function simplePlots()
%Generate the plots used for Figure 4e,f, Figure 5c, Figure 6d and EDFig 5, EDFig 10d.

global sm minCorrect maxTrials bootiter minError

sm = 19;
minCorrect = 50;
maxTrials = 50;
bootiter = 10;
minError = -1;

set(0, 'DefaultAxesFontSize', 14);

[tag, parent] = defineDataset();
tag = loadAndProcessData(parent, tag);

gr = [tag.gr(:,1) tag.gr(:,2)];

plotFiringRates(tag, gr);
showISIHists(tag, gr);
[... 617 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/Code && cat VarianceExplained.m; diff Projections.m Projections.asv; diff decodingAccuracy.m decodingAccuracy.asv; diff CDCorrelation.m CDCorrelation.asv
```

```
Exit code 2
function VarianceExplained()
%Generate the plots used for EDFig. 6.

global sm minCorrect maxTrials bootiter minError

sm = 39;
minCorrect = 50;
maxTrials = 50;
bootiter = 1000;
minError = -1;


[tag, parent] = defineDataset();
tag = loadAndProcessData(parent, tag);


cl = 2.5;
param.Ncomp = 6;
param.useix = 1:1000;
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
cat schemas/claims.schema.json | head -200; grep -rl "elsewhere" claims | head
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
[... 190 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,400p schemas/claims.schema.json; grep -n "where:" claims/*/*.yaml | head -5
```

```
}
    },
    "checks": {
      "description": "Checks of the claims file against the paper by a second reader (docs/protocol.md, Reader, step 5), oldest first. The file is ready for an attempt when the last says so.",
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "date",
          "kind",
          "ready"
        ],
        "properties": {
          "date": {
            "type": "string",
            "format": "date"
          },
          "kind": {
            "enum": [
[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s -m 30 https://api.dandiarchive.org/api/dandisets/000006/versions/draft/info/ | python3 -c "import json,sys;d=json.load(sys.stdin);m=d['metadata'];print(m['name']);print(m.get('description'));print(d['version'])"
```

Result: the fetched text is not kept.

**Agent**

Paper text is complete (main, Methods, Extended Data legends); the paper's MATLAB code from Figshare (Ephys.zip, Code/) has been read. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000006/10.1038-s41586-018-0642-9.yaml",
 "content": "# Claims for Economo, Viswanathan, Tasic et al. (2018) on dandiset 000006.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-20, protocol\n# as stated in docs/protocol.md (pilot-10), Reader steps 1 to 4.\n#\n# Why this file was rewritten. The earlier file was written from the abstract only and is\n# deprecated. Read against the full text on 2026-10-20, its claims pt-lower-late-and-motor and\n# pt-types-differ-in-timing were tested with fractions of selective units and a label-shuffle null,\n# measures the paper does not use (it uses coding directions, a hierarchical bootstrap and single\n# neuron early selectivity), and eleven of the paper's findings on these data had no claim. This\n# file is written again from the full text. Ids are kept where the finding is the same:\n# pt-types-transcriptomic, pt-types-shared-targets, pt-upper-thalamus-projection,\n# pt-lower-medulla-projection, pt-preparatory-activity, pt-upper-early-preparatory,\n# pt-upper-persistent, pt-lower-late-and-motor and pt-types-differ-in-timing. All their criteria\n# are new; the old shuffle null, McNemar and Fisher tests are gone, as the paper uses none of them.\n# pt-lower-late-and-motor now tests selectivity along CDlate and CDgo (Fig. 6b, c; Extended Data\n# Fig. 7b); pt-types-differ-in-timing is now the summary of the coding direction claims it\n# depends on. The other claims are new.\n#\n# Text read: the version of record (Nature 563, 79-84, 2018), as the PDF supplied by a person and\n# its text extraction (paper/10.1038-s41586-018-0642-9.txt): main text, Methods, Extended Data\n# Figs 1 to 10 legends and the Reporting Summary. The Supplementary Information (Supplementary\n# Tables 1 to 4: reconstructed neurons, mice, viruses and coordinates) is not in the text. No\n# claim on these data rests on it; the reconstruction counts of pt-types-account-for-all-pt are\n# quoted from the main text, which cites Supplementary Table 1.\n#\n# Code read: the paper links \"https://github.com/SvobodaJanelia\" (an organisation, no repository\n# named) and deposits its electrophysiology at Figshare doi:10.25378/janelia.7007846 version 1,\n# file Ephys.zip (Figshare file id 13292708), whose folder Code/ holds the MATLAB analysis code\n# (defineDataset.m, loadAndProcessData.m, Projections.m for Fig. 5a, b, Fig. 6a-c, Extended Data\n# Figs 7a, b and 10a, b; CDCorrelation.m for Extended Data Figs 7c, e and 10c; decodingAccuracy.m\n# for Extended Data Fig. 9; simplePlots.m for Fig. 4e, f, 5c, 6d and Extended Data Figs 5, 10d;\n# VarianceExplained.m for Extended Data Fig. 6; MySmooth.m, doROC.m). Only the .m files were\n# read, not the data files. Below, \"the code\" is this folder.\n#\n# The data the paper used for the claims on this dandiset (Methods, Electrophysiology). Mice\n# performed a tactile delayed-response task: sample epoch 1.0 s (pole in reach and still), delay\n# 1.3 s, auditory go cue (3.4 kHz, 0.1 s), then directional licking, lick right for the caudal\n# (posterior) pole and lick left for the rostral one. Times below are relative to the go cue;\n# the code's epochs are baseline -3.1 to -2.7 s, sample -2.5 to -2.1 s (the first 400 ms of the\n# sample epoch), delay -1.3 to 0 s, late delay -0.4 to 0 s and response 0 to 0.4 s; pole\n# movement starts at -2.7 s and the full sample epoch is -2.5 to -1.5 s. Units were recorded in\n# ALM with two-shank 64-channel silicon probes and identified by antidromic photostimulation and\n# a collision test: PTupper (thalamus-projecting) neurons tagged from the thalamus, 61 cells in 8\n# mice, 37 sessions, left hemisphere; PTlower (medulla-projecting) neurons tagged from the\n# medulla, 69 cells in 4 mice, 23 sessions, both hemispheres. 143 tagged units were sorted, 130\n# kept. The code calls the PTlower cohort \"MP\" (mice WR29, WR30, WR31, WR43, with right\n# hemisphere recordings of WR29 and WR30 under separate animal numbers 29.5 and 30.5) and the\n# PTupper cohort \"TP\" (WR33, WR34, WR36, WR38, WR39, WR40, WR41, WR42). Also 495 unidentified\n# single units from 15 sessions of the PTupper cohort and 511 from 14 sessions of the PTlower\n# cohort. Measured variables: spike times, unit depth (manipulator reading), trial type (lick\n# left or right), outcome, early licks, photostimulation, lick times; videography at 400 Hz from 3\n# mice, 14 sessions, for reaction times. The dandiset's description says it holds the\n# extracellular recordings of the two PT populations in ALM; the anatomy and sequencing data are\n# elsewhere (see the claims with data elsewhere).\n#\n# Methods shared by the electrophysiology claims, with their source.\n# - Trials (code, defineDataset.m): correct trials of each type without early licks and without\n#   photostimulation (\"hit&L&~lickearly&~stim\" and the same for R). Methods, Mouse behaviour:\n#   trials with premature licks were excluded from all analyses.\n# - Trial range per unit: the code keeps, for the last-lick-aligned rates, trials from 10 after\n#   the unit's first trial with a spike to 10 before the earlier of its last trial with a spike\n#   and the session's last correct trial (loadAndProcessData.m, ObjToLickPSTH). The go-cue-aligned\n#   rates come precomputed in the data files, so their range is open: readings (a) the same range,\n#   (b) all trials of the session.\n# - Unit inclusion. Methods: units from sessions where performance was not greater than 65% for\n#   both trial types, or with less than 50 correct trials of each type, were excluded (13 of 143\n#   rejected, 130 kept). The code (loadAndProcessData.m) counts per unit over the trials in its\n#   range: more than 50 correct trials of each type (strictly more; the Methods keep 50), more\n#   than 3.2 spikes per trial (spikes over the range of trials with spikes; the Methods do not\n#   name this rule, the code settles it), more than 65% correct for each type, and unit quality\n#   Excellent, Good or single. Readings: (a) the code's per-unit rule, (b) the Methods' session\n#   rule with at least 50 trials. The selection is checked by pt-tagged-units (61 and 69).\n# - Rates: 5 ms bins, causal 50 ms boxcar (Methods; the code's MySmooth with 19 gives 10 bins,\n#   the current and the nine before).\n# - Coding direction (Methods, equations 1 and 2; code, Projections.m DirectionVector): per\n#   neuron, mean rate on lick right minus lick left trials in a 400 ms window, over the root of\n#   the summed across-trial variances; NaN set to 0; the vector over the population normalised\n#   by its L1 norm. Windows CDearly -2.5 to -2.1 s, CDlate -0.4 to 0 s, CDgo 0 to 0.4 s (the code\n#   takes time >= start and < end); CDgo orthogonalised to CDlate by Gram-Schmidt. Separate CDs\n#   per population.\n# - Projection and selectivity (Methods, equations 3 to 5; code, projectOntoVector): the\n#   trial-averaged rates of each trial type times the CD; selectivity is the right projection\n#   minus the left. For go-cue-aligned rates the code subtracts the selectivity's mean in the\n#   baseline epoch (plotProjectionSelectivity); the Methods are silent, the code settles it.\n# - Hierarchical bootstrap (Methods): 1,000 iterations; draw M mice with replacement from the\n#   cohort (M the cohort size), then n neurons with replacement (n the population size), and for\n#   each neuron 50 correct trials of each type with replacement. Selectivity is significant where\n#   the 5th percentile of the bootstrap is above zero (5-95% interval, one-sided P < 0.05). The\n#   code settles how: neurons are drawn from the pooled neurons of the drawn mice (a mouse drawn\n#   twice is pooled once), each drawn neuron's weight in the CD is multiplied by the number of\n#   times it was drawn, the resampled trials enter the CD only and the projection uses the\n#   trial-averaged rates of all trials. Open, with readings: what a mouse is, (a) the 4 and 8\n#   mice of the Methods, (b) the code's animal numbers (6 for PTlower, with 29.5 and 30.5); and\n#   whether resampled trials also enter the projected rates, (a) no, as the code, (b) yes.\n#   Projections.m runs 100 iterations and draws a band of mean +/- 1.545 s.d.; that is a variant.\n# - Readings. For a reported number that can be read in more than one way, the claim holds if\n#   it matches under any reading. For an open method detail, the notebook runs every reading;\n#   the outcome is the one they all give, and the claim is methods_underspecified when they give\n#   different outcomes.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000006\"\npaper: doi:10.1038/s41586-018-0642-9\nclaims:\n- id: pt-types-transcriptomic\n  statement: In ALM scRNA-seq, PT neurons map to three glutamatergic transcriptomic clusters (Slco2a1,\n    and the closely related Npsr1 and Hpgd), and with axonal reconstructions this divides PT neurons\n    into two cell types.\n  source: Results, Two types of PT neuron in layer 5, paragraphs 1 and 5; Fig. 1\n  quote: ALM PT neurons mapped to three transcriptomic clusters ... Axonal reconstructions and scRNA-seq\n    data suggest that PT neurons can be divided into two distinct cell types.\n  expected:\n  - quantity: glutamatergic clusters in ALM\n    value: 27\n    tolerance: 0\n  data: elsewhere\n  where: scRNA-seq data of Tasic et al. 2018, doi:10.1038/s41586-018-0654-5 (Allen Institute); Figshare\n    doi:10.25378/janelia.7007846 version 1, Seq.zip\n  criterion: Not testable on this dandiset, which holds electrophysiology only. The cluster count is\n    an exact count (tolerance 0).\n- id: pt-upper-thalamus-projection\n  statement: Of 12 reconstructed PT neurons, 8 innervate the thalamus.\n  source: Results, Two types of PT neuron in layer 5, paragraph 2; Fig. 2a, b; Extended Data Fig. 2\n  quote: \"Patterns of axonal collaterals revealed two neuron types: one group innervated the thalamus\n    (n = 8; Fig. 2a, b; green hues and Extended Data Fig. 2)\"\n  expected:\n  - quantity: thalamus-projecting reconstructed neurons\n    value: 8\n    tolerance: 0\n  data: elsewhere\n  where: Figshare doi:10.25378/janelia.7007846 version 1, Axons.zip (MouseLight reconstructions)\n- id: pt-lower-medulla-projection\n  statement: The other 4 of 12 reconstructed PT neurons bypass the thalamus and branch in the medulla,\n    including the reticular nuclei with premotor neurons for orofacial movements.\n  source: Results, Two types of PT neuron in layer 5, paragraph 2; Fig. 2a, b\n  quote: the other group bypassed the thalamus and branched in the medulla, including the reticular\n    nuclei containing premotor neurons for orofacial movements23 (n = 4; magenta hues)\n  expected:\n  - quantity: medulla-projecting reconstructed neurons\n    value: 4\n    tolerance: 0\n  data: elsewhere\n  where: Figshare doi:10.25378/janelia.7007846 version 1, Axons.zip (MouseLight reconstructions)\n- id: pt-types-shared-targets\n  statement: Both PT types project to several shared targets; all reconstructed cells innervate the\n    superior colliculus, and both types send collaterals to the subthalamic nucleus, zona incerta and\n    midbrain reticular nucleus.\n  source: Results, Two types of PT neuron in layer 5, paragraph 2; Extended Data Fig. 2e legend\n  quote: All cells innervated the superior colliculus and subsets of both groups branched in other areas\n    ... Both cell types extended axon collaterals locally within the same sublamina as their somata, the\n    subthalamic nucleus, zona incerta, and the midbrain reticular nucleus.\n  data: elsewhere\n  where: Figshare doi:10.25378/janelia.7007846 version 1, Axons.zip and Anatomy.zip\n- id: pt-retrograde-sublaminae\n  statement: Thalamus-projecting PT neurons lie in upper L5b and medulla-projecting PT neurons in lower\n    L5b; few neurons are co-labelled from thalamus and medulla (2.2%, 22 of 984) while many are\n    co-labelled from thalamus and superior colliculus (77.1%, 687 of 890).\n  source: Results, Two types of PT neuron in layer 5, paragraph 3; Fig. 2c, d; Extended Data Fig. 3\n  quote: Few neurons were co-labelled by injections into the thalamus and medulla (2.2%; 22 out of 984\n    cells labelled from either location), whereas many neurons were co-labelled by injections into the\n    thalamus and superior colliculus (77.1%; 687 out of 890 thalamus-labelled cells)\n  expected:\n  - quantity: co-labelled from thalamus and medulla\n    value: 2.2\n    tolerance: 0.22\n    unit: percent\n  - quantity: co-labelled from thalamus and superior colliculus\n    value: 77.1\n    tolerance: 7.71\n    unit: percent\n  data: elsewhere\n  where: Figshare doi:10.25378/janelia.7007846 version 1, Anatomy.zip\n- id: pt-projection-cluster-mapping\n  statement: All 62 medulla-projecting PT neurons map to the Slco2a1 cluster, and 91 of 94\n    thalamus-projecting PT neurons map to the Npsr1 and Hpgd clusters.\n  source: Results, Two types of PT neuron in layer 5, paragraphs 4 and 5; Fig. 2e, f\n  quote: All (62 out of 62) medulla- projecting PT neurons mapped to the Slco2a1 taxonomic cluster.\n    Similarly, thalamus-projecting PT neurons mapped to the Npsr1 and Hpgd clusters (91 out of 94\n  expected:\n  - quantity: medulla-projecting neurons in Slco2a1\n    value: 62\n    tolerance: 0\n  - quantity: thalamus-projecting neurons in Npsr1 or Hpgd\n    value: 91\n    tolerance: 9.1\n  data: elsewhere\n  where: scRNA-seq data of Tasic et al. 2018, doi:10.1038/s41586-018-0654-5; Figshare\n    doi:10.25378/janelia.7007846 version 1, Seq.zip\n- id: pt-types-account-for-all-pt\n  statement: All 18 partially and fully reconstructed PT neurons project to the superior colliculus and\n    none lacks projections to both thalamus and medulla, so most if not all PT neurons belong to the two\n    types.\n  source: Results, Two types of PT neuron in layer 5, paragraph 5; Supplementary Table 1 (not in the\n    text read)\n  quote: All (18 out of 18) partially and fully reconstructed PT neurons projected to the superior colliculus\n    and no (0 out of 18) PT neurons lacked projections to both the thalamus and medulla\n  data: elsewhere\n  where: Figshare doi:10.25378/janelia.7007846 version 1, Axons.zip\n- id: pt-marker-genes\n  statement: smFISH confirms Slco2a1 as a PTlower marker and Npnt as a PTupper marker (Slco2a1 puncta\n    IQR 1-2.5 in PTupper against 6-22 in PTlower; Npnt IQR 16-40 in PTupper against 1-9 in PTlower).\n  source: Results, Two types of PT neuron in layer 5, paragraph 6; Fig. 3c legend\n  quote: Slco2a1, PTupper interquartile range (IQR) = 1–2.5 puncta, n = 60; Slco2a1, PTlower IQR = 6–22,\n    n = 95; Npnt, PTupper IQR = 16–40, n = 145; Npnt, PTlower IQR = 1–9, n = 69\n  data: elsewhere\n  where: Figshare doi:10.25378/janelia.7007846 version 1, Anatomy.zip\n- id: pt-bulk-sc-fold-change-correlation\n  statement: Fold changes between PTupper and PTlower of the 200 most discriminative genes correlate\n    between scRNA-seq and bulk RNA-seq (Pearson's r = 0.87).\n  source: Extended Data Fig. 4i legend\n  quote: The correlation coefficient (Pearson’s r) in fold change expression was 0.87 for this set of\n    200 differentially expressed genes.\n  expected:\n  - quantity: Pearson's r\n    value: 0.87\n    tolerance: 0.087\n  data: elsewhere\n  where: GEO GSE119182 (bulk RNA-seq); scRNA-seq of Tasic et al. 2018, doi:10.1038/s41586-018-0654-5\n- id: pt-tagged-units\n  statement: The recordings yield 61 identified PTupper cells from 8 mice and 69 identified PTlower\n    neurons from 4 mice after exclusions (130 of 143 tagged units kept).\n  source: Results, Cell-type-specific recordings, paragraph 2; Methods, Electrophysiology data analysis\n  quote: (61 PTupper cells, 8 mice; 69 PTlower neurons, 4 mice; Fig. 4d and Extended Data Fig. 5)\n  expected:\n  - quantity: included PTupper units\n    value: 61\n    tolerance: 6.1\n  - quantity: included PTlower units\n    value: 69\n    tolerance: 6.9\n  - quantity: PTupper mice\n    value: 8\n    tolerance: 0\n  - quantity: PTlower mice\n    value: 4\n    tolerance: 0\n  criterion: The unit selection of the opening comment, under each of its readings (code's per-unit\n    rule; Methods' session rule), applied to the tagged units of the dandiset. Reproduced when one\n    reading gives both unit counts within tolerance and the mouse counts exactly. The counts under\n    every reading are shown, with the 143 tagged units before exclusion. The reading that matches is\n    the selection the other electrophysiology claims use; when both match, both are carried.\n- id: pt-depth\n  statement: Identified PTupper cells are at more superficial recording depths than PTlower neurons.\n  source: Results, Cell-type-specific recordings, paragraph 2; Fig. 4e\n  quote: Identified PTupper cells were at more superficial recording depths than PTlower neurons, consistent\n    with retrograde labelling experiments\n  depends_on:\n  - pt-tagged-units\n  criterion: Depth is the micromanipulator reading, uncorrected (Fig. 4e legend, Methods). The paper\n    reports no test; Fig. 4e shows mean +/- s.d. Reproduced when the mean depth of included PTupper\n    units is smaller than that of PTlower units. Shown both with all units, as the code's error bars,\n    and without the right-hemisphere PTlower recordings (animals 29.5 and 30.5), which the code leaves\n    out of the plotted points (simplePlots.m, plotDepth).\n- id: pt-spike-rates-similar\n  statement: Baseline and trial-averaged peak spike rates do not differ between PTupper (baseline 4.3 +/-\n    3.5 Hz, peak 17.7 +/- 13.8 Hz, median +/- s.d.) and PTlower cells (5.2 +/- 4.8 Hz, 17.2 +/- 22 Hz).\n  source: Results, Cell-type-specific recordings, paragraph 3\n  quote: Baseline and trial-averaged peak spike rates were not significantly different (P > 0.1, two-sided\n    t-test) in PTupper cells (baseline 4.3 ± 3.5 Hz; peak 17.7 ± 13.8 Hz; median ± s.d.) compared to PTlower\n    cells (baseline 5.2 ± 4.8 Hz; peak 17.2 ± 22 Hz)\n  statistics:\n  - test: two-sided t-test (Student's, Methods)\n    p: 0.1\n    p_relation: \">\"\n    n: 61 PTupper and 69 PTlower neurons\n  depends_on:\n  - pt-tagged-units\n  expected:\n  - quantity: PTupper median baseline rate\n    value: 4.3\n    tolerance: 0.43\n    unit: Hz\n  - quantity: PTupper median peak rate\n    value: 17.7\n    tolerance: 1.77\n    unit: Hz\n  - quantity: PTlower median baseline rate\n    value: 5.2\n    tolerance: 0.52\n    unit: Hz\n  - quantity: PTlower median peak rate\n    value: 17.2\n    tolerance: 1.72\n    unit: Hz\n  criterion: From the code (simplePlots.m, plotFiringRates). Baseline rate is the mean, over lick left\n    and lick right correct trials, of each trial type's mean rate in the baseline epoch (-3.1 to -2.7\n    s); peak rate is the maximum over time of the smoothed trial-averaged rate of either trial type.\n    A claim of absence, judged on the paper's test, a two-sided Student's t-test between the two\n    populations, for baseline and for peak. Reproduced when neither test has p < 0.05 and the four\n    medians are within tolerance; partially reproduced when the tests hold and a median is out of\n    tolerance; not reproduced when either test has p < 0.05. Whether p exceeds the reported bound\n    0.1 is reported, as are the s.d.\n- id: pt-lower-heterogeneous-rates\n  statement: Spike rates are more heterogeneous across the PTlower population than the PTupper population,\n    for baseline (P = 0.02) and peak rates (P = 3 x 10^-4).\n  source: Results, Cell-type-specific recordings, paragraph 3\n  quote: \"Spike rates in PTlower cells were more heterogeneous across the population (baseline: P = 0.02;\n    peak: P = 3 × 10−4; χ2 test)\"\n  statistics:\n  - about: baseline rate variance, PTlower against PTupper\n    test: χ2 test\n    p: 0.02\n  - about: peak rate variance, PTlower against PTupper\n    test: χ2 test\n    p: 3.0e-04\n  depends_on:\n  - pt-spike-rates-similar\n  criterion: Rates as in pt-spike-rates-similar. The paper names a chi-squared test; the code compares\n    variances with MATLAB's vartest2, a two-sample F test (simplePlots.m). The Methods come first, and\n    the two-sample variance test with a chi-squared statistic is Bartlett's test, so Bartlett's test is\n    the main reading and the F test of the code is a variant. Reproduced when, for both baseline and\n    peak, the PTlower variance is larger and the test has p < 0.05; partially reproduced when that\n    holds for one. The F test result is shown.\n- id: pt-lower-bursting\n  statement: A substantial proportion of PTlower neurons fire bursts (18.8%), which are rare among PTupper\n    cells (3.3%).\n  source: Results, Cell-type-specific recordings, paragraph 3; Extended Data Fig. 5c\n  quote: A substantial proportion of PTlower neurons displayed spike bursts (18.8%), which were rare among\n    PTupper cells (3.3%; P = 0.006, Fisher’s exact test; Extended Data Fig. 5c).\n  statistics:\n  - test: Fisher's exact test\n    p: 0.006\n    n: 61 PTupper and 69 PTlower neurons\n  depends_on:\n  - pt-tagged-units\n  expected:\n  - quantity: bursting PTlower neurons\n    value: 18.8\n    tolerance: 1.88\n    unit: percent\n  - quantity: bursting PTupper neurons\n    value: 3.3\n    tolerance: 0.33\n    unit: percent\n  criterion: A bursting cell has more than 10% of its inter-spike intervals shorter than 5 ms (Extended\n    Data Fig. 5c legend). From the code (simplePlots.m, showISIHists) intervals are taken within trials\n    only, an interval across a trial boundary being dropped from the count of short intervals but kept\n    in the denominator, over all of the unit's spikes. Reproduced when both percentages are within\n    tolerance and the two-sided Fisher exact test on the 2 x 2 counts has p < 0.05; partially\n    reproduced when the test holds and a percentage is out of tolerance.\n- id: pt-selective-any-epoch\n  statement: Most recorded PT neurons (122 of 130, 94%) have significant trial-type selectivity in at\n    least one task epoch.\n  source: Results, Cell-type-specific recordings, paragraph 4\n  quote: Most recorded PT neurons had significant selectivity, defined as the difference in spike rate\n    between trial types (‘lick left’ versus ‘lick right’), during at least one task epoch (P < 0.01, two-sided\n    Mann–Whitney U-test; 122 out of 130; 94%).\n  depends_on:\n  - pt-tagged-units\n  expected:\n  - quantity: selective PT neurons\n    value: 122\n    tolerance: 12.2\n  criterion: Per unit and epoch, the mean rate of each correct trial in the epoch, lick right against\n    lick left, two-sided Mann-Whitney test at p < 0.01. The code (simplePlots.m, sigCellsByType) counts a\n    unit when any of the sample (-2.5 to -2.1 s), delay (-1.3 to 0 s) and response (0 to 0.4 s) epochs\n    is significant. \"Task epoch\" in the text can also be read as the full sample epoch (-2.5 to -1.5 s)\n    in place of its first 400 ms; both readings are run, and the count holds if it is within tolerance\n    under one.\n- id: pt-variance-explained\n  statement: Trial-averaged activity patterns are nearly as diverse within each PT population as across\n    all neurons recorded in ALM; cell type explains relatively little of the variance.\n  source: Results, Cell-type-specific recordings, paragraph 4; Extended Data Fig. 6; Discussion,\n    paragraph 3\n  quote: Trial-averaged activity patterns were nearly as diverse within each PT population as across all\n    neurons recorded within ALM (Extended Data Fig. 6).\n  depends_on:\n  - pt-tagged-units\n  criterion: From the Methods (variance explained paragraph) and the code (VarianceExplained.m).\n    Trial-averaged lick right and lick left rates of each neuron, concatenated and z-scored (Methods);\n    PCA per PT population; fraction of variance explained by 1 to 6 components (the code's Ncomp);\n    compared with 1,000 size-matched samples drawn without replacement from the unidentified units of\n    the same cohort (the code's groups 3 and 4). The paper gives no threshold for \"nearly as diverse\";\n    Extended Data Fig. 6b, d plot the ratio of PT to unidentified variance explained on an axis from 1\n    to 1.3 (the code's ylim). Reproduced when, for both populations, the median ratio is at most 1.3 at\n    every number of components. Variants that do not change the outcome are the code's own choices,\n    which differ from the Methods text (a 100 ms smoothing, sm = 39; baseline subtraction and division\n    by s.d. in place of z-scoring; the first 1,000 time bins). The asterisks of the figure (ratio\n    above 1, z > 1.645 of the bootstrap) are reported.\n- id: pt-preparatory-activity\n  statement: Along the late delay coding direction (CDlate) selectivity is substantial in both PT types,\n    with 40 of 61 PTupper and 44 of 69 PTlower neurons selective.\n  source: Results, Preparatory activity, paragraph 2; Extended Data Fig. 7a, b\n  quote: \"along a different direction in activity space, which maximized selectivity at the end of the\n    delay epoch, CDlate, selectivity was substantial in both cell types18 (Extended Data Fig. 7a, b;\n    PTupper: 40 out of 61 neurons selective; PTlower: 44 out of 69)\"\n  depends_on:\n  - pt-tagged-units\n  expected:\n  - quantity: selective PTupper neurons in the late delay epoch\n    value: 40\n    tolerance: 4\n  - quantity: selective PTlower neurons in the late delay epoch\n    value: 44\n    tolerance: 4.4\n  criterion: Two parts. (a) Counts from the code (simplePlots.m, sigCellsByType) - a unit is selective\n    when the mean rates of its correct trials in the late delay epoch (-0.4 to 0 s) differ between\n    lick right and lick left by a two-sided Mann-Whitney test at p < 0.01; both counts within\n    tolerance. (b) Selectivity along each population's CDlate, with the shared bootstrap, is\n    significant (5th percentile above zero) over the late delay epoch in both populations, read as\n    (i) at every time bin from -0.4 to 0 s, or (ii) for the mean over that window. Reproduced when\n    both parts hold, partially reproduced when one does.\n- id: pt-upper-early-preparatory\n  statement: Along the early coding direction (CDearly, first 400 ms of the sample epoch), selectivity is\n    larger and more consistent across trials in the PTupper population than in the PTlower population.\n  source: Results, Preparatory activity, paragraph 2; Fig. 5a, b\n  quote: In this projection, selectivity was larger and more consistent across trials in the PTupper population\n    compared to the PTlower population (Fig. 5b).\n  depends_on:\n  - pt-tagged-units\n  criterion: CDearly and selectivity with the shared bootstrap. The paper reports no test or window for\n    \"larger\". Readings for the window over which bootstrap selectivity is averaged, (a) -2.5 to -2.1\n    s, the CDearly window, (b) the sample epoch -2.5 to -1.5 s. Larger holds when the bootstrap median\n    of the PTupper mean exceeds that of PTlower and the PTupper 5th percentile exceeds the PTlower\n    median. \"More consistent across trials\" is read as a smaller spread of the bootstrap (which\n    resamples trials) relative to its median, the s.d. over median. Reproduced when both hold,\n    partially reproduced when larger holds alone, not reproduced when larger does not hold.\n- id: pt-upper-persistent\n  statement: In the PTupper population, selectivity along CDearly remains constant through the sample\n    and delay epochs until the go cue.\n  source: Results, Preparatory activity, paragraph 2; Fig. 5b\n  quote: Furthermore, selectivity in the PTupper population remained constant throughout the sample and\n    delay epochs until the go cue, implying retention of decision-related information.\n  depends_on:\n  - pt-upper-early-preparatory\n  criterion: PTupper selectivity along its CDearly, shared bootstrap. Readings of \"remained constant\"\n    (the paper names no measure), (a) the 5th percentile is above zero at every time bin from -2.1 s\n    to the go cue; (b) the mean over the last 400 ms before the go cue (-0.4 to 0 s) is significant by\n    the bootstrap (fewer than 5% of iterations at or below zero), the window and test the paper uses\n    for PTlower (pt-lower-cdearly-decay). Reproduced when the readings agree that it holds; the ratio\n    of the mean in -0.4 to 0 s to the mean in -2.5 to -2.1 s is reported.\n- id: pt-lower-cdearly-decay\n  statement: In the PTlower population, selectivity along CDearly decays rapidly, with no significant\n    selectivity in the 400 ms before the go cue (P = 0.34, bootstrap).\n  source: Results, Preparatory activity, paragraph 2; Fig. 5b\n  quote: By contrast, selectivity in the PTlower population decayed rapidly along CDearly (no significant\n    selectivity in 400 ms preceding go cue; P = 0.34, bootstrap).\n  statistics:\n  - test: bootstrap\n    p: 0.34\n    n: 69 PTlower neurons, 4 mice\n  depends_on:\n  - pt-tagged-units\n  criterion: A claim of absence, judged on the paper's test. PTlower selectivity along its CDearly with\n    the shared bootstrap; the p-value is the fraction of iterations in which the mean selectivity over\n    -0.4 to 0 s is at or below zero (one-sided, as the paper's bootstrap tests are). Reproduced when p\n    >= 0.05; not reproduced when p < 0.05. The p-value is compared with the reported 0.34, and the\n    selectivity in that window is given either way.\n- id: pt-cd-stability\n  statement: The coding direction stays more similar across the sample and delay epochs in the PTupper\n    population than in the PTlower population, whose delay-epoch coding directions are largely\n    orthogonal to those of the sample epoch.\n  source: Results, Preparatory activity, paragraph 2; Extended Data Fig. 7c, d\n  quote: For the PTupper population, the CD remained more similar across the sample and delay epochs compared\n    to the PTlower population (Extended Data Fig. 7c, d).\n  depends_on:\n  - pt-tagged-units\n  criterion: The paper reports no number or test. Two measures from the paper. (a) Extended Data Fig. 7d\n    legend and the code (Projections.m, plotEarlyLateCorr) - Pearson's r across the units of a\n    population between the CDearly and CDlate weights. (b) Methods and the code (CDCorrelation.m,\n    compareEpochs) - the inner product of the unit-normalised CDs of the sample (-2.5 to -2.1 s) and\n    late delay (-0.4 to 0 s) windows, mean over the bootstrap (the code uses 100 iterations, all\n    trials per type up to 500). Reproduced when PTupper's value exceeds PTlower's under both\n    measures. The code's interval (mean +/- 1.96 s.e. over iterations), the r p-values, and the\n    PTlower values (for \"largely orthogonal\", which the paper does not quantify) are reported.\n- id: pt-single-neuron-early-selectivity\n  statement: Individual PTupper neurons have higher early selectivity than PTlower neurons (0.41 +/- 0.04\n    against 0.25 +/- 0.02, mean +/- s.e.m., P < 0.01).\n  source: Results, Preparatory activity, paragraph 2\n  quote: \"exhibited higher early selectivity (PTupper: 0.41 ± 0.04; mean ± s.e.m.; PTlower: 0.25 ± 0.02;\n    P < 0.01)\"\n  statistics:\n  - test: not named\n    p: 0.01\n    p_relation: \"<\"\n    n: 61 PTupper and 69 PTlower neurons\n  depends_on:\n  - pt-tagged-units\n  expected:\n  - quantity: PTupper mean early selectivity\n    value: 0.41\n    tolerance: 0.04\n  - quantity: PTlower mean early selectivity\n    value: 0.25\n    tolerance: 0.02\n  criterion: Tolerances are the reported s.e.m. The paper does not define \"early selectivity\" or name\n    the test. Readings of the measure, each from the first 400 ms of the sample epoch (-2.5 to -2.1 s),\n    over correct trials, (a) the absolute value of the unit's CD weight before normalisation, the\n    difference of mean rates over the root of the summed variances (Methods, equation 1); (b) the d'\n    at the accuracy-maximising threshold that decodingAccuracy.m computes (acc.dprime, from doROC.m),\n    as an absolute value. Readings of the test, (i) two-sided Student's t-test (Methods - all\n    two-sample t-tests were Student's), (ii) two-sided Mann-Whitney test (used for the same window in\n    Extended Data Fig. 9). Reproduced when, under one reading of the measure, both means are within\n    tolerance and PTupper is higher with p < 0.01 under one of the tests; partially reproduced when\n    PTupper is higher with p < 0.01 but a mean is out of tolerance under every reading.\n- id: pt-upper-decoding\n  statement: Single PTupper neurons decode trial type better than PTlower neurons in the first 400 ms of\n    the sample epoch; 24.6% (15 of 61) of PTupper and 4.4% (3 of 69) of PTlower neurons reach 70%\n    accuracy, mean accuracy is 64.4 +/- 1.0% against 58.9 +/- 0.6%, and the ten most discriminative\n    neurons are all PTupper.\n  source: Extended Data Fig. 9a, b legend; Results, Preparatory activity, paragraph 2\n  quote: 24.6% (15 out of 61) of PTupper neurons predicted trial type with at least 70% accuracy, whereas only\n    4.4% (3 out of 69) of PTlower neurons did so. Mean accuracy was also significantly higher in PTupper neurons\n    (PTupper 64.4 ± 1.0%; PTlower 58.9 ± 0.6%, mean ± s.e.m.; P = 1 × 10−4, two-sided Mann–Whitney test).\n    The ten most discriminative neurons all belonged to the PTupper population.\n  statistics:\n  - test: two-sided Mann–Whitney test\n    statistic: 64.4 ± 1.0% against 58.9 ± 0.6% (mean ± s.e.m.)\n    p: 1.0e-04\n    n: 61 PTupper and 69 PTlower neurons\n  depends_on:\n  - pt-tagged-units\n  expected:\n  - quantity: PTupper neurons with at least 70% accuracy\n    value: 15\n    tolerance: 1.5\n  - quantity: PTlower neurons with at least 70% accuracy\n    value: 3\n    tolerance: 0.3\n  - quantity: PTupper mean accuracy\n    value: 64.4\n    tolerance: 1.0\n    unit: percent\n  - quantity: PTlower mean accuracy\n    value: 58.9\n    tolerance: 0.6\n    unit: percent\n  criterion: Methods (single-cell decoding) and the code (decodingAccuracy.m, doROC.m). Per unit, the\n    mean rate of each correct trial in -2.5 to -2.1 s; every observed rate is a threshold, with the\n    polarity set by the side of the ROC area; accuracy is the maximum over thresholds of the fraction\n    of trials classified correctly. Mean tolerances are the reported s.e.m. Reproduced when all four\n    numbers are within tolerance, the two-sided Mann-Whitney test has p < 0.05 with PTupper higher,\n    and the ten most accurate units are all PTupper; partially reproduced when the test holds and some\n    of the rest do not.\n- id: pt-upper-decoding-rectified\n  statement: Decoding from spike rates rectified at baseline, no PTlower neuron reaches 70% accuracy while\n    the same 24.6% of PTupper neurons do, PTupper neurons make up 20 of the 21 most predictive, and mean\n    accuracy is 62.7 +/- 1.1% against 56.7 +/- 0.4%.\n  source: Extended Data Fig. 9c, d legend\n  quote: Disregarding spike rate changes below baseline, no PTlower neurons predicted trial type with at least\n    70% accuracy, whereas the same 24.6% of PTupper neurons continued to do so and accounted for 20 out of\n    21 of the most predictive neurons (PTupper 62.7 ± 1.1%; PTlower 56.7 ± 0.4%, mean ± s.e.m.; P = 9 × 10−7,\n    two-sided Mann–Whitney test).\n  statistics:\n  - test: two-sided Mann–Whitney test\n    statistic: 62.7 ± 1.1% against 56.7 ± 0.4% (mean ± s.e.m.)\n    p: 9.0e-07\n    n: 61 PTupper and 69 PTlower neurons\n  depends_on:\n  - pt-upper-decoding\n  expected:\n  - quantity: PTlower neurons with at least 70% accuracy\n    value: 0\n    tolerance: 0\n  - quantity: PTupper neurons with at least 70% accuracy\n    value: 15\n    tolerance: 1.5\n  - quantity: PTupper among the 21 most predictive neurons\n    value: 20\n    tolerance: 2\n  - quantity: PTupper mean accuracy\n    value: 62.7\n    tolerance: 1.1\n    unit: percent\n  - quantity: PTlower mean accuracy\n    value: 56.7\n    tolerance: 0.4\n    unit: percent\n  criterion: As pt-upper-decoding, after subtracting from each trial's rate the unit's baseline (the\n    mean over the two trial types of their mean rate in -3.1 to -2.7 s) and setting negative values to\n    zero (decodingAccuracy.m, signConstraint 1). Reproduced when all numbers are within tolerance and\n    the Mann-Whitney test has p < 0.05 with PTupper higher; partially reproduced when the test holds\n    and a number is out of tolerance.\n- id: pt-lower-late-and-motor\n  statement: PTlower neurons carry late preparatory activity (selectivity along CDlate) and a movement\n    command; along the go cue coding direction (CDgo) selectivity is larger, emerges faster and persists\n    longer in PTlower than in PTupper.\n  source: Results, Movement commands, paragraph 2; Fig. 6b, c; Extended Data Fig. 7b; Discussion,\n    paragraph 2\n  quote: Along CDgo, selectivity was larger, emerged faster, and persisted longer in the PTlower than in the\n    PTupper population (Fig. 6b, c).\n  depends_on:\n  - pt-preparatory-activity\n  - pt-cdgo-onset\n  criterion: CDgo (0 to 0.4 s, orthogonalised to CDlate) and selectivity with the shared bootstrap,\n    go-cue aligned. Late preparatory activity is part (b) of pt-preparatory-activity for PTlower. For\n    CDgo, the paper gives no measure; readings fixed here from its words. Larger, (a) the bootstrap\n    median of the mean selectivity over 0 to 0.4 s, (b) the peak of the median selectivity after the\n    go cue; PTlower above PTupper. Emerged faster, from pt-cdgo-onset. Persisted longer, the last time\n    after the go cue of the first run of bins with the 5th percentile above zero is later for PTlower.\n    Reproduced when PTlower CDlate selectivity holds and larger, faster and longer all hold; partially\n    reproduced when some do.\n- id: pt-cdgo-onset\n  statement: Along CDgo, significant selectivity emerges 24 ms after the go cue in PTlower neurons,\n    faster than in PTupper neurons (48 ms), before the first detectable movement.\n  source: Results, Movement commands, paragraph 2; Fig. 6c legend\n  quote: In the PTlower population, significant selectivity emerged 24 ms after the go cue, faster than in\n    the PTupper population (48 ms) (Fig. 6c).\n  depends_on:\n  - pt-tagged-units\n  expected:\n  - quantity: PTlower CDgo selectivity onset after the go cue\n    value: 24\n    tolerance: 5\n    unit: ms\n  - quantity: PTupper CDgo selectivity onset after the go cue\n    value: 48\n    tolerance: 5\n    unit: ms\n  criterion: Onset is the first time after the go cue at which the 5th percentile of the bootstrap\n    selectivity along CDgo is above zero (Fig. 6c legend, significance as in the Methods). The\n    tolerance is one 5 ms bin, the resolution of the rates (10% of the values is below a bin). Open,\n    with readings - the bin time stamp, (a) bin centre, (b) bin end, (c) bin start; whether onset must\n    be sustained, (i) the first significant bin, (ii) the first of three consecutive significant bins.\n    Reproduced when, under one reading, both onsets are within tolerance and PTlower is earlier;\n    partially reproduced when PTlower is earlier but an onset is out of tolerance.\n- id: reaction-time\n  statement: The first detectable movement occurs about 50 ms after the go cue (99% confidence interval 38\n    to 56 ms).\n  source: Results, Movement commands, paragraph 2; Fig. 6c legend; Methods, Videography\n  quote: The onset of the first detectable movement occurred approximately 50 ms after the go cue onset (99%\n    confidence interval 38–56 ms).\n  statistics:\n  - test: bootstrap of session means across mice and sessions\n    ci:\n      level: 0.99\n      low: 38\n      high: 56\n      unit: ms\n    n: 3 mice, 14 sessions\n  expected:\n  - quantity: reaction time\n    value: 50\n    tolerance: 5\n    unit: ms\n  criterion: Methods, Videography - reaction time from the luminance change in a region of interest just\n    below the jaw in 400 Hz side-view video, averaged over all trials of a session; confidence interval\n    by bootstrapping session means across mice (3) and sessions (14). The Methods say 95% and the\n    Results 99%; both are computed. The region is placed by hand and the onset rule for the luminance\n    trace is not given, so the test needs the video. Reproduced when the bootstrap mean is within\n    tolerance (10% of 50 ms) and the interval overlaps 38 to 56 ms. Not testable if the dandiset holds\n    no video.\n- id: pt-cd-change-at-go-cue\n  statement: The coding direction changes rapidly at the go cue in the PTlower population, and more slowly,\n    over several hundred milliseconds, in the PTupper population.\n  source: Results, Movement commands, paragraph 2; Extended Data Fig. 7c, e\n  quote: The coding direction changed rapidly at the go cue in the PTlower population, and more slowly, over\n    several hundred milliseconds, in the PTupper population (Extended Data Fig. 7c, e).\n  depends_on:\n  - pt-tagged-units\n  criterion: Extended Data Fig. 7e legend - the correlation (inner product of unit-normalised CDs, Methods)\n    between the CD at each time bin and CDlate, normalised to its mean in the 400 ms before the go cue;\n    1,000 bootstrap iterations. The code (CDCorrelation.m) averages the inner product over the CDs of\n    every bin of the delay epoch (-1.3 to 0 s) and normalises to the delay epoch mean, with 100\n    iterations; this is a variant. The paper does not say how the speed of change is measured. The\n    reading fixed here is the time after the go cue at which the bootstrap median of the normalised\n    correlation first falls below a level, with levels (a) 0.5 and (b) 0.75. Reproduced when PTlower's\n    time is shorter than PTupper's and PTupper's is at least 0.2 s (\"several hundred milliseconds\");\n    partially reproduced when PTlower's is shorter only.\n- id: pt-lower-movement-termination\n  statement: In PTlower neurons, selectivity along both CDlate and CDgo ceases with the offset of movement\n    (the last lick), together with an abrupt change in the coding direction; this transition is not seen\n    in the PTupper population.\n  source: Results, Movement commands, paragraph 3; Extended Data Fig. 10a-c\n  quote: Selectivity along both CDlate and CDgo ceased with the offset of movement (Extended Data Fig. 10a, b),\n    simultaneous with an abrupt change in the coding direction (Extended Data Fig. 10c). This transition was\n    not observed in the dynamics of the PTupper population.\n  depends_on:\n  - pt-lower-late-and-motor\n  criterion: Rates aligned to the last lick-port contact after the go cue (either side) on correct trials,\n    within each unit's trial range (loadAndProcessData.m, getLickInfo and ObjToLickPSTH), projected on\n    the go-cue CDlate and CDgo of the population, without baseline subtraction (Projections.m), with the\n    shared bootstrap. The paper gives no window. Readings fixed here - (a) the 5th percentile is above\n    zero for most bins of the 200 ms before the last lick and for none of the bins from 0.2 to 0.4 s\n    after it; (b) the same with 400 ms windows before and from 0.1 to 0.5 s after. Reproduced when this\n    holds for PTlower along both CDs; partially reproduced for one CD. The PTupper result along both\n    CDs and the CD correlation matrix after the go cue (Extended Data Fig. 10c, from CDCorrelation.m with\n    lick-aligned rates) are reported, as the paper gives no measure for the abrupt change.\n- id: pt-cohort-control\n  statement: Differences in coding between PTupper and PTlower neurons are not explained by the animal\n    cohorts; unidentified neurons recorded in the two cohorts give similar coding direction projections,\n    nearly indistinguishable once depth-matched.\n  source: Results, Preparatory activity, paragraph 2; Extended Data Fig. 8 legend; Methods,\n    Electrophysiology\n  quote: Differences in coding between PTupper and PTlower neurons could not be explained by variation across\n    animal cohorts (Extended Data Fig. 8).\n  depends_on:\n  - pt-upper-early-preparatory\n  - pt-cdgo-onset\n  expected:\n  - quantity: unidentified units, PTupper cohort\n    value: 495\n    tolerance: 49.5\n  - quantity: unidentified units, PTlower cohort\n    value: 511\n    tolerance: 51.1\n  - quantity: depth-matched unidentified units, PTlower cohort\n    value: 276\n    tolerance: 27.6\n  criterion: Unidentified single units of each cohort, with the inclusion rule of the opening comment\n    (the code applies it to untagged units, groups 3 and 4; whether the reported counts are before or\n    after it is open, and both are given); depth matching by keeping the PTlower cohort's left ALM\n    recordings only (Methods). Selectivity along CDearly and CDgo computed for each unidentified\n    population as for the PT populations. The paper gives no test for \"similar\". Reproduced when, for\n    the depth-matched populations, the difference that separates the PT types is absent - the\n    PTlower-cohort population's mean CDearly selectivity over -2.5 to -2.1 s lies inside the\n    PTupper-cohort population's 5-95% bootstrap interval, and the two CDgo onsets (pt-cdgo-onset rule)\n    differ by no more than the difference between the PT types; partially reproduced when one holds.\n    The z-scored variant of the legend's bottom row is shown.\n- id: pt-types-differ-in-timing\n  statement: The two PT types have different roles in time; PTupper populations carry early preparatory\n    activity that persists until movement, while PTlower populations mainly carry late preparatory\n    activity and movement commands.\n  source: Abstract; Discussion, paragraphs 1 and 2\n  quote: Preparatory activity appeared early and remained persistent in PTupper neurons, whereas movement\n    commands were observed in PTlower neurons.\n  depends_on:\n  - pt-upper-early-preparatory\n  - pt-upper-persistent\n  - pt-lower-cdearly-decay\n  - pt-single-neuron-early-selectivity\n  - pt-lower-late-and-motor\n  - pt-cdgo-onset\n  criterion: The summary of the claims it depends on, with no measure of its own. Reproduced when all six\n    are reproduced; partially reproduced when at least one claim on each side (PTupper early and\n    persistent; PTlower late and motor) is reproduced; not reproduced otherwise.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000006/10.1038-s41586-018-0642-9.yaml paper/10.1038-s41586-018-0642-9.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python - <<'EOF'
import re
p='claims/000006/10.1038-s41586-018-0642-9.yaml'
s=open(p).read()
rep={
"""  quote: All (62 out of 62) medulla- projecting PT neurons mapped to the Slco2a1 taxonomic cluster.
    Similarly, thalamus-projecting PT neurons mapped to the Npsr1 and Hpgd clusters (91 out of 94""":
"""  quote: projecting PT neurons mapped to the Slco2a1 taxonomic cluster. ... Similarly, thalamus-projecting
    PT neurons mapped to the Npsr1 and Hpgd clusters (91 out of 94""",
"""  quote: Slco2a1, PTupper interquartile range (IQR) = 1–2.5 puncta, n = 60; Slco2a1, PTlower IQR = 6–22,
    n = 95; Npnt, PTupper IQR = 16–40, n = 145; Npnt, PTlower IQR = 1–9, n = 69""":
"""  quote: "Slco2a1, PTupper: interquartile range (IQR) = 1–2.5 puncta, n = 60; Slco2a1, PTlower: IQR = 6–22,
    n = 95; Npnt, PTupper: IQR = 16–40, n = 145; Npnt, PTlower: IQR = 1–9, n = 69\"""",
"""  quote: Baseline and trial-averaged peak spike rates were not significantly different (P > 0.1, two-sided
    t-test) in PTupper cells (baseline 4.3 ± 3.5 Hz; peak 17.7 ± 13.8 Hz; median ± s.d.) compared to PTlower
    cells (baseline 5.2 ± 4.8 Hz; peak 17.2 ± 22 Hz)""":
"""  quote: "Baseline and trial-averaged peak spike rates were not significantly different (P > 0.1, two-sided
    t-test) in PTupper cells (baseline: 4.3 ± 3.5 Hz; peak: 17.7 ± 13.8 Hz; median ± s.d.) compared to PTlower
    cells (baseline: 5.2 ± 4.8 Hz; peak: 17.2 ± 22 Hz)\"""",
"""    (PTupper 64.4 ± 1.0%; PTlower 58.9 ± 0.6%, mean ± s.e.m.; P = 1 × 10−4, two-sided Mann–Whitney test).""":
"""    (PTupper: 64.4 ± 1.0%; PTlower: 58.9 ± 0.6%, mean ± s.e.m.; P = 1 × 10−4, two-sided Mann–Whitney test).""",
"""    21 of the most predictive neurons (PTupper 62.7 ± 1.1%; PTlower 56.7 ± 0.4%, mean ± s.e.m.; P = 9 × 10−7,""":
"""    21 of the most predictive neurons (PTupper: 62.7 ± 1.1%; PTlower: 56.7 ± 0.4%, mean ± s.e.m.; P = 9 × 10−7,""",
"""    confidence interval 38–56 ms).""":"""    confidence interval: 38–56 ms)."""}
for a,b in rep.items():
    assert a in s,a[:40]; s=s.replace(a,b)
# make the two decoding quotes and reaction-time quote double-quoted
for start in ["  quote: 24.6% (15 out of 61)","  quote: Disregarding spike rate changes","  quote: The onset of the first detectable movement"]:
    i=s.index(start); j=s.index("\n  ",i+3)
    # find end of quote block: next line starting with two spaces and a key
    m=re.search(r"\n  [a-z_]+:",s[i+3:]); j=i+3+m.start()
    body=s[i+len("  quote: "):j]
    s=s[:i]+'  quote: "'+body+'"'+s[j:]
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/000006/10.1038-s41586-018-0642-9.yaml paper/10.1038-s41586-018-0642-9.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/000006/10.1038-s41586-018-0642-9.yaml; grep -n -i "rather\|—" $f; python3 - <<'EOF'
import yaml
d=yaml.safe_load(open('claims/000006/10.1038-s41586-018-0642-9.yaml'))
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c),sum(x.get('data')=='elsewhere' for x in c))
EOF
git status --short
```

```
31 8 23 17 9
 M claims/000006/10.1038-s41586-018-0642-9.yaml
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

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000006/10.1038-s41586-018-0642-9.yaml",
 "old_string": "  statement: In ALM scRNA-seq, PT neurons map to three glutamatergic transcriptomic clusters (Slco2a1,",
 "new_string": "  statement: In ALM scRNA-seq, glutamatergic neurons form 27 clusters and PT neurons map to three of them (Slco2a1,"
}
```

```
The file claims/000006/10.1038-s41586-018-0642-9.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000006/10.1038-s41586-018-0642-9.yaml paper/10.1038-s41586-018-0642-9.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I rewrote `claims/000006/10.1038-s41586-018-0642-9.yaml` from the full text, and the quote checker passes with no problems.

**Text read:** the version of record (Nature 563, 79–84, 2018), from the PDF someone supplied and its `.txt` extraction. That covers the main text, Methods, the Extended Data Fig. 1–10 legends and the Reporting Summary. The supplement (Supplementary Tables 1–4) is not in the text.

**Code read:** the paper only links a GitHub organisation (`github.com/SvobodaJanelia`), not a repository. I read the MATLAB `.m` files in `Code/` of `Ephys.zip` from Figshare doi:10.25378/janelia.7007846, version 1 (file 13292708). I did not open the data files in that zip.

**Claims:** 31 claims, all with quotes; none needed an `inferred` note.
- 8 claims carry statistics (10 values), 17 have expected values with tolerances, and 23 have criteria.
- 9 claims rest on anatomy and sequencing data held elsewhere (Figshare, GEO GSE119182, Tasic et al. 2018). The dandiset cannot test them.
- Kept ids: the 9 from the old file. All their criteria are new; the old label-shuffle null, McNemar and Fisher tests are gone.
  - `pt-lower-late-and-motor` now tests selectivity along the late-delay and go-cue coding directions (CDlate, CDgo) with the paper's hierarchical bootstrap.
  - `pt-types-differ-in-timing` is now a summary that depends on six claims.
- New claims: 22, among them unit counts, depth, spike rates and their spread, bursting, selectivity in any epoch, variance explained, CDearly decay in PTlower, coding-direction stability, single-neuron early selectivity, decoding (plain and rectified), CDgo onset, reaction time, the change in coding direction at the go cue, movement termination, and the cohort control.

**Details the paper leaves open, and the readings named for each:**
- **Trial range per unit, go-cue-aligned rates:** (a) the code's ±10-trial range, which it applies only to last-lick-aligned rates; (b) all trials.
- **Unit inclusion:** (a) the code's per-unit rule (>50 trials, >3.2 spikes per trial, >65% correct, unit quality); (b) the Methods' per-session rule (≥50 trials). The code and Methods differ here.
- **Bootstrap:**
  - what a "mouse" is: 4 mice, or the code's 6 animal ids (two right-hemisphere recording sets are numbered as separate animals);
  - whether resampled trials enter the projected rates: no, as in the code, or yes.
  - The code's 100 iterations with a ±1.545 s.d. band is kept only as a variant.
- **Early selectivity 0.41 vs 0.25:** the measure is either the coding-direction-style d′ or the code's ROC d′; the test is not named, so both Student's t and Mann–Whitney are run.
- **Rate heterogeneity "χ2 test":** Bartlett's test is the main reading; the code's two-sample F test is a variant.
- **"Task epoch" in the 122/130 count:** the code's 400 ms sample window, or the full 1 s sample epoch.
- **"Larger" along CDearly:** averaged over the CDearly window or the whole sample epoch. "More consistent across trials" is read as bootstrap s.d. over median.
- **"Remained constant":** significant at every bin, or a significant mean over the last 400 ms of the delay.
- **The CDearly decay p-value (P = 0.34):** computed as the bootstrap fraction at or below zero.
- **CD stability:** Pearson r of the coding-direction weights (from the Extended Data 7d legend) and the code's inner product.
- **CDgo onset:** bin time stamp (start, centre or end), and whether one bin or three consecutive bins count.
- **"Larger / persisted longer" along CDgo:** the window mean or the peak, and the end of the first significant run.
- **Rapid vs slow change at the go cue:**
  - the time at which normalised similarity falls to 0.5 or 0.75;
  - the code normalises to the whole delay epoch, against the legend's last 400 ms; the code's version is a variant.
- **Movement-termination windows:** 200 ms or 400 ms either side of the last lick.
- **"Nearly as diverse" (variance explained):** a ratio of at most 1.3, taken from the code's plot axis. Separately, the code smooths with 100 ms and normalises differently from the Methods.
- **Cohort control:** what counts as "similar", and whether the 495/511/276 unit counts are before or after exclusion.

**Missing from the paper:**
- The reaction-time onset rule is not given, and its confidence level is stated as 95% in the Methods but 99% in the Results.
- Supplementary Table 1 is not in the text; `pt-types-account-for-all-pt` cites it, but its numbers are quoted from the main text.
- No method detail a claim on this dandiset needed is missing beyond the open details listed above.

## End of run

22 turns, 7 minutes, result: success.
