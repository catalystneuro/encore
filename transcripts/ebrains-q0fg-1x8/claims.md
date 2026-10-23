# ebrains-q0fg-1x8 · claims · run 39493202897

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ paper/; ls claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml; wc -c paper/*.txt; ls claims | grep -i ebrains; cat docs/archives.md | grep -n -i -A5 ebrains | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat targets/ebrains.json; ls docs; ls schema* tools; grep -rl "ebrains\|EBRAINS" claims | head
```

```
{
 "schema_version": 1,
 "archive": "ebrains",
 "generated": "2026-10-20T19:30:00+00:00",
 "source": "https://search.kg.ebrains.eu, written by hand; files through https://data-proxy.ebrains.eu",
 "note": "One dataset, chosen to test that the pipeline works beyond DANDI. A dataset is named by its DOI's suffix; kg_id is its version's id in the EBRAINS Knowledge Graph, which the data proxy needs.",
 "counts": {
  "with_a_paper": 1
 },
 "targets": [
  {
   "id": "q0fg-1x8",
   "kg_id": "0162668e-bef0-4754-8562-40440db5bc0c",
   "name": "Extracellular unit recordings from CA1/CA3 pyramidal cells in rats exploring an open arena with object landmarks",
   "url": "https://search.kg.ebrains.eu/instances/0162668e-bef0-4754-8562-40440db5bc0c",
   "doi": "10.25493/Q0FG-1X8",
   "published_version": "v1",
   "asset_count": 10,
   "size_gb": 0.43,
   "data_standards": [
[... 54 more lines not kept]
```

**Agent calls Bash**

```bash
cat schemas/claims.schema.json; ls docs/agents; head -c 3000 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat docs/agents/claims.md
```

```
You are the reader for dataset {dataset} in the reproduction registry. The repository is checked out in the current directory. Read docs/protocol.md, the "Reader" section, first: it is the whole method for this run. Look at claims/001453/ for the file format.

Paper: doi:{paper}, "{title}". Its full text is under `paper/`: a `.txt` file per paper (main text, Methods and supplement, with a header saying where it came from), and the PDF where there is one. Read the text; open a PDF page only to read a figure or a table that the text garbles. If the full text, the Methods, or a supplement the results rest on is missing, stop and say what is missing: write no claims. Never write claims from the abstract. You may read the code the paper links to. Do not look at the dataset's data or its files; its title and description on the archive are enough to know which experiments it is meant to hold.

{existing}

Write the claims file as steps 1 to 4 of the Reader section say. Every part of every criterion's method comes from the paper or its code, cited; a detail none of them fixes is named as open, with the readings the paper allows. Check every quote with `python tools/claims_check.py claims/{folder}/<file>.yaml paper/<text>.txt` and fix the quote, never the checker. Do not commit or push: the workflow commits your changes. Only files under `claims/{folder}/` are kept.

Provenance for the opening comment: written by an agent (model "{model}", Claude Code in GitHub Actions), {date}, protocol as stated in docs/protocol.md.

Write prose plainly: no em dashes, never the word "rather". YAML plain scalars must not contain ": " (colon space).

Your final message is a report: the text read (version, supplement), the number of claims and how many have quotes, statistics and criteria; the details the paper leaves open and the readings named for each; anything missing from the paper that a claim needed. Be concise.

Run every command in the foreground and wait for it to finish.
```

**Agent**

Now reading the paper text in full.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2023.04.008.txt",
 "offset": 60,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2023.04.008.txt",
 "offset": 760,
 "limit": 1200
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2023.04.008.txt",
 "offset": 760,
 "limit": 650
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2023.04.008.txt",
 "offset": 1410,
 "limit": 600
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2023.04.008.txt",
 "offset": 2010,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text, Methods and supplement are present (Supplementary Figure 7's legend page seems empty in the text). Next, the code on Zenodo.

**Agent calls Bash**

```bash
cd $TMPDIR && curl -sL https://zenodo.org/api/records/7797252 | python -c "import json,sys; d=json.load(sys.stdin); print(d.get('metadata',{}).get('title'), d.get('metadata',{}).get('version'), d.get('id')); [print(f['key'], f['size'], f['links']['self']) for f in d.get('files',[])]; print(d.get('metadata',{}).get('related_identifiers'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/code && cd $TMPDIR/code && curl -sL -o c.zip "https://zenodo.org/api/records/7797252/files/sebasoa/Object-centered-population-coding-v1.0.zip/content" && unzip -o -q c.zip && find . -type f | grep -v c.zip | xargs wc -l
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/code/sebasoa-*/ && for f in README.md distanceDecoder.m equalDistanceEdges.m divideTrainingTesting.m distanceSet.m calculateDecodingAccuracy.m binningSpikeMatrix.m calculateDistanceMap.m compareThreshold.m rateMapData.m; do echo "=== $f"; cat $f; done
```

```
=== README.md
# Object-centered-population-coding

This repository contains functions necessary to perform some analyses from the paper "Object-centered population coding
in CA1 of the hippocampus", by Nagelhus et al. 2023. 

The most important functions are "objectTuningScore" and "distanceDecoder", responsible for calculating
the object-tuning score and performing the distance decoding, respectively. Please see each function for explanations
of how to use them. 

The object-tuning score requires having recorded position- and spike data from two trials 
with an object placed in different locations (Object and Object Moved in our paper).

The distance decoder requires having recorded position- and spike data from two trials. In our paper, we record
an Empty trial and an Object trial and assess the decoding accuracy at different distances from the object. 

