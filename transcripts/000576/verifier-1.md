# 000576 · verifier-1 · run 41135101308

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 636
drwxr-xr-x 6 runner runner    4096 Oct 30 22:07 .
drwxr-xr-x 7 runner runner    4096 Oct 30 22:07 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 21:57 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 21:57 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 30 22:07 .claude
-rw-r--r-- 1 runner runner       0 Oct 30 22:07 .env
-rw-r--r-- 1 runner runner       0 Oct 30 22:07 .env.development
-rw-r--r-- 1 runner runner       0 Oct 30 22:07 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 30 22:07 .env.local
-rw-r--r-- 1 runner runner       0 Oct 30 22:07 .env.production
-rw-r--r-- 1 runner runner       0 Oct 30 22:07 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 30 22:07 .env.test
-rw-r--r-- 1 runner runner       0 Oct 30 22:07 .env.test.local
drwx------ 2 runner runner    4096 Oct 30 22:07 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 21:57 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 21:57 .github
-rw-r--r-- 1 runner runner       0 Oct 30 22:07 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 30 21:57 .idea
[... 24 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1016-j.neuroimage.2020.116705.yaml"
}
```

```
1	# Claims for Fedele, Tzovara et al. (2020), NeuroImage 213, 116705, on dandiset 000576.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
3	# protocol pilot-10 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record (PDF supplied by a person, text extracted with PyMuPDF),
6	# main text, figure legends, Tables 1 and 2 and Methods. Table 2 was read from the extracted
7	# text, in which minus signs print as a replacement glyph; its signs agree with the counts the
8	# Results give (12 of 14 negative DELTA MI, HGP MI positive in 7 of 7 nSOZ and negative in 6 of
9	# 7 SOZ amygdalae). The PDF pages could not be rendered here. The supplement (Appendix A, online)
10	# was not supplied; the text cites it only for Fig. S2 (waveforms and inter-spike intervals of
11	# the neurons of each patient), which carries no finding. The Results also cite "Methods 7.8"
12	# for the other spectral bands; no such section exists in the text, and section 4.8 lists the
13	# bands without results.
14	# The data descriptor of the same data (Fedele et al. 2021, Sci Data, doi:10.1038/s41597-020-00790-x,
15	# in paper/) was read for the layout of the deposited data only; no claim is taken from it.
16	#
17	# Code: the paper links no analysis code. The data descriptor says scripts for reading the NIX
18	# files and for its own Figs 2 and 3 come with the G-Node and OpenNeuro deposits; these are not
19	# the paper's analysis and were not read. Every method below is from the paper's Methods (4.7
20	# to 4.11), Results and figure legends.
[... 801 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "amygdala.py"
}
```

```
1	"""Loading and measures for dandiset 000576: iEEG and neurons of the human amygdala during aversive videos.
2	
3	Fedele, Tzovara et al. (2020), NeuroImage 213, 116705, doi:10.1016/j.neuroimage.2020.116705.
4	
5	The dandiset holds one session per patient, deposited twice: `*_ecephys.nwb` and `*_ecephys+image.nwb`,
6	which adds a link to the video and holds the same iEEG, spikes and trials (the notebook checks this).
7	Only the `_ecephys.nwb` files are read. Each holds the bipolar amygdala iEEG channels (`AL2-AL1`,
8	`AR2-AR1`) at 2 kHz as 17 epochs of 26 s laid end to end (0 to 442 s), the trial table (17 trials,
9	alternating NEUTRAL and AVERSIVE, 9 and 8), and for 5 patients a units table of spike times. Within
10	each 26 s epoch the first 2 s are the repeated neutral baseline clip and 2 to 26 s the 24 s block
11	(the trial table's start times for trials 2 to 17 are at 2 s into their epoch). Files are streamed at
12	the pinned version; nothing is written to disk.
13	
14	Where the parameters come from:
15	
16	- Bands, filter (IIR Butterworth of order 2), Hilbert amplitude, 1 s smoothing, baseline correction
17	  with the 1 s before the sequence, z-scoring within each trial: Methods 4.8, as the claims file's
18	  opening comment gives them. HGP is a high-pass at 60 Hz (reading (a) of the claims file).
19	- Zero-phase filtering (`sosfiltfilt`) and a boxcar smoothing window: standard choices that the
20	  claims file names; with 1 s smoothing they cannot change the outcome.
[... 373 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_fedele_2020.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:4000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1418 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Fedele, Tzovara et al. (2020) from dandiset 000576
3	
4	Paper. Fedele T, Tzovara A, Steiger B, Hilfiker P, Grunwald T, Stieglitz L, Jokeit H, Sarnthein J
5	(2020). The relation between neuronal firing, local field potentials and hemodynamic activity in the
6	human amygdala in response to aversive dynamic visual stimuli. *NeuroImage* 213, 116705.
7	[doi:10.1016/j.neuroimage.2020.116705](https://doi.org/10.1016/j.neuroimage.2020.116705). The claims
8	file was written from the version of record (main text, legends, Tables 1 and 2, Methods); the
9	supplement was not supplied and carries no finding. The data descriptor of the same recordings
10	(Fedele et al. 2021, *Sci Data*, doi:10.1038/s41597-020-00790-x) was read for the layout of the data.
11	
12	Dandiset. [DANDI:000576](https://dandiarchive.org/dandiset/000576/0.231010.1811), version
13	0.231010.1811. The paper (2020) predates the dandiset (2023) and cites no version of it. This is the
14	only published version, so it is pinned; the draft lists the same 27 assets with the same total size.
15	
16	What the dandiset holds. For each of the 9 patients one session of the video task: the bipolar
17	iEEG of each implanted amygdala (14 channels in all) at 2 kHz as 17 epochs of 26 s, the trial table,
18	and for 5 patients the spike times of 42 sorted units. Each session is deposited twice, as
19	`_ecephys.nwb` and `_ecephys+image.nwb` (the second adds a link to the video); the data in each pair
20	are identical (checked below), and each is counted once. The BOLD time courses (clinical fMRI) and the
[... 659 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 680,
 "limit": 740
}
```

```
680	alpha amygdala  nSOZ   lmm mass                -0.174          0          0    0.0      0       0.273                                                                              none
681	alpha amygdala  nSOZ   lmm size                -0.174          0          0    0.0      0       0.240                                                                              none
682	alpha amygdala all14   lmm mass                -0.265          3          0   12.0      0       0.004 A<N 6.7 to 12.1 s p=0.004; A<N 13.0 to 16.2 s p=0.004; A<N 20.6 to 24.0 s p=0.004
683	alpha amygdala all14   lmm size                -0.265          3          0   12.0      0       0.002 A<N 6.7 to 12.1 s p=0.002; A<N 13.0 to 16.2 s p=0.012; A<N 20.6 to 24.0 s p=0.010
684	alpha  trialsd  nSOZ   lmm mass                -0.309          0          0    0.0      0       0.150                                                                              none
685	alpha  trialsd  nSOZ   lmm size                -0.309          0          0    0.0      0       0.120                                                                              none
686	alpha  trialsd all14   lmm mass                -0.409          3          0   15.0      0       0.004 A<N 6.7 to 12.1 s p=0.004; A<N 12.8 to 18.2 s p=0.004; A<N 19.8 to 24.0 s p=0.004
687	alpha  trialsd all14   lmm size                -0.409          3          0   15.0      0       0.002 A<N 6.7 to
688	==================== 28 markdown
689	## Modulation indices (table2-mi-values and the claims built on them)
690	
691	MI = AVERSIVE minus NEUTRAL time-averaged power over the window where the conditions differ
692	(Methods 4.11, Table 2 legend), per amygdala. Window readings: (a) the group clusters of the band
693	(Fig. 1B and 1C) under the same z-scoring, from the mixed model with cluster mass over the 7 nSOZ
694	amygdalae (`a_nSOZ`) or all 14 (`a_all14`); (b) clusters found per amygdala (unpaired t-test of its
695	8 AVERSIVE against 9 NEUTRAL trials, cluste
[... 724 more lines not kept]
```

**Agent**

I've read the notebook, the helper module and the claims file. Next I'll get the two outputs that my dump cut short: the delta table in cell 20 and the other-bands table in cell 27.

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_fedele_2020.ipynb'))
for i in [20,27]:
    c=nb['cells'][i]
    for o in c.get('outputs',[]):
        if 'text' in o:
            t=''.join(o['text']); print(t[5500:])
"
```

```
mass                -0.337          2          0   17.1      0       0.002                                                                                   A<N 5.9 to 20.3 s p=0.002; A<N 21.3 to 24.0 s p=0.012
delta amygdala all14 ttest size                -0.337          2          0   17.1      0       0.002                                                                                   A<N 5.9 to 20.3 s p=0.002; A<N 21.3 to 24.0 s p=0.010
delta  trialsd  nSOZ   lmm mass                -0.498          4          0    7.0      0       0.034                             A<N 5.6 to 7.4 s p=0.034; A<N 8.8 to 10.7 s p=0.036; A<N 11.8 to 13.4 s p=0.044; A<N 21.6 to 23.3 s p=0.042
delta  trialsd  nSOZ   lmm size                -0.498          2          0    3.7      0       0.040                                                                                     A<N 5.6 to 7.4 s p=0.048; A<N 8.8 to 10.7 s p=0.040
delta  trialsd  nSOZ ttest mass                -0.498          1          0    2.6      0       0.022                                                                                                              A<N 21.4 to 24.0 s p=0.022
delta  trialsd  nSOZ ttest size                -0.498          3          0    6.4      0       0.018                                                         A<N 5.6 to 7.5 s p=0.044; A<N 8.8 to 10.7 s p=0.044; A<N 21.4 to 24.0 s p=0.018
delta  trialsd all14   lmm mass                -0.445          2          0   16.1      0       0.002                                                                                   A<N 5.8 to 19.3 s p=0.002; A<N 21.4 to 24.0 s p=0.030
delta  trialsd all14   lmm size                -0.445          2          0   16.1      0       0.002                                                                                   A<N 5.8 to 19.3 s p=0.002; A<N 21.4 to 24.0 s p=0.022
delta  trialsd all14 ttest mass                -0.445          2          0   16.1      0       0.002                      
[... 74 more lines not kept]
```

**Agent**

Next I'll run the helper functions on synthetic inputs, check the paper's Table 1 against the data descriptor, and query the archive's metadata for the claims the notebook treats as blocked.

**Agent calls Bash**

```bash
cd  grep -n -i -E "1\.66|firing rate|units|microwire|neurons" paper/10.1038-s41597-020-00790-x.txt | head -40; echo ----; grep -n -i -E "Table 1|MUA" paper/10.1016-j.neuroimage.2020.116705.txt | head;
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json, urllib.request
API="https://api.dandiarchive.org/api"
u=f"{API}/dandisets/000576/versions/0.231010.1811/assets/?page_size=200"
a=json.load(urllib.request.urlopen(u))
print(a['count'])
for x in a['results']: print(x['path'], x['size'])
aid=[x for x in a['results'] if x['path'].endswith('_ecephys+image.nwb')][0]['asset_id']
m=json.load(urllib.request.urlopen(f"{API}/dandisets/000576/versions/0.231010.1811/assets/{aid}/"))
print(json.dumps(m.get('variableMeasured'),indent=0)[:1500]); print(m.get('measurementTechnique'))
aid=[x for x in a['results'] if x['path'].endswith('_ecephys.nwb')][0]['asset_id']
m=json.load(urllib.request.urlopen(f"{API}/dandisets/000576/versions/0.231010.1811/assets/{aid}/"))
print([v.get('value') for v in m.get('variableMeasured',[])])
v=json.load(urllib.request.urlopen(f"{API}/dandisets/000576/versions/0.231010.1811/"))
print(v.get('description')[:1500]); print(v.get('assetsSummary'))
EOF
```

```
27
sub-03/sub-03_ses-20150304T164400_ecephys.nwb 14105034
sub-05/sub-05_ses-20121207T173500_ecephys.nwb 14062778
sub-02/sub-02_ses-20160302T164800_ecephys.nwb 21113775
sub-04/sub-04_ses-20120829T175200_ecephys.nwb 14243738
sub-01/sub-01_ses-20140828T132700_ecephys.nwb 20876593
sub-08/sub-08_ses-20161217T120200_ecephys.nwb 14061953
sub-06/sub-06_ses-20131209T113600_ecephys.nwb 20790986
sub-07/sub-07_ses-20160212T171400_ecephys.nwb 21032650
sub-09/sub-09_ses-20170311T170500_ecephys.nwb 20788090
sub-01/sub-01_ses-20140828T132700_ecephys+image.nwb 20876721
sub-03/sub-03_ses-20150304T164400_ecephys+image.nwb 14105218
sub-02/sub-02_ses-20160302T164800_ecephys+image.nwb 21113951
sub-04/sub-04_ses-20120829T175200_ecephys+image/fe217a3c-380b-4480-9e79-9383df92ee3c_external_file_0.avi 207720448
sub-05/sub-05_ses-20121207T173500_ecephys+image/75fe4cca-e26c-4fa2-ac68-bd4b422e37c7_external_file_0.avi 207720448
sub-03/sub-03_ses-20150304T164400_ecephys+image/5f6936b7-752f-416f-b5bb-5f8649c7c4bc_external_file_0.avi 207720448
sub-02/sub-02_ses-20160302T164800_ecephys+image/b2670e2b-931b-4252-bdec-5518f284f7c4_external_file_0.avi 207720448
sub-01/sub-01_ses-20140828T132700_ecephys+image/b154b52f-1818-4b7a-9e77-28fbbeef4b70_external_file_0.avi 207720448
sub-06/sub-06_ses-20131209T113600_ecephys+image/2a349116-0412-4eac-bb6c-cdea8fe69b00_external_file_0.avi 207720448
sub-07/sub-07_ses-20160212T171400_ecephys+image/c1913d6e-8080-4684-b485-6e584920a2c0_external_file_0.avi 207720448
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import numpy as np, amygdala as A
from scipy import stats
rng=np.random.default_rng(0)
# envelope: 80 Hz sine amplitude 2 over 26 s epochs
t=np.arange(int(26*A.FS))/A.FS
ep=np.vstack([2*np.sin(2*np.pi*80*t), 3*np.sin(2*np.pi*2*t)])
e=A.envelope(ep,'hgp'); print('hgp env', e.shape, e[0,50:55].round(3), e[1,50:55].round(3))
e=A.envelope(ep,'delta'); print('delta env', e[1,50:55].round(3), e[0,50:55].round(4))
print('times', A.times()[:3], A.times()[18:22], len(A.times()))
# clusters
tt=np.array([0,3,3,0,-3,-3,-3,0,3])
print(A.clusters(tt,2))
# lmm_t vs OLS with patient dummies
n=60; g=np.repeat([0,1,2],20); x=np.tile([0,1],30); y=(0.5*x+g+rng.normal(size=n))[:,None]
import statsmodels.api as sm
X=np.column_stack([x, g==1, g==2, np.ones(n)]).astype(float)
f=sm.OLS(y[:,0],X).fit(); print('lmm_t',A.lmm_t(y,x,g)[0], 'ols fe t', f.tvalues[0])
# cluster_test null calibration: no effect -> fraction of p<0.05
fp=0
for k in range(40):
    y=rng.normal(size=(34,100)); y=np.apply_along_axis(lambda v: np.convolve(v,np.ones(10)/10,'same'),1,y)
    x=np.tile(np.r_[np.zeros(9),np.ones(8)].astype(int),2); g=np.repeat([0,1],17)
    _,_,res=A.cluster_test(y,x,g,rng,n_perm=100)
    fp+=any(r['p']<0.05 for r in res)
print('false pos rate', fp/40)
print(A.clopper_pearson(7,7), A.clopper_pearson(6,7), A.clopper_pearson(13,14))
# normalise baseline: check
env=np.ones((2,260)); env[:, 20:]+=1; env+=rng.normal(scale=.01,size=env.shape)
print(A.normalise(env,'trial')[:,25].round(2), A.normalise(env,'trialsd')[:,25].round(2))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls .claude; which -a python3 python; ls ~/.venv* /opt 2>/dev/null | head; pip --version 2>&1 | head -1
```

```
agents
commands
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/python
/usr/bin/python
/bin/python
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
pip 26.2.2 from /opt/hostedtoolcache/Python/3.13.17/x64/lib/python3.13/site-packages/pip (python 3.13)
```

**Agent calls Bash**

```bash
for p in /usr/bin/python3; do $p -c "import numpy,scipy,statsmodels;print('ok')" ; done; python3 -m pip install --quiet --target $TMPDIR/pylib numpy scipy statsmodels h5py remfile 2>&1 | tail -2
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy,scipy,statsmodels;print('ok')
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  PYTHONPATH=$TMPDIR/pylib python3 - <<'EOF'
import numpy as np, amygdala as A
rng=np.random.default_rng(0)
t=np.arange(int(26*A.FS))/A.FS
ep=np.vstack([2*np.sin(2*np.pi*80*t), 3*np.sin(2*np.pi*2*t)])
e=A.envelope(ep,'hgp'); print('hgp env', e.shape, e[0,50:53].round(3), e[1,50:53].round(3))
e=A.envelope(ep,'delta'); print('delta env', e[1,50:53].round(3), e[0,50:53].round(4))
print('times', A.times()[:2], A.times()[19:21], len(A.times()))
print(A.clusters(np.array([0,3,3,0,-3,-3,-3,0,3.]),2))
n=60; g=np.repeat([0,1,2],20); x=np.tile([0,1],30); y=(0.5*x+g+rng.normal(size=n))[:,None]
import statsmodels.api as sm
X=np.column_stack([x, g==1, g==2, np.ones(n)]).astype(float)
f=sm.OLS(y[:,0],X).fit(); print('lmm_t',A.lmm_t(y,x,g)[0], 'ols fe t', f.tvalues[0])
fp=0
for k in range(60):
    y=rng.normal(size=(34,120)); y=np.apply_along_axis(lambda v: np.convolve(v,np.ones(10)/10,'same'),1,y)
    x=np.tile(np.r_[np.zeros(9),np.ones(8)].astype(int),2); g=np.repeat([0,1],17); l=np.repeat([1,2],17)
    _,_,res=A.cluster_test(y,x,g,rng,n_perm=100,linked=l)
    fp+=any(r['p']<0.05 for r in res)
print('false pos rate (2 groups,linked)', fp/60)
print(A.clopper_pearson(7,7), A.clopper_pearson(6,7), A.clopper_pearson(13,14))
env=np.ones((2,260)); env[:, 20:]+=1; env+=rng.normal(scale=.01,size=env.shape)
print(A.normalise(env,'trial')[:,25].round(2), A.normalise(env,'trialsd')[:,25].round(2))
# series 1.5s alignment
x=np.zeros((17,260)); x[1]=1
s,ep_,t_=A.series(x,np.ones(17,bool),'1.5s'); print(len(s), ep_[:20])
EOF
```

```
hgp env (2, 260) [1.523 1.523 1.523] [0. 0. 0.]
delta env [3. 3. 3.] [0.0018 0.0018 0.0017]
times [-1.95 -1.85] [-0.05  0.05] 260
[(np.int64(1), np.int64(3), 1), (np.int64(4), np.int64(7), -1), (np.int64(8), np.int64(9), 1)]
lmm_t [3.91271534] ols fe t 3.912715342889707
false pos rate (2 groups,linked) 0.05
(np.float64(0.5903836027749967), 1.0) (np.float64(0.42127680295680486), np.float64(0.9963897031380994)) (np.float64(0.6613155100681788), np.float64(0.9981932193408746))
[0.29 0.27] [3.76 3.73]
294 [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1]
```

**Agent**

I've finished the checks and am writing up the verdicts. Of the 18 claims the notebook tested, none is reproduced in full. Three are partially reproduced, two are blocked because the paper's methods allow readings that disagree, and the rest are not reproduced. The 7 claims the notebook treats as blocked are genuinely blocked, since their data are not in the archive.

**A. Outcomes** (25 claims in the claims file)

| Claim | My outcome | Reason |
|---|---|---|
| fig1b-delta-decrease | blocked (methods_underspecified) | Under the mixed model with the claims file's readings, it holds for `baseline` z-scoring in both amygdala sets (significant clusters cover 14.3 s for nSOZ and 15.6 s for all 14, against the abstract's 18 s) and for `amygdala` z-scoring over all 14. It fails for `amygdala` over nSOZ (smallest cluster p 0.072/0.056) and for `trial` under both sets (no clusters; cell 20). The criterion says to block when readings disagree. |
| fig1c-hgp-increase-first-2s | not_reproduced | 0 of 16 mixed-model readings and 0 of 16 t-test readings have a positive HGP cluster (cell 23). The closest is nSOZ with `baseline` z-scoring, p 0.056–0.062. The 60–150 and 60–250 Hz variants only give a cluster at 6.2–7.8 s (cell 24). |
| other-bands-no-effect | not_reproduced | Every reading that shows the delta effect also shows a significant cluster in another band (cell 27). `baseline` nSOZ has alpha at 13.3–15.9 s, p=0.016. `baseline` all14 has theta (p=0.002) and alpha. `amygdala` all14 has clusters in all four bands. Only `trial` z-scoring is clean, and it removes the delta effect as well. |
| table2-mi-values | not_reproduced | At most 6 of 28 values are within tolerance under any reading, and at most 23 of 28 signs agree (cell 29). Window (a) gives no HGP MI because there is no HGP group cluster. |
| fig1d-delta-hgp-mi-correlation | not_reproduced | r runs from −0.33 to +0.50 and no reading has p<0.05 (cell 33). The printed Table 2 values give r = −0.736. |
| nsoz-delta-hgp-mi-inverse | not_reproduced | r<0 in only 3 of 8 readings (cell 35). |
| table2-delta-reduced-12-of-14 | partially_reproduced | 11–13 negative, with negative values both inside and outside the SOZ, under window (a) wherever it is defined and under (c) except `trial` z-scoring (10). It fails under every per-amygdala window (b) reading (0–2 negative; most MIs are set to 0). The criterion requires every reading (cell 37). |
| table2-hgp-mi-positive-nsoz | not_reproduced | At best 5 of 7 nSOZ amygdalae are positive and the 7/7 + 6/7 count pattern is never matched (cell 39). |
| fig1e-hgp-not-delta-distinguishes-soz | not_reproduced | HGP p≥0.056 in all 16 rows (cell 41). Note that the printed Table 2 values would also fail the DELTA half (p 0.035/0.013). |
| hgp-soz-sensitivity-specificity | not_reproduced | Sensitivity reaches at most 5/7 and the 7/7 / 6/7 / 13/14 counts are never matched (cell 43). |
| fig1f-hgp-more-specific-than-delta | blocked (methods_underspecified) | Under the claims file's MI windows, HGP is never more specific: (a) is undefined and (b) gives ties or reverses. Under the notebook's added window (c), HGP is more specific for 3 of 4 z-scorings. The chi-square p (0.001–0.11) never approaches the paper's ~0.2 (cell 45). |
| neuron-count | partially_reproduced | 40 (over 442 s) or 42 (over observed epochs) units are above 1 Hz, both within 4.1 of 41. The units sit in 8 amygdalae, not 9 (cell 47). The 50 putative clusters cannot be tested: the dataset holds only the kept units. |
| fig3a-firing-increase-aversive | not_reproduced | Mean FRV is 0.007–0.033 Hz against 0.26 ± 0.15, with 23–27 of 42 units positive and Wilcoxon p ≈ 0.5 (cell 49). |
| fig3a-firing-gradual-sustained | not_reproduced | Both readings fail: the 0–2 s mean (0.31) is above the 2–24 s mean (0.018), the first peak is at 0.15 s, and 4 of the twelve 2 s bins are negative (cell 51). |
| fig3b-firing-hgp-no-condition-difference | partially_reproduced | No difference at the Fig. 3A time base (both spans, p 0.37/0.83) or with any per-block span. The means (0.083 and 0.096) are within the stated spreads. With 1.5 s and 15 s concatenated series, NEUTRAL > AVERSIVE at p=0.002 and 0.009 (cell 53). |
| fig3b-firing-muhgp-higher-aversive | blocked (data_missing) | Confirmed on the archive: each NWB file is 14–21 MB with variableMeasured LFP/Units/ElectricalSeries only. That is too small to hold 32 kHz microwire signals. |
| fig3c-ssi-frv-correlation | not_reproduced | r=0.255, p=0.11 (1 s) and r=0.403, p=0.009 (15 s), against 0.78. The "partially" condition needs p<0.05 under every reading, which the 1 s reading fails (cell 55). |
| fig3d-firing-correlations-modalities | partially_reproduced | The HGP part holds: 0.136 ± 0.24 (15 s) and 0.139 ± 0.20 (1.5 s), within 0.19 ± 0.17 (cell 57). The muHGP and BOLD parts and both Wilcoxon tests are untestable (data_missing). |
| fig4b-regression-firing-hgp | not_reproduced | R is within tolerance in 3 of 4 readings, but the FRV coefficient never reaches p<0.05 (0.07–0.65). The model p<1e-4 in only 2 of 4 readings (cell 59). |
| fig2-participant4-bold-correlations, table2-bold-correlations-group, table2-bold-correlation-values, bold-hgp-uncorrelated-low-mi, fig4c-regression-firing-bold, fig4d-hgp-bold-covariation | blocked (data_missing) | The archive lists 27 assets: 9 `_ecephys.nwb`, 9 `_ecephys+image.nwb` and 9 `.avi`, with no fMRI. The BOLD part is outside data (with_inputs). No part can be tested from the dandiset. For fig4d, only the firing-HGP axis exists. |

**B. Problems**

1. [affects a conclusion] Cells 26, 30, 53 and 55. Where the criteria require every reading, the notebook judges against one it chose itself: `baseline` z-scoring for other-bands and the MI claims, and the 1 s concatenated reading for fig3b. Adopting `baseline` as "FieldTrip's zscore" is the author's own assumption, not the paper's. For fig1b, the readings disagree, which the criterion says should be blocked.
2. [affects a conclusion] `normalise('baseline')`. The SD is taken over 20 samples of the 2 s baseline clip, smoothed over 1 s, so it rests on roughly 2 independent values. This inflates and destabilises the z-values (MIs of −4.8 and 4.0 in cell 29) and drives the MI-based results under that reading.
3. [affects a conclusion] Cells 28–29. MI window (c), fixed windows of 0–2 s and 0–24 s, is the author's own reading and not in the claims file. Window (b) sets MI to 0 when an amygdala has no cluster, also the author's choice, which makes (b) degenerate. The table2-delta-12, fig1f and fig1d judgements depend on these choices.
4. [affects a conclusion] Cell 55, SSI. The paper defines SSI over neurons on *different* microwires. The notebook uses every other unit in the amygdala, including units on the same wire, and never checked whether the units table records the microwire. This bears on fig3c and fig4b.
5. [affects a conclusion] `condition_corr`/`series` with span "concat". Smoothing (7.5 s and 15 s) runs over the whole session before the per-condition mask, so neighbouring opposite-condition blocks and baseline clips mix into each condition's series. In the "1.5s" series the bins also straddle epoch boundaries. These are the two readings that find a difference in fig3b.
6. [affects a conclusion] Cell 15. `trialsd` is a reading the claims file does not list. It is labelled as added, but it enters the hold counts for fig1b and the MI claims.
7. [does not affect a conclusion] Cells 11 and 47. Units are in subjects 1, 2, 3, 4 and 7, while the paper's Table 1 puts MUA in 1, 2, 3, 4, 5 R and 8 L. File ages differ for subjects 2 and 8. Together these hint that dandiset and paper patient numbers may not match; the notebook did not pursue this.
8. [does not affect a conclusion] Cell 43. The Clopper–Pearson interval for 7/7 is 59–100, against the paper's printed 66–100. The paper's bound matches a one-sided 95% interval (0.05^(1/7) ≈ 0.65). This is a claims-file reading that does not reproduce the printed CI, and the notebook did not comment on it.
9. [does not affect a conclusion] `normalise`/`envelope`. The 1 s centred boxcar lets activity from 0–0.5 s leak into the −1 to 0 s baseline window, slightly reducing early HGP effects. The readings fig1c fails under are far from threshold, so the outcome stands.
10. [does not affect a conclusion] Cell 13. The spike–iEEG clock alignment is only weakly supported (24 of 42 units, p=0.042). The firing claims rest on trial times from the same file, so this matters little.
11. [does not affect a conclusion] The helpers pass my synthetic tests:
    * `lmm_t` equals the patient fixed-effects OLS t exactly.
    * `clusters` finds the correct runs.
    * `cluster_test` has a 5% false-positive rate on null data.
    * `envelope` scales by a constant (0.76 at 80 Hz because of the 2nd-order filter applied forwards and backwards), which z-scoring removes.
12. [does not affect a conclusion] Claims file versus the paper's own numbers: on the printed Table 2 values, DELTA MI also differs between SOZ and nSOZ (p 0.035/0.013), so fig1e's "not DELTA" half conflicts with Table 2 itself.

**C. Not checked**

- **Microwire identity for SSI:** the plots could not show this. Printing the units table's columns and the electrode rows each unit points to would show whether a microwire is recorded.
- **Fig. 1-style curves per amygdala:** I could not compare the per-amygdala delta and HGP time courses with Fig. 1B and 1C. A table of each amygdala's A−N difference in 2 s bins would have allowed it.
- **fig3b readings:** the notebook gives no per-block-masked version of the 1.5 s and 15 s concatenated readings, with smoothing inside each block. That would show whether problem 5 explains the difference.
- **Methods 4.8 baseline variants:** the variants (mean of all epochs, previous epoch) were never run.
- **Firing-rate check against the data descriptor:** a PSTH per unit aligned to trial onset would have let me compare the computed mean rate of 4.65 Hz with the descriptor's 1.66 Hz.
- **Patient mapping:** no output tested the dandiset-to-paper patient mapping, for example per-amygdala MIs under a swap of subjects 2 and 7, or 5/8 against 7.

## End of run

14 turns, 4 minutes, result: success.
