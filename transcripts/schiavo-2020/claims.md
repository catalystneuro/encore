# 000249 · claims · run 39996867811

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000249/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n '/^## Reader/,/^## Author/p' docs/protocol.md
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
ls claims/001453/ claims/000249/ paper/; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/10.1016-j.cub.2025.04.027.yaml | head -250
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
[... 230 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-020-2807-6.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41586-020-2807-6.txt",
 "offset": 7,
 "limit": 30
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)" "substr($0,1,100)}' *.txt
```

```
1: 30 DOI: 10.1038/s41586-020-2807-6
2: 30 Version: as served by ncbi_pmc
3: 46 Source: ncbi_pmc+crossref (paper-text-fetcher)
4: 18 Stored: 2026-10-20
5: 21 Extracted: as fetched
6: 72 ------------------------------------------------------------------------
7: 73903 Nature Nature 319 nihpa 0410462 Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collecti
8: 0 
9: 71 Innate and plastic mechanisms for maternal behaviour in auditory cortex
10: 0 
11: 165 [1] Swain, J. E., Kim, P. & Ho, S. S. Neuroendocrinology of parental response to baby-cry. J. Neuroe
12: 0 
13: 198 [2] Lingle, S., Wyman, M. T., Kotrba, R., Teichroeb, L. J. & Romanow, C. A. What makes a cry a cry? 
14: 0 
15: 144 [3] Dulac, C., O’Connell, L. A. & Wu, Z. Neural control of maternal and paternal behaviors. Science 
16: 0 
17: 145 [4] Zeskind, P. S. in Infant Crying: Theoretical and Research Perspectives (eds Boukydis, C. F. Z. a
18: 0 
19: 184 [5] Ehret, G., Koch, M., Haack, B. & Markl, H. Sex and parental experience determine the onset of an
20: 0 
[... 53 more lines not kept]
```

**Agent**

Line 7 holds the whole body. I'll read it in chunks.

**Agent calls Bash**

```bash
cd  sed -n 7p paper/*.txt | fold -w 4000 -s > $TMPDIR/body.txt; wc -l $TMPDIR/body.txt; sed -n 1,6p $TMPDIR/body.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 7,13p $TMPDIR/body.txt
```

```
back to the nest. If the pup was retrieved, the latency to retrieve was recorded. If the pup was not retrieved, the trial was marked a failure and another trial was initiated upon the mouse remaining in the nest for at least two minutes. Testing continued until each animal performed 8–16 trials, or testing could not continue as the result of nursing, cannibalization, or failure to enter the nest after three hours. Trials in which cold pups began vocalizing or warm pups failed to vocalize were excluded from analysis. Data from lactating dams and experienced virgins were pooled as there was no difference between groups ( Extended Data Fig. 2a ) A y-maze was used to assess approach towards pup calls in the absence of live pups ( Extended Data Fig. 2c ). Dams and their litters, along with cohoused virgins, were placed in a modified y-maze box (Plexiglas; 47×36×28 cm) 24 hours prior to testing. When testing a cohoused virgin, the dam was removed prior to testing and vice versa. At the start of each trial, three pups were placed in the left, right, and center chambers. After retrieval of all three pups, the speakers in the left and right chambers were simultaneously switched on to play competing pup call bouts (inter-bout interval: 1s). A prototypical call was played from one speaker, while the same call morphed in the temporal domain was played from the other. The calls played continuously until a chamber was chosen or the timeout period (two minutes) elapsed. Only the first room entrance was counted. Prototypical and morphed calls alternated left and right speakers across trials in a pseudorandom order. Room entry (% trials) was calculated by dividing the number of trials a female approached a stimulus by the total number of trials that given stimulus was played. Operant conditioning was used to assess behavioral responses to pup calls in naive virgins ( Fig. 1h , i ). The operant chamber (25×20×15 cm) consisted of an electrostatic speaker and metal lever connected to a
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 14,19p $TMPDIR/body.txt
```

```
with a dam and litter. Left, day 0: n=21 neurons, day 2: n=26. Right, day 1: n=57, day 2: n=26. Mean±s.e.m. g, Cumulative distribution of temporal tuning widths before (N=2 mice, n=78 neurons) and after the onset of reliable retrieval (n=52). A larger proportion of neurons were more broadly tuned (higher normalized ΔF/Fs) when EVs retrieved on 100% of trials (p<0.0001; two-tailed unpaired Kolmogorov-Smirnov test). Stats: *p<0.05, **p<0.01. Extended Data Figure 5. Pup-naive virgins did not increase the number of times they pressed a lever to turn off prototypes or morphs. a, Normalized learning trajectories in the operant test from Fig. 1h , i (N=7 mice per group). Each line denotes an individual virgin’s learning curve. b, The total number of levers presses in a session (which turns off continuously playing prototypes or morphs) did not increase by session 8, regardless of the stimulus group (N=7 mice per group; 175 ms, p=0.44; 75 ms, p=0.19; 575 ms, p=0.14; paired two-tailed t-test). Extended Data Figure 6. Experience-dependent neuronal and synaptic temporal tuning in auditory cortex. a, Interneuron temporal tuning curves from experienced virgins (‘EVs’; N=5 mice). Each line=individual animal. b, Same as (a) in naive virgins (‘NVs’; N=6). c, Tuning width across behaviorally-salient ISIs 75:375 ms (average normalized ΔF/F). Excitatory neuronal tuning curves were significantly broader in EVs (N=9 mice) than in NVs (N=12; p=0.001), and interneuron tuning was broader than excitatory tuning in naive cortex (Inh: N=6; p=0.04). Interneuron tuning width did not differ between experienced (N=5) and naive virgins (p>0.99; one-way ANOVA, Bonferroni correction). Median±interquartile. d, Slope of population tuning curves at the behavioral transition (375:975 ms). Slopes in EVs were significantly negative. EV exc : N=7 mice, p=0.02; EV inh : N=5, p=0.007; NV exc : N=11, p=0.84; NV inh : N=6, p=0.29 (one-sample t-test to 0.0). Mean±s.e.m. e, Excitatory synaptic tuning in experien
[... 5 more lines not kept]
```

**Agent**

The text is the NIH author manuscript (PMC7677212), with Methods and Extended Data legends. Next: the dataset's description and the linked code (figshare collection).

**Agent calls Bash**

```bash
grep -rl "000249" --include=*.yaml --include=*.md --include=*.json . 2>/dev/null | head; ls; ls tools
```

```
./targets/dandisets.json
./papers/manifest.yaml
LICENSE
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
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
items=d if isinstance(d,list) else d.get('dandisets',d)
for x in (items if isinstance(items,list) else items.values()):
  if '000249' in json.dumps(x): print(json.dumps(x,indent=1)[:3000])
"; grep -n -B2 -A10 "000249" papers/manifest.yaml
```

```
[
 {
  "dandiset": "000003",
  "name": "Physiological Properties and Behavioral Correlates of Hippocampal Granule Cells and Mossy Cells",
  "published_version": "0.260218.2052",
  "asset_count": 101,
  "size_gb": 2559.25,
  "data_standards": [
   "Neurodata Without Borders (NWB)"
  ],
  "species": [
   "House mouse"
  ],
  "approaches": [
   "electrophysiological approach",
   "behavioral approach"
  ],
  "papers": [
   {
    "doi": "10.1016/j.neuron.2016.12.011",
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
import json;d=json.load(open('targets/dandisets.json'))
for x in d:
  if x['dandiset']=='000249': print(json.dumps(x,indent=1))
"; curl -s -m 20 https://api.dandiarchive.org/api/dandisets/000249/ | head -c 1500
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s -m 20 https://api.dandiarchive.org/api/dandisets/000249/versions/0.230423.1416/ | python3 -c "
import json,sys;d=json.load(sys.stdin)
for k in ['name','description','keywords','assetsSummary','relatedResource','protocol','wasGeneratedBy']: print(k, json.dumps(d.get(k),indent=1)[:1500])"
```

Result: the fetched text is not kept.

**Agent**

The dandiset holds the two-photon imaging (raw TwoPhotonSeries, 54 subjects). Now the code at the figshare DOI the paper links.

**Agent calls Bash**

```bash
curl -sL -m 30 -o /dev/null -w "%{url_effective} %{http_code}\n" https://doi.org/10.35092/yhjc.c.5037737; curl -s -m 30 "https://api.figshare.com/v2/collections/5037737" | head -c 2000; echo; curl -s -m 30 "https://api.figshare.com/v2/collections/5037737/articles?page_size=100" | head -c 3000
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
for c in 5043830; do curl -s -m 30 "https://api.figshare.com/v2/collections/$c" | python3 -c "import json,sys;d=json.load(sys.stdin);print(d.get('title'),d.get('doi'),d.get('version'),d.get('description','')[:800])"; curl -s -m 30 "https://api.figshare.com/v2/collections/$c/articles?page_size=100" | python3 -c "
import json,sys
for a in json.load(sys.stdin): print(a['id'],a['title'],a.get('doi'))"; done; curl -s -m 30 "https://api.figshare.com/v2/articles/search" -H 'Content-Type: application/json' -d '{"search_for":"maternal behavior auditory cortex Schiavo"}' | head -c 1500
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL -m 30 -o /dev/null -w "%{http_code}\n" https://nih.figshare.com/collections/_/5037737; curl -s -m 30 https://api.datacite.org/dois/10.35092/yhjc.c.5037737 | head -c 800; echo; for a in 13054076 13056584; do curl -s -m 30 https://api.figshare.com/v2/articles/$a | python3 -c "
import json,sys;d=json.load(sys.stdin);print(d['title'],d.get('description','')[:600]);[print(' ',f['name'],f['size'],f['download_url']) for f in d['files']]"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
for a in $(curl -s -m 30 "https://api.figshare.com/v2/collections/5043830/articles?page_size=100" | python3 -c "import json,sys;[print(a['id']) for a in json.load(sys.stdin)]"); do curl -s -m 30 https://api.figshare.com/v2/articles/$a | python3 -c "
import json,sys;d=json.load(sys.stdin)
code=[f['name'] for f in d['files'] if f['name'].lower().endswith(('.m','.py','.ipynb','.r','.rcx','.ijm'))]
if code: print(d['id'],d['title'],code)"; done; curl -s -m 30 https://api.figshare.com/v2/articles/12609695 | python3 -c "import json,sys;print(json.load(sys.stdin)['description'][:800])"
```

Result: the fetched text is not kept.

**Agent**

No analysis code was deposited. I'll read the operant task code, since it defines how lever-press duration was logged.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/code && cd $TMPDIR/code && for f in 24979211 24979214 24979217 24979220 24979223; do curl -sL -m 30 -OJ https://ndownloader.figshare.com/files/$f; done; ls; cat KAMB_OperantTask_prototypes.m; diff KAMB_OperantTask_prototypes.m KAMB_OperantTask_slows.m
```

Result: the fetched text is not kept.

**Agent**

The operant code only runs the task: 30-minute sessions, with a touch time written at each polling sample while the sensor is touched. It holds no analysis. Now the schema and the checker.

**Agent calls Bash**

```bash
ls schemas; sed -n 1,80p tools/claims_check.py; grep -n "kind\|data\b\|enum" schemas/*claims* | head -60
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
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
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,200p schemas/claims.schema.json
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,400p schemas/claims.schema.json
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
[... 127 more lines not kept]
```

**Agent**

I've read the full text and checked the code: the paper's code DOI does not resolve, and the only code deposited is the operant task runner. Writing the claims file now.

**Agent calls Bash**

```bash
sed -n 250,400p claims/001453/10.1016-j.cub.2025.04.027.yaml | grep -n "elsewhere\|where:\|inferred" | head; grep -rn "where:" claims/*/*.yaml | head -5
```

```
claims/000006/10.1038-s41586-018-0642-9.yaml:134:  where: scRNA-seq data of Tasic et al. 2018, doi:10.1038/s41586-018-0654-5 (Allen Institute); Figshare
claims/000006/10.1038-s41586-018-0642-9.yaml:152:  where: Figshare doi:10.25378/janelia.7007846 version 1, Axons.zip (MouseLight reconstructions)
claims/000006/10.1038-s41586-018-0642-9.yaml:172:  where: Figshare doi:10.25378/janelia.7007846 version 1, Axons.zip (MouseLight reconstructions)
claims/000006/10.1038-s41586-018-0642-9.yaml:187:  where: Figshare doi:10.25378/janelia.7007846 version 1, Axons.zip and Anatomy.zip
claims/000006/10.1038-s41586-018-0642-9.yaml:213:  where: Figshare doi:10.25378/janelia.7007846 version 1, Anatomy.zip
```

**Agent calls Write**

```json
{
 "file_path": "claims/000249/10.1038-s41586-020-2807-6.yaml",
 "content": "# Claims for Schiavo, Valtcheva, Bair-Marshall, Song, Martin & Froemke (2020), Nature 587, 426-431,\n# on dandiset 000249.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23, protocol\n# pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the NIH author manuscript in PubMed Central (PMC7677212, NIHMS1609780), as served by\n# ncbi_pmc: main text, Methods, the ten Extended Data figure legends and the four main figure legends.\n# It is the accepted manuscript, not the version of record, and its title reads \"Innate and plastic\n# mechanisms in auditory cortex for maternal behavior\". The paper has no separate supplement beyond\n# Extended Data; the source data Excel sheet it mentions was not available and no claim relies on it.\n# No PDF was read.\n#\n# Code. The paper's data and code statements point to figshare doi:10.35092/yhjc.c.5037737, which\n# did not resolve on 2026-10-23 (doi.org, DataCite and the figshare API all return not found). The\n# dandiset links figshare collection doi:10.6084/m9.figshare.c.5043830.v6, same title as the\n# manuscript. Its only code item is \"Behavior code\" (doi:10.6084/m9.figshare.13054076.v1), read in\n# full; it holds MATLAB scripts (KAMB_OperantTask_prototypes.m, _fast.m, _slows.m, a circuit loader\n# and a date helper) and RPvdsEx circuits that run the operant task. They run 30 min sessions (1800 s)\n# and append to a csv the time of every polling sample at which the touch sensor reads a touch; they\n# hold no analysis. No analysis code for imaging, whole-cell or behaviour was found, so every method\n# detail below comes from the Methods and legends, and what they leave open is named in the criteria.\n# The same collection holds per-mouse imaging items (titled e.g. EV27_Experienced_Exc,\n# NV33_Naive_Inh, EV123_Experienced-Right ACtx_Exc, OXTHALO-19_Naive_Synapsin, M001_Dam_Exc), the\n# in vivo and in vitro whole-cell recordings, and the operant touch-time files; only titles and\n# descriptions were read, not data.\n#\n# The dandiset (title as the paper; 777 NWB files, 54 subjects, two-photon microscopy, variables\n# TwoPhotonSeries, ImagingPlane, OpticalChannel) holds the two-photon calcium imaging. The behavioural\n# assays, whole-cell recordings, in vitro slices and vocalization recordings are not described by it.\n#\n# Data the paper used, as it reports them.\n# - Subjects. C57BL/6 virgin females 6-48 weeks old; naive virgins (NV, no retrieval at baseline);\n#   experienced virgins (EV, cohoused with a dam and litter at least 72 h); lactating dams; Gad2-IRES-Cre\n#   mice for interneurons; Oxt-IRES-Cre and Oxt-IRES-Cre x Ai39 mice for oxytocin neuron inhibition.\n# - Stimuli. 6-9 prototypical pup calls (4-5 syllables, ISI 175 +/- 25 ms, about 1 s long) and for\n#   each seven temporal morphs with ISI bin centres 75, 125, 225, 275, 375, 575 and 975 ms; pure tones\n#   (4-64 kHz, 500 ms, 70 dB SPL, 0.2 Hz) and tone-pip sequences at the best frequency with ISIs 75,\n#   175, 375 and 575 ms. Calls played in pseudorandom order at 0.1 Hz; morphs played only for the\n#   prototypes that evoked responses.\n# - Imaging. Awake head-fixed mice, layer 2/3 of left auditory cortex (right in Extended Data Fig.\n#   4a-c), GCaMP6f in excitatory neurons (AAV9.CamKII) or interneurons (mDLX, or Flex in Gad2-Cre),\n#   pan-neuronal (Syn.Flex) in the oxytocin-inhibition mice; 256x256 pixels at 4 Hz (0.26 s per\n#   frame), one example at 16 Hz. Groups and counts: EV excitatory N=9 mice, NV excitatory N=12,\n#   EV interneurons N=5, NV interneurons N=6, EV right cortex N=4, one dam; chronic imaging through\n#   cohousing (N=13 virgins, retrieval tested every 12 h, imaged at least every 24 h, always at first\n#   retrieval and 24 h after); non-cohoused controls (3 sessions); CH+575 virgins (N=6); CH+575\n#   opto-OT virgins (N=4).\n# - Behaviour. Cold pup retrieval assay with dubbed calls (trials, % retrieved, latency), y-maze,\n#   operant lever task (N=7 per group, 8 sessions). Whole-cell in vivo (EPSC, IPSC per cell and ISI)\n#   and in vitro (short-term depression; oxytocin spike probability).\n#\n# Imaging method from the Methods, used by every imaging claim below (\"the imaging method\").\n# ROIs drawn by hand on the average image after TurboReg x-y registration (Fiji). A cell responds to a\n# prototype when the integral of fluorescence in the stimulus epoch (from 250 ms after call onset,\n# 1 s long) is significantly above baseline (F0, the 1 s before onset) by a paired one-tailed\n# Student's t-test across trials at p < 0.05 and is at least 1.5 standard deviations above baseline.\n# dF/F (%) is the mean of (Ft - F0)/F0 x 100 over the epoch; for morphs the epoch gains or loses a\n# frame for each 500 ms added to or taken from the call, and the window is shifted to the signal's\n# peak cell by cell. Each responsive cell and prototype gives one tuning curve. Normalized dF/F for a\n# morph is 1 - |(P - M)/(P + M)|, P and M the prototype- and morph-evoked dF/F. Tuning width is the\n# mean normalized dF/F over the behaviourally salient ISIs 75:375 ms. Slope at the transition is the\n# slope of the line between 375 and 975 ms.\n# Open in the imaging method, with the readings the text allows.\n# (i) ROIs. The paper's ROIs were drawn by hand. If the dataset holds them they are used; if not,\n#     any segmentation is not the paper's and is recorded as a deviation.\n# (ii) The 1.5 SD rule. (a) The trial-averaged epoch mean exceeds the baseline mean by 1.5 SD of the\n#     baseline frames pooled over trials; (b) by 1.5 SD of the trial-wise baseline means.\n# (iii) The peak shift. (a) One shift per cell, from the peak of the mean prototype response, applied\n#     to all its stimuli; (b) a shift per stimulus from that stimulus's own mean response peak. The\n#     maximal shift is not given; a shift that keeps the epoch inside the inter-call interval is used.\n# (iv) Tuning width. Whether the prototype (normalized value 1 by definition) is in the average is not\n#     said; including it is an affine change of every width and changes no test, so it is left out,\n#     a standard choice.\n# (v) Slope. (a) The two-point slope (y975 - y375)/600 per ms; (b) the least-squares slope over the\n#     points 375, 575 and 975 ms.\n# (vi) Population tuning of a mouse. (a) The mean over that mouse's single-cell normalized curves;\n#     (b) normalized from the mouse's mean raw dF/F curve (Extended Data Fig. 3g,h shows raw population\n#     tuning \"summarized in Fig. 1f\").\n# (vii) Normalized dF/F when P + M is near zero or of mixed sign is not addressed; values are used as\n#     computed, and the count of curves with P + M <= 0 is reported.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000249\"\npaper: doi:10.1038/s41586-020-2807-6\nclaims:\n- id: subject-group-link\n  kind: link\n  statement: The dandiset's subjects can be assigned to the paper's imaging groups (experienced or\n    naive virgin, dam, right cortex, cohousing, CH+575, opto-OT; excitatory, inhibitory or\n    pan-neuronal indicator), with stimulus identity (prototype or morph ISI) for each presentation.\n  source: Methods, Data availability statement; Methods, In vivo two-photon calcium imaging\n  quote: \"The data that support the findings of this study are further available at figshare\"\n  data: with_labels\n  criterion: Reproduced when every subject carries a group and indicator, from the dataset's own\n    metadata or from the title of the figshare item (collection doi:10.6084/m9.figshare.c.5043830.v6)\n    with the same mouse ID, and every imaging presentation can be assigned its call and ISI bin.\n    The counts per group are compared with the paper's (EV excitatory N=9, NV excitatory N=12, EV\n    interneurons N=5, NV interneurons N=6, EV right cortex N=4, dam N=1, CH+575 N=6, CH+575 opto-OT\n    N=4, chronic cohousing N=13). Partially reproduced when groups can be assigned but stimulus\n    identity cannot, or counts differ for some groups; not reproduced when groups cannot be assigned.\n\n- id: fig1a-isi-distribution\n  statement: Pup distress call ISIs (5,355 intervals from 37 recordings of pups at postnatal days\n    1-8) follow a lognormal distribution; calls with ISIs around the median (175 +/- 25 ms) serve as\n    prototypes, and ISIs of 575 ms or more essentially never occur.\n  source: Figure 1a; Methods, Stimulus library and vocalization analysis\n  quote: \"5,355 inter-syllable intervals were measured from 37 audio recordings ... and a lognormal frequency distribution was generated\"\n  expected:\n  - quantity: number of ISIs measured\n    value: 5355\n    tolerance: 0\n  - quantity: number of audio recordings\n    value: 37\n    tolerance: 0\n  criterion: From the vocalization recordings, the ISIs measured and binned at +/-25 ms. Reproduced\n    when the counts match, a lognormal fits (the median lies in the 150-200 ms bin), and fewer than\n    1% of ISIs are 550 ms or longer. The 1% bound is not in the paper; it reads \"essentially never\".\n\n- id: fig1c-warm-vs-cold\n  statement: Experienced females (dams and experienced virgins pooled) retrieve cold, silent pups on\n    fewer trials than warm, vocalizing pups (32.0% against 80.0%).\n  source: Figure 1c; main text, paragraph citing Fig. 1c\n  quote: \"Experienced females retrieved cold, silent pups on fewer trials than warm, vocalizing pups (retrieval (cold) : 32.0% of trials, retrieval (warm) : 80.0%\"\n  statistics:\n  - about: warm against cold, single syllable and 575 ms\n    test: two-tailed Fisher's test, FDR correction\n    p: 0.0003\n    corrected: FDR (Benjamini-Hochberg)\n    n: warm 55 trials, cold 25, single 20, 575 ms 22\n  expected:\n  - quantity: retrieval, cold pups\n    value: 32.0\n    tolerance: 3.2\n    unit: \"% of trials\"\n  - quantity: retrieval, warm pups\n    value: 80.0\n    tolerance: 8.0\n    unit: \"% of trials\"\n  criterion: Reproduced when both rates are within tolerance and warm against cold is significant by\n    two-tailed Fisher's exact test with Benjamini-Hochberg correction at p < 0.05. The family of\n    comparisons is not stated; the legend lists comparisons against warm, so the family is every\n    condition (cold, prototypes, the seven morphs, single syllables) against warm; uncorrected\n    p-values are shown as a variant.\n\n- id: fig1c-salient-isis-retrieved\n  statement: Cold pups dubbed over with prototypes (76.7%) or with morphs of ISIs 75 to 375 ms\n    (73.7-81.0%) are retrieved at rates similar to warm pups.\n  source: Figure 1c; main text, paragraph citing Fig. 1c\n  quote: \"Cold pups dubbed over with prototypes (76.7%), as well as morphs with ISIs between 75:375 ms (73.7–81.0%), were retrieved at similar rates to warm pups\"\n  expected:\n  - quantity: retrieval, prototypes\n    value: 76.7\n    tolerance: 7.7\n    unit: \"% of trials\"\n  - quantity: retrieval range over morphs 75 to 375 ms, low bound\n    value: 73.7\n    tolerance: 7.4\n    unit: \"% of trials\"\n  - quantity: retrieval range over morphs 75 to 375 ms, high bound\n    value: 81.0\n    tolerance: 8.1\n    unit: \"% of trials\"\n  criterion: A claim of absence. Each of prototypes and morphs 75, 125, 225, 275, 375 ms against warm\n    by two-tailed Fisher's exact test with Benjamini-Hochberg correction over the family named in\n    fig1c-warm-vs-cold. Reproduced when none differs at p < 0.05 and the rates lie within the range\n    widened by 10% of each bound; the differences from warm are reported.\n  depends_on:\n  - fig1c-warm-vs-cold\n\n- id: fig1c-slow-and-single-not-retrieved\n  statement: ISIs slower than 575 ms (27.3%) and single syllables (15.0%) do not effectively elicit\n    retrieval, being retrieved less than warm pups.\n  source: Figure 1c; main text, paragraph citing Fig. 1c\n  quote: \"In contrast, ISIs slower than 575 ms (27.3%) and single syllables (15.0%) did not effectively elicit retrieval\"\n  statistics:\n  - about: warm against cold, single syllable and 575 ms\n    test: two-tailed Fisher's test, FDR correction\n    p: 0.0003\n    corrected: FDR (Benjamini-Hochberg)\n    n: warm 55 trials, single 20, 575 ms 22\n  expected:\n  - quantity: retrieval, 575 ms morphs\n    value: 27.3\n    tolerance: 2.7\n    unit: \"% of trials\"\n  - quantity: retrieval, single syllables\n    value: 15.0\n    tolerance: 1.5\n    unit: \"% of trials\"\n  criterion: Reproduced when both rates are within tolerance and each is below warm by two-tailed\n    Fisher's exact test with Benjamini-Hochberg correction (family as in fig1c-warm-vs-cold) at\n    p < 0.05. The 975 ms morph is reported but not required, since the text names 575 ms.\n  depends_on:\n  - fig1c-warm-vs-cold\n\n- id: ed2a-dams-evs-similar\n  statement: Dams and experienced virgins do not differ in retrieval of warm pups, prototype-dubbed\n    pups or cold pups.\n  source: Extended Data Fig. 2a\n  quote: \"Dams and EVs did not differ in their retrieval behavior\"\n  statistics:\n  - about: warm, dams 85.2% (27 trials) against EVs 77.0% (26)\n    test: two-tailed Fisher's test\n    p: 0.50\n  - about: prototypes, dams 91.7% (12) against EVs 66.7% (18)\n    test: two-tailed Fisher's test\n    p: 0.19\n  - about: cold, dams 25.0% (12) against EVs 38.5% (13)\n    test: two-tailed Fisher's test\n    p: 0.67\n  criterion: A claim of absence. Two-tailed Fisher's exact test, dams against EVs, for each of warm,\n    prototype and cold. Reproduced when none has p < 0.05; the rates are reported.\n\n- id: ed2b-latency-slow-longer\n  statement: On successful trials, latencies to retrieve cold pups and pups dubbed with slow stimuli\n    (single syllables and 575 ms) are longer than for warm pups and for pups dubbed with 75 to 375 ms\n    ISIs.\n  source: Extended Data Fig. 2b\n  quote: \"Latencies to retrieve cold pups and cold pups dubbed over with slow morphs (single syllables (‘SS’) and 575 ms ISIs) were longer than for warm pups (p=0.02) or cold pups dubbed over with morphs containing ISIs between 75:375 ms (p=0.001)\"\n  statistics:\n  - about: slow and cold against warm\n    test: Kruskal-Wallis H-test with Dunn's correction\n    p: 0.02\n  - about: slow and cold against 75:375 ms morphs\n    test: Kruskal-Wallis H-test with Dunn's correction\n    p: 0.001\n  criterion: Latencies of successful trials in three bins (warm; morphs 75 to 375 ms; cold, single\n    syllable and 575 ms). Whether prototypes are in the 75 to 375 ms bin is not said; the readings\n    are with and without prototypes. Reproduced when, under one reading, the Kruskal-Wallis test\n    with Dunn's post hoc shows the slow bin longer than both others at p < 0.05.\n\n- id: ed2d-ymaze-approach\n  statement: In a y-maze, experienced females show no preference between a prototype and a morph\n    with ISIs 25 to 350 ms, but approach prototypes more than morphs slower than 350 ms (425 ms 25.0%,\n    575+ ms 15.8% of trials approaching the morph).\n  source: Extended Data Fig. 2d; main text, paragraph citing Extended Data Fig. 2c,d\n  quote: \"Mice showed a significant preference to approach prototypes when ISIs were slower than 350 ms\"\n  statistics:\n  - about: 62.5 ms bin, 44.2%, 52 trials\n    test: two-tailed binomial test against 0.50\n    p: 0.49\n  - about: 275 ms bin, 55.6%, 45 trials\n    test: two-tailed binomial test against 0.50\n    p: 0.46\n  - about: 425 ms bin, 25.0%, 20 trials\n    test: two-tailed binomial test against 0.50\n    p: 0.04\n  - about: 575+ ms bin, 15.8%, 19 trials\n    test: two-tailed binomial test against 0.50\n    p: 0.005\n  expected:\n  - quantity: morph approach, 425 ms bin\n    value: 25.0\n    tolerance: 2.5\n    unit: \"% of trials\"\n  - quantity: morph approach, 575+ ms bin\n    value: 15.8\n    tolerance: 1.6\n    unit: \"% of trials\"\n  criterion: First room entry per trial, bins of +/-75 ms except 575+. Reproduced when the 425 and\n    575+ bins differ from 0.5 by two-tailed binomial test at p < 0.05 with values in tolerance, and\n    the 62.5 and 275 ms bins do not.\n\n- id: ed3e-prototype-responsive-fraction\n  statement: About 16% of excitatory neurons in left auditory cortex respond to prototypes,\n    regardless of maternal experience.\n  source: Extended Data Fig. 3e; main text, paragraph citing it\n  quote: \"We observed robust responses to prototypes in ~16% of excitatory neurons regardless of maternal experience\"\n  statistics:\n  - test: two-tailed unpaired t-test\n    p: 0.74\n    n: 9 experienced and 12 naive virgins\n  expected:\n    quantity: prototype-responsive excitatory neurons\n    value: 16\n    tolerance: 1.6\n    unit: \"% of neurons\"\n  criterion: Per mouse, the responsive ROIs (the imaging method, responsive to any of the 6-9\n    prototypes) over all ROIs. Whether ~16% is the mean over mice or over neurons pooled is not\n    said; both readings are computed. Reproduced when, under one reading, the value is within\n    tolerance and the per-mouse percentages of EV and NV do not differ by two-tailed unpaired t-test\n    at p < 0.05.\n\n- id: fig1f-ev-broader-than-nv\n  statement: Excitatory neuronal tuning to temporal morphs is broader in experienced than in naive\n    virgins across the ISIs that elicit retrieval; naive cortex responds less to morphs than to\n    prototypes.\n  source: Figure 1f; main text, paragraph citing Fig. 1e,f\n  quote: \"Compared to naive virgins, temporal tuning was broader in experienced virgins across ISIs that reliably elicited pup retrieval\"\n  statistics:\n  - about: EV against NV at 375 ms\n    test: one-way ANOVA, Bonferroni correction\n    p: 0.050\n    corrected: Bonferroni\n    n: 9 experienced and 12 naive virgins\n  criterion: Per-mouse population tuning curves of normalized dF/F (the imaging method, readings (vi)\n    a and b). The ANOVA design is not given; the readings are (a) a one-way ANOVA over all group and\n    ISI cells with Bonferroni-corrected EV against NV comparisons at each of the seven morph ISIs;\n    (b) EV against NV t-tests per morph ISI, Bonferroni over the seven. Reproduced when the EV mean\n    exceeds the NV mean at each of 75, 125, 225, 275 and 375 ms and the 375 ms comparison has\n    p <= 0.05 under one reading; partially reproduced when EV exceeds NV at all five but no reading\n    gives p <= 0.05 at 375 ms.\n\n- id: ed6c-tuning-width-groups\n  statement: Tuning width over 75 to 375 ms is broader for excitatory neurons in experienced than in\n    naive virgins; in naive cortex interneurons are more broadly tuned than excitatory neurons; and\n    interneuron tuning width does not differ between experienced and naive virgins.\n  source: Extended Data Fig. 6c\n  quote: \"Excitatory neuronal tuning curves were significantly broader in EVs (N=9 mice) than in NVs (N=12; p=0.001), and interneuron tuning was broader than excitatory tuning in naive cortex (Inh: N=6; p=0.04). Interneuron tuning width did not differ between experienced (N=5) and naive virgins (p>0.99; one-way ANOVA, Bonferroni correction)\"\n  statistics:\n  - about: EV against NV excitatory\n    test: one-way ANOVA, Bonferroni correction\n    p: 0.001\n    corrected: Bonferroni\n    n: 9 EV and 12 NV mice\n  - about: NV interneurons against NV excitatory\n    test: one-way ANOVA, Bonferroni correction\n    p: 0.04\n    corrected: Bonferroni\n    n: 6 and 12 mice\n  - about: EV against NV interneurons\n    test: one-way ANOVA, Bonferroni correction\n    p: 0.99\n    p_relation: \">\"\n    corrected: Bonferroni\n    n: 5 and 6 mice\n  criterion: Per-mouse tuning widths (the imaging method, readings (vi) a and b) in four groups (EV\n    and NV, excitatory and interneuron); one-way ANOVA with Bonferroni post hoc comparisons. Which\n    pairs form the Bonferroni family is not stated; the readings are (a) the three pairs reported,\n    (b) all six pairs. Reproduced when, under one reading, EV excitatory exceeds NV excitatory and NV\n    interneurons exceed NV excitatory, each at p < 0.05, and EV against NV interneurons is not\n    significant (the absence part is judged on the paper's test as written).\n\n- id: ed3k-tones-no-experience-effect\n  statement: The narrow tuning in naive cortex does not extend to temporally modulated pure tones;\n    tuning width to tone sequences does not differ between experienced and naive virgins.\n  source: Extended Data Fig. 3k; main text, paragraph citing Extended Data Fig. 3i-m\n  quote: \"the narrow tuning in naive cortex did not extend to temporally-modulated pure tones\"\n  statistics:\n  - test: unpaired two-tailed t-test\n    p: 0.97\n    n: experienced 3 mice, 94 neurons; naive 4 mice, 45 neurons\n  criterion: A claim of absence. Cells responsive to the best frequency and to the 175 ms (5 Hz)\n    sequence by paired one-tailed t-test at p < 0.05; normalized dF/F of the 75, 375 and 575 ms\n    sequences to the 175 ms one; width as the mean \"across all stimuli\" (the legend), the readings\n    being with or without the 175 ms value (an affine change, so one is used). Unpaired two-tailed\n    t-test over neurons. Reproduced when p >= 0.05; the difference is reported.\n\n- id: ed3m-tones-broader-than-calls-naive\n  statement: In naive auditory cortex, normalized responses to temporally modulated tones are higher\n    than to pup call morphs at 75, 375 and 575 ms.\n  source: Extended Data Fig. 3m\n  quote: \"We observed higher normalized ΔF/Fs to temporally-modulated tones (N=5 mice) than to pup call morphs (n=11–12) in naive auditory cortex\"\n  statistics:\n  - about: 75 ms\n    test: unpaired two-tailed Mann-Whitney test\n    p: 0.009\n  - about: 375 ms\n    test: unpaired two-tailed Mann-Whitney test\n    p: 0.04\n  - about: 575 ms\n    test: unpaired two-tailed Mann-Whitney test\n    p: 0.004\n  criterion: The units of the samples are unclear (N=5 mice for tones, n=11-12 for calls); the\n    readings are (a) per-mouse medians for both, (b) per-mouse tone values against the 12 naive\n    excitatory mice of Fig. 1f. Reproduced when, under one reading, tones exceed calls at all three\n    ISIs by unpaired two-tailed Mann-Whitney test at p < 0.05.\n\n- id: ed4c-left-broader-than-right\n  statement: Broad temporal tuning in experienced virgins is left-lateralized; tuning width (75 to\n    375 ms) is larger in left than in right auditory cortex.\n  source: Extended Data Fig. 4a-c\n  quote: \"broad temporal tuning was left-lateralized in experienced females\"\n  statistics:\n  - test: unpaired two-tailed Mann-Whitney test\n    p: 0.003\n    n: 9 left and 4 right experienced virgins\n  criterion: Per-mouse tuning widths (the imaging method) of EV excitatory neurons, left (the nine of\n    Fig. 1f) against right (N=4). The p of 0.003 is below the smallest exact two-sided Mann-Whitney\n    p for 9 against 4 mice (2/715, about 0.0028, only at complete separation), so the test may have\n    been run over curves; the readings are (a) mice, (b) single-cell tuning curves. Reproduced when,\n    under one reading, left exceeds right at p < 0.05.\n\n- id: ed4d-response-tracks-isi-probability\n  statement: In experienced virgins, call-evoked dF/F across ISI bins is correlated with the\n    probability of each ISI in natural pup calls.\n  source: Extended Data Fig. 4d\n  quote: \"In EVs (N=9 mice), evoked ΔF/Fs were correlated with ISI probability from the distribution in Fig. 1a (Pearson’s r=0.86, p=0.007; two-tailed)\"\n  statistics:\n  - test: two-tailed Pearson correlation\n    statistic: r = 0.86\n    p: 0.007\n    n: 9 experienced virgins; 8 ISI bins\n  expected:\n    quantity: Pearson r, dF/F against ISI probability\n    value: 0.86\n    tolerance: 0.086\n  data: with_inputs\n  criterion: The mean dF/F per ISI bin over the nine EV mice (eight points, prototype and seven\n    morphs) against the probability of that bin in the Fig. 1a distribution. The ISI distribution is\n    not in the dataset; it comes from fig1a-isi-distribution or from the source data. Whether raw or\n    normalized dF/F is used is not said; both are computed. Reproduced when, under one reading, r is\n    within tolerance and p < 0.05.\n  depends_on:\n  - fig1a-isi-distribution\n\n- id: ed4e-dam-broad-tuning\n  statement: Qualitatively, the left auditory cortex of a lactating dam shows broad temporal tuning.\n  source: Extended Data Fig. 4e\n  quote: \"Qualitatively, we observed broad temporal tuning in the left auditory cortex of a lactating dam (N=1 dam, n=10 single-cell tuning curves)\"\n  criterion: The dam's mean normalized curve (10 single-cell curves). Reproduced when its tuning\n    width lies within the range of the nine EV mice's widths and above the NV median.\n\n- id: ed4g-broadening-with-reliable-retrieval\n  statement: In virgins retrieving on 10-30% of trials, temporal tuning was sharper before the\n    onset of reliable retrieval; more neurons are broadly tuned once they retrieve on 100% of trials.\n  source: Extended Data Fig. 4f,g\n  quote: \"A larger proportion of neurons were more broadly tuned (higher normalized ΔF/Fs) when EVs retrieved on 100% of trials (p<0.0001; two-tailed unpaired Kolmogorov-Smirnov test)\"\n  statistics:\n  - test: two-tailed unpaired Kolmogorov-Smirnov test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 2 mice, 78 neurons before and 52 after\n  criterion: Single-cell tuning widths of the two virgins before (n=78) and after (n=52) reliable\n    retrieval. Reproduced when the after distribution lies to the right (higher median) and the\n    two-sample KS test has p < 0.0001; partially reproduced when p < 0.05.\n\n- id: fig1g-ipsc-depress-faster\n  statement: In pup-naive auditory cortical slices, IPSCs depress faster than EPSCs at the\n    prototypical stimulation rate (175 ms), while EPSCs and IPSCs depress similarly at 75 or 575 ms.\n  source: Figure 1g; main text, paragraph citing Fig. 1g\n  quote: \"whole-cell recordings in pup-naive auditory cortical slices revealed that IPSCs adapted out faster than EPSCs at prototypical repetition rates, while PSCs were similarly depressed at faster or slower stimulation rates\"\n  statistics:\n  - test: one-way ANOVA, Bonferroni correction\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 75 ms 10 cells, 175 ms 14, 575 ms 13\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.12611522.v1 (ACtx slice recordings - Repeated stimulation),\n    in collection doi:10.6084/m9.figshare.c.5043830.v6; the paper's own figshare DOI did not resolve\n  criterion: Peak PSCs normalized to the first (Sn/S1) per cell. The p-value is not printed (the\n    legend marks significance with asterisks), and the ANOVA factors are not given; the readings are\n    (a) IPSC against EPSC Sn/S1 at each pulse, Bonferroni over pulses, per rate; (b) the mean Sn/S1\n    over pulses 2 to 5, IPSC against EPSC, per rate. Reproduced when, under one reading, IPSCs are\n    lower than EPSCs at p < 0.05 at 175 ms and not at 75 or 575 ms.\n\n- id: fig1i-operant-prototypes\n  statement: Of naive virgins able to silence playback with a lever press, only those hearing\n    prototypes significantly increased their press duration by session 8.\n  source: Figure 1h,i; main text, paragraph citing Fig. 1h,i\n  quote: \"Only virgins listening to prototypes exhibited a significant increase in press duration by session 8 (p=0.03)\"\n  statistics:\n  - about: prototypes (175 ms)\n    test: paired two-tailed t-test\n    p: 0.03\n    n: 7 virgins\n  - about: fast morphs (75 ms)\n    test: paired two-tailed t-test\n    p: 0.24\n    n: 7 virgins\n  - about: slow morphs (575 ms)\n    test: paired two-tailed t-test\n    p: 0.13\n    n: 7 virgins\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.13056584.v1 (Behavior files, touch times), in collection\n    doi:10.6084/m9.figshare.c.5043830.v6; the paper's own figshare DOI did not resolve\n  criterion: Touch-time files of 30 min sessions (KAMB_OperantTask_*.m write the time of each\n    polling sample with a touch). A press is a run of consecutive touch samples; the gap that ends a\n    press is not given, and the readings are gaps above (a) the median inter-sample interval times\n    2, (b) 100 ms. The mean press duration per session; files marked b (e.g. v4b) are joined to\n    their session. The comparison is not stated; the readings are (a) session 1 against session 8,\n    (b) the mean of sessions 1-2 against 7-8. Reproduced when, under every reading, prototypes give\n    p < 0.05 by paired two-tailed t-test with an increase and the other groups do not; blocked as\n    methods_underspecified when the readings disagree.\n\n- id: ed5b-press-count-unchanged\n  statement: The number of lever presses per session did not increase by session 8 in any of the\n    three groups.\n  source: Extended Data Fig. 5b\n  quote: \"The total number of levers presses in a session (which turns off continuously playing prototypes or morphs) did not increase by session 8, regardless of the stimulus group\"\n  statistics:\n  - about: 175 ms\n    test: paired two-tailed t-test\n    p: 0.44\n  - about: 75 ms\n    test: paired two-tailed t-test\n    p: 0.19\n  - about: 575 ms\n    test: paired two-tailed t-test\n    p: 0.14\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.13056584.v1 (Behavior files, touch times)\n  criterion: A claim of absence. Presses counted as in fig1i-operant-prototypes; paired two-tailed\n    t-test of session 8 against session 1 per group (N=7). Reproduced when no group shows an increase\n    at p < 0.05.\n  depends_on:\n  - fig1i-operant-prototypes\n\n- id: fig2d-interneuron-slope-sharper\n  statement: Interneurons are broadly tuned regardless of experience, but their tuning curve slopes\n    at the transition between retrieved (75:375 ms) and ignored (575:975 ms) ISIs are sharper in\n    experienced virgins.\n  source: Figure 2c,d; main text, paragraph citing Fig. 2\n  quote: \"tuning curve slopes at the transition between ISIs eliciting retrieval (75:375 ms, Fig. 1c ) and ignored ISIs (575:975 ms) were significantly sharper in experienced virgins (p=0.03\"\n  statistics:\n  - test: unpaired two-tailed t-test\n    p: 0.03\n    n: 5 experienced and 6 naive virgins\n  criterion: Per-mouse population curves of interneurons (the imaging method, readings (v) and (vi));\n    slope 375 to 975 ms. Reproduced when the EV slope is more negative than the NV slope at p < 0.05\n    by unpaired two-tailed t-test under every reading of (v) and (vi); blocked as\n    methods_underspecified when they disagree.\n\n- id: ed6d-slopes-negative-in-ev\n  statement: Population tuning slopes at the behavioural transition (375:975 ms) are significantly\n    negative in experienced virgins, for excitatory neurons and interneurons, and not in naive\n    virgins.\n  source: Extended Data Fig. 6d; main text, paragraph citing Fig. 2e\n  quote: \"Slopes in EVs were significantly negative\"\n  statistics:\n  - about: EV excitatory\n    test: one-sample t-test to 0.0\n    p: 0.02\n    n: 7 mice\n  - about: EV interneurons\n    test: one-sample t-test to 0.0\n    p: 0.007\n    n: 5 mice\n  - about: NV excitatory\n    test: one-sample t-test to 0.0\n    p: 0.84\n    n: 11 mice\n  - about: NV interneurons\n    test: one-sample t-test to 0.0\n    p: 0.29\n    n: 6 mice\n  criterion: Per-mouse population slopes (readings (v) and (vi)). The mice counts (7 and 11) are\n    fewer than in Fig. 1f (9 and 12); which were left out is not said, so all mice with a 975 ms\n    response are used and the counts reported. Reproduced when both EV groups have slopes below zero\n    at p < 0.05 and neither NV group does, under every reading; blocked as methods_underspecified\n    when they disagree.\n\n- id: fig2e-ev-matched-ei-tuning\n  statement: In experienced virgins, excitatory and inhibitory single-cell tuning are matched across\n    behaviourally salient ISIs and differ at 575 and 975 ms.\n  source: Figure 2e\n  quote: \"Excitatory and inhibitory neuronal tuning were also matched in experienced virgins, responding similarly across behaviorally-salient ISIs and with negative slopes between 375:975 ms\"\n  statistics:\n  - about: excitatory against inhibitory at 575 ms\n    test: one-way ANOVA, Bonferroni correction\n    p: 0.009\n    corrected: Bonferroni\n    n: 366 excitatory and 260 inhibitory single-cell tuning curves\n  - about: excitatory against inhibitory at 975 ms\n    test: one-way ANOVA, Bonferroni correction\n    p: 0.048\n    corrected: Bonferroni\n    n: 366 excitatory and 260 inhibitory single-cell tuning curves\n  criterion: Single-cell normalized curves of EV excitatory and inhibitory neurons; one-way ANOVA over\n    cell type and ISI cells with Bonferroni-corrected comparisons, excitatory against inhibitory at\n    each morph ISI. The direction at 575 and 975 is not stated in the text; it is reported. Reproduced\n    when 575 and 975 differ at p < 0.05 and none of 75 to 375 ms does.\n\n- id: fig2f-nv-mismatched-ei-tuning\n  statement: In naive cortex, interneurons are more broadly tuned than excitatory neurons but lack a\n    sharp boundary at the behavioural transition.\n  source: Figure 2f; main text, paragraph citing Fig. 2f\n  quote: \"while interneurons in naive cortex were more broadly tuned than excitatory neurons, the lack of a sharp boundary suggests interneurons were still relatively untuned to relevant statistics\"\n  statistics:\n  - test: one-way ANOVA, Bonferroni correction\n    p: 0.05\n    p_relation: \"<\"\n    corrected: Bonferroni\n    n: 268 excitatory and 128 inhibitory single-cell tuning curves\n  criterion: As fig2e-ev-matched-ei-tuning on NV curves. Reproduced when interneurons exceed\n    excitatory neurons at p < 0.05 at two or more of 75, 125, 225, 275, 375 ms, and the interneuron\n    curve's 375 to 975 slope (reading (v)) does not differ from zero by one-sample t-test over\n    curves. The legend gives no p for this panel; the asterisks are not readable in the text.\n\n- id: ed6ef-epsc-tuning\n  statement: In experienced females, prototype- and morph-evoked EPSCs are similar and negatively\n    correlated with ISI; in naive cortex morph-evoked EPSCs are weaker than prototype-evoked ones\n    and uncorrelated with ISI.\n  source: Extended Data Fig. 6e,f; main text, paragraph citing Fig. 2g\n  quote: \"In experienced females, prototype- and morph-evoked EPSCs were similar in magnitude and negatively correlated with ISI duration\"\n  statistics:\n  - about: NV 175 against 125 ms\n    test: repeated measures one-way ANOVA, Bonferroni correction\n    p: 0.006\n  - about: NV 175 against 275 ms\n    test: repeated measures one-way ANOVA, Bonferroni correction\n    p: 0.003\n  - about: NV 175 against 575 ms\n    test: repeated measures one-way ANOVA, Bonferroni correction\n    p: 0.02\n  - about: EV EPSC against ISI\n    test: two-tailed Pearson correlation\n    statistic: r = -0.37\n    p: 0.01\n    n: 12 cells\n  - about: NV EPSC against ISI\n    test: two-tailed Pearson correlation\n    statistic: r = -0.13\n    p: 0.35\n    n: 14 cells\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.12611657.v3 (experienced) and\n    doi:10.6084/m9.figshare.12613496.v2 (naive), in collection doi:10.6084/m9.figshare.c.5043830.v6\n  criterion: PSC area over the window from call onset to 250 ms after offset, divided by its length,\n    minus the 1 s baseline, mean of the largest 5-10 trials (the readings 5 and 10 are both run).\n    Correlation over all cell and ISI points (n=12 cells by 4 ISIs, matching the p for r=-0.37).\n    Reproduced when, under one reading, NV prototype exceeds 125, 275 and 575 ms at p < 0.05 by\n    repeated measures ANOVA with Bonferroni, no EV pair differs, the EV correlation is negative at\n    p < 0.05 and the NV one is not significant.\n\n- id: fig2h-epsc-enhanced-ev\n  statement: Prototype-evoked EPSCs are similar between groups, but EPSCs evoked by non-prototypical\n    ISIs are larger in experienced than in naive females.\n  source: Figure 2h; main text, paragraph citing Fig. 2h\n  quote: \"While prototype-evoked EPSCs were similar, responses to non-prototypical ISIs were enhanced in experienced females\"\n  statistics:\n  - about: 125 ms\n    test: unpaired one-tailed t-test\n    p: 0.001\n    n: 12 EV and 14 NV cells\n  - about: 275 ms\n    test: unpaired one-tailed t-test\n    p: 0.03\n  - about: 575 ms\n    test: unpaired one-tailed t-test\n    p: 0.04\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.12611657.v3 and doi:10.6084/m9.figshare.12613496.v2\n  criterion: EPSC magnitudes as in ed6ef-epsc-tuning. Reproduced when EV exceeds NV at 125, 275 and\n    575 ms at p < 0.05 by unpaired one-tailed t-test and the prototype comparison is not significant.\n  depends_on:\n  - ed6ef-epsc-tuning\n\n- id: fig2i-ipsc-weaker-nv\n  statement: IPSCs are broadly tuned in both groups but weaker in naive virgins at every ISI.\n  source: Figure 2i; Extended Data Fig. 6i-k\n  quote: \"IPSCs were broadly tuned in both groups ( Extended Data Figure 6i – k ), albeit weaker in naive virgins\"\n  statistics:\n  - about: 125 ms\n    test: unpaired two-tailed t-test\n    p: 0.047\n    n: 6 cells each\n  - about: 175 ms\n    test: unpaired two-tailed t-test\n    p: 0.009\n  - about: 275 ms\n    test: unpaired two-tailed t-test\n    p: 0.01\n  - about: 575 ms\n    test: unpaired two-tailed t-test\n    p: 0.004\n  - about: EV IPSC against ISI\n    test: two-tailed Pearson correlation\n    statistic: r = 0.33\n    p: 0.11\n    n: 6 cells\n  - about: NV IPSC against ISI\n    test: two-tailed Pearson correlation\n    statistic: r = 0.13\n    p: 0.56\n    n: 6 cells\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.12611657.v3 and doi:10.6084/m9.figshare.12613496.v2\n  criterion: IPSC magnitudes as in ed6ef-epsc-tuning. Reproduced when EV exceeds NV at all four ISIs\n    at p < 0.05 by unpaired two-tailed t-test, and neither correlation with ISI is significant.\n  depends_on:\n  - ed6ef-epsc-tuning\n\n- id: fig2j-ie-ratio-tracks-isi\n  statement: In experienced females the IPSC-EPSC ratio is positively correlated with ISI, so that\n    the balance shifts toward inhibition for slower ISIs; not so in naive females.\n  source: Figure 2j; main text, paragraph citing Fig. 2j\n  quote: \"In experienced females, this ratio was positively correlated with ISI duration (Pearson’s r=0.47, p=0.02\"\n  statistics:\n  - about: experienced\n    test: two-tailed Pearson correlation\n    statistic: r = 0.47\n    p: 0.02\n    n: 6 cells\n  - about: naive\n    test: two-tailed Pearson correlation\n    statistic: r = 0.01\n    p: 0.96\n    n: 6 cells\n  expected:\n    quantity: Pearson r, IPSC-EPSC ratio against ISI, experienced\n    value: 0.47\n    tolerance: 0.047\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.12611657.v3 and doi:10.6084/m9.figshare.12613496.v2\n  criterion: (IPSC - EPSC)/(IPSC + EPSC) per cell and ISI, from cells with both currents recorded,\n    correlated with ISI over all cell and ISI points. Reproduced when the EV r is within tolerance\n    with p < 0.05 and the NV correlation is not significant.\n  depends_on:\n  - ed6ef-epsc-tuning\n\n- id: fig2k-ipsc-exceeds-epsc-575\n  statement: Within cells of experienced cortex, 575 ms-evoked IPSCs are stronger than EPSCs, while\n    the two do not differ at 125, 175 or 275 ms.\n  source: Figure 2k; Extended Data Fig. 6l\n  quote: \"575-evoked IPSCs were significantly stronger than EPSCs (p=0.03\"\n  statistics:\n  - about: 575 ms\n    test: paired two-tailed t-test\n    p: 0.03\n    n: 6 cells\n  - about: 125 ms\n    test: two-tailed paired t-test\n    p: 0.47\n  - about: 175 ms\n    test: two-tailed paired t-test\n    p: 0.26\n  - about: 275 ms\n    test: two-tailed paired t-test\n    p: 0.44\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.12611657.v3\n  criterion: Reproduced when IPSC exceeds EPSC at 575 ms at p < 0.05 by paired two-tailed t-test and\n    the other ISIs are not significant.\n  depends_on:\n  - ed6ef-epsc-tuning\n\n- id: ed6h-dams-evs-epsc-similar\n  statement: Prototype- and morph-evoked EPSCs do not differ between lactating dams and experienced\n    virgins, justifying their pooling.\n  source: Extended Data Fig. 6g,h\n  quote: \"Prototype and morph-evoked EPSCs did not differ between dams (n=4 cells) and EVs (n=8)\"\n  statistics:\n  - about: 125 ms\n    test: unpaired two-tailed t-test\n    p: 0.11\n  - about: 175 ms\n    test: unpaired two-tailed t-test\n    p: 0.80\n  - about: 275 ms\n    test: unpaired two-tailed t-test\n    p: 0.85\n  - about: 575 ms\n    test: unpaired two-tailed t-test\n    p: 0.85\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.12611657.v3\n  criterion: A claim of absence. Unpaired two-tailed t-test, dams (n=4) against EVs (n=8), per ISI.\n    Reproduced when none has p < 0.05.\n  depends_on:\n  - ed6ef-epsc-tuning\n\n- id: ed7bc-tracked-responsiveness\n  statement: During cohousing prototype-responsive interneurons are relatively stable while the set\n    of prototype-responsive excitatory neurons changes; about 18.8% of excitatory and 72.3% of\n    inhibitory neurons responsive at baseline remain responsive in the final session.\n  source: Extended Data Fig. 7a-c; main text, paragraph citing Fig. 3b\n  quote: \"Of the neurons that were prototype-responsive at baseline and successfully tracked, ~18.8% of excitatory neurons and ~72.3% of inhibitory neurons remained responsive in the final imaging session\"\n  statistics:\n  - about: excitatory, baseline against post-onset prototype dF/F\n    test: two-tailed Spearman correlation\n    statistic: r = -0.40\n    p: 0.0001\n    p_relation: \"<\"\n    n: 104 neurons\n  - about: inhibitory\n    test: two-tailed Spearman correlation\n    statistic: r = 0.46\n    p: 0.0001\n    p_relation: \"<\"\n    n: 122 neurons\n  expected:\n  - quantity: excitatory neurons remaining responsive\n    value: 18.8\n    tolerance: 1.9\n    unit: \"%\"\n  - quantity: inhibitory neurons remaining responsive\n    value: 72.3\n    tolerance: 7.2\n    unit: \"%\"\n  - quantity: Spearman r, excitatory\n    value: -0.40\n    tolerance: 0.04\n  - quantity: Spearman r, inhibitory\n    value: 0.46\n    tolerance: 0.046\n  criterion: Chronic imaging virgins. ROIs matched across days by spatial cross-correlation of the\n    100x100-pixel image around each ROI; cells below the 95th percentile of the across-ROI null are\n    dropped. Prototype dF/F at baseline and in the final session (+24 to 96 h), zero for\n    non-responsive cells. Reproduced when the percentages and r values are within tolerance and\n    both correlations have p < 0.0001; partially reproduced when the signs and p < 0.05 hold.\n\n- id: fig3e-exc-broadens-after-onset\n  statement: During cohousing, excitatory single-cell tuning broadens between 75 and 375 ms after\n    retrieval onset, while interneuron tuning does not broaden; excitatory and inhibitory tuning,\n    mismatched at first, become similar 24 hours after first retrieval.\n  source: Figure 3e-g; main text, paragraph citing Fig. 3e\n  quote: \"Excitatory population tuning broadened between 75:375 ms ( Fig. 3e , f ), elaborating on the initial preference for prototypes. Interneurons did not broaden their tuning\"\n  statistics:\n  - about: excitatory widths before against after onset\n    test: unpaired two-tailed Kolmogorov-Smirnov test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 165 naive and 70 (+24 h) excitatory curves\n  - about: interneuron widths before against after onset\n    test: unpaired two-tailed Kolmogorov-Smirnov test\n    p: 0.16\n    n: 128 naive and 86 (+24 h) interneuron curves\n  criterion: Chronic imaging, sessions aligned to first retrieval, binned +/-12 h. \"Before and after\n    retrieval onset\" is read as (a) naive against +24 h, as Extended Data Fig. 8a,b pairs them, or\n    (b) naive against first retrieval and +24 h pooled. Reproduced when, under every reading, the\n    excitatory width distribution shifts up with KS p < 0.0001 and the interneuron KS has\n    p >= 0.05; blocked as methods_underspecified when they disagree. The excitatory against\n    inhibitory comparison at each time point (one-way ANOVA, Bonferroni) is reported.\n\n- id: fig3h-slopes-sharpen\n  statement: Both excitatory and inhibitory population tuning sharpen at the transition 375 to 975\n    ms after virgins start retrieving.\n  source: Figure 3h\n  quote: \"both excitatory and inhibitory tuning selectively sharpened between 375:975 ms\"\n  statistics:\n  - about: excitatory\n    test: one-tailed paired t-test\n    p: 0.02\n    n: 6 mice\n  - about: inhibitory\n    test: one-tailed paired t-test\n    p: 0.02\n    n: 6 mice\n  criterion: Per-mouse population slopes (readings (v) and (vi)) before cohousing against after\n    retrieving. \"After virgins were successfully retrieving\" is read as (a) +24 h after first\n    retrieval, (b) the last session. Reproduced when, under every reading, slopes become more\n    negative at p < 0.05 by one-tailed paired t-test in both cell types; blocked as\n    methods_underspecified when they disagree.\n\n- id: fig3-retrieval-onset-range\n  statement: Retrieval onset ranged from 12 to 109 hours of cohousing in the 13 chronically imaged\n    virgins.\n  source: Methods, In vivo two-photon calcium imaging\n  quote: \"Retrieval onset ranged from 12–109 hours of cohousing in N=13 virgins\"\n  expected:\n  - quantity: earliest retrieval onset\n    value: 12\n    tolerance: 1.2\n    unit: hours\n  - quantity: latest retrieval onset\n    value: 109\n    tolerance: 10.9\n    unit: hours\n  - quantity: chronically imaged virgins\n    value: 13\n    tolerance: 0\n\n- id: ed8cd-no-change-without-cohousing\n  statement: Pup-naive virgins imaged on three consecutive days without cohousing show no systematic\n    change in temporal tuning.\n  source: Extended Data Fig. 8c,d\n  quote: \"non-cohoused controls only exposed to calls during consecutive imaging sessions showed no systematic tuning changes\"\n  criterion: A claim of absence. Single-cell normalized curves, session 1 (N=4 mice, n=53) against\n    session 3 (N=5, n=48), one-way ANOVA with Bonferroni-corrected session 1 against session 3 at\n    each morph ISI. No p is reported. Reproduced when no ISI differs at p < 0.05.\n\n- id: fig4b-ch575-broader-at-575\n  statement: Virgins that heard slow morphs (575 ms) during cohousing have excitatory tuning broader\n    at 575 ms than standard cohoused virgins.\n  source: Figure 4b; main text, paragraph citing Fig. 4b\n  quote: \"prototype-responsive neurons in virgins that heard slow exemplars were more broadly tuned to 575 ms ISIs\"\n  statistics:\n  - test: one-way ANOVA, Bonferroni correction\n    p: 0.007\n    corrected: Bonferroni\n    n: 6 CH+575 and 5 CH virgins\n  criterion: Population curves 24 h after first retrieval, CH+575 against CH (the +24 h mice of\n    Fig. 3e, per Methods; reading (vi)). Reproduced when CH+575 exceeds CH at 575 ms at p < 0.05\n    with Bonferroni over the seven morph ISIs.\n\n- id: fig4c-ch575-retrieve-slow\n  statement: Virgins exposed to slow morphs during cohousing retrieve pups dubbed with slow morphs\n    more reliably than standard cohoused virgins (75% against 14.3% of trials).\n  source: Figure 4c; main text, paragraph citing Fig. 4c\n  quote: \"virgins in the CH+575 group retrieved cold pups dubbed over with slow morphs (ISI:575 ms; 75% of trials) more reliably than controls (14.3%\"\n  statistics:\n  - test: two-tailed Fisher's test\n    p: 0.001\n    n: CH 14-26 trials, CH+575 12-16 trials\n  expected:\n  - quantity: CH+575 retrieval of slow morphs\n    value: 75\n    tolerance: 7.5\n    unit: \"% of trials\"\n  - quantity: CH retrieval of slow morphs\n    value: 14.3\n    tolerance: 1.4\n    unit: \"% of trials\"\n  criterion: Reproduced when both rates are within tolerance and the two-tailed Fisher's exact test\n    gives p < 0.05. Latencies (Extended Data Fig. 8f, p=0.73, Mann-Whitney) are reported.\n\n- id: fig4d-actx-inhibition-blocks\n  statement: Photoinhibiting left auditory cortex only during slow morph playback blocks the learning\n    of slow ISIs (18.8% against 66.7% in shams) without affecting retrieval of prototypes or\n    latencies.\n  source: Figure 4d; Extended Data Fig. 8g\n  quote: \"Photoinhibiting left auditory cortex (ACtx) exclusively during slow morph playback selectively blocked the learning of slow ISIs compared to shams\"\n  statistics:\n  - about: slow morphs, sham against opto-ACtx\n    test: two-tailed Fisher's test\n    p: 0.02\n    n: sham 3 mice 12 trials, opto 4 mice 16 trials\n  - about: latencies\n    test: unpaired two-tailed Mann-Whitney test\n    p: 0.19\n    n: 26 and 23 trials\n  expected:\n  - quantity: sham retrieval of slow morphs\n    value: 66.7\n    tolerance: 6.7\n    unit: \"% of trials\"\n  - quantity: opto-ACtx retrieval of slow morphs\n    value: 18.8\n    tolerance: 1.9\n    unit: \"% of trials\"\n  criterion: Reproduced when both rates are within tolerance, slow differs at p < 0.05 by two-tailed\n    Fisher's exact test, and prototypes do not.\n\n- id: ed8hi-single-syllables-not-learned\n  statement: Virgins hearing single syllables during cohousing do not learn to retrieve pups dubbed\n    with single syllables.\n  source: Extended Data Fig. 8h,i; main text, paragraph citing it\n  quote: \"virgins hearing single syllables (ISI:30s) during cohousing were unable to associate these calls with isolated pups\"\n  statistics:\n  - about: single syllable, CH 22.2% (9 trials) against CH+SS 25.0% (16)\n    test: two-tailed Fisher's exact test\n    p: 0.99\n    p_relation: \">\"\n  - about: warm, CH 84.6% (13) against CH+SS 85.7% (14)\n    test: two-tailed Fisher's exact test\n    p: 0.99\n    p_relation: \">\"\n  - about: latencies\n    test: unpaired two-tailed Mann-Whitney test\n    p: 0.98\n    n: 17 trials each\n  criterion: A claim of absence. Two-tailed Fisher's exact test, CH against CH+SS, single syllable\n    trials. Reproduced when p >= 0.05; the rates are reported.\n\n- id: ed9b-oxytocin-enhances-spiking\n  statement: Oxytocin enhances spiking to repeated 575 ms pulses in auditory cortical slices from\n    stimulus 2 on, while stimulation without oxytocin does not change spike probability.\n  source: Extended Data Fig. 9a,b\n  quote: \"evoked spike probability was significantly enhanced 15–30 minutes following the onset of oxytocin wash\"\n  statistics:\n  - about: stim 1\n    test: one-way Friedman test with Dunn's correction\n    p: 0.34\n    n: 9 cells\n  - about: stim 2\n    test: one-way Friedman test with Dunn's correction\n    p: 0.009\n  - about: stim 3\n    test: one-way Friedman test with Dunn's correction\n    p: 0.008\n  - about: stim 4\n    test: one-way Friedman test with Dunn's correction\n    p: 0.001\n  - about: stim 5\n    test: one-way Friedman test with Dunn's correction\n    p: 0.04\n  data: elsewhere\n  where: figshare doi:10.6084/m9.figshare.12613811.v1 (In vitro recordings_oxytocin)\n  criterion: Spike probability per pulse, baseline against 15-30 min after wash onset. Reproduced\n    when stimuli 2 to 5 increase at p < 0.05 by Friedman test with Dunn's post hoc, stimulus 1 does\n    not, and ACSF controls (n=7) show no change at p < 0.05.\n\n- id: fig4e-ot-inhibition-deficits\n  statement: Inhibiting oxytocin neurons during slow morph playback lowers retrieval of warm pups\n    (43.8% against 92.3%), prototype-dubbed pups (36.8% against 83.3%) and slow-morph-dubbed pups\n    (33.3% against 83.3%), and lengthens latencies.\n  source: Figure 4e; Extended Data Fig. 9d\n  quote: \"we observed deficits in retrieval rates for warm pups (CH+575 sham : 92.3% vs. CH+575 opto-OT : 43.8% of trials), as well as cold pups dubbed over with prototypes (83.3% vs. 36.8%) and slow morphs (83.3% vs. 33.3%\"\n  statistics:\n  - about: warm\n    test: two-tailed Fisher's test\n    p: 0.008\n    n: sham 3 mice 12-13 trials, opto-OT 5 mice 16-19 trials\n  - about: prototypes\n    test: two-tailed Fisher's test\n    p: 0.02\n  - about: slow\n    test: two-tailed Fisher's test\n    p: 0.01\n  - about: latencies\n    test: unpaired two-tailed Mann-Whitney test\n    p: 0.0003\n    n: 32 and 20 trials\n  expected:\n  - quantity: warm, sham\n    value: 92.3\n    tolerance: 9.2\n    unit: \"% of trials\"\n  - quantity: warm, opto-OT\n    value: 43.8\n    tolerance: 4.4\n    unit: \"% of trials\"\n  - quantity: prototypes, sham\n    value: 83.3\n    tolerance: 8.3\n    unit: \"% of trials\"\n  - quantity: prototypes, opto-OT\n    value: 36.8\n    tolerance: 3.7\n    unit: \"% of trials\"\n  - quantity: slow, sham\n    value: 83.3\n    tolerance: 8.3\n    unit: \"% of trials\"\n  - quantity: slow, opto-OT\n    value: 33.3\n    tolerance: 3.3\n    unit: \"% of trials\"\n  criterion: Reproduced when all six rates are within tolerance and each pair differs at p < 0.05 by\n    two-tailed Fisher's exact test.\n\n- id: fig4g-ot-inhibition-narrow-tuning\n  statement: Virgins with oxytocin neurons inhibited during cohousing have uncharacteristically\n    narrow tuning 24 hours after first retrieval, narrower than cohoused virgins' excitatory and\n    inhibitory tuning.\n  source: Figure 4f,g; Extended Data Fig. 9e\n  quote: \"These behavioral deficits were associated with uncharacteristically narrow temporal tuning in auditory cortex 24 hours after first retrieval\"\n  statistics:\n  - about: opto-OT against CH excitatory\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.008\n    n: 4 opto-OT and 14 CH mice\n  - about: opto-OT against CH inhibitory\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.03\n    n: 4 opto-OT and 10 CH mice\n  criterion: Per-mouse tuning widths (reading (vi)); CH is all retrieving virgins imaged (Methods),\n    excitatory N=14 and inhibitory N=10. Reproduced when opto-OT is lower than both at p < 0.05 by\n    Kruskal-Wallis with Dunn's post hoc. Which mice make up the 14 and 10 is not listed; the\n    counts reached are reported.\n\n- id: fig4h-ot-like-unreliable-retrievers\n  statement: Single-cell tuning in opto-OT virgins is narrower than in reliably retrieving virgins\n    but similar to virgins retrieving on 10-30% of trials.\n  source: Figure 4h; main text, paragraph citing Fig. 4h\n  quote: \"Single-cell tuning curves in CH+575 opto-OT virgins were significantly narrower compared to reliably retrieving virgins\"\n  statistics:\n  - about: against CH 100%\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.0001\n    p_relation: \"<\"\n    n: 40 opto-OT and 52 CH 100% curves\n  - about: against CH 10-30%\n    test: Kruskal-Wallis test with Dunn's correction\n    p: 0.99\n    p_relation: \">\"\n    n: 40 opto-OT and 78 CH 10-30% curves\n  criterion: Single-cell widths of opto-OT (N=4, n=40) and the two virgins of Extended Data Fig. 4g\n    before (n=78) and after (n=52) reliable retrieval. Reproduced when opto-OT is lower than CH 100%\n    at p < 0.05 and does not differ from CH 10-30%, by Kruskal-Wallis with Dunn's post hoc.\n  depends_on:\n  - ed4g-broadening-with-reliable-retrieval\n\n- id: ed3bc-neuropil-no-effect\n  statement: Neuropil correction has no significant effect on prototype-evoked dF/F in excitatory or\n    inhibitory neurons.\n  source: Extended Data Fig. 3a-c; Methods, Image processing and analysis\n  quote: \"Neuropil correction had no significant effect on call-evoked ΔF/Fs in excitatory or inhibitory neurons\"\n  statistics:\n  - about: excitatory\n    test: two-tailed unpaired Kolmogorov-Smirnov test\n    p: 0.57\n    n: 52 neurons, one region\n  - about: inhibitory\n    test: two-tailed unpaired Kolmogorov-Smirnov test\n    p: 0.14\n    n: 64 neurons, one region\n  criterion: A claim of absence. F_true = F_raw - r F_neuropil, r = F_blood_vessel / F_neuropil, on\n    one excitatory and one inhibitory region; which regions is not said, so every region is run and\n    the claim judged on the regions with 52 and 64 responsive neurons if they can be identified, and\n    on all otherwise. Reproduced when the two-sample KS test of corrected against uncorrected\n    prototype dF/F gives p >= 0.05 in both.\n"
}
```

```
File created successfully at: claims/000249/10.1038-s41586-020-2807-6.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/000249/10.1038-s41586-020-2807-6.yaml paper/10.1038-s41586-020-2807-6.txt; echo EXIT $?
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/000249/10.1038-s41586-020-2807-6.yaml",
 "old_string": "    Fig. 1f) against right (N=4). The p of 0.003 is below the smallest exact two-sided Mann-Whitney\n    p for 9 against 4 mice (2/715, about 0.0028, only at complete separation), so the test may have\n    been run over curves; the readings are (a) mice, (b) single-cell tuning curves. Reproduced when,\n    under one reading, left exceeds right at p < 0.05.",
 "new_string": "    Fig. 1f) against right (N=4). The legend gives N in mice, and p = 0.003 matches the smallest\n    exact two-sided Mann-Whitney p for 9 against 4 mice (2/715, about 0.0028, complete separation).\n    The unit is not stated otherwise; the readings are (a) mice, (b) single-cell tuning curves.\n    Reproduced when, under one reading, left exceeds right at p < 0.05."
}
```

```
The file claims/000249/10.1038-s41586-020-2807-6.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
f=claims/000249/10.1038-s41586-020-2807-6.yaml; grep -n "—\|rather" $f; python3 - <<'E'
import re
for i,l in enumerate(open("claims/000249/10.1038-s41586-020-2807-6.yaml"),1):
    if l.lstrip().startswith('#'): continue
    s=l.rstrip('\n')
    m=re.match(r'^\s*(- )?[A-Za-z_]+: (.*)$',s)
    rest = m.group(2) if m else s.strip()
    if rest.startswith('"'): continue
    if ': ' in rest: print(i,s)
