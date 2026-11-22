# russo-2025 · claims · run 44940556254

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "^#" docs/protocol.md; ls paper/ ; ls claims | head; wc -c paper/*
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md",
 "offset": 1,
 "limit": 200
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-18`. Record this version in the attempt's provenance.
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

**Agent calls Bash**

```bash
cat papers/datasets/russo-2025.yaml 2>/dev/null; head -c 3000 paper/10.1038-s41467-025-58717-2.txt; ls -t claims | head -5; cat tools/claims_check.py | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
head -30 claims/zhuang-2025.yaml; wc -l paper/*.txt; fold -w 4000 -s paper/10.1038-s41467-025-58717-2.txt | wc -l
```

Result: not kept, because it reads the paper's text.

**Agent**

The text has line structure. Reading the paper now.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-025-58717-2.txt",
 "offset": 7,
 "limit": 400
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-025-58717-2.txt",
 "offset": 7,
 "limit": 120
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
awk '{print NR": "length($0)}' paper/10.1038-s41467-025-58717-2.txt | sort -t: -k2 -n -r | head -5
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n 7p paper/10.1038-s41467-025-58717-2.txt | fold -w 1000 -s > main.txt; wc -l main.txt; sed -n '8,40p' paper/10.1038-s41467-025-58717-2.txt | cut -c1-200
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt"
}
```

```
1	pmc Nat Commun Nat Commun Nature Communications 2041-1723 Nature Publishing Group UK London 12003640 40240330 58717 10.1038/s41467-025-58717-2 Article Thalamic feedback shapes brain responses evoked by cortical stimulation in mice and humans Russo Simone 1 2 3 4 http://orcid.org/0000-0002-4030-9171 Claar Leslie D. 3 Furregoni Giulia 1 5 http://orcid.org/0000-0002-7270-2680 Marks Lydia C. 3 Krishnan Giri 6 http://orcid.org/0000-0002-7328-6068 Zauli Flavia Maria 1 2 7 Hassan Gabriel 1 2 Solbiati Michela 1 7 d’Orio Piergiorgio 7 8 http://orcid.org/0000-0001-7259-6120 Mikulan Ezequiel 9 Sarasso Simone 1 Rosanova Mario 1 Sartori Ivana 7 Bazhenov Maxim 6 10 http://orcid.org/0000-0002-1856-3413 Pigorini Andrea 11 12 http://orcid.org/0000-0003-2271-957X Massimini Marcello 1 13 14 http://orcid.org/0000-0001-6482-8067 Koch Christof 3 http://orcid.org/0000-0001-7121-4442 Rembado Irene [removed: an e-mail address] 3 1 https://ror.org/00wjc7c48 grid.4708.b 0000 0004 1757 2822 Department of 
2	Biomedical and Clinical Sciences, Università degli Studi di Milano, Milan, 20157 Italy 2 https://ror.org/00wjc7c48 grid.4708.b 0000 0004 1757 2822 Department of Philosophy ‘Piero Martinetti’, University of Milan, Milan, Italy 3 https://ror.org/03cpe7c52 grid.507729.e Brain and Consciousness, Allen Institute, Seattle, USA 4 https://ror.org/02j15s898 grid.470935.c Wallace H Coulter Department of Biomedical Engineering, Georgia Institute of Technology and Emory University, Atlanta, GA USA 5 https://ror.org/0005w8d69 grid.5602.1 0000 0000 9745 6549 School of Advanced Studies, Center of Neuroscience, University of Camerino, Camerino, Italy 6 https://ror.org/0168r3w48 grid.266100.3 0000 0001 2107 4242 Department of Medicine, University of California San Diego, La Jolla, CA 92093 USA 7 https://ror.org/00htrxv69 grid.416200.1 ASST Grande Ospedale Metropolitano Niguarda, “C. Munari” Epilepsy Surgery Centre, Milan, Italy 8 https://ror.org/02k7wn190 grid.10383.39 0000 0004 1758 0937 University 

[... 51 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 54,
 "limit": 45
}
```

```
54	hyperpolarizing the thalamus after cortical stimulation, which in turn enables the thalamic rebound response (Fig. 5B ). Our results are in line with previous findings showing that stimulation of the cortico-thalamic pathway triggers a prominent depolarization followed by a long-lasting hyperpolarization frequently ending with a burst discharge of thalamic relay cells 83 , 84 . In some cases, the hyperpolarization remained even after lesioning the reticular thalamic complex 83 , suggesting that sources other than the TRN can induce inhibitory postsynaptic potentials (IPSP). Although both studies 83 , 84 attributed the remaining IPSPs to other thalamic interneurons, an earlier experiment that inactivated visual cortex via cooling led to a decrease of baseline firing rate and changes of response features to visual stimuli in the directly connected units of the lateral geniculate thalamic nucleus 85 . This study demonstrated that the lack of cortical inputs can suppress thalamic activity 
55	85 , as also confirmed by our simulated (Fig. 4 ) and optogenetic data (Fig. 2 , S8 ). This mechanism coexists with the IPSPs followed by a rebound burst of TC neurons induced by TRN 86 and shaped by neuromodulators associated to different states of arousal. Importantly the state of the subject, i.e. anesthetized versus awake, could affect the time course of the responses 21 . However, the time course of the off-period here described is in line with a reduction of cortical excitatory PSPs (EPSPs) and a reduction of firing probability of TC neurons evoked by a thalamic electrical pulse when a conditioning paired pulse was delivered to the cortex of anesthetized cats up to 100 ms before it 87 . Interestingly, the electrically evoked responses elicited by cortical stimulation resemble the interictal spikes spontaneously occurring in epileptic patients (data not shown because intentionally excluded from the analyzed dataset used for this study). From a mechanistic perspective, both 
[... 43 more lines not kept]
```

**Agent**

Main text and Methods are present. Next I'm checking whether the supplement's text is in the .txt file or only in the PDF.

**Agent calls Bash**

```bash
cd paper; grep -n -i "supplementary fig\|Figure S1\b\|Fig\. S4\|^Figure S" 10.1038-s41467-025-58717-2.txt | sed -n '1,20p' | cut -c1-200; grep -n "^=\|^---\|^\[" 10.1038-s41467-025-58717-2.txt | head; which pdftotext
```

```
Exit code 1
7:pmc Nat Commun Nat Commun Nature Communications 2041-1723 Nature Publishing Group UK London 12003640 40240330 58717 10.1038/s41467-025-58717-2 Article Thalamic feedback shapes brain responses evoked
567:Figure S1. Behavioral-state-dependent modulation of the phase-locking factor (PLF) in humans and 
593:Figure S2. Controls for the TMS-EEG experiments in humans. 
633:Figure S3. Monopolar derivation of the iEEG recording and associated quantifications. 
653:Figure S4. Modulation of the late response evoked by electrical stimulation of MOs in mice as a 
679:Figure S5. Modulation of the early component evoked by the electrical stimulation of MOs in mice 
697:Figure S6. Lack of modulation of both early and late responses across recording modalities evoked 
717:Figure S7. Latencies of the rebound responses at rest and active state across recording modalities 
745:Figure S8. Characterization of the units’ responses to optogenetic stimulation of GABAergic 
778:Figure S9. Lack of modulation of MOs and SM-TH firing rate at rest and during active state.  
802:Figure S10. Electrically evoked responses of cortical and thalamic GABAergic neurons. 
838:Figure S12. Current intensity modulates the relative percentage of thalamic units classified as LF 
880:Figure S14. Characterization of the cortical and thalamic responses to cortical stimulation in the 
6:------------------------------------------------------------------------
9:[HYPERLINKS]
664:= 0.89, ns).  
2195:[... cut at 60000 characters; the whole file is 41467_2025_58717_MOESM4_ESM.xlsx beside this text]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.1038-s41467-025-58717-2.txt",
 "offset": 520,
 "limit": 420
}
```

Result: not kept, because it reads the paper's text.

**Agent**

The full text, Methods and supplement legends are all present. Next I'll try to fetch the paper's mouse analysis code from figshare.

**Agent calls Bash**

```bash
cd $TMPDIR; for id in 28047749 25595829 25595871 25773501; do curl -sL "https://api.figshare.com/v2/articles/$id" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('title'), d.get('version'), d.get('published_date')); [print(' ', f['name'], f['size'], f['download_url']) for f in d.get('files',[])]"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -o mouse.zip https://ndownloader.figshare.com/files/51254174 && unzip -l mouse.zip | grep -v -i "\.npy\|\.pkl\|\.png\|\.svg\|\.pdf" | head -80; unzip -l mouse.zip | tail -1
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; unzip -q -o mouse.zip -d code; unzip -l mouse.zip | grep -v "\.git/" ; cat code/DataAnalysesMouse/Notes.txt; cd code/DataAnalysesMouse/tbd_eeg && git log --oneline | head -3; git remote -v
```

```
Archive:  mouse.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
        0  2024-07-18 13:23   DataAnalysesMouse/
      329  2024-12-17 18:19   DataAnalysesMouse/Notes.txt
        0  2024-07-18 13:20   DataAnalysesMouse/tbd_eeg/
        0  2022-05-09 16:45   DataAnalysesMouse/tbd_eeg/.ipynb_checkpoints/
     1540  2024-07-18 13:20   DataAnalysesMouse/tbd_eeg/CONTRIBUTING.md
     3390  2024-07-18 13:20   DataAnalysesMouse/tbd_eeg/environment.yml
     1969  2024-07-18 13:20   DataAnalysesMouse/tbd_eeg/LICENSE
     3200  2024-07-18 13:20   DataAnalysesMouse/tbd_eeg/README.md
     1297  2024-07-18 13:20   DataAnalysesMouse/tbd_eeg/setup.py
        0  2024-07-18 13:22   DataAnalysesMouse/tbd_eeg/tbd_eeg/
        0  2024-07-18 13:20   DataAnalysesMouse/tbd_eeg/tbd_eeg/.vscode/
       81  2024-07-18 13:20   DataAnalysesMouse/tbd_eeg/tbd_eeg/.vscode/settings.json
        0  2024-07-18 13:20   DataAnalysesMouse/tbd_eeg/tbd_eeg/AdditionalUtilities/
     5674  2024-07-18 13:20   DataAnalysesMouse/tbd_eeg/tbd_eeg/AdditionalUtilities/filters.py
    27394  2024-07-18 13:20   DataAnalysesMouse/tbd_eeg/tbd_eeg/AdditionalUtilities/units_analysis.py
     5197  2024-07-18 13:20   DataAnalysesMouse/tbd_eeg/tbd_eeg/AdditionalUtilities/utilities.py
        0  2024-07-18 13:20   DataAnalysesMouse/tbd_eeg/tbd_eeg/AdditionalUtilities/__pycache__/
[... 118 more lines not kept]
```

**Agent**

I have the mouse analysis code (figshare 10.6084/m9.figshare.28047749 v1, a snapshot of AllenInstitute/tbd_eeg with My_scripts). Extracting its code cells now.

**Agent calls Bash**

```bash
cd $TMPDIR/code/DataAnalysesMouse/tbd_eeg/tbd_eeg/My_scripts; python3 - <<'EOF'
import json
for nb in ["MainScript.ipynb","MainScript_Opto.ipynb"]:
    d=json.load(open(nb))
    out=open("/tmp/claude-1001/"+nb+".py","w")
    for i,c in enumerate(d["cells"]):
        src="".join(c["source"])
        out.write(f"\n# ---- cell {i} [{c['cell_type']}]\n"+src+"\n")
    print(nb,len(d["cells"]))
EOF
wc -l /tmp/claude-1001/*.ipynb.py; wc -l ../AdditionalUtilities/*.py
```

```
MainScript.ipynb 1211
MainScript_Opto.ipynb 1235
  17412 /tmp/claude-1001/MainScript.ipynb.py
  16888 /tmp/claude-1001/MainScript_Opto.ipynb.py
  34300 total
  185 ../AdditionalUtilities/filters.py
  550 ../AdditionalUtilities/units_analysis.py
  134 ../AdditionalUtilities/utilities.py
  869 total
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n -A3 "\[markdown\]" MainScript.ipynb.py | grep -v "^\-\-$" | grep -v "cell" | grep -v "^[0-9]*-$" | cut -c1-160 | head -250
```

```
2382-# Auto-corr and Cross-corr per trial
2893-# Origin of the rebound within unit - baseline firing rate VS rebound latency VS ISI
3202-# Correlation baseline firing rate VS 2np peak EEG latency/amplitude
3289-# Correlation EEG 2np peak amplitude VS latency
3372-# Histogram spike width
3455-# Rebound ISI Thalamus and Cortex _ Fs VS Rs
7089-# % High-firing and low-firing units in each thalamic nucleus - per area
7090-## Write High-firing Low-firing indexes
7284-# Dose-response - does HF and LF populations shift between intensities?
7480-# Percentage of HF and LF units for each mouse
7568-# Dose-response Thalamus and Cortex _ Fs VS Rs
7919-# Early response of HF and LF units
8057-# State-dependent and -independent contributions to CSD
8272-# Origin of the response - FR vs EEG Pw
8381-# Origin of response Thalamic VS cortical firing rate 
8523-# Dose-response Inter-trial variability
8632-# Test different EEG references
8709-# Create grand average EEG
8813-# Create grand average CSD/LFP
9158-# Dose reponse analysis - EEG
[... 44 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 1,200p MainScript.ipynb.py | cut -c1-220
```

```
# ---- cell 0 [code]
# Import packages

import os
import sys
import json
import time
import scipy
import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.signal import hilbert, chirp
import csv
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from itertools import groupby
import pickle
#import tftb
import matlab.engine
[... 180 more lines not kept]
```

**Agent**

Now the key sections: EEG, CSD/LFP and units rest-run analyses.

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 15755,16140p MainScript.ipynb.py | cut -c1-200
```

```
# EEG Rest-Run Analysis

# ---- cell 1125 [code]
DataFrame = LoadDF_DataFrame()
#DataFrame = FilterDF(DataFrame, 'Npx_GoodBad', 1)
DataFrame = FilterDF(DataFrame, 'EEG_GoodBad', 1)
DataFrame = FilterDF(DataFrame, 'brain_states', 'awake', 'contains')
#DataFrame = FilterDF(DataFrame, 'brain_states', 'ISO', 'contains')
#DataFrame = FilterDF(DataFrame, 'Npx', ('F', 'B'))
#DataFrame = FilterDF(DataFrame, 'Npx', ('F'))
DataFrame = FilterDF(DataFrame, 'stim_depth_label', ('deep','unique'))
#DataFrame = FilterDF(DataFrame, 'stim_int_label', ('max','unique'))
#DataFrame = FilterDF(DataFrame, 'stim_int_label', ('min'))
DataFrame = FilterDF(DataFrame, 'stim_int_label', ('max','mid'))
#DataFrame = FilterDF(DataFrame, 'stim_target_area', ('M2','M2-frontal'))
DataFrame = FilterDF(DataFrame, 'stim_area', ('CA3 from ephys', 'VIS4', 'RSPagl6 from ephys', 'VISrl5')) #'CA2' 'CA3 from ephys' 'VIS4' 'RSPagl6 from ephys' 
#'VISrl5' ???

###################################################################
################################################################### Drop equal sessions
[... 367 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n "^def \|^    def " MainScript.ipynb.py | head -100
```

```
72:def find_ones(xs):
83:def find_nearest(array, value):
88:def moving_average(x, w):
91:def moving_average_2dim(x, w):
94:def moving_average_gaussian(x, w):
99:def moving_average_gaussian_2dim(x, w):
105:def calc_time_to_first_spike(data):
121:def get_evoked_traces(data, timestamps, events, plot_before, plot_after, data_sample_rate):
136:def surface_laplacian_SR(data, leg_order, m, smoothing, locs):
179:    def cart2sph(x, y, z):
274:def get_index_positions(list_of_elems, element):
292:def ImshowAreas(data, Ts, Areas,MinMax = (-1,1), Mask = 'none'):
322:def ImshowAreasAreas(Matrix, Areas1, Areas2, MaxMin = (0,1), Title = '', ColorBarLabel = ''):
358:def PlotWithAreas(data, Ts, FullNames):
388:def ImshowAndPlotAreas(data, Ts, Areas, data2, Ts2, Areas2, MinMax = (-1,1), PlotScaling = 1, Axis = 'new'):
466:def PlotEEG_CSD_PSTH(currDataFrame, XLim = (-1,1), AvgRef = True):
507:def ButterflyPlot_EEG(currDataFrame, XLim=(-1,1), AvgRef = 0, HighlightCh = 'auto'):
537:def RemoveNulls(data, Areas):
544:def AutocleanLFP(InputData):
671:def get_index_multipleAreas(SampledAreas, AreasOfInterest):
[... 67 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n '957,1060p;1294,1335p;1517,1522p;1550,1557p;1607,1662p;1697,1730p;2136,2200p' MainScript.ipynb.py | cut -c1-200
```

```
def DFLoad_SplittedEEG(currSessDF, BadChsAction = 'nan', BadTrialsAction = 'nan', MainFolder =  r'E:\AllenInstitute\Data'):
    currSessFolder = MainFolder + '\\' + currSessDF['mouse_name'].values[0] + '\\' + currSessDF['exp_name'].values[0] + '\\' + 'EEG' + '\\' + str(int(currSessDF['sweep_num'].values[0])) + '_' + currSe
    SplittedEEG = np.load(currSessFolder + 'SplittedEEG.npy')
    TsEEG = np.load(currSessFolder + 'TsEEG.npy')
    if BadChsAction == 'keep': 
        SplittedEEG = SplittedEEG
    elif BadChsAction == 'reject': 
        if not pd.isnull(currSessDF['EEG bad_channels'].values[0]):
            if type(currSessDF['EEG bad_channels'].values[0]) == int:
                SplittedEEG = np.delete(SplittedEEG, currSessDF['EEG bad_channels'].values[0], axis=1)
            else:
                ChsIndexesToRemove = [int(x) for x in currSessDF['EEG bad_channels'].values[0].split(',')]
                SplittedEEG = np.delete(SplittedEEG, ChsIndexesToRemove, axis=1)
        else: 
            SplittedEEG = SplittedEEG
    elif BadChsAction == 'nan':
        if not pd.isnull(currSessDF['EEG bad_channels'].values[0]):
            if type(currSessDF['EEG bad_channels'].values[0]) == int:
                SplittedEEG[:,currSessDF['EEG bad_channels'].values[0],:] = np.nan
            else:
[... 296 more lines not kept]
```

**Agent**

Checking how the per-trial wheel speed is computed.

**Agent calls Bash**

```bash
cd $TMPDIR/code/DataAnalysesMouse/tbd_eeg/tbd_eeg/My_scripts/CreateExportedData; python3 - <<'EOF'
import json
for nb in ["CreateWheelVelocityPerTrial.ipynb","CreateEvokedEEGFolder.ipynb","CreateCleanedEvokedEEG.ipynb"]:
    d=json.load(open(nb))
    print("=====",nb)
    for i,c in enumerate(d["cells"]):
        if c["cell_type"]=="code":
            s="".join(c["source"])
            if s.strip(): print(f"--- cell {i}\n{s[:3000]}")
EOF
```

```
===== CreateWheelVelocityPerTrial.ipynb
--- cell 0
# Import packages

import os
import sys
import json
import time
import scipy
import numpy as np
import pandas as pd
from scipy.stats import norm
from scipy.signal import hilbert, chirp
import csv
import matplotlib.pyplot as plt

sys.path.append(r'C:\Users\simone.russo\Documents\GitHub')

from tbd_eeg.tbd_eeg.data_analysis.eegutils import EEGexp
from tbd_eeg.tbd_eeg.data_analysis.Utilities.utilities import get_stim_events, find_nearest_ind
[... 828 more lines not kept]
```

**Agent**

Wheel speed: mean linear velocity over ±0.5 s, threshold 0.1 cm/s, confirmed. Now the LFP/CSD and units rest-run cells.

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 16134,16560p MainScript.ipynb.py | grep -v "savefig" | cut -c1-200
```

```
# CSD/LFP Rest-Run Analysis

# ---- cell 1144 [code]

currentAreaOfInterest = areas_of_interest['MO']
#currentAreaOfInterest = areas_of_interest['CTX']
#AreasOfInterestForControlAreas = ['Hip','Hip','VIS','VIS','VIS','VIS','RSPagl','RSPagl','VISrl','VISrl','VISrl','VISrl']


DataFrame = LoadDF_DataFrame()
DataFrame = FilterDF(DataFrame, 'Npx_GoodBad', 1)
DataFrame = FilterDF(DataFrame, 'brain_states', 'awake', 'contains')
DataFrame = FilterDF(DataFrame, 'stim_depth_label', ('deep','unique'))
#DataFrame = FilterDF(DataFrame, 'stim_int_label', ('max','unique'))
#DataFrame = FilterDF(DataFrame, 'stim_int_label', ('min'))
DataFrame = FilterDF(DataFrame, 'stim_int_label', ('mid','max','unique'))
#DataFrame = FilterDF(DataFrame, 'stim_target_area', ('M2','M2-frontal'))
DataFrame = FilterDF_NpxExploredArea(DataFrame, currentAreaOfInterest)

DataFrame = FilterDF(DataFrame, 'stim_area', ('CA3 from ephys', 'VIS4', 'RSPagl6 from ephys', 'VISrl5'))
[... 288 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 16560,17412p MainScript.ipynb.py | grep -v "savefig" | cut -c1-220
```

```
#DataFrame = FilterDF(DataFrame, 'Stim_Npx', (1))
DataFrame


#TimeWindowResp = (0.075,0.25)
#TimeWindowResp = (0.075,0.100)
#TimeWindowResp = (0.100,0.125)
#TimeWindowResp = (0.125,0.150)
#TimeWindowResp = (0.150,0.175)
#TimeWindowResp = (0.175,0.200)
#TimeWindowResp = (0.200,0.225)
TimeWindowResp = (0.225,0.250)
#TimeWindowResp = (0.250,0.275)
#TimeWindowResp = (0.275,0.300)
#TimeWindowResp = (0.300,0.325)
#TimeWindowResp = (0.325,0.350)
#TimeWindowResp = (0.350,0.375)



[... 797 more lines not kept]
```

**Agent**

Next, the HF/LF clustering and ISI sections.

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n "KMeans\|0.01788\|17.88\|UniDip\|dip(\|diptst\|calinski\|davies" MainScript.ipynb.py | head -40
```

```
53:from unidip import UniDip
2200:def DFLoad_DetectHTBursts(currSessDF,TimeRange = (-1,1), UnitsOfInterest = 'all', MainFolder =  r'E:\AllenInstitute\Data', SpikeType = 'Unit', nBins = 200, Threshold = 0.01788):
2291:    Threshold = 0.01788
3670:Pop_TH_Rs_Threshold = 0.017883
4333:plt.title(dip.diptst(tmp)[1])
4340:plt.title(dip.diptst(tmp)[1])
4347:plt.title(dip.diptst(tmp)[1])
4355:plt.title(dip.diptst(tmp)[1])
4360:np.sum(ISIPerUnit_TH_Rs>0.01788)
4361:np.sum(ISIPerUnit_TH_Rs<0.01788)
4364:dip.diptst?
4810:np.nansum(ISIPerUnit_TH_Rs>0.01788)
6947:    km = sklearn.cluster.KMeans(n_clusters=k)
6965:    kmeans = sklearn.cluster.KMeans(n_clusters=n_clusters,
6977:    ch = sklearn.metrics.calinski_harabasz_score(DataToCluster.reshape(-1,1), labels_clusters)
6978:    db = sklearn.metrics.davies_bouldin_score(DataToCluster.reshape(-1,1), labels_clusters)
6981:                  "calinski_harabasz_score": ch,
6982:                  "davies_bouldin_score": db,
7031:km = sklearn.cluster.KMeans(n_clusters = 2)
7055:#kmeans = sklearn.cluster.KMeans(n_clusters=2).fit(h.reshape(200,1))
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 3455,3700p MainScript.ipynb.py | grep -v savefig | cut -c1-220
```

```
# Rebound ISI Thalamus and Cortex _ Fs VS Rs

# ---- cell 84 [code]
SelectedAreas_MO = areas_of_interest['MO']
SelectedAreas_TH = areas_of_interest['MO-TH']



DataFrame = LoadDF_DataFrame()
#DataFrame = FilterDF(DataFrame, 'EEG_GoodBad', 1)
DataFrame = FilterDF(DataFrame, 'stim_target_area', ('M2','M2-frontal'))
DataFrame = FilterDF(DataFrame, 'stim_depth_label', ('deep','unique'))
DataFrame = FilterDF(DataFrame, 'stim_int_label', ('max','unique')) ###### THIS ///////////
#DataFrame = FilterDF(DataFrame, 'stim_int_label', ('min'))
DataFrame = FilterDF(DataFrame, 'brain_states', 'awake', 'contains')
DataFrame_MO = FilterDF_NpxExploredArea(DataFrame, SelectedAreas_MO)
DataFrame_TH = FilterDF_NpxExploredArea(DataFrame, SelectedAreas_TH)
#DataFrame = FilterDF(DataFrame, 'brain_states', 'ISO', 'contains')

DataFrame_MO, DataFrame_TH, Indexes1, Indexes2 = MatchDF_DifferentNpx(DataFrame_MO,DataFrame_TH)
[... 227 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 3700,3900p MainScript.ipynb.py | grep -v savefig | cut -c1-260
```

```
tmpISIPerUnit_MO_Rs = np.nanmedian(ISI[currIndexes_Rs,:], axis =1)
    tmpISIVariabilityPerTrial_MO_Fs = np.nanstd(ISI[currIndexes_Fs,:], axis =0)
    tmpISIVariabilityPerTrial_MO_Rs = np.nanstd(ISI[currIndexes_Rs,:], axis =0)
    tmpISIVariabilityPerUnit_MO_Fs = np.nanstd(ISI[currIndexes_Fs,:], axis =1)
    tmpISIVariabilityPerUnit_MO_Rs = np.nanstd(ISI[currIndexes_Rs,:], axis =1)
    BurstingRatioPerUnit_MO = np.nanmean(ISI[currIndexes,:]<0.004, axis =1)
    tmpBurstingRatioPerTrial_MO_Fs = np.nanmean(ISI[currIndexes_Fs,:]<0.004, axis =0)
    tmpBurstingRatioPerTrial_MO_Rs = np.nanmean(ISI[currIndexes_Rs,:]<0.004, axis =0)
    tmpBurstingRatioPerUnit_MO_Fs = np.nanmean(ISI[currIndexes_Fs,:]<0.004, axis =1)
    tmpBurstingRatioPerUnit_MO_Rs = np.nanmean(ISI[currIndexes_Rs,:]<0.004, axis =1)
    tmpFirstSpikeVariability_MO = np.nanstd(Latencies[currIndexes,:], axis = 0)
    tmpFirstSpikeVariabilityPerTrial_MO_Fs = np.nanstd(Latencies[currIndexes_Fs,:], axis = 0) 
    tmpFirstSpikeVariabilityPerTrial_MO_Rs = np.nanstd(Latencies[currIndexes_Rs,:], axis = 0) 
    tmpFirstSpikeVariabilityPerUnit_MO_Fs = np.nanstd(Latencies[currIndexes_Fs,:], axis = 1) 
    tmpFirstSpikeVariabilityPerUnit_MO_Rs = np.nanstd(Latencies[currIndexes_Rs,:], axis = 1) 
    tmpFirstSpikeLatencyPerUnit_MO_Fs = AverageLatencies[currIndexes_Fs]
    tmpFirstSpikeLatencyPerUnit_MO_Rs = AverageLatencies[currIndexes_Rs]
    tmpFirstSpikeLatencyPerTrial_MO_Fs = np.nanmedian(Latencies[currIndexes_Fs,:], axis = 0)
    tmpFirstSpikeLatencyPerTrial_MO_Rs = np.nanmedian(Latencies[currIndexes_Rs,:], axis = 0)
    tmpBaselineFrPerTrial_MO_Fs = np.nanmean(AllNSpikes[currIndexes_Fs,:], axis = 0)
[... 182 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n "multipletests\|bonferroni" MainScript.ipynb.py | head -20
```

```
5241:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3,Box4], p_adjust = 'bonferroni')
5349:statsmodels.stats.multitest.multipletests([Stat_Firing_Rest[1],Stat_Firing_Run[1],Stat_Bursting_Rest[1],Stat_Bursting_Run[1]], alpha = 0.05)
5975:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3,Box4], p_adjust = 'bonferroni')
6102:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3,Box4], p_adjust = 'bonferroni')
6137:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3,Box4], p_adjust = 'bonferroni')
6145:statsmodels.stats.multitest.multipletests((RanksumHF[1],RanksumLF[1]), method='bonferroni')
6184:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3,Box4], p_adjust = 'bonferroni')
6192:statsmodels.stats.multitest.multipletests((RanksumHF[1],RanksumLF[1]), method='bonferroni')
6231:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3,Box4], p_adjust = 'bonferroni')
6239:statsmodels.stats.multitest.multipletests((RanksumHF[1],RanksumLF[1]), method='bonferroni')
6267:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3,Box4], p_adjust = 'bonferroni')
6276:statsmodels.stats.multitest.multipletests((RanksumHF[1],RanksumLF[1]), method='bonferroni')
6308:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3,Box4], p_adjust = 'bonferroni')
6610:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3,Box4], p_adjust = 'bonferroni')
6640:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3,Box4], p_adjust = 'bonferroni')
6680:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3,Box4,Box5], p_adjust = 'bonferroni')
6715:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3,Box4], p_adjust = 'bonferroni')
6748:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3,Box4], p_adjust = 'bonferroni')
7788:PostHoc = sp.posthoc_dunn([Box1,Box2,Box3], p_adjust = 'bonferroni')
9034:#a = multitest.multipletests(np.reshape(AllP,[AllP.shape[0]*AllP.shape[1]]), alpha=0.05, method='fdr_bh')
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 6080,6300p MainScript.ipynb.py | grep -v savefig | cut -c1-240
```

```
#Box1 = BaselineFrPerTrial_Pop_Bursting[AllWheelVelocity>0.1]
#Box2 = BaselineFrPerTrial_Pop_Firing[AllWheelVelocity>0.1]
#Box3 = BaselineFrPerTrial_Pop_Bursting[AllWheelVelocity<0.1]
#Box4 = BaselineFrPerTrial_Pop_Firing[AllWheelVelocity<0.1]

#Box1 = LatenciesPerTrial_Pop_Bursting[AllWheelVelocity>0.1]
#Box2 = LatenciesPerTrial_Pop_Firing[AllWheelVelocity>0.1]
#Box3 = LatenciesPerTrial_Pop_Bursting[AllWheelVelocity<0.1]
#Box4 = LatenciesPerTrial_Pop_Firing[AllWheelVelocity<0.1]

#Box1 = LatenciesVariabilityPerTrial_Pop_Bursting[AllWheelVelocity>0.1]
#Box2 = LatenciesVariabilityPerTrial_Pop_Firing[AllWheelVelocity>0.1]
#Box3 = LatenciesVariabilityPerTrial_Pop_Bursting[AllWheelVelocity<0.1]
#Box4 = LatenciesVariabilityPerTrial_Pop_Firing[AllWheelVelocity<0.1]

#Box1 = ISIPerTrial_Pop_Bursting[AllWheelVelocity>0.1]
#Box2 = ISIPerTrial_Pop_Firing[AllWheelVelocity>0.1]
#Box3 = ISIPerTrial_Pop_Bursting[AllWheelVelocity<0.1]
#Box4 = ISIPerTrial_Pop_Firing[AllWheelVelocity<0.1]

[... 199 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n '1366,1453p;1534,1550p;1912,1947p' MainScript.ipynb.py | cut -c1-240
```

```
def DFLoad_UnitsFirstSpike(currSessDF,TimeRange = (0.003,0.5), UnitsOfInterest = 'all' , MainFolder =  r'E:\AllenInstitute\Data', SpikeType = 'Unit', SpikeFirstLast = 'First'):
    
    currSessFolder_Units = MainFolder + '\\' + currSessDF['mouse_name'].values[0] + '\\' + currSessDF['exp_name'].values[0] + '\\' + 'probe' +currSessDF['Npx'].values[0] + '\\' + str(int(currSessDF['sweep_num'].values[0])) + '_' + currSessD
    SortedUnits = np.load(currSessFolder_Units + 'SortedUnits.npy')
    SortedPeakChs = np.load(currSessFolder_Units + 'SortedPeakChs.npy')
    
    if SpikeType== 'Unit':
        currSessFolder = MainFolder + '\\' + currSessDF['mouse_name'].values[0] + '\\' + currSessDF['exp_name'].values[0] + '\\' + 'probe' +currSessDF['Npx'].values[0] + '\\' + str(int(currSessDF['sweep_num'].values[0])) + '_' + currSessDF[
        UnitLabel = 'Unit'
    elif SpikeType == 'Burst':
        currSessFolder = MainFolder + '\\' + currSessDF['mouse_name'].values[0] + '\\' + currSessDF['exp_name'].values[0] + '\\' + 'probe' +currSessDF['Npx'].values[0] + '\\' + str(int(currSessDF['sweep_num'].values[0])) + '_' + currSessDF[
        UnitLabel = 'UnitBursts'
    
    nTrials = 0
    for iUnits in range(0,len(SortedUnits)):
        currUnit = SortedUnits[iUnits]
        SpikeTrialsPath = os.path.join(currSessFolder, UnitLabel + ' '+ str(currUnit)+ '_Trial.npy')
        if os.path.exists(SpikeTrialsPath):
            currUnitEventsTrials = np.load(SpikeTrialsPath)
            if len(currUnitEventsTrials)>0:
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 4300,4370p MainScript.ipynb.py | grep -v savefig | cut -c1-200; echo =====; sed -n 6930,7070p MainScript.ipynb.py | grep -v savefig | cut -c1-200
```

```
currISIBursting3 = currISIBursting2[currISIBursting3Indexes];
currISI2Bursting3 = currISI2Bursting2[currISIBursting3Indexes];
currISI3Bursting3 = currISI3Bursting2[currISIBursting3Indexes];

#np.nanmedian(currISIBursting)
#np.nanmedian(currISI2Bursting)

#np.nanmedian(currISIBursting2)
np.nanmedian(currISI2Bursting2)

#np.nanmedian(currISIBursting3)
#np.nanmedian(currISI2Bursting3)
#np.nanmedian(currISI3Bursting3)

# ---- cell 100 [code]
#np.mean(ISIPerUnit_TH_Rs>ISI2PerUnit_TH_Rs)

Index1 = np.where(ISIPerUnit_TH_Rs<0.017)[0]
Index2 = np.where(ISI2PerUnit_TH_Rs<0.017)[0]
IndexAll = np.intersect1d(Index1,Index2)
[... 188 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n "anova_lm\|f_oneway\|pairwise_tukeyhsd\|tukey_hsd\|AnovaRM" MainScript.ipynb.py MainScript_Opto.ipynb.py | head -20
```

```
MainScript.ipynb.py:35:from statsmodels.stats.anova import AnovaRM
MainScript.ipynb.py:4571:#sm.stats.anova_lm(model, typ=2)
MainScript.ipynb.py:4579:res.tukey_hsd(df=AnovaDF, res_var='Pw', xfac_var='Condition', anova_model='Pw~C(Area)+C(Condition)+C(Area):C(Condition)', ss_typ=3)
MainScript.ipynb.py:4583:res.tukey_hsd(df=AnovaDF, res_var='Pw', xfac_var='Area', anova_model='Pw~C(Area)+C(Condition)+C(Area):C(Condition)', ss_typ=3)
MainScript.ipynb.py:4619:stat.tukey_hsd?
MainScript.ipynb.py:6613:#scipy.stats.f_oneway(Box1,Box2,Box3,Box4)
MainScript.ipynb.py:6644:#scipy.stats.f_oneway(Box1,Box2,Box3,Box4)
MainScript.ipynb.py:6683:#scipy.stats.f_oneway(Box1,Box2,Box3,Box4)
MainScript.ipynb.py:6718:#scipy.stats.f_oneway(Box1,Box2,Box3,Box4)
MainScript.ipynb.py:6751:#scipy.stats.f_oneway(Box1,Box2,Box3,Box4)
MainScript_Opto.ipynb.py:35:from statsmodels.stats.anova import AnovaRM
MainScript_Opto.ipynb.py:3876:fvalue, pvalue = stats.f_oneway(OptoSuppressionEstimOnly, OptoSuppressionOpto1, OptoSuppressionOpto2)
MainScript_Opto.ipynb.py:3879:from statsmodels.stats.multicomp import pairwise_tukeyhsd
MainScript_Opto.ipynb.py:3885:tukey = pairwise_tukeyhsd(endog=df['score'],
MainScript_Opto.ipynb.py:3913:fvalue, pvalue = stats.f_oneway(OptoSuppressionEstimOnly, OptoSuppressionOpto1, OptoSuppressionOpto2)
MainScript_Opto.ipynb.py:3916:from statsmodels.stats.multicomp import pairwise_tukeyhsd
MainScript_Opto.ipynb.py:3922:tukey = pairwise_tukeyhsd(endog=df['score'],
MainScript_Opto.ipynb.py:3952:fvalue, pvalue = stats.f_oneway(OptoSuppressionEstimOnly, OptoSuppressionOpto1, OptoSuppressionOpto2)
MainScript_Opto.ipynb.py:3955:from statsmodels.stats.multicomp import pairwise_tukeyhsd
MainScript_Opto.ipynb.py:3961:tukey = pairwise_tukeyhsd(endog=df['score'],
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n 4440,4600p MainScript.ipynb.py | grep -v savefig | cut -c1-220
```

```
Box2 = np.array(list(set(CtxLatMean_rest)));
Box3 = np.array(list(set(CSDLatMean_rest)));
Box4 = np.array(list(set(LFPLatMean_rest)));
Box5 = np.array(list(set(EEGLatMean_rest)));

#Matrix = np.concatenate((Box1[:,np.newaxis],Box2[:,np.newaxis],Box3[:,np.newaxis]), axis = 1)
Box1 = Box1[np.where(np.logical_not(np.isnan(Box1)))[0]];
Box2 = Box2[np.where(np.logical_not(np.isnan(Box2)))[0]];
Box3 = Box3[np.where(np.logical_not(np.isnan(Box3)))[0]];
Box4 = Box4[np.where(np.logical_not(np.isnan(Box4)))[0]];
Box5 = Box5[np.where(np.logical_not(np.isnan(Box5)))[0]];

fig, ax = plt.subplots(figsize=(6,6))
plt.boxplot((Box1,Box2,Box3,Box4,Box5), showfliers = False)

plt.xticks([1,2,3,4,5],['Thalamus', 'Cortex', 'CSD', 'LFP', 'EEG'])
#plt.plot(Matrix.T)
#plt.ylim((0.100,0.200))

scipy.stats.kruskal(Box1,Box2,Box3,Box4,Box5)
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; grep -n "EEGLatMean_rest = \|ThLatMean_rest = \|LFPLatMean_rest = \|CSDLatMean_rest = \|CtxLatMean_rest = " MainScript.ipynb.py | head; grep -n "AllEEGPeakLat = np.concat\|tmpEEGPeakLat\b\|EEGPeakLat =" MainScript.ipynb.py | head
```

```
3641:EEGLatMean_rest = np.empty(0)
3646:CSDLatMean_rest = np.empty(0)
3647:LFPLatMean_rest = np.empty(0)
3653:ThLatMean_rest = np.empty(0)
3654:CtxLatMean_rest = np.empty(0)
4165:    EEGLatMean_rest = np.concatenate((EEGLatMean_rest,np.array(np.nanmean(tmpEEGPeakLat_rest))[np.newaxis]))
4169:    CSDLatMean_rest = np.concatenate((CSDLatMean_rest,np.array(np.nanmean(tmpCSDPeakLat_rest))[np.newaxis]))
4172:    LFPLatMean_rest = np.concatenate((LFPLatMean_rest,np.array(np.nanmean(tmpLFPPeakLat_rest))[np.newaxis]))
4179:    ThLatMean_rest = np.concatenate((ThLatMean_rest,np.array(np.nanmean(tmpFirstSpikeLatencyPerTrial_TH_Rs[np.where(WheelVelocity<0.1)[0]]))[np.newaxis]))
4180:    CtxLatMean_rest = np.concatenate((CtxLatMean_rest,np.array(np.nanmean(tmpFirstSpikeLatencyPerTrial_MO_Rs[np.where(WheelVelocity<0.1)[0]]))[np.newaxis]))
3632:AllEEGPeakLat = np.empty(0)
4053:        tmpEEGPeakAmp, tmpEEGPeakLat = FindResponsePeaks_SingleTrial(SplittedEEG, TsEEG, BaselineTimeRange = 'all',ResponseTimeRange = (0.075,0.25), StdThreshold = 3, numberOfPeaks = 1)
4058:        #if np.logical_not(np.isnan(tmpEEGPeakLat)):
4059:        #    NO, tmpEEGPeakOnset = FindResponsePeaks(moving_average_2dim(EvokedEEGDiff,25), moving_average(TsEEG[1::],25), BaselineTimeRange = 'all',ResponseTimeRange = (0.150,tmpEEGPeakLat), StdThreshold = 0, numberOfPeaks = 1)
4065:        tmpEEGPeakLat = np.zeros(tmpISIPerTrial_Pop_Bursting.shape[0])
4074:        tmpEEGPeakLat[:] = np.nan
4154:    AllEEGPeakLat = np.concatenate((AllEEGPeakLat,tmpEEGPeakLat))
4164:    EEGLatMean = np.concatenate((EEGLatMean,np.array(np.nanmean(tmpEEGPeakLat))[np.newaxis]))
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR; sed -n '1264,1294p;1503,1517p' MainScript.ipynb.py; sed -n 4040,4100p MainScript.ipynb.py | cut -c1-220
```

```
def FindResponsePeaks(EvokedEEG, Ts, BaselineTimeRange = 'all',ResponseTimeRange = 'all', StdThreshold = 3, numberOfPeaks = 1):
    if ResponseTimeRange == 'all':
        ResponseTimeRange = (0,max(Ts))
    if BaselineTimeRange == 'all':
        BaselineTimeRange = (min(Ts),0)
    currTimeIndexesResponse = np.where(np.logical_and(Ts>ResponseTimeRange[0], Ts<ResponseTimeRange[1]))[0].astype(int)
    currTimeIndexesBaseline = np.where(np.logical_and(Ts>BaselineTimeRange[0], Ts<BaselineTimeRange[1]))[0].astype(int)
    GMFP = computeGMFP(EvokedEEG)
    ProminenceThreshold = np.nanmean(GMFP[currTimeIndexesBaseline]) + np.nanstd(GMFP[currTimeIndexesBaseline])*StdThreshold
    if numberOfPeaks== 'all':
        tmpPeaks = scipy.signal.find_peaks(GMFP[currTimeIndexesResponse] ,prominence = ProminenceThreshold)
        PeaksIndices = tmpPeaks[0].astype(int)
        PeaksFeatures = tmpPeaks[1]
    else:
        tmpPeaks = scipy.signal.find_peaks(GMFP[currTimeIndexesResponse] ,prominence = ProminenceThreshold)
        PeaksIndices = tmpPeaks[0].astype(int)
        #tmpPeaksOnset = tmpPeaks[1]['left_bases']
        #PeaksIndices, PeaksProperties = scipy.signal.find_peaks(GMFP[currTimeIndexesResponse] ,prominence = ProminenceThreshold)[0].astype(int)
        SortedIndices = PeaksIndices[np.argsort(-GMFP[currTimeIndexesResponse[PeaksIndices]]).astype(int)]
        #SortedOnset = tmpPeaksOnset[np.argsort(-GMFP[currTimeIndexesResponse[PeaksIndices]]).astype(int)]
[... 88 more lines not kept]
```

**Agent**

I've finished the code review. Checking the claims schema before writing.

**Agent calls Bash**

```bash
cat schemas/claims.schema.json | head -200
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
[... 180 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,400p schemas/claims.schema.json
```

```
"then": {
              "required": [
                "where"
              ]
            }
          }
        ]
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
[... 134 more lines not kept]
```

**Agent calls Bash**

```bash
grep -l "relation: reuses" papers/datasets/*.yaml | head -5; grep -n -B2 -A2 "where:" claims/*.yaml | head -30
```

```
papers/datasets/alasfour-2024.yaml
papers/datasets/burman-2023.yaml
papers/datasets/cambrainha-2025.yaml
papers/datasets/clark-2026.yaml
papers/datasets/du-2026.yaml
claims/andrews-2024.yaml-173-    50% of the granule cell population ( Extended data Fig. 3 )
claims/andrews-2024.yaml-174-  data: elsewhere
claims/andrews-2024.yaml:175:  where: GitHub braingeneers/AndrewsGengVoitiukEtAl_SourceCode at commit 6865bf68cc3c8ea36a9b4f853b9248288fa1e52b,
claims/andrews-2024.yaml-176-    Simulation directory (model code, rerun)
claims/andrews-2024.yaml-177-  criterion: Run Simulation/simulation.py as published (NEST 3.4, NESTML, 1000 granule and 12
--
claims/azcorra-2023.yaml-728-    mean of 1,683 features.
claims/azcorra-2023.yaml-729-  data: elsewhere
claims/azcorra-2023.yaml:730:  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
claims/azcorra-2023.yaml-731-  expected:
claims/azcorra-2023.yaml-732-  - quantity: Nuclei after quality control
--
claims/azcorra-2023.yaml-749-    Aldh1a1-expressing neurons.
claims/azcorra-2023.yaml-750-  data: elsewhere
claims/azcorra-2023.yaml:751:  where: GEO GSE222558 (samples GSM6926026 and GSM6926027)
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "not public\|not available\|data_missing\|source data file" claims/*.yaml | head -15
```

```
claims/ashworth-2025.yaml:1229:  - Open, the code-derived details (notebook values, function names, priors on log k) were not checked against the repository in this check; the code was not available here.
claims/bouchard-2013.yaml:738:  - Header, major articulator labels. It said the labels come from Fig. 4c, a main figure the file says was not available, and its reading (b) put /h/ in the dorsal set, which no source supports. Now read from the Supplementary Figure 12 place features, with /w/ and /j/ also named as unplaced, and /h/ left out in both readings.
claims/brinke-2017.yaml:1881:    blocked data_missing) unless the author finds those data public, then elsewhere.
claims/calvigioni-2023.yaml:11:# PDF pages (pages 8 to 11), as they are images. The source data files and the supplementary videos
claims/calvigioni-2023.yaml:12:# were not available and are not needed by any claim below.
claims/chartrand-2023.yaml:514:    the claim is methods_underspecified with both shown. The paper names no deposit for the mouse TEa electrophysiology; if it is not public
claims/chartrand-2023.yaml:515:    the claim is blocked data_missing.
claims/chartrand-2023.yaml:792:    every combination of these readings, r is within tolerance and p < 0.05. The ZINB curve fits (zinb_human.h5) are not public; they are refitted
claims/chartrand-2023.yaml:883:    dandiset does not hold them the claim is blocked data_missing.
claims/chen-2026.yaml:8:# they were blocked with data_missing. Under pilot-7 a claim whose data the paper deposited in
claims/chen-2026.yaml:10:# data_missing now means public nowhere. These eight claims now carry `data`, `where` and a
claims/chen-2026.yaml:36:# author had also read the layout of the paper's source data file (Zenodo 10.5281/zenodo.19930567)
claims/chen-2026.yaml:77:    images with metadata files in this study are available in source data file via the open-access
claims/clark-2024.yaml:794:    which was not available. Reproduced when the non-beaconed odds rat
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 940,2195p 10.1038-s41467-025-58717-2.txt | grep -n -i "sheet\|^#\|Fig" | head -60
```

```
23:##### Supplement: 41467_2025_58717_MOESM4_ESM.xlsx (from the publisher's site)
25:### Sheet Figure 1 A
26:Figure 1A,,,,,,,,,,,,,,
43:### Sheet Figure 1 B
44:Figure 1B,,,,,,,,,,,,,,
54:### Sheet Figure 1 C
55:Figure 1C,,,,,,,,,,,,,,
86:### Sheet Figure 1 D
87:Figure 1D,,,,,,,,,,,,,,
104:### Sheet Figure 1 E
105:Figure 1E,,,,,,,,,,,
122:### Sheet Figure 2 B
123:Figure 2B,,,,,,,,,,,,,,,,
147:### Sheet Figure 2 G
148:Figure 2G,,,,,,,,,
306:### Sheet Figure 3 A
307:Figure 3A,,,,,,,,,,,,,,
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 960,1100p 10.1038-s41467-025-58717-2.txt | cut -c1-200
```

```
##### Supplement: 41467_2025_58717_MOESM4_ESM.xlsx (from the publisher's site)

### Sheet Figure 1 A
Figure 1A,,,,,,,,,,,,,,
,Panel A,,,,,,,,,,,,,
,TMS-EEG,,,,,,,,,,,,,
,Rest (μV),Active (μV),,,,,,,,,,,,
,1.09576465216692,0.939183222038337,,,,,,,,,,,,
,0.944265943674968,0.826887444610503,,,,,,,,,,,,
,1.34353380321158,1.0061829487271,,,,,,,,,,,,
,2.73763814692387,1.12504294344285,,,,,,,,,,,,
,0.96225259157187,0.773482337685569,,,,,,,,,,,,
,1.47967200089188,0.803642798844195,,,,,,,,,,,,
,0.653888768573335,0.376671120756988,,,,,,,,,,,,
,0.907062777253186,0.638473313732555,,,,,,,,,,,,
,1.5789632230623,0.479003878434742,,,,,,,,,,,,
,2.03181374700987,0.823672556482855,,,,,,,,,,,,
,1.03445138437981,0.5440926675806,,,,,,,,,,,,
,1.78454769000376,0.920483748823453,,,,,,,,,,,,

[... 120 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 1240,1300p 10.1038-s41467-025-58717-2.txt | cut -c1-200; tail -5 10.1038-s41467-025-58717-2.txt | cut -c1-200
```

```
,,,,0.253851159140594,0.230262273274547,0.26440034992629,,,
,,,,0.165844568074021,0.216644540264724,0.25126133604499,,,
,,,,0.175059050466188,0.21164692397383,0.233352428290345,,,
,,,,0.180536666307943,0.199586967868754,0.234527591538608,,,

### Sheet Figure 3 A
Figure 3A,,,,,,,,,,,,,,
,Panel  A,,,,,,,,,,,,,
,Rest (Hz),Active (Hz),,,,,,,,,,,,
,15.3125,20,,,,,,,,,,,,
,16.5625,21.875,,,,,,,,,,,,
,17.03125,18.90625,,,,,,,,,,,,
,14.0625,15.3125,,,,,,,,,,,,
,15.3125,20.15625,,,,,,,,,,,,
,9.6875,21.40625,,,,,,,,,,,,
,12.96875,20.78125,,,,,,,,,,,,
,16.875,18.4375,,,,,,,,,,,,
,13.4375,20,,,,,,,,,,,,
,14.6875,17.1875,,,,,,,,,,,,
,13.28125,17.96875,,,,,,,,,,,,
[... 46 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
import openpyxl
wb=openpyxl.load_workbook('10.1038-s41467-025-58717-2.supp-41467_2025_58717_MOESM4_ESM.xlsx',read_only=True,data_only=True)
for ws in wb.worksheets:
    rows=list(ws.iter_rows(values_only=True))
    hdr=[r for r in rows[:5]]
    print(ws.title, len(rows), [ [c for c in r if c is not None] for r in rows[1:4]])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import openpyxl
ModuleNotFoundError: No module named 'openpyxl'
```

**Agent calls Bash**

```bash
cd $TMPDIR; mkdir -p x && cd x && unzip -o -q paper/10.1038-s41467-025-58717-2.supp-41467_2025_58717_MOESM4_ESM.xlsx && grep -o '<sheet [^>]*name="[^"]*"' xl/workbook.xml | sed 's/.*name="//;s/"//'; for f in xl/worksheets/sheet*.xml; do echo "$f $(grep -o '<row ' $f | wc -l)"; done
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/x; grep -o '<sheet [^>]*>' xl/workbook.xml | sed -n '6,11p'; cat xl/_rels/workbook.xml.rels | tr '>' '>\n' | grep -o 'Id="rId[0-9]*"[^>]*Target="[^"]*"' | head -12; python3 - <<'EOF'
import re
ss=open('xl/sharedStrings.xml').read()
strs=[re.sub('<[^>]+>','',m) for m in re.findall(r'<si>(.*?)</si>',ss,flags=re.S)]
for n in [8,9]:
    x=open(f'xl/worksheets/sheet{n}.xml').read()
    rows=re.findall(r'<row [^>]*>(.*?)</row>',x,flags=re.S)
    def cells(r):
        out=[]
        for c in re.findall(r'<c ([^>]*?)(?:/>|>(.*?)</c>)',r,flags=re.S):
            attrs,body=c
            v=re.search(r'<v>(.*?)</v>',body or '')
            if not v: continue
            v=v.group(1)
            if 't="s"' in attrs: v=strs[int(v)]
            out.append(v)
        return out
    print(n,[cells(r) for r in rows[:6]], cells(rows[-1]), len(rows))
EOF
```

```
<sheet name="Figure 2 B" sheetId="2" r:id="rId6"/>
<sheet name="Figure 2 G" sheetId="9" r:id="rId7"/>
<sheet name="Figure 3 A" sheetId="3" r:id="rId8"/>
<sheet name="Figure 3 E" sheetId="10" r:id="rId9"/>
<sheet name="Figure 4 E" sheetId="4" r:id="rId10"/>
<sheet name="Figure 4 F" sheetId="11" r:id="rId11"/>
Id="rId13" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet13.xml"
Id="rId18" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet18.xml"
Id="rId26" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet26.xml"
Id="rId39" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet39.xml"
Id="rId21" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet21.xml"
Id="rId34" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet34.xml"
Id="rId42" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet42.xml"
Id="rId47" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/sharedStrings" Target="sharedStrings.xml"
Id="rId7" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet7.xml"
Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet2.xml"
Id="rId16" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet16.xml"
Id="rId29" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet29.xml"
8 [['Figure 3A'], ['Panel  A'], [], [], ['Rest (Hz)', 'Active (Hz)'], ['15.3125', '20']] ['15'] 1445
9 [['Figure 3E'], ['Panel E'], ['HF', 'LF'], ['Baseline', 
[... 1 more lines not kept]
```

**Agent**

I have what I need from the code. Computing a few summary values from the paper's own Source Data sheets (paper material, not the dataset) for a link claim.

**Agent calls Bash**

```bash
cd paper; python3 - <<'EOF'
import re,statistics as st
txt=open('10.1038-s41467-025-58717-2.txt').read()
def sheet(name):
    m=re.search(r'### Sheet '+re.escape(name)+r'\n(.*?)(?=\n### Sheet|\n\[\.\.\.)',txt,flags=re.S)
    rows=[r.split(',') for r in m.group(1).splitlines()]
    return rows
for name,ncol in [('Figure 1 C',2),('Figure 1 D',2),('Figure 1 E',2),('Figure 2 B',5)]:
    rows=sheet(name)
    cols=[[] for _ in range(ncol)]
    for r in rows:
        for i in range(ncol):
            try: cols[i].append(float(r[i+1]))
            except: pass
    print(name,[ (len(c), round(st.median(c),4), round(st.mean(c),4)) for c in cols])
EOF
```

```
Figure 1 C [(26, 97.8631, 102.9682), (26, 67.7298, 74.0387)]
Figure 1 D [(12, 2.529, 2.6222), (12, 1.3434, 1.5706)]
Figure 1 E [(12, 0.8545, 0.8749), (12, 0.5478, 0.5639)]
Figure 2 B [(20, 0.1588, 0.1538), (15, 0.1734, 0.1707), (12, 0.1732, 0.1738), (13, 0.1722, 0.1701), (13, 0.1703, 0.1713)]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -o human.zip https://ndownloader.figshare.com/files/45634542 && unzip -o -q human.zip -d human && find human -type f | head; curl -sL https://ndownloader.figshare.com/files/45634605
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd "$TMPDIR/human/DataAnalysisHuman"; grep -n -i "signrank\|wilcox\|Fc1\|FC1\|150\|0.15\|plf\|abs(" "TMS EEG/RestMov_ExtractFeatures.m" | head -30; wc -l "TMS EEG/RestMov_ExtractFeatures.m" "ES SEEG/Extract result.m"
```

```
6:MainFolderPLF='D:\RestMov\TMS-EEG\PLF';
35:    load(fullfile(MainFolderPLF,currSessSubj,[currSessStimArea '_' currSessStimHemisphere],[currSessConditionTask '_' currSessConditionSide '-' currSessPart '_' currSessConditionEyes '.mat']))
39:    PLF=squeeze(DataPLF(1,:,:));
42:    AbsEvoked=abs(Evoked);
46:    PLFGlobal = mean(PLF,2);
47:    PLFLocal = mean(PLF(:,SelectedChs),2);
50:    IndexesMiddle=find((Ts>50).*(Ts<150));
51:    IndexesLate=find((Ts>150).*(Ts<250));
57:    MainTable.PLF{counterSession}=PLFGlobal;
58:    MainTable.PLF_ROI{counterSession}=PLFLocal;
64:    MainTable.LMFP_ROI_50_150(counterSession)=mean(LMFP(IndexesMiddle));
65:    MainTable.LMFP_ROI_150_250(counterSession)=mean(LMFP(IndexesLate));
66:    MainTable.PLF_0_50(counterSession)=mean(PLFGlobal(IndexesEarly));
67:    MainTable.PLF_ROI_0_50(counterSession)=mean(PLFLocal(IndexesEarly));
68:    MainTable.PLF_50_150(counterSession)=mean(PLFGlobal(IndexesMiddle));
69:    MainTable.PLF_ROI_50_150(counterSession)=mean(PLFLocal(IndexesMiddle));
70:    MainTable.PLF_150_250(counterSession)=mean(PLFGlobal(IndexesLate));
71:    MainTable.PLF_ROI_150_250(counterSession)=mean(PLFLocal(IndexesLate));
110:LMFPGrandAverage = zeros(size(UniqueSiteID,1),size(ColorCodeByCond_Cond,2),1501);
112:PLFROI_GrandAverage = zeros(size(UniqueSiteID,1),size(ColorCodeByCond_Cond,2),1501);
[... 14 more lines not kept]
```

**Agent**

Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/russo-2025.yaml",
 "content": "# Claims for Russo, Claar, Furregoni et al. (2025), Nat Commun 16:3627, \"Thalamic feedback shapes\n# brain responses evoked by cortical stimulation in mice and humans\", tested on dandiset 000458\n# (reused; the paper's Data availability names version 0.230317.0039).\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-21,\n# protocol pilot-18 as stated in docs/protocol.md. The writer did not look at the dandiset's data or\n# files; only its title, as the paper cites it, was used to know what it holds.\n#\n# Text read: the version of record (open access, CC BY-NC-ND), full text from PubMed Central\n# (main text, Methods, figure legends, Data and Code availability), with the supplement\n# 41467_2025_58717_MOESM1_ESM.pdf (Figures S1 to S14 with legends, Table S1) as text, and the Source\n# Data file 41467_2025_58717_MOESM4_ESM.xlsx (sheets for Figures 1A to 1E, 2B, 2G, 3A, 3E, 4E, 4F\n# and most supplementary panels). No PDF page was opened; no figure was read as an image, so\n# claims shown only in a figure rest on its legend and the Results sentence citing it.\n#\n# Code read. (1) Mouse analysis, figshare doi:10.6084/m9.figshare.28047749 version 1\n# (DataAnalysesMouse_v1.zip): a copy of AllenInstitute/tbd_eeg at commit ef9aa65 with the paper's\n# notebooks under tbd_eeg/My_scripts. Its Notes.txt says MainScript.ipynb runs the mouse analyses of\n# Figures 1 and 2 and the supplement and MainScript_Opto.ipynb the optogenetic analyses (it names\n# them Figure 3 and Figure S8, an older numbering; in the paper the optogenetic results are Figure 2\n# and Figure S8). Cited below as \"MainScript\", by its markdown section names. Cells read: \"EEG\n# Rest-Run Analysis\", \"CSD/LFP Rest-Run Analysis\", \"Units Rest-Run Analysis\", \"Rebound ISI Thalamus\n# and Cortex _ Fs VS Rs\" (latency, ISI, ROV, baseline rate and the HF and LF split), the k-means and\n# dip-test cells, the two-way ANOVA of latencies, the helper functions (IdentifyResponsiveUnits,\n# DFLoad_UnitsFirstSpike, DFLoad_NSpikesWindow, FindResponsePeaks), and\n# CreateExportedData/CreateWheelVelocityPerTrial.ipynb. The notebooks read precomputed files from a\n# lab drive and a lab spreadsheet (TableAllData.xlsx, with per-session good or bad flags and bad\n# channels and trials) that are not in the deposit; the selections those files encode are open\n# where noted. (2) Human analysis, figshare doi:10.6084/m9.figshare.25595829 v1\n# (RestMov_ExtractFeatures.m, signrank tests on per-subject ROI values) and\n# doi:10.6084/m9.figshare.25595871 v1 (StatRestMov_SPES.R: contacts 5 to 30 mm from the stimulated\n# site with response above 6 SD, log amplitude and log PLF, lmer Value ~ Condition + (1 | Subj)).\n# (3) Not read: the model (github.com/bazhlab-ucsd/sleep-stage-transition, branch stim) and the\n# simulated-data analysis (doi:10.6084/m9.figshare.25773501.v1); the simulation claims are data\n# elsewhere and name them.\n#\n# Where the Methods and the code disagree, the Methods are followed and the code's choice is named\n# as a variant: (a) the mouse EEG rectified amplitude (Methods, absolute value of the averaged EP;\n# the code's EEG cell averages the absolute single-trial signal after z-scoring each trial to its\n# baseline); (b) the rest against active unit tests (Methods, Wilcoxon signed rank; the code uses\n# rank-sum tests); (c) the window of the evoked ISI and response frequency (Methods, 150 to 250 ms;\n# the code takes the first spike and its ISI in 75 to 250 ms).\n#\n# Data the paper used.\n# - Mice (dandiset 000458; the paper's own Methods summarise Claar et al. 2023): C57BL/6J wild-type\n#   mice (n = 21, male and female, 9 to 28 weeks), awake, head-fixed on a running wheel in darkness;\n#   30-electrode skull EEG array, up to three Neuropixels 1.0 probes (MOs, SS, VIS and thalamus;\n#   one always in sensorimotor thalamus, SM-TH, the nuclei AV, CL, MD, PO, VAL, VPL, VPM and VM),\n#   and a bipolar stimulating electrode in deep MOs (layer 5/6). Up to 120 biphasic,\n#   cathodic-first pulses (200 us per phase, 3.5 to 4.5 s jittered interval) at each of three\n#   intensities, high 66.15 +- 12.11 uA, intermediate 47.35 +- 13.30 uA and low 30.59 +- 15.80 uA.\n#   Control sessions stimulated posterior areas (visual and retrosplenial cortex, hippocampus;\n#   12 sessions from 6 mice). Trials are rest when mean wheel speed from -0.5 to +0.5 s around the\n#   pulse is below 0.1 cm/s and active when above. Measured variables: EEG, MOs LFP and CSD, sorted\n#   units (Kilosort 2.0) classed by spike duration (cortex RS > 400 us, FS <= 400 us; thalamus relay\n#   > 450 us, TRN < 350 us), wheel speed.\n# - Optogenetics: VGAT-ChR2-YFP/wt mice (n = 4), fiber over TRN (or over MOs, Figure S8), 50 ms of\n#   5 mW blue light at 75 or 125 ms after the pulse. The paper deposited the processed data in\n#   figshare (\"Data Mouse Opto\", article 28440311 version 1); those claims are data elsewhere.\n# - Humans: TMS-EEG in 12 healthy volunteers (left premotor TMS at rest, active squeezing and\n#   passive movement of the right hand; controls with cycling, posterior TMS and median nerve\n#   stimulation), and single-pulse electrical stimulation with intracerebral EEG in 5 epilepsy\n#   patients. The raw human data are not public; the paper gives per-subject processed values in its\n#   Source Data file, so those claims are data elsewhere with the Source Data file as their place.\n# - Simulation: a thalamo-cortical Hodgkin-Huxley network (500 PY, 100 IN, 100 TC, 100 TRN), 15 rest\n#   and 15 active trials; data elsewhere (the model and its analysis code).\nschema_version: 2\npaper: doi:10.1038/s41467-025-58717-2\nclaims:\n- id: source-data-link\n  kind: link\n  statement: The dandiset holds the mouse sessions behind the paper's Figure 1C and Figure 2B, so\n    that values computed from it agree with the per-session and per-subject values in the paper's\n    Source Data file.\n  source: Source Data file, sheets Figure 1 C and Figure 2 B; Figure 1C and Figure 2B legends\n  quote: EEG rectified amplitude evoked during rest and active state, calculated over all EEG\n    contacts for all subjects (26 sessions, 15 subjects)\n  data: dataset\n  criterion: The Source Data sheet Figure 1 C lists 26 rest and active pairs of late (150 to 250\n    ms) EEG rectified amplitude in uV, with medians 97.9 (rest) and 67.7 (active); the sheet Figure\n    2 B lists per-subject late latencies with means 153.8 ms (SM-TH units, 20 subjects), 170.7 ms\n    (MOs units, 15), 173.8 ms (CSD peak, 12), 170.1 ms (LFP peak, 13) and 171.3 ms (EEG peak, 13).\n    No identifier links Source Data rows to dandiset sessions, so the distributions are compared.\n    Computed with the method of fig1c-eeg-late-rest-larger and fig2b-thalamus-leads, the link\n    holds (reproduced) when the session count is within 26 +- 3, both Figure 1C medians are within\n    10% of the Source Data medians, and at least four of the five Figure 2B means are within 10 ms\n    of the Source Data means; partially reproduced when either the Figure 1C or the Figure 2B part\n    holds; not reproduced otherwise.\n  depends_on:\n  - fig1c-eeg-late-rest-larger\n  - fig2b-thalamus-leads\n- id: fig1a-tms-late-rest-active\n  statement: In 12 healthy subjects, the late (150 to 250 ms) TMS-evoked EEG response over premotor\n    channels has a larger rectified amplitude and phase locking at rest than during active hand\n    squeezing (amplitude 1.37 +- 0.59 against 0.77 +- 0.22 uV; PLF 0.21 +- 0.07 against 0.15 +-\n    0.05).\n  source: Results, Multiscale late EP responses elicited by cortical stimulation are modulated by\n    behavioral state in humans and mice, paragraph 2; Figure 1A; Figure S1A\n  quote: \"Compared to rest, both the rectified amplitude of the late response over premotor areas\n    (Fc1, Fcz, Fc2, C1, Cz, C2), and its associated phase locking factor (PLF 37 , see methods for\n    details on this measurement) were significantly reduced during the active condition (amplitude\n    at rest: 1.37 ± 0.59 μV versus during active condition\"\n  statistics:\n  - about: late rectified amplitude, rest against active\n    test: two-tailed Wilcoxon signed rank test\n    p: 0.002\n    n: 12 subjects\n  - about: late PLF, rest against active\n    test: Wilcoxon signed rank test\n    p: 0.002\n    n: 12 subjects\n  data: elsewhere\n  where: The paper's Source Data file 41467_2025_58717_MOESM4_ESM.xlsx, sheets Figure 1 A and Figure\n    S1A (per-subject values); the raw TMS-EEG recordings are not public.\n  expected:\n  - quantity: late rectified amplitude at rest\n    value: 1.37\n    tolerance: 0.59\n    unit: uV\n  - quantity: late rectified amplitude, active\n    value: 0.77\n    tolerance: 0.22\n    unit: uV\n  - quantity: late PLF at rest\n    value: 0.21\n    tolerance: 0.07\n  - quantity: late PLF, active\n    value: 0.15\n    tolerance: 0.05\n  criterion: Tolerances are the paper's reported SDs. Only the per-subject values of the Source\n    Data file are public. Reproduced when the means of its 12 rest and active values are within\n    tolerance and a two-tailed Wilcoxon signed-rank test (Methods, EPs statistical analysis) on the\n    pairs gives p < 0.05 with rest larger, for amplitude and for PLF.\n- id: fig1b-ieeg-late-rest-active\n  statement: In 5 epilepsy patients, the late (150 to 250 ms) iEEG response to single-pulse\n    electrical stimulation of premotor cortex is smaller in rectified amplitude and PLF during\n    active hand squeezing than at rest (z-scored amplitude 5.95 +- 5.79 against 4.30 +- 4.18; PLF\n    0.55 +- 0.27 against 0.49 +- 0.27).\n  source: Results, Multiscale late EP responses ..., paragraph 3; Figure 1B; Figure S1A\n  quote: \"The late responses evoked in nearby iEEG contacts (within 3 cm from the stimulated site)\n    showed a significant reduction of the evoked amplitude (Fig. 1B , z-scored amplitude at rest:\n    5.95 ± 5.79 and during active state: 4.30 ± 4.18; p < 0.05) and PLF during active state\"\n  statistics:\n  - about: late rectified amplitude, rest against active\n    test: Linear Mixed Effect Model\n    p: 0.015\n    n: 105 contacts from 5 subjects\n  - about: late PLF, rest against active\n    test: mixed-effect model\n    p: 0.033\n    n: 5 subjects\n  data: elsewhere\n  where: The paper's Source Data file 41467_2025_58717_MOESM4_ESM.xlsx, sheets Figure 1 B and Figure\n    S1A (per-subject values); the raw iEEG recordings are not public.\n  expected:\n  - quantity: late z-scored amplitude at rest\n    value: 5.95\n    tolerance: 5.79\n  - quantity: late z-scored amplitude, active\n    value: 4.3\n    tolerance: 4.18\n  - quantity: late PLF at rest\n    value: 0.55\n    tolerance: 0.27\n  - quantity: late PLF, active\n    value: 0.49\n    tolerance: 0.27\n  criterion: The paper's test (Methods; StatRestMov_SPES.R) is a mixed model on contacts, log value\n    ~ Condition + (1 | Subj), which needs per-contact values that are not public. With the five\n    per-subject values of the Source Data file, reproduced when active is lower than rest in at\n    least four of five subjects for amplitude and for PLF; the mixed model is not run and this is\n    recorded as a deviation.\n- id: figs2-tms-controls\n  statement: The TMS late-component modulation is also seen with passive hand movement and with\n    leg cycling, is absent for posterior TMS, is absent for median nerve somatosensory evoked\n    potentials, and does not differ between hand closing and opening.\n  source: Results, Multiscale late EP responses ..., paragraph 2; Figure S2A, C, D, E, G\n  quote: We conclude that the amplitude of the TMS-evoked EP in the 150–250 ms window is reduced\n    during both active and passive movement of the contralateral hand and the legs, an effect that\n    is network-specific, given the lack of modulation when TMS was delivered to posterior areas,\n    and not related to somatosensory stimulation.\n  statistics:\n  - about: late amplitude, rest against passive movement\n    test: Wilcoxon signed rank test\n    p: 0.01\n    p_relation: \"<\"\n  - about: late amplitude, rest against cycling\n    test: Wilcoxon signed rank test\n    p: 0.016\n    n: 12 subjects\n  - about: late amplitude, posterior TMS, rest against active\n    test: Wilcoxon signed rank test\n    p: 0.31\n    n: 12 subjects\n  - about: late amplitude, SSEP, rest against active\n    test: Wilcoxon signed rank test\n    p: 0.96\n  - about: late amplitude, hand contraction against relaxation\n    test: Wilcoxon signed rank test\n    p: 0.57\n    n: 12 subjects\n  data: elsewhere\n  where: The paper's Source Data file 41467_2025_58717_MOESM4_ESM.xlsx, sheets Figure S2A, S2C, S2D,\n    S2E and S2G (per-subject values); the raw recordings are not public.\n  criterion: On the per-subject Source Data values, two-sided Wilcoxon signed-rank tests as in\n    Figure S2. Reproduced when rest against passive and rest against cycling give p < 0.05 with\n    rest larger, and posterior TMS (rest against active and against passive), SSEP (both) and\n    contraction against relaxation all give p >= 0.05.\n- id: figs2a-tms-early-component\n  statement: The early (3 to 50 ms) TMS-evoked component is reduced in amplitude during active\n    movement but not in phase locking (2.24 +- 0.45 against 1.88 +- 0.32 uV; PLF 0.43 in both), and\n    its reduction is not correlated with that of the late component.\n  source: Results, Multiscale late EP responses ..., paragraph 2; Figure S2A, S2B\n  quote: \"In the premotor TMS, the early component of the EP (3–50 ms from stimulus onset) showed a\n    reduction in amplitude, but not in phase locking (amplitude at rest 2.24 ± 0.45 μV versus 1.88\n    ± 0.32 μV during active state\"\n  statistics:\n  - about: early amplitude, rest against active\n    test: Wilcoxon signed rank test\n    p: 0.01\n    p_relation: \"<\"\n  - about: early PLF, rest against active\n    test: Wilcoxon signed rank test\n    p: 0.97\n  - about: decrease of early against late amplitude\n    test: Spearman's correlation\n    statistic: r = 0.46\n    p: 0.13\n    n: 12 subjects\n  data: elsewhere\n  where: The paper's Source Data file 41467_2025_58717_MOESM4_ESM.xlsx, sheet Figure S2A\n    (per-subject values); the raw recordings are not public.\n  expected:\n  - quantity: early amplitude at rest\n    value: 2.24\n    tolerance: 0.45\n    unit: uV\n  - quantity: early amplitude, active\n    value: 1.88\n    tolerance: 0.32\n    unit: uV\n  criterion: Reproduced when the Source Data means are within tolerance (the paper's SDs), the\n    early amplitude signed-rank test gives p < 0.05 with rest larger and the early PLF test gives p\n    >= 0.05. The text names the correlation Spearman's and the Figure S2B legend Pearson's; both\n    are run and the absence of correlation (p >= 0.05) is judged on each.\n- id: figs3b-ieeg-early-no-modulation\n  statement: The early (3 to 50 ms) iEEG response to electrical stimulation in humans is not\n    modulated by state, in monopolar or bipolar derivation.\n  source: Results, Multiscale late EP responses ..., paragraph 3; Figure S3B\n  quote: The early component did not show any significant modulation (Fig. S3B ).\n  statistics:\n  - about: bipolar early amplitude\n    test: Mixed effect model\n    p: 0.99\n  - about: bipolar early PLF\n    test: Mixed effect model\n    p: 0.88\n  - about: monopolar early amplitude\n    test: Mixed effect model\n    p: 0.91\n  - about: monopolar early PLF\n    test: Mixed effect model\n    p: 0.93\n  data: elsewhere\n  where: The paper's Source Data file 41467_2025_58717_MOESM4_ESM.xlsx, sheet Figure S3B; the raw\n    iEEG recordings are not public.\n  criterion: A claim of absence; the paper's test is a mixed model on contacts that the public data\n    cannot rerun. On the Source Data values, two-sided Wilcoxon signed-rank tests of rest against\n    active; reproduced when none of the four gives p < 0.05. Recorded as a deviation from the\n    paper's test.\n- id: fig5a-human-mouse-similar\n  statement: Evoked responses to cortical stimulation are remarkably similar between humans and\n    mice, both for scalp EEG (TMS in humans, electrical stimulation in mice) and for intracranial\n    recordings (iEEG and LFP).\n  source: Figure 5A; Discussion, paragraph 1\n  quote: Evoked responses elicited by cortical stimulation (invasive and non-invasive) are\n    remarkably similar between human and mouse.\n  criterion: The paper shows normalized rectified grand averages and reports no measure. The human\n    grand averages are not public and the Source Data file has no Figure 5 sheet, so the claim\n    cannot be tested unless the author finds them; the mouse traces alone are described.\n- id: fig1c-eeg-late-rest-larger\n  statement: In mice, the late (150 to 250 ms) EEG response to deep MOs electrical stimulation has a\n    larger rectified amplitude at rest than during running.\n  source: Figure 1C; Results, Multiscale late EP responses ..., paragraph 5\n  quote: Averaged EEG rectified amplitude over the late response window (150–250 ms, shaded gray) at\n    rest and active state for all EEG electrodes across subjects (two-tailed Wilcoxon signed rank\n    test p = 0.000579).\n  statistics:\n  - test: two-tailed Wilcoxon signed rank test\n    p: 0.000579\n    n: 26 sessions from 15 subjects\n  data: dataset\n  criterion: \"Methods (Data analysis, EPs analyses and statistical analysis) with the code where they\n    are silent: EEG epochs -2 to +2 s, the -3 to +3 ms artifact replaced by the reversed -9 to -3 ms\n    signal, 0.5 Hz third-order Butterworth high-pass (filtfilt); trials rest when mean wheel speed\n    from -0.5 to +0.5 s is below 0.1 cm/s and active above (Methods; CreateWheelVelocityPerTrial\n    takes the mean linear velocity in that window); deep MOs stimulation in awake mice. Rectified\n    amplitude per session and state is the absolute value of the trial-averaged EP from 150 to 250\n    ms, averaged over time and over all good EEG channels (Methods); a two-tailed Wilcoxon\n    signed-rank test pairs rest and active per session. Open, the unit and the intensity: Figure 1C\n    gives 26 sessions from 15 mice and the high intensity (66.15 uA), while the code's EEG cell\n    keeps both high and medium intensity, a session being one mouse, experiment, sweep and\n    intensity. Readings (a) high intensity only, one value per session; (b) high and medium\n    intensity as separate sessions (code). Open, channel and trial exclusion (visual inspection in\n    the paper, a lab spreadsheet in the code): readings (i) all channels and trials, (ii) channels\n    and trials flagged as bad in the dandiset, if it flags any, removed. Reproduced when, under a\n    reading, the test gives p < 0.05 with rest larger. The code's measure (mean absolute single-trial\n    signal after baseline z-scoring, -1 to -0.01 s) is shown as a variant.\"\n- id: fig1d-lfp-late-rest-larger\n  statement: In mice, the late (150 to 250 ms) MOs LFP response to MOs stimulation has a larger\n    rectified amplitude at rest than during running.\n  source: Figure 1D\n  quote: D Modulation of murine LFP responses in MOs. ... ( n = 13 subjects. two-tailed Wilcoxon\n    signed rank test; p = 0.000976)\n  statistics:\n  - test: two-tailed Wilcoxon signed rank test\n    p: 0.000976\n    n: 13 subjects\n  data: dataset\n  depends_on:\n  - fig1c-eeg-late-rest-larger\n  criterion: \"As fig1c-eeg-late-rest-larger for state and windows, with the LFP of the Neuropixels\n    channels in MOs (Methods, analyses apply to mouse LFP of MOs contacts): epochs -2 to +2 s,\n    detrended (Methods), artifact 0 to 3 ms replaced by the mirrored preceding signal and each\n    channel and trial z-scored to -1 to -0.01 s (code, CSD/LFP Rest-Run cell; the Source Data are in\n    z units); rectified amplitude the absolute value of the trial-averaged signal per channel,\n    averaged over 150 to 250 ms and over MOs channels (code, marked as the method applied in the\n    figure). Intensity open, readings (a) high only, (b) high and medium as separate sessions\n    (code keeps high, medium and unique). Reproduced when, under a reading, a two-tailed Wilcoxon\n    signed-rank test across sessions or mice gives p < 0.05 with rest larger.\"\n- id: fig1e-csd-late-rest-larger\n  statement: In mice, the late MOs CSD response to MOs stimulation is larger at rest than during\n    running, with a current sink between layers 2/3 and 5 at the time of the late response for high\n    and medium but not low intensity.\n  source: Figure 1E; Results, Multiscale late EP responses ..., paragraph 5\n  quote: E Modulation of the murine CSD in MOs. Same structure as ( D ) ( n = 13 subjects.\n    two-tailed Wilcoxon signed rank test; p = 0.001).\n  statistics:\n  - test: two-tailed Wilcoxon signed rank test\n    p: 0.001\n    n: 13 subjects\n  data: dataset\n  depends_on:\n  - fig1d-lfp-late-rest-larger\n  criterion: \"As fig1d-lfp-late-rest-larger with the CSD in place of the LFP. CSD (Methods,\n    Neuropixels EPs pre-processing): channels exceeding +-7 SD of the others interpolated, LFP\n    smoothed in time (1.6 ms) and depth (26 then 4 channels), second spatial derivative, sigma 0.3\n    S/m. Reproduced when, under a reading, the signed-rank test gives p < 0.05 with rest larger.\n    The sink between layers 2/3 and 5 is described from the depth profile and is not judged.\"\n- id: figs1b-mouse-plf\n  statement: In mice the PLF of the late response is larger at rest than during running for LFP\n    and CSD, while for EEG the difference does not reach significance (p = 0.055).\n  source: Figure S1B\n  quote: \"PLF as a function of time from the stimulation onset and averaged PLF calculated over the\n    late response time window (150-250 ms, shaded gray) at rest (black) and active state (red) in\n    mice across recording modalities: EEG, LFP, CSD (Wilcoxon signed rank test: ES-EEG p=0.055;\n    ES-LFP p<0.001; ES-CSD p<0.01).\"\n  statistics:\n  - about: EEG\n    test: Wilcoxon signed rank test\n    p: 0.055\n  - about: LFP\n    test: Wilcoxon signed rank test\n    p: 0.001\n    p_relation: \"<\"\n  - about: CSD\n    test: Wilcoxon signed rank test\n    p: 0.01\n    p_relation: \"<\"\n  data: dataset\n  depends_on:\n  - fig1c-eeg-late-rest-larger\n  - fig1d-lfp-late-rest-larger\n  - fig1e-csd-late-rest-larger\n  criterion: PLF (Methods, after Sinkkonen et al.) per channel is the absolute value of the\n    trial-averaged unit phase vector of the Hilbert transform, averaged over 150 to 250 ms, then\n    over channels; selections and readings as in the three amplitude claims. Reproduced when LFP\n    and CSD give p < 0.05 with rest larger; the EEG result is reported with its p-value and is\n    consistent with the paper when p is between 0.01 and 0.1 or below.\n- id: figs4-intensity-dependence\n  statement: The state modulation of the late response depends on stimulation intensity; EEG late\n    amplitude is larger at rest for high and intermediate but not low intensity, LFP at all three,\n    and CSD for high and intermediate but not low.\n  source: Results, Multiscale late EP responses ..., paragraph 5; Figure S4\n  quote: However, the modulation was reduced, or not observed, when low current intensity was\n    applied (Fig. S4 ).\n  statistics:\n  - about: EEG amplitude, high\n    test: Wilcoxon signed rank test\n    p: 0.001\n    p_relation: \"<\"\n    n: 21 subjects\n  - about: EEG amplitude, intermediate\n    test: Wilcoxon signed rank test\n    p: 0.002\n  - about: EEG amplitude, low\n    test: Wilcoxon signed rank test\n    p: 0.28\n  - about: LFP amplitude, low\n    test: Wilcoxon signed rank test\n    p: 0.003\n  - about: CSD amplitude, intermediate\n    test: Wilcoxon signed rank test\n    p: 0.002\n  - about: CSD amplitude, low\n    test: Wilcoxon signed rank test\n    p: 0.42\n  data: dataset\n  depends_on:\n  - fig1c-eeg-late-rest-larger\n  - fig1d-lfp-late-rest-larger\n  - fig1e-csd-late-rest-larger\n  criterion: Per intensity, the amplitude measures of the three claims it depends on, one value per\n    mouse and state (Figure S4 gives n = 21). Reproduced when EEG and CSD give p < 0.05 with rest\n    larger at high and intermediate and p >= 0.05 at low, and LFP gives p < 0.05 at all three;\n    partially reproduced when the high and intermediate results hold and the low results differ.\n- id: speed-threshold-robust\n  statement: The EEG, LFP and CSD state modulations remain when the speed threshold separating rest\n    and active trials is raised up to 5 cm/s.\n  source: Results, Multiscale late EP responses ..., paragraph 5\n  quote: Note that the same EEG, LFP, and CSD modulations were also observed when using speed\n    thresholds up to 5 cm/s.\n  data: dataset\n  depends_on:\n  - fig1c-eeg-late-rest-larger\n  - fig1d-lfp-late-rest-larger\n  - fig1e-csd-late-rest-larger\n  criterion: The paper gives no list of thresholds tested; thresholds 0.1, 0.5, 1, 2 and 5 cm/s are\n    used here as a standard grid (open; stated as a choice). Reproduced when, at each threshold,\n    EEG, LFP and CSD late amplitudes give p < 0.05 with rest larger, with the methods and the\n    reading under which the three base claims were reproduced; a session with fewer than 10 trials\n    in either state at a threshold is left out (a choice; reported).\n- id: figs5-early-component-mouse\n  statement: In mice the early (3 to 50 ms) EEG component is not modulated by state, while the early\n    LFP and CSD responses are larger during running.\n  source: Results, Multiscale late EP responses ..., paragraph 5; Figure S5\n  quote: The modulation was specific for the late EP component as opposed to the early component\n    (Fig. S5 ), and network specific (Fig. S6 ).\n  statistics:\n  - about: EEG early amplitude\n    test: Wilcoxon signed rank test\n    p: 0.53\n    n: 15 subjects\n  - about: EEG early PLF\n    test: Wilcoxon signed rank test\n    p: 0.052\n  - about: LFP early amplitude, active larger\n    test: Wilcoxon signed rank test\n    p: 0.002\n    n: 13 subjects\n  - about: CSD early amplitude\n    test: Wilcoxon signed rank test\n    p: 0.001\n    p_relation: \"<\"\n  data: dataset\n  depends_on:\n  - fig1c-eeg-late-rest-larger\n  - fig1d-lfp-late-rest-larger\n  - fig1e-csd-late-rest-larger\n  criterion: The three amplitude measures over 3 to 50 ms, with the selections under which the late\n    claims were reproduced. Reproduced when the EEG early amplitude signed-rank test gives p >= 0.05\n    (the paper's test, a claim of absence) and LFP and CSD give p < 0.05 with active larger.\n- id: figs6-posterior-no-modulation\n  statement: Electrical stimulation of posterior areas (visual and retrosplenial cortex,\n    hippocampus) evokes EEG responses whose early and late amplitude and PLF are not modulated by\n    state.\n  source: Figure S6\n  quote: Absence of modulation of the EEG response to the electrical stimulation of control areas\n    (visual cortex, retrosplenial cortex, hippocampus) in mice during rest (black) and active state\n    (red).\n  statistics:\n  - about: early amplitude\n    test: Wilcoxon signed rank test\n    p: 0.15\n    n: 12 sessions from 6 subjects\n  - about: late amplitude\n    test: Wilcoxon signed rank test\n    p: 0.79\n  - about: early PLF\n    test: Wilcoxon signed rank test\n    p: 0.12\n  - about: late PLF\n    test: Wilcoxon signed rank test\n    p: 0.38\n  data: dataset\n  depends_on:\n  - fig1c-eeg-late-rest-larger\n  criterion: A claim of absence. EEG measures as in fig1c-eeg-late-rest-larger and figs1b-mouse-plf,\n    for sessions whose stimulating electrode is in visual cortex, retrosplenial cortex or\n    hippocampus (the code's EEG cell selects the stimulated areas CA3, VIS layer 4, RSPagl layer 6\n    and VISrl layer 5, with high and medium intensity). Reproduced when none of the four\n    signed-rank tests across sessions gives p < 0.05.\n- id: triphasic-pattern\n  statement: Deep MOs stimulation evokes a triphasic spiking pattern in MOs and SM-TH, an initial\n    excitation within 10 ms, an off period of about 10 to 140 ms (127.8 +- 4.1 ms of silence) and a\n    rebound excitation at 140 to 250 ms.\n  source: Results, Multiscale late EP responses ..., paragraph 4; Results, Optogenetic dissection\n    ..., paragraph 1; Figure 2A\n  quote: accompanied by a stereotyped triphasic spiking pattern characterized by an initial\n    excitation (within 10 ms), followed by an off period (i.e., neuronal silence; 10–140 ms) and a\n    strong rebound excitation both in MOs and SM-TH (140-250 ms; Fig. 2A , Fig. S11A )\n  data: dataset\n  expected:\n  - quantity: duration of the off period\n    value: 127.8\n    tolerance: 4.1\n    unit: ms\n  criterion: The paper does not say how the 127.8 ms silence was measured. For responsive (Methods,\n    +-7 SD of the -500 to -50 ms baseline within 3 to 500 ms) RS units in MOs and relay units in\n    SM-TH at high intensity, the population PSTH is computed (1 ms bins). Readings of the silence\n    (open) (a) per mouse, from the end of the initial excitation to the first rebound spike, the\n    median over units of the first spike latency in 75 to 250 ms minus 10 ms, averaged over mice;\n    (b) per mouse, the time the population rate stays below its baseline mean minus 2 SD after the\n    initial peak. Reproduced when both areas show a peak within 10 ms, rate below baseline over most\n    of 10 to 140 ms and a peak in 140 to 250 ms, and under a reading the silence is within 127.8 +-\n    4.1 ms (tolerance the paper's spread); partially reproduced when the pattern holds and the\n    duration does not match.\n- id: fig2b-thalamus-leads\n  statement: The late rebound of SM-TH units precedes that of MOs RS units and the late CSD, LFP and\n    EEG peaks, at rest and during running.\n  source: Figure 2B; Figure S7A; Results, Optogenetic dissection ..., paragraph 1\n  quote: For both resting and active state, SM-TH units rebound consistently and significantly\n    preceded RS cortical rebound spiking and the global mean latencies of CSD, LFP and EEG peaks (\n    p < 0.001, Figs. 2B , S7A .\n  statistics:\n  - test: two-way ANOVA\n    statistic: F = 15.92\n    p: 3.65e-11\n    n: 20, 15, 12, 13 and 13 subjects for SM-TH units, MOs units, CSD, LFP and EEG\n  - about: SM-TH against each other measure\n    test: Tukey post-hoc test\n    p: 0.001\n  data: dataset\n  criterion: \"From Figure S7A legend and MainScript (Rebound ISI and two-way ANOVA cells): per mouse\n    at high intensity, the SM-TH and MOs latency is the median over responsive relay (SM-TH, > 450\n    us) or RS (MOs, > 400 us) units of the first-spike latency in 75 to 250 ms, taken per trial and\n    averaged over trials; the EEG, CSD and LFP latency is, per trial, the time of the largest\n    global field power peak in 75 to 250 ms whose prominence exceeds the baseline mean plus 3 SD\n    (FindResponsePeaks), averaged over trials. Two-way ANOVA on measure and state with Tukey HSD\n    (code, bioinfokit). Reproduced when the measure factor gives p < 0.05 and SM-TH is earlier than\n    each of the four other measures by Tukey at p < 0.05.\"\n- id: figs7a-active-shorter-latency\n  statement: Late responses have shorter latencies during running than at rest for all measures.\n  source: Figure S7A\n  quote: Responses during active state showed shorter latencies than at rest for all the evaluated\n    matrices\n  statistics:\n  - test: two-way ANOVA, Tukey post-hoc test\n    p: 0.001\n    p_relation: \"<\"\n  data: dataset\n  depends_on:\n  - fig2b-thalamus-leads\n  criterion: In the ANOVA of fig2b-thalamus-leads, reproduced when the mean latency is shorter in\n    active than rest for all five measures and the state factor gives p < 0.05.\n- id: figs7b-latency-correlation\n  statement: On single trials, the later the SM-TH units rebound, the later the MOs units and the\n    CSD, LFP and EEG peaks.\n  source: Figure S7B; Results, Optogenetic dissection ..., paragraph 1\n  quote: \"All these metrics positively and significantly correlated with the latency of SM-TH units:\n    that is, the later the SM-TH spiked on any one trial, the later cortical RS responses on that\n    trial (Fig. S7B ; Mixed effect models, all p < 0.001).\"\n  statistics:\n  - test: Mixed effect models\n    p: 0.001\n    p_relation: \"<\"\n    n: 1395 cortical and 1269 thalamic units from 21 subjects\n  data: dataset\n  depends_on:\n  - fig2b-thalamus-leads\n  criterion: Per trial, the latencies of fig2b-thalamus-leads (per-trial values before averaging).\n    Four mixed models as in the Figure S7B legend, Measure ~ ThalamicUnits + (1 | MouseID)\n    (statsmodels mixedlm). Reproduced when all four slopes are positive with p < 0.05.\n- id: fig3a-thalamic-rate-higher-active\n  statement: The evoked firing rate of SM-TH units in the late window (150 to 250 ms) is higher\n    during running than at rest, unlike the late EP component.\n  source: Figure 3A; Results, EP late component to MOs stimulation correlates ..., paragraph 1\n  quote: We indeed observed an increase in the firing rate calculated over the late response time\n    window during the active state (Figs. 3A , S9 , S10 ; p = 0.03, rest lower than active state)\n  statistics:\n  - test: two-tailed Wilcoxon signed rank test\n    p: 0.03\n    n: 1269 units from 21 subjects\n  data: dataset\n  criterion: \"Responsive (+-7 SD, Methods) putative relay units (> 450 us) in the SM-TH nuclei\n    (Methods list), high intensity; per unit, spike count in 150 to 250 ms divided by 0.1 s, averaged\n    over rest and over active trials. Open, the unit of the paired test: the legend says across\n    subjects, the Source Data sheet lists over a thousand rest and active pairs, and the code\n    compares per-session medians with a rank-sum test. Readings (a) per unit, two-tailed Wilcoxon\n    signed-rank on the unit pairs; (b) per mouse, the median over its units, signed-rank on 21\n    pairs. Reproduced when, under a reading, p < 0.05 with active larger; the code's rank-sum on\n    per-session medians is shown as a variant.\"\n- id: figs9-mos-rate-no-modulation\n  statement: The late evoked firing rate of MOs units is not modulated by state.\n  source: Figure S9A\n  quote: MOs firing rate averaged over the late response (150-250 ms, shaded gray) during rest and\n    active state across subjects (n=19 subjects, Wilcoxon signed rank test p = 0.14, ns).\n  statistics:\n  - test: Wilcoxon signed rank test\n    p: 0.14\n    n: 19 subjects\n  data: dataset\n  depends_on:\n  - fig3a-thalamic-rate-higher-active\n  criterion: A claim of absence, on the paper's test. As fig3a-thalamic-rate-higher-active with\n    responsive RS units (> 400 us) in MOs, one median value per mouse and state, two-sided Wilcoxon\n    signed-rank test across mice. Reproduced when p >= 0.05.\n- id: figs10a-fs-trn-no-modulation\n  statement: The late evoked firing of putative cortical interneurons (FS) and TRN units is not\n    modulated by state.\n  source: Figure S10A\n  quote: (Wilcoxon signed rank test; FS p = 0.35, ns; TRN p = 0.77, ns)\n  statistics:\n  - about: MOs FS units\n    test: Wilcoxon signed rank test\n    p: 0.35\n    n: 145 units from 19 mice\n  - about: TRN units\n    test: Wilcoxon signed rank test\n    p: 0.77\n    n: 67 units from 21 mice\n  data: dataset\n  depends_on:\n  - fig3a-thalamic-rate-higher-active\n  criterion: A claim of absence. As fig3a-thalamic-rate-higher-active with responsive FS units (<=\n    400 us) in MOs and units under 350 us in the thalamus (TRN), under the reading of the unit of\n    test adopted there. Reproduced when neither test gives p < 0.05.\n- id: fig3b-bimodal-isi\n  statement: The evoked late ISI of putative thalamic relay units is bimodal, splitting them into\n    high-firing (HF, ISI below 17.88 ms, 569 units) and low-firing (LF, 700 units) groups, while the\n    ISI distributions of cortical RS, cortical FS and TRN units are unimodal.\n  source: Figure 3B; Figure S11B; Results, EP late component ..., paragraph 2\n  quote: One with a short-evoked ISI (<17.88 ms), referred to as high-firing units (HF; n = 569),\n    and a second one characterized by a long-evoked ISI (>17.88 ms) and referred to as low-firing\n    units (LF; n = 700)\n  statistics:\n  - about: relay units\n    test: Dip test\n    p: 0.001\n    p_relation: \"<\"\n    n: 1269 units from 21 subjects\n  - about: TRN units\n    test: Hartigans' dip test\n    p: 0.81\n  - about: MOs RS units\n    test: Hartigans' dip test\n    p: 1\n  - about: MOs FS units\n    test: Hartigans' dip test\n    p: 0.87\n  data: dataset\n  expected:\n  - quantity: HF units\n    value: 569\n    tolerance: 56.9\n  - quantity: LF units\n    value: 700\n    tolerance: 70\n  - quantity: ISI threshold between clusters\n    value: 17.88\n    tolerance: 1.788\n    unit: ms\n  criterion: \"Responsive units at high intensity, classed by spike duration (Methods). Evoked ISI\n    per unit is the median over trials of the interval between the first spike and the next in the\n    late window (Methods); the window is open, (a) 150 to 250 ms (Methods, Figure 3B legend), (b) 75\n    to 250 ms (code, DetectionTimeWindow). k-means with two clusters on the log ISI per unit (code;\n    Methods name cluster.KMeans), threshold the largest ISI of the short cluster; dip test\n    (unidip diptst, code) on log10 ISI per unit for relay, TRN, MOs RS and MOs FS units.\n    Reproduced when, under a reading, the relay dip test gives p < 0.05, the three others p >=\n    0.05, and the counts and threshold are within tolerance (10%); partially reproduced when the\n    dip tests hold and the counts or threshold do not.\"\n- id: figs11d-hf-earlier-less-variable\n  statement: HF units respond earlier and with less latency variability than LF units in the early\n    window (3 to 50 ms).\n  source: Figure S11D; Results, EP late component ..., paragraph 2\n  quote: HF units responded earlier and with less variability than LF units (Fig. S11D ) during the\n    early phase (3–50 ms)\n  statistics:\n  - about: early latency\n    test: Wilcoxon signed rank test\n    p: 0.01\n    p_relation: \"<\"\n  - about: early latency variability\n    test: Wilcoxon signed rank test\n    p: 0.01\n    p_relation: \"<\"\n  data: dataset\n  depends_on:\n  - fig3b-bimodal-isi\n  criterion: Per unit, the median over trials of the first-spike latency in 3 to 50 ms and its SD\n    over trials. The paper names a signed-rank test, which needs pairs; HF and LF are different\n    units, so the pairing is open. Readings (a) per mouse, the median over its HF and over its LF\n    units, signed-rank on the mouse pairs; (b) a rank-sum test on the unit values. Reproduced when,\n    under a reading, HF is lower than LF for both measures with p < 0.05.\n- id: figs12-intensity-shifts-to-hf\n  statement: Higher stimulation intensities recruit more responsive thalamic units and a larger\n    share of HF relative to LF units, LF units shifting to HF as intensity increases.\n  source: Figure S12; Results, EP late component ..., paragraph 2\n  quote: Furthermore, the strength of the electrical stimulus (i.e., current intensity) affected not\n    only the overall number of responsive units, but also the relative size of the two subsets, such\n    that higher stimulation intensities revealed progressively more HF units than LF units (Fig. S12 )\n  data: dataset\n  depends_on:\n  - fig3b-bimodal-isi\n  criterion: The paper reports no test. Units classed HF or LF by the 17.88 ms threshold at each\n    intensity, with the ISI reading of fig3b-bimodal-isi. Reproduced when the number of responsive\n    relay units and the HF fraction both increase from low to intermediate to high intensity\n    (pooled over mice), and the HF fraction per mouse is higher at high than at low intensity in\n    most mice.\n- id: fig3e-baseline-rate-doubles\n  statement: During running the baseline firing rate of thalamic relay units almost doubles (6.78 +-\n    4.4 Hz at rest, 12.48 +- 4.6 Hz active), for both HF and LF units.\n  source: Results, EP late component ..., paragraph 3; Figure 3E\n  quote: By correlating baseline firing rate, ROV, response frequency and late EP component\n    amplitude at the EEG level, we found that the active state almost doubled the thalamic baseline\n    firing rate (from 6.78 ± 4.4 Hz at rest to 12.48 ± 4.6 Hz during active state; p < 0.001)\n  statistics:\n  - about: HF units\n    test: two-tailed Wilcoxon signed rank test\n    p: 2.13e-184\n    p_relation: \"<\"\n    corrected: Bonferroni\n  - about: LF units\n    test: two-tailed Wilcoxon signed rank tests\n    p: 5.67e-169\n    corrected: Bonferroni\n  data: dataset\n  depends_on:\n  - fig3b-bimodal-isi\n  expected:\n  - quantity: baseline firing rate at rest\n    value: 6.78\n    tolerance: 4.4\n    unit: Hz\n  - quantity: baseline firing rate, active\n    value: 12.48\n    tolerance: 4.6\n    unit: Hz\n  criterion: \"Baseline rate per unit and trial is the spike count from -1 to -0.01 s (code,\n    DFLoad_NSpikesWindow) for responsive relay units at high intensity, HF and LF as in\n    fig3b-bimodal-isi. Open, the unit of the test and of the mean +- SD: the code takes per trial\n    the mean over the group's units and compares rest and active trials pooled over sessions with\n    rank-sum tests, Bonferroni over HF and LF, and prints mean and SD of those trial values; the\n    Methods name Wilcoxon signed-rank tests with Bonferroni. Readings (a) per trial as in the code,\n    rank-sum; (b) per unit, mean over rest and over active trials, signed-rank on the unit pairs.\n    Reproduced when, under a reading, the relay-unit mean rate at rest and active are within\n    tolerance (the paper's SDs) and both HF and LF give corrected p < 0.05 with active larger.\"\n- id: fig3e-lf-synchrony-reduced\n  statement: During running the rebound onset variability (ROV) of LF units increases (35.7 +- 11.8\n    to 40.7 +- 8.2 ms), a loss of synchrony, while the ROV of HF units does not change.\n  source: Results, EP late component ..., paragraph 3; Figure 3E\n  quote: correlating with a decreased synchronicity as quantified by the increased onset variability\n    of LF units (from 35.7 ± 11.8 ms at rest to 40.7 ± 8.2 ms during active state; p < 0.001\n  statistics:\n  - about: LF units\n    test: two-tailed Wilcoxon signed rank tests\n    p: 1.38e-05\n    corrected: Bonferroni\n  - about: HF units\n    test: two-tailed Wilcoxon signed rank test\n    p: 0.37\n    corrected: Bonferroni\n  data: dataset\n  depends_on:\n  - fig3e-baseline-rate-doubles\n  expected:\n  - quantity: LF ROV at rest\n    value: 35.7\n    tolerance: 11.8\n    unit: ms\n  - quantity: LF ROV, active\n    value: 40.7\n    tolerance: 8.2\n    unit: ms\n  criterion: \"ROV per trial is the SD across the group's units of the rebound first-spike latency\n    (Methods); window open, (a) 150 to 250 ms (Methods), (b) 75 to 250 ms (code). Unit of test as\n    the two readings of fig3e-baseline-rate-doubles (per trial, rank-sum as in the code; per unit\n    is not defined for an across-unit SD, so the Methods' signed-rank is run per mouse, mean ROV of\n    its rest and active trials). Reproduced when, under a reading, the LF means are within\n    tolerance, LF gives corrected p < 0.05 with active larger, and HF gives p >= 0.05.\"\n- id: fig3e-hf-frequency-reduced\n  statement: During running the late response frequency of HF units falls (309 +- 126 to 241 +- 116\n    Hz), while that of LF units does not change significantly.\n  source: Results, EP late component ..., paragraph 3; Figure 3E\n  quote: and to a smaller response frequency of HF units (from 309 ± 126 Hz at rest to 241 ± 116 Hz\n    during active state; p < 0.001)\n  statistics:\n  - about: HF units\n    test: two-tailed Wilcoxon signed rank test\n    p: 1.9e-33\n    corrected: Bonferroni\n  - about: LF units\n    test: two-tailed Wilcoxon signed rank tests\n    p: 0.08\n    corrected: Bonferroni\n  data: dataset\n  depends_on:\n  - fig3e-baseline-rate-doubles\n  expected:\n  - quantity: HF response frequency at rest\n    value: 309\n    tolerance: 126\n    unit: Hz\n  - quantity: HF response frequency, active\n    value: 241\n    tolerance: 116\n    unit: Hz\n  criterion: Response frequency is the reciprocal of the evoked ISI (Methods); per trial, the code\n    takes the median ISI across the group's units and inverts it. Window and unit of test as in\n    fig3e-lf-synchrony-reduced (per unit, mean frequency over rest and over active trials, for the\n    signed-rank reading). Reproduced when, under a reading, the HF means are within tolerance, HF\n    gives corrected p < 0.05 with rest larger and LF gives p >= 0.05.\n- id: figs13-thalamic-features-predict-eeg\n  statement: On single trials, baseline thalamic rate predicts HF response frequency and LF onset\n    variability, and the late EEG amplitude is predicted by ROV of HF and LF units and by HF\n    response frequency, but not by LF response frequency.\n  source: Figure S13A, S13B; Results, EP late component ..., paragraph 1\n  quote: we found that the rectified amplitude of the EP late component was correlated to the\n    synchronicity and bursting frequency of thalamic units\n  statistics:\n  - about: baseline rate against HF ROV\n    test: Linear mixed effect model\n    p: 0.58\n  - about: baseline rate against HF response frequency\n    test: Linear mixed effect model\n    p: 0.012\n  - about: baseline rate against LF ROV\n    test: Linear mixed effect model\n    p: 0.001\n    p_relation: \"<\"\n  - about: baseline rate against LF response frequency\n    test: Linear mixed effect model\n    p: 0.75\n  - about: EEG late amplitude against HF ROV\n    test: Linear mixed effect model\n    p: 0.001\n    p_relation: \"<\"\n  - about: EEG late amplitude against HF response frequency\n    test: Linear mixed effect model\n    p: 0.001\n    p_relation: \"<\"\n  - about: EEG late amplitude against LF ROV\n    test: Linear mixed effect model\n    p: 0.001\n    p_relation: \"<\"\n  - about: EEG late amplitude against LF response frequency\n    test: Linear mixed effect model\n    p: 0.18\n  data: dataset\n  depends_on:\n  - fig3e-lf-synchrony-reduced\n  - fig3e-hf-frequency-reduced\n  criterion: \"Per trial, the HF and LF features of the two claims it depends on, the baseline rate\n    of fig3e-baseline-rate-doubles and the single-trial EEG late rectified amplitude (150 to 250\n    ms, mean over channels of the absolute signal). Models from the Methods, Feature ~ BaselineFr +\n    (1 | MouseID) and EEG ~ ResponseFrequencyHF + ResponseVariabilityHF + ResponseFrequencyLF +\n    ResponseVariabilityLF + (1 | MouseID) (statsmodels mixedlm). Open, transforms: the code logs\n    the EEG amplitude and the frequencies and centres all terms; readings (a) raw values, (b) the\n    code's transforms. Reproduced when, under a reading, the four effects with p < 0.05 in the\n    paper give p < 0.05 and the four with p >= 0.05 give p >= 0.05; partially reproduced for six or\n    seven of eight.\"\n- id: figs13d-lf-crosscorrelation\n  statement: Cross-correlation between LF thalamic units differs between rest and running, while\n    that between HF units does not.\n  source: Figure S13D; Results, EP late component ..., paragraph 3\n  quote: Cross-correlation of HF and LF SM-TH neurons across rest and active state (black and red\n    traces, respectively. 10 ms window, Wilcoxon signed rank test; LF: p=0.013; HF=0.57).\n  statistics:\n  - about: LF units\n    test: Wilcoxon signed rank test\n    p: 0.013\n  - about: HF units\n    test: Wilcoxon signed rank test\n    p: 0.57\n  data: dataset\n  depends_on:\n  - fig3b-bimodal-isi\n  criterion: Cross-correlograms (Methods) per pair of units in the late window, 2 ms bins of the\n    absolute spike delays divided by the number of seed spikes; the value is the mean over the first\n    10 ms (5 bins), rest and active per pair, Wilcoxon signed-rank test. The late window is open\n    (150 to 250 ms or 75 to 250 ms, as in fig3b-bimodal-isi). Reproduced when, under a reading, LF\n    pairs give p < 0.05 with rest more correlated and HF pairs p >= 0.05.\n- id: discussion-orthodromic-initial-excitation\n  statement: The first-spike latency of the initial response is more variable in SM-TH than in MOs,\n    and does not differ between SM-TH nuclei and TRN.\n  source: Discussion, Mechanisms of neural responses to cortical stimulation, paragraph 1\n  quote: This generates an initial excitation in cortex and in the thalamus mainly via orthodromic\n    activation from the cortex as suggested by the significantly larger variability of the first\n    spike latency in the SM-TH compared to MOs (Wilcoxon test; p < 0.001) and the lack of\n    significant differences between SM-TH nuclei and TRN in the latency of the first spike\n    (Wilcoxon test; p = 0.99).\n  statistics:\n  - about: first-spike latency variability, SM-TH against MOs\n    test: Wilcoxon test\n    p: 0.001\n    p_relation: \"<\"\n  - about: first-spike latency, SM-TH nuclei against TRN\n    test: Wilcoxon test\n    p: 0.99\n  data: dataset\n  criterion: Per responsive unit at high intensity, the median and the SD over trials of the\n    first-spike latency in the early window (3 to 50 ms). The paper does not say whether the test is\n    paired or which variant; readings (a) rank-sum on unit values, (b) signed-rank on per-mouse\n    medians for mice with units in both groups. Reproduced when, under a reading, SM-TH variability\n    exceeds MOs with p < 0.05 and the SM-TH against TRN latency test gives p >= 0.05.\n- id: fig2fg-opto-thalamic-inhibition-delays-rebound\n  statement: Optogenetic activation of TRN (thalamic inhibition) at 75 to 125 ms or 125 to 175 ms\n    after the pulse progressively delays the rebound of SM-TH and MOs units and the late LFP peak\n    (by 58, 8 and 31 ms, and by 72, 39 and 77 ms).\n  source: Results, Optogenetic dissection ..., paragraph 2; Figure 2F, 2G\n  quote: On average, optogenetic stimulation between 75–125 ms following the electrical stimulation\n    delayed the response of SM-TH units, MOs units, and the peak of the LFP by 58 ± 39, 8 ± 28, and\n    31 ± 10 ms, respectively.\n  statistics:\n  - about: SM-TH, ES against ES+Opto75-125\n    test: two-tailed Wilcoxon-signed rank-test\n    p: 2.51e-16\n    n: 118 SM-TH units from 4 mice\n  - about: MOs, ES against ES+Opto125-175\n    test: two-tailed Wilcoxon-signed rank-test\n    p: 6.45e-22\n    n: 155 MOs units from 4 mice\n  - about: LFP peak latency across protocols\n    test: one-way ANOVA test\n    statistic: F = 47.90\n    p: 1.6e-05\n  data: elsewhere\n  where: figshare article 28440311 version 1 (\"Data Mouse Opto\", file 52456058), processed data of\n    the optogenetic experiments as the paper deposited them\n  expected:\n  - quantity: SM-TH delay, Opto 75-125\n    value: 58\n    tolerance: 39\n    unit: ms\n  - quantity: MOs delay, Opto 75-125\n    value: 8\n    tolerance: 28\n    unit: ms\n  - quantity: LFP peak delay, Opto 75-125\n    value: 31\n    tolerance: 10\n    unit: ms\n  - quantity: SM-TH delay, Opto 125-175\n    value: 72\n    tolerance: 53\n    unit: ms\n  - quantity: MOs delay, Opto 125-175\n    value: 39\n    tolerance: 33\n    unit: ms\n  - quantity: LFP peak delay, Opto 125-175\n    value: 77\n    tolerance: 14\n    unit: ms\n  criterion: Tolerances are the paper's SDs. First rebound spike latency per unit in 75 to 250 ms\n    (Results), LFP peak in 75 to 300 ms (Figure 2D legend). Reproduced when the mean delays are\n    within tolerance, the unit comparisons give two-tailed signed-rank p < 0.05 for all six\n    protocol pairs, and the LFP one-way ANOVA gives p < 0.05 with Tukey post hoc tests significant.\n- id: figs8b-opto-cortical-inhibition-minimal\n  statement: Optogenetic activation of GABAergic neurons in MOs minimally shifts the rebound\n    latency (MOs 208, 213, 220 ms; SM-TH 201, 191, 204 ms for ES alone and with light at 75 or 125\n    ms), unlike thalamic inhibition.\n  source: Results, Optogenetic dissection ..., paragraph 3; Figure S8B\n  quote: \"As opposed to thalamic inhibition, optogenetic stimulation of GABAergic neurons in MOs\n    minimally affected the rebound response (Fig. S8B ; MOs: ES Only = 208 ± 39 ms\"\n  data: elsewhere\n  where: figshare article 28440311 version 1 (\"Data Mouse Opto\", file 52456058)\n  expected:\n  - quantity: MOs rebound latency, ES only\n    value: 208\n    tolerance: 39\n    unit: ms\n  - quantity: MOs rebound latency, ES+Opto 75-125\n    value: 213\n    tolerance: 40\n    unit: ms\n  - quantity: MOs rebound latency, ES+Opto 125-175\n    value: 220\n    tolerance: 44\n    unit: ms\n  - quantity: SM-TH rebound latency, ES only\n    value: 201\n    tolerance: 36\n    unit: ms\n  - quantity: SM-TH rebound latency, ES+Opto 75-125\n    value: 191\n    tolerance: 32\n    unit: ms\n  - quantity: SM-TH rebound latency, ES+Opto 125-175\n    value: 204\n    tolerance: 36\n    unit: ms\n  criterion: Tolerances are the paper's SDs. Reproduced when all six means are within tolerance and\n    the mean shifts are smaller than those of fig2fg-opto-thalamic-inhibition-delays-rebound for the\n    same light window in SM-TH.\n- id: fig2h-opto-gaba-suppresses-both\n  statement: Optogenetic activation of GABAergic neurons in either the thalamus or MOs suppresses\n    firing in both SM-TH and MOs units within the light period.\n  source: Figure 2H; Figure S8C; Results, Optogenetic dissection ..., paragraph 3\n  quote: However, optogenetic activation of only GABAergic units in MOs did induce a suppression of\n    firing rate in both RS MOs and SM-TH units (Fig. 2H , S8C ).\n  statistics:\n  - about: thalamic light, SM-TH and MOs units\n    test: Wilcoxon signed rank tests\n    p: 0.001\n    p_relation: \"<\"\n    n: 129 SM-TH and 156 MOs units\n  - about: MOs light, SM-TH and MOs units\n    test: Wilcoxon signed rank tests\n    p: 0.001\n    p_relation: \"<\"\n    n: 417 SM-TH and 440 MOs units\n  data: elsewhere\n  where: figshare article 28440311 version 1 (\"Data Mouse Opto\", file 52456058)\n  criterion: Per unit, firing rate 0 to 50 ms from light onset against a baseline of equal length\n    (open; the paper names only the 0 to 50 ms window, the comparison window is a choice), light\n    alone trials. Reproduced when all four signed-rank tests give p < 0.05 with lower rates during\n    light.\n- id: fig4e-model-latencies\n  statement: In the model, PY neurons fire before TC neurons in the early response (3.15 against\n    8.38 ms) and TC neurons lead PY neurons in the rebound (141.80 against 151.56 ms).\n  source: Figure 4E\n  quote: \"early responses: PY:3.15 ± 3.22 ms; TC:8.38 ± 7.03 ms; two-tailed Wilcoxon-rank-sum test,\n    p = 1.56e-20. Rebound responses: PY:151.56 ± 11.83 ms; TC:141.80 ± 9.68 ms; two-tailed\n    Wilcoxon-rank-sum test, p = 1.11e-04\"\n  statistics:\n  - about: early latency\n    test: two-tailed Wilcoxon-rank-sum test\n    p: 1.56e-20\n    n: 30 sessions\n  - about: rebound latency\n    test: two-tailed Wilcoxon-rank-sum test\n    p: 0.000111\n    n: 30 sessions\n  data: elsewhere\n  where: github.com/bazhlab-ucsd/sleep-stage-transition, branch stim (model), and figshare\n    doi:10.6084/m9.figshare.25773501.v1 (AnalysisRestVSRun_ForSharing.m)\n  expected:\n  - quantity: PY early latency\n    value: 3.15\n    tolerance: 3.22\n    unit: ms\n  - quantity: TC early latency\n    value: 8.38\n    tolerance: 7.03\n    unit: ms\n  - quantity: PY rebound latency\n    value: 151.56\n    tolerance: 11.83\n    unit: ms\n  - quantity: TC rebound latency\n    value: 141.8\n    tolerance: 9.68\n    unit: ms\n  criterion: Tolerances are the paper's SDs. Rerun of the published model (30 trials, 15 rest and 15\n    active, pulse 1 ms to PY 125 to 375 and IN 25 to 75) and analysis code. Reproduced when the four\n    means are within tolerance and both rank-sum tests give p < 0.05 in the stated direction.\n- id: fig4f-model-tc-hyperpolarization\n  statement: In the model, TC neurons hyperpolarize by about 6.3 mV during the 25 to 100 ms off\n    period (-61.38 to -67.64 mV), while PY membrane potential does not change.\n  source: Figure 4F; Results, Cellular mechanisms ..., paragraph 3\n  quote: there was no significant change, compared to baseline, in the membrane potential of PY\n    neurons ( p = 0.46; Baseline\n  statistics:\n  - about: PY baseline against response\n    test: Wilcoxon-rank-sum test\n    p: 0.46\n  - about: TC baseline against response\n    test: two-tailed Wilcoxon-rank-sum test\n    p: 3.87e-20\n    n: 30 sessions\n  data: elsewhere\n  where: github.com/bazhlab-ucsd/sleep-stage-transition, branch stim (model), and figshare\n    doi:10.6084/m9.figshare.25773501.v1\n  expected:\n  - quantity: TC baseline membrane potential\n    value: -61.38\n    tolerance: 0.36\n    unit: mV\n  - quantity: TC off-period membrane potential\n    value: -67.64\n    tolerance: 3.13\n    unit: mV\n  criterion: Tolerances are the paper's SDs. Reproduced when the TC values are within tolerance with\n    the rank-sum test p < 0.05, and the PY test gives p >= 0.05.\n- id: fig4hi-model-gaba-contributions\n  statement: In the model, silencing TRN leaves the pause-burst pattern largely intact, silencing\n    cortical interneurons abolishes the thalamic rebound, and stronger cortical and thalamic GABA-A\n    connections both deepen TC hyperpolarization.\n  source: Figure 4H, 4I; Results, Cellular mechanisms ..., paragraph 4\n  quote: When TRN was silenced, the pause-burst pattern appeared to be largely unaffected (Fig. 4H ,\n    top). Conversely, when cortical interneurons were silenced, PY showed a reduced off-period, and\n    the thalamic rebound was abolished.\n  data: elsewhere\n  where: github.com/bazhlab-ucsd/sleep-stage-transition, branch stim (model)\n  criterion: The paper reports no measure. Rerun with TRN silenced, with IN silenced, and over a grid\n    of IN to PY and TRN to TC GABA-A strengths. Reproduced when TC neurons still rebound in 75 to 250\n    ms with TRN silenced, do not rebound with IN silenced, and the mean TC voltage in 25 to 100 ms\n    falls as either strength increases.\n- id: figs14a-model-hf-more-input\n  statement: In the model, TC neurons that receive more synaptic input from the stimulated PY\n    neurons have shorter rebound ISIs (HF), with HF neurons receiving about twice the input of LF\n    neurons (0.77 against 0.37 uS/cm2).\n  source: Figure S14A; Results, Cellular mechanisms ..., paragraph 4\n  quote: \"Lastly, as suggested by the mouse data, the model confirms that TC neurons exhibit two\n    rebound regimens, determined by the amount of synaptic inputs they receive from cortical neurons\n    (Wilcoxon rank sum test; p < 0.001; HF: 0.77 ± 0.098 μS/cm 2 ; LF: 0.37 ± 0.16 μS/cm 2 ; Fig.\n    S14 )\"\n  statistics:\n  - about: HF against LF synaptic input\n    test: Wilcoxon rank sum test\n    p: 0.001\n    p_relation: \"<\"\n  - about: rebound ISI against synaptic input\n    test: Pearson's correlation\n    statistic: r = -0.68\n    p: 0.001\n    p_relation: \"<\"\n  data: elsewhere\n  where: github.com/bazhlab-ucsd/sleep-stage-transition, branch stim (model), and figshare\n    doi:10.6084/m9.figshare.25773501.v1\n  expected:\n  - quantity: HF synaptic input\n    value: 0.77\n    tolerance: 0.098\n    unit: uS/cm2\n  - quantity: LF synaptic input\n    value: 0.37\n    tolerance: 0.16\n    unit: uS/cm2\n  criterion: Tolerances are the paper's SDs; HF and LF split at 17.88 ms. Reproduced when both means\n    are within tolerance, the rank-sum test gives p < 0.05 and the correlation is negative with p <\n    0.05.\n- id: figs14b-model-state-effects\n  statement: In the model the active state lowers the rebound firing rate of HF neurons and raises\n    the onset variability of LF neurons, as in the mice.\n  source: Figure S14B\n  quote: \"Left: evoked firing rate for HF units (Wilcoxon Rank sum test; p<0.001). Right: response\n    onset variability for LF units (Wilcoxon Rank sum test; p=0.019).\"\n  statistics:\n  - about: HF evoked firing rate\n    test: Wilcoxon Rank sum test\n    p: 0.001\n    p_relation: \"<\"\n  - about: LF response onset variability\n    test: Wilcoxon Rank sum test\n    p: 0.019\n  data: elsewhere\n  where: github.com/bazhlab-ucsd/sleep-stage-transition, branch stim (model), and figshare\n    doi:10.6084/m9.figshare.25773501.v1\n  criterion: Reproduced when the rerun model gives a lower HF evoked rate and a higher LF ROV in\n    active than rest trials, each with rank-sum p < 0.05.\n"
}
```

```
File created successfully at: claims/russo-2025.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/russo-2025.yaml paper/10.1038-s41467-025-58717-2.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import re
lines=open('claims/russo-2025.yaml').read().split('\n')
inq=False
for i,l in enumerate(lines,1):
    if l.startswith('#'): continue
    m=re.match(r'^(\s*-?\s*[a-z_]+: )(.*)$',l)
    body=m.group(2) if m else l
    if m:
        inq = body.startswith('"') and not (body.endswith('"') and len(body)>1)
        if body.startswith('"'): continue
        if ': ' in body: print(i,l)
    else:
        if inq:
            if l.rstrip().endswith('"'): inq=False
            continue
        if ': ' in l: print(i,l)
EOF
```

```
866     traces, respectively. 10 ms window, Wilcoxon signed rank test; LF: p=0.013; HF=0.57).
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/russo-2025.yaml",
 "old_string": "  quote: Cross-correlation of HF and LF SM-TH neurons across rest and active state (black and red\n    traces, respectively. 10 ms window, Wilcoxon signed rank test; LF: p=0.013; HF=0.57).",
 "new_string": "  quote: \"Cross-correlation of HF and LF SM-TH neurons across rest and active state (black and red\n    traces, respectively. 10 ms window, Wilcoxon signed rank test; LF: p=0.013; HF=0.57).\""
}
```

```
The file claims/russo-2025.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/russo-2025.yaml paper/10.1038-s41467-025-58717-2.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -i 's/    p: 0.000111$/    p: 1.11e-04/' claims/russo-2025.yaml && python tools/claims_check.py claims/russo-2025.yaml paper/10.1038-s41467-025-58717-2.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 55,106p tools/claims_check.py
```

```
if i < 0:
                break
            pos = i + len(f)
        else:
            return True
    return False


def printed_forms(v: float) -> set[str]:
    """Ways a paper prints a number: 0.002, .002, 2 × 10-5, 2e-5, 0.00002, 10-10."""
    out = {f"{v:g}", f"{v:g}".lstrip("0") if abs(v) < 1 else f"{v:g}"}
    if 0 < abs(v) < 1:
        m, e = f"{v:.3e}".split("e")
        m, e = f"{float(m):g}", str(int(e))
        out |= {f"{m}×10{e}", f"{m} × 10{e}", f"{m} x 10{e}", f"{m}x10{e}", f"{m}e{e}"}
        if m == "1":
            out.add(f"10{e}")
    if 0 < abs(v) < 0.001:
        plain = f"{v:.12f}".rstrip("0")
        out |= {plain, plain.lstrip("0")}
[... 32 more lines not kept]
```

**Agent**

The checker's one remaining flag is a format limit: the paper prints "p = 1.11e-04" (Figure 4E legend), which I confirmed by reading; the checker only tries "1.11e-4". Making two small wording fixes.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/russo-2025.yaml",
 "old_string": "    over channels; selections and readings as in the three amplitude claims. Reproduced when LFP\n    and CSD give p < 0.05 with rest larger; the EEG result is reported with its p-value and is\n    consistent with the paper when p is between 0.01 and 0.1 or below.",
 "new_string": "    over channels; selections and readings as in the three amplitude claims. Reproduced when LFP\n    and CSD give p < 0.05 with rest larger. The paper reports EEG at p = 0.055 and does not claim\n    it, so the EEG result is reported with its p-value and does not decide the claim."
}
```

```
The file claims/russo-2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/russo-2025.yaml",
 "old_string": "    10% of the Source Data medians, and at least four of the five Figure 2B means are within 10 ms\n    of the Source Data means; partially",
 "new_string": "    10% of the Source Data medians, and at least four of the five Figure 2B means are within 10%\n    of the Source Data means; partially"
}
```

```
The file claims/russo-2025.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/russo-2025.yaml",
 "old_string": "  criterion: The paper does not say how the 127.8 ms silence was measured. For responsive",
 "new_string": "  criterion: The paper does not say how the 127.8 ms silence was measured, and neither does the\n    code read; the two readings below are this file's, from the Results wording. For responsive"
}
```

```
The file claims/russo-2025.yaml has been updated successfully.
```

**Agent calls Bash**

```bash
python tools/claims_check.py claims/russo-2025.yaml paper/10.1038-s41467-025-58717-2.txt; grep -c "—\|rather" claims/russo-2025.yaml; git status --short
```

Result: not kept, because it reads the paper's text.

**Agent**

I wrote `claims/russo-2025.yaml` (not committed). It has 39 claims, and every one has a word-for-word quote, so none needed an `inferred` note. The checker passes everything except one p-value: the paper prints "p = 1.11e-04" in the Figure 4E legend and the checker only looks for "1.11e-4". I confirmed that value by reading the legend and left the checker alone.

**Text read.** The version of record from PubMed Central (main text, Methods, legends), the supplement PDF as text (Figures S1 to S14 and Table S1), and the Source Data spreadsheet. No PDF page was opened. Nothing the claims needed was missing from the paper.

**Code read.** The mouse analysis on figshare (doi:10.6084/m9.figshare.28047749 v1). It is a copy of AllenInstitute/tbd_eeg at commit ef9aa65 plus the paper's notebooks; I read the relevant cells of MainScript.ipynb and the wheel-speed notebook. I also read the human scripts (figshare 25595829 and 25595871). I did not read the model code or the simulated-data analysis.

**Claims**
- **Data:** 22 claims use the dandiset (1 of them is a `link` check against the Source Data). 17 are `data: elsewhere`:
  - 6 human claims: only the per-subject values in the Source Data file are public.
  - 3 optogenetics claims: the processed data are on figshare (article 28440311).
  - 5 simulation claims: the model on GitHub plus the figshare analysis code.
  - 1 human claim (Figure 5A, human against mouse traces) has no public data, so it is untestable unless the author finds the human grand averages.
- **Statistics:** 36 claims record the paper's tests, 81 p-values in all.
- **Expected values:** 15 claims carry numbers to match. Tolerances are the paper's SDs where it gives them, otherwise 10%.
- **Criteria:** all 39 have one.

**Details the paper leaves open, with the readings named**
- **Unit and intensity for Figure 1C (mouse EEG):** (a) high intensity only, one value per session; (b) high and medium intensity as separate sessions, which is what the code does. The same choice applies to the LFP and CSD panels.
- **EEG channel and trial exclusion:** the paper uses visual inspection and the code a lab spreadsheet that isn't deposited. Readings: (i) keep all channels and trials; (ii) drop any the dandiset flags as bad.
- **EEG rectified amplitude:** the Methods (absolute value of the averaged response) are followed. The code's version (average of absolute single trials after baseline z-scoring) is a variant.
- **Unit of the rest against active unit tests (Figures 3A and 3E):** the Methods say Wilcoxon signed-rank; the code uses rank-sum on per-trial or per-session values. Readings: (a) per trial with rank-sum, as in the code; (b) per unit or per mouse with signed-rank, as in the Methods.
- **Window for the evoked ISI, onset variability and response frequency:** (a) 150 to 250 ms, from the Methods; (b) 75 to 250 ms, from the code.
- **HF against LF in Figure S11D:** the paper names a signed-rank test, but HF and LF are different units. Readings: per-mouse pairs, or rank-sum on units.
- **Mixed-model transforms (Figure S13):** raw values, or the code's logs and centring.
- **How the 127.8 ms off period was measured:** neither the paper nor the code says. I named two readings of my own, based on the Results wording.
- **Speed thresholds "up to 5 cm/s":** the grid of 0.1, 0.5, 1, 2 and 5 cm/s is my choice and is stated as such.
- **Quality thresholds for sorted units:** the paper only cites Siegle, Jia et al. Readings: units as deposited, or filtered by any quality labels the dandiset carries.
- **Pearson or Spearman for the human early against late correlation:** the text and the legend disagree, so both are run.

**Where the claims can't use the paper's own test**
- The human iEEG mixed models need per-contact values, which aren't public. Those claims fall back to tests on the five per-subject Source Data values, recorded as a deviation.
- The lab spreadsheet behind the code's session flags and bad channels or trials isn't in the deposit, so those selections stay open as named above.

## End of run

62 turns, 8 minutes, $4.95 at API prices, result: success.
