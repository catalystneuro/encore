# sabatini-2024 · author-revise-2 · run 44780045721

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/sabatini-2024/verifier-2-report.md; ls entries/sabatini-2024 transcripts/sabatini-2024 questions
```

```
Fri Nov 20 17:13:42 UTC 2026
I found nothing that changes an outcome, and I agree with all 34. The main points:

- **Finding 1 should be `critical`, not `major`.** The Nitschke file holds five recordings whose clocks overlap. An analysis that selects spikes by trial time would silently mix them.
- **The segment 3 anomaly is still open.** Finding 6's explanation, that the units changed, is contradicted by cell 9.
- **The standard decoders in fig7f-decoder-beats-standard are weak or degenerate.** The `partially_reproduced` label holds by the criterion, but the comparison tests little.
- **The conclusions match the printed numbers,** apart from the small slips listed in section 2.

**1. Outcomes**

The attempt record has 34 outcomes: 11 reproduced, 12 partially reproduced, 11 not reproduced. The claims file has 34 claims. The README's counts match.

I agree with all 34 outcomes. The `assumed: true` outcomes (33; data-composition carries none) rest mainly on trial reading (a), all successful trials. That is stated in every deviation, it is reasonable, and the companion notebook runs reading (b) with the same outcome for every claim. I checked this against the companion's outputs. Claim-specific assumptions:

- **fig7c-standard-encoding-worse:** no kernel penalty. Stated and reasonable; the 0.1 penalty variant still predicts only the mean.
- **fig4c-subspace-excursion-angles:** the noise SEA as chance. Stated, and now compares like with like.
- **tbf-shuffle-control:** the shuffle span. Stated, but no other span was run, and PMd-J's 28.7% against 31.5% may depend on it.
- **fig6e, fig7c-ldr-encoding, suppfig7a:** the scale of the kinematic basis. Stated, and length scales of 1e2 and 1e4 change values by at most 0.002 (cells 97, 104, 106).

