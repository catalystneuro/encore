# silkuniene-2025 · claims · run 42839207930

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls; ls paper; ls claims/silkuniene-2025; wc -l docs/protocol.md; grep -n '^#' docs/protocol.md
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
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
scripts
[... 33 more lines not kept]
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
cd  cat claims/fouke-2025.yaml | head -150; cat papers/datasets/silkuniene-2025.yaml; head -30 paper/*.txt; wc -w paper/*.txt
```

**Agent calls Bash**

```bash
cd  cat claims/silkuniene-2025/*.yaml
```

Result: not kept, because it reads the paper's text.

```
Exit code 1
bwrap: Can't get type of source .git/config.worktree.lock: No such file or directory
```

**Agent calls Bash**

```bash
cd  ls claims/silkuniene-2025/; wc -l claims/silkuniene-2025/*
```

```
001047.yaml
001276.yaml
001277.yaml
  526 claims/silkuniene-2025/001047.yaml
  536 claims/silkuniene-2025/001276.yaml
  436 claims/silkuniene-2025/001277.yaml
 1498 total
```

**Agent calls Read**

```json
{
 "file_path": "claims/silkuniene-2025/001047.yaml"
}
```

```
1	# Claims for Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025), Bioelectrochemistry 166,
2	# 109016, on dandiset 001047.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
4	# docs/protocol.md version pilot-10, as the reader.
5	#
6	# Text read. The NIH author manuscript (NIHMS2087238, PMC12331426) as served by PMC: abstract, main
7	# text, Materials and methods, Results, Discussion and figure legends (Figures 1 to 7), in
8	# paper/10.1016-j.bioelechem.2025.109016.txt. PMC lists no supplement and the text cites none. The
9	# version of record was not read. There is no PDF, so Figures 1 to 7 were not seen; values shown only
10	# in a figure (the packet rates tested, the burst numbers, the measured distances, per-group means)
11	# are not known here and no claim rests on reading them from a figure.
12	#
13	# Code. The paper links no code; its Data availability says "Data will be made available on
14	# request". It names the software: MetaMorph 7.8.13 for intensities, RStudio, Excel and Grapher 16
15	# for processing, fits and plots, Sim4Life Lite 7.0.1.8169 for the field. No repository was read, so
16	# no method detail below is settled by code.
17	#
18	# The dandiset. Its title on DANDI (version 0.250701.1609) is "Optimizing NG-CanCan Protocol Delivery
19	# with MHz Compression to Minimize Near-Electrode Ablation", species house mouse and Chinese hamster,
20	# and it names this paper (IsPublishedIn). It is taken to hold the monolayer images of this paper (CT26
[... 507 more lines not kept]
```

**Agent**

I've read the protocol and the earlier 001047 claims file. Next I'm reading the other two per-dataset files and the paper.

**Agent calls Read**

```json
{
 "file_path": "claims/silkuniene-2025/001276.yaml"
}
```

```
1	# Claims for Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025) on dandiset 001276.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the accepted author manuscript in PubMed Central (PMC12331426, NIHMS2087238), full
6	# text with Methods and figure legends, as fetched to paper/. The version of record was not read.
7	# PMC lists no supplement for this paper and the text cites none. No PDF was available, so the
8	# figures were not seen; numbers are taken from the text and legends only. The paper links no
9	# code ("Data will be made available on request"), so no code was read.
10	#
11	# Data the paper describes. Confluent monolayers of CT26 mouse colon carcinoma cells and CHO-K1
12	# cells in 6-well plates, stained with Hoechst 33342 before exposure (uniformity check) and with
13	# 1 uM YO-PRO-1 (YP) present during exposure, imaged 30 min later as stitched whole-well images
14	# (4x objective, FITC cube for YP, DAPI cube for Hoechst). In cell-killing experiments wells were
15	# also stained with propidium (Pr) 2 h after exposure (Cy3 cube). Four hollow needle electrodes
16	# (2.8 mm outer diameter) form a square with 15.3 mm side-to-side diagonals (Methods 2.2); 6 and
17	# 7 mm from the center along a diagonal are 1.65 and 0.65 mm from an electrode (Results 3.1). The
18	# dandiset's description gives an inter-electrode distance of 10.0 mm, which agrees with this
19	# geometry if read as the edge-to-edge distance along a side (10.0 + 2.8 = 12.8 mm between
20	# centers, 12.8 x 1.414 - 2.8 = 15.3 mm along the diagonal). Pulses are 600 ns (300 and 900 ns in
[... 517 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/silkuniene-2025/001277.yaml"
}
```

```
1	# Claims for Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025) on dandiset 001277.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22,
3	# protocol as stated in docs/protocol.md.
4	#
5	# Source: the accepted author manuscript in PubMed Central (PMC12331426, NIHMS2087238), full
6	# text as served by ncbi_pmc, read from its Methods, Results and figure legends. PMC lists no
7	# supplement and the text cites none. No PDF was stored, so the figures were not seen; numbers
8	# shown only in figures could not be read and are not claimed. The paper links no code (its
9	# Data availability says "Data will be made available on request"); analysis was done in
10	# MetaMorph 7.8.13, RStudio, Excel and Grapher 16, with no scripts given.
11	#
12	# Data the paper reports. Monolayers of CT26 mouse colon carcinoma cells (all experiments) and
13	# CHO-K1 cells (burst-number experiments only), in 6-well plates. Four hollow needle electrodes
14	# (2.8 mm outer diameter) in a square with 15.3-mm side-to-side diagonals, touching the dish
15	# bottom unless raised by 1 or 2 mm (Fig. 5). Each well was stained with Hoechst before
16	# exposure, exposed in 1 uM YO-PRO-1 (YP), incubated 30 min, rinsed and imaged as one stitched
17	# whole-well image (4x, FITC cube; Hoechst with DAPI cube). In cell-killing experiments the
18	# wells were also stained with propidium (Pr) 2 h later and imaged with a Cy3 cube, and
19	# re-imaged for Hoechst. Measured variable is the background-subtracted fluorescence in
20	# 325 x 406 um ROIs along the two diagonals (and in one set along lines through the centre
[... 417 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.bioelechem.2025.109016.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text is all there: the author manuscript with Methods and legends, no supplement listed, no PDF. Now checking what each of the four datasets is meant to hold.

**Agent calls Bash**

```bash
cd  cat papers/datasets/silkuniene-2025.yaml; git show --stat HEAD | head -20; ls targets | head; grep -rl "001284\|001047\|001276\|001277" --include=*.yaml targets queue papers 2>/dev/null | head -20
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1016/j.bioelechem.2025.109016
datasets:
- archive: dandi
  id: '001047'
  relation: primary
- archive: dandi
  id: '001276'
  relation: primary
- archive: dandi
  id: '001277'
  relation: primary
- archive: dandi
  id: 001284
  relation: primary
commit ff729c5ddfddab918cffdb4d0c8ef8e2fe5d6e30
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Tue Nov 10 09:56:16 2026 -0500

[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat papers/match/001284.yaml; ls papers/match | grep -E "001047|001276|001277"; python3 -c "
import json
d=json.load(open('targets/dandisets.json'))
items = d if isinstance(d,list) else d.get('dandisets', d)
for x in (items if isinstance(items,list) else items.values()):
    s=json.dumps(x)
    if any(k in s for k in ['\"001047','\"001276','\"001277','\"001284']):
        print(s[:1500]); print()
"
```

```
# Whether each paper DANDI:001284 names is the paper behind its data (tools/paper_match.py, docs/pipeline.md step 1).
schema_version: 1
dataset:
  archive: dandi
  id: 001284
date: '2026-11-10'
papers:
- doi: 10.1016/j.bioelechem.2025.109016
  relation: IsPublishedIn
  checks:
    text: true
    title_in_text: true
    names_this: false
    names_others: []
  verdict: partial
  by: agent
  reason: The dataset holds the pseudo-3D experiment of the paper (electrodes at 0, 1 or 2 mm above CT26 monolayers, YO-PRO-1 and propidium imaging), which is Fig. 5. The paper's other experiments (packet repetition rate, pulse duration, number of bursts, CHO cells) are not described in the dataset, whose only species is mouse.
  evidence:
  - source: archive metadata
    quote: A pseudo-3D model was created by elevating the electrode array 0 mm, 1 mm, or 2 mm above the monolayer.
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
d=json.load(open('targets/dandisets.json'))
for x in d:
    if x.get('dandiset') in ('001047','001276','001277','001284'):
        print(x['dandiset'], x['name'], x.get('published_version'), x.get('species'), x.get('asset_count'))
"; grep -rn "001047\|001276\|001277" papers/manifest.yaml | head
```

```
Traceback (most recent call last):
  File "<string>", line 5, in <module>
    if x.get('dandiset') in ('001047','001276','001277','001284'):
       ^^^^^
AttributeError: 'str' object has no attribute 'get'
1297:  '001047':
1605:  '001276':
1612:  '001277':
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
d=json.load(open('targets/dandisets.json'))
L=[v for v in (d.values() if isinstance(d,dict) else d) if isinstance(v,list)]
for lst in L:
  for x in lst:
    if isinstance(x,dict) and x.get('dandiset') in ('001047','001276','001277','001284'):
        print(x['dandiset'], '|', x['name'], '|', x.get('published_version'), x.get('species'), x.get('asset_count'))
"; ls paper/; ls questions | grep silk
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1290,1310p papers/manifest.yaml; sed -n 1600,1625p papers/manifest.yaml; ls questions/silkuniene-2025; head -c 3000 questions/silkuniene-2025/* 2>/dev/null
```

```
'001044':
  - doi: 10.1016/j.yebeh.2023.109120
    status: stored
    version: version of record
    source: PDF supplied by a person
    pdf: true
    supplements: 0
  '001047':
  - doi: 10.1016/j.bioelechem.2025.109016
    status: stored
    version: as served by ncbi_pmc
    source: ncbi_pmc+crossref (paper-text-fetcher)
    pdf: false
    supplements: 0
  001048:
  - doi: 10.1016/j.xcrp.2025.102660
    status: stored
    version: as served by europe_pmc
    source: europe_pmc+crossref (paper-text-fetcher)
    pdf: false
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
for d in 001047 001276 001277 001284; do echo "== $d"; curl -s --max-time 20 "https://api.dandiarchive.org/api/dandisets/$d/versions/draft/info/" | python3 -c "import json,sys; m=json.load(sys.stdin)['metadata']; print(m.get('name')); print(m.get('description'))"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  ls schemas; python3 - <<'E'
import json,glob
for f in glob.glob('schemas/*claim*'):
    print(f)
    s=json.load(open(f)) if f.endswith('.json') else None
    if s:
        props=s.get('$defs',{}) 
        print(json.dumps(s,indent=1)[:200])
E
grep -n "datasets\|elsewhere\|with_inputs\|not available\|blocked" schemas/*claim* | head -40; grep -rln "^  datasets:" claims/*.yaml | head -3
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
schemas/claims.schema.json
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "Claims proposed for one target (a dataset and one of its papers)",
 "description": "Draft. To be revised after the pilot.",
 "t
139:            "description": "What the claim's test uses: the dataset alone (`dataset`, the default); the dataset with names for its own codes taken from elsewhere (`with_labels`), which counts as the dataset; the dataset with other data from elsewhere (`with_inputs`), which is counted apart; or data the paper deposited in another public archive, which the dataset does not hold (`elsewhere`), counted apart from both. Outside sources that a test uses are listed under `inputs` in the attempt.",
143:              "with_inputs",
144:              "elsewhere"
148:            "description": "For a claim with data `elsewhere`: the archive and the pinned identifier of the data, e.g. 'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
152:          "datasets": {
193:                  "const": "elsewhere"
claims/kim-2022.yaml
claims/pakhomov-2023.yaml
```

**Agent calls Bash**

```bash
cd  sed -n 1,60p schemas/claims.schema.json; sed -n 130,230p schemas/claims.schema.json; head -60 claims/pakhomov-2023.yaml; grep -n "datasets:" -A3 claims/pakhomov-2023.yaml | head -40
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
[... 241 more lines not kept]
```

**Agent**

The sister paper (pakhomov-2023) already has a combined file in this format, so I'll follow its layout. Reading its header and a few claims.

**Agent calls Read**

```json
{
 "file_path": "claims/pakhomov-2023.yaml",
 "offset": 60,
 "limit": 110
}
```

```
60	# - Electric field simulations (Fig. 3; Methods 2.3) in Sim4Life, as in the paper's reference 15
61	#   (doi:10.1016/j.bioelechem.2021.107876). Model outputs, not recordings.
62	#
63	# Statistics (Methods 2.4). "Two-sided Student's t-test", p < 0.05, the only test the paper
64	# names; Student's names the equal-variance form, and Welch's form is a variant only. Between
65	# treatments the groups are different dishes, so the test is unpaired. In the figures,
66	# significance is read from the gap between error bars (a gap longer than the bars means
67	# p < 0.05); this rule is shown as a variant where a claim rests on a figure. Methods 2.2 names no
68	# test for the single cells; the Methods 2.4 test is used for them, and this is a reading.
69	#
70	# Details the paper leaves open, with the readings it allows. A criterion that uses one says so.
71	# For an expected value, the claim holds when it matches under any combination of readings. For a
72	# test, the outcome is the one all readings give; when they differ, the author adopts the reading
73	# the paper best supports, as an assumption, or blocks the claim as methods_underspecified, with
74	# every result shown.
75	# (O1) ROI layout. 92 (small) or 224 (large) ROIs "along one or both diagonals" over the stated
76	#      range. Readings (a) the count is for one diagonal, spacing about 36 um (small) or 33 um
77	#      (large); (b) the count is split over two diagonals, about 72 um or 65 um. The count and
78	#      range fix the ROI length along the diagonal under each reading; the extent across the
79	#      diagonal is not given. Readings (w1) square ROIs, side equal to the spacing (a standard
[... 90 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 60,130p schemas/claims.schema.json; sed -n 230,300p schemas/claims.schema.json; sed -n 1,40p tools/claims_check.py
```

```
"claims": {
      "type": "array",
      "minItems": 1,
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": [
          "id",
          "statement",
          "source"
        ],
        "properties": {
          "id": {
            "description": "Stable within the file, e.g. fig2b.",
            "type": "string",
            "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"
          },
          "statement": {
            "description": "The finding in one or two sentences, in words. Not a copy of the figure.",
            "type": "string",
[... 160 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/silkuniene-2025.yaml",
 "content": "# Claims for Silkuniene, Silkunas, Pakhomova, Semenov & Pakhomov (2025), \"MHz compression of pulse\n# packets facilitates remote focusing of electroporation\", Bioelectrochemistry 166, 109016, tested on\n# dandisets 001047, 001276, 001277 and 001284.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-10,\n# protocol pilot-14 as stated in docs/protocol.md. It replaces the three files written 2026-10-22\n# under pilot-10, one per dataset (claims/silkuniene-2025/001047.yaml, 001276.yaml, 001277.yaml);\n# ids are kept where the finding is the same, taken from the file of the dataset that holds the\n# figure (Figs. 3 to 5 from 001047, Fig. 6 from 001277, Fig. 7 from 001276).\n#\n# Text read. The accepted author manuscript in PubMed Central (PMC12331426, NIHMS2087238), as served\n# by ncbi_pmc, in paper/10.1016-j.bioelechem.2025.109016.txt: abstract, Introduction, Materials and\n# methods 2.1 to 2.5, Results 3.1 to 3.4, Discussion, Conclusion and the legends of Figs. 1 to 7.\n# It is not the version of record. The paper has no supplement (PMC marks \"has-supplement no\" and\n# the text cites none). No PDF was supplied, so no figure was seen; values printed only in a figure\n# (the packet rates other than 1 Hz, 1 kHz, 10 kHz and 0.2 MHz, the ROI positions, the zones of Fig.\n# 5C, axis values) are not used.\n#\n# Code. The paper links no code and no data deposit (\"Data will be made available on request\").\n# It names the software only: MetaMorph 7.8.13 for intensities, RStudio, Excel and Grapher 16 for\n# processing, fits and graphs, Sim4Life Lite 7.0.1.8169 for the field. No repository was read, so no\n# method detail below is settled by code.\n#\n# The datasets, from their titles and descriptions on DANDI (draft metadata, read 2026-11-10).\n# - 001047, \"Optimizing NG-CanCan Protocol Delivery with MHz Compression to Minimize Near-Electrode\n#   Ablation\"; packets at 0.2 MHz against 1 Hz, YP and propidium. The packet-rate series of Figs. 3\n#   and 4 rest on it. Its description also names propidium two hours after delivery, which in the\n#   paper is measured only in the Fig. 5 series, so the 0-mm Fig. 5 claims list it as well.\n# - 001276, \"... Impact of Burst Number Variation ...\"; 0.2 MHz, 600 ns, 1, 2, 4 or 6 bursts,\n#   Hoechst and YP. The Fig. 7 series.\n# - 001277, \"... Impact of Pulse Duration and Protocol Delivery Frequency\"; 300, 600 and 900 ns, 18,\n#   9 or 6 packets, repeated twice, Hoechst and YP. The Fig. 6 series.\n# - 001284, \"... Focused Cell Electroporation and Ablation in a Pseudo-3D Model\"; electrodes 0, 1 or\n#   2 mm above the monolayer, YP and propidium. The Fig. 5 series.\n# - No description names the thermochromic film images (Fig. 2) or the field simulation (Fig. 1).\n#   Those claims list all four datasets; the author checks each and blocks the claim as data_missing\n#   when none holds the data. The descriptions give a 10-mm inter-electrode spacing; with the\n#   paper's geometry this is the edge-to-edge distance along a side (12.8 mm between centres minus\n#   2.8 mm), and the paper's 15.3-mm diagonal is used throughout.\n#\n# Data the paper used, as it reports them. Confluent monolayers of CT26 mouse colon carcinoma cells\n# (all series) and CHO-K1 cells (Fig. 7 only) in 6-well plates. Four hollow needle electrodes, 2.8 mm\n# outer diameter, in a square with 15.3-mm side-to-side diagonals (Methods 2.2), touching the\n# monolayer unless raised 1 or 2 mm (Fig. 5); 6 and 7 mm from the centre along a diagonal are 1.65\n# and 0.65 mm from an electrode (Results 3.1). Packets of 16 pulses (Fig. 1B), first pulse 7.2 kV,\n# later pairs 12.5% lower per phase; 9 packets per burst, bursts at 1 Hz, rotated over 4 directions\n# (\"2 bursts (x4)\" is 8 bursts). Controls deliver only the first pulse of each packet. Each well is\n# imaged as one stitched image (4x, 0.16 NA): Hoechst 33342 (DAPI cube) before exposure, YO-PRO-1\n# (YP, 1 uM, FITC cube) 30 min after exposure, and in killing experiments propidium (Pr, Cy3 cube) 2\n# h after, with Hoechst re-imaged (Methods 2.4). Series:\n# - (S1) Figs. 3 and 4. CT26, 600 ns, 2 bursts (x4), packet rates from 1 Hz to 0.208333 MHz\n#   (\"0.2 MHz\", no interval between packets) and control; n = 3 per CANCAN rate, n = 5 controls.\n#   The text names 1 Hz, 1 kHz, 10 kHz and 0.2 MHz; the Fig. 4C fit has n = 15 at n = 3 per rate\n#   below 0.2 MHz, so five rates below 0.2 MHz. One set also has ROIs parallel to the sides (Fig. 3C).\n# - (S2) Fig. 5. CT26, 0.2 MHz, 2 bursts (x4), electrodes at 0, 1 or 2 mm; YP n = 6 to 7, Pr n = 4\n#   to 5; high-resolution images of three zones (Fig. 5C).\n# - (S3) Fig. 6. CT26, packets of 300-, 600- or 900-ns pulses with no interval, 18, 9 or 6 packets\n#   per 43.2-us burst, 2 bursts (x4); n = 5 each.\n# - (S4) Fig. 7. CT26 (n = 3 to 5) and CHO (n = 4), 0.2 MHz, 600 ns; the text names 1, 2 and 6\n#   bursts (x4), and the 001276 description gives 1, 2, 4 and 6.\n# - (S5) Fig. 2. Thermochromic film after 2 and 6 bursts at 0.2 MHz without rotation.\n# - (S6) Fig. 1. Sim4Life field maps; model outputs, not recordings.\n#\n# Method fixed by the paper, cited by the criteria (Methods 2.5 unless noted).\n# (F1) Intensity is the mean fluorescence in 325 x 406 um ROIs placed along the diagonals of the\n#      square, connecting the electrode footprints, at signed distances x (mm) from the geometrical\n#      centre of the array; in one S1 set also along lines through the centre parallel to the sides.\n# (F2) Background is the mean of 3 ROIs inside an electrode footprint, subtracted from every ROI.\n# (F3) The two diagonals of a well are pooled as one experiment; n counts wells (also Fig. 3B and 4B\n#      legends). Data are mean +/- s.e. over experiments, in a.u. or in % of the centre value.\n# (F4) YP profiles are fitted with YP(x) = a (b/2)^2 / (x^2 + (b/2)^2), a the value at x = 0 and b\n#      the FWHM in mm. Pr profiles are fitted with Pr(x) = a exp(-x^2 / (2 sigma^2)), FWHM about\n#      2.4 sigma (Methods 2.5, which says Fig. 6 where the Gaussian appears in Fig. 5; the Fig. 5B\n#      legend fixes it for Pr). Fits are least squares in Grapher, the standard reading of \"fitted\".\n# (F5) FWHM per condition is the mean of the FWHM of Lorentzian fits to each experiment (Results 3.1;\n#      Fig. 4C and 6D legends). FWHM in % of the gap is FWHM / 15.3 mm (Fig. 4C legend, \"% of the\n#      diagonal distance between electrodes\"; Results 3.3 gives 1.7 mm as 11.1%).\n# (F6) Fitted ranges. -4 to 4 mm for Fig. 3 and the per-experiment fits of Fig. 4C (Results 3.1, Fig.\n#      3B legend); -5 to 5 mm for the mean profiles of Figs. 5B and 6B (legends, Results 3.2).\n# (F7) Tests. Two-sided Student's t-tests, with Bonferroni correction where several comparisons are\n#      made, or ANOVA, at p < 0.05. Groups are different wells, so t-tests are unpaired and\n#      equal-variance (Student's); Welch's form is a variant only. Slopes are tested by the\n#      two-sided one-sample t test of the regression slope (Fig. 4C, 6D and 7 legends).\n# (F8) The paper's reading of its graphs. \"A gap exceeding the length of the error bars indicates a\n#      significant difference at p<0.05\" (Methods 2.5, citing Cumming et al. 2007). Where the paper\n#      states a difference from a graph without a test, it is judged by this rule on mean +/- s.e.,\n#      and the t-test of F7 is reported.\n# (F9) Near electrodes is 6 and 7 mm from the centre toward an electrode (Results 3.1, Fig. 4B).\n# (F10) Fields from the paper's simulation, not from the data. 7.2 kV on one electrode gives 3.3\n#      kV/cm at the centre, 9.4 and 13.5 kV/cm at 6 and 7 mm toward it (Methods 2.2).\n#\n# Details the paper leaves open, with the readings it allows. A criterion that uses one says so. For\n# an expected value, the claim holds when it matches under any combination of readings (the paper\n# reports one number for a choice it leaves open). For a test, the outcome is the one all readings\n# give; when they differ, the author adopts the reading the paper best supports, as an assumption,\n# or blocks the claim as methods_underspecified, with every result shown. Claims of absence are\n# judged on the one test each names.\n# (O1) ROI positions along a diagonal are not given; the text names only whole-mm distances (0, 2,\n#      4, 5, 6, 7 mm). Positions are taken from the dataset when it holds them; otherwise readings\n#      (a) ROIs centred at whole-mm distances, 0 to 7 mm each way; (b) contiguous ROIs from the\n#      centre outward, one ROI length per step. Which side of the ROI (325 or 406 um) lies along the\n#      diagonal is not given; 406 um along the diagonal is a standard choice that moves a centre by\n#      under 0.05 mm. Which footprint holds the background ROIs is not given; any one, a standard\n#      choice.\n# (O2) Pooling of diagonals. Readings (a) the two diagonals averaged at each signed distance (the\n#      profiles run from -x to x in Figs. 3B, 5B, 6B); (b) all four half-diagonals averaged at each\n#      distance (Fig. 4A legend, \"measurements in 4 diagonal directions from the center were pooled\"),\n#      mirrored to -x for fitting.\n# (O3) Fit range of per-experiment fits where no figure fixes it. Methods say \"limited to 4-6 mm\".\n#      For Fig. 6D (\"as described in 3.1\") readings (a) -4 to 4 mm, (b) -5 to 5 mm (Fig. 6B\n#      legend); for Fig. 7 readings (a) 4, (b) 5, (c) 6 mm half-widths.\n# (O4) Points of a regression. Fig. 4C fits individual experiments (n = 15 for fitting). Figs. 6D\n#      and 7 do not say; readings (a) individual experiments, the one Fig. 4C supports, (b) group\n#      means.\n# (O5) Which near-electrode distance and which ratio give the reported centre to near-electrode\n#      ratios. Readings (a) 6 mm, (b) 7 mm (F9); (i) the ratio of group means, (ii) the mean of\n#      per-experiment ratios.\nschema_version: 2\npaper: doi:10.1016/j.bioelechem.2025.109016\nclaims:\n- id: fig1e-field-simulation\n  statement: In the simulation, 7.2 kV on one electrode gives 3.3 kV/cm in the centre of the array and\n    9.4 and 13.5 kV/cm at 6 and 7 mm from the centre toward the active electrode.\n  source: Methods 2.2, paragraph 4; Figure 1E\n  quote: Specifically, 7.2 kV applied to one electrode produced the electric field of 3.3 kV/cm in the\n    center, and 9.4 and 13.5 kV/cm at 6 and 7 mm from the center towards the active electrode,\n    respectively\n  datasets:\n  - \"001047\"\n  - \"001276\"\n  - \"001277\"\n  - \"001284\"\n  expected:\n  - quantity: field at the centre, 7.2 kV on one electrode\n    value: 3.3\n    tolerance: 0.33\n    unit: kV/cm\n  - quantity: field at 6 mm toward the active electrode\n    value: 9.4\n    tolerance: 0.94\n    unit: kV/cm\n  - quantity: field at 7 mm toward the active electrode\n    value: 13.5\n    tolerance: 1.35\n    unit: kV/cm\n  criterion: The values are outputs of the paper's Sim4Life Lite model (Methods 2.2, built as in its\n    references 16 and 18), which the paper does not deposit. The claim is tested only if a dataset\n    holds the simulated field maps; a field model built by the author is not the paper's and is not\n    a test. With the maps (1 kV on one electrode, scaled linearly to 7.2 kV as Methods 2.2 says),\n    reproduced when the three values are within tolerance along the diagonal from the active\n    electrode. Without them, blocked as data_missing.\n- id: fig2-heating-below-44c\n  statement: With packets at the maximum rate, heating followed the field and was largest near the\n    electrodes; after 2 bursts it was confined to about 2 mm next to the electrodes and could exceed\n    30 C but not 44 C; after 6 bursts it spread further, exceeding 30 C even near the centre, yet\n    never exceeded 44 C.\n  source: Methods 2.3, paragraph 1; Figure 2\n  quote: With 2 bursts ( Fig. 2A ), heating was restricted to an approximately 2-mm zone next to\n    electrodes, where it could reach over 30 °C but did not exceed 44 °C. With 6 bursts ( Fig. 2B ),\n    heating was more widespread ... Temperature could exceed 30 °C even near the center of the\n    array, but did not exceed 44 °C even near the electrodes.\n  datasets:\n  - \"001047\"\n  - \"001276\"\n  - \"001277\"\n  - \"001284\"\n  criterion: Set S5, film frames at the end of the 2nd and 6th burst (Methods 2.3). Temperature classes\n    from the calibrated colour transitions, black to red, green, blue and back to black at 25, 26, 30\n    and 44 C (Methods 2.3). The hue limits of the colours are not given; readings (a) red below 45,\n    green 75 to 165, blue 180 to 270 degrees of hue, (b) red below 30, green 90 to 150, blue 195 to\n    255 degrees, with black any pixel of HSV value below 0.2 (standard choices). Above 30 C is blue;\n    above 44 C is black after blue, a dark pixel enclosed by a blue region outside the electrode\n    footprints (dashed circles, Fig. 2 legend). \"Near the center\" is not given as a distance;\n    readings (a) within 1 mm, (b) within 2 mm of the centre. Reproduced when, under every reading,\n    the 2-burst image has blue pixels only within 2.2 mm of an electrode edge (\"approximately 2-mm\",\n    widened by 10%), the 6-burst image has blue pixels near the centre, and neither image has a dark\n    pixel enclosed by blue. Blocked as data_missing when no dataset holds the film images.\n- id: fig3a-centre-enhanced\n  statement: Every CANCAN protocol enhanced electroporation at the array centre, while in the control\n    (a single unipolar pulse per packet) YP uptake decreased gradually toward the centre.\n  source: Results 3.1, paragraph 2; Figure 3A\n  quote: All CANCAN protocols visibly enhanced electroporation at the center of the array, in\n    contrast to its gradual decrease toward the center in the control ( Fig. 3A ).\n  datasets:\n  - \"001047\"\n  criterion: Set S1, diagonal profiles by F1 to F3, under O1 and O2. The field at the centre is the\n    same in CANCAN and control (Methods 2.2), so enhanced at the centre is read as a central peak.\n    For each CANCAN rate, mean YP at x = 0 exceeds mean YP at 4 mm (the edge of the Fig. 3B fit\n    range) by a gap larger than the error bars (F8). For the control, mean YP at x = 0 is below the\n    means at 4, 6 and 7 mm by such a gap. Reproduced when both hold for every rate under every\n    reading; YP at 6 and 7 mm against x = 0 for each CANCAN rate is reported and judged in\n    fig4b-near-electrode-decline. The t-tests of F7 are reported.\n- id: fig3bc-rate-suppresses-off-target\n  statement: Raising the packet rate from 1 Hz to 0.2 MHz suppressed electroporation better both near\n    the electrodes (diagonal profile) and at the perimeter between electrodes (profile parallel to\n    the sides).\n  source: Results 3.1, paragraph 2; Figure 3B, 3C\n  quote: The most conspicuous effect of increasing the packet rate from 1 Hz to 0.208333 MHz\n    (abbreviated to 0.2 MHz below and in figure legends) was better suppression of electroporation\n    both near electrodes ( Fig. 3B ) and at the perimeter between electrodes ( Fig. 3C ).\n  datasets:\n  - \"001047\"\n  criterion: Set S1, F1 to F3, F8, F9, O1, O2. Near electrodes is YP at 6 and 7 mm on the diagonals.\n    The perimeter between electrodes is the end of the parallel profile, which meets the side of the\n    square about 6.4 mm from the centre (half the 12.8-mm side between electrode centres, from the\n    15.3-mm diagonal and 2.8-mm needles of Methods 2.2); readings (a) the outermost parallel ROIs,\n    (b) the parallel ROIs at 6 mm. Reproduced when, under every reading, mean YP at 0.2 MHz is below\n    that at 1 Hz by a gap larger than the error bars (F8) at 6 mm, at 7 mm and at the perimeter; the\n    two-sided t-tests (F7) are reported. The perimeter part is blocked as data_missing when the\n    dataset has no parallel measurements.\n- id: fig3-lorentzian-profile\n  statement: The decline of YP emission from the centre was bell-shaped and fitted a Lorentzian\n    function over -4 to 4 mm nearly perfectly (R > 0.9, p < 0.001) for every packet rate.\n  source: Results 3.1, paragraph 3; Figure 3B, 3C legend; Methods 2.5\n  quote: The fit correlation with data in the −4 to 4 mm radius was nearly perfect (R>0.9, p<0.001).\n  datasets:\n  - \"001047\"\n  statistics:\n  - about: correlation of the Lorentzian fit with the data, -4 to 4 mm\n    statistic: R > 0.9\n    p: 0.001\n    p_relation: \"<\"\n  - about: significance of each YP fit in Figures 3, 5 and 6 (Methods 2.5)\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n    quantity: correlation of fitted and measured mean YP, -4 to 4 mm, each rate and direction\n    value: 0.9\n    tolerance: 0\n  criterion: Set S1, CANCAN rates, F1 to F4, F6, O1, O2. The Lorentzian is fitted to the mean\n    diagonal profile over -4 to 4 mm (the dotted fits of Fig. 3B, drawn on mean +/- s.e.), and to the\n    mean parallel profile where present (Fig. 3C). How R is computed is not given; readings (a) the\n    Pearson correlation of fitted and measured values over the fitted points, with its t test; (b)\n    the square root of R2 = 1 - SSres/SStot, with the F test of the fit. Reproduced when R exceeds\n    0.9 with p < 0.001 for every rate and direction under every reading; 0.9 is the paper's bound,\n    so the tolerance is zero.\n- id: fig3-tail-deviation-falls-with-rate\n  statement: Beyond the fitted range, the data deviated from the Lorentzian fit less as the packet\n    rate increased.\n  source: Results 3.1, paragraph 3; Figure 3B, 3C\n  quote: The deviation of experimental data from the fits at larger distances from the center\n    diminished with increasing the packet repetition rate, highlighting better suppression of the\n    off-target electroporation.\n  datasets:\n  - \"001047\"\n  depends_on:\n  - fig3-lorentzian-profile\n  criterion: Set S1, the fits of fig3-lorentzian-profile extended to all distances (Fig. 3B legend,\n    the plots were extended to the x-axis limits). The paper gives no measure or test of the\n    deviation. The measure is the mean of (data - fit) over the ROIs beyond 4 mm; its units are not\n    given, readings (a) a.u., (b) percent of the fitted peak a. Reproduced when, under every\n    reading and in both directions, the deviation is largest at 1 Hz and smallest at 0.2 MHz, and\n    its Spearman correlation with rate over the tested rates is negative (a standard measure of a\n    monotone trend, as the paper names none). The value for every rate is reported.\n- id: fig4b-40-fold-ratio\n  statement: At 0.2 MHz, YP uptake at the centre was 40 times that near the electrodes, despite the\n    field there being about 4 times weaker (3.3 against about 14 kV/cm).\n  source: Results 3.1, paragraph 2; Figure 4A, 4B; Abstract\n  quote: Now, by increasing the packet repetition rate to 0.2 MHz, we achieved a 40-fold difference (\n    Fig. 4B ), despite using a bigger array with larger reduction of the electric field from\n    electrodes to the center.\n  datasets:\n  - \"001047\"\n  expected:\n    quantity: ratio of centre YP to near-electrode YP, CT26, 2 bursts (x4), 0.2 MHz\n    value: 40\n    tolerance: 4\n  criterion: Set S1 at 0.2 MHz, F1 to F3, F9, O2, O5. Background-subtracted YP at x = 0 over YP at\n    the near-electrode distance. Reproduced when the ratio is within 36 to 44 under one combination\n    of the readings of O2 and O5; every combination is shown. The fields are from the simulation\n    (F10) and are not tested here.\n- id: fig4b-centre-no-rate-effect\n  statement: YP uptake at the array centre showed no significant effect of packet rate.\n  source: Results 3.1, paragraph 4; Figure 4B\n  quote: YP intensity in the center showed no significant effect of the packet rate ( t -test with\n    Bonferroni correction, Fig. 4B ).\n  datasets:\n  - \"001047\"\n  criterion: A claim of absence, judged on the paper's test. Set S1, CANCAN rates, F1 to F3, O2;\n    per experiment the background-subtracted YP at x = 0. Two-sided Student's t-tests with\n    Bonferroni correction (F7). The comparisons are not named here; the test is each rate against 1\n    Hz, the family the Fig. 4C legend uses on the same experiments, with Bonferroni over the number\n    of rates compared with 1 Hz. Reproduced when no corrected comparison has p < 0.05; not\n    reproduced when any does. Group means and the largest ratio between rates are reported either\n    way; all pairs of rates are shown as a variant.\n- id: fig4b-near-electrode-decline\n  statement: In contrast to the centre, YP uptake at 6 and 7 mm from the centre (1.65 and 0.65 mm from\n    the electrodes) declined steeply as the packet rate increased.\n  source: Results 3.1, paragraph 4; Figure 4B\n  quote: It contrasted with a steep, packet rate-dependent decline of YP uptake at 6 and 7 mm from\n    the center (i.e., 1.65 and 0.65 mm from electrodes).\n  datasets:\n  - \"001047\"\n  criterion: Set S1, CANCAN rates, F1 to F3, O2. At 6 mm and at 7 mm, a power function YP = c rate^k\n    is fitted to YP against packet rate by least squares (Fig. 4B legend, \"best fits using power\n    function\"; Methods 2.5). Whether the fit uses the plotted means or the individual experiments is\n    not given; readings (a) group means, (b) per-experiment values. Reproduced when, under every\n    reading, k < 0 at both distances and mean YP at 0.2 MHz is below that at 1 Hz by a gap larger\n    than the error bars (F8) at both; the two-sided t-tests (F7) are reported.\n- id: fig4c-fwhm-falls-with-rate\n  statement: Higher packet rates focused electroporation into a smaller spot; the FWHM fell from about\n    4 mm at 1 Hz to about 2 mm at 1 kHz, 10 kHz and 0.2 MHz (p = 0.03, 0.02 and 0.09 against 1 Hz),\n    and could be under 15% of the gap between electrodes.\n  source: Results 3.1, paragraphs 5 and 6; Figure 4C\n  quote: FWHM decreased from ~4 mm at 1 Hz to ~2 mm at 1 kHz, 10 kHz, and 0.2 MHz packet rates (p =\n    0.03; 0.02, and 0.09, respectively; t -test with Bonferroni correction).\n  datasets:\n  - \"001047\"\n  statistics:\n  - about: 1 kHz against 1 Hz\n    test: t-test with Bonferroni correction\n    p: 0.03\n    corrected: Bonferroni\n    n: 3 experiments per rate\n  - about: 10 kHz against 1 Hz\n    test: t-test with Bonferroni correction\n    p: 0.02\n    corrected: Bonferroni\n    n: 3 experiments per rate\n  - about: 0.2 MHz against 1 Hz\n    test: t-test with Bonferroni correction\n    p: 0.09\n    corrected: Bonferroni\n    n: 3 experiments per rate\n  expected:\n  - quantity: mean FWHM at 1 Hz\n    value: 4\n    tolerance: 0.4\n    unit: mm\n  - quantity: mean FWHM at 1 kHz\n    value: 2\n    tolerance: 0.2\n    unit: mm\n  - quantity: mean FWHM at 10 kHz\n    value: 2\n    tolerance: 0.2\n    unit: mm\n  - quantity: mean FWHM at 0.2 MHz\n    value: 2\n    tolerance: 0.2\n    unit: mm\n  criterion: Set S1, CANCAN rates, F1 to F7, O1, O2. Per experiment, the Lorentzian fitted over -4 to\n    4 mm (Results 3.1) gives b; FWHM per rate is the mean over experiments (F5). Two-sided t-tests of\n    each rate against 1 Hz (Fig. 4C legend), Bonferroni over the rates compared with 1 Hz; the\n    number of comparisons is not given, readings (a) every other tested rate, (b) the three rates the\n    text names. Reproduced when the four means are within tolerance, 1 kHz and 10 kHz differ from 1\n    Hz at corrected p < 0.05 (the legend marks *p<0.05), and at least one rate has mean FWHM below\n    15% of 15.3 mm (2.3 mm). Partially reproduced when the tests hold but a mean is outside\n    tolerance. The 0.2 MHz comparison (p = 0.09) is reported, not required.\n- id: fig4c-log-trend\n  statement: FWHM fell logarithmically with packet rate from 1 Hz to 10 kHz (R = 0.77, p < 0.001; n =\n    15), with no further narrowing from 10 kHz to 0.2 MHz.\n  source: Results 3.1, paragraph 5; Figure 4C legend\n  quote: FWHM decrease followed the logarithmic dependence from 1 Hz to 10 kHz (correlation\n    coefficient R = 0.77, p<0.001), but there was no further focality increase when the packet rate\n    increased from 10 kHz to 0.2 MHz.\n  datasets:\n  - \"001047\"\n  statistics:\n  - about: log fit of FWHM against packet rate, 1 Hz to 10 kHz\n    test: correlation\n    statistic: R = 0.77\n    p: 0.001\n    p_relation: \"<\"\n    n: 15 experiments (0.2 MHz excluded)\n  - about: slope of the log fit (Fig. 4C legend)\n    test: 2-sided, one-sample t test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 15 experiments\n  expected:\n    quantity: correlation of FWHM with log packet rate, 1 Hz to 10 kHz\n    value: 0.77\n    tolerance: 0.077\n  depends_on:\n  - fig4c-fwhm-falls-with-rate\n  criterion: Per-experiment FWHM from fig4c-fwhm-falls-with-rate, rates 1 Hz to 10 kHz, 0.2 MHz left\n    out (Fig. 4C legend, n = 15 for fitting). FWHM = m log(rate) + c by least squares; R is the\n    absolute Pearson correlation of FWHM with log rate; the slope is tested by the two-sided\n    one-sample t test (legend). Reproduced when R is within tolerance, the slope is negative with p <\n    0.001, and mean FWHM at 0.2 MHz is not below that at 10 kHz by a gap larger than the error bars\n    (F8, the paper's reading for \"no further focality increase\"; the t-test is reported). Partially\n    reproduced when the slope is negative with p < 0.05 but R or p falls short.\n- id: fig5-raised-electrodes-weaken-centre\n  statement: Since with MHz-CANCAN there was practically no YP staining near electrodes (a finding the\n    text cites to Figure 4), the only clear effect of raising the electrodes 1 or 2 mm above the\n    monolayer was a weakening of electroporation in the central spot.\n  source: Results 3.2, paragraph 1; Figure 5A, 5B\n  quote: With MHz-CANCAN (CT26 cells, 2 bursts (x4), Fig. 4 ), there was practically no YP staining\n    near electrodes to start with, so the only clear effect of raising electrodes was the weakening\n    of electroporation in the central spot.\n  datasets:\n  - \"001284\"\n  criterion: Set S2, F1 to F3, F8, O1, O2. YP in percent of the mean 0-mm peak (Fig. 5B legend); the\n    centre is x = 0. The paper gives no test. Reproduced when mean centre YP at 1 mm and at 2 mm\n    elevation are each below that at 0 mm by a gap larger than the error bars (F8); two-sided t-tests\n    with Bonferroni over the two comparisons (F7) are reported. The near-electrode part is the Figure\n    4 finding, judged in fig4b-40-fold-ratio; mean YP at 6 and 7 mm at each elevation, in % of the\n    0-mm centre, is reported.\n- id: fig5ab-yp-spot-slightly-larger-than-pr\n  statement: The central spot of YP staining (electroporation) was only slightly larger than the spot\n    of Pr staining (cell killing).\n  source: Results 3.2, paragraph 1; Figure 5A, 5B\n  quote: Somewhat unexpectedly, the central spot of YP staining (electroporation) was just slightly\n    larger than the spot of Pr staining (cell killing; Fig 5A and B ).\n  datasets:\n  - \"001284\"\n  - \"001047\"\n  criterion: Set S2, F1 to F4, F6, O1, O2. Spot size is the FWHM, the paper's measure of spot size\n    (Results 3.1). FWHM of the Lorentzian fit to mean YP and of the Gaussian fit to mean Pr over -5 to\n    5 mm (Fig. 5B legend); the Gaussian FWHM is 2.4 sigma as the Methods give it, and 2.355 sigma as\n    a variant. The paper bounds \"slightly\" by no number; readings (a) YP FWHM / Pr FWHM between 1 and\n    1.25, (b) between 1 and 1.5. Reproduced when the ratio falls in the range under every reading at\n    0 mm elevation (Fig. 5A shows all three; the text gives no elevation); the 1 and 2 mm elevations\n    are reported.\n- id: fig5b-gaussian-pr-lorentzian-yp\n  statement: Pr intensity declined from the peak as a Gaussian and YP as a Lorentzian; in the left\n    panel of Figure 5B the R2 was 0.92 (Lorentzian) against 0.96 (Gaussian) for Pr, and 0.98 against\n    0.95 for YP, fitted from -5 to 5 mm with p < 0.0001.\n  source: Results 3.2, paragraph 2; Figure 5B\n  quote: For Pr data in the left panel of Fig. 5B , the coefficient of determination increased from\n    0.92 for Lorentzian fit to 0.96 for Gaussian fit. YP data showed the opposite trend, with the\n    coefficients of 0.98 and 0.95 for Lorentzian and Gaussian fits, respectively (for all these\n    fits, the fitted region was from −5 to 5 mm, p<0.0001).\n  datasets:\n  - \"001284\"\n  - \"001047\"\n  statistics:\n  - about: each of the four fits\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - quantity: R2 of Lorentzian fit to Pr\n    value: 0.92\n    tolerance: 0.092\n  - quantity: R2 of Gaussian fit to Pr\n    value: 0.96\n    tolerance: 0.096\n  - quantity: R2 of Lorentzian fit to YP\n    value: 0.98\n    tolerance: 0.098\n  - quantity: R2 of Gaussian fit to YP\n    value: 0.95\n    tolerance: 0.095\n  criterion: Set S2. The left panel of Figure 5B is not named; it is read as the 0-mm panel, the one\n    whose peak is 100% (legend). Mean profiles in percent, F4 fits over -5 to 5 mm, O1, O2. R2 is 1 -\n    SSres / SStot over the fitted points. As 10% tolerances on R2 near 1 are loose, the orderings are\n    part of the claim. Reproduced when every R2 is within tolerance and the ordering holds (Gaussian\n    above Lorentzian for Pr, Lorentzian above Gaussian for YP) under every reading; partially when\n    the values are within tolerance but an ordering fails. The other elevations are reported.\n- id: fig5b-reversible-beyond-2mm\n  statement: The Lorentzian YP profile and the Gaussian Pr profile differ mainly in the tails, where\n    YP is broader, marking an area of predominantly reversible electroporation that starts about 2\n    mm from the centre.\n  source: Results 3.2, paragraph 2; Figure 5B\n  quote: The difference between the fits is primarily in the tails, which are broader in Lorentzian\n    distribution compared to Gaussian. This difference highlights the area of predominantly\n    reversible electroporation, which extends outwards starting at about 2 mm from the center.\n  datasets:\n  - \"001284\"\n  - \"001047\"\n  depends_on:\n  - fig5b-gaussian-pr-lorentzian-yp\n  expected:\n    quantity: distance from the centre where YP first exceeds Pr, both in % of their peaks, 0 mm\n      elevation\n    value: 2\n    tolerance: 0.2\n    unit: mm\n  criterion: Set S2 at 0 mm elevation, F1 to F4, O1, O2. YP and Pr each in % of their own 0-mm peak\n    (Fig. 5B legend). The paper does not say how 2 mm was found; readings (a) the smallest distance at\n    which mean YP% exceeds mean Pr% by a gap larger than the error bars (F8); (b) the smallest\n    distance at which the fitted Lorentzian, in % of its a, exceeds the fitted Gaussian, in % of its\n    a, by more than the mean s.e. of YP% over the fitted points. Each side of the centre is taken\n    separately and averaged. Reproduced when the distance is within 1.8 to 2.2 mm under one reading;\n    where the ROIs are more than 0.4 mm apart (O1), when it is the ROI nearest 2 mm.\n- id: fig5c-nuclear-yp-centre\n  statement: In the central spot cells showed bright nuclear YP staining, indicating irreversible\n    damage, while farther out reversibly electroporated cells were weakly stained with less contrast\n    between nucleus and cytoplasm; cells inside the electrode footprint were unstained though present\n    (Hoechst).\n  source: Results 3.2, paragraph 1; Figure 5C\n  quote: Indeed, a closer examination of the central spot confirmed bright YP staining of cell nuclei\n    ( Fig. 5C , zone 1), which is indicative of the irreversible membrane damage and cell death.\n    Reversible electroporation is distinguished by a much weaker YP staining and smaller difference\n    in staining of the nucleus and cytoplasm, such as in zones 2 and 3 in Fig. 5C .\n  datasets:\n  - \"001284\"\n  - \"001047\"\n  criterion: Set S2 at 0 mm. The zones are marked only in Figure 5A, not seen. Zone 1 is in the\n    central spot; zone 3 straddles an electrode wall (its right portion lies inside the footprint,\n    Results 3.2; the Fig. 5C legend marks the wall), so its outside part is the band within 0.5 mm\n    outside a wall; zone 2 is not placed by the text, readings (a) 2 to 4 mm, (b) 3 to 5 mm from the\n    centre along a diagonal; zone 1 is within 1 mm of the centre. Intensity part, on the whole-well\n    images. Background-subtracted YP (F2) in zone 1 exceeds that in zones 2 and 3, footprint YP is\n    below zones 2 and 3, and the footprint holds Hoechst-positive cells in the Hoechst image taken\n    after the Pr image (Methods 2.4, re-imaged \"to check for possible cell loss\"), judged against\n    the same footprint's cell-free lumen or, without one, against the camera offset (a standard\n    choice; the paper names no reference level). Nuclear part, on the high-resolution images of Fig.\n    5C. Nuclei are Hoechst-positive objects (Otsu threshold, a standard choice) and the cytoplasm a\n    ring around each, readings (a) 2 to 4 um, (b) 4 to 8 um; the median nucleus to cytoplasm YP\n    ratio is higher in zone 1 than in zones 2 and 3. Reproduced when both parts hold under every\n    reading; partially when the intensity part holds and the nuclear part is blocked because no\n    dataset holds high-resolution images. Blocked as data_missing for the footprint part when no\n    post-exposure Hoechst image is held.\n- id: fig6b-peak-900ns-not-significant\n  statement: The central YP peak was highest for 900-ns pulses, but not significantly different from\n    300- or 600-ns pulses.\n  source: Results 3.3, paragraph 2; Figure 6B\n  quote: The central peak of YP uptake was higher for 900-ns pulses, but the difference from the\n    other two pulse durations was not statistically significant (CT26 cells, 2 bursts (x4), Fig. 6B ).\n  datasets:\n  - \"001277\"\n  criterion: A claim of absence. Set S3, F1 to F3, O2; per experiment the background-subtracted YP at\n    x = 0, n = 5 per duration. The paper does not name the test here; the sentence frames two\n    comparisons (\"the difference from the other two\"), and Fig. 6D tests durations by two-sided\n    t-tests with Bonferroni correction, so the test is 900 ns against 300 ns and against 600 ns,\n    two-sided Student's t-tests with Bonferroni over the two (F7). Reproduced when the 900-ns mean is\n    the highest and no corrected p is below 0.05; not reproduced when one is. A one-way ANOVA over\n    the three durations (Methods 2.5) and Bonferroni over all three pairs are shown as variants;\n    effect sizes are reported.\n- id: fig6c-normalized-decline-similar\n  statement: Normalized to the central peak, the sideways decline of YP was similar for the three\n    pulse durations.\n  source: Results 3.3, paragraph 2; Figure 6C\n  quote: When the peak YP emission was taken as 100%, its decline sideways was similar for the three\n    tested pulse durations ( Fig. 6C ).\n  datasets:\n  - \"001277\"\n  criterion: A claim of absence, for which the paper reports no test; it is judged by the paper's own\n    rule for its graphs (F8). Set S3, F1 to F3, O1, O2; each experiment's profile in percent of its\n    value at x = 0, then mean +/- s.e. per duration (Fig. 6C, \"same data as in B, but normalized to\n    the peak\"; per-experiment normalization is the one that gives per-experiment error bars).\n    Reproduced when at no measured distance do two durations' means differ by a gap larger than the\n    error bars; not reproduced when any does, with the distances and gaps reported. Normalizing the\n    mean profile and limiting the range to -5 to 5 mm (the Fig. 6B fit range) are shown as variants.\n- id: fig6d-longer-pulses-sharper-peak\n  statement: Fitted per experiment, the FWHM of the central YP peak decreases with pulse duration from\n    300 to 900 ns, with a trend slope different from zero (p = 0.003).\n  source: Results 3.3, paragraph 2; Figure 6D legend\n  quote: However, a more detailed analysis based on fitting of individual experiments (as described\n    in 3.1 ) revealed significant sharpening of the central peak when packets were built from 600-\n    and 900-ns pulses ( Fig. 6D ). The slope coefficient of the logarithmic fit of the data was\n    different from zero at p = 0.003 (one sample, 2-sided t -test).\n  datasets:\n  - \"001277\"\n  statistics:\n  - about: slope of FWHM against pulse duration\n    test: one sample, 2-sided t-test\n    p: 0.003\n    n: 5 experiments per duration\n  criterion: Set S3, F1 to F5, F7, O1 to O4. Per-experiment Lorentzian FWHM (centre fixed at 0, a and\n    b free, no offset, as F4 writes it). The form of the trend is open, as the text says \"logarithmic\n    fit\" and the legend \"best linear fit\"; readings (a) FWHM against duration, (b) FWHM against log\n    duration, each slope tested by the two-sided one-sample t test. Reproduced when the slope is\n    negative with p < 0.05 under every reading; the p under each is reported and compared with\n    0.003.\n- id: fig6d-600-900-differ-from-300\n  statement: FWHM for 600-ns and for 900-ns packets is each significantly smaller than for 300-ns\n    packets (Bonferroni-corrected t-tests, p = 0.028 for one and p = 0.0072 for the other).\n  source: Figure 6D legend\n  quote: \"*p=0.028, **p=0.0072 for the difference from 300-ns pulse exposure (2-sided t -test with\n    Bonferroni correction)\"\n  datasets:\n  - \"001277\"\n  statistics:\n  - about: one of 600 ns and 900 ns against 300 ns (the legend does not say which)\n    test: 2-sided t-test with Bonferroni correction\n    p: 0.028\n    corrected: Bonferroni\n    n: 5 experiments per duration\n  - about: the other of 600 ns and 900 ns against 300 ns\n    test: 2-sided t-test with Bonferroni correction\n    p: 0.0072\n    corrected: Bonferroni\n    n: 5 experiments per duration\n  depends_on:\n  - fig6d-longer-pulses-sharper-peak\n  criterion: Per-experiment FWHM as in fig6d-longer-pulses-sharper-peak. Two-sided Student's t-tests\n    of 600 against 300 ns and of 900 against 300 ns (legend), Bonferroni-corrected; the number of\n    comparisons is not stated, readings (a) 2, each against 300 ns as the legend frames them, (b) 3,\n    all pairs. Reproduced when both corrected p are below 0.05 with the smaller FWHM at the longer\n    duration under every reading of O1 to O3 and the comparison count; partially when only one of\n    the two is. The legend's asterisks are not assigned to durations in the text, so the p-values\n    are compared with 0.028 and 0.0072 in either order and shown.\n- id: fig6d-900ns-fwhm\n  statement: Packets of 900-ns pulses reduced FWHM to 1.7 +/- 0.08 mm, 11.1 +/- 0.6% of the gap between\n    electrodes.\n  source: Results 3.3, paragraph 2; Figure 6D\n  quote: 900-ns pulse packets reduced FWHM to 1.7 ± 0.08 mm, that was 11.1 ± 0.6% of the gap between\n    electrodes.\n  datasets:\n  - \"001277\"\n  depends_on:\n  - fig6d-longer-pulses-sharper-peak\n  expected:\n  - quantity: mean FWHM, 900-ns packets\n    value: 1.7\n    tolerance: 0.08\n    unit: mm\n  - quantity: mean FWHM, 900-ns packets, in % of 15.3 mm\n    value: 11.1\n    tolerance: 0.6\n    unit: \"%\"\n  criterion: Mean over the 5 experiments of the per-experiment FWHM of\n    fig6d-longer-pulses-sharper-peak, in mm and in % of 15.3 mm (F5). Tolerances are the paper's\n    stated spread, read as the s.e. (Methods 2.5). Reproduced when both values are within tolerance\n    under one combination of O1 to O3; the result under each is shown.\n- id: fig7be-center-linear-with-bursts\n  statement: The central YP peak grew linearly with the number of bursts in both CT26 and CHO cells\n    (slopes different from zero at p < 0.001), except that it saturated after 6 bursts (x4) in CT26\n    cells.\n  source: Results 3.4, paragraph 1; Figure 7B, 7E and legend\n  quote: Increasing the number of bursts increased the amplitude of the central peak of YP uptake in\n    both CT26 and CHO cells ( Fig 7A and D ). The increase was linear in both cell lines, except\n    when it reached saturation after 6 bursts (x4) in CT26 cells ( Fig. 7B and E ).\n  datasets:\n  - \"001276\"\n  statistics:\n  - about: slope of centre YP against bursts, CT26, 6 bursts (x4) excluded\n    test: 2-sided one-sample t test\n    p: 0.001\n    p_relation: \"<\"\n    n: 3 to 5 experiments per burst number\n  - about: slope of centre YP against bursts, CHO\n    test: 2-sided one-sample t test\n    p: 0.001\n    p_relation: \"<\"\n    n: 4 experiments per burst number\n  criterion: Set S4, F1 to F3, F7, O1, O2, O4. Per experiment the background-subtracted YP at x = 0,\n    regressed linearly on the number of bursts (x4) by least squares, the CT26 6-burst point left\n    out (Fig. 7B legend), all CHO points in; slopes tested by the two-sided one-sample t test.\n    Counting bursts as 1, 2, 4, 6 or as 4, 8, 16, 24 gives the same p. Reproduced when both slopes\n    are positive with p < 0.001 under every reading; partially when a slope is positive with p <\n    0.05 only, or when it holds in one cell line only. The saturation is fig7b-ct26-saturation.\n- id: fig7b-ct26-saturation\n  statement: In CT26 cells the central YP uptake saturated at 6 bursts (x4), falling below the linear\n    increase seen at fewer bursts, as expected when all central cells are already killed.\n  source: Results 3.4, paragraph 1; Figure 7B legend\n  quote: Considering that even 2 bursts (x4) caused strong cell death in the center ( Fig. 5 ),\n    saturation was expected and indicated that all cells were already killed and YP staining\n    reached its maximum.\n  datasets:\n  - \"001276\"\n  depends_on:\n  - fig7be-center-linear-with-bursts\n  criterion: The paper gives no test of saturation; it shows it by leaving the 6-burst point out of\n    the CT26 fit and drawing the fit's 95% confidence band (Fig. 7 legend). Readings (a) the CT26\n    mean centre YP at 6 bursts (x4) lies below the lower edge of the 95% confidence band of the\n    linear fit of fig7be-center-linear-with-bursts, extrapolated to 6 bursts; (b) the 6-burst mean\n    is not above the mean at the next lower burst number by a gap larger than the error bars (F8).\n    Reproduced when both hold under every reading of O4; partially when the 6-burst mean lies below\n    the fitted line but inside the band. The CHO 6-burst mean against the CHO fit through the lower\n    burst numbers is reported.\n- id: fig7cf-fwhm-with-bursts\n  statement: The FWHM of the central peak increased in proportion to the number of bursts in CT26\n    cells (slope p < 0.001) but not in CHO cells (p = 0.44).\n  source: Results 3.4, paragraph 2; Figure 7C, 7F legend\n  quote: Concurrently, FWHM of the central peak increased proportionally to the burst number in CT26\n    cells, but not in CHO cells ( Fig. 7C and F ).\n  datasets:\n  - \"001276\"\n  statistics:\n  - about: slope of FWHM against bursts, CT26\n    test: 2-sided one-sample t test\n    p: 0.001\n    p_relation: \"<\"\n  - about: slope of FWHM against bursts, CHO\n    test: 2-sided one-sample t test\n    p: 0.44\n  criterion: Set S4, F1 to F5, F7, O1 to O4. Per-experiment Lorentzian FWHM against burst number,\n    linear least squares, slope tested by the two-sided one-sample t test. CHO 1-burst wells are left\n    out (Fig. 7 legend, too small to measure FWHM). The CT26 6-burst point is kept, as the legend\n    leaves it out of panel B only; leaving it out is a variant. The CHO part is a claim of absence\n    judged on the paper's test, the slope t test at p < 0.05. Reproduced when, under every reading,\n    the CT26 slope is positive with p < 0.001 and the CHO slope has p >= 0.05. Partially when the\n    CT26 slope is positive with p < 0.05 only; not reproduced when the CHO slope has p < 0.05.\n- id: fig7-sharpest-peak-one-burst\n  statement: One burst (x4) in CT26 cells gave the sharpest peak of the study, FWHM 1.1 +/- 0.1 mm,\n    7.3% of the inter-electrode gap and 2.3% of the electrode array area.\n  source: Results 3.4, paragraph 3; Figure 7A, 7C; Abstract\n  quote: That being said, 1 burst (x4) in CT26 cells produced the sharpest peak of electroporation\n    seen in this study ... at FWHM of 1.1 ± 0.1 mm, it occupied just 7.3% of the inter-electrode gap\n    and 2.3% of the electrode array area.\n  datasets:\n  - \"001276\"\n  - \"001047\"\n  - \"001277\"\n  - \"001284\"\n  depends_on:\n  - fig7cf-fwhm-with-bursts\n  expected:\n  - quantity: mean FWHM, CT26, 1 burst (x4)\n    value: 1.1\n    tolerance: 0.1\n    unit: mm\n  - quantity: FWHM in % of 15.3 mm\n    value: 7.3\n    tolerance: 0.73\n    unit: \"%\"\n  - quantity: spot area in % of the electrode array area\n    value: 2.3\n    tolerance: 0.23\n    unit: \"%\"\n  criterion: Set S4, CT26 1-burst wells, FWHM as in fig7cf-fwhm-with-bursts under every reading of O3;\n    the FWHM tolerance is the paper's spread (s.e.). The paper does not say how the area percentage\n    is computed; readings (a) a disk of diameter FWHM over the square with 15.3-mm diagonals (117\n    mm2); (b) a disk of radius FWHM over the square of the electrode centres (12.8-mm sides, 164 mm2,\n    from Methods 2.2), the reading that gives 2.3% from 1.1 mm; (c) a disk of diameter FWHM over the\n    square of the electrode centres. Sharpest in the study means the smallest mean FWHM of any group\n    fitted per experiment in S1, S3 and S4 (Figs. 4C, 6D, 7C, 7F), with S2 as reported. Reproduced\n    when the three values are within tolerance under one reading and the 1-burst CT26 FWHM is the\n    smallest; partially when the FWHM alone is within tolerance. Groups held in datasets other than\n    001276 enter the comparison where they are held; a missing series is reported.\n- id: fig7-offtarget-40-50-fold\n  statement: With MHz-CANCAN in CT26 cells, YP emission near the electrodes was 40 to 50 times smaller\n    than at the remote target in the centre.\n  source: Results 3.4, paragraph 3\n  quote: Off-target effects, characterized by YP emission near electrodes, were 40–50 times smaller\n    than at the remote target.\n  datasets:\n  - \"001276\"\n  expected:\n    quantity: ratio of centre YP to near-electrode YP, CT26\n    value: 45.5\n    tolerance: 9.5\n  criterion: Set S4, F1 to F3, F9, O2, O5. The reported range 40 to 50, widened by 10% of each bound,\n    is 36 to 55, which the value and tolerance give. The group is not named; readings (A) 1 burst\n    (x4) only, as the sentence follows the 1-burst result; (B) every CT26 burst number below\n    saturation (1, 2 and 4 bursts (x4)), as the sentence closes a paragraph on all of them and a\n    range can be the span over groups. Reproduced when the ratio lies in 36 to 55 under one\n    combination of readings (for B, for each of those groups); every combination is shown.\n- id: fig7-cho-replicates-ct26\n  statement: Remote focusing of electroporation was consistent across the two cell types; in CHO cells\n    as in CT26 cells the YP uptake peaked at the centre of the array.\n  source: Conclusion; Results 3.4, paragraph 1; Figure 7D\n  quote: The improved focusing was consistent across two cell types and extended to both\n    electroporation and cell killing.\n  datasets:\n  - \"001276\"\n  criterion: Set S4, CHO diagonal profiles by F1 to F3, O1, O2. Reproduced when, for each burst number\n    from 2 bursts (x4) up (after one burst CHO uptake was too small to measure FWHM, Fig. 7 legend;\n    the 1-burst profile is reported), mean centre YP exceeds mean YP at 6 and at 7 mm (the paper's\n    measure of focusing, centre against near electrodes, Results 3.1) by a gap larger than the error\n    bars (F8), and the same holds for CT26 at the same burst numbers. The growth of the CHO peak\n    with bursts is judged in fig7be-center-linear-with-bursts; the cell-killing part rests on CT26\n    only (Fig. 5) and is not tested here.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/silkuniene-2025.yaml paper/10.1016-j.bioelechem.2025.109016.txt; grep -n "—\|rather" claims/silkuniene-2025.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('claims/silkuniene-2025.yaml'))
c=d['claims'];print(len(c),sum('statistics' in x for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))
import re
for x in c:
  for k in ('statement','criterion','source'):
    if ': ' in x.get(k,''): print(x['id'],k)
"; git status --short
```

```
27 8 27 10
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
?? claims/silkuniene-2025.yaml
?? scripts
```

**Agent**

I wrote `claims/silkuniene-2025.yaml`. The quote checker passes it: 27 claims, 27 quotes, 15 statistical values, 0 problems.

**Text read.** The accepted author manuscript in PubMed Central (PMC12331426, NIHMS2087238), not the version of record. It has full Methods 2.1 to 2.5, Results, Discussion, Conclusion and the legends of Figs. 1 to 7. There is no supplement: PMC marks none and the text cites none. No PDF was supplied, so no figure was seen. The paper links no code, so none was read.

**Datasets.** I mapped each dataset from its title and description on DANDI:
- **001047:** the packet-rate series, Figs. 3 and 4. Its description also names propidium, which the paper measures only in the Fig. 5 series, so the four 0-mm Fig. 5 claims (fits, spot sizes, zones) list it too.
- **001284:** the raised-electrode series, Fig. 5.
- **001277:** the pulse-duration series, Fig. 6.
- **001276:** the burst-number series, Fig. 7.
- **No dataset:** no description names the heating images (Fig. 2) or the field simulation (Fig. 1E). Those two claims list all four datasets and are blocked as data_missing if none holds them. The "sharpest peak of the study" claim also lists all four, because it compares groups across series.

**Counts.** 27 claims, all with quotes and criteria, 8 with statistics and 10 with expected values. I kept the earlier ids, taking Figs. 3 to 5 from the 001047 file, Fig. 6 from 001277, Fig. 7 from 001276 and the heating claim's id from 001276/001277. One claim is new: `fig5b-reversible-beyond-2mm` (Results 3.2), which says reversible electroporation starts about 2 mm from the centre.

**Details the paper leaves open, and the readings named:**
- **ROI positions (O1):** whole-mm steps, or contiguous ROIs. Which ROI side lies along the diagonal and which footprint holds the background are standard choices.
- **Pooling diagonals (O2):** two diagonals averaged at each signed distance, or four half-diagonals (Fig. 4A legend).
- **Fit range where no figure fixes it (O3):** Fig. 6D at ±4 or ±5 mm; Fig. 7 at ±4, ±5 or ±6 mm.
- **Regression points (O4):** individual experiments, which Fig. 4C supports, or group means.
- **Centre to near-electrode ratios (O5):** 6 or 7 mm, and the ratio of means or the mean of ratios.
- **How R is computed (Fig. 3):** Pearson correlation of fit and data, or the square root of R².
- **Number of Bonferroni comparisons (Figs. 4C and 6D):** two readings each.
- **Fig. 6D trend form:** linear (legend) or logarithmic (text).
- **Deviation beyond the fit (Fig. 3):** in a.u. or in % of the peak.
- **"Perimeter" (Fig. 3C):** outermost parallel ROIs, or the ROIs at 6 mm.
- **"Slightly larger" (Fig. 5):** ratio bounds of 1.25 or 1.5.
- **The 2-mm boundary (Fig. 5B):** a gap between data points, or a divergence between the fitted curves.
- **Zone locations (Fig. 5C):** zone 2 at 2 to 4 mm or 3 to 5 mm; a cytoplasm ring of 2 to 4 µm or 4 to 8 µm.
- **Heating images (Fig. 2):** two sets of hue limits, and "near the center" as 1 or 2 mm.
- **Which CT26 groups give "40 to 50 times":** 1 burst only, or 1, 2 and 4 bursts.
- **How 2.3% of the array area is computed:** three readings; only a disk of radius FWHM over the electrode-centre square gives 2.3%.
- **Saturation at 6 bursts:** the 95% confidence band, or the error-bar gap rule.

**Where a claim needed something the paper does not give:**
- **Tests not reported:** several findings come with no test (Fig. 5 raised electrodes, Fig. 6C, saturation, near-electrode suppression). These are judged by the paper's own rule from Methods 2.5, that a gap larger than the error bars means p < 0.05.
- **Fig. 5C:** the nuclear-staining comparison needs the high-resolution images, and the footprint check needs the Hoechst image taken after exposure. The paper names no reference level for that Hoechst check.
- **Slips in the paper:** Methods 2.5 says the Gaussian fit appears in Fig. 6, where it is in Fig. 5. The slope p for Fig. 4C is p<0.001 in the text and p<0.0001 in the legend; both are recorded.

I did not commit anything.

## End of run

23 turns, 6 minutes, $2.13 at API prices, result: success.
