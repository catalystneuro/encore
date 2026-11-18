# nishimoto-2011 · verifier-1 · run 43566842292

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null
```

```
Exit code 2
total 304
drwxr-xr-x 6 runner runner    4096 Nov 14 07:16 .
drwxr-xr-x 8 runner runner    4096 Nov 14 07:16 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 06:32 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 06:32 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov 14 07:16 .claude
-rw-r--r-- 1 runner runner       0 Nov 14 07:16 .env
-rw-r--r-- 1 runner runner       0 Nov 14 07:16 .env.development
-rw-r--r-- 1 runner runner       0 Nov 14 07:16 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov 14 07:16 .env.local
-rw-r--r-- 1 runner runner       0 Nov 14 07:16 .env.production
-rw-r--r-- 1 runner runner       0 Nov 14 07:16 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov 14 07:16 .env.test
-rw-r--r-- 1 runner runner       0 Nov 14 07:16 .env.test.local
drwx------ 2 runner runner    4096 Nov 14 07:16 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 06:32 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 06:32 .github
-rw-r--r-- 1 runner runner       0 Nov 14 07:16 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov 14 06:32 .idea
[... 24 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "nishimoto-2011.yaml"
}
```

```
1	# Claims for Nishimoto & Gallant (2011), J Neurosci 31(41):14551-14564, tested on CRCNS mt-2.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-10,
3	# protocol pilot-14 as stated in docs/protocol.md.
4	#
5	# Text read: the version of record (paper/10.1523-jneurosci.6801-10.2011.txt, PyMuPDF extraction
6	# of the publisher PDF), main text, Materials and Methods and figure legends. The paper has no
7	# supplement other than Movie 1 (stimulus spectra, not a result). Figure 2B, Figure 3, Figure 6
8	# and Figure 7 were read from the PDF where the text extraction garbled symbols; the
9	# inequality signs of every p-value were read there (p < 0.01, p > 0.10 and so on). The paper
10	# links no code, so no repository was read. The dataset's own documentation
11	# (paper/mt-2.data-description.txt) was read only to know what the dataset is meant to hold.
12	#
13	# Data the paper used (Materials and Methods, Physiology; Visual stimuli; Results, opening
14	# paragraph). 52 single MT neurons from two adult male macaques (Macaca mulatta) performing a
15	# fixation task. Each neuron saw 20,000 to 40,000 frames (mean 27,120) of motion-enhanced
16	# natural movies at 83 Hz as training data (the Results say 22,000 to 42,000 frames), and a
17	# separate 2000-frame motion-enhanced movie repeated 5 to 20 times as validation data. A subset
18	# of 15 neurons also saw a 2000-frame natural movie without motion enhancement, repeated 5 to
19	# 20 times, as a second validation set. Measured variable is the spike train, analysed at the
20	# 83 Hz frame rate. The CRCNS description says mt-2 holds 45 neurons (not 52), each with the
[... 551 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/mt-2.data-description.txt"
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_nishimoto_2011.ipynb'))
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
1128 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Nishimoto and Gallant (2011) on CRCNS mt-2
3	
4	Paper: Nishimoto S, Gallant JL (2011), "A Three-Dimensional Spatiotemporal Receptive Field Model
5	Explains Responses of Area MT Neurons to Naturalistic Movies", J Neurosci 31(41):14551-14564,
6	doi:10.1523/jneurosci.6801-10.2011.
7	
8	Dataset: CRCNS mt-2, "Extracellular recordings from area MT of awake macaques in response to
9	naturalistic movies", doi:10.6080/K0DN4374, read from the public bucket
10	`crcnsarchive/mt-2/live/`. CRCNS data sets are not versioned; the version is recorded as
11	`unversioned` and the next cell prints the MD5 sums of `checksums.md5` for the 45 files read, so a
12	later change can be detected. The `live` folder is the only copy in the bucket (there is no
13	`old` folder), so it is the version pinned.
14	
15	Claims: `claims/nishimoto-2011.yaml`, written from the version of record (main text, Methods and
16	legends; the paper has no supplement beyond a movie of stimulus spectra and links no code).
17	
18	The model cannot be fitted here at the paper's size (about 6000 filters at 11 delays, boosted
19	five times, for 12 models and 45 neurons) within the time limit. The filter bank follows the
20	paper's rules (about 7000 complex and 1100 simple channels), and the regression weights are
[... 731 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 751
}
```

```
751	for rc in RCOMB:
752	    v = np.array([real[n][rc]["sup"] for n in names_run])
753	    for key, lst in sorted(nulls.items()):
754	        ns_ = np.array([x[rc]["sup"] for x in lst])
755	        ne_ = np.array([x[rc]["exc"] for x in lst])
756	        p1, p2 = ranksums(v, ns_).pvalue, ranksums(v, ne_).pvalue
757	        rows.append(dict(balance=rc[0], quantity=rc[1], sign=rc[2], mean_sup=v.mean(), null=f"{key[0]}{key[1]}{key[2]}",
758	                         null_sup=ns_.mean(), p_vs_null_sup=p1, null_exc=ne_.mean(), p_vs_null_exc=p2,
759	                         ok=(0.162 <= v.mean() <= 0.198) and p1 < 0.01 and v.mean() < ns_.mean()))
760	ST = pd.DataFrame(rows)
761	print(ST.round(4).to_string())
762	print("\ncombinations meeting the criterion:", int(ST.ok.sum()), "of", len(ST))
763	--OUT--
764	   balance quantity sign  mean_sup null  null_sup  p_vs_null_sup  null_exc  p_vs_null_exc     ok
765	0        a        a    a    0.1677  aaa    0.2005         0.0029    0.3956            0.0   True
766	1        a        a    a    0.1677  aab    0.1957         0.0097    0.4449            0.0   True
767	2        a        a    a    0.1677  aba    0.1644         0.8898    0.4986            0.0  False
768	3        a        a    a    0.1677  abb    0.1458         0.2342    0.5234            0.0  False
769	4        a        a    a    0.1677  baa    0.1955         0.0058    0.4034            0.0   True
770	5        a        a    b    0.1538  aaa    0.2072         0.0000    0.4220            0.0  False
[... 359 more lines not kept]
```

**Agent**

I've read the notebook. Next: the full data-check output (it was cut off in my dump) and the helper module.

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_nishimoto_2011.ipynb'))
c=nb['cells'][5]
for o in c['outputs']:
    print(''.join(o.get('text','')))
"
```

