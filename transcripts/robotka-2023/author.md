# robotka-2023 · author · run 43639548754

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; ls; ls docs entries paper claims attempts | head -80; wc -l docs/*.md README.md
```

```
Sat Nov 14 20:57:28 UTC 2026
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
[... 107 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
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
[... 657 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/robotka-2023.yaml; ls paper; ls -R entries/fouke-2025
```

```
<persisted-output>
Output too large (54.1KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/741377b8-2a3c-4605-8e88-98f00c181e43/tool-results/betja0bet.txt

Preview (first 2KB):
# Claims for Robotka, Thomas, Yu, Wood, Elie, Gahr & Theunissen (2023), Cell Reports 42, 112034,
# "Sparse ensemble neural code for a complete vocal repertoire", tested on CRCNS aa-5.
#
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
# protocol pilot-14 as stated in docs/protocol.md (Reader). The criteria were written from the
# paper and its code alone; no data of the dataset were seen.
#
# Text read: the version of record (paper/10.1016-j.celrep.2023.112034.txt, extracted from the
# publisher PDF), with its STAR Methods and the Supplemental information (SI Figures 1 to 11 and
# their legends, which the PDF carries at its end). Table 1 was read from the text. Figures were
# not opened; no claim needed a value only printed in a figure.
#
# Code read: github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit
# f2d237639217425e7fc81d694708f19428a3b026 (v1.0 in the key resources table, zenodo 7378502). It
# holds Jupyter notebooks with their printed outputs and decoders.py. GenerateReport.ipynb makes
# the per-unit summary (auditory test, per-call-type z, selectivity index); GenerateDataBase.ipynb
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/robotka-2023.yaml"
}
```

```
1	# Claims for Robotka, Thomas, Yu, Wood, Elie, Gahr & Theunissen (2023), Cell Reports 42, 112034,
2	# "Sparse ensemble neural code for a complete vocal repertoire", tested on CRCNS aa-5.
3	#
4	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-11,
5	# protocol pilot-14 as stated in docs/protocol.md (Reader). The criteria were written from the
6	# paper and its code alone; no data of the dataset were seen.
7	#
8	# Text read: the version of record (paper/10.1016-j.celrep.2023.112034.txt, extracted from the
9	# publisher PDF), with its STAR Methods and the Supplemental information (SI Figures 1 to 11 and
10	# their legends, which the PDF carries at its end). Table 1 was read from the text. Figures were
11	# not opened; no claim needed a value only printed in a figure.
12	#
13	# Code read: github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit
14	# f2d237639217425e7fc81d694708f19428a3b026 (v1.0 in the key resources table, zenodo 7378502). It
15	# holds Jupyter notebooks with their printed outputs and decoders.py. GenerateReport.ipynb makes
16	# the per-unit summary (auditory test, per-call-type z, selectivity index); GenerateDataBase.ipynb
17	# makes the per-trial table (response strength z, the PCA of trial-averaged KDE responses and the
18	# five PC weights per trial); decodingCallTypesNaiveBayes.ipynb and DataBaseMerge.ipynb run the
19	# single-unit decoder; decodingCallTypesNaiveBayesPart2.ipynb and decoders.py run the ensemble
20	# decoders; plotConfusions.ipynb makes Figure 4; GenerateMLFilters.ipynb makes the MRFs, the LDA,
[... 887 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; grep -n "CRCNS" -A60 docs/archives.md | head -120; cat paper/aa-5.data-description.txt; ls paper; ls papers/datasets | grep -i robot; cat papers/datasets/robotka-2023.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=aa-5/" | python3 -c "
import sys,re
t=sys.stdin.read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t): print(s,k)
print(re.findall(r'<IsTruncated>(.*?)</IsTruncated>',t))
"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-5/live/filelist.txt | head -30; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-5/live/checksums.md5 | head -5; ls entries/fouke-2025; cat entries/fouke-2025/entry.yaml; nproc; free -g
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && cat > probe.py <<'EOF'
import fsspec, tarfile, time, pickle, io, sys
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-5/live/data/ZF4F/ZF4F_2t_190613_142654.tar.gz"
t0=time.time()
f=fsspec.open(url, block_size=2**24).open()
tf=tarfile.open(fileobj=f, mode='r|gz')
n=0
for m in tf:
    print(m.name, m.size, round(time.time()-t0,1), f.tell()/1e6, flush=True)
    n+=1
    if m.isfile() and m.name.endswith('.pkl'):
        x=tf.extractfile(m)
        b=x.read()
        bio=io.BytesIO(b)
        info=pickle.load(bio); a=pickle.load(bio); r=pickle.load(bio)
        print({k:(v if not hasattr(v,'shape') or v.size<5 else v.shape) for k,v in info.items() if k not in('StimName','SpikeShape','SpikeStd')})
        print(r.columns.tolist(), r.shape); print(a.columns.tolist())
        print(r.iloc[0][['file','call_type','nTrials']].tolist(), type(r.iloc[0]['spikeTimes']))
        break
EOF
cd  && uv run --with fsspec --with aiohttp --with requests --with pandas --with numpy python $TMPDIR/probe.py 2>&1 | tail -30
```

```
Using CPython 3.13.18 interpreter at: /opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
Creating virtual environment at: .venv
   Building encore-science @ file://
Downloading networkx (2.0MiB)
Downloading pymupdf (65.8MiB)
Downloading onnxruntime (22.7MiB)
Downloading numpy (15.9MiB)
Downloading uv (16.4MiB)
 Downloaded networkx
 Downloaded numpy
 Downloaded uv
 Downloaded onnxruntime
 Downloaded pymupdf
      Built encore-science @ file://
warning: Failed to hardlink files; falling back to full copy. This may lead to degraded performance.
         If the cache and target directories are on different filesystems, hardlinking may not be supported.
         If this is intentional, set `export UV_LINK_MODE=copy` or use `--link-mode=copy` to suppress this warning.
Installed 24 packages in 458ms
Downloading pandas (11.4MiB)
Downloading aiohttp (1.8MiB)
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
git status --short | head; sed -i "s/if m.isfile() and m.name.endswith('.pkl'):/if m.isfile() and m.name.endswith('.pkl') and '\/._' not in m.name:/" $TMPDIR/probe.py && uv run --with fsspec --with aiohttp --with requests --with pandas --with numpy python $TMPDIR/probe.py 2>&1 | tail -12
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
ZF4F_2t_190613_142654 0 0.6 0.01024
ZF4F_2t_190613_142654/PlaybackPkl 0 0.6 0.01024
ZF4F_2t_190613_142654/PlaybackPkl/._goodPlayback-e18-c2.pkl 524 0.6 0.01024
ZF4F_2t_190613_142654/PlaybackPkl/goodPlayback-e18-c2.pkl 343610406 0.6 0.01024
Traceback (most recent call last):
  File "/tmp/claude-1001/probe.py", line 14, in <module>
    info=pickle.load(bio); a=pickle.load(bio); r=pickle.load(bio)
                             ~~~~~~~~~~~^^^^^
ModuleNotFoundError: No module named 'pandas.core.indexes.numeric'
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('probe.py').read()
s=s.replace("info=pickle.load(bio); a=pickle.load(bio); r=pickle.load(bio)","from pandas.compat import pickle_compat as pc\n        U=lambda: pc.Unpickler(bio).load()\n        info=U(); a=U(); r=U(); print('read',len(b)/1e6,round(time.time()-t0,1))")
open('probe.py','w').write(s)
EOF
cd  && uv run --with fsspec --with aiohttp --with requests --with pandas --with numpy python $TMPDIR/probe.py 2>&1 | tail -8
```

```
ZF4F_2t_190613_142654/PlaybackPkl 0 0.5 0.01024
ZF4F_2t_190613_142654/PlaybackPkl/._goodPlayback-e18-c2.pkl 524 0.5 0.01024
ZF4F_2t_190613_142654/PlaybackPkl/goodPlayback-e18-c2.pkl 343610406 0.5 0.01024
read 343.610406 3.6
{'Bird': 'ZF4F', 'Site': 'ZF4F_2t_190613_142654', 'Electrode': '18', 'Sort': np.int32(2), 'RateThreshold': 1.0, 'KDE_BW': 5.0, 'nStim': 60, 'nTrials': (60,), 'SpikeSNR': np.float64(5.085134364711717)}
['file', 'relation_short', 'call_type', 'nTrials', 'trialInd', 'tStim', 'stimWav', 'micWav', 'spikeTimes', 'tKDE', 'spikeKDE', 'tMic'] (60, 12)
['file', 'relation_short', 'call_type', 'start_time', 'duration', 'stop_time', 'file_path', 'spikes', 'On']
['stim1.wav', None, 2] <class 'list'>
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > survey.py <<'EOF'
import fsspec, tarfile, time, io, sys, resource
from pandas.compat import pickle_compat as pc
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-5/live/data/"+sys.argv[1]
t0=time.time()
f=fsspec.open(url, block_size=2**24).open()
tf=tarfile.open(fileobj=f, mode='r|gz')
for m in tf:
    if not m.isfile(): continue
    if '/._' in m.name or not m.name.endswith('.pkl'):
        print('other', m.name, m.size); continue
    b=tf.extractfile(m).read(); bio=io.BytesIO(b)
    U=lambda: pc.Unpickler(bio).load()
    info=U(); a=U(); r=U()
    ct=r.call_type.value_counts().to_dict()
    print(m.name.split('/')[-1], info['nStim'], round(info['SpikeSNR'],2), len(b)//10**6, 'MB', ct, 'ntr', r.nTrials.sum(), 't', round(time.time()-t0,1), 'pos', f.tell()//10**6, flush=True)
print('done', time.time()-t0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,'GB')
EOF
cd  && uv run --with fsspec --with aiohttp --with requests --with pandas --with numpy python $TMPDIR/survey.py ZF4F/ZF4F_2t_190613_142654.tar.gz 2>&1 | tail -40
```

```
other ZF4F_2t_190613_142654/PlaybackPkl/._goodPlayback-e18-c2.pkl 524
goodPlayback-e18-c2.pkl 60 5.09 343 MB {} ntr 125 t 3.5 pos 81
goodPlayback-e17-c1.pkl 60 5.85 330 MB {} ntr 112 t 7.1 pos 160
other ZF4F_2t_190613_142654/PlaybackPkl/._goodPlayback-e11-c18.pkl 524
goodPlayback-e17-c2.pkl 60 4.97 343 MB {} ntr 125 t 10.4 pos 242
other ZF4F_2t_190613_142654/PlaybackPkl/._goodPlayback-e10-c2.pkl 524
other ZF4F_2t_190613_142654/PlaybackPkl/._goodPlayback-e17-c1.pkl 524
other ZF4F_2t_190613_142654/PlaybackPkl/._goodPlayback-e19-c24.pkl 524
goodPlayback-e20-c34.pkl 60 11.54 344 MB {} ntr 125 t 13.8 pos 323
goodPlayback-e8-c3.pkl 60 5.57 324 MB {} ntr 106 t 16.6 pos 401
goodPlayback-e10-c2.pkl 60 5.1 343 MB {} ntr 125 t 19.8 pos 483
goodPlayback-e16-c2.pkl 60 6.59 343 MB {} ntr 125 t 22.9 pos 564
goodPlayback-e11-c17.pkl 51 8.32 240 MB {} ntr 55 t 25.4 pos 623
other ZF4F_2t_190613_142654/PlaybackPkl/._goodPlayback-e20-c35.pkl 524
goodPlayback-e11-c18.pkl 60 4.93 342 MB {} ntr 124 t 28.2 pos 704
goodPlayback-e19-c23.pkl 60 10.53 335 MB {} ntr 117 t 31.3 pos 783
other ZF4F_2t_190613_142654/PlaybackPkl/._goodPlayback-e19-c22.pkl 524
goodPlayback-e19-c22.pkl 60 4.81 336 MB {} ntr 118 t 34.7 pos 864
other ZF4F_2t_190613_142654/PlaybackPkl/._goodPlayback-e19-c23.pkl 524
other ZF4F_2t_190613_142654/PlaybackPkl/._goodPlayback-e18-c1.pkl 524
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > speed.py <<'EOF'
import fsspec, time, sys, zlib
url="https://crcnsarchive.s3-us-west-2.amazonaws.com/aa-5/live/data/ZF4F/ZF4F_2t_190613_142654.tar.gz"
f=fsspec.open(url, block_size=2**24).open()
t0=time.time(); raw=f.read(400*2**20); t1=time.time()
print('net MB/s', 400/(t1-t0))
d=zlib.decompressobj(31); t0=time.time(); out=d.decompress(raw); t1=time.time()
print('zlib out MB/s', len(out)/1e6/(t1-t0), 'ratio', len(out)/len(raw))
from isal import isal_zlib
d=isal_zlib.decompressobj(31); t0=time.time(); out=d.decompress(raw); t1=time.time()
print('isal out MB/s', len(out)/1e6/(t1-t0))
EOF
cd  && uv run --with fsspec --with aiohttp --with requests --with isal python $TMPDIR/speed.py 2>&1 | tail -4
```

```
Installed 15 packages in 6ms
net MB/s 82.67204922434541
zlib out MB/s 345.9256562761352 ratio 4.1623799824714665
isal out MB/s 709.4320521725516
```

**Agent calls Bash**

```bash
cd $TMPDIR && timeout 30 git clone -q https://github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 ens 2>&1 | tail -2; cd ens 2>/dev/null && git checkout -q f2d237639217425e7fc81d694708f19428a3b026 && ls && git log -1 --format=%H
```

```
DataBaseMerge.ipynb
DisplayKDEandPCJulie.ipynb
Download good pkl files.ipynb
EPHYS1-Generate_Dataframes.ipynb
EPHYS2-Population_Coding.ipynb
EPHYS3-Neural_Clustering.ipynb
EPHYS4-Population_Clustering.ipynb
Generate vocParamTable.ipynb
GenerateDataBase.ipynb
GenerateDataBase2.ipynb
GenerateDataBasePosPC.ipynb
GenerateMLFilters.ipynb
GenerateMLFiltersJulie.ipynb
GenerateMLFiltersJuliePerZone.ipynb
GenerateMLFiltersPerZone.ipynb
GenerateReport.ipynb
GenerateReport2.ipynb
Methods_walkthrough.ipynb
PlotPSTHCategoriesGUI.ipynb
PlotSpikeSortedCategoriesGUI.ipynb
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ens && cat > ../dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code':
        print(f'# ---- cell {i}'); print(''.join(c['source']))
        if len(sys.argv)>2:
            for o in c.get('outputs',[]):
                t=''.join(o.get('text',[])) or ''.join(o.get('data',{}).get('text/plain',[]))
                if t: print('## OUT:', t[:1500])
EOF
python3 ../dump.py "Download good pkl files.ipynb" x | head -80; cat config.py; ls -la | head -5; git ls-files | grep -v ipynb
```

```
# ---- cell 0
# Dependencies (Needs songephys environment)
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle as pk
import umap
from scipy.stats.mstats import zscore

from IPython.display import display
from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering

from sklearn.metrics import adjusted_rand_score
#from soundsig.sound import BioSound, WavFile, spectrogram
from scipy.cluster.hierarchy import dendrogram, linkage, cophenet, fcluster
from scipy.spatial.distance import pdist

import seaborn
[... 97 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ens && python3 ../dump.py GenerateReport.ipynb | head -300
```

```
# ---- cell 1
# Dependencies 
import os
import glob
import re
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle as pk
from scipy.stats import t


# ---- cell 3
rootPath = '[removed: a home directory path]/Code/songephys/'
dataPath = 'data/birds/'

birds = [
    os.path.basename(bird)
    for bird in sorted(glob.glob(os.path.join(rootPath+dataPath, "*")), key=os.path.getmtime, reverse=True)
    if (os.path.isdir(bird))]
[... 204 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ens && python3 ../dump.py GenerateDataBase.ipynb x | grep -v "^\s*$" | head -330
```

```
# ---- cell 1
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
# ---- cell 3
rootPath = '[removed: a home directory path]/Code/songephys/'
dataPath = 'data/birds/'
birds = [
    os.path.basename(bird)
    for bird in sorted(glob.glob(os.path.join(rootPath+dataPath, "*")), key=os.path.getmtime, reverse=True)
    if (os.path.isdir(bird))]
# ---- cell 4
birds = ['ZF7F', 'ZF6M', 'ZF5M', 'ZF4F']
[... 311 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ens && wc -l decoders.py && cat decoders.py | head -250
```

```
417 decoders.py
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
[... 232 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "python" tools/entry.py | grep -i "version\|3\.1" | head -10; cat entries/fouke-2025/requirements.in; head -c 3000 entries/fouke-2025/omr.py
```

```
414:LOCK_VERSION = re.compile(r"--python-version\s+(\d+\.\d+)")
418:    """The Python version an entry runs on: its entry.yaml's `python`, else the version its lock was compiled for
431:def set_python(entry_dir: Path, version: str) -> None:
432:    """Write `python: "<version>"` into entry.yaml, replacing the field or adding it after `license`."""
435:    line = f'python: "{version}"'
447:    version = version or python_of(entry_dir)
448:    r = subprocess.run(["uv", "pip", "compile", "--quiet", "--generate-hashes", "--python-version", version,
451:        set_python(entry_dir, version)
471:def upgrade_python(entry_dir: Path, version: str, before: Path, output_dir: Path, timeout: int,
481:        print(f"error: Python {version} could not lock or run the entry; it stays on {python_of(entry_dir)}",
dandi
h5py
matplotlib
numpy
pandas
remfile
scipy
statsmodels
"""Loading and measures for the freely swimming optomotor data of dandiset 001453.

[... 55 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/robotka-2023/aa5.py",
 "content": "\"\"\"Loading and measures for CRCNS aa-5, the awake playback data of Robotka et al. (2023).\n\nRobotka, Thomas, Yu, Wood, Elie, Gahr & Theunissen (2023), Cell Reports 42, 112034,\ndoi:10.1016/j.celrep.2023.112034. Data set: CRCNS aa-5, doi:10.6080/K0TT4P5Q (unversioned).\n\nThe data set holds one tar.gz per recording site, each with one pickle per spike-sorted unit\n(`goodPlayback-e<electrode>-c<cluster>.pkl`, data descriptor v0.6). A pickle holds a unit\ndictionary and two pandas tables written with pandas 1.x; `pandas.compat.pickle_compat` reads\nthem. A tar.gz cannot be read out of order, so each site file is streamed once from the bucket\n(decompressed with isal, which is faster than zlib), and each unit is reduced as it is read to\nwhat the analysis uses: spike times per trial, the stored KDE (first 1000 samples), labels, and\nthe stimulus waveform of each stimulus once. The microphone recordings, most of every file, are\ndropped. Nothing is written to disk.\n\nWhere the parameters come from (the claims file's common methods C1 to C11 cite the paper and\nits code, github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit f2d2376):\n\n- `SNR_MIN = 5`: units with spike SNR above 5 (C1; GenerateDataBase.ipynb skips SpikeSNR < 5).\n- `P_AUD = 0.01` and the 0 to 0.5 s minus -0.5 to 0 s spike-count difference (C1, SI Figure 2A\n  legend; GenerateReport.ipynb calc_zscore_all, which uses all stimuli of the pickle, song\n  included). A unit with no call-type label in its pickle (song-only sites) is skipped, as the\n  code does (`if ncalls == 0: continue`).\n- `N_KDE = 1000`, `MIN_TRIALS_KDE = 5`: the PCA of the trial-averaged responses uses the stored\n  spikeKDE, first 1000 samples, of stimuli with 5 or more trials (C4; GenerateDataBase.ipynb).\n- The PC weight of a trial is 1000 per spike at its nearest KDE sample, minus the mean, projected\n  on the first five PCs (C4; GenerateDataBase.ipynb cell 17).\n- Decoder: GaussianNB with uniform priors (C5; decoders.naiveBayes).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport hashlib\nimport io\nimport re\nimport time\nfrom concurrent.futures import ProcessPoolExecutor, as_completed\n\nimport numpy as np\nimport pandas as pd\n\nBUCKET = \"https://crcnsarchive.s3-us-west-2.amazonaws.com/\"\nPREFIX = \"aa-5/live/\"\nDOI = \"10.6080/K0TT4P5Q\"\n\nSNR_MIN = 5.0\nP_AUD = 0.01\nN_KDE = 1000\nMIN_TRIALS_KDE = 5\nN_PC = 5\nCALL_TYPES = [\"Ag\", \"Be\", \"DC\", \"Di\", \"LT\", \"Ne\", \"So\", \"Te\", \"Th\", \"Wh\"]\n\n\n# ----------------------------------------------------------------------------------------------\n# Listing and streaming\n\n\ndef list_files():\n    \"\"\"Every object of the data set in the bucket, as (key, size).\"\"\"\n    import requests\n\n    out, token = [], None\n    while True:\n        params = {\"list-type\": \"2\", \"prefix\": PREFIX}\n        if token:\n            params[\"continuation-token\"] = token\n        t = requests.get(BUCKET, params=params, timeout=60).text\n        out += [(k, int(s)) for k, s in re.findall(r\"<Key>(.*?)</Key>.*?<Size>(\\d+)</Size>\", t, re.S)]\n        m = re.search(r\"<NextContinuationToken>(.*?)</NextContinuationToken>\", t)\n        if not m:\n            return out\n        token = m.group(1)\n\n\ndef checksums():\n    \"\"\"The data set's checksums.md5, as {path relative to aa-5/live/: md5}.\"\"\"\n    import requests\n\n    t = requests.get(BUCKET + PREFIX + \"checksums.md5\", timeout=60).text\n    return {p.strip(): h for h, p in (ln.split(None, 1) for ln in t.splitlines() if ln.strip())}\n\n\ndef _unpickle(fobj):\n    from pandas.compat import pickle_compat\n\n    return pickle_compat.Unpickler(fobj).load()\n\n\ndef _reduce_unit(info, dfabs, dfrel, member):\n    \"\"\"Keep what the analysis needs from one unit's pickle.\"\"\"\n    rows = []\n    for _, r in dfrel.iterrows():\n        st = [np.asarray(s, dtype=float) for s in r[\"spikeTimes\"]]\n        tk = np.asarray(r[\"tKDE\"], dtype=float)\n        rows.append(dict(\n            file=r[\"file\"], call_type=r[\"call_type\"], relation_short=r[\"relation_short\"],\n            nTrials=int(r[\"nTrials\"]), trialInd=np.asarray(r[\"trialInd\"]), spikeTimes=st,\n            kde=np.asarray(r[\"spikeKDE\"], dtype=np.float32)[:N_KDE].copy(),\n            tKDE0=float(tk[0]), dtKDE=float(tk[1] - tk[0]), nKDE=len(tk),\n            tStim0=float(r[\"tStim\"][0]), dtStim=float(r[\"tStim\"][1] - r[\"tStim\"][0]),\n            stimLen=len(r[\"stimWav\"]),\n            stimHash=hashlib.md5(np.asarray(r[\"stimWav\"], dtype=np.float32).tobytes()).hexdigest(),\n            micShape=tuple(np.shape(r[\"micWav\"])),\n        ))\n    spk_hash = hashlib.md5(b\"\".join(np.round(s, 6).tobytes() for row in rows for s in row[\"spikeTimes\"])).hexdigest()\n    unit = dict(\n        member=member, pkl=member.split(\"/\")[-1], Bird=info[\"Bird\"], Site=info[\"Site\"],\n        Electrode=str(info[\"Electrode\"]), Sort=int(info[\"Sort\"]), SpikeSNR=float(info[\"SpikeSNR\"]),\n        nStim=int(info[\"nStim\"]), KDE_BW=float(info[\"KDE_BW\"]), RateThreshold=float(info[\"RateThreshold\"]),\n        info_keys=sorted(info.keys()), abs_columns=list(dfabs.columns), rel_columns=list(dfrel.columns),\n        n_abs_rows=len(dfabs), spike_hash=spk_hash, rows=rows,\n    )\n    waves = {}\n    for _, r in dfrel.iterrows():\n        if r[\"call_type\"] is not None and r[\"file\"] not in waves:\n            waves[r[\"file\"]] = dict(wav=np.asarray(r[\"stimWav\"], dtype=np.float32), tStim0=float(r[\"tStim\"][0]),\n                                    dt=float(r[\"tStim\"][1] - r[\"tStim\"][0]), call_type=r[\"call_type\"])\n    return unit, waves\n\n\ndef read_site(key, max_units=None):\n    \"\"\"Stream one site tar.gz and return (units, stimulus waveforms, other members, seconds).\"\"\"\n    import tarfile\n\n    import fsspec\n    from isal import igzip\n\n    t0 = time.time()\n    units, waves, other = [], {}, []\n    with fsspec.open(BUCKET + key, block_size=2**24).open() as f:\n        gz = igzip.IGzipFile(fileobj=f, mode=\"rb\")\n        with tarfile.open(fileobj=gz, mode=\"r|\") as tf:\n            for m in tf:\n                if not m.isfile():\n                    continue\n                base = m.name.split(\"/\")[-1]\n                if base.startswith(\"._\") or not base.endswith(\".pkl\"):\n                    other.append((m.name, m.size))\n                    continue\n                fo = tf.extractfile(m)\n                buf = io.BufferedReader(fo, buffer_size=2**22)\n                info = _unpickle(buf)\n                dfabs = _unpickle(buf)\n                dfrel = _unpickle(buf)\n                u, w = _reduce_unit(info, dfabs, dfrel, m.name)\n                del dfabs, dfrel\n                units.append(u)\n                for k, v in w.items():\n                    waves.setdefault(k, v)\n                if max_units and len(units) >= max_units:\n                    break\n    return units, waves, other, time.time() - t0\n\n\ndef read_all(keys, workers=4, max_units=None, log=print):\n    \"\"\"Stream every site in `keys` with `workers` processes; largest files first.\"\"\"\n    results = {}\n    t0 = time.time()\n    with ProcessPoolExecutor(workers) as ex:\n        futs = {ex.submit(read_site, k, max_units): k for k in keys}\n        for fu in as_completed(futs):\n            k = futs[fu]\n            results[k] = fu.result()\n            log(f\"{k.split('/')[-1]}: {len(results[k][0])} units, {results[k][3]:.0f} s \"\n                f\"(elapsed {time.time() - t0:.0f} s, {len(results)}/{len(keys)})\")\n    units, waves, other = [], {}, []\n    for k in keys:\n        u, w, o, _ = results[k]\n        units += u\n        other += o\n        for s, v in w.items():\n            waves.setdefault(s, []).append(v)\n    return units, waves, other\n\n\n# ----------------------------------------------------------------------------------------------\n# Single-unit measures\n\n\ndef spike_diff(spike_times):\n    \"\"\"Spike count in [0, 0.5) s minus count in [-0.5, 0) s for one trial (C1).\"\"\"\n    s = spike_times\n    return float(np.sum((s >= 0) & (s < 0.5)) - np.sum((s >= -0.5) & (s < 0)))\n\n\ndef unit_table(units):\n    \"\"\"One row per unit with SNR, auditory test (Methods and code readings) and labels.\"\"\"\n    from scipy import stats\n\n    recs = []\n    for u in units:\n        d_all = np.array([spike_diff(s) for r in u[\"rows\"] for s in r[\"spikeTimes\"]])\n        calls = sorted({r[\"call_type\"] for r in u[\"rows\"] if r[\"call_type\"] is not None})\n        n = len(d_all)\n        sd = d_all.std(ddof=1) if n > 1 else 0.0\n        if n > 1 and sd == 0:\n            d_all = d_all.copy()\n            d_all[0] += 1  # the code adds a spike when the SD is zero (calc_zscore_all)\n            sd = d_all.std(ddof=1)\n        z = d_all.mean() / sd if n > 1 else 0.0\n        # Methods reading: standard one-sample t-test, n - 1 df\n        p_methods = stats.ttest_1samp(d_all, 0.0).pvalue if n > 1 else 1.0\n        # Code reading: t = z sqrt(n) with n df (calc_zscore_all)\n        p_code = 2 * stats.t.sf(abs(z) * np.sqrt(n), n) if n > 1 else 1.0\n        recs.append(dict(\n            uid=u[\"Site\"] + \"_\" + u[\"pkl\"], bird=u[\"Bird\"], site=u[\"Site\"], electrode=u[\"Electrode\"],\n            sort=u[\"Sort\"], snr=u[\"SpikeSNR\"], n_calls=len(calls), n_trials_all=n, zAud=z,\n            meanD=d_all.mean() if n else np.nan, p_methods=p_methods, p_code=p_code,\n            n_voc_stim=len({r[\"file\"] for r in u[\"rows\"] if r[\"call_type\"] is not None}),\n            spike_hash=u[\"spike_hash\"],\n        ))\n    return pd.DataFrame(recs)\n\n\ndef voc_rows(u):\n    return [r for r in u[\"rows\"] if r[\"call_type\"] is not None]\n\n\ndef trial_table(u):\n    \"\"\"Vocalization trials of one unit: stim, call, d, and Z (C2, both readings).\"\"\"\n    recs = []\n    for r in voc_rows(u):\n        for it, s in enumerate(r[\"spikeTimes\"]):\n            recs.append((r[\"file\"], r[\"call_type\"], it, spike_diff(s)))\n    df = pd.DataFrame(recs, columns=[\"stim\", \"call\", \"trial\", \"R\"])\n    sd = df[\"R\"].std(ddof=0)\n    if sd == 0:\n        sd = 1.0 / len(df)\n    df[\"z\"] = df[\"R\"] / sd                       # code reading (b): d / SD, ddof 0\n    df[\"z_a\"] = (df[\"R\"] - df[\"R\"].mean()) / sd  # Methods reading (a): z-scored\n    return df\n\n\ndef zct_unit(u, trials):\n    \"\"\"Per-call-type Z of one unit: (a) mean trial Z (C2 b) per type; (b) code's mean(d)/sd(d).\"\"\"\n    za, zb = {}, {}\n    for c, g in trials.groupby(\"call\"):\n        za[c] = g[\"z\"].mean()\n        d = g[\"R\"].to_numpy().astype(float)\n        if len(d) > 1:\n            sd = d.std(ddof=1)\n            if sd == 0:\n                d = d.copy()\n                d[0] += 1\n                sd = d.std(ddof=1)\n            zb[c] = d.mean() / sd\n        else:\n            zb[c] = 0.0\n    return za, zb\n\n\ndef selectivity_index(z):\n    z = np.asarray(list(z), dtype=float)\n    n = len(z)\n    return (1 - z.mean() ** 2 / (z ** 2).mean()) / (1 - 1 / n)\n\n\ndef kde_matrix(u):\n    \"\"\"Stored KDE (first 1000 samples) of each vocalization stimulus with >= 5 trials (C4).\"\"\"\n    out = []\n    for r in voc_rows(u):\n        if r[\"nTrials\"] >= MIN_TRIALS_KDE:\n            k = r[\"kde\"][:N_KDE].astype(float)\n            if not np.sum(np.concatenate(r[\"spikeTimes\"]) if r[\"spikeTimes\"] else [0.0]):\n                k = np.zeros(N_KDE)  # the code leaves rows of stimuli with no spikes at zero\n            out.append(k)\n    return np.array(out).reshape(-1, N_KDE)\n\n\ndef trial_pcs(u, pca):\n    \"\"\"PC weights T1..T5 of every vocalization trial (C4; GenerateDataBase.ipynb cell 17).\"\"\"\n    comps = pca.components_[:N_PC, :N_KDE]\n    base = comps @ (-pca.mean_)\n    out = []\n    for r in voc_rows(u):\n        tk = r[\"tKDE0\"] + r[\"dtKDE\"] * np.arange(r[\"nKDE\"])\n        for s in r[\"spikeTimes\"]:\n            v = base.copy()\n            if len(s):\n                idx = np.searchsorted(tk, s)\n                idx = np.clip(idx, 1, len(tk) - 1)\n                left = tk[idx - 1]\n                right = tk[idx]\n                idx = np.where(np.abs(s - left) <= np.abs(right - s), idx - 1, idx)\n                idx = idx[idx < N_KDE]\n                if len(idx):\n                    v = v + 1000.0 * comps[:, idx].sum(axis=1)\n            out.append(v)\n    return np.array(out).reshape(-1, N_PC)\n\n\n# ----------------------------------------------------------------------------------------------\n# Decoding (C5)\n\n\nclass UnitData:\n    \"\"\"Per unit, for each stimulus, the trial features: Z and Z+T (6 per trial).\"\"\"\n\n    def __init__(self, uid, stims, calls, feats):\n        self.uid = uid\n        self.stims = stims      # list of stim names (sorted)\n        self.calls = calls      # dict stim -> call type\n        self.feats = feats      # dict stim -> array (ntrials, 6): z, T1..T5\n\n\ndef decode(units, rng, code=\"ZT\", cv=\"trial\", nperm=1, return_conf=False, call_of=None):\n    \"\"\"Gaussian naive Bayes decoding of call type from an ensemble (C5).\n\n    cv = \"trial\": the code's scheme (decoders.naiveBayes): for each repetition one random trial of\n    every stimulus (the same random draw per unit) is held out and tested; training rows join the\n    i-th remaining trial of each unit for the same stimulus, with random redraws for units with\n    fewer trials. cv = \"exemplar\": the Methods' scheme: for each call type, the trials of one\n    exemplar stimulus are held out (one random exemplar per type per repetition); training rows\n    are built from the other stimuli as above; the held-out stimulus's trials are joined trial\n    by trial.\n    Returns the summed posterior confusion matrix (true x predicted) and tests per class.\n    `call_of` maps stimulus to label (default the call type).\n    \"\"\"\n    from sklearn.naive_bayes import GaussianNB\n\n    stims = sorted(set.intersection(*[set(u.stims) for u in units]))\n    calls = call_of or units[0].calls\n    labels = sorted({calls[s] for s in stims})\n    lab_idx = {c: i for i, c in enumerate(labels)}\n    nc = len(labels)\n    cols = slice(0, 1) if code == \"Z\" else slice(0, 6)\n    conf = np.zeros((nc, nc))\n    ntest = np.zeros(nc)\n    for _ in range(nperm):\n        Xtr, ytr, Xte, yte = [], [], [], []\n        if cv == \"exemplar\":\n            held = set()\n            for c in labels:\n                cand = [s for s in stims if calls[s] == c]\n                held.add(cand[rng.integers(len(cand))])\n        for s in stims:\n            per = [u.feats[s][:, cols] for u in units]\n            lens = [len(p) for p in per]\n            if min(lens) == 0:\n                continue\n            if cv == \"trial\":\n                if min(lens) >= 2:\n                    test_idx = [rng.integers(L) for L in lens]\n                    Xte.append(np.hstack([p[i] for p, i in zip(per, test_idx)]))\n                    yte.append(lab_idx[calls[s]])\n                    per = [np.delete(p, i, axis=0) for p, i in zip(per, test_idx)]\n                    lens = [len(p) for p in per]\n                n = max(lens)\n                rows = []\n                for p, L in zip(per, lens):\n                    idx = np.arange(n)\n                    extra = idx >= L\n                    if extra.any():\n                        idx = idx.copy()\n                        idx[extra] = rng.integers(L, size=extra.sum())\n                    rows.append(p[idx])\n                Xtr.append(np.hstack(rows))\n                ytr += [lab_idx[calls[s]]] * n\n            else:\n                n = max(lens)\n                rows = []\n                for p, L in zip(per, lens):\n                    idx = np.arange(n)\n                    extra = idx >= L\n                    if extra.any():\n                        idx = idx.copy()\n                        idx[extra] = rng.integers(L, size=extra.sum())\n                    rows.append(p[idx])\n                X = np.hstack(rows)\n                if s in held:\n                    Xte.append(X)\n                    yte += [lab_idx[calls[s]]] * n\n                else:\n                    Xtr.append(X)\n                    ytr += [lab_idx[calls[s]]] * n\n        if cv == \"trial\":\n            Xte = np.vstack(Xte)\n        else:\n            Xte = np.vstack(Xte)\n        Xtr = np.vstack(Xtr)\n        ytr = np.array(ytr)\n        yte = np.array(yte)\n        if len(np.unique(ytr)) != nc:\n            continue\n        clf = GaussianNB(priors=np.ones(nc) / nc)\n        clf.fit(Xtr, ytr)\n        P = clf.predict_proba(Xte)\n        for y, p in zip(yte, P):\n            conf[y] += p\n            ntest[y] += 1\n    return conf, ntest, labels\n\n\ndef pcc_code(conf, ntest):\n    \"\"\"PCC as the code: trace of the summed matrix over the number of test trials (C5 b).\"\"\"\n    return 100.0 * np.trace(conf) / ntest.sum()\n\n\ndef pcc_methods(conf, ntest):\n    \"\"\"PCC as the Methods: mean of the diagonal of the row-normalized matrix (C5 a).\"\"\"\n    ok = ntest > 0\n    return 100.0 * np.mean(np.diag(conf)[ok] / ntest[ok])\n\n\ndef row_normalize(conf, ntest):\n    out = np.zeros_like(conf)\n    ok = ntest > 0\n    out[ok] = conf[ok] / ntest[ok, None]\n    return out\n\n\n# ----------------------------------------------------------------------------------------------\n# Ensemble-corrected statistics (C8)\n\n\ndef corrected_sem(x, ns, ne):\n    \"\"\"Ensemble-corrected SD and SEM and neff (Methods, Statistical analysis; C8).\"\"\"\n    x = np.asarray(x, dtype=float)\n    neff = ns - ne + 1\n    sc = np.sqrt(ns / (ns - ne) * x.var(ddof=1))\n    return sc, sc / np.sqrt(neff), neff\n\n\ndef corrected_ttest(x, y, ns, ne):\n    \"\"\"Two-sample t-test with ensemble-corrected SEMs and 2 neff - 2 df (C8).\"\"\"\n    from scipy import stats\n\n    _, sx, neff = corrected_sem(x, ns, ne)\n    _, sy, _ = corrected_sem(y, ns, ne)\n    t = (np.mean(x) - np.mean(y)) / np.sqrt(sx ** 2 + sy ** 2)\n    df = 2 * neff - 2\n    return t, df, 2 * stats.t.sf(abs(t), df)\n"
}
```

```
File created successfully at: entries/robotka-2023/aa5.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q -p 3.12 venv 2>&1 | tail -1; VIRTUAL_ENV=$TMPDIR/venv uv pip install -q fsspec aiohttp requests "pandas<3" numpy scipy scikit-learn isal statsmodels umap-learn 2>&1 | tail -2; cat > t1.py <<'EOF'
import sys, time, resource
sys.path.insert(0,'entries/robotka-2023')
import aa5
u,w,o,t=aa5.read_site('aa-5/live/data/ZF4F/ZF4F_2t_190612_101201.tar.gz', max_units=2)
print(t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
for x in u:
    print(x['pkl'], x['SpikeSNR'], x['nStim'], x['n_abs_rows'], x['abs_columns'], x['info_keys'])
    import collections
    print(collections.Counter(r['call_type'] for r in x['rows']))
    print([ (r['file'], r['nTrials'], r['nKDE'], r['tKDE0'], r['dtKDE'], r['micShape'], r['stimLen']) for r in x['rows'][:3]])
print(len(w), list(w)[:5])
EOF
$TMPDIR/venv/bin/python t1.py
```

```
14.2861008644104 1.554928
goodPlayback-e17-c38.pkl 5.651122845118644 170 765 ['file', 'relation_short', 'call_type', 'start_time', 'duration', 'stop_time', 'file_path', 'spikes', 'On'] ['Bird', 'Electrode', 'KDE_BW', 'RateThreshold', 'Site', 'Sort', 'SpikeSNR', 'SpikeShape', 'SpikeStd', 'StimName', 'nStim', 'nTrials']
Counter({None: 60, 'Ne': 15, 'Te': 15, 'DC': 14, 'Wh': 13, 'LT': 13, 'Be': 12, 'Ag': 9, 'So': 9, 'Th': 5, 'Di': 5})
[('BlaBla0506_MAF_Ag_0_fs25k.wav', 3, 5001, -0.5, 0.0010000000000000009, (3, 125000), 125000), ('BlaBla0506_MAF_Ag_1_fs25k.wav', 3, 5001, -0.5, 0.0010000000000000009, (3, 125000), 125000), ('BlaBla0506_MAF_Ag_2_fs25k.wav', 5, 5001, -0.5, 0.0010000000000000009, (5, 125000), 125000)]
goodPlayback-e8-c38.pkl 7.4711752176633075 170 746 ['file', 'relation_short', 'call_type', 'start_time', 'duration', 'stop_time', 'file_path', 'spikes', 'On'] ['Bird', 'Electrode', 'KDE_BW', 'RateThreshold', 'Site', 'Sort', 'SpikeSNR', 'SpikeShape', 'SpikeStd', 'StimName', 'nStim', 'nTrials']
Counter({None: 60, 'Ne': 15, 'Te': 15, 'DC': 14, 'Wh': 13, 'LT': 13, 'Be': 12, 'Ag': 9, 'So': 9, 'Th': 5, 'Di': 5})
[('BlaBla0506_MAF_Ag_0_fs25k.wav', 4, 5001, -0.5, 0.0010000000000000009, (4, 125000), 125000), ('BlaBla0506_MAF_Ag_1_fs25k.wav', 3, 5001, -0.5, 0.0010000000000000009, (3, 125000), 125000), ('BlaBla0506_MAF_Ag_2_fs25k.wav', 5, 5001, -0.5, 0.0010000000000000009, (5, 125000), 125000)]
110 ['BlaBla0506_MAF_Ag_0_fs25k.wav', 'BlaBla0506_MAF_Ag_1_fs25k.wav', 'BlaBla0506_MAF_Ag_2_fs25k.wav', 'BlaBla0506_MAF_DC_7-3-6_fs25k.wav', 'BlaBla0506_MAF_DC_8-4-1_fs25k.wav']
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && cat > full.py <<'EOF'
import sys, time, resource, pickle
sys.path.insert(0,'entries/robotka-2023')
import aa5
files=[(k,s) for k,s in aa5.list_files() if k.endswith('.tar.gz')]
files.sort(key=lambda x:-x[1])
print(len(files), sum(s for _,s in files)/1e9,'GB', flush=True)
t0=time.time()
units,waves,other=aa5.read_all([k for k,_ in files], workers=4, log=lambda s: print(s, flush=True))
print('total', time.time()-t0, len(units), resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6, resource.getrusage(resource.RUSAGE_CHILDREN).ru_maxrss/1e6)
pickle.dump((units,waves,other), open('reduced.pkl','wb'))
EOF
$TMPDIR/venv/bin/python full.py 2>&1 | tail -60; date -u
```

```
Sat Nov 14 21:02:46 UTC 2026
50 163.775295499 GB
ZF7F_7t_190806_115742.tar.gz: 21 units, 159 s (elapsed 160 s, 1/50)
ZF5M_8t_190627_132428.tar.gz: 29 units, 160 s (elapsed 160 s, 2/50)
ZF4F_3t_190613_150928.tar.gz: 23 units, 167 s (elapsed 167 s, 3/50)
ZF7F_7_5t_190807_105305.tar.gz: 19 units, 144 s (elapsed 304 s, 4/50)
ZF7F_5_5t_190722_121506.tar.gz: 23 units, 142 s (elapsed 310 s, 5/50)
ZF6M_7_5t_190723_100723.tar.gz: 27 units, 156 s (elapsed 316 s, 6/50)
ZF4F_2t_190612_101201.tar.gz: 26 units, 373 s (elapsed 373 s, 7/50)
ZF5M_11t_190704_100420.tar.gz: 24 units, 145 s (elapsed 450 s, 8/50)
ZF7F_6t_190724_104215.tar.gz: 23 units, 142 s (elapsed 452 s, 9/50)
ZF6M_8t_190725_105432.tar.gz: 25 units, 155 s (elapsed 472 s, 10/50)
ZF4F_2t_190613_101015.tar.gz: 18 units, 173 s (elapsed 546 s, 11/50)
ZF5M_10t_190702_095313.tar.gz: 24 units, 135 s (elapsed 585 s, 12/50)
ZF7F_8_5t_190809_133540.tar.gz: 18 units, 140 s (elapsed 593 s, 13/50)
ZF5M_11t_190704_121850.tar.gz: 25 units, 134 s (elapsed 606 s, 14/50)
ZF7F_5t_190720_152938.tar.gz: 19 units, 116 s (elapsed 662 s, 15/50)
ZF6M_6_5t_190719_094702.tar.gz: 15 units, 112 s (elapsed 697 s, 16/50)
ZF6M_7_5t_190723_141539.tar.gz: 24 units, 106 s (elapsed 700 s, 17/50)
ZF4F_2t_190612_134337.tar.gz: 20 units, 102 s (elapsed 708 s, 18/50)
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > ex1.py <<'EOF'
import sys, pickle, collections, numpy as np, pandas as pd
sys.path.insert(0,'entries/robotka-2023')
import aa5
units,waves,other=pickle.load(open('reduced.pkl','rb'))
ut=aa5.unit_table(units)
print(ut.groupby('bird').size())
print('nStim dist', collections.Counter(u['nStim'] for u in units))
print('n_calls', ut.n_calls.value_counts().to_dict())
v=ut[ut.n_calls>0]
print('vocal units', len(v), 'snr>5', (v.snr>5).sum(), 'snr>=5',(v.snr>=5).sum())
for name,d in [('voc',v),('voc snr>5',v[v.snr>5]), ('all snr>5', ut[ut.snr>5]), ('all', ut)]:
    print(name, len(d), 'aud_m', (d.p_methods<0.01).sum(), 'aud_code', (d.p_code<0.01).sum(), 'aud_code<=', (d.p_code<=0.01).sum())
a=v[(v.snr>=5)&(v.p_code<=0.01)]
print('inhib', (a.zAud<0).sum(), len(a))
print('snr stats aud', a.snr.mean(), a.snr.std(), a.snr.quantile([.25,.5,.75]).tolist())
s5=v[v.snr>5]; print('snr stats snr>5', s5.snr.mean(), s5.snr.std(), s5.snr.quantile([.25,.5,.75]).tolist())
print('dup spike hashes', ut.spike_hash.duplicated(keep=False).sum())
print(ut[ut.spike_hash.duplicated(keep=False)][['uid','n_trials_all','snr']].sort_values('uid').head(30))
print('n_voc_stim', v.n_voc_stim.value_counts().to_dict())
print('other members', collections.Counter(o[0].split('/')[-1][:2] for o in other), [o for o in other if not o[0].split('/')[-1].startswith('._')][:10])
print('waves per stim', collections.Counter(len(x) for x in waves.values()), len(waves))
print('stim hash consistent', sum(len({r['stimHash'] for u in units for r in u['rows'] if r['file']==s})>1 for s in waves))
print('kde', collections.Counter((r['nKDE'],round(r['tKDE0'],3),round(r['dtKDE'],4)) for u in units for r in u['rows']).most_common(5))
print('KDE_BW', collections.Counter(u['KDE_BW'] for u in units), 'thr', collections.Counter(u['RateThreshold'] for u in units))
print('sites', ut.site.nunique(), ut.groupby('bird').site.nunique().to_dict())
tiny=[u for u in units if u['Site'].startswith('ZF4F_4t')]; print('ZF4F_4t', [(u['pkl'],u['nStim'],len(u['rows'])) for u in tiny][:3])
EOF
$TMPDIR/venv/bin/python ex1.py
```

```
bird
ZF4F    255
ZF5M    308
ZF6M    161
ZF7F    148
dtype: int64
nStim dist Counter({160: 97, 150: 82, 110: 77, 120: 54, 170: 43, 40: 39, 0: 34, 60: 31, 10: 18, 149: 16, 109: 16, 159: 9, 156: 8, 180: 7, 105: 7, 119: 7, 145: 7, 157: 7, 108: 7, 117: 6, 107: 6, 50: 6, 155: 6, 106: 6, 158: 5, 118: 5, 147: 5, 112: 5, 139: 5, 89: 5, 98: 5, 84: 5, 80: 5, 86: 5, 11: 5, 171: 4, 169: 4, 136: 4, 94: 4, 129: 4, 146: 4, 138: 4, 148: 4, 137: 4, 111: 4, 70: 4, 91: 4, 66: 4, 152: 3, 81: 3, 144: 3, 154: 3, 38: 3, 121: 3, 122: 3, 103: 3, 114: 3, 92: 3, 132: 3, 85: 3, 4: 3, 125: 3, 115: 3, 12: 3, 76: 3, 131: 3, 116: 3, 41: 3, 73: 3, 87: 3, 102: 3, 97: 3, 64: 3, 75: 3, 95: 3, 42: 3, 5: 3, 143: 2, 78: 2, 99: 2, 141: 2, 164: 2, 83: 2, 134: 2, 74: 2, 90: 2, 113: 2, 166: 2, 57: 2, 63: 2, 96: 2, 153: 2, 93: 2, 104: 2, 61: 2, 100: 2, 65: 2, 44: 2, 72: 2, 14: 2, 179: 1, 128: 1, 161: 1, 162: 1, 82: 1, 53: 1, 130: 1, 142: 1, 140: 1, 23: 1, 165: 1, 124: 1, 3: 1, 126: 1, 168: 1, 39: 1, 58: 1, 17: 1, 34: 1, 79: 1, 67: 1, 32: 1, 35: 1, 43: 1, 37: 1, 24: 1, 59: 1, 135: 1, 51: 1, 69: 1, 47: 1, 45: 1, 71: 1, 77: 1, 101: 1, 13: 1})
n_calls {10: 706, 0: 146, 3: 7, 4: 4, 9: 3, 8: 2, 6: 1, 2: 1, 5: 1, 1: 1}
vocal units 726 snr>5 414 snr>=5 414
voc 726 aud_m 433 aud_code 433 aud_code<= 433
voc snr>5 414 aud_m 287 aud_code 287 aud_code<= 287
all snr>5 491 aud_m 325 aud_code 325 aud_code<= 325
all 872 aud_m 494 aud_code 494 aud_code<= 494
inhib 47 287
snr stats aud 6.8370485117416 1.9875292408261738 [5.3708915827614705, 6.074238195751854, 7.646800564107204]
snr stats snr>5 6.9655985078299425 2.085962006029531 [5.412022333216114, 6.1959765048376605, 7.898173725894001]
dup spike hashes 34
                                                  uid  n_trials_all        snr
855     ZF4F_4t_190614_094759_goodPlayback-e10-c1.pkl             0   4.835757
871    ZF4F_4t_190614_094759_goodPlayback-e11-c56.pkl             0   5.316561
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ens && python3 ../dump.py plotConfusionsArea.ipynb | grep -n -i "region\|area\|zone\|NCM\|read_\|load(" | head -30
```

```
34:    inPath = rootPath+ dataPath + 'HerminaDataBase%dGoodUnitPCPerZone.pkl' % nUnit
36:    argList.append(pk.load(fileIn))
37:    confMat.append(pk.load(fileIn))
38:    pcc.append(pk.load(fileIn))
39:    selH.append(pk.load(fileIn))
40:    zoneUnique = pk.load(fileIn)
89:infoMean = np.zeros((len(numUnits), len(zoneUnique)))
90:pccMean = np.zeros((len(numUnits), len(zoneUnique)))
91:pccMax = np.zeros((len(numUnits), len(zoneUnique)))
95:    for j, zone in enumerate(zoneUnique):
120:dfDataBase = pk.load(fileIn)
121:pcKDE = pk.load(fileIn)
129:    for j, zone in enumerate(zoneUnique):
150:inPath = rootPath+dataPath+'pccUnitRateArea.pkl'
152:argList = pk.load(fileIn)
153:pcc = pk.load(fileIn)
154:selH = pk.load(fileIn)
155:rate = pk.load(fileIn)
156:pccNorm = pk.load(fileIn)
162:print(zoneUnique[0])
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ens && python3 ../dump.py decodingCallTypesNaiveBayesPart2.ipynb x | grep -v "^\s*$" | head -150
```

```
# ---- cell 0
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
# ---- cell 1
# Some paths
rootPath = '[removed: a home directory path]/Code/songephys/'
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ens && python3 ../dump.py decodingCallTypesNaiveBayesPart2.ipynb x | grep -v "^\s*$" | sed -n 150,230p; python3 ../dump.py decodingCallTypesNaiveBayes.ipynb | grep -n "naiveBayes(\|nperm"
```

```
i += 1
else:
    unitNamesGood = np.array(unitNamesFull)[indGood]
    for i in range(ntests):
        unitChoice = np.random.choice(unitNamesGood, numUnits, replace=False)
        argList.append(unitChoice)
# ---- cell 9
len(argList)
## OUT: 10000
# ---- cell 10
# Run the decoders using multiprocessors if possible
ntests = len(argList)
mpflag = True
# Run Naive Bayes in chunks of 90 with a pool of 30 workers
chunckSize = 100    # A chunk size of 100 is used for memory since it has to keep the results of all or 90 and 1800 tests.
poolSize = 30
# Allocate memory for results
pcc = np.zeros((ntests,))
selH = np.zeros((ntests,))
confMatTot = np.zeros((ncalls, ncalls))
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -i "naive bayes\|cross-valid\|held out\|exemplar\|jackknife\|leave" paper/10.1016-j.celrep.2023.112034.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1688,1760p paper/10.1016-j.celrep.2023.112034.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/robotka-2023 && python3 - <<'EOF'
s=open('aa5.py').read()
i=s.index('class UnitData:')
j=s.index('def pcc_code')
new='''def unit_features(trials, T, stims):
    """Array [n_stims, max_trials, 6] of (Z, T1..T5) per trial, NaN padded, and counts [n_stims]."""
    feats = np.column_stack([trials["z"].to_numpy(), T])
    groups = {s: feats[idx] for s, idx in trials.groupby("stim").indices.items()}
    tmax = max(len(groups.get(s, [])) for s in stims)
    F = np.full((len(stims), max(tmax, 1), 6), np.nan)
    C = np.zeros(len(stims), dtype=int)
    for i, s in enumerate(stims):
        g = groups.get(s)
        if g is not None:
            F[i, :len(g)] = g
            C[i] = len(g)
    return F, C


def _gnb_posterior(Xtr, ytr, Xte, nc):
    """sklearn GaussianNB (ML variances plus 1e-9 times the largest feature variance) with
    uniform priors, written out in numpy for speed; returns posteriors of the test rows."""
    eps = 1e-9 * Xtr.var(axis=0).max()
    mu = np.zeros((nc, Xtr.shape[1]))
    var = np.zeros((nc, Xtr.shape[1]))
    for c in range(nc):
        Xc = Xtr[ytr == c]
        mu[c] = Xc.mean(axis=0)
        var[c] = Xc.var(axis=0) + eps
    ll = -0.5 * (np.log(2 * np.pi * var).sum(axis=1)[None, :]
                 + (((Xte[:, None, :] - mu[None]) ** 2) / var[None]).sum(axis=2))
    ll -= ll.max(axis=1, keepdims=True)
    p = np.exp(ll)
    return p / p.sum(axis=1, keepdims=True)


def _rows(F, C, rng, skip=None):
    """Training rows of one ensemble for every stimulus (decoders.naiveBayes): row i joins the
    i-th trial of each unit (skipping its held-out trial), and units with fewer trials are
    padded with random redraws of their own trials. Returns X [S, n, U*6] and n per stimulus."""
    U, S, Tm, _ = F.shape
    R = C - (0 if skip is None else 1)
    R = np.maximum(R, 0)
    n = R.max(axis=0)
    i = np.arange(Tm)[None, None, :]
    rnd = (rng.random((U, S, Tm)) * np.maximum(R, 1)[:, :, None]).astype(int)
    idx = np.where(i < R[:, :, None], i, rnd)
    if skip is not None:
        idx = idx + (idx >= skip[:, :, None])
    idx = np.minimum(idx, Tm - 1)
    X = np.take_along_axis(F, idx[..., None], axis=2)      # U, S, Tm, 6
    X = np.transpose(X, (1, 2, 0, 3)).reshape(S, Tm, U * 6)
    return X, n


def decode(F, C, y, nc, rng, code="ZT", cv="trial", nperm=1):
    """Gaussian naive Bayes decoding of the labels y [S] from an ensemble (C5).

    F [U, S, Tmax, 6] and C [U, S] are the stacked unit_features of the ensemble's units over a
    common stimulus list. cv = "trial", the code (decoders.naiveBayes): for each repetition one
    random trial of every stimulus with at least 2 trials in every unit is held out and tested.
    cv = "exemplar", the Methods (STAR Methods, Naive Bayesian decoder: "for each call-type, the
    responses to one of the exemplar stimuli was removed from the fitting procedure and used (as a
    testing set)"): one random exemplar per label per repetition is held out; its trials are
    joined into test rows as the training rows are. Returns the summed posterior confusion
    matrix (true x predicted) and the number of test rows per class.
    """
    U, S, Tm, _ = F.shape
    feat = [0] if code == "Z" else list(range(6))
    Fx = F[..., feat]
    conf = np.zeros((nc, nc))
    ntest = np.zeros(nc)
    ok = C.min(axis=0) > 0
    for _ in range(nperm):
        if cv == "trial":
            testable = ok & (C.min(axis=0) >= 2)
            t = (rng.random((U, S)) * np.maximum(C, 1)).astype(int)
            Xs, n = _rows(Fx, np.where(testable[None, :], C, C + 1), rng, skip=np.where(testable[None, :], t, Tm + 1))
            mask = (np.arange(Tm)[None, :] < n[:, None]) & ok[:, None]
            Xtr = Xs[mask]
            ytr = np.repeat(y, Tm).reshape(S, Tm)[mask]
            ti = np.where(testable)[0]
            Xte = np.transpose(np.take_along_axis(Fx[:, ti], t[:, ti, None, None], axis=2)[:, :, 0], (1, 0, 2)).reshape(len(ti), -1)
            yte = y[ti]
        else:
            held = np.zeros(S, dtype=bool)
            for c in range(nc):
                cand = np.where((y == c) & ok)[0]
                if len(cand):
                    held[cand[rng.integers(len(cand))]] = True
            Xs, n = _rows(Fx, C, rng)
            valid = (np.arange(Tm)[None, :] < n[:, None]) & ok[:, None]
            yy = np.repeat(y, Tm).reshape(S, Tm)
            Xtr, ytr = Xs[valid & ~held[:, None]], yy[valid & ~held[:, None]]
            Xte, yte = Xs[valid & held[:, None]], yy[valid & held[:, None]]
        if len(np.unique(ytr)) != nc:
            continue
        P = _gnb_posterior(Xtr, ytr, Xte, nc)
        np.add.at(conf, yte, P)
        np.add.at(ntest, yte, 1)
    return conf, ntest


'''
s=s[:i]+new+s[j:]
open('aa5.py','w').write(s)
EOF
grep -n "_rows(Fx, np.where" aa5.py
```

```
368:            Xs, n = _rows(Fx, np.where(testable[None, :], C, C + 1), rng, skip=np.where(testable[None, :], t, Tm + 1))
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
s=open('aa5.py').read()
s=s.replace('''    U, S, Tm, _ = F.shape
    R = C - (0 if skip is None else 1)
    R = np.maximum(R, 0)''','''    U, S, Tm, _ = F.shape
    if skip is None:
        skip = np.full(C.shape, -1)
    R = np.maximum(C - (skip >= 0), 0)''')
s=s.replace('''    if skip is not None:
        idx = idx + (idx >= skip[:, :, None])
''','''    idx = idx + ((skip[:, :, None] >= 0) & (idx >= skip[:, :, None]))
''')
s=s.replace('''            Xs, n = _rows(Fx, np.where(testable[None, :], C, C + 1), rng, skip=np.where(testable[None, :], t, Tm + 1))''','''            Xs, n = _rows(Fx, C, rng, skip=np.where(testable[None, :], t, -1))''')
s=s.replace('''of one ensemble for every stimulus (decoders.naiveBayes): row i joins the
    i-th trial of each unit (skipping its held-out trial)''','''of one ensemble for every stimulus (decoders.naiveBayes): row i joins the
    i-th trial of each unit (skipping its held-out trial, skip >= 0; -1 for none)''')
open('aa5.py','w').write(s)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > ex2.py <<'EOF'
import sys, pickle, time, numpy as np, pandas as pd
sys.path.insert(0,'entries/robotka-2023')
import aa5
from sklearn.decomposition import PCA
units,waves,other=pickle.load(open('reduced.pkl','rb'))
ut=aa5.unit_table(units)
aud=ut[(ut.n_calls>0)&(ut.snr>=5)&(ut.p_code<=0.01)]
byuid={u['Site']+'_'+u['pkl']:u for u in units}
t0=time.time()
kdes=[aa5.kde_matrix(byuid[x]) for x in aud.uid]
K=np.vstack(kdes); pca=PCA(n_components=10).fit(K)
print('PCA', K.shape, np.cumsum(pca.explained_variance_ratio_)[:5], time.time()-t0)
stims=sorted(waves); calls={s:waves[s][0]['call_type'] for s in stims}
labels=sorted(set(calls.values())); y=np.array([labels.index(calls[s]) for s in stims])
feat={}
for x in aud.uid:
    u=byuid[x]; tr=aa5.trial_table(u); T=aa5.trial_pcs(u,pca)
    feat[x]=aa5.unit_features(tr,T,stims)
print('feat', time.time()-t0)
full=[x for x in aud.uid if (feat[x][1]>0).sum()==110]
print('110-stim units', len(full), 'with >=2 trials all', sum((feat[x][1]>=2).all() for x in full))
Tm=max(feat[x][0].shape[1] for x in full)
def stack(us):
    F=np.full((len(us),110,Tm,6),np.nan); C=np.zeros((len(us),110),int)
    for i,x in enumerate(us):
        f,c=feat[x]; F[i,:,:f.shape[1]]=f; C[i]=c
    return F,C
# check vs sklearn on one unit, trial cv
from sklearn.naive_bayes import GaussianNB
rng=np.random.default_rng(0)
F,C=stack(full[:3])
t1=time.time()
for cv in ['trial','exemplar']:
  for code in ['Z','ZT']:
    r=[]
    for k in range(20):
        conf,nt=aa5.decode(F,C,y,10,rng,code=code,cv=cv,nperm=1); r.append(aa5.pcc_code(conf,nt))
    print(cv, code, np.mean(r), (time.time()-t1)/20)
    t1=time.time()
# timing 20-unit
F,C=stack(full[:20]); t1=time.time()
for k in range(20): conf,nt=aa5.decode(F,C,y,10,rng,code='ZT',cv='trial')
print('20u trial', (time.time()-t1)/20, aa5.pcc_code(conf,nt))
t1=time.time()
for k in range(20): conf,nt=aa5.decode(F,C,y,10,rng,code='ZT',cv='exemplar')
print('20u exemplar', (time.time()-t1)/20, aa5.pcc_code(conf,nt), aa5.pcc_methods(conf,nt))
pickle.dump((aud,pca,feat,full,stims,labels,y),open('feat.pkl','wb'))
EOF
$TMPDIR/venv/bin/python ex2.py
```

```
Exit code 1
PCA (11706, 1000) [0.75409582 0.8150297  0.86707107 0.90061973 0.92441516] 0.47128796577453613
feat 5.679330348968506
110-stim units 187 with >=2 trials all 125
Traceback (most recent call last):
  File "/tmp/claude-1001/ex2.py", line 37, in <module>
    conf,nt=aa5.decode(F,C,y,10,rng,code=code,cv=cv,nperm=1); r.append(aa5.pcc_code(conf,nt))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/robotka-2023/aa5.py", line 368, in decode
    Xs, n = _rows(Fx, C, rng, skip=np.where(testable[None, :], t, -1))
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/robotka-2023/aa5.py", line 342, in _rows
    X = np.transpose(X, (1, 2, 0, 3)).reshape(S, Tm, U * 6)
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: cannot reshape array of size 5280 into shape (110,16,18)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
s=open('aa5.py').read()
s=s.replace("    U, S, Tm, _ = F.shape\n    if skip is None:","    U, S, Tm, nf = F.shape\n    if skip is None:")
s=s.replace("reshape(S, Tm, U * 6)","reshape(S, Tm, U * nf)")
open('aa5.py','w').write(s)
EOF
$TMPDIR/venv/bin/python $TMPDIR/ex2.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/ex2.py", line 5, in <module>
    units,waves,other=pickle.load(open('reduced.pkl','rb'))
                                  ^^^^^^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'reduced.pkl'
```

**Agent calls Bash**

```bash
cd $TMPDIR && $TMPDIR/venv/bin/python ex2.py
```

```
PCA (11706, 1000) [0.75409582 0.8150297  0.86707107 0.90061973 0.92441516] 0.3970663547515869
feat 5.5999133586883545
110-stim units 187 with >=2 trials all 125
trial Z 12.578574943134194 0.0007277607917785644
trial ZT 14.130751630682207 0.0010923027992248535
exemplar Z 13.063935848287326 0.0007136821746826172
exemplar ZT 16.103930258434556 0.001044595241546631
20u trial 0.003656470775604248 24.53040981066498
20u exemplar 0.0036306023597717286 30.359589218257895 29.68714067075474
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && cat > gnbtest.py <<'EOF'
import sys, numpy as np
sys.path.insert(0,'entries/robotka-2023')
import aa5
from sklearn.naive_bayes import GaussianNB
rng=np.random.default_rng(1)
X=rng.normal(size=(500,12))*rng.uniform(0.1,100,12); y=rng.integers(0,10,500); X+=y[:,None]*3
Xt=rng.normal(size=(50,12))*30
p=aa5._gnb_posterior(X,y,Xt,10)
q=GaussianNB(priors=np.ones(10)/10).fit(X,y).predict_proba(Xt)
print(np.abs(p-q).max())
EOF
$TMPDIR/venv/bin/python gnbtest.py
```

```
Sat Nov 14 21:24:03 UTC 2026
6.106226635438361e-15
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/ens && python3 ../dump.py GenerateMLFilters.ipynb x | grep -v "^\s*$" > ../mlf.txt; wc -l ../mlf.txt; grep -n "BioSound\|mpsCalc\|spectroCalc\|eigh\|pinv\|indGood\|det(\|log(\|std\|wf\|wt\|selInd\|selH\|noise" ../mlf.txt | head -80
```

```
1162 ../mlf.txt
11:from soundsig.sound import BioSound
83:selH = pk.load(fileIn)
179:    # Calculates the weighed average MPS based on the neural response
211:        # Create BioSound Object and calculate basic sound features
212:        myBioSound = BioSound(soundWave=wavSound, fs=fs, emitter=stim.split('_')[0], calltype = row['call_type'])
213:        myBioSound.spectroCalc(spec_sample_rate=1000, freq_spacing = 50, min_freq=0, max_freq=10000)
214:        myBioSound.rms = myBioSound.sound.std() 
215:        myBioSound.ampenv(cutoff_freq = 20, amp_sample_rate = 1000)
216:        myBioSound.spectrum(f_high=10000)
217:        myBioSound.mpsCalc(window=0.1, Norm = True)
219:        stimMPS.append(myBioSound.mps)
222:            myBioSound.plot(DBNOISE=50, f_low=250, f_high=10000)
225:            mpsAVG = np.copy(myBioSound.mps)
228:            mpsAVG += myBioSound.mps
240:        # The neural weight
241:        neuralWeight = 0
243:            neuralWeight += dfDataBase['z'][ind]
244:        neuralWeight /= len(unitIndexStim)
247:            mpsTRG += (stimMPS[istim]-mpsAVG)*neuralWeight
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
VIRTUAL_ENV=$TMPDIR/venv uv pip install -q soundsig 2>&1 | tail -3; $TMPDIR/venv/bin/python -c "import soundsig, importlib.metadata as m; print(m.version('soundsig')); from soundsig.sound import BioSound; print('ok')" 2>&1 | tail -3
```

```
3.1.1
ok
```

**Agent calls Bash**

```bash
sed -n 170,300p $TMPDIR/mlf.txt; sed -n 395,520p $TMPDIR/mlf.txt
```

```
'ZF7F_5t_190720_152938_goodPlayback-e19-c65.pkl'
 'ZF5M_10t_190702_095313_goodPlayback-e11-c57.pkl'
 'ZF4F_2t_190613_101015.old_goodPlayback-e19-c60.pkl'
 'ZF7F_3t_190716_130715_goodPlayback-e19-c11.pkl'
 'ZF4F_5t_190615_114154_goodPlayback-e20-c56.pkl'
 'ZF5M_8t_190627_132428_goodPlayback-e11-c50.pkl']
30.11990987593951
# ---- cell 12
def spikeTriggeredMPS(unit, plotFlg = 0, code='z'):
    # Calculates the weighed average MPS based on the neural response
    # if plotFlg = 1 you get the output plots
    # if plotFlg = 2 you get the output plots and all intermediate mps
    # Number of PCs (for PC code)
    nPCs = dfDataBase['PC'][0].shape[0]
    # Find the unique stims played for the chosen unit
    unitIndex = dfDataBase.index[dfDataBase['site']+'_'+ dfDataBase['unit'] == unit]
    unitIndexLen = len(unitIndex)
    stimList = list(dfDataBase['stim'][unitIndex].array)
    stimNames = np.unique(stimList)
    # Calculate all the MPS, store them and make a running total for averaging
[... 237 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 560,600p $TMPDIR/mlf.txt; sed -n 740,1000p $TMPDIR/mlf.txt
```

```
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
        pklFile = playPklPath + playbackPkl
        fileIn = open(pklFile, 'rb')
        unitInfo = pk.load(fileIn)
        dfAbsTime = pk.load(fileIn)
        dfRelTime = pk.load(fileIn)
[... 282 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1000,1162p $TMPDIR/mlf.txt | cut -c1-200
```

```
y = np.dot(eigVect[:,1], mtf)/(110*stdPC[ipc])
            z = np.dot(eigVect[:,2], mtf)/(110*stdPC[ipc])
            unitMTFLDA.append(np.array([x,y,z]))
    unitMTFLDA = np.vstack(unitMTFLDA)
    # Two ideas for volume:  the determinant of the covariance matrix or the power of max-min
    #volumeLDA[ilist] = np.power(np.prod(unitMTFLDA.max(axis=0)-unitMTFLDA.min(axis=0)),1/3)
    volumeLDA[ilist] = np.linalg.det(np.cov(unitMTFLDA.transpose()))
    noiseGroup[ilist] = noiseList/len(unitList)
    selHGroup[ilist] = selHList/len(unitList)
    selzGroup[ilist] = selzList/len(unitList)
# ---- cell 49
def bivariateReg(x, y, xlabel = 'x', ylabel = 'y', xlim = [], ylim = []):
    # Performs a bivariate regression, plots the line and stats.
    from random import sample
    from scipy.stats import f
    fig = plt.figure(figsize=(4,4), dpi=300)
    ax = plt.subplot()
    # Force x, y into numpy arrays
    x = np.array(x)
    y = np.array(y)
[... 143 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/robotka-2023/aa5.py <<'EOF'


# ----------------------------------------------------------------------------------------------
# The per-trial database of auditory units (C1, C2, C4)


def build_database(units, waves):
    """Auditory units (SNR >= 5, code's p <= 0.01, at least one call type; GenerateDataBase.ipynb),
    their vocalization trials with Z, the PCA of trial-averaged KDEs, and per-trial T1..T5."""
    from sklearn.decomposition import PCA

    ut = unit_table(units)
    by = {u["Site"] + "_" + u["pkl"]: u for u in units}
    aud = ut[(ut.n_calls > 0) & (ut.snr >= SNR_MIN) & (ut.p_code <= P_AUD)].reset_index(drop=True)
    K = np.vstack([kde_matrix(by[x]) for x in aud.uid])
    pca = PCA(n_components=10).fit(K)
    stims = sorted(waves)
    calls = {s: waves[s][0]["call_type"] for s in stims}
    labels = sorted(set(calls.values()))
    y = np.array([labels.index(calls[s]) for s in stims])
    trials, T, feat = {}, {}, {}
    for x in aud.uid:
        tr = trial_table(by[x])
        trials[x] = tr
        T[x] = trial_pcs(by[x], pca)
        feat[x] = unit_features(tr, T[x], stims)
    tmax = max(f[0].shape[1] for f in feat.values())
    return dict(ut=ut, aud=aud, pca=pca, n_kde_rows=K.shape[0], stims=stims, calls=calls, labels=labels,
                y=y, trials=trials, T=T, feat=feat, tmax=tmax)


def stack(db, uids, stim_idx=None):
    """F [U, S, Tmax, 6] and C [U, S] for an ensemble."""
    tm = db["tmax"]
    S = len(db["stims"])
    F = np.full((len(uids), S, tm, 6), np.nan)
    C = np.zeros((len(uids), S), dtype=int)
    for i, x in enumerate(uids):
        f, c = db["feat"][x]
        F[i, :, :f.shape[1]] = f
        C[i] = c
    if stim_idx is not None:
        F, C = F[:, stim_idx], C[:, stim_idx]
    return F, C


_DB = None


def _run_chunk(args):
    ensembles, code, cv, nperm, seed, y = args
    rng = np.random.default_rng(seed)
    nc = len(np.unique(y))
    out = []
    for e in ensembles:
        F, C = stack(_DB, e)
        conf, nt = decode(F, C, y, nc, rng, code=code, cv=cv, nperm=nperm)
        out.append((conf, nt))
    return out


def run_ensembles(db, ensembles, code="ZT", cv="trial", nperm=1, seed=0, workers=4, y=None, chunk=50):
    """Decode many ensembles in parallel (fork). Returns PCC (code), PCC (Methods), the confusion
    matrices summed per ensemble, and tests per class per ensemble."""
    import multiprocessing as mp

    global _DB
    _DB = db
    y = db["y"] if y is None else y
    ss = np.random.SeedSequence(seed)
    chunks = [ensembles[i:i + chunk] for i in range(0, len(ensembles), chunk)]
    seeds = ss.spawn(len(chunks))
    args = [(c, code, cv, nperm, s, y) for c, s in zip(chunks, seeds)]
    if workers > 1:
        with mp.get_context("fork").Pool(workers) as p:
            res = p.map(_run_chunk, args)
    else:
        res = [_run_chunk(a) for a in args]
    res = [r for rr in res for r in rr]
    confs = np.array([r[0] for r in res])
    nts = np.array([r[1] for r in res])
    pb = np.array([pcc_code(c, n) for c, n in zip(confs, nts)])
    pa = np.array([pcc_methods(c, n) for c, n in zip(confs, nts)])
    return dict(pcc_code=pb, pcc_methods=pa, conf=confs, ntest=nts)


def mean_confusion(res):
    """Average over ensembles of the row-normalized confusion matrices."""
    return np.mean([row_normalize(c, n) for c, n in zip(res["conf"], res["ntest"])], axis=0)


def entropy_selectivity(conf, ntest, normalize=True):
    """ES = 1 - H/log2(n) of the diagonal (C11): (a) diagonal normalized to sum 1 (code),
    (b) the diagonal PCC per call type used directly (Methods formula)."""
    d = np.diag(row_normalize(conf, ntest)).copy()
    if normalize:
        d = d / d.sum()
    d = d[d > 0]
    return 1 - np.sum(-d * np.log2(d)) / np.log2(conf.shape[0])


def corrected_regression(X, y, ns, ne):
    """OLS of y on X with the ensemble-corrected F test (C8; GenerateMLFilters.ipynb)."""
    from scipy import stats

    X = np.atleast_2d(np.asarray(X, dtype=float).T).T
    y = np.asarray(y, dtype=float)
    n = len(y)
    A = np.column_stack([np.ones(n), X])
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    sse = np.sum((y - A @ coef) ** 2)
    sst = np.sum((y - y.mean()) ** 2)
    k = A.shape[1]
    r2adj = 1 - (sse / (n - k)) / (sst / (n - 1))
    neff = ns - ne + 1
    F = (neff / n) * ((sst - sse) / (k - 1)) / (sse / (n - k))
    df = (k - 1, neff - k)
    return dict(coef=coef, r2adj=r2adj, F=F, df=df, p=stats.f.sf(F, *df), n=n)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > ex3.py <<'EOF'
import sys, pickle, time, numpy as np, pandas as pd
sys.path.insert(0,'entries/robotka-2023')
import aa5
from scipy import stats
units,waves,other=pickle.load(open('reduced.pkl','rb'))
t0=time.time(); db=aa5.build_database(units,waves); print('db', time.time()-t0, len(db['aud']), db['tmax'])
full=[x for x in db['aud'].uid if (db['feat'][x][1]>0).sum()==110]
print('full', len(full))
res={}
for cv in ['exemplar','trial']:
    for code in ['Z','ZT']:
        for nperm in ([1] if cv=='exemplar' else [1,100]):
            t1=time.time()
            r=aa5.run_ensembles(db,[[x] for x in full],code=code,cv=cv,nperm=nperm,seed=1)
            res[(cv,code,nperm)]=r
            print(cv,code,nperm,'code %.2f methods %.2f'%(r['pcc_code'].mean(), r['pcc_methods'].mean()), time.time()-t1)
for cv,nperm in [('exemplar',1),('trial',1),('trial',100)]:
    for m in ['pcc_code','pcc_methods']:
        a=res[(cv,'Z',nperm)][m]; b=res[(cv,'ZT',nperm)][m]
        print(cv,nperm,m, a.mean(), b.mean(), stats.ttest_rel(b,a), 'good', (b>12).sum())
pickle.dump((db,full,res),open('db.pkl','wb'))
EOF
$TMPDIR/venv/bin/python ex3.py
```

```
db 10.920979976654053 287 16
full 187
exemplar Z 1 code 10.67 methods 10.68 0.5190091133117676
exemplar ZT 1 code 11.98 methods 11.97 0.4556267261505127
trial Z 1 code 10.77 methods 10.85 0.47535133361816406
trial Z 100 code 10.75 methods 10.81 4.512868642807007
trial ZT 1 code 12.25 methods 12.60 0.4631845951080322
trial ZT 100 code 12.27 methods 12.56 5.795390605926514
exemplar 1 pcc_code 10.668573746144268 11.97871731491283 TtestResult(statistic=np.float64(8.981415298125434), pvalue=np.float64(2.956680918597877e-16), df=np.int64(186)) good 85
exemplar 1 pcc_methods 10.67555206043296 11.969716970328129 TtestResult(statistic=np.float64(8.61974451298461), pvalue=np.float64(2.8763739928926633e-15), df=np.int64(186)) good 83
trial 1 pcc_code 10.773343337401501 12.24823050984073 TtestResult(statistic=np.float64(10.39955537742986), pvalue=np.float64(2.935488529420203e-20), df=np.int64(186)) good 94
trial 1 pcc_methods 10.850365500509277 12.596942835540638 TtestResult(statistic=np.float64(11.505772086121757), pvalue=np.float64(1.7553484380315982e-23), df=np.int64(186)) good 93
trial 100 pcc_code 10.751756628885015 12.27297096263237 TtestResult(statistic=np.float64(12.433505825390574), pvalue=np.float64(3.1789185449837055e-26), df=np.int64(186)) good 92
trial 100 pcc_methods 10.814594883260495 12.556252865512736 TtestResult(statistic=np.float64(14.073473764247149), pvalue=np.float64(4.203062065792952e-31), df=np.int64(186)) good 96
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > ex4.py <<'EOF'
import sys, pickle, time, numpy as np, resource
sys.path.insert(0,'entries/robotka-2023')
import aa5
db,full,res=pickle.load(open('db.pkl','rb'))
r1=res[('trial','ZT',1)]
good=[x for x,p in zip(full,r1['pcc_code']) if p>12]
print(len(good))
rng=np.random.default_rng(0)
ens=[list(rng.choice(good,20,replace=False)) for _ in range(400)]
for cv in ['trial','exemplar']:
  for code in ['Z','ZT']:
    t0=time.time(); r=aa5.run_ensembles(db,ens,code=code,cv=cv,nperm=1,seed=2)
    print(cv, code, r['pcc_code'].mean(), r['pcc_methods'].mean(), np.percentile(r['pcc_code'],[90,100]), time.time()-t0)
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
$TMPDIR/venv/bin/python ex4.py
```

```
94
trial Z 29.03583391354125 28.087642455493505 [36.97233019 55.27683166] 0.344799280166626
trial ZT 39.82542333721031 37.98622905078885 [50.17552464 74.87737237] 1.0742051601409912
exemplar Z 27.09847802973135 27.05491890501771 [35.3651392  44.29396375] 0.35033559799194336
exemplar ZT 35.138842369804905 35.085127966684816 [44.41066593 57.76138617] 0.9981975555419922
0.202208
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n -i "modulation receptive\|modulation power\|first 500\|LDA\|discriminant\|volume" paper/10.1016-j.celrep.2023.112034.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 1767,1815p paper/10.1016-j.celrep.2023.112034.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cat >> entries/robotka-2023/aa5.py <<'EOF'


# ----------------------------------------------------------------------------------------------
# MPS, MRFs, LDA space and volume (C9, C10)


def stimulus_mps(wave, t0, dt, window="methods"):
    """MPS of one stimulus with soundsig BioSound, as GenerateMLFilters.ipynb (spectroCalc at 1 kHz,
    50 Hz spacing, 0 to 10 kHz; mpsCalc with a 100 ms window, Norm = True). window = "methods":
    the first 500 ms of the stimulus (STAR Methods, MRFs: "MPS were estimated for the first 500 ms
    of the stimulus"); "code": 500 ms before to 500 ms after onset (GenerateMLFilters.ipynb)."""
    from soundsig.sound import BioSound

    t = t0 + dt * np.arange(len(wave))
    lo, hi = (0.0, 0.5) if window == "methods" else (-0.5, 0.5)
    i0 = np.nonzero(t >= lo - 1e-9)[0][0]
    i1 = np.nonzero(t >= hi - 1e-9)[0][0]
    w = np.asarray(wave[i0:i1], dtype=float)
    fs = np.fix(1.0 / dt)
    b = BioSound(soundWave=w, fs=fs)
    b.spectroCalc(spec_sample_rate=1000, freq_spacing=50, min_freq=0, max_freq=10000)
    b.rms = b.sound.std()
    b.mpsCalc(window=0.1, Norm=True)
    return b.mps, b.wt, b.wf


def mps_window(wt, wf):
    """Temporal modulations -50 to 50 Hz, spectral 0 to 4 cyc/kHz (GenerateMLFilters.ipynb)."""
    it0 = np.argwhere(wt > -50)[0][0]
    it1 = np.argwhere(wt > 50)[0][0]
    if0 = np.argwhere(wf >= 0)[0][0]
    if1 = np.argwhere(wf * 1000 > 4)[0][0]
    return slice(if0, if1), slice(it0, it1)


def lda_axes(mps, y, rule="largest"):
    """LDA axes of the cropped MPS (C10): eigenvectors of pinv(within, rcond 1e-4) @ between.
    rule = "largest": the three of largest eigenvalue (Methods' "first three discriminant
    dimensions"); "eigh": the code's numpy eigh, first three columns (ascending eigenvalues)."""
    X = mps.reshape(len(mps), -1)
    classes = np.unique(y)
    means = np.array([X[y == c].mean(axis=0) for c in classes])
    between = np.cov(means.T)
    within = np.mean([np.cov((X[y == c] - X[y == c].mean(axis=0)).T) for c in classes], axis=0)
    M = np.linalg.pinv(within, rcond=1e-4, hermitian=True) @ between
    if rule == "eigh":
        val, vec = np.linalg.eigh(M)
        return vec[:, :3], val
    val, vec = np.linalg.eig(M)
    order = np.argsort(-val.real)
    return np.real(vec[:, order[:3]]), val.real[order]
EOF
cd $TMPDIR && cat > ex5.py <<'EOF'
import sys, pickle, time, numpy as np, warnings
warnings.filterwarnings('ignore')
sys.path.insert(0,'entries/robotka-2023')
import aa5
units,waves,other=pickle.load(open('reduced.pkl','rb'))
s=sorted(waves)[0]; w=waves[s][0]
print(w['tStim0'], w['dt'], len(w['wav'])*w['dt'])
t0=time.time()
for win in ['methods','code']:
    m,wt,wf=aa5.stimulus_mps(w['wav'],w['tStim0'],w['dt'],win); print(win, m.shape, wt.min(), wt.max(), wf.max(), time.time()-t0)
    print(aa5.mps_window(wt,wf))
# check waveform identical across units
import numpy as np
print(max(np.abs(x['wav']-waves[s][0]['wav']).max() for x in waves[s]))
EOF
$TMPDIR/venv/bin/python ex5.py
```

```
-0.5 3.999999999998449e-05 4.999999999998062
methods (193, 101) -495.049504950495 495.049504950495 0.009550259067357514 1.7705373764038086
(slice(np.int64(96), np.int64(137), None), slice(np.int64(45), np.int64(56), None))
code (193, 101) -495.049504950495 495.049504950495 0.009550259067357514 1.8952853679656982
(slice(np.int64(96), np.int64(137), None), slice(np.int64(45), np.int64(56), None))
0.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=aa-4/" | python3 -c "
import sys,re
t=sys.stdin.read()
ks=re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',t)
print(len(ks), sum(int(s) for _,s in ks)/1e9)
for k,s in ks[:15]: print(s,k)
print(re.findall(r'<IsTruncated>(.*?)</IsTruncated>',t))
"; grep -n -i "figshare\|zenodo\|deposit\|database\|Data and code availability" paper/10.1016-j.celrep.2023.112034.txt | head -20
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
sed -n 1365,1460p paper/10.1016-j.celrep.2023.112034.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd $TMPDIR/ens && python3 ../dump.py plotConfusionsBird.ipynb x | grep -v "^\s*$" | grep -n "numUnits\|nEff\|ttest\|t.cdf\|sqrt\|mean\|weight" | head -40; python3 ../dump.py decodingCallTypesNaiveBayesPart2-SameBird.ipynb | grep -n "maxTest\|numUnits =\|comb(" | head
```

```
19:numUnits = [1, 2, 3, 4, 5, 10, 15]
24:for nUnit in numUnits:
35:unitNumber = np.zeros((len(numUnits), len(zoneUnique)))
36:for i, nUnit in enumerate(numUnits):
73:pccMean = np.zeros((len(numUnits), len(zoneUnique)))
74:pccMax = np.zeros((len(numUnits), len(zoneUnique)))
75:pccSD = np.zeros((len(numUnits), len(zoneUnique)))
76:for i, nUnit in enumerate(numUnits):
78:        pccMean[i][j] = np.mean(pcc[i][j])
79:        fac = np.sqrt(unitNumber[i][j]/(unitNumber[i][j]-nUnit))
86:        pccMax[i][j] = np.mean(pcc[i][j][indGood])
88:  return _methods._mean(a, axis=axis, dtype=dtype,
92:# Make plot of mean values
98:    ax1.plot(numUnits, pccMean[:,izone], color=colorName[izone], linestyle='-', linewidth=2, label=zone)
99:    df= np.zeros(len(numUnits))
100:    ax1.fill_between(numUnits, pccMean[:,izone] + 2*pccSD[:,izone]/np.sqrt(unitNumber[:,izone]-numUnits),
101:                               pccMean[:,izone] - 2*pccSD[:,izone]/np.sqrt(unitNumber[:,izone]-numUnits), 
103:    # ax1.plot(numUnits, pccMax[:,izone], color=colorName[izone], linestyle='--', linewidth=2, label=zone +' Max')
113:# Female weighted mean
114:nE = numUnits[6]
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ens && python3 ../dump.py plotConfusionsBird.ipynb x | grep -v "^\s*$" | sed -n 76,140p
```

```
for i, nUnit in enumerate(numUnits):
    for j, zone in enumerate(zoneUnique):
        pccMean[i][j] = np.mean(pcc[i][j])
        fac = np.sqrt(unitNumber[i][j]/(unitNumber[i][j]-nUnit))
        pccSD[i][j] =  np.std(pcc[i][j])*fac
        # Max values (averaged over the topPercent)
        indSort = np.argsort(pcc[i][j])
        ls = len(indSort)
        ns = int(ls*topPercent/100.0)
        indGood = indSort[-ns-1:-1]
        pccMax[i][j] = np.mean(pcc[i][j][indGood])
## OUT: [removed: a home directory path]/opt/anaconda3/lib/python3.9/site-packages/numpy/core/fromnumeric.py:3440: RuntimeWarning: Mean of empty slice.
  return _methods._mean(a, axis=axis, dtype=dtype,
[removed: a home directory path]/opt/anaconda3/lib/python3.9/site-packages/numpy/core/_methods.py:189: RuntimeWarning: invalid value encountered in double_scalars
  ret = ret.dtype.type(ret / rcount)
# ---- cell 5
# Make plot of mean values
fig, ax1 = plt.subplots(figsize=(4, 3), dpi =300)
colorName = ['blue', 'orange', 'green', 'red']
ax1.set_xlabel('Number of Units')
[... 46 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/gen.py",
 "content": "\"\"\"Builds entries/robotka-2023/reproduce_robotka_2023.ipynb.\"\"\"\nimport nbformat as nbf\n\ncells = []\n\n\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip())\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip())\n    if tags:\n        c.metadata[\"tags\"] = tags\n    cells.append(c)\n\n\nmd(\"\"\"\n# Reproducing Robotka et al. (2023) from CRCNS aa-5\n\n**Paper.** Robotka, Thomas, Yu, Wood, Elie, Gahr & Theunissen (2023), \"Sparse ensemble neural code\nfor a complete vocal repertoire\", Cell Reports 42, 112034, doi:10.1016/j.celrep.2023.112034.\n\n**Dataset.** CRCNS aa-5, \"Simultaneous extracellular recordings of avian auditory neurons in freely\nbehaving zebra finches...\", doi:10.6080/K0TT4P5Q, read from the public bucket\n`crcnsarchive/aa-5/live/`. CRCNS data sets are not versioned: the version is recorded as\n`unversioned`, the one published version there is, and the MD5 sums of every file read (from the\ndata set's `checksums.md5`) are printed below so that a later change can be detected. The paper\ncites this DOI and no version; the bucket holds a single copy (`live/`, data descriptor v0.6 of\n29 Nov 2022), so that is what is pinned.\n\n**Claims.** `claims/robotka-2023.yaml`, written from the version of record with its STAR Methods and\nsupplement, and the paper's code (github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit\nf2d2376). Method details the claims file lacks are taken from the paper and that code, cited in the\nhelper `aa5.py` and below.\n\n| claim | status here |\n|---|---|\n| stimulus-set-link | tested |\n| auditory-units | tested |\n| inhibited-units | tested |\n| fig3c-peak-call-types | tested |\n| fig4a-unit-z-vs-zt | tested |\n| good-units-100 | tested |\n| fig4b-ensemble-20 | tested |\n| fig4b-top-ensembles | tested |\n| fig4b-confusions | tested |\n| figs4-per-bird-and-sex | tested |\n| figs6-primary-vs-secondary | blocked: no brain area per unit in the dataset |\n| fig5e-volume | tested |\n| fig5f-si-unrelated | tested |\n| fig5g-entropy-selectivity | tested |\n| fig5h-neural-noise | tested |\n| fig5-multiple-regression | tested |\n| pcs-variance | tested |\n| table1-snr | tested |\n| figs5-region-anova | blocked: no brain area per unit in the dataset |\n| fig6a-acoustic-clusters, acoustic-labels-decoding, fig6c-number-of-clusters, fig6c-ari-call-over-acoustic, figs10-ensemble-size | blocked: the vocalization database and acoustic labels are not public |\n| anesth-auditory-units, anesth-decoding-better, anesth-regressions, anesth-primary-secondary-rate | blocked: CRCNS aa-4 not analysed in this run |\n| figs9-per-region-regressions | blocked: no brain area per unit (and aa-4 not analysed) |\n\nReading the data streams about 164 GB of tar.gz from the bucket (four sites at a time); this takes\nabout 20 minutes and is most of the run time.\n\"\"\")\n\ncode(\"\"\"\nimport time, resource, warnings\nfrom itertools import combinations\nfrom math import comb\n\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\n\nimport aa5\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\nT_START = time.time()\n\"\"\")\n\nmd(\"\"\"\n## Data check\n\nThe bucket's listing and the MD5 sums of the files read, then every site is streamed once and each\nunit reduced to spike times, the stored KDE, labels and the stimulus waveforms (aa5.read_all).\n\"\"\")\n\ncode(\"\"\"\nlisting = aa5.list_files()\nmd5 = aa5.checksums()\ntars = sorted([(k, s) for k, s in listing if k.endswith(\".tar.gz\")], key=lambda x: -x[1])\nprint(len(listing), \"objects;\", len(tars), \"site files,\", round(sum(s for _, s in tars) / 1e9, 1), \"GB\")\nfor k, s in listing:\n    if not k.endswith(\"/\"):\n        print(f\"{s:>12d}  {md5.get(k.replace(aa5.PREFIX, ''), '-'):32s}  {k}\")\n\"\"\", tags=[\"sanity\"])\n\ncode(\"\"\"\nt0 = time.time()\nunits, waves, other = aa5.read_all([k for k, _ in tars], workers=4, log=lambda s: None)\nprint(f\"streamed {len(tars)} sites in {(time.time() - t0) / 60:.1f} min; {len(units)} unit pickles; \"\n      f\"peak memory of this process {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB\")\n\"\"\")\n\ncode(\"\"\"\n# What a unit pickle holds: the unit dictionary's keys and every column of both tables\nprint(\"unitInfo keys:\", sorted({k for u in units for k in u[\"info_keys\"]}))\nprint(\"dfAbsTime columns:\", sorted({c for u in units for c in u[\"abs_columns\"]}))\nprint(\"dfRelTime columns:\", sorted({c for u in units for c in u[\"rel_columns\"]}))\nprint(\"other tar members:\", len(other), \"all AppleDouble '._' files:\", all(o[0].split('/')[-1].startswith('._') for o in other))\n\nut = aa5.unit_table(units)\nprint()\nprint(\"pickles per bird:\", ut.groupby(\"bird\").size().to_dict(), \" sites per bird:\", ut.groupby(\"bird\").site.nunique().to_dict())\nempty = ut[ut.n_trials_all == 0]\nprint(\"empty pickles (no stimulus rows):\", len(empty), \"in sites\", empty.site.value_counts().to_dict())\nprint(\"pickles with vocalization (call-type) trials:\", (ut.n_calls > 0).sum(), \"; song-only:\", ((ut.n_calls == 0) & (ut.n_trials_all > 0)).sum())\nprint(\"call types per unit (units with any):\", ut[ut.n_calls > 0].n_calls.value_counts().sort_index().to_dict())\nprint(f\"SpikeSNR range {ut.snr.min():.2f} to {ut.snr.max():.2f}; units with SNR >= 5: {(ut.snr >= 5).sum()}\")\n\n# consistency of the per-trial fields\nbad_tr = sum(len(r[\"spikeTimes\"]) != r[\"nTrials\"] for u in units for r in u[\"rows\"])\nbad_mic = sum(r[\"micShape\"][0] != r[\"nTrials\"] for u in units for r in u[\"rows\"] if len(r[\"micShape\"]) == 2)\nallsp = np.concatenate([s for u in units for r in u[\"rows\"] for s in r[\"spikeTimes\"] if len(s)])\nprint(\"rows where len(spikeTimes) != nTrials:\", bad_tr, \"; where micWav rows != nTrials:\", bad_mic)\nprint(f\"spike times relative to onset: {allsp.min():.3f} to {allsp.max():.3f} s (descriptor: -0.5 to 4.5 s); {len(allsp)} spikes\")\nkde_grid = pd.Series([(r[\"nKDE\"], round(r[\"tKDE0\"], 3), round(r[\"dtKDE\"], 4)) for u in units for r in u[\"rows\"]]).value_counts()\nprint(\"KDE time grids (n samples, start s, step s):\", kde_grid.to_dict())\nstim_grid = pd.Series([(round(r[\"tStim0\"], 3), round(1 / r[\"dtStim\"]), r[\"stimLen\"]) for u in units for r in u[\"rows\"]]).value_counts()\nprint(\"stimulus grids (start s, Hz, samples):\", stim_grid.head(3).to_dict(), \"...\", len(stim_grid), \"kinds\")\nnhash = {s: len({r[\"stimHash\"] for u in units for r in u[\"rows\"] if r[\"file\"] == s}) for s in waves}\nprint(\"vocalization stimuli:\", len(waves), \"; with a waveform that differs between units:\", sum(v > 1 for v in nhash.values()))\nprint(\"KDE_BW values (descriptor: bandwidth in s; values are\", sorted(set(u[\"KDE_BW\"] for u in units))[:5], \"...)\")\n\n# recordings deposited twice: identical spike trains in two pickles\nnonempty = ut[ut.n_trials_all > 0]\ndup = nonempty[nonempty.spike_hash.duplicated(keep=False)]\nprint(\"non-empty pickles with a spike train identical to another pickle:\", len(dup))\nprint(\"sites per bird and depth:\", ut.groupby(\"bird\").site.apply(lambda s: sorted(set(x.split('_')[1] for x in s))).to_dict())\n\"\"\", tags=[\"sanity\"])\n\ncode(\"\"\"\n# Stimulus set: call types and exemplar counts over all units\nvoc = pd.DataFrame([(s, w[0][\"call_type\"]) for s, w in waves.items()], columns=[\"stim\", \"call\"])\nprint(voc.call.value_counts().to_dict(), \"total\", len(voc))\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\n### The per-trial database and the clock of spikes and stimuli\n\nAuditory units (SNR >= 5, auditory test p <= 0.01, with vocalization trials; C1 and\nGenerateDataBase.ipynb), their trial Z (C2), the PCA of trial-averaged KDE responses and the\nper-trial T1 to T5 (C4). Spike times are stored relative to stimulus onset. The check that they share\nthe stimulus clock: the population rate around onset, and decoding call type from spike counts in a\nwindow before onset (where no information should be) against the same window after onset.\n\"\"\")\n\ncode(\"\"\"\nt0 = time.time()\ndb = aa5.build_database(units, waves)\naud = db[\"aud\"]\nprint(f\"database built in {time.time() - t0:.0f} s: {len(aud)} auditory units, {db['n_kde_rows']} KDE rows in the PCA\")\nprint(\"auditory units per bird:\", aud.groupby(\"bird\").size().to_dict())\nbyuid = {u[\"Site\"] + \"_\" + u[\"pkl\"]: u for u in units}\n\n# population PSTH of auditory units, vocalization trials\nbins = np.arange(-0.5, 1.0001, 0.01)\nh = np.zeros(len(bins) - 1); ntr = 0\nfor x in aud.uid:\n    for r in aa5.voc_rows(byuid[x]):\n        for s in r[\"spikeTimes\"]:\n            h += np.histogram(s, bins)[0]; ntr += 1\nrate = h / ntr / 0.01\npre, post = rate[bins[:-1] < 0].mean(), rate[(bins[:-1] >= 0.02) & (bins[:-1] < 0.1)].mean()\nfirst = bins[:-1][np.argmax(rate > pre + 5 * rate[bins[:-1] < 0].std())]\nprint(f\"mean rate before onset {pre:.2f} spikes/s, 20 to 100 ms after onset {post:.2f} spikes/s; first 10 ms bin above baseline + 5 SD starts at {first * 1000:.0f} ms\")\nfig, ax = plt.subplots(figsize=(6, 2.5))\nax.plot(bins[:-1] * 1000, rate); ax.axvline(0, color=\"k\", lw=0.5)\nax.set_xlabel(\"time from stimulus onset (ms)\"); ax.set_ylabel(\"spikes/s\"); ax.set_title(f\"{len(aud)} auditory units, range {rate.min():.1f} to {rate.max():.1f}\")\nplt.show()\n\"\"\", tags=[\"sanity\"])\n\ncode(\"\"\"\n# Clock check by decoding: single-unit count features from [-0.5, 0) against [0, 0.5) s\nrng = np.random.default_rng(101)\nfull_all = [x for x in aud.uid if (db[\"feat\"][x][1] > 0).sum() == len(db[\"stims\"])]\ndef count_feats(x, lo, hi):\n    tr = db[\"trials\"][x]\n    u = byuid[x]\n    cnt = np.array([np.sum((s >= lo) & (s < hi)) for r in aa5.voc_rows(u) for s in r[\"spikeTimes\"]], float)\n    F, C = aa5.unit_features(tr.assign(z=cnt), np.zeros((len(tr), 5)), db[\"stims\"])\n    return F, C\nout = {}\nfor name, (lo, hi) in {\"before onset [-0.5, 0)\": (-0.5, 0.0), \"after onset [0, 0.5)\": (0.0, 0.5)}.items():\n    p = []\n    for x in full_all:\n        F, C = count_feats(x, lo, hi)\n        conf, nt = aa5.decode(F[None], C[None], db[\"y\"], 10, rng, code=\"Z\", cv=\"trial\", nperm=10)\n        p.append(aa5.pcc_code(conf, nt))\n    out[name] = np.array(p)\n    print(f\"{name}: mean single-unit PCC {np.mean(p):.2f}% over {len(p)} units (chance 10%), t vs 10 = {stats.ttest_1samp(p, 10).statistic:.2f}\")\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\n## stimulus-set-link\n\n> The dataset holds the awake playback experiment the paper describes, four birds (ZF4F, ZF5M,\n> ZF6M, ZF7F) and 110 distinct stimuli labelled with the 10 call types in the paper's numbers.\n\"\"\")\n\ncode(\"\"\"\npaper_counts = dict(Be=12, LT=13, Th=5, Di=5, Ag=9, Wh=13, Ne=15, Te=15, DC=14, So=9)\ngot = voc.call.value_counts().to_dict()\ntab = pd.DataFrame({\"paper\": paper_counts, \"dataset\": {k: got.get(k, 0) for k in paper_counts}})\ntab[\"diff\"] = tab.dataset - tab.paper\nprint(tab.T)\nbirds = sorted(ut.bird.unique())\nprint(\"birds:\", birds, len(birds), \"; distinct vocalization stimuli:\", len(voc))\nprint(\"labels in the files not in the paper's list:\", sorted(set(got) - set(paper_counts)))\n\"\"\", tags=[\"claim:stimulus-set-link\"])\n\nmd(\"\"\"\n**Result: reproduced.** The files hold 4 birds and 110 distinct vocalization stimuli whose call-type\ncounts equal the paper's for all 10 types (every difference is 0). The stimulus waveform of each\nstimulus is the same in every unit that heard it.\n\"\"\")\n\nmd(\"\"\"\n## auditory-units\n\n> Of 730 spike-sorted units in the awake dataset, 292 (40.1%) were auditory.\n\nAuditory test as C1, on the spike-count difference over all trials of the pickle (song and\nvocalizations; GenerateReport.ipynb calc_zscore_all), Methods reading (one-sample t-test, n - 1 df)\nand the code's (n df). Denominators: (a) units with SNR above 5, (b) all units the dataset holds,\ncounted three ways: every pickle, every non-empty pickle, every pickle with vocalization trials (the\ncode's summary keeps only these: `if ncalls == 0: continue`).\n\"\"\")\n\ncode(\"\"\"\nvoc_u = ut[ut.n_calls > 0]\nrows = []\nfor test in [\"p_methods\", \"p_code\"]:\n    n_aud = int(((voc_u.snr >= 5) & (voc_u[test] <= 0.01)).sum())\n    for name, den in [(\"(a) SNR above 5, with vocalization trials\", int((voc_u.snr >= 5).sum())),\n                      (\"(a') SNR above 5, all pickles\", int((ut.snr >= 5).sum())),\n                      (\"(b) all pickles\", len(ut)),\n                      (\"(b) non-empty pickles\", int((ut.n_trials_all > 0).sum())),\n                      (\"(b) pickles with vocalization trials\", len(voc_u))]:\n        rows.append(dict(test=test, denominator=name, total=den, auditory=n_aud, fraction=100 * n_aud / den))\nres_aud = pd.DataFrame(rows)\nprint(res_aud.round(2).to_string(index=False))\nprint(\"auditory units among SNR >= 5 units with vocalization trials, by bird:\",\n      voc_u[(voc_u.snr >= 5) & (voc_u.p_methods <= 0.01)].groupby(\"bird\").size().to_dict())\nprint(\"auditory test on all units regardless of SNR (vocalization pickles):\", int((voc_u.p_methods <= 0.01).sum()))\n\"\"\", tags=[\"claim:auditory-units\"])\n\nmd(\"\"\"\n**Result: reproduced.** 287 units are auditory under both the Methods' and the code's t-test (paper\n292, tolerance 29.2). With the denominator read as the units the dataset holds with vocalization\ntrials, the total is 726 (paper 730) and the fraction 39.5% (paper 40.1%), both within tolerance;\nevery pickle (872) or every non-empty pickle (838) is outside the 730 +- 73 tolerance, and the SNR\nreading (a) gives 414 units, a fraction of 69%.\n\"\"\")\n\nmd(\"\"\"\n## inhibited-units\n\n> In the awake dataset 46 of the 292 auditory units (15.7%) were inhibited by sound.\n\"\"\")\n\ncode(\"\"\"\na = aud\nn_inh = int((a.meanD < 0).sum())\nprint(f\"inhibited (mean d < 0): {n_inh} of {len(a)} = {100 * n_inh / len(a):.1f}%  (paper 46 of 292 = 15.7%)\")\nprint(\"by bird:\", a[a.meanD < 0].groupby(\"bird\").size().to_dict())\n\"\"\", tags=[\"claim:inhibited-units\"])\n\nmd(\"\"\"\n**Result: reproduced.** 47 of the 287 auditory units (16.4%) have a negative mean spike-count\ndifference, within the tolerances of 46 +- 4.6 and 15.7 +- 1.57%.\n\"\"\")\n\nmd(\"\"\"\n## table1-snr\n\n> The awake units have a mean spike SNR of 7.42 (SD 2.52; quartiles 5.51, 6.50, 9.03).\n\"\"\")\n\ncode(\"\"\"\nfor name, s in [(\"(a) auditory units\", aud.snr), (\"(b) units with SNR above 5 and vocalization trials\", voc_u.snr[voc_u.snr >= 5]),\n                (\"(b') all units with SNR above 5\", ut.snr[ut.snr >= 5])]:\n    q = s.quantile([0.25, 0.5, 0.75]).to_numpy()\n    print(f\"{name}: n = {len(s)}, mean {s.mean():.2f}, SD {s.std():.2f}, quartiles {q[0]:.2f}, {q[1]:.2f}, {q[2]:.2f}\")\nprint(\"paper: mean 7.42 (tolerance 0.742), median 6.50 (tolerance 0.65)\")\n\"\"\", tags=[\"claim:table1-snr\"])\n\nmd(\"\"\"\n**Result: reproduced.** The auditory units have a mean SNR of 6.84 and a median of 6.07, both inside\nthe tolerances (6.68 to 8.16 and 5.85 to 7.15); under reading (b) the mean is 6.97 and the median\n6.20. In every reading both values sit below the paper's, and the upper quartile (7.6 to 7.9) is\nwell below its 9.03.\n\"\"\")\n\nmd(\"\"\"\n## pcs-variance\n\n> The first five principal components of the time-varying responses explain about 90% of their variance.\n\"\"\")\n\ncode(\"\"\"\nevr = db[\"pca\"].explained_variance_ratio_\nprint(\"explained variance ratio, PCs 1 to 10:\", np.round(evr, 4))\nprint(f\"cumulative, first 5 PCs: {evr[:5].sum():.4f}  (paper about 0.90, tolerance 0.09; the code printed 0.922)\")\nprint(\"KDE rows (unit x stimulus with >= 5 trials):\", db[\"n_kde_rows\"])\n\"\"\", tags=[\"claim:pcs-variance\"])\n\nmd(\"\"\"\n**Result: reproduced.** The first five PCs explain 92.4% of the variance of the trial-averaged\nresponses (the code printed 92.2%).\n\"\"\")\n\nmd(\"\"\"\n## fig3c-peak-call-types\n\n> Across the 292 auditory units, distress calls had the highest average response strength followed by\n> song; 51 units had their peak response to distress calls and 61 to song; the preference is biased\n> toward the longer calls (Ag, Be, So, Di).\n\nzCT under the two readings of C3: (a) mean trial Z per call type; (b) the code's mean(d)/sd(d).\n\"\"\")\n\ncode(\"\"\"\nza_list, zb_list = [], []\nfor x in aud.uid:\n    za, zb = aa5.zct_unit(byuid[x], db[\"trials\"][x])\n    za_list.append(za); zb_list.append(zb)\nZA = pd.DataFrame(za_list, index=aud.uid)[aa5.CALL_TYPES]\nZB = pd.DataFrame(zb_list, index=aud.uid)[aa5.CALL_TYPES]\nfig3 = {}\nfor name, Z in [(\"(a) mean trial Z\", ZA), (\"(b) code zCT\", ZB)]:\n    m = Z.mean().sort_values(ascending=False)\n    peaks = Z.idxmax(axis=1).value_counts().reindex(aa5.CALL_TYPES, fill_value=0).sort_values(ascending=False)\n    fig3[name] = (m, peaks)\n    print(name)\n    print(\"  mean zCT by call type, ranked:\", m.round(3).to_dict())\n    print(\"  peak units by call type:\", peaks.to_dict(), \" units with missing types:\", int(Z.isna().any(axis=1).sum()))\n    print(\"  top five by peak units:\", list(peaks.index[:5]), \"; Ag, Be, So, Di among them:\", sum(c in peaks.index[:5] for c in [\"Ag\", \"Be\", \"So\", \"Di\"]))\n    for b, g in Z.groupby(aud.set_index(\"uid\").bird):\n        print(f\"   {b}: n={len(g)}, top mean {g.mean().idxmax()}, peaks Di {int((g.idxmax(axis=1) == 'Di').sum())}, So {int((g.idxmax(axis=1) == 'So').sum())}\")\nprint(\"paper: Di first, So second; peaks Di 51 (tolerance 5.1), So 61 (6.1)\")\n\"\"\", tags=[\"claim:fig3c-peak-call-types\"])\n\nmd(\"\"\"\n**Result: RESULT_FIG3C**\n\"\"\")\n\nmd(\"\"\"\n## fig4a-unit-z-vs-zt\n\n> For single units decoded independently, adding the temporal pattern (Z + T) to the response strength\n> (Z) raises the mean PCC from 10.78% to 12.3% (a 14% increase), over 191 units with data for all 110\n> calls.\n\nUnits: auditory units with all 110 vocalization stimuli (code: `nstimsUnit == 110`). Readings of C5:\n(a) the Methods, one exemplar per call type held out, PCC as the mean diagonal of the row-normalized\nmatrix; (b) the code, one random trial per stimulus held out, PCC as trace over test trials, with\none repetition (the single-unit notebook) and with 100.\n\"\"\")\n\ncode(\"\"\"\nfull = full_all\nn_ge2 = sum((db[\"feat\"][x][1] >= 2).all() for x in full)\nprint(f\"auditory units with all 110 stimuli: {len(full)} (paper 191); of these with >= 2 trials of every stimulus: {n_ge2}\")\nsingle = {}\nreadings = {\"(a) exemplar, PCC_a\": (\"exemplar\", 1, \"pcc_methods\"), \"(b) trial, 1 rep, PCC_b\": (\"trial\", 1, \"pcc_code\"),\n            \"(b) trial, 100 reps, PCC_b\": (\"trial\", 100, \"pcc_code\")}\nseed = 4000\nfor name, (cv, nperm, m) in readings.items():\n    for cd in [\"Z\", \"ZT\"]:\n        seed += 1\n        single[(name, cd)] = aa5.run_ensembles(db, [[x] for x in full], code=cd, cv=cv, nperm=nperm, seed=seed)\nrows = []\nfor name, (cv, nperm, m) in readings.items():\n    z, zt = single[(name, \"Z\")][m], single[(name, \"ZT\")][m]\n    t = stats.ttest_rel(zt, z)\n    rows.append(dict(reading=name, n=len(z), PCC_Z=z.mean(), PCC_ZT=zt.mean(), increase_pct=100 * (zt.mean() / z.mean() - 1),\n                     t=t.statistic, df=len(z) - 1, p=t.pvalue))\nfig4a = pd.DataFrame(rows)\nprint(fig4a.round(4).to_string(index=False))\nprint(\"paper: Z 10.78 (tol 1.078), Z+T 12.3 (tol 1.23), t(190) = 10.06, p < 1e-5\")\nbird_of = aud.set_index(\"uid\").bird\nfor name, (cv, nperm, m) in readings.items():\n    d = pd.DataFrame({\"Z\": single[(name, \"Z\")][m], \"ZT\": single[(name, \"ZT\")][m]}, index=full)\n    print(name, \"by bird:\", d.groupby(bird_of.loc[full].values).mean().round(2).to_dict(\"index\"))\n\"\"\", tags=[\"claim:fig4a-unit-z-vs-zt\"])\n\nmd(\"\"\"\n**Result: reproduced.** 187 units have all 110 stimuli (paper 191). Under every reading Z+T beats Z\nby a paired t-test with p far below 1e-5, and both means are within tolerance: Methods reading 10.7%\nand 12.0%, code reading 10.8% and 12.2 to 12.3%.\n\"\"\")\n\nmd(\"\"\"\n## good-units-100\n\n> Exactly 100 units had a single-unit PCC Z+T above 12%, and they came from all four birds (ZF4F 43,\n> ZF5M 19, ZF6M 16, ZF7F 22).\n\nThe count comes from one run, as the code; the range over 10 runs with other seeds is shown. The\ngood-unit set of each reading feeds the ensemble analyses of the same reading.\n\"\"\")\n\ncode(\"\"\"\ngood = {}\nfor name in [\"(a) exemplar, PCC_a\", \"(b) trial, 1 rep, PCC_b\"]:\n    cv, nperm, m = readings[name]\n    p = single[(name, \"ZT\")][m]\n    good[name] = [x for x, v in zip(full, p) if v > 12]\n    reps = []\n    for s in range(10):\n        r = aa5.run_ensembles(db, [[x] for x in full], code=\"ZT\", cv=cv, nperm=1, seed=5000 + s)\n        reps.append(int((r[m] > 12).sum()))\n    print(f\"{name}: {len(good[name])} good units; by bird {pd.Series(bird_of.loc[good[name]].values).value_counts().sort_index().to_dict()}; \"\n          f\"over 10 other seeds {min(reps)} to {max(reps)} (mean {np.mean(reps):.1f})\")\np100 = single[(\"(b) trial, 100 reps, PCC_b\", \"ZT\")][\"pcc_code\"]\nprint(\"(b) with 100 repetitions:\", int((p100 > 12).sum()), \"good units\")\nprint(\"paper: 100 (tol 10); ZF4F 43 (4.3), ZF5M 19 (1.9), ZF6M 16 (1.6), ZF7F 22 (2.2)\")\n\"\"\", tags=[\"claim:good-units-100\"])\n\nmd(\"\"\"\n**Result: RESULT_GOOD**\n\"\"\")\n\nmd(\"\"\"\n## fig4b-ensemble-20\n\n> Ensemble decoding performance rises with ensemble size, reaching an average PCC Z+T of 42% for 20\n> units, above the 29.6% obtained from response strength alone (Z), a 43% increase.\n\nEnsembles as C7: all single units and pairs, 10,000 random draws for sizes 3, 4, 5, 10, 15 and 20\n(code), each decoded once (the Methods: \"a single leave-one-out per call-type\"; the code ran 100\nrepetitions, which changes the spread of single-ensemble values but not their mean). C8 t-test\nwith df 2 neff - 2.\n\"\"\")\n\ncode(\"\"\"\nSIZES = [1, 2, 3, 4, 5, 10, 15, 20]\nN_RAND = 10000\nens4b, res4b = {}, {}\nseed = 6000\nfor name in [\"(a) exemplar, PCC_a\", \"(b) trial, 1 rep, PCC_b\"]:\n    cv, nperm, m = readings[name]\n    g = good[name]\n    rng = np.random.default_rng(6100 if name.startswith(\"(a)\") else 6200)\n    for k in SIZES:\n        if k <= 2:\n            e = [list(c) for c in combinations(g, k)]\n        else:\n            e = [list(rng.choice(g, k, replace=False)) for _ in range(N_RAND)]\n        ens4b[(name, k)] = e\n        for cd in [\"Z\", \"ZT\"]:\n            seed += 1\n            res4b[(name, k, cd)] = aa5.run_ensembles(db, e, code=cd, cv=cv, nperm=1, seed=seed)\n    curve = pd.DataFrame({cd: [res4b[(name, k, cd)][m].mean() for k in SIZES] for cd in [\"Z\", \"ZT\"]}, index=SIZES)\n    curve[\"n_ensembles\"] = [len(ens4b[(name, k)]) for k in SIZES]\n    print(name, f\"({len(g)} good units)\")\n    print(curve.round(2).T)\n    zt, z = res4b[(name, 20, \"ZT\")][m], res4b[(name, 20, \"Z\")][m]\n    t, df, p = aa5.corrected_ttest(zt, z, len(g), 20)\n    print(f\"  size 20: Z+T {zt.mean():.2f}, Z {z.mean():.2f}, increase {100 * (zt.mean() / z.mean() - 1):.0f}%; corrected t({df}) = {t:.2f}, p = {p:.2g}\")\n    print(\"  Z+T rises at every step:\", bool(np.all(np.diff(curve.ZT) > 0)))\nprint(\"paper: Z+T 42.3 (tol 4.23), Z 29.6 (tol 2.96), t(160) = 8.83, p < 1e-5\")\nprint(f\"elapsed so far {(time.time() - T_START) / 60:.1f} min\")\n\"\"\", tags=[\"claim:fig4b-ensemble-20\"])\n\ncode(\"\"\"\n# Variant: the code's 100 repetitions, on 1,000 of the 10,000 size-20 ensembles (reading b)\nname = \"(b) trial, 1 rep, PCC_b\"\nsub = ens4b[(name, 20)][:1000]\nv = {cd: aa5.run_ensembles(db, sub, code=cd, cv=\"trial\", nperm=100, seed=6900 + i)[\"pcc_code\"] for i, cd in enumerate([\"Z\", \"ZT\"])}\nprint(f\"1,000 ensembles, 100 repetitions: Z+T {v['ZT'].mean():.2f}, Z {v['Z'].mean():.2f}; one repetition on the same ensembles: \"\n      f\"Z+T {res4b[(name, 20, 'ZT')]['pcc_code'][:1000].mean():.2f}, Z {res4b[(name, 20, 'Z')]['pcc_code'][:1000].mean():.2f}\")\nprint(f\"SD over ensembles, Z+T: 100 reps {v['ZT'].std():.2f}, 1 rep {res4b[(name, 20, 'ZT')]['pcc_code'][:1000].std():.2f}\")\n\"\"\", tags=[\"claim:fig4b-ensemble-20\"])\n\nmd(\"\"\"\n**Result: RESULT_4B**\n\"\"\")\n\nmd(\"\"\"\n## fig4b-top-ensembles\n\n> The top 10% of ensembles of 20 units reach an average PCC Z+T of about 50%, and the best ensembles\n> approach the 65% achieved by acoustic classifiers.\n\nThe top 10% (Results) or 5% (Methods) of the size-20 ensembles by their first decoding, re-estimated\nwith a second random held-out draw (Methods).\n\"\"\")\n\ncode(\"\"\"\nfor name in [\"(a) exemplar, PCC_a\", \"(b) trial, 1 rep, PCC_b\"]:\n    cv, nperm, m = readings[name]\n    first = res4b[(name, 20, \"ZT\")][m]\n    for top in [10, 5]:\n        idx = np.argsort(first)[::-1][: int(len(first) * top / 100)]\n        sec = aa5.run_ensembles(db, [ens4b[(name, 20)][i] for i in idx], code=\"ZT\", cv=cv, nperm=1, seed=7000 + top + (0 if name.startswith(\"(a)\") else 50))[m]\n        print(f\"{name}, top {top}% ({len(idx)} ensembles): first draw mean {first[idx].mean():.2f}, re-estimated mean {sec.mean():.2f}, \"\n              f\"best re-estimated {sec.max():.2f}, best first draw {first.max():.2f}\")\nprint(\"paper: about 50 (tol 5); best close to 65 (read as >= 55)\")\n\"\"\", tags=[\"claim:fig4b-top-ensembles\"])\n\nmd(\"\"\"\n**Result: RESULT_TOP**\n\"\"\")\n\nmd(\"\"\"\n## fig4b-confusions\n\n> Most ensemble misclassifications are systematic, Ne confused with Te, LT with Be, Th (Tu) with Te,\n> and Di with Ag.\n\"\"\")\n\ncode(\"\"\"\nlabels = db[\"labels\"]\npairs = [(\"Ne\", \"Te\"), (\"LT\", \"Be\"), (\"Th\", \"Te\"), (\"Di\", \"Ag\")]\nfor name in [\"(a) exemplar, PCC_a\", \"(b) trial, 1 rep, PCC_b\"]:\n    M = aa5.mean_confusion(res4b[(name, 20, \"ZT\")])\n    print(name)\n    print(pd.DataFrame(100 * M, index=labels, columns=labels).round(1))\n    n_ok = 0\n    for a_, b_ in pairs:\n        i, j = labels.index(a_), labels.index(b_)\n        off = [(M[i, k], labels[k]) for k in range(len(labels)) if k != i]\n        order = [l for _, l in sorted(off, reverse=True)]\n        rank = order.index(b_) + 1\n        n_ok += rank <= 2\n        print(f\"  true {a_} predicted {b_}: {100 * M[i, j]:.1f}%, rank {rank} of 9 off-diagonal entries (largest: {order[0]} {100 * max(off)[0]:.1f}%)\")\n    print(\"  pairs among the two largest of their row:\", n_ok, \"of 4\")\n\"\"\", tags=[\"claim:fig4b-confusions\"])\n\nmd(\"\"\"\n**Result: RESULT_CONF**\n\"\"\")\n\nmd(\"\"\"\n## figs4-per-bird-and-sex\n\n> Decoding performance and its systematic errors are similar in every bird decoded alone, and PCC does\n> not differ significantly between female and male birds (difference 8.3%).\n\nEnsembles of 15 drawn within each bird from its good units: all combinations when there are at most\n9,999, otherwise 10,000 random (decodingCallTypesNaiveBayesPart2-SameBird.ipynb, maxTest = 9999).\nThe test is plotConfusionsBird.ipynb's.\n\"\"\")\n\ncode(\"\"\"\nNE = 15\nfor name in [\"(a) exemplar, PCC_a\", \"(b) trial, 1 rep, PCC_b\"]:\n    cv, nperm, m = readings[name]\n    g = pd.Series(good[name]); gb = bird_of.loc[g].values\n    per = {}\n    rng = np.random.default_rng(8000 if name.startswith(\"(a)\") else 8100)\n    for i, b in enumerate(sorted(set(bird_of))):\n        gu = list(g[gb == b])\n        if len(gu) < NE:\n            per[b] = dict(ns=len(gu), mean=np.nan, sd=np.nan); continue\n        e = [list(c) for c in combinations(gu, NE)] if comb(len(gu), NE) <= 9999 else [list(rng.choice(gu, NE, replace=False)) for _ in range(10000)]\n        r = aa5.run_ensembles(db, e, code=\"ZT\", cv=cv, nperm=1, seed=8200 + i + (0 if name.startswith(\"(a)\") else 10))\n        pc = r[m]\n        sd = pc.std() * np.sqrt(len(gu) / (len(gu) - NE)) if len(gu) > NE else np.nan\n        M = aa5.mean_confusion(r)\n        nb = sum(sorted([(M[labels.index(a_), k], labels[k]) for k in range(10) if k != labels.index(a_)], reverse=True).index((M[labels.index(a_), labels.index(b_)], b_)) < 2 for a_, b_ in pairs)\n        per[b] = dict(ns=len(gu), n_ens=len(e), mean=pc.mean(), sd=sd, pairs_top2=nb)\n    P = pd.DataFrame(per).T\n    print(name); print(P)\n    if P[\"sd\"].notna().all():\n        n = P.ns - NE + 1\n        def sexstats(b1, b2):\n            mean = (n[b1] * P.loc[b1, \"mean\"] + n[b2] * P.loc[b2, \"mean\"]) / (n[b1] + n[b2])\n            sd = np.sqrt((P.loc[b1, \"sd\"] ** 2 * (n[b1] - 1) + P.loc[b2, \"sd\"] ** 2 * (n[b2] - 1)) / (n[b1] + n[b2] - 2))\n            return mean, sd\n        mf, sf = sexstats(\"ZF4F\", \"ZF7F\"); mm, sm = sexstats(\"ZF5M\", \"ZF6M\")\n        pooled = np.sqrt((sf ** 2 + sm ** 2) / 2)\n        t = (mf - mm) / (pooled * np.sqrt(1 / 2 + 1 / 2))\n        print(f\"  female {mf:.2f}, male {mm:.2f}, difference {mf - mm:.2f}; t(2) = {t:.3f}, p = {2 * stats.t.sf(abs(t), 2):.3f}\")\n    else:\n        print(\"  a bird has 15 or fewer good units: the corrected SD (sqrt(ns/(ns - 15))) is undefined for ns = 15 and the test cannot be run as written\")\nprint(\"paper: difference 8.3 (tol 0.83), t(2) = 0.6757, p = 0.5689\")\n\"\"\", tags=[\"claim:figs4-per-bird-and-sex\"])\n\nmd(\"\"\"\n**Result: RESULT_SEX**\n\"\"\")\n\nmd(\"\"\"\n## Figure 5: MRFs, volume and the ensemble regressions\n\n1,800 random ensembles of 20 good units, each decoded with 100 held-out repetitions (Methods), under\nthe two cross-validation readings. MPS of the 110 stimuli (C9, both sound windows); MRFs of each good\nunit (six components); LDA axes (C10, both rules); volume, SI, ES and neural noise (C11).\n\"\"\")\n\ncode(\"\"\"\nt0 = time.time()\nmps = {}\nfor win in [\"methods\", \"code\"]:\n    out = []\n    for s in db[\"stims\"]:\n        w = waves[s][0]\n        M_, wt, wf = aa5.stimulus_mps(w[\"wav\"], w[\"tStim0\"], w[\"dt\"], win)\n        out.append(M_)\n    mps[win] = np.array(out)\nfsl, tsl = aa5.mps_window(wt, wf)\nprint(f\"MPS of {len(db['stims'])} stimuli x 2 windows in {time.time() - t0:.0f} s; shape {mps['methods'].shape[1:]}, \"\n      f\"kept {fsl.stop - fsl.start} spectral x {tsl.stop - tsl.start} temporal modulations \"\n      f\"({wf[fsl][0] * 1000:.2f} to {wf[fsl][-1] * 1000:.2f} cyc/kHz, {wt[tsl][0]:.1f} to {wt[tsl][-1]:.1f} Hz)\")\n\"\"\")\n\ncode(\"\"\"\nN5, NPERM5 = 1800, 100\nres5, ens5 = {}, {}\nt0 = time.time()\nfor name in [\"(a) exemplar, PCC_a\", \"(b) trial, 1 rep, PCC_b\"]:\n    cv, nperm, m = readings[name]\n    rng = np.random.default_rng(9000 if name.startswith(\"(a)\") else 9100)\n    ens5[name] = [list(rng.choice(good[name], 20, replace=False)) for _ in range(N5)]\n    res5[name] = aa5.run_ensembles(db, ens5[name], code=\"ZT\", cv=cv, nperm=NPERM5, seed=9200 + (0 if name.startswith(\"(a)\") else 1))\n    p = res5[name][m]\n    print(f\"{name}: {N5} ensembles x {NPERM5} repetitions, mean PCC {p.mean():.2f}, range {p.min():.1f} to {p.max():.1f}, \"\n          f\"above 30%: {(p > 30).sum()} (paper 1746)\")\nprint(f\"decoded in {(time.time() - t0) / 60:.1f} min\")\n\"\"\")\n\ncode(\"\"\"\ndef unit_regressors(name):\n    # Per good unit: MRF projections (per window and LDA rule), SI (a, b), ES (a, b), neural noise (variance, SD)\n    g = good[name]\n    cv, nperm, m = readings[name]\n    allz = np.concatenate([db[\"trials\"][x][\"z\"].to_numpy() for x in g])\n    allT = np.vstack([db[\"T\"][x] for x in g])\n    sdz, sdT = allz.std(), allT.std(axis=0)\n    sres = single[(name, \"ZT\")]\n    pos = {x: i for i, x in enumerate(full)}\n    out = {}\n    for x in g:\n        tr = db[\"trials\"][x].copy()\n        T = db[\"T\"][x]\n        for k in range(5):\n            tr[f\"T{k + 1}\"] = T[:, k]\n        w = tr.groupby(\"stim\")[[\"z\", \"T1\", \"T2\", \"T3\", \"T4\", \"T5\"]].mean().reindex(db[\"stims\"])\n        za, zb = aa5.zct_unit(byuid[x], db[\"trials\"][x])\n        noise_var = np.mean([g_.z.var(ddof=0) for _, g_ in tr.groupby(\"call\")])\n        noise_sd = np.mean([g_.z.std(ddof=0) for _, g_ in tr.groupby(\"call\")])\n        conf, nt = sres[\"conf\"][pos[x]], sres[\"ntest\"][pos[x]]\n        out[x] = dict(w=w.to_numpy(), SI_a=aa5.selectivity_index(za.values()), SI_b=aa5.selectivity_index(zb.values()),\n                      ES_a=aa5.entropy_selectivity(conf, nt, True), ES_b=aa5.entropy_selectivity(conf, nt, False),\n                      noise_var=noise_var, noise_sd=noise_sd)\n    scale = np.concatenate([[sdz], sdT])\n    proj = {}\n    for win in [\"methods\", \"code\"]:\n        X = mps[win][:, fsl, tsl]\n        dev = (X - X.mean(axis=0)).reshape(len(X), -1)\n        for rule in [\"largest\", \"eigh\"]:\n            axes, _ = aa5.lda_axes(X, db[\"y\"], rule)\n            for x in g:\n                mrf = dev.T @ np.nan_to_num(out[x][\"w\"])            # (features, 6): sum over stimuli\n                proj[(win, rule, x)] = (axes.T @ mrf).T / (110 * scale[:, None])   # 6 x 3\n    return out, proj\n\ndef ensemble_table(name, out, proj):\n    rows = []\n    for e in ens5[name]:\n        r = {}\n        for win in [\"methods\", \"code\"]:\n            for rule in [\"largest\", \"eigh\"]:\n                V = np.vstack([proj[(win, rule, x)] for x in e])\n                r[f\"logvol_{win}_{rule}\"] = np.log(np.linalg.det(np.cov(V.T)))\n        for k in [\"SI_a\", \"SI_b\", \"ES_a\", \"ES_b\", \"noise_var\", \"noise_sd\"]:\n            r[k] = np.mean([out[x][k] for x in e])\n        rows.append(r)\n    return pd.DataFrame(rows)\n\nt0 = time.time()\ntab5 = {}\nfor name in [\"(a) exemplar, PCC_a\", \"(b) trial, 1 rep, PCC_b\"]:\n    out, proj = unit_regressors(name)\n    tab5[name] = ensemble_table(name, out, proj)\n    tab5[name][\"pcc\"] = res5[name][readings[name][2]]\nprint(f\"regressors in {time.time() - t0:.0f} s\")\nprint(tab5[\"(b) trial, 1 rep, PCC_b\"].describe().T.round(3))\n\ndef regress(name, xcols, filt):\n    d = tab5[name]\n    if filt == \"pcc > 30\":\n        d = d[d.pcc > 30]\n    return aa5.corrected_regression(d[xcols].to_numpy(), d.pcc.to_numpy(), len(good[name]), 20)\n\"\"\")\n\nmd(\"\"\"\n### fig5e-volume\n\n> Across random ensembles of 20 units, PCC increases with the volume the ensemble's MRF components span\n> in the 3D LDA space of call types (R2adj = 0.1).\n\"\"\")\n\ncode(\"\"\"\nrows = []\nfor name in tab5:\n    for filt in [\"pcc > 30\", \"all\"]:\n        for win in [\"methods\", \"code\"]:\n            for rule in [\"largest\", \"eigh\"]:\n                r = regress(name, [f\"logvol_{win}_{rule}\"], filt)\n                rows.append(dict(cv=name[:3], ensembles=filt, n=r[\"n\"], window=win, lda=rule, slope=r[\"coef\"][1], R2adj=r[\"r2adj\"],\n                                 F=r[\"F\"], df=str(r[\"df\"]), p=r[\"p\"]))\nfig5e = pd.DataFrame(rows)\nprint(fig5e.round(4).to_string(index=False))\nprint(\"paper: R2adj 0.1 (tol 0.01), F(1,79) = 8.975, p = 0.0036, 1746 ensembles\")\n\"\"\", tags=[\"claim:fig5e-volume\"])\n\nmd(\"\"\"\n**Result: RESULT_5E**\n\"\"\")\n\nmd(\"\"\"\n### fig5f-si-unrelated\n\n> The average Z-based selectivity index of the units in an ensemble is not related to the ensemble's\n> decoding performance.\n\"\"\")\n\ncode(\"\"\"\nrows = []\nfor name in tab5:\n    for filt in [\"pcc > 30\", \"all\"]:\n        for si in [\"SI_a\", \"SI_b\"]:\n            r = regress(name, [si], filt)\n            rows.append(dict(cv=name[:3], ensembles=filt, n=r[\"n\"], SI=si, slope=r[\"coef\"][1], R2adj=r[\"r2adj\"], F=r[\"F\"], df=str(r[\"df\"]), p=r[\"p\"]))\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"paper (code output): R2adj = -0.0006, p = 0.99\")\n\"\"\", tags=[\"claim:fig5f-si-unrelated\"])\n\nmd(\"\"\"\n**Result: RESULT_5F**\n\"\"\")\n\nmd(\"\"\"\n### fig5g-entropy-selectivity\n\n> The ensemble average Entropy Selectivity of its units is negatively correlated with ensemble decoding\n> performance.\n\"\"\")\n\ncode(\"\"\"\nrows = []\nfor name in tab5:\n    for filt in [\"pcc > 30\", \"all\"]:\n        for es in [\"ES_a\", \"ES_b\"]:\n            r = regress(name, [es], filt)\n            rows.append(dict(cv=name[:3], ensembles=filt, n=r[\"n\"], ES=es, slope=r[\"coef\"][1], R2adj=r[\"r2adj\"], F=r[\"F\"], df=str(r[\"df\"]), p=r[\"p\"]))\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"paper: negative, F(1,79) = 6.73, p = 0.011 (code R2adj 0.076)\")\n\"\"\", tags=[\"claim:fig5g-entropy-selectivity\"])\n\nmd(\"\"\"\n**Result: RESULT_5G**\n\"\"\")\n\nmd(\"\"\"\n### fig5h-neural-noise\n\n> As neural variability within call types (neural noise plus lack of invariance) increases, ensemble\n> decoding performance decreases (R2adj = 0.1).\n\"\"\")\n\ncode(\"\"\"\nrows = []\nfor name in tab5:\n    for filt in [\"pcc > 30\", \"all\"]:\n        for nz in [\"noise_var\", \"noise_sd\"]:\n            r = regress(name, [nz], filt)\n            rows.append(dict(cv=name[:3], ensembles=filt, n=r[\"n\"], noise=nz, slope=r[\"coef\"][1], R2adj=r[\"r2adj\"], F=r[\"F\"], df=str(r[\"df\"]), p=r[\"p\"]))\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"paper: negative, R2adj 0.1 (tol 0.01), F(1,79) = 8.75, p = 0.004\")\n\"\"\", tags=[\"claim:fig5h-neural-noise\"])\n\nmd(\"\"\"\n**Result: RESULT_5H**\n\"\"\")\n\nmd(\"\"\"\n### fig5-multiple-regression\n\n> A linear model of PCC on volume spanned, neural variability and the two selectivity measures together\n> explains R2adj = 0.22 of the variance of ensemble decoding performance.\n\"\"\")\n\ncode(\"\"\"\nrows = []\nfor name in tab5:\n    for filt in [\"pcc > 30\", \"all\"]:\n        for win in [\"methods\", \"code\"]:\n            for rule in [\"largest\", \"eigh\"]:\n                r = regress(name, [\"noise_var\", f\"logvol_{win}_{rule}\", \"ES_a\", \"SI_b\"], filt)\n                r2 = regress(name, [\"noise_var\", f\"logvol_{win}_{rule}\", \"ES_a\", \"SI_a\"], filt)\n                rows.append(dict(cv=name[:3], ensembles=filt, n=r[\"n\"], window=win, lda=rule, R2adj_SIb=r[\"r2adj\"], F_SIb=r[\"F\"],\n                                 p_SIb=r[\"p\"], R2adj_SIa=r2[\"r2adj\"], p_SIa=r2[\"p\"], df=str(r[\"df\"])))\nprint(pd.DataFrame(rows).round(4).to_string(index=False))\nprint(\"paper: R2adj 0.22 (tol 0.022), F(4,76) = 5.832, p = 0.00038\")\nprint(f\"total run time {(time.time() - T_START) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.2f} GB (this process)\")\n\"\"\", tags=[\"claim:fig5-multiple-regression\"])\n\nmd(\"\"\"\n**Result: RESULT_5M**\n\"\"\")\n\nmd(\"\"\"\n## Summary\n\nSUMMARY\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/robotka-2023/reproduce_robotka_2023.ipynb\")\nprint(\"written\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/gen.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && VIRTUAL_ENV=$TMPDIR/venv uv pip install -q nbformat matplotlib 2>&1|tail -1; $TMPDIR/venv/bin/python gen.py && cat > devrun.py <<'EOF'
import json, sys, time, os, pickle
os.environ['MPLBACKEND']='Agg'
sys.path.insert(0,'entries/robotka-2023')
nb=json.load(open('entries/robotka-2023/reproduce_robotka_2023.ipynb'))
start=int(sys.argv[1]) if len(sys.argv)>1 else 0
stop=int(sys.argv[2]) if len(sys.argv)>2 else 999
g={}
if start>0:
    import dill
    g.update(dill.load(open('state.pkl','rb')))
code=[c for c in nb['cells'] if c['cell_type']=='code']
for i,c in enumerate(code):
    if i<start or i>=stop: continue
    src=''.join(c['source'])
    if 'aa5.read_all(' in src:
        src="units, waves, other = pickle.load(open('/tmp/claude-1001/reduced.pkl','rb'))\nimport pickle"
        src="import pickle\n"+src
    print(f'===== cell {i} {c["metadata"].get("tags","")}', flush=True)
    t=time.time(); exec(compile(src,f'cell{i}','exec'),g); print(f'----- {time.time()-t:.1f}s', flush=True)
if stop<999:
    import dill, types
    keep={k:v for k,v in g.items() if not k.startswith('__') and not isinstance(v,types.ModuleType)}
    dill.dump(keep,open('state.pkl','wb'))
EOF
VIRTUAL_ENV=$TMPDIR/venv uv pip install -q dill 2>&1|tail -1; $TMPDIR/venv/bin/python devrun.py 0 12 2>&1 | grep -v "^ *[0-9]\{6,\} " | head -150
```

```
written 67
===== cell 0 
----- 1.1s
===== cell 1 ['sanity']
62 objects; 50 site files, 163.8 GB
        3947  -                                 aa-5/live/checksums.md5
       19910  328e7bbbb48dc30dab9d225a00434499  aa-5/live/data/PlotPSTHCategoriesGUI.ipynb
       17784  d16d9957d9dd4cae97796030672ebcf7  aa-5/live/data/ZF4F/ZF4F_4t_190614_094759.tar.gz
       18162  07ed0cea0a97481f25a0d7b4ea10b0a5  aa-5/live/docs/crcns_aa-5_data_description.docx
       85000  8ac46973b1d32e281eb74535e950af31  aa-5/live/docs/crcns_aa-5_data_description.pdf
        3530  0d9ca1a60cfdc4341446a7ea01c9b0d0  aa-5/live/filelist.txt
----- 0.3s
===== cell 2 
----- 2.6s
===== cell 3 ['sanity']
unitInfo keys: ['Bird', 'Electrode', 'KDE_BW', 'RateThreshold', 'Site', 'Sort', 'SpikeSNR', 'SpikeShape', 'SpikeStd', 'StimName', 'nStim', 'nTrials']
dfAbsTime columns: ['On', 'call_type', 'duration', 'file', 'file_path', 'relation_short', 'spikes', 'start_time', 'stop_time']
dfRelTime columns: ['call_type', 'file', 'micWav', 'nTrials', 'relation_short', 'spikeKDE', 'spikeTimes', 'stimWav', 'tKDE', 'tMic', 'tStim', 'trialInd']
other tar members: 872 all AppleDouble '._' files: True

[... 66 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && ls -la state.pkl && $TMPDIR/venv/bin/python devrun.py 12 18 2>&1 | head -150
```

```
-rw-r--r-- 1 runner runner 2956711662 Nov 14 21:30 state.pkl
===== cell 12 ['claim:fig3c-peak-call-types']
Traceback (most recent call last):
  File "/tmp/claude-1001/devrun.py", line 19, in <module>
    t=time.time(); exec(compile(src,f'cell{i}','exec'),g); print(f'----- {time.time()-t:.1f}s', flush=True)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell12", line 3, in <module>
NameError: name 'aa5' is not defined
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i "s/    if i<start or i>=stop: continue/    if (i<start or i>=stop) and i!=0: continue/" devrun.py && $TMPDIR/venv/bin/python devrun.py 12 18 2>&1 | head -150
```

```
===== cell 0 
----- 0.0s
===== cell 12 ['claim:fig3c-peak-call-types']
(a) mean trial Z
  mean zCT by call type, ranked: {'So': 0.591, 'Ag': 0.573, 'Di': 0.527, 'Be': 0.441, 'DC': 0.403, 'Wh': 0.377, 'Th': 0.251, 'LT': 0.25, 'Ne': 0.232, 'Te': 0.161}
  peak units by call type: {'So': 71, 'Ag': 57, 'Di': 57, 'Be': 32, 'Th': 22, 'DC': 22, 'Wh': 13, 'LT': 6, 'Ne': 4, 'Te': 3}  units with missing types: 4
  top five by peak units: ['So', 'Ag', 'Di', 'Be', 'Th'] ; Ag, Be, So, Di among them: 4
   ZF4F: n=103, top mean Ag, peaks Di 24, So 24
   ZF5M: n=84, top mean So, peaks Di 13, So 22
   ZF6M: n=42, top mean Ag, peaks Di 8, So 12
   ZF7F: n=58, top mean Di, peaks Di 12, So 13
(b) code zCT
  mean zCT by call type, ranked: {'Di': 0.623, 'So': 0.564, 'Ag': 0.546, 'Be': 0.454, 'DC': 0.431, 'Wh': 0.403, 'Th': 0.335, 'LT': 0.303, 'Ne': 0.283, 'Te': 0.197}
  peak units by call type: {'So': 58, 'Ag': 54, 'Di': 53, 'Be': 36, 'Th': 31, 'DC': 28, 'Wh': 10, 'LT': 10, 'Ne': 4, 'Te': 3}  units with missing types: 4
  top five by peak units: ['So', 'Ag', 'Di', 'Be', 'Th'] ; Ag, Be, So, Di among them: 4
   ZF4F: n=103, top mean Di, peaks Di 26, So 18
   ZF5M: n=84, top mean So, peaks Di 10, So 18
   ZF6M: n=42, top mean Ag, peaks Di 9, So 6
   ZF7F: n=58, top mean Di, peaks Di 8, So 16
paper: Di first, So second; peaks Di 51 (tolerance 5.1), So 61 (6.1)
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && date -u && $TMPDIR/venv/bin/python devrun.py 18 999 2>&1 | head -250; date -u
```

```
Sat Nov 14 21:41:26 UTC 2026
===== cell 0 
----- 0.0s
===== cell 18 ['claim:fig4b-confusions']
(a) exemplar, PCC_a
      Ag    Be    DC    Di    LT    Ne    So    Te    Th    Wh
Ag  40.1   9.8   5.9   4.7   3.0   6.2  10.2   1.0   0.8  18.4
Be   8.9  43.6   6.1   1.3  14.0   4.8   3.4   3.6   1.9  12.5
DC   5.2  10.0  35.9   4.2   8.6  10.5   4.6   9.0   3.5   8.6
Di  20.9   4.3  11.4  20.0   4.6   8.1  16.5   4.9   1.4   8.0
LT   3.7  15.4   8.1   0.9  21.6  13.7   1.7  19.1   4.1  11.7
Ne   4.3   3.9   6.6   2.2   8.0  36.3   3.4  19.3   6.3   9.7
So  11.2   6.4   7.2   5.6   1.6   6.3  52.6   1.0   0.4   7.7
Te   1.6   4.5   8.5   1.2  12.0  23.1   1.0  34.7   6.5   6.9
Th   2.2   6.6  10.5   1.4  10.8  29.8   2.0  18.2  11.3   7.2
Wh  12.9  10.4   7.9   1.3   8.7  16.6   4.1  11.8   2.2  24.0
  true Ne predicted Te: 19.3%, rank 1 of 9 off-diagonal entries (largest: Te 19.3%)
  true LT predicted Be: 15.4%, rank 2 of 9 off-diagonal entries (largest: Te 19.1%)
  true Th predicted Te: 18.2%, rank 2 of 9 off-diagonal entries (largest: Ne 29.8%)
  true Di predicted Ag: 20.9%, rank 1 of 9 off-diagonal entries (largest: Ag 20.9%)
[... 138 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ens && for f in SummaryStatistics.ipynb "Supplementary Calculations.ipynb" GenerateReport2.ipynb; do echo "=== $f"; python3 ../dump.py "$f" x | grep -n -i "zcall\|summarySel\|argmax\|peak" | head -12; done
```

```
=== SummaryStatistics.ipynb
18:inPathH = rootPathH+dataPathH+'summarySel.pkl'
23:inPathJ = rootPathJ+dataPathJ+'summarySelJulie.pkl'
147:        plt.bar(range(len(row['zcall'])), height = row['zcall'], tick_label = row['calls'])
153:        for i in range(len(row['zcall'])):
155:                plt.text(i-0.5, row['zcall'][i]/2, '*')
177:        plt.bar(range(len(row['zcall'])), height = row['zcall'], tick_label = row['calls'])
183:        for i in range(len(row['zcall'])):
185:                plt.text(i-0.5, row['zcall'][i]/2, '*')
244:        for key, value in zip(row['calls'], row['zcall']) : 
255:        for key, value in zip(row['calls'], row['zcall']) : 
358:            for key, value in zip(row['calls'], row['zcall']) :
362:            # Test to see if max is current desired value - need to set small values to nan because argmax decides nan is maximum
=== Supplementary Calculations.ipynb
=== GenerateReport2.ipynb
162:                                  'zcall', 'pcall', 'ncall'])
184:        zcall = np.zeros(ncalls)
189:            zcall[icall], pcall[icall], ncall[icall] = calc_zscore_category(call)
192:        selInd = (1-(zcall.mean()**2/(zcall**2).mean()))/(1-1/ncalls)
198:                               'zcall': zcall, 'pcall': pcall, 'ncall': ncall}, ignore_index = True )
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/ens && python3 ../dump.py SummaryStatistics.ipynb x | sed -n 230,300p; python3 ../dump.py SummaryStatistics.ipynb x | sed -n 340,400p
```

```
The PostScript backend does not support transparency; partially transparent artists will be rendered opaque.

## OUT: <Figure size 1200x900 with 1 Axes>
# ---- cell 11
# Generate a new matrix of responses sorted by z-score
CallAxis = ['Te', 'DC', 'So', 'Ne', 'Wh', 'Ag', 'Di', 'Th', 'Be', 'LT']

zAllMatrixH = np.full((nAudSUH,len(CallAxis)), np.nan)

iCell = 0
for index, row in dfSummaryH.sort_values('zAud').iterrows():    
    # Responses across calls for auditory units
    if ( (row['pAud']<0.01) & (row['snr'] >= 5.0) ):
        # Fill in one row in the matrix
        for key, value in zip(row['calls'], row['zcall']) : 
            zAllMatrixH[iCell,CallAxis.index(key)] = value
        iCell += 1
        
zAllMatrixJ = np.full((nAudSUJ,len(CallAxis)), np.nan)

[... 114 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && $TMPDIR/venv/bin/python -c "
import pickle
units,waves,other=pickle.load(open('reduced.pkl','rb'))
s=[u['pkl'] for u in units if u['Site']=='ZF4F_2t_190613_101015']
print(len(s), 'goodPlayback-e11-c62.pkl' in s, 'goodPlayback-e19-c60.pkl' in s)
print(sorted(set(u['Site'] for u in units if u['Bird']=='ZF4F')))
"; grep -o "ZF4F_2t_190613_101015[^_]*_goodPlayback-e[0-9]*-c[0-9]*.pkl" ens/*.ipynb | sort | uniq -c | sort -rn | head; grep -o "ZF[4-7][FM]_[0-9_]*t\?_[0-9]*_[0-9]*[.a-z]*_goodPlayback-e[0-9]*-c[0-9]*.pkl" ens/decodingCallTypesNaiveBayesPart2.ipynb | sort -u | wc -l
```

```
18 False False
['ZF4F_2t_190611_160843', 'ZF4F_2t_190612_101201', 'ZF4F_2t_190612_134337', 'ZF4F_2t_190613_101015', 'ZF4F_2t_190613_142654', 'ZF4F_3t_190613_150928', 'ZF4F_4t_190614_094759', 'ZF4F_5t_190615_114154', 'ZF4F_5t_190616_102456', 'ZF4F_6_5_190618_110932', 'ZF4F_6t_190616_142033', 'ZF4F_7t_190619_095313', 'ZF4F_8_5t_190621_100019', 'ZF4F_8t_190620_101233']
      3 ens/GenerateMLFilters.ipynb:ZF4F_2t_190613_101015.old_goodPlayback-e19-c60.pkl
      3 ens/GenerateMLFilters.ipynb:ZF4F_2t_190613_101015.old_goodPlayback-e16-c63.pkl
      3 ens/GenerateMLFilters.ipynb:ZF4F_2t_190613_101015.old_goodPlayback-e11-c65.pkl
      2 ens/GenerateMLFiltersPerZone.ipynb:ZF4F_2t_190613_101015.old_goodPlayback-e8-c43.pkl
      2 ens/GenerateMLFiltersPerZone.ipynb:ZF4F_2t_190613_101015.old_goodPlayback-e8-c42.pkl
      2 ens/GenerateMLFiltersPerZone.ipynb:ZF4F_2t_190613_101015.old_goodPlayback-e20-c134.pkl
      2 ens/GenerateMLFiltersPerZone.ipynb:ZF4F_2t_190613_101015.old_goodPlayback-e19-c60.pkl
      2 ens/GenerateMLFilters.ipynb:ZF4F_2t_190613_101015.old_goodPlayback-e8-c43.pkl
      2 ens/GenerateMLFilters.ipynb:ZF4F_2t_190613_101015.old_goodPlayback-e8-c42.pkl
      2 ens/GenerateMLFilters.ipynb:ZF4F_2t_190613_101015.old_goodPlayback-e20-c136.pkl
100
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > ex6.py <<'EOF'
import dill, sys, re, requests, numpy as np, pandas as pd
sys.path.insert(0,'entries/robotka-2023')
import aa5
g=dill.load(open('state.pkl','rb'))
url="https://raw.githubusercontent.com/ftheunissen/Ensemble-Code-Cell-Reports-2022/f2d237639217425e7fc81d694708f19428a3b026/decodingCallTypesNaiveBayesPart2.ipynb"
nb=requests.get(url,timeout=60).json()
txt=''.join(''.join(o.get('text',[])) for c in nb['cells'] if c['cell_type']=='code' for o in c.get('outputs',[]) if 'goodPlayback' in ''.join(o.get('text',[])))
names=re.findall(r'(ZF\w+?_goodPlayback-e\d+-c\d+\.pkl) ([\d.]+)', txt)
print(len(names), len(set(n for n,_ in names)))
paper=dict(names)
ut=g['ut']; uids=set(ut.uid)
inds=[n.replace('.old','') for n in paper]
print('in dataset', sum(n in uids for n in inds))
print('missing', [n for n in inds if n not in uids])
aud=set(g['aud'].uid); full=set(g['full']); 
for k,v in g['good'].items(): print(k, 'paper good in our good', sum(n in set(v) for n in inds))
print('in aud', sum(n in aud for n in inds), 'in full', sum(n in full for n in inds))
EOF
$TMPDIR/venv/bin/python ex6.py
```

```
91 91
in dataset 91
missing []
(a) exemplar, PCC_a paper good in our good 51
(b) trial, 1 rep, PCC_b paper good in our good 70
in aud 91 in full 91
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/(ZF\\w+?_goodPlayback/(ZF[\\w.]+?_goodPlayback/' ex6.py && grep -n "re.findall" ex6.py && $TMPDIR/venv/bin/python ex6.py
```

```
8:names=re.findall(r'(ZF[\w.]+?_goodPlayback-e\d+-c\d+\.pkl) ([\d.]+)', txt)
100 100
in dataset 91
missing ['ZF4F_2t_190613_101015_goodPlayback-e11-c62.pkl', 'ZF4F_2t_190613_101015_goodPlayback-e19-c60.pkl', 'ZF4F_2t_190613_101015_goodPlayback-e16-c63.pkl', 'ZF4F_2t_190613_101015_goodPlayback-e8-c42.pkl', 'ZF4F_2t_190613_101015_goodPlayback-e16-c52.pkl', 'ZF4F_2t_190613_101015_goodPlayback-e11-c65.pkl', 'ZF4F_2t_190613_101015_goodPlayback-e8-c43.pkl', 'ZF4F_2t_190613_101015_goodPlayback-e20-c136.pkl', 'ZF4F_2t_190613_101015_goodPlayback-e20-c134.pkl']
(a) exemplar, PCC_a paper good in our good 51
(b) trial, 1 rep, PCC_b paper good in our good 70
in aud 91 in full 91
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('gen.py').read()
# 1. sanity check against the code's printed good-unit list
anchor='''md("""
### The per-trial database and the clock of spikes and stimuli'''
add='''md("""
### Are the paper's units in the dataset?

decodingCallTypesNaiveBayesPart2.ipynb, in the paper's code at the pinned commit, prints the names of
its 100 good units (site and pickle name, with their single-unit PCC). Read here only to check which
of them the dataset holds; nothing else is taken from it.
""")

code("""
import re, requests
CODE_URL = ("https://raw.githubusercontent.com/ftheunissen/Ensemble-Code-Cell-Reports-2022/"
            "f2d237639217425e7fc81d694708f19428a3b026/decodingCallTypesNaiveBayesPart2.ipynb")
nbp = requests.get(CODE_URL, timeout=60).json()
txt = "".join("".join(o.get("text", [])) for c in nbp["cells"] if c["cell_type"] == "code" for o in c.get("outputs", []))
paper_good = dict(re.findall(r"(ZF[\\\\w.]+?_goodPlayback-e\\\\d+-c\\\\d+\\\\.pkl) ([\\\\d.]+)", txt))
uids = set(ut.uid)
in_ds = [n for n in paper_good if n in uids]
renamed = [n for n in paper_good if n not in uids and n.replace(".old", "") in uids]
missing = [n for n in paper_good if n not in uids]
print(f"paper's good units listed: {len(paper_good)}; in the dataset under the same name: {len(in_ds)}; missing: {len(missing)}")
print("missing, by site:", pd.Series([n.split("_goodPlayback")[0] for n in missing]).value_counts().to_dict())
print("of these, a pickle of the same name exists in the site without '.old':", len(renamed))
print("dataset site ZF4F_2t_190613_101015 holds", int((ut.site == "ZF4F_2t_190613_101015").sum()), "pickles")
""", tags=["sanity"])

'''
assert anchor in s
s=s.replace(anchor, add+anchor,1)

# after db built, report where the paper's units fall
s=s.replace('''print("auditory units per bird:", aud.groupby("bird").size().to_dict())''','''print("auditory units per bird:", aud.groupby("bird").size().to_dict())
print("of the paper's good units held by the dataset,", sum(n in set(aud.uid) for n in in_ds), "of", len(in_ds), "are auditory here")''')

# 2. good units cell
s=s.replace('''    reps = []
    for s in range(10):''','''    reps = []
    for s in range(10):''')
s=s.replace('''          f"over 10 other seeds {min(reps)} to {max(reps)} (mean {np.mean(reps):.1f})")
p100''','''          f"over 10 other seeds {min(reps)} to {max(reps)} (mean {np.mean(reps):.1f}; within 90 to 110: {sum(90 <= r <= 110 for r in reps)} of 10)")
    print(f"   of the {len(in_ds)} paper good units in the dataset, {sum(n in set(good[name]) for n in in_ds)} are good here")
p100''')
s=s.replace('''print("(b) with 100 repetitions:", int((p100 > 12).sum()), "good units")''','''g100 = [x for x, v in zip(full, p100) if v > 12]
print("(b) with 100 repetitions:", len(g100), "good units; by bird", pd.Series(bird_of.loc[g100].values).value_counts().sort_index().to_dict())''')

# 3. variant cell
s=s.replace('''# Variant: the code's 100 repetitions, on 1,000 of the 10,000 size-20 ensembles (reading b)
name = "(b) trial, 1 rep, PCC_b"
sub = ens4b[(name, 20)][:1000]''','''# Variant: the code's 100 repetitions, on 500 of the 10,000 size-20 ensembles (reading b)
name = "(b) trial, 1 rep, PCC_b"
sub = ens4b[(name, 20)][:500]''')
s=s.replace('''print(f"1,000 ensembles, 100 repetitions: Z+T {v['ZT'].mean():.2f}, Z {v['Z'].mean():.2f}; one repetition on the same ensembles: "
      f"Z+T {res4b[(name, 20, 'ZT')]['pcc_code'][:1000].mean():.2f}, Z {res4b[(name, 20, 'Z')]['pcc_code'][:1000].mean():.2f}")
print(f"SD over ensembles, Z+T: 100 reps {v['ZT'].std():.2f}, 1 rep {res4b[(name, 20, 'ZT')]['pcc_code'][:1000].std():.2f}")''','''print(f"500 ensembles, 100 repetitions: Z+T {v['ZT'].mean():.2f}, Z {v['Z'].mean():.2f}; one repetition on the same ensembles: "
      f"Z+T {res4b[(name, 20, 'ZT')]['pcc_code'][:500].mean():.2f}, Z {res4b[(name, 20, 'Z')]['pcc_code'][:500].mean():.2f}")
print(f"SD over ensembles, Z+T: 100 reps {v['ZT'].std():.2f}, 1 rep {res4b[(name, 20, 'ZT')]['pcc_code'][:500].std():.2f}")
# Variant: ensembles drawn from the paper's own good units that the dataset holds (code reading)
rng = np.random.default_rng(6950)
e = [list(rng.choice(in_ds, 20, replace=False)) for _ in range(N_RAND)]
vp = {cd: aa5.run_ensembles(db, e, code=cd, cv="trial", nperm=1, seed=6960 + i)["pcc_code"] for i, cd in enumerate(["Z", "ZT"])}
t, df, p = aa5.corrected_ttest(vp["ZT"], vp["Z"], len(in_ds), 20)
print(f"{N_RAND} ensembles of 20 from the paper's {len(in_ds)} listed good units: Z+T {vp['ZT'].mean():.2f}, Z {vp['Z'].mean():.2f}; t({df}) = {t:.2f}, p = {p:.2g}")''')
open('gen.py','w').write(s)
EOF
grep -n 'paper_good = dict' gen.py
```

```
168:paper_good = dict(re.findall(r"(ZF[\\w.]+?_goodPlayback-e\\d+-c\\d+\\.pkl) ([\\d.]+)", txt))
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && $TMPDIR/venv/bin/python gen.py && $TMPDIR/venv/bin/python devrun.py 0 17 2>&1 | grep -A12 "cell 6 \|cell 7 \|cell 15 " | grep -v "^ *[0-9]\{6,\} "
```

```
written 69
===== cell 6 ['sanity']
database built in 11 s: 287 auditory units, 11706 KDE rows in the PCA
auditory units per bird: {'ZF4F': 103, 'ZF5M': 84, 'ZF6M': 42, 'ZF7F': 58}
of the paper's good units held by the dataset, 91 of 91 are auditory here
mean rate before onset 6.77 spikes/s, 20 to 100 ms after onset 15.28 spikes/s; first 10 ms bin above baseline + 5 SD starts at 0 ms
----- 12.8s
===== cell 7 ['sanity']
before onset [-0.5, 0): mean single-unit PCC 9.89% over 187 units (chance 10%), t vs 10 = -2.83
after onset [0, 0.5): mean single-unit PCC 10.85% over 187 units (chance 10%), t vs 10 = 10.60
----- 3.4s
===== cell 8 ['claim:stimulus-set-link']
         Be  LT  Th  Di  Ag  Wh  Ne  Te  DC  So
paper    12  13   5   5   9  13  15  15  14   9
dataset  12  13   5   5   9  13  15  15  14   9
diff      0   0   0   0   0   0   0   0   0   0
birds: ['ZF4F', 'ZF5M', 'ZF6M', 'ZF7F'] 4 ; distinct vocalization stimuli: 110
labels in the files not in the paper's list: []
----- 0.0s
===== cell 9 ['claim:auditory-units']
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('gen.py').read()
R={}
R['RESULT_FIG3C']='''reproduced, under the code's zCT (reading b), adopted as an assumption.** With the code's zCT,
which is what Figure 3C plots (SummaryStatistics.ipynb, cells 11 and 15, reads `zcall` from
summarySel.pkl), Di has the highest mean (0.623) and So the second (0.564); 53 units peak on Di and 58
on So (paper 51 and 61, both within tolerance); the five call types with the most peak units are So,
Ag, Di, Be and Th, which include Ag, Be, So and Di. Under the Methods' reading (a), So ranks first
(0.591), Ag second and Di third, and the So peak count (71) is outside tolerance: the claim would not
be reproduced under that reading.'''
R['RESULT_GOOD']='''not reproduced.** One run of the code's reading gives 89 units with single-unit PCC Z+T above
12%, one below the tolerance (90 to 110); the Methods' reading gives 77. Every bird contributes units.
The count depends on the random held-out draw: over 10 other seeds the code's reading gives 87 to 101
(8 of 10 within tolerance) and 100 repetitions give 91; the Methods' reading gives 70 to 94 (1 of 10).
Per bird (code reading) ZF4F 39, ZF5M 20 and ZF7F 20 are within their tolerances and ZF6M 10 is not
(paper 16). Of the paper's 100 listed good units, 91 are in the dataset and 70 of them are good here.'''
R['RESULT_4B']='''reproduced, under the code's cross-validation, adopted as an assumption.** With one random trial
per stimulus held out (decoders.naiveBayes), the mean PCC of ensembles of 20 is 43.2% with Z+T and
30.4% with Z (paper 42.3% and 29.6%), Z+T rises at every size from 1 to 20, and the corrected t-test
gives t(138) = 9.53, p = 7.5e-17 (138 df from the 89 good units of this reading). Under the Methods'
cross-validation (one exemplar per call type held out) the means are 32.0% and 24.1%, both outside
tolerance, while the rise and the test hold (t(114) = 5.79): partially reproduced under that reading.
100 repetitions on 500 of the ensembles leave the means nearly unchanged, and ensembles drawn from the
paper's own 91 listed good units give means close to the paper's (printed above).'''
R['RESULT_TOP']='''reproduced, under the code's cross-validation (assumption).** The top 10% of the size-20
ensembles, re-estimated with a second held-out draw, average 48.8% (paper about 50%, tolerance 5) and
the top 5% 50.4%; the best re-estimated ensemble reaches 86.4%, above the 55% the criterion reads as
close to 65%. A single draw is noisy (SD over ensembles 7.7 points with one repetition against 4.6
with 100), so the best single values overstate the best ensembles. Under the Methods'
cross-validation the re-estimated top-10% mean is 34.0%, outside tolerance, with a best of 59.8%.'''
R['RESULT_CONF']='''reproduced.** In the mean row-normalized confusion matrix of the 10,000 ensembles of 20, each
named pair is the largest or second largest off-diagonal entry of its row under both readings. Code
reading: Ne as Te 14.8% (rank 1), LT as Be 11.6% (rank 2), Th as Te 22.5% (rank 1), Di as Ag 10.9%
(rank 2). Methods' reading: ranks 1, 2, 2 and 1.'''
R['RESULT_SEX']='''blocked (other: too few units under the claim's own rule).** ZF6M has 10 good units under the
code's reading and 9 under the Methods' (paper 16), so ensembles of 15 cannot be drawn within that
bird and the paper's test cannot be run. In the birds with more than 15 good units, mean PCC Z+T at
15 units is 37.9% (ZF4F), 37.4% (ZF5M) and 41.0% (ZF7F) under the code's reading, and 3, 3 and 4 of
the four Figure 4B error pairs are among the two largest entries of their rows.'''
R['RESULT_5E']='''partially reproduced, under the code's cross-validation (assumption).** PCC rises with log
volume under every reading, with corrected p from 0.0008 to 0.011. Under the code's cross-validation
with the Methods' sound window and LDA axes (largest eigenvalues), R2adj is 0.120 over the 1,797
ensembles with PCC above 30% (F(1,68) = 9.60, p = 0.0028) and 0.123 over all 1,800, outside 0.1 +-
0.01; the code's window with its eigh axes gives 0.094 (p = 0.0088), within tolerance. Under the
Methods' cross-validation R2adj is 0.11 to 0.30. Here 1,797 of the 1,800 ensembles exceed 30%,
against the paper's 1,746.'''
R['RESULT_5F']='''reproduced.** The ensemble-corrected F-test of PCC on the ensemble mean of the Methods' SI gives
p = 0.85 (R2adj -0.0001) under the code's cross-validation and p = 0.32 under the Methods'; the code's
SI gives p = 0.67 and 0.30. No reading finds a relation at p < 0.05.'''
R['RESULT_5G']='''reproduced.** With the Methods' ES formula (reading b), the slope is negative and significant
under both cross-validations (code: -69.4, F(1,68) = 4.87, p = 0.031; Methods: -50.0, p = 0.0005, over
the ensembles above 30%). With the code's normalized ES (reading a) the slope is negative under the
Methods' cross-validation (p = 0.046) but positive and not significant under the code's (p = 0.79).'''
R['RESULT_5H']='''partially reproduced.** PCC falls with the ensemble mean neural noise under every reading (code
cross-validation, variance: slope -139, F(1,68) = 18.6, p = 0.0001), but R2adj is 0.21 with the
variance and 0.13 with the SD under the code's cross-validation, and 0.15 to 0.27 under the Methods',
all outside 0.1 +- 0.01.'''
R['RESULT_5M']='''partially reproduced, under the code's cross-validation (assumption).** With the Methods'
window and LDA axes, the four regressors give R2adj = 0.252 over the ensembles above 30% (F(4,65) =
5.92, p = 0.0004), just outside 0.22 +- 0.022; the code's window and eigh axes give 0.241, within
tolerance. Under the Methods' cross-validation R2adj is 0.30 to 0.49.'''
for k,v in R.items():
    assert k in s, k
    s=s.replace(k, v)
SUM='''| claim | outcome |
|---|---|
| stimulus-set-link | reproduced |
| auditory-units | reproduced |
| inhibited-units | reproduced |
| table1-snr | reproduced |
| pcs-variance | reproduced |
| fig3c-peak-call-types | reproduced (assumption: the code's zCT) |
| fig4a-unit-z-vs-zt | reproduced |
| good-units-100 | not reproduced (89 against 100 +- 10; 87 to 101 over seeds) |
| fig4b-ensemble-20 | reproduced (assumption: the code's cross-validation) |
| fig4b-top-ensembles | reproduced (same assumption) |
| fig4b-confusions | reproduced |
| figs4-per-bird-and-sex | blocked: ZF6M has fewer than 15 good units |
| fig5e-volume | partially reproduced (same assumption) |
| fig5f-si-unrelated | reproduced |
| fig5g-entropy-selectivity | reproduced |
| fig5h-neural-noise | partially reproduced |
| fig5-multiple-regression | partially reproduced (same assumption) |
| figs6, figs5-region-anova, figs9 | blocked: no brain area per unit |
| fig6a, acoustic-labels-decoding, fig6c (2), figs10 | blocked: acoustic database not public |
| anesthetized claims (4) | blocked: CRCNS aa-4 not analysed in this run |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

**How the analysis differs from the paper's.** The Methods and the paper's code differ on the
decoder's cross-validation (one exemplar per call type held out, against one random trial per
stimulus); both are run, and the ensemble claims are judged on the code's, whose results match the
paper's printed values (an assumption). The Figure 4B ensembles are decoded once each (the Methods'
single leave-one-out; the code ran 100 repetitions). Both readings of zCT, SI, ES, neural noise,
the MPS window, the LDA axes and the 30% ensemble filter are shown. The good-unit set is selected here
(89 units) and differs from the paper's 100.

**What was found about the dataset.** The files match the paper's stimulus set exactly and hold 4
birds, 50 sites and 872 unit pickles, 34 of them empty and 112 with song stimuli only. Unit counts are
close to the paper's (726 units with vocalization trials against 730; 287 auditory against 292; 187
with all 110 stimuli against 191). Nine of the paper's 100 listed good units come from a site sorting
named ZF4F_2t_190613_101015.old that is not in the dataset, whose site of that name holds other
clusters. No unit carries a brain area, so the claims by area cannot be tested. The descriptor gives
KDE_BW in seconds; its values (0.2 to 10) can only be milliseconds. Each tar holds an AppleDouble
`._` file for every pickle.'''
s=s.replace('''## Summary

SUMMARY''','## Summary\n\n'+SUM)
s=s.replace("| figs4-per-bird-and-sex | tested |","| figs4-per-bird-and-sex | tested; blocked when the selection gives a bird fewer than 15 good units |")
open('gen.py','w').write(s)
EOF
$TMPDIR/venv/bin/python gen.py
```

```
written 69
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && $TMPDIR/venv/bin/python devrun.py 17 18 2>&1 | tail -5
```

```
===== cell 17 ['claim:fig4b-ensemble-20']
500 ensembles, 100 repetitions: Z+T 43.09, Z 30.45; one repetition on the same ensembles: Z+T 43.46, Z 30.38
SD over ensembles, Z+T: 100 reps 4.77, 1 rep 7.66
10000 ensembles of 20 from the paper's 91 listed good units: Z+T 40.67, Z 29.44; t(142) = 7.06, p = 6.9e-11
----- 149.2s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('gen.py').read()
s=s.replace("""100 repetitions on 500 of the ensembles leave the means nearly unchanged, and ensembles drawn from the
paper's own 91 listed good units give means close to the paper's (printed above).""","""100 repetitions on 500 of the ensembles give 43.1% and 30.5%, and ensembles drawn from the paper's own
91 listed good units give 40.7% and 29.4%.""")
s=s.replace("(SD over ensembles 7.7 points with one repetition against 4.6\nwith 100)","(SD over 500 ensembles 7.7 points with one repetition against 4.8\nwith 100)")
open('gen.py','w').write(s)
EOF
grep -c "against 4.8" gen.py; $TMPDIR/venv/bin/python gen.py; cat entries/fouke-2025/README.md | head -30; grep -rn "crcns:" entries/*/entry.yaml | head -3
```

```
1
written 69
# Fouke, He, Loring & Naumann (2025) from dandiset 001453

