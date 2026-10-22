# 000128 · author · run 39810757909

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
cat docs/protocol.md; ls; ls claims/000128 entries paper attempts | head -80
```

```
<persisted-output>
Output too large (29.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/5eee1a2a-53fa-4cd0-a40e-45a2f2bb13da/tool-results/bas6tp5k5.txt

Preview (first 2KB):
# Protocol for an attempt

Version: `pilot-10`. Record this version in the attempt's provenance.

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
[... 23 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/5eee1a2a-53fa-4cd0-a40e-45a2f2bb13da/tool-results/bas6tp5k5.txt"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-10`. Record this version in the attempt's provenance.
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
18	  claim, and it asks a reader for any method detail the file lacks.
19	- The **verifier** checks the author's work and must not be the author.
20	
[... 569 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000128/*.yaml; ls paper; cat README.md | head -100
```

```
<persisted-output>
Output too large (51.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/5eee1a2a-53fa-4cd0-a40e-45a2f2bb13da/tool-results/b6yo6b88y.txt

Preview (first 2KB):
# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset
# 000128.
# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, protocol
# pilot-10 as stated in docs/protocol.md.
#
# Text read: the accepted author manuscript in PubMed Central (PMC2991102, NIHMS240235), full text
# with Results, Methods and figure legends, and its supplement (NIHMS240235-supplement-01.pdf,
# Supplemental Figures 1 to 5 with legends, Supplemental Text and Supplemental Experimental
# Procedures), as extracted under paper/. The version of record and the main figures were not seen,
# only their legends; no PDF of the main text was supplied.
#
# Code: the paper links no code and names no repository (it says only that regressions were done in
# Matlab). No code was read. Every method below is from the Methods, the legends or the supplement.
#
# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
# Procedures). Three adult male rhesus monkeys (A, B, J, about 10 kg) made delayed reaches on a
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-reproduction-registry-reproduction-registry/5eee1a2a-53fa-4cd0-a40e-45a2f2bb13da/tool-results/b6yo6b88y.txt"
}
```

```
1	# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset
2	# 000128.
3	# Written by an agent (model "claude-opus-5-5", Claude Code in GitHub Actions), 2026-10-22, protocol
4	# pilot-10 as stated in docs/protocol.md.
5	#
6	# Text read: the accepted author manuscript in PubMed Central (PMC2991102, NIHMS240235), full text
7	# with Results, Methods and figure legends, and its supplement (NIHMS240235-supplement-01.pdf,
8	# Supplemental Figures 1 to 5 with legends, Supplemental Text and Supplemental Experimental
9	# Procedures), as extracted under paper/. The version of record and the main figures were not seen,
10	# only their legends; no PDF of the main text was supplied.
11	#
12	# Code: the paper links no code and names no repository (it says only that regressions were done in
13	# Matlab). No code was read. Every method below is from the Methods, the legends or the supplement.
14	#
15	# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
16	# Procedures). Three adult male rhesus monkeys (A, B, J, about 10 kg) made delayed reaches on a
17	# fronto-parallel screen; hand tracked optically at 60 Hz (0.35 mm), eye at 240 Hz. A trial is a
18	# touch-spot hold of at least 400 ms, target onset (the target jitters, 2 mm SD), a delay of about 0
19	# to 1000 ms, then the go cue (jitter stops, touch spot disappears) and the reach. Four datasets.
20	# - Monkeys A and B, speed task, single electrodes; 7 directions x 2 distances x 2 instructed speeds
[... 651 more lines not kept]
```

**Agent calls Bash**

```bash
cat docs/design.md | head -150; echo ----; cat docs/archives.md
```

```
# Reproduction registry: design

Status: draft for discussion. "Reproduction registry" is a working name.

## Goal

Agents work through the dandisets on the DANDI Archive that have an associated
paper. For each one, an agent tries to reproduce the paper's key findings and
figures from the open data, writes the analysis as a notebook, and registers it
here. People can deposit too, but most deposits are expected to come from
agents.

This serves two purposes:

1. **Check the data.** A finding that can be reproduced shows the dandiset is
   complete and accurate enough to support it. A finding that cannot be
   reproduced, with the reason, tells the data owner and the archive what is
   missing.
2. **Give analysts a starting point.** Someone who wants to test a new
   hypothesis on a dandiset starts from notebooks that already load the data
[... 228 more lines not kept]
```

**Agent calls Bash**

```bash
ls -la entries/001453-fouke-2025/ ; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in; cat attempts/001453-fouke-2025-01.yaml | head -150; ls questions | head; cat tools/entry.py | head -80
```

```
total 124
drwxr-xr-x  2 runner runner  4096 Oct 22 16:04 .
drwxr-xr-x 62 runner runner  4096 Oct 22 16:04 ..
-rw-r--r--  1 runner runner  2158 Oct 22 16:04 README.md
-rw-r--r--  1 runner runner   914 Oct 22 16:04 entry.yaml
-rw-r--r--  1 runner runner 16218 Oct 22 16:04 omr.py
-rw-r--r--  1 runner runner 79403 Oct 22 16:04 reproduce_fouke_2025.ipynb
-rw-r--r--  1 runner runner    61 Oct 22 16:04 requirements.in
-rw-r--r--  1 runner runner  5989 Oct 22 16:04 requirements.lock.txt
schema_version: 1
name: 001453-fouke-2025
type: reproduction
title: Optomotor swimming of zebrafish and Danionella cerebrum (Fouke et al. 2025)
description: Tests the freely swimming findings of Fouke, He, Loring and Naumann (2025) on dandiset
  001453, which holds the tracking data of 25 zebrafish and 12 Danionella cerebrum larvae during the
  optomotor protocol. It compares swimming speed, turning and angular acceleration between species
  and stimuli, the response to monocular stimuli, and how steady the swimming is. The imaging and
  head-fixed tail tracking of the paper's Figures 2 to 4 are not in the dandiset.
license: Apache-2.0
notebooks:
[... 258 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 150,400p attempts/001453-fouke-2025-01.yaml | grep -n -A12 "blocked\|^findings\|^verif" | head -120; cat questions/README.md; cat questions/000006.yaml | head -60
```

```
49:  outcome: blocked
50:  blocked_by: metadata_insufficient
51-  notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
52-    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the
53-    dandiset gives no mapping from those folders to its subjects, nor the original file names.
54-- claim: fig2d-shared-architecture
55:  outcome: blocked
56:  blocked_by: data_missing
57-  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
58-    tracking. The GitLab repository the paper names for "all behavioral and imaging data" holds
59-    notebooks only, and no other dandiset of this lab or paper was found on the archive.
60-- claim: fig2g-dsi-similar
61:  outcome: blocked
62:  blocked_by: data_missing
63-  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
64-- claim: fig2h-fewer-motion-responsive
65:  outcome: blocked
66:  blocked_by: data_missing
67-  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
68-- claim: fig2k-more-monocular
[... 118 more lines not kept]
```

**Agent**

Now the dataset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000128/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000128/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/000128/versions/0.220113.0400/" | python -m json.tool | head -150; curl -s "https://api.dandiarchive.org/api/dandisets/000128/versions/0.220113.0400/assets/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && . env/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy scipy pandas 2>&1 | tail -3; python -c "import pynwb; print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > insp.py <<'EOF'
import remfile, h5py, pynwb, requests, sys
from dandi.dandiapi import DandiAPIClient
c=DandiAPIClient(); ds=c.get_dandiset("000128","0.220113.0400")
for a in ds.get_assets():
    url=a.get_content_url(follow_redirects=1, strip_query=True)
    print("=====",a.path,url)
    f=h5py.File(remfile.File(url),'r')
    nwb=pynwb.NWBHDF5IO(file=f,load_namespaces=True).read()
    print(nwb)
    print("desc",nwb.session_description, nwb.experiment_description, nwb.session_start_time, nwb.subject)
    for k,v in nwb.processing.items():
        print("proc",k,list(v.data_interfaces))
        for n,di in v.data_interfaces.items():
            print("  ",n,di)
    print("acq",list(nwb.acquisition))
    tr=nwb.trials.to_dataframe() if nwb.trials is not None else None
    if tr is not None:
        print(tr.columns.tolist()); print(tr.head(10).T); print(len(tr))
        for col in nwb.trials.columns: print(col.name, '|', col.description)
    u=nwb.units
    print(u.colnames, len(u))
    for col in u.columns: print(col.name,'|',col.description)
    ud=u.to_dataframe()
    print(ud.drop(columns=['spike_times'],errors='ignore').head(10).T)
    print(nwb.electrodes.to_dataframe().head().T if nwb.electrodes is not None else None)
    if nwb.electrodes is not None: 
        e=nwb.electrodes.to_dataframe(); print(len(e)); print(e.describe(include='all').T)
    print(nwb.electrode_groups, nwb.devices, nwb.intervals)
EOF
python insp.py 2>&1 | head -300
```

```
===== sub-Jenkins/sub-Jenkins_ses-full_desc-test_ecephys.nwb https://dandiarchive.s3.amazonaws.com/blobs/faf/1f3/faf1f307-a06d-464c-8700-a659ab94ce2a
root pynwb.file.NWBFile at 0x133309832225392
Fields:
  devices: {
    electrode_array_M1 <class 'pynwb.device.Device'>,
    electrode_array_PMd <class 'pynwb.device.Device'>
  }
  electrode_groups: {
    electrode_group_M1 <class 'pynwb.ecephys.ElectrodeGroup'>,
    electrode_group_PMd <class 'pynwb.ecephys.ElectrodeGroup'>
  }
  electrodes: electrodes <class 'pynwb.ecephys.ElectrodesTable'>
  experiment_description: Center-out delayed reaching task with maze barriers
  experimenter: ['Mark M. Churchland' 'Matthew T. Kaufman']
  file_create_date: [datetime.datetime(2021, 9, 2, 0, 32, 11, 612762, tzinfo=tzoffset(None, -14400))]
  identifier: bda8ff86-0ba6-11ec-93c2-ab1d5afd05f0
  institution: Stanford University
  intervals: {
    trials <class 'pynwb.epoch.TimeIntervals'>
  }
[... 280 more lines not kept]
```

**Agent calls Bash**

```bash
wc -c paper/*; grep -n -i "proto\|delay > 400\|400 ms\|movement onset was\|onset" paper/10.1016-j.neuron.2010.09.015.txt | head -50
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; fold -s -w 200 10.1016-j.neuron.2010.09.015.txt > $TMPDIR/paper.txt; wc -l $TMPDIR/paper.txt; grep -n "Experimental Procedures\|Methods\|Task design\|Neural recordings and datasets\|PCA-based spaces\|Task spaces\|PD performance" $TMPDIR/paper.txt | head -30
```

```
1062 /tmp/claude-1001/paper.txt
65:during the preparatory and peri-movement epochs ( Methods ). A neuron's tuning in one epoch is then described by a vector of firing rates, with one entry per condition. We intentionally chose to not 
104:well a PD in this four-dimensional space captures the pattern of preparatory activity ( Figure 5F ). We refer to spaces constructed in this manner as ‘task’ spaces. Task spaces are constructed by the 
109:Testing preparatory tuning in PCA-based spaces A presumed purpose of preparatory tuning is for changes in a given neuron's activity to contribute, in a small but specific way, to changes in some 
127:time-varying kinematic variables or EMG records for peri-movement activity). Most tested spaces were greater than 2-dimensional. Figure 5F,G plots PD performance in a 4-dimensional task space and a 
131:( Methods ). PD performance in a variety of spaces We quantified the ability of the PD, in each space, to account for preparatory tuning ( Figure 6 ). Points above zero indicate performance 
137:activity truly depends upon. Performance of the PCA-based spaces is plotted for a range of dimensionalities (values of k ). Performance typically improved with dimensionality. This increase is 
146:was computed for spaces of 3 dimensions or less. The other subpanels allow spaces up to 6 and 12 dimensions. For PCA-based spaces, if the best dimensionality was less than the maximum dimensionality 
152:First, when using a PD to capture a given neuron's preparatory activity, the peri-movement space was based on the responses of all the other neurons ( Methods ). Second, because peri-movement 
228:will produce movement. Methods Task design and behavior Animal protocols were approved by the Stanford University Institutional Animal Care and Use Committee. Our basic methods have been described 
246:neuron, but all other variables differ. The vector b can be represented as g *PD: a gain times a preferred direction of unit length. Task spaces The ‘ target
[... 11 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 55,
 "limit": 240
}
```

```
55	clear preparatory tuning, preferences are not maintained between the preparatory and peri-movement epochs (color ordering differs between epochs). Furthermore, peri-movement activity was often 
56	complex and multiphasic ( Churchland and Shenoy, 2007b ; Sergio et al., 2005 ). These neurons show negative correlations between preparatory and peri-movement tuning. Figure 3 plots responses of six 
57	neurons recorded using the maze task. Panels A-D plot single-electrode recordings (27 conditions). Panels E-F plot array-based recordings (108 conditions). Some neurons maintained similar tuning 
58	between preparatory and peri-movement epochs (panel A ) but most did not. Also, while most neurons showed a rough directional preference during the preparatory period ( insets ), it was not uncommon 
59	for a few (panel B ) or even many (panels E,F ) conditions to evoke activity not easily explained by a pure directional preference. Peri-movement response complexity is not due to noise, but is a 
60	real feature of most neural responses ( Churchland and Shenoy, 2007b ). Still, in Figure 3 response complexity is partly due to the variety of reach paths. Given this, it is worth stressing two 
61	things. First, any model regarding how preparatory activity leads to peri-movement activity should work for curved as well as straight reaches. Second, both peri-movement response complexity and the 
62	failure of preparatory tuning to predict peri-movement tuning are quite apparent even for simple center-out reaches ( Figure 2 ). Correlations between preparatory and peri-movement tuning Similar 
63	levels of preparatory activity can lead to opposing patterns of peri-movement activity (e.g., middlemost traces in Figure 2D and traces near top of Figure 3C ). Thus, it is not simply that tuning 
64	preferences can reverse; tuning is often weakly correlated between the two epochs (population analysis in Figure 4A-D ). To compute correlations, for each condition we took the average firing ra
[... 230 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 294,
 "limit": 20
}
```

```
294	targs + inst. spd. ’ was not included, but ‘ endpoints + max. spd. ’ was included). Subpanels plot performance for spaces of the indicated dimensionality or less. Bars plot SEs. Asterisks indicate 
295	performance significantly worse (p<0.001) than the best space. Figure 7 Further controls and analyses. A. Performance of the ‘shuffled’ peri-movement spaces, averaged over all the datasets. During 
296	shuffling, the firing rate for each neuron/condition, was either left intact (50% probability) or the peri-movement pattern was inverted. This was done by preserving activity up 150 ms before 
297	movement onset, and reflecting (vertically) all subsequent activity around the firing rate at that time. B. Performance (averaged across neurons) versus the start of the peri-movement interval. 
298	Performance was measured using the best dimensionality for that dataset/start-time. C. Performance of the peri-movement space for subsets of the original data. Performance was computed for a 
299	six-dimensional space, normalized, and averaged across datasets. Left-most bar : performance for all data. Gray bars : performance for sites with AP locations >= the median ( anterior ), <= to the 
300	median ( posterior ). Second black bar : performance when data were randomly subdivided. D. PD consistency for the peri-movement space versus that for a variety of other spaces. Kinematic and EMG 
301	spaces were chosen because they had performed the best overall (after the peri-movement space) in the analysis in Fig. 6 . ‘ Targs. + inst. speed ’ and ‘ segment directions ’ spaces were chosen 
302	because they performed well for the speed and maze tasks respectively. ‘ Targs. + inst. speed ’ was undefined for the maze task; the similar ‘ endpoints + max. spd. ’ space was analyzed instead. 
303	Figure 8 Illustration of the behavior of a simple linear dynamical system: a harmonic oscillator. A. Changes in the initial state produce a linear scaling of the subsequent activity pattern. In this
[... 10 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 965,
 "limit": 100
}
```

```
965	rate among conditions, and for not the overall average firing rate. 
966	 
967	
968	=== page 15 ===
969	!
970	Supplemental Experimental Procedures 
971	 
972	Task design and behavioral control 
973	Our basic methods have been described previously (Churchland et al., 2006c). 
974	Briefly, three adult male monkeys (monkeys A,B and J, Macaca mulatta, ~10 kg) sat in a 
975	customized chair with head restraint and performed the task on a fronto-parallel screen. 
976	The hand and eye were tracked optically (accuracy of 0.35 mm and ~1°, 60 and 240 Hz). 
977	On each task trial, a central touch spot was held (for at least 400 ms) and a reach target 
978	then appeared. This target initially jittered slightly (2 mm SD) in place, during which 
979	time the monkey could prepare his reach but was not yet allowed to move his hand. 
980	Following a variable (~0-1000 ms, the exact range varied across monkeys) delay, jitter 
981	ceased and the touch spot disappeared, providing the ‘go cue’ for the monkey to execute 
982	his reach. Monkeys rapidly learned that the jittering target could not be struck, and the 
983	hand was typically held very steady until the go cue. Allowable reaction times were 100-
984	500 ms (speed task) and 120-900 ms (maze task). Median reaction times were typically 
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > insp2.py <<'EOF'
import remfile, h5py, pynwb, numpy as np, pandas as pd
url="https://dandiarchive.s3.amazonaws.com/blobs/df3/e3f/df3e3f73-50ab-42b4-8827-82664ddd474a"
f=h5py.File(remfile.File(url),'r')
nwb=pynwb.NWBHDF5IO(file=f,load_namespaces=True).read()
tr=nwb.trials.to_dataframe()
print(tr.split.value_counts())
print(tr[['delay','rt','num_targets','num_barriers','trial_version','active_target']].describe())
print("types",tr.trial_type.nunique(), "mazes", tr.maze_id.nunique(), "type x version", tr.groupby(['trial_type','trial_version']).ngroups, "maze x version", tr.groupby(['maze_id','trial_version']).ngroups)
print(tr.groupby(['trial_type','trial_version']).size().describe())
print(pd.crosstab(tr.trial_version, tr.num_targets)); print(pd.crosstab(tr.trial_version, tr.num_barriers>0))
print("delay check", np.abs((tr.go_cue_time-tr.target_on_time)*1000-tr.delay).max(), "rt check", np.abs((tr.move_onset_time-tr.go_cue_time)*1000-tr.rt).max())
print("pre-go", (tr.go_cue_time-tr.start_time).min(), "post-move", (tr.stop_time-tr.move_onset_time).min(), (tr.stop_time-tr.move_onset_time).describe())
print("target_on-start", (tr.target_on_time-tr.start_time).describe())
print((tr.delay>400).sum())
for n in ['hand_pos','hand_vel','cursor_pos','eye_pos']:
    ts=nwb.processing['behavior'][n]
    d=f[f'processing/behavior/{n}/data']; t=f[f'processing/behavior/{n}/timestamps']
    print(n, d.chunks, d.compression, t.chunks, t[:5], t[-5:])
u=nwb.units.to_dataframe()
print(u.heldout.value_counts())
el=nwb.electrodes.to_dataframe()
u['grp']=[e.group_name.iloc[0] for e in u.electrodes]
u['eid']=[e.index[0] for e in u.electrodes]
print(pd.crosstab(u.grp,u.heldout)); print("units per electrode", u.eid.value_counts().value_counts())
ns=u.spike_times.apply(len); print(ns.describe())
st=np.concatenate(u.spike_times.values); print(st.min(), st.max())
print(u.index.tolist()[:20])
print(nwb.keywords[:])
EOF
python insp2.py 2>&1 | tail -80
```

```
mean    645.257952   349.341176  ...       0.985621       0.333333
std     241.389908    93.382084  ...       0.820542       0.667465
min      -3.000000   218.000000  ...       0.000000       0.000000
25%     515.000000   295.000000  ...       0.000000       0.000000
50%     665.000000   325.000000  ...       1.000000       0.000000
75%     848.000000   371.000000  ...       2.000000       0.000000
max     999.000000  1100.000000  ...       2.000000       2.000000

[8 rows x 6 columns]
types 36 mazes 36 type x version 108 maze x version 108
count    108.000000
mean      21.250000
std        2.091929
min       17.000000
25%       20.000000
50%       22.000000
75%       22.000000
max       27.000000
dtype: float64
num_targets      1    3
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > insp3.py <<'EOF'
import remfile, h5py, pynwb, numpy as np, pandas as pd
url="https://dandiarchive.s3.amazonaws.com/blobs/df3/e3f/df3e3f73-50ab-42b4-8827-82664ddd474a"
f=h5py.File(remfile.File(url),'r')
print(list(f['units'].keys()))
print(f['units/electrodes'][:30], f['units/electrodes_index'][:10])
print(f['units/id'][:])
el=f['general/extracellular_ephys/electrodes']
print(list(el.keys()))
loc=el['location'][:]; print(loc[:5], loc[90:100], np.unique(loc,return_counts=True)); print(el['id'][:5], el['id'][-5:])
g=el['group_name'][:]; print(np.unique(g,return_counts=True))
e=f['units/electrodes'][:]
print(np.unique(e), len(np.unique(e)))
for k in ['x','y','z','imp','filtering']: print(k, el[k][:3])
print(f['units/electrodes'].attrs.items())
EOF
python insp3.py
```

```
['electrodes', 'electrodes_index', 'heldout', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index']
[ 0  1  1  2  2  2  2  3  4  5  5  5  6  6  8  8  9  9 10 10 11 11 11 13
 14 15 15 16 17 17] [ 1  2  3  4  5  6  7  8  9 10]
[1011 1021 1022 1031 1032 1033 1034 1041 1051 1061 1062 1063 1071 1072
 1091 1092 1101 1102 1111 1112 1121 1122 1123 1141 1151 1161 1162 1171
 1182 1183 1191 1192 1193 1211 1231 1232 1233 1241 1251 1252 1261 1271
 1291 1292 1341 1361 1362 1372 1381 1401 1411 1421 1431 1441 1442 1461
 1471 1481 1501 1502 1511 1512 1541 1561 1562 1581 1582 1601 1661 1662
 1663 1691 1701 1702 1711 1721 1741 1751 1752 1761 1781 1791 1801 1812
 1831 1841 1851 1861 1881 1891 1901 1902 2051 2121 2131 2132 2151 2161
 2181 2191 2192 2231 2232 2241 2251 2252 2271 2272 2273 2281 2301 2302
 2311 2321 2331 2341 2351 2352 2361 2371 2381 2391 2392 2401 2412 2413
 2421 2422 2423 2431 2441 2451 2452 2453 2461 2471 2472 2481 2491 2492
 2501 2541 2542 2561 2571 2581 2591 2601 2602 2611 2612 2621 2631 2641
 2651 2691 2721 2731 2732 2741 2742 2751 2761 2762 2771 2791 2792 2801
 2811 2821 2841 2842 2861 2862 2871 2881 2882 2911 2931 2941 2951 2961]
['filtering', 'group', 'group_name', 'id', 'imp', 'location', 'x', 'y', 'z']
[b'PMd' b'PMd' b'PMd' b'PMd' b'PMd'] [b'PMd' b'PMd' b'PMd' b'PMd' b'PMd' b'PMd' b'M1' b'M1' b'M1' b'M1'] (array([b'M1', b'PMd'], dtype=object), array([96, 96]))
[1 2 3 4 5] [188 189 190 191 192]
(array([b'electrode_group_M1', b'electrode_group_PMd'], dtype=object), array([96, 96]))
[... 11 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > insp4.py <<'EOF'
import remfile, h5py, numpy as np
for url in ["https://dandiarchive.s3.amazonaws.com/blobs/df3/e3f/df3e3f73-50ab-42b4-8827-82664ddd474a","https://dandiarchive.s3.amazonaws.com/blobs/faf/1f3/faf1f307-a06d-464c-8700-a659ab94ce2a"]:
    f=h5py.File(remfile.File(url),'r')
    ids=f['units/id'][:]; e=f['units/electrodes'][:]; ei=f['units/electrodes_index'][:]
    print(len(ids),len(e), (np.diff(np.r_[0,ei])==1).all())
    ch=(ids//10)%100; arr=ids//1000
    print("e==ch-1 all:", (e==(ch-1)).all(), "array 1:", (arr==1).sum(), "array 2:", (arr==2).sum())
    print(list(zip(ids[90:100],e[90:100])))
    ho=f['units/heldout'][:]; print("heldout by array", [(a,ho[arr==a].sum()) for a in (1,2)])
    print(f['general'].keys())
    for k in f['general'].keys():
        try: print(k, f['general'][k][()])
        except Exception as ex: print(k,'group')
EOF
python insp4.py
```

```
182 182 True
e==ch-1 all: True array 1: 92 array 2: 90
[(np.int64(1901), np.int64(89)), (np.int64(1902), np.int64(89)), (np.int64(2051), np.int64(4)), (np.int64(2121), np.int64(11)), (np.int64(2131), np.int64(12)), (np.int64(2132), np.int64(12)), (np.int64(2151), np.int64(14)), (np.int64(2161), np.int64(15)), (np.int64(2181), np.int64(17)), (np.int64(2191), np.int64(18))]
heldout by array [(1, np.int64(24)), (2, np.int64(21))]
<KeysViewHDF5 ['devices', 'experiment_description', 'experimenter', 'extracellular_ephys', 'institution', 'keywords', 'lab', 'related_publications', 'session_id', 'subject']>
devices group
experiment_description b'Center-out delayed reaching task with maze barriers'
experimenter [b'Mark M. Churchland' b'Matthew T. Kaufman']
extracellular_ephys group
institution b'Stanford University'
keywords [b'motor cortex' b'premotor cortex' b'reaching' b'macaque'
 b'Neural Latents Benchmark']
lab b'Shenoy'
related_publications [b'https://doi.org/10.1016/j.neuron.2010.09.015']
session_id b'full'
subject group
137 137 True
e==ch-1 all: True array 1: 68 array 2: 69
[(np.int64(2421), np.int64(41)), (np.int64(2422), np.int64(41)), (np.int64(2423), np.int64(41)), (np.int64(2431), np.int64(42)), (np.int64(2441), np.int64(43)), (np.int64(2451), np.int64(44)), (np.int64(2452), np.int64(44)), (np.int64(2461), np.int64(45)), (np.int64(2472), np.int64(46)), (np.int64(2481), np.int64(47))]
heldout by array [(1, np.int64(0)), (2, np.int64(0))]
[... 13 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && uv pip install -q diptest scikit-learn matplotlib 2>&1|tail -2; python -c "
import diptest, numpy as np
x=np.r_[np.random.randn(100)-3, np.random.randn(100)+3]; print(diptest.diptest(x)); print(diptest.diptest(np.random.randn(200)))"
```

```
(0.10670148338271708, 0.0)
(0.020084893776931134, 0.8830717105953576)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import requests
r=requests.get("https://api.dandiarchive.org/api/dandisets/000128/versions/draft/assets/").json()
for a in r['results']: print(a['path'],a['blob'],a['size'],a['modified'])
r=requests.get("https://api.dandiarchive.org/api/dandisets/000128/versions/0.220113.0400/assets/",params={'path':'sub-Jenkins/sub-Jenkins_ses-full_desc-train'}).json()
print(r['count'], r['results'][0]['asset_id'])
h=requests.head("https://api.dandiarchive.org/api/assets/26e85f09-39b7-480f-b337-278a8f034007/download/",allow_redirects=False); print(h.status_code,h.headers.get('Location'))
EOF
```

```
sub-Jenkins/sub-Jenkins_ses-full_desc-test_ecephys.nwb faf1f307-a06d-464c-8700-a659ab94ce2a 3392688 2021-09-02T05:04:24.866192Z
sub-Jenkins/sub-Jenkins_ses-full_desc-train_behavior+ecephys.nwb df3e3f73-50ab-42b4-8827-82664ddd474a 690612247 2021-09-02T05:04:55.563735Z
1 26e85f09-39b7-480f-b337-278a8f034007
302 https://dandiarchive.s3.amazonaws.com/blobs/df3/e3f/df3e3f73-50ab-42b4-8827-82664ddd474a?response-content-disposition=attachment%3B%20filename%3D%22sub-Jenkins_ses-full_desc-train_behavior%2Becephys.nwb%22&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=[removed: an AWS key]%2F20261022%2Fus-east-2%2Fs3%2Faws4_request&X-Amz-Date=20261022T161126Z&X-Amz-Expires=21600&X-Amz-SignedHeaders=host&X-Amz-Signature=871c27329434640f281993976838cb9b0937c068fbdcb10c67e67679fe8fa631
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/000128-churchland-2010/mcmaze.py",
 "content": "\"\"\"Loading and measures for dandiset 000128 (MC_Maze, monkey Jenkins, maze task, two Utah arrays).\n\nUsed by the reproduction of Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68:387-400.\nWhere a parameter comes from is said next to it: \"M1\" to \"M9\" are the method headers of the claims\nfile claims/000128/10.1016-j.neuron.2010.09.015.yaml (which cite the paper), and \"standard choice\"\nmarks a detail that the claims file calls a standard choice or that cannot change a result.\n\nThe data are streamed from the archive with remfile and h5py and read with pynwb; nothing is\nwritten to disk.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport numpy as np\nimport pandas as pd\nimport requests\nimport remfile\nimport h5py\nimport pynwb\nfrom scipy.ndimage import gaussian_filter1d\n\nDANDISET_ID = \"000128\"\nVERSION = \"0.220113.0400\"          # the only published version; see the notebook header\nAPI = \"https://api.dandiarchive.org/api\"\nTRAIN_PATH = \"sub-Jenkins/sub-Jenkins_ses-full_desc-train_behavior+ecephys.nwb\"\nTEST_PATH = \"sub-Jenkins/sub-Jenkins_ses-full_desc-test_ecephys.nwb\"\n\nSIGMA_MS = 20        # M2, Gaussian of 20 ms, read as SD 20 ms (claims file: a standard choice)\nSTEP_MS = 10         # M2, rates sampled every 10 ms (claims file: a standard choice)\nPREP_WIN = (-200, 100)     # M4, ms from the go cue\nPERI_WIN = (-100, 350)     # M4, ms from movement onset\nTMAT_WIN = (-150, 800)     # M5, maze peri-movement T-matrix, ms from movement onset\nMIN_DELAY_MS = 400         # M1, trials with delay > 400 ms\nPROTO_R = 0.9              # M1, correlation with the proto-trial\nPROTO_WIN = (-150, 800)    # M1 (T1, T2), window of the velocity profiles, ms from movement onset\nPREP_TUNING_MIN = 5.0      # M6, J-array, more than 5 spikes/s of preparatory tuning\nPERI_TUNING_RATIO = 1.5    # M6, peri-movement tuning at least 1.5 times the preparatory tuning\n\n\n# ---------------------------------------------------------------- archive access\n\ndef list_assets(version: str = VERSION) -> list[dict]:\n    \"\"\"Assets of the dandiset at a version, from the DANDI REST API.\"\"\"\n    out, url = [], f\"{API}/dandisets/{DANDISET_ID}/versions/{version}/assets/\"\n    while url:\n        r = requests.get(url, timeout=60).json()\n        out += r[\"results\"]\n        url = r.get(\"next\")\n    return out\n\n\ndef version_metadata(version: str = VERSION) -> dict:\n    return requests.get(f\"{API}/dandisets/{DANDISET_ID}/versions/{version}/\", timeout=60).json()\n\n\ndef asset_s3_url(path: str, version: str = VERSION) -> str:\n    \"\"\"The S3 address of an asset at the pinned version (the API's download redirect).\"\"\"\n    asset = next(a for a in list_assets(version) if a[\"path\"] == path)\n    r = requests.head(f\"{API}/assets/{asset['asset_id']}/download/\", allow_redirects=False, timeout=60)\n    return r.headers[\"Location\"].split(\"?\")[0]\n\n\ndef open_nwb(path: str, version: str = VERSION):\n    \"\"\"Stream an NWB file; returns (nwbfile, io). Keep io open while reading.\"\"\"\n    f = h5py.File(remfile.File(asset_s3_url(path, version)), \"r\")\n    io = pynwb.NWBHDF5IO(file=f, mode=\"r\", load_namespaces=True)\n    return io.read(), io\n\n\n# ---------------------------------------------------------------- loading\n\ndef load_session(nwb) -> dict:\n    \"\"\"Trials, units, spike times and hand kinematics of the train file.\n\n    Spike times are read as one flat array and split by the units' index. Hand position and\n    velocity are read whole (1 kHz, mm and mm/s as the series descriptions say).\n    \"\"\"\n    trials = nwb.trials.to_dataframe()\n    tp = np.array([np.asarray(p)[a] for p, a in zip(trials.target_pos, trials.active_target)])\n    trials[\"target_x\"], trials[\"target_y\"] = tp[:, 0], tp[:, 1]\n    trials[\"condition\"] = trials.groupby([\"trial_type\", \"trial_version\"]).ngroup()\n\n    u = nwb.units\n    flat = u.spike_times.data[:]\n    idx = u.spike_times_index.data[:]\n    starts = np.r_[0, idx[:-1]]\n    spikes = [np.asarray(flat[a:b]) for a, b in zip(starts, idx)]\n    el_idx = u.electrodes.data[:]\n    el = nwb.electrodes.to_dataframe()\n    units = pd.DataFrame({\n        \"unit_id\": u.id.data[:],\n        \"heldout\": u.heldout.data[:],\n        \"electrode_row\": el_idx,\n        \"electrode_group\": el[\"group_name\"].values[el_idx],\n        \"n_spikes\": [len(s) for s in spikes],\n    })\n    units[\"id_digit\"] = units.unit_id // 1000          # leading digit of the unit id\n    units[\"id_channel\"] = (units.unit_id // 10) % 100   # next two digits\n\n    beh = nwb.processing[\"behavior\"]\n    pos = beh[\"hand_pos\"].data[:]\n    vel = beh[\"hand_vel\"].data[:]\n    ts = beh[\"hand_pos\"].timestamps\n    n = ts.shape[0]\n    probe = np.unique(np.r_[np.linspace(0, n - 1, 2001).astype(int), n - 1])\n    ts_probe = ts[probe[0]:probe[-1] + 1][probe - probe[0]] if False else np.array([ts[i] for i in probe[::50]])\n    return dict(trials=trials, units=units, spikes=spikes, hand_pos=pos, hand_vel=vel,\n                ts_first=float(ts[0]), ts_n=n, ts_probe_idx=probe[::50], ts_probe=ts_probe)\n\n\ndef sample_index(times_s: np.ndarray, t0: float = 0.0, dt: float = 0.001) -> np.ndarray:\n    return np.round((np.asarray(times_s) - t0) / dt).astype(int)\n\n\ndef kinematic_windows(sess: dict, event: np.ndarray, before_ms: int, after_ms: int):\n    \"\"\"Hand position and velocity (trials x ms x 2) from event-before to event+after, 1 ms steps.\"\"\"\n    i0 = sample_index(event - before_ms / 1000, sess[\"ts_first\"])\n    off = np.arange(before_ms + after_ms + 1)\n    ii = i0[:, None] + off[None, :]\n    return sess[\"hand_pos\"][ii], sess[\"hand_vel\"][ii]\n\n\n# ---------------------------------------------------------------- trial selection (M1)\n\ndef proto_trial_keep(vel: np.ndarray, cond: np.ndarray, base: np.ndarray, reading: str) -> np.ndarray:\n    \"\"\"M1: keep trials whose velocity profile correlates with the condition's mean at r > 0.9.\n\n    vel: trials x time x 2 over PROTO_WIN; base: trials eligible (delay > 400 ms), which also form\n    the proto-trial (T1, T2: the condition's mean velocity over its trials). T1: each component at\n    r > 0.9; T2: the two components concatenated.\n    \"\"\"\n    keep = np.zeros(len(cond), bool)\n    for c in np.unique(cond):\n        m = np.where(base & (cond == c))[0]\n        proto = vel[m].mean(0)\n        for i in m:\n            if reading == \"T1\":\n                r = [np.corrcoef(vel[i, :, j], proto[:, j])[0, 1] for j in (0, 1)]\n                keep[i] = min(r) > PROTO_R\n            elif reading == \"T2\":\n                keep[i] = np.corrcoef(vel[i].T.ravel(), proto.T.ravel())[0, 1] > PROTO_R\n            else:\n                raise ValueError(reading)\n    return keep\n\n\n# ---------------------------------------------------------------- firing rates (M2)\n\ndef averaging_matrix(cond: np.ndarray, keep: np.ndarray, n_cond: int) -> np.ndarray:\n    A = np.zeros((n_cond, len(cond)))\n    for c in range(n_cond):\n        m = keep & (cond == c)\n        A[c, m] = 1.0 / m.sum()\n    return A\n\n\ndef condition_rates(spikes: list[np.ndarray], event: np.ndarray, before_ms: int, after_ms: int,\n                    avg: dict[str, np.ndarray], pad_ms: int = 100) -> tuple[np.ndarray, dict]:\n    \"\"\"Condition-mean smoothed rates (spikes/s), units x conditions x samples, for each averaging matrix.\n\n    Spikes are counted in 1 ms bins from event-before-pad to event+after+pad, smoothed with a\n    Gaussian of SD 20 ms (M2), sampled every 10 ms from -before to +after, and averaged over the\n    trials each matrix in `avg` selects. The pad keeps the edges free of the smoothing's boundary.\n    \"\"\"\n    times = np.arange(-before_ms, after_ms + 1, STEP_MS)\n    nb = before_ms + after_ms + 2 * pad_ms + 1\n    lo_t = event - (before_ms + pad_ms) / 1000\n    hi_t = event + (after_ms + pad_ms + 1) / 1000\n    samp = pad_ms + before_ms + times\n    out = {k: np.zeros((len(spikes), a.shape[0], len(times))) for k, a in avg.items()}\n    ntr = len(event)\n    for u, s in enumerate(spikes):\n        lo = np.searchsorted(s, lo_t)\n        hi = np.searchsorted(s, hi_t)\n        cnt = hi - lo\n        tot = cnt.sum()\n        counts = np.zeros((ntr, nb))\n        if tot:\n            idx = np.repeat(lo - np.r_[0, np.cumsum(cnt)[:-1]], cnt) + np.arange(tot)\n            tri = np.repeat(np.arange(ntr), cnt)\n            b = np.floor((s[idx] - lo_t[tri]) * 1000).astype(int)\n            ok = (b >= 0) & (b < nb)\n            np.add.at(counts, (tri[ok], b[ok]), 1.0)\n        sm = gaussian_filter1d(counts, SIGMA_MS, axis=1, mode=\"constant\")[:, samp] * 1000.0\n        for k, a in avg.items():\n            out[k][u] = a @ sm\n    return times, out\n\n\ndef window_mean(rates: np.ndarray, times: np.ndarray, win: tuple[int, int]) -> np.ndarray:\n    m = (times >= win[0]) & (times <= win[1])\n    return rates[..., m].mean(-1)\n\n\ndef tuning(x: np.ndarray, reading: str) -> np.ndarray:\n    \"\"\"M6 tuning of condition rates (units x conditions). S1 range, S2 SD over conditions.\"\"\"\n    if reading == \"S1\":\n        return x.max(1) - x.min(1)\n    if reading == \"S2\":\n        return x.std(1)\n    raise ValueError(reading)\n\n\n# ---------------------------------------------------------------- PD fits (M7)\n\ndef loo_performance(S: np.ndarray, Y: np.ndarray) -> np.ndarray:\n    \"\"\"M7: leave-one-condition-out performance of x = b0 + S b, for each column of Y (c x N).\n\n    Performance = 1 - mean squared LOO error / variance over conditions (denominator c). The LOO\n    residuals are the exact ones of least squares, e_i / (1 - h_ii).\n    \"\"\"\n    c = Y.shape[0]\n    X = np.column_stack([np.ones(c), S])\n    H = X @ np.linalg.pinv(X)\n    R = Y - H @ Y\n    loo = R / (1 - np.diag(H))[:, None]\n    return 1 - (loo ** 2).mean(0) / Y.var(0)\n\n\ndef pca_scores(T: np.ndarray, kmax: int) -> np.ndarray:\n    \"\"\"First kmax PCA scores of the rows of T (columns mean-centred).\"\"\"\n    Tc = T - T.mean(0)\n    U, s, _ = np.linalg.svd(Tc, full_matrices=False)\n    return U[:, :kmax] * s[:kmax]\n\n\ndef gram_leave_one_out_scores(blocks: np.ndarray, kmax: int):\n    \"\"\"For each neuron n, PCA scores (c x kmax) of the T-matrix of all other neurons (M5).\n\n    blocks: neurons x conditions x times. Uses the Gram matrix of the centred T-matrix, from which\n    each neuron's own block is subtracted. Yields (n, scores).\n    \"\"\"\n    B = blocks - blocks.mean(1, keepdims=True)\n    G = np.einsum(\"nct,ndt->cd\", B, B)\n    for n in range(B.shape[0]):\n        Gn = G - B[n] @ B[n].T\n        w, V = np.linalg.eigh(Gn)\n        order = np.argsort(w)[::-1][:kmax]\n        yield n, V[:, order] * np.sqrt(np.clip(w[order], 0, None))\n\n\ndef peri_space_performance(blocks: np.ndarray, X: np.ndarray, kmax: int) -> np.ndarray:\n    \"\"\"Performance (neurons x k=1..kmax) of each neuron's preparatory rates X (c x neurons) in the\n    peri-movement space built from the other neurons' blocks.\"\"\"\n    out = np.zeros((blocks.shape[0], kmax))\n    for n, S in gram_leave_one_out_scores(blocks, kmax):\n        for k in range(1, kmax + 1):\n            out[n, k - 1] = loo_performance(S[:, :k], X[:, [n]])[0]\n    return out\n\n\ndef space_performance_all_k(S_full: np.ndarray, X: np.ndarray, kmax: int) -> np.ndarray:\n    \"\"\"Performance (neurons x k) in one PCA space shared by all neurons.\"\"\"\n    return np.column_stack([loo_performance(S_full[:, :k], X) for k in range(1, kmax + 1)])\n\n\n# ---------------------------------------------------------------- kinematic and task spaces\n\ndef unit_range(a: np.ndarray) -> np.ndarray:\n    return a / (a.max() - a.min())\n\n\ndef kinematic_tmatrix(pos: np.ndarray, vel: np.ndarray, acc: np.ndarray, n_blocks: int | None):\n    \"\"\"Kinematic T-matrix (Methods, PCA-based spaces): horizontal and vertical position, velocity\n    and acceleration of the condition means (conditions x times), each scaled to unit range over\n    times and conditions. n_blocks None: the six variables once each (D1); otherwise the six in\n    turn until there are n_blocks column blocks (D2).\"\"\"\n    vars6 = [unit_range(v) for v in (pos[..., 0], pos[..., 1], vel[..., 0], vel[..., 1],\n                                     acc[..., 0], acc[..., 1])]\n    if n_blocks is None:\n        return np.concatenate(vars6, axis=1)\n    return np.concatenate([vars6[i % 6] for i in range(n_blocks)], axis=1)\n\n\ndef end_of_reach(speed: np.ndarray, start: int) -> int:\n    \"\"\"M9: when speed first falls below 5% of its peak after the peak (claims file standard choice);\n    the last sample if it never does.\"\"\"\n    pk = start + int(np.argmax(speed[start:]))\n    below = np.where(speed[pk:] < 0.05 * speed[pk])[0]\n    return pk + int(below[0]) if len(below) else len(speed) - 1\n\n\ndef _resample_path(xy: np.ndarray, fractions: np.ndarray) -> np.ndarray:\n    seg = np.r_[0, np.cumsum(np.linalg.norm(np.diff(xy, axis=0), axis=1))]\n    s = fractions * seg[-1]\n    return np.column_stack([np.interp(s, seg, xy[:, 0]), np.interp(s, seg, xy[:, 1])])\n\n\ndef task_features(pos: np.ndarray, vel: np.ndarray, onset_idx: int) -> dict:\n    \"\"\"M9 task-space features of one condition-mean trajectory (1 ms samples; onset at onset_idx).\"\"\"\n    speed = np.linalg.norm(vel, axis=1)\n    end = end_of_reach(speed, onset_idx)\n    p, v = pos[onset_idx:end + 1], vel[onset_idx:end + 1]\n    sp = speed[onset_idx:end + 1]\n    start, endp = p[0], p[-1]\n    d = endp - start\n    dn = d / np.linalg.norm(d)\n    rel = p - start\n    perp = dn[0] * rel[:, 1] - dn[1] * rel[:, 0]          # positive to the left: counterclockwise\n    i_abs = int(np.argmax(np.abs(perp)))\n    i_ccw = int(np.argmax(perp))\n    ipk = int(np.argmax(sp))\n    ix, iy = int(np.argmax(np.abs(v[:, 0]))), int(np.argmax(np.abs(v[:, 1])))\n    n = len(p)\n    thirds_t = p[[0, n // 3, (2 * n) // 3, n - 1]]\n    thirds_l = _resample_path(p, np.array([0, 1 / 3, 2 / 3, 1]))\n    return dict(\n        end_ms=end - onset_idx,\n        endpoint=endp,\n        max_speed=sp.max(),\n        init_vel=vel[onset_idx:onset_idx + 150].mean(0),\n        orth_excursion=perp[i_abs],\n        viapoint=p[i_abs],\n        maxvel_V1a=np.array([np.abs(v[:, 0]).max(), np.abs(v[:, 1]).max()]),\n        maxvel_V1b=np.array([v[ix, 0], v[iy, 1]]),\n        maxvel_V2=v[ipk],\n        halfpoint=_resample_path(p, np.array([0.5]))[0],\n        segdirs_G1=np.diff(thirds_l, axis=0).ravel(),\n        segdirs_G2=np.diff(thirds_t, axis=0).ravel(),\n        ccw_excursion=perp[i_ccw],\n        ccw_point=p[i_ccw],\n    )\n\n\ndef task_spaces(feats: list[dict], barriers: np.ndarray, distractors: np.ndarray) -> dict:\n    \"\"\"M9 task spaces (conditions x dims), with the readings V1 (a: magnitudes, b: signed value at\n    the maximum magnitude), V2, G1 and G2 as separate entries.\"\"\"\n    F = lambda k: np.array([f[k] for f in feats])\n    ep = F(\"endpoint\")\n    sp = {\n        \"endpoints + max speed\": np.column_stack([ep, F(\"max_speed\")]),\n        \"initial velocity\": F(\"init_vel\"),\n        \"endpoints + orthogonal excursion\": np.column_stack([ep, F(\"orth_excursion\")]),\n        \"endpoints + viapoint\": np.column_stack([ep, F(\"viapoint\")]),\n        \"endpoints + max velocity (V1a)\": np.column_stack([ep, F(\"maxvel_V1a\")]),\n        \"endpoints + max velocity (V1b)\": np.column_stack([ep, F(\"maxvel_V1b\")]),\n        \"endpoints + max velocity (V2)\": np.column_stack([ep, F(\"maxvel_V2\")]),\n        \"endpoints + halfpoint\": np.column_stack([ep, F(\"halfpoint\")]),\n        \"segment directions (G1)\": F(\"segdirs_G1\"),\n        \"segment directions (G2)\": F(\"segdirs_G2\"),\n    }\n    for g in (\"G1\", \"G2\"):\n        sp[f\"kitchen sink ({g})\"] = np.column_stack([F(f\"segdirs_{g}\"), F(\"ccw_excursion\"),\n                                                     F(\"ccw_point\"), barriers, distractors])\n    return sp\n\n\n# ---------------------------------------------------------------- tests\n\ndef mean_tests(r: np.ndarray) -> dict:\n    \"\"\"P1 to P3 of fig4d: tests of the mean correlation against zero, two-sided.\"\"\"\n    from scipy import stats\n    return {\n        \"P1 t-test on r\": stats.ttest_1samp(r, 0).pvalue,\n        \"P2 t-test on Fisher z\": stats.ttest_1samp(np.arctanh(np.clip(r, -0.999999, 0.999999)), 0).pvalue,\n        \"P3 Wilcoxon\": stats.wilcoxon(r).pvalue,\n    }\n\n\ndef corr_rows(a: np.ndarray, b: np.ndarray) -> np.ndarray:\n    \"\"\"Pearson correlation of matching rows of a and b.\"\"\"\n    a = a - a.mean(1, keepdims=True)\n    b = b - b.mean(1, keepdims=True)\n    return (a * b).sum(1) / np.sqrt((a * a).sum(1) * (b * b).sum(1))\n\n\ndef spearman_rows(a: np.ndarray, b: np.ndarray) -> np.ndarray:\n    from scipy.stats import rankdata\n    return corr_rows(rankdata(a, axis=1), rankdata(b, axis=1))\n\n\n# ---------------------------------------------------------------- the Figure 8 model\n\ndef oscillator(x0: np.ndarray, n_steps: int, exact: bool = False) -> np.ndarray:\n    \"\"\"x(t+1) = W x(t) from the Figure 8 legend (exact=True: the pure one-degree rotation).\n    x0: conditions x 2. Returns conditions x 2 x n_steps (the states after 1..n_steps steps).\"\"\"\n    a = 2 * np.pi / 360\n    W = np.array([[np.cos(a), -np.sin(a)], [np.sin(a), np.cos(a)]]) if exact else \\\n        np.array([[1, -a], [a, 1]])\n    out = np.zeros((x0.shape[0], 2, n_steps))\n    x = x0.copy()\n    for t in range(n_steps):\n        x = x @ W.T\n        out[:, :, t] = x\n    return out\n"
}
```

```
File created successfully at: entries/000128-churchland-2010/mcmaze.py (file state is current in your context — no need to Read it back)
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "entries/000128-churchland-2010/mcmaze.py",
 "old_string": "    ts = beh[\"hand_pos\"].timestamps\n    n = ts.shape[0]\n    probe = np.unique(np.r_[np.linspace(0, n - 1, 2001).astype(int), n - 1])\n    ts_probe = ts[probe[0]:probe[-1] + 1][probe - probe[0]] if False else np.array([ts[i] for i in probe[::50]])\n    return dict(trials=trials, units=units, spikes=spikes, hand_pos=pos, hand_vel=vel,\n                ts_first=float(ts[0]), ts_n=n, ts_probe_idx=probe[::50], ts_probe=ts_probe)",
 "new_string": "    ts = beh[\"hand_pos\"].timestamps\n    n = ts.shape[0]\n    # timestamps are checked for a regular 1 ms grid on 21 blocks of 1000 samples spread over the series\n    starts_probe = np.linspace(0, n - 1000, 21).astype(int)\n    idx_probe = np.concatenate([np.arange(a, a + 1000) for a in starts_probe])\n    ts_probe = np.concatenate([ts[a:a + 1000] for a in starts_probe])\n    same_ts = all(np.array_equal(beh[k].timestamps[:1000], ts[:1000]) for k in (\"hand_vel\",))\n    return dict(trials=trials, units=units, spikes=spikes, hand_pos=pos, hand_vel=vel,\n                ts_first=float(ts[0]), ts_n=n, ts_probe_idx=idx_probe, ts_probe=ts_probe,\n                vel_shares_pos_timestamps=same_ts)"
}
```

```
The file entries/000128-churchland-2010/mcmaze.py has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > dev1.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/000128-churchland-2010')
import numpy as np, mcmaze as mm
t=time.time()
nwb, io = mm.open_nwb(mm.TRAIN_PATH)
sess = mm.load_session(nwb)
print("load", time.time()-t)
print(sess['ts_first'], sess['ts_n'], np.abs(sess['ts_probe'] - sess['ts_probe_idx']*0.001).max(), sess['vel_shares_pos_timestamps'])
pickle.dump(sess, open('sess.pkl','wb'))
EOF
python dev1.py
```

```
load 6.5527448654174805
0.0 6809920 142.3810000000003 True
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import sys, time; sys.path.insert(0,'entries/000128-churchland-2010')
import numpy as np, mcmaze as mm
nwb, io = mm.open_nwb(mm.TRAIN_PATH)
t=time.time(); ts=nwb.processing['behavior']['hand_pos'].timestamps[:]; print(time.time()-t)
d=np.diff(ts); print(np.unique(np.round(d,4),return_counts=True))
tr=nwb.trials.to_dataframe()
# are gaps between trials?
gi=np.where(d>0.0015)[0]; print(len(gi), ts[gi][:5], ts[gi+1][:5]); print(tr.stop_time.values[:5], tr.start_time.values[1:6])
# coverage of trials
lo=np.searchsorted(ts, tr.start_time.values); hi=np.searchsorted(ts,tr.stop_time.values)
print(((ts[hi]-tr.stop_time.values)).max(), (ts[lo]-tr.start_time.values).max())
EOF
```

```
Exit code 1
0.6690201759338379
(array([0.001, 0.015, 0.02 , 0.025, 0.03 , 0.035, 0.04 , 0.045, 0.05 ,
       0.055, 0.06 , 0.065, 0.07 , 0.075, 0.08 , 0.085, 0.09 , 0.095,
       0.1  , 0.105, 0.11 ]), array([6807625,     113,     102,     113,     110,     109,     116,
           135,     117,     116,     107,     118,     112,     111,
           107,     104,     131,     110,     117,     120,     126]))
2294 [ 3.32   6.52   9.855 12.945 15.48 ] [ 3.4  6.6  9.9 13.  15.5]
[ 3.321  6.521  9.856 12.946 15.481] [ 3.4  6.6  9.9 13.  15.5]
Traceback (most recent call last):
  File "<stdin>", line 11, in <module>
IndexError: index 6809920 is out of bounds for axis 0 with size 6809920
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010 && python - <<'EOF'
s=open('mcmaze.py').read()
old=s[s.index('    ts = beh["hand_pos"].timestamps\n'):s.index('def sample_index')]
new='''    ts = beh["hand_pos"].timestamps[:]
    same_ts = np.array_equal(beh["hand_vel"].timestamps[:], ts)
    return dict(trials=trials, units=units, spikes=spikes, hand_pos=pos, hand_vel=vel,
                hand_t=ts, vel_shares_pos_timestamps=same_ts)


'''
s=s.replace(old,new)
old=s[s.index('def sample_index'):s.index('# ---------------------------------------------------------------- trial selection')]
new='''def kinematic_windows(sess: dict, event: np.ndarray, before_ms: int, after_ms: int):
    """Hand position and velocity (trials x ms x 2) from event-before to event+after, 1 ms steps.

    The behaviour series have timestamps on a 1 ms grid within trials and gaps between trials;
    the sample nearest each window start is found by its timestamp, and the largest difference
    between the timestamps used and the intended times is returned as a check (seconds).
    """
    t = sess["hand_t"]
    start = event - before_ms / 1000
    i0 = np.clip(np.searchsorted(t, start - 0.0005), 0, len(t) - 1)
    off = np.arange(before_ms + after_ms + 1)
    ii = np.clip(i0[:, None] + off[None, :], 0, len(t) - 1)
    err = np.abs(t[ii] - (start[:, None] + off[None, :] / 1000)).max()
    return sess["hand_pos"][ii], sess["hand_vel"][ii], err


'''
s=s.replace(old,new)
open('mcmaze.py','w').write(s)
EOF
grep -n "sample_index\|ts_first" mcmaze.py
```

```
(Bash completed with no output)
```

**Agent**

Now a development script computing the core quantities, to see results and timings.

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > dev2.py <<'EOF'
import sys, time, pickle; sys.path.insert(0,'entries/000128-churchland-2010')
import numpy as np, mcmaze as mm
T0=time.time()
nwb, io = mm.open_nwb(mm.TRAIN_PATH)
sess = mm.load_session(nwb); print("load", time.time()-T0)
tr=sess['trials']; cond=tr.condition.values; C=cond.max()+1
move=tr.move_onset_time.values; go=tr.go_cue_time.values
base=(tr.delay.values>400)
pos,vel,err=mm.kinematic_windows(sess, move, 150, 900); print("kin err",err, pos.shape)
pw=slice(0, 951)
keep={'T1':mm.proto_trial_keep(vel[:,pw],cond,base,'T1')&base,'T2':mm.proto_trial_keep(vel[:,pw],cond,base,'T2')&base}
for k,v in keep.items(): print(k, v.sum(), v.sum()/base.sum(), np.bincount(cond[v],minlength=C).min())
avg={k:mm.averaging_matrix(cond,v,C) for k,v in keep.items()}
t=time.time()
tg,go_r=mm.condition_rates(sess['spikes'],go,400,500,avg); print("go rates",time.time()-t)
t=time.time()
tm,mv_r=mm.condition_rates(sess['spikes'],move,400,800,avg); print("move rates",time.time()-t)
pickle.dump(dict(sess=sess,keep=keep,tg=tg,go_r=go_r,tm=tm,mv_r=mv_r,pos=pos,vel=vel),open('dev.pkl','wb'))
for k in keep:
    X=mm.window_mean(go_r[k],tg,mm.PREP_WIN); P=mm.window_mean(mv_r[k],tm,mm.PERI_WIN)
    for s in ('S1','S2'):
        pt=mm.tuning(X,s); qt=mm.tuning(P,s)
        sel=(pt>5)&(qt>=1.5*pt)
        r=mm.corr_rows(X[sel],P[sel]); rs=mm.spearman_rows(X[sel],P[sel])
        print(k,s,"prep-tuned",(pt>5).sum(),"sel",sel.sum(),"mean r %.3f sp %.3f"%(r.mean(),rs.mean()), mm.mean_tests(r))
EOF
python dev2.py
```

```
entries/000128-churchland-2010/mcmaze.py:155: RuntimeWarning: divide by zero encountered in divide
  A[c, m] = 1.0 / m.sum()
/tmp/claude-1001/dev2.py:25: RuntimeWarning: Mean of empty slice
  print(k,s,"prep-tuned",(pt>5).sum(),"sel",sel.sum(),"mean r %.3f sp %.3f"%(r.mean(),rs.mean()), mm.mean_tests(r))
/tmp/claude-1001/env/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
entries/000128-churchland-2010/mcmaze.py:356: SmallSampleWarning: One or more sample arguments is too small; all returned values will be NaN. See documentation for sample size requirements.
  "P1 t-test on r": stats.ttest_1samp(r, 0).pvalue,
entries/000128-churchland-2010/mcmaze.py:357: SmallSampleWarning: One or more sample arguments is too small; all returned values will be NaN. See documentation for sample size requirements.
  "P2 t-test on Fisher z": stats.ttest_1samp(np.arctanh(np.clip(r, -0.999999, 0.999999)), 0).pvalue,
/tmp/claude-1001/env/lib/python3.13/site-packages/scipy/_lib/_util.py:882: SmallSampleWarning: One or more sample arguments is too small; all returned values will be NaN. See documentation for sample size requirements.
  return fun(*args, **kwargs)
load 6.310159683227539
kin err 9.094947017729282e-13 (2295, 1051, 2)
T1 1452 0.7381799694966955 0
T2 1786 0.9079816980172852 10
go rates 31.85315203666687
move rates 39.04197907447815
T1 S1 prep-tuned 97 sel 24 mean r 0.117 sp 0.102 {'P1 t-test on r': np.float64(0.011632051777826122), 'P2 t-test on Fisher z': np.float64(0.011528894623033355), 'P3 Wilcoxon': np.float64(0.015044927597045898)}
T1 S2 prep-tuned 6 sel 0 mean r nan sp nan {'P1 t-test on r': np.float64(nan), 'P2 t-test on Fisher z': np.float64(nan), 'P3 Wilcoxon': np.float64(nan)}
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import pickle, numpy as np, sys; sys.path.insert(0,'entries/000128-churchland-2010')
d=pickle.load(open('dev.pkl','rb')); tr=d['sess']['trials']; cond=tr.condition.values
for k,v in d['keep'].items():
    bc=np.bincount(cond[v],minlength=108); print(k, (bc==0).sum(), np.sort(bc)[:8], np.isnan(d['go_r'][k]).any(axis=(0,2)).sum())
base=tr.delay.values>400; print(np.bincount(cond[base],minlength=108).min())
c0=np.where(np.bincount(cond[d['keep']['T1']],minlength=108)==0)[0]; print(c0, tr[tr.condition.isin(c0)][['trial_type','trial_version','target_x','target_y']].drop_duplicates())
EOF
```

```
T1 2 [0 0 1 2 4 5 5 5] 0
T2 0 [10 10 11 11 12 12 12 12] 0
14
[51 78]      trial_type  trial_version  target_x  target_y
id                                                
65           30              0      -109         2
221          20              0      -130       -13
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010 && python - <<'EOF'
s=open('mcmaze.py').read()
old='''    A = np.zeros((n_cond, len(cond)))
    for c in range(n_cond):
        m = keep & (cond == c)
        A[c, m] = 1.0 / m.sum()
    return A'''
new='''    """Rows average the kept trials of each condition; a condition with no kept trial gets a row of NaN."""
    A = np.zeros((n_cond, len(cond)))
    for c in range(n_cond):
        m = keep & (cond == c)
        if m.any():
            A[c, m] = 1.0 / m.sum()
        else:
            A[c] = np.nan
    return A'''
assert old in s; s=s.replace(old,new); open('mcmaze.py','w').write(s)
EOF
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > dev3.py <<'EOF'
import pickle, numpy as np, sys, time; sys.path.insert(0,'entries/000128-churchland-2010')
import mcmaze as mm
d=pickle.load(open('dev.pkl','rb')); sess=d['sess']; tr=sess['trials']; cond=tr.condition.values; C=108
tg,tm=d['tg'],d['tm']; pos,vel=d['pos'],d['vel']
KMAX=14
res={}
for T in ('T1','T2'):
    keep=d['keep'][T]; has=np.bincount(cond[keep],minlength=C)>0
    G=d['go_r'][T][:,has]; M=d['mv_r'][T][:,has]
    X=mm.window_mean(G,tg,mm.PREP_WIN)   # units x c
    blocks=M[:,:,(tm>=-150)&(tm<=800)]
    t=time.time(); peri=mm.peri_space_performance(blocks, X.T, KMAX); print("peri",time.time()-t)
    blocks0=M[:,:,(tm>=0)&(tm<=800)]
    peri0=mm.peri_space_performance(blocks0, X.T, KMAX)
    # kinematics condition means
    A=mm.averaging_matrix(cond,keep,C)[has]
    P=np.einsum('ct,tsj->csj',A,pos); V=np.einsum('ct,tsj->csj',A,vel)
    Acc=np.gradient(V,axis=1)*1000
    kin={}
    for W,end in (('W1',800),('W2',600)):
        sl=np.arange(0,150+end+1,10)
        for D,nb in (('D1',None),('D2',blocks.shape[0]-1)):
            Tk=mm.kinematic_tmatrix(P[:,sl],V[:,sl],Acc[:,sl],nb)
            kin[W+D]=mm.space_performance_all_k(mm.pca_scores(Tk,KMAX),X.T,KMAX)
    trc=tr[keep].groupby('condition').first().loc[np.where(has)[0]]
    feats=[mm.task_features(P[c],V[c],150) for c in range(P.shape[0])]
    ts_=mm.task_spaces(feats,(trc.num_barriers>0).astype(float).values,(trc.num_targets>1).astype(float).values)
    task={k:mm.loo_performance(S,X.T) for k,S in ts_.items()}
    print(T,"end of reach ms", np.percentile([f['end_ms'] for f in feats],[0,50,100]))
    res[T]=dict(X=X,peri=peri,peri0=peri0,kin=kin,task=task,dims={k:S.shape[1] for k,S in ts_.items()},has=has)
    for S in ('S1',):
        sel=mm.tuning(X,S)>5
        print(T,S,sel.sum(),"peri",np.round(peri[sel].mean(0),3))
        print(" peri0",np.round(peri0[sel].mean(0),3))
        for k,v in kin.items(): print(" kin",k,np.round(v[sel].mean(0),3))
        for k,v in task.items(): print(" task",k,res[T]['dims'][k],round(v[sel].mean(),3))
pickle.dump(res,open('res.pkl','wb'))
EOF
python dev3.py
```

```
peri 0.8529782295227051
T1 end of reach ms [208.  426.5 669. ]
T1 S1 96 peri [ 0.104  0.173  0.207  0.265  0.281  0.268  0.104  0.148  0.143 -0.145
 -0.075 -0.098 -0.19  -0.287]
 peri0 [ 0.086  0.155  0.191  0.245  0.258  0.233  0.19   0.009 -0.172 -0.086
 -0.034 -0.047 -0.294 -0.283]
 kin W1D1 [0.101 0.157 0.195 0.248 0.254 0.274 0.289 0.288 0.286 0.289 0.293 0.294
 0.28  0.272]
 kin W1D2 [0.102 0.157 0.195 0.248 0.254 0.274 0.289 0.288 0.286 0.289 0.293 0.295
 0.28  0.272]
 kin W2D1 [0.1   0.166 0.201 0.251 0.256 0.276 0.29  0.289 0.286 0.29  0.29  0.295
 0.281 0.274]
 kin W2D2 [0.101 0.166 0.201 0.251 0.256 0.276 0.29  0.289 0.286 0.29  0.29  0.295
 0.281 0.274]
 task endpoints + max speed 3 0.131
 task initial velocity 2 0.184
 task endpoints + orthogonal excursion 3 0.153
 task endpoints + viapoint 4 0.195
 task endpoints + max velocity (V1a) 4 0.175
 task endpoints + max velocity (V1b) 4 0.174
[... 33 more lines not kept]
```

**Agent calls Skill**

```json
{
 "skill": "dataviz"
}
```

```
Launching skill: dataviz
```

## Prompt

Base directory for this skill: /tmp/claude-1001/bundled-skills/2.1.284/dade65989b676059664831d936f19124/dataviz

# Data Visualization

A chart is **read by people and executed by you**. This skill turns "make it look
good" into a procedure with checks, so the result is right by construction rather
than by taste.

**The method here is design-system-agnostic.** Nothing in the procedure, the form
heuristic, the six checks, or the mark specs is specific to one product. A design
system supplies a small set of *parameters* (its ramps, a categorical order, a
diverging pair, a status palette, a texture, its surfaces, its filter components);
the method consumes them unchanged. A **validated default palette** is the
reference instance, fully specified in `references/palette.md`. To target your
brand, read that file's structure and substitute its values - touch nothing else.

> The single most important habit: **the color part is computable, so compute it.**
> Never eyeball whether a palette is colorblind-safe - run `scripts/validate_palette.js`.

## The procedure - do these in order

Color comes LAST. Most bad charts pick colors first.

1. **Pick the form.** What is the data's job - magnitude, identity, polarity, a
   single headline, change-over-time? The job picks the chart type, and sometimes
   the answer is *not a chart* (a stat tile or hero number). -> `references/choosing-a-form.md`
2. **Assign color by the job it does.** Categorical (identity), sequential
   (magnitude), diverging (polarity), or status (state) - each has one rule.
   Assign categorical hues in fixed order, never cycled. -> `references/color-formula.md`
3. **VALIDATE the palette - run the script, don't reason about Delta E.**
   `node scripts/validate_palette.js "<hex,hex,...>" --mode light` (relative to
   this skill's base directory - or load it as `<script type="module">` in the
   chart's own page, where it reads
   `data-palette` off `<body>` and logs a `console.table` report). It returns
   pass/fail on the lightness band, chroma floor, adjacent-pair CVD separation,
   the normal-vision floor, and contrast. Fix anything that FAILs before continuing. Re-run for
   `--mode dark` with that mode's surface.
4. **Apply mark specs & spacers.** Thin marks, 4px rounded data-ends anchored to
   the baseline, 2px lines, >=8px markers, a 2px surface gap between fills (stacked
   segments and adjacent bars alike) and a 2px surface ring on overlapping marks,
   selective direct labels. -> `references/marks-and-anatomy.md`
5. **Add the hover layer - by default.** An HTML/SVG chart *is* interactive; ship
   a crosshair+tooltip on line/area and a per-mark hover tooltip on bar/dot/cell.
   The only form that skips it is a bare stat tile with no plot. Hit targets bigger
   than the mark; filters in one row above the charts. -> `references/interaction.md`
6. **Final accessibility pass.** For >= 2 series a legend is always present and <= 4
   are also direct-labeled (a single series needs no legend box - the title names
   it), so identity is never color-alone; a table view exists; dark mode is **selected** - its own
   steps from the same ramps, validated against the dark surface, not an automatic
   flip; texture is available for the CVD/print/forced-colors case.
7. **Render it and look at it.** The validator checks color, not layout - open or
   screenshot the output and eyeball it for label collisions, geometry, and overflow
   before calling it done.

Then check the result against **`references/anti-patterns.md`** - it is the catalog
of what goes wrong. If your chart matches an entry, it's wrong.

## Non-negotiables (true in every design system)

- **Assign categorical hues in fixed order, never cycled.** A 9th series is never a
  generated hue - it folds into "Other," small multiples, or composite encoding.
- **One axis.** Never a dual-axis chart (two y-scales). Two measures of different
  scale -> two charts, small multiples, or indexed to a common base. *(This is the
  #1 chart mistake - see anti-patterns.)*
- **Color follows the entity, never its rank.** A filter that changes the series
  count must not repaint the survivors.
- **Sequential = one hue, light->dark. Diverging = two hues + a neutral gray
  midpoint.** Never a rainbow; never a hue at the diverging midpoint.
- **Run the validator before shipping any categorical palette.** CVD Delta E >= 8 is the
  target (OKLab ×100); 6-8 is a floor that is legal ONLY with secondary encoding. A
  normal-vision floor below 15 is a hard FAIL - full-color readers can't tell the
  pair apart; re-step it on the adjacent pairlist (secondary encoding does not excuse
  this one); under `--pairs all` cut series or facet instead - see check 4. A contrast WARN
  obligates visible labels or a table view - it is not dismissable.
- **Thin marks; a legend always present for >= 2 series (none for one), with
  selective direct labels (never a number on every point); recessive grid/axes.**
- **Text wears text tokens, never the series color** - values, labels, and legends
  stay in primary/secondary/muted ink; a colored mark beside them carries identity.
- **Status colors are reserved** (good/warning/serious/critical) and never reused
  for "series 4"; they ship with an icon + label, never color alone.

## Plugging in a design system

The method is invariant; only these parameters change per system. The reference
instance - every value filled in - is `references/palette.md`.

| Parameter | What the system provides |
|---|---|
| **Ramps** | the hue scales (named steps) the palette draws from |
| **Categorical theme** | the fixed hue order (a named theme); default + alternates |
| **Sequential hue** | the default single hue for magnitude |
| **Diverging pair** | two warm/cool poles + a neutral midpoint |
| **Status palette** | good / warning / serious / critical - steps distinct from categorical |
| **Texture fill** | one directional hand-drawn fill, used at 45° / 135° |
| **Surfaces** | light & dark chart-surface colors (the validator needs these) |
| **Filter controls** | date-range & dimension controls (behavioral spec in `interaction.md`) |

To onboard a new system: fill those rows, feed its ramps to the validator, and let
it snap each slot to the nearest passing step. Structure and rules stay as written.

## Reference files

| File | What it answers |
|------|-----------------|
| `references/choosing-a-form.md` | Which chart type / is it even a chart? |
| `references/color-formula.md` | The four jobs, the six checks, snap-to-passing |
| `references/marks-and-anatomy.md` | Mark specs, spacers, labels, figures, hero number |
| `references/interaction.md` | Tooltips & hover, filters & time ranges |
| `references/components.md` | The pieces a chart is made of - build each in plain HTML |
| `references/anti-patterns.md` | **What goes wrong - check every chart against this** |
| `references/palette.md` | **The reference palette instance** - every parameter, filled in; swap for your brand's |
| `scripts/validate_palette.js` | Runnable six-checks validator (run it; don't eyeball) |

**Agent**

Now the notebook builder.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "import nbformat as nbf\n\ncells = []\ndef md(s, tags=None):\n    c = nbf.v4.new_markdown_cell(s.strip(\"\\n\"))\n    if tags: c.metadata[\"tags\"] = tags\n    cells.append(c)\ndef code(s, tags=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tags: c.metadata[\"tags\"] = tags\n    cells.append(c)\n\nmd(r\"\"\"\n# Reproducing Churchland et al. (2010) from dandiset 000128\n\n**Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory\nactivity: representation of movement or first cog in a dynamical machine? *Neuron* 68:387-400,\ndoi:10.1016/j.neuron.2010.09.015.\n\n**Dataset.** DANDI:000128 (MC_Maze, Neural Latents Benchmark), version `0.220113.0400`,\ndoi:10.48324/dandi.000128/0.220113.0400. The paper cites no version of the dataset (it predates it).\nThis is the only published version, so it is pinned. The draft (modified 2023-06-20) holds the same two\nassets with the same blobs (checked below), so the choice changes nothing the analysis uses.\n\n**Claims file.** `claims/000128/10.1016-j.neuron.2010.09.015.yaml`, written from the accepted author\nmanuscript in PubMed Central (PMC2991102) with its supplement, and checked by a second reader. The\nclaims file fixes every method; the labels M1 to M9, T1/T2, S1/S2 and so on are its readings.\n\nThe dataset holds one session of monkey Jenkins on the maze task, recorded with two 96-electrode\narrays: the paper's J-array dataset. It holds none of the speed-task data (monkeys A and B), none of the\nsingle-electrode maze recordings (monkey J) and no EMG.\n\n| Claim | Status here |\n|---|---|\n| recordings-jarray | tested |\n| recordings-single-electrode | blocked: data_missing |\n| fig2b-example-concordant-tuning | blocked: data_missing (speed task) |\n| fig2ce-example-opposing-tuning | blocked: data_missing (speed task) |\n| fig3-maze-most-not-maintained | tested |\n| fig4d-mean-correlation-jarray | tested |\n| fig4abc-mean-correlation-single-electrode | blocked: data_missing |\n| fig4-no-separate-populations | tested (J-array only) |\n| fig4e-correlation-time-course | tested |\n| suppfig1-population-averages | tested |\n| fig6-peri-movement-space-best | tested (J-array) |\n| fig6-each-dimensionality | tested (J-array) |\n| fig6-performance-vs-dimensionality | tested (J-array) |\n| prep-dimensionality | tested (J-array) |\n| fig6e-summary-across-datasets | blocked: data_missing (A, B, J and EMG) |\n| fig7a-shuffled-space-poor | tested (J-array) |\n| fig7b-window-start-slide | tested (J-array ratio, reading J2) |\n| ap-location-no-effect-on-correlation | blocked: metadata_insufficient (no AP location; array labels wrong); a variant is shown |\n| fig7c-anterior-posterior-performance | blocked: metadata_insufficient (as above) |\n| fig7d-pd-consistency | tested (J-array) |\n| fig8-model-weak-correlation | tested (simulation) |\n| fig8-model-pd-perfect | tested (simulation) |\n\"\"\")\n\ncode(r\"\"\"\nimport os\nos.environ.setdefault(\"OMP_NUM_THREADS\", \"1\")\nos.environ.setdefault(\"OPENBLAS_NUM_THREADS\", \"1\")\nimport time\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy import stats\nimport diptest\nfrom sklearn.discriminant_analysis import LinearDiscriminantAnalysis\nfrom sklearn.model_selection import StratifiedKFold, cross_val_score\nimport mcmaze as mm\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 30)\nT_START = time.time()\nprint(\"dandiset\", mm.DANDISET_ID, \"version\", mm.VERSION)\n\"\"\")\n\nmd(\"## Data check\")\n\ncode(r\"\"\"\nmeta = mm.version_metadata()\npub = {a[\"path\"]: (a[\"blob\"], a[\"size\"]) for a in mm.list_assets(mm.VERSION)}\ndraft = {a[\"path\"]: (a[\"blob\"], a[\"size\"]) for a in mm.list_assets(\"draft\")}\nprint(\"title:\", meta[\"name\"])\nprint(\"related publications in metadata:\", [r.get(\"identifier\") for r in meta.get(\"relatedResource\", [])])\nfor p, (b, s) in pub.items():\n    print(f\"  {p}: {s/1e6:.1f} MB, blob {b}\")\nprint(\"draft holds the same assets with the same blobs:\", pub == draft)\n\nnwb, io = mm.open_nwb(mm.TRAIN_PATH)\nsess = mm.load_session(nwb)\nnwb_test, io_test = mm.open_nwb(mm.TEST_PATH)\ntr = sess[\"trials\"]\nunits = sess[\"units\"]\nprint(\"subject:\", nwb.subject.subject_id, nwb.subject.species, \"| session:\", nwb.session_start_time.date(),\n      \"| related publication in file:\", list(nwb.related_publications))\nprint(\"train file trials columns:\", list(tr.columns))\nprint(\"units columns:\", nwb.units.colnames)\nprint(\"electrodes columns:\", list(nwb.electrodes.colnames))\nprint(\"behaviour:\", list(nwb.processing[\"behavior\"].data_interfaces))\n\"\"\")\n\ncode(r\"\"\"\n# what was loaded: counts and ranges of every variable used\nprint(\"=== trials (train file) ===\")\nprint(\"trials:\", len(tr), \"| split:\", tr.split.value_counts().to_dict(), \"| success all True:\", bool(tr.success.all()))\nprint(\"trial_type values:\", tr.trial_type.nunique(), \"| maze_id values:\", tr.maze_id.nunique(),\n      \"| trial_type <-> maze_id one to one:\", tr.groupby(\"trial_type\").maze_id.nunique().max() == 1\n      and tr.groupby(\"maze_id\").trial_type.nunique().max() == 1)\nprint(\"conditions (trial_type x trial_version):\", tr.condition.nunique())\nprint(\"trials per condition: min\", tr.condition.value_counts().min(), \"median\", tr.condition.value_counts().median(),\n      \"max\", tr.condition.value_counts().max())\nprint(pd.crosstab(tr.trial_version, [tr.num_targets, tr.num_barriers > 0]).rename_axis(index=\"version\",\n      columns=[\"targets\", \"barriers\"]))\nprint(\"delay (ms): min\", tr.delay.min(), \"max\", tr.delay.max(), \"| delay > 400 ms:\", (tr.delay > 400).sum(),\n      \"| negative delay:\", (tr.delay < 0).sum())\nprint(\"delay equals go - target onset (max |diff| ms):\", np.abs((tr.go_cue_time - tr.target_on_time) * 1000 - tr.delay).max().round(6))\nprint(\"rt (ms): min\", tr.rt.min(), \"max\", tr.rt.max(), \"| rt equals move onset - go (max |diff| ms):\",\n      np.abs((tr.move_onset_time - tr.go_cue_time) * 1000 - tr.rt).max().round(6))\nprint(\"trial start to go cue (s): min %.3f; move onset to trial end (s): min %.3f\" % (\n      (tr.go_cue_time - tr.start_time).min(), (tr.stop_time - tr.move_onset_time).min()))\nprint(\"target positions (mm): x %d to %d, y %d to %d\" % (tr.target_x.min(), tr.target_x.max(), tr.target_y.min(), tr.target_y.max()))\n\nprint(\"\\n=== units ===\")\nprint(\"units:\", len(units), \"| held out:\", int(units.heldout.sum()), \"| held in:\", int((~units.heldout).sum()))\nprint(\"spikes per unit: min\", units.n_spikes.min(), \"median\", int(units.n_spikes.median()), \"max\", units.n_spikes.max())\nprint(\"electrode group of each unit, as the units table gives it:\", units.electrode_group.value_counts().to_dict())\nel = nwb.electrodes.to_dataframe()\nprint(\"electrodes table:\", el.group_name.value_counts().to_dict(), \"| x, y, z all NaN:\",\n      bool(el[[\"x\", \"y\", \"z\"]].isna().all().all()))\nprint(\"units' electrode row equals the unit id's channel digits minus 1 for every unit:\",\n      bool((units.electrode_row == units.id_channel - 1).all()))\nprint(\"leading digit of unit id:\", units.id_digit.value_counts().sort_index().to_dict())\nobs_n = np.diff(np.r_[0, nwb.units.obs_intervals_index.data[:]])\nprint(\"observation intervals per unit: min\", obs_n.min(), \"max\", obs_n.max())\nobs = nwb.units.obs_intervals.data[: obs_n[0]]\nprint(\"unit 0 observation intervals equal the trial intervals:\",\n      bool(np.allclose(obs, tr[[\"start_time\", \"stop_time\"]].values)))\nallsp = np.concatenate(sess[\"spikes\"])\nti = np.searchsorted(tr.start_time.values, allsp, side=\"right\") - 1\ninside = (ti >= 0) & (allsp <= tr.stop_time.values[np.clip(ti, 0, None)])\nprint(\"spikes inside a trial interval: %.4f\" % inside.mean())\nprint(\"spike times sorted within every unit:\", all(np.all(np.diff(s) >= 0) for s in sess[\"spikes\"]))\n\nprint(\"\\n=== behaviour ===\")\nt = sess[\"hand_t\"]\ndt = np.diff(t)\nprint(\"hand samples:\", len(t), \"| steps of 1 ms: %.4f of steps; larger steps (between trials):\" % np.isclose(dt, 0.001).mean(),\n      int((~np.isclose(dt, 0.001)).sum()), \"| hand_vel shares timestamps:\", sess[\"vel_shares_pos_timestamps\"])\npos, vel = sess[\"hand_pos\"], sess[\"hand_vel\"]\nprint(\"hand position (mm): x %.1f to %.1f, y %.1f to %.1f\" % (pos[:, 0].min(), pos[:, 0].max(), pos[:, 1].min(), pos[:, 1].max()))\nprint(\"hand velocity (mm/s): x %.0f to %.0f, y %.0f to %.0f\" % (vel[:, 0].min(), vel[:, 0].max(), vel[:, 1].min(), vel[:, 1].max()))\nok = np.r_[np.isclose(dt, 0.001), False]\ngv = np.gradient(pos[:, 0]) * 1000\nm = ok & np.r_[False, ok[:-1]]\nslope = np.polyfit(gv[m][::50], vel[m, 0][::50], 1)[0]\nprint(\"hand_vel x against the derivative of hand_pos x: r = %.3f, slope %.3f\" % (\n      np.corrcoef(gv[m][::50], vel[m, 0][::50])[0, 1], slope))\n\nprint(\"\\n=== test file ===\")\ntt = nwb_test.trials.to_dataframe()\ntu = nwb_test.units\nprint(\"test trials:\", len(tt), \"| columns:\", list(tt.columns), \"| split:\", tt.split.unique())\nprint(\"test trial length (s):\", np.unique(np.round(tt.stop_time - tt.start_time, 3)),\n      \"| movement onset after trial start (s):\", np.unique(np.round(tt.move_onset_time - tt.start_time, 3)))\nprint(\"test units:\", len(tu), \"| same ids as the held-in train units:\",\n      set(tu.id.data[:]) == set(units.unit_id[~units.heldout]))\nprint(\"test file has behaviour:\", len(nwb_test.processing) > 0)\n\"\"\", tags=[\"sanity\"])\n\nmd(\"\"\"\nThe test file holds 574 more trials of the same session, as 0.7 s segments around movement onset\nwithout condition labels or behaviour, and only the 137 held-in units. It cannot enter a\ncondition-mean analysis. Below, its trials are checked against the train file for duplicates (the same\nspikes deposited twice).\n\"\"\")\n\ncode(r\"\"\"\n# duplicates: spike counts of the held-in units in the test segments against the same window of every train trial\nheld_ids = units.unit_id[~units.heldout].values\ntid = list(tu.id.data[:])\ntflat = tu.spike_times.data[:]; tidx = tu.spike_times_index.data[:]\ntsp = {tid[i]: np.asarray(tflat[a:b]) for i, (a, b) in enumerate(zip(np.r_[0, tidx[:-1]], tidx))}\ndef count_matrix(spk_list, starts, stops):\n    return np.array([np.searchsorted(s, stops) - np.searchsorted(s, starts) for s in spk_list]).T\ntest_counts = count_matrix([tsp[u] for u in held_ids], tt.start_time.values, tt.stop_time.values)\ntrain_sp = [sess[\"spikes\"][i] for i in np.where(~units.heldout)[0]]\nmv = tr.move_onset_time.values\ntrain_counts = count_matrix(train_sp, mv - 0.25, mv + 0.45)\nkey_train = {r.tobytes() for r in train_counts}\ndup = sum(r.tobytes() in key_train for r in test_counts)\nprint(\"test segments whose spike-count vector over 137 units equals that of a train trial:\", dup, \"of\", len(test_counts))\nprint(\"total spikes per segment: test median %d, train median %d\" % (np.median(test_counts.sum(1)), np.median(train_counts.sum(1))))\n\"\"\")\n\nmd(\"\"\"\n### Clocks\n\nHand speed is checked against the movement onset of the trial table, and the spikes against the trial\nevents by decoding the reach direction (the active target's angle in eight sectors) from the\npopulation spike counts in windows before and after target onset. Before target onset the direction\nis not yet known and decoding must be at chance; after it, it should be above chance.\n\"\"\")\n\ncode(r\"\"\"\np_w, v_w, err = mm.kinematic_windows(sess, tr.move_onset_time.values, 400, 600)\nprint(\"largest timestamp error of the kinematic windows (s): %.2e\" % err)\nspd = np.linalg.norm(v_w, axis=2)\ntk = np.arange(-400, 601)\nfor a, b in [(-400, -300), (-200, -100), (-50, 0), (0, 50), (100, 150), (200, 300)]:\n    mk = (tk >= a) & (tk < b)\n    print(f\"  mean hand speed {a:>5} to {b:>4} ms from movement onset: {spd[:, mk].mean():7.1f} mm/s\")\npeak = spd.max(1)\ncross = np.array([tk[np.argmax((s > 0.1 * pk) & (tk > -300))] for s, pk in zip(spd, peak)])\nprint(\"time speed first exceeds 10%% of its peak (ms from marked onset): median %d, 5th-95th percentile %d to %d\"\n      % (np.median(cross), *np.percentile(cross, [5, 95])))\n\nang = np.degrees(np.arctan2(tr.target_y, tr.target_x))\nsector = (np.round(ang / 45).astype(int) % 8).values\nspk_all = sess[\"spikes\"]\ncv = StratifiedKFold(5, shuffle=True, random_state=0)\nrng_clk = np.random.default_rng(1)\nrows = []\nfor name, ev, a, b in [(\"before target onset\", tr.target_on_time.values, -400, -100),\n                       (\"after target onset\", tr.target_on_time.values, 100, 400),\n                       (\"delay, before go\", tr.go_cue_time.values, -300, 0),\n                       (\"after movement onset\", tr.move_onset_time.values, 0, 300)]:\n    Xc = count_matrix(spk_all, ev + a / 1000, ev + b / 1000).astype(float)\n    acc = cross_val_score(LinearDiscriminantAnalysis(solver=\"lsqr\", shrinkage=\"auto\"), Xc, sector, cv=cv).mean()\n    accs = cross_val_score(LinearDiscriminantAnalysis(solver=\"lsqr\", shrinkage=\"auto\"), Xc,\n                           rng_clk.permutation(sector), cv=cv).mean()\n    rows.append((name, a, b, round(acc, 3), round(accs, 3)))\nprint(pd.DataFrame(rows, columns=[\"window\", \"from ms\", \"to ms\", \"accuracy\", \"accuracy, shuffled labels\"]).to_string(index=False))\nprint(\"chance (largest sector share): %.3f\" % (np.bincount(sector).max() / len(sector)))\n\"\"\")\n\nmd(\"\"\"\n### Trial selection and firing rates (M1, M2)\n\nTrials with delay > 400 ms (M1), then the proto-trial selection under readings T1 and T2. Rates: spikes\nsmoothed with a Gaussian of SD 20 ms, sampled every 10 ms, averaged over the kept trials of each\ncondition, locked to the go cue (-400 to +500 ms) and to movement onset (-400 to +800 ms). A condition\nleft with no trial is dropped from that reading's analyses.\n\"\"\")\n\ncode(r\"\"\"\ncond = tr.condition.values\nC = cond.max() + 1\nbase = tr.delay.values > mm.MIN_DELAY_MS\nmv = tr.move_onset_time.values\ngo = tr.go_cue_time.values\nkp, kv, _ = mm.kinematic_windows(sess, mv, 150, 900)      # 1 ms, -150 to +900 ms from onset\nproto = slice(0, 150 + 800 + 1)                          # M1 window, -150 to +800 ms\nkeep = {T: mm.proto_trial_keep(kv[:, proto], cond, base, T) & base for T in (\"T1\", \"T2\")}\nfor T, k in keep.items():\n    bc = np.bincount(cond[k], minlength=C)\n    print(f\"{T}: kept {k.sum()} of {base.sum()} trials with delay > 400 ms ({k.sum()/base.sum():.1%}); \"\n          f\"conditions with no trial {int((bc == 0).sum())}; trials per condition min {bc[bc > 0].min()}, \"\n          f\"median {int(np.median(bc[bc > 0]))}\")\nempty_T1 = np.where(np.bincount(cond[keep['T1']], minlength=C) == 0)[0]\nprint(\"conditions empty under T1:\")\nprint(tr[tr.condition.isin(empty_T1)].groupby(\"condition\")[[\"trial_type\", \"trial_version\", \"target_x\", \"target_y\"]].first())\n\navg = {T: mm.averaging_matrix(cond, k, C) for T, k in keep.items()}\nt0 = time.time()\ntg, GO = mm.condition_rates(sess[\"spikes\"], go, 400, 500, avg)\ntm, MV = mm.condition_rates(sess[\"spikes\"], mv, 400, 800, avg)\nprint(\"rates computed in %.0f s\" % (time.time() - t0))\n\nD = {}\nfor T in (\"T1\", \"T2\"):\n    has = np.bincount(cond[keep[T]], minlength=C) > 0\n    G, M = GO[T][:, has], MV[T][:, has]\n    X = mm.window_mean(G, tg, mm.PREP_WIN)      # units x conditions, preparatory (M4)\n    Pm = mm.window_mean(M, tm, mm.PERI_WIN)     # peri-movement (M4)\n    A = avg[T][has]\n    kin_p = np.einsum(\"ct,tsj->csj\", A, kp)\n    kin_v = np.einsum(\"ct,tsj->csj\", A, kv)\n    rt_c = A @ tr.rt.values\n    D[T] = dict(has=has, G=G, M=M, X=X, P=Pm, kin_p=kin_p, kin_v=kin_v, rt=rt_c,\n                trc=tr[keep[T]].groupby(\"condition\").first().loc[np.where(has)[0]])\n    print(f\"{T}: {has.sum()} conditions; preparatory rates {X.min():.1f} to {X.max():.1f} spikes/s; \"\n          f\"peri-movement rates {Pm.min():.1f} to {Pm.max():.1f} spikes/s\")\n\nSEL = {}\nfor T in D:\n    for S in (\"S1\", \"S2\"):\n        pt, qt = mm.tuning(D[T][\"X\"], S), mm.tuning(D[T][\"P\"], S)\n        prep = pt > mm.PREP_TUNING_MIN\n        both = prep & (qt >= mm.PERI_TUNING_RATIO * pt)\n        SEL[T, S] = dict(prep=prep, both=both)\n        print(f\"{T} {S}: preparatory tuning > 5 spikes/s: {prep.sum()} of {len(pt)} units; \"\n              f\"also peri-movement tuning >= 1.5x: {both.sum()} \"\n              f\"(tuning range {pt.min():.1f} to {pt.max():.1f} spikes/s)\")\n\"\"\")\n\n# ---------------------------------------------------------------- claims\nmd(\"\"\"\n## recordings-jarray\n\n> The J-array dataset holds 146 single- and multi-unit isolations from two 96-electrode arrays,\n> recorded on the maze task with 108 conditions, with a mean of 2166 trials per neuron.\n\nExpected 146 ± 14.6 units, 108 conditions (tolerance 0), 2166 ± 216.6 trials per neuron, under reading\n(a) all successful trials or (b) those kept by M1. Every unit is observed on every trial (its\nobservation intervals are the trial intervals), so trials per neuron is the trial count.\n\"\"\")\n\ncode(r\"\"\"\nrows = [(\"units (all)\", len(units), 146, 14.6),\n        (\"units (held in only)\", int((~units.heldout).sum()), 146, 14.6),\n        (\"conditions\", tr.condition.nunique(), 108, 0),\n        (\"trials per neuron, (a) successful trials with condition labels (train file)\", len(tr), 2166, 216.6),\n        (\"trials per neuron, (a) all successful trials incl. 574 unlabelled test segments\", len(tr) + len(tt), 2166, 216.6),\n        (\"trials per neuron, (b) M1 with T1\", int(keep['T1'].sum()), 2166, 216.6),\n        (\"trials per neuron, (b) M1 with T2\", int(keep['T2'].sum()), 2166, 216.6),\n        (\"trials per neuron, delay > 400 ms only\", int(base.sum()), 2166, 216.6)]\ndf = pd.DataFrame(rows, columns=[\"quantity\", \"dataset\", \"paper\", \"tolerance\"])\ndf[\"within\"] = (df.dataset - df.paper).abs() <= df.tolerance\nprint(df.to_string(index=False))\n\"\"\", tags=[\"claim:recordings-jarray\"])\n\nmd(\"\"\"\n**Result: partially reproduced.** The 108 conditions match, and the 2295 labelled successful trials are\nwithin tolerance of 2166 (reading a), as are the 1967 trials with delay > 400 ms; under M1 with T2 the\n1786 kept trials are not, nor are T1's 1452. The unit count is not: the dataset has 182 units (137 held in\nand 45 held out), 36 more than 146 and outside the tolerance of 14.6.\n\"\"\")\n\n# fig3 + fig4d\nmd(\"\"\"\n## fig4d-mean-correlation-jarray\n\n> In the J-array dataset the correlation between a neuron's preparatory and peri-movement tuning is\n> positive on average but small (mean r = 0.13, p = 0.03; mean Spearman r = 0.11).\n\nPer neuron passing M6 (S1, S2), Pearson and Spearman correlations over conditions between the M4\npreparatory and peri-movement rates, trials by M1 (T1, T2); tests P1 to P3. Reproduced when under one\ncombination both means are within tolerance (0.13 ± 0.013, 0.11 ± 0.011) and p < 0.05 with the mean positive.\n\"\"\")\n\ncode(r\"\"\"\nR = {}\nrows = []\nfor T in D:\n    for S in (\"S1\", \"S2\"):\n        sel = SEL[T, S][\"both\"]\n        X, Pm = D[T][\"X\"][sel], D[T][\"P\"][sel]\n        r = mm.corr_rows(X, Pm) if sel.sum() else np.array([])\n        rs = mm.spearman_rows(X, Pm) if sel.sum() else np.array([])\n        R[T, S] = dict(r=r, rs=rs, ids=np.where(sel)[0])\n        if len(r) < 2:\n            rows.append((T, S, len(r), np.nan, np.nan, \"\", np.nan, False))\n            continue\n        for P, p in mm.mean_tests(r).items():\n            ok = (abs(r.mean() - 0.13) <= 0.013 + 1e-12) and (abs(rs.mean() - 0.11) <= 0.011 + 1e-12) and p < 0.05 and r.mean() > 0\n            rows.append((T, S, len(r), round(r.mean(), 4), round(rs.mean(), 4), P, p, ok))\ntab4d = pd.DataFrame(rows, columns=[\"trials\", \"tuning\", \"neurons\", \"mean r\", \"mean Spearman\", \"test\", \"p\", \"reproduced\"])\nprint(tab4d.to_string(index=False))\nprint(\"\\nSD of r and range, per selection:\")\nfor k, v in R.items():\n    if len(v[\"r\"]):\n        print(f\"  {k}: n={len(v['r'])}, SD {v['r'].std(ddof=1):.3f}, r from {v['r'].min():.2f} to {v['r'].max():.2f}\")\n\"\"\", tags=[\"claim:fig4d-mean-correlation-jarray\"])\n\ncode(r\"\"\"\nfig, axs = plt.subplots(1, 2, figsize=(8, 2.8), sharey=True)\nfor ax, T in zip(axs, (\"T1\", \"T2\")):\n    r = R[T, \"S1\"][\"r\"]\n    ax.hist(r, bins=np.linspace(-1, 1, 21), color=\"#4a6fa5\", edgecolor=\"white\")\n    ax.axvline(r.mean(), color=\"k\", lw=1)\n    ax.set_title(f\"{T}, S1: n={len(r)}, mean r={r.mean():.2f}\", fontsize=9)\n    ax.set_xlabel(\"tuning correlation (all values within -1 to 1)\")\naxs[0].set_ylabel(\"neurons\")\nplt.tight_layout(); plt.show()\n\"\"\", tags=[\"claim:fig4d-mean-correlation-jarray\"])\n\nmd(\"\"\"\n**Result: reproduced.** Under T1 with S1 (24 neurons) the mean Pearson r is 0.117 and the mean Spearman r\n0.102, both within tolerance, and all three tests give p < 0.05 (0.011 to 0.015). Under T2 with S1 (17\nneurons) the means are 0.051 and 0.072 and no test is significant. S2 selects no neuron under either\ntrial reading, so it gives no result.\n\"\"\")\n\nmd(\"\"\"\n## fig3-maze-most-not-maintained\n\n> In the maze task some neurons keep similar tuning between the preparatory and peri-movement epochs, but most do not.\n\nNeurons as for Figure 4 (M6, both readings). Reproduced when at least one neuron has r ≥ 0.72 and more than\nhalf have r < 0.72.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (T, S), v in R.items():\n    r = v[\"r\"]\n    if not len(r):\n        rows.append((T, S, 0, 0, np.nan, None)); continue\n    rows.append((T, S, len(r), int((r >= 0.72).sum()), round((r < 0.72).mean(), 3),\n                 bool((r >= 0.72).sum() >= 1 and (r < 0.72).mean() > 0.5)))\nprint(pd.DataFrame(rows, columns=[\"trials\", \"tuning\", \"neurons\", \"r >= 0.72\", \"share r < 0.72\", \"holds\"]).to_string(index=False))\nfor T in D:\n    r = R[T, \"S1\"][\"r\"]\n    print(f\"{T} S1: largest r values\", np.round(np.sort(r)[-4:], 3))\n\"\"\", tags=[\"claim:fig3-maze-most-not-maintained\"])\n\nmd(\"\"\"\n**Result: reproduced.** Under both trial readings with S1, at least one neuron keeps its tuning (r ≥ 0.72; 1 neuron under\nT1, 1 under T2) and most do not (share below 0.72 of 0.958 and 0.941). S2 selects no neuron.\n\"\"\")\n\nmd(\"\"\"\n## fig4-no-separate-populations\n\n> The distributions of tuning correlations give little evidence ... of one population with concordant\n> tuning (r near 1) and another with opposing tuning (r near -1); most neurons have weakly correlated tuning.\n\nJ-array only (Figure 4D). U1: Hartigan's dip test p ≥ 0.05; U2: more neurons with |r| < 0.5 than with |r| ≥ 0.5.\nReproduced when both hold, not reproduced when neither does, methods_underspecified when they disagree.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (T, S), v in R.items():\n    r = v[\"r\"]\n    if len(r) < 4:\n        rows.append((T, S, len(r), np.nan, np.nan, None, None, np.nan)); continue\n    dip, p = diptest.diptest(r)\n    u2 = (np.abs(r) < 0.5).sum() > (np.abs(r) >= 0.5).sum()\n    rows.append((T, S, len(r), round(dip, 4), round(p, 3), p >= 0.05, bool(u2), round((np.abs(r) >= 0.8).mean(), 3)))\nprint(pd.DataFrame(rows, columns=[\"trials\", \"tuning\", \"neurons\", \"dip\", \"dip p\", \"U1\", \"U2\", \"share |r| >= 0.8\"]).to_string(index=False))\nfor T in D:\n    r = R[T, \"S1\"][\"r\"]\n    print(f\"{T} S1: |r| < 0.5 in {(np.abs(r) < 0.5).sum()}, |r| >= 0.5 in {(np.abs(r) >= 0.5).sum()}; median r {np.median(r):.3f}\")\n\"\"\", tags=[\"claim:fig4-no-separate-populations\"])\n\nmd(\"\"\"\n**Result: reproduced.** Under T1 and T2 with S1, the dip test finds no departure from unimodality (p of 0.85\nand 0.95), and most neurons have |r| < 0.5 (22 of 24 and 16 of 17). No neuron has |r| ≥ 0.8.\n\"\"\")\n\nmd(\"\"\"\n## fig4e-correlation-time-course\n\n> The correlation between preparatory tuning and peri-movement tuning measured at single time points begins\n> to decline about 200 ms before movement onset and is near zero by movement onset.\n\nNeurons as in fig4d. Readings A1 (movement-locked rates throughout) and A2 (go-locked up to 100 ms after\nthe go cue, movement-locked from 300 ms before onset; in the gap between them, or where they overlap, the\ntwo are joined linearly; each condition's go cue is placed at its mean reaction time before onset).\n(i) mean correlation at onset not significantly above zero by P1 to P3; (ii) lower at onset than at -200 ms,\nwith more than half the drop from -400 ms to onset after -200 ms.\n\"\"\")\n\ncode(r\"\"\"\ntau = np.arange(-400, 201, 10)\n\ndef spliced(T):\n    G, M, rt_c = D[T][\"G\"], D[T][\"M\"], D[T][\"rt\"]\n    out = np.zeros(G.shape[:2] + (len(tau),))\n    mv_part = M[:, :, np.searchsorted(tm, tau.clip(-400, 800))]\n    for c in range(G.shape[1]):\n        go_end = 100 - rt_c[c]                    # end of the go-locked part, ms from onset\n        g = np.array([np.interp(tau + rt_c[c], tg, G[u, c]) for u in range(G.shape[0])])\n        m = mv_part[:, c]\n        w = np.zeros(len(tau))\n        lo, hi = min(go_end, -300), max(go_end, -300)\n        w[tau >= hi] = 1\n        mid = (tau > lo) & (tau < hi)\n        w[mid] = (tau[mid] - lo) / (hi - lo)\n        if go_end > -300:      # overlap: fade from go-locked to movement-locked\n            out[:, c] = (1 - w) * g + w * m\n        else:                  # gap: join the last go-locked value to the first movement-locked one\n            g_end = np.array([np.interp(go_end + rt_c[c], tg, G[u, c]) for u in range(G.shape[0])])\n            m_start = M[:, c, np.searchsorted(tm, -300)]\n            out[:, c] = np.where(tau <= lo, g.T, np.where(tau >= hi, m.T, (g_end + np.outer(w, m_start - g_end).T.T * 0).T * 0\n                                 + ((1 - w)[:, None] * g_end + w[:, None] * m_start))).T\n    return out\n\ncurves = {}\nrows = []\nfor T in D:\n    print(f\"{T}: mean reaction time per condition {D[T]['rt'].min():.0f} to {D[T]['rt'].max():.0f} ms\")\n    rate_A = {\"A1\": D[T][\"M\"][:, :, np.searchsorted(tm, tau)], \"A2\": spliced(T)}\n    for S in (\"S1\", \"S2\"):\n        ids = R[T, S][\"ids\"]\n        if len(ids) < 2:\n            continue\n        for A, rates in rate_A.items():\n            cc = np.array([mm.corr_rows(D[T][\"X\"][ids], rates[ids, :, i]) for i in range(len(tau))]).T\n            mc = cc.mean(0)\n            curves[T, S, A] = mc\n            c0, c200, c400 = mc[tau == 0][0], mc[tau == -200][0], mc[tau == -400][0]\n            tests = mm.mean_tests(cc[:, tau == 0][:, 0])\n            cond_i = all((p >= 0.05) or (c0 <= 0) for p in tests.values())\n            cond_ii = (c0 < c200) and ((c200 - c0) > 0.5 * (c400 - c0))\n            rows.append((T, S, A, len(ids), round(c400, 3), round(c200, 3), round(c0, 3),\n                         round(min(tests.values()), 3), cond_i, round((c200 - c0) / (c400 - c0), 3), cond_ii))\ntab4e = pd.DataFrame(rows, columns=[\"trials\", \"tuning\", \"rates\", \"neurons\", \"r(-400)\", \"r(-200)\", \"r(0)\",\n                                    \"smallest p at 0\", \"(i)\", \"share of drop after -200\", \"(ii)\"])\nprint(tab4e.to_string(index=False))\n\"\"\", tags=[\"claim:fig4e-correlation-time-course\"])\n\ncode(r\"\"\"\nfig, ax = plt.subplots(figsize=(5, 3))\nfor (T, S, A), mc in curves.items():\n    ax.plot(tau, mc, lw=1.5, ls=\"-\" if A == \"A1\" else \"--\", label=f\"{T} {S} {A}\")\nax.axhline(0, color=\"0.7\", lw=0.8); ax.axvline(0, color=\"0.7\", lw=0.8)\nax.set_xlabel(\"ms from movement onset\"); ax.set_ylabel(\"mean correlation with preparatory tuning\")\nax.legend(fontsize=7); plt.tight_layout(); plt.show()\nprint(\"range of plotted values: %.3f to %.3f\" % (min(c.min() for c in curves.values()), max(c.max() for c in curves.values())))\n\"\"\", tags=[\"claim:fig4e-correlation-time-course\"])\n\nmd(\"\"\"\n**Result: ...** (filled in after the run)\n\"\"\")\n\nmd(\"\"\"\n## suppfig1-population-averages\n\n> In population averages sorted by each neuron's preparatory preference, the weak agreement ... dominates\n> early, but the separation shrinks with time and shows little relation to preparatory tuning by movement onset.\n\nNeurons as in fig4d. Per neuron the strongest and weakest preparatory conditions and those at one and two\nthirds of the rank order; rates divided by the neuron's maximum rate; averaged over neurons. Separation =\nstrongest minus weakest. Reproduced when the preparatory separation is positive and the separation at onset\nis below half (R1) or a quarter (R2) of it. Which maximum is open; readings (a) the maximum over all\nconditions and times of the go- and movement-locked averages; (b) the maximum over the four chosen\nconditions' traces.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nsep_curves = {}\nfor T in D:\n    G, M, X = D[T][\"G\"], D[T][\"M\"], D[T][\"X\"]\n    c = X.shape[1]\n    for S in (\"S1\", \"S2\"):\n        ids = R[T, S][\"ids\"]\n        if len(ids) < 1:\n            continue\n        for NM in (\"a\", \"b\"):\n            sg, sm, mids = [], [], []\n            for u in ids:\n                order = np.argsort(X[u])\n                pick = [order[-1], order[int(round(2 * (c - 1) / 3))], order[int(round((c - 1) / 3))], order[0]]\n                mx = max(G[u].max(), M[u].max()) if NM == \"a\" else max(G[u, pick].max(), M[u, pick].max())\n                sg.append((G[u, pick[0]] - G[u, pick[3]]) / mx)\n                sm.append((M[u, pick[0]] - M[u, pick[3]]) / mx)\n                mids.append((M[u, pick[1]] - M[u, pick[2]]) / mx)\n            sg, sm = np.mean(sg, 0), np.mean(sm, 0)\n            sep_curves[T, S, NM] = (sg, sm)\n            prep = sg[(tg >= -200) & (tg <= 100)].mean()\n            at0 = sm[tm == 0][0]\n            rows.append((T, S, NM, len(ids), round(prep, 4), round(at0, 4), round(at0 / prep, 3),\n                         prep > 0 and at0 < 0.5 * prep, prep > 0 and at0 < 0.25 * prep))\nprint(pd.DataFrame(rows, columns=[\"trials\", \"tuning\", \"max\", \"neurons\", \"separation, prep epoch\",\n                                  \"separation at onset\", \"ratio\", \"R1 (< 1/2)\", \"R2 (< 1/4)\"]).to_string(index=False))\nfor T in D:\n    sg, sm = sep_curves[T, \"S1\", \"a\"]\n    print(f\"{T} S1 (a): separation at -300, -200, -100, 0, +100 ms from onset:\",\n          np.round(sm[np.searchsorted(tm, [-300, -200, -100, 0, 100])], 4))\n\"\"\", tags=[\"claim:suppfig1-population-averages\"])\n\nmd(\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(\"\"\"\n## prep-dimensionality\n\n> Preparatory activity is moderately high-dimensional; depending on the dataset, 7 to 10 dimensions capture 90% of its variance.\n\nThe c x n matrix of M4 preparatory rates, columns mean-centred, PCA; the number of components for 90%.\nReproduced when within 7 to 11 under one reading (N1: prep-tuned neurons, S1 and S2; N2: all neurons).\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor T in D:\n    X = D[T][\"X\"]\n    for N, sel in ((\"N1 S1\", SEL[T, \"S1\"][\"prep\"]), (\"N1 S2\", SEL[T, \"S2\"][\"prep\"]), (\"N2\", np.ones(len(X), bool))):\n        M_ = X[sel].T\n        Mc = M_ - M_.mean(0)\n        sv = np.linalg.svd(Mc, compute_uv=False) ** 2\n        cum = np.cumsum(sv) / sv.sum()\n        k90 = int(np.searchsorted(cum, 0.9) + 1)\n        rows.append((T, N, int(sel.sum()), k90, 7 <= k90 <= 11, np.round(cum[:3], 3)))\nprint(pd.DataFrame(rows, columns=[\"trials\", \"neurons\", \"n\", \"components for 90%\", \"within 7 to 11\", \"first 3 cumulative\"]).to_string(index=False))\n\"\"\", tags=[\"claim:prep-dimensionality\"])\n\nmd(\"\"\"\n**Result: ...**\n\"\"\")\n\n# fig6\nmd(\"\"\"\n## PD performance (fig6 claims, fig7a, fig7b, fig7d)\n\nNeurons passing the preparatory part of M6 (S1, S2). The peri-movement space (M5) is built for each neuron\nfrom the condition-mean rates of all other 181 units, -150 to +800 ms from onset. The kinematic space is the\nPCA of position, velocity and acceleration (acceleration as the time derivative of the dataset's hand\nvelocity) from -150 ms to 800 (W1) or 600 (W2) ms, each scaled to unit range, the six variables once (D1) or\nrepeated to 181 column blocks (D2). Task spaces by M9 from the condition-mean hand trajectories, with the\nreadings V1 (a: largest magnitudes; b: signed component at its largest magnitude), V2, G1 and G2.\nPerformance by M7 for k = 1 to 14.\n\"\"\")\n\ncode(r\"\"\"\nKMAX = 14\nPERF = {}\nt0 = time.time()\nfor T in D:\n    X, M = D[T][\"X\"], D[T][\"M\"]\n    win = (tm >= -150) & (tm <= 800)\n    blocks = M[:, :, win]\n    out = dict(blocks=blocks)\n    out[\"peri\"] = mm.peri_space_performance(blocks, X.T, KMAX)\n    out[\"peri_start0\"] = mm.peri_space_performance(M[:, :, (tm >= 0) & (tm <= 800)], X.T, KMAX)\n    P_, V_ = D[T][\"kin_p\"], D[T][\"kin_v\"]\n    Acc = np.gradient(V_, axis=1) * 1000\n    kin, kinS = {}, {}\n    for W, end in ((\"W1\", 800), (\"W2\", 600)):\n        sl = np.arange(0, 150 + end + 1, 10)\n        for Dd, nb in ((\"D1\", None), (\"D2\", blocks.shape[0] - 1)):\n            Tk = mm.kinematic_tmatrix(P_[:, sl], V_[:, sl], Acc[:, sl], nb)\n            kinS[W + Dd] = mm.pca_scores(Tk, KMAX)\n            kin[W + Dd] = mm.space_performance_all_k(kinS[W + Dd], X.T, KMAX)\n    out[\"kin\"], out[\"kinS\"] = kin, kinS\n    feats = [mm.task_features(P_[c], V_[c], 150) for c in range(P_.shape[0])]\n    trc = D[T][\"trc\"]\n    tsp = mm.task_spaces(feats, (trc.num_barriers > 0).astype(float).values, (trc.num_targets > 1).astype(float).values)\n    out[\"taskS\"] = tsp\n    out[\"task\"] = {k: mm.loo_performance(S_, X.T) for k, S_ in tsp.items()}\n    ends = np.array([f[\"end_ms\"] for f in feats])\n    print(f\"{T}: end of reach {ends.min()} to {ends.max()} ms after onset (median {np.median(ends):.0f}); \"\n          f\"reaches never falling below 5% of peak speed by +900 ms: {(ends >= 900).sum()}\")\n    PERF[T] = out\nprint(\"PD performance computed in %.0f s\" % (time.time() - t0))\n\nTASK_BASE = {\"endpoints + max speed\": [\"endpoints + max speed\"], \"initial velocity\": [\"initial velocity\"],\n             \"endpoints + orthogonal excursion\": [\"endpoints + orthogonal excursion\"],\n             \"endpoints + viapoint\": [\"endpoints + viapoint\"],\n             \"endpoints + max velocity\": [\"endpoints + max velocity (V1a)\", \"endpoints + max velocity (V1b)\", \"endpoints + max velocity (V2)\"],\n             \"endpoints + halfpoint\": [\"endpoints + halfpoint\"],\n             \"segment directions\": [\"segment directions (G1)\", \"segment directions (G2)\"],\n             \"kitchen sink\": [\"kitchen sink (G1)\", \"kitchen sink (G2)\"]}\n\ndef mean_curves(T, S):\n    sel = SEL[T, S][\"prep\"]\n    pf = PERF[T]\n    return dict(n=int(sel.sum()), peri=pf[\"peri\"][sel].mean(0), peri0=pf[\"peri_start0\"][sel].mean(0),\n                kin={k: v[sel].mean(0) for k, v in pf[\"kin\"].items()},\n                task={k: v[sel].mean() for k, v in pf[\"task\"].items()},\n                dims={k: S_.shape[1] for k, S_ in pf[\"taskS\"].items()})\n\nMC = {(T, S): mean_curves(T, S) for T in D for S in (\"S1\", \"S2\")}\nfor (T, S), mc in MC.items():\n    print(f\"\\n{T} {S}: {mc['n']} neurons\")\n    print(\"  k:             \", \" \".join(f\"{k:6d}\" for k in range(1, KMAX + 1)))\n    print(\"  peri-movement: \", \" \".join(f\"{v:6.3f}\" for v in mc[\"peri\"]))\n    for k, v in mc[\"kin\"].items():\n        print(f\"  kinematic {k}:\", \" \".join(f\"{x:6.3f}\" for x in v))\n    for k, v in mc[\"task\"].items():\n        print(f\"  task {k} ({mc['dims'][k]}-D): {v:.3f}\")\n\"\"\")\n\ncode(r\"\"\"\nfig, axs = plt.subplots(1, 2, figsize=(9, 3.2), sharey=True)\nks = np.arange(1, KMAX + 1)\nfor ax, T in zip(axs, (\"T1\", \"T2\")):\n    mc = MC[T, \"S1\"]\n    ax.plot(ks, mc[\"peri\"], color=\"#1f4e79\", lw=2, label=\"peri-movement\")\n    ax.plot(ks, mc[\"kin\"][\"W1D1\"], color=\"#c55a11\", lw=2, label=\"kinematic (W1 D1)\")\n    for k, v in mc[\"task\"].items():\n        ax.plot(mc[\"dims\"][k], v, \"o\", color=\"#548235\", ms=5)\n    ax.plot([], [], \"o\", color=\"#548235\", label=\"task spaces\")\n    ax.axhline(0, color=\"0.8\", lw=0.8)\n    ax.set_title(f\"{T}, S1 ({mc['n']} neurons)\", fontsize=9); ax.set_xlabel(\"dimensionality k\")\naxs[0].set_ylabel(\"mean PD performance\"); axs[0].legend(fontsize=7)\nplt.tight_layout(); plt.show()\nallv = np.concatenate([np.r_[MC[T, 'S1']['peri'], MC[T, 'S1']['kin']['W1D1'], list(MC[T, 'S1']['task'].values())] for T in D])\nprint(\"range of plotted values: %.3f to %.3f (all inside the axes)\" % (allv.min(), allv.max()))\n\"\"\")\n\nmd(\"\"\"\n## fig6-peri-movement-space-best\n\n> For every dataset the highest cross-validated PD performance ... is reached when the PD is expressed in\n> the space built by PCA from the population peri-movement response.\n\nReproduced when, under every combination (T, S, K, W, D, V, G), the best mean performance over k of the\nperi-movement space exceeds the best of every other space; methods_underspecified if the combinations disagree.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (T, S), mc in MC.items():\n    for K in (14, 12):\n        pb, pk = mc[\"peri\"][:K].max(), int(np.argmax(mc[\"peri\"][:K]) + 1)\n        kb = max(v[:K].max() for v in mc[\"kin\"].values())\n        tb_name = max(mc[\"task\"], key=mc[\"task\"].get)\n        tb = mc[\"task\"][tb_name]\n        # every combination of W, D, V, G is won only if the peri-movement best exceeds every variant\n        n_comb = 0; n_win = 0\n        for W in (\"W1\", \"W2\"):\n            for Dd in (\"D1\", \"D2\"):\n                for V in (\"V1a\", \"V1b\", \"V2\"):\n                    for Gg in (\"G1\", \"G2\"):\n                        others = [mc[\"kin\"][W + Dd][:K].max()] + [mc[\"task\"][n] for n in mc[\"task\"]\n                                  if (\"(\" not in n) or (f\"({V})\" in n) or (f\"({Gg})\" in n)]\n                        n_comb += 1; n_win += pb > max(others)\n        rows.append((T, S, f\"K{1 if K == 14 else 2}\", mc[\"n\"], round(pb, 3), pk, round(kb, 3), tb_name, round(tb, 3), f\"{n_win}/{n_comb}\"))\ntab6 = pd.DataFrame(rows, columns=[\"trials\", \"tuning\", \"k max\", \"neurons\", \"peri best\", \"at k\", \"kinematic best\", \"best task space\",\n                                   \"its perf.\", \"combinations won by peri\"])\nprint(tab6.to_string(index=False))\n\"\"\", tags=[\"claim:fig6-peri-movement-space-best\"])\n\nmd(\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(\"\"\"\n## fig6-each-dimensionality\n\n> Considering each dimensionality separately, PD performance is almost always higher in the peri-movement space ...;\n> for the maze task the 3-D endpoints and peak speed space does not perform well.\n\nEach task space against the peri-movement space at its dimensionality; the kinematic space against it at each\nk up to K. L1: all comparisons but at most one won; L2: at least 90% won. Reproduced when the 3-D endpoints +\nmax speed space is below the 3-D peri-movement space and the peri-movement space wins under L1 and L2.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (T, S), mc in MC.items():\n    for K in (14, 12):\n        for W in (\"W1\", \"W2\"):\n            for Dd in (\"D1\", \"D2\"):\n                for V in (\"V1a\", \"V1b\", \"V2\"):\n                    for Gg in (\"G1\", \"G2\"):\n                        comps = []\n                        for base_name, variants in TASK_BASE.items():\n                            n = variants[0] if len(variants) == 1 else next(v for v in variants if f\"({V})\" in v or f\"({Gg})\" in v)\n                            d = mc[\"dims\"][n]\n                            comps.append(mc[\"peri\"][d - 1] > mc[\"task\"][n])\n                        comps += list(mc[\"peri\"][:K] > mc[\"kin\"][W + Dd][:K])\n                        comps = np.array(comps)\n                        ems = mc[\"task\"][\"endpoints + max speed\"] < mc[\"peri\"][2]\n                        L1 = (~comps).sum() <= 1\n                        L2 = comps.mean() >= 0.9\n                        rows.append((T, S, K, W + Dd, V, Gg, len(comps), int(comps.sum()), ems, L1, L2))\ntab6b = pd.DataFrame(rows, columns=[\"trials\", \"tuning\", \"K\", \"kin\", \"V\", \"G\", \"comparisons\", \"won\", \"ems below peri 3-D\", \"L1\", \"L2\"])\nsummary = tab6b.groupby([\"trials\", \"tuning\", \"K\"]).agg(won_min=(\"won\", \"min\"), won_max=(\"won\", \"max\"), comps=(\"comparisons\", \"first\"),\n                                                       ems=(\"ems below peri 3-D\", \"all\"), L1_all=(\"L1\", \"all\"), L1_any=(\"L1\", \"any\"),\n                                                       L2_all=(\"L2\", \"all\"), L2_any=(\"L2\", \"any\"))\nprint(summary.to_string())\nfor (T, S), mc in MC.items():\n    print(f\"{T} {S}: endpoints + max speed {mc['task']['endpoints + max speed']:.3f}, peri-movement 3-D {mc['peri'][2]:.3f}\")\n\"\"\", tags=[\"claim:fig6-each-dimensionality\"])\n\nmd(\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(\"\"\"\n## fig6-performance-vs-dimensionality\n\n> PD performance in PCA-based spaces generally improves with dimensionality, peaks in a middle range, and\n> declines beyond about 10 dimensions through over-fitting.\n\nPeri-movement space, k = 1 to 14: reproduced when performance at the best k exceeds that at k = 1, the best\nk is 10 or below, and performance at k = 14 is below that at the best k.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (T, S), mc in MC.items():\n    p = mc[\"peri\"]\n    kb = int(np.argmax(p) + 1)\n    rows.append((T, S, mc[\"n\"], round(p[0], 3), kb, round(p.max(), 3), round(p[-1], 3),\n                 p.max() > p[0], kb <= 10, p[-1] < p.max()))\nprint(pd.DataFrame(rows, columns=[\"trials\", \"tuning\", \"neurons\", \"k=1\", \"best k\", \"best\", \"k=14\",\n                                  \"improves\", \"best k <= 10\", \"declines at 14\"]).to_string(index=False))\n\"\"\", tags=[\"claim:fig6-performance-vs-dimensionality\"])\n\nmd(\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(\"\"\"\n## fig7a-shuffled-space-poor\n\n> A control space built from peri-movement responses in which each neuron's peri-movement pattern was inverted\n> on a random half of the conditions performs poorly.\n\nPer neuron and condition with probability 0.5, activity after -150 ms reflected about the rate at -150 ms;\n10 shuffles (claims file standard choice), mean performance. H1: below the unshuffled space at every k;\nH2: H1 and its best over k below the best kinematic space. Reproduced when both hold; methods_underspecified\nwhen only H1 holds.\n\"\"\")\n\ncode(r\"\"\"\nrng7a = np.random.default_rng(7001)\nSHUF = {}\nfor T in D:\n    blocks = PERF[T][\"blocks\"]\n    X = D[T][\"X\"]\n    reps = []\n    for s in range(10):\n        flip = rng7a.random(blocks.shape[:2]) < 0.5\n        b = blocks.copy()\n        ref = blocks[:, :, :1]\n        b[flip] = (2 * ref - blocks)[flip]\n        reps.append(mm.peri_space_performance(b, X.T, KMAX))\n    SHUF[T] = np.array(reps)            # shuffles x neurons x k\nrows = []\nfor (T, S), mc in MC.items():\n    sel = SEL[T, S][\"prep\"]\n    sh = SHUF[T][:, sel].mean(1)        # shuffles x k\n    shm = sh.mean(0)\n    print(f\"{T} {S}: shuffled mean by k\", np.round(shm, 3), \"| spread over shuffles of the best: %.3f to %.3f\" % (sh.max(1).min(), sh.max(1).max()))\n    for K in (14, 12):\n        H1 = bool(np.all(shm[:K] < mc[\"peri\"][:K]))\n        kb = min(v[:K].max() for v in mc[\"kin\"].values())\n        kbmax = max(v[:K].max() for v in mc[\"kin\"].values())\n        H2_all = H1 and shm[:K].max() < kb\n        rows.append((T, S, K, round(shm[:K].max(), 3), round(mc[\"peri\"][:K].max(), 3), round(kb, 3), round(kbmax, 3), H1, H2_all))\nprint(pd.DataFrame(rows, columns=[\"trials\", \"tuning\", \"K\", \"shuffled best\", \"peri best\", \"kinematic best (lowest variant)\",\n                                  \"(highest variant)\", \"H1\", \"H2 (every W, D)\"]).to_string(index=False))\n\"\"\", tags=[\"claim:fig7a-shuffled-space-poor\"])\n\nmd(\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(\"\"\"\n## fig7b-window-start-slide\n\n> Moving the start of the peri-movement window from 150 ms before movement onset to movement onset costs little\n> PD performance; at movement onset performance is 97% (monkey J) and 94% (monkeys A, B) of its original value.\n\nPerformance at the best k for the window starting at -150 and at 0 ms (end at +800). Reading J2: the J-array\nratio is compared with 0.97 ± 0.097. The A and B value cannot be tested.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (T, S), mc in MC.items():\n    for K in (14, 12):\n        a, b = mc[\"peri\"][:K].max(), mc[\"peri0\"][:K].max()\n        rows.append((T, S, K, mc[\"n\"], round(a, 3), int(np.argmax(mc[\"peri\"][:K]) + 1), round(b, 3),\n                     int(np.argmax(mc[\"peri0\"][:K]) + 1), round(b / a, 3), abs(b / a - 0.97) <= 0.097))\nprint(pd.DataFrame(rows, columns=[\"trials\", \"tuning\", \"K\", \"neurons\", \"best from -150\", \"k\", \"best from 0\", \"k\", \"ratio\",\n                                  \"within 0.97 +- 0.097\"]).to_string(index=False))\n\"\"\", tags=[\"claim:fig7b-window-start-slide\"])\n\nmd(\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(\"\"\"\n## fig7d-pd-consistency\n\n> When the PD is measured on two random sets of 25 conditions, it is most stable in the peri-movement space,\n> for every comparison space and all four datasets.\n\nPer neuron, 25 conditions drawn with replacement, the PD (unit length) fitted by M7 regression, refitted on\nanother 25; consistency is the dot product, averaged over 100 draws (claims file standard choice) and over\nneurons. Comparisons: endpoints + max speed (3-D), segment directions (6-D; G1, G2), the kinematic space at its\nbest k (each of W, D, K); the peri-movement space at the same dimensionality.\n\"\"\")\n\ncode(r\"\"\"\nrng7d = np.random.default_rng(7004)\nNDRAW = 100\n\ndef pd_dir(S_, x, idx):\n    Xd = np.column_stack([np.ones(len(idx)), S_[idx]])\n    b = np.linalg.lstsq(Xd, x[idx], rcond=None)[0][1:]\n    return b / np.linalg.norm(b)\n\ndef consistency(S_list, x, draws):\n    # S_list: one space per neuron-independent draw set; returns mean dot product over draws\n    return np.mean([pd_dir(S_list, x, i1) @ pd_dir(S_list, x, i2) for i1, i2 in draws])\n\nrows = []\nfor T in D:\n    X = D[T][\"X\"]\n    c = X.shape[1]\n    blocks = PERF[T][\"blocks\"]\n    peri_S = {n: S_ for n, S_ in mm.gram_leave_one_out_scores(blocks, KMAX)}\n    for S in (\"S1\", \"S2\"):\n        sel = np.where(SEL[T, S][\"prep\"])[0]\n        mc = MC[T, S]\n        comps = [(\"endpoints + max speed\", PERF[T][\"taskS\"][\"endpoints + max speed\"])]\n        comps += [(f\"segment directions ({g})\", PERF[T][\"taskS\"][f\"segment directions ({g})\"]) for g in (\"G1\", \"G2\")]\n        for K in (14, 12):\n            for k_, v in mc[\"kin\"].items():\n                kb = int(np.argmax(v[:K]) + 1)\n                comps.append((f\"kinematic {k_} K{1 if K == 14 else 2} (k={kb})\", PERF[T][\"kinS\"][k_][:, :kb]))\n        seen = {}\n        for name, Sc in comps:\n            key = (name.split(\" K\")[0], Sc.shape[1])\n            if key in seen:\n                rows.append((T, S, name, Sc.shape[1], *seen[key])); continue\n            k = Sc.shape[1]\n            cs, cp = [], []\n            for n in sel:\n                draws = [(rng7d.integers(0, c, 25), rng7d.integers(0, c, 25)) for _ in range(NDRAW)]\n                cs.append(consistency(Sc, X[n], draws))\n                cp.append(consistency(peri_S[n][:, :k], X[n], draws))\n            seen[key] = (len(sel), round(np.mean(cs), 3), round(np.mean(cp), 3), np.mean(cp) > np.mean(cs))\n            rows.append((T, S, name, k, *seen[key]))\ntab7d = pd.DataFrame(rows, columns=[\"trials\", \"tuning\", \"comparison space\", \"k\", \"neurons\", \"comparison consistency\",\n                                    \"peri consistency\", \"peri higher\"])\nprint(tab7d.to_string(index=False))\nprint(\"\\ncomparisons won by the peri-movement space, per trials x tuning:\")\nprint(tab7d.groupby([\"trials\", \"tuning\"])[\"peri higher\"].agg([\"sum\", \"count\"]).to_string())\n\"\"\", tags=[\"claim:fig7d-pd-consistency\"])\n\nmd(\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(\"\"\"\n## ap-location-no-effect-on-correlation (blocked) and fig7c-anterior-posterior-performance (blocked)\n\nBoth need each unit's anterior-posterior location. The electrodes table has no coordinates (x, y, z are NaN),\nand its array labels cannot be used: every unit's electrode reference points into the 96 PMd rows, so by the\nfile every unit is in PMd, while the dataset describes two arrays. The unit ids carry a leading digit (1 or 2)\nthat splits the units into 92 and 90, which looks like an array number, but nothing in the dataset says so or\nsays which array is which. As a variant that decides nothing, the regression of tuning correlation on that\ndigit is shown; its p-value does not depend on which digit is anterior.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor (T, S), v in R.items():\n    if len(v[\"r\"]) < 3:\n        continue\n    dig = units.id_digit.values[v[\"ids\"]]\n    res = stats.pearsonr(dig, v[\"r\"])\n    rows.append((T, S, len(v[\"r\"]), int((dig == 1).sum()), int((dig == 2).sum()), round(res.statistic, 3), round(res.pvalue, 3)))\nprint(pd.DataFrame(rows, columns=[\"trials\", \"tuning\", \"neurons\", \"digit 1\", \"digit 2\", \"r (sign undetermined)\", \"p\"]).to_string(index=False))\n\"\"\")\n\nmd(\"\"\"\n## fig8-model-weak-correlation\n\n> In a simulated linear dynamical system (a harmonic oscillator held at 25 random initial states, then released),\n> the preparatory to peri-movement tuning correlation of a unit is low (0.08) ...\n\nW as printed in the Figure 8 legend (the exact rotation as a variant); initial states uniform in [-1, 1]² (I1)\nor standard normal (I2); the gray interval as the first 360 (J1) or 180 (J2) steps after release. 1000 draws of\n25 states. Reproduced when 0.08 lies within the central 95% of the spread under one combination.\n\"\"\")\n\ncode(r\"\"\"\nrng8a = np.random.default_rng(8001)\nrows = []\nfor I in (\"I1\", \"I2\"):\n    for J, nst in ((\"J1\", 360), (\"J2\", 180)):\n        for Wn, exact in ((\"printed W\", False), (\"exact rotation\", True)):\n            rs_ = []\n            for _ in range(1000):\n                x0 = rng8a.uniform(-1, 1, (25, 2)) if I == \"I1\" else rng8a.standard_normal((25, 2))\n                traj = mm.oscillator(x0, nst, exact)\n                rs_.append(np.corrcoef(x0[:, 0], traj[:, 0].mean(1))[0, 1])\n            lo, hi = np.percentile(rs_, [2.5, 97.5])\n            rows.append((I, J, Wn, round(np.median(rs_), 3), round(lo, 3), round(hi, 3), lo <= 0.08 <= hi))\nprint(pd.DataFrame(rows, columns=[\"initial states\", \"interval\", \"W\", \"median r\", \"2.5%\", \"97.5%\", \"0.08 inside\"]).to_string(index=False))\n\"\"\", tags=[\"claim:fig8-model-weak-correlation\"])\n\nmd(\"\"\"\n**Result: ...**\n\"\"\")\n\nmd(\"\"\"\n## fig8-model-pd-perfect\n\n> In the same simulated system, preparatory tuning is captured perfectly by a PD in the two-dimensional space\n> found by PCA of the peri-movement activity.\n\nPCA of the 25 x 2t matrix of both units' activity over the interval, k = 2; unit 1's initial rates fitted by M7\nwithout and with cross-validation. Reproduced when R² and leave-one-out performance exceed 0.999 under every\nreading; 100 draws of 25 states per reading, the smallest values shown.\n\"\"\")\n\ncode(r\"\"\"\nrng8b = np.random.default_rng(8002)\nrows = []\nfor I in (\"I1\", \"I2\"):\n    for J, nst in ((\"J1\", 360), (\"J2\", 180)):\n        for Wn, exact in ((\"printed W\", False), (\"exact rotation\", True)):\n            r2s, loos = [], []\n            for _ in range(100):\n                x0 = rng8b.uniform(-1, 1, (25, 2)) if I == \"I1\" else rng8b.standard_normal((25, 2))\n                traj = mm.oscillator(x0, nst, exact)\n                Tm = traj.reshape(25, -1)                 # both units over the interval\n                S_ = mm.pca_scores(Tm, 2)\n                y = x0[:, [0]]\n                Xd = np.column_stack([np.ones(25), S_])\n                fit = Xd @ np.linalg.lstsq(Xd, y, rcond=None)[0]\n                r2s.append(1 - ((y - fit) ** 2).sum() / ((y - y.mean()) ** 2).sum())\n                loos.append(mm.loo_performance(S_, y)[0])\n            rows.append((I, J, Wn, min(r2s), min(loos), min(r2s) > 0.999 and min(loos) > 0.999))\nprint(pd.DataFrame(rows, columns=[\"initial states\", \"interval\", \"W\", \"smallest R2\", \"smallest LOO performance\", \"both > 0.999\"]).to_string(index=False))\n\"\"\", tags=[\"claim:fig8-model-pd-perfect\"])\n\nmd(\"\"\"\n**Result: ...**\n\"\"\")\n\ncode(r\"\"\"\nprint(\"notebook runtime: %.1f min\" % ((time.time() - T_START) / 60))\n\"\"\")\n\nmd(\"\"\"\n## Summary\n\n(filled in after the run)\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/000128-churchland-2010/reproduce_churchland_2010.ipynb\")\nprint(len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build_nb.py').read()
a=s.index("def spliced(T):"); b=s.index("curves = {}")
new='''def spliced(T):
    G, M, rt_c = D[T]["G"], D[T]["M"], D[T]["rt"]
    out = np.zeros(G.shape[:2] + (len(tau),))
    mv_part = M[:, :, np.searchsorted(tm, tau)]
    for c in range(G.shape[1]):
        go_end = 100 - rt_c[c]                   # end of the go-locked part, ms from onset
        g = np.array([np.interp(tau + rt_c[c], tg, G[u, c]) for u in range(G.shape[0])])
        m = mv_part[:, c]
        if go_end >= -300:     # overlap from -300 ms to go_end: fade linearly from go-locked to movement-locked
            w = np.clip((tau + 300) / max(go_end + 300, 1e-9), 0, 1)
            out[:, c] = (1 - w) * g + w * m
        else:                  # gap from go_end to -300 ms: join the two ends linearly
            g_end = G[:, c, np.searchsorted(tg, 100)][:, None]
            m_start = M[:, c, np.searchsorted(tm, -300)][:, None]
            w = np.clip((tau - go_end) / (-300 - go_end), 0, 1)
            out[:, c] = np.where(tau <= go_end, g, np.where(tau >= -300, m, (1 - w) * g_end + w * m_start))
    return out

'''
s=s[:a]+new+s[b:]
open('build_nb.py','w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && uv pip install -q nbformat nbconvert ipykernel && python build_nb.py
```

```
65
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010 && . $TMPDIR/env/bin/activate && time jupyter nbconvert --to notebook --execute reproduce_churchland_2010.ipynb --output $TMPDIR/out.ipynb --ExecutePreprocessor.timeout=3600 2>&1 | tail -20
```

```
[NbConvertApp] Converting notebook reproduce_churchland_2010.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 234133 bytes to /tmp/claude-1001/out.ipynb

real	2m28.607s
user	2m20.981s
sys	0m2.013s
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read('out.ipynb',4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    for o in c.get('outputs',[]):
        if o.output_type=='stream': print(f"--- cell {i}\n"+o.text[:6000])
        elif o.output_type=='error': print("ERR",i,o.ename,o.evalue)
EOF
```

```
--- cell 1
dandiset 000128 version 0.220113.0400

--- cell 3
title: MC_Maze: macaque primary motor and dorsal premotor cortex spiking activity during delayed reaching
related publications in metadata: ['10.1016/j.neuron.2010.09.015', '10.1038/nature11129']
  sub-Jenkins/sub-Jenkins_ses-full_desc-test_ecephys.nwb: 3.4 MB, blob faf1f307-a06d-464c-8700-a659ab94ce2a
  sub-Jenkins/sub-Jenkins_ses-full_desc-train_behavior+ecephys.nwb: 690.6 MB, blob df3e3f73-50ab-42b4-8827-82664ddd474a
draft holds the same assets with the same blobs: True

--- cell 3
subject: Jenkins Macaca mulatta | session: 2009-09-25 | related publication in file: ['https://doi.org/10.1016/j.neuron.2010.09.015']
train file trials columns: ['start_time', 'stop_time', 'trial_type', 'trial_version', 'maze_id', 'success', 'target_on_time', 'go_cue_time', 'move_onset_time', 'rt', 'delay', 'num_targets', 'target_pos', 'num_barriers', 'barrier_pos', 'active_target', 'split', 'target_x', 'target_y', 'condition']
units columns: ('heldout', 'spike_times', 'obs_intervals', 'electrodes')
electrodes columns: ['x', 'y', 'z', 'imp', 'location', 'filtering', 'group', 'group_name']
behaviour: ['cursor_pos', 'eye_pos', 'hand_pos', 'hand_vel']

--- cell 4
=== trials (train file) ===
trials: 2295 | split: {'train': 1721, 'val': 574} | success all True: True
[... 404 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build_nb.py').read()
def rep(old,new):
    global s
    assert s.count(old)==1, old[:60]
    s=s.replace(old,new)
rep("""**Result: reproduced.** Under T1 with S1 (24 neurons) the mean Pearson r is 0.117 and the mean Spearman r
0.102, both within tolerance, and all three tests give p < 0.05 (0.011 to 0.015). Under T2 with S1 (17
neurons) the means are 0.051 and 0.072 and no test is significant. S2 selects no neuron under either
trial reading, so it gives no result.""",
"""**Result: not reproduced.** No combination puts the means within tolerance or gives p < 0.05. Under T1 with S1
(18 neurons) the mean Pearson r is 0.025 and the mean Spearman r 0.054 (p 0.64 to 0.67); under T2 with S1
(17 neurons) they are 0.051 and 0.072 (p 0.42 to 0.61). The means are positive but less than half the
paper's 0.13 and 0.11. S2 selects no neuron under either trial reading, so it gives no result.""")
rep("""**Result: reproduced.** Under both trial readings with S1, at least one neuron keeps its tuning (r ≥ 0.72; 1 neuron under
T1, 1 under T2) and most do not (share below 0.72 of 0.958 and 0.941). S2 selects no neuron.""",
"""**Result: blocked (methods_underspecified).** The trial readings disagree. Under T2 with S1, one of 17 neurons keeps its
tuning (r = 0.765) and 94.1% have r < 0.72, so the claim holds. Under T1 with S1 no neuron reaches 0.72 (the
largest r is 0.411), so it does not. S2 selects no neuron. A question on T1 and T2 has been asked.""")
rep("""**Result: reproduced.** Under T1 and T2 with S1, the dip test finds no departure from unimodality (p of 0.85
and 0.95), and most neurons have |r| < 0.5 (22 of 24 and 16 of 17). No neuron has |r| ≥ 0.8.""",
"""**Result: reproduced.** Under T1 and T2 with S1 the dip test finds no departure from unimodality (dip p 0.596 and
0.683), and most neurons have |r| < 0.5 (18 of 18 and 16 of 17), so U1 and U2 both hold. No neuron has
|r| ≥ 0.8. The median r is 0.026 and 0.013. S2 selects no neuron.""")
results=[
"""**Result: reproduced.** Under every reading that selects neurons (T1 and T2 with S1, rates A1 and A2) the mean
correlation falls from 0.70 to 0.76 at -400 ms and 0.55 to 0.61 at -200 ms to between -0.006 and 0.012 at
movement onset, where no test finds it above zero (smallest p 0.854). Between 75% and 82% of the drop from
-400 ms to onset comes after -200 ms.""",
"""**Result: reproduced.** The separation between the strongest and weakest preparatory conditions is positive in the
preparatory epoch (0.207 to 0.346 of the maximum rate) and falls at movement onset to 0.225 to 0.308 of it.
R1 (below a half) holds under every reading; R2 (below a quarter) holds with normalisation (a), ratios 0.225
and 0.240, but not with (b), ratios 0.308 and 0.274. The claim needs one of R1 and R2.""",
"""**Result: not reproduced.** No reading gives 7 to 11 components. With the prep-tuned neurons under S1, 90% of the
variance needs 18 (T1) and 15 (T2) components; with all 182 units, 20 and 18; with the 6 units S2 selects, 4.""",
"""**Result: blocked (methods_underspecified).** The trial readings disagree. Under T2 the peri-movement space has the
best performance in every combination (with S1, 0.518 at k = 14 against 0.424 for the best kinematic space
and 0.412 for the kitchen-sink space; 24 of 24 combinations, and also with S2). Under T1 with S1 it wins
none: its best is 0.281 (k = 5), below the kinematic space (0.295) and the kitchen-sink space (0.313); with S2
it wins 12 of 24. A question on T1 and T2 has been asked.""",
"""**Result: blocked (methods_underspecified).** The readings disagree. The 3-D endpoints + max speed space is below the
3-D peri-movement space under every reading (for example 0.168 against 0.271 under T2 with S1). Under T2
with S1 the peri-movement space wins 21 of 22 comparisons (K1) and 19 of 20 (K2), so L1 and L2 hold. Under
T2 with S2 it wins 20 or 21 of 22, so L2 holds but L1 does not in every combination. Under T1 it wins 11 or 12
of 20 to 22, and neither holds.""",
"""**Result: blocked (methods_underspecified).** The trial readings disagree. Under T1 performance rises from k = 1 to a
best at k = 5 (S1, 0.281) or 10 (S2, 0.645) and falls at k = 14 (-0.287 and 0.393), as the claim says. Under T2 it
rises through k = 14 (S1, 0.140 to 0.518; S2, 0.339 to 0.821) with no decline, so the best k is above 10.""",
"""**Result: blocked (methods_underspecified).** The trial readings disagree. Under T2 the shuffled space is below the
unshuffled one at every k, and its best (0.224 with S1, 0.467 with S2) is below the best kinematic space
(0.421 or more, and 0.644 or more), so H1 and H2 hold. Under T1 the unshuffled space falls below zero at
k ≥ 10 while the shuffled one stays positive (best 0.090 with S1), so H1 fails, and with it H2.""",
"""**Result: reproduced.** Under reading J2, the J-array ratio of performance with the window starting at onset to that
starting at -150 ms is within 0.97 ± 0.097 under every reading: 0.918 (T1, S1), 0.904 (T1, S2), 0.957 to 0.959
(T2, S1) and 0.968 to 0.972 (T2, S2). The 94% of monkeys A and B cannot be tested.""",
"""**Result: reproduced.** The PD is more stable in the peri-movement space in all 11 comparisons under every reading
(for example, under T2 with S1, 0.742 against 0.547 for endpoints + max speed, 0.642 and 0.647 against 0.492
and 0.456 for segment directions, and 0.194 to 0.314 against 0.172 to 0.229 for the kinematic spaces).""",
"""**Result: reproduced.** Over 1000 draws of 25 initial states, the correlation spreads around zero (medians -0.041 to
0.019) with a central 95% of about -0.43 to 0.43 under every reading, and 0.08 lies inside it in all eight.
The second part of the statement (one preparatory rate leading to opposing patterns) is not tested by the
criterion.""",
"""**Result: reproduced.** Under all eight readings the smallest R² and leave-one-out performance over 100 draws are 1.0
to the printed precision, above 0.999.""",
]
for r in results:
    rep_old="""md(\"\"\"
**Result: ...**
\"\"\")"""
    i=s.index(rep_old); s=s[:i]+'md("""\n'+r+'\n""")'+s[i+len(rep_old):]
rep("""md(\"\"\"
**Result: ...** (filled in after the run)
\"\"\")""","XX")
s=s.replace("XX",'md("""\n'+results[0]+'\n""")',1) if False else s
open('build_nb.py','w').write(s)
print(s.count("Result: ..."))
EOF
```

```
Exit code 1
Traceback (most recent call last):
  File "<stdin>", line 69, in <module>
ValueError: substring not found
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "Result: \.\.\." build_nb.py | head; grep -c "Result: reproduced.\*\* Under every reading that selects" build_nb.py
```

```
513:**Result: ...** (filled in after the run)
564:**Result: ...**
591:**Result: ...**
718:**Result: ...**
761:**Result: ...**
786:**Result: ...**
832:**Result: ...**
857:**Result: ...**
921:**Result: ...**
974:**Result: ...**
0
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
src=open('/dev/stdin').read() if False else None
EOF
sed -n '1,200p' /dev/null; python - <<'EOF'
import re
code=open('/tmp/claude-1001/fix.py').read() if False else None
EOF
echo ok
```

```
ok
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/fix.py",
 "content": "s = open('/tmp/claude-1001/build_nb.py').read()\ndef rep(old, new):\n    global s\n    assert s.count(old) == 1, old[:60]\n    s = s.replace(old, new)\n\nrep(\"\"\"**Result: reproduced.** Under T1 with S1 (24 neurons) the mean Pearson r is 0.117 and the mean Spearman r\n0.102, both within tolerance, and all three tests give p < 0.05 (0.011 to 0.015). Under T2 with S1 (17\nneurons) the means are 0.051 and 0.072 and no test is significant. S2 selects no neuron under either\ntrial reading, so it gives no result.\"\"\",\n\"\"\"**Result: not reproduced.** No combination puts the means within tolerance or gives p < 0.05. Under T1 with S1\n(18 neurons) the mean Pearson r is 0.025 and the mean Spearman r 0.054 (p 0.64 to 0.67); under T2 with S1\n(17 neurons) they are 0.051 and 0.072 (p 0.42 to 0.61). The means are positive but less than half the\npaper's 0.13 and 0.11. S2 selects no neuron under either trial reading, so it gives no result.\"\"\")\nrep(\"\"\"**Result: reproduced.** Under both trial readings with S1, at least one neuron keeps its tuning (r ≥ 0.72; 1 neuron under\nT1, 1 under T2) and most do not (share below 0.72 of 0.958 and 0.941). S2 selects no neuron.\"\"\",\n\"\"\"**Result: blocked (methods_underspecified).** The trial readings disagree. Under T2 with S1, one of 17 neurons keeps its\ntuning (r = 0.765) and 94.1% have r < 0.72, so the claim holds. Under T1 with S1 no neuron reaches 0.72 (the\nlargest r is 0.411), so it does not. S2 selects no neuron. A question on T1 and T2 has been asked.\"\"\")\nrep(\"\"\"**Result: reproduced.** Under T1 and T2 with S1, the dip test finds no departure from unimodality (p of 0.85\nand 0.95), and most neurons have |r| < 0.5 (22 of 24 and 16 of 17). No neuron has |r| ≥ 0.8.\"\"\",\n\"\"\"**Result: reproduced.** Under T1 and T2 with S1 the dip test finds no departure from unimodality (dip p 0.596 and\n0.683), and most neurons have |r| < 0.5 (18 of 18 and 16 of 17), so U1 and U2 both hold. No neuron has\n|r| ≥ 0.8. The median r is 0.026 and 0.013. S2 selects no neuron.\"\"\")\nresults = [\n\"\"\"**Result: reproduced.** Under every reading that selects neurons (T1 and T2 with S1, rates A1 and A2) the mean\ncorrelation falls from 0.70 to 0.76 at -400 ms and 0.55 to 0.61 at -200 ms to between -0.006 and 0.012 at\nmovement onset, where no test finds it above zero (smallest p 0.854). Between 75% and 82% of the drop from\n-400 ms to onset comes after -200 ms.\"\"\",\n\"\"\"**Result: reproduced.** The separation between the strongest and weakest preparatory conditions is positive in the\npreparatory epoch (0.207 to 0.346 of the maximum rate) and falls at movement onset to 0.225 to 0.308 of it.\nR1 (below a half) holds under every reading; R2 (below a quarter) holds with normalisation (a), ratios 0.225\nand 0.240, but not with (b), ratios 0.308 and 0.274. The claim needs one of R1 and R2.\"\"\",\n\"\"\"**Result: not reproduced.** No reading gives 7 to 11 components. With the prep-tuned neurons under S1, 90% of the\nvariance needs 18 (T1) and 15 (T2) components; with all 182 units, 20 and 18; with the 6 units S2 selects, 4.\"\"\",\n\"\"\"**Result: blocked (methods_underspecified).** The trial readings disagree. Under T2 the peri-movement space has the\nbest performance in every combination (with S1, 0.518 at k = 14 against 0.424 for the best kinematic space\nand 0.412 for the kitchen-sink space; 24 of 24 combinations, and also with S2). Under T1 with S1 it wins\nnone: its best is 0.281 (k = 5), below the kinematic space (0.295) and the kitchen-sink space (0.313); with S2\nit wins 12 of 24. A question on T1 and T2 has been asked.\"\"\",\n\"\"\"**Result: blocked (methods_underspecified).** The readings disagree. The 3-D endpoints + max speed space is below the\n3-D peri-movement space under every reading (for example 0.168 against 0.271 under T2 with S1). Under T2\nwith S1 the peri-movement space wins 21 of 22 comparisons (K1) and 19 of 20 (K2), so L1 and L2 hold. Under\nT2 with S2 it wins 20 or 21 of 22, so L2 holds but L1 does not in every combination. Under T1 it wins 11 or 12\nof 20 to 22, and neither holds.\"\"\",\n\"\"\"**Result: blocked (methods_underspecified).** The trial readings disagree. Under T1 performance rises from k = 1 to a\nbest at k = 5 (S1, 0.281) or 10 (S2, 0.645) and falls at k = 14 (-0.287 and 0.393), as the claim says. Under T2 it\nrises through k = 14 (S1, 0.140 to 0.518; S2, 0.339 to 0.821) with no decline, so the best k is above 10.\"\"\",\n\"\"\"**Result: blocked (methods_underspecified).** The trial readings disagree. Under T2 the shuffled space is below the\nunshuffled one at every k, and its best (0.224 with S1, 0.467 with S2) is below the best kinematic space\n(0.421 or more, and 0.644 or more), so H1 and H2 hold. Under T1 the unshuffled space falls below zero at\nk ≥ 10 while the shuffled one stays positive (best 0.090 with S1), so H1 fails, and with it H2.\"\"\",\n\"\"\"**Result: reproduced.** Under reading J2, the J-array ratio of performance with the window starting at onset to that\nstarting at -150 ms is within 0.97 ± 0.097 under every reading: 0.918 (T1, S1), 0.904 (T1, S2), 0.957 to 0.959\n(T2, S1) and 0.968 to 0.972 (T2, S2). The 94% of monkeys A and B cannot be tested.\"\"\",\n\"\"\"**Result: reproduced.** The PD is more stable in the peri-movement space in all 11 comparisons under every reading\n(for example, under T2 with S1, 0.742 against 0.547 for endpoints + max speed, 0.642 and 0.647 against 0.492\nand 0.456 for segment directions, and 0.194 to 0.314 against 0.172 to 0.229 for the kinematic spaces).\"\"\",\n\"\"\"**Result: reproduced.** Over 1000 draws of 25 initial states, the correlation spreads around zero (medians -0.041 to\n0.019) with a central 95% of about -0.43 to 0.43 under every reading, and 0.08 lies inside it in all eight.\nThe second part of the statement (one preparatory rate leading to opposing patterns) is not tested by the\ncriterion.\"\"\",\n\"\"\"**Result: reproduced.** Under all eight readings the smallest R² and leave-one-out performance over 100 draws are 1.0\nto the printed precision, above 0.999.\"\"\",\n]\nrep(\"**Result: ...** (filled in after the run)\", results[0])\nfor r in results[1:]:\n    i = s.index(\"**Result: ...**\")\n    s = s[:i] + r + s[i + len(\"**Result: ...**\"):]\nassert \"Result: ...\" not in s\nopen('/tmp/claude-1001/build_nb.py', 'w').write(s)\nprint(\"done\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/fix.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python fix.py
```

```
done
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('build_nb.py').read()
a="T2 with S2 it wins 20 or 21 of 22, so L2 holds but L1 does not in every combination."
assert a in s
s=s.replace(a,"T2 with S2 it wins 20 or 21 of 22 (K1) and 18 or 19 of 20 (K2), so L2 holds but L1 does not in every combination.")
a="(0.421 or more, and 0.644 or more)"; assert a in s
s=s.replace(a,"(0.414 or more, and 0.644 or more)")
summary='''md("""
## Summary

| Claim | Outcome |
|---|---|
| recordings-jarray | partially reproduced: 108 conditions and 2295 trials match; 182 units against 146 |
| recordings-single-electrode | blocked: data_missing |
| fig2b-example-concordant-tuning | blocked: data_missing |
| fig2ce-example-opposing-tuning | blocked: data_missing |
| fig3-maze-most-not-maintained | blocked: methods_underspecified (holds under T2, not under T1) |
| fig4d-mean-correlation-jarray | not reproduced: mean r 0.025 to 0.051, p > 0.4 |
| fig4abc-mean-correlation-single-electrode | blocked: data_missing |
| fig4-no-separate-populations | reproduced |
| fig4e-correlation-time-course | reproduced |
| suppfig1-population-averages | reproduced |
| fig6-peri-movement-space-best | blocked: methods_underspecified (holds under T2, not under T1) |
| fig6-each-dimensionality | blocked: methods_underspecified (readings disagree) |
| fig6-performance-vs-dimensionality | blocked: methods_underspecified (holds under T1, not under T2) |
| prep-dimensionality | not reproduced: 15 to 20 components, not 7 to 10 |
| fig6e-summary-across-datasets | blocked: data_missing |
| fig7a-shuffled-space-poor | blocked: methods_underspecified (holds under T2, not under T1) |
| fig7b-window-start-slide | reproduced (J-array ratio only) |
| ap-location-no-effect-on-correlation | blocked: metadata_insufficient |
| fig7c-anterior-posterior-performance | blocked: metadata_insufficient |
| fig7d-pd-consistency | reproduced |
| fig8-model-weak-correlation | reproduced |
| fig8-model-pd-perfect | reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the
differences from the paper's method.

**How the analysis differs from the paper's.** Only the J-array dataset is in the archive; the speed task,
the single-electrode maze recordings and EMG are not. The session here has 182 units where the paper's J-array
dataset has 146, and nothing tells which of them the paper used, or whether the session is the same one. The
paper's proto-trial selection is not defined; under reading T1 it keeps 74% of trials and empties two
conditions, under T2 91% (the paper says typically about 90%), and five claims change outcome between them
(a question has been asked). Reading S2 of the tuning measure selects no unit for the correlation claims and 6
for the PD claims. Acceleration is the time derivative of the dataset's hand velocity. Movement onset is the
dataset's. All methods follow the claims file; the details it leaves open are run under every reading.

**What was found about the dataset.** Every unit's electrode reference points into the PMd rows of the
electrodes table, so by the file all 182 units are in PMd, while the dataset describes two arrays; the unit
ids' leading digit (92 and 90 units) may be the array, undocumented. The electrodes have no coordinates, so no
anterior-posterior location. The dataset holds 182 units against the paper's 146, with no record of the
paper's unit or trial selection. 574 trials sit in a test file as 0.7 s segments with no condition labels or
behaviour and only the 137 held-in units. 14 trials have a negative delay (down to -3 ms). The behaviour
series' timestamps run on a 1 ms grid within trials with gaps between trials, and the spike times only cover
the trials; both share the trial table's clock as far as the checks show (hand speed rises at the marked
movement onset; reach direction is decoded from spikes after target onset, 0.661, and not before, 0.166).
""")
'''
i=s.index('md("""\n## Summary'); j=s.index('nb = nbf.v4.new_notebook()')
s=s[:i]+summary+"\n"+s[j:]
open('build_nb.py','w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && python build_nb.py
```

```
65
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/\*\*How the analysis differs from the paper.s.\*\*/How the analysis differs from the paper'"'"'s./; s/\*\*What was found about the dataset.\*\*/What was found about the dataset./' build_nb.py && grep -n "How the analysis\|What was found" build_nb.py && . env/bin/activate && python build_nb.py; cat entries/001453-fouke-2025/README.md; ls schemas
```

```
1078:How the analysis differs from the paper's. Only the J-array dataset is in the archive; the speed task,
1087:What was found about the dataset. Every unit's electrode reference points into the PMd rows of the
65
# Fouke, He, Loring & Naumann (2025) from dandiset 001453

Tests the findings of [Fouke et al. (2025)](https://doi.org/10.1016/j.cub.2025.04.027) that can be
tested on [DANDI:001453](https://dandiarchive.org/dandiset/001453/0.250518.1950), which holds the
freely swimming tracking of 25 zebrafish and 12 *Danionella cerebrum* larvae (Figure 1 and Figure
S1). The imaging and head-fixed tail tracking of Figures 2 to 4 are not in it.

| Claim | Outcome |
|---|---|
| The stimulus codes can be linked to the paper's stimuli through its code | Reproduced |
| DC swim faster than ZF, over all stimulus codes | Reproduced |
| Median speed over whole-field stimuli, DC 9.8 and ZF 6.4 mm/s | Reproduced |
| ZF are faster to forward motion than to a static grating (8.8 against 5.0 mm/s) | Reproduced |
| DC do not modulate speed with stimulus direction | Not reproduced |
| DC are faster than ZF for oblique stimuli | Reproduced |
| Both species turn in the direction of motion | Partially reproduced |
| ZF have higher angular acceleration than DC | Not reproduced |
[... 21 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/000128-churchland-2010 && cat > entry.yaml <<'EOF'
schema_version: 1
name: 000128-churchland-2010
type: reproduction
title: Preparatory and peri-movement tuning in motor and premotor cortex (Churchland et al. 2010)
description: Tests the findings of Churchland, Cunningham, Kaufman, Ryu and Shenoy (2010) on dandiset
  000128 (MC_Maze), which holds the J-array session of monkey Jenkins on the maze task, recorded with two
  Utah arrays. It tests the correlation between preparatory and peri-movement tuning, its time course,
  the dimensionality of preparatory activity, the performance and stability of preferred directions in
  the peri-movement, kinematic and task spaces, and the paper's oscillator model. The speed task, the
  single-electrode recordings and EMG are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_churchland_2010.ipynb
  title: Reproducing Churchland et al. (2010) from dandiset 000128
  runtime_minutes: 3
helpers:
- mcmaze.py
related:
- id: dandi:000128/0.220113.0400
  relation: uses_data
- id: doi:10.1016/j.neuron.2010.09.015
  relation: reproduces
EOF
printf "diptest\nh5py\nmatplotlib\nnumpy\npandas\npynwb\nremfile\nrequests\nscikit-learn\nscipy\n" > requirements.in
cat > README.md <<'EOF'
# Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010) from dandiset 000128

Tests the findings of [Churchland et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.015) that can
be tested on [DANDI:000128](https://dandiarchive.org/dandiset/000128/0.220113.0400) (MC_Maze), which
holds the paper's J-array dataset: one session of monkey Jenkins on the maze task, 108 conditions,
recorded with two 96-electrode arrays. The speed task (monkeys A and B), the single-electrode maze
recordings (monkey J) and EMG are not in it.

| Claim | Outcome |
|---|---|
| The J-array dataset: 146 units, 108 conditions, about 2166 trials | Partially reproduced (182 units) |
| Mean correlation of preparatory and peri-movement tuning 0.13 (J-array) | Not reproduced |
| No separate concordant and opposing populations | Reproduced |
| The correlation declines from about 200 ms before movement onset to near zero | Reproduced |
| Population averages lose their relation to preparatory tuning by movement onset | Reproduced |
| 7 to 10 dimensions capture 90% of preparatory variance | Not reproduced |
| Starting the peri-movement window at onset keeps about 97% of PD performance | Reproduced |
| The PD is most stable in the peri-movement space | Reproduced |
| The oscillator model: low tuning correlation, PD captures tuning perfectly | Reproduced (2 claims) |
| Most maze neurons do not keep their tuning; the peri-movement space performs best; performance against dimensionality; the shuffled control | Blocked: methods underspecified (5 claims; the trial selection readings disagree, a question is asked) |
| Anterior against posterior sites | Blocked: metadata insufficient (2 claims) |
| Speed task, single-electrode and EMG data | Blocked: data missing (5 claims) |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The attempt record, with the reasons and the differences from the paper's method, is
[`attempts/000128-churchland-2010-01.yaml`](../../attempts/000128-churchland-2010-01.yaml).

- `reproduce_churchland_2010.ipynb`: the analysis. It takes about three minutes, most of it computing
  smoothed firing rates.
- `mcmaze.py`: streaming the files, the trial selection, condition-mean firing rates, the PD fits and
  the kinematic and task spaces. Other notebooks on this dandiset can import it.
EOF
cd ../.. && python tools/entry.py lock entries/000128-churchland-2010 2>&1 | tail -5
```

```
wrote entries/000128-churchland-2010/requirements.lock.txt
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=1)[:6000])"
```

```
{
 "$schema": "https://json-schema.org/draft/2020-12/schema",
 "title": "One attempt at reproducing the claims of a target",
 "description": "Draft. To be revised after the pilot. An attempt is recorded whether or not it produced a working notebook.",
 "type": "object",
 "additionalProperties": false,
 "required": [
  "schema_version",
  "id",
  "dataset",
  "paper",
  "date",
  "provenance",
  "outcomes"
 ],
 "properties": {
  "schema_version": {
   "const": 2
  },
  "id": {
[... 215 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000128-churchland-2010-01.yaml",
 "content": "schema_version: 2\nid: 000128-churchland-2010-01\ndataset:\n  archive: dandi\n  id: \"000128\"\n  version: 0.220113.0400\n  doi: 10.48324/dandi.000128/0.220113.0400\npaper: doi:10.1016/j.neuron.2010.09.015\ndate: 2026-10-22\nentry: 000128-churchland-2010\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code (GitHub Actions)\n    model: claude-opus-5-5\n    protocol: pilot-10\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/reproduction-registry/actions/runs/39810757909\noutcomes:\n- claim: recordings-jarray\n  outcome: partially_reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:recordings-jarray\n  measured:\n  - 182\n  - 108\n  - 2295\n  notes: The dataset has 108 conditions (36 mazes in 3 versions) and 2295 successful trials with\n    condition labels, within tolerance of 2166 under reading (a); every unit is observed on every\n    trial. Under reading (b) the trials kept by M1 are 1452 (T1) and 1786 (T2), both outside. The\n    unit count is 182 (137 held in, 45 held out), outside 146 plus or minus 14.6. A further 574\n    successful trials are in the test file as 0.7 s segments without labels (2869 in all, outside\n    the tolerance).\n  deviations:\n  - Nothing in the dataset says which units or trials the paper used, or whether this session\n    (2009-09-25) is the one the paper analysed.\n- claim: recordings-single-electrode\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The dandiset holds only the array session of monkey Jenkins. No speed-task data (monkeys A\n    and B) and no single-electrode maze recordings are in it, and the paper names no other archive\n    for them.\n- claim: fig2b-example-concordant-tuning\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the speed task, which is not in the dandiset.\n- claim: fig2ce-example-opposing-tuning\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the speed task, which is not in the dandiset.\n- claim: fig3-maze-most-not-maintained\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig3-maze-most-not-maintained\n  notes: The trial readings disagree. Under T2 with S1, 1 of 17 neurons has r of 0.72 or more (0.765)\n    and 94.1% have r below 0.72, so the claim holds. Under T1 with S1 no neuron of 18 reaches 0.72\n    (largest r 0.411), so it does not. S2 selects no neuron under either. A question on the\n    proto-trial readings is in questions/000128.yaml.\n  deviations:\n  - Under T1 two conditions keep no trial and are left out (106 conditions).\n- claim: fig4d-mean-correlation-jarray\n  outcome: not_reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig4d-mean-correlation-jarray\n  measured:\n  - 0.025\n  - 0.054\n  notes: No combination of readings puts the means within tolerance or gives p below 0.05. T1 with\n    S1, 18 neurons, mean Pearson r 0.025, mean Spearman r 0.054, p 0.64 to 0.67 (P1 to P3). T2 with\n    S1, 17 neurons, 0.051 and 0.072, p 0.42 to 0.61. S2 (SD over conditions above 5 spikes/s) selects\n    6 units with preparatory tuning and none that also pass the peri-movement rule, so it gives no\n    result. The means are positive but below half the paper's 0.13 and 0.11.\n  deviations:\n  - The dataset has 182 units, not the paper's 146, and the paper's unit selection is not\n    recorded; the selected neurons may differ from the paper's.\n  - Under T1 two conditions keep no trial and are left out (106 conditions).\n- claim: fig4abc-mean-correlation-single-electrode\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The single-electrode datasets of monkeys A, B and J are not in the dandiset.\n- claim: fig4-no-separate-populations\n  outcome: reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig4-no-separate-populations\n  notes: J-array only. Under T1 and T2 with S1 the dip statistic is 0.073 and 0.071 (p 0.596 and\n    0.683), so U1 holds, and 18 of 18 and 16 of 17 neurons have |r| below 0.5, so U2 holds. No neuron\n    has |r| of 0.8 or more; median r 0.026 and 0.013. S2 selects no neuron. The panel B part of the\n    statement (monkey B) cannot be tested.\n- claim: fig4e-correlation-time-course\n  outcome: reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig4e-correlation-time-course\n  notes: Under T1 and T2 with S1 and rates A1 and A2, the mean correlation is 0.700 to 0.759 at -400\n    ms, 0.550 to 0.608 at -200 ms and -0.006 to 0.012 at movement onset, where no test is significant\n    (smallest p 0.854). 75% to 82% of the drop from -400 ms to onset comes after -200 ms. S2 selects\n    no neuron.\n  deviations:\n  - Under A2 the criterion's linear joining was implemented as a straight line between the last\n    go-locked value and the first movement-locked one where they leave a gap, and a linear fade from\n    one to the other where they overlap, with each condition's go cue placed at its mean reaction\n    time before onset. A1 and A2 differ only before -300 ms and give the same outcome.\n- claim: suppfig1-population-averages\n  outcome: reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:suppfig1-population-averages\n  notes: The strongest-minus-weakest separation is 0.207 to 0.346 of the maximum rate in the\n    preparatory epoch and 0.225 to 0.308 of that at movement onset. R1 holds under every reading; R2\n    holds with normalisation (a) (ratios 0.225, 0.240) and not with (b) (0.308, 0.274).\n  deviations:\n  - The claims file does not say over what the maximum rate is taken; readings (a) all conditions\n    and times of the go- and movement-locked averages and (b) the four chosen conditions were run,\n    and both give the outcome. Asked in questions/000128.yaml.\n- claim: fig6-peri-movement-space-best\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-peri-movement-space-best\n  notes: The trial readings disagree. Under T2 the peri-movement space is best in every combination\n    (S1, 83 neurons, best 0.518 at k = 14 against 0.424 for the best kinematic space and 0.412 for the\n    kitchen-sink space; 24 of 24 combinations of W, D, V and G, with K1 and K2, and with S2). Under\n    T1 with S1 (96 neurons) its best is 0.281 at k = 5, below the kinematic space (0.295) and the\n    kitchen-sink space (0.313), in 24 of 24 combinations; with S2 it wins 12 of 24. Under T1 the\n    peri-movement performance falls below zero at k of 10 or more; two conditions are empty and some\n    keep 1 or 2 trials.\n  deviations:\n  - J-array only; EMG is not recorded for it.\n  - Acceleration is the time derivative of the dataset's hand velocity.\n  - V1 (\"each component's maximum absolute value\") was run as the magnitudes (V1a) and as the signed\n    component at its largest magnitude (V1b); they do not change the outcome.\n- claim: fig6-each-dimensionality\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-each-dimensionality\n  notes: The 3-D endpoints + max speed space is below the 3-D peri-movement space under every reading\n    (0.131 to 0.360 against 0.207 to 0.463). Under T2 with S1 the peri-movement space wins 21 of 22\n    comparisons (K1) and 19 of 20 (K2), so L1 and L2 hold. Under T2 with S2 it wins 20 or 21 of 22\n    (K1) and 18 or 19 of 20 (K2), so L2 holds and L1 does not in every combination. Under T1 it wins\n    11 or 12, and neither holds.\n  deviations:\n  - J-array only.\n- claim: fig6-performance-vs-dimensionality\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-performance-vs-dimensionality\n  notes: The trial readings disagree. Under T1 performance rises from k = 1 (0.104 with S1) to its best\n    at k = 5 (0.281) and falls by k = 14 (-0.287); with S2 best at k = 10. Under T2 it rises through\n    k = 14 (S1 0.140 to 0.518, S2 0.339 to 0.821) with no decline, so the best k is above 10.\n  deviations:\n  - J-array only.\n- claim: prep-dimensionality\n  outcome: not_reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:prep-dimensionality\n  measured: 18\n  notes: 90% of the variance of the preparatory condition-mean matrix needs 18 (T1) and 15 (T2)\n    components with the neurons of N1 under S1 (96 and 83), 20 and 18 with all 182 units (N2), and 4\n    with the 6 units S2 selects. None is within 7 to 11. Trial-averaged rates from 1 to 27 trials per\n    condition carry noise that adds dimensions; the paper's procedure may differ in this.\n  deviations:\n  - J-array only.\n- claim: fig6e-summary-across-datasets\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs monkeys A, B and J (single electrodes) and EMG, none of which is in the dandiset.\n- claim: fig7a-shuffled-space-poor\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7a-shuffled-space-poor\n  notes: The trial readings disagree. Under T2 the shuffled space (10 shuffles) is below the\n    unshuffled one at every k and its best (0.224 with S1, 0.467 with S2) is below the best kinematic\n    space (0.414 or more, 0.644 or more), so H1 and H2 hold. Under T1 the unshuffled space falls below\n    zero at k of 10 or more while the shuffled one stays positive (best 0.090 with S1), so H1 fails.\n  deviations:\n  - J-array only; the paper averages over datasets.\n- claim: fig7b-window-start-slide\n  outcome: reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7b-window-start-slide\n  measured: 0.918\n  notes: Reading J2, the J-array ratio. With the window starting at onset, performance at the best k is\n    0.918 (T1, S1), 0.904 (T1, S2), 0.957 to 0.959 (T2, S1) and 0.968 to 0.972 (T2, S2) of that with\n    the window starting at -150 ms, all within 0.97 plus or minus 0.097. The 94% of monkeys A and B\n    and the single-electrode J value (J1) cannot be tested.\n  deviations:\n  - J-array only (reading J2).\n- claim: ap-location-no-effect-on-correlation\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: The electrodes table has no coordinates, so no anterior-posterior location. The criterion's\n    fallback, the array, is not usable either, as every unit's electrode reference points into the 96\n    PMd rows, so by the file all units are in PMd. The unit ids' leading digit (1 for 92 units, 2 for\n    90) looks like an array number, but nothing in the dataset documents it or which array is which.\n    As a variant that decides nothing, regressing tuning correlation on that digit gives r of\n    magnitude 0.384 (T1, p 0.115) and 0.432 (T2, p 0.084), not significant.\n- claim: fig7c-anterior-posterior-performance\n  outcome: blocked\n  blocked_by: metadata_insufficient\n  notes: Needs each unit's AP location or at least its array; see ap-location-no-effect-on-correlation.\n    Not run.\n- claim: fig7d-pd-consistency\n  outcome: reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7d-pd-consistency\n  notes: The peri-movement space has the higher mean PD consistency in all 11 comparisons under every\n    combination of T and S (for T2 with S1, 0.742 against 0.547 for endpoints + max speed, 0.642 and\n    0.647 against 0.492 and 0.456 for segment directions G1 and G2, and 0.194 to 0.314 against 0.172 to\n    0.229 for the kinematic spaces at their best k).\n  deviations:\n  - J-array only.\n- claim: fig8-model-weak-correlation\n  outcome: reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig8-model-weak-correlation\n  notes: Over 1000 draws of 25 initial states, the correlation has medians -0.041 to 0.019 and central\n    95% ranges of about -0.43 to 0.43 under the eight readings; 0.08 lies inside all of them. The\n    second part of the statement (a given preparatory rate leading to opposing patterns) is not tested\n    by the criterion.\n- claim: fig8-model-pd-perfect\n  outcome: reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig8-model-pd-perfect\n  measured: 1.0\n  notes: Under all eight readings the smallest R squared and leave-one-out performance over 100 draws\n    are 1.0 to the printed precision.\nfindings:\n- kind: metadata_error\n  statement: Every unit's electrode reference in the units table points into the first 96 rows of the\n    electrodes table, which are labelled PMd, so by the file all 182 units are in PMd. The dataset\n    describes two arrays, in M1 and PMd. The reference equals the unit id's channel digits minus one,\n    which suggests the array offset was dropped in conversion.\n- kind: metadata_insufficient\n  statement: The electrodes have no coordinates (x, y and z are NaN), and the leading digit of the unit\n    ids (1 or 2), which may be the array, is not documented. No unit can be placed on the\n    anterior-posterior axis or on an array.\n- kind: selection_undocumented\n  statement: The dataset holds 182 units where the paper reports 146 isolations for the J-array dataset,\n    and does not record which units or trials the paper used, or that this session is the paper's.\n- kind: other\n  statement: 574 of the session's successful trials are in the test file as 0.7 s segments around\n    movement onset, without condition labels or behaviour and with only the 137 held-in units, so they\n    cannot enter a condition-mean analysis. None duplicates a train trial.\n- kind: other\n  statement: 14 trials have a negative delay (as low as -3 ms), where the go cue precedes the recorded\n    target onset.\nEOF\n"
}
```

```
File created successfully at: attempts/000128-churchland-2010-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
sed -i '$ d' attempts/000128-churchland-2010-01.yaml && tail -2 attempts/000128-churchland-2010-01.yaml && cat questions/001754.yaml | head -30
```

```
statement: 14 trials have a negative delay (as low as -3 ms), where the go cue precedes the recorded
    target onset.
# Questions from attempt 001754-knierim-2000-03 (author, 2026-10-20) about the claims file
# claims/001754/10.1038-72910.yaml. Each is asked under docs/protocol.md, Author, step 1.6; the
# attempt runs every reading it can see and records the claims whose outcome depends on the answer.
dandiset: "001754"
paper: doi:10.1038/72910
questions:
- claim: si-comparable-to-preflight
  also: [si-rat1-fd9-vs-preflight, si-rat3-fd4-vs-preflight, fd4-abnormal-selectivity, fig3-stability-across-sessions]
  asked: 2026-10-20
  question: Reading M-b recomputes rate maps from spikes and position. The dandiset gives position
    only at the spike times of each file's units, so no occupancy time can be computed from it,
    and the preflight files hold no position at all. Should M-b divide spike counts by the
    deposited occupancy map of the epoch (the attempt does this for the flight epochs), and when
    M-b cannot be computed for the preflight cells, is a comparison with preflight judged on M-a
    alone?
  passage: The Fig. 1 legend says all statistical analyses kept off-track positions; the paper
    gives no bin size, smoothing or occupancy rule.
  why: Unsmoothed 64 x 64 maps give a spatial information about twice that of the deposited maps
[... 12 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "questions/000128.yaml",
 "content": "# Questions from attempt 000128-churchland-2010-01 (author, 2026-10-22) about the claims file\n# claims/000128/10.1016-j.neuron.2010.09.015.yaml. Each is asked under docs/protocol.md, Author,\n# step 1.6; the attempt runs every reading it can see and records the claims whose outcome depends on\n# the answer.\ndandiset: \"000128\"\npaper: doi:10.1016/j.neuron.2010.09.015\nquestions:\n- claim: fig6-peri-movement-space-best\n  also: [fig3-maze-most-not-maintained, fig6-each-dimensionality, fig6-performance-vs-dimensionality,\n    fig7a-shuffled-space-poor]\n  attempt: 000128-churchland-2010-01\n  asked: 2026-10-22\n  question: Header M1 gives two readings of the proto-trial selection, T1 (each velocity component\n    must correlate with the condition mean at r > 0.9) and T2 (the two components concatenated). On\n    the dataset T1 keeps 1452 of 1967 trials with delay > 400 ms (73.8%), leaves two conditions (the\n    straight leftward reaches, whose vertical velocity is flat) with no trial and several with one or\n    two, while T2 keeps 1786 (90.8%) and at least 10 per condition. The paper says the selection kept\n    typically about 90% of trials. Does that sentence allow T1 to be set aside, or are both readings\n    to stand?\n  passage: Supplemental Experimental Procedures, Task design and behavioral control (\"Subsequent\n    analysis was thus restricted to the subset of trials (typically ~90% of all trials) where the\n    horizontal and vertical velocity profiles correlated with those of a reference 'proto-trial' with\n    r > 0.9.\").\n  why: Five claims change outcome between the readings and are blocked as methods_underspecified.\n    Under T2 the peri-movement space is best (0.518 against 0.424 kinematic), the shuffled control\n    holds, and one maze neuron keeps its tuning; under T1 the peri-movement space falls below the\n    kinematic and kitchen-sink spaces and below zero at k of 10 or more, the shuffled control fails\n    and no neuron reaches r = 0.72. Performance against dimensionality goes the other way (holds under\n    T1, not under T2).\n- claim: fig4d-mean-correlation-jarray\n  also: [fig3-maze-most-not-maintained, fig4-no-separate-populations, fig4e-correlation-time-course,\n    suppfig1-population-averages, fig6-each-dimensionality]\n  attempt: 000128-churchland-2010-01\n  asked: 2026-10-22\n  question: Header M6 reads \"tuning\" as the range over conditions (S1) or the SD over conditions (S2).\n    With the J-array threshold of more than 5 spikes/s, S2 selects 6 of 182 units, and none that also\n    has peri-movement tuning at least 1.5 times as strong, so the correlation claims have no neuron\n    under S2. Does the paper allow S2 with these thresholds, or is it to be dropped?\n  passage: Methods, Neural recordings and datasets (\"restricted to neurons with at least 10 spikes/s of\n    preparatory tuning\" and \">5 spikes/s of preparatory tuning\" for the arrays); Methods,\n    Correlations (\"at least 1.5 times as strong as preparatory tuning\").\n  why: S2 gives no result for fig3, fig4d, fig4-no-separate-populations, fig4e and suppfig1, which are\n    decided on S1 alone; in fig6-each-dimensionality, S2 under T2 makes L1 fail where S1 makes it\n    hold.\n- claim: suppfig1-population-averages\n  attempt: 000128-churchland-2010-01\n  asked: 2026-10-22\n  question: The criterion divides each neuron's rates by \"its maximum rate\" without saying over what.\n    Is it the maximum over all conditions and times (the attempt's reading a) or over the four plotted\n    conditions (reading b)?\n  passage: Supplemental Figure 1 legend, as cited in the criterion.\n  why: R2 (below a quarter) holds under (a) and not under (b); R1 holds under both, so the outcome\n    does not change at present, but would if R1 were dropped.\n"
}
```

```
File created successfully at: questions/000128.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/000128-churchland-2010 2>&1 | tail -20
```

```
0 error(s)
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/000128-churchland-2010 2>&1 | tail -15
```

```
Installed kernelspec registry-000128-churchland-2010 in executed/000128-churchland-2010/.venv/share/jupyter/kernels/registry-000128-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (152 s)

real	2m54.268s
user	2m44.909s
sys	0m4.649s
```

**Agent**

Passed in 152 s. Now confirm the executed outputs still match the conclusions (seeded, but verify key numbers).

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && python - <<'EOF'
import nbformat
a=nbformat.read('out.ipynb',4); b=nbformat.read('executed/000128-churchland-2010/reproduce_churchland_2010.ipynb',4)
def txt(nb): return [''.join(o.get('text','') for o in c.get('outputs',[]) if o.output_type=='stream') for c in nb.cells if c.cell_type=='code']
ta,tb=txt(a),txt(b)
import re
for i,(x,y) in enumerate(zip(ta,tb)):
    x=re.sub(r'computed in \d+ s|runtime: [\d.]+ min','',x); y=re.sub(r'computed in \d+ s|runtime: [\d.]+ min','',y)
    if x!=y: print("DIFF cell",i); 
print([o.ename for c in b.cells if c.cell_type=='code' for o in c.get('outputs',[]) if o.output_type=='error'])
EOF
```

```
[]
Shell cwd was reset to
```

**Agent**

Outputs are identical to my development run. Building the handover.

**Agent calls Bash**

```bash
python tools/entry.py handover entries/000128-churchland-2010 2>&1 | tail -5; ls executed/000128-churchland-2010/handover; git status --short
```

```
wrote executed/000128-churchland-2010/handover
10.1016-j.neuron.2010.09.015.yaml
mcmaze.py
reproduce_churchland_2010.ipynb
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
?? attempts/000128-churchland-2010-01.yaml
?? entries/000128-churchland-2010/
?? questions/000128.yaml
?? scripts
```

**Agent**

I did steps 1 to 6 of the Author section. The entry passes `check` and `run` in 152 s, and the handover is built in `executed/000128-churchland-2010/handover/`. Nothing is committed.

**(1) Outcomes per claim**

| Claim | Outcome |
|---|---|
| recordings-jarray | partially reproduced: 108 conditions and 2295 trials match; 182 units against 146 |
| recordings-single-electrode | blocked, data_missing |
| fig2b-example-concordant-tuning | blocked, data_missing |
| fig2ce-example-opposing-tuning | blocked, data_missing |
| fig3-maze-most-not-maintained | blocked, methods_underspecified (holds under T2, not under T1) |
| fig4d-mean-correlation-jarray | not reproduced: mean r 0.025 to 0.051, p > 0.4 |
| fig4abc-mean-correlation-single-electrode | blocked, data_missing |
| fig4-no-separate-populations | reproduced |
| fig4e-correlation-time-course | reproduced |
| suppfig1-population-averages | reproduced |
| fig6-peri-movement-space-best | blocked, methods_underspecified (holds under T2, not under T1) |
| fig6-each-dimensionality | blocked, methods_underspecified (readings disagree) |
| fig6-performance-vs-dimensionality | blocked, methods_underspecified (holds under T1, not under T2) |
| prep-dimensionality | not reproduced: 15 to 20 components, not 7 to 10 |
| fig6e-summary-across-datasets | blocked, data_missing |
| fig7a-shuffled-space-poor | blocked, methods_underspecified (holds under T2, not under T1) |
| fig7b-window-start-slide | reproduced (J-array ratio 0.90 to 0.97) |
| ap-location-no-effect-on-correlation | blocked, metadata_insufficient |
| fig7c-anterior-posterior-performance | blocked, metadata_insufficient |
| fig7d-pd-consistency | reproduced |
| fig8-model-weak-correlation | reproduced (simulation) |
| fig8-model-pd-perfect | reproduced (simulation) |

**(2) The dataset and the questions asked**

I pinned 0.220113.0400, the only published version. The draft holds the same two files with identical contents.

The dataset holds only the paper's J-array session (monkey Jenkins, 2009-09-25). There is no speed task, no single-electrode recording and no EMG.

What I found, all recorded under `findings`:
- **Array labels are wrong.** Every unit's electrode reference points into the 96 PMd rows, so by the file all 182 units are in PMd. The reference equals the unit id's channel minus one, so the array offset looks lost in conversion.
- **No locations.** The electrodes have no coordinates. The unit ids' leading digit (92 and 90 units) may be the array number, but nothing documents it.
- **Unit and trial selection.** There are 182 units against the paper's 146, with no record of which units or trials the paper used.
- **Test file.** 574 more trials sit in a test file as 0.7 s segments, with no labels or behaviour and only the 137 held-in units. None is a duplicate of a train trial.
- **Negative delays.** 14 trials have a delay below zero (down to -3 ms).
- **Clocks.** Hand speed rises at the marked movement onset. Reach direction can be decoded from spikes after target onset (accuracy 0.66) but not before (0.17).

Three questions are in `questions/000128.yaml`:
1. **T1 or T2 for the proto-trial selection.** This decides five of the blocked claims. T1 keeps 74% of trials and leaves two conditions empty; T2 keeps 91%. The question cites the supplement's "typically ~90% of all trials".
2. **Whether reading S2 can stand.** It selects 6 units, and none for the correlation claims.
3. **What "maximum rate" means in suppfig1.** The outcome does not change at present.

**(3) Where the protocol was unclear or missing something**

1. A reading that selects no units (S2 for the correlation claims) gives no outcome. The protocol says the outcome is "the one they all give" but does not cover a reading that yields nothing. I decided those claims on the readings that gave a result and recorded the gap.
2. A trial reading can leave a condition with no trials (T1 empties two). Nothing says what to do. I dropped those conditions for that reading and recorded it as a deviation.
3. The claims file allows the array as a fallback for anterior-posterior location, but the dataset's array labels are wrong. The protocol has no rule for an undocumented substitute such as the unit-id digit. I blocked both claims as metadata_insufficient and showed the digit regression only as a variant that decides nothing.
4. The paper's own "~90% kept" works like the protocol's chance-level check for a selection, but that check is written only for chance levels and false-positive rates. I did not use it to drop T1 and asked instead.
5. recordings-jarray: the criterion only says when the claim is reproduced, not when it is partial. Two of three counts match, so I called it partially reproduced.
6. Some details the criteria leave open below their stated readings. I ran both versions of each and recorded them as deviations, not questions, since neither changes an outcome:
   - V1 "maximum absolute value": run as the magnitude and as the signed component.
   - How the go- and movement-locked rates are joined under A2.
   - Acceleration: taken as the time derivative of the dataset's hand velocity.

**(4) Runtime and failures**

The notebook runs in about 2.5 minutes (152 s under `tools/entry.py run`; `all` took 2 min 54 s). Nothing failed.

One bug turned up during development and is fixed: an empty condition was averaged as zero rates. That had made fig4d look reproduced (mean r 0.117); with the fix it is not reproduced.

Some untracked dotfiles (`.bashrc`, `.idea` and others) are in the repository root. I did not create them and left them alone.

## End of run

53 turns, 22 minutes, result: success.
