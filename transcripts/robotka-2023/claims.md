# robotka-2023 · claims · run 42947492403

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  grep -n "^#" docs/protocol.md | head -50; ls paper/ claims/ | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1,200p docs/protocol.md; ls -la paper/
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  cat claims/fouke-2025.yaml | head -150; cat papers/datasets/robotka-2023.yaml; cat paper/aa-5.data-description.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent**

Now read the paper text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2023.112034.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2023.112034.txt",
 "offset": 844,
 "limit": 700
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "paper/10.1016-j.celrep.2023.112034.txt",
 "offset": 1544,
 "limit": 625
}
```

Result: not kept, because it reads the paper's text.

**Agent**

Full text, Methods and supplement are present. Now the code.

**Agent calls Bash**

```bash
cd $TMPDIR && git clone -q https://github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 ens 2>&1 | tail -3; cd ens && git log -1 --format='%H %cd' && find . -type f -not -path './.git/*' | head -80
```

```
f2d237639217425e7fc81d694708f19428a3b026 Mon Nov 21 12:11:33 2022 -0800
./decodingCallTypesNaiveBayesPart2-PerRegion.ipynb
./DisplayKDEandPCJulie.ipynb
./plotConfusionsHerminaNW.ipynb
./SpikeSortingStatisticsPart2.ipynb
./readRHDHeader.ipynb
./decodingCallTypesNaiveBayesPart2AcousticClusters.ipynb
./SpikeSortingStatistics.ipynb
./plotConfusionsJulie.ipynb
./GenerateDataBase2.ipynb
./decodingCallTypesNaiveBayesPart3Julie.ipynb
./decodingCallTypesNaiveBayes.ipynb
./SummaryStatistics.ipynb
./decodingCallTypesNaiveBayesJulie.ipynb
./plotConfusionsArea.ipynb
./gapEstimation.ipynb
./plotElectrodes3D.ipynb
./decoders.py
./README.md
./EPHYS1-Generate_Dataframes.ipynb
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ens && cat README.md; python3 - <<'EOF'
import json,glob
for f in sorted(glob.glob('*.ipynb')):
    nb=json.load(open(f))
    code=[ ''.join(c['source']) for c in nb['cells'] if c['cell_type']=='code']
    print(f, len(code), sum(len(c) for c in code))
EOF
wc -l decoders.py config.py
```

```
# Ensemble-Code-Cell-Reports-2022

This repository has all the jupyter notebooks and python code that were used in the decoding, encoding and hierarchical analyses of the ensemble neural responses of high-level avian auditory neurons for call types.  The research was published in:

<i> Sparse Ensemble Neural Code for a Complete Vocal Repertoire </i> by Robotka et al. Cell Reports 2022.

DataBaseMerge.ipynb 11 13184
DisplayKDEandPCJulie.ipynb 12 10758
Download good pkl files.ipynb 44 31095
EPHYS1-Generate_Dataframes.ipynb 19 12106
EPHYS2-Population_Coding.ipynb 55 21420
EPHYS3-Neural_Clustering.ipynb 54 24961
EPHYS4-Population_Clustering.ipynb 98 35790
Generate vocParamTable.ipynb 11 8737
GenerateDataBase.ipynb 14 13517
GenerateDataBase2.ipynb 17 14024
GenerateDataBasePosPC.ipynb 13 17032
GenerateMLFilters.ipynb 59 39328
GenerateMLFiltersJulie.ipynb 56 40558
GenerateMLFiltersJuliePerZone.ipynb 33 20058
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ens && mkdir -p ../encode && python3 - <<'EOF'
import json,glob
for f in sorted(glob.glob('*.ipynb')):
    try: nb=json.load(open(f))
    except Exception as e: print('BAD',f); continue
    out=[]
    for i,c in enumerate(nb['cells']):
        src=''.join(c['source'])
        if c['cell_type']=='markdown': out.append(f'## [md {i}]\n'+src)
        elif c['cell_type']=='code':
            out.append(f'## [code {i}]\n'+src)
            for o in c.get('outputs',[]):
                t=o.get('text') or o.get('data',{}).get('text/plain')
                if t:
                    t=''.join(t)
                    out.append('# OUT: '+t[:1500])
    open('../encode/'+f.replace(' ','_')+'.py','w').write('\n'.join(out))
EOF
ls -la ../encode | head -60
```

```
BAD SpikeSortingStatistics.ipynb
total 1104
drwxr-xr-x 2 runner runner   4096 Nov 11 02:44 .
drwx------ 7 runner runner   4096 Nov 11 02:44 ..
-rw-r--r-- 1 runner runner  16508 Nov 11 02:44 DataBaseMerge.ipynb.py
-rw-r--r-- 1 runner runner  11519 Nov 11 02:44 DisplayKDEandPCJulie.ipynb.py
-rw-r--r-- 1 runner runner 135176 Nov 11 02:44 Download_good_pkl_files.ipynb.py
-rw-r--r-- 1 runner runner  20357 Nov 11 02:44 EPHYS1-Generate_Dataframes.ipynb.py
-rw-r--r-- 1 runner runner  30961 Nov 11 02:44 EPHYS2-Population_Coding.ipynb.py
-rw-r--r-- 1 runner runner  57993 Nov 11 02:44 EPHYS3-Neural_Clustering.ipynb.py
-rw-r--r-- 1 runner runner  83274 Nov 11 02:44 EPHYS4-Population_Clustering.ipynb.py
-rw-r--r-- 1 runner runner  15395 Nov 11 02:44 GenerateDataBase.ipynb.py
-rw-r--r-- 1 runner runner  19079 Nov 11 02:44 GenerateDataBase2.ipynb.py
-rw-r--r-- 1 runner runner  19001 Nov 11 02:44 GenerateDataBasePosPC.ipynb.py
-rw-r--r-- 1 runner runner  52625 Nov 11 02:44 GenerateMLFilters.ipynb.py
-rw-r--r-- 1 runner runner  53346 Nov 11 02:44 GenerateMLFiltersJulie.ipynb.py
-rw-r--r-- 1 runner runner  27784 Nov 11 02:44 GenerateMLFiltersJuliePerZone.ipynb.py
-rw-r--r-- 1 runner runner  29609 Nov 11 02:44 GenerateMLFiltersPerZone.ipynb.py
-rw-r--r-- 1 runner runner   9305 Nov 11 02:44 GenerateReport.ipynb.py
-rw-r--r-- 1 runner runner   8751 Nov 11 02:44 GenerateReport2.ipynb.py
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && cat GenerateDataBase.ipynb.py | cut -c1-300
```

```
## [md 0]
### Generates a data base of responses for each trail for the single units. 

#### Run this notebook after creating the /PlaybackPkl files inside the site folder using PlotSpikeSortedCategoriesGUI.ipynb

#### You should only have to modify the rootPath in cell 2 for this notebook to work.

## [code 1]
# Dependencies 
import os
import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle as pk
from scipy.stats import t
from sklearn.decomposition import PCA

