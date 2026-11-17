# shi-2013 · author-revise-1 · run 42694217552

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/shi-2013/verifier-1-report.md; ls entries/shi-2013 entries/shi-2013/*; wc -l docs/protocol.md
```

```
Mon Nov  9 20:41:38 UTC 2026
**Verifier report, round 1: Shi, Apker & Buneo 2013 on CRCNS ppc-1**

The claims file has 28 claims. The notebook marks 25 as tested and 3 as blocked.

### A. Outcomes

| Claim | My outcome | Reason |
|---|---|---|
| behavior-mean-position-sessions | not_reproduced | Cell 24 gives 16.1% under both readings, against 6.9 ± 1.5%. Monkey X only (8 target percentages, not 16). This rests on record fields 19–21 being the trial mean over the hold, which was never checked (B2). |
| behavior-variability-sessions | not_reproduced | Cell 26: no centre and averaging combination puts all three axes within tolerance. Mean-centred gives 8.1, 8.1 and 7.0%; median-centred gives 0.4 to 0.7%. |
| table1-endpoint-means | partially_reproduced | Cell 28: all 48 monkey X means are within the Table 1 SDs. But the largest V vs NV difference is 0.150 cm (135°, y), above the 0.121 bound. Monkey B's 48 values cannot be tested. |
| table1-endpoint-sd | not_reproduced | Cell 30: 8.3% of SDs are within 10%. Data SDs are about 0.55 × Table 1 (0.32 to 0.67 cm against 0.50 to 1.28 cm). |
| fig3-example-neuron | not_reproduced | Cell 32: 8 units peak at 225° in both conditions with a position effect, but none matches. The closest has P_vis 0.364 and P_int 0.537. The paper's cell may be from monkey B, which the notebook could not find. |
| movement-epoch-tuning | not_reproduced | Cell 34: 187/359 (52.1%, 179 scaled to 343), against 139 ± 13.9, with code 8 read as onset. Reading (b) was not run. |
| hold-position-main-effect | reproduced | Cell 36: 141/359 (39.3%, 135 scaled to 343), against 135 ± 13.5. The PSTH variant agrees (142). |
| hold-vision-main-effect | reproduced | 49/359 (13.6%, 47 scaled to 343), against 44 ± 4.4, and fewer than position. The all-units variant (49 scaled) falls just outside. |
| hold-interaction | reproduced | 27/359 (7.5%, 26 scaled to 343), against 27 ± 2.7 (reading a). |
| hold-subepochs | not_reproduced | Cell 38, main population: 1 of 6 va
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/protocol.md
```

```
<persisted-output>
Output too large (37.5KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5451ffff-aeb9-406a-bbb1-a1bd3eb4633c/tool-results/bdul3nsje.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-14`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
- The **author** tests the claims on the dataset. It reads the paper to
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/5451ffff-aeb9-406a-bbb1-a1bd3eb4633c/tool-results/bdul3nsje.txt"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-14`. Record this version in the attempt's provenance.
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
[... 628 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep shi; wc -l attempts/shi-2013-01.yaml entries/shi-2013/ppc.py; cat entries/shi-2013/entry.yaml; ls questions | grep shi; ls executed/shi-2013 2>/dev/null; ls paper; git log --oneline -8 -- entries/shi-2013
```

```
ishii-2025-01.yaml
shi-2013-01.yaml
shin-2025-01.yaml
  467 attempts/shi-2013-01.yaml
  349 entries/shi-2013/ppc.py
  816 total
schema_version: 1
name: shi-2013
type: reproduction
title: Limb position, vision and area 5 activity (Shi, Apker and Buneo 2013)
description: Tests the findings of Shi, Apker and Buneo (2013) on CRCNS ppc-1, which holds the
  sorted spikes and trial events of area 5 recordings while monkeys held the arm at eight targets
  with or without vision of a cursor. It compares hand positions, ANOVA effect counts, suppression
  indexes, variability and decoding between the Vision and No Vision conditions. The data set holds
  monkey X's sessions only, and which condition code is Vision is inferred from the data.
license: Apache-2.0
notebooks:
- path: reproduce_shi_2013.ipynb
  title: Reproducing Shi et al. (2013) from CRCNS ppc-1
  runtime_minutes: 12
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/shi-2013-01.yaml
```

```
schema_version: 3
id: shi-2013-01
datasets:
- archive: crcns
  id: ppc-1
  version: unversioned
  doi: 10.6080/K0CZ353K
  relation: primary
paper: doi:10.1152/jn.00223.2012
date: 2026-11-09
entry: shi-2013
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code
    model: claude-opus-5-5
    protocol: pilot-14
  runner:
[... 447 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/shi-2013/ppc.py
```

```
"""Loading and measures for CRCNS ppc-1 (Shi, Apker and Buneo 2013).

Dataset: crcns:ppc-1/unversioned (CRCNS data sets are not versioned; DOI
10.6080/K0CZ353K). The file read is ppc-1/live/data.tar.gz, MD5
bbb341b8947a6314b2618f0caa0b64f8 in the data set's checksums.md5.

The data set is one gzip-compressed tar file, ``ppc-1/live/data.tar.gz`` in the
public CRCNS bucket. A gzip stream cannot be read at random, so the file is
streamed once from the start (``tarfile`` in stream mode over ``fsspec``) and
each session's MATLAB file is reduced to a trial table and spike times as it
passes. Nothing is written to disk.

What the files hold (worked out from the data; the data descriptor describes
only the variable names):

- ``<session>.mat``: ``strobed`` (event times in seconds, event codes),
  ``data.<chan><unit>`` (spike times in milliseconds), ``waveforms``, ``nunits``.
- The event stream of each trial starts with code 0. After the trial's events
  a code 255 is followed by an ASCII text record, one character per strobe
  (codes 44 to 57 are ',', '-', '.', '0' to '9'), of 22 comma separated
[... 329 more lines not kept]
```

**Agent**

Starting the round-1 revision. I've read the report, protocol, record and helper; now looking at the notebook structure.

**Agent calls Bash**

```bash
cd entries/shi-2013 && python - <<'EOF'
import json
nb=json.load(open('reproduce_shi_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(f"--- [{i}] {c['cell_type']} tags={c.get('metadata',{}).get('tags')} len={len(src)}")
    print(src[:300])
EOF
```

```
<persisted-output>
Output too large (30.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/5451ffff-aeb9-406a-bbb1-a1bd3eb4633c/tool-results/bo25nvmle.txt

Preview (first 2KB):
--- [0] markdown tags=None len=2731
# Reproducing Shi, Apker and Buneo (2013) on CRCNS ppc-1

**Paper.** Shi Y, Apker G, Buneo CA (2013). Multimodal representation of limb endpoint position in
the posterior parietal cortex. *J Neurophysiol* 109: 2097-2107.
[doi:10.1152/jn.00223.2012](https://doi.org/10.1152/jn.00223.2012)

**Dataset.*
--- [1] code tags=None len=573
import time
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
[... 36 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/5451ffff-aeb9-406a-bbb1-a1bd3eb4633c/tool-results/bo25nvmle.txt"
}
```

```
1	--- [0] markdown tags=None len=2731
2	# Reproducing Shi, Apker and Buneo (2013) on CRCNS ppc-1
3	
4	**Paper.** Shi Y, Apker G, Buneo CA (2013). Multimodal representation of limb endpoint position in
5	the posterior parietal cortex. *J Neurophysiol* 109: 2097-2107.
6	[doi:10.1152/jn.00223.2012](https://doi.org/10.1152/jn.00223.2012)
7	
8	**Dataset.*
9	--- [1] code tags=None len=573
10	import time
11	import warnings
12	from pathlib import Path
13	
14	import matplotlib.pyplot as plt
15	import numpy as np
16	import pandas as pd
17	import yaml
18	from scipy import stats
19	
20	import ppc
[... 544 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -l paper/*.txt; grep -n -i -E "hold|eye|219|124|343|session|optotrak|sampled|endpoint position was|analog" paper/10.1152-jn.00223.2012.txt | head -80
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 100,215p paper/10.1152-jn.00223.2012.txt; sed -n 1040,1080p paper/10.1152-jn.00223.2012.txt; cat paper/ppc-1.data-description.txt | head -156
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i -E "received|accepted|submitted|first published" paper/10.1152-jn.00223.2012.txt | head; sed -n 315,330p paper/10.1152-jn.00223.2012.txt; sed -n 655,665p paper/10.1152-jn.00223.2012.txt; ls executed 2>/dev/null | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd entries/shi-2013; echo $TMPDIR; python -c "import sys;print(sys.version)"; pip list 2>/dev/null | grep -i -E "numpy|scipy|pandas|fsspec|aiohttp|statsmodels"
```

```
/tmp/claude-1001
3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
```

**Agent calls Bash**

```bash
cd  ls; cat tools/entry.py | head -60; ls .venv* envs 2>/dev/null | head
```

```
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
encore_science
entries
node_modules
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
pyproject.toml
questions
queue
schemas
scripts
[... 67 more lines not kept]
```

**Agent**

Building a dev venv from the lock file, then streaming once into a cache.

**Agent calls Bash**

```bash
cd entries/shi-2013; uv venv -q $TMPDIR/venv --python 3.13 && uv pip install -q --python $TMPDIR/venv/bin/python -r requirements.lock.txt 2>&1 | tail -3; $TMPDIR/venv/bin/python -c "import numpy, scipy, pandas, fsspec; print('ok')"
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/shi-2013; cat > $TMPDIR/cache.py <<'EOF'
import pickle, time, re, os
import ppc
t=time.time()
tf = ppc.open_stream()
members, sessions, errors, ana = [], {}, {}, {}
for m in tf:
    members.append((m.name, m.size))
    if not m.isfile(): continue
    if "plxAnaAD" in m.name and len(ana) < 12 and m.size < 150e6:
        ana[m.name] = tf.extractfile(m).read(); continue
    if not ppc.SESSION_RE.match(m.name): continue
    raw = tf.extractfile(m).read()
    try:
        units, strobed = ppc.read_session_mat(raw)
        sessions[m.name] = dict(units=units, trials=ppc.trial_table(strobed), strobed=strobed)
    except Exception as exc:
        errors[m.name] = repr(exc)
pickle.dump(dict(members=members, sessions=sessions, errors=errors), open(os.environ["TMPDIR"]+"/D.pkl","wb"))
pickle.dump(ana, open(os.environ["TMPDIR"]+"/ana.pkl","wb"))
print("done", (time.time()-t)/60, "min", len(sessions), len(ana))
import resource; print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,"GB")
EOF
$TMPDIR/venv/bin/python $TMPDIR/cache.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/cache.py", line 2, in <module>
    import ppc
ModuleNotFoundError: No module named 'ppc'
```

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/cache.py
```

```
done 5.62826626698176 min 415 12
0.546756 GB
```

**Agent calls Bash**

```bash
cd entries/shi-2013; date -u; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, io, numpy as np, scipy.io as sio
ana=pickle.load(open(os.environ["TMPDIR"]+"/ana.pkl","rb"))
for k,v in ana.items(): print(k, len(v))
k=[k for k in ana if k.endswith(".mat")][0]
d=sio.loadmat(io.BytesIO(ana[k]),squeeze_me=True)
for kk,vv in d.items():
    if kk.startswith("__"): continue
    print(kk, type(vv), getattr(vv,'shape',None), getattr(vv,'dtype',None), str(vv)[:200])
EOF
```

```
Mon Nov  9 20:48:25 UTC 2026
data/010609/010609_1.plxAnaAD.dat 9117630
data/010609/010609_1.plxAnaAD.mat 139550
data/010609/010609_2.plxAnaAD.dat 9690290
data/010609/010609_2.plxAnaAD.mat 147263
data/010809/010809_1.plxAnaAD.dat 8387734
data/010809/010809_1.plxAnaAD.mat 125807
data/010809/010809_2.plxAnaAD.dat 11481056
data/010809/010809_2.plxAnaAD.mat 178143
data/010809/010809_3.plxAnaAD.dat 12783990
data/010809/010809_3.plxAnaAD.mat 200051
data/010809/010809_4.plxAnaAD.dat 2131516
data/010809/010809_4.plxAnaAD.mat 24858
aChannel <class 'int'> None None 0
ADFrequency <class 'int'> None None 40000
EVCounts <class 'numpy.ndarray'> (512,) int32 [     0      1      0      0      0      0      0      0      0      0
      0      0      0      0      0      0      0      0      0      0
      0      0      0      0      0      0      0      0  
analogOffset <class 'int'> None None 4468604
baseANACounts <class 'numpy.ndarray'> (512,) int32 [      0       0       0       0       0       0       0       0       0
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, io, numpy as np, scipy.io as sio
ana=pickle.load(open(os.environ["TMPDIR"]+"/ana.pkl","rb"))
k="data/010609/010609_1.plxAnaAD"
d=sio.loadmat(io.BytesIO(ana[k+".mat"]),squeeze_me=True)
b=d["baseANACounts"]; print(np.flatnonzero(b), b[b>0], b.sum())
e=d["EVCounts"]; print(np.flatnonzero(e)[:20], e[e>0][:20])
raw=ana[k+".dat"]; print(len(raw), len(raw)/2, len(raw)/2/7)
x=np.frombuffer(raw,dtype="<i2")
n=b[b>0][0]
print("first 30:", x[:30])
# try channel-blocked
for layout in ("blocked","interleaved"):
    if layout=="blocked": X=x[:n*7].reshape(7,n)
    else: X=x[:n*7].reshape(n,7).T
    print(layout)
    for c in range(7):
        xc=X[c].astype(float); print(c, xc.min(), xc.max(), xc.mean().round(1), xc.std().round(1), "lag1 diff sd", np.diff(xc).std().round(2))
EOF
```

```
[301 302 303 304 305 306 307 308 309 310 311 312 313 314 315] [ 638372 1276744 1915116 2553488 2553488 2553488 2553488 2553488 2553488
 2553488 3191860 3830232 4468604 4468604 4468604] 42132552
[  1 257 258 259 300 301 302 303 310 311 312] [     1  28173      1      1 638372 638372 638372 638372 638372 638372
 638372]
9117630 4558815.0 651259.2857142857
first 30: [19536 22597   106     0     0     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0     0     0     0     0
     0     0     0     0     0     0]
blocked
0 -25536.0 31560.0 28.1 896.8 lag1 diff sd 295.3
1 -2048.0 2047.0 35.4 1949.8 lag1 diff sd 715.24
2 -2048.0 2047.0 30.1 1823.3 lag1 diff sd 573.17
3 -2048.0 2047.0 39.9 1471.4 lag1 diff sd 370.63
4 -2048.0 2047.0 -1825.1 821.3 lag1 diff sd 88.56
5 -2048.0 2047.0 -454.4 1155.9 lag1 diff sd 103.58
6 -2048.0 2047.0 -502.9 1149.5 lag1 diff sd 53.39
interleaved
0 -16988.0 23144.0 -378.6 1522.9 lag1 diff sd 1449.27
1 -2416.0 28173.0 -378.2 1522.7 lag1 diff sd 1449.44
2 -16988.0 28173.0 -378.4 1522.0 lag1 diff sd 1448.46
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, io, numpy as np, scipy.io as sio
ana=pickle.load(open(os.environ["TMPDIR"]+"/ana.pkl","rb"))
k="data/010609/010609_1.plxAnaAD"
raw=ana[k+".dat"]
x=np.frombuffer(raw,dtype="<i2"); n=638372
extra=len(x)-7*n
for off in (0, extra):
    X=x[off:off+7*n].reshape(7,n).astype(float)
    print("offset",off)
    for c in range(7): print(c, X[c].min(), X[c].max(), X[c].mean().round(1), X[c].std().round(1), np.diff(X[c]).std().round(2))
print(x[:12], x[extra-6:extra+6])
# search where blocks start: check for each candidate offset smoothness
EOF
```

```
offset 0
0 -25536.0 31560.0 28.1 896.8 295.3
1 -2048.0 2047.0 35.4 1949.8 715.24
2 -2048.0 2047.0 30.1 1823.3 573.17
3 -2048.0 2047.0 39.9 1471.4 370.63
4 -2048.0 2047.0 -1825.1 821.3 88.56
5 -2048.0 2047.0 -454.4 1155.9 103.58
6 -2048.0 2047.0 -502.9 1149.5 53.39
offset 90211
0 -2048.0 2047.0 30.0 1099.0 355.64
1 -2048.0 2047.0 31.9 1940.0 699.08
2 -2048.0 2047.0 32.5 1781.4 548.03
3 -2048.0 2047.0 -209.7 1534.1 342.95
4 -2048.0 2047.0 -1637.8 997.9 85.82
5 -2048.0 2047.0 -460.7 1152.0 97.8
6 -32764.0 32766.0 -424.1 4220.9 5769.79
[19536 22597   106     0     0     0     0     0     0     0     0     0] [  31  144  140  239  252  315  711  962 1097 1161 1284 1189]
```

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, io, struct, numpy as np
ana=pickle.load(open(os.environ["TMPDIR"]+"/ana.pkl","rb"))
b=ana["data/010609/010609_1.plxAnaAD.dat"]
print(b[:8], struct.unpack_from("<i",b,4), struct.unpack_from("<iii",b,140), struct.unpack_from("<i",b,136))
adfreq,=struct.unpack_from("<i",b,136); nd,ne,ns=struct.unpack_from("<iii",b,140)
off=7504+1020*nd+296*ne+296*ns
# slow channel headers: name at 0 (32 chars), channel at 32 int, ADFreq, Gain, Enabled, PreAmpGain
base=7504+1020*nd+296*ne
for i in range(ns):
    h=base+296*i
    name=b[h:h+32].split(b"\0")[0]; ch,fr,gain,en,pre=struct.unpack_from("<iiiii",b,h+32)
    if en: print(i,name,ch,fr,gain,en,pre)
from collections import Counter
cnt=Counter(); data={}
n=len(b)
while off+16<=n:
    typ,up,ts,ch,unit,nw,nwords=struct.unpack_from("<hHIhhhh",b,off); off+=16
    if typ==5:
        data.setdefault(ch,[]).append((((up<<32)+ts)/adfreq, np.frombuffer(b,dtype="<i2",count=nwords,offset=off)))
    cnt[(typ,ch)]+=1
    off+=2*nw*nwords
print(cnt.most_common(20))
for ch,v in data.items():
    x=np.concatenate([a for _,a in v]).astype(float)
    print(ch, len(x), x.min(), x.max(), x.mean().round(1), x.std().round(1), np.diff(x).std().round(2), "t0", v[0][0], "nblocks", len(v))
EOF
```

```
b'PLEXj\x00\x00\x00' (106,) (16, 28, 16) (40000,)
0 b'm\xfb\x9d\xfa\xea\xfa"\xfc\x8d\xfc\x02\xfdx\xfd\x07\xfe[\xfe\xf6\xfe\xa5\xfe\xe5\xfe\x16\x01P\x03<\x03\xe7\x03' 89916612 91096501 44041234 -1834864 42926255
1 b'f\x04\x15\x04M\x04\x83\x04r\x05\xd1\x04?\x04\xe0\x03\x18\x04 \x04t\x03I\x03d\x03\xec\x03Y\x04l\x03' 24183322 2556047 14745621 16515355 10813639
2 b'C\xfa\xc6\xf97\xfa[\xf9E\xf9\x96\xf9\r\xfa\xce\xfa\xaf\xfb\x95\xfe\xce\xfc\xa4\xfbf\xfeV\xff\xb6\xff\x03\x01' 15139232 13303765 23921010 7733467 24576288
3 b'\x1b' -25493948 -18678072 -12058898 -35520753 -83362851
4 b'C\x04#\x04[\x04\xfe\x03\xf2\x03\x99\x04p\x04\xfa\x03\xdc\x03\xdc\x03n\x04\xc1\x03\x95\x03\xb3\x03s\x03-\x04' 66585727 37028451 49480384 15598211 -7995258
5 b'\xc4\xfd@\xfd\xea\xfb\x9b\xfb\x03\xfc\xd6\xfc6\xfd$\xfe\x89\xfd\x92\xfd)\xfe\xfd\xfcZ\xfcU\xfcT\xfd\x90\xfd' -65471386 -33555290 -41156989 -33555086 -30343782
6 b'+\xfe\xaf\xfd\xd3\xfe\xb7\xfeL\xffC' 87164223 82248932 49677204 53740212 41419673
7 b'|\xff0\xff\xb3\xfex\xfd\xfc\xfc\xcb\xfc\x86\xfd\x8c\xfe\xe2\xfd\xa7\xfd\xe0\xfd2\xfe^\xfee\xfe,\xff\xe8\xfe' -51118594 -60687345 -41353904 -52233041 -33424053
8 b'e\xff\x1a\xffR\xff\x9e\xfe\xff\xfd\xe8\xfd\x11\xfe\xf1\xfdC\xfe\xa0\xfeo\xff\xc1\xff\xf6\xfe\xb0\xff\xcc' 51774074 61145879 89130176 88212838 101320061
9 b'\xe4\xff\xd4\xff\xce' -4980548 -18219209 -26476878 -131285 -24313914
10 b'm' 31327002 2162756 -12451896 -17957129 -13762786
11 b'\x95\xfe\x1f\xff7\xff\x96\xff\xa9\xff\x03\xff1\xff&' -8061277 -46203290 -57213534 -82707498 -73598210
12 b'\x10\x02h\x02\x17\x02d\x01\xe9' -30801775 -39715610 -30015970 -48366352 -41419300
13 b'\x9d\xff4\xff\xde\xff\xeb\xff;\xff6' -59900930 -39060186 -32703053 -77857656 -39912511
14 b'\xee\x035\x03\xb7\x02\n\x04\x82\x03\x85\x03P\x03\xb9\x03\x14\x04\xc4\x03;\x03\x95\x03e\x03\xd4\x04A\x05\x97\x04' 77726865 79168689 71238754 41616144 61866755
15 b'\x86\xf9]\xfa\xbc\xfa\xc0\xf9\x19\xf9\xf6\xf8?\xf9\xef\xf9$\xfbD\xfb\xbf\xfb\x9f\xfc\x9b\xfdW\xfe\x9a\xfe\x9e' 1061
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, struct, numpy as np
ana=pickle.load(open(os.environ["TMPDIR"]+"/ana.pkl","rb"))
b=ana["data/010609/010609_1.plxAnaAD.dat"]
x=np.frombuffer(b[:len(b)//2*2],dtype="<i2")
# find candidate block headers: typ=5, nw=1 at +5 words, nwords in 1..10000 at +6 words, ch in 0..63 at +4
idx=np.flatnonzero((x[:-8]==5)&(x[5:-3]==1)&(x[6:-2]>0)&(x[6:-2]<=10000)&(x[4:-4]>=0)&(x[4:-4]<64))
print(len(idx), idx[:10]*2)
off=idx[0]*2
from collections import Counter
cnt=Counter(); data={}
while off+16<=len(b):
    typ,up,ts,ch,unit,nw,nwords=struct.unpack_from("<hHIhhhh",b,off)
    if typ!=5: print("stop at",off,typ,ch,nw,nwords); break
    off+=16
    data.setdefault(ch,[]).append((((up<<32)+ts)/40000, np.frombuffer(b,dtype="<i2",count=nwords,offset=off)))
    off+=2*nw*nwords
print("end",off,len(b))
for ch,v in sorted(data.items()):
    xx=np.concatenate([a for _,a in v]).astype(float)
    print(ch, len(xx), "blocks",len(v), "t0",v[0][0], xx.min(), xx.max(), xx.mean().round(1), xx.std().round(1), "diff sd", np.diff(xx).std().round(2))
pickle.dump({ch:(np.array([t for t,_ in v]), [a for _,a in v]) for ch,v in data.items()}, open(os.environ["TMPDIR"]+"/ad1.pkl","wb"))
EOF
```

```
Exit code 1
0 []
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
IndexError: index 0 is out of bounds for axis 0 with size 0
```

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, struct, numpy as np
ana=pickle.load(open(os.environ["TMPDIR"]+"/ana.pkl","rb"))
b=ana["data/010609/010609_1.plxAnaAD.dat"]
x=np.frombuffer(b[:len(b)//2*2],dtype="<i2")
nz=np.flatnonzero(x!=0); print("first nonzero words", nz[:40])
print(x[3750:3800])
# look at runs: compute rolling smoothness per 10000-word segment
seg=10000
for s in range(0, len(x), 400000):
    y=x[s:s+seg].astype(float); print(s, y.min(), y.max(), round(y.std(),1), round(np.diff(y).std(),1))
EOF
```

```
first nonzero words [   0    1    2   68   70   72   74   76   78   80   82   84   86   88
   90   98   99  100  101  102  103  104  105  106  107  108  109  138
  140 1438 1440 2730 3242 3244 3246 3328 3329 3330 3331 3332]
[    0     0 12156    68 28173     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0     0     0     0     0
     0     0     0     0     0     0     0     0     0     0     0     0
     0     0]
0 -25536.0 31560.0 1171.5 1316.8
400000 -2048.0 2047.0 859.5 238.1
800000 -2048.0 2047.0 1969.1 753.7
1200000 -2048.0 2047.0 1977.9 792.2
1600000 -2048.0 2047.0 1823.3 557.2
2000000 -2048.0 2047.0 1525.4 402.5
2400000 -2048.0 2047.0 1536.3 419.1
2800000 -2048.0 2047.0 1330.3 135.9
3200000 -2048.0 2047.0 1249.3 138.3
3600000 -2048.0 796.0 690.5 63.9
4000000 -2048.0 2047.0 1096.2 35.2
4400000 -2048.0 2047.0 988.1 40.3
```

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, numpy as np
ana=pickle.load(open(os.environ["TMPDIR"]+"/ana.pkl","rb"))
b=ana["data/010609/010609_1.plxAnaAD.dat"]
x=np.frombuffer(b[:len(b)//2*2],dtype="<i2")
nz=np.flatnonzero(x[3755:]!=0)[:5]+3755; print(nz, len(x)-nz[0], len(x)-7*638372, (len(x)-7*638372-3755))
s=len(x)-7*638372
X=x[s:].reshape(7,638372).astype(float)
for c in range(7): print(c, X[c].min(), X[c].max(), X[c].mean().round(1), X[c].std().round(1), np.diff(X[c]).std().round(2), np.mean(np.abs(X[c])>=2047).round(3))
print(x[s-20:s+20])
EOF
```

```
[4358 4359 4360 4361 4362] 4554457 90211 86456
0 -2048.0 2047.0 30.0 1099.0 355.64 0.142
1 -2048.0 2047.0 31.9 1940.0 699.08 0.848
2 -2048.0 2047.0 32.5 1781.4 548.03 0.653
3 -2048.0 2047.0 -209.7 1534.1 342.95 0.423
4 -2048.0 2047.0 -1637.8 997.9 85.82 0.831
5 -2048.0 2047.0 -460.7 1152.0 97.8 0.255
6 -32764.0 32766.0 -424.1 4220.9 5769.79 0.263
[-1028  -940 -1283 -1140 -1070 -1070 -1018  -938  -915  -998  -912  -805
  -518  -258    31   144   140   239   252   315   711   962  1097  1161
  1284  1189  1373  1645  1489  1277  1397  1244  1014   913  1199  1468
  1560  1376  1056  1316]
```

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, numpy as np
ana=pickle.load(open(os.environ["TMPDIR"]+"/ana.pkl","rb"))
b=ana["data/010609/010609_1.plxAnaAD.dat"]
x=np.frombuffer(b[:len(b)//2*2],dtype="<i2")
print(x[4330:4400])
print(len(b)%2, len(b))
EOF
```

```
[     0      0      0      0      0      0      0      0      0      0
      0      0      0      0      0      0      0      0      0      0
      0      0      0      0      0      0      0      0 -16988      9
  31560     19  14572     29  -2416     38  -2416     38  -2416     38
  -2416     38  -2416     38  -2416     38  -2416     38 -19404     48
  29144     58  12156     68  12156     68  12156     68      0      0
      0      0      0      0      0      0      0      0      0      0]
0 9117630
```

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, io, numpy as np, scipy.io as sio, pandas as pd
ana=pickle.load(open(os.environ["TMPDIR"]+"/ana.pkl","rb"))
D=pickle.load(open(os.environ["TMPDIR"]+"/D.pkl","rb"))
for sess in ["010609_1","010809_2","010809_3"]:
    k=f"data/{sess[:6]}/{sess}.plxAnaAD"
    m=sio.loadmat(io.BytesIO(ana[k+".mat"]),squeeze_me=True)
    n=m["baseANACounts"][301]; nch=m["numADChannels"]
    b=ana[k+".dat"]; x=np.frombuffer(b,dtype="<i2")
    X=x[len(x)-nch*n:].reshape(nch,n).astype(float)
    t0=m["beginOfData"]/m["ADFrequency"]
    tt=D["sessions"][f"data/{sess[:6]}/{sess}.mat"]["trials"]
    c=tt[tt.completed & tt.target.notna()].copy()
    for ch in range(nch):
        vals=[]
        for t12 in c.t12:
            i0=int(round((t12-0.8-t0)*1000)); i1=int(round((t12-t0)*1000))
            vals.append(X[ch,i0:i1].mean() if 0<=i0 and i1<=n else np.nan)
        c[f"ad{ch}"]=vals
    print(sess, "n trials", len(c), "t0", t0, "dur", n/1000, "last t12", c.t12.max())
    cols=[f"ad{i}" for i in range(nch)]
    print(c[cols+["x","y","z"]].corr().loc[cols,["x","y","z"]].round(2).to_string())
    print(c.groupby("target")[cols].mean().round(0).to_string())
    print("within-target SD:", c.groupby("target")[cols].std().mean().round(0).to_dict())
EOF
```

```
010609_1 n trials 80 t0 0.2846 dur 638.372 last t12 632.134175
        x     y     z
ad0 -0.11  0.08  0.07
ad1  0.22  0.05  0.12
ad2  0.25  0.08  0.16
ad3  0.03 -0.06  0.03
ad4 -0.15 -0.15 -0.04
ad5 -0.12 -0.13 -0.17
ad6 -0.20 -0.03 -0.17
          ad0    ad1    ad2    ad3     ad4    ad5     ad6
target                                                   
44       79.0   21.0  -35.0 -210.0 -1286.0 -177.0   154.0
45      -46.0  -39.0  -22.0  -51.0 -1692.0 -308.0    -7.0
46       66.0  168.0  113.0  -81.0 -1666.0 -658.0 -1249.0
54      -16.0  -36.0  -57.0 -157.0 -1380.0 -355.0  -504.0
56      -17.0   34.0    7.0 -168.0 -1944.0 -725.0 -1008.0
64      137.0  -20.0  -54.0 -248.0 -1774.0 -554.0  -468.0
65       23.0  -22.0   64.0 -171.0 -1982.0 -743.0    38.0
66       37.0  296.0  188.0 -203.0 -1724.0 -514.0  -992.0
within-target SD: {'ad0': 181.0, 'ad1': 336.0, 'ad2': 251.0, 'ad3': 637.0, 'ad4': 699.0, 'ad5': 780.0, 'ad6': 1531.0}
[... 40 more lines not kept]
```

**Agent**

No analog channel follows hand position under the most plausible layout (all |r| < 0.26). Now checking session dates against the paper's submission date.

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, numpy as np, pandas as pd
import ppc
D=pickle.load(open(os.environ["TMPDIR"]+"/D.pkl","rb"))
kept, sel = ppc.select_sessions(D["sessions"])
sel["folder"]=sel.session.str.split("/").str[1]
sel["date"]=pd.to_datetime(sel.folder, format="%m%d%y")
sel["kept"]=sel.status.str.startswith("kept")
sel["ym"]=sel.date.dt.to_period("Q")
print(pd.crosstab(sel.ym, sel.kept).to_string())
k=sel[sel.kept]
print("kept before 2012-03-14:", (k.date<"2012-03-14").sum(), " after:", (k.date>="2012-03-14").sum())
print("units kept before:", k[k.date<"2012-03-14"].n_units.sum())
print("folders kept before:", k[k.date<"2012-03-14"].folder.nunique())
# record length by date
nrec={s:D["sessions"][s]["trials"].nrec.max() for s in k.session}
k=k.assign(nrec=k.session.map(nrec))
print(pd.crosstab(k.ym,k.nrec).to_string())
EOF
```

```
kept    False  True 
ym                  
2008Q2      9      0
2008Q4     11     46
2009Q1     21    163
2009Q2      8     57
2009Q3      6     73
2009Q4      1     20
kept before 2012-03-14: 359  after: 0
units kept before: 485
folders kept before: 92
nrec    22  24
ym            
2008Q4  46   0
2009Q1  89  74
2009Q2   0  57
2009Q3   0  73
2009Q4   0  20
```

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, numpy as np, pandas as pd
import ppc
D=pickle.load(open(os.environ["TMPDIR"]+"/D.pkl","rb"))
kept, sel = ppc.select_sessions(D["sessions"])
rows=[]
for k,t in kept.items():
    us=D["sessions"][k]["units"]
    for u in us:
        cnt=ppc.unit_counts(t, us[u], ppc.WINDOWS["hold"])/0.8
        a=ppc.cell_array(t,cnt)
        rows.append(dict(session=k, folder=k.split("/")[1], sn=int(k.split("_")[-1].split(".")[0]) if "_" in k else -1, unit=u, tun=a.mean(axis=(0,2)), rate=a.mean()))
U=pd.DataFrame(rows)
print(U.unit.value_counts().head(10))
first=U.groupby("session").head(1).sort_values(["folder","sn"]).reset_index(drop=True)
def sim(a,b): return np.corrcoef(a,b)[0,1]
same=[];diff=[]; rr_same=[]; rr_diff=[]
rng=np.random.default_rng(0)
for f,g in first.groupby("folder"):
    g=g.reset_index(drop=True)
    for i in range(len(g)-1):
        same.append(sim(g.tun[i],g.tun[i+1])); rr_same.append(abs(np.log((g.rate[i]+.1)/(g.rate[i+1]+.1))))
for _ in range(2000):
    i,j=rng.choice(len(first),2,replace=False)
    if first.folder[i]==first.folder[j]: continue
    diff.append(sim(first.tun[i],first.tun[j])); rr_diff.append(abs(np.log((first.rate[i]+.1)/(first.rate[j]+.1))))
print("consecutive same day: n",len(same),"median tuning r",np.nanmedian(same).round(2),"median |log rate ratio|",np.median(rr_same).round(2))
print("different days: n",len(diff),"median tuning r",np.nanmedian(diff).round(2),"median |log rate ratio|",np.median(rr_diff).round(2))
print("fraction r>0.8: same", np.mean(np.array(same)>0.8).round(2), "diff", np.mean(np.array(diff)>0.8).round(2))
print("same unit name consecutive:", )
# also: channel names per session
print(first.unit.value_counts().head())
print(first.groupby("folder").size().describe())
EOF
```

```
unit
chan1a    359
chan1b    103
chan1c     21
chan1d      1
chan2a      1
Name: count, dtype: int64
consecutive same day: n 267 median tuning r 0.04 median |log rate ratio| 0.8
different days: n 1979 median tuning r -0.04 median |log rate ratio| 0.98
fraction r>0.8: same 0.03 diff 0.02
same unit name consecutive:
unit
chan1a    359
Name: count, dtype: int64
count    92.000000
mean      3.902174
std       2.431749
min       1.000000
25%       2.000000
50%       4.000000
[... 3 more lines not kept]
```

**Agent**

Same-day consecutive sessions have unrelated tuning (median r 0.04 vs −0.04 across days), so they are distinct neurons. Now geometry by date, to look for a block that could be monkey B.

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, numpy as np, pandas as pd
import ppc
D=pickle.load(open(os.environ["TMPDIR"]+"/D.pkl","rb"))
kept, sel = ppc.select_sessions(D["sessions"])
rows=[]
for k,t in kept.items():
    m=t.groupby("target")[["x","y","z"]].mean()
    rows.append(dict(session=k, date=pd.to_datetime(k.split("/")[1],format="%m%d%y"),
        dx=(m.loc[[56,66,46],"x"].mean()-m.loc[[54,64,44],"x"].mean())/2,
        dy=(m.loc[[64,65,66],"y"].mean()-m.loc[[44,45,46],"y"].mean())/2,
        ymid=m.loc[[54,56],"y"].mean(), z=m.z.mean(), xc=m.loc[[45,65],"x"].mean(),
        nrec=D["sessions"][k]["trials"].nrec.max(), f1=t.params.iloc[0][1], f11=t.params.iloc[0][11]))
G=pd.DataFrame(rows)
G["month"]=G.date.dt.to_period("M")
print(G.groupby("month")[["dx","dy","ymid","z","xc"]].agg(["mean"]).round(2).assign(n=G.groupby("month").size()).to_string())
print(G[["dx","dy","ymid","z","xc"]].describe().round(2).to_string())
print(pd.crosstab(G.month,G.f1).to_string())
print(pd.crosstab(G.month,G.f11).to_string())
EOF
```

```
<stdin>:15: Pandas4Warning: Setting a new column on a DataFrame with a MultiIndex using a key that is not a full-length tuple is deprecated and will raise in a future version. DataFrame.assign cannot take a tuple key; use df[('n', '')] = ... instead.
           dx    dy  ymid      z    xc   n
         mean  mean  mean   mean  mean    
month                                     
2008-10  4.41  3.48 -4.23   9.71  0.06  10
2008-11  4.70  3.72 -4.57  10.30  0.40   2
2008-12  4.31  4.09 -3.91   9.99 -0.15  34
2009-01  4.38  3.69 -4.27  10.05  0.07  73
2009-02  4.52  3.65 -4.84   9.93 -0.05  16
2009-03  4.55  3.54 -3.99   9.83  0.08  74
2009-04  4.76  3.64 -3.86  10.02  0.09  39
2009-05  4.85  3.68 -3.91  10.24 -0.01  18
2009-07  4.72  3.86 -4.05  10.03  0.12  25
2009-08  4.70  3.57 -3.98  10.36  0.09  40
2009-09  5.05  3.88 -4.16   9.99  0.14   8
2009-10  5.11  3.64 -4.23  10.22 -0.18  19
2009-11  4.89  3.88 -4.22   9.94 -0.28   1
           dx      dy    ymid       z      xc
count  359.00  359.00  359.00  359.00  359.00
mean     4.60    3.68   -4.09   10.03    0.04
[... 36 more lines not kept]
```

**Agent**

Geometry is uniform across all 13 months (one animal, monkey X's layout), so there is no monkey B block. Next: endpoint SDs within sessions, trial ordering, and hold timing.

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, numpy as np, pandas as pd
import ppc
D=pickle.load(open(os.environ["TMPDIR"]+"/D.pkl","rb"))
kept, sel = ppc.select_sessions(D["sessions"])
K=pd.concat([t.assign(session=k) for k,t in kept.items()])
w=K.groupby(["session","target","cond"])[["x","y","z"]].std()
print("within-session trial SD per target and cond (cm): median", w.median().round(3).to_dict(), "IQR", w.quantile([.25,.75]).round(3).values.tolist())
# ordering
rows=[]
for k,t in kept.items():
    allc=D["sessions"][k]["trials"]; c=allc[allc.completed & allc.cond.isin([4,7])].sort_values("t0")
    seq=c.cond.values
    runs=1+np.sum(seq[1:]!=seq[:-1]); n1=(seq==4).sum(); n2=(seq==7).sum(); n=n1+n2
    exp=1+2*n1*n2/n
    # position in session of V vs NV
    rank=np.arange(n)/n
    rows.append(dict(session=k, n=n, runs=runs, exp_runs=exp, mean_rank_V=rank[seq==4].mean(), first=seq[0], seq=''.join('V' if s==4 else 'N' for s in seq[:40])))
O=pd.DataFrame(rows)
print(O[["n","runs","exp_runs","mean_rank_V"]].describe().round(2).to_string())
print((O.runs<=3).sum(),"sessions with 3 or fewer runs")
for s in O.seq.head(6): print(s)
# time trend: within session, correlation of position with trial order vs condition
EOF
```

```
within-session trial SD per target and cond (cm): median {'x': 0.294, 'y': 0.288, 'z': 0.19} IQR [[0.213, 0.207, 0.139], [0.387, 0.381, 0.252]]
            n    runs  exp_runs  mean_rank_V
count  359.00  359.00    359.00       359.00
mean    80.19   41.84     41.10         0.49
std      2.51   10.32      1.24         0.06
min     80.00   23.00     41.00         0.32
25%     80.00   35.00     41.00         0.45
50%     80.00   39.00     41.00         0.49
75%     80.00   45.00     41.00         0.52
max    122.00   74.00     61.85         0.65
0 sessions with 3 or fewer runs
NNNNNVVNNNVVVNVVVVNVNNNNNVVNVVVVNVNVNNVN
NVNVVVNVNNVNNNVNNVNVVNVNVNNNVNVVVVVNNNVN
VVNNVNNVNVVNNVNNVNVNVNVVNNVVNVVVVVVNNVVV
NVNNVVNNVVNNNNNNVVVVVVVNNNVVVNVVVVNNVVVN
VVVNNVVNVNVNNNNVVNNVNNVVVNNVNNVNNVVNVVNV
NVVVVNNNVVNVVVNVVNVVNNVNNNNNVVNVNNVVNVNN
```

**Agent calls Bash**

```bash
cd entries/shi-2013; PYTHONPATH=. $TMPDIR/venv/bin/python - <<'EOF'
import pickle, os, numpy as np, pandas as pd
import ppc
D=pickle.load(open(os.environ["TMPDIR"]+"/D.pkl","rb"))
kept, sel = ppc.select_sessions(D["sessions"])
K=pd.concat([t.assign(session=k) for k,t in kept.items()])
K["f11"]=K.params.apply(lambda p:p[11])
K["d_t_10"]=K.t10-K.t_target; K["d10_12"]=K.t12-K.t10; K["d12_13"]=K.t13-K.t12
for c in ["d_t_10","d10_12","d12_13"]:
    print(c, K[c].quantile([0,.01,.05,.25,.5,.75,.95,.99,1]).round(3).to_dict())
print(K.groupby("f11").d10_12.describe().round(3).to_string())
print(K.groupby(["f11","cond"]).d10_12.median().round(3).to_string())
print("fraction with t12-0.8 within 0.25 s of t10:", np.mean(K.d10_12<1.05).round(3), " within 0.3 s:", np.mean(K.d10_12<1.1).round(3))
# per trial, d10_12 minus f11
K["slack"]=K.d10_12-K.f11/1000
print("d10_12 - f11:", K.slack.quantile([0,.01,.05,.5,.95,1]).round(3).to_dict())
# full trial event sequence for one trial
s=D["sessions"][list(kept)[0]]["strobed"]
c=s[:,1].astype(int); i=np.flatnonzero(c==0)[3]; j=np.flatnonzero(c==255); j=j[j>i][0]
print([(int(cc), round(tt-s[i,0],3)) for tt,cc in s[i:j+1]])
EOF
```

```
d_t_10 {0.0: 0.224, 0.01: 0.304, 0.05: 0.304, 0.25: 0.32, 0.5: 0.32, 0.75: 0.32, 0.95: 0.32, 0.99: 0.32, 1.0: 0.416}
d10_12 {0.0: 0.832, 0.01: 0.928, 0.05: 0.96, 0.25: 1.12, 0.5: 1.184, 0.75: 1.248, 0.95: 1.376, 0.99: 1.472, 1.0: 1.856}
d12_13 {0.0: 0.016, 0.01: 0.016, 0.05: 0.016, 0.25: 0.032, 0.5: 0.032, 0.75: 0.032, 0.95: 0.032, 0.99: 0.032, 1.0: 0.032}
          count   mean    std    min    25%    50%    75%    max
f11                                                             
800.0     146.0  1.022  0.094  0.832  0.960  1.024  1.088  1.248
900.0   25124.0  1.177  0.109  0.928  1.136  1.184  1.248  1.792
1000.0   3290.0  1.256  0.151  1.056  1.056  1.312  1.376  1.856
1100.0    160.0  1.152  0.000  1.152  1.152  1.152  1.152  1.152
f11     cond
800.0   4.0     1.024
        7.0     1.024
900.0   4.0     1.184
        7.0     1.184
1000.0  4.0     1.312
        7.0     1.312
1100.0  4.0     1.152
        7.0     1.152
fraction with t12-0.8 within 0.25 s of t10: 0.116  within 0.3 s: 0.21
d10_12 - f11: {0.0: 0.028, 0.01: 0.028, 0.05: 0.056, 0.5: 0.284, 0.95: 0.44, 1.0: 0.892}
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "id:" claims/shi-2013.yaml | head -40; awk '/id: fig5-fano-factor/,/id: cv2-larger-nv/' claims/shi-2013.yaml
```

```
55:- id: behavior-mean-position-sessions
76:- id: behavior-variability-sessions
103:- id: table1-endpoint-means
504:- id: table1-endpoint-sd
899:- id: fig3-example-neuron
932:- id: movement-epoch-tuning
949:- id: hold-position-main-effect
967:- id: hold-vision-main-effect
982:- id: hold-interaction
997:- id: hold-subepochs
1034:- id: hold-overall-effects
1060:- id: correlation-endpoint-datasets
1087:- id: fig4-indx1-negative
1141:- id: fig4-indx1-means
1162:- id: indx1-tuning-shift
1189:- id: indx2-means
1215:- id: rate-variance-nv-higher
1236:- id: fig5-fano-factor
1264:- id: cv2-larger-nv
1281:- id: fig6-decoding-vv
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -E "Fig\. 5|FF|Fano|outlier" paper/10.1152-jn.00223.2012.txt | head -30
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 245,280p paper/10.1152-jn.00223.2012.txt; sed -n 495,512p paper/10.1152-jn.00223.2012.txt; sed -n 895,910p paper/10.1152-jn.00223.2012.txt; sed -n 955,990p paper/10.1152-jn.00223.2012.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -n 1141,1236p claims/shi-2013.yaml
```

```
- id: fig4-indx1-means
  statement: Mean INDX1 was least negative for Position Only cells (-13%) and most negative for
    Position/Vision cells (-31%).
  source: Results, Neurophysiology, paragraph 4; Figure 4B, C
  quote: the mean INDX1 was least negative ... In contrast, the average index was most negative in
    the population of cells showing both positional and visual modulation by the ANOVA
  expected:
  - quantity: mean INDX1, Position Only cells
    value: -13
    tolerance: 1.3
    unit: "%"
  - quantity: mean INDX1, Position/Vision cells
    value: -31
    tolerance: 3.1
    unit: "%"
  depends_on:
  - fig4-indx1-negative
  criterion: INDX1 and groups as in fig4-indx1-negative, after outlier removal under each of its
    readings. Reproduced when both means are within tolerance under a reading and the
    Position/Vision mean is the most negative and the Position Only mean the least negative of
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/shi-2013 && python - <<'EOF'
import json
nb=json.load(open('reproduce_shi_2013.ipynb'))
for i in [1,3,9,10,11,12,13,14,16,17,19,20,22,24]:
    print(f"=== [{i}] {nb['cells'][i].get('metadata',{}).get('tags')}"); print(''.join(nb['cells'][i]['source']))
EOF
```

```
=== [1] None
import time
import warnings
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yaml
from scipy import stats

import ppc

warnings.filterwarnings("ignore", category=RuntimeWarning)
pd.set_option("display.width", 220)
pd.set_option("display.max_columns", 40)
pd.set_option("display.max_rows", 200)
CLAIMS = {c["id"]: c for c in yaml.safe_load(Path("../../claims/shi-2013.yaml").read_text())["claims"]}
def expected(cid):
    return [(e["quantity"], e["value"], e.get("tolerance")) for e in CLAIMS[cid].get("expected", [])]
[... 217 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('reproduce_shi_2013.ipynb'))
for i in [56,70,76,83,88,89,92,95,97]:
    print(f"=== [{i}] {nb['cells'][i].get('metadata',{}).get('tags')}"); print(''.join(nb['cells'][i]['source']))
EOF
```

```
=== [56] ['claim:fig4-indx1-negative']
def indexes(M):
    out = []
    for _, r in M.iterrows():
        m = r.hold.mean(axis=2)
        pnv, pv = int(np.argmax(m[1])), int(np.argmax(m[0]))
        nv = m[1, pnv]
        out.append(dict(pnv=pnv, pv=pv,
                        indx1=np.nan if nv == 0 else (m[0, pnv] - nv) / nv * 100,
                        indx2=np.nan if nv == 0 else (m[0, pv] - nv) / nv * 100))
    return pd.DataFrame(out, index=M.index)
def fences(x):
    q1, q3 = np.nanpercentile(x, [25, 75])
    return q1 - 1.5 * (q3 - q1), q3 + 1.5 * (q3 - q1), q3 - q1
def outliers(M, col, reading):
    x = M[col]
    g = groups(M)
    if reading == "a":
        lo, hi, _ = fences(x)
        return (x < lo) | (x > hi)
[... 257 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
from pathlib import Path
p=Path("ppc.py"); s=p.read_text()
old='''    c, t, n = train.shape
    conf = np.zeros((t, t), int)
    same = train is test
    for k in range(n):
        if not loo:
            lam = train.mean(axis=2)
        elif same:
            lam = (train.sum(axis=2) - train[:, :, k]) / (n - 1)
        else:
            lam = np.delete(train, k, axis=2).mean(axis=2)'''
new='''    c, t, n = train.shape
    conf = np.zeros((t, t), int)
    for k in range(n):
        if loo:
            lam = np.delete(train, k, axis=2).mean(axis=2)
        else:
            lam = train.mean(axis=2)'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    model lambda[cell, target] is the mean of the other four training trials
    (when train and test are the same data) and the test trial''','''    model lambda[cell, target] is the mean of the other four training trials
    (trial k is left out of training whether or not train and test are the
    same condition) and the test trial''')
old='''def load_all(url=URL, check_plx="data/010609/010609_1"):
    """One pass over the tar: every session file, reduced to its trial table
    and spike times; the member list; and, for one session, the .plx file's
    events and spikes to check the .mat extraction against."""
    import struct
    tf = open_stream(url)
    members, sessions, errors, plx = [], {}, {}, None
    for m in tf:
        members.append((m.name, m.size))
        if not m.isfile():
            continue
        if check_plx and m.name == check_plx + ".plx":'''
new='''ANA_CHECK = ("data/010609/010609_1", "data/010609/010609_2", "data/010809/010809_2")


def load_all(url=URL, check_plx="data/010609/010609_1", ana_check=ANA_CHECK):
    """One pass over the tar: every session file, reduced to its trial table
    and spike times; the member list; for one session, the .plx file's
    events and spikes to check the .mat extraction against; and, for the
    sessions in ``ana_check``, the analog files (``read_anaad``)."""
    tf = open_stream(url)
    members, sessions, errors, plx, ana = [], {}, {}, None, {}
    for m in tf:
        members.append((m.name, m.size))
        if not m.isfile():
            continue
        stem = m.name.split(".plxAnaAD")[0]
        if ".plxAnaAD." in m.name and stem in ana_check:
            ana.setdefault(stem, {})[m.name.rsplit(".", 1)[1]] = tf.extractfile(m).read()
            if len(ana[stem]) == 2:
                ana[stem] = read_anaad(ana[stem]["mat"], ana[stem]["dat"])
            continue
        if check_plx and m.name == check_plx + ".plx":'''
assert old in s; s=s.replace(old,new)
old='''    return dict(members=members, sessions=sessions, errors=errors, plx=plx)'''
new='''    return dict(members=members, sessions=sessions, errors=errors, plx=plx, ana=ana)


def read_anaad(mat_bytes, dat_bytes):
    """Analog channels of one session from its ``.plxAnaAD.mat`` (sampling
    rates, counts) and ``.plxAnaAD.dat`` (samples).

    The descriptor lists the .mat variables but not the .dat layout. Read
    from the files: the .dat starts with a Plexon file header ("PLEX") and
    per-channel counts, and ends with ``numADChannels`` x ``baseANACounts``
    16-bit samples; the samples are taken as the last n x channels words,
    one channel after another, the first sample at ``beginOfData /
    ADFrequency`` s and then at the channel's ``adfreq``. This layout is a
    reading of the files, not documented. Returns dict(t0, fs, X[channel,
    sample], gains)."""
    d = sio.loadmat(io.BytesIO(mat_bytes), squeeze_me=True)
    nch = int(d["numADChannels"])
    counts = np.asarray(d["baseANACounts"])
    n = int(counts[counts > 0][0])
    x = np.frombuffer(dat_bytes[: len(dat_bytes) // 2 * 2], dtype="<i2")
    X = x[len(x) - nch * n:].reshape(nch, n)
    fs = float(np.atleast_1d(d["adfreq"])[0])
    gains = np.asarray(d["slowChannelGains"])
    return dict(t0=float(d["beginOfData"]) / float(d["ADFrequency"]), fs=fs, X=X,
                gains=gains[gains > 0], n_samples=n, n_channels=nch)


def late_windows(trials, delay=0.25):
    """Variant hold windows that start no earlier than ``delay`` s after
    event 10 (target offset, the cue to saccade to the centre): the hold
    window [max(t12 - 0.8, t10 + delay), t12], its first part [that start,
    t12 - 0.4] and the last 400 ms [t12 - 0.4, t12]. ``delay`` is a choice
    for this sensitivity check (a typical saccadic latency), not from the
    paper. Returns (start, mid, end) arrays relative to nothing (absolute
    times)."""
    end = trials.t12.values
    start = np.maximum(end - 0.8, trials.t10.values + delay)
    mid = end - 0.4
    return start, np.maximum(mid, start), end'''
assert old in s; s=s.replace(old,new)
s=s.replace('''def read_plx_events_spikes(b):''','''def read_plx_events_spikes(b):''')
s=s.replace('''    import struct
    adfreq, = struct.unpack_from("<i", b, 136)''','''    import struct
    adfreq, = struct.unpack_from("<i", b, 136)''')
old='''# Windows, relative to event 12 (end of the static holding period), seconds.'''
new='''# Windows, relative to event 12 (end of the static holding period), seconds.
# On every completed trial the time from event 10 to event 12 is at least the
# trial's record field 11 (800 to 1,100 ms) plus 28 ms (see the notebook), so
# field 11 is read as the minimum hold, timed from about event 10, and the 800
# ms before event 12 lie inside it.'''
assert old in s; s=s.replace(old,new)
p.write_text(s)
EOF
grep -n "import struct" ppc.py
```

```
257:    import struct
```

**Agent calls Bash**

```bash
python - <<'EOF'
from pathlib import Path
p=Path("ppc.py"); s=p.read_text()
s=s.replace("""    paper. Returns (start, mid, end) arrays relative to nothing (absolute
    times).\"\"\"""","""    paper. Returns the (start, mid, end) times of each trial, in s.\"\"\"""")
p.write_text(s)
EOF
grep -n "Returns the (start" ppc.py
```

```
244:    paper. Returns the (start, mid, end) times of each trial, in s."""
```

**Agent**

Now a dev harness that runs the notebook's code cells against the cached data, so I can test new cells without re-streaming.

**Agent calls Bash**

```bash
cat > $TMPDIR/dev.py <<'EOF'
import json, pickle, os, sys, io, matplotlib
matplotlib.use("Agg")
import ppc
T=os.environ["TMPDIR"]
def load_D():
    D=pickle.load(open(T+"/D.pkl","rb"))
    for k,s in D["sessions"].items():
        s["strobed_head"]=s["strobed"][:2000]; s["n_strobes"]=len(s["strobed"])
    ana=pickle.load(open(T+"/ana.pkl","rb"))
    D["ana"]={st: ppc.read_anaad(ana[st+".plxAnaAD.mat"], ana[st+".plxAnaAD.dat"]) for st in ppc.ANA_CHECK}
    D["plx"]=None
    return D
def run(upto=None, cells=None, ns=None, skip=(3,5,7)):
    nb=json.load(open("reproduce_shi_2013.ipynb"))
    ns = ns if ns is not None else {}
    if "D" not in ns:
        ns["D"]=load_D()
    idx = cells if cells is not None else range(upto)
    for i in idx:
        c=nb["cells"][i]
        if c["cell_type"]!="code" or i in skip: continue
        print(f"##### cell {i}", flush=True)
        exec(compile("".join(c["source"]), f"cell{i}", "exec"), ns)
    return ns
EOF
cat > $TMPDIR/dev_base.py <<'EOF'
import sys, os, pickle, time; sys.path.insert(0, os.environ["TMPDIR"]); sys.path.insert(0, ".")
import dev
t=time.time()
ns=dev.run(upto=23)
print("time", time.time()-t)
keep={k:ns[k] for k in ["kept","sel","M1","MA","allt","a","UNITS_ALL"]}
pickle.dump(keep, open(os.environ["TMPDIR"]+"/ns.pkl","wb"))
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/dev_base.py 2>&1 | tail -30
```

```
cond                      4.0    7.0
phase                               
aborted after code 10    4423   5688
aborted before code 10   6006   6040
completed               15473  15315
chi-square, aborts after code 10 against completed, by code: (np.float64(128.94788771406652), np.float64(6.962253719773221e-30))
sessions with more aborts after code 10 on code 7 / on code 4 / equal: 210 165 28
binomial test over sessions: 0.02295027298522436
##### cell 19
 window end relative to code 12 (s)  fraction of units with a target effect
                               -6.0                                   0.035
                               -4.0                                   0.023
                               -3.0                                   0.039
                               -2.5                                   0.045
                               -2.0                                   0.049
                               -1.5                                   0.359
                               -1.0                                   0.602
                               -0.5                                   0.482
                                0.0                                   0.361
                                0.5                                   0.336
[... 10 more lines not kept]
```

**Agent**

Setup runs in 12 s on the cache. Writing the new cells now.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/newcells; cd $TMPDIR/newcells
cat > timing.py <<'EOF'
c10 = allt[allt.completed & allt.params.notna()].copy()
c10["field11_s"] = c10.params.apply(lambda p: p[11]) / 1000
c10["d10_12"] = c10.t12 - c10.t10
c10["excess"] = c10.d10_12 - c10.field11_s
c10["kept"] = c10.session.isin(kept)
print("completed trials with a record: code 10 to code 12 interval against the trial's own field 11 (s):")
print(c10.groupby("field11_s").agg(trials=("d10_12", "size"), min_10_to_12=("d10_12", "min"),
                                   median_10_to_12=("d10_12", "median"), max_10_to_12=("d10_12", "max"),
                                   min_excess=("excess", "min")).round(3).to_string())
print("trials where code 10 to code 12 is shorter than field 11:", int((c10.excess < 0).sum()), "of", len(c10))
print("excess of code 10 to code 12 over field 11 (s), quantiles:",
      c10.excess.quantile([0, 0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 1]).round(3).to_dict())
for lim in (0.25, 0.30):
    for lab, sub in (("all", c10), ("kept sessions", c10[c10.kept])):
        print(f"{lab}: trials whose 800 ms window (code 12 - 0.8 s) starts less than {lim} s after code 10: "
              f"{100 * np.mean(sub.d10_12 - 0.8 < lim):.1f}% of {len(sub)}")
EOF
cat > timing.md <<'EOF'
On every completed trial the time from code 10 to code 12 is at least the trial's own record field
11 plus 28 ms (the table above): the shortest intervals, 0.83 s, are on trials with field 11 = 800,
and with 900 and 1,000 the shortest are 0.93 and 1.06 s. Field 11 is therefore read as the
minimum hold, timed from a point at least 28 ms after code 10 (target offset, the cue to saccade
to the centre), and code 12 as its end, so the 800 ms before code 12 lie inside the hold as the
task timed it. A start 28 ms after the cue is too early for a saccade; the fixation window is
6.5 degrees in radius (Methods, Experimental paradigm), so the eyes may already have been inside it.
Where the window starts soon after code 10 it may still include the end of a saccade, and this
bears most on the first 400 ms. The share of such trials is printed above. A variant that starts
the window at least 250 ms after code 10 is run for hold-subepochs and decoding-subepochs.
EOF
cat > clock.py <<'EOF'
rows = []
for k in kept:
    t = kept[k]
    ph, pp = [], []
    for u_, sp in D["sessions"][k]["units"].items():
        for align, lst in (("t12", ph), ("t0", pp)):
            cnt = ppc.unit_counts(t, sp, (-0.8, 0.0), align=align)
            g_ = [cnt[t.target.values == tg] for tg in ppc.TARGETS]
            lst.append(1.0 if np.all(cnt == cnt[0]) else stats.f_oneway(*g_).pvalue)
    rows.append(dict(session=k, n_units=len(ph), p_hold=min(ph), p_pre=min(pp)))
CK = pd.DataFrame(rows)
print("per session, smallest one-way ANOVA P of the target effect over its units:")
print(f"   last 800 ms before code 12: P < 0.05 in {int((CK.p_hold < 0.05).sum())} of {len(CK)} sessions")
print(f"   800 ms before the trial's first event: P < 0.05 in {int((CK.p_pre < 0.05).sum())} of {len(CK)} sessions"
      f" (expected by chance about {0.05 * CK.n_units.sum():.0f} units' worth)")
print("sessions where the clock is not supported by this check (no unit with a hold target effect):",
      int((CK.p_hold >= 0.05).sum()))
EOF
cat > clock.md <<'EOF'
Per session the check has one to four units, so it can support the shared clock only where a unit
is tuned to the target in the hold. It does so in the sessions counted above; in the others (whose
units carry no target effect in the hold) the clock is not established by this check, and they are
kept, as the paper kept untuned cells.
EOF
cat > population.py <<'EOF'
SUBMITTED = pd.Timestamp("2012-03-14")  # paper, header: "Submitted 14 March 2012"
ks_ = sel[sel.status.str.startswith("kept")].copy()
ks_["date"] = pd.to_datetime(ks_.session.str.split("/").str[1], format="%m%d%y")
print("kept sessions by quarter of the recording date (folder name):")
print(ks_.groupby(ks_.date.dt.to_period("Q")).agg(sessions=("session", "size"), units=("n_units", "sum")).to_string())
print("kept sessions recorded on or after 14 March 2012 (paper submitted):", int((ks_.date >= SUBMITTED).sum()),
      "; recording days:", ks_.date.nunique(), "; first", ks_.date.min().date(), "; last", ks_.date.max().date())
gk = geo.merge(ks_[["session", "date"]], on="session")
gm = gk.groupby(gk.date.dt.to_period("M"))
print("target geometry by month of recording, kept sessions (cm, means over sessions):")
print(gm[["x_right_minus_left", "y_top_minus_bottom", "y_middle_row", "z"]].mean().round(2)
      .assign(sessions=gm.size()).to_string())
# Is one neuron recorded in several sessions of a day? Compare the hold tuning (mean rate per
# target, both conditions) of the first unit of consecutive sessions on a day with that of
# sessions on different days.
T_ = pd.DataFrame({"session": M1.session, "tuning": [r.mean(axis=(0, 2)) for r in M1.hold],
                   "rate": [r.mean() for r in M1.hold]})
T_["day"] = T_.session.str.split("/").str[1]
T_["num"] = T_.session.str.extract(r"_(\d+)\.mat$")[0].astype(float)
T_ = T_.sort_values(["day", "num"]).reset_index(drop=True)
def tuning_r(i, j):
    return np.corrcoef(T_.tuning[i], T_.tuning[j])[0, 1]
same_day = [(i, i + 1) for i in range(len(T_) - 1) if T_.day[i] == T_.day[i + 1]]
rng_pop = np.random.default_rng(11)
other = []
while len(other) < 2000:
    i, j = rng_pop.choice(len(T_), 2, replace=False)
    if T_.day[i] != T_.day[j]:
        other.append((i, j))
for lab, pairs in (("consecutive sessions, same day", same_day), ("sessions on different days", other)):
    r_ = np.array([tuning_r(i, j) for i, j in pairs])
    lr = np.array([abs(np.log((T_.rate[i] + 0.1) / (T_.rate[j] + 0.1))) for i, j in pairs])
    print(f"{lab}: {len(pairs)} pairs; tuning correlation median {np.nanmedian(r_):.2f}, above 0.8 in "
          f"{100 * np.nanmean(r_ > 0.8):.1f}%; median |log rate ratio| {np.median(lr):.2f}")
EOF
cat > population.md <<'EOF'
The kept sessions were all recorded between October 2008 and November 2009, before the paper was
submitted, on 92 days, and their target geometry is the same in every month (monkey X's layout
throughout; no block of sessions has monkey B's square layout or depth near 14.5 cm). The paper
gives one neuron per session (Table 1 legend, "means +/- SD over 219 sessions for monkey X"; Results,
Behavior, "both animals (N = 343 sessions)" with 343 neurons). Consecutive sessions on one day do
not look like the same neuron recorded again: their tuning correlates no more than that of
sessions on different days. So the data set holds about 140 more monkey X sessions than the
paper's 219, the descriptor's 124 monkey B cells are not identifiable in it, and which sessions the
paper used is not documented. All 359 are used, one unit from each, as the paper has one neuron
per session; which unit is a choice (the first sorted, "a"), and the 483 sorted units are shown as
a variant throughout.
EOF
ls
```

```
clock.md
clock.py
population.md
population.py
timing.md
timing.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/newcells
cat > endpoint.py <<'EOF'
# Checks of the record's hand position (fields 19 to 21) asked for in verification.
K_ = pd.concat([t.assign(session=k) for k, t in kept.items()])
w_sd = K_.groupby(["session", "target", "cond"])[["x", "y", "z"]].std()
print("SD over a session's five trials at a target and condition (cm), median and IQR over",
      len(w_sd), "session, target and condition cells:")
print(w_sd.quantile([0.25, 0.5, 0.75]).round(3).to_string())
sm_sd = K_.groupby(["session", "target", "cond"])[["x", "y", "z"]].mean().groupby(["target", "cond"]).std()
print("SD over sessions of the session means (cm), range over targets and conditions:",
      {ax: (round(sm_sd[ax].min(), 2), round(sm_sd[ax].max(), 2)) for ax in "xyz"},
      "; Table 1 (monkey X) runs from 0.50 to 1.28")
# Order of conditions within a session: interleaved or in blocks?
rows = []
for k in kept:
    c_ = D["sessions"][k]["trials"]
    c_ = c_[c_.completed & c_.cond.isin([4, 7])].sort_values("t0")
    s_ = c_.cond.values
    n1, n2 = int((s_ == 4).sum()), int((s_ == 7).sum())
    rows.append(dict(session=k, runs=1 + int(np.sum(s_[1:] != s_[:-1])), expected=1 + 2 * n1 * n2 / (n1 + n2)))
RU = pd.DataFrame(rows)
print(f"runs of one condition among a session's completed trials: median {RU.runs.median():.0f} "
      f"(expected under random order {RU.expected.median():.0f}); fewest {RU.runs.min()}, most {RU.runs.max()}")
for k in list(kept)[:3]:
    c_ = D["sessions"][k]["trials"]
    c_ = c_[c_.completed & c_.cond.isin([4, 7])].sort_values("t0")
    print("  ", k, "first 40 completed trials:", "".join("V" if x == ppc.V_CODE else "N" for x in c_.cond.values[:40]))
# The MANOVA on these data with V and NV labels shuffled within each session and target.
rng_beh = np.random.default_rng(21)
p_null = []
for k, t in kept.items():
    for tg in ppc.TARGETS:
        X_ = t[t.target == tg][["x", "y", "z"]].values
        lab_ = rng_beh.permutation(np.r_[np.zeros(5), np.ones(5)])
        p_null.append(ppc.hotelling2(X_[lab_ == 0], X_[lab_ == 1])[1])
print(f"MANOVA with shuffled V/NV labels: {100 * np.nanmean(np.array(p_null) < 0.05):.1f}% of {len(p_null)} pairs significant (nominal 5%)")
dmean = beh.assign(**{f"d{ax}": np.nan for ax in "xyz"})
dd = K_.groupby(["session", "target", "cond"])[["x", "y", "z"]].mean().unstack("cond")
diff_ = pd.DataFrame({ax: dd[(ax, ppc.NV_CODE)] - dd[(ax, ppc.V_CODE)] for ax in "xyz"})
print("NV minus V session mean position (cm), mean and SD over session and target pairs:",
      diff_.mean().round(3).to_dict(), diff_.std().round(3).to_dict())
EOF
cat > endpoint.md <<'EOF'
The conditions are interleaved within each session (the number of runs is that of a random
order), so slow drift cannot make V and NV differ. The MANOVA is calibrated on these data: with
the labels shuffled it rejects at about the nominal 5% (printed above). The 16% is therefore a
property of the positions recorded under the real labels. Whether the record's position is the
mean over the hold, as the paper's Fig. 2 legend describes, or one sample, the data do not say.
Within a session the five trials at a target spread by about 0.2 to 0.4 cm, and the session means
spread by 0.3 to 0.7 cm over sessions, about half of Table 1's SDs. No analog channel follows the
hand (see eye-position-no-difference), so there is no position trace to check the record against.
EOF
cat > analog.py <<'EOF'
# The analog files of three sessions (ppc.read_anaad; layout read from the files, not documented).
for st, A in D["ana"].items():
    k = st + ".mat"
    t = D["sessions"][k]["trials"]
    t = t[t.completed & t.target.isin(ppc.TARGETS)].copy()
    X = A["X"].astype(float)
    print(f"{st}: {A['n_channels']} channels, {A['n_samples']} samples at {A['fs']:.0f} Hz "
          f"({A['n_samples'] / A['fs']:.0f} s; last code 12 at {t.t12.max():.0f} s); gains {A['gains'].tolist()}")
    rows = []
    for ch in range(A["n_channels"]):
        x = X[ch]
        hm = []
        for t12 in t.t12.values:
            i0, i1 = int(round((t12 - 0.8 - A["t0"]) * A["fs"])), int(round((t12 - A["t0"]) * A["fs"]))
            hm.append(x[i0:i1].mean() if i0 >= 0 and i1 <= len(x) else np.nan)
        t[f"ad{ch}"] = hm
        grp = [t[f"ad{ch}"][t.target == tg].dropna() for tg in ppc.TARGETS]
        rows.append(dict(channel=ch, min=x.min(), max=x.max(), sd=round(x.std(), 1),
                         saturated_pct=round(100 * np.mean(np.abs(x) >= 2047), 1),
                         r_x=round(np.corrcoef(t[f"ad{ch}"], t.x)[0, 1], 2), r_y=round(np.corrcoef(t[f"ad{ch}"], t.y)[0, 1], 2),
                         r_z=round(np.corrcoef(t[f"ad{ch}"], t.z)[0, 1], 2),
                         target_anova_p=stats.f_oneway(*grp).pvalue,
                         hold_sd_within_target=round(t.groupby("target")[f"ad{ch}"].std().mean(), 1)))
    print(pd.DataFrame(rows).to_string(index=False))
EOF
cat > analog.md <<'EOF'
Under this reading of the analog files, no channel's hold-period mean correlates with the record's
hand position beyond |r| of about 0.3 (printed above), and the channels saturate often at the 12-bit
limits (+/-2047). None is a clean arm position trace. A fixation trace would be nearly constant
across targets in the hold; with the layout undocumented, a channel cannot be named as eye position
on that alone. This is consistent with no usable eye or arm channel, not a proof of it: another
layout of the .dat file could give other channels.
EOF
cat > late.py <<'EOF'
# Variant (verification round 1): hold windows starting no earlier than 250 ms after code 10
# (ppc.late_windows); rates, as the windows differ in length between trials.
def late_measures(M):
    out = {"hold": [], "first": [], "last": []}
    for r in M.itertuples():
        t = kept[r.session]
        sp = np.sort(D["sessions"][r.session]["units"][r.unit])
        s0, mid, e0 = ppc.late_windows(t)
        for key, (a_, b_) in (("hold", (s0, e0)), ("first", (s0, mid)), ("last", (mid, e0))):
            dur = b_ - a_
            cnt = np.searchsorted(sp, b_) - np.searchsorted(sp, a_)
            out[key].append(ppc.cell_array(t, np.where(dur > 0, cnt / np.where(dur > 0, dur, 1), np.nan)))
    return out
LATE = {lab: late_measures(M) for lab, M in (("main", M1), ("all units", MA))}
s0, mid, e0 = ppc.late_windows(pd.concat(kept.values()))
print(f"first part of the variant window: median {np.median(mid - s0):.3f} s, shortest {np.min(mid - s0):.3f} s; "
      f"trials where it is shorter than 400 ms: {100 * np.mean(mid - s0 < 0.3999):.1f}%")
EOF
cat > late_sub.py <<'EOF'
for lab, M in (("main", M1), ("all units", MA)):
    vals = []
    for key in ("first", "last"):
        p = np.array([ppc.anova2(y) for y in LATE[lab][key]])
        ok = ~np.isnan(p[:, 0])
        vals += [100 * np.mean(p[ok, i] < 0.05) for i in range(3)]
    within = [abs(v - e[1]) <= e[2] for v, e in zip(vals, exp_sub)]
    print(f"variant, window from 250 ms after code 10, {lab}: first part {vals[0]:.1f}/{vals[1]:.1f}/{vals[2]:.1f}%, "
          f"last 400 ms {vals[3]:.1f}/{vals[4]:.1f}/{vals[5]:.1f}%; within tolerance {sum(within)} of 6")
EOF
cat > late_dec.py <<'EOF'
# Variant: the same with the windows starting no earlier than 250 ms after code 10. The decoder is
# given counts scaled to 400 ms (rate x 0.4 s) so that the two parts are compared on one scale.
for lab in ("main", "all units"):
    res = {key: boot(np.stack(LATE[lab][key]) * 0.4, schemes=((0, 0), (1, 1)), seed=5) for key in ("first", "last")}
    for ci, cn in ((0, "V"), (1, "NV")):
        s = (ci, ci)
        f_, l_ = res["first"][s], res["last"][s]
        print(f"variant, {lab}, {cn}: first part {f_.mean():.1f}, last 400 {l_.mean():.1f}; "
              f"(a) paired over targets P {stats.ttest_rel(f_.mean(0), l_.mean(0)).pvalue:.3g}, "
              f"(b) over bootstraps P {stats.ttest_ind(f_.mean(1), l_.mean(1)).pvalue:.3g}, "
              f"(c) two-sample over targets P {stats.ttest_ind(f_.mean(0), l_.mean(0)).pvalue:.3g}; difference {f_.mean() - l_.mean():.1f}")
EOF
cat > ff80.py <<'EOF'
# Variant (verification round 1): the Fig. 5 axes run from 0 to 80 in count mean and variance.
# Cells whose four values (V and NV count mean and variance) all lie in that range.
in80 = (cm_all.max(axis=1) <= 80) & (cv_all.max(axis=1) <= 80)
ffv, ffn, p2, p1, n, cm, cv = ff_test(M1, in80)
print(f"main, cells within the plotted range 0 to 80: n {n} of {len(M1)}; FF V {ffv:.3f}, NV {ffn:.3f}; "
      f"permutation P two-sided {p2:.3f}, one-sided {p1:.3f}")
EOF
cat > chance.py <<'EOF'
# Chance level of this decoder: each cell's 40 trials in a condition are given shuffled target
# labels (independently per cell), and the full population is decoded leave-one-out, 20 times.
rng_ch = np.random.default_rng(31)
C0 = counts_of(M1)
null = {s: [] for s in ((0, 0), (1, 1))}
for _ in range(20):
    Cs = C0.copy()
    for i in range(Cs.shape[0]):
        for ci in (0, 1):
            flat = Cs[i, ci].reshape(-1)
            Cs[i, ci] = rng_ch.permutation(flat).reshape(8, ppc.N_PER_CELL)
    for s in null:
        null[s].append(run_decoder(Cs, *s).mean())
for s, v in null.items():
    print(f"shuffled labels, {names_s[s]}: mean accuracy {np.mean(v):.1f}% (range {np.min(v):.1f} to {np.max(v):.1f}); nominal chance 12.5%")
EOF
ls
```

```
analog.md
analog.py
chance.py
clock.md
clock.py
endpoint.md
endpoint.py
ff80.py
late.py
late_dec.py
late_sub.py
population.md
population.py
timing.md
timing.py
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/newcells && sed -i '/^dmean = beh.assign/d' endpoint.py && cd entries/shi-2013 && cp reproduce_shi_2013.ipynb $TMPDIR/nb_orig.ipynb && python - <<'EOF'
import json, os
T=os.environ["TMPDIR"]+"/newcells/"
nb=json.load(open('reproduce_shi_2013.ipynb'))
cells=nb['cells']
def code(name, tags):
    return {"cell_type":"code","execution_count":None,"metadata":{"tags":tags} if tags else {},"outputs":[],"source":open(T+name).read().rstrip("\n").splitlines(True)}
def md(name, text=None):
    src = text if text is not None else open(T+name).read()
    return {"cell_type":"markdown","metadata":{},"source":src.rstrip("\n").splitlines(True)}
def find(prefix):
    hits=[i for i,c in enumerate(cells) if ''.join(c['source']).startswith(prefix)]
    assert len(hits)==1, (prefix, hits); return hits[0]
ins = [  # (anchor prefix, offset after anchor, new cells)
 ("Reading of the codes, from the timing", [code("timing.py",["sanity"]), md("timing.md")]),
 ("The target is decoded in about a third", [code("clock.py",["sanity"]), md("clock.md")]),
 ("def measures(unit_list", [md(None,"### Which sessions and neurons\n\nThe paper has 219 monkey X neurons, one per session; the data set has 359 usable monkey X sessions.\nThe recording dates, the target geometry by month, and whether one neuron was recorded in several\nsessions of a day:"), code("population.py",["sanity"]), md("population.md")]),
 ("beh = []\nfor k, t in kept.items():", [code("endpoint.py",["claim:behavior-mean-position-sessions"]), md("endpoint.md")]),
 ("exp_sub = [e[1:] for e in expected(\"hold-subepochs\")]", [code("late.py",["claim:hold-subepochs"]), code("late_sub.py",["claim:hold-subepochs"])]),
 ("def ff_slope", [code("ff80.py",["claim:fig5-fano-factor"])]),
 ("def counts_of", [code("chance.py",["claim:fig6-decoding-vv"])]),
 ("for lab, M in ((\"main\", M1), (\"all units\", MA)):\n    res = {}", [code("late_dec.py",["claim:decoding-subepochs"])]),
 ("E = pd.concat(", [code("analog.py",["claim:eye-position-no-difference"]), md("analog.md")]),
]
pos=[(find(p), new) for p,new in ins]
for i,new in sorted(pos, key=lambda x:-x[0]):
    cells[i+1:i+1]=new
i=find("def indexes(M):")
cells[i]["metadata"]["tags"]=["claim:fig4-indx1-negative","claim:fig4-indx1-means"]
json.dump(nb, open('reproduce_shi_2013.ipynb','w'), indent=1, ensure_ascii=False)
print(len(cells))
EOF
```

```
114
```

**Agent calls Bash**

```bash
cd entries/shi-2013; date -u; cat > $TMPDIR/dev_all.py <<'EOF'
import sys, os, time; sys.path.insert(0, os.environ["TMPDIR"]); sys.path.insert(0, ".")
import dev, json
nb=json.load(open("reproduce_shi_2013.ipynb"))
t=time.time()
ns=dev.run(upto=len(nb["cells"]))
print("time", time.time()-t)
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/dev_all.py > $TMPDIR/dev_out.txt 2>&1; echo exit $?; tail -5 $TMPDIR/dev_out.txt; date -u
```

```
Mon Nov  9 20:54:49 UTC 2026
exit 1
  File "/tmp/claude-1001/dev.py", line 23, in run
    exec(compile("".join(c["source"]), f"cell{i}", "exec"), ns)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell11", line 5, in <module>
NameError: name 'kept' is not defined
Mon Nov  9 20:54:50 UTC 2026
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('reproduce_shi_2013.ipynb')); cells=nb['cells']
i=[k for k,c in enumerate(cells) if ''.join(c['source']).startswith('c10 = allt[')][0]
moved=cells[i:i+2]; del cells[i:i+2]
j=[k for k,c in enumerate(cells) if ''.join(c['source']).startswith('Kept are the sessions')][0]
cells[j+1:j+1]=moved
json.dump(nb, open('reproduce_shi_2013.ipynb','w'), indent=1, ensure_ascii=False)
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/dev_all.py > $TMPDIR/dev_out.txt 2>&1; echo exit $?; tail -5 $TMPDIR/dev_out.txt; date -u
```

```
exit 1
  File "/tmp/claude-1001/dev.py", line 23, in run
    exec(compile("".join(c["source"]), f"cell{i}", "exec"), ns)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell58", line 7, in <module>
IndexError: tuple index out of range
Mon Nov  9 20:55:16 UTC 2026
```

**Agent calls Bash**

```bash
grep -n "#####" $TMPDIR/dev_out.txt | tail -3; python -c "
import json;nb=json.load(open('reproduce_shi_2013.ipynb'));print(''.join(nb['cells'][58]['source']))"
```

```
322:##### cell 56
326:##### cell 57
328:##### cell 58
for lab, M in (("main", M1), ("all units", MA)):
    vals = []
    for key in ("first", "last"):
        p = np.array([ppc.anova2(y) for y in LATE[lab][key]])
        ok = ~np.isnan(p[:, 0])
        vals += [100 * np.mean(p[ok, i] < 0.05) for i in range(3)]
    within = [abs(v - e[1]) <= e[2] for v, e in zip(vals, exp_sub)]
    print(f"variant, window from 250 ms after code 10, {lab}: first part {vals[0]:.1f}/{vals[1]:.1f}/{vals[2]:.1f}%, "
          f"last 400 ms {vals[3]:.1f}/{vals[4]:.1f}/{vals[5]:.1f}%; within tolerance {sum(within)} of 6")
```

**Agent calls Bash**

```bash
python -c "
import json;nb=json.load(open('reproduce_shi_2013.ipynb'));print(''.join(nb['cells'][55]['source']))"; sed -n 300,330p $TMPDIR/dev_out.txt
```

```
## hold-subepochs

> hold-subepochs: Similar percentages were found when the first 400 ms and the last 400 ms of the hold were analyzed separately, 31%, 9% and 5% and 29%, 10% and 4% for position main effect, vision main effect and interaction.
main: units with the peak at 225 deg in V and NV and a position effect: 8 ; candidates matching all: 0
                 session   unit  peak_V  peak_NV  p_pos  p_vis  p_int  peak225_both  dist  match
data/073009/073009_4.mat chan1a      44       44  0.000  0.364  0.537          True 3.400  False
data/031909/031909_3.mat chan1a      44       44  0.000  0.372  0.841          True 4.231  False
data/102408/102408_2.mat chan1a      44       44  0.005  0.378  0.347          True 5.338  False
all units: units with the peak at 225 deg in V and NV and a position effect: 10 ; candidates matching all: 0
                 session   unit  peak_V  peak_NV  p_pos  p_vis  p_int  peak225_both  dist  match
data/073009/073009_4.mat chan1a      44       44  0.000  0.364  0.537          True 3.400  False
data/031909/031909_3.mat chan1a      44       44  0.000  0.372  0.841          True 4.231  False
data/102408/102408_2.mat chan1a      44       44  0.005  0.378  0.347          True 5.338  False
##### cell 48
main: 187 of 359 units (52.1%) with a target main effect or interaction; scaled to 343: 179 (paper 139, 41%)
all units: 241 of 483 units (49.9%) with a target main effect or interaction; scaled to 343: 171 (paper 139, 41%)
variant, 500 ms centred on target acquired: 65.5% of 359
variant, 500 ms centred on code 3: 6.1% of 358
##### cell 51
main, spike count rate: n = 359; position 141 (39.3%), vision 49 (13.6%), interaction 27 (7.5%); scaled to 343: 135, 47, 26
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('reproduce_shi_2013.ipynb'))
c=nb['cells'][58]; s=''.join(c['source']).replace("abs(v - e[1]) <= e[2]","abs(v - e[0]) <= e[1]"); c['source']=s.splitlines(True)
json.dump(nb, open('reproduce_shi_2013.ipynb','w'), indent=1, ensure_ascii=False)
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/dev_all.py > $TMPDIR/dev_out.txt 2>&1; echo exit $?; tail -5 $TMPDIR/dev_out.txt; date -u
```

```
exit 0
1000.0         46         0.960            1.056         1.056
1100.0          4         1.152            1.152         1.152
sessions whose field 11 changes within the session: 3
trials with field 11 >= 1200, any outcome: 4 ; completed: 0
time 31.10259771347046
Mon Nov  9 20:55:55 UTC 2026
```

**Agent**

Whole analysis runs in 31 s on the cache. Reading the new outputs.

**Agent calls Bash**

```bash
cd entries/shi-2013; python - <<'EOF'
import json
nb=json.load(open('reproduce_shi_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code': 
        s=''.join(c['source'])
        if any(s.startswith(p) for p in ["c10 = allt","rows = []\nfor k in kept:","SUBMITTED","# Checks of the record","# Variant (verification","for lab, M in ((\"main\", M1), (\"all units\", MA)):\n    vals = []","# Chance level","# Variant: the same","# The analog files"]): print(i, s[:40].replace("\n"," "))
EOF
```

```
15 c10 = allt[allt.completed & allt.params.
23 rows = [] for k in kept:     t = kept[k]
28 SUBMITTED = pd.Timestamp("2012-03-14")  
32 # Checks of the record's hand position (
57 # Variant (verification round 1): hold w
58 for lab, M in (("main", M1), ("all units
82 # Variant (verification round 1): the Fi
89 # Chance level of this decoder: each cel
97 # Variant: the same with the windows sta
104 # The analog files of three sessions (pp
```

**Agent calls Bash**

```bash
cd $TMPDIR; awk '/^##### cell (15|23|28|32|57|58|82|89|97|104)$/{p=1;print;next} /^##### cell/{p=0} p' dev_out.txt
```

```
##### cell 15
completed trials with a record: code 10 to code 12 interval against the trial's own field 11 (s):
           trials  min_10_to_12  median_10_to_12  max_10_to_12  min_excess
field11_s                                                                 
0.8           266         0.832            0.992         1.248       0.032
0.9         26942         0.928            1.184         1.792       0.028
1.0          3386         1.056            1.312         1.856       0.056
1.1           195         1.152            1.152         1.152       0.052
trials where code 10 to code 12 is shorter than field 11: 0 of 30789
excess of code 10 to code 12 over field 11 (s), quantiles: {0.0: 0.028, 0.01: 0.028, 0.05: 0.056, 0.25: 0.22, 0.5: 0.284, 0.75: 0.348, 0.95: 0.44, 1.0: 0.892}
all: trials whose 800 ms window (code 12 - 0.8 s) starts less than 0.25 s after code 10: 11.9% of 30789
kept sessions: trials whose 800 ms window (code 12 - 0.8 s) starts less than 0.25 s after code 10: 11.6% of 28790
all: trials whose 800 ms window (code 12 - 0.8 s) starts less than 0.3 s after code 10: 21.2% of 30789
kept sessions: trials whose 800 ms window (code 12 - 0.8 s) starts less than 0.3 s after code 10: 21.0% of 28790
##### cell 23
per session, smallest one-way ANOVA P of the target effect over its units:
   last 800 ms before code 12: P < 0.05 in 153 of 359 sessions
   800 ms before the trial's first event: P < 0.05 in 10 of 359 sessions (expected by chance about 24 units' worth)
sessions where the clock is not supported by this check (no unit with a hold target effect): 206
##### cell 28
[... 84 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat questions/ishii-2025.yaml | head -40; ls questions
```

```
# Questions from attempt ishii-2025-01 (author, 2026-11-01) about
# claims/001249/10.7554-elife.91765.yaml, asked under docs/protocol.md, Author, step 1.6. The claim was
# tested as the file has it.
dandiset: "001249"
paper: doi:10.7554/elife.91765
questions:
- claim: fig6c-decay-length
  asked: 2026-11-01
  question: Should the readings of the decay length include the time from the peak of the response after
    onset to the first sample below 0? The criterion lists (a) the time from onset to the first sample
    below 0 and (b) the total time below 0 in 0 to 120 s, both measured from onset. The Results describe
    the decay length as the time for the increased signal to return to baseline, which reads naturally
    as starting from the increased signal, that is from the peak.
  passage: To quantify this difference, we calculated the decay length of calcium signal, the time for
    the increased calcium signal to return to baseline (Results, MPOA Vgat cells display prolonged
    activity, paragraph 1); The decay length was quantified by calculating the time the z-scored signal
    was smaller than 0 (Methods, In vivo calcium imaging experiments and analysis).
  why: Under (a) Vgat responders decay no later than Vglut2 responders (18.7 against 22.2 s, p = 0.544)
    and under (b) they are below 0 for less time (53.9 against 75.3 s, p = 0.0089), so the claim is not
    reproduced. Measured from the peak, the decay length equals the deposited per-cell values for 207 of
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -l -r "crcns" questions | head -3; ls schemas; f=$(grep -l -r "crcns" questions | head -1); head -12 $f
```

```
questions/moaddab-2021.yaml
questions/watson-2016/crcns-fcx-1.yaml
questions/johnson-2018.yaml
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
# Questions from attempt moaddab-2021-01 (author revision after verifier round 1,
# 2026-11-06) about claims/crcns-rrf-1/10.1016-j.cub.2021.02.055.yaml, asked under docs/protocol.md,
# "Hand over for verification". The verifier reported these as places where the claims file may
# misread the paper; the claims were tested as the file has them.
dataset: CRCNS:rrf-1
paper: doi:10.1016/j.cub.2021.02.055
questions:
- claim: fig6a-k1-shock
  asked: 2026-11-06
  question: For k1, k3, k5 and k6 the claims file takes the outcome window from the Figure 6 gray
    boxes (0 to 8 s after shock offset) and the expected means and CI patterns from Table S4.
    Table S4's means for these four clusters are reproduced to within 0.008 by 0 to 4 s after shock
```

**Agent calls Write**

```json
{
 "file_path": "questions/shi-2013.yaml",
 "content": "# Questions from attempt shi-2013-01 (author revision after verifier round 1, 2026-11-09) about\n# claims/shi-2013.yaml, asked under docs/protocol.md, \"Hand over for verification\". The verifier\n# reported this as a place where the claims file may misread the paper; the claim was tested as\n# the file has it.\ndataset: CRCNS:ppc-1\npaper: doi:10.1152/jn.00223.2012\nquestions:\n- claim: fig5-fano-factor\n  asked: 2026-11-09\n  question: Do the outlier readings of the criterion match the cells the paper plotted in Fig. 5?\n    The criterion names (a) the 5 cells removed for Fig. 4 and (b) Tukey outliers (1.5 IQR) on the\n    count means or variances. Both axes of Fig. 5 (count mean and count variance) run from 0 to 80,\n    which suggests that every cell left after outlier removal had a count variance of at most about\n    80. Removing only the 5 Fig. 4 cells, whose outliers are defined on the index INDX1 and not on\n    the counts, keeps cells far outside those axes. Should a reading that removes cells outside\n    the plotted range (or outliers on the count variance alone) be part of the criterion? Raised by\n    the round-1 verifier of attempt shi-2013-01.\n  passage: Fig. 5. Fano factors (FFs) in the V and NV conditions. Shown are scatterplots of the spike\n    count mean vs. the spike count variance for all cells (after outlier removal) for the location\n    defined by the peak rate in the NV condition (Fig. 5 legend; axes 0 to 80 in the figure).\n    Note that N represents no. of neurons after outlier removal (5 neurons total), defined as\n    indexes >1.5 times the interquartile range (Fig. 4 legend).\n  why: Under reading (a) (356 cells) the count variances reach 2,188, a few high-rate cells set the\n    slopes, and FF is 1.84 in V and 3.19 in NV (P = 0.28). Under reading (b) (295 cells) FF is 0.98\n    and 1.24 (P = 0.020). With the 331 cells whose count means and variances lie within 0 to 80, a\n    variant shown in the notebook, FF is 1.03 and 1.21 (P = 0.17). None puts both FFs within\n    tolerance with P < 0.05, so the outcome would not change on present numbers, but the reading\n    decides which cells enter the test.\n"
}
```

```
File created successfully at: questions/shi-2013.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "questions/shi-2013.yaml",
 "old_string": "    defined as\n    indexes >1.5 times the interquartile range (Fig. 4 legend).",
 "new_string": "    defined as\n    indexes ... 1.5 times the interquartile range (Fig. 4 legend)."
}
```

```
<tool_use_error>String to replace not found in file.
String:     defined as
    indexes >1.5 times the interquartile range (Fig. 4 legend).</tool_use_error>
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "^(results|behavior|neurophysiology)" paper/10.1152-jn.00223.2012.txt | head; grep -n "RESULTS\|Behavior$" paper/10.1152-jn.00223.2012.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  sed -i 's/indexes >1.5 times the interquartile range/indexes ... 1.5 times the interquartile range/' questions/shi-2013.yaml; grep -n "interquartile" questions/shi-2013.yaml; python -c "import yaml;yaml.safe_load(open('questions/shi-2013.yaml'))"
```

```
22:    indexes ... 1.5 times the interquartile range (Fig. 4 legend).
```

**Agent**

Now updating the clock print and the markdown/conclusion cells.

**Agent calls Bash**

```bash
cd entries/shi-2013; python - <<'EOF'
import json
nb=json.load(open('reproduce_shi_2013.ipynb')); cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def find(prefix):
    h=[i for i,c in enumerate(cells) if src(i).startswith(prefix)]; assert len(h)==1,(prefix,h); return h[0]
def rep(prefix, old, new):
    i=find(prefix); s=src(i); assert old in s, (prefix, old); cells[i]['source']=s.replace(old,new).splitlines(True)
def setsrc(prefix, new):
    i=find(prefix); cells[i]['source']=new.rstrip("\n").splitlines(True)
rep("rows = []\nfor k in kept:", '''      f" (expected by chance about {0.05 * CK.n_units.sum():.0f} units' worth)")''',
    '''      f" (expected if no unit were tuned: {np.sum(1 - 0.95 ** CK.n_units):.0f})")''')
rep("rows = []\nfor k in kept:", '''print("sessions where the clock is not supported by this check (no unit with a hold target effect):",
      int((CK.p_hold >= 0.05).sum()))''', '''print("sessions where this check does not support the clock (no unit with a hold target effect):",
      int((CK.p_hold >= 0.05).sum()))''')
setsrc("Per session the check has one to four units", '''Per session the check has one to four units, so it supports the shared clock only where a unit is
tuned to the target in the hold: 153 of the 359 sessions. Before the trial starts, 10 sessions
have a unit with a target effect, fewer than the 19 expected if no unit were tuned. In the other
206 sessions no unit carries a target effect in the hold, so the clock is not established for them
by this check. They are kept, as the paper kept cells without a position effect.''')
setsrc("The kept sessions were all recorded between", '''The kept sessions were all recorded between October 2008 and November 2009, on 92 days, before
the paper was submitted (14 March 2012). Their target geometry is the same in every month: monkey
X's layout throughout, with no block of sessions in monkey B's square layout or at a depth near
14.5 cm. The paper has one neuron per session (Table 1 legend, "means +/- SD over 219 sessions for
monkey X"; Results, Behavior, "both animals (N = 343 sessions)" against 343 neurons). Consecutive
sessions on one day do not look like one neuron recorded again: their tuning correlation has a
median of 0.04, against -0.01 for sessions on different days, and 3.4% of the same-day pairs
correlate above 0.8, against 1.1%, so at most a handful could be repeats. The data set therefore
holds about 140 more monkey X sessions than the paper's 219, the descriptor's 124 monkey B cells
are not identifiable in it, and which sessions the paper used is not documented. All 359 are used.
One unit is taken from each, as the paper has one neuron per session; which unit is an assumption
(the first sorted, "a"), and all 483 sorted units are shown as a variant throughout.''')
setsrc("The conditions are interleaved within each session", '''The conditions are interleaved within each session (a median of 39 runs, against 41 for a random
order), so slow drift cannot make V and NV differ. The MANOVA is calibrated on these data: with the
labels shuffled it rejects in 5.7% of pairs. The 16% is therefore a property of the positions
recorded under the real labels. Whether the record's position is the mean over the hold, as the
paper's Fig. 2 legend describes, or one sample, the data do not say. Within a session the five
trials at a target spread by about 0.2 to 0.4 cm (median SD 0.29, 0.29 and 0.19 cm in x, y, z), and
the session means spread over sessions by 0.32 to 0.67 cm, about half of Table 1's SDs. No analog
channel follows the hand (see eye-position-no-difference), so there is no position trace to check
the record against.''')
setsrc("Under this reading of the analog files", '''Under this reading of the analog files, no channel's hold-period mean correlates with the
record's hand position beyond |r| = 0.25, and none differs between targets in the hold (one-way
ANOVA P from 0.15 to 1.00), as an arm position channel would. Most channels saturate often at the
12-bit limits (+/-2047), and channel 6 spans the full 16-bit range, which a 12-bit converter cannot
give, so the reading of the layout is at least partly wrong for it. A fixation trace would be
nearly constant across targets in the hold, and no channel can be named as eye position on that
alone. This is consistent with no usable eye or arm channel, not a proof of it: another layout of
the .dat file could give other channels.''')
json.dump(nb, open('reproduce_shi_2013.ipynb','w'), indent=1, ensure_ascii=False)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('reproduce_shi_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if c['cell_type']=='markdown' and (s.startswith('**Result') or s.startswith('## eye') or s.startswith('## movement')):
        print(f"=== [{i}]"); print(s)
EOF
```

```
=== [34]
**Result: not reproduced.** In monkey X, 16.1% of session and target pairs (2,872 pairs, 359
sessions) show a significant V against NV difference in endpoint position by the two-group MANOVA,
both as the mean of the 8 target percentages (16.12 +/- 4.27) and pooled (16.12), against 6.9 +/-
1.5%. Each trial has one endpoint in the data (the record's x, y, z), not the paper's mean over the
800 ms hold; monkey B is not in the data set.
=== [37]
**Result: not reproduced.** With Levene's test centred on the mean, 8.1%, 8.1% and 7.0% of pairs
differ in x, y and z (paper 5 +/- 1.9, 4.7 +/- 1.6, 6 +/- 0.9): z is within tolerance, x and y are
not. Centred on the median (Brown-Forsythe), 0.4 to 0.7%, none within. No reading puts all three
axes within tolerance.
=== [40]
**Result: partially reproduced.** All 48 of monkey X's means are within the Table 1 SDs (100%,
also after removing the mean offsets of -0.10, -0.17 and +0.26 cm), but the largest V minus NV
difference of the means is 0.150 cm (135 degrees, y), above the 0.121 cm bound. Monkey B's 48
values cannot be tested; the data set holds 359 usable monkey X sessions against the paper's 219.
=== [43]
**Result: not reproduced.** 8.3% of monkey X's 48 SDs over sessions are within 10% of Table 1; the
SDs run from 0.32 to 0.67 cm against 0.50 to 1.28 cm, a median of 0.55 times the paper's. The SD
over all trials (a variant) runs from 0.41 to 0.73 cm, 14.6% within.
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; awk '/^##### cell (96|88|90|100)$/{p=1;print;next} /^##### cell/{p=0} p' dev_out.txt | cut -c1-400
```

```
##### cell 88
main: 359 cells, full population, accuracy per target and mean:
   V/V                [ 80. 100.  80. 100.  80. 100. 100.  60.] mean 87.5
   NV/NV              [ 80.  80.  80.  60.  60.  80. 100.  80.] mean 77.5
   train NV, test V   [ 20.  60.  20. 100.   0. 100. 100.  80.] mean 60.0
   train V, test NV   [40. 20. 40. 60. 60. 60. 40. 80.] mean 50.0
   bootstrap (a) resample n cells, V/V               : mean 77.4 +/- 6.5 (SD over 200); SD over targets of the mean 8.2
   bootstrap (a) resample n cells, NV/NV             : mean 63.7 +/- 7.0 (SD over 200); SD over targets of the mean 9.4
   bootstrap (a) resample n cells, train NV, test V  : mean 58.9 +/- 6.8 (SD over 200); SD over targets of the mean 28.3
   bootstrap (a) resample n cells, train V, test NV  : mean 52.7 +/- 7.2 (SD over 200); SD over targets of the mean 12.7
   bootstrap (b) populations of 200 cells, V/V               : mean 73.3 +/- 7.2 (SD over 200); SD over targets of the mean 6.9
   bootstrap (b) populations of 200 cells, NV/NV             : mean 57.2 +/- 8.3 (SD over 200); SD over targets of the mean 8.0
   bootstrap (b) populations of 200 cells, train NV, test V  : mean 55.1 +/- 7.4 (SD over 200); SD over targets of the mean 23.2
   bootstrap (b) populations of 200 cells, train V, test NV  : mean 50.6 +/- 8.2 (SD over 200); SD over targets of the mean 11.9
   cross reading (b), all five trials: train NV, test V 62.1 +/- 6.4
   cross reading (b), all five trials: train V, test NV 56.8 +/- 7.0
all units: 483 cells, full population, accuracy per target and mean:
   V/V                [ 80. 100.  80.  60.  80. 100.  80.  60.] mean 80.0
   NV/NV              [80. 80. 20. 80. 60. 80. 80. 60.] mean 67.5
   train NV, test V   [ 20.  60.   0. 100.   0. 100.  80.  80.] mean 55.0
[... 28 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 997,1034p claims/shi-2013.yaml; sed -n 1317,1400p claims/shi-2013.yaml
```

```
- id: hold-subepochs
  statement: Similar percentages were found when the first 400 ms and the last 400 ms of the hold
    were analyzed separately, 31%, 9% and 5% and 29%, 10% and 4% for position main effect,
    vision main effect and interaction.
  source: Results, Neurophysiology, paragraph 2
  quote: Similar percentages were noted when the first 400 ms and the last 400 ms of the holding
    period were separately analyzed (31/9/5% and 29/10/4%, respectively)
  expected:
  - quantity: first 400 ms, position main effect
    value: 31
    tolerance: 3.1
    unit: "%"
  - quantity: first 400 ms, vision main effect
    value: 9
    tolerance: 0.9
    unit: "%"
  - quantity: first 400 ms, interaction
    value: 5
    tolerance: 0.5
    unit: "%"
[... 102 more lines not kept]
```

**Agent**

Now rewriting the affected conclusion cells.

**Agent calls Bash**

```bash
cd entries/shi-2013; python - <<'EOF'
import json
nb=json.load(open('reproduce_shi_2013.ipynb')); cells=nb['cells']
def src(i): return ''.join(cells[i]['source'])
def find(prefix):
    h=[i for i,c in enumerate(cells) if src(i).startswith(prefix)]; assert len(h)==1,(prefix,h); return h[0]
def setsrc(prefix, new):
    i=find(prefix); cells[i]['source']=new.rstrip("\n").splitlines(True)
setsrc("**Result: not reproduced.** In monkey X, 16.1%", '''**Result: not reproduced.** In monkey X, 16.1% of session and target pairs (2,872 pairs, 359
sessions) show a significant V against NV difference in endpoint position by the two-group MANOVA,
both as the mean of the 8 target percentages (16.12 +/- 4.27) and pooled (16.12), against 6.9 +/-
1.5%. The test is calibrated on these data (5.7% with shuffled labels), and the conditions are
interleaved within sessions, so neither the test nor drift explains the excess. Each trial has one
endpoint in the data (the record's x, y, z), and whether it is the mean over the 800 ms hold, as in
the paper, is not documented; monkey B is not in the data set.''')
setsrc("**Result: reproduced.** 49 of 359 units", '''**Result: reproduced (resting on an assumption).** 49 of 359 units (13.6%; 47 scaled to 343)
have a vision main effect, against 44 +/- 4.4, and fewer than the 141 with a position effect. All
483 units give 14.3% (49 scaled), just above the bound of 48.4, so the outcome rests on taking one
unit per session (the first sorted). The count does not depend on which code is V.''')
setsrc("**Result: not reproduced.** In the first and last 400 ms", '''**Result: not reproduced (resting on an assumption).** In the first and last 400 ms,
35.7/11.4/7.0% and 28.7/13.6/5.0% of the 359 units have position, vision and interaction effects,
against 31/9/5% and 29/10/4%: 1 of 6 within tolerance. All 483 units give 3 of 6
(31.5/11.2/6.2% and 27.1/13.3/4.3%), which would be partial, so the outcome rests on taking one
unit per session. Starting the window at least 250 ms after code 10 (variant) gives 35.7/10.9/7.5%
and 28.8/13.7/5.0% (1 of 6) and, for all units, 3 of 6: the possible inclusion of a saccade at the
start of the window does not explain the difference. The position percentages are close; the
vision and interaction ones are higher than the paper's.''')
setsrc("**Result: partially reproduced.** After removing outliers (reading (a), 3 cells)", '''**Result: partially reproduced (resting on an assumption).** After removing outliers (reading
(a), 3 cells), INDX1 is negative in 77.8% of all cells, 68.4% of Position Only, 75.0% of
Position/Vision and 75.0% of Vision Only cells (paper 84, 77, 85, 84%): only the first is within
tolerance, and the others are 0.6 to 1.5 points below it. Readings (b) and (c) give the same.
Group sizes are 356, 98, 44 and 20 (paper 338, 110, 38, 27). Among all 483 units the four
percentages (81.4, 71.4, 76.8, 81.2%) are within tolerance, so the outcome rests on taking one unit
per session. INDX1 is mostly negative also under the other code mapping (80.5% of all cells).''')
setsrc("**Result: not reproduced (resting on an assumption).** With the Fig. 4 outliers removed", '''**Result: not reproduced (resting on an assumption).** With the Fig. 4 outliers removed
(reading (a), 356 cells), FF is 1.84 in V and 3.19 in NV, larger in NV but not significantly
(permutation P = 0.280) and both above tolerance. With Tukey outliers of the count means or
variances removed (reading (b), 295 cells), FF is 0.98 and 1.24, larger in NV with P = 0.020, but
both below tolerance. Reading (a) is adopted, as the paper defines outliers only for Fig. 4.
Keeping only the 331 cells within the plotted range of Fig. 5 (0 to 80, a variant) gives 1.03 and
1.21 (P = 0.172): V within tolerance, NV not, and no significant difference. Whether the criterion's
outlier readings match the paper's Fig. 5 is asked of a reader (questions/shi-2013.yaml).''')
setsrc("**Result: not reproduced.** Trained and tested on V, the decoder", '''**Result: not reproduced.** Trained and tested on V, the decoder's accuracy over 200 bootstrap
resamples of the 359 cells is 77.4 +/- 6.5% (reading (a)) and 73.3% with populations of 200 cells
(reading (b)), below 91.6 +/- 9%. The full population without resampling gives 87.5%. With
shuffled target labels the decoder gives 16.1% (V) and 11.2% (NV) on average over 20 shuffles,
near the nominal chance of 12.5%, so the accuracies are far above chance.''')
setsrc("**Result: reproduced (resting on an assumption).** V accuracy exceeds NV accuracy", '''**Result: reproduced (resting on an assumption).** V accuracy exceeds NV accuracy (77.4 against
63.7%) and every t-test reading finds it (paired over targets P = 0.0087, over bootstraps P <
1e-60, unpaired over targets P = 0.0081), as do populations of 200 cells. Which condition is V
rests on the code mapping: under the other one NV decodes better (77.4 against 63.7%). With all 483
units only the test over bootstraps finds it (paired over targets P = 0.29, unpaired P = 0.40).''')
setsrc("**Result: not reproduced.** The 400 ms windows decode less well", '''**Result: not reproduced (resting on an assumption).** The 400 ms windows decode less well than
the 800 ms window (V 61.2 and 66.0 against 78.3%; NV 59.8 and 42.8 against 64.6%), as the paper
says. In V the first and last 400 ms do not differ by the paired test (P = 0.38), but in NV the
last 400 ms decode 17.0 points worse than the first (paired P = 0.0073, unpaired over targets P =
0.017), so a difference is found. With the window starting at least 250 ms after code 10 (variant)
NV still differs (57.7 against 42.8%, paired P = 0.019, unpaired P = 0.031). With all 483 units the
NV difference (14.6 points) is not significant by the paired (P = 0.072) or unpaired (P = 0.074)
test over targets, and only the test over bootstraps finds it, so the outcome rests on taking one
unit per session.''')
setsrc("## eye-position-no-difference", '''## eye-position-no-difference

> eye-position-no-difference: Neither mean eye position nor the variance of its horizontal or vertical component differed between V and NV for any target (MANOVA and Levene's test).

The claim is blocked (`metadata_insufficient`): the data set holds no documented eye position.
The analog files' channels are named only AD01 to AD16, and a summary of the channels of three
sessions is printed below. The 24 field record (in part of the sessions) ends with two numbers
near (0, -1.8) that might be an eye position averaged over the hold (the eye was to fixate the
centre), but no file names them, and their spread within a session (SD about 0.05 to 0.07) cannot
show what they are: it is below the eye tracker's resolution of 0.25 degrees (Methods,
Experimental apparatus), which a mean over about 100 samples could reach. The test is run on them
below only to show what they give; it decides nothing.''')
setsrc("**Result: blocked (metadata_insufficient).** The data set holds no documented eye position.", '''**Result: blocked (metadata_insufficient).** The data set holds no documented eye position. No
analog channel of the three sessions summarised differs between targets in the hold or follows the
hand, and the layout of the analog files is itself undocumented; record fields 22 and 23 are
unnamed.''')
setsrc("**Result: blocked (metadata_insufficient).** Which code is NV was inferred", '''**Result: blocked (metadata_insufficient).** Which code is NV was inferred above from the aborts
themselves, so the claim's comparison of NV with V aborts would test the inference, not the paper.
The window sizes are not documented either (field 1 of the record is read as one). For the record,
with field 1 at 8, 10 and 12, 31.4, 26.6 and 5.7% of code 7 trials and 13.9, 24.4 and 3.6% of code 4
trials that reached code 10 were aborted. The part that does not depend on the mapping, more aborts
as the window shrinks, holds for code 7 but not for code 4 (24.4% at 10 against 13.9% at 8), if
field 1 is the window size.''')
setsrc("**Result: blocked (data_missing).** Record field 11", '''**Result: blocked (data_missing).** On every completed trial the time from code 10 to code 12 is
at least the trial's own field 11 plus 28 ms (data check), and each session's shortest interval
follows its field 11 (800 to 1,100 ms against 0.83 to 1.15 s), so field 11 is read as the minimum
hold. No completed trial has a minimum hold of 1,200 ms or more; the data set holds no subset of
sessions with the extended hold.''')
json.dump(nb, open('reproduce_shi_2013.ipynb','w'), indent=1, ensure_ascii=False)
EOF
```

```
(Bash completed with no output)
```

**Agent**

Updating the summary cell.

**Agent calls Bash**

```bash
cd entries/shi-2013; python - <<'EOF'
import json
nb=json.load(open('reproduce_shi_2013.ipynb')); cells=nb['cells']
i=[k for k,c in enumerate(cells) if ''.join(c['source']).startswith('## Summary')][0]
s=''.join(cells[i]['source'])
old_a='''  one unit from each (the first sorted unit), with all 483 sorted units as a variant. Counts are
  compared with the paper's as percentages, or scaled to 343.'''
new_a='''  one unit from each, as the paper has one neuron per session; that it is the first sorted unit is
  an assumption, and all 483 sorted units are a variant. Four outcomes (hold-vision-main-effect,
  hold-subepochs, fig4-indx1-negative, decoding-subepochs) would differ with all units and are
  marked as resting on it. Counts are compared with the paper's as percentages, or scaled to 343.'''
assert old_a in s; s=s.replace(old_a,new_a)
old_b='''- The meaning of the event codes is read from their timing: 12 as the end of the hold, 8 as
  movement onset (cursor leaving the start window).'''
new_b='''- The meaning of the event codes is read from their timing: 12 as the end of the hold, 8 as
  movement onset (cursor leaving the start window). On every completed trial code 10 to code 12
  lasts at least the record's field 11 (the minimum hold) plus 28 ms, so the 800 ms window lies in
  the hold as the task timed it; in 11.6% of trials it starts less than 250 ms after code 10, and a
  variant that starts it later leaves the sub-epoch results as they are.'''
assert old_b in s; s=s.replace(old_b,new_b)
old_c='''- The data descriptor says 343 cells, 219 from monkey X and 124 from monkey B; every session with a
  trial record has monkey X's layout, and there are more usable monkey X sessions (359, with 485
  sorted units) than the paper's 219. Which of them the paper used is not documented.'''
new_c='''- The data descriptor says 343 cells, 219 from monkey X and 124 from monkey B; every session with a
  trial record has monkey X's layout, in every month from October 2008 to November 2009, and there
  are more usable monkey X sessions (359, with 485 sorted units, all recorded before the paper was
  submitted, and not repeats of one neuron within a day) than the paper's 219. Which of them the
  paper used is not documented.'''
assert old_c in s; s=s.replace(old_c,new_c)
old_d='''- The analog files' channels are named AD01 to AD16 without description.'''
new_d='''- The analog files' channels are named AD01 to AD16 without description, and the layout of the
  `.plxAnaAD.dat` files is not documented. Under the layout read here no channel of three sessions
  follows the hand or differs between targets in the hold.'''
assert old_d in s; s=s.replace(old_d,new_d)
cells[i]['source']=s.splitlines(True)
json.dump(nb, open('reproduce_shi_2013.ipynb','w'), indent=1, ensure_ascii=False)
EOF
PYTHONPATH=. $TMPDIR/venv/bin/python $TMPDIR/dev_all.py > $TMPDIR/dev_out.txt 2>&1; echo exit $?; grep -A6 "^##### cell 23$" $TMPDIR/dev_out.txt; date -u
```

```
exit 0
##### cell 23
per session, smallest one-way ANOVA P of the target effect over its units:
   last 800 ms before code 12: P < 0.05 in 153 of 359 sessions
   800 ms before the trial's first event: P < 0.05 in 10 of 359 sessions (expected if no unit were tuned: 24)
sessions where this check does not support the clock (no unit with a hold target effect): 206
##### cell 26
main population (first unit per session): 359 units; left out, no hold spikes: 0
Mon Nov  9 20:58:28 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/shi-2013; sed -i 's/have a unit with a target effect, fewer than the 19 expected if no unit were tuned/have a unit with a target effect, fewer than the 24 expected if no unit were tuned/' reproduce_shi_2013.ipynb; grep -c "fewer than the 24 expected" reproduce_shi_2013.ipynb; git diff --stat; cd  && python tools/entry.py check entries/shi-2013 2>&1 | tail -5
```

```
1
 entries/shi-2013/ppc.py                   |  74 ++++-
 entries/shi-2013/reproduce_shi_2013.ipynb | 512 +++++++++++++++++++++++++++---
 tools/build_site.py                       | 248 ++++++++++++++-
 tools/entry.py                            | 112 ++++++-
 tools/notify.py                           |   5 +-
 tools/runner/chain.sh                     |   5 +-
 tools/site_assets/app.css                 |  31 ++
 tools/site_assets/list.js                 |  33 +-
 8 files changed, 945 insertions(+), 75 deletions(-)
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
0 error(s)
```

**Agent calls Bash**

```bash
cd entries/shi-2013; python - <<'EOF'
import json, uuid
nb=json.load(open('reproduce_shi_2013.ipynb'))
print(nb.get('nbformat'), nb.get('nbformat_minor'), sum('id' in c for c in nb['cells']), len(nb['cells']))
for c in nb['cells']:
    if 'id' not in c and nb.get('nbformat_minor',0)>=5: c['id']=uuid.uuid4().hex[:8]
json.dump(nb, open('reproduce_shi_2013.ipynb','w'), indent=1, ensure_ascii=False)
EOF
git diff reproduce_shi_2013.ipynb | head -30
```

```
4 5 98 114
diff --git a/entries/shi-2013/reproduce_shi_2013.ipynb b/entries/shi-2013/reproduce_shi_2013.ipynb
index b5ada022f2..a6bcba16a3 100644
--- a/entries/shi-2013/reproduce_shi_2013.ipynb
+++ b/entries/shi-2013/reproduce_shi_2013.ipynb
@@ -344,6 +344,52 @@
     "to 15) and may be window sizes; no file says."
    ]
   },
+  {
+   "cell_type": "code",
+   "execution_count": null,
+   "metadata": {
+    "tags": [
+     "sanity"
+    ]
+   },
+   "outputs": [],
+   "source": [
+    "c10 = allt[allt.completed & allt.params.notna()].copy()\n",
[... 11 more lines not kept]
```

**Agent**

Format is consistent. Checking for banned words/dashes, then running the full entry.

**Agent calls Bash**

```bash
cd  grep -n -P "—|\brather\b" entries/shi-2013/reproduce_shi_2013.ipynb entries/shi-2013/ppc.py questions/shi-2013.yaml attempts/shi-2013-01.yaml | head; date -u; timeout 7000 python tools/entry.py all entries/shi-2013 > $TMPDIR/run.log 2>&1; echo exit $?; tail -15 $TMPDIR/run.log; date -u
```

```
Mon Nov  9 20:58:41 UTC 2026
exit 0
Installed kernelspec registry-shi-2013 in executed/shi-2013/.venv/share/jupyter/kernels/registry-shi-2013
0 error(s)
pass  reproduce_shi_2013.ipynb  (253 s)
Mon Nov  9 21:03:00 UTC 2026
```

**Agent**

Full run passed (253 s). Checking the executed outputs against the text.

**Agent calls Bash**

```bash
cd  python - <<'EOF' > $TMPDIR/exec_out.txt
import json
nb=json.load(open('executed/shi-2013/reproduce_shi_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    if c['cell_type']!='code': continue
    out=''
    for o in c.get('outputs',[]):
        if o.get('output_type')=='stream': out+=''.join(o['text'])
        elif 'data' in o and 'text/plain' in o['data']: out+=''.join(o['data']['text/plain'])+"\n"
        elif o.get('output_type')=='error': out+="ERROR "+o['ename']
    print(f"##### cell {i}\n{out}")
EOF
diff <(grep -v "^##### cell [0-7]$" $TMPDIR/dev_out.txt | sed -n '/##### cell 9/,$p' | grep -v "^time ") <(sed -n '/##### cell 9$/,$p' $TMPDIR/exec_out.txt) | head -40; sed -n '/##### cell 3$/,/##### cell 9$/p' $TMPDIR/exec_out.txt | head -40
```

```
27a28
> 
39a41
> 
73a76
> 
87a91
> 
96a101
> 
112a118
> 
117a124
> 
122a130
> 
150a159
> 
165a175
> 
[... 57 more lines not kept]
```

**Agent**

Executed outputs match the dev run. Now the attempt record; checking the schema for `verifications`.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
s=json.load(open('schemas/attempt.schema.json'))
def find(d, key, path=""):
    if isinstance(d, dict):
        for k,v in d.items():
            if k==key: print(path+"/"+k, json.dumps(v, indent=1)[:3000])
            find(v, key, path+"/"+k)
    elif isinstance(d, list):
        for i,v in enumerate(d): find(v,key,path+f"[{i}]")
find(s, "verifications")
EOF
grep -l "verifications:" attempts/*.yaml | head -3
```

```
/properties/verifications {
 "type": "array",
 "items": {
  "type": "object",
  "additionalProperties": false,
  "required": [
   "date",
   "kind",
   "by",
   "results"
  ],
  "properties": {
   "date": {
    "type": "string",
    "format": "date"
   },
   "kind": {
    "enum": [
     "agent",
     "person",
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
cd  awk '/^verifications:/,0' attempts/amjad-2025-01.yaml | head -30
```

```
verifications:
- date: '2026-10-15'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: The first executed notebook with the conclusion cells and the summary removed, the helper
    module and the claims file, with the paper's full text (PMC12183687). The verifier read the
    archive's file list and metadata through the DANDI API and tested the helpers on synthetic inputs
    (beta_power, burst_onsets, window_mean, codes_per_trial, rereference, fscv_window_mean, best_lag,
    reward_blocks). It had no attempt record and took the claims from the claims file.
  results:
  - claim: insertion-yield
    agrees: true
    outcome: blocked
    reason: The archive has 3 assets with sites c8dg, c3bs, c3a and cl3, and nothing about implanted
      or failed sensors. Figure 3 names 4 functional Monkey T sites against the paper's "3/14", so
      "sensor" may mean probe. Neither count can be checked; an implant log of sensors per monkey is
      not in the archive.
    response: No change.
  - claim: chronic-duration
    agrees: true
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml, difflib
s=open('attempts/shi-2013-01.yaml').read()
d=yaml.safe_load(s)
out=yaml.safe_dump(d, sort_keys=False, width=100, allow_unicode=True)
diff=list(difflib.unified_diff(s.splitlines(), out.splitlines(), lineterm=""))
print(len(diff)); print("\n".join(diff[:30]))
EOF
```

```
600
--- 
+++ 
@@ -26,19 +26,19 @@
   notebook: reproduce_shi_2013.ipynb
   output: claim:behavior-mean-position-sessions
   measured: 16.12
-  notes: In 2,872 session and target pairs of 359 monkey X sessions, 16.1% show a significant V
-    against NV difference by the two-group MANOVA (Hotelling T squared), both as the mean of the 8
-    target percentages (16.12, SD 4.27 over targets) and pooled (16.12), against 6.9 +/- 1.5%.
-    Per target the percentage runs from 9.2 to 22.8%.
-  deviations:
-  - Monkey X only; the data set holds no monkey B session, so the average is over 8 targets of one
-    animal, not 16 animal and target cells.
-  - Each trial has one hand position in the data (fields 19 to 21 of the trial's text record), not
-    a position trace, so the MANOVA uses that value in place of the trial's mean over the 800 ms
-    hold (Fig. 2 legend). That it is the hold endpoint is read from the data (its target means
-    match Table 1 within its SDs); the data set does not say when it is sampled.
-  - V and NV are codes 4 and 7 of the record's field 14 under an assumed mapping; the test is
-    symmetric in V and NV, so the mapping does not change it.
[... 11 more lines not kept]
```

**Agent**

Reflow is cosmetic; I'll edit the record programmatically.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/rec.py <<'PYEOF'
import yaml
P='attempts/shi-2013-01.yaml'
d=yaml.safe_load(open(P))
O={o['claim']:o for o in d['outcomes']}
UNIT_DEV=("One unit per session, as the paper has one neuron per session (Table 1 legend, means over 219 "
  "sessions for monkey X; Results, Behavior, N = 343 sessions for 343 neurons). Which unit of a session "
  "the paper used is not stated; the first sorted unit (a) is assumed, a standard choice. With all 483 "
  "sorted units (a variant) the outcome would differ, so it rests on this assumption. Question for the "
  "paper's authors (methods_unavailable finding).")
def add_assumed(cid, extra_note):
    o=O[cid]; o['assumed']=True
    o['deviations']=[x for x in o.get('deviations',[])]+[UNIT_DEV]
    o['notes']=o['notes'].rstrip()+" "+extra_note
    # keep key order: put assumed after outcome
    keys=list(o.keys()); 
    new={}
    for k in ['claim','outcome','blocked_by','assumed']:
        if k in o: new[k]=o[k]
    for k in keys:
        if k not in new: new[k]=o[k]
    O[cid].clear(); O[cid].update(new)
add_assumed('hold-vision-main-effect', "With all units the scaled count (49) is just above the bound of 48.4.")
add_assumed('hold-subepochs', "Starting the window at least 250 ms after code 10 (a variant, against a possible saccade at its start) gives 35.7, 10.9, 7.5% and 28.8, 13.7, 5.0% (1 of 6 within), and 3 of 6 with all units.")
add_assumed('fig4-indx1-negative', "")
add_assumed('decoding-subepochs', "With the window starting at least 250 ms after code 10 (a variant), NV still differs (57.7 against 42.8%, paired P = 0.019, unpaired over targets P = 0.031). With all 483 units the NV difference (14.6 points) is not significant over targets (paired P = 0.072, unpaired P = 0.074) and only the test over bootstraps finds it.")
O['fig4-indx1-negative']['notes']=O['fig4-indx1-negative']['notes'].rstrip()
O['behavior-mean-position-sessions']['notes']+=(" With the V and NV labels shuffled within each session and target the MANOVA rejects in 5.7% of"
  " pairs, and the conditions are interleaved within sessions (median 39 runs of one condition"
  " against 41 for a random order), so neither the test nor slow drift accounts for the 16%. Within"
  " a session the five trials at a target spread by a median SD of 0.29, 0.29 and 0.19 cm in x, y, z.")
O['behavior-mean-position-sessions']['deviations'][1]=("Each trial has one hand position in the data (fields 19 to 21 of the trial's text record), not"
  " a position trace, so the MANOVA uses that value in place of the trial's mean over the 800 ms"
  " hold (Fig. 2 legend). That it is the hold endpoint is read from the data (its target means"
  " match Table 1 within its SDs); the data set does not say whether it is a hold mean or one sample."
  " No analog channel of the three sessions summarised follows the hand, so it cannot be checked"
  " against a trace.")
O['fig5-fano-factor']['notes']+=(" Keeping the 331 cells whose count means and variances lie within the plotted range of Fig. 5"
  " (0 to 80; a variant) gives 1.03 and 1.21 (P = 0.172), V within tolerance and NV not. Whether"
  " the criterion's outlier readings match the cells of Fig. 5 is asked of a reader"
  " (questions/shi-2013.yaml); the claim is tested as the file has it.")
O['fig6-decoding-vv']['notes']+=(" With target labels shuffled within each cell and condition, the decoder gives 16.1% (V) and"
  " 11.2% (NV) on average over 20 shuffles, near the nominal chance of 12.5%.")
O['decoding-v-better-than-nv']['notes']+=" With all units the unpaired test over targets gives P = 0.40."
O['eye-position-no-difference']['notes']=("The data set holds no documented eye position. The analog channels are named only AD01 to"
  " AD16, and the layout of the .plxAnaAD.dat files is undocumented. Read as 7 channels of 12-bit"
  " samples at 1 kHz at the end of each file, no channel of three sessions differs between targets in"
  " the hold (one-way ANOVA P 0.15 to 1.00) or correlates with the record's hand position beyond |r|"
  " = 0.25; most saturate at +/-2047, and one spans the 16-bit range, so the layout reading is at"
  " least partly wrong. The 24 field record (224 of the 359 sessions) ends with two numbers near (0,"
  " -1.8) that might be an eye position averaged over the hold, but nothing names them; their SD"
  " within a session (0.05 to 0.07) is below the tracker's 0.25 degree resolution, which a mean of"
  " about 100 samples could reach, so the spread does not settle what they are. Tested on them for"
  " the record only (trials pooled over sessions), no target shows a V against NV difference by"
  " MANOVA, and one shows one by Levene's test (90 degrees, second value, P = 0.012 centred on the"
  " mean, 0.28 on the median); 8.7% of session and target pairs differ by MANOVA.")
O['aborted-trials-nv']['notes']+=(" The part that does not depend on the mapping, more aborts as the window shrinks, holds for"
  " code 7 but not for code 4 (24.4% at 10 against 13.9% at 8), if field 1 is the window size.")
O['longer-hold-no-difference']['notes']=("On every completed trial the time from code 10 to code 12 is at least the trial's own record"
  " field 11 plus 28 ms (30,789 trials; the shortest intervals, 0.83 s, are on trials with field 11 ="
  " 800, and 0.93 and 1.06 s with 900 and 1,000), so field 11 is read as the minimum hold. No completed"
  " trial in the data set has a minimum hold of 1,200 ms or more (4 aborted trials do), so the sessions"
  " with the extended hold are not in it.")
O['fig4-indx1-means']['output']='claim:fig4-indx1-means'
O['fig6-decoding-nvnv']['output']='claim:fig6-decoding-nvnv'
O['fig6-decoding-cross']['output']='claim:fig6-decoding-cross'
O['hold-position-main-effect']['deviations'][1]=("The end of the hold is event code 12, read from the data: it follows code 10 (read as target"
  " offset) by 0.83 to 1.86 s, and on every completed trial by at least the record's minimum hold"
  " (field 11) plus 28 ms; the window is the 800 ms before it. In 11.6% of trials the window starts"
  " less than 250 ms after code 10.")
F=d['findings']
for f in F:
    if f['kind']=='data_missing':
        f['statement']=("The data descriptor gives 343 cells, 219 from monkey X and 124 from monkey B. Every session"
          " with a trial record has monkey X's target layout (targets about 9.2 cm apart horizontally and"
          " 7.4 cm vertically, middle row at y near -4 cm, depth near 10 cm, as in Table 1 for monkey X),"
          " in every month from October 2008 to November 2009; none has monkey B's square layout at a"
          " depth near 14.5 cm. Monkey B's data appear not to be in the data set.")
    if f['kind']=='selection_undocumented':
        f['statement']=("The data set holds 359 monkey X sessions with the paper's complete design (5 completed"
          " trials per target and condition) and 485 sorted units in them (83 sessions have 2 units, 21"
          " have 3 or 4), against the paper's 219 monkey X sessions and neurons, plus 47 sessions with an"
          " incomplete design. All were recorded on 92 days before the paper was submitted, and"
          " consecutive sessions of a day do not look like one neuron recorded again (median tuning"
          " correlation 0.04, against -0.01 across days). Which sessions and units the paper analysed"
          " is not documented.")
    if f['kind']=='metadata_insufficient' and f['statement'].startswith("The analog channels"):
        f['statement']=("The analog channels (in .plx and .plxAnaAD files) are named AD01 to AD16 without"
          " description, the descriptor does not say what they record, and it lists the variables of the"
          " .plxAnaAD.mat files but not the layout of the .plxAnaAD.dat files that hold the samples. No"
          " continuous arm or eye position could be identified; the trial record gives one hand position"
          " per trial.")
    if f['kind']=='methods_unavailable':
        f['statement']=f['statement'].rstrip()[:-1]+(", and which unit of a session was the session's"
          " neuron (the first sorted unit was assumed here). (6) Whether the hand position of Table 1"
          " and the MANOVA is a mean over the hold or one sample, and whether it is the one in the"
          " record's fields 19 to 21.")
yaml.safe_dump(d, open(P,'w'), sort_keys=False, width=96, allow_unicode=True)
PYEOF
python $TMPDIR/rec.py && grep -n "(5) Which sessions" attempts/shi-2013-01.yaml; tail -12 attempts/shi-2013-01.yaml
```

```
512:    or averages per trial values. (5) Which sessions and units form the 219 monkey X neurons, and
    and a minimum hold (record field 11) of 500 or 600 ms where the other sessions have 800 to 1,100
    ms, below the paper's 800 ms hold.
- kind: methods_unavailable
  statement: Questions for the paper's authors. (1) How movement onset was defined for the 500 ms
    movement epoch; this attempt used event code 8, which fits the cursor leaving the start window.
    (2) What a response pair is in the Spearman correlations between V and NV (each cell's mean rate
    at a target, adopted here, or single trials). (3) Which cells were outliers in Fig. 5 (the Fig.
    4 outliers were adopted here). (4) Whether CV2 pools the ISIs of a cell's trials (adopted here)
    or averages per trial values. (5) Which sessions and units form the 219 monkey X neurons, and
    which unit of a session was the session's neuron (the first sorted unit was assumed here). (6)
    Whether the hand position of Table 1 and the MANOVA is a mean over the hold or one sample, and
    whether it is the one in the record's fields 19 to 21.
```

**Agent**

Now the `verifications` block for round 1.

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/ver.py <<'PYEOF'
import yaml
P='attempts/shi-2013-01.yaml'
d=yaml.safe_load(open(P))
U="Population (B1, B5): added a data check of recording dates, geometry by month and same-day tuning; all 359 sessions predate submission, have monkey X's layout and are distinct neurons, so the extra sessions over the paper's 219 remain unexplained (selection_undocumented finding)."
R=[
("behavior-mean-position-sessions",True,"not_reproduced",
 "Cell 24 gives 16.1% under both readings, against 6.9 +/- 1.5%. Monkey X only (8 target percentages, not 16). This rests on record fields 19 to 21 being the trial mean over the hold, which was never checked (B2). In my simulation hotelling2 rejects 4.7% of the time under the null at n = 5 per group; whether V and NV trials are interleaved or blocked (drift would inflate the MANOVA) was not checked.",
 "Added the outputs asked for (B2): the MANOVA with V/NV labels shuffled within each session and target rejects in 5.7% of pairs; the conditions are interleaved (median 39 runs against 41 for a random order, with example sequences); within-session SDs of fields 19 to 21 per target are printed (median 0.29, 0.29, 0.19 cm). The analog channels were summarised and none follows the hand, so whether the record is a hold mean or one sample cannot be checked; this is stated in the deviation and asked of the paper's authors. Outcome unchanged."),
("behavior-variability-sessions",True,"not_reproduced",
 "Cell 26: no centre and averaging combination puts all three axes within tolerance. Mean-centred gives 8.1, 8.1 and 7.0%; median-centred gives 0.4 to 0.7%.","No change."),
("table1-endpoint-means",True,"partially_reproduced",
 "Cell 28: all 48 monkey X means are within the Table 1 SDs. But the largest V vs NV difference is 0.150 cm (135 degrees, y), above the 0.121 bound. Monkey B's 48 values cannot be tested.","No change."),
("table1-endpoint-sd",True,"not_reproduced",
 "Cell 30: 8.3% of SDs are within 10%. Data SDs are about 0.55 x Table 1 (0.32 to 0.67 cm against 0.50 to 1.28 cm).",
 "No change to the outcome. The within-session SDs asked for under B2 are printed in the behaviour section."),
("fig3-example-neuron",True,"not_reproduced",
 "Cell 32: 8 units peak at 225 degrees in both conditions with a position effect, but none matches. The closest has P_vis 0.364 and P_int 0.537. The paper's cell may be from monkey B, which the notebook could not find.","No change."),
("movement-epoch-tuning",True,"not_reproduced",
 "Cell 34: 187/359 (52.1%, 179 scaled to 343), against 139 +/- 13.9, with code 8 read as onset. Reading (b) was not run.",
 "No change. Reading (b) needs a continuous arm position; the analog channel summary now shown finds none that follows the hand."),
("hold-position-main-effect",True,"reproduced",
 "Cell 36: 141/359 (39.3%, 135 scaled to 343), against 135 +/- 13.5. The PSTH variant agrees (142). The analysis window was not shown to lie inside the hold (B3).",
 "Added a per-trial table of code 10 to code 12 against the trial's own field 11: on all 30,789 completed trials the interval is at least field 11 plus 28 ms, so the 800 ms window lies in the hold as the task timed it (the 0.832 s intervals are on trials with field 11 = 800). In 11.6% of trials the window starts less than 250 ms after code 10. Outcome unchanged."),
("hold-vision-main-effect",True,"reproduced",
 "49/359 (13.6%, 47 scaled to 343), against 44 +/- 4.4, and fewer than position. The all-units variant (49 scaled) falls just outside.",
 "Outcome kept, now marked as resting on the assumption of the first sorted unit per session, as all units fall just outside. "+U),
("hold-interaction",True,"reproduced","27/359 (7.5%, 26 scaled to 343), against 27 +/- 2.7 (reading a).","No change."),
("hold-subepochs",True,"not_reproduced",
 "Cell 38, main population: 1 of 6 values within tolerance. The all-units variant gets 3 of 6, which would be partial. The window may include the saccade in short trials, which most affects the first 400 ms and fits the high first-400 ms position count (B3).",
 "Outcome kept, marked as resting on the one-unit assumption. Added a variant that starts the window at least 250 ms after code 10: 35.7/10.9/7.5% and 28.8/13.7/5.0% (1 of 6), all units 3 of 6, so the window placement does not explain the difference."),
("hold-overall-effects",True,"partially_reproduced",
 "Cell 40: any position 40.4% (within 44 +/- 4.4) and any vision 18.7% (within 19 +/- 1.9), but both 13.1% (outside 11 +/- 1.1).","No change."),
("correlation-endpoint-datasets",True,"reproduced",
 "Cell 42, reading (a): r = 0.924 and 0.915, permutation P = 0.469. Reading (b) (single trials) finds a difference (P = 0.025). Data set 1 is built from the MANOVA, which did not reproduce (16% significant). The +/-0.093 tolerance on r is barely diagnostic.",
 "No change; the notes already say data set 1 is larger than the paper's would be."),
("fig4-indx1-negative",True,"partially_reproduced",
 "Main population: only all cells is within (77.8%); the other three groups are 68.4/75/75%, each 0.6 to 1.5 points below tolerance. Under the all-units variant all four are within (81.4/71.4/76.8/81.2). Group sizes are 98/44/20, against 110/38/27. Depends on V=4.",
 "Outcome kept, marked as resting on the one-unit assumption, since all units would reproduce it. On V=4: the notes show INDX1 is mostly negative under the other mapping too (80.5, 72.3, 74.4, 73.7%), the same outcome."),
("fig4-indx1-means",False,"not_reproduced",
 "Position Only is -12.0% (within), but Position/Vision is -24.2% against -31 +/- 3.1, and it is not the most negative group (all cells -24.9%).",
 "Kept as partially_reproduced, with the disagreement recorded. The claim has two parts: Position Only least negative at -13%, which holds in full (-12.0%, within tolerance, and the least negative group), and Position/Vision most negative at -31%, which fails. One part holding is the protocol's partial outcome. The output pointer now names this claim's own tag."),
("indx1-tuning-shift",True,"not_reproduced","Cell 47: 33/44 same or adjacent, against 22/38. The other cells average -27.6%, against -40 +/- 4.","No change."),
("indx2-means",True,"not_reproduced","Cell 49: no reading has all three means within tolerance. The closest is all units, outliers on INDX2, reading (c): -2.0/-14.1/-9.9.","No change."),
("rate-variance-nv-higher",False,"not_reproduced",
 "Cell 51: 46.4 vs 23.1 (spikes/s)^2, against 56 +/- 5.6 and 30 +/- 3. The direction and the about 2x ratio match.",
 "Kept as partially_reproduced, with the disagreement recorded. The claim is a trend (NV higher), and it is present in the same direction and ratio (2.0 against 1.9), in 67% of cells, with both means about 20% below the paper's: an effect present but weaker, the protocol's partial outcome."),
("fig5-fano-factor",True,"not_reproduced",
 "Cell 53, reading (a): FF 1.84 vs 3.19, P = 0.28. Reading (b): 0.98 vs 1.24, P = 0.02, but both FFs are outside tolerance. Reading (a) keeps variances up to 2188 while the paper's Fig. 5 axes stop at 80, which suggests the paper trimmed more heavily and the claims file's reading (a) may be wrong (B6).",
 "Added the question to questions/shi-2013.yaml for a reader, without changing the claim, and a variant with the 331 cells inside the plotted range (FF 1.03 and 1.21, P = 0.172; NV outside tolerance, not significant). Outcome unchanged."),
("cv2-larger-nv",True,"reproduced",
 "Cell 55, reading (a): median 0.737 NV vs 0.622 V, Kruskal-Wallis P = 0.024. Reading (b) gives P = 0.098. The direction rests on the V=4 assumption.","No change; already marked as resting on the mapping."),
("fig6-decoding-vv",True,"not_reproduced",
 "Cell 57: bootstrap 77.4 (a) and 73.3 (b), against 91.6 +/- 9. The unbootstrapped full population gives 87.5, which is within tolerance but is not a criterion reading. Leave-one-out Poisson decoding of random data gave 7.5% in my test, not 12.5% (B7).",
 "Added the decoder's chance level on these data, with target labels shuffled within each cell (20 shuffles): 16.1% (V) and 11.2% (NV), near 12.5%. Removed the unused branch of ppc.decode (B9); results are unchanged. Outcome unchanged."),
("fig6-decoding-nvnv",True,"not_reproduced","Bootstrap 63.7 (a) and 57.2 (b), against the lower bound of 63.9. A marginal miss. The full population gives 77.5.","Output pointer now names this claim's own tag. No other change."),
("decoding-v-better-than-nv",True,"reproduced",
 "Cell 58, main population: V > NV with P < 0.05 under all of (a), (b) and (c). Wholly dependent on the V=4 mapping: cell 58 shows the other mapping reverses it. A t-test over 200 bootstrap means always gives tiny P values (B8).",
 "No change to the outcome, already marked as resting on the mapping. The conclusion now also gives the all-units result, where only the test over bootstraps finds the difference."),
("fig6-decoding-cross",True,"reproduced","Bootstrap (a): 58.9 and 52.7, both within tolerance and both below V/V (77.4). Cross reading (b) also passes (62.1 and 56.8).","Output pointer now names this claim's own tag. No other change."),
("decoding-subepochs",True,"not_reproduced",
 "Cell 60: NV first 400 ms is 59.8 and last 400 ms is 42.8, paired t P = 0.007 and two-sample P = 0.017, so the first and last windows differ. The all-units variant passes under (a) and (c). The window placement may affect the first 400 ms (B3).",
 "Outcome kept, marked as resting on the one-unit assumption. Added the late-start window variant: NV still differs (57.7 against 42.8%, paired P = 0.019, unpaired P = 0.031)."),
("decoding-nonsignificant-cells",True,"not_reproduced","Cell 62, main population: V 24.7 and NV 12.5 are both outside tolerance, and V vs NV is significant (P = 0.00016).","No change."),
("eye-position-no-difference",True,"blocked",
 "No documented eye channel. The archive does hold .plxAnaAD files for 607 sessions (16 AD channels). The notebook says none looks like a fixation trace but does not show it, so I cannot confirm the block.",
 "Added a per-channel summary of the analog files of three sessions (range, SD, saturation, correlation with the record's hand position, target effect in the hold). Under the layout read from the files no channel differs between targets or follows the hand, and the layout is undocumented. Corrected the note on fields 22 and 23: their small spread does not exclude a mean eye position over the hold. Block kept."),
("aborted-trials-nv",True,"blocked",
 "The window size is undocumented (field 1 is a guess), and the V/NV labels were inferred from these same aborts, so the test would be circular. The mapping-free part (aborts rise as the window shrinks) could be tested only if field 1 is the window size. The cell 66 counts are non-monotonic for code 4 (13.9% at 8, 24.4% at 10, 3.6% at 12).",
 "Added the mapping-free part to the notes and conclusion: it holds for code 7 and not for code 4, if field 1 is the window size. Block kept."),
("longer-hold-no-difference",True,"blocked",
 "No completed trial has field 11 >= 1200 (cell 68). Field 11's meaning as minimum hold is itself contradicted by the event timing (B3): the shortest code 10 to code 12 interval is 0.832 s both in sessions with field 11 = 900 and with 1000. The verifier would block it as metadata_insufficient.",
 "Block kept as data_missing. The per-trial table now shows that no completed trial has a code 10 to code 12 interval shorter than its own field 11 plus 28 ms; the 0.832 s intervals are on trials with field 11 = 800 (some sessions change field 11 within the session), so the timing supports field 11 as the minimum hold."),
]
d['verifications']=[dict(date='2026-11-09', kind='agent',
  by='Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
  reviewed=('The first executed notebook with the conclusion cells and the summary removed, the helper module'
    ' (ppc.py) and the claims file, with the paper\'s full text under paper/. The verifier checked anova2 and'
    ' hotelling2 against statsmodels and decode on synthetic data, and took the claims from the claims file.'),
  results=[dict(claim=c, agrees=a, outcome=o, reason=r, response=s) for c,a,o,r,s in R])]
assert {r[0] for r in R}=={o['claim'] for o in d['outcomes']}
yaml.safe_dump(d, open(P,'w'), sort_keys=False, width=96, allow_unicode=True)
PYEOF
python $TMPDIR/ver.py && python tools/entry.py check entries/shi-2013 2>&1 | grep -v Warning | tail -3
```

Result: not kept, because it reads the paper's text.

**Agent**

Record passes the check. Checking the entry README for anything now out of date.

**Agent calls Bash**

```bash
cd  cat entries/shi-2013/README.md; grep -n -P "—|\brather\b" attempts/shi-2013-01.yaml questions/shi-2013.yaml entries/shi-2013/*.py entries/shi-2013/*.ipynb entries/shi-2013/README.md | head; python - <<'EOF'
import yaml,re
d=yaml.safe_load(open('attempts/shi-2013-01.yaml'))
EOF
grep -n -E "^[^#]*[a-z_]+: [^\"'>|].*: " questions/shi-2013.yaml | head
```

```
# Shi, Apker & Buneo (2013) from CRCNS ppc-1

Tests the findings of [Shi et al. (2013)](https://doi.org/10.1152/jn.00223.2012) on
[CRCNS ppc-1](https://doi.org/10.6080/K0CZ353K), which holds the sorted spikes and trial events of
area 5 recordings while monkeys held the arm at eight targets with or without vision of the arm
cursor. The notebook streams the data set's single `data.tar.gz` from the public CRCNS bucket.

| Claim | Outcome |
|---|---|
| Neurons with a position, vision or interaction effect in the hold (39%, 13%, 9%) | Reproduced |
| V and NV responses correlate alike whether endpoints differed or not | Reproduced (assumption) |
| CV2 larger in NV; decoding better in V; cross-condition decoding lower | Reproduced (two rest on an assumption) |
| Table 1 endpoint means; overall effect percentages; INDX1 mostly negative and its group means; rate variance higher in NV | Partially reproduced |
| Behavioural MANOVA and Levene percentages; Table 1 SDs; example neuron; movement epoch tuning; 400 ms subepochs; tuning shift; INDX2; Fano factor; decoding accuracies and subepochs; cells without effects | Not reproduced |
| Eye position; aborted trials; longer hold | Blocked |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The data set holds monkey X's sessions only (every session has monkey X's target layout), and
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/shi-2013; python - <<'EOF'
from pathlib import Path
p=Path("README.md"); s=p.read_text()
s=s.replace("| Neurons with a position, vision or interaction effect in the hold (39%, 13%, 9%) | Reproduced |",
            "| Neurons with a position, vision or interaction effect in the hold (39%, 13%, 9%) | Reproduced (vision count rests on an assumption) |")
s=s.replace("""trials. The event codes and the per-trial text record are undocumented and were read from the
data.""","""trials. The data set has 359 usable monkey X sessions against the paper's 219; one unit is taken
from each, as the paper has one neuron per session, and which unit is an assumption (the first
sorted). The event codes and the per-trial text record are undocumented and were read from the
data.""")
p.write_text(s)
p=Path("entry.yaml"); s=p.read_text(); s=s.replace("runtime_minutes: 12","runtime_minutes: 5"); p.write_text(s)
EOF
git diff --stat .; date -u
```

```
entries/shi-2013/README.md                |   6 +-
 entries/shi-2013/entry.yaml               |   2 +-
 entries/shi-2013/ppc.py                   |  74 ++++-
 entries/shi-2013/reproduce_shi_2013.ipynb | 528 +++++++++++++++++++++++++++---
 4 files changed, 552 insertions(+), 58 deletions(-)
Mon Nov  9 21:04:49 UTC 2026
```

**Agent**

Final clean run of the entry after the last edits.

**Agent calls Bash**

```bash
cd  python tools/entry.py all entries/shi-2013 > $TMPDIR/run2.log 2>&1; echo exit $?; tail -3 $TMPDIR/run2.log; python - <<'EOF'
import json
nb=json.load(open('executed/shi-2013/reproduce_shi_2013.ipynb'))
errs=[i for i,c in enumerate(nb['cells']) if c['cell_type']=='code' and any(o.get('output_type')=='error' for o in c.get('outputs',[]))]
print("error cells:", errs)
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if s.startswith('SUBMITTED') or s.startswith('# Chance level') or s.startswith('# Variant (verification round 1): the Fi'):
        print(''.join(''.join(o.get('text','')) for o in c['outputs'])[-400:])
EOF
git status --short; date -u
```

```
exit 0
Installed kernelspec registry-shi-2013 in executed/shi-2013/.venv/share/jupyter/kernels/registry-shi-2013
0 error(s)
pass  reproduce_shi_2013.ipynb  (325 s)
error cells: []
09-10               10.22                7.28         -4.23  10.22        19
2009-11                9.77                7.76         -4.22   9.94         1
consecutive sessions, same day: 267 pairs; tuning correlation median 0.04, above 0.8 in 3.4%; median |log rate ratio| 0.80
sessions on different days: 2000 pairs; tuning correlation median -0.01, above 0.8 in 1.1%; median |log rate ratio| 1.03

main, cells within the plotted range 0 to 80: n 331 of 359; FF V 1.027, NV 1.205; permutation P two-sided 0.172, one-sided 0.081

shuffled labels, V/V: mean accuracy 16.1% (range 5.0 to 37.5); nominal chance 12.5%
shuffled labels, NV/NV: mean accuracy 11.2% (range 2.5 to 22.5); nominal chance 12.5%

 M attempts/shi-2013-01.yaml
 M entries/shi-2013/README.md
 M entries/shi-2013/entry.yaml
 M entries/shi-2013/ppc.py
 M entries/shi-2013/reproduce_shi_2013.ipynb
[... 21 more lines not kept]
```

**Agent**

I revised the attempt in reply to the round-1 verification. No outcome changed. The entry re-ran cleanly with `python tools/entry.py all entries/shi-2013` (passes, 325 s), and `entry.py check` reports 0 errors. Nothing is committed.

**Outcomes**
- **No outcome changed.** Every number in the conclusions matches the re-run.
- **Disagreements kept and recorded:**
  - `fig4-indx1-means` stays partially reproduced: the Position Only part holds in full and the Position/Vision part fails. The verifier says not reproduced.
  - `rate-variance-nv-higher` stays partially reproduced: NV is higher in the same direction and about the same 2× ratio, but both means are about 20% low. The verifier says not reproduced.
- **Four outcomes are now marked as resting on an assumption:** `hold-vision-main-effect`, `hold-subepochs`, `fig4-indx1-negative` and `decoding-subepochs`. The assumption is taking the first sorted unit from each session, and using all 483 units would change each of these outcomes. The paper supports one neuron per session (Table 1 legend, and "N = 343 sessions" for 343 neurons), but not which unit.

**Outputs the verifier asked for, now in the notebook**
- **Population (B1):**
  - All 359 sessions were recorded from October 2008 to November 2009, on 92 days, before the paper was submitted (14 March 2012).
  - Their target layout is monkey X's in every month.
  - Consecutive sessions on the same day have unrelated tuning (median correlation 0.04, against −0.01 across days), so they are different neurons.
  - Why there are about 140 more sessions than the paper's 219 is still unexplained.
- **Hold timing (B3):** on all 30,789 completed trials, the time from code 10 to code 12 is at least the trial's own field 11 plus 28 ms. The verifier's 0.832 s intervals all come from trials with field 11 = 800. So the 800 ms window sits inside the hold. In 11.6% of trials it starts less than 250 ms after code 10; starting it later leaves `hold-subepochs` and `decoding-subepochs` unchanged.
- **Hand position (B2):**
  - V and NV trials are interleaved: the median session has 39 runs of one condition, against 41 expected for a random order.
  - With the V/NV labels shuffled, the MANOVA rejects in 5.7% of pairs, so the test is calibrated and the 16% is real.
  - Within a session, the five trials at a target spread by a median SD of 0.29, 0.29 and 0.19 cm in x, y and z.
- **Analog files:** I read their layout from the files themselves (it is undocumented) and summarised the channels of three sessions. No channel differs between targets during the hold or follows the hand (|r| ≤ 0.25). One channel spans a range a 12-bit converter cannot give, so my reading of the layout is at least partly wrong; the notebook says so. The eye-position block stays. I also corrected its note: the small spread of record fields 22–23 does not rule out an averaged eye position.
- **Other checks:**
  - The per-session clock check holds in 153 of 359 sessions; the other 206 are named as not established.
  - The decoder's chance level on shuffled labels is 16.1% (V) and 11.2% (NV), near the 12.5% used.
  - A Fano-factor variant keeping only the 331 cells within Fig. 5's plotted range gives 1.03 against 1.21, P = 0.17: still not reproduced.
  - The non-monotonic abort rates for code 4 are now in the `aborted-trials-nv` notes.

**Other corrections**
- I added `questions/shi-2013.yaml`, asking a reader whether the Fano-factor outlier readings match Fig. 5's 0 to 80 axes. The claim itself is unchanged.
- I removed an unused branch from `ppc.decode`; results are identical.
- The `output` tags of three outcomes now point at the claim's own tag.
- New methods questions for the paper's authors: which unit per session they used, and whether the recorded hand position is a mean over the hold.
- The `verifications` block for round 1 is recorded in `attempts/shi-2013-01.yaml`.

**Not done**
- `longer-hold-no-difference` stays blocked as `data_missing`, not the verifier's `metadata_insufficient`, because the per-trial timing supports reading field 11 as the minimum hold.
- I could not settle whether the hand position in fields 19–21 is a hold mean or a single sample: no position trace was found to check it against.

Several untracked files appeared in the repo root during the run (`.bashrc`, `.profile`, `.idea`, `.vscode`, `.mcp.json`, and others) along with a `scripts` folder. I did not create them, and they should be left out of the commit. The `tools/` changes were already there when the run started.

## End of run

74 turns, 29 minutes, $4.99 at API prices, result: success.
