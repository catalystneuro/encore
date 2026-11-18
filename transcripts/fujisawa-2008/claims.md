# fujisawa-2008 · claims · run 43761542707

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls; ls paper claims claims/fujisawa-2008; grep -n "^#" docs/protocol.md
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
[... 348 more lines not kept]
```

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

**Agent calls Read**

```json
{
 "file_path": "claims/fujisawa-2008/000067.yaml"
}
```

```
1	# Claims for Fujisawa, Amarasingham, Harrison & Buzsaki (2008) on dandiset 000067.
2	# Source: the author manuscript in PubMed Central (PMC2562676), full text of the Results,
3	# figure legends and Methods. The supplementary information (which defines some measures, for
4	# example the rate-normalized peak height of Figure 6 and the satellites of Figure 7) could not
5	# be retrieved: PubMed Central and the publisher answered with a reCAPTCHA page.
6	# Quotes and statistics added 2026-10-19 from the full text (PubMed Central author manuscript
7	# PMC2562676, article page).
8	# Checked against the version of record (publisher PDF) 2026-10-20; every quote, number,
9	# statistic and figure or panel reference is the same as in the manuscript (the text differs
10	# only by PDF symbol-font artefacts). The PDF does not include the supplementary information.
11	#
12	# What had been seen when these criteria were written: the file list and metadata of every
13	# file; the contents of the units, trials, position and electrode tables; spikes per unit and
14	# firing rates; the shank and region of each unit from its mean wideband waveform; the
15	# refractory violations used to flag multi-unit clusters; the nose-poke sensor channels; the
16	# theta ratio of every channel. In addition, a timing run of the jitter test for monosynaptic
17	# connections printed, per session, the number of PFC single units, of ordered pairs, and of
18	# excitatory and inhibitory connections (293 and 73 of 31754 ordered pairs in total). That run
19	# came before the criteria of fig3-connection-rates, fig3-cell-classes and fig3f-distance were
20	# written; no method choice of those claims was changed after it. No other claim's analysis had
[... 382 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/fujisawa-2008/crcns-pfc-2.yaml"
}
```

```
1	# Claims for Fujisawa, Amarasingham, Harrison & Buzsaki (2008), Nature Neuroscience 11:823-833,
2	# on CRCNS data set pfc-2 (doi:10.6080/K01V5BWK).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-07,
4	# protocol as stated in docs/protocol.md (Reader).
5	#
6	# Text read: the version of record (PDF supplied by a person, text by PyMuPDF), main text, figure
7	# legends and Methods, with its supplement (Supplementary Note, legends of Supplementary Figures
8	# 1 to 16, references). The PDF pages could not be rendered in this run, so numbers and
9	# significance marks printed only inside figure panels (Figure 2b, 2d, 2e, 3e, 3f, 7b, the
10	# supplementary panels) are not recorded; the claims rest on the text and legends. Figure 2d
11	# (mean firing rates, t-test marks) and Figure 2e (fraction of maze length discriminated) have
12	# no claim for that reason: what the marks compare is shown only in the panels. The paper links
13	# no analysis code; the only link is to the KlustaKwik spike sorter. None was read.
14	#
15	# Data the paper used. Four adult male rats (3 to 5 months old) trained on an odor-based delayed
16	# matching-to-sample task on a figure-eight T-maze: a nose-poke in the start box gives a cheese or
17	# chocolate odor, which signals the reward in the right or left goal arm (the pairing varied
18	# across rats). Mean correct performance in recording sessions 91.9%. One 8-shank, 64-site silicon
19	# probe per rat (200 um shank separation, 8 staggered sites per shank) in anterior cingulate (area
20	# 24) and dorsal prelimbic (area 32) cortex; three rats in layer 2/3, one in layer 5. Wideband
[... 735 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; head -30 paper/10.1038-nn.2134.txt; cat papers/datasets/fujisawa-2008.yaml; head -50 tools/claims_check.py
```

Result: not kept, because it reads the paper's text.

**Agent**

Now read the full paper text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.2134.txt",
 "offset": 30,
 "limit": 900
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.2134.txt",
 "offset": 929,
 "limit": 800
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-nn.2134.txt",
 "offset": 1729,
 "limit": 640
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; grep -l "^datasets:" claims/*.yaml | head -3; grep -rl "  datasets:" claims/*.yaml | head -3
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
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
cd  head -40 claims/kim-2022.yaml; grep -n "datasets:" -A3 claims/kim-2022.yaml | head -20; head -60 paper/pfc-2.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -rl "000067" --include=*.yaml --include=*.json --include=*.md . 2>/dev/null | grep -v node_modules | head; sed -n 60,140p paper/pfc-2.data-description.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls transcripts/fujisawa-2008/ transcripts/fujisawa-2008/*; grep -rhi "title" transcripts/fujisawa-2008/000067/*.md | grep -i 000067 | head -5
```

```
transcripts/fujisawa-2008/:
000067
crcns-pfc-2

transcripts/fujisawa-2008/000067:
author-report.md
author-revise-1-report.md
author-revise-1.md
author-revise-2-report.md
author-revise-2.md
author-revise-3-report.md
author-revise-3.md
author.md
recorder-report.md
recorder.md
verifier-1-report.md
verifier-1.md
verifier-2-report.md
verifier-2.md
verifier-3-report.md
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s -m 20 https://api.dandiarchive.org/api/dandisets/000067/ | python -c "import json,sys;d=json.load(sys.stdin);print(d['most_recent_published_version'] or d['draft_version'])"; curl -s -m 20 https://api.dandiarchive.org/api/dandisets/000067/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin)['metadata'];print(d.get('name'));print(d.get('description'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python -c "
import fitz
d=fitz.open('paper/10.1038-nn.2134.pdf')
for i in [2,3]:
  p=d[i]; pix=p.get_pixmap(dpi=200); pix.save('$TMPDIR/p%d.png'%(i+1))
print('ok')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  (uv run --quiet python -c "import fitz;print('uv ok')" 2>&1 | tail -1); which pdftoppm mutool 2>&1 | head
```

```
uv ok
```

**Agent calls Bash**

```bash
cd  uv run --quiet python -c "
import fitz
d=fitz.open('paper/10.1038-nn.2134.pdf')
for i in [2,3]:
  p=d[i]; pix=p.get_pixmap(dpi=150); pix.save('$TMPDIR/p%d.png'%(i+1))
print(len(d))
"; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text and supplement are present; no linked analysis code. Checking Figure 2 and 3 panels whose numbers the text garbles.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p3.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p4.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  uv run --quiet python -W ignore -c "
import pymupdf
d=pymupdf.open('paper/10.1038-nn.2134.pdf')
p=d[4]; 
r=p.search_for('13,572')
print(r)
clip=pymupdf.Rect(0,r[0].y0-30,p.rect.width,r[0].y1+20)
p.get_pixmap(dpi=200,clip=clip).save('$TMPDIR/l.png')
s=pymupdf.open('paper/10.1038-nn.2134.supp.pdf'); print(len(s))
q=s[14]; r=q.search_for('1422'); print(r)
clip=pymupdf.Rect(0,r[0].y0-30,q.rect.width,r[0].y1+30)
q.get_pixmap(dpi=200,clip=clip).save('$TMPDIR/s.png')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/l.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
cd  uv run --quiet python -W ignore -c "
import pymupdf
s=pymupdf.open('paper/10.1038-nn.2134.supp.pdf')
for i in [3,4,5]:
  s[i].get_pixmap(dpi=130).save('$TMPDIR/s%d.png'%(i+1))
"
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s4.png"
}
```

Result: not kept, because it reads the paper's text.

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s5.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/s6.png"
}
```

Result: no output.

**Agent**

Writing the merged claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/fujisawa-2008.yaml",
 "content": "# Claims for Fujisawa, Amarasingham, Harrison & Buzsaki (2008), Nature Neuroscience 11:823-833,\n# doi:10.1038/nn.2134, tested on DANDI:000067 and CRCNS pfc-2 (doi:10.6080/K01V5BWK).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-15,\n# protocol as stated in docs/protocol.md (version pilot-15, Reader). It replaces the two files\n# read per dataset, claims/fujisawa-2008/000067.yaml and claims/fujisawa-2008/crcns-pfc-2.yaml;\n# their ids are kept where the finding is the same (map below).\n#\n# Text read. The version of record (PDF supplied by a person; text by PyMuPDF in\n# paper/10.1038-nn.2134.txt): main text, figure legends, Methods, and the supplement (Supplementary\n# Note; legends of Supplementary Figures 1 to 16; references). PDF pages were opened only for\n# figures the text garbles: Figure 2 (the counts and t-test marks of panels d and e), Figure 3\n# (legend of 3b, the matrix size printed as 117 squared), Supplementary Figures 1 to 3, and the\n# legend of Supplementary Figure 11 (142 squared). Where the extracted text prints \"1172\" and\n# \"1422\" the PDF has 117^2 and 142^2 (a lost superscript); quotes keep the extracted text. The\n# paper links no analysis code; its only link is to the KlustaKwik spike sorter, which was not\n# read, as it is not analysis code of the paper.\n#\n# The datasets. DANDI:000067 is titled with the paper's title and carries its abstract as\n# description. The CRCNS pfc-2 description says it holds simultaneous PFC (64 channels) and CA1\n# (32 channels) recordings in three rats (EE, FF, GG) during the working memory task of this\n# paper, with sleep and a spontaneous alternation task on some days, and names session EE.188 as\n# the session of Figures 2A and 3D. Both are read here as holding the same recordings, so every\n# claim on the recordings rests on both. The channel map link rests on 000067 alone.\n#\n# Data the paper used, as it reports them. Four adult male rats (3 to 5 months) trained on an\n# odor-based delayed matching-to-sample task on a figure-eight T-maze: after a nose poke in the\n# start box an odor (cheese or chocolate) signals the reward in the right or left goal arm (the\n# pairing varied across rats). Mean correct performance in the recording sessions 91.9%. One\n# 8-shank, 64-site silicon probe per rat (200 um shank separation, 8 staggered sites per shank,\n# 20 um vertical separation) in anterior cingulate (area 24) and dorsal prelimbic (area 32)\n# cortex; three rats in layer 2/3 and one in layer 5. Supplementary Figure 1 names the rats E, F,\n# G and H: F in layer 5, E, G and H in layer 2/3. Wideband signals at 20 kHz, high-pass 0.8 to\n# 5 kHz for sorting, KlustaKwik with manual adjustment; two head LEDs (5 cm apart) tracked at 40\n# Hz. 633 well-isolated units, 411 in layer 2/3 and 222 in layer 5 (counts printed in Figure 2d);\n# of these, putative pyramidal cells 133 (layer 2/3) and 85 (layer 5), putative interneurons 37\n# and 47. Each trial's path is linearised to a normalised position from 0 (odor sampling, the\n# end of nose poking; Supplementary Figure 6 legend) to 1 (reward area), total length 230 cm, and\n# labelled LEFT or RIGHT by the goal arm. Figure 2a and Figures 3b to 3d, 4, 5, 6b and 7a use one\n# layer 2/3 session of 117 neurons; Figure 2a and Supplementary Figure 11 use one layer 5 session\n# of 142 neurons (Figure 2a legend, \"in two rats\").\n#\n# Rats and layers (open). The datasets name three rats EE, FF and GG; the paper names four, E to\n# H, and never links its names to the files. Readings: R-a, the datasets' EE, FF and GG are the\n# paper's rats E, F and G, so FF is the layer 5 rat and layer 2/3 rat H is not in the data; R-b,\n# the names are not linked, each dataset rat may be either layer, with at most one in layer 5.\n# Every claim with values by layer is run under both.\n#\n# Shared method, from the Methods unless stated.\n# - Trials and positions. A trial runs from the end of the last nose poke (position 0) to the\n#   start of reward consumption (position 1). Whether error trials enter any analysis is not\n#   said (open; readings T-a correct trials only, T-b all trials).\n# - Firing-rate differences (LEFT against RIGHT, or any two trial labels). Spikes are placed at\n#   the normalised position where they occur; the PSTH per condition is the sum of Gaussian\n#   kernels (bandwidth 0.05 normalised length) over the condition's spikes divided by its number\n#   of trials. Statistic D0(x) = left PSTH minus right PSTH. Labels are permuted M times;\n#   pointwise two-sided bands, and global bands by the stepping procedure (the smallest pointwise\n#   band whose global acceptance level is alpha). A segment is significant when the global band is\n#   broken; its extent is where the pointwise band is broken (Figure 1c legend, Supplementary\n#   Figure 4E). Alpha = 0.05 (Figure 1c legend). M is not given (Methods M, Supplementary\n#   Figure 4 R): 1,000 is a standard choice, as for the jitter; it should not change the outcome.\n#   The positions at which D0 is evaluated are not given; 101 points from 0 to 1 is a standard\n#   choice.\n# - Rates for display and widths. Figure 1c legend says rates are normalised by the time spent at\n#   each position (Hz); the Methods' PSTH is spikes per unit length per trial (Supplementary\n#   Figure 4A says one converts to the other by dividing by occupancy). Where a rate's shape\n#   matters (widths, peaks), readings P-a occupancy-normalised, P-b the Methods' PSTH.\n# - Units. All well-isolated PFC units of a session; the paper sets no rate threshold. The 1 Hz\n#   \"Cells\" list of the CRCNS description is not the paper's and is only a variant.\n# - Monosynaptic connections. Every spike of each neuron is jittered uniformly on [-5, +5] ms,\n#   1,000 surrogates. Cross-correlogram over latencies [-5, +5] ms; pointwise and global bands at\n#   the 99% level, the global band from the maximum and minimum of each surrogate. A connection is\n#   excitatory (peak) or inhibitory (trough) when the counts break the global band anywhere in\n#   [1, 4] ms. Pairs are counted in both directions. The Results add onset below 5 ms and a peak\n#   of 2 ms or less. Supplementary Figure 9A jitters the spikes of one neuron only, a variant.\n#   The CCG bin width is not given (open; readings B-a 1 ms, B-b 0.5 ms). How the 2 ms width is\n#   measured is not given (open; readings W-a the [1, 4] ms global band test alone, as the\n#   Methods state it; W-b also requiring the run of bins above the pointwise 99% band to span 2 ms\n#   or less). A pair's CCG uses the whole task session, intertrial intervals included (Results,\n#   on Figure 3b).\n# - Cell types. A reference cell with a significant short-latency peak is a putative pyramidal\n#   cell, one with a significant trough a putative interneuron (Figure 3a legend). A unit with\n#   both is not covered (open; readings C-a unclassified, C-b excluded from the denominators).\n# - Position of excess coincidences. Coincident events are spike pairs with 1 <= tdiff <= 4 ms\n#   (presynaptic first), placed at the position where they occur, smoothed with the 0.05 kernel\n#   and divided by the number of trials; surrogates by jittering the spikes on [-5, +5] ms (both\n#   cells, Methods; the presynaptic cell only, Supplementary Figure 12B, as a variant; 1,000, a\n#   standard choice, as this section gives no number); one-sided pointwise and global bands for\n#   excess at P < 0.01 (Figures 4 and 5). Whether the event is placed at the presynaptic or the\n#   postsynaptic spike is not said; the two are at most 4 ms apart, so the presynaptic spike is a\n#   standard choice.\n#\n# Id map. From 000067.yaml: rats-and-units (crcns unit-count), fig2c-active-fraction (crcns\n# fig2c-synchrony-by-layer), fig2-field-size (crcns lifetime-width), traj-diverge (crcns\n# trajectory-divergence), odor-nosepoke (crcns odor-selective-fraction), fig3-connection-rates\n# (crcns connection-counts), fig3-cell-classes (crcns cell-type-fractions), fig4-position-dependence\n# (crcns position-dependent-transmission), fig6-facilitation-depression (crcns\n# fig6-depression-facilitation), fig7-supralinear (crcns fig7-supralinear-coincidence),\n# fig3-trajectory-by-class (crcns connected-cells-trajectory-specific). The 000067 claim\n# fig2b-trajectory-selective is split into side-arm-selectivity-by-layer and\n# central-arm-selectivity; its ee188-example-session is split into fig3b-session-connections,\n# fig3d-hub, fig5a-session-selective-connections, fig4-pair-156-136, fig5b-example-pairs and\n# fig6b-convergent-examples. New: fig2d-layer-rates and fig2e-layer-discrimination.\nschema_version: 2\npaper: doi:10.1038/nn.2134\nclaims:\n- id: channel-region-link\n  kind: link\n  statement: The recording channels of DANDI:000067 can be assigned to the prefrontal probe, the\n    CA1 probe and the nose-poke sensors by the channel map of the CRCNS pfc-2 description of the\n    same recordings (channels 1 to 64 prefrontal, 65 to 96 CA1, 97 right and 98 left nose-poke\n    sensors), and the data agree with that map.\n  source: Methods, Surgery and recording (8-shank, 64-site probe in mPFC); CRCNS pfc-2 data\n    description, version 0.7\n  data: with_labels\n  datasets:\n  - \"000067\"\n  criterion: Two checks in each working memory session. (i) The median theta ratio (6 to 10 Hz\n    over 1 to 40 Hz power, during trials) of the CA1 channels is above that of channels 1 to 64.\n    (ii) In at least 90% of trials the sensor channel with more activity during the nose poke is\n    the one of the trial's side. Reproduced when both hold in every session with the CRCNS channel\n    numbers; partially reproduced when both hold only with a per-rat correction of the channel\n    numbers found in the data; not reproduced otherwise.\n- id: rats-and-units\n  statement: A total of 633 well-isolated units were recorded from anterior cingulate and dorsal\n    prelimbic cortex in four rats, 411 in layer 2/3 (three rats) and 222 in layer 5 (one rat).\n  source: Results, paragraph 1; Methods, Surgery and recording; Figure 2d (unit counts in the bars)\n  quote: We recorded a total of 633 well-isolated units from the anterior cingulate area (area 24)\n    and dorsal prelimbic area (area 32) of the medial prefrontal cortex (mPFC)22 in four rats.\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  expected:\n  - quantity: well-isolated mPFC units, layer 5 rat\n    value: 222\n    tolerance: 22.2\n    unit: units\n  - quantity: well-isolated mPFC units, all four rats\n    value: 633\n    tolerance: 63.3\n    unit: units\n  criterion: Units are the sorted PFC units of all working memory sessions, each session's units\n    counted as distinct (the paper does not say whether a unit recorded on several days counts\n    once; sorting is per session). The datasets hold three of the four rats, so their total is\n    expected below 633. Layer 5 is one rat, so its 222 units can be checked whole. Reproduced when\n    one rat's units are within 222 +/- 22.2 (FF under reading R-a; any rat under R-b) and the\n    other two rats together hold no more than 411 + 41.1; partially reproduced when the total\n    over the three rats is within 633 +/- 63.3 but no rat matches 222; not reproduced otherwise.\n    The total is reported against 633.\n- id: task-performance\n  statement: Rats performed the odor-place matching task at 92% correct, 91.9% in the recording\n    sessions.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 1;\n    Methods, Behavioral task\n  quote: All rats performed the task at high proficiency (mean performance, 92% correct) at the\n    time of neurophysiological data collection ... In the recording sessions, the mean correct\n    performance was 91.9%.\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  expected:\n    quantity: mean percentage of correct trials over recording sessions\n    value: 91.9\n    tolerance: 9.19\n    unit: percent\n  criterion: Correct trials over all trials, per session, averaged over the working memory\n    sessions; the pooled percentage over sessions is shown as a variant (the paper does not say\n    which). Blocked (data_missing) if the datasets list correct trials only.\n- id: fig2-population-uniform\n  statement: Individual neurons fire transiently at specific locations, but the population as a\n    whole fires relatively uniformly over the whole maze.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 3; Figure\n    2a and 2b\n  quote: viewed as a population, the firing properties of mPFC neurons were quite homogeneous\n    ... individual neurons fired transiently, but, as a whole, the population of neurons fired\n    relatively uniformly over the entire apparatus\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  criterion: The paper gives no measure or test. Per neuron, the left and right PSTHs (shared\n    method); the position of each neuron's peak rate on its side of higher peak, as Figure 2a\n    orders them. Reproduced when, in each Figure 2a session, no tenth of the maze holds more than\n    twice or less than half its expected share of peaks, and the population mean rate per tenth\n    stays within 50% of its overall mean (Figure 2b). These thresholds are standard choices, not\n    the paper's; a chi-square test of the peak positions against uniform at p < 0.05 is reported\n    as a variant, and all sessions as a second variant.\n- id: fig2c-active-fraction\n  statement: About 10% of layer 2/3 neurons and 20% of layer 5 neurons fire at least one spike in\n    a given 100 ms window, a fraction relatively constant over the maze.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 3; Figure\n    2c; Discussion, Behavior-dependence of short-term plasticity in mPFC, paragraph 1\n  quote: the population firing rates (Fig. 2b) and the fraction of simultaneously active neurons\n    (10% and 20% in 100-ms windows, layers 2/3 and 5, respectively; Fig. 2c) were relatively\n    constant in all segments of the maze\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  expected:\n  - quantity: mean percentage of layer 2/3 neurons active in a 100 ms window\n    value: 10\n    tolerance: 1\n    unit: percent\n  - quantity: mean percentage of layer 5 neurons active in a 100 ms window\n    value: 20\n    tolerance: 2\n    unit: percent\n  criterion: Per Figure 2c legend, the percentage of the session's neurons firing at least one\n    spike in consecutive 100 ms windows, averaged over the windows within trials (Figure 2c is\n    plotted against normalised position, left and right trials apart). Which sessions is open;\n    readings (a) the two Figure 2a sessions (117 and 142 neurons; Figure 2c sits under them and,\n    unlike 2b, is not labelled \"group\"); (b) all sessions of each layer, under rat readings R-a\n    and R-b. Reproduced when both values are within tolerance under one reading, and the mean\n    over the windows in each tenth of the maze stays within 50% of the overall mean (a standard\n    choice for \"relatively constant\"; the paper gives no test).\n- id: fig2-field-size\n  statement: Most neurons are active over a similar stretch of the maze, 0.27 (62 cm) +/- 0.17 (39\n    cm) of normalised length (mean +/- s.d.), measured between the 50% boundaries of the peak\n    rate.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 3;\n    Supplementary Figure 2B\n  quote: most neurons were generically active for similar standardized distances of 0.27 (62 cm)\n    ± 0.17 (39 cm) (mean ± s.d.) in the maze (as determined by the 50% firing boundaries of the\n    peak firing rate\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  expected:\n  - quantity: mean width of firing at 50% of peak\n    value: 0.27\n    tolerance: 0.17\n    unit: normalised length\n  - quantity: s.d. of width across neurons\n    value: 0.17\n    tolerance: 0.017\n    unit: normalised length\n  criterion: Width of the PSTH between the 50% boundaries of its peak height (Supplementary\n    Figure 2B), with rate readings P-a and P-b. The tolerance of the mean is the stated s.d.; the\n    s.d. takes 10%. Open details and readings. Which PSTH; (a) each neuron's PSTH over all\n    trials; (b) its left and right PSTHs as two entries; (c) the PSTH of the side with the higher\n    peak. The width; (i) the contiguous run around the peak at or above 50%; (ii) the total length\n    at or above 50%. Which neurons; (x) the two Figure 2a sessions, (y) all units of the task\n    sessions (Supplementary Figure 2B shows \"All\" with a count axis to 150, larger than one\n    session). Reproduced when both values are within tolerance under one combination.\n- id: population-vector-width\n  statement: Population vector correlations fall off over similar distances throughout the maze,\n    0.18 +/- 0.087 of normalised length in layer 2/3 and 0.27 +/- 0.13 in layer 5.\n  source: Supplementary Figure 2A\n  quote: Neuronal populations were relatively evenly correlated throughout the maze segments with\n    0.18(41cm) ± 0.087(29cm) (L2/3) and 0.27(62cm) ± 0.13(30cm) (L5) in normalized length\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  expected:\n  - quantity: layer 2/3 correlation width\n    value: 0.18\n    tolerance: 0.087\n    unit: normalised length\n  - quantity: layer 5 correlation width\n    value: 0.27\n    tolerance: 0.13\n    unit: normalised length\n  criterion: Population vectors of PSTHs (shared method) at each position, and the correlation\n    matrix between positions, as Supplementary Figure 2A. The width is not defined in the paper;\n    reading, for each position, the length around the diagonal over which the correlation stays\n    above half its diagonal value, mean +/- s.d. over positions. Which trials is open; readings\n    (a) left and right PSTHs concatenated in each vector, (b) all trials. The panel does not name\n    its sessions; the Figure 2a sessions, with all sessions of each layer as a variant. The\n    tolerances are the stated s.d. Reproduced when both values are within tolerance under one\n    reading.\n- id: fig2d-layer-rates\n  statement: Layer 5 neurons fire at higher mean rates than layer 2/3 neurons, over all neurons\n    (222 against 411) and over putative pyramidal cells (85 against 133), both at P < 0.01 by\n    t-test; putative interneurons (47 against 37) carry no significance mark.\n  source: Figure 2d\n  quote: Mean firing rates of the neuronal populations (± s.d.)\n  statistics:\n  - about: all neurons, layer 5 against layer 2/3\n    test: t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 411 layer 2/3 and 222 layer 5 neurons\n  - about: putative pyramidal cells, layer 5 against layer 2/3\n    test: t-test\n    p: 0.01\n    p_relation: \"<\"\n    n: 133 layer 2/3 and 85 layer 5 cells\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3-cell-classes\n  criterion: Per neuron, its mean rate over the task session (the paper does not say over which\n    period; readings (a) trials only, (b) the whole task session). Layers by rat readings R-a and\n    R-b; cell types from fig3-cell-classes. The t-test form is not given; readings Student's and\n    Welch's two-sample tests. Reproduced when, under one combination, layer 5 is higher for all\n    neurons and for pyramidal cells, each at p < 0.01; partially reproduced when one of the two\n    holds. The interneuron comparison is reported, not judged. Figure 2d bars read near 2.0 and\n    3.6 Hz (all), 1.6 and 2.9 Hz (pyramidal), 8.3 and 7.8 Hz (interneurons); these are read from\n    the figure, so they are reported for comparison and not judged.\n- id: fig2e-layer-discrimination\n  statement: Single layer 5 neurons discriminate left from right trials over a larger fraction of\n    the maze than layer 2/3 neurons, for all neurons (P < 0.05), putative pyramidal cells (P <\n    0.01) and putative interneurons (P < 0.01), by t-test.\n  source: Figure 2e\n  quote: Mean fraction of maze lengths discriminated by firing rates of single neurons (± s.d.)\n  statistics:\n  - about: all neurons, layer 5 against layer 2/3\n    test: t-test\n    p: 0.05\n    p_relation: \"<\"\n  - about: putative pyramidal cells, layer 5 against layer 2/3\n    test: t-test\n    p: 0.01\n    p_relation: \"<\"\n  - about: putative interneurons, layer 5 against layer 2/3\n    test: t-test\n    p: 0.01\n    p_relation: \"<\"\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3-cell-classes\n  - side-arm-selectivity-by-layer\n  criterion: Per neuron, the total length of its significant segments (global band broken,\n    extent by the pointwise band, shared method) as a fraction of the maze. Which neurons enter\n    the mean is open; readings (a) all neurons, a non-selective neuron counting 0, (b) selective\n    neurons only. Layers by rat readings R-a and R-b; t-test readings Student's and Welch's.\n    Reproduced when, under one combination, layer 5 is higher in all three groups at the paper's\n    levels; partially reproduced when it is higher in at least two at p < 0.05. Bars read near\n    0.16 and 0.28 (all), 0.22 and 0.29 (pyramidal), 0.12 and 0.35 (interneurons) are reported,\n    not judged.\n- id: traj-diverge\n  statement: Left and right running paths overlap in the central arm and diverge significantly\n    from position 0.30; head directions diverge from 0.24.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 4;\n    Supplementary Figure 3B\n  quote: Left and right lap trajectories in segments 0 to 0.3 of the central arm overlapped; they\n    began to differ significantly at position 0.3 ... Significant separation of left/right\n    trajectories and head directions emerged at position 0.30 and 0.24, respectively (p<0.01)\n  statistics:\n  - test: permutation test with global bands, left and right labels shuffled\n    p: 0.01\n    p_relation: \"<\"\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  expected:\n  - quantity: first position of significant left-right difference in path\n    value: 0.30\n    tolerance: 0.03\n    unit: normalised position\n  - quantity: first position of significant left-right difference in head direction\n    value: 0.24\n    tolerance: 0.024\n    unit: normalised position\n  criterion: The permutation test of the shared method (Supplementary Figure 3B legend) at global\n    level 0.01, applied per trial to the horizontal (lateral) head position in cm (the panel's\n    \"Trajectory difference\" axis, R/L difference in cm) and to head direction, the angle of the\n    line between the two LEDs, each as a function of normalised position. Per trial, the variable\n    is taken at each point of the position grid (interpolated), and the left minus right mean is\n    the statistic. The panel does not name the session; Supplementary Figure 3A uses the Figure\n    2a layer 2/3 session, which is used, with all sessions shown as a variant. Reproduced when\n    the first globally significant position is within tolerance for both. Partially reproduced\n    when the path matches and head direction does not, or the reverse.\n- id: side-arm-selectivity-by-layer\n  statement: In the side arms (positions 0.5 to 1) the fraction of neurons firing differently on\n    left and right trials is almost twice as large in layer 5 (40%) as in layer 2/3 (22%).\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 4; Figure\n    2b\n  quote: The fraction of trajectory-selective neurons in the side arms (positions 0.5-1) was\n    almost twice as large in deep (layer 5, 40%) than in superficial (layer 2/3, 22%) neurons\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  expected:\n  - quantity: layer 5 neurons with a significant left-right segment in positions 0.5 to 1\n    value: 40\n    tolerance: 4\n    unit: percent\n  - quantity: layer 2/3 neurons with a significant left-right segment in positions 0.5 to 1\n    value: 22\n    tolerance: 2.2\n    unit: percent\n  criterion: The permutation test of the shared method per neuron, pooled from all rats and\n    sessions of each layer (Figure 2b legend), with rat readings R-a and R-b. Open details. A\n    neuron counts when (a) any part of a significant segment lies in 0.5 to 1, or (b) the global\n    band is broken within 0.5 to 1. Reproduced when both values are within tolerance under one\n    reading; partially reproduced when the layer 5 fraction is above the layer 2/3 fraction by a\n    one-sided Fisher exact test at p < 0.05 but the values are not within tolerance.\n- id: central-arm-selectivity\n  statement: A smaller fraction of neurons, 16% in layer 2/3 and 18% in layer 5, fire differently\n    on left and right trials already in the central arm (positions 0 to 0.3), where paths and\n    head directions are apparently indistinguishable.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 4; Figure\n    2b\n  quote: a sizable but smaller fraction of neurons in both layer 2/3 and layer 5 (16% and 18%,\n    respectively; Fig. 2b) was also differentially active in the central arm (segments 0-0.3)\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - side-arm-selectivity-by-layer\n  expected:\n  - quantity: layer 2/3 neurons with a significant left-right segment in positions 0 to 0.3\n    value: 16\n    tolerance: 1.6\n    unit: percent\n  - quantity: layer 5 neurons with a significant left-right segment in positions 0 to 0.3\n    value: 18\n    tolerance: 1.8\n    unit: percent\n  criterion: As side-arm-selectivity-by-layer, for positions 0 to 0.3, with the same readings.\n    Reproduced when both values are within tolerance under one reading; partially reproduced\n    when the pooled fraction is above the fraction from one random relabelling of each neuron's\n    trials (one-sided Fisher exact test, p < 0.05) but the values are not within tolerance.\n- id: odor-nosepoke\n  statement: About a quarter of neurons (26% in one layer 2/3 session) fire at significantly\n    different rates during nose poking for the two odors.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 4;\n    Supplementary Figure 6B\n  quote: Approximately one-quarter of the neurons showed significantly different ... firing rates\n    in response to one of the two odorants ... Although 26% of neurons showed significant odor\n    preference (t-test, p<.05)\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  expected:\n    quantity: neurons with different nose-poke firing rates for the two odors\n    value: 26\n    tolerance: 2.6\n    unit: percent\n  criterion: Per neuron, its rate during each trial's nose poke (Supplementary Figure 6A, the\n    duration of nose poking from the photoelectric sensor; from the start of the first poke to\n    the end of the last), left (one odor) against right (the other) trials, t-test at p < 0.05\n    (Supplementary Figure 6B). The odor is given by the side, as the pairing of odor and side is\n    fixed within a rat. Open details and readings. Which neurons; (a) the Figure 2a layer 2/3\n    session, as Supplementary Figure 6B (\"same as Fig 2A left\"); (b) all neurons, as the Results\n    sentence may mean. The t-test form; Student's or Welch's. Reproduced when the fraction is\n    within tolerance under one reading.\n- id: odor-unrelated-to-stem\n  statement: Neurons' odor preference during nose poking is unrelated to their left-right\n    differences in the stem and side arms, so odor traces do not explain the stem selectivity.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 4;\n    Supplementary Figure 6B\n  quote: we ruled out this possibility after examining, and finding no reliable relationship\n    among, the differential firing patterns in the stem area and during nose poking\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - odor-nosepoke\n  - central-arm-selectivity\n  criterion: A claim of absence for which the paper names no test. Readings (a) a Fisher exact\n    test of odor-selective against stem-selective classification over the session's neurons;\n    (b) the correlation across neurons between the nose-poke rate difference and the mean left\n    minus right PSTH in 0 to 0.3, at p < 0.05. Both readings are run for the stem (0 to 0.3) and\n    the side arms (0.5 to 1), as the Supplementary Figure 6B legend states independence from both,\n    on the session of odor-nosepoke reading (a). Reproduced when neither reading finds an\n    association at p < 0.05 in either region; the size of each is reported.\n- id: retrospective-coding-rare\n  statement: Only a small fraction of neurons fire differently according to the reward location of\n    the previous trial.\n  source: Results, Medial prefrontal cortical units predict behavioral choice, paragraph 4;\n    Supplementary Figures 7 and 8\n  quote: found only spare evidence that any neurons fired differentially on the basis of previously\n    visited positions ... Note that only a small fraction of neurons show retrospective coding\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - side-arm-selectivity-by-layer\n  criterion: The permutation test of the shared method with trials labelled by the previous\n    trial's reward side (Supplementary Figure 7, P < 0.05); the first trial of a session has no\n    label and is left out. Supplementary Figures 7 and 8 show layer 2/3 and layer 5 without\n    naming sessions; readings (a) the Figure 2a sessions, (b) all sessions of each layer. \"Small\"\n    is not defined; reproduced when, in each layer, the fraction of neurons with a significant\n    segment for previous-trial labels is less than half the fraction for current-trial labels (a\n    standard choice, not the paper's).\n- id: speed-not-correlated\n  statement: Firing rates show no net positive relationship with running speed; the distribution\n    of rate-speed correlations is symmetric around zero.\n  source: Supplementary Figure 3C\n  quote: The symmetry of these histograms around 0 suggests that, unlike in the hippocampus, this\n    population of neurons does not exhibit a net positive relationship between firing rate and\n    speed.\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3-cell-classes\n  criterion: Per Supplementary Figure 3C, trials divided into 0.5 s bins, mean rate and speed per\n    bin, the correlation coefficient per neuron over its bins. A claim of absence with no test\n    named; reading, a two-sided Wilcoxon signed-rank test of the correlations against 0 over all\n    neurons, and within putative pyramidal cells and interneurons. Reproduced when the median\n    correlation over all neurons is not significantly above 0 at p < 0.05; the median and the\n    test are reported for every group. Speed from the midpoint of the two LEDs (a standard\n    choice).\n- id: fig3-connection-rates\n  statement: Of 62,408 directed pairs of simultaneously recorded neurons, 495 (0.79%) show a\n    short-latency narrow peak or trough in the cross-correlogram by the jitter test, 0.55%\n    excitatory and 0.24% inhibitory, and 0.17% of pairs are reciprocally connected.\n  source: Results, Characterization of mPFC neurons and their connections, paragraph 5; Figure 3a\n    and 3e; Methods, Identifying monosynaptic interactions\n  quote: Of the 62,408 cell pairs (counting each literal pair twice, corresponding to the two\n    directions), 495 (0.79%) had short latency ... 0.55% excitatory connections and 0.24%\n    inhibitory connections (single directions); 0.17% of cell pairs were connected reciprocally\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  expected:\n  - quantity: directed pairs of simultaneously recorded units\n    value: 62408\n    tolerance: 6240.8\n    unit: pairs\n  - quantity: directed pairs with a significant short-latency peak or trough\n    value: 0.79\n    tolerance: 0.079\n    unit: percent\n  - quantity: excitatory connections\n    value: 0.55\n    tolerance: 0.055\n    unit: percent of directed pairs\n  - quantity: inhibitory connections\n    value: 0.24\n    tolerance: 0.024\n    unit: percent of directed pairs\n  - quantity: reciprocally connected pairs\n    value: 0.17\n    tolerance: 0.017\n    unit: percent of pairs\n  criterion: The jitter method of the shared method over every ordered pair of units recorded in\n    the same session, under bin readings B-a and B-b and width readings W-a and W-b. The datasets\n    hold three of the four rats, so the pair count is expected below 62,408 and is reported, not\n    judged. The denominator of the reciprocal fraction is open; readings (a) directed pairs, (b)\n    unordered pairs. Reproduced when the three directed percentages are within tolerance under\n    one combination and the reciprocal fraction under one of its readings; partially reproduced\n    when one or two of the three directed percentages are.\n- id: fig3-cell-classes\n  statement: By their cross-correlogram interactions 32.5% of units are putative pyramidal cells\n    and 12.5% putative interneurons; 50.7% of the targets of excitatory cells themselves suppress\n    other neurons; the ratio of putative pyramidal cells to interneurons is 2.82 +/- 0.51 (s.d.).\n  source: Results, Characterization of mPFC neurons and their connections, paragraph 5\n  quote: a sizable fraction of the recorded units could be classified as putative pyramidal cells\n    (32.5%) or inhibitory interneurons (12.5%). A large percentage of the postsynaptic targets of\n    the putative excitatory cells (50.7%) were suppressing other neurons ... The ratio of putative\n    principal cells to inhibitory interneurons in the entire population, identified by\n    physiological criteria, was 2.82 ± 0.51 (s.d.)\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3-connection-rates\n  expected:\n  - quantity: putative pyramidal cells\n    value: 32.5\n    tolerance: 3.25\n    unit: percent of units\n  - quantity: putative interneurons\n    value: 12.5\n    tolerance: 1.25\n    unit: percent of units\n  - quantity: targets of excitatory cells that are putative interneurons\n    value: 50.7\n    tolerance: 5.07\n    unit: percent\n  - quantity: ratio of putative pyramidal cells to interneurons\n    value: 2.82\n    tolerance: 0.51\n  criterion: Cell types as in the shared method, from the connections of fig3-connection-rates,\n    with readings C-a and C-b. The 50.7% is the fraction of distinct units receiving a significant\n    excitatory peak that themselves have a significant trough as reference. The ratio is a mean\n    over units of analysis the paper does not name; readings (a) per session (sessions with at\n    least one interneuron), (b) per rat, (c) the pooled ratio. The ratio's tolerance is the stated\n    s.d. The counts printed in Figure 2d (218 pyramidal cells and 84 interneurons of 633 units,\n    34.4% and 13.3%) do not give exactly 32.5% and 12.5%; the paper does not say why, and the\n    Figure 2d fractions are reported as a variant. Reproduced when all four values are within\n    tolerance under one combination of readings; partially reproduced when two or three are.\n- id: pyr-pyr-connections\n  statement: Monosynaptic excitation between putative pyramidal cells is rare, found in 0.12% of\n    layer 2/3 and 0.27% of layer 5 pairs.\n  source: Results, Characterization of mPFC neurons and their connections, paragraph 5;\n    Supplementary Note, Potential caveat with the cross-correlation method, paragraph 4\n  quote: Monosynaptic excitation between putative pyramidal cells was detected in 0.12% of layer\n    2/3 and 0.27% of layer 5 pairs\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3-cell-classes\n  expected:\n  - quantity: layer 2/3 pairs with pyramidal to pyramidal excitation\n    value: 0.12\n    tolerance: 0.012\n    unit: percent\n  - quantity: layer 5 pairs with pyramidal to pyramidal excitation\n    value: 0.27\n    tolerance: 0.027\n    unit: percent\n  criterion: Excitatory connections whose target is also a putative pyramidal cell, by layer under\n    rat readings R-a and R-b. The denominator is open; readings (a) all directed pairs of the\n    layer, (b) directed pairs of two putative pyramidal cells. Reproduced when both values are\n    within tolerance under one reading; partially reproduced when the layer 5 value is above the\n    layer 2/3 value but not both within tolerance.\n- id: nearby-pyr-int-probability\n  statement: The connection probability between nearby (under 200 um) putative pyramidal cells and\n    interneurons is 1 to 2%.\n  source: Supplementary Note, Potential caveat with the cross-correlation method, paragraph 3\n  quote: The 1-2% connection probability we detected between the physiologically identified nearby\n    (<200 μm) pyramidal cell-interneuron pairs by the cross-correlation method\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3-cell-classes\n  expected:\n    quantity: probability of a connection between a putative pyramidal cell and interneuron on the\n      same shank\n    value: 1.55\n    tolerance: 0.65\n    unit: percent\n  criterion: The range 1 to 2% widened by 10% of each bound (0.9 to 2.2%). \"Nearby (under 200\n    um)\" is read as the same shank, the shanks being 200 um apart. Direction is open; readings (a)\n    pyramidal to interneuron excitatory connections over such directed pairs, (b) a connection in\n    either direction over unordered pairs. Reproduced when the value lies in the range under one\n    reading.\n- id: fig3b-session-connections\n  statement: In the single layer 2/3 session of Figure 3b (117 neurons, 117 squared pairs) 48\n    connections have a putative pyramidal reference cell and 30 a putative interneuron; in the\n    layer 5 session of Supplementary Figure 11 (142 neurons) the numbers are 73 and 25.\n  source: Figure 3b legend; Results, Characterization of mPFC neurons and their connections,\n    paragraph 6; Supplementary Figure 11 legend\n  quote: Figure 3b illustrates significant peaks and troughs of crosscorrelograms of 1172 pairs of\n    layer 2/3 cells (13,572 matrix points) simultaneously recorded in a single session\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3-connection-rates\n  expected:\n  - quantity: layer 2/3 session, connections with a pyramidal reference cell\n    value: 48\n    tolerance: 4.8\n  - quantity: layer 2/3 session, connections with an interneuron reference cell\n    value: 30\n    tolerance: 3\n  - quantity: layer 5 session, connections with a pyramidal reference cell\n    value: 73\n    tolerance: 7.3\n  - quantity: layer 5 session, connections with an interneuron reference cell\n    value: 25\n    tolerance: 2.5\n  criterion: The jitter method on the Figure 2a sessions, identified by their 117 and 142 neurons\n    (the CRCNS description names EE.188 for the layer 2/3 one; the layer 5 one is in rat F, FF\n    under reading R-a). The \"1172\" of the extracted text is 117 squared in the PDF, and the 13,572\n    matrix points are 117 x 116 ordered pairs; Supplementary Figure 11 gives about 142 squared.\n    Whether the counts are directed connections or distinct reference cells is open; readings (a)\n    directed connections, (b) distinct reference cells. Reproduced when all four are within\n    tolerance under one combination of readings with B-a or B-b and W-a or W-b; partially\n    reproduced when one session's two counts are.\n- id: fig3d-hub\n  statement: A large part of the recorded neurons belong to a single interconnected circuit, 39 of\n    117 (33%) in the layer 2/3 session and 45 of 142 in the layer 5 session.\n  source: Figure 3d; Results, Characterization of mPFC neurons and their connections, paragraph 7;\n    Supplementary Figure 11C\n  quote: a large portion of the active neurons (39 of the 117) belonged to a single\n    interconnected circuit ... a large fraction (45 of 142 total) belonged to a single \"hub\" of\n    network\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3b-session-connections\n  expected:\n  - quantity: neurons in the largest connected circuit, layer 2/3 session\n    value: 39\n    tolerance: 3.9\n  - quantity: neurons in the largest connected circuit, layer 5 session\n    value: 45\n    tolerance: 4.5\n  criterion: The largest connected component of the graph of excitatory and inhibitory\n    connections, edges taken as undirected (Figure 3d draws uni- and bidirectional links), in the\n    sessions of fig3b-session-connections. Reproduced when both counts are within tolerance under\n    one of its readings; partially reproduced when one is.\n- id: fig3f-distance\n  statement: Most connected pairs are on the same shank and connection probability falls rapidly\n    with the distance between the neurons, yet connections are found up to 1,200 um apart.\n  source: Figure 3f; Results, Characterization of mPFC neurons and their connections, paragraph 7\n  quote: most functionally connected pairs were detected locally and recorded by the same probe\n    shank. The probability of putative connections decreased rapidly as a function of distance\n    between the somata of the recorded pair (Fig. 3f), but connections were detected between\n    neurons up to 1,200\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3-connection-rates\n  criterion: Connection probability (excitatory and inhibitory apart, as Figure 3e and 3f) by\n    shank separation (same shank, then 200 to 1,200 um, the Figure 3f axis), with exact\n    Clopper-Pearson 99% intervals (Figure 3 legend). Reproduced when more connected pairs are on\n    the same shank than on all other shanks together, the same-shank probability is above the\n    200 um probability with non-overlapping intervals, and the largest shank separation with a\n    connection is 1,200 um; partially reproduced when the first two hold. Distance from estimated\n    soma positions (Figure 3c, ref. 18) is not used, as the paper does not give that method.\n- id: fig3-trajectory-by-class\n  statement: Large fractions of putative pyramidal cells (72.2% in layer 2/3, 84.7% in layer 5)\n    and of putative interneurons (58.3% and 83%) are trajectory specific.\n  source: Results, Characterization of mPFC neurons and their connections, paragraph 7; Figure 3c;\n    Supplementary Figure 11B\n  quote: In addition to a large fraction of putative pyramidal cells (72.2% and 84.7% in layers 2/3\n    and 5, respectively), many interneurons (58.3% and 83% in layers 2/3 and 5, respectively) ...\n    were also trajectory specific\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3-cell-classes\n  - side-arm-selectivity-by-layer\n  expected:\n  - quantity: trajectory-specific putative pyramidal cells, layer 2/3\n    value: 72.2\n    tolerance: 7.22\n    unit: percent\n  - quantity: trajectory-specific putative pyramidal cells, layer 5\n    value: 84.7\n    tolerance: 8.47\n    unit: percent\n  - quantity: trajectory-specific putative interneurons, layer 2/3\n    value: 58.3\n    tolerance: 5.83\n    unit: percent\n  - quantity: trajectory-specific putative interneurons, layer 5\n    value: 83\n    tolerance: 8.3\n    unit: percent\n  criterion: A cell is trajectory specific when the permutation test of the shared method gives a\n    significant segment anywhere on the maze (Figure 3c colours R, L or R&L). Which cells is open;\n    readings (a) the identified cells of the two Figure 3 sessions, (b) all sessions of each\n    layer under rat readings R-a and R-b. Reproduced when all four values are within tolerance\n    under one reading; partially reproduced when two or three are.\n- id: no-spatial-clustering\n  statement: Left- and right-specific neurons are not clustered on the probe but spread over the\n    whole recorded volume, and neurons active at any part of the maze are found on all shanks.\n  source: Results, Characterization of mPFC neurons and their connections, paragraph 7; Figure 3c;\n    Discussion, Behavior-dependence of short-term plasticity in mPFC, paragraph 1\n  quote: left and right trajectory-specific neurons (Fig. 1c and Fig. 2) were not clustered\n    together but occupied a large neuronal volume\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3-trajectory-by-class\n  criterion: A claim of absence with no test in the paper. Reading, a chi-square test of shank\n    against class (left, right, both, none) in each Figure 3 session, and, as a variant, in all\n    sessions. Reproduced when no Figure 3 session shows an association at p < 0.05; the effect\n    size (Cramer's V) is reported.\n- id: fig4-position-dependence\n  statement: Of 343 pairs with significant excitatory monosynaptic connections, 67 show\n    identifiable position dependence of excess short-latency coincidences in the maze.\n  source: Results, Behavioral modulation of monosynaptic interactions, paragraph 1; Figure 4b;\n    Methods, Identifying position dependence of monosynaptic interactions; Supplementary Figure 12\n  quote: Across all sessions, out of 343 pairs with significant excitatory monosynaptic connections\n    in all sessions, 67 pairs showed identifiable position dependence in monosynaptic interactions\n    by this measure\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3-connection-rates\n  expected:\n    quantity: excitatory pairs with position-dependent excess coincidences\n    value: 19.5\n    tolerance: 1.95\n    unit: percent\n  criterion: Position of excess coincidences as in the shared method, at global P < 0.01, over the\n    excitatory connections of fig3-connection-rates (343 is 0.55% of 62,408). The datasets hold\n    three of the four rats, so the fraction 67/343 is judged and the counts are reported. Open\n    details and readings. Trials; (a) left and right analysed apart, a pair counting when either\n    shows dependence (Figures 4 and 5 show them apart); (b) all trials together. Position\n    dependence; (i) a globally significant region anywhere; (ii) a globally significant region\n    and a part of the maze where the pointwise band is not broken (Methods, Controlling for\n    power, requires a region with and a region without). Reproduced when the fraction is within\n    tolerance under one combination; partially reproduced when it is outside tolerance but above\n    the 1% the test gives under its null (one-sided binomial test, p < 0.05).\n- id: fig5a-session-selective-connections\n  statement: In the layer 2/3 session of Figure 3d, 15 of 36 excitatory connections are active\n    selectively in maze segments of left or right trajectories.\n  source: Figure 5a legend\n  quote: Putative monosynaptic connections that were active selectively in maze segments during\n    left or right turn trajectories (15 of 36 excitatory connections; same set of neurons, and\n    session, as in Fig. 3d)\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig4-position-dependence\n  - fig3b-session-connections\n  expected:\n  - quantity: excitatory connections in the session\n    value: 36\n    tolerance: 3.6\n  - quantity: connections with position or trajectory selective excess coincidences\n    value: 15\n    tolerance: 1.5\n  criterion: The method and readings of fig4-position-dependence, on the session of Figure 3d.\n    Figure 3b reports 48 connections with a pyramidal reference cell in the same session; the\n    paper does not say how the 36 relate to them (excitatory connections between identified\n    cells, or a stricter set), and the readings that give each are reported. Reproduced when both\n    counts are within tolerance under one combination; partially reproduced when the fraction\n    15/36 (41.7%, tolerance 4.2 points) is within tolerance but the counts are not.\n- id: fig4-pair-156-136\n  statement: Pair 156-136, on different shanks, keeps steady firing rates between positions 0.2\n    and 0.5 on left trials, yet excess short-latency coincidences occur only between 0.4 and 0.6.\n  source: Figure 4; Results, Behavioral modulation of monosynaptic interactions, paragraph 2\n  quote: cell pair 156-136, recorded from different electrode shanks, maintained steady firing\n    rates between maze segments 0.2 and 0.5, yet short-latency coincident spikes significantly in\n    excess of firing rate-controlled coincidences (the 'expected coincidence rate') occurred only\n    between maze locations 0.4 and 0.6\n  statistics:\n  - test: jitter test with global bands, one-sided\n    p: 0.01\n    p_relation: \"<\"\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  expected:\n  - quantity: start of the significant region\n    value: 0.4\n    tolerance: 0.04\n    unit: normalised position\n  - quantity: end of the significant region\n    value: 0.6\n    tolerance: 0.06\n    unit: normalised position\n  criterion: Cells 156 (presynaptic, putative pyramidal) and 136 (putative interneuron) in the\n    session of Figure 3d, left trials (Figure 4a legend), position of excess coincidences as in\n    the shared method at global P < 0.01, extent by the pointwise band. Reproduced when the only\n    significant region starts and ends within tolerance, and each cell's PSTH between 0.2 and 0.5\n    varies by less than 50% of its maximum there (a standard choice for \"steady\"). Cell numbers\n    are the paper's; whether the datasets use the same numbering is the author's to find; if the\n    pair cannot be identified the claim is blocked (data_missing).\n- id: fig5b-example-pairs\n  statement: In pair 197-201 transmission is significant only between 0.4 and 0.5 of left trials\n    although the expected coincidence rate is as high from 0 to 0.5; pair 49-52 transmits only on\n    left trials; pair 186-201 transmits only toward the end of the right arm although expected\n    coincidences are higher earlier.\n  source: Figure 5b; Results, Behavioral modulation of monosynaptic interactions, paragraph 2\n  quote: in pair 197-201, the expected coincidence rate was equally high between maze locations 0\n    and 0.5 of the left trials, yet significant spike transmission was detected only between maze\n    locations 0.4 and 0.5 (Fig. 5b). In pair 49-52, the expected coincidence rate in the first two\n    segments was equally high on left and on right trajectory trials, yet significant spike\n    transmission was detected only on left trajectory trials. In pair 186-201, significant\n    effects were observed only toward the end of the right arm\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  expected:\n  - quantity: pair 197-201, start of the significant region, left trials\n    value: 0.4\n    tolerance: 0.04\n    unit: normalised position\n  - quantity: pair 197-201, end of the significant region, left trials\n    value: 0.5\n    tolerance: 0.05\n    unit: normalised position\n  criterion: As fig4-pair-156-136, in the same session. Reproduced when 197-201 meets its expected\n    values on left trials, 49-52 has a significant region on left and none on right trials, and\n    186-201 has its only significant region on right trials beyond position 0.75 (a standard\n    reading of \"toward the end of the right arm\"). Partially reproduced when two of the three\n    pairs hold.\n- id: thinning-preserves-dependence\n  statement: In several pairs, position-dependent transmission remains after spikes are thinned so\n    that both cells fire at a flat rate over the region examined.\n  source: Results, Behavioral modulation of monosynaptic interactions, paragraph 1; Methods,\n    Controlling for power; Supplementary Figure 13\n  quote: Applying this approach, we indeed found that in several cases, the conclusion of\n    position-dependent synaptic efficacy remained unaltered after thinning\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig4-position-dependence\n  criterion: Per the Methods, for a pair and a region with enough firing and differential\n    coincidences, spikes are removed one at a time, chosen at random within [-s, +s] around the\n    PSTH maximum (s = 0.05, the kernel bandwidth), until the PSTH minimum is within 10% of the\n    maximum, for both cells; then the position test of the shared method. The region is open (the\n    paper chose it per example); readings (a) positions 0.2 to 0.5 as in Supplementary Figure\n    13A, (b) for each position-dependent pair, the smallest span holding its significant region\n    and an equal length of non-significant maze next to it. Thinning is random; ten repetitions\n    with fixed seeds. Reproduced when at least two pairs (a standard reading of \"several\"; the\n    paper gives no number) keep, in the majority of repetitions, a globally significant region and\n    a non-significant part of the region under one reading.\n- id: fig6-facilitation-depression\n  statement: Comparing first spikes of trains with later spikes, about equal shares of pairs show\n    depressing (12.7%) and facilitating (10.7%) spike transmission; 32.2% of the significant pairs\n    are on different shanks.\n  source: Figure 6c; Results, Behavioral modulation of monosynaptic interactions, paragraph 4\n  quote: we found that approximately equal percentages of neuron pairs showed firing\n    pattern-dependent depressing (12.7%) and facilitating (10.7%) effects (Fig. 6c)\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3-connection-rates\n  expected:\n  - quantity: pairs with significant depression\n    value: 12.7\n    tolerance: 1.27\n    unit: percent\n  - quantity: pairs with significant facilitation\n    value: 10.7\n    tolerance: 1.07\n    unit: percent\n  - quantity: significant pairs on different shanks\n    value: 32.2\n    tolerance: 3.22\n    unit: percent\n  criterion: Presynaptic spikes labelled first (preceded by more than 200 ms without spikes) or\n    second-and-later (less than 40 ms after the previous spike) (Results; Figure 6b legend). For\n    each label, the standardized peak height (h minus the jitter mean, over the jitter s.d.;\n    Supplementary Figure 9B), the jitter as in the shared method. The difference of the two\n    heights; labels shuffled for a two-sided permutation test at P < 0.10 (Figure 6c legend,\n    Supplementary Figure 16); depression is first above later. Open details and readings. Pairs;\n    (a) the excitatory connections, (b) all connections (Figure 6c says \"all neuron pairs\"). The\n    peak height h; (i) the largest bin in [1, 4] ms, (ii) the sum over [1, 4] ms. Whether a later\n    spike must belong to a train begun after 200 ms of silence; (x) yes, (y) any spike within 40\n    ms of the previous. The number of permutations (Supplementary Figure 16, R) is not given; a\n    standard 1,000. Reproduced when all three values are within tolerance under one combination;\n    partially reproduced when the two fractions are each above the 5% the test gives each side\n    under its null (one-sided binomial test, p < 0.05) but not all within tolerance.\n- id: fig6b-convergent-examples\n  statement: Two putative pyramidal cells converging on one layer 2/3 interneuron behave\n    oppositely; cell 197 depresses with spike repetition while the first spikes of cell 186 are\n    ineffective and its later spikes drive the interneuron.\n  source: Figure 6b; Results, Behavioral modulation of monosynaptic interactions, paragraphs 3 and\n    4; Supplementary Figure 14\n  quote: Figure 6b shows a putative layer 2/3 interneuron innervated by two pyramidal cells, with\n    ... pyramidal cell 197 showing a depressing effect with spike repetition. In contrast, the\n    first spike of spike trains of cell 186 was ineffective\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig6-facilitation-depression\n  criterion: Cells 197 and 186 onto 201 (Supplementary Figure 14) in the Figure 3d session, with\n    the measure of fig6-facilitation-depression. Reproduced when 197-201 has a first-spike height\n    above its later-spike height and 186-201 the reverse, each significant at P < 0.10 under one\n    of its readings; partially reproduced when both differences have these signs but one is not\n    significant.\n- id: fig7-supralinear\n  statement: Coincident spikes of two or more presynaptic cells within 5 ms discharge their common\n    target interneuron supralinearly, more than the sum of their separate effects, while\n    coincidences in windows over 10 ms add only linearly; group data come from 14 satellites.\n  source: Figure 7a and 7b; Results, Behavioral modulation of monosynaptic interactions, paragraph\n    5; Discussion, Behavior-dependence of short-term plasticity in mPFC, paragraph 3\n  quote: Coincident discharge of two presynaptic neurons within 5 ms was more effective than the\n    sum of the effects of nonsynchronous spikes (Fig. 7a), and coincidence of three or four spikes\n    resulted in a supralinear effect in various independently tested cell assemblies (Fig. 7b)\n    ... showed only a linear additive effect on the cooperative ability of presynaptic neurons to\n    discharge a postsynaptic partner\n  datasets:\n  - \"000067\"\n  - crcns-pfc-2\n  depends_on:\n  - fig3-cell-classes\n  expected:\n    quantity: satellites (putative pyramidal cells converging on one interneuron)\n    value: 14\n    tolerance: 1.4\n  criterion: A satellite is a putative interneuron with its convergent excitatory presynaptic\n    putative pyramidal cells (Figure 7a). For each event, the number of coincident spikes within\n    the window (2, 5, 10 and 20 ms, Figure 7a), and the spike transmission probability, the\n    fraction of events followed by a target spike 1 to 4 ms after the last presynaptic spike (the\n    lag of the Methods). Open details and readings. The minimum number of presynaptic cells in a\n    satellite; S-a two, S-b three (the satellite count of 14 is the check). Whether k counts\n    spikes or distinct presynaptic cells; both are run. Supralinear is (a) above k times the\n    one-spike probability, the literal \"sum of the effects\"; (b) above 1 - (1 - p1)^k, the\n    probability of independent effects. The paper reports no test. Reproduced when, under one\n    reading, with 5 ms windows the mean over satellites (Figure 7b) is above the linear prediction\n    for 2 and for 3 coincident spikes in most satellites, with 20 ms windows it is not above the\n    prediction by more than its s.d. over satellites, and the number of satellites is within\n    tolerance of 14 (Figure 7b, n = 14); partially reproduced when the 5 ms part holds alone.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  uv run --quiet python tools/claims_check.py claims/fujisawa-2008.yaml paper/10.1038-nn.2134.txt; echo exit $?; grep -n "rather\|—" claims/fujisawa-2008.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -nE "^[^#]*\S: " claims/fujisawa-2008.yaml | grep -vE "^[0-9]+:\s*(- )?[a-z_]+: " | head; uv run --quiet python -c "
import yaml;d=yaml.safe_load(open('claims/fujisawa-2008.yaml'));c=d['claims']
print(len(c),sum('criterion' in x for x in c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c))"
```