Two caveats:
[... 255 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "" docs/protocol.md | sed -n '1,400p'
```

```
1:# Protocol for an attempt
2:
3:Version: `pilot-18`. Record this version in the attempt's provenance.
4:
5:This is what agents, or people, do to attempt a target and deposit the
6:result. A target is a dataset in a public archive and a paper it names. How
7:each archive's datasets are named, versioned and read is in
8:[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9:([pilot notes](pilot-notes.md)); the reasons for the rules are there.
10:
11:An attempt has three roles, each a separate run with a separate context:
12:
13:- The **reader** reads the paper and writes the claims file: every finding,
14:  and how each is to be tested, taken from the paper. A second reader checks
15:  it against the paper. Readers never see the dataset's data.
16:- The **author** tests the claims on the dataset. It reads the paper to
17:  understand the claims, but the claims file binds it: it cannot change a
18:  claim's statement, expected values or criterion. A method detail the file
19:  lacks it takes from the paper, citing the passage, and it asks a reader
20:  only when it believes the file misreads the paper.
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '400,900p' docs/protocol.md
```

```
attempts on a claim then start from the same seed, and each claim's section
  has its own generator, so that adding a cell earlier does not change its
  numbers. Never make a generator without a seed.
- **Say how much the seed matters.** A result that depends on random draws (a
  shuffle or permutation test, a bootstrap, a random split, a random start)
  is computed under the claim's seed and under four more: the seed plus 1000,
  2000, 3000 and 4000. Give the range of the measured value over the five in
  the notes. The outcome is the one under the claim's own seed: the criterion
  is applied as it is written. When the five do not all give that outcome,
  set `seed_sensitive: true` on the outcome (step 5).
- **Put loading and reusable measures in a helper module**, so later notebooks
  on the dataset can import it. Say in its docstring where a parameter comes
  from: the claim's criterion (which cites the paper or its code), the
  passage of the paper it was taken from (author, step 1.6), an assumption
  (say what and why), or a standard choice for a detail that cannot change a
  result (say so).
- **Keep it fast.** Reduce the data to what the analysis needs as it loads.
  Aim for under ten minutes, and keep every notebook under sixty in your own
  run. The verifier's re-run and the pull request's checks allow eighty, as a
  download from the archive can be slower there; that margin is not for
[... 354 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep sabatini; wc -l attempts/sabatini-2024-01.yaml; grep -n "^[a-z_]*:" attempts/sabatini-2024-01.yaml; git diff --stat
```

```
sabatini-2024-01.yaml
1212 attempts/sabatini-2024-01.yaml
1:schema_version: 3
2:id: sabatini-2024-01
3:datasets:
9:paper: doi:10.1038/s41467-024-51308-7
10:date: 2026-11-20
11:entry: sabatini-2024
12:provenance:
23:inputs: []
24:outcomes:
804:findings:
862:verifications:
 tools/build_site.py       | 73 +++++++++++++++++++++++++++++++++++------------
 tools/entry.py            | 11 +++++++
 tools/site_assets/app.css |  2 ++
 3 files changed, 68 insertions(+), 18 deletions(-)
```

**Agent calls Bash**

```bash
sed -n 804,1212p attempts/sabatini-2024-01.yaml
```

```
findings:
- kind: format_error
  about: data
  severity: major
  statement: The Nitschke file (sub-Nitschke_ses-20100923) joins five recording segments whose clocks
    overlap. Trial start times, hand timestamps and every unit's spike times jump backwards four times
    (segments span 5 to 6076 s, 6074 to 12077 s, 6071 to 12494 s, 6120 to 13516 s and 6074 to 6658 s),
    so spike times are not sorted and a trial's spikes cannot be selected by time alone; doing so mixes
    spikes of up to four segments. Splitting each unit's spikes at the jumps and assigning trials to segments
    in file order gives condition decoding of 0.44 to 0.50 in segments 0 to 2 and 0.18 in segment 3 (all
    successful trials; chance 0.014; 0.010 to 0.024 with the previous trial's labels).
- kind: metadata_insufficient
  about: data
  severity: major
  statement: The units table holds 96 units per array, exactly one on each of the 192 electrodes, in both
    files. Its columns are electrode_group, electrodes, id, obs_intervals and spike_times, with no column
    for single or multi-unit, sorting quality or isolation. The paper reports 79 to 118 single and stable
    multi-units per array. Whether these units are threshold crossings or sorted units merged per electrode
    is not stated.
- kind: format_error
[... 389 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "verification\|proposed\|severity" tools/entry.py | head -60; grep -ln "agrees:" attempts/*.yaml | head;
```

```
362:            if version and int(version[1]) >= 18 and about == "data" and not f.get("severity"):
363:                report.error(where, f"finding {n}: it is about the data; give its `severity` (critical, major, minor "
376:            elif its[number - 1].get("severity"):
379:        # A verification round's review of a finding points at the finding by its number in the record.
380:        for r, rnd in enumerate(attempt.get("verifications") or [], 1):
383:                    report.error(where, f"verification round {r} reviews finding {item['finding']}, and the record "
388:        for rnd in (attempt.get("verifications") or [])[1:]:
410:                                    f"verification agreed with {verified!r}; record the change under `proposed`, "
attempts/amjad-2025-01.yaml
attempts/andrews-2024-01.yaml
attempts/armstrong-2026-01.yaml
attempts/asari-2009-01.yaml
attempts/asari-2009-02.yaml
attempts/ashworth-2025-01.yaml
attempts/athalye-2023-01.yaml
attempts/azcorra-2023-01.yaml
attempts/bakalar-2023-01.yaml
attempts/bech-2026-01.yaml
```

**Agent calls Bash**

```bash
sed -n 340,420p tools/entry.py; grep -l "  findings:" attempts/*.yaml | head -3
```

```
import author_notes
            import paper_records
            key = paper_records.key_of_doi(attempt["paper"])
            there = [n["issue"] for n in (author_notes.load(key) if key else []) if str(n["date"]) <= str(attempt.get("date"))]
            named = (attempt.get("provenance") or {}).get("author_notes") or []
            for issue in named:
                if issue not in there:
                    report.error(where, f"`provenance: author_notes` names {issue}, which is not a note in "
                                        f"papers/author-notes/{key}.yaml")
            if there and not named:
                report.error(where, f"the paper's authors had sent notes (papers/author-notes/{key}.yaml) when this "
                                    "attempt was made; list those it used under `provenance: author_notes`")
        for n, f in enumerate(attempt.get("findings") or [], 1):
            if told and f.get("kind") in ("other", "selection_undocumented") and not f.get("about"):
                report.error(where, f"finding {n} ({f.get('kind')}): say what it is about, `about: data` or `about: paper`")
            about = f.get("about") or ("paper" if f.get("kind") in ("methods_unavailable", "code_mismatch",
                                                                   "paper_inconsistency") else "data")
            if told and about == "data" and len(used) > 1 and not f.get("datasets"):
                report.error(where, f"finding {n}: the attempt used {len(used)} datasets; name the ones it is about "
                                    f"(`datasets:`, from {', '.join(used)})")
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n -B2 -A12 "^  findings:" attempts/gao-2018-02.yaml | head -50
```

```
1616-    other papers' recorder transcripts that name docs/pilot-notes/gao-2018-01.md, without its content.
1617-    That run changed no outcome, note, finding or file of the attempt.
1618:  findings:
1619-  - finding: 1
1620-    status: still_present
1621-    now: 1
1622-    note: >-
1623-      Finding 1 reports the same missing data (CN recordings, lick times, behavior-only sessions,
1624-      VGAT-ChR2-EYFP experiments, anatomy) in both datasets. It counts 24 of 46 claims as untestable
1625-      where gao-2018-01 counted 26 of 45, as the claims file now has 46 claims and gao-2018-02 tested
1626-      the ALM half of two Fig. 2 claims.
1627-  - finding: 2
1628-    status: still_present
1629-    now: 14
1630-    note: >-
```

**Agent calls Bash**

```bash
grep -n -A8 "^  findings:" attempts/*.yaml | grep -A8 "agrees" | head -30; grep -rn "findings" docs/schema* schemas 2>/dev/null | head
```

```
attempts/pelot-2020-02.yaml-1327-    agrees: false
attempts/pelot-2020-02.yaml-1328-    severity: critical
attempts/pelot-2020-02.yaml-1329-    reason: I would rate finding 2 critical instead of major. The deposited output metrics file gives pig fascicle diameters
attempts/pelot-2020-02.yaml-1330-      about 1.40 times those measured from the masks and reported in the paper, by a factor that varies from 1.36 to
attempts/pelot-2020-02.yaml-1331-      1.61 per fascicle, so it is not a scale error (cell 6, median ratio 1.4022; cell 7, 1.360 to 1.610). Its pig fascicle
attempts/pelot-2020-02.yaml-1332-      counts are those of the superseded version 1 masks, equal to version 1 in 18 of 18 samples and to version 4 in
attempts/pelot-2020-02.yaml-1333-      only 7 (cell 7). Nothing in the datasets flags this. An analysis that takes the file as given would report pig
--
attempts/pelot-2020-02.yaml:1341:  findings:
schemas/claims.schema.json:87:            "description": "A finding the paper reports (`finding`, the default), or a check the registry adds that the dataset is the data the paper's outside material describes (`link`: the paper's tables, source data, code or deposits). Links are not findings of the paper and are counted apart from them.",
schemas/attempt.schema.json:466:          "findings": {
schemas/attempt.schema.json:478:                  "description": "The finding's number in this record's `findings`, from 1.",
schemas/attempt.schema.json:509:    "findings": {
schemas/attempt.schema.json:572:      "description": "A repeat attempt's comparison with the attempt before it, written by the reconcile step once this attempt, made blind, has been verified (docs/protocol.md, \"Repeat attempts\"). A finding of this attempt that no item of `findings` points at is new.",
schemas/attempt.schema.json:579:        "findings"
schemas/attempt.schema.json:598:        "findings": {
```

**Agent calls Bash**

```bash
sed -n 400,510p schemas/attempt.schema.json; sed -n 1315,1345p attempts/pelot-2020-02.yaml
```

```
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
          },
          "kind": {
            "enum": [
              "agent",
              "person",
[... 122 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la executed/sabatini-2024/ 2>/dev/null; cat entries/sabatini-2024/entry.yaml; cat entries/sabatini-2024/README.md | head -80
```

```
total 1216
drwxr-xr-x 3 runner runner   4096 Nov 20 16:55 .
drwxr-xr-x 3 runner runner   4096 Nov 20 17:13 ..
-rw-r--r-- 1 runner runner    502 Nov 20 16:55 .clean-run.json
drwxr-xr-x 5 runner runner   4096 Nov 20 15:54 .venv
-rw-r--r-- 1 runner runner 623310 Nov 20 16:33 reproduce_sabatini_2024.ipynb
-rw-r--r-- 1 runner runner 596257 Nov 20 16:55 reproduce_sabatini_2024_trials_b.ipynb
-rw-r--r-- 1 runner runner    293 Nov 20 16:55 result.json
schema_version: 1
name: sabatini-2024
type: reproduction
title: Reach-dependent reorientation of rotational dynamics in motor cortex (Sabatini & Kaufman 2024)
description: Tests the findings of Sabatini and Kaufman (2024) on dandiset 000070, which holds the two
  maze-task sessions the paper names (monkeys J and N, a PMd and an M1 Utah array each). It rebuilds the
  four datasets from the units, trials and hand position, and tests jPCA, single-condition dynamics, the
  temporal basis factorization, the alignment and dimensionality of rotational planes, the state space
  location, and LDR encoding and decoding.
license: Apache-2.0
python: "3.13"
notebooks:
[... 40 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/sabatini-2024 && python3 - <<'EOF'
import json
nb=json.load(open('reproduce_sabatini_2024.ipynb'))
print(len(nb['cells']))
for i in [4,5,8,9]:
    c=nb['cells'][i]
    print('=====',i,c['cell_type'],c['metadata'].get('tags'))
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        print('---OUT'); print(''.join(o.get('text',''))[:4000])
EOF
```

```
125
===== 4 markdown None
## Data check
===== 5 code ['sanity']
import resource
for m in ("J", "N"):
    S = SESS[m]
    d = S["all_trials"]
    tr = S["trials"]
    print(f"== monkey {m} (asset {S['info']['asset_id']})")
    print("  trials in file", S["info"]["n_all_trials"], "| successful", int(d["task_success"].sum()),
          "| maze_condition values", len(np.unique(d["maze_condition"])),
          "(min", d["maze_condition"].min(), "max", d["maze_condition"].max(), ")")
    print("  units", len(S["area"]), {a: int((S["area"] == a).sum()) for a in ("M1", "PMd")})
    print("  units table columns:", S["info"]["unit_columns"], "| electrodes table columns:", S["info"]["electrode_columns"])
    print("  electrodes in the file", S["info"]["n_electrodes"], "| units per electrode:",
          np.unique(np.bincount(S["info"]["unit_electrode"], minlength=S["info"]["n_electrodes"]), return_counts=True))
    sp = S["info"]["spikes_per_unit"]
    print("  spikes per unit: min", sp.min(), "median", int(np.median(sp)), "max", sp.max())
    print("  recording segments (backward jumps of hand timestamps + 1):", S["info"]["n_hand_segments"],
[... 111 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && python3 - <<'EOF'
import json
nb=json.load(open('executed/sabatini-2024/reproduce_sabatini_2024.ipynb'))
for i in [0,1,2,3,6,7,10,11,12,13]:
    c=nb['cells'][i]
    print('=====',i,c['cell_type'],c['metadata'].get('tags'))
    print(''.join(c['source'])[:3000])
    for o in c.get('outputs',[]):
        print('---OUT'); print(''.join(o.get('text',''))[:2000])
EOF
wc -l entries/sabatini-2024/ldr.py; grep -n "^def \|segment" entries/sabatini-2024/ldr.py | head -80
```

```
===== 0 markdown None
# Reproducing Sabatini & Kaufman (2024) on DANDI:000070

**Paper.** Sabatini, D. A. & Kaufman, M. T. (2024). Reach-dependent reorientation of rotational dynamics
in motor cortex. *Nature Communications* 15, 7007. doi:10.1038/s41467-024-51308-7. The claims file
(`claims/sabatini-2024.yaml`) was written from the version of record (PMC11325044) with its Methods and
its supplement, and from the paper's code (github.com/kaufmanlab/LDR-public at commit b65f28d).

**Dataset.** DANDI:000070 ("Neural population dynamics during reaching"), version **0.260528.0919**,
streamed. The paper cites the dandiset without a version. Of its three versions (0.251218.1714,
0.260528.0919 and the draft), the two published ones list the same ten assets with the same asset ids,
sizes and modification times, so they hold the same files; the most recent published one is pinned, as
the protocol asks when no version is cited. The two files the paper's Data availability statement
names are read: `sub-Jenkins_ses-20090918` (monkey J) and `sub-Nitschke_ses-20100923` (monkey N).

**What is tested.** The four datasets of the paper (M1-J, PMd-J, M1-N, PMd-N) are rebuilt from the
units, trials and hand position in the two files. The dataset holds no EMG.

| Claim | Tested here |
|---|---|
[... 264 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 30,235p entries/sabatini-2024/ldr.py
```

```
GRID_MS = np.arange(-350, 851, 10)
# Dynamics are fitted from -150 ms on (Methods, Fitting dynamics to single conditions); index 20.
FIT0 = 20
# 1 ms counts are taken over a wider window so that the 20 ms Gaussian has data at the edges
# (standard; the code pads symmetrically).
PAD_MS = 150
WIN0_MS, WIN1_MS = -350 - PAD_MS, 850 + PAD_MS + 1
SMOOTH_SD_MS = 20  # Methods, Subjects, behavior and data pre-processing
WARP_MS = 600  # Methods, Control for stereotyped time course of behavior


def asset_url(path, version=VERSION):
    r = requests.get(f"{API}/dandisets/{DANDISET}/versions/{version}/assets/",
                     params={"path": path}, timeout=60)
    r.raise_for_status()
    hits = [a for a in r.json()["results"] if a["path"] == path]
    assert len(hits) == 1, path
    aid = hits[0]["asset_id"]
    return requests.head(f"{API}/assets/{aid}/download/", allow_redirects=True, timeout=60).url, aid

[... 187 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && date -u && timeout 900 python3 - <<'EOF'
import numpy as np, ldr, time
t0=time.time()
f, aid = ldr.open_nwb("J")
u=f["units"]; sidx=u["spike_times_index"][:]
a0=np.r_[0,sidx[:-1]]
for un in range(len(sidx)):
    s=u["spike_times"][a0[un]:sidx[un]]
    segs=ldr._segments(s)
    if len(segs)>1:
        print("unit",un,"id",u["id"][un],"electrode",u["electrodes"][un],"runs",[(b-a, s[a], s[b-1]) for a,b in segs])
        r1=s[segs[0][0]:segs[0][1]]; r2=s[segs[1][0]:segs[1][1]]
        print("run sizes",len(r1),len(r2))
        # overlap / duplication
        common=np.intersect1d(r1,r2)
        print("identical times shared",len(common))
        # nearest-neighbour distance from r2 to r1
        j=np.clip(np.searchsorted(r1,r2),1,len(r1)-1)
        dmin=np.minimum(np.abs(r2-r1[j-1]),np.abs(r2-r1[j]))
        print("r2 to nearest r1 spike: frac <0.1ms",(dmin<1e-4).mean(),"<1ms",(dmin<1e-3).mean(),"median ms",np.median(dmin)*1e3)
        # ISI of merged
        m=np.sort(s); isi=np.diff(m)
        print("merged ISI <1ms frac",(isi<1e-3).mean(),"run1 ISI<1ms",(np.diff(r1)<1e-3).mean(),"run2",(np.diff(r2)<1e-3).mean())
        # rate over time in 100 s bins
        bins=np.arange(0,15800,500)
        print("run1 counts/500s",np.histogram(r1,bins)[0])
        print("run2 counts/500s",np.histogram(r2,bins)[0])
        # obs intervals
        oi=u["obs_intervals"][:]; oii=u["obs_intervals_index"][:]
        print("obs_intervals rows for unit", oii[un]-(oii[un-1] if un else 0))
        un_=un
# neighbour unit rate for comparison
print("spikes per unit median",np.median(np.diff(np.r_[0,sidx])))
print(time.time()-t0)
EOF
```

```
Exit code 1
Fri Nov 20 17:14:39 UTC 2026
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'numpy'
```

**Agent calls Bash**

```bash
ls executed/sabatini-2024/.venv/bin | head;
```

```
activate
activate.bat
activate.csh
activate.fish
activate.nu
activate.ps1
activate.xsh
activate_this.py
deactivate.bat
debugpy
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && PY=executed/sabatini-2024/.venv/bin/python && timeout 900 $PY - <<'EOF'
import numpy as np, ldr, time
t0=time.time()
f, aid = ldr.open_nwb("J")
u=f["units"]; sidx=u["spike_times_index"][:]
a0=np.r_[0,sidx[:-1]]
for un in [0,1,2]:
    s=u["spike_times"][a0[un]:sidx[un]]
    segs=ldr._segments(s)
    print(un, len(segs))
    if len(segs)>1:
        print("unit",un,"id",u["id"][un],"electrode",u["electrodes"][un],"runs",[(b-a, s[a], s[b-1]) for a,b in segs])
        r1=s[segs[0][0]:segs[0][1]]; r2=s[segs[1][0]:segs[1][1]]
        common=np.intersect1d(r1,r2)
        print("identical times shared",len(common))
        j=np.clip(np.searchsorted(r1,r2),1,len(r1)-1)
        dmin=np.minimum(np.abs(r2-r1[j-1]),np.abs(r2-r1[j]))
        print("r2 to nearest r1 spike: frac <0.1ms",(dmin<1e-4).mean(),"<1ms",(dmin<1e-3).mean(),"median ms",np.median(dmin)*1e3)
        m=np.sort(s); isi=np.diff(m)
        print("merged ISI <1ms frac",(isi<1e-3).mean(),"run1 ISI<1ms",(np.diff(r1)<1e-3).mean(),"run2",(np.diff(r2)<1e-3).mean())
        bins=np.arange(0,16001,1000)
        print("run1 counts/1000s",np.histogram(r1,bins)[0])
        print("run2 counts/1000s",np.histogram(r2,bins)[0])
        oii=u["obs_intervals_index"][:]
        print("obs_intervals rows", oii[:4])
print("spikes per unit", np.diff(np.r_[0,sidx])[:4])
print(time.time()-t0)
EOF
```

```
0 1
1 2
unit 1 id 1 electrode 1 runs [(np.int64(196608), np.float64(4259.096533333333), np.float64(15668.638358580109)), (np.int64(264946), np.float64(4.716733333333334), np.float64(15668.614558580108))]
identical times shared 1049
r2 to nearest r1 spike: frac <0.1ms 0.011779758894265246 <1ms 0.061642749843364306 median ms 18.433333332723123
merged ISI <1ms frac 0.03543255054132462 run1 ISI<1ms 0.0 run2 0.0
run1 counts/1000s [    0     0     0     0 13032 16429 16246 16975 19529 16562 16943 16522
 17754 19402 16129 11085]
run2 counts/1000s [18393 16597 16989 15818 17227 15951 15820 16078 18720 15975 15694 15642
 17520 18915 17108 12499]
obs_intervals rows [ 2636  5272  7908 10544]
2 1
spikes per unit [ 61030 461554 541656 301613]
2.7452869415283203
```

**Agent calls Bash**

```bash
PY=executed/sabatini-2024/.venv/bin/python && date -u && timeout 1200 $PY - <<'EOF'
import numpy as np, ldr, time
t0=time.time()
f, aid = ldr.open_nwb("J")
u=f["units"]; sidx=u["spike_times_index"][:]
a0=np.r_[0,sidx[:-1]]
s1=u["spike_times"][a0[1]:sidx[1]]
r1=s1[:196608]; r2=s1[196608:]
for un in range(len(sidx)):
    if un==1: continue
    s=u["spike_times"][a0[un]:sidx[un]]
    k=np.isin(r1, s).mean(); k2=np.isin(r2,s).mean()
    if k>0.05 or k2>0.05:
        print("unit",un,"electrode",u["electrodes"][un],"spikes",len(s),"frac run1 in it",k,"frac run2 in it",k2, "range", s[0], s[-1])
print("done",time.time()-t0)
EOF
```

```
Fri Nov 20 17:15:01 UTC 2026
unit 18 electrode 18 spikes 162414 frac run1 in it 0.074859619140625 frac run2 in it 0.0030798728797566295 range 4.7209666666666665 15668.639158580107
unit 32 electrode 32 spikes 232859 frac run1 in it 0.2643025716145833 frac run2 in it 0.0034459852196296603 range 4.889233333333333 15668.648625246775
unit 33 electrode 33 spikes 226821 frac run1 in it 0.2895100911458333 frac run2 in it 0.0032195239784710847 range 4.7138 15668.648625246775
unit 68 electrode 68 spikes 587407 frac run1 in it 0.3741048177083333 frac run2 in it 0.00838661463090592 range 4.7138 15668.639558580107
unit 73 electrode 73 spikes 255618 frac run1 in it 0.2779998779296875 frac run2 in it 0.003721513063039261 range 4.847366666666667 15668.64079191344
unit 84 electrode 84 spikes 227498 frac run1 in it 0.2786458333333333 frac run2 in it 0.0031553599601428215 range 4.722 15668.640758580108
unit 85 electrode 85 spikes 182227 frac run1 in it 0.1143798828125 frac run2 in it 0.0027892476202697907 range 4.8962 15668.634258580107
done 19.075002193450928
```

**Agent calls Bash**

```bash
PY=executed/sabatini-2024/.venv/bin/python && date -u && timeout 1200 $PY - <<'EOF'
import numpy as np, ldr, time, os
t0=time.time()
S=ldr.load_session("N")
tr=S["trials"]
np.savez(os.environ["TMPDIR"]+"/N.npz", R=S["R"], C10=S["C10"], area=S["area"], **{"tr_"+k:v for k,v in tr.items() if np.asarray(v).dtype!=object})
print("saved", time.time()-t0)
EOF
```

```
Fri Nov 20 17:15:42 UTC 2026
saved 81.72762036323547
```

**Agent calls Bash**

```bash
PY=executed/sabatini-2024/.venv/bin/python && $PY - <<'EOF'
import numpy as np, ldr, os
Z=np.load(os.environ["TMPDIR"]+"/N.npz")
R=Z["R"]; seg=Z["tr_segment"]; mc=Z["tr_maze_condition"]; st=Z["tr_start_time"]
tr={k[3:]:Z[k] for k in Z.files if k.startswith("tr_")}
ct=ldr.condition_table(tr); cond=ct["cond"]
gi=(ldr.GRID_MS>=-100)&(ldr.GRID_MS<=300)
F=R[:,:,gi].mean(2)
tot=F.sum(1)
for s in range(5):
    m=seg==s
    print(s, m.sum(), "pop rate pct", np.round(np.percentile(tot[m],[0,5,25,50,75,95,100]),0), "conds", len(np.unique(cond[m])), "trials/cond", np.bincount(np.bincount(cond[m],minlength=72)))
# per unit mean rate by segment, correlation
mu=np.array([F[seg==s].mean(0) for s in range(5)])
print("corr of unit mean rates between segments\n", np.round(np.corrcoef(mu),3))
# within segment 3: order in time
i3=np.where(seg==3)[0]
print("seg3 start times range", st[i3].min(), st[i3].max())
# rolling pop rate over seg3 in blocks of 50
for b in range(0,len(i3),50):
    print(b, np.round(tot[i3[b:b+50]].mean(),0), np.round(st[i3[b]],0))
EOF
```

```
0 534 pop rate pct [ 7517.  8871.  9677. 10242. 10759. 11675. 14651.] conds 72 trials/cond [ 0  0  0  0  0  8 21 14 13  5  6  1  2  2]
1 510 pop rate pct [ 8180.  9310. 10052. 10592. 11045. 12036. 14042.] conds 72 trials/cond [ 0  0  0  0  4  9 16 19  8  8  7  0  0  0  1]
2 521 pop rate pct [ 8190.  9631. 10195. 10678. 11214. 12596. 14627.] conds 72 trials/cond [ 0  0  0  0  1  6 16 19 21  4  3  0  2]
3 532 pop rate pct [ 8168.  9431. 10211. 10794. 11309. 12270. 14008.] conds 72 trials/cond [ 0  0  0  0  0  7 16 17 16 10  3  2  1]
4 24 pop rate pct [ 9193.  9354. 10059. 10606. 11105. 11636. 12063.] conds 23 trials/cond [49 22  1]
corr of unit mean rates between segments
 [[1.    0.979 0.913 0.806 0.854]
 [0.979 1.    0.957 0.832 0.902]
 [0.913 0.957 1.    0.879 0.952]
 [0.806 0.832 0.879 1.    0.884]
 [0.854 0.902 0.952 0.884 1.   ]]
seg3 start times range 6119.761116729867 13506.435550063201
0 11236.0 6120.0
50 11214.0 7225.0
100 11202.0 7914.0
150 10953.0 8489.0
200 10780.0 9006.0
250 10607.0 9723.0
300 10547.0 10311.0
350 10313.0 10975.0
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
PY=executed/sabatini-2024/.venv/bin/python && $PY - <<'EOF'
import numpy as np, ldr, os
Z=np.load(os.environ["TMPDIR"]+"/N.npz")
R=Z["R"]; seg=Z["tr_segment"]; area=Z["area"]
tr={k[3:]:Z[k] for k in Z.files if k.startswith("tr_")}
cond=ldr.condition_table(tr)["cond"]
gi=(ldr.GRID_MS>=-100)&(ldr.GRID_MS<=300)
F=R[:,:,gi].mean(2)
sd=np.array([F[seg==s].std(0) for s in range(4)])
mu=np.array([F[seg==s].mean(0) for s in range(4)])
ratio=sd[3]/np.median(sd[:3],0)
o=np.argsort(-ratio)[:12]
print("units with largest sd ratio seg3/others:")
for u in o: print(u, area[u], "sd by seg",np.round(sd[:,u],1),"mean",np.round(mu[:,u],1), "max seg3", np.round(F[seg==3,u].max(),1))
# decoding within seg3 dropping top units
def loo(X,lab):
    hits=0
    for q in range(len(lab)):
        o=np.ones(len(lab),bool);o[q]=False
        cs=np.unique(lab[o]); cen=np.array([X[o&(lab==c)].mean(0) for c in cs])
        hits+=cs[np.argmin(((cen-X[q])**2).sum(1))]==lab[q]
    return hits/len(lab)
i3=seg==3
for drop in [0,1,2,3,5,10]:
    keep=np.setdiff1d(np.arange(F.shape[1]),np.argsort(-ratio)[:drop])
    print("drop",drop,"seg3 within",round(loo(F[i3][:,keep],cond[i3]),3),"seg0 within",round(loo(F[seg==0][:,keep],cond[seg==0]),3))
EOF
```

```
units with largest sd ratio seg3/others:
170 M1 sd by seg [ 11.5   8.7   8.7 171.8] mean [ 39.8  28.7  27.8 175.6] max seg3 428.4
82 PMd sd by seg [ 9.6 11.6 12.4 22.1] mean [27.7 31.8 34.1 38.4] max seg3 162.7
187 M1 sd by seg [17.6 18.1 22.  23.8] mean [ 76.2  82.4  97.  108.3] max seg3 193.3
116 M1 sd by seg [ 9.8 10.2 11.  12.2] mean [34.1 35.2 37.1 39.9] max seg3 90.2
71 PMd sd by seg [11.  11.4 12.8 13.7] mean [41.5 44.1 49.1 48.1] max seg3 97.5
97 M1 sd by seg [14.2 13.2 15.1 16.8] mean [48.5 44.5 48.8 52.4] max seg3 107.4
76 PMd sd by seg [15.1 15.3 16.8 18.1] mean [62.8 66.1 71.1 74.9] max seg3 129.0
105 M1 sd by seg [12.8 12.  14.  15. ] mean [47.3 54.  57.9 60.2] max seg3 104.4
93 PMd sd by seg [12.8 13.7 16.3 16.1] mean [34.5 35.8 60.4 43.8] max seg3 102.7
60 PMd sd by seg [17.3 17.4 18.3 20.3] mean [57.5 53.5 59.4 62.5] max seg3 128.8
42 PMd sd by seg [22.7 24.6 29.9 28. ] mean [59.2 65.  79.2 80.6] max seg3 198.3
180 M1 sd by seg [25.1 23.9 24.3 27.6] mean [118.5 122.7 125.5 124.8] max seg3 204.0
drop 0 seg3 within 0.179 seg0 within 0.442
drop 1 seg3 within 0.425 seg0 within 0.448
drop 2 seg3 within 0.429 seg0 within 0.448
drop 3 seg3 within 0.423 seg0 within 0.448
drop 5 seg3 within 0.427 seg0 within 0.449
drop 10 seg3 within 0.429 seg0 within 0.449
```

**Agent calls Bash**

```bash
PY=executed/sabatini-2024/.venv/bin/python && $PY - <<'EOF'
import numpy as np, ldr, os
Z=np.load(os.environ["TMPDIR"]+"/N.npz")
R=Z["R"]; seg=Z["tr_segment"]; st=Z["tr_start_time"]
F=R[:,170].mean(1)
for s in range(5):
    x=F[seg==s]; print(s, np.round(np.percentile(x,[0,10,25,50,75,90,100]),1), "trials >100:", (x>100).sum(), "of", len(x))
i3=np.where(seg==3)[0]
print([ (round(st[i]), round(F[i])) for i in i3[::20]])
EOF
```

```
0 [ 7.6 29.9 34.6 39.9 46.  51.  68.2] trials >100: 0 of 534
1 [11.4 20.7 24.  27.6 31.4 34.8 46.2] trials >100: 0 of 510
2 [13.2 20.4 23.7 27.3 31.5 34.8 45.2] trials >100: 0 of 521
3 [ 13.4  22.   27.4  40.1 388.1 397.4 414.7] trials >100: 229 of 532
4 [18.3 22.4 26.2 30.3 33.4 39.7 44.1] trials >100: 0 of 24
[(6120, 36), (6522, 365), (7054, 387), (7362, 403), (7687, 396), (7914, 395), (8150, 390), (8371, 399), (8582, 392), (8821, 399), (9006, 383), (9274, 174), (9646, 21), (9846, 76), (10091, 26), (10311, 23), (10577, 47), (10852, 19), (11092, 25), (11361, 20), (11648, 26), (11980, 26), (12281, 22), (12563, 16), (12810, 35), (13085, 20), (13360, 26)]
```

**Agent calls Bash**

```bash
ls paper/; grep -n -i "stable\|isolat\|sorted\|multi-unit\|multiunit" paper/*.txt paper/*.md 2>/dev/null | head -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -o -i ".\{300\}stable multi.\{300\}\|.\{200\}single and.\{200\}" paper/10.1038-s41467-024-51308-7.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
PY=executed/sabatini-2024/.venv/bin/python && $PY - <<'EOF'
import numpy as np, os
Z=np.load(os.environ["TMPDIR"]+"/N.npz")
R=Z["R"]; st=Z["tr_start_time"]; seg=Z["tr_segment"]
F=R.mean(2)  # trial mean rate per unit
o=np.lexsort((st,seg))  # file order is trial order already; use index order
F=F  # index order = file order
nb=len(F)//50
B=np.array([F[i*50:(i+1)*50].mean(0) for i in range(nb)])
ratio=B.max(0)/np.median(B,0)
print(np.round(np.sort(ratio)[::-1][:8],2), np.argsort(-ratio)[:5])
EOF
```

```
[13.69  2.53  1.99  1.95  1.94  1.9   1.61  1.54] [170  32 185 160   7]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
a=json.load(open('reproduce_sabatini_2024.ipynb'));b=json.load(open('reproduce_sabatini_2024_trials_b.ipynb'))
print(len(a['cells']),len(b['cells']))
import difflib
sa=[''.join(c['source']) for c in a['cells']]; sb=[''.join(c['source']) for c in b['cells']]
for i,(x,y) in enumerate(zip(sa,sb)):
    if x!=y: print("differs cell",i, x[:200].replace("\n"," | "), "\n   VS", y[:200].replace("\n"," | "))
for i,x in enumerate(sa):
    if '"area"' in x or "area" in x and "==" in x: print("area use cell",i)
EOF
grep -rn "trials_b" tools/*.py | head
```

```
<persisted-output>
Output too large (33.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/d37cd774-5469-44e5-90b7-4a671c8b07c9/tool-results/bz6535o5p.txt

Preview (first 2KB):
125 91
differs cell 0 # Reproducing Sabatini & Kaufman (2024) on DANDI:000070 |  | **Paper.** Sabatini, D. A. & Kaufman, M. T. (2024). Reach-dependent reorientation of rotational dynamics | in motor cortex. *Nature Communication 
   VS # Sabatini & Kaufman (2024) on DANDI:000070: trial reading (b) |  | This notebook is `reproduce_sabatini_2024.ipynb` with two parameters changed in its first code cell: `READING = "b"` (successful trials 
differs cell 1 import os | for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): |     os.environ[_v] = "1"  # many small fits, some in parallel worker processes (protocol) | import time | import zlib | im 
   VS import os | for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): |     os.environ[_v] = "1"  # many small fits, some in parallel worker processes (protocol) | import time | import zlib | im
differs cell 14 **Result: reproduced.** Both monkeys have the 72 conditions (36 straight, 36 curved), and the trial counts are within 10% of the paper's under both readings (J 1595 or 1381 against 1469; N 2121 or 188 
   VS ## Single-condition LDSs: fig2c-condition-lds-variance |  | > Activity on each single condition was low-dimensional and approximated by an LDS of 5 to 9 dimensions, | > which explained 71 to 93% of the popu
differs cell 15 ## Single-condition LDSs: fig2c-condition-lds-variance |  | > Activity on each single condition was low-dimensional and approximated by an LDS of 5 to 9 dimensions, | > which explained 71 to 93% of the popu 
   VS KS = list(range(1, 22, 2)) |  |  | def dim_job(args): |     ds, sd, frac, folds = args |     cv = ldr.cv_condition_dim(D[ds]["R"], D[ds]["cond"], 72, np.random.default_rng(sd), KS, folds=folds, mask=MASK[ds[0]]
differs cell 16 KS = list(r
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
a=json.load(open('reproduce_sabatini_2024.ipynb'));b=json.load(open('reproduce_sabatini_2024_trials_b.ipynb'))
sa=[''.join(c['source']) for c in a['cells']]; sb=set(''.join(c['source']) for c in b['cells'])
print("main cells not in b:",[ (i, sa[i][:40]) for i in range(len(sa)) if sa[i] not in sb])
for i,x in enumerate(sa):
    for ln in x.split("\n"):
        if "area" in ln and a['cells'][i]['cell_type']=='code': print(i, ln.strip()[:150])
print(''.join(b['cells'][0]['source'])); print(''.join(b['cells'][1]['source'])[-600:])
EOF
```

```
main cells not in b: [(0, '# Reproducing Sabatini & Kaufman (2024) '), (1, 'import os\nfor _v in ("OMP_NUM_THREADS", '), (14, '**Result: reproduced.** Both monkeys hav'), (17, '**Result: reproduced.** The cross-valida'), (20, '**Result: not reproduced.** Every condit'), (24, '**Result: not reproduced.** The AUC betw'), (27, '**Result: not reproduced.** The cross-va'), (30, '**Result: reproduced.** The factorizatio'), (34, '**Result: partially reproduced.** Shuffl'), (36, '**Result: partially reproduced.** Recove'), (39, '**Result: not reproduced.** Before warpi'), (42, '**Result: not reproduced.** One LDS fitt'), (47, '**Result: reproduced.** For every rotati'), (50, '**Result: partially reproduced.** The st'), (54, '**Result: partially reproduced.** The nu'), (58, '**Result: not reproduced.** Rotation ori'), (60, '**Result: not reproduced.** SEA finds 1 '), (64, '**Result: reproduced.** Under reading (a'), (66, '**Result: reproduced.** In every dataset'), (70, '**Result: reproduced.** Each rotation pr'), (72, '**Result: reproduced.** The state space '), (75, '**Result: partially reproduced.** With P'), (80, '**Result: partially reproduced.** With t'), (83, '**Result: partially reproduced.** The re'), (86, '**Result: not reproduced.** Under the ma'), (90, '**Result: not reproduced.** Rotational v'), (92, '**Result: partially reproduced.** The al'), (98, '**Result: reproduced.** With the SVD kin'), (101, '**Result: not reproduced.** Reach parame'), (105, '**Result: reproduced.** Linear LDR encod'), (107, '**Result: partially reproduced.** With t'), (111, '**Result: reproduced.** Both LDR models '), (115, '**Result: partially reproduced.** The LD'), (117, '**Result: partially reproduced.** Decode'), (119, '**Result: not reproduced.** Removing the'), (123, '**Result: partially reproduced.** The LD'), (124, '## Summary\n\n| Claim | Outcome |\n|---|---')]
5 print("  units", len(S["area"]), {a: int((S["area"] == a).sum()) for a in ("M1", "PMd")})
11 m, area = ds
11 u = S[
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
grep -o -i "Control for data smoothing.\{1500\}" paper/10.1038-s41467-024-51308-7.txt | head -3; grep -n "tbf-shuffle-control" -A40 claims/sabatini-2024.yaml | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
curl -sL --max-time 30 https://raw.githubusercontent.com/kaufmanlab/LDR-public/b65f28d/ 2>&1 | head -5; curl -sL --max-time 30 "https://api.github.com/repos/kaufmanlab/LDR-public/git/trees/b65f28d?recursive=1" | grep -i '"path"' | grep -i "scramble\|jpca\|preprocess\|load" | head -20
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -sL --max-time 30 https://raw.githubusercontent.com/kaufmanlab/LDR-public/b65f28d/utils/TBFandCondSpecificDynamics/scrambleTrials.m; echo ======; curl -sL --max-time 30 https://raw.githubusercontent.com/kaufmanlab/LDR-public/b65f28d/utils/crossvalidation/preprocessTrials.m | head -80; curl -sL --max-time 30 "https://api.github.com/repos/kaufmanlab/LDR-public/git/trees/b65f28d?recursive=1" | grep '"path"' | grep -i scramble
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
nb=json.load(open('executed/sabatini-2024/reproduce_sabatini_2024.ipynb'))
for i in range(31,37):
    c=nb['cells'][i]
    print('=====',i,c['cell_type'],c['metadata'].get('tags'))
    print(''.join(c['source']))
    for o in c.get('outputs',[]):
        print('---OUT'); print(''.join(o.get('text',''))[:3000])
EOF
```

```
===== 31 markdown None
## tbf-shuffle-control and fig3h-recoverability

Shuffled data: the 1 ms bins of each trial permuted in time (one permutation for all units of a trial)
before smoothing and averaging, then TBF with the dataset's k. The span permuted is the 1.5 s window
read around movement onset (assumption; the paper does not give it). Recoverability per condition: the
variance of the basis functions explained by pinv(L(c)) X(c) (Methods, Eq. 6), on the de-mixed basis.
Chance is the same measure on the shuffled data, with the shuffled basis de-mixed in the same way; the
raw shuffled basis is shown as a variant.
===== 32 code None
def recoverability(L, B, Xw):
    out = []
    for c in range(len(L)):
        Bh = np.linalg.pinv(L[c]) @ Xw[c]
        out.append(ldr.pop_ve(B, Bh))
    return np.array(out)


SH = {}
for ds in DATASETS:
[... 52 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json,re
a=json.load(open('reproduce_sabatini_2024.ipynb'))
for i,c in enumerate(a['cells']):
    if c['cell_type']!='code': continue
    for ln in ''.join(c['source']).split("\n"):
        if re.search(r'SESS\[|\bS\["|\["u"\]|\bu\b', ln): print(i, ln.strip()[:160])
EOF
```

```
3 SESS[m] = ldr.load_session(m, shuffle_seeds=seeds5("tbf-shuffle-control"))
3 len(SESS[m]["trials"]["maze_condition"]))
5 S = SESS[m]
5 d = S["all_trials"]
5 tr = S["trials"]
5 print("  trials in file", S["info"]["n_all_trials"], "| successful", int(d["task_success"].sum()),
5 print("  units", len(S["area"]), {a: int((S["area"] == a).sum()) for a in ("M1", "PMd")})
5 print("  units table columns:", S["info"]["unit_columns"], "| electrodes table columns:", S["info"]["electrode_columns"])
5 print("  electrodes in the file", S["info"]["n_electrodes"], "| units per electrode:",
5 np.unique(np.bincount(S["info"]["unit_electrode"], minlength=S["info"]["n_electrodes"]), return_counts=True))
5 sp = S["info"]["spikes_per_unit"]
5 print("  recording segments (backward jumps of hand timestamps + 1):", S["info"]["n_hand_segments"],
5 "| bounds (s):", [(round(a, 1), round(b, 1)) for a, b in S["info"]["hand_segment_bounds"]])
5 print("  backward jumps in spike times per unit:", np.bincount(S["info"]["unit_jumps"]))
5 print("  -500..+1000 ms window inside the trial interval for", int(S["info"]["ok_window"].sum()), "of",
5 len(S["info"]["ok_window"]), "kept trials")
5 h = S["hand"]
5 print("  smoothed rates (spikes/s): range", float(S["R"].min()), float(S["R"].max()), "mean", float(S["R"].mean()))
7 d = SESS[m]["all_trials"]
7 tr = SESS[m]["trials"]
[... 20 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; sed -n 1,29p ldr.py; grep -n "def pop_ve" -A12 ldr.py
```

```
Fri Nov 20 17:19:25 UTC 2026
"""Loading and measures for testing Sabatini & Kaufman (2024) on DANDI:000070.

Where each parameter comes from is said beside it:
- "claims": the claim's criterion in claims/sabatini-2024.yaml (which cites the paper or its code);
- "Methods, <section>": a passage of the paper taken by the author (protocol, author step 1.6);
- "assumption": a choice the paper leaves open, recorded as a deviation in the attempt;
- "standard": a choice that cannot change a result (a padding margin, a plotting detail).

The dandiset is read by streaming (remfile + h5py); nothing is written to disk.
"""

from __future__ import annotations

import numpy as np
import h5py
import remfile
import requests
from scipy.ndimage import gaussian_filter1d

[... 24 more lines not kept]
```

**Agent**

Now the helper edits: the code's shuffle span, a report on a restarted spike train, and a stability check.

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/sabatini-2024/ldr.py",
 "old_string": "def load_session(monkey, shuffle_seeds=(), progress=False):",
 "new_string": "def load_session(monkey, shuffle_seeds=(), shuffle_window_seeds=(), progress=False):"
}
```

```
The file entries/sabatini-2024/ldr.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/sabatini-2024/ldr.py",
 "old_string": "          smoothing (tbf-shuffle-control), one array per seed;\n      RW  as R,",
 "new_string": "          smoothing (tbf-shuffle-control), one array per seed;\n      RSW {seed: array} as RS, with only the 1201 bins of the analysis window (-350 to +850 ms)\n          permuted and smoothed with symmetric padding at its edges: the span of the paper's code,\n          which permutes all columns of a trial's 1 ms matrix (scrambleTrials.m) and then smooths\n          with symmetric padding and keeps every tenth column of the same matrix (preprocessTrials.m),\n          so that the matrix spans the analysis window;\n      RW  as R,"
}
```

```
The file entries/sabatini-2024/ldr.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/sabatini-2024/ldr.py",
 "old_string": "    RS = {sd: np.zeros_like(R) for sd in shuffle_seeds}\n    rngs = {sd: np.random.default_rng(sd) for sd in shuffle_seeds}",
 "new_string": "    RS = {sd: np.zeros_like(R) for sd in shuffle_seeds}\n    rngs = {sd: np.random.default_rng(sd) for sd in shuffle_seeds}\n    RSW = {sd: np.zeros_like(R) for sd in shuffle_window_seeds}\n    rngs_w = {sd: np.random.default_rng(sd) for sd in shuffle_window_seeds}\n    aw = slice(gi[0], gi[-1] + 1)  # the 1201 bins of -350..+850 ms"
}
```

```
The file entries/sabatini-2024/ldr.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/sabatini-2024/ldr.py",
 "old_string": "            RS[sd][i] = gaussian_filter1d(cs, SMOOTH_SD_MS, axis=1, mode=\"reflect\")[:, gi] * 1000\n",
 "new_string": "            RS[sd][i] = gaussian_filter1d(cs, SMOOTH_SD_MS, axis=1, mode=\"reflect\")[:, gi] * 1000\n        for sd in shuffle_window_seeds:\n            cw = c[:, aw]\n            cw = cw[:, rngs_w[sd].permutation(cw.shape[1])]\n            RSW[sd][i] = gaussian_filter1d(cw, SMOOTH_SD_MS, axis=1, mode=\"reflect\")[:, ::10] * 1000\n"
}
```

```
The file entries/sabatini-2024/ldr.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/sabatini-2024/ldr.py",
 "old_string": "    return dict(trials=tr, all_trials=d, R=R, RS=RS, RW=RW,",
 "new_string": "    return dict(trials=tr, all_trials=d, R=R, RS=RS, RSW=RSW, RW=RW,"
}
```

```
The file entries/sabatini-2024/ldr.py has been updated successfully.
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/sabatini-2024/ldr.py",
 "old_string": "def reach_duration(hand):",
 "new_string": "def spike_run_report(monkey, unit):\n    \"\"\"The runs of one unit whose spike train restarts: for each run its size and first and last\n    time, the spike times the runs share, the fraction of the merged train's intervals under 1 ms\n    (and of each run's), and for each run the largest fraction of its times found exactly in another\n    unit's train, with that unit.\"\"\"\n    f, _ = open_nwb(monkey)\n    u = f[\"units\"]\n    sidx = u[\"spike_times_index\"][:]\n    a0 = np.r_[0, sidx[:-1]]\n    s = u[\"spike_times\"][a0[unit]:sidx[unit]]\n    runs = [s[a:b] for a, b in _segments(s)]\n    out = dict(runs=[(len(r), float(r[0]), float(r[-1])) for r in runs],\n               shared=len(np.intersect1d(runs[0], runs[1])) if len(runs) > 1 else 0,\n               isi_below_1ms_merged=float((np.diff(np.sort(s)) < 1e-3).mean()),\n               isi_below_1ms_runs=[float((np.diff(r) < 1e-3).mean()) for r in runs])\n    best = [(0.0, -1)] * len(runs)\n    for other in range(len(sidx)):\n        if other == unit:\n            continue\n        so = u[\"spike_times\"][a0[other]:sidx[other]]\n        best = [max(b, (float(np.isin(r, so).mean()), other)) for b, r in zip(best, runs)]\n    f.close()\n    out[\"most_shared_with_other_unit\"] = best\n    return out\n\n\ndef block_rate_ratio(R, block=50):\n    \"\"\"Per unit: the largest mean rate over blocks of `block` successive trials (file order) divided\n    by the median block mean. A stable unit stays near 1. The paper used 'single-units and stable\n    multi-units' (Methods, Subjects, behavior and data pre-processing) without a rule; the block size\n    is a standard choice, and the notebook shows the ratios so that any threshold can be read off.\"\"\"\n    F = R.mean(2)\n    nb = len(F) // block\n    B = np.array([F[i * block:(i + 1) * block].mean(0) for i in range(nb)])\n    return B.max(0) / np.median(B, 0)\n\n\ndef reach_duration(hand):"
}
```

```
The file entries/sabatini-2024/ldr.py has been updated successfully.
```

**Agent calls Bash**

```bash
PY=executed/sabatini-2024/.venv/bin/python && $PY - <<'EOF'
import numpy as np, ldr, os, time
t=time.time()
print(ldr.spike_run_report("J",1), time.time()-t)
Z=np.load(os.environ["TMPDIR"]+"/N.npz")
r=ldr.block_rate_ratio(Z["R"]); print(np.round(np.sort(r)[::-1][:4],2), np.argsort(-r)[:3])
EOF
```

```
{'runs': [(196608, 4259.096533333333, 15668.638358580109), (264946, 4.716733333333334, 15668.614558580108)], 'shared': 1049, 'isi_below_1ms_merged': 0.03543255054132462, 'isi_below_1ms_runs': [0.0, 0.0], 'most_shared_with_other_unit': [(0.3741048177083333, 68), (0.02535988465574117, 64)]} 20.68077254295349
[13.69  2.53  1.99  1.95] [170  32 185]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json,re
a=json.load(open('reproduce_sabatini_2024.ipynb'))
for i,c in enumerate(a['cells']):
    s=''.join(c['source'])
    for kw in ["segment 3","merged","88.7","change of","units changed","restart","1.6 to 2.4","all 20 rotation"]:
        for m in re.finditer(re.escape(kw), s):
            print(i, kw, "::", s[max(0,m.start()-300):m.end()+300].replace("\n"," "))
            print()
EOF
```

```
64 all 20 rotation :: **Result: reproduced.** Under reading (a), same-frequency alignment is higher than different-frequency alignment for all 20 rotation comparisons: the one-sided signed-rank test gives p at most 1.4e-12 and the Hodges-Lehmann estimate of the paired difference is positive in every comparison (+0.011 to +0.558). For M1-N 3.24 Hz onto the other two rotations the effect is small: the medians of the two distributions are 0.183 against 

98 88.7 :: **Result: reproduced.** With the SVD kinematic basis (reading a), the four reach parameters linearly predict 55.5, 55.5, 70.5 and 41.5% of the variance of the location (within 33.3 to 78.1%), and OU kernel regression 73.0, 68.5, 88.7 and 77.9% (within 62.1 to 89.1%), both above all 1000 permutations. The four other seeds stay in range (OU 65.5 to 88.7%, linear 38.4 to 70.1%). The skew-normal basis (reading b) gives linear 41.6 to 70.5% and OU 69.3 to 89.1%. OU length scales of 1e2 and 1e4 change the kernel values by at most 0.0

98 88.7 :: sis (reading a), the four reach parameters linearly predict 55.5, 55.5, 70.5 and 41.5% of the variance of the location (within 33.3 to 78.1%), and OU kernel regression 73.0, 68.5, 88.7 and 77.9% (within 62.1 to 89.1%), both above all 1000 permutations. The four other seeds stay in range (OU 65.5 to 88.7%, linear 38.4 to 70.1%). The skew-normal basis (reading b) gives linear 41.6 to 70.5% and OU 69.3 to 89.1%. OU length scales of 1e2 and 1e4 change the kernel values by at most 0.002. The Gaussian kernel (reading b of the kernel) gives 32 to 55%, below the range.

124 segment 3 :: trial's spikes cannot be found by time alone. Assigning each trial to its segment in file order gives condition decoding well above chance in segments 0 to 3 and at chance with the previous trial's labels, so the alignment within segments is consistent with the trial table; condition information in segment 3 is lower within the segment (0.18) than in segments 0 to 2 (0.44 to 0.50), while a decoder 
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
nb=json.load(open('executed/sabatini-2024/reproduce_sabatini_2024.ipynb'))
for i in [18,19,20,63,64,97,98,124]:
    c=nb['cells'][i]
    print('=====',i,c['cell_type'],c['metadata'].get('tags'))
    if c['cell_type']=='markdown' or i in(18,): print(''.join(c['source']))
    for o in c.get('outputs',[]):
        print('---OUT'); print(''.join(o.get('text',''))[:3500])
EOF
```

```
===== 18 markdown None
## fig3a-eigenvalue-clusters

> Eigenvalues of the single-condition LDSs formed distinct clusters, corresponding to rotations at about
> 0.5, 1.5, 2.5 and 4 Hz on every condition, along with an offset.
===== 19 code ['claim:fig3a-eigenvalue-clusters']
---OUT
M1-J: k=5; complex pairs per condition [ 0  0 72] ; real eigenvalues per condition [ 0 72] ; conditions with >=1 real: 72/72
   median frequency of pair rank 1..2 (Hz): [0.86 2.38] (conditions: [72, 72]); within 10% of 0.5,1.5,2.5,4: [np.False_, np.False_]
   all eigenvalue frequencies: range 0.00-2.91 Hz; |eigenvalue| range 0.958-0.999
   points outside the axes: 0
PMd-J: k=5; complex pairs per condition [ 0  0 72] ; real eigenvalues per condition [ 0 72] ; conditions with >=1 real: 72/72
   median frequency of pair rank 1..2 (Hz): [0.56 1.55] (conditions: [72, 72]); within 10% of 0.5,1.5,2.5,4: [np.False_, np.True_]
   all eigenvalue frequencies: range 0.00-2.13 Hz; |eigenvalue| range 0.951-0.999
   points outside the axes: 0
M1-N: k=7; complex pairs per condition [ 0  0  1 71] ; real eigenvalues per condition [ 0 71  0  1] ; conditions with >=1 real: 72/72
   median frequency of pair rank 1..3 (Hz): [0.68 1.76 3.2 ] (conditions: [72, 72, 71]); within 10% of 0.5,1.5,2.5,4: [np.False_, np.False_, np.False_]
   all eigenvalue frequencies: range 0.00-3.76 Hz; |eigenvalue| range 0.907-0.999
   points outside the axes: 0
PMd-N: k=5; complex pairs per condition [ 0  0 72] ; real eigenvalues per condition [ 0 72] ; conditions with >=1 real: 72/72
[... 159 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
a=json.load(open('reproduce_sabatini_2024.ipynb'))
for i in [2,3,9,11]:
    print("=====",i); print(''.join(a['cells'][i]['source']))
print(a['cells'][9].keys(), a['nbformat'], a['nbformat_minor'])
EOF
```

```
===== 2
## Loading

Each session is streamed once. Spike times are binned at 1 ms from 500 ms before to 1000 ms after
movement onset, smoothed with a Gaussian of 20 ms s.d. and sampled every 10 ms from -350 to +850 ms
(Methods, Subjects, behavior and data pre-processing; claims, shared method). The time-shuffled
copies for tbf-shuffle-control are made at load time under that claim's five seeds, and the warped
copies for fig3i at the same time.
===== 3
SESS = {}
for m in ("J", "N"):
    t0 = time.time()
    SESS[m] = ldr.load_session(m, shuffle_seeds=seeds5("tbf-shuffle-control"))
    print(m, "loaded in", round(time.time() - t0), "s; trials kept (successful, 72 conditions):",
          len(SESS[m]["trials"]["maze_condition"]))
===== 9
def clock_check(m):
    S = SESS[m]
    tr = S["trials"]
    cond = CT[m]["cond"]
[... 69 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/edit_nb.py <<'PYEOF'
import json, uuid
P = 'entries/sabatini-2024/reproduce_sabatini_2024.ipynb'
nb = json.load(open(P))
C = nb['cells']
def src(i): return ''.join(C[i]['source'])
def put(i, s): C[i]['source'] = s.splitlines(keepends=True)
def rep(i, old, new):
    s = src(i); assert old in s, (i, old[:60]); put(i, s.replace(old, new))
def cell(kind, s, tags=None):
    c = dict(cell_type=kind, id=uuid.uuid4().hex[:8], metadata={} if not tags else {"tags": tags}, source=s.splitlines(keepends=True))
    if kind == 'code': c.update(execution_count=None, outputs=[])
    return c

# header
rep(0, "a delay above 400 ms, with each claim's own seed only; every outcome is the same under both readings.",
    "a delay above 400 ms, with each claim's own seed only; every outcome is the same under both readings.\n"
    "A second companion, `reproduce_sabatini_2024_stable_units.ipynb`, runs this notebook without the two\n"
    "units whose spike trains are not one stable unit's (see \"Unit checks\"), with each claim's own seed only.")
# parameters
rep(1, 'FULL_SEEDS = True\n',
    'FULL_SEEDS = True\n'
    '# Leave out the units found in "Unit checks" whose spike train is not one stable unit\'s (the paper used\n'
    '# "single-units and stable multi-units"). The companion notebook reproduce_sabatini_2024_stable_units.ipynb\n'
    '# is this notebook with EXCLUDE_UNSTABLE = True and FULL_SEEDS = False.\n'
    'EXCLUDE_UNSTABLE = False\n')
rep(1, '"| five seeds", FULL_SEEDS)', '"| five seeds", FULL_SEEDS,\n      "| unstable units left out", EXCLUDE_UNSTABLE)')
# loading
rep(2, "copies for tbf-shuffle-control are made at load time under that claim's five seeds, and the warped",
    "copies for tbf-shuffle-control are made at load time under that claim's five seeds, a copy shuffled over\n"
    "the span of the paper's code (the analysis window) under the claim's own seed, and the warped")
rep(3, 'shuffle_seeds=seeds5("tbf-shuffle-control"))',
    'shuffle_seeds=seeds5("tbf-shuffle-control"),\n'
    '                               shuffle_window_seeds=[seed("tbf-shuffle-control")])')
# clock check: optional unit mask
rep(9, 'def clock_check(m):', 'def clock_check(m, units=None):')
rep(9, '    F = S["R"][:, :, gi].mean(2)\n', '    F = S["R"][:, :, gi].mean(2)\n    if units is not None:\n        F = F[:, units]\n')

unit_md = """### Unit checks

The paper used "single-units and stable multi-units" (Methods, Subjects, behavior and data
pre-processing). Two units of the dandiset are neither. In the Jenkins file one unit's spike train
holds two sorted runs one after the other; the cell prints each run's size and span, the spike times
they share, intervals under 1 ms, and how many of each run's times are found exactly in another
unit's train. In the Nitschke file, the cell prints each segment's per-trial summed rate, and, per
unit, the largest mean rate over blocks of 50 successive trials divided by the median block mean
(`ldr.block_rate_ratio`); a unit above 5 is unstable (a threshold chosen here; the cell prints the
ratios, so that the range of thresholds giving the same units can be read off). The clock check is
repeated without the unstable units. The main analyses keep every unit, as before; the companion
notebook `reproduce_sabatini_2024_stable_units.ipynb` leaves both units out.
"""
unit_code = '''RUNS = {}
for m in ("J", "N"):
    S = SESS[m]
    if S["info"]["n_hand_segments"] == 1:
        for un in np.where(S["info"]["unit_jumps"] > 0)[0]:
            RUNS[(m, int(un))] = ldr.spike_run_report(m, un)
for (m, un), rep in RUNS.items():
    print(f"{m} unit {un} ({SESS[m]['area'][un]}), one recording segment: runs (spikes, first s, last s)",
          [(n, round(a, 1), round(b, 1)) for n, a, b in rep["runs"]])
    print(f"   spike times found in both runs: {rep['shared']}; intervals under 1 ms: merged train {rep['isi_below_1ms_merged']:.4f}, "
          f"each run {[round(x, 4) for x in rep['isi_below_1ms_runs']]}")
    print("   largest fraction of each run's times found exactly in another unit's train (fraction, unit):",
          [(round(f, 3), int(o)) for f, o in rep["most_shared_with_other_unit"]])

gi_ = (ldr.GRID_MS >= -100) & (ldr.GRID_MS <= 300)
for m in ("J", "N"):
    tr = SESS[m]["trials"]
    tot = SESS[m]["R"][:, :, gi_].mean(2).sum(1)
    for sg in np.unique(tr["segment"]):
        ii = (tr["segment"] == sg) & MASK[m]
        print(f"{m} segment {sg}: {int(ii.sum())} trials; per-trial rate summed over units, -100 to +300 ms (spikes/s), "
              f"percentiles 0/5/50/95/100: {np.round(np.percentile(tot[ii], [0, 5, 50, 95, 100])).astype(int).tolist()}")

RATIO = {m: ldr.block_rate_ratio(SESS[m]["R"]) for m in ("J", "N")}
UNSTABLE = {}
for m in ("J", "N"):
    o = np.argsort(-RATIO[m])[:4]
    UNSTABLE[m] = np.where(RATIO[m] > 5)[0]
    print(f"{m}: block rate ratio, largest four (unit: ratio)", {int(u): round(float(RATIO[m][u]), 2) for u in o},
          "| median over units", round(float(np.median(RATIO[m])), 2), "| above 5:", UNSTABLE[m].tolist())
    for un in UNSTABLE[m]:
        tr = SESS[m]["trials"]
        fr = SESS[m]["R"][:, un].mean(1)
        for sg in np.unique(tr["segment"]):
            ii = (tr["segment"] == sg) & MASK[m]
            print(f"   unit {un} ({SESS[m]['area'][un]}) segment {sg}: mean rate {fr[ii].mean():.1f} spikes/s, "
                  f"median {np.median(fr[ii]):.1f}, trials above 100 spikes/s {int((fr[ii] > 100).sum())} of {int(ii.sum())}")
        st = SESS[m]["trials"]["start_time"]
        hi = (fr > 100) & MASK[m]
        if hi.any():
            print(f"   trials above 100 spikes/s start from {st[hi].min():.0f} to {st[hi].max():.0f} s (segment clock)")

DROP = {m: sorted(set(UNSTABLE[m].tolist()) | {un for (mm, un) in RUNS if mm == m}) for m in ("J", "N")}
KEEP = {m: np.ones(len(SESS[m]["area"]), bool) for m in ("J", "N")}
for m in ("J", "N"):
    if EXCLUDE_UNSTABLE:
        KEEP[m][DROP[m]] = False
    print(f"{m}: units not one stable unit's {DROP[m]} ({[str(SESS[m]['area'][u]) for u in DROP[m]]}); "
          f"left out in this run: {EXCLUDE_UNSTABLE}")
for m in ("N",):
    keep_u = ~np.isin(np.arange(len(SESS[m]["area"])), UNSTABLE[m])
    for sg, n, acc, acc_sh, cross in clock_check(m, keep_u):
        print(f"{m} segment {sg} without the unstable units: condition decoded {acc:.3f} (labels of the previous trial "
              f"{acc_sh:.3f}; trained on the other segments {cross:.3f})")
'''
C[10:10] = [cell('markdown', unit_md), cell('code', unit_code, ['sanity'])]
# indices shift by 2 from here on (old i -> i+2)
def I(old): return old + 2
rep(I(11), '    u = S["area"] == area\n', '    u = (S["area"] == area) & KEEP[m]\n')
rep(I(11), '    print(NAME[ds], "held-out VE by k:"', '    print(NAME[ds], f"({int(D[ds][\'u\'].sum())} units)", "held-out VE by k:"')
# shuffle over the code's span
rep(I(31), "The span permuted is the 1.5 s window\nread around movement onset (assumption; the paper does not give it).",
    "The span permuted is the 1.5 s window\nread around movement onset (assumption; the paper's text does not give it). The paper's code permutes\n"
    "all columns of a trial's 1 ms matrix (scrambleTrials.m) and smooths and down-samples the same matrix\n"
    "(preprocessTrials.m), so its span is the analysis window, -350 to +850 ms; that span is run as a\n"
    "variant under the claim's own seed.")
rep(I(32), '        SH[ds][sd] = dict(ve=ve, rec=recoverability(Lsd, Bsd, Xs), rec_raw=recoverability(Ls, Bs, Xs))\n',
    '        SH[ds][sd] = dict(ve=ve, rec=recoverability(Lsd, Bsd, Xs), rec_raw=recoverability(Ls, Bs, Xs))\n'
    '    # variant: shuffled over the span of the paper\'s code, the analysis window (scrambleTrials.m)\n'
    '    for sd, RSW in SESS[m]["RSW"].items():\n'
    '        Xs = ldr.cond_average(RSW[:, D[ds]["u"]], D[ds]["cond"], 72, MASK[m])[..., ldr.FIT0:]\n'
    '        Bs, Ls = ldr.tbf(Xs, D[ds]["k"])\n'
    '        Bsd, Lsd = ldr.demix(Bs, Ls)[:2]\n'
    '        SHW[ds] = dict(ve=ldr.pop_ve(Xs, np.einsum("cnk,kt->cnt", Ls, Bs)), rec=recoverability(Lsd, Bsd, Xs))\n')
rep(I(32), 'SH = {}\n', 'SH = {}\nSHW = {}\n')
rep(I(33), '    print("   shuffled mean under the five seeds:"',
    '    w = SHW[ds]["ve"]\n'
    '    print(f"   variant, shuffled over the code\'s span (-350 to +850 ms): mean {w.mean():.3f} s.d. {w.std():.3f}; "\n'
    '          f"rank-sum p {stats.ranksums(real, w).pvalue:.2e}; real higher on {int((real > w).sum())}/72")\n'
    '    print("   shuffled mean under the five seeds:"')
rep(I(35), '          f"{recoverability(D[ds][\'Lraw\'], D[ds][\'Braw\'], D[ds][\'Xw\']).mean():.3f}")\n',
    '          f"{recoverability(D[ds][\'Lraw\'], D[ds][\'Braw\'], D[ds][\'Xw\']).mean():.3f}")\n'
    '    w = SHW[ds]["rec"]\n'
    '    print(f"   variant, chance on data shuffled over the code\'s span (-350 to +850 ms): mean {w.mean():.3f}; "\n'
    '          f"rank-sum p {stats.ranksums(rec, w).pvalue:.2e}; real higher on {int((rec > w).sum())}/72")\n')
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False)
open(P, 'a').write('\n')
print("ok", len(C))
PYEOF
cd entries/sabatini-2024 && cp reproduce_sabatini_2024.ipynb $TMPDIR/main_backup.ipynb && head -c 300 reproduce_sabatini_2024.ipynb && tail -c 100 reproduce_sabatini_2024.ipynb | od -c | tail -3 && python3 $TMPDIR/edit_nb.py && git diff --stat .
```

```
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "e7adaf51",
   "metadata": {},
   "source": [
    "# Reproducing Sabatini & Kaufman (2024) on DANDI:000070\n",
    "\n",
    "**Paper.** Sabatini, D. A. & Kaufman, M. T. (2024). Reach-dependent reorientation of rotational dynamics\n",
    "in mo0000120   b   f   o   r   m   a   t   _   m   i   n   o   r   "   :    
0000140   5  \n   }  \n
0000144
Traceback (most recent call last):
  File "/tmp/claude-1001/edit_nb.py", line 117, in <module>
    rep(I(32), '        SH[ds][sd] = dict(ve=ve, rec=recoverability(Lsd, Bsd, Xs), rec_raw=recoverability(Ls, Bs, Xs))\n',
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        '        SH[ds][sd] = dict(ve=ve, rec=recoverability(Lsd, Bsd, Xs), rec_raw=recoverability(Ls, Bs, Xs))\n'
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    ...<4 lines>...
[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('edit_nb.py').read()
s=s.replace("""rec_raw=recoverability(Ls, Bs, Xs))\\n',
    '        SH[ds][sd] = dict(""","""rec_raw=recoverability(Ls, Bs, Xs))',
    '        SH[ds][sd] = dict(""")
s=s.replace("""rec=recoverability(Lsd, Bsd, Xs))\\n')
rep(I(32), 'SH = {}""","""rec=recoverability(Lsd, Bsd, Xs))')
rep(I(32), 'SH = {}""")
s=s.replace("""D[ds]['Xw']).mean():.3f}")\\n',
    '          f"{recoverability""","""D[ds]['Xw']).mean():.3f}")',
    '          f"{recoverability""")
s=s.replace("""real higher on {int((rec > w).sum())}/72")\\n')""","""real higher on {int((rec > w).sum())}/72")')""")
open('edit_nb.py','w').write(s)
EOF
grep -n "rec_raw=recoverability\|SHW\[ds\] = dict\|Xw'\]).mean" edit_nb.py; cd entries/sabatini-2024 && python3 $TMPDIR/edit_nb.py && git diff --stat .
```

```
117:rep(I(32), '        SH[ds][sd] = dict(ve=ve, rec=recoverability(Lsd, Bsd, Xs), rec_raw=recoverability(Ls, Bs, Xs))',
118:    '        SH[ds][sd] = dict(ve=ve, rec=recoverability(Lsd, Bsd, Xs), rec_raw=recoverability(Ls, Bs, Xs))\n'
124:    '        SHW[ds] = dict(ve=ldr.pop_ve(Xs, np.einsum("cnk,kt->cnt", Ls, Bs)), rec=recoverability(Lsd, Bsd, Xs))')
Traceback (most recent call last):
  File "/tmp/claude-1001/edit_nb.py", line 131, in <module>
    rep(I(35), '          f"{recoverability(D[ds][\'Lraw\'], D[ds][\'Braw\'], D[ds][\'Xw\']).mean():.3f}")\n',
    ~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        '          f"{recoverability(D[ds][\'Lraw\'], D[ds][\'Braw\'], D[ds][\'Xw\']).mean():.3f}")\n'
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        '    w = SHW[ds]["rec"]\n'
        ^^^^^^^^^^^^^^^^^^^^^^^^^^
        '    print(f"   variant, chance on data shuffled over the code\'s span (-350 to +850 ms): mean {w.mean():.3f}; "\n'
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        '          f"rank-sum p {stats.ranksums(rec, w).pvalue:.2e}; real higher on {int((rec > w).sum())}/72")')
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/tmp/claude-1001/edit_nb.py", line 8, in rep
    s = src(i); assert old in s, (i, old[:60]); put(i, s.replace(old, new))
                       ^^^^^^^^
AssertionError: (37, '          f"{recoverability(D[ds][\'Lraw\'], D[ds][\'Braw\'], D[')
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i "s|D\[ds\]\[\\\\'Xw\\\\'\]).mean():.3f}\")\\\\n',|D[ds][\\\\'Xw\\\\']).mean():.3f}\")',|" edit_nb.py && sed -n 129,136p edit_nb.py && cd entries/sabatini-2024 && python3 $TMPDIR/edit_nb.py && git diff --stat .
```

```
'          f"rank-sum p {stats.ranksums(real, w).pvalue:.2e}; real higher on {int((real > w).sum())}/72")\n'
    '    print("   shuffled mean under the five seeds:"')
rep(I(35), '          f"{recoverability(D[ds][\'Lraw\'], D[ds][\'Braw\'], D[ds][\'Xw\']).mean():.3f}")',
    '          f"{recoverability(D[ds][\'Lraw\'], D[ds][\'Braw\'], D[ds][\'Xw\']).mean():.3f}")\n'
    '    w = SHW[ds]["rec"]\n'
    '    print(f"   variant, chance on data shuffled over the code\'s span (-350 to +850 ms): mean {w.mean():.3f}; "\n'
    '          f"rank-sum p {stats.ranksums(rec, w).pvalue:.2e}; real higher on {int((rec > w).sum())}/72")')
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False)
ok 127
 entries/sabatini-2024/ldr.py                       |  53 ++++++++-
 .../sabatini-2024/reproduce_sabatini_2024.ipynb    | 131 +++++++++++++++++++--
 2 files changed, 173 insertions(+), 11 deletions(-)
```

**Agent calls Bash**

```bash
git diff reproduce_sabatini_2024.ipynb | head -150
```

```
diff --git a/entries/sabatini-2024/reproduce_sabatini_2024.ipynb b/entries/sabatini-2024/reproduce_sabatini_2024.ipynb
index 8b41eb2..8e0fd5f 100644
--- a/entries/sabatini-2024/reproduce_sabatini_2024.ipynb
+++ b/entries/sabatini-2024/reproduce_sabatini_2024.ipynb
@@ -39,6 +39,8 @@
     "conditions (an assumption; see \"Conditions and trial readings\"). The companion notebook\n",
     "`reproduce_sabatini_2024_trials_b.ipynb` is this notebook run under reading (b), successful trials with\n",
     "a delay above 400 ms, with each claim's own seed only; every outcome is the same under both readings.\n",
+    "A second companion, `reproduce_sabatini_2024_stable_units.ipynb`, runs this notebook without the two\n",
+    "units whose spike trains are not one stable unit's (see \"Unit checks\"), with each claim's own seed only.\n",
     "\n",
     "Where a parameter comes from (the claim, a passage of the paper, an assumption, or a standard choice)\n",
     "is said in the docstrings of the helper `ldr.py` and beside the code here."
@@ -68,6 +70,10 @@
     "READING = \"a\"\n",
     "# Run the four extra seeds of each claim (protocol); the companion notebook runs the claim's own seed only.\n",
     "FULL_SEEDS = True\n",
+    "# Leave out the units found in \"Unit checks\" whose spike train is not one stable unit's (the paper used\n",
+    "# \"single-units and stable multi-units\"). The companion notebook reproduce_sabatini_2024_stable_units.ipynb\n",
+    "# is this notebook with EXCLUDE_UNSTABLE = True and FULL_SEEDS = False.\n",
[... 130 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "sanity" tools/*.py | head
```

```
tools/entry.py:21:- each notebook has a cell tagged `sanity` that prints what was loaded;
tools/entry.py:236:        if not any("sanity" in c.metadata.get("tags", []) for c in nb.cells if c.cell_type == "code"):
tools/entry.py:237:            report.error(rel / name, "no code cell tagged `sanity` (the data check; see docs/protocol.md)")
```

**Agent calls Bash**

```bash
date -u && PY=executed/sabatini-2024/.venv/bin/python && cat > $TMPDIR/runcells.py <<'EOF'
import json, sys, time
nb = json.load(open(sys.argv[1]))
idx = [int(x) for x in sys.argv[2].split(",")]
g = {"__name__": "__main__"}
for i in idx:
    c = nb["cells"][i]
    if c["cell_type"] != "code": continue
    t = time.time()
    print(f"##### cell {i}", flush=True)
    exec(compile("".join(c["source"]), f"cell{i}", "exec"), g)
    print(f"##### cell {i} took {time.time()-t:.0f}s", flush=True)
EOF
timeout 2400 $PY $TMPDIR/runcells.py reproduce_sabatini_2024.ipynb 1,3,5,7,9,11,13,33,35,37 2>&1 | grep -v Warning | tail -80; date -u
```

```
Fri Nov 20 17:21:35 UTC 2026
##### cell 1
Traceback (most recent call last):
  File "/tmp/claude-1001/runcells.py", line 10, in <module>
    exec(compile("".join(c["source"]), f"cell{i}", "exec"), g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "cell1", line 9, in <module>
ModuleNotFoundError: No module named 'ldr'
Fri Nov 20 17:21:37 UTC 2026
```

**Agent calls Bash**

```bash
date -u && PY=executed/sabatini-2024/.venv/bin/python && PYTHONPATH=. timeout 2400 $PY $TMPDIR/runcells.py reproduce_sabatini_2024.ipynb 1,3,5,7,9,11,13,33,35,37 2>&1 | grep -v Warning | tail -80; date -u
```

```
Fri Nov 20 17:21:39 UTC 2026
  peak hand speed per trial (file units per s): median 741.4
  reach duration ms: median 383.0 range 206.0 813.0
  smoothed rates (spikes/s): range 0.0 484.21783447265625 mean 47.47356414794922
peak memory GB 4.93236
##### cell 5 took 0s
##### cell 7
J reading (a) conditions 72 | reading (b) 1-target conditions 73 | (b) minus maze 0: 72 | same set as (a): True
   maze 0 trials: 203 targets [1 3] barriers [2 7 9] novel_maze [0 1]
   conditions kept: 72 | straight (no barrier): 36 | curved: 36
   trial reading (a): 1595 trials; per condition 17 to 29
   trial reading (b): 1381 trials; per condition 16 to 23
   with correct_reach also required (not a reading): 1345
N reading (a) conditions 72 | reading (b) 1-target conditions 73 | (b) minus maze 0: 72 | same set as (a): True
   maze 0 trials: 419 targets [1 3] barriers [0 1 2 3 4 5 6 7 8 9] novel_maze [0 1]
   conditions kept: 72 | straight (no barrier): 36 | curved: 36
   trial reading (a): 2121 trials; per condition 23 to 42
   trial reading (b): 1884 trials; per condition 19 to 37
   with correct_reach also required (not a reading): 1867
trials analysed (reading (a), with hand position): {'J': 1595, 'N': 2120}
[... 62 more lines not kept]
```

**Agent calls Bash**

```bash
PY=executed/sabatini-2024/.venv/bin/python && $PY - <<'EOF'
import numpy as np, ldr
f,_=ldr.open_nwb("J"); u=f["units"]; sidx=u["spike_times_index"][:]
s=u["spike_times"][0:sidx[0]]
print(len(s), s[0], s[-1], np.histogram(s, np.arange(0,16001,500))[0])
EOF
```

```
61030 4.863466666666667 4259.041966666667 [5992 6385 6518 6829 7650 7835 7330 8405 4086    0    0    0    0    0
    0    0    0    0    0    0    0    0    0    0    0    0    0    0
    0    0    0    0]
```

**Agent calls Bash**

```bash
PY=executed/sabatini-2024/.venv/bin/python && $PY - <<'EOF'
import numpy as np, ldr
f,_=ldr.open_nwb("J"); u=f["units"]; sidx=u["spike_times_index"][:]; a0=np.r_[0,sidx[:-1]]
g=lambda k: u["spike_times"][a0[k]:sidx[k]]
s0=g(0); s1=g(1); r1=s1[:196608]; r2=s1[196608:]
for k in (68,32,33,73,84):
    sk=g(k); print(k, "unit0 in it", round(np.isin(s0,sk).mean(),3), "run1 in it", round(np.isin(r1,sk).mean(),3), "run2", round(np.isin(r2,sk).mean(),3))
print("gap between unit0 last and run1 first (ms):", (r1[0]-s0[-1])*1e3)
print("rate unit0 /s", len(s0)/(s0[-1]-s0[0]), "run1", len(r1)/(r1[-1]-r1[0]), "run2", len(r2)/(r2[-1]-r2[0]))
EOF
```

```
68 unit0 in it 0.279 run1 in it 0.374 run2 0.008
32 unit0 in it 0.247 run1 in it 0.264 run2 0.003
33 unit0 in it 0.266 run1 in it 0.29 run2 0.003
73 unit0 in it 0.26 run1 in it 0.278 run2 0.004
84 unit0 in it 0.258 run1 in it 0.279 run2 0.003
gap between unit0 last and run1 first (ms): 54.566666666687524
rate unit0 /s 14.345895453140953 run1 17.23189265715739 run2 16.914436173923775
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='ldr.py'; s=open(p).read()
old='''    """The runs of one unit whose spike train restarts: for each run its size and first and last
    time, the spike times the runs share, the fraction of the merged train's intervals under 1 ms
    (and of each run's), and for each run the largest fraction of its times found exactly in another
    unit's train, with that unit."""'''
new='''    """The runs of one unit whose spike train restarts: for each run its size and first and last
    time, the spike times the runs share, the fraction of the merged train's intervals under 1 ms
    (and of each run's), for each run the largest fraction of its times found exactly in another
    unit's train, with that unit, and the other units whose train ends within 1 s before a run
    starts (unit, spikes, first and last time)."""'''
assert old in s; s=s.replace(old,new)
old='''    best = [(0.0, -1)] * len(runs)
    for other in range(len(sidx)):
        if other == unit:
            continue
        so = u["spike_times"][a0[other]:sidx[other]]
        best = [max(b, (float(np.isin(r, so).mean()), other)) for b, r in zip(best, runs)]
    f.close()
    out["most_shared_with_other_unit"] = best'''
new='''    best = [(0.0, -1)] * len(runs)
    ends = []
    for other in range(len(sidx)):
        if other == unit:
            continue
        so = u["spike_times"][a0[other]:sidx[other]]
        best = [max(b, (float(np.isin(r, so).mean()), other)) for b, r in zip(best, runs)]
        if len(so) and any(0 <= r[0] - so.max() < 1 for r in runs):
            ends.append((other, len(so), float(so.min()), float(so.max())))
    f.close()
    out["most_shared_with_other_unit"] = best
    out["ends_before_a_run"] = ends'''
assert old in s; s=s.replace(old,new); open(p,'w').write(s)

import json
P='reproduce_sabatini_2024.ipynb'; nb=json.load(open(P)); c=nb['cells'][11]; src=''.join(c['source'])
old='''          [(round(f, 3), int(o)) for f, o in rep["most_shared_with_other_unit"]])
'''
new='''          [(round(f, 3), int(o)) for f, o in rep["most_shared_with_other_unit"]])
    for o, n, a, b in rep["ends_before_a_run"]:
        print(f"   unit {o} ({SESS[m]['area'][o]}): {n} spikes from {a:.1f} to {b:.1f} s, ending "
              f"{(min(r[1] for r in rep['runs'] if r[1] > b) - b) * 1000:.0f} ms before a run of unit {un} starts")
'''
assert old in src; src=src.replace(old,new); c['source']=src.splitlines(keepends=True)
json.dump(nb, open(P,'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
EOF
sed -i 's/^g = {"__name__": "__main__"}/g = sys.modules["__main__"].__dict__/' $TMPDIR/runcells.py
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
python3 -c "
import json;nb=json.load(open('reproduce_sabatini_2024.ipynb'))
for i in range(12,40):
    c=nb['cells'][i]; s=''.join(c['source'])
    if 'tbf_ve' in s and '=' in s: print(i,c['cell_type'],s[:150].replace(chr(10),' | '))
"
```

```
31 code for ds in DATASETS: |     Xw = D[ds]["Xw"] |     ve_a = ldr.pop_ve(Xw, np.einsum("cnk,kt->cnt", D[ds]["L"], D[ds]["B"])) |     B2, L2 = ldr.tbf(D[ds]["X"], 
35 code s0 = seed("tbf-shuffle-control") | for ds in DATASETS: |     real, sh = D[ds]["tbf_ve"], SH[ds][s0]["ve"] |     p_rs = stats.ranksums(real, sh).pvalue |     p
```

**Agent calls Bash**

```bash
date -u && PY=executed/sabatini-2024/.venv/bin/python && PYTHONPATH=. timeout 2400 $PY $TMPDIR/runcells.py reproduce_sabatini_2024.ipynb 1,3,7,11,13,31,34,35,37 2>&1 | grep -v Warning | grep -v "^##### cell [0-9]*$" | tail -60; date -u
```

```
Fri Nov 20 17:31:05 UTC 2026
dandiset 000070 version 0.260528.0919 | trial reading a | five seeds True | unstable units left out False
##### cell 1 took 1s
J loaded in 204 s; trials kept (successful, 72 conditions): 1595
N loaded in 283 s; trials kept (successful, 72 conditions): 2121
##### cell 3 took 487s
J reading (a) conditions 72 | reading (b) 1-target conditions 73 | (b) minus maze 0: 72 | same set as (a): True
   maze 0 trials: 203 targets [1 3] barriers [2 7 9] novel_maze [0 1]
   conditions kept: 72 | straight (no barrier): 36 | curved: 36
   trial reading (a): 1595 trials; per condition 17 to 29
   trial reading (b): 1381 trials; per condition 16 to 23
   with correct_reach also required (not a reading): 1345
N reading (a) conditions 72 | reading (b) 1-target conditions 73 | (b) minus maze 0: 72 | same set as (a): True
   maze 0 trials: 419 targets [1 3] barriers [0 1 2 3 4 5 6 7 8 9] novel_maze [0 1]
   conditions kept: 72 | straight (no barrier): 36 | curved: 36
   trial reading (a): 2121 trials; per condition 23 to 42
   trial reading (b): 1884 trials; per condition 19 to 37
   with correct_reach also required (not a reading): 1867
trials analysed (reading (a), with hand position): {'J': 1595, 'N': 2120}
##### cell 7 took 0s
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
df -h $TMPDIR | tail -1; free -g | head -2
```

```
/dev/root       145G   59G   86G  41% /tmp/claude-1001
               total        used        free      shared  buff/cache   available
Mem:              15           1          11           0           3          14
```

**Agent calls Bash**

```bash
cat > $TMPDIR/runcells.py <<'EOF'
import json, sys, time, os, pickle
nb = json.load(open(sys.argv[1]))
idx = [int(x) for x in sys.argv[2].split(",")]
g = sys.modules["__main__"].__dict__
cache = os.environ["TMPDIR"] + "/SESS.pkl"
for i in idx:
    c = nb["cells"][i]
    if c["cell_type"] != "code": continue
    t = time.time()
    print(f"##### cell {i}", flush=True)
    if i == 3 and os.path.exists(cache):
        g["SESS"] = pickle.load(open(cache, "rb"))
    else:
        exec(compile("".join(c["source"]), f"cell{i}", "exec"), g)
        if i == 3:
            pickle.dump(g["SESS"], open(cache, "wb"), protocol=5)
    print(f"##### cell {i} took {time.time()-t:.0f}s", flush=True)
EOF
date -u && PY=executed/sabatini-2024/.venv/bin/python && PYTHONPATH=. timeout 2400 $PY $TMPDIR/runcells.py reproduce_sabatini_2024.ipynb 1,3,7,9,11,13,31,34,35,37 2>&1 | grep -v Warning | grep -v "^##### cell [0-9]*$" | tail -42; date -u
```

```
Fri Nov 20 17:39:40 UTC 2026
##### cell 11 took 23s
M1-J (96 units) held-out VE by k: [0.4   0.559 0.681 0.719 0.735 0.742 0.739 0.734 0.727 0.72  0.714 0.708]
   best k under five seeds [6, 6, 6, 6, 6] -> k used 7 | frequencies (Hz) [0.   0.71 0.71 1.85 1.85 3.13 3.13] | |eigenvalue| [1.001 0.988 0.988 0.987 0.987 0.979 0.979]
PMd-J (96 units) held-out VE by k: [0.407 0.643 0.774 0.805 0.813 0.811 0.806 0.8   0.794 0.788 0.783 0.778]
   best k under five seeds [5, 5, 5, 5, 5] -> k used 5 | frequencies (Hz) [0.   0.64 0.64 1.54 1.54] | |eigenvalue| [1.    0.988 0.988 0.987 0.987]
M1-N (96 units) held-out VE by k: [0.324 0.606 0.775 0.837 0.864 0.876 0.88  0.88  0.878 0.876 0.873 0.87 ]
   best k under five seeds [7, 7, 7, 7, 7] -> k used 7 | frequencies (Hz) [0.   0.69 0.69 1.81 1.81 3.24 3.24] | |eigenvalue| [0.999 0.988 0.988 0.977 0.977 0.971 0.971]
PMd-N (96 units) held-out VE by k: [0.414 0.615 0.748 0.788 0.81  0.814 0.814 0.811 0.806 0.801 0.796 0.791]
   best k under five seeds [6, 6, 6, 6, 6] -> k used 7 | frequencies (Hz) [0.   0.74 0.74 1.56 1.56 2.71 2.71] | |eigenvalue| [0.994 0.991 0.991 0.974 0.974 0.972 0.972]
##### cell 13 took 223s
M1-J: (a) -150..+850 ms, de-mixed basis: mean 0.941 s.d. 0.011 range 0.912-0.962 | (b) -350..+850 ms, raw SVD basis: mean 0.928 s.d. 0.013
PMd-J: (a) -150..+850 ms, de-mixed basis: mean 0.943 s.d. 0.014 range 0.901-0.962 | (b) -350..+850 ms, raw SVD basis: mean 0.930 s.d. 0.014
M1-N: (a) -150..+850 ms, de-mixed basis: mean 0.969 s.d. 0.007 range 0.953-0.979 | (b) -350..+850 ms, raw SVD basis: mean 0.963 s.d. 0.008
PMd-N: (a) -150..+850 ms, de-mixed basis: mean 0.958 s.d. 0.009 range 0.934-0.974 | (b) -350..+850 ms, raw SVD basis: mean 0.950 s.d. 0.008
##### cell 31 took 0s
##### cell 34 took 4s
M1-J: shuffled VE mean 0.422 s.d. 0.019 (real 0.941); rank-sum p 3.91e-25; signed-rank (variant) p 1.66e-13; real higher on 72/72
   variant, shuffled over the code's span (-350 to +850 ms): mean 0.420 s.d. 0.018; rank-sum p 3.91e
[... 25 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/make_companions.py <<'EOF'
import json, copy, uuid
D = 'entries/sabatini-2024/'
main = json.load(open(D + 'reproduce_sabatini_2024.ipynb'))
old_b = json.load(open(D + 'reproduce_sabatini_2024_trials_b.ipynb'))
HEAD_B = ''.join(old_b['cells'][0]['source'])
HEAD_S = """# Sabatini & Kaufman (2024) on DANDI:000070: stable units only

This notebook is `reproduce_sabatini_2024.ipynb` with two parameters changed in its first code cell: `EXCLUDE_UNSTABLE = True` (the units that "Unit checks" finds are not one stable unit's are left out: in the Jenkins file units 0 and 1, whose spike trains are split between their rows, and in the Nitschke file unit 170, which fires at about 400 spikes/s on 229 trials of segment 3) and `FULL_SEEDS = False` (each claim's own seed only). Trials are reading (a), as in the main notebook. Every analysis and every claim cell is the same. The paper used "single-units and stable multi-units" (Methods, Subjects, behavior and data pre-processing); this notebook shows whether the outcomes depend on these units. The conclusions, and the outcomes, are in the main notebook and the attempt record.

Dataset: DANDI:000070, version 0.260528.0919, streamed. Paper: doi:10.1038/s41467-024-51308-7.
"""
def make(head, params, path):
    nb = copy.deepcopy(main)
    cells = []
    for i, c in enumerate(nb['cells']):
        s = ''.join(c['source'])
        if c['cell_type'] == 'markdown' and (s.startswith('**Result') or s.startswith('## Summary')):
            continue
        if i == 0:
            c['source'] = head.splitlines(keepends=True)
        if i == 1:
            for a, b in params:
                assert a in s, a
                s = s.replace(a, b)
            c['source'] = s.splitlines(keepends=True)
        if c['cell_type'] == 'code':
            c['outputs'] = []
            c['execution_count'] = None
        cells.append(c)
    nb['cells'] = cells
    json.dump(nb, open(path, 'w'), indent=1, ensure_ascii=False)
    open(path, 'a').write('\n')
    print(path, len(cells))
make(HEAD_B, [('READING = "a"\n', 'READING = "b"\n'), ('FULL_SEEDS = True\n', 'FULL_SEEDS = False\n')],
     D + 'reproduce_sabatini_2024_trials_b.ipynb')
make(HEAD_S, [('EXCLUDE_UNSTABLE = False\n', 'EXCLUDE_UNSTABLE = True\n'), ('FULL_SEEDS = True\n', 'FULL_SEEDS = False\n')],
     D + 'reproduce_sabatini_2024_stable_units.ipynb')
EOF
python3 $TMPDIR/make_companions.py && git diff --stat . && git status --short .
```

```
entries/sabatini-2024/reproduce_sabatini_2024_trials_b.ipynb 92
entries/sabatini-2024/reproduce_sabatini_2024_stable_units.ipynb 92
 entries/sabatini-2024/ldr.py                       |  58 +++-
 .../sabatini-2024/reproduce_sabatini_2024.ipynb    | 134 ++++++++-
 .../reproduce_sabatini_2024_trials_b.ipynb         | 322 ++++++++++++++-------
 3 files changed, 394 insertions(+), 120 deletions(-)
 M ldr.py
 M reproduce_sabatini_2024.ipynb
 M reproduce_sabatini_2024_trials_b.ipynb
?? reproduce_sabatini_2024_stable_units.ipynb
```

**Agent calls Bash**

```bash
date -u && PY=executed/sabatini-2024/.venv/bin/python && N=$(python3 -c "import json;print(len(json.load(open('reproduce_sabatini_2024_stable_units.ipynb'))['cells']))") && PYTHONPATH=. timeout 3000 $PY $TMPDIR/runcells.py reproduce_sabatini_2024_stable_units.ipynb $(seq -s, 1 $((N-1))) > $TMPDIR/stable.log 2>&1; echo exit $?; date -u; grep -c "took" $TMPDIR/stable.log; tail -5 $TMPDIR/stable.log
```

```
Fri Nov 20 17:52:29 UTC 2026
exit 1
Fri Nov 20 17:58:21 UTC 2026
13
Traceback (most recent call last):
  File "/tmp/claude-1001/runcells.py", line 14, in <module>
    exec(compile("".join(c["source"]), f"cell{i}", "exec"), g)
    ~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: exec() globals must be a dict, not numpy.ndarray
```

**Agent calls Bash**

```bash
cat > $TMPDIR/runcells.py <<'EOF'
import json as __json, sys as __sys, time as __time, os as __os, pickle as __pickle
__nb = __json.load(open(__sys.argv[1]))
__idx = [int(x) for x in __sys.argv[2].split(",")]
__G = __sys.modules["__main__"].__dict__
__cache = __os.environ["TMPDIR"] + "/SESS.pkl"
for __i in __idx:
    __c = __nb["cells"][__i]
    if __c["cell_type"] != "code": continue
    __t = __time.time()
    print(f"##### cell {__i}", flush=True)
    if __i == 3 and __os.path.exists(__cache):
        __G["SESS"] = __pickle.load(open(__cache, "rb"))
    else:
        exec(compile("".join(__c["source"]), f"cell{__i}", "exec"), __G)
    print(f"##### cell {__i} took {__time.time()-__t:.0f}s", flush=True)
EOF
date -u && PY=executed/sabatini-2024/.venv/bin/python && N=$(python3 -c "import json;print(len(json.load(open('reproduce_sabatini_2024_stable_units.ipynb'))['cells']))") && PYTHONPATH=. timeout 3000 $PY $TMPDIR/runcells.py reproduce_sabatini_2024_stable_units.ipynb $(seq -s, 1 $((N-1))) > $TMPDIR/stable.log 2>&1; echo exit $?; date -u; tail -5 $TMPDIR/stable.log
```

```
Fri Nov 20 17:58:29 UTC 2026
exit 0
Fri Nov 20 18:18:21 UTC 2026
   kernel, trial averages, z-scored, 100 ms smoothing: mean 0.173 against LDR 0.697 (2120 trials); two-sided signed-rank p 1.3e-301; median difference +0.589; check on training-condition trials 0.216
   kernel, single trials, 6000 points, 100 ms smoothing: mean 0.506 against LDR 0.697 (2120 trials); two-sided signed-rank p 2.5e-144; median difference +0.184; check on training-condition trials 0.802
kinematic reading (a): LDR higher with p < 0.001 in 24 of 24 comparisons with the main decoders (raw rates, 3000 points; GPFA decoders not run)
kinematic reading (b): LDR higher with p < 0.001 in 24 of 24 comparisons with the main decoders (raw rates, 3000 points; GPFA decoders not run)
##### cell 91 took 0s
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF' > cmp.txt
import json,re
st=json.load(open('entries/sabatini-2024/reproduce_sabatini_2024_stable_units.ipynb'))
mn=json.load(open('executed/sabatini-2024/reproduce_sabatini_2024.ipynb'))
log=open('stable.log').read()
parts=re.split(r'##### cell (\d+)\n', log)
out={}
for k in range(1,len(parts),2):
    out[int(parts[k])]=re.sub(r'##### cell \d+ took \d+s\n','',parts[k+1])
def tag(c): 
    t=[x for x in c['metadata'].get('tags',[]) if x.startswith('claim:')]; return t[0] if t else None
mo={}
for c in mn['cells']:
    if tag(c): mo.setdefault(tag(c),[]).append(''.join(''.join(o.get('text','')) for o in c.get('outputs',[])))
so={}
for i,c in enumerate(st['cells']):
    if tag(c): so.setdefault(tag(c),[]).append(out.get(i,''))
for t in mo:
    a='\n'.join(mo[t]).splitlines(); b='\n'.join(so.get(t,[])).splitlines()
    print("########", t)
    for x in b:
        if x not in a and ('PMd-J' in x or 'M1-N' in x or not re.match(r'^(M1-J|PMd-N)',x)):
            print("  S:", x[:400])
EOF
wc -l cmp.txt; head -c 20000 cmp.txt
```

```
227 cmp.txt
######## claim:data-composition
######## claim:fig2c-condition-lds-variance
  S: PMd-J: held-out VE by k {1: np.float64(0.477), 3: np.float64(0.789), 5: np.float64(0.807), 7: np.float64(0.796), 9: np.float64(0.785), 11: np.float64(0.775), 13: np.float64(0.767), 15: np.float64(0.761), 17: np.float64(0.757), 19: np.float64(0.753), 21: np.float64(0.75)}
  S:    chosen k 5 (even split) | 5 (3/4 split) ; LDS VE mean 0.911 s.d. 0.036 range 0.814-0.961 | at k=5: mean 0.911
  S: M1-N: held-out VE by k {1: np.float64(0.375), 3: np.float64(0.81), 5: np.float64(0.87), 7: np.float64(0.878), 9: np.float64(0.874), 11: np.float64(0.869), 13: np.float64(0.864), 15: np.float64(0.86), 17: np.float64(0.858), 19: np.float64(0.855), 21: np.float64(0.854)}
  S:    chosen k 7 (even split) | 7 (3/4 split) ; LDS VE mean 0.945 s.d. 0.035 range 0.804-0.976 | at k=7: mean 0.945
  S: PMd-J chosen k under the four other seeds: []
  S: M1-N chosen k under the four other seeds: []
######## claim:fig3a-eigenvalue-clusters
  S:    median frequency of pair rank 1..2 (Hz): [0.55 1.55] (conditions: [72, 72]); within 10% of 0.5,1.5,2.5,4: [np.False_, np.True_]
  S:    all eigenvalue frequencies: range 0.00-2.23 Hz; |eigenvalue| range 0.959-0.999
  S:    median frequency of pair rank 1..3 (Hz): [0.68 1.76 3.21] (conditions: [72, 72, 71]); within 10% of 0.5,1.5,2.5,4: [np.False_, np.False_, np.False_]
######## claim:fig3c-eigenvalue-distance-auc
  S: PMd-J null (a): AUC 0.705 (unfolded 0.705); median distance between conditions 0.0117, noise 0.0073 | code's norm variant AUC 0.707
  S: PMd-J null (b): AUC 0.670 (unfolded 0.670); median distance between conditions 0.0117, noise 0.0082 | code's norm variant AUC 0.673
  S: M1-N null (a): AUC 0.634 (unfolded 0.634); median distance between conditions 0.0166, noise 0.0126 | code's norm variant AUC 0.636
  S: M1-N null (b): AUC 0.689 (unfolded 0.689); median distance between conditions 0.0166, noise 0.0115 | code's norm variant AUC 0.686
  S: PMd-J n
[... 137 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/claim:fig7c-ldr-encoding/,$p' $TMPDIR/cmp.txt | cut -c1-330
```

```
######## claim:fig7c-ldr-encoding
  S: kinematic reading (a) M1-J: linear mean 0.777 s.d. 0.067 (null 0.650, signed-rank p 2.0e-13; other seeds []) | kernel mean 0.855 s.d. 0.044 (null 0.539, p 1.9e-13; other seeds []) | variant, kernel length scale 1e2 0.855, 1e4 0.855
  S: kinematic reading (a) PMd-J: linear mean 0.690 s.d. 0.192 (null 0.588, signed-rank p 3.0e-08; other seeds []) | kernel mean 0.864 s.d. 0.076 (null 0.454, p 2.0e-13; other seeds []) | variant, kernel length scale 1e2 0.862, 1e4 0.864
  S: kinematic reading (a) M1-N: linear mean 0.850 s.d. 0.058 (null 0.642, signed-rank p 1.7e-13; other seeds []) | kernel mean 0.927 s.d. 0.026 (null 0.532, p 1.7e-13; other seeds []) | variant, kernel length scale 1e2 0.927, 1e4 0.927
  S: kinematic reading (a) PMd-N: linear mean 0.736 s.d. 0.132 (null 0.577, signed-rank p 2.0e-12; other seeds []) | kernel mean 0.878 s.d. 0.052 (null 0.451, p 1.7e-13; other seeds []) | variant, kernel length scale 1e2 0.878, 1e4 0.878
  S: kinematic reading (b) M1-J: linear mean 0.778 s.d. 0.067 (null 0.650, signed-rank p 1.7e-13; other seeds []) | kernel mean 0.857 s.d. 0.041 (null 0.537, p 2.0e-13; other seeds []) | variant, kernel length scale 1e2 0.857, 1e4 0.857
  S: kinematic reading (b) PMd-J: linear mean 0.690 s.d. 0.194 (null 0.587, signed-rank p 2.4e-08; other seeds []) | kernel mean 0.869 s.d. 0.066 (null 0.450, p 1.9e-13; other seeds []) | variant, kernel length scale 1e2 0.868, 1e4 0.869
  S: kinematic reading (b) M1-N: linear mean 0.851 s.d. 0.057 (null 0.642, signed-rank p 1.7e-13; other seeds []) | kernel mean 0.927 s.d. 0.027 (null 0.530, p 1.7e-13; other seeds []) | variant, kernel length scale 1e2 0.926, 1e4 0.927
  S: kinematic reading (b) PMd-N: linear mean 0.737 s.d. 0.131 (null 0.577, signed-rank p 1.5e-12; other seeds []) | kernel mean 0.877 s.d. 0.055 (null 0.450, p 1.7e-13; other seeds []) | variant, kernel length scale 1e2 0.877, 1e4 0.877
######## claim:suppfig7a-not-memorization
  S: kinematic reading (
[... 64 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "id: fig6e-kinematics-predict-location" -A30 claims/sabatini-2024.yaml | grep -n "criterion\|expected" -A8 | head -40; grep -n "rule for ranges\|partially by" claims/sabatini-2024.yaml | head -5
```

```
6:578-    cross-validation), greater than expected by chance (shuffle, p < 0.001). Allowing nonlinearities
7-579-    via kernel regression raised the variance explained to 69–81% of the variance in state space
8-580-    (6-fold cross-validation; shuffle, p < 0.001).
9-581-  statistics:
10-582-  - about: linear regression against shuffle
11-583-    test: shuffle
12-584-    p: 0.001
13-585-    p_relation: "<"
14-586-  - about: kernel regression against shuffle
--
20:592-  criterion: Reach parameters per condition are the least-squares coefficients of hand x and y
21-593-    position over -350 to +850 ms on two kinematic basis functions (Methods, Extracting kinematic
22-594-    basis functions; code predictDataUsingTBFandKinCondStructure.m). The basis functions
23-595-    (kinFuncEval) are not in the code; readings are (a) the top two velocity singular vectors of
24-596-    an SVD over all conditions of the datasets, integrated to position; (b) their skew-normal and
25-597-    skew-normal-derivative fits (the Methods say the results were essentially identical). The
26-598-    code for this regression is not published; following LDR encoding, ridge regression (lambda
27-599-    0.1) with intercept from the four parameters to the offset column, 6 folds over conditions,
28-600-    variance explained in the offset column over held-out conditions. The kernel is open between
139:    conditions judged by the rule for ranges (6.3 to 13.2%); the s.d. across conditions is
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 600,615p claims/sabatini-2024.yaml
```

```
variance explained in the offset column over held-out conditions. The kernel is open between
    (a) the Ornstein-Uhlenbeck kernel, length scale 10^3, of the LDR encoder and (b) the Gaussian
    kernel, length scale 400, lambda 0.1, of the rotation predictions (Methods). Shuffle, reach
    parameters permuted across conditions; the paper gives no count, and 1000 permutations is a
    standard choice, the fewest that can give p < 0.001. Reproduced when, under one reading,
    every dataset's linear value lies in 33.3 to 78.1% and kernel value in 62.1 to 89.1%, both
    above all permutations.
- id: fig7c-ldr-encoding
  statement: Predicting each condition's loading matrix from four reach parameters and multiplying
    by the shared basis functions explained 60 to 78% of the population variance with a linear
    model and 71 to 87% with kernel regression, above chance.
  source: Results, Reach kinematics correlate with the dynamics of motor cortex activity, paragraphs
    3 and 4; Figure 7b, c
  quote: 'This linear LDR-encoding model explained most of the population variance: 60–78% (s.d.
    <22%, 6-fold cross-validation), greater than expected by chance (Wilcoxon signed-rank test, p <
    0.001). ... This nonlinear LDR encoding model explained 71–87% of the population variance (s.d.
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json,yaml
cl=yaml.safe_load(open('claims/sabatini-2024.yaml'))
for c in cl['claims']:
    if c['id'] in ('fig4b-plane-alignment','rotation-orientation-dimensionality','fig4c-subspace-excursion-angles','fig2c-condition-lds-variance','suppfig6b-location-dimensionality','fig6c-location-tracks-direction'):
        print(c['id'], '::', c.get('criterion'))
nb=json.load(open('executed/sabatini-2024/reproduce_sabatini_2024.ipynb'))
for c in nb['cells']:
    if 'claim:fig4c-subspace-excursion-angles' in c['metadata'].get('tags',[]):
        for o in c['outputs']:
            for l in ''.join(o.get('text','')).splitlines():
                if 'angles >45' in l: print(l[:120])
EOF
```

```
fig2c-condition-lds-variance :: Methods, Fitting dynamics to single conditions. Per condition a discrete-time LDS by reduced-rank regression from -150 to +850 ms, eigenvalue half-lives above 10 s cut to 10 s, simulated forward from the state at -150 ms; dimensionality by cross-validation over two trial partitions, 100 repeats, one k for all conditions of a dataset. The code (crossValidateDimensionalityConditions.m) tests odd k from 1 to 21 and splits trials 3/4 to 1/4; the Methods' even split is the main reading and the code's is a variant. Reproduced when every dataset's chosen dimensionality is 5 to 9 and its mean variance explained lies in 63.9 to 100% (rule for ranges).
fig4b-plane-alignment :: Alignment index as in the shared method for each ordered pair of different conditions and each rotation. Noise is the alignment index between loading matrices fitted by regression on the fixed basis to two random halves of a condition's trials (Methods, Measuring the across-condition alignment of rotations), 36 repeats (Methods); the code's 200 repeats (singleFrequencyOverlapControl.m) are a variant. The paper's AUC is per rotation; the range covers rotations and datasets. The Results name a Wilcoxon signed-rank test and do not say what is paired; readings are (a) per condition, its mean alignment with the other conditions against its mean noise alignment, signed-rank test over conditions; (b) the code's rank-sum test of the two unpaired distributions. Reproduced when every rotation in every dataset has AUC in 0.765 to 1 with observed alignment lower, and the test gives p < 0.001 under one reading; partially when at least half of the rotations do.
fig4c-subspace-excursion-angles :: Subspace excursion angles as in the Methods, computed to 25 dimensions (code subspaceExcursionAngles.m called with 25, angles from subspacea.m), the seed and sequence optimised as the code does. Per rotation and dataset, the count of excursion angles above 45 degrees. Reproduced when every coun
[... 14 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
nb=json.load(open('entries/sabatini-2024/reproduce_sabatini_2024.ipynb'))
for i,c in enumerate(nb['cells']):
    s=''.join(c['source'])
    if s.startswith('**Result') and any(k in s for k in ['Shuffling time bins','Recoverability is','four reach parameters linearly','LDR decoder','Decoders']):
        print(i, s, '\n')
EOF
```

```
36 **Result: partially reproduced.** Shuffling time bins lowers the variance explained to 42.2, 28.7, 41.9 and 42.1%, below the real data on all 72 conditions of every dataset (rank-sum p = 3.9e-25). Three of four lie in 31.5 to 50.6%; PMd-J (28.7%) is below, and stays below under the five seeds (28.7 to 29.1%) and under trial reading (b) (28.7%). 

38 **Result: partially reproduced.** Recoverability is 97.4, 98.0, 98.6 and 98.7%, within 81.9 to 100%, and above the shuffled data on every condition (rank-sum p = 3.9e-25). The chance level, now with the shuffled basis de-mixed as the real one is, is 89.5, 86.5, 89.1 and 89.6%, the same to three decimals as with the raw shuffled basis; only PMd-J lies in 56.7 to 88%. The five seeds move chance by less than 0.01. 

100 **Result: reproduced.** With the SVD kinematic basis (reading a), the four reach parameters linearly predict 55.5, 55.5, 70.5 and 41.5% of the variance of the location (within 33.3 to 78.1%), and OU kernel regression 73.0, 68.5, 88.7 and 77.9% (within 62.1 to 89.1%), both above all 1000 permutations. The four other seeds stay in range (OU 65.5 to 88.7%, linear 38.4 to 70.1%). The skew-normal basis (reading b) gives linear 41.6 to 70.5% and OU 69.3 to 89.1%. OU length scales of 1e2 and 1e4 change the kernel values by at most 0.002. The Gaussian kernel (reading b of the kernel) gives 32 to 55%, below the range. 

117 **Result: partially reproduced.** The LDR decoder explains on average 77.0, 74.4, 86.6 and 73.0% of the variance of single-trial hand position (SVD basis; medians 82 to 92%); M1-J and M1-N lie in 75.6 to 100%, PMd-J and PMd-N below. The skew-normal basis gives 72.5 to 86.0% with the same two in range, and trial reading (b) 73.4 to 87.4%, again two. Under the four other seeds PMd-J reaches 76.3% once and PMd-N 75.9% once, so two or three of four lie in range under every seed. 

125 **Result: partially reproduced.** The LDR decoder explains more of the single-trial hand position than each of the 
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cat > $TMPDIR/edit_text.py <<'PYEOF'
import json
P = 'entries/sabatini-2024/reproduce_sabatini_2024.ipynb'
nb = json.load(open(P)); C = nb['cells']
def find(prefix):
    h = [i for i, c in enumerate(C) if ''.join(c['source']).startswith(prefix)]
    assert len(h) == 1, (prefix, h); return h[0]
def rep(i, old, new):
    s = ''.join(C[i]['source']); assert old in s, (i, old[:70]); C[i]['source'] = s.replace(old, new).splitlines(keepends=True)

i = find('**Result: partially reproduced.** Shuffling time bins')
rep(i, "and under trial reading (b) (28.7%).",
    "and under trial reading (b) (28.7%). Shuffled over the span of the paper's code, the analysis window\n"
    "(scrambleTrials.m), the values are 42.0, 29.4, 41.9 and 42.1%, with PMd-J again below; without the\n"
    "unstable units (companion notebook) PMd-J is 28.7%.")
i = find('**Result: partially reproduced.** Recoverability is')
rep(i, "The five seeds move chance by less than 0.01.",
    "The five seeds move chance by less than 0.01, and shuffling over the code's span gives 89.9, 86.8, 89.5\n"
    "and 89.9%, again with only PMd-J in range.")
i = find('**Result: reproduced.** Under reading (a), same-frequency')
rep(i, "same-frequency alignment is higher than different-frequency alignment for all 20 rotation comparisons: the one-sided signed-rank test gives p at most 1.4e-12 and the Hodges-Lehmann estimate of the paired difference is positive in every comparison (+0.011 to +0.558).",
    "the paper's test finds same-frequency alignment higher than different-frequency alignment in all 20\n"
    "rotation comparisons: the one-sided signed-rank test gives p at most 1.4e-12, and the Hodges-Lehmann\n"
    "estimate of the paired difference is positive in every comparison (+0.011 to +0.558). The medians do\n"
    "not agree everywhere.")
i = find('**Result: reproduced.** With the SVD kinematic basis')
rep(i, "The four other seeds stay in range (OU 65.5 to 88.7%, linear 38.4 to 70.1%).",
    "Under the four other seeds the values stay in range (OU 65.5 to 87.1%, linear 38.4 to 70.1%).")
rep(i, "The Gaussian kernel (reading b of the kernel) gives 32 to 55%, below the range.",
    "The Gaussian kernel (reading b of the kernel) gives 32 to 55%, below the range. Without the unstable\n"
    "units (companion notebook `reproduce_sabatini_2024_stable_units.ipynb`), M1-N's kernel value is 90.9%\n"
    "under the SVD basis and 91.2% under the skew-normal basis, above 89.1%, so no reading has every\n"
    "dataset in range there; the record proposes partially reproduced on that ground.")
i = find('**Result: partially reproduced.** The LDR decoder explains more')
rep(i, "The GPFA decoders were not run,",
    "Without the unstable units (companion notebook) the M1-N decoders improve (kernel on single trials,\n"
    "100 ms, 77.8% against LDR 86.9%) and LDR still wins all 24 comparisons. The GPFA decoders were not run,")
i = find('## Summary')
rep(i, "not reproduced (clusters present; frequencies near 0.7, 1.6 to 2.4 Hz)",
    "not reproduced (clusters present; median pair frequencies 0.56 to 0.86, 1.55 to 2.38 and, in M1-N, 3.20 Hz)")
rep(i, "claims file, the Methods, and the code as the claims file reports it. Assumptions where the paper is\nsilent: the span of the time shuffle,",
    "claims file, the Methods, and the code as the claims file reports it. Assumptions where the paper is\n"
    "silent: the span of the time shuffle (the code's span, the analysis window, is run as a variant and\n"
    "gives the same outcomes),")
rep(i, "no EMG, so suppfig8 removes the kinematic dimensions only. The GPFA decoders were not run.",
    "no EMG, so suppfig8 removes the kinematic dimensions only. The GPFA decoders were not run. The main\n"
    "analyses keep every unit of the dandiset; the companion notebook\n"
    "`reproduce_sabatini_2024_stable_units.ipynb` leaves out the three units that \"Unit checks\" finds are\n"
    "not one stable unit's, and gives the same outcome for every claim except\n"
    "fig6e-kinematics-predict-location, where M1-N's kernel value (90.9%) rises above its range.")
s = ''.join(C[i]['source'])
a = s.index("**What was found about the dataset.**")
s = s[:a] + """**What was found about the dataset.** The Nitschke file joins five recording segments whose clocks
overlap: trial start times, hand timestamps and every unit's spike times jump backwards four times, so
spike times are not sorted and a trial's spikes cannot be found by time alone. Assigning each trial to
its segment in file order gives condition decoding well above chance in segments 0 to 3 and at chance
with the previous trial's labels, so the alignment within segments is consistent with the trial table.
Within segment 3, decoding is 0.18 against 0.44 to 0.50 in segments 0 to 2, while a decoder trained on
the other segments reaches 0.49 there. One M1 unit (170) explains this: it fires at a mean of 175
spikes/s in segment 3 against 28 to 40 in the others, above 100 spikes/s on 229 of its 532 trials,
and without it decoding within segment 3 is 0.43. The per-trial summed rates of the segments have
similar ranges. In the Jenkins file, unit 0's spike train stops at 4259.0 s, and 55 ms later the first
of two runs in unit 1's row begins: 196608 spikes to the end of the session, sharing 0.4% of its times
with unit 1's own run (which spans the whole session), with refractory violations only when the two are
merged, and sharing exact times with other units' trains as unit 0 does. Unit 1's row thus holds what
appears to be the rest of unit 0's train. Hand position is stored as "meters" with a conversion of NaN,
but its values are in millimetres (reaches of about 130). The units table has one unit per electrode on
all 192 electrodes of each file and no quality, sorting or single/multi-unit column.
"""
C[i]['source'] = s.splitlines(keepends=True)
json.dump(nb, open(P, 'w'), indent=1, ensure_ascii=False); open(P, 'a').write('\n')
print('ok')
PYEOF
python3 $TMPDIR/edit_text.py
```

```
ok
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && python3 - <<'EOF'
p='ldr.py'; s=open(p).read()
old='''    f.close()
    out["most_shared_with_other_unit"] = best
    out["ends_before_a_run"] = ends'''
new='''    # for a unit that ends just before a run, the same measure of sharing as for the runs
    for k, (e, n, a, b) in enumerate(ends):
        se = u["spike_times"][a0[e]:sidx[e]]
        top = max((float(np.isin(se, u["spike_times"][a0[o]:sidx[o]]).mean()), o)
                  for o in range(len(sidx)) if o not in (e, unit))
        ends[k] = (e, n, a, b, top)
    f.close()
    out["most_shared_with_other_unit"] = best
    out["ends_before_a_run"] = ends'''
assert old in s; s=s.replace(old,new)
s=s.replace('''    unit's train, with that unit, and the other units whose train ends within 1 s before a run
    starts (unit, spikes, first and last time)."""''','''    unit's train, with that unit, and the other units whose train ends within 1 s before a run
    starts (unit, spikes, first and last time, and the largest fraction of its times found exactly
    in a third unit's train, with that unit)."""''')
open(p,'w').write(s)
import json
P='reproduce_sabatini_2024.ipynb'; nb=json.load(open(P)); C=nb['cells']
def fix(i, old, new):
    t=''.join(C[i]['source']); assert old in t, (i, old); C[i]['source']=t.replace(old,new).splitlines(keepends=True)
fix(11, '''    for o, n, a, b in rep["ends_before_a_run"]:
        print(f"   unit {o} ({SESS[m]['area'][o]}): {n} spikes from {a:.1f} to {b:.1f} s, ending "
              f"{(min(r[1] for r in rep['runs'] if r[1] > b) - b) * 1000:.0f} ms before a run of unit {un} starts")''',
'''    for o, n, a, b, (fr, o3) in rep["ends_before_a_run"]:
        print(f"   unit {o} ({SESS[m]['area'][o]}): {n} spikes from {a:.1f} to {b:.1f} s, ending "
              f"{(min(r[1] for r in rep['runs'] if r[1] > b) - b) * 1000:.0f} ms before a run of unit {un} starts; "
              f"largest fraction of its times found exactly in another unit's train {fr:.3f} (unit {o3})")''')
fix(10, '''pre-processing). Two units of the dandiset are neither. In the Jenkins file one unit's spike train
holds two sorted runs one after the other; the cell prints each run's size and span, the spike times
they share, intervals under 1 ms, and how many of each run's times are found exactly in another
unit's train.''', '''pre-processing). Three units of the dandiset are not one stable unit's. In the Jenkins file one unit's
spike train holds two sorted runs one after the other; the cell prints each run's size and span, the
spike times they share, intervals under 1 ms, how many of each run's times are found exactly in another
unit's train, and any unit whose train ends just before a run begins.''')
fix(10, "notebook `reproduce_sabatini_2024_stable_units.ipynb` leaves both units out.",
    "notebook `reproduce_sabatini_2024_stable_units.ipynb` leaves out the units the cell lists (`DROP`).")
json.dump(nb, open(P,'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
EOF
sed -i 's/^This notebook is `reproduce_sabatini_2024.ipynb` with two parameters changed in its first code cell: `EXCLUDE_UNSTABLE = True` (the units that "Unit checks" finds are not one stable unit.s are left out: in the Jenkins file units 0 and 1, whose spike trains are split between their rows, and in the Nitschke file unit 170, which fires at about 400 spikes\/s on 229 trials of segment 3) and `FULL_SEEDS = False` (each claim.s own seed only)./This notebook is `reproduce_sabatini_2024.ipynb` with one parameter changed in its first code cell: `EXCLUDE_UNSTABLE = True`, so that the units that "Unit checks" finds are not one stable unit'"'"'s are left out (in the Jenkins file units 0 and 1, whose spike trains are split between their rows, and in the Nitschke file unit 170, which fires above 100 spikes\/s on 229 trials of segment 3). It runs the five seeds of each claim, as the main notebook does./' $TMPDIR/make_companions.py
sed -i "s/make(HEAD_S, \[('EXCLUDE_UNSTABLE = False\\\\n', 'EXCLUDE_UNSTABLE = True\\\\n'), ('FULL_SEEDS = True\\\\n', 'FULL_SEEDS = False\\\\n')\],/make(HEAD_S, [('EXCLUDE_UNSTABLE = False\\\\n', 'EXCLUDE_UNSTABLE = True\\\\n')],/" $TMPDIR/make_companions.py
grep -n "HEAD_S = \|^This notebook\|make(HEAD_S" $TMPDIR/make_companions.py | cut -c1-200
```

```
6:HEAD_S = """# Sabatini & Kaufman (2024) on DANDI:000070: stable units only
8:This notebook is `reproduce_sabatini_2024.ipynb` with one parameter changed in its first code cell: `EXCLUDE_UNSTABLE = True`, so that the units that "Unit checks" finds are not one stable unit's ar
36:make(HEAD_S, [('EXCLUDE_UNSTABLE = False\n', 'EXCLUDE_UNSTABLE = True\n')],
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
P='reproduce_sabatini_2024.ipynb'; nb=json.load(open(P)); C=nb['cells']
def fix(i, old, new):
    t=''.join(C[i]['source']); assert old in t, (i, old); C[i]['source']=t.replace(old,new).splitlines(keepends=True)
fix(0, 'units whose spike trains are not one stable unit\'s (see "Unit checks"), with each claim\'s own seed only.',
       'units whose spike trains are not one stable unit\'s (see "Unit checks"), with the five seeds of each claim.')
fix(1, "# is this notebook with EXCLUDE_UNSTABLE = True and FULL_SEEDS = False.", "# is this notebook with EXCLUDE_UNSTABLE = True.")
json.dump(nb, open(P,'w'), indent=1, ensure_ascii=False); open(P,'a').write('\n')
EOF
python3 $TMPDIR/make_companions.py && date -u && PY=executed/sabatini-2024/.venv/bin/python && PYTHONPATH=. timeout 900 $PY $TMPDIR/runcells.py reproduce_sabatini_2024.ipynb 1,3,7,9,11 2>&1 | sed -n '/cell 11$/,$p' | head -12; date -u
```

```
entries/sabatini-2024/reproduce_sabatini_2024_trials_b.ipynb 92
entries/sabatini-2024/reproduce_sabatini_2024_stable_units.ipynb 92
Fri Nov 20 18:20:17 UTC 2026
##### cell 11
entries/sabatini-2024/ldr.py:293: RuntimeWarning: divide by zero encountered in divide
  return B.max(0) / np.median(B, 0)
J unit 1 (PMd), one recording segment: runs (spikes, first s, last s) [(196608, 4259.1, 15668.6), (264946, 4.7, 15668.6)]
   spike times found in both runs: 1049; intervals under 1 ms: merged train 0.0354, each run [0.0, 0.0]
   largest fraction of each run's times found exactly in another unit's train (fraction, unit): [(0.374, 68), (0.025, 64)]
   unit 0 (PMd): 61030 spikes from 4.9 to 4259.0 s, ending 55 ms before a run of unit 1 starts; largest fraction of its times found exactly in another unit's train 0.279 (unit 68)
J segment 0: 1595 trials; per-trial rate summed over units, -100 to +300 ms (spikes/s), percentiles 0/5/50/95/100: [6937, 8280, 10027, 12424, 15752]
N segment 0: 533 trials; per-trial rate summed over units, -100 to +300 ms (spikes/s), percentiles 0/5/50/95/100: [7517, 8886, 10243, 11675, 14651]
N segment 1: 510 trials; per-trial rate summed over units, -100 to +300 ms (spikes/s), percentiles 0/5/50/95/100: [8180, 9310, 10592, 12036, 14042]
N segment 2: 521 trials; per-trial rate summed over units, -100 to +300 ms (spikes/s), percentiles 0/5/50/95/100: [8190, 9631, 10678, 12596, 14627]
N segment 3: 532 trials; per-trial rate summed over units, -100 to +300 ms (spikes/s), percentiles 0/5/50/95/100: [8168, 9431, 10794, 12270, 14008]
Fri Nov 20 18:20:52 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='ldr.py'; s=open(p).read()
old="    return B.max(0) / np.median(B, 0)"
new="    with np.errstate(divide=\"ignore\"):  # a unit silent in most blocks gets an infinite ratio\n        return B.max(0) / np.median(B, 0)"
assert old in s; open(p,'w').write(s.replace(old,new))
p='entry.yaml'; s=open(p).read()
old="""  runtime_minutes: 15
helpers:"""
new="""  runtime_minutes: 15
- path: reproduce_sabatini_2024_stable_units.ipynb
  title: The same analyses without the units that are not one stable unit's
  runtime_minutes: 25
helpers:"""
assert old in s; open(p,'w').write(s.replace(old,new))
p='README.md'; s=open(p).read()
old="""with a delay above 400 ms, the claims file's other reading, and every outcome is the same."""
new="""with a delay above 400 ms, the claims file's other reading, and every outcome is the same.
`reproduce_sabatini_2024_stable_units.ipynb` leaves out three units whose spike trains are not one stable
unit's (in the Jenkins file, unit 0's train continues in unit 1's row; in the Nitschke file, unit 170 fires
above 100 spikes/s on 229 trials of one segment), and every outcome is the same except
fig6e-kinematics-predict-location, for which the record proposes a change."""
assert old in s; s=s.replace(old,new)
old="""position and the two notebooks take about 25 and 15 minutes."""
new="""position and the three notebooks take about 25, 15 and 25 minutes."""
assert old in s; s=s.replace(old,new)
old="""sorted units; the Nitschke file joins five recording segments whose clocks overlap."""
new="""sorted units; the Nitschke file joins five recording segments whose clocks overlap, and in the Jenkins
file one unit's spike train continues in the next unit's row."""
assert old in s; s=s.replace(old,new)
open(p,'w').write(s)
EOF
grep -n "README\|readme" tools/entry.py | head -5; cat README.md | sed -n 1,40p | tail -22
```

```
|---|---|
| Reproduced | 11 claims, among them the factorization's variance explained, the misalignment of rotational planes across conditions, the segregation of frequencies, prediction of rotations from each other and from the location, and LDR encoding against standard encoding models |
| Partially reproduced | 12 claims, among them LDR decoding, the time-shuffle control, and the comparison with instantaneous decoders, run without the GPFA decoders |
| Not reproduced | 11 claims, among them the eigenvalue frequencies and distances, the basis frequencies, the single-LDS fit, the dimensionality of rotation orientations and location, and the warping control |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and
the differences from the paper's method.

The dandiset's units are one per electrode, with no single- or multi-unit label, where the paper used
sorted units; the Nitschke file joins five recording segments whose clocks overlap, and in the Jenkins
file one unit's spike train continues in the next unit's row. The main notebook
uses all successful trials; `reproduce_sabatini_2024_trials_b.ipynb` runs the same analyses on trials
with a delay above 400 ms, the claims file's other reading, and every outcome is the same.
`reproduce_sabatini_2024_stable_units.ipynb` leaves out three units whose spike trains are not one stable
unit's (in the Jenkins file, unit 0's train continues in unit 1's row; in the Nitschke file, unit 170 fires
above 100 spikes/s on 229 trials of one segment), and every outcome is the same except
fig6e-kinematics-predict-location, for which the record proposes a change. The attempt record,
with the reasons, the differences from the paper's method and the findings about the dataset, is
[`attempts/sabatini-2024-01.yaml`](../../attempts/sabatini-2024-01.yaml).

[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && date -u && timeout 7000 python tools/entry.py all entries/sabatini-2024 > $TMPDIR/all.log 2>&1; echo exit $?; date -u; tail -30 $TMPDIR/all.log
```

```
Fri Nov 20 18:21:04 UTC 2026
exit 0
Fri Nov 20 20:01:43 UTC 2026
Installed kernelspec registry-sabatini-2024 in executed/sabatini-2024/.venv/share/jupyter/kernels/registry-sabatini-2024
0 error(s)
pass  reproduce_sabatini_2024.ipynb  (2335 s)
pass  reproduce_sabatini_2024_trials_b.ipynb  (1380 s)
pass  reproduce_sabatini_2024_stable_units.ipynb  (2311 s)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
def outs(p, tag):
    nb=json.load(open(p)); r=[]
    for c in nb['cells']:
        if tag in c['metadata'].get('tags',[]): r.append(''.join(''.join(o.get('text','')) for o in c.get('outputs',[])))
    return '\n'.join(r)
m='executed/sabatini-2024/reproduce_sabatini_2024.ipynb'; s='executed/sabatini-2024/reproduce_sabatini_2024_stable_units.ipynb'
print(outs(m,'claim:tbf-shuffle-control')[:600])
print(outs(m,'claim:fig6e-kinematics-predict-location')[:300])
print("STABLE fig6e"); print(outs(s,'claim:fig6e-kinematics-predict-location'))
nb=json.load(open(m))
for c in nb['cells']:
    if c['cell_type']=='code':
        for o in c.get('outputs',[]):
            if o.get('output_type')=='error': print("ERROR", o)
EOF
```

```
M1-J: shuffled VE mean 0.422 s.d. 0.019 (real 0.941); rank-sum p 3.91e-25; signed-rank (variant) p 1.66e-13; real higher on 72/72
   variant, shuffled over the code's span (-350 to +850 ms): mean 0.420 s.d. 0.018; rank-sum p 3.91e-25; real higher on 72/72
   shuffled mean under the five seeds: [np.float64(0.4222), np.float64(0.4165), np.float64(0.4183), np.float64(0.4167), np.float64(0.4186)]
PMd-J: shuffled VE mean 0.287 s.d. 0.018 (real 0.943); rank-sum p 3.91e-25; signed-rank (variant) p 1.66e-13; real higher on 72/72
   variant, shuffled over the code's span (-350 to +850 ms): mean 0.294 s
M1-J kinematic reading (a): linear 0.555 (null max -0.000, p 0.0010; other seeds [0.557 0.547 0.554 0.55 ]) | kernel OU 0.730 (null max -0.186, p 0.0010; other seeds [0.738 0.718 0.723 0.721]) | kernel Gaussian 0.422 (null max 0.040, p 0.0010; other seeds [0.416 0.42  0.415 0.423])
   variant, OU le
STABLE fig6e
M1-J kinematic reading (a): linear 0.555 (null max -0.000, p 0.0010; other seeds [0.557 0.547 0.554 0.55 ]) | kernel OU 0.730 (null max -0.186, p 0.0010; other seeds [0.738 0.718 0.723 0.721]) | kernel Gaussian 0.422 (null max 0.040, p 0.0010; other seeds [0.416 0.42  0.415 0.423])
   variant, OU length scale 1e2: 0.728; 1e4: 0.730
M1-J kinematic reading (b): linear 0.554 (null max 0.001, p 0.0010; other seeds [0.557 0.546 0.554 0.548]) | kernel OU 0.741 (null max -0.181, p 0.0010; other seeds [0.749 0.729 0.738 0.736]) | kernel Gaussian 0.435 (null max 0.039, p 0.0010; other seeds [0.432 0.434 0.43  0.437])
   variant, OU length scale 1e2: 0.740; 1e4: 0.741
PMd-J kinematic reading (a): linear 0.560 (null max 0.033, p 0.0010; other seeds [0.564 0.555 0.552 0.555]) | kernel OU 0.687 (null max -0.140, p 0.0010; other seeds [0.693 0.657 0.681 0.673]) | kernel Gaussian 0.437 (null max 0.038, p 0.0010; other seeds [0.436 0.435 0.431 0.44 ])
   variant, OU length scale 1e2: 0.687; 1e4: 0.687
PMd-J kinematic reading (b): linear 0.559 (null max 0.034, p 0.0010; other seeds [0.
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n '"proposed"' -A25 schemas/attempt.schema.json | head -40; grep -n "claim: tbf-shuffle-control\|claim: fig3h-recoverability\|claim: fig6e-kinematics\|claim: fig7f-decoder-beats\|claim: fig5a\|claim: data-composition\|claim: fig7c-ldr-encoding" attempts/sabatini-2024-01.yaml
```

```
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
331-                  "blocked"
332-                ]
333-              },
334-              "blocked_by": {
335-                "description": "Required when outcome is blocked.",
336-                "enum": [
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/sabatini-2024-01.yaml",
 "offset": 1,
 "limit": 300
}
```

```
1	schema_version: 3
2	id: sabatini-2024-01
3	datasets:
4	- archive: dandi
5	  id: '000070'
6	  version: 0.260528.0919
7	  doi: 10.48324/dandi.000070/0.260528.0919
8	  relation: reuses
9	paper: doi:10.1038/s41467-024-51308-7
10	date: 2026-11-20
11	entry: sabatini-2024
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-18
20	  runner:
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/sabatini-2024-01.yaml'; s=open(p).read()
old="""  - Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label, where
    the paper used 79 to 118 sorted single and stable multi-units.
"""
new="""  - Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label, where
    the paper used 79 to 118 sorted single and stable multi-units. All are kept, including three that
    are not one stable unit's (Jenkins units 0 and 1, whose train is split between their rows, and Nitschke
    unit 170, above 100 spikes/s on 229 trials of segment 3); reproduce_sabatini_2024_stable_units.ipynb
    leaves them out, and its outcome is the same.
"""
n=s.count(old); print(n); s=s.replace(old,new)
open(p,'w').write(s)
EOF
grep -n "claim: fig6e-kinematics-predict-location" -A30 attempts/sabatini-2024-01.yaml | head -34
```

```
34
682:- claim: fig6e-kinematics-predict-location
683-  outcome: reproduced
684-  notebook: reproduce_sabatini_2024.ipynb
685-  output: claim:fig6e-kinematics-predict-location
686-  assumed: true
687-  notes: Kinematic reading (a) (SVD basis), linear 55.5, 55.5, 70.5, 41.5% (in 33.3 to 78.1%); OU kernel
688-    73.0, 68.5, 88.7, 77.9% (in 62.1 to 89.1%); both above all 1000 permutations (p = 0.001). Reading
689-    (b) (skew-normal basis) gives linear 41.6 to 70.5% and OU 69.3 to 89.1%, also all in range. The Gaussian
690-    kernel (kernel reading b) gives 32.1 to 54.6%, below the range. Five seeds give OU 71.8 to 73.8 (M1-J),
691-    65.5 to 69.1, 86.7 to 88.7 and 74.0 to 77.9%, all in range. OU length scales of 1e2 and 1e4 change
692-    the kernel values by at most 0.002, so the unpublished scale of the kinematic basis does not matter
693-    here.
694-  deviations:
695-  - Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label, where
696-    the paper used 79 to 118 sorted single and stable multi-units. All are kept, including three that
697-    are not one stable unit's (Jenkins units 0 and 1, whose train is split between their rows, and Nitschke
698-    unit 170, above 100 spikes/s on 229 trials of segment 3); reproduce_sabatini_2024_stable_units.ipynb
699-    leaves them out, and its outcome is the same.
700-  - Trials are all successful trials of the 72 conditions (trial reading (a) of the claims file), an assumption.
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/sabatini-2024-01.yaml'; s=open(p).read()
a=s.index("- claim: fig6e-kinematics-predict-location\n  outcome: reproduced")
b=s.index("- claim: fig7c-ldr-encoding", a)
seg=s[a:b]
seg=seg.replace("""    the kernel values by at most 0.002, so the unpublished scale of the kinematic basis does not matter
    here.
""","""    the kernel values by at most 0.002, so the unpublished scale of the kinematic basis does not matter
    here. Without the three units that are not one stable unit's (reproduce_sabatini_2024_stable_units.ipynb),
    M1-N's OU kernel value is 90.9% under the SVD basis (89.2 to 90.9% over the five seeds) and 91.2%
    under the skew-normal basis (89.3 to 91.2%), above 89.1%; the other values stay in range (linear 41.5
    to 71.5%, OU 68.7 to 77.9% elsewhere).
""")
seg=seg.replace("""    leaves them out, and its outcome is the same.
""","""    leaves them out, and there M1-N's kernel value lies above its range (see proposed).
""")
seg=seg.replace("""  assumed: true
  notes: Kinematic reading (a)""","""  assumed: true
  proposed:
    outcome: partially_reproduced
    reason: The paper used single-units and stable multi-units (Methods, Subjects, behavior and data pre-processing).
      Leaving out the three units of the dandiset that are not one stable unit's, found after round 2
      in answer to the verifier's point on segment 3, M1-N's OU kernel value rises to 90.9% (SVD basis)
      and 91.2% (skew-normal basis), above 62.1 to 89.1%, under all five seeds (89.2 to 90.9%), while the
      Gaussian kernel stays below its range; no reading then has every dataset in range. The effect is
      present and the other values are in range, so the claim holds in part. The analysis is the companion
      notebook reproduce_sabatini_2024_stable_units.ipynb, cell tagged claim:fig6e-kinematics-predict-location.
  notes: Kinematic reading (a)""")
s=s[:a]+seg+s[b:]
open(p,'w').write(s)
EOF
grep -n "claim: fig7f-decoder-beats-standard" -A16 attempts/sabatini-2024-01.yaml | head -18
```

```
832:- claim: fig7f-decoder-beats-standard
833-  outcome: partially_reproduced
834-  notebook: reproduce_sabatini_2024.ipynb
835-  output: claim:fig7f-decoder-beats-standard
836-  assumed: true
837-  notes: Against 24 instantaneous decoders (ridge, lambda 1, on single trials; OU kernel, length scale
838-    100, L2 0.1, on single trials or trial averages; rates in spikes/s smoothed at 20 or 100 ms, 100 ms
839-    lag; six per dataset), the LDR decoder is higher in every comparison with two-sided signed-rank p
840-    at most 3e-127, scored over the same window (-250 to +850 ms; LDR 73.8, 70.8, 84.7, 69.7%). The instantaneous
841-    decoders explain 0.0 to 74.7% (the best, M1-N kernel on single trials at 100 ms). On trials of their
842-    own training conditions they explain 0.0 to 86.9% (the trial-average kernel decoders 0.0 to 18.6%),
843-    so as configured they are weak decoders. Z-scored rates and a 6000-point training set (variants) give
844-    0.4 to 78.0% and the same outcome, as does the LDR decoder under kinematic reading (b) and trial reading
845-    (b). The GPFA decoders were not run, so the claim holds against all but them, which the criterion
846-    counts as partial.
847-  deviations:
848-  - Units are the dandiset's 96 per-electrode units per array, with no single or multi-unit label, where
--
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/sabatini-2024-01.yaml'; s=open(p).read()
def rep(old,new):
    global s; assert s.count(old)==1, old[:80]; s=s.replace(old,new)
rep("""    (b). The GPFA decoders were not run, so the claim holds against all but them, which the criterion
    counts as partial.
""","""    (b). On trials of their training conditions the kernel decoders on trial averages at 20 ms explain
    0.000 to 0.018 and the linear decoders at 20 ms 0.021 to 0.176, so these baselines test little. Without
    the three units that are not one stable unit's (companion notebook) the M1-N decoders improve (kernel
    on single trials at 100 ms 77.8% against LDR 86.9%), and LDR still wins all 24 comparisons. The GPFA
    decoders were not run, so the claim holds against all but them, which the criterion counts as partial.
""")
rep("""    shuffled means vary by at most 0.008 (PMd-J 0.287 to 0.291); trial reading (b) gives PMd-J 0.287.
""","""    shuffled means vary by at most 0.008 (PMd-J 0.287 to 0.291); trial reading (b) gives PMd-J 0.287.
    Shuffled over the span of the paper's code, the analysis window (-350 to +850 ms), the values are 42.0,
    29.4, 41.9 and 42.1%, PMd-J again below; without the three units that are not one stable unit's, PMd-J
    is 28.7%.
""")
rep("""  - Time bins are permuted within the 1.5 s window read around movement onset (-500 to +1001 ms), with
    one permutation for all units of a trial so that correlations between units are kept (Methods, Control
    for data smoothing, "preserving inter-neuron spike correlations"); the span shuffled is not given
    and is an assumption. A longer span would lower the shuffled value, a shorter one raise it.
""","""  - Time bins are permuted within the 1.5 s window read around movement onset (-500 to +1001 ms), with
    one permutation for all units of a trial so that correlations between units are kept (Methods, Control
    for data smoothing, "preserving inter-neuron spike correlations"); the Methods do not give the span,
    and this span is an assumption. The paper's code permutes all columns of a trial's 1 ms matrix (scrambleTrials.m)
    and then smooths and keeps every tenth column of the same matrix (preprocessTrials.m), so its span
    is the analysis window, -350 to +850 ms; that span is run as a variant under the claim's seed and
    gives the same outcome.
""")
rep("""    than the paper's. Trial reading (b) gives chance 86.0 to 89.7%, again only PMd-J in range.
""","""    than the paper's. Trial reading (b) gives chance 86.0 to 89.7%, again only PMd-J in range. Shuffled
    over the span of the paper's code (-350 to +850 ms, scrambleTrials.m), chance is 89.9, 86.8, 89.5 and
    89.9%, again only PMd-J in range.
""")
open(p,'w').write(s)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json,re
nb=json.load(open('executed/sabatini-2024/reproduce_sabatini_2024.ipynb'))
for c in nb['cells']:
    if 'claim:fig7f-decoder-beats-standard' in c['metadata'].get('tags',[]):
        t=''.join(''.join(o.get('text','')) for o in c['outputs'])
        for l in t.splitlines():
            if ('trial averages, 20 ms' in l and 'z-scored' not in l) or ('linear, single trials' in l and '20 ms' in l) or 'LDR decoder over' in l: print(l[:60], '...', l[-45:])
EOF
```

```
M1-J: LDR decoder over -250..+850 ms mean 0.738 (over -350.. ... +850 ms mean 0.738 (over -350..+850 ms 0.770)
   linear, single trials, 20 ms smoothing: mean 0.019 agains ... 803; check on training-condition trials 0.031
   linear, single trials, z-scored, 20 ms smoothing: mean 0. ... 803; check on training-condition trials 0.031
   kernel, trial averages, 20 ms smoothing: mean 0.000 again ... 822; check on training-condition trials 0.001
PMd-J: LDR decoder over -250..+850 ms mean 0.708 (over -350. ... +850 ms mean 0.708 (over -350..+850 ms 0.744)
   linear, single trials, 20 ms smoothing: mean 0.030 agains ... 761; check on training-condition trials 0.046
   linear, single trials, z-scored, 20 ms smoothing: mean 0. ... 761; check on training-condition trials 0.046
   kernel, trial averages, 20 ms smoothing: mean 0.000 again ... 799; check on training-condition trials 0.000
M1-N: LDR decoder over -250..+850 ms mean 0.847 (over -350.. ... +850 ms mean 0.847 (over -350..+850 ms 0.866)
   linear, single trials, 20 ms smoothing: mean 0.144 agains ... 740; check on training-condition trials 0.176
   linear, single trials, z-scored, 20 ms smoothing: mean 0. ... 740; check on training-condition trials 0.176
   kernel, trial averages, 20 ms smoothing: mean 0.000 again ... 904; check on training-condition trials 0.000
PMd-N: LDR decoder over -250..+850 ms mean 0.697 (over -350. ... +850 ms mean 0.697 (over -350..+850 ms 0.730)
   linear, single trials, 20 ms smoothing: mean 0.013 agains ... 782; check on training-condition trials 0.021
   linear, single trials, z-scored, 20 ms smoothing: mean 0. ... 782; check on training-condition trials 0.021
   kernel, trial averages, 20 ms smoothing: mean 0.000 again ... 796; check on training-condition trials 0.000
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
nb=json.load(open('executed/sabatini-2024/reproduce_sabatini_2024.ipynb'))
for c in nb['cells']:
    if 'claim:fig7f-decoder-beats-standard' in c['metadata'].get('tags',[]):
        t=''.join(''.join(o.get('text','')) for o in c['outputs'])
        print([l[-6:] for l in t.splitlines() if 'trial averages, z-scored, 20 ms' in l])
EOF
date -u
```

```
[' 0.018', ' 0.004', ' 0.060', ' 0.029']
Fri Nov 20 20:02:40 UTC 2026
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/sabatini-2024-01.yaml'; s=open(p).read()
old="""conditions the kernel decoders on trial averages at 20 ms explain
    0.000 to 0.018 and the linear decoders at 20 ms 0.021 to 0.176,"""
assert old in s
s=s.replace(old,"""conditions the kernel decoders on trial averages at 20 ms explain
    0.000 to 0.001 (0.004 to 0.060 with z-scored rates) and the linear decoders at 20 ms 0.021 to 0.176,""")
open(p,'w').write(s)
EOF
sed -n '/^findings:/,/^verifications:/p' attempts/sabatini-2024-01.yaml | head -30
```

```
findings:
- kind: format_error
  about: data
  severity: major
  statement: The Nitschke file (sub-Nitschke_ses-20100923) joins five recording segments whose clocks
    overlap. Trial start times, hand timestamps and every unit's spike times jump backwards four times
    (segments span 5 to 6076 s, 6074 to 12077 s, 6071 to 12494 s, 6120 to 13516 s and 6074 to 6658 s),
    so spike times are not sorted and a trial's spikes cannot be selected by time alone; doing so mixes
    spikes of up to four segments. Splitting each unit's spikes at the jumps and assigning trials to segments
    in file order gives condition decoding of 0.44 to 0.50 in segments 0 to 2 and 0.18 in segment 3 (all
    successful trials; chance 0.014; 0.010 to 0.024 with the previous trial's labels).
- kind: metadata_insufficient
  about: data
  severity: major
  statement: The units table holds 96 units per array, exactly one on each of the 192 electrodes, in both
    files. Its columns are electrode_group, electrodes, id, obs_intervals and spike_times, with no column
    for single or multi-unit, sorting quality or isolation. The paper reports 79 to 118 single and stable
    multi-units per array. Whether these units are threshold crossings or sorted units merged per electrode
    is not stated.
- kind: format_error
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/sabatini-2024-01.yaml'; s=open(p).read()
def rep(old,new):
    global s; assert s.count(old)==1, old[:80]; s=s.replace(old,new)
rep("""- kind: format_error
  about: data
  severity: major
  statement: The Nitschke file (sub-Nitschke_ses-20100923) joins five recording segments whose clocks
    overlap. Trial start times, hand timestamps and every unit's spike times jump backwards four times
    (segments span 5 to 6076 s, 6074 to 12077 s, 6071 to 12494 s, 6120 to 13516 s and 6074 to 6658 s),""",
"""- kind: format_error
  about: data
  severity: critical
  statement: The Nitschke file (sub-Nitschke_ses-20100923) joins five recording segments whose clocks
    overlap, and no metadata says so. Trial start times, hand timestamps and every unit's spike times jump
    backwards four times (hand timestamps span 5.4 to 6075.4 s, 6074.2 to 12075.9 s, 6070.6 to 12493.5
    s, 6119.8 to 13515.2 s and 6073.5 to 6656.8 s),""")
rep("""- kind: format_error
  about: data
  severity: minor
  statement: In the Jenkins file, one unit's spike train (the second row of the units table) holds two
    sorted runs one after the other, the second restarting at 4.7 s after the first reached 15668.6 s.
    The two runs were merged and sorted here.""",
"""- kind: format_error
  about: data
  severity: critical
  statement: In the Jenkins file (sub-Jenkins_ses-20090918), unit 1's row of the units table holds two
    sorted spike trains one after the other. The first, 196608 spikes from 4259.1 to 15668.6 s, begins
    55 ms after unit 0's train, which holds 61030 spikes from 4.9 s, stops at 4259.0 s. The second, 264946
    spikes from 4.7 to 15668.6 s, spans the session as the other units do. The two share 1049 spike times;
    neither has intervals under 1 ms, while merged 3.5% of intervals are. Of the first run's times 37.4%
    are found exactly in another unit's train (unit 68), as are 27.9% of unit 0's, against at most 2.5%
    for the second run. Unit 1's row thus appears to hold the rest of unit 0's train after 4259 s, and
    unit 0's row is cut short. Nothing but the unsorted order of unit 1's spike times shows it; merging
    the two runs, as the main analyses do, gives unit 1 a train with another unit's spikes. The companion
    notebook leaves units 0 and 1 out.""")
rep("""- kind: other
  about: data
  severity: minor
  statement: In the Nitschke file, condition information in segment 3 is lower within the segment (decoding
    0.179) than in segments 0 to 2 (0.445 to 0.495), while a decoder trained on the other segments reaches
    0.491 on it, and decoding does not peak at another time offset. This is consistent with a change of
    the recorded units over the session; segment 4 (24 trials) is too small to check on its own.""",
"""- kind: other
  about: data
  severity: major
  statement: In the Nitschke file, one M1 unit (unit 170) fires at a mean of 175.2 spikes/s in segment
    3, above 100 spikes/s on 229 of its 532 trials (trials starting 6446 to 10006 s on that segment's
    clock), against means of 27.6 to 40.4 spikes/s and no such trial in the other segments. Its ratio
    of largest to median mean rate over blocks of 50 trials is 13.7, against at most 2.5 for the other
    units of the file. Nothing in the file marks it. It lowers condition decoding within segment 3 to
    0.179, against 0.445 to 0.495 in segments 0 to 2; without it, decoding within segment 3 is 0.425.
    The per-trial rates summed over units have similar ranges in all segments. The companion notebook
    leaves this unit out.""")
open(p,'w').write(s)
EOF
echo ok
```

```
ok
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import yaml
d=yaml.safe_load(open('attempts/sabatini-2024-01.yaml'))
for o in d['outcomes']: print(o['claim'], o['outcome'], o.get('assumed'))
print(len(d['findings']))
for i,f in enumerate(d['findings'],1): print(i, f['kind'], f.get('severity'))
EOF
grep -o "trials above 100 spikes/s start from [0-9]* to [0-9]*" executed/sabatini-2024/reproduce_sabatini_2024.ipynb
```

```
data-composition reproduced None
jpca-fit-r2 partially_reproduced True
jpca-variance-explained partially_reproduced True
single-lds-variance not_reproduced True
fig2c-condition-lds-variance reproduced True
fig3a-eigenvalue-clusters not_reproduced True
fig3c-eigenvalue-distance-auc not_reproduced True
suppfig2-eigenvalues-from-kinematics not_reproduced True
fig3g-basis-frequencies not_reproduced True
tbf-variance-explained reproduced True
tbf-shuffle-control partially_reproduced True
fig3h-recoverability partially_reproduced True
fig3i-duration-warping not_reproduced True
suppfig3-model-comparison not_reproduced True
fig4b-plane-alignment reproduced True
fig4c-subspace-excursion-angles partially_reproduced True
rotation-orientation-dimensionality not_reproduced True
fig4d-jpca-variance-correlation not_reproduced True
fig4f-plane-alignment-explains-jpca partially_reproduced True
fig5a-frequencies-segregated reproduced True
[... 24 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/sabatini-2024-01.yaml'; s=open(p).read()
old="(6) Over what span were time bins shuffled\n    in the control for data smoothing?"
if old not in s:
    import re; i=s.index("(6) "); print(repr(s[i-5:i+120]))
else:
    s=s.replace(old,"(6) Did the trial matrices shuffled in the control\n    for data smoothing span the analysis window, as preprocessTrials.m implies?"); open(p,'w').write(s); print("done")
EOF
```

```
done
```

**Agent**

Now the round-2 verification block.

**Agent calls Bash**

```bash
cat > $TMPDIR/round2.py <<'PYEOF'
import yaml
p = 'attempts/sabatini-2024-01.yaml'
d = yaml.safe_load(open(p))
GEN = ("I agree with the outcome. It rests mainly on trial reading (a), all successful trials, which is stated "
       "in every deviation and is reasonable, and the companion notebook runs reading (b) with the same outcome.")
GEN_R = ("No change to the outcome. The units deviation now names the three units that are not one stable unit's; "
         "the companion notebook reproduce_sabatini_2024_stable_units.ipynb leaves them out and gives the same outcome.")
R = {
 'data-composition': ("I agree with the outcome; it carries no assumption. Remaining: whether the units are sorted is "
    "unknown, since the files have no sort or quality column (cell 5).",
    "No change; the units remain unlabelled, kept as finding 2. The unit checks now also show three units that are not "
    "one stable unit's (findings 3 and 6)."),
 'tbf-shuffle-control': ("I agree with the outcome. The shuffle span is stated as an assumption, but no other span was "
    "run, and PMd-J's 28.7% against 31.5% may depend on it.",
    "The paper's code fixes the span: scrambleTrials.m permutes all columns of a trial's 1 ms matrix, and preprocessTrials.m "
    "smooths and down-samples that same matrix, so the span is the analysis window. That span is now run as a variant "
    "(42.0, 29.4, 41.9 and 42.1%), with PMd-J again below 31.5%; outcome unchanged. Notes, deviation, Result cell and the "
    "question to the authors updated."),
 'fig3h-recoverability': (GEN, "Chance under the code's shuffle span is now printed (89.9, 86.8, 89.5 and 89.9%), again "
    "only PMd-J in range; outcome unchanged."),
 'fig3a-eigenvalue-clusters': (GEN + " Summary (cell 124), fig3a row, \"frequencies near 0.7, 1.6 to 2.4 Hz\": the "
    "first-pair medians are 0.56-0.86 Hz, and M1-N's third pair at 3.20 Hz is left out.",
    "Summary row corrected to the printed medians (0.56 to 0.86, 1.55 to 2.38 and, in M1-N, 3.20 Hz). Outcome unchanged."),
 'fig4c-subspace-excursion-angles': ("I agree with the outcome. The noise SEA as chance is stated, and now compares like "
    "with like.", GEN_R),
 'fig7c-standard-encoding-worse': ("I agree with the outcome. No kernel penalty is stated and reasonable; the 0.1 penalty "
    "variant still predicts only the mean.", GEN_R),
 'fig6e-kinematics-predict-location': ("I agree with the outcome. The scale of the kinematic basis is stated, and length "
    "scales of 1e2 and 1e4 change values by at most 0.002 (cells 97, 104, 106). Cell 98, \"The four other seeds stay in "
    "range (OU 65.5 to 88.7% ...)\": the other seeds reach at most 87.1%; 88.7% is the claim's own seed.",
    "Cell corrected (OU 65.5 to 87.1% under the four other seeds). The outcome stays reproduced, as verified. Without the "
    "three units that are not one stable unit's, M1-N's kernel value rises to 90.9% (89.2 to 90.9% over five seeds), above "
    "89.1%; a change to partially reproduced is proposed under `proposed` for a third round."),
 'fig7c-ldr-encoding': ("I agree with the outcome. The scale of the kinematic basis is stated, and length scales of 1e2 "
    "and 1e4 change values by at most 0.002.", GEN_R),
 'suppfig7a-not-memorization': ("I agree with the outcome. The scale of the kinematic basis is stated, and length scales "
    "of 1e2 and 1e4 change values by at most 0.002.", GEN_R),
 'fig5a-frequencies-segregated': ("I agree with the outcome. It meets the criterion's letter, with one-sided p <= 1.4e-12 "
    "and positive Hodges-Lehmann estimates (cell 63). For M1-N 3.24 Hz, however, the same-frequency median is lower (0.183 "
    "against 0.197 and 0.198), it is higher on only 49-50% of pairs, and the rank-sum p is 0.31 and 0.29. The notes say "
    "so. Cell 64, \"same-frequency alignment is higher ... for all 20 rotation comparisons\", holds for M1-N 3.24 Hz only "
    "in mean and Hodges-Lehmann terms.",
    "Cell 64 reworded: the paper's test finds same-frequency alignment higher in all 20 comparisons, and the medians do not "
    "agree everywhere; the next sentence gives the M1-N numbers. Outcome unchanged."),
 'fig7f-decoder-beats-standard': ("I agree with the label, but the baselines barely work. On trials of their own training "
    "conditions the kernel decoders on trial averages at 20 ms score 0.000-0.018 and the linear decoders at 20 ms "
    "0.021-0.176. The OU length scale of 100 in spikes/s pushes the kernel towards the training mean when tested on single "
    "trials (cell 122). The record calls the decoders weak, which is fair, but the comparison shows little beyond that. "
    "The GPFA decoders were not run.",
    "Not fixed: the length scale of 100 is the paper's, and the GPFA decoders were not run in this revision. The notes now "
    "give the baselines' scores on training-condition trials and say that these baselines test little. Without the "
    "unstable units the M1-N decoders improve (kernel on single trials at 100 ms 77.8% against LDR 86.9%), and LDR still "
    "wins all 24 comparisons. Outcome unchanged."),
 'suppfig3-model-comparison': (GEN + " B11: the outcome depends on how the claims file is read; it has been sent to a "
    "reader as a question.", "No change; the question stays open in questions/sabatini-2024.yaml."),
 'jpca-fit-r2': (GEN + " The jPCA port's fidelity to the codepack is still unchecked.",
    "Not checked in this revision: the paper's code loads files available only on request, so the port could not be "
    "compared on the same input. Outcome unchanged; the units deviation updated as for every claim."),
 'jpca-variance-explained': (GEN + " The jPCA port's fidelity to the codepack is still unchecked.",
    "Not checked in this revision, as for jpca-fit-r2. Outcome unchanged; the units deviation updated as for every claim."),
}
res = []
for o in d['outcomes']:
    c = o['claim']
    reason, resp = R.get(c, (GEN, GEN_R))
    res.append(dict(claim=c, agrees=True, outcome=o['outcome'], reason=reason, response=resp))
F = [
 dict(finding=1, agrees=False, severity='critical',
      reason=("Rated major; I would rate it critical. Cell 5 shows what it states: hand timestamps in five segments with "
              "overlapping bounds, all 192 units with four backward spike-time jumps, and trial start times that are not "
              "monotonic. Cell 9 shows that assigning trials to segments in file order works. This is signals on different "
              "clocks within one file, and no metadata says so. An analysis that takes the times as given and selects a "
              "trial's spikes by time silently mixes up to four recordings. The segment bounds 6076, 12077, 13516 and 6658 s "
              "are not printed; cell 5 prints 6075.4, 12075.9, 13515.2 and 6656.8."),
      response="Severity changed from major to critical, the verifier's rating. The bounds now quote the printed values."),
 dict(finding=3, agrees=False, severity='critical',
      reason=("Rated minor; this cannot be judged from the outputs. Cell 5 shows only one unit with one backward jump. If "
              "the second run holds another unit's spikes, or duplicates the first, it is a spike train holding another "
              "unit's spikes, which is critical. The notebook merges the two runs. Printing each run's spike count, and "
              "whether the two runs overlap or repeat each other, would settle it. \"The second row\", \"4.7 s\" and "
              "\"15668.6 s\" are not printed."),
      response=("The unit checks now print both runs (196608 spikes from 4259.1 s and 264946 from 4.7 s, both to 15668.6 "
                "s), the 1049 times they share, the intervals under 1 ms (none in either run, 3.5% merged), and the "
                "largest share of each run's times found in another unit's train (37.4% and 2.5%). They also show that "
                "unit 0's train stops at 4259.0 s, 55 ms before the first run begins, with the same sharing (27.9%). "
                "Unit 1's row holds what appears to be the rest of unit 0's train, so the finding is rewritten and rated "
                "critical, as the verifier's condition gives. The companion notebook leaves units 0 and 1 out.")),
]
d['verifications'].append(dict(
    date='2026-11-20', kind='agent',
    by='Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
    reviewed=("Round 2. The full executed notebook with its conclusions and summary, the companion notebook on trial "
              "reading (b), the helper module, the claims file and the attempt record, with the paper under paper/."),
    results=res, findings=F))
blk = yaml.safe_dump([d['verifications'][-1]], sort_keys=False, allow_unicode=True, width=110, default_flow_style=False)
open(p, 'a').write(blk)
print(blk[:600])
PYEOF
tail -c 200 attempts/sabatini-2024-01.yaml | od -c | tail -2; python3 $TMPDIR/round2.py && python3 -c "import yaml;d=yaml.safe_load(open('attempts/sabatini-2024-01.yaml'));print(len(d['verifications']), len(d['verifications'][-1]['results']))"
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
python tools/entry.py check entries/sabatini-2024 2>&1 | tail -15; date -u
```

```
0 error(s)
Fri Nov 20 20:03:51 UTC 2026
```

**Agent calls Bash**

```bash
grep -n "clean-run\|def stamp\|fingerprint\|sha256" tools/entry.py | head -20
```

```
30:A run that passes leaves a stamp beside the executed copies (.clean-run.json):
65:STAMP = ".clean-run.json"                 # beside the executed copies: what they were made from (entry_hash)
561:    return hashlib.sha256(path.read_bytes()).hexdigest()
569:    h = hashlib.sha256(f"run {RUN_VERSION}; harness {' '.join(HARNESS)}; python {python_of(entry_dir)}\n".encode())
589:            if not r["ok"] or r["seconds"] > max_minutes * 60 or file_hash(output_dir / r["notebook"]) != r["sha256"]:
648:                         "sha256": file_hash(output_dir / r["notebook"])} for r in results]}, indent=1) + "\n")
```

**Agent calls Bash**

```bash
sed -n 25,45p tools/entry.py; sed -n 560,600p tools/entry.py
```

```
`run` builds a fresh virtual environment from the lock file and executes each
notebook through a Jupyter kernel installed in that environment, in the entry
directory. The executed copies
go to --output-dir (default: executed/<name>/, which git ignores). A notebook
that takes longer than --max-minutes fails, even if it ran without error.
A run that passes leaves a stamp beside the executed copies (.clean-run.json):
a hash of everything the run read (`hash` prints it) and of each executed
copy. `run` asked again with nothing changed since reuses those copies and says
so, without executing anything; --fresh executes all the same.

`handover` builds what a verifier is given in its first round
(docs/protocol.md): the executed notebooks with the conclusions removed (every
markdown cell that begins "**Result:" and everything from the "## Summary"
heading on), the helper modules and the claims files, in
executed/<name>/handover/. Run the entry first.

Requires `uv` on PATH, and `pyyaml`, `jsonschema` and `nbformat` to run this
script itself. The entry's own dependencies come only from its lock file.
"""

[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "add_argument" tools/entry.py | head -20
```

```
698:    parser.add_argument("command", choices=["lock", "check", "run", "all", "handover", "upgrade-python", "hash"])
699:    parser.add_argument("entry", type=Path, nargs="+",
701:    parser.add_argument("--output-dir", type=Path, help="where executed notebooks go")
702:    parser.add_argument("--timeout", type=int, default=3600, help="seconds allowed per cell")
703:    parser.add_argument("--max-minutes", type=float, default=60,
705:    parser.add_argument("--fresh", action="store_true",
707:    parser.add_argument("--python", help="lock: the Python version to lock for (default: the entry's); "
709:    parser.add_argument("--before", type=Path, help="upgrade-python: the executed notebooks to compare with "
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import yaml, json, jsonschema
s=json.load(open('schemas/attempt.schema.json')); d=yaml.safe_load(open('attempts/sabatini-2024-01.yaml'))
jsonschema.validate(json.loads(json.dumps(d, default=str)), s); print("valid")
EOF
grep -n "attempts/" tools/entry.py | head -5; ls tools | head -30
```

```
valid
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
build_reuse_targets.py
build_site.py
build_sparc_targets.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
contributors.py
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
git diff attempts/ entries/ | grep "^+" | grep -n -i "—\|rather" | head; git status --short
```

```
M attempts/sabatini-2024-01.yaml
 M entries/sabatini-2024/README.md
 M entries/sabatini-2024/entry.yaml
 M entries/sabatini-2024/ldr.py
 M entries/sabatini-2024/reproduce_sabatini_2024.ipynb
 M entries/sabatini-2024/reproduce_sabatini_2024_trials_b.ipynb
 M tools/build_site.py
 M tools/entry.py
 M tools/site_assets/app.css
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
?? entries/sabatini-2024/reproduce_sabatini_2024_stable_units.ipynb
[... 1 more lines not kept]
```

**Agent**

I left all 34 outcomes as verified: 11 reproduced, 12 partially reproduced, 11 not reproduced. Two ratings went up to critical, and I proposed one outcome change for round 3. `python tools/entry.py all entries/sabatini-2024` ran from a clean environment and passed for all three notebooks, and `check` reports 0 errors. One wrong sentence remains in the notebook summary (see the end).

**Outcomes**
- **Proposed change (fig6e-kinematics-predict-location):** the verified outcome stays reproduced, with partially reproduced written under `proposed`. The cause is three bad units, described under Findings below, which the main analyses keep. A new companion notebook, `reproduce_sabatini_2024_stable_units.ipynb`, leaves them out. The paper used "single-units and stable multi-units". In that notebook, M1-N's kernel value is 90.9% (89.2 to 90.9% over the five seeds), above the 89.1% bound. That fig6e figure is the only outcome that changes there.
- **Shuffle span (tbf-shuffle-control):** the paper's code fixes it to the analysis window (`scrambleTrials.m` and `preprocessTrials.m`). I ran that span: shuffled values are 42.0, 29.4, 41.9 and 42.1%, and recoverability chance is 89.9, 86.8, 89.5 and 89.9%. PMd-J is still below its range, so neither outcome changes.

**Findings**
- **Finding 1 (overlapping clocks in the Nitschke file):** raised to critical, the verifier's rating. The segment bounds now quote the printed values.
- **Finding 3 (Jenkins unit 1):** the new output settles it, and it is now critical. Unit 0's spike train stops at 4259.0 s. 55 ms later the first of unit 1's two runs begins: 196,608 spikes running to the end of the session. The two runs share only 1,049 spike times. Neither run alone has intervals under 1 ms, but 3.5% of intervals are once merged. The first run matches other units' spike times the way unit 0 does (37.4% against 27.9%); the second run matches at most 2.5%. So unit 1's row appears to hold the rest of unit 0's train.
- **Finding 6 (segment 3):** rewritten and raised to major. It is not a change of the recorded units, as the old text said. One M1 unit (170) fires above 100 spikes/s on 229 of the 532 trials in segment 3. Without it, decoding within segment 3 rises from 0.179 to 0.425. The per-trial spike-count distributions the verifier asked for are printed and are similar across segments.

**Other corrections**
- Fixed the verifier's text slips in cell 64 (fig5a wording), cell 98 (four other seeds now 65.5 to 87.1%) and the fig3a row of the Summary.
- The fig7f-decoder-beats-standard notes now say the instantaneous baselines test little.
- Added round 2 under `verifications`: all 34 claims agreed, in the verifier's words, plus its review of findings 1 and 3.
- Also updated the units deviation on every outcome, the README, `entry.yaml`, and one of the questions to the paper's authors.

**Not done**
- **Wrong summary sentence:** the notebook Summary says unit 1's first run shares "0.4% of its times" with its own second run. The correct figure is 0.5% of the first run (1,049 of 196,608); 0.4% is the share of the second run. The full run takes 100 minutes and would not have finished before the 21:22 cutoff, so this was not corrected. The attempt record gives the correct count. It needs fixing in the next revision.
- GPFA decoders: not run.
- jPCA port fidelity: still unchecked, because the paper's code needs preprocessed files that are only available on request.
- The fig7f baselines keep the paper's length scale of 100.
- No new question for a reader: the verifier reported no new place where the claims file misreads the paper.

## End of run

91 turns, 171 minutes, $7.19 at API prices, result: success.