```
file cellid monkey  frames  crange  train_rows  nan_in_crange                    val_sets  reps_enh  reps_nat  mean_count  motion_train  motion_enh  motion_nat  stim_min  stim_max  offset
0   ct0001  f0024      f   22000   20000       19501            479               enhanced:2000        11       NaN       0.162         0.327       0.347         NaN       0.0     255.0       0
1   ct0002  f0027      f   22000   20000       19720            260               enhanced:2000        19       NaN       0.087         0.334       0.355         NaN       0.0     255.0       0
2   ct0005  f0032      f   22000   20000       19861            119               enhanced:2000        21       NaN       0.210         0.346       0.373         NaN       0.0     255.0       0
3   ct0006  f0033      f   22000   20000       19976              4               enhanced:2000        20       NaN       0.080         0.344       0.369         NaN       0.0     255.0       0
4   ct0008  f0035      f   42000   40000       38828           1152               enhanced:2000        19       NaN       0.139         0.357       0.385         NaN       0.0     255.0       0
5   ct0009  f0037      f   42000   35794       35370            404               enhanced:2000        21       NaN       0.475         0.317       0.339         NaN       0.0     255.0       0
6   ct0010  f0038      f   22000   20000       19680            300               enhanced:2000        20       NaN       0.073         0.314       0.330         NaN       0.0     255.0       0
7   ct0011  f0039      f   22000   20000       19412            568               enhanced:2000        19       NaN       0.101         0.376       0.413         NaN       0.0     255.0       3
8   ct0013  f0041      f   42000   40000       39173            807               enhanced:2000        20       NaN       1.195         0.356       0.387         NaN       0.0     255.0       0
9   ct0014  f0042      f   42000   40000       39464            51
[... 45 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "mt2.py"
}
```

