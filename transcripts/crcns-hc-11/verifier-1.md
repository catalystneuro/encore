# crcns-hc-11 · verifier-1 · run 42381718866

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 280
drwxr-xr-x 6 runner runner    4096 Nov  7 15:06 .
drwxr-xr-x 7 runner runner    4096 Nov  7 15:06 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  7 14:26 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  7 14:26 .bashrc
drwxr-xr-x 5 runner runner    4096 Nov  7 15:06 .claude
-rw-r--r-- 1 runner runner       0 Nov  7 15:06 .env
-rw-r--r-- 1 runner runner       0 Nov  7 15:06 .env.development
-rw-r--r-- 1 runner runner       0 Nov  7 15:06 .env.development.local
-rw-r--r-- 1 runner runner       0 Nov  7 15:06 .env.local
-rw-r--r-- 1 runner runner       0 Nov  7 15:06 .env.production
-rw-r--r-- 1 runner runner       0 Nov  7 15:06 .env.production.local
-rw-r--r-- 1 runner runner       0 Nov  7 15:06 .env.test
-rw-r--r-- 1 runner runner       0 Nov  7 15:06 .env.test.local
drwx------ 2 runner runner    4096 Nov  7 15:06 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  7 14:26 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  7 14:26 .github
-rw-r--r-- 1 runner runner       0 Nov  7 15:06 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Nov  7 14:26 .idea
[... 41 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.1126-science.aad1935.yaml"
}
```

```
1	# Claims for Grosmark & Buzsaki (2016), Science 351:1440-1443, on CRCNS data set hc-11
2	# (doi:10.6080/K0862DC5).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-07,
4	# protocol as stated in docs/protocol.md (Reader).
5	#
6	# Text read: the NIH author manuscript in PubMed Central (PMC4919122), as supplied under paper/,
7	# with the main text and the legends of Figures 1 to 4, and its supplement (Materials and
8	# Methods, Figures S1 to S22 with legends, references; PDF from PMC, text by PyMuPDF). The
9	# images of the main Figures 1 to 4 are not under paper/, so numbers and significance marks
10	# printed only inside those panels are not recorded here. The supplement PDF was rendered to
11	# read the supplementary panels: values printed in panel titles (Figures S5, S9, S12, S13, S14,
12	# S16 to S19) are marked as read from a figure; the text extraction does not hold them, so the
13	# quote checker cannot find their p-values. The paper links no analysis code ("Spike and LFP
14	# data are available at CRCNS.org"); none was read.
15	#
16	# Main-text figure numbers for supplementary figures are off by one in places: the main text
17	# cites figs. S16 and S17 for pair-wise coactivity and temporal bias, which are Figures S17 and
18	# S18 of the supplement, and fig. S12 for the exclusion analysis that the Methods call fig. S8.
19	# The claims below cite the supplement's own numbering.
20	#
[... 909 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_grosmark_2016.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--');print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('ERROR',o['ename'],o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
2062 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	==================== 0 markdown
2	# Grosmark & Buzsáki (2016) on CRCNS hc-11
3	
4	Paper: Grosmark, A. D. and Buzsáki, G. (2016). Diversity in neural firing dynamics supports both rigid and learned hippocampal sequences. Science 351, 1440-1443, doi:10.1126/science.aad1935. The claims file (`claims/crcns-hc-11/10.1126-science.aad1935.yaml`) was written from the NIH author manuscript in PubMed Central (PMC4919122) and its supplement (Materials and Methods, Figures S1 to S22).
5	
6	Dataset: CRCNS hc-11, doi:10.6080/K0862DC5, read from the public bucket at `https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-11/live/`. Version: CRCNS data sets are not versioned, so the version is recorded as `unversioned`; the paper cites no version, and the `live/` folder is the only copy of the data files (the `old/` and `orig/` folders hold only earlier descriptions). The one file read is `data/NoveltySessInfoMatFiles.tar.gz`, MD5 `2666ee13c8c1e3609c08c6f4ba444d11` in the data set's `checksums.md5`, so that a later change can be detected. It is streamed and decompressed in memory; the eight `<session>_sessInfo.mat` files in it hold the spike times, cluster identities with putative cell types, position and the state epochs. The LFP (`*_eeg.tar.gz`, 5 to 10 GB each) and the per-shank spike files are not read (see the deviations).
7	
8	What differs from the paper's method throughout, as stated in `hc11.py` and the attempt record:
9	
10	- Ripple events are the paper's population synchrony events without the condition that each holds the peak of an LFP-detected ripple: the LFP is only in tar.gz archives of 70 GB in all, which stream at about 23 MB/s (about 55 minutes), and the detector is not described.
11	- Offline states are the data set's own state epochs (reading S-a of the claims file): NREM, Drowsy (quiet waking) and Intermediate. On the maze, where the epochs mark only Wake, offline is time not running on the track (an assumption; 2D head speed under 5 cm/s is shown as a variant fo
[... 701 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 713,
 "limit": 700
}
```

```
713	> Splitting strongly contributing cells at each session's median dPCC gives 105 rigid and 105 plastic cells.
714	
715	Source: Materials and Methods, Rigid and Plastic Cell Classification.
716	
717	Criterion (claims file): Classification as in the opening comment (per session and running direction, the median cell dropped for odd counts). Reproduced when both counts are within tolerance.
718	==================== 25 code
719	print(f2b[["Y", "D", "P", "strong", "rigid", "plastic"]].to_string())
720	print("expected 105 +- 10.5 each")
721	MAIN = classify(UNITS[("a", "a")], "a")  # readings Y-a, D-a, P-a for the claims that use the groups
722	print("groups used below (Y-a, D-a, P-a):", MAIN.group.value_counts().to_dict())
723	print(MAIN[MAIN.group != ""].groupby(["session", "group"]).size().unstack().to_string())
724	--OUT--
725	    Y  D  P  strong  rigid  plastic
726	0   a  a  a     247    121      121
727	1   a  a  b      36     16       16
728	2   a  b  a     222    109      109
729	3   a  b  b      22      9        9
730	4   b  a  a     251    121      121
731	5   b  a  b      39     16       16
732	6   b  b  a     232    113      113
[... 680 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 1413,
 "limit": 660
}
```

```
1413	RUN-POST: rigid 0.176 vs plastic 0.256, Fisher z = -1.56, p = 0.119; stated direction (plastic higher) holds: True
1414	
1415	==================== 50 markdown
1416	## figs18-temporal-bias
1417	
1418	> Pair-wise temporal biases are not preserved from PRE to RUN (r = -0.009) but are preserved from RUN to POST (r = 0.117) and PRE to POST (r = 0.201); the PRE to POST preservation is carried by rigid cell pairs (r = 0.29) and the RUN to POST preservation by plastic cell pairs (r = 0.26).
1419	
1420	Source: Figure S18B and S18C (r values read from the panels); Results, paragraph 4.
1421	
1422	Criterion (claims file): Temporal bias and its median r over 1,000 sign randomisations as in the opening comment. The PRE-RUN value is near zero; its tolerance of 0.05 reads it as consistent with zero. Reproduced when the PRE-RUN r is not significant (p > 0.05), RUN-POST and PRE-POST are (p < 0.05), the rigid PRE-POST and plastic RUN-POST r are significant while the plastic PRE-POST (-0.037) and rigid RUN-POST (0.024) are not, and the values are within tolerance; partially reproduced when the significance pattern holds and a value does not.
1423	==================== 51 code
1424	rng18 = np.random.default_rng(18)
1425	
1426	
1427	def bias_similarity(df, e1, e2, n_perm=1000):
1428	    d = df[(df[f"n_{e1}"] >= 40) & (df[f"n_{e2}"] >= 40)][[f"bias_{e1}", f"bias_{e2}"]].dropna().values
1429	    if len(d) < 4:
1430	        return len(d), np.nan, np.nan
1431	    rs, ps = [], []
1432	    for _ in range(n_perm):
[... 631 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "hc11.py"
}
```

```
1	"""Loading and measures for CRCNS hc-11 (Grosmark & Buzsaki 2016, Science 351:1440).
2	
3	Everything is read from the eight sessInfo .mat files in
4	NoveltySessInfoMatFiles.tar.gz, streamed from the public CRCNS bucket and
5	decompressed in memory. Sources of the parameters below:
6	
7	- [M] the paper's supplement, Materials and Methods, as cited by the claims file's
8	  opening comment or by the section named;
9	- [A] an assumption, said what and why, and listed as a deviation in the record;
10	- [S] a standard choice for a detail that cannot change a result.
11	"""
12	import io
13	import tarfile
14	from concurrent.futures import ThreadPoolExecutor
15	
16	import fsspec
17	import h5py
18	import numpy as np
19	from scipy.ndimage import gaussian_filter1d
20	
[... 558 more lines not kept]
```

**Agent**

Notebook, helper module and claims file are read. Next I'm checking the archive file list for the blocked claim and the LFP deviation, and testing a few helpers on synthetic input.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/?list-type=2&prefix=hc-11/live/" -o list.xml; python3 - <<'E'
import re
x=open('list.xml').read()
for k,s in re.findall(r'<Key>(.*?)</Key>.*?<Size>(\d+)</Size>',x):
    print(f"{int(s)/1e9:8.3f} GB  {k}")
print(re.findall(r'<IsTruncated>(.*?)</IsTruncated>',x))
E
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-11/live/filelist.txt" | head -80; echo; curl -s "https://crcnsarchive.s3-us-west-2.amazonaws.com/hc-11/live/checksums.md5" | grep -i sessinfo
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd paper; grep -n -i -E "intermediate|drowsy|\.fet|\.clu|\.res|\.spk|_spk|eeg|ripple|tar" hc-11.data-description.txt | head -60
```

```
51:supplementary methods of Grosmark and Buzsáki, 2016 and are similar to those of 
61:There are eight sessions. Data for each session is supplied in three “.tar.gz” files, with 
62:names like: “X_eeg.tar.gz”, “X_spk.tar.gz” and “X.tar.gz”, where “X” is the base name of 
63:the session, e.g. “Achilles_10252013”. The “X_eeg.tar.gz” file contains the LFP file, the 
64:“X_spk.tar.gz” contains the spike waveforms, and the “X.tar.gz” file contains everything 
68:executing the following command in the directory containing the downloaded tar.gz files: 
69:find *.tar.gz -exec tar xzf {} \;  (e.g. if X.tar.gz and X_eeg.tar.gz are both 
71:contents of both of the .tar.gz files). The end result of download all the files and running 
76:were performed at 20 kHZ, and downsampled to 1250 HZ to produce the ‘*.eeg’ (LFP) 
87:‘NoveltySessInfoMatFiles.tar.gz’. A summary pdf (‘HC-11_Recording_Summary.pdf’) 
106:>> baseName.eeg – binary file containing the downsampled (to 1250 HZ) 
109:>> baseName.N.spk – (where N is a shank-number) binary file containing the 
113:>> baseName.N.res  - binary file containing spike times (in 20 kHZ sampling 
116:>> baseName.N.fet – binary file containing PCA features (3 per recording site on 
119:>> baseName.N.clu – binary file containing the cluster ID’s assigned to each 
121:noise, and cluster ‘1’ corresponds to putative none-clustarable multi-units.  
127:‘NoveltySessInfoMatFiles.tar.gz’ file). These '.mat' files were saved with the '-v7.3' flag 
185:momentarily outside the field of view of the cameras or when the position 
196:timestamp vector does not start at 0. 
203:>> sessInfo.Epochs.PREEpoch: [start, end] vector indicating the beginning and 
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n 55,125p hc-11.data-description.txt; sed -n 215,258p hc-11.data-description.txt
```

```
MAZE running for these animals.  
 
 
Data files organization 
 
 
There are eight sessions. Data for each session is supplied in three “.tar.gz” files, with 
names like: “X_eeg.tar.gz”, “X_spk.tar.gz” and “X.tar.gz”, where “X” is the base name of 
the session, e.g. “Achilles_10252013”. The “X_eeg.tar.gz” file contains the LFP file, the 
“X_spk.tar.gz” contains the spike waveforms, and the “X.tar.gz” file contains everything 
else (e.g. cluster assignments, spike times, ...). After downloading and unpacking, all 
files associated with the same session (e.g. having the same prefix “X”) should be in the 
same directory, which will be named “X”. On Unix systems this can be accomplished by 
executing the following command in the directory containing the downloaded tar.gz files: 
find *.tar.gz -exec tar xzf {} \;  (e.g. if X.tar.gz and X_eeg.tar.gz are both 
downloaded, executing the command will create a folder named X containing the 
contents of both of the .tar.gz files). The end result of download all the files and running 
the above command will be eight folders containing data corresponding to each of the 
eight novelty sessions. 
Each folder contains the concatenated pre-processed data associated with each 
[... 95 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import numpy as np, hc11
rng=np.random.default_rng(0)
# weighted correlation vs direct formula (eqs 3-5)
P=40; nbins=[7,5,9]
posts=[rng.dirichlet(np.ones(P)*0.3,size=k) for k in nbins]
Ep=np.concatenate([p@np.arange(P) for p in posts]); Ep2=np.concatenate([p@np.arange(P)**2 for p in posts])
evb=np.repeat(np.arange(3),nbins); tb=np.concatenate([np.arange(k) for k in nbins]).astype(float)
r=hc11._wcorr_from_moments(Ep,Ep2,evb,np.array(nbins),tb)
def direct(Pm):
    T,X=np.meshgrid(np.arange(Pm.shape[0]),np.arange(P),indexing='ij'); w=Pm
    mx=(w*X).sum()/w.sum(); mt=(w*T).sum()/w.sum()
    c=lambda a,b:(w*(a-mx if a is X else a-mt)*(b-mx if b is X else b-mt)).sum()/w.sum()
    return c(X,T)/np.sqrt(c(X,X)*c(T,T))
print(r,[direct(p) for p in posts])
# intervals
iv=np.array([[0,10],[20,30],[40,45]])
print(hc11.last_T(iv,12), hc11.first_T(iv,12))
print(hc11.in_intervals(np.array([0,9.99,10,25,44.9,45]),iv))
# spatial info: uniform rate -> 0; single bin -> log2(1/p)
occ=np.ones(10); print(hc11.spatial_info(np.ones(10),occ), hc11.spatial_info(np.r_[10,np.zeros(9)],occ))
print(hc11.min_participants(30),hc11.min_participants(75))
# yoke check on fake session
ses=dict(pre=(0,100),post=(150,200),states={k:np.zeros((0,2)) for k in ("NREM","Drowsy","Intermediate")})
ses["states"]["NREM"]=np.array([[0,100],[150,200]])
print(hc11.yoke(ses,"a"),hc11.yoke(ses,"b"),hc11.yoke(ses,"c"))
E
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls node_modules; which -a python3 python; ls ~/.venv* /opt 2>/dev/null | head; pip --version 2>&1 | head -2
```

```
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.18/x64/bin/python
/opt/hostedtoolcache/Python/3.13.18/x64/python
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
pip 26.2.2 from /opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/pip (python 3.13)
```

**Agent calls Bash**

```bash
for p in /usr/bin/python3; do $p -c "import numpy,scipy;print(numpy.__version__)"; done 2>&1; python3 -m venv $TMPDIR/v && $TMPDIR/v/bin/pip -q install numpy scipy h5py fsspec 2>&1 | tail -2
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import numpy,scipy;print(numpy.__version__)
    ^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'numpy'
[notice] A new release of pip is available: 26.2.2 -> 26.3
[notice] To update, run: /tmp/claude-1001/v/bin/python3 -m pip install --upgrade pip
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python3 - <<'E'
import numpy as np, hc11
rng=np.random.default_rng(0)
P=40; nbins=[7,5,9]
posts=[rng.dirichlet(np.ones(P)*0.3,size=k) for k in nbins]
Ep=np.concatenate([p@np.arange(P) for p in posts]); Ep2=np.concatenate([p@np.arange(P)**2 for p in posts])
evb=np.repeat(np.arange(3),nbins); tb=np.concatenate([np.arange(k) for k in nbins]).astype(float)
r=hc11._wcorr_from_moments(Ep,Ep2,evb,np.array(nbins),tb)
def direct(w):
    T,X=np.meshgrid(np.arange(w.shape[0]),np.arange(P),indexing='ij')
    mx=(w*X).sum()/w.sum(); mt=(w*T).sum()/w.sum()
    cxt=(w*(X-mx)*(T-mt)).sum()/w.sum(); cxx=(w*(X-mx)**2).sum()/w.sum(); ctt=(w*(T-mt)**2).sum()/w.sum()
    return cxt/np.sqrt(cxx*ctt)
print("wcorr",r,[round(direct(p),6) for p in posts])
iv=np.array([[0,10],[20,30],[40,45]])
print("lastT",hc11.last_T(iv,12).tolist(),"firstT", hc11.first_T(iv,12).tolist())
print(hc11.in_intervals(np.array([0,9.99,10,25,44.9,45]),iv))
occ=np.ones(10); print("info",hc11.spatial_info(np.ones(10),occ), hc11.spatial_info(np.r_[10,np.zeros(9)],occ), np.log2(10))
print(hc11.min_participants(30),hc11.min_participants(75))
ses=dict(pre=(0,100),mz=(100,150),post=(150,200),states={k:np.zeros((0,2)) for k in ("NREM","Drowsy","Intermediate")})
ses["states"]["NREM"]=np.array([[0,100],[150,200]])
for y in "abc": print("yoke",y,[a.tolist() for a in hc11.yoke(ses,y)])
# smoothing kernel SD
v=np.zeros(101); v[50]=1; s=hc11.smooth(v); x=np.arange(101)*2
print("kernel SD cm", np.sqrt((s*(x-100)**2).sum()/s.sum()))
# rotate_smooth with 0 shift vs smooth(raw)
raw=rng.random((3,20)); print(np.allclose(hc11.rotate_smooth(raw,np.zeros(3,int)),hc11.smooth(raw,axis=1)))
# ripple_events on synthetic: spikes after duration
E
```

```
wcorr [ 0.13189625 -0.23229498  0.17536292] [np.float64(0.131896), np.float64(-0.232295), np.float64(0.175363)]
lastT [[23.0, 30.0], [40.0, 45.0]] firstT [[0.0, 10.0], [20.0, 22.0]]
[ True  True False  True  True False]
info (0.0, 0.0) (3.321928094887362, 3.321928094887362) 3.321928094887362
5 8
yoke a [[[50.0, 100.0]], [[150.0, 200.0]]]
yoke b [[[0.0, 50.0]], [[150.0, 200.0]]]
yoke c [[[50.0, 100.0]], [[150.0, 200.0]]]
kernel SD cm 4.998877201961305
True
```

**Agent**

A. Outcomes per claim (31 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| place-cell-count | partially_reproduced | Cell 7: 562 pyramidal cells (exact match), but 565 place units, outside 491 ± 49.1. The percentage is 62.1% under reading (a) and 100.5% under (b), both outside 54 ± 5.4. With the 5 cm kernel read as FWHM (cell 8) there are 504 units and 55.4%, both within tolerance. So the outcome depends on a kernel reading the claims file leaves open. |
| fig1c-sequence-content | reproduced | Cell 10: every condition holds in 12 of 12 Y × D × maze-offline combinations. Caveat: the L and S-b readings were never run, because events lack the LFP condition (problem 1). In the per-animal comparison (cell 11), Buddy has POST above PRE and MAZE not highest, the reverse of Figure S6. |
| figs5b-abs-r-above-null | reproduced | Cell 13: observed \|r\| exceeds the one-draw null in every epoch under every reading (p ≤ 1e-31). The bootstrap interval of dObs − dNull is above zero under all six readings. |
| figs5e-duration-unchanged | reproduced | Cell 15, reading (b) replay events: medians 172–173 ms against 183/186 ± 18, rank-sum p = 0.48–0.91. Reading (a) misses (144/143 ms, p < 0.001), which is expected because the LFP condition was dropped. |
| figs5f-more-participation-post | reproduced | Cell 17: POST > PRE at p ≤ 3e-88 under every Y reading. Per session, 2 of 8 sessions go the other way (problem 9). |
| figs9b-pcc-post-higher | partially_reproduced | Cell 19: both tests hold under every reading (rank-sum p ≤ 1.3e-4, signed-rank p ≤ 5e-8). POST median 0.10 (expected 0.183 ± 0.018) and dPCC 0.08–0.12 (expected 0.159 ± 0.016) are outside tolerance everywhere. The PRE median is outside under Y-a D-a (0.0121 > 0.009). |
| fig2b-strong-contributors | partially_reproduced | Cell 21: no reading puts all four counts within tolerance. Under D-b with P-a the total (222–232) is within tolerance but PRE (109–119) is not. Under D-a even the total (247–252) is out. P-b gives 22–39 cells, below the roughly 55 expected by chance. |
| fig2-pre-contributors-persist | reproduced | Cell 23, P-a with D-a: 73.9%, 72.7%, 71.7% under Y-a, Y-b, Y-c, all within 73 ± 7.3. Under D-b it is 59.7–65.1%, all outside. |
| rigid-plastic-counts | partially_reproduced | Cell 25: under D-b with P-a there are 108–113 per group, within 105 ± 10.5. Under D-a, the reading used for every downstream claim, there are 121–123, outside. |
| fig2d-high-dpcc-shuffle-abolishes-replay | reproduced | Cell 67: shuffling from the highest dPCC, the change first goes ≤ 0 at 10% (−0.003). Shuffling from the lowest, it stays above zero (lower bound > 0) up to 75%. Run only under Y-a, D-a, with 100 templates per step (a 1,000-template check at 15% agrees). |
| figs12-high-dpcc-exclusion | reproduced | Cell 69: excluding from the highest dPCC, the change first goes below zero at 15%. Excluding from the lowest, the lower bound stays above zero up to 75%. Run only under Y-a, D-a, with 200 null shuffles. |
| figs2-rigid-plastic-along-track | reproduced | Cell 30: KS p = 0.39 and end-distance rank-sum p = 0.22. Both groups are enriched in the outer fifths (0.64 and 0.71, against 0.40 for a uniform spread). |
| fig3a-plastic-more-specific | partially_reproduced | Cell 32: plastic cells are higher on all five specificity measures, p = 2e-5 to 0.013, under both stability readings. Number of fields: medians 1 against 1, p = 0.51; plastic is lower only in mean and geometric mean. |
| fig3b-plastic-specificity-increases | not_reproduced | Cell 34: plastic r = +0.052 (p = 0.10), rigid p = 0.15, plastic > rigid p = 0.48. |
| figs13-outfield-rate-falls | reproduced | Cell 36: plastic out-of-field rate falls (p(<0) = 0.015) and rigid does not (0.12). Overall rate: neither group differs from zero two-sided (0.10, 0.94). Within-field: neither group rises (p(>0) = 0.33, 0.80). |
| fig4a-rigid-fire-faster | not_reproduced | Cell 38: session-wide offline p = 0.09–0.10 and POST p = 0.31, both not significant. Only PRE is significant (p ≈ 0.002–0.003). Rigid median 0.66–0.68 Hz is outside 0.76 ± 0.076. |
| figs14-plastic-ripple-gain | not_reproduced | Cell 40: POST gain p = 0.057 two-sided (0.029 one-sided). Change in gain p = 0.15 (0.074 one-sided). The plastic POST median (5.01) and rigid change median (0.55) are outside tolerance. |
| figs14-plastic-ripple-bursting | not_reproduced | Cell 42: the POST test holds (p = 0.007) and both POST medians are within tolerance. The change test fails: p = 0.93, and the direction is reversed (plastic 0.43, rigid 0.77 points). |
| figs16ab-plastic-synchrony-increase | reproduced | Cell 45: ripple-triggered rate rises in plastic cells (p = 0.002; peak bin 0.001) and not in rigid cells (0.73). Coactivity change, plastic > rigid: reading (c) p = 0.035 one-sided (0.07 two-sided), reading (d) p = 3.5e-7. |
| low-high-rate-split | reproduced | Cell 53: all six split readings give medians within tolerance (low 0.355–0.395 Hz, high 1.02–1.09 Hz). |
| figs16c-low-rate-coding | partially_reproduced | Cell 55, split (a, i): all four tests hold. The high-rate information median (0.47), high-rate geometric-mean field count (1.40), and both gain-change medians (0.64, 0.31) are outside tolerance. Under the three PRE-rate splits (ii), the gain-change difference reverses (low 0.37 < high 0.555), so the claim fails under half the matching readings (problem 4). |
| fig4c-coactivation-by-rate | partially_reproduced | Cell 57: reading (a), within-session ranks, meets every condition. Reading (b), pooled ranks, fails the Figure S16C condition (low-half > high-half p = 0.64). |
| fig4d-slow-cells-replay | partially_reproduced | Cell 59: low-rate POST − PRE is above zero under every reading. High-rate also increases significantly (diff 0.027–0.065, CI above 0), though always by less than low-rate. Only split (a, i) was run. |
| fig4e-high-gain-cells-replay | partially_reproduced | Cell 61: high-gain increases under every reading. Low-gain is significant under D-a by rank-sum (p = 0.002–0.015), and its bootstrap interval excludes zero under Y-b and Y-c with D-a. It is not significant under D-b. Its increase is always smaller than high-gain's. |
| figs16de-more-ripples-post | not_reproduced | Cell 65: POST intervals are shorter (p ≈ 1e-17), but medians are 1.35/1.24 s against 3/2.47 s. LFP-SWR intervals were not tested. The events are not the claim's events (no LFP peak), so this is not a fair test of the medians. |
| figs17-coactivity-preservation | partially_reproduced | Cell 47: the order PRE-RUN < RUN-POST < PRE-POST holds and both Fisher tests are significant. PRE-RUN 0.054, PRE-POST 0.393 and the difference 0.227 are outside tolerance. |
| figs17d-rigid-plastic-coactivity | not_reproduced | Cell 49: all three directions hold, but only PRE-POST differs significantly (p = 8e-12). PRE-RUN gives p = 0.10 and RUN-POST p = 0.12. |
| figs18-temporal-bias | not_reproduced | Cell 51: all-pairs PRE-RUN is significant (median p = 0.044); the claim requires it not to be. Plastic RUN-POST is 0.177, outside 0.26 ± 0.026. The rest of the pattern holds. A narrow miss. |
| figs11-cluster-quality-similar | blocked (other: not attempted) | Cell 70. The archive's `<session>.tar.gz` files hold `.fet/.clu/.res` (11.7 GB in total; the notebook itself estimates about 8 minutes to stream), so quality and stability were testable. Waveform similarity needs the `_spk.tar.gz` files, 87 GB in total. |
| fig2e-plastic-removal | reproduced | Cell 63: with plastic cells removed, the interval reaches ≤ 0 under all six Y × D readings (diff −0.010 to −0.022). With rigid cells removed, it stays well above zero (lower bound ≥ 0.108). Groups are from D-a only. |
| figs19c-pcc-change-per-cell | not_reproduced | Cell 27: PRE > POST is 3.7–6.4% (expected 2.2 ± 0.22) and POST > PRE is 13.5–15.9% (expected 21.4 ± 2.14). The PRE > POST value is at the 5% chance level of a one-tailed p < 0.05 test, while the paper's 2.2% is below it. |

Tally: 12 reproduced, 10 partially reproduced, 8 not reproduced, 1 blocked.

B. Problems

1. [affects a conclusion] `hc11.ripple_events` / `ripple_selected`: events omit the paper's condition that each holds an LFP-detected SWR peak. The L-a and L-b readings, which the fig1c criterion requires ("under all readings of Y, L, S and D"), were never run, and neither was S-b. The archive holds the LFP (`*_eeg.tar.gz`, 69.7 GB), so this was a choice, not a data limit. Cell 65 shows the effect: median event intervals are 1.35 s against the paper's 3 s, so the notebook has roughly twice as many events, about the rate of the paper's LFP-SWRs (1.21 s). Every event-based claim rests on this deviation. figs5e reading (a) and figs16de fail directly because of it.
2. [affects a conclusion] Cell 25 (`MAIN`): every rigid/plastic claim uses Y-a, D-a, P-a. That combination gives 121/121, outside tolerance, while D-b gives 108–113, matching the paper. The notebook calls this "an assumption" without justification. The following claims were never run on D-b groups: fig4a, figs14 (both), figs16ab, figs17d, figs18, fig3a/3b, figs13, figs2, and the group membership in fig2e. Of these, fig4a, figs14 and figs17d are near the threshold (p = 0.057–0.12), so D-b groups could change their outcomes.
3. [affects a conclusion] Cells 7–8: only the FWHM kernel reading matches the 491 place-cell count, but every downstream analysis uses the SD reading (565 units). Unit counts feed the PCC scale (× participating cells), strong-contributor counts, percentages and group sizes.
4. [affects a conclusion] Cells 53, 55, 59: all six split readings match, and the claims file says "the reading(s) that match fix the split". The notebook ran only the first, (a, i). figs16c reverses its gain-change result under the (ii) readings. fig4d and fig4e were not run under the other splits.
5. [affects a conclusion] Cells 67 and 69: fig2d and figs12 criteria say "under readings Y and D", but only Y-a, D-a were run, with 100 templates per step for fig2d and 200 null shuffles for figs12. The 10% step in fig2d (−0.003) sits essentially at zero.
6. [does not affect a conclusion] Cells 38/40/42/45 (`OFFG`, `ps`): units are counted per direction, so 14 "mixed" cells sit in both groups and cells with fields in both directions appear twice. This pseudo-replication slightly inflates the per-cell tests.
7. [does not affect a conclusion] Cells 10/13/17 under D-a: each linear-maze event enters twice (once per template), and the events are pooled as if independent. D-b results agree.
8. [does not affect a conclusion] Cells 40/42/45: one-sided p-values are printed next to two-sided ones. For POST gain (0.029 against 0.057) and coactivity reading (c) (0.035 against 0.07), the verdict depends on which is used. MATLAB's `ranksum` default, presumably the paper's, is two-sided.
9. [does not affect a conclusion] Cell 17 (figs5f): events are pooled across sessions with unequal PRE/POST counts. Cicero_09012014 and Cicero_09172014 have high participation and many more POST events, so composition inflates p = 1e-88. The per-session direction is 6 of 8. A within-session test is missing.
10. [does not affect a conclusion] `hc11.ripple_events`: in Gatsby_08022013, 1,589 s of spikes past `sessDuration` (cell 2) are clipped into the last 1 ms bin, which can create a spurious event at the session end. `rate_sess_all` also counts those spikes.
11. [does not affect a conclusion] Cell 28 `laps`: Cicero_09102014, a circular session with 10 minutes of running, has 23 laps, against 81–82 for the other circular sessions. Tracking gaps probably split laps, and segments covering under half the track are dropped. This affects the per-lap measures for fig3b and figs13.
12. [does not affect a conclusion] `hc11.maze_immobile('notrun')`: MAZE offline time is everything that is not running at 5 cm/s or more along the track, including slow movement. The 2-D variant gives the same fig1c result.
13. Helper checks on synthetic input all passed: weighted correlation against a direct implementation of eqs. 3–5, interval helpers, yoking (Y-a/b/c), the kernel SD (5.00 cm), Skaggs information, `min_participants`, and `rotate_smooth` with zero shift. The Tukey-Kramer q formula and the offline-state choice (Drowsy plus Intermediate, per the data description) are reasonable.

C. What I could not check

- How many events would survive the LFP-SWR condition, and whether that changes any event-based result. Outputs that would help: candidate-event counts after each selection step, and events per hour of NREM per session, compared with the paper's 3 s interval.
- The rigid/plastic claims under D-b (and P-a) groups, and the dependent claims under the FWHM place-field reading. Outputs needed: the cell 38–51 tables rerun on `classify(UNITS[('a','b')])` and on FWHM-derived units.
- fig4d, fig4e and figs16c under the five unused rate splits. Output needed: the SUBTAB rows for each `SPLITS` key.
- fig2d and figs12 under Y-b, Y-c and D-b.
- Lap segmentation quality. Output needed: laps per session against running time, and a sample lap raster.
- A within-session (stratified) test for figs5f and fig1c.
- Whether the sessInfo file read matches MD5 `2666ee13…`. The archive's `checksums.md5` lists that value, but the notebook never prints a computed hash.
- figs11: the cluster-quality and stability parts can be tested from `<session>.tar.gz`; the waveform part needs `_spk.tar.gz`.

## End of run

16 turns, 5 minutes, $2.01 at API prices, result: success.
