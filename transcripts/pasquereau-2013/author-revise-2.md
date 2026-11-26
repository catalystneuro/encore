# pasquereau-2013 · author-revise-2 · run 45878790120

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/pasquereau-2013/verifier-2-report.md; ls entries/pasquereau-2013 entries/pasquereau-2013/*; ls transcripts/pasquereau-2013
```

```
Thu Nov 26 18:55:12 UTC 2026
**Verifier report, round 2: Pasquereau & Turner 2013 on DANDI:001636 (0.261124.1906)**

Counts come from the claims file and the attempt record. There are 28 claims and 28 outcomes: 4 reproduced, 3 partially reproduced, 3 not reproduced and 18 blocked. Cell numbers below are positions in the re-executed notebook, counted from 0.

**1. Outcomes**

I agree with all 28 stated outcomes. No outcome has `assumed: true`, so there is no assumption to check.

- **cell-counts, baseline-rate, ptn-faster-than-csn: reproduced.** Agree (cells 25, 31, 34).
- **antidromic-latency: partially reproduced.** Agree (cell 37: CSN p = 0.019, above 0.0167).
- **monkey-l-perturbations: blocked, data missing.** Agree (cells 20, 28).
- **false-positive-rate and the 15 claims that depend on it: blocked, methods underspecified.** Agree. The false-positive rate is 0.230 (cell 40). The `trial_sd` reading, shown in cells 44–58, would not reproduce torque-related-fractions either (20.0% and 18.5% of M1 cells against 75 and 68% expected, cell 44).
- **velocity-matched-magnitude: blocked.** Agree. It would also stay untestable because of the data: only 2 of 581 session-directions fall in the velocity range (cell 22).
- **trial-correlations: blocked.** Agree.
- **kinematics-slower: not reproduced.** Agree by the criterion (cell 61). The torque pulse is still about twice as large after MPTP inside the "matched" 60–250 range (cell 72: median 90.9 against 181.8 units for flexion). So the faster, larger displacements cannot be separated from stimulus size.
- **kinematic-latency-unchanged: not reproduced.** I now agree; in round 1 I had it as blocked. The causal-filter variant is a valid onset measure. It gives shorter post-MPTP latencies (F = 422.5, and 146.2 within the 60–250 range; cell 66). The deciding F = 709 still comes from a measure whose post-MPTP flexion mean (3.05 ms) falls before the command leaves rest (4 ms, cell 14). The same stimulus-size confound applies.
- **
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "" docs/protocol.md | sed -n '1,400p' | grep -n -i -E "step 6|Hand over|proposed|verifications|round 2|findings|Time" | head -60; wc -l docs/protocol.md
```

```
31:31:[Agent run](../.github/workflows/attempt.yml) workflow, one role at a time:
78:78:     number when the full text is available. Cover the paper's main findings,
160:160:     its own findings, from its analysis of those data. Its findings on
181:181:paper's main findings each have a claim. The checker corrects what it can
190:190:not say what the paper says (author, step 1.6, and "Hand over for
205:205:(step 6).
207:207:**Time.** An author run is stopped five hours after it starts, and whatever
209:209:time by which to finish. Check the clock (`date -u`) between steps. When that
210:210:time comes, stop analysing and finish: record each claim not yet tested as
213:213:with some claims blocked for time is worth more than a run that is cut off.
234:234:   version too, and record which versions have it (step 5, `findings`): a
255:255:     claims are the registry's checks, not findings of the paper, so the
304:304:     (step 6; see also chance levels, under "Record the attempt").
311:311:     within the time limit. Say what was tried. For an outside input that is
354:354:     claims file (reader, step 6), and a later run, `author-answers`,
383:383:sessions, decoding the annotations with the labels shifted in time), and name any
391:391:that show the problem (the two recordings' correlation, the timestamps that
813 docs/protocol.md
```

**Agent calls Bash**

```bash
sed -n 395,560p docs/protocol.md
```

```
tests it.

### 3. Write the entry

An entry is a directory `entries/<paper>/` holding
`entry.yaml`, `requirements.in`, one or more notebooks, and usually a helper
module.

- **Stream the data** from the archive, at a pinned version of the dataset
  ([archives.md](archives.md)). Do not download files to disk or read local
  paths.
- **Compute every result from the data.** No embedded numbers, arrays or
  images, and no figures read from files.
- **Take every random seed from the claim.** Do not choose one. The seed of a
  claim's generator is `zlib.crc32(b"<paper key>/<claim id>")`, for example
  `np.random.default_rng(zlib.crc32(b"sohn-2019/initial-speed-biased"))`. A
  second generator for the same claim adds 1 to the seed, a third adds 2. Two
  attempts on a claim then start from the same seed, and each claim's section
  has its own generator, so that adding a cell earlier does not change its
  numbers. Never make a generator without a seed.
[... 146 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 560,700p docs/protocol.md
```

```
code, with nothing wrong in the files. These are on the paper's page.

  The kinds are `metadata_error`, `data_missing`, `identifier_missing`,
  `format_error` (files that break their own format, such as unsorted spike
  times) and `metadata_insufficient` (a variable without a description or a
  needed mapping), which are about the data; `methods_unavailable`,
  `code_mismatch` (published code that disagrees with the paper or the data)
  and `paper_inconsistency` (the paper disagrees with itself), which are
  about the paper; and `selection_undocumented` and `other`, which can be
  either, so give `about` for these two. In an attempt on several datasets,
  give each finding about the data its `datasets` (their folders, as in the
  claims file).

  Give each finding about the data its `severity`: how much it harms someone
  who uses the dataset. Rate what the finding shows, not how much work it
  took to find.

  | `severity` | Meaning | Examples |
  |---|---|---|
  | `critical` | The data are wrong, and nothing in the files shows it. An analysis that takes them as given comes out wrong. | One recording, session or unit deposited as two. Data filed under the wrong subject, session, area or label. Spikes, signals or events on different clocks. A spike train that holds another unit's spikes. Labels that say the opposite of the data. |
[... 121 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/pasquereau-2013-03.yaml; cat entries/pasquereau-2013/README.md; cat questions/pasquereau-2013.yaml 2>/dev/null | head -80
```

```
<persisted-output>
Output too large (44.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/7d5d078e-7ec5-4bc0-a39c-31205c1506c0/tool-results/bvo1dbvd9.txt

Preview (first 2KB):
schema_version: 3
id: pasquereau-2013-03
datasets:
- archive: dandi
  id: '001636'
  version: 0.261124.1906
  doi: 10.48324/dandi.001636/0.261124.1906
  relation: primary
paper: doi:10.3389/fnsys.2013.00098
date: '2026-11-26'
entry: pasquereau-2013
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 35 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/7d5d078e-7ec5-4bc0-a39c-31205c1506c0/tool-results/bvo1dbvd9.txt"
}
```

```
1	schema_version: 3
2	id: pasquereau-2013-03
3	datasets:
4	- archive: dandi
5	  id: '001636'
6	  version: 0.261124.1906
7	  doi: 10.48324/dandi.001636/0.261124.1906
8	  relation: primary
9	paper: doi:10.3389/fnsys.2013.00098
10	date: '2026-11-26'
11	entry: pasquereau-2013
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-19
20	  runner:
[... 690 more lines not kept]
```

**Agent calls Bash**

```bash
ls executed/pasquereau-2013/ 2>/dev/null; python - <<'EOF'
import json
nb=json.load(open('entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    src=''.join(c['source'])
    print(i,c['cell_type'],c.get('metadata',{}).get('tags'),src[:100].replace('\n',' | '))
EOF
```

```
reproduce_pasquereau_2013.ipynb
result.json
0 markdown None # Pasquereau & Turner (2013) on DANDI:001636 |  | Paper: Pasquereau B, Turner RS (2013). Primary motor c
1 code None import time | import warnings |  | import numpy as np | import pandas as pd | import pynwb | import remfile | impo
2 markdown None ## What one file holds |  | One Venus file opened with pynwb: its acquisition and processing series, its
3 code None path, url = venus_urls[0] | with pynwb.NWBHDF5IO(file=h5py.File(remfile.File(url), "r"), load_namespac
4 markdown None ## Loading |  | Every Venus file is streamed once; only windows around each perturbation are kept (spike
5 code None venus = pasq.load_all(venus_urls) | leu = pasq.load_meta_all(leu_urls) | print(f"loaded in {time.time() 
6 code None cells = pasq.cell_responses(venus) | cells["unit"] = cells.groupby("file").cumcount() | cells["studied"]
7 markdown None ## Data check
8 code ['sanity'] all_units = pd.concat([x["units"].assign(subject="Venus", path=x["path"]) for x in venus] |           
9 markdown None ### Recordings deposited twice |  | Each trial's spikes, relative to its trial start, and each perturbat
10 code ['sanity'] from collections import defaultdict | from itertools import combinations |  | def shared(keys_by_file): |   
11 markdown None ### Files made of several source files |  | The trials table's `source_file` names the lab file each tri
12 code ['sanity'] src_files = pd.concat([x["trials"][["source_file"]].assign(file=i) for i, x in enumerate(venus)]) | pe
13 markdown None ### Clocks |  | The torque command, the elbow angle and the spikes are checked against the trials table'
14 code ['sanity'] zt = -pasq.TORQUE_WINDOW_MS[0] | for post in [False, True]: |     cmd = [] |     for x in venus: |         i
15 markdown None The command leaves rest a few ms after the marked onset and the joint moves in the torque's | directio
16 markdown None ### Scale of the angle |  | The paper gives a mean torque-evoked displacement of 10 de
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/pasquereau-2013 && python - <<'EOF'
import json
nb=json.load(open('reproduce_pasquereau_2013.ipynb'))
def out(c):
    s=''
    for o in c.get('outputs',[]):
        if 'text' in o: s+=''.join(o['text'])
        elif 'data' in o and 'text/plain' in o['data']: s+=''.join(o['data']['text/plain'])
    return s
for i in [8,20,21,22]:
    c=nb['cells'][i]
    print('=====',i); print(''.join(c['source'])); print('--- out'); print(out(c)[:5000])
EOF
```

```
===== 8
all_units = pd.concat([x["units"].assign(subject="Venus", path=x["path"]) for x in venus]
                      + [x["units"].assign(subject="Leu", path=x["path"]) for x in leu], ignore_index=True)
print("units by subject, MPTP state and projection type")
print(all_units.groupby(["subject", "post", "ptype"]).size().to_string())
print("unit names repeated across files:", all_units.unit_name.duplicated().sum())
fname_post = all_units.path.str.contains("PostMPTP")
print("units whose is_post_mptp disagrees with the file name:", int((fname_post != all_units.post).sum()))

pert = pd.concat([x["pert"].assign(file=i, post=bool(x["units"].post.iloc[0])) for i, x in enumerate(venus)])
print("\nVenus perturbations by state and direction")
print(pert.groupby(["post", "torque"]).size().to_string())
print("Venus files without any perturbation:", sum(len(x["pert"]) == 0 for x in venus))
print("Leu trials by torque_perturbation_type:",
      pd.Series(np.concatenate([x["torque_type"] for x in leu])).value_counts().to_dict())
print("Leu perturbation onset times that are not NaN:", int(sum(np.isfinite(x["onset"]).sum() for x in leu)))

dates = pd.to_datetime(cells.date)
print("\nVenus recording dates: pre", dates[~cells.post].min().date(), "to", dates[~cells.post].max().date(),
      "; post", dates[cells.post].min().date(), "to", dates[cells.post].max().date())
[... 149 more lines not kept]
```

**Agent calls Bash**

```bash
python - <<'EOF'
import json
nb=json.load(open('reproduce_pasquereau_2013.ipynb'))
def out(c):
    s=''
    for o in c.get('outputs',[]):
        if 'text' in o: s+=''.join(o['text'])
        elif 'data' in o and 'text/plain' in o['data']: s+=''.join(o['data']['text/plain'])
    return s
for i in [14,57,59]+list(range(61,81)):
    c=nb['cells'][i]
    print('=====',i); print(''.join(c['source'])); print('--- out'); print(out(c)[:4000])
EOF
```

```
===== 14
zt = -pasq.TORQUE_WINDOW_MS[0]
for post in [False, True]:
    cmd = []
    for x in venus:
        if x["torque_cmd"] is None or bool(x["units"].post.iloc[0]) != post or len(x["pert"]) == 0:
            continue
        s = np.where(x["pert"].torque.values == "flexion", 1.0, -1.0)[:, None]
        cmd.append(s * (x["torque_cmd"] - x["torque_cmd"][:, :zt].mean(1, keepdims=True)))
    m = np.nanmean(np.vstack(cmd), 0)
    half = np.where(m[zt:] > m[zt:zt + 50].max() / 2)[0][0]
    leave = np.where(m[zt:] > 0.05 * m[zt:zt + 50].max())[0][0]
    print(f"{'post' if post else 'pre'}-MPTP: mean command leaves rest (5% of pulse) at {leave} ms and reaches half its peak at {half} ms after onset")
za = -pasq.ANGLE_WINDOW_MS[0]
for dname, sgn in [("flexion", 1), ("extension", -1)]:
    a = np.vstack([x["angle"][x["pert"].torque.values == dname] for x in venus if x["angle"] is not None and len(x["pert"])])
    disp = np.nanmean(a - a[:, [za]], 0)
    print(f"{dname} torque: mean angle change at 0, 20, 50, 100 ms: "
          + ", ".join(f"{disp[za + t]:+.2f}" for t in [0, 20, 50, 100]) + " deg (positive = flexion)")

[... 366 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "^def \|^[A-Z_]* = " entries/pasquereau-2013/pasq.py | head -60; python - <<'EOF'
import json
nb=json.load(open('entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb'))
for i in [1,5,6]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
EOF
date -u
```

```
67:DANDISET_ID = "001636"
68:DANDISET_VERSION = "0.261124.1906"
70:MIN_PERTURBATIONS = 5
72:KERNEL_MS = 400
73:BASELINE_MS = 500
74:EPOCH_MS = 200
75:ONSET_WINDOW_MS = (20, 60)
76:P_THRESHOLD = 0.002
77:T_CRIT = float(stats.t.ppf(1 - P_THRESHOLD / 2, BASELINE_MS - 1))
78:PSEUDO_SHIFT_MS = 600          # claims, false-positive-rate: pseudo onset 600 ms before torque
82:SPIKE_WINDOW_MS = (-1500, 500)
83:ANGLE_WINDOW_MS = (-200, 400)
84:EMG_WINDOW_MS = (-300, 300)
85:TORQUE_WINDOW_MS = (-50, 100)
86:EMG_CHANNELS = ["EMGTricepsLongus1", "EMGTricepsLongus2", "EMGTricepsLateralis",
88:TRICEPS = ["EMGTricepsLongus1", "EMGTricepsLongus2", "EMGTricepsLateralis"]
91:VELOCITY_THRESHOLD = 5.0       # deg/s, Methods
92:EMG_BASELINE_MS = 200
94:EMG_SEARCH_MS = (10, 150)
97:def asset_urls(subject: str = "sub-Venus") -> list[tuple[str, str]]:
[... 65 more lines not kept]
```

**Agent calls Bash**

```bash
ls -a; ls executed/pasquereau-2013; cat executed/pasquereau-2013/result.json | head -30; grep -n "venv\|env_dir\|\.venv" tools/entry.py | head -20
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
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q --python 3.13 v && uv pip install -q --python v/bin/python -r entries/pasquereau-2013/requirements.lock.txt 2>&1 | tail -3; v/bin/python -c "import pynwb, statsmodels; print('ok')"
```

**Agent calls Bash**

```bash
sed -n 460,560p entries/pasquereau-2013/pasq.py
```

```
ok
Shell cwd was reset to
```

```
def session_kinematics(files: list[dict]) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Per-perturbation kinematics with the torque command's pulse size, and session means per
    direction. The pulse size is the command over 10 to 50 ms after onset less its mean over the
    50 ms before, signed so that the torque's direction is positive (arbitrary units)."""
    rows = []
    for fi, x in enumerate(files):
        if x["angle"] is None or len(x["pert"]) == 0:
            continue
        dirs = x["pert"].torque.values
        k = kinematics(x["angle"], dirs)
        sign = np.where(dirs == "flexion", 1.0, -1.0)
        z = -TORQUE_WINDOW_MS[0]
        cmd = x["torque_cmd"]
        k["command"] = sign * (cmd[:, z + 10:z + 50].mean(1) - cmd[:, :z].mean(1))
        # Peak of the file's own ElbowVelocity series over 0 to 200 ms, signed as above
        if x["velocity"] is not None:
            za = -ANGLE_WINDOW_MS[0]
            k["file_peak_velocity"] = (sign[:, None] * x["velocity"][:, za:za + 200]).max(1)
        k["direction"], k["file"], k["session"] = dirs, fi, x["session"]
        k["post"] = bool(x["units"].post.iloc[0])
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pasquereau-2013 && cat > $TMPDIR/load.py <<'EOF'
import pickle, time, resource
import pasq
t=time.time()
venus = pasq.load_all(pasq.asset_urls("sub-Venus"))
kt, ks = pasq.session_kinematics(venus)
# keep only what's needed for variants: pert, torque_cmd, emg triceps, units post, session, angle
slim=[{k:x[k] for k in ["pert","torque_cmd","emg","units","session","angle","velocity","trials","path"] if k in x} for x in venus]
pickle.dump((slim,kt,ks), open(__import__('os').environ['TMPDIR']+"/venus.pkl","wb"))
print(time.time()-t, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6,"GB")
EOF
$TMPDIR/v/bin/python $TMPDIR/load.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/load.py", line 2, in <module>
    import pasq
ModuleNotFoundError: No module named 'pasq'
```

**Agent calls Bash**

```bash
cd entries/pasquereau-2013 && PYTHONPATH=. $TMPDIR/v/bin/python $TMPDIR/load.py
```

```
806.2456510066986 0.975912 GB
```

**Agent calls Bash**

```bash
PYTHONPATH=. $TMPDIR/v/bin/python - <<'EOF'
import pickle,os,numpy as np,pandas as pd
slim,kt,ks=pickle.load(open(os.environ['TMPDIR']+"/venus.pkl","rb"))
print(pd.crosstab(kt.post, pd.cut(kt.command,[0,30,40,50,60,70,80,85,90,95,100,110,120,140,160,175,185,200,250,400])).T)
EOF
date -u
```

```
post        False  True 
command                 
(0, 30]        13      2
(30, 40]        0      5
(40, 50]     1372      4
(50, 60]        0     20
(60, 70]        0     28
(70, 80]        0     44
(80, 85]        0     23
(85, 90]        4     27
(90, 95]      479    200
(95, 100]       0     33
(100, 110]      0     70
(110, 120]      0     69
(120, 140]      0    189
(140, 160]      0    252
(160, 175]      0    205
(175, 185]     41   1540
(185, 200]      0    191
(200, 250]      0    469
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
PYTHONPATH=. $TMPDIR/v/bin/python - <<'EOF'
import pickle,os,numpy as np,pandas as pd, statsmodels.api as sm, statsmodels.formula.api as smf
from scipy import stats
import pasq
slim,kt,ks=pickle.load(open(os.environ['TMPDIR']+"/venus.pkl","rb"))
def anova(df, meas):
    return sm.stats.anova_lm(smf.ols(f"{meas} ~ C(post) * C(direction)", data=df).fit(), typ=2)
for lo,hi in [(85,95),(175,185)]:
    m=kt[kt.command.between(lo,hi)]
    print(lo,hi,"perts",m.groupby(['post','direction']).size().to_dict(),"median cmd",m.groupby('post').command.median().round(2).to_dict())
    ms=m.groupby(["file","post","direction"])[["latency","peak_velocity","amplitude","latency_quiet","latency_causal"]].mean().reset_index()
    print(" sessions",ms.groupby(['post','direction']).size().to_dict())
    for meas in ["peak_velocity","amplitude","latency","latency_quiet","latency_causal"]:
        s=ms.dropna(subset=[meas]); a=anova(s,meas)
        print(f"  {meas}: {s.groupby(['post','direction'])[meas].mean().round(2).to_dict()} F={a.loc['C(post)','F']:.1f} p={a.loc['C(post)','PR(>F)']:.2g}")
    em=pasq.session_emg(slim,command_range=(lo,hi))
    um=em[~em.has_nan&(em.baseline_sd>=1)]
    print(" emg used",um.groupby(['channel','post']).size().to_dict())
    for ch,g in um.groupby('channel'):
        a,b=g[~g.post].m2,g[g.post].m2
        if len(a) and len(b): print(f"  m2 {ch}: {a.median():.1f} {b.median():.1f} p={stats.ks_2samp(a,b).pvalue:.2g}")
    d=um.dropna(subset=['duration']); a,b=d[~d.post],d[d.post]
    print(f"  dur {a.duration.mean():.1f} {b.duration.mean():.1f} p={stats.ks_2samp(a.duration,b.duration).pvalue:.2g}; onset {a.onset.mean():.1f} {b.onset.mean():.1f} p={stats.ks_2samp(a.onset,b.onset).pvalue:.2g}")
    for post,g in um.groupby('post'): print(f"  m1w {post}: {100*(g.m2>g.m1).mean():.1f}% of {len(g)}, ratio {(g.m1/g.m2).median():.2f}")
EOF
```

```
/tmp/claude-1001/v/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1998: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
entries/pasquereau-2013/pasq.py:521: RuntimeWarning: Mean of empty slice
  "level": float(np.nanmean(w[:, z - EMG_BASELINE_MS:z])), **m})
/tmp/claude-1001/v/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1998: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
entries/pasquereau-2013/pasq.py:521: RuntimeWarning: Mean of empty slice
  "level": float(np.nanmean(w[:, z - EMG_BASELINE_MS:z])), **m})
/tmp/claude-1001/v/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1998: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
entries/pasquereau-2013/pasq.py:521: RuntimeWarning: Mean of empty slice
  "level": float(np.nanmean(w[:, z - EMG_BASELINE_MS:z])), **m})
/tmp/claude-1001/v/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1998: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
entries/pasquereau-2013/pasq.py:521: RuntimeWarning: Mean of empty slice
  "level": float(np.nanmean(w[:, z - EMG_BASELINE_MS:z])), **m})
/tmp/claude-1001/v/lib/python3.13/site-packages/numpy/lib/_nanfunctions_impl.py:1998: RuntimeWarning: Degrees of freedom <= 0 for slice.
  var = nanvar(a, axis=axis, dtype=dtype, out=out, ddof=ddof,
entries/pasquereau-2013/pasq.py:521: RuntimeWarning: Mean of empty slice
  "level": float(np.nanmean(w[:, z - EMG_BASELINE_MS:z])), **m})
[... 59 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -A30 "id: kinematics-slower\|id: kinematic-latency-unchanged\|id: emg-m2-larger\|id: emg-duration-longer\|id: emg-onset-unchanged\|id: emg-m1-weak" claims/pasquereau-2013.yaml | grep -v "^--$" | head -230; sed -n 1,40p claims/pasquereau-2013.yaml
```

```
601:- id: kinematics-slower
602-  statement: After MPTP, torque-induced displacements were slower and smaller; mean peak velocity
603-    fell by 16.2% and amplitude by 6.6% (ANOVA, F > 515 and F > 49).
604-  source: Results, Behavioral effects of MPTP, paragraph 2; Figure 1
605-  quote: Induction of parkinsonism also led to a slowing of torque-induced displacements of the arm
606-    (ANOVA; F > 515, p < 0.001; Figure 1) and a reduction in movement amplitude (F > 49, p < 0.01).
607-  statistics:
608-  - about: peak velocity, pre against post MPTP
609-    test: ANOVA
610-    statistic: F > 515
611-    p: 0.001
612-    p_relation: "<"
613-  - about: amplitude, pre against post MPTP
614-    test: ANOVA
615-    statistic: F > 49
616-    p: 0.01
617-    p_relation: "<"
618-  expected:
619-  - quantity: change of peak velocity after MPTP
620-    value: -16.2
[... 145 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pasquereau-2013 && PYTHONPATH=. $TMPDIR/v/bin/python - <<'EOF' 2>&1 | grep -v Warning
import pickle,os,numpy as np,pandas as pd
slim,kt,ks=pickle.load(open(os.environ['TMPDIR']+"/venus.pkl","rb"))
x=slim[0]
print(x['trials'].columns.tolist()); print(x['pert'].columns.tolist())
print(x['trials'].head(3).T)
p=pd.concat([s['pert'] for s in slim])
d=(p.onset-p.center).round(4)
print(d.value_counts().head(10))
EOF
grep -n "center\|onset" pasq.py | sed -n 1,30p
```

```
['start', 'stop', 'center', 'torque', 'onset', 'movement', 'source_file', 'target_amplitude', 'mov_onset', 'mov_end', 'derived_peak_velocity', 'derived_amplitude', 'angle_at_mov_onset', 'angle_at_mov_end']
['start', 'stop', 'center', 'torque', 'onset', 'movement', 'source_file', 'target_amplitude', 'mov_onset', 'mov_end', 'derived_peak_velocity', 'derived_amplitude']
                               0          1           2
start                        0.0     12.203      23.499
stop                       9.203     20.499      31.782
center                     2.766     14.302      25.573
torque                   flexion  extension   extension
onset                      4.463     15.998      27.269
movement                 flexion  extension     flexion
source_file                v0502      v0502       v0502
target_amplitude            20.0       20.0        20.0
mov_onset                  7.489     18.688      30.115
mov_end                    7.791     19.158      30.488
derived_peak_velocity  118.66013  94.408327  107.853065
derived_amplitude         20.184   -20.0796   18.642524
angle_at_mov_onset     -0.459788   0.578952    2.100354
angle_at_mov_end       19.735896 -19.494065   20.696452
1.696    3010
1.697    1859
1.698      83
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls paper; grep -rn -i "random\|1–2\|1-2 s\|captur" paper/* | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  grep -o -i ".\{300\}random.\{300\}" paper/10.3389-fnsys.2013.00098.txt | head -5; grep -o -i ".\{200\}0\.1 Nm.\{200\}" paper/10.3389-fnsys.2013.00098.txt | head -3
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb'))
for i in [0,18,26,29,84]:
    print('=====',i); print(''.join(nb['cells'][i]['source']))
EOF
```

```
===== 0
# Pasquereau & Turner (2013) on DANDI:001636

Paper: Pasquereau B, Turner RS (2013). Primary motor cortex of the parkinsonian monkey: altered
neuronal responses to muscle stretch. *Front. Syst. Neurosci.* 7:98,
[doi:10.3389/fnsys.2013.00098](https://doi.org/10.3389/fnsys.2013.00098).

Dataset: [DANDI:001636](https://dandiarchive.org/dandiset/001636/0.261124.1906), version
`0.261124.1906` (doi:10.48324/dandi.001636/0.261124.1906). This version was asked for in the
prompt of this attempt; it is also the newest published version (published 2026-11-24). The
paper cites no version.

Claims: `claims/pasquereau-2013.yaml`, written from the full text in PubMed Central
(PMC3840326), its Methods, Results, Table 1, figure legends and supplementary data sheet
(DataSheet1.PDF), whose table gives the results for each monkey.

The files of monkey L mark no torque perturbation, so every claim is tested on monkey V
(Venus, elbow), as the claims file says.

| Claim | Tested or blocked |
[... 82 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/pasquereau-2013 && PYTHONPATH=. $TMPDIR/v/bin/python - <<'EOF' 2>&1 | grep -v Warn
import pickle,os,numpy as np,pandas as pd
from scipy import stats
slim,kt,ks=pickle.load(open(os.environ['TMPDIR']+"/venus.pkl","rb"))
print(stats.f.sf(709.4511,1,577))
p=pd.concat([s['pert'].assign(post=bool(s['units'].post.iloc[0])) for s in slim])
d=p.onset-p.center
print(d.between(1.695,1.698).mean(), d.between(1,2).mean(), d.min(), d.max())
print(d.groupby(p.post).apply(lambda s: s.between(1.695,1.698).mean()))
# fraction of files whose median delay is 1.696-1.697
fm=[ (s['pert'].onset-s['pert'].center).median() for s in slim]
print(np.mean([1.695<=f<=1.698 for f in fm]))
# start-to-center
t=pd.concat([s['trials'] for s in slim]); print((t.center-t.start).describe())
EOF
```

```
1.5454377681451828e-102
0.8836036036036036 0.972072072072072 1.2569999999999908 11.840999999999951
post
False    0.891628
True     0.879267
dtype: float64
0.9896907216494846
count    8360.000000
mean        2.437483
std         0.724770
min         1.272000
25%         2.047000
50%         2.336000
75%         2.633000
max        11.420000
dtype: float64
```

**Agent calls Bash**

```bash
cd  date -u; python - <<'EOF'
import json
nb=json.load(open('entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb'))
for i in [41,42,43]:
    print('=====',i); print(''.join(nb['cells'][i]['source'])[:1500])
print(nb['cells'][22]['metadata'], nb['metadata'].keys(), nb['cells'][22].keys())
EOF
```

```
Thu Nov 26 19:11:18 UTC 2026
===== 41
**Result: blocked (methods underspecified).** The claims file's detection crosses its threshold in
0.23 of cell-directions after a pseudo onset (0.20 in trials without a torque), far above the
paper's 0.01 and outside 0.0033 to 0.03, so this procedure is not the paper's. Of the other
readings, only a threshold from the SD of all single-trial baseline values comes near 0.01
(0.013), and it calls only 0.20 of real cell-directions responsive, far below the paper's 62 to
75% of cells; no reading gives both. The question of
which test the Methods mean is asked of a reader (`questions/pasquereau-2013.yaml`) and of the
authors (findings).
===== 42
### Claims that use the selection of responses (blocked, shown)

These claims depend on `torque-related-fractions`, which depends on `false-positive-rate`, and are
blocked with it. Their results under the claims file's detection are computed here so that a later
attempt, or the authors, can see them; they decide nothing.

Each cell also gives the results under the `trial_sd` reading (threshold from the SD of all
single-trial SDF values over the baseline), the one reading of the Methods' t-test whose
false-positive rate (0.013) falls inside 0.0033 to 0.03 (cell `claim:false-positive-rate`). It
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/edit.py <<'PYEOF'
import json, uuid
P='entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb'
nb=json.load(open(P))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
def code(s,tags): return {"cell_type":"code","execution_count":None,"id":uuid.uuid4().hex[:8],"metadata":{"tags":tags},"outputs":[],"source":s.splitlines(keepends=True)}
def md(s): return {"cell_type":"markdown","id":uuid.uuid4().hex[:8],"metadata":{},"source":s.splitlines(keepends=True)}
def rep(i,a,b):
    s=src(i); assert a in s,(i,a); setsrc(i,s.replace(a,b))

ALL_EMG=['claim:emg-m2-larger','claim:emg-duration-longer','claim:emg-onset-unchanged','claim:emg-m1-weak']

# --- summary (84)
setsrc(84, src(84).split("How the analysis differs")[0] + """How the analysis differs from the paper's: monkey V only; units are this dataset's files' units;
the response detection is the claims file's, whose false-positive rate is about 20 times the
paper's, so no claim that rests on the response selection is decided; kinematic and EMG
parameters the paper does not give are the claims file's or standard choices (`pasq.py`).

Revisions after verification: the onset of the evoked movement was also measured with a causal
filter and with a below-threshold requirement; both give shorter latencies after MPTP over all
perturbations, and only the causal filter avoids the spread of the forwards-backwards filter. The
kinematic and EMG claims were repeated at equal torque command pulses (85 to 95 and 175 to 185
units, the two pulse sizes both states share). There the outcome by the criterion changes for
kinematic-latency-unchanged, emg-onset-unchanged and emg-m1-weak (reproduced) and for
emg-duration-longer (not reproduced); these changes are proposed in the attempt record, not
applied, and rest on few post-MPTP sessions at 85 to 95 units and few pre-MPTP sessions at 175
to 185. The claims on the response selection were shown under the `trial_sd` reading, which meets
the paper's false-positive rate but finds about a quarter of the paper's responsive cells.

What was found about the dataset: the counts of cells by state and projection type are within 3
cells of the paper's monkey V table (115 against 112 before MPTP); no recording is deposited
twice; the Leu files hold no perturbation times; the torque command's pulses are larger after
MPTP than before (mean 174.7 against 58.4 units, about three times; median 181.6 against 45.7,
about four times); the evoked displacements (2.4 to 3.8 degrees by state and direction) are
smaller than the paper's 10 degrees and faster, not slower, after MPTP; the angle's scale is
consistent with the 20 degree targets and the file's own velocity series, so this is in the data.
Twelve files join two lab source files without repeating trials. In the one post-MPTP Leu file
whose torque command was timed against task events, the command moves at those events, not at
times where perturbations would fall. In 88% of Venus perturbations the onset is 1.695 to 1.698 s
after the centre target appears, where the paper describes a delay drawn uniformly from 1 to 2 s.
""")

# --- EMG conclusions
setsrc(80, """**Result: partially reproduced.** After MPTP m2 exceeds m1 in 98.3% of channel-sessions and the
median m1/m2 is 0.25; before MPTP the median ratio is 0.14 but m2 exceeds m1 in 74.0%, just under
the 75% the criterion asks (74.3% under the other channel rule). Not deciding: at command pulses
of 60 to 250 units, which still differ about twofold between states, m2 exceeds m1 in 94.9% of
pre-MPTP and 97.1% of post-MPTP channel-sessions; at equal pulses of 85 to 95 units in 96.3% (54
channel-sessions, median ratio 0.10) and 85.7% (14, 0.39), and at 175 to 185 units in 80.0% (5,
0.19) and 95.2% (186, 0.32). The criterion is met in both states at equal pulses, so the pre-MPTP
shortfall comes from sessions with small pulses. A change to reproduced is proposed in the record.
""")
setsrc(78, """**Result: not reproduced.** The earliest EMG responses start earlier after MPTP (44.2 against 25.0
ms on average, KS p < 1e-20). Not deciding: at command pulses of 60 to 250 units, which still
differ about twofold, the onset is also earlier after MPTP (33.3 against 24.7 ms, KS p = 8.5e-07),
but at equal pulses it does not differ (85 to 95 units, 33.0 against 32.3 ms, KS p = 0.40; 175 to
185 units, 37.4 against 24.9 ms, KS p = 0.057, 5 pre-MPTP channel-sessions). The earlier onset
over all perturbations goes with the larger post-MPTP pulse; a change to reproduced is proposed in
the record.
""")
setsrc(76, """**Result: partially reproduced.** Durations are longer after MPTP (22.2 against 51.5 ms, KS
p < 1e-30), but both means are far outside the paper's 57 +/- 6 and 79 +/- 3 ms. Not deciding: at
command pulses of 60 to 250 units, which still differ about twofold, the durations are 32.0 and
51.1 ms; at equal pulses they are not longer after MPTP (85 to 95 units, 32.4 against 24.1 ms, KS
p = 0.32; 175 to 185 units, 27.0 against 46.7 ms, KS p = 0.087, 5 pre-MPTP channel-sessions). A
change to not reproduced is proposed in the record.
""")
setsrc(74, """**Result: reproduced.** m2 is larger after MPTP in all three triceps channels (KS p < 1e-14 in
each) under both channel rules. The torque pulses are larger after MPTP (cell
`finding-torque-command-levels`), and this comparison cannot separate pulse size from MPTP. At
command pulses of 60 to 250 units (median 90.9 and 181.8, still about twofold apart) m2 is larger
after MPTP in every channel (KS p 7.5e-08 to 2.2e-15). At equal pulses of 85 to 95 units it is
larger after MPTP in both triceps longus channels (KS p = 0.016 and 0.0017), but the triceps
lateralis has only 2 post-MPTP sessions there (median 19.6 before, 15.8 after, p = 0.64), and at
175 to 185 units it has no pre-MPTP session, so the criterion cannot be applied at equal pulses
and no change is proposed. The background also differs between the states: the median
single-trial baseline SD of triceps longus 2 is 2.98 units before and 19.58 after MPTP, and half
of its pre-MPTP session averages have a baseline SD below 1 unit; the pre-MPTP m2 medians (4.6 to
10.3 units) are close to that background.
""")
setsrc(71, """### EMG claims at other torque commands (variants)

The command pulse is larger after MPTP (cell `finding-torque-command-levels`). The four EMG
measures are computed again, with the main channel rule, on the perturbations whose pulse is 60
to 250 units (where both states have pulses, though their medians still differ about twofold),
and on the perturbations at the two pulse sizes both states use, 85 to 95 and 175 to 185 units
(equal pulses). Not deciding.
""")
eq_emg = code("""# Equal pulses: the two pulse sizes both states use (cell finding-torque-command-levels)
EQUAL_PULSES = [(85, 95), (175, 185)]
for lo, hi in EQUAL_PULSES:
    fl = kin_trials[(kin_trials.direction == "flexion") & kin_trials.command.between(lo, hi)]
    print(f"pulses {lo} to {hi} units: flexion perturbations {fl.groupby('post').size().to_dict()}, "
          f"median command {fl.groupby('post').command.median().round(1).to_dict()}")
    e_ = pasq.session_emg(venus, command_range=(lo, hi))
    ue = e_[~e_.has_nan & (e_.baseline_sd >= 1)]
    print("  channel-sessions used:", ue.groupby(["channel", "post"]).size().to_dict())
    for ch, g in ue.groupby("channel"):
        a, b = g[~g.post].m2, g[g.post].m2
        if len(a) and len(b):
            print(f"  m2 {ch}: median pre {a.median():.1f}, post {b.median():.1f}, n {len(a)} and {len(b)}, "
                  f"KS p = {stats.ks_2samp(a, b).pvalue:.2g}")
        else:
            print(f"  m2 {ch}: n {len(a)} and {len(b)}, no test")
    d = ue.dropna(subset=["duration"])
    a, b = d[~d.post], d[d.post]
    print(f"  duration pre {a.duration.mean():.1f} ms (n {len(a)}), post {b.duration.mean():.1f} (n {len(b)}), "
          f"KS p = {stats.ks_2samp(a.duration, b.duration).pvalue:.2g}")
    print(f"  onset pre {a.onset.mean():.1f} ms, post {b.onset.mean():.1f}, KS p = {stats.ks_2samp(a.onset, b.onset).pvalue:.2g}")
    for post, g in ue.groupby("post"):
        print(f"  {'post' if post else 'pre'}: m2 > m1 in {100 * (g.m2 > g.m1).mean():.1f}% of {len(g)}, "
              f"median m1/m2 {(g.m1 / g.m2).median():.2f}")
""", ALL_EMG)
C.insert(73, eq_emg)

# --- kinematic latency
setsrc(67, """**Result: not reproduced.** The movement onset latency is shorter after MPTP, MPTP effect F = 709,
p = 1.5e-102 (printed above); the MPTP by direction interaction is F = 16.1 (the paper's F > 94).
The claims file's filter moves onsets early after MPTP: 6.7% of post-MPTP onsets are at 0 ms with
the velocity already above 5 deg/s (0.1% before). The below-threshold variant removes these but
not the spread of the forwards-backwards filter: its post-MPTP flexion mean (3.38 ms) is still
before the command leaves rest at 4 ms (cell 14). Only the causal filter avoids both; it also
gives shorter latencies after MPTP (pre 21.44 and 20.33, post 18.18 and 15.62 ms; F = 422.5), with
a smaller difference (3.3 and 4.7 ms, against 4.9 and 6.6 ms with the claims file's onset), so
the filter enlarges the difference. The unfiltered velocity also rises earlier after MPTP (5.1
against 1.7 deg/s at 10 ms, 13.2 against 4.0 at 12 ms).

Not deciding: at command pulses of 60 to 250 units, which still differ about twofold, the
latencies remain shorter (F = 214.3 and 146.2 for the two variants). At equal pulses (cell
above) the MPTP effect on the claims file's onset is F = 2.0, p = 0.16 at 85 to 95 units and
F = 0.0, p = 0.98 at 175 to 185 units; the causal filter gives F = 9.3, p = 0.0027 at 85 to 95
units, with post-MPTP latencies longer by under 1 ms, and F = 0.2, p = 0.69 at 175 to 185. The
shorter latency over all perturbations goes with the larger post-MPTP pulse; a change to
reproduced is proposed in the record.
""")
rep(66, 'print(a.round(4))\n', 'print(a.round(4))\nprint("MPTP effect: F = %.1f on 1 and %d df, p = %.2g" % (a.loc["C(post)", "F"], a.loc["Residual", "df"],\n                                                   stats.f.sf(a.loc["C(post)", "F"], 1, a.loc["Residual", "df"])))\n')
# --- kinematics conclusions
setsrc(64, """**Result: not reproduced.** Under both readings the displacements are faster and larger after
MPTP, not slower and smaller (peak velocity +28.1% pooled and +29.7% for flexion; amplitude +14.8%
and +11.1%; MPTP F = 98.5 and 25.0). Restricted to command pulses of 60 to 250 units the increase
remains (+47.0% and +40.4%), but there the pulses still differ about twofold (median 90.9 against
181.8 units, cell `claim:emg-m2-larger` below), so pulse size is not excluded. At equal pulses
(cell above) the displacements are not slower and smaller after MPTP either: at 85 to 95 units
peak velocity and amplitude are higher after MPTP (MPTP F = 4.3, p = 0.04, and F = 3.9, p =
0.049, from faster flexion responses in 15 post-MPTP sessions), and at 175 to 185 units peak
velocity does not differ (F = 0.0, p = 0.95) and amplitude is smaller after MPTP (F = 7.8, p =
0.0055, 4 pre-MPTP sessions per direction). Neither meets the criterion, so the outcome would be
the same at equal pulses.
""")
eq_kin = code("""# Equal pulses: the two pulse sizes both states use (cell finding-torque-command-levels)
for lo, hi in [(85, 95), (175, 185)]:
    m_ = kin_trials[kin_trials.command.between(lo, hi)]
    s_ = m_.groupby(["file", "post", "direction"])[["latency", "peak_velocity", "amplitude", "latency_quiet",
                                                     "latency_causal"]].mean().reset_index()
    print(f"pulses {lo} to {hi} units: perturbations {m_.groupby(['post', 'direction']).size().to_dict()}, "
          f"median command {m_.groupby('post').command.median().round(1).to_dict()}; "
          f"sessions {s_.groupby(['post', 'direction']).size().to_dict()}")
    for meas in ["peak_velocity", "amplitude", "latency", "latency_quiet", "latency_causal"]:
        s = s_.dropna(subset=[meas])
        a = anova(s, meas)
        ch = 100 * (s[s.post][meas].mean() / s[~s.post][meas].mean() - 1)
        print(f"  {meas}: means {s.groupby(['post', 'direction'])[meas].mean().round(2).to_dict()}, change {ch:+.1f}%, "
              f"MPTP F = {a.loc['C(post)', 'F']:.1f}, p = {a.loc['C(post)', 'PR(>F)']:.2g}")
""", ['claim:kinematics-slower','claim:kinematic-latency-unchanged'])
C.insert(64, eq_kin)
setsrc(62, """A variant, not deciding: the pulse of the torque command is larger after MPTP (cell
`finding-torque-command-levels`). Restricting to perturbations whose command pulse is 60 to 250
units keeps the range both states have pulses in, though the pulses there still differ about
twofold. The next cell compares the states at equal pulses: 85 to 95 units, the larger pre-MPTP
level, which some post-MPTP sessions also use, and 175 to 185 units, the usual post-MPTP level,
which a few pre-MPTP sessions use.
""")

# --- 59 blocked summary
rep(59, """No session has a mean peak velocity in the 130 to 200 deg/s range of
velocity-matched-magnitude under either reading.""", """Only 2 of 581 session-directions have a mean peak velocity in the 130 to 200 deg/s range
of velocity-matched-magnitude (cell `finding-kinematics-vs-paper`); they hold one post-MPTP
flexion response under the claims file's detection and none under `trial_sd`.""")

# --- new finding cell after 22
fcell = code("""# Perturbation onset against the centre target: the paper gives an unpredictable delay, uniform over 1 to 2 s.
delay = pert.onset - pert.center
print("perturbations:", len(delay), "; delay from centre target appearance to torque onset (s): min %.3f, max %.3f"
      % (delay.min(), delay.max()))
print("fraction 1.695 to 1.698 s: %.3f (pre %.3f, post %.3f); fraction 1 to 2 s: %.3f"
      % (delay.between(1.695, 1.698).mean(), delay[~pert.post].between(1.695, 1.698).mean(),
         delay[pert.post].between(1.695, 1.698).mean(), delay.between(1, 2).mean()))
print("most common delays (s):", delay.round(3).value_counts().head(5).to_dict())
file_median = delay.groupby(pert.file).median()
print("files whose median delay is 1.695 to 1.698 s: %d of %d" % (file_median.between(1.695, 1.698).sum(), len(file_median)))
""", ['finding-perturbation-timing'])
C.insert(23, fcell)

# --- cell 21 comment
rep(21, "# The torque command's pulse is about three times larger after MPTP;", "# The torque command's pulse is larger after MPTP (means about three times, medians about four);")
# --- cell 20 comment (Leu timing)
rep(20, "# against its trials' events; Venus perturbations come 1.7 s after the centre target appears.",
    "# against its trials' events; Venus perturbations come 1.7 s after the centre target appears\n# (cell finding-perturbation-timing), though the paper gives 1 to 2 s. Only this file is timed.")
# --- header revision note
rep(0, """Revised after the first round of verification: the source files within each file, the angle's
scale, the Leu torque command, the blocked claims under the `trial_sd` reading, variants of the
kinematic onset and the EMG claims at matched torque commands were added.""",
"""Revised after the first round of verification: the source files within each file, the angle's
scale, the Leu torque command, the blocked claims under the `trial_sd` reading, variants of the
kinematic onset and the EMG claims at commands of 60 to 250 units were added. Revised after the
second round: the kinematic and EMG claims at equal torque pulses, the timing of the
perturbations against the centre target, and the exact p of the latency ANOVA were added, and
conclusions the outputs did not support were corrected.""")
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
PYEOF
python $TMPDIR/edit.py && git diff --stat 2>/dev/null; python -c "
import json;nb=json.load(open('entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb'))
for i,c in enumerate(nb['cells']): print(i,c['metadata'].get('tags'),''.join(c['source'])[:70].replace(chr(10),' '))" | sed -n 18,30p
```

```
17 ['sanity'] vol = pd.concat([x["trials"].assign(post=bool(x["units"].post.iloc[0])
18 None The angle's scale agrees with the task: voluntary movements to 20 degr
19 None ### Findings about the data  Each cell below shows one problem, loadin
20 ['finding-leu-no-perturbations'] # Monkey L: no perturbation times, and no pulses in the torque command
21 ['finding-torque-command-levels'] # The torque command's pulse is larger after MPTP (means about three t
22 ['finding-kinematics-vs-paper'] # Torque-evoked displacements: the paper's mean is 10 degrees, and slo
23 ['finding-perturbation-timing'] # Perturbation onset against the centre target: the paper gives an unp
24 None ## Claims
25 None ### cell-counts  > In monkey V, 112 neurons were studied before MPTP a
26 ['claim:cell-counts'] expected = {"M1": (112, 159), "PTN": (49, 54), "CSN": (31, 48)} for g,
27 None **Result: reproduced.** 115 and 157 cells before and after MPTP (112 a
28 None ### monkey-l-perturbations  > In monkey L, 57 of 115 neurons before MP
29 ['claim:monkey-l-perturbations'] print("Leu units by state:", all_units[all_units.subject == "Leu"].gro
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
P='entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb'
nb=json.load(open(P))
for c in nb['cells']:
    s=''.join(c['source'])
    if s.startswith('**Result: not reproduced.** The movement onset latency'):
        s=s.replace("before the command leaves rest at 4 ms (cell 14).","before the command leaves rest at 4 ms (data check, clocks).")
        s=s.replace("At equal pulses (cell\nabove)","At equal pulses (the second\ncell under kinematics-slower)")
        assert "data check, clocks" in s and "second\ncell" in s
        c['source']=s.splitlines(keepends=True)
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
git status --short 2>/dev/null | head; date -u
```

```
Thu Nov 26 19:12:19 UTC 2026
```

**Agent calls Bash**

```bash
cd  head -c 300 entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb; echo; head -c 300 executed/pasquereau-2013/reproduce_pasquereau_2013.ipynb
```

```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f94066aa",
   "metadata": {},
   "source": [
    "# Pasquereau & Turner (2013) on DANDI:001636\n",
    "\n",
    "Paper: Pasquereau B, Turner RS (2013). Primary motor cortex of the parkinsonian monkey: altered\n",
    "neuronal responses to mus
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "f94066aa",
   "metadata": {},
   "source": [
    "# Pasquereau & Turner (2013) on DANDI:001636\n",
    "\n",
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  time python tools/entry.py all entries/pasquereau-2013 2>&1 | tail -15; date -u
```

```
Installed kernelspec registry-pasquereau-2013 in executed/pasquereau-2013/.venv/share/jupyter/kernels/registry-pasquereau-2013
0 error(s)
pass  reproduce_pasquereau_2013.ipynb  (842 s)

real	14m15.213s
user	1m7.038s
sys	0m11.339s
Thu Nov 26 19:26:41 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/pasquereau-2013 && python - <<'EOF'
import json
nb=json.load(open('reproduce_pasquereau_2013.ipynb'))
def out(c):
    s=''
    for o in c.get('outputs',[]):
        if 'text' in o: s+=''.join(o['text'])
        elif 'data' in o and 'text/plain' in o['data']: s+=''.join(o['data']['text/plain'])
    return s
for i,c in enumerate(nb['cells']):
    t=c['metadata'].get('tags',[])
    if 'finding-perturbation-timing' in t or 'finding-torque-command-levels' in t or (c['cell_type']=='code' and ('EQUAL' in ''.join(c['source']) or 'Equal pulses' in ''.join(c['source']) or 'MPTP effect: F' in ''.join(c['source']))):
        print('=====',i,t); print(out(c)[:3000])
EOF
```

```
===== 21 ['finding-torque-command-levels']
        count   mean   std   min    25%    50%    75%    max
post                                                        
False  1947.0   58.4  28.1  -0.7   45.3   45.7   90.3  182.7
True   3603.0  174.7  47.6  26.0  155.3  181.6  184.5  343.5

sessions by median pulse size (a.u.), pre and post:
command  (30, 60]  (60, 120]  (120, 250]
post                                    
False         105         43           3
True            0         12         125

===== 23 ['finding-perturbation-timing']
perturbations: 5550 ; delay from centre target appearance to torque onset (s): min 1.257, max 11.841
fraction 1.695 to 1.698 s: 0.884 (pre 0.892, post 0.879); fraction 1 to 2 s: 0.972
most common delays (s): {1.696: 3010, 1.697: 1859, 1.698: 83, 1.7: 22, 1.699: 22}
files whose median delay is 1.695 to 1.698 s: 288 of 291

===== 65 ['claim:kinematics-slower', 'claim:kinematic-latency-unchanged']
pulses 85 to 95 units: perturbations {(False, 'extension'): 246, (False, 'flexion'): 237, (True, 'extension'): 127, (True, 'flexion'): 100}, median command {False: 90.8, True: 90.8}; sessions {(False, 'extension'): 42, (False, 'flexion'): 41, (True, 'extension'): 43, (True, 'flexion'): 15}
[... 57 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls schemas; grep -n -B2 -A25 '"proposed"' schemas/*attempt* | head -60; grep -n -A40 '"verifications"' schemas/*attempt* | grep -n "findings\|severity\|agrees\|number\|finding" | head
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
315-            "description": "True when the outcome is not the same under all five seeds the protocol asks for (docs/protocol.md, Author, step 3)."
316-          },
317:          "proposed": {
318-            "description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
319-            "type": "object",
320-            "additionalProperties": false,
321-            "required": [
322-              "outcome",
323-              "reason"
324-            ],
325-            "properties": {
326-              "outcome": {
327-                "enum": [
328-                  "reproduced",
329-                  "partially_reproduced",
330-                  "not_reproduced",
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 395,520p schemas/attempt.schema.json
```

```
}
          }
        ]
      }
    },
    "verifications": {
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
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python -c "import ruamel.yaml; print(ruamel.yaml.__version__)"; python -c "import yaml; print(yaml.__version__)"
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import ruamel.yaml; print(ruamel.yaml.__version__)
    ^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'ruamel'
6.0.4
```

**Agent calls Read**

```json
{
 "file_path": "attempts/pasquereau-2013-03.yaml",
 "limit": 5
}
```

```
1	schema_version: 3
2	id: pasquereau-2013-03
3	datasets:
4	- archive: dandi
5	  id: '001636'
```

**Agent**

Now the monkey-L notes and torque-related-fractions notes.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/pasquereau-2013-03.yaml",
 "old_string": "    none 1 to 2.5 s after it where the Venus perturbations fall (1.7 s), and 55 within 0.15 s of a voluntary\n    movement onset; they are timed to the task, not to perturbations. The criterion",
 "new_string": "    none 1 to 2.5 s after it where the Venus perturbations fall (1.7 s), and 55 within 0.15 s of a voluntary\n    movement onset; they are timed to the task, not to perturbations. Only this one of the 34 files was timed\n    against task events. The 1.7 s is the Venus files' near-fixed delay (finding 7), where the paper gives\n    1 to 2 s; the outcome does not rest on it, since no Leu trial marks an onset. The criterion"
}
```

```
The file attempts/pasquereau-2013-03.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/pasquereau-2013-03.yaml",
 "old_string": "  notes: Blocked with false-positive-rate, through torque-related-fractions; the claims file's detection, whose\n    false-positive rate is 0.23 per cell-direction, gives the numbers here, which decide nothing. Torque-related",
 "new_string": "  notes: Blocked with false-positive-rate, on which the selection of responses depends; the claims file's detection,\n    whose false-positive rate is 0.23 per cell-direction, gives the numbers here, which decide nothing. Torque-related"
}
```

```
The file attempts/pasquereau-2013-03.yaml has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/pasquereau-2013-03.yaml",
 "old_string": "    Restricted to command pulses of 60 to 250 units, the range both states\n    share, the changes are +47.0% and +40.4%. Mean displacements",
 "new_string": "    Restricted to command pulses of 60 to 250 units the changes are +47.0% and +40.4%, but the pulses there\n    still differ about twofold (median 90.9 against 181.8 units), so pulse size is not excluded. At equal\n    pulses the displacements are not slower and smaller after MPTP either: at 85 to 95 units (median 90.8\n    in both states) peak velocity +16.7% (MPTP F = 4.3, p = 0.04) and amplitude +17.0% (F = 3.9, p = 0.049),\n    from faster flexion responses in 15 post-MPTP sessions; at 175 to 185 units (4 pre-MPTP sessions per\n    direction) peak velocity -0.3% (F = 0.0, p = 0.95) and amplitude -10.7% (F = 7.8, p = 0.0055). The outcome\n    is the same at equal pulses. Mean displacements"
}
```

```
<tool_use_error>String to replace not found in file.
String:     Restricted to command pulses of 60 to 250 units, the range both states
    share, the changes are +47.0% and +40.4%. Mean displacements</tool_use_error>
```

**Agent calls Read**

```json
{
 "file_path": "attempts/pasquereau-2013-03.yaml",
 "offset": 265,
 "limit": 100
}
```

```
265	- claim: kinematics-slower
266	  outcome: not_reproduced
267	  notebook: reproduce_pasquereau_2013.ipynb
268	  output: claim:kinematics-slower
269	  measured:
270	  - 28.1
271	  - 14.8
272	  notes: 'Session means (154 and 153 pre, 137 and 137 post session-directions). After MPTP peak velocity is
273	    higher, +28.1% pooled and +29.7% for flexion (MPTP F = 98.5, p = 1.5e-21), and amplitude larger, +14.8%
274	    and +11.1% (F = 25.0, p = 7.5e-07). Restricted to command pulses of 60 to 250 units, the range both states
275	    share, the changes are +47.0% and +40.4%. Mean displacements are 2.4 to 3.8 degrees, where the paper gives
276	    a mean of 10. No file repeats another''s trials, so none was left out. The angle''s scale was checked:
277	    voluntary movements to 20 degree targets measure 19.87 and 18.13 degrees from the angle, 1.000 times derived_movement_amplitude,
278	    and the peak of the file''s ElbowVelocity is 1.028 times the peak velocity from the angle (r = 1.000),
279	    so the small, faster displacements are in the data.'
280	  deviations:
281	  - Monkey V only, so the ANOVA has no animal factor (criterion).
282	  - The FIR filter has 101 taps at 1 kHz, a standard choice; onset, peak velocity and amplitude windows are
283	    the claims file's.
284	- claim: kinematic-latency-unchanged
[... 80 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat > $TMPDIR/block.yaml <<'EOF'
- claim: kinematics-slower
  outcome: not_reproduced
  notebook: reproduce_pasquereau_2013.ipynb
  output: claim:kinematics-slower
  measured:
  - 28.1
  - 14.8
  notes: 'Session means (154 and 153 pre, 137 and 137 post session-directions). After MPTP peak velocity is
    higher, +28.1% pooled and +29.7% for flexion (MPTP F = 98.5, p = 1.5e-21), and amplitude larger, +14.8%
    and +11.1% (F = 25.0, p = 7.5e-07). Restricted to command pulses of 60 to 250 units the changes are +47.0%
    and +40.4%, but the pulses there still differ about twofold (median 90.9 against 181.8 units), so pulse
    size is not excluded. At equal pulses the displacements are not slower and smaller after MPTP either: at
    85 to 95 units (median 90.8 in both states) peak velocity +16.7% (MPTP F = 4.3, p = 0.04) and amplitude
    +17.0% (F = 3.9, p = 0.049), from faster flexion responses in 15 post-MPTP sessions; at 175 to 185 units
    (4 pre-MPTP sessions per direction) peak velocity -0.3% (F = 0.0, p = 0.95) and amplitude -10.7% (F = 7.8,
    p = 0.0055). The outcome is the same at equal pulses. Mean displacements are 2.4 to 3.8 degrees, where
    the paper gives a mean of 10. No file repeats another''s trials, so none was left out. The angle''s scale
    was checked: voluntary movements to 20 degree targets measure 19.87 and 18.13 degrees from the angle, 1.000
    times derived_movement_amplitude, and the peak of the file''s ElbowVelocity is 1.028 times the peak velocity
    from the angle (r = 1.000), so the small, faster displacements are in the data.'
  deviations:
  - Monkey V only, so the ANOVA has no animal factor (criterion).
  - The FIR filter has 101 taps at 1 kHz, a standard choice; onset, peak velocity and amplitude windows are
    the claims file's.
  - Variants restricted to command pulses of 60 to 250 units and to equal pulses (85 to 95 and 175 to 185
    units) are shown, not deciding.
- claim: kinematic-latency-unchanged
  outcome: not_reproduced
  notebook: reproduce_pasquereau_2013.ipynb
  output: claim:kinematic-latency-unchanged
  notes: 'Movement onset latency is shorter after MPTP (pre 9.65 and 10.86 ms, post 3.05 and 5.99 ms for flexion
    and extension), MPTP F = 709.5 on 1 and 577 df, p = 1.5e-102; the MPTP by direction interaction is F =
    16.1 (the paper''s F > 94). The forwards-backwards filter moves onsets early after MPTP: 6.7% of post-MPTP
    onsets are at 0 ms with the velocity already above 5 deg/s (0.1% before). The variant with the velocity
    at or below threshold over the 20 ms before onset removes these but not the filter''s spread (pre 10.87
    and 9.65, post 6.13 and 3.38 ms for extension and flexion, F = 596.5; the post-MPTP flexion mean is still
    before the command leaves rest at 4 ms). Only the causal 25 Hz filter avoids both; it also gives shorter
    latencies after MPTP (pre 21.44 and 20.33, post 18.18 and 15.62 ms, F = 422.5), with a smaller difference
    (3.3 and 4.7 ms against 4.9 and 6.6 ms), so the forwards-backwards filter enlarges the difference. The unfiltered
    mean velocity at 10 and 12 ms is 1.7 and 4.0 deg/s before and 5.1 and 13.2 after MPTP. At command pulses
    of 60 to 250 units, still about twofold apart, F = 214.3 and 146.2. At equal pulses the MPTP effect is
    absent with the claims file''s onset (85 to 95 units F = 2.0, p = 0.16; 175 to 185 units F = 0.0, p = 0.98);
    the causal filter gives F = 9.3, p = 0.0027 at 85 to 95 units, with post-MPTP latencies longer by under
    1 ms, and F = 0.2, p = 0.69 at 175 to 185 units.'
  deviations:
  - The claims file's forwards-backwards filter and onset search are used; a below-threshold requirement and
    a causal 2nd-order Butterworth filter are run as variants (standard choices), since the paper says only
    that onset was detected with 'angle, velocity, and duration criteria' and a 5 deg/s threshold (Methods,
    Data analysis).
  - Variants restricted to command pulses of 60 to 250 units and to equal pulses (85 to 95 and 175 to 185
    units) are shown, not deciding.
  proposed:
    outcome: reproduced
    reason: The paper applied one torque (0.1 Nm, Methods) in both states, while in the files the post-MPTP
      pulse is about three to four times the pre-MPTP pulse (finding 3), so the comparison over all perturbations
      tests pulse size together with MPTP. At the two pulse sizes both states use, the claims file's onset
      gives no MPTP effect (85 to 95 units F = 2.0, p = 0.16, 41 and 42 pre and 15 and 43 post sessions; 175
      to 185 units F = 0.0, p = 0.98, 4 pre sessions per direction), which the criterion calls reproduced.
      The causal filter agrees at 175 to 185 units (p = 0.69) and at 85 to 95 units finds post-MPTP latencies
      longer by under 1 ms (p = 0.0027), not shorter. Notebook, second cell under kinematics-slower.
- claim: emg-m2-larger
  outcome: reproduced
  notebook: reproduce_pasquereau_2013.ipynb
  output: claim:emg-m2-larger
  notes: 'm2 medians pre and post (a.u.) triceps lateralis 5.4 and 78.9 (KS p = 3.6e-15, 35 and 32 sessions),
    triceps longus 1 4.6 and 165.6 (p = 3e-46), triceps longus 2 10.3 and 301.1 (p = 7.5e-41); the same under
    the other channel rule. The torque pulses are larger after MPTP (finding 3), which this comparison cannot
    separate from the effect of MPTP. At command pulses of 60 to 250 units (median 90.9 and 181.8, still about
    twofold apart) m2 medians are 19.6 and 76.0, 59.4 and 153.5, 76.9 and 295.1, KS p 7.5e-08 to 2.2e-15. At
    equal pulses of 85 to 95 units m2 is larger after MPTP in triceps longus 1 (60.6 and 89.3, p = 0.016) and
    2 (74.6 and 245.1, p = 0.0017), but the triceps lateralis has 2 post-MPTP sessions there (19.6 and 15.8,
    p = 0.64) and none before MPTP at 175 to 185 units, so the criterion cannot be applied at equal pulses
    and no change is proposed. The background differs between states: the median single-trial baseline SD
    of triceps longus 2 is 2.98 units before and 19.58 after MPTP, and 50% of its pre-MPTP session averages
    have a baseline SD below 1 unit (20% after); triceps lateralis has the larger SD before MPTP (16.76 against
    8.02) while its m2 is far smaller, but the pre-MPTP m2 medians (4.6 to 10.3 units) are close to the background.'
  deviations:
  - The claims file does not say whether a channel's baseline SD is that of the session-average trace or of
    the single-trial samples; both were run and give the same outcome.
  - Variants restricted to command pulses of 60 to 250 units and to equal pulses (85 to 95 and 175 to 185
    units) are shown, not deciding.
- claim: emg-duration-longer
  outcome: partially_reproduced
  notebook: reproduce_pasquereau_2013.ipynb
  output: claim:emg-duration-longer
  measured:
  - 22.2
  - 51.5
  notes: Mean duration 22.2 ms before (181 channel-sessions) and 51.5 ms after MPTP (241), KS p = 5.2e-33;
    both far outside 57 +/- 6 and 79 +/- 3 ms. 23 channel-sessions before MPTP have no response. Under the
    other channel rule 21.3 and 50.0 ms. At command pulses of 60 to 250 units, still about twofold apart, 32.0
    and 51.1 ms (KS p = 1.7e-06). At equal pulses not longer after MPTP, 85 to 95 units 32.4 and 24.1 ms (54
    and 14 channel-sessions, KS p = 0.32), 175 to 185 units 27.0 and 46.7 ms (5 and 185, KS p = 0.087).
  deviations:
  - Both readings of the channel rule were run (see emg-m2-larger); they give the same outcome.
  - Variants restricted to command pulses of 60 to 250 units and to equal pulses (85 to 95 and 175 to 185
    units) are shown, not deciding.
  proposed:
    outcome: not_reproduced
    reason: The longer post-MPTP durations over all perturbations go with a post-MPTP torque pulse three to four
      times the pre-MPTP one (finding 3), where the paper applied one torque. At the two pulse sizes both states
      use, durations are not longer after MPTP with p < 0.05 (85 to 95 units 32.4 against 24.1 ms, KS p =
      0.32; 175 to 185 units 27.0 against 46.7 ms, p = 0.087), and all means are outside tolerance, which the
      criterion calls not reproduced. Few channel-sessions enter (14 post-MPTP at 85 to 95 units, 5 pre-MPTP
      at 175 to 185). Notebook, cell tagged for the four EMG claims under EMG claims at other torque commands.
- claim: emg-onset-unchanged
  outcome: not_reproduced
  notebook: reproduce_pasquereau_2013.ipynb
  output: claim:emg-onset-unchanged
  notes: Onset of the EMG responses 44.2 ms before (median 36) and 25.0 ms after MPTP (median 25), KS p = 5.8e-22;
    under the other channel rule 41.2 and 24.2 ms, p = 7.1e-21. At command pulses of 60 to 250 units, still
    about twofold apart, 33.3 and 24.7 ms, KS p = 8.5e-07. At equal pulses, 85 to 95 units 33.0 and 32.3 ms
    (KS p = 0.40), 175 to 185 units 37.4 and 24.9 ms (KS p = 0.057, 5 pre-MPTP channel-sessions).
  deviations:
  - Both readings of the channel rule were run; they give the same outcome.
  - Variants restricted to command pulses of 60 to 250 units and to equal pulses (85 to 95 and 175 to 185
    units) are shown, not deciding.
  proposed:
    outcome: reproduced
    reason: The earlier post-MPTP onsets over all perturbations go with a post-MPTP torque pulse three to four
      times the pre-MPTP one (finding 3), where the paper applied one torque. At the two pulse sizes both states
      use, the onsets do not differ with p < 0.05 (85 to 95 units 33.0 against 32.3 ms, KS p = 0.40; 175 to
      185 units 37.4 against 24.9 ms, p = 0.057), which the criterion calls reproduced. Few channel-sessions
      enter (14 post-MPTP at 85 to 95 units, 5 pre-MPTP at 175 to 185), and at 175 to 185 units the onset is
      earlier after MPTP with p just above 0.05. Notebook, cell tagged for the four EMG claims under EMG claims
      at other torque commands.
- claim: emg-m1-weak
  outcome: partially_reproduced
  notebook: reproduce_pasquereau_2013.ipynb
  output: claim:emg-m1-weak
  notes: After MPTP m2 exceeds m1 in 237 of 241 channel-sessions (98.3%) and the median m1/m2 is 0.25; before
    MPTP the median ratio is 0.14 but m2 exceeds m1 in 151 of 204 (74.0%), just under 75%. Under the other
    channel rule 74.3% and 0.11 before, 96.3% and 0.23 after, the same outcome. Not deciding, at command pulses
    of 60 to 250 units m2 exceeds m1 in 94.9% before (59 channel-sessions, median ratio 0.10) and 97.1% after
    MPTP (0.26); at equal pulses of 85 to 95 units in 96.3% (54, 0.10) and 85.7% (14, 0.39), at 175 to 185
    units in 80.0% (5, 0.19) and 95.2% (186, 0.32). The pre-MPTP shortfall comes from sessions with small pulses.
  deviations:
  - Both readings of the channel rule were run; they give the same outcome.
  - Variants restricted to command pulses of 60 to 250 units and to equal pulses (85 to 95 and 175 to 185
    units) are shown, not deciding.
  proposed:
    outcome: reproduced
    reason: The pre-MPTP shortfall (74.0% against the 75% asked) comes from sessions whose pulse is about half
      or a quarter of the post-MPTP pulse (finding 3), where the paper applied one torque. At the two pulse sizes
      both states use, the criterion is met in both states (85 to 95 units 96.3% and 85.7%, median m1/m2 0.10
      and 0.39; 175 to 185 units 80.0% and 95.2%, 0.19 and 0.32), as it is at 60 to 250 units (94.9% and 97.1%).
      Few channel-sessions enter in one state at each size (14 post-MPTP, 5 pre-MPTP). Notebook, cell tagged
      for the four EMG claims under EMG claims at other torque commands.
EOF
python - <<'EOF'
import os
P='attempts/pasquereau-2013-03.yaml'
s=open(P).read()
a=s.index('- claim: kinematics-slower\n'); b=s.index('- claim: trial-correlations\n')
s=s[:a]+open(os.environ['TMPDIR']+'/block.yaml').read()+s[b:]
open(P,'w').write(s)
import yaml; yaml.safe_load(open(P)); print('ok')
EOF
```

```
ok
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
P='attempts/pasquereau-2013-03.yaml'
s=open(P).read()
old=s[s.index("- kind: other\n  about: data\n  severity: minor\n  notebook: reproduce_pasquereau_2013.ipynb\n  output: finding-torque-command-levels"):s.index("- kind: other\n  about: data\n  severity: none")]
new='''- kind: other
  about: data
  severity: major
  notebook: reproduce_pasquereau_2013.ipynb
  output: finding-torque-command-levels
  statement: The torque command's pulse is larger after MPTP than before (mean 174.7 against 58.4 units, about
    three times; median 181.6 against 45.7, about four times; 125 of 137 post-MPTP sessions have a median
    pulse of 120 to 250 units, 3 of 151 before), where the paper describes one 0.1 Nm pulse throughout. The
    units have no conversion to newton-metres, so whether the applied torque changed cannot be told; the ElbowTorque
    description notes the varying levels. The two states share only two pulse sizes, near 90 units (483 pre-MPTP
    and 227 post-MPTP perturbations) and near 180 units (41 and 1540), so comparisons of evoked movements and
    EMG before and after MPTP over all perturbations cannot separate the torque from the effect of MPTP.
'''
s=s.replace(old,new)
a=s.index("verifications:\n")
f7='''- kind: other
  about: data
  severity: minor
  notebook: reproduce_pasquereau_2013.ipynb
  output: finding-perturbation-timing
  statement: In the Venus files the torque onset follows center_target_appearance_time by a near-fixed delay,
    1.695 to 1.698 s in 88.4% of 5550 perturbations (1.696 s in 3010), and the median delay is in that range
    in 288 of 291 files. The paper says the torque came at an unpredictable time, 1 to 2 s from a uniform
    distribution. Either the files' centre target time is placed from the perturbation onset or the timing
    differs from the paper's; the spikes and analog series agree with the onset (data check), so the analyses
    aligned to the onset are not affected, but a delay from the centre target computed from the files would be.
'''
s=s[:a]+f7+s[a:]
open(P,'w').write(s)
import yaml; d=yaml.safe_load(open(P)); print(len(d['findings']))
EOF
```

```
7
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
P='entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb'
nb=json.load(open(P))
c=[c for c in nb['cells'] if 'finding-torque-command-levels' in c['metadata'].get('tags',[])][0]
s=''.join(c['source'])
s+='''print("\\nperturbations at the two pulse sizes both states use:")
for lo, hi in [(85, 95), (175, 185)]:
    print(f"  {lo} to {hi} units:", kin_trials[kin_trials.command.between(lo, hi)].groupby("post").size().to_dict())
'''
c['source']=s.splitlines(keepends=True)
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
EOF
tail -5 entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb | head -3; grep -n "verifier-1\|by:" attempts/pasquereau-2013-03.yaml | head
```

```
}
 },
 "nbformat": 4,
49:  blocked_by: data_missing
102:  blocked_by: methods_underspecified
123:  blocked_by: methods_underspecified
134:  blocked_by: methods_underspecified
143:  blocked_by: methods_underspecified
152:  blocked_by: methods_underspecified
161:  blocked_by: methods_underspecified
170:  blocked_by: methods_underspecified
180:  blocked_by: methods_underspecified
191:  blocked_by: methods_underspecified
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml, textwrap
P='attempts/pasquereau-2013-03.yaml'
d=yaml.safe_load(open(P))
order=[o['claim'] for o in d['outcomes']]
oc={o['claim']:o['outcome'] for o in d['outcomes']}
sel=['torque-related-fractions','prevalence-unchanged','ptn-more-responsive','one-direction-half','excitatory-majority','magnitude-unchanged','venus-response-magnitudes','latency-shorter','latency-not-training','fwhm-shorter-ptn','dsi-reduced','venus-dsi','dsi-not-baseline','session-correlations']
R={
'cell-counts':("Agree (cell 25). Cell 84 said the counts match the paper's monkey V table; they are within 3 cells of it, not equal (cell 25, 115 against 112).",
 "No change of outcome. The summary now says the counts are within 3 cells of the table (115 against 112 before MPTP)."),
'monkey-l-perturbations':("Agree (cells 20, 28). Only one of the 34 files was timed against task events (cell 20). The Leu timing argument in cell 20 relies on the near-fixed 1.7 s delay of the Venus perturbations; the Leu outcome stays blocked either way, because no Leu trial marks an onset.",
 "No change of outcome. The notes and the summary now say that only one Leu file was timed against task events, and that the 1.7 s is the Venus files' near-fixed delay (new finding 7), on which the outcome does not rest."),
'baseline-rate':("Agree (cell 31).","No change of outcome."),
'ptn-faster-than-csn':("Agree (cell 34).","No change of outcome."),
'antidromic-latency':("Agree (cell 37, CSN p = 0.019, above 0.0167).","No change of outcome."),
'false-positive-rate':("Agree. The false-positive rate is 0.230 (cell 40). The trial_sd reading, shown in cells 44 to 58, would not reproduce torque-related-fractions either (20.0% and 18.5% of M1 cells against 75 and 68% expected, cell 44).","No change of outcome."),
'torque-related-fractions':("Agree, blocked with false-positive-rate (cells 40, 44). The notes said Blocked ... through torque-related-fractions, which names the claim as its own gate.",
 "No change of outcome. The notes now say the claim is blocked with false-positive-rate, on which the selection depends."),
'velocity-matched-magnitude':("Agree. It would also stay untestable because of the data, as only 2 of 581 session-directions fall in the velocity range (cell 22). Cell 59 said no session has a mean peak velocity in the 130 to 200 deg/s range, but cell 22 shows 2 of 581 session-directions in that range and cell 57 one post-MPTP flexion response there under the claims file's detection.",
 "No change of outcome. The conclusion of the blocked claims now says 2 of 581 session-directions are in the range, with one post-MPTP flexion response under the claims file's detection and none under trial_sd."),
'trial-correlations':("Agree.","No change of outcome."),
'kinematics-slower':("Agree by the criterion (cell 61). The torque pulse is still about twice as large after MPTP inside the matched 60 to 250 range (cell 72, median 90.9 against 181.8 units for flexion), so the faster, larger displacements cannot be separated from stimulus size. Cell 64 said the command's arbitrary units do not explain the increase; within that range the pulses still differ about twofold, so stimulus size is not excluded.",
 "No change of outcome. The conclusion now says pulse size is not excluded at 60 to 250 units. A new variant compares the states at equal pulses, 85 to 95 and 175 to 185 units, the two sizes both states use (median 90.8 and about 182 in both states). There the displacements are not slower and smaller after MPTP either (85 to 95 units peak velocity +16.7%, p = 0.04, amplitude +17.0%, p = 0.049; 175 to 185 units -0.3%, p = 0.95, and -10.7%, p = 0.0055), so the outcome would be the same."),
'kinematic-latency-unchanged':("Now agrees; in round 1 it had the claim as blocked. The causal-filter variant is a valid onset measure and gives shorter post-MPTP latencies (F = 422.5, and 146.2 within the 60 to 250 range, cell 66). The deciding F = 709 still comes from a measure whose post-MPTP flexion mean (3.05 ms) falls before the command leaves rest (4 ms, cell 14). The same stimulus-size confound applies. Cell 67 and the notes said the variants that avoid the artifact give the same outcome, but the below-threshold variant still puts the post-MPTP flexion onset at 3.38 ms, before the command leaves rest; only the causal variant avoids the filter's spread. The round-1 response said the artifact shrinks the difference; cell 66 shows it enlarges it (4.9 and 6.6 ms with the claims file's onset, 3.3 and 4.7 ms causal, F 709 against 422). The p < 1e-100 is correct but the notebook printed it only as 0.0000; from F = 709 on 1 and 577 df it is about 1.5e-102.",
 "Outcome kept as verified (not_reproduced); a change to reproduced is proposed. The conclusion and notes now say only the causal filter avoids the spread and that the forwards-backwards filter enlarges the difference, correcting the round-1 response. The notebook prints p = 1.5e-102. A new variant at equal pulses (85 to 95 and 175 to 185 units) gives no MPTP effect with the claims file's onset (F = 2.0, p = 0.16 and F = 0.0, p = 0.98); the causal filter gives p = 0.0027 at 85 to 95 units with post-MPTP latencies longer by under 1 ms, and p = 0.69 at 175 to 185. Since the paper applied one torque, the proposed outcome is reproduced; see proposed on the outcome."),
'emg-m2-larger':("Agree by the criterion (cell 73), with the same stimulus-size confound. The README said the EMG results hold at matched torque commands and cell 84 that the EMG claims were repeated at matched torque commands with the same outcomes; the commands are not matched (cell 72, about 2x apart). The background differs by channel and state (cell 70); for triceps longus 2 the single-trial baseline SD is 2.98 before and 19.58 after MPTP, for triceps lateralis it is larger before (16.76 against 8.02) while its m2 is far smaller, which argues against a simple gain change, but the pre-MPTP m2 values (medians 4.6 to 10.3 units) are still near the noise.",
 "No change of outcome and none proposed. The README and summary no longer call the 60 to 250 range matched. At equal pulses of 85 to 95 units m2 is larger after MPTP in both triceps longus channels (p = 0.016 and 0.0017), but triceps lateralis has 2 post-MPTP sessions there and none before MPTP at 175 to 185 units, so the criterion cannot be applied at equal pulses. The notes now give the lateralis background and say the pre-MPTP m2 medians are close to the background."),
'emg-duration-longer':("Agree by the criterion (cell 75), with the same confound.",
 "Outcome kept as verified (partially_reproduced); a change to not_reproduced is proposed. At equal pulses durations are not longer after MPTP (85 to 95 units 32.4 against 24.1 ms, KS p = 0.32; 175 to 185 units 27.0 against 46.7 ms, p = 0.087); see proposed on the outcome."),
'emg-onset-unchanged':("Agree by the criterion (cell 77), with the same confound.",
 "Outcome kept as verified (not_reproduced); a change to reproduced is proposed. At equal pulses the onsets do not differ with p < 0.05 (85 to 95 units 33.0 against 32.3 ms, KS p = 0.40; 175 to 185 units 37.4 against 24.9 ms, p = 0.057); see proposed on the outcome."),
'emg-m1-weak':("Agree by the criterion (cell 79). Within the 60 to 250 range the criterion is met in both states, 94.9% with median ratio 0.10 before and 97.1% with 0.26 after (cell 72), so emg-m1-weak would change from partially reproduced to reproduced in that range, and the summary's same outcomes is wrong for it.",
 "Outcome kept as verified (partially_reproduced); a change to reproduced is proposed. The conclusion and notes now say the criterion is met in both states at 60 to 250 units and at equal pulses (85 to 95 units 96.3% and 85.7%; 175 to 185 units 80.0% and 95.2%); see proposed on the outcome."),
}
for c in sel:
    if c not in R:
        R[c]=("Agree, blocked with false-positive-rate (cells 40, 44 to 58).","No change of outcome.")
res=[]
for c in order:
    r,resp=R[c]
    res.append({'claim':c,'agrees':True,'outcome':oc[c],'reason':r,'response':resp})
v={'date':'2026-11-26','kind':'agent','by':d['verifications'][0]['by'],
 'reviewed':'Round 2: the full executed notebook after the round-1 revision (cell numbers in the reasons count from 0 in that notebook; this revision inserted cells, so they now point one to three cells earlier than the cells they name after cell 22), the helper module, the claims file and the attempt record, with the paper under paper/.',
 'results':res,
 'findings':[{'finding':3,'agrees':False,'severity':'major','reason':"Rated minor; I would rate it major. It changes the kinematic and EMG comparisons, and it cannot be worked around, since the two states barely overlap in pulse size. It is not critical, because it is evident from the command values and from the ElbowTorque description.",
   'response':"Severity changed to major. The states do share two pulse sizes, near 90 units (483 pre-MPTP and 227 post-MPTP perturbations) and near 180 units (41 and 1540), now printed in the finding's cell; the kinematic and EMG claims are compared there as variants, and four outcome changes are proposed from them."}]}
d['verifications'][0]['reviewed']+=" Cell numbers in the round-1 reasons are those of the round-1 notebook; the cells have moved since, and each claim's cells carry the tag claim:<id>."
# dump only the new verification block and append; patch round-1 reviewed via text
s=open(P).read()
old_rev=yaml.safe_load(s)['verifications'][0]['reviewed']
txt=yaml.safe_dump([v],sort_keys=False,width=110,allow_unicode=True)
txt=textwrap.indent(txt,'')
open(P,'w').write(s.rstrip('\n')+'\n'+txt)
d2=yaml.safe_load(open(P)); print(len(d2['verifications']))
EOF
tail -30 attempts/pasquereau-2013-03.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import yaml
P='attempts/pasquereau-2013-03.yaml'
s=open(P).read()
a="did not download data or re-run\n    the notebook.'"
assert s.count(a)==1
s=s.replace(a,"did not download data or re-run\n    the notebook. Cell numbers in the round-1 reasons are those of the round-1 notebook; the cells have moved\n    since, and each claim''s cells carry the tag claim:<id>.'")
d=yaml.safe_load(s)
r=d['verifications'][1]['reviewed']
print(r)
open(P,'w').write(s)
EOF
grep -n "Round 2" -A4 attempts/pasquereau-2013-03.yaml; grep -n "summary's same outcomes" -B1 -A1 attempts/pasquereau-2013-03.yaml
```

```
Round 2: the full executed notebook after the round-1 revision (cell numbers in the reasons count from 0 in that notebook; this revision inserted cells, so they now point one to three cells earlier than the cells they name after cell 22), the helper module, the claims file and the attempt record, with the paper under paper/.
717:  reviewed: 'Round 2: the full executed notebook after the round-1 revision (cell numbers in the reasons count from
718-    0 in that notebook; this revision inserted cells, so they now point one to three cells earlier than the cells
719-    they name after cell 22), the helper module, the claims file and the attempt record, with the paper under paper/.'
720-  results:
721-  - claim: cell-counts
903-      with median ratio 0.10 before and 97.1% with 0.26 after (cell 72), so emg-m1-weak would change from partially
904:      reproduced to reproduced in that range, and the summary's same outcomes is wrong for it.
905-    response: Outcome kept as verified (partially_reproduced); a change to reproduced is proposed. The conclusion
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
P='attempts/pasquereau-2013-03.yaml'
s=open(P).read()
s=s.replace("""(cell numbers in the reasons count from
    0 in that notebook; this revision inserted cells, so they now point one to three cells earlier than the cells
    they name after cell 22)""","""(cell numbers in the reasons count from
    0 in that notebook; this revision inserted three cells, so from cell 23 on the cells named are one to three
    positions later now)""")
s=s.replace("""reproduced to reproduced in that range, and the summary's same outcomes is wrong for it.""","""reproduced to reproduced in that range, so the summary's statement that the outcomes are the same is wrong
      for it.""")
open(P,'w').write(s)
import yaml; yaml.safe_load(open(P)); print("ok")
EOF
```

```
ok
```

**Agent**

Now the README.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/pasquereau-2013/README.md",
 "old_string": "of responses are blocked; their results are shown in the notebook. The torque command's pulses are\nabout three times larger after MPTP than before, and the evoked displacements are faster and\nlarger after MPTP, the reverse of the paper's; the angle's scale agrees with the task's 20 degree\ntargets and with the files' own velocity series, so this is in the data. The shorter latency of\nthe evoked movement after MPTP holds with a causal filter as well as with the claims file's, and\nthe EMG results hold at matched torque commands. The attempt record, with the reasons and the\ndifferences from the paper's method, is",
 "new_string": "of responses are blocked; their results are shown in the notebook. The torque command's pulses are\nlarger after MPTP than before (mean 174.7 against 58.4 units, about three times; median 181.6\nagainst 45.7, about four times), and the evoked displacements are faster and larger after MPTP,\nthe reverse of the paper's; the angle's scale agrees with the task's 20 degree targets and with\nthe files' own velocity series, so this is in the data. Over all perturbations the evoked movement\nstarts earlier after MPTP with a causal filter as well as with the claims file's. The two states\nshare two pulse sizes, near 90 and near 180 units. Compared there, the latency of the evoked\nmovement and the onset of the EMG response do not change after MPTP, the EMG response is not\nlonger, and m1 is much smaller than m2 in both states. The record keeps the verified outcomes and\nproposes these four changes for a further round of verification. The attempt record, with the\nreasons and the differences from the paper's method, is"
}
```

```
The file entries/pasquereau-2013/README.md has been updated successfully.
```

**Agent calls Bash**

```bash
cd  grep -n -i "about three times\|matched" entries/pasquereau-2013/README.md entries/pasquereau-2013/pasq.py attempts/pasquereau-2013-03.yaml | grep -v "verifications" | head -20; python -c "
import json;nb=json.load(open('entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb'))
for i,c in enumerate(nb['cells']):
  s=''.join(c['source'])
  for k in ['three times','matched','—',' rather']:
    if k in s: print(i,k,repr(s[max(0,s.find(k)-80):s.find(k)+60]))"
```

```
entries/pasquereau-2013/README.md:31:larger after MPTP than before (mean 174.7 against 58.4 units, about three times; median 181.6
attempts/pasquereau-2013-03.yaml:245:- claim: velocity-matched-magnitude
attempts/pasquereau-2013-03.yaml:249:  output: claim:velocity-matched-magnitude
attempts/pasquereau-2013-03.yaml:439:    fall in the 130 to 200 deg/s range the paper uses for its velocity-matched sessions. After MPTP the displacements
attempts/pasquereau-2013-03.yaml:650:      Both rise after MPTP under both readings. The matched-command variant (cell 50) also rises (+47%, +40%).'
attempts/pasquereau-2013-03.yaml:663:      latencies after MPTP (F = 596.5 and 422.5), also at matched commands (F = 214.3 and 146.2), and the unfiltered
attempts/pasquereau-2013-03.yaml:680:    response: No change of outcome. At matched commands 32.0 and 51.1 ms, the same outcome.
attempts/pasquereau-2013-03.yaml:685:    response: No change of outcome. At matched commands 33.3 and 24.7 ms, KS p = 8.5e-07.
attempts/pasquereau-2013-03.yaml:691:    response: No change of outcome. At matched commands (not deciding) 94.9% before; the notes say so.
attempts/pasquereau-2013-03.yaml:692:  - claim: velocity-matched-magnitude
attempts/pasquereau-2013-03.yaml:826:  - claim: velocity-matched-magnitude
attempts/pasquereau-2013-03.yaml:844:      matched 60 to 250 range (cell 72, median 90.9 against 181.8 units for flexion), so the faster, larger displacements
attempts/pasquereau-2013-03.yaml:875:      hold at matched torque commands and cell 84 that the EMG claims were repeated at matched torque commands with
attempts/pasquereau-2013-03.yaml:876:      the same outcomes; the commands are not matched (cell 72, about 2x apart). The background differs by channel
attempts/pasquereau-2013-03.yaml:881:      matched. At equal pulses of 85 to 95 units m2 is larger after MPTP in both triceps longus channels (p = 0.016
0 matched '-training, fwhm-shorter-ptn, dsi-reduced, venus-dsi, dsi-not-baseline, velocity-matc
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; python tools/entry.py all entries/pasquereau-2013 2>&1 | tail -4; date -u
```

```
Thu Nov 26 19:29:03 UTC 2026


0 error(s)
FAIL  reproduce_pasquereau_2013.ipynb  (833 s)
Thu Nov 26 19:43:09 UTC 2026
```

**Agent calls Bash**

```bash
cd  cat executed/pasquereau-2013/result.json | head -20; python - <<'EOF'
import json
nb=json.load(open('executed/pasquereau-2013/reproduce_pasquereau_2013.ipynb'))
for i,c in enumerate(nb['cells']):
    for o in c.get('outputs',[]):
        if o.get('output_type')=='error': print(i,o['ename'],o['evalue'][:500]); print(''.join(c['source'])[-400:])
EOF
```

```
{
 "entry": "pasquereau-2013",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_pasquereau_2013.ipynb",
   "ok": false,
   "seconds": 833,
   "error": "python3.13/site-packages/nbconvert/exporters/exporter.py\", line 353, in _preprocess\n    nbc, resc = preprocessor(nbc, resc)\n                ~~~~~~~~~~~~^^^^^^^^^^^\n  File \"executed/pasquereau-2013/.venv/lib/python3.13/site-packages/nbconvert/preprocessors/base.py\", line 48, in __call__\n    return self.preprocess(nb, resources)\n           ~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^\n  File \"executed/pasquereau-2013/.venv/lib/python3.13/site-packages/nbconvert/preprocessors/execute.py\", line 103, in preprocess\n    self.preprocess_cell(cell, resources, index)\n    ~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^\n  File \"executed/pasquereau-2013/.venv/lib/python3.13/site-packages/nbconvert/preprocessors/execute.py\", line 124, in preprocess_cell\n    cell = self.execute_cell(cell, index, store_history=True)\n  File \"executed/pasquereau-2013/.venv/lib/python3.13/site-packages/jupyter_core/utils/__init__.py\", line 165, in wrapped\n    return loop.run_until_complete(inner)\n           ~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^\n  File \"/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/asyncio/base_events.py\", line 726, in run_until_complete\n    return future.result()\n           ~~~~~~~~~~~~~^^\n  File \"executed/pasquereau-2013/.venv/lib/python3.13/site-packages/nbclient/client.py\", line 1062, in async_execute_cell\n    await self._check_raise_for_error(cell, cell_index, exec_reply)\n  File \"executed/pasquereau-2013/.venv/lib/python3.13/site-packages/nbclient/client.py\", line 918, in _check_raise_for_error\n    raise CellExecutionError.from_cell_and_msg(cell, exec_reply_content)\nnbclient.exceptions.CellExecutionError: An error occurred while executing the following cell:\n------------------\n# The torque command's pulse is larger after MPTP (means about three times, medians about four); the paper gives one 0.1 
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json, ast
P='entries/pasquereau-2013/reproduce_pasquereau_2013.ipynb'
nb=json.load(open(P))
for c in nb['cells']:
    s=''.join(c['source'])
    if ')))print(' in s:
        s=s.replace(')))print(', ')))\nprint('); c['source']=s.splitlines(keepends=True)
for i,c in enumerate(nb['cells']):
    if c['cell_type']=='code': ast.parse(''.join(c['source']))
json.dump(nb,open(P,'w'),indent=1,ensure_ascii=False); open(P,'a').write('\n')
print('ok')
EOF
date -u; python tools/entry.py all entries/pasquereau-2013 2>&1 | tail -3; date -u
```

```
ok
Thu Nov 26 19:43:16 UTC 2026
Installed kernelspec registry-pasquereau-2013 in executed/pasquereau-2013/.venv/share/jupyter/kernels/registry-pasquereau-2013
0 error(s)
pass  reproduce_pasquereau_2013.ipynb  (838 s)
Thu Nov 26 19:57:27 UTC 2026
```

**Agent**

Run passed. Now I confirm the outputs match the text and run the checks.

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('executed/pasquereau-2013/reproduce_pasquereau_2013.ipynb'))
def out(c):
    s=''
    for o in c.get('outputs',[]):
        if 'text' in o: s+=''.join(o['text'])
        elif 'data' in o and 'text/plain' in o['data']: s+=''.join(o['data']['text/plain'])
    return s
for i,c in enumerate(nb['cells']):
    t=c['metadata'].get('tags',[])
    if t and t[0] in ('finding-torque-command-levels','finding-perturbation-timing','claim:emg-m2-larger') or i in (65,68,75):
        print('==',i,t); print(out(c)[-1400:])
EOF
python tools/entry.py check entries/pasquereau-2013 2>&1 | tail -5
```

```
== 21 ['finding-torque-command-levels']
        count   mean   std   min    25%    50%    75%    max
post                                                        
False  1947.0   58.4  28.1  -0.7   45.3   45.7   90.3  182.7
True   3603.0  174.7  47.6  26.0  155.3  181.6  184.5  343.5

sessions by median pulse size (a.u.), pre and post:
command  (30, 60]  (60, 120]  (120, 250]
post                                    
False         105         43           3
True            0         12         125

perturbations at the two pulse sizes both states use:
  85 to 95 units: {False: 483, True: 227}
  175 to 185 units: {False: 41, True: 1540}

== 23 ['finding-perturbation-timing']
perturbations: 5550 ; delay from centre target appearance to torque onset (s): min 1.257, max 11.841
fraction 1.695 to 1.698 s: 0.884 (pre 0.892, post 0.879); fraction 1 to 2 s: 0.972
most common delays (s): {1.696: 3010, 1.697: 1859, 1.698: 83, 1.7: 22, 1.699: 22}
[... 77 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls tools; grep -rn "em dash\|—" attempts/pasquereau-2013-03.yaml entries/pasquereau-2013/README.md | head -3; grep -c " rather" attempts/pasquereau-2013-03.yaml entries/pasquereau-2013/README.md
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
author_notes.py
authors.py
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_osf_targets.py
build_reuse_targets.py
build_site.py
build_sparc_targets.py
build_targets.py
build_zenodo_targets.py
changed_entries.py
claims_check.py
colab.py
[... 29 more lines not kept]
```

**Agent**

I addressed every point in the round-2 report. The entry re-ran cleanly (`tools/entry.py all` passed in 838 s, check reports 0 errors), and every number in the notes and conclusions matches the new outputs.

**Outcomes**
No outcome changed. The verifier agreed with all 28, and the record keeps them. I did add four proposed changes for a third round to review.

The verifier said the two MPTP states "barely overlap" in torque pulse size. They do share two sizes, though: near 90 units (483 perturbations before MPTP, 227 after) and near 180 units (41 before, 1540 after). Comparing the states at these equal pulses changes four results by the claims' criteria:
- **kinematic-latency-unchanged**: proposed reproduced. With the claims file's onset there is no MPTP effect (p = 0.16 near 90 units, p = 0.98 near 180).
- **emg-onset-unchanged**: proposed reproduced (p = 0.40 and 0.057).
- **emg-duration-longer**: proposed not reproduced. Durations are not longer after MPTP (p = 0.32 and 0.087).
- **emg-m1-weak**: proposed reproduced. The criterion is met in both states at both sizes.

Each proposal states its weakness: few post-MPTP sessions near 90 units (14 EMG channel-sessions) and few pre-MPTP sessions near 180 (5). The causal-filter version of the latency also disagrees near 90 units: it finds post-MPTP latencies about 1 ms longer (p = 0.0027).

I proposed nothing for two claims:
- **kinematics-slower**: at equal pulses the movements are still not slower and smaller after MPTP, so the outcome would not change.
- **emg-m2-larger**: the criterion needs the triceps lateralis, which has only 2 post-MPTP sessions near 90 units and no pre-MPTP session near 180, so it cannot be applied.

**Corrected or added**
- **Notebook text**: I fixed every sentence the verifier said the outputs did not support:
  - The velocity range now holds 2 of 581 session-directions with one response.
  - The 60 to 250 unit range is no longer called matched; the pulses there still differ about twofold.
  - Only the causal filter avoids the onset artifact.
  - The forwards-backwards filter enlarges the latency difference. This corrects my round-1 response, which said it shrank it.
  - The torque pulse ratio is about three times for the means and four times for the medians.
  - The cell counts are within 3 cells of the paper's table, not equal to it.
  - Only one Leu file was timed against task events.
  - The displacements are 2.4 to 3.8 degrees.
- **Exact p**: the latency ANOVA's p is now printed as 1.5e-102, not 0.0000.
- **torque-related-fractions notes**: they no longer name the claim as its own gate.
- **EMG background**: the notes now give the triceps lateralis background and say the pre-MPTP m2 values are close to the noise.
- **Finding 3** (torque pulse sizes): raised from minor to major, as the verifier asked. Its cell now prints the perturbation counts at the two shared pulse sizes.
- **New finding 7** (minor, cell `finding-perturbation-timing`): 88% of Venus perturbations come 1.695 to 1.698 s after the centre target appears, where the paper describes a delay drawn uniformly from 1 to 2 s.
- **README and summary**: rewritten to match the above.
- **Verification record**: round 2 is recorded with the verifier's reasons and my responses, plus its view on finding 3. A note explains that the round-1 cell numbers point to the old notebook.

**Not done**
- No question was added to `questions/pasquereau-2013.yaml`: this round reported no new place where the claims file misreads the paper.
- The round-1 responses that say "matched commands" and "the artifact shrinks the difference" are left as written. The round-2 responses correct them.
- I did not time the other 33 Leu files against task events. The text now says only one file was checked, and the Leu outcome stays blocked either way, because no Leu trial marks a perturbation onset.

Nothing was committed or pushed.

## End of run

51 turns, 63 minutes, $2.92 at API prices, result: success.