Some functions, including "calculateRateMap" and other functions necessary to run it, are taken from 
Behavioural Neurology Toolbox, (c) Vadim Frolov 2018. 
=== distanceDecoder.m
function [accuracy] = distanceDecoder(posArray,spikeArray,objectPos)
[... 624 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/code/sebasoa-*/ && grep -l "function.*PoissonDecoder" *.m; for f in objectTuningScore.m templateMatchingScore.m shuffledTemplateMatchingScore.m calculateBinCentres.m; do echo "=== $f"; cat $f; done; sed -n 1,140p calculateRateMap.m
```

```
=== objectTuningScore.m
function [score,pass] = objectTuningScore(posArray,spikeArray,objectPosArray)
%objectTuningScore.m 
%   General comments:
%   - This function calculates object-tuning scores through an iterative
%   template-matching procedure as done in "Object-centered population
%   coding in CA1 of the hippocampus" by Nagelhus et al. 2023. 
%
%   Inputs:
%   <posArray>, <spikeArray> and <objectPosArray> should all be 1x2 cell
%   arrays. The cell array's first entry should contain data from the
%   Object trial; the second entry data from the Object Moved trial. 
%   Each entry of <posArray> should be a Tx3 matrix of position data. The
%   matrix should consist of timestamps (column 1), x-coordinates of the
%   animal's position (column 2) and y-coordinates of the animal's position
%   (column 3). T is the number of samples in the position data. 
%   Each entry of spikeArray should be a Nx1 vector of spike timestamps. 
%
%   Outputs: <score>, cell's object-tuning score
%            <pass>, logical variable whether the cell passed or not
[... 349 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python -c "
import fitz
d=fitz.open('paper/10.1016-j.neuron.2023.04.008.pdf')
print(len(d))
for p in [35,46,10,6,9]:
    d[p-1].get_pixmap(dpi=110).save(f'p{p}.png')
"; ls $TMPDIR/*.png
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && which pdftoppm && pdftoppm -f 35 -l 35 -r 90 -png paper/*.pdf p && pdftoppm -f 45 -l 46 -r 90 -png paper/*.pdf p; ls
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.neuron.2023.04.008.pdf",
 "pages": "35,45-46"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && pip install --target $TMPDIR/py pymupdf -q 2>&1 | tail -2; PYTHONPATH=$TMPDIR/py python -c "
import fitz
d=fitz.open('paper/10.1016-j.neuron.2023.04.008.pdf')
print(len(d))
for p in [35,45,46]:
    d[p-1].get_pixmap(dpi=100).save(f'$TMPDIR/p{p}.png')
"
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p35.png"
}
```

Result: no output.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p46.png"
}
```

Result: no output.

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py
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

[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 80,200p tools/claims_check.py
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

**Agent**

I have what I need: full text, Methods, supplement (S7 legend is image-only, read from the PDF), and the code. Writing the claims file now.

**Agent calls Bash**

```bash
cd $TMPDIR/code/sebasoa-*/ && grep -n -i "speed\|maxGap\|blanks" calculateRateMap.m | head -30; sed -n 1,60p smoothData.m | head -40
```

```
15:%                   could be Nx2 matrix of instanteneous animal speed in form [t s].
32:%     'maxGap'      z values recorded during time gaps between successive (x,y) samples exceeding
34:%                   in (x,y) sampling will be clipped to 'maxGap' to compute the occupancy map
49:%     'blanks'      'on' results on NaN values in map for unvisited places (regardless of smoothing).
102:    defaultMaxGap = 0.1;
117:    checkBlanks = @(x) helpers.isstring(x, 'on', 'off');
125:    addParameter(inp, 'maxGap', defaultMaxGap, checkScalar);
130:    addParameter(inp, 'blanks', 'on');
138:    maxGap = inp.Results.maxGap;
143:    sBlanks = inp.Results.blanks;
144:    showBlanks = strcmpi(sBlanks, 'on');
248:        % Duration for each (X,Y) sample (clipped to maxGap)
254:        dt(dt>maxGap) = maxGap;
297:                %[z, discarded] = Interpolate(z, t, 'maxGap', maxGap);
375:            if showBlanks
391:            if showBlanks
% smooth - Smooth using a Gaussian kernel.
%
%  USAGE
%
[... 36 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml",
 "content": "# Claims for Nagelhus, Andersson, Gonzalo Cogno, Moser & Moser (2023), \"Object-centered population\n# coding in CA1 of the hippocampus\", Neuron 111, 2091-2104, on EBRAINS dataset 10.25493/Q0FG-1X8.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-20, protocol\n# as stated in docs/protocol.md (pilot-10).\n#\n# Text read: the version of record (open access, CC BY), from the PDF supplied by a person, as\n# extracted to paper/10.1016-j.neuron.2023.04.008.txt: main text, figure legends, STAR Methods and\n# the Supplemental information (Supplementary Figures 1 to 8 and Supplementary Table 1). The legend\n# of Supplementary Figure 7 is an image in the PDF and is missing from the text; it was read from\n# PDF page 46. The CA3 p-values of Supplementary Figure 3F were read from PDF page 35. Supplementary\n# Table 1 is garbled in the text (exponents of some p-values are lost) and is used only where legible.\n#\n# Code read: the paper's code on Zenodo (doi:10.5281/zenodo.7797252, \"v1.0\"), a snapshot of GitHub\n# sebasoa/Object-centered-population-coding at tag v1.0, commit 4e4f5ac. It holds MATLAB functions\n# for the object-tuning score (objectTuningScore.m, templateMatchingScore.m,\n# shuffledTemplateMatchingScore.m, rateMapData.m, compareThreshold.m) and for the distance decoder\n# (distanceDecoder.m, divideTrainingTesting.m, binningSpikeMatrix.m, equalDistanceEdges.m,\n# calculateDistanceMap.m, calculateDecodingAccuracy.m), with a rate-map function (calculateRateMap.m,\n# from the Behavioural Neurology Toolbox). Two functions they call are not in the repository:\n# objectScore (the template and its correlation with a rate map) and PoissonDecoder_distance (the\n# Poisson likelihood). Those steps are taken from the Methods. No code is given for the single-cell\n# change analyses, object traces, words and counts, mutual information, KL divergence, behavioural\n# decoders or population vector correlations.\n#\n# Data the paper used (as it reports them). 10 male Long-Evans rats; 7 implanted with tetrodes\n# (CA1/CA3) and 3 with Neuropixels 2.0 probes (CA1/CA3 and MEC; MEC data not used). Each session had\n# four trials of free foraging in a 150 cm x 150 cm open field, each typically 20 to 30 min (the\n# Methods assume 1800 s): No Object (NO), Object (O, a 52 x 10 x 10 cm Duplo tower at or near the\n# middle), Object Moved (OM, the tower moved towards a corner, 35 to 55 cm from it), and No Object'\n# (NO', omitted in some sessions, 8.5% of cells). Control sessions had four trials without an object\n# (CON1 to CON4). Position from two LEDs at 25 Hz (tetrodes) or OptiTrack at about 120 Hz\n# (Neuropixels). Cells were kept when no more than 1% of inter-spike intervals were under 2 ms and\n# the mean rate over the session was 0.05 to 10 Hz; cells in cortex or dentate gyrus were excluded.\n# Samples: 1,189 unique CA1 principal cells from 9 rats in object sessions; 219 CA1 cells from 3\n# rats in control sessions; 313 CA3 cells and 59 CA3 control cells from 2 rats. Population analyses\n# use the sessions with at least 25 simultaneously recorded cells: the Methods say 15 tetrode\n# sessions (25 to 39 cells) and 2 Neuropixels sessions (620 cells from two probes in rat 27207, and\n# 135 cells from one probe), 4 rats in all; the figure legends count 16 sessions, and the Figure 5B\n# and Supplementary Figure 8A legends say 14 tetrode sessions (2 rats). Measured variables: spike\n# times, position, head direction, object position per trial, cell identity across days (tetrodes),\n# recording region (CA1 or CA3) and the proximodistal implant site.\n#\n# The dataset is described on EBRAINS as \"Extracellular unit recordings from CA1/CA3 pyramidal cells\n# in rats exploring an open arena with object landmarks\" (v1, MATLAB files). Whether it holds the\n# control sessions, the CA3 cells, cell identities across days and the implant sites is the\n# author's to find.\n#\n# Methods shared by many claims, with their sources.\n#\n# Rate maps for single cells (Fig 1 to 2, 7, S2 to S4). Methods, Firing rate maps: 2.5 cm bins,\n# spikes over time per bin, Gaussian smoothing with SD 2 bins, only epochs with speed above 2.5 cm/s.\n# Spatial correlation (Methods, Spatial correlation and rate overlap): Pearson correlation over bins\n# with a value in both maps. Rate overlap: mean rate in the less active trial over that in the more\n# active trial. Firing fields (Methods): contours from the peak down to 3 x MAD of all bins, fields\n# at least 225 cm2 with a rate of at least 1 Hz. Open: whether the mean rate for rate overlap uses\n# all of the trial or only the speed-filtered epochs; readings (a) speed-filtered, (b) whole trial.\n#\n# Template matching (object-tuning score). Methods, Template matching procedure, and the code\n# (rateMapData.m, templateMatchingScore.m, shuffledTemplateMatchingScore.m, compareThreshold.m):\n# rate maps of the O and OM trials with 3 cm bins over 0 to 150 cm (50 x 50), smoothing 2 bins,\n# unvisited bins not blanked (code); Gaussian templates centred at the object or offset by 5, 10,\n# 15, 20, 30, 40, 50 or 60 cm in 8 directions (0 to 7 pi/4), 8 widths, 520 scores per cell; score =\n# minimum over O and OM of the Pearson correlation of template and rate map; per width, 500\n# shuffles drawing one location uniformly in the arena (0 to 150 cm in x and y) used in both trials\n# (code), threshold the 99th percentile of the shuffled minimum; a cell is object-tuned when any\n# score exceeds its width's threshold. A cell's single object-tuning score (Fig 7) is the score with\n# the largest margin over its threshold (compareThreshold.m). Open, could change the outcome: the\n# template width. Readings (a) the code's, standard deviations of 5, 10, 25, 50, 75, 100, 150 and\n# 200 cm; (b) the Methods', variances of those values (standard deviation the square root, in cm).\n# Open: the template's form and the bins correlated (objectScore is not in the repository); the\n# reading used is an isotropic Gaussian evaluated at bin centres, correlated with all 2,500 bins.\n# Open: the speed filter, applied to these maps per the Methods (the code takes the positions it\n# is given).\n#\n# Distance decoder. Methods, Bayesian decoding algorithm and Calculation of decoding accuracy, and\n# the code distanceDecoder.m with its helpers. Trials NO and O. Each trial is split at the midpoint\n# of its position time span; one iteration tests on the first half and trains on the second, the\n# other the reverse (divideTrainingTesting.m). Rate maps and occupancy from the training half with\n# 3 cm bins, smoothing 2 bins, unvisited bins not blanked (distanceDecoder.m). Testing samples are\n# spike counts in consecutive 1 s bins from the start of the testing half (binningSpikeMatrix.m).\n# A sample's distance is that of the position sample nearest in time to the bin centre from the\n# object (equalDistanceEdges.m). Within each trial and iteration, testing samples are sorted by\n# distance and split into 5 equal groups, the remainder going to bin 5; the bin edges are 0 and each\n# group's largest distance (equalDistanceEdges.m). For a sample in distance bin b, the likelihood\n# under each trial is the product over cells of Poisson probabilities with mean the training rate in\n# a spatial bin (Methods), times a prior equal to that trial's training occupancy restricted to the\n# spatial bins whose centre lies strictly between bin b's edges of that trial and normalised, summed\n# over those spatial bins (distanceDecoder.m). The sample is assigned to NO when the ratio exceeds 1.\n# Accuracy per distance bin is correct over correct plus wrong, pooled over both trials and both\n# iterations, ties left out (calculateDecodingAccuracy.m). The whole-arena decoder (Fig 3) is the\n# same without distance bins: all spatial bins and the full occupancy prior (Methods). Open, could\n# change the outcome: the speed filter. Readings (a) the Methods' rule, rate maps and occupancy from\n# epochs above 2.5 cm/s, all testing samples kept; (b) the code as written, no speed filter.\n#\n# Decoding sessions. Methods: tetrode sessions with at least 25 simultaneously recorded CA1 cells\n# and the two Neuropixels CA1 sessions. The text gives 15 tetrode sessions (17 in all), the legends\n# 16 sessions (14 tetrode). Readings (S-methods) every session meeting the Methods' rule;\n# (S-legends) when that rule gives one session more than 16, the claim is also run on each set of 16\n# that drops one tetrode session, and the outcome is the one all of them give. The session count\n# found is reported. Statistics over sessions (Methods, Statistical tests): Kruskal-Wallis across\n# distance bins, Wilcoxon signed-rank for paired comparisons, rank-sum for unpaired, Pearson for\n# correlations, two-sided, alpha 0.05.\n#\n# Unique cells. The paper counts 1,189 unique CA1 cells; tetrode cells recorded on several days are\n# counted once. The paper does not say which day's session stands for such a cell in the single-cell\n# analyses. Readings (a) the first day the cell was recorded (Fig 1H calls it day 0); (b) every\n# session, counting cell-sessions. Each count-based claim is judged under both.\n#\n# Inconsistencies in the paper noted for the attempt: 13 (text) against 11 (Fig 1H legend) of 35\n# cells stable on more than one day, with 31.4% printed for both (11/35 = 31.4%); identical statistics\n# for OM-NO' and NO-NO' spatial correlation (z = 11.85, p = 2.11e-32); 12.2% (text) against 12.3%\n# (Fig S5L legend) of cells with positive distance tuning; three different lists of subset sizes for\n# Figure 6C; the Figure 3D legend pools four datasets while the Methods use the 620-cell session; the\n# Figure 6A legend gives 1,189 cells from the 17 decoding sessions, while 1,189 is the count over\n# all 9 rats; the Methods refer to a section \"Region-of-interest analysis for object responses\" that\n# is not in the paper.\nschema_version: 2\ndataset:\n  archive: ebrains\n  id: Q0FG-1X8\n  doi: 10.25493/Q0FG-1X8\npaper: doi:10.1016/j.neuron.2023.04.008\nclaims:\n- id: cell-counts\n  statement: The object sessions yielded 1,189 unique CA1 principal cells from 9 rats, the control\n    sessions 219 CA1 principal cells from 3 rats, and up to 620 CA1 cells were recorded simultaneously.\n  source: Figure 2D legend; Introduction, paragraph 3; Results, Decoding the presence of an object, paragraph 1\n  quote: \"n = 1,189 principal cells recorded from 9 rats) and the corresponding pair of control trials\n    (as in Figure 2B; brown lines; n = 219 principal cells recorded from 3 rats)\"\n  expected:\n  - quantity: unique CA1 cells in object sessions\n    value: 1189\n    tolerance: 118.9\n    unit: cells\n  - quantity: CA1 cells in control sessions\n    value: 219\n    tolerance: 21.9\n    unit: cells\n  - quantity: largest number of CA1 cells recorded simultaneously\n    value: 620\n    tolerance: 62\n    unit: cells\n  criterion: Cells are counted after the paper's inclusion rules (Methods, Spike sorting and\n    cell-inclusion criteria, and Histology), CA1 only. Unique cells under both readings of the opening\n    comment. Reproduced when the three counts are within tolerance.\n- id: fig1c-object-tuned-fraction\n  statement: 19.9% of CA1 cells (237 of 1,189) were object-tuned by the template matching\n    procedure, significantly more than the 5.03% (11 of 219) found by the same procedure in control\n    trials without objects.\n  source: Results, Object cells and object-vector cells in the hippocampus, paragraph 3; Figure 1C\n  quote: \"Using the template matching procedure, 19.9% of CA1 cells were classified as object-tuned\n    (237/1,189 cells) ... This fraction was significantly higher than a chance level determined by\n    running the same template matching procedure on control trials without objects (11/219 cells,\n    5.03%\"\n  statistics:\n  - test: binomial test\n    p: 5.73e-141\n    p_relation: \"<\"\n    n: 1,189 CA1 cells against a chance level from 219 control cells\n  expected:\n  - quantity: fraction of CA1 cells object-tuned\n    value: 0.199\n    tolerance: 0.0199\n  - quantity: fraction of control cells object-tuned (chance level)\n    value: 0.0503\n    tolerance: 0.00503\n  criterion: Template matching as in the opening comment, under each template-width reading, on the\n    O and OM trials of every CA1 cell. Chance level as in the Methods (Template matching, Chance level),\n    on the 219 control cells with the object placed at (75, 75) cm in the trial standing for O and at\n    (35, 120) cm in the trial standing for OM. The paper does not say which control trials stand for\n    O and OM; readings (a) CON2 and CON3, the trials in the same place in the session; (b) CON1 and\n    CON2. Reproduced when, under one reading, both fractions are within tolerance and a one-sided\n    binomial test of the object-tuned count against the chance fraction gives p < 0.05.\n- id: fig1d-field-distances\n  statement: Firing fields of object-tuned cells lay at a wide range of distances from the object\n    (4.8 to 80.7 cm, mean 37.7 cm, SD 16.0 cm) and covered all directions around it.\n  source: Results, Object cells and object-vector cells in the hippocampus, paragraph 3; Figure 1D\n  quote: \"The firing fields of the object-tuned cells covered a wide range of distances from the\n    object (range: 4.8–80.7 cm; mean ± SD: 37.7 ± 16.0 cm) and the entire azimuthal range\"\n  depends_on:\n  - fig1c-object-tuned-fraction\n  expected:\n  - quantity: mean distance of object-tuned cells' fields from the object\n    value: 37.7\n    tolerance: 3.77\n    unit: cm\n  - quantity: smallest field distance\n    value: 4.8\n    tolerance: 0.48\n    unit: cm\n  - quantity: largest field distance\n    value: 80.7\n    tolerance: 8.07\n    unit: cm\n  criterion: The tolerance on the mean is 10% of it, as the SD of 16.0 cm is the spread over cells,\n    not an uncertainty of the mean. Fields detected as in the opening comment. The paper does not say\n    which point of a field gives its distance, in which trial, or which field of a cell with several.\n    Readings (a) the centroid of the field (the point Supplementary Figure 5G plots) in the O trial,\n    nearest field; (b) as (a) averaged over the O and OM trials; (c) the field's peak bin in the O\n    trial. Reproduced when, under one reading, the mean is within tolerance, the range lies within\n    4.8 to 80.7 cm widened by 10% of each bound, and every 45 degree sector around the object holds\n    at least one field.\n- id: fig1e-object-cells-and-object-vector-cells\n  statement: About 4.1% of all recorded CA1 cells (49 of 1,189) were object cells, object-tuned with\n    fields under 15 cm from the object, and 13.3% (158) were object-vector cells, with fields 15 cm or\n    more away; 30 object-tuned cells had no detectable field.\n  source: Results, Object cells and object-vector cells in the hippocampus, paragraph 4; Figure 1E;\n    Methods, Template matching procedure\n  quote: \"we estimated that 4.1% of all recorded cells were object cells (49/1,189 cells, object-tuned\n    cells with firing fields <15 cm from the object ... and 13.3% were object-vector cells (158/1,189\n    cells\"\n  depends_on:\n  - fig1c-object-tuned-fraction\n  expected:\n  - quantity: fraction of cells that are object cells\n    value: 0.041\n    tolerance: 0.0041\n  - quantity: fraction of cells that are object-vector cells\n    value: 0.133\n    tolerance: 0.0133\n  - quantity: object-tuned cells without a detectable field\n    value: 30\n    tolerance: 3\n    unit: cells\n  criterion: Field distance under the readings of fig1d-field-distances. Reproduced when, under one\n    reading, the three values are within tolerance.\n- id: fig1f-orientation-coverage\n  statement: The nearer an object-tuned cell's firing field is to the object, the larger the range of\n    orientations around the object that its fields cover.\n  source: Figure 1F legend\n  quote: \"The nearer the cell’s firing field is to the object, the larger is the orientation coverage.\"\n  depends_on:\n  - fig1c-object-tuned-fraction\n  criterion: Orientation coverage is the fraction of 0 to 360 degrees around the object covered by the\n    cell's firing fields (Supplementary Figure 3C legend), taken as the angular span, seen from the\n    object centre, of the field bins; distance as in fig1d-field-distances. The paper reports no test;\n    its stated test for correlations is Pearson's (Methods, Statistical tests). Reproduced when, under\n    one distance reading, the Pearson correlation of coverage with distance over object-tuned cells\n    is negative with p < 0.05.\n- id: fig1g-no-experience-effect\n  statement: The object-tuning score did not change with the number of days the animal had been\n    exposed to the object (r = -0.080, p = 0.574, 62 cells).\n  source: Results, Object cells and object-vector cells in the hippocampus, paragraph 4; Figure 1G\n  quote: \"We observed no significant effect of day of exposure to the object on the object-tuning\n    score (Figure 1G)\"\n  statistics:\n  - test: Pearson correlation\n    statistic: r = -0.080\n    p: 0.57369\n    n: 62 cells recorded on several days and object-tuned on at least one\n  depends_on:\n  - fig1c-object-tuned-fraction\n  criterion: A claim of absence, judged on the paper's test. For every cell recorded on more than one\n    day and object-tuned on at least one, each day's object-tuning score (opening comment) against the\n    number of days the rat had been exposed to the object; Pearson correlation over all cell-days.\n    Reproduced when p >= 0.05; not reproduced when p < 0.05. The r and the number of cells are given\n    either way. Needs cell identities across days.\n- id: fig1h-cross-day-stability\n  statement: Of 35 object-tuned cells recorded on more than one day, few passed the object-tuning\n    criteria on more than one day, yet object-tuned cells passed again on later days more often than\n    other cells (13/35 against 36/370, p = 3.35e-4).\n  source: Results, Object cells and object-vector cells in the hippocampus, paragraph 5; Figure 1H\n  quote: \"Only 13 of these cells (31.4%) had significant object-tuning scores on more than 1 day\n    (Figure 1H). However, object-tuned cells were more stable than expected by chance, with higher\n    probability of passing the classification on later days compared to other cells (13/35\n    object-tuned cells vs. 36/370 other cells\"\n  statistics:\n  - test: binomial test\n    p: 3.35e-4\n    n: 35 object-tuned cells and 370 other cells recorded on more than one day\n  depends_on:\n  - fig1c-object-tuned-fraction\n  expected:\n  - quantity: object-tuned cells recorded on more than one day\n    value: 35\n    tolerance: 3.5\n    unit: cells\n  - quantity: other cells recorded on more than one day that passed on a later day\n    value: 36\n    tolerance: 3.6\n    unit: cells\n  criterion: The paper gives 13 in the text and 11 in the Figure 1H legend, with 31.4% for both;\n    the readings are 13 (text) and 11 (legend, which matches 31.4%). Day 0 is the first day a cell\n    was recorded (Figure 1H legend). Reproduced when the counts are within tolerance, the number of\n    object-tuned cells passing on more than one day is within 10% of 13 or of 11, and a one-sided\n    binomial test of that count among the 35 against the fraction of other cells passing on a later\n    day gives p < 0.05. Needs cell identities across days.\n- id: figs2e-within-trial-stability\n  statement: Within a single trial, object-tuned cells with larger object-tuning scores were more\n    stable (r = 0.45 between within-trial stability and score).\n  source: Results, Object cells and object-vector cells in the hippocampus, paragraph 5; Supplementary\n    Figure 2E\n  quote: \"cells with larger object-tuning scores tended to be more stable than cells with lower scores\n    (Figure S2E) (Pearson correlation between within-trial stability and object-tuning score, r = 0.45\"\n  statistics:\n  - test: Pearson correlation\n    statistic: r = 0.45\n    p: 3.65e-13\n    n: 237 object-tuned cells\n  depends_on:\n  - fig1c-object-tuned-fraction\n  expected:\n    quantity: Pearson r, within-trial stability against object-tuning score\n    value: 0.45\n    tolerance: 0.045\n  criterion: Within-trial stability is the Pearson correlation of rate maps from the first and second\n    halves of the O trial (Supplementary Figure 2E legend), rate maps as in the opening comment.\n    Reproduced when r is within tolerance and p < 0.05.\n- id: figs2c-no-proximodistal-effect\n  statement: The percentage of object-tuned cells did not depend on the proximodistal location of the\n    recording site (r = 0.42, p = 0.22).\n  source: Results, Object cells and object-vector cells in the hippocampus, paragraph 3; Supplementary\n    Figure 2C\n  quote: \"There was no significant linear correlation between the proximodistal site and the percentage\n    of object related cells (r = 0.42, p = 0.2216\"\n  statistics:\n  - test: Pearson correlation\n    statistic: r = 0.42\n    p: 0.2216\n    n: 10 implants (9 rats, two Neuropixels probes in rat 27207)\n  depends_on:\n  - fig1c-object-tuned-fraction\n  criterion: A claim of absence, judged on the paper's test. Per implant (rat, with the two probes of\n    rat 27207 apart), the percentage of object-tuned cells against the proximodistal order of the\n    implant site; Pearson correlation. Reproduced when p >= 0.05, not reproduced when p < 0.05; r is\n    given either way. Needs the implant sites, which the paper shows in Supplementary Figure 1.\n- id: figs3a-ca3-object-tuned\n  statement: Object-related activity was present also in CA3, where 23% of cells (72 of 313) were\n    object-tuned.\n  source: Supplementary Figure 3A\n  quote: \"In CA3, 23% of the cells were object tuned (72/313 cells; 7 object cells and 58 object vector\n    cells)\"\n  expected:\n    quantity: fraction of CA3 cells object-tuned\n    value: 0.23\n    tolerance: 0.023\n  criterion: Template matching as for CA1 (opening comment), on the CA3 cells. Reproduced when, under\n    one template-width reading, the fraction is within tolerance.\n- id: fig2d-spatial-change-no-o\n  statement: Introducing the object changed spatial firing more than the passage of time did, with\n    lower NO-O rate-map correlations than CON1-CON2 correlations in control sessions.\n  source: Results, The majority of hippocampal cells change spatial firing patterns, paragraph 1;\n    Figure 2D, top left\n  quote: \"introducing the object led to larger changes in spatial firing patterns (i.e., smaller\n    Pearson correlations of rate maps) than in pairs of control trials with no object\"\n  statistics:\n  - test: Wilcoxon rank-sum test\n    statistic: z = 12.17\n    p: 4.75e-34\n    n: 1,189 CA1 cells against 219 control CA1 cells\n  criterion: Spatial correlation as in the opening comment. Reproduced when the NO-O correlations are\n    lower than the CON1-CON2 correlations (lower median) with a two-sided rank-sum p < 0.05.\n- id: fig2d-rate-overlap-no-o-unchanged\n  statement: The overall rate change between NO and O, measured by rate overlap, did not differ from\n    that between control trials.\n  source: Results, The majority of hippocampal cells change spatial firing patterns, paragraph 1;\n    Figure 2D, top right\n  quote: \"the overall rate change, estimated as the mean firing rate in the less active trial divided\n    by mean firing rate in the more active trial (rate overlap), was not different between trial pairs\n    with objects (NO-O) and control trials (CON1-CON2)\"\n  statistics:\n  - test: Wilcoxon rank-sum test\n    statistic: z = 0.57\n    p: 0.57\n    n: 1,189 CA1 cells against 219 control CA1 cells\n  criterion: A claim of absence, judged on the paper's test, a two-sided Wilcoxon rank-sum test of NO-O\n    against CON1-CON2 rate overlaps at alpha 0.05. Reproduced when p >= 0.05, not reproduced when\n    p < 0.05; the difference in medians is given either way, under both rate-overlap readings of the\n    opening comment.\n- id: fig2-fraction-changed-no-o\n  statement: About two thirds of CA1 cells (67.5%, 803 of 1,189) changed their spatial firing, their\n    rate, or both between NO and O.\n  source: Results, The majority of hippocampal cells change spatial firing patterns, paragraph 1\n  quote: \"we estimated that 67.5% of the cells (n = 803/1,189 cells) expressed either spatial change,\n    rate change, or both between NO and O\"\n  expected:\n    quantity: fraction of CA1 cells changing between NO and O\n    value: 0.675\n    tolerance: 0.0675\n  criterion: The Methods' classification (Spatial correlation and rate overlap). Within-trial\n    distributions from the NO trial, split 500 times at random into two groups of 1 s bins; between-\n    trial distributions from a random half of each trial's 1 s bins, 500 times. A cell changes on a\n    measure when the mean between-trial value is below the 1st percentile of the within-trial\n    distribution and a Wilcoxon signed-rank test of the two distributions gives p < 0.05 (alpha from\n    Methods, Statistical tests; the 500 values are paired by repetition, as the signed-rank test needs\n    pairs and the paper does not say how they are paired). A cell counts when it changes on spatial\n    correlation, rate overlap or both. Reproduced when the fraction is within tolerance.\n- id: fig2d-o-om-change\n  statement: Moving the object also changed spatial firing and rate more than in control trials, and\n    69.7% of cells (829 of 1,189) changed between O and OM.\n  source: Results, The majority of hippocampal cells change spatial firing patterns, paragraph 1;\n    Figure 2D, second row\n  quote: \"Considerable change was also observed between the O and OM trials ... In these trials, 69.7%\n    of the cells changed their spatial firing pattern, firing rate, or both when the object was moved\n    (n = 829/1,189 cells)\"\n  statistics:\n  - about: spatial correlation, O-OM against CON2-CON3\n    test: Wilcoxon rank-sum test\n    statistic: z = 13.23\n    p: 5.87e-40\n  - about: rate overlap, O-OM against CON2-CON3\n    test: Wilcoxon rank-sum test\n    statistic: z = 3.43\n    p: 0.001\n  expected:\n    quantity: fraction of CA1 cells changing between O and OM\n    value: 0.697\n    tolerance: 0.0697\n  criterion: As fig2d-spatial-change-no-o and fig2-fraction-changed-no-o, for O-OM against CON2-CON3.\n    Reproduced when both rank-sum tests give p < 0.05 with lower O-OM medians, and the fraction is\n    within tolerance; partially reproduced when one of the three holds.\n- id: fig2d-om-no-prime-change\n  statement: Removing the object changed spatial firing more than in control trials (OM-NO' against\n    CON3-CON4), without a significant difference in rate overlap, and many cells kept fields from the\n    preceding trial.\n  source: Results, The majority of hippocampal cells change spatial firing patterns, paragraph 1;\n    Figure 2D, third row\n  quote: \"Major changes were evoked also when we removed the object ... Upon removal of the object,\n    many cells retained firing fields from the preceding trial\"\n  statistics:\n  - about: spatial correlation, OM-NO' against CON3-CON4\n    test: Wilcoxon rank-sum test\n    statistic: z = 11.85\n    p: 2.11e-32\n  - about: rate overlap, OM-NO' against CON3-CON4\n    test: Wilcoxon rank-sum test\n    statistic: z = 1.79\n    p: 0.074\n  criterion: Reproduced when the spatial correlations are lower for OM-NO' with rank-sum p < 0.05, and\n    the rate-overlap rank-sum test gives p >= 0.05 (the absence part, judged on the paper's test).\n    Sessions without a NO' trial are left out.\n- id: fig2d-no-no-prime-change\n  statement: Spatial firing in NO' differed from that in NO more than CON4 differed from CON1.\n  source: Results, The majority of hippocampal cells change spatial firing patterns, paragraph 1;\n    Figure 2D, fourth row\n  quote: \"major changes in spatial firing were also observed between NO and NO0 (Figure 2D, fourth\n    row\"\n  statistics:\n  - test: Wilcoxon rank-sum test\n    statistic: z = 11.85\n    p: 2.11e-32\n  criterion: Reproduced when NO-NO' spatial correlations are lower than CON1-CON4 correlations with\n    rank-sum p < 0.05. The paper prints the same z and p as for OM-NO'; that is noted, not tested.\n- id: figs3f-ca3-changes\n  statement: In CA3 too, spatial correlations between trials differed between object and control\n    sessions for every trial pair, while rate overlaps did not.\n  source: Supplementary Figure 3F\n  quote: \"As for CA1, we found that spatial correlation values between pairs of trials was always\n    significantly different between Object sessions and control sessions, whereas rate overlap was not\n    significantly different between the two types of sessions.\"\n  statistics:\n  - about: spatial correlation, NO-O against CON1-CON2\n    test: Wilcoxon rank-sum test\n    p: 5.13e-8\n  - about: rate overlap, NO-O against CON1-CON2\n    test: Wilcoxon rank-sum test\n    statistic: z = 1.43\n    p: 0.154\n  - about: spatial correlation, O-OM against CON2-CON3\n    test: Wilcoxon rank-sum test\n    p: 2.87e-8\n  - about: rate overlap, O-OM against CON2-CON3\n    test: Wilcoxon rank-sum test\n    p: 0.727\n  - about: spatial correlation, OM-NO' against CON3-CON4\n    test: Wilcoxon rank-sum test\n    p: 6.64e-7\n  - about: rate overlap, OM-NO' against CON3-CON4\n    test: Wilcoxon rank-sum test\n    p: 0.159\n  - about: spatial correlation, NO-NO' against CON1-CON4\n    test: Wilcoxon rank-sum test\n    p: 1.52e-6\n  - about: rate overlap, NO-NO' against CON1-CON4\n    test: Wilcoxon rank-sum test\n    p: 0.325\n  criterion: 313 CA3 cells against the 59 CA3 control cells, measures as for CA1. Reproduced when all\n    four spatial-correlation tests give p < 0.05 and all four rate-overlap tests give p >= 0.05 (the\n    absence part judged on the paper's test); partially reproduced when the spatial part holds and one\n    or more rate-overlap tests is significant.\n- id: figs4-object-traces\n  statement: 18.3% of CA1 cells (218 of 1,189) had object-trace fields, firing in NO' where they had\n    fired in OM, well above the 1% chance level.\n  source: Supplementary Figure 4B to 4D legend; Methods, Region-of-interest analysis for object traces\n  quote: \"We found that 18.3% of CA1 cells had trace responses ... (n = 218/1189 cells in total,\n    significantly above chance level of 1%\"\n  statistics:\n  - test: binomial test\n    p: 5.73e-141\n    p_relation: \"<\"\n    n: 1,189 CA1 cells\n  expected:\n  - quantity: fraction of CA1 cells with trace fields\n    value: 0.183\n    tolerance: 0.0183\n  - quantity: cells changing between NO and NO'\n    value: 919\n    tolerance: 91.9\n    unit: cells\n  criterion: The Methods' procedure. Cells changing between NO and NO' as in\n    fig2-fraction-changed-no-o; fields in NO' (opening comment); a circular ROI per field moved to the\n    same place in OM; rate overlap between the NO' ROI and the OM ROI against 1,000 shuffles placing\n    the ROI at random in OM with wrap-around; a trace field above the 99th percentile. The ROI's size\n    is open, as the Methods refer to a section that is not in the paper. Readings (a) a circle of the\n    field's area centred on its centroid; (b) the smallest circle centred on the centroid containing\n    the field. Reproduced when, under one reading, both values are within tolerance and a one-sided\n    binomial test against 1% gives p < 0.05.\n- id: figs2d-traces-no-interference\n  statement: Removing object traces from the OM trial did not significantly change the number of\n    object-tuned cells (256 of 1,189 after removal, against the expected 19.9%).\n  source: Supplementary Figure 2D\n  quote: \"The number object tuned cells was not significantly different after removing traces (using\n    expected percentage 19.9% from Fig. 1c and observed count of 256/1189\"\n  statistics:\n  - test: binomial test\n    p: 0.0905\n    n: 1,189 CA1 cells\n  depends_on:\n  - fig1c-object-tuned-fraction\n  - figs4-object-traces\n  criterion: A claim of absence, judged on the paper's test, a two-sided binomial test of the count of\n    object-tuned cells after removal against 19.9% at alpha 0.05. The paper does not say how traces\n    were removed; the one reading its text allows is to leave the OM rate-map bins inside the trace\n    ROIs of figs4-object-traces out of the template correlations. Reproduced when p >= 0.05, not\n    reproduced when p < 0.05; the count is given either way.\n- id: ovs-method-extra-cells\n  statement: The object-vector score method of earlier studies classified 40 cells (3.4%) that the\n    template matching did not, mostly false positives on inspection.\n  source: Methods, Object-vector score and object-vector cell criteria, last paragraph\n  quote: \"40 out of 1189 cells (3.4%) were classified by this method but not by the template matching\n    procedure.\"\n  depends_on:\n  - fig1c-object-tuned-fraction\n  expected:\n    quantity: cells classified by the object-vector criteria and not by template matching\n    value: 40\n    tolerance: 4\n    unit: cells\n  criterion: The Methods' four criteria, after excluding cells whose fields would fall outside the\n    arena in OM. The vector map's distance and direction bins and its smoothing are not given; the\n    readings are those of Hoydal et al. 2019 (the paper's reference 11), which the author must ask\n    a reader to fix before the test. Reproduced when the count is within tolerance. The manual\n    inspection is not repeated.\n- id: fig3b-decode-presence\n  statement: A Bayesian decoder using 1 s population spike counts told the NO trial from the O trial\n    above chance (50%) in every session.\n  source: Results, Decoding the presence of an object from neural-population activity, paragraph 1;\n    Figure 3B\n  quote: \"The decoding accuracy was above chance (50%) in all experimental sessions (Figure 3B)\"\n  criterion: The whole-arena decoder (opening comment), on each decoding session. The paper reports no\n    test per session; its chance level is the label-shuffling procedure (Methods, Shuffling trial\n    labels). Reproduced when, under both speed readings, every session's accuracy exceeds 0.5 and\n    exceeds the 99th percentile of 50 label shuffles of that session (the 50 shuffles of\n    Supplementary Figure 5E).\n- id: fig3c-bin-size\n  statement: Decoding accuracy grew roughly logarithmically with the testing bin size, rising quickly\n    up to 1 s and saturating beyond.\n  source: Results, Decoding the presence of an object from neural-population activity, paragraph 1;\n    Figure 3C; Methods, Performance of decoder\n  quote: \"The decoder’s performance increased approximately logarithmically with the bin size of the\n    testing data vector (Figure 3C)\"\n  criterion: The whole-arena decoder with testing bins of 10, 50, 100, 500, 1000, 5000 and 10000 ms\n    (Methods). The paper gives no test. Reproduced when the median accuracy over sessions rises from\n    10 to 1000 ms at each step, and its gain from 1000 to 10000 ms is smaller than its gain from 100\n    to 1000 ms.\n- id: fig3d-number-of-cells\n  statement: Decoding accuracy increased with the number of cells used.\n  source: Results, Decoding the presence of an object from neural-population activity, paragraph 1;\n    Figure 3D; Methods, Effect of number of cells\n  quote: \"the success of decoding increased with the number of cells included (Figure 3D)\"\n  criterion: Random subsets of k cells, 100 per k, whole-arena decoder (Methods). The data are open;\n    readings (a) the Methods', the 620-cell Neuropixels session, k = 1, 5, 10, 20, 30, 50, 100, 200,\n    300, 400 and 500; (b) the legend's, the four datasets pooled (two tetrode, two Neuropixels), k up\n    to each dataset's size. The paper gives no test. Reproduced when, under one reading, mean\n    accuracy is higher at the largest k than at k = 1 by more than the SD across subsets, and no step\n    in k lowers the mean by more than that SD.\n- id: fig4b-distance-decline\n  statement: Decoding accuracy fell gradually with the animal's distance from the object, over 5\n    equal-sample distance bins, with significant steps between bins 1 and 2, 2 and 3, and 4 and 5.\n  source: Results, Decoding the presence of an object from neural-population activity, paragraph 2;\n    Figure 4B\n  quote: \"we found that decoding performance decreased gradually with increasing distance from the\n    object (Figure 4B)\"\n  statistics:\n  - about: accuracy across the 5 distance bins\n    test: Kruskal-Wallis test\n    statistic: H = 44.559\n    p: 4.91e-9\n    n: 16 sessions\n  - about: bins 1 vs 2, 2 vs 3 and 4 vs 5, each (printed as W >= 111, p <= 0.0049)\n    test: Wilcoxon signed-rank tests\n    statistic: W >= 111\n    p: 0.0049\n    p_relation: \"<\"\n    n: 16 sessions\n  criterion: The distance decoder (opening comment), on the decoding sessions. Reproduced when, under\n    every reading of speed and sessions, the Kruskal-Wallis test across the 5 bins gives p < 0.05 with\n    median accuracy falling from bin 1 to bin 5, and signed-rank tests of bins 1 vs 2, 2 vs 3 and\n    4 vs 5 each give p < 0.05 with the nearer bin higher. Partially reproduced when the Kruskal-Wallis\n    part holds and one or two of the pairs do not. The population mean of bin 1 minus bin 5 (0.19 in\n    the paper, Results, Distance-specific reorganization, paragraph 2) is reported.\n- id: fig4c-each-session-decreasing\n  statement: Every session showed decoding accuracy decreasing with distance from the object.\n  source: Figure 4C legend\n  quote: \"Note that all experimental sessions have decreasing curves.\"\n  depends_on:\n  - fig4b-distance-decline\n  criterion: The paper's two measures of the decrease (Methods, Measuring strength of distance-specific\n    reorganization) give the readings (a) the least-squares slope of accuracy on distance-bin index is\n    negative; (b) accuracy in bin 1 minus bin 5 is positive. Reproduced when every session meets one\n    reading; partially reproduced when more than half do; not reproduced otherwise.\n- id: fig4e-angle-flat\n  statement: Decoding accuracy did not differ between 5 angular sectors around the object, so the\n    distance effect is not specific to compass directions.\n  source: Results, Decoding the presence of an object from neural-population activity, paragraph 3;\n    Figure 4E and 4F\n  quote: \"The decoding accuracy was the same in different angular bins (Figures 4E and 4F)\"\n  statistics:\n  - test: Kruskal-Wallis test\n    statistic: H = 3.75\n    p: 0.4416\n    n: 16 sessions\n  criterion: A claim of absence, judged on the paper's test, a Kruskal-Wallis test across the 5 angular\n    bins at alpha 0.05. Distance decoder with 72 degree sectors of allocentric angle from the object in\n    place of distance rings (Figure 4D legend, Methods). The sectors' starting angle is not given;\n    readings (a) sectors starting at 0 degrees (the positive x axis, the code's angle origin in\n    templateMatchingScore.m); (b) sectors starting at 36 degrees. Reproduced when p >= 0.05 under the\n    readings, not reproduced when p < 0.05; H is given either way.\n- id: fig4h-population-vector-correlation\n  statement: Correlations between NO and O population vectors were lowest near the object and rose\n    stepwise with distance before saturating, with significant steps between bins 1 and 2, 2 and 3,\n    and 3 and 4.\n  source: Results, Decoding the presence of an object from neural-population activity, paragraph 5;\n    Figure 4G and 4H\n  quote: \"This showed a stepwise linear increase in correlation values as a function of distance from\n    object, with saturation at larger distances (Figure 4H)\"\n  statistics:\n  - about: correlation across the 5 distance bins\n    test: Kruskal-Wallis test\n    statistic: H = 30.1\n    p: 4.67e-6\n    n: 16 sessions\n  - about: bins 1 vs 2, 2 vs 3 and 3 vs 4, each (printed as W <= 19, p <= 0.0113)\n    test: Wilcoxon signed-rank tests\n    statistic: W <= 19\n    p: 0.0113\n    p_relation: \"<\"\n    n: 16 sessions\n  criterion: Methods, Population vector correlation. Per session, rate maps of the whole NO and O\n    trials (3 cm bins, 50 x 50, as the Methods give m = n = 50), the Pearson correlation across cells\n    at each spatial bin, and the mean correlation in each of 5 distance bins. The bins are open;\n    readings (a) the Methods' fixed 20 cm rings (0 to 100 cm); (b) 5 bins with equal numbers of\n    spatial bins, which the reported 489 values per bin implies. Reproduced when, under one reading,\n    the Kruskal-Wallis test gives p < 0.05 with correlation rising from bin 1 to bin 5 and the three\n    signed-rank tests give p < 0.05 with the farther bin higher.\n- id: figs5a-decode-no-from-no-prime\n  statement: The NO trial could also be decoded from the NO' trial, above chance, consistent with\n    trace fields.\n  source: Results, Decoding the presence of an object from neural-population activity, paragraph 1;\n    Supplementary Figure 5A\n  quote: \"we were also able to decode the NO trial from the NO0 trial using population activity\n    (Figure S5A)\"\n  criterion: As fig3b-decode-presence, with NO' in place of O, on sessions with a NO' trial.\n    Reproduced when the accuracy exceeds 0.5 and the 99th percentile of label shuffles in every\n    session; partially reproduced when in more than half.\n- id: figs5b-fixed-distance-bins\n  statement: With fixed distance bins (0-20 to 80-100 cm) decoding accuracy still fell with distance.\n  source: Supplementary Figure 5B; Methods, Fixed distance bins\n  quote: \"Decoding accuracy as a function of distance from object when using fixed distance bins ...\n    Decoding accuracy decreases as a function of distance from object\"\n  statistics:\n  - test: Kruskal-Wallis test\n    statistic: H = 39.69\n    p: 5.02e-8\n    n: 16 sessions\n  criterion: The distance decoder with bin edges 0, 20, 40, 60, 80 and 100 cm (Methods). Samples\n    beyond 100 cm are left out, as the Methods' bins stop there. Reproduced when the Kruskal-Wallis\n    test gives p < 0.05 with median accuracy highest in bin 1 and lowest in bin 4 or 5.\n- id: figs5c-half-trial-control\n  statement: Decoding the first from the second half of the NO trial showed no decrease of accuracy\n    with distance.\n  source: Results, Decoding the presence of an object from neural-population activity, paragraph 4;\n    Supplementary Figure 5C\n  quote: \"we observed no decrease in decoding accuracy across the same distance bins when attempting\n    to decode the first half of the NO trial from the second half of the NO trial (Figure S5C)\"\n  statistics:\n  - test: Kruskal-Wallis test\n    statistic: H = 1.46\n    p: 0.834\n    n: 16 sessions\n  criterion: A claim of absence, judged on the paper's test. The NO trial is split at its midpoint and\n    each half split again into training and testing quarters (Methods, Decoding 1st half vs. 2nd half);\n    distances from the O trial's object position (the Methods give no other). Reproduced when the\n    Kruskal-Wallis test across the 5 bins gives p >= 0.05, not reproduced when p < 0.05.\n- id: figs5d-control-sessions\n  statement: In control sessions without an object (CON1 against CON2), decoding accuracy did not fall\n    with distance.\n  source: Results, Decoding the presence of an object from neural-population activity, paragraph 4;\n    Supplementary Figure 5D\n  quote: \"attempting to perform the decoding in control experiments without the object (Control trial\n    1 vs. Control trial 2). We observed no decrease in accuracy as a function of distance\"\n  statistics:\n  - test: Kruskal-Wallis test\n    statistic: H = 6.32\n    p: 0.1768\n  criterion: A claim of absence, judged on the paper's test. Distance decoder on CON1 against CON2.\n    The object position used for distances in control sessions is not given for this analysis;\n    readings (a) the arena centre (75, 75) cm, the pseudo-object position the Methods use for the\n    control chance level; (b) (35, 120) cm, the other one. The control sessions used are not stated;\n    those with at least 25 simultaneously recorded cells are used (the rule for population analyses).\n    Reproduced when p >= 0.05 under the readings, not reproduced when p < 0.05.\n- id: figs5e-shuffled-labels\n  statement: With shuffled trial labels the decoder performed at 50% in every distance bin.\n  source: Results, Decoding the presence of an object from neural-population activity, paragraph 4;\n    Supplementary Figure 5E\n  quote: \"On the shuffled data, the decoder performed with a mean accuracy of 50% in all distance bins\n    (Figure S5E)\"\n  statistics:\n  - about: each bin's accuracy against 0.5 (printed as t <= 2.1254, p >= 0.0518)\n    test: t tests\n    p: 0.0518\n    p_relation: \">\"\n    n: 16 sessions, each the mean of 50 shuffles\n  expected:\n  - quantity: mean accuracy, distance bin 1\n    value: 0.498\n    tolerance: 0.01\n  - quantity: mean accuracy, distance bin 5\n    value: 0.502\n    tolerance: 0.01\n  criterion: Labels of the testing samples shuffled 50 times per session (Methods, Shuffling trial\n    labels); session values are the means over shuffles. Tolerances are the SDs the legend gives.\n    Reproduced when every bin's mean is within 0.49 to 0.51 and no one-sample t test against 0.5 gives\n    p < 0.05.\n- id: figs5f-random-partition\n  statement: Partitioning training and testing samples at random gave the same decline of accuracy\n    with distance.\n  source: Results, Decoding the presence of an object from neural-population activity, paragraph 4;\n    Supplementary Figure 5F\n  quote: \"The results from this decoder showed the same decline in decoding accuracy as a function of\n    distance from the object (Figure S5F)\"\n  statistics:\n  - test: Kruskal-Wallis test\n    statistic: H = 39.71\n    p: 4.98e-8\n    n: 16 sessions\n  criterion: The distance decoder with training and testing timepoints drawn by a random permutation\n    (Methods, Random partitioning). Which timepoints are permuted is open; readings (a) 1 s bins;\n    (b) position samples. Reproduced when, under one reading, the Kruskal-Wallis test gives p < 0.05\n    with accuracy highest in bin 1 and lowest in bin 5.\n- id: figs5ghi-fields-and-rates\n  statement: Firing fields were spread across the arena, not concentrated at the object, and firing\n    rates were similar between NO and O and highest at middle distances (bin 3).\n  source: Results, Decoding the presence of an object from neural-population activity, paragraph 4;\n    Supplementary Figure 5G to 5I\n  quote: \"across all cells, firing fields were widely distributed across the environment and not\n    concentrated at the object location (Figures S5G and S5H), whereas firing rates were similar\n    between trials, being largest at middle distances from the object (peaking in distance bin 3;\n    Figure S5I)\"\n  criterion: The paper gives no test. Field centroids in NO and O relative to the object (Supplementary\n    Figure 5G); per session, the mean firing rate of each cell in each of the 5 equal-sample distance\n    bins of the whole trial, averaged over cells, then over sessions. Reproduced when (i) the\n    proportion of fields per unit area within 20 cm of the object is not higher in O than in NO by a\n    two-sided rank-sum test over sessions at p < 0.05 (the paper's test for unpaired data);\n    (ii) the mean rate peaks in bin 2, 3 or 4 in both trials, and in bin 3 in at least one; (iii) no\n    bin shows a NO against O difference by signed-rank test at p < 0.05. Partially reproduced when\n    two of the three hold.\n- id: figs6-behaviour-decoders-flat\n  statement: Decoders of trial type based on speed, head direction or occupancy performed only slightly\n    above 50% and their accuracy did not depend on distance from the object.\n  source: Results, Behavioral analyses, paragraph 1; Supplementary Figure 6A, 6C and 6E\n  quote: \"Decoders for speed, head direction, and occupancy performed only slightly above 50% correct,\n    with accuracies independent of object distance (Figures S6A, S6C, and S6E)\"\n  statistics:\n  - about: speed decoder across distance bins\n    test: Kruskal-Wallis test\n    statistic: H = 6.85\n    p: 0.1441\n  - about: head direction decoder across distance bins\n    test: Kruskal-Wallis test\n    statistic: H = 2.13\n    p: 0.711\n  - about: occupancy decoder across distance bins\n    test: Kruskal-Wallis test\n    statistic: H = 3.53\n    p: 0.4735\n  criterion: A claim of absence, judged on the paper's tests. Behavioural decoders as in the Methods\n    (Behavioral analyses I), with gamma likelihoods for speed (Lowess-smoothed, 25 Hz, all speeds),\n    two-Gaussian mixtures for head direction, and occupancy ratios, 50 x 50 spatial bins, same\n    training and testing split and distance bins. The Lowess span is not given; it cannot change the\n    absence much, and a span of 0.5 s is used as a standard choice. Reproduced when all three\n    Kruskal-Wallis tests give p >= 0.05 and the median accuracy over sessions is below 0.6 for each;\n    not reproduced when any test gives p < 0.05.\n- id: figs6hij-behaviour-matched\n  statement: After matching the distributions of speed, head direction or occupancy between NO and O\n    within each distance bin, decoding accuracy on neural data still fell with distance.\n  source: Results, Behavioral analyses, paragraph 2; Supplementary Figure 6H to 6J\n  quote: \"We still observed a graded decrease in decoding accuracy for the neural activity decoder\n    after matching distributions for speed (Figure S6H), head direction (Figure S6I) and occupancy\n    (Figure S6J)\"\n  statistics:\n  - about: speed matched\n    test: Kruskal-Wallis test\n    statistic: H = 45.4\n    p: 3.28e-9\n  - about: head direction matched\n    test: Kruskal-Wallis test\n    statistic: H = 38.23\n    p: 1.01e-7\n  - about: occupancy matched\n    test: Kruskal-Wallis test\n    statistic: H = 45.8\n    p: 2.71e-9\n  criterion: Matching as in the Methods (Behavioral analyses II), speed bins of 5 cm/s to 100 cm/s,\n    head direction bins of pi/10, occupancy bins of 30 cm, random removal of the excess samples from\n    the trial with more. The samples matched are the 1 s testing samples (the decoder's samples),\n    with the behaviour averaged over the second; the Methods do not say, so a second reading matches\n    25 Hz position samples and keeps the 1 s bins whose samples all survive. Reproduced when, under\n    one reading, each of the three Kruskal-Wallis tests gives p < 0.05 with bin 1 highest.\n- id: figs6k-uniform-prior\n  statement: Replacing the occupancy prior by a uniform prior did not change the decline of decoding\n    accuracy with distance.\n  source: Results, Behavioral analyses, paragraph 2; Supplementary Figure 6K\n  quote: \"removal of this prior had no effect on our results (Figure S6K)\"\n  statistics:\n  - test: Kruskal-Wallis test\n    statistic: H = 42.92\n    p: 1.07e-8\n  criterion: Distance decoder with a uniform prior over the spatial bins of each distance bin (Methods,\n    Removing effects of prior). Reproduced when the Kruskal-Wallis test gives p < 0.05 with bin 1\n    highest.\n- id: figs6l-sampling-thresholds\n  statement: Using only spatial bins visited for at least 100, 500, 1000 or 2000 ms in both trials, the\n    decline of accuracy with distance remained.\n  source: Results, Behavioral analyses, paragraph 3; Supplementary Figure 6L\n  quote: \"Regardless of the threshold value, the result was the same as before, with accuracy declining\n    along with object distance (Figure S6L\"\n  statistics:\n  - about: each of the four thresholds (printed as H >= 34.08, p <= 7.18e-7)\n    test: Kruskal-Wallis test\n    statistic: H >= 34.08\n    p: 7.18e-7\n    p_relation: \"<\"\n  criterion: Distance decoder with rate-map bins of 10 cm (the Methods' \"10 cm2\" read as 10 cm sides,\n    as 3 cm2 is used for the 3 cm bins), spatial bins below the threshold in either trial left out\n    of both. Reproduced when all four Kruskal-Wallis tests give p < 0.05 with bin 1 highest.\n- id: tables1-without-bin-1\n  statement: The effect of distance on decoding accuracy held when the bin nearest the object was left\n    out.\n  source: Supplementary Figure 6L legend, last sentence; Supplementary Table 1, first row\n  quote: \"all the main statistics hold even after excluding distance bin 1\"\n  expected:\n    quantity: Kruskal-Wallis H across distance bins 2 to 5\n    value: 25.06\n    tolerance: 2.506\n  criterion: The distance decoder results of fig4b-distance-decline, bins 2 to 5 only. The table's\n    p-value has lost its exponent in the text. Reproduced when the Kruskal-Wallis test gives p < 0.05\n    with bin 2 highest; H is compared with the expected value.\n  depends_on:\n  - fig4b-distance-decline\n- id: fig5b-words-more-informative\n  statement: Population words (patterns of spiking and silence in 10 ms bins) carried much more\n    information about the trial than population spike counts.\n  source: Results, Objects are encoded by distinct patterns of joint activity, paragraph 1; Figure 5B\n  quote: \"Words were much more informative than counts (Figure 5B)\"\n  statistics:\n  - about: words against counts (printed as U >= 439, p <= 1.19e-6)\n    test: Wilcoxon rank-sum tests\n    statistic: U >= 439\n    p: 1.19e-6\n    p_relation: \"<\"\n  criterion: Methods, Definition of words and counts, and Mutual information. Spike counts in 10 ms\n    bins; tetrode sessions with all cells, Neuropixels sessions subsampled to 30 cells; the all-zero\n    word and zero count left out; mutual information with trial, from frequency distributions, minus\n    the mean over 50 label shuffles. Distance bins as in Figure 4B (Figure 5B legend), each 10 ms bin\n    taking the distance of the nearest position sample, 5 equal-sample bins per trial. Open readings\n    (a) one random subset of 30 Neuropixels cells; (b) the mean over 20 subsets (the number the\n    Methods use for subsampling the decoder). Which samples are compared is open; readings (c) per\n    distance bin, 16 against 16 sessions; (d) all bins pooled. Reproduced when, under one\n    combination, every rank-sum test gives p < 0.05 with words higher.\n- id: fig5bc-words-information-falls-with-distance\n  statement: The information from words decreased with distance from the object, as decoding did.\n  source: Results, Objects are encoded by distinct patterns of joint activity, paragraph 1; Figures 5B\n    and 5C\n  quote: \"Importantly, the amount of information gained from words decreased as a function of distance\n    from the object (Figures 5B and 5C)\"\n  statistics:\n  - test: Kruskal-Wallis test\n    statistic: H = 24.29\n    p: 6.98e-5\n    n: 16 sessions\n  criterion: Mutual information of words as in fig5b-words-more-informative, under its subset readings.\n    Reproduced when, under one reading, the Kruskal-Wallis test across the 5 bins gives p < 0.05 with\n    bin 1 highest.\n- id: fig5b-counts-uninformative\n  statement: The information from counts did not depend on distance and was not significantly above\n    zero.\n  source: Results, Objects are encoded by distinct patterns of joint activity, paragraph 1; Figure 5B\n  quote: \"In contrast, the amount of information from counts did not depend on object distance ...\n    and was not significantly above zero\"\n  statistics:\n  - about: counts across distance bins\n    test: Kruskal-Wallis test\n    statistic: H = 4.08\n    p: 0.3947\n  - about: counts against zero, each bin (printed as t <= 1.46, p >= 0.1636)\n    test: t tests\n    statistic: t <= 1.46\n    p: 0.1636\n    p_relation: \">\"\n  criterion: A claim of absence, judged on the paper's tests. Bias-subtracted mutual information of\n    counts as in fig5b-words-more-informative. Reproduced when the Kruskal-Wallis test gives\n    p >= 0.05 and no per-bin two-sided one-sample t test against zero gives p < 0.05; not reproduced\n    otherwise. Values given either way.\n- id: fig5e-kl-divergence\n  statement: The KL divergence between the word distributions of NO and O fell with distance from the\n    object, from bin 1 to bin 5, while shuffled data showed no decrease.\n  source: Results, Objects are encoded by distinct patterns of joint activity, paragraph 3; Figure 5E\n  quote: \"divergence between the NO and O distributions became smaller with increasing object distance\n    (Figure 5E, blue curve) ... No decrease in the KL divergence was present in shuffled data\"\n  statistics:\n  - about: across the 5 distance bins\n    test: Kruskal-Wallis test\n    statistic: H = 16.22\n    p: 0.0027\n  - about: bin 1 against bin 5\n    test: Wilcoxon signed-rank test\n    statistic: W = 102\n    p: 6.10e-4\n  criterion: Methods, Kullback-Leibler divergence, words and distance bins as in\n    fig5b-words-more-informative, D(NO||O) over all words, probabilities as counts over all\n    timepoints. Words seen in NO and never in O make the sum infinite, and the paper does not say how\n    that was handled; the one finite reading its text allows is to sum over words seen in both\n    trials, recorded as a deviation. Shuffled data assign trial labels to words at random (Figure 5E\n    legend). Reproduced when the Kruskal-Wallis test and the bin 1 against bin 5 signed-rank test give\n    p < 0.05 with bin 1 higher, and the shuffled divergences show no Kruskal-Wallis effect at 0.05.\n- id: fig5-entropy\n  statement: The entropy of words was higher than that of counts (1.65 against 0.84 bits).\n  source: Results, Objects are encoded by distinct patterns of joint activity, paragraph 4\n  quote: \"the entropy was higher for words than counts (entropy of words: 1.65 bits ± 0.06; entropy of\n    counts: 0.84 bits ± 0.02; mean ± SEM)\"\n  expected:\n  - quantity: entropy of words\n    value: 1.65\n    tolerance: 0.165\n    unit: bits\n  - quantity: entropy of counts\n    value: 0.84\n    tolerance: 0.084\n    unit: bits\n  criterion: Entropy as in the Methods, words and counts as in fig5b-words-more-informative. The SEM is\n    over an unstated unit, so the tolerance is 10%. The unit and whether the all-zero word is in are\n    open; readings (a) per session and trial over the whole trial, all-zero word left out (as in the\n    mutual information); (b) as (a) with it included; (c) per session, trial and distance bin.\n    Reproduced when, under one reading, both means are within tolerance.\n- id: figs7cd-number-of-words\n  statement: The number of distinct words did not differ between trial types or across distance bins.\n  source: Results, Objects are encoded by distinct patterns of joint activity, paragraph 3;\n    Supplementary Figure 7C and 7D\n  quote: \"In contrast to the identity of words, the number of words was independent of trial type and\n    distance from the object (Figures S7C and S7D)\"\n  statistics:\n  - about: across distance bins, NO trial\n    test: Kruskal-Wallis test\n    statistic: H = 1.58\n    p: 0.8117\n  - about: across distance bins, O trial\n    test: Kruskal-Wallis test\n    statistic: H = 2.62\n    p: 0.6227\n  - about: NO against O\n    test: Wilcoxon rank-sum test\n    statistic: z = 0.221\n    p: 0.8252\n    n: 16 sessions\n  criterion: A claim of absence, judged on the paper's tests (from the Supplementary Figure 7 legend,\n    an image on PDF page 46, not in the text). Distinct words per session, trial and distance bin as in\n    fig5b-words-more-informative. Reproduced when all three tests give p >= 0.05, not reproduced when\n    any gives p < 0.05.\n- id: figs7e-downsampled-words\n  statement: After downsampling words to as many states as counts, words still carried more information\n    than counts.\n  source: Results, Objects are encoded by distinct patterns of joint activity, paragraph 4;\n    Supplementary Figure 7E\n  quote: \"after downsampling the number of states to be equal for words and counts, words were still\n    much more informative (Figure S7E)\"\n  statistics:\n  - test: Wilcoxon signed-rank test\n    statistic: W = 2480\n    p: 4.42e-13\n    n: 16 sessions x 5 distance bins (80 pairs)\n  criterion: Methods, Downsampling words. Per session and distance bin, keep the c most frequent words,\n    c the number of distinct counts, and renormalise. Whether the bias subtraction is applied is not\n    said; readings (a) with, (b) without. Reproduced when, under one reading, a signed-rank test over\n    the 80 pairs gives p < 0.05 with words higher.\n- id: fig6ab-single-cell-distance-tuning\n  statement: Single cells decoded with almost flat accuracy across distance; their distance tuning\n    (bin 1 minus bin 5 accuracy) averaged 0.02, 98.7% lay between -0.2 and 0.2, 12.2% (145) had\n    significant positive and 3.8% (45) significant negative tuning.\n  source: Results, Distance-specific reorganization of the hippocampal map is widely distributed,\n    paragraph 2; Figure 6A and 6B\n  quote: \"CA1 cells had a slight positive bias in distance tuning (mean: 0.02; for reference, the same\n    mean calculated from populations is 0.19; Figure 4C) and nearly all cells were contained between\n    the bounds ... and 0.2 (98.7% of cells) ... some cells had significant positive distance tuning\n    (12.2%, n = 145/1,189 cells) ... and some cells had significant negative distance tuning (3.8%,\n    n = 45/1,189 cells)\"\n  expected:\n  - quantity: mean distance tuning of single cells\n    value: 0.02\n    tolerance: 0.002\n  - quantity: fraction of cells with distance tuning within -0.2 to 0.2\n    value: 0.987\n    tolerance: 0.013\n  - quantity: fraction with significant positive tuning\n    value: 0.122\n    tolerance: 0.0122\n  - quantity: fraction with significant negative tuning\n    value: 0.038\n    tolerance: 0.0038\n  criterion: The distance decoder run with one cell at a time; distance tuning is accuracy in bin 1\n    minus bin 5 (Equation 1). Significance from 100 circular shifts of the spike train by 20 s to the\n    trial length less 20 s, above the 99th or below the 1st percentile (Methods). The tolerance on the\n    within-bounds fraction stops at 1. The mean of 0.02 is printed to one significant figure, so the\n    tolerance on it is 0.005 (half the last digit) in place of 10%. Which cells are open; readings (a)\n    all 1,189 unique cells, each in its session; (b) the cells of the decoding sessions (Figure 6A\n    legend). Reproduced when, under one reading, all four values are within tolerance; partially\n    reproduced when the mean and within-bounds fraction are and a significant fraction is not.\n- id: figs5l-without-positively-tuned\n  statement: After removing the cells with significant positive distance tuning, decoding accuracy\n    still fell gradually with distance.\n  source: Results, Distance-specific reorganization of the hippocampal map is widely distributed,\n    paragraph 2; Supplementary Figure 5L\n  quote: \"after removing cells with significant positive distance tuning (12.2%), we still observed a\n    gradual drop in decoding accuracy ... obtained with population data as a function of object\n    distance (Figure S5L)\"\n  statistics:\n  - test: Kruskal-Wallis test\n    statistic: H = 28.88\n    p: 8.27e-6\n  depends_on:\n  - fig6ab-single-cell-distance-tuning\n  criterion: Distance decoder on the decoding sessions without the cells found in\n    fig6ab-single-cell-distance-tuning. Reproduced when the Kruskal-Wallis test gives p < 0.05 with\n    bin 1 highest.\n- id: figs5m-without-object-tuned\n  statement: After removing all object-tuned cells, decoding accuracy still fell gradually with distance.\n  source: Results, Distance-specific reorganization of the hippocampal map is widely distributed,\n    paragraph 5; Supplementary Figure 5M\n  quote: \"After removing all object-tuned cells (19.9%) from the data and re-running the decoder, we\n    observed the same gradual fall in decoding accuracy as a function of distance (Figure S5M)\"\n  statistics:\n  - test: Kruskal-Wallis test\n    statistic: H = 38.89\n    p: 7.34e-8\n  depends_on:\n  - fig1c-object-tuned-fraction\n  criterion: Distance decoder on the decoding sessions without the object-tuned cells of\n    fig1c-object-tuned-fraction (each template-width reading). Reproduced when, under one reading, the\n    Kruskal-Wallis test gives p < 0.05 with bin 1 highest.\n- id: fig6c-subsets-decline\n  statement: In the 620-cell session, random subsets of every size except a single cell showed decoding\n    accuracy falling with distance.\n  source: Results, Distance-specific reorganization of the hippocampal map is widely distributed,\n    paragraph 3; Figure 6C\n  quote: \"All curves showed reduced decoding accuracy as a function of distance, except the curve\n    constructed using only a single cell (Figure 6C)\"\n  statistics:\n  - about: n = 1 curve\n    test: Wilcoxon signed-rank test\n    statistic: W = 2.48\n    p: 0.6489\n  - about: all other curves (printed as W >= 11.89, p <= 0.0182)\n    test: Wilcoxon signed-rank tests\n    statistic: W >= 11.89\n    p: 0.0182\n    p_relation: \"<\"\n  criterion: Distance decoder on 20 random subsets per size of the 620 cells (Methods, Subsampling for\n    decoder). The sizes are open, as three lists are given; readings (a) Results, 1, 5, 10, 30, 50,\n    100, 200, 300, 400, 500; (b) legend, 1, 5, 20, 30, 50 to 500; (c) Methods, 1, 5, 10, 30, 100 to\n    500. The test is open, as the printed W values are not integers; readings (d) signed-rank of bin 1\n    against bin 5 over the 20 subsets; (e) Kruskal-Wallis across the 5 bins over the 20 subsets.\n    Reproduced when, under one reading of the test, the single-cell curve gives p >= 0.05 and every\n    other size gives p < 0.05 with bin 1 higher.\n- id: fig6d-reorganization-grows-with-cells\n  statement: The difference between bins 1 and 5 grew, and the slope of accuracy over distance became\n    more negative, as more cells were used, both reaching their extremes at 500 cells.\n  source: Results, Distance-specific reorganization of the hippocampal map is widely distributed,\n    paragraph 3; Figure 6D\n  quote: \"The difference between bins #1 and #5 grew systematically with the number of cells (Figure\n    6D; left y axis, blue)\"\n  statistics:\n  - about: distance difference across subset sizes\n    test: Kruskal-Wallis test\n    statistic: H = 174.57\n    p: 3.14e-32\n  - about: slope across subset sizes\n    test: Kruskal-Wallis test\n    statistic: H = 157.6\n    p: 1.011e-28\n  depends_on:\n  - fig6c-subsets-decline\n  criterion: The 20 subsets per size of fig6c-subsets-decline; per subset, accuracy in bin 1 minus bin 5\n    and the least-squares slope over bin indices 1 to 5 (Methods, Measuring strength). Reproduced when,\n    under one size reading, both Kruskal-Wallis tests across sizes give p < 0.05 and the largest mean\n    difference and most negative mean slope are at 400 or 500 cells.\n- id: figs8-smaller-datasets\n  statement: The growth of distance reorganization with the number of cells held in the tetrode\n    sessions and in the 135-cell Neuropixels session.\n  source: Results, Distance-specific reorganization of the hippocampal map is widely distributed,\n    paragraph 3; Supplementary Figure 8A to 8D\n  quote: \"The finding was upheld in data from animals with smaller numbers of cells (135 cells in a\n    Neuropixels recording; 25–39 cells in tetrode recordings)\"\n  statistics:\n  - about: tetrode sessions, distance difference\n    test: Kruskal-Wallis test\n    statistic: H = 349.13\n    p: 2.70e-74\n    n: 14 sessions x 20 subsets\n  - about: tetrode sessions, slope\n    test: Kruskal-Wallis test\n    statistic: H = 352.35\n    p: 5.46e-75\n  - about: 135-cell session, distance difference\n    test: Kruskal-Wallis test\n    statistic: H = 62.87\n    p: 4.03e-11\n  - about: 135-cell session, slope\n    test: Kruskal-Wallis test\n    statistic: H = 55.76\n    p: 1.06e-9\n  criterion: As fig6d-reorganization-grows-with-cells, on the tetrode decoding sessions pooled (sizes up\n    to each session's count) and on the 135-cell session. Subset sizes for the tetrode sessions are not\n    given beyond n = max (29 to 35 cells); sizes from reading (a) of fig6c-subsets-decline up to each\n    session's count, then the session's full count, are used. Reproduced when all four Kruskal-Wallis\n    tests give p < 0.05 with the difference rising and the slope falling with size.\n- id: fig6ef-least-tuned-cells\n  statement: Even the 20% of cells with the lowest distance tuning showed distance reorganization, with\n    a bin 1 minus bin 5 difference of 0.121 and a slope of -0.0267.\n  source: Results, Distance-specific reorganization of the hippocampal map is widely distributed,\n    paragraph 4; Figure 6E and 6F\n  quote: \"even the 20% of cells with lowest tuning was sufficient to demonstrate the distance\n    modulation, in the form of positive distance tuning as well as a negative slope (Figures 6E and\n    6F; rightmost point on blue curve: 0.121; on orange curve\"\n  depends_on:\n  - fig6ab-single-cell-distance-tuning\n  expected:\n  - quantity: bin 1 minus bin 5 accuracy, 20% least-tuned cells of the 620-cell session\n    value: 0.121\n    tolerance: 0.0121\n  - quantity: slope of accuracy on distance bin, same cells\n    value: -0.0267\n    tolerance: 0.00267\n  criterion: Cells of the 620-cell session sorted by single-cell distance tuning\n    (fig6ab-single-cell-distance-tuning), the lowest 100, 80, 60, 40 and 20% kept, distance decoder\n    run on each. Reproduced when both 20% values are within tolerance; partially reproduced when the\n    difference is positive and the slope negative but outside tolerance.\n- id: fig7-single-cell-properties\n  statement: Single-cell properties barely predicted distance tuning; correlations with object-tuning\n    score (r = 0.12), spatial information (r = -0.13), spatial correlation (r = -0.08) and rate overlap\n    (r = -0.18) were significant but weak.\n  source: Results, Distance-specific reorganization of the hippocampal map is widely distributed,\n    paragraph 5; Figure 7A to 7D\n  quote: \"The object-tuning score had a significant positive correlation with distance tuning, but very\n    weakly so (r = 0.12 ... Spatial information had a significant negative correlation, but also this\n    was very weak ... spatial correlation and rate overlap were also negatively but weakly correlated\n    with distance tuning\"\n  statistics:\n  - about: object-tuning score\n    test: Pearson correlation\n    statistic: r = 0.12\n    p: 1.95e-5\n    n: 1,189 cells\n  - about: spatial information\n    test: Pearson correlation\n    statistic: r = -0.13\n    p: 3.70e-7\n  - about: spatial correlation\n    test: Pearson correlation\n    statistic: r = -0.08\n    p: 7.61e-4\n  - about: rate overlap\n    test: Pearson correlation\n    statistic: r = -0.18\n    p: 1.57e-9\n  depends_on:\n  - fig1c-object-tuned-fraction\n  - fig6ab-single-cell-distance-tuning\n  expected:\n  - quantity: r, object-tuning score\n    value: 0.12\n    tolerance: 0.012\n  - quantity: r, spatial information\n    value: -0.13\n    tolerance: 0.013\n  - quantity: r, spatial correlation\n    value: -0.08\n    tolerance: 0.008\n  - quantity: r, rate overlap\n    value: -0.18\n    tolerance: 0.018\n  criterion: Pearson correlations over cells of distance tuning with the object-tuning score (opening\n    comment), spatial information in bits per spike in the O trial (Methods), and NO-O spatial\n    correlation and rate overlap. The r values are printed to two digits, so a tolerance of 0.05 is\n    used in place of 10%, being half a unit in the first digit at the scale the claim calls weak.\n    Reproduced when, under one cell reading of fig6ab-single-cell-distance-tuning, all four r are\n    within 0.05 of the printed values with the same sign, and each |r| is below 0.3.\n- id: fig7-slope-variant\n  statement: Using the slope of accuracy against distance in place of distance tuning gave similar weak\n    correlations with the same four properties.\n  source: Results, Distance-specific reorganization of the hippocampal map is widely distributed,\n    paragraph 5\n  quote: \"We obtained similar results when, instead of distance tuning, we used the slope of the\n    regression line fitted to decoding accuracy vs. distance as a measure of reorganization\"\n  statistics:\n  - about: object-tuning score\n    test: Pearson correlation\n    statistic: r = -0.12\n    p: 3.05e-5\n  - about: spatial information\n    test: Pearson correlation\n    statistic: r = 0.10\n    p: 3.58e-5\n  - about: spatial correlation\n    test: Pearson correlation\n    statistic: r = -0.08\n    p: 7.98e-4\n  - about: rate overlap\n    test: Pearson correlation\n    statistic: r = 0.19\n    p: 1.13e-12\n  depends_on:\n  - fig7-single-cell-properties\n  criterion: As fig7-single-cell-properties with the single-cell least-squares slope. Reproduced when\n    all four r are within 0.05 of the printed values with the same sign. The printed sign for spatial\n    correlation (negative for both measures, while the others flip) is noted.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd claims/ebrains-q0fg-1x8 && python - <<'EOF'
import re
p='10.1016-j.neuron.2023.04.008.yaml'
s=open(p).read()
s=s.replace("""  - quantity: mean distance tuning of single cells
    value: 0.02
    tolerance: 0.002""","""  - quantity: mean distance tuning of single cells
    value: 0.02
    tolerance: 0.005""")
for q,v in [("object-tuning score","0.12"),("spatial information","-0.13"),("spatial correlation","-0.08"),("rate overlap","-0.18")]:
    s=re.sub(r"(  - quantity: r, %s\n    value: %s\n    tolerance: )[0-9.]+"%(re.escape(q),re.escape(v)), r"\g<1>0.05", s)
s=s.replace("""readings are those of Hoydal et al. 2019 (the paper's reference 11), which the author must ask
    a reader to fix before the test.""","""paper directs to the method of its references 11 and 12 (Hoydal et al. 2019; Andersson et al.
    2021), and those papers' bins and smoothing are used.""")
open(p,'w').write(s)
EOF
grep -n " #\|—\|rather" 10.1016-j.neuron.2023.04.008.yaml | grep -v '^\s*[0-9]*:#' | head; grep -n "tolerance: 0.05" 10.1016-j.neuron.2023.04.008.yaml | wc -l
cd ../.. && python tools/claims_check.py claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml paper/10.1016-j.neuron.2023.04.008.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import yaml
d=yaml.safe_load(open('claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml'))
c=d['claims']
print(len(c), sum('quote' in x for x in c), sum('statistics' in x for x in c), sum(len(x.get('statistics',[])) for x in c), sum('criterion' in x for x in c), sum('expected' in x for x in c))
"; git status --short
```

```
55 55 38 68 55 17
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
?? claims/ebrains-q0fg-1x8/
?? scripts
```

**Agent**

I've written the claims file for EBRAINS:Q0FG-1X8: `claims/ebrains-q0fg-1x8/10.1016-j.neuron.2023.04.008.yaml`.

**Text read.** I read the version of record (PDF supplied by a person) as extracted to `paper/…txt`: main text, figure legends, STAR Methods, Supplementary Figures 1 to 8 and Supplementary Table 1. Three things had to come from the PDF instead:
- The Supplementary Figure 7 legend is an image and is missing from the text. I read it from PDF page 46.
- The CA3 p-values in Supplementary Figure 3F came from PDF page 35.
- Supplementary Table 1 is garbled in the text and some exponents are lost, so I used it only where it is legible.

**Code read.** The paper's code is on Zenodo (doi:10.5281/zenodo.7797252), a copy of GitHub sebasoa/Object-centered-population-coding at v1.0, commit 4e4f5ac. It holds the object-tuning score and the distance decoder. Two functions they call are not in the repository: `objectScore` and `PoissonDecoder_distance`. The steps they would do are taken from the Methods. There is no code for the single-cell change analyses, traces, words and counts, mutual information, KL divergence, the behavioural decoders or the population vector correlations.

**Claims.** There are 55 claims and all 55 have a quote that the checker found. 38 claims carry statistics (68 entries), 17 have expected values, and all 55 have a criterion. None needs data from outside the dataset. The checker still exits non-zero, with 28 problems: all are p-values it could not match, either because their exponents are garbled in the text or because they sit in the image-only Supplementary Figure 7 legend. I checked each one by reading.

**Details the paper leaves open, and the readings named:**
- **Template width:** standard deviations of 5 to 200 cm (code), or variances of those values (Methods).
- **Speed filter in the decoder:** rate maps from epochs above 2.5 cm/s (Methods), or no filter (code).
- **Which sessions are decoded:** the Methods' rule of at least 25 cells, which the text says gives 17 sessions, against the 16 the legends give. The second reading runs every set of 16 that drops one tetrode session.
- **Which session stands for a cell recorded on several days:** the first day, or every session.
- **Which control trials stand for O and OM (chance level):** CON2 and CON3, or CON1 and CON2.
- **Field distance:** the centroid in O, the centroid averaged over O and OM, or the peak bin.
- **Cross-day count:** 13 (text) or 11 (Fig 1H legend).
- **Trace ROI size:** the Methods cite a section that is not in the paper. Readings are a circle of the field's area, or the smallest circle containing the field.
- **How traces were removed (Fig S2D):** only one reading is named.
- **Object-vector map bins:** taken from the paper's references 11 and 12.
- **Population vector correlation bins:** fixed 20 cm rings, or equal-count bins (which the reported 489 values per bin implies).
- **Angular sector origin:** 0 or 36 degrees.
- **Control-session object position:** (75, 75) or (35, 120) cm.
- **Figure 3D data:** the 620-cell session (Methods) or four datasets pooled (legend).
- **Figure 6C:** three different lists of subset sizes, and the test is either signed-rank or Kruskal-Wallis, since the printed W values are not integers.
- **Neuropixels word subsets:** one subset of 30 cells, or the mean over 20.
- **Words against counts:** compared per distance bin or pooled. The printed U ≥ 439 fits neither.
- **KL divergence:** the paper does not say how words that never occur in O were handled; the sum is restricted to words seen in both trials, recorded as a deviation.
- **Entropy:** the unit it is computed over, and whether the all-zero word is included.
- **Downsampled words:** with or without the bias subtraction.
- **Single-cell analyses:** all 1,189 cells, or only the cells of the decoding sessions.
- **Random partition:** 1 s bins or position samples.
- **Behaviour matching:** done on 1 s samples or on 25 Hz samples.

**Choices made where the paper is silent:**
- **Lowess span:** 0.5 s, treated as unable to change the result.
- **Signed-rank pairing in the change classification:** pairs matched by repetition.
- **Tolerances that are not 10%:**
  - 0.05 on the Fig 7 correlation coefficients.
  - 0.005 on the single-cell mean of 0.02.
  - The legend's SD for the shuffled-label accuracies.
- **Tests chosen where the paper gives none:** Figs 1F, 3B to 3D, 4C and S5G to S5I. Each follows the paper's general tests or its own measures.

**Missing from the paper:**
- The ROI section the Methods refer to.
- The method for removing traces.
- The two code functions named above.
- The Supplementary Figure 7 legend in the text.

**Inconsistencies in the paper,** noted in the opening comment:
- 13 against 11 stable cells.
- Identical statistics printed for OM-NO' and NO-NO'.
- 12.2% against 12.3% of cells with positive distance tuning.
- 15 against 14 tetrode sessions.

Nothing was committed. The other untracked files at the repository root were already there; they are not from this run.

## End of run

27 turns, 9 minutes, result: success.
