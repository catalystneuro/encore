# crcns-hc-11 · claims · run 42365321753

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/001453/ claims/crcns-hc-11 2>&1; ls claims | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "limit": 185
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-13`. Record this version in the attempt's provenance.
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
[... 165 more lines not kept]
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
cd  ls claims | grep -i crcns; ls tools; wc -l paper/*.txt; head -30 paper/10.1126-science.aad1935.txt; head -40 paper/hc-11.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "Supplement\|^#####\|Materials and Methods" paper/10.1126-science.aad1935.txt | head;
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.aad1935.txt",
 "offset": 8,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Supplement and Methods are present. Continuing through the Methods and supplementary figure legends.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.aad1935.txt",
 "offset": 707,
 "limit": 940
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls claims/crcns-hc-10 claims/crcns-hc-9; head -60 claims/crcns-hc-9/*.yaml; grep -n "open\b\|readings\|open:" claims/crcns-hc-9/*.yaml | head; sed -n 1,80p tools/claims_check.py
```

```
claims/crcns-hc-10:
10.1016-j.neuron.2014.03.034.yaml

claims/crcns-hc-9:
10.1523-jneurosci.5680-12.2013.yaml
# Claims for Quattrocolo & Maccaferri (2013), J Neurosci 33:5486-5498, on CRCNS data set hc-9
# (doi:10.6080/K0HQ3WTH).
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-04,
# protocol as stated in docs/protocol.md (Reader).
#
# Text read: the version of record, as supplied under paper/ (PyMuPDF text of the journal PDF),
# with its Materials and Methods, Results, Discussion and the legends of Figures 1 to 13. The
# paper has no supplement. It links no analysis code, so none was read. The PDF could not be
# rendered here, and the extracted text prints the signs =, < and > (and minus, plus/minus,
# mu, Omega) as a replacement character. Each p_relation below is read from the sentence it
# sits in: a difference the text calls significant, or a change it reports, is p < 0.05; one
# it calls absent ("did not change significantly", "similar", "ineffective", "returned to
# baseline") is p > 0.05. Values printed with that character between them are read as mean
# plus/minus SE, as the Methods state ("Data are presented as mean ±SE").
#
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"; grep -n -i "doi\|10.6080" paper/hc-11.data-description.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)); print(list(s['properties']['claims']['items']['properties']))"; sed -n 40,120p paper/hc-11.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  mkdir -p $TMPDIR/pg; python -c "
import fitz,os
d=fitz.open('paper/10.1126-science.aad1935.supp.pdf'); print(len(d))
for p in [13,15,17,19,21,24,25,26,30,31,33,35,37,39,41,43,45,47]:
    d[p-1].get_pixmap(dpi=110).save(os.environ['TMPDIR']+f'/pg/p{p}.png')
"; ls $TMPDIR/pg
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftoppm mutool; pip list 2>/dev/null | grep -i -E "pdf|mupdf|pypdfium"
```

```
(Bash completed with no output)
```

**Agent**

No PDF renderer is installed; I'll read the supplementary figure pages through the Read tool.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.aad1935.supp.pdf",
 "pages": "17,25,33"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  pip install --quiet pymupdf 2>&1 | tail -2; python -c "import fitz;print(fitz.__doc__)"
```

```
Exit code 1
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import fitz;print(fitz.__doc__)
    ^^^^^^^^^^^
ModuleNotFoundError: No module named 'fitz'
```

**Agent calls Bash**

```bash
cd  pip install pymupdf 2>&1 | tail -5; python -m pip --version; which python
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: pip install --upgrade pip
pip 26.2.2 from /opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/pip (python 3.13)
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
```

**Agent calls Bash**

```bash
cd  pip install --target $TMPDIR/pylib pymupdf 2>&1 | tail -3; PYTHONPATH=$TMPDIR/pylib python -c "
import fitz,os
d=fitz.open('paper/10.1126-science.aad1935.supp.pdf'); print(len(d))
for p in [17,19,21,23,25,29,30,31,33,35,36,38,40,41,43,45,47]:
    d[p-1].get_pixmap(dpi=100).save(os.environ['TMPDIR']+f'/p{p}.png')
"; ls $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p17.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p25.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p33.png"
}
```

Result: no output.

**Agent**

Supplementary figures are readable (S5, S9, S14 give medians and p values). Checking the remaining supplementary pages.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p36.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p41.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p30.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p31.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p38.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p40.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p43.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p47.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  sed -n 80,200p tools/claims_check.py
```

