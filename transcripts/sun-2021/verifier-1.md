# 001878 · verifier-1 · run 39220514890

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls docs paper 2>/dev/null; cat *claims* 2>/dev/null | head -200
```

```
total 292
drwxr-xr-x 5 runner runner    4096 Oct 19 08:11 .
drwxr-xr-x 7 runner runner    4096 Oct 19 08:11 ..
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 19 08:06 .bash_profile
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 19 08:06 .bashrc
drwxr-xr-x 5 runner runner    4096 Oct 19 08:11 .claude
-rw-r--r-- 1 runner runner       0 Oct 19 08:11 .env
-rw-r--r-- 1 runner runner       0 Oct 19 08:11 .env.development
-rw-r--r-- 1 runner runner       0 Oct 19 08:11 .env.development.local
-rw-r--r-- 1 runner runner       0 Oct 19 08:11 .env.local
-rw-r--r-- 1 runner runner       0 Oct 19 08:11 .env.production
-rw-r--r-- 1 runner runner       0 Oct 19 08:11 .env.production.local
-rw-r--r-- 1 runner runner       0 Oct 19 08:11 .env.test
-rw-r--r-- 1 runner runner       0 Oct 19 08:11 .env.test.local
drwx------ 2 runner runner    4096 Oct 19 08:11 .git
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 19 08:06 .gitconfig
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 19 08:06 .github
-rw-r--r-- 1 runner runner       0 Oct 19 08:11 .gitmodules
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 19 08:06 .idea
crw-rw-rw- 1 nobody nogroup   1, 3 Oct 19 08:06 .mcp.json
[... 18 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.22002-d1.1991.yaml
```

```
# Claims for the CalMS21 dataset (Sun et al. 2021) on dandiset 001878.
#
# The target's DOI, 10.22002/D1.1991, is the CaltechDATA record of the dataset, not a paper. The
# paper that describes the dataset and is cited by that record is Sun, Karigo, Chakraborty,
# Mohanty, Wild, Sun, Chen, Anderson, Perona, Yue and Kennedy (2021), "The Multi-Agent Behavior
# Dataset: Mouse Dyadic Social Interactions", NeurIPS 2021 Datasets and Benchmarks track,
# arXiv:2104.02710v4. Its full text is open access and was used, including the appendix with the
# datasheet (Appendix B), the data format (C), the dataset preparation (D) and the results tables.
#
# Dandiset 001878 is a collection of conversions from three source datasets. It holds one CalMS21
# sequence, the Task 1 test sequence mouse071 (pose, annotations as bouts, and the video). The rest
# of CalMS21 is public on CaltechDATA (record s0vdx-0k302, version 1.0), so the claims about the
# dataset as a whole are `data: elsewhere` and are tested on those files.
#
# When these criteria were written, the author had seen: the dandiset's file list and metadata;
# every object of the CalMS21 NWB file and the values of its data check (14 keypoint series at 30
# Hz, positions within the image, every confidence value NaN, bouts that tile the session with the
# labels investigation, other and mount and no attack, the derived speed and distance series);
# the frame count, rate and size of its video; the list of members of the CaltechDATA zips, and the
# sequence keys of the Task 1 files (70 train and 19 test sequences, mouse071 the first test
[... 326 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_sun_2021.ipynb'))
for i,c in enumerate(nb['cells']):
    print(f'===== CELL {i} [{c[\"cell_type\"]}] =====')
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--'); print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT--'); print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('--ERR--', o['ename'], o['evalue'])
" > $TMPDIR/nb.txt; wc -l $TMPDIR/nb.txt
```

```
1222 /tmp/claude-1001/nb.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt"
}
```

```
1	===== CELL 0 [markdown] =====
2	# Reproducing the CalMS21 dataset paper (Sun et al. 2021) from dandiset 001878
3	
4	**Paper.** Sun JJ, Karigo T, Chakraborty D, Mohanty SP, Wild B, Sun Q, Chen C, Anderson DJ, Perona P,
5	Yue Y, Kennedy A (2021). The Multi-Agent Behavior Dataset: Mouse Dyadic Social Interactions. NeurIPS
6	2021 Datasets and Benchmarks track. [arXiv:2104.02710v4](https://arxiv.org/abs/2104.02710). The target
7	names [doi:10.22002/D1.1991](https://doi.org/10.22002/D1.1991), which is the CaltechDATA record of the
8	dataset (CalMS21); this paper is the one that record and the dataset describe. The full text (arXiv v4,
9	with its appendix and datasheet) was used.
10	
11	**Dandiset.** [DANDI:001878](https://dandiarchive.org/dandiset/001878/draft), version `draft`.
12	The dandiset has no published version, so the draft is the only one there is. It was last modified on
13	2026-06-25T18:32:10Z. To keep a changing draft from passing unnoticed, the helper module checks the
14	blob id of each asset it reads against the one recorded when this notebook was written, and stops if
15	it differs. The dandiset is a collection of conversions from three source datasets; for CalMS21 it
16	holds one sequence, the Task 1 test sequence mouse071 (pose, annotations as bouts, and the video).
17	
18	**Data from elsewhere.** The paper deposited the whole dataset on CaltechDATA (record s0vdx-0k302,
19	version 1.0, the target DOI). The claims about the dataset as a whole (`elsewhere`) are tested on
20	those files, streamed from the record's zips with range requests. The link claim and one pose-error
[... 814 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/nb.txt",
 "offset": 835
}
```

```
835	print(ctab.round(4).to_string(index=False))
836	per_mouse = {name: {"close": np.median(ref_sc[d_cent <= np.quantile(d_cent, 0.1), m].mean(axis=1)) -
837	                    np.median(ref_sc[d_cent > np.quantile(d_cent, 0.1), m].mean(axis=1))}
838	             for m, name in enumerate(calms21.MICE)}
839	print("variant, per mouse, median confidence close minus rest (10%):", {k: round(v["close"], 4) for k, v in per_mouse.items()})
840	print("correlation of confidence with the error flags of pose-errors-close-fast:",
841	      round(stats.pointbiserialr(err, conf)[0], 3))
842	fig, ax = plt.subplots(1, 2, figsize=(9, 3))
843	ax[0].scatter(d_cent[::10], conf[::10], s=2); ax[0].set_xlabel("centroid distance (px)"); ax[0].set_ylabel("mean confidence")
844	ax[1].scatter(v_fast[::10], conf[::10], s=2); ax[1].set_xlabel("faster mouse speed (px/s)")
845	ax[1].set_xlim(0, 1500)
846	print("every 10th frame plotted; frames above 1500 px/s (outside the right axes):", int((v_fast[::10] > 1500).sum()))
847	plt.show()
848	--OUT--
849	mean confidence per frame: median 0.735, range 0.373 to 0.817
850	
851	--OUT--
852	 fraction group  median_in_group  median_elsewhere    diff   ci_lo   ci_hi
853	     0.10 close           0.6491            0.7397 -0.0907 -0.1072 -0.0735
854	     0.10  fast           0.7505            0.7323  0.0182  0.0121  0.0252
[... 369 more lines not kept]
```

**Agent**

Notebook read (22 claims; 16 tested, 6 marked blocked). Now reading the helper module.

**Agent calls Read**

```json
{
 "file_path": "calms21.py"
}
```

```
1	"""Loading CalMS21 (Sun et al. 2021) from dandiset 001878 and from its CaltechDATA deposit.
2	
3	Dandiset 001878 has no published version. The entry reads the draft and pins it by the blob id of
4	each asset it uses: if an asset changes, `asset_url` raises, so that a changed draft cannot pass
5	unnoticed. The draft's modification time when the entry was written is DRAFT_MODIFIED.
6	
7	The dandiset holds one CalMS21 sequence, Task 1 test sequence mouse071, as an NWB file with MARS
8	pose (ndx-pose), the frame annotations as bouts (ndx-ethogram), two per-frame series the converter
9	derived from the pose, and the source video as an external mp4.
10	
11	The paper's full dataset is on CaltechDATA (doi:10.22002/D1.1991, record s0vdx-0k302, version
12	1.0), as zip files of JSON. `caltech_sequences` streams one JSON member of a zip with HTTP range
13	requests and yields its sequences one at a time, without writing anything to disk.
14	
15	Parameters and conventions:
16	- Keypoint order (nose, left ear, right ear, neck, left hip, right hip, tail base), mouse 0 the
17	  resident and mouse 1 the intruder, image size 1024 x 570, 30 Hz, and the Task 1 vocabulary
18	  {attack: 0, investigation: 1, mount: 2, other: 3}: the paper's Appendix C and D.
19	- Array layout of keypoints (frames, mouse, x/y, body part): the paper's Appendix C and the
20	  CaltechDATA readme.
[... 427 more lines not kept]
```

**Agent**

Helper module read. Next: fetch the paper (arXiv 2104.02710v4) and check the DANDI and CaltechDATA archives directly.

**Agent calls Bash**

```bash
cd  mkdir -p paper; curl -sL -o paper/2104.02710v4.pdf https://arxiv.org/pdf/2104.02710v4 && ls -la paper && python3 -c "import fitz" 2>&1; which pdftotext
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/001878/versions/draft/assets/?page_size=100" | python3 -c "import json,sys; [print(a['path'],a['size'],a['blob'],a['modified']) for a in json.load(sys.stdin)['results']]"; curl -s "https://api.dandiarchive.org/api/dandisets/001878/versions/draft/info/" | python3 -c "import json,sys; d=json.load(sys.stdin); print(d['modified'], d['asset_count'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 -c "import pypdf" 2>&1 || pip install -q pypdf 2>&1 | tail -1; python3 -c "
import pypdf
r=pypdf.PdfReader('paper/2104.02710v4.pdf')
open('paper/2104.02710v4.txt','w').write('\n\n=====PAGE=====\n'.join(p.extract_text() for p in r.pages))
print(len(r.pages))
"; wc -c paper/2104.02710v4.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -E "139,1|139112|Table 5|Table 6|Table 7|Table 10|2\.76|independent|close contact|moving very|errors in pose|1024|570|confidence|chance|license|CC-BY|BALB|C57|over 1 million|70 hours|10 hours|282|6 million|gitlab|github" paper/2104.02710v4.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 918,1004p paper/2104.02710v4.txt; echo ----; sed -n 1310,1370p paper/2104.02710v4.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -E "3\.25|1\.47|19\.3|9\.29|4\.74|0\.90|bout duration|shorter|percentage of frames|videos? (are|is) (also )?(released|available)|source video|Figure 4" paper/2104.02710v4.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 290,360p paper/2104.02710v4.txt; echo ----; sed -n 495,520p paper/2104.02710v4.txt; echo -----; sed -n 1490,1515p paper/2104.02710v4.txt; echo ----; sed -n 1655,1700p paper/2104.02710v4.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'EOF' 2>&1 | grep -v Warning
import numpy as np, pandas as pd, itertools, json
from scipy import stats
import importlib.util, sys, types
# stub remfile/h5py if missing
for m in ("remfile","h5py"):
    try: __import__(m)
    except ImportError: sys.modules[m]=types.ModuleType(m)
import calms21 as c
# frame_labels
b=pd.DataFrame({"start_time":[0,1/30*3],"stop_time":[3/30,10/30],"label":["a","b"]})
print(c.frame_labels(b,10))
try: c.frame_labels(pd.DataFrame({"start_time":[0,0.05],"stop_time":[0.1,0.2],"label":["a","b"]}),10)
except ValueError as e: print("overlap raises",e)
# run_lengths
print(c.run_lengths(np.array([1,1,0,1,0,0,1,1,1])))
# sequence_summary
rng=np.random.default_rng(0)
n=5
seq={"keypoints":rng.random((n,2,2,7)).tolist(),"scores":rng.random((n,2,7)).tolist(),"annotations":[0,1,1,3,3],"metadata":{"annotator-id":0,"vocab":{"a":0}}}
txt=json.dumps(seq,indent=2).encode()
s=c.sequence_summary(txt); print("n_frames",s["n_frames"],s["annotations"],s["metadata"])
# streaming parser on synthetic doc
doc=json.dumps({"task1/test/x1":seq,"task1/test/x2":dict(seq,annotations=[0]*5)}).encode()
c._member_bytes=lambda z,m: iter([doc[:100],doc[100:3000],doc[3000:]])
out=list(c.caltech_sequences("z","m"))
print([k for k,_ in out],[c.sequence_summary(t)["annotations"].tolist() for _,t in out])
# nose_to_intruder
kp=np.zeros((1,2,2,7)); kp[0,1,0,:]=np.arange(7)+3; kp[0,1,1,:]=4
print("nose dist",c.nose_to_intruder(kp), "expected 5")
# bootstrap: null data -> CI covers 0
r=np.random.default_rng(1)
v=r.normal(size=6000); g=r.random(6000)<0.1
print(c.block_bootstrap_diff(v,g,300,500,r))
v2=v+g*1.0
print(c.block_bootstrap_diff(v2,g,300,500,r))
# spearman
F1=[0.338,0.195,0.289,0.721,0.034,0.358,0.430]
tr_p=[3.249,1.466,13.988,19.255,0.903,4.744,9.295]; tr_b=[22.333,7.594,137.370,336.091,30.214,24.676,29.5]
te_p=[3.023,1.194,5.451,13.389,0.551,5.980,14.705]; te_b=[21.478,12.667,61.884,284.346,24.895,38.116,29.640]
for x in (tr_p,tr_b,te_p,te_b):
    rho=stats.spearmanr(x,F1)[0]
    ry=stats.rankdata(F1); rx=stats.rankdata(x)
    p=np.mean([stats.spearmanr(rx,pp)[0]>=rho-1e-12 for pp in itertools.permutations(ry)])
    print(round(rho,3),round(p,3))
print("3.25-3.2 <= .05:", 3.25-3.2<=0.05, 4521/139122*100, 4522/139122*100)
EOF
```

```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
cd  ls; which -a python python3; ls ~/.venv* /opt 2>/dev/null | head; pip install -q numpy pandas scipy 2>&1 | tail -2
```

```
10.22002-d1.1991.yaml
bunfig.toml
calms21.py
node_modules
package-lock.json
package.json
paper
pnpm-lock.yaml
reproduce_sun_2021.ipynb
scripts
yarn.lock
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
/opt/hostedtoolcache/Python/3.13.16/x64/python
/usr/bin/python
/bin/python
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt:
actionarchivecache
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 -m venv v && v/bin/pip install -q numpy pandas scipy requests 2>&1 | tail -2; v/bin/python -c "import numpy, scipy, pandas; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'EOF' 2>&1
import numpy as np, pandas as pd, itertools, json, sys, types
from scipy import stats
for m in ("remfile","h5py"):
    sys.modules[m]=types.ModuleType(m)
import calms21 as c
b=pd.DataFrame({"start_time":[0,3/30],"stop_time":[3/30,10/30],"label":["a","b"]})
print(c.frame_labels(b,10))
try: c.frame_labels(pd.DataFrame({"start_time":[0,0.05],"stop_time":[0.1,0.2],"label":["a","b"]}),10)
except ValueError as e: print("overlap raises",e)
print(c.run_lengths(np.array([1,1,0,1,0,0,1,1,1])))
rng=np.random.default_rng(0); n=5
seq={"keypoints":rng.random((n,2,2,7)).tolist(),"scores":rng.random((n,2,7)).tolist(),"annotations":[0,1,1,3,3],"metadata":{"annotator-id":0,"vocab":{"a":0}}}
s=c.sequence_summary(json.dumps(seq,indent=2).encode()); print("n_frames",s["n_frames"],s["annotations"],s["metadata"])
doc=json.dumps({"task1/test/x1":seq,"task1/test/x2":dict(seq,annotations=[0]*5)}).encode()
c._member_bytes=lambda z,m: iter([doc[:100],doc[100:3000],doc[3000:]])
out=list(c.caltech_sequences("z","m"))
print([k for k,_ in out],[c.sequence_summary(t)["annotations"].tolist() for _,t in out])
kp=np.zeros((1,2,2,7)); kp[0,1,0,:]=np.arange(7)+3; kp[0,1,1,:]=4
print("nose dist",c.nose_to_intruder(kp), "expected 5")
r=np.random.default_rng(1)
v=r.normal(size=6000); g=r.random(6000)<0.1
print("null",c.block_bootstrap_diff(v,g,300,500,r))
print("shift 1",c.block_bootstrap_diff(v+g*1.0,g,300,500,r))
F1=[0.338,0.195,0.289,0.721,0.034,0.358,0.430]
xs={"tr_p":[3.249,1.466,13.988,19.255,0.903,4.744,9.295],"tr_b":[22.333,7.594,137.370,336.091,30.214,24.676,29.5],
"te_p":[3.023,1.194,5.451,13.389,0.551,5.980,14.705],"te_b":[21.478,12.667,61.884,284.346,24.895,38.116,29.640]}
for k,x in xs.items():
    rho=stats.spearmanr(x,F1)[0]; ry=stats.rankdata(F1); rx=stats.rankdata(x)
    p=np.mean([stats.spearmanr(rx,pp)[0]>=rho-1e-12 for pp in itertools.permutations(ry)])
    print(k,round(rho,3),round(p,3))
print("3.25-3.2 <= .05:", 3.25-3.2<=0.05, 4521/139122*100, 4522/139122*100)
print("attack 14039/507738", 100*14039/507738)
EOF
```

```
['a' 'a' 'a' 'b' 'b' 'b' 'b' 'b' 'b' 'b']
overlap raises bouts overlap
[2 1 3]
n_frames 5 [0 1 1 3 3] {'annotator-id': 0, 'vocab': {'a': 0}}
['task1/test/x1', 'task1/test/x2'] [[0, 1, 1, 3, 3], [0, 0, 0, 0, 0]]
nose dist [5.] expected 5
null (0.007067132816158278, -0.07287827608877992, 0.1308967974223202)
shift 1 (1.0070671328161582, 0.9242233599367556, 1.1340230925179329)
tr_p 0.786 0.024
tr_b 0.321 0.249
te_p 0.929 0.003
te_b 0.607 0.083
3.25-3.2 <= .05: True 3.24966576098676 3.2503845545636207
attack 14039/507738 2.7650087249723283
```

**Agent**

Helpers pass synthetic tests and the Spearman values reproduce. Last step: checking the archives and code links for the six claims marked blocked.

**Agent calls Bash**

```bash
curl -s -m 30 -o /dev/null -w "%{http_code}\n" https://gitlab.aicrowd.com/aicrowd/research/mab-e/mab-e-baselines; curl -s -m 30 "https://api.github.com/search/repositories?q=mab-e-baselines" | $TMPDIR/v/bin/python -c "import json,sys; d=json.load(sys.stdin); print(d.get('total_count'), [r['full_name'] for r in d.get('items',[])][:10])"; curl -s -m 30 "https://api.github.com/search/repositories?q=calms21" | $TMPDIR/v/bin/python -c "import json,sys; d=json.load(sys.stdin); print(d.get('total_count'), [r['full_name'] for r in d.get('items',[])][:15])"; curl -sL -m 60 "https://data.caltech.edu/records/s0vdx-0k302/files/readme.md?download=1" | head -c 6000
```

Result: the fetched text is not kept.

**Agent**

**A. Outcomes** (22 claims in the claims file: 10 reproduced, 6 partially reproduced, 6 blocked)

| Claim | My outcome | Reason |
|---|---|---|
| format-keypoints | partially_reproduced | Cell 16: 14 correctly named series, pixels, 30 Hz, all coordinates inside 1024 x 570. But all 333,340 confidence values are NaN, and the criterion's partial rule covers exactly that case. |
| resident-is-black | reproduced | Cell 18: with 746 frames ≥60 px apart and the 12 px patch, the resident is darker in 1.000 of frames (median grey 46 vs 251). This holds in every minute and every patch-size variant. |
| task1-vocab | reproduced | Cell 20: codes {attack 0, investigation 1, mount 2, other 3} and annotator "CalMS21 annotator 0". Cell 7: bouts tile 0 to 793.67 s with no gaps, so 0 unlabelled frames, and `frame_labels` raises on overlap. |
| task1-video | reproduced | Cells 9 and 22: 1024 x 570, 30 fps, 23,810 frames decoded, equal to the pose count. Motion energy peaks at lag 0. CaltechDATA also holds 89 Task 1 mp4s (70 + 19). |
| contact-during-social-behaviors | reproduced | Cell 24, nose-to-intruder minus other: investigation −354.6 px (CI −407 to −293), mount −361.0 px (CI −412 to −304). Attack has 0 frames in this session, so it is untested, as the criterion allows. |
| pose-errors-close-fast | partially_reproduced | Cell 26, factor 3 at 10%: errors are higher in close frames (+0.115, CI 0.064 to 0.179) but lower in fast frames (−0.020, CI −0.033 to −0.008). The same pattern holds in every variant. |
| link-mouse071 | reproduced | Cell 28: 23,810 frames in both, max coordinate difference 0 px, frame labels agree on 23,810 of 23,810. The CaltechDATA confidence scores (0.03 to 0.98) are absent from the dandiset. |
| pose-errors-close-fast-confidence | partially_reproduced | Cell 30: median confidence is lower in close frames (−0.091, CI −0.107 to −0.074) but higher in fast frames (+0.018, CI 0.012 to 0.025). The link it depends on is reproduced. |
| table5-task1-counts | reproduced | Cell 32: 507,738 frames / 70 sequences (train) and 262,107 / 19 (test), all exact. |
| table5-task2-counts | partially_reproduced | Cell 34: 19 of 20 counts are exact. Annotator 1 training frames are 139,122 against the paper's 139,112 (Table 5, confirmed in the arXiv v4 text), which is within 10% but the tolerance is 0. |
| table5-task3-counts | reproduced | Cell 36: 28 of 28 counts exact. |
| table6-task1-label-fractions | partially_reproduced | Cell 38, reading (a): attack is 14,039 / 507,738 = 2.76501%, which misses the 0.005 tolerance around 2.76 by 9e-6. The other three are within tolerance and all four are within 10%. Figure 4B's pie shows 2.8%, consistent with 2.765. |
| fig4b-task2-label-fractions | reproduced | Cell 40, reading (a) training split in Task 1 class order: 20 of 20 within 0.05. |
| table7-task3-label-fractions | reproduced | Cell 42, reading (a): all 7 within tolerance (largest gap 0.045, intromission). In v4 these percentages sit in the "% Frames" column of Table 7, the class-weight table. |
| dataset-size | reproduced | Cell 44: 282 unlabelled sequences with 5,952,058 frames. The over-1M-frames, >10 h and >70 h statements all hold under readings (b) and (c), and (c) counts duplicates once: 2.27 M frames, 21.1 h annotated, 76.2 h pose. |
| table10-task3-difficulty | partially_reproduced | Cell 46: the percent-of-frames correlation is significant (train rho 0.786, p 0.024; test 0.929, p 0.003), but mean bout length is positive and not significant (train 0.321, p 0.249; test 0.607, p 0.083). I recomputed these values exactly from the printed features, and the F1 constants match Table 10. |
| table1-architectures | blocked (methods_underspecified) | Model training is needed. The baseline repo (gitlab.aicrowd.com/.../mab-e-baselines) timed out from here too, and GitHub has no repository of that name. Neither the DANDI assets nor the CaltechDATA files hold predictions or weights. |
| table2-task-programming | blocked (methods_underspecified) | Same as table1. The task-programming features are deposited (`taskprog_features` JSONs in the task zips, per the CaltechDATA readme), so only a reimplemented baseline could be tried, not the paper's. The top-entry 0.864 cannot be tested (data_missing). |
| table3-task2-style-transfer | blocked (methods_underspecified) | Model outputs are needed and none are deposited. |
| table4-task3-new-behaviors | blocked (methods_underspecified) | Same. The "far below Tasks 1 and 2" comparison exists only between the paper's own reported numbers. |
| fig7-errors-at-transitions | blocked (data_missing) | Needs the baseline models' per-frame predictions, which are in neither archive. |
| fig11-annotator-similarity | blocked (data_missing) | Needs the top entry's learned annotator matrix. Its code is not linked and the matrix is not deposited. |

No claim states a chance level, so there is nothing to compare there.

**B. Problems**

1. [affects a conclusion] Cell 26, `error_flags`: the pose-error proxy flags body lengths outside the session's IQR bounds. During mount and close investigation, a hunched or occluded posture can produce real outliers, so the "close" excess may partly reflect behaviour and not pose error. Error fractions are 0.105 in mount and 0.045 in investigation, against 0.009 in other. This follows the pre-set criterion, so the outcome stands, but the close half of the partial result is weaker evidence than its confidence interval suggests. The confidence-based claim in cell 30 supports it independently.
2. [does not affect a conclusion] `block_bootstrap_diff` as called in cells 24 and 26 variants: in cell 24 it runs on `nose_d[base]`, a concatenation of non-contiguous frames, so some 300-frame blocks straddle removed stretches. The effect sizes are far from 0.
3. [does not affect a conclusion] Cell 26, `v_fast`: the criterion's order is ambiguous. The code takes the running median per mouse, then the maximum, not the maximum and then the median. The result is unlikely to change, since the fast effect is negative at every threshold.
4. [does not affect a conclusion] Cell 9, patch loop: with `half=3` and `STEP=2`, `h=1` gives a 2 x 2 downsampled patch, which is 4 full-resolution pixels, but it is labelled "6 px". The slices `yi-h:yi+h` are also off-centre by half a pixel. The main 12 px patch is correct.
5. [does not affect a conclusion] Cell 40: annotator 1 attack in reading (a) prints as 3.25. It is 4521/139122 = 3.2497%, 0.0497 from 3.2, so the 20/20 result depends on a single frame. The printout rounds to 2 decimals and hides this.
6. [does not affect a conclusion] Cell 20: the annotator check is a string test, `endswith(" 0")`, on free text. It is adequate here.
7. [does not affect a conclusion] Dandiset metadata, cells 5 and 8:
   - licence CC-BY-4.0, while the paper's datasheet says CC-BY-NC-SA (CaltechDATA also says CC-BY-4.0);
   - subject strain is C57BL/6 only, with the BALB/c intruder absent, sex U and age `P0D/`;
   - ethogram definitions are empty;
   - `centroid_speed` is the speed of the pair's midpoint, not of either animal;
   - confidence values are not carried over.
8. [does not affect a conclusion] Cell 13 (dataset finding, checked against the CaltechDATA readme): the readme says train and test are "split by animal identity". Yet four Task 2 recordings cross the train/test split between annotators 3 and 4, and mouse071 (Task 1 test) is also Task 3 groom training data. This matters for the blocked model claims, not the tested ones.
9. [does not affect a conclusion] task1-video, paper consistency: Section 3.1 says the Task 1 videos are released, but the datasheet (Appendix B) says the dataset "does not include the original raw videos". The dandiset mp4 (184 MB) is a re-encode of CaltechDATA's (964 MB).

Helper checks on synthetic inputs all passed:
- `frame_labels`: [start, stop) labelling, and it raises on overlap.
- `run_lengths` returns the correct lengths.
- `sequence_summary`: its "]]" frame count is right on indented JSON.
- `caltech_sequences` splits keys correctly across chunk boundaries.
- `nose_to_intruder` returns the expected distance.
- `block_bootstrap_diff` covers 0 under the null and recovers a shift of 1.

**C. What I could not check**

- The source of the 10-frame Task 2 gap (139,122 vs 139,112). A per-sequence frame table for annotator 1's training set would show whether one sequence accounts for it, which would point to a typo in the paper or a different deposit.
- Whether flagged "pose errors" are real tracking errors or real postures. A handful of video frames with keypoints overlaid, taken from flagged close frames, would settle problem 1.
- The unlabelled frame counts (`]]` in `scores`) were not cross-checked against `keypoints` length. The labelled sets validate the method, but printing keypoints-length totals for the unlabelled parts would confirm it.
- The exact label counts behind cells 38, 40 and 42. Raw integer counts per class, not only rounded percentages, would make the boundary cases (table6 attack, fig4b annotator 1 attack) auditable.
- The notebook's figures, which I did not view. All decisions above rest on printed numbers.
- I re-ran no data loading, as instructed. The dandiset asset list, blob ids and draft modification time match the notebook (6 assets, modified 2026-06-25T18:32:10Z). The paper text I used is saved at `paper/2104.02710v4.txt`.

## End of run

19 turns, 4 minutes, result: success.
