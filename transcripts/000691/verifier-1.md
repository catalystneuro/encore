# 000691 · verifier-1 · run 39529389902

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper; ls docs 2>/dev/null
```

```
Exit code 2
total 3144
drwxr-xr-x 6 runner runner     4096 Oct 21 02:53 .
drwxr-xr-x 7 runner runner     4096 Oct 21 02:53 ..
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 21 01:46 .bash_profile
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 21 01:46 .bashrc
drwxr-xr-x 5 runner runner     4096 Oct 21 02:53 .claude
-rw-r--r-- 1 runner runner        0 Oct 21 02:52 .env
-rw-r--r-- 1 runner runner        0 Oct 21 02:52 .env.development
-rw-r--r-- 1 runner runner        0 Oct 21 02:52 .env.development.local
-rw-r--r-- 1 runner runner        0 Oct 21 02:52 .env.local
-rw-r--r-- 1 runner runner        0 Oct 21 02:52 .env.production
-rw-r--r-- 1 runner runner        0 Oct 21 02:52 .env.production.local
-rw-r--r-- 1 runner runner        0 Oct 21 02:52 .env.test
-rw-r--r-- 1 runner runner        0 Oct 21 02:52 .env.test.local
drwx------ 2 runner runner       40 Oct 21 02:53 .git
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 21 01:46 .gitconfig
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 21 01:46 .github
-rw-r--r-- 1 runner runner        0 Oct 21 02:52 .gitmodules
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 21 01:46 .idea
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat 10.1038-s41592-023-01806-1.yaml
```

```
<persisted-output>
Output too large (37.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/a7b413dc-7fa5-43b5-baed-168072785168/tool-results/bxn2nzw4x.txt

Preview (first 2KB):
# Claims for Scherrer, Lynch, Zhang & Fee (2023) on dandiset 000691.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20,
# protocol as stated in docs/protocol.md (version pilot-10).
#
# Text read: the version of record (Nature Methods 20, 546-549), from a PDF supplied by a person,
# as extracted text in paper/10.1038-s41592-023-01806-1.txt. It holds the main text, the figure
# legends, the Methods, the Extended Data legends (Extended Data Figs. 1 to 10) and the reporting
# summary. The supplementary information is two videos (Supplementary Videos 1 and 2), which no
# result rests on. The PDF was not opened; the numbers needed were in the text. In the extracted
# text, the sentence on the Featherscope's resolution (page 547) is split by figure labels, its
# second half placed before its first; the quote of fig1e-featherscope-psf is that second half, and
# its first half reads "The Featherscope has a resolution of approximately 4 μm at the".
#
# Rewritten 2026-10-20 from the full text. The earlier file was written from the abstract and the
# public figure legends, and its criteria were written after its author had seen the data check
# and a prototype decoder. This file is written from the paper and its code alone, by a reader
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/a7b413dc-7fa5-43b5-baed-168072785168/tool-results/bxn2nzw4x.txt"
}
```

```
1	# Claims for Scherrer, Lynch, Zhang & Fee (2023) on dandiset 000691.
2	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-20,
3	# protocol as stated in docs/protocol.md (version pilot-10).
4	#
5	# Text read: the version of record (Nature Methods 20, 546-549), from a PDF supplied by a person,
6	# as extracted text in paper/10.1038-s41592-023-01806-1.txt. It holds the main text, the figure
7	# legends, the Methods, the Extended Data legends (Extended Data Figs. 1 to 10) and the reporting
8	# summary. The supplementary information is two videos (Supplementary Videos 1 and 2), which no
9	# result rests on. The PDF was not opened; the numbers needed were in the text. In the extracted
10	# text, the sentence on the Featherscope's resolution (page 547) is split by figure labels, its
11	# second half placed before its first; the quote of fig1e-featherscope-psf is that second half, and
12	# its first half reads "The Featherscope has a resolution of approximately 4 μm at the".
13	#
14	# Rewritten 2026-10-20 from the full text. The earlier file was written from the abstract and the
15	# public figure legends, and its criteria were written after its author had seen the data check
16	# and a prototype decoder. This file is written from the paper and its code alone, by a reader
17	# who has not seen the dandiset's data. What changed, and why:
18	# - ed9c-local-decoding-map: the null is now the paper's (Methods, Data analysis, paragraph 5),
19	#   a thousand decoders trained on shuffled data from 32 randomly chosen footprints, where each
20	#   footprint's trace is circularly shifted by its own random offset. The earlier null shifted the
[... 551 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
import json
for f in ['reproduce_scherrer_2023.ipynb','decoding_octant.ipynb','decoding_quadrant_direction.ipynb','motion_scherrer_2023.ipynb']:
    nb=json.load(open(f))
    print(f, len(nb['cells']), nb.get('metadata',{}).keys())
EOF
```

```
reproduce_scherrer_2023.ipynb 41 dict_keys(['kernelspec', 'language_info'])
decoding_octant.ipynb 11 dict_keys(['kernelspec', 'language_info'])
decoding_quadrant_direction.ipynb 14 dict_keys(['kernelspec', 'language_info'])
motion_scherrer_2023.ipynb 9 dict_keys(['kernelspec', 'language_info'])
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/dump.py <<'EOF'
import json,sys
nb=json.load(open(sys.argv[1]))
for i,c in enumerate(nb['cells']):
    print(f"\n######## CELL {i} [{c['cell_type']}]")
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: t=''.join(o['text'])
        elif 'data' in o:
            d=o['data']; t=''.join(d.get('text/plain','')) + (' [IMAGE]' if 'image/png' in d else '')
        elif o.get('output_type')=='error': t='ERROR '+o['ename']+': '+o['evalue']
        else: t=str(o)[:200]
        if len(t)>6000: t=t[:6000]+'\n...[TRUNC]'
        print('--> OUT:', t)
EOF
python3 $TMPDIR/dump.py reproduce_scherrer_2023.ipynb > $TMPDIR/main.txt; wc -c $TMPDIR/main.txt
```

```
82785 /tmp/claude-1001/main.txt
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt"
}
```

```
1	
2	######## CELL 0 [markdown]
3	# Reproducing Scherrer, Lynch et al. (2023) from dandiset 000691
4	
5	Paper. Scherrer JR, Lynch GF, Zhang JJ, Fee MS (2023). An optical design enabling lightweight
6	and large field-of-view head-mounted microscopes. *Nature Methods* 20, 546-549.
7	[doi:10.1038/s41592-023-01806-1](https://doi.org/10.1038/s41592-023-01806-1).
8	
9	Claims. The claims file `claims/000691/10.1038-s41592-023-01806-1.yaml` was written on
10	2026-10-20 from the full text of the version of record (main text, figure legends, Methods,
11	Extended Data legends and reporting summary) and the paper's code, GitHub
12	`FeeLab/Feescope-Paper-Code` at commit d596646, by a reader who did not see the data, and checked
13	by a second reader. It decides what is tested and how. This is the second attempt on the dandiset
14	(`000691-scherrer-2023-02`); the first (`-01`) worked from claims written from the abstract and
15	the public legends, and is deprecated.
16	
17	Dandiset. [DANDI:000691](https://dandiarchive.org/dandiset/000691/0.260827.1358), version
18	0.260827.1358. Why this version: the paper cites no DANDI version (its data statement points to an
19	Academic Torrents deposit), and 0.260827.1358 is the only published version, the one the first
20	attempt used. The draft was last modified when that version was published and holds the same two
[... 733 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/main.txt",
 "offset": 754
}
```

```
754	    table = pd.DataFrame({"n": by.size(), "median_major": by.fwhm_major.median(), "median_minor": by.fwhm_minor.median(),
755	                          "mean_major": by.fwhm_major.mean(), "mean_minor": by.fwhm_minor.mean()}).round(3)
756	    centre_g, edge_g = s["groups"][0], s["groups"][-1]
757	    rows = []
758	    for label, col in [("(a) median major", "median_major"), ("(b) median minor", "median_minor"),
759	                       ("(c) mean major", "mean_major"), ("(d) mean minor", "mean_minor")]:
760	        cv, ev = table.loc[centre_g, col], table.loc[edge_g, col]
761	        rows.append({"reading": label, "centre_um": cv, "edge_um": ev,
762	                     "centre_within": abs(cv - s["expect"][0]) <= 0.1 * s["expect"][0],
763	                     "edge_within": abs(ev - s["expect"][1]) <= 0.1 * s["expect"][1]})
764	    return table, pd.DataFrame(rows)
765	
766	psf = {}
767	for name in psf_setups:
768	    t0 = time.time()
769	    psf[name] = psf_fits(name)
770	    fits = psf[name]
771	    table, read = readings(fits, name)
772	    print(f"\n{name}: {len(fits)} fits in {time.time() - t0:.0f} s; stopped by the evaluation limit: {(fits.status == 0).sum()}; "
773	          f"FWHM major {fits.fwhm_major.min():.2f} to {fits.fwhm_major.max():.2f} um, minor {fits.fwhm_minor.min():.2f} to {fits.fwhm_minor.max():.2f} um")
[... 488 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/dump.py decoding_quadrant_direction.ipynb
```

```
######## CELL 0 [markdown]
# Scherrer, Lynch et al. (2023), dandiset 000691: decoding quadrant and direction

Paper. Scherrer JR, Lynch GF, Zhang JJ, Fee MS (2023). An optical design enabling lightweight
and large field-of-view head-mounted microscopes. *Nature Methods* 20, 546-549.
[doi:10.1038/s41592-023-01806-1](https://doi.org/10.1038/s41592-023-01806-1).

Claims. `claims/000691/10.1038-s41592-023-01806-1.yaml`, written from the full text of the
version of record and the paper's code (GitHub `FeeLab/Feescope-Paper-Code`, commit d596646). It
decides what is tested and how.

Dandiset. [DANDI:000691](https://dandiarchive.org/dandiset/000691/0.260827.1358), version
0.260827.1358, the only published version (the paper cites none); see the main notebook,
`reproduce_scherrer_2023.ipynb`, for the reasons and the full data check. This notebook holds the
quadrant and direction decoding claims, apart to keep each notebook within the time limit.

Footprints. The claims use the 2,382 curated footprints, with all 2,948 as a named variant.
The dandiset does not mark the curated set, so all 2,948 are used.

| Claim | Data | Status |
[... 236 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 $TMPDIR/dump.py decoding_octant.ipynb; python3 $TMPDIR/dump.py motion_scherrer_2023.ipynb
```

```
######## CELL 0 [markdown]
# Scherrer, Lynch et al. (2023), dandiset 000691: decoding octant

Paper. Scherrer JR, Lynch GF, Zhang JJ, Fee MS (2023). An optical design enabling lightweight
and large field-of-view head-mounted microscopes. *Nature Methods* 20, 546-549.
[doi:10.1038/s41592-023-01806-1](https://doi.org/10.1038/s41592-023-01806-1).

Claims. `claims/000691/10.1038-s41592-023-01806-1.yaml`, written from the full text of the
version of record and the paper's code (GitHub `FeeLab/Feescope-Paper-Code`, commit d596646). It
decides what is tested and how.

Dandiset. [DANDI:000691](https://dandiarchive.org/dandiset/000691/0.260827.1358), version
0.260827.1358, the only published version (the paper cites none); see the main notebook,
`reproduce_scherrer_2023.ipynb`, for the reasons and the full data check. This notebook holds the
octant decoding claims, apart to keep each notebook within the time limit.

Footprints. The claims use the 2,382 curated footprints, with all 2,948 as a named variant.
The dandiset does not mark the curated set, so all 2,948 are used.

| Claim | Data | Status |
[... 372 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 1,400p kiloscope.py
```

```
"""Loading and measures for the freely moving mouse session of dandiset 000691.

Scherrer, Lynch, Zhang & Fee (2023), Nature Methods, doi:10.1038/s41592-023-01806-1.

The dandiset holds one NWB file: the raw video of the large-FOV microscope (the Kiloscope), the
traces, masks and centroids of 2948 EXTRACT footprints, and the timestamps of a behaviour video
whose AVI is a second asset. Both are streamed from the archive at the pinned version: small
datasets through h5py and remfile, the AVI (105 MB), the masks (9 MB compressed) and the movie
(15 GB) by HTTP range requests into memory, whose chunks are decompressed here. Nothing is written
to disk.

Where the parameters come from. The claims file (claims/000691/10.1038-s41592-023-01806-1.yaml)
fixes the method; it cites the Methods of the paper and its code, GitHub
FeeLab/Feescope-Paper-Code at commit d596646b16a505907203828d8026feb7736ca69c (`CODE_COMMIT`).
Each constant below names its source. A detail that neither fixes and that cannot change a
result is marked "standard choice".

- Tracking (claims file, common method; f3+sf8/mouse_position_tracking.m): the video is read from
  64 s at the AVI's nominal 30 frames/s (frame 1920); each frame is rotated by 86.79 degrees
  (bilinear, MATLAB's imrotate with a loose bounding box) and cropped to rows 229 to 560 and
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 400,1000p kiloscope.py
```

```
direction = np.where(movmean(step) > 0, 1, -1)
    return {"sel": sel, "t": t_img[sel], "x": x, "y": y, "quadrant": quadrant, "octant": octant,
            "s": s, "sunwrap": sunwrap, "perimeter": perimeter, "speed": speed,
            "direction": direction, "running": speed > np.median(speed)}


def load_behaviour(urls: dict[str, str], S: dict, keep_frames=()) -> tuple[dict, dict]:
    """Track the mouse in the session's behaviour video and derive the labels: (track, behaviour)."""
    video_url = next(u for p, u in urls.items() if p.endswith(".avi"))
    track = track_mouse(video_url, keep_frames=keep_frames)
    return track, behaviour(S["t_img"], S["t_video"], track)


def quad_dir_labels(b: dict) -> np.ndarray:
    """Quadrant and direction as eight classes, 0-based: 2 * quadrant + (direction > 0)."""
    return 2 * b["quadrant"] + (b["direction"] > 0)


# --- decoders ----------------------------------------------------------------------------------

[... 432 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000691/versions/0.260827.1358/assets/?page_size=100" | python3 -m json.tool | head -50; curl -s "https://api.dandiarchive.org/api/dandisets/000691/versions/0.260827.1358/" > v.json; python3 -c "
import json;d=json.load(open('v.json'));print(d.get('description'));print(json.dumps(d.get('assetsSummary'),indent=0)[:1500]);print([r.get('url') for r in d.get('relatedResource',[])])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000691/versions/0.260827.1358/assets/a59d3244-f125-4691-af89-8068280a13c3/" | python3 -c "
import json,sys;d=json.load(sys.stdin)
for k in ['wasGeneratedBy','measurementTechnique','variableMeasured','description','wasAttributedTo','approach']: print(k, json.dumps(d.get(k),indent=0)[:1500])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  grep -n -i -E "normcorre|motion|0\.13 pix|raw|registration|Extended Data Fig. 7|shuffl|chance" paper/*.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 395,435p paper/*.txt; sed -n 760,790p paper/*.txt; sed -n 995,1000p paper/*.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  timeout 600 python3 - <<'EOF'
import numpy as np, kiloscope as ks
rng=np.random.default_rng(0)
# shuffle_columns: each column circularly shifted, labels untouched
X=np.tile(np.arange(10.)[:,None],(1,3))
Y=ks.shuffle_columns(np.asfortranarray(X),rng); print(Y.T)
# split
lab=np.arange(100); Xtr,ytr,Xte,yte=ks._split(lab[:,None],lab,0); print(len(ytr),ytr[-1],yte[0],yte[-1])
# confusion: rows predicted, cols actual
h,p=ks.confusion(np.array([0,0,1,1]),np.array([0,1,1,1]),2); print(h)
# decoding on separable synthetic
n=4000; lab=rng.integers(0,4,n); X=np.eye(4)[lab]+0.3*rng.standard_normal((n,4))
d=ks.decoding_matrix(X,lab,4,1e-4,3,rng); print('sep exact',d['median'])
X2=np.hstack([X,rng.standard_normal((n,200))]); d=ks.decoding_matrix(X2,lab,4,1e-6,3,rng); print('sep sgd',d['median'])
d=ks.decoding_matrix(rng.standard_normal((n,200)),lab,4,1e-6,3,rng); print('noise sgd',d['median'])
# nmf_groups
H=np.array([[5,1,0.1],[1,2,0.2]]); print(ks.nmf_groups(H))
# behaviour labels on a synthetic loop
xmin,xmax,ymin,ymax=ks.RECT
t=np.linspace(0,100,3000); pts=[]
per=2*((xmax-xmin)+(ymax-ymin)); 
def xy(u):
    u=u%per; L1=ymax-ymin; L2=xmax-xmin
    if u<L1: return xmin, ymax-u
    u-=L1
    if u<L2: return xmin+u, ymin
    u-=L2
    if u<L1: return xmax, ymin+u
    u-=L1; return xmax-u, ymax
xy_=np.array([xy(u) for u in np.linspace(0,3*per,3000)])
tr={"x":xy_[:,0],"y":xy_[:,1]}
B=ks.behaviour(t,t,tr)
print('quadrants',np.bincount(B['quadrant']),'octants',np.bincount(B['octant']),'dir',np.unique(B['direction'],return_counts=True), 'span m',B['sunwrap'][-1]-B['sunwrap'][0], 'expected', 3*per*ks.M_PER_PIXEL)
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
ls /usr/bin/python3* /opt 2>/dev/null; which -a python python3 pip uv conda 2>/dev/null; ls ~/.local/bin 2>/dev/null | head
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config

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
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -m venv $TMPDIR/venv && $TMPDIR/venv/bin/pip install -q numpy scipy scikit-learn joblib h5py pypng remfile requests dandi 2>&1 | tail -3
```

```
[notice] A new release of pip is available: 26.2.1 -> 26.2.2
[notice] To update, run: /tmp/claude-1001/venv/bin/python3 -m pip install --upgrade pip
```

**Agent calls Bash**

```bash
cd  timeout 900 $TMPDIR/venv/bin/python3 - <<'EOF'
import numpy as np, kiloscope as ks
rng=np.random.default_rng(0)
X=np.tile(np.arange(10.)[:,None],(1,3))
Y=ks.shuffle_columns(np.asfortranarray(X),rng); print(Y.T)
lab=np.arange(100); Xtr,ytr,Xte,yte=ks._split(lab[:,None],lab,0); print(len(ytr),ytr[-1],yte[0],yte[-1])
h,p=ks.confusion(np.array([0,0,1,1]),np.array([0,1,1,1]),2); print(h)
n=4000; lab=rng.integers(0,4,n); X=np.eye(4)[lab]+0.3*rng.standard_normal((n,4))
d=ks.decoding_matrix(X,lab,4,1e-4,3,rng); print('sep exact',d['median'])
X2=np.hstack([X,rng.standard_normal((n,200))]); d=ks.decoding_matrix(X2,lab,4,1e-6,3,rng); print('sep sgd',d['median'])
d=ks.decoding_matrix(rng.standard_normal((n,200)),lab,4,1e-6,3,rng); print('noise sgd',d['median'], d['diag'])
H=np.array([[5,1,0.1],[1,2,0.2]]); print(ks.nmf_groups(H))
xmin,xmax,ymin,ymax=ks.RECT
per=2*((xmax-xmin)+(ymax-ymin))
def xy(u):
    u=u%per; L1=ymax-ymin; L2=xmax-xmin
    if u<L1: return xmin, ymax-u
    u-=L1
    if u<L2: return xmin+u, ymin
    u-=L2
    if u<L1: return xmax, ymin+u
    u-=L1; return xmax-u, ymax
t=np.linspace(0,100,3000)
xy_=np.array([xy(u) for u in np.linspace(0,3*per,3000)])
B=ks.behaviour(t,t,{"x":xy_[:,0],"y":xy_[:,1]})
print('quadrants',np.bincount(B['quadrant']),'octants',np.bincount(B['octant']),'dir',np.unique(B['direction'],return_counts=True), 'span m',B['sunwrap'][-1]-B['sunwrap'][0], 'expected', 3*per*ks.M_PER_PIXEL)
Bc=ks.behaviour(t,t,{"x":xy_[:,0],"y":xy_[:,1]},unwrap="code"); print('code unwrap span',Bc['sunwrap'][-1]-Bc['sunwrap'][0])
# octant order along the loop
print('octant seq', [int(o) for o in B['octant'][np.r_[0:3000:60]]][:20])
EOF
```

```
[[1. 2. 3. 4. 5. 6. 7. 8. 9. 0.]
 [3. 4. 5. 6. 7. 8. 9. 0. 1. 2.]
 [4. 5. 6. 7. 8. 9. 0. 1. 2. 3.]]
49 48 50 98
[[1.         0.33333333]
 [0.         0.66666667]]
sep exact 0.9792210614861665
sep sgd 0.9262391113336168
noise sgd 0.2566291270969433 [0.27230391 0.27364827 0.2210642  0.24095435]
[0 1 0]
quadrants [842 657 843 656] octants [421 421 329 328 421 422 328 328] dir (array([1]), array([2998])) span m 4.411400949741868 expected 4.414344827586207
code unwrap span 4.3587696393203395
octant seq [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 0, 0, 1]
```

**Agent**

**A. Outcomes** (23 claims in the claims file)

| Claim | Outcome | Reason |
|---|---|---|
| abstract-thousands-of-neurons | reproduced | Main nb cell 19: 2948 EXTRACT footprints, all in one movie on shared timestamps. The mouse tracked over 47.7 loops of the maze; `cellfind_min_snr` = 2. |
| ed6a-curated-footprints | blocked (metadata_insufficient) | The only PlaneSegmentation columns are `image_mask` and `ROICentroids` (cell 3), so nothing marks the curated footprints. The claim's criterion says it then cannot be tested. |
| ed6bcd-other-mice | blocked (data_missing) | The DANDI API lists 2 assets and 1 subject (I checked this myself). |
| ed5-songbirds | blocked (data_missing) | No bird data in the archive. |
| birds-singing-rate | blocked (data_missing) | No bird data in the archive. |
| fig2d-lman-sparse-bursting | blocked (methods_underspecified; the data are also missing) | The claims file gives methods_underspecified. The notebook's table says only "data missing". |
| abstract-kiloscope-fov | reproduced | Cell 23: 808×608 px gives 4.80×3.61 mm at 5.94 µm/px and 4.32×3.25 mm at 5.35 µm/px. Both sides are within tolerance under both pixel sizes. |
| abstract-weights | blocked (data_missing) | No dataset could hold the hardware weights. |
| fig1e-featherscope-psf | reproduced | Cell 26, reading (a): 3.919 µm at the centre and 6.433 µm at the edge; reading (c): 3.887 and 6.884 µm. Both readings are inside 4±0.4 and 7±0.7, and they are stable under the Jacobian variant (cell 27). |
| fig1f-kiloscope-psf | partially_reproduced | No reading meets the criterion with either optimizer. Under (a) the edge is 5.441 µm (within tolerance) but the centre is 4.422 µm, 0.022 µm above the bound. With Jacobian scaling the centre is 3.578 µm, 0.022 µm below the other bound. The claims file has no partial rule; I call it partial because the centre is about 4 µm and the edge about 5 µm, rising with radius. |
| ed1cf-field-curvature | blocked (methods_underspecified) | As the criterion says. Best-focus slice against radius is shown in cell 30. |
| ed1-ed4-resolution | blocked (data_missing) | No USAF target images, in the dandiset or in the repository listing (cell 21). |
| ed2b-featherscope-flat-illumination | reproduced | Cell 32: corrected vs total-vignetting profile 0.511 vs 0.193 at 0.5 mm and 0.628 vs 0.257 at 0.45 mm. The corrected profile falls less from the centre at both radii. Robust to moving the centre (cell 33). |
| ed2c-kiloscope-flat-illumination | reproduced | 0.557 vs 0.180 at 1.8 mm and 0.420 vs 0.148 at 2.0 mm; the comparison holds for all 6 centres tried. |
| ed7-motion-small | not_reproduced (tentative) | Motion nb cell 6: RMS 0.037, 0.038 and 0.026 px under readings (a), (b) and (c), all far below 0.13±0.013. This rests on the deposited movie being raw, which nothing checks (problem 1); if it is motion-corrected, the right outcome is blocked (metadata_insufficient). |
| fig2-quadrant-direction-decoding | reproduced (null n1 only) | Quadrant nb cells 6–7: median accuracy 0.437 ≥ 0.375 (reading a; reading b fails, min 0.239). Null (n1): max 0.227 over 1000 shuffles, so p = 0. Null (n2), which the criterion also requires, was not run; its one sample (0.136) and the margin make a disagreement very unlikely. |
| fig2k-decoder-size | blocked (other: not run, compute) | Cell 10 only times the fits (4.2 h on 4 cores). The data are present, so this is not a data block. |
| fig2l-local-decoding-map | blocked (other: not run, compute) | Cell 12 only counts the map points used (5411/5905) and times the fits (about 4 h on 4 cores). |
| ed8-coactive-distributed | blocked (methods_underspecified) | Cell 36: all four quarters are covered in 8 of 8 events under reading (a) but 7 of 8 under reading (b) (component 1 at 1000 s has 0 footprints in the lower left). The criterion says that when the readings disagree the outcome is methods_underspecified. |
| ed9b-octant-decoding | reproduced (null n1 only) | Octant nb cell 6: 0.326 > 1/8, above the n1 null maximum of 0.229, p = 0. As for fig2, n2 was not run; its one sample is 0.110. |
| ed9c-local-decoding-map | blocked (other: not run, compute) | Cell 9 times it only (10–11 h on 4 cores). |
| ed10-localized-activity | blocked (methods_underspecified) | As the criterion says. Maps, entropies and peaks are shown in cell 39. |

**B. Problems**

1. **[affects a conclusion]** motion nb, cell 6 / `normcorre_rigid`: nothing checks that the deposited movie is raw, and the API metadata do not say. The paper says shifts were corrected with NoRMCorre before EXTRACT. Several outputs fit an already-registered movie:
   - the largest shift in 36,596 frames of a freely moving mouse is 0.16 px;
   - the per-window RMS is flat at 0.03–0.05 px (cell 7);
   - block 0 contains values of exactly 0 (cell 3).
   
   The ed7 outcome depends on this. Also, the registration is a Python re-implementation built from NoRMCorre defaults "as recalled here", not NoRMCorre itself.
2. **[affects a conclusion]** quadrant nb cell 8 and octant nb cell 7: the n2 null (1000 decoders of 200 fits each) was not run, though both criteria require it. The n1 comparison also sets a 200-fit averaged real matrix against single-fit null matrices: the n1 null median is 0.074, below chance, while the averaged null sample is 0.136. So n1 overstates the separation, though not enough to matter here.
3. **[affects a conclusion]** fig2k, fig2l, ed9c were not attempted. The estimated costs are 4–11 h on 4 cores, so this is a compute choice, not a data block. A reduced run was possible within limits, e.g. fig2k reading (b) with fewer fits, or fig2l with one fit per null decoder.
4. **[affects a conclusion]** `fit_bead` / cell 27: the main PSF fits often stop short of the least-squares minimum. The Jacobian variant finds a lower cost for 49 of 118 Kiloscope beads and 68 of 155 Featherscope beads. For fig1f the centre value swings from 4.42 to 3.58 µm depending on the optimizer. One edge bead is fitted at 27.77 µm, which inflates reading (c) at the edge (7.373 µm). No result is reported using the lower-cost fit for each bead.
5. **[affects a conclusion]** cells 36–37 (ed8):
   - The quarters split at the midlines of the footprints' extent leave 85 of 2948 footprints in the lower left, so the test turns on one sparse corner.
   - Under reading (b), the code's event times land where temporal weights are only 0.04–0.13 of their maxima for four components. Those times are not events of this NMF run.
6. **[does not affect a conclusion]** All decoding claims and ed8 use all 2948 footprints, not the curated 2382. The claims file names this as a variant, so it is allowed, but it is not the paper's set.
7. **[does not affect a conclusion]** `behaviour`: position is unwrapped by the loop length rather than with the code's MATLAB unwrap. About 0.6–0.9% of labels differ (cell 9). My synthetic loop test confirmed the quadrant, octant and unwrap logic.
8. **[does not affect a conclusion]** Cell 12: quadrant decoding peaks with labels shifted +2 s (0.519, against 0.495 at 0 s), so there may be a small clock offset. Any such offset would only make the decoders look worse.
9. **[does not affect a conclusion]** abstract-kiloscope-fov: both pixel sizes come from the authors' code, not the data. With 5.94 µm/px the test reduces to 808 px × a constant that yields exactly 4.80 mm, so it is close to circular.
10. **[does not affect a conclusion]** The Kiloscope bead stack's image order (file number) is not confirmed: only 72% of beads have their brightest slice within 5 slices of the listed one (cell 25). The Featherscope order is confirmed (155 of 155).
11. **[does not affect a conclusion]** The fig2d status in the notebook table ("data missing") differs from the claims file's methods_underspecified.
12. **[does not affect a conclusion]** Main nb cells 28 and 34 still hold the author's "Result" verdicts, although conclusion cells were meant to be removed.

Helper functions I tested on synthetic inputs all behaved as documented: `shuffle_columns`, `_split` (49/49 with a 1-frame buffer for n = 100), `confusion` (normalized by actual class), `decoding_matrix` (0.98 on separable data, about chance 0.26 on noise with 4 classes), `nmf_groups`, and `behaviour`.

**C. What I could not check, and the output that would have let me**

- **Whether the movie is raw:** for example, per-frame counts of zero-valued pixels at the frame edges, any NWB attributes or comments on the series, or the shifts estimated on the movie after a known synthetic jitter is added.
- **The n2 null distributions** for fig2 and ed9b (even 100 decoders), and the distribution of single-fit median accuracies for the real decoder, to put the n1 comparison on equal terms.
- **Any output at all for fig2k, fig2l and ed9c.**
- **PSF readings using, for each bead, the lower-cost of the two fits**, plus the Kiloscope readings with the 27.77 µm outlier listed.
- **Which images `sf3/*/analysis.m` actually loads for ed2b/ed2c**: the lines of the script that name the files. The notebook hard-codes one file per folder without showing that the script uses those files.
- **For ed8:** the active-footprint counts per quarter with the quarters split at the image midlines rather than the footprints' extent.

## End of run

20 turns, 4 minutes, result: success.