```
texts = [t for p in paper_paths for t in flattenings(p.read_text(encoding="utf-8", errors="replace"))]
    problems = 0
    for err in schema("claims").iter_errors(_plain(doc)):
        print("SCHEMA", "/".join(str(x) for x in err.path) or "(top level)", err.message)
        problems += 1
    quotes = values = 0
    for c in doc.get("claims", []):
        if c.get("quote"):
            quotes += 1
            if not quote_found(c["quote"], texts):
                print("QUOTE NOT FOUND", c["id"])
                problems += 1
        for s in c.get("statistics", []):
            for v in [s.get("p")] + ([s["ci"]["low"], s["ci"]["high"]] if "ci" in s else []):
                if v is None:
                    continue
                values += 1
                if not any(f in t for f in printed_forms(v) for t in texts):
                    print("VALUE NOT FOUND (confirm by reading)", c["id"], v)
                    problems += 1
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -o "github[^ ]*\|code[^ ]* availab[^.]*" paper/10.1126-science.aad1935.txt | head; grep -c "" claims/crcns-hc-10/*.yaml; sed -n 1,40p claims/crcns-hc-10/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/crcns-hc-11/10.1126-science.aad1935.yaml",
 "content": "# Claims for Grosmark & Buzsaki (2016), Science 351:1440-1443, on CRCNS data set hc-11\n# (doi:10.6080/K0862DC5).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-07,\n# protocol as stated in docs/protocol.md (Reader).\n#\n# Text read: the NIH author manuscript in PubMed Central (PMC4919122), as supplied under paper/,\n# with the main text and the legends of Figures 1 to 4, and its supplement (Materials and\n# Methods, Figures S1 to S22 with legends, references; PDF from PMC, text by PyMuPDF). The\n# images of the main Figures 1 to 4 are not under paper/, so numbers and significance marks\n# printed only inside those panels are not recorded here. The supplement PDF was rendered to\n# read the supplementary panels: values printed in panel titles (Figures S5, S9, S12, S13, S14,\n# S16 to S19) are marked as read from a figure; the text extraction does not hold them, so the\n# quote checker cannot find their p-values. The paper links no analysis code (\"Spike and LFP\n# data are available at CRCNS.org\"); none was read.\n#\n# Main-text figure numbers for supplementary figures are off by one in places: the main text\n# cites figs. S16 and S17 for pair-wise coactivity and temporal bias, which are Figures S17 and\n# S18 of the supplement, and fig. S12 for the exclusion analysis that the Methods call fig. S8.\n# The claims below cite the supplement's own numbering.\n#\n# Data the paper used. Four male Long-Evans rats, bilateral silicon probes in dorsal CA1 (two\n# with 8-shank BUZ64, two with 6-shank BUZ64SP), recorded at 20 kHz with neck EMG and a\n# head-mounted accelerometer; 562 well isolated pyramidal cells. Eight novelty sessions, each a\n# PRE epoch of about 4 hours of rest and sleep in the home cage in the familiar room A, a MAZE\n# epoch in a novel room on a 1.9 m wooden linear maze (4 sessions), a 2.3 m metal linear maze\n# (1 session) or a 1 m diameter wooden circular maze (3 sessions), then a POST epoch of about 4\n# hours in room A. Position from two head LEDs at 39.69 Hz. Linear mazes have 15 cm reward areas\n# at both ends (1.6 m or 2 m stem); the circular maze has a 30 cm reward area and clockwise\n# running. Place cells n = 491 (counted per running direction on linear mazes). The hc-11\n# description lists the same eight sessions (PRE, MAZE and POST concatenated per session),\n# spike times, cluster identities with putative cell types, LFP at 1250 Hz with EMG and\n# accelerometer channels, spike waveforms and features, and tracked position.\n#\n# Shared method, from the supplement's Materials and Methods unless stated.\n# - Offline states are quiet waking (immobility) and NREM sleep, scored from the CA1 theta/delta\n#   ratio, accelerometer and EMG as in reference 31 (Grosmark et al. 2012). No thresholds are\n#   given (open; see readings S-a and S-b below).\n# - Every PRE and POST analysis is yoked to the duration of the shorter of the two epochs of the\n#   session. Which part of the longer epoch is kept is open. Readings Y-a, the last T of PRE and\n#   the first T of POST (the parts nearest the maze); Y-b, the first T of each epoch; Y-c, T\n#   counted in offline time. T is the duration of the shorter epoch.\n# - Place fields. Spikes and occupancy in 2 cm bins, each smoothed with a 5 cm Gaussian kernel;\n#   rate is smoothed spikes over smoothed occupancy. Only running at 5 cm/s or more outside the\n#   reward areas. Circular maze linearised from the edge of the reward area, clockwise. Null,\n#   5,000 rate vectors from spikes resampled with the unsmoothed occupancy as the density. A\n#   place field is at least 5 consecutive bins above the null 99th percentile with an in-field\n#   peak of at least 1 Hz. Linear mazes are analysed separately for left and right runs. Whether\n#   \"5 cm\" is the kernel's SD or its width is not stated; SD is the standard reading.\n# - Ripple events. All CA1 pyramidal spikes in 1 ms bins convolved with a 15 ms Gaussian (SD,\n#   the standard reading); trigger at mean + 3 SD of all 1 ms bins in NREM of PRE and POST\n#   together; event bounds where the rate returns to that NREM mean. Kept when the event holds\n#   the peak of at least one LFP-detected sharp wave-ripple, lasts 50 to 500 ms, falls in an\n#   offline state, and has at least five distinct pyramidal cells firing. The LFP ripple\n#   detector is not described beyond the 150-250 Hz band of Figure S4; its threshold is open\n#   (readings L-a, peak 150-250 Hz power above mean + 3 SD; L-b, above mean + 5 SD).\n# - Bayesian replay. Events of at least 100 ms with at least 10% of place cells or 5 (whichever\n#   is greater) firing; 20 ms non-overlapping bins; uniform-prior Poisson decoder (equations 1\n#   and 2) on all place cells' smoothed rate maps; weighted correlation r of position and time\n#   (equations 3 to 5); 1,000 circular place-field shuffles (each cell's unsmoothed map rotated\n#   by a random number of bins, then re-smoothed); rZ = (|r observed| - mean |r null|) / SD |r\n#   null| (equation 7). On linear mazes the decoding is done separately for each running\n#   direction. Whether each event is scored with both direction templates (D-a, both scores\n#   kept, as the Figure S20 legend \"we independently compared the results of each running\n#   direction to its null distribution\" suggests) or assigned to one direction by the\n#   direction decoder of equation 6 (D-b, the method the Methods give for Figure 1D) is open.\n# - Per cell contribution (PCC). For each place cell, 1,000 templates in which only that cell's\n#   map is circularly shuffled; for each event the cell fired in, PCC = (rZ observed - mean rZ\n#   cell shuffle) x number of participating place cells (equation 8, Figure S9A); rZ of a\n#   cell-shuffled template uses the event's own null mean and SD (the reading the equations\n#   imply). PRE and POST PCC are the means over the cell's PRE and POST events; dPCC = POST - PRE.\n# - Strongly contributing cells, rigid and plastic cells. A cell is strongly contributing when\n#   its per-event PCC scores are significant (p < 0.05, one-tailed) in PRE or POST. The Methods\n#   name a one-tailed rank-sum test; the Figure S19B legend names a one-tailed signed-rank test\n#   (readings P-a, signed-rank test of per-event PCC against zero; P-b, rank-sum test of the\n#   event's observed rZ against its mean cell-shuffled rZ). Within each session and running\n#   direction, strongly contributing cells at or below the 50th percentile of dPCC are rigid,\n#   those above are plastic, and with an odd count the median cell is dropped.\n# - Offline excitability measures (Figure S14 legend). Firing rate, spikes per second in\n#   offline states; within-ripple rate over concatenated ripple events; within-ripple gain,\n#   within-ripple rate over offline rate; ripple participation, the percentage of ripple events\n#   with at least one spike; burstiness, the percentage of ISIs under 6 ms (all, or within\n#   ripples); within-ripple \"on\" rate, the within-ripple rate over events with a spike.\n# - Pair-wise coactivity. Pearson correlation of 100 ms binned rates in offline states of PRE\n#   and POST, and during running above 5 cm/s on the maze; pairs on the same shank excluded.\n# - Temporal bias. CCG of half-width 150 ms in offline PRE and POST and in running on the maze;\n#   bias = (spikes with the reference after the comparison - spikes before) / all coincident\n#   spikes; pairs on one shank or with fewer than 40 coincident spikes in either condition\n#   excluded; similarity is the median Pearson r (and its p) over 1,000 random sign flips per\n#   pair applied alike to both epochs.\n# Readings S-a and S-b for state scoring: S-a, the lab's own state epochs if the data set holds\n# them (the paper's scoring); S-b, a recomputed scoring by the theta/delta ratio and EMG with\n# thresholds the author states. Every criterion below names the readings it rests on; the\n# outcome is the one all its readings give.\nschema_version: 2\ndataset:\n  archive: crcns\n  id: hc-11\n  doi: 10.6080/K0862DC5\npaper: doi:10.1126/science.aad1935\nclaims:\n- id: place-cell-count\n  statement: Of the 562 well isolated CA1 pyramidal cells recorded in the eight sessions, 491 had\n    place fields on the novel maze, counted separately for each running direction on the linear\n    mazes, which is 54% of pyramidal cells by running direction.\n  source: Results, paragraph 2; Materials and Methods, Animals, Surgery and Data Collection;\n    Figure S2 legend; Figure S19 legend\n  quote: constructed from the firing-rate vectors of place cells ( n = 491 cells) during track\n    running (eight novel exploration sessions) ... In total, 562 well isolated pyramidal cells\n    were included in this study ... Note that 54% of all putative pyramidal cells were\n    considered to have place fields by running direction\n  expected:\n  - quantity: place cells, per running direction\n    value: 491\n    tolerance: 49.1\n  - quantity: pyramidal cells\n    value: 562\n    tolerance: 56.2\n  - quantity: percentage of pyramidal cells with place fields, by running direction\n    value: 54\n    tolerance: 5.4\n    unit: '%'\n  criterion: Pyramidal cells as the data set's putative cell types label them. Place fields by\n    the place-field method of the opening comment, per running direction on the linear mazes\n    and once on the circular maze. The denominator of 54% is open; readings (a) pyramidal cells\n    times the number of running directions of their session (2 on linear mazes, 1 on the\n    circular maze); (b) the 562 pyramidal cells. Reproduced when the counts are within\n    tolerance under one reading.\n- id: fig1c-sequence-content\n  statement: Ripple-event sequence scores (rZ) are above chance in PRE, MAZE and POST, highest on\n    the MAZE, and higher in POST than in PRE sleep (replay).\n  source: Figure 1C; Figure S5 legend; Results, paragraph 2\n  quote: Cumulative distribution of rZ for PRE, MAZE, and POSTevents ... Sequence content\n    increases from PRE to POST\n  criterion: Events, decoding and rZ by the ripple-event and Bayesian replay methods of the\n    opening comment. Tests from the Figure 1C legend, a sign-rank test of rZ against zero within\n    each epoch, and a Kruskal-Wallis test across PRE, MAZE and POST followed by Tukey-Kramer\n    tests. Reproduced when rZ is above zero in all three epochs (p < 0.05), POST rZ exceeds PRE\n    rZ and MAZE exceeds both (Tukey-Kramer p < 0.05), under all readings of Y, L, S and D;\n    partially reproduced when POST exceeds PRE but another part fails. The Figure 1C panel\n    values are not available here, so no level is fixed. The time-bin-shuffle rZ of Figure S22B\n    is shown as a variant.\n- id: figs5b-abs-r-above-null\n  statement: Absolute weighted correlations of ripple events exceed those of the shuffled null\n    in PRE, MAZE and POST, and the POST minus PRE increase is larger in the observed than in the\n    null data.\n  source: Figure S5B\n  quote: Note that in all three epochs, a greater degree of sequence content is observed than\n    expected by chance\n  criterion: Events and shuffles as in fig1c-sequence-content. Per the Figure S5B legend,\n    observed against null |r| within each epoch by rank-sum test, and the POST - PRE change of\n    mean |r| tested by bootstrap. Reproduced when observed |r| exceeds null |r| in all three\n    epochs at p < 0.05 and the observed POST - PRE change exceeds the null change (bootstrap 95%\n    interval of the difference above zero), under the readings of fig1c-sequence-content.\n  depends_on:\n  - fig1c-sequence-content\n- id: figs5e-duration-unchanged\n  statement: Ripple-event duration did not differ between PRE and POST (median 183 ms against\n    186 ms).\n  source: Figure S5E legend\n  quote: While ripple-event duration did not differ between the PRE and POST epochs (PRE median\n    duration 183ms, POST median duration 186ms, p < 0.07, Rank-Sum test)\n  statistics:\n  - test: Rank-Sum test\n    p: 0.07\n    p_relation: <\n  expected:\n  - quantity: PRE median ripple-event duration\n    value: 183\n    tolerance: 18.3\n    unit: ms\n  - quantity: POST median ripple-event duration\n    value: 186\n    tolerance: 18.6\n    unit: ms\n  criterion: A claim of absence, judged by the paper's rank-sum test of PRE against POST event\n    durations at p < 0.05. Which events are plotted is open; readings (a) all ripple events of\n    the opening comment; (b) the events used for Bayesian replay (at least 100 ms, enough place\n    cells). Reproduced when the test is not significant and both medians are within tolerance\n    under one reading; the size of the difference is reported either way.\n- id: figs5f-more-participation-post\n  statement: A greater percentage of place cells participated (fired at least one spike) in POST\n    than in PRE ripple events.\n  source: Figure S5F legend\n  quote: a significantly greater percentage of place cells participated (fired at least one spike\n    in) POST epoch events\n  criterion: Per event, the percentage of the session's place cells (per running direction\n    template under reading D-a) firing at least one spike, on the events of\n    fig1c-sequence-content. The Figure S5 legend names no test for panel F; the rank-sum test it\n    names for panel E is used. Reproduced when POST exceeds PRE at p < 0.05.\n  depends_on:\n  - fig1c-sequence-content\n- id: figs9b-pcc-post-higher\n  statement: Place cells contribute more to POST than to PRE sequence content (median PCC -0.011\n    in PRE, 0.183 in POST), and the median change dPCC is 0.159.\n  source: Figure S9B (values read from the panel titles)\n  quote: Note that consistent with the main Δreplay effect (Fig. 1C, POST > PRE sequence scores\n    (rZ)), cells show significantly higher POST, compared to PRE PCC scores\n  statistics:\n  - about: PRE against POST PCC, all place cells\n    test: rank-sum test\n    p: 0\n    n: 491 place cells\n  - about: dPCC against zero\n    test: signed-rank test\n    p: 0\n    n: 491 place cells\n  expected:\n  - quantity: median PRE PCC\n    value: -0.011\n    tolerance: 0.02\n  - quantity: median POST PCC\n    value: 0.183\n    tolerance: 0.0183\n  - quantity: median dPCC\n    value: 0.159\n    tolerance: 0.0159\n  criterion: PCC by the method of the opening comment, for all place cells. Panel titles print\n    \"p ~ 0\", recorded as 0. The tolerance on the PRE median is not 10% of a value near zero;\n    it is about 10% of the gap between the PRE and POST medians (0.194). Reproduced when POST PCC\n    exceeds PRE PCC (rank-sum p < 0.05), dPCC exceeds zero (signed-rank p < 0.05), and the\n    three medians are within tolerance, under readings Y and D; partially reproduced when the\n    tests hold but a median falls outside its tolerance.\n  depends_on:\n  - fig1c-sequence-content\n- id: fig2b-strong-contributors\n  statement: 216 place cells contributed significantly to PRE or POST sequence content; 97 in\n    PRE, 190 in POST, 71 in both, 26 in PRE only and 119 in POST only.\n  source: Results, paragraph 2; Figure 2B; Figure S19A (counts read from the panel)\n  quote: Neurons that showed significant PCC scores in either PRE or POST were considered to be\n    strongly contributing to sequence formation ( n = 216 neurons\n  expected:\n  - quantity: strongly contributing cells\n    value: 216\n    tolerance: 21.6\n  - quantity: cells significant in PRE\n    value: 97\n    tolerance: 9.7\n  - quantity: cells significant in POST\n    value: 190\n    tolerance: 19\n  - quantity: cells significant in both\n    value: 71\n    tolerance: 7.1\n  criterion: Counts of place cells (per running direction) with per-event PCC significant at p\n    < 0.05 one-tailed, under readings P-a and P-b of the opening comment. Reproduced when all\n    four counts are within tolerance under one reading; partially reproduced when the total is\n    within tolerance but a subset count is not.\n  depends_on:\n  - figs9b-pcc-post-higher\n- id: fig2-pre-contributors-persist\n  statement: The majority (73%) of neurons strongly contributing to PRE sequences also\n    contributed to POST sequences.\n  source: Results, paragraph 2; Figure S19A\n  quote: Importantly, the majority of neurons strongly contributing to PRE (73%) also contributed\n    to POST sequences\n  expected:\n    quantity: percentage of PRE-significant cells also POST-significant\n    value: 73\n    tolerance: 7.3\n    unit: '%'\n  criterion: From the cells of fig2b-strong-contributors, the number significant in both PRE and\n    POST over the number significant in PRE, under readings P-a and P-b. Reproduced when within\n    tolerance under one reading.\n  depends_on:\n  - fig2b-strong-contributors\n- id: rigid-plastic-counts\n  statement: Splitting strongly contributing cells at each session's median dPCC gives 105 rigid\n    and 105 plastic cells.\n  source: Materials and Methods, Rigid and Plastic Cell Classification\n  quote: the strongly contributing cells equal to or below the 50th percentile of that session’s\n    ΔPCC were considered rigid cells (n = 105 cells, blue x’s), while the strongly contributing\n    cells above the 50th percentile of that session’s ΔPCC distribution were considered plastic\n    cells (n = 105 cells\n  expected:\n  - quantity: rigid cells\n    value: 105\n    tolerance: 10.5\n  - quantity: plastic cells\n    value: 105\n    tolerance: 10.5\n  criterion: Classification as in the opening comment (per session and running direction, the\n    median cell dropped for odd counts). Reproduced when both counts are within tolerance.\n  depends_on:\n  - fig2b-strong-contributors\n- id: fig2d-high-dpcc-shuffle-abolishes-replay\n  statement: Shuffling the place fields of the 10 to 20% of cells with the highest dPCC\n    eliminates the POST over PRE increase in sequence content, while it survives shuffling\n    of the cells with the lowest dPCC.\n  source: Figure 2D; Results, paragraph 2\n  quote: Replay (POST > PRE) was eliminated after shuffling or removal of the top 10 to 20% of\n    cells with the highest ΔPCC scores, whereas it remained after shuffling or removal of the\n    bottom 75%\n  expected:\n    quantity: percentage of highest-dPCC cells shuffled at which POST - PRE rZ reaches zero\n    value: 15\n    tolerance: 7\n    unit: '%'\n  criterion: Per the Methods (Per Cell Contribution, last paragraph) and the Figure 2D legend,\n    within each session an increasing percentage of place cells (ranked by dPCC, from the\n    highest or from the lowest) has its maps circularly shuffled (1,000 templates), the\n    replay analysis is rerun, and mean POST rZ - mean PRE rZ is pooled over sessions, with a\n    bootstrapped 95% interval. Percentage steps are not given; 5% steps are a standard choice.\n    The expected value stands for the range 10 to 20%, widened by 10% of each bound (9 to 22%).\n    Reproduced when, shuffling from the highest dPCC, the change first falls to zero or below\n    between 9 and 22%, and, shuffling from the lowest dPCC, it stays above zero up to 75%,\n    under readings Y and D.\n  depends_on:\n  - figs9b-pcc-post-higher\n- id: figs12-high-dpcc-exclusion\n  statement: Excluding the 10 to 20% of cells with the highest dPCC turns the POST minus PRE\n    change in sequence content negative, while excluding up to about 75% of the lowest dPCC\n    cells leaves POST above PRE.\n  source: Figure S12\n  quote: Note that even after excluding up to ~75% of ‘low’ ΔPCC cells, POST epoch sequence\n    content exceeds PRE epoch sequence content ... after the exclusion of just 10 to 20% of\n    cells PRE epoch sequence content exceeded POST epoch sequence content\n  criterion: As fig2d-high-dpcc-shuffle-abolishes-replay, with cells excluded from the template\n    and event selection (the 100 ms and 10% or 5 cell criteria applied after exclusion, per the\n    Methods) in place of shuffled. Reproduced when, excluding from the highest dPCC, POST - PRE\n    rZ falls below zero between 9 and 22% excluded, and, excluding from the lowest, the lower\n    bound of its bootstrapped 95% interval stays above zero up to 75%, under readings Y and D.\n  depends_on:\n  - figs9b-pcc-post-higher\n- id: figs2-rigid-plastic-along-track\n  statement: Rigid and plastic cells' place fields are similarly distributed along the track,\n    both enriched near the start and goal ends.\n  source: Results, paragraph 2; Figure S2 legend\n  quote: Rigid and plastic neurons were similarly distributed along the track\n  criterion: The paper shows this only as rate maps and gives no test, so the test is open.\n    Measure, each cell's peak place-field position (per running direction) as a fraction of\n    track length from the start of the run. Readings (a) a two-sample Kolmogorov-Smirnov test of\n    rigid against plastic positions; (b) a rank-sum test of the distance of each peak from the\n    nearer track end. Reproduced when neither reading finds a difference at p < 0.05; the\n    fractions of fields in the outer fifths of the track are reported for each group.\n  depends_on:\n  - rigid-plastic-counts\n- id: fig3a-plastic-more-specific\n  statement: On the novel maze plastic cells have higher place specificity than rigid cells and\n    fewer place fields.\n  source: Figure 3A; Results, paragraph 3; Figure S19E\n  quote: Plastic neurons had higher place-specific indices and fewer place fields compared with\n    rigid cells\n  statistics:\n  - test: rank-sum tests\n    p: 0.05\n    p_relation: <\n  criterion: The Figure 3A panels are not available here; Figure S19E, which the legend says to\n    compare to Figure 3A, shows six measures, within/outside place-field rate ratio, information\n    per spike, information per second, spatial coherence, place-field stability and number of\n    place fields. Measures as in reference 32 (Mizuseki et al. 2012) per the Methods; the\n    stability split is not given here (readings (a) first against second half of the maze\n    epoch; (b) odd against even laps). Rank-sum test, rigid against plastic (Figure 3A legend).\n    Reproduced when plastic cells are higher on at least four of the five specificity measures\n    and have fewer place fields, each at p < 0.05, under one stability reading; partially\n    reproduced when the direction holds for all six but fewer reach p < 0.05.\n  depends_on:\n  - rigid-plastic-counts\n- id: fig3b-plastic-specificity-increases\n  statement: Plastic but not rigid cells steadily increased their spatial specificity during maze\n    running.\n  source: Figure 3B; Results, paragraph 3; Figure S19F\n  quote: plastic but not rigid neurons increased their spatial specificity steadily during\n    learning\n  criterion: Per lap, each cell's percentage of spikes inside its place field(s) (the measure of\n    Figure S19F, the legend's \"infield versus outside field firing ratio\"), using only laps\n    with at least 5 spikes from the cell (Figure S13 legend); per cell, the Pearson\n    correlation of this value with lap number. Tests per the Figure S13C legend, a signed-rank\n    test of each group's correlations against zero and a rank-sum test between groups.\n    Reproduced when plastic cells' correlations are above zero (p < 0.05), rigid cells' are not,\n    and plastic exceeds rigid (p < 0.05). The within-field rate gain of Figure S13C is shown as\n    a variant.\n  depends_on:\n  - rigid-plastic-counts\n- id: figs13-outfield-rate-falls\n  statement: Neither group's overall or within-field firing rate changed significantly over laps;\n    plastic cells' increase in specificity came from a fall in their out-of-field firing rate,\n    which rigid cells did not show.\n  source: Figure S13A, S13D and S13E\n  quote: Notably, neither cell group showed a significant increase in within-field firing rate\n    over the course of maze running. (E) Conversely, a significant decrease was observed in\n    plastic cells’, but not rigid cells’, outside of field firing rates\n  criterion: Per cell, the Pearson correlation of lap rate (overall, within field, outside field)\n    with lap number, laps with at least 5 spikes, running above 5 cm/s. Signed-rank test of each\n    group's correlations against zero (Figure S13C legend). Reproduced when the outside-field\n    correlations of plastic cells are below zero (p < 0.05) and those of rigid cells are not,\n    and neither group's overall or within-field correlations differ from zero at p < 0.05.\n  depends_on:\n  - rigid-plastic-counts\n- id: fig4a-rigid-fire-faster\n  statement: Rigid cells fire faster than plastic cells in offline states (session-wide median\n    0.76 against 0.54 Hz; PRE 0.762 against 0.479 Hz; POST 0.753 against 0.472 Hz), but not\n    during maze running (1.09 against 1.13 Hz).\n  source: Figure 4A; Results, paragraph 4; Figure S14, firing rate row (values read from the\n    panel titles)\n  quote: Session-wide firing rates of rigid neurons were significantly higher compared with\n    plastic neurons\n  statistics:\n  - about: session-wide\n    test: rank-sum test\n    p: 0.001\n    p_relation: <\n    n: 105 rigid and 105 plastic cells\n  - about: PRE\n    test: rank-sum test\n    p: 0.00159\n    p_relation: <\n  - about: POST\n    test: rank-sum test\n    p: 0.00146\n    p_relation: <\n  - about: MAZE\n    test: rank-sum test\n    p: 0.976\n    p_relation: <\n  expected:\n  - quantity: session-wide median rate, rigid\n    value: 0.76\n    tolerance: 0.076\n    unit: Hz\n  - quantity: session-wide median rate, plastic\n    value: 0.54\n    tolerance: 0.054\n    unit: Hz\n  - quantity: PRE median rate, rigid\n    value: 0.762\n    tolerance: 0.0762\n    unit: Hz\n  - quantity: PRE median rate, plastic\n    value: 0.479\n    tolerance: 0.0479\n    unit: Hz\n  - quantity: POST median rate, rigid\n    value: 0.753\n    tolerance: 0.0753\n    unit: Hz\n  - quantity: POST median rate, plastic\n    value: 0.472\n    tolerance: 0.0472\n    unit: Hz\n  criterion: Firing rate as in Figure S14, spikes per second in offline states of each epoch, and\n    during running on the maze for MAZE (the measure for MAZE is not stated; readings (a) all\n    MAZE time; (b) running above 5 cm/s). \"Session-wide\" is not defined; readings (a) offline\n    time of PRE and POST together; (b) the whole recording. Rank-sum tests. Reproduced when the\n    session-wide, PRE and POST differences are significant (p < 0.05) with rigid higher and the\n    medians within tolerance under one reading; partially reproduced when the tests hold and\n    the medians do not.\n  depends_on:\n  - rigid-plastic-counts\n- id: figs14-plastic-ripple-gain\n  statement: Plastic cells have a higher within-ripple firing rate gain than rigid cells (POST\n    median 5.75 against 4.52) and a larger PRE to POST increase in gain (0.81 against 0.14).\n  source: Figure 4A; Results, paragraph 4; Figure S14, within-ripple firing rate gain row\n    (values read from the panel titles)\n  quote: Ripple-related spiking, bursting, and pair-wise coactivation were higher in plastic\n    versus rigid neurons\n  statistics:\n  - about: POST gain\n    test: rank-sum test\n    p: 0.0001\n    p_relation: <\n  - about: session-wide gain\n    test: rank-sum test\n    p: 0.002\n    p_relation: <\n  - about: PRE gain\n    test: rank-sum test\n    p: 0.04\n    p_relation: <\n  - about: POST - PRE change in gain\n    test: rank-sum test\n    p: 0.00306\n    p_relation: <\n  expected:\n  - quantity: POST median gain, plastic\n    value: 5.75\n    tolerance: 0.575\n  - quantity: POST median gain, rigid\n    value: 4.52\n    tolerance: 0.452\n  - quantity: median change in gain, plastic\n    value: 0.81\n    tolerance: 0.081\n  - quantity: median change in gain, rigid\n    value: 0.14\n    tolerance: 0.1\n  criterion: Gain as in the Figure S14 legend, within-ripple rate over offline rate, per epoch.\n    Rank-sum tests, plastic against rigid. The rigid change median is near zero, so its\n    tolerance is set at 0.1, about 10% of the gap between the two groups' changes. Reproduced\n    when plastic exceeds rigid for POST gain and for the change at p < 0.05 and the four medians\n    are within tolerance; partially reproduced when the tests hold and a median does not.\n  depends_on:\n  - rigid-plastic-counts\n- id: figs14-plastic-ripple-bursting\n  statement: Plastic cells burst more within ripples than rigid cells in POST (median 27.3%\n    against 23.3% of ISIs under 6 ms) and increase their within-ripple bursting more from PRE\n    to POST (2.81 against 1.13 percentage points).\n  source: Figure S14, within-ripple burstiness row (values read from the panel titles)\n  inferred: The main text states that ripple-related bursting was higher in plastic cells (Figure\n    4A); the numbers are only in the Figure S14 panel titles.\n  statistics:\n  - about: POST within-ripple burstiness\n    test: rank-sum test\n    p: 0.00183\n    p_relation: <\n  - about: POST - PRE change\n    test: rank-sum test\n    p: 0.01\n    p_relation: <\n  expected:\n  - quantity: POST median within-ripple burstiness, plastic\n    value: 27.3\n    tolerance: 2.73\n    unit: '%'\n  - quantity: POST median within-ripple burstiness, rigid\n    value: 23.3\n    tolerance: 2.33\n    unit: '%'\n  - quantity: median change, plastic\n    value: 2.81\n    tolerance: 0.281\n    unit: percentage points\n  - quantity: median change, rigid\n    value: 1.13\n    tolerance: 0.113\n    unit: percentage points\n  criterion: Within-ripple burstiness as the percentage of within-ripple ISIs under 6 ms. Whether\n    ISIs spanning two ripple events count is open; the reading kept is ISIs between spikes of\n    one event (standard), with all ISIs inside concatenated ripple time as a variant. Rank-sum\n    tests. Reproduced when both tests hold with plastic higher and the medians are within\n    tolerance; partially reproduced when the tests hold and a median does not.\n  depends_on:\n  - rigid-plastic-counts\n- id: figs16ab-plastic-synchrony-increase\n  statement: The PRE to POST increase in ripple-triggered firing is present in plastic but not\n    rigid cells, and the PRE to POST increase in pair-wise coactivity is larger among plastic\n    cells.\n  source: Figure S16A and S16B\n  quote: The PRE to POST increases in ripple-event triggered firing rates seen when all place\n    cells are taken into account (A, left panel) are uniquely present in plastic (A,\n    third-panel) but not rigid (A, second panel) cells ... the PRE to POST increase in pair-wise\n    co-activity observed across all place cells (B, left panel) is more robustly observed in the\n    plastic cell population\n  criterion: Ripple-triggered rate from -50 to 100 ms around event onset (the panel's axis), per\n    cell, PRE and POST. The legend gives no test for panel A; readings (a) a signed-rank test of\n    each cell's POST - PRE mean rate in 0 to 100 ms; (b) the same at the peak bin. Coactivity\n    as in the opening comment, pairs within each group. Reproduced when plastic cells' rate\n    increase is significant (p < 0.05) and rigid cells' is not under one reading of A, and\n    plastic pairs' mean coactivity increase exceeds rigid pairs' (rank-sum, p < 0.05).\n  depends_on:\n  - rigid-plastic-counts\n- id: low-high-rate-split\n  statement: Splitting place cells into equal halves by offline firing rate gives low-rate cells\n    with median 0.39 Hz and high-rate cells with median 1.12 Hz.\n  source: Results, paragraph 5\n  quote: Low-rate neurons (median, 0.39 Hz) contributed more spatial information per spike on the\n    maze and displayed increased within-ripple firing-rate gains from PRE to POST sleep than\n    high-rate cells (median, 1.12 Hz)\n  expected:\n  - quantity: median rate, low-rate cells\n    value: 0.39\n    tolerance: 0.039\n    unit: Hz\n  - quantity: median rate, high-rate cells\n    value: 1.12\n    tolerance: 0.112\n    unit: Hz\n  criterion: The Figure S16 legend points to the Methods for the split, which the Methods do not\n    give. From the text, place cells are split into equal groups by \"off-line\" sleep firing\n    rate, and the Methods state that cells removed from an analysis are chosen within each\n    session. Readings (a) median split within each session and running direction; (b) median\n    split within each session; (c) a pooled median split; and for the rate, (i) offline PRE\n    and POST together; (ii) offline PRE only. Reproduced when both medians are within\n    tolerance under one reading. The reading(s) that match fix the split for the claims that\n    depend on this one.\n- id: figs16c-low-rate-coding\n  statement: Low-rate cells carry more spatial information per spike (0.91 against 0.56\n    bits/spike), have a higher in/out place-field rate ratio (6.38 against 3.86), fewer place\n    fields (log-mean 1.29 against 1.59), and a larger PRE to POST increase in within-ripple gain\n    (0.71 against 0.06) than high-rate cells.\n  source: Figure S16C legend; Results, paragraph 5\n  quote: Low Rate median.:\n    0.91 bits/spike, High Rate med: 0.56 bits/spike, p < 2.5x10-9, Rank-Sum test), had a\n    greater within/outside of place field(s) firing ratio (Low Rate med.: 6.38, High Rate med:\n    3.86, p < 7.9x10-14), and had fewer place fields on the maze (Low Rate log-mean: 1.29,\n    High Rate  log-mean: 1.59, p < 3.94 x10-06). In addition, low rate cells tended to show a\n    more pronounced increase in their within-ripple firing rate gain (Low Rate Δripple-gain\n    med.: 0.71, High Rate med.: 0.06, p <  7.585x10-4\n  statistics:\n  - about: information per spike\n    test: Rank-Sum test\n    p: 2.5e-09\n    p_relation: <\n  - about: within/outside field rate ratio\n    test: Rank-Sum test\n    p: 7.9e-14\n    p_relation: <\n  - about: number of place fields\n    test: Rank-Sum test\n    p: 3.94e-06\n    p_relation: <\n  - about: change in within-ripple gain\n    test: Rank-Sum test\n    p: 0.0007585\n    p_relation: <\n  expected:\n  - quantity: median information per spike, low-rate\n    value: 0.91\n    tolerance: 0.091\n    unit: bits/spike\n  - quantity: median information per spike, high-rate\n    value: 0.56\n    tolerance: 0.056\n    unit: bits/spike\n  - quantity: median in/out field ratio, low-rate\n    value: 6.38\n    tolerance: 0.638\n  - quantity: median in/out field ratio, high-rate\n    value: 3.86\n    tolerance: 0.386\n  - quantity: log-mean number of place fields, low-rate\n    value: 1.29\n    tolerance: 0.129\n  - quantity: log-mean number of place fields, high-rate\n    value: 1.59\n    tolerance: 0.159\n  - quantity: median change in within-ripple gain, low-rate\n    value: 0.71\n    tolerance: 0.071\n  - quantity: median change in within-ripple gain, high-rate\n    value: 0.06\n    tolerance: 0.07\n  criterion: Groups from low-high-rate-split under the reading that matched there. Measures as in\n    fig3a-plastic-more-specific and figs14-plastic-ripple-gain. \"Log-mean\" is read as the\n    geometric mean. The high-rate gain change is near zero, so its tolerance is 0.07, about 10%\n    of the gap between the groups. Reproduced when all four rank-sum tests give p < 0.05 in the\n    stated direction and the medians are within tolerance; partially reproduced when the tests\n    hold and a median does not.\n  depends_on:\n  - low-high-rate-split\n- id: fig4c-coactivation-by-rate\n  statement: In PRE sleep coactivity is dominated by fast-firing cells, whose correlations stay\n    unchanged into POST, while slow-firing cells show the largest PRE to POST increase in\n    coactivation and the greatest replay of maze coactivity.\n  source: Figure 4B and 4C; Results, paragraph 4; Figure S16C\n  quote: In PRE sleep, coactivity was dominated by fast-firing neurons, and these correlations\n    remained unchanged into POST sleep. In contrast, slow-firing neurons showed the strongest\n    increases in coactivation from PRE to POST sleep\n  criterion: Per the Figure 4B and 4C legends, place cells sorted by session firing rate and\n    grouped in overlapping windows of 20% of cells stepped by 1%; in each window, the mean\n    coactivity of its pairs (different shanks) in PRE and POST, the POST - PRE change, and the\n    partial correlation of RUN and POST coactivity given PRE. Whether ranks are taken within\n    session or pooled is open (readings (a) percentile of rate within session; (b) pooled);\n    \"session firing rate\" as in fig4a-rigid-fire-faster. Reproduced when PRE coactivity rises\n    with the window's rate rank, the POST - PRE change and the partial correlation fall with\n    it (Spearman over windows, both p < 0.05), the change in the top window is not\n    significant (signed-rank over pairs, p > 0.05), and, per Figure S16C, the low-rate half's\n    mean change exceeds the high-rate half's (rank-sum, p < 0.05). Partially reproduced when\n    the slow-firing increase holds and the PRE dominance or the top-window stability does not.\n  depends_on:\n  - low-high-rate-split\n- id: fig4d-slow-cells-replay\n  statement: Slow-firing, but not fast-firing, place cells increased their contribution to\n    sequences from PRE to POST sleep.\n  source: Figure 4D; Results, paragraph 5; Figures S20D, S21B and S22E\n  quote: Slow-firing, but not fast-firing, neurons increased their contribution to neuronal\n    sequences from PRE to POST sleep\n  criterion: The Bayesian replay analysis rerun with templates of only the low-rate or only the\n    high-rate place cells (low-high-rate-split), the event criteria applied to the kept cells.\n    The test of the change is open; readings (a) a rank-sum test of POST against PRE rZ within\n    each group (as in Figure 1D); (b) a bootstrapped 95% interval of mean POST - PRE rZ (as in\n    Figure 2D). Reproduced when the low-rate group's POST - PRE rZ is above zero (p < 0.05) and\n    the high-rate group's is not, under each reading; partially reproduced when the low-rate\n    increase holds and the high-rate group also increases but less. The paired-latency (Figure\n    S20D) and time-bin-shuffle (Figure S22E) versions are shown as variants.\n  depends_on:\n  - low-high-rate-split\n  - fig1c-sequence-content\n- id: fig4e-high-gain-cells-replay\n  statement: The PRE to POST increase in sequence content was limited to cells with high\n    ripple-specific recruitment (within-ripple rate gain).\n  source: Figure 4E; Results, paragraph 5; Figures S20E, S21C and S22E\n  quote: Conversely, PRE to POST increases in sequence content were limited to cells that showed a\n    high degree of ripple-specific recruitment (gain)\n  criterion: As fig4d-slow-cells-replay, with the place cells split into equal halves by\n    within-ripple firing-rate gain, under the split and epoch readings that matched in\n    low-high-rate-split. Reproduced when the high-gain group's POST - PRE rZ is above zero (p <\n    0.05) and the low-gain group's is not, under each reading of the test.\n  depends_on:\n  - low-high-rate-split\n  - fig1c-sequence-content\n- id: figs16de-more-ripples-post\n  statement: Ripple events occur more often in POST than in PRE (median inter-event interval 2.47\n    s against 3 s), as do purely LFP-detected sharp wave-ripples (1.06 s against 1.21 s).\n  source: Figure S16D and S16E (medians read from the panel titles)\n  quote: Increased synchrony (B) in the\n    POST compared to PRE epoch may be attributable to both increases in ripple-triggered\n    spiking (A) as well as to an increase in the incidence of ripple events\n  statistics:\n  - about: inter ripple-event intervals, PRE against POST\n    test: Rank-Sum test\n    p: 0\n  - about: inter LFP-SWR intervals, PRE against POST\n    test: Rank-Sum test\n    p: 0\n  expected:\n  - quantity: median inter ripple-event interval, PRE\n    value: 3\n    tolerance: 0.3\n    unit: s\n  - quantity: median inter ripple-event interval, POST\n    value: 2.47\n    tolerance: 0.247\n    unit: s\n  - quantity: median inter LFP-SWR interval, PRE\n    value: 1.21\n    tolerance: 0.121\n    unit: s\n  - quantity: median inter LFP-SWR interval, POST\n    value: 1.06\n    tolerance: 0.106\n    unit: s\n  criterion: Intervals between consecutive events within offline states, intervals under 60 s\n    only (legend); rank-sum test of PRE against POST intervals (\"p ~ 0\" printed, recorded as 0).\n    Ripple events as in the opening comment; LFP-SWR events under readings L-a and L-b. Reproduced\n    when POST intervals are shorter for both event types at p < 0.05 and the ripple-event\n    medians are within tolerance; the LFP-SWR medians depend on the open detector and are\n    reported, matching under one L reading counts toward reproduced.\n- id: figs17-coactivity-preservation\n  statement: Pair-wise coactivity is weakly preserved from PRE to RUN (r = 0.045), more strongly\n    from RUN to POST (r = 0.16), and most strongly from PRE to POST (r = 0.34).\n  source: Figure S17A and S17C (r values read from the panels)\n  quote: the\n    similarity between RUN and POST co-activity patterns (middle panel) was significantly\n    greater (corr(RUN, POST) - corr(RUN, PRE) = 0.11, p ≈ 0, Fisher's Z-test). However, the\n    similarity between RUN and POST was likewise far exceeded by the similarity between\n    PRE and POST co-activity patterns (corr(PRE, POST) - corr(RUN, POST) = 0.18, p ≈ 0,\n    Fisher's Z-test)\n  statistics:\n  - about: corr(RUN, POST) - corr(RUN, PRE)\n    test: Fisher's Z-test\n    p: 0\n  - about: corr(PRE, POST) - corr(RUN, POST)\n    test: Fisher's Z-test\n    p: 0\n  expected:\n  - quantity: Pearson r, PRE against RUN coactivity\n    value: 0.045\n    tolerance: 0.0045\n  - quantity: Pearson r, POST against RUN coactivity\n    value: 0.16\n    tolerance: 0.016\n  - quantity: Pearson r, PRE against POST coactivity\n    value: 0.34\n    tolerance: 0.034\n  - quantity: corr(RUN, POST) - corr(RUN, PRE)\n    value: 0.11\n    tolerance: 0.011\n  - quantity: corr(PRE, POST) - corr(RUN, POST)\n    value: 0.18\n    tolerance: 0.018\n  criterion: Coactivity as in the opening comment, all place-cell pairs on different shanks;\n    Pearson correlation across pairs between epochs; differences of correlations by Fisher's Z\n    test (as two independent correlations, the test's usual form; a test for dependent\n    correlations is the other reading). Reproduced when both differences are significant (p <\n    0.05) in the stated direction and the values are within tolerance; partially reproduced\n    when the order RUN-PRE < RUN-POST < PRE-POST holds but values fall outside tolerance.\n- id: figs17d-rigid-plastic-coactivity\n  statement: Rigid cell pairs preserve PRE coactivity into RUN (r = 0.139) and into POST (r =\n    0.31) more than plastic pairs (-0.02 and 0.09), while plastic pairs show higher RUN to POST\n    preservation (0.36 against 0.11).\n  source: Figure S17D (r values read from the panels); Results, paragraph 4\n  quote: Rigid cell, but not plastic cell, pairs\n    showed preservation of PRE co-activity patterns during the RUN. Conversely, plastic cell\n    pairs showed a significantly higher preservation of co-activity patterns from the RUN to\n    the POST\n  expected:\n  - quantity: rigid pairs, PRE against RUN r\n    value: 0.139\n    tolerance: 0.0139\n  - quantity: plastic pairs, PRE against RUN r\n    value: -0.02\n    tolerance: 0.05\n  - quantity: rigid pairs, RUN against POST r\n    value: 0.11\n    tolerance: 0.011\n  - quantity: plastic pairs, RUN against POST r\n    value: 0.36\n    tolerance: 0.036\n  - quantity: rigid pairs, PRE against POST r\n    value: 0.31\n    tolerance: 0.031\n  - quantity: plastic pairs, PRE against POST r\n    value: 0.09\n    tolerance: 0.009\n  criterion: As figs17-coactivity-preservation within rigid-rigid and plastic-plastic pairs;\n    groups compared by Fisher's Z test (Figure S17D legend). The plastic PRE-RUN r is near zero,\n    so its tolerance is 0.05, read as consistent with zero. Reproduced when the three group\n    differences are significant (p < 0.05) in the stated direction; the r values are reported\n    against tolerance, and a mismatch in values with the differences holding is partially\n    reproduced.\n  depends_on:\n  - rigid-plastic-counts\n- id: figs18-temporal-bias\n  statement: Pair-wise temporal biases are not preserved from PRE to RUN (r = -0.009) but are\n    preserved from RUN to POST (r = 0.117) and PRE to POST (r = 0.201); the PRE to POST\n    preservation is carried by rigid cell pairs (r = 0.29) and the RUN to POST preservation by\n    plastic cell pairs (r = 0.26).\n  source: Figure S18B and S18C (r values read from the panels); Results, paragraph 4\n  quote: When\n    all place cells are included in the analysis, no similarity is observed between PRE and\n    RUN (left panel) temporal biases. However, temporal biases are strongly preserved from\n    the RUN to POST epochs (middle panel), as well as from the PRE to POST epochs\n    (right). (C) Limiting this analysis to rigid (blue) or plastic (red) cell pairs, reveals that the\n    preservation of temporal spiking patterns from PRE to POST and from RUN to POST is\n    attributable to the rigid and plastic cell subpopulations, respectively\n  expected:\n  - quantity: all pairs, PRE against RUN r\n    value: -0.009\n    tolerance: 0.05\n  - quantity: all pairs, RUN against POST r\n    value: 0.117\n    tolerance: 0.0117\n  - quantity: all pairs, PRE against POST r\n    value: 0.201\n    tolerance: 0.0201\n  - quantity: rigid pairs, PRE against POST r\n    value: 0.29\n    tolerance: 0.029\n  - quantity: plastic pairs, RUN against POST r\n    value: 0.26\n    tolerance: 0.026\n  criterion: Temporal bias and its median r over 1,000 sign randomisations as in the opening\n    comment. The PRE-RUN value is near zero; its tolerance of 0.05 reads it as consistent with\n    zero. Reproduced when the PRE-RUN r is not significant (p > 0.05), RUN-POST and PRE-POST are\n    (p < 0.05), the rigid PRE-POST and plastic RUN-POST r are significant while the plastic\n    PRE-POST (-0.037) and rigid RUN-POST (0.024) are not, and the values are within tolerance;\n    partially reproduced when the significance pattern holds and a value does not.\n  depends_on:\n  - rigid-plastic-counts\n- id: figs11-cluster-quality-similar\n  statement: Rigid and plastic cells have similar waveforms and similar cluster quality and\n    stability across PRE, MAZE and POST, so clustering errors do not explain their differences.\n  source: Figure S11; Results, paragraph 3\n  quote: Note\n    that rigid and plastic cell waveforms are similar to each other and stable from the PRE to\n    the POST epochs\n  criterion: A claim of absence, judged by the paper's rank-sum tests of rigid against plastic\n    cells at p < 0.05 (Figure S11 legend). Quality is the median Mahalanobis distance of each\n    spike's PCA features to its cluster mean, for spikes in PRE ripple events, MAZE running and\n    POST ripple events; stability is the symmetric Mahalanobis distance between a cell's\n    clusters in two conditions; first spikes of bursts (ISI under 6 ms) only. Reproduced when no\n    comparison is significant; the effect sizes are reported either way.\n  depends_on:\n  - rigid-plastic-counts\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/crcns-hc-11/10.1126-science.aad1935.yaml paper/10.1126-science.aad1935.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/crcns-hc-11/10.1126-science.aad1935.yaml'
s=open(p).read()
start=s.index('  quote: Low Rate median.:')
end=s.index('  statistics:',start)
new='''  quote: low-rate cells also contributed more information per spike (Low Rate median ... 0.91
    bits/spike, High Rate med ... 0.56 bits/spike, p < 2.5x10-9, Rank-Sum test), had a greater
    within/outside of place field(s) firing ratio (Low Rate med ... 6.38, High Rate med ... 3.86,
    p < 7.9x10-14), and had fewer place fields on the maze (Low Rate log-mean ... 1.29, High Rate
    log-mean ... 1.59, p < 3.94 x10-06). In addition, low rate cells tended to show a more
    pronounced increase in their within-ripple firing rate gain (Low Rate Δripple-gain med ...
    0.71, High Rate med ... 0.06, p < 7.585x10-4
'''
s=s[:start]+new+s[end:]
s=s.replace('p_relation: <\n','p_relation: "<"\n')
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/crcns-hc-11/10.1126-science.aad1935.yaml paper/10.1126-science.aad1935.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n "corr(RUN, POST) - corr" paper/10.1126-science.aad1935.txt | cat -A | cut -c1-200
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='claims/crcns-hc-11/10.1126-science.aad1935.yaml'
s=open(p).read()
old="co-activity patterns (middle panel) was significantly\n    greater (corr"
assert old in s
s=s.replace(old,"co-activity patterns (middle panel) was significantly ...\n    greater (corr")
open(p,'w').write(s)
EOF
python tools/claims_check.py claims/crcns-hc-11/10.1126-science.aad1935.yaml paper/10.1126-science.aad1935.txt; grep -n " — \|rather" claims/crcns-hc-11/10.1126-science.aad1935.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/crcns-hc-11/10.1126-science.aad1935.yaml'))
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c),[x['id'] for x in c if 'inferred' in x])"
```

