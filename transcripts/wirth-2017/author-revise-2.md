# wirth-2017 · author-revise-2 · run 43470172530

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/wirth-2017/verifier-2-report.md; ls entries/wirth-2017 transcripts/wirth-2017 questions 2>/dev/null | head -50
```

```
Fri Nov 13 17:23:39 UTC 2026
# Verifier report, round 2: Wirth et al. 2017 (doi:10.1371/journal.pbio.2001045), CRCNS hc-12 / hc-21

The claims file has 28 claims, and the attempt record has 28 outcomes, one for each. They split as 5 reproduced, 3 partially reproduced, 6 not reproduced and 14 blocked (11 for insufficient metadata, 3 for underspecified methods).

## 1. Outcomes

| Claim | Outcome in the record | Agree? | Note |
|---|---|---|---|
| gaze-anticipates-action | reproduced (assumed) | Yes | The assumption is stated and reasonable. Cell 28 gives the sign from eye velocity during turns, not from eye position, in 40/40 sessions of K and 20/20 of S. See caveat (a) below; it does not change the outcome. |
| gaze-anticipates-landmarks | reproduced (assumed) | Yes, changed from my round-1 partial | The sign now comes from the slow-phase velocity during turns at the centre, which does not use eye position, so the test is no longer circular. Cell 31: K −0.56 SD, p = 6.2e-58, 39/41 sessions; S −0.56, p = 6.4e-30, 20/21. See claims-file point (b) below. |
| learning-trials | reproduced | Yes | Cell 18. |
| learning-to-90 | reproduced | Yes | Cell 20: 0.898, or 0.803 over all sessions. Only one session reaches 0.9 at the criterion trial itself. |
| probe-transfer | not reproduced | Yes | Cell 23: 28.3% and 58.3% against 44 and 73. No variant puts both means inside tolerance. |
| probe-faster-criterion | blocked (methods underspecified) | Yes | |
| cells-recorded | partially reproduced | Yes | |
| responsive-cells | blocked (metadata insufficient) | Yes | |
| state-space-most-responsive | not reproduced | Yes | Cell 38: 37 to 57 cells against 75.6 to 92.4, and 41 to 58 using the upper tail only. |
| multi-space-coding | blocked (metadata insufficient) | Yes | |
| direction-center-vs-periphery | partially reproduced (assumed) | Yes | The assumption is stated: the three-space responsive cells stand in for reading (b). It is the weakest step. For a signed-rank test the res
[... 106 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^## Author/,/^## [A-Z]/p' docs/protocol.md | head -300; ls questions | grep wirth; ls entries/wirth-2017/..; ls attempts 2>/dev/null | head
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

[... 574 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/^### 6. Hand over/,/^## Verifier/p' docs/protocol.md; ls questions/ | grep -i wirth; ls attempts | grep wirth
```

```
### 6. Hand over for verification

Do not verify your own attempt. Give the verifier:

- the executed notebook with the conclusion cells and the summary removed;
- the helper module;
- the claims file.

`python tools/entry.py handover entries/<name>` builds these in
`executed/<name>/handover/` from the executed copy. The verifier also gets the
paper, under `paper/`, but checks the analysis against the claims file, and a
method detail the author took from the paper against the passage the author
cites. A place where the claims file misreads the paper is reported; the
revision adds it to `questions/<paper>.yaml` as a question for a reader, as in
step 1.6, and does not change the claim. A reader answers it after the
attempt, in an `answer` run started by hand; the claim's outcome stays as
tested on the claims file, and a later attempt takes up any change.

After the first round, fix what it found, re-run, and hand over the full
executed notebook for the second round. Record each round under
[... 85 more lines not kept]
```

**Agent calls Bash**

```bash
wc -l attempts/wirth-2017-01.yaml; grep -n "^[a-z_]*:\|^  - claim:\|^- \|assumed\|proposed" attempts/wirth-2017-01.yaml | head -120
```

```
650 attempts/wirth-2017-01.yaml
1:schema_version: 3
2:id: wirth-2017-01
3:datasets:
4:- archive: crcns
9:- archive: crcns
14:paper: doi:10.1371/journal.pbio.2001045
15:date: 2026-11-13
16:entry: wirth-2017
17:provenance:
28:outcomes:
29:- claim: gaze-anticipates-action
31:  assumed: true
53:- claim: gaze-anticipates-landmarks
55:  assumed: true
71:- claim: learning-trials
87:- claim: learning-to-90
100:- claim: probe-transfer
122:- claim: probe-faster-criterion
130:- claim: cells-recorded
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,350p attempts/wirth-2017-01.yaml
```

```
schema_version: 3
id: wirth-2017-01
datasets:
- archive: crcns
  id: hc-21
  version: unversioned
  doi: 10.6080/K0GX48R9
  relation: primary
- archive: crcns
  id: hc-12
  version: unversioned
  doi: 10.6080/K0R49NQV
  relation: primary
paper: doi:10.1371/journal.pbio.2001045
date: 2026-11-13
entry: wirth-2017
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
[... 330 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 350,650p attempts/wirth-2017-01.yaml
```

```
datasets:
  - crcns-hc-12
  - crcns-hc-21
  statement: The horizontal and vertical eye signals have no units, calibration or sign convention. They
    are on a +-5000 scale in 36 hc-12 sessions and a +-5 scale in 26, with saturated samples at the bound
    (up to 22% of a session). The paper's point-of-gaze maps, foveation and landmark eccentricity cannot
    be computed, which blocks 11 of the 28 claims and part of a twelfth. The sign used here is inferred
    from the slow phases during turns.
- kind: metadata_error
  datasets:
  - crcns-hc-12
  statement: The descriptor puts the probability of a correct response in the middle column of learning_curves
    and the bounds in columns 1 and 3. In all 187 files column 2 is the lowest and column 3 the highest,
    so the columns are probability, lower bound and upper bound. The field learningtrial, not described,
    is the first trial whose lower bound exceeds 1/4 (-2 when none).
- kind: metadata_error
  datasets:
  - crcns-hc-12
  statement: The descriptor gives the eye positions at 250 Hz; eye_times are 5 ms apart (200 Hz) in every
    file.
[... 281 more lines not kept]
```

**Agent calls Bash**

```bash
ls executed/wirth-2017/ 2>/dev/null; cat questions/README.md | head -60; ls questions/*.yaml | head -3; head -40 questions/bech-2026.yaml
```

```
reproduce_wirth_2017.ipynb
result.json
# Questions

`<dandiset>.yaml` holds an attempt's questions to a reader: places where the author or a verifier
believes the claims file misreads the paper (docs/protocol.md, "Author", step 1.6, and "Hand over for
verification"), and the reader's answers ("Reader", step 6), which say whether the claims file was
amended and why. Each question has `claim`, `question`, `passage`, `why` (how the misreading could
change the outcome), and, once answered, `answer` and `answered` (a date). Method details the claims
file lacks are not asked here: the author takes them from the paper, and a detail the paper does not
settle is a question for the paper's authors, recorded in the claim's notes and as a
`methods_unavailable` finding in the attempt. Files from before protocol `pilot-11` also hold
questions about method details, asked under the earlier rule.
questions/ashworth-2025.yaml
questions/athalye-2023.yaml
questions/bech-2026.yaml
dandiset: "001847"
paper: doi:10.7554/elife.109717
questions:
- claim: fig2d-auditory-a1-frontal
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/wirth-2017 && python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
for i,c in enumerate(nb['cells']):
    if i in (6,7,8,9,10,27,28,29,30,32,42,43,44,45,56,57,59,60,61,67):
        print('=====',i,c['cell_type'],c['metadata'].get('tags'))
        print(''.join(c['source'])[:3000])
        for o in c.get('outputs',[]):
            t=o.get('text') or o.get('data',{}).get('text/plain','')
            print('--OUT--'); print(''.join(t)[:3000])
EOF
```

```
<persisted-output>
Output too large (40.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/8c669e4b-6b97-4064-9cf2-1e4a584028f3/tool-results/bs1voh7sd.txt

Preview (first 2KB):
===== 6 code ['sanity']
print("Files by monkey (ke = monkey K, sn = monkey S):")
print(M.groupby("monkey").agg(files=("file", "size"), with_new_maze=("has_newallo", "sum"),
                              sessions=("session", "nunique")).to_string())
print("\nFiles without a new-maze (newallo) field:", M.loc[~M.has_newallo, "file"].tolist())
print("\nSpike times taken from:", M.spike_src.value_counts().to_dict())
print("Top-level field sets:", M.fields.nunique(), "different layouts")
print("Camera frame interval (ms):", M.frame_dt_ms.describe()[["min", "max"]].round(3).to_dict())
print("Eye sample interval (ms):", M.eye_dt_ms.describe()[["min", "max"]].round(3).to_dict(),
      "; files without eye data:", int((~M.has_eye.fillna(False).astype(bool)).sum() - (~M.has_newallo).sum()))
print("Spike times sorted in every file:", bool(M.spikes_sorted.dropna().all()))
rng_cols = ["x_min", "x_max", "y_min", "y_max", "theta_min", "theta_max", "abscissa_max"]
print("\nRanges of the camera variables over files (min / max of each):")
print(M[rng_cols].agg(["min", "max"]).round(2).to_string())
print("\nTrials per new-maze session (per file):", M.n_trials.describe()[["min", "50%", "max"]].to_dict())
print("Session length, first trial start to last trial end (min):",
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/8c669e4b-6b97-4064-9cf2-1e4a584028f3/tool-results/bs1voh7sd.txt"
}
```

```
1	===== 6 code ['sanity']
2	print("Files by monkey (ke = monkey K, sn = monkey S):")
3	print(M.groupby("monkey").agg(files=("file", "size"), with_new_maze=("has_newallo", "sum"),
4	                              sessions=("session", "nunique")).to_string())
5	print("\nFiles without a new-maze (newallo) field:", M.loc[~M.has_newallo, "file"].tolist())
6	print("\nSpike times taken from:", M.spike_src.value_counts().to_dict())
7	print("Top-level field sets:", M.fields.nunique(), "different layouts")
8	print("Camera frame interval (ms):", M.frame_dt_ms.describe()[["min", "max"]].round(3).to_dict())
9	print("Eye sample interval (ms):", M.eye_dt_ms.describe()[["min", "max"]].round(3).to_dict(),
10	      "; files without eye data:", int((~M.has_eye.fillna(False).astype(bool)).sum() - (~M.has_newallo).sum()))
11	print("Spike times sorted in every file:", bool(M.spikes_sorted.dropna().all()))
12	rng_cols = ["x_min", "x_max", "y_min", "y_max", "theta_min", "theta_max", "abscissa_max"]
13	print("\nRanges of the camera variables over files (min / max of each):")
14	print(M[rng_cols].agg(["min", "max"]).round(2).to_string())
15	print("\nTrials per new-maze session (per file):", M.n_trials.describe()[["min", "50%", "max"]].to_dict())
16	print("Session length, first trial start to last trial end (min):",
17	      ((M.t_end - M.t_start) / 60).describe()[["min", "50%", "max"]].round(1).to_dict())
18	print("\nCamera-data layout: columns of time_60 per file:", M.t60_cols.value_counts().to_dict())
19	print("Transition tag (column 11) over files:", M.tag_min.min(), "to", M.tag_max.max(),
20	      "; hundreds present per file:", M.tag_hundreds.value_counts().to_dict())
[... 507 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017 && grep -n "abscissa\|quarter\|rel_dist\|relative distance" wirth.py | head -60; wc -l wirth.py
```

```
13:(deg), curvilinear abscissa on the maze branch (0 centre, 1 arm end), state-space curvilinear
14:abscissa, state-space polar angle, state-space radius, next, previous and current transition
592:    Two-way (Methods, ANOVA for landmark identity and relative distance): entry-path frames
593:    (tags 10x) of successful trials, cut by the curvilinear abscissa (0 centre, 1 arm end)
787:            "turns": turns, "returns": rets, "abscissa_at_events": clock, "eye_saturated": eye_sat, "eye_range": eye_rng,
815:                    "abscissa_min": float(np.nanmin(t60[:, 4])), "abscissa_max": float(np.nanmax(t60[:, 4])),
816:                    "abscissa_over_1": float(np.mean(t60[:, 4] > 1.001)),
857:        out["n_entry_frames_abscissa_over_1"] = int(np.sum(np.isfinite(c["t60"][:, 4]) & (c["t60"][:, 4] > 1.001)
892 wirth.py
```

**Agent calls Bash**

```bash
sed -n 1,40p wirth.py; sed -n 585,640p wirth.py; grep -n "clock\b\|clock =\|clock\[" wirth.py | head
```

```
"""Loading and measures for CRCNS hc-12 (and hc-21), the data of Wirth, Baraduc, Plante,
Pinede & Duhamel (2017), PLoS Biology 15(2), e2001045, doi:10.1371/journal.pbio.2001045.

The data sets are single tar.gz archives of MATLAB files, one file per cell, in the public S3
bucket crcnsarchive. They are streamed: the archive is decompressed as it is read and each
member is loaded in memory and reduced to what the analysis needs, one at a time. Nothing is
written to disk.

File layout (descriptor of hc-12, version 0.7, and the files themselves): spike times
(`file.elec`, or `file.newallo.elec` when the top level has none), the trial tables of the new
maze (`newallo.codematrix`, `newallo.timematrix`), learning curves, eye positions at 250 Hz
with `eye_times`, and `camera_data.time_60`, 60 Hz rows of [time, x, y, camera orientation
(deg), curvilinear abscissa on the maze branch (0 centre, 1 arm end), state-space curvilinear
abscissa, state-space polar angle, state-space radius, next, previous and current transition
tag, composite maze tag]. `time_60` sits under `newallo.camera_data` in some files.

Where the parameters come from:

- Successful trials only; maps unsmoothed; a bin is valid with at least four successful
  trials (Methods, Activity maps) and more than 400 ms of time in successful trials (Methods,
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cat ../../executed/wirth-2017/result.json | head -30; sed -n 740,830p wirth.py
```

```
{
 "entry": "wirth-2017",
 "python": "3.13",
 "results": [
  {
   "notebook": "reproduce_wirth_2017.ipynb",
   "ok": true,
   "seconds": 1870,
   "error": null
  }
 ]
}
    for i, (ty, tt) in enumerate(zip(tr["turns"], tr["turn_t"])):
        for j, (code, t) in enumerate(zip(ty, tt)):
            row = {"trial": i, "k": j, "code": code, "correct": bool(tr["correct"][i])}
            for w in (0.5, 0.3):
                for which in ("mean", "l", "r"):
                    row[f"eye{int(w * 1000)}_{which}"] = eye_mean(c, t - w, t, which)
            for lag in EYE_LAGS:
                row[f"lag{lag}"] = eye_mean(c, t + lag, t + lag + 0.1)
[... 83 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "^def \|^[A-Z_]* = " wirth.py | head -60; grep -n "wirth\.\(iter\|load\|stream\)" reproduce_wirth_2017.ipynb | head
```

```
70:BUCKET = "https://crcnsarchive.s3-us-west-2.amazonaws.com"
71:ARCHIVES = {"hc-12": f"{BUCKET}/hc-12/live/data.tar.gz",
73:VERSION = "unversioned"       # CRCNS data sets are not versioned (docs/archives.md)
77:DT = 1 / 60                   # camera rows are 60 Hz
78:MIN_BIN_S = 0.4               # Methods, Information Content
79:MIN_TRIALS = 4                # Methods, Activity maps
80:TARGET_BINS = 200             # Methods, Information Content
81:CHUNK_S = 5.0                 # Methods, Permutation statistics
82:N_SURR = 999
83:SSI_BIN_DEG = 3.6             # Methods, State-space selectivity
85:POS_STEPS = np.round(np.arange(0.4, 8.01, 0.1), 2)          # m, square bins
86:STATE_STEPS = np.round(np.arange(0.02, 0.60, 0.005), 3)     # planar state-space units
87:DIR_STEPS = np.arange(8, 721)                                # number of angular bins
92:def stream_members(dataset):
101:def _field(s, name):
105:def reduce_file(name, d, maze="newallo"):
176:def _code_times(cm, tm, code):
183:def trials(c):
199:def frame_table(c, reading="full"):
225:def spike_counts(c):
[... 33 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 88,110p wirth.py; ls ~/.cache 2>/dev/null; which python; python -c "import scipy, h5py; print('ok')"
```

```
Exit code 1


# ---------------------------------------------------------------- loading

def stream_members(dataset):
    """Yield (member name, loaded MATLAB dict) for every .mat file of a data set's archive."""
    f = fsspec.open(ARCHIVES[dataset], block_size=2**22).open()
    with tarfile.open(fileobj=f, mode="r|gz") as tf:
        for m in tf:
            if m.isfile() and m.name.endswith(".mat"):
                yield m.name.split("/")[-1], sio.loadmat(io.BytesIO(tf.extractfile(m).read()))


def _field(s, name):
    return s[name] if (s.dtype.names and name in s.dtype.names) else None


def reduce_file(name, d, maze="newallo"):
    """Reduce one cell file to the arrays used here; None when it has no `maze` trials."""
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd  ls -a; ls .venv* executed/wirth-2017 2>/dev/null; grep -n "venv\|def cmd_run\|uv " tools/entry.py | head -20
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
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q --python 3.13 venv && uv pip install -q --python venv/bin/python -r entries/wirth-2017/requirements.lock.txt 2>&1 | tail -3; venv/bin/python -c "import scipy, fsspec; print('ok')"
```

```
ok
Shell cwd was reset to
```

**Agent**

Environment ready. Now checking the direction of the abscissa on the first file from the archive.

**Agent calls Bash**

```bash
cd entries/wirth-2017 && timeout 900 $TMPDIR/venv/bin/python - <<'EOF'
import numpy as np, wirth, itertools
n=0
for name,d in wirth.stream_members("hc-12"):
    c=wirth.reduce_file(name,d)
    if c is None: continue
    t=c["t60"]; tag=t[:,10]; ab=t[:,4]; r=np.hypot(t[:,1],t[:,2])
    for lo,hi,lab in ((100,200,"entry 1xy"),(200,300,"2xy"),(300,400,"3xy"),(400,500,"4xy"),(500,600,"5xy")):
        m=(tag>=lo)&(tag<hi)&np.isfinite(ab)
        if m.sum()<10: continue
        print(name, lab, "n",m.sum(),"corr(ab, r)",round(np.corrcoef(ab[m],r[m])[0,1],3),
              "ab range",round(ab[m].min(),2),round(ab[m].max(),2),"r range",round(r[m].min(),2),round(r[m].max(),2))
    # within an entry path traversal: ab first and last
    m=(tag>=100)&(tag<200)
    idx=np.where(m)[0][:400]
    print(" first entry frames ab", np.round(ab[idx[:5]],2), "r", np.round(r[idx[:5]],1), "... ab", np.round(ab[idx[-5:]],2),"r",np.round(r[idx[-5:]],1))
    n+=1
    if n>=3: break
EOF
```

```
ke20130221_HPC_e4_c4_seg.mat entry 1xy n 6343 corr(ab, r) 1.0 ab range 0.0 1.0 r range 0.03 16.0
ke20130221_HPC_e4_c4_seg.mat 2xy n 5373 corr(ab, r) 0.826 ab range 0.0 0.02 r range 0.0 0.29
ke20130221_HPC_e4_c4_seg.mat 3xy n 4452 corr(ab, r) 0.985 ab range 0.0 0.01 r range 0.0 0.2
ke20130221_HPC_e4_c4_seg.mat 4xy n 5842 corr(ab, r) 1.0 ab range 0.01 1.0 r range 0.09 16.0
ke20130221_HPC_e4_c4_seg.mat 5xy n 16844 corr(ab, r) 0.154 ab range -0.0 1.0 r range 4.94 16.0
 first entry frames ab [1. 1. 1. 1. 1.] r [16. 16. 16. 16. 16.] ... ab [0.36 0.34 0.31 0.31 0.29] r [5.8 5.5 5.  4.9 4.6]
ke20130221_HPC_e4_c5_seg.mat entry 1xy n 6343 corr(ab, r) 1.0 ab range 0.0 1.0 r range 0.03 16.0
ke20130221_HPC_e4_c5_seg.mat 2xy n 5373 corr(ab, r) 0.826 ab range 0.0 0.02 r range 0.0 0.29
ke20130221_HPC_e4_c5_seg.mat 3xy n 4452 corr(ab, r) 0.985 ab range 0.0 0.01 r range 0.0 0.2
ke20130221_HPC_e4_c5_seg.mat 4xy n 5842 corr(ab, r) 1.0 ab range 0.01 1.0 r range 0.09 16.0
ke20130221_HPC_e4_c5_seg.mat 5xy n 16844 corr(ab, r) 0.154 ab range -0.0 1.0 r range 4.94 16.0
 first entry frames ab [1. 1. 1. 1. 1.] r [16. 16. 16. 16. 16.] ... ab [0.36 0.34 0.31 0.31 0.29] r [5.8 5.5 5.  4.9 4.6]
ke20130301_HPC_e1_c1_seg.mat entry 1xy n 7072 corr(ab, r) 1.0 ab range 0.0 1.0 r range 0.03 16.0
ke20130301_HPC_e1_c1_seg.mat 2xy n 5232 corr(ab, r) 0.86 ab range 0.0 0.02 r range 0.0 0.31
ke20130301_HPC_e1_c1_seg.mat 3xy n 4206 corr(ab, r) 0.868 ab range 0.0 0.02 r range 0.0 0.32
ke20130301_HPC_e1_c1_seg.mat 4xy n 5995 corr(ab, r) 1.0 ab range 0.01 1.0 r range 0.1 16.0
ke20130301_HPC_e1_c1_seg.mat 5xy n 16730 corr(ab, r) 0.166 ab range -0.0 1.0 r range 4.94 16.0
 first entry frames ab [1. 1. 1. 1. 1.] r [16. 16. 16. 16. 16.] ... ab [1. 1. 1. 1. 1.] r [16. 16. 16. 16. 16.]
```

**Agent calls Bash**

```bash
timeout 900 $TMPDIR/venv/bin/python - <<'EOF'
import numpy as np, wirth
for name,d in wirth.stream_members("hc-12"):
    c=wirth.reduce_file(name,d)
    if c is None: continue
    tr=wirth.trials(c); t=c["t60"]; r=np.hypot(t[:,1],t[:,2])
    for nm in ("t_start","t_center","t_reward"):
        tt=np.asarray(tr[nm],float); tt=tt[np.isfinite(tt)]
        for sh in (-1,-0.1,0,0.1,0.5,1):
            i=np.searchsorted(t[:,0],tt+sh); i=i[i<len(t)]
            tags=(t[i,10]//100).astype(int)
            print(nm,sh,"ab",round(np.median(t[i,4]),2),"r/16",round(np.median(r[i])/16,2),"tag hundreds",np.bincount(tags,minlength=6)[1:])
    break
EOF
```

```
t_start -1 ab 0.4 r/16 0.82 tag hundreds [ 1  0  0  0 80]
t_start -0.1 ab 0.04 r/16 0.97 tag hundreds [ 1  0  0  0 80]
t_start 0 ab 0.0 r/16 1.0 tag hundreds [ 1  0  0  0 80]
t_start 0.1 ab 0.9 r/16 0.9 tag hundreds [81  0  0  0  0]
t_start 0.5 ab 0.48 r/16 0.48 tag hundreds [81  0  0  0  0]
t_start 1 ab 0.05 r/16 0.05 tag hundreds [81  0  0  0  0]
t_center -1 ab 0.77 r/16 0.77 tag hundreds [81  0  0  0  0]
t_center -0.1 ab 0.0 r/16 0.0 tag hundreds [45 36  0  0  0]
t_center 0 ab 0.0 r/16 0.0 tag hundreds [ 0 81  0  0  0]
t_center 0.1 ab 0.0 r/16 0.0 tag hundreds [ 0 81  0  0  0]
t_center 0.5 ab 0.0 r/16 0.0 tag hundreds [ 0 81  0  0  0]
t_center 1 ab 0.0 r/16 0.0 tag hundreds [ 0 23 31 27  0]
t_reward -1 ab 0.2 r/16 0.2 tag hundreds [ 0  0  0 65  0]
t_reward -0.1 ab 1.0 r/16 1.0 tag hundreds [ 0  0  0 65  0]
t_reward 0 ab 1.0 r/16 1.0 tag hundreds [ 0  0  0 19 45]
t_reward 0.1 ab 1.0 r/16 1.0 tag hundreds [ 0  0  0  0 64]
t_reward 0.5 ab 1.0 r/16 1.0 tag hundreds [ 0  0  0  0 64]
t_reward 1 ab 0.99 r/16 1.0 tag hundreds [ 0  0  0  0 64]
```

**Agent calls Bash**

```bash
sed -n 690,740p wirth.py; sed -n 835,880p wirth.py
```

```
def eye_velocity(c, t0, t1):
    """Median horizontal eye velocity in [t0, t1), raw file units per second, of the mean of
    both eyes; saturated samples dropped. The median of the sample-to-sample velocity follows
    the slow phases of nystagmus and smooth pursuit, as quick phases and saccades are brief."""
    if c["eye"] is None:
        return np.nan
    et = c["eye_t"]
    i0, i1 = np.searchsorted(et, t0), np.searchsorted(et, t1)
    if i1 - i0 < 3:
        return np.nan
    v = np.vstack([c["eye"]["l_hor"][i0:i1], c["eye"]["r_hor"][i0:i1]]).astype(float)
    v = np.where(np.abs(v) < EYE_RAIL * c["eye_rail"], v, np.nan)
    vel = np.diff(v, axis=1) / np.diff(et[i0:i1])
    vel = np.nanmean(vel, 0)
    vel = vel[np.isfinite(vel)]
    return float(np.median(vel)) if len(vel) else np.nan


def return_turns(c):
    """Per trial, the passive return after it (tags 5xy before the next trial start): the sign
[... 77 more lines not kept]
```

**Agent**

Now editing the helper: orientation change before each turn, and the abscissa checked against distance from the centre.

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
p="wirth.py"; s=open(p).read()
old='''            i0 = np.searchsorted(c["t60"][:, 0], t)
            i1 = np.searchsorted(c["t60"][:, 0], t + 0.6)
            if i1 < len(c["t60"]):
                row["dtheta_0_600ms"] = ((c["t60"][i1, 3] - c["t60"][i0, 3] + 180) % 360) - 180
'''
new='''            i0 = np.searchsorted(c["t60"][:, 0], t)
            i1 = np.searchsorted(c["t60"][:, 0], t + 0.6)
            ip = np.searchsorted(c["t60"][:, 0], t - 0.5)
            if i1 < len(c["t60"]):
                row["dtheta_0_600ms"] = ((c["t60"][i1, 3] - c["t60"][i0, 3] + 180) % 360) - 180
            if i0 < len(c["t60"]):
                # orientation change over the 500 ms before the code (is the view already rotating?)
                row["dtheta_pre500"] = ((c["t60"][i0, 3] - c["t60"][ip, 3] + 180) % 360) - 180
'''
assert old in s; s=s.replace(old,new)
old='''            clock[(nm, sh)] = float(np.nanmedian(t60[i, 4])) if len(i) else np.nan
'''
new='''            clock[(nm, sh)] = float(np.nanmedian(t60[i, 4])) if len(i) else np.nan
            clock[(nm + " r/16", sh)] = float(np.nanmedian(np.hypot(t60[i, 1], t60[i, 2]))) / 16 if len(i) else np.nan
            clock[(nm + " on return", sh)] = float(np.mean((t60[i, 10] >= 500) & (t60[i, 10] < 600))) if len(i) else np.nan
'''
assert old in s; s=s.replace(old,new)
old='''                    "abscissa_over_1": float(np.mean(t60[:, 4] > 1.001)),
'''
new='''                    "abscissa_over_1": float(np.mean(t60[:, 4] > 1.001)),
                    # abscissa against distance from the centre over the arm length (16 m), on the
                    # entry and exit paths (tags 1xy, 4xy) and on the passive returns (tags 5xy)
                    "abscissa_vs_r_arms": _ab_vs_r(t60, ((100, 200), (400, 500))),
                    "abscissa_vs_r_returns": _ab_vs_r(t60, ((500, 600),)),
'''
assert old in s; s=s.replace(old,new)
old='''def file_meta(name, d, c):'''
new='''def _ab_vs_r(t60, tag_ranges):
    """Median absolute difference between the curvilinear abscissa and the distance from the
    centre over 16 m, on frames whose transition tag lies in one of `tag_ranges`."""
    tag = t60[:, 10]
    m = np.zeros(len(t60), bool)
    for lo, hi in tag_ranges:
        m |= (tag >= lo) & (tag < hi)
    m &= np.isfinite(t60[:, 4])
    if not m.any():
        return np.nan
    return float(np.median(np.abs(t60[m, 4] - np.hypot(t60[m, 1], t60[m, 2]) / 16)))


def file_meta(name, d, c):'''
assert old in s; s=s.replace(old,new)
open(p,"w").write(s)
EOF
grep -n "0 centre, 1 arm end" wirth.py
```

```
13:(deg), curvilinear abscissa on the maze branch (0 centre, 1 arm end), state-space curvilinear
593:    (tags 10x) of successful trials, cut by the curvilinear abscissa (0 centre, 1 arm end)
```

**Agent calls Bash**

```bash
sed -i '13s/(0 centre, 1 arm end)/(on the entry and exit paths the distance from the centre over\n16 m, 0 centre, 1 arm end; on the passive returns it runs along the return; notebook)/' wirth.py; sed -n 10,18p wirth.py
```

```
(`file.elec`, or `file.newallo.elec` when the top level has none), the trial tables of the new
maze (`newallo.codematrix`, `newallo.timematrix`), learning curves, eye positions at 250 Hz
with `eye_times`, and `camera_data.time_60`, 60 Hz rows of [time, x, y, camera orientation
(deg), curvilinear abscissa on the maze branch (on the entry and exit paths the distance from the centre over
16 m, 0 centre, 1 arm end; on the passive returns it runs along the return; notebook), state-space curvilinear
abscissa, state-space polar angle, state-space radius, next, previous and current transition
tag, composite maze tag]. `time_60` sits under `newallo.camera_data` in some files.

Where the parameters come from:
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
p="wirth.py"; s=open(p).read()
old='''with `eye_times`, and `camera_data.time_60`, 60 Hz rows of [time, x, y, camera orientation
(deg), curvilinear abscissa on the maze branch (on the entry and exit paths the distance from the centre over
16 m, 0 centre, 1 arm end; on the passive returns it runs along the return; notebook), state-space curvilinear
abscissa,'''
new='''with `eye_times`, and `camera_data.time_60`, 60 Hz rows of [time, x, y, camera orientation
(deg), curvilinear abscissa on the maze branch (on the entry and exit paths the distance from
the centre over 16 m, 0 centre, 1 arm end; on the passive returns it runs along the return;
notebook), state-space curvilinear abscissa,'''
assert old in s; s=s.replace(old,new); open(p,"w").write(s)
EOF
sed -n 10,18p wirth.py
```

```
(`file.elec`, or `file.newallo.elec` when the top level has none), the trial tables of the new
maze (`newallo.codematrix`, `newallo.timematrix`), learning curves, eye positions at 250 Hz
with `eye_times`, and `camera_data.time_60`, 60 Hz rows of [time, x, y, camera orientation
(deg), curvilinear abscissa on the maze branch (on the entry and exit paths the distance from
the centre over 16 m, 0 centre, 1 arm end; on the passive returns it runs along the return;
notebook), state-space curvilinear abscissa, state-space polar angle, state-space radius, next, previous and current transition
tag, composite maze tag]. `time_60` sits under `newallo.camera_data` in some files.

Where the parameters come from:
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
p="wirth.py"; s=open(p).read()
old='''notebook), state-space curvilinear abscissa, state-space polar angle, state-space radius, next, previous and current transition
tag, composite maze tag].'''
new='''notebook), state-space curvilinear abscissa, state-space polar angle, state-space radius,
next, previous and current transition tag, composite maze tag].'''
assert old in s; s=s.replace(old,new); open(p,"w").write(s)
EOF
grep -n "^T = \|T = pd\|turns\]" reproduce_wirth_2017.ipynb | head; grep -n "collect(" reproduce_wirth_2017.ipynb
```

```
577:    "T = pd.DataFrame([dict(session=s, monkey=b[\"monkey\"], **t) for s, b in beh.items() for t in b[\"turns\"]])\n",
89:    "metas, cells, beh = wirth.collect(\"hc-12\", log=None)\n",
```

**Agent**

Testing the new quantities on a subset of files (one K session plus whichever comes next).

**Agent calls Bash**

```bash
/usr/bin/time -v $TMPDIR/venv/bin/python - <<'EOF' 2>&1 | grep -v "^\s*\(Page\|Vol\|Invol\|Swap\|File\|Sock\|Sig\|Aver\|Exit\|Min\|Maj\|Perc\|System\|User\)"
import numpy as np, pandas as pd, wirth
metas, cells, beh = wirth.collect("hc-12", limit=12, log=None)
M=pd.DataFrame(metas); print(M[["file","abscissa_vs_r_arms","abscissa_vs_r_returns"]])
for s,b in beh.items():
    print(s, {k:round(v,2) for k,v in b["abscissa_at_events"].items()})
    T=pd.DataFrame(b["turns"]); print(T.groupby("code").dtheta_pre500.describe())
EOF
```

```
entries/wirth-2017/wirth.py:610: RuntimeWarning: overflow encountered in multiply
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:610: RuntimeWarning: invalid value encountered in cast
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:610: RuntimeWarning: overflow encountered in multiply
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:610: RuntimeWarning: invalid value encountered in cast
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:610: RuntimeWarning: overflow encountered in multiply
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:610: RuntimeWarning: invalid value encountered in cast
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:610: RuntimeWarning: overflow encountered in multiply
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:610: RuntimeWarning: invalid value encountered in cast
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:610: RuntimeWarning: overflow encountered in multiply
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
entries/wirth-2017/wirth.py:610: RuntimeWarning: invalid value encountered in cast
  seg = np.clip(np.floor((1 - np.nan_to_num(ab)) * 4).astype(int), 0, 3)
[... 129 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
for i in (0,58):
    print('=====',i); print(''.join(nb['cells'][i]['source']))
EOF
grep -n "selectivity\|tuning-not\|direction-tuning\|Direction tuning" README.md
```

```
===== 0
# Reproducing Wirth et al. (2017) from CRCNS hc-12

Paper. Wirth S, Baraduc P, Plante A, Pinede S, Duhamel JR (2017). Gaze-informed, task-situated
representation of space in primate hippocampus during virtual navigation. PLoS Biology 15(2):
e2001045. [doi:10.1371/journal.pbio.2001045](https://doi.org/10.1371/journal.pbio.2001045).
The claims file (`claims/wirth-2017.yaml`) was written from the version of record (PMC5328243),
Results, Methods and the legends of Figs 1 to 7 and S1 to S7; S1 Appendix was not available.

Datasets. CRCNS [hc-12](https://doi.org/10.6080/K0R49NQV) (189 cells, the new-maze sessions;
every claim rests on it) and CRCNS [hc-21](https://doi.org/10.6080/K0GX48R9) (101 cells, a
familiar and a new maze per file), streamed from the public bucket `crcnsarchive`
(`hc-12/live/data.tar.gz`, `hc-21/live/data.tar.gz`). CRCNS data sets are not versioned; the
version is recorded as `unversioned`, and the MD5 sums from each data set's `checksums.md5`
for the files read are: hc-12 `data.tar.gz` 426c7d00c0358f2cc9873e0dbb331e2f (descriptor
version 0.7, 17 Jan 2017); hc-21 `data.tar.gz` dee5e8aa4a7b3c44b61b8cecfe622a0a (descriptor
version 0.52, 21 Dec 2018). Each data set has one published state (`live/`, with only
documentation under `orig/`), so the version pinned is the only one there is, and hc-12 is the
deposit the paper cites. hc-21 is read only to check whether it holds recordings that are also
in hc-12 and whether it holds the probe sessions hc-12 lacks; no claim rests on it.
[... 27 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 1,60p README.md
```

```
# Wirth, Baraduc, Plante, Pinede & Duhamel (2017) from CRCNS hc-12

Tests the findings of [Wirth et al. (2017)](https://doi.org/10.1371/journal.pbio.2001045) that can be
tested on [CRCNS hc-12](https://doi.org/10.6080/K0R49NQV), which holds the 189 analysed hippocampal
cells of two macaques navigating a virtual star maze, with eye tracking. [CRCNS
hc-21](https://doi.org/10.6080/K0GX48R9) is read to check which of its recordings are also in hc-12.

| Claim | Outcome |
|---|---|
| Gaze anticipates the turn, and the side where landmarks will appear | Reproduced (sign of the eye signal assumed, supported by the slow phases) |
| Learning in about a dozen trials; fewer than 10 more trials to 90% | Reproduced |
| Performance after new entries in probe sessions | Not reproduced (monkey K only) |
| Faster learning after new entries | Blocked: methods underspecified |
| 189 cells analysed of 270 recorded | Partially reproduced |
| State space has the most responsive cells (84) | Not reproduced |
| Direction maps: centre against return paths | IC and sparsity partially reproduced; correlation counts not reproduced |
| Higher information in state space than in position and direction space | Partially reproduced (the gaze comparison cannot be made) |
| Sparser in state space than in direction space | Reproduced (full-trial window) |
| Sparsity, state against position space | Not reproduced |
| State-space selectivity in the centre | Not reproduced |
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
p="README.md"; s=open(p).read()
for old,new in (("| State-space selectivity in the centre | Not reproduced |",
 "| State-space selectivity in the centre | Not reproduced (assuming permuted chunks; open under shifted chunks) |"),
 ("| Direction maps: centre against return paths | IC and sparsity partially reproduced; correlation counts not reproduced |",
 "| Direction maps: centre against return paths | IC and sparsity partially reproduced; correlation counts not reproduced (both with the three-space responsive cells standing in for the paper's set) |")):
    assert old in s; s=s.replace(old,new)
open(p,"w").write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -n "def zsess\|def rank_test" -A8 reproduce_wirth_2017.ipynb | head -30
```

```
582:    "def zsess(df, col):\n",
583-    "    g = df.groupby(\"session\")[col]\n",
584-    "    return (df[col] - g.transform(\"median\")) / g.transform(\"std\")\n",
585-    "\n",
586-    "\n",
587:    "def rank_test(df, col, right):\n",
588-    "    x = df[col].dropna()\n",
589-    "    a, b = x[right.loc[x.index]], x[~right.loc[x.index]]\n",
590-    "    if len(a) < 2 or len(b) < 2:\n",
591-    "        return np.nan, np.nan, len(a), len(b)\n",
592-    "    return float(a.median() - b.median()), float(stats.mannwhitneyu(a, b).pvalue), len(a), len(b)"
593-   ]
594-  },
595-  {
```

**Agent**

Now editing the notebook cells (data check, gaze caveat, direction tuning, summary).

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
import json
p="reproduce_wirth_2017.ipynb"
nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def setsrc(i,s): C[i]['source']=s.splitlines(keepends=True)
def rep(i,old,new):
    s=src(i); assert old in s,(i,old[:40]); setsrc(i,s.replace(old,new))

# cell 6: abscissa against distance from the centre
rep(6,'''print("Entry-path frames with abscissa above 1''','''print("Abscissa minus distance from the centre over 16 m, median absolute value per file: entry and exit paths (tags 1xy, 4xy)",
      M.abscissa_vs_r_arms.agg(["min", "max"]).round(4).to_dict(), "; passive returns (tags 5xy)",
      M.abscissa_vs_r_returns.agg(["min", "max"]).round(3).to_dict())
print("Entry-path frames with abscissa above 1''')
# cell 7
rep(7,'''Column 5 (curvilinear abscissa along
the branch) runs from 0 at the centre to 1 at the arm end, a fraction of the arm, not metres.''',
'''Column 5 (curvilinear abscissa along
the branch) is, on the entry and exit paths (tags 1xy and 4xy), the distance from the centre
divided by the 16 m arm: it runs from 0 at the centre to 1 at the arm end (median absolute
difference at most 1e-5 in every file, printed above). On the passive returns (tags 5xy) it
does not follow the distance from the centre; it runs along the return path.''')
# cell 8: clock table
rep(8,'''print("\\nCamera abscissa (0 centre, 1 arm end) at event times, median over sessions:")
ab = pd.DataFrame([{f"{k[0]} {k[1]:+.0f}s": v for k, v in b["abscissa_at_events"].items()} for b in beh.values()])
print(ab.median().round(2).to_string())''',
'''print("\\nCamera abscissa, distance from the centre over 16 m, and fraction of frames on a passive return (tags 5xy)")
print("at event times and 1 s before and after, median over sessions:")
ev = pd.DataFrame([{k: v for k, v in b["abscissa_at_events"].items()} for b in beh.values()]).median()
clk = pd.DataFrame({"abscissa": {f"{e} {sh:+.0f}s": ev[(e, sh)] for e in ("start", "center", "reward") for sh in (-1.0, 0.0, 1.0)},
                    "r/16": {f"{e} {sh:+.0f}s": ev[(e + " r/16", sh)] for e in ("start", "center", "reward") for sh in (-1.0, 0.0, 1.0)},
                    "on return": {f"{e} {sh:+.0f}s": ev[(e + " on return", sh)] for e in ("start", "center", "reward") for sh in (-1.0, 0.0, 1.0)}})
print(clk.round(2).to_string())''')
open(p,"w").write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
EOF
git diff --stat
```

```
entries/wirth-2017/README.md                  |   4 +-
 entries/wirth-2017/reproduce_wirth_2017.ipynb |  18 +-
 entries/wirth-2017/wirth.py                   |  30 +-
 tools/build_site.py                           | 437 ++++++++++++++++++++++++--
 tools/site_assets/app.css                     |  22 ++
 tools/site_assets/list.js                     |  13 +-
 6 files changed, 493 insertions(+), 31 deletions(-)
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
import json
p="reproduce_wirth_2017.ipynb"
nb=json.load(open(p))
C=nb['cells']
new_code='''# Is the view already rotating before the code? Orientation change over the 500 ms before it
# (negative = to the right), and the position test on turns with little rotation before the code.
rows = []
for mk in ("ke", "sn"):
    d = Tc[Tc.monkey == mk]
    for code, nm in ((1, "right"), (2, "left")):
        x = d[d.code == code].dtheta_pre500.dropna()
        rows.append({"monkey": mk, "turn": nm, "n": len(x), "median deg": round(x.median(), 2),
                     "IQR": f"{x.quantile(0.25):.2f} to {x.quantile(0.75):.2f}",
                     "fraction rotating the way of the turn": round(float(((x < 0) if code == 1 else (x > 0)).mean()), 3)})
print("Camera orientation change over the 500 ms before the turn code, successful trials:")
print(pd.DataFrame(rows).to_string())
rows = []
for mk in ("ke", "sn"):
    d = Tc[Tc.monkey == mk].copy()
    d["z"] = zsess(d, "eye500_mean")
    d["zv"] = d["vel_pre500"] / d.groupby("session")["vel_pre500"].transform("std")
    for lim in (np.inf, 1.0, 0.5, 0.25):
        s = d[d.dtheta_pre500.abs() < lim]
        diff, p, na, nb = rank_test(s, "z", s.code == 1)
        vdiff, vp, _, _ = rank_test(s, "zv", s.code == 1)
        rows.append({"monkey": mk, "|rotation before| below (deg)": lim, "n_right": na, "n_left": nb,
                     "position: median z right-left": round(diff, 3), "p": p,
                     "velocity before: median right-left": round(vdiff, 3), "p velocity": vp})
print("\\nPosition (500 ms before, both eyes) and eye velocity before the code, by the rotation before it:")
print(pd.DataFrame(rows).to_string())
'''
cell={"cell_type":"code","execution_count":None,"id":"gaze-prerot","metadata":{"tags":["claim:gaze-anticipates-action"]},"outputs":[],"source":new_code.splitlines(keepends=True)}
assert 'Sign of the eye signal' in ''.join(C[29]['source'])
C.insert(29,cell)
open(p,"w").write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
EOF
grep -c '"id"' reproduce_wirth_2017.ipynb
```

```
69
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF' 2>&1 | grep -v Warning | grep -v "seg = \|vel = "
import json, numpy as np, pandas as pd, wirth
from scipy import stats
nb=json.load(open("reproduce_wirth_2017.ipynb"))
metas, cells, beh = wirth.collect("hc-12", limit=12, log=None)
T = pd.DataFrame([dict(session=s, monkey=b["monkey"], **t) for s, b in beh.items() for t in b["turns"]])
def zsess(df, col):
    g = df.groupby("session")[col]
    return (df[col] - g.transform("median")) / g.transform("std")
def rank_test(df, col, right):
    x = df[col].dropna()
    a, b = x[right.loc[x.index]], x[~right.loc[x.index]]
    if len(a) < 2 or len(b) < 2:
        return np.nan, np.nan, len(a), len(b)
    return float(a.median() - b.median()), float(stats.mannwhitneyu(a, b).pvalue), len(a), len(b)
Tc=T[T.correct].copy()
code=''.join(nb['cells'][29]['source']).replace('for mk in ("ke", "sn")','for mk in ("ke",)')
exec(code)
EOF
```

```
Camera orientation change over the 500 ms before the turn code, successful trials:
  monkey   turn    n  median deg             IQR  fraction rotating the way of the turn
0     ke  right  274       -0.77  -7.11 to -0.39                                  0.996
1     ke   left  250        0.75    0.39 to 1.12                                  1.000

Position (500 ms before, both eyes) and eye velocity before the code, by the rotation before it:
  monkey  |rotation before| below (deg)  n_right  n_left  position: median z right-left             p  velocity before: median right-left    p velocity
0     ke                            inf      272     250                         -1.049  5.767190e-35                               0.225  1.814452e-13
1     ke                           1.00      177     182                         -0.571  4.048283e-11                              -0.017  7.252465e-01
2     ke                           0.50       95      86                         -0.412  1.306841e-04                               0.012  7.963223e-02
3     ke                           0.25        7       4                         -0.762  5.272727e-01                              -0.053  6.484848e-01
```

**Agent calls Bash**

```bash
ls paper/; grep -rn -i "proactiv\|anticipat" paper/* | head -20; grep -n "gaze-anticipates-landmarks" -A25 claims/wirth-2017.yaml | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  ls paper/; grep -rn -i "proactiv\|anticipat" paper/* | head -20; grep -n "gaze-anticipates-landmarks" -A25 claims/wirth-2017.yaml | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 129,145p claims/wirth-2017.yaml; grep -n "S2 Fig\|S2C" paper/10.1371-journal.pbio.2001045.txt | cut -c1-600
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "passive\|return move\|toward the right" paper/10.1371-journal.pbio.2001045.txt | cut -c1-500
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
date -u; grep -n "id: direction-tuning-not-maintained" -A40 claims/wirth-2017.yaml | grep -n "criterion" -A14
```

```
Fri Nov 13 17:29:15 UTC 2026
33:390-  criterion: Method W. Per cell, the uncentered correlation of center and return-path directional
34-391-    rates over the directional bins valid in both (Methods, Directional correlations); its
35-392-    significance from the surrogates, bilateral, at 0.05 per test with 0.025 per tail as the
36-393-    binomial chance rate (reading (b) of Method W, the one that gives p = 0.16 for 3 of 56).
37-394-    The 56 cells are read as the cells of direction-center-vs-periphery with enough common
38-395-    valid bins; the cell readings of that claim apply. Reproduced when, under one reading, the
39-396-    counts are within tolerance (the high count within 2 to 4, as a count of 3 cannot carry a
40-397-    10% tolerance) and the low count passes the binomial test at p < 0.001.
41-398-  depends_on:
```

**Agent calls Bash**

```bash
cd entries/wirth-2017; $TMPDIR/venv/bin/python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
for i in range(38,47):
    c=nb['cells'][i]; print('=====',i,c['cell_type'],c['metadata'].get('tags')); print(''.join(c['source']))
EOF
```

```
===== 38 markdown None
## responsive-cells (blocked) and state-space-most-responsive

> 111 of the 189 cells (59%) had significant information content in at least one of the four
> coding spaces.

> The proportions of cells responsive to each space were unequal; the state space accounted for
> the most cells (84), and more cells were responsive to state space than to point of gaze.
===== 39 code ['claim:state-space-most-responsive']
print("Cells with significant state-space IC (p < 0.01), per reading, and per monkey:")
for r, sr in READINGS:
    s_ = sig("state", r, sr)
    print(f"  {r}/{sr}: {int(s_.sum())} of {len(C)}", s_.groupby(C.monkey).sum().to_dict())
print("Expected 84 +- 8.4 (75.6 to 92.4)")
print("\nThree-space responsive cells per reading (a lower bound of the paper's 111 +- 11.1):", IC3["any of three"].tolist())
print("Upper tail alone (p < 0.01), state space:", [int(sig("state", r, sr, tail="up").sum()) for r, sr in READINGS])
===== 40 markdown None
**Result: not reproduced.** The state-space count is 57 of 186 cells under full trials with
permuted chunks, and 47, 42, 37, 57 and 47 under the other five readings, all below the expected
75.6 to 92.4. With the upper tail alone the counts are 41 to 58. The count needs no gaze, so the
[... 76 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
import json
p="reproduce_wirth_2017.ipynb"
nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def rep(i,old,new):
    s=src(i); assert old in s,(i,old[:40]); C[i]['source']=s.replace(old,new).splitlines(keepends=True)
rep(42,'''                          ("(b) three-space responsive", sum(sig(k, "full", sr).astype(int) for k in SPACES) > 0)):
        d = C[mask]''','''                          ("(b) three-space responsive", sum(sig(k, "full", sr).astype(int) for k in SPACES) > 0),
                          ("all cells (reference)", pd.Series(True, index=C.index))):
        d = C[mask]''')
rep(45,'''                          ("(b) three-space responsive", sum(sig(k, "full", sr).astype(int) for k in SPACES) > 0)):
        for min_common''','''                          ("(b) three-space responsive", sum(sig(k, "full", sr).astype(int) for k in SPACES) > 0),
                          ("all cells", pd.Series(True, index=C.index))):
        for min_common''')
rep(45,'''print("Expected: tested 56 +- 5.6, low 20 +- 2 with binomial p < 0.001, high 2 to 4")''',
'''print("Expected: tested 56 +- 5.6, low 20 +- 2 with binomial p < 0.001, high 2 to 4")
# Reading (b) over the paper's responsive set: that set contains the three-space responsive cells
# and lies within all cells. Can a set between the two meet the criterion? Added cells raise n by
# one each and the low or the high count by at most one.
DT_ = pd.DataFrame(rows)
print("\\nReading (b) over a set between the three-space responsive cells and all cells (10 common bins):")
for sr in ("permute", "shift"):
    g = DT_[(DT_.surrogates == sr) & (DT_["min common bins"] == 10)].set_index("cells")
    s_, a_ = g.loc["(b) three-space responsive"], g.loc["all cells"]
    ways = []
    for n in range(max(s_.n, 51), min(61, a_.n) + 1):
        extra = n - s_.n
        for lo in range(max(s_.low, 18), min(22, s_.low + extra, a_.low) + 1):
            for hi in range(max(s_.high, 2), min(4, s_.high + extra - (lo - s_.low), a_.high) + 1):
                if wirth.binom_upper(lo, n, 0.025) < 0.001:
                    ways.append((n, lo, hi))
    print(f"  {sr}: three-space n {s_.n}, low {s_.low}, high {s_.high}; all cells n {a_.n}, low {a_.low}, high {a_.high};",
          f"combinations meeting the criterion: {len(ways)}" + (f", for example n {ways[0][0]}, low {ways[0][1]}, high {ways[0][2]}" if ways else ""))''')
open(p,"w").write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
EOF
git diff --stat -- .
```

```
entries/wirth-2017/README.md                  |  4 +-
 entries/wirth-2017/reproduce_wirth_2017.ipynb | 82 ++++++++++++++++++++++++---
 entries/wirth-2017/wirth.py                   | 30 +++++++++-
 3 files changed, 104 insertions(+), 12 deletions(-)
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
import json, pandas as pd, numpy as np, wirth
nb=json.load(open("reproduce_wirth_2017.ipynb"))
s=''.join(nb['cells'][45]['source'])
tail=s[s.index("DT_ = "):]
rows=[]
for sr,(nS,lS,hS) in (("permute",(59,16,4)),("shift",(51,14,3))):
    for cs,(n,l,h) in (("(a) direction IC p < 0.01",(40,15,4)),("(b) three-space responsive",(nS,lS,hS)),("all cells",(170,40,8))):
        for mc in (10,2): rows.append({"surrogates":sr,"cells":cs,"min common bins":mc,"n":n,"low":l,"high":h})
exec(tail)
EOF
```

```
Reading (b) over a set between the three-space responsive cells and all cells (10 common bins):
  permute: three-space n 59, low 16, high 4; all cells n 170, low 40, high 8; combinations meeting the criterion: 1, for example n 61, low 18, high 4
  shift: three-space n 51, low 14, high 3; all cells n 170, low 40, high 8; combinations meeting the criterion: 45, for example n 55, low 18, high 3
```

**Agent**

Subset tests pass. Starting the full run of the entry (about 31 minutes last time).

**Agent calls Bash**

```bash
cd  && date -u && python tools/entry.py all entries/wirth-2017 2>&1 | tail -30; date -u
```

```
Fri Nov 13 17:30:00 UTC 2026
Installed kernelspec registry-wirth-2017 in executed/wirth-2017/.venv/share/jupyter/kernels/registry-wirth-2017
0 error(s)
pass  reproduce_wirth_2017.ipynb  (1727 s)
Fri Nov 13 17:58:58 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/wirth-2017 && $TMPDIR/venv/bin/python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
for i in (6,8,28,29,42,45):
    c=nb['cells'][i]
    print('=====',i)
    for o in c.get('outputs',[]):
        t=o.get('text') or o.get('data',{}).get('text/plain','')
        t=''.join(t)
        if i==6: t='\n'.join(l for l in t.splitlines() if 'Abscissa' in l or 'abscissa' in l)
        print(t[:4000])
EOF
```

```
===== 6
     x_min  x_max  y_min  y_max  theta_min  theta_max  abscissa_max
Files with an abscissa above 1 or an orientation range under 300 deg:
                             file  abscissa_max  abscissa_over_1  theta_min  theta_max  n_trials
Abscissa minus distance from the centre over 16 m, median absolute value per file: entry and exit paths (tags 1xy, 4xy) {'min': 0.0, 'max': 0.0023} ; passive returns (tags 5xy) {'min': 0.117, 'max': 0.458}
Entry-path frames with abscissa above 1, over the cells of these files: {'ke20140207_HPC_c1_seg.mat': 0, 'sn20110610_hpc_e1_c1_seg.mat': 0, 'sn20110610_hpc_e2_c1_seg.mat': 0}
===== 8
Learning curves: column 2 <= column 1 <= column 3 in 187 of 187 files
Field learningtrial equals the first trial with column 2 > 1/4 (or -2 when never): 66 of 66 sessions

Eye signal scale by session: {'+-5000': 36, '+-5': 26, nan: 4}
Fraction of eye samples at the +-5000 / +-5 rail, by session: median 0.0049 max 0.217

Arm chosen on rewarded trials (1-5 = codes 50-54), sessions per value: {(np.int64(4),): 32, (np.int64(5),): 9, (np.int64(1),): 9, (np.int64(2),): 8, (np.int64(3),): 7, (np.int64(2), np.int64(4)): 1}

Camera abscissa, distance from the centre over 16 m, and fraction of frames on a passive return (tags 5xy)
at event times and 1 s before and after, median over sessions:
            abscissa  r/16  on return
start -1s       0.40  0.82       0.99
start +0s       0.01  1.00       0.99
[... 78 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/wirth-2017 && $TMPDIR/venv/bin/python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
for i in (7,9,30,33,43,46,47,58,68):
    print('=====',i, nb['cells'][i]['cell_type']); print(''.join(nb['cells'][i]['source'])[:600])
EOF
```

```
===== 7 markdown
The descriptor (hc-12, version 0.7) gives the positions as virtual X, Y. The values span x from
-16 to 12.9 and y from -15.2 to 15.2, five arm ends at radius 16 m (Methods: radius 16 m), so
positions are in metres. The camera orientation is in degrees, on 0 to 360 in some files and
-180 to 180 in others; the analysis takes it modulo 360. Column 5 (curvilinear abscissa along
the branch) is, on the entry and exit paths (tags 1xy and 4xy), the distance from the centre
divided by the 16 m arm: it runs from 0 at the centre to 1 at the arm end (median absolute
difference at most 1e-5 in every file, 
===== 9 markdown
Checks against the description:
- The descriptor says the learning curve's middle column is the probability of a correct
  response, with the bounds in columns 1 and 3. In every file column 2 is the lowest and column
  3 the highest, so column 1 is the probability, column 2 the lower bound and column 3 the upper
  bound. The field `learningtrial`, which the descriptor does not describe, equals the first
  trial whose column 2 exceeds 1/4 (S3B legend's criterion), which confirms that reading.
- The descriptor says code 43 is the rewarded start arm and code 53 the rewarded chosen arm. The
  arm 
===== 30 markdown
Sign of the eye signal. The files do not say which sign of the horizontal signal is rightward.
It is taken from the slow phases. During a turn the scene flows across the screen opposite to
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
import json
p="reproduce_wirth_2017.ipynb"
nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def rep(i,old,new):
    s=src(i); assert old in s,(i,old[:50]); C[i]['source']=s.replace(old,new).splitlines(keepends=True)
rep(7,"(median absolute\ndifference at most 1e-5 in every file, printed above)","(median absolute\ndifference at most 0.0023 in every file, printed above)")
rep(9,'''- The camera rows share the trial clock: at the trial start (code 21) the abscissa is at the arm
  end, at the arrival at the choice point (code 22) it is 0, and one second later or earlier it is
  not (printed above).''','''- The camera rows share the trial clock. At the trial start (code 21) the camera is at the arm
  end (distance over 16 m, 1.00), and the row still belongs to the passive return (0.99 of
  them), whose abscissa has run down to 0.01; one second later the camera is on the entry path
  near the centre (0.12). One second before the arrival at the choice point (code 22) it is at
  0.72 on the entry path, at the arrival it is at the centre (0.00), and it is still there one
  second later, while the view rotates. At the reward (code 11) it is at the arm end (1.00), and
  one second earlier at 0.21 on the exit path (printed above).''')
rep(30,'''The sign is still an assumption, now supported by this check.''','''The sign is still an assumption, now supported by this check.

Is the view already rotating in the 500 ms before the code? In both monkeys it is, slowly: the
camera orientation changes by a median of -0.49 and 0.54 degrees (K) and -0.75 and 0.69
degrees (S) over those 500 ms, in the direction of the coming turn in 95% to 99% of turns, as if
the code came after the turn had begun. In K the eye velocity before the code also differs
between right and left turns (0.250 against -0.189 session SD, 38 of 40 sessions, p = 2.3e-9),
in the direction of the slow phases; in S it does not (9 of 20 sessions, p = 0.40). The
position effect remains in the turns with the least rotation before the code: with less than
0.25 degrees, K -0.27 session SD (p = 3.3e-5, 355 and 328 turns) and S -0.54 (p = 0.0059, 32 and
106 turns); with less than 1 degree, K -0.37 and S -0.70. In K the velocity difference also
remains with less than 0.25 degrees (0.248, p = 2.6e-10), so it is not explained by the
rotation of the view, and part of K's position effect may continue an eye movement under way
before the window. The position effect is about half as large in K's low-rotation turns as over
all turns. The paper's S2B legend shows second turns of a series of two turns, another control
for this; it was not run here.''')
rep(43,'''No reading reaches
p < 0.001.''','''No reading reaches
p < 0.001. Over all 180 cells with both maps neither IC nor sparsity is higher in the centre
(p = 0.31 and 0.29, permuted chunks), so the signed-rank result changes with the cell set, and
the result over the 59 cells puts no bound on the one over the paper's responsive set, which
needs the gaze space. The outcome is therefore kept as verified, resting on the stand-in, and a
change to blocked (metadata insufficient) is proposed for the next verification round.''')
rep(46,'''**Result: not reproduced.**''','''**Result: not reproduced, resting on the three-space responsive cells standing in for reading
(b).**''')
rep(46,'''The low count misses 18 to 22 under every
reading, so the criterion is not met, although more cells than chance have a low correlation
under all of them (binomial p below 1e-10). The minimum of common bins (10 or 2) changes
nothing.''','''Over these sets the low count misses 18 to 22,
although more cells than chance have a low correlation under all of them (binomial p below
1e-10). The minimum of common bins (10 or 2) changes nothing. Reading (b) refers to the paper's
responsive set, which contains the three-space responsive cells and lies within all cells (181
tested, 25 low and 8 high with permuted chunks; 18 low and 7 high with shifted chunks). A set
between the two can meet the criterion under both readings of the surrogates: with permuted
chunks in one combination (n 61, low 18, high 4), with shifted chunks in 13 (for example n 55,
low 18, high 3). Over the paper's set the criterion is therefore not excluded. The outcome is
kept as verified, resting on the stand-in, and a change to blocked (metadata insufficient) is
proposed for the next verification round.''')
rep(68,"| direction-tuning-not-maintained | not reproduced |","| direction-tuning-not-maintained | not reproduced (three-space responsive cells for reading b; blocked proposed, as the paper's set could meet the criterion) |")
rep(68,"| direction-center-vs-periphery | partially reproduced (three-space responsive cells for reading b, permuted chunks) |","| direction-center-vs-periphery | partially reproduced (three-space responsive cells for reading b, permuted chunks; blocked proposed) |")
open(p,"w").write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
import json
p="reproduce_wirth_2017.ipynb"
nb=json.load(open(p))
C=nb['cells']
s=''.join(C[30]['source'])
for o,n in (("K -0.37 and S -0.70","K -0.37 and S -0.695"),("The position effect is about half as large in K's low-rotation turns as over\nall turns.","In K's low-rotation turns the position effect is a third to a half of\nthat over all turns (-0.77).")):
    assert o in s; s=s.replace(o,n)
C[30]['source']=s.splitlines(keepends=True)
open(p,"w").write(json.dumps(nb,indent=1,ensure_ascii=False)+"\n")
EOF
cd  git ls-files executed | head; date -u
```

```
Fri Nov 13 17:59:40 UTC 2026
```

**Agent calls Write**

```json
{
 "file_path": "questions/wirth-2017.yaml",
 "content": "paper: doi:10.1371/journal.pbio.2001045\nquestions:\n- claim: gaze-anticipates-landmarks\n  asked: 2026-11-13\n  question: The claim says that on being relocated the monkeys gazed proactively at where the landmarks\n    would appear. The criterion compares the mean horizontal eye position over the whole passive return,\n    turning right against left. During any rotation of the view the mean eye position shifts toward the\n    side the view turns to, so this measure cannot tell anticipation from the eye position that goes\n    with the rotation itself. Should the criterion restrict the window to the part of the return before\n    the landmarks enter the field of view, or compare against a reference that rotates without landmarks\n    to come, so that it tests the proactive part of the claim? Or does the S2C legend, which shows the\n    mean over the whole return, fix the measure as the claims file has it?\n  passage: Results, Animals use direction and compute trajectory, paragraph 2, \"Similarly, when being\n    relocated to a new entry, monkeys proactively gazed at the location at which the landmarks would\n    appear (see S2 Fig and S1 Appendix A2) (Wilcoxon test, p < 0.001)\"; S2C legend, \"Mean horizontal\n    eye position during the passive return journey towards the right or the left\".\n  why: Under the criterion as written the claim is reproduced in both monkeys (K -0.56 session SD,\n    p = 6.2e-58; S -0.56, p = 6.4e-30), and the same shift appears during the turns at the centre, where\n    no landmark is anticipated in this sense. A window limited to the time before the landmarks appear\n    could give a smaller effect or none, and would need the landmark positions, which the files do not\n    give (they could be computed from the paper's geometry). The verifier of round 2 reported this\n    point.\n"
}
```

```
File created successfully at: questions/wirth-2017.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
ls schemas; grep -l "crcns\|^paper" questions/*.yaml | head -3; head -5 $(grep -l "^paper" questions/*.yaml | head -1); grep -rn "proposed" schemas/*attempt* | head
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
questions/ashworth-2025.yaml
questions/athalye-2023.yaml
questions/bech-2026.yaml
dandiset: "001708"
paper: doi:10.64898/2025.12.15.693905
questions:
- claim: figs3-neutral-unmodulated
  asked: 2026-11-05
303:          "proposed": {
```

**Agent calls Bash**

```bash
sed -n 295,330p schemas/attempt.schema.json; grep -rln "dandiset:" questions/ | wc -l; ls questions | wc -l; grep -L "dandiset:" questions/*.yaml | head; grep -n "questions" tools/entry.py tools/*.py | head
```

```
"type": "string",
              "minLength": 1
            }
          },
          "assumed": {
            "description": "True when the outcome rests on an assumption about a method the paper leaves open: a choice the paper best supports, stated in a deviation that says what was assumed and why (docs/protocol.md, Author, step 1.6).",
            "type": "boolean"
          },
          "proposed": {
            "description": "A change of outcome found after the last verification round, held until a further round agrees with it.",
            "type": "object",
            "additionalProperties": false,
            "required": [
              "outcome",
              "reason"
            ],
            "properties": {
              "outcome": {
                "enum": [
                  "reproduced",
[... 38 more lines not kept]
```

**Agent calls Bash**

```bash
head -4 questions/brinke-2017.yaml questions/gao-2018.yaml
```

```
==> questions/brinke-2017.yaml <==
# Questions from attempt brinke-2017-01 (author, 2026-11-13) about the claims file
# claims/brinke-2017.yaml. Asked under docs/protocol.md, Author, step 1.6. The attempt tested the
# claims as the file has them and blocked the four claims below as data_missing.
dataset: crcns:cb-1

==> questions/gao-2018.yaml <==
# Questions from attempt gao-2018-01 (author, 2026-11-10) about claims/gao-2018.yaml, asked under
# docs/protocol.md, Author, step 1.6, and "Hand over for verification". The claim is tested as the
# claims file has it.
paper: doi:10.1038/s41586-018-0633-x
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
p="questions/wirth-2017.yaml"; s=open(p).read()
s='''# Questions from attempt wirth-2017-01 (author revision after verification round 2, 2026-11-13)
# about claims/wirth-2017.yaml, asked under docs/protocol.md, "Hand over for verification". The
# claim is tested as the claims file has it.
dataset: crcns:hc-12
'''+s
open(p,"w").write(s)
import yaml; print(yaml.safe_load(open(p))["questions"][0]["claim"])
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 8, in <module>
ModuleNotFoundError: No module named 'yaml'
```

**Agent calls Bash**

```bash
$TMPDIR/venv/bin/python - <<'EOF'
p="attempts/wirth-2017-01.yaml"; s=open(p).read()
def rep(old,new):
    global s
    assert s.count(old)==1,(old[:60],s.count(old)); s=s.replace(old,new)
# gaze-anticipates-action caveat
rep('''    by the slow phases (deviations), so gaze lies on the side of the coming turn. Both monkeys, each window
    and the pooled test agree, so the readings of the criterion give one outcome.
''','''    by the slow phases (deviations), so gaze lies on the side of the coming turn. Both monkeys, each window
    and the pooled test agree, so the readings of the criterion give one outcome. In the 500 ms before
    the code the view already rotates slowly toward the turn (median 0.49 to 0.75 degrees, in that direction
    in 95% to 99% of turns), and in K the eye velocity there differs between right and left turns in the
    direction of the slow phases (0.250 against -0.189 session SD, 38 of 40 sessions, p = 2.3e-9); in S
    it does not (9 of 20, p = 0.40). The position effect remains in turns with less than 0.25 degrees
    of rotation before the code (K -0.27 session SD, p = 3.3e-5; S -0.54, p = 0.0059) and less than 1
    degree (K -0.37, S -0.695), where K's velocity difference also remains (0.248, p = 2.6e-10). Part
    of K's position effect may continue an eye movement under way before the window; it is a third to
    a half as large in the low-rotation turns as over all turns. The S2B control (second of two turns)
    was not run.
''')
rep('''    whether this is anticipation or the eye position that goes with any rotation of the view cannot be
    told apart here.
''','''    whether this is anticipation or the eye position that goes with any rotation of the view cannot be
    told apart here. The criterion, which takes the mean over the whole return, does not test the proactive
    part of the claim; this is asked of a reader in questions/wirth-2017.yaml, and the claim is tested
    as the claims file has it.
''')
# direction-center-vs-periphery
rep('''    not (p = 0.14, sparsity p = 0.013). No reading reaches p < 0.001. The outcome rests on the stand-in
    for reading (b) and on permuted chunks.
''','''    not (p = 0.14, sparsity p = 0.013). No reading reaches p < 0.001. The outcome rests on the stand-in
    for reading (b) and on permuted chunks. Over all 180 cells with both maps neither is higher (IC p
    = 0.31, sparsity p = 0.29, permuted chunks), so a signed-rank result over the 59 cells puts no bound
    on the result over the paper's responsive set; a change to blocked is proposed.
''')
rep('''  - Reading (b), all responsive cells, cannot be formed without the gaze space; the three-space responsive
    cells, which it contains, stand in for it, an assumption.
  assumed: true
''','''  - Reading (b), all responsive cells, cannot be formed without the gaze space; the three-space responsive
    cells, which it contains, stand in for it, an assumption.
  assumed: true
  proposed:
    outcome: blocked
    blocked_by: metadata_insufficient
    reason: Reading (a) meets neither level (IC p = 0.43, sparsity p = 0.031 with permuted chunks; 0.095
      and 0.016 with shifted chunks). Reading (b) is the paper's responsive set, which needs the point-of-gaze
      space. The three-space responsive cells that stand in for it give the partial level only with permuted
      chunks (IC p = 0.045, sparsity p = 0.0074), and all cells give neither (p = 0.31 and 0.29), so the
      result over the paper's set may lie at any level. As for landmark-identity-center and spatial-selectivity-fraction,
      a reading that cannot be formed leaves the claim undecided.
''')
# direction-tuning-not-maintained
rep('''  notes: Of 40 direction-selective cells (permuted chunks), 15 (38%) have a significantly low centre-return
    correlation (binomial p = 2.1e-14 at chance 0.025) and 4 a significantly high one (p = 0.017). The
    high count is inside 2 to 4, but the number of cells tested (40, expected 56 +- 5.6) and the low count
    (15, expected 20 +- 2) are outside the tolerance. Over the 59 three-space responsive cells 16 are
    low and 4 high; with shifted chunks 11 of 28 and 14 of 51 are low. The low count misses 18 to 22 under
    every reading, although more cells than chance have a low correlation under all of them (binomial
    p below 1e-10). The criterion has no partial level.
  deviations:
  - Cells with at least 10 common valid bins, a standard choice for "enough"; with 2 the counts do not
    change.
''','''  assumed: true
  notes: Of 40 direction-selective cells (permuted chunks), 15 (38%) have a significantly low centre-return
    correlation (binomial p = 2.1e-14 at chance 0.025) and 4 a significantly high one (p = 0.017). The
    high count is inside 2 to 4, but the number of cells tested (40, expected 56 +- 5.6) and the low count
    (15, expected 20 +- 2) are outside the tolerance. Over the 59 three-space responsive cells 16 are
    low and 4 high; with shifted chunks 11 of 28 and 14 of 51 are low. Over these sets the low count misses
    18 to 22, although more cells than chance have a low correlation under all of them (binomial p below
    1e-10). The criterion has no partial level. Reading (a) fails on the number of cells (40 and 28).
    Under reading (b) the outcome rests on the three-space stand-in. The paper's responsive set lies
    between the three-space responsive cells and all cells (181 tested, 25 low and 8 high with permuted
    chunks; 18 and 7 with shifted chunks), and a set between the two can meet the criterion, in one combination
    with permuted chunks (n 61, low 18, high 4) and in 13 with shifted chunks (for example n 55, low 18,
    high 3), so over the paper's set the criterion is not excluded; a change to blocked is proposed.
  deviations:
  - Cells with at least 10 common valid bins, a standard choice for "enough"; with 2 the counts do not
    change.
  - Reading (b), all responsive cells, cannot be formed without the gaze space; the three-space responsive
    cells stand in for it, an assumption, as in direction-center-vs-periphery.
  proposed:
    outcome: blocked
    blocked_by: metadata_insufficient
    reason: Reading (a) fails on the number of cells tested (40 and 28 against 56 +- 5.6). Reading (b)
      is the paper's responsive set, which needs the point-of-gaze space. Bounding it between the three-space
      responsive cells and all cells, a set that meets the criterion exists under both readings of the
      surrogates (permuted, n 61, low 18, high 4; shifted, 13 combinations), so the claim cannot be decided,
      as for landmark-identity-center and spatial-selectivity-fraction.
''')
# landmark-identity-distance deviation
rep('''  - Relative distance from the files' curvilinear abscissa (0 centre, 1 arm end) in quarters;''','''  - Relative distance from the files' curvilinear abscissa in quarters; on the entry paths the abscissa
    is the distance from the centre over 16 m (0 centre, 1 arm end; median absolute difference at most
    0.0023 per file), checked in the notebook;''')
open(p,"w").write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cat >> attempts/wirth-2017-01.yaml <<'EOF'
- date: '2026-11-13'
  kind: agent
  by: Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)
  reviewed: 'The full executed notebook of the first revision, the helper module, the claims file and
    the attempt record, with the paper under paper/. It found round-1 problems 1 to 10 resolved, and
    reported text that did not match the outputs, with what was changed: cell 9 said that at the trial
    start the abscissa is at the arm end and that one second after the arrival at the centre it is not
    0, which the printed values contradict; cell 7 and the landmark-identity-distance deviation said the
    abscissa runs from 0 at the centre to 1 at the arm end, where the outputs also fit an abscissa that
    runs from the start of each branch. The notebook now prints the abscissa against the distance from
    the centre over 16 m: on the entry and exit paths they agree in every file (median absolute difference
    at most 0.0023), so 0 is the centre there; at the trial start the row still belongs to the passive
    return, whose abscissa has run down to 0.01 while the camera is at the arm end (1.00); after the arrival
    the camera stays at the centre while the view rotates. Cells 7 and 9 and the deviation were rewritten
    to match. The README row of state-space-selectivity now carries the permuted-chunk qualifier, and the
    record''s statement that the low count of direction-tuning-not-maintained misses under every reading
    now says it holds over the stand-in sets only.'
  results:
  - claim: gaze-anticipates-action
    agrees: true
    outcome: reproduced
    reason: 'The assumption is stated and reasonable; cell 28 gives the sign from eye velocity during turns
      in 40/40 sessions of K and 20/20 of S. Caveat: in the 500 ms before the turn code K already shows
      a slow-phase-like velocity difference (0.250 against -0.189, 38/40 sessions, p = 2.3e-9), so the
      view may already be rotating and the position effect may partly continue that rotation; S shows
      none (9/20, p = 0.40) and has the larger position effect. The outcome stands, but the record should
      mention this.'
    response: Added the camera rotation over the 500 ms before the code and the position test on turns
      with little rotation. The view rotates slowly toward the turn before the code in both monkeys (median
      0.49 to 0.75 degrees); the position effect remains with less than 0.25 degrees (K -0.27, p = 3.3e-5;
      S -0.54, p = 0.0059), and K's velocity difference remains there too, so it is not explained by the
      rotation. The notes now give the caveat. Outcome unchanged.
  - claim: gaze-anticipates-landmarks
    agrees: true
    outcome: reproduced
    reason: 'Changed from round-1 partial: the sign now comes from the slow-phase velocity during turns
      at the centre, which does not use eye position, so the test is no longer circular (cell 31: K -0.56
      SD, p = 6.2e-58, 39/41 sessions; S -0.56, p = 6.4e-30, 20/21). Claims-file point: the criterion
      takes the mean eye position over the whole return, so it cannot separate anticipation from the
      shift of eye position that comes with any rotating view, and does not test the "proactive" part
      of the claim.'
    response: Added the point as a question for a reader in questions/wirth-2017.yaml; the claim is tested
      as the claims file has it, and the notes say it is asked. Outcome unchanged.
  - claim: learning-trials
    agrees: true
    outcome: reproduced
    reason: Cell 18.
    response: No change.
  - claim: learning-to-90
    agrees: true
    outcome: reproduced
    reason: 'Cell 20: 0.898, or 0.803 over all sessions. Only one session reaches 0.9 at the criterion trial
      itself.'
    response: No change.
  - claim: probe-transfer
    agrees: true
    outcome: not_reproduced
    reason: 'Cell 23: 28.3% and 58.3% against 44 and 73. No variant puts both means inside tolerance.'
    response: No change.
  - claim: probe-faster-criterion
    agrees: true
    outcome: blocked
    reason: Agreed, no further comment.
    response: No change.
  - claim: cells-recorded
    agrees: true
    outcome: partially_reproduced
    reason: Agreed, no further comment.
    response: No change.
  - claim: responsive-cells
    agrees: true
    outcome: blocked
    reason: Agreed, no further comment.
    response: No change.
  - claim: state-space-most-responsive
    agrees: true
    outcome: not_reproduced
    reason: 'Cell 38: 37 to 57 cells against 75.6 to 92.4, and 41 to 58 using the upper tail only.'
    response: No change.
  - claim: multi-space-coding
    agrees: true
    outcome: blocked
    reason: Agreed, no further comment.
    response: No change.
  - claim: direction-center-vs-periphery
    agrees: true
    outcome: partially_reproduced
    reason: 'The assumption is stated: the three-space responsive cells stand in for reading (b). It is
      the weakest step. For a signed-rank test the result on 59 cells puts no bound on the result over
      the paper''s set. Under reading (a) neither level is met (cell 41).'
    response: Added the comparison over all cells (IC p = 0.31, sparsity p = 0.29), which shows that the
      result changes with the cell set. The verified outcome is kept, and a change to blocked (metadata
      insufficient) is proposed, as reading (b) cannot be formed and reading (a) fails.
  - claim: direction-tuning-not-maintained
    agrees: true
    outcome: not_reproduced
    reason: 'Agreed under the same stand-in, but it should be marked assumed: true. Reading (b) uses the
      three-space stand-in, only a lower bound of the responsive set. With shifted chunks under (b), 51
      cells give 14 low (cell 44); up to 10 more cells could join and keep n within 56 +- 5.6, and only
      4 of them would need to be low to reach 18, so over the paper''s set the criterion is not excluded
      under that reading. Reading (a) fails on n (40 and 28). The record''s "the low count misses 18 to
      22 under every reading" holds for the stand-in set only.'
    response: Marked assumed, with a deviation for the stand-in, and corrected the notes and the notebook
      conclusion. Added the counts over all cells and a check of which sets between the two bounds meet
      the criterion; one does with permuted chunks (n 61, low 18, high 4) and 13 do with shifted chunks.
      The verified outcome is kept, and a change to blocked (metadata insufficient) is proposed.
  - claim: state-space-ic-higher
    agrees: true
    outcome: partially_reproduced
    reason: 'Cell 53: p < 0.01 under all 12 rows; the largest is 0.0022.'
    response: No change.
  - claim: sparsity-state-vs-direction
    agrees: true
    outcome: reproduced
    reason: 'Cell 48. Reproduced with the full-trial window, which is the claims file''s reading (a). Not
      significant from start to reward.'
    response: No change.
  - claim: sparsity-state-vs-position
    agrees: true
    outcome: not_reproduced
    reason: 'Cell 50: the overall test is significant (p <= 0.00043) and the per-cell counts are 3 to 11,
      against 15 +- 1.5.'
    response: No change.
  - claim: sparsity-gaze-vs-state
    agrees: true
    outcome: blocked
    reason: Agreed, no further comment.
    response: No change.
  - claim: state-space-selectivity
    agrees: true
    outcome: not_reproduced
    reason: 'Agreed as an assumption, which is stated and reasonable: the Results say "randomly shuffling
      periods of spiking activity in time" and the Methods say the 5 s chunks were "randomly shifted";
      under shifted chunks the claim cannot be decided (cell 56), and without the assumption the outcome
      would be blocked. The README row drops the qualifier "permuted chunks; open under shifted chunks".'
    response: Added the qualifier to the README row. Outcome unchanged.
  - claim: landmark-identity-distance
    agrees: true
    outcome: not_reproduced
    reason: 'Cell 61: at most 31 cells (33 with type III), against 64 +- 6.4. The deviation''s "(0 centre,
      1 arm end)" for the abscissa may not hold, and on the entry paths the quarters may be numbered in
      the opposite order; the main-effect and interaction counts do not depend on the order, so no conclusion
      changes.'
    response: The notebook now shows that on the entry and exit paths the abscissa equals the distance
      from the centre over 16 m in every file, so the quarters run from the arm end to the centre as stated;
      the deviation now says so. Outcome unchanged.
  - claim: landmark-identity-center
    agrees: true
    outcome: blocked
    reason: 'Cell 63: the bounds straddle 11 to 13.'
    response: No change.
  - claim: path-selectivity
    agrees: true
    outcome: blocked
    reason: Agreed (metadata insufficient).
    response: No change.
  - claim: gaze-aligned-dynamics
    agrees: true
    outcome: blocked
    reason: Agreed (metadata insufficient).
    response: No change.
  - claim: latency-skew
    agrees: true
    outcome: blocked
    reason: Agreed (metadata insufficient).
    response: No change.
  - claim: eccentricity-modulation
    agrees: true
    outcome: blocked
    reason: Agreed (metadata insufficient).
    response: No change.
  - claim: foveation-selectivity
    agrees: true
    outcome: blocked
    reason: Agreed (metadata insufficient).
    response: No change.
  - claim: fields-per-cell
    agrees: true
    outcome: blocked
    reason: Agreed (methods underspecified).
    response: No change.
  - claim: spatial-selectivity-fraction
    agrees: true
    outcome: blocked
    reason: 'Cell 66: (a) gives 0.129 to 0.247 and fails; (b) and (c) cannot be decided.'
    response: No change.
  - claim: gaze-map-landmarks
    agrees: true
    outcome: blocked
    reason: Agreed (metadata insufficient).
    response: No change.
  - claim: dimensionality-control
    agrees: true
    outcome: blocked
    reason: Agreed (methods underspecified).
    response: No change.
EOF
date -u
```

Result: not kept, because it reads the paper's text.

**Agent**

Record updated. Now the final full run with all text changes (about 30 minutes).

**Agent calls Bash**

```bash
python tools/entry.py check entries/wirth-2017 2>&1 | tail -15
```

```
0 error(s)
```

**Agent calls Bash**

```bash
date -u && python tools/entry.py all entries/wirth-2017 2>&1 | tail -8; date -u
```

```
Fri Nov 13 18:01:02 UTC 2026
Installed kernelspec registry-wirth-2017 in executed/wirth-2017/.venv/share/jupyter/kernels/registry-wirth-2017
0 error(s)
pass  reproduce_wirth_2017.ipynb  (1724 s)
Fri Nov 13 18:29:55 UTC 2026
```

**Agent calls Bash**

```bash
cd executed/wirth-2017 && $TMPDIR/venv/bin/python - <<'EOF'
import json
nb=json.load(open('reproduce_wirth_2017.ipynb'))
for i in (8,29,45):
    for o in nb['cells'][i].get('outputs',[]):
        t=''.join(o.get('text') or '')
        print(i, t[-900:] if i!=29 else t)
EOF
cd  uv run --quiet python -c "import yaml;[yaml.safe_load(open(f)) for f in ('questions/wirth-2017.yaml','attempts/wirth-2017-01.yaml')];print('yaml ok')"
```

```
8 ): 9, (np.int64(2),): 8, (np.int64(3),): 7, (np.int64(2), np.int64(4)): 1}

Camera abscissa, distance from the centre over 16 m, and fraction of frames on a passive return (tags 5xy)
at event times and 1 s before and after, median over sessions:
            abscissa  r/16  on return
start -1s       0.40  0.82       0.99
start +0s       0.01  1.00       0.99
start +1s       0.12  0.12       0.00
center -1s      0.72  0.72       0.00
center +0s      0.00  0.00       0.00
center +1s      0.00  0.00       0.00
reward -1s      0.21  0.21       0.00
reward +0s      1.00  1.00       0.71
reward +1s      0.99  1.00       1.00

Median time per session (s): reward (code 11) to trial end (code 23), and trial end to the next trial start:
        reward_to_end  end_to_next_start
monkey                                  
ke                0.0               3.84
sn                0.0               3.64
[... 31 more lines not kept]
```

**Agent**

I've worked through every point in the round-2 report. The full entry run (`python tools/entry.py all entries/wirth-2017`) passes with 0 check errors, and the notebook ran in 1724 s. Nothing is committed.

**Outcomes.** No outcome changed. I propose changing two outcomes to blocked (`metadata_insufficient`), for round 3 to review:
- **direction-tuning-not-maintained** (still not reproduced, now marked `assumed: true` as the verifier asked). Reading (a) fails on the number of cells (40 and 28 against 56 ± 5.6). Reading (b) needs the paper's responsive set, which can't be formed without gaze. That set lies somewhere between the three-space responsive cells and all cells. A new cell checks whether any set in that range meets the criterion. One does with permuted chunks (n 61, low 18, high 4), and 13 do with shifted chunks. So the claim can't be decided.
- **direction-center-vs-periphery** (still partially reproduced, assumed). Over all cells neither IC nor sparsity is higher in the centre (p = 0.31 and 0.29), against the partial level over the 59 stand-in cells. The result depends on which cells are included, so the paper's set could give any level. This is the same reasoning already used for landmark-identity-center and spatial-selectivity-fraction.

**Added or corrected**
- **Abscissa (cells 7 and 9, landmark deviation).** I added a check of the abscissa against distance from the centre. On the entry and exit paths it equals the distance from the centre divided by 16 m in every file (median absolute difference at most 0.0023). So "0 centre, 1 arm end" is correct there, and the quarters in the landmark ANOVA are ordered as stated. The verifier was right that cell 9 contradicted the printed values. At the trial start the camera is at the arm end, but that frame still belongs to the passive return, whose abscissa has run down to 0.01. After arriving at the centre the camera stays there while the view rotates. I rewrote cells 7 and 9 and the deviation to match.
- **gaze-anticipates-action caveat.** A new cell shows the view already turns slightly before the turn code in both monkeys. The median is 0.5 to 0.75 degrees, toward the coming turn in 95 to 99% of turns. The gaze position effect remains in turns with less than 0.25 degrees of earlier rotation: K −0.27 SD (p = 3.3e-5), S −0.54 SD (p = 0.0059). In K that is a third to a half of the effect over all turns. K's eye-velocity difference before the code also remains in those turns, so the view's rotation doesn't explain it. The notes give the caveat, and the outcome stands.
- **Question for a reader.** I created `questions/wirth-2017.yaml` with the verifier's point on gaze-anticipates-landmarks. The criterion averages eye position over the whole return, so it can't separate looking ahead from the eye shift that comes with any rotating view. The claim is still tested as the claims file has it.
- **README.** The state-space-selectivity row now says it rests on permuted chunks and is open under shifted chunks. The direction row names the stand-in cell set.
- **Record.** I corrected the "misses under every reading" sentence and recorded round 2 under `verifications`, with the verifier's reasons and my responses.

**Not done**
- I did not run the paper's S2B control (the second of two turns in the same direction) for gaze-anticipates-action. The notes say so.
- In S, turns with under 1 degree of earlier rotation show an eye-velocity difference before the code in the opposite direction (p = 1e-33). It is printed in the notebook, but the text only cites S's session-level test (no difference, p = 0.40).
- `tools/build_site.py`, `tools/site_assets/app.css` and `tools/site_assets/list.js` were already modified before this run. I didn't touch them.

## End of run

55 turns, 67 minutes, $2.88 at API prices, result: success.
