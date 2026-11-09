# 001341 · claims · run 39684083245

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/001453/ claims/001341 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -l paper/*.txt; head -30 paper/10.1073-pnas.2514107123.txt; head -20 paper/10.1101-2025.03.29.646003.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 150,400p claims/001453/*.yaml
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
[... 152 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,700p claims/001453/*.yaml; cat tools/claims_check.py | head -80
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
wc -l claims/001453/*.yaml; cat schemas/claims.schema.json | head -200
```

```
321 claims/001453/10.1016-j.cub.2025.04.027.yaml
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
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,320p schemas/claims.schema.json
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
[... 101 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1073-pnas.2514107123.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Main text read. Now reading the rest (references and the supplement text).

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1073-pnas.2514107123.txt').read()
i=t.find('Supplementary Information') 
print(len(t)); 
import re
s=t[52000:]
j=s.find('SI Appendix'); 
" ; python3 -c "
t=open('10.1073-pnas.2514107123.txt').read()
for k in ['Supplement','SUPPLEMENT','Supporting','Animal Preparation','Data Analysis','Table S1','github']:
  print(k,[m.start() for m in __import__('re').finditer(k,t)][:20])
"
```

```
129456
Supplement [44475, 75347]
SUPPLEMENT []
Supporting [75426]
Animal Preparation [42977]
Data Analysis [44381]
Table S1 [11411, 12254, 42812, 43569, 69925, 70279, 76565, 88818, 88908, 94456, 103182, 105461]
github [108487, 108667, 109258, 110237, 115020, 119710]
```

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.1073-pnas.2514107123.txt').read()
print(t[60000:100000])" | fold -w 250 -s
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
t=open('paper/10.1073-pnas.2514107123.txt').read()
open('$TMPDIR/p.txt','w').write(t[52000:])"; fold -w 300 -s $TMPDIR/p.txt > $TMPDIR/pf.txt; wc -l $TMPDIR/pf.txt; echo $TMPDIR
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pf.txt",
 "limit": 400
}
```

```
1	 , Pezaris JS , Sahani M , Mitra PP , Andersen RA , Temporal structure in neuronal activity during working memory in macaque parietal cortex . Nat. Neurosci. 5 , 805 – 811 ( 2002 ), 10.1038/nn890 . 12134152 37. Bellardita C , Kiehn O , Phenotypic characterization of speed-associated gait changes in 
2	mice reveals modular organization of locomotor networks . Curr. Biol. 25 , 1426 – 1436 ( 2015 ), 10.1016/j.cub.2015.04.005 . PMC4469368 25959968 38. Pillow JW , Spatio-temporal correlations and visual signalling in a complete neuronal population . Nature 454 , 995 – 999 ( 2008 ), 
3	10.1038/nature07140 . PMC2684455 18650810 39. Esmaeili V , Learning-related congruent and incongruent changes of excitation and inhibition in distinct cortical areas . PLoS Biol. 20 , e3001667 ( 2022 ), 10.1371/journal.pbio.3001667 . PMC9187120 35639787 40. Stringer C , Spontaneous behaviors drive 
4	multidimensional, brainwide activity . Science 364 , eaav7893 ( 2019 ), 10.1126/science.aav7893 . PMC6525101 31000656 41. Keller Georg B. , Bonhoeffer T , Hübener M , Sensorimotor mismatch signals in primary visual cortex of the behaving mouse . Neuron 74 , 809 – 815 ( 2012 ), 
5	10.1016/j.neuron.2012.03.040 . 22681686 42. Musall S , Tactile frequency discrimination is enhanced by circumventing neocortical adaptation . Nat. Neurosci. 17 , 1567 – 1573 ( 2014 ), 10.1038/nn.3821 . 25242306 43. Staiger JF , Petersen CCH , Neuronal circuits in barrel cortex for whisker sensory 
6	perception . Physiol. Rev. 101 , 353 – 415 ( 2020 ), 10.1152/physrev.00019.2019 . 32816652 44. Cunningham JP , Yu BM , Dimensionality reduction for large-scale neural recordings . Nat. Neurosci. 17 , 1500 – 1509 ( 2014 ), 10.1038/nn.3776 . PMC4433019 25151264 45. Churchland MM , Stimulus onset 
7	quenches neural variability: A widespread cortical phenomenon . Nat. Neurosci. 13 , 369 – 378 ( 2010 ), 10.1038/nn.2501 . PMC2828350 20173745 46. Ganguli S , One-dimensional dynamics of attention and decision making in LIP . Neur
[... 393 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pf.txt",
 "offset": 400,
 "limit": 520
}
```

```
400	 
401	
402	=== page 10 ===
403	 
404	 
405	10 
406	 
407	 
408	Figure S7. Procedure for extraction of reaction times.  
409	A) Top: Run angle (animal 503) during a 305 OL_L left turn trials corresponding to data in Fig.2A. 
410	Blue curve is ensemble average. Bottom: Angle derivative for data in Top. Red curve is ensemble 
411	average. Red arrows show characteristic push by RH leg (Fig.2G) at the turn start and LH leg at the 
412	turn end. Vertical red dashed lines correspond to the start (t=0s) and the end (t=1.8s) of the turn. 
413	B) Same as A) but for 304 OL_R right turns randomized with left turns in A). Blue arrows show 
414	characteristic push by LH leg (Fig.2G) at the turn start and RH leg at the turn end. Vertical red dashed 
415	lines correspond to the start (t=0s) and the end (t=1.8s) of the turn. 
416	C) Run angle (animal 489) during 520 trials at the start of the left turn corresponding to data in 
417	Fig.S6A.  
418	D) Histogram of the maximum angle derivative (reaction time) for data in C). 
419	E) Run angle (animal 503) during 305 trials at the start of the left turn corresponding to data in D). 
[... 500 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/pf.txt",
 "offset": 919,
 "limit": 520
}
```

```
919	Eq.2 
920	where γ is a calibrated feedback coefficient. When taken as negative it generates a positive closed-
921	loop (CL) virtual reality (VR) that moves walls closer to the snout if the animal is moving closer to 
922	them and, therefore, encourages the animal to stay in the middle of the VR corridor.  
923	The real time control and acquisition system is custom designed to power a FPGA 
924	CompactRIO (cRIO-9045, NI) with 32 channel analog voltage input module (NI 9205) to read sphere 
925	velocities, 4 channel analog output module (NI‐9263) to operate mechanical walls, and 32 channel 
926	TTL input/output (NI-9403) to provide synchronization to video cameras and other equipment. The 
927	module is operated via LabVIEW real time module (NI) by the custom designed LabVIEW acquisition 
928	and control program7 that has Master/Slave architecture. The program operates several parallel 
929	processes that need to run simultaneously and continuously but at different rates. The master 
930	process runs in a loop at 30MHz and provides real time analog acquisition and control data to the 
931	rig. The master loop controls several slave loops and communicates with them using messaging 
932	architectures. One of the slave loops buffers recorded data and logs the data to disk at its own much 
933	slower pace. As a result, the acquisition and control experimental protocol executed in the master 
934	loop can run continuously without interruptions with virtually no inter-trial interval. Another slave loop 
935	is designed to provide a graphical user interface (GUI) that allows the user to observe data on the 
936	screen such as overlaid trial trajectories of the animal and to change parameters for each trial 
937	session if needed. Control signals generated in the master loop are directed to synchronize 3 high-
938	speed cameras (Fig.1A) to acquire videos of whiskers and paws, as well as to synchronize 
[... 495 more lines not kept]
```

**Agent**

The main text, Methods and supplement are all present. Table S2/S3 are images in the text; I'll check the supplement PDF page for them, and look at the preprint text.

**Agent calls Bash**

```bash
cd  head -c 3000 paper/10.1101-2025.03.29.646003.txt; echo; wc -c paper/10.1101-2025.03.29.646003.txt; grep -o 'github[^ ]*' paper/*.txt | sort | uniq
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import fitz
d=fitz.open('paper/10.1073-pnas.2514107123.supp.pdf'); print(len(d))
p=d[16]; pix=p.get_pixmap(dpi=110); pix.save('$TMPDIR/p17.png')
" && echo ok
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1073-pnas.2514107123.supp.pdf",
 "pages": "17"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import re
t=open('paper/10.1101-2025.03.29.646003.txt').read()
for k in ['Table S2','BIC','slope','linear regression','t-test','t test','P >','p >','epoch 2 delay','delay of','2.91','11.12','12.25','13.05','dimensionality','success rate','psychometric']:
    for m in re.finditer(re.escape(k),t):
        print('==',k,':',t[max(0,m.start()-250):m.start()+300].replace('\n',' '))
        break
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/001341/10.1073-pnas.2514107123.yaml",
 "content": "# Claims for Armstrong & Vlasov (2026), \"Neural correlates of perceptual decision-making in the\n# primary somatosensory cortex\", PNAS 123(18) e2514107123, on dandiset 001341.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read. The accepted author manuscript in PubMed Central (NIHMS2207436, PMC13142948, as served\n# by Europe PMC), full text with figure legends, and its SI Appendix (NIHMS2207436-supplement-1.pdf,\n# extracted to text in the same file), which holds Figures S1 to S12, Table S1, the SI Materials and\n# Methods and the SI Data Analysis. The main text's Materials and Methods is a short pointer to the\n# SI; the methods below come from the SI. Tables S2 and S3 (fitted DDM parameters, animals 489 and\n# 503) are images with no extracted text, and the PDF page could not be rendered in this run, so\n# their numbers are known only where the main text repeats them. The bioRxiv preprint\n# (10.1101/2025.03.29.646003, version 1) was searched for method details the published text lacks;\n# it gives none beyond the published text, and no claim rests on it.\n#\n# Code. The paper links no analysis code of its own. It names third-party tools only: Kilosort 3,\n# the Allen Institute ecephys_spike_sorting package, Phy, the Pillow lab GLM tutorial\n# (github.com/pillowlab/GLMspiketraintutorial_python), PyDDM (github.com/mwshinn/PyDDM) and SLEAP.\n# None of these holds the paper's settings, so no repository was read and no detail below is\n# settled by code.\n#\n# Data the paper describes. 19 Scnn1a-TG3-Cre x Ai32 (or Scnn1a) mice, P65 to P112, both sexes\n# (Table S1). All whiskers but the two C2 whiskers trimmed. Each animal ran one unrewarded 2-h\n# terminal session on an air-suspended sphere in tactile VR. Trials are closed-loop (CL) straight\n# runs, with walls at 10 mm following the animal, and open-loop (OL) turns: at t = 0 (start of\n# wall movement, \"trial switch\") the walls retract within about 12 ms, then one wall approaches\n# the snout within 0.2 s to 2 mm and stays for 1.8 s before retracting. OL_L (left turn) trials\n# have the right wall approaching, contralateral to the probe in the left hemisphere; OL_R (right\n# turn) trials have the left wall approaching (ipsilateral). Ephys animals (Table S1) 453, 454,\n# 456 (D1, D2, D2 barrels), 480, 489, 503, 516, 528, 579 (C2), 482 (B2), 488 and 530 (C1), 517\n# (C3); probes Cambridge NeuroTech 64-channel or Neuropixels 1.0. Behaviour-only animals 474, 475,\n# 499, 518 (psychometric curves, Fig. 2C-D), 573 (whisker tracking, Fig. 2E, F, I) and 589\n# (whisker and gait tracking, Fig. 2G-H, Fig. 3A-D, G-P). Units are Kilosort 3 + ecephys quality\n# filtered (amplitude cutoff <= 0.1, ISI violations <= 0.5, presence ratio >= 0.90) and curated in\n# Phy; FS if waveform duration < 0.4 ms, else RS; each unit has a cortical depth and layer (L2/3,\n# L4, L5A, L5B, L6). Behaviour: sphere forward and lateral velocity at 500 Hz, run angle (Eq. 1),\n# wall positions, the wall feedback signal V_wall (Eq. 2), whisker angle and curvature from 1,000\n# fps video (SLEAP), whisker-wall touch times, and paw contacts from 50 fps side video. The SI says\n# spikes of all filtered units are packaged with the behavioural data in one NWB file per animal.\n# The paper cites dandiset 001341 version 0.260414.1316. Example animal for Figs. 1, 4 and 5B is\n# 489 (65 units, 266 OL_L and 265 OL_R trials); for Fig. 2A-B it is 503.\n#\n# Definitions used by several criteria, all from the paper.\n# - t = 0 is the start of wall movement in an OL trial (Fig. 1L-O legends, \"vertical dashed line\n#   corresponds to start of wall movement\"); the turn lasts to t = 1.8 s.\n# - Population-averaged spike rate (SI Data Analysis, Spike rates): spikes binned at 0.005 s,\n#   averaged over the trials of one type, and averaged over the units of the animal (\"normalized on\n#   the number of units\"), in Hz. For comparison with the DDM (Fig. 4B, Fig. S9) and between\n#   animals (Fig. 5B-D), min-max normalised to 0 and 1. The SI names no smoothing; criteria use\n#   unsmoothed 5 ms bins and say where smoothing could matter.\n# - Epoch windows (Results). Epoch 1 is t < 0. Epoch 2 is the sharp peak at t = 0.026 s (animal\n#   489). Epoch 3 is the suppression, \"(+65 ms: +140 ms)\" (Results, Could the neural activity...,\n#   paragraph 2), ending at the ramp onset, which Fig. 4B and the Results put at 0.12 s for animal\n#   489. Epoch 4 is the ramp, from that onset to its maximum, at t = 0.25 s in Fig. 1N and at t =\n#   0.23 s in the SI (Analysis of VarCE). Epoch 5 is the later stable spiking to t = 1.8 s.\n# - Reaction time (SI, Fitting of drift diffusion models): the largest peak of the lateral\n#   acceleration (\"or run angle derivative\") after the start of the turn trial. Correct trial: the\n#   animal \"achieves ±1cm clearance at t=1s from the trial start\", otherwise error.\n#\n# Inconsistencies found in the paper, recorded so that the author can name them.\n# - Unit counts. The SI says 634 units (Fig. S2C, n = 12 animals); Table S1 totals 668 over 13\n#   ephys animals. The difference is animal 579 (34 units, the GLM animal of Fig. 2J-K).\n# - Fig. 2K shows 30 units for animal 579, which Table S1 lists with 34. The GLM used 40 random CL\n#   trials (SI) or 55 CL trials (Fig. 2J legend).\n# - Animal 503. Fig. 2A has 414 trials, Fig. S1 481 trials, Fig. S4A and Fig. S7 305 OL_L and 304\n#   OL_R trials, Table S1 1027 trials in all. Animal 489. Fig. 1J-K has 266 OL_L and 265 OL_R\n#   trials; Fig. S6A and Fig. S7C have 520 OL_L trials.\n# - Unit 489101 is \"RS, layer 5A\" in Fig. 4F and Fig. S10, \"RS, layer 5B\" in Fig. S5E.\n# - Fig. 2C-D give n = 5 animals; the Results give n = 7; Table S1 lists four animals (474, 475,\n#   499, 518) for Fig. 2C-D.\n# - The reported DDM drift K = 2.91 and bound B = 0.59 give K/B = 4.93, not the 11.12 the text\n#   gives as \"normalized drift\" (which follows the GDDM sentence).\n# - The Results call whisking amplitudes, set angles and curvature maxima across epochs\n#   \"statistically identical\" (Fig. 3J-L); the legends of Fig. 3J, K and L give \"Two-sample t\n#   test P value < 0.0001\".\n# - Epoch 2 peaks at t = 0.026 s (Fig. 1N) and first touch is at 0.06 to 0.07 s (Fig. 2F, 2I), yet\n#   the Results say epoch 2 peaks \"appear within 10 ms range from FT\".\n# - The streak index is described as a count of 0-1 switches in an 8-bin string (0 to 7), but its\n#   reported distribution has mean 0.06 and SD 1.36, which a count of switches cannot have.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001341\"\n  doi: 10.48324/dandi.001341\npaper: doi:10.1073/pnas.2514107123\nclaims:\n- id: table-s1-recordings\n  statement: The recordings comprise 13 ephys sessions and 6 behaviour-only sessions, one per\n    animal, with the numbers of accepted single units and of trials per animal listed in Table S1,\n    and with the units and OL turn trials of the example sessions given in Fig. 1J-K and Fig. S4.\n  source: SI Appendix, Table S1; Fig. 1J-K legend; Fig. S4 legend\n  inferred: Numbers read from Table S1 and the legends of Fig. 1J-K and Fig. S4; no sentence states\n    them together.\n  expected:\n  - {quantity: units animal 453, value: 56, tolerance: 0}\n  - {quantity: units animal 454, value: 40, tolerance: 0}\n  - {quantity: units animal 456, value: 39, tolerance: 0}\n  - {quantity: units animal 480, value: 42, tolerance: 0}\n  - {quantity: units animal 482, value: 38, tolerance: 0}\n  - {quantity: units animal 488, value: 29, tolerance: 0}\n  - {quantity: units animal 489, value: 65, tolerance: 0}\n  - {quantity: units animal 503, value: 48, tolerance: 0}\n  - {quantity: units animal 516, value: 33, tolerance: 0}\n  - {quantity: units animal 517, value: 42, tolerance: 0}\n  - {quantity: units animal 528, value: 89, tolerance: 0}\n  - {quantity: units animal 530, value: 113, tolerance: 0}\n  - {quantity: units animal 579, value: 34, tolerance: 0}\n  - {quantity: trials animal 453, value: 2563, tolerance: 256}\n  - {quantity: trials animal 454, value: 2581, tolerance: 258}\n  - {quantity: trials animal 456, value: 2262, tolerance: 226}\n  - {quantity: trials animal 474, value: 131, tolerance: 13}\n  - {quantity: trials animal 475, value: 55, tolerance: 5.5}\n  - {quantity: trials animal 480, value: 758, tolerance: 76}\n  - {quantity: trials animal 482, value: 1518, tolerance: 152}\n  - {quantity: trials animal 488, value: 939, tolerance: 94}\n  - {quantity: trials animal 489, value: 1000, tolerance: 100}\n  - {quantity: trials animal 499, value: 1123, tolerance: 112}\n  - {quantity: trials animal 503, value: 1027, tolerance: 103}\n  - {quantity: trials animal 516, value: 1071, tolerance: 107}\n  - {quantity: trials animal 517, value: 1287, tolerance: 129}\n  - {quantity: trials animal 518, value: 1291, tolerance: 129}\n  - {quantity: trials animal 528, value: 525, tolerance: 53}\n  - {quantity: trials animal 530, value: 1654, tolerance: 165}\n  - {quantity: trials animal 573, value: 401, tolerance: 40}\n  - {quantity: trials animal 579, value: 55, tolerance: 5.5}\n  - {quantity: trials animal 589, value: 50, tolerance: 5}\n  - {quantity: OL_L and OL_R trials animal 489 (Fig. 1J-K), value: 531, tolerance: 0}\n  - {quantity: OL_L and OL_R trials animal 503 (Fig. S4A), value: 609, tolerance: 0}\n  - {quantity: OL_L and OL_R trials animal 528 (Fig. S4B), value: 190, tolerance: 0}\n  - {quantity: OL_L and OL_R trials animal 530 (Fig. S4C), value: 805, tolerance: 0}\n  - {quantity: OL_L and OL_R trials animal 482 (Fig. S4D), value: 700, tolerance: 0}\n  - {quantity: OL_L and OL_R trials animal 480 (Fig. S4E), value: 375, tolerance: 0}\n  - {quantity: OL_L and OL_R trials animal 517 (Fig. S4F), value: 538, tolerance: 0}\n  criterion: Unit counts are single units that passed the acceptance criteria (Table S1 footnote;\n    SI Spike sorting and unit filtering) and must match exactly, as must the OL_L plus OL_R counts\n    of Fig. 1J-K and Fig. S4, which the legends give per turn type (489 266 and 265; 503 305 and\n    304; 528 95 and 95; 530 402 and 403; 482 350 and 350; 480 185 and 190; 517 270 and 268); the\n    per-type counts are compared as well. Table S1 trials are \"Total number of trials including CL\n    straight, randomzied left and right turns\" and are matched within 10%. Reproduced when every\n    unit count and every OL count matches and at least 17 of the 19 total trial counts are within\n    tolerance; partially reproduced when the unit counts match for at least 10 of the 13 ephys\n    animals. The notes list each mismatch and the inconsistencies the header names.\n- id: fig1lm-staged-modulation\n  statement: In the C2 principal barrel column, population spiking across all layers is strongly\n    and synchronously modulated during OL turns, in five consecutive epochs (stable spiking, a\n    sharp peak, suppression, a ramp for contralateral turns, and a return to stable spiking).\n  source: Results, Population dynamics in C2 barrel column..., paragraph 2; Fig. 1J-O\n  quote: Spiking activity across all cortical layers is strongly modulated during navigation\n    decisions and can roughly be divided into five consecutive epochs\n  criterion: Animal 489, all units, population-averaged spike rate (header) over the 266 OL_L\n    trials and, separately, the 265 OL_R trials. Reproduced when, for OL_L, the rate shows in\n    order a peak between 0 and 0.065 s above the epoch 1 mean (t from -1 to 0 s), a minimum\n    between 0.065 and 0.14 s below the epoch 1 mean, a maximum between 0.12 and 0.3 s above the\n    epoch 1 mean, and a mean rate from 0.5 to 1.8 s that is below that maximum; and, for OL_R, the\n    same epoch 2 peak and epoch 3 suppression. Each \"above\" or \"below\" is judged by a two-sided\n    Wilcoxon signed-rank test over units at p < 0.05 on per-unit trial-averaged rates in the two\n    windows (the paper gives no test; the windows are the paper's, the test is this file's).\n    Partially reproduced when the OL_L sequence holds but one OL_R part fails.\n- id: fig1n-epoch-rates\n  statement: For animal 489, the population rate is about 2 Hz during straight running before the\n    turn, peaks sharply at t = 0.026 s (epoch 2), drops to about 0.7 Hz (epoch 3) for both turn\n    directions, and, for contralateral turns only, ramps to a maximum at about t = 0.25 s (epoch\n    4); for ipsilateral turns the suppression lasts to the end of the turn.\n  source: Results, Population dynamics in C2 barrel column..., paragraph 2; Fig. 1N\n  quote: the stable spiking (t < 0 s, 2 ± 0.1 Hz, mean ± SD) of epoch 1 during CL straight running\n    is disrupted by a sharp peak we refer as epoch 2 (t = 0.026 s) ... Epoch 3 follows, which\n    exhibits strong suppression of spiking activity down to 0.7 ± 0.1 Hz (mean ± SD) for both left\n    and right turns ... While for ipsilateral turns the suppression lasts until the turn end ...\n    contralateral turns produce a strong ramping activity labeled as epoch 4, (t = 0.25 s\n  expected:\n  - {quantity: epoch 1 population rate, value: 2.0, tolerance: 0.1, unit: Hz}\n  - {quantity: time of epoch 2 peak, value: 0.026, tolerance: 0.005, unit: s}\n  - {quantity: epoch 3 minimum population rate, value: 0.7, tolerance: 0.1, unit: Hz}\n  - {quantity: time of epoch 4 maximum (OL_L), value: 0.25, tolerance: 0.025, unit: s}\n  criterion: Animal 489, population-averaged rate in Hz (header), OL_L and OL_R separately.\n    Tolerances are the paper's stated spread for the rates, one 5 ms bin for the epoch 2 peak time\n    (10% of 0.026 s is smaller than the bin), and 10% for the epoch 4 time. The epoch 1 window is\n    not given beyond t < 0; readings (a) -0.5 to 0 s and (b) -1 to 0 s. Epoch 2 peak is the maximum\n    bin between 0 and 0.065 s; epoch 3 minimum is the minimum bin between 0.065 and 0.14 s (both\n    windows from the Results); the epoch 4 maximum is the maximum bin between 0.12 and 0.5 s of\n    OL_L. The rates must hold for both turn types where the paper says so. Smoothing is not named\n    by the SI; the main reading is unsmoothed 5 ms bins, and because a single-bin minimum or\n    maximum depends on noise, a variant with the rates averaged over three bins is shown.\n    Reproduced when all four values match under some epoch 1 reading and the OL_R rate between\n    0.14 and 1.8 s has no maximum above the epoch 1 mean (suppression to the turn end).\n- id: fig1jk-all-units\n  statement: All five epochs dominate the activity of every one of the 65 simultaneously recorded\n    units of animal 489, reproducibly across 531 randomized trials with a jitter of about 30 ms.\n  source: Results, Population dynamics in C2 barrel column..., paragraph 2; Fig. 1J-K; Fig. S5\n  quote: all five epochs are major features that dominate the activity for all 65 simultaneously\n    recorded units ... highly reproducible across 531 randomized trials with jitter of just 30 ms\n  expected:\n  - {quantity: units recorded simultaneously, value: 65, tolerance: 0}\n  - {quantity: OL turn trials, value: 531, tolerance: 0}\n  - {quantity: trial-to-trial jitter, value: 0.03, tolerance: 0.003, unit: s}\n  criterion: Animal 489, z-scored trial-averaged rate per unit (SI Spike rates, Fig. 1J-K) over\n    OL_L trials. The paper gives no per-unit test and no definition of jitter; both are open. For\n    the units, readings (a) the unit's trial-averaged rate is lower in the epoch 3 window (0.065\n    to 0.14 s) than in epoch 1 (-1 to 0 s) and higher at its maximum in 0.12 to 0.3 s than in the\n    epoch 3 window, as signs only; (b) the same two differences tested over trials by a\n    two-sided Wilcoxon signed-rank test at p < 0.05. The unit part is reproduced when at least 90%\n    of the 65 units show both under a reading (\"all\", with a 10% margin), partially reproduced when\n    a majority do. For jitter, readings (a) the SD over trials of the time of the population\n    epoch 2 peak (maximum of the trial's summed spike count, 5 ms bins, 0 to 0.065 s); (b) the SD\n    over trials of the time of the epoch 4 maximum (0.12 to 0.5 s); jitter is reported under both\n    and holds when either is within 10% of 30 ms. The outcome is the unit part; jitter is reported\n    in the notes. When the unit readings disagree the claim is blocked as methods_underspecified.\n- id: fig1n-ramp-slope\n  statement: For animal 489 the linear slope of the epoch 4 ramp in contralateral (OL_L) trials is\n    12.25 (12.25 ± 0.88, mean ± SEM, in Fig. 4B; 12.25 ± 0.76 in Fig. 1N).\n  source: Results, Ramping neural activity reflects temporal accumulation..., paragraph 2; Fig. 4B\n    bottom; Discussion, paragraph 2; Fig. 1N\n  quote: This is noticeably close to the linear slope of ramping peak 4 of 12.25 ± 0.88 (mean ±\n    SEM)\n  expected:\n  - {quantity: epoch 4 ramp slope, value: 12.25, tolerance: 0.88}\n  criterion: Animal 489, 266 OL_L trials, population-averaged rate (header), linear regression of\n    rate on time over the ramp. The paper does not give the slope's units, the fit window or the\n    normalisation range, so readings are named. Rate units (a) min-max normalised to 0 and 1 (SI\n    Spike rates, \"For comparison with DDM results (Fig.4B ...) ... normalized\"), per second; (b)\n    Hz per second (Fig. 1N plots the unnormalised rate and its triangle gives the same slope).\n    Fit window (c) 0.12 to 0.17 s (start and end of linear ramping in Fig. 4F, SI Analysis of\n    VarCE); (d) 0.12 to 0.18 s (Fig. 4G arrows, SI); (e) 0.12 s to the epoch 4 maximum (0.25 s in\n    Fig. 1N). Normalisation range, for (a), the minimum and maximum over 0 to 1 s (the Fig. 1N\n    window) and over 0 to 1.8 s; these coincide unless the extremes fall after 1 s, and both are\n    shown. The SEM is the regression's standard error. The tolerance is the paper's SEM. The\n    claim is reproduced when the slope matches under any reading; the notebook shows all.\n- id: fig1o-trial-end-ramp\n  statement: At the end of the turn, when the contralateral wall moves back out at t = 1.8 s, the\n    contralateral population shows a peak (2'), a longer suppression with ramp onset at t = 2.0 s,\n    and a slower ramp (4') that peaks at t = 2.58 s with a slope of 2.05, about 7 times smaller\n    than the slope of the first ramp.\n  source: Discussion, paragraph 2; Fig. 1O; Results, Stages of decision-making..., paragraph 2\n  quote: Epoch 3′ suppression is significantly longer with the onset of ramping activity at t = 2.0\n    s (0.21 s delay) suggesting regulation of integration onset to task demand. Ramping in epoch 4′\n    is much slower reaching maximum at t = 2.58 s (0.78 s delay). The fitted linear slope (2.05 ±\n    0.05, mean ± SEM, black triangle in Fig. 1O ) is 7× smaller than for the first turn at trial\n    start (12.25 ± 0.76, mean ± SEM, triangle Fig. 1N )\n  expected:\n  - {quantity: time of epoch 2' peak (OL_L), value: 1.84, tolerance: 0.01, unit: s}\n  - {quantity: ramp 4' onset, value: 2.0, tolerance: 0.02, unit: s}\n  - {quantity: time of epoch 4' maximum, value: 2.58, tolerance: 0.078, unit: s}\n  - {quantity: epoch 4' slope, value: 2.05, tolerance: 0.05}\n  - {quantity: ratio of epoch 4 slope to epoch 4' slope, value: 7, tolerance: 0.7}\n  depends_on:\n  - fig1n-ramp-slope\n  criterion: Animal 489, OL_L population-averaged rate (header) over the last 1.4 s of the trial\n    (Fig. 1O, from about 1.6 to 3.0 s; the window's end is not given, readings end at 3.0 s and\n    at 3.2 s). Epoch 2' peak is the maximum bin from 1.8 to 1.9 s (paper 1.84 s, tolerance two\n    bins); ramp onset is the minimum of the epoch 3' suppression between the 2' peak and the 4'\n    maximum (tolerance 10% of the 0.21 s delay); the 4' maximum is the maximum bin from 2.0 to 3.0\n    s (tolerance 10% of the 0.78 s delay). The slope uses the readings of fig1n-ramp-slope for\n    units, with the fit window from the 4' onset to the 4' maximum, the only window the text gives;\n    the tolerance is the paper's SEM. The ratio uses the first-ramp slope under the same reading.\n    Also reported, from the same section of the Results, the time of the OL_R 2' peak (paper 2.15\n    s). Reproduced when the times and the slope ratio match under one reading; the absolute slope\n    is reported and judged as well.\n- id: fig1-ramp-contralateral-only\n  statement: The ramps of epochs 4 and 4' appear only in contralateral (OL_L) turns, while the\n    epoch 2 and 2' peaks appear for both turn directions, showing strong lateralization.\n  source: Discussion, paragraph 5; Fig. 1J-O; Fig. 5C-D\n  quote: While epochs 2 (at trial start) and 2′ (at trial end) are present for both left and right\n    turns, the ramping in epochs 4 and 4′ is exclusively presented only for contralateral left\n    turn trials indicating extraordinarily strong lateralization\n  criterion: For each ephys animal in Fig. 5C-D (480, 489, 503, 528, 482, 517, 530; Table S1), the\n    population-averaged rate (header) in OL_L and OL_R trials. Epoch 4 size is the mean rate from\n    0.12 to 0.25 s minus the mean rate from 0.065 to 0.12 s (end of suppression), and epoch 4'\n    size the mean rate from 2.0 to 2.58 s minus that from 1.9 to 2.0 s (windows from the times the\n    paper gives for animal 489). Per animal, the OL_L size is compared with the OL_R size by a\n    two-sided Mann-Whitney test over trials of the per-trial window means (the paper gives no\n    test; this is the test of this file). Reproduced when epoch 4 is larger for OL_L in every\n    animal at p < 0.05 and in at least 5 of 7 for epoch 4'; partially reproduced when epoch 4\n    holds in at least 5 of 7. Epoch 2 and 2' peaks for both directions are reported.\n- id: figs1-running-speed\n  statement: Mice run at fast speeds, 21 ± 4 cm/s (mean ± SD).\n  source: Results, Ethological decision-making..., paragraph 1; SI Fig. S1A; SI Animal preparation\n  quote: running at fast speeds (21 ± 4 cm/s, mean ± SD\n  expected:\n  - {quantity: running speed, value: 21, tolerance: 4, unit: cm/s}\n  criterion: Speed is the absolute speed of the sphere, from forward and lateral velocities. The\n    paper cites Fig. S1A, the speed histogram of animal 503 in the 481-trial experiment of Fig. 2A,\n    while Table S1 gives animal 503 a mean running speed of 16.1 cm/s; the population it refers to\n    is open. Readings (a) animal 503, mean over samples of the session's absolute speed; (b) the\n    same restricted to running, mean trial speed above 10 cm/s (Table S1 footnote); (c) across all\n    19 animals, the mean of the per-animal mean running speeds (Table S1 definition); the per-animal\n    values are also compared with Table S1's mean speeds (10% each). Reproduced when the mean lies\n    within 4 cm/s of 21 under any reading.\n- id: fig2a-success-rate\n  statement: In the unrewarded task, with a correct trial defined as ±1 cm lateral clearance at t =\n    1 s, animal 503 succeeds in 95% of 414 randomized turn trials (14 failed trajectories).\n  source: Results, Behavioral correlates of decision-making..., paragraph 1; Fig. 2A\n  quote: Defining threshold for correct trials as ±1 cm lateral clearance at t = 1 s, the success\n    rate reaches 95% (14 failed red trajectories in Fig. 2A\n  expected:\n  - {quantity: success rate, value: 0.95, tolerance: 0.095}\n  - {quantity: failed trials, value: 14, tolerance: 1.4}\n  criterion: Animal 503, OL_L and OL_R trials, lateral position integrated from the sphere's\n    lateral velocity, taken relative to the position at t = 0. Open details and readings. Which 414\n    trials (animal 503 has 609 OL trials in Fig. S4A and Fig. S7) is not said; readings (a) all OL\n    trials; (b) the first 414 consecutive OL trials (\"414 consecutive randomized left and right\n    turn trials\"). What \"±1 cm clearance\" means is not defined; readings (c) displacement at t = 1\n    s of at least 1 cm in the turn direction (left for OL_L); (d) absolute displacement of at least\n    1 cm, the deviation rule of Fig. S1B. Reproduced when the success rate is within 10% of 0.95\n    under any reading; the number of failed trials is reported for each.\n- id: fig2b-lateral-spread\n  statement: Lateral positions are tightly confined during the straight CL section (0.14 ± 0.55 cm,\n    mean ± SD, at t = 0) and their distribution widens over time after the turn (t = 1 s and 3 s),\n    about twice as wide at 3 s as at 2 s (SD 2.30 against 1.49).\n  source: Results, Behavioral correlates of decision-making..., paragraph 1; Fig. 2B; Discussion,\n    paragraph 2; Fig. S6B\n  quote: While the straight CL section produces trajectories tightly confined within 0.14 cm ± 0.55\n    (mean ± SD) ... distributions of lateral distances after the turn widen over time ... (2.30 SD\n    at 3 s trial time vs. 1.49 SD at 2 s time for Fig. 2 B , Top , and SI Appendix , Fig. S6 B ,\n    Top )\n  expected:\n  - {quantity: mean lateral distance at t = 0, value: 0.14, tolerance: 0.55, unit: cm}\n  - {quantity: SD of lateral distance at t = 0, value: 0.55, tolerance: 0.055, unit: cm}\n  - {quantity: SD of lateral distance at t = 3 s, value: 2.30, tolerance: 0.23, unit: cm}\n  - {quantity: SD of lateral distance at t = 2 s, value: 1.49, tolerance: 0.149, unit: cm}\n  criterion: Animal 503 (Fig. 2B), and animal 489 for Fig. S6B. Lateral distance is not defined\n    beyond Fig. 2B; since the values at t = 0 are not zero, it is not relative to t = 0. Readings\n    (a) the lateral position as the dataset stores it; (b) lateral velocity integrated from the\n    start of the trial's CL section. The SD at 2 s and 3 s are attributed jointly to Fig. 2B top\n    (animal 503, t = 3 s) and Fig. S6B top (animal 489, t = 2 s); readings (c) 2.30 for animal 503\n    at 3 s and 1.49 for animal 489 at 2 s; (d) both values for animal 503; (e) both for animal 489.\n    Units are taken as cm. The widening holds when the SD rises from t = 0 to 1 s to 3 s. Reproduced\n    when the t = 0 values and the widening hold and the 2 s and 3 s SDs match under one reading;\n    partially reproduced when only the t = 0 values and the widening hold.\n- id: fig2c-psychometric\n  statement: The success rate rises steeply as the approaching wall comes closer to the snout,\n    from 8 mm (whisker barely touching) to 1 mm (whisker strongly bent).\n  source: Results, Behavioral correlates of decision-making..., paragraph 1; Fig. 2C; Fig. S6E-G\n  quote: The resulting success rate as a function of wall distance ( Fig. 2C ) exhibits a strong\n    increase toward shorter distances\n  criterion: Behaviour-only psychometric animals of Table S1 (474, 475, 499, 518); the text says n =\n    7 and the legend n = 5, so any other animal whose session varies the OL wall distance is also\n    used and listed. Per animal and turn direction, success fraction (correct as in\n    fig2a-success-rate, both readings of \"±1 cm clearance\") at each wall distance with at least 20\n    trials (Fig. 2C legend). Reproduced when the population average (mean over animals) has a\n    negative Spearman correlation with distance and the average at the two shortest distances\n    exceeds that at the two longest in at least 3 of 4 animals; the paper reports no test and this\n    rule is this file's.\n- id: fig2d-turn-angle\n  statement: Turns are steeper (larger mean turn angle) when the wall comes closer.\n  source: Results, Behavioral correlates of decision-making..., paragraph 1; Fig. 2D\n  quote: Better threshold clearance is achieved by steeper turn angles ( Fig. 2D ) at closer wall\n    distances\n  depends_on:\n  - fig2c-psychometric\n  criterion: Same animals and trials as fig2c-psychometric. Turn angle is the run angle of Eq. 1,\n    theta = atan(D_lat/D_for), positive for left turns (SI Behavioral tactile virtual reality rig);\n    turns to the right are sign-flipped. How the \"mean turn angle\" of a trial is taken is not\n    given; readings (a) the mean of theta over the turn, 0 to 1.8 s; (b) the angle of the\n    displacement from t = 0 to t = 1 s, atan of lateral over forward displacement. Reproduced when\n    the population-average angle has a negative Spearman correlation with wall distance under\n    either reading.\n- id: fig2f-whisking-params\n  statement: During straight CL running the C2 whisker whisks at 15 ± 2 Hz with an amplitude of 39\n    ± 5 degrees around a set point of 58 ± 5 degrees; once the wall is close (t > 0.2 s) the\n    whisker angle is clamped at 68 ± 12 degrees.\n  source: Results, Behavioral correlates of decision-making..., paragraph 2; Fig. 2E-F\n  quote: Whisking during CL straight run (t < 0) is executed at 15 ± 2 Hz (mean ± SD) with an\n    amplitude of just 39 ± 5° (mean ± SD) around a set point of 58 ± 5° (mean ± SD) ... (whisker\n    angle clamped at 68° ± 12 (mean ± SD) for t > 0.2 s\n  expected:\n  - {quantity: whisking frequency, value: 15, tolerance: 2, unit: Hz}\n  - {quantity: whisking amplitude, value: 39, tolerance: 5, unit: deg}\n  - {quantity: whisking set point, value: 58, tolerance: 5, unit: deg}\n  - {quantity: clamped whisker angle, value: 68, tolerance: 12, unit: deg}\n  criterion: Contralateral (right) C2 whisker angle, 0 degrees perpendicular to the head's AP axis,\n    from the two tracked points nearest the base (SI Whisker tracking), in OL_L trials of the\n    whisker-tracking animal of Fig. 2E-F (573 per Table S1; 589 also has whisker tracking and is\n    shown as a variant). Phase and amplitude from the Hilbert transform (SI Multiparameter GLM);\n    set point is not defined, readings (a) the slowly varying mean of the angle (mean per whisk\n    cycle); (b) the mean angle over t < 0. Frequency is the inverse cycle duration. Window for the\n    CL values is t < 0 within the trial (-1 to 0 s, open); clamped angle is the mean angle for t\n    from 0.2 to 1.8 s. Tolerances are the paper's SD. Reproduced when all four means fall within\n    tolerance under one set-point reading.\n- id: fig2i-ft-rt\n  statement: The choice period lasts 0.32 s, between the mean first whisker touch of the\n    approaching wall (0.06 ± 0.03 s) and the mean reaction time defined by the stereotypic hind-leg\n    push (0.38 ± 0.07 s).\n  source: Results, Behavioral correlates of decision-making..., paragraph 3; Fig. 2I\n  quote: Corresponding time histograms for FT and RT ( Fig. 2I ) indicate the choice period of 0.32\n    s between the mean FT (0.06 ± 0.03 s, mean ± SD) and mean RT (0.38 ± 0.07 s, mean ± SD)\n  expected:\n  - {quantity: mean first touch time, value: 0.06, tolerance: 0.03, unit: s}\n  - {quantity: mean reaction time, value: 0.38, tolerance: 0.07, unit: s}\n  - {quantity: choice period, value: 0.32, tolerance: 0.032, unit: s}\n  criterion: Animal of Fig. 2I, 573 per Table S1 (\"2EFI\"); OL_L trials. FT is the first\n    whisker-wall touch after t = 0 to the approaching wall (Fig. 2F; Fig. 3Q); touches of the\n    retracting wall in the first 11 ms (Fig. 3P) are excluded, reading (a), or not, reading (b).\n    RT is the time of the largest peak of the lateral acceleration after t = 0 (SI Fitting of\n    drift diffusion models), in the turn direction (positive for left turns, Fig. 2H). Open\n    details and readings. The signal, (c) the derivative of the run angle theta of Eq. 1, (d) the\n    derivative of the lateral velocity (the SI treats these as the same); the search window, (e)\n    0 to 1 s, (f) 0 to 1.8 s (the turn). Tolerances are the paper's SD for FT and RT, 10% for the\n    choice period (mean RT minus mean FT). Reproduced when all three match under one combination.\n    RT under the same readings is also reported for every ephys animal, for use by\n    fig4-ddm-fit.\n- id: fig2jk-glm-mixed-tuning\n  statement: During straight CL running, over 80% of units encode more than one behavioural or\n    sensory variable (whisking kinetics and kinematics, speed, gait), and the wall feedback signal\n    V_wall is among the strongest encoded variables.\n  source: Results, Stages of decision-making..., paragraph 2; Fig. 2J-K; SI Multiparameter GLM\n    regression\n  quote: In fact, multidimensional tuning is characteristic for the majority of population (over\n    80% of units, Fig. 2K ) ... Unsurprisingly, among the strongest correlations is the feedback\n    signal V wall\n  expected:\n  - {quantity: fraction of units encoding more than one variable, value: 0.8, tolerance: 0.08}\n  criterion: Animal 579 (Table S1, \"2JK\"). Poisson GLM with exponential link (SI Eq. 3), 13\n    regressors (whisking phase and amplitude from the Hilbert transform of the angle, set angle,\n    curvature and its derivative, forward, absolute and lateral speed, run angle and its derivative,\n    RH and LH leg push times) plus V_wall (Eq. 2); the same 3 s segment of 40 randomly chosen CL\n    trials (SI; the Fig. 2J legend says 55 trials, a reading); spikes in 20 ms bins smoothed with a\n    Savitzky-Golay filter; five-fold cross-validation with ridge regularisation; for each\n    variable, the log likelihood ratio of full against reduced model averaged over the five folds,\n    referred to a chi-squared distribution with 1 degree of freedom. Open details. The\n    Savitzky-Golay window and order, the ridge penalty, the regressor lags or bases, which 3 s\n    segment, and the significance threshold for \"encoding\" are not given; readings for the\n    threshold are p < 0.05 and p < 0.01, and for the penalty the values a five-fold\n    cross-validated search selects and no penalty. Reproduced when at least 72% of units encode at\n    least two variables and V_wall is among the three variables encoded by most units, under all\n    readings; when readings disagree the claim is blocked as methods_underspecified.\n- id: fig2-epoch2-at-first-touch\n  statement: The epoch 2 peaks appear within 10 ms of the first whisker touch, consistent with the\n    afferent delay from follicle to barrel cortex, which marks them as sensory (mismatch) signals.\n  source: Results, Stages of decision-making..., paragraph 3; Fig. 1N-O; Fig. 2F\n  quote: In all cases, epoch 2 peaks appear within 10 ms range from FT, which is consistent with the\n    expected afferent delay from whisker follicle to barrel cortex\n  expected:\n  - {quantity: delay from FT to epoch 2 peak, value: 0.0, tolerance: 0.01, unit: s}\n  criterion: Needs, in the same session, spikes and whisker touch times. Per ephys session with\n    whisker touch times, the population epoch 2 peak time (maximum bin from 0 to 0.065 s, OL_L and\n    OL_R) is compared with the mean FT of the same trials (FT as in fig2i-ft-rt, readings (a) and\n    (b)), and in a second reading, the peak of the population rate aligned to each trial's FT.\n    Reproduced when the absolute difference is at most 10 ms in every such session under a\n    reading. The header notes that the paper's own numbers (epoch 2 at 0.026 s, FT at 0.06 to 0.07\n    s) disagree with this; the notes give the difference either way.\n- id: fig2l-running-vs-sitting\n  statement: The epoch 4 ramp dominates the response only when the animal is actively running;\n    during brief stops with active whisking the epoch 2 peak dominates and the ramp is absent.\n  source: Results, Stages of decision-making..., paragraph 4; Fig. 2L\n  quote: peak 4 activity dominates the modulation only when the animal is actively navigating\n  criterion: OL_L trials split into sitting, the animal stopped for about 2 s with whisking\n    maintained (Fig. 2L legend, 20 trials), and running (96 trials). The animal is not named; the\n    session whose OL_L trials split into about 20 sitting and 96 running trials is used, and\n    otherwise every ephys animal with at least 10 sitting trials. Sitting is not defined;\n    readings (a) mean speed below 10 cm/s over -1 to 1 s (Table S1 defines running as above 10\n    cm/s); (b) mean speed below 10 cm/s over -2 to 0 s. Population-averaged rate (header). Epoch 2\n    size is the maximum from 0 to 0.065 s and epoch 4 size the maximum from 0.12 to 0.3 s, each\n    minus the epoch 1 mean (-1 to 0 s). Reproduced when, in running trials, epoch 4 exceeds epoch 2,\n    and in sitting trials epoch 2 exceeds epoch 4, in the named session or in most sessions used,\n    under either reading; when readings disagree the claim is blocked as methods_underspecified.\n- id: fig2m-dimensionality-collapse\n  statement: Population activity is high-dimensional during epoch 1 and collapses to a single\n    dimension after first touch during epochs 2 to 4, staying one-dimensional through the choice\n    period and rising again at decision execution and in epoch 5.\n  source: Results, Stages of decision-making..., paragraph 5; Fig. 2M; SI Dimensionality reduction\n  quote: confirms the high-dimensional neural coding during epoch 1 that collapses rapidly to just a\n    single dimension following the FT during epochs 2, 3, and 4 ... the neural population remains\n    one-dimensional ( 46 ) during choice period between FT and RT and starts to increase only at\n    the onset of decision execution and later, in epoch 5\n  criterion: Animal 489 (Table S1, \"2M\"), OL_L trials. As the SI Dimensionality reduction gives\n    it, spikes in 1 ms bins, smoothed with a 2 ms Gaussian kernel, units below 1 Hz removed, cut in\n    100 ms segments; for each segment, the matrix of trial-averaged rates (units by 1 ms time\n    points) is analysed by PCA and the number of components that explain 90% of the variance is\n    its dimensionality. Open details and readings. The kernel width as (a) SD of 2 ms or (b) FWHM\n    of 2 ms; the 1 Hz rate taken (c) over the whole session or (d) over the OL_L trial window;\n    PCA on time points as samples and units as variables, centred per unit (the standard method of\n    the cited references). Reproduced when, under all readings, dimensionality is 1 in every\n    segment from 0.1 to 0.3 s and greater than 1 in the epoch 1 segments (-1 to 0 s), and rises\n    above 1 in a segment after 0.4 s; when readings disagree the claim is blocked as\n    methods_underspecified.\n- id: fig3-wall-kinematics\n  statement: At turn onset the wall retracts to its maximum 12 mm distance within a mean of 11 ms,\n    so most (>80%) first touches are on the approaching wall; during the epoch 3 suppression the\n    wall approaches from 8.7 to 4.4 mm, and it reaches its final 2 mm position at 200 ms.\n  source: Results, Could the neural activity modulation be explained by simple sensory drive?,\n    paragraphs 2 and 3; Fig. 3A, 3P-Q\n  quote: The wall retracts very rapidly ( Fig. 3P ), reaching the maximum 12 mm distance at a mean\n    delay as fast as 11 ms. Therefore, the majority (>80%) of first whisker touch (FT) events (\n    Fig. 3Q ) correspond to whisker palpating approaching ... when the wall is not retracting but\n    fast approaching from 8.7 mm to 4.4 mm ... at a constant speed until the final position of 2\n    mm is reached at 200 ms\n  expected:\n  - {quantity: mean time of maximum wall distance, value: 0.011, tolerance: 0.0011, unit: s}\n  - {quantity: maximum wall distance, value: 12, tolerance: 1.2, unit: mm}\n  - {quantity: fraction of FT on the approaching wall, value: 0.8, tolerance: 0.08}\n  - {quantity: wall distance at 0.065 s, value: 8.7, tolerance: 0.87, unit: mm}\n  - {quantity: wall distance at 0.14 s, value: 4.4, tolerance: 0.44, unit: mm}\n  - {quantity: final wall distance, value: 2, tolerance: 0.2, unit: mm}\n  - {quantity: time final distance is reached, value: 0.2, tolerance: 0.02, unit: s}\n  criterion: Approaching-wall position in OL_L trials of the session of Fig. 3A and 3P (50 trials;\n    the animal is 589 for Fig. 3A and 489 for Fig. 3P per Table S1; both are used and reported).\n    Time of maximum distance per trial, then its mean. Wall distances at 0.065 and 0.14 s are the\n    mean trace at the ends of the epoch 3 window the Results give. FT on the approaching wall\n    means FT after the time of maximum distance in that trial. The fraction holds when above 0.72\n    (\">80%\" with a 10% margin). Reproduced when all values match in at least one of the two\n    sessions; the wall values are expected in all sessions and are reported for each.\n- id: fig3c-touch-statistics\n  statement: The whisker touches the wall about 48 ± 4% of the time, in touches of median duration\n    21 ms; touch probability increases during epoch 4, reaching 90% in epoch 5.\n  source: Results, Could the neural activity modulation be explained by simple sensory drive?,\n    paragraph 3; Fig. 3B-D, 3M-O\n  quote: The whisker stays in direct contact with the wall about 48 ± 4% of the time ( Fig. 3C )\n    with median touch duration of 21 ms ... Whisker touch probability ( Fig. 3C ) increases\n    monotonously during epoch 4, as does mean whisker curvature ( Fig. 3D ), reaching 90% in epoch\n    5\n  expected:\n  - {quantity: fraction of time in contact, value: 0.48, tolerance: 0.04}\n  - {quantity: median touch duration, value: 0.021, tolerance: 0.0021, unit: s}\n  - {quantity: touch probability in epoch 5, value: 0.9, tolerance: 0.09}\n  criterion: Animal 589 (Table S1, \"3ABCD\"), the 75 OL_L trials of Fig. 3B-C (which 75 is not said;\n    all OL_L trials with touch annotations are used, and the first 75 as a variant). Touch\n    probability is the fraction of trials in contact per 1 ms frame. The 48% is taken during\n    epochs 2 to 3 (0 to 0.14 s, where the paragraph places it; reading a) and over epochs 1 to 3\n    (reading b); the median duration over all touches in the trials (reading c) and in epochs 2 to\n    3 (Fig. 3N; reading d); epoch 5 is 0.3 to 1.8 s. The increase in epoch 4 holds when the touch\n    probability averaged over 0.2 to 0.3 s exceeds that over 0.12 to 0.2 s. Reproduced when all\n    hold under one reading.\n- id: fig3ijkl-whisking-across-epochs\n  statement: Across epochs 1, 2-3 and 4-5 the whisker palpates the wall at a constant 15 ± 2 Hz,\n    with statistically identical amplitudes, set angles and per-cycle curvature maxima.\n  source: Results, Could the neural activity modulation be explained by simple sensory drive?,\n    paragraph 3; Fig. 3I-L\n  quote: The whisker palpates the wall at a constant 15 ± 2 Hz frequency ( Fig. 3I ), with\n    statistically identical amplitudes ( Fig. 3J ), and set angles ( Fig. 3K ) ... producing\n    periodically modulated curvature with statistically identical maximum per each cycle ( Fig. 3L\n    )\n  statistics:\n  - about: whisking amplitude across epoch groups (Fig. 3J legend), a result that contradicts the\n      text\n    test: two-sample t test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 25 trials\n  - about: whisking set angle across epoch groups (Fig. 3K legend)\n    test: two-sample t test\n    p: 0.0001\n    p_relation: \"<\"\n    n: 25 trials\n  - about: per-cycle maximum curvature across epoch groups (Fig. 3L legend)\n    test: two-sample t test\n    p: 0.0001\n    p_relation: \"<\"\n  expected:\n  - {quantity: whisking frequency, value: 15, tolerance: 2, unit: Hz}\n  criterion: Animal 589 (Table S1, \"3G-P\"), 25 OL_L trials (Fig. 3I legend; which 25 is not said,\n    all tracked OL_L trials are used and the first 25 as a variant). Per whisk cycle (Hilbert\n    phase), frequency, amplitude, set angle (cycle mean angle) and maximum curvature, grouped\n    into epoch 1 (t < 0), epochs 2-3 (0 to 0.14 s) and epochs 4-5 (0.14 to 1.8 s). This is a\n    claim of absence judged on the paper's test: two-sample t tests between groups (each pair) at\n    p < 0.05. Reproduced when frequency stays within 15 ± 2 Hz in each group and no amplitude,\n    set angle or curvature comparison is significant; not reproduced when they are, which is what\n    the legends' P < 0.0001 report. The notes give each effect size and say whether the legends'\n    result is what was found.\n- id: fig3-not-sensory-drive\n  statement: While sensory input is monotonous during the turn (constant whisking, wall contact\n    rising steadily), neural activity is highly nonstationary (peak, suppression, ramp, return), so\n    the modulation is not explained by simple sensory drive.\n  source: Results, Could the neural activity modulation be explained by simple sensory drive?,\n    paragraph 3; Fig. 3\n  quote: However, while sensory input is monotonous, in stark contrast to the “simple sensory\n    drive” hypothesis, the neural activity is highly nonstationary\n  depends_on:\n  - fig1lm-staged-modulation\n  - fig3c-touch-statistics\n  - fig3ijkl-whisking-across-epochs\n  criterion: An interpretation resting on the claims it depends on. Reproduced when\n    fig1lm-staged-modulation is reproduced and, in fig3c-touch-statistics, touch probability does\n    not decrease from 0.065 to 0.3 s (mean per 10 ms bin is non-decreasing in its linear trend),\n    so that the epoch 3 drop and epoch 4 rise are not matched by a drop and rise of contact.\n    Whisking constancy (fig3ijkl-whisking-across-epochs) is reported, not required.\n- id: fig4-ddm-fit\n  statement: A classical drift-diffusion model fitted to the reaction-time distribution of animal\n    489 gives a nondecision time of 0.12 s, drift 2.91, bound 0.59 and noise 0.25 (BIC -664); a\n    generalized DDM with collapsing bounds and leak fits better (BIC -705), with normalized drift\n    K/B of 11.12.\n  source: Results, Ramping neural activity reflects temporal accumulation..., paragraph 1; Fig.\n    4B-E; SI Table S2\n  quote: Fitting classical DDM ( Materials and Methods ) to experimental distribution of RT ( Fig.\n    4B ) produces best fit (Bayesian information criterion, BIC of −664, Fig. 4C ) for nondecision\n    time (NDT) of 0.12 s ( Fig. 4D ), drift K = 2.91, bound B = 0.59 ( Fig. 4E ), and noise σ =\n    0.25 ... that produce a better fit (BIC of −705). Normalized drift K/B that defines the time\n    needed to reach the bound in absence of noise and decay is 11.12\n  expected:\n  - {quantity: DDM nondecision time, value: 0.12, tolerance: 0.012, unit: s}\n  - {quantity: DDM drift K, value: 2.91, tolerance: 0.291}\n  - {quantity: DDM bound B, value: 0.59, tolerance: 0.059}\n  - {quantity: DDM noise sigma, value: 0.25, tolerance: 0.025}\n  - {quantity: DDM BIC, value: -664, tolerance: 66.4}\n  - {quantity: GDDM BIC, value: -705, tolerance: 70.5}\n  - {quantity: normalized drift K/B, value: 11.12, tolerance: 1.112}\n  depends_on:\n  - fig2i-ft-rt\n  criterion: Animal 489 (Fig. 4B; Table S2), OL_L trials, RT as in fig2i-ft-rt, correct and error\n    trials as in fig2a-success-rate, fitted with PyDDM (SI Fitting of drift diffusion models).\n    Models as the Results describe them. DDM, constant drift K, constant bounds at ±B, noise\n    sigma, nondecision time; full DDM, adding uniform variability of the starting point X0 and of\n    the nondecision time; GDDM, the DDM with exponentially collapsing bounds and a leaky\n    integrator. Open details. Table S2's parameter list could not be read here, and the paper does\n    not say which parameters were free, the fitting loss, the time step or the RT window. Readings\n    (a) sigma free with K, B and NDT (as the reported sigma = 0.25 implies), PyDDM's default\n    likelihood loss; (b) sigma fixed at 0.25 and the rest free. The RT readings of fig2i-ft-rt are\n    carried. The K/B value is taken from the GDDM under reading (c), from the DDM under reading\n    (d) (the header notes the reported DDM values give 4.93). Reproduced when NDT is within 10% of\n    0.12 s and the GDDM BIC is lower than the DDM BIC under some reading, and each other value is\n    reported against its tolerance; partially reproduced when only one of these two holds.\n- id: fig4b-ddm-matches-ramp\n  statement: The DDM nondecision time (0.12 s) matches the 0.12 s onset of the epoch 4 ramp, and\n    the normalized drift (11.12) is close to the ramp's slope (12.25), so the ramp is consistent\n    with accumulation of evidence to a bound.\n  source: Results, Ramping neural activity reflects temporal accumulation..., paragraphs 1 and 2;\n    Fig. 4B\n  quote: appreciable NDT = 0.12 s from both DDM and full DDM ( Fig. 4D ) fits well to the 0.12 s\n    delay of experimentally observed ramping onset at end of epoch 3 for this example animal\n  expected:\n  - {quantity: ramp onset, value: 0.12, tolerance: 0.012, unit: s}\n  depends_on:\n  - fig4-ddm-fit\n  - fig1n-ramp-slope\n  criterion: Animal 489. Ramp onset is the end of the epoch 3 suppression in the OL_L\n    population-averaged rate; it is not defined further, readings (a) the time of the minimum\n    between 0.065 s and the epoch 4 maximum; (b) the last bin before the epoch 4 maximum at or below\n    the epoch 3 minimum plus 10% of the range between them. Reproduced when the ramp onset and the\n    DDM nondecision time from fig4-ddm-fit both lie within 0.012 s of 0.12 s and the fitted K/B lies\n    within the 10% tolerance of the ramp slope of fig1n-ramp-slope under the normalised reading;\n    partially reproduced when only the timing agrees.\n- id: fig5e-slope-across-animals\n  statement: Across seven animals, the epoch 4 ramp slope is 13.05 ± 4.59 (mean ± SD).\n  source: Results, Ramping neural activity reflects temporal accumulation..., paragraph 2; Fig. 5E;\n    Fig. S9\n  quote: (other examples in SI Appendix , Fig. S9 and Fig. 5E below, n = 7, 13.05 ± 4.59, mean ± SD)\n  expected:\n  - {quantity: mean ramp slope over animals, value: 13.05, tolerance: 4.59}\n  depends_on:\n  - fig1n-ramp-slope\n  criterion: The seven animals of Fig. 5C-E (480, 489, 503, 528 in C2; 482, 517, 530 in\n    neighbouring barrels; Table S1), OL_L trials, slope per animal under the readings of\n    fig1n-ramp-slope, with the fit window per animal from its own ramp onset (readings of\n    fig4b-ddm-matches-ramp) to (a) its onset plus 0.05 s, (b) plus 0.06 s, (c) its epoch 4 maximum\n    (the windows of 489 carried over by duration; the paper gives no per-animal rule). Fig. 5 uses\n    normalised rates (SI Spike rates), so the normalised reading is the main one. Tolerance is the\n    paper's SD. Reproduced when the mean lies within it under some reading.\n- id: fig4f-varce-example-unit\n  statement: For an example high-rate unit (489101), the Fano factor is 0.74 ± 0.04 in epochs 1 and\n    2 and drops to 0.29 at the epoch 4 peak (t = 0.23 s) as total variance saturates, and its VarCE\n    rises quickly at the start of epoch 4 (0.12 to 0.17 s).\n  source: Results, Ramping neural activity reflects temporal accumulation..., paragraph 3; Fig. 4F;\n    SI Analysis of VarCE, paragraph 2; Fig. S10A\n  quote: results in a Fano factor (Fig.S10A, top, black) of 0.74±0.04 (mean ± s.d.). Total variance\n    saturates midway through a strong increase of mean firing rate during ramping that results in a\n    Fano factor dropping down to 0.29 at the peak of epoch 4 at t=0.23s\n  expected:\n  - {quantity: Fano factor in epochs 1 and 2, value: 0.74, tolerance: 0.04}\n  - {quantity: minimum Fano factor, value: 0.29, tolerance: 0.029}\n  - {quantity: time of the Fano minimum, value: 0.23, tolerance: 0.023, unit: s}\n  criterion: Unit 489101 of animal 489, 266 OL_L trials, spike counts in 10 ms bins (SI Analysis of\n    VarCE). Fano factor per bin is variance over mean across trials. The epochs 1 and 2 value is\n    the mean ± SD over bins from -1 to 0.065 s (window open; reading -0.5 to 0.065 s also shown).\n    VarCE = variance minus phi times mean, phi the lowest Fano factor in the trial (SI Eq. 4).\n    Reproduced when the three values match and VarCE averaged over 0.15 to 0.17 s exceeds that\n    over 0.10 to 0.12 s. If the dataset's unit identifiers do not include 489101, the unit is the\n    highest-rate RS unit in L5A or L5B of animal 489 (the paper's description, \"an outlier with\n    the highest spiking rate\"), and the notes say so.\n- id: fig4g-varce-population\n  statement: Population VarCE increases linearly between decision onset (0.12 s) and decision\n    termination (0.18 s), whether computed over all units, without outliers, or on residuals, and\n    then declines to a minimum at t = 0.23 s when the decision is executed.\n  source: Results, Ramping neural activity reflects temporal accumulation..., paragraph 3; Fig.\n    4G-I; SI Analysis of VarCE\n  quote: When VarCE is calculated from residuals ( 5 , 51 ) ( Materials and Methods ), it is similar\n    ( Fig. 4G , black) showing linear increase between decision onset ( Fig. 4G , up arrow) and\n    decision termination ( Fig. 4G , down arrow) times. VarCE exhibits a fast decline at decision\n    end, reaching minimum at t = 0.23 when the decision is executed\n  expected:\n  - {quantity: time of the VarCE minimum after the ramp, value: 0.23, tolerance: 0.023, unit: s}\n  criterion: Animal 489, 266 OL_L trials, 10 ms bins, per-unit VarCE with phi the unit's lowest\n    Fano factor that keeps VarCE positive in the choice period (SI Eq. 4). Population VarCE is the\n    \"union\" of unit VarCEs (SI); readings (a) sum over units, (b) mean over units. Three versions\n    as the SI gives them; all units; without the four outliers of Fig. 4I (the four units with the\n    largest summed VarCE over the choice period, taken as 0.06 to 0.38 s, mean FT to mean RT of\n    fig2i-ft-rt); and on residuals (each unit's per-bin trial mean subtracted from its counts).\n    Reproduced when, in all three versions under a reading, the linear regression of VarCE on time\n    over 0.12 to 0.18 s has a positive slope with p < 0.05 and the VarCE minimum between 0.18 and\n    0.4 s lies within 0.023 s of 0.23 s; partially reproduced when the increase holds in all three\n    but the minimum's time does not.\n- id: fig4j-corce\n  statement: The CorCE matrix, computed on residuals, shows correlation rising with time along the\n    diagonal and decaying with time lag along a row, a pattern that disappears when bins are\n    shuffled, as expected for a diffusion process.\n  source: Results, Ramping neural activity reflects temporal accumulation..., paragraph 4; Fig. 4J;\n    Fig. S10C\n  quote: The calculated ( Materials and Methods ) CorCE matrix ( Fig. 4J ) indeed exhibits\n    characteristic increase of correlation as a function of time and, for given time (e.g., along\n    the top row), shows sequential decay as often observed ( 5 , 51 ) during decision-making. This\n    correlation disappears when bins are randomly shuffled\n  criterion: Animal 489, OL_L trials, residual spike counts in 10 ms bins (SI Analysis of VarCE and\n    CorCE, SI Eq. 6), covariance of conditional expectation across bins with VarCE on the\n    diagonal, normalised to correlation. The bins of the matrix are not given; readings (a) 0.12 to\n    0.18 s (the ramp's VarCE window); (b) 0.06 to 0.38 s (the choice period, mean FT to mean RT).\n    How units are combined is not given; readings (c) residuals summed over units per trial; (d)\n    per-unit matrices averaged. Reproduced when, under a reading, the diagonal's linear trend is\n    positive, the top row's correlation decreases with lag (negative Spearman correlation), and in\n    100 shuffles of bin order within trials (seeded) the top-row trend is gone (shuffled mean\n    Spearman within ±0.2 of zero).\n- id: fig4k-streak-index\n  statement: Trial-by-trial streak index analysis during ramping shows random local spike count\n    fluctuations with close to zero mean (0.06 ± 1.36, mean ± SD), indicating a gradual, not\n    step-like, transition in each trial.\n  source: Results, Ramping neural activity reflects temporal accumulation..., paragraph 4; Fig. 4K;\n    SI Streak Index analysis\n  quote: showed randomness of local spike count fluctuations with close to zero mean (0.06 ± 1.36,\n    mean ± SD, Fig. 4K ), indicated gradual\n  expected:\n  - {quantity: mean streak index, value: 0.06, tolerance: 1.36}\n  - {quantity: SD of streak index, value: 1.36, tolerance: 0.136}\n  criterion: Animal 489, OL_L trials. The SI gives 8 successive 5 ms bins, counts compared with the\n    across-trial median per bin, 1 above and 0 below, and the number of 0-1 switches per trial.\n    Open details and readings. The statistic, (a) the switch count as the SI describes it, which\n    cannot have a mean near zero; (b) the z-scored runs statistic of the cited methods (observed\n    number of runs minus its expectation under randomness, over its SD, Wald-Wolfowitz). Placement\n    of the 40 ms window during the ramp, (c) 0.12 to 0.16 s; (d) 0.14 to 0.18 s. Counts, (e) all\n    units summed per trial (\"from all layers combined\", SI); (f) per unit and trial (\"all units\n    across all trials\", Fig. 4K legend). Ties with the median, (g) assigned 0; (h) bins at the\n    median left out. Reproduced when mean and SD match under some reading; the notes say which.\n- id: fig5b-epochs-in-subpopulations\n  statement: All epochs, including the suppression and ramp of epochs 3 and 4, are present in layer\n    4 FS and RS units and in the units of every cortical layer and of each cell class, so the\n    modulation is not confined to a subpopulation.\n  source: Discussion, paragraph 3; Fig. 5B\n  quote: All epochs including epochs 3 and 4 are already present in thalamo-recipient Layer 4\n    populations of fast spiking (FS, putative inhibitory, Fig. 5 B , Top ) and regular spiking (RS,\n    putative excitatory, Fig. 5 B , Top ) units. They also dominate the activity in subpopulations\n    of all units across different cortical laminae\n  expected:\n  - {quantity: L2/3 units, value: 10, tolerance: 0}\n  - {quantity: L4 units, value: 13, tolerance: 0}\n  - {quantity: L5A units, value: 13, tolerance: 0}\n  - {quantity: L5B units, value: 16, tolerance: 0}\n  - {quantity: L6 units, value: 13, tolerance: 0}\n  - {quantity: FS units, value: 43, tolerance: 0}\n  - {quantity: RS units, value: 22, tolerance: 0}\n  criterion: Animal 489, OL_L trials, normalised population rate (SI Spike rates) of each\n    subpopulation; layers and FS/RS (waveform duration threshold 0.4 ms, SI) as the dataset\n    labels them, and FS/RS recomputed from waveform duration when durations are available. In each\n    subpopulation (L4 FS, L4 RS, each layer, all FS, all RS), the epoch sequence of\n    fig1lm-staged-modulation is tested on that subpopulation's units. Reproduced when the\n    sequence holds in L4 FS and L4 RS and in at least 6 of the 7 others; the counts are reported\n    against the legend's.\n- id: fig5cd-other-animals\n  statement: Similar synchronous modulation epochs are seen in the other animals recorded in the C2\n    principal column (n = 4) and in animals recorded in neighbouring barrel columns of the same or\n    a different row (n = 3).\n  source: Discussion, paragraphs 3 and 4; Fig. 5C-D; Fig. S4\n  quote: Similar synchronous modulation is observed for other animals (n = 4, Fig. 5C ) with\n    recordings from principal barrel column ... similar characteristic modulation epochs were\n    observed in animals where recordings were done in a neighboring barrel column in the same or\n    even a different row (n = 3, Fig. 5D )\n  depends_on:\n  - fig1lm-staged-modulation\n  criterion: Animals 480, 489, 503, 528 (C2) and 482 (B2), 517 (C3), 530 (C1), per Table S1 and\n    Fig. S4, OL_L and OL_R trials; the test of fig1lm-staged-modulation applied per animal.\n    Reproduced when it holds in at least 3 of the 4 principal and 2 of the 3 neighbouring\n    animals; partially reproduced when it holds in at least half of each group.\n- id: fig5e-principal-vs-neighbor\n  statement: The delay of the epoch 2 peak, the delay of ramp onset at the end of epoch 3, and the\n    ramp slope do not differ between recordings in the principal C2 column (n = 4) and in\n    neighbouring columns (n = 3).\n  source: Discussion, paragraph 4; Fig. 5E\n  quote: delay of epoch 2 ( Fig. 5 E , Left ), start of ramping at end of epoch 3 ( Fig. 5 E ,\n    Middle ) and the linear slope of ramping activity in epoch 4 ( Fig. 5 E , Right ) shows no\n    statistically significant difference (two-sample t test, P > 0.05) between principal C2\n    whisker and neighboring barrel columns\n  statistics:\n  - about: epoch 2 delay, principal against neighbouring columns\n    test: two-sample t test\n    p: 0.109\n    n: 4 principal and 3 neighbouring animals\n  - about: ramp onset delay, principal against neighbouring columns\n    test: two-sample t test\n    p: 0.14\n    n: 4 principal and 3 neighbouring animals\n  - about: ramp slope, principal against neighbouring columns\n    test: two-sample t test\n    p: 0.97\n    n: 4 principal and 3 neighbouring animals\n  depends_on:\n  - fig5e-slope-across-animals\n  criterion: Animals as in fig5cd-other-animals, OL_L trials, normalised population rate. Per\n    animal, epoch 2 delay is the time of the maximum bin from 0 to 0.065 s; ramp onset delay\n    under the readings of fig4b-ddm-matches-ramp; slope under the readings of\n    fig5e-slope-across-animals. A claim of absence on the paper's test. Reproduced when a\n    two-sample t test (equal variances, the default reading of \"two-sample t test\") of the 4\n    against the 3 per-animal values gives p > 0.05 for all three measures; not reproduced when any\n    gives p < 0.05. The group means, their difference and Welch's test as a variant are reported.\n    When the measure readings give different outcomes the claim is blocked as\n    methods_underspecified.\n"
}
```

```
File created successfully at: claims/001341/10.1073-pnas.2514107123.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/001341/10.1073-pnas.2514107123.yaml paper/10.1073-pnas.2514107123.txt; grep -nE '—|\brather\b' claims/001341/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -nE '^\s+[^#{]*\S: ' claims/001341/*.yaml | grep -vE '^\S+:\s+(- )?[a-z_]+: ' | head; grep -nE '^\s{4,}\S.*: ' claims/001341/*.yaml | grep -v '{quantity' | head
```

```
554:    claim of absence judged on the paper's test: two-sample t tests between groups (each pair) at
535:    test: two-sample t test
536:    p: 0.0001
537:    p_relation: "<"
538:    n: 25 trials
540:    test: two-sample t test
541:    p: 0.0001
542:    p_relation: "<"
543:    n: 25 trials
545:    test: two-sample t test
546:    p: 0.0001
```

**Agent calls Bash**

```bash
cd  sed -i "554s/the paper's test: two-sample/the paper's test, two-sample/" claims/001341/10.1073-pnas.2514107123.yaml; python tools/claims_check.py claims/001341/10.1073-pnas.2514107123.yaml paper/10.1073-pnas.2514107123.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml;d=yaml.safe_load(open('claims/001341/10.1073-pnas.2514107123.yaml'))
for c in d['claims']:
  for e in (c.get('expected') or []): 
    if set(e)-{'quantity','value','tolerance','unit'} or not isinstance(e['value'],(int,float)): print(c['id'],e)
print(sum('criterion' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('expected' in c for c in d['claims']))
"; grep -c '' claims/001341/*.yaml
```

```
32 2 22
800
```

**Agent**

I wrote `claims/001341/10.1073-pnas.2514107123.yaml`, and the quote checker passes it: 32 claims, 31 quotes, 6 statistical values, 0 problems. Nothing is committed.

**Text read**
- The version of record as the PubMed Central author manuscript (NIHMS2207436, PMC13142948), with its SI Appendix: Figs S1–S12, Table S1 and the SI Methods and Data Analysis. The main text's Methods only points to the SI, so the methods come from the SI.
- The paper's title is "Neural correlates of perceptual decision-making in the primary somatosensory cortex". The title in the task is the dataset's title.
- I searched the bioRxiv preprint (v1) for extra method details. It has none, and no claim rests on it.
- The paper links no analysis code of its own, only third-party tools (Kilosort 3, ecephys, Phy, the Pillow lab GLM tutorial, PyDDM, SLEAP). I read none of them, and no method detail is settled by code.

**Counts**
- 32 claims: 31 have quotes, and one (`table-s1-recordings`, the per-animal unit and trial counts) is marked `inferred`.
- 22 have expected values.
- 2 have statistics, 6 entries in all: the Fig. 5E two-sample t tests (p = 0.109, 0.140, 0.970) and the Fig. 3J–L legend tests (p < 0.0001).
- All 32 have criteria. Every claim uses the dataset's own data; there are no outside inputs.

**Details the paper leaves open, and the readings named**
- **Ramp slope (12.25):** the units could be min-max normalised rate per second or Hz per second. The fit window could be 0.12–0.17 s, 0.12–0.18 s, or from ramp onset to the peak at 0.25 s. The normalisation range is also open.
- **Ramp onset:** either the minimum of the epoch 3 dip, or a rise of 10% of the range above it. The second reading is mine; the paper only says "end of epoch 3".
- **Epoch 1 baseline window:** −0.5 to 0 s or −1 to 0 s. No smoothing is named, so the main reading is unsmoothed 5 ms bins.
- **Success at "±1 cm clearance":** either displacement in the turn direction or absolute displacement. Which of animal 503's trials make up the "414" is not said: all of its OL turn trials, or the first 414.
- **Running speed of 21 ± 4 cm/s:** animal 503's session (all samples, or running only), or the mean over animals in Table S1.
- **Lateral distance:** its reference point is open, and so is which animal each of the 2.30 and 1.49 SD values belongs to.
- **Reaction time:** run-angle derivative or lateral-velocity derivative, searched over 0–1 s or 0–1.8 s. First touch is counted with or without touches of the retracting wall.
- **Turn angle:** the mean of θ over the turn, or the displacement angle at t = 1 s.
- **Whisking set point:** the mean angle per whisk cycle, or the mean angle before t = 0.
- **GLM:** the significance threshold (p < 0.05 or 0.01), ridge penalty, Savitzky-Golay settings, lags and segment are not given, and the trial count is 40 in the SI against 55 in the legend.
- **Dimensionality:** whether the 2 ms kernel is an SD or a FWHM, and over what period the 1 Hz rate cut is taken.
- **DDM:** which parameters were free (σ free or fixed), and whether K/B is taken from the GDDM or the DDM.
- **VarCE and CorCE:** whether units are summed or averaged, and which bins the CorCE matrix covers.
- **Streak index:** a raw switch count (the SI's description) or a z-scored runs statistic. Also open: where the 40 ms window sits, whether counts are summed over units or kept per unit, and how ties with the median are handled.
- **Fig. 2L:** which animal is shown, and how "sitting" is defined.
- **Jitter of 30 ms:** not defined. I named two readings, and it is reported but does not decide the claim's outcome.
- **Claims with no test in the paper:** for psychometric trend, lateralisation, staged modulation and similar claims, the windows come from the paper but the judging test was chosen in the file, and the criterion says so.

**Missing from the paper, or self-contradictory**
- **Tables S2 and S3 (fitted DDM parameters) could not be read.** They are images with no extracted text, and no PDF renderer was available in this run. Only the values the main text repeats are used.
- **Paper inconsistencies,** listed in the file's header comment:
  - Unit totals: 634 in the SI against 668 in Table S1. The difference is animal 579.
  - Trial counts differ between figures for animals 489 and 503.
  - Unit 489101 is given as layer 5A in one figure and 5B in another.
  - The number of animals for Fig. 2C–D is given as 5, 7, or 4.
  - The reported drift and bound give K/B = 4.93, while the text gives 11.12.
  - The text calls the whisking parameters "statistically identical", while the legends of Fig. 3J–L report p < 0.0001.
  - Epoch 2 peaks at 0.026 s, while first touch is at 0.06–0.07 s, yet the text says the two are within 10 ms.
  - The streak index's mean of 0.06 is impossible for a switch count.

## End of run

23 turns, 8 minutes, result: success.