```
1	"""Loading CRCNS mt-2 and fitting the V1 filter bank model of Nishimoto and Gallant (2011).
2	
3	Each of the 45 files holds one MT neuron: `rawStims` (frames x 128 x 128, uint8, the movie
4	patch around the receptive field), `psths` (spike counts per 83 Hz frame, averaged over
5	repeats; NaN where responses were removed), and `ranges` with `crange` (training frames),
6	`vrange` (validation frames) and, in 15 files, `nrange` (an undocumented subset of
7	`vrange`). The files are streamed from the public S3 bucket; nothing is written to disk.
8	
9	Where each parameter comes from (P = the paper, with its passage; C = the claims file;
10	A = an assumption, with why; S = a standard choice that cannot change a result; D = a
11	deviation forced by compute, stated in the attempt record):
12	
13	- cRF = half the stored patch (C, opening comment, reading (a); the data descriptor says the
14	  patch covers "around 2 times the receptive field", so readings (a) and (b) coincide).
15	- Frames are block-averaged from 128 x 128 to 32 x 32 pixels (16 px per cRF), which keeps
16	  the highest filter frequency, 6 cycles per cRF, below the Nyquist limit of 8 (S).
17	- Filter bank (P, Materials and Methods, "The V1 filter bank"): spatial frequencies 0, 0.75,
18	  1.5, 3 and 6 cycles per cRF ("log distributed from zero to six"; the four non-zero values
19	  are an octave apart, A); envelope SD = half a carrier cycle ("one cycle of the sine wave
20	  was two sigma"); grid spacing 2.2 sigma; 12 directions; simple cells only up to 2 cycles
[... 783 more lines not kept]
```

**Agent**

I've read the helper module. Now checking the archive listing (for the blocked claim) and a few paper passages (luminance normalization, pattern index, quadrant geometry).

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=mt-2/" -o l.xml; python3 -c "
import re;t=open('l.xml').read()
ks=re.findall(r'<Key>([^<]+)</Key>.*?<Size>(\d+)</Size>',t)
print(len(ks)); [print(k,s) for k,s in ks if not k.startswith('mt-2/live/data/ct')]
print('truncated' , re.findall('<IsTruncated>(\w+)',t))"; curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/mt-2/live/checksums.md5 | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s https://crcnsarchive.s3-us-west-2.amazonaws.com/mt-2/live/filelist.txt | head -20; cd paper; grep -n -i -E "luminance|contrast normaliz|pattern index|Smith et al|quadrant|horizontal|trange|repeated|explainable" 10.1523-jneurosci.6801-10.2011.txt | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; sed -n 315,345p 10.1523-jneurosci.6801-10.2011.txt; echo ----; sed -n 684,700p 10.1523-jneurosci.6801-10.2011.txt; echo ---; sed -n 730,750p 10.1523-jneurosci.6801-10.2011.txt; sed -n 140,160p 10.1523-jneurosci.6801-10.2011.txt
```

```
which elements were included or excluded from the model. (The V1
filters were present in all cases and were never switched out of the circuit.)
The switching framework included three kinds of nonlinearity: (1) luminance and contrast normalization placed before the V1 filters, (2) a static
nonlinearity, and (3) divisive normalization.
The luminance and contrast normalization were implemented as a
stimulus preprocessing stage interposed between the movie and the V1
filters:
I��x,y,t��
I�x,y,t��Lum�t�
Con�t�
,
(10)
where the I�(x,y,t) is the normalized luminance. The time course of luminance, Lum(t) was defined as follows:
Lum�t���
x �
y
I�x,y,t�.
(11)
Con(t), the time course of contrast, was defined as follows:
Con�t����
[... 72 more lines not kept]
```

**Agent**

Quick synthetic tests of `pattern_index`, `plane_geometry`/`optimal_plane`/`on_plane_ratio` and `hv_ratio`.

**Agent calls Bash**

```bash
cd  python3 -c "
import numpy as np, mt2
d=np.arange(24)*15.
g=lambda x,k=2: np.exp(k*(np.cos(np.deg2rad(x))-1))
g24=g(d)
pl=np.arange(12)*30.
comp=g(pl-60)+g(pl+60); pat=g(pl)
print('component cell PI', mt2.pattern_index(g24,comp,120), 'pattern cell PI', mt2.pattern_index(g24,pat,120))
rng=np.random.default_rng(0)
print('component+5% noise', mt2.pattern_index(g24,comp+0.05*rng.normal(size=12),120))
print('mix 50/50', mt2.pattern_index(g24,0.5*comp+pat,120))
# plane: synthetic regressors on a velocity plane
rd=[]
for sf in [0.75,1.5,3,6]:
  for dd in np.arange(0,360,30.):
    for tf in [0,3.75,7.5,15,30]:
      rd.append((sf,dd,tf,0,0,0))
