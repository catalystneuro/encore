# grosmark-2016 · claims · run 45713932982

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/grosmark-2016/; wc -l paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
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
 "file_path": "paper/10.1126-science.aad1935.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.aad1935.txt",
 "offset": 934
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/grosmark-2016/000044.yaml claims/grosmark-2016/crcns-hc-11.yaml; cat papers/datasets/grosmark-2016.yaml
```

```
<persisted-output>
Output too large (71.3KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/4abcaa14-1ccc-47cc-bb3a-8805f8db08c9/tool-results/biz4j1n6y.txt

Preview (first 2KB):
# Claims for Grosmark & Buzsaki (2016), Science 351:1440, on dandiset 000044.
# Source: the NIH author manuscript in PubMed Central (PMC4919122), full main text and the
# legends of Figures 1 to 4. The supplementary Materials and Methods (figs. S1 to S22) could
# not be retrieved: PMC and Science serve the supplement only behind a browser check, and
# Europe PMC does not hold it. Every definition the main text does not give (place cells,
# candidate events, the shuffles, the PCC test, bursting) is a common choice fixed here, and
# each is a deviation. Neither the paper nor the dandiset links analysis code.
#
# When these criteria were written, the author had seen the data check only: the file list
# and the full HDF5 listing of one file, and for every file the counts of units by cell type
# and hemisphere, the epochs, the totals of the sleep-state intervals, the ranges of the
# positions, the shape of the LFP and the difference between versions. No claim's analysis
# had been run.
#
# Method choices fixed here, for all claims:
# - Pyramidal cells are units with cell_type "excitatory".
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims/grosmark-2016; grep -nE "^  - id:|^- id:|statement:" 000044.yaml | head -80; echo ----; grep -nE "^  - id:|^- id:|statement:" crcns-hc-11.yaml | head -80; cat ../../papers/datasets/grosmark-2016.yaml
```

```
56:- id: sessions-and-tracks
57:  statement: Recordings were made in four rats, in eight novel exploration sessions, each a
66:- id: place-cell-count
67:  statement: The Bayesian decoder was built from 491 place cells over the eight sessions.
77:- id: fig1c-post-gt-pre
78:  statement: Sequence scores (rZ) of candidate events are higher in POST sleep than in PRE
90:- id: fig1c-maze-gt-pre
91:  statement: Sequence content is higher in MAZE immobility events than in PRE sleep events.
98:- id: fig2b-strong-contributors
99:  statement: 216 neurons showed significant PCC scores in PRE or POST and were considered to
112:- id: fig2-pre-post-overlap
113:  statement: Most neurons strongly contributing to PRE sequences (73%) also contributed to POST
127:- id: fig2d-shuffle-high-dpcc
128:  statement: The PRE to POST increase in sequence score is eliminated when the place fields
142:- id: fig2e-remove-plastic
143:  statement: The PRE to POST increase in sequence content is attributable to a small number of
155:- id: figs2-track-distribution
156:  statement: Rigid and plastic neurons were similarly distributed along the track.
165:- id: fig3a-plastic-specificity
166:  statement: Plastic neurons had higher place-specific indices and fewer place fields than
[... 93 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/grosmark-2016/crcns-hc-11.yaml"
}
```

```
1	# Claims for Grosmark & Buzsaki (2016), Science 351:1440-1443, on CRCNS data set hc-11
2	# (doi:10.6080/K0862DC5).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-07,
4	# protocol as stated in docs/protocol.md (Reader).
5	#
6	# Text read: the NIH author manuscript in PubMed Central (PMC4919122), as supplied under paper/,
7	# with the main text and the legends of Figures 1 to 4, and its supplement (Materials and
8	# Methods, Figures S1 to S22 with legends, references; PDF from PMC, text by PyMuPDF). The
9	# images of the main Figures 1 to 4 are not under paper/, so numbers and significance marks
10	# printed only inside those panels are not recorded here. The supplement PDF was rendered to
11	# read the supplementary panels: values printed in panel titles (Figures S5, S9, S12, S13, S14,
12	# S16 to S19) are marked as read from a figure; the text extraction does not hold them, so the
13	# quote checker cannot find their p-values. The paper links no analysis code ("Spike and LFP
14	# data are available at CRCNS.org"); none was read.
15	#
16	# Main-text figure numbers for supplementary figures are off by one in places: the main text
17	# cites figs. S16 and S17 for pair-wise coactivity and temporal bias, which are Figures S17 and
18	# S18 of the supplement, and fig. S12 for the exclusion analysis that the Methods call fig. S8.
19	# The claims below cite the supplement's own numbering.
20	#
[... 909 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,80p claims/fouke-2025.yaml; grep -n "datasets:" claims/fouke-2025.yaml | head -3; grep -rn "datasets:" claims/*.yaml | head -5; sed -n 1,120p claims/grosmark-2016/000044.yaml | sed -n 30,120p
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
[... 156 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -B2 -A12 "^schema_version" claims/du-2026.yaml; sed -n 180,195p claims/du-2026.yaml; ls tools/; python tools/claims_check.py --help 2>&1 | head -20; grep -n "datasets" tools/claims_check.py | head
```

```
100-#
101-# Details the paper and code leave open are named in the criteria of the claims they affect.
102:schema_version: 2
103-paper: doi:10.64898/2026.08.04.742876
104-claims:
105-- id: synthetic-template-null
106-  statement: In the matched-seed synthetic calibration, the template-only regime (no trial signal
107-    in the neural features) gave a median context-conditional neural gain of about zero
108-    (-0.0000023, range -0.0000588 to 0.0000248 over ten seeds).
109-  source: Results 2.2, paragraph 2; Figure 2a
110-  quote: The template-only median context-conditional neural gain was -0.0000023 (range,
111-    -0.0000588 to 0.0000248; Figure 2)
112-  data: elsewhere
113-  where: Not deposited; generated by the paper's code, github.com/gwkuqgfkqe/neural-decoder-context-audit
114-    tag v1.0-jne-submission (commit b042fbe), src/neural_evidence/synthetic.py and
    tolerance.
- id: link-development-sample
  statement: The LINK development set is the nine dates with both a CO and an RD session, 18
    sessions and 6,750 usable trials from one macaque, with 375 usable trials in every analyzed
    session.
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd  curl -s https://api.dandiarchive.org/api/dandisets/000044/versions/draft/info/ | python -c "import json,sys; d=json.load(sys.stdin); m=d.get('metadata',{}); print(m.get('name')); print(m.get('description')); print(d.get('version'))" 2>&1 | head -30; sed -n 1,60p paper/hc-11.data-description.txt
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python -c "
import fitz,os
d=fitz.open('paper/10.1126-science.aad1935.supp.pdf')
print(len(d))
for p in [25,33,36,38,40,41]:
    d[p-1].get_pixmap(dpi=110).save(os.environ['TMPDIR']+f'/p{p}.png')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  which pdftoppm mutool; pip list 2>/dev/null | grep -i -E "pdf|mupdf"
```

```
(Bash completed with no output)
```

**Agent**

Status: no PDF renderer is installed, so I'm using the file reader to spot-check the supplementary panel values the earlier file took from figures.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1126-science.aad1935.supp.pdf",
 "pages": "25,33,36,38,40,41"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
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

**Agent calls Read**

```json
{
 "file_path": "claims/grosmark-2016/000044.yaml",
 "offset": 120,
 "limit": 210
}
```

```
120	  expected:
121	    quantity: fraction of PRE strongly contributing neurons also strongly contributing in POST
122	    value: 73
123	    tolerance: 7.3
124	    unit: percent
125	  criterion: The fraction is pooled over sessions. Its chance level, the fraction of all
126	    place cells that are strongly contributing in POST, is shown.
127	- id: fig2d-shuffle-high-dpcc
128	  statement: The PRE to POST increase in sequence score is eliminated when the place fields
129	    of the 10 to 20% of cells with the highest dPCC are shuffled, and remains after shuffling
130	    the bottom 75%.
131	  source: Results, paragraph 3; Figure 2D
132	  quote: Replay (POST > PRE) was eliminated after shuffling or removal of the top 10 to 20% of cells
133	    with the highest ΔPCC scores, whereas it remained after shuffling or removal of the bottom 75%
134	  depends_on:
135	  - place-cell-count
136	  criterion: Within each session the place cells are ranked by dPCC; the rate maps of the top
137	    or bottom X% (X = 10, 20, 50, 75) are circularly shifted by random amounts and PRE and POST
138	    events are decoded again. Replay is present when the mean POST rZ exceeds the mean PRE rZ
139	    with a one-sided rank-sum p < 0.05 (pooled over sessions). Reproduced when replay is absent
[... 175 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import pypdf; print(pypdf.__version__)"; python -c "import PIL; print(PIL.__version__)"; python -c "import pdfminer; print('pdfminer')"; pip download pymupdf -d $TMPDIR/x -q 2>&1 | tail -2
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pypdf; print(pypdf.__version__)
    ^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pypdf'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import PIL; print(PIL.__version__)
    ^^^^^^^^^^
ModuleNotFoundError: No module named 'PIL'
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pdfminer; print('pdfminer')
    ^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pdfminer'
```

**Agent calls Bash**

```bash
cd $TMPDIR && pip install --target $TMPDIR/pm pymupdf -q 2>&1 | tail -2; ls $TMPDIR/pm | head
```

```
_yaml
bin
fitz
flatbuffers
flatbuffers-25.12.19.dist-info
google
networkx
networkx-3.7.dist-info
numpy
numpy-2.5.5.dist-info
Shell cwd was reset to
```

**Agent calls Bash**

```bash
PYTHONPATH=$TMPDIR/pm python -c "
import fitz,os
d=fitz.open('paper/10.1126-science.aad1935.supp.pdf')
print(len(d))
for p in [17,19,25,30,33,36,38,40,41,42]:
    d[p-1].get_pixmap(dpi=130).save(os.environ['TMPDIR']+f'/p{p}.png')
"; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent**

Status: rendering works now (PyMuPDF in a temp dir). I'm checking the panel values on the supplementary figure pages.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p33.png"
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
 "file_path": "/tmp/claude-1001/p41.png"
}
```

Result: no output.

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
 "file_path": "/tmp/claude-1001/p19.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p17.png"
}
```

Result: no output.

**Agent**

Status: the supplementary panel values the earlier crcns-hc-11 file used (Figs. S5, S6, S9, S14, S16 to S19) match the rendered pages. Now I'm writing the merged claims file.

**Agent calls Write**

```json
{
 "file_path": "claims/grosmark-2016.yaml",
 "content": "# Claims for Grosmark & Buzsaki (2016), Science 351:1440-1443, doi:10.1126/science.aad1935,\n# across its two datasets, DANDI 000044 and CRCNS hc-11 (doi:10.6080/K0862DC5).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-25,\n# protocol as stated in docs/protocol.md (version pilot-19, Reader).\n#\n# Text read: the NIH author manuscript in PubMed Central (PMC4919122), as supplied under paper/\n# (main text and the legends of Figures 1 to 4), with its supplement (Materials and Methods,\n# Figures S1 to S22 with legends, references; PDF from PMC, text by PyMuPDF). This is the author\n# manuscript, not the version of record. The images of the main Figures 1 to 4 are not under\n# paper/, so numbers and significance marks printed only inside those panels are not recorded.\n# Supplementary figure pages were rendered from the supplement PDF to read values printed only in\n# panel titles (Figures S5, S6, S9, S14, S16 to S19); those values are marked as read from a\n# panel, and the quote checker cannot find their p-values in the text. The paper links no\n# analysis code (\"Spike and LFP data are available at CRCNS.org\"); none was read.\n#\n# Datasets. The DANDI 000044 and CRCNS hc-11 descriptions both name this paper and describe the\n# same eight sessions in four rats (PRE, MAZE and POST concatenated per session), with spikes,\n# LFP, EMG and accelerometer, and tracked position; the hc-11 descriptor also lists spike\n# waveforms and features. Every claim below rests on the paper's own recordings and lists both\n# folders; which of them holds a given variable (for instance the spike features of\n# figs11-cluster-quality-similar) is the author's to find.\n#\n# Ids. Claims were read before, one file per dataset (claims/grosmark-2016/000044.yaml and\n# crcns-hc-11.yaml). Where both files had the same finding under two ids, the 000044 id is kept\n# and the crcns-hc-11 id is named here, so the outcomes can be compared:\n# fig2-pre-post-overlap (crcns fig2-pre-contributors-persist), fig2d-shuffle-high-dpcc\n# (fig2d-high-dpcc-shuffle-abolishes-replay), fig2e-remove-plastic (fig2e-plastic-removal),\n# figs2-track-distribution (figs2-rigid-plastic-along-track), fig3a-plastic-specificity\n# (fig3a-plastic-more-specific), fig3b-plastic-improve (fig3b-plastic-specificity-increases),\n# fig4a-rigid-faster (fig4a-rigid-fire-faster), rate-split-medians (low-high-rate-split),\n# fig4d-slow-sequences (fig4d-slow-cells-replay), fig4e-gain-sequences\n# (fig4e-high-gain-cells-replay). The crcns claim fig1c-sequence-content is split here into\n# fig1c-above-chance (new id), fig1c-post-gt-pre and fig1c-maze-gt-pre; the crcns claim\n# fig4c-coactivation-by-rate into fig4c-pre-fast-coactivation, fig4c-slow-coactivation-increase\n# and fig4c-slow-replay. The 000044 claim fig4a-plastic-ripple-burst-coactivation is split into\n# figs14-plastic-ripple-gain, figs14-plastic-ripple-bursting and figs16ab-plastic-synchrony-increase;\n# the 000044 claim figs16-low-rate-info-gain is contained in figs16c-low-rate-coding. The method\n# choices of the 000044 file were made before the supplement was available and are replaced by\n# the supplement's methods.\n#\n# Supplementary figure numbers in the main text are off by one in places: the main text cites\n# figs. S16 and S17 for pair-wise coactivity and temporal bias, which are Figures S17 and S18 of\n# the supplement, and the Methods cite fig. S8 for the exclusion analysis that is Figure S12. The\n# claims cite the supplement's own numbering.\n#\n# Data the paper used. Four male Long-Evans rats, bilateral silicon probes in dorsal CA1 (two\n# with 8-shank BUZ64, two with 6-shank BUZ64SP), recorded at 20 kHz with neck EMG and a\n# head-mounted accelerometer; 562 well isolated pyramidal cells. Eight novelty sessions, each a\n# PRE epoch of about 4 hours of rest and sleep in the home cage in the familiar room A, a MAZE\n# epoch in a novel room on a 1.9 m wooden linear maze (4 sessions), a 2.3 m metal linear maze\n# (1 session) or a 1 m diameter wooden circular maze (3 sessions), then a POST epoch of about 4\n# hours in room A. Position from two head LEDs at 39.69 Hz. Linear mazes have 15 cm reward areas\n# at both ends (1.6 m or 2 m stem); the circular maze has a 30 cm reward area and clockwise\n# running. Place cells n = 491 (counted per running direction on linear mazes). Interneurons\n# (n = 128) appear only in Figure S11.\n#\n# Shared method, from the supplement's Materials and Methods unless stated.\n# - Offline states are quiet waking (immobility) and NREM sleep, scored from the CA1 theta/delta\n#   ratio, accelerometer and EMG as in reference 31 (Grosmark et al. 2012). No thresholds are\n#   given. Open; readings S-a, the lab's own state epochs if a dataset holds them (the paper's\n#   scoring); S-b, a scoring recomputed from the theta/delta ratio and EMG with thresholds the\n#   author states.\n# - Every PRE and POST analysis is yoked to the duration of the shorter of the two epochs of the\n#   session. Which part of the longer epoch is kept is open. Readings Y-a, the last T of PRE and\n#   the first T of POST (the parts nearest the maze); Y-b, the first T of each epoch; Y-c, T\n#   counted in offline time. T is the duration of the shorter epoch.\n# - Place fields. Spikes and occupancy in 2 cm bins, each smoothed with a 5 cm Gaussian kernel;\n#   rate is smoothed spikes over smoothed occupancy. Only running at 5 cm/s or more outside the\n#   reward areas. Circular maze linearised from the edge of the reward area, clockwise. Null,\n#   5,000 rate vectors from spikes resampled with the unsmoothed occupancy as the density. A\n#   place field is at least 5 consecutive bins above the null 99th percentile with an in-field\n#   peak of at least 1 Hz. Linear mazes are analysed separately for left and right runs. Whether\n#   \"5 cm\" is the kernel's SD or its width is not stated; SD is the standard reading and is a\n#   smoothing choice that should not change outcomes.\n# - Ripple events. All CA1 pyramidal spikes in 1 ms bins convolved with a 15 ms Gaussian (SD,\n#   the standard reading); trigger at mean + 3 SD of all 1 ms bins in NREM of PRE and POST\n#   together; event bounds where the rate returns to that NREM mean. Kept when the event holds\n#   the peak of at least one LFP-detected sharp wave-ripple, lasts 50 to 500 ms, falls in an\n#   offline state, and has at least five distinct pyramidal cells firing. The LFP ripple\n#   detector is not described beyond the 150-250 Hz band of Figure S4; its threshold is open\n#   (readings L-a, peak 150-250 Hz power above mean + 3 SD; L-b, above mean + 5 SD).\n# - Bayesian replay. Events of at least 100 ms with at least 10% of place cells or 5 (whichever\n#   is greater) firing; 20 ms non-overlapping bins; uniform-prior Poisson decoder (equations 1\n#   and 2) on all place cells' smoothed rate maps; weighted correlation r of position and time\n#   (equations 3 to 5); 1,000 circular place-field shuffles (each cell's unsmoothed map rotated\n#   by a random number of bins, then re-smoothed); rZ = (|r observed| - mean |r null|) / SD |r\n#   null| (equation 7). On linear mazes the decoding is done separately for each running\n#   direction. Whether each event is scored with both direction templates (D-a, both scores\n#   kept, as the Figure S20 legend \"we independently compared the results of each running\n#   direction to its null distribution\" suggests) or assigned to one direction by the\n#   direction decoder of equation 6 (D-b, the method the Methods give for Figure 1D) is open.\n#   Events of all sessions are pooled (Methods, Per Cell Contribution, last paragraph).\n# - Per cell contribution (PCC). For each place cell, 1,000 templates in which only that cell's\n#   map is circularly shuffled; for each event the cell fired in, PCC = (rZ observed - mean rZ\n#   cell shuffle) x number of participating place cells (equation 8, Figure S9A); rZ of a\n#   cell-shuffled template uses the event's own null mean and SD (the reading the equations\n#   imply). PRE and POST PCC are the means over the cell's PRE and POST events; dPCC = POST - PRE.\n# - Strongly contributing cells, rigid and plastic cells. A cell is strongly contributing when\n#   its per-event PCC scores are significant (p < 0.05, one-tailed) in PRE or POST. The Methods\n#   name a one-tailed rank-sum test; the Figure S19B legend names a one-tailed signed-rank test\n#   (readings P-a, signed-rank test of per-event PCC against zero; P-b, rank-sum test of the\n#   event's observed rZ against its mean cell-shuffled rZ). Within each session and running\n#   direction, strongly contributing cells at or below the 50th percentile of dPCC are rigid,\n#   those above are plastic, and with an odd count the median cell is dropped.\n# - Offline excitability measures (Figure S14 legend). Firing rate, spikes per second in\n#   offline states; within-ripple rate over concatenated ripple events; within-ripple gain,\n#   within-ripple rate over offline rate; ripple participation, the percentage of ripple events\n#   with at least one spike; burstiness, the percentage of ISIs under 6 ms (all, or within\n#   ripples); within-ripple \"on\" rate, the within-ripple rate over events with a spike.\n# - Pair-wise coactivity. Pearson correlation of 100 ms binned rates in offline states of PRE\n#   and POST, and during running above 5 cm/s on the maze; pairs on the same shank excluded.\n# - Temporal bias. CCG of half-width 150 ms in offline PRE and POST and in running on the maze;\n#   bias = (spikes with the reference after the comparison - spikes before) / all coincident\n#   spikes; pairs on one shank or with fewer than 40 coincident spikes in either condition\n#   excluded; similarity is the median Pearson r (and its p) over 1,000 random sign flips per\n#   pair applied alike to both epochs.\n# Every criterion below names the readings it rests on; the outcome is the one all its readings\n# give, and where they differ the author proceeds as docs/protocol.md says.\n#\n# Not made claims: Figure 1D (forward and reverse events; neither the text nor the legend states\n# its result); the secondary or control findings of Figures S3 (decoder validation), S5C to S5H,\n# S7 (cell-ID shuffle and \"negative preplay\"), S8 (surrogate data), S9C (forward against reverse\n# PCC), S10 (synthetic model), S15 (dPCC against excitability), S17B, S17E and S17F, S20 to S22\n# (other replay methods, shown here as variants of the claims they confirm).\nschema_version: 2\npaper: doi:10.1126/science.aad1935\nclaims:\n- id: sessions-and-tracks\n  statement: Recordings were made in four rats, in eight novel exploration sessions, each a PRE\n    rest and sleep epoch in the home cage, a MAZE epoch on one of two linear tracks or a circular\n    track in a novel room, and a POST rest and sleep epoch in the home cage.\n  source: Results, paragraph 2; Materials and Methods, Behavioral Procedures and Behavioral State\n    Scoring, paragraph 2; Figure S1\n  quote: Simultaneous recordings of well-isolated CA1 pyramidal single units were performed in four\n    rats ... exploration of one of two linear or a circular track (MAZE) ... preexperience sleep\n    (PRE) and postexperience sleep (POST) ... (eight novel exploration sessions)\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  expected:\n  - quantity: rats\n    value: 4\n    tolerance: 0\n  - quantity: novelty sessions\n    value: 8\n    tolerance: 0\n  - quantity: sessions on the 1.9 m linear maze, the 2.3 m linear maze and the circular maze\n    value: 4, 1 and 3\n    tolerance: exact\n  criterion: Counts as the Methods give them (4 rats; 4, 1 and 3 sessions on the three mazes).\n    Reproduced when the data hold 4 subjects and 8 sessions, each with PRE, MAZE and POST epochs\n    in this order, and the MAZE positions come from linear tracks in 5 sessions and a circular\n    track in 3; the track lengths are reported.\n- id: place-cell-count\n  statement: Of the 562 well isolated CA1 pyramidal cells recorded in the eight sessions, 491 had\n    place fields on the novel maze, counted separately for each running direction on the linear\n    mazes, which is 54% of pyramidal cells by running direction.\n  source: Results, paragraph 2; Materials and Methods, Animals, Surgery and Data Collection;\n    Figure S2 legend; Figure S19 legend\n  quote: constructed from the firing-rate vectors of place cells ( n = 491 cells) during track\n    running (eight novel exploration sessions) ... In total, 562 well isolated pyramidal cells\n    were included in this study ... Note that 54% of all putative pyramidal cells were\n    considered to have place fields by running direction\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  expected:\n  - quantity: place cells, per running direction\n    value: 491\n    tolerance: 49.1\n  - quantity: pyramidal cells\n    value: 562\n    tolerance: 56.2\n  - quantity: percentage of pyramidal cells with place fields, by running direction\n    value: 54\n    tolerance: 5.4\n    unit: '%'\n  criterion: Pyramidal cells as the dataset's putative cell types label them. Place fields by\n    the place-field method of the opening comment (Methods, Place Field Analysis), per running\n    direction on the linear mazes and once on the circular maze. The denominator of 54% is open;\n    readings (a) pyramidal cells times the number of running directions of their session (2 on\n    linear mazes, 1 on the circular maze); (b) the 562 pyramidal cells. Reproduced when the\n    counts are within tolerance under one reading.\n- id: fig1c-above-chance\n  statement: Ripple-event sequence scores (rZ) are above chance in each of PRE, MAZE and POST,\n    and absolute weighted correlations exceed those of the shuffled null in all three epochs.\n  source: Figure 1C legend; Figure S5B legend; Figure S6\n  quote: Note that in all three epochs, a greater degree of sequence content is observed than\n    expected by chance\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: Events, decoding and rZ by the ripple-event and Bayesian replay methods of the\n    opening comment. Tests from the Figure 1C legend (\"Sign-rank tests were used for\n    within-condition significance testing\"), a signed-rank test of rZ against zero in each\n    epoch. Reproduced when rZ is above zero in all three epochs at p < 0.05 under all readings of\n    Y, L, S and D. The time-bin-shuffle rZ of Figure S22B is shown as a variant.\n  depends_on:\n  - place-cell-count\n- id: fig1c-post-gt-pre\n  statement: Sequence scores (rZ) of ripple events are higher in POST sleep than in PRE sleep\n    (replay).\n  source: Figure 1C; Figure S5 title; Figure S6 (per animal); Results, paragraph 2\n  quote: Cumulative distribution of rZ for PRE, MAZE, and POSTevents ... Inset, mean ± SE of\n    sequence scores in each condition. *P < 0.05; **P < 0.005; ***P < 0.0005 (Kruskal-Wallis\n    test, followed by post hoc Tukey-Kramer tests)\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: Events and rZ as in fig1c-above-chance. Test from the Figure 1C legend, a\n    Kruskal-Wallis test on rZ across PRE, MAZE and POST followed by Tukey-Kramer comparisons.\n    Reproduced when mean POST rZ exceeds mean PRE rZ with Tukey-Kramer p < 0.05 under all\n    readings of Y, L, S and D. The Figure 1C panel values are not available here, so no level is\n    fixed. Figure S6 (read from the panels) shows POST above PRE in three of the four animals and\n    not in animal B; the per-animal results are reported and compared with it. The bootstrap\n    test of the POST - PRE change of |r| against the null change (Figure S5B, right) is shown.\n  depends_on:\n  - place-cell-count\n- id: fig1c-maze-gt-pre\n  statement: Sequence content is higher in MAZE immobility events than in PRE sleep events.\n  source: Figure 1C; Figure 2C legend; Figure S6 (per animal)\n  quote: the marked increase in sequence content observed in the MAZE and POSTepochs is driven by\n    the recruitment of plastic cells\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: As fig1c-post-gt-pre, with MAZE events in place of POST events. Reproduced when mean\n    MAZE rZ exceeds mean PRE rZ with Tukey-Kramer p < 0.05 under all readings. Figure S6 (read\n    from the panels) shows MAZE highest of the three epochs in each animal; MAZE against POST is\n    reported.\n  depends_on:\n  - place-cell-count\n- id: figs5e-duration-unchanged\n  statement: Ripple-event duration did not differ between PRE and POST (median 183 ms against\n    186 ms).\n  source: Figure S5E legend\n  quote: While ripple-event duration did not differ between the PRE and POST epochs (PRE median\n    duration 183ms, POST median duration 186ms, p < 0.07, Rank-Sum test)\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  statistics:\n  - test: Rank-Sum test\n    p: 0.07\n    p_relation: \"<\"\n  expected:\n  - quantity: PRE median ripple-event duration\n    value: 183\n    tolerance: 18.3\n    unit: ms\n  - quantity: POST median ripple-event duration\n    value: 186\n    tolerance: 18.6\n    unit: ms\n  criterion: A claim of absence, judged by the paper's rank-sum test of PRE against POST event\n    durations at p < 0.05. Which events are plotted is open; readings (a) all ripple events of\n    the opening comment; (b) the events used for Bayesian replay (at least 100 ms, enough place\n    cells). Reproduced when the test is not significant and both medians are within tolerance\n    under one reading; the size of the difference is reported either way.\n- id: figs5f-more-participation-post\n  statement: A greater percentage of place cells participated (fired at least one spike) in POST\n    than in PRE ripple events.\n  source: Figure S5F legend\n  quote: a significantly greater percentage of place cells participated (fired at least one spike\n    in) POST epoch events\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: Per event, the percentage of the session's place cells (per running direction\n    template under reading D-a) firing at least one spike, on the events of fig1c-above-chance.\n    The Figure S5 legend names no test for panel F; the rank-sum test it names for panel E is\n    used. Reproduced when POST exceeds PRE at p < 0.05.\n  depends_on:\n  - fig1c-above-chance\n- id: figs9b-pcc-post-higher\n  statement: Place cells contribute more to POST than to PRE sequence content (median PCC -0.011\n    in PRE, 0.183 in POST), and the median change dPCC is 0.159.\n  source: Figure S9B (values read from the panel titles)\n  quote: Note that consistent with the main Δreplay effect (Fig. 1C, POST > PRE sequence scores\n    (rZ)), cells show significantly higher POST, compared to PRE PCC scores\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  statistics:\n  - about: PRE against POST PCC, all place cells\n    test: rank-sum test\n    p: 0\n    n: 491 place cells\n  - about: dPCC against zero\n    test: signed-rank test\n    p: 0\n    n: 491 place cells\n  expected:\n  - quantity: median PRE PCC\n    value: -0.011\n    tolerance: 0.02\n  - quantity: median POST PCC\n    value: 0.183\n    tolerance: 0.0183\n  - quantity: median dPCC\n    value: 0.159\n    tolerance: 0.0159\n  criterion: PCC by the method of the opening comment (Methods, Per Cell Contribution Analysis),\n    for all place cells. Panel titles print \"p ~ 0\", recorded as 0. The tolerance on the PRE\n    median is not 10% of a value near zero; it is about 10% of the gap between the PRE and POST\n    medians (0.194). Reproduced when POST PCC exceeds PRE PCC (rank-sum p < 0.05), dPCC exceeds\n    zero (signed-rank p < 0.05), and the three medians are within tolerance, under readings Y and\n    D; partially reproduced when the tests hold but a median falls outside its tolerance.\n  depends_on:\n  - fig1c-post-gt-pre\n- id: fig2b-strong-contributors\n  statement: 216 place cells contributed significantly to PRE or POST sequence content; 97 in\n    PRE, 190 in POST, 71 in both, 26 in PRE only and 119 in POST only.\n  source: Results, paragraph 2; Figure 2B; Figure S19A (counts read from the panel)\n  quote: Neurons that showed significant PCC scores in either PRE or POST were considered to be\n    strongly contributing to sequence formation ( n = 216 neurons\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  expected:\n  - quantity: strongly contributing cells\n    value: 216\n    tolerance: 21.6\n  - quantity: cells significant in PRE\n    value: 97\n    tolerance: 9.7\n  - quantity: cells significant in POST\n    value: 190\n    tolerance: 19\n  - quantity: cells significant in both\n    value: 71\n    tolerance: 7.1\n  criterion: Counts of place cells (per running direction) with per-event PCC significant at p\n    < 0.05 one-tailed, under readings P-a and P-b of the opening comment (Methods, Rigid and\n    Plastic Cell Classification; Figure S19B legend). Reproduced when all four counts are within\n    tolerance under one reading; partially reproduced when the total is within tolerance but a\n    subset count is not.\n  depends_on:\n  - figs9b-pcc-post-higher\n- id: fig2-pre-post-overlap\n  statement: The majority (73%) of neurons strongly contributing to PRE sequences also\n    contributed to POST sequences.\n  source: Results, paragraph 2; Figure S19A\n  quote: Importantly, the majority of neurons strongly contributing to PRE (73%) also contributed\n    to POST sequences\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  expected:\n    quantity: percentage of PRE-significant cells also POST-significant\n    value: 73\n    tolerance: 7.3\n    unit: '%'\n  criterion: From the cells of fig2b-strong-contributors, the number significant in both PRE and\n    POST over the number significant in PRE (71 of 97 in Figure S19A), under readings P-a and\n    P-b. Reproduced when within tolerance under one reading. The chance level, the fraction of\n    all place cells significant in POST, is reported.\n  depends_on:\n  - fig2b-strong-contributors\n- id: rigid-plastic-counts\n  statement: Splitting strongly contributing cells at each session's median dPCC gives 105 rigid\n    and 105 plastic cells.\n  source: Materials and Methods, Rigid and Plastic Cell Classification\n  quote: the strongly contributing cells equal to or below the 50th percentile of that session’s\n    ΔPCC were considered rigid cells (n = 105 cells, blue x’s), while the strongly contributing\n    cells above the 50th percentile of that session’s ΔPCC distribution were considered plastic\n    cells (n = 105 cells\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  expected:\n  - quantity: rigid cells\n    value: 105\n    tolerance: 10.5\n  - quantity: plastic cells\n    value: 105\n    tolerance: 10.5\n  criterion: Classification as in the opening comment (per session and running direction, the\n    median cell dropped for odd counts). Reproduced when both counts are within tolerance.\n  depends_on:\n  - fig2b-strong-contributors\n- id: figs19c-pcc-change-per-cell\n  statement: Testing each place cell's per-event PCC scores between PRE and POST, 2.2% of cells\n    had significantly higher PRE than POST scores and 21.4% significantly higher POST than PRE\n    scores.\n  source: Figure S19C legend\n  quote: 2.2% of cells showed significantly greater PRE compared to POST PCC scores while 21.4%\n    showed higher POST > PRE\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  expected:\n  - quantity: percentage of place cells with PRE PCC above POST PCC\n    value: 2.2\n    tolerance: 0.22\n    unit: '%'\n  - quantity: percentage of place cells with POST PCC above PRE PCC\n    value: 21.4\n    tolerance: 2.14\n    unit: '%'\n  criterion: Per the Figure S19C legend, for each place cell (491, per running direction) two\n    one-tailed rank-sum tests of its per-event PCC scores in PRE events against those in POST\n    events, one for each direction, counted at p < 0.05 (the counting threshold of the panel);\n    the denominator is all place cells (the panel's axis, \"491 total\"). PCC as in\n    figs9b-pcc-post-higher. Reproduced when both percentages are within tolerance under readings\n    Y and D; partially reproduced when the POST > PRE percentage is within tolerance and much\n    larger than the PRE > POST one but a value falls outside tolerance.\n  depends_on:\n  - figs9b-pcc-post-higher\n- id: fig2d-shuffle-high-dpcc\n  statement: Shuffling the place fields of the 10 to 20% of cells with the highest dPCC\n    eliminates the POST over PRE increase in sequence content, while it survives shuffling of\n    the bottom 75% of cells.\n  source: Figure 2D; Results, paragraph 2\n  quote: Replay (POST > PRE) was eliminated after shuffling or removal of the top 10 to 20% of\n    cells with the highest ΔPCC scores, whereas it remained after shuffling or removal of the\n    bottom 75%\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  expected:\n    quantity: percentage of highest-dPCC cells shuffled at which POST - PRE rZ is eliminated\n    value: 15.5\n    tolerance: 6.5\n    unit: '%'\n  criterion: Per the Methods (Per Cell Contribution, last paragraph) and the Figure 2D legend,\n    within each session an increasing percentage of place cells (ranked by dPCC, from the\n    highest or from the lowest) has its maps circularly shuffled (1,000 templates), the replay\n    analysis is rerun, and mean POST rZ - mean PRE rZ is pooled over sessions, with a\n    bootstrapped 95% interval. Percentage steps are not given; 5% steps are a standard choice\n    that resolves the 10 to 20% range. What \"eliminated\" means is open; readings (a) mean POST -\n    PRE rZ at or below zero; (b) its bootstrapped 95% interval includes zero. The expected value\n    and tolerance stand for the range 10 to 20%, widened by 10% of each bound (9 to 22%).\n    Reproduced when, shuffling from the highest dPCC, replay is first eliminated between 9 and\n    22%, and, shuffling from the lowest dPCC, replay is still present at 75% (interval above\n    zero), under readings Y and D and one reading of \"eliminated\".\n  depends_on:\n  - figs9b-pcc-post-higher\n- id: figs12-high-dpcc-exclusion\n  statement: Excluding the 10 to 20% of cells with the highest dPCC turns the POST minus PRE\n    change in sequence content negative, while excluding up to about 75% of the lowest dPCC\n    cells leaves POST above PRE.\n  source: Figure S12\n  quote: Note that even after excluding up to ~75% of ‘low’ ΔPCC cells, POST epoch sequence\n    content exceeds PRE epoch sequence content ... after the exclusion of just 10 to 20% of\n    cells PRE epoch sequence content exceeded POST epoch sequence content\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: As fig2d-shuffle-high-dpcc, with cells excluded from the template and event\n    selection (the 100 ms and 10% or 5 cell criteria applied after exclusion, per the Methods,\n    Bayesian Replay Analysis) in place of shuffled. Reproduced when, excluding from the highest\n    dPCC, mean POST - PRE rZ falls below zero between 9 and 22% excluded, and, excluding from the\n    lowest, the lower bound of its bootstrapped 95% interval stays above zero up to 75%, under\n    readings Y and D.\n  depends_on:\n  - figs9b-pcc-post-higher\n- id: fig2e-remove-plastic\n  statement: The PRE to POST increase in sequence content is attributable to a small number of\n    plastic cells; removing them, unlike removing rigid cells, removes the increase.\n  source: Figure 2E legend\n  quote: Effect on sequence content of removal of rigid (black) or plastic (gray) neurons. The PRE\n    to POST increase in sequence content is attributable to only a small number of plastic cells.\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: The Figure 2E panel is not available here and its legend gives no method beyond\n    removal. Removal as in figs12-high-dpcc-exclusion (cells excluded from template and event\n    selection, the 100 ms and 10% or 5 cell criteria applied after exclusion, within each\n    session, results pooled), excluding all rigid or all plastic cells of rigid-plastic-counts;\n    mean POST rZ - mean PRE rZ with a bootstrapped 95% interval, the annotation of Figure 2D and\n    Figure S12. Reproduced when, after removing the plastic cells, the interval of POST - PRE rZ\n    reaches zero or below, and after removing the rigid cells it stays above zero, under\n    readings Y and D; partially reproduced when both stay above zero but removing plastic cells\n    lowers POST - PRE rZ more than removing rigid cells.\n  depends_on:\n  - rigid-plastic-counts\n  - fig1c-post-gt-pre\n- id: figs2-track-distribution\n  statement: Rigid and plastic cells' place fields are similarly distributed along the track,\n    both enriched near the start and goal ends.\n  source: Results, paragraph 2; Figure S2 legend\n  quote: Rigid and plastic neurons were similarly distributed along the track\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: The paper shows this only as rate maps and gives no test, so the test is open.\n    Measure, each cell's peak place-field position (per running direction) as a fraction of\n    track length from the start of the run. Readings (a) a two-sample Kolmogorov-Smirnov test of\n    rigid against plastic positions; (b) a rank-sum test of the distance of each peak from the\n    nearer track end. Reproduced when neither reading finds a difference at p < 0.05; the\n    fractions of fields in the outer fifths of the track are reported for each group.\n  depends_on:\n  - rigid-plastic-counts\n- id: fig3a-plastic-specificity\n  statement: On the novel maze plastic cells have higher place specificity than rigid cells and\n    fewer place fields.\n  source: Figure 3A; Results, paragraph 3; Figure S19E\n  quote: Plastic neurons had higher place-specific indices and fewer place fields compared with\n    rigid cells\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: The Figure 3A panels are not available here; Figure S19E, which its legend says to\n    compare to Figure 3A, shows six measures, within/outside place-field rate ratio, information\n    per spike, information per second, spatial coherence, place-field stability and number of\n    place fields, and marks every one as significant, plastic higher on the first five and\n    lower on the number of fields. Measures as in reference 32 (Mizuseki et al. 2012) per the\n    Methods (Place Field Analysis); the stability split is not given here (readings (a) first\n    against second half of the maze epoch; (b) odd against even laps). Rank-sum test, rigid\n    against plastic (Figure 3A legend). Reproduced when plastic cells are higher on all five\n    specificity measures and have fewer place fields, each at p < 0.05, under one stability\n    reading; partially reproduced when the direction holds for all six but fewer reach p < 0.05.\n  depends_on:\n  - rigid-plastic-counts\n- id: fig3b-plastic-improve\n  statement: Plastic but not rigid cells steadily increased their spatial specificity during maze\n    running.\n  source: Figure 3B; Results, paragraph 3; Figure S13C; Figure S19F\n  quote: plastic but not rigid neurons increased their spatial specificity steadily during\n    learning\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: Per lap, each cell's percentage of spikes inside its place field(s) (the measure of\n    Figure S19F, the legend's \"infield versus outside field firing ratio\"), using only laps\n    with at least 5 spikes from the cell (Figure S13 legend); per cell, the Pearson\n    correlation of this value with lap number. Tests per the Figure S13C legend, a signed-rank\n    test of each group's correlations against zero and a rank-sum test between groups.\n    Reproduced when plastic cells' correlations are above zero (p < 0.05), rigid cells' are not,\n    and plastic exceeds rigid (p < 0.05). The within-field rate gain of Figure S13C is shown as\n    a variant.\n  depends_on:\n  - rigid-plastic-counts\n- id: figs13-outfield-rate-falls\n  statement: Neither group's overall firing rate changed significantly over laps, and neither\n    group's within-field firing rate increased significantly; plastic cells' increase in\n    specificity came from a fall in their out-of-field firing rate, which rigid cells did not\n    show.\n  source: Figure S13A, S13D and S13E\n  quote: Notably, neither cell group showed a significant increase in within-field firing rate\n    over the course of maze running. (E) Conversely, a significant decrease was observed in\n    plastic cells’, but not rigid cells’, outside of field firing rates\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: Per cell, the Pearson correlation of lap rate (overall, within field, outside field)\n    with lap number, laps with at least 5 spikes, running above 5 cm/s (Figure S13 legend).\n    Signed-rank test of each group's correlations against zero (Figure S13C legend). Reproduced\n    when the outside-field correlations of plastic cells are below zero (p < 0.05) and those of\n    rigid cells are not, neither group's overall-rate correlations differ from zero at p < 0.05,\n    and neither group's within-field correlations are above zero at p < 0.05.\n  depends_on:\n  - rigid-plastic-counts\n- id: fig4a-rigid-faster\n  statement: Rigid cells fire faster than plastic cells in offline states (session-wide median\n    0.76 against 0.54 Hz; PRE 0.762 against 0.479 Hz; POST 0.753 against 0.472 Hz), but not\n    during maze running (1.09 against 1.13 Hz).\n  source: Figure 4A; Results, paragraph 4; Figure S14, firing rate row (values read from the\n    panel titles)\n  quote: Session-wide firing rates of rigid neurons were significantly higher compared with\n    plastic neurons\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  statistics:\n  - about: session-wide\n    test: rank-sum test\n    p: 0.001\n    p_relation: \"<\"\n    n: 105 rigid and 105 plastic cells\n  - about: PRE\n    test: rank-sum test\n    p: 0.00159\n    p_relation: \"<\"\n  - about: POST\n    test: rank-sum test\n    p: 0.00146\n    p_relation: \"<\"\n  - about: MAZE\n    test: rank-sum test\n    p: 0.976\n    p_relation: \"<\"\n  expected:\n  - quantity: session-wide median rate, rigid\n    value: 0.76\n    tolerance: 0.076\n    unit: Hz\n  - quantity: session-wide median rate, plastic\n    value: 0.54\n    tolerance: 0.054\n    unit: Hz\n  - quantity: PRE median rate, rigid\n    value: 0.762\n    tolerance: 0.0762\n    unit: Hz\n  - quantity: PRE median rate, plastic\n    value: 0.479\n    tolerance: 0.0479\n    unit: Hz\n  - quantity: POST median rate, rigid\n    value: 0.753\n    tolerance: 0.0753\n    unit: Hz\n  - quantity: POST median rate, plastic\n    value: 0.472\n    tolerance: 0.0472\n    unit: Hz\n  criterion: Firing rate as in Figure S14, spikes per second in offline states of each epoch,\n    and on the maze for MAZE (the measure for MAZE is not stated; readings (a) all MAZE time;\n    (b) running above 5 cm/s). \"Session-wide\" is not defined; readings (a) offline time of PRE,\n    MAZE and POST together; (b) offline time of PRE and POST; (c) the whole recording. Rank-sum\n    tests. Reproduced when the session-wide, PRE and POST differences are significant (p <\n    0.05) with rigid higher, the MAZE difference is not (rank-sum p >= 0.05), and the medians\n    are within tolerance under one reading; partially reproduced when the tests hold and the\n    medians do not. The Figure S14 colour key labels rigid cells red and plastic cells blue,\n    the reverse of its legend text; the legend text is followed.\n  depends_on:\n  - rigid-plastic-counts\n- id: figs14-plastic-ripple-gain\n  statement: Plastic cells have a higher within-ripple firing rate gain than rigid cells (POST\n    median 5.75 against 4.52) and a larger PRE to POST increase in gain (0.81 against 0.14).\n  source: Figure 4A; Results, paragraph 4; Figure S14, within-ripple firing rate gain row\n    (values read from the panel titles)\n  quote: Ripple-related spiking, bursting, and pair-wise coactivation were higher in plastic\n    versus rigid neurons\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  statistics:\n  - about: POST gain\n    test: rank-sum test\n    p: 0.0001\n    p_relation: \"<\"\n  - about: session-wide gain\n    test: rank-sum test\n    p: 0.002\n    p_relation: \"<\"\n  - about: PRE gain\n    test: rank-sum test\n    p: 0.04\n    p_relation: \"<\"\n  - about: POST - PRE change in gain\n    test: rank-sum test\n    p: 0.00306\n    p_relation: \"<\"\n  expected:\n  - quantity: POST median gain, plastic\n    value: 5.75\n    tolerance: 0.575\n  - quantity: POST median gain, rigid\n    value: 4.52\n    tolerance: 0.452\n  - quantity: median change in gain, plastic\n    value: 0.81\n    tolerance: 0.081\n  - quantity: median change in gain, rigid\n    value: 0.14\n    tolerance: 0.1\n  criterion: Gain as in the Figure S14 legend, within-ripple rate over offline rate, per epoch.\n    Rank-sum tests, plastic against rigid. The rigid change median is near zero, so its\n    tolerance is set at 0.1, about 10% of the gap between the two groups' changes. Reproduced\n    when plastic exceeds rigid for POST gain and for the change at p < 0.05 and the four medians\n    are within tolerance; partially reproduced when the tests hold and a median does not.\n  depends_on:\n  - rigid-plastic-counts\n- id: figs14-plastic-ripple-bursting\n  statement: Plastic cells burst more within ripples than rigid cells in POST (median 27.3%\n    against 23.3% of ISIs under 6 ms) and increase their within-ripple bursting more from PRE\n    to POST (2.81 against 1.13 percentage points).\n  source: Figure S14, within-ripple burstiness row (values read from the panel titles)\n  inferred: The main text states that ripple-related bursting was higher in plastic cells (Figure\n    4A); the numbers are only in the Figure S14 panel titles.\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  statistics:\n  - about: POST within-ripple burstiness\n    test: rank-sum test\n    p: 0.00183\n    p_relation: \"<\"\n  - about: POST - PRE change\n    test: rank-sum test\n    p: 0.01\n    p_relation: \"<\"\n  expected:\n  - quantity: POST median within-ripple burstiness, plastic\n    value: 27.3\n    tolerance: 2.73\n    unit: '%'\n  - quantity: POST median within-ripple burstiness, rigid\n    value: 23.3\n    tolerance: 2.33\n    unit: '%'\n  - quantity: median change, plastic\n    value: 2.81\n    tolerance: 0.281\n    unit: percentage points\n  - quantity: median change, rigid\n    value: 1.13\n    tolerance: 0.113\n    unit: percentage points\n  criterion: Within-ripple burstiness as the percentage of within-ripple ISIs under 6 ms (Figure\n    S14 legend). Whether ISIs spanning two ripple events count is open; readings (a) ISIs\n    between spikes of one event; (b) all ISIs inside concatenated ripple time. Rank-sum tests.\n    Reproduced when both tests hold with plastic higher and the medians are within tolerance\n    under one reading; partially reproduced when the tests hold and a median does not.\n  depends_on:\n  - rigid-plastic-counts\n- id: figs16ab-plastic-synchrony-increase\n  statement: The PRE to POST increase in ripple-triggered firing is present in plastic but not\n    rigid cells, and the PRE to POST increase in pair-wise coactivity is larger among plastic\n    cells.\n  source: Figure S16A and S16B; Figure 4A and Figure S19G (change in pair-wise coactivity)\n  quote: The PRE to POST increases in ripple-event triggered firing rates seen when all place\n    cells are taken into account (A, left panel) are uniquely present in plastic (A,\n    third-panel) but not rigid (A, second panel) cells ... the PRE to POST increase in pair-wise\n    co-activity observed across all place cells (B, left panel) is more robustly observed in the\n    plastic cell population\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: Ripple-triggered rate from -50 to 100 ms around event onset (the panel's axis), per\n    cell, PRE and POST. The legend gives no test for panel A; readings (a) a signed-rank test of\n    each cell's POST - PRE mean rate in 0 to 100 ms; (b) the same at the peak bin. Coactivity\n    as in the opening comment. Figure S16B shows a significant PRE to POST increase within both\n    rigid and plastic pairs, larger in plastic pairs, with no test between groups; Figure 4A\n    (and Figure S19G, which shows it with p < 0.023) compares the per-cell POST - PRE change\n    in pair-wise coactivity between rigid and plastic cells by rank-sum test. How a cell's\n    change is formed from its pairs is not stated; readings (c) the mean change over the\n    cell's pairs with all other place cells on other shanks; (d) the mean over its pairs\n    within its own group. Reproduced when plastic cells' rate increase is significant (p <\n    0.05) and rigid cells' is not under one reading of A, and plastic cells' coactivity change\n    exceeds rigid cells' (rank-sum, p < 0.05) under one reading of the per-cell change.\n  depends_on:\n  - rigid-plastic-counts\n- id: figs11-cluster-quality-similar\n  statement: Rigid and plastic cells have similar waveforms and similar cluster quality and\n    stability across PRE, MAZE and POST, so clustering errors do not explain their differences.\n  source: Figure S11; Results, paragraph 3\n  quote: Note\n    that rigid and plastic cell waveforms are similar to each other and stable from the PRE to\n    the POST epochs\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: A claim of absence, judged by the paper's rank-sum tests of rigid against plastic\n    cells at p < 0.05 (Figure S11 legend). Quality is the median Mahalanobis distance of each\n    spike's PCA features to its cluster mean, for spikes in PRE ripple events, MAZE running and\n    POST ripple events; stability is the symmetric Mahalanobis distance between a cell's\n    clusters in two conditions; first spikes of bursts (ISI under 6 ms) only. Reproduced when no\n    comparison is significant; the effect sizes are reported either way. Needs the spike\n    features used in clustering.\n  depends_on:\n  - rigid-plastic-counts\n- id: rate-split-medians\n  statement: Splitting place cells into equal halves by offline firing rate gives low-rate cells\n    with median 0.39 Hz and high-rate cells with median 1.12 Hz.\n  source: Results, paragraph 5; Figure S16C\n  quote: we divided place cells into equal subgroups by either “off-line” sleep-firing rate or\n    ripple-rate gain ... Low-rate neurons (median, 0.39 Hz) ... than high-rate cells (median, 1.12\n    Hz)\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  expected:\n  - quantity: median rate, low-rate cells\n    value: 0.39\n    tolerance: 0.039\n    unit: Hz\n  - quantity: median rate, high-rate cells\n    value: 1.12\n    tolerance: 0.112\n    unit: Hz\n  criterion: The Figure S16 legend points to the Methods for the split, which the Methods do not\n    give; Figure S16C labels the groups below and above the 50th percentile. From the text,\n    place cells are split into equal groups by \"off-line\" sleep firing rate, and the Methods\n    state that cells removed from an analysis are chosen within each session. Readings (a)\n    median split within each session and running direction; (b) median split within each\n    session; (c) a pooled median split; and for the rate, (i) offline PRE and POST together;\n    (ii) offline PRE only. Reproduced when both medians are within tolerance under one reading.\n    The reading(s) that match fix the split for the claims that depend on this one.\n  depends_on:\n  - place-cell-count\n- id: figs16c-low-rate-coding\n  statement: Low-rate cells carry more spatial information per spike (0.91 against 0.56\n    bits/spike), have a higher in/out place-field rate ratio (6.38 against 3.86), fewer place\n    fields (log-mean 1.29 against 1.59), and a larger PRE to POST increase in within-ripple gain\n    (0.71 against 0.06) than high-rate cells.\n  source: Figure S16C legend; Results, paragraph 5\n  quote: low-rate cells also contributed more information per spike (Low Rate median ... 0.91\n    bits/spike, High Rate med ... 0.56 bits/spike, p < 2.5x10-9, Rank-Sum test), had a greater\n    within/outside of place field(s) firing ratio (Low Rate med ... 6.38, High Rate med ... 3.86,\n    p < 7.9x10-14), and had fewer place fields on the maze (Low Rate log-mean ... 1.29, High Rate\n    log-mean ... 1.59, p < 3.94 x10-06). In addition, low rate cells tended to show a more\n    pronounced increase in their within-ripple firing rate gain (Low Rate Δripple-gain med ...\n    0.71, High Rate med ... 0.06, p < 7.585x10-4\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  statistics:\n  - about: information per spike\n    test: Rank-Sum test\n    p: 2.5e-09\n    p_relation: \"<\"\n  - about: within/outside field rate ratio\n    test: Rank-Sum test\n    p: 7.9e-14\n    p_relation: \"<\"\n  - about: number of place fields\n    test: Rank-Sum test\n    p: 3.94e-06\n    p_relation: \"<\"\n  - about: change in within-ripple gain\n    test: Rank-Sum test\n    p: 0.0007585\n    p_relation: \"<\"\n  expected:\n  - quantity: median information per spike, low-rate\n    value: 0.91\n    tolerance: 0.091\n    unit: bits/spike\n  - quantity: median information per spike, high-rate\n    value: 0.56\n    tolerance: 0.056\n    unit: bits/spike\n  - quantity: median in/out field ratio, low-rate\n    value: 6.38\n    tolerance: 0.638\n  - quantity: median in/out field ratio, high-rate\n    value: 3.86\n    tolerance: 0.386\n  - quantity: log-mean number of place fields, low-rate\n    value: 1.29\n    tolerance: 0.129\n  - quantity: log-mean number of place fields, high-rate\n    value: 1.59\n    tolerance: 0.159\n  - quantity: median change in within-ripple gain, low-rate\n    value: 0.71\n    tolerance: 0.071\n  - quantity: median change in within-ripple gain, high-rate\n    value: 0.06\n    tolerance: 0.07\n  criterion: Groups from rate-split-medians under the reading that matched there. Measures as in\n    fig3a-plastic-specificity and figs14-plastic-ripple-gain. \"Log-mean\" is read as the\n    geometric mean, as the Figure S14 legend uses it for bar graphs in log scale. The high-rate\n    gain change is near zero, so its tolerance is 0.07, about 10% of the gap between the groups.\n    Reproduced when all four rank-sum tests give p < 0.05 in the stated direction and the\n    medians are within tolerance; partially reproduced when the tests hold and a median does\n    not.\n  depends_on:\n  - rate-split-medians\n- id: fig4c-pre-fast-coactivation\n  statement: In PRE sleep, pair-wise coactivation was dominated by fast-firing neurons, and\n    their correlations stayed unchanged into POST sleep.\n  source: Figure 4B and 4C legends; Results, paragraph 4\n  quote: In PRE sleep, coactivity was dominated by fast-firing neurons, and these correlations\n    remained unchanged into POST sleep\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: Per the Figure 4B and 4C legends, place cells sorted by session firing rate and\n    grouped in overlapping windows of 20% of cells stepped by 1%; in each window, the mean\n    coactivity of its pairs (different shanks) in PRE and in POST. Whether ranks are taken\n    within session or pooled is open (readings (a) percentile of rate within session, curves\n    averaged over sessions; (b) pooled); \"session firing rate\" as in fig4a-rigid-faster. The\n    legends name no test; the Spearman and signed-rank tests here are standard choices, not\n    the paper's. Reproduced when PRE coactivity rises with the window's rate rank (Spearman over\n    windows, p < 0.05; the windows overlap, so the p-value is indicative) and the POST - PRE\n    change in the fastest window is not significant (signed-rank over its pairs, p >= 0.05),\n    under both readings; partially reproduced when the PRE dominance holds and the stability\n    does not.\n  depends_on:\n  - place-cell-count\n- id: fig4c-slow-coactivation-increase\n  statement: Slow-firing neurons showed the strongest increases in coactivation from PRE to POST\n    sleep.\n  source: Figure 4C legend; Results, paragraph 4; Figure S16C\n  quote: In contrast, slow-firing neurons showed the strongest increases in coactivation from PRE\n    to POST sleep\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: Windows as in fig4c-pre-fast-coactivation, on the POST - PRE change of mean\n    coactivity. Reproduced when the change falls with the window's rate rank (Spearman over\n    windows, p < 0.05, a standard choice) and, per Figure S16C, the low-rate half's mean change\n    exceeds the high-rate half's (rank-sum over pairs, p < 0.05; Figure S16C marks it ***), under\n    both readings of the ranking.\n  depends_on:\n  - place-cell-count\n  - rate-split-medians\n- id: fig4c-slow-replay\n  statement: Slow-firing cells showed the greatest replay, measured as the partial correlation\n    between RUN and POST coactivation accounting for PRE.\n  source: Figure 4C legend\n  quote: Moreover, it was the slow-firing cells that showed the greatest replay (partial\n    correlation across coactivation values between RUN and POST, accounting for PRE)\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: Windows as in fig4c-pre-fast-coactivation; in each window, the partial correlation\n    across its pairs between MAZE running and POST coactivation given PRE coactivation (RUN\n    coactivity during running above 5 cm/s, Methods, Pair-Wise Co-Activity Analysis).\n    Reproduced when the partial correlation falls with the window's rate rank (Spearman over\n    windows, p < 0.05, a standard choice) and is largest in the slowest windows, under both\n    readings of the ranking.\n  depends_on:\n  - place-cell-count\n- id: fig4d-slow-sequences\n  statement: Slow-firing, but not fast-firing, place cells increased their contribution to\n    sequences from PRE to POST sleep.\n  source: Figure 4D; Results, paragraph 5; Figures S20D, S21B and S22E\n  quote: Slow-firing, but not fast-firing, neurons increased their contribution to neuronal\n    sequences from PRE to POST sleep\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: The Bayesian replay analysis rerun with templates of only the low-rate or only the\n    high-rate place cells (rate-split-medians), the event criteria applied to the kept cells\n    (Methods, Bayesian Replay Analysis). The test of the change is open; readings (a) a rank-sum\n    test of POST against PRE rZ within each group (as in Figure 1D); (b) a bootstrapped 95%\n    interval of mean POST - PRE rZ (the Figure 2D annotation, which the Figure 4 legend refers\n    to). Reproduced when the low-rate group's POST - PRE rZ is above zero (p < 0.05) and the\n    high-rate group's is not, under each reading; partially reproduced when the low-rate\n    increase holds and the high-rate group also increases but less. The paired-latency (Figure\n    S20D), burst-decimated (Figure S21B) and time-bin-shuffle (Figure S22E) versions are shown\n    as variants.\n  depends_on:\n  - rate-split-medians\n  - fig1c-post-gt-pre\n- id: fig4e-gain-sequences\n  statement: The PRE to POST increase in sequence content was limited to cells with high\n    ripple-specific recruitment (within-ripple rate gain).\n  source: Figure 4E; Results, paragraph 5; Figures S20E, S21C and S22E\n  quote: Conversely, PRE to POST increases in sequence content were limited to cells that showed a\n    high degree of ripple-specific recruitment (gain)\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: As fig4d-slow-sequences, with the place cells split into equal halves by\n    within-ripple firing-rate gain (Figure S14 legend), under the split and epoch readings that\n    matched in rate-split-medians. Reproduced when the high-gain group's POST - PRE rZ is above\n    zero (p < 0.05) and the low-gain group's is not, under each reading of the test.\n  depends_on:\n  - rate-split-medians\n  - fig1c-post-gt-pre\n- id: figs16de-more-ripples-post\n  statement: Ripple events occur more often in POST than in PRE (median inter-event interval 2.47\n    s against 3 s), as do purely LFP-detected sharp wave-ripples (1.06 s against 1.21 s).\n  source: Figure S16D and S16E (medians read from the panel titles)\n  quote: Increased synchrony (B) in the\n    POST compared to PRE epoch may be attributable to both increases in ripple-triggered\n    spiking (A) as well as to an increase in the incidence of ripple events\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  statistics:\n  - about: inter ripple-event intervals, PRE against POST\n    test: Rank-Sum test\n    p: 0\n  - about: inter LFP-SWR intervals, PRE against POST\n    test: Rank-Sum test\n    p: 0\n  expected:\n  - quantity: median inter ripple-event interval, PRE\n    value: 3\n    tolerance: 0.3\n    unit: s\n  - quantity: median inter ripple-event interval, POST\n    value: 2.47\n    tolerance: 0.247\n    unit: s\n  - quantity: median inter LFP-SWR interval, PRE\n    value: 1.21\n    tolerance: 0.121\n    unit: s\n  - quantity: median inter LFP-SWR interval, POST\n    value: 1.06\n    tolerance: 0.106\n    unit: s\n  criterion: Intervals between consecutive events within offline states, intervals under 60 s\n    only (legend); rank-sum test of PRE against POST intervals (\"p ~ 0\" printed, recorded as 0).\n    Ripple events as in the opening comment; LFP-SWR events under readings L-a and L-b.\n    Reproduced when POST intervals are shorter for both event types at p < 0.05 and the\n    ripple-event medians are within tolerance; the LFP-SWR medians depend on the open detector\n    and are reported, and matching under one L reading counts toward reproduced.\n- id: figs17-coactivity-preservation\n  statement: Pair-wise coactivity is weakly preserved from PRE to RUN (r = 0.045), more strongly\n    from RUN to POST (r = 0.16), and most strongly from PRE to POST (r = 0.34).\n  source: Figure S17A and S17C (r values read from the panels)\n  quote: the\n    similarity between RUN and POST co-activity patterns (middle panel) was significantly ...\n    greater (corr(RUN, POST) - corr(RUN, PRE) = 0.11, p ≈ 0, Fisher's Z-test). However, the\n    similarity between RUN and POST was likewise far exceeded by the similarity between\n    PRE and POST co-activity patterns (corr(PRE, POST) - corr(RUN, POST) = 0.18, p ≈ 0,\n    Fisher's Z-test)\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  statistics:\n  - about: corr(RUN, POST) - corr(RUN, PRE)\n    test: Fisher's Z-test\n    p: 0\n  - about: corr(PRE, POST) - corr(RUN, POST)\n    test: Fisher's Z-test\n    p: 0\n  expected:\n  - quantity: Pearson r, PRE against RUN coactivity\n    value: 0.045\n    tolerance: 0.0045\n  - quantity: Pearson r, POST against RUN coactivity\n    value: 0.16\n    tolerance: 0.016\n  - quantity: Pearson r, PRE against POST coactivity\n    value: 0.34\n    tolerance: 0.034\n  - quantity: corr(RUN, POST) - corr(RUN, PRE)\n    value: 0.11\n    tolerance: 0.011\n  - quantity: corr(PRE, POST) - corr(RUN, POST)\n    value: 0.18\n    tolerance: 0.018\n  criterion: Coactivity as in the opening comment, all place-cell pairs on different shanks;\n    Pearson correlation across pairs between epochs; differences of correlations by Fisher's Z\n    test. Which form is open; readings (a) two independent correlations, the test's usual form;\n    (b) a test for dependent correlations sharing one variable. Reproduced when both differences\n    are significant (p < 0.05) in the stated direction under one reading and the values are\n    within tolerance; partially reproduced when the order RUN-PRE < RUN-POST < PRE-POST holds\n    but values fall outside tolerance.\n- id: figs17d-rigid-plastic-coactivity\n  statement: Rigid cell pairs preserve PRE coactivity into RUN (r = 0.139) and into POST (r =\n    0.31) more than plastic pairs (-0.02 and 0.09), while plastic pairs show higher RUN to POST\n    preservation (0.36 against 0.11).\n  source: Figure S17D (r values read from the panels); Results, paragraph 4\n  quote: Rigid cell, but not plastic cell, pairs\n    showed preservation of PRE co-activity patterns during the RUN. Conversely, plastic cell\n    pairs showed a significantly higher preservation of co-activity patterns from the RUN to\n    the POST\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  expected:\n  - quantity: rigid pairs, PRE against RUN r\n    value: 0.139\n    tolerance: 0.0139\n  - quantity: plastic pairs, PRE against RUN r\n    value: -0.02\n    tolerance: 0.05\n  - quantity: rigid pairs, RUN against POST r\n    value: 0.11\n    tolerance: 0.011\n  - quantity: plastic pairs, RUN against POST r\n    value: 0.36\n    tolerance: 0.036\n  - quantity: rigid pairs, PRE against POST r\n    value: 0.31\n    tolerance: 0.031\n  - quantity: plastic pairs, PRE against POST r\n    value: 0.09\n    tolerance: 0.009\n  criterion: As figs17-coactivity-preservation within rigid-rigid and plastic-plastic pairs;\n    groups compared by Fisher's Z test (Figure S17D legend), as independent correlations. The\n    plastic PRE-RUN r is near zero, so its tolerance is 0.05, read as consistent with zero.\n    Reproduced when the three group differences are significant (p < 0.05) in the stated\n    direction; the r values are reported against tolerance, and a mismatch in values with the\n    differences holding is partially reproduced.\n  depends_on:\n  - rigid-plastic-counts\n- id: figs18-temporal-bias\n  statement: Pair-wise temporal biases are not preserved from PRE to RUN (r = -0.009) but are\n    preserved from RUN to POST (r = 0.117) and PRE to POST (r = 0.201); the PRE to POST\n    preservation is carried by rigid cell pairs (r = 0.29) and the RUN to POST preservation by\n    plastic cell pairs (r = 0.26).\n  source: Figure S18B and S18C (r values read from the panels); Results, paragraph 4\n  quote: When\n    all place cells are included in the analysis, no similarity is observed between PRE and\n    RUN (left panel) temporal biases. However, temporal biases are strongly preserved from\n    the RUN to POST epochs (middle panel), as well as from the PRE to POST epochs\n    (right). (C) Limiting this analysis to rigid (blue) or plastic (red) cell pairs, reveals that the\n    preservation of temporal spiking patterns from PRE to POST and from RUN to POST is\n    attributable to the rigid and plastic cell subpopulations, respectively\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  expected:\n  - quantity: all pairs, PRE against RUN r\n    value: -0.009\n    tolerance: 0.05\n  - quantity: all pairs, RUN against POST r\n    value: 0.117\n    tolerance: 0.0117\n  - quantity: all pairs, PRE against POST r\n    value: 0.201\n    tolerance: 0.0201\n  - quantity: rigid pairs, PRE against POST r\n    value: 0.29\n    tolerance: 0.029\n  - quantity: plastic pairs, RUN against POST r\n    value: 0.26\n    tolerance: 0.026\n  criterion: Temporal bias and its median r over 1,000 sign randomisations as in the opening\n    comment (Methods, Pair-Wise Temporal Interaction Analysis). The PRE-RUN value is near zero;\n    its tolerance of 0.05 reads it as consistent with zero. Reproduced when the PRE-RUN r is not\n    significant (p >= 0.05), RUN-POST and PRE-POST are (p < 0.05), the rigid PRE-POST and\n    plastic RUN-POST r are significant while the plastic PRE-POST (-0.037) and rigid RUN-POST\n    (0.024) are not, and the values are within tolerance; partially reproduced when the\n    significance pattern holds and a value does not.\n  depends_on:\n  - rigid-plastic-counts\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/grosmark-2016.yaml",
 "old_string": "  - quantity: novelty sessions\n    value: 8\n    tolerance: 0\n  - quantity: sessions on the 1.9 m linear maze, the 2.3 m linear maze and the circular maze\n    value: 4, 1 and 3\n    tolerance: exact\n  criterion:",
 "new_string": "  - quantity: novelty sessions\n    value: 8\n    tolerance: 0\n  criterion:"
}
```

```
The file claims/grosmark-2016.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/grosmark-2016.yaml",
 "old_string": "  statement: Ripple-event sequence scores (rZ) are above chance in each of PRE, MAZE and POST,\n    and absolute weighted correlations exceed those of the shuffled null in all three epochs.\n  source: Figure 1C legend; Figure S5B legend; Figure S6\n  quote: Note that in all three epochs, a greater degree of sequence content is observed than\n    expected by chance\n  datasets:",
 "new_string": "  statement: Ripple-event sequence scores (rZ) are above chance in each of PRE, MAZE and POST.\n  source: Figure 1C legend; Figure S6 (per animal)\n  quote: Cumulative distribution of rZ for PRE, MAZE, and POSTevents, and 95% confidence\n    intervals ... Sign-rank tests were used for within-condition significance testing\n  datasets:"
}
```

```
The file claims/grosmark-2016.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/grosmark-2016.yaml",
 "old_string": "    reported.\n  depends_on:\n  - place-cell-count\n- id: figs5e-duration-unchanged",
 "new_string": "    reported.\n  depends_on:\n  - place-cell-count\n- id: figs5b-abs-r-above-null\n  statement: Absolute weighted correlations of ripple events exceed those of the shuffled null\n    in PRE, MAZE and POST, and the POST minus PRE increase is larger in the observed than in the\n    null data.\n  source: Figure S5B\n  quote: Note that in all three epochs, a greater degree of sequence content is observed than\n    expected by chance\n  datasets:\n  - \"000044\"\n  - crcns-hc-11\n  criterion: Events and shuffles as in fig1c-above-chance. Per the Figure S5B legend, observed\n    against null |r| within each epoch by rank-sum test, and the POST - PRE change of mean |r|\n    tested by bootstrap. How the bootstrap compares the observed and null changes is not\n    stated; readings (a) the bootstrap 95% interval of the observed minus null change lies above\n    zero; (b) the observed change lies above the 95th percentile of bootstrapped null changes.\n    Reproduced when observed |r| exceeds null |r| in all three epochs at p < 0.05 and the\n    observed POST - PRE change exceeds the null change under one bootstrap reading, under the\n    readings of fig1c-above-chance.\n  depends_on:\n  - fig1c-above-chance\n- id: figs5e-duration-unchanged"
}
```

```
The file claims/grosmark-2016.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Also update the opening comment's id note for figs5b, then run the checker.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/grosmark-2016.yaml",
 "old_string": "# fig1c-above-chance (new id), fig1c-post-gt-pre and fig1c-maze-gt-pre; the crcns claim",
 "new_string": "# fig1c-above-chance (new id, rZ only; |r| against the null stays in figs5b-abs-r-above-null),\n# fig1c-post-gt-pre and fig1c-maze-gt-pre; the crcns claim"
}
```

```
The file claims/grosmark-2016.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/grosmark-2016.yaml paper/10.1126-science.aad1935.txt; echo EXIT $?; grep -n -i -E "rather|—" claims/grosmark-2016.yaml
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/grosmark-2016.yaml`. All quotes pass the checker; it still exits with 9 problems, all numbers printed only in supplementary figures, which I confirmed by reading the rendered pages.

**Text read:** the NIH author manuscript in PubMed Central (PMC4919122), not the version of record: the main text, the Figure 1–4 legends, and the full supplement (Methods, Figs. S1–S22 with legends). The paper links no analysis code; it only says the data are on CRCNS.org. Both datasets' archive descriptions describe the same eight sessions in four rats, so every claim lists both `000044` and `crcns-hc-11`.

**Claims:** 36. 35 have quotes; one (`figs14-plastic-ripple-bursting`) is marked `inferred`, because its numbers appear only in the Fig. S14 panel titles. 8 claims carry statistics (21 p-values), and all 36 have a criterion.
- Where the two earlier files named the same finding differently, I kept the 000044 id and listed the crcns-hc-11 alias in the opening comment.
- Composite claims are split: Fig. 1C into above-chance, POST > PRE and MAZE > PRE; Fig. 4C into three; the 000044 ripple/burst/coactivation claim into three.
- The 000044 file's method choices were made before the supplement was available. They are replaced by the supplement's methods.
- The 9 checker problems:
  - 8 p-values printed only in the Fig. S14 panel titles.
  - The Fig. S16 legend's "3.94 x10-06", a number format the checker doesn't parse.

  To read these I installed PyMuPDF into a temp directory and rendered the pages. The Fig. S5, S6, S9 and S16–S19 values match too.

**Details the paper leaves open, with the readings named:**
- **Sleep scoring (S):** the lab's own state epochs, or a recomputed theta/delta + EMG scoring.
- **PRE/POST yoking to the shorter epoch (Y):** the parts nearest the maze, the first part of each epoch, or counted in offline time.
- **LFP ripple threshold (L):** mean + 3 SD, or mean + 5 SD.
- **Linear-maze direction handling (D):** both direction templates scored, or one direction assigned by the direction decoder.
- **Test for "strongly contributing" (P):** the Methods say rank-sum, the Fig. S19B legend says signed-rank.
- **Denominator of the 54% place cells:** per running direction, or all 562 pyramidal cells.
- **Duration test events:** all ripple events, or only the replay-eligible ones.
- **What "eliminated" means in Fig. 2D:** mean change at or below zero, or a bootstrap interval that includes zero. Steps of 5% are a standard choice.
- **Fig. S5B bootstrap comparison:** two forms named.
- **Fig. S2 track distribution:** no test given; KS test, or rank-sum on distance from the track end.
- **Place-field stability split:** halves, or odd/even laps.
- **Firing rates:** what "session-wide" covers (three readings) and the MAZE rate (two).
- **Within-ripple ISIs:** within one event, or across concatenated ripples.
- **Ripple-triggered rate test and per-cell coactivity change:** two readings each.
- **Low/high rate split** (Methods referenced but absent): per session and direction, per session, or pooled; rate from PRE + POST or PRE only.
- **Fig. 4C ranking:** within session or pooled. No test is named, so Spearman and signed-rank are flagged as standard choices, not the paper's.
- **Fig. 4D/E test:** rank-sum, or bootstrap interval.
- **Fisher Z form:** independent or dependent correlations.

**Missing from the paper:** the images of main Figures 1–4 are not under `paper/`, so values printed only in those panels are not recorded. Criteria for those claims rely on the legends and the supplementary counterparts. There are also inconsistencies the claims work around:
- The main text's supplementary figure numbers are off by one in places; the claims use the supplement's own numbering.
- The Fig. S14 colour key is reversed relative to its legend; the legend text is followed.

## End of run

33 turns, 6 minutes, $2.38 at API prices, result: success.
