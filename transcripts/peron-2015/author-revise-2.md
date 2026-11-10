# peron-2015 · author-revise-2 · run 42710213375

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/peron-2015/verifier-2-report.md; ls entries/peron-2015 entries/peron-2015/*;
```

```
Mon Nov  9 22:24:03 UTC 2026
**Verifier report, round 2: peron-2015-01 (Peron et al. 2015, CRCNS ssc-1)**

**1. Outcomes**

The claims file has 43 claims, and the attempt record has 43 outcomes covering the same IDs. One is reproduced, one is not_reproduced, and 41 are blocked: 22 data_missing, 18 metadata_insufficient and 1 methods_underspecified.

- **results-trials-per-session: reproduced.** I agree. Cell 28 gives 290.2 pooled and 272.5 as the mean of per-mouse means, both inside [174, 316]. It is weak evidence (5 sessions from 3 of 8 mice), and the record now says so.
- **results-whisking-amplitude: not_reproduced.** I now agree; in round 1 I said partially_reproduced. In cell 33 every listed reading is still outside [42.2, 68.8] after removing only the artefacts: (a) 72.4 or 71.9, (b) 28.6 to 29.0, (c) 26.6. The criterion's "within tolerance under one reading" rule therefore gives not_reproduced. The miss is narrow, though:
  - Reading (a) falls steadily as the threshold drops: 74.1 at 88°, 72.4 at 85°, 70.3 at 80°, 67.4 at 70°.
  - The mean of per-mouse medians is 68.6, which is inside.
  - Multi-sample jumps are not removed by either artefact mask (see section 3).
- **The 41 blocked claims:** I agree with each one. Cell 7 now shows that no identifier or description field carries a layer, class or column label, so the M6 blocks stand. For methods-event-detection I accept methods_underspecified over my round-1 data_missing, given the protocol rule the record cites. Either way the outcome is blocked.
- **Assumptions:** the record has no `assumed: true` entries. The choices the whisking outcome rests on are all stated as deviations: the 6–30 Hz band, valid whisker trials only, and the poleInReach epoch. None of them changes the outcome (cell 31 shows all bands; cell 33 shows the artefact variants). They are reasonable.
- **Claims file:** I found no misreading. Its note that the degree values are "garbled in the extraction" is only partly true. Only the degree sig
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^## Author/,/^## Verifier/p' docs/protocol.md | head -300; grep -n "Hand over\|round 2\|proposed" docs/protocol.md
```

```
## Author

The workflow puts the paper under `paper/`, as for the reader. Read it to
understand the claims, their data and their figures. The claims file still
decides what is tested: do not change a claim's statement, expected values or
criterion. A method detail the claims file lacks is taken from the paper
(step 6).

**Time.** An author run is stopped five hours after it starts, and whatever
is not recorded by then is lost. The prompt says when the run started and the
time by which to finish. Check the clock (`date -u`) between steps. When that
time comes, stop analysing and finish: record each claim not yet tested as
blocked, `too_large` where the computation is what stopped it, saying how far
it got, then write the attempt record and run the entry's checks. A record
with some claims blocked for time is worth more than a run that is cut off.

### 1. Establish what can be tested

Do this before any analysis.

[... 292 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 480,560p docs/protocol.md; ls attempts | grep peron; ls questions | grep peron
```

```
outcomes. These are for the data owner and the archive. The kinds are
  `metadata_error`, `data_missing`, `identifier_missing`,
  `selection_undocumented`, `methods_unavailable`, `format_error` (files that
  break their own format, such as unsorted spike times), `code_mismatch`
  (published code that disagrees with the paper or the data),
  `paper_inconsistency` (the paper disagrees with itself),
  `metadata_insufficient` (a variable without a description or a needed
  mapping) and `other`.
- **`provenance`**: who is accountable, and for an agent the harness, model
  and this protocol's version.

If any outcome is `not_reproduced` or `partially_reproduced`, the entry's
`README.md` and the notebook's summary carry this sentence: "A failure to
reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method."

### 6. Hand over for verification

Do not verify your own attempt. Give the verifier:

[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2015; python - <<'EOF'
import json
nb=json.load(open('reproduce_peron_2015.ipynb'))
for i,c in enumerate(nb['cells']):
    if i in (0,6) or i>=29:
        print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'))
        print(''.join(c['source']))
EOF
wc -l ssc1.py; ls ../../executed/peron-2015/ 2>/dev/null
```

```
Exit code 2
===== 0 markdown None
# Reproducing Peron et al. (2015) from CRCNS ssc-1

Paper. Peron SP, Freeman J, Iyer V, Guo C, Svoboda K (2015). A cellular resolution map of barrel
cortex activity during tactile behavior. *Neuron* 86:783-799.
[doi:10.1016/j.neuron.2015.03.027](https://doi.org/10.1016/j.neuron.2015.03.027). The claims file
(`claims/peron-2015.yaml`) was written from the version of record with its Supplemental Information.

Data set. [CRCNS ssc-1](https://doi.org/10.6080/K0TB14TN), read anonymously from the public S3
bucket `crcnsarchive` under `ssc-1/`. CRCNS data sets are not versioned (docs/archives.md, "CRCNS"),
so the version recorded is `unversioned`; the paper cites the data set's DOI and no version, and
the bucket holds one copy (no `live/` or `old/` folder). A later change is detectable from the MD5
sums of the files read, taken from the data set's `checksums.md5` and checked against the bytes
read:

| File | MD5 |
|---|---|
| an197522_2013_03_08/an197522_2013_03_08_session.mat | 1d4bd20b7bd82a3bb41b0655d45998c0 |
| an197522_2013_03_10/an197522_2013_03_10_session.mat | f0dfe39427828d0b1f77f0bed35412d6 |
[... 118 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2015; python - <<'EOF'
import json
nb=json.load(open('reproduce_peron_2015.ipynb'))
for i,c in enumerate(nb['cells']):
    if i in (30,31,32,33):
        print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'))
        print(''.join(c['source']))
EOF
```

```
===== 30 markdown None
## results-whisking-amplitude

> The task elicited larger amplitude whisker movements than similar two-position tasks, 55.5 ±
> 13.3 degrees (mean ± SD, n = 8 mice) against about 20 degrees.

Criterion: readings (a) per-trial range of whisker angle (maximum minus minimum) over the trial,
(b) the same over the sample epoch, (c) the peak Hilbert amplitude of whisking per trial; each
averaged per mouse, then over mice; reproduced when the mean over mice is within 55.5 ± 13.3 under
one reading.

Method details. The sample epoch is the pole-in-reach interval of the data set's `poleInReach`
series (the paper's "sample epoch (pole in reach)"). Reading (c) follows the Supplemental
Experimental Procedures ("the amplitude of whisking, obtained using the Hilbert transform (as
described previously; see (Huber et al., 2012))"); the band used to isolate whisking is not given,
and 6 to 30 Hz is assumed (helper docstring), with 4 to 30 and 8 to 25 Hz shown. Only trials the
data set lists as valid whisker trials are used.
===== 31 code ['claim:results-whisking-amplitude']
rows = []
for s in sessions:
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2015; grep -n "def \|spike\|limit\|unwrap" ssc1.py | head -80
```

```
72:def list_bucket(prefix: str = "ssc-1/") -> list[tuple[str, int]]:
92:def _read_struct(name: str):
103:def _list(x):
112:def _events(s, key):
119:def load_session(name: str) -> dict:
240:ARTEFACT_LIMIT = 85.0   # degrees; |angle| above this is near the +/-90 degree limit of the tracker
245:def artefact_masks(ang: np.ndarray) -> dict:
248:    ``limit``: |angle| > ARTEFACT_LIMIT (85 degrees). The angle is reported within +/-90 degrees,
249:    and isolated samples jump to the limits (for example 87.3, 37.8, -89.2, 41.7 degrees on
252:    ``spike``: samples more than SPIKE_DEV (20 degrees) from the median of the 5 samples around
259:    return {"limit": np.abs(ang) > ARTEFACT_LIMIT, "spike": dev > SPIKE_DEV, "dev": dev}
262:def _fill(x: np.ndarray, drop: np.ndarray) -> np.ndarray:
270:def whisking_amplitudes(sess: dict, band=(6.0, 30.0), limits=(70.0, 80.0, 85.0, 88.0),
271:                        spike_devs=(10.0, 20.0, 40.0)) -> dict:
281:    (a) and (b) without the samples of each artefact mask (``artefact_masks``; ``_limit`` and
282:    ``_spike``), and (a) with other thresholds (``range_trial_limit<L>``, ``range_trial_spike<D>``);
283:    (a) after unwrapping the angle with a 180 degree period and removing spikes
284:    (``range_trial_unwrap_spike``), and the number of wraps (steps over 90 degrees) per trial;
304:    def rng(v):
325:        lim, spk = masks["limit"][s0:e0], masks["spike"][s0:e0]
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2015; sed -n 230,365p ssc1.py; sed -n 395,475p ssc1.py
```

```
"id_strs_detailed": [str(x) for x in _list(v.idStrsDetailed)],
            "descr_keys": [str(x) for x in _list(d.keyNames)],
            "roi_array_fields": list(roi_defs[0]._fieldnames) if roi_defs else [],
            "roi_fields": list(_list(roi_defs[0].rois)[0]._fieldnames) if roi_defs else [],
            "plane_fields": list(_list(v.imagingPlane)[0]._fieldnames),
        })
    out["subvolumes"] = subs
    return out


ARTEFACT_LIMIT = 85.0   # degrees; |angle| above this is near the +/-90 degree limit of the tracker
SPIKE_DEV = 20.0        # degrees from the 5-sample running median; a one- or two-sample jump
EDGE_S = 0.2            # seconds left out at each end of a trial for the edge-trimmed Hilbert peak


def artefact_masks(ang: np.ndarray) -> dict:
    """Samples of the whisker angle that look like tracking errors, two ways.

    ``limit``: |angle| > ARTEFACT_LIMIT (85 degrees). The angle is reported within +/-90 degrees,
    and isolated samples jump to the limits (for example 87.3, 37.8, -89.2, 41.7 degrees on
[... 197 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2015; sed -n 1,70p ssc1.py; cat entry.yaml; ls ../../executed/peron-2015
```

```
Exit code 2
"""Loading and measures for CRCNS ssc-1 (Peron, Freeman, Iyer, Guo & Svoboda 2015).

The data set holds one MATLAB v5 structure ``s`` per session
(``<animal>_<date>/<animal>_<date>_session.mat``), described in the data set's
docs/crcns_ssc-1_data_description.pdf (version 0.8). Files are streamed from the
public S3 bucket ``crcnsarchive`` (docs/archives.md, "CRCNS"); nothing is
written to disk. Each file is read whole into memory (100 to 200 MB) and
reduced at once to the arrays the analysis uses.

Parameters and where they come from:

- Trial epochs. The pole-in-reach interval of each trial is the data set's
  ``poleInReach`` event series (start and end), and the reward cue its
  ``rewardCue`` series. The sample epoch is the pole-in-reach interval, as the
  paper defines it ("a 1 s sample epoch (pole in reach)", claims file opening
  comment; "remained in place for the 1 s sample epoch", Supplemental Experimental
  Procedures, Behavioral training; data description, "Imaging and behavior"). The
  Figure 1C legend gives the sample epoch as "1 to 2 s"; the data's pole-in-reach
  intervals (0.84 to 1.18 s in the median) are used as they are, so the difference
[... 75 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2015; time python -c "
import ssc1,resource
s=ssc1.load_session('an229717_2013_12_01')
import pickle,os
w=s['whisker']; import numpy as np
np.savez(os.environ['TMPDIR']+'/w.npz', t=w['time'], tr=w['trial'], ang=w['angle'], valid=s['valid_whisker_trials'])
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
"
```

```
Exit code 1
Traceback (most recent call last):
  File "<string>", line 2, in <module>
    import ssc1,resource
  File "entries/peron-2015/ssc1.py", line 40, in <module>
    import fsspec
ModuleNotFoundError: No module named 'fsspec'

real	0m0.037s
user	0m0.033s
sys	0m0.004s
```

**Agent calls Bash**

```bash
cd  ls -a; ls .venv* venvs 2>/dev/null | head; grep -n "venv\|def cmd_run\|uv " tools/entry.py | head -20
```

```
.
..
.bash_profile
.bashrc
.claude
.env
.env.development
.env.development.local
.env.local
.env.production
.env.production.local
.env.test
.env.test.local
.git
.gitconfig
.github
.gitignore
.gitmodules
.idea
.mcp.json
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd  uv venv --quiet --python 3.13 $TMPDIR/venv && uv pip install --quiet --python $TMPDIR/venv/bin/python -r entries/peron-2015/requirements.lock.txt 2>&1 | tail -3; cd entries/peron-2015; time $TMPDIR/venv/bin/python -c "
import ssc1,resource,os
import numpy as np
s=ssc1.load_session('an229717_2013_12_01')
w=s['whisker']
np.savez(os.environ['TMPDIR']+'/w.npz', t=w['time'], tr=w['trial'], ang=w['angle'], valid=s['valid_whisker_trials'])
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
"
```

```
0.47236

real	0m6.539s
user	0m4.505s
sys	0m0.437s
```

**Agent calls Bash**

```bash
cd entries/peron-2015; $TMPDIR/venv/bin/python -c "
import numpy as np, os
from scipy.ndimage import median_filter
d=np.load(os.environ['TMPDIR']+'/w.npz'); ang=d['ang']; tr=d['tr']
bad=~np.isfinite(ang); ang[bad]=np.interp(np.flatnonzero(bad),np.flatnonzero(~bad),ang[~bad])
df=np.abs(np.diff(ang))
print('diff pct', np.percentile(df,[50,90,99,99.9,99.99]).round(2))
for th in [5,8,10,15,20,30,50]: print(th,(df>th).sum())
valid=set(d['valid'].tolist())
bounds=np.flatnonzero(np.diff(tr))+1; st=np.r_[0,bounds]; en=np.r_[bounds,len(tr)]
for W in [5,7,11,21,41]:
  dev=np.abs(ang-median_filter(ang,size=W,mode='nearest'))
  r=[]
  for s0,e0 in zip(st,en):
    if int(tr[s0]) not in valid or e0-s0<500: continue
    x=ang[s0:e0]; k=dev[s0:e0]<=20
    r.append(x[k].max()-x[k].min())
  r=np.array(r); print(W, len(r), r.mean().round(1), np.median(r).round(1))
"
```

```
diff pct [  0.32   2.17   8.34  34.72 171.97]
5 16415
8 7412
10 5035
15 2568
20 1706
30 940
50 375
5 183 91.6 87.2
7 183 90.5 87.2
11 183 86.0 87.2
21 183 82.8 86.7
41 183 70.7 70.4
```

**Agent calls Bash**

```bash
cd entries/peron-2015; cat > $TMPDIR/proto.py <<'EOF'
import numpy as np, os
d=np.load(os.environ['TMPDIR']+'/w.npz'); ang=d['ang']; tr=d['tr']
bad=~np.isfinite(ang); ang[bad]=np.interp(np.flatnonzero(bad),np.flatnonzero(~bad),ang[~bad])
def jumps(x,J,N):
    dx=np.diff(x); big=np.flatnonzero(np.abs(dx)>J)
    m=np.zeros(len(x),bool)
    for a,b in zip(big[:-1],big[1:]):
        if b-a<=N and np.sign(dx[a])!=np.sign(dx[b]): m[a+1:b+1]=True
    return m
valid=set(d['valid'].tolist())
bounds=np.flatnonzero(np.diff(tr))+1; st=np.r_[0,bounds]; en=np.r_[bounds,len(tr)]
for J in [15,20,30,50]:
  for N in [5,10,25,50]:
    r=[];nm=0
    for s0,e0 in zip(st,en):
      if int(tr[s0]) not in valid or e0-s0<500: continue
      x=ang[s0:e0]; m=jumps(x,J,N); nm+=m.sum()
      k=~m; r.append(x[k].max()-x[k].min())
    r=np.array(r); print(J,N, nm, r.mean().round(1), np.median(r).round(1))
EOF
$TMPDIR/venv/bin/python $TMPDIR/proto.py
```

```
15 5 1630 86.6 87.2
15 10 2171 85.3 86.9
15 25 3750 84.8 86.7
15 50 7211 84.5 86.7
20 5 1106 86.7 87.2
20 10 1522 85.4 86.9
20 25 2681 85.0 86.7
20 50 5168 84.7 86.7
30 5 690 86.8 87.2
30 10 979 85.5 86.9
30 25 1583 85.3 86.9
30 50 2856 85.2 86.9
50 5 350 87.1 87.2
50 10 524 86.0 87.2
50 25 838 86.0 87.2
50 50 1855 86.0 87.2
```

**Agent calls Bash**

```bash
cd entries/peron-2015; $TMPDIR/venv/bin/python - <<'EOF'
import re
p='ssc1.py'; s=open(p).read()
s=s.replace('''EDGE_S = 0.2            # seconds left out at each end of a trial for the edge-trimmed Hilbert peak
''','''EDGE_S = 0.2            # seconds left out at each end of a trial for the edge-trimmed Hilbert peak
JUMP_STEP = 30.0        # degrees in one 2 ms sample (15,000 degrees/s); a step no whisker makes
JUMP_SAMPLES = 25       # samples (50 ms) within which a jump must return to be a multi-sample error
''')
s=s.replace('''def _fill(x''','''def jump_mask(x: np.ndarray, step: float = JUMP_STEP, n: int = JUMP_SAMPLES) -> np.ndarray:
    """Samples between a step of more than ``step`` degrees and an opposite step within ``n`` samples.

    Multi-sample tracking errors (round-2 verifier): the angle jumps away and back after three or
    more samples (for example -24.1, 72.8, 72.8, 72.1, -23.1), which the 5-sample spike mask misses.
    A step of 30 degrees in one 2 ms sample is 15,000 degrees/s, several times the fastest whisker
    movement in the data (the 99th percentile of the step is about 8 degrees); the angle must come back
    within 50 ms, less than half a whisk cycle at 10 Hz. Both are standard choices, not from the paper,
    and the notebook shows other values. Angles that wrap past 90 degrees and back are also
    caught, so this mask also drops the part of a protraction beyond 90 degrees.
    """
    dx = np.diff(x)
    big = np.flatnonzero(np.abs(dx) > step)
    m = np.zeros(len(x), bool)
    for a, b in zip(big[:-1], big[1:]):
        if b - a <= n and np.sign(dx[a]) != np.sign(dx[b]):
            m[a + 1:b + 1] = True
    return m


def _fill(x''')
s=s.replace('''                        spike_devs=(10.0, 20.0, 40.0)) -> dict:''','''                        spike_devs=(10.0, 20.0, 40.0), median_windows=(11, 21),
                        jumps=((20.0, 10), (20.0, 25), (30.0, 10), (30.0, 25), (30.0, 50), (50.0, 25))) -> dict:''')
s=s.replace('''    either mask are replaced by interpolation (``hilbert_peak_trim_clean``); the number of samples
    of each mask in the trial.
''','''    either mask are replaced by interpolation (``hilbert_peak_trim_clean``); the number of samples
    of each mask in the trial.
    For the multi-sample errors the round-2 verifier found: (a) without samples more than SPIKE_DEV
    from a running median of ``median_windows`` samples (``range_trial_med<W>``, which removes
    jumps of up to (W - 1) / 2 samples), (a) without the samples of ``jump_mask`` for each
    (step, samples) pair (``range_trial_jump<step>_<n>``), and (a) without the samples of every
    mask together (limit, spike, 21-sample median, default jump mask: ``range_trial_all``).
''')
s=s.replace('''        for D in spike_devs:
            e[f"range_trial_spike{D:g}"] = rng(x[dev[s0:e0] <= D])
''','''        for D in spike_devs:
            e[f"range_trial_spike{D:g}"] = rng(x[dev[s0:e0] <= D])
        med = {}
        for W in median_windows:
            med[W] = np.abs(x - median_filter(x, size=W, mode="nearest")) > SPIKE_DEV
            e[f"range_trial_med{W}"] = rng(x[~med[W]])
        for J, N in jumps:
            e[f"range_trial_jump{J:g}_{N}"] = rng(x[~jump_mask(x, J, N)])
        jm = jump_mask(x)
        e["n_jump"] = int(jm.sum())
        e["range_trial_all"] = rng(x[~(lim | spk | jm | med[max(median_windows)])])
''')
open(p,'w').write(s)
EOF
grep -n "jump" ssc1.py | head
```

```
241:SPIKE_DEV = 20.0        # degrees from the 5-sample running median; a one- or two-sample jump
244:JUMP_SAMPLES = 25       # samples (50 ms) within which a jump must return to be a multi-sample error
251:    and isolated samples jump to the limits (for example 87.3, 37.8, -89.2, 41.7 degrees on
255:    them, i.e. jumps that last one or two samples (4 ms) and return; this keeps smooth excursions.
264:def jump_mask(x: np.ndarray, step: float = JUMP_STEP, n: int = JUMP_SAMPLES) -> np.ndarray:
267:    Multi-sample tracking errors (round-2 verifier): the angle jumps away and back after three or
294:                        jumps=((20.0, 10), (20.0, 25), (30.0, 10), (30.0, 25), (30.0, 50), (50.0, 25))) -> dict:
314:    jumps of up to (W - 1) / 2 samples), (a) without the samples of ``jump_mask`` for each
315:    (step, samples) pair (``range_trial_jump<step>_<n>``), and (a) without the samples of every
316:    mask together (limit, spike, 21-sample median, default jump mask: ``range_trial_all``).
```

**Agent calls Bash**

```bash
cd entries/peron-2015; $TMPDIR/venv/bin/python - <<'EOF'
s=open('ssc1.py').read()
s=s.replace('''        "angle_abs_over_85": float(np.mean(np.abs(w["angle"]) > 85)),
''','''        "angle_abs_over_85": float(np.mean(np.abs(w["angle"]) > 85)),
        # Step between successive samples (degrees per 2 ms), percentiles 50, 99, 99.9, 99.99.
        "step_pct": np.nanpercentile(np.abs(np.diff(w["angle"])), [50, 99, 99.9, 99.99]).tolist(),
''')
open('ssc1.py','w').write(s)
EOF
time $TMPDIR/venv/bin/python - <<'EOF'
import ssc1, numpy as np, pandas as pd, resource, time
t0=time.time()
s=ssc1.reduce_session(ssc1.load_session('an229717_2013_12_01'))
print(time.time()-t0, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
w=s['whisking'][(6.0,30.0)]
print(s['whisker_summary']['step_pct'])
for k in w:
    if k.startswith('range_trial') or k.startswith('n_'): print(k, np.nanmean(w[k]).round(1), np.nanmedian(w[k]).round(1))
EOF
```

```
entries/peron-2015/ssc1.py:424: RuntimeWarning: Mean of empty slice
  pop = np.nanmean(sv["dff"], 0)
3.803724765777588 0.465656
[0.31909381685880245, 8.338385157590471, 34.47907387325418, 171.97251941893992]
range_trial 99.2 87.2
range_trial_limit 92.8 87.2
range_trial_spike 91.6 87.2
range_trial_unwrap_spike 104.6 87.2
n_wrap 1.5 0.0
n_limit 2.3 0.0
n_spike 4.4 3.0
range_trial_limit70 79.5 86.3
range_trial_limit80 87.2 87.2
range_trial_limit85 92.8 87.2
range_trial_limit88 97.5 87.2
range_trial_spike10 91.0 87.2
range_trial_spike20 91.6 87.2
range_trial_spike40 91.8 87.2
range_trial_med11 86.1 87.2
range_trial_med21 82.9 86.7
[... 12 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2015; time $TMPDIR/venv/bin/python - <<'EOF' 2>/dev/null
import ssc1, numpy as np, pandas as pd, pickle, os
ss=ssc1.load_all()
pickle.dump(ss, open(os.environ['TMPDIR']+'/ss.pkl','wb'))
allw=pd.concat([pd.DataFrame({"mouse": s["meta"]["animalID"], **{k: v for k, v in s["whisking"][(6.0, 30.0)].items() if k != "fs"}}) for s in ss])
ks=[k for k in allw.columns if k.startswith('range_trial')]
m=allw.groupby('mouse')[ks].mean(); md=allw.groupby('mouse')[ks].median()
out=m.T.round(1); out['mean']=m.mean().round(1); out['medmean']=md.mean().round(1)
print(out.to_string())
for s in ss: print(s['name'], np.round(s['whisker_summary']['step_pct'],1))
EOF
```

```
mouse                     an197522  an229717  an229719  mean  medmean
range_trial                   70.6      99.2      54.2  74.7     68.6
range_trial_limit             70.1      92.8      54.1  72.4     68.6
range_trial_spike             70.1      91.6      54.1  71.9     68.6
range_trial_unwrap_spike      71.6     104.6      54.8  77.0     68.6
range_trial_limit70           68.9      79.5      53.9  67.4     68.3
range_trial_limit80           69.6      87.2      54.1  70.3     68.6
range_trial_limit85           70.1      92.8      54.1  72.4     68.6
range_trial_limit88           70.5      97.5      54.2  74.1     68.6
range_trial_spike10           70.0      91.0      54.1  71.7     68.6
range_trial_spike20           70.1      91.6      54.1  71.9     68.6
range_trial_spike40           70.3      91.8      54.2  72.1     68.6
range_trial_med11             69.7      86.1      54.0  69.9     68.6
range_trial_med21             69.0      82.9      53.9  68.6     68.4
range_trial_jump20_10         70.0      85.4      54.1  69.8     68.5
range_trial_jump20_25         69.9      85.0      54.1  69.7     68.4
range_trial_jump30_10         70.0      85.5      54.1  69.9     68.5
range_trial_jump30_25         70.0      85.3      54.1  69.8     68.5
range_trial_jump30_50         70.0      85.2      54.1  69.8     68.5
range_trial_jump50_25         70.1      86.0      54.2  70.1     68.6
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2015; $TMPDIR/venv/bin/python - <<'EOF'
s=open('ssc1.py').read()
s=s.replace('''        e["range_trial_all"] = rng(x[~(lim | spk | jm | med[max(median_windows)])])
''','''        e["n_med"] = int(med[max(median_windows)].sum())
        e["range_trial_lsj"] = rng(x[~(lim | spk | jm)])
        e["range_trial_all"] = rng(x[~(lim | spk | jm | med[max(median_windows)])])
''')
s=s.replace('''    mask together (limit, spike, 21-sample median, default jump mask: ``range_trial_all``).
''','''    mask together (limit, spike, 21-sample median, default jump mask: ``range_trial_all``), and
    of all but the 21-sample median (``range_trial_lsj``), with the counts ``n_jump`` and ``n_med``.
''')
open('ssc1.py','w').write(s)
EOF
$TMPDIR/venv/bin/python - <<'EOF' 2>/dev/null
import ssc1, numpy as np, pandas as pd, pickle, os
ss=[ssc1.reduce_session(ssc1.load_session(n)) for n in ssc1.SESSIONS]
pickle.dump(ss, open(os.environ['TMPDIR']+'/ss.pkl','wb'))
allw=pd.concat([pd.DataFrame({"mouse": s["meta"]["animalID"], **{k: v for k, v in s["whisking"][(6.0, 30.0)].items() if k != "fs"}}) for s in ss])
for k in ['range_trial_lsj','range_trial_all']:
    m=allw.groupby('mouse')[k].mean(); print(k, m.round(1).to_dict(), round(m.mean(),2))
clean=allw[(allw.n_limit==0)&(allw.n_spike==0)&(allw.n_jump==0)&(allw.n_med==0)]
g=clean.groupby('mouse').range_trial
print('clean trials', g.size().to_dict(), g.mean().round(1).to_dict(), g.median().round(1).to_dict(), round(g.mean().mean(),1))
c2=allw[(allw.n_limit==0)&(allw.n_spike==0)&(allw.n_jump==0)]
g=c2.groupby('mouse').range_trial
print('clean lsj', g.size().to_dict(), g.mean().round(1).to_dict(), round(g.mean().mean(),1))
print(allw.groupby('mouse').n_med.apply(lambda n:(n>0).sum()).to_dict(), allw.groupby('mouse').n_jump.apply(lambda n:(n>0).sum()).to_dict())
EOF
```

```
range_trial_lsj {'an197522': 69.6, 'an229717': 84.0, 'an229719': 54.1} 69.21
range_trial_all {'an197522': 68.9, 'an229717': 82.2, 'an229719': 53.9} 68.31
clean trials {'an197522': 679, 'an229717': 24, 'an229719': 473} {'an197522': 66.1, 'an229717': 60.4, 'an229719': 51.8} {'an197522': 64.1, 'an229717': 57.2, 'an229719': 51.6} 59.4
clean lsj {'an197522': 737, 'an229717': 30, 'an229719': 491} {'an197522': 67.9, 'an229717': 64.5, 'an229719': 53.3} 61.9
{'an197522': 79, 'an229717': 159, 'an229719': 23} {'an197522': 9, 'an229717': 116, 'an229719': 4}
```

**Agent calls Bash**

```bash
cd entries/peron-2015; $TMPDIR/venv/bin/python - <<'EOF'
import json
p='reproduce_peron_2015.ipynb'
nb=json.load(open(p))
src='''# Multi-sample tracking errors (round-2 verifier, point 1). The 5-sample spike mask misses jumps
# that last three or more samples. Two masks for them: samples more than 20 degrees from a running
# median of 11 or 21 samples (jumps of up to 5 or 10 samples), and the jump mask of the helper
# (a step of more than 30 degrees in one sample, back within 25 samples, with other values). The
# step sizes show which sessions hold such errors: the 99th percentile step of a smooth whisk.
print("step between successive angle samples (degrees per 2 ms), percentiles 50, 99, 99.9, 99.99:")
for s in sessions:
    print(f"  {s['name']}: {np.round(s['whisker_summary']['step_pct'], 1).tolist()}")
cnt2 = allw.groupby("mouse").agg(trials=("trial", "size"),
                                 with_jump=("n_jump", lambda n: int((n > 0).sum())),
                                 with_med21=("n_med", lambda n: int((n > 0).sum())))
print("\\ntrials per mouse with samples in the jump mask (30 degrees, 25 samples) and the 21-sample median mask:")
print(cnt2.to_string())
mvars = [("range_trial", "(a) as listed"), ("range_trial_limit", "(a) without |angle| > 85"),
         ("range_trial_spike", "(a) without spikes (5-sample median)"),
         ("range_trial_med11", "(a) without jumps, 11-sample median"),
         ("range_trial_med21", "(a) without jumps, 21-sample median"),
         ("range_trial_jump20_10", "(a) jump mask, 20 deg, 10 samples"),
         ("range_trial_jump20_25", "(a) jump mask, 20 deg, 25 samples"),
         ("range_trial_jump30_10", "(a) jump mask, 30 deg, 10 samples"),
         ("range_trial_jump30_25", "(a) jump mask, 30 deg, 25 samples"),
         ("range_trial_jump30_50", "(a) jump mask, 30 deg, 50 samples"),
         ("range_trial_jump50_25", "(a) jump mask, 50 deg, 25 samples"),
         ("range_trial_lsj", "(a) without limit, spike and jump masks"),
         ("range_trial_all", "(a) without every mask, 21-sample median too")]
mm = allw.groupby("mouse")[[k for k, _ in mvars]].mean()
md = allw.groupby("mouse")[[k for k, _ in mvars]].median()
rows = [{"measure": name, **{m: round(mm.loc[m, k], 1) for m in mm.index},
         "mean over mice": round(mm[k].mean(), 2), "SD over mice": round(mm[k].std(), 1),
         "within": bool(lo <= mm[k].mean() <= hi), "above bound by": round(mm[k].mean() - hi, 2),
         "median-per-mouse mean": round(md[k].mean(), 1)} for k, name in mvars]
print(f"\\nreading (a) per mouse and over mice (degrees), against [{lo:.1f}, {hi:.1f}]:")
print(pd.DataFrame(rows).to_string(index=False))
# Trials with no sample in any mask. A selection, not a cleaning: it shows the range of the trials
# the tracker followed throughout, and it may favour smaller sweeps (compare with all trials).
cl = allw[(allw.n_limit == 0) & (allw.n_spike == 0) & (allw.n_jump == 0) & (allw.n_med == 0)]
g = cl.groupby("mouse").range_trial
print("\\ntrials with no sample in any mask: n", g.size().to_dict(), "; mean range", g.mean().round(1).to_dict(),
      f"; mean over mice {g.mean().mean():.1f}; all trials", mm["range_trial"].round(1).to_dict())
'''
cell={"cell_type":"code","execution_count":None,"metadata":{"tags":["claim:results-whisking-amplitude"]},"outputs":[],"source":src.splitlines(True)}
nb['cells'].insert(34,cell)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat
```

```
entries/peron-2015/reproduce_peron_2015.ipynb | 51 +++++++++++++++++++++++++++
 entries/peron-2015/ssc1.py                    | 44 ++++++++++++++++++++++-
 2 files changed, 94 insertions(+), 1 deletion(-)
```

**Agent calls Bash**

```bash
cd entries/peron-2015; $TMPDIR/venv/bin/python - <<'EOF' 2>&1 | grep -v Warning
import json, pickle, os, numpy as np, pandas as pd, ssc1
sessions=pickle.load(open(os.environ['TMPDIR']+'/ss.pkl','rb'))
nb=json.load(open('reproduce_peron_2015.ipynb'))
g={'np':np,'pd':pd,'ssc1':ssc1,'sessions':sessions}
import io,contextlib
for i in (31,33):
    with contextlib.redirect_stdout(io.StringIO()): exec(''.join(nb['cells'][i]['source']),g)
exec(''.join(nb['cells'][34]['source']),g)
EOF
```

```
step between successive angle samples (degrees per 2 ms), percentiles 50, 99, 99.9, 99.99:
  an197522_2013_03_08: [0.3, 3.9, 7.0, 11.3]
  an197522_2013_03_10: [0.3, 3.6, 6.2, 9.1]
  an229717_2013_12_01: [0.3, 8.3, 34.5, 172.0]
  an229719_2013_12_02: [0.1, 3.5, 6.5, 11.4]
  an229719_2013_12_05: [0.1, 2.6, 4.5, 7.5]

trials per mouse with samples in the jump mask (30 degrees, 25 samples) and the 21-sample median mask:
          trials  with_jump  with_med21
mouse                                  
an197522     764          9          79
an229717     183        116         159
an229719     496          4          23

reading (a) per mouse and over mice (degrees), against [42.2, 68.8]:
                                     measure  an197522  an229717  an229719  mean over mice  SD over mice  within  above bound by  median-per-mouse mean
                               (a) as listed      70.6      99.2      54.2           74.67          22.8   False            5.87                   68.6
                    (a) without |angle| > 85      70.1      92.8      54.1           72.36          19.5   False            3.56                   68.6
        (a) without spikes (5-sample median)      70.1      91.6      54.1           71.93          18.8   False            3.13                   68.6
         (a) without jumps, 11-sample median      69.7      86.1      54.0           69.93          16.0   False            1.13                   68.6
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd  cat entries/peron-2015/README.md; grep -n "" attempts/peron-2015-01.yaml | sed -n '1,40p'; grep -n "whisking-amplitude\|fig2e-fraction\|45 TIFF\|71.7\|verifications\|round:\|^[a-z_]*:" attempts/peron-2015-01.yaml
```

```
Mon Nov  9 22:28:17 UTC 2026
# Peron, Freeman, Iyer, Guo & Svoboda (2015) from CRCNS ssc-1

Tests the findings of [Peron et al. (2015)](https://doi.org/10.1016/j.neuron.2015.03.027) that can be
tested on [CRCNS ssc-1](https://doi.org/10.6080/K0TB14TN). The data set holds five imaging sessions
from three of the paper's eight volume-imaging mice. Each session has dF/F per ROI, whisker angle and
curvature, touches and trial data. It has no calcium events and no layer, cell-class or column
labels, and none of the learning, L4 axon, anesthetized or L5 soma and dendrite data.

| Claim | Outcome |
|---|---|
| Mice performed 245 ± 71 trials per session during imaging | Reproduced |
| Whisker movement amplitude 55.5 ± 13.3 degrees | Not reproduced |
| ROI counts per mouse (Table S1) | Blocked: data missing |
| Claims comparing layers, cell classes or columns (18) | Blocked: metadata insufficient |
| GABAergic, stack, training, trimming and dendrite claims (7) | Blocked: data missing |
| Neuropil, L4 axon, learning and anesthetized claims (14) | Blocked: data missing |
| Event detector validation on outside data | Blocked: methods underspecified |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 44,110p attempts/peron-2015-01.yaml; sed -n 330,600p attempts/peron-2015-01.yaml
```

```
blocked_by: data_missing
    notes: The only mouse with labelled GABAergic neurons, an194181 (Gad2-T2A-NLS-mCherry), is not in
      the data set, and no ROI carries a cell-class label.
  - claim: fig2e-fraction-imaged
    outcome: blocked
    blocked_by: data_missing
    notes: The high-resolution reference stacks and the nucleus counts from them are not in the data set.
      Its imaging archives hold registered trial TIFFs per plane; one archive listed in full held 45 TIFFs
      and nothing else. The criterion uses nuclei counts the data set carries and blocks the claim otherwise.
  - claim: fig1e-days-to-criterion
    outcome: blocked
    blocked_by: data_missing
    notes: The data set holds no training sessions, only five imaging sessions of trained mice.
  - claim: results-trials-per-session
    outcome: reproduced
    notebook: reproduce_peron_2015.ipynb
    output: claim:results-trials-per-session
    measured: 290.2
    notes: The five sessions hold 398, 370, 184, 231 and 268 behavioural trials. Pooled over sessions
      the mean is 290.2 (SD 91.2), and the mean of the three per-mouse means (384.0, 184.0, 249.5) is
[... 318 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2015; $TMPDIR/venv/bin/python - <<'EOF'
import json
p='reproduce_peron_2015.ipynb'
nb=json.load(open(p))
c=nb['cells'][35]; assert ''.join(c['source']).startswith('**Result: not reproduced.**')
new='''**Result: not reproduced.** Over the three mice in the data set, the mean whisker angle range per
trial is 74.7 degrees over the whole trial (a), 29.0 over the sample epoch (b), and the mean peak
Hilbert amplitude is 26.9 (c). None is within 55.5 ± 13.3 (42.2 to 68.8). Reading (c) gives 22.2 to
30.4 with the other bands and stays outside.

Removing the tracking errors brings reading (a) close to the upper bound but, with every mask that
removes only errors, not inside it. Samples above 85 degrees occur in 2 to 52 trials per mouse,
one- or two-sample spikes in 5 to 152 and wraps past 90 degrees in 3 to 43, most in an229717 (52,
152 and 43 of its 183 trials). Without them reading (a) is 72.4 (no samples above 85 degrees) or
71.9 (no spikes). It falls steadily as the threshold on |angle| drops: 74.1 at 88 degrees, 72.4 at
85, 70.3 at 80 and 67.4 at 70, the last two also removing the tops of real protractions. With the
spike threshold at 10 to 40 degrees it is 71.7 to 72.1. Unwrapping angles past 90 degrees raises it
to 77.0, as some protractions pass 90 degrees and wrap to the other sign (for example 84.6, 89.2,
-87.5, -88.7, 89.3, 83.9 in an197522); other errors are single samples at the limit (87.3, 37.8,
-89.2, 41.7 in an229717) or jumps that last three samples or more (-24.1, 72.8, 72.8, 72.1, -23.1
in an229719), which the 5-sample spike filter does not remove.

Jumps of several samples are nearly all in an229717: its 99.9th percentile step between samples is
34.5 degrees against 4.5 to 7.0 in the other sessions, and 116 of its 183 trials hold a step over 30
degrees that returns within 25 samples, against 9 of 764 and 4 of 496 in the other mice. Removing
these jumps gives reading (a) 69.7 to 70.1 with the six step and duration values tried (69.8 at 30
degrees and 25 samples), and 69.2 with the limit and spike masks as well, 0.4 above the bound; an229717
falls from 99.2 to 84.0 to 86.0, and the other mice by at most 1.0. Only the 21-sample running median,
alone (68.6) or with every other mask (68.3), brings it inside; that mask also flags samples in 79 of
764 trials of an197522, whose largest steps (99.99th percentile 9.1 to 11.3 degrees) show no jumps,
and lowers that mouse from 70.1 to 69.0, so it also removes the peaks of real whisks. The trials
with no sample in any mask (679, 24 and 473 per mouse) give 59.4 over mice, but they are a selection:
in an197522 they average 66.1 against 70.6 for all its trials. So the best-supported cleaning leaves
reading (a) 0.4 to 1.3 above the bound, and whether a cleaned reading (a) falls inside depends on a
choice the paper does not describe. The outcome stays not reproduced, by a narrow margin.

The filter's edge effect inflates the peak Hilbert amplitude of a sinusoid of amplitude 20 to 22.0,
and 20.1 once 0.2 s at each end is left out; on the data, leaving out the ends changes reading (c)
from 26.9 to 26.6, so the peaks lie inside the trials. With the multi-sample jumps removed an229717
still has a mean range of 84.0 to 86.0 and a median of 86.6 to 87.2, the largest of the three mice.

Measures the criterion does not list come within the tolerance: the mean over mice of the per-mouse
medians of reading (a) (68.6, 0.2 below the upper bound, and 68.3 to 68.6 under every mask), the
trial range between the 1st and 99th percentiles of angle (49.2), and twice the peak Hilbert
amplitude, a peak-to-peak measure (53.7 ± 15.7, or 53.2 without the ends and artefacts). The part
of the statement the criterion does not test, that the movements are larger than about 20 degrees,
holds for every full-sweep measure (28.6 to 77.0). The paper does not define the measure, and the
test rests on 3 of the 8 mice.
'''
c['source']=new.splitlines(True)
s=''.join(nb['cells'][36]['source'])
s=s.replace("| results-whisking-amplitude | not reproduced (74.7, 29.0, 26.9 degrees under the three readings, 72.4, 29.0, 26.6 without tracking errors and edge effects; 55.5 ± 13.3) |",
"| results-whisking-amplitude | not reproduced (74.7, 29.0, 26.9 degrees under the three readings; reading (a) 69.2 without every kind of tracking error, 0.4 above the bound; 55.5 ± 13.3) |")
s=s.replace('''- The whisker angle holds tracking errors: samples jumping to the tracker's +/-90 degree limit for
  one or two samples, and protractions past 90 degrees that wrap to the other sign. Neither is
  described.''','''- The whisker angle holds tracking errors: samples jumping to the tracker's +/-90 degree limit for
  one or two samples, jumps to a distant value lasting three samples or more (mostly in an229717,
  in 116 of its 183 trials), and protractions past 90 degrees that wrap to the other sign. None is
  described.''')
assert '69.2' in s and '116 of its' in s
nb['cells'][36]['source']=s.splitlines(True)
s0=''.join(nb['cells'][0]['source'])
s0=s0.replace('''unwrapping angles past 90 degrees, without the filter's edge effects, and with per-mouse medians.
''','''unwrapping angles past 90 degrees, without the filter's edge effects, and with per-mouse medians.
After the second, reading (a) without tracking errors that last several samples.
''')
assert 'After the second' in s0
nb['cells'][0]['source']=s0.splitlines(True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat
```

```
entries/peron-2015/reproduce_peron_2015.ipynb | 194 +++++++++++++++++++++++++-
 entries/peron-2015/ssc1.py                    |  44 +++++-
 2 files changed, 234 insertions(+), 4 deletions(-)
```

**Agent calls Bash**

```bash
cd  git diff entries/peron-2015/reproduce_peron_2015.ipynb | grep '^[-+]' | cut -c1-100 | head -60
```

```
--- a/entries/peron-2015/reproduce_peron_2015.ipynb
+++ b/entries/peron-2015/reproduce_peron_2015.ipynb
-   "source": "# Reproducing Peron et al. (2015) from CRCNS ssc-1\n\nPaper. Peron SP, Freeman J, Iye
+   "source": [
+    "# Reproducing Peron et al. (2015) from CRCNS ssc-1\n",
+    "\n",
+    "Paper. Peron SP, Freeman J, Iyer V, Guo C, Svoboda K (2015). A cellular resolution map of barr
+    "cortex activity during tactile behavior. *Neuron* 86:783-799.\n",
+    "[doi:10.1016/j.neuron.2015.03.027](https://doi.org/10.1016/j.neuron.2015.03.027). The claims f
+    "(`claims/peron-2015.yaml`) was written from the version of record with its Supplemental Inform
+    "\n",
+    "Data set. [CRCNS ssc-1](https://doi.org/10.6080/K0TB14TN), read anonymously from the public S3
+    "bucket `crcnsarchive` under `ssc-1/`. CRCNS data sets are not versioned (docs/archives.md, \"C
+    "so the version recorded is `unversioned`; the paper cites the data set's DOI and no version, a
+    "the bucket holds one copy (no `live/` or `old/` folder). A later change is detectable from the
+    "sums of the files read, taken from the data set's `checksums.md5` and checked against the byte
+    "read:\n",
+    "\n",
+    "| File | MD5 |\n",
+    "|---|---|\n",
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2015; $TMPDIR/venv/bin/python - <<'EOF'
import json
p='reproduce_peron_2015.ipynb'
nb=json.load(open(p))
for c in nb['cells']:
    if isinstance(c['source'],list): c['source']=''.join(c['source']).rstrip('\n')
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
cd ..; git diff --stat; date -u; cd  && time python tools/entry.py all entries/peron-2015 2>&1 | tail -15
```

```
entries/peron-2015/reproduce_peron_2015.ipynb | 396 +++-----------------------
 entries/peron-2015/ssc1.py                    |  44 ++-
 2 files changed, 85 insertions(+), 355 deletions(-)
Mon Nov  9 22:28:52 UTC 2026
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
Installed kernelspec registry-peron-2015 in executed/peron-2015/.venv/share/jupyter/kernels/registry-peron-2015
0 error(s)
pass  reproduce_peron_2015.ipynb  (33 s)

real	0m41.850s
user	0m31.364s
sys	0m4.542s
```

**Agent calls Bash**

```bash
cd  git show HEAD:entries/peron-2015/reproduce_peron_2015.ipynb | python -c "
import json,sys; nb=json.load(sys.stdin); print(nb['nbformat'],nb['nbformat_minor'],[type(c['source']).__name__[0] for c in nb['cells']], [('id' in c) for c in nb['cells']][:3])"
```

```
4 5 ['s', 'l', 'l', 'l', 'l', 'l', 'l', 's', 's', 'l', 'l', 's', 's', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 's', 'l', 'l', 'l', 's', 's', 's', 'l'] [True, True, True]
```

**Agent calls Bash**

```bash
cd  git show HEAD:entries/peron-2015/reproduce_peron_2015.ipynb > $TMPDIR/old.ipynb; python - <<'EOF'
import json,os
old=json.load(open(os.environ['TMPDIR']+'/old.ipynb'))
p='entries/peron-2015/reproduce_peron_2015.ipynb'
new=json.load(open(p))
oc=old['cells']
cells=[]
for i,c in enumerate(new['cells']):
    j=i if i<34 else i-1
    if i==34:
        c['id']='whisk-multisample'; c['source']=c['source'].splitlines(True); cells.append(c); continue
    o=oc[j]
    if ''.join(o['source']).rstrip('\n')==c['source']: cells.append(o)
    else:
        o=dict(o); o['source']=c['source'] if isinstance(oc[j]['source'],str) else c['source'].splitlines(True); cells.append(o)
old['cells']=cells
json.dump(old,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat; tail -c 50 $TMPDIR/old.ipynb | od -c | tail -3
```

```
entries/peron-2015/reproduce_peron_2015.ipynb | 58 +++++++++++++++++++++++++--
 entries/peron-2015/ssc1.py                    | 44 +++++++++++++++++++-
 2 files changed, 98 insertions(+), 4 deletions(-)
0000040   o   r   m   a   t   _   m   i   n   o   r   "   :       5  \n
0000060   }  \n
0000062
```

**Agent calls Bash**

```bash
python tools/entry.py all entries/peron-2015 2>&1 | tail -4; python - <<'EOF'
import json
nb=json.load(open('executed/peron-2015/reproduce_peron_2015.ipynb'))
for i in (31,32,33,34,37):
    for o in nb['cells'][i].get('outputs',[]):
        print('---',i); print(''.join(o.get('text','')) if 'text' in o else o.get('data',{}).get('text/plain',''))
EOF
```

```
Installed kernelspec registry-peron-2015 in executed/peron-2015/.venv/share/jupyter/kernels/registry-peron-2015
0 error(s)
pass  reproduce_peron_2015.ipynb  (32 s)
--- 31
trials per mouse: {'an197522': 764, 'an229717': 183, 'an229719': 496}

per session (mean over trials, degrees):
                              range_trial  range_sample  hilbert_peak
mouse    session                                                     
an197522 an197522_2013_03_08         75.0          22.8          28.5
         an197522_2013_03_10         65.8          21.9          24.0
an229717 an229717_2013_12_01         99.2          35.4          35.0
an229719 an229719_2013_12_02         60.4          33.1          22.5
         an229719_2013_12_05         48.8          25.9          16.6

--- 31

per mouse (mean over trials, degrees):
          range_trial  range_sample  hilbert_peak
mouse                                            
[... 112 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/peron-2015; python - <<'EOF'
import json
p='reproduce_peron_2015.ipynb'
nb=json.load(open(p))
c=nb['cells'][35]
s=c['source'] if isinstance(c['source'],str) else ''.join(c['source'])
old='''from 26.9 to 26.6, so the peaks lie inside the trials. With the multi-sample jumps removed an229717
still has a mean range of 84.0 to 86.0 and a median of 86.6 to 87.2, the largest of the three mice.'''
assert old in s
s=s.replace(old,'''from 26.9 to 26.6, so the peaks lie inside the trials. With the multi-sample jumps removed an229717
still has a mean range of 84.0 to 86.0, the largest of the three mice, and its median of 87.2 is
unchanged by the 1- or 2-sample spikes.''')
c['source']=s if isinstance(c['source'],str) else s.splitlines(True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
cd ../..; git diff --stat
```

```
entries/peron-2015/reproduce_peron_2015.ipynb | 58 +++++++++++++++++++++++++--
 entries/peron-2015/ssc1.py                    | 44 +++++++++++++++++++-
 2 files changed, 98 insertions(+), 4 deletions(-)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='entries/peron-2015/README.md'; s=open(p).read()
old='''three mice give 74.7, 29.0 and 26.9 degrees, and 72.4, 29.0 and 26.6 once tracking errors in the
whisker angle and the filter's edge effects are removed. Twice the peak Hilbert amplitude, which the criterion
does not list, gives 53.7.'''
assert old in s
s=s.replace(old,'''three mice give 74.7, 29.0 and 26.9 degrees. Removing the tracking errors in the whisker angle,
including jumps that last several samples, brings the first to 69.2 to 70.1, just above the upper
bound of 68.8; only a filter that also cuts the peaks of real whisks brings it inside (68.3 to 68.6).
Twice the peak Hilbert amplitude, which the criterion does not list, gives 53.7.''')
open(p,'w').write(s)
EOF
grep -n "results-whisking-amplitude" -A3 questions/peron-2015.yaml | head; sed -n 110,118p attempts/peron-2015-01.yaml; sed -n 600,760p attempts/peron-2015-01.yaml
```

```
6:- claim: results-whisking-amplitude
7-  asked: 2026-11-09
8-  question: >-
9-    The claims file's opening comment describes the trials as having "a 1 s sample epoch (pole in
        not from the paper, and every one gives the same outcome; the 1st to 99th percentile range is
        shown as a further variant.
  - claim: fig1g-early-stereotypy
    outcome: blocked
    blocked_by: data_missing
    notes: The data set holds no training videography or training sessions.
  - claim: supp-trim-all-chance
    outcome: blocked
    blocked_by: data_missing
        outcome: blocked
        reason: No imaging during learning. an197522 is a learning mouse, but its deposited sessions are
          volume-imaging sessions with no training-day index.
        response: No change.
      - claim: fig6c-no-trimming-expansion
        agrees: true
        outcome: blocked
[... 154 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 760,800p attempts/peron-2015-01.yaml; wc -l attempts/peron-2015-01.yaml; grep -n "proposed" -A8 schemas/*.json | head -30
```

```
response: Outcome unchanged. The block stays methods_underspecified, since the protocol never blocks a
          data elsewhere claim as data_missing (author, step 4), and the notes say why the test cannot be
          repeated as described.
762 attempts/peron-2015-01.yaml
schemas/attempt.schema.json:303:          "proposed": {
schemas/attempt.schema.json-304-            "description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
schemas/attempt.schema.json-305-            "type": "object",
schemas/attempt.schema.json-306-            "additionalProperties": false,
schemas/attempt.schema.json-307-            "required": [
schemas/attempt.schema.json-308-              "outcome",
schemas/attempt.schema.json-309-              "reason"
schemas/attempt.schema.json-310-            ],
schemas/attempt.schema.json-311-            "properties": {
--
schemas/claims.schema.json:3:  "title": "Claims proposed for one target (a dataset and one of its papers)",
schemas/claims.schema.json-4-  "description": "Draft. To be revised after the pilot.",
schemas/claims.schema.json-5-  "type": "object",
schemas/claims.schema.json-6-  "additionalProperties": false,
schemas/claims.schema.json-7-  "required": [
schemas/claims.schema.json-8-    "schema_version",
[... 3 more lines not kept]
```

**Agent**

Now the record edits for the whisking outcome, the fig2e note and the findings.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/peron-2015-01.yaml'; s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1, old[:60]
    s=s.replace(old,new)
rep('''      Its imaging archives hold registered trial TIFFs per plane; one archive listed in full held 45 TIFFs
      and nothing else. The criterion uses nuclei counts the data set carries and blocks the claim otherwise.''',
'''      Its imaging archives are named for imaging planes and, by the data description, hold registered
      trial TIFFs; their contents are not listed in the notebook. The criterion uses nuclei counts the
      data set carries and blocks the claim otherwise.''')
rep('''      Tracking errors do not explain the miss. Without samples above 85 degrees (in 26, 52 and 2 trials
      per mouse) reading (a) is 72.4, without one- or two-sample spikes 71.9, and 71.7 to 74.1 with other
      thresholds; only dropping all samples above 70 degrees, which also cuts real protractions, gives
      67.4. Unwrapping protractions that pass 90 degrees and wrap to the other sign gives 77.0.''',
'''      Removing tracking errors brings reading (a) close to the upper bound but not inside it under any
      mask that removes only errors. Without samples above 85 degrees (in 26, 52 and 2 trials per mouse)
      reading (a) is 72.4 and without one- or two-sample spikes 71.9. It falls steadily as the threshold on
      the angle drops, 74.1 at 88 degrees, 72.4 at 85, 70.3 at 80 and 67.4 at 70, the lower thresholds also
      cutting the tops of real protractions; spike thresholds of 10 to 40 degrees give 71.7 to 72.1.
      Unwrapping protractions that pass 90 degrees and wrap to the other sign gives 77.0. Jumps that last
      three samples or more are nearly all in an229717 (99.9th percentile step 34.5 degrees per 2 ms
      against 4.5 to 7.0 in the other sessions; a step over 30 degrees that returns within 25 samples in
      116 of its 183 trials, against 9 of 764 and 4 of 496). Removing them gives 69.7 to 70.1 over six
      step and duration values (69.8 at 30 degrees and 25 samples), and 69.2 with the limit and spike masks
      as well, 0.4 above the bound of 68.8; an229717 falls from 99.2 to 84.0 to 86.0. A 21-sample running
      median filter gives 68.6, and 68.3 with every other mask, inside, but it also removes real whisk
      peaks, flagging samples in 79 of 764 trials of an197522, whose largest steps are 9.1 to 11.3 degrees
      (99.99th percentile), and lowering that mouse from 70.1 to 69.0. Trials with no masked sample give
      59.4 over mice, but they are a selection (in an197522 66.1 against 70.6 for all trials). The miss is
      therefore narrow, 0.4 to 1.3 degrees for the cleanings that remove only errors, and whether a cleaned
      reading (a) falls inside depends on a choice the paper does not describe.''')
rep('''      1st to 99th percentile range of angle per trial (49.2) and twice the peak Hilbert amplitude, a peak-to-peak
      measure (53.7 +/- 15.7; 53.2 without ends and artefacts). The part of the statement the criterion
      does not test, larger movements than about 20 degrees, holds for every full-sweep measure (29.0
      to 77.0).''','''      1st to 99th percentile range of angle per trial (49.2) and twice the peak Hilbert amplitude, a peak-to-peak
      measure (53.7 +/- 15.7; 53.2 without ends and artefacts). The part of the statement the criterion
      does not test, larger movements than about 20 degrees, holds for every full-sweep measure (28.6
      to 77.0).''')
rep('''        above 85 degrees and without spikes over 20 degrees from a 5-sample running median, with other
        thresholds, and after unwrapping; reading (c) without 0.2 s at each end. These are standard choices,
        not from the paper, and every one gives the same outcome; the 1st to 99th percentile range is
        shown as a further variant.''','''        above 85 degrees and without spikes over 20 degrees from a 5-sample running median, with other
        thresholds, and after unwrapping; reading (a) also without jumps of several samples (a step over
        30 degrees in one sample that returns within 25 samples, with other values, and running medians of
        11 and 21 samples); reading (c) without 0.2 s at each end. These are standard choices, not from the
        paper, which says nothing on tracking errors. Every one that removes only errors gives the same
        outcome; the 21-sample median, which also cuts real whisk peaks, does not (68.6, or 68.3 with every
        mask). The 1st to 99th percentile range is shown as a further variant.''')
rep('''      on successive 2 ms samples in an229717), jump briefly to a distant value (-24.1, 72.8, 72.8, 72.1,
      -23.1 in an229719), and protractions''','''      on successive 2 ms samples in an229717), jump to a distant value for three samples or more (-24.1,
      72.8, 72.8, 72.1, -23.1 in an229719; in an229717 a step over 30 degrees that returns within 25 samples
      occurs in 116 of 183 trials, and its 99.9th percentile step is 34.5 degrees against 4.5 to 7.0 in the
      other sessions), and protractions''')
rep('''      is 74.7 degrees (72.4 without tracking errors), its range''','''      is 74.7 degrees (69.2 without the tracking errors), its range''')
open(p,'w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
p='attempts/peron-2015-01.yaml'; s=open(p).read()
old='''      Its imaging archives are named for imaging planes and, by the data description, hold registered
      trial TIFFs; their contents are not listed in the notebook.'''
assert old in s
s=s.replace(old,'''      By the data description its imaging archives hold registered trial TIFFs; the notebook does not
      list their contents.''')
open(p,'w').write(s)
EOF
grep -n "registered\|TIFF" paper/*.md 2>/dev/null | head -3; ls paper
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -n -i "tif\|registered" paper/ssc-1.data-description.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml, textwrap
p='attempts/peron-2015-01.yaml'
rec=yaml.safe_load(open(p))
def block(key, text, ind):
    lines=textwrap.wrap(text, 104-ind)
    return f"{' '*ind}{key}: " + ("\n"+" "*(ind+2)).join(lines) + "\n"
R={
'results-trials-per-session':("reproduced","I agree. Cell 28 gives 290.2 pooled and 272.5 as the mean of per-mouse means, both inside [174, 316]. It is weak evidence (5 sessions from 3 of 8 mice), and the record now says so.","No change."),
'results-whisking-amplitude':("not_reproduced","I now agree; in round 1 I said partially_reproduced. In cell 33 every listed reading is still outside [42.2, 68.8] after removing only the artefacts, (a) 72.4 or 71.9, (b) 28.6 to 29.0, (c) 26.6, so the criterion's within tolerance under one reading rule gives not_reproduced. The miss is narrow. Reading (a) falls steadily as the threshold drops (74.1 at 88 degrees, 72.4 at 85, 70.3 at 80, 67.4 at 70), the mean of per-mouse medians is 68.6, inside, and multi-sample jumps are not removed by either artefact mask. Reading (a) with multi-sample jumps removed has not been computed, and since the miss is 3.6 degrees above the bound, moves with the threshold and is driven by an229717, this check could move the outcome. The sentences 71.7 to 74.1 with other thresholds (70.3 is printed for 80 degrees), tracking errors do not explain the miss, most of reading (a) is real whisking, and 29.0 to 77.0 (reading b without spikes is 28.6) are not supported as written, and the summary omits the multi-sample jumps.",
 "Outcome unchanged, and no change is proposed. A new cell (cell 34) removes multi-sample jumps two ways: a jump mask (a step over 30 degrees in one sample that returns within 25 samples, with five other step and duration values) and running medians of 11 and 21 samples. The jumps are nearly all in an229717 (116 of its 183 trials; 99.9th percentile step 34.5 degrees against 4.5 to 7.0 elsewhere). Reading (a) becomes 69.7 to 70.1 with the jump mask and 69.2 with the limit, spike and jump masks together, 0.4 above the bound; an229717 falls from 99.2 to 84.0 to 86.0. Only the 21-sample median brings it inside (68.6, or 68.3 with every mask), and it also cuts real whisk peaks, lowering an197522, which has no jumps (99.99th percentile step 9.1 to 11.3), from 70.1 to 69.0. The best-supported cleaning thus leaves the outcome not_reproduced, by 0.4 to 1.3 degrees, and the notes say that a cleaned reading (a) inside the tolerance depends on a choice the paper does not describe. The conclusion, notes, README and summary now give the threshold series 74.1, 72.4, 70.3, 67.4, drop the sentences the verifier found unsupported, give 28.6 to 77.0, and list the multi-sample jumps in the summary and the finding."),
'methods-event-detection':("blocked","I accept methods_underspecified over my round-1 data_missing, given the protocol rule the record cites. Either way the outcome is blocked.","No change."),
'fig2e-fraction-imaged':("blocked","I agree with each of the blocked claims. The record's 45 TIFFs and nothing else is not supported by any printed output; cell 6 says it was not run here.","Outcome unchanged. The sentence on 45 TIFFs is removed from the notes, which now say only what the data description says of the imaging archives and that the notebook does not list their contents."),
}
lab="I agree with each of the blocked claims. Cell 7 now shows that no identifier or description field carries a layer, class or column label, so the M6 blocks stand."
gen="I agree with each of the blocked claims."
out=["  - date: '2026-11-09'\n","    kind: agent\n",
"    by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)\n"]
out.append(block("reviewed","Round 2. The full executed notebook of the first revision, the helper module ssc1.py, the claims file and the attempt record, with the paper. Its report agrees with all 43 outcomes; it asked for reading (a) without multi-sample tracking jumps and corrections to sentences the numbers did not support. It found no misreading of the paper in the claims file (the degree values it calls garbled are legible apart from the degree signs, which does not affect the criterion), so no question was added. Report in transcripts/peron-2015/verifier-2-report.md.",4))
out.append("    results:\n")
for o in rec['outcomes']:
    c=o['claim']
    if c in R: oc,rs,rp=R[c]
    else:
        oc="blocked"; rs=lab if o.get('blocked_by')=='metadata_insufficient' else gen; rp="No change."
    out.append(f"      - claim: {c}\n        agrees: true\n        outcome: {oc}\n")
    out.append(block("reason",rs,8)); out.append(block("response",rp,8))
s=open(p).read()
if not s.endswith('\n'): s+='\n'
s+=''.join(out)
open(p,'w').write(s)
y=yaml.safe_load(open(p)); print(len(y['verifications']), len(y['verifications'][-1]['results']))
EOF
grep -n ": .*: " attempts/peron-2015-01.yaml | sed -n '1,5p' | cut -c1-120
```

```
Traceback (most recent call last):
  File "<stdin>", line 31, in <module>
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/__init__.py", line 125, in safe_load
    return load(stream, SafeLoader)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/__init__.py", line 81, in load
    return loader.get_single_data()
           ~~~~~~~~~~~~~~~~~~~~~~^^
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/constructor.py", line 49, in get_single_data
    node = self.get_single_node()
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/composer.py", line 36, in get_single_node
    document = self.compose_document()
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/composer.py", line 55, in compose_document
    node = self.compose_node(None, None)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/composer.py", line 84, in compose_node
    node = self.compose_mapping_node(anchor)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/composer.py", line 133, in compose_mapping_node
    item_value = self.compose_node(node, item_key)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/composer.py", line 82, in compose_node
    node = self.compose_sequence_node(anchor)
  File "/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/yaml/composer.py", line 111, in compose_sequence_node
[... 34 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 838,844p attempts/peron-2015-01.yaml
```

```
thresholds (70.3 is printed for 80 degrees), tracking errors do not explain the miss, most of
          reading (a) is real whisking, and 29.0 to 77.0 (reading b without spikes is 28.6) are not
          supported as written, and the summary omits the multi-sample jumps.
        response: Outcome unchanged, and no change is proposed. A new cell (cell 34) removes multi-sample jumps
          two ways: a jump mask (a step over 30 degrees in one sample that returns within 25 samples, with
          five other step and duration values) and running medians of 11 and 21 samples. The jumps are
          nearly all in an229717 (116 of its 183 trials; 99.9th percentile step 34.5 degrees against 4.5
```

**Agent calls Bash**

```bash
cd  sed -i 's/          two ways: a jump mask/          two ways, a jump mask/' attempts/peron-2015-01.yaml; python -c "
import yaml; y=yaml.safe_load(open('attempts/peron-2015-01.yaml')); print(len(y['verifications']), len(y['verifications'][-1]['results']))"; awk 'NR>762' attempts/peron-2015-01.yaml | grep -n ': .*: ' | head; grep -c "—\|rather" attempts/peron-2015-01.yaml entries/peron-2015/README.md
```

```
2 43
attempts/peron-2015-01.yaml:0
entries/peron-2015/README.md:0
```

**Agent calls Bash**

```bash
cd  grep -c "—\|rather" entries/peron-2015/reproduce_peron_2015.ipynb entries/peron-2015/ssc1.py; python tools/entry.py all entries/peron-2015 2>&1 | tail -3; python tools/entry.py check entries/peron-2015 2>&1 | tail -3; git status --short
```

```
entries/peron-2015/reproduce_peron_2015.ipynb:0
entries/peron-2015/ssc1.py:0
Installed kernelspec registry-peron-2015 in executed/peron-2015/.venv/share/jupyter/kernels/registry-peron-2015
0 error(s)
pass  reproduce_peron_2015.ipynb  (33 s)
0 error(s)
 M attempts/peron-2015-01.yaml
 M entries/peron-2015/README.md
 M entries/peron-2015/reproduce_peron_2015.ipynb
 M entries/peron-2015/ssc1.py
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
[... 1 more lines not kept]
```

**Agent**

I made no outcome changes and proposed none. The verifier agreed with all 43 outcomes in round 2, and the new check it asked for leaves the whisking result outside the tolerance, though only just. `python tools/entry.py all entries/peron-2015` passes (the notebook runs in 33 s) and `check` reports 0 errors.

**The new whisking check.** The verifier asked for reading (a), the per-trial angle range, with tracking jumps lasting three or more samples removed. A new cell (34) and new masks in `ssc1.py` do this two ways:
- **Jump mask:** a step of more than 30° in one 2 ms sample that comes back within 25 samples, plus five other step and duration values.
- **Running-median filters:** windows of 11 and 21 samples.

What the numbers show:
- **Where the jumps are:** nearly all in an229717. They are in 116 of its 183 trials, against 9 of 764 and 4 of 496 in the other two mice. Its 99.9th percentile step is 34.5°, against 4.5° to 7.0° in the other sessions.
- **Reading (a) without the jumps:** 69.7 to 70.1 with the jump mask, and 69.2 with all the error masks together. The upper bound is 68.8.
- **What brings it inside:** only the 21-sample median, which gives 68.6 (68.3 with every mask). That filter also cuts real whisk peaks. It flags 79 trials of an197522, a mouse with no jumps (largest steps 9.1° to 11.3°), and lowers it from 70.1 to 69.0.
- **Conclusion:** under every cleaning that removes only tracking errors, the result misses by 0.4° to 1.3°, so `not_reproduced` stands. The notes now say the miss is narrow, and that whether a cleaned reading lands inside depends on a choice the paper does not describe.

**Text corrected in the notebook, README and attempt record:**
- I removed the sentences the verifier found unsupported: "71.7 to 74.1", "tracking errors do not explain the miss" and "most of reading (a) is real whisking".
- They now give the steady fall with the angle threshold: 74.1 at 88°, 72.4 at 85°, 70.3 at 80°, 67.4 at 70°.
- "29.0 to 77.0" is now "28.6 to 77.0".
- The summary and the tracking-error finding now list the multi-sample jumps.
- The question to the paper's authors now cites 69.2.
- I removed the unsupported "45 TIFFs and nothing else" from the fig2e note. It now says only what the data description says about the imaging archives.

**Recorded:** a round-2 entry under `verifications` in `attempts/peron-2015-01.yaml`, with the verifier's reasons for all 43 claims and my response to each.

**Not done:**
- **No question added to `questions/peron-2015.yaml`:** the verifier found no misreading of the paper. It noted the degree signs in the claims file are garbled, but the numbers are legible and the criterion is unaffected.
- **Imaging archive contents (point C5) not listed:** that would mean streaming a multi-GB archive, and it bears only on the wording of the fig2e note, which I changed instead.

Nothing is committed, as instructed.

## End of run

38 turns, 9 minutes, $1.78 at API prices, result: success.