```
33 33 4 7
```

**Agent**

I've written `claims/fujisawa-2008.yaml`: 33 claims, one of them the `channel-region-link` link check on 000067. The quote checker passes with 0 problems. Nothing is committed.

**Text read.** The version of record (main text, figure legends, Methods) and its supplement (Supplementary Note, legends of Supplementary Figures 1 to 16). I opened PDF pages only for Figures 2d/e and 3b and Supplementary Figures 1 to 3 and 11. The paper links no analysis code; its only link is to the KlustaKwik spike sorter.

**Counts.**
- 32 claims have quotes; the link check has none.
- 4 claims carry statistics, 7 entries in all: three t-tests in Figure 2d and 2e, the permutation test for the path divergence, and the jitter test for pair 156-136.
- All 33 have criteria.
- Every claim rests on both datasets, except the link check, which rests on 000067 alone.

**Ids.** Ids from the two old files are kept and mapped in the opening comment. Two old claims are split: 000067's `fig2b-trajectory-selective` into the side-arm and central-arm claims, and its `ee188-example-session` into six session and pair claims. Two claims are new: `fig2d-layer-rates` and `fig2e-layer-discrimination`.

**Corrections to the earlier reading.**
- The text's "1172 pairs" and "n ~ 1422" are 117² and 142² in the PDF.
- Supplementary Figure 1 names the rats E, F, G and H, with F in layer 5. The earlier files did not have this.
- Figure 2d prints the unit counts: 411 in layer 2/3 and 222 in layer 5. Its pyramidal and interneuron counts (218 and 84 of 633) give 34.4% and 13.3%, not the 32.5% and 12.5% the Results state. I recorded this as a variant.

