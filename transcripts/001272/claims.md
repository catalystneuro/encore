# 001272 · claims · run 39759919845

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/001453/ claims/001272/ 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat claims/001453/*.yaml | head -150; wc -c paper/*.txt; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/3647bcc6-dda4-485a-a147-47bb46f1dcbb/tool-results/b41eg2t0o.txt",
 "limit": 200
}
```

```
File content (30115 tokens) exceeds maximum allowed tokens (25000). Use offset and limit parameters to read specific portions of the file, or search for specific content instead of reading the whole file.
```

**Agent calls Bash**

```bash
wc -c paper/*.txt; cat paper/*.txt | head -c 60000
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && fold -s -w 200 paper/*.txt > p.txt; wc -l p.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1,260p $TMPDIR/p.txt
```

```
<persisted-output>
Output too large (49.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/3647bcc6-dda4-485a-a147-47bb46f1dcbb/tool-results/b55wav5p3.txt

Preview (first 2KB):
DOI: 10.1016/j.xcrp.2025.102660
Version: as served by europe_pmc
Source: europe_pmc+crossref (paper-text-fetcher)
Stored: 2026-10-20
Extracted: as fetched; with 1 supplement file(s) from the PMC Open Access cloud data (PMC12320893), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
------------------------------------------------------------------------
319 nihpa Cell reports. Physical science Cell Rep Phys Sci PMC12320893 12320893 12320893 NIHMS2098259 40762005 10.1016/j.xcrp.2025.102660 Excitation and polarization of isolated neurons by 
high-frequency sine waves for temporal interference stimulation Semenov Iurii 1 Kim Vitalii 1 2 Silkuniene Giedre 1 Pakhomov Andrei G 1 3 4 * 1 Frank Reidy Research Center for Bioelectrics, Old 
Dominion University, Norfolk, VA 23508, USA 2 Present address: Department of Chemical and Biomolecular Engineering, University of California, Irvine, Irvine, CA 92697, USA 3 Senior author 4 Lead 
contact * Correspondence: [removed: an e-mail address] AUTHOR CONTRIBUTIONS Conceptualization, A.G.P.; methodology, V.K., I.S., and A.G.P.; investigation, V.K., I.S., and A.G.P.; dosimetry, V.K. and G.S.; data 
processing, V.K., I.S., G.S., and A.G.P.; writing – original draft, A.G.P.; writing – review & editing, V.K., I.S., G.S., and A.G.P.; funding acquisition, A.G.P.; supervision, A.G.P. 16 6 2025 6 7 
102660 102660 4 8 2025 This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ). The publisher's version of this article is available at Cell Rep Phys 
Sci SUMMARY The capacity of temporal interference (TI) stimulation to target deep brain regions without affecting nearby surface electrodes remains uncertain. Using artifact-free optical recording,
[... 3 more lines not kept]
```

**Agent**

I'll read the paper text in chunks with the Read tool.

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/3647bcc6-dda4-485a-a147-47bb46f1dcbb/tool-results/b55wav5p3.txt",
 "limit": 130
}
```

```
1	DOI: 10.1016/j.xcrp.2025.102660
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 1 supplement file(s) from the PMC Open Access cloud data (PMC12320893), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	319 nihpa Cell reports. Physical science Cell Rep Phys Sci PMC12320893 12320893 12320893 NIHMS2098259 40762005 10.1016/j.xcrp.2025.102660 Excitation and polarization of isolated neurons by 
8	high-frequency sine waves for temporal interference stimulation Semenov Iurii 1 Kim Vitalii 1 2 Silkuniene Giedre 1 Pakhomov Andrei G 1 3 4 * 1 Frank Reidy Research Center for Bioelectrics, Old 
9	Dominion University, Norfolk, VA 23508, USA 2 Present address: Department of Chemical and Biomolecular Engineering, University of California, Irvine, Irvine, CA 92697, USA 3 Senior author 4 Lead 
10	contact * Correspondence: [removed: an e-mail address] AUTHOR CONTRIBUTIONS Conceptualization, A.G.P.; methodology, V.K., I.S., and A.G.P.; investigation, V.K., I.S., and A.G.P.; dosimetry, V.K. and G.S.; data 
11	processing, V.K., I.S., G.S., and A.G.P.; writing – original draft, A.G.P.; writing – review & editing, V.K., I.S., G.S., and A.G.P.; funding acquisition, A.G.P.; supervision, A.G.P. 16 6 2025 6 7 
12	102660 102660 4 8 2025 This is an open access article under the CC BY license ( http://creativecommons.org/licenses/by/4.0/ ). The publisher's version of this article is available at Cell Rep Phys 
13	Sci SUMMARY The capacity of temporal interference (TI) stimulation to target deep brain regions without affecting nearby surface electrodes remains uncertain. Using artifact-free optical recording, 
14	we compare excitation patterns and thresholds in hippocampal neurons stimulated by “pure” and amplitude-modulated sine waves, representing TI waveforms near electrodes and at the target, 
15	respectively. We sho
[... 115 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/3647bcc6-dda4-485a-a147-47bb46f1dcbb/tool-results/b55wav5p3.txt",
 "offset": 130,
 "limit": 131
}
```

```
130	activated. With sine wave stimuli, the poles keep charging to the opposite potentials in alternation. The induced transmembrane potential (TMP) is determined by the electric field strength and 
131	duration, as well as by the charging rate time constant. A large time constant would slow down charging and impede excitation by high-frequency sinusoids. Time constants of charging by external 
132	electric fields (also called “cellular time constants”) are orders of magnitude smaller than those in response to intracellular current injection. 37 For spherical cells, they can be calculated from 
133	intra- and extracellular conductivities, specific membrane capacitance, and cell radius. 42 , 44 However, for randomly shaped cells like neurons, analytical solutions are too complicated. We employed 
134	pulsed laser strobe microscopy 45 , 46 to measure the kinetics of membrane charging and its dependence on neuron shape and alignment with the electric field. A 2-μs square pulse was applied in 
135	synchrony with 6-ns laser flashes to capture images of a FluoVolt-loaded cell at intervals from 1 μs before the pulse to 6 μs after it in 50-ns steps. The electric field strength was set at 140 V/cm, 
136	which is 10-fold below the AP threshold for 2-μs pulses. 35 Changes in FluoVolt emission were quantified in cell regions most de- and hyperpolarized by the pulse ( Figures 4A - 4C ), and the data 
137	from eight replicates (1,440 images per experiment) were fitted with exponential functions to determine the time constants. The experiment was repeated the same way after repositioning the electrodes 
138	to apply the electric field in the orthogonal direction. Figure 4. Membrane polarization by 2-μs pulses and the kinetics of charging and relaxation (A–C) Membrane polarization in elongated, round, 
139	and triangular neurons exposed to 2-μs, 140 V/cm rectangular pulses. Two pairs of images show the same neuron exposed to the electric field from two orthogonal directions (arrows)
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 260,1007p $TMPDIR/p.txt | head -c 45000
```

```
<persisted-output>
Output too large (43.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/3647bcc6-dda4-485a-a147-47bb46f1dcbb/tool-results/b00ebubp5.txt

Preview (first 2KB):
experiments were performed in a standard physiological solution containing (in mM) 140 NaCl, 5.4 KCl, 2 CaCl 2 , 1.5 MgCl 2 , 10 HEPES, and 10 glucose (pH 7.2–7.3, 300–310 mOsm/kg, 16.4 mS/cm). The 
experiments presented in Figure 3 were performed in the same solution modified to have a lower conductivity of 8.4 mS/cm by replacing NaCl with NaGlu. The chemicals were purchased from Thermo Fisher 
Scientific (Waltham, MA) and Sigma-Aldrich (St. Louis, MO), except for tetrodotoxin (Tocris, Bristol, UK). A FluoVolt Membrane Potential Kit was purchased from Thermo Fisher Scientific. The dye and 
the PowerLoad concentrate (part of the kit) were added at 1:1,000× and 1:100×, respectively, to either the standard or low-conductivity physiological solution. Cells were loaded with the dye by 
incubation in this solution for 15–30 min, rinsed, and left in the dye-free solution. In one set of experiments ( Figure S1 ), neurons were loaded with 5 μM Di-8-ANEPPS dye (Thermo Fisher Scientific) 
for 30 min in the dark. Fluorescence images were taken with a TRITC filter cube. Changing the cell membrane potential shifted the dye emission spectrum in such a way that depolarization resulted in 
the reduced signal, so the vertical scale in Figure S2 has been inverted to present APs in a conventional manner, facing upward. The time-lapse imaging of the membrane potential was described 
previously. 35 After dye loading, the coverslips with neurons were placed in a 50-mm glass-bottom culture dish (MatTek, Ashland, MA) on a stage of an IX71 inverted microscope (Olympus America, Center 
Valley, PA). The dye was excited with a pE-340 fura illuminator (CoolLED, Andover, UK) using a FITC fluorescence cube and a PlanApo N 60, 1.42 NA objective (Olympus). 
[... 3 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/3647bcc6-dda4-485a-a147-47bb46f1dcbb/tool-results/b00ebubp5.txt",
 "limit": 120
}
```

```
1	experiments were performed in a standard physiological solution containing (in mM) 140 NaCl, 5.4 KCl, 2 CaCl 2 , 1.5 MgCl 2 , 10 HEPES, and 10 glucose (pH 7.2–7.3, 300–310 mOsm/kg, 16.4 mS/cm). The 
2	experiments presented in Figure 3 were performed in the same solution modified to have a lower conductivity of 8.4 mS/cm by replacing NaCl with NaGlu. The chemicals were purchased from Thermo Fisher 
3	Scientific (Waltham, MA) and Sigma-Aldrich (St. Louis, MO), except for tetrodotoxin (Tocris, Bristol, UK). A FluoVolt Membrane Potential Kit was purchased from Thermo Fisher Scientific. The dye and 
4	the PowerLoad concentrate (part of the kit) were added at 1:1,000× and 1:100×, respectively, to either the standard or low-conductivity physiological solution. Cells were loaded with the dye by 
5	incubation in this solution for 15–30 min, rinsed, and left in the dye-free solution. In one set of experiments ( Figure S1 ), neurons were loaded with 5 μM Di-8-ANEPPS dye (Thermo Fisher Scientific) 
6	for 30 min in the dark. Fluorescence images were taken with a TRITC filter cube. Changing the cell membrane potential shifted the dye emission spectrum in such a way that depolarization resulted in 
7	the reduced signal, so the vertical scale in Figure S2 has been inverted to present APs in a conventional manner, facing upward. The time-lapse imaging of the membrane potential was described 
8	previously. 35 After dye loading, the coverslips with neurons were placed in a 50-mm glass-bottom culture dish (MatTek, Ashland, MA) on a stage of an IX71 inverted microscope (Olympus America, Center 
9	Valley, PA). The dye was excited with a pE-340 fura illuminator (CoolLED, Andover, UK) using a FITC fluorescence cube and a PlanApo N 60, 1.42 NA objective (Olympus). Images were captured with an 
10	iXon Ultra 897 charge-coupled device (CCD) camera with a Solis interface (Andor Technology, Belfast, UK). The camera sensor outside the area of interest was physically shielded with an Optomask 

[... 110 more lines not kept]
```

**Agent**

Now the supplement text.

**Agent calls Bash**

```bash
grep -n -i "supplement\|Figure S1\b\|Table S1" $TMPDIR/p.txt | tail -20; grep -n "SUPPLEMENT\|Supplemental\|=====\|-----" $TMPDIR/p.txt
```

```
5:Extracted: as fetched; with 1 supplement file(s) from the PMC Open Access cloud data (PMC12320893), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
121:neurons using different electric field strengths tested in a random sequence. A typical experiment is illustrated in Figure S1 . Compared to FluoVolt recordings, the traces were expectedly noisier 
259:approximately 1 week before the experiments. Half of the medium was changed every 3 days during incubation. See Table S1 for more details. Recording of the optical APs and data analyses All 
264:incubation in this solution for 15–30 min, rinsed, and left in the dye-free solution. In one set of experiments ( Figure S1 ), neurons were loaded with 5 μM Di-8-ANEPPS dye (Thermo Fisher Scientific) 
335:protocols were followed but the signal amplitude was set to zero) and vehicle controls in experiments with tetrodotoxin. Supplementary Material 1 Supplemental information can be found online at 
431:12, 1763. 10.1038/s41598-022-04868-x. Associated Data Supplementary Materials 1
805:##### Supplement: NIHMS2098259-supplement-1.pdf
809:Supplemental information 
819:Figure S1, related to Figure 1. Excitation and inhibition of firing in a neuron loaded with Di-8-ANEPPS 
931:Table S1: Key Resource Table 
6:------------------------------------------------------------------------
335:protocols were followed but the signal amplitude was set to zero) and vehicle controls in experiments with tetrodotoxin. Supplementary Material 1 Supplemental information can be found online at 
809:Supplemental information
```

**Agent calls Bash**

```bash
sed -n 805,1007p $TMPDIR/p.txt
```

```
##### Supplement: NIHMS2098259-supplement-1.pdf

=== page 1 ===
Cell Reports Physical Science, Volume 6 
Supplemental information 
Excitation and polarization of isolated neurons 
by high-frequency sine waves 
for temporal interference stimulation 
Iurii Semenov, Vitalii Kim, Giedre Silkuniene, and Andrei G. Pakhomov 

=== page 2 ===
 
 
 
Figure S1, related to Figure 1. Excitation and inhibition of firing in a neuron loaded with Di-8-ANEPPS 
potentiometric dye. The cell was stimulated by 250-ms-long, 2-kHz sine waves at different field strengths 
(V/cm). Depolarization reduces the emission of Di-8-ANEPPS, so the optical membrane potential traces 
have been inverted to display depolarizions upward. See Figure 1 for more details. 

=== page 3 ===
[... 182 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/ | grep -E "00103|00127"; head -60 claims/001273/*.yaml
```

```
000127
001038
001273
001274
001276
001277
# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,
# on dandiset 001273.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, under
# docs/protocol.md version pilot-10, as the reader.
#
# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC, with its
# main text, figure legends and STAR Methods, and the supplement (NIHMS2098259-supplement-1.pdf,
# Figures S1 to S4 and Table S1, the Key Resource Table), all in
# paper/10.1016-j.xcrp.2025.102660.txt. The version of record was not read. No main-text PDF was
# available, so Figures 1 to 6 could not be looked at; values shown only in figures (the group
# means of Figures 4D and 4E, the n per group of Figure 2D) are not used.
#
# Code. The paper states that it does not report original code. Exponential fits and the standard
# errors of fitted constants were made with Origin 8.0; ROI intensities with MetaMorph; linear
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/001272/ | python -c "import json,sys;d=json.load(sys.stdin);print(json.dumps(d,indent=1)[:3000])"; curl -s https://api.dandiarchive.org/api/dandisets/001272/versions/draft/info/ | python -c "import json,sys;d=json.load(sys.stdin);m=d.get('metadata',d);print(m.get('name'));print(m.get('description'));print(m.get('keywords'));print(m.get('relatedResource'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 60,400p claims/001273/*.yaml
```

```
# (Figure 4D and 4E legend). The cathode-facing pole is the depolarized ROI, the anode-facing pole
# the hyperpolarized one (Results, Kinetics paragraph 1); anodic dF is negative and magnitudes are
# compared. (F5) Groups, n and tests are those of the Figure 4D and 4E legend and the text, as each
# criterion cites.
#
# Details the paper leaves open, with the readings named. (O1) ROI size and position are not given,
# only that they were "selected over the most polarized membrane regions" of the RATIO image
# (last 0.5 us of the pulse over the CONTROL image, both low-pass filtered at 12 x 12 pixels). The
# ROIs are taken from the dataset when it holds them. When it does not, they are rebuilt from the
# RATIO image as the Methods describe, under readings (a) a 12 x 12 pixel square (the Methods'
# filter size) centred on the extreme pixel of each sign within the cell, (b) the pixels within the
# cell beyond half the extreme of each sign; the outcome is the one both give, and the rebuild is
# recorded as a deviation. (O2) Fit weighting is not given (Origin 8.0); readings (a) unweighted,
# (b) weighted by 1/SEM^2 of the replicate mean. (O3) Whether the discharge amplitude is a free
# parameter is not given; the Methods write the same dFmax in both equations; readings (a) free
# discharge amplitude, (b) discharge amplitude fixed at the charging fit's dFmax. The tau readings
# are all combinations of O1 to O3 and of F2; a claim on tau is reproduced when all give its
# outcome, and blocked as methods_underspecified when they give different outcomes. (O4) Cell
# shape (elongated or random) and orientation (parallel or perpendicular) were judged by eye; the
# paper gives no rule beyond "random" when long and short cross-sections could not be identified.
[... 321 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 400,700p claims/001273/*.yaml; head -50 claims/001274/*.yaml | grep -n "00127\|001030\|001031"
```

```
(Figure S2 legend). Reproduced when, in every TTX neuron, APs (as in fig1-pure-sine-excites-all)
    present before are absent after and the mean dF over the last 100 ms of the stimulus is above
    5% before and below it after, while vehicle neurons keep their response. The window and level
    are standard choices.
- id: fig6-sine-less-than-pulse
  statement: FluoVolt sensitivity to 2-us pulses averaged 28% plus or minus 2.5% per 1 kV/cm (15% to
    47%), and to 2-kHz sine waves 11.8% plus or minus 1.7% per 1 kV/cm, 42% of the pulse value,
    smaller in every ROI.
  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,
    paragraphs 4 and 5; Figures 6B to 6D
  quote: All numbers were invariably smaller than those measured for the same ROIs with the pulse (
    Figure 6D ). The electric field sensitivity averaged across all ROIs in all the cells was 11.8% ±
    1.7% per 1 kV/cm, just 42% of the value for the 2-μs pulses
  data: elsewhere
  where: DANDI:001274 (assigned from its title); the 2-us pulse recordings of these nine cells may be
    in 001274 or in this dandiset
  expected:
  - quantity: mean pulse sensitivity over the 18 ROIs
    value: 28
    tolerance: 2.5
[... 108 more lines not kept]
```

**Agent calls Bash**

```bash
for d in 001030 001031 001032 001033 001034 001035 001271 001273 001274; do echo "$d: $(curl -s https://api.dandiarchive.org/api/dandisets/$d/ | python -c "import json,sys;print(json.load(sys.stdin)['draft_version']['name'])")"; done
```

Result: the fetched text is not kept.

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
python -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:5000])"
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
[... 129 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001272/10.1016-j.xcrp.2025.102660.yaml",
 "content": "# Claims for Semenov, Kim, Silkuniene & Pakhomov (2025), Cell Reports Physical Science 6, 102660,\n# on dandiset 001272.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-22, under\n# docs/protocol.md version pilot-10, as the reader.\n#\n# Text read. The NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC, with its\n# main text, figure legends and STAR Methods, and the supplement (NIHMS2098259-supplement-1.pdf,\n# Figures S1 to S4 and Table S1, the Key Resource Table), all in\n# paper/10.1016-j.xcrp.2025.102660.txt. The version of record was not read. No main-text PDF was\n# available; the supplement's figures were read from their legends only. Values shown only in\n# figures (the traces of Figure S1, the n per group of Figure 2D) are not used.\n#\n# Code. The paper states \"This paper does not report original code\". It names the software used:\n# Fiji ImageJ 1.53C or MetaMorph 7.7 for soma emission, Grapher 16 for traces and linear\n# regression, Origin 8.0 for fits, Sim4Life 5.2 for the field, and RStudio in Table S1. No\n# repository was read, so no method detail below is settled by code.\n#\n# Data the paper used. E18 Sprague-Dawley rat hippocampal neurons (BrainBits), cultured about one\n# week on 12-mm coverslips. A single neuron with no apparent somatic contact is centred in the\n# field, with a bipolar tungsten electrode (two 100-um rods, 120-um gap, 45 degrees, tips 50 um\n# above the coverslip) and the neuron centred in the gap. Fast imaging of the optical membrane\n# potential, 64 x 64 pixels after 4 x 4 binning, at 3,130 or 3,086.4 frames/s, 1,200 images per\n# session (50 ms before, 250 ms during and about 90 ms after the stimulus), sessions 20 to 60 s\n# apart. F is the emission over the entire soma, F0 its mean before the stimulus, and\n# dF = 100% (F - F0)/F0. Most neurons were stained with FluoVolt and recorded with 250-ms\n# unmodulated or 20-Hz modulated sine waves at 2 and 20 kHz (Figures 1, 2), in NaCl (16.4 mS/cm) or\n# sodium gluconate (8.4 mS/cm) solution (Figure 3A, 3B), with 2-s ramped 2-kHz sine waves (Figure\n# 3C) and with 1 uM tetrodotoxin (Figure S2). Strobe imaging with 2-us pulses and single sine wave\n# beats measured membrane charging (Figures 4 to 6, S3).\n#\n# This dandiset. Its title and description (DANDI:001272, \"The Use of Di8-ANEPPS to Evaluate\n# Neuronal Sensitivity to Unmodulated Sine Waves\"; control experiments with Di8-ANEPPS to make sure\n# that APs recorded with FluoVolt \"published in other DANDIsets\" were not influenced by the dye)\n# match the Figure S1 experiment. That experiment, as the paper reports it, is eight neurons loaded\n# with 5 uM Di-8-ANEPPS for 30 min in the dark, imaged with a TRITC cube, stimulated with 250-ms,\n# 2-kHz unmodulated sine waves at field strengths (V/cm) in a random sequence. Depolarization\n# reduces Di-8-ANEPPS emission, so the paper inverts its traces. The measured variable is the soma\n# emission per frame; the per-session variables are the field strength and the session order. The\n# paper spells the dye \"Di-8-ANEPSS\" in the Results and \"Di-8-ANEPPS\" elsewhere; it is one dye.\n# The claims on the Figure S1 experiment are data dataset. The paper deposited its raw images in\n# ten dandisets (Data and code availability) without saying which figure is in which. From their\n# titles only, 001030 (2-kHz sine waves, effect of the field) and 001032 to 001035 (sine wave\n# stimulation at varying frequencies) hold the FluoVolt experiments of Figures 1 to 3, 001271\n# tetrodotoxin (Figure S2), 001273 the 2-us pulse kinetics (Figure 4), 001274 sine wave\n# polarization (Figures 5, 6, S3); 001031 (100-kHz bipolar pulses) matches no figure. Claims on\n# those are data elsewhere, and the comparisons of Di-8-ANEPPS with FluoVolt are data with_inputs,\n# their FluoVolt side taken from 001030 and 001032 to 001035.\n#\n# Method details fixed from the paper, used by the Figure S1 criteria.\n# (F1) F is the mean emission over the entire cell soma per frame, F0 the mean over an interval\n# before the stimulus, dF = 100% (F - F0)/F0 (Methods, Recording of the optical APs). For\n# Di-8-ANEPPS the trace is inverted, -dF, so that depolarization is upward (Methods; Figure S1\n# legend; Results, \"APs were identified by the reduction instead of the increase of emission\").\n# (F2) Traces are not filtered or modified in any way (Methods); no detrending or smoothing.\n# (F3) The stimulus is a 250-ms, 2-kHz unmodulated sine wave (Figure S1 legend), starting 50 ms\n# into the session (Methods); the onset and the field strength of each session are taken from the\n# dataset, and the 50 ms is used when the onset is not given there.\n# (F4) A neuron's excitation threshold is the lowest field strength of a session with at least one\n# AP during the 250-ms stimulus (Figure 2D legend).\n# (F5) The maximum firing rate of a session is the inverse of the peak-to-peak interval between its\n# first two APs (Methods).\n# (F6) The two-sided Student's t test, paired or unpaired as appropriate, at p < 0.05, is the\n# paper's test where a criterion needs one and the paper names none for that finding (Methods,\n# Quantification and statistical analysis).\n#\n# Details the paper leaves open, with the readings named. Every Figure S1 criterion runs every\n# combination of the readings below; a claim is decided when all give its outcome, and blocked as\n# methods_underspecified when they give different outcomes.\n# (O1) The soma outline is not given. ROIs are taken from the dataset when it holds them. When it\n# does not, readings (a) the connected component nearest the image centre (the Methods centre the\n# neuron) of an Otsu threshold of the mean pre-stimulus frame, (b) that mask eroded by 2 pixels, to\n# leave out the neurite bases at its edge. Otsu and the 2 pixels are standard choices.\n# (O2) The length of the F0 interval is not given (\"a time interval preceding the electrical\n# stimulation\"); readings (a) all frames before the onset (about 50 ms), (b) the last 20 ms before\n# the onset. This is unlikely to change an outcome.\n# (O3) AP detection is given only as \"brief emission upticks\", with the FluoVolt neurons selected for\n# APs above 5% dF lasting about 10 ms (typical 11.3% and 8 ms). The paper says Di-8-ANEPPS has a\n# lower voltage sensitivity and gives no level for it. An AP is a local maximum of the inverted\n# trace, with width at half height between 2 and 20 ms (\"about 10 ms\"; the bounds are a standard\n# choice) and at least 5 ms from a larger maximum (standard choice; the paper's highest rates, 60 to\n# 90 Hz, give intervals over 11 ms). Readings of the height (a) above 5% (the Methods' FluoVolt\n# level), (b) above 5 SD of the inverted trace before the onset. Under (a) a neuron may show no APs\n# because the dye is less sensitive; the notebook reports it.\n# (O4) \"Near the threshold\" is not defined; readings (a) the sessions at the threshold field (F4),\n# (b) the sessions at fields up to 10% above it (the upper end of the 5% to 10% steps of the\n# Methods).\n# (O5) \"Delayed\" is not quantified for Figure S1. The Results give 100 to 200 ms after onset near\n# threshold for FluoVolt (Stimulation by 2- and 20-kHz unmodulated sine waves, paragraph 1), and say\n# the Di-8-ANEPPS effects were not different; readings (a) first AP at least 100 ms after onset,\n# (b) first AP later than the median first-AP latency of the neuron's sessions at higher fields.\n# (O6) \"Sustained firing\" and \"sustained depolarization\" are not defined by a measure. Sustained\n# firing is, as a standard choice, at least three APs with one in the last 50 ms of the stimulus.\n# Sustained depolarization is no AP in the last 100 ms of the stimulus while the mean inverted dF\n# over that window is above, reading (a) 5 SD of the inverted trace before the onset, (b) half the\n# median AP height of the neuron. The windows are standard choices.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001272\"\npaper: doi:10.1016/j.xcrp.2025.102660\nclaims:\n- id: figs1-eight-neurons\n  statement: The Di-8-ANEPPS control experiments were made on eight neurons, at field strengths tested\n    in a random sequence.\n  source: Results, Sensitivity to unmodulated sine waves was not caused by FluoVolt dye, paragraph 1;\n    Figure S1\n  quote: Experiments were performed on eight neurons using different electric field strengths tested\n    in a random sequence\n  expected:\n  - quantity: neurons recorded with Di-8-ANEPPS\n    value: 8\n    tolerance: 0\n    unit: neurons\n  criterion: Neurons are counted from the dataset's subjects, sessions or cell identifiers, each\n    recording counted once (author, step 1). The tolerance is 0, as a count of neurons is whole and\n    10% of 8 admits no other value. The order of fields over each neuron's sessions is reported\n    (the number of neurons whose fields rise monotonically with session order), not judged, since\n    the Methods also allow escalating sequences.\n- id: figs1-aps-as-emission-decrease\n  statement: With Di-8-ANEPPS, APs appear as brief reductions of emission, opposite in sign to\n    FluoVolt.\n  source: Results, Sensitivity to unmodulated sine waves was not caused by FluoVolt dye, paragraph 1;\n    Methods, Recording of the optical APs and data analyses; Figure S1 legend\n  quote: APs were identified by the reduction instead of the increase of emission\n  criterion: F1 and F2, under the readings O1 and O2. Per neuron, over the sessions at fields above\n    its threshold (F4, under O3), the largest brief deflections of dF during the stimulus are\n    negative. Detection under O3 is run on the trace as recorded (not inverted) and on the inverted\n    trace; reproduced when in every neuron with APs the inverted trace yields more APs than the\n    trace as recorded, in more than 75% of its sessions with APs (a standard choice). The counts\n    each way are reported.\n- id: figs1-near-threshold-delayed-aps\n  statement: Near threshold, 2-kHz sine waves elicited one or a few delayed APs in Di-8-ANEPPS\n    neurons.\n  source: Results, Sensitivity to unmodulated sine waves was not caused by FluoVolt dye, paragraph 1;\n    Figure S1\n  quote: Stimulation near the threshold elicited one or a few delayed APs\n  depends_on:\n  - figs1-aps-as-emission-decrease\n  criterion: F1 to F4, under O1 to O5. Per neuron, the near-threshold sessions (O4); their AP count\n    and first-AP latency from the onset (F3). The paper gives no count for \"a few\"; at most 3 APs\n    is a standard choice. Reproduced when, in more than half of the neurons with APs (a standard\n    choice), the median near-threshold session has 1 to 3 APs and its first AP is delayed (O5).\n    Counts and latencies per neuron are reported.\n- id: figs1-stronger-field-shorter-delay-sustained-firing\n  statement: In Di-8-ANEPPS neurons, increasing the field strength reduced the delay to the first AP\n    and induced sustained firing.\n  source: Results, Sensitivity to unmodulated sine waves was not caused by FluoVolt dye, paragraph 1;\n    Figure S1\n  quote: Increasing the electric field strength reduced the delay and induced sustained firing\n  depends_on:\n  - figs1-aps-as-emission-decrease\n  criterion: F1 to F4, under O1 to O3 and O6. Per neuron with sessions with APs at 3 or more fields,\n    the Spearman correlation of first-AP latency with field over those sessions. The paper reports\n    no test; reproduced when the correlation is negative in more than half of those neurons and\n    more than half of all neurons show sustained firing (O6) in some session. The majority and the\n    Spearman correlation are standard choices. The maximum firing rate (F5) against field is\n    reported per neuron.\n- id: figs1-culminates-in-sustained-depolarization\n  statement: In Di-8-ANEPPS neurons, the strongest fields replaced firing with sustained\n    depolarization (excitation followed by inhibition of firing).\n  source: Results, Sensitivity to unmodulated sine waves was not caused by FluoVolt dye, paragraph 1;\n    Figure S1 legend\n  quote: induced sustained firing that culminated in sustained depolarization\n  depends_on:\n  - figs1-stronger-field-shorter-delay-sustained-firing\n  criterion: F1 to F4, under O1 to O3 and O6. Per neuron, its sessions at its highest field. The\n    paper gives no fraction of neurons; reproduced when more than half of the neurons (a standard\n    choice) show sustained depolarization (O6) at their highest field and sustained firing or\n    more APs at some lower field. The Figure S1 legend's \"Excitation and inhibition of firing\"\n    describes one neuron; the number of neurons with each is reported.\n- id: figs1-noisier-than-fluovolt\n  statement: Di-8-ANEPPS traces were noisier than FluoVolt traces, as the dye has a lower voltage\n    sensitivity.\n  source: Results, Sensitivity to unmodulated sine waves was not caused by FluoVolt dye, paragraph 1\n  quote: Compared to FluoVolt recordings, the traces were expectedly noisier (Di-8-ANEPSS has a lower\n    voltage sensitivity)\n  data: with_inputs\n  depends_on:\n  - figs1-aps-as-emission-decrease\n  criterion: F1 to F3, under O1 to O3, for the Di-8-ANEPPS neurons of this dataset and for the FluoVolt\n    neurons stimulated with 250-ms unmodulated 2-kHz sine waves in NaCl solution in DANDI:001030 and\n    001032 to 001035 (assigned from their titles; FluoVolt traces not inverted). Per neuron, the\n    signal to noise ratio is the median AP height over the SD of dF before the onset. \"Noisier\" is\n    not defined; readings (a) that ratio, (b) the SD of dF before the onset. Reproduced when the\n    Di-8-ANEPPS median is worse (lower ratio, larger SD) than the FluoVolt median under both. A\n    two-sided unpaired t test (F6) is reported. As a variant on this dataset alone, the median\n    Di-8-ANEPPS AP height is compared with the 11.3% typical of FluoVolt (Methods).\n- id: figs1-effects-same-as-fluovolt\n  statement: Overall, the effects of 2-kHz sine waves in Di-8-ANEPPS neurons did not differ from those\n    with FluoVolt, so the excitation by unmodulated sine waves is not a sensitization by FluoVolt.\n  source: Results, Sensitivity to unmodulated sine waves was not caused by FluoVolt dye, paragraph 1;\n    Discussion, paragraph 2\n  quote: Overall, stimulation effects were not different from those observed with FluoVolt dye\n  data: with_inputs\n  depends_on:\n  - figs1-near-threshold-delayed-aps\n  - figs1-stronger-field-shorter-delay-sustained-firing\n  - figs1-culminates-in-sustained-depolarization\n  expected:\n  - quantity: mean unmodulated 2-kHz 1-AP threshold of FluoVolt neurons, the reference\n    value: 57.7\n    tolerance: 3.6\n    unit: V/cm\n  criterion: A claim of absence, for which the paper names no test. The response pattern holds when\n    figs1-near-threshold-delayed-aps, figs1-stronger-field-shorter-delay-sustained-firing and\n    figs1-culminates-in-sustained-depolarization are reproduced. The paper's own concern is a\n    sensitization by FluoVolt (Discussion, \"we ruled out possible sensitization\"), which would\n    show as lower thresholds with FluoVolt; so the 1-AP threshold (F4) of the Di-8-ANEPPS neurons is\n    compared with that of the FluoVolt neurons of figs1-noisier-than-fluovolt by a two-sided\n    unpaired t test at p < 0.05 (F6). Reproduced when the pattern holds and the test finds no\n    difference; not reproduced when the test finds the Di-8-ANEPPS threshold higher. The expected\n    value is the paper's FluoVolt threshold (Results, Asymmetric and less-efficient membrane\n    charging, last paragraph, from Figure 2D), with its SEM, against which the FluoVolt neurons\n    used are checked. A one-sample t test of the Di-8-ANEPPS thresholds against 57.7 V/cm is shown\n    as a variant on this dataset alone. The difference of means and its 95% interval are reported.\n    The Di-8-ANEPPS sessions may not have been a threshold search (fields in a random sequence), so\n    the threshold is the lowest exciting field tested, which is an upper bound; the notebook\n    reports the gap to the next lower field tested.\n- id: fig1-pure-sine-excites-all\n  statement: Unmodulated 250-ms sine waves at 2 and 20 kHz excited every neuron tested, with APs\n    100 to 200 ms after onset near threshold, firing rate rising to a ceiling of 60 to 90 Hz, and\n    an excitation block with sustained depolarization at the highest fields.\n  source: Results, Stimulation by 2- and 20-kHz unmodulated sine waves, paragraph 1; Figures 1A to 1C\n    and inset\n  quote: Pure sine waves at 2 and even 20 kHz excited 100% of neurons ... The maximum firing rate\n    increased linearly until reaching a ceiling of 60-90 Hz\n  data: elsewhere\n  where: DANDI:001030 and 001032 to 001035 (assigned from their titles; the paper does not map\n    figures to dandisets)\n  expected:\n  - quantity: fraction of neurons excited\n    value: 100\n    tolerance: 10\n    unit: percent\n  - quantity: median over neurons of the highest maximum firing rate\n    value: 76.5\n    tolerance: 22.5\n    unit: Hz\n  - quantity: first-AP latency at each neuron's lowest exciting field, median over neurons\n    value: 155\n    tolerance: 65\n    unit: ms\n  criterion: F1 to F5 and O1 to O3 and O6 of the header, applied to FluoVolt traces without\n    inversion. Reproduced when, under every reading, at least 90% of neurons are excited at each\n    frequency, the median ceiling lies within 54 to 99 Hz (60 to 90 Hz widened by 10% of each bound,\n    written above as its midpoint and half-width) and the median first-AP latency at threshold lies\n    within 90 to 220 ms (100 to 200 ms widened the same way); blocked as methods_underspecified\n    when the readings disagree. Whether the ceiling is meant for the median neuron or every neuron\n    is open (the inset shows three); the median is a standard choice and the range over neurons is\n    reported. The block is reported under O6, not judged.\n- id: fig1-20khz-needs-twice-the-field\n  statement: Responses to 20 kHz needed about 2-fold stronger fields than at 2 kHz, and all\n    thresholds at 20 kHz were about 2-fold higher than at 2 kHz.\n  source: Results, Stimulation by 2- and 20-kHz unmodulated sine waves, paragraph 1; Results,\n    Excitation thresholds are similar or lower, paragraph 1; Figure 2D\n  quote: All thresholds at 20 kHz were about 2-fold higher than at 2 kHz ( p < 0.0001, two-tailed\n    unpaired t test)\n  statistics:\n  - about: 20 kHz against 2 kHz, all thresholds\n    test: two-tailed unpaired t test\n    p: 0.0001\n    p_relation: \"<\"\n  data: elsewhere\n  where: DANDI:001032 to 001035 (assigned from their titles)\n  depends_on:\n  - fig1-pure-sine-excites-all\n  expected:\n  - quantity: ratio of mean 20-kHz to mean 2-kHz threshold, each stimulus and AP count\n    value: 2\n    tolerance: 0.2\n  criterion: Thresholds for at least 1 and at least 5 APs (Figure 2D legend), as F4, with the AP\n    readings of the header. The paper gives one p over \"all thresholds\"; readings (a) one test per\n    stimulus (modulated or not) and AP count, each p < 0.0001, (b) one test pooling the four.\n    Reproduced when each ratio is within tolerance and 20 against 2 kHz reaches p < 0.0001 under\n    every reading; blocked as methods_underspecified when they disagree.\n- id: fig2d-modulated-thresholds-higher\n  statement: Thresholds for sine waves modulated at 20 Hz were significantly higher than for pure\n    sine waves at the same carrier, for 5 APs at 2 kHz and for 1 and 5 APs at 20 kHz, so modulation\n    did not lower excitation thresholds.\n  source: Results, Excitation thresholds are similar or lower for pure 2- and 20-kHz sine waves than\n    those for modulated sine waves, paragraph 1; Figure 2D\n  quote: thresholds for modulated sine waves, which emulate the TI stimulus at the target, were\n    significantly higher than those for pure sine waves at the same frequency (for 2 kHz, 5 APs\n    p = 0.0079; for 20 kHz, 1 and 5 APs, respectively p = 0.0142 and p = 0.0037)\n  statistics:\n  - about: modulated against unmodulated, 2 kHz, 5 APs\n    test: two-tailed unpaired t test\n    p: 0.0079\n  - about: modulated against unmodulated, 20 kHz, 1 AP\n    test: two-tailed unpaired t test\n    p: 0.0142\n  - about: modulated against unmodulated, 20 kHz, 5 APs\n    test: two-tailed unpaired t test\n    p: 0.0037\n  data: elsewhere\n  where: DANDI:001032 to 001035 (assigned from their titles)\n  depends_on:\n  - fig1-pure-sine-excites-all\n  criterion: Thresholds as in fig1-20khz-needs-twice-the-field. Two-tailed unpaired t tests, as the\n    Figure 2D legend names them. Reproduced when the three modulated thresholds are higher with\n    p < 0.05 (Methods) and the 1-AP threshold at 2 kHz is not lower for modulated waves at p < 0.05,\n    under every AP reading; blocked as methods_underspecified when they disagree.\n- id: fig2-modulated-locks-to-beats\n  statement: With 20-Hz modulation, firing above threshold locked to the beats, one AP near the peak\n    of each of the five beats and at most two per beat (ten in all), and modulated sine waves\n    triggered no sustained firing or sustained depolarization.\n  source: Results, Stimulation by 2- and 20-kHz sinusoids modulated at 20 Hz, paragraph 1; Figures 2A\n    and 2B\n  quote: single APs emerged near the peak of each beat, so the firing rate equaled the modulation\n    rate ... the maximum number of APs evoked by five beats was limited to ten. Unlike pure sine\n    waves, modulated stimuli did not trigger sustained firing or sustained depolarization\n  data: elsewhere\n  where: DANDI:001032 to 001035 (assigned from their titles)\n  depends_on:\n  - fig1-pure-sine-excites-all\n  criterion: AP readings of the header, modulated sessions only. The paper does not quantify \"near the\n    peak\"; as standard choices, reproduced when no session has more than 10 APs, in sessions with 5\n    APs or more most APs fall within 12.5 to 37.5 ms of each 50-ms beat, and no session shows\n    sustained depolarization (O6). The AP phase histogram is reported.\n- id: fig2c-pure-more-aps\n  statement: In the same neuron at the same field strength, pure sine waves triggered more APs than\n    modulated ones, and the threshold was typically lower for unmodulated signals.\n  source: Results, Stimulation by 2- and 20-kHz sinusoids modulated at 20 Hz, paragraph 2; Figures 2A\n    to 2C\n  quote: the threshold was typically lower for unmodulated signals ( Figures 2A - 2C ). At the same\n    field strengths, pure sine waves triggered a larger number of APs\n  data: elsewhere\n  where: DANDI:001032 to 001035 (assigned from their titles)\n  depends_on:\n  - fig1-pure-sine-excites-all\n  criterion: AP readings of the header. Pairs are a neuron's modulated and unmodulated sessions at the\n    same carrier and field. The paper reports no test; reproduced when the unmodulated count is\n    larger in more pairs than the reverse, and the unmodulated threshold lower in more neurons than\n    the reverse, under every reading. A two-sided paired t test (F6) of the counts is reported.\n- id: fig3b-low-conductivity-halves-threshold\n  statement: Lowering solution conductivity from 16.4 to 8.4 mS/cm with sodium gluconate reversibly\n    lowered excitation thresholds about 2-fold at all sine wave frequencies from 2 to 20 kHz.\n  source: Results, Decreased extracellular conductivity lowers excitation thresholds, paragraph 1;\n    Figures 3A and 3B\n  quote: Switching to the NaGlu-based solution reversibly and reproducibly decreased excitation\n    thresholds ~2-fold across all sine wave frequencies tested\n  data: elsewhere\n  where: DANDI:001030 and 001032 to 001035 (assigned from their titles)\n  depends_on:\n  - fig1-pure-sine-excites-all\n  expected:\n  - quantity: ratio of NaCl to NaGlu mean 1-AP threshold, each frequency\n    value: 2\n    tolerance: 0.2\n  criterion: 1-AP thresholds (F4) for 250-ms unmodulated sine waves per frequency and solution, 4 to 8\n    neurons per point (Figure 3B legend), AP readings of the header. Reproduced when the ratio is\n    within tolerance at every frequency under every reading.\n- id: fig3c-sustained-firing-2s\n  statement: In the low-conductivity solution, a 2-s unmodulated 2-kHz sine wave ramped over 250 ms\n    evoked firing for its whole duration, rising with field until replaced by a firing block with\n    sustained depolarization.\n  source: Results, Decreased extracellular conductivity lowers excitation thresholds, paragraph 3;\n    Figure 3C\n  quote: we observed sustained firing for the entire duration of the sine wave ( Figure 3C ). The rate\n    of firing increased with the electric field strength until it was replaced by a firing block\n    and sustained depolarization\n  data: elsewhere\n  where: DANDI:001030 (assigned from its title)\n  criterion: Traces corrected for bleaching by subtracting a trace without APs (Methods); AP readings\n    of the header. Reproduced when an intermediate field has APs in the last 250 ms of the stimulus,\n    the AP count rises with field up to some field, and the highest field shows sustained\n    depolarization (O6, over the last 250 ms of the stimulus). The windows are standard choices.\n- id: figs2-ttx-blocks-depolarization\n  statement: 1 uM tetrodotoxin abolished both the APs and the sustained depolarization caused by\n    intense unmodulated 2-kHz sine waves, while the vehicle did not.\n  source: Results, Tetrodotoxin blocks sustained depolarization, paragraph 1; Figure S2 legend\n  quote: the inhibition of sodium channels with 1 μM tetrodotoxin not only abolished the APs but also\n    fully blocked the sustained depolarization\n  data: elsewhere\n  where: DANDI:001271 (assigned from its title)\n  criterion: Per neuron, sessions before and about 5 min after TTX or vehicle at the same field (Figure\n    S2 legend), AP readings of the header. Reproduced when, in every TTX neuron, APs present before\n    are absent after and sustained depolarization (O6) present before is absent after, while vehicle\n    neurons keep their response.\n- id: fig4-pooled-time-constants\n  statement: Membrane charging by 2-us pulses is fast; pooled over 19 experiments, charging and\n    discharging time constants averaged 0.7 and 0.91 us at the cathodic pole and 0.65 and 0.8 us at\n    the anodic pole, so membranes charge fully within each sine wave cycle up to 100 to 200 kHz.\n  source: Results, Kinetics of membrane charging by pulsed electric fields, the paragraph after the\n    Figure 4 legend; Figures 4D and 4E\n  quote: The time constants pooled together for all cells averaged 0.7 ± 0.08 (charging) and 0.91 ±\n    0.08 (discharging) μs for the cathodic cell pole and 0.65 ± 0.05 and 0.8 ± 0.07 μs for the\n    anodic pole, respectively (mean ± SEM, n = 19)\n  data: elsewhere\n  where: DANDI:001273 (assigned from its title)\n  expected:\n  - quantity: charging tau, cathodic pole\n    value: 0.7\n    tolerance: 0.08\n    unit: us\n  - quantity: discharging tau, cathodic pole\n    value: 0.91\n    tolerance: 0.08\n    unit: us\n  - quantity: charging tau, anodic pole\n    value: 0.65\n    tolerance: 0.05\n    unit: us\n  - quantity: discharging tau, anodic pole\n    value: 0.8\n    tolerance: 0.07\n    unit: us\n  criterion: Fits and readings as in the claims file for DANDI:001273 (fig4-pooled-time-constants),\n    which tests this claim on its own data; tolerances are the paper's SEMs.\n- id: fig4-orientation-and-poles\n  statement: Aligning elongated cells with the field doubled the time constants; the maximum optical\n    TMP and the time constants did not differ between the cathode- and anode-facing poles; and\n    discharging was slower than charging except in elongated cells aligned with the field.\n  source: Results, Kinetics of membrane charging by pulsed electric fields, the paragraph after the\n    Figure 4 legend; Figures 4D and 4E\n  quote: Δ F max did not differ at the cathodic and anodic cell poles, indicating the lack of\n    rectification of the applied electric field ... Aligning elongated cells with the electric\n    field doubled the time constants ... discharging time constants were always larger than the\n    charging ones in the same cell ( p < 0.001, paired t test)\n  statistics:\n  - about: elongated cells, parallel against perpendicular\n    test: paired t test\n    p: 0.001\n    p_relation: \"<\"\n  - about: elongated parallel against random cells\n    test: unpaired t test\n    p: 0.01\n    p_relation: \"<\"\n  - about: discharging against charging tau\n    test: paired t test\n    p: 0.001\n    p_relation: \"<\"\n  data: elsewhere\n  where: DANDI:001273 (assigned from its title)\n  criterion: As in the claims file for DANDI:001273 (fig4-orientation-time-constants,\n    fig4-no-pole-difference and fig4-discharging-slower), which tests each part on its own data;\n    reproduced when all three are reproduced there.\n- id: fig6-sine-less-than-pulse\n  statement: FluoVolt sensitivity to 2-kHz sine waves (11.8% per 1 kV/cm) was 42% of that to 2-us\n    pulses (28% per 1 kV/cm) and smaller in every ROI, with sine waves polarizing the two poles more\n    asymmetrically than pulses.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    paragraphs 2 to 5; Figures 5, 6B to 6D and S3\n  quote: All numbers were invariably smaller than those measured for the same ROIs with the pulse (\n    Figure 6D ). The electric field sensitivity averaged across all ROIs in all the cells was 11.8% ±\n    1.7% per 1 kV/cm, just 42% of the value for the 2-μs pulses\n  data: elsewhere\n  where: DANDI:001274 (assigned from its title)\n  expected:\n  - quantity: mean pulse sensitivity over the 18 ROIs\n    value: 28\n    tolerance: 2.5\n    unit: percent per kV/cm\n  - quantity: mean sine wave sensitivity over the 18 ROIs\n    value: 11.8\n    tolerance: 1.7\n    unit: percent per kV/cm\n  - quantity: mean sine over mean pulse sensitivity\n    value: 42\n    tolerance: 4.2\n    unit: percent\n  criterion: Measures and readings as in the claims file for DANDI:001274, which tests this finding on\n    its own data; tolerances are the paper's SEMs, and 10% for the ratio.\n- id: threshold-depolarization-estimate\n  statement: The 2-kHz AP threshold of 57.7 V/cm times the sine wave sensitivity gives a 0.68%\n    emission change, about 6.8 mV, so the threshold depolarization is 5 to 15 mV, as with\n    intracellular current injection.\n  source: Results, Asymmetric and less-efficient membrane charging by sine waves compared to pulses,\n    last paragraph\n  quote: This threshold corresponds to a 0.68% ± 0.11% FluoVolt emission change (11.8 × 57.7/1,000)\n    ... a 0.68% emission change corresponds to a 6.8-mV depolarization at the AP threshold\n  data: elsewhere\n  where: DANDI:001032 to 001035 for the threshold and DANDI:001274 for the sensitivity (assigned from\n    their titles)\n  depends_on:\n  - fig1-20khz-needs-twice-the-field\n  - fig6-sine-less-than-pulse\n  expected:\n  - quantity: mean unmodulated 2-kHz 1-AP threshold\n    value: 57.7\n    tolerance: 3.6\n    unit: V/cm\n  - quantity: emission change at the 2-kHz AP threshold\n    value: 0.68\n    tolerance: 0.11\n    unit: percent\n  - quantity: depolarization at the 2-kHz AP threshold\n    value: 6.8\n    tolerance: 1.1\n    unit: mV\n  criterion: Mean sine sensitivity of fig6-sine-less-than-pulse times the mean unmodulated 2-kHz 1-AP\n    threshold (F4), divided by 1,000, and that times 10 mV per 1% (the calibration of reference 47 as\n    the paper uses it). Tolerances are the paper's SEMs, the last being 0.11% times 10 mV per 1%.\n    Reproduced when all three are within tolerance.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001272/10.1016-j.xcrp.2025.102660.yaml",
 "old_string": "    significantly higher than those for pure sine waves at the same frequency (for 2 kHz, 5 APs\n    p = 0.0079; for 20 kHz, 1 and 5 APs, respectively p = 0.0142 and p = 0.0037)",
 "new_string": "    significantly higher than those for pure sine waves at the same frequency ... p = 0.0079 ...\n    p = 0.0142 and p = 0.0037"
}
```

```
The file claims/001272/10.1016-j.xcrp.2025.102660.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001272/10.1016-j.xcrp.2025.102660.yaml paper/10.1016-j.xcrp.2025.102660.txt; grep -nP "(?<!#)[^#\n]*[^\"']: [^\n]*" claims/001272/*.yaml | grep -v "^\S*:\s*#" | grep -vE "^[0-9]+:\s*(- )?[a-z_]+: " | head; grep -c "—\|rather" claims/001272/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python -c "
import yaml;d=yaml.safe_load(open('claims/001272/10.1016-j.xcrp.2025.102660.yaml'))
def walk(x,p=''):
  if isinstance(x,dict):
    [walk(v,p+'.'+str(k)) for k,v in x.items()]
  elif isinstance(x,list):
    [walk(v,p+'[%d]'%i) for i,v in enumerate(x)]
  elif isinstance(x,str) and (': ' in x or '—' in x or 'rather' in x): print(p,x[:80])
walk(d)
print(sum('criterion' in c for c in d['claims']), sum('statistics' in c for c in d['claims']), sum('expected' in c for c in d['claims']), [c.get('data','dataset') for c in d['claims']].count('dataset'))"
```

```
19 3 8 5
```

**Agent**

I wrote `claims/001272/10.1016-j.xcrp.2025.102660.yaml`. The quote checker reports 19 claims, 19 quotes, 7 statistical values and 0 problems. Nothing is committed.

**Text read.** I read the NIH author manuscript (NIHMS2098259, PMC12320893) as served by Europe PMC: main text, figure legends, STAR Methods, and the supplement PDF (Figures S1 to S4, Table S1). I did not read the version of record. There is no main-text PDF, so I could not look at the figures themselves; I read Figure S1 from its legend. The paper says it reports no original code, so I read none and no method detail is settled by code.

**This dataset.** I matched it to the paper from its archive title and description only: "The Use of Di8-ANEPPS to Evaluate Neuronal Sensitivity to Unmodulated Sine Waves". That is the Figure S1 control experiment: eight neurons stained with Di-8-ANEPPS, stimulated with 250-ms, 2-kHz sine waves.

**Claims (19).** Every claim has a quote and a criterion.
- **Tested on this dataset (5):** the count of eight neurons; action potentials appear as drops in emission; one or a few delayed spikes near threshold; stronger fields shorten the delay and give sustained firing; the strongest fields end in sustained depolarization.
- **Need the FluoVolt dandisets 001030 and 001032 to 001035 as well (2):** Di-8-ANEPPS traces are noisier than FluoVolt traces; the effects are the same with either dye.
- **Tested elsewhere (12):** the paper's other main findings, each assigned from the dandiset titles (Figures 1 to 3, S2, 4, 5 and 6, and the threshold depolarization estimate). The paper itself does not say which figure is in which dandiset. The Figure 4 and Figure 6 criteria refer to the existing claims files for 001273 and 001274.
- **Statistics:** 3 claims have them, 7 entries in all. All are from the threshold and Figure 4 findings; the paper reports no test for any Figure S1 finding.
- **Expected values:** 8 claims have them. The neuron count has tolerance 0, because 10% of 8 allows no other whole number.

**Details the paper leaves open, and the readings named.** A claim counts as decided only when every reading gives the same outcome.
- **Soma outline:** taken from the dataset if it holds one. Otherwise (a) an Otsu mask of the mean pre-stimulus frame, keeping the part nearest the image centre, or (b) that mask shrunk by 2 pixels.
- **Baseline interval for F0:** (a) all frames before the stimulus (about 50 ms), or (b) the last 20 ms before it.
- **Spike detection for Di-8-ANEPPS:** the paper gives no level for this dye. Readings: (a) a peak above 5% (the Methods' level for FluoVolt), or (b) a peak above 5 SD of the pre-stimulus trace. Both require a width of 2 to 20 ms, which is a standard choice.
- **"Near the threshold":** (a) sessions at the threshold field, or (b) sessions up to 10% above it.
- **"Delayed":** (a) the first spike at least 100 ms after onset, the lower end of the range the paper gives for FluoVolt, or (b) later than the same neuron's spikes at higher fields.
- **Sustained depolarization:** no spike in the last 100 ms of the stimulus while the signal stays above (a) 5 SD of baseline, or (b) half the neuron's median spike height.
- **Standard choices:** "a few" as 1 to 3 spikes; majority rules across neurons; a Spearman correlation for the delay falling with field.
- **"Noisier":** (a) signal to noise ratio, or (b) baseline SD.
- **Elsewhere claims:** whether "all thresholds" means one test per group or one pooled test, and whether the 60 to 90 Hz ceiling applies to the median neuron or to every neuron.

**Missing from the paper.**
- No test, measure or count for any Figure S1 finding, and no spike detection rule for Di-8-ANEPPS.
- No mapping from figures to dandisets.
- No statement of whether the Di-8-ANEPPS sessions were a threshold search. If they were not, the lowest firing field tested is only an upper bound on the threshold, so the comparison with the FluoVolt threshold of 57.7 ± 3.6 V/cm is limited; the criterion asks the notebook to report the gap to the next lower field.

The paper spells the dye "Di-8-ANEPSS" once in the Results and "Di-8-ANEPPS" elsewhere; it is the same dye.

## End of run

24 turns, 5 minutes, result: success.