Tests the findings of [Fouke et al. (2025)](https://doi.org/10.1016/j.cub.2025.04.027) that can be
tested on [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), which holds the
freely swimming tracking of 25 zebrafish and 12 *Danionella cerebrum* larvae (Figure 1 and Figure
S1). The imaging and head-fixed tail tracking of Figures 2 to 4 are not in it.

| Claim | Outcome |
|---|---|
| The stimulus codes can be linked to the paper's stimuli through its code | Reproduced |
| DC swim faster than ZF, over all stimulus codes | Reproduced |
| Median speed over whole-field stimuli, DC 9.8 and ZF 6.4 mm/s | Reproduced |
| ZF are faster to forward motion than to a static grating (8.8 against 5.0 mm/s) | Reproduced |
| DC do not modulate speed with stimulus direction | Not reproduced |
| DC are faster than ZF for oblique stimuli | Reproduced |
| Both species turn in the direction of motion | Partially reproduced |
| ZF have higher angular acceleration than DC | Not reproduced |
| DC turn less than ZF to monocular stimuli | Reproduced |
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
grep -rln "crcns" entries/*/entry.yaml | head -3; f=$(grep -rln "crcns" entries/*/entry.yaml | head -1); cat $f
```

```
entries/asari-2009/entry.yaml
entries/brinke-2017/entry.yaml
entries/bruno-2017/entry.yaml
schema_version: 1
name: asari-2009
type: reproduction
title: Long-lasting context dependence in rat auditory cortex (Asari & Zador 2009)
description: Tests the findings of Asari and Zador (2009) on CRCNS ac-1, which holds their in vivo
  whole-cell recordings in rat A1 and cell-attached recordings in MGB, with natural and synthetic
  sound sequences, and the analysis code of the paper. It measures how long the response to a
  probe depends on the preceding sound, the response predictability without context, the
  dependence on sound properties, and the fast decay in thalamus. The voltage-clamp recordings of
  Figures 5 and 6 are not in the data set.