```
29 9 29 16 ['figs14-plastic-ripple-bursting']
```

**Agent**

I wrote `claims/crcns-hc-11/10.1126-science.aad1935.yaml`. All quotes pass the checker. The only problems it reports are 9 p-values I read from supplementary figure panels, which the text file does not contain; I checked each against the rendered page.

**Text read:** the NIH author manuscript in PMC (PMC4919122), with the main text, the legends of Figures 1 to 4, and the full supplement (Materials and Methods, Figures S1 to S22 with legends, references). I rendered the supplement PDF to read numbers printed inside panels of Figures S5, S9, S12, S13, S14 and S16 to S19. The paper links no analysis code; it only says the data are at CRCNS.org.

**Claims:** 29 in total.
- 28 have quotes. One (`figs14-plastic-ripple-bursting`) is marked `inferred`, because its numbers appear only in Figure S14 panel titles.
- 9 have statistics, 16 have expected values, and all 29 have criteria.
- They cover:
  - the replay increase from PRE to POST, and the scores against the shuffled null
  - per-cell contribution scores (PCC), the strongly contributing cells, the 73% overlap, and the 105 rigid and 105 plastic cells
  - the shuffle and exclusion analyses of the highest-ΔPCC cells
  - spatial coding of rigid against plastic cells, and specificity changes within the session
  - firing rate, ripple gain and bursting
  - the low and high firing-rate split, coactivity by firing rate, and replay restricted to slow-firing or high-gain cells
  - ripple incidence, preservation of coactivity and temporal bias, and cluster quality