## [md 2]
[... 418 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && diff GenerateDataBase.ipynb.py GenerateDataBase2.ipynb.py | cut -c1-250 | head -150; grep -n "HerminaDataBase\|\.pkl'" *.py | cut -c1-200 | head -60
```

```
4c4
< #### Run this notebook after creating the /PlaybackPkl files inside the site folder using PlotSpikeSortedCategoriesGUI.ipynb
---
> #### Run this notebook after creating the /PlaybackPkl files. For Julie's data these were made by translating the h5 files  using readUnith5_file.ipynb
24,25c24,25
< rootPath = '[removed: a home directory path]/Code/songephys/'
< dataPath = 'data/birds/'
---
> rootPath = '[removed: a home directory path]/Google Drive/My Drive/julie/'
> pklPath = 'pkl'
27,33c27,30
< birds = [
<     os.path.basename(bird)
<     for bird in sorted(glob.glob(os.path.join(rootPath+dataPath, "*")), key=os.path.getmtime, reverse=True)
<     if (os.path.isdir(bird))]
< ## [code 4]
< birds = ['ZF7F', 'ZF6M', 'ZF5M', 'ZF4F']
< ## [md 5]
---
> 
[... 191 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && diff GenerateDataBase.ipynb.py GenerateDataBasePosPC.ipynb.py | cut -c1-250 | head -80; cut -c1-250 DataBaseMerge.ipynb.py | head -400
```

```
176,205c176,178
< dfDataBase = pd.DataFrame(columns=['bird', 'site', 'unit', 'stim', 'call', 'trial', 'R', 'z', 'PC'])
< itKDE = 1000    # Number of points in the KDE for PCs
< 
< kdeList = []
< 
< for bird in birds:    
<     # Find sites
<     sites = [ 
<         os.path.basename(site)
<         for site in glob.glob(os.path.join(rootPath+dataPath+bird+'/sites/', "*"))
<     ]
<     
<     # Loop through sites
<     for site in sites:
<         playPklPath = rootPath + dataPath + bird + '/sites/' + site + '/PlaybackPkl/'
<     
<         # Set up list of Playback files available for this site
<         playPkls = [ 
<             os.path.basename(efile)
[... 461 more lines not kept]
```

**Agent**

Full text, Methods and supplement are all present. I've cloned the analysis code (commit f2d2376) and am reading the decoder code now.

**Agent calls Bash**

```bash
cd $TMPDIR/ens && cat decoders.py config.py | cut -c1-220
```

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 09:36:09 2021

@author: frederictheunissen
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.naive_bayes import GaussianNB

import config



def naiveBayes(unitChoice, plotFlg = False, usingAllCombos = False, code='PC', verbose = False, nperm=100):
    # naiveBayes runs a guassian classifier for call types using the responses in the units in the list unitChoice
    
    dfDataBase = config.DF
    
[... 421 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && cut -c1-250 decodingCallTypesNaiveBayes.ipynb.py | grep -v "^# OUT: Total\|^Total number\|^PCC" | head -300
```

```
## [code 0]
# Dependencies 
import os
import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle as pk
from scipy.stats import t
from sklearn.naive_bayes import GaussianNB
from scipy.special import comb


from soundsig.discriminate import discriminatePlot
## [code 1]
# Some paths
rootPath = '[removed: a home directory path]/Code/songephys/'
dataPath = 'data/birds/'

[... 282 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && for f in decodingCallTypesNaiveBayesPart2.ipynb.py decodingCallTypesNaiveBayesPart3Julie.ipynb.py; do echo "=== $f"; awk '/^# OUT:/{skip=1} /^## \[/{skip=0} !skip' $f | cut -c1-200 | grep -v "^\s*$" | head -230; done
```

```
=== decodingCallTypesNaiveBayesPart2.ipynb.py
## [code 0]
# Dependencies 
import os
import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle as pk
import multiprocessing as mp
from scipy.stats import t
from sklearn.naive_bayes import GaussianNB
from scipy.special import comb
from scipy.stats import norm
from decoders import naiveBayes
import h5py
import config
## [code 1]
# Some paths
[... 443 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && awk '/^# OUT:/{skip=1} /^## \[/{skip=0} !skip' GenerateMLFilters.ipynb.py | cut -c1-200 | grep -v "^\s*$" | sed -n 1,400p | grep -n "" | grep -iv "plt\.\|ax\.\|color\|fig" | head -330
```

```
1:## [code 0]
2:# Dependencies 
3:import os
4:import glob
5:import re
6:import numpy as np
7:import matplotlib.pyplot as plt
8:import pandas as pd
9:import pickle as pk
10:from scipy.stats import t
11:from soundsig.sound import BioSound
13:## [code 1]
14:# Some paths
15:rootPath = '[removed: a home directory path]/Code/songephys/'
16:dataPath = 'data/birds/'
17:birds = [
18:    os.path.basename(bird)
19:    for bird in sorted(glob.glob(os.path.join(rootPath+dataPath, "*")), key=os.path.getmtime, reverse=True)
20:    if (os.path.isdir(bird))]
23:             'Di': (255/255.0, 105/255.0, 15/255.0), 'Ag': (255/255.0, 0/255.0, 0/255.0), 'Wh': (255/255.0, 180/255.0, 255/255.0), 'Ne': (255/255.0, 100/255.0, 255/255.0),
[... 284 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && awk '/^# OUT:/{skip=1} /^## \[/{skip=0} !skip' GenerateMLFilters.ipynb.py | cut -c1-200 | grep -v "^\s*$" | sed -n 400,1200p | grep -iv "plt\.\|ax\.\|color\|fig\|set_" | head -400
```

```
callMPS = {'Be': [], 'LT': [], 'Th': [], 
             'Di': [], 'Ag': [], 'Wh': [], 'Ne': [],
             'Te': [], 'DC': [], 'So': []}
    callSpectro = {'Be': [], 'LT': [], 'Th': [], 
             'Di': [], 'Ag': [], 'Wh': [], 'Ne': [],
             'Te': [], 'DC': [], 'So': []}
    # Find the unique stims played for the chosen unit
    unitIndex = dfDataBase.index[dfDataBase['site']+'_'+ dfDataBase['unit'] == unit]
    unitIndexLen = len(unitIndex)
    stimList = list(dfDataBase['stim'][unitIndex].array)
    stimNames = np.unique(stimList)
    print('Found', len(stimNames), 'unique stimuli')
    # Calculate all the MPS, store them and make a running total for averaging
    firstTime = True
    for stim in stimNames:
        # These are the rows that have this stim. 
        unitIndexStim = [ind for ind in unitIndex if dfDataBase['stim'][ind] == stim]
        # Use the data in the first unit to find the stim           
        playbackPkl = dfDataBase['unit'][unitIndexStim[0]]
        playPklPath = rootPath + dataPath + dfDataBase['bird'][unitIndexStim[0]] + '/sites/' + dfDataBase['site'][unitIndexStim[0]] + '/PlaybackPkl/'
[... 381 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && grep -n "## \[code 3[45]\]" -A12 GenerateMLFilters.ipynb.py | cut -c1-200; awk '/^## \[code 53\]/{p=1} p' GenerateMLFilters.ipynb.py | cut -c1-200 | grep -v "^\s*$" | grep -iv "plt\.\|ax\.\|color\|fig\|set_" | head -200
```

```
928:## [code 34]
929-# Look at the DFA Space:
930-eigMatrix = np.matmul(np.linalg.pinv(withinCov, rcond = 0.0001, hermitian=True), betweenCov)
931-#eigMatrix = betweenCov
932-#eigMatrix = overallCov
933-eigVal, eigVect = np.linalg.eigh(eigMatrix)
934:## [code 35]
935-plt.plot(np.cumsum(np.abs(eigVal[0:10])))
936-# OUT: [<matplotlib.lines.Line2D at 0x7fd86385bd00>]
937-# OUT: <Figure size 432x288 with 1 Axes>
938-## [code 36]
939-plt.figure(dpi=300, figsize= (6, 3))
940-ex = (wt[indTLow], wt[indTHigh-1], wf[indFLow]*1e3, wf[indFHigh-1]*1e3)
941-cmap = plt.get_cmap('jet')
942-                
943-for iplot in range(3):
944-    plt.subplot(1,3,1+iplot)
945-    plt.imshow(np.reshape(eigVect[:,iplot], mpstemp.shape), interpolation='nearest', aspect='auto', origin='lower', cmap=cmap, extent=ex)
946-    plt.clim(-0.25,0.25)
## [code 53]
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && grep -n "R2=\|np.sum(indGood)" -A1 GenerateMLFilters.ipynb.py | cut -c1-200; grep -n "## \[code 51\]" -A3 GenerateMLFilters.ipynb.py; grep -n "## \[code 9\]" -A3 GenerateMLFilters.ipynb.py
```

```
1305:print('R2=', r2adj, 'F(1,', dfd, ')=' , fval, 'p=', pval)
1306-
--
1309:# OUT: R2= 0.09708196841929917 F(1, 79 )= 8.750543585214825 p= 0.004081787820817362
1310-
--
1313:np.sum(indGood)
1314-# OUT: 1746
--
1326:print('R2=', r2adj, 'F(1,', dfd, ')=' , fval, 'p=', pval)
1327-# OUT: The PostScript backend does not support transparency; partially transparent artists will be rendered opaque.
--
1329:# OUT: R2= 0.09934320556613618 F(1, 79 )= 8.975643155715106 p= 0.0036540354230240046
1330-
--
1342:print('R2=', r2adj, 'F(1,', dfd, ')=' , fval, 'p=', pval)
1343-# OUT: The PostScript backend does not support transparency; partially transparent artists will be rendered opaque.
--
1345:# OUT: R2= 0.07630933465989609 F(1, 79 )= 6.734254059169004 p= 0.011271074752492671
1346-
[... 23 more lines not kept]
```

**Agent**

Code so far settles several open points (CV scheme, the PCC>30 filter giving 1,746 ensembles, log volume, noise as variance). Reading the summary-statistics and clustering notebooks next.

**Agent calls Bash**

```bash
cd $TMPDIR/encode && awk '/^# OUT:/{skip=1} /^## \[/{skip=0} !skip' SummaryStatistics.ipynb.py | cut -c1-220 | grep -v "^\s*$" | grep -iv "plt\.\|ax\.\|color\|fig\|set_" | head -250; echo ======; cat Supplementary_Calculations.ipynb.py | cut -c1-250
```

```
## [md 0]
## Reads the summary file and makes some summary statistics
## [code 1]
# Dependencies 
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle as pk
from scipy.stats import t, ks_2samp
## [code 2]
# Set paths
rootPathH = '[removed: a home directory path]/Code/songephys/'
dataPathH = 'data/birds/'
rootPathJ = '/[removed: a home directory path]/Google Drive/My Drive/julie/'
dataPathJ = 'pkl/'
## [code 3]
# Read data files 
inPathH = rootPathH+dataPathH+'summarySel.pkl'
fileInH = open(inPathH,"rb")
dfSummaryH = pk.load(fileInH)
[... 349 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && grep -n "selInd" *.py | grep -v "SummaryStatistics\|GenerateMLFilters" | cut -c1-220 | head -20
```

```
Download_good_pkl_files.ipynb.py:132:summary[(summary['zAud'] > .5)&(summary['selInd'] > .1)].shape
Download_good_pkl_files.ipynb.py:134:for ind,row in summary[(summary['zAud'] > .5)&(summary['selInd'] > .1)].iterrows():
Download_good_pkl_files.ipynb.py:165:for ind,row in summary[(summary['zAud'] > .5)&(summary['selInd'] > .1)].iterrows():
Download_good_pkl_files.ipynb.py:321:for ind,row in summary[(summary['zAud'] > .5)&(summary['selInd'] > .1)].iterrows():
Download_good_pkl_files.ipynb.py:617:for ind,row in summary[(summary['zAud'] > .5)&(summary['selInd'] > .1)].iterrows():
Download_good_pkl_files.ipynb.py:1499:good_inds = (summary['zAud'] > .5)&(summary['selInd'] > .1)
Download_good_pkl_files.ipynb.py:1778:good_inds = (summary['zAud'] > .5)&(summary['selInd'] > .1)
Download_good_pkl_files.ipynb.py:2105:good_inds = (summary['zAud'] > .5)&(summary['selInd'] > .1)
Download_good_pkl_files.ipynb.py:2436:good_inds = (summary['zAud'] > .5)&(summary['selInd'] > .1)
Download_good_pkl_files.ipynb.py:2643:good_inds = (summary['zAud'] > .5)&(summary['selInd'] > .1)
Download_good_pkl_files.ipynb.py:2862:good_inds = (summary['zAud'] > .5)&(summary['selInd'] > .1)
Download_good_pkl_files.ipynb.py:3165:summary[(summary['zAud'] > .5)&(summary['selInd'] > .1)].shape
Download_good_pkl_files.ipynb.py:3191:#for ind,row in summary[(summary['zAud'] > .5)&(summary['selInd'] > .1)].iterrows():
Download_good_pkl_files.ipynb.py:3229:for ind,row in summary[(summary['zAud'] > .5)&(summary['selInd'] > .1)].iterrows():
EPHYS1-Generate_Dataframes.ipynb.py:125:print(summary[(summary['zAud'] > .5)&(summary['selInd'] > .1)].shape)
EPHYS3-Neural_Clustering.ipynb.py:115:print(summary[(summary['zAud'] > .5)&(summary['selInd'] > .1)].shape)
EPHYS3-Neural_Clustering.ipynb.py:200:for ind,row in summary[(summary['zAud'] > .5)&(summary['selInd'] > .1)].iterrows():
EPHYS3-Neural_Clustering.ipynb.py:345:for ind,row in summary[(summary['zAud'] > .5)&(summary['selInd'] > .1)].iterrows():
EPHYS3-Neural_Cluste
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && grep -ln "summarySel" *.py; grep -n "zcall\|sparse\|1.0 - \|1-1/" GenerateReport.ipynb.py GenerateReport2.ipynb.py | cut -c1-200 | head -30
```

```
Download_good_pkl_files.ipynb.py
EPHYS1-Generate_Dataframes.ipynb.py
EPHYS3-Neural_Clustering.ipynb.py
EPHYS4-Population_Clustering.ipynb.py
GenerateMLFilters.ipynb.py
GenerateMLFiltersJulie.ipynb.py
GenerateMLFiltersJuliePerZone.ipynb.py
GenerateMLFiltersPerZone.ipynb.py
GenerateReport.ipynb.py
GenerateReport2.ipynb.py
SpikeSortingStatisticsPart2.ipynb.py
SummaryStatistics.ipynb.py
gapEstimation.ipynb.py
plotConfusions.ipynb.py
plotConfusionsHerminaNW.ipynb.py
plotConfusionsJulie.ipynb.py
GenerateReport.ipynb.py:67:            pvalue = (1.0 - t.cdf(zscore*np.sqrt(row['nTrials']), row['nTrials']))*2.0
GenerateReport.ipynb.py:106:            pvalue = (1.0 - t.cdf(zscore*np.sqrt(row['nTrials']), row['nTrials']))*2.0
GenerateReport.ipynb.py:141:            pvalue = (1.0 - t.cdf(zscore*np.sqrt(nTotal), nTotal))*2.0
GenerateReport.ipynb.py:177:                                  'zcall', 'pcall', 'ncall'])
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && grep -n "linkage\|ttest\|def cluster_analysis\|fcluster\|n_neighbors\|UMAP(\|method=\|metric=\|log(" EPHYS4-Population_Clustering.ipynb.py EPHYS3-Neural_Clustering.ipynb.py EPHYS2-Population_Coding.ipynb.py EPHYS1-Generate_Dataframes.ipynb.py | cut -c1-230 | head -60
```

```
EPHYS4-Population_Clustering.ipynb.py:16:from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, fcluster
EPHYS4-Population_Clustering.ipynb.py:236:def cluster_analysis_short(db_sites):
EPHYS4-Population_Clustering.ipynb.py:521:clustered=linkage(umaps_neur[ind][has_wavs,:],method ='ward')
EPHYS4-Population_Clustering.ipynb.py:1291:    clustered=linkage(results[max_ari_ind][0][2],method ='ward')
EPHYS4-Population_Clustering.ipynb.py:1334:#These will be the features used to create linkages between the calls in the stimuli set or full bank
EPHYS4-Population_Clustering.ipynb.py:1510:aud_clust = linkage(Xallz,method='ward')
EPHYS4-Population_Clustering.ipynb.py:1522:    neu_clust = linkage(results[rand_ind][0][2][has_wavs],method='ward')
EPHYS4-Population_Clustering.ipynb.py:1695:aud_clust = linkage(aud_pcs,method='ward')
EPHYS4-Population_Clustering.ipynb.py:1697:aud_uclust = linkage(aud_umaps,method='ward')
EPHYS4-Population_Clustering.ipynb.py:1699:neu_clust = linkage(results[max_ari_ind][0][2][has_wavs],method='ward')
EPHYS4-Population_Clustering.ipynb.py:1724:clustered=linkage(results[max_ari_ind][0][2],method ='ward')
EPHYS4-Population_Clustering.ipynb.py:1746:    clustered=linkage(results[i][0][2][has_wavs],method ='ward')
EPHYS4-Population_Clustering.ipynb.py:1760:        F = fcluster(clustered, start_thresh + cl*delta, criterion='distance')
EPHYS3-Neural_Clustering.ipynb.py:21:from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, fcluster
EPHYS3-Neural_Clustering.ipynb.py:1008:    # Create linkage matrix and then plot the dendrogram
EPHYS3-Neural_Clustering.ipynb.py:1022:    linkage_matrix = np.column_stack([model.children_, model.distances_,
EPHYS3-Neural_Clustering.ipynb.py:1026:    dendrogram(linkage_matrix, **kwargs)
EPHYS2-Population_Coding.ipynb.py:238:um = umap.UMAP()
EPHYS2-Population_Coding.ipynb.py:434:    um = umap.UMAP()
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && awk '/^# OUT:/{skip=1} /^## \[/{skip=0} !skip' EPHYS4-Population_Clustering.ipynb.py | cut -c1-200 | grep -v "^\s*$" | grep -iv "plt\.\|ax\.\|color\|fig\|set_\|legend" | sed -n 120,520p
```

```
dbHermina = pd.read_pickle('../data/ephys_Germany/HerminaDatabase.')
## [code 8]
dbHermina.head()
## [code 9]
# this will be an example of doing this for one grouping just to see what we are dealin with
# first take a grouping near 95% pcc
pcen = np.percentile(pcc[1],95)
i_near=abs(pcc[3]-pcen).argmin()
grouping = groupings[3][i_near]
## [code 10]
pcc
## [code 11]
# Attempt to optimize code above
import multiprocessing,time
stims = np.unique(dbHermina.stim)  
identities_orig = [x.split('_')[0] for x in stims]
calltypes_orig = [x.split('_')[2] for x in stims]
n_pcs = 5
def cluster_analysis_short(db_sites):
    avg_responses = np.zeros((len(stims),len(db_sites)*(1+n_pcs)))
[... 382 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && grep -n "def cluster_analysis" *.py; f=$(grep -ln "def cluster_analysis(" *.py | head -1); n=$(grep -n "def cluster_analysis(" $f | head -1 | cut -d: -f1); sed -n "${n},$((n+90))p" $f | cut -c1-200; grep -n "ttest\|t(80)\|log10\|np.log" EPHYS4-Population_Clustering.ipynb.py | cut -c1-200 | head
```

```
Download_good_pkl_files.ipynb.py:236:def cluster_analysis(representation, labels, and_plot=False, use_umap=False, method='ward',criterion='distance',save=None):
EPHYS4-Population_Clustering.ipynb.py:236:def cluster_analysis_short(db_sites):
Supplementary_Calculations.ipynb.py:30:def cluster_analysis_short(db_sites):
def cluster_analysis(representation, labels, and_plot=False, use_umap=False, method='ward',criterion='distance',save=None):
    numcomps = min(20, representation.shape[1])
    nfiles = 5
    MesPCS = dict()
    if use_umap:
        MesPCS = umap.UMAP(
            ).fit_transform(representation[:,:])
    else:
        # first run PCA with a large amount of components
        pca = PCA(n_components=numcomps)
        pca.fit_transform(representation[:,:])
        #Find the number of components that represent 95% of variance
        nc = np.where(np.cumsum(pca.explained_variance_ratio_)>.95)[0][0]
        pca = PCA(n_components=nc)
        MesPCS=pca.fit_transform(representation[:,:])

    PCs4Linkage=MesPCS
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/encode && grep -n "outPath\|ttest\|t(\|nperm\|unitNamesFull) ==\|== 110\|1UnitPC" decodingCallTypesNaiveBayes.ipynb.py plotConfusions.ipynb.py decodingCallTypesNaiveBayesPart2AcousticClusters.ipynb.py | cut -c1-200 | head -40
```

```
decodingCallTypesNaiveBayes.ipynb.py:34:outPath = rootPath+dataPath+'HerminaDataBase.pkl'
decodingCallTypesNaiveBayes.ipynb.py:35:fileIn = open(outPath,"rb")
decodingCallTypesNaiveBayes.ipynb.py:77:nstimsUnit = dict()
decodingCallTypesNaiveBayes.ipynb.py:87:print(nunitsFull)
decodingCallTypesNaiveBayes.ipynb.py:104:    unitIndexDict = dict()
decodingCallTypesNaiveBayes.ipynb.py:111:        stimList.extend(list(dfDataBaseNW['stim'][unitIndex].array))
decodingCallTypesNaiveBayes.ipynb.py:134:                print('Stim ', stim, 'has no response for unit', unit, '. Skipping')
decodingCallTypesNaiveBayes.ipynb.py:196:    print('Total number of trials:', totTrials)
decodingCallTypesNaiveBayes.ipynb.py:197:    print('Total number of test trials:', totTestTrials)
decodingCallTypesNaiveBayes.ipynb.py:233:    clf.fit(Xfit,Yfit)
decodingCallTypesNaiveBayes.ipynb.py:254:    print('PCC %.0f %%' % (pcc))
decodingCallTypesNaiveBayes.ipynb.py:269:        ax.set(xticks=np.arange(nClasses),
decodingCallTypesNaiveBayes.ipynb.py:307:    outPath = rootPath+dataPath+'HerminaDataBase1UnitPCNW.pkl'
decodingCallTypesNaiveBayes.ipynb.py:308:    fileOut = open(outPath,"wb")
decodingCallTypesNaiveBayes.ipynb.py:448:ax.hist(pcc, bins = 30, range = (0,30))
decodingCallTypesNaiveBayes.ipynb.py:464:ax.set(xticks=np.arange(ncalls),
plotConfusions.ipynb.py:66:    print(unitNumber[ind[0]], np.mean(selHValList[ind[0]]))
plotConfusions.ipynb.py:90:            print('Error: Row', i, 'does not sum to 1')
plotConfusions.ipynb.py:100:        print('Error in info_matrix: input matrix sums to %f' % sump)
plotConfusions.ipynb.py:135:    fac = np.sqrt(unitNumber[i]/(unitNumber[i]-nUnit))
[... 21 more lines not kept]
```

**Agent**

I have what I need from the code. Now checking the claims file schema before writing.

**Agent calls Bash**

```bash
cd  sed -n 1,80p tools/claims_check.py; grep -l "elsewhere" claims/*.yaml | head -3; ls schemas 2>/dev/null; grep -rn "kind:" claims/*.yaml | awk '{print $NF}' | sort | uniq -c
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

[... 70 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s,indent=1)[:6000])"; grep -n "dataset:" -A3 claims/berg-2020.yaml | head; grep -n "elsewhere" -B2 -A6 claims/berg-2020.yaml | head -30
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
[... 215 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json;s=json.load(open('schemas/claims.schema.json'));print(json.dumps(s['\$defs'],indent=1)[:5000]); print(json.dumps(s['properties'].get('checks',{}),indent=1)[:500])"
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
[... 106 more lines not kept]
```

**Agent**

The paper is complete: version of record with STAR Methods and the supplement (SI Figs 1 to 11), and I've read the analysis code. Writing the claims file now.

**Agent calls Write**

```json
{
 "file_path": "claims/robotka-2023.yaml",
 "content": "# Claims for Robotka, Thomas, Yu, Wood, Elie, Gahr & Theunissen (2023), Cell Reports 42, 112034,\n# \"Sparse ensemble neural code for a complete vocal repertoire\", tested on CRCNS aa-5.\n#\n# Written by an agent (model \"claude-opus-5-5\", Claude Code, runner \"GitHub Actions\"), 2026-11-11,\n# protocol pilot-14 as stated in docs/protocol.md (Reader). The criteria were written from the\n# paper and its code alone; no data of the dataset were seen.\n#\n# Text read: the version of record (paper/10.1016-j.celrep.2023.112034.txt, extracted from the\n# publisher PDF), with its STAR Methods and the Supplemental information (SI Figures 1 to 11 and\n# their legends, which the PDF carries at its end). Table 1 was read from the text. Figures were\n# not opened; no claim needed a value only printed in a figure.\n#\n# Code read: github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit\n# f2d237639217425e7fc81d694708f19428a3b026 (v1.0 in the key resources table, zenodo 7378502). It\n# holds Jupyter notebooks with their printed outputs and decoders.py. GenerateReport.ipynb makes\n# the per-unit summary (auditory test, per-call-type z, selectivity index); GenerateDataBase.ipynb\n# makes the per-trial table (response strength z, the PCA of trial-averaged KDE responses and the\n# five PC weights per trial); decodingCallTypesNaiveBayes.ipynb and DataBaseMerge.ipynb run the\n# single-unit decoder; decodingCallTypesNaiveBayesPart2.ipynb and decoders.py run the ensemble\n# decoders; plotConfusions.ipynb makes Figure 4; GenerateMLFilters.ipynb makes the MRFs, the LDA,\n# the volume, the neural noise and the Figure 5 regressions (its printed outputs reproduce the\n# paper's F(1,79) = 8.975, 6.73, 8.75 and F(4,76) = 5.832); EPHYS4-Population_Clustering.ipynb\n# and Supplementary Calculations.ipynb make the Figure 6 clusterings. The acoustic clustering reads\n# a vocalization parameter table (vocParamTable.h5) and a stimulus segment table that are not in\n# the repository.\n#\n# Data the paper used (STAR Methods, Animals; Playback experiment and stimuli; Electrophysiology).\n# Awake data (this dataset, CRCNS aa-5, doi 10.6080/K0TT4P5Q). Four freely behaving adult zebra\n# finches, two pair-bonded couples, ZF4F, ZF5M, ZF6M and ZF7F, each implanted in the left\n# hemisphere with a 16-electrode array on a microdrive, recorded 4 to 8 h a day for 28 to 31 days\n# while the electrodes were lowered by 0.5 to 1 turn a day (a recording site is bird, depth in\n# turns, date and time). Stimuli were 110 distinct vocalizations of 10 call types (Be 12, LT 13,\n# Th 5, Di 5, Ag 9, Wh 13, Ne 15, Te 15, DC 14, So 9), each played 10 times per site in pseudo\n# random order with 3 to 6 s intervals. Spikes were sorted with a hierarchical, drift-tracking\n# sorter; units with spike SNR above 5 are the paper's units; 730 sorted units, of which 292\n# auditory. Measured variables per trial are spike times from 500 ms before to 4.5 s after\n# stimulus onset (the dataset's description), with the stimulus waveform and call-type label.\n# Units were assigned to CLM, CMM, Field L, NCM or the L/NCM border from histology and depth\n# (SI Figure 5). Anesthetized data (CRCNS aa-4, doi 10.6080/K00C4T06, Elie and Theunissen 2015,\n# 2019): six urethane-anesthetized birds, four (BlaBro09xxF, GreBlu9508M, WhiWhi4522M,\n# YelBlu6903F) used for decoding, 123 stimuli of 9 call types (no Wh). The claims on it are\n# `elsewhere`. The acoustic clustering uses the Theunissen lab vocalization database (3405 bouts\n# from 45 birds, 7920 to 8136 calls, Elie and Theunissen 2016); the paper gives no deposit for it.\n#\n# Common method, used by several criteria (C1 to C12). Where the Methods leave a choice open and\n# the code settles it, the code is followed and named; where they disagree, the Methods come first\n# and the code's choice is a variant.\n# C1 Units. A unit is a spike-sorted cluster with SNR above 5 (Results, Auditory units, paragraph\n#   1; Methods, Electrophysiology and spike sorting). It is auditory when a two-tailed one-sample\n#   t-test on its spike-count difference d (spikes in 0 to 500 ms after onset minus spikes in the\n#   500 ms before) over all trials of all stimuli gives p < 0.01 (SI Figure 2A legend). The code\n#   (GenerateReport.ipynb calc_zscore_all) computes t as mean(d)/sd(d) times sqrt(n) with n degrees\n#   of freedom; a standard one-sample t-test (n - 1 df) is the Methods reading and the code's is a\n#   variant.\n# C2 Response strength Z per trial. The Methods text reads as d z-scored with the mean and SD of d\n#   over all trials and stimuli of the unit (reading a). The code (GenerateDataBase.ipynb) divides d\n#   by its SD over all trials (numpy std, ddof 0) without subtracting the mean (reading b), which\n#   keeps Z relative to background as the Results describe. The decoder results do not depend on\n#   the reading (a Gaussian naive Bayes is unchanged by a shift of one feature). Only vocalization\n#   stimuli are used.\n# C3 Per-call-type Z and the selectivity index SI (Figure 3C, 3D). SI = (1 - mean(zCT)^2 /\n#   mean(zCT^2)) / (1 - 1/n) over the n = 10 call types (Methods, Response strength). zCT is read\n#   as (a) the mean of the trial Z of C2 over all trials of the call type (Methods), or (b) the\n#   code's zCT, mean(d)/sd(d, ddof 1) over the trials of the call type (GenerateReport.ipynb\n#   calc_zscore_category), which is what summarySel.pkl and the Figure 5F regressor use.\n# C4 Time-varying response T (Methods, PC analysis; GenerateDataBase.ipynb). For each unit and\n#   stimulus with at least 5 trials, the trial-averaged response is a Gaussian KDE of the spike\n#   times with a 30 ms kernel, sampled at 1 ms over the first 1000 samples of the stored KDE (the\n#   code's time base, which starts before stimulus onset; the stored tKDE fixes it). A PCA (sklearn)\n#   over all these responses of all auditory units gives the PCs; each trial's T1 to T5 are the\n#   projection of its spike train (1000 per spike at the sample of the spike) minus the PCA mean\n#   onto the first five PCs. The PCA is fitted separately for each dataset.\n# C5 Decoder (Methods, Naive Bayesian decoder). sklearn GaussianNB with uniform priors (code), on\n#   Z (code Z) or on Z with T1 to T5 per unit (code Z+T). Units used are those with responses to all\n#   110 stimuli and at least 2 trials of each (Methods; the code keeps units with 110 distinct\n#   stimuli). Cross-validation is open. Reading (a), the Methods: for each call type the trials of\n#   one exemplar stimulus are held out and tested, the decoder trained on the rest. Reading (b), the\n#   code (decoders.naiveBayes): one randomly chosen trial of every stimulus is held out and tested,\n#   the decoder trained on the remaining trials of all stimuli, and this is repeated (nperm = 100\n#   repetitions by default in decoders.py, used for the ensembles; one repetition in the\n#   single-unit notebook). For ensembles, training rows join the i-th trial of each unit to the\n#   same stimulus, with random redraws for units with fewer trials (code). The confusion matrix sums\n#   the posterior probabilities of the test trials by true call type. PCC is (a) the mean of the\n#   diagonal of the row-normalized matrix (Methods, Figure 4 legend) or (b) the trace of the summed\n#   matrix over the number of test trials (code). Chance is 10% (9 call types, 11.1%, without Wh).\n# C6 The 100 good units. Units with 110 stimuli whose single-unit PCC Z+T is above 12% (Results,\n#   Decoding call types, paragraph 2; Methods, Naive Bayesian decoder, paragraph 6; code\n#   decodingCallTypesNaiveBayesPart2.ipynb, pcc > 12).\n# C7 Ensembles. Ensembles are drawn from the 100 good units across birds and areas: all\n#   combinations of 1 and 2 units, 10,000 random draws for larger sizes (sizes 1, 2, 3, 4, 5, 10,\n#   15, 20 in the code), for the Figure 4B curve. For Figure 5, 1800 random 20-unit ensembles, each\n#   with 100 held-out repetitions (Methods). The paper's 1746 ensembles are those of the 1800 with\n#   PCC above 30% (GenerateMLFilters.ipynb, indGood = pcc > 30, printed sum 1746); the Methods do\n#   not state this filter. Readings, (a) the code's filter and (b) all 1800 ensembles.\n# C8 Ensemble-corrected statistics (Methods, Statistical analysis). With ns units sampled and\n#   ensembles of ne, neff = ns - ne + 1 (81 for ns = 100, ne = 20). Corrected variance s_c^2 =\n#   ns/(ns - ne) times the sample variance over ensembles; SEM = s_c/sqrt(neff). Two-sample t-tests\n#   use these SEMs with 2 neff - 2 df (t(160)); paired tests across ensembles use neff - 1 df\n#   (t(80)). Regression F = (neff/n)((SST - SSE)/(k - 1))/(SSE/(n - k)), with n ensembles, k model\n#   parameters including the intercept, and df (k - 1, neff - k) (F(1,79), F(4,76)). R2adj = 1 -\n#   (SSE/(n - k))/(SST/(n - 1)). The code (GenerateMLFilters.ipynb) implements these formulas.\n# C9 MPS and MRFs (Methods, Modulation receptive fields; GenerateMLFilters.ipynb). Stimulus MPS by\n#   soundsig BioSound (spectroCalc at 1 kHz sample rate, 50 Hz frequency spacing, 0 to 10 kHz;\n#   mpsCalc with a 100 ms window, Norm = True). The window of sound is the first 500 ms of the\n#   stimulus in the Methods; the code takes 500 ms before to 500 ms after onset (variant). Each MRF\n#   component of a unit is the sum over stimuli of (MPS minus the mean MPS over stimuli) weighted by\n#   the unit's trial-averaged Z (MRF-Z) or trial-averaged Tk (MRF-Tk), six components per unit. The\n#   code keeps temporal modulations from -50 to 50 Hz and spectral modulations from 0 to 4 cyc/kHz.\n# C10 LDA space and volume. Between covariance of the call-type mean MPS, within covariance the\n#   mean over call types of the covariance of single MPS about their call-type mean; the LDA axes\n#   are the eigenvectors of pinv(within) times between (code, rcond 1e-4). The Methods name the\n#   first three discriminant dimensions, read as the three of largest eigenvalue. The code calls\n#   numpy eigh and takes its first three columns, which eigh orders by ascending eigenvalue; this\n#   is a variant to be run as written. Each MRF component is projected on the three axes and divided\n#   by 110 times the SD of its response variable over all trials (code). The volume of an ensemble\n#   is the determinant of the 3x3 covariance of its 120 projected vectors (Methods); the\n#   regressions use its natural log (code).\n# C11 Ensemble regressors. Mean over the 20 units of SI (C3), of Entropy Selectivity (ES), and of\n#   neural noise. ES = 1 - H/log2(10) with H the entropy of the diagonal of the unit's single-unit\n#   Z+T confusion matrix; the code normalizes the diagonal to sum 1 before the entropy (reading a),\n#   the Methods formula uses the diagonal PCC values directly (reading b). Neural noise per unit is\n#   the variance of trial Z within each call type, averaged over the 10 call types (Results; code,\n#   numpy std ddof 0 squared); the Figure 5 legend says standard deviation (variant).\n# C12 Neural clustering (Methods, Hierarchical clustering of neural ensemble activity;\n#   EPHYS4-Population_Clustering.ipynb). For an ensemble, a stimulus by (units x 6) matrix of\n#   trial-averaged Z and T1 to T5. The code embeds it with UMAP (default parameters, 2 dimensions)\n#   and builds a Ward linkage; the Methods name hierarchical agglomerative clustering only. Readings,\n#   (a) UMAP then Ward (code), (b) Ward on the averaged responses. The tree is cut at 499 evenly\n#   spaced distance thresholds between its smallest and largest linkage distance (code) and the cut\n#   with maximal ARI against the labels is kept, giving ARIcall or ARIacoustic and the optimal\n#   number of clusters. ARIacoustic is computed on the stimuli that have an acoustic label.\n# Random draws (ensembles, held-out trials, UMAP) use any seed; a seed is a standard choice that\n# should not change an outcome judged on averages over many ensembles.\nschema_version: 2\npaper: doi:10.1016/j.celrep.2023.112034\nclaims:\n- id: stimulus-set-link\n  kind: link\n  statement: The dataset holds the awake playback experiment the paper describes, four birds\n    (ZF4F, ZF5M, ZF6M, ZF7F) and 110 distinct stimuli labelled with the 10 call types in the\n    paper's numbers.\n  source: STAR Methods, Playback experiment and stimuli, paragraph 3; Animals, paragraph 2\n  quote: For the awake dataset we used 110 distinct stimuli sampling 10 call-types (Begging or Be\n    12; Long-Tonal or LT 13; Thuk or Th 5\n  expected:\n  - quantity: distinct stimuli\n    value: 110\n    tolerance: 0\n  - quantity: birds\n    value: 4\n    tolerance: 0\n  criterion: Count the distinct stimulus files and their call-type labels over all units, and the\n    birds. Reproduced when there are 4 birds and the stimulus counts per call type are Be 12, LT 13,\n    Th 5, Di 5, Ag 9, Wh 13, Ne 15, Te 15, DC 14 and So 9 (110 in all); partially reproduced when\n    the total is 110 but up to two call-type counts differ by one (a label variant such as Tu for\n    Th); not reproduced otherwise.\n- id: auditory-units\n  statement: Of 730 spike-sorted units in the awake dataset, 292 (40.1%) were auditory.\n  source: STAR Methods, Electrophysiology and spike sorting, last paragraph; SI Figure 2A legend\n  quote: In the awake dataset, we recorded the activity of 730 spike-sorted units of which 292 were\n    classified as auditory (40.1%).\n  expected:\n  - quantity: spike-sorted units (SNR above 5)\n    value: 730\n    tolerance: 73\n  - quantity: auditory units\n    value: 292\n    tolerance: 29.2\n  - quantity: auditory fraction\n    value: 40.1\n    tolerance: 4.01\n    unit: percent\n  criterion: Units and the auditory test as in C1. The dataset may hold only part of the sorted\n    units (the descriptor says pickle files are for units); the readings of the denominator are\n    (a) all units the dataset holds with SNR above 5, (b) all units the dataset holds. Reproduced\n    when the auditory count is within tolerance and, under one reading, the total and the fraction\n    are; partially reproduced when only the auditory count is.\n- id: inhibited-units\n  statement: In the awake dataset 46 of the 292 auditory units (15.7%) were inhibited by sound.\n  source: SI Figure 2A legend\n  quote: In the awake dataset (4 birds), 292 units had z scores that were significantly different\n    from zero and 46/292 (15.7 %) that were inhibited by sounds.\n  depends_on:\n  - auditory-units\n  expected:\n  - quantity: inhibited auditory units\n    value: 46\n    tolerance: 4.6\n  - quantity: inhibited fraction of auditory units\n    value: 15.7\n    tolerance: 1.57\n    unit: percent\n  criterion: Auditory units as in C1; a unit is inhibited when its mean spike-count difference d\n    over all trials is negative (code, zAud < 0). Reproduced when both values are within tolerance.\n- id: fig3c-peak-call-types\n  statement: Across the 292 auditory units, distress calls had the highest average response\n    strength followed by song; 51 units had their peak response to distress calls and 61 to song;\n    the preference is biased toward the longer calls (Ag, Be, So, Di).\n  source: Figure 3C legend; Results, Auditory units have heterogeneous and selective responses,\n    paragraph 2\n  quote: distress calls (Di) had the highest average response strength followed by song (So), etc.\n    ... 51 units had the peak responses for distress call, 61 for song, etc.\n  depends_on:\n  - auditory-units\n  expected:\n  - quantity: units with peak Z for Di\n    value: 51\n    tolerance: 5.1\n  - quantity: units with peak Z for So\n    value: 61\n    tolerance: 6.1\n  criterion: Per-call-type Z of each auditory unit under the two readings of C3 (zCT). The call\n    types are ranked by their mean zCT over units. Reproduced when, under one reading, Di ranks\n    first and So second, both peak counts are within tolerance, and Ag, Be, So and Di are four of\n    the five call types with the most peak units; partially reproduced when Di and So are the two\n    highest ranked but a count is outside tolerance.\n- id: fig4a-unit-z-vs-zt\n  statement: For single units decoded independently, adding the temporal pattern (Z + T) to the\n    response strength (Z) raises the mean PCC from 10.78% to 12.3% (a 14% increase), over 191 units\n    with data for all 110 calls.\n  source: Results, Decoding call types from ensemble responses, paragraph 1; Figure 4A\n  quote: 'mean percentage of correct classification [PCC] ... PCCZ = 10.78%; PCCZ+T = 12.3%; 14%\n    increase; t(190) = 10.06'\n  statistics:\n  - test: t-test (paired across units, as the 190 df imply)\n    statistic: t(190) = 10.06\n    p: 0.00001\n    p_relation: <\n    n: 191 units with data for all 110 calls\n  depends_on:\n  - auditory-units\n  expected:\n  - quantity: units decoded\n    value: 191\n    tolerance: 19.1\n  - quantity: mean single-unit PCC with Z\n    value: 10.78\n    tolerance: 1.078\n    unit: percent\n  - quantity: mean single-unit PCC with Z+T\n    value: 12.3\n    tolerance: 1.23\n    unit: percent\n  criterion: Decoder and units as in C5, each auditory unit decoded alone with Z and with Z+T,\n    under the readings of C5 for cross-validation and PCC (reading b run with one repetition, as\n    the single-unit notebook, and with 100). Reproduced when, under one reading, both means are\n    within tolerance, Z+T exceeds Z, and a paired t-test across units gives p < 1e-5; partially\n    reproduced when Z+T is significantly higher but a mean is outside tolerance.\n- id: good-units-100\n  statement: Exactly 100 units had a single-unit PCC Z+T above 12%, and they came from all four\n    birds (ZF4F 43, ZF5M 19, ZF6M 16, ZF7F 22).\n  source: Results, Decoding call types from ensemble responses, paragraph 2; STAR Methods, Naive\n    Bayesian decoder, paragraph 6\n  quote: The number of units that satisfied that requirement is exactly n = 100.\n  depends_on:\n  - fig4a-unit-z-vs-zt\n  expected:\n  - quantity: units with single-unit PCC Z+T above 12%\n    value: 100\n    tolerance: 10\n  - quantity: good units in ZF4F\n    value: 43\n    tolerance: 4.3\n  - quantity: good units in ZF5M\n    value: 19\n    tolerance: 1.9\n  - quantity: good units in ZF6M\n    value: 16\n    tolerance: 1.6\n  - quantity: good units in ZF7F\n    value: 22\n    tolerance: 2.2\n  criterion: C6, under the readings of C5. Because each held-out draw is random, a unit near 12%\n    can fall either side; the count is taken as the mean over 10 runs of the single-unit decoder.\n    Reproduced when the total is within tolerance and every bird contributes units; the per-bird\n    counts are reported and judged within tolerance as a second part (partially reproduced when the\n    total holds and two or more birds are outside tolerance).\n- id: fig4b-ensemble-20\n  statement: Ensemble decoding performance rises with ensemble size, reaching an average PCC Z+T\n    of 42% for 20 units, above the 29.6% obtained from response strength alone (Z), a 43% increase.\n  source: Results, Decoding call types from ensemble responses, paragraph 2; Figure 4B\n  quote: as the ensemble size grew, the neuronal decoding performance using both the strength and\n    the temporal patterns of the response (Z + T) increases, reaching average levels of 42% for 20\n    neurons ... (mean PCCZ = 29.6%; mean PCCZ+T = 42.3%; 43% increase; t(160) = 8.83\n  statistics:\n  - about: PCC Z+T against PCC Z for ensembles of 20 units\n    test: t-test with ensemble-corrected standard errors and df\n    statistic: t(160) = 8.83\n    p: 0.00001\n    p_relation: <\n    n: 10,000 ensembles of 20 units sampled from 100 units\n  depends_on:\n  - good-units-100\n  expected:\n  - quantity: mean PCC Z+T, ensembles of 20\n    value: 42.3\n    tolerance: 4.23\n    unit: percent\n  - quantity: mean PCC Z, ensembles of 20\n    value: 29.6\n    tolerance: 2.96\n    unit: percent\n  criterion: Ensembles as in C7 (Figure 4B sampling) from the good units, decoded as in C5 under\n    its readings, with Z and with Z+T. Reproduced when, under one reading, both means are within\n    tolerance, mean PCC Z+T increases with each step of ensemble size from 1 to 20, and the C8\n    two-sample t-test (df 160) of Z+T against Z gives p < 1e-5; partially reproduced when the\n    increase and the test hold but a mean is outside tolerance.\n- id: fig4b-top-ensembles\n  statement: The top 10% of ensembles of 20 units reach an average PCC Z+T of about 50%, and the\n    best ensembles approach the 65% achieved by acoustic classifiers.\n  source: Results, Decoding call types from ensemble responses, paragraph 2; Figure 4B legend\n  quote: The top 10% of the neuronal ensembles of size 20 reach an average PCCZ+T of �50% (Figure\n    4B) and the best ensembles (e.g., Figure 5A) reach values close to the optimal performance of\n    65%\n  depends_on:\n  - fig4b-ensemble-20\n  expected:\n  - quantity: mean PCC Z+T of the top ensembles of 20\n    value: 50\n    tolerance: 5\n    unit: percent\n  criterion: The Results and Figure 4 legend say top 10%; the Methods say top 5%, re-estimated with\n    a second random held-out draw to remove the selection bias. Readings, (a) top 10% and (b) top\n    5%, each re-estimated by a second held-out draw as the Methods describe, among the Figure 4B\n    ensembles of 20. Reproduced when, under one reading, the mean is within tolerance and the best\n    ensemble's PCC Z+T is at least 55% (close to 65%, read as within 10 points); partially\n    reproduced when only the mean holds.\n- id: fig4b-confusions\n  statement: Most ensemble misclassifications are systematic, Ne confused with Te, LT with Be, Th\n    (Tu) with Te, and Di with Ag.\n  source: Results, Decoding call types from ensemble responses, paragraph 3; Figure 4B\n  quote: 'most misclassifications originated from the same systematic errors: the soft Ne call is\n    often confused with the soft contact Te call; the juvenile LT call with the Be call; the alarm\n    Tu call with the Te call; and the Di call with the Ag call.'\n  depends_on:\n  - fig4b-ensemble-20\n  criterion: The average row-normalized confusion matrix of the ensembles of 20 (C5, C7). For each\n    named pair (true Ne predicted Te, LT as Be, Th as Te, Di as Ag) the off-diagonal entry is\n    compared with the other off-diagonal entries of its row. Reproduced when all four are the\n    largest or second largest off-diagonal entry of their row; partially reproduced for two or\n    three of them; not reproduced for fewer.\n- id: figs4-per-bird-and-sex\n  statement: Decoding performance and its systematic errors are similar in every bird decoded\n    alone, and PCC does not differ significantly between female and male birds (difference 8.3%).\n  source: SI Figure 4 legend; Results, Decoding call types from ensemble responses, paragraph 4\n  quote: 'We did not measure any significant differences in PCC between sexes (Awake: Diff PCC\n    Female - Male = 8.3%, t(2)= 0.6757 p= 0.5689'\n  statistics:\n  - about: female against male PCC, awake\n    test: t-test\n    statistic: t(2) = 0.6757\n    p: 0.5689\n    n: 2 female and 2 male birds\n  depends_on:\n  - good-units-100\n  expected:\n  - quantity: female minus male PCC, awake\n    value: 8.3\n    tolerance: 0.83\n    unit: percent\n  criterion: Ensembles drawn within one bird at a time from its good units (C6), decoded as in C5,\n    at size 15 for the confusion matrices (SI Figure 4A). A claim of absence for sex, judged on the\n    paper's test, a two-sample t-test with 2 df on the four birds' mean PCC (two per sex) at the\n    ensemble size the legend's panels C use, read as 15 units (the largest size every bird allows\n    with 16 units in ZF6M); reproduced when p >= 0.05, with the difference reported. The\n    per-bird similarity is reported (each bird's PCC curve and whether the four Figure 4B error\n    pairs are among the two largest off-diagonal entries in each bird).\n- id: figs6-primary-vs-secondary\n  statement: In the awake data, ensemble decoding as a function of size is very similar in primary\n    (Field L/CLM, 56 units) and secondary (NCM/CMM, 38 units) auditory pallium; at 20 units the\n    difference is small but significant at the 5% level, while response rate and coding efficiency\n    do not differ.\n  source: SI Figure 6 legend; Results, Decoding call types from ensemble responses, paragraph 4\n  quote: For ensembles of size 20, the measured differences were small and statistically\n    significant at the 5% level in the awake dataset (d= 0.72, t(54)= 2.55, p= 0.013)\n  statistics:\n  - about: PCC at 20 units, primary against secondary\n    test: t-test, ensemble corrected\n    statistic: d = 0.72, t(54) = 2.55\n    p: 0.013\n  - about: summed response rate at 20 units, primary against secondary\n    test: t-test, ensemble corrected\n    statistic: d = -0.006, t(54) = -0.026\n    p: 0.98\n  - about: PCC per unit rate (efficiency), primary against secondary\n    test: t-test, ensemble corrected\n    statistic: d = 0.51, t(54) = 1.81\n    p: 0.076\n  depends_on:\n  - good-units-100\n  expected:\n  - quantity: good units in the primary auditory pallium\n    value: 56\n    tolerance: 5.6\n  - quantity: good units in the secondary auditory pallium\n    value: 38\n    tolerance: 3.8\n  - quantity: effect size d, PCC at 20 units\n    value: 0.72\n    tolerance: 0.072\n  criterion: Areas from the unit assignment of SI Figure 5 (border L/NCM units excluded). Ensembles\n    drawn within each area from its good units, decoded as in C5. Tests as C8 with neff = 37 and\n    19 (df 54). Reproduced when the PCC test gives p < 0.05 and the rate and efficiency tests give\n    p >= 0.05 (the absence claims, judged on the same test), with d reported; partially reproduced\n    when the rate and efficiency absences hold but the PCC difference is not significant. If the\n    dataset does not hold the area of each unit, the claim cannot be tested.\n- id: fig5e-volume\n  statement: Across random ensembles of 20 units, PCC increases with the volume the ensemble's MRF\n    components span in the 3D LDA space of call types (R2adj = 0.1).\n  source: Results, Modulation receptive fields of single neurons and ensemble decoding performance,\n    paragraph 4; Figure 5E legend\n  quote: Supporting this hypothesis, we find that, as the volume span increases the PCC increases\n    (Figure 5E, R2 adj = 0.1, p = 0.0036\n  statistics:\n  - test: F-test of a bivariate regression, ensemble corrected\n    statistic: F(1,79) = 8.975\n    p: 0.0036\n    n: 1,746 ensembles of 20 units sampled from 100 units\n  depends_on:\n  - good-units-100\n  expected:\n  - quantity: R2adj, PCC on volume\n    value: 0.1\n    tolerance: 0.01\n  - quantity: ensembles in the regression\n    value: 1746\n    tolerance: 174.6\n  criterion: Ensembles of 20 as in C7 (Figure 5 sampling) with PCC Z+T from C5 under its readings;\n    volume as C9 and C10 with all six MRF components of the 20 units; regression of PCC on log\n    volume (code), F and R2adj as C8. Readings of C7 (a, b), C9 (sound window) and C10 (LDA axes)\n    are each run. Reproduced when, under one reading, the slope is positive, R2adj is within\n    tolerance and the corrected F-test gives p < 0.05; partially reproduced when the slope is\n    positive and significant but R2adj is outside tolerance.\n- id: fig5f-si-unrelated\n  statement: The average Z-based selectivity index of the units in an ensemble is not related to\n    the ensemble's decoding performance.\n  source: Results, Modulation receptive fields of single neurons and ensemble decoding performance,\n    paragraph 5; Figure 5F\n  quote: Surprisingly, the average Z-based selectivity index (average across the 20 units in each\n    ensemble) is not related to the ensemble decoder performance (Figure 5F)\n  depends_on:\n  - fig5e-volume\n  criterion: A claim of absence, judged on the paper's test, the ensemble-corrected F-test (C8) of\n    the bivariate regression of PCC on the ensemble mean SI (C3, C11) over the Figure 5 ensembles\n    (C7). Reproduced when p >= 0.05; not reproduced when p < 0.05. R2adj and the slope are reported\n    (the code printed R2adj = -0.0006, p = 0.99). The SI readings of C3 are shown, the code's (b)\n    as the paper's test.\n- id: fig5g-entropy-selectivity\n  statement: The ensemble average Entropy Selectivity of its units is negatively correlated with\n    ensemble decoding performance.\n  source: Results, Modulation receptive fields of single neurons and ensemble decoding performance,\n    paragraph 5; Figure 5G legend\n  quote: whereas the unit average entropy selectivity is negatively correlated (Figure 5G)\n  statistics:\n  - test: F-test of a bivariate regression, ensemble corrected\n    statistic: F(1,79) = 6.73\n    p: 0.011\n    n: 1,746 ensembles of 20 units\n  depends_on:\n  - fig5e-volume\n  criterion: Regression of PCC on the ensemble mean ES (C11, both readings) over the Figure 5\n    ensembles (C7), F as C8. Reproduced when, under one reading, the slope is negative and p <\n    0.05; the code printed R2adj = 0.076.\n- id: fig5h-neural-noise\n  statement: As neural variability within call types (neural noise plus lack of invariance)\n    increases, ensemble decoding performance decreases (R2adj = 0.1).\n  source: Results, Modulation receptive fields of single neurons and ensemble decoding performance,\n    paragraph 6; Figure 5H legend\n  quote: As shown in Figure 5H, as neural variability (neural noise + lack of invariance within call\n    type) increases, the decoder performance decreases (R2 adj = 0.1, p = 0.004)\n  statistics:\n  - test: F-test of a bivariate regression, ensemble corrected\n    statistic: F(1,79) = 8.75\n    p: 0.004\n    n: 1,746 ensembles of 20 units\n  depends_on:\n  - fig5e-volume\n  expected:\n  - quantity: R2adj, PCC on neural noise\n    value: 0.1\n    tolerance: 0.01\n  criterion: Regression of PCC on the ensemble mean neural noise (C11, variance and SD readings)\n    over the Figure 5 ensembles (C7), F and R2adj as C8. Reproduced when, under one reading, the\n    slope is negative, R2adj is within tolerance and p < 0.05; partially reproduced when the slope\n    is negative and significant but R2adj is outside tolerance.\n- id: fig5-multiple-regression\n  statement: A linear model of PCC on volume spanned, neural variability and the two selectivity\n    measures together explains R2adj = 0.22 of the variance of ensemble decoding performance.\n  source: Results, Modulation receptive fields of single neurons and ensemble decoding performance,\n    paragraph 7\n  quote: When all four regressors are taken into account (i.e., volume spanned, neural variability,\n    and the two measures of selectivity) in a linear model to predict PCC, one obtains a\n    coefficient of determination (R2 adj) of 0.22 (F(4,76) = 5.832, p = 0.00038)\n  statistics:\n  - test: F-test of a multiple linear regression, ensemble corrected\n    statistic: F(4,76) = 5.832\n    p: 0.00038\n    n: 1,746 ensembles of 20 units\n  depends_on:\n  - fig5e-volume\n  expected:\n  - quantity: R2adj, PCC on the four regressors\n    value: 0.22\n    tolerance: 0.022\n  criterion: Ordinary least squares of PCC on neural noise, log volume, mean ES and mean SI (the\n    code's regressors, GenerateMLFilters.ipynb) over the Figure 5 ensembles (C7); R2adj and F as C8\n    with k = 5. Reproduced when, under one reading, R2adj is within tolerance and p < 0.05;\n    partially reproduced when p < 0.05 and R2adj is outside tolerance.\n- id: pcs-variance\n  statement: The first five principal components of the time-varying responses explain about 90%\n    of their variance.\n  source: STAR Methods, PC analysis; SI Figure 7A legend\n  quote: The first 5 PCs explained �90% of the variance as shown in SI Figure S7.\n  depends_on:\n  - auditory-units\n  expected:\n  - quantity: variance explained by the first 5 PCs, awake\n    value: 90\n    tolerance: 9\n    unit: percent\n  criterion: PCA as C4 over the auditory units of the awake dataset. Reproduced when the cumulative\n    explained variance ratio of the first five PCs is within tolerance (the code printed 0.922).\n- id: table1-snr\n  statement: The awake units have a mean spike SNR of 7.42 (SD 2.52; quartiles 5.51, 6.50, 9.03).\n  source: Table 1, awake behaving dataset\n  inferred: The values are in Table 1 only; no sentence states them. Read from the table's SNR\n    column for the awake behaving dataset.\n  expected:\n  - quantity: mean SNR\n    value: 7.42\n    tolerance: 0.742\n  - quantity: median SNR\n    value: 6.5\n    tolerance: 0.65\n  criterion: SNR is the stored unit SNR (peak-to-trough of the mean snippet over the mean snippet\n    rms, Methods, Electrophysiology and spike sorting). Table 1 does not say over which units; the\n    readings are (a) the 292 auditory units and (b) all units with SNR above 5. Reproduced when,\n    under one reading, mean and median are within tolerance. The refractory-period indices Qisi and\n    Qacc need the full spike trains, which the dataset does not hold (spikes are kept only around\n    stimuli), and are not claimed.\n- id: figs5-region-anova\n  statement: Of the 100 good units, 16 were in CLM, 25 in CMM, 40 in Field L, 13 in NCM and 6 at\n    the L/NCM border; region has only small effects on decoder performance, mean rate and Entropy\n    Selectivity, and none on SI; after Bonferroni correction only Entropy Selectivity differs.\n  source: SI Figure 5 legend\n  quote: An ANOVA with anatomical region as the predictor suggested small differences across\n    regions in decoder performance (Radj2= 0.059, F(4,95) = 2.558, p=0.0436), mean rate across\n    regions (Radj2 = 0.084, F(4,95) = 2.7, p = 0.0351) and in Entropy Selectivity (Radj2 = 0.09, F(4,\n    95) = 3.54, p= 0.00965) but not SI\n  statistics:\n  - about: decoder performance by region\n    test: one-way ANOVA\n    statistic: F(4,95) = 2.558\n    p: 0.0436\n  - about: mean rate by region\n    test: one-way ANOVA\n    statistic: F(4,95) = 2.7\n    p: 0.0351\n  - about: Entropy Selectivity by region\n    test: one-way ANOVA\n    statistic: F(4,95) = 3.54\n    p: 0.00965\n    corrected: Bonferroni over four tests\n  - about: SI by region\n    test: one-way ANOVA\n    statistic: F(4,95) = 1.9\n    p: 0.102\n  depends_on:\n  - good-units-100\n  expected:\n  - quantity: good units in Field L\n    value: 40\n    tolerance: 4\n  - quantity: good units in CMM\n    value: 25\n    tolerance: 2.5\n  - quantity: good units in CLM\n    value: 16\n    tolerance: 1.6\n  - quantity: good units in NCM\n    value: 13\n    tolerance: 1.3\n  criterion: Regions as assigned by the paper (the dataset's unit metadata, if it has them). One-way\n    ANOVA with five regions over the 100 good units, of single-unit PCC Z+T, mean rate, ES and SI\n    (C3, C11). Reproduced when the counts are within tolerance and only ES has p < 0.0125 (0.05 over\n    four tests) while SI has p >= 0.05; partially reproduced when the ES result holds and the\n    counts do not. Not testable when the dataset holds no region per unit.\n- id: fig6a-acoustic-clusters\n  statement: Hierarchical clustering of the acoustic features of the vocalization database (without\n    song) matches the ethogram-based call types with a best ARI of 0.7 at six clusters, and 0.49\n    at nine clusters.\n  source: Results, Neural categories for ethogram-based call types versus acoustical clusters,\n    paragraph 2; Figure 6A\n  quote: The best adjusted Rand index (ARI), that quantifies the correlation between the labels\n    given by the cut of the hierarchical tree and the ethogram-based call types is 0.7, with the\n    optimal cut generating six clusters, and 0.49 with the tree cut generating nine clusters.\n  data: with_inputs\n  expected:\n  - quantity: best ARI, acoustic clusters against call types\n    value: 0.7\n    tolerance: 0.07\n  - quantity: clusters at the best cut\n    value: 6\n    tolerance: 0\n  - quantity: ARI at the 9-cluster cut\n    value: 0.49\n    tolerance: 0.049\n  criterion: Uses the lab's vocalization database (4,987 calls of 9 call types without song in\n    Figure 6A; Elie and Theunissen 2016), which the dataset does not hold and the paper gives no\n    deposit for. The 20 acoustic features of Methods, Acoustic feature space, z-scored, embedded by\n    UMAP in 20 dimensions, Ward linkage (code), ARI at every cut. Reproduced when both ARIs are within\n    tolerance and the best cut has six clusters. Blocked when the database cannot be obtained.\n- id: acoustic-labels-decoding\n  statement: Ensembles of 20 units classify vocalizations by acoustic cluster labels with PCC Z+T\n    of only 38.0%, below the 42.3% for ethogram-based call types.\n  source: Results, Neural categories for ethogram-based call types versus acoustical clusters,\n    paragraph 3\n  quote: The neuronal decoding performance (PCCZ+T) reaches only 38.0% for acoustic clusters, below\n    the 42.3% performance previously found for call types (t(160) = 2.71, p = 0.0074).\n  statistics:\n  - test: t-test, ensemble corrected\n    statistic: t(160) = 2.71\n    p: 0.0074\n    n: 1,746 ensembles of 20 units sampled from the same 100 units\n  data: with_inputs\n  depends_on:\n  - fig6a-acoustic-clusters\n  - fig4b-ensemble-20\n  expected:\n  - quantity: mean PCC Z+T with acoustic labels, ensembles of 20\n    value: 38.0\n    tolerance: 3.8\n    unit: percent\n  criterion: Each stimulus labelled by its acoustic cluster (the 9-cluster cut of\n    fig6a-acoustic-clusters, songs as a 10th label); decoder and ensembles as C5 and C7 under their\n    readings. Reproduced when, under one reading, the mean is within tolerance and below the\n    call-type PCC of the same ensembles with p < 0.05 by the C8 t-test (df 160).\n- id: fig6c-number-of-clusters\n  statement: The optimal number of neural clusters varies from 1 to 30 across ensembles, but its\n    mean and median are close to the number of call types whether call types (mean 10.83, median\n    9) or acoustic labels (mean 10.03, median 9) are the reference, with no significant difference\n    between the two.\n  source: Results, Neural categories for ethogram-based call types versus acoustical clusters,\n    paragraph 4; Figure 6C bottom\n  quote: (range 1-30 clusters), both the median and the average number of clusters are very close\n    to the number of ethogram-based call types irrespective if the acoustic labels or the call types\n    are used as labels (call types, mean = 10.83, median = 9; acoustic labels, mean = 10.03, median =\n    9; paired t test on log transformed data t(80) = �0.808, p = 0.21)\n  statistics:\n  - test: paired t-test on log-transformed cluster numbers, ensemble corrected\n    statistic: t(80) = -0.808\n    p: 0.21\n    n: random ensembles of 20 units (10,000 in the Figure 6C legend)\n  data: with_inputs\n  depends_on:\n  - fig6a-acoustic-clusters\n  expected:\n  - quantity: mean optimal clusters, call-type labels\n    value: 10.83\n    tolerance: 1.083\n  - quantity: median optimal clusters, call-type labels\n    value: 9\n    tolerance: 0.9\n  - quantity: mean optimal clusters, acoustic labels\n    value: 10.03\n    tolerance: 1.003\n  - quantity: median optimal clusters, acoustic labels\n    value: 9\n    tolerance: 0.9\n  criterion: Neural clustering as C12 under its readings, on random ensembles of 20 good units (C7;\n    the legend's 10,000 ensembles, or the 1,746 of Figure 5 as a variant). The call-type values use\n    the dataset alone and are judged on their own. The absence is judged on the paper's test, a\n    paired t-test on log cluster numbers with df 80 (C8); p = 0.21 at t = -0.808 with 80 df is a\n    one-sided value, so the test is one-sided as printed and the two-sided p is shown. Reproduced\n    when, under one reading, the four values are within tolerance and p >= 0.05; partially\n    reproduced when only the call-type values and the absence hold.\n- id: fig6c-ari-call-over-acoustic\n  statement: In the large majority of sampled ensembles the neural clustering matches the call-type\n    labels better than the acoustic labels.\n  source: Results, Neural categories for ethogram-based call types versus acoustical clusters,\n    paragraph 4; Figures 6B and 6C top\n  quote: in the large majority of all sampled ensembles, there is a better match between the neural\n    clustering with the call type labels than with the acoustic labels (Figures 6B and 6C, top,\n    paired t test t(80) = 5.144\n  statistics:\n  - test: paired t-test, ensemble corrected\n    statistic: t(80) = 5.144\n    p: 0.00001\n    p_relation: <\n  data: with_inputs\n  depends_on:\n  - fig6a-acoustic-clusters\n  criterion: ARIcall and ARIacoustic per ensemble as C12 under its readings. Reproduced when, under\n    one reading, ARIcall exceeds ARIacoustic in more than half of the ensembles (the large majority,\n    read as at least 75%) and the C8 paired t-test (df 80) gives p < 1e-5; partially reproduced\n    when the test holds and the share is between 50% and 75%.\n- id: figs10-ensemble-size\n  statement: The advantage of call-type labels over acoustic labels in matching neural clusters\n    grows with ensemble size.\n  source: SI Figure 10 legend; Results, Neural categories, paragraph 4\n  quote: The differences in ARI is positive and increases with ensemble size, indicating an\n    increased greater match of neural clusters with call-types as compared to acoustic labels.\n  data: with_inputs\n  depends_on:\n  - fig6c-ari-call-over-acoustic\n  criterion: Mean ARIcall minus ARIacoustic (C12) for ensembles of 1, 2, 3, 4, 5, 10 and 20 good\n    units (the code's sizes). Reproduced when the mean difference is positive at every size from 2\n    up and its Spearman correlation with size is positive (p < 0.05 over the sizes, or a\n    monotone rise); partially reproduced when it is positive at 20 units but does not rise.\n- id: anesth-auditory-units\n  statement: In the anesthetized dataset 607 of 1207 spike-sorted units (50%) were auditory, and\n    13 of 609 auditory units (2.1%) were inhibited by sound.\n  source: STAR Methods, Electrophysiology and spike sorting, last paragraph; SI Figure 2A legend\n  quote: In the anesthetized dataset 607 out of a total of 1207 spike-sorted units (50%) were\n    classified as auditory using the same criterion\n  data: elsewhere\n  where: CRCNS aa-4, doi 10.6080/K00C4T06\n  expected:\n  - quantity: auditory units, anesthetized\n    value: 607\n    tolerance: 60.7\n  - quantity: inhibited auditory units, anesthetized\n    value: 13\n    tolerance: 1.3\n  criterion: C1 on the anesthetized units. The paper prints 607 in the Methods and 609 in SI Figure\n    2; either count within tolerance holds. Reproduced when both values are within tolerance.\n- id: anesth-decoding-better\n  statement: Ensemble decoding is slightly better in the anesthetized dataset, which has a higher\n    response SNR, with systematic errors that overlap those of the awake data.\n  source: Results, Decoding call types from ensemble responses, paragraph 2; SI Figures 4 and 8\n  quote: The average decoding performance in the anesthetized dataset is slightly better (Figure\n    S8).\n  data: elsewhere\n  where: CRCNS aa-4, doi 10.6080/K00C4T06\n  depends_on:\n  - fig4b-ensemble-20\n  criterion: Anesthetized good units are those with 100 or more common stimuli of 9 call types and\n    single-unit PCC above 13% (n = 375, Methods). Mean PCC Z+T of ensembles of 20 (C5, C7) in both\n    datasets on the 9 call types without Wh (SI Figure 4C, D). Reproduced when the anesthetized\n    mean exceeds the awake mean on 9 call types and at least two of the four error pairs of\n    fig4b-confusions are among the two largest off-diagonal entries of their rows in both.\n- id: anesth-regressions\n  statement: In the anesthetized dataset, volume spanned explains R2adj = 0.48 of decoder\n    performance, neural variability 0.38, and both with the two selectivity measures 0.55.\n  source: Results, Modulation receptive fields of single neurons and ensemble decoding performance,\n    paragraph 7; SI Figure 8E to 8H\n  quote: In the anesthetized dataset, the effect size (i.e., explained variance of PCC of call type)\n    for the volume spanned by the MRF vectors is R2 adj = 0.48 (F(1,343) = 314.8, p < 10\n  statistics:\n  - about: PCC on volume\n    test: F-test, ensemble corrected\n    statistic: F(1,343) = 314.8\n    p: 0.00001\n    p_relation: <\n  - about: PCC on neural variability\n    test: F-test, ensemble corrected\n    statistic: F(1,343) = 209.5\n    p: 0.00001\n    p_relation: <\n  - about: PCC on all regressors\n    test: F-test, ensemble corrected\n    statistic: F(2,341) = 215.0\n    p: 0.00001\n    p_relation: <\n  data: elsewhere\n  where: CRCNS aa-4, doi 10.6080/K00C4T06\n  expected:\n  - quantity: R2adj, volume, anesthetized\n    value: 0.48\n    tolerance: 0.048\n  - quantity: R2adj, neural variability, anesthetized\n    value: 0.38\n    tolerance: 0.038\n  - quantity: R2adj, all regressors, anesthetized\n    value: 0.55\n    tolerance: 0.055\n  criterion: As fig5e-volume, fig5h-neural-noise and fig5-multiple-regression on the anesthetized\n    1348 (Methods) or 1358 (SI Figure 8 legend) ensembles of 20 from 375 units. The combined model's\n    printed F(2,341) does not match four regressors; the R2adj is judged. Reproduced when the\n    three values are within tolerance with positive volume and negative noise slopes.\n- id: figs9-per-region-regressions\n  statement: Analysed separately for primary and secondary auditory pallium, the relation of\n    decoder performance with volume spanned (positive) and neural variability (negative) appears in\n    both datasets but is significant only in the anesthetized one; there the four regressors\n    explain R2adj = 0.752 in primary and 0.633 in secondary pallium.\n  source: SI Figure 9 legend; Results, Modulation receptive fields of single neurons and ensemble\n    decoding performance, paragraph 7\n  quote: The relationship between decoder performance and volume spanned was observed in both the\n    primary and secondary auditory pallium and in both the awake and anesthetized sets but was\n    statistically significant only in the anesthetized dataset\n  statistics:\n  - about: four regressors, primary auditory pallium\n    test: F-test, ensemble corrected\n    statistic: F(4, 125) = 98.694\n    p: 0.00001\n    p_relation: <\n  - about: four regressors, secondary auditory pallium\n    test: F-test, ensemble corrected\n    statistic: F(4,170) = 98.696\n    p: 0.00001\n    p_relation: <\n  depends_on:\n  - figs6-primary-vs-secondary\n  expected:\n  - quantity: R2adj, four regressors, primary pallium\n    value: 0.752\n    tolerance: 0.0752\n  - quantity: R2adj, four regressors, secondary pallium\n    value: 0.633\n    tolerance: 0.0633\n  criterion: The awake part uses this dataset; the R2adj values are read as anesthetized (the S9\n    legend's significant results; the Results do not name the dataset and the printed df match\n    neither dataset's neff). Awake part, Figure 5 regressions (C7 to C11) within each area's good\n    units; reproduced when volume slopes are positive and noise slopes negative in both areas and\n    the corrected F-tests give p >= 0.05 (no significance, as the legend says). The R2adj values are\n    tested on CRCNS aa-4 when available, within tolerance; on the awake data they are reported only.\n"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/robotka-2023.yaml paper/10.1016-j.celrep.2023.112034.txt; echo EXIT $?
```

Result: not kept, because it reads the paper's text.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/robotka-2023.yaml",
 "old_string": "  quote: For the awake dataset we used 110 distinct stimuli sampling 10 call-types (Begging or Be\n    12; Long-Tonal or LT 13; Thuk or Th 5",
 "new_string": "  quote: For the awake dataset we used 110 distinct stimuli sampling 10 call-types"
}
```

```
The file claims/robotka-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd  python tools/claims_check.py claims/robotka-2023.yaml paper/10.1016-j.celrep.2023.112034.txt; echo EXIT $?; python3 - <<'EOF'
import yaml,re
d=yaml.safe_load(open('claims/robotka-2023.yaml'))
raw=open('claims/robotka-2023.yaml').read()
print('emdash', '—' in raw, 'rather' in raw.lower())
def walk(o,path=''):
    if isinstance(o,dict):
        for k,v in o.items(): walk(v,path+'.'+k)
    elif isinstance(o,list):
        for i,v in enumerate(o): walk(v,path+f'[{i}]')
    elif isinstance(o,str) and ': ' in o: print('COLON',path,o[:80])
walk(d)
c=d['claims']
print(len(c), sum('quote' in x for x in c), sum('statistics' in x for x in c), sum('criterion' in x for x in c), sum(x.get('kind')=='link' for x in c))
from collections import Counter; print(Counter(x.get('data','dataset') for x in c))
EOF
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  git status --short
```

```
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
?? claims/robotka-2023.yaml
?? scripts
```

**Agent**

I wrote `claims/robotka-2023.yaml`. The quote checker passes with 0 problems. Nothing was committed, and the other untracked files in the working tree were there before this run.

**Text read:** the version of record, with the STAR Methods and the full supplement (SI Figs 1 to 11 and their legends, at the end of the PDF). Table 1 was read from the text. I did not open the PDF, since no figure or table was garbled. I also read the analysis code, `ftheunissen/Ensemble-Code-Cell-Reports-2022` at commit f2d2376. Its printed outputs match the Figure 5 statistics: F(1,79) = 8.975, 6.73 and 8.75, and F(4,76) = 5.832.

**Claims:** 28 in all: 27 findings plus one link claim checking the stimulus set.
- 27 have quotes. The other one, the Table 1 SNR claim, is marked `inferred` because its values appear only in the table.
- 14 have statistics.
- All 28 have criteria.
- Data: 20 use this dataset alone, 5 need outside inputs (`with_inputs`), and 3 use the anesthetized dataset CRCNS aa-4, which is a separate deposit (`elsewhere`).

**Details the paper leaves open, with the readings named.** These are recorded once in the opening comment as shared rules C1 to C12, which the claims refer to.
- **Response strength Z:** the Methods read as subtracting the mean; the code divides by the SD only. This does not affect any decoder result.
- **Per-call-type Z for the selectivity index:** (a) the mean of trial Z over the call type; (b) the code's mean(d)/sd(d) within each call type.
- **Cross-validation:** (a) the Methods hold out one exemplar stimulus per call type; (b) the code holds out one random trial of every stimulus, repeated 100 times for ensembles.
- **PCC:** (a) the mean of the row-normalized diagonal; (b) the code's trace over the number of test trials.
- **The 1,746 ensembles:** (a) the code keeps the 1,800 sampled ensembles with PCC above 30%, a filter the Methods never state; (b) all 1,800.
- **Top ensembles:** the Results and Figure 4 legend say top 10%, the Methods say top 5%.
- **Sound window for the MPS:** the Methods say the first 500 ms; the code uses 500 ms before to 500 ms after onset.
- **LDA axes:** the Methods' "first three", read as the three largest eigenvalues. The code's `eigh` puts the smallest first, so its literal choice is run as a variant. The regressions use log volume, as in the code.
- **Neural noise:** variance (Results and code) or SD (Figure 5 legend).
- **Entropy Selectivity:** the diagonal normalized to sum 1 (code) or used as is (Methods formula).
- **Neural clustering:** UMAP then Ward linkage (code), or Ward linkage alone (Methods).
- **Auditory t-test:** n − 1 degrees of freedom (standard) or n (code).
- **Smaller ones:**
  - The auditory count is 607 in the Methods but 609 in SI Fig 2.
  - The printed p = 0.21 for t(80) = −0.808 is a one-sided value.
  - The combined anesthetized regression is printed as F(2,341) with four regressors.
  - The per-region F(4,125) and F(4,170) match neither dataset's corrected sample size, so the dataset behind them is read as anesthetized.
  - The ensemble size for the sex comparison is read as 15 units.

**Missing material a claim needs:**
- **Vocalization database:** the acoustic clustering claims (Fig 6, the acoustic-label decoding, SI Fig 10) need the lab's database (3,405 bouts from 45 birds). The paper gives no deposit for it, and the code reads parameter and segment tables that are not in the repository.
- **Anatomical areas:** the area claims (SI Figs 5, 6, 9) need each unit's area. If the dataset does not hold it, those claims cannot be tested.
- **Spike-sorting quality indices:** the Qisi and Qacc indices in Table 1 need full spike trains, which the dataset does not hold, so they are not claimed.

## End of run

35 turns, 6 minutes, $3.25 at API prices, result: success.