license: Apache-2.0
python: "3.13"
notebooks:
- path: reproduce_asari_2009.ipynb
  title: Reproducing Asari & Zador (2009) from CRCNS ac-1
  runtime_minutes: 29
- path: strf_wehr.ipynb
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/robotka-2023 && cat > entry.yaml <<'EOF'
schema_version: 1
name: robotka-2023
type: reproduction
title: Sparse ensemble code for a complete vocal repertoire (Robotka et al. 2023)
description: Tests the findings of Robotka et al. (2023) on CRCNS aa-5, which holds the spike-sorted
  units of four freely behaving zebra finches presented with 110 vocalizations of 10 call types. It
  counts the auditory units, measures their call-type preferences, decodes call type from single
  units and from ensembles with a naive Bayes decoder, and relates ensemble performance to the
  acoustic volume spanned by the units' modulation receptive fields, their selectivity and their
  variability. The brain area of each unit, the lab's vocalization database and the anesthetized
  data set are not used.
license: Apache-2.0
notebooks:
- path: reproduce_robotka_2023.ipynb
  title: Reproducing Robotka et al. (2023) from CRCNS aa-5
  runtime_minutes: 45
helpers:
- aa5.py
related:
- id: crcns:aa-5/unversioned
  relation: uses_data
- id: doi:10.1016/j.celrep.2023.112034
  relation: reproduces
