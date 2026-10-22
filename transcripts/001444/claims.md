# 001444 · claims · run 39657017164

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls claims/001453/ claims/001444/ paper/ 2>&1; ls tools
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; wc -l *; head -30 10.1038-s41531-025-01070-4.txt; head -15 10.1101-2024.05.23.595566.txt; cat ../claims/001453/*.yaml | head -150
```

```
<persisted-output>
Output too large (86.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/678d6f69-e8f1-44f3-b808-114f664d7888/tool-results/b0jvub474.txt

Preview (first 2KB):
   363 10.1038-s41531-025-01070-4.txt
   453 10.1101-2024.05.23.595566.txt
   816 total
DOI: 10.1038/s41531-025-01070-4
Version: as served by europe_pmc
Source: europe_pmc+crossref (paper-text-fetcher)
Stored: 2026-10-21
Extracted: as fetched
------------------------------------------------------------------------
pmc NPJ Parkinsons Dis NPJ Parkinsons Dis NPJ Parkinson's Disease 2373-8057 Nature Publishing Group UK London 12325672 40764619 1070 10.1038/s41531-025-01070-4 Article Enhanced beta power emerges from simulated parkinsonian primary motor cortex Doherty Donald W. [removed: an e-mail address] 1 2 Chen Liqiang 2 3 Smith Yoland 2 4 Wichmann Thomas 2 4 Chu Hong-Yuan 2 3 Lytton William W. 1 2 5 1 https://ror.org/0041qmd21 grid.262863.b 0000 0001 0693 2202 Department of Physiology & Pharmacology, SUNY Downstate Medical Center, Brooklyn, NY 11203 USA 2 grid.513948.2 0000 0005 0380 6410 Aligning Science Across Parkinson’s (ASAP) Collaborative Research Network, Chevy Chase, MD 20815 USA 3 https://ror.org/00hjz7x27 grid.411667.3 0000 0001 2186 0438 Department of Pharmacology and Physiology, Georgetown University Medical Center, Washington D.C., USA 4 https://ror.org/03czfpz43 grid.189967.8 0000 0001 0941 6502 Emory National Primate Research Center, Department of Neurology, Udall Center of Excellence for Parkinson’s Disease Research, Emory University, School of Medicine, Atlanta, GA 30329 USA 5 https://ror.org/02emy8e21 grid.415345.2 0000 0004 0451 974X Kings County Hospital, Brooklyn, NY 11203 USA 5 8 2025 5 8 2025 2025 11 230 18 3 2025 6 7 2025 © The Author(s) 2025 2025 https://creativecommons.org/licenses/by/4.0/ Open Access This article is licensed under a Creative Commons Attribution 4.0 International License, wh
[... 2 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41531-025-01070-4.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; for f in *.txt; do echo "== $f"; grep -o -i ".\{150\}supplementary.\{200\}" $f | tail -n +1 | cut -c1-400; done; python3 -c "
s=open('10.1038-s41531-025-01070-4.txt').read(); print(len(s)); print(s[-3000:])"
```

```
/bin/bash: line 1: cd: paper: No such file or directory
== 10.1038-s41531-025-01070-4.txt
 modification, redistribution and research use by the community (feel free to email authors with questions) 43 – 45 . All resources are listed in the Supplementary Data Key Resource Table (Supplementary Table 1 ). To demonstrate robustness, we ran 4 sets of 4 simulations (Supplementary Table 2 ), each set including the control and parkinsonian conditions in res
uron location. In this paper we used the experiment set sM1_12-12-2023 as a typical example. Analyses of the 3 other sets of experiments are shown in Supplementary Table 2 and a typical example set of Supplementary Figs. 2 - 5 . We compared the control “healthy” condition with a model of the parkinsonian condition based on our co-authors physiology of the 6-hyd
lity since further from threshold. However, the slope of the current-frequency (I-f) curve was too shallow so we increased NaT to more closely match (Supplementary Fig. 1 of present paper; Supplementary Table 3 ). Morphology and physiology of neuron classes Seven excitatory pyramidal cell types and two interneuron cell types were simulated in the network (Fig. 
s identical to M1 validated in the Dura-Bernal et al. 21 paper except in the current study control PT5B currents were slightly modified (NaT, and BK; Supplementary Table 2 ) so that their response properties were more similar to the mean control PT5B neurons reported by Chen et al. 19 . In the simulated parkinsonian mouse M1 PT5B currents (BK and NaT) were modi
e was too shallow. A small increase in NaT current increased the slope of the current-frequency curve to more closely match the values seen in vitro (Supplementary Fig. 1 ). Microcircuit composition: neuron locations, densities and ratios We modeled a cylindrical volume of the mouse M1 cortical microcircuit with a 300 μm diameter and 1350 μm height (cortical de
as the duration from the time increasing activity crosses the 50% activity threshold to th
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
head -c 3000 10.1101-2024.05.23.595566.txt; echo; grep -n -i -o ".\{100\}supplem.\{150\}" 10.1101-2024.05.23.595566.txt | head; grep -c "" 10.1101-2024.05.23.595566.txt
```

```
DOI: 10.1101/2024.05.23.595566
Version: as served by playwright_biorxiv
Source: playwright_biorxiv+crossref (paper-text-fetcher)
Stored: 2026-10-21
Extracted: as fetched
------------------------------------------------------------------------
Skip to main content
HOMESUBMITFAQBLOGALERTS / RSSRESOURCESABOUTCHANNELS
Search for this keyword
Advanced Search
New Results
 Follow this preprint
Decreased cellular excitability of pyramidal tract neurons in primary motor cortex leads to paradoxically increased network activity in simulated parkinsonian motor cortex
 
View ORCID Profile
Donald W Doherty,  
View ORCID Profile
Liqiang Chen,  
View ORCID Profile
Yoland Smith,  
[... 19 more lines not kept]
```

**Agent calls Bash**

```bash
cd ..; grep -n -i "supplement" docs/pilot-notes.md | head -30; grep -l -i "supplement.*not\|missing" claims/*/*.yaml | head
```

```
942:photometry of Figure 6 and Supplementary Figures 7 and 8; the imaging,
1120:stated spread" for a mean and SD over cells; supplementary material and a
1143:Supplementary Figures 7 and 8 were tested on the dandiset as before, and the
1155:the Calb1 dF/F is not the trace behind Supplementary Figure 8 (0 of 384
1207:are described only in the Supplemental Experimental Procedures, which could
1253:text available without its supplement, whose claims were blocked as
1335:tables; counting the same unit across days; and claims citing supplementary
1370:the supplementary Materials and Methods that define them are served only
1391:supplement; no guidance for a pre-registered test confounded by pooling
1418:supplementary files could not be downloaded, as PubMed Central served a
1460:tenfold"; open-access supplements that cannot be downloaded; where
1481:not in the dandiset. The supplement could not be obtained, so supplementary
1530:available without its supplement; `measured` when no reading matches; and
1623:and the supplement, which defines the measures of Figures 6 and 7 and the
1665:to interpret the files; no rule for when the unavailable supplement defines
1692:supplement does not expect shuffles 2 and 3 to reduce; in
1700:the Supplementary Information was taken from the publisher's site, as PubMed
1728:Supplementary Figure 5, may be dated a year early.
1928:author manuscript (PMC6605060) and did not read the supplementary figures.
2011:author manuscript in PubMed Central (PMC6952543), whose supplementary figures
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1245,1260p docs/pilot-notes.md; sed -n 1475,1490p docs/pilot-notes.md; sed -n 1660,1670p docs/pilot-notes.md
```

```
states and movement to define WAKE; and in 14 sessions the state labels
agree best with the spikes when shifted 5 to 60 s earlier, while the LFP
agrees with the spikes to within 50 ms in 14 of 21 sessions, three others
have a clear extreme 56 to 64 ms from zero lag, and in three agreement is
not established.

The author's points on the protocol: "open access" is not defined, and a
free-to-read author manuscript was taken as full text; no rule for a main
text available without its supplement, whose claims were blocked as
`methods_underspecified` though that reason is defined for a procedure
neither the paper nor its code fixes; no guidance on looking for code when
none is linked (the author read the conversion code, which explained both
corrupt files); a clock check by decoding shifted labels that is coarse for
states lasting minutes and does not apply to LFP; no guidance on a label the
paper uses and the dandiset lacks, or on corruption of single sessions; the
10% tolerance for correlations that depend on binning the paper does not
choice errors and speed, place cell and interneuron rates and oscillation
frequencies, waveforms, field size and information, phase precession and the
pair correlogram, compression and lag claims were tested, on session lists
and parameters taken from the paper's MATLAB code, read and not run.
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/suny-downstate-medical-center/pd_m1_6ohda && cd pd_m1_6ohda && git log -3 --format='%H %ad %s' && find . -type f -not -path './.git/*' | head -100 && find . -type f -not -path './.git/*' | wc -l
```

```
0a1f0e89920c6aaeb6b0a7a8dbe15384c899b832 Wed Aug 20 11:46:51 2025 -0700 Change ' to " in cfg.seeds. Otherwise leads to erroneous results
45ad64ffa321ec1a97148329c780b8df9c5a4a31 Wed Aug 6 12:00:46 2025 -0400 Update README.md
1cbd88467107c6cf733ffb6d05788d1898b2a485 Wed Aug 6 09:55:08 2025 -0400 Update README.md
./sim/run_sim_dev
./sim/run_sim
./sim/netParams.py
./sim/mod/vecstim.mod
./sim/mod/savedist.mod
./sim/mod/parameters.multi
./sim/mod/naz.mod
./sim/mod/nax_BS.mod
./sim/mod/nap_sidi.mod
./sim/mod/nafx.mod
./sim/mod/nafcr.mod
./sim/mod/my_exp2syn.mod
./sim/mod/misc.h
./sim/mod/kv.mod
./sim/mod/km.mod
./sim/mod/kdrin.mod
./sim/mod/kdrcr.mod
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pd_m1_6ohda && find . -type f -not -path './.git/*' | tail -22; cat README.md; git log --format='%h %ad %s' | head -30
```

```
./sim/cells/LTS3.hoc
./sim/cells/ITcell.py
./sim/cells/IT_full_BS1579_cellParams.pkl
./sim/cells/IT_full_BS1578_cellParams.pkl
./sim/cells/IT6_reduced_cellParams.pkl
./sim/cells/IT5B_reduced_cellParams.pkl
./sim/cells/IT5B_full_cellParams.pkl
./sim/cells/IT5A_reduced_cellParams.pkl
./sim/cells/IT5A_full_cellParams.pkl
./sim/cells/IT4_reduced_cellParams.pkl
./sim/cells/IT2_reduced_cellParams.pkl
./sim/cells/FS3.hoc
./sim/cells/CT6_reduced_cellParams.pkl
./sim/cells/CSTR6.py
./sim/batch.py
./sim/README
./README.md
./Parkinsonian_Quiet_Wakefulness.ipynb
./Parkinsonian_Movement.ipynb
./LICENSE
[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pd_m1_6ohda && python3 - <<'EOF'
import json
nb=json.load(open('Control_Quiet_Wakefulness.ipynb'))
for c in nb['cells']:
    print('-----',c['cell_type'])
    print(''.join(c['source'])[:6000])
EOF
```

```
----- markdown
# sM1_12-12-2023_01: Control, Quiet Wakefulness
----- markdown
This notebook shows how you can analyze data streamed from our NWB data residing in the DANDI archive.
----- code
from dandi.dandiapi import DandiAPIClient
import fsspec
from fsspec.implementations.cached import CachingFileSystem
import h5py
import matplotlib.pyplot as plt
import numpy as np
import pynwb

----- markdown
The data used in this tutorial were used in this publication: Doherty, et al. "Enhanced beta power emerges from simulated parkinsonian primary motor cortex." npj Parkinson's Disease (2025). (https://doi.org/10.1101/2024.05.23.595566) The data can be found on the DANDI Archive in Dandiset 001444.
----- code
dandiset_id = "001444"
filepath = "sub-001/sub-001_ses-sM1-12-12-2023-01.nwb"
with DandiAPIClient() as client:
    asset = client.get_dandiset(dandiset_id, 'draft').get_asset_by_path(filepath)
[... 117 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pd_m1_6ohda && for n in *.ipynb; do python3 -c "
import json,sys
nb=json.load(open('$n'))
print('$n', ''.join(nb['cells'][0]['source']))
for c in nb['cells']:
  s=''.join(c['source'])
  if 'filepath' in s or 'Segment 0 LFP' in s: print(s[:400])
"; done; diff <(python3 -c "import json;print('\n'.join(''.join(c['source']) for c in json.load(open('Control_Quiet_Wakefulness.ipynb'))['cells']))") <(python3 -c "import json;print('\n'.join(''.join(c['source']) for c in json.load(open('Parkinsonian_Movement.ipynb'))['cells']))")
```

```
Control_Movement.ipynb # sM1_12-12-2023_03: Control, Movement
dandiset_id = "001444"
filepath = "sub-001/sub-001_ses-sM1-12-12-2023-03.nwb"
with DandiAPIClient() as client:
    asset = client.get_dandiset(dandiset_id, 'draft').get_asset_by_path(filepath)
    s3_url = asset.get_content_url(follow_redirects=1, strip_query=True)
    
# 40 samples per ms
# data window from 2 seconds (2000 ms) to 2.25 sec (2250 ms)
xmin = 2000 * 40
xmax = 2250 * 40
plt.figure(figsize=(15,5))
plt.xlim(xmin, xmax)
plt.ylim(-0.17, 0.05)
plt.title('Control Movement', fontsize= 30)
plt.plot(nwbfile.acquisition.get('Segment 0 LFP 0').data, color='black')
plt.xticks([])
plt.yticks([])

Control_Quiet_Wakefulness.ipynb # sM1_12-12-2023_01: Control, Quiet Wakefulness
[... 74 more lines not kept]
```

**Agent**

Now the simulation config and analysis settings.

**Agent calls Bash**

```bash
cd $TMPDIR/pd_m1_6ohda/sim && grep -n -i "duration\|recordStep\|dt\b\|cfg.dt\|LFP\|analysis\|seeds\|spectro\|granger\|rate\|ihGbar\|gnaf\|kBK\|gpeak\|recordTraces\|recordCells\|saveFolder\|simLabel" cfg.py | head -120; cat README
```

```
24:cfg.duration = 4.3*1e3 
25:cfg.dt = 0.025
26:cfg.seeds = {"conn": 4321, "stim": 1234, "loc": 4321} 
39:cfg.printPopAvgRates = [1000., 5000.]
53:if cfg.cellsrec == 0:  cfg.recordCells = ['all'] # record all cells
54:elif cfg.cellsrec == 1: cfg.recordCells = [('PT5B',[x]) for x in range(0, 400)] #
55:elif cfg.cellsrec == 2: cfg.recordCells = [5130, 5131, 5132, 5133, 5134, 5135, 5136, 5137, 5138, 5139, 5140, 5141, 5142, 5143, 5144, 5145, 5146, 5147, 5148, 5149]
56:elif cfg.cellsrec == 3: cfg.recordCells = [(pop,50) for pop in ['IT5A', 'PT5B']]+[('PT5B',x) for x in [393,579,19,104]] #,214,1138,799]] # record selected cells # record selected cells
57:elif cfg.cellsrec == 4: cfg.recordCells = [(pop,50) for pop in ['IT2', 'IT4', 'IT5A', 'PT5B']]+[('PT5B',x) for x in [393,447,579,19,104,214,1138,979,799]] # record selected cells
59:cfg.recordTraces = {'V_soma': {'sec':'soma', 'loc':0.5, 'var':'v'}}#,
65:cfg.recordLFP = [[150, y, 150] for y in range(200,1300,100)] # [[150, y, 150] for y in range(200,1300,100)]
67:cfg.saveLFPPops =  False # allpops 
73:cfg.recordStep = 0.025
79:cfg.simLabel = 'sM1_04-28-2023_06'
80:cfg.saveFolder = 'data/'
91:# Analysis and plotting 
95:#cfg.analysis['plotRaster'] = {'include': allpops, 'orderBy': ['pop', 'y'], 'timeRange': [0, cfg.duration], 'saveFig': True, 'showFig': False, 'popRates': True, 'orderInverse': True, 'popColors': popColors, 'figSize': (12,10), 'lw': 0.3, 'markerSize':3, 'marker': '.', 'dpi': 300} 
98:#cfg.analysis['plotLFP'] = {'plots': ['timeSeries'], 'electrodes': list(range(len(cfg.recordLFP))), 'figSize': (12,10), 'timeRange': [1000,5000],  'saveFig': True, 'showFig':False} 
101:#cfg.analysis['plotTraces'] = {'include': [], 'timeRange': [0, cfg.duration], 'oneFigPer': 'trace', 'figSize': (10,4), 'saveFig': True, 'showFig': False} 
116:cfg.ihGbar = 0.75  # multiplicative factor for ih gbar in PT cells
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/pd_m1_6ohda/sim && sed -n 20,115p cfg.py; cat init.py; grep -n "kBK\|gpeak\|gnafbar\|nafx" netParams.py | head
```

```
#------------------------------------------------------------------------------
# Run parameters
#------------------------------------------------------------------------------
cfg.duration = 4.3*1e3 
cfg.dt = 0.025
cfg.seeds = {"conn": 4321, "stim": 1234, "loc": 4321} 
cfg.hParams = {'celsius': 34, 'v_init': -80}  
cfg.verbose = 0
cfg.createNEURONObj = 1
cfg.createPyStruct = 1
cfg.connRandomSecFromList = False  # set to false for reproducibility 
cfg.cvode_active = False
cfg.cvode_atol = 1e-6
cfg.cache_efficient = True
cfg.printRunTime = 0.1
cfg.oneSynPerNetcon = True  # only affects conns not in subconnParams; produces identical results

cfg.includeParamsLabel = False #True # needed for modify synMech False
cfg.printPopAvgRates = [1000., 5000.]

[... 104 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -o ".\{200\}\(t-test\|wilcoxon\|mann\|kolmogorov\|anova\|wavelet\|morlet\|welch\|fourier\|FFT\|spectrogram\|unitary\|statistic\|electrode\|depth\).\{200\}" 10.1101-2024.05.23.595566.txt | head -40
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -n -i -E "t-test|wilcoxon|mann|kolmogorov|anova|wavelet|morlet|welch|fourier|FFT|spectrogram|unitary|statistic|electrode|depth|Methods" 10.1101-2024.05.23.595566.txt | cut -c1-300 | head -40
```

```
22:Thomas Wichmann,  
42:Methods
57:We used unitary event analysis for identifying synchronous spiking significantly above the expected number of synchronous spikes for the neuron population size and firing rates.12
70:Control condition. A. and B. show the resting state on the left, and the activated state on the right. A. Top-to-bottom: LFP, raster plot (red excitatory; black inhibitory neurons); PT5B spike count histograms (left: dashed lines at half height). B. Examples of PT5B voltage traces -- same 5 (out 
83:Time-resolved spectrograms of cortical LFPs in the healthy state, under rest (A.) and activation (B) conditions. Power in bars x 1.0e-5.
104:Time-resolved spectrograms of LFPs in M1 in the parkinsonian state. A. resting state, B. activated state. Color coding shown in colorbar (x 1.0e-4).
110:LFP spectrograms of resting oscillatory power displayed continuous high-power 15 Hz beta-band power with bursts of power in the ∼25-35 Hz (∼50-250 ms duration) occurring about once every 200 ms (∼5.0 Hz; Fig. 6A). In the activated state, ∼20-35 Hz bursts ∼25-100 ms in duration were seen that occ
157:2.↵Galvan, A., and Wichmann, T. (2008). Pathophysiology of parkinsonism. Clin. Neurophysiol. 119, 1459–1474.OpenUrlCrossRefPubMedWeb of ScienceGoogle Scholar
160:5.↵Dura-Bernal, S., Neymotin, S.A., Suter, B.A., Dacre, J., Moreira, J.V.S., Urdapilleta, E., Schiemann, J., Duguid, I., Shepherd, G.M.G., and Lytton, W.W. (2023). Multiscale model of primary motor cortex circuits predicts in vivo cell-type-specific, behavioral state-dependent dynamics. Cell Rep
167:12.↵Grün, S., Diesmann, M., Grammont, F., Riehle, A., and Aertsen, A. (1999). Detecting unitary events without discretization of time. J. Neurosci. Methods 94, 67–79.OpenUrlCrossRefPubMedWeb of ScienceGoogle Scholar
168:13.↵Dura-Bernal, S., Neymotin, S.A., Suter, B.A., Dacre, J., Schiemann, J., Duguid, I., Shepherd, G.M.G., and Lytton, W.W. Multiscale model of primary motor cortex circuits predicts in vivo cell type-sp
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd ..; sed -n 1,200p claims/001453/*.yaml
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/claims_check.py; grep -rn "inferred:" claims/*/*.yaml | head -3; grep -rn "where:" claims/*/*.yaml | head -3
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

[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
python3 -c "
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

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[5000:12000])"
```

```
'PRIDE PXD012345' or 'Zenodo doi:10.5281/zenodo.123'.",
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
[... 178 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "claims/001444/10.1038-s41531-025-01070-4.yaml",
 "content": "# Claims for Doherty, Chen, Smith, Wichmann, Chu & Lytton (2025), npj Parkinson's Disease 11, 230,\n# \"Enhanced beta power emerges from simulated parkinsonian primary motor cortex\", on dandiset 001444.\n# Written by an agent (model \"claude-opus-5-5\", Claude Code in GitHub Actions), 2026-10-21, protocol\n# pilot-10 as stated in docs/protocol.md.\n#\n# Text read: the version of record as served by Europe PMC (PMC12325672), main text, figure legends\n# and Methods. The supplement (Supplementary Tables 1 to 3, Supplementary Figs. 1 to 5) was not in\n# the text supplied and was not read. The main text reports every result below from one set of\n# simulations; the supplement holds the analyses of the three other sets (Supplementary Table 2),\n# the PT5B current-frequency curves (Supplementary Fig. 1) and the conductance changes\n# (Supplementary Table 3). The bioRxiv preprint (doi:10.1101/2024.05.23.595566) was also supplied;\n# it is an earlier version with another title and was not used for claims.\n#\n# Code read: github.com/suny-downstate-medical-center/pd_m1_6ohda at commit 0a1f0e8 (2025-08-20, the\n# head of main; the paper cites Zenodo 10.5281/zenodo.12399983). It holds the NetPyNE simulation\n# (sim/cfg.py, sim/netParams.py, cells, mechanisms) and four notebooks that stream one file each\n# from dandiset 001444 and plot the LFP, a raster and five PT5B voltage traces. It holds no code for\n# rates, statistics, CV, duty cycle, spectrograms, coincidences or unitary events. The README gives\n# the four parameter settings (control or parkinsonian PT5B BK and NaT conductances; rest or\n# activated Ih factor and thalamic rates).\n#\n# The data the paper used. A simulation of a 300 um diameter, 1350 um deep cylinder of mouse M1 with\n# 10,073 neurons in 15 populations (IT2, PV2, SOM2, IT4, IT5A, PV5A, SOM5A, IT5B, PT5B, PV5B, SOM5B,\n# IT6, CT6, PV6, SOM6; cfg.py), driven by Poisson spike generators standing for thalamic and\n# cortical inputs. Four sets of four simulations, each 4.3 s long; each set holds the control and\n# parkinsonian conditions in the rest (quiet wakefulness) and activated (movement) states, and each\n# set used its own random seeds (Methods, paragraph 2). The paper's results come from set\n# sM1_12-12-2023. The paper's notebooks name its files sub-001/sub-001_ses-sM1-12-12-2023-01.nwb\n# (control rest), -02 (parkinsonian rest), -03 (control activated) and -04 (parkinsonian\n# activated). Measured variables: spike times of every neuron (units named \"<population> <index>\",\n# including the input generators), somatic membrane potential of some PT5B neurons (the notebooks\n# plot \"Segment 0 PT5B 5401 5\" and four others), and the LFP at 11 electrodes at depths 200 to\n# 1200 um in 100 um steps (cfg.recordLFP), sampled every 0.025 ms (40 samples per ms; cfg.recordStep\n# and the notebooks). The dandiset description says it holds the main and supplemental data.\n#\n# Definitions used by several criteria, each from the paper or its code as cited:\n# - Analysis window W. Rates are \"calculated from the last 2.3 s of 4.3 s simulation to avoid\n#   initialization transients\" (Fig. 2C and 5C legends), so 2.0 to 4.3 s. The spectrograms show\n#   \"2.3 s of activity starting 2 s after simulation initiation\" (Fig. 3 and 6 legends), the same\n#   window. The 250 ms panels of Figs. 2A,B and 5A,B are 2.0 to 2.25 s (the notebooks).\n# - Rate of a neuron is its spike count in W divided by 2.3 s; a population is given as mean and\n#   standard deviation over its neurons (legends of Figs. 2C and 5C, \"mean, std dev\"). Open is\n#   whether neurons silent in W are counted. Readings R1, all neurons of the population; R2, only\n#   neurons with at least one spike in W. The IT5A and IT5B rates of 0 spikes/s in the activated\n#   state suggest R1, but the text does not say.\n# - The paper names no test for any firing-rate p-value. The same network (same seeds) is run in\n#   all four simulations of a set, so the neurons can be paired. Readings T1, Wilcoxon signed-rank\n#   on paired neurons; T2, paired t-test; T3, Mann-Whitney U on the two groups; T4, Welch's t-test.\n#   Two-sided, at the p bound the paper prints.\n# - Spectra. The Methods say the LFP was computed with the method built into NetPyNE; they name no\n#   spectral method or electrode. Readings S1, the spectrogram of NetPyNE 1.0.5 (the version the\n#   Methods name; netpyne.analysis plotLFP, Morlet wavelets, its default parameters); S2, a\n#   short-time Fourier transform (NetPyNE's fft option). Electrode readings E1, electrode 0\n#   (y = 200 um), the one the paper's notebooks plot as the LFP of Figs. 2 and 5; E2, the mean\n#   over the 11 electrodes (NetPyNE's \"avg\" electrode). Time-averaged power spectra for peak\n#   frequencies are taken by Welch's method with 1 s segments, a standard choice that sets only\n#   the frequency resolution (1 Hz), well inside every tolerance below.\n# - PT5B spike count histogram (SCH): spikes of all PT5B neurons in 2 ms bins (Fig. 2 and 5\n#   legends).\n# Where the readings of a claim give different outcomes, the claim is blocked as\n# methods_underspecified, with every result shown (docs/protocol.md, Reader, step 3).\nschema_version: 2\ndataset:\n  archive: dandi\n  id: \"001444\"\npaper: doi:10.1038/s41531-025-01070-4\nclaims:\n- id: fig1-network-size\n  statement: The simulated M1 network is composed of 10,073 neurons in 15 populations of\n    excitatory pyramidal (IT, PT5B, CT) and inhibitory (PV, SOM) neurons.\n  source: Figure 1 legend; Methods, Microcircuit composition, paragraph 1\n  quote: Simulated primary motor cortex (M1) is composed of 10,073 neurons.\n  expected:\n  - quantity: number of M1 neurons (input generators excluded)\n    value: 10073\n    tolerance: 0\n    unit: neurons\n  criterion: In each of the four files of set sM1_12-12-2023, count the units whose population is\n    one of the 15 M1 populations of sim/cfg.py (allpops), leaving out the input spike generators.\n    Reproduced when the count is 10,073 in each file. The tolerance is zero because the number is\n    a count of a fixed model, not a measurement.\n- id: model-pt5b-excitability-decrease\n  statement: In the parkinsonian condition the PT5B neuron model was changed (BK and NaT\n    conductances) so that its spike count across current injections fell by 64%, as in 6-OHDA\n    mouse slices.\n  source: Methods, paragraph 2 and Morphology and physiology of neuron classes, paragraph 3;\n    Supplementary Fig. 1 (not read)\n  quote: In the simulated parkinsonian mouse M1 PT5B currents (BK and NaT) were modified so that\n    they showed a 64% decrease in excitability as reported by Chen et al.\n  expected:\n  - quantity: decrease of PT5B spike count averaged across current injections, parkinsonian against\n    control\n    value: 64\n    tolerance: 6.4\n    unit: percent\n  criterion: Needs single-neuron current-injection simulations of the control and parkinsonian\n    PT5B model (README parameter settings; cfg.gpeak and cfg.gnafbar). The current amplitudes,\n    step duration and averaging behind the 64% are those of Fig. 1D of Chen et al. 2021 (J.\n    Neurosci. 41, 5553) and Supplementary Fig. 1, which was not available to this reader. The\n    claim can be tested only if the dataset holds these current-injection simulations and the\n    supplement or the question process supplies the protocol; otherwise the detail is open and\n    the claim is blocked as methods_underspecified.\n- id: robustness-four-sets\n  statement: The results hold across four sets of four simulations with different random seeds;\n    set sM1_12-12-2023 is a typical example and the other three sets are analysed in\n    Supplementary Table 2.\n  source: Methods, paragraph 2; Supplementary Table 2 and Supplementary Figs. 2 to 5 (not read)\n  quote: To demonstrate robustness, we ran 4 sets of 4 simulations (Supplementary Table 2 ), each\n    set including the control and parkinsonian conditions in rest state and in the activated\n    (movement) state.\n  criterion: Supplementary Table 2, which gives the measures and values for the other three sets,\n    was not in the text supplied, so this reader cannot fix the measures, the expected values or\n    what counts as holding. The claim is blocked as methods_underspecified until a reader with the\n    supplement completes it. The author may report, for each set the dataset holds, the measures\n    of the claims below, without an outcome.\n- id: fig2-control-rest-beta\n  statement: In the control condition at rest, M1 activity is dominated by beta-band activity of\n    about 20 Hz, particularly clear in the PT5B spike count histogram.\n  source: Figure 2A legend; Results, Control simulations, paragraph 1\n  quote: Resting state (250 ms at midpoint of 4.3 s simulation) displayed dominant beta-band\n    activity (~20 Hz; particularly clear in the PT5B spike count histogram).\n  expected:\n  - quantity: dominant frequency, control rest\n    value: 20\n    tolerance: 2\n    unit: Hz\n  criterion: File -01. The frequency of the largest peak of the time-averaged power spectrum in W\n    of (a) the PT5B SCH (the legend's measure) and (b) the LFP under E1 and E2. The paper reports\n    separate 2 Hz activity in the rest LFP (Fig. 3A), so the peak is searched (i) above 0 Hz and\n    (ii) above 5 Hz, a range the paper does not fix. Reproduced when the peak is within 18 to\n    22 Hz under every reading of the SCH; the LFP readings are reported as variants, since the\n    legend names the SCH.\n- id: fig2-control-activated-gamma\n  statement: In the control condition, the activated state shifts M1 activity to gamma-band\n    activity of about 44 Hz.\n  source: Figure 2B legend; Results, Control simulations, paragraph 1\n  quote: Activated state showed change to high-frequency gamma-band activity (~44 Hz).\n  expected:\n  - quantity: dominant frequency, control activated\n    value: 44\n    tolerance: 4.4\n    unit: Hz\n  criterion: File -03, the measure and readings of fig2-control-rest-beta. Reproduced when the\n    largest spectral peak of the PT5B SCH in W is within 39.6 to 48.4 Hz under every reading; the\n    LFP readings (E1, E2) are reported as variants.\n- id: fig2c-control-pt5b-rate-activated\n  statement: In the control condition PT5B neurons fire more in the activated state than at rest\n    (11.7 +/- 9.4 against 26.8 +/- 18.2 spikes/s, p < 0.001).\n  source: Figure 2C legend; Results, Control simulations, paragraph 5\n  quote: 'Pyramidal tract neurons had the highest spike rate of any neuron population during the\n    rest state, and increased further in the activated state (rest: 11.7 ± 9.4 spikes/s; activated:\n    26.8 ± 18.2 spikes/s; p < 0.001; Fig. 2C ).'\n  statistics:\n  - test: not named\n    p: 0.001\n    p_relation: \"<\"\n    n: PT5B neurons of the control rest and activated simulations\n  expected:\n  - quantity: PT5B mean rate, control rest\n    value: 11.7\n    tolerance: 1.17\n    unit: spikes/s\n  - quantity: PT5B rate standard deviation, control rest\n    value: 9.4\n    tolerance: 0.94\n    unit: spikes/s\n  - quantity: PT5B mean rate, control activated\n    value: 26.8\n    tolerance: 2.68\n    unit: spikes/s\n  - quantity: PT5B rate standard deviation, control activated\n    value: 18.2\n    tolerance: 1.82\n    unit: spikes/s\n  criterion: Files -01 and -03, rates in W, readings R1 and R2. Reproduced when, under one rate\n    reading, all four values are within tolerance and the activated rates are higher with p <\n    0.001 under every test reading T1 to T4.\n- id: fig2c-control-it23-rate-activated\n  statement: In the control condition IT2/3 neurons fire more in the activated state than at rest\n    (1.2 +/- 1.6 against 6.7 +/- 8.9 spikes/s, p < 0.001).\n  source: Figure 2C legend; Results, Control simulations, paragraph 5\n  quote: 'IT2/3 neurons significantly increased their firing rate (rest: 1.2 spikes/s; activated:\n    6.6 spikes/s; p < 0.001).'\n  statistics:\n  - test: not named\n    p: 0.001\n    p_relation: \"<\"\n    n: IT2/3 neurons of the control rest and activated simulations\n  expected:\n  - quantity: IT2/3 mean rate, control rest\n    value: 1.2\n    tolerance: 0.12\n    unit: spikes/s\n  - quantity: IT2/3 rate standard deviation, control rest\n    value: 1.6\n    tolerance: 0.16\n    unit: spikes/s\n  - quantity: IT2/3 mean rate, control activated\n    value: 6.7\n    tolerance: 0.67\n    unit: spikes/s\n  - quantity: IT2/3 rate standard deviation, control activated\n    value: 8.9\n    tolerance: 0.89\n    unit: spikes/s\n  criterion: Files -01 and -03, population IT2, rates in W, readings R1 and R2. The legend gives\n    6.7 and the text 6.6 spikes/s for the activated mean; the tolerance of 6.7 covers both.\n    Reproduced when, under one rate reading, all four values are within tolerance and the\n    activated rates are higher with p < 0.001 under every test reading T1 to T4.\n- id: fig2c-control-it6-rate-activated\n  statement: In the control condition IT6 neurons fire less in the activated state than at rest\n    (5.8 +/- 5.8 against 3.5 +/- 5.2 spikes/s, p < 0.001).\n  source: Figure 2C legend; Results, Control simulations, paragraph 5\n  quote: IT6 firing rates decreased from 5.8 spikes/s at rest to 3.5 spikes/s in the activated\n    state ( p < 0.001).\n  statistics:\n  - test: not named\n    p: 0.001\n    p_relation: \"<\"\n    n: IT6 neurons of the control rest and activated simulations\n  expected:\n  - quantity: IT6 mean rate, control rest\n    value: 5.8\n    tolerance: 0.58\n    unit: spikes/s\n  - quantity: IT6 rate standard deviation, control rest\n    value: 5.8\n    tolerance: 0.58\n    unit: spikes/s\n  - quantity: IT6 mean rate, control activated\n    value: 3.5\n    tolerance: 0.35\n    unit: spikes/s\n  - quantity: IT6 rate standard deviation, control activated\n    value: 5.2\n    tolerance: 0.52\n    unit: spikes/s\n  criterion: Files -01 and -03, rates in W, readings R1 and R2. Reproduced when, under one rate\n    reading, all four values are within tolerance and the activated rates are lower with p <\n    0.001 under every test reading T1 to T4.\n- id: control-it5-silenced-activated\n  statement: In the control condition IT5A and IT5B neurons fire at about 3 spikes/s at rest (3.3\n    and 3.1 spikes/s) and stop firing (0 spikes/s) in the activated state.\n  source: Results, Control simulations, paragraph 5; Figure 2B\n  quote: In contrast, IT5A and IT5B firing rates decreased from 3 Hz (IT5A... 3.3 spikes/s; IT5B...\n    3.1 spikes/s) at rest, to 0 spikes/s in the activated state\n  expected:\n  - quantity: IT5A mean rate, control rest\n    value: 3.3\n    tolerance: 0.33\n    unit: spikes/s\n  - quantity: IT5B mean rate, control rest\n    value: 3.1\n    tolerance: 0.31\n    unit: spikes/s\n  - quantity: IT5A mean rate, control activated\n    value: 0\n    tolerance: 0.05\n    unit: spikes/s\n  - quantity: IT5B mean rate, control activated\n    value: 0\n    tolerance: 0.05\n    unit: spikes/s\n  criterion: Files -01 and -03, rates in W, reading R1 (under R2 an activated mean is undefined\n    when no neuron fires; if some fire, R2 is reported as a variant). The tolerance of the zero\n    rates is 0.05 spikes/s, the rounding of the paper's one decimal place, since 10% of zero is\n    zero. Reproduced when all four values are within tolerance.\n- id: control-it4-rate-activated\n  statement: In the control condition the IT4 population rate rises from 2.6 spikes/s at rest to\n    4.7 spikes/s in the activated state.\n  source: Results, Control simulations, paragraph 5\n  quote: The IT4 neuron population firing rate increased from 2.6 Hz during rest to 4.7 Hz during\n    the activated state.\n  expected:\n  - quantity: IT4 mean rate, control rest\n    value: 2.6\n    tolerance: 0.26\n    unit: spikes/s\n  - quantity: IT4 mean rate, control activated\n    value: 4.7\n    tolerance: 0.47\n    unit: spikes/s\n  criterion: Files -01 and -03, rates in W, readings R1 and R2. Reproduced when, under one\n    reading, both values are within tolerance. The paper reports no test.\n- id: pt5b-highest-rate\n  statement: PT5B neurons have the highest mean spike rate of any population in the control rest\n    state and in both the parkinsonian rest and activated states.\n  source: Results, Control simulations, paragraph 5; Results, Parkinsonian condition, paragraph 5\n  quote: Pyramidal tract neurons had the highest spike rate of any neuronal population during the\n    rest and activated states in the parkinsonian condition\n  criterion: Files -01, -02 and -04, mean rates in W of every M1 population. \"Any neuron\n    population\" can be read as (a) all 15 M1 populations, interneurons included, or (b) the seven\n    excitatory populations shown in Figs. 2C and 5C. Reproduced when the PT5B mean is the highest\n    in all three simulations under one rate reading (R1 or R2) and both population readings;\n    when the population readings disagree, the claim is blocked as methods_underspecified with\n    both shown.\n- id: control-cv-isi\n  statement: In the control condition PT5B interspike-interval CV is highly variable at rest (0.59\n    +/- 0.37; 47.8% regular with CV <= 0.5, 52.2% irregular) and mainly irregular in the activated\n    state (0.61 +/- 0.30; 25.7% regular, 74.3% irregular).\n  source: Results, Control simulations, paragraph 2\n  quote: The CV was found to be highly variable across the PT5B population during rest (0.59 +\n    /−0.37), indicating the presence of both regular (CV < = 0.5; 47.8%) and irregular activity\n    (CV > 0.5; 52.2%).\n  expected:\n  - quantity: mean PT5B ISI CV, control rest\n    value: 0.59\n    tolerance: 0.059\n  - quantity: standard deviation of PT5B ISI CV, control rest\n    value: 0.37\n    tolerance: 0.037\n  - quantity: percent of PT5B neurons with CV <= 0.5, control rest\n    value: 47.8\n    tolerance: 4.78\n    unit: percent\n  - quantity: mean PT5B ISI CV, control activated\n    value: 0.61\n    tolerance: 0.061\n  - quantity: standard deviation of PT5B ISI CV, control activated\n    value: 0.30\n    tolerance: 0.030\n  - quantity: percent of PT5B neurons with CV <= 0.5, control activated\n    value: 25.7\n    tolerance: 2.57\n    unit: percent\n  criterion: Files -01 and -03. CV of each PT5B neuron's ISIs (standard deviation over mean), mean\n    and standard deviation over neurons, and the share with CV <= 0.5 (regular) and > 0.5\n    (irregular), as in the Results. Open, with readings - the window, (a) W (the window of the\n    rates in the same figure) or (b) the whole 4.3 s; which neurons, (i) neurons with at least\n    two ISIs or (ii) at least one ISI (a single ISI gives CV 0). Reproduced when, under one\n    combination of readings, all six values are within tolerance.\n- id: control-subthreshold-oscillations\n  statement: In the control condition subthreshold membrane-potential oscillations appear in 57.4%\n    of PT5B neurons in the activated state and not at rest.\n  source: Results, Control simulations, paragraph 3; Figure 2A,B\n  quote: Oscillations in subthreshold membrane potentials appeared frequently during the activated\n    state (57.4% of PT5B neurons) but not during rest\n  expected:\n    quantity: percent of PT5B neurons with subthreshold oscillations, control activated\n    value: 57.4\n    tolerance: 5.74\n    unit: percent\n  criterion: Files -01 and -03, somatic membrane potentials of the PT5B neurons recorded. Neither\n    the paper nor its code says how a subthreshold oscillation is detected or over which neurons\n    the 57.4% is taken, and no reading follows from the text. The claim is blocked as\n    methods_underspecified unless a question to a reader settles it; the number of PT5B neurons\n    with recorded voltage is reported.\n- id: control-duty-cycle\n  statement: In the control condition the PT5B duty cycle, the share of each oscillation period\n    with activity above half-height, is 31% at rest and 48% in the activated state.\n  source: Results, Control simulations, paragraph 4; Figure 2A,B; Methods, Duty cycle\n  quote: The duty cycle was 31% during rest (Fig. 2A ) and 48% during activated state (Fig. 2B ;\n    dashed vertical lines not shown).\n  expected:\n  - quantity: PT5B duty cycle, control rest\n    value: 31\n    tolerance: 3.1\n    unit: percent\n  - quantity: PT5B duty cycle, control activated\n    value: 48\n    tolerance: 4.8\n    unit: percent\n  criterion: Files -01 and -03, the PT5B SCH (2 ms bins, unsmoothed, as the legends describe it).\n    A period runs from one rising crossing of half-height to the next, and the duty cycle is the\n    time above half-height divided by the period (Results, paragraph 4; the Methods sentence that\n    a period runs from the rising to the falling crossing would make every duty cycle 100% and is\n    read as defining the time on). Open, with readings - half-height, (a) halfway between the\n    minimum and maximum of the window shown (one line per panel, Fig. 2 legend) or (b) halfway\n    between the trough and peak of each period (Methods); the window, (i) the 250 ms of Fig. 2A,B,\n    2.0 to 2.25 s (the notebooks) or (ii) W; the duty cycle is the mean over complete periods.\n    Reproduced when, under one combination, both values are within tolerance.\n- id: fig3a-control-rest-spectrogram\n  statement: In the control rest state the LFP spectrogram shows virtually continuous power around\n    2 Hz and 15 to 25 Hz beta bursts recurring every 600 ms (1.7 Hz).\n  source: Figure 3A legend; Results, Control simulations, paragraph 6\n  quote: The rest state simulation revealed virtually continuous power around 2 Hz, as well as\n    15–25 Hz beta-band bursts (Fig. 3A ), occurring every 600 ms (or with a burst-rate of 1.7 Hz).\n  expected:\n  - quantity: beta (15 to 25 Hz) burst rate, control rest\n    value: 1.7\n    tolerance: 0.17\n    unit: Hz\n  criterion: File -01, LFP spectrogram in W, readings S1, S2 and E1, E2. Power around 2 Hz is\n    present when the time-averaged spectrum has a local maximum within 1 to 3 Hz, the reading of\n    \"power around 2 Hz\" as a spectral peak. The paper does not define a burst. The one reading the\n    paper's text offers is its own half-height convention (Methods, Duty cycle) applied to the\n    15 to 25 Hz band power over time - a burst is an epoch above halfway between the minimum and\n    maximum of that band power in W. Reproduced when the 2 Hz peak is present and the burst rate\n    is within tolerance under every reading; the author may ask a reader for a burst definition.\n- id: fig3b-control-activated-spectrogram\n  statement: In the control activated state the 2 Hz activity disappears, 15 to 20 Hz power is no\n    longer visible except 15 Hz bursts of about 100 to 500 ms at about 1.5 Hz, and brief (about\n    50 ms) 25 to 35 Hz bursts occur at about 1 Hz.\n  source: Figure 3B legend; Results, Control simulations, paragraph 6\n  quote: During the activated state the 2 Hz activity disappeared and beta bursts shifted to 15 Hz\n    bursts ~100–500 ms in duration or about 1.5 Hz. Beta-band power between 15–20 Hz was no longer\n    visible (Fig. 3B ).\n  expected:\n  - quantity: 15 Hz burst rate, control activated\n    value: 1.5\n    tolerance: 0.15\n    unit: Hz\n  - quantity: 25 to 35 Hz burst rate, control activated\n    value: 1.0\n    tolerance: 0.1\n    unit: Hz\n  criterion: File -03 against file -01, the spectrogram readings and the 2 Hz and burst readings\n    of fig3a-control-rest-spectrogram, with 15 Hz bursts taken in the 14 to 16 Hz band and 25 to\n    35 Hz bursts in that band. Reproduced when the time-averaged spectrum has no local maximum\n    within 1 to 3 Hz, the mean 15 to 20 Hz power is lower than at rest, the burst rates are within\n    tolerance and the 15 Hz burst durations fall within 90 to 550 ms (the reported range widened\n    by 10% of each bound), under every reading.\n- id: control-coincident-spikes\n  statement: In the control condition 1% of PT5B spikes are coincident with another PT5B spike\n    within 1 ms at rest, and 3% in the activated state.\n  source: Results, Control simulations, paragraph 7; Figure 4\n  quote: PT5B spike coincident firing was observed in 1% of spikes at rest and increased to 3%\n    during the activated state\n  expected:\n  - quantity: percent of PT5B spikes coincident within 1 ms, control rest\n    value: 1\n    tolerance: 0.1\n    unit: percent\n  - quantity: percent of PT5B spikes coincident within 1 ms, control activated\n    value: 3\n    tolerance: 0.3\n    unit: percent\n  criterion: Files -01 and -03, PT5B spikes. A spike is coincident when another PT5B neuron fires\n    \"within a 1 ms time window\" (Results, paragraph 7). Open, with readings - (a) another PT5B\n    spike within 1 ms either side, or (b) another PT5B spike in the same 1 ms bin (\"2 or more\n    spikes firing in 1 ms\", Results, Parkinsonian condition, paragraph 7); the window, (i) W, (ii)\n    0.3 to 4.3 s or (iii) 0 to 4.0 s (the unitary-event analysis covers 4.0 s, Fig. 4 legend, and\n    the paper does not say which). Reproduced when, under one combination, both values are within\n    tolerance.\n- id: fig4-control-unitary-events\n  statement: In the control condition, PT5B coincident firing above that expected from\n    rate-matched Poisson processes occurs at rest in 100 to 275 ms clusters with 15 to 24 Hz\n    periodicity (mean 19 Hz), totalling 0.7 of 4.0 s (17.5%), and in the activated state in more\n    frequent 125 to 250 ms clusters totalling 1.1 of 4.0 s (27.5%).\n  source: Figure 4B,D legends; Results, Control simulations, paragraph 7\n  quote: The total duration of significant synchronous activity increased from 0.7 s out of 4.0 s\n    (17.5%) at rest to 1.1 s out of 4.0 s (27.5%).\n  statistics:\n  - about: periods of significant coincident firing\n    test: joint-surprise test (unitary event analysis)\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: duration of significant synchrony, control rest\n    value: 0.7\n    tolerance: 0.07\n    unit: s\n  - quantity: duration of significant synchrony, control activated\n    value: 1.1\n    tolerance: 0.11\n    unit: s\n  - quantity: mean periodicity within significant periods, control rest\n    value: 19\n    tolerance: 1.9\n    unit: Hz\n  criterion: Files -01 and -03, all PT5B spikes. Unitary event analysis (Methods, Identifying\n    synchronous spiking; Grün et al. 1999 and 2002, refs. 77, 24, 87) - coincidences are 2 or more\n    PT5B spikes within 1 ms; the expected count comes from Poisson processes matched to the\n    neurons' rates in a 100 ms window (Fig. 4D legend); a window is significant when the\n    joint-surprise p < 0.05; significant periods are the union of significant windows. Open,\n    with readings - window placement, (a) 100 ms windows slid in 1 ms steps or (b) non-overlapping\n    100 ms windows; the 4.0 s analysed, (i) 0.3 to 4.3 s or (ii) 0 to 4.0 s; the periodicity of a\n    significant period, (x) the peak of the PT5B SCH spectrum within it or (y) the inverse of the\n    mean interval between SCH peaks. Reproduced when, under one combination, the three values are\n    within tolerance, the rest cluster durations fall within 90 to 302.5 ms and the activated\n    within 112.5 to 275 ms (reported ranges widened by 10% of each bound), and the activated\n    state has more significant periods than rest.\n- id: fig5-pd-rest-beta\n  statement: In the parkinsonian condition at rest, M1 activity shows focused beta-band activity at\n    15 Hz.\n  source: Figure 5A legend; Results, Parkinsonian condition, paragraph 1\n  quote: Resting state (250 ms shown at midpoint of 4.3 s simulation) displayed focused 15 Hz\n    beta-band activity.\n  expected:\n    quantity: dominant frequency, parkinsonian rest\n    value: 15\n    tolerance: 1.5\n    unit: Hz\n  criterion: File -02, the measure and readings of fig2-control-rest-beta. Reproduced when the\n    largest spectral peak of the PT5B SCH in W is within 13.5 to 16.5 Hz under every reading; the\n    LFP readings (E1, E2) are reported as variants.\n- id: fig5-pd-activated-gamma\n  statement: In the parkinsonian condition the activated state shifts M1 activity to gamma-band\n    activity of about 43 Hz.\n  source: Figure 5B legend; Results, Parkinsonian condition, paragraph 1\n  quote: Activated state showed change to high-frequency gamma-band activity (~43 Hz).\n  expected:\n    quantity: dominant frequency, parkinsonian activated\n    value: 43\n    tolerance: 4.3\n    unit: Hz\n  criterion: File -04, the measure and readings of fig2-control-rest-beta. Reproduced when the\n    largest spectral peak of the PT5B SCH in W is within 38.7 to 47.3 Hz under every reading; the\n    LFP readings (E1, E2) are reported as variants.\n- id: fig5c-pd-pt5b-rate-activated\n  statement: In the parkinsonian condition PT5B neurons fire more in the activated state than at\n    rest (14.2 +/- 7.1 against 29.7 +/- 12.7 spikes/s, p < 0.001).\n  source: Figure 5C legend; Results, Parkinsonian condition, paragraph 5\n  quote: 'Pyramidal tract neurons had the highest spike rate of any neuronal population during the\n    rest and activated states in the parkinsonian condition (rest: 14.2 ± 7.1 spikes/s; activated:\n    29.7 ± 12.7 spikes/s; p < 0.001; Fig. 5C ).'\n  statistics:\n  - test: not named\n    p: 0.001\n    p_relation: \"<\"\n    n: PT5B neurons of the parkinsonian rest and activated simulations\n  expected:\n  - quantity: PT5B mean rate, parkinsonian rest\n    value: 14.2\n    tolerance: 1.42\n    unit: spikes/s\n  - quantity: PT5B rate standard deviation, parkinsonian rest\n    value: 7.1\n    tolerance: 0.71\n    unit: spikes/s\n  - quantity: PT5B mean rate, parkinsonian activated\n    value: 29.7\n    tolerance: 2.97\n    unit: spikes/s\n  - quantity: PT5B rate standard deviation, parkinsonian activated\n    value: 12.7\n    tolerance: 1.27\n    unit: spikes/s\n  criterion: Files -02 and -04, rates in W, readings R1 and R2. Reproduced when, under one rate\n    reading, all four values are within tolerance and the activated rates are higher with p <\n    0.001 under every test reading T1 to T4.\n- id: fig5c-pd-it23-rate-activated\n  statement: In the parkinsonian condition IT2/3 neurons fire more in the activated state than at\n    rest (0.78 +/- 1.1 against 4.3 +/- 7.1 spikes/s, p < 0.001).\n  source: Figure 5C legend; Results, Parkinsonian condition, paragraph 5\n  quote: 'In contrast, superficial layer IT2/3 neurons significantly increased their average firing\n    rates with activation (rest: 0.8 spikes/s; activated: 4.3 spikes/s; p < 0.001).'\n  statistics:\n  - test: not named\n    p: 0.001\n    p_relation: \"<\"\n    n: IT2/3 neurons of the parkinsonian rest and activated simulations\n  expected:\n  - quantity: IT2/3 mean rate, parkinsonian rest\n    value: 0.78\n    tolerance: 0.078\n    unit: spikes/s\n  - quantity: IT2/3 rate standard deviation, parkinsonian rest\n    value: 1.1\n    tolerance: 0.11\n    unit: spikes/s\n  - quantity: IT2/3 mean rate, parkinsonian activated\n    value: 4.3\n    tolerance: 0.43\n    unit: spikes/s\n  - quantity: IT2/3 rate standard deviation, parkinsonian activated\n    value: 7.1\n    tolerance: 0.71\n    unit: spikes/s\n  criterion: Files -02 and -04, population IT2, rates in W, readings R1 and R2. Reproduced when,\n    under one rate reading, all four values are within tolerance and the activated rates are\n    higher with p < 0.001 under every test reading T1 to T4.\n- id: pd-it5-silenced-activated\n  statement: In the parkinsonian condition IT5A and IT5B neurons fire at 2.2 and 1.2 spikes/s at\n    rest and stop firing (0 spikes/s) in the activated state.\n  source: Results, Parkinsonian condition, paragraph 5\n  quote: IT5A and IT5B firing rates decreased from 2.2 and 1.2 spikes/s, respectively, at rest to 0\n    spikes/s in the activated state.\n  expected:\n  - quantity: IT5A mean rate, parkinsonian rest\n    value: 2.2\n    tolerance: 0.22\n    unit: spikes/s\n  - quantity: IT5B mean rate, parkinsonian rest\n    value: 1.2\n    tolerance: 0.12\n    unit: spikes/s\n  - quantity: IT5A mean rate, parkinsonian activated\n    value: 0\n    tolerance: 0.05\n    unit: spikes/s\n  - quantity: IT5B mean rate, parkinsonian activated\n    value: 0\n    tolerance: 0.05\n    unit: spikes/s\n  criterion: Files -02 and -04, as in control-it5-silenced-activated. Reproduced when all four\n    values are within tolerance.\n- id: pd-it6-rate-unchanged\n  statement: In the parkinsonian condition the IT6 firing rate does not change with activation (6.0\n    spikes/s at rest and in the activated state).\n  source: Results, Parkinsonian condition, paragraph 5\n  quote: 'The firing rates of IT6 neurons did not change (rest and activated: 6.0 spikes/s).'\n  expected:\n  - quantity: IT6 mean rate, parkinsonian rest\n    value: 6.0\n    tolerance: 0.6\n    unit: spikes/s\n  - quantity: IT6 mean rate, parkinsonian activated\n    value: 6.0\n    tolerance: 0.6\n    unit: spikes/s\n  criterion: A claim of absence. Files -02 and -04, IT6 rates in W, readings R1 and R2. The paper\n    names neither the test nor the threshold for this comparison; its other rate comparisons use\n    bounds down to p < 0.05, so the threshold is p < 0.05 and the test readings are T1 to T4.\n    Reproduced when both means are within tolerance under one rate reading and no test reading\n    finds a difference at p < 0.05; not reproduced when a test does. The difference of means and\n    every p-value are reported.\n- id: pd-cv-isi\n  statement: In the parkinsonian condition PT5B spiking is mainly regular at rest (CV 0.34 +/- 0.27;\n    80.6% with CV <= 0.5) and more regular in the activated state (CV 0.18 +/- 0.19; 93.8% regular).\n  source: Results, Parkinsonian condition, paragraph 2\n  quote: In the activated state, PT5B population analysis showed regular spiking that included a\n    small number of irregular spiking neurons (CV 0.18 + /- 0.19; 93.8% CV < = 0.5 regular; 6.2% CV\n    > 0.5 irregular).\n  expected:\n  - quantity: mean PT5B ISI CV, parkinsonian rest\n    value: 0.34\n    tolerance: 0.034\n  - quantity: standard deviation of PT5B ISI CV, parkinsonian rest\n    value: 0.27\n    tolerance: 0.027\n  - quantity: percent of PT5B neurons with CV <= 0.5, parkinsonian rest\n    value: 80.6\n    tolerance: 8.06\n    unit: percent\n  - quantity: mean PT5B ISI CV, parkinsonian activated\n    value: 0.18\n    tolerance: 0.018\n  - quantity: standard deviation of PT5B ISI CV, parkinsonian activated\n    value: 0.19\n    tolerance: 0.019\n  - quantity: percent of PT5B neurons with CV <= 0.5, parkinsonian activated\n    value: 93.8\n    tolerance: 9.38\n    unit: percent\n  criterion: Files -02 and -04, the measure and readings of control-cv-isi. Reproduced when, under\n    one combination of readings, all six values are within tolerance.\n- id: pd-no-subthreshold-oscillations\n  statement: No subthreshold membrane-potential oscillations are seen in PT5B neurons in the\n    parkinsonian rest or activated states.\n  source: Results, Parkinsonian condition, paragraph 3; Figure 5A,B\n  quote: No subthreshold membrane potential oscillations were observed in the parkinsonian rest or\n    active states.\n  depends_on:\n  - control-subthreshold-oscillations\n  criterion: Files -02 and -04, with the detection rule of control-subthreshold-oscillations,\n    which the paper does not give. Blocked as methods_underspecified with that claim unless a\n    question settles the rule; then reproduced when no recorded PT5B neuron meets it in either\n    state.\n- id: pd-activated-vm-more-negative\n  statement: In the activated state, PT5B membrane potential is on average more negative in the\n    parkinsonian than in the control condition, which the paper gives as the reason the EPSPs\n    look larger.\n  source: Results, Parkinsonian condition, paragraph 3\n  quote: Activated state EPSPs appear larger in the parkinsonian in contrast with the control\n    condition due to the greater driving force on EPSP since, on average, the membrane potential is\n    more negative in the parkinsonian condition with its reduced excitability.\n  criterion: Files -03 and -04, somatic membrane potential of the PT5B neurons recorded in both, in\n    W. The paper gives no measure. Readings (a) the mean of each neuron's trace, spikes included,\n    and (b) its median, which spikes barely move. Reproduced when the mean over neurons is lower\n    in the parkinsonian file under both readings; the per-neuron differences are reported.\n- id: pd-duty-cycle\n  statement: In the parkinsonian condition the PT5B duty cycle is 29% at rest and 25% in the\n    activated state.\n  source: Results, Parkinsonian condition, paragraph 4; Figure 5A,B; Methods, Duty cycle\n  quote: The duty cycle was 29% during the parkinsonian rest state (Fig. 5A ) and 25% during\n    activated state (Fig. 5B ; dashed vertical lines not shown).\n  expected:\n  - quantity: PT5B duty cycle, parkinsonian rest\n    value: 29\n    tolerance: 2.9\n    unit: percent\n  - quantity: PT5B duty cycle, parkinsonian activated\n    value: 25\n    tolerance: 2.5\n    unit: percent\n  criterion: Files -02 and -04, the measure and readings of control-duty-cycle. Reproduced when,\n    under one combination, both values are within tolerance.\n- id: fig6a-pd-rest-spectrogram\n  statement: In the parkinsonian rest state the LFP spectrogram shows continuous high-power 15 Hz\n    beta with 25 to 35 Hz bursts of about 50 to 250 ms recurring about every 200 ms (about 5 Hz).\n  source: Figure 6A legend; Results, Parkinsonian condition, paragraph 6\n  quote: LFP spectrograms of resting oscillatory power displayed continuous high-power 15 Hz\n    beta-band power with bursts of power in the ~25–35 Hz (~50–250 ms duration) occurring about\n    once every 200 ms (~5.0 Hz; Fig. 6A ).\n  expected:\n    quantity: 25 to 35 Hz burst rate, parkinsonian rest\n    value: 5.0\n    tolerance: 0.5\n    unit: Hz\n  criterion: File -02, spectrogram readings S1, S2 and E1, E2 in W, bursts as in\n    fig3a-control-rest-spectrogram in the 25 to 35 Hz band. \"Continuous\" 15 Hz power is read with\n    the same half-height convention - the 14 to 16 Hz band power stays above halfway between its\n    minimum and maximum in W for at least 90% of the time, a share the paper does not give (the\n    90% is this reader's, so it is reported, not decisive). Reproduced when the burst rate is\n    within tolerance and the burst durations fall within 45 to 275 ms (reported range widened by\n    10% of each bound) under every reading; the share of time the 15 Hz band is above half-height\n    is reported.\n- id: fig6b-pd-activated-spectrogram\n  statement: In the parkinsonian activated state the LFP spectrogram shows 20 to 35 Hz bursts of\n    about 25 to 100 ms recurring every 50 to 100 ms (about 10 to 20 Hz).\n  source: Figure 6B legend; Results, Parkinsonian condition, paragraph 6\n  quote: In the activated state, ~20–35 Hz bursts ~25–100 ms in duration were seen that occurred\n    every ~50–100 ms (~10–20 Hz; Fig. 6B ).\n  criterion: File -04, the readings of fig6a-pd-rest-spectrogram, bursts in the 20 to 35 Hz band.\n    Reproduced when, under every reading, the burst rate is within 9 to 22 Hz and the median\n    burst duration within 22.5 to 110 ms (the reported ranges widened by 10% of each bound).\n- id: pd-coincident-spikes\n  statement: In the parkinsonian condition 2% of PT5B spikes are coincident (2 or more spikes in 1\n    ms) at rest and 3% in the activated state.\n  source: Results, Parkinsonian condition, paragraph 7; Figure 7\n  quote: PT5B spike coincident firing (2 or more spikes firing in 1 ms) was observed in 2% of spikes\n    at rest and increased to 3% during the activated state\n  expected:\n  - quantity: percent of PT5B spikes coincident within 1 ms, parkinsonian rest\n    value: 2\n    tolerance: 0.2\n    unit: percent\n  - quantity: percent of PT5B spikes coincident within 1 ms, parkinsonian activated\n    value: 3\n    tolerance: 0.3\n    unit: percent\n  criterion: Files -02 and -04, the measure and readings of control-coincident-spikes. Reproduced\n    when, under one combination, both values are within tolerance.\n- id: fig7-pd-unitary-events\n  statement: In the parkinsonian condition, significant PT5B coincident firing occurs at rest in\n    400 to 1100 ms clusters of 6 to 16 periods at 14 to 15 Hz (mean 15 Hz), totalling 3.1 of 4.0 s\n    (77.5%), and in the activated state in 100 to 350 ms epochs totalling 1.4 of 4.0 s (35.0%).\n  source: Figure 7B,D legends; Results, Parkinsonian condition, paragraph 7\n  quote: The total duration of significant synchronous activity during rest was 3.1 s out of 4.0 s\n    (77.5%). During the activated state, 1.4 s of 4.0 s (35.0%), was significantly synchronous.\n  statistics:\n  - about: periods of significant coincident firing\n    test: joint-surprise test (unitary event analysis)\n    p: 0.05\n    p_relation: \"<\"\n  expected:\n  - quantity: duration of significant synchrony, parkinsonian rest\n    value: 3.1\n    tolerance: 0.31\n    unit: s\n  - quantity: duration of significant synchrony, parkinsonian activated\n    value: 1.4\n    tolerance: 0.14\n    unit: s\n  - quantity: mean periodicity within significant periods, parkinsonian rest\n    value: 15\n    tolerance: 1.5\n    unit: Hz\n  criterion: Files -02 and -04, the method and readings of fig4-control-unitary-events.\n    Reproduced when, under one combination, the three values are within tolerance, the rest\n    cluster durations fall within 360 to 1210 ms and the activated within 90 to 385 ms (reported\n    ranges widened by 10% of each bound).\n- id: rest-pt5b-rate-pd-vs-control\n  statement: At rest, PT5B firing rate is higher and less variable in the parkinsonian than in the\n    control condition (14.2 +/- 7.1 against 11.7 +/- 9.4 spikes/s, p < 0.001), a paradoxical\n    increase given the reduced PT5B excitability.\n  source: Results, Control vs parkinsonian comparison, paragraph 1; Discussion, paragraph 1\n  quote: 'The most substantial changes in firing between conditions were seen in the simulated rest\n    state, where there was a significant increase in PT5B firing rate and a decrease in firing rate\n    variability in the parkinsonian condition as compared with control condition (control: 11.7 ±\n    9.4 spikes/s; parkinsonian: 14.2 ± 7.1 spikes/s; p < 0.001).'\n  statistics:\n  - test: not named\n    p: 0.001\n    p_relation: \"<\"\n    n: PT5B neurons of the control and parkinsonian rest simulations\n  depends_on:\n  - fig2c-control-pt5b-rate-activated\n  - fig5c-pd-pt5b-rate-activated\n  criterion: Files -01 and -02, rates in W, readings R1 and R2, with the expected values of the\n    two claims it depends on. Reproduced when, under one rate reading, the four rest values are\n    within tolerance, the parkinsonian mean is higher with p < 0.001 under every test reading T1\n    to T4 (paired readings pair neurons by index, the network being the same), and the\n    parkinsonian standard deviation is lower. The paper names no test of the variability; the\n    standard deviations are compared as numbers.\n- id: rest-it4-rate-pd-vs-control\n  statement: At rest, IT4 firing rate is higher in the parkinsonian than in the control condition\n    (14.1 against 2.6 spikes/s, p < 0.05).\n  source: Results, Control vs parkinsonian comparison, paragraph 1\n  quote: 'There was also an increase in IT4 firing rate (control: 2.6 spikes/s; parkinsonian: 14.1\n    spikes/s; p < 0.05)'\n  statistics:\n  - test: not named\n    p: 0.05\n    p_relation: \"<\"\n    n: IT4 neurons of the control and parkinsonian rest simulations\n  expected:\n  - quantity: IT4 mean rate, control rest\n    value: 2.6\n    tolerance: 0.26\n    unit: spikes/s\n  - quantity: IT4 mean rate, parkinsonian rest\n    value: 14.1\n    tolerance: 1.41\n    unit: spikes/s\n  criterion: Files -01 and -02, rates in W, readings R1 and R2. Reproduced when, under one rate\n    reading, both values are within tolerance and the parkinsonian rate is higher with p < 0.05\n    under every test reading T1 to T4.\n- id: rest-it5a-rate-pd-vs-control\n  statement: At rest, IT5A firing rate is lower in the parkinsonian than in the control condition\n    (2.2 against 3.3 spikes/s, p < 0.01).\n  source: Results, Control vs parkinsonian comparison, paragraph 1\n  quote: 'a decrease in IT5A firing rate (control: 3.3 spikes/s; parkinsonian: 2.2 spikes/s; p <\n    0.01)'\n  statistics:\n  - test: not named\n    p: 0.01\n    p_relation: \"<\"\n    n: IT5A neurons of the control and parkinsonian rest simulations\n  expected:\n  - quantity: IT5A mean rate, control rest\n    value: 3.3\n    tolerance: 0.33\n    unit: spikes/s\n  - quantity: IT5A mean rate, parkinsonian rest\n    value: 2.2\n    tolerance: 0.22\n    unit: spikes/s\n  criterion: Files -01 and -02, rates in W, readings R1 and R2. Reproduced when, under one rate\n    reading, both values are within tolerance and the parkinsonian rate is lower with p < 0.01\n    under every test reading T1 to T4.\n- id: activated-pt5b-rate-pd-vs-control\n  statement: In the activated state, PT5B firing rate is higher and less variable in the\n    parkinsonian than in the control condition (29.7 +/- 12.7 against 26.8 +/- 18.2 spikes/s, p <\n    0.001).\n  source: Results, Control vs parkinsonian comparison, paragraph 1\n  quote: 'Activated (movement-associated) cortical dynamics also showed a significant increase in\n    PT5B firing rate and a decrease in firing rate variability in the parkinsonian condition as\n    compared with control condition (control: 26.8 ± 18.2 spikes/s; parkinsonian: 29.7 ± 12.7\n    spikes/s; p < 0.001).'\n  statistics:\n  - test: not named\n    p: 0.001\n    p_relation: \"<\"\n    n: PT5B neurons of the control and parkinsonian activated simulations\n  depends_on:\n  - fig2c-control-pt5b-rate-activated\n  - fig5c-pd-pt5b-rate-activated\n  criterion: Files -03 and -04, as in rest-pt5b-rate-pd-vs-control, with the four activated\n    values. The Discussion (paragraph 1) says the opposite, that there was no significant change\n    in PT5B population firing rate in the activated state; this claim follows the Results, which\n    give the numbers, and the outcome under every test reading is reported for both.\n- id: activated-it6-rate-pd-vs-control\n  statement: In the activated state, IT6 firing rate is higher in the parkinsonian than in the\n    control condition (6.0 against 3.5 spikes/s, p < 0.001).\n  source: Results, Control vs parkinsonian comparison, paragraph 1\n  quote: 'The firing rate of IT6 neurons also increased in the parkinsonian condition (control: 3.5\n    spikes/s; parkinsonian: 6.0 spikes/s; p < 0.001).'\n  statistics:\n  - test: not named\n    p: 0.001\n    p_relation: \"<\"\n    n: IT6 neurons of the control and parkinsonian activated simulations\n  expected:\n  - quantity: IT6 mean rate, control activated\n    value: 3.5\n    tolerance: 0.35\n    unit: spikes/s\n  - quantity: IT6 mean rate, parkinsonian activated\n    value: 6.0\n    tolerance: 0.6\n    unit: spikes/s\n  criterion: Files -03 and -04, rates in W, readings R1 and R2. Reproduced when, under one rate\n    reading, both values are within tolerance and the parkinsonian rate is higher with p < 0.001\n    under every test reading T1 to T4.\n- id: rest-beta-power-order-of-magnitude\n  statement: At rest, LFP beta power around 15 Hz is an order of magnitude larger in the\n    parkinsonian than in the control condition.\n  source: Discussion, paragraph 3; Figures 3A and 6A (colour bars x 10^-5 and x 10^-4)\n  quote: In the resting state, an order of magnitude increase in beta power was observed around 15\n    Hz.\n  criterion: Files -01 and -02, LFP in W, readings S1, S2 and E1, E2. The paper shows the increase\n    by the colour scales of Figs. 3 and 6 and gives no band; \"around 15 Hz\" is read as (a) the\n    power at 15 Hz and (b) the mean power over 14 to 16 Hz (the range of the parkinsonian rest\n    periodicity, Results, Parkinsonian condition, paragraph 7). The ratio of time-averaged\n    parkinsonian to control power is computed. \"An order of magnitude\" is read as a ratio that\n    rounds to 10 on a log scale, from 10^0.5 (3.16) to 10^1.5 (31.6), since the paper gives no\n    number. Reproduced when the ratio lies in that range under every reading; not reproduced\n    when it is below 3.16 under every reading.\n- id: activated-20-35hz-power-pd-vs-control\n  statement: In the activated state, the parkinsonian condition shows more power at 20 to 35 Hz than\n    the control condition.\n  source: Discussion, paragraph 1; Figures 3B and 6B\n  quote: Parkinsonism-associated changes were less marked in the activated (movement) state, where\n    we found no significant change in PT5B population firing rate but did see a change in PT5B\n    activity pattern with an increase in power of 20–35 Hz activity\n  criterion: Files -03 and -04, LFP in W, readings S1, S2 and E1, E2, and the PT5B SCH spectrum\n    (the sentence speaks of PT5B activity, the figures of the LFP). The paper gives no size or\n    test. Reproduced when the mean 20 to 35 Hz power is higher in the parkinsonian file under\n    every reading; the ratios are reported.\n- id: rest-synchrony-increase\n  statement: At rest, PT5B spike synchrony is substantially larger in the parkinsonian than in the\n    control condition (significant synchrony 3.1 against 0.7 of 4.0 s).\n  source: Discussion, paragraphs 1 and 6; Figures 4B and 7B\n  quote: We found a substantial increase in synchronous spiking in our simulations of the\n    parkinsonian rest state.\n  depends_on:\n  - fig4-control-unitary-events\n  - fig7-pd-unitary-events\n  criterion: Files -01 and -02, the unitary-event method and readings of\n    fig4-control-unitary-events. Reproduced when the total duration of significant synchrony at\n    rest is larger in the parkinsonian file under every reading; the durations come from the two\n    claims it depends on, with their expected values.\n"
}
```

```
File created successfully at: claims/001444/10.1038-s41531-025-01070-4.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001444/10.1038-s41531-025-01070-4.yaml paper/10.1038-s41531-025-01070-4.txt; grep -n "—\|rather" claims/001444/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/001444/10.1038-s41531-025-01070-4.yaml",
 "old_string": "  - quantity: decrease of PT5B spike count averaged across current injections, parkinsonian against\n    control",
 "new_string": "  - quantity: PT5B spike count decrease across current injections, parkinsonian against control"
}
```

```
The file claims/001444/10.1038-s41531-025-01070-4.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/001444/10.1038-s41531-025-01070-4.yaml paper/10.1038-s41531-025-01070-4.txt 2>&1 | tail -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
f=claims/001444/10.1038-s41531-025-01070-4.yaml; grep -c "—" $f; grep -ci "rather" $f; python3 -c "
import yaml;d=yaml.safe_load(open('$f'));c=d['claims']
print(len(c),sum('quote' in x for x in c),sum('statistics' in x for x in c),sum(len(x.get('statistics',[])) for x in c),sum('criterion' in x for x in c),sum('expected' in x for x in c))
import re
for x in c:
  for k,v in x.items():
    if isinstance(v,str) and ': ' in v and k!='quote': print(x['id'],k)"
```

```
0
0
40 40 12 12 40 30
```

**Agent**

I wrote `claims/001444/10.1038-s41531-025-01070-4.yaml`. The quote checker passes: 40 claims, 40 quotes, 12 statistical values, 0 problems. Nothing is committed.

**Text read.** I used the version of record (npj Parkinson's Disease 11:230, 2025, from Europe PMC): main text, figure legends and Methods. Its title differs from the one in the task; it is the same DOI. The bioRxiv preprint was also supplied, but it is an earlier version with another title, so I took no claims from it. The supplement was not supplied (Supplementary Tables 1 to 3, Supplementary Figs. 1 to 5). I did not stop, because the main text reports every main result from one simulation set, sM1_12-12-2023.

**Code read.** The linked repository is `suny-downstate-medical-center/pd_m1_6ohda`, read at commit 0a1f0e8 (2025-08-20). It holds the NetPyNE simulation, the parameters for the four conditions, and four notebooks. The notebooks map the files -01 to -04 to control rest, parkinsonian rest, control activated and parkinsonian activated. They also show which LFP electrode and which five voltage traces the figures use. The repository has no analysis code: nothing for firing rates, statistical tests, CV, duty cycle, spectrograms, coincidences or unitary events.

**Claims.**
- 40 claims, all with quotes, none marked `inferred`.
- 12 claims carry statistics. Ten are firing-rate p-bounds, and the paper never names their test. Two are joint-surprise tests at p < 0.05.
- All 40 have a criterion, and 30 have expected values. Tolerances are 10%, except a count with zero tolerance, zero rates at ±0.05 (the paper's rounding), and "an order of magnitude" read as a ratio between 3.16 and 31.6.
- All claims use `data: dataset`.

**Details the paper leaves open, and the readings named:**
- **Rate test:** Wilcoxon signed-rank, paired t, Mann-Whitney U or Welch t. Pairing is possible because the four simulations of a set share the same seeds.
- **Rate population:** all neurons, or only neurons that spike.
- **Spectra:** NetPyNE's Morlet spectrogram or a short-time Fourier transform; electrode 0 (the one the notebooks plot) or the mean of the 11 electrodes.
- **Dominant frequency:** the peak searched above 0 Hz or above 5 Hz; the spike-count histogram decides, and the LFP is a variant.
- **CV:** window 2.0 to 4.3 s or the whole 4.3 s; neurons with at least one or at least two ISIs.
- **Duty cycle:** half-height from the whole window or from each period; window 0.25 s or 2.3 s.
- **Coincidence:** within ±1 ms or in the same 1 ms bin; window 2.0–4.3 s, 0.3–4.3 s or 0–4.0 s.
- **Unitary events:** 100 ms windows slid in 1 ms steps or non-overlapping; periodicity from the spectral peak or from the interval between peaks.
- **Bursts:** the paper defines none. The only reading the text offers is its own half-height convention. I flagged the 90% threshold for "continuous" 15 Hz power as my own choice, so it is reported but does not decide the outcome.
- **"Around 15 Hz":** the 15 Hz bin or 14 to 16 Hz.
- **Membrane potential:** the mean or the median of each trace.

**Missing or contradictory in the paper:**
- **Supplement:** Supplementary Table 2 holds the robustness results for the other three simulation sets, so `robustness-four-sets` is blocked until a reader with the supplement completes it. Supplementary Fig. 1 holds the current-injection protocol behind the 64% excitability decrease, so that claim is also unfixable.
- **No detection rule:** the paper gives none for subthreshold oscillations, so `control-subthreshold-oscillations` (57.4% of PT5B neurons) and `pd-no-subthreshold-oscillations` are blocked unless a question to a reader settles it.
- **Activated PT5B rate:** the Results report a significant increase in the parkinsonian condition (p < 0.001), but the Discussion says there was no significant change. The claim follows the Results.
- **Duty-cycle period:** the Methods define a period as running from the rising to the falling crossing, which would make every duty cycle 100%. I followed the Results, where a period runs from one rising crossing to the next.
- **Small mismatches:** IT2/3 activated rate is 6.7 in the legend and 6.6 in the text; the 10% tolerance covers both. In the code, NaT goes up 20-fold, while the Methods call it "a small increase".

## End of run

25 turns, 7 minutes, result: success.
