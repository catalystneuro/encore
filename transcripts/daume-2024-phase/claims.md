# 000673 · claims · run 39906678261

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/000673/ paper/ 2>&1
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '/^## Reader/,/^## Author/' docs/protocol.md
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
ls claims/001453/ claims/000673/ paper/ 2>&1; wc -l paper/*; head -30 paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls claims/001453/; cat claims/001453/*.yaml | head -250
```

```
10.1016-j.cub.2025.04.027.yaml
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
[... 231 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 250,600p claims/001453/*.yaml | grep -nE '^\S|^  [a-z_]+:|^- id|kind|data:|elsewhere|with_' | head -80; ls tools docs; grep -rn "kind" docs/claims*.md 2>/dev/null | head
```

```
1:- id: fig2k-more-monocular
2:  statement: DC have a higher proportion of purely monocular neurons than ZF (0.37 against 0.16,
4:  source: Figure 2K
5:  quote: DC show a higher proportion of purely monocular neurons (ZF = 0.16, DC = 0.37
6:  statistics:
11:- id: fig2l-bi-ratio
12:  statement: The binocularity index ratio is higher in ZF than in DC (0.72 against 0.24, p =
14:  source: Figure 2L
15:  quote: BI ratios show a higher fraction of binocular neurons in ZF compared to DC (ZF = 0.72, DC =
17:  statistics:
21:- id: fig3e-longer-swims
22:  statement: Head-fixed DC perform longer swims than ZF (median 0.75 s against 0.29 s, p <
24:  source: Figure 3E and 3F
25:  quote: DC performed significantly longer swims than ZF (DC = 0.75 s, ZF = 0.29 s
26:  statistics:
31:- id: fig3cd-zf-turn-more
32:  statement: Head-fixed ZF show larger directional tail angles than DC to turn-inducing stimuli,
34:  source: Figure 3C and 3D
35:  quote: In ZF, swims during forward last significantly longer than those during turn-inducing
38:  statistics:
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,200p tools/claims_check.py
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

[... 93 more lines not kept]
```

**Agent calls Bash**

```bash
cat schemas/claims.schema.json | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d,indent=1))" | head -250
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
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "import json; d=json.load(open('schemas/claims.schema.json')); print(json.dumps(d['\$defs'],indent=1))"
```

```
{
 "expected": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "quantity",
   "value"
  ],
  "properties": {
   "quantity": {
    "type": "string"
   },
   "value": {
    "type": "number"
   },
   "tolerance": {
    "type": "number",
    "minimum": 0
   },
   "unit": {
[... 82 more lines not kept]
```

**Agent**

Now the paper text.

**Agent calls Bash**

```bash
cd paper; python - <<'E'
t=open('10.1038-s41586-024-07309-z.txt').read()
print(len(t))
print(t[:60000])
E
```

```
<persisted-output>
Output too large (59.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/4a24e30c-a203-4da9-b3c0-e0d61f8c46fc/tool-results/bmiayx3j4.txt

Preview (first 2KB):
316576
DOI: 10.1038/s41586-024-07309-z
Version: as served by europe_pmc
Source: europe_pmc+crossref (paper-text-fetcher)
Stored: 2026-10-20
Extracted: as fetched; with 3 supplement file(s) from the PMC Open Access cloud data (PMC11078732), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
------------------------------------------------------------------------
pmc Nature Nature 981 npgopen 0410462 Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title Nature Portfolio PMC11078732 PMC11078732.1 11078732 11078732 38632400 10.1038/s41586-024-07309-z 7309 1 Article Control of working memory by phase–amplitude coupling of human hippocampal neurons http://orcid.org/0000-0002-6516-7288 Daume Jonathan [removed: an e-mail address] 1 2 3 Kamiński Jan 1 4 Schjetnan Andrea G. P. 5 Salimpour Yousef 6 http://orcid.org/0009-0005-5328-3977 Khan Umais 1 http://orcid.org/0009-0004-4392-9933 Kyzar Michael 1 http://orcid.org/0000-0002-7157-3645 Reed Chrystal M. 2 http://orcid.org/0000-0003-0958-050X Anderson William S. 6 http://orcid.org/0000-0002-3443-3790 Valiante Taufik A. 5 Mamelak Adam N. 1 http://orcid.org/0000-0002-9207-7069 Rutishauser Ueli [removed: an e-mail address] 1 2 3 7 1 https://ror.org/02pammg90 grid.50956.3f 0000 0001 2152 9905 Department of Neurosurgery, Cedars-Sinai Medical Center, Los Angeles, CA USA 2 https://ror.org/02pammg90 grid.50956.3f 0000 0001 2152 9905 Department of Neurology, Cedars-Sinai Medical Center, Los Angeles, CA USA 3 https://ror.org/02pammg90 grid.50956.3f 0000 0001 2152 9905 Center for Neural Science and Medicine, Department of Biomedical Sciences, Cedars-Sinai Medical Center, Los Angeles, CA USA 4 grid.413454.3 0000 0001 1958 0162 Center of Excellence for Neural Plasticity and Brain Disorders: 
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  fold -s -w 200 paper/10.1038-s41586-024-07309-z.txt > $TMPDIR/p.txt; wc -l $TMPDIR/p.txt; echo $TMPDIR; grep -n -iE "supplementary (information|table)|methods|code availability|github" $TMPDIR/p.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "limit": 250
}
```

```
1	DOI: 10.1038/s41586-024-07309-z
2	Version: as served by europe_pmc
3	Source: europe_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 3 supplement file(s) from the PMC Open Access cloud data (PMC11078732), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	pmc Nature Nature 981 npgopen 0410462 Nature 0028-0836 1476-4687 pmc-is-collection-domain yes pmc-collection-title Nature Portfolio PMC11078732 PMC11078732.1 11078732 11078732 38632400 
8	10.1038/s41586-024-07309-z 7309 1 Article Control of working memory by phase–amplitude coupling of human hippocampal neurons http://orcid.org/0000-0002-6516-7288 Daume Jonathan 
9	[removed: an e-mail address] 1 2 3 Kamiński Jan 1 4 Schjetnan Andrea G. P. 5 Salimpour Yousef 6 http://orcid.org/0009-0005-5328-3977 Khan Umais 1 http://orcid.org/0009-0004-4392-9933 Kyzar Michael 1 
10	http://orcid.org/0000-0002-7157-3645 Reed Chrystal M. 2 http://orcid.org/0000-0003-0958-050X Anderson William S. 6 http://orcid.org/0000-0002-3443-3790 Valiante Taufik A. 5 Mamelak Adam N. 1 
11	http://orcid.org/0000-0002-9207-7069 Rutishauser Ueli [removed: an e-mail address] 1 2 3 7 1 https://ror.org/02pammg90 grid.50956.3f 0000 0001 2152 9905 Department of Neurosurgery, Cedars-Sinai Medical 
12	Center, Los Angeles, CA USA 2 https://ror.org/02pammg90 grid.50956.3f 0000 0001 2152 9905 Department of Neurology, Cedars-Sinai Medical Center, Los Angeles, CA USA 3 https://ror.org/02pammg90 
13	grid.50956.3f 0000 0001 2152 9905 Center for Neural Science and Medicine, Department of Biomedical Sciences, Cedars-Sinai Medical Center, Los Angeles, CA USA 4 grid.413454.3 0000 0001 1958 0162 
14	Center of Excellence for Neural Plasticity and Brain Disorders: BRAINCITY, Nencki Institute of Experimental Biology, Polish Academy of Sciences, Warsaw, Poland 5 grid.17063.33 0000 0001 2157 2938 
15	Krembil Research Institute and Division of Neur
[... 235 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 250,
 "limit": 240
}
```

```
250	confirm here for WM, but that remains to be tested for other high-level cognitive functions involving top-down control from frontal regions such as attention 53 , decision making 54 , 55 , speech 
251	comprehension 56 and long-term memory retrieval 34 . Methods Patients A total of 36 patients (44 sessions; 21 female individuals; 15 male individuals; age: 40.47 ± 13.76 years; Supplementary Table 5 
252	; no statistical methods were used to predetermine sample sizes) participated in the study. All of the patients had Behnke–Fried hybrid electrodes (AdTech) implanted for intracranial seizure 
253	monitoring and evaluation for surgical treatment of drug-resistant epilepsy. Their participation was voluntary, and all of the patients gave their informed consent. This study was part of an NIH 
254	Brain consortium between three institutions (Cedars-Sinai Medical Center, Toronto Western Hospital and Johns Hopkins Hospital) and was approved by the Institutional Review Board of the institution at 
255	which the patient was enrolled. A pre-operative magnetic resonance imaging (MRI) image together with MRI or computed tomography post-operative images were used to localize the electrodes using 
256	Freesurfer as previously described 34 . Electrode positions are plotted on the CITI168 Atlas Brain 57 in MNI152 coordinates for the sole purpose of visualization (Fig. 1b ). The 3D plot was generated 
257	using FieldTrip (v.20200409) and the Brainnetome Atlas 58 . Coordinates appearing in white matter or outside of the target area is due to usage of a template brain. Electrodes that were localized 
258	outside of the target area in native space were excluded from analysis (8 out of a total of 265 recording sites). Data used in this study are available in the DANDI archive 59 . Task The task 
259	consists of 140 trials and 280 novel pictures. Each trial started with a fixation cross presented for 0.9 to 1.2 s (Fig. 1a ). Depending on the load condition, the fixation cross was follow
[... 230 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 489,
 "limit": 240
}
```

```
489	deviations from the original signal are due to the fact that signals at frequencies lower or higher than the edge frequencies of 2 and 150 Hz, respectively, were not represented by the wavelet 
490	transform but present in the original signal. ( k ) Assessment of the wavelet-based signal reconstruction. We computed linear models using the reconstructed signal as predictor for the original 
491	signal and extracted R-squared values as a function of time and frequency in each trial and channel. Values were averaged across all trials and all hippocampal channels. An R-squared values of close 
492	to 1 indicates almost perfect reconstruction of the original signal. As stated above, the slight drop in reconstruction quality at extreme frequencies is explained by the fact that signals at 
493	frequencies lower or higher than the edge frequencies, respectively, were not represented by the wavelet transform but present in the original signal. Extended Data Fig. 2 Additional PAC analyses. ( 
494	a ) PAC comodulogram averaged across all channels separately for each area. Strongest PAC was observed between theta and gamma in both areas of the MTL. Frontal areas did not show strong PAC, with 
495	weak PAC at <2 Hz in pre-SMA and vmPFC. We focused our analysis on frequencies above 2 Hz (1–3 Hz bandpass) to ensure that at least 2 full cycles fit within our analysis window of 2.5 s (length of 
496	maintenance period). ( b ) In addition to testing theta-gamma PAC across significant channels (see main text), we tested PAC between the load conditions across patients after averaging all 
497	significant PAC channels within each patient. The results were similar to the analysis across channels, with strongest PAC in MTL areas and only weak PAC in frontal channels (see percent of patients 
498	with significant PAC channels below each figure), suggesting that the results were not driven by channels from a single patient. Only in the hippocampus again, PAC was stronger for load 1 as c
[... 230 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -E "^=+|SUPPLEMENT|supp[123]|Supplementary Table [1-5]\b" $TMPDIR/p.txt | sed -n 1,200p | awk -F: '$1>700' | head -60
```

```
942:=== page 1 ===
952:=== page 2 ===
1035:=== page 3 ===
1175:=== page 4 ===
1434:=== page 5 ===
1659:=== page 6 ===
1694:=== page 7 ===
1730:=== page 8 ===
1767:=== page 9 ===
1802:=== page 10 ===
1836:=== page 11 ===
1872:=== page 12 ===
1887:=== page 1 ===
1889:=== page 2 ===
1891:=== page 3 ===
1896:=== page 1 ===
1938:=== page 2 ===
1985:=== page 3 ===
2036:=== page 4 ===
2081:=== page 5 ===
[... 40 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/p.txt",
 "offset": 900,
 "limit": 300
}
```

```
900	[71] Kramer, M. A., Tort, A. B. L. & Kopell, N. J. Sharp edge artifacts and spurious coupling in EEG frequency comodulation measures. J. Neurosci. Methods 170, 352–357 (2008). 
901	10.1016/j.jneumeth.2008.01.020
902	
903	[72] Cole, S. & Voytek, B. Cycle-by-cycle analysis of neural oscillations. J. Neurophysiol. 122, 849–861 (2019). 10.1152/jn.00273.2019
904	
905	[73] Minxha, J. & Daume, J. in Intracranial EEG: A Guide for Cognitive Neuroscientists 719–737 (Springer, 2023). 10.1007/978-3-031-20910-9_45
906	
907	[74] Tallon-Baudry, C., Bertrand, O., Delpuech, C. & Pernier, J. Stimulus specificity of phase-locked and non-phase-locked 40 hz visual responses in human. J. Neurosci. 16, 4240–4249 (1996). 
908	10.1523/JNEUROSCI.16-13-04240.1996
909	
910	[75] Cohen, M. X. & Donner, T. H. Midfrontal conflict-related theta-band power reflects neural oscillations that predict behavior. J. Neurophysiol. 110, 2752–2763 (2013). 10.1152/jn.00479.2013
911	
912	[76] Cohen, M. Analyzing Neural Time Series Data: Theory and Practice (MIT Press, 2014). 10.7551/mitpress/9609.001.0001
913	
914	[77] Kamiński, J., Brzezicka, A., Mamelak, A. N. & Rutishauser, U. Combined phase-rate coding by persistently active neurons as a mechanism for maintaining multiple items in working memory in humans. 
915	Neuron 106, 256–264 (2020). 10.1016/j.neuron.2020.01.032
916	
917	[78] Al-Daffaie, K. & Khan, S. Logistic regression for circular data. AIP Conf. Proc. 1842, 030022 (2017). 10.1063/1.4982860
918	
919	[79] Krekelberg, B. BayesFactor (v.2.3.0) (Zenodo, 2022);
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1400,1700p $TMPDIR/p.txt | grep -v '^ *$' | head -150
```

```
p 
Intercept 
-0.0565 
-2.76 
0.005 
0.021 
1.37 
0.17 
SC 
0.0032 
2.19 
0.028 
-3 x 10-5 
-0.02 
0.98 
Load1 
0.0931 
3.26 
0.001 
-0.054 
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1650,1900p $TMPDIR/p.txt | grep -v '^ *$' | head -120; sed -n 1887,1900p $TMPDIR/p.txt; grep -n "##### Supplement" $TMPDIR/p.txt
```

```
=== page 6 ===
5 
Supplementary Discussion 
Role of high gamma band in PAC and WM 
The high gamma band has been suggested to reflect processing of encoded information within 
the hippocampus24,25,88. In favor of this hypothesis, PAC in our study differed as a function of WM 
load only for frequencies involving the high gamma range. In line with earlier reports82, our results 
show that storing more information in WM leads to lower estimates of theta-high gamma PAC 
because high gamma power is more broadly distributed across the theta cycle. A related finding 
is that in rats, the number of gamma cycles increases specifically in the high gamma range when 
the length of a running track increased89,90, potentially signaling an increase in WM load. 
Moreover, in our study persistently active category neurons were more strongly phase locked to 
signals in the high gamma range when their preferred stimulus was maintained. No effects were 
observed for frequencies involving the low gamma band (30-55 Hz). Our study provides evidence 
for a specific role of the high gamma band in the processing and maintenance of WM content in 
the hippocampus, and reports load-dependent effects of theta-gamma PAC during WM 
maintenance.  
In line with earlier studies91–93, activity in the high gamma (70-140 Hz) frequency range was 
reflective of processing and maintenance in WM of encoded sensory information. Yamamoto and 
colleagues91 found that in mice, the activity of high gamma oscillations (65-140 Hz) in the 
[... 117 more lines not kept]
```

**Agent**

Full text, Methods, Extended Data legends and Supplementary Information (Tables S1–S5) are all present. Next, the linked code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/rutishauserlab/SBCAT-release-NWB.git sbcat 2>&1 | tail -3; cd sbcat && git log -1 --format='%H %ad' && find . -type f -not -path './.git/*' | head -100
```

```
a25e8cc3f61630a428f190381745257d4506f148 Tue Jan 21 12:33:07 2025 -0800
./assets/Figure1.png
./README.md
./NWB_SBCAT_analysis/helpers/internal/geometry/popGeometry_plotSignalNoiseAxes3D.m
./NWB_SBCAT_analysis/helpers/internal/geometry/popGeometry_plotSignalNoiseAxes2D.m
./NWB_SBCAT_analysis/helpers/internal/geometry/popGeometry_defineAxes.m
./NWB_SBCAT_analysis/helpers/internal/geometry/noiseCorr_genData.m
./NWB_SBCAT_analysis/helpers/internal/geometry/main_popGeometry_noiseCorrs.m
./NWB_SBCAT_analysis/helpers/internal/geometry/getNoiseVar_alongSignalAxis.m
./NWB_SBCAT_analysis/helpers/internal/geometry/LinearClassifier_getSignalAxis.m
./NWB_SBCAT_analysis/helpers/internal/etc/spikePDFestimate.m
./NWB_SBCAT_analysis/helpers/internal/etc/setCommonAxisRange.m
./NWB_SBCAT_analysis/helpers/internal/etc/plotTrialMarkers.m
./NWB_SBCAT_analysis/helpers/internal/etc/plotSpikeRaster_multiple_simplified.m
./NWB_SBCAT_analysis/helpers/internal/etc/plotSpikeRaster_multiple.m
./NWB_SBCAT_analysis/helpers/internal/etc/plotSpikeRasterMain.m
./NWB_SBCAT_analysis/helpers/internal/etc/plotPSTH_forSpikeRaster.m
./NWB_SBCAT_analysis/helpers/internal/etc/getTimestamps_forSortedRasterPlot.m
./NWB_SBCAT_analysis/helpers/internal/etc/getTimestampsOfTrials.m
./NWB_SBCAT_analysis/helpers/internal/etc/getRelativeTimestamps.m
[... 53 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sbcat; cat README.md; cat NWB_SBCAT_analysis/NWB_SBCAT_analysis_main.m
```

```
# Sample code for: Control of working memory by phase–amplitude coupling of human hippocampal neurons

[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
[![Generic badge](https://img.shields.io/badge/release-1.0.0-green.svg)](https://github.com/rutishauserlab/SBCAT-release-NWB/releases/tag/v1.0.0)
[![Generic badge](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.10494534-orange.svg)](https://doi.org/10.5281/zenodo.10494534)

## Introduction

This repository contains the code that accompanies [Daume et. al. 2024](https://www.nature.com/articles/s41586-024-07309-z) 'Control of working memory maintenance by theta-gamma phase amplitude coupling of human hippocampal neurons.' The purpose of the code in this repository is to provide examples of how to use the released data. This dataset is formatted in the [Neurodata Without Borders (NWB)](https://www.nwb.org/) format, which can easily be accessed from both MATLAB and Python as described [here](https://nwb-schema.readthedocs.io/en/latest/index.html). 

Abstract of the paper:
>Retaining information in working memory is a demanding process that relies on cognitive control to protect memoranda-specific persistent activity from interference. However, how cognitive control regulates working memory storage is unclear. Here we show that interactions of frontal control and hippocampal persistent activity are coordinated by theta–gamma phase–amplitude coupling (TG-PAC). We recorded single neurons in the human medial temporal and frontal lobe while patients maintained multiple items in their working memory. In the hippocampus, TG-PAC was indicative of working memory load and quality. We identified cells that selectively spiked during nonlinear interactions of theta phase and gamma amplitude. The spike timing of these PAC neurons was coordinated with frontal theta activity when cognitive control demand was high. By introducing noise correlations with persisten
[... 386 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sbcat/NWB_SBCAT_analysis/helpers/custom; cat NWB_calcSelective_SB.m NWB_determineSBPeriods.m condenseAreas.m
```

```
function [sig_cells,areasSternberg] = NWB_calcSelective_SB(nwbAll, all_units, params)
%NWB_CALCSELECTIVE Takes the output of NWB_SB_extractUnits and runs
%selectivity tests for the sternberg task. Optionally plots trial aligned
%spikes

if isfield(params,'rateFilter') && ~isempty(params.rateFilter) && params.rateFilter > 0
    rateFilter = params.rateFilter;
else
    rateFilter = [];
end

% Filtering for Global Rate (rateFilter should be a nonzero float)
aboveRate = ones(length(all_units),1);
if ~isempty(rateFilter)
    for i = 1:length(all_units)
        globalRate = length(all_units(i).spike_times)/(max(all_units(i).spike_times)-min(all_units(i).spike_times));
        rateBool = globalRate < rateFilter;
        if rateBool % If the rate is below the filter threshold
            aboveRate(i) = 0;
        end
[... 461 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sbcat/NWB_SBCAT_analysis/helpers; grep -n -iE "accura|RT|resp|ttest|statcond|load|correct" custom/NWB_QA_graphs.m | head -60; cat custom/NWB_SB_extractUnits.m | head -80
```

```
2:% NWB_QA_graphs Generates behavioral and spike sorting metrics used in the SB
14:    %% Accuracy
17:        accTrials = nwbAll{i}.intervals_trials.vectordata.get('response_accuracy').data.load();
21:    plot(sort(accTotals),'k.','MarkerSize',10); hold on
24:    acc_sem = std(accTotals)/sqrt(length(accTotals));
29:    title(sprintf('Accuracy: \\mu=%.2f \\sigma=%.2f',mean(accTotals),std(accTotals)))
31:    ylabel('Accuracy (%)')
39:    %% RT vs Load
40:    filter_correct = 1;
41:    RTs_all = []; % Compiling raw RTs; {subject ID, load, RT}
43:        session_Loads = double(nwbAll{i}.intervals_trials.vectordata.get('loads').data.load());
44:        tsResp = nwbAll{i}.intervals_trials.vectordata.get('timestamps_Response').data.load();
45:        tsProbe = nwbAll{i}.intervals_trials.vectordata.get('timestamps_Probe').data.load();
46:        if filter_correct % Filtering out incorrect trials
47:            accuracyBool = logical(nwbAll{i}.intervals_trials.vectordata.get('response_accuracy').data.load());
48:            session_Loads = session_Loads(accuracyBool);
49:            tsResp = tsResp(accuracyBool);
50:            tsProbe = tsProbe(accuracyBool);
52:        session_RTs = tsResp-tsProbe; 
53:        session_Num = NaN(length(session_RTs),1); session_Num(:) = i;
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sbcat/NWB_SBCAT_analysis/helpers/internal/PAC; cat NWB_samplePAC_LFP.m call_cfc.m cfc_tort_comodulogram.m | grep -v "^\s*$"
```

```
function [LFP_PAC_figs] = NWB_samplePAC_LFP(nwbAll, paths)
%% NWB_SAMPLEPAC_LFP Calculates phase-amplitude coupling metrics for a sample electrode (Fig 2d, Daume et al)
% in:
% - nwbAll: a cell array of all nwb files imported in NWB_SBCAT_import_main
% operation: 
% - paths: Paths defined in NWB_SBCAT_import_main. The path of interest is
% the code path, which is used to load the dataset of the trials selected
% for the computation of LFP PAC
% - Extracts the example lfp channel of interest and separates it into
% periods of [-0.5 3] seconds for each maintenance period. PAC is then
% calculated using Tort's method for loads 1 & 3. 
% out:
% - LFP_PAC_figs: a cell array containing figures for all lfps analyzed.
% For this case, only one lfp is being analyzed so there should only be 1
% fig in this array. 
%
% Example Channel: sub-4_ses-1_P60CS, channel row 49
fs = filesep;
sample_sub = 4;
sample_ses = 1;
[... 375 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sbcat/NWB_SBCAT_analysis/helpers/internal/PAC; grep -v "^\s*$" NWB_samplePAC_SU.m; grep -v "^\s*$" plot_PAC_neuron.m | head -150
```

```
function [figOut] = NWB_samplePAC_SU(nwbAll, all_units, paths)
% - nwbAll: a cell array of all nwb files imported in NWB_SBCAT_import_main
% operation: 
% - paths: Paths defined in NWB_SBCAT_import_main. The path of interest is
% the code path, which is used to load the dataset of the trials selected
% for the computation of LFP PAC
% - all_units: The output of NWB_SB_extractUnits
fs = filesep;
sample_sub = 26;
sample_ses = 1;
% Access data loaded from import script
% Check if session of interest was imported
sub_ses_arr = NaN(length(nwbAll),2);
for k = 1:length(nwbAll)
    sub_ses_arr(k,1) = str2double(nwbAll{k}.general_subject.subject_id);
    sub_ses_arr(k,2) = str2double(nwbAll{k}.general_session_id);
end
find_example = find(sample_sub == sub_ses_arr(:,1) & sample_ses == sub_ses_arr(:,2),1);
if isempty(find_example)
    warning('Example not found. Please import session (5) sub-4_ses-1_P60CS.')
[... 224 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/sbcat/NWB_SBCAT_analysis/helpers/internal/geometry; grep -v "^\s*%\|^\s*$" LinearClassifier_getSignalAxis.m popGeometry_defineAxes.m getNoiseVar_alongSignalAxis.m | head -150; grep -n "naccu\|tail\|paired" ../../3rdParty/stats/statcond.m | head -20
```

```
LinearClassifier_getSignalAxis.m:function [signalVector_derived, signalVector_fromModel_norm, fHyperplane, fBoundLine] = LinearClassifier_getSignalAxis(Betas, Bias, P )
LinearClassifier_getSignalAxis.m:Beta = Betas;
LinearClassifier_getSignalAxis.m:b    = Bias;
LinearClassifier_getSignalAxis.m:fHyperplane = @(X) -(X(2:end)*Beta(2:end) + b)/Beta(1);
LinearClassifier_getSignalAxis.m:fBoundLine = @(X) -(X*Beta(1) + b)/Beta(2);
LinearClassifier_getSignalAxis.m:H=[];
LinearClassifier_getSignalAxis.m:for k=1:P-1    
LinearClassifier_getSignalAxis.m:    hypPoint1 = randn(1,P);
LinearClassifier_getSignalAxis.m:    hypPoint1(1) = fHyperplane(hypPoint1);
LinearClassifier_getSignalAxis.m:    hypPoint2 = randn(1,P);
LinearClassifier_getSignalAxis.m:    hypPoint2(1) = fHyperplane(hypPoint2);
LinearClassifier_getSignalAxis.m:    H(:,k) = hypPoint2-hypPoint1;
LinearClassifier_getSignalAxis.m:end
LinearClassifier_getSignalAxis.m:[Q,R] = qr(H);
LinearClassifier_getSignalAxis.m:l = size(H,2);   % l+1, l+2 ... are orthogonal
LinearClassifier_getSignalAxis.m:signalVector_derived = Q(:,l+1);
LinearClassifier_getSignalAxis.m:angels=[];
LinearClassifier_getSignalAxis.m:for k=1:l
LinearClassifier_getSignalAxis.m:    angels(k) = dot(signalVector_derived, H(:,k)/norm(H(:,k)) );
LinearClassifier_getSignalAxis.m:end
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
curl -s https://api.dandiarchive.org/api/dandisets/000673/ | python -c "import json,sys; d=json.load(sys.stdin); print(json.dumps({k:d[k] for k in ('identifier','most_recent_published_version','draft_version') if k in d},indent=1)[:1500])"; curl -s "https://api.dandiarchive.org/api/dandisets/000673/versions/draft/info/" | python -c "import json,sys; d=json.load(sys.stdin)['metadata']; print(d.get('name')); print(d.get('description'))"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
ls claims/ | head -50; ls claims/000686 claims/000678 2>/dev/null; head -60 claims/000686/*.yaml
```

```
000003
000004
000005
000006
000008
000009
000010
000011
000013
000015
000016
000017
000019
000023
000034
000035
000036
000037
000041
000044
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd  for s in "93.66 ± 7.04%" "t 43 = −4.45" "137 out of 586" "t 129 = 1.43" "pre-SMA: t 4" "n = 23 patients" "89 neurons (24.72%)" "t 269 = 2.93" "t 245 = 2.43" "t 88 = 0.73" "cluster P = 0.004" "F 1,150 = 16.23" "t 150 = 3.06" "79 (37.29%) out of 212" "28 (35.44%)" "72.77%" "t 78 = 2.43" "t 62 = 3.82" "t 162 = 6.40" "cluster P < 0.001" "t 166 = 2.10" "t 161 = 5.26" "t 20 = 3.16" "t 21 = 2.94" "t 21 = 3.59" "t 31 = 2.77" "F 1,18 = 12.55" "t 161 = 2.15" "P = 0.016; Fig. 6j" "t 585 = −0.86"; do grep -c -F "$s" paper/10.1038-s41586-024-07309-z.txt | tr '\n' ' '; echo "$s"; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Write**

```json
{
 "file_path": "claims/000673/10.1038-s41586-024-07309-z.yaml",
 "content": "# Claims for Daume, Kaminski, Schjetnan, Salimpour, Khan, Kyzar, Reed, Anderson, Valiante,\n# Mamelak & Rutishauser (2024), \"Control of working memory by phase-amplitude coupling of human\n# hippocampal neurons\", Nature 629, 393-401, on dandiset 000673.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-23,\n# protocol pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record (open access, CC BY) as served by Europe PMC (PMC11078732),\n# full text with Results, Methods, figure legends and Extended Data Fig. 1 to 9 legends, and the\n# Supplementary Information PDF (41586_2024_7309_MOESM1_ESM: Supplementary Tables S1 to S5 and the\n# Supplementary Discussion). The Peer Review File (MOESM3) is in the text too; the Reporting\n# Summary (MOESM2) came through empty and nothing here rests on it. The text of Supplementary\n# Table S4 is garbled (its model formula is lost); its rows (Intercept, SC, Load1, SC:Load1 for\n# hippocampus and amygdala) were read from the text that survives.\n#\n# Code read: github.com/rutishauserlab/SBCAT-release-NWB at commit a25e8cc3 (2025-01-21), the\n# repository the paper links (also Zenodo 10.5281/zenodo.10494533). It holds sample code only:\n# loading the NWB files, behaviour metrics (NWB_QA_graphs.m), category cell selection\n# (NWB_calcSelective_SB.m), the LFP PAC comodulogram with Tort's modulation index\n# (cfc_tort_comodulogram.m, NWB_samplePAC_LFP.m), the PAC neuron GLMs for one example neuron\n# (plot_PAC_neuron.m, NWB_samplePAC_SU.m), spike sorting metrics, and a simulation of signal and\n# noise axes (helpers/internal/geometry). It holds no code for single-trial PAC, the mixed-effects\n# GLMs, spike-field coherence, noise correlations on the data, population decoding, or the\n# cluster statistics. Where the code settles a detail it is cited as \"code\" below.\n#\n# Data the paper used (as the paper reports it). 36 patients (21 female, 15 male, 40.47 +/- 13.76\n# years), 44 sessions, with Behnke-Fried hybrid depth electrodes (8 microwires per bundle) in the\n# hippocampus, amygdala, pre-SMA, dACC and vmPFC (left and right), recorded at Cedars-Sinai,\n# Toronto Western and Johns Hopkins. 1,454 single neurons (360 hippocampus, 496 amygdala, 204\n# pre-SMA, 188 dACC, 206 vmPFC) sorted with OSort, and 1,922 microwire LFP channels (586, 421, 283,\n# 325, 307); the LFP was low-passed at 175 Hz and downsampled to 400 Hz after spike waveforms were\n# interpolated out. Task: a Sternberg working memory task of 140 trials, 70 load 1 and 70 load 3,\n# with pictures from five categories (faces, animals, cars or tools, fruits, landscapes); each\n# picture 2 s on screen, then a 2.55 to 2.85 s maintenance period, then a probe (match or\n# non-match) answered by button press. The code reads, from each session's trials table, the\n# timestamps of fixation, encoding 1 to 3, maintenance, probe and response, the picture IDs of\n# encoding 1 to 3 and the probe (the category is the first digit of the picture ID), the load,\n# probe_in_out and response_accuracy. The data availability statement names DANDI 000673, which\n# the dandiset's title and description match (44 sessions); it should hold every experiment of\n# the paper.\n#\n# General rules for the criteria below.\n# (G1) Unless a criterion says otherwise, a claim of an effect is reproduced when the paper's test,\n#      run as described, gives p < 0.05 (after the correction the paper applied) in the direction\n#      the paper reports, and every expected value is within tolerance; partially reproduced when\n#      the test holds and an expected value is out of tolerance; not reproduced when the test does\n#      not hold. A claim of absence follows the protocol: the paper's test, as written.\n# (G2) Tests. \"Two-sided permutation-based t-test\" is statcond.m (EEGLAB) with method 'perm',\n#      10,000 permutations, paired over neurons, channels, pairs or sessions unless the paper says\n#      unpaired (Methods, Statistics). Cluster tests are FieldTrip cluster-based permutation over\n#      frequencies, 10,000 permutations, alpha 0.025 per one-sided cluster, Bonferroni corrected\n#      for the number of tests named in the legend. The cluster-forming threshold and cluster\n#      statistic are not stated; FieldTrip's defaults (clusteralpha 0.05, maxsum) are the reading\n#      the citation implies and are used.\n# (G3) Windows. Maintenance is 0 to 2.5 s after maintenance onset (Methods, Task). Baseline is\n#      -0.9 to -0.3 s before picture 1 onset (Fig. 3b legend). Only correct trials unless stated.\n# (G4) Preferred trials of a category neuron are trials in which a picture of its preferred\n#      category was among the encoded pictures (code, NWB_calcSelective_SB.m, maintenance raster);\n#      in load 3 the three pictures are from three different categories (Methods, Task).\n#\n# Details the paper and code leave open, used in the criteria below. Where a detail could change\n# the outcome the readings are named, and the notebook runs each.\n# (O1) LFP artefact rejection. The Methods give the automated steps (amplitude z-scored per channel\n#      across all trials after capping at 6 s.d.; a trial is removed for a wire when any sample\n#      exceeds 4 s.d., or when the z-scored difference between every fourth sample exceeds 10\n#      s.d.), then visual inspection that cannot be repeated. The span z-scored is not stated.\n#      Readings are (a) the automated steps on the -0.5 to 3 s maintenance epochs; (b) the same on\n#      whole trials (fixation to response). The visual step is left out under both, a deviation.\n#      Whether the released LFP already excludes channels or trials is for the author to find.\n# (O2) Equal trial counts. Correct load 1 and load 3 trials are randomly subsampled to equal\n#      numbers per channel (Methods, PAC); the seed is a standard choice and cannot change the\n#      outcome much.\n# (O3) Band averages for LFP PAC. The code (NWB_samplePAC_LFP.m) takes theta as phase centre\n#      frequencies 4 and 6 Hz (2 Hz bandwidth, so 3 to 7 Hz) and high gamma as amplitude centres\n#      70 to 140 Hz in 5 Hz steps; low gamma is read the same way as centres 30 to 55 Hz. A\n#      channel's value is the mean z-scored MI over those pairs.\n# (O4) Surrogate null of the proportion of PAC channels (Fig. 2b). Not described beyond \"trial-\n#      shuffled surrogates\". Reading is that for each of the 200 surrogates of each channel the\n#      surrogate MI is z-scored with the normal fitted to all 200, and the null is the 200\n#      proportions of channels whose surrogate exceeds z 1.64 (200 surrogates give the printed\n#      minimum P of 0.005).\n# (O5) Single-trial PAC. The Methods do not say how it is computed. Readings are (a) Tort's MI\n#      (18 bins) computed on each trial's 0 to 2.5 s window, averaged over the theta and high-gamma\n#      pairs of O3, raw; (b) the same, z-scored across trials within each channel. GLM forms are\n#      from Supplementary Tables S2 and S3 (normal response; random intercepts for patient and\n#      for channel, or neuron-channel pair, nested in patient).\n# (O6) Firing rate units for comparisons with baseline and between conditions. Figures show the\n#      percentage change from baseline, the tests do not say. Readings are (a) rate in Hz; (b)\n#      percentage change from each neuron's baseline.\n# (O7) \"Insufficient data in the incorrect condition\". No minimum is given. Readings are a\n#      minimum of (a) one; (b) two; (c) three incorrect trials per neuron; the n each gives is\n#      reported against the paper's n.\n# (O8) SFC surrogates. The spike times are perturbed \"by adding random noise\" 500 times; the size\n#      of the noise is not given. Readings are (a) each spike moved to a uniformly random time\n#      within the same 0 to 2.5 s window; (b) each spike shifted by a uniform jitter of +/-250 ms\n#      (half a cycle at 2 Hz, the lowest frequency analysed).\n# (O9) PAC neuron FDR. \"FDR corrected for all possible channel combinations\". Readings are\n#      Benjamini-Hochberg over (a) all neuron-to-channel combinations of an area and load; (b) the\n#      channel combinations of each neuron.\n# (O10) Noise correlation averaging (Fig. 6a). Readings are (a) the mean over all correct trials\n#      of each pair; (b) the mean within each condition (preferred or not, by load), then across\n#      conditions.\n# (O11) Decoding. The Methods fix the decoder (linear SVM, fitcecoc one-versus-one, 80% train and\n#      20% test, z-scored maintenance rates, load 1 correct trials, trials subsampled to the\n#      smallest category, 500 repetitions, greedy ensembles) and the removal of noise correlations\n#      (trials shuffled per neuron within category). They do not fix (i) whether the intact and\n#      removed ensembles are built separately or the intact order is reused; (ii) the measure of\n#      Fig. 6c. Readings for (i) are (a) separate greedy ensembles; (b) the intact ensemble order\n#      used for both. For (ii) the measure is, per session, the mean accuracy gain at the steps\n#      where a PAC neuron was added before peak accuracy, averaged over the PAC neurons of the\n#      session, as Leavitt et al. (ref. 36) define it; the paper gives no other.\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"000673\"\npaper: doi:10.1038/s41586-024-07309-z\nclaims:\n- id: cohort-counts\n  statement: The study recorded 36 patients in 44 sessions, with 1,454 single neurons (360\n    hippocampus, 496 amygdala, 204 pre-SMA, 188 dACC, 206 vmPFC) and 1,922 microwire LFP channels\n    (586, 421, 283, 325 and 307).\n  source: Methods, Patients and Spike sorting; Results, Hippocampal PAC is modulated by WM load,\n    paragraph 1\n  quote: We isolated 360 neurons in the hippocampus, 496 in the amygdala, 204 in the pre-SMA, 188\n    in the dACC and 206 in the vmPFC. Of the LFP channels, 586 channels were in the hippocampus,\n    421 in the amygdala, 283 in the pre-SMA, 325 in the dACC and 307 in the vmPFC\n  expected:\n  - quantity: sessions\n    value: 44\n    tolerance: 0\n  - quantity: patients\n    value: 36\n    tolerance: 0\n  - quantity: single neurons, all areas\n    value: 1454\n    tolerance: 0\n  - quantity: LFP channels, all areas\n    value: 1922\n    tolerance: 0\n  criterion: Counts from the units and LFP electrode tables, with areas merged across hemispheres\n    as condenseAreas.m does. Reproduced when every total and every per-area count matches exactly;\n    partially reproduced when all are within 2%.\n- id: fig1d-rt-load\n  statement: Patients responded more slowly in load 3 than in load 1 trials (1.46 s against 1.33\n    s).\n  source: Results, Main, paragraph 3; Figure 1d\n  quote: the participants responded slower (1.46 s versus 1.33 s; t 43 = 6.42, P < 0.001)\n  statistics:\n  - test: two-sided permutation-based t-test, 10,000 permutations\n    statistic: t43 = 6.42\n    p: 0.0001\n    n: 44 sessions\n  expected:\n  - quantity: RT, load 3\n    value: 1.46\n    tolerance: 0.146\n    unit: s\n  - quantity: RT, load 1\n    value: 1.33\n    tolerance: 0.133\n    unit: s\n  criterion: RT is response time minus probe onset (Fig. 1d legend; code). Per session the median\n    RT of correct trials in each load, as NWB_QA_graphs.m computes it; the values are the means\n    over sessions; the paired permutation t-test over 44 sessions (G2). The per-session mean RT\n    of correct trials is shown as a variant.\n- id: fig1d-accuracy-load\n  statement: Patients were less accurate in load 3 than in load 1 trials (91.60% against 95.71%).\n  source: Results, Main, paragraph 3; Figure 1d\n  quote: less accurately (91.60% versus 95.71%; t 43 = −4.45, P < 0.001) in load 3 trials compared\n    with load 1 trials\n  statistics:\n  - test: two-sided permutation-based t-test, 10,000 permutations\n    statistic: t43 = -4.45\n    p: 0.0001\n    n: 44 sessions\n  expected:\n  - quantity: accuracy, load 3\n    value: 91.6\n    tolerance: 9.16\n    unit: '%'\n  - quantity: accuracy, load 1\n    value: 95.71\n    tolerance: 9.57\n    unit: '%'\n  criterion: Per session the percentage of correct trials (response_accuracy) in each load; means\n    over sessions; paired permutation t-test over 44 sessions (G2).\n- id: behaviour-overall-accuracy\n  statement: Mean accuracy was 93.66 +/- 7.04% (s.d. over sessions), and 78.34 +/- 20.09% of\n    errors were false negatives.\n  source: Results, Main, paragraph 3\n  quote: Mean accuracy was 93.66 ± 7.04% (mean ± s.d.; 78.34 ± 20.09% of all errors were false\n    negatives)\n  expected:\n  - quantity: mean accuracy over sessions\n    value: 93.66\n    tolerance: 7.04\n    unit: '%'\n  - quantity: false negatives as a share of errors, mean over sessions\n    value: 78.34\n    tolerance: 20.09\n    unit: '%'\n  criterion: Tolerance is the s.d. the paper reports. A false negative is an incorrect response to\n    a match probe (probe_in_out = 1). Sessions without errors are left out of the second mean.\n- id: fig2a-theta-gamma-pac\n  statement: Across all recorded channels, PAC during maintenance was strongest between theta\n    phase (3-7 Hz) and the amplitude of a low (30-55 Hz) and a high (70-140 Hz) gamma band.\n  source: Results, Hippocampal PAC is modulated by WM load, paragraph 1; Figure 2a\n  quote: PAC was strongest between the phase in the theta range (3–7 Hz) and the amplitude in two\n    different gamma-frequency bands—a lower (30–55 Hz) and a higher gamma range (70–140 Hz)\n  criterion: Comodulogram as in cfc_tort_comodulogram.m (Methods, PAC; O1, O2) on the -0.5 to 3 s\n    epochs of subsampled correct trials of both loads, cut to 0 to 2.5 s, phase centres 2 to 14\n    Hz (2 Hz bandwidth), amplitude centres 30 to 150 Hz in 5 Hz steps (bandwidth twice the phase\n    centre), 18 bins, z-scored against 200 trial-shuffled surrogates; averaged over channels\n    (1,917 in the paper). Reproduced when the largest mean z lies at a phase centre of 4 or 6 Hz,\n    and the amplitude profile at those phase centres has a local maximum within 30 to 55 Hz and\n    another within 70 to 140 Hz.\n- id: fig2b-pac-channel-proportions\n  statement: 137 of 586 hippocampal channels showed significant theta-high-gamma PAC; the\n    proportions of such channels in the hippocampus, amygdala and vmPFC exceeded the\n    trial-shuffled null, while pre-SMA and dACC had few such channels.\n  source: Results, Hippocampal PAC is modulated by WM load, paragraphs 1 and 2; Figure 2b\n  quote: For theta to high-gamma PAC, 137 out of 586 hippocampal channels showed significant PAC\n    across all correct trials from both load conditions\n  statistics:\n  - test: right-sided permutation test against trial-shuffled surrogates\n    p: 0.005\n    n: channels per area; hippocampus, amygdala and vmPFC\n  expected:\n  - quantity: significant hippocampal channels\n    value: 137\n    tolerance: 13.7\n  - quantity: significant amygdala channels\n    value: 130\n    tolerance: 13\n  - quantity: significant vmPFC channels\n    value: 40\n    tolerance: 4\n  - quantity: significant pre-SMA channels\n    value: 5\n    tolerance: 0.5\n  - quantity: significant dACC channels\n    value: 14\n    tolerance: 1.4\n  criterion: A channel has significant PAC when its mean z-scored MI over theta and high gamma\n    (O3), from all subsampled trials of both loads, exceeds 1.64 (Methods, PAC). The amygdala,\n    vmPFC, pre-SMA and dACC counts are the n of the load tests (Fig. 2c legend; t129, t39, t4,\n    t13). Reproduced when the hippocampal, amygdala and vmPFC proportions exceed the 99th\n    percentile of their surrogate null (O4) and the counts are within tolerance; partially\n    reproduced when the three exceed the null and a count is out of tolerance.\n- id: fig2c-hippocampus-load\n  statement: In the 137 hippocampal channels with significant PAC, theta-high-gamma PAC was weaker\n    in load 3 than in load 1 trials.\n  source: Results, Hippocampal PAC is modulated by WM load, paragraph 1; Figure 2c (left)\n  quote: This comparison revealed significantly weaker theta–high-gamma PAC in load 3 compared with\n    load 1 trials ( t 136 = −4.26, P < 0.001\n  statistics:\n  - test: two-sided permutation-based t-test\n    statistic: t136 = -4.26\n    p: 0.0005\n    corrected: FDR over five brain areas\n    n: 137 channels\n  depends_on:\n  - fig2b-pac-channel-proportions\n  criterion: Per significant hippocampal channel, the mean z-scored MI over theta and high gamma\n    (O3) in load 1 and in load 3 (equal trial counts, O2), each z-scored against 200 surrogates\n    of its own load; paired permutation t-test over channels; Benjamini-Hochberg over the five\n    areas' p-values. Reproduced when the corrected p < 0.05 with load 1 higher.\n- id: fig2c-no-load-effect-other-areas\n  statement: Theta-high-gamma PAC did not differ between loads in the amygdala, vmPFC, pre-SMA or\n    dACC channels with significant PAC.\n  source: Results, Hippocampal PAC is modulated by WM load, paragraph 2; Figure 2c (middle and\n    right)\n  quote: theta–high-gamma PAC did not differ significantly between the two load conditions in\n    neither of these two areas (Fig. 2c ; t 129 = 1.43, P = 0.38, Bayes factor (BF) 01 = 1.40;\n    and t 39 = 0.16, P = 0.87, BF 01 = 5.84, respectively)\n  statistics:\n  - about: amygdala\n    test: two-sided permutation-based t-test\n    statistic: t129 = 1.43\n    p: 0.38\n    corrected: FDR over five brain areas\n    n: 130 channels\n  - about: vmPFC\n    test: two-sided permutation-based t-test\n    statistic: t39 = 0.16\n    p: 0.87\n    corrected: FDR over five brain areas\n    n: 40 channels\n  - about: pre-SMA\n    test: two-sided permutation-based t-test\n    statistic: t4 = -0.16\n    p: 0.87\n    n: 5 channels\n  - about: dACC\n    test: two-sided permutation-based t-test\n    statistic: t13 = -0.82\n    p: 0.73\n    n: 14 channels\n  depends_on:\n  - fig2b-pac-channel-proportions\n  criterion: A claim of absence. The test of fig2c-hippocampus-load in each of the four areas, FDR\n    corrected over five areas. Reproduced when no area has corrected p < 0.05; not reproduced\n    when any has. The mean load difference of each area is reported.\n- id: edf2b-hippocampus-load-patients\n  statement: Averaging significant PAC channels within each patient, hippocampal PAC was again\n    stronger in load 1 than in load 3, and no other area showed a load difference.\n  source: Extended Data Fig. 2b legend\n  quote: Only in the hippocampus again, PAC was stronger for load 1 as compared to load 3 (n = 23\n    patients, p = 0.0049), observable in almost each single patient. No significant differences\n    were found between the load conditions in other regions\n  statistics:\n  - test: two-sided permutation-based t-test\n    p: 0.0049\n    n: 23 patients\n  depends_on:\n  - fig2c-hippocampus-load\n  criterion: Per patient (sessions of one patient pooled), the mean over significant channels of\n    each load's z-scored theta-high-gamma MI; paired permutation t-test over patients per area.\n    Reproduced when the hippocampus gives p < 0.05 with load 1 higher and no other area gives\n    p < 0.05; partially reproduced when the hippocampus holds and another area also differs.\n- id: edf2c-low-gamma-no-load-effect\n  statement: Theta-low-gamma (30-55 Hz) PAC did not differ between loads in any region.\n  source: Results, Hippocampal PAC is modulated by WM load, paragraph 2; Extended Data Fig. 2c\n  quote: For PAC involving the low gamma band (30–55 Hz), there were no significant differences\n    between the load conditions in any of the regions\n  criterion: A claim of absence. As fig2c-hippocampus-load with low gamma (amplitude centres 30 to\n    55 Hz, O3) both for channel selection and for the load test (the paper's n are 148, 155, 10,\n    22 and 48 channels). The paper's correction is not stated for this panel; the test is run\n    uncorrected, as the legend lists none. Reproduced when no area has p < 0.05; not reproduced\n    when any has.\n- id: tables1-slow-fast-theta\n  statement: Split into slow (2-5 Hz) and fast (5-9 Hz) theta, PAC differed between loads only in\n    the hippocampus and only with high gamma, most strongly for fast theta (t116 = -3.05, p =\n    0.0015; slow theta, t147 = -2.31, p = 0.0163).\n  source: Supplementary Table S1; Supplementary Discussion, Related work on role of theta\n  quote: PAC differed significantly only in the hippocampus and only for high gamma power combined\n    with either low or high theta frequency bands, with the strongest differences in the fast\n    theta band\n  statistics:\n  - about: hippocampus, fast theta to high gamma\n    test: two-sided permutation-based t-test, uncorrected\n    statistic: t(116) = -3.05\n    p: 0.0015\n  - about: hippocampus, slow theta to high gamma\n    test: two-sided permutation-based t-test, uncorrected\n    statistic: t(147) = -2.3141\n    p: 0.0163\n  criterion: The phase bands are not mapped to centre frequencies in the text. Readings are (a)\n    slow theta as phase centres 2 and 4 Hz and fast theta as 6 and 8 Hz of the comodulogram;\n    (b) bands filtered directly at 2-5 Hz and 5-9 Hz. Channels are selected per band\n    combination, as the differing n of Table S1 show. Reproduced when, under one reading, of the\n    20 area and band tests only the two hippocampal high-gamma tests give p < 0.05, both with\n    load 1 higher.\n- id: fig2f-rt-single-trial-pac\n  statement: In the hippocampus, stronger single-trial theta-high-gamma PAC went with faster RTs,\n    while no such relation held in the amygdala or vmPFC.\n  source: Results, Hippocampal PAC is modulated by WM load, paragraph 2; Figure 2f; Supplementary\n    Table S2\n  quote: In the hippocampus, faster RTs were associated with stronger single-trial estimates of\n    TG-PAC\n  statistics:\n  - about: hippocampus, PAC term\n    test: mixed-effects GLM\n    statistic: estimate -49.07, t = -4.01\n    p: 6.0e-5\n    n: 137 channels\n  - about: amygdala, PAC term\n    test: mixed-effects GLM\n    statistic: estimate -5.15, t = -0.70\n    p: 0.48\n    n: 130 channels\n  - about: vmPFC, PAC term\n    test: mixed-effects GLM\n    statistic: estimate 24.51, t = 1.18\n    p: 0.24\n    n: 40 channels\n  depends_on:\n  - fig2b-pac-channel-proportions\n  criterion: Correct trials of the significant PAC channels; RT ~ 1 + PAC + load + PAC*load +\n    (1|patientID) + (1|patientID:channelID), normal response (Table S2), single-trial PAC under\n    each reading of O5. Reproduced when, under the readings, the hippocampal PAC term is negative\n    with p < 0.05 and the amygdala and vmPFC terms have p >= 0.05; methods_underspecified when the\n    readings disagree.\n- id: edf3-hippocampus-pac-controls\n  statement: The hippocampal load effect on PAC was not explained by theta or gamma power, theta\n    waveform asymmetry, theta-gamma phase-phase coupling, preferred phase or PAC peak frequency.\n  source: Results, Hippocampal PAC is modulated by WM load, paragraph 2; Extended Data Fig. 3b,\n    c, d, g, h\n  quote: we tested whether the differences in hippocampal PAC between loads could be explained by\n    changes in power, theta waveform shape, cross-frequency phase–phase coupling, preferred phase\n    or PAC peak frequency but did not find evidence for any of those factors\n  depends_on:\n  - fig2c-hippocampus-load\n  criterion: A claim of absence over the 137 channels, each with a two-sided paired permutation\n    t-test between loads (Extended Data Fig. 3 legend). Theta (3-7 Hz) and gamma (70-140 Hz)\n    power on the PAC trials; peak-to-trough and rise-to-decay asymmetry from the bycycle toolbox\n    with its default settings (the paper gives none); theta-high-gamma phase-phase coupling as\n    the n:m phase locking value of refs 73 and 83 (the ratio is not given; readings are the\n    ratio of the band centres, 5 to 105 Hz, and the ratio of each phase and amplitude centre pair\n    of O3, averaged); the load difference of preferred phase tested against zero with a circular\n    one-sample test (V test against 0); the peak frequency from a comodulogram with 0.5 Hz phase\n    steps. Reproduced when none of the tests gives p < 0.05; partially reproduced when one does;\n    not reproduced when more do. The asymmetries are also tested against 0.5.\n- id: edf3a-kappa-load\n  statement: The distribution of gamma amplitude over theta phase was wider (lower kappa) in load\n    3 than in load 1 across hippocampal PAC channels.\n  source: Extended Data Fig. 3a legend\n  quote: Across all PAC channels, kappa was significantly lower in load 3 compared to load 1 (n =\n    137 channels, t(136) = −3.7453, p = 0.0001) trials\n  statistics:\n  - test: two-sided permutation-based t-test\n    statistic: t(136) = -3.7453\n    p: 0.0001\n    n: 137 channels\n  depends_on:\n  - fig2b-pac-channel-proportions\n  criterion: Kappa is the von Mises concentration estimated (circ_kappa) from the 18-bin\n    distribution of high-gamma amplitude over theta phase, bins weighted by their normalized\n    amplitude; the estimator is not named, and circ_kappa of the CircStat toolbox is the\n    standard choice. Paired permutation t-test over channels.\n- id: edf3e-nesting\n  statement: 110 of the 137 hippocampal PAC channels (80.29%) showed theta-high-gamma nesting, and\n    PAC remained lower in load 3 than load 1 in those channels.\n  source: Extended Data Fig. 3e legend\n  quote: 110 of the 137 significant PAC channels (80.29%) in the hippocampus showed nesting between\n    high gamma and theta. When testing PAC between the load conditions after removing channels\n    that did not show significant nesting, PAC was still significantly lower in load 3 than 1 (n =\n    110; t(109) = −4.10; p = 0.0001)\n  statistics:\n  - test: two-sided permutation-based t-test\n    statistic: t(109) = -4.10\n    p: 0.0001\n    n: 110 channels\n  expected:\n  - quantity: channels with nesting\n    value: 110\n    tolerance: 11\n  depends_on:\n  - fig2c-hippocampus-load\n  criterion: Nesting as in the Methods (PAC, last paragraph) after Vaz et al.; a local maximum is a\n    sample of the averaged raw waveform larger than both neighbours. Reproduced when the load\n    test holds in the nested channels and the count is within tolerance.\n- id: edf3f-raw-mi-load\n  statement: Raw (not z-scored) theta-gamma MI was also larger in load 1 than in load 3 in the\n    hippocampal PAC channels.\n  source: Extended Data Fig. 3f legend\n  quote: Raw theta-gamma PAC was significantly larger in load 1 compared to load 3 (n = 137;\n    t(136) = −4.0264, p = 0.0001)\n  statistics:\n  - test: two-sided permutation-based t-test\n    statistic: t(136) = -4.0264\n    p: 0.0001\n    n: 137 channels\n  depends_on:\n  - fig2b-pac-channel-proportions\n- id: methods-spectral-slope\n  statement: The slope of the log-log power spectrum did not differ between load 1 and load 3\n    trials in hippocampal channels.\n  source: Methods, LFP preprocessing\n  quote: The slope of log–log power spectra did not differ significantly between load 1 and load 3\n    trials in hippocampal channels ( n = 586 channels; mean slope −1.7526 ± 0.3902 versus\n    −1.7517 ± 0.3928, t 585 = −0.86, P = 0.39)\n  statistics:\n  - test: two-sided permutation-based t-test\n    statistic: t585 = -0.86\n    p: 0.39\n    n: 586 channels\n  expected:\n  - quantity: mean slope, load 1\n    value: -1.7526\n    tolerance: 0.3902\n  - quantity: mean slope, load 3\n    value: -1.7517\n    tolerance: 0.3928\n  criterion: A claim of absence. The frequency range and the spectral estimate for the slope are\n    not given. Readings are a linear fit of log power on log frequency of the Welch spectrum of\n    the 0 to 2.5 s maintenance window over (a) 2 to 150 Hz; (b) 30 to 150 Hz. Tolerance is the\n    reported s.d. Reproduced when the paired permutation t-test gives p >= 0.05; not reproduced\n    when it gives p < 0.05.\n- id: category-cell-counts\n  statement: Category neurons were found above chance in the hippocampus (89, 24.72%), amygdala\n    (181, 36.49%) and vmPFC (37, 17.96%), but not in the pre-SMA and dACC.\n  source: Results, Category cells support WM maintenance, paragraph 1; Extended Data Fig. 4a\n  quote: We identified such cells at numbers higher than expected by chance within the\n    hippocampus (89 neurons (24.72%)), amygdala (181 neurons (36.49%)) and vmPFC (37 neurons\n    (17.96%)) but not within the pre-SMA and dACC\n  statistics:\n  - test: right-sided permutation test, 500 label shuffles\n    p: 0.002\n    corrected: Bonferroni over five areas (99th percentile)\n    n: hippocampus, amygdala and vmPFC\n  expected:\n  - quantity: hippocampal category neurons\n    value: 89\n    tolerance: 8.9\n  - quantity: amygdala category neurons\n    value: 181\n    tolerance: 18.1\n  - quantity: vmPFC category neurons\n    value: 37\n    tolerance: 3.7\n  - quantity: pre-SMA category neurons\n    value: 18\n    tolerance: 1.8\n  - quantity: dACC category neurons\n    value: 14\n    tolerance: 1.4\n  criterion: Selection as in NWB_calcSelective_SB.m, which matches the Methods. Spike rate 0.2 to\n    1.0 s after the onset of every encoding picture and of the probe, all trials; category is the\n    first digit of the picture ID; a permutation one-way ANOVA over categories (statcond, 2,000\n    permutations) with p < 0.05, then an unpaired permutation t-test (2,000) of the category with\n    the highest mean rate against all other presentations with two-sided p < 0.1 (one-sided 0.05).\n    Chance by shuffling category labels across presentations 500 times; significant above the\n    99th percentile. The pre-SMA and dACC counts are from Extended Data Fig. 4b. Reproduced when\n    the three areas exceed the 99th percentile, pre-SMA and dACC do not, and the counts are\n    within tolerance.\n- id: fig3b-persistent-activity\n  statement: MTL category neurons stayed above baseline during maintenance in both preferred and\n    non-preferred trials, and fired more when their preferred category was held in memory.\n  source: Results, Category cells support WM maintenance, paragraph 1; Figure 3b\n  quote: Category neurons ( n = 270) remained active (preferred (pref.) versus baseline (bsl), P =\n    0.0001; non-preferred (non-pref.), P = 0.0001) and retained their selectivity during the\n    maintenance period, with FRs higher for preferred compared with non-preferred categories ( P\n    = 0.001)\n  statistics:\n  - about: preferred against baseline\n    test: two-sided permutation-based t-test\n    p: 0.0001\n    n: 270 neurons\n  - about: non-preferred against baseline\n    test: two-sided permutation-based t-test\n    p: 0.0001\n    n: 270 neurons\n  - about: preferred against non-preferred\n    test: two-sided permutation-based t-test\n    statistic: t269 = 2.93\n    p: 0.001\n    n: 270 neurons\n  depends_on:\n  - category-cell-counts\n  criterion: Hippocampal and amygdala category neurons pooled; per neuron the mean maintenance\n    rate over correct preferred trials (G4), over correct non-preferred trials, and the mean\n    baseline rate over all correct trials (G3); paired permutation t-tests over neurons, under\n    both readings of O6 (for b the baseline is 0% by definition, so the first two tests are\n    one-sample tests against zero). Reproduced when all three tests give p < 0.05 with\n    maintenance above baseline and preferred above non-preferred under both readings.\n- id: edf4b-persistent-activity-by-area\n  statement: Persistent and selective maintenance activity of category neurons held in the\n    hippocampus and amygdala separately, but vmPFC category neurons returned to baseline and did\n    not differ between preferred and non-preferred trials.\n  source: Extended Data Fig. 4b legend\n  quote: The activity of category neurons in the vmPFC (right) during the delay period was not\n    significantly larger than that during baseline (n = 37; pref.: p = 0.12; non-pref.: p =\n    0.26). Also, their FRs did not differ significantly between when the preferred and the\n    non-preferred category of a cell was maintained in WM (t(36) = 1.03, p = 0.32, BF 01 = 3.47)\n  statistics:\n  - about: hippocampus, preferred against non-preferred\n    test: two-sided permutation-based t-test\n    p: 0.025\n    n: 89 neurons\n  - about: amygdala, preferred against non-preferred\n    test: two-sided permutation-based t-test\n    p: 0.037\n    n: 181 neurons\n  - about: vmPFC, preferred against baseline\n    test: two-sided permutation-based t-test\n    p: 0.12\n    n: 37 neurons\n  - about: vmPFC, non-preferred against baseline\n    test: two-sided permutation-based t-test\n    p: 0.26\n    n: 37 neurons\n  - about: vmPFC, preferred against non-preferred\n    test: two-sided permutation-based t-test\n    statistic: t(36) = 1.03\n    p: 0.32\n    n: 37 neurons\n  depends_on:\n  - category-cell-counts\n  criterion: The tests of fig3b-persistent-activity per area. Reproduced when, in the hippocampus\n    and amygdala, all three tests give p < 0.05 in the paper's direction, and in the vmPFC none\n    does (the vmPFC part is a claim of absence on the same tests); partially reproduced when one\n    of the two parts holds.\n- id: fig3c-category-load\n  statement: In preferred trials, MTL category neurons fired more during maintenance in load 1\n    than in load 3, while no load effect appeared in non-preferred trials.\n  source: Results, Category cells support WM maintenance, paragraph 2; Figure 3c; Extended Data\n    Fig. 5a\n  quote: The activity of category neurons in the MTL was modulated by load, with FRs higher in\n    load 1 than in load 3 in preferred trials ( t 269 = 2.65, P = 0.004; Fig. 3c ), but not in\n    non-preferred trials ( t 269 = −1.46, P = 0.14\n  statistics:\n  - about: preferred trials, load 1 against load 3\n    test: two-sided permutation-based t-test\n    statistic: t269 = 2.65\n    p: 0.004\n    n: 270 neurons\n  - about: non-preferred trials, load 1 against load 3\n    test: two-sided permutation-based t-test\n    statistic: t269 = -1.46\n    p: 0.14\n    n: 270 neurons\n  depends_on:\n  - category-cell-counts\n  criterion: Per neuron the mean maintenance rate in correct preferred load 1 and correct\n    preferred load 3 trials (G4), and the same for non-preferred trials; paired permutation\n    t-tests, both readings of O6. Reproduced when the preferred test gives p < 0.05 with load 1\n    higher and the non-preferred test gives p >= 0.05; partially reproduced when only the first\n    holds.\n- id: fig3d-category-correct-incorrect\n  statement: MTL category neurons fired more during maintenance in correct than in incorrect\n    trials.\n  source: Results, Category cells support WM maintenance, paragraph 2; Figure 3d\n  quote: FRs were higher in correct as compared to incorrect trials across both load conditions (\n    t 245 = 2.43, P = 0.02\n  statistics:\n  - test: two-sided permutation-based t-test\n    statistic: t245 = 2.43\n    p: 0.02\n    n: 246 neurons\n  expected:\n  - quantity: neurons with enough incorrect trials\n    value: 246\n    tolerance: 24.6\n  depends_on:\n  - category-cell-counts\n  criterion: Per neuron the mean maintenance rate over correct and over incorrect trials of both\n    loads. The trials are not specified; readings are (a) all trials; (b) preferred trials only.\n    Neurons without enough incorrect trials are left out (O7). Reproduced when, under a reading\n    of each, the paired permutation t-test gives p < 0.05 with correct higher; the n is reported.\n- id: category-no-rt-effect\n  statement: Category neuron maintenance rates did not differ between fast and slow RT trials in\n    the hippocampus or amygdala.\n  source: Results, Category cells support WM maintenance, paragraph 2\n  quote: There was no significant difference in the FRs between fast and slow RT trials (median\n    split; computed per load condition and then averaged across loads for the preferred category\n    and correct trials only; hippocampus, t 88 = 0.73, P = 0.47; amygdala, t 180 = 1.38, P =\n    0.18)\n  statistics:\n  - about: hippocampus\n    test: two-sided permutation-based t-test\n    statistic: t88 = 0.73\n    p: 0.47\n    n: 89 neurons\n  - about: amygdala\n    test: two-sided permutation-based t-test\n    statistic: t180 = 1.38\n    p: 0.18\n    n: 181 neurons\n  depends_on:\n  - category-cell-counts\n  criterion: A claim of absence. Correct preferred trials, median split of RT within each load,\n    fast and slow rates averaged over loads, paired permutation t-test per area. Reproduced when\n    both areas give p >= 0.05; not reproduced when either gives p < 0.05.\n- id: fig3f-gamma-sfc-preferred\n  statement: Hippocampal category neurons paired with PAC channels were more strongly phase-locked\n    to local high-gamma LFP when their preferred category was held in memory; no such effect held\n    in the amygdala, for non-PAC channels or in the theta band.\n  source: Results, Category cells support WM maintenance, paragraph 3; Figure 3f; Extended Data\n    Fig. 5e\n  quote: In the hippocampus, high-gamma-band SFC was significantly stronger in preferred trials than\n    in non-preferred trials for neuron-to-channel combinations that involved significant PAC\n    channels (cluster P = 0.004; Fig. 3f )\n  statistics:\n  - test: two-sided cluster-based permutation t-test\n    p: 0.004\n    corrected: Bonferroni over two MTL areas\n    n: 151 neuron-channel combinations\n  depends_on:\n  - category-cell-counts\n  - fig2b-pac-channel-proportions\n  criterion: SFC as in the Methods (SFC). LFP phase from 40 complex Morlet wavelets, 2 to 150 Hz\n    in log steps, 3 to 10 cycles in log steps, on -0.5 to 3 s epochs cut to 0 to 2.5 s; spikes in\n    correct trials subsampled to equal counts in the two conditions (at least 10 per condition),\n    500 subsamples, mean vector length averaged; computed within each load and averaged over\n    loads; z-scored within condition against 500 surrogates (O8). Pairs are each category neuron\n    with every significant PAC channel (fig2b) in the same bundle. Cluster test over the 40\n    frequencies (G2) with alpha 0.025/2. Reproduced when, under both readings of O8, the\n    hippocampus has a cluster with preferred above non-preferred that overlaps 70 to 140 Hz, and\n    the amygdala and the hippocampal non-PAC channel pairs have no gamma cluster.\n- id: fig3g-gamma-sfc-anova\n  statement: Gamma (70-140 Hz) SFC of hippocampal category neurons was stronger in preferred than\n    non-preferred trials in both loads, with no main effect of load and no interaction.\n  source: Figure 3g legend; Results, Category cells support WM maintenance, paragraph 3\n  quote: Gamma (70–140 Hz) SFC for hippocampal category neurons was stronger for preferred versus\n    non-preferred trials in both load conditions (main effect preference, F 1,150 = 16.23, P =\n    0.0001; load 1, P = 0.003; load 3, P = 0.004). No main effect of load ( P = 0.25) or\n    interaction ( P = 0.33) was found\n  statistics:\n  - about: main effect of preference\n    test: permutation-based 2 x 2 ANOVA\n    statistic: F1,150 = 16.23\n    p: 0.0001\n    n: 151 neuron-channel pairs\n  - about: load 1, preferred against non-preferred\n    test: two-sided permutation-based t-test\n    statistic: t150 = 3.14\n    p: 0.003\n  - about: load 3, preferred against non-preferred\n    test: two-sided permutation-based t-test\n    statistic: t150 = 2.88\n    p: 0.004\n  - about: main effect of load\n    test: permutation-based 2 x 2 ANOVA\n    p: 0.25\n  - about: interaction\n    test: permutation-based 2 x 2 ANOVA\n    p: 0.33\n  depends_on:\n  - fig3f-gamma-sfc-preferred\n  criterion: The SFC of fig3f, z-scored, averaged over the wavelets with centres in 70 to 140 Hz,\n    in each load and preference (not averaged over loads); a 2 x 2 repeated-measures permutation\n    ANOVA (statcond, paired) and paired t-tests per load. Reproduced when the preference effect\n    and both per-load tests give p < 0.05 with preferred higher, and load and interaction give\n    p >= 0.05; partially reproduced when the preference effect holds and another part does not.\n- id: edf5d-sfc-high-gamma-power\n  statement: The preferred against non-preferred difference in gamma SFC held only for spikes\n    during high hippocampal gamma power, not during low gamma power.\n  source: Results, Category cells support WM maintenance, paragraph 3; Extended Data Fig. 5d\n  quote: SFC was different between preferred and non-preferred trials only for spikes that\n    occurred during high ( t 150 = 3.06, P = 0.002) but not low high-gamma band power in the\n    hippocampus ( t 150 = 0.26, P = 0.85\n  statistics:\n  - about: high gamma power\n    test: two-sided permutation-based t-test\n    statistic: t150 = 3.06\n    p: 0.002\n    n: 151 neuron-channel pairs\n  - about: low gamma power\n    test: two-sided permutation-based t-test\n    statistic: t150 = 0.26\n    p: 0.85\n    n: 151 neuron-channel pairs\n  depends_on:\n  - fig3f-gamma-sfc-preferred\n  criterion: Gamma amplitude (70 to 140 Hz) at each spike, median split across trials per pair;\n    gamma SFC as in fig3g-gamma-sfc-anova for the spikes of each half, spike counts equalized.\n    Reproduced when the high-power test gives p < 0.05 with preferred higher and the low-power\n    test gives p >= 0.05.\n- id: edf5c-theta-sfc-null\n  statement: Theta-band (3-7 Hz) SFC of hippocampal category neurons with PAC channels showed no\n    effect of load or preference and no interaction.\n  source: Extended Data Fig. 5c legend; Results, Category cells support WM maintenance, paragraph\n    3\n  quote: When averaging theta band (3–7 Hz) SFC values for hippocampal category neurons paired\n    with significant PAC channels, we did not observe a significant main effect for load or\n    preference nor a significant interaction\n  depends_on:\n  - fig3f-gamma-sfc-preferred\n  criterion: A claim of absence. The ANOVA of fig3g-gamma-sfc-anova on the wavelets with centres\n    in 3 to 7 Hz. Reproduced when no effect gives p < 0.05.\n- id: edf5fg-gamma-sfc-all-channels-patients\n  statement: The gamma SFC preference effect of hippocampal category neurons held across all\n    channels, not only PAC channels, and at the patient level.\n  source: Extended Data Fig. 5f and 5g legends\n  quote: Patient-averaged gamma SFC was significantly higher for preferred trials, suggesting that\n    the effect was not driven by a few channels or patients (n = 19, t(18) = 2.8512, p = 0.005)\n  statistics:\n  - about: all channels, hippocampus\n    test: two-sided cluster-based permutation t-test\n    p: 0.007\n    corrected: Bonferroni over two MTL areas\n  - about: patient averages\n    test: two-sided permutation-based t-test\n    statistic: t(18) = 2.8512\n    p: 0.005\n    n: 19 patients\n  depends_on:\n  - fig3f-gamma-sfc-preferred\n  criterion: Panel f, the cluster test of fig3f with every channel of the bundle; panel g, gamma\n    SFC averaged over pairs within patient, paired test over patients. Reproduced when both give\n    p < 0.05 with preferred higher.\n- id: fig3h-pac-category-firing\n  statement: Trial by trial, single-trial theta-high-gamma PAC was weakly positively related to\n    the spike count of hippocampal category neurons, but not of amygdala category neurons.\n  source: Results, Category cells support WM maintenance, paragraph 4; Figure 3h; Supplementary\n    Table S3\n  quote: In the hippocampus, PAC was weakly but significantly positively correlated with the FR of\n    category neurons\n  statistics:\n  - about: hippocampus, SC term\n    test: mixed-effects GLM\n    statistic: estimate 0.002, t = 2.40\n    p: 0.017\n    n: 151 neuron-channel combinations\n  - about: amygdala, SC term\n    test: mixed-effects GLM\n    statistic: estimate -0.001, t = -0.75\n    p: 0.45\n    n: 423 neuron-channel combinations\n  depends_on:\n  - fig3f-gamma-sfc-preferred\n  criterion: Correct trials of each category neuron paired with each significant PAC channel of\n    its bundle; PAC ~ 1 + SC + load + SC*load + (1|patientID) + (1|patientID:neuron-channelID),\n    normal response (Table S3), SC the spike count in 0 to 2.5 s, single-trial PAC under each\n    reading of O5. The trials are not restricted in the text; readings are (a) all correct\n    trials; (b) correct preferred trials. Reproduced when, under the readings, the hippocampal SC\n    term is positive with p < 0.05 and the amygdala term has p >= 0.05; methods_underspecified\n    when they disagree.\n- id: pac-neuron-counts\n  statement: 79 of 212 hippocampal neurons (37.29%) and 163 of 358 amygdala neurons (45.53%)\n    qualified as PAC neurons, more than expected by chance.\n  source: Results, Category neurons are not PAC neurons, paragraph 1; Figure 4a, b\n  quote: In the hippocampus, 79 (37.29%) out of 212 available neurons ( P < 0.005; 200 permutations\n    ( Methods ); pre-processing steps removed broadband LFPs for some of the neurons and those\n    were therefore not part of this analysis) qualified as PAC neurons. In the amygdala, 163\n    (45.53%) out of 358 neurons ( P < 0.005) qualified as PAC neurons\n  statistics:\n  - about: hippocampus\n    test: permutation test, 200 trial re-pairings of spikes and LFP\n    p: 0.005\n    p_relation: <\n    n: 212 neurons\n  - about: amygdala\n    test: permutation test, 200 trial re-pairings of spikes and LFP\n    p: 0.005\n    p_relation: <\n    n: 358 neurons\n  expected:\n  - quantity: hippocampal PAC neurons\n    value: 79\n    tolerance: 7.9\n  - quantity: amygdala PAC neurons\n    value: 163\n    tolerance: 16.3\n  criterion: Selection as in plot_PAC_neuron.m and the Methods (Selection of PAC neurons). For each\n    MTL neuron and each LFP channel of its bundle, correct trials of one load, -0.5 to 3 s\n    epochs (the code uses -1.5 to 4 s; both are cut to 0 to 2.5 s); theta phase from a 3-7 Hz\n    pop_eegfiltnew filter and Hilbert transform; gamma amplitude from 7-cycle Morlet wavelets at\n    70 to 140 Hz in 5 Hz steps, each z-scored over the concatenated samples and averaged; median\n    split of gamma; 10 phase bins; spike counts in the 20 bins; Poisson GLMs (fitglme, Laplace)\n    with the bin's left phase edge as cos and sin terms; likelihood-ratio tests of model 1 against\n    models 2 and 3, both p < 0.01 after FDR (O9). A neuron qualifies through any channel in\n    either load. Chance from 200 runs with spikes and LFP paired from random trials. Artefact\n    trials as in O1. Reproduced when, under the readings, both areas exceed every shuffled count\n    (or all but 1 of 200) and the counts are within tolerance; partially reproduced when the\n    counts are out of tolerance and the shuffle test holds. The number of neurons with LFP in\n    their bundle is reported against 212 and 358.\n- id: pac-category-overlap\n  statement: The overlap of PAC and category neurons (28 of 79 in the hippocampus, 68 of 163 in\n    the amygdala) did not exceed that expected of independent populations.\n  source: Results, Category neurons are not PAC neurons, paragraph 2; Figure 4b\n  quote: In the hippocampus, 28 (35.44%) out of the 79 PAC neurons were both PAC neurons as well as\n    category neurons. In the amygdala, this was the case for 68 (41.72%) out of the 163 PAC\n    neurons (Fig. 4b ). The proportion of category neurons among PAC neurons was not\n    significantly higher than expected by independent subpopulations in any of the two regions\n    (both P > 0.05\n  statistics:\n  - test: test against independent subpopulations\n    p: 0.05\n    p_relation: '>'\n    n: 79 hippocampal and 163 amygdala PAC neurons\n  expected:\n  - quantity: hippocampal PAC neurons that are category neurons\n    value: 28\n    tolerance: 2.8\n  - quantity: amygdala PAC neurons that are category neurons\n    value: 68\n    tolerance: 6.8\n  depends_on:\n  - pac-neuron-counts\n  - category-cell-counts\n  criterion: A claim of absence. The test is not named. Readings are (a) a right-sided binomial\n    test of the overlap against the product of the two proportions among the analysed neurons;\n    (b) a right-sided hypergeometric (Fisher) test. Reproduced when the test gives p >= 0.05 in\n    both areas; not reproduced when it gives p < 0.05 in either.\n- id: edf7a-pac-neurons-no-category-decoding\n  statement: Category could be decoded from encoding-period rates of category neurons\n    (hippocampus 72.77%, amygdala 88.71%) but not from PAC neurons that are not category neurons\n    (26.06% and 25.86%, chance 20%).\n  source: Results, Category neurons are not PAC neurons, paragraph 2; Extended Data Fig. 7a\n  quote: the decoder was able to differentiate between the picture categories when it was trained\n    on FRs from the category neurons (hippocampus, 72.77%, P = 0.001; amygdala, 88.71%, P =\n    0.001; Extended Data Fig. 7a ). However, the decoder could not differentiate between the\n    categories when it was trained on FRs from PAC neurons that were not also category neurons in\n    both MTL areas (hippocampus, 26.06%, P = 0.16; amygdala, 25.86%, P = 0.15; chance level = 20%)\n  statistics:\n  - about: hippocampal category neurons\n    test: right-sided permutation test, 1,000 label shuffles\n    p: 0.001\n  - about: amygdala category neurons\n    test: right-sided permutation test, 1,000 label shuffles\n    p: 0.001\n  - about: hippocampal PAC-only neurons\n    test: right-sided permutation test, 1,000 label shuffles\n    p: 0.16\n  - about: amygdala PAC-only neurons\n    test: right-sided permutation test, 1,000 label shuffles\n    p: 0.15\n  expected:\n  - quantity: decoding accuracy, hippocampal category neurons\n    value: 72.77\n    tolerance: 7.28\n    unit: '%'\n  - quantity: decoding accuracy, amygdala category neurons\n    value: 88.71\n    tolerance: 8.87\n    unit: '%'\n  - quantity: decoding accuracy, hippocampal PAC-only neurons\n    value: 26.06\n    tolerance: 2.61\n    unit: '%'\n  - quantity: decoding accuracy, amygdala PAC-only neurons\n    value: 25.86\n    tolerance: 2.59\n    unit: '%'\n  depends_on:\n  - pac-neuron-counts\n  - category-cell-counts\n  criterion: Pseudo-populations across sessions (legend), linear SVM as in O11 on rates 0.2 to 1.0\n    s after each encoding picture (the selection window), trials per category subsampled to the\n    smallest count across neurons, 1,000 repetitions, accuracy the mean; null from 1,000 label\n    shuffles. Which encoding presentations enter is not stated; readings are (a) all encoding\n    pictures of both loads; (b) encoding 1 of load 1 trials. Reproduced when, under a reading,\n    category neurons decode above the null (p < 0.05) in both areas, PAC-only neurons do not, and\n    the accuracies are within tolerance; partially reproduced when the pattern holds without the\n    values.\n- id: fig4c-pac-neuron-firing-single-trial-pac\n  statement: Spike counts of hippocampal PAC neurons were positively related to single-trial\n    theta-high-gamma PAC on their selected channel; amygdala PAC neurons showed no relation.\n  source: Results, Properties of PAC neurons, paragraph 1; Figure 4c, d; Supplementary Table S4\n  quote: FRs of PAC neurons were positively correlated with single-trial estimates of TG-PAC in the\n    hippocampus ( c ; n = 79, P = 0.028, mixed-effects GLM), but not in the amygdala ( d ; n =\n    163, P = 0.98\n  statistics:\n  - about: hippocampus, SC term\n    test: mixed-effects GLM\n    statistic: estimate 0.0032, t = 2.19\n    p: 0.028\n    n: 79 neurons\n  - about: amygdala, SC term\n    test: mixed-effects GLM\n    statistic: estimate -3e-5, t = -0.02\n    p: 0.98\n    n: 163 neurons\n  depends_on:\n  - pac-neuron-counts\n  criterion: Correct trials, each PAC neuron with its selected channel (highest model 1 R2, Methods);\n    the GLM of fig3h-pac-category-firing with random intercepts for neuron-channel pair nested in\n    patient (Methods, Properties of PAC neurons), single-trial PAC under each reading of O5.\n    Reproduced when, under the readings, the hippocampal SC term is positive with p < 0.05 and the\n    amygdala term has p >= 0.05; methods_underspecified when they disagree.\n- id: fig4e-hippocampus-pac-neurons-accuracy\n  statement: Hippocampal PAC neurons fired above baseline during maintenance, more in correct than\n    in incorrect trials, and above baseline in correct trials only.\n  source: Results, Properties of PAC neurons, paragraph 1; Figure 4e\n  quote: Second, their FR was elevated throughout the maintenance period compared with the\n    baseline ( t 78 = 2.43, P = 0.01). Third, FRs varied as a function of accuracy (correct versus\n    incorrect trials ( t 62 = 3.82, P < 0.001\n  statistics:\n  - about: maintenance against baseline\n    test: two-sided permutation-based t-test\n    statistic: t78 = 2.43\n    p: 0.01\n    n: 79 neurons\n  - about: correct against incorrect\n    test: two-sided permutation-based t-test\n    statistic: t62 = 3.82\n    p: 0.0001\n    n: 63 neurons\n  - about: correct against baseline\n    test: two-sided permutation-based t-test\n    statistic: t62 = 2.67\n    p: 0.01\n    n: 63 neurons\n  - about: incorrect against baseline\n    test: two-sided permutation-based t-test\n    statistic: t62 = -0.98\n    p: 0.33\n    n: 63 neurons\n  expected:\n  - quantity: neurons with enough incorrect trials\n    value: 63\n    tolerance: 6.3\n  depends_on:\n  - pac-neuron-counts\n  criterion: Maintenance against baseline over all correct trials; correct against incorrect over\n    all trials of both loads, neurons without enough incorrect trials left out (O7); both\n    readings of O6. Reproduced when the first three tests give p < 0.05 in the paper's direction\n    and the incorrect against baseline test gives p >= 0.05; partially reproduced when the\n    correct against incorrect test holds and another part does not.\n- id: fig4g-hippocampus-pac-neurons-load\n  statement: Hippocampal PAC neuron rates did not differ between loads but were above baseline in\n    each load; they also did not differ between fast and slow RT trials.\n  source: Results, Properties of PAC neurons, paragraph 1; Figure 4g\n  quote: FRs were not significantly different between the two load conditions (load 3 − load 1,\n    t 78 = 1.38, P = 0.20), but FRs were elevated compared with the baseline in each condition\n    considered separately (load 1, t 78 = 2.14, P = 0.03; load 3, t 78 = 2.45, P = 0.01\n  statistics:\n  - about: load 3 against load 1\n    test: two-sided permutation-based t-test\n    statistic: t78 = 1.38\n    p: 0.2\n    n: 79 neurons\n  - about: load 1 against baseline\n    test: two-sided permutation-based t-test\n    statistic: t78 = 2.14\n    p: 0.03\n  - about: load 3 against baseline\n    test: two-sided permutation-based t-test\n    statistic: t78 = 2.45\n    p: 0.01\n  - about: fast against slow RT\n    test: two-sided permutation-based t-test\n    statistic: t78 = -0.07\n    p: 0.94\n  depends_on:\n  - pac-neuron-counts\n  criterion: Correct trials; the load and RT parts are claims of absence (RT median split within\n    load, averaged over loads). Reproduced when both baseline tests give p < 0.05 with\n    maintenance higher and the load and RT tests give p >= 0.05; partially reproduced when one\n    part fails.\n- id: fig4-amygdala-pac-neurons\n  statement: Amygdala PAC neurons fired above baseline during maintenance but did not differ\n    between correct and incorrect trials, loads, or fast and slow RT trials.\n  source: Results, Properties of PAC neurons, paragraph 2; Figure 4f, h\n  quote: PAC neurons in the amygdala also showed higher FRs during the maintenance period compared\n    with the baseline ( t 162 = 6.40, P < 0.001), but there were no significant differences\n    between correct and incorrect WM trials ( t 156 = −0.77, P = 0.45; Fig. 4f ), loads (load 3 −\n    load 1, t 162 = 0.26, P = 0.80\n  statistics:\n  - about: maintenance against baseline\n    test: two-sided permutation-based t-test\n    statistic: t162 = 6.40\n    p: 0.001\n    p_relation: <\n    n: 163 neurons\n  - about: correct against incorrect\n    test: two-sided permutation-based t-test\n    statistic: t156 = -0.77\n    p: 0.45\n    n: 156 neurons\n  - about: load 3 against load 1\n    test: two-sided permutation-based t-test\n    statistic: t162 = 0.26\n    p: 0.8\n  - about: fast against slow RT\n    test: two-sided permutation-based t-test\n    statistic: t162 = 1.87\n    p: 0.07\n  depends_on:\n  - pac-neuron-counts\n  criterion: As fig4e and fig4g for amygdala PAC neurons. Reproduced when the baseline test gives\n    p < 0.05 with maintenance higher and the three others give p >= 0.05; partially reproduced\n    when one part fails.\n- id: edf7bc-pac-neuron-local-sfc\n  statement: Local theta and gamma SFC of PAC neurons did not differ between loads in the\n    hippocampus or amygdala, though both exceeded shuffled surrogates.\n  source: Extended Data Fig. 7b, c legends\n  quote: Theta and gamma SFC between PAC neurons and local LFP recordings did not differ as a\n    function of load in ( b ) the hippocampus (theta, t(78) = −1.54, p = 0.13; gamma, t(78) =\n    −1.12, p = 0.27, n = 79), or ( c ) the amygdala (theta, t(162) = −0.71, p = 0.47; gamma,\n    t(162) = 0.76, p = 0.45, n = 163)\n  statistics:\n  - about: hippocampus theta\n    test: two-sided permutation-based t-test\n    statistic: t(78) = -1.54\n    p: 0.13\n  - about: hippocampus gamma\n    test: two-sided permutation-based t-test\n    statistic: t(78) = -1.12\n    p: 0.27\n  - about: amygdala theta\n    test: two-sided permutation-based t-test\n    statistic: t(162) = -0.71\n    p: 0.47\n  - about: amygdala gamma\n    test: two-sided permutation-based t-test\n    statistic: t(162) = 0.76\n    p: 0.45\n  - about: against shuffled surrogates, all\n    test: two-sided permutation-based t-test\n    p: 0.0001\n  depends_on:\n  - pac-neuron-counts\n  criterion: SFC as in fig3f (at least 50 spikes per condition) between each PAC neuron and its\n    selected channel, per load, averaged over 3-7 Hz and 70-140 Hz. The load part is a claim of\n    absence. Reproduced when the four load tests give p >= 0.05 and the z-scored SFC exceeds\n    zero (the surrogate mean) with p < 0.05 in every band and area.\n- id: fig5b-hippocampus-vmpfc-theta-sfc-load\n  statement: Spikes of hippocampal PAC neurons were more strongly phase-locked to vmPFC theta LFP\n    (2.5-4.3 Hz) in load 3 than in load 1, with no such effect for other frequencies or for\n    pre-SMA and dACC LFPs.\n  source: Results, PAC neurons phase lock to the frontal cortex, paragraph 1; Figure 5b; Extended\n    Data Fig. 8a\n  quote: SFC was significantly stronger in load 3 compared with load 1 between spiking activity of\n    PAC neurons in the hippocampus and theta-band LFPs recorded in the vmPFC (Fig. 5b and Methods\n    ; cluster P < 0.001). We did not observe significant differences for other frequency bands,\n    nor for the other two frontal brain areas\n  statistics:\n  - test: two-sided cluster-based permutation t-test\n    p: 0.0001\n    corrected: Bonferroni over two MTL areas, three frontal areas and two cell populations\n    n: 175 connections\n  expected:\n  - quantity: hippocampal PAC neuron to vmPFC channel connections\n    value: 175\n    tolerance: 17.5\n  depends_on:\n  - pac-neuron-counts\n  criterion: SFC as in fig3f between each hippocampal PAC neuron and every LFP channel of each\n    frontal area in the same hemisphere, at least 50 spikes per load, per load (no averaging over\n    loads), both readings of O8; cluster test over 40 frequencies with alpha 0.025/12 (G2).\n    Reproduced when vmPFC has a cluster with load 3 higher within 2 to 8 Hz and no other\n    cluster, and pre-SMA and dACC have none; partially reproduced when the vmPFC theta cluster\n    holds and another cluster appears.\n- id: fig5cd-no-effect-category-amygdala\n  statement: Hippocampal category neurons and amygdala PAC neurons showed no load difference in SFC\n    to vmPFC LFP.\n  source: Figure 5c, d legends; Results, PAC neurons phase lock to the frontal cortex, paragraph 1\n  quote: Category neurons from the hippocampus ( c ; n = 215) or PAC neurons from the amygdala ( d\n    ; n = 767) did not show significant SFC differences between loads relative to the vmPFC LFP\n  depends_on:\n  - fig5b-hippocampus-vmpfc-theta-sfc-load\n  criterion: A claim of absence. The test of fig5b for hippocampal category neurons and for\n    amygdala PAC neurons with vmPFC (and the other frontal areas for amygdala PAC neurons).\n    Reproduced when no cluster is significant at 0.025/12; not reproduced when one is.\n- id: fig5e-random-subsets\n  statement: The theta SFC load difference of hippocampal PAC neurons to vmPFC was larger than for\n    every one of 10,000 random sets of hippocampus-vmPFC connections.\n  source: Figure 5e legend; Results, PAC neurons phase lock to the frontal cortex, paragraph 1\n  quote: Hippocampal PAC cells ( n = 175, cyan line) yielded the strongest long-range theta SFC\n    difference between load 3 and load 1 trials among 10,000 random selections of\n    hippocampus–vmPFC connections ( P = 0.0001, right-sided permutation test)\n  statistics:\n  - test: right-sided permutation test, 10,000 random selections\n    p: 0.0001\n    n: 175 connections\n  depends_on:\n  - fig5b-hippocampus-vmpfc-theta-sfc-load\n  criterion: The t value of load 3 against load 1 for SFC averaged over 2.5 to 4.3 Hz, for the PAC\n    neuron connections and for 10,000 random sets of the same number of connections from all\n    hippocampal neurons. Reproduced when the PAC neuron t exceeds at least 95% of the random t\n    values.\n- id: fig5f-theta-sfc-rt\n  statement: Theta SFC between hippocampal PAC neurons and vmPFC was stronger in fast than in slow\n    RT trials; amygdala PAC neurons showed no such effect.\n  source: Results, PAC neurons phase lock to the frontal cortex, paragraph 1; Figure 5f\n  quote: theta SFC was stronger for fast compared with slow RTs for PAC neurons from the\n    hippocampus ( t 166 = 2.10, P = 0.03; Fig. 5f ), but not from the amygdala ( t 705 = 1.40, P\n    = 0.16)\n  statistics:\n  - about: hippocampus\n    test: two-sided permutation-based t-test\n    statistic: t166 = 2.10\n    p: 0.03\n    n: 167 connections\n  - about: amygdala\n    test: two-sided permutation-based t-test\n    statistic: t705 = 1.40\n    p: 0.16\n    n: 706 connections\n  depends_on:\n  - fig5b-hippocampus-vmpfc-theta-sfc-load\n  criterion: Median split of RT among correct trials within each load; SFC computed in fast and in\n    slow trials within each load and averaged over loads, averaged over 2.5 to 4.3 Hz; paired\n    permutation t-test over connections with enough spikes (the minimum is not stated for this\n    test; readings are 50 spikes per condition, as for SFC in general, and 10). Reproduced when\n    the hippocampal test gives p < 0.05 with fast higher and the amygdala test p >= 0.05.\n- id: edf8b-vmpfc-sfc-patients\n  statement: At the patient level, theta SFC between hippocampal PAC neurons and vmPFC was higher\n    in load 3 than in load 1.\n  source: Extended Data Fig. 8b legend\n  quote: At the patient-level, theta cross-regional SFC was significantly higher for load 3 than\n    load 1 trials, suggesting that the effect was not driven by a few channels or patients (n =\n    20; t(19) = −2.8297, p = 0.0071)\n  statistics:\n  - test: two-sided permutation-based t-test\n    statistic: t(19) = -2.8297\n    p: 0.0071\n    n: 20 patients\n  depends_on:\n  - fig5b-hippocampus-vmpfc-theta-sfc-load\n- id: edf8c-pac-against-category\n  statement: The load modulation of hippocampus-vmPFC theta SFC was stronger for PAC neurons than\n    for category neurons.\n  source: Extended Data Fig. 8c legend\n  quote: the load modulation of cross-regional theta SFC between hippocampal neurons and vmPFC\n    LFPs was significantly stronger for PAC than for category neurons (PAC, n = 175, Cat, n = 215;\n    t(376.07) = 3.3942, p = 0.0001; unpaired two-sided permutation t -test)\n  statistics:\n  - test: unpaired two-sided permutation t-test\n    statistic: t(376.07) = 3.3942\n    p: 0.0001\n    n: 175 PAC and 215 category neuron connections\n  depends_on:\n  - fig5b-hippocampus-vmpfc-theta-sfc-load\n  criterion: Per connection the load 3 minus load 1 SFC averaged over 2.5 to 4.3 Hz.\n- id: edf8de-narrow-spiking\n  statement: The load and RT effects on hippocampus-vmPFC theta SFC held for narrow-spiking PAC\n    neurons only, not broad-spiking ones.\n  source: Extended Data Fig. 8d, e legends\n  quote: we observed a significant difference in theta SFC between load 3 and load 1 only for the\n    narrow-spiking PAC neurons (trough-to-peak time <0.5 ms; n = 91 connections; cluster-p =\n    0.0001, left). No effect was found for broad-spiking PAC neurons (n = 84)\n  statistics:\n  - about: load, narrow-spiking\n    test: two-sided cluster-based permutation t-test\n    p: 0.0001\n    n: 91 connections\n  - about: RT, narrow-spiking\n    test: two-sided permutation-based t-test\n    statistic: t(90) = 3.02\n    p: 0.003\n    n: 91 connections\n  - about: RT, broad-spiking\n    test: two-sided permutation-based t-test\n    statistic: t(75) = -0.66\n    p: 0.52\n    n: 76 connections\n  depends_on:\n  - fig5b-hippocampus-vmpfc-theta-sfc-load\n  - fig5f-theta-sfc-rt\n  criterion: Narrow-spiking is a trough-to-peak time of the mean waveform below 0.5 ms. Reproduced\n    when the narrow-spiking load cluster and RT test give p < 0.05 and the broad-spiking tests do\n    not.\n- id: fig6a-noise-correlations\n  statement: Pairs of category and PAC neurons had positive noise correlations on average in both\n    the hippocampus (162 pairs) and amygdala (892 pairs), larger than after shuffling trials within\n    conditions.\n  source: Results, Information-enhancing noise correlations, paragraph 1; Figure 6a; Extended Data\n    Fig. 9a\n  quote: In both the hippocampus (162 pairs; t 161 = 5.26; P < 0.001) and the amygdala (892 pairs;\n    t 891 = 15.51; P < 0.001), pairs of category neurons and PAC neurons had on average positive\n    co-fluctuations of spike counts\n  statistics:\n  - about: hippocampus, against zero\n    test: two-sided permutation-based t-test\n    statistic: t161 = 5.26\n    p: 0.0001\n    n: 162 pairs\n  - about: amygdala, against zero\n    test: two-sided permutation-based t-test\n    statistic: t891 = 15.51\n    p: 0.0001\n    n: 892 pairs\n  - about: hippocampus, against within-condition trial shuffles\n    test: right-sided permutation test, 1,000 shuffles\n    p: 0.001\n    n: 162 pairs\n  expected:\n  - quantity: hippocampal category-PAC pairs\n    value: 162\n    tolerance: 16.2\n  - quantity: amygdala category-PAC pairs\n    value: 892\n    tolerance: 89.2\n  depends_on:\n  - pac-neuron-counts\n  - category-cell-counts\n  criterion: Spike counts in 200 ms bins sliding by 25 ms over 0 to 2.5 s (101 bins); per correct\n    trial the correlation across bins; averaged over trials (O10). Pairs of a category neuron and\n    a PAC neuron in the same session and area, not on the same wire. Shuffle as in the Methods\n    (trial labels shuffled within preferred or not and load, 1,000 times, mean over pairs).\n    Reproduced when, under both readings of O10, both areas give p < 0.05 above zero, the\n    hippocampal mean exceeds every shuffle (or all but 5%), and the pair counts are within\n    tolerance.\n- id: edf9ef-non-category-pac-pairs\n  statement: Noise correlations stayed positive, and above shuffles, for pairs of category neurons\n    with PAC neurons that are not category neurons.\n  source: Extended Data Fig. 9e, f legends\n  quote: Bin-wise correlations among pairs of category neurons and PAC neurons that were not also\n    category neurons were significantly positive on average in hippocampus (n = 101, p = 0.0003)\n    and amygdala (n = 555, p = 0.0001)\n  statistics:\n  - about: hippocampus\n    test: two-sided permutation-based t-test\n    p: 0.0003\n    n: 101 pairs\n  - about: amygdala\n    test: two-sided permutation-based t-test\n    p: 0.0001\n    n: 555 pairs\n  - about: hippocampus against shuffles\n    test: right-sided permutation test\n    p: 0.0001\n  depends_on:\n  - fig6a-noise-correlations\n- id: fig6c-adding-pac-neurons\n  statement: In the hippocampus, adding single PAC neurons to the optimized decoding ensemble raised\n    category decoding when noise correlations were intact but not when they were removed.\n  source: Results, Information-enhancing noise correlations, paragraph 2; Figure 6c\n  quote: adding single PAC neurons to the optimized decoding ensemble significantly enhanced\n    category decoding when noise correlations were intact ( t 20 = 3.16, P < 0.001) but not when\n    they were removed ( t 20 = −0.12, P = 0.91, BF 01 = 4.37; intact versus removed, t 20 = 3.33,\n    P = 0.003\n  statistics:\n  - about: intact\n    test: two-sided permutation-based t-test\n    statistic: t20 = 3.16\n    p: 0.0007\n    n: 21 sessions\n  - about: removed\n    test: two-sided permutation-based t-test\n    statistic: t20 = -0.12\n    p: 0.91\n    n: 21 sessions\n  - about: intact against removed\n    test: two-sided permutation-based t-test\n    statistic: t20 = 3.33\n    p: 0.003\n    n: 21 sessions\n  depends_on:\n  - pac-neuron-counts\n  - category-cell-counts\n  criterion: Decoding of the category held in load 1 correct trials from hippocampal maintenance\n    rates of each session (O11), all hippocampal neurons of the session. The per-session gain of\n    O11 (ii), tested against zero for intact and removed and between them. Sessions with at\n    least one PAC neuron added before peak. Reproduced when, under both readings of O11 (i), the\n    intact gain is above zero and above the removed gain with p < 0.05 and the removed gain has\n    p >= 0.05; methods_underspecified when the readings disagree.\n- id: fig6d-removing-pac-neurons\n  statement: Removing all PAC neurons from the hippocampal ensembles reduced maximal decoding only\n    with intact noise correlations, while removing as many non-PAC neurons reduced it with intact\n    and removed correlations.\n  source: Results, Information-enhancing noise correlations, paragraph 3; Figure 6d\n  quote: PAC neurons enhanced the decodability of category, but only when noise correlations were\n    intact ( t 21 = 2.94; P = 0.004; FDR corrected for all comparisons; Fig. 6d ). Removing PAC\n    neurons from the ensemble after noise correlations were removed did not significantly change\n    the decoding performance ( t 21 = 1.36, P = 0.20\n  statistics:\n  - about: PAC removed, intact correlations\n    test: two-sided permutation-based t-test\n    statistic: t21 = 2.94\n    p: 0.004\n    corrected: FDR over all comparisons\n    n: 22 sessions\n  - about: PAC removed, removed correlations\n    test: two-sided permutation-based t-test\n    statistic: t21 = 1.36\n    p: 0.2\n    n: 22 sessions\n  - about: non-PAC removed, intact correlations\n    test: two-sided permutation-based t-test\n    p: 0.01\n    n: 22 sessions\n  - about: non-PAC removed, removed correlations\n    test: two-sided permutation-based t-test\n    statistic: t21 = 3.89\n    p: 0.0001\n    n: 22 sessions\n  depends_on:\n  - fig6c-adding-pac-neurons\n  criterion: Per session with at least one PAC neuron and at least two neurons left after removing\n    them, the maximal accuracy of greedy ensembles before and after removing all PAC neurons, for\n    intact and removed correlations; the non-PAC control removes as many random non-PAC neurons,\n    averaged over 500 draws; paired permutation t-tests, FDR (Benjamini-Hochberg) over the four.\n    Reproduced when, under both readings of O11 (i), the PAC intact test and both non-PAC tests\n    give p < 0.05 with decoding lower after removal and the PAC removed test gives p >= 0.05.\n- id: fig6e-decoding-difference\n  statement: The gain of intact over removed noise correlations in maximal decoding was smaller\n    after removing PAC neurons, but not after removing non-PAC neurons.\n  source: Results, Information-enhancing noise correlations, paragraph 3; Figure 6e\n  quote: the maximal differences between intact and removed noise correlations were larger when PAC\n    neurons were part of the ensembles as compared to being removed ( t 21 = 3.59, P < 0.001; Fig.\n    6e )\n  statistics:\n  - about: PAC neurons\n    test: two-sided permutation-based t-test\n    statistic: t21 = 3.59\n    p: 0.0007\n    n: 22 sessions\n  - about: non-PAC neurons\n    test: two-sided permutation-based t-test\n    statistic: t21 = -1.77\n    p: 0.1\n    n: 22 sessions\n  depends_on:\n  - fig6d-removing-pac-neurons\n  criterion: From the values of fig6d. Reproduced when the PAC test gives p < 0.05 (difference\n    larger with PAC neurons) and the non-PAC test gives p >= 0.05.\n- id: edf9g-non-category-pac-decoding\n  statement: Removing only PAC neurons that are not category neurons also lowered decoding with\n    intact noise correlations only.\n  source: Extended Data Fig. 9g legend\n  quote: Like for all PAC neurons, decoding performance was enhanced by nonCatPAC neurons only when\n    noise correlations were intact (n = 23 sessions, p = 0.0005)\n  statistics:\n  - test: two-sided permutation-based t-test\n    p: 0.0005\n    n: 23 sessions\n  depends_on:\n  - fig6d-removing-pac-neurons\n- id: edf9jk-amygdala-decoding\n  statement: In the amygdala, PAC neurons raised decoding with both intact and removed noise\n    correlations, and removing them lowered decoding in both cases, as for random cells.\n  source: Results, Information-enhancing noise correlations, paragraph 3; Extended Data Fig. 9j, k\n  quote: In the amygdala, adding single PAC neurons (n = 28) to the decoding ensemble did not only\n    enhance decodability when noise correlations were intact (p = 0.0001), but also when removed\n    (p = 0.049; intact – removed, p = 0.0009)\n  statistics:\n  - about: adding, intact\n    test: two-sided permutation-based t-test\n    p: 0.0001\n    n: 28\n  - about: adding, removed\n    test: two-sided permutation-based t-test\n    p: 0.049\n  - about: adding, intact against removed\n    test: two-sided permutation-based t-test\n    p: 0.0009\n  - about: removing, intact\n    test: two-sided permutation-based t-test\n    p: 0.0001\n    n: 32 sessions\n  - about: removing, removed\n    test: two-sided permutation-based t-test\n    p: 0.0001\n    n: 32 sessions\n  depends_on:\n  - fig6c-adding-pac-neurons\n  criterion: The analyses of fig6c and fig6d on amygdala neurons. Reproduced when all five tests\n    give p < 0.05 in the paper's direction.\n- id: fig6g-signal-noise-angle\n  statement: The angle between the signal and noise axes was about 69 degrees with intact noise\n    correlations and became smaller after removing them.\n  source: Results, Information-enhancing noise correlations, paragraph 4; Figure 6g\n  quote: when noise correlations were intact, the signal–noise axis angle was around 69° (out of\n    maximally 90°). After removing noise correlations, this angle became significantly smaller,\n    as hypothesized ( t 31 = 2.77, P = 0.009\n  statistics:\n  - test: two-sided permutation-based t-test\n    statistic: t31 = 2.77\n    p: 0.009\n    n: 32 sessions\n  expected:\n  - quantity: signal-noise angle, intact\n    value: 69\n    tolerance: 6.9\n    unit: degrees\n  depends_on:\n  - fig6c-adding-pac-neurons\n  criterion: Per session with at least two hippocampal neurons, at the ensemble with the largest\n    intact minus removed decoding difference; signal axis orthogonal to each of the 10 binary SVM\n    hyperplanes (QR decomposition, as LinearClassifier_getSignalAxis.m); noise axis the first\n    principal component of the data across categories; angle as subspace() in the code (0 to 90\n    degrees), averaged over learners and 500 repetitions.\n- id: fig6h-projection-variance\n  statement: Removing PAC neurons raised the s.d. of responses projected on the signal axis, and\n    removing noise correlations raised it only while PAC neurons were in the ensemble.\n  source: Results, Information-enhancing noise correlations, paragraph 4; Figure 6h\n  quote: Removing PAC neurons from the ensembles significantly increased the s.d. of the projection\n    values (main effect for ensemble, F 1,18 = 12.55, P = 0.0013; Fig. 6h ). Moreover, the s.d.\n    of the projected values was larger when noise correlations were removed (main effect for\n    noise correlations, F 1,18 = 7.24, P = 0.014). This was only the case if PAC neurons were\n    part of the ensembles ( t 18 = −2.66, P = 0.014), and there was no significant difference\n    between intact and removed noise correlations when PAC neurons were removed ( t 18 = −1.69,\n    P = 0.11)\n  statistics:\n  - about: main effect of ensemble\n    test: permutation-based F-test (2 x 2 ANOVA)\n    statistic: F1,18 = 12.55\n    p: 0.0013\n    n: 19 sessions\n  - about: main effect of noise correlations\n    test: permutation-based F-test (2 x 2 ANOVA)\n    statistic: F1,18 = 7.24\n    p: 0.014\n    n: 19 sessions\n  - about: intact against removed, with PAC neurons\n    test: two-sided permutation-based t-test\n    statistic: t18 = -2.66\n    p: 0.014\n  - about: intact against removed, without PAC neurons\n    test: two-sided permutation-based t-test\n    statistic: t18 = -1.69\n    p: 0.11\n  depends_on:\n  - fig6g-signal-noise-angle\n  criterion: Per session with at least one hippocampal PAC neuron and two neurons left, the s.d. of\n    projections on the signal axis per class, averaged over classes, the 10 learners and 500\n    repetitions; 2 x 2 repeated-measures permutation ANOVA. Reproduced when both main effects\n    and the with-PAC test give p < 0.05 in the paper's direction and the without-PAC test gives\n    p >= 0.05.\n- id: fig6i-noise-correlations-rt\n  statement: Noise correlations of hippocampal PAC-category pairs in preferred trials were stronger\n    in fast than in slow RT trials, positive only in fast trials, and the RT difference held in\n    load 3 but not in load 1.\n  source: Results, Information-enhancing noise correlations, paragraph 5; Figure 6i\n  quote: In the hippocampus, noise correlations were significantly stronger for fast compared with\n    slow RT trials ( t 161 = 2.15, P = 0.028; Fig. 6i (left)\n  statistics:\n  - about: fast against slow\n    test: two-sided permutation-based t-test\n    statistic: t161 = 2.15\n    p: 0.028\n    n: 162 pairs\n  - about: fast against zero\n    test: two-sided permutation-based t-test\n    statistic: t161 = 4.10\n    p: 0.001\n    p_relation: <\n  - about: slow against zero\n    test: two-sided permutation-based t-test\n    statistic: t161 = 1.94\n    p: 0.06\n  - about: load 3, fast against slow\n    test: two-sided permutation-based t-test\n    statistic: t161 = 2.60\n    p: 0.009\n  - about: load 1, fast against slow\n    test: two-sided permutation-based t-test\n    statistic: t161 = 0.96\n    p: 0.34\n  depends_on:\n  - fig6a-noise-correlations\n  criterion: Correct trials with the category neuron's preferred category held; RT median split\n    within each load; correlations of fig6a averaged over the fast and over the slow trials of\n    each load, then over loads. Reproduced when the fast against slow test gives p < 0.05 with\n    fast higher; partially reproduced when that holds and the load split or the tests against\n    zero differ from the paper in significance.\n- id: edf9hil-noise-correlations-rt-controls\n  statement: The fast against slow difference was absent for non-preferred trials and in the\n    amygdala, and held at the patient level in the hippocampus.\n  source: Extended Data Fig. 9h, i, l legends\n  quote: Correlations for pairs of PAC and category neurons in preferred trials were averaged within\n    each patient and then compared between fast and slow RTs across all patients (n = 16, p =\n    0.0027)\n  statistics:\n  - about: hippocampus, non-preferred trials\n    test: two-sided permutation-based t-test\n    p: 0.9\n    n: 162 pairs\n  - about: hippocampus, patient level\n    test: two-sided permutation-based t-test\n    p: 0.0027\n    n: 16 patients\n  depends_on:\n  - fig6i-noise-correlations-rt\n  criterion: Reproduced when the patient-level test gives p < 0.05 with fast higher and the\n    hippocampal non-preferred and amygdala (884 pairs) preferred tests give p >= 0.05.\n- id: fig6j-specific-to-pac-pairs\n  statement: The fast against slow RT difference in noise correlations was larger for PAC-category\n    pairs than for random pairs of category neurons with non-PAC neurons.\n  source: Results, Information-enhancing noise correlations, paragraph 5; Figure 6j\n  quote: PAC-to-category neuron pairs showed a significantly stronger effect compared with most\n    randomly selected cell pairs ( P = 0.016; Fig. 6j )\n  statistics:\n  - test: right-sided permutation test\n    p: 0.016\n    n: 162 pairs\n  depends_on:\n  - fig6i-noise-correlations-rt\n  criterion: The fast minus slow mean correlation (as fig6i) of the 162 PAC-category pairs against\n    that of 162 random pairs of a category neuron with a non-PAC neuron of the same session and\n    area, redrawn 10,000 times (the number of draws is not stated; 10,000 is the paper's default\n    for permutations). Reproduced when fewer than 5% of draws reach the PAC pairs' value.\n"
}
```

```
File created successfully at: claims/000673/10.1038-s41586-024-07309-z.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/000673/10.1038-s41586-024-07309-z.yaml paper/10.1038-s41586-024-07309-z.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -v '^#' claims/000673/10.1038-s41586-024-07309-z.yaml | sed -E 's/^([0-9]+):\s*(- )?[a-z_]+: /\1:/' | grep -E '^[0-9]+:.*: '
```

```
553:    significantly larger than that during baseline (n = 37; pref.: p = 0.12; non-pref.: p =
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='claims/000673/10.1038-s41586-024-07309-z.yaml'
s=open(p).read()
rep={
"""  quote: The activity of category neurons in the vmPFC (right) during the delay period was not
    significantly larger than that during baseline (n = 37; pref.: p = 0.12; non-pref.: p =
    0.26). Also, their FRs did not differ significantly between when the preferred and the
    non-preferred category of a cell was maintained in WM (t(36) = 1.03, p = 0.32, BF 01 = 3.47)""":
"""  quote: The activity of category neurons in the vmPFC (right) during the delay period was not
    significantly larger than that during baseline ... Also, their FRs did not differ
    significantly between when the preferred and the non-preferred category of a cell was
    maintained in WM (t(36) = 1.03, p = 0.32, BF 01 = 3.47)""",
"""  quote: Theta and gamma SFC between PAC neurons and local LFP recordings did not differ as a
    function of load in ( b ) the hippocampus (theta, t(78) = −1.54, p = 0.13; gamma, t(78) =
    −1.12, p = 0.27, n = 79), or ( c ) the amygdala (theta, t(162) = −0.71, p = 0.47; gamma,
    t(162) = 0.76, p = 0.45, n = 163)""":
"""  quote: Theta and gamma SFC between PAC neurons and local LFP recordings did not differ as a
    function of load in ( b ) the hippocampus ... or ( c ) the amygdala ... Theta and gamma SFC,
    however, were both significantly stronger than shuffled surrogates in both areas (all p =
    0.0001)""",
"""    LFPs was significantly stronger for PAC than for category neurons (PAC, n = 175, Cat, n = 215;
    t(376.07) = 3.3942, p = 0.0001; unpaired two-sided permutation t -test)""":
"""    LFPs was significantly stronger for PAC than for category neurons ... t(376.07) = 3.3942, p =
    0.0001; unpaired two-sided permutation t -test)""",
}
for a,b in rep.items():
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
E
python tools/claims_check.py claims/000673/10.1038-s41586-024-07309-z.yaml paper/10.1038-s41586-024-07309-z.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'E'
p='claims/000673/10.1038-s41586-024-07309-z.yaml'
s=open(p).read()
rep={
"""    (p = 0.049; intact – removed, p = 0.0009)""":"""    (p = 0.049""",
"""    p: 0.0001
    n: 28
""":"""    p: 0.0001
    n: 28, printed after "PAC neurons" (sessions in the hippocampal panel)
""",
}
for a,b in rep.items():
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
E
python tools/claims_check.py claims/000673/10.1038-s41586-024-07309-z.yaml paper/10.1038-s41586-024-07309-z.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -- "—" claims/000673/*.yaml; grep -n -i "rather" claims/000673/*.yaml
```

```
209:    different gamma-frequency bands—a lower (30–55 Hz) and a higher gamma range (70–140 Hz)
```

**Agent calls Bash**

```bash
cd  python - <<'E'
p='claims/000673/10.1038-s41586-024-07309-z.yaml'
s=open(p).read()
rep={
"different gamma-frequency bands—a lower (30–55 Hz)":"different gamma-frequency bands ... a lower (30–55 Hz)",
"""    trial re-pairings of spikes and LFP. Artefact""":"""    trial re-pairings of spikes and LFP. Artefact""",
"""    trials as in O1. Reproduced when, under the readings, both areas exceed every shuffled count
    (or all but 1 of 200) and the counts are within tolerance;""":"""    trials as in O1. Reproduced when, under the readings, in both areas fewer than 5% of the 200
    shuffled counts reach the observed count and the counts are within tolerance;""",
"""    hippocampal mean exceeds every shuffle (or all but 5%), and the pair counts are within
    tolerance.""":"""    hippocampal mean exceeds at least 95% of the shuffles, and the pair counts are within
    tolerance.""",
"""    22 and 48 channels). The paper's correction is not stated for this panel; the test is run
    uncorrected, as the legend lists none.""":"""    22 and 48 channels). The legend names no correction, so the test is run uncorrected; the
    FDR-corrected result is shown as a variant.""",
}
for a,b in rep.items():
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
E
python tools/claims_check.py claims/000673/10.1038-s41586-024-07309-z.yaml paper/10.1038-s41586-024-07309-z.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'E'
p='claims/000673/10.1038-s41586-024-07309-z.yaml'
s=open(p).read()
rep={
"different gamma-frequency bands—a lower (30–55 Hz)":"different gamma-frequency bands ... a lower (30–55 Hz)",
"""    trials as in O1. Reproduced when, under the readings, both areas exceed every shuffled count
    (or all but 1 of 200) and the counts are within tolerance;""":"""    trials as in O1. Reproduced when, under the readings, in both areas fewer than 5% of the 200
    shuffled counts reach the observed count and the counts are within tolerance;""",
"""    hippocampal mean exceeds every shuffle (or all but 5%), and the pair counts are within
    tolerance.""":"""    hippocampal mean exceeds at least 95% of the shuffles, and the pair counts are within
    tolerance.""",
"""    22 and 48 channels). The paper's correction is not stated for this panel; the test is run
    uncorrected, as the legend lists none.""":"""    22 and 48 channels). The legend names no correction, so the test is run uncorrected; the
    FDR-corrected result is shown as a variant.""",
}
for a,b in rep.items():
    assert a in s, a[:60]
    s=s.replace(a,b)
open(p,'w').write(s)
E
python tools/claims_check.py claims/000673/10.1038-s41586-024-07309-z.yaml paper/10.1038-s41586-024-07309-z.txt; grep -c -- "—" claims/000673/*.yaml; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python -c "
import yaml;d=yaml.safe_load(open('claims/000673/10.1038-s41586-024-07309-z.yaml'))
c=d['claims'];print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))"
```

```
56 56 49 113 52 16
```

**Agent**

I wrote `claims/000673/10.1038-s41586-024-07309-z.yaml`. The quote checker passes with 0 problems: 56 claims, 56 quotes, 113 statistical values found in the text. Nothing is committed.

**Text read.** The version of record (open access) from Europe PMC (PMC11078732), including Results, Methods, figure legends and all nine Extended Data legends. The Supplementary Information was also there: Tables S1–S5 and the Supplementary Discussion. The Peer Review File came through; the Reporting Summary came through empty, and no claim rests on it. Supplementary Table S4's model formula is garbled in the text. Its rows survive and were used, so nothing needed for a claim is missing.

**Code read.** github.com/rutishauserlab/SBCAT-release-NWB at commit a25e8cc3. It is sample code: behaviour metrics, category-cell selection, the LFP phase–amplitude coupling (PAC) comodulogram, the PAC-neuron GLMs for one example neuron, and a simulation of signal and noise axes. It settles several details:
- the category-selection windows and tests;
- the theta and high-gamma frequency bins;
- how PAC neurons are binned and their GLMs fitted;
- RT as the per-session median of correct trials.

It has no code for single-trial PAC, the mixed-effects GLMs, spike-field coherence (SFC), noise correlations on the data, decoding, or cluster statistics.

**Counts.** 56 claims, all with quotes and none inferred. 49 claims carry statistics (113 entries), 52 have criteria and 16 have expected values. All use the dataset's own data; the paper names no outside data.

**Details left open, with the readings named for each:**
- **O1, LFP artefact rejection:** the visual-inspection step can't be repeated, and the span that gets z-scored isn't stated. Readings: the automated steps on the maintenance epochs, or on whole trials.
- **O2, equalising trial counts between loads:** random subsampling, so the seed is a standard choice.
- **O3, which frequency bins form the bands:** settled by the code for high gamma; low gamma is read the same way.
- **O4, the null for the proportion of PAC channels:** one reading is named.
- **O5, single-trial PAC:** not defined in the paper. Readings: raw per-trial modulation index, or the same z-scored within channel.
- **O6, firing-rate units in the tests:** rate in Hz, or percentage change from baseline.
- **O7, minimum incorrect trials per neuron:** at least 1, 2 or 3.
- **O8, size of the SFC surrogate jitter:** spikes redrawn uniformly within the window, or jittered by ±250 ms.
- **O9, scope of the FDR correction in PAC-neuron selection:** per area and load, or per neuron.
- **O10, averaging of noise correlations:** over all trials, or within conditions and then across them.
- **O11, decoding:** intact and shuffled ensembles built separately, or the intact order reused. The Fig. 6c gain measure is taken from the paper's reference 36.

**Open details within single claims:**
- which trials enter the correct-vs-incorrect test and the PAC–firing GLM;
- the slow and fast theta bands of Table S1;
- the test for overlap between PAC and category neurons;
- the encoding presentations used for the Extended Data Fig. 7a decoding;
- the spectral-slope frequency range;
- the n:m ratio for phase–phase coupling;
- the spike minimum for the RT test of cross-regional SFC.

The cluster-forming threshold isn't stated, so FieldTrip's defaults are used, following the paper's citation of FieldTrip.

**Missing from the paper:** nothing a claim needed is absent. The one gap is that the paper never says how single-trial PAC is computed, which affects 3 claims (Fig. 2f, 3h and 4c); readings are named for it.

## End of run

37 turns, 8 minutes, result: success.