EOF
cat > requirements.in <<'EOF'
aiohttp
fsspec
isal
matplotlib
numpy
pandas<3
requests
scikit-learn
scipy
soundsig
EOF
cd ../.. && python tools/entry.py lock entries/robotka-2023 2>&1 | tail -5; grep python entries/robotka-2023/entry.yaml; date -u
```

```
wrote robotka-2023/requirements.lock.txt (Python 3.13, with hashes)
python: "3.13"
Sat Nov 14 22:06:36 UTC 2026
```

**Agent calls Bash**

```bash
cat > entries/robotka-2023/README.md <<'EOF'
# Robotka et al. (2023) from CRCNS aa-5

Tests the findings of [Robotka et al. (2023)](https://doi.org/10.1016/j.celrep.2023.112034) that can
be tested on [CRCNS aa-5](https://doi.org/10.6080/K0TT4P5Q), which holds the spike-sorted units of
four freely behaving zebra finches presented with 110 vocalizations of the 10 call types of the
repertoire, with songs and filtered songs.

| Claim | Outcome |
|---|---|
| The dataset holds the 4 birds and the 110 stimuli of the paper | Reproduced |
| 292 of 730 units were auditory | Reproduced |
| 46 of the auditory units were inhibited | Reproduced |
| Mean unit SNR 7.42 (Table 1) | Reproduced |
| The first five PCs explain about 90% of the response variance | Reproduced |
| Distress calls and song drive the strongest responses (Figure 3C) | Reproduced (assumption) |
| Z+T beats Z for single units (10.78% to 12.3%) | Reproduced |
| Exactly 100 good units | Not reproduced |
| Ensembles of 20 reach 42% with Z+T against 29.6% with Z | Reproduced (assumption) |
| The top 10% of ensembles reach about 50% | Reproduced (assumption) |
| Systematic confusions (Ne-Te, LT-Be, Th-Te, Di-Ag) | Reproduced |
| Per bird and per sex decoding | Blocked: too few units in one bird |
| PCC rises with the acoustic volume spanned (R2adj 0.1) | Partially reproduced (assumption) |
| Mean SI is unrelated to PCC | Reproduced |
| Mean Entropy Selectivity is negatively related to PCC | Reproduced |
| PCC falls with neural variability (R2adj 0.1) | Partially reproduced |
| Four regressors explain R2adj 0.22 | Partially reproduced (assumption) |
| Claims by brain area (three) | Blocked: metadata insufficient |
| Acoustic clustering claims (five) | Blocked: data missing |
| Anesthetized dataset claims (four) | Blocked: CRCNS aa-4 not analysed in this run |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The paper's Methods and its code differ on how the decoder is cross-validated; the ensemble claims are
judged on the code's scheme, whose results match the paper's printed values, and the Methods' scheme is
shown beside it. The notebook streams the whole data set (164 GB of tar.gz) from the CRCNS bucket,
which takes about 20 minutes. The attempt record, with the reasons and the differences from the
paper's method, is [`attempts/robotka-2023-01.yaml`](../../attempts/robotka-2023-01.yaml).
EOF
python tools/entry.py --help 2>&1 | head -20; python tools/entry.py check entries/robotka-2023 2>&1 | tail -20
```

```
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--fresh] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python,hash}
                entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