**Details the paper leaves open, and the readings named for each:**
- **Yoking PRE and POST to the shorter epoch:** (a) the last part of PRE and the first part of POST; (b) the first part of each; (c) time counted only in offline states.
- **LFP ripple detection threshold:** (a) mean + 3 SD; (b) mean + 5 SD, both in the 150 to 250 Hz band.
- **Sleep and state scoring thresholds:** (a) the lab's own state epochs; (b) a recomputed scoring.
- **Linear-track events:** (a) each event scored with both direction templates; (b) each event assigned to one direction by the direction decoder.
- **Test for a strongly contributing cell:** the Methods name a rank-sum test and the Figure S19B legend a signed-rank test. Readings: (a) signed-rank test of per-event PCC against zero; (b) rank-sum test of observed against cell-shuffled scores.
- **Low and high firing-rate split:** the Figure S16 legend refers to the Methods, which do not describe it. Readings: median split within session and direction, within session, or pooled; rate from offline PRE and POST together or from PRE alone.
- **"Session-wide" firing rate:** (a) offline time of PRE and POST together; (b) the whole recording.
- **MAZE rate:** (a) all maze time; (b) running only.
- **Place-field stability:** (a) first against second half of the maze epoch; (b) odd against even laps.
- **Event set for the duration claim:** (a) all ripple events; (b) only the events used for Bayesian replay.
- **Tests the paper does not name:**
  - for the replay comparisons of slow against fast cells and high against low gain: rank-sum test, or a bootstrapped confidence interval
  - for the similar track distribution of rigid and plastic fields: Kolmogorov-Smirnov test, or a rank-sum test of distance from the track ends
  - for the ripple-triggered rate change: mean rate over 0 to 100 ms, or the peak bin
  - for the rate-window ranking in the coactivity analysis: ranks within session, or pooled
- **Standard choices that cannot change the outcome:** the Gaussian kernels are read as SDs, and the shuffle analyses use 5% steps.

**Missing from the paper:** the images of the main Figures 1 to 4 are not under `paper/`. So the Figure 1C sequence scores and their significance marks, the Figure 3A values, and the Figure 4A to 4E values are not recorded. Those claims rest on direction and the named tests, without expected numbers. The main text also cites some supplementary figures one number off (S16 and S17 for what the supplement numbers S17 and S18); the file follows the supplement's own numbering.

## End of run

36 turns, 6 minutes, $2.35 at API prices, result: success.