rd=np.array(rd)
near,side,TH,V=mt2.plane_geometry(rd)
# true plane: azimuth 90, speed 5 cRF/s ; weight filters with tf ~= 5*sf*cos(d-90)
tfp=5*rd[:,0]*np.cos(np.deg2rad(rd[:,1]-90))
E=np.where((np.abs(rd[:,2]-tfp)<1.5)&(tfp>0),1.0,0.0)
j=mt2.optimal_plane(E,near,side,'a'); print('found az,speed',TH[j],V[j],'ratio',mt2.on_plane_ratio(E,near[:,j]))
print('hv ratio', mt2.hv_ratio(E,rd,TH[j],near[:,j],'a'))
Er=rng.random(len(rd)); jr=mt2.optimal_plane(Er,near,side,'a'); print('random E ratio',mt2.on_plane_ratio(Er,near[:,jr]))
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import numpy as np, mt2
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls ~/.venv* /opt 2>/dev/null | head; which -a python python3; for p in $(which -a python3 python); do $p -c "import numpy,scipy;print('$p ok')" 2>/dev/null; done; pip --version 2>/dev/null
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
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
pip 26.3 from /opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/pip (python 3.13)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -m venv v >/dev/null && v/bin/pip -q install numpy scipy requests h5py fsspec 2>&1 | tail -2; v/bin/python -c "import numpy;print(numpy.__version__)"
```

```
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
2.5.4
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import numpy as np, mt2
d=np.arange(24)*15.
g=lambda x,k=2: np.exp(k*(np.cos(np.deg2rad(x))-1))
g24=g(d)
pl=np.arange(12)*30.
comp=g(pl-60)+g(pl+60); pat=g(pl)
print('component cell PI', mt2.pattern_index(g24,comp,120), 'pattern cell PI', mt2.pattern_index(g24,pat,120))
rng=np.random.default_rng(0)
print('component+5% noise', mt2.pattern_index(g24,comp+0.05*rng.normal(size=12),120))
print('mix', mt2.pattern_index(g24,comp+pat,120))
rd=[]
for sf in [0.75,1.5,3,6]:
  for dd in np.arange(0,360,30.):
    for tf in [0,3.75,7.5,15,30]:
      rd.append((sf,dd,tf,0,0,0))
rd=np.array(rd)
near,side,TH,V=mt2.plane_geometry(rd)
tfp=5*rd[:,0]*np.cos(np.deg2rad(rd[:,1]-90))
E=np.where((np.abs(rd[:,2]-tfp)<1.5)&(tfp>0),1.0,0.0)
print('n true',E.sum())
for b in 'ab':
  j=mt2.optimal_plane(E,near,side,b); print(b,'found az,speed',TH[j],round(V[j],2),'ratio',mt2.on_plane_ratio(E,near[:,j]),'hv',mt2.hv_ratio(E,rd,TH[j],near[:,j],'a'))
Er=rng.random(len(rd)); jr=mt2.optimal_plane(Er,near,side,'a'); print('random E ratio',mt2.on_plane_ratio(Er,near[:,jr]))
"
```

```
mt2.py:553: RuntimeWarning: divide by zero encountered in scalar divide
  Rp = (rp - rc * rpc) / np.sqrt((1 - rc**2) * (1 - rpc**2))