E
python tools/claims_check.py $f paper/10.1038-s41586-020-2807-6.txt
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/000249/10.1038-s41586-020-2807-6.yaml`. The quote checker passes it (44 claims, 44 quotes, 90 statistical values, 0 problems), and it has no em dashes, no "rather" and no ": " in plain scalars. Nothing was committed.

**Text read.** The NIH author manuscript in PubMed Central (PMC7677212), not the version of record: main text, Methods, the four main figure legends and the ten Extended Data legends. There is no separate supplement, and I used no PDF. The source-data Excel sheet the paper mentions is not available, and no claim needs it.

**Code.**
- **Link fails:** the paper's code and data DOI (`10.35092/yhjc.c.5037737`) did not resolve on doi.org, DataCite or the figshare API.
- **Collection checked instead:** the dandiset links figshare collection `c.5043830.v6`. Its only code is "Behavior code" (`13054076.v1`), MATLAB that runs the operant task: 30-minute sessions, with a touch time written at each polling sample.
- **No analysis code:** none was deposited, so every method detail comes from the Methods and the legends.

**Claims.** 44 in all (1 link check, 43 findings). All 44 have quotes and none needed `inferred`. 41 have statistics, 13 have expected values with tolerances and 41 have criteria. 10 use whole-cell or operant data on figshare (`elsewhere`), one needs the ISI distribution as an input, and the link claim needs subject labels. The dandiset holds only the two-photon imaging; the rest are behaviour or ISI-distribution claims whose data the dandiset does not seem to hold.

**Details left open, with the readings named:**
- **Imaging method (in the opening comment):**
  - ROIs were drawn by hand; any other segmentation counts as a deviation.
  - The 1.5 SD rule: SD of baseline frames, or SD of trial-wise baselines.
  - The peak shift of the window: one shift per cell, or one per stimulus.
  - Tuning width with or without the prototype: this cannot change any test, so I made a standard choice.
  - Slope: two-point, or least squares over 375, 575 and 975 ms.
  - Population tuning: mean of single-cell curves, or normalized from the raw mean.
  - Normalized ΔF/F when P+M ≤ 0: used as computed, and the count reported.
- **Per-claim readings:**
  - Fig 1c: the family for FDR correction.
  - Fig 1f: the ANOVA design.
  - ED 6c: the Bonferroni family.
  - ED 2b: whether prototypes are in the 75–375 ms bin.
  - ED 3e: ~16% as a mean over mice, or over pooled neurons.
  - ED 3m and ED 4c: the sample unit (mice or tuning curves).
  - ED 4d: raw or normalized ΔF/F.
  - Fig 1g: the ANOVA factors.
  - Fig 1i: the gap that ends a press, and which sessions are compared.
  - Fig 3f: naive against +24 h, or against pooled post-onset sessions.
  - Fig 3h: which "retrieving" session.
  - ED 6d and Fig 4g: which mice make up the stated counts.
  - ED 3b,c: which regions were neuropil-corrected.
  - Whole-cell: the largest 5 or the largest 10 trials.

**Missing from the paper:**
- Fig 1g and Fig 2f print no p-value, only asterisks. I recorded p < 0.05.
- Neither the dandiset description nor the text says whether the dandiset holds ROIs or stimulus identity per presentation. The link claim tests this.
- The fig1a claim's "fewer than 1% of ISIs at 550 ms or more" stands in for the paper's "essentially never". That bound is mine and is flagged as such in the criterion.

## End of run

28 turns, 6 minutes, result: success.
