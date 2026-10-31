# 000631 · verifier-1 · run 41168019845

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cd  ls -la; ls paper docs 2>/dev/null; wc -c *
```

```
Exit code 1
total 2752
drwxr-xr-x 6 runner runner     4096 Oct 31 04:29 .
drwxr-xr-x 7 runner runner     4096 Oct 31 04:29 ..
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 31 04:17 .bash_profile
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 31 04:17 .bashrc
drwxr-xr-x 5 runner runner     4096 Oct 31 04:29 .claude
-rw-r--r-- 1 runner runner        0 Oct 31 04:29 .env
-rw-r--r-- 1 runner runner        0 Oct 31 04:29 .env.development
-rw-r--r-- 1 runner runner        0 Oct 31 04:29 .env.development.local
-rw-r--r-- 1 runner runner        0 Oct 31 04:29 .env.local
-rw-r--r-- 1 runner runner        0 Oct 31 04:29 .env.production
-rw-r--r-- 1 runner runner        0 Oct 31 04:29 .env.production.local
-rw-r--r-- 1 runner runner        0 Oct 31 04:29 .env.test
-rw-r--r-- 1 runner runner        0 Oct 31 04:29 .env.test.local
drwx------ 2 runner runner     4096 Oct 31 04:29 .git
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 31 04:17 .gitconfig
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 31 04:17 .github
-rw-r--r-- 1 runner runner        0 Oct 31 04:29 .gitmodules
crw-rw-rw- 1 nobody nogroup    1, 3 Oct 31 04:17 .idea
[... 36 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "10.3390-ijms241310921.yaml"
}
```

```
1	# Claims for Kim, Semenov, Kiester, Keppler, Ibey, Bixler, Colunga Biancatelli & Pakhomov (2023),
2	# "Control of the Electroporation Efficiency of Nanosecond Pulses by Swinging the Electric Field
3	# Vector Direction", Int J Mol Sci 24, 10921, on dandiset 000631.
4	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-23,
5	# protocol pilot-10 as stated in docs/protocol.md.
6	#
7	# Text read: the version of record as served by Europe PMC (PMC10341945), full text with
8	# Introduction, Results, Discussion, Materials and Methods and figure legends. The paper has no
9	# supplement (PMC lists none). No PDF was supplied, so values shown only in figures could not be
10	# read: the curves of Figure 2 and the bar heights and printed p-values of Figure 3. The paper
11	# links no code; its Data Availability Statement says the data are available on request. No code
12	# was read. Methods 4.4 and 4.5 say the staining, analysis and strobe protocols are those of its
13	# reference 17 (Kim et al. 2023, Bioelectrochemistry 149, 108319,
14	# doi:10.1016/j.bioelechem.2022.108319), which was not read; details left open below may be
15	# fixed there.
16	#
17	# The dandiset's title and description on DANDI name the Figure 2 experiment (paired-pulse
18	# against single-pulse trains, 5 pulses, 600 + 600 ns or 600 ns, 1 Hz or 833 kHz, BPAE
19	# monolayers, YP emission as % of the single-pulse train in the same ROI, against the angle of
20	# field direction change) and say it holds the images. Claims on Figures 3 to 5 are kept to
[... 324 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "swing.py"
}
```

```
1	"""Loading and measures for the YO-PRO-1 images of dandiset 000631.
2	
3	Kim, Semenov, Kiester, Keppler, Ibey, Bixler, Colunga Biancatelli & Pakhomov (2023), Int J Mol
4	Sci 24, 10921, doi:10.3390/ijms241310921.
5	
6	Each NWB file holds one dish: one stitched image (`acquisition/ScaningImaging/data`, uint16,
7	rows x columns x 2) whose channel 0 is MemBrite (all cells) and channel 1 is YO-PRO-1 (YP, the
8	electroporation marker), as the ImageSeries description lists them. The files hold no pixel
9	size, no electrode positions, no ROIs and no angles. Files are streamed from the archive at the
10	pinned version: each file is fetched into memory by parallel HTTP range requests and its chunks
11	are decompressed there; nothing is written to disk.
12	
13	Where the parameters come from:
14	
15	- `UM_PER_PX = 0.65`: an assumption. The files give no pixel size. Methods 4.4 names the camera
16	  (ORCA-Flash4 sCMOS) and a 10x objective; the camera's 6.5 um pixels through a 10x objective
17	  give 0.65 um per pixel. The notebook checks it against the footprint of the 1.5 mm needles
18	  (Methods 4.2) and against the 32 ROIs of 200 um that Methods 4.4 places from base to apex.
19	- `ROI_UM = 200`, `N_ROI = 32`: Methods 4.4 ("a total of 32 ROIs (200 x 200 um) were placed
20	  along the dashed line").
[... 553 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_kim_2023.ipynb'))
for i,c in enumerate(nb['cells']):
    print('='*20,i,c['cell_type'])
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        if 'text' in o: print('--OUT--');print(''.join(o['text'])[:6000])
        elif 'data' in o:
            d=o['data']
            if 'text/plain' in d: print('--OUT(data)--');print(''.join(d['text/plain'])[:6000])
            if 'image/png' in d: print('[image]')
        elif o.get('output_type')=='error': print('--ERR--',o['ename'],o['evalue'])
"
```

```
<persisted-output>
Output too large (90KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work--temp-work/c29e45d5-9485-4dd7-a71d-7b5c9c560448/tool-results/bl5h8h0ic.txt

Preview (first 2KB):
==================== 0 markdown
# Reproducing Kim et al. (2023) from dandiset 000631

**Paper.** Kim V, Semenov I, Kiester AS, Keppler MA, Ibey BL, Bixler JN, Colunga Biancatelli RML,
Pakhomov AG (2023). Control of the Electroporation Efficiency of Nanosecond Pulses by Swinging the
Electric Field Vector Direction. *Int J Mol Sci* 24, 10921.
[doi:10.3390/ijms241310921](https://doi.org/10.3390/ijms241310921). The claims file was written
from the version of record as served by Europe PMC (PMC10341945), with no supplement (the paper
has none) and no figures; the paper links no code.

**Dandiset.** [DANDI:000631](https://dandiarchive.org/dandiset/000631/0.231012.1508), version
0.231012.1508. The paper cites no version of the dandiset (its data statement says the data are
available on request), so the most recent published version is pinned; it is the only one. The
draft holds the same 15 assets (same asset ids and sizes).

**What the dandiset holds.** Fifteen stitched images (MemBrite and YO-PRO-1) of BPAE monolayers
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/c29e45d5-9485-4dd7-a71d-7b5c9c560448/tool-results/bl5h8h0ic.txt"
}
```

```
1	==================== 0 markdown
2	# Reproducing Kim et al. (2023) from dandiset 000631
3	
4	**Paper.** Kim V, Semenov I, Kiester AS, Keppler MA, Ibey BL, Bixler JN, Colunga Biancatelli RML,
5	Pakhomov AG (2023). Control of the Electroporation Efficiency of Nanosecond Pulses by Swinging the
6	Electric Field Vector Direction. *Int J Mol Sci* 24, 10921.
7	[doi:10.3390/ijms241310921](https://doi.org/10.3390/ijms241310921). The claims file was written
8	from the version of record as served by Europe PMC (PMC10341945), with no supplement (the paper
9	has none) and no figures; the paper links no code.
10	
11	**Dandiset.** [DANDI:000631](https://dandiarchive.org/dandiset/000631/0.231012.1508), version
12	0.231012.1508. The paper cites no version of the dandiset (its data statement says the data are
13	available on request), so the most recent published version is pinned; it is the only one. The
14	draft holds the same 15 assets (same asset ids and sizes).
15	
16	**What the dandiset holds.** Fifteen stitched images (MemBrite and YO-PRO-1) of BPAE monolayers
17	after paired-pulse and single-pulse trains in the triangular array at 1 Hz and 833 kHz: the
18	experiment of Figure 2, whose 833 kHz dishes are also those of Figure 4. One 1 Hz control image is
19	deposited twice. The square-array experiment of Figure 3 and the FluoVolt strobe imaging of
20	Figure 5 are not in it. The files hold no pixel size, electrode positions, ROIs, angles or
[... 620 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work--temp-work/c29e45d5-9485-4dd7-a71d-7b5c9c560448/tool-results/bl5h8h0ic.txt",
 "offset": 640,
 "limit": 600
}
```

```
640	             b    True    False      False
641	L2     B     a   False    False      False
642	             b   False     True      False
643	       C     a   False    False      False
644	             b   False     True      False
645	
646	Outcome per layout, background (b), which decides: {'L1': 'criterion not met', 'L2': 'criterion not met'}
647	Variant, background (a), deciding nothing: {'L1': 'criterion not met', 'L2': 'criterion not met'}
648	
649	==================== 22 code
650	# Variants: control subsets, the 833 kHz paired dish with the wrong description left out, YP over MemBrite.
651	variants = {
652	    "all controls": dict(),
653	    "1 Hz controls of 7-31-21 only": dict(controls=lambda s: "7-31-21" in s),
654	    "1 Hz controls of 8-9-21 only (day of the paired dishes)": dict(controls=lambda s: "8-9-21" in s),
655	    "833 kHz without BPAE-13 of 8-24-21": dict(paired=lambda s: not s.endswith("8-24-21-BPAE-13")),
656	    "YP / MemBrite": dict(measure="ratio"),
657	}
658	rows = []
659	for name, kw in variants.items():
[... 556 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/*; grep -n -i -E "footprint|ROI|spontaneous|dashed|180|plateau|60-fold|20-fold|control samples|n = 3|200 ×|pixel|camera|objective" paper/*.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import re
t=open('paper/10.3390-ijms241310921.txt').read()
for kw in ['footprint','32 ROI','control samples','Figure 2 .','dashed','angle of','Figure 1 ','pixel','ORCA','4.3','Figure 7']:
    for m in re.finditer(re.escape(kw),t):
        print('##',kw,':',t[max(0,m.start()-500):m.start()+600].replace('\n',' '));print()
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
t=open('paper/10.3390-ijms241310921.txt').read()
for kw in ['2.1. ','Figure 2. ','4.2. ','4.3. ','2.3. ']:
    i=t.find(kw)
    print('##',kw,i, t[i:i+3500].replace('\n',' '));print()
E
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('reproduce_kim_2023.ipynb'))
for i in (26,32):
    for o in nb['cells'][i].get('outputs',[]):
        if 'text' in o: print(''.join(o['text'])[-3500:])
print(len(nb['cells']))
for i,c in enumerate(nb['cells'][33:],33): print(i,c['cell_type'],''.join(c['source'])[:3000])
"
```

```
1 False
    L2     B  a    i 833 kHz    1.37    1.74           114.58            80.21              -0.68        0.35      11 False          1 False
    L2     B  a   ii    1 Hz    1.08    1.60           147.81            33.78              -1.35        0.52      11 False          1 False
    L2     B  a   ii 833 kHz    1.36    1.72           114.58            80.21              -0.61        0.35      11 False          1 False
    L2     B  b    i    1 Hz    1.24    2.36           147.81            33.78              -2.79        1.52      11 False          1 False
    L2     B  b    i 833 kHz    2.78    2.96            94.55            94.55               0.04        1.11      11  True          1 False
    L2     B  b   ii    1 Hz    1.15    2.08           147.81            33.78              -2.00        1.08      11 False          1 False
    L2     B  b   ii 833 kHz    2.58    2.80            94.55            94.55               0.29        1.05      11  True          1  True
    L2     C  a    i    1 Hz    1.10    1.66           146.09            41.08              -1.80        0.63      11 False          0 False
    L2     C  a    i 833 kHz    1.37    1.74           115.05            82.58              -0.80        0.40      11 False          0 False
    L2     C  a   ii    1 Hz    1.08    1.60           146.09            41.08              -1.58        0.61      11 False          0 False
    L2     C  a   ii 833 kHz    1.36    1.72           115.05            82.58              -0.71        0.41      11 False          0 False
    L2     C  b    i    1 Hz    1.24    2.36           146.09            41.08              -3.31        1.74      11 False          0 False
    L2     C  b    i 833 kHz    2.78    2.96            96.14            96.14               0.05        1.29      11  True          0 False
    L2     C  b   ii    1 Hz    1.15    2.08           146.09            41.08              -2.36        1.25      11 False          0 False
    L2     C  b   
[... 79 more lines not kept]
```

**Agent**

Notebook read. Now checking the archive for the blocked Figure 3/5 claims.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000631/versions/0.231012.1508/assets/?page_size=200" | python3 -c "
import json,sys; d=json.load(sys.stdin); print(d['count'])
for a in d['results']: print(a['path'], a['size'])"; curl -s "https://api.dandiarchive.org/api/dandisets/000631/versions/0.231012.1508/" | python3 -c "
import json,sys; d=json.load(sys.stdin); print(d.get('name')); print(d.get('description')); print(d.get('assetsSummary'))"; curl -s "https://api.dandiarchive.org/api/dandisets/000631/versions/" | python3 -m json.tool | grep -E '"version"|"status"'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  python3 - <<'E'
import numpy as np, swing
# synthetic triangle in blocks: base 4.63mm, height 6.1mm
mpb=swing.mm_per_block()
c=np.array([60.,60.])/mpb*0+np.array([1500.,1500.])
g={"apex":c+np.array([-6.1/mpb,0]),"base1":c+np.array([0,-2.315/mpb]),"base2":c+np.array([0,2.315/mpb])}
for lay in ("L1","L2"):
    r=swing.roi_centres(g,lay); s=(np.linalg.norm(r-c,axis=1)*mpb*np.sign(c[0]-r[:,0]))
    print(lay, s[:3].round(2), s[-2:].round(2), np.diff(s)[:2].round(3))
    aC,fC=swing.bisector_angles(g,lay,"C",None)
    grid=swing.GridModel(np.array([g[k] for k in ("apex","base1","base2")])*mpb, np.array([3000,3000])*mpb)
    aB,fB=swing.bisector_angles(g,lay,"B",None,grid)
    print(' C',aC[[0,5,15,25,31]].round(1),' B',aB[[0,5,15,25,31]].round(1), 'fieldratio B/C', (fB/fC)[[0,15,31]].round(2))
# crossover & at_180
a=np.array([180,170,160,150,140.]); v=np.array([50,80,90,110,120.])
print(swing.crossover(v,a), swing.at_180(v,a,1), swing.at_180(v,a,2))
P=np.array([[1,2.],[3,4]]); S=np.array([[2,2.],[4,4]])
print(swing.normalised(P,S,"i").mean(0), swing.normalised(P,S,"ii"))
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
cd  ls /usr/bin/python3* ; which -a python3 python; for p in $(which -a python3 python); do $p -c "import numpy,scipy,h5py;print('$p ok')" 2>/dev/null; done; pip install --user numpy scipy h5py requests 2>&1 | tail -1
```

```
/usr/bin/python3
/usr/bin/python3-config
/usr/bin/python3.14
/usr/bin/python3.14-config
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python3
/usr/bin/python3
/bin/python3
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
/opt/hostedtoolcache/Python/3.13.17/x64/python
/usr/bin/python
/bin/python
```

**Agent calls Bash**

```bash
cd  python3 -m venv $TMPDIR/v && $TMPDIR/v/bin/pip install -q numpy scipy h5py requests 2>&1 | tail -2; $TMPDIR/v/bin/python -c "import numpy,scipy;print('ok')"
```

```
ok
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'E'
import numpy as np, swing
mpb=swing.mm_per_block()
c=np.array([1500.,1500.])
g={"apex":c+np.array([-6.1/mpb,0]),"base1":c+np.array([0,-2.315/mpb]),"base2":c+np.array([0,2.315/mpb])}
grid=swing.GridModel(np.array([g[k] for k in ("apex","base1","base2")])*mpb, np.array([3000,3000])*mpb)
for lay in ("L1","L2"):
    r=swing.roi_centres(g,lay); s=(c[0]-r[:,0])*mpb
    print(lay, s[:2].round(2), s[-1].round(2), np.diff(s)[:1].round(3))
    aC,fC=swing.bisector_angles(g,lay,"C",None)
    aB,fB=swing.bisector_angles(g,lay,"B",None,grid)
    print(' C',aC[[0,5,15,25,31]].round(1),' B',aB[[0,5,15,25,31]].round(1), 'field B/C', (fB/fC)[[0,15,31]].round(2))
# angle exactly at base midpoint and where 180
pts=np.array([[c[0]+d/mpb, c[1]] for d in (0,0.5,1.0,1.5,2.0)])*mpb
cen=np.array([g[k] for k in ("apex","base1","base2")])*mpb
E1=swing.field_line_sources(cen,np.array([0,1.,0]),pts);E2=swing.field_line_sources(cen,np.array([0,0,1.]),pts)
print('C angle at 0,0.5..2 mm beyond midpoint (away from apex):',swing.angle_deg(E1,E2).round(1))
a=np.array([180,170,160,150,140.]); v=np.array([50,80,90,110,120.])
print(swing.crossover(v,a), swing.at_180(v,a,1), swing.at_180(v,a,2))
P=np.array([[1,2.],[3,4]]); S=np.array([[2,2.],[4,4]])
print(swing.normalised(P,S,"i").mean(0), swing.normalised(P,S,"ii"))
# square_mean on constant/gradient image
img=np.tile(np.arange(400.),(400,1))
print(swing.square_mean(img,np.array([200.,200.]),np.array([1.,0])), swing.disk_mean(img,np.array([200.,200.]),0.5))
E
```

```
swing.py:376: RuntimeWarning: invalid value encountered in divide
  c = (E1 * E2).sum(1) / (np.linalg.norm(E1, axis=1) * np.linalg.norm(E2, axis=1))
L1 [0.   0.17] 5.25 [0.169]
 C [168.5 154.  112.   54.9  22.4]  B [180. 180. 180. 180.  nan] field B/C [1.03 0.93 0.  ]
L2 [-0.95 -0.75] 5.25 [0.2]
 C [179.2 167.7 126.2  61.3  22.4]  B [180. 180. 180. 180.  nan] field B/C [1.02 0.97 0.  ]
C angle at 0,0.5..2 mm beyond midpoint (away from apex): [168.5 175.4 178.6 173.4 168.9]
155.0 (50.0, 0) (50.0, 0)
[ 75.  112.5] [[ 66.66666667 100.        ]]
199.5 199.5
```

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python - <<'E'
import numpy as np, swing
mpb=swing.mm_per_block()
c=np.array([1500.,1500.])
g={"apex":c+np.array([-6.1/mpb,0]),"base1":c+np.array([0,-2.315/mpb]),"base2":c+np.array([0,2.315/mpb])}
cen=np.array([g[k] for k in ("apex","base1","base2")])*mpb
for dc in (np.array([3000,3000])*mpb, cen.mean(0)):
    grid=swing.GridModel(cen, dc)
    print('dish centre',dc.round(2),'x0',grid.x0.round(2),'n',grid.n,'elec counts',[(grid.elec==i).sum() for i in range(3)])
    phi=grid.potential([0,1.,0]); print(' phi range',phi[grid.inside].min(),phi[grid.inside].max())
    aB,fB=swing.bisector_angles(g,"L2","B",None,grid); aC,fC=swing.bisector_angles(g,"L2","C",None)
    print(' B',aB[[0,5,15,25,31]].round(1),'C',aC[[0,5,15,25,31]].round(1),'|E| B/C',(fB/fC)[[0,15,30]].round(2))
E
```

```
swing.py:376: RuntimeWarning: invalid value encountered in divide
  c = (E1 * E2).sum(1) / (np.linalg.norm(E1, axis=1) * np.linalg.norm(E2, axis=1))
dish centre [19.5 19.5] x0 [1.9 1.9] n 353 elec counts [np.int64(0), np.int64(172), np.int64(172)]
 phi range 0.0 1.0
 B [180. 180. 180. 180.  nan] C [179.2 167.7 126.2  61.3  22.4] |E| B/C [1.02 0.97 0.  ]
dish centre [7.72 9.75] x0 [-9.88 -7.85] n 353 elec counts [np.int64(179), np.int64(177), np.int64(177)]
 phi range 0.0 1.0
 B [179.9 169.4 126.7  57.8   9. ] C [179.2 167.7 126.2  61.3  22.4] |E| B/C [1.02 1.   0.99]
```

**Agent**

Helpers behave correctly on synthetic inputs (one false alarm was my own test geometry). Quick look at the fit overview and the profile plots.

**Agent calls Bash**

```bash
cd  $TMPDIR/v/bin/python -c "
import json,base64,os
nb=json.load(open('reproduce_kim_2023.ipynb'))
for i in (13,18):
    for o in nb['cells'][i]['outputs']:
        if 'data' in o and 'image/png' in o['data']:
            open(os.environ['TMPDIR']+f'/c{i}.png','wb').write(base64.b64decode(o['data']['image/png']))
"; ls $TMPDIR/*.png
```

```
/tmp/claude-1001/c13.png
/tmp/claude-1001/c18.png
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c13.png"
}
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/c18.png"
}
```

Result: no output.

Result: no output.

## Prompt

[Image: original 2169x1290, displayed at 2000x1189. Multiply coordinates by 1.08 to map to original image.]

**Agent**

**Verifier report, round 1: Kim et al. 2023 (doi:10.3390/ijms241310921) on DANDI:000631 v0.231012.1508**

The claims file has 12 claims. The notebook tests 6: five on Figure 2 and one on Figure 4. It treats 6 as blocked: four on Figure 3 and two on Figure 5.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| fig2-180-cancellation | partially_reproduced | Under background (b), no ROI layout gives both values (cell 21). Layout L2 gives 18.5 / 22.0-fold at 833 kHz (holds), but 2.42–2.51-fold at 1 Hz, outside 2 ± 0.2. Layout L1 gives 1.92 / 2.19-fold at 1 Hz (holds), but only about 11-fold at 833 kHz. Cancellation at 180°, and stronger cancellation at 833 kHz, are clear under every reading. |
| fig2-crossover-angle | reproduced | Cell 24: 1 Hz crosses at 145.3–149.6° (tolerance 144–176) and 833 kHz at 125.3–125.9° (117–143), under every layout, angle model and normalisation. The 1 Hz value is fragile; see problem 4. |
| fig2-facilitation-plateau | partially_reproduced | At 833 kHz with layout L2, the level is 2.58–2.96, reached at 94.5–96°, and the plateau holds (cell 26). At 1 Hz the 90–100° level is only 1.15–1.36-fold. The 1 Hz slope below 90° is significantly non-zero under every reading, and uptake keeps rising to about 3-fold near 0°, so there is no plateau. The criterion needs both frequencies. |
| fig2-frequency-dependence | reproduced | Cell 28: all conditions met in all 16 readings. The 180° value is lower at 833 kHz (4.5–8.9% against 40–52% at 1 Hz), the crossover angle is smaller (125° against 145–150°), and the curves are above 100% at the smallest angle and below 100% at the largest. |
| fig2-60-fold-co-counter | reproduced (low confidence) | Under background (b) with layout L2, plateau level ÷ lowest-ROI value gives 54.8 / 61.6 (level2) and 56.8 (level1, norm ii), inside 60 ± 6 (cell 30). Layout L1 gives at most 34.5 and fails. I take L2 as the reading that decides, because L1 never reaches 180°: its largest angle is about 170° (cell 11), while the paper puts 180° at the base. The ratio rests on a denominator of about 5% of control and is very sensitive to the background estimate (problem 1). |
| fig4-unipolar-pattern | reproduced | Cell 32: all 8 readings agree. In 3 of 3 paired dishes the apex is above both bases, and in 3 of 3 single dishes the energised base is above the apex. In the single dishes both bases exceed the apex, so which base is taken as energised does not matter. Field-map Spearman ρ is 0.50, 0.96 and 0.93 for single dishes, and negative for paired dishes (cell 33). |
| fig3-1hz-co-equals-cross | blocked (data_missing) | I checked the archive: all 15 assets are triangular-array YP/MemBrite images from the Figure 2 experiment (1 Hz / 833 kHz, BP/UP). There is no square-array data. |
| fig3-770khz-co-enhanced | blocked (data_missing) | Same as above; no 770 kHz files. |
| fig3-770khz-cross-same-as-1hz | blocked (data_missing) | Same as above. |
| fig3-no-area-dependence | blocked (data_missing) | The claims file judges it by fig3-1hz-co-equals-cross, which is blocked. The Figure 2 plateau result does not decide it. |
| fig5-base-sawtooth | blocked (data_missing) | No FluoVolt strobe or CHO-K1 files in the archive. All 15 assets are single stitched 2-channel images with no time series. |
| fig5-apex-larger-polarization | blocked (data_missing) | Same as above. |

### B. Problems

1. **[affects a conclusion]** Background estimate, `swing.footprint_background` / `FOOTPRINT_BG_MM = 0.5`.
   - Methods 4.4 says the footprint cells were "shielded from the field". The needles are hollow, with a 0.5 mm inner diameter, so the shielded lumen has a radius of 0.25 mm.
   - The 0.5 mm disk the notebook uses is about 75% steel-wall annulus by area, where the needle tip sits on the glass. That is not clearly the shielded cells.
   - The fold values are extremely sensitive to this number. From cell 18 at 833 kHz near 180°, paired YP is only about 25 counts above a background of about 215, against about 570 counts for the controls. A 10-count shift in background moves the 20-fold value to roughly 16 or 36, and moves the 60-fold ratio with it.
   - The paper's 1 Hz 2-fold sits between the (a) and (b) readings (1.3–1.5 and 2.4–2.5).
   - No sensitivity run was done, using the lumen only or other radii. This affects fig2-180, fig2-60-fold and the plateau levels.
2. **[affects a conclusion]** ROI layout, cells 16–30 and `roi_centres`.
   - The claims-file layout (32 contiguous ROIs from the base midpoint, outside the footprints) cannot fit: it spans 6.4 mm, but the midpoint-to-apex-footprint distance is 5.37 mm (cell 9). This is not stated as a deviation from the claims file.
   - The two substitutes give different outcomes for fig2-60-fold (`combine` output in cell 30: L1 not met, L2 met). No printed rule says which layout decides.
   - L1 overlaps ROIs by about 15% and never reaches 180°, which argues against it. That argument is mine, not the notebook's.
3. **[affects a conclusion, fig2-180 and fig2-60]** Selection bias. Reading (2), "ROI of lowest mean", takes a minimum over 32 noisy ROIs. This biases the fold upward, and it is the only route by which 833 kHz reaches 20 ± 2 (reading 1 gives 11.8–12.7) and 60 ± 6. The claims file permits this reading; the bias is not discussed.
4. **[does not affect a conclusion]** The 1 Hz crossover rests on one ROI. In cell 18 (L2), ROI 11 at 147.8° is 108%, while ROIs 12–14 fall back to 79–93%. Without that ROI the crossover would be about 128°, outside the tolerance. Also, the 8-9-21-only controls give 130.5° under normalisation (ii) (cell 24). The criterion is still met as written.
5. **[does not affect a conclusion]** In `plateau_measures` (cell 26), P2 needs ROIs below 10°. Model C has none (smallest angle about 22°), so P2 is automatically False. This creates a spurious disagreement between angle models B and C at 833 kHz. It should be reported as untestable, not "not met".
6. **[does not affect a conclusion]** Plateau level1, "between 90 and 100°", contains a single ROI (94.3° or 94.5°) under L2. It is a one-ROI estimate, not a mean.
7. **[does not affect a conclusion]** Some choices are made without the paper specifying them:
   - Which 1 Hz controls count toward n: all 5 unique dishes from two days are used, while the paper gives n = 3 for paired dishes only.
   - The 833 kHz controls were imaged on a different day with a larger mosaic. Normalisation therefore assumes the same exposure and gain across days, which is never checked.
   - Variants are shown for the control subsets.
8. **[does not affect a conclusion]** Checks that were sound:
   - The duplicate file (7-31-21 BPAE-03/18) was correctly dropped.
   - The mislabelled 833 kHz BPAE-13 is used, with an exclusion variant.
   - The pixel-size assumption of 0.65 µm is supported by the measured footprint radius (0.72 mm) and the field range (5–10 kV/cm at 4 kV).
   - I tested `crossover`, `at_180`, `normalised`, `square_mean`, `field_line_sources` and `GridModel` on synthetic inputs. They behave correctly, and models B and C agree to within about 1° away from the apex.

### C. What I could not check

- **Background sensitivity.** Needed: the radial YP profile inside each footprint (rings at r < 0.25 mm and 0.25–0.5 mm) and the fig2-180 / fig2-60 values recomputed with a lumen-only background.
- **Cross-day intensity comparability.** Needed: the exposure and gain metadata, which the files lack, or at least the MemBrite and unexposed-region YP levels compared per day.
- **Saturation inside ROIs.** Needed: the fraction of pixels at or above 60000 within the bisector and adjacent ROIs, before block averaging.
- **Which layout the paper used.** Needed: the paper's Figure 7B, which was not available, or the notebook printing the angle at the base midpoint and the position of the 180° point relative to the base line.
- **Pairing of control and paired ROIs.** Needed: a per-dish table of the ROI-0 to ROI-5 values for paired and control dishes, to see whether the 833 kHz denominator is driven by one dish. Per-dish values are shown only for the largest-angle ROI (cell 22: 5.8–9.0%).

## End of run

21 turns, 4 minutes, result: success.