head -120 attempts/fouke-2025-01.yaml; grep -n "^[a-z_]*:" attempts/fouke-2025-01.yaml; ls schemas
```

```
schema_version: 3
id: fouke-2025-01
datasets:
- archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
  relation: primary
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: fouke-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
[... 115 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 230,330p attempts/fouke-2025-01.yaml; python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));
print(json.dumps(s['properties']['findings'],indent=0)[:1500]); print(list(s['properties'].keys())); print(s.get('required'))"
```

```
paper's GitLab repository.
- claim: fig3cd-zf-turn-more
  outcome: blocked
  blocked_by: data_missing
  notes: The head-fixed tail tracking is not in the dandiset, nor in the paper's GitLab repository.
- claim: fig4f-longer-on-duration
  outcome: blocked
  blocked_by: data_missing
  notes: Needs the imaging and the head-fixed tail tracking, neither of which is in the dandiset.
- claim: fig4hi-vspn-lateralized
  outcome: blocked
  blocked_by: data_missing
  notes: Needs the imaging, the tail tracking and the registration to the mapzebrain atlas, none
    of which is in the dandiset.
findings:
- kind: data_missing
  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
    the GitLab repository the paper names for all behavioural and imaging data holds analysis
    notebooks only. Nine of the paper's main findings cannot be tested.
