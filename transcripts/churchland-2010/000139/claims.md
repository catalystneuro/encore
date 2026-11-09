# 000139 · claims · run 40754094428

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453 claims/000139 paper/; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls claims/001453 claims/000139 paper/ tools; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 182
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-12`. Record this version in the attempt's provenance.
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
[... 162 more lines not kept]
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

**Agent calls Bash**

```bash
ls claims | head -50; ls -t claims/*/*.yaml | head -5; head -60 tools/claims_check.py; head -30 paper/10.1016-j.neuron.2010.09.015.txt; head -15 paper/10.1038-nature11129.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -30 paper/10.1016-j.neuron.2010.09.015.txt; echo ----; head -15 paper/10.1038-nature11129.txt; echo ---; head -40 claims/000129/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -rn "000139" --include=*.yaml --include=*.json --include=*.csv --include=*.md . 2>/dev/null | grep -v "^./transcripts" | head -20
```

```
./papers/manifest.yaml:389:  000139:
./targets/dandisets.json:1235:   "dandiset": "000139",
```

**Agent calls Bash**

```bash
sed -n 380,410p papers/manifest.yaml; sed -n 1225,1275p targets/dandisets.json
```

```
source: ncbi_pmc+crossref (paper-text-fetcher)
    pdf: false
    supplements: 1
  - doi: 10.1038/nature11129
    status: stored
    version: as served by europe_pmc
    source: europe_pmc+crossref (paper-text-fetcher)
    pdf: false
    supplements: 0
  000139:
  - doi: 10.1016/j.neuron.2010.09.015
    status: stored
    version: as served by ncbi_pmc
    source: ncbi_pmc+crossref (paper-text-fetcher)
    pdf: false
    supplements: 1
  - doi: 10.1038/nature11129
    status: stored
    version: as served by europe_pmc
    source: europe_pmc+crossref (paper-text-fetcher)
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/000128 claims/000138 claims/000140 claims/000129 2>&1; grep -l "neuron.2010" -r claims | head
```

```
ls: cannot access 'claims/000138': No such file or directory
ls: cannot access 'claims/000140': No such file or directory
claims/000128:
10.1016-j.neuron.2010.09.015.yaml

claims/000129:
10.1088-1741-2552-aa9e95.yaml
claims/000128/10.1016-j.neuron.2010.09.015.yaml
```

**Agent calls Bash**

```bash
head -40 claims/000129/*.yaml; cat schemas/claims.schema.json | head -150
```

```
# Claims for Makin, O'Doherty, Cardoso & Sabes (2018), J. Neural Eng. 15 026010, on dandiset 000129.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol as stated in docs/protocol.md.
#
# Text read: the version of record (PDF supplied by a person, extracted to
# paper/10.1088-1741-2552-aa9e95.txt), main text with its Methods, Results, Discussion and figure
# legends. The paper has no supplement. Two equations are garbled in the extracted text (the
# ridge penalty of equation 10 and the Wiener filter order sweep); the PDF could not be rendered
# here, and the code settles both (below).
#
# Data the paper used (Methods, Animal experiments, Data acquisition, Tasks). Three monkeys, 49
# sessions of continuous reaching in the horizontal plane. Monkey I (Sabes lab, 37 sessions,
# right hemisphere, left arm) and monkey L (Sabes lab, 10 sessions, left hemisphere, right arm):
# point-to-point reaching to targets on an 8 by 8 or 8 by 17 grid (I) or a 6 by 6 grid (L),
# 15 mm spacing, 450 ms hold, no inter-trial interval. 96-channel Utah arrays in M1 and S1;
# S1 was recorded in 7 of monkey I's 37 sessions and in all 10 of monkey L's. Spikes sorted
# online, with an unsorted hash unit kept per channel; units below 0.5 Hz discarded, leaving
# 171 to 413 units per session for monkey I and 416 to 523 for L. Fingertip position from a
# Polhemus sensor at 250 Hz. Monkey C (Koerding lab, 2 sessions, 75 and 91 units, center-out
# task) came from a public dataset (Dyer et al., biorxiv 080861). The Sabes lab data are
[... 170 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p schemas/claims.schema.json
```

```
"type": "string",
            "minLength": 1
          }
        },
        "allOf": [
          {
            "not": {
              "required": [
                "quote",
                "inferred"
              ]
            }
          },
          {
            "if": {
              "properties": {
                "kind": {
                  "const": "link"
                }
              },
[... 177 more lines not kept]
```

**Agent**

Schema understood. Now reading the paper text.

**Agent calls Bash**

```bash
cd paper; fold -s -w 200 10.1016-j.neuron.2010.09.015.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt
```

```
1062 /tmp/claude-1001/p.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 350
}
```

```
1	DOI: 10.1016/j.neuron.2010.09.015
2	Version: as served by ncbi_pmc
3	Source: ncbi_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 1 supplement file(s) from PubMed Central, downloaded in a browser (PMC2991102), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC2991102 PMC2991102.1 2991102 2991102 NIHMS240235 21040842 
8	10.1016/j.neuron.2010.09.015 NIHMS240235 NIHPA240235 1 Article Cortical preparatory activity: representation of movement or first cog in a dynamical machine? Churchland MM 1 Cunningham JP 1 3 Kaufman 
9	MT 2 Ryu SI 1 4 Shenoy KV 1 2 5 1 Dept. of Electrical Engineering, Stanford University, Stanford CA, 94305, USA 2 Neurosciences Program, Stanford University, Stanford CA, 94305, USA 3 Dept. of 
10	Engineering, University of Cambridge, Cambridge, UK 4 Dept. of Neurosurgery, Palo Alto Medical Foundation, Palo Alto CA, 94301, USA 5 Dept. of Bioengineering, Stanford University, Stanford CA, 94705, 
11	USA 4 11 2010 68 3 191982 387 400 06 10 2010 04 11 2011 04 11 2011 06 10 2011 14 10 2026 This file is available for text mining. It may also be used consistent with the principles of fair use under 
12	the copyright law. Summary The motor cortices are active during both movement and movement preparation. A common assumption is that preparatory activity constitutes a sub-threshold form of movement 
13	activity: a neuron active during rightwards movements becomes modestly active during preparation of a rightwards movement. We asked whether this pattern of activity is in fact observed. We found that 
14	it was not: at the level of a single neuron, preparatory tuning was weakly correlated with movement-period tuning. Yet somewhat paradoxically, preparatory tuning could be captured by a preferred 

[... 336 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "supplement\|Supp" $TMPDIR/p.txt | sed -n 1,200p | cut -c1-200 | tail -30; grep -n "SUPPLEMENT\|Supplementary Figure 1\|====" $TMPDIR/p.txt | head
```

```
313:We thank M. Risch for surgical and veterinary assistance and S. Eisensee for administrative support. Bastian A Riehle A Erlhagen W Schoner G 1998 Prior information preshapes the population 
481:##### Supplement: NIHMS240235-supplement-01.pdf
484:Inventory of Supplemental Information 
486:Supplemental Figure 1. Population PSTHs.  
491:Supplemental Figure 2. Illustration of how PCA is used to assign each condition a 
497:Supplemental Figure 3. Array locations in monkey J.  
502:Supplemental Figure 4. Illustration of how PSTHs were smoothed. 
508:Supplemental Figure 5. Illustration of why, for a linear dynamical system, preparatory 
512:in the supplemental text (see below). 
515:Supplemental Text: Explanation of how a PD in peri-movement space can capture 
521:Supplemental Experimental Procedures 
558:Supplemental  figure  1
561:Supplemental Figure 1. Population PSTHs. Each panel plots the average firing rate 
602:Supplemental  Figure  2
632:Supplemental Figure 2. Illustration of how PCA is used to construct the peri-movement 
658:Supplemental  Figure  3
661:Supplemental Figure 3. Array locations in monkey J: the first in caudal PMd (left) the 
670:Supplemental  Figure  4
735:Supplemental Figure 4. Illustration of how PSTHs were smoothed for improved 
877:Supplemental  Figure  5
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 478,
 "limit": 600
}
```

```
478	
479	[54] Gaussian-process factor analysis for low-dimensional single-trial analysis of neural population activity. J. Neurophysiol.. 2009. 10.1152/jn.90941.2008
480	
481	##### Supplement: NIHMS240235-supplement-01.pdf
482	
483	=== page 1 ===
484	Inventory of Supplemental Information 
485	 
486	Supplemental Figure 1. Population PSTHs.  
487	This figure relates to the interpretation of Figure 4 of the main text, and is briefly 
488	discussed in the main text. 
489	 
490	 
491	Supplemental Figure 2. Illustration of how PCA is used to assign each condition a 
492	location in a space based on the population peri-movement responses.  
493	This figure relates to Figure 5 of the main text, and visually illustrates some 
494	mathematical procedures. 
495	 
496	 
497	Supplemental Figure 3. Array locations in monkey J.  
[... 566 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 351,478p $TMPDIR/p.txt | grep -n -i "figure\|github\|code\|http" | head; grep -o -i "github[^ ]*\|http[^ ]*" ../paper/10.1016-j.neuron.2010.09.015.txt | sort -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s -m 20 https://api.dandiarchive.org/api/dandisets/000139/versions/0.220113.0408/info/ | python3 -c "import json,sys; d=json.load(sys.stdin); m=d.get('metadata',d); print(m.get('name')); print(m.get('description'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd ..; grep -rn -i -B2 -A6 "simulat" claims/*/*.yaml | grep -i "data:\|criterion" | head -10; grep -rn "cannot test\|not hold\|does not hold" claims/*/*.yaml | head -5
```

```
claims/000009/10.1038-nature22324.yaml:649:  criterion: A simulation, not a test on recorded data; its parameters are in the Supplementary
claims/000011/10.1038-nature17643.yaml:907:  criterion: A simulation, not a test on recorded data. Parameters from the Methods and Extended
claims/000011/10.1038-nature17643.yaml:924:  criterion: A simulation, not a test on recorded data. Modular attractor with the Methods'
claims/000013/10.7554-elife.06619.yaml:1146:  criterion: Methods, last paragraph, and Figure 6D. Per L4 C2 cell, spike trains simulated as a
claims/000016/10.1016-j.neuron.2019.09.045.yaml:527:  criterion: A simulation, not a test on recorded data. The linearised rate model of the STAR
claims/000016/10.1016-j.neuron.2019.09.045.yaml:546:  criterion: A simulation, not a test on recorded data. As fig5a-nonselective-model; signal-selective
claims/000016/10.1016-j.neuron.2019.09.045.yaml:559:  criterion: A simulation, not a test on recorded data. As fig5bc-selective-models-match, with
claims/000034/10.7554-elife.61834.yaml-195-  criterion: 'Sorters, agreement graph and k as in the opening comment. Two details are open. The recording:
claims/000034/10.7554-elife.61834.yaml-252-  criterion: Sorters as in the opening comment, with the same parameters as on the real recording, on
claims/000034/10.7554-elife.61834.yaml-283-  criterion: Accuracy per ground-truth unit as in fig2s1a-precision-recall-bias; ground-truth SNR as in
claims/000006/10.1038-s41586-018-0642-9.yaml:504:    partially reproduced when larger holds alone, not reproduced when larger does not hold. Answer of
claims/000008/10.1038-s41586-020-2907-3.yaml:750:    contains 0.05 does not show the grouping at p < 0.05, and (b) does not hold.
claims/000037/10.1038-s41597-023-02214-y.yaml:430:    Values the table does not hold are listed as untestable.
claims/000044/10.1126-science.aad1935.yaml:5:# Europe PMC does not hold it. Every definition the main text does not give (place cells,
claims/000054/10.1038-s4159
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 30,140p tools/claims_check.py
```

```
SAME = {"−": "-", "–": "-", "—": "-", "‐": "-", "‑": "-", "‘": "'", "’": "'", "“": '"', "”": '"',
        " ": " ", " ": " ", " ": " "}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", html.unescape(s))
    for a, b in SAME.items():
        s = s.replace(a, b)
    return re.sub(r"\s+", " ", s).strip().lower()


def flattenings(raw: str) -> list[str]:
    """The text with inline tags removed, with every tag as a space, and both without spaces."""
    tight = norm(re.sub(r"</?[A-Za-z!?][^<>]*>", " ", re.sub(INLINE, "", raw, flags=re.I)))
    loose = norm(re.sub(r"</?[A-Za-z!?][^<>]*>", " ", raw))
    return [tight, loose, tight.replace(" ", ""), loose.replace(" ", "")]


def quote_found(quote: str, texts: list[str]) -> bool:
    fragments = [f for f in (norm(x).strip(" .,;") for x in quote.split("...")) if f]
[... 63 more lines not kept]
```

**Agent**

Full text, Methods and supplement (PMC author manuscript) are present; the paper links no code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/000139/10.1016-j.neuron.2010.09.015.yaml",
 "content": "# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000139.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-10-28,\n# protocol as stated in docs/protocol.md (version pilot-12).\n#\n# Text read: the NIH author manuscript in PubMed Central (PMC2991102), as extracted to\n# paper/10.1016-j.neuron.2010.09.015.txt, with its Results, Methods, figure legends and the one\n# supplement (NIHMS240235-supplement-01.pdf: Supplemental Figures 1 to 5, Supplemental Text and\n# Supplemental Experimental Procedures). Not the version of record. The figures themselves are not\n# in the text; values plotted only in Figures 4, 6 and 7 are not available and no claim rests on\n# them. The paper links no code, so every method below comes from the Methods, the legends or the\n# supplement.\n#\n# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental\n# Procedures). Three adult male rhesus monkeys (A, B, J), delayed reaches from a central touch spot\n# to a target on a fronto-parallel screen. Trial events: target onset (the target jitters), go cue\n# (jitter stops and the touch spot disappears), movement onset. Delays about 0 to 1000 ms; only\n# trials with delays above 400 ms analysed. Four datasets. Monkeys A and B, speed task, 28\n# conditions (7 directions, 2 distances, 2 instructed speeds), single electrodes, 64 and 74\n# single units. Monkey J, maze task, single electrodes, 172 single units, recorded on four sets of\n# 27 conditions each (about 53 neurons per set; population analyses done per set, then averaged).\n# Monkey J-array, maze task, all 108 conditions interleaved, two 96-electrode arrays (caudal PMd,\n# and surface M1 perhaps extending into caudal PMd), 146 single- and multi-unit isolations, mean\n# 2166 trials per neuron (2155 in the Methods). Maze conditions are one third straight reaches\n# without barriers, one third curved around virtual barriers, one third the same mazes with\n# distractor targets. Measured variables: spike times; hand position (optical tracking) from\n# which velocity and acceleration follow; eye position; EMG from 6, 11 and 8 muscle heads in\n# monkeys A, B and J (not recorded for the J-array dataset).\n#\n# The dandiset (title \"MC_Maze_Medium, macaque primary motor and dorsal premotor cortex spiking\n# activity during delayed reaching\") is described on the archive as sorted units from arrays in\n# M1 and PMd of one macaque doing the maze task, with cursor, hand and eye position and hand\n# velocity, limited to 250 training and 100 test trials, released for the Neural Latents\n# Benchmark. That matches the kind of data of the J-array dataset, with far fewer trials than the\n# paper's (a mean of 2166 per neuron). Whether it is the same recording, and how many conditions\n# it holds, is the author's to find. The speed-task datasets (A, B), the single-electrode monkey J\n# dataset and all EMG are not described there; the claims that rest on them are listed to cover\n# the paper's findings.\n#\n# Method common to the claims below, with its source.\n# - Trials: delays above 400 ms (Methods, Task design). For the maze task only trials whose\n#   horizontal and vertical velocity profiles correlate with a reference proto-trial at r > 0.9\n#   (Supplemental Experimental Procedures, Task design). Open: what the proto-trial is (readings\n#   (a) the condition's mean velocity profile, (b) one representative trial of the condition) and\n#   whether both profiles must pass separately (a) or the two concatenated (b). Open: how\n#   movement onset is detected; the paper does not say. Readings (a) the dataset's own movement\n#   onset times, (b) a threshold on hand speed.\n# - Rates: spikes smoothed with a 20 ms Gaussian (Supplemental Experimental Procedures, Computing\n#   the mean firing rate), read as its standard deviation; means taken per condition, locked to\n#   the go cue or to movement onset. The time step of the rate traces is not given; a standard\n#   choice (1 or 10 ms) cannot change the outcome.\n# - Preparatory rate: the mean from 200 ms before the go cue to 100 ms after; peri-movement rate\n#   (correlations only) the mean from 100 ms before movement onset to 350 ms after (Methods,\n#   Correlations between preparatory and peri-movement tuning). The Methods define no other\n#   preparatory window, so the PD analyses use the same one; this is a reading, as \"Activity\n#   during the preparatory epoch\" is not given its own window.\n# - Neurons: for array data, more than 5 spikes/s of preparatory tuning (Methods, Neural\n#   recordings and datasets); for correlations also peri-movement tuning at least 1.5 times as\n#   strong as preparatory tuning (Methods, Correlations). Open: how tuning strength is measured.\n#   Readings (a) the range across conditions (largest minus smallest condition mean), (b) the\n#   standard deviation across conditions. PD analyses use all neurons that pass the preparatory\n#   threshold, regardless of peri-movement activity (Methods, Correlations, last sentence).\n# - PD model: x_n = b_o + S b by least squares, PD = b / |b| (Methods, Using a PD). Performance:\n#   leave-one-condition-out cross validation, one minus the mean squared error of the left-out\n#   predictions divided by the variance of x_n across conditions, averaged over neurons (Methods,\n#   PD performance). S is fixed for all folds (Methods, \"The matrix S is the same for every\n#   neuron\"); only the regression leaves the condition out. Whether the variance uses c or c - 1\n#   is a standard choice that cannot change any comparison between spaces.\n# - Peri-movement space: a c by n*t matrix T of condition-mean rates from 150 ms before movement\n#   onset to 800 ms after (maze), every neuron except the one being fitted, not normalized; PCA\n#   over conditions, the first k scores are S (Methods, PCA-based spaces). k from 1 to 14 (Results,\n#   \"k in the range of 3-14\"; Figure 6E goes to 12).\n# - Kinematic space: horizontal and vertical hand position, velocity and acceleration from 150 ms\n#   before movement onset, each normalized to unit range across times and conditions, PCA as\n#   above (Methods, PCA-based spaces). Open: where the window ends (\"until after the reach\");\n#   readings (a) 800 ms after onset, as for the neural matrix, (b) the end of the slowest\n#   condition's reach. Open: \"Each neuron contributed one kinematic variable\"; readings (a) the six\n#   signals repeated in turn until there are as many blocks as neurons, (b) the six signals once.\n#   They give the same space when the repeats are even.\n# - Task spaces for the maze task (Methods, Task spaces): endpoints + maximum speed (3-D),\n#   initial velocity (mean velocity over the first 150 ms of the reach, 2-D), endpoints +\n#   orthogonal excursion (3-D, counterclockwise positive), endpoints + viapoint (4-D), endpoints +\n#   maximum velocity (4-D), endpoints + halfpoint (4-D), segment directions (6-D, displacements of\n#   three segments), kitchen sink (11-D, adds barriers present and distractors present). Open:\n#   whether the three segments are equal in time or in path length; readings both.\n# - The EMG space cannot be built from this dataset; the paper did not record EMG for J-array.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000139\"\npaper: doi:10.1016/j.neuron.2010.09.015\nclaims:\n- id: j-array-recordings\n  statement: The J-array dataset holds 146 single- and multi-unit isolations recorded with two\n    96-electrode arrays during the maze task, over 108 conditions, with a mean of 2166 trials per\n    neuron.\n  source: Results, Behavior and recordings, paragraph 1; Methods, Neural recordings and datasets\n  quote: a pair of implanted 96-electrode arrays (J-array dataset, 146 single- and multi-unit\n    isolations)\n  expected:\n  - quantity: units in the J-array dataset\n    value: 146\n    tolerance: 14.6\n  - quantity: conditions in the J-array dataset\n    value: 108\n    tolerance: 10.8\n  - quantity: mean trials per neuron, J-array\n    value: 2166\n    tolerance: 216.6\n  criterion: The counts are compared with the dataset's. The archive limits the dataset to 250\n    training and 100 test trials, so the trial count is not expected to match and is reported\n    only. The paper gives 2166 in the Results and 2155 in the Methods; either is the paper's.\n    Reproduced when the unit count is within tolerance and the conditions are the 108 of the\n    paper; partially reproduced when the units match and the dataset holds a subset of the 108\n    conditions (the paper also used 27-condition subsets, Methods, Task design).\n- id: fig4d-mean-correlation-j-array\n  statement: For the J-array dataset, preparatory and peri-movement tuning are positively but only\n    weakly correlated on average across neurons (mean r = 0.13, p = 0.03; mean Spearman r =\n    0.11).\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 1; Figure\n    4D\n  quote: Across the four datasets the mean correlation was positive (p=0.01, p=0.01, p=0.12, p=0.03)\n    but only very modestly so (mean r = 0.21, 0.19, 0.06 and 0.13). Non-parametric correlations\n    were similarly modest (mean Spearman's r = 0.20, 0.20, 0.06 and 0.11)\n  statistics:\n  - about: mean correlation against zero, J-array\n    test: not named\n    p: 0.03\n  expected:\n  - quantity: mean Pearson r between preparatory and peri-movement rate vectors, J-array\n    value: 0.13\n    tolerance: 0.013\n  - quantity: mean Spearman r, J-array\n    value: 0.11\n    tolerance: 0.011\n  criterion: Per neuron passing both tuning thresholds (opening comment), the vector of\n    condition-mean preparatory rates (200 ms before to 100 ms after the go cue) correlated with\n    the vector of peri-movement rates (100 ms before to 350 ms after movement onset), as in the\n    Methods, Correlations. The test of the mean against zero is not named. Readings (a) a\n    two-sided one-sample t-test of r, (b) a Wilcoxon signed-rank test of r, (c) a t-test of\n    Fisher z-transformed r. Reproduced when, under one reading of the tests and of the tuning\n    measure, both means are within tolerance and the Pearson mean is above zero at p < 0.05.\n    Partially reproduced when the Pearson mean is positive at p < 0.05 and inside the range the\n    paper reports over its four datasets (0.06 to 0.21, widened by 10% of each bound to 0.054 to\n    0.231) but outside tolerance. The number of neurons kept is reported.\n- id: fig4abc-mean-correlation-other-datasets\n  statement: For monkeys A, B and J (single electrodes) the mean correlation between preparatory\n    and peri-movement tuning is 0.21, 0.19 and 0.06 (p = 0.01, 0.01, 0.12), with mean Spearman r\n    of 0.20, 0.20 and 0.06.\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 1; Figure\n    4A to 4C\n  quote: Across the four datasets the mean correlation was positive (p=0.01, p=0.01, p=0.12, p=0.03)\n    but only very modestly so (mean r = 0.21, 0.19, 0.06 and 0.13)\n  statistics:\n  - about: monkey A\n    p: 0.01\n  - about: monkey B\n    p: 0.01\n  - about: monkey J, single electrodes\n    p: 0.12\n  expected:\n  - quantity: mean r, monkey A\n    value: 0.21\n    tolerance: 0.021\n  - quantity: mean r, monkey B\n    value: 0.19\n    tolerance: 0.019\n  - quantity: mean r, monkey J\n    value: 0.06\n    tolerance: 0.006\n  criterion: As fig4d-mean-correlation-j-array, on the speed-task datasets (single-electrode\n    threshold of 10 spikes/s of preparatory tuning) and the single-electrode monkey J dataset\n    (per 27-condition set, then averaged). The archive describes array recordings only, so these\n    data are not expected in the dataset.\n- id: fig4-broad-unimodal\n  statement: Individual neurons span a broad range of preparatory to peri-movement correlations\n    centred near zero, with little sign of separate populations of concordant (r near 1) and\n    opposing (r near -1) tuning.\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 2; Figure\n    4A to 4D\n  quote: different neurons show markedly different relationships between preparatory and\n    peri-movement activity, with a broad range of correlations centered near zero\n  depends_on:\n  - fig4d-mean-correlation-j-array\n  criterion: On the per-neuron correlations of fig4d-mean-correlation-j-array. The paper names no\n    test for the absence of two populations; it judges the histograms by eye. Readings (a)\n    Hartigan's dip test does not reject unimodality at p < 0.05; (b) fewer neurons have |r| >\n    0.8 than have |r| < 0.5. Reproduced when the correlations include both negative and positive\n    values, the mean is inside 0.054 to 0.231 (the paper's range over datasets, widened by 10%),\n    and the distribution is unimodal under a reading. The histogram, its standard deviation and\n    the dip statistic are reported.\n- id: fig4e-correlation-time-course\n  statement: The correlation between preparatory tuning and peri-movement activity at a single\n    time point begins to decline about 200 ms before movement onset and is near zero by movement\n    onset.\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 2; Figure\n    4E\n  quote: The correlation with preparatory activity began to decline ∼200 ms prior to movement\n    onset, and reached values near zero by movement onset\n  depends_on:\n  - fig4d-mean-correlation-j-array\n  criterion: Per neuron, the preparatory rate vector correlated with the vector of\n    condition-mean rates at each single time point of the movement-locked trace (20 ms Gaussian,\n    Figure 4E legend) from 400 ms before to 100 ms after movement onset, averaged over neurons.\n    Open, the neurons; readings (a) those of Figure 4A to 4D (both thresholds), (b) all neurons\n    passing the preparatory threshold. Open, \"near zero\"; readings (a) the mean at onset is not\n    greater than zero at p < 0.05 by the tests named in fig4d-mean-correlation-j-array, (b) its\n    absolute value is below 0.1 (a value the paper does not give). Reproduced when the mean at\n    200 ms before onset is above the mean at onset, the onset value is near zero under a reading,\n    and the decline begins (the last time before onset at which the mean is within 10% of its\n    value at 400 ms before onset) between 300 and 100 ms before onset, a window read from the\n    paper's \"∼200 ms\". The curve is shown.\n- id: suppfig1-population-psth-weak-movement-tuning\n  statement: In population averages sorted by each neuron's preparatory preference, the\n    preparatory differences carry weakly into the peri-movement epoch and show little\n    relationship with preparatory tuning by movement onset.\n  source: Results, Correlations between preparatory and peri-movement tuning, paragraph 2;\n    Supplemental Figure 1\n  quote: By movement onset even population averages show little relationship with preparatory\n    tuning\n  criterion: As the Supplemental Figure 1 legend describes. Neurons passing both thresholds of\n    Figure 4; per neuron the conditions with the strongest and weakest preparatory rate and two\n    intermediate ones; each neuron's rates divided by its maximum rate, then averaged across\n    neurons, locked to movement onset. Open, how strongly the difference must shrink; readings\n    (a) the strongest minus weakest difference at movement onset is smaller than in the\n    preparatory window, (b) it is less than half of it. Reproduced when it holds under a reading;\n    the traces and the ratio are reported.\n- id: fig6d-perimovement-best-j-array\n  statement: For the J-array dataset, the highest cross-validated PD performance over all tested\n    spaces and dimensionalities is reached when the PD is expressed in the peri-movement space.\n  source: Results, PD performance in a variety of spaces, paragraph 2; Figure 6D\n  quote: For every dataset, the highest level of performance was achieved ... when PDs were\n    expressed in the peri-movement space\n  criterion: PD method, peri-movement, kinematic and task spaces as in the opening comment. For\n    each space and each k from 1 to 14, performance averaged over neurons. Reproduced when the\n    largest value of the peri-movement space exceeds the largest value of every kinematic and\n    task space, under every reading of the kinematic window and replication; not reproduced\n    when another space is higher under every reading; otherwise the result rests on the reading.\n    All curves are shown, with the upper limit of fig6-preparatory-dimensionality as a reference.\n- id: fig6-perimovement-best-each-dimensionality\n  statement: Even taken one dimensionality at a time, PD performance is almost always higher in\n    the peri-movement space than in other spaces of the same dimensionality.\n  source: Results, PD performance in a variety of spaces, paragraph 2; Figure 6A to 6D\n  quote: Even if we consider each dimensionality individually, performance was almost always\n    higher for the peri-movement space\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: On the performances of fig6d-perimovement-best-j-array. Comparisons are the\n    kinematic space at each k from 1 to 14 and each task space at its own dimensionality, against\n    the peri-movement space at the same k. \"Almost always\" is read as at least 80% of the\n    comparisons (a reading; the paper gives no count). Reproduced when at least 80% favour the\n    peri-movement space; partially reproduced for 60 to 79%; not reproduced below.\n- id: fig6-dimensionality-peak\n  statement: Performance of the PCA-based spaces typically improves with dimensionality, peaks\n    usually at a middle range, and declines at dimensionalities above 10, a sign of over-fitting.\n  source: Results, PD performance in a variety of spaces, paragraph 1; Figure 6A to 6D\n  quote: Performance typically improved with dimensionality. This increase is nontrivial, as\n    generalization performance is being assessed ... Performance typically declined at\n    dimensionalities >10, an indication of over-fitting\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: On the peri-movement and kinematic curves of fig6d-perimovement-best-j-array.\n    Reproduced when, for the peri-movement space, performance at the best k is above that at k =\n    1, the best k is between 2 and 10, and performance at k = 14 is below that at the best k; the\n    same is reported for the kinematic space.\n- id: fig6-maze-task-spaces\n  statement: For the maze task, the segment directions and initial velocity task spaces perform\n    reasonably well, while the endpoints + maximum speed space does not perform well.\n  source: Results, PD performance in a variety of spaces, paragraphs 1 and 2; Figure 6C and 6D\n  quote: A number of task spaces performed reasonably well, including ... ' segment dirs. ' ... and\n    ' initial vel. ' ... The former is undefined for the maze task, but the latter did not perform\n    well\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: Task-space performances from fig6d-perimovement-best-j-array. \"Reasonably well\" is\n    read from the Figure 6 legend sense, performance above zero (\"Points above zero indicate\n    performance considerably better than chance\"). Open, the reference for \"did not perform\n    well\"; readings (a) endpoints + maximum speed below the 3-D peri-movement space, (b) below\n    both segment directions and initial velocity. Reproduced when segment directions and initial\n    velocity are above zero and endpoints + maximum speed falls short under a reading.\n- id: fig6abc-perimovement-best-other-datasets\n  statement: For monkeys A, B and J (single electrodes) too, the best PD performance is in the\n    peri-movement space, though among 3-D spaces the targets + instructed speed and endpoints +\n    maximum speed spaces perform very well for the speed-task datasets.\n  source: Results, PD performance in a variety of spaces, paragraph 2; Figure 6A to 6C\n  quote: An exception was that, among 3-dimensional spaces, the 'targs+instr. spd.' and 'endpoints\n    + max. spd.' performed very well for the datasets collected using the speed task\n  criterion: As fig6d-perimovement-best-j-array, with the EMG space added and the speed-task\n    spaces (targets + instructed speed, 1 slow and 2 fast) where defined. These datasets are not\n    described on the archive.\n- id: fig6e-summary-rank\n  statement: Across monkeys A, B and J, performance averaged over neurons is highest for the\n    peri-movement space, with the gap growing at higher dimensionalities; task spaces are\n    outcompeted by the kinematic and EMG spaces, which are outperformed by the peri-movement space.\n  source: Results, PD performance in a variety of spaces, paragraph 3; Figure 6E\n  quote: Performance (averaged across neurons) was highest when the PD employed the space based on\n    peri-movement neural activity. This performance differential increased at higher\n    dimensionalities\n  statistics:\n  - about: spaces against the best space, per dimensionality limit\n    test: not named\n    p: 0.001\n    p_relation: \"<\"\n  criterion: The summary pools monkeys A, B and J and excludes J-array (Figure 6E legend), with\n    limits of 3, 6 and 12 dimensions and, for PCA spaces, the best dimensionality under the limit.\n    It needs the speed-task, single-electrode and EMG data, which the archive does not describe.\n- id: fig6-preparatory-dimensionality\n  statement: Preparatory activity needs 7 to 10 dimensions, depending on the dataset, to capture\n    90% of its variance.\n  source: Supplemental Experimental Procedures, Estimating the upper limit of PD performance;\n    Results, PD performance in a variety of spaces, paragraph 1\n  quote: depending on the dataset, 7-10 dimensions were required to capture 90% of the data variance\n  expected:\n    quantity: principal components for 90% of variance of the c by n preparatory matrix\n    value: 8.5\n    tolerance: 2.2\n  criterion: PCA of the c by n matrix of condition-mean preparatory rates of all neurons kept for\n    the PD analyses. The reported range 7 to 10 widened by 10% of each bound is 6.3 to 11, which\n    the value and tolerance encode. Reproduced when the count lies in it. The paper had 108\n    conditions for J-array; with fewer conditions the count is bounded by c - 1, which is\n    reported.\n- id: fig7a-shuffled-space-poor\n  statement: A peri-movement space built after randomly inverting each condition's peri-movement\n    response on half the conditions performs poorly.\n  source: Results, Controls, paragraph 1; Figure 7A\n  quote: The PCA-based 'shuffled-space' performed poorly\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: As the Figure 7A legend gives it. For each neuron and condition, with probability 0.5,\n    activity after 150 ms before movement onset is reflected vertically about the rate at that\n    time; then the peri-movement space and PD performance as in the opening comment, k from 1 to\n    14. The random draw is a standard choice; 20 draws are averaged. The paper averages over\n    datasets; here one dataset. Open, the reference for \"poorly\"; readings (a) the best shuffled\n    performance is below the best unshuffled peri-movement performance, (b) it is also below the\n    best kinematic and task spaces. Reproduced when (a) holds; the result under (b) is reported.\n- id: fig7b-window-start-slide\n  statement: Sliding the start of the peri-movement window from 150 ms before movement onset to\n    movement onset barely lowers PD performance, to 97% (monkey J) and 94% (monkeys A, B) of its\n    original value.\n  source: Results, Controls, paragraph 1; Figure 7B\n  quote: Even when the window began at movement onset ... performance was still at 97% (monkey J),\n    and 94% (monkeys A, B) of its original value\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  expected:\n    quantity: performance with the window starting at movement onset, as a fraction of that with\n      the window starting 150 ms before, monkey J\n    value: 0.97\n    tolerance: 0.097\n  criterion: Performance at the best k for each start time (Figure 7B legend), start times from\n    150 ms before onset to onset. Open, whether \"monkey J\" includes the J-array dataset; readings\n    (a) it does, so 0.97 applies, (b) it is the single-electrode dataset only, and no value is\n    given for J-array, which is then judged by \"little decline\" read as the 94 to 97% the paper\n    gives (0.846 to 1.067 with 10% of each bound). Open, the window end; readings (a) fixed at\n    800 ms after onset, (b) the window shifted whole. Reproduced when the fraction is within\n    tolerance under a reading.\n- id: ap-location-no-effect-j-array\n  statement: For the J-array dataset the correlation between preparatory and peri-movement tuning\n    does not depend on anterior-posterior location (r = 0.20, p = 0.27).\n  source: Results, Comparison of anterior versus posterior sites, paragraph 1\n  quote: Regressing tuning correlation (as in Figure 4 ) against AP location yielded little or no\n    effect\n  statistics:\n  - about: tuning correlation against AP location, J-array\n    test: regression\n    statistic: r = 0.20\n    p: 0.27\n  depends_on:\n  - fig4d-mean-correlation-j-array\n  criterion: A claim of absence, judged on the paper's test, a linear regression of each neuron's\n    tuning correlation (fig4d-mean-correlation-j-array) on its AP location, at p < 0.05.\n    Reproduced when p >= 0.05; not reproduced when p < 0.05; r is reported either way. Open, the\n    AP location of an array unit; readings (a) its electrode's position along the\n    anterior-posterior axis with both arrays in one frame, (b) the array (PMd anterior, M1\n    posterior). Whether the dataset gives electrode positions is the author's to find.\n- id: ap-location-no-effect-other-datasets\n  statement: For monkeys A, B and J (single electrodes) the tuning correlation does not depend on\n    AP location (r = -0.05, p = 0.82; r = -0.03, p = 0.85; r = -0.07, p = 0.52).\n  source: Results, Comparison of anterior versus posterior sites, paragraph 1\n  quote: r =-0.05, p =0.82; r =-0.03, p =0.85; r =-0.07, p =0.52; and r =0.20, p =0.27 for the four\n    datasets\n  statistics:\n  - about: monkey A\n    test: regression\n    statistic: r = -0.05\n    p: 0.82\n  - about: monkey B\n    test: regression\n    statistic: r = -0.03\n    p: 0.85\n  - about: monkey J\n    test: regression\n    statistic: r = -0.07\n    p: 0.52\n  criterion: As ap-location-no-effect-j-array, on single-electrode datasets the archive does not\n    describe.\n- id: fig7c-anterior-posterior-performance\n  statement: The peri-movement space captures preparatory tuning at both anterior and posterior\n    sites, with normalized performance only slightly different from that of randomly divided data,\n    and slightly better at anterior sites.\n  source: Results, Comparison of anterior versus posterior sites, paragraph 1; Figure 7C\n  quote: The ability of the peri-movement space to capture tuning also held for both anterior and\n    posterior sites\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: As the Figure 7C legend gives it. Neurons split at the median AP location (anterior\n    at or above, posterior at or below); for each half, a 6-D peri-movement space from that half's\n    neurons and PD performance, divided by the upper limit of fig6-preparatory-dimensionality\n    computed on the same half; the same for random halves (20 random splits, a standard choice).\n    Open, the dimensionality of the upper limit; readings (a) 6, (b) its best k. AP location as\n    in ap-location-no-effect-j-array. The paper averages over datasets. Reproduced when both\n    halves have normalized performance above zero and within 10% of the random halves' value;\n    which half is higher is reported.\n- id: prep-activity-more-anterior\n  statement: Preparatory activity is more prevalent at anterior sites.\n  source: Results, Comparison of anterior versus posterior sites, paragraph 1\n  quote: We similarly found preparatory activity to be more prevalent at anterior sites (data not\n    shown)\n  criterion: The paper shows no data or test. The fraction of units passing the preparatory\n    tuning threshold (opening comment) in the anterior and posterior halves split at the median\n    AP location, AP as in ap-location-no-effect-j-array. Readings (a) a higher fraction anterior,\n    (b) higher with a Fisher exact test at p < 0.05. Reproduced when it holds under a reading.\n- id: fig7d-pd-consistency\n  statement: The PD is most stable across random condition subsets when measured in the\n    peri-movement space, for every comparison and all four datasets.\n  source: Results, Stability of the PD, paragraph 1; Figure 7D\n  quote: Yet for every comparison, and for all four datasets, the PD was most stable when measured\n    in the peri-movement space\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: As the Results and Figure 7D legend give it. Per neuron, 25 conditions drawn at random\n    with replacement, the PD fitted; another 25 drawn, the PD refitted; consistency is the dot\n    product of the two unit PDs, averaged over neurons. Comparison spaces for the maze task are\n    endpoints + maximum speed (3-D), segment directions (6-D) and the kinematic space at its best\n    k from fig6d-perimovement-best-j-array; the peri-movement space at the same dimensionality as\n    each. EMG is absent for J-array. The number of draws per neuron is not given; 100 is used as\n    a standard choice that changes only the noise of the mean. Reproduced when the peri-movement\n    space is more consistent in all three comparisons; partially reproduced in two.\n- id: some-neurons-better-elsewhere\n  statement: Although the peri-movement space performs best on average, some individual neurons are\n    better captured in one of the other spaces.\n  source: Discussion, paragraph 3\n  quote: while the peri-movement space performed better on average, there were individual neurons\n    whose activity was better captured in one of the other spaces\n  depends_on:\n  - fig6d-perimovement-best-j-array\n  criterion: Per-neuron performances of fig6d-perimovement-best-j-array, each space at its best k\n    (averaged over neurons) and task spaces at their own dimensionality. Reproduced when at least\n    one neuron has higher performance in another space than in the peri-movement space; the\n    fraction is reported.\n- id: fig8-linear-dynamics-simulation\n  statement: In a simulated two-unit linear dynamical system with 25 random initial states,\n    preparatory activity correlates weakly with peri-movement activity at the single-unit level (r\n    = 0.08), yet a PD in the PCA-based peri-movement space captures preparatory tuning perfectly.\n  source: Results, Tuning from a dynamical systems perspective, paragraph 2; Figure 8\n  quote: The correlation of preparatory activity with peri-movement activity (averaged over the\n    gray interval) was 0.08 ... The PD points towards the pattern recruited by the activity of\n    unit one (panel A ), and perfectly captures preparatory 'tuning'\n  expected:\n    quantity: correlation of unit 1 preparatory rate with its mean peri-movement rate\n    value: 0.08\n    tolerance: 0.008\n  criterion: A simulation, not a test on recorded data. x(t+1) = W x(t), W = [1, -2π/360; 2π/360,\n    1], 25 random initial states held, then released (Figure 8 legend). Open, the distribution of\n    initial states (readings uniform in a square centred on zero, standard Gaussian), the number\n    of time steps after release and the gray interval (readings one full cycle of 360 steps, the\n    first quarter cycle). The 0.08 rests on one random draw, so its tolerance does not apply to a\n    single run; reproduced when 0.08 lies inside the central 95% of the correlations over 1000\n    draws under a reading, and the 2-D PCA peri-movement space with the PD model of the opening\n    comment fits unit 1's initial rates with performance 1 to numerical precision, without\n    cross validation.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/000139/10.1016-j.neuron.2010.09.015.yaml; sed -i '/^    test: not named$/d' $f; sed -i 's/^    value: 8.5$/    value: 8.65/; s/^    tolerance: 2.2$/    tolerance: 2.35/' $f; python tools/claims_check.py $f paper/10.1016-j.neuron.2010.09.015.txt; grep -n "—\|rather" $f; grep -nE "^\s+[^#].*[^ ]: " $f | grep -vE "^\s*[0-9]+:\s*(- )?[a-z_]+: " | head
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/000139/10.1016-j.neuron.2010.09.015.yaml`. The quote checker passes it with no problems: 22 claims, 22 quotes found word for word, 9 statistical values.

**Text read:** the NIH author manuscript in PubMed Central (PMC2991102), not the version of record. That covers the main text, Methods, figure legends and the one supplement (Supplemental Figures 1 to 5, Supplemental Text, Supplemental Experimental Procedures). The paper links no code, so every method comes from the Methods, the legends or the supplement.

**Claims:**
- **Quotes:** all 22 have one, so none needed an `inferred` note.
- **Statistics:** 7 claims carry them. These are the p-values for the mean tuning correlations, the regressions on anterior-posterior (AP) location, and Figure 6E's p < 0.001. The paper doesn't name the tests behind the mean-correlation p-values or the Figure 6E asterisks.
- **Expected values:** 6 claims.
- **Criteria:** all 22 have one. A shared method section in the opening comment gives the trial selection, time windows, neuron thresholds, the preferred-direction (PD) model, the cross-validated performance measure, and the PCA and task spaces, each with its source.
- **What this dataset can test:** the archive describes array recordings of monkey J in the maze task, so the claims for that dataset (Figure 4D, 4E, 6D, 7A to 7D, Supplemental Figure 1, the AP analyses) are testable. Five claims rest on data the archive doesn't describe: the speed-task monkeys A and B, the single-electrode monkey J recordings, EMG, and the Figure 6E summary. One is a simulation (Figure 8).

**Details the paper leaves open, and the readings named:**
- **Maze trial selection:** the "proto-trial" is either the condition's mean velocity profile or one representative trial. The r > 0.9 test applies either to the horizontal and vertical profiles separately or to the two joined.
- **Movement onset detection:** either the dataset's own onset times or a hand-speed threshold.
- **Tuning strength** (for the 5 spikes/s threshold and the 1.5× peri-movement rule): either the range across conditions or the standard deviation across conditions.
- **Preparatory window for the PD analyses:** I use the only window the Methods define (200 ms before the go cue to 100 ms after) and mark it as a reading.
- **Test of mean r against zero:** a one-sample t-test, a Wilcoxon signed-rank test, or a t-test on Fisher z.
- **Kinematic space:** the window ends either at 800 ms after onset or at the end of the reach. "Each neuron contributed one kinematic variable" means either repeating the six signals once per neuron or using them once.
- **Segment directions:** the three segments are equal either in time or in path length.
- **Figure 4E:** which neurons enter (both thresholds, or the preparatory threshold only). "Near zero" means either not significantly above zero or an absolute value below 0.1; the 0.1 is not from the paper.
- **Supplemental Figure 1:** the difference at movement onset must be either smaller than in the preparatory window or less than half of it.
- **"Almost always" (Figure 6, per dimensionality):** read as at least 80% of comparisons; the paper gives no count.
- **The maze task space that "did not perform well":** it is compared either with the 3-D peri-movement space or with the other task spaces.
- **Shuffled control:** "poorly" means either below the unshuffled peri-movement space, or also below the kinematic and task spaces.
- **Figure 7B:** "monkey J" (97%) either includes the J-array dataset or doesn't. When the window start slides, either the window end stays fixed or the whole window shifts.
- **AP location of an array unit:** either the electrode's position along the axis or which array it sits on.
- **Figure 7C:** the dimensionality used for the upper limit is either 6 or its best value.
- **Prevalence of preparatory activity at anterior sites:** the paper shows no data, so the readings are either any higher fraction or a Fisher exact test.
- **Figure 8 simulation:** the distribution of initial states, how long the simulation runs, and the averaging interval.
- **Standard choices that can't change the outcome:** random seeds and the number of draws, and whether the variance divides by c or c - 1.

**Missing from the paper that a claim needed:**
- The values plotted only in Figures 4, 6 and 7 are not in the text, so no claim rests on them.
- The trial count per neuron for J-array is 2166 in the Results and 2155 in the Methods; the claim accepts either.
- The archive limits the dataset to 250 training and 100 test trials, far fewer than the paper's. Whether it is the same recording as J-array, and how many conditions it holds, is left to the author.

I have not committed or pushed anything.

## End of run

22 turns, 5 minutes, result: success.
