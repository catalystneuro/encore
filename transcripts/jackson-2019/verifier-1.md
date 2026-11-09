# openneuro-ds002778 · verifier-1 · run 40599314758

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 436
drwxr-xr-x 6 runner runner    4096 Oct 27 23:09 .
drwxr-xr-x 7 runner runner    4096 Oct 27 23:09 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 23:01 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 23:01 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 27 23:09 .claude
-rw-r--r-- 1 runner runner       0 Oct 27 23:09 .env
-rw-r--r-- 1 runner runner       0 Oct 27 23:09 .env.development
-rw-r--r-- 1 runner runner       0 Oct 27 23:09 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 27 23:09 .env.local
-rw-r--r-- 1 runner runner       0 Oct 27 23:09 .env.production
-rw-r--r-- 1 runner runner       0 Oct 27 23:09 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 27 23:09 .env.test
-rw-r--r-- 1 runner runner       0 Oct 27 23:09 .env.test.local
drwx------ 2 runner runner      40 Oct 27 23:09 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 23:01 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 23:01 .github
-rw-r--r-- 1 runner runner       0 Oct 27 23:09 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 27 23:01 .idea
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1523-eneuro.0151-19.2019.yaml
```

```
<persisted-output>
Output too large (35.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/43d6bf64-897e-448d-81ee-21c5bd95fe98/tool-results/bm7g9fnid.txt

Preview (first 2KB):
# Claims for Jackson, Cole, Voytek & Swann (2019), eNeuro 6(3) ENEURO.0151-19.2019, on OpenNeuro ds002778.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
# protocol as stated in docs/protocol.md.
#
# Text read: the version of record, full text from Europe PMC PMC6553574 (main text, Methods, figure
# legends, Tables 1 to 3). The only supplement is Extended Data 1, the analysis code, which is the
# GitHub repository read below. Figures were not opened; no claim needs a value read off a figure.
#
# Code read: https://github.com/SwannLab/Jackson_2019 at commit a7c89f50106aa4ccec76ace18bbfa45a5440545e
# (2020-05-19). It holds utils.py (loading the preprocessed traces, shape and PAC per recording),
# shape.py (zero crossings, peaks and troughs, sharpness, steepness), pac.py (normalized modulation
# index, Ozkurt and Schnitzler 2011) and notebooks Figure_1, Figures_2,3 and Figure_4. The notebooks
# print the Wilcoxon, rank sum, Spearman and Cohen's d values of Tables 1 and 2 (beta) and Figure 3.
# The code starts from preprocessed MATLAB files (AVG_motor.mat, rejectscombined.mat) that are not in
# the repository: the MATLAB preprocessing, the manual artifact marks, the mu/alpha analysis, the
# bipolar and CSD analyses, the F7/F8 and T7/T8 tests, the power spectra, the topographies and the Q4
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat waveshape.py
```

```
"""Loading and waveform measures for OpenNeuro ds002778 (UC San Diego resting EEG in Parkinson's disease).

Jackson, Cole, Voytek & Swann (2019), eNeuro 6(3) ENEURO.0151-19.2019, doi:10.1523/ENEURO.0151-19.2019.

The dataset is BIDS: 15 patients recorded off (`ses-off`) and on (`ses-on`) medication and 16
controls (`ses-hc`), one BioSemi BDF file per session (32 scalp electrodes, 8 external EXG
channels, a Status channel, 512 Hz). Files are read from the pinned snapshot 1.0.5: the file list
comes from OpenNeuro's GraphQL API, each file is opened at its `urls[0]`, which is pinned to that
snapshot, and read into memory. Nothing is written to disk.

Where the parameters come from. "Claims" is the claims file `claims/openneuro-ds002778/`, whose
opening comment cites the paper's Methods and its code (SwannLab/Jackson_2019 at commit a7c89f5);
"Methods" is the paper's Materials and Methods.

- Preprocessing (`preprocess`): each electrode's mean removed, common average over the 32 scalp
  electrodes, high-pass at 0.5 Hz with a two-way FIR filter (Methods, Data preprocessing: "each
  electrode's mean was removed and then a common average reference was applied ... high pass
  filtered at 0.5 Hz ... using a two-way FIR filter, eegfilt"). The filter is eegfilt's: firls
  of order 3 * fix(512 / 0.5) = 3072 with a 15% transition band (claims, opening comment, a
  standard choice). It is applied forwards and backwards with FFT convolution, with the odd
[... 356 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/43d6bf64-897e-448d-81ee-21c5bd95fe98/tool-results/bm7g9fnid.txt"
}
```

```
1	# Claims for Jackson, Cole, Voytek & Swann (2019), eNeuro 6(3) ENEURO.0151-19.2019, on OpenNeuro ds002778.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-27,
3	# protocol as stated in docs/protocol.md.
4	#
5	# Text read: the version of record, full text from Europe PMC PMC6553574 (main text, Methods, figure
6	# legends, Tables 1 to 3). The only supplement is Extended Data 1, the analysis code, which is the
7	# GitHub repository read below. Figures were not opened; no claim needs a value read off a figure.
8	#
9	# Code read: https://github.com/SwannLab/Jackson_2019 at commit a7c89f50106aa4ccec76ace18bbfa45a5440545e
10	# (2020-05-19). It holds utils.py (loading the preprocessed traces, shape and PAC per recording),
11	# shape.py (zero crossings, peaks and troughs, sharpness, steepness), pac.py (normalized modulation
12	# index, Ozkurt and Schnitzler 2011) and notebooks Figure_1, Figures_2,3 and Figure_4. The notebooks
13	# print the Wilcoxon, rank sum, Spearman and Cohen's d values of Tables 1 and 2 (beta) and Figure 3.
14	# The code starts from preprocessed MATLAB files (AVG_motor.mat, rejectscombined.mat) that are not in
15	# the repository: the MATLAB preprocessing, the manual artifact marks, the mu/alpha analysis, the
16	# bipolar and CSD analyses, the F7/F8 and T7/T8 tests, the power spectra, the topographies and the Q4
17	# effect sizes (Table 3) are not in the code.
18	#
19	# Data the paper used (Methods, Participants and Data collection): resting scalp EEG from a dataset
20	# first published by George et al. (2013) and reanalysed by Swann et al. (2015). 15 PD patients (8
[... 621 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_jackson_2019.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('ERR',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1338 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Jackson, Cole, Voytek & Swann (2019) from OpenNeuro ds002778
3	
4	**Paper.** Jackson N, Cole SR, Voytek B, Swann NC (2019). Characteristics of waveform shape in
5	Parkinson's disease detected with scalp electroencephalography. *eNeuro* 6(3)
6	ENEURO.0151-19.2019. [doi:10.1523/ENEURO.0151-19.2019](https://doi.org/10.1523/ENEURO.0151-19.2019).
7	The claims file was written from the version of record (Europe PMC PMC6553574: main text,
8	Methods, legends, Tables 1 to 3) and the paper's code, SwannLab/Jackson_2019 at commit a7c89f5.
9	
10	**Dataset.** [OpenNeuro ds002778](https://openneuro.org/datasets/ds002778/versions/1.0.5),
11	"UC San Diego Resting State EEG Data from Patients with Parkinson's Disease", snapshot 1.0.5,
12	DOI 10.18112/openneuro.ds002778.v1.0.5. The paper (2019) predates the dataset (first snapshot
13	1.0.0, 2020-05-05) and cites no version. 1.0.5 is the most recent published snapshot. Its
14	CHANGES list fixes to the README, citations, a medication entry of sub-pd22 (1.0.1) and Beck
15	scores (1.0.5); none changes the EEG files, so no earlier snapshot matches the paper better.
16	Files are read from the URLs the OpenNeuro API gives for this snapshot, into memory.
17	
18	**What the dataset holds.** Resting EEG (BioSemi, 32 scalp electrodes and 8 external
19	channels, 512 Hz) of 15 patients off and on medication and 16 controls, with UPDRS and other
20	scores in per-session JSON files. It holds no artifact marks and no bad-channel marks, which
[... 726 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 747
}
```

```
747	fig, axes = plt.subplots(1, 3, figsize=(12, 3))
748	for ax, m in zip(axes, ["ShR", "StR", "PAC methods"]):
749	    t = topo[topo.measure == m].set_index("electrode").loc[ws.SCALP]
750	    ax.bar(range(32), -np.log10(t.p))
751	    ax.axhline(-np.log10(0.05), color="k", lw=0.5)
752	    ax.set_xticks(range(32), ws.SCALP, rotation=90, fontsize=6)
753	    ax.set_title(m)
754	    ax.set_ylabel("-log10 p")
755	plt.tight_layout()
756	plt.show()
757	print("-log10 p range plotted: %.2f to %.2f; nothing outside the axes" % ((-np.log10(topo.p)).min(), (-np.log10(topo.p)).max()))
758	--OUT--
759	ShR: smallest p at P8 (p = 0.0064); in sensorimotor set: False; significant uncorrected: ['P8', 'CP6', 'AF3']; FDR: []
760	   F7/F8/T7/T8 p: {'T8': 0.233, 'F8': 0.4603, 'T7': 0.4955, 'F7': 0.5701} 
761	   five smallest: {'P8': 0.0064, 'CP6': 0.0171, 'AF3': 0.0309, 'C3': 0.0995, 'F4': 0.0995}
762	StR: smallest p at C4 (p = 0.0231); in sensorimotor set: True; significant uncorrected: ['C4']; FDR: []
763	   F7/F8/T7/T8 p: {'T7': 0.2115, 'F7': 0.256, 'F8': 0.4265, 'T8': 0.5701} 
764	   five smallest: {'C4': 0.0231, 'CP6': 0.0691, 'Oz': 0.1118, 'P4': 0.1252, 'Fp2': 0.1556}
765	PAC methods: smallest p at CP6 (p = 0.0268); in sensorimotor set: True; significant uncorrected: ['CP6', 'Fz', 'C3', 'F7', 'C4']; FDR: []
766	   F7/F8/T7/T8 p: {'F7': 0.0409, 'T8': 0.0783, 'F8': 0.1914, 'T7': 0.5321} 
[... 573 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, waveshape as ws
off=np.array([0.0297,0.0127,0.0587,0.0013,0.0398,0.0183,0.0357,0.0350,0.0221,0.0456,0.0154,0.0192,0.0339,0.0196,0.0154])
on=np.array([0.0062,0.0283,0.0237,0.0036,0.0098,0.0055,0.0128,0.0340,0.0053,0.0443,0.0111,0.0095,0.0126,0.0189,0.0042])
print('pac raw',ws.signed_rank(off,on),ws.cohen_d(off,on),'log',ws.cohen_d(np.log10(off),np.log10(on)))
so=np.array([0.0545,0.0363,0.0659,0.0159,0.0473,0.0418,0.0257,0.0735,0.0325,0.0473,0.0293,0.0496,0.0489,0.0258,0.0202])
sn=np.array([0.0087,0.0612,0.0603,0.0041,0.0154,0.0152,0.0135,0.0593,0.0243,0.0526,0.0193,0.0161,0.0302,0.0224,0.0076])
print('shr',ws.signed_rank(so,sn),ws.cohen_d(so,sn))
to=np.array([0.0810,0.0639,0.1417,0.0454,0.1755,0.0194,0.0941,0.1100,0.0707,0.1422,0.1068,0.0240,0.1290,0.0744,0.0281])
tn=np.array([0.0108,0.0046,0.0560,0.0059,0.0487,0.0056,0.0468,0.1064,0.1227,0.1336,0.0703,0.0293,0.0943,0.0794,0.0069])
print('str',ws.signed_rank(to,tn),ws.cohen_d(to,tn))
from scipy import stats
print(stats.spearmanr(so,off), stats.spearmanr(sn,on))
print(stats.spearmanr(to,off), stats.spearmanr(tn,on))
print(ws.fdr_bh([0.4768,0.0143,0.0578,0.6353,0.0177,0.3230]))
from statsmodels.stats.multitest import multipletests as m
print(m([0.4768,0.0143,0.0578,0.6353,0.0177,0.3230],method='fdr_bh')[1])
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, waveshape as ws
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls ~/.venv* /opt 2>/dev/null; which -a python3 python uv pip3 conda 2>/dev/null; pip3 install --user numpy scipy 2>&1 | tail -2
```

```
/opt:
actionarchivecache
az
containerd
google
hca
hostedtoolcache
microsoft
pipelinesagent-cache
pipx
pipx_bin
post-generation
primer
runner-cache
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
/opt/hostedtoolcache/Python/3.13.16/x64/python
/usr/bin/python
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "import numpy,scipy;print(numpy.__version__,scipy.__version__)"; pip3 install --user pandas requests statsmodels mne 2>&1 | tail -1
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy,scipy;print(numpy.__version__,scipy.__version__)
    ^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'scipy'
[notice] To update, run: pip install --upgrade pip
```

**Agent calls Bash**

```bash
cd  pip3 install --user scipy 2>&1 | tail -1; python3 -c "import numpy,scipy,pandas,mne;print(numpy.__version__,scipy.__version__,mne.__version__)"
```

```
Exit code 1
[notice] To update, run: pip install --upgrade pip
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy,scipy,pandas,mne;print(numpy.__version__,scipy.__version__,mne.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pandas'
```

**Agent calls Bash**

```bash
cd  pip3 install --user pandas requests statsmodels mne 2>&1 | tail -4; python3 -c "import numpy,scipy,pandas,mne;print(numpy.__version__,scipy.__version__,mne.__version__)"
```

```
Exit code 1


[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: pip install --upgrade pip
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy,scipy,pandas,mne;print(numpy.__version__,scipy.__version__,mne.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pandas'
```

**Agent calls Bash**

```bash
cd  pip3 install --user pandas 2>&1 | grep -iv notice | tail -5; python3 -m site --user-site; python3 -c "import sys;print(sys.path)"
```

```
Using cached python_dateutil-3.0.0-py2.py3-none-any.whl (94 kB)
Installing collected packages: python-dateutil, pandas

Successfully installed pandas-3.1.0 python-dateutil-3.0.0

/home/runner/.local/lib/python3.13/site-packages
['', '/opt/hostedtoolcache/Python/3.13.16/x64/lib/python313.zip', '/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13', '/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/lib-dynload', '/home/runner/.local/lib/python3.13/site-packages', '/opt/hostedtoolcache/Python/3.13.16/x64/lib/python3.13/site-packages']
```

**Agent calls Bash**

```bash
cd  pip3 install --user mne statsmodels requests 2>&1 | grep -iv notice | tail -2; python3 -c "import numpy,scipy,pandas,mne;print(numpy.__version__,scipy.__version__,mne.__version__)"
```

```
Exit code 1


Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy,scipy,pandas,mne;print(numpy.__version__,scipy.__version__,mne.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'mne'
```

**Agent calls Bash**

```bash
cd  pip3 install --user mne 2>&1 | grep -iv notice | tail -8
```

```
Using cached requests-2.34.2-py3-none-any.whl (73 kB)
Using cached charset_normalizer-3.5.2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl (254 kB)
Using cached certifi-2026.10.23-py3-none-any.whl (135 kB)
Installing collected packages: decorator, cycler, contourpy, charset_normalizer, certifi, requests, matplotlib, pooch, mne
ERROR: Could not install packages due to an OSError: [Errno 30] Read-only file system: '/home/runner/.local/bin/normalizer'
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q v && VIRTUAL_ENV=$TMPDIR/v uv pip install -q numpy scipy pandas mne statsmodels requests 2>&1 | tail -2; $TMPDIR/v/bin/python -c "import numpy,scipy,mne;print(numpy.__version__,scipy.__version__,mne.__version__)"
```

```
2.5.4 1.18.1 1.13.2
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import numpy as np, waveshape as ws
off=np.array([0.0297,0.0127,0.0587,0.0013,0.0398,0.0183,0.0357,0.0350,0.0221,0.0456,0.0154,0.0192,0.0339,0.0196,0.0154])
on=np.array([0.0062,0.0283,0.0237,0.0036,0.0098,0.0055,0.0128,0.0340,0.0053,0.0443,0.0111,0.0095,0.0126,0.0189,0.0042])
print('pac raw',ws.signed_rank(off,on),ws.cohen_d(off,on),'log',ws.cohen_d(np.log10(off),np.log10(on)))
so=np.array([0.0545,0.0363,0.0659,0.0159,0.0473,0.0418,0.0257,0.0735,0.0325,0.0473,0.0293,0.0496,0.0489,0.0258,0.0202])
sn=np.array([0.0087,0.0612,0.0603,0.0041,0.0154,0.0152,0.0135,0.0593,0.0243,0.0526,0.0193,0.0161,0.0302,0.0224,0.0076])
print('shr',ws.signed_rank(so,sn),ws.cohen_d(so,sn))
to=np.array([0.0810,0.0639,0.1417,0.0454,0.1755,0.0194,0.0941,0.1100,0.0707,0.1422,0.1068,0.0240,0.1290,0.0744,0.0281])
tn=np.array([0.0108,0.0046,0.0560,0.0059,0.0487,0.0056,0.0468,0.1064,0.1227,0.1336,0.0703,0.0293,0.0943,0.0794,0.0069])
print('str',ws.signed_rank(to,tn),ws.cohen_d(to,tn))
from scipy import stats
print(stats.spearmanr(so,off), stats.spearmanr(sn,on))
print(stats.spearmanr(to,off), stats.spearmanr(tn,on))
print(ws.fdr_bh([0.4768,0.0143,0.0578,0.6353,0.0177,0.3230]))
from statsmodels.stats.multitest import multipletests as m
print(m([0.4768,0.0143,0.0578,0.6353,0.0177,0.3230],method='fdr_bh')[1])
print(ws.signed_rank(np.arange(15)+0.5, np.zeros(15)))
"
```

```
pac raw (13.0, 0.007598223082063245) 0.8496482249906263 log 0.724835717865696
shr (13.0, 0.007598223082063245) 0.7310932940585327
str (16.0, 0.01245330404618514) 0.7010131816385856
SignificanceResult(statistic=np.float64(0.5796064400715564), pvalue=np.float64(0.02353777324588401)) SignificanceResult(statistic=np.float64(0.7892857142857141), pvalue=np.float64(0.0004673267561781763))
SignificanceResult(statistic=np.float64(0.7882040680887783), pvalue=np.float64(0.0004817850747454804)) SignificanceResult(statistic=np.float64(0.4464285714285714), pvalue=np.float64(0.09529321315352628))
[0.57216 0.0531  0.1156  0.6353  0.0531  0.4845 ]
[0.57216 0.0531  0.1156  0.6353  0.0531  0.4845 ]
(0.0, 0.0006549583433856954)
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import numpy as np, waveshape as ws
from scipy import signal
fs=512; t=np.arange(0,60,1/fs); rng=np.random.default_rng(0)
# sawtooth-ish 20 Hz: slow rise, fast decay -> RDR<0 ; sharper peaks: add harmonic
f=20
x=signal.sawtooth(2*np.pi*f*t, width=0.8)  # rise 80%, fall 20%: decay steeper
x=x+0.01*rng.standard_normal(len(t))
m=ws.shape_measures(x,ws.BETA,118); print('saw width .8',m)
P,T=ws.find_extrema(x,ws.BETA,118); print(len(P),len(T), 60*f)
y=np.sin(2*np.pi*f*t)+0.01*rng.standard_normal(len(t)); print('sine',ws.shape_measures(y,ws.BETA,118))
# peaks sharper than troughs: |sin| inverted-> cusp troughs... use 1-|sin| has sharp peaks
z=-np.abs(np.sin(np.pi*f*t)); z=z-z.mean()+0.005*rng.standard_normal(len(t)); print('sharp peaks', ws.shape_measures(z,ws.BETA,118))
# PAC
ph=2*np.pi*20*t; a=1+0.8*np.cos(ph); s=np.cos(ph)+0.3*a*np.sin(2*np.pi*90*t)+0.1*rng.standard_normal(len(t))
print('pac coupled',ws.pac_ozkurt(s,ws.BETA,118), 'uncoupled', ws.pac_ozkurt(np.cos(ph)+0.3*np.sin(2*np.pi*90*t)+0.1*rng.standard_normal(len(t)),ws.BETA,118))
# filtfilt fft vs scipy
b=ws.eegfilt_highpass_taps(); w=rng.standard_normal((2,20000)).cumsum(1)
print('hp diff', np.abs(ws._filtfilt_fft(w,b)-signal.filtfilt(b,[1],w,axis=-1)).max(), len(b))
H=np.abs(np.fft.rfft(b,8192)); fr=np.fft.rfftfreq(8192,1/fs); print('hp gain at 0.1,0.425,0.5,1 Hz',[round(H[np.argmin(abs(fr-q))],3) for q in (0.1,0.425,0.5,1)])
"
```

```
saw width .8 {'ShR': np.float64(0.00026466088350754805), 'StR': np.float64(0.5147821838590494), 'PTR': np.float64(0.00026466088350754805), 'RDR': np.float64(-0.5147821838590494), 'n_peaks': 1192, 'n_troughs': 1193}
1192 1193 1200
sine {'ShR': np.float64(0.00018021921067813232), 'StR': np.float64(0.0005732973971102786), 'PTR': np.float64(-0.00018021921067813232), 'RDR': np.float64(0.0005732973971102786), 'n_peaks': 1192, 'n_troughs': 1192}
sharp peaks {'ShR': np.float64(0.6762257775630359), 'StR': np.float64(0.0004939486319236005), 'PTR': np.float64(0.6762257775630359), 'RDR': np.float64(-0.0004939486319236005), 'n_peaks': 1193, 'n_troughs': 1192}
pac coupled 0.3217173768430921 uncoupled 0.0020760000482498934
hp diff 2.282618538629322e-13 3073
hp gain at 0.1,0.425,0.5,1 Hz [np.float64(0.039), np.float64(0.355), np.float64(0.718), np.float64(1.015)]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import waveshape as ws
df=ws.listing(); print(len(df)); import re
print(sorted({re.sub(r'sub-(pd|hc)\d+','sub-X',f) for f in df.index}))
print(ws.read_tsv('sub-pd3/ses-off/eeg/sub-pd3_ses-off_task-rest_channels.tsv').head(3).to_string())
print(ws.fetch('README').decode()[:1500])
"
```

```
331
['.datalad/.gitattributes', '.datalad/config', '.gitattributes', 'CHANGES', 'README', 'dataset_description.json', 'participants.json', 'participants.tsv', 'sub-X/ses-hc/beh/sub-X_ses-hc_task-rest_beh.json', 'sub-X/ses-hc/beh/sub-X_ses-hc_task-rest_beh.tsv', 'sub-X/ses-hc/eeg/sub-X_ses-hc_task-rest_channels.tsv', 'sub-X/ses-hc/eeg/sub-X_ses-hc_task-rest_eeg.bdf', 'sub-X/ses-hc/eeg/sub-X_ses-hc_task-rest_eeg.json', 'sub-X/ses-hc/eeg/sub-X_ses-hc_task-rest_events.tsv', 'sub-X/ses-hc/sub-X_ses-hc_scans.tsv', 'sub-X/ses-off/beh/sub-X_ses-off_task-rest_beh.json', 'sub-X/ses-off/beh/sub-X_ses-off_task-rest_beh.tsv', 'sub-X/ses-off/eeg/sub-X_ses-off_task-rest_channels.tsv', 'sub-X/ses-off/eeg/sub-X_ses-off_task-rest_eeg.bdf', 'sub-X/ses-off/eeg/sub-X_ses-off_task-rest_eeg.json', 'sub-X/ses-off/eeg/sub-X_ses-off_task-rest_events.tsv', 'sub-X/ses-off/sub-X_ses-off_scans.tsv', 'sub-X/ses-on/beh/sub-X_ses-on_task-rest_beh.json', 'sub-X/ses-on/beh/sub-X_ses-on_task-rest_beh.tsv', 'sub-X/ses-on/eeg/sub-X_ses-on_task-rest_channels.tsv', 'sub-X/ses-on/eeg/sub-X_ses-on_task-rest_eeg.bdf', 'sub-X/ses-on/eeg/sub-X_ses-on_task-rest_eeg.json', 'sub-X/ses-on/eeg/sub-X_ses-on_task-rest_events.tsv', 'sub-X/ses-on/sub-X_ses-on_scans.tsv', 'task-rest_beh.json']
  name type units  low_cutoff  high_cutoff           description  sampling_frequency status
0  Fp1  EEG    µV         0.0        104.0  ElectroEncephaloGram               512.0   good
1  AF3  EEG    µV         0.0        104.0  ElectroEncephaloGram               512.0   good
2   F7  EEG    µV         0.0        104.0  ElectroEncephaloGram               512.0   good
Welcome to the resting state EEG dataset collected at the University of San Diego and curated by Alex Rockhill at the University of Oregon.

Please email [removed: an e-mail address] before submitting a manuscript to be published in a peer-reviewed journal using this data, we wish to ensure that the data to be analyzed and interpreted with scientific integrity so as not to misl
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import waveshape as ws
print(ws.fetch('README').decode()[1500:]); print(ws.fetch('CHANGES').decode())
print(ws.fetch('sub-pd3/ses-off/beh/sub-pd3_ses-off_task-rest_beh.tsv').decode()[:300])
print(ws.fetch('participants.json').decode()[:1500])
"
```

```
d all open-source data and be sure to credit authors by citing them.

An example of an analysis that we could consider problematic and would strongly advice to be corrected before submission to a publication would be using machine learning to classify Parkinson's patients from healthy controls using this dataset. This is because there are far too few patients for proper statistics. Parkinson's disease presents heterogeneously across patients, and, with a proper test-training split, there would be fewer than 8 patients in the testing set. Statistics on 8 or fewer patients for such a complicated diease would be inaccurate due to having too small of a sample size. Furthermore, if multiple machine learning algorithms were desired to be tested, a third split would be required to choose the best method, further lowering the number of patients in the testing set. We strongly advise against using any such approach because it would mislead patients and people who are interested in knowing if they have Parkinson's disease.

Note that UPDRS rating scales were collected by laboratory personnel who had completed online training and not a board-certified neurologist. Results should be interpreted accordingly, especially that analyses based largely on these ratings should be taken with the appropriate amount of uncertainty.

In addition to contacting the aforementioned email, please cite the following papers:

Nicko Jackson, Scott R. Cole, Bradley Voytek, Nicole C. Swann. Characteristics of Waveform Shape in Parkinson's Disease Detected with Scalp Electroencephalography. eNeuro 20 May 2019, 6 (3) ENEURO.0151-19.2019; DOI: 10.1523/ENEURO.0151-19.2019.

Swann NC, de Hemptinne C, Aron AR, Ostrem JL, Knight RT, Starr PA. Elevated synchrony in Parkinson disease detected with electroencephalography. Ann Neurol. 2015 Nov;78(5):742-50. doi: 10.1002/ana.24507. Epub 2015 Sep 2. PMID: 26290353; PMCID: PMC4623949.

George JS, Strunk J, Mak-McCully R, Houser M, Poizner H, Aron AR. Dopaminergic
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "pwelch|power spectr|Figure 1|Fig. 1C|1C|CSD|current source|log|Q4|quadrant|noisy|artifact" 10.1523-eneuro.0151-19.2019.txt | head -60
```

```
<persisted-output>
Output too large (30.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/43d6bf64-897e-448d-81ee-21c5bd95fe98/tool-results/btdrsf2mn.txt

Preview (first 2KB):
7:Characteristics of Waveform Shape in Parkinson’s Disease Detected with Scalp Electroencephalography
10:AbstractNeural activity in the β frequency range (13–30 Hz) is excessively synchronized in Parkinson’s disease (PD). Previous work using invasive intracranial recordings and non-invasive scalp electroencephalography (EEG) has shown that correlations between β phase and broad-band γ (>50 Hz) amplitude [i.e., phase amplitude coupling (PAC)] are elevated in PD, perhaps a reflection of this synchrony. Recently, it has also been shown, in invasive human recordings, that non-sinusoidal features of β oscillation shape also characterize PD. Here, we show that these features of β waveform shape also distinguish PD patients on and off medication using non-invasive recordings in a dataset of 15 PD patients with resting scalp EEG. Specifically, β oscillations over sensorimotor electrodes in PD patients off medication had greater sharpness asymmetry and steepness asymmetry than on medication (sign rank, p < 0.02, corrected). We also showed that β oscillations over sensorimotor cortex most often had a canonical shape, and that using this prototypical shape as an inclusion criteria increased the effect size of our findings. Together, our findings suggest that novel ways of measuring β synchrony that incorporate waveform shape could improve detection of PD pathophysiology in non-invasive recordings. Moreover, they motivate the consideration of waveform shape in future EEG studies.Keywords: β, EEG, electrophysiology, motor cortex, Parkinson’s disease, waveform shape
...
</persisted-output>
```

**Agent calls Bash**

```bash
cd paper; grep -n -o -i -E ".{250}(pwelch|average power spectr|Figure 1C|Fig. 1C|spectra).{300}" 10.1523-eneuro.0151-19.2019.txt | head -10
```

```
98:metrics examined. This suggests the consideration of waveform shape could improve the efficacy of non-invasive PD biomarkers. Importantly, this difference in waveform shape occurred in the context of a lack of a consistent difference in conventional spectral power in the β range over sensorimotor cortex in previous publications examining PD (Stoffers et al., 2007; de Hemptinne et al., 2013, 2015; Malekmohammadi et al., 2018), including two which analyzed the same dataset we examined here (George et al., 2013; Swann et al., 2015). This underscores the
```

**Agent calls Bash**

```bash
cd paper; grep -n -o -i -E ".{0,400}(welch|μ/α oscillation|alpha oscillation).{0,400}" 10.1523-eneuro.0151-19.2019.txt | head; grep -n -o -i -E ".{0,300}(spline flexibility|surface Laplacian).{0,300}" 10.1523-eneuro.0151-19.2019.txt
```

```
34:The following measures were calculated using Python code that were modified from (Cole et al., 2017), unless otherwise specified. Details are described below for each measure. Based on the previous publications, we focused our analysis on the β frequency range (de Hemptinne et al., 2015; Swann et al., 2015; Cole et al., 2017). However, we did compute average power spectral density (using the pwelch function in MATLAB, window = 256, overlap =128, nFFT = 450) to verify that an oscillation was indeed present in the β frequency range and to determine if prominent oscillations in other frequency ranges were also present.
63:r each group to verify that an oscillation in β was indeed present (Fig. 1C). This is important because analyzing the raw signal as is done for the sharpness and steepness measures is not precise if there is no dominant oscillation present. These plots demonstrated that there was indeed an oscillation present in β, as would be expected in sensorimotor EEG. However, unsurprisingly there was also a μ/α oscillation in the 8–12 Hz range (Pfurtscheller, 1981). Thus, we repeated our analyses for the μ/α range and have reported those results in Tables 1, 2. We found these values to be overall similar to those we found for β, with the exception of PAC, which was non-significant for μ/α, while being significant for β. Indeed, for PAC, the difference between off medication and on medication in β was significantly 
30: complicate interpretation of waveform shape. Thus, to be consistent, we used an average reference approach for all measures. However, for direct comparison with the previous publication (Swann et al., 2015) we implemented a CSD referencing approach as a confirmatory analysis (CSDtoolbox in MATLAB, spline flexibility = 3; Kayser and Tenke, 2006a,b; Kayser, 2009).
```

**Agent calls Bash**

```bash
cd paper; grep -n -o -E "Figure 1\..{0,900}" 10.1523-eneuro.0151-19.2019.txt | head -3; grep -n -o -E ".{300}Swann et al., 2015\) and from.{0,10}|.{0,300}(artifacts were|marked).{0,300}" 10.1523-eneuro.0151-19.2019.txt | head
```

```
41:Figure 1.] Schematic summarizing waveform shape calculations. A, First rising and falling zerocrossings were identified from the β-filtered signal. Then, peaks and troughs that lie between adjacent zerocrossings were found in the raw signal. B, Peak sharpness was calculated as the mean of the difference between the peak (purple circle) and the voltage points three samples before and after the peak (purple triangles). The trough sharpness was calculated in a similar fashion, indicated with blue circles and triangles similar to the peaks analysis. The yellow area, between a trough and subsequent peak, indicates an area where rise steepness is determined, while the green area, between a peak and subsequent trough, indicates an area where decay steepness was found. The maximum slope (shown with arrows) for each of these shaded regions (red circles) was derived as rise and decay steepness and then the
40:.e., voltage sign-changes) were identified in this filtered signal. Next, returning to the raw signal, the indices of the maximum voltage (the “peak”), and minimum voltage (the “trough”), between zerocrossings were found. Once peaks and troughs were identified, those that fell in regions previously marked for rejection due to artifacts were excluded from further analysis. Peak sharpness was defined as the mean of the voltage difference between the peak and three data points before and after the peak. Trough sharpness was calculated in an analogous way. Three sample points corresponds to ∼5.9 ms of d
47:window, β and γ components were extracted from the signal. Beta was filtered between 13 and 30 Hz with a filter order of 231 ms using the function “firwin” in python. Gamma was filtered using the same filter between 50 and 150 Hz with a filter order of 240 ms. After filtering, regions that had been marked as containing artifacts were removed. Beta phase and γ amplitude time series were calculated by extracting the angle and amplitude of the Hilbert transform, respective
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n -o -E "Figure 1\..{900,2200}" 10.1523-eneuro.0151-19.2019.txt | cut -c900-2300
```

```
and then the ratio was taken to find steepness ratio, as described in Materials and Methods. Figure modeled after Cole et al. (2017), but here is shown with the present EEG data. C, Average power spectral density plots for each group. Plots confirm that there is a β oscillation as well as a prominent α/μ oscillation (each indicated with black arrow).
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import json
nb=json.load(open('reproduce_jackson_2019.ipynb'))
o=''.join(nb['cells'][6]['outputs'][0]['text']); print('\n'.join(l for l in o.splitlines() if ' on ' in l or 'range' in l or 'Dur' in l or 'status' in l))
"
```

```
sub ses  sfreq  dur_s  sidecar_dur_s  n_chan  scalp_names_ok  status_all_good units  highcut  raw_mean_abs_uv  raw_max_abs_sum_uv  pre_sd_min  pre_sd_median  pre_sd_max max_sd_chan min_sd_chan
pd11  on  512.0  187.0          187.0      41            True             True    µV    104.0          3887.84           81358.756        5.78           7.84        15.3         Fp1          C4
pd12  on  512.0  192.0          192.0      41            True             True    µV    104.0          3892.92           28587.291        5.79           9.33        24.1         Fp1          Cz
pd13  on  512.0  187.0          187.0      41            True             True    µV    104.0          8500.54           16761.406        3.31           4.97         8.3         Fp1          C3
pd14  on  512.0  189.0          189.0      41            True             True    µV    104.0          8760.99          217373.505        5.50           8.72        18.6         Fp2         CP1
pd16  on  512.0  187.0          187.0      41            True             True    µV    256.0            23.32          306597.929       11.51          62.61       224.4         Fp2         PO3
pd17  on  512.0  186.0          186.0      41            True             True    µV    104.0          6369.04          156627.304        3.77           9.97        35.4         Fp1         FC2
pd19  on  512.0  188.0          188.0      41            True             True    µV    104.0          4090.04          113107.822        6.49          11.14        34.1         Fp2         FC1
pd22  on  512.0  184.0          184.0      41            True             True    µV    104.0          4506.14           68729.592        5.38          11.69        52.3         Fp2         FC1
pd23  on  512.0  186.0          186.0      41            True             True    µV    104.0          5917.87          132154.162        5.33           9.07        27.6         Fp2          Cz
pd26  on  512.0  216.0          216.0      41            True
[... 8 more lines not kept]
```

**Agent**

**Verification report, round 1: Jackson et al. 2019 (eNeuro 0151-19.2019) on OpenNeuro ds002778 v1.0.5**

The claims file has 24 claims. The notebook tests all 24 and blocks none. My outcomes: 9 reproduced, 9 partially reproduced, 6 not reproduced, 0 blocked.

How I checked:
- I recomputed W, p, d and Spearman r from the per-patient values the notebook prints. They match to rounding.
- The helpers behave correctly on synthetic signals:
  - A sawtooth with a slow rise gives a negative rise-to-fall ratio.
  - Cusp-shaped peaks give a positive peak-to-trough ratio, and a sine gives about 0 for both.
  - Coupled PAC is 0.32 and uncoupled PAC is 0.002.
  - The FFT high-pass equals scipy's filtfilt to 2e-13.
  - `fdr_bh` equals statsmodels' BH.
- I queried the archive's file list. It has 331 files, with no artifact or bad-segment marks, every channels.tsv says "good", and events.tsv holds only a start trigger. So readings (a) and (b) for artifact rejection and noisy electrodes are the same here.

### A. Outcomes

| Claim | Outcome | Reason |
|---|---|---|
| fig2-sharpness-off-on | partially_reproduced | FDR p 0.0228; off higher in 13/15; W 13 is within 10.8–13.2. d 0.731 is outside 0.774–0.946 (cells 14, 16). |
| fig2-steepness-off-on | partially_reproduced | FDR p 0.0249; d 0.701 is within tolerance. W 16 is outside 8.1–9.9 (cell 18). |
| fig2-pac-off-on | partially_reproduced | FDR p 0.0228 and raw d 0.851/0.863 are within tolerance. W is 13 (Methods filters) or 12 (code filters), both outside 13.5–16.5 (cell 20). Reproduced if the criterion's last sentence, which drops W, applies (problem 1). |
| bipolar-off-on | reproduced | All three FDR p < 0.05 with off higher: 0.0106, 0.0044, 0.0096 (code filters 0.0081). Only steepness approaches the paper's p < 0.004 bound (cell 22). |
| temporalis-f7f8-null | reproduced | p = 0.69, 0.17, and 0.10 (Methods) or 0.078 (code); none below 0.05 (cell 24). |
| temporalis-t7t8-null | reproduced | p = 0.36, 0.95, 0.11 (cell 25). |
| fig2c-topography-sensorimotor | partially_reproduced | Smallest p for sharpness is at P8, outside the sensorimotor set. Steepness (C4) passes. PAC (Methods filters) has its minimum at CP6, but F7 is significant uncorrected (0.041). That gives 2/3 measures under the FDR reading and 1/3 uncorrected (cell 27). |
| offctrl-sharpness-null | reproduced | z 0.47, p 0.635 (paper 0.91, 0.363) (cell 29). |
| offctrl-steepness | not_reproduced | z 2.37 and d 0.855 are within tolerance, but FDR p over Table 2 is 0.0531 under every filter reading. The bipolar single test (p 0.0177) would hold, but the criterion needs the average-reference result first (cell 31). |
| offctrl-pac-null | reproduced | p 0.323 (Methods) and 0.286 (code) (cell 33). |
| offctrl-pac-csd | not_reproduced | Rank sum p 0.075 under both filter readings (cell 34). |
| updrs-improvement | reproduced | "Total UPDRS": W 3.5, p 0.0033, matching the paper exactly (cell 36). |
| fig1c-beta-alpha-peaks | not_reproduced | The C3/C4 mean spectrum has no local maximum in 8–12 or 13–30 Hz for off or on; only controls have both. The all-electrode variant gives off a beta maximum only. The off group's maximum sits at 7.96 Hz, just below the window (cell 38). |
| table1-alpha-shape-off-on | partially_reproduced | Both FDR p < 0.05 (0.026/0.032). Sharpness W and d are within tolerance. Steepness W 21 is outside 10.8–13.2 under both alpha filter readings (cell 40). |
| table1-alpha-pac-null | not_reproduced | Readings disagree: FDR p 0.061 (a192) and 0.078 (b231) are null, but 0.036 (c118) is significant. The criterion asks for the outcome all readings give. d is 0.66–0.72 against 0.51 ± 0.05 in every reading (cell 42). |
| table2-alpha-offctrl | not_reproduced | Steepness z 2.45 and d 0.89 are within tolerance, but FDR p is 0.0531 under all readings. Sharpness and PAC are null as expected (cell 44). |
| pac-beta-larger-than-alpha | partially_reproduced | Raw PAC: p 0.015, beta difference larger in 12/15, but W is 17–18 against 9.9–12.1. The log-PAC variant is not significant. The criterion has no partial clause (cell 46). |
| fig3-sharpness-pac-correlation | partially_reproduced | Both r are positive and significant. Methods filters: off r 0.586 is out of tolerance. Code filters: on r 0.843 is out. No reading puts both within tolerance (cell 48). |
| fig3-steepness-pac-correlation | partially_reproduced | Code filters: off r 0.796 is within tolerance; on r 0.532 (p 0.041) is significant but out of tolerance. Methods filters: on r 0.446 is not significant (p 0.095) (cell 49). |
| fig4a-sensorimotor-q4 | reproduced | 48/60 points in Q4 (cell 51). |
| q4-patient-counts | not_reproduced | C3 10, C4 10, both 7, at least one 13, against 9/8/8/9 ± 1. C4 and at-least-one are out in either electrode order (cell 53). |
| fig4b-temporalis-variable-shape | reproduced | Both readings agree: most-common-quadrant share is 0.68 at F7/F8 against 0.80 at C3/C4, and RMS distance to the centroid is 0.093 against 0.076 (cell 55). |
| controls-q4 | reproduced | 25/32 points in Q4 (cell 57). |
| table3-q4-effect-size | partially_reproduced | d rises for all three measures under every reading. Q4 sharpness d 0.994 is within tolerance; steepness 0.817 and PAC 0.95–1.06 are out. All-patient PAC d matches 0.75 only for log10 PAC with Methods filters (0.731). The Q4 subset has 13 patients, not the paper's 9 (cell 59). |

The paper states no chance levels, so there was nothing to compare.

### B. Problems

1. **[affects a conclusion]** In the claims file, the fig2-pac-off-on criterion contradicts itself. It says "As for fig2-sharpness-off-on", which requires W and d within tolerance, and then "holds when the test holds under one reading and d is within tolerance". It also lists an expected W. With W out (13 and 12) and d in, the outcome is partially_reproduced or reproduced depending on which sentence governs. I applied the stricter reading.
2. **[affects a conclusion]** The table1-alpha-pac-null criterion assumes the three phase-filter readings agree; they do not (cell 42). The outcome rests on the reading: 2/3 readings reproduce the null. The notebook reports every reading but does not flag the disagreement.
3. **[affects a conclusion]** In table3-q4-effect-size (cells 53, 59), the Q4 inclusion set is 13 patients against the paper's 9, so the Q4 d values come from a different subset than Table 3's. The notebook compares them to Table 3 without noting this.
4. **[does not affect a conclusion]** Cell 12's markdown says "Total UPDRS" exceeds "UPDRS 18-26" by "0 to 14"; cell 11 prints 1 to 14. Its identification of "Total UPDRS" as Part III is asserted as "consistent with the values, not shown". The "total of all parts" reading is not computed separately, but the dataset holds no other part. W = 3.5 matches either way.
5. **[does not affect a conclusion]** Two on sessions, pd6 and pd16, were exported from preprocessed EEGLAB files. pd6 is already average-referenced; pd16 has electrode SDs about 6 times the others and a high cutoff of 256 Hz. Both stay in the main analysis. Exclusion variants appear only in cells 16, 18 and 38, not for PAC, the correlations or Q4. The ratio measures do not depend on scale, but whatever preprocessing those files carry is unknown.
6. **[does not affect a conclusion]** `pac_ozkurt` keeps the filter-edge samples, whereas pacpy's `firf` (rmvedge) drops them. This is a few hundred samples out of 90k or more.
7. **[does not affect a conclusion]** `csd` uses MNE's spherical spline on template biosemi32 positions instead of the CSD toolbox's lookup positions. This is a stated, reasonable assumption, but untested. offctrl-pac-csd misses at p 0.075, so a sensitivity check would be informative.
8. **[does not affect a conclusion]** The paper's artifact rejection and noisy-electrode exclusion cannot be reproduced; I verified the archive holds no marks. This may explain the out-of-tolerance W and d values, but it is not an error in the notebook.

### C. What I could not check

- **CSD against the CSD toolbox.** I could not confirm MNE's output equals the toolbox's. A comparison of the CSD transform on one recording, or C3/C4 spectra before and after CSD, would let me.
- **The pd6 and pd16 sessions.** Whether they were artifact-cleaned or filtered differently is unknown. Off-on PAC, the correlations, the Q4 counts and Table 3 rerun without these two patients would show their influence.
- **Q4 membership.** Which patients the paper's 9 Q4 cases are is unknown, so I could not tell why the counts differ. Per-patient PTR/RDR values at C3 and C4 would help localise the gap.
- **Figure images.** I did not inspect the plots; I relied on the printed ranges, which show no points clipped.
- **Table 2's FDR method.** Whether the paper used BH for Table 2 is uncertain (its printed p = 1, noted in the claims file). offctrl-steepness and table2-alpha-offctrl hinge on BH giving 0.0531, so a sensitivity output under other correction procedures would show how fragile those two outcomes are.

## End of run

27 turns, 5 minutes, result: success.