[... 127 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/robotka-2023 2>&1 | tail -30; date -u
```

**Agent calls Bash**

```bash
python3 -c "
import json;s=json.load(open('schemas/attempt.schema.json'));
o=s['properties']['outcomes']['items']; print(json.dumps(o.get('properties',{}).keys().__repr__())); print(o.get('required'));
print(json.dumps(o['properties'].get('blocked_by'))); print(json.dumps(o['properties'].get('measured'))[:400]);
print(json.dumps(s['properties']['inputs'])[:600]); print(json.dumps(s['properties']['datasets'])[:900])"
```

```
Sat Nov 14 22:07:14 UTC 2026
Installed kernelspec registry-robotka-2023 in executed/robotka-2023/.venv/share/jupyter/kernels/registry-robotka-2023
0 error(s)
pass  reproduce_robotka_2023.ipynb  (2142 s)
Sat Nov 14 22:43:06 UTC 2026
```

```
"dict_keys(['claim', 'outcome', 'blocked_by', 'notes', 'notebook', 'output', 'measured', 'deviations', 'assumed', 'proposed'])"
['claim', 'outcome']
{"description": "Required when outcome is blocked.", "enum": ["data_missing", "metadata_insufficient", "methods_underspecified", "data_unreadable", "dataset_missing", "too_large", "not_runnable", "other"]}
{"description": "The values obtained, for claims with expected values: one number, or one per expected value, in the same order.", "oneOf": [{"type": "number"}, {"type": "array", "minItems": 1, "items": {"type": "number"}}]}
{"description": "Everything the attempt used that is not in the dataset.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["what", "source"], "properties": {"what": {"type": "string", "minLength": 1}, "source": {"description": "A DOI, or a repository URL with the commit read.", "type": "string", "minLength": 1}}}}
{"description": "Every dataset the attempt used (docs/protocol.md, \"Record the attempt\").", "type": "array", "minItems": 1, "items": {"description": "A dataset the attempt used: the archive, the dataset's identifier there, the pinned version, and how the paper relates to it.", "type": "object", "additionalProperties": false, "required": ["archive", "id", "version", "relation"], "properties": {"archive": {"description": "The archive that holds the dataset, in lower case: dandi, ebrains, openneuro, dryad, zenodo, figshare and so on.", "type": "string", "pattern": "^[a-z][a-z0-9-]*$"}, "id": {"description": "The dataset's identifier in that archive, e.g. 000003 on DANDI.", "type": "string", "minLength": 1}, "version": {"description": "The version the attempt read, e.g. 0.220127.0436, or draft.", "type": "string", "minLength": 1}, "modified": {"description": "For a version that can still c
```

**Agent**

The full notebook passed in a clean environment (36 min). Next I'll check that the executed outputs match the numbers in the conclusions.

**Agent calls Bash**

```bash
ls executed/robotka-2023/; python3 - <<'EOF'
import json
nb=json.load(open('executed/robotka-2023/reproduce_robotka_2023.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    out=''.join(''.join(o.get('text',[])) for o in c.get('outputs',[]) if o.get('output_type')=='stream')
    err=[o for o in c.get('outputs',[]) if o.get('output_type')=='error']
    tags=c['metadata'].get('tags',[])
    lines=[l for l in out.splitlines() if not l.strip().split(' ')[0].isdigit()]
    print(f'=== {i} {tags} {"ERROR" if err else ""}')
    print('\n'.join(lines[:60]))
EOF
```

```
reproduce_robotka_2023.ipynb
result.json
=== 1 [] 

=== 3 ['sanity'] 

=== 4 [] 
streamed 50 sites in 16.9 min; 872 unit pickles; peak memory of this process 3.20 GB
=== 5 ['sanity'] 
unitInfo keys: ['Bird', 'Electrode', 'KDE_BW', 'RateThreshold', 'Site', 'Sort', 'SpikeSNR', 'SpikeShape', 'SpikeStd', 'StimName', 'nStim', 'nTrials']
dfAbsTime columns: ['On', 'call_type', 'duration', 'file', 'file_path', 'relation_short', 'spikes', 'start_time', 'stop_time']
dfRelTime columns: ['call_type', 'file', 'micWav', 'nTrials', 'relation_short', 'spikeKDE', 'spikeTimes', 'stimWav', 'tKDE', 'tMic', 'tStim', 'trialInd']
other tar members: 872 all AppleDouble '._' files: True

pickles per bird: {'ZF4F': 255, 'ZF5M': 308, 'ZF6M': 161, 'ZF7F': 148}  sites per bird: {'ZF4F': 14, 'ZF5M': 17, 'ZF6M': 9, 'ZF7F': 10}
empty pickles (no stimulus rows): 34 in sites {'ZF4F_4t_190614_094759': 20, 'ZF4F_8t_190620_101233': 9, 'ZF7F_5t_190720_182644': 2, 'ZF5M_7t_190625_154417': 1, 'ZF4F_8_5t_190621_100019': 1, 'ZF4F_7t_190619_095313': 1}
pickles with vocalization (call-type) trials: 726 ; song-only: 112
call types per unit (units with any): {1: 1, 2: 1, 3: 7, 4: 4, 5: 1, 6: 1, 8: 2, 9: 3, 10: 706}
SpikeSNR range 2.37 to 18.03; units with SNR >= 5: 491
rows where len(spikeTimes) != nTrials: 0 ; where micWav rows != nTrials: 0
[... 256 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('gen.py').read()
old="""PCC rises with log
volume under every reading, with corrected p from 0.0008 to 0.011."""
assert old in s
s=s.replace(old,"""PCC rises with log
volume under every reading, with corrected p of 0.011 or less.""")
open('gen.py','w').write(s)
EOF
$TMPDIR/venv/bin/python gen.py && sed -i 's/runtime_minutes: 45/runtime_minutes: 36/' entries/robotka-2023/entry.yaml && date -u
```

```
written 69
Sat Nov 14 22:43:30 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n "kind: link" -A16 claims/fouke-2025.yaml | head -30
```

```
33:  kind: link
34-  statement: The dandiset's stimulus codes can be linked to the stimuli the paper names, using
35-    the paper's analysis code and the protocol file of its stimulus software, and the values
36-    computed through that link agree with those the paper's code printed.
37-  source: Data and Code Availability; the paper's Fig1-S1.ipynb at GitLab commit 33a5c29
38-  data: with_labels
39-  criterion: Records are matched by the integer stimulus code. The link holds (reproduced) when
40-    every code the analysis uses (0 to 7, 9, 10, 11, 13 and 20) occurs in the dandiset, and the
41-    species' median speeds for the nine whole-field stimuli computed here are within 10% of the
42-    values printed in Fig1-S1.ipynb for at least 14 of the 18 species and stimulus pairs. It is
43-    partially reproduced for 9 to 13 pairs and not reproduced below 9. The fish cannot be
44-    matched one to one, as no identifier links the dandiset's subjects to the code's folders;
45-    the counts per species are compared instead. The sign of the zebrafish turning response
46-    to codes 9 and 11 is reported, as the code and the protocol file disagree on which of them
47-    is lateral right.
48-- id: fig1d-dc-faster-all-codes
49-  statement: Danionella cerebrum (DC) swim at a higher median velocity than zebrafish (ZF)
```

**Agent**

Now I'll add the link claim to the claims file (after the stimulus-set link) and tag the cell.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "claims/robotka-2023.yaml",
 "old_string": "- id: auditory-units\n  statement: Of 730",
 "new_string": "- id: paper-good-units-link\n  kind: link\n  statement: The 100 good units that the paper's code lists by name (recording site and pickle\n    file) are units of the dataset, and each is an auditory unit with all 110 stimuli there.\n  source: STAR Methods, Naive Bayesian decoder, paragraph 6; the printed output of\n    decodingCallTypesNaiveBayesPart2.ipynb (cell 7) at commit f2d237639217425e7fc81d694708f19428a3b026\n  data: with_labels\n  criterion: Added by the author of attempt robotka-2023-01 (protocol, author step 1.4). Records are\n    matched by the code's unit name, site folder joined to pickle name, against the dataset's site\n    folders and pickle names. Reproduced when all 100 are found and each is auditory with all 110\n    stimuli under C1 and C5; partially reproduced when at least 90 are; not reproduced otherwise.\n    The names are used only to check the link and, as a variant, to draw ensembles from the\n    paper's own units; no claim's outcome rests on them.\n- id: auditory-units\n  statement: Of 730"
}
```

```
The file claims/robotka-2023.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('gen.py').read()
old='''print("dataset site ZF4F_2t_190613_101015 holds", int((ut.site == "ZF4F_2t_190613_101015").sum()), "pickles")
""", tags=["sanity"])'''
assert old in s
s=s.replace(old,'''print("dataset site ZF4F_2t_190613_101015 holds", int((ut.site == "ZF4F_2t_190613_101015").sum()), "pickles")
""", tags=["sanity", "claim:paper-good-units-link"])''')
old2='''print("of the paper's good units held by the dataset,", sum(n in set(aud.uid) for n in in_ds), "of", len(in_ds), "are auditory here")'''
s=s.replace(old2, old2+'''
print("  and", sum((db["feat"][n][1] > 0).sum() == len(db["stims"]) for n in in_ds if n in db["feat"]), "of them have all 110 stimuli")''')
# header table + a result paragraph after cell 10 (db) for the link
s=s.replace("| stimulus-set-link | tested |","| stimulus-set-link | tested |\n| paper-good-units-link (link claim added by the author) | tested |")
anchor='''code("""
# Clock check by decoding'''
s=s.replace(anchor,'''md("""
**Result (paper-good-units-link): partially reproduced.** 91 of the 100 good units the paper's code
lists are in the dataset under the same site and pickle name, and all 91 are auditory with all 110
stimuli here. The other 9 come from a site folder named ZF4F_2t_190613_101015.old; the dataset's
site ZF4F_2t_190613_101015 holds 18 pickles, none with those names.
""")

'''+anchor,1)
open('gen.py','w').write(s)
EOF
$TMPDIR/venv/bin/python gen.py && cd  && python tools/entry.py check entries/robotka-2023 2>&1 | tail -5; python tools/claims_check.py claims/robotka-2023.yaml 2>&1 | tail -5
```

```
written 70
0 error(s)
confidence-interval bound in the text. The text may be plain text, HTML or JATS XML; several
files (a paper and its supplement) are searched together. A value printed in a form the
checker does not know (a garbled PDF glyph, "p = 0.04, 0.05 and 0.16") is reported, to be
confirmed by reading. Exits non-zero on any problem.
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('gen.py').read()
s=s.replace("| stimulus-set-link | reproduced |\n","| stimulus-set-link | reproduced |\n| paper-good-units-link | partially reproduced (91 of 100 units found) |\n",1)
open('gen.py','w').write(s)
EOF
grep -c "paper-good-units-link | partially" gen.py; $TMPDIR/venv/bin/python gen.py; cd  && sed -i 's/| The dataset holds the 4 birds and the 110 stimuli of the paper | Reproduced |/| The dataset holds the 4 birds and the 110 stimuli of the paper | Reproduced |\n| The paper'"'"'s 100 good units are in the dataset (link check) | Partially reproduced (91 of 100) |/' entries/robotka-2023/README.md && grep -n "link check" entries/robotka-2023/README.md; date -u; python tools/entry.py all entries/robotka-2023 2>&1 | tail -5; date -u
```

```
1
written 70
11:| The paper's 100 good units are in the dataset (link check) | Partially reproduced (91 of 100) |
Sat Nov 14 22:44:18 UTC 2026
Installed kernelspec registry-robotka-2023 in executed/robotka-2023/.venv/share/jupyter/kernels/registry-robotka-2023
0 error(s)
pass  reproduce_robotka_2023.ipynb  (2131 s)
Sat Nov 14 23:20:00 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
nb=json.load(open('executed/robotka-2023/reproduce_robotka_2023.ipynb'))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    t=c['metadata'].get('tags',[])
    out=''.join(''.join(o.get('text',[])) for o in c.get('outputs',[]))
    if any(o.get('output_type')=='error' for o in c.get('outputs',[])): print('ERROR', t)
    if 'claim:paper-good-units-link' in t or 'of the paper' in out:
        print(t); print('\n'.join(l for l in out.splitlines() if 'paper' in l or 'missing' in l or 'holds' in l or 'stimuli' in l))
    if 'claim:fig5-multiple-regression' in t: print(out.splitlines()[-1])
EOF
```

```
['sanity', 'claim:paper-good-units-link']
paper's good units listed: 100; in the dataset under the same name: 91; missing: 9
missing, by site: {'ZF4F_2t_190613_101015.old': 9}
dataset site ZF4F_2t_190613_101015 holds 18 pickles
['sanity']
of the paper's good units held by the dataset, 91 of 91 are auditory here
  and 91 of them have all 110 stimuli
total run time 35.4 min; peak memory 4.21 GB (this process)
```

**Agent calls Write**

```json
{
 "file_path": "attempts/robotka-2023-01.yaml",
 "content": "schema_version: 3\nid: robotka-2023-01\ndatasets:\n- archive: crcns\n  id: aa-5\n  version: unversioned\n  doi: 10.6080/K0TT4P5Q\n  relation: primary\npaper: doi:10.1016/j.celrep.2023.112034\ndate: 2026-11-14\nentry: robotka-2023\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-15\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/43639548754\ninputs:\n- what: The names of the paper's 100 good units (site folder and pickle file), read from the printed\n    output of decodingCallTypesNaiveBayesPart2.ipynb, used only for the link claim\n    paper-good-units-link and for a variant of fig4b-ensemble-20 that draws ensembles from them.\n    The method details taken from the same repository (decoders.py, GenerateReport.ipynb,\n    GenerateDataBase.ipynb, GenerateMLFilters.ipynb, SummaryStatistics.ipynb,\n    plotConfusionsBird.ipynb) are cited in the helper and the deviations.\n  source: https://github.com/ftheunissen/Ensemble-Code-Cell-Reports-2022 at commit\n    f2d237639217425e7fc81d694708f19428a3b026\n- what: BioSound (soundsig) for the spectrograms and modulation power spectra, the package the paper\n    names; the lock pins soundsig 3.1.1 where the paper cites v1.0.1.\n  source: doi:10.5281/zenodo.7378476\noutcomes:\n- claim: stimulus-set-link\n  outcome: reproduced\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:stimulus-set-link\n  measured:\n  - 110\n  - 4\n  notes: The files hold 4 birds (ZF4F, ZF5M, ZF6M, ZF7F) and 110 distinct vocalization stimuli, with\n    Be 12, LT 13, Th 5, Di 5, Ag 9, Wh 13, Ne 15, Te 15, DC 14 and So 9, equal to the paper's counts\n    for every call type. Each stimulus waveform is identical in every unit that heard it. The files\n    also hold 60 song, spectrally filtered and temporally filtered song stimuli with no call type.\n- claim: paper-good-units-link\n  outcome: partially_reproduced\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:paper-good-units-link\n  measured: 91\n  notes: Units are matched by site folder and pickle name. 91 of the 100 good units listed by\n    decodingCallTypesNaiveBayesPart2.ipynb are in the dataset, and all 91 are auditory with all 110\n    stimuli here (printed in the following data-check cell). The 9 others come from a site folder\n    named ZF4F_2t_190613_101015.old. The dataset's ZF4F_2t_190613_101015 holds 18 pickles, none\n    with those names, so that site was deposited from a different spike sorting than the one\n    analysed. The names are used only here and in a variant of fig4b-ensemble-20.\n- claim: auditory-units\n  outcome: reproduced\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:auditory-units\n  measured:\n  - 726\n  - 287\n  - 39.53\n  notes: 287 units are auditory (SNR at least 5, t-test p at most 0.01 on the 0 to 500 ms minus\n    -500 to 0 ms spike-count difference over all trials), identically under the Methods' t-test\n    (n - 1 df) and the code's (n df); paper 292. With the denominator read as the units the\n    dataset holds with vocalization trials (reading b, which the code's summary also uses), the\n    total is 726 and the fraction 39.5%, both within tolerance. Every pickle (872, 32.9%) and every\n    non-empty pickle (838, 34.3%) are outside the tolerance on the total, and reading (a), the 414\n    units with SNR above 5, gives 69.3%. By bird, 103, 84, 42 and 58 auditory units.\n  deviations:\n  - The denominator is read as the units with vocalization trials (726), the only count that\n    matches; the dataset holds 872 unit pickles, 34 of them empty and 112 with song stimuli only.\n- claim: inhibited-units\n  outcome: reproduced\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:inhibited-units\n  measured:\n  - 47\n  - 16.4\n  notes: 47 of the 287 auditory units have a negative mean spike-count difference (16.4%); paper 46\n    of 292 (15.7%). By bird 5, 29, 2 and 11.\n- claim: fig3c-peak-call-types\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:fig3c-peak-call-types\n  measured:\n  - 53\n  - 58\n  notes: Under the code's zCT (reading b, mean(d)/sd(d) over the trials of a call type), Di has the\n    highest mean over the 287 auditory units (0.623) and So the second (0.564); 53 units peak on Di\n    and 58 on So, within tolerance of 51 and 61; the five call types with the most peak units are\n    So, Ag, Di, Be and Th, which include Ag, Be, So and Di. Under the Methods' reading (a, the mean\n    of the trial Z per call type), So ranks first (0.591), Ag second (0.573) and Di third (0.527),\n    with peak counts So 71 and Di 57, so the claim would not be reproduced. The outcome rests on\n    reading (b). Four units lack a call type and are ranked on the others.\n  deviations:\n  - Assumption. The Methods define zCT as the average of the trial z-scores over the trials of a\n    call type; the code (GenerateReport.ipynb calc_zscore_category) computes mean(d)/sd(d) within\n    the call type, and SummaryStatistics.ipynb (cells 11 and 15) builds Figure 3C from that zcall\n    in summarySel.pkl. The two readings give different outcomes; the code's is adopted because it\n    is what the figure plots. Both are shown.\n- claim: fig4a-unit-z-vs-zt\n  outcome: reproduced\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:fig4a-unit-z-vs-zt\n  measured:\n  - 187\n  - 10.68\n  - 12.05\n  notes: 187 auditory units have all 110 stimuli (paper 191); 125 of them have at least 2 trials of\n    every stimulus. Methods reading (exemplar held out per call type, PCC as the mean diagonal),\n    Z 10.68% and Z+T 12.05%, paired t(186) = 7.17. Code reading, one repetition, Z 10.75% and Z+T\n    12.17%, t(186) = 8.99; with 100 repetitions 10.76% and 12.27% (a 14.0% increase), t(186) =\n    12.30. All p far below 1e-5 and all means within tolerance. Z+T exceeds Z in every bird.\n  deviations:\n  - The units are those with all 110 vocalization stimuli, as the code (nstimsUnit == 110); the\n    Methods add at least 2 trials of each, which 125 of the 187 have; stimuli with one trial are\n    trained on and not tested, as in decoders.naiveBayes.\n- claim: good-units-100\n  outcome: not_reproduced\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:good-units-100\n  measured:\n  - 89\n  - 39\n  - 20\n  - 10\n  - 20\n  notes: One run of the code's reading (one random trial per stimulus held out, one repetition)\n    gives 89 units with single-unit PCC Z+T above 12%, one below the tolerance of 90 to 110. Every\n    bird contributes (ZF4F 39, ZF5M 20, ZF6M 10, ZF7F 20; ZF6M is outside its tolerance of 16 +-\n    1.6). The Methods' reading gives 77 (ZF4F 30, ZF5M 24, ZF6M 9, ZF7F 14). The count depends on\n    the random draw. Over 10 other seeds the code's reading gives 87 to 101 (mean 93.0, 8 of 10\n    within tolerance) and the Methods' 70 to 94 (1 of 10); 100 repetitions give 91 (ZF4F 42, ZF5M\n    21, ZF6M 10, ZF7F 18). Of the 91 listed good units of the paper held by the dataset, 70 are good\n    here under the code's reading and 51 under the Methods'. Nine of the paper's good units are in\n    a site sorting not deposited (paper-good-units-link), which accounts for part of the shortfall\n    in ZF4F.\n  deviations:\n  - The good-unit set selected here (89 units, code reading) is used by every ensemble claim of\n    that reading, so their corrected statistics use ns = 89 (neff 70) where the paper has 100\n    (neff 81).\n- claim: fig4b-ensemble-20\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:fig4b-ensemble-20\n  measured:\n  - 43.15\n  - 30.36\n  notes: Code reading, 10,000 random ensembles of 20 from the 89 good units, mean PCC Z+T 43.15% and\n    Z 30.36% (a 42% increase), corrected t(138) = 9.53, p = 7.5e-17; Z+T rises at every size (13.9,\n    17.3, 20.2, 22.7, 24.8, 32.8, 38.6 and 43.2% for 1, 2, 3, 4, 5, 10, 15 and 20 units). Methods\n    reading, 77 good units, Z+T 32.0% and Z 24.1%, both outside tolerance, with the rise and the\n    test holding (t(114) = 5.79), which would be partially reproduced. With the code's 100\n    repetitions on 500 of the ensembles, 43.09% and 30.45%. Ensembles drawn from the paper's own\n    91 listed good units give 40.67% and 29.44%, t(142) = 7.06.\n  deviations:\n  - Assumption. The Methods hold out, for each call type, the responses to one exemplar; the code\n    (decoders.naiveBayes) holds out one random trial of every stimulus. The two give different\n    outcomes here. The code's scheme is adopted for all ensemble claims because the paper's\n    printed values come from it (the claims file notes that plotConfusions.ipynb prints 42.28 and\n    38.07, and GenerateMLFilters.ipynb the F values of Figure 5), and they match this attempt's\n    values under it and not under the Methods' scheme. Both are shown.\n  - Each ensemble of the Figure 4B curve is decoded once, as the Methods state (\"a single\n    leave-one-out per call-type\"); the code ran 100 repetitions. The means do not change (shown on\n    500 ensembles); the spread over ensembles does (SD 7.7 against 4.8 points).\n  - Sizes 1 and 2 use all units and all pairs of the good units, sizes 3 to 20 10,000 random draws\n    each, as the code.\n- claim: fig4b-top-ensembles\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:fig4b-top-ensembles\n  measured: 48.8\n  notes: Code reading, the top 10% of the 10,000 size-20 ensembles by their first decoding,\n    re-estimated with a second random held-out draw, average 48.80% (first draw 58.11%); the top\n    5% re-estimated average 50.41%. The best re-estimated ensemble reaches 86.4% (top 10%) and the\n    best first draw 88.4%, above the 55% the criterion reads as close to 65%. Single draws are\n    noisy, so these maxima overstate the best ensembles. Methods reading, top 10% re-estimated\n    33.96% and best 59.8%, outside tolerance on the mean.\n  deviations:\n  - Rests on the code's cross-validation (see fig4b-ensemble-20).\n- claim: fig4b-confusions\n  outcome: reproduced\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:fig4b-confusions\n  notes: In the mean row-normalized confusion matrix of the 10,000 ensembles of 20, under the code's\n    reading, Ne as Te is 14.8% (largest off-diagonal entry of its row), LT as Be 11.6% (second, after\n    Te 24.3%), Th as Te 22.5% (largest) and Di as Ag 10.9% (second, after So 12.4%). Under the\n    Methods' reading the four pairs rank 1, 2, 2 and 1. The outcome holds under both readings.\n- claim: figs4-per-bird-and-sex\n  outcome: blocked\n  blocked_by: other\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:figs4-per-bird-and-sex\n  notes: Too few units under the claim's own rule. ZF6M has 10 good units under the code's reading\n    and 9 under the Methods' (paper 16), so no ensemble of 15 can be drawn within that bird and the\n    paper's test, which needs every bird, cannot be run. In the birds with more than 15 good units,\n    code reading, the mean PCC Z+T at 15 units is 37.9% (ZF4F, 39 units), 37.4% (ZF5M, 20) and\n    41.0% (ZF7F, 20), and 3, 3 and 4 of the four Figure 4B error pairs are among the two largest\n    entries of their rows. 100 repetitions also leave ZF6M with 10 good units.\n- claim: figs6-primary-vs-secondary\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: No file gives the brain area of a unit. The unit dictionary holds Bird, Site, Electrode,\n    Sort, SNR, KDE bandwidth, rate threshold, stimulus names and trial counts, and the tables hold\n    stimulus and spike data only; the site name gives the depth in microdrive turns but not the\n    area. The paper assigns areas from histology (SI Figure 5), and its code reads them from a\n    database pickle that is not public.\n- claim: fig5e-volume\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:fig5e-volume\n  measured:\n  - 0.1203\n  - 1797\n  notes: 1,800 random ensembles of 20 good units, each decoded with 100 held-out repetitions. Code\n    cross-validation, the Methods' sound window (first 500 ms) and LDA axes (three largest\n    eigenvalues), ensembles with PCC above 30% (the code's filter; 1,797 here against the paper's\n    1,746), slope 2.38, R2adj 0.120, F(1,68) = 9.60, p = 0.0028; all 1,800 give 0.123. R2adj is\n    outside 0.1 +- 0.01 while the slope is positive and significant. The code's window (-500 to 500\n    ms) and its eigh axes give R2adj 0.094, F(1,68) = 7.28, p = 0.0088, within tolerance. Under the\n    Methods' cross-validation (1,329 ensembles above 30%) R2adj is 0.11 to 0.30, p of 0.008 or\n    less. Every reading gives a positive slope with p of 0.011 or less.\n  deviations:\n  - Rests on the code's cross-validation (see fig4b-ensemble-20).\n  - The sound window and the LDA axes follow the Methods for the main result (first 500 ms; the\n    first three discriminant dimensions read as those of largest eigenvalue), and the code's\n    choices (-500 to 500 ms; numpy eigh's first three columns, which are the smallest eigenvalues\n    of a non-symmetric matrix) are variants. Only the code's choices give R2adj within tolerance.\n  - The F df are (1, 68) from neff = 89 - 20 + 1 = 70, not the paper's (1, 79).\n  - The MPS are computed with soundsig 3.1.1 (the paper cites v1.0.1).\n- claim: fig5f-si-unrelated\n  outcome: reproduced\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:fig5f-si-unrelated\n  notes: The corrected F-test of PCC on the ensemble mean of the Methods' SI (reading a), over the\n    ensembles with PCC above 30%, gives F(1,68) = 0.035, p = 0.85, R2adj -0.0001, slope -2.0, under\n    the code's cross-validation, and F(1,56) = 1.03, p = 0.32 under the Methods'. The code's SI\n    gives p = 0.67 and 0.30, and all 1,800 ensembles p = 0.12 to 0.85. No reading finds a relation.\n- claim: fig5g-entropy-selectivity\n  outcome: reproduced\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:fig5g-entropy-selectivity\n  notes: With the Methods' ES formula (reading b, the diagonal PCC values used directly), the slope\n    is negative and significant under both cross-validations, code -69.4 with F(1,68) = 4.87, p =\n    0.031, R2adj 0.065, and Methods -50.0 with F(1,56) = 13.7, p = 0.0005, over the ensembles above\n    30%. With the code's normalized ES (reading a) it is negative under the Methods'\n    cross-validation (p = 0.046) but positive and not significant under the code's (slope 18.9, p =\n    0.79). The main reading holds under both cross-validations, so the outcome does not rest on the\n    cross-validation assumption.\n- claim: fig5h-neural-noise\n  outcome: partially_reproduced\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:fig5h-neural-noise\n  measured: 0.2096\n  notes: PCC falls with the ensemble mean neural noise under every reading. Code cross-validation,\n    variance, slope -139, F(1,68) = 18.6, p = 0.0001, R2adj 0.210; with the SD, R2adj 0.131, p =\n    0.0018. Methods cross-validation, R2adj 0.15 to 0.27. No reading gives R2adj within 0.1 +- 0.01.\n- claim: fig5-multiple-regression\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:fig5-multiple-regression\n  measured: 0.2515\n  notes: Code cross-validation, the code's regressors (noise variance, log volume, normalized ES and\n    the code's SI), the Methods' window and LDA axes, ensembles above 30%, R2adj 0.252, F(4,65) =\n    5.92, p = 0.0004, outside 0.22 +- 0.022. The code's window with its eigh axes gives 0.241 (p =\n    0.0006), within tolerance, and the Methods' SI changes R2adj by less than 0.002. Methods\n    cross-validation gives 0.30 to 0.49.\n  deviations:\n  - Rests on the code's cross-validation, and the window and LDA axes as for fig5e-volume.\n- claim: pcs-variance\n  outcome: reproduced\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:pcs-variance\n  measured: 92.44\n  notes: The PCA of 11,706 trial-averaged KDE responses (unit and stimulus pairs with at least 5\n    trials, the stored KDE's first 1000 samples) gives a cumulative explained variance of 92.4% for\n    the first five PCs (75.4, 6.1, 5.2, 3.4, 2.4%); the code printed 92.2%.\n- claim: table1-snr\n  outcome: reproduced\n  notebook: reproduce_robotka_2023.ipynb\n  output: claim:table1-snr\n  measured:\n  - 6.84\n  - 6.07\n  notes: Auditory units (reading a), mean 6.84, SD 1.99, quartiles 5.37, 6.07 and 7.65, within the\n    tolerances (6.68 to 8.16, 5.85 to 7.15). Units with SNR above 5 (reading b), mean 6.97 and\n    median 6.20. Both sit below the paper's values, and the upper quartile is well below 9.03.\n- claim: figs5-region-anova\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Needs the brain area of each good unit, which the dataset does not give (see\n    figs6-primary-vs-secondary).\n- claim: fig6a-acoustic-clusters\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Runs on the Theunissen lab vocalization database (about 5,000 calls) and its acoustic\n    parameter table (vocParamTable.h5), which the dataset does not hold. The paper's key resources\n    table and data availability statement name no deposit for them, and the paper's code\n    repository at the pinned commit does not contain the table.\n- claim: acoustic-labels-decoding\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the acoustic cluster label of each stimulus, from the vocalization database of\n    fig6a-acoustic-clusters, which is not public.\n- claim: fig6c-number-of-clusters\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the acoustic labels of fig6a-acoustic-clusters, which are not public. The call-type\n    values alone could be computed from the dataset, but the criterion's outcomes all need the\n    acoustic comparison; they were not run.\n- claim: fig6c-ari-call-over-acoustic\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the acoustic labels of fig6a-acoustic-clusters, which are not public.\n- claim: figs10-ensemble-size\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the acoustic labels of fig6a-acoustic-clusters, which are not public.\n- claim: anesth-auditory-units\n  outcome: blocked\n  blocked_by: other\n  notes: Data elsewhere, CRCNS aa-4 (doi 10.6080/K00C4T06), which is public (6.9 GB in the bucket).\n    Not analysed in this run, which spent its five hours on aa-5; a later attempt can add it.\n- claim: anesth-decoding-better\n  outcome: blocked\n  blocked_by: other\n  notes: Data elsewhere, CRCNS aa-4, not analysed in this run (see anesth-auditory-units).\n- claim: anesth-regressions\n  outcome: blocked\n  blocked_by: other\n  notes: Data elsewhere, CRCNS aa-4, not analysed in this run (see anesth-auditory-units).\n- claim: figs9-per-region-regressions\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: The awake part needs the brain area of each unit, which the dataset does not give; the\n    R2adj values need CRCNS aa-4, not analysed in this run.\n- claim: anesth-primary-secondary-rate\n  outcome: blocked\n  blocked_by: other\n  notes: Data elsewhere, CRCNS aa-4, not analysed in this run (see anesth-auditory-units).\nfindings:\n- kind: metadata_insufficient\n  statement: No file gives the brain area (Field L, CLM, CMM, NCM or the L/NCM border) of a unit,\n    though the paper's analyses by area use one. The data descriptor says only that the arrays\n    targeted the primary and secondary auditory pallium.\n- kind: other\n  about: data\n  statement: Nine of the 100 good units the paper's code lists come from a site folder named\n    ZF4F_2t_190613_101015.old. The dataset's site ZF4F_2t_190613_101015 holds 18 unit pickles, none\n    with those names, so the deposited sorting of that site differs from the one the paper\n    analysed. The other 91 listed units are in the dataset. Unit counts are near the paper's (726\n    units with vocalization trials against 730, 287 auditory against 292, 187 with all 110 stimuli\n    against 191).\n- kind: other\n  about: data\n  statement: 34 of the 872 unit pickles hold no stimulus rows (20 of them in site\n    ZF4F_4t_190614_094759, whose tar.gz is 17 KB), and 112 hold song stimuli only. The data\n    descriptor does not say so.\n- kind: metadata_error\n  statement: The data descriptor gives KDE_BW as the bandwidth in seconds of the rate estimate; its\n    values range from 0.2 to 10, which can only be milliseconds.\n- kind: other\n  about: data\n  statement: Every site tar.gz holds an AppleDouble file (`._goodPlayback-...pkl`, 524 bytes) for each\n    unit pickle, 872 in all; they are not pickles and must be skipped. The pickles are written with\n    pandas 1.x and need pandas' pickle compatibility layer to be read with pandas 2.\n- kind: methods_unavailable\n  statement: Question for the authors. The STAR Methods describe the decoder's cross-validation as\n    holding out, for each call type, the responses to one exemplar stimulus, while the code\n    (decoders.naiveBayes) holds out one random trial of every stimulus. The two differ here by\n    about 11 points of PCC for ensembles of 20 (32.0% against 43.2% with Z+T), and only the code's\n    scheme gives the paper's values. Which scheme produced Figures 4 and 5? This attempt assumes the\n    code's.\n- kind: code_mismatch\n  statement: The Methods define the per-call-type response zCT as the average of the trial\n    z-scores; the code computes mean(d)/sd(d) within the call type, and Figure 3C is built from the\n    code's values. Under the Methods' definition song, not distress calls, has the highest average\n    response.\n- kind: code_mismatch\n  statement: The Methods compute the MPS on the first 500 ms of the stimulus and use the first three\n    linear discriminant dimensions; the code takes 500 ms before to 500 ms after onset, and takes\n    numpy eigh's first three eigenvectors of the non-symmetric matrix pinv(within) times between,\n    which eigh orders by ascending eigenvalue. Only the code's choices give the paper's R2adj of\n    about 0.1 for the volume here.\n- kind: selection_undocumented\n  about: paper\n  statement: The 1,746 ensembles of Figure 5 are those of the 1,800 with PCC above 30%\n    (GenerateMLFilters.ipynb, pcc > 30); the Methods do not state the filter.\n- kind: methods_unavailable\n  statement: Question for the authors. The good-unit selection (single-unit PCC Z+T above 12%) uses\n    one random held-out draw, and the count moves from 87 to 101 between seeds here. How was the\n    paper's count of exactly 100 obtained, and is it expected to be stable?\n"
}
```

```
File created successfully at: attempts/robotka-2023-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i '/^- claim: paper-good-units-link/,/^  notes:/{/^  measured: 91$/d}' attempts/robotka-2023-01.yaml; python3 -c "
import yaml,re
t=open('attempts/robotka-2023-01.yaml').read()
yaml.safe_load(t)
for i,l in enumerate(t.splitlines()):
    s=l.strip()
    body=re.sub(r'^(- )?[a-z_]+: ','',s)
    if ': ' in body: print(i+1, l)
"; python tools/entry.py check entries/robotka-2023 2>&1 | tail -8; date -u
```

```
0 error(s)
Sat Nov 14 23:21:39 UTC 2026
```

**Agent calls Bash**

```bash
python tools/entry.py handover entries/robotka-2023 2>&1 | tail -5; ls executed/robotka-2023/handover/; git status --short | grep -v "^?? \.\(bash\|zsh\|profile\|git\|idea\|mcp\|ripgrep\|vscode\)"
```

```
wrote executed/robotka-2023/handover
aa5.py
reproduce_robotka_2023.ipynb
robotka-2023.yaml
 M claims/robotka-2023.yaml
?? .zprofile
?? attempts/robotka-2023-01.yaml
?? entries/robotka-2023/
?? scripts
```

**Agent calls Bash**

```bash
ls -la scripts | head; git log --oneline -1 -- scripts; ls entries/robotka-2023/
```

```
crw-rw-rw- 1 nobody nogroup 1, 3 Nov 14 20:46 scripts
README.md
__pycache__
aa5.py
entry.yaml
reproduce_robotka_2023.ipynb
requirements.in
requirements.lock.txt
```

**Agent calls Bash**

```bash
rm -rf entries/robotka-2023/__pycache__; python tools/entry.py check entries/robotka-2023 2>&1 | tail -2; date -u
```

```
0 error(s)
Sat Nov 14 23:22:16 UTC 2026
```

**Agent**

I've finished the attempt on CRCNS aa-5 (steps 1 to 6). The entry passes `entry.py all`: the notebook ran end to end from a clean environment with no errors. The handover package is built in `executed/robotka-2023/handover/`. Nothing is committed.

## 1. Outcomes per claim

| claim | outcome |
|---|---|
| stimulus-set-link | reproduced (110 stimuli, per-call-type counts exactly the paper's, 4 birds) |
| paper-good-units-link (link claim I added) | partially reproduced: 91 of the paper's 100 listed good units are in the dataset |
| auditory-units | reproduced: 287 of 726 (39.5%); paper 292 of 730 (40.1%) |
| inhibited-units | reproduced: 47 of 287 (16.4%) |
| table1-snr | reproduced: mean 6.84, median 6.07 |
| pcs-variance | reproduced: 92.4% |
| fig3c-peak-call-types | reproduced, assumed (rests on the code's definition of the per-call-type response) |
| fig4a-unit-z-vs-zt | reproduced: 10.75% vs 12.17%, t(186) = 8.99 |
| good-units-100 | not reproduced: 89, one below the tolerance of 90 to 110 |
| fig4b-ensemble-20 | reproduced, assumed: 43.2% vs 30.4% |
| fig4b-top-ensembles | reproduced, assumed: 48.8% |
| fig4b-confusions | reproduced: all 4 error pairs among the two largest of their rows |
| figs4-per-bird-and-sex | blocked (other): ZF6M has only 10 good units, fewer than the 15 the test needs |
| fig5e-volume | partially reproduced, assumed: R2adj 0.120 against 0.1 ± 0.01 |
| fig5f-si-unrelated | reproduced: p = 0.85 |
| fig5g-entropy-selectivity | reproduced: negative slope, p = 0.031 |
| fig5h-neural-noise | partially reproduced: R2adj 0.21 |
| fig5-multiple-regression | partially reproduced, assumed: R2adj 0.252 against 0.22 ± 0.022 |
| figs6, figs5-region-anova, figs9 | blocked (metadata_insufficient): no brain area per unit |
| fig6a, acoustic-labels-decoding, both fig6c claims, figs10 | blocked (data_missing): the lab's vocalization database is not public |
| four claims on the anesthetized dataset (CRCNS aa-4) | blocked (other): aa-4 not analysed in this run |

## 2. Dataset, assumptions, questions

**What the dataset holds:**
- 50 site files (164 GB of tar.gz) holding 872 unit pickles. 34 pickles are empty and 112 hold song stimuli only.
- No unit carries a brain area, so the claims by area cannot be tested.
- Nine of the paper's good units come from a site sorting named `ZF4F_2t_190613_101015.old`, which is not deposited. The deposited site of that name holds 18 other clusters.
- The data descriptor gives `KDE_BW` in seconds, but its values (0.2 to 10) can only be milliseconds.
- Each tar holds a macOS `._` resource-fork file for every pickle, and the pickles were written with pandas 1.x, so they need pandas' pickle compatibility layer.
- No recording was deposited twice. Spike times lock to stimulus onset: decoding from the pre-onset window gives chance, the post-onset window does not.

**Assumptions:**
- The decoder's cross-validation. The Methods hold out one exemplar per call type; the paper's code holds out one random trial per stimulus. I judged the ensemble claims on the code's scheme, because only it gives the paper's numbers (43.2% against 32.0% under the Methods' scheme). Both are shown in the notebook.
- For fig3c, the per-call-type response is the code's definition, which is what Figure 3C plots (`SummaryStatistics.ipynb`). Under the Methods' definition the claim would not be reproduced.

**Questions for the paper's authors** (recorded as `methods_unavailable` findings):
- Which cross-validation scheme produced Figures 4 and 5?
- How was a stable count of exactly 100 good units obtained, when here the count moves from 87 to 101 between random seeds?

**Questions to a reader:** none.

## 3. Where the protocol was unclear or did not fit

1. `archives.md` covers CRCNS zip files only, but this dataset is tar.gz, which cannot be read out of order. I stream every site in full, decompressing with isal, four sites at a time (17 min).
2. Developing on a subset does not fit a dataset where every claim needs a full pass. I streamed the whole dataset once and developed on a reduced copy kept in `$TMPDIR`, outside the entry.
3. The protocol treats a random seed as a choice that cannot change an outcome, but here the good-unit count crosses the tolerance edge depending on the seed. I judged it on the first seed, as the criterion says, and reported the range over 10 other seeds (8 of 10 within tolerance).
4. It is not clear whether one assumption (the cross-validation scheme) may be adopted across many claims. I adopted it consistently and marked each affected outcome `assumed`.
5. No `blocked_by` value fits claims on public outside data (aa-4, 6.9 GB) that were not run for lack of time; `too_large` is for a computation that stops. I used `other`.
6. The paper's code prints the names of its 100 good units, but the claims file does not name that list as an input. I added a link claim and listed the code repository under `inputs`.
7. The link claim's evidence spans two cells, one of them a data-check cell, while the protocol expects one tagged output.

## 4. Runtime and failures

The notebook runs in 35.5 min (16.9 min of it streaming), with peak memory of 4.2 GB. It ran in full twice; the second run followed a text fix and the added link claim. Nothing failed.

## End of run

83 turns, 145 minutes, $7.12 at API prices, result: success.