**Details the paper leaves open, with the readings named:**
- **Which dataset rat is which:** R-a, the datasets' EE, FF and GG are the paper's E, F and G (FF in layer 5, rat H missing); R-b, the names are unlinked and at most one rat is layer 5.
- **Trials:** correct trials only, or all trials.
- **Rate for widths and peaks:** occupancy-normalised (Figure 1c legend) or the Methods' density per trial.
- **Cross-correlogram bin width:** 1 ms or 0.5 ms.
- **How the "2 ms or less" peak width is applied:** the band test alone, or a pointwise run of 2 ms or less.
- **Units with both a peak and a trough:** unclassified, or left out of the denominators.
- **Which sessions:** the Figure 2a sessions, or all sessions (for the active fraction, field width, population vectors, odor, previous-trial coding and class fractions).
- **Field width:**
  - PSTH: all trials, left and right as two entries, or the side with the higher peak.
  - Width: the contiguous run around the peak, or the total length above 50%.
- **Odor and Figure 2d/e t-tests:** Student's or Welch's.
- **Figure 2d rate period:** trials only, or the whole session.
- **Figure 2e mean:** all neurons, or selective neurons only.
- **Cell-ratio average:** per session, per rat, or pooled.
- **Denominators:** for the reciprocal fraction, directed or unordered pairs; for pyramidal-to-pyramidal connections, all pairs or pyramidal pairs only.
- **Direction for the nearby pyramidal-interneuron probability:** one direction over directed pairs, or either direction over unordered pairs.
- **Session counts:** directed connections or distinct reference cells.
- **Position dependence:**
  - Trials: left and right apart, or together.
  - What counts: any significant region, or a significant region plus a non-significant one.
- **Thinning region:** positions 0.2 to 0.5, or one span per pair.
- **Facilitation and depression:**
  - Pairs: excitatory only, or all connections.
  - Peak height: the largest bin, or the sum over 1 to 4 ms.
  - Later spikes: inside a train begun after 200 ms of silence, or any spike within 40 ms.
- **Satellites:**
  - Size: two or more presynaptic cells, or three or more.
  - Count: spikes, or distinct cells.
  - The linear baseline: k times the one-spike probability, or independent summation.
- **Minor details given standard choices:** numbers of permutations and surrogates (1,000), the evaluation grid, and thresholds for "steady", "relatively constant", "small" and "several".

**Missing for the claims that need it:**
- Only three of the paper's four rats are in the data, so totals are judged as fractions or per rat.
- Task performance needs error trials. The CRCNS description lists correct trials only, so that claim may end up blocked.
- The paper does not give how soma positions are estimated (Figure 3c), so distance is measured by shank separation.
- Figure 7 reports no test.
- Fig. 2d and 2e bar heights are read off the figure, so the files report them without judging them.

## End of run

30 turns, 7 minutes, $2.56 at API prices, result: success.