component cell PI 0.0 pattern cell PI 21.76298582899043
component+5% noise -7.508418041804306
mix 0.0
n true 22.0
a found az,speed 90.0 2.55 ratio 0.9999999999999546 hv 1.75
b found az,speed 90.0 2.55 ratio 0.9999999999999546 hv 1.75
random E ratio 0.4227845179652231
```

**Agent**

**Verifier report, round 1: Nishimoto & Gallant (2011) on CRCNS mt-2**

The claims file has 20 claims. The notebook tests 19 and blocks 1. One fact applies to every model-based claim: the notebook does not fit the paper's model. It downsamples the frames from 128 to 32 pixels and pools the bank onto 763 regressors (deviation D in `mt2.py`).

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig3b-mean-prediction | not_reproduced | Cell 11: mean r is 0.448. The best reading gives 0.451 (sigma chosen on held-out data), below the 0.468 lower bound. All 45 neurons fall between 0.2 and 0.8, as in Fig. 3B. The model was pooled for compute (problem 1), so this tests a reduced model. |
| fig3b-explainable-variance | blocked: data_missing | `psths` holds only the mean over repeats. The archive listing has only 45 `.mat` files, docs, `checksums.md5` and `filelist.txt`. No trial-level files exist, so no part can be tested as David & Gallant (2005) specify. |
| fig3a-example-neuron | reproduced | Cell 13: 3 neurons fall in 0.648–0.792 (ct0013 0.710, ct0021 0.708, ct0039 0.730). None of them shows 10 repeats. |
| fig2b-contrast-normalization-no-effect | reproduced | Cell 17: change −0.3% (a), Wilcoxon p = 0.41, ×11 = 1. Enhanced-only p = 0.89. |
| fig2b-compressive-improves | partially_reproduced | Cells 15/19: both increases are significant (×11 p ≈ 1e-7 and 2e-8). No single reading puts both values in tolerance: reading (b) gives 9.2% (expected 16 ± 4) and 16.1% (expected 19 ± 4, within). |
| fig2b-expansive-decreases | partially_reproduced | Cell 21: both decreases are significant. Reading (b) gives −26.9% (expected −36 ± 4, outside) and −24.5% (within). With divisive normalization, the expansive model beats the simplest model in 7 of 45 neurons, against the paper's "always". |
| fig2b-divisive-improves | not_reproduced | Cell 23: reading (b) gives 5.1% (within 8 ± 4), but Wilcoxon p = 0.0051, ×11 = 0.056 and ×5 = 0.026. The criterion needs corrected p < 0.01, and its partial grade also needs a significant increase. |
| fig2b-compressive-divisive-best | reproduced | Cell 25: compressive + divisive beats compressive alone (p = 1.6e-4; ×11 = 0.0017, ×12 = 0.0019). No other model is better: the closest, lum compressive + div, differs by −0.0065 (p = 0.36). |
| fig2b-no-interaction | reproduced | Cell 27: under both readings, with and without divisive normalization, compressive is better and expansive worse, all with ×11 p < 1e-7. |
| complex-cells-dominate | reproduced | Cell 29: complex-only gives mean r 0.448, the same as the full model (r² ratio 1.001). Simple-only drops to 0.194. The simple-only arm is weakened (problem 8), but the first condition alone carries the claim. |
| fig6a-null-on-plane | reproduced | Cell 33: 12 of 40 combinations fall in 0.324–0.396. Under the combination that also passes fig6a and fig6b (plane aaa, null aaa) the null mean is 0.3956, at the tolerance edge. A second consistent combination (plane baa, null aaa) gives 0.378. This null is the paper's chance level (0.36). |
| fig6a-excitatory-on-plane | reproduced | Cell 35: 40 of 40 combinations pass. The mean is 0.55–0.60 and the rank-sum against the null is p ≤ 0.01. |
| fig6b-suppressive-off-plane | reproduced (fragile) | Cell 37: 6 of 40 combinations pass, among them plane aaa with null aaa (0.168 against null 0.201, p = 0.0029), the same combination that passes fig6a. With the null's offset rate reading (b), no combination is significant, and quantity reading (b) puts the mean (0.11) outside tolerance. |
| fig7a-partial-ring | reproduced | Cell 39: 25 of 32 combinations pass, including aaa/a: 71% of neurons between the extremes, 6.7% low, 22% ring. |
| fig7a-no-corr-prediction-hv | partially_reproduced | Cell 41: p > 0.10 in 10 of 16 readings and p < 0.05 in 2. The reading that passes fig6a, fig6b and fig7a (aaa/a) gives r = −0.28, p = 0.061, which is in the partial band. r is negative in all 16 readings. |
| fig7b-pattern-index | not_reproduced | Cell 43: 0 of 4 combinations pass. Medians run from −8.6 to −10.7, and only 0–18% of neurons fall in −6.6 to 2.2. The noise-free simulation (problem 2) may cause part of this. |
| fig7c-hv-pattern-correlation | not_reproduced | Cell 45: 0 of 64 combinations pass. r runs from −0.34 to 0.33, and no positive r reaches p < 0.01. It rests on pattern indices that are themselves not reproduced. |
| fig7c-no-corr-prediction-pattern | reproduced | Cell 47: p > 0.10 in 3 of 4 readings, including the primary one (a, 120°: p = 0.13). The fourth gives p = 0.055. It is a weak test, because the pattern indices are far outside the paper's range. |
| natural-movie-control | partially_reproduced | Cell 49: 14 neurons have `nrange`, against the paper's 15. Wilcoxon p = 0.24. The natural mean, 0.493, is within tolerance; the enhanced mean, 0.462, is below 0.483. The identification of `nrange` as the natural movie rests on its lower motion content in 14 of 14 neurons (cell 5), which is convincing. |
| fig8-recovery-simulated | reproduced | Cell 51: under both noise readings each recovered field correlates best with its own true field (diagonals 0.84/0.57/0.50 and 0.79/0.60/0.67; off-diagonals ≤ 0.13). |

### B. Problems

1. **[affects a conclusion]** `mt2.pooling`, `load`, cells 0/11/19/21/23/43. The fitted model is not the paper's model. The paper fits about 5956 filters at every position; here 32×32 frames are pooled onto 4 or 1 regions (763 regressors), and simple cells enter only at SF 0.75 (one position) and SF 0. The deviation is stated, but its effect is never measured, for example by an unpooled fit on a few small neurons. The shortfall in mean r (0.448 against 0.52), the smaller Fig. 2B effect sizes and the extreme pattern indices may all come from this reduction. The not_reproduced and partially_reproduced outcomes above therefore test a reduced model.
2. **[affects a conclusion]** `pattern_index` and `process_neuron` (plaid block), cell 43. The tuning curves are noise-free model outputs. The Smith et al. Z-scores then grow without bound as the partial correlations approach ±1, so their magnitude depends on numerical detail. My synthetic check: a pure component cell plus 5% noise gives −7.5, against the notebook's medians near −9. Whether, and how, the paper added response variability is an open detail that could change fig7b and fig7c, and only one reading was run. Separately, an exactly pure component cell returns 0.0 (divide by zero at line 553). That case did not occur here (maximum −4.4).
3. **[affects a conclusion]** `boost`, `fit_neuron`. Early stopping uses a patience of 50 steps at 0.01 SD, with `maxit` = 20000. The per-fold iteration counts (`its`) are stored but never printed, so stopping too early or hitting the cap could not be ruled out. Either would lower r (fig3b-mean-prediction).
4. **[does not affect a conclusion]** `bank_outputs` (`CENTRED`) and `shift_rows`. The temporal filters are centred, so a feature reads 5 frames ahead of the response frame, and offsets of 3 or 6 frames (chosen for 14 neurons) extend this to 11 frames ahead. The model is acausal, unlike Eq. 5. The offset is chosen on held-out training data, so validation responses do not leak, and offset 0 for every neuron gives the same mean r (0.448, cell 11). The largest weight share sits at delay 10 (0.131, cell 7), which suggests the delay window is truncated.
5. **[does not affect a conclusion]** `optimal_plane`, balance (a). Coverage ties across speeds are broken by the lowest index. In my synthetic test the true plane (azimuth 90°, speed 5 cRF/s) was found at speed 2.55. The on-plane ratio stayed correct (1.0), but `near_col`, and so the HV ratio, depends on the speed picked. The fig7a outcome is robust (25 of 32).
6. **[does not affect a conclusion]** `hv_ratio`. A regressor's quadrant is set by its SF-direction angle, not its position within the tilted plane, which biases the ratio toward horizontal for fast planes. This is stated in the docstring.
7. **[does not affect a conclusion]** Cell 33. Null movie reading (b) was run only with rate and delay readings (a,a). The claims file asks for every combination to be shown.
8. **[does not affect a conclusion]** `pooling`. The simple-only model lacks the SF 1.5 simple cells and every position but one. This makes the second condition of complex-cells-dominate easy to meet, though the first condition carries the outcome.
9. **[does not affect a conclusion]** `_process`, repeats estimate. It reports up to 33 repeats, while the paper says 5–20, so the estimator is unreliable. It only feeds the fig3a listing.
10. **[does not affect a conclusion]** Cell 5. ct0133 keeps 7093 of 19842 training frames (12729 removed) and enters every test without comment. Separately, for neurons with gaps the lag-product Gram in `Fold` is approximate. It changes only the boosting path, since early stopping uses exact held-out predictions.

### C. What I could not check

- Whether fits stopped at `maxit` or too early. Needed: per-neuron, per-fold `its` for the main model.
- Whether pooling or downsampling lowers accuracy. Needed: an unpooled fit, or a finer pooling, on 2–3 of the 22000-frame neurons, compared with the pooled r.
- The full HDF5 contents, to confirm the blocked claim beyond the archive listing. `read_meta` reads `trange` but never reports it. Needed: the key list and the shape and content of `trange` for one file, to confirm no trial-level responses exist.
- The fig3a candidates among neurons with 10 repeats. Needed: r for ct0028 and ct0030.
- The sensitivity of the pattern index to response noise. Needed: indices with Poisson or trial-like noise added to the simulated grating and plaid responses.
- That the validation segments are contiguous and NaN-free, which `val_corr`'s smoothing and trimming assume. Needed: a printed check per set.

## End of run

16 turns, 5 minutes, $1.57 at API prices, result: success.
