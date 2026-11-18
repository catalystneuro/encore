# niknam-2019 · author-revise-1 · run 42971134002

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat transcripts/niknam-2019/verifier-1-report.md; ls entries/niknam-2019 entries/niknam-2019/*; ls questions | grep nik
```

```
Wed Nov 11 06:21:23 UTC 2026
**A. Outcomes**

| Claim | Outcome | Reason |
|---|---|---|
| probe-locations-link | reproduced | Cell 9: all 41 files match a probe_list row and no row lacks a file. The recomputed RF is the listed probe for 38 neurons and the listed probe or a neighbour for 41 of 41 (the threshold is 37). The sign of FF minus RF gives 27 left and 14 right. |
| methods-neuron-counts | reproduced | Cell 11: 41 neurons in 11 sessions; 27 neurons in 9 sessions go left and 14 in 2 sessions go right. All four counts are exact. The 49 to 41 selection cannot be tested because the 8 dropped neurons are not deposited. |
| fig1b-saccadic-suppression | reproduced | Cell 16, reading (b, i): count 8. Fixation is 2.235 against 2.53±0.37 and perisaccadic is 1.239 against 1.51±0.29, and the response drops. Both values sit near the edge of tolerance. Only about 5 of the 8 neurons are the authors' (35/41 agreement with nuron_list, cell 31). |
| fig1c-ff-remapping | not_reproduced | Cell 18, (b, i): count 8 against 23±2.3; 0.792 and 1.609 are both out of tolerance. The direction holds but no number does. |
| fig1d-st-remapping | not_reproduced | Cell 20, (b, i): count 11 against 37±3.7; 0.749 and 1.629 are out of tolerance. |
| fig1e-ff-and-st-remapping | not_reproduced | Cell 22, (b, i): count 6 against 22, with 0 of 5 numbers in tolerance. The partial rule needs at least 2. |
| fig1-remapping-longer-latency | reproduced | Cell 24: the fixation RF peak is at 62 ms, and the perisaccadic FF and ST peaks are at 108 and 99 ms under (b, i). Every other testable reading also stays inside 80-150 ms. The remapped peaks are partly forced by selecting neurons on an increase at 80-150 ms (problem 5). |
| fig1-example-neurons | partially_reproduced | Cell 26, onset reading: the FF (2015071702), ST (2015092707) and FF+ST (2015051115) examples match on values and on D2(b) p < 0.05. No neuron matches the RF example. The every-ms variant matches all four, but it does not decide. |
| fig
[... 45 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n '/## Author/,/## Verifier/p' docs/protocol.md | head -300; grep -n "Hand over\|^## \|^### " docs/protocol.md
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

[... 303 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 495,660p docs/protocol.md
```

```
and this protocol's version.

If any outcome is `not_reproduced` or `partially_reproduced`, the entry's
`README.md` and the notebook's summary carry this sentence: "A failure to
reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method."

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
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
ls attempts | grep nik; wc -l attempts/niknam-2019-01.yaml entries/niknam-2019/*; cat entries/niknam-2019/entry.yaml; ls claims | grep nik; ls questions/niknam* ; ls paper
```

```
niknam-2019-01.yaml
   473 attempts/niknam-2019-01.yaml
    26 entries/niknam-2019/README.md
    22 entries/niknam-2019/entry.yaml
   278 entries/niknam-2019/mt3.py
  1015 entries/niknam-2019/reproduce_niknam_2019.ipynb
     7 entries/niknam-2019/requirements.in
  1447 entries/niknam-2019/requirements.lock.txt
  3268 total
schema_version: 1
name: niknam-2019
type: reproduction
title: Perisaccadic responses of MT neurons (Niknam et al. 2019)
description: Tests the findings of Niknam, Akbarian, Clark, Zamani, Noudoost and Nategh (2019) on
  CRCNS mt-3, which holds the spike trains, probe sequences and saccade times of 41 MT neurons from
  11 sessions. It links the neurons to the RF, FF and ST probes listed in the paper's code, and
  tests the recorded saccadic suppression, FF- and ST-remapping of Figure 1. The model claims
  (S-, F-, A- and N-models, Figures 3 to 8) are blocked, with the cost of the S-model timed.
license: Apache-2.0
python: "3.13"
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cat entries/niknam-2019/mt3.py; cat attempts/niknam-2019-01.yaml
```

```
<persisted-output>
Output too large (40.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/491d4793-1618-4b9c-bd20-46cf3378b71e/tool-results/bgrflmn5a.txt

Preview (first 2KB):
"""Loading and response measures for CRCNS mt-3 (Niknam et al. 2019, PLoS Comput Biol).

The data set holds one MATLAB 7.3 file per MT neuron in ``data.zip`` (data descriptor,
"Data format"): ``stimcode`` (trial x ms, probe index 0-81, 0 = no probe), ``resp``
(trial x ms spikes, 1 ms bins), ``conds`` (condition per trial) and ``tsaccade``
(saccade onset per trial, ms from the start of the trial). The zip is streamed from the
public CRCNS bucket and opened in place; nothing is written to disk.

Where each parameter comes from:

- Probe index to grid position: ``[i, j] = ind2sub([9, 9], x)`` (data descriptor); the
  paper's code (``code2stim.m``) calls ``i`` x and ``j`` y.
- Saccade index: the paper's code reads the saccade-aligned samples as
  ``tsaccade(i) + times`` in MATLAB's 1-based indexing (``select_bases.m``), so the
  0-based index of saccade onset is ``tsaccade - 1``.
- Windows: fixation -500 to -100 ms, perisaccadic -30 to 0 ms (RF) and -50 to 0 ms (FF,
[... 15 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "entries/niknam-2019/mt3.py"
}
```

```
1	"""Loading and response measures for CRCNS mt-3 (Niknam et al. 2019, PLoS Comput Biol).
2	
3	The data set holds one MATLAB 7.3 file per MT neuron in ``data.zip`` (data descriptor,
4	"Data format"): ``stimcode`` (trial x ms, probe index 0-81, 0 = no probe), ``resp``
5	(trial x ms spikes, 1 ms bins), ``conds`` (condition per trial) and ``tsaccade``
6	(saccade onset per trial, ms from the start of the trial). The zip is streamed from the
7	public CRCNS bucket and opened in place; nothing is written to disk.
8	
9	Where each parameter comes from:
10	
11	- Probe index to grid position: ``[i, j] = ind2sub([9, 9], x)`` (data descriptor); the
12	  paper's code (``code2stim.m``) calls ``i`` x and ``j`` y.
13	- Saccade index: the paper's code reads the saccade-aligned samples as
14	  ``tsaccade(i) + times`` in MATLAB's 1-based indexing (``select_bases.m``), so the
15	  0-based index of saccade onset is ``tsaccade - 1``.
16	- Windows: fixation -500 to -100 ms, perisaccadic -30 to 0 ms (RF) and -50 to 0 ms (FF,
17	  ST) from saccade onset; early response 50-75 ms and late response 80-150 ms after probe
18	  onset (claims file D2; Methods, Statistical analysis of perisaccadic responses). Windows
19	  are taken inclusive at 1 ms, as ``get_mean_resp.m`` takes ``t:t+window``; a standard
20	  choice that cannot change a result beyond one bin.
[... 259 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "attempts/niknam-2019-01.yaml"
}
```

```
1	schema_version: 3
2	id: niknam-2019-01
3	datasets:
4	- archive: crcns
5	  id: mt-3
6	  version: unversioned
7	  doi: 10.6080/K0FB514J
8	  relation: primary
9	paper: doi:10.1371/journal.pcbi.1007275
10	date: '2026-11-11'
11	entry: niknam-2019
12	provenance:
13	  kind: agent
14	  accountable:
15	    name: CatalystNeuro
16	  agent:
17	    harness: Claude Code
18	    model: claude-opus-5-5
19	    protocol: pilot-14
20	  runner:
[... 454 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims; grep -n "" niknam-2019.yaml | sed -n 1,400p
```

```
1:# Claims for Niknam, Akbarian, Clark, Zamani, Noudoost & Nategh (2019), "Characterizing and
2:# dissociating multiple time-varying modulatory computations influencing neuronal activity",
3:# PLoS Comput Biol, doi:10.1371/journal.pcbi.1007275, tested on CRCNS:mt-3.
4:# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"),
5:# 2026-11-11, protocol pilot-14 as stated in docs/protocol.md.
6:#
7:# Text read. paper/10.1371-journal.pcbi.1007275.txt, the version of record (PMC6759185, open
8:# access, Europe PMC full-text XML flattened). It holds the abstract, Introduction, Results,
9:# Discussion, Methods, the legends of Figures 1 to 8, the legends of S1 to S6 Fig and S1 to S3
10:# Movie, and the Data Availability statement. No PDF was supplied, so no figure could be read.
11:# The supplement figures themselves are not in the text, only their legends; the numbers the
12:# results rest on are in the Results text and the legends, so the supplement's absence does not
13:# block a claim. Lost in extraction: every displayed equation (Eqs 1 to 14, including the
14:# parameter-selection threshold, Eq 10; the classification measures of the dichotomous analysis;
15:# the prevalence-map indicator m(t, tau); the maximum-detectability definition) and the whole
16:# reference list, so ref [48] (the N-model), ref [49] (the McNemar mid-P test) and ref [73]
17:# (Chen et al., algorithm 2) are known only by number.
18:#
19:# Code. https://github.com/nnategh/SFA-Models, commit 1438dde9dd3207348ec0df1e5c4dd2a7b014e68e
20:# (2019-12-20), linked in Methods (A-model framework) and Data Availability. MATLAB. It holds
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python - <<'EOF'
import json
nb=json.load(open('entries/niknam-2019/reproduce_niknam_2019.ipynb'))
for i,c in enumerate(nb['cells']):
    print('=====',i,c['cell_type'],c.get('metadata',{}).get('tags'))
    print(''.join(c['source']))
EOF
```

```
<persisted-output>
Output too large (37.6KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/491d4793-1618-4b9c-bd20-46cf3378b71e/tool-results/bm3yn1dph.txt

Preview (first 2KB):
===== 0 markdown None
# Niknam et al. (2019) on CRCNS mt-3

Paper: Niknam, Akbarian, Clark, Zamani, Noudoost and Nategh (2019), "Characterizing and dissociating
multiple time-varying modulatory computations influencing neuronal activity", PLoS Comput Biol,
doi:10.1371/journal.pcbi.1007275. The claims (`claims/niknam-2019.yaml`) were written from the
version of record (PMC6759185), its figure legends and the legends of its supplement.

Dataset: CRCNS mt-3 (doi:10.6080/K0FB514J), `mt-3/live/data.zip` in the public bucket
`crcnsarchive`, streamed and opened in place. CRCNS data sets are not versioned, so the version is
recorded as `unversioned` (docs/archives.md). The bucket holds one copy of the data (`live/`, no
`old/`), so there is no other version to choose; the data descriptor is version 0.6 of
2019-08-06, the only one, and describes these files. MD5 sums from the data set's `checksums.md5`:
`data.zip` a5f225a0b73d64b5e2d2f881e345752a (checked below against the bytes read),
`docs/crcns_mt-3_data_description.pdf` 0a3515c7d3a4a8aae3b0aded6daa3d7a.

[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/491d4793-1618-4b9c-bd20-46cf3378b71e/tool-results/bm3yn1dph.txt"
}
```

```
1	===== 0 markdown None
2	# Niknam et al. (2019) on CRCNS mt-3
3	
4	Paper: Niknam, Akbarian, Clark, Zamani, Noudoost and Nategh (2019), "Characterizing and dissociating
5	multiple time-varying modulatory computations influencing neuronal activity", PLoS Comput Biol,
6	doi:10.1371/journal.pcbi.1007275. The claims (`claims/niknam-2019.yaml`) were written from the
7	version of record (PMC6759185), its figure legends and the legends of its supplement.
8	
9	Dataset: CRCNS mt-3 (doi:10.6080/K0FB514J), `mt-3/live/data.zip` in the public bucket
10	`crcnsarchive`, streamed and opened in place. CRCNS data sets are not versioned, so the version is
11	recorded as `unversioned` (docs/archives.md). The bucket holds one copy of the data (`live/`, no
12	`old/`), so there is no other version to choose; the data descriptor is version 0.6 of
13	2019-08-06, the only one, and describes these files. MD5 sums from the data set's `checksums.md5`:
14	`data.zip` a5f225a0b73d64b5e2d2f881e345752a (checked below against the bytes read),
15	`docs/crcns_mt-3_data_description.pdf` 0a3515c7d3a4a8aae3b0aded6daa3d7a.
16	
17	Outside input (`with_labels`): `assets/data/main_lists.mat` of the paper's code,
18	https://github.com/nnategh/SFA-Models at commit 1438dde9dd3207348ec0df1e5c4dd2a7b014e68e, for
19	each neuron's RF, FF and ST probe (`probe_list`). Its other tables are shown for reference only.
20	
[... 591 more lines not kept]
```

**Agent calls Bash**

```bash
ls executed/niknam-2019/ 2>/dev/null; ls -a; python -c "import h5py, fsspec, scipy, pandas; print('ok')"; grep -n "venv\|def cmd_run\|uv " tools/entry.py | head -30
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
[... 46 more lines not kept]
```

**Agent**

First I'll run the entry as it stands, to get an environment to explore in.

**Agent calls Bash**

```bash
time python tools/entry.py all entries/niknam-2019 2>&1 | tail -15
```

```
Installed kernelspec registry-niknam-2019 in executed/niknam-2019/.venv/share/jupyter/kernels/registry-niknam-2019
0 error(s)
pass  reproduce_niknam_2019.ipynb  (55 s)

real	1m5.255s
user	0m49.838s
sys	0m5.704s
```

**Agent calls Bash**

```bash
cd entries/niknam-2019 && PY=../../executed/niknam-2019/.venv/bin/python; $PY - <<'EOF'
import pickle, os, mt3
zf=mt3.open_zip(); names=mt3.neuron_names(zf)
N=[mt3.load_neuron(zf,n) for n in names]
L=mt3.load_probe_list()
pickle.dump((N,{k:L[k] for k in L if not k.startswith('__')}),open(os.environ['TMPDIR']+'/nik.pkl','wb'))
print(len(N))
EOF
```

```
41
```

**Agent calls Bash**

```bash
cat > $TMPDIR/load.py <<'EOF'
import pickle, os, sys
sys.path.insert(0, 'entries/niknam-2019')
import numpy as np, mt3
N, L = pickle.load(open(os.environ['TMPDIR']+'/nik.pkl','rb'))
row_of = {(int(r[0]), int(r[1])): r for r in L['probe_list']}
byname = {d['name']: d for d in N}
def probes(d):
    r = row_of[(d['session'], d['channel'])]
    return {"RF": mt3.sub2ind(r[2], r[3]), "FF": mt3.sub2ind(r[4], r[5]), "ST": mt3.sub2ind(r[6], r[7])}
EOF
cd $TMPDIR && executed/niknam-2019/.venv/bin/python - <<'EOF'
exec(open('load.py').read())
EX=[("2015092709","RF",(50,75),60.89,(-30,0),40.49),("2015071702","FF",(80,150),7.90,(-50,0),18.42),
    ("2015092707","ST",(80,150),23.80,(-50,0),64.64),("2015051115","FF",(80,150),15.83,(-50,0),39.10),("2015051115","ST",(80,150),16.15,(-50,0),36.17)]
for mode in ("onset","every"):
  for nm,loc,win,ef,peri,ep in EX:
    d=byname[nm]; tr,t=mt3.presentations(d,probes(d)[loc],mode)
    c=mt3.counts(d,tr,t,win)*1000/(win[1]-win[0]+1)
    rel=t-d['sacc'][tr]
    per=(rel>=peri[0])&(rel<=peri[1])
    fix=(rel>=-500)&(rel<=-100)
    print(mode,nm,loc,'fix %.2f (paper %.2f) n=%d  peri %.2f (paper %.2f) n=%d'%(c[fix].mean(),ef,fix.sum(),c[per].mean(),ep,per.sum()))
    # scan
    best=[]
    for a in range(-700,-199,10):
      for b in range(-300,1,10):
        if b<=a: continue
        f=(rel>=a)&(rel<=b)
        best.append((abs(c[f].mean()-ef),a,b,c[f].mean()))
    best.sort(); print('   best windows',[(a,b,round(v,2)) for _,a,b,v in best[:6]])
EOF
```

```
onset 2015092709 RF fix 56.94 (paper 60.89) n=283  peri 40.49 (paper 40.49) n=19
   best windows [(-230, -190, np.float64(60.9)), (-370, -290, np.float64(60.9)), (-330, -110, np.float64(60.92)), (-390, -130, np.float64(60.86)), (-420, -230, np.float64(60.92)), (-370, -280, np.float64(60.85))]
onset 2015071702 FF fix 7.83 (paper 7.90) n=196  peri 18.96 (paper 18.42) n=26
   best windows [(-370, -230, np.float64(7.9)), (-700, -120, np.float64(7.9)), (-550, -60, np.float64(7.9)), (-450, -110, np.float64(7.9)), (-510, -80, np.float64(7.9)), (-700, -210, np.float64(7.9))]
onset 2015092707 ST fix 23.61 (paper 23.80) n=284  peri 64.64 (paper 64.64) n=39
   best windows [(-620, -120, np.float64(23.8)), (-260, -170, np.float64(23.8)), (-690, -250, np.float64(23.81)), (-690, -230, np.float64(23.79)), (-270, -210, np.float64(23.79)), (-570, -80, np.float64(23.81))]
onset 2015051115 FF fix 15.76 (paper 15.83) n=436  peri 39.10 (paper 39.10) n=67
   best windows [(-370, -100, np.float64(15.83)), (-640, -240, np.float64(15.83)), (-610, -200, np.float64(15.83)), (-430, -100, np.float64(15.83)), (-500, -90, np.float64(15.83)), (-600, -100, np.float64(15.84))]
onset 2015051115 ST fix 16.05 (paper 16.15) n=437  peri 36.17 (paper 36.17) n=81
   best windows [(-340, -120, np.float64(16.15)), (-600, -220, np.float64(16.15)), (-690, -170, np.float64(16.15)), (-360, -70, np.float64(16.15)), (-610, -170, np.float64(16.15)), (-580, -130, np.float64(16.15))]
every 2015092709 RF fix 38.44 (paper 60.89) n=2096  peri 33.82 (paper 40.49) n=141
   best windows [(-280, -260, np.float64(60.83)), (-250, -240, np.float64(61.97)), (-270, -240, np.float64(59.55)), (-270, -250, np.float64(58.97)), (-310, -300, np.float64(63.63)), (-270, -220, np.float64(56.92))]
every 2015071702 FF fix 7.92 (paper 7.90) n=1470  peri 18.51 (paper 18.42) n=191
   best windows [(-550, -80, np.float64(7.9)), (-700, -130, np.float64(7.9)), (-390, -280, np.float64(7.9)), (-370, -220, np.float64(7.9)), (-690, -230, np.float64(
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && for f in lib/get/get_mean_resp.m lib/get/get_info.m; do echo "=== $f"; curl -s https://raw.githubusercontent.com/nnategh/SFA-Models/1438dde9dd3207348ec0df1e5c4dd2a7b014e68e/$f; done; curl -s "https://api.github.com/repos/nnategh/SFA-Models/git/trees/1438dde9dd3207348ec0df1e5c4dd2a7b014e68e?recursive=1" | grep '"path"' | grep -v assets/data/20 | head -80
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && for f in lib/get/get_stim.m lib/get/get_resp.m lib/load/load_trials.m lib/load/load_data.m lib/load/code2stim.m lib/plot/plot_mean_resp.m; do echo "=== $f"; curl -s https://raw.githubusercontent.com/nnategh/SFA-Models/1438dde9dd3207348ec0df1e5c4dd2a7b014e68e/$f | grep -v "^ *%"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && executed/niknam-2019/.venv/bin/python - <<'EOF'
exec(open('load.py').read())
EX=[("2015092709","RF",(50,75),60.89,(-30,0),40.49),("2015071702","FF",(80,150),7.90,(-50,0),18.42),
    ("2015092707","ST",(80,150),23.80,(-50,0),64.64),("2015051115","FF",(80,150),15.83,(-50,0),39.10),("2015051115","ST",(80,150),16.15,(-50,0),36.17)]
def pres7(d,probe):
    on=d['stimcode']==probe
    start=on&~np.concatenate([np.zeros((on.shape[0],1),bool),on[:,:-1]],1)
    tr,t=np.nonzero(start)
    out=[]
    for a,b in zip(tr,t):
        L=0
        while b+L<on.shape[1] and on[a,b+L]: L+=1
        for k in range(0,L-3,7): out.append((a,b+k))
    out=np.array(out); keep=out[:,1]+150<on.shape[1]
    return out[keep,0],out[keep,1]
for nm,loc,win,ef,peri,ep in EX:
    d=byname[nm]
    for lab,(tr,t) in (("onset",mt3.presentations(d,probes(d)[loc])),("every7",pres7(d,probes(d)[loc]))):
        c=mt3.counts(d,tr,t,win)*1000/(win[1]-win[0]+1)
        rel=t-d['sacc'][tr]
        res=[]
        for off in (0,1,-1):
            r2=rel+off
            per=(r2>=peri[0])&(r2<=peri[1]); fix=(r2>=-500)&(r2<=-100)
            res.append('off%d fix %.2f peri %.2f'%(off,c[fix].mean(),c[per].mean()))
        # restrict to trials with sacc >= 540 and sacc+540 < 3000
        ok=(d['sacc'][tr]>=540)
        per=(rel>=peri[0])&(rel<=peri[1])&ok; fix=(rel>=-500)&(rel<=-100)&ok
        res.append('sacc>=540: fix %.2f peri %.2f'%(c[fix].mean(),c[per].mean()))
        print(nm,loc,lab,'paper',ef,ep,'|',' | '.join(res))
    print('  tsaccade range',d['tsaccade'].min(),d['tsaccade'].max(), 'trials',len(d['tsaccade']))
EOF
```

```
2015092709 RF onset paper 60.89 40.49 | off0 fix 56.94 peri 40.49 | off1 fix 56.88 peri 44.87 | off-1 fix 56.94 peri 33.94 | sacc>=540: fix 56.94 peri 40.49
2015092709 RF every7 paper 60.89 40.49 | off0 fix 55.09 peri 40.49 | off1 fix 55.04 peri 44.87 | off-1 fix 55.09 peri 33.94 | sacc>=540: fix 55.09 peri 40.49
  tsaccade range 913 1274 trials 437
2015071702 FF onset paper 7.9 18.42 | off0 fix 7.83 peri 18.96 | off1 fix 7.83 peri 18.78 | off-1 fix 7.83 peri 19.50 | sacc>=540: fix 7.83 peri 18.96
2015071702 FF every7 paper 7.9 18.42 | off0 fix 8.17 peri 18.26 | off1 fix 8.17 peri 18.78 | off-1 fix 8.17 peri 18.78 | sacc>=540: fix 8.17 peri 18.26
  tsaccade range 927 1275 trials 305
2015092707 ST onset paper 23.8 64.64 | off0 fix 23.61 peri 64.64 | off1 fix 23.61 peri 64.58 | off-1 fix 23.62 peri 63.90 | sacc>=540: fix 23.61 peri 64.64
2015092707 ST every7 paper 23.8 64.64 | off0 fix 23.56 peri 64.08 | off1 fix 23.56 peri 64.05 | off-1 fix 23.58 peri 63.38 | sacc>=540: fix 23.56 peri 64.08
  tsaccade range 913 1274 trials 437
2015051115 FF onset paper 15.83 39.1 | off0 fix 15.76 peri 39.10 | off1 fix 15.65 peri 38.94 | off-1 fix 15.76 peri 38.63 | sacc>=540: fix 15.76 peri 39.10
2015051115 FF every7 paper 15.83 39.1 | off0 fix 15.75 peri 38.26 | off1 fix 15.64 peri 38.12 | off-1 fix 15.75 peri 37.82 | sacc>=540: fix 15.75 peri 38.26
  tsaccade range 845 1271 trials 641
2015051115 ST onset paper 16.15 36.17 | off0 fix 16.05 peri 36.17 | off1 fix 16.05 peri 36.37 | off-1 fix 16.11 peri 36.82 | sacc>=540: fix 16.05 peri 36.17
2015051115 ST every7 paper 16.15 36.17 | off0 fix 15.74 peri 36.12 | off1 fix 15.74 peri 36.31 | off-1 fix 15.76 peri 36.75 | sacc>=540: fix 15.74 peri 36.12
  tsaccade range 845 1271 trials 641
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && executed/niknam-2019/.venv/bin/python - <<'EOF'
exec(open('load.py').read())
EX=[("2015092709","RF",(50,75),60.89,2.82,(-30,0),40.49),("2015071702","FF",(80,150),7.90,1.02,(-50,0),18.42),
    ("2015092707","ST",(80,150),23.80,1.77,(-50,0),64.64),("2015051115","FF",(80,150),15.83,.91,(-50,0),39.10),("2015051115","ST",(80,150),16.15,.94,(-50,0),36.17)]
for nm,loc,win,ef,se,peri,ep in EX:
    d=byname[nm]; tr,t=mt3.presentations(d,probes(d)[loc])
    c=mt3.counts(d,tr,t,win)*1000/(win[1]-win[0]+1)
    rel=t-d['sacc'][tr]
    fix=(rel>=-500)&(rel<=-100)
    out={}
    out['pooled']=(c[fix].mean(), c[fix].std(ddof=1)/np.sqrt(fix.sum()), fix.sum())
    for key,lab in ((tr,'trial'),(d['conds'][tr],'cond')):
        ks=np.unique(key[fix]); m=np.array([c[fix&(key==k)].mean() for k in ks])
        out[lab]=(m.mean(), m.std(ddof=1)/np.sqrt(len(m)), len(m))
    for b in (-150,-170,-200):
        f=(rel>=-500)&(rel<=b); out[f'-500..{b}']=(c[f].mean(), c[f].std(ddof=1)/np.sqrt(f.sum()),f.sum())
    for a in (-450,-400):
        f=(rel>=a)&(rel<=-100); out[f'{a}..-100']=(c[f].mean(), c[f].std(ddof=1)/np.sqrt(f.sum()),f.sum())
    # fixation = all presentations before -100 within aligned -540
    f=(rel>=-540)&(rel<=-100); out['-540..-100']=(c[f].mean(), c[f].std(ddof=1)/np.sqrt(f.sum()),f.sum())
    f=(rel<=-100); out['all<-100']=(c[f].mean(), c[f].std(ddof=1)/np.sqrt(f.sum()),f.sum())
    print(nm,loc,'paper %.2f±%.2f'%(ef,se))
    for k,v in out.items(): print('   %-12s %.2f ± %.2f  n=%d'%(k,*v))
EOF
```

```
2015092709 RF paper 60.89±2.82
   pooled       56.94 ± 2.71  n=283
   trial        56.94 ± 2.71  n=283
   cond         53.24 ± 3.61  n=78
   -500..-150   58.58 ± 2.93  n=239
   -500..-170   58.87 ± 3.03  n=228
   -500..-200   59.42 ± 3.17  n=211
   -450..-100   56.99 ± 2.92  n=245
   -400..-100   57.33 ± 3.09  n=214
   -540..-100   56.46 ± 2.62  n=312
   all<-100     49.69 ± 1.60  n=726
2015071702 FF paper 7.90±1.02
   pooled       7.83 ± 1.01  n=196
   trial        7.83 ± 1.01  n=196
   cond         7.47 ± 1.03  n=78
   -500..-150   6.64 ± 0.83  n=176
   -500..-170   6.67 ± 0.85  n=169
   -500..-200   6.69 ± 0.88  n=162
   -450..-100   8.18 ± 1.13  n=167
   -400..-100   8.89 ± 1.31  n=141
[... 36 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && executed/niknam-2019/.venv/bin/python - <<'EOF'
exec(open('load.py').read())
EX=[("2015092709","RF",(50,75),60.89,(-30,0)),("2015071702","FF",(80,150),7.90,(-50,0)),
    ("2015092707","ST",(80,150),23.80,(-50,0)),("2015051115","FF",(80,150),15.83,(-50,0)),("2015051115","ST",(80,150),16.15,(-50,0))]
pre=[]
for nm,loc,win,ef,peri in EX:
    d=byname[nm]; tr,t=mt3.presentations(d,probes(d)[loc])
    c=mt3.counts(d,tr,t,win)*1000/(win[1]-win[0]+1); rel=t-d['sacc'][tr]; pre.append((c,rel,ef))
res=[]
for a in range(-560,-440):
    for b in range(-160,-40):
        errs=[abs(c[(rel>=a)&(rel<=b)].mean()-ef) for c,rel,ef in pre]
        res.append((max(errs[1:]),a,b,[round(c[(rel>=a)&(rel<=b)].mean(),2) for c,rel,ef in pre]))
res.sort()
for r in res[:15]: print(r)
EOF
```

```
(np.float64(0.0544625264540608), -495, -100, [np.float64(57.14), np.float64(7.95), np.float64(23.79), np.float64(15.8), np.float64(16.12)])
(np.float64(0.061827748097780244), -497, -99, [np.float64(57.14), np.float64(7.91), np.float64(23.74), np.float64(15.77), np.float64(16.11)])
(np.float64(0.06568936555110483), -498, -99, [np.float64(57.14), np.float64(7.87), np.float64(23.74), np.float64(15.76), np.float64(16.11)])
(np.float64(0.07111100167437989), -495, -99, [np.float64(57.14), np.float64(7.91), np.float64(23.81), np.float64(15.76), np.float64(16.15)])
(np.float64(0.07111100167437989), -494, -99, [np.float64(57.14), np.float64(7.91), np.float64(23.84), np.float64(15.76), np.float64(16.09)])
(np.float64(0.07609629407651752), -498, -100, [np.float64(57.14), np.float64(7.91), np.float64(23.72), np.float64(15.8), np.float64(16.09)])
(np.float64(0.07609629407651752), -497, -100, [np.float64(57.14), np.float64(7.95), np.float64(23.72), np.float64(15.8), np.float64(16.09)])
(np.float64(0.07609629407651752), -494, -97, [np.float64(57.14), np.float64(7.91), np.float64(23.72), np.float64(15.78), np.float64(16.09)])
(np.float64(0.08375327340929672), -457, -99, [np.float64(56.54), np.float64(7.98), np.float64(23.78), np.float64(15.76), np.float64(16.07)])
(np.float64(0.08587330434217932), -494, -100, [np.float64(57.14), np.float64(7.95), np.float64(23.83), np.float64(15.8), np.float64(16.06)])
(np.float64(0.08927036607170535), -508, -94, [np.float64(56.49), np.float64(7.91), np.float64(23.71), np.float64(15.82), np.float64(16.06)])
(np.float64(0.08945721110287508), -455, -99, [np.float64(56.38), np.float64(7.99), np.float64(23.82), np.float64(15.78), np.float64(16.07)])
(np.float64(0.09443830446795509), -495, -106, [np.float64(57.69), np.float64(7.89), np.float64(23.76), np.float64(15.74), np.float64(16.07)])
(np.float64(0.09692470343690474), -456, -99, [np.float64(56.62), np.float64(7.98), np.float64(23.78), np.float64(15.73), np.float64(16.07)])
(np.float64(0.09773515464
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > tb.py <<'EOF'
exec(open('load.py').read())
from scipy import stats
SPECS={"supp":("RF",(-30,0),(50,75),"less"),"ff":("FF",(-50,0),(80,150),"greater"),"st":("ST",(-50,0),(80,150),"greater")}
def tbin(d,loc,peri,win,di,mode="onset",smooth=False):
    F,P=mt3.mean_trains(d,probes(d)[loc],peri,mode)
    f,p=F.mean(0),P.mean(0)
    if smooth: f,p=mt3.gauss_smooth(f),mt3.gauss_smooth(p)
    f,p=f[win[0]:win[1]+1],p[win[0]:win[1]+1]
    if np.all(p-f==0): return 1.0
    return stats.wilcoxon(p,f,alternative=di).pvalue
nl=L['nuron_list']; nlk={(int(a),int(b)):r for a,b,*r in [list(x) for x in nl]}
rows=[]
for d in N:
    r=nlk[(d['session'],d['channel'])]
    row=dict(neuron=d['name'],nl_supp=r[0],nl_ff=r[1],nl_c5=r[2],nl_st=r[3])
    for e,(loc,peri,win,di) in SPECS.items():
        for pr in ("condition","unpaired"):
            row[f"{e}_{pr[:4]}"]=mt3.effect_test(d,probes(d)[loc],peri,win,di,pr,"onset")["p"]
        row[f"{e}_tbin"]=tbin(d,loc,peri,win,di)
        row[f"{e}_tbs"]=tbin(d,loc,peri,win,di,smooth=True)
    rows.append(row)
import pandas as pd
T=pd.DataFrame(rows)
T.to_pickle('tb.pkl')
EOF
executed/niknam-2019/.venv/bin/python tb.py && executed/niknam-2019/.venv/bin/python - <<'EOF'
import pandas as pd, numpy as np
T=pd.read_pickle('/'.join([__import__('os').environ['TMPDIR'],'tb.pkl']))
for e,c in (("supp","nl_supp"),("ff","nl_ff"),("st","nl_st")):
    for v in ("cond","unpa","tbin","tbs"):
        s=T[f"{e}_{v}"]<0.05
        print(e,v,'count',s.sum(),'agree with nuron_list',(s==(T[c]==1)).sum(),'/41')
print('nuron_list sums',T[['nl_supp','nl_ff','nl_c5','nl_st']].sum().tolist())
for v in ("cond","unpa","tbin","tbs"):
    print(v,'ff&st',((T[f"ff_{v}"]<.05)&(T[f"st_{v}"]<.05)).sum())
EOF
```

```
supp cond count 8 agree with nuron_list 35 /41
supp unpa count 9 agree with nuron_list 38 /41
supp tbin count 13 agree with nuron_list 34 /41
supp tbs count 15 agree with nuron_list 34 /41
ff cond count 8 agree with nuron_list 26 /41
ff unpa count 10 agree with nuron_list 28 /41
ff tbin count 10 agree with nuron_list 26 /41
ff tbs count 19 agree with nuron_list 29 /41
st cond count 11 agree with nuron_list 15 /41
st unpa count 24 agree with nuron_list 28 /41
st tbin count 16 agree with nuron_list 20 /41
st tbs count 34 agree with nuron_list 36 /41
nuron_list sums [8, 23, 23, 37]
cond ff&st 6
unpa ff&st 10
tbin ff&st 9
tbs ff&st 19
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && executed/niknam-2019/.venv/bin/python - <<'EOF'
exec(open('load.py').read())
import pandas as pd
T=pd.read_pickle('tb.pkl')
def pop(names,loc,peri,win):
    fs,ps=[],[]
    for nm in names:
        d=byname[nm]; F,P=mt3.mean_trains(d,probes(d)[loc],peri); f,p=mt3.normalized(F,P)
        fs.append(f[win[0]:win[1]+1].mean()); ps.append(p[win[0]:win[1]+1].mean())
    return round(np.mean(fs),3),round(np.mean(ps),3)
for v in ("tbin","tbs","unpa"):
    s={e:set(T.neuron[T[f"{e}_{v}"]<.05]) for e in ("supp","ff","st")}
    print(v,'supp',len(s['supp']),pop(s['supp'],"RF",(-30,0),(50,75)),'ff',len(s['ff']),pop(s['ff'],"FF",(-50,0),(80,150)),
          'st',len(s['st']),pop(s['st'],"ST",(-50,0),(80,150)))
    b=s['ff']&s['st']; print('   both',len(b),pop(b,"FF",(-50,0),(80,150)),pop(b,"ST",(-50,0),(80,150)))
ex=["2015092709","2015083106","2015071702","2015092707","2015051115"]
print(T[T.neuron.isin(ex)][["neuron","supp_cond","supp_unpa","supp_tbin","supp_tbs","ff_cond","ff_unpa","ff_tbin","ff_tbs","st_cond","st_unpa","st_tbin","st_tbs"]].to_string())
EOF
```

```
Wed Nov 11 06:25:01 UTC 2026
tbin supp 13 (np.float64(2.212), np.float64(1.297)) ff 10 (np.float64(0.817), np.float64(1.587)) st 16 (np.float64(0.793), np.float64(1.509))
   both 9 (np.float64(0.826), np.float64(1.586)) (np.float64(0.727), np.float64(1.691))
tbs supp 15 (np.float64(2.18), np.float64(1.35)) ff 19 (np.float64(0.885), np.float64(1.411)) st 34 (np.float64(0.815), np.float64(1.365))
   both 19 (np.float64(0.885), np.float64(1.411)) (np.float64(0.791), np.float64(1.492))
unpa supp 9 (np.float64(2.291), np.float64(1.297)) ff 10 (np.float64(0.825), np.float64(1.637)) st 24 (np.float64(0.781), np.float64(1.439))
   both 10 (np.float64(0.825), np.float64(1.637)) (np.float64(0.749), np.float64(1.718))
        neuron  supp_cond  supp_unpa  supp_tbin      supp_tbs   ff_cond       ff_unpa       ff_tbin        ff_tbs   st_cond       st_unpa       st_tbin        st_tbs
0   2015051115   0.960272   0.978220   0.996314  1.000000e+00  0.000626  2.049543e-06  1.096864e-09  1.214880e-13  0.000374  7.198017e-06  1.399976e-10  1.214880e-13
1   2015071702   0.800781   0.999701   0.954249  1.000000e+00  0.016599  1.108699e-04  2.273834e-02  8.680490e-11  0.092282  4.469135e-05  1.352000e-03  4.572645e-11
13  2015083106   0.026375   0.005192   0.007117  4.470348e-08  0.999998  1.000000e+00  1.000000e+00  1.000000e+00  0.997454  1.000000e+00  1.000000e+00  1.000000e+00
18  2015092707   0.976197   0.997230   0.999278  1.000000e+00  0.007316  4.704536e-07  1.949628e-10  1.214880e-13  0.005931  2.673005e-08  2.257295e-10  1.214880e-13
20  2015092709   0.485968   0.019606   0.015062  9.536743e-06  0.911281  9.922524e-01  9.999750e-01  1.000000e+00  0.468763  7.199940e-01  8.547653e-01  9.991876e-01
Shell cwd was reset to
```

**Agent calls Bash**

```bash
grep -n -i "signed-rank\|signed rank\|rank-sum\|stimulus-aligned" paper/10.1371-journal.pcbi.1007275.txt | head; grep -n "Statistical analysis of perisaccadic" paper/10.1371-journal.pcbi.1007275.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
ls questions | head; f=$(ls questions/*.yaml | head -1); cat $f | head -40; grep -n "N-model\|nmodel\|n-model" claims/niknam-2019.yaml | head -30
```

```
README.md
ashworth-2025.yaml
athalye-2023.yaml
bech-2026.yaml
bellvila-2026.yaml
bennett-2024.yaml
berg-2020.yaml
boran-2022.yaml
bouchard-2013.yaml
buccino-2024.yaml
dandiset: "001708"
paper: doi:10.64898/2025.12.15.693905
questions:
- claim: figs3-neutral-unmodulated
  asked: 2026-11-05
  question: >-
    The criterion takes the trials of all NEUTRAL units of all files, and expects 32 cells with 69
    and 70 trials. The dataset has 36 NEUTRAL units. Four are in 'evoked' files, labelled "NEUT";
    the other 32, labelled "Neutral", are the ongoing and evoked/ongoing cells. The 36 give 76 to 79
    trials. The paper's n = 32 is the second set, which is also the set of the ongoing analyses.
[... 60 more lines not kept]
```

**Agent calls Bash**

```bash
cd claims; awk '/^- id:/{id=$3} /N-model \(O8\)|depends_on/{print id": "$0}' niknam-2019.yaml | grep -i "o8"; grep -n "fig5a-n-model-no-perisaccadic-gain\|fig5a-s-f-beat-n-model$" niknam-2019.yaml; cat ../questions/README.md | head -40
```

```
fig5a-n-model-no-perisaccadic-gain:     Needs the N-model (O8). Delta LL per spike by D5 with NULL model O5 (a main; b, c
fig5a-s-f-beat-n-model:     Needs the N-model (O8). Per-neuron Delta LL per spike of these claims, compared by a
fig5b-st-remapping-better-than-n:     Needs the N-model (O8). Per neuron, the recorded classification of D2 (all trials, O1 and
397:- id: fig5a-n-model-no-perisaccadic-gain
490:- id: fig5a-s-f-beat-n-model
520:  - fig5a-n-model-no-perisaccadic-gain
1301:  - fig5a-n-model-no-perisaccadic-gain. The criterion called the paper's test two-sided; the paper gives only "the Wilcoxon signed-rank test". Now says sidedness is not stated, uses two-sided as a standard choice and shows the one-sided p.
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
```

**Agent calls Bash**

```bash
cd  python3 -c "
import yaml
c=yaml.safe_load(open('claims/niknam-2019.yaml'))
for x in c['claims']:
    if 'N-model' in (x.get('criterion','')+x['statement']): print(x['id'], x.get('depends_on'))
"; ls schemas; grep -n "verifications" -A40 schemas/attempt*.json | head -80
```

```
fig5a-n-model-no-perisaccadic-gain None
fig5a-s-f-beat-n-model ['fig5a-n-model-no-perisaccadic-gain', 'fig5a-s-model-perisaccadic-better', 'fig5a-f-model-perisaccadic-better']
fig5b-st-remapping-better-than-n ['fig1d-st-remapping']
fig5b-ff-remapping-a-model-only ['fig1c-ff-remapping']
fig5b-suppression-no-difference ['fig1b-saccadic-suppression']
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
386:    "verifications": {
387-      "type": "array",
388-      "items": {
389-        "type": "object",
390-        "additionalProperties": false,
391-        "required": [
392-          "date",
393-          "kind",
394-          "by",
395-          "results"
396-        ],
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 426,480p schemas/attempt.schema.json; grep -rl "verifications:" attempts | head -2 | xargs -I{} sh -c 'grep -n "verifications:" -A25 {}'
```

```
"type": "boolean"
                },
                "reason": {
                  "description": "The verifier's reason, in its own words.",
                  "type": "string"
                },
                "response": {
                  "description": "What the author changed or replied, kept apart from the verifier's reason.",
                  "type": "string"
                },
                "outcome": {
                  "description": "The outcome the verifier would give.",
                  "enum": [
                    "reproduced",
                    "partially_reproduced",
                    "not_reproduced",
                    "blocked"
                  ]
                }
              }
[... 87 more lines not kept]
```

**Agent calls Bash**

```bash
git show --stat f49e2c6787 | head -20; git show --stat b57422db3c | head; git show --stat 2650729e7e | head -20; ls transcripts/niknam-2019/
```

```
commit f49e2c67878f9d2ab8453d5582238195f1de38b0
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Wed Nov 11 05:59:41 2026 +0000

    Agent run on niknam-2019: author-answers (success)
    
    Run: https://github.com/catalystneuro/encore/actions/runs/42968326216
    
    Account: verified

 transcripts/niknam-2019/author-answers-report.md |  28 +++
 transcripts/niknam-2019/author-answers.md        | 221 +++++++++++++++++++++++
 2 files changed, 249 insertions(+)
commit b57422db3cf0e8d5b93e526358e4674dc70e650b
Author: github-actions[bot] <github-actions[bot]@users.noreply.github.com>
Date:   Wed Nov 11 05:49:50 2026 +0000

    Agent run on niknam-2019: answer (success)
    
    Run: https://github.com/catalystneuro/encore/actions/runs/42967421208
[... 35 more lines not kept]
```

**Agent calls Bash**

```bash
cd executed/niknam-2019 && ls; python3 - <<'EOF'
import json
nb=json.load(open('reproduce_niknam_2019.ipynb'))
for i in (4,15,36):
    for o in nb['cells'][i].get('outputs',[]):
        print(i, ''.join(o.get('text','')))
EOF
```

```
reproduce_niknam_2019.ipynb
result.json
4 probe run lengths (ms: share of runs): {6: 0.0555, 7: 0.9151, 8: 0.0015, 9: 0.0002, 10: 0.0033, 11: 0.0005, 12: 0.0, 13: 0.0021, 14: 0.0172, 15: 0.0, 18: 0.0, 20: 0.0008, 21: 0.0037, 22: 0.0, 27: 0.0, 28: 0.0001}
gaps between probes inside the sequence (ms: count): {7: 3, 8: 1, 9: 5, 10: 1458, 11: 4434, 12: 29, 13: 16, 14: 155, 17: 1, 18: 3, 20: 1225, 21: 4525, 27: 2, 28: 9}
first probe at 9-17 ms, last probe ends at 1468-2371 ms of the 3000 ms arrays
trials whose onsets run in blocks of 81 distinct codes: 0.076

15 Neurons significant by D2 under each reading (paper: 8, 23, 37, 22)
  pairing presentations  pairs_median  neurons_testable  suppression  ff  st  ff_and_st
    trial         onset           0.0                 0            0   0   0          0
condition         onset          30.0                41            8   8  11          6
 unpaired         onset           0.0                41            9  10  24         10
    trial         every           0.0                 0            0   0   0          0
condition         every          34.0                41            4   9   9          6
 unpaired         every           0.0                41           12  17  31         17
     supp_n_fix  supp_n_peri  ff_n_fix  ff_n_peri  st_n_fix  st_n_peri
min       117.0          8.0     130.0       17.0     137.0       10.0
50%       425.0         30.0     420.0       60.0     420.0       50.0
max       592.0         51.0     601.0       80.0     597.0       92.0

[... 8 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && executed/niknam-2019/.venv/bin/python - <<'EOF'
exec(open('load.py').read())
import collections
d=byname["2015051115"]
sc=d['stimcode']
tr,t,c=mt3.all_onsets(d)
per_trial=np.bincount(tr,minlength=sc.shape[0])
print('onsets per trial: min/median/max',per_trial.min(),np.median(per_trial),per_trial.max())
reps=collections.Counter()
for i in range(sc.shape[0]):
    cc=np.bincount(c[tr==i],minlength=82)[1:]
    reps.update(cc.tolist())
print('presentations of each probe per trial (count of probe-trial pairs):',dict(sorted(reps.items())))
# within a trial: positions of onsets of the same code: spacing in onsets
i=0; seq=c[tr==i]; tt=t[tr==i]
print('trial0 first 100 codes',seq[:100].tolist())
print('trial0 length',len(seq),'distinct',len(set(seq)))
# check: does each code appear once per 81 onsets if we split at the right phase?
# do trials with the same cond share stimcode?
same=[]
for k in np.unique(d['conds'])[:20]:
    idx=np.flatnonzero(d['conds']==k)
    same.append(all((sc[j]==sc[idx[0]]).all() for j in idx))
print('trials of a condition share stimcode (first 20 conds):',sum(same),'of',len(same))
# sacc-relative distribution: how many onsets per trial fall in -500..0
rel=t-d['sacc'][tr]
print('onsets per trial in -500..-100', np.median(np.bincount(tr[(rel>=-500)&(rel<=-100)])), 'in -50..0', np.median(np.bincount(tr[(rel>=-50)&(rel<=0)])))
# for one probe, per trial: in fix and in peri, both?
p=probes(d)['FF']; m=c==p
f=np.unique(tr[m&(rel>=-500)&(rel<=-100)]); q=np.unique(tr[m&(rel>=-50)&(rel<=0)])
print('FF probe: trials with fixation presentation',len(f),'with peri',len(q),'both',len(np.intersect1d(f,q)))
# min gap (ms) between presentations of the same code in a trial
gaps=[]
for i in range(sc.shape[0]):
    s=c[tr==i]; ts=t[tr==i]
    for code in np.unique(s):
        x=np.sort(ts[s==code]); gaps.extend(np.diff(x).tolist())
gaps=np.array(gaps); print('ms between repeats of a code in a trial: min',gaps.min(),'5th pct',np.percentile(gaps,5),'median',np.median(gaps))
EOF
```

```
onsets per trial: min/median/max 198 228.0 259
presentations of each probe per trial (count of probe-trial pairs): {0: 3846, 2: 2599, 3: 41126, 4: 4350}
trial0 first 100 codes [52, 60, 74, 53, 49, 73, 72, 47, 44, 43, 48, 61, 77, 54, 58, 46, 69, 39, 66, 33, 34, 30, 40, 9, 78, 71, 26, 24, 81, 63, 42, 80, 3, 19, 5, 79, 76, 7, 18, 2, 6, 75, 70, 17, 11, 13, 4, 12, 16, 20, 32, 25, 8, 14, 38, 15, 21, 35, 45, 22, 36, 28, 29, 41, 31, 55, 1, 37, 64, 27, 23, 51, 56, 10, 50, 52, 60, 74, 53, 49, 73, 72, 47, 44, 43, 48, 61, 77, 54, 58, 46, 69, 39, 66, 33, 34, 30, 40, 9, 78]
trial0 length 244 distinct 75
trials of a condition share stimcode (first 20 conds): 0 of 20
onsets per trial in -500..-100 52.0 in -50..0 7.0
FF probe: trials with fixation presentation 436 with peri 67 both 0
ms between repeats of a code in a trial: min 34 5th pct 389.0 median 562.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && executed/niknam-2019/.venv/bin/python - <<'EOF'
exec(open('load.py').read())
import collections
for nm in ["2015051115","2015092707","2015121401" if "2015121401" in byname else N[-1]['name']]:
    d=byname[nm]; sc=d['stimcode']; tr,t,c=mt3.all_onsets(d)
    nd=[];cyc=[];conds_same=[]
    seqs={}
    for i in range(sc.shape[0]):
        s=c[tr==i]; nd.append(len(set(s)))
        # cycle length: smallest L such that s[L:]==s[:-L]
        L=next((L for L in range(1,len(s)) if np.array_equal(s[L:],s[:-L])),None); cyc.append(L)
        seqs.setdefault(d['conds'][i],[]).append(tuple(s[:L]) if L else tuple(s))
    print(nm,'distinct codes per trial',collections.Counter(nd).most_common(5),'cycle length',collections.Counter(cyc).most_common(5))
    # trials of a condition: same cycle up to rotation?
    def canon(x):
        x=list(x); k=x.index(min(x)); return tuple(x[k:]+x[:k])
    same=sum(len({canon(s) for s in v})==1 for v in seqs.values()); print('  conditions whose trials share one cyclic order:',same,'of',len(seqs))
    print('  distinct cycles over trials', len({canon(s) for v in seqs.values() for s in v}), 'conditions',len(seqs))
EOF
```

```
2015051115 distinct codes per trial [(75, 641)] cycle length [(145, 25), (156, 22), (155, 22), (157, 22), (146, 22)]
  conditions whose trials share one cyclic order: 0 of 75
  distinct cycles over trials 584 conditions 75
2015092707 distinct codes per trial [(80, 437)] cycle length [(168, 21), (167, 19), (166, 17), (80, 16), (190, 15)]
  conditions whose trials share one cyclic order: 0 of 80
  distinct cycles over trials 418 conditions 80
2015121516 distinct codes per trial [(81, 918)] cycle length [(81, 37), (165, 36), (169, 32), (182, 32), (164, 31)]
  conditions whose trials share one cyclic order: 0 of 81
  distinct cycles over trials 823 conditions 81
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && executed/niknam-2019/.venv/bin/python - <<'EOF'
exec(open('load.py').read())
import collections
res=[]
for s in sorted({d['session'] for d in N}):
    d=next(x for x in N if x['session']==s); sc=d['stimcode']; tr,t,c=mt3.all_onsets(d)
    nd=[len(set(c[tr==i])) for i in range(sc.shape[0])]
    # block check with the trial's own number of codes K
    ok=[];okK=[]
    for i in range(sc.shape[0]):
        q=c[tr==i]; K=len(set(q))
        okK.append(all(len(set(q[j:j+K]))==len(q[j:j+K]) for j in range(0,len(q)-K+1)))
    first=[c[tr==i][0] for i in range(sc.shape[0])]
    m=collections.defaultdict(set)
    for i in range(sc.shape[0]): m[d['conds'][i]].add(first[i])
    res.append((s,len(np.unique(d['conds'])),collections.Counter(nd).most_common(2),round(np.mean(okK),3),
                np.mean([len(v)==1 for v in m.values()]).round(2)))
for r in res: print(r)
EOF
```

```
(20150511, 75, [(75, 641)], np.float64(0.016), np.float64(1.0))
(20150717, 81, [(81, 305)], np.float64(1.0), np.float64(1.0))
(20150720, 81, [(81, 675)], np.float64(0.039), np.float64(1.0))
(20150729, 81, [(81, 290)], np.float64(0.041), np.float64(1.0))
(20150820, 81, [(81, 784)], np.float64(0.04), np.float64(1.0))
(20150831, 81, [(81, 493)], np.float64(0.022), np.float64(1.0))
(20150905, 81, [(81, 547)], np.float64(0.029), np.float64(1.0))
(20150927, 80, [(80, 437)], np.float64(0.037), np.float64(1.0))
(20150929, 80, [(80, 197)], np.float64(0.03), np.float64(1.0))
(20151214, 81, [(81, 646)], np.float64(0.022), np.float64(1.0))
(20151215, 81, [(81, 918)], np.float64(0.04), np.float64(1.0))
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && executed/niknam-2019/.venv/bin/python - <<'EOF'
exec(open('load.py').read())
d=byname["2015071702"]; sc=d['stimcode']
for i in range(3):
    row=sc[i]; ch=np.flatnonzero(np.diff(row)!=0)+1; st=np.r_[0,ch]; ln=np.diff(np.r_[st,row.size]); v=row[st]
    on=v>0; q=v[on]; L=ln[on]
    K=len(set(q))
    bad=[j for j in range(len(q)-K+1) if len(set(q[j:j+K]))<K]
    # compare q to q shifted by K
    eq=(q[K:]==q[:-K])
    print('trial',i,'onsets',len(q),'K',K,'windows not distinct',len(bad),'of',len(q)-K+1,'| q[j]==q[j+K] share',eq.mean().round(3),
          '| first mismatch at',np.flatnonzero(~eq)[:5],'run lens there',L[np.flatnonzero(~eq)[:3]], 'lens>7 at',np.flatnonzero(L>8)[:6])
EOF
```

```
Wed Nov 11 06:26:48 UTC 2026
trial 0 onsets 324 K 81 windows not distinct 0 of 244 | q[j]==q[j+K] share 1.0 | first mismatch at [] run lens there [] lens>7 at [ 41  80 107 132 133 147]
trial 1 onsets 324 K 81 windows not distinct 0 of 244 | q[j]==q[j+K] share 1.0 | first mismatch at [] run lens there [] lens>7 at [ 41  80 101 120 121 135]
trial 2 onsets 324 K 81 windows not distinct 0 of 244 | q[j]==q[j+K] share 1.0 | first mismatch at [] run lens there [] lens>7 at [ 41  80 106 129 130 144]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && executed/niknam-2019/.venv/bin/python - <<'EOF'
exec(open('load.py').read())
for nm in ["2015051115","2015121516"]:
    d=byname[nm]; sc=d['stimcode']
    for i in range(2):
        row=sc[i]; ch=np.flatnonzero(np.diff(row)!=0)+1; st=np.r_[0,ch]; ln=np.diff(np.r_[st,row.size]); v=row[st]
        on=v>0; q=v[on]; L=ln[on]; S=st[on]
        K=len(set(q)); eq=(q[K:]==q[:-K]); mm=np.flatnonzero(~eq)
        print(nm,i,'onsets',len(q),'K',K,'q[j]==q[j+K]',eq.mean().round(3),'first mismatch',mm[:4],'at ms',S[mm[:4]],'sacc',d['sacc'][i])
        j=mm[0] if len(mm) else 0
        print('   around', q[max(j-3,0):j+5].tolist(), 'vs', q[max(j-3,0)+K:j+5+K].tolist(), 'lens',L[j-3:j+5].tolist(),L[j-3+K:j+5+K].tolist())
EOF
```

```
2015051115 0 onsets 244 K 75 q[j]==q[j+K] 0.556 first mismatch [94 95 96 97] at ms [690 697 704 711] sacc 1135
   around [69, 39, 66, 33, 34, 30, 40, 9] vs [69, 39, 66, 52, 60, 74, 53, 49] lens [7, 7, 6, 7, 7, 7, 7, 7] [7, 7, 7, 7, 7, 7, 7, 7]
2015051115 1 onsets 231 K 75 q[j]==q[j+K] 0.519 first mismatch [81 82 83 84] at ms [593 600 607 614] sacc 1090
   around [53, 49, 73, 72, 47, 44, 43, 48] vs [53, 49, 73, 52, 60, 74, 53, 49] lens [7, 7, 6, 7, 7, 7, 7, 7] [7, 7, 7, 7, 7, 7, 7, 7]
2015121516 0 onsets 264 K 81 q[j]==q[j+K] 0.557 first mismatch [102 103 104 105] at ms [739 746 760 767] sacc 1136
   around [64, 37, 41, 22, 39, 74, 24, 28] vs [64, 37, 41, 3, 26, 56, 20, 63] lens [7, 7, 7, 7, 14, 7, 7, 7] [7, 7, 7, 7, 7, 7, 7, 7]
2015121516 1 onsets 230 K 81 q[j]==q[j+K] 0.456 first mismatch [68 69 70 71] at ms [489 496 503 510] sacc 1012
   around [70, 75, 27, 44, 67, 72, 68, 7] vs [70, 75, 27, 3, 26, 56, 20, 63] lens [7, 7, 7, 7, 7, 7, 7, 7] [7, 7, 7, 7, 7, 7, 7, 7]
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && executed/niknam-2019/.venv/bin/python - <<'EOF'
exec(open('load.py').read())
for s in sorted({d['session'] for d in N}):
    d=next(x for x in N if x['session']==s); sc=d['stimcode']; rel=[]; nre=[]
    for i in range(sc.shape[0]):
        row=sc[i]; ch=np.flatnonzero(np.diff(row)!=0)+1; st=np.r_[0,ch]; v=row[st]; on=v>0; q=v[on]; S=st[on]
        # restarts: onset j>0 where q[j:j+3]==q[0:3]
        r=[j for j in range(1,len(q)-3) if (q[j:j+3]==q[:3]).all()]
        K=len(set(q))
        extra=[j for j in r if j%K!=0]  # restarts not at a cycle boundary
        nre.append(len(extra))
        rel+= [S[j]-d['sacc'][i] for j in extra]
    rel=np.array(rel)
    print(s,'trials',sc.shape[0],'trials with off-cycle restart',np.mean(np.array(nre)>0).round(2), 'restart time rel. saccade ms: median',np.median(rel) if len(rel) else None, 'range',(rel.min(),rel.max()) if len(rel) else None)
EOF
```

```
20150511 trials 641 trials with off-cycle restart 0.98 restart time rel. saccade ms: median 107.0 range (np.int64(40), np.int64(247))
20150717 trials 305 trials with off-cycle restart 0.0 restart time rel. saccade ms: median None range None
20150720 trials 675 trials with off-cycle restart 0.96 restart time rel. saccade ms: median 213.0 range (np.int64(42), np.int64(292))
20150729 trials 290 trials with off-cycle restart 0.96 restart time rel. saccade ms: median 211.0 range (np.int64(45), np.int64(288))
20150820 trials 784 trials with off-cycle restart 0.96 restart time rel. saccade ms: median 209.0 range (np.int64(35), np.int64(273))
20150831 trials 493 trials with off-cycle restart 0.98 restart time rel. saccade ms: median 85.5 range (np.int64(37), np.int64(295))
20150905 trials 547 trials with off-cycle restart 0.97 restart time rel. saccade ms: median 83.0 range (np.int64(40), np.int64(295))
20150927 trials 437 trials with off-cycle restart 0.96 restart time rel. saccade ms: median 200.0 range (np.int64(38), np.int64(296))
20150929 trials 197 trials with off-cycle restart 0.97 restart time rel. saccade ms: median 186.0 range (np.int64(35), np.int64(264))
20151214 trials 646 trials with off-cycle restart 0.98 restart time rel. saccade ms: median 217.0 range (np.int64(37), np.int64(294))
20151215 trials 918 trials with off-cycle restart 0.96 restart time rel. saccade ms: median 210.0 range (np.int64(40), np.int64(275))
Shell cwd was reset to
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/niknam-2019/mt3.py",
 "old_string": "- Test: one-sided Wilcoxon signed-rank on spike counts (D2). The pairs are open (claims\n  file O1): ``pairing='trial'`` (a), ``'condition'`` (b), or ``'unpaired'`` (c, a\n  one-sided rank-sum on all presentations, a variant).",
 "new_string": "- Test: one-sided Wilcoxon signed-rank on spike counts (D2). The pairs are open (claims\n  file O1): ``pairing='trial'`` (a), ``'condition'`` (b), or ``'unpaired'`` (c, a\n  one-sided rank-sum on all presentations, a variant). ``timebin_test`` adds a pairing\n  outside O1, raised by the verifier: the mean count in each 1 ms bin of the response\n  window, perisaccadic against fixation, paired by bin (Methods: \"comparing the\n  perisaccadic and fixation spike counts (during the same stimulus-aligned window)\"). Its\n  smoothed form pairs the curves smoothed as for plots, which the Methods exclude (\"all\n  statistical analyses were performed on spike counts ... (not estimates of firing\n  rate)\"); both are variants and decide no outcome."
}
```

```
The file entries/niknam-2019/mt3.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/niknam-2019/mt3.py",
 "old_string": "def mean_trains(d, probe, peri, mode=\"onset\"):",
 "new_string": "def timebin_test(d, probe, peri, resp_win, direction, mode=\"onset\", smooth=False):\n    \"\"\"Variant pairing: mean count per 1 ms bin of resp_win, perisaccadic against fixation,\n    one-sided signed-rank over the bins (smooth=True: the FWHM 13 ms curves of D3).\"\"\"\n    F, P = mean_trains(d, probe, peri, mode)\n    f, p = F.mean(0), P.mean(0)\n    if smooth:\n        f, p = gauss_smooth(f), gauss_smooth(p)\n    f, p = f[resp_win[0] : resp_win[1] + 1], p[resp_win[0] : resp_win[1] + 1]\n    out = {\"n\": len(f), \"n_fix\": len(F), \"n_peri\": len(P), \"mean_fix\": f.mean() / 1000, \"mean_peri\": p.mean() / 1000}\n    out[\"p\"] = 1.0 if np.all(p == f) else stats.wilcoxon(p, f, alternative=direction).pvalue\n    return out\n\n\ndef mean_trains(d, probe, peri, mode=\"onset\"):"
}
```

```
The file entries/niknam-2019/mt3.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent**

Now the notebook edits. I'll write them with a script that replaces cell sources by index.

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/cells && cd $TMPDIR/cells && cat > c4_add.py <<'EOF'

# Order of probes within a trial (bears on which pairings of O1 exist). Per session: onsets per
# trial, distinct codes per trial, presentations of each shown probe per trial, ms between repeats
# of a probe, trials where one probe falls in both the fixation (-500 to -100 ms) and the
# perisaccadic (-50 to 0 ms) window, and where the order restarts from its first probe.
seq_rows = []
for s in inv.session.unique():
    d = next(x for x in N if x["session"] == s)
    tr, t, c = mt3.all_onsets(d)
    rel = t - d["sacc"][tr]
    fixw, periw = mt3.in_window(d, tr, t, mt3.FIX), mt3.in_window(d, tr, t, mt3.PERI_LATE)
    n_on, n_codes, reps, rep_ms, both, restart = [], [], collections.Counter(), [], 0, []
    for i in range(d["stimcode"].shape[0]):
        m = tr == i
        q, ti = c[m], t[m]
        n_on.append(len(q)); n_codes.append(len(set(q)))
        reps.update(np.bincount(q)[np.unique(q)].tolist())
        for code in np.unique(q):
            rep_ms.extend(np.diff(np.sort(ti[q == code])).tolist())
        both += len(np.intersect1d(q[fixw[m]], q[periw[m]]))
        K = len(set(q))
        r = [j for j in range(1, len(q) - 3) if j % K and (q[j:j + 3] == q[:3]).all()]
        if r:
            restart.append(ti[r[0]] - d["sacc"][i])
    restart = np.array(restart)
    seq_rows.append(dict(session=s, onsets_per_trial=f"{min(n_on)}-{max(n_on)}",
                         codes_per_trial=sorted(set(n_codes)), presentations_per_probe_per_trial=dict(sorted(reps.items())),
                         ms_between_repeats_median=float(np.median(rep_ms)), ms_between_repeats_5pct=float(np.percentile(rep_ms, 5)),
                         probe_in_both_windows=both, trials_restarting=f"{len(restart)}/{len(n_on)}",
                         restart_ms_from_saccade=f"{restart.min()}-{restart.max()}" if len(restart) else "-"))
print(pd.DataFrame(seq_rows).to_string(index=False))
# Runs longer than 7 ms: in session 20150717, whose order never restarts, the onset sequence repeats
# exactly every 81 onsets, so a 14 or 21 ms run takes one place in the order (one probe held longer).
d = next(x for x in N if x["session"] == 20150717)
tr, t, c = mt3.all_onsets(d)
exact = all((c[tr == i][81:] == c[tr == i][:-81]).all() for i in range(d["stimcode"].shape[0]))
long_runs = sum(((np.diff(np.r_[0, np.flatnonzero(np.diff(row) != 0) + 1, row.size]) >= 13)
                 & (row[np.r_[0, np.flatnonzero(np.diff(row) != 0) + 1]] > 0)).sum() for row in d["stimcode"])
print(f"session 20150717: onset order repeats every 81 onsets in every trial: {exact}; runs of 13 ms or more: {long_runs}")
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/cells && cat > c15.py <<'EOF'
SPECS = {"supp": ("RF", mt3.PERI_RF, mt3.EARLY, "less"),
         "ff": ("FF", mt3.PERI_LATE, mt3.LATE, "greater"),
         "st": ("ST", mt3.PERI_LATE, mt3.LATE, "greater")}
PROBES = {}
for d in N:
    r = row_of[(d["session"], d["channel"])]
    PROBES[d["name"]] = {"RF": mt3.sub2ind(r[2], r[3]), "FF": mt3.sub2ind(r[4], r[5]), "ST": mt3.sub2ind(r[6], r[7])}
# O1 a (trial) and b (condition) decide, with O2 i (onset); the rest are variants: O1 c (unpaired),
# and two pairings outside O1, over the 1 ms bins of the response window, of mean counts (timebin)
# and of the smoothed curves (timebin_smoothed), which the Methods exclude ("not estimates of firing rate").
PAIRINGS = ("trial", "condition", "unpaired", "timebin", "timebin_smoothed")
READINGS = [(p, m) for m in ("onset", "every") for p in PAIRINGS]
DECIDES = {("trial", "onset"), ("condition", "onset")}


def run_test(d, eff, p, m):
    loc, peri, win, di = SPECS[eff]
    if p.startswith("timebin"):
        return mt3.timebin_test(d, PROBES[d["name"]][loc], peri, win, di, m, smooth=p == "timebin_smoothed")
    return mt3.effect_test(d, PROBES[d["name"]][loc], peri, win, di, p, m)


TESTS = {(d["name"], eff, p, m): run_test(d, eff, p, m) for d in N for eff in SPECS for p, m in READINGS}
sig, TESTABLE = {}, {}
rows = []
for p, m in READINGS:
    TESTABLE[(p, m)] = any(not np.isnan(TESTS[(d["name"], "ff", p, m)]["p"]) for d in N)
    for eff in SPECS:
        ps = np.array([TESTS[(d["name"], eff, p, m)]["p"] for d in N])
        sig[(eff, p, m)] = np.nan_to_num(ps, nan=1.0) < 0.05
    row = dict(pairing=p, presentations=m, decides=(p, m) in DECIDES,
               pairs_median=np.median([TESTS[(d["name"], "ff", p, m)]["n"] if p != "unpaired" else 0 for d in N]),
               neurons_testable=sum(not np.isnan(TESTS[(d["name"], "ff", p, m)]["p"]) for d in N))
    for eff, lab in (("supp", "suppression"), ("ff", "ff"), ("st", "st")):
        row[lab] = int(sig[(eff, p, m)].sum()) if TESTABLE[(p, m)] else "not testable"
    row["ff_and_st"] = int((sig[("ff", p, m)] & sig[("st", p, m)]).sum()) if TESTABLE[(p, m)] else "not testable"
    rows.append(row)
counts_tab = pd.DataFrame(rows)
print("Neurons significant by D2 under each reading (paper: 8, 23, 37, 22)")
print(counts_tab.to_string(index=False))
# number of presentations per neuron in each window, onset reading
npres = pd.DataFrame([{**{"neuron": d["name"]}, **{f"{e}_{k}": TESTS[(d["name"], e, "condition", "onset")][k]
                       for e in SPECS for k in ("n_fix", "n_peri")}} for d in N])
print(npres.describe().loc[["min", "50%", "max"]].round(1).to_string())
EOF
cat > c16.py <<'EOF'
def population(names_sel, loc, peri, win, mode="onset"):
    """D3 normalized responses of the selected neurons; O4 a and b."""
    fs, ps = [], []
    for d in N:
        if d["name"] not in names_sel:
            continue
        F, P = mt3.mean_trains(d, PROBES[d["name"]][loc], peri, mode)
        f, p = mt3.normalized(F, P)
        fs.append(f); ps.append(p)
    fs, ps = np.array(fs), np.array(ps)
    if len(fs) == 0:
        return dict(n=0)
    wf = fs[:, win[0]:win[1] + 1].mean(1); wp = ps[:, win[0]:win[1] + 1].mean(1)
    sf, sp = mt3.gauss_smooth(fs.mean(0)), mt3.gauss_smooth(ps.mean(0))
    return dict(n=len(fs), fix_a=wf.mean(), fix_a_se=wf.std(ddof=1) / np.sqrt(len(wf)) if len(wf) > 1 else np.nan,
                peri_a=wp.mean(), peri_a_se=wp.std(ddof=1) / np.sqrt(len(wp)) if len(wp) > 1 else np.nan,
                fix_b=sf[win[0]:win[1] + 1].max(), peri_b=sp[win[0]:win[1] + 1].max(), curves=(fs, ps))


def within(v, e, tol):
    return abs(v - e) <= tol + 1e-9


def fig1_table(eff, loc, peri, win, expected, selector=None):
    rows = []
    for p, m in READINGS:
        row = dict(pairing=p, presentations=m, decides=(p, m) in DECIDES)
        if not TESTABLE[(p, m)]:
            row["count"] = "not testable"
            rows.append(row)
            continue
        sel = sig[(eff, p, m)] if selector is None else selector(p, m)
        names_sel = {d["name"] for d, s in zip(N, sel) if s}
        pop = population(names_sel, loc, peri, win, m)
        row["count"] = int(sel.sum())
        if pop["n"]:
            row.update(fix_a=pop["fix_a"], fix_a_se=pop["fix_a_se"], peri_a=pop["peri_a"], peri_a_se=pop["peri_a_se"],
                       fix_b=pop["fix_b"], peri_b=pop["peri_b"])
            row["in_tol_a"] = [within(row["count"], expected[0][0], expected[0][1]), within(row["fix_a"], *expected[1]),
                               within(row["peri_a"], *expected[2])]
        rows.append(row)
    return pd.DataFrame(rows)
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/cells && cat > c27.py <<'EOF'
rows = []
for p, m in READINGS:
    row = dict(pairing=p, presentations=m, decides=(p, m) in DECIDES)
    if not TESTABLE[(p, m)]:
        row["count"] = "not testable"
        rows.append(row)
        continue
    sel = sig[("ff", p, m)] & sig[("st", p, m)]
    names_sel = {d["name"] for d, s in zip(N, sel) if s}
    row["count"] = int(sel.sum())
    if names_sel:
        a = population(names_sel, "FF", mt3.PERI_LATE, mt3.LATE, m)
        b = population(names_sel, "ST", mt3.PERI_LATE, mt3.LATE, m)
        row.update(ff_fix=a["fix_a"], ff_peri=a["peri_a"], st_fix=b["fix_a"], st_peri=b["peri_a"],
                   ff_fix_b=a["fix_b"], ff_peri_b=a["peri_b"], st_fix_b=b["fix_b"], st_peri_b=b["peri_b"])
        exp = [(22, 2.2), (0.90, 0.03), (1.32, 0.08), (0.80, 0.03), (1.46, 0.08)]
        vals = [row["count"], row["ff_fix"], row["ff_peri"], row["st_fix"], row["st_peri"]]
        row["n_in_tol"] = sum(within(v, *e) for v, e in zip(vals, exp))
        row["both_increase"] = bool(row["ff_peri"] > row["ff_fix"] and row["st_peri"] > row["st_fix"])
    rows.append(row)
t1e = pd.DataFrame(rows)
print("expected: count 22 (2.2); FF 0.90 (0.03) to 1.32 (0.08); ST 0.80 (0.03) to 1.46 (0.08)")
print(t1e.round(3).to_string(index=False))
EOF
cat > c30.py <<'EOF'
allnames = {d["name"] for d in N}
rf_pop = population(allnames, "RF", mt3.PERI_RF, mt3.EARLY, "onset")
rf_curve = mt3.gauss_smooth(rf_pop["curves"][0].mean(0))
print(f"RF fixation peak (41 neurons, onset reading): {rf_curve.argmax()} ms")
rf_every = int(mt3.gauss_smooth(population(allnames, "RF", mt3.PERI_RF, mt3.EARLY, "every")["curves"][0].mean(0)).argmax())
rows = []
for p, m in READINGS:
    row = dict(pairing=p, presentations=m, decides=(p, m) in DECIDES)
    row["rf_peak"] = int(rf_curve.argmax()) if m == "onset" else rf_every
    if not TESTABLE[(p, m)]:
        row["n_ff"] = row["n_st"] = "not testable"
        rows.append(row)
        continue
    for eff, loc in (("ff", "FF"), ("st", "ST")):
        names_sel = {d["name"] for d, s in zip(N, sig[(eff, p, m)]) if s}
        row[f"n_{eff}"] = len(names_sel)
        if names_sel:
            c = mt3.gauss_smooth(population(names_sel, loc, mt3.PERI_LATE, mt3.LATE, m)["curves"][1].mean(0))
            row[f"{eff}_peri_peak"] = int(c.argmax())
    rows.append(row)
tlat = pd.DataFrame(rows)
print(tlat.to_string(index=False))
# per-neuron variant: peak of each remapping neuron's smoothed perisaccadic response (onset, condition)
for eff, loc in (("ff", "FF"), ("st", "ST")):
    pk = []
    for d, s in zip(N, sig[(eff, "condition", "onset")]):
        if s:
            F, P = mt3.mean_trains(d, PROBES[d["name"]][loc], mt3.PERI_LATE)
            pk.append(int(mt3.gauss_smooth(P.mean(0)).argmax()))
    print(f"{eff}: per-neuron perisaccadic peaks {sorted(pk)}")
EOF
cat > c33_add.py <<'EOF'
# p of the D2 test under every pairing (onset presentations) for the matched neurons and the
# closest neuron of each example; the paper gives p < 0.001 for each example.
closest = {ex: sorted((sum(abs(mt3.window_rate(mt3.mean_trains(byname[n], PROBES[n][loc], SPECS[eff][1])[k], SPECS[eff][2]).mean() - v) / tol
                           for eff, loc, ef, tf, ep, tp in parts for k, v, tol in ((0, ef, tf), (1, ep, tp))), n) for n in byname)[0][1]
           for ex, parts in EX.items()} if (byname := {d["name"]: d for d in N}) else None
shown = sorted(set(ex_tab[ex_tab.match].neuron) | set(closest.values()))
prow = []
for n in shown:
    for eff in SPECS:
        prow.append(dict(neuron=n, effect=eff, **{p: TESTS[(n, eff, p, "onset")]["p"] for p in PAIRINGS}))
with pd.option_context("display.float_format", "{:.2g}".format):
    print("closest neuron of each example:", closest)
    print(pd.DataFrame(prow).to_string(index=False))

# Fixation set: the fixation rate of the closest neuron of each example as the fixation window moves,
# start -560 to -440 ms and end -160 to -40 ms (1 ms steps), with the SE across presentations.
scan = []
for ex, parts in EX.items():
    n = closest[ex]; d = byname[n]
    for eff, loc, ef, tf, ep, tp in parts:
        _, peri, win, _ = SPECS[eff]
        tr, t = mt3.presentations(d, PROBES[n][loc])
        cr = mt3.counts(d, tr, t, win) * 1000.0 / (win[1] - win[0] + 1)
        rel = t - d["sacc"][tr]
        vals = {(a, b): cr[(rel >= a) & (rel <= b)].mean() for a in range(-560, -439) for b in range(-160, -39)}
        fx = (rel >= -500) & (rel <= -100)
        scan.append(dict(example=ex, neuron=n, probe=loc, paper=ef, paper_se=tf, here=cr[fx].mean(),
                         here_se=cr[fx].std(ddof=1) / np.sqrt(fx.sum()), n_fix=int(fx.sum()),
                         scan_min=min(vals.values()), scan_max=max(vals.values()), vals=vals))
scan = pd.DataFrame(scan)
print(scan.drop(columns="vals").round(2).to_string(index=False))
# one window for the three matched examples (four comparisons) at once
keys = list(scan.vals.iloc[0])
matched = scan[scan.example != "RF example"]
err = {k: max(abs(v[k] - e) for v, e in zip(matched.vals, matched.paper)) for k in keys}
best = sorted(err, key=err.get)[:3]
print("windows that bring the three matched examples closest to the paper (max |difference| spk/s):",
      [(k, round(err[k], 3)) for k in best], "; at -500 to -100:", round(err[(-500, -100)], 3))
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/cells && python3 - <<'EOF'
s=open('c33_add.py').read()
start=s.index('closest = {ex:'); end=s.index('shown = ')
s=s[:start]+'byname = {d["name"]: d for d in N}\n'+s[end:]
s=s.replace('best = sorted(err, key=err.get)[:3]','best_win = sorted(err, key=err.get)[:3]').replace('for k in best]','for k in best_win]')
open('c33_add.py','w').write(s)
EOF
cat > c40_add.py <<'EOF'
# Per neuron, by name: nuron_list columns 3 (suppression), 4 (FF) and 6 (ST), and the one-sided p of
# D2 under each pairing with onset presentations (cond = O1 b, unp = O1 c, tb = time bins of mean
# counts, tbs = time bins of smoothed curves).
nl_row = {(int(r[0]), int(r[1])): r for r in nl}
pn = []
for d in N:
    r = nl_row[(d["session"], d["channel"])]
    row = dict(neuron=d["name"], list_supp=int(r[2]), list_ff=int(r[3]), list_st=int(r[5]))
    for e in SPECS:
        for p, lab in (("condition", "cond"), ("unpaired", "unp"), ("timebin", "tb"), ("timebin_smoothed", "tbs")):
            row[f"{e}_{lab}"] = TESTS[(d["name"], e, p, "onset")]["p"]
    pn.append(row)
pn = pd.DataFrame(pn)
with pd.option_context("display.float_format", "{:.2g}".format, "display.width", 250):
    print(pn.to_string(index=False))
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent**

Now apply all code changes to the notebook.

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json, os
T=os.environ['TMPDIR']+'/cells/'
p='entries/niknam-2019/reproduce_niknam_2019.ipynb'
nb=json.load(open(p))
C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def put(i,s): C[i]['source']=s.splitlines(keepends=True)
assert 'probe run lengths' in src(4); put(4, src(4).rstrip('\n')+'\n'+open(T+'c4_add.py').read())
assert src(15).startswith('SPECS'); put(15, open(T+'c15.py').read())
assert src(16).startswith('def population'); put(16, open(T+'c16.py').read())
assert 'for p, m in READINGS' in src(27); put(27, open(T+'c27.py').read())
assert src(30).startswith('allnames'); put(30, open(T+'c30.py').read())
s=src(33)
s=s.replace('# closest neurons by values only (onset reading), for each example\nfor ex, parts in EX.items():',
            '# closest neurons by values only (onset reading), for each example\nclosest = {}\nfor ex, parts in EX.items():')
s=s.replace('    best = sorted(dist)[:3]\n','    best = sorted(dist)[:3]\n    closest[ex] = best[0][1]\n')
assert 'closest[ex]' in s
s=s.rstrip('\n')+'\n'+open(T+'c33_add.py').read()
put(33,s)
s=src(40)
s=s.replace('''for p, m in READINGS:
    s_ = [sig''','''for p, m in READINGS:
    if not TESTABLE[(p, m)]:
        print(f"agreement with nuron_list ({p}, {m}): not testable")
        continue
    s_ = [sig''')
assert 'not testable' in s
put(40, s.rstrip('\n')+'\n'+open(T+'c40_add.py').read())
for c in C:
    if c['cell_type']=='code': c['outputs']=[]; c['execution_count']=None
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
git diff --stat
```

```
entries/niknam-2019/mt3.py                      |  21 ++-
 entries/niknam-2019/reproduce_niknam_2019.ipynb | 175 ++++++++++++++++++++----
 2 files changed, 167 insertions(+), 29 deletions(-)
```

**Agent calls Bash**

```bash
date -u; python tools/entry.py all entries/niknam-2019 2>&1 | tail -5
```

```
Wed Nov 11 06:29:13 UTC 2026
Installed kernelspec registry-niknam-2019 in executed/niknam-2019/.venv/share/jupyter/kernels/registry-niknam-2019
0 error(s)
pass  reproduce_niknam_2019.ipynb  (72 s)
```

**Agent calls Bash**

```bash
cd executed/niknam-2019 && python3 - <<'EOF'
import json
nb=json.load(open('reproduce_niknam_2019.ipynb'))
for i in (4,15,18,21,24,27,30,33,36,40):
    for o in nb['cells'][i].get('outputs',[]):
        if 'text' in o: print('-----',i); print(''.join(o['text']))
EOF
```

```
----- 4
probe run lengths (ms: share of runs): {6: 0.0555, 7: 0.9151, 8: 0.0015, 9: 0.0002, 10: 0.0033, 11: 0.0005, 12: 0.0, 13: 0.0021, 14: 0.0172, 15: 0.0, 18: 0.0, 20: 0.0008, 21: 0.0037, 22: 0.0, 27: 0.0, 28: 0.0001}
gaps between probes inside the sequence (ms: count): {7: 3, 8: 1, 9: 5, 10: 1458, 11: 4434, 12: 29, 13: 16, 14: 155, 17: 1, 18: 3, 20: 1225, 21: 4525, 27: 2, 28: 9}
first probe at 9-17 ms, last probe ends at 1468-2371 ms of the 3000 ms arrays
trials whose onsets run in blocks of 81 distinct codes: 0.076

----- 4
 session onsets_per_trial codes_per_trial presentations_per_probe_per_trial  ms_between_repeats_median  ms_between_repeats_5pct  probe_in_both_windows trials_restarting restart_ms_from_saccade
20150511          198-259            [75]      {2: 2599, 3: 41126, 4: 4350}                      562.0                   389.00                      0           631/641                  40-247
20150717          324-324            [81]                        {4: 24705}                      584.0                   563.00                      0             0/305                       -
20150720          212-282            [81]      {2: 2003, 3: 43999, 4: 8673}                      604.0                   229.00                      0           649/675                  42-292
20150729          213-282            [81]       {2: 825, 3: 18933, 4: 3732}                      604.0                   236.00                      0           278/290                  45-288
20150820          212-282            [81]     {2: 1233, 3: 51066, 4: 11205}                      604.0                   222.00                      0           753/784                  35-273
20150831          212-282            [81]      {2: 3076, 3: 33117, 4: 3740}                      597.0                   389.00                      0           482/493                  37-295
20150905          212-281            [81]      {2: 3990, 3: 37063, 4: 3254}                      591.0            
[... 242 more lines not kept]
```

**Agent**

Outputs look right. Now the conclusions, header and summary text.

**Agent calls Bash**

```bash
cd  && python3 - <<'EOF'
import json
p='entries/niknam-2019/reproduce_niknam_2019.ipynb'
nb=json.load(open(p)); C=nb['cells']
def src(i): return ''.join(C[i]['source'])
def put(i,s): C[i]['source']=s.strip('\n').splitlines(keepends=True)
s=src(0)
old="| fig3, fig5a to fig5c, fig6, fig7, fig8, figs4, figs5 (25 claims) | blocked: they need the S-, F-, A- or N-model, which cannot be fitted within the limits (timed below) |"
assert old in s
s=s.replace(old,"| fig3, fig5a to fig5c, fig6, fig7, fig8, figs4, figs5 (25 claims) | blocked: they need the S-, F-, A- or N-model. The S-model's parameter selection alone, timed below, needs hours on the runner's 4 CPUs, over the 60-minute notebook limit and the five hours of an author run (`too_large`); fig5a-n-model-no-perisaccadic-gain is blocked because the N-model (ref [48]) is not defined (O8), which also holds for the four other claims that need it |")
put(0,s)
assert src(14).startswith('## Recorded perisaccadic effects')
put(14,"""## Recorded perisaccadic effects (Figure 1)

Each neuron is classified by D2 under every reading of O1 (pairs: (a) trial, (b) condition,
(c) unpaired rank-sum, a variant) and O2 (presentations: (i) onset, (ii) every ms, a variant).
Two pairings outside O1, raised by the verifier, are shown as variants: a one-sided signed-rank
test over the 1 ms bins of the response window, on the mean count per bin (`timebin`) and on the
curves smoothed as for plots (`timebin_smoothed`). The Methods allow the first ("comparing the
perisaccadic and fixation spike counts (during the same stimulus-aligned window)") and exclude the
second ("all statistical analyses were performed on spike counts ... (not estimates of firing
rate)"). Only (a) and (b) with onsets decide (column `decides`). Reading (a) cannot be tested: in
no session does any trial show a probe in both the fixation and the perisaccadic window (data
check, `probe_in_both_windows`), as a probe returns only after a pass through the whole order,
562 to 604 ms (median per session). The outcomes therefore rest on (b).

The normalized responses follow D3; O4 (a) is the mean over the effect window of the normalized
response, averaged over neurons with SE across neurons, and O4 (b) the peak inside the window of
the neuron-averaged curve smoothed with a Gaussian of FWHM 13 ms.""")
assert C[19]['metadata'].get('tags')==['conclusion']
put(19,"""**Result: reproduced under O1 (b), pairing by condition, with onsets (O2 i).** Eight neurons are significant (paper 8), and their normalized RF response falls from 2.235 to 1.239 by O4 (a) (paper 2.53 ± 0.37 to 1.51 ± 0.29; both within tolerance, near its lower edge); by O4 (b) the peaks are 2.541 and 1.530. Reading (a), pairing by trial, cannot be tested, because no trial shows the same probe in both windows. The 8 neurons are only partly the paper's: the classification agrees with the code's `nuron_list` on 35 of 41 neurons (reference section), so 5 of the 8 are in that list and 3 are not. The variants give 4 to 16 neurons; the unpaired test with onsets gives 9 with both values within tolerance, the time-bin tests 13 and 15.""")
put(22,"""**Result: not reproduced.** Under O1 (b) with onsets only 8 neurons show FF-remapping (paper 23, tolerance 2.3), and their normalized FF response rises from 0.792 to 1.609 (paper 0.90 to 1.30); the rise is present but none of the three numbers is within tolerance. Reading (a) cannot be tested. No variant reaches the count: they give 9 to 19 neurons. The closest, the time-bin test on smoothed curves with onsets (19 neurons, 0.885 to 1.411) and the unpaired, time-bin and smoothed time-bin tests with every-ms presentations (17 neurons, 0.888 or 0.889 to 1.427 or 1.430), have only the fixation value within tolerance. The time-bin test on mean counts with onsets gives 10 neurons. 7 of the 8 neurons under (b) are from leftward sessions.""")
put(25,"""**Result: not reproduced.** Under O1 (b) with onsets 11 neurons show ST-remapping (paper 37, tolerance 3.7), and their normalized ST response rises from 0.749 to 1.629 (paper 0.83 to 1.35); none of the three numbers is within tolerance. Reading (a) cannot be tested. The outcome depends on the pairing. The time-bin test on smoothed curves with onsets gives 34 neurons, 0.815 to 1.365, all three numbers within tolerance, and agrees with the code's `nuron_list` on ST for 36 of 41 neurons, against 15 for (b) (reference section). The Methods exclude that test, as it compares firing-rate estimates, and the claims file does not list it, so it decides nothing here; whether O1 should hold a pairing over time bins is asked of a reader (`questions/niknam-2019.yaml`). On mean counts per bin, the time-bin test gives 16 neurons with onsets (no number within tolerance) and 29 with every-ms presentations (0.819 to 1.383, both values within tolerance); the unpaired test with every-ms presentations gives 31 (0.823 to 1.369).""")
put(28,"""**Result: not reproduced.** Under O1 (b) with onsets 6 neurons show both effects (paper 22), and none of the five numbers is within tolerance (FF 0.777 to 1.680, ST 0.750 to 1.789), though both responses rise. Reading (a) cannot be tested. The variants give 6 to 19 neurons, none within tolerance of 22. The time-bin test on smoothed curves with onsets (19 neurons) and the unpaired, time-bin and smoothed time-bin tests with every-ms presentations (17 neurons) each have 3 of 5 numbers within tolerance, which would meet the partial rule; the others have none.""")
put(31,"""**Result: reproduced.** The neuron-averaged fixation RF response of the 41 neurons peaks at 62 ms after onset, inside 50-75 ms, and the perisaccadic FF and ST responses of the remapping neurons peak at 108 and 99 ms under O1 (b) with onsets, inside 80-150 ms. Every testable reading gives the same order (RF 59-62 ms, FF 103-108 ms, ST 96-128 ms). The remapped peaks are not an independent test: the neurons are selected for an increase 80-150 ms after onset, which pulls the averaged perisaccadic peak into that window, and the peaks of single neurons are spread (FF 12 to 150 ms, ST 0 to 150 ms). The RF peak, over all 41 neurons with no selection, is the part of the result that does not depend on the selection.""")
put(34,"""**Result: partially reproduced.** With onsets (O2 i), neurons match three of the four examples on both values and on a significant D2 test under O1 (b): 2015071702 for the FF example (7.83 to 18.96 spk/s, p 0.017), 2015092707 for the ST example (23.61 to 64.64, p 0.0059) and 2015051115 for the example with both effects (FF 15.76 to 39.10, p 0.00063; ST 16.05 to 36.17, p 0.00037). Their perisaccadic means equal the paper's to the second decimal in three of the five comparisons. No neuron matches the RF example. The closest, 2015092709, has the paper's perisaccadic value (40.49 ± 12.64) but a fixation rate of 56.94 ± 2.71 against 60.89 ± 2.82, and p 0.49 under (b) (0.02 unpaired, 0.015 on time bins); moving the fixation window (start -560 to -440 ms, end -160 to -40 ms) gives it 53.87 to 59.68, never 60.89. With every-ms presentations (a variant) 2015083106 matches the RF example.

The paper's p < 0.001 holds under (b) only for the example with both effects. Under the unpaired test the three matched examples give p 0.00011 or less, and under the time-bin test on mean counts 0.0014 or less except the FF example (0.023). The fixation values of the three matched examples differ from the paper's by 0.07 to 0.19 spk/s while their SEs agree within 0.01 (for example 1.01 against 1.02), so the paper's fixation sets are about the same size as ours. No window in the scan matches all three at once: the closest, -495 to -100 ms, is within 0.054 spk/s, against 0.194 at -500 to -100 ms. The paper's fixation set is not identified.""")
put(37,"""**Result: not tested; the model claims are blocked as too large.** The S-model has 290,628 stimulus-basis parameters per neuron, and its selection step runs 58,125,600 single-parameter fits per neuron. This port of `select_bases.m` takes about 7 ms per fit, about 1,050 hours on 4 CPUs for the 41 neurons. A fully batched port that evaluates only the nonzero samples would still need about 28 CPU hours, 7 hours on the runner's 4 CPUs, in this run; the timing varies between machines and runs. The limits that make this too large are the notebook's 60 minutes (CI fails a notebook over sixty) and the five hours of an author run, shared with everything else in it. The bound covers the selection step only: the full S-model fit, ten S- and F-model fits per neuron for the A-model, the per-bin F-model optimizations and the 1000 simulated sequences come on top. Five claims also need the N-model, which the paper defines only through ref [48] (O8); they would be blocked as methods underspecified with any budget.""")
s=src(41)
a=s.index('How the analysis differs'); 
s=s[:a]+"""How the analysis differs from the paper's. The Methods name a one-sided signed-rank test without
saying what is paired. Pairing by trial (O1 a) is impossible in these data, because no trial shows
the same probe in both windows, so the outcomes rest on pairing by condition (O1 b). Under that
reading saccadic suppression matches the paper (8 neurons, 5 of them in the code's `nuron_list`)
but FF- and ST-remapping are found in far fewer neurons (8 and 11 against 23 and 37). Variants the
claims file does not let decide come closer: the unpaired test on every millisecond a probe is on
gives 12, 17 and 31, and a signed-rank test over the 1 ms bins of the smoothed response curves,
which the Methods exclude, gives 15, 19 and 34, agreeing with `nuron_list` on ST for 36 of 41
neurons. Whether the claims file should include a pairing over time bins is asked of a reader. The
example neurons' fixation rates differ slightly from the paper's while their perisaccadic rates
match, so the paper's fixation set also differs from -500 to -100 ms in a way not identified here.
No model was fitted.

What was found about the dataset. The 41 files match the paper's 41 neurons and 11 sessions and
the descriptor's per-session counts, and they are identical to the copies in the paper's code
repository. Each recording appears once. The stimulus and saccade clocks hold: the RF response
peaks at 58 ms after probe onset and disappears with codes shifted by 300 ms. The files do not
give the saccade direction, the RF, FF or ST probes, the grid's position and spacing, or which
monkey each session comes from; the probes are only in the code repository. Probes do not tile
time as the paper says: about 91.5% of probe runs last 7 ms, with 6, 14 and 21 ms runs, and gaps
of 10 to 21 ms with no probe on screen; a 14 or 21 ms run takes one place in the probe order. The
order does not hold all 81 probes in three sessions (75 in 20150511, 80 in 20150927 and 20150929),
and in every session but 20150717 it restarts from its first probe 35 to 296 ms after saccade
onset in most trials, so each probe is shown 2 to 4 times per trial. The arrays are 3000 ms long,
while the paper gives trials of 2100 to 2300 ms.
"""
put(41,s)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
grep -c "" entries/niknam-2019/reproduce_niknam_2019.ipynb; tail -c 50 entries/niknam-2019/reproduce_niknam_2019.ipynb | od -c | tail -3
```

```
1153
0000040   o   r   m   a   t   _   m   i   n   o   r   "   :       5  \n
0000060   }  \n
0000062
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='entries/niknam-2019/reproduce_niknam_2019.ipynb'
s=open(p).read()
old="time-bin test on mean counts 0.0014 or less except the FF example (0.023)"
assert s.count(old)==1
s=s.replace(old,"time-bin test on mean counts 1.1e-09 or less except the FF example (0.023)")
open(p,'w').write(s)
EOF
date -u
```

```
Wed Nov 11 06:31:58 UTC 2026
```

**Agent calls Bash**

```bash
grep -l "^dataset\|crcns" questions/*.yaml | head -3; head -5 $(grep -l "crcns" questions/*.yaml | head -1); grep -n "questions" schemas/*.json tools/entry.py | head
```

```
questions/dias-2025.yaml
questions/didion-gency-2024.yaml
questions/dimakopoulos-2022.yaml
# Questions from attempt gu-2011-01 (author, 2026-11-06) about the claims file
# claims/crcns-stc-1/10.1016-j.neuron.2011.06.015.yaml. Each was raised by the round-2 verifier
# and is asked under docs/protocol.md, "Hand over for verification"; the claims are tested as
# written.
questions:
```

**Agent calls Bash**

```bash
head -12 questions/dias-2025.yaml; grep -rn "questions/" tools/*.py | head -5
```

```
# Questions from attempt dias-2025-01 (author, 2026-10-27) about the claims file
# claims/dryad-bvq83bkk9/10.1098-rspb.2024.2556.yaml. Each is asked under docs/protocol.md, Author,
# step 1.6. The attempt applied the criteria as written and showed ten further seed sets.
dataset: DRYAD:bvq83bkk9
paper: doi:10.1098/rspb.2024.2556
questions:
- claim: s4-s6-spring-migration-temperature-none
  also: [s6-autumn-ahy-recent-wintering-prebreeding-precipitation-none]
  asked: 2026-10-27
  question: How is a 95% bound that lies within Monte Carlo error of 0 to be judged? The criteria
    count any interval that excludes 0, under interval reading (i) or (ii), as not reproduced. The
    code sets no seed for the MCMCglmm runs, so the seed is a choice of the attempt. In the spring
tools/datasets.py:9:files in the repository (claims/, questions/, transcripts/, attempt branches, the paper store) are
tools/migrate_paper_first.py:20:| questions/<folder>.yaml | questions/<key>.yaml | questions/<key>/<folder>.yaml |
tools/migrate_paper_first.py:165:            moves.append((f"questions/{folder}.yaml",
tools/migrate_paper_first.py:166:                          f"questions/{keys[doi]}/{folder}.yaml" if doi in several else f"questions/{keys[doi]}.yaml"))
tools/paper_records.py:14:    questions/<key>.yaml                   the author's questions on them
```

**Agent calls Write**

```json
{
 "file_path": "questions/niknam-2019.yaml",
 "content": "# Questions from attempt niknam-2019-01 (author, round-1 revision, 2026-11-11) about the claims file\n# claims/niknam-2019.yaml. The question was raised by the round-1 verifier and is asked under\n# docs/protocol.md, \"Hand over for verification\"; the claims are tested as written.\ndataset: CRCNS:mt-3\npaper: doi:10.1371/journal.pcbi.1007275\nquestions:\n- claim: fig1d-st-remapping\n  also: [fig1c-ff-remapping, fig1e-ff-and-st-remapping, fig1b-saccadic-suppression]\n  asked: 2026-11-11\n  question: >-\n    O1 lets two pairings decide the signed-rank test of D2, (a) per trial and (b) per condition.\n    In these data (a) has no pairs at all, since no trial shows a probe in both the fixation and\n    the perisaccadic window, so every Figure 1 outcome rests on (b). Should O1 also hold a pairing\n    over the 1 ms bins of the response window (mean count per bin, perisaccadic against fixation),\n    which the Methods' wording \"during the same stimulus-aligned window\" also allows? Should a\n    test on the smoothed response curves be counted at all, given that the Methods say the\n    statistics use spike counts and not firing-rate estimates?\n  passage: >-\n    \"In all three cases, the statistical significance was tested by comparing the perisaccadic and\n    fixation spike counts (during the same stimulus-aligned window) using the Wilcoxon one-sided\n    signed-rank test\" and \"Note that all statistical analyses were performed on spike counts between\n    windows of the same duration (not estimates of firing rate).\" (Methods, Statistical analysis of\n    perisaccadic responses, paragraphs 1 and 2)\n  why: >-\n    Under (b) the counts are 8, 8, 11 and 6 against the paper's 8, 23, 37 and 22, and fig1c, fig1d\n    and fig1e are not reproduced. Pairing over time bins of mean counts gives 13, 10, 16 and 9 with\n    onsets, or 13, 17, 29 and 17 with every-ms presentations, which leaves those outcomes unchanged.\n    Pairing over time bins of the smoothed curves gives 15, 19, 34 and 19 with onsets: fig1d would\n    then be reproduced (34 neurons, 0.815 to 1.365), fig1c and fig1e partially reproduced, and fig1b\n    not reproduced (15 neurons). That pairing also agrees best with the code's undocumented\n    nuron_list (ST for 36 of 41 neurons, against 15 for (b)). The example neurons point away from\n    (b) as well: their perisaccadic means equal the paper's, but their (b) p values are 0.017 and\n    0.0059 where the paper gives p < 0.001.\n"
}
```

```
File created successfully at: questions/niknam-2019.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='questions/niknam-2019.yaml'
s=open(p).read()
s=s.replace("  also: [fig1c-ff-remapping, fig1e-ff-and-st-remapping, fig1b-saccadic-suppression]","  also: [fig1c-ff-remapping, fig1e-ff-and-st-remapping]")
old="""then be reproduced (34 neurons, 0.815 to 1.365), fig1c and fig1e partially reproduced, and fig1b
    not reproduced (15 neurons)."""
assert old in s
s=s.replace(old,"""then be reproduced (34 neurons, 0.815 to 1.365) and fig1c and fig1e partially reproduced; fig1b
    stays reproduced under (b).""")
open(p,'w').write(s)
import yaml; yaml.safe_load(open(p)); print('ok')
EOF
```

```
ok
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "questions/niknam-2019.yaml",
 "old_string": "    onsets, or 13, 17, 29 and 17 with every-ms presentations, which leaves those outcomes unchanged.",
 "new_string": "    onsets, which leaves those outcomes unchanged (13, 17, 29 and 17 with every-ms presentations,\n    which do not decide)."
}
```

```
The file questions/niknam-2019.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -n -o ".\{200\}81 probe.\{200\}" paper/10.1371-journal.pcbi.1007275.txt | head -3; grep -n -i -o ".\{100\}81.\{150\}" paper/mt-3.data-description.txt | head -5
```

Result: not kept, because it reads the paper's text.

**Agent**

Now the attempt record. I'll update it with a script so the 24 repeated model notes stay consistent.

**Agent calls Bash**

```bash
date -u; python3 - <<'EOF'
import yaml
p='attempts/niknam-2019-01.yaml'
A=yaml.safe_load(open(p))
O={o['claim']:o for o in A['outcomes']}
pair_dev=("Pairing by trial (O1 a) cannot be tested: no trial in any session shows the same probe in both the fixation "
  "and the perisaccadic window, as a probe returns only after a pass through the whole order (median 562 to 604 ms "
  "between repeats per session). The outcome rests on pairing by condition (O1 b), the other reading the criterion "
  "lets decide.")
pres_dev=("Presentations are the first ms of each run of a probe code (O2 i); runs of 14 or 21 ms count once, as such a run "
  "takes one place in the probe order (session 20150717, data check). Windows are taken inclusive at 1 ms, as "
  "get_mean_resp.m indexes t:t+window, a standard choice. Saccade onset is sample tsaccade in MATLAB's 1-based "
  "indexing, as select_bases.m reads it (tsaccade(i) + times).")
for c in ('fig1b-saccadic-suppression','fig1c-ff-remapping','fig1d-st-remapping','fig1e-ff-and-st-remapping',
          'fig1-remapping-longer-latency','fig1-example-neurons'):
    d=O[c]['deviations']
    O[c]['deviations']=[pair_dev,pres_dev]+[x for x in d[2:]]
O['fig1b-saccadic-suppression']['notes']=(
 "Under O1 b with onsets, 8 neurons are significant, and their normalized RF response over 50-75 ms falls from 2.235 "
 "+- 0.291 to 1.239 +- 0.183 (O4 a), both within tolerance near its lower edge; the O4 b peaks are 2.541 and 1.530. "
 "Reading O1 a cannot be tested. The 8 neurons come from 5 sessions, with p 0.0002 to 0.043. They are only partly the "
 "paper's: the code's undocumented nuron_list also marks 8 suppressed neurons, and 5 of them are among these 8 (35 of "
 "41 neurons agree). Variants: unpaired with onsets 9 neurons (2.291 to 1.297); signed-rank over time bins of mean "
 "counts 13 and of smoothed curves 15; with every-ms presentations 4 to 16 neurons.")
O['fig1c-ff-remapping']['notes']=(
 "Under O1 b with onsets 8 neurons show FF-remapping (paper 23), with the normalized late FF response rising from "
 "0.792 +- 0.037 to 1.609 +- 0.111 (paper 0.90 to 1.30); the rise is there but none of the three numbers is within "
 "tolerance, so the partial rule (direction and one number) is not met. Reading O1 a cannot be tested. No variant "
 "reaches the count (9 to 19 neurons). The closest, the signed-rank test over time bins of the smoothed curves with "
 "onsets (19 neurons, 0.885 to 1.411) and the unpaired and time-bin tests with every-ms presentations (17 neurons, "
 "0.888 or 0.889 to 1.427 or 1.430), have only the fixation value within tolerance; they are outside O1 or O2 i and "
 "do not decide. The code's nuron_list marks 23 FF neurons; 26 of 41 neurons agree with it under O1 b. Whether O1 "
 "should hold a pairing over time bins is asked of a reader (questions/niknam-2019.yaml).")
O['fig1d-st-remapping']['notes']=(
 "Under O1 b with onsets 11 neurons show ST-remapping (paper 37), rising from 0.749 +- 0.046 to 1.629 +- 0.112 (paper "
 "0.83 to 1.35); no number within tolerance. Reading O1 a cannot be tested. The outcome depends on the pairing: a "
 "signed-rank test over the 1 ms bins of the smoothed response curves gives 34 neurons, 0.815 to 1.365, all three "
 "numbers within tolerance, and agrees with the code's nuron_list on ST for 36 of 41 neurons (15 under O1 b). The "
 "Methods exclude that test (statistics on spike counts, \"not estimates of firing rate\") and the claims file does "
 "not list it, so it does not decide; whether O1 should hold a pairing over time bins is asked of a reader "
 "(questions/niknam-2019.yaml). On mean counts per bin the time-bin test gives 16 neurons with onsets and 29 with "
 "every-ms presentations (0.819 to 1.383); the unpaired test with every-ms presentations gives 31 (0.823 to 1.369). "
 "The ST probe is taken from probe_list, whose selection used the same perisaccadic increase.")
O['fig1e-ff-and-st-remapping']['notes']=(
 "Under O1 b with onsets 6 neurons show both effects (paper 22); FF 0.777 to 1.680 and ST 0.750 to 1.789, both rising, "
 "none of the five numbers within tolerance (the partial rule needs two). Reading O1 a cannot be tested. The variants "
 "give 6 to 19 neurons; the smoothed time-bin test with onsets (19 neurons) and the unpaired, time-bin and smoothed "
 "time-bin tests with every-ms presentations (17 neurons) have 3 of 5 numbers within tolerance, the others none. The "
 "code's nuron_list has 22 neurons with both. Asked of a reader with fig1d-st-remapping.")
O['fig1-remapping-longer-latency']['notes']=(
 "The smoothed (FWHM 13 ms) neuron-averaged fixation RF response of all 41 neurons peaks at 62 ms; the perisaccadic "
 "FF response of the FF-remapping neurons peaks at 108 ms and the ST response of the ST-remapping neurons at 99 ms "
 "under O1 b with onsets. Every testable reading gives RF 59-62 ms, FF 103-108 ms and ST 96-128 ms. The remapped peaks "
 "are not an independent test: the neurons are selected for an increase 80-150 ms after onset, which pulls the "
 "averaged peak into that window, and single-neuron peaks are spread (FF 12 to 150 ms, ST 0 to 150 ms). The RF peak, "
 "over all 41 neurons with no selection, is the part that does not depend on the selection. The selected populations "
 "are smaller than the paper's (8 and 11 neurons).")
O['fig1-example-neurons']['notes']=(
 "With onsets, three of four examples are matched on both values and a significant D2 test under O1 b: FF example "
 "2015071702 (7.83 to 18.96 spk/s, p 0.017), ST example 2015092707 (23.61 to 64.64, p 0.0059), example with both "
 "2015051115 (FF 15.76 to 39.10, p 0.00063; ST 16.05 to 36.17, p 0.00037). Perisaccadic means equal the paper's to the "
 "second decimal for 64.64, 39.10 and 36.17, so these are likely the paper's neurons. No neuron matches the RF "
 "example; 2015092709 has the paper's perisaccadic 40.49 +- 12.64 but a fixation rate of 56.94 +- 2.71 against 60.89 "
 "+- 2.82, and p 0.49 under O1 b (0.02 unpaired); fixation windows starting -560 to -440 ms and ending -160 to -40 ms "
 "give it 53.87 to 59.68, never 60.89. With every-ms presentations (variant) 2015083106 matches the RF example. The "
 "paper's p < 0.001 holds under O1 b only for the example with both effects; the unpaired test gives p 0.00011 or less "
 "for all three matched examples. Their fixation rates differ from the paper's by 0.07 to 0.19 spk/s with SEs equal "
 "within 0.01, and no single fixation window in the scan matches all three (closest -495 to -100 ms, within 0.054 "
 "spk/s); the paper's fixation set is not identified.")
bench=("The notebook ports the parameter selection of select_bases.m and times it on one neuron and probe: 290,628 "
 "stimulus-basis parameters and 58,125,600 single-parameter fits per neuron, about 7 ms per fit in this port, about "
 "1,050 hours on 4 CPUs for 41 neurons; a fully batched port evaluating only nonzero samples needs about 28 CPU hours, "
 "7 hours on the runner's 4 CPUs, in this run (timings vary between machines). That is over the 60 minute notebook "
 "limit and the five hours of an author run, for the selection step alone. Not run beyond that benchmark; no model "
 "was fitted.")
nmodel=(" The claim also needs the N-model, which the paper defines only through ref [48] (O8) and the code does not "
 "hold, so it would stay blocked as methods_underspecified with any compute budget.")
for o in A['outcomes']:
    if o.get('blocked_by')=='too_large':
        need=o['notes'].split('The notebook ports')[0].strip()
        o['notes']=need+' '+bench+(nmodel if o['claim'] in ('fig5a-s-f-beat-n-model','fig5b-st-remapping-better-than-n',
                     'fig5b-ff-remapping-a-model-only','fig5b-suppression-no-difference') else '')
        o['output']='claim:fig5a-s-model-perisaccadic-better'
for o in A['outcomes']:
    if o['claim'] in ('fig5b-ff-remapping-a-model-only','fig5b-suppression-no-difference'):
        print(o['notes'][:120])
F=A['findings']
F[1]['statement']=(
 "The paper and the descriptor say each probe lasted 7 ms with exactly one probe on screen at each time, and that "
 "\"In each condition, a complete sequence of 81 probe stimuli was presented throughout the length of a trial.\" In "
 "the files 91.5% of probe runs last 7 ms, 5.6% last 6 ms and others 14 or 21 ms, and the sequences contain gaps of "
 "10 to 21 ms with no probe (code 0). The probe order holds 75 codes in session 20150511 and 80 in 20150927 and "
 "20150929. In every session but 20150717 the order restarts from its first probe 35 to 296 ms after saccade onset "
 "in most trials, so each probe is shown 2 to 4 times per trial. The arrays are 3000 ms long with probes until 1468 "
 "to 2371 ms, while the paper gives trials of 2100 to 2300 ms.")
F[2]['statement']=(
 "The Methods test each effect with a one-sided Wilcoxon signed-rank test but do not say what is paired. Pairing by "
 "trial is impossible in these data, as no trial shows the same probe in both windows; pairing by condition gives 8 "
 "suppressed, 8 FF-remapping and 11 ST-remapping neurons against the paper's 8, 23 and 37. An unpaired test on "
 "every millisecond a probe is on gives 12, 17 and 31, and a signed-rank test over the 1 ms bins of the smoothed "
 "response curves gives 15, 19 and 34. Question for the authors: which presentations, pairs and test produced the "
 "classification of Figure 1 (and the nuron_list of main_lists.mat)? The example neurons' fixation rates also differ "
 "slightly from the paper's while their perisaccadic rates match (RF example 56.94 against 60.89 spk/s; FF, ST and "
 "both-effects examples 0.07 to 0.19 spk/s lower), and no single fixation window between -560 to -440 ms and -160 to "
 "-40 ms matches them all, so the fixation set used for Figure 1 is not the -500 to -100 ms the Methods give, or not "
 "only that.")
yaml.safe_dump(A,open(p,'w'),sort_keys=False,width=110,allow_unicode=True)
EOF
git diff --stat attempts/
```

```
Wed Nov 11 06:33:04 UTC 2026
Needs the S-model fitted per neuron (D4), the F- and A-models (ten fits each), 1000 simulated sequences per model and th
Needs the S-model fitted per neuron (D4), the F- and A-models (ten fits each), 1000 simulated sequences per model and th
 attempts/niknam-2019-01.yaml | 573 ++++++++++++++++++++++++-------------------
 1 file changed, 317 insertions(+), 256 deletions(-)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import yaml
p='attempts/niknam-2019-01.yaml'
A=yaml.safe_load(open(p))
model_reason=("Cell 28: parameter selection alone is 58.1 M single-parameter fits per neuron. That is about 2,081 CPU-h "
 "as ported, with a batched lower bound of 13 CPU-h, before the full fit, ten A-model fits and 1000-sequence "
 "simulations. The five claims that need the N-model are also blocked as methods_underspecified (O8, ref [48] not "
 "identified). That reason holds whatever the compute budget. The limits behind too_large are not stated, and the "
 "13 CPU-h lower bound (3.2 h on 4 CPUs) for selection alone is not prohibitive in itself (problem 6).")
model_resp=("No change of outcome. The notebook and the notes now state the limits: the 60 minute notebook limit and "
 "the five hours of an author run; this run's batched lower bound is about 28 CPU hours, 7 hours on 4 CPUs, for the "
 "selection step alone, and timings vary between machines. The notes of the four too_large claims that need the "
 "N-model now say they would stay blocked as methods_underspecified with any budget; fig5a-n-model-no-perisaccadic-gain "
 "keeps methods_underspecified as its main reason.")
R=[]
def add(c,outcome,reason,response): R.append(dict(claim=c,agrees=True,outcome=outcome,reason=reason,response=response))
add('probe-locations-link','reproduced',
 "Cell 9: all 41 files match a probe_list row and no row lacks a file. The recomputed RF is the listed probe for 38 "
 "neurons and the listed probe or a neighbour for 41 of 41 (the threshold is 37). The sign of FF minus RF gives 27 left "
 "and 14 right.","No change.")
add('methods-neuron-counts','reproduced',
 "Cell 11: 41 neurons in 11 sessions; 27 neurons in 9 sessions go left and 14 in 2 sessions go right. All four counts "
 "are exact. The 49 to 41 selection cannot be tested because the 8 dropped neurons are not deposited.","No change.")
add('fig1b-saccadic-suppression','reproduced',
 "Cell 16, reading (b, i): count 8. Fixation is 2.235 against 2.53+-0.37 and perisaccadic is 1.239 against "
 "1.51+-0.29, and the response drops. Both values sit near the edge of tolerance. Only about 5 of the 8 neurons are "
 "the authors' (35/41 agreement with nuron_list, cell 31); the match on 8 may partly be chance (problem 4).",
 "No change of outcome. Reading (a) is now reported as not testable instead of a count of 0 (problem 1), with the "
 "data check showing that no trial has a probe in both windows. The conclusion and notes say the values are near the "
 "edge of tolerance and that 5 of the 8 neurons are in nuron_list; a per-neuron table by name gives nuron_list and the "
 "p of each pairing (reference section). The dead branch in population (problem 8) is removed.")
for c,cnt in (('fig1c-ff-remapping',"Cell 18, (b, i): count 8 against 23+-2.3; 0.792 and 1.609 are both out of tolerance. The direction holds but no number does."),
              ('fig1d-st-remapping',"Cell 20, (b, i): count 11 against 37+-3.7; 0.749 and 1.629 are out of tolerance."),
              ('fig1e-ff-and-st-remapping',"Cell 22, (b, i): count 6 against 22, with 0 of 5 numbers in tolerance. The partial rule needs at least 2.")):
    add(c,'not_reproduced',cnt+(" Reading (a) gives 0 pairs for all 41 neurons (problem 1). The notebook's own outputs "
      "suggest the paper did not use pairing (b); a signed-rank test over the ms bins of the window, which the Methods "
      "wording also allows, is covered by neither O1 nor the notebook, and the not_reproduced outcomes may reflect the "
      "pairing choice more than the data (problem 2)."),
      "No change of outcome. Two pairings over the 1 ms bins of the response window are added as variants, on mean "
      "counts and on the smoothed curves, with onsets and every-ms presentations, in every Figure 1 table. On mean "
      "counts they leave the outcome unchanged. On smoothed curves, which the Methods exclude (\"not estimates of firing "
      "rate\"), fig1d would be reproduced (34 neurons, 0.815 to 1.365) and fig1c and fig1e partially reproduced. Since "
      "the claims file lets only O1 a and b decide, this is asked of a reader in questions/niknam-2019.yaml, and the "
      "notes say so. Reading (a) is reported as not testable.")
add('fig1-remapping-longer-latency','reproduced',
 "Cell 24: the fixation RF peak is at 62 ms, and the perisaccadic FF and ST peaks are at 108 and 99 ms under (b, i). "
 "Every other testable reading also stays inside 80-150 ms. The remapped peaks are partly forced by selecting neurons "
 "on an increase at 80-150 ms; per-neuron peaks scatter from 0 to 150 ms, and only the RF peak at 62 ms is an "
 "independent test (problem 5).",
 "No change of outcome. The conclusion and notes now say that the remapped peaks depend on the selection and that the "
 "RF peak is the part that does not.")
add('fig1-example-neurons','partially_reproduced',
 "Cell 26, onset reading: the FF (2015071702), ST (2015092707) and FF+ST (2015051115) examples match on values and on "
 "D2(b) p < 0.05. No neuron matches the RF example. The every-ms variant matches all four, but it does not decide. "
 "For every matched example the perisaccadic values match to about 0.01 spk/s but the fixation values are off, so the "
 "paper's fixation set differs from -500 to -100 ms as implemented here; the notebook did not investigate this, and "
 "it decides the RF example (problem 3).",
 "No change of outcome. The notebook now prints the p of every pairing for the matched and closest neurons (unpaired "
 "p 0.00011 or less for the three matched examples) and scans the fixation window (start -560 to -440 ms, end -160 to "
 "-40 ms). The SEs of the matched examples agree with the paper's within 0.01, but no window matches all three means "
 "(closest -495 to -100 ms, within 0.054 spk/s), and the RF candidate 2015092709 reaches 53.87 to 59.68, never 60.89. "
 "The fixation set is not identified; this is added to the methods_unavailable finding. The saccade index was also "
 "shifted by one ms either way: the perisaccadic values then no longer match the paper's (checked while preparing, "
 "not in the notebook), so it is kept.")
for c in ['fig3-example-trial-predictions','fig5a-n-model-no-perisaccadic-gain','fig5a-s-model-perisaccadic-better',
 'fig5a-f-model-perisaccadic-better','fig5a-s-f-beat-n-model','fig5b-st-remapping-better-than-n','fig5b-ff-remapping-a-model-only',
 'fig5b-suppression-no-difference','fig5c-f-higher-ratio-than-s','fig5c-source-contributions','fig5c-percent-changes',
 'fig6a-model-saccadic-suppression','fig6b-model-ff-remapping','fig6c-model-st-remapping','fig6d-model-ff-and-st-remapping',
 'fig6-example-neuron-predictions','fig7-prevalence-maps-correlate','fig7-experimental-maps-lower','fig8c-example-neuron-detectability',
 'fig8d-equal-detectability-at-55ms','fig8e-example-neuron-time-course','fig8e-population-ff-detectability',
 'fig8e-population-st-detectability','figs4-f-model-share-of-s-model','figs5-spike-history-no-effect']:
    add(c,'blocked',model_reason,model_resp)
add('figs1-rf-centres','blocked',
 "The files hold only 9x9 grid codes, and the paper gives only ranges of grid extent and spacing. The bucket listing "
 "(mt-3/live/) and filelist.txt hold only data.zip, the descriptor (pdf and docx), example_scripts.zip and "
 "checksums.md5; DemoScript.m plots the grid in probe units only. No grid position or spacing exists anywhere in the "
 "archive, so figs1 cannot be tested even in part.","No change.")
assert len(R)==34, len(R)
claims={o['claim'] for o in A['outcomes']}; assert claims=={r['claim'] for r in R}
A['verifications']=[dict(date='2026-11-11',kind='agent',
  by='Independent agent run by CatalystNeuro (same harness, separate context, did not write the notebook)',
  reviewed=("Round 1. The handover of the author run (commit 2650729e; author-answers changed no entry file): the "
   "executed notebook with the conclusion cells and the summary removed, the helper module and the claims file, with "
   "the paper. The verifier also listed the archive and tested the helper functions on synthetic input. In reply: the "
   "per-neuron table against nuron_list, the p values of every pairing for the example neurons and all 41 neurons, the "
   "fixation-window scan, and the number of onsets and of presentations of each probe per trial were added, as the "
   "report's section C asked. The probe order is now explained in the data check (problem 7): it restarts after the "
   "saccade, which breaks the blocks of 81, three sessions use 75 or 80 codes, and a 14 or 21 ms run takes one place "
   "in the order. The docx version of the descriptor was not compared with the pdf."),
  results=R)]
yaml.safe_dump(A,open(p,'w'),sort_keys=False,width=110,allow_unicode=True)
print('ok')
EOF
```

```
ok
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
import json
p='entries/niknam-2019/reproduce_niknam_2019.ipynb'
nb=json.load(open(p)); C=nb['cells']
s=''.join(C[33]['source'])
add='''
# Saccade index one ms either way (tsaccade - 2, - 1 as used, and tsaccade): fixation and
# perisaccadic rates of the closest neurons.
off_rows = []
for ex, parts in EX.items():
    n = closest[ex]; d = byname[n]
    for eff, loc, ef, tf, ep, tp in parts:
        _, peri, win, _ = SPECS[eff]
        tr, t = mt3.presentations(d, PROBES[n][loc])
        cr = mt3.counts(d, tr, t, win) * 1000.0 / (win[1] - win[0] + 1)
        for off in (-1, 0, 1):
            rel = t - (d["sacc"][tr] + off)
            off_rows.append(dict(example=ex, probe=loc, shift_ms=off, fix=cr[(rel >= -500) & (rel <= -100)].mean(),
                                 peri=cr[(rel >= peri[0]) & (rel <= peri[1])].mean(), paper_fix=ef, paper_peri=ep))
print(pd.DataFrame(off_rows).round(2).to_string(index=False))
'''
C[33]['source']=(s.rstrip('\n')+'\n'+add.strip('\n')).splitlines(keepends=True)
json.dump(nb,open(p,'w'),indent=1,ensure_ascii=False); open(p,'a').write('\n')
EOF
python tools/entry.py all entries/niknam-2019 2>&1 | tail -3
```

```
Installed kernelspec registry-niknam-2019 in executed/niknam-2019/.venv/share/jupyter/kernels/registry-niknam-2019
0 error(s)
pass  reproduce_niknam_2019.ipynb  (68 s)
```

**Agent calls Bash**

```bash
cd executed/niknam-2019 && python3 - <<'EOF'
import json
nb=json.load(open('reproduce_niknam_2019.ipynb'))
for i in (15,33,36):
    outs=[''.join(o.get('text','')) for o in nb['cells'][i].get('outputs',[])]
    print('-----',i); print('\n'.join(outs)[-2600:] if i==33 else '\n'.join(outs))
EOF
```

```
----- 15
Neurons significant by D2 under each reading (paper: 8, 23, 37, 22)
         pairing presentations  decides  pairs_median  neurons_testable  suppression           ff           st    ff_and_st
           trial         onset     True           0.0                 0 not testable not testable not testable not testable
       condition         onset     True          30.0                41            8            8           11            6
        unpaired         onset    False           0.0                41            9           10           24           10
         timebin         onset    False          71.0                41           13           10           16            9
timebin_smoothed         onset    False          71.0                41           15           19           34           19
           trial         every    False           0.0                 0 not testable not testable not testable not testable
       condition         every    False          34.0                41            4            9            9            6
        unpaired         every    False           0.0                41           12           17           31           17
         timebin         every    False          71.0                41           13           17           29           17
timebin_smoothed         every    False          71.0                41           16           17           32           17
     supp_n_fix  supp_n_peri  ff_n_fix  ff_n_peri  st_n_fix  st_n_peri
min       117.0          8.0     130.0       17.0     137.0       10.0
50%       425.0         30.0     420.0       60.0     420.0       50.0
max       592.0         51.0     601.0       80.0     597.0       92.0

----- 33
aN      0.092   4.5e-05   0.0014           4.6e-11
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && python3 - <<'EOF'
p='entries/niknam-2019/reproduce_niknam_2019.ipynb'
s=open(p).read()
for a,b in [("about 1,050 hours on 4 CPUs for the 41 neurons","about 1,000 hours on 4 CPUs for the 41 neurons"),
            ("The paper's fixation set is not identified.\"","Shifting the saccade index by 1 ms either way moves the perisaccadic rates away from the paper's (40.49 becomes 44.87 or 33.94) and the fixation rates by 0.11 spk/s at most. The paper's fixation set is not identified.\"")]:
    assert s.count(a)==1,(a,s.count(a)); s=s.replace(a,b)
open(p,'w').write(s)
p='attempts/niknam-2019-01.yaml'
s=open(p).read()
n=s.count('1,050 hours'); s=s.replace('1,050 hours','1,000 hours'); print(n)
open(p,'w').write(s)
EOF
grep -n "checked while preparing" attempts/niknam-2019-01.yaml
```

```
24
638:      the paper''s (checked while preparing, not in the notebook), so it is kept.'
```

**Agent calls Bash**

```bash
sed -n 630,640p attempts/niknam-2019-01.yaml
```

```
fixation values are off, so the paper''s fixation set differs from -500 to -100 ms as implemented here; the
      notebook did not investigate this, and it decides the RF example (problem 3).'
    response: 'No change of outcome. The notebook now prints the p of every pairing for the matched and closest
      neurons (unpaired p 0.00011 or less for the three matched examples) and scans the fixation window (start -560
      to -440 ms, end -160 to -40 ms). The SEs of the matched examples agree with the paper''s within 0.01, but
      no window matches all three means (closest -495 to -100 ms, within 0.054 spk/s), and the RF candidate 2015092709
      reaches 53.87 to 59.68, never 60.89. The fixation set is not identified; this is added to the methods_unavailable
      finding. The saccade index was also shifted by one ms either way: the perisaccadic values then no longer match
      the paper''s (checked while preparing, not in the notebook), so it is kept.'
  - claim: fig3-example-trial-predictions
    agrees: true
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='attempts/niknam-2019-01.yaml'
s=open(p).read()
a="""The saccade index was also shifted by one ms either way: the perisaccadic values then no longer match
      the paper''s (checked while preparing, not in the notebook), so it is kept.'"""
assert a in s
s=s.replace(a,"""The notebook also shifts the saccade index by one ms either way: the perisaccadic values then move away from
      the paper''s (40.49 becomes 44.87 or 33.94) and the fixation values change by 0.11 spk/s at most, so the index
      is kept.'""")
open(p,'w').write(s)
EOF
python tools/entry.py all entries/niknam-2019 2>&1 | tail -3; date -u
```

```
Installed kernelspec registry-niknam-2019 in executed/niknam-2019/.venv/share/jupyter/kernels/registry-niknam-2019
0 error(s)
pass  reproduce_niknam_2019.ipynb  (71 s)
Wed Nov 11 06:36:41 UTC 2026
```

**Agent calls Bash**

```bash
ls tools; python tools/entry.py check entries/niknam-2019 2>&1 | tail -5
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
backfill_summaries.py
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_reuse_targets.py
build_site.py
build_targets.py
changed_entries.py
claims_check.py
colab.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
[... 16 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "attempts/\|def check" tools/entry.py | head -20; ls tests | head;
```

```
172:def check(entry_dir: Path) -> Report:
test_agent_run.py
test_build_site.py
test_build_targets.py
test_claims_check.py
test_datasets.py
test_encore.py
test_entry_tool.py
test_flagged.py
test_notify.py
test_paper_match.py
```

**Agent calls Bash**

```bash
sed -n 172,260p tools/entry.py | grep -n "attempt\|question\|schema"
```

```
73:    # Claims and attempts that go with this entry.
89:    mine = [p for p in sorted((ROOT / "attempts").glob("*.yaml"))
```

**Agent calls Bash**

```bash
sed -n 1,80p tools/entry.py | grep -n "attempt" ; grep -n "def check_attempt\|attempt.schema" tools/*.py | head
```

```
13:`check` validates entry.yaml, and the claims and attempt files that mention
79:    """The identifier of the one dataset a claims file or attempt record is about, in its archive: None for a
80:    paper's own claims file (claims/<paper>.yaml) and for an attempt on several datasets."""
```

**Agent calls Bash**

```bash
cat entries/niknam-2019/README.md
```

```
# Niknam et al. (2019) from CRCNS mt-3

Tests the findings of [Niknam et al. (2019)](https://doi.org/10.1371/journal.pcbi.1007275) on
[CRCNS mt-3](https://doi.org/10.6080/K0FB514J), the spike trains, probe sequences and saccade
times of the paper's 41 MT neurons. The RF, FF and ST probes come from the paper's code
repository (https://github.com/nnategh/SFA-Models at commit 1438dde).

| Claim | Outcome |
|---|---|
| The code's RF, FF and ST probes link to the neurons | Reproduced |
| 41 neurons, 11 sessions, 27 leftward and 14 rightward | Reproduced |
| Saccadic suppression in 8 neurons (Figure 1B) | Reproduced |
| FF-remapping in 23 neurons (Figure 1C) | Not reproduced |
| ST-remapping in 37 neurons (Figure 1D) | Not reproduced |
| Both remapping effects in 22 neurons (Figure 1E) | Not reproduced |
| Remapped responses come later than RF responses | Reproduced |
| Example neurons of Figure 1 | Partially reproduced |
| N-model comparison (Figure 5A) | Blocked: methods underspecified |
| S-, F- and A-model claims (Figures 3, 5 to 8, S4, S5; 24 claims) | Blocked: too large |
| RF centres in degrees (Figure S1) | Blocked: metadata insufficient |
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
p='entries/niknam-2019/README.md'
s=open(p).read()
a="A failure to reproduce here"
s=s.replace(a,"""The remapping counts depend on what the paper's signed-rank test pairs, which the Methods do not
say; whether the claims file should include a pairing over time bins is asked of a reader in
[`questions/niknam-2019.yaml`](../../questions/niknam-2019.yaml).

"""+a,1)
open(p,'w').write(s)
EOF
grep -n "—\|rather" entries/niknam-2019/README.md entries/niknam-2019/mt3.py entries/niknam-2019/reproduce_niknam_2019.ipynb attempts/niknam-2019-01.yaml questions/niknam-2019.yaml | head; python3 -c "
import yaml
for f in ['attempts/niknam-2019-01.yaml','questions/niknam-2019.yaml']: yaml.safe_load(open(f))
print('yaml ok')"; git status --short
```

```
yaml ok
 M attempts/niknam-2019-01.yaml
 M entries/niknam-2019/README.md
 M entries/niknam-2019/mt3.py
 M entries/niknam-2019/reproduce_niknam_2019.ipynb
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
?? questions/niknam-2019.yaml
?? scripts
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/niknam-2019 2>&1 | tail -2; git diff --stat
```

```
0 error(s)
 attempts/niknam-2019-01.yaml                    | 1011 +++++++++++++++++------
 entries/niknam-2019/README.md                   |    4 +
 entries/niknam-2019/mt3.py                      |   21 +-
 entries/niknam-2019/reproduce_niknam_2019.ipynb |  242 +++++-
 4 files changed, 976 insertions(+), 302 deletions(-)
```

**Agent**

No outcome changed. The verifier agreed with all 34 outcomes, and nothing in the new outputs moves any of them. I re-ran the entry with `python tools/entry.py all entries/niknam-2019`: the check reports 0 errors and the notebook ran in 71 s.

The outcomes stay as before:
- **Reproduced (4):** probe-locations-link, methods-neuron-counts, fig1b, fig1-remapping-longer-latency.
- **Partially reproduced (1):** fig1-example-neurons.
- **Not reproduced (3):** fig1c, fig1d, fig1e.
- **Blocked (26):** 24 model claims as too large, the N-model claim as methods underspecified, and figs1 as metadata insufficient.

**What I added or corrected, by point in the report:**
- **Pairing by trial (problem 1):** this reading is now shown as "not testable" instead of counts of 0. A new data check explains why. In no session does a trial show a probe in both the fixation and the perisaccadic window, because a probe comes back only after the whole probe order has played, a median 562 to 604 ms later.
- **Pairing (problem 2, and C2):** I added two variant pairings over the 1 ms bins of the response window, one on mean counts and one on smoothed curves. They appear in every Figure 1 table.
  - On mean counts, fig1c, fig1d and fig1e still fail.
  - On smoothed curves, fig1d would be reproduced (34 neurons, 0.815 to 1.365), and fig1c and fig1e would be partially reproduced. This variant agrees with the code's `nuron_list` on ST for 36 of 41 neurons. The Methods exclude it, though ("not estimates of firing rate").
  - Because the claims file lets only pairing by trial or by condition decide, I asked a reader in the new `questions/niknam-2019.yaml` whether that list should include a pairing over time bins. The claim notes say this.
- **Fixation values of the example neurons (problem 3, and C3):** I added a scan of the fixation-window boundaries and a ±1 ms shift of the saccade index. Our standard errors match the paper's to within 0.01. Even so, no single window matches the means of all three matched examples; the closest, -495 to -100 ms, is off by up to 0.054 spk/s. The RF example's candidate neuron reaches 53.87 to 59.68 spk/s, never 60.89. Shifting the saccade index moves the perisaccadic values away from the paper's, so I kept it. The paper's fixation set is still not identified, and this is now part of the methods finding.
- **Overlap with the authors' list (problem 4, and C1):** I added a per-neuron table, by name, of `nuron_list` against the p-value under each pairing. The fig1b notes now say that 5 of the 8 suppressed neurons are the authors'.
- **Latency claim (problem 5):** the conclusion now says the remapped peaks partly follow from how neurons are selected, and that the RF peak at 62 ms is the independent part.
- **Compute limits (problem 6):** the notes now name the limits: the 60-minute notebook limit and the 5 hours of an author run. This run's lower bound for the parameter-selection step alone is about 28 CPU hours, 7 hours on 4 CPUs. The four too-large claims that also need the N-model now say they would stay blocked as methods underspecified with any compute budget.
- **Probe order (problem 7, and C4):** the data check now prints, per session, onsets per trial, probe codes per trial, presentations of each probe per trial, and where the order restarts.
  - Three sessions use 75 or 80 codes instead of 81.
  - In most trials of every session except 20150717, the order restarts from its first probe 35 to 296 ms after the saccade. This is why only 7.6% of trials passed the check for blocks of 81.
  - A 14 or 21 ms run takes one place in the order, so it is one probe held longer.
  - I added these facts to the metadata finding.
- **Dead code (problem 8):** removed.
- **Record:** the round is recorded under `verifications`, quoting the report's reasons, with a response for each claim. The README now points to the reader question.

**Not done:** I did not compare the docx version of the data descriptor with the pdf. I did not commit or push.

## End of run

66 turns, 16 minutes, $4.48 at API prices, result: success.
