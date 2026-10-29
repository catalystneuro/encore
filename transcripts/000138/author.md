# 000138 · author · run 40756966342

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (35.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/b96738ae-f3f9-4001-acf0-9aea9e3b2361/tool-results/b7qgr1pku.txt

Preview (first 2KB):
Wed Oct 28 19:47:00 UTC 2026
# Protocol for an attempt

Version: `pilot-12`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
[... 20 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "docs/protocol.md"
}
```

```
1	# Protocol for an attempt
2	
3	Version: `pilot-12`. Record this version in the attempt's provenance.
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
[... 593 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; echo ----; cat docs/design.md | head -150; echo ----; cat docs/archives.md
```

```
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>, and the `encore` command that runs the same check on your own data ([docs/encore.md](docs/encore.md)). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Dashboard:** <https://encorescience.org/>

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 499 more lines not kept]
```

**Agent calls Bash**

```bash
ls claims/000138 claims/001453 entries/001453-fouke-2025 paper/ questions/ 2>&1 | head -50; cat claims/000138/*.yaml
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "claims/000138/10.1016-j.neuron.2010.09.015.yaml"
}
```

```
1	# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000138.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
3	# protocol pilot-12 as stated in docs/protocol.md.
4	#
5	# Text read: the NIH author manuscript in PubMed Central (PMC2991102, NIHMS240235), main text,
6	# Methods and figure legends, with its one supplement file (NIHMS240235-supplement-01.pdf:
7	# Supplemental Figures 1 to 5, Supplemental Text, Supplemental Experimental Procedures). This is
8	# the accepted manuscript, not the copyedited version of record. The main-text PDF was not
9	# available, so Figure 6A-D, the range of dimensionalities plotted there and the per-dataset
10	# values in Figures 6 and 7 could not be read. The paper links no analysis code, so no code was
11	# read.
12	#
13	# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
14	# Procedures). Three adult male rhesus monkeys (A, B, J) made delayed reaches on a fronto-parallel
15	# screen. Speed task (monkeys A, B): 7 directions, 2 distances, 2 instructed speeds, 28 conditions.
16	# Maze task (monkey J): straight reaches, or reaches curving around virtual barriers, with or
17	# without distractor targets, 108 conditions in all. Four datasets: A (64 single units), B (74), J
18	# (172 single units by single electrode, in four sets of 27 conditions, about 53 neurons each,
19	# analysed per set and then averaged), and J-array (two 96-electrode arrays, one in caudal PMd and
20	# one in surface M1, 146 single- and multi-unit isolations, all 108 conditions interleaved). Mean
[... 408 more lines not kept]
```

**Agent**

Read the protocol and the claims file (15 claims). Next: the format of the newest entry, then the dataset.

**Agent calls Bash**

```bash
cd entries/001453-fouke-2025; cat entry.yaml README.md requirements.in; head -c 3000 omr.py; python -c "
import json;nb=json.load(open('reproduce_fouke_2025.ipynb'))
for c in nb['cells'][:6]: print(c['cell_type'],c.get('metadata'),''.join(c['source'])[:1500]); print('=====')
print(len(nb['cells']))
"
```

```
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
- path: reproduce_fouke_2025.ipynb
  title: Reproducing Fouke et al. (2025) from dandiset 001453
  runtime_minutes: 6
helpers:
- omr.py
related:
- id: dandi:001453/0.250518.1950
  relation: uses_data
- id: doi:10.1016/j.cub.2025.04.027
[... 200 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat attempts/001453-fouke-2025-01.yaml | head -150; grep -n "" attempts/001453-fouke-2025-01.yaml | sed -n '150,400p' | grep -n -E "^[0-9]+:[a-z_]+:|findings|provenance"
```

```
schema_version: 2
id: 001453-fouke-2025-01
dataset:
  archive: dandi
  id: "001453"
  version: 0.250518.1950
  doi: 10.48324/dandi.001453/0.250518.1950
paper: doi:10.1016/j.cub.2025.04.027
date: 2026-10-14
entry: 001453-fouke-2025
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
    harness: Claude Code (GitHub Actions)
    model: claude-opus-5-5
    protocol: pilot-5
  runner:
    platform: GitHub Actions
[... 133 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,320p attempts/001453-fouke-2025-01.yaml; ls schemas tools; cat questions/README.md | head -40
```

```
notes: The numbers come from single representative fish and trials. Fig1-S1.ipynb selects them
    by the index of a data folder and a trial number (for example DC folder 29, trial 79), and the
    dandiset gives no mapping from those folders to its subjects, nor the original file names.
- claim: fig2d-shared-architecture
  outcome: blocked
  blocked_by: data_missing
  notes: The two-photon imaging data are not in the dandiset, which holds only freely swimming
    tracking. The GitLab repository the paper names for "all behavioral and imaging data" holds
    notebooks only, and no other dandiset of this lab or paper was found on the archive.
- claim: fig2g-dsi-similar
  outcome: blocked
  blocked_by: data_missing
  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
- claim: fig2h-fewer-motion-responsive
  outcome: blocked
  blocked_by: data_missing
  notes: Imaging data not in the dandiset, nor found elsewhere (see fig2d-shared-architecture).
- claim: fig2k-more-monocular
  outcome: blocked
  blocked_by: data_missing
[... 146 more lines not kept]
```

**Agent**

Now the dataset.

**Agent calls Bash**

```bash
cd  curl -s https://api.dandiarchive.org/api/dandisets/000138/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000138/versions/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd  V=0.220113.0407; curl -s "https://api.dandiarchive.org/api/dandisets/000138/versions/$V/" > $TMPDIR/meta.json; python -c "
import json;m=json.load(open('$TMPDIR/meta.json'))
print(m.get('description'));print(m.get('relatedResource'));print(m.get('assetsSummary'));print(m.get('doi'))"; curl -s "https://api.dandiarchive.org/api/dandisets/000138/versions/$V/assets/" | python -m json.tool; curl -s "https://api.dandiarchive.org/api/dandisets/000138/versions/draft/assets/" | python -c "import json,sys;[print(a['path'],a['size'],a['blob'] if 'blob' in a else a.get('asset_id')) for a in json.load(sys.stdin)['results']]"
```

Result: the fetched text is not kept.

**Agent**

One published version (0.220113.0407), same blobs as the draft. Opening the train file.

**Agent calls Bash**

```bash
cd  python -c "import pynwb,remfile,h5py,dandi;print(pynwb.__version__)" 2>&1; which uv python; python --version
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb,remfile,h5py,dandi;print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.16/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.16/x64/bin/python
Python 3.13.16
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb remfile h5py dandi numpy scipy pandas matplotlib scikit-learn statsmodels ipykernel nbclient 2>&1 | tail -3; python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/dev/bin/activate; cat > $TMPDIR/look.py <<'EOF'
import remfile,h5py,pynwb,time
from dandi.dandiapi import DandiAPIClient
c=DandiAPIClient(); d=c.get_dandiset("000138","0.220113.0407")
for a in d.get_assets():
    url=a.get_content_url(follow_redirects=1,strip_query=True)
    t=time.time()
    f=h5py.File(remfile.File(url),'r'); io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
    print(a.path, time.time()-t)
    print(nwb)
    print(nwb.session_description, nwb.subject)
    for k,v in nwb.acquisition.items(): print('acq',k,v)
    for k,m in nwb.processing.items():
        print('proc',k)
        for kk,vv in m.data_interfaces.items(): print('  ',kk,vv)
    if nwb.trials is not None:
        df=nwb.trials.to_dataframe(); print(df.columns.tolist()); print(df.head(5).T); print(df.describe().T)
    if nwb.units is not None:
        print(nwb.units.colnames); u=nwb.units.to_dataframe(); print(u.head().T); print(len(u))
    print(nwb.electrodes.to_dataframe().head() if nwb.electrodes is not None else None)
    print(nwb.electrode_groups)
EOF
python $TMPDIR/look.py 2>&1 | head -300
```

```
sub-Jenkins/sub-Jenkins_ses-large_desc-test_ecephys.nwb 0.5777385234832764
root pynwb.file.NWBFile at 0x133966153448288
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
  file_create_date: [datetime.datetime(2021, 9, 1, 22, 26, 51, 523004, tzinfo=tzoffset(None, -14400))]
  identifier: 3b56e14e-0b95-11ec-a513-5fc582312949
  institution: Stanford University
  intervals: {
    trials <class 'pynwb.epoch.TimeIntervals'>
  }
[... 248 more lines not kept]
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/dev/bin/activate; cat > $TMPDIR/look2.py <<'EOF'
import remfile,h5py,pynwb,numpy as np,pandas as pd
pd.set_option('display.width',250); pd.set_option('display.max_columns',30)
from dandi.dandiapi import DandiAPIClient
d=DandiAPIClient().get_dandiset("000138","0.220113.0407")
a=d.get_asset_by_path("sub-Jenkins/sub-Jenkins_ses-large_desc-train_behavior+ecephys.nwb")
f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1,strip_query=True)),'r')
nwb=pynwb.NWBHDF5IO(file=f,load_namespaces=True).read()
e=nwb.electrodes.to_dataframe(); print(e.columns.tolist()); print(e.head(3).T); print(e.group_name.value_counts()); print(e.describe(include='all').T)
print(nwb.electrodes.colnames, [ (c.name,c.description) for c in nwb.electrodes.columns])
u=nwb.units
print([(c.name,c.description) for c in u.columns])
ud=u.to_dataframe(); print(ud.heldout.value_counts()); 
el=[ (r.index[0], r.group_name.iloc[0]) for r in ud.electrodes]; print(pd.Series([g for _,g in el]).value_counts())
print(sorted([i for i,_ in el])[:200])
t=nwb.trials.to_dataframe()
print([(c.name,c.description) for c in nwb.trials.columns])
print(t.split.value_counts()); print(t.success.value_counts())
print(t.groupby(['trial_type','trial_version']).size().unstack())
print(t.maze_id.nunique(), t.groupby(['trial_type','trial_version']).maze_id.nunique().unstack())
print(t.num_targets.value_counts(), t.num_barriers.value_counts())
print(t.delay.describe(), (t.delay>400).sum())
print(t[['start_time','target_on_time','go_cue_time','move_onset_time','stop_time','rt','delay']].head(10))
print(((t.go_cue_time-t.target_on_time)*1000-t.delay).describe())
print(((t.move_onset_time-t.go_cue_time)*1000-t.rt).describe())
print((t.stop_time-t.start_time).describe())
hp=nwb.processing['behavior']['hand_pos']; ts=hp.timestamps[:10000]; print(np.diff(ts)[:5], ts[0], hp.timestamps[-1])
print(f['processing/behavior/hand_pos/data'].chunks, f['processing/behavior/hand_pos/data'].compression)
st=ud.spike_times; print(len(np.concatenate(st.values)))
print(ud.obs_intervals.iloc[0][:3], len(ud.obs_intervals.iloc[0]))
EOF
python $TMPDIR/look2.py 2>&1
```

```
['x', 'y', 'z', 'imp', 'location', 'filtering', 'group', 'group_name']
id                                                          1                                                  2                                                  3
x                                                         NaN                                                NaN                                                NaN
y                                                         NaN                                                NaN                                                NaN
z                                                         NaN                                                NaN                                                NaN
imp                                                       NaN                                                NaN                                                NaN
location                                                  PMd                                                PMd                                                PMd
filtering                                             1000 Hz                                            1000 Hz                                            1000 Hz
group       electrode_group_PMd pynwb.ecephys.ElectrodeGro...  electrode_group_PMd pynwb.ecephys.ElectrodeGro...  electrode_group_PMd pynwb.ecephys.ElectrodeGro...
group_name                                electrode_group_PMd                                electrode_group_PMd                                electrode_group_PMd
group_name
electrode_group_PMd    96
electrode_group_M1     96
Name: count, dtype: int64
           count unique                                                top freq mean  std  min  25%  50%  75%  max
x            0.0    NaN                                                NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
y            0.0    NaN                                                NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN  NaN
z            0.0   
[... 107 more lines not kept]
```

**Agent calls Bash**

```bash
cd  wc -c paper/*; grep -n -i -E "2009|J-array|jenkins|array" paper/10.1016-j.neuron.2010.09.015.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd  fold -s -w 200 paper/10.1016-j.neuron.2010.09.015.txt > $TMPDIR/paper.txt; wc -l $TMPDIR/paper.txt
```

Result: not kept, because it reads the paper's text.

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 1,
 "limit": 300
}
```

```
1	DOI: 10.1016/j.neuron.2010.09.015
2	Version: as served by ncbi_pmc
3	Source: ncbi_pmc+crossref (paper-text-fetcher)
4	Stored: 2026-10-20
5	Extracted: as fetched; with 1 supplement file(s) from PubMed Central, downloaded in a browser (PMC2991102), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
6	------------------------------------------------------------------------
7	Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-title NIHPA Author Manuscripts PMC2991102 PMC2991102.1 2991102 2991102 NIHMS240235 21040842 
8	10.1016/j.neuron.2010.09.015 NIHMS240235 NIHPA240235 1 Article Cortical preparatory activity: representation of movement or first cog in a dynamical machine? Churchland MM 1 Cunningham JP 1 3 Kaufman 
9	MT 2 Ryu SI 1 4 Shenoy KV 1 2 5 1 Dept. of Electrical Engineering, Stanford University, Stanford CA, 94305, USA 2 Neurosciences Program, Stanford University, Stanford CA, 94305, USA 3 Dept. of 
10	Engineering, University of Cambridge, Cambridge, UK 4 Dept. of Neurosurgery, Palo Alto Medical Foundation, Palo Alto CA, 94301, USA 5 Dept. of Bioengineering, Stanford University, Stanford CA, 94705, 
11	USA 4 11 2010 68 3 191982 387 400 06 10 2010 04 11 2011 04 11 2011 06 10 2011 14 10 2026 This file is available for text mining. It may also be used consistent with the principles of fair use under 
12	the copyright law. Summary The motor cortices are active during both movement and movement preparation. A common assumption is that preparatory activity constitutes a sub-threshold form of movement 
13	activity: a neuron active during rightwards movements becomes modestly active during preparation of a rightwards movement. We asked whether this pattern of activity is in fact observed. We found that 
14	it was not: at the level of a single neuron, preparatory tuning was weakly correlated with movement-period tuning. Yet somewhat paradoxically, preparatory tuning could be captured by a preferred 

[... 286 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 300,
 "limit": 40
}
```

```
300	median ( posterior ). Second black bar : performance when data were randomly subdivided. D. PD consistency for the peri-movement space versus that for a variety of other spaces. Kinematic and EMG 
301	spaces were chosen because they had performed the best overall (after the peri-movement space) in the analysis in Fig. 6 . ‘ Targs. + inst. speed ’ and ‘ segment directions ’ spaces were chosen 
302	because they performed well for the speed and maze tasks respectively. ‘ Targs. + inst. speed ’ was undefined for the maze task; the similar ‘ endpoints + max. spd. ’ space was analyzed instead. 
303	Figure 8 Illustration of the behavior of a simple linear dynamical system: a harmonic oscillator. A. Changes in the initial state produce a linear scaling of the subsequent activity pattern. In this 
304	case, the larger the initial state of unit 1, the greater the amplitude of the oscillation. B. State space containing 25 randomly chosen initial states (25 ‘conditions’). Symbol size/color indicates 
305	the initial firing rate of unit 1. For the simulations below, activity evolved counterclockwise from the initial state: x (t+1) = W x (t), where x is the 2-dimensional vector of unit activities, and 
306	the matrix W = [1 - 2π/360; 2π/360 1]. Thus, the state rotates one degree with each time-step. C. Activity of unit 1 versus time for the initial states shown in B. The initial state was at first held 
307	constant (as if W were the identity matrix) to emulate preparatory activity. The dynamics were then released to produce sinusoidal ‘peri-movement’ activity. Asterisks indicate the same two conditions 
308	as in B. D. The pattern of initial states (the ‘preparatory tuning’) from C is captured by a PD in peri-movement space. Analysis/format are the same as for figure 5C . Traces on each axis plot the 
309	time-evolving pattern corresponding to that PC (black and blue traces for units one and two). The pattern at the end of the arrow is the weighted sum of the two PCs, with w
[... 30 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n -i -E "supplement|proto|smooth|gaussian|upper limit|upper-limit|90%" $TMPDIR/paper.txt | sed -n 1,80p | cut -c1-250
```

```
5:Extracted: as fetched; with 1 supplement file(s) from PubMed Central, downloaded in a browser (PMC2991102), PDFs extracted with PyMuPDF (dehyphenated, NFKC), Word files with textutil
18:no pmc-prop-olf no pmc-prop-manuscript yes pmc-prop-open-manuscript yes pmc-prop-legally-suppressed no pmc-prop-has-pdf yes pmc-prop-has-supplement yes pmc-prop-pdf-only no 
171:yield poorer performance, as the peri-movement space is impacted more by sampling noise. To combat this complication, we normalized performance by its estimated upper limit (e.g., the gray line in 
228:will produce movement. Methods Task design and behavior Animal protocols were approved by the Stanford University Institutional Animal Care and Use Committee. Our basic methods have been described 
268:Performance below zero typically indicates overfitting. Supplementary Material 01 Figures Figure 1 Illustration of behavior. A. Reaches were from a central spot to a target. An example trajectory is 
275:averaged separately locked to target onset, the go cue, and movement onset. To aid viewing, data have been interpolated across the gaps between these three epochs. See Supplemental Figure 4 for a 
276:description of the smoothing used to produce these PSTHs. Inset plots mean hand trajectory using the same color-coding. C-E. Similar plots for three more example neurons. Data have been down-selected 
281:different reach patterns, corresponding to different subsets. In addition to temporal filtering, additional de-noising was accomplished via the method in Supplemental Figure 4 . This method removes 
284:indicates the distribution mean. E. Average correlation as a function of when peri-movement activity was assessed. Peri-movement activity was measured at a single time-point, after smoothing with a 
285:20 ms Gaussian kernel. Correlations are initially high, as preparatory tuning is being correlated with itself. Figure 5 Example PDs in a space based on movement endpoints ( left column ) and the 
293:upper-limit on
[... 50 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 600,
 "limit": 80
}
```

```
600	   -0.59 
601	    0.69
602	Supplemental  Figure  2
603	≈
604	��
605	�����������
606	��
607	�
608	�����������
609	����
610	���
611	horizontal target location
612	����
613	���
614	vertical target location
615	�
616	A
617	C
618	peri-movement  neural  data  (’T’  matrix)
619	peri-movement space
[... 60 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/tmp/claude-1001/paper.txt",
 "offset": 905,
 "limit": 160
}
```

```
905	than directly via a behavioral measurement (see Supp. Fig. 2).
906	
907	=== page 13 ===
908	Supplemental Text: explanation of how a PD in peri-movement space can capture 
909	preparatory activity for a time-varying linear dynamical system (please see Supp. Fig 5 
910	for a less formal illustration of the derivation below). 
911	 
912	Consider a dynamical neural system, with the firing rate of each neuron 
913	represented by the state x(t), a 1!n vector. Suppose the dynamics of this system are 
914	captured by,  
915	xcond(t+1) = xcond (t)W(t) 
916	where xcond(t) is the evolution of the state for a particular condition, and W(t) is an 
917	n!n time-varying matrix. If we have c conditions we can write,  
918	X(t+1) = X(t)W(t) 
919	where X(t) has dimensions c!n. Now consider the c!nt matrix,  
920	R = [X(1), X(2) ), X(3)... ] 
921	and the n!nt matrix,  
922	F = [W(0), W(0)W(1), W(0)W(1)W(2)... ]. 
923	We can write 
924	R = X(0)F 
[... 139 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; . $TMPDIR/dev/bin/activate; cat > $TMPDIR/look3.py <<'EOF'
import remfile,h5py,pynwb,numpy as np,pandas as pd
from dandi.dandiapi import DandiAPIClient
d=DandiAPIClient().get_dandiset("000138","0.220113.0407")
a=d.get_asset_by_path("sub-Jenkins/sub-Jenkins_ses-large_desc-train_behavior+ecephys.nwb")
f=h5py.File(remfile.File(a.get_content_url(follow_redirects=1,strip_query=True)),'r')
print(list(f['units'].keys()))
print(f['units/id'][:20], f['units/id'][-5:])
print(f['units/electrodes'][:20], f['units/electrodes_index'][:10])
print(f['general/extracellular_ephys/electrodes/id'][:5], f['general/extracellular_ephys/electrodes/id'][-5:])
print(f['general/extracellular_ephys/electrodes/location'][[0,95,96,191]])
nwb=pynwb.NWBHDF5IO(file=f,load_namespaces=True).read()
t=nwb.trials.to_dataframe()
print('stop-move', (t.stop_time-t.move_onset_time).describe())
print('target-start', (t.target_on_time-t.start_time).describe())
print('next start - stop', (t.start_time.values[1:]-t.stop_time.values[:-1]).min())
ud=nwb.units.to_dataframe()
allsp=np.concatenate(ud.spike_times.values)
# spikes outside trials?
st=t.start_time.values; sp=t.stop_time.values
idx=np.searchsorted(st,allsp,side='right')-1
inside=(idx>=0)&(allsp<=sp[np.clip(idx,0,None)])
print('spikes outside trial intervals', (~inside).sum(), len(allsp))
print(np.diff(np.concatenate(ud.spike_times.values[:1])).min())
print([ (np.diff(s)<0).sum() for s in ud.spike_times.values][:20], sum((np.diff(s)<0).sum() for s in ud.spike_times.values))
print(pd.Series(t.target_pos.apply(lambda x: tuple(np.asarray(x)[0]) )).value_counts().head())
print(t.groupby(['trial_type','trial_version']).apply(lambda g: np.asarray(g.target_pos.iloc[0])[int(g.active_target.iloc[0])]).to_string())
print(t.groupby(['trial_type','trial_version']).active_target.unique().to_string())
EOF
python $TMPDIR/look3.py 2>&1
```

```
Wed Oct 28 19:50:20 UTC 2026
['electrodes', 'electrodes_index', 'heldout', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index']
[1011 1012 1021 1031 1041 1042 1043 1051 1061 1062 1063 1071 1081 1082
 1091 1092 1101 1111 1112 1121] [2821 2861 2881 2941 2951]
[ 0  0  1  2  3  3  3  4  5  5  5  6  7  7  8  8  9 10 10 11] [ 1  2  3  4  5  6  7  8  9 10]
[1 2 3 4 5] [188 189 190 191 192]
[b'PMd' b'PMd' b'M1' b'M1']
stop-move count    500.000000
mean       1.146076
std        0.095425
min        0.963000
25%        1.070750
50%        1.139500
75%        1.216000
max        1.540000
dtype: float64
target-start count    500.000000
mean       0.802786
std        0.087246
min        0.650000
[... 72 more lines not kept]
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/dev/bin/activate; python - <<'EOF'
import remfile,h5py,numpy as np
from dandi.dandiapi import DandiAPIClient
d=DandiAPIClient().get_dandiset("000138","0.220113.0407")
for p in ["sub-Jenkins/sub-Jenkins_ses-large_desc-train_behavior+ecephys.nwb","sub-Jenkins/sub-Jenkins_ses-large_desc-test_ecephys.nwb"]:
    f=h5py.File(remfile.File(d.get_asset_by_path(p).get_content_url(follow_redirects=1,strip_query=True)),'r')
    ids=f['units/id'][:]; el=f['units/electrodes'][:]; ho=f['units/heldout'][:]
    arr=ids//1000; ch=(ids%1000)//10; s=ids%10
    print(p, len(ids), np.unique(arr,return_counts=True))
    print('channel==electrode+1:', np.all(ch==el+1), 'max ch', ch.max())
    for a in (1,2): print(a, 'heldout', ho[arr==a].sum(), 'of', (arr==a).sum())
EOF
```

```
sub-Jenkins/sub-Jenkins_ses-large_desc-train_behavior+ecephys.nwb 162 (array([1, 2]), array([83, 79]))
channel==electrode+1: True max ch 95
1 heldout 20 of 83
2 heldout 20 of 79
sub-Jenkins/sub-Jenkins_ses-large_desc-test_ecephys.nwb 122 (array([1, 2]), array([63, 59]))
channel==electrode+1: True max ch 95
1 heldout 0 of 63
2 heldout 0 of 59
```

**Agent calls Bash**

```bash
cd  . $TMPDIR/dev/bin/activate; python - <<'EOF'
import remfile,h5py,numpy as np
from dandi.dandiapi import DandiAPIClient
d=DandiAPIClient().get_dandiset("000138","0.220113.0407")
f=h5py.File(remfile.File(d.get_asset_by_path("sub-Jenkins/sub-Jenkins_ses-large_desc-train_behavior+ecephys.nwb").get_content_url(follow_redirects=1,strip_query=True)),'r')
p=f['processing/behavior/hand_pos/data'][200000:203000]; v=f['processing/behavior/hand_vel/data'][200000:203000]
dp=np.gradient(p,axis=0)*1000
print(np.corrcoef(dp[:,0],v[:,0])[0,1], np.median(np.abs(v[:,0])), np.median(np.abs(dp[:,0])))
print(np.round(p[1000:1040,0],3))
print(np.round(v[1000:1040,0],2))
print(f['processing/behavior/hand_pos/timestamps'][:3], f['processing/behavior/hand_pos/timestamps'].shape)
EOF
```

```
0.095361287831693 1.8878119513825176 1.8926087389875974
[-0.736 -0.736 -0.735 -0.735 -0.735 -0.734 -0.734 -0.733 -0.733 -0.732
 -0.732 -0.731 -0.731 -0.731 -0.73  -0.73  -0.73  -0.729 -0.729 -0.728
 -0.728 -0.727 -0.727 -0.726 -0.725 -0.724 -0.724 -0.723 -0.721 -0.72
 -0.719 -0.717 -0.716 -0.714 -0.713 -0.711 -0.709 -0.707 -0.705 -0.704]
[0.3  0.35 0.34 0.39 0.42 0.4  0.47 0.46 0.49 0.5  0.45 0.4  0.37 0.42
 0.33 0.27 0.35 0.43 0.42 0.44 0.49 0.6  0.66 0.68 0.83 0.9  0.98 1.07
 1.16 1.3  1.42 1.53 1.62 1.66 1.65 1.74 1.81 1.79 1.68 1.69]
[0.    0.001 0.002] (1453340,)
```

**Agent calls Write**

```json
{
 "file_path": "entries/000138-churchland-2010/prepspace.py",
 "content": "\"\"\"Loading and measures for dandiset 000138 (MC_Maze_Large), for Churchland, Cunningham, Kaufman,\nRyu & Shenoy (2010), Neuron 68:387-400, doi:10.1016/j.neuron.2010.09.015.\n\nThe dandiset holds one session of monkey J (Jenkins, 2009-10-06) on the maze task: 500 successful\ntrials over 27 conditions (9 mazes, `trial_type`, each in 3 versions, `trial_version`), 162 sorted\nunits from two 96-electrode arrays, and hand position and velocity at 1 kHz. Files are streamed\nfrom the archive at the pinned version; nothing is written to disk.\n\nWhere the parameters come from. \"Claims file\" means the shared methods at the top of\nclaims/000138/10.1016-j.neuron.2010.09.015.yaml, which cite the paper; \"paper\" means a passage\ntaken here (protocol, author, step 1.6); \"assumption\" and \"standard choice\" are said as such.\n\n- `MIN_DELAY_MS` = 400: only trials with delays over 400 ms (claims file; Methods, Task design).\n- `PROTO_R` = 0.9: maze trials kept when their horizontal and vertical velocity profiles\n  correlate with a reference proto-trial at r > 0.9 (claims file; Supplemental Experimental\n  Procedures, Task design). The proto-trial is the condition's mean profile (reading a) or its\n  elementwise median profile (reading b). The window of the profile is not given; the window of\n  the peri-movement T-matrix (`T_WINDOW`) is used (assumption: it is the window the paper\n  analyses). Whether horizontal and vertical are each required to pass (`each`) or are\n  correlated as one concatenated profile (`concat`) is not said; both are run.\n- `SMOOTH_SD_MS` = 20: spike trains smoothed with a 20 ms Gaussian before averaging (claims\n  file; Supplemental Experimental Procedures, Computing the mean firing rate versus time). SD\n  20 ms is the claims file's standard choice.\n- `PREP_WINDOW` = go cue -200 to +100 ms; `PERI_WINDOW` = movement onset -100 to +350 ms\n  (claims file; Methods, Correlations between preparatory and peri-movement tuning).\n- `T_WINDOW` = movement onset -150 to +800 ms, the maze task's peri-movement T-matrix (claims\n  file; Methods, PCA-based spaces). Time step 1 ms (standard choice, as the claims file says).\n- `ARRAY_MIN_TUNING` = 5 spikes/s, the array inclusion criterion (claims file; Methods, Neural\n  recordings). Tuning is the range (reading a) or the SD (reading b) of the condition means.\n- `PERI_RATIO` = 1.5, the extra Figure 4 criterion (claims file; Methods, Correlations).\n- Movement onset: the trial table's `move_onset_time` (reading a), or a hand speed threshold\n  crossing (reading b), at `ONSET_FRACTION` = 10% of the trial's peak speed, the last crossing\n  before the peak (standard choice; the claims file leaves the threshold open).\n- Reach end, for task spaces and reading b of the kinematic window: the first time after peak\n  speed that speed falls below `END_FRACTION` = 10% of the peak (standard choice), or, as the\n  claims file's other reading, a fixed time, here the end of `T_WINDOW` (+800 ms).\n- Task spaces follow the Methods, Task spaces, as listed in the claims file. They are measured\n  on the condition's mean hand trajectory (standard choice: the paper measures \"average\n  endpoint and peak velocity for each condition\", Results, Testing preparatory tuning).\n- Kinematic T-matrix: horizontal and vertical position, velocity and acceleration from 150 ms\n  before movement onset, each variable scaled to unity range across times and conditions\n  (claims file; Methods, PCA-based spaces). Acceleration is the time derivative of the\n  condition-mean velocity (standard choice). Replicating the six variables equally to the number\n  of neurons gives the same PC scores up to a scale and so the same PD fits, so they are used\n  once.\n- PD performance: leave-one-condition-out, 1 - MSE / variance (claims file; Methods, PD\n  performance). The space is computed once from all conditions (`fold=\"once\"`, reading a) or\n  recomputed without the left-out condition (`fold=\"refit\"`, reading b). Variance is the\n  population variance (ddof 0) of the neuron's condition means.\n\"\"\"\n\nfrom __future__ import annotations\n\nimport h5py\nimport numpy as np\nimport pandas as pd\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy.ndimage import gaussian_filter1d\nfrom scipy.stats import rankdata\n\nDANDISET_ID = \"000138\"\nDANDISET_VERSION = \"0.220113.0407\"\nTRAIN_PATH = \"sub-Jenkins/sub-Jenkins_ses-large_desc-train_behavior+ecephys.nwb\"\nTEST_PATH = \"sub-Jenkins/sub-Jenkins_ses-large_desc-test_ecephys.nwb\"\n\nMIN_DELAY_MS = 400\nPROTO_R = 0.9\nSMOOTH_SD_MS = 20\nPREP_WINDOW = (-200, 100)      # ms from the go cue\nPERI_WINDOW = (-100, 350)      # ms from movement onset\nT_WINDOW = (-150, 800)         # ms from movement onset\nMOVE_TRACE = (-600, 850)       # ms from movement onset, the traces kept per trial\nARRAY_MIN_TUNING = 5.0\nPERI_RATIO = 1.5\nONSET_FRACTION = 0.10\nEND_FRACTION = 0.10\n\nTASK_SPACES = [\"initial velocity\", \"endpoints + max speed\", \"endpoints + orthogonal excursion\",\n               \"endpoints + viapoint\", \"endpoints + max velocity\", \"endpoints + halfpoint\",\n               \"segment directions\", \"kitchen sink\"]\n\n\n# ----------------------------------------------------------------------------------------------\n# Loading\n\ndef asset_url(path):\n    dandiset = DandiAPIClient().get_dandiset(DANDISET_ID, DANDISET_VERSION)\n    return dandiset.get_asset_by_path(path).get_content_url(follow_redirects=1, strip_query=True)\n\n\ndef open_h5(path):\n    return h5py.File(remfile.File(asset_url(path)), \"r\")\n\n\ndef _ragged(f, name):\n    data, index = f[name][:], f[name + \"_index\"][:]\n    return np.split(data, index[:-1])\n\n\ndef load_train():\n    \"\"\"Trials, units and hand data of the training file, read with h5py from the stream.\"\"\"\n    f = open_h5(TRAIN_PATH)\n    tr = f[\"intervals/trials\"]\n    trials = pd.DataFrame({k: tr[k][:] for k in [\n        \"start_time\", \"stop_time\", \"trial_type\", \"trial_version\", \"maze_id\", \"success\",\n        \"target_on_time\", \"go_cue_time\", \"move_onset_time\", \"rt\", \"delay\", \"num_targets\",\n        \"num_barriers\", \"active_target\"]})\n    trials[\"split\"] = [s.decode() for s in tr[\"split\"][:]]\n    trials[\"target_pos\"] = _ragged(tr, \"target_pos\")\n    trials[\"barrier_pos\"] = _ragged(tr, \"barrier_pos\")\n    trials[\"condition\"] = list(zip(trials.trial_type, trials.trial_version))\n    u = f[\"units\"]\n    ids = u[\"id\"][:]\n    units = pd.DataFrame({\n        \"id\": ids, \"heldout\": u[\"heldout\"][:],\n        \"electrode\": [e[0] for e in _ragged(u, \"electrodes\")],\n        \"id_array\": ids // 1000, \"id_channel\": (ids % 1000) // 10})\n    spikes = _ragged(u, \"spike_times\")\n    el = f[\"general/extracellular_ephys/electrodes\"]\n    electrodes = pd.DataFrame({\n        \"id\": el[\"id\"][:], \"location\": [s.decode() for s in el[\"location\"][:]],\n        \"group_name\": [s.decode() for s in el[\"group_name\"][:]],\n        \"x\": el[\"x\"][:], \"y\": el[\"y\"][:], \"z\": el[\"z\"][:]})\n    units[\"electrode_location\"] = electrodes.location.values[units.electrode.values]\n    beh = f[\"processing/behavior\"]\n    hand = {\"t\": beh[\"hand_pos/timestamps\"][:]}\n    for name in [\"hand_pos\", \"hand_vel\", \"cursor_pos\", \"eye_pos\"]:\n        hand[name] = beh[name + \"/data\"][:]\n        hand[name + \"_unit\"] = beh[name + \"/data\"].attrs[\"unit\"]\n        hand[name + \"_conversion\"] = beh[name + \"/data\"].attrs[\"conversion\"]\n        hand[name + \"_description\"] = beh[name].attrs[\"description\"]\n    meta = {\"session_start\": f[\"session_start_time\"][()].decode(),\n            \"subject\": f[\"general/subject/subject_id\"][()].decode(),\n            \"species\": f[\"general/subject/species\"][()].decode(),\n            \"session_description\": f[\"session_description\"][()].decode()}\n    return {\"trials\": trials, \"units\": units, \"spikes\": spikes, \"hand\": hand,\n            \"electrodes\": electrodes, \"meta\": meta}\n\n\ndef load_test_summary():\n    f = open_h5(TEST_PATH)\n    tr = f[\"intervals/trials\"]\n    u = f[\"units\"]\n    return {\"trial_columns\": list(tr.keys()), \"n_trials\": len(tr[\"start_time\"][:]),\n            \"unit_ids\": u[\"id\"][:], \"spikes\": _ragged(u, \"spike_times\"),\n            \"starts\": tr[\"start_time\"][:], \"stops\": tr[\"stop_time\"][:]}\n\n\n# ----------------------------------------------------------------------------------------------\n# Movement onset, trial selection\n\ndef speed_onset(hand, go_s, fraction=ONSET_FRACTION, search_ms=1200):\n    \"\"\"Movement onset by hand speed: last crossing of `fraction` of peak speed before the peak,\n    searched from the go cue to `search_ms` after it.\"\"\"\n    i0 = int(round(go_s * 1000))\n    v = hand[\"hand_vel\"][i0:i0 + search_ms]\n    sp = np.hypot(v[:, 0], v[:, 1])\n    ipk = int(np.argmax(sp))\n    below = np.nonzero(sp[:ipk] < fraction * sp[ipk])[0]\n    j = below[-1] + 1 if len(below) else 0\n    return hand[\"t\"][i0 + j]\n\n\ndef onset_times(data, reading):\n    t = data[\"trials\"]\n    if reading == \"a\":\n        return t.move_onset_time.values.copy()\n    return np.array([speed_onset(data[\"hand\"], g) for g in t.go_cue_time.values])\n\n\ndef _segment(x, centre_s, window_ms):\n    i = int(round(centre_s * 1000))\n    return x[i + window_ms[0]: i + window_ms[1]]\n\n\ndef select_trials(data, onset, proto=\"a\", combine=\"each\"):\n    \"\"\"Trials with delay > 400 ms whose velocity profiles in T_WINDOW correlate with the\n    condition's proto-trial at r > 0.9. Returns a boolean mask over all trials and the r values.\"\"\"\n    t = data[\"trials\"]\n    hv = data[\"hand\"][\"hand_vel\"]\n    keep = (t.delay.values > MIN_DELAY_MS)\n    r_all = np.full((len(t), 2), np.nan)\n    passed = np.zeros(len(t), bool)\n    for cond, idx in t.groupby(\"condition\").indices.items():\n        idx = idx[keep[idx]]\n        prof = np.stack([_segment(hv, onset[i], T_WINDOW) for i in idx])   # trials x time x 2\n        ref = prof.mean(0) if proto == \"a\" else np.median(prof, 0)\n        for j, i in enumerate(idx):\n            if combine == \"each\":\n                r = [np.corrcoef(prof[j, :, d], ref[:, d])[0, 1] for d in (0, 1)]\n                r_all[i] = r\n                passed[i] = min(r) > PROTO_R\n            else:\n                r = np.corrcoef(prof[j].T.ravel(), ref.T.ravel())[0, 1]\n                r_all[i] = [r, r]\n                passed[i] = r > PROTO_R\n    return keep & passed, r_all\n\n\n# ----------------------------------------------------------------------------------------------\n# Firing rates\n\ndef smoothed_rate(spike_times, n_ms, sd_ms=SMOOTH_SD_MS):\n    counts = np.bincount(np.floor(spike_times * 1000).astype(int), minlength=n_ms)[:n_ms]\n    return gaussian_filter1d(counts.astype(float), sd_ms) * 1000.0\n\n\ndef trial_rates(data, onsets_by_reading):\n    \"\"\"Per unit and trial: mean rate in the preparatory epoch, and the movement-locked trace\n    (MOVE_TRACE) for each movement-onset reading. Also the go-locked trace -200..+500 ms.\"\"\"\n    t = data[\"trials\"]\n    n_ms = int(np.ceil(t.stop_time.max() * 1000)) + 2000\n    go = np.round(t.go_cue_time.values * 1000).astype(int)\n    nu, nt = len(data[\"spikes\"]), len(t)\n    prep = np.zeros((nu, nt))\n    go_trace = np.zeros((nu, nt, 700), np.float32)\n    move = {r: np.zeros((nu, nt, MOVE_TRACE[1] - MOVE_TRACE[0]), np.float32)\n            for r in onsets_by_reading}\n    go_idx = go[:, None] + np.arange(-200, 500)[None, :]\n    mv_idx = {r: np.round(o * 1000).astype(int)[:, None] + np.arange(*MOVE_TRACE)[None, :]\n              for r, o in onsets_by_reading.items()}\n    for u, st in enumerate(data[\"spikes\"]):\n        rate = smoothed_rate(st, n_ms)\n        go_trace[u] = rate[go_idx]\n        prep[u] = go_trace[u][:, 200 + PREP_WINDOW[0]: 200 + PREP_WINDOW[1]].mean(1)\n        for r in move:\n            move[r][u] = rate[mv_idx[r]]\n    return {\"prep\": prep, \"go_trace\": go_trace, \"move\": move}\n\n\ndef condition_means(values, trials, mask):\n    \"\"\"Average over the selected trials of each condition, along axis 1 (trials).\"\"\"\n    conds = sorted(trials.condition.unique())\n    out = []\n    for c in conds:\n        idx = np.nonzero((trials.condition.values == pd.Series([c] * len(trials)).values) & mask)[0] \\\n            if False else np.nonzero(np.array([x == c for x in trials.condition]) & mask)[0]\n        out.append(values[:, idx].mean(1))\n    return np.stack(out, 1), conds\n\n\ndef tuning(prep_means, reading):\n    \"\"\"Tuning strength in spikes/s across conditions: range (a) or SD (b).\"\"\"\n    if reading == \"a\":\n        return prep_means.max(1) - prep_means.min(1)\n    return prep_means.std(1)\n\n\ndef epoch_mean(trace_means, window, origin=MOVE_TRACE[0]):\n    return trace_means[..., window[0] - origin: window[1] - origin].mean(-1)\n\n\n# ----------------------------------------------------------------------------------------------\n# Hand kinematics per condition\n\ndef hand_condition_means(data, onset, mask, conds, window=(-200, 1000)):\n    \"\"\"Condition-mean hand position and velocity, movement-locked, ms from onset in `window`.\"\"\"\n    t = data[\"trials\"]\n    pos, vel = [], []\n    for c in conds:\n        idx = np.nonzero(np.array([x == c for x in t.condition]) & mask)[0]\n        pos.append(np.mean([_segment(data[\"hand\"][\"hand_pos\"], onset[i], window) for i in idx], 0))\n        vel.append(np.mean([_segment(data[\"hand\"][\"hand_vel\"], onset[i], window) for i in idx], 0))\n    return np.stack(pos), np.stack(vel), np.arange(*window)\n\n\ndef reach_end_index(vel, times, fraction=END_FRACTION):\n    \"\"\"Per condition, index of the first sample after peak speed (after onset) below `fraction`\n    of the peak.\"\"\"\n    out = []\n    for v in vel:\n        sp = np.hypot(v[:, 0], v[:, 1])\n        sp = np.where(times >= 0, sp, 0)\n        ipk = int(np.argmax(sp))\n        after = np.nonzero(sp[ipk:] < fraction * sp[ipk])[0]\n        out.append(ipk + (after[0] if len(after) else len(sp) - 1 - ipk))\n    return np.array(out)\n\n\ndef _split_points(path, n, by):\n    \"\"\"Indices that cut a path (time x 2) into n parts, by path length or by time.\"\"\"\n    if by == \"time\":\n        return [int(round(len(path) - 1) * j / n) for j in range(n + 1)]\n    seg = np.r_[0, np.cumsum(np.hypot(*np.diff(path, axis=0).T))]\n    return [int(np.searchsorted(seg, seg[-1] * j / n)) for j in range(n + 1)]\n\n\ndef task_spaces(pos, vel, times, conds, trials, end=\"speed\", split=\"length\"):\n    \"\"\"The maze task spaces of the Methods, one c x k matrix each.\"\"\"\n    i0 = int(np.nonzero(times == 0)[0][0])\n    ends = reach_end_index(vel, times) if end == \"speed\" else \\\n        np.full(len(pos), int(np.nonzero(times == T_WINDOW[1] - 1)[0][0]))\n    feats = {k: [] for k in TASK_SPACES}\n    for c, (p, v, ie) in enumerate(zip(pos, vel, ends)):\n        path, pv = p[i0:ie + 1], v[i0:ie + 1]\n        start, stop = path[0], path[-1]\n        d = stop - start\n        perp = (d[0] * (path[:, 1] - start[1]) - d[1] * (path[:, 0] - start[0])) / np.hypot(*d)\n        imax = int(np.argmax(np.abs(perp)))\n        sp = np.hypot(pv[:, 0], pv[:, 1])\n        ipk = int(np.argmax(sp))\n        ivx, ivy = int(np.argmax(np.abs(pv[:, 0]))), int(np.argmax(np.abs(pv[:, 1])))\n        cuts3 = _split_points(path, 3, split)\n        cuts2 = _split_points(path, 2, split)\n        segs = np.concatenate([path[cuts3[j + 1]] - path[cuts3[j]] for j in range(3)])\n        tri = trials[np.array([x == conds[c] for x in trials.condition])].iloc[0]\n        feats[\"initial velocity\"].append(v[i0:i0 + 150].mean(0))\n        feats[\"endpoints + max speed\"].append([*stop, sp[ipk]])\n        feats[\"endpoints + orthogonal excursion\"].append([*stop, perp[imax]])\n        feats[\"endpoints + viapoint\"].append([*stop, *path[imax]])\n        feats[\"endpoints + max velocity\"].append([*stop, pv[ivx, 0], pv[ivy, 1]])\n        feats[\"endpoints + halfpoint\"].append([*stop, *path[cuts2[1]]])\n        feats[\"segment directions\"].append(segs)\n        feats[\"kitchen sink\"].append([*segs, perp[imax], *path[imax],\n                                      float(tri.num_barriers > 0), float(tri.num_targets > 1)])\n    return {k: np.asarray(v, float) for k, v in feats.items()}, ends\n\n\ndef kinematic_matrix(pos, vel, times, end_ms):\n    \"\"\"c x 6t kinematic T-matrix from -150 ms to end_ms, each variable scaled to unity range.\"\"\"\n    sel = (times >= T_WINDOW[0]) & (times < end_ms)\n    acc = np.gradient(vel, axis=1) * 1000.0\n    blocks = []\n    for arr in (pos, vel, acc):\n        for d in (0, 1):\n            x = arr[:, sel, d]\n            blocks.append(x / (x.max() - x.min()))\n    return np.concatenate(blocks, 1)\n\n\n# ----------------------------------------------------------------------------------------------\n# PD performance\n\ndef _scores_from_gram(Gc, kmax):\n    \"\"\"Leading kmax PC scores (c x kmax) from a centred Gram matrix.\"\"\"\n    w, V = np.linalg.eigh(Gc)\n    order = np.argsort(w)[::-1][:kmax]\n    w, V = np.clip(w[order], 1e-12, None), V[:, order]\n    return V * np.sqrt(w), V, w\n\n\ndef centre_gram(G):\n    c = len(G)\n    H = np.eye(c) - 1.0 / c\n    return H @ G @ H\n\n\ndef loo_errors_fixed(S, X):\n    \"\"\"Leave-one-condition-out prediction errors of OLS with offset, for a fixed c x k space S\n    and responses X (n x c). Uses the exact leave-one-out identity e_i / (1 - h_ii).\"\"\"\n    c = S.shape[0]\n    D = np.column_stack([np.ones(c), S])\n    H = D @ np.linalg.pinv(D)\n    resid = X - X @ H.T\n    return resid / (1.0 - np.diag(H))[None, :]\n\n\ndef loo_errors_refit_gram(G, x, kmax):\n    \"\"\"Leave-one-condition-out errors when the PCA space is recomputed without the left-out\n    condition. G is the uncentred c x c Gram matrix of the T-matrix rows; x the c responses.\n    Returns kmax x c errors.\"\"\"\n    c = len(x)\n    err = np.zeros((kmax, c))\n    for i in range(c):\n        tr = np.r_[0:i, i + 1:c]\n        B = G[np.ix_(tr, tr)]\n        A = G[i, tr]\n        Gc = centre_gram(B)\n        scores, V, w = _scores_from_gram(Gc, kmax)\n        cross = A - A.mean() - B.mean(0) + B.mean()\n        test = cross @ V / np.sqrt(w)\n        for k in range(1, kmax + 1):\n            D = np.column_stack([np.ones(c - 1), scores[:, :k]])\n            beta = np.linalg.lstsq(D, x[tr], rcond=None)[0]\n            err[k - 1, i] = x[i] - (beta[0] + test[:k] @ beta[1:])\n    return err\n\n\ndef performance(err, X, pooled=False):\n    \"\"\"1 - MSE / variance per neuron (reading a), or pooled over neurons (reading b).\n    err and X are n x c.\"\"\"\n    var = X.var(1)\n    if pooled:\n        return 1.0 - (err ** 2).sum() / (X.shape[1] * var.sum())\n    return 1.0 - (err ** 2).mean(1) / var\n\n\ndef neuron_grams(M):\n    \"\"\"Per-neuron c x c Gram contributions of a neuron x condition x time array.\"\"\"\n    return np.einsum(\"nct,ndt->ncd\", M, M, optimize=True)\n\n\ndef loo_pca_space(G_total, G_parts, X, kmax, fold):\n    \"\"\"Errors (n x kmax x c) for each neuron's responses X[n] in the PCA space of the T-matrix\n    with that neuron's part removed (G_total - G_parts[n]). G_parts may be None (space shared by\n    all neurons, as for the kinematic space).\"\"\"\n    n, c = X.shape\n    err = np.zeros((n, kmax, c))\n    for j in range(n):\n        G = G_total if G_parts is None else G_total - G_parts[j]\n        if fold == \"once\":\n            S = _scores_from_gram(centre_gram(G), kmax)[0]\n            for k in range(1, kmax + 1):\n                err[j, k - 1] = loo_errors_fixed(S[:, :k], X[j:j + 1])[0]\n        else:\n            err[j] = loo_errors_refit_gram(G, X[j], kmax)\n    return err\n\n\ndef pd_fit(S, x):\n    \"\"\"PD fit with offset; returns the unit-length PD (or None if b is zero).\"\"\"\n    D = np.column_stack([np.ones(len(x)), S])\n    b = np.linalg.lstsq(D, x, rcond=None)[0][1:]\n    nb = np.linalg.norm(b)\n    return b / nb if nb > 0 else None\n\n\ndef corr_pearson_spearman(a, b):\n    \"\"\"Row-wise Pearson and Spearman correlations between two n x c arrays.\"\"\"\n    def rowcorr(x, y):\n        x = x - x.mean(1, keepdims=True)\n        y = y - y.mean(1, keepdims=True)\n        return (x * y).sum(1) / np.sqrt((x ** 2).sum(1) * (y ** 2).sum(1))\n    ra = np.apply_along_axis(rankdata, 1, a)\n    rb = np.apply_along_axis(rankdata, 1, b)\n    return rowcorr(a, b), rowcorr(ra, rb)\n\n\n# ----------------------------------------------------------------------------------------------\n# Figure 8 oscillator\n\ndef oscillator(rng, n_cond=25, hold=100, release=360, init=\"uniform\"):\n    \"\"\"Unit activities (cond x time x 2) for x(t+1) = W x(t), W = [1 -a; a 1], a = 2 pi / 360,\n    held at the initial state for `hold` steps, then released for `release` steps.\"\"\"\n    a = 2 * np.pi / 360\n    W = np.array([[1, -a], [a, 1]])\n    x0 = rng.uniform(-1, 1, (n_cond, 2)) if init == \"uniform\" else rng.standard_normal((n_cond, 2))\n    out = np.zeros((n_cond, hold + release, 2))\n    out[:, :hold] = x0[:, None, :]\n    x = x0.copy()\n    for s in range(release):\n        x = x @ W.T\n        out[:, hold + s] = x\n    return out, x0\n"
}
```

```
File created successfully at: entries/000138-churchland-2010/prepspace.py (file state is current in your context — no need to Read it back)
```

**Agent**

Let me clean up the condition indexing before testing.

**Agent calls Bash**

```bash
cd entries/000138-churchland-2010 && python - <<'EOF'
s=open('prepspace.py').read()
s=s.replace('''    trials["condition"] = list(zip(trials.trial_type, trials.trial_version))
''','''    trials["condition"] = list(zip(trials.trial_type, trials.trial_version))
    conds = sorted(trials.condition.unique())
    trials["cond_idx"] = [conds.index(c) for c in trials.condition]
''')
s=s.replace('''    conds = sorted(trials.condition.unique())
    out = []
    for c in conds:
        idx = np.nonzero((trials.condition.values == pd.Series([c] * len(trials)).values) & mask)[0] \\
            if False else np.nonzero(np.array([x == c for x in trials.condition]) & mask)[0]
        out.append(values[:, idx].mean(1))
    return np.stack(out, 1), conds''','''    ci = trials.cond_idx.values
    return np.stack([values[:, (ci == c) & mask].mean(1) for c in range(ci.max() + 1)], 1)''')
s=s.replace('''def hand_condition_means(data, onset, mask, conds, window=(-200, 1000)):''','''def hand_condition_means(data, onset, mask, window=(-200, 1000)):''')
s=s.replace('''    for c in conds:
        idx = np.nonzero(np.array([x == c for x in t.condition]) & mask)[0]
        pos.append''','''    for c in range(t.cond_idx.max() + 1):
        idx = np.nonzero((t.cond_idx.values == c) & mask)[0]
        pos.append''')
s=s.replace('''def task_spaces(pos, vel, times, conds, trials, end="speed", split="length"):''','''def task_spaces(pos, vel, times, trials, end="speed", split="length"):''')
s=s.replace('''        tri = trials[np.array([x == conds[c] for x in trials.condition])].iloc[0]''','''        tri = trials[trials.cond_idx.values == c].iloc[0]''')
open('prepspace.py','w').write(s)
EOF
grep -n "conds" prepspace.py
```

```
113:    conds = sorted(trials.condition.unique())
114:    trials["cond_idx"] = [conds.index(c) for c in trials.condition]
```

**Agent**

Now a development script to load, time and check the pieces.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/dev1.py <<'EOF'
import time, pickle, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import prepspace as ps
t0=time.time(); data=ps.load_train(); print('load', time.time()-t0)
t=data['trials']
on={'a':ps.onset_times(data,'a'),'b':ps.onset_times(data,'b')}
print('onset diff b-a ms', pd.Series((on['b']-on['a'])*1000).describe())
for proto in 'ab':
  for comb in ['each','concat']:
    for o in 'ab':
      m,r=ps.select_trials(data,on[o],proto,comb)
      print(proto,comb,o,'kept',m.sum(),'of',(t.delay>400).sum(), 'min per cond', pd.Series(t.cond_idx[m]).value_counts().min())
t0=time.time(); R=ps.trial_rates(data,on); print('rates', time.time()-t0)
pickle.dump((data,on,R),open('/tmp/claude-1001/cache.pkl','wb'))
EOF
python $TMPDIR/dev1.py
```

```
Exit code 1
load 3.4072470664978027
Traceback (most recent call last):
  File "/tmp/claude-1001/dev1.py", line 6, in <module>
    on={'a':ps.onset_times(data,'a'),'b':ps.onset_times(data,'b')}
                                         ~~~~~~~~~~~~~~^^^^^^^^^^
  File "entries/000138-churchland-2010/prepspace.py", line 171, in onset_times
    return np.array([speed_onset(data["hand"], g) for g in t.go_cue_time.values])
                     ~~~~~~~~~~~^^^^^^^^^^^^^^^^^
  File "entries/000138-churchland-2010/prepspace.py", line 161, in speed_onset
    ipk = int(np.argmax(sp))
              ~~~~~~~~~^^^^
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/fromnumeric.py", line 1352, in argmax
    return _wrapfunc(a, 'argmax', axis=axis, out=out, **kwds)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/fromnumeric.py", line 54, in _wrapfunc
    return bound(*args, **kwds)
ValueError: attempt to get argmax of an empty sequence
```

**Agent**

Hand timestamps are not a continuous 1 kHz grid from 0 (1.45M samples over 1485 s). Checking the gaps.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import sys; sys.path.insert(0,'.')
import prepspace as ps, numpy as np
d=ps.load_train(); ts=d['hand']['t']; dt=np.diff(ts)
print(ts[0],ts[-1],len(ts)); print(np.unique(np.round(dt,4),return_counts=True))
t=d['trials']
# are samples within trials only?
i=np.searchsorted(t.start_time.values, ts, side='right')-1
print('outside trials', np.sum(ts>t.stop_time.values[i]+1e-9))
print(np.isnan(d['hand']['hand_pos']).sum(0), np.isnan(d['hand']['hand_vel']).sum(0))
EOF
```

```
0.0 1485.02 1453340
(array([0.001, 0.015, 0.02 , 0.025, 0.03 , 0.035, 0.04 , 0.045, 0.05 ,
       0.055, 0.06 , 0.065, 0.07 , 0.075, 0.08 , 0.085, 0.09 , 0.095,
       0.1  , 0.105, 0.11 ]), array([1452840,      20,      25,      19,      34,      15,      25,
            22,      22,      28,      25,      21,      32,      29,
            20,      24,      27,      26,      30,      28,      27]))
outside trials 0
[0 0] [0 0]
```

**Agent**

Hand samples exist only inside trials, at 1 ms. I'll index by timestamp.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
s=open('prepspace.py').read()
s=s.replace('''def _segment(x, centre_s, window_ms):
    i = int(round(centre_s * 1000))
    return x[i + window_ms[0]: i + window_ms[1]]''','''def _segment(hand, key, centre_s, window_ms):
    """Samples of hand[key] from window_ms[0] to window_ms[1] ms around centre_s. Hand samples
    exist only within trials, at 1 ms, so the window is found by timestamp; it must lie within
    the trial."""
    i = int(np.searchsorted(hand["t"], centre_s - 0.0005))
    seg = hand[key][i + window_ms[0]: i + window_ms[1]]
    tt = hand["t"][i + window_ms[0]: i + window_ms[1]]
    assert np.allclose(np.diff(tt), 0.001, atol=1e-6), "window crosses a trial boundary"
    return seg''')
s=s.replace('''    i0 = int(round(go_s * 1000))
    v = hand["hand_vel"][i0:i0 + search_ms]
    sp = np.hypot(v[:, 0], v[:, 1])
    ipk = int(np.argmax(sp))
    below = np.nonzero(sp[:ipk] < fraction * sp[ipk])[0]
    j = below[-1] + 1 if len(below) else 0
    return hand["t"][i0 + j]''','''    i0 = int(np.searchsorted(hand["t"], go_s - 0.0005))
    i1 = i0 + int(np.searchsorted(np.diff(hand["t"][i0:i0 + search_ms]), 0.0015))
    v = hand["hand_vel"][i0:i1]
    sp = np.hypot(v[:, 0], v[:, 1])
    ipk = int(np.argmax(sp))
    below = np.nonzero(sp[:ipk] < fraction * sp[ipk])[0]
    j = below[-1] + 1 if len(below) else 0
    return hand["t"][i0 + j]''')
s=s.replace('''prof = np.stack([_segment(hv, onset[i], T_WINDOW) for i in idx])''','''prof = np.stack([_segment(data["hand"], "hand_vel", onset[i], T_WINDOW) for i in idx])''')
s=s.replace('''    hv = data["hand"]["hand_vel"]
''','')
s=s.replace('''def hand_condition_means(data, onset, mask, window=(-200, 1000)):''','''def hand_condition_means(data, onset, mask, window=(-200, 950)):''')
s=s.replace('''pos.append(np.mean([_segment(data["hand"]["hand_pos"], onset[i], window) for i in idx], 0))
        vel.append(np.mean([_segment(data["hand"]["hand_vel"], onset[i], window) for i in idx], 0))''','''pos.append(np.mean([_segment(data["hand"], "hand_pos", onset[i], window) for i in idx], 0))
        vel.append(np.mean([_segment(data["hand"], "hand_vel", onset[i], window) for i in idx], 0))''')
open('prepspace.py','w').write(s)
EOF
python $TMPDIR/dev1.py
```

```
load 3.1746537685394287
onset diff b-a ms count    500.000000
mean      14.408000
std        6.841868
min      -74.000000
25%       10.000000
50%       14.000000
75%       18.000000
max       39.000000
dtype: float64
a each a kept 325 of 401 min per cond 3
a each b kept 332 of 401 min per cond 3
a concat a kept 386 of 401 min per cond 11
a concat b kept 386 of 401 min per cond 11
b each a kept 317 of 401 min per cond 2
b each b kept 326 of 401 min per cond 3
b concat a kept 380 of 401 min per cond 10
b concat b kept 382 of 401 min per cond 11
rates 14.619319200515747
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/dev2.py <<'EOF'
import time, pickle, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import prepspace as ps
from scipy import stats
data,on,R=pickle.load(open('/tmp/claude-1001/cache.pkl','rb'))
t=data['trials']
for proto,comb,o in [('a','each','a'),('a','concat','a'),('b','concat','b')]:
    m,_=ps.select_trials(data,on[o],proto,comb)
    prep=ps.condition_means(R['prep'],t,m)
    mv=ps.condition_means(R['move'][o],t,m)   # units x cond x time
    peri=ps.epoch_mean(mv,ps.PERI_WINDOW)
    for tun in 'ab':
        tp=ps.tuning(prep,tun); tq=ps.tuning(peri,tun)
        inc=tp>5; inc4=inc&(tq>=1.5*tp)
        r,rs=ps.corr_pearson_spearman(prep[inc4],peri[inc4])
        print(proto,comb,o,tun,'incl',inc.sum(),'fig4',inc4.sum(),'r',r.mean().round(3),'rs',rs.mean().round(3),'p',stats.ttest_1samp(r,0).pvalue.round(4))
EOF
python $TMPDIR/dev2.py
```

```
Exit code 1
a each a a incl 101 fig4 22 r 0.134 rs 0.165 p 0.0845
Traceback (most recent call last):
  File "/tmp/claude-1001/dev2.py", line 15, in <module>
    r,rs=ps.corr_pearson_spearman(prep[inc4],peri[inc4])
         ~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/000138-churchland-2010/prepspace.py", line 428, in corr_pearson_spearman
    ra = np.apply_along_axis(rankdata, 1, a)
  File "/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/lib/_shape_base_impl.py", line 385, in apply_along_axis
    raise ValueError(
        'Cannot apply_along_axis when any iteration dimensions are 0'
    ) from None
ValueError: Cannot apply_along_axis when any iteration dimensions are 0
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && sed -i 's/    ra = np.apply_along_axis(rankdata, 1, a)\n//' prepspace.py && python - <<'EOF'
s=open('prepspace.py').read()
s=s.replace('''    ra = np.apply_along_axis(rankdata, 1, a)
    rb = np.apply_along_axis(rankdata, 1, b)''','''    ra, rb = rankdata(a, axis=1), rankdata(b, axis=1)''')
open('prepspace.py','w').write(s)
EOF
python $TMPDIR/dev2.py
```

```
/tmp/claude-1001/dev2.py:16: RuntimeWarning: Mean of empty slice
  print(proto,comb,o,tun,'incl',inc.sum(),'fig4',inc4.sum(),'r',r.mean().round(3),'rs',rs.mean().round(3),'p',stats.ttest_1samp(r,0).pvalue.round(4))
/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
/tmp/claude-1001/dev2.py:16: SmallSampleWarning: One or more sample arguments is too small; all returned values will be NaN. See documentation for sample size requirements.
  print(proto,comb,o,tun,'incl',inc.sum(),'fig4',inc4.sum(),'r',r.mean().round(3),'rs',rs.mean().round(3),'p',stats.ttest_1samp(r,0).pvalue.round(4))
a each a a incl 101 fig4 22 r 0.134 rs 0.165 p 0.0845
a each a b incl 7 fig4 0 r nan rs nan p nan
a concat a a incl 92 fig4 20 r 0.195 rs 0.212 p 0.0233
a concat a b incl 6 fig4 0 r nan rs nan p nan
b concat b a incl 92 fig4 19 r 0.105 rs 0.146 p 0.2046
b concat b b incl 6 fig4 0 r nan rs nan p nan
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat > $TMPDIR/dev3.py <<'EOF'
import time, pickle, numpy as np, pandas as pd, sys
sys.path.insert(0,'.')
import prepspace as ps
data,on,R=pickle.load(open('/tmp/claude-1001/cache.pkl','rb'))
t=data['trials']
o='a'; m,_=ps.select_trials(data,on[o],'a','each')
prep=ps.condition_means(R['prep'],t,m)
mv=ps.condition_means(R['move'][o],t,m)
Tn=mv[:,:,ps.T_WINDOW[0]-ps.MOVE_TRACE[0]:ps.T_WINDOW[1]-ps.MOVE_TRACE[0]].astype(float)
inc=ps.tuning(prep,'a')>5
Gp=ps.neuron_grams(Tn); G=Gp.sum(0)
X=prep[inc]
K=14
for fold in ['once','refit']:
    t0=time.time(); err=ps.loo_pca_space(G,Gp[inc],X,K,fold); print(fold,time.time()-t0)
    perf=np.array([ps.performance(err[:,k],X) for k in range(K)])
    print(np.round(perf.mean(1),3))
pos,vel,times=ps.hand_condition_means(data,on[o],m)
for end in ['speed','fixed']:
  for split in ['length','time']:
    sp,ends=ps.task_spaces(pos,vel,times,t,end,split)
    print(end,split,{k:round(ps.performance(ps.loo_errors_fixed(v,X),X).mean(),3) for k,v in sp.items()})
print('reach end ms', times[ends] if False else times[ps.reach_end_index(vel,times)])
for kend in [ps.T_WINDOW[1], times[ps.reach_end_index(vel,times)].max()+1]:
    KT=ps.kinematic_matrix(pos,vel,times,kend); Gk=KT@KT.T
    for fold in ['once','refit']:
        err=ps.loo_pca_space(Gk,None,X,K,fold)
        print('kin',kend,fold,np.round([ps.performance(err[:,k],X).mean() for k in range(K)],3))
EOF
python $TMPDIR/dev3.py
```

```
Exit code 1
once 0.14750289916992188
[ 0.026  0.071  0.08   0.05   0.094  0.15   0.132 -0.183 -0.425 -1.666
 -1.756 -1.71  -1.838 -3.102]
refit 2.4237990379333496
[0.027 0.08  0.093 0.09  0.103 0.16  0.227 0.256 0.29  0.308 0.307 0.349
 0.353 0.36 ]
Traceback (most recent call last):
  File "/tmp/claude-1001/dev3.py", line 21, in <module>
    sp,ends=ps.task_spaces(pos,vel,times,t,end,split)
            ~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "entries/000138-churchland-2010/prepspace.py", line 309, in task_spaces
    segs = np.concatenate([path[cuts3[j + 1]] - path[cuts3[j]] for j in range(3)])
                           ~~~~^^^^^^^^^^^^^^
IndexError: index 469 is out of bounds for axis 0 with size 469
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
s=open('prepspace.py').read()
s=s.replace('''    return [int(np.searchsorted(seg, seg[-1] * j / n)) for j in range(n + 1)]''','''    return [min(int(np.searchsorted(seg, seg[-1] * j / n)), len(path) - 1) for j in range(n + 1)]''')
s=s.replace('''        return [int(round(len(path) - 1) * j / n) for j in range(n + 1)]''','''        return [int(round((len(path) - 1) * j / n)) for j in range(n + 1)]''')
open('prepspace.py','w').write(s)
EOF
python - <<'EOF'
import sys; sys.path.insert(0,'.')
import numpy as np, prepspace as ps
rng=np.random.default_rng(0)
c,p=27,300; T=rng.standard_normal((c,p))*np.linspace(3,0.1,p); x=rng.standard_normal(c)
G=T@T.T; K=6
e1=ps.loo_errors_refit_gram(G,x,K)
e2=np.zeros((K,c))
for i in range(c):
    tr=np.r_[0:i,i+1:c]; m=T[tr].mean(0); U,s,Vt=np.linalg.svd(T[tr]-m,full_matrices=False)
    sc=(T[tr]-m)@Vt[:K].T; te=(T[i]-m)@Vt[:K].T
    for k in range(1,K+1):
        D=np.column_stack([np.ones(c-1),sc[:,:k]]); b=np.linalg.lstsq(D,x[tr],rcond=None)[0]
        e2[k-1,i]=x[i]-(b[0]+te[:k]@b[1:])
print('refit max diff',np.abs(e1-e2).max())
# once: hat identity vs explicit
S=ps._scores_from_gram(ps.centre_gram(G),K)[0]
ea=ps.loo_errors_fixed(S[:,:4],x[None])[0]
eb=[]
for i in range(c):
    tr=np.r_[0:i,i+1:c]; D=np.column_stack([np.ones(c-1),S[tr,:4]]); b=np.linalg.lstsq(D,x[tr],rcond=None)[0]; eb.append(x[i]-(b[0]+S[i,:4]@b[1:]))
print('once max diff',np.abs(ea-np.array(eb)).max())
U,s,Vt=np.linalg.svd(T-T.mean(0),full_matrices=False); print('scores match', np.allclose(np.abs(S),np.abs(U[:,:K]*s[:K])))
EOF
```

```
refit max diff 2.708944180085382e-14
once max diff 2.220446049250313e-15
scores match True
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python $TMPDIR/dev3.py 2>&1 | tail -12; date -u
```

```
fixed length {'initial velocity': np.float64(0.054), 'endpoints + max speed': np.float64(-0.016), 'endpoints + orthogonal excursion': np.float64(0.016), 'endpoints + viapoint': np.float64(0.086), 'endpoints + max velocity': np.float64(-0.13), 'endpoints + halfpoint': np.float64(0.063), 'segment directions': np.float64(0.064), 'kitchen sink': np.float64(-0.081)}
fixed time {'initial velocity': np.float64(0.054), 'endpoints + max speed': np.float64(-0.016), 'endpoints + orthogonal excursion': np.float64(0.016), 'endpoints + viapoint': np.float64(0.086), 'endpoints + max velocity': np.float64(-0.13), 'endpoints + halfpoint': np.float64(-0.036), 'segment directions': np.float64(-0.057), 'kitchen sink': np.float64(-0.097)}
reach end ms [271 380 370 269 441 485 271 468 470 270 437 443 271 426 444 307 392 393
 266 351 346 276 340 340 335 466 458]
kin 800 once [ 0.035  0.034  0.063  0.068  0.04   0.016  0.005  0.007 -0.024 -0.052
 -0.244 -0.29  -0.497 -0.579]
kin 800 refit [0.036 0.035 0.064 0.069 0.065 0.056 0.047 0.05  0.049 0.065 0.03  0.04
 0.035 0.043]
kin 486 once [ 0.033  0.043  0.068  0.074  0.054  0.031  0.016  0.011 -0.008 -0.041
 -0.226 -0.294 -0.497 -0.555]
kin 486 refit [0.033 0.043 0.068 0.073 0.076 0.064 0.072 0.058 0.072 0.076 0.043 0.051
 0.047 0.048]
Wed Oct 28 19:55:17 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && cat >> prepspace.py <<'EOF'


# ----------------------------------------------------------------------------------------------
# Readings and the grid of PD performance

READINGS = {
    "proto": ["a", "b"],          # proto-trial: mean (a) or elementwise median (b) profile
    "combine": ["each", "concat"],  # r > 0.9 for horizontal and vertical each, or concatenated
    "onset": ["a", "b"],          # movement onset: trial table (a) or speed threshold (b)
    "tuning": ["a", "b"],         # tuning: range (a) or SD (b) of condition means
    "t_units": ["all", "included"],  # neurons entering the peri-movement T-matrix
    "fold": ["once", "refit"],    # PCA space computed once, or recomputed per left-out condition
    "norm": ["neuron", "pooled"],  # performance per neuron then mean (a), or pooled ratio (b)
    "kin_end": ["fixed", "speed"],  # kinematic window ends at +800 ms (a) or at the reach end (b)
    "task_end": ["speed", "fixed"],  # reach end for task spaces: speed threshold or +800 ms
    "split": ["length", "time"],  # halfpoint and segments by path length or by time
    "kmax": [14, 12],             # range of dimensionalities
}
MAIN = {k: v[0] for k, v in READINGS.items()}


def prepare(data, R, onsets, proto, combine, onset):
    """Condition means under one trial-selection reading."""
    t = data["trials"]
    mask, r = select_trials(data, onsets[onset], proto, combine)
    pos, vel, times = hand_condition_means(data, onsets[onset], mask)
    return {"mask": mask, "r": r, "prep": condition_means(R["prep"], t, mask),
            "move": condition_means(R["move"][onset], t, mask), "pos": pos, "vel": vel,
            "times": times, "trials": t}


def t_matrix(move, start=T_WINDOW[0], stop=T_WINDOW[1]):
    return move[:, :, start - MOVE_TRACE[0]: stop - MOVE_TRACE[0]].astype(float)


def peri_errors(ctx, inc, t_units, fold, kmax=14, start=T_WINDOW[0], move=None):
    """Errors (n_inc x kmax x c) of the PD in the peri-movement space built from every neuron in
    the T-matrix except the one being fit (Methods, PCA-based spaces)."""
    move = ctx["move"] if move is None else move
    Gp = neuron_grams(t_matrix(move, start))
    in_t = np.ones(len(inc), bool) if t_units == "all" else inc
    G = Gp[in_t].sum(0)
    parts = Gp[inc] * in_t[inc][:, None, None]
    return loo_pca_space(G, parts, ctx["prep"][inc], kmax, fold)


def kinematic_end_ms(ctx, kin_end):
    if kin_end == "fixed":
        return T_WINDOW[1]
    return int(ctx["times"][reach_end_index(ctx["vel"], ctx["times"])].max()) + 1


def kinematic_errors(ctx, inc, fold, kin_end, kmax=14):
    KT = kinematic_matrix(ctx["pos"], ctx["vel"], ctx["times"], kinematic_end_ms(ctx, kin_end))
    return loo_pca_space(KT @ KT.T, None, ctx["prep"][inc], kmax, fold)


def task_errors(ctx, inc, task_end, split):
    spaces, _ = task_spaces(ctx["pos"], ctx["vel"], ctx["times"], ctx["trials"], task_end, split)
    X = ctx["prep"][inc]
    return {name: loo_errors_fixed(S, X) for name, S in spaces.items()}, \
        {name: S.shape[1] for name, S in spaces.items()}


def perf_both(err, X):
    return {"neuron": float(np.mean(performance(err, X))),
            "pooled": float(performance(err, X, pooled=True))}
EOF
cat > $TMPDIR/dev4.py <<'EOF'
import time, pickle, numpy as np, pandas as pd, sys, itertools
sys.path.insert(0,'.')
import prepspace as ps
data,on,R=pickle.load(open('/tmp/claude-1001/cache.pkl','rb'))
t0=time.time()
ctx=ps.prepare(data,R,on,'a','each','a'); print('prepare',time.time()-t0)
inc=ps.tuning(ctx['prep'],'a')>5
for fold in ['once','refit']:
    t0=time.time(); e=ps.peri_errors(ctx,inc,'all',fold); print(fold,time.time()-t0, [round(ps.perf_both(e[:,k],ctx['prep'][inc])['neuron'],3) for k in range(14)])
    t0=time.time(); e=ps.kinematic_errors(ctx,inc,fold,'speed'); print('kin',fold,time.time()-t0)
EOF
python $TMPDIR/dev4.py
```

```
prepare 0.20745635032653809
once 0.1609492301940918 [0.026, 0.071, 0.08, 0.05, 0.094, 0.15, 0.132, -0.183, -0.425, -1.666, -1.756, -1.71, -1.838, -3.102]
kin once 0.14593720436096191
refit 2.47765851020813 [0.027, 0.08, 0.093, 0.09, 0.103, 0.16, 0.227, 0.256, 0.29, 0.308, 0.307, 0.349, 0.353, 0.36]
kin refit 2.4283406734466553
```

**Agent**

The "once" collapse at k ≥ 8 may come from conditions left with very few trials under the "each" selection (minimum 3). Checking under the concatenated selection.

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
import pickle, numpy as np, sys
sys.path.insert(0,'.')
import prepspace as ps
data,on,R=pickle.load(open('/tmp/claude-1001/cache.pkl','rb'))
for comb in ['each','concat']:
    ctx=ps.prepare(data,R,on,'a',comb,'a'); inc=ps.tuning(ctx['prep'],'a')>5
    e=ps.peri_errors(ctx,inc,'all','once'); print(comb, [round(ps.perf_both(e[:,k],ctx['prep'][inc])['neuron'],3) for k in range(14)])
    X=ctx['prep'][inc]; worst=(e[:,9]**2).mean(0)/X.var(1).mean(); print(' per-cond err k=10', np.round(worst,1))
    print(' trials per cond', np.bincount(data['trials'].cond_idx[ctx['mask']]))
EOF
```

```
each [0.026, 0.071, 0.08, 0.05, 0.094, 0.15, 0.132, -0.183, -0.425, -1.666, -1.756, -1.71, -1.838, -3.102]
 per-cond err k=10 [ 1.2  0.3  0.3  0.5  0.4  0.8  4.1  0.2  0.3  0.3  0.3  0.4  0.3  0.3
  0.6  0.7  0.6  0.3  0.5  0.4  0.3  0.4  0.6  0.4 38.3  0.3  0.6]
 trials per cond [ 9 13 14 12 13 10  6 14 14 13 14 11 14 13  8 14 10 14 12 12 17 11 10 15
  3 15 14]
concat [0.056, 0.124, 0.126, 0.163, 0.238, 0.277, 0.336, 0.35, 0.348, 0.351, 0.322, 0.251, -0.047, -0.456]
 per-cond err k=10 [1.1 0.3 0.3 0.4 0.3 0.5 0.4 0.2 0.3 0.3 0.3 0.4 0.3 0.5 0.8 0.6 0.5 0.3
 0.4 0.3 0.3 0.5 0.6 0.4 0.8 0.3 0.5]
 trials per cond [15 14 17 13 13 14 14 15 14 15 17 12 15 13 13 14 11 16 13 14 18 14 11 16
 12 16 17]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && python - <<'EOF'
s=open('prepspace.py').read()
s=s.replace('''    "combine": ["each", "concat"],  # r > 0.9 for horizontal and vertical each, or concatenated''','''    "combine": ["concat", "each"],  # r > 0.9 for the concatenated profile, or for each axis''')
open('prepspace.py','w').write(s)
EOF
ls ../../tools; sed -n 1,80p ../../tools/entry.py | head -120; date -u
```

```
__pycache__
agent_run.py
archive_transcripts.sh
archives
blind.sh
build_dryad_targets.py
build_figshare_targets.py
build_openneuro_targets.py
build_site.py
build_targets.py
claims_check.py
conversion_issue.py
datasets.py
entry.py
flagged.py
get_papers.sh
notify.py
paper_match.py
papers_manifest.py
progress.py
[... 88 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build_nb.py",
 "content": "\"\"\"Build the notebook from a percent-format source. Cells start with '# %%' (code) or\n'# %% [markdown]'; tags with 'tags=a,b'.\"\"\"\nimport re\nimport sys\n\nimport nbformat\n\nsrc = open(sys.argv[1]).read()\nout = sys.argv[2]\ncells = []\nfor block in re.split(r\"^# %%\", src, flags=re.M)[1:]:\n    head, _, body = block.partition(\"\\n\")\n    tags = []\n    m = re.search(r\"tags=([\\w:,\\-]+)\", head)\n    if m:\n        tags = m.group(1).split(\",\")\n    body = body.strip(\"\\n\")\n    if \"[markdown]\" in head:\n        text = \"\\n\".join(l[2:] if l.startswith(\"# \") else l.lstrip(\"#\") for l in body.splitlines())\n        cells.append(nbformat.v4.new_markdown_cell(text))\n    else:\n        c = nbformat.v4.new_code_cell(body)\n        if tags:\n            c.metadata[\"tags\"] = tags\n        cells.append(c)\nnb = nbformat.v4.new_notebook(cells=cells)\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbformat.write(nb, out)\nprint(len(cells), \"cells\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/build_nb.py (file state is current in your context — no need to Read it back)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb.py",
 "content": "# %% [markdown]\n# # Reproducing Churchland et al. (2010) from dandiset 000138\n#\n# HEADER\n\n# %%\nimport itertools\nimport time\nimport warnings\n\nimport matplotlib.pyplot as plt\nimport numpy as np\nimport pandas as pd\nimport requests\nfrom scipy import stats\n\nimport prepspace as ps\n\npd.set_option(\"display.width\", 220)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 300)\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\n\nstarted = time.time()\ndata = ps.load_train()\ntrials, units, spikes, hand = data[\"trials\"], data[\"units\"], data[\"spikes\"], data[\"hand\"]\nprint(f\"loaded dandiset {ps.DANDISET_ID} version {ps.DANDISET_VERSION}, {ps.TRAIN_PATH}, \"\n      f\"in {time.time() - started:.0f} s\")\n\n# %% [markdown]\n# ## Data check\n#\n# The archive's listing of the pinned version and of the draft, and the file's metadata.\n\n# %% tags=sanity\napi = \"https://api.dandiarchive.org/api/dandisets/000138\"\nversions = requests.get(f\"{api}/versions/\").json()[\"results\"]\nprint(\"Versions:\", [(v[\"version\"], v[\"asset_count\"], v[\"size\"]) for v in versions])\nfor v in [\"0.220113.0407\", \"draft\"]:\n    assets = requests.get(f\"{api}/versions/{v}/assets/\").json()[\"results\"]\n    print(v, [(a[\"path\"], a[\"size\"], a[\"blob\"]) for a in assets])\nmeta = requests.get(f\"{api}/versions/{ps.DANDISET_VERSION}/\").json()\nprint(\"\\nRelated resources:\", [(r[\"identifier\"], r[\"relation\"]) for r in meta[\"relatedResource\"]])\nprint(\"Description:\", meta[\"description\"])\nprint(\"\\nFile metadata:\", data[\"meta\"])\n\n# %% [markdown]\n# Both versions hold the same two blobs, so the published version is the draft's content. The\n# training file holds trials, units and behaviour; the test file holds 100 unlabelled trial\n# segments for the benchmark (checked below).\n\n# %% tags=sanity\nprint(\"Trials:\", len(trials), \"; success:\", trials.success.value_counts().to_dict(),\n      \"; split:\", trials.split.value_counts().to_dict())\nprint(\"Conditions (trial_type x trial_version):\", trials.condition.nunique(),\n      \"; maze_id values:\", trials.maze_id.nunique())\nprint(trials.groupby([\"trial_type\", \"trial_version\"]).size().unstack().to_string())\ncheck = trials.groupby(\"condition\").agg(maze_ids=(\"maze_id\", \"nunique\"),\n                                        barriers=(\"num_barriers\", lambda x: sorted(set(x))),\n                                        targets=(\"num_targets\", lambda x: sorted(set(x))),\n                                        active=(\"active_target\", lambda x: sorted(set(x))))\nprint(\"\\nPer condition, distinct maze_id, number of barriers, targets, active target index:\")\nprint(check.to_string())\nprint(\"\\ndelay field minus (go cue - target on) in ms, max abs:\",\n      float(np.abs(trials.delay - (trials.go_cue_time - trials.target_on_time) * 1000).max()))\nprint(\"rt field minus (move onset - go cue) in ms, max abs:\",\n      float(np.abs(trials.rt - (trials.move_onset_time - trials.go_cue_time) * 1000).max()))\nprint(\"Delay (ms) range:\", trials.delay.min(), \"to\", trials.delay.max(),\n      \"; trials with delay > 400 ms:\", int((trials.delay > 400).sum()))\nprint(\"RT (ms) range:\", trials.rt.min(), \"to\", trials.rt.max())\nprint(\"Target on after trial start (s):\", round((trials.target_on_time - trials.start_time).min(), 3),\n      \"to\", round((trials.target_on_time - trials.start_time).max(), 3))\nprint(\"Trial stop after movement onset (s):\", round((trials.stop_time - trials.move_onset_time).min(), 3),\n      \"to\", round((trials.stop_time - trials.move_onset_time).max(), 3))\n\n# %% [markdown]\n# The `delay` and `rt` fields agree with the event times to rounding. Each condition is one maze\n# (`maze_id`) in one version: version 0 has one target and no barriers, version 1 one target\n# with barriers, version 2 three targets with barriers, as the field descriptions say, and as the\n# Supplemental Experimental Procedures describe (straight reaches, curved reaches, and curved\n# reaches with distractors). The paper's J-array dataset had 108 conditions and a mean 2166\n# trials per neuron; this file has 27 conditions and 500 trials (about 18 per condition).\n\n# %% tags=sanity\nel = data[\"electrodes\"]\nprint(\"Electrodes:\", len(el), \"; by group:\", el.group_name.value_counts().to_dict(),\n      \"; x, y, z all NaN:\", bool(el[[\"x\", \"y\", \"z\"]].isna().all().all()))\nprint(\"Units:\", len(units), \"; heldout:\", units.heldout.value_counts().to_dict())\nprint(\"Location of the electrode each unit references:\", units.electrode_location.value_counts().to_dict())\nprint(\"Unit id = array * 1000 + channel * 10 + sort: id prefix counts\",\n      units.id_array.value_counts().sort_index().to_dict())\nprint(\"Channel in the id equals the referenced electrode index + 1 for every unit:\",\n      bool((units.id_channel == units.electrode + 1).all()))\nprint(\"Heldout units by id prefix:\", units.groupby(\"id_array\").heldout.sum().to_dict())\nn_spk = np.array([len(s) for s in spikes])\nprint(\"Spikes per unit:\", n_spk.min(), \"to\", n_spk.max(), \"; total\", n_spk.sum())\nprint(\"Spike times sorted in every unit:\", all(np.all(np.diff(s) >= 0) for s in spikes))\nstarts, stops = trials.start_time.values, trials.stop_time.values\nallsp = np.concatenate(spikes)\nk = np.searchsorted(starts, allsp, side=\"right\") - 1\nprint(\"Spikes outside the trial intervals:\", int(np.sum((k < 0) | (allsp > stops[np.clip(k, 0, None)]))))\ndur = (stops - starts).sum()\nrates = n_spk / dur\nprint(f\"Mean rate per unit over the trial intervals (spikes/s): {rates.min():.2f} to {rates.max():.2f}, \"\n      f\"median {np.median(rates):.2f}\")\n\n# %% [markdown]\n# The units' electrode references all point into the first 96 rows of the electrodes table,\n# the PMd group, and every electrode coordinate is NaN. The unit ids carry a prefix of 1 (83\n# units) or 2 (79 units) and the channel, and the referenced electrode is the channel minus\n# one for both prefixes, so the 79 units of prefix 2 reference PMd electrodes by the same channel\n# numbers as prefix 1. The heldout units are split 20 and 20 between the prefixes. The data\n# description says the units come from an M1 and a PMd array. The prefix is consistent with the\n# array a unit was recorded on, but which prefix is which array is not stated anywhere in the\n# files; that the references are wrong for one prefix is a finding.\n\n# %% tags=sanity\nhp, hv, ht = hand[\"hand_pos\"], hand[\"hand_vel\"], hand[\"t\"]\nfor name in [\"hand_pos\", \"hand_vel\", \"cursor_pos\", \"eye_pos\"]:\n    x = hand[name]\n    print(f\"{name}: stored unit {hand[name + '_unit']!r}, conversion {hand[name + '_conversion']}, \"\n          f\"description {hand[name + '_description']!r}; x {x[:, 0].min():.1f} to {x[:, 0].max():.1f}, \"\n          f\"y {x[:, 1].min():.1f} to {x[:, 1].max():.1f}\")\ndt = np.diff(ht)\nprint(\"Hand samples:\", len(ht), \"; interval within trials\", np.median(dt) * 1000, \"ms; samples outside trials:\",\n      int(np.sum(ht > stops[np.searchsorted(starts, ht, side='right') - 1] + 1e-9)))\n# velocity against the derivative of position, within trials\nwithin = np.r_[False, np.isclose(dt, 0.001)]\ndpos = np.r_[np.zeros((1, 2)), np.diff(hp, axis=0)] * 1000\nfast = within & (np.hypot(hv[:, 0], hv[:, 1]) > 100)\nfor d, ax in enumerate(\"xy\"):\n    r = np.corrcoef(dpos[fast, d], hv[fast, d])[0, 1]\n    slope = np.polyfit(dpos[fast, d], hv[fast, d], 1)[0]\n    print(f\"hand_vel {ax} against the derivative of hand_pos {ax} (samples above 100 mm/s): r = {r:.3f}, slope {slope:.3f}\")\n# reach endpoint against the active target\nend_err = []\nfor _, tr in trials.iterrows():\n    i = np.searchsorted(ht, tr.move_onset_time + 0.75)\n    target = np.asarray(tr.target_pos)[int(tr.active_target)]\n    end_err.append(np.hypot(*(hp[i] - target)))\nend_err = np.array(end_err)\nprint(f\"Hand 750 ms after movement onset to the active target (mm): median {np.median(end_err):.1f}, \"\n      f\"95th percentile {np.percentile(end_err, 95):.1f}, max {end_err.max():.1f}\")\n\n# %% [markdown]\n# Hand position is stored in millimetres with a conversion of 0.001 to metres, and velocity in\n# mm/s; velocity agrees with the derivative of position (slope near 1). Hand samples exist only\n# inside trials, at 1 ms; the paper tracked the hand at 60 Hz, so the 1 kHz series is\n# resampled. Hand positions 750 ms after movement onset lie near the active target, which ties\n# the hand, the target positions and the movement onset times together.\n#\n# Clock check. If spikes share the trial table's clock, the reach target can be decoded from\n# spike counts after target onset and not before it; if hand data share it, hand speed rises at\n# the table's movement onset. Target (one of 9 mazes, `trial_type`) is decoded with a\n# leave-one-trial-out nearest-centroid classifier on square-root spike counts (a standard\n# choice), in 200 ms windows. The same is done with the windows shifted 1 s earlier, which\n# moves every window before target onset.\n\n# %% tags=sanity\ndef decode(t0_s, window):\n    i0 = np.round((t0_s + window[0] / 1000) * 1000).astype(int)\n    counts = np.zeros((len(trials), len(spikes)))\n    for u, s in enumerate(spikes):\n        ms = np.floor(s * 1000).astype(int)\n        cs = np.r_[0, np.cumsum(np.bincount(ms, minlength=int(stops.max() * 1000) + 3000))]\n        counts[:, u] = cs[i0 + window[1] - window[0]] - cs[i0]\n    X = np.sqrt(counts)\n    y = trials.trial_type.values\n    labels = np.unique(y)\n    sums = np.stack([X[y == l].sum(0) for l in labels])\n    ns = np.array([(y == l).sum() for l in labels])\n    correct = 0\n    for i in range(len(y)):\n        li = np.searchsorted(labels, y[i])\n        cent = sums.copy()\n        cent[li] -= X[i]\n        nn = ns.copy()\n        nn[li] -= 1\n        cent = cent / nn[:, None]\n        correct += labels[np.argmin(((cent - X[i]) ** 2).sum(1))] == y[i]\n    return correct / len(y)\n\nclock = []\nfor name, ev, win in [(\"target onset\", trials.target_on_time.values, (-250, -50)),\n                      (\"target onset\", trials.target_on_time.values, (100, 300)),\n                      (\"go cue\", trials.go_cue_time.values, (-200, 0)),\n                      (\"movement onset\", trials.move_onset_time.values, (0, 200))]:\n    clock.append({\"event\": name, \"window_ms\": win, \"accuracy\": decode(ev, win),\n                  \"accuracy_window_1s_earlier\": decode(ev - 1.0, win) if name == \"target onset\" else np.nan})\nprint(\"Chance for 9 mazes about\", round(1 / 9, 3))\nprint(pd.DataFrame(clock).round(3).to_string(index=False))\nspeed_on = []\nfor tm in trials.move_onset_time.values:\n    i = np.searchsorted(ht, tm - 0.0005)\n    speed_on.append(np.hypot(*hv[i - 100:i + 101].T))\nspeed_on = np.array(speed_on)\nprint(\"Median hand speed (mm/s) at -100, -50, 0, +50, +100 ms from the table's movement onset:\",\n      np.round(np.median(speed_on, 0)[[0, 50, 100, 150, 200]], 1))\n\n# %% [markdown]\n# The test file: what it holds, and whether its segments duplicate training trials. A run of\n# five successive inter-spike intervals of a unit is looked up among the same unit's training\n# intervals (rounded to 0.1 ms).\n\n# %% tags=sanity\ntest = ps.load_test_summary()\nprint(\"Test file trial columns:\", test[\"trial_columns\"], \"; trials:\", test[\"n_trials\"],\n      \"; units:\", len(test[\"unit_ids\"]),\n      \"; unit ids all among the training file's held-in units:\",\n      set(test[\"unit_ids\"]) == set(units.id[~units.heldout]))\nprint(\"Segment durations (s):\", np.unique(np.round(test[\"stops\"] - test[\"starts\"], 3)))\nhits, tried = 0, 0\nfor uid, st in zip(test[\"unit_ids\"][:20], test[\"spikes\"][:20]):\n    train_isi = np.round(np.diff(spikes[int(np.nonzero(units.id.values == uid)[0][0])]) * 1e4).astype(int)\n    train_keys = {tuple(train_isi[i:i + 5]) for i in range(len(train_isi) - 4)}\n    isi = np.round(np.diff(st) * 1e4).astype(int)\n    for i in range(0, len(isi) - 4, 5):\n        tried += 1\n        hits += tuple(isi[i:i + 5]) in train_keys\nprint(f\"Runs of 5 test intervals found in the training intervals of the same unit: {hits} of {tried}\")\n\n# %% [markdown]\n# The test segments carry no condition, so the analysis uses the training file only (its\n# `train` and `val` trials, 500 in all).\n#\n# Trial selection under each reading (Methods: delay over 400 ms; Supplemental Experimental\n# Procedures: velocity profiles correlated with a proto-trial at r > 0.9, \"typically ~90% of all\n# trials\"). Movement onset reading (b) is the speed threshold crossing.\n\n# %% tags=sanity\nonsets = {\"a\": ps.onset_times(data, \"a\"), \"b\": ps.onset_times(data, \"b\")}\nd_on = (onsets[\"b\"] - onsets[\"a\"]) * 1000\nprint(f\"Onset (b) minus onset (a), ms: median {np.median(d_on):.0f}, 5th to 95th percentile \"\n      f\"{np.percentile(d_on, 5):.0f} to {np.percentile(d_on, 95):.0f}, range {d_on.min():.0f} to {d_on.max():.0f}\")\nt0 = time.time()\nR = ps.trial_rates(data, onsets)\nprint(f\"Smoothed rates computed in {time.time() - t0:.0f} s\")\nctxs = {}\nrows = []\nfor proto, combine, onset in itertools.product(ps.READINGS[\"proto\"], ps.READINGS[\"combine\"], ps.READINGS[\"onset\"]):\n    ctx = ps.prepare(data, R, onsets, proto, combine, onset)\n    ctxs[(proto, combine, onset)] = ctx\n    per = np.bincount(trials.cond_idx[ctx[\"mask\"]], minlength=27)\n    row = {\"proto\": proto, \"combine\": combine, \"onset\": onset, \"kept\": int(ctx[\"mask\"].sum()),\n           \"of_delay_over_400\": int((trials.delay > 400).sum()),\n           \"fraction\": ctx[\"mask\"].sum() / (trials.delay > 400).sum(),\n           \"min_per_condition\": per.min(), \"max_per_condition\": per.max()}\n    for tun in ps.READINGS[\"tuning\"]:\n        tp = ps.tuning(ctx[\"prep\"], tun)\n        row[f\"included_tuning_{tun}\"] = int((tp > ps.ARRAY_MIN_TUNING).sum())\n    rows.append(row)\nselection = pd.DataFrame(rows)\nprint(selection.round(3).to_string(index=False))\n\n# %% [markdown]\n# Requiring the horizontal and the vertical profile each to correlate at r > 0.9 (`each`)\n# keeps about 80% of trials and leaves as few as 2 or 3 trials in a condition: in reaches that\n# are nearly vertical or horizontal, one velocity component is small and its correlation with\n# the proto-trial is mostly noise. Correlating the concatenated profile (`concat`) keeps about\n# 95%. The paper reports \"typically ~90%\".\n#\n# Under the range reading of tuning (a) about 90 to 100 of the 162 units pass the array\n# criterion of more than 5 spikes/s; under the SD reading (b) only 6 or 7 do. Ranges and units\n# of the measures used:\n\n# %% tags=sanity\nctx = ctxs[(\"a\", \"concat\", \"a\")]\ntp_a, tp_b = ps.tuning(ctx[\"prep\"], \"a\"), ps.tuning(ctx[\"prep\"], \"b\")\nprint(f\"Preparatory condition means (spikes/s): {ctx['prep'].min():.2f} to {ctx['prep'].max():.2f}\")\nprint(f\"Preparatory tuning, range (spikes/s): {tp_a.min():.2f} to {tp_a.max():.2f}, median {np.median(tp_a):.2f}\")\nprint(f\"Preparatory tuning, SD (spikes/s): {tp_b.min():.2f} to {tp_b.max():.2f}, median {np.median(tp_b):.2f}\")\nperi = ps.epoch_mean(ctx[\"move\"], ps.PERI_WINDOW)\nprint(f\"Peri-movement condition means (spikes/s): {peri.min():.2f} to {peri.max():.2f}\")\ninc_a = tp_a > ps.ARRAY_MIN_TUNING\nprint(\"Included units (range reading) by id prefix:\", pd.Series(units.id_array[inc_a]).value_counts().sort_index().to_dict())\nprint(\"Median preparatory tuning (range) by id prefix:\",\n      pd.Series(tp_a).groupby(units.id_array.values).median().round(2).to_dict())\nprint(\"Median peri-movement tuning (range) by id prefix:\",\n      pd.Series(peri.max(1) - peri.min(1)).groupby(units.id_array.values).median().round(2).to_dict())\nprint(f\"Hand position, condition means (mm): x {ctx['pos'][..., 0].min():.0f} to {ctx['pos'][..., 0].max():.0f}, \"\n      f\"y {ctx['pos'][..., 1].min():.0f} to {ctx['pos'][..., 1].max():.0f}; \"\n      f\"peak speed {np.hypot(ctx['vel'][..., 0], ctx['vel'][..., 1]).max():.0f} mm/s\")\n\n# %% [markdown]\n# The paper found preparatory activity more prevalent at anterior sites (Results, Comparison of\n# anterior versus posterior sites). The prefix with more preparatory tuning would then be the\n# PMd array; this is printed above and used only as a consistency check of the assumption made\n# below that prefix 1 is PMd, the group the electrode references name.\n\n# %% [markdown]\n# ## Readings\n#\n# The claims file and the paper leave several method details open. Each is run. The first\n# value listed is the main reading, chosen as best supported by the paper (the reasons are in\n# the attempt record):\n#\n# - `proto`: proto-trial as the condition's mean (a) or elementwise median (b) velocity profile.\n# - `combine`: the r > 0.9 test on the concatenated horizontal and vertical profile, or on each.\n# - `onset`: movement onset from the trial table (a) or a speed threshold (b).\n# - `tuning`: preparatory tuning as the range (a) or SD (b) of condition means.\n# - `t_units`: all units (a) or only included units (b) in the peri-movement T-matrix.\n# - `fold`: PCA space computed once (a) or recomputed without the left-out condition (b).\n# - `norm`: performance per neuron, then averaged (a), or pooled (b).\n# - `kin_end`: kinematic window ends at +800 ms (a) or at the end of the reach (b).\n# - `task_end`: reach end by speed threshold (a) or at +800 ms (b), for task spaces.\n# - `split`: halfpoint and segments by path length (a) or time (b).\n# - `kmax`: dimensionalities 1 to 14 (a) or 1 to 12 (b).\n\n# %%\nprint(ps.MAIN)\n\n# %% [markdown]\n# ## fig4abc-tuning-correlation-single-electrode\n#\n# > In the three single-electrode datasets (monkeys A, B, J) the correlation across conditions\n# > between a neuron's preparatory and peri-movement firing rates is positive on average but\n# > small.\n#\n# Not tested: the dandiset holds only array data from monkey J. The single-electrode recordings\n# of monkeys A, B and J are not in it.\n\n# %% [markdown]\n# ## fig4d-tuning-correlation-j-array\n#\n# > In the J-array dataset the mean correlation between preparatory and peri-movement tuning is\n# > positive but small (mean r 0.13, p = 0.03; mean Spearman r 0.11).\n#\n# Per neuron, Pearson and Spearman correlation over the 27 conditions between preparatory\n# (go -200 to +100 ms) and peri-movement (movement onset -100 to +350 ms) rates, for units with\n# more than 5 spikes/s of preparatory tuning and peri-movement tuning at least 1.5 times that.\n# Tests of the mean against zero: (a) one-sample t-test on r, (b) the same on Fisher z, (c)\n# Wilcoxon signed-rank.\n\n# %% tags=claim:fig4d-tuning-correlation-j-array\ndef fig4_selection(ctx, tun, onset):\n    prep = ctx[\"prep\"]\n    peri = ps.epoch_mean(ctx[\"move\"], ps.PERI_WINDOW)\n    tp, tq = ps.tuning(prep, tun), ps.tuning(peri, tun)\n    inc = (tp > ps.ARRAY_MIN_TUNING) & (tq >= ps.PERI_RATIO * tp)\n    return inc, prep, peri\n\nrows = []\nfig4 = {}\nfor (proto, combine, onset), ctx in ctxs.items():\n    for tun in ps.READINGS[\"tuning\"]:\n        inc, prep, peri = fig4_selection(ctx, tun, onset)\n        row = {\"proto\": proto, \"combine\": combine, \"onset\": onset, \"tuning\": tun,\n               \"n_units\": int(inc.sum())}\n        if inc.sum() >= 3:\n            r, rs = ps.corr_pearson_spearman(prep[inc], peri[inc])\n            fig4[(proto, combine, onset, tun)] = (inc, r, rs)\n            row.update({\"mean_r\": r.mean(), \"mean_spearman\": rs.mean(),\n                        \"p_t\": stats.ttest_1samp(r, 0).pvalue,\n                        \"p_t_fisher\": stats.ttest_1samp(np.arctanh(np.clip(r, -0.999999, 0.999999)), 0).pvalue,\n                        \"p_wilcoxon\": stats.wilcoxon(r).pvalue})\n            row[\"r_within_tol\"] = abs(row[\"mean_r\"] - 0.13) <= 0.013\n            row[\"spearman_within_tol\"] = abs(row[\"mean_spearman\"] - 0.11) <= 0.011\n            row[\"positive_p05\"] = row[\"mean_r\"] > 0 and min(row[\"p_t\"], row[\"p_t_fisher\"], row[\"p_wilcoxon\"]) < 0.05\n        rows.append(row)\nfig4d = pd.DataFrame(rows)\nprint(\"Expected: mean r 0.13 +/- 0.013, mean Spearman 0.11 +/- 0.011, mean r > 0 at p < 0.05\")\nprint(fig4d.round(4).to_string(index=False))\nmain4 = fig4d[(fig4d.proto == \"a\") & (fig4d.combine == \"concat\") & (fig4d.onset == \"a\") & (fig4d.tuning == \"a\")].iloc[0]\nprint(\"\\nMain reading:\", main4.round(4).to_dict())\nok = fig4d.dropna(subset=[\"mean_r\"])\nprint(\"Readings with a result:\", len(ok), \"; both means within tolerance:\",\n      int((ok.r_within_tol & ok.spearman_within_tol).sum()), \"; mean r positive at p < 0.05:\", int(ok.positive_p05.sum()))\nprint(\"Range of mean r over readings with a result:\", round(ok.mean_r.min(), 3), \"to\", round(ok.mean_r.max(), 3),\n      \"; mean Spearman:\", round(ok.mean_spearman.min(), 3), \"to\", round(ok.mean_spearman.max(), 3))\n\n# %% tags=claim:fig4d-tuning-correlation-j-array\ninc, r, rs = fig4[(\"a\", \"concat\", \"a\", \"a\")]\nprint(\"Main reading, per-unit Pearson r: range\", round(r.min(), 3), \"to\", round(r.max(), 3),\n      \"; by id prefix:\", pd.Series(r).groupby(units.id_array.values[inc]).agg([\"count\", \"mean\"]).round(3).to_dict())\n# how the result moves with the peri-movement criterion\nfor ratio in [1.0, 1.25, 1.5, 2.0]:\n    ctx = ctxs[(\"a\", \"concat\", \"a\")]\n    prep = ctx[\"prep\"]; peri = ps.epoch_mean(ctx[\"move\"], ps.PERI_WINDOW)\n    tp, tq = ps.tuning(prep, \"a\"), ps.tuning(peri, \"a\")\n    sel = (tp > 5) & (tq >= ratio * tp)\n    rr, rrs = ps.corr_pearson_spearman(prep[sel], peri[sel])\n    print(f\"peri/prep tuning ratio >= {ratio}: {sel.sum()} units, mean r {rr.mean():.3f}, \"\n          f\"mean Spearman {rrs.mean():.3f}, t-test p {stats.ttest_1samp(rr, 0).pvalue:.4f}\")\nfig, ax = plt.subplots(figsize=(4, 3))\nax.hist(r, bins=np.linspace(-1, 1, 21), color=\"0.5\")\nax.axvline(r.mean(), color=\"r\")\nax.set_xlabel(\"Pearson r, preparatory vs peri-movement\")\nax.set_ylabel(\"units\")\nax.set_title(\"Main reading (all values inside the axes)\")\nplt.show()\n\n# %% [markdown]\n# ## fig4e-correlation-time-course\n#\n# > The correlation of preparatory tuning with peri-movement tuning measured at single time\n# > points starts to fall about 200 ms before movement onset and is near zero by movement onset.\n#\n# Same units as Figure 4D. The rate at each time point is taken from the movement-locked\n# average (the movement-locked part of the paper's spliced trace); the go-locked curve is shown\n# alongside.\n\n# %% tags=claim:fig4e-correlation-time-course\ntt = np.arange(*ps.MOVE_TRACE)\nrows = []\ncurves = {}\nfor key, (inc, r, rs) in fig4.items():\n    ctx = ctxs[key[:3]]\n    prep = ctx[\"prep\"][inc]\n    trace = ctx[\"move\"][inc]\n    pc = prep - prep.mean(1, keepdims=True)\n    tc = trace - trace.mean(1, keepdims=True)\n    curve = np.nanmean((pc[:, :, None] * tc).sum(1) / np.sqrt((pc ** 2).sum(1)[:, None] * (tc ** 2).sum(1)), 0)\n    curves[key] = curve\n    at = {ms: curve[ms - ps.MOVE_TRACE[0]] for ms in [-400, -300, -250, -200, -100, 0]}\n    rows.append({\"proto\": key[0], \"combine\": key[1], \"onset\": key[2], \"tuning\": key[3], \"n_units\": int(inc.sum()),\n                 **{f\"r_at_{ms}\": v for ms, v in at.items()},\n                 \"near_zero_at_0\": abs(at[0]) < 0.1, \"below_half_of_-250\": at[0] < 0.5 * at[-250],\n                 \"no_early_decline\": at[-300] >= 0.75 * at[-400]})\nfig4e = pd.DataFrame(rows)\nfig4e[\"criterion_met\"] = fig4e.near_zero_at_0 & fig4e.below_half_of_250 if False else (\n    fig4e[\"near_zero_at_0\"] & fig4e[\"below_half_of_-250\"] & fig4e[\"no_early_decline\"])\nprint(fig4e.round(3).to_string(index=False))\nprint(\"Readings meeting the criterion:\", int(fig4e.criterion_met.sum()), \"of\", len(fig4e))\nmain_curve = curves[(\"a\", \"concat\", \"a\", \"a\")]\nprint(\"Main reading, mean correlation every 50 ms from -600 to +400 ms:\")\nprint(pd.Series(main_curve[::50], index=tt[::50]).round(3).to_string())\n\n# %% tags=claim:fig4e-correlation-time-course\ninc = fig4[(\"a\", \"concat\", \"a\", \"a\")][0]\nctx = ctxs[(\"a\", \"concat\", \"a\")]\ngt = np.arange(-200, 500)\ngtrace = ps.condition_means(R[\"go_trace\"], trials, ctx[\"mask\"])[inc]\nprep = ctx[\"prep\"][inc]\npc = prep - prep.mean(1, keepdims=True)\ngc = gtrace - gtrace.mean(1, keepdims=True)\ngo_curve = np.nanmean((pc[:, :, None] * gc).sum(1) / np.sqrt((pc ** 2).sum(1)[:, None] * (gc ** 2).sum(1)), 0)\nprint(\"Go-locked mean correlation every 50 ms from -200 to +450 ms after the go cue:\")\nprint(pd.Series(go_curve[::50], index=gt[::50]).round(3).to_string())\nfig, axs = plt.subplots(1, 2, figsize=(8, 3), sharey=True)\naxs[0].plot(gt, go_curve, \"k\"); axs[0].set_xlabel(\"ms from go cue\")\naxs[1].plot(tt, main_curve, \"k\"); axs[1].set_xlabel(\"ms from movement onset\")\nfor a in axs:\n    a.axhline(0, color=\"0.7\"); a.set_ylim(-0.4, 1.05)\naxs[0].set_ylabel(\"mean r with preparatory rates\")\nplt.show()\nprint(\"Curve values outside the axes:\", int(np.sum((main_curve < -0.4) | (main_curve > 1.05)) + np.sum((go_curve < -0.4) | (go_curve > 1.05))))\n\n# %% [markdown]\n# ## results-ap-location-no-effect\n#\n# > The tuning correlation of Figure 4 does not depend on anterior-posterior recording location\n# > in any dataset (r = -0.05, -0.03, -0.07 and 0.20; p = 0.82, 0.85, 0.52 and 0.27).\n#\n# Only the J-array dataset can be tested. Electrode coordinates are NaN, so reading (a), the AP\n# coordinate of the electrode, cannot be run. Reading (b), array membership, needs the array of\n# each unit; it is taken from the unit id prefix, assuming prefix 1 is the PMd array (anterior,\n# coded 1) and prefix 2 the M1 array (posterior, coded 0). The per-unit Pearson r of Figure 4D\n# is regressed on that code; the slope's p-value is the paper's (r and p of the regression), and\n# p of 0.05 or more is \"no effect\" (assumed threshold, as the claims file says).\n\n# %% tags=claim:results-ap-location-no-effect\nrows = []\nfor key, (inc, r, rs) in fig4.items():\n    ap = (units.id_array.values[inc] == 1).astype(float)\n    if len(set(ap)) < 2:\n        continue\n    lr = stats.linregress(ap, r)\n    rows.append({\"proto\": key[0], \"combine\": key[1], \"onset\": key[2], \"tuning\": key[3],\n                 \"n_anterior\": int(ap.sum()), \"n_posterior\": int((1 - ap).sum()),\n                 \"mean_r_anterior\": r[ap == 1].mean(), \"mean_r_posterior\": r[ap == 0].mean(),\n                 \"regression_r\": lr.rvalue, \"p\": lr.pvalue, \"no_effect_p_ge_05\": lr.pvalue >= 0.05})\nap_tab = pd.DataFrame(rows)\nprint(ap_tab.round(3).to_string(index=False))\nprint(\"Readings with no effect (p >= 0.05):\", int(ap_tab.no_effect_p_ge_05.sum()), \"of\", len(ap_tab))\n\n# %% [markdown]\n# ## supp-preparatory-dimensionality\n#\n# > Depending on the dataset, 7 to 10 dimensions capture 90% of the variance of preparatory\n# > activity across conditions.\n#\n# PCA of the 27 x n matrix of preparatory condition means, rates not normalized; components\n# for 90% of variance. Units entering: (a) all, (b) included.\n\n# %% tags=claim:supp-preparatory-dimensionality\ndef n_for_90(M):\n    Mc = M - M.mean(0)\n    s = np.linalg.svd(Mc, compute_uv=False) ** 2\n    return int(np.searchsorted(np.cumsum(s) / s.sum(), 0.9) + 1), np.cumsum(s) / s.sum()\n\nrows = []\nfor (proto, combine, onset), ctx in ctxs.items():\n    M = ctx[\"prep\"].T\n    n_all, cum_all = n_for_90(M)\n    row = {\"proto\": proto, \"combine\": combine, \"onset\": onset, \"units_all\": M.shape[1], \"k90_all\": n_all}\n    for tun in ps.READINGS[\"tuning\"]:\n        inc = ps.tuning(ctx[\"prep\"], tun) > ps.ARRAY_MIN_TUNING\n        row[f\"units_included_{tun}\"] = int(inc.sum())\n        row[f\"k90_included_{tun}\"] = n_for_90(M[:, inc])[0]\n    rows.append(row)\ndim = pd.DataFrame(rows)\nprint(\"Expected: 7 to 10, widened to 6.3 to 11\")\nprint(dim.to_string(index=False))\n_, cum = n_for_90(ctxs[(\"a\", \"concat\", \"a\")][\"prep\"].T)\nprint(\"Main reading, all units, cumulative variance of the first 15 PCs:\", np.round(cum[:15], 3))\n# the same on a split of trials, to see how much of the 90% is trial noise\nrng = np.random.default_rng(4)\nctx = ctxs[(\"a\", \"concat\", \"a\")]\nhalf = ctx[\"mask\"] & (rng.random(len(trials)) < 0.5)\nother = ctx[\"mask\"] & ~half\nA = ps.condition_means(R[\"prep\"], trials, half).T\nB = ps.condition_means(R[\"prep\"], trials, other).T\nprint(\"Split halves of trials (seed 4): k90 =\", n_for_90(A)[0], \"and\", n_for_90(B)[0])\nprint(\"Trial counts per condition in each half:\", np.bincount(trials.cond_idx[half], minlength=27).min(), \"to\",\n      np.bincount(trials.cond_idx[half], minlength=27).max())\n\n# %% [markdown]\n# ## PD performance in each space (Figure 6, J-array)\n#\n# One grid of PD performance serves the Figure 6 claims and Figure 7B. For each trial-selection\n# and tuning reading, the leave-one-condition-out performance of every included unit is\n# computed in the peri-movement space (k = 1 to 14, window from -150 ms, and from 0 ms for\n# Figure 7B), the kinematic space (k = 1 to 14) and the eight maze task spaces. EMG was not\n# recorded for J-array, and `targets + instructed speed` does not exist for the maze task.\n\n# %% tags=claim:fig6-peri-movement-space-best\nt0 = time.time()\nperi_rows, kin_rows, task_rows = [], [], []\nfor (proto, combine, onset), ctx in ctxs.items():\n    for tun in ps.READINGS[\"tuning\"]:\n        inc = ps.tuning(ctx[\"prep\"], tun) > ps.ARRAY_MIN_TUNING\n        X = ctx[\"prep\"][inc]\n        base = {\"proto\": proto, \"combine\": combine, \"onset\": onset, \"tuning\": tun, \"n_units\": int(inc.sum())}\n        for t_units in ps.READINGS[\"t_units\"]:\n            for fold in ps.READINGS[\"fold\"]:\n                for start in [-150, 0]:\n                    err = ps.peri_errors(ctx, inc, t_units, fold, 14, start)\n                    for k in range(1, 15):\n                        pf = ps.perf_both(err[:, k - 1], X)\n                        for norm in ps.READINGS[\"norm\"]:\n                            peri_rows.append({**base, \"t_units\": t_units, \"fold\": fold, \"start\": start,\n                                              \"k\": k, \"norm\": norm, \"perf\": pf[norm]})\n        for fold in ps.READINGS[\"fold\"]:\n            for kin_end in ps.READINGS[\"kin_end\"]:\n                err = ps.kinematic_errors(ctx, inc, fold, kin_end)\n                for k in range(1, 15):\n                    pf = ps.perf_both(err[:, k - 1], X)\n                    for norm in ps.READINGS[\"norm\"]:\n                        kin_rows.append({**base, \"fold\": fold, \"kin_end\": kin_end, \"k\": k, \"norm\": norm, \"perf\": pf[norm]})\n        for task_end in ps.READINGS[\"task_end\"]:\n            for split in ps.READINGS[\"split\"]:\n                errs, dims = ps.task_errors(ctx, inc, task_end, split)\n                for name, err in errs.items():\n                    pf = ps.perf_both(err, X)\n                    for norm in ps.READINGS[\"norm\"]:\n                        task_rows.append({**base, \"task_end\": task_end, \"split\": split, \"space\": name,\n                                          \"k\": dims[name], \"norm\": norm, \"perf\": pf[norm]})\nperi_df, kin_df, task_df = pd.DataFrame(peri_rows), pd.DataFrame(kin_rows), pd.DataFrame(task_rows)\nprint(f\"Grid computed in {time.time() - t0:.0f} s: {len(peri_df)} peri-movement, {len(kin_df)} kinematic, \"\n      f\"{len(task_df)} task-space values\")\n\n# %% [markdown]\n# ### fig6-peri-movement-space-best\n#\n# > For every dataset, preferred directions capture preparatory tuning best (highest\n# > cross-validated performance) when expressed in the peri-movement space, usually at middle\n# > dimensionalities.\n#\n# Reproduced when the peri-movement space's best mean performance over k is higher than that of\n# every other space under one combination of the readings.\n\n# %% tags=claim:fig6-peri-movement-space-best\nPREP_KEYS = [\"proto\", \"combine\", \"onset\", \"tuning\"]\n\ndef combos():\n    names = [\"proto\", \"combine\", \"onset\", \"tuning\", \"t_units\", \"fold\", \"norm\", \"kin_end\", \"task_end\", \"split\", \"kmax\"]\n    for vals in itertools.product(*[ps.READINGS[n] for n in names]):\n        yield dict(zip(names, vals))\n\npi = peri_df[peri_df.start == -150].set_index(PREP_KEYS + [\"t_units\", \"fold\", \"norm\", \"k\"]).perf.sort_index()\npi0 = peri_df[peri_df.start == 0].set_index(PREP_KEYS + [\"t_units\", \"fold\", \"norm\", \"k\"]).perf.sort_index()\nki = kin_df.set_index(PREP_KEYS + [\"fold\", \"kin_end\", \"norm\", \"k\"]).perf.sort_index()\nti = task_df.set_index(PREP_KEYS + [\"task_end\", \"split\", \"norm\", \"space\"]).sort_index()\n\ndef curves_for(c):\n    pk = tuple(c[k] for k in PREP_KEYS)\n    ks = np.arange(1, c[\"kmax\"] + 1)\n    peri = pi.loc[pk + (c[\"t_units\"], c[\"fold\"], c[\"norm\"])].loc[ks]\n    peri0 = pi0.loc[pk + (c[\"t_units\"], c[\"fold\"], c[\"norm\"])].loc[ks]\n    kin = ki.loc[pk + (c[\"fold\"], c[\"kin_end\"], c[\"norm\"])].loc[ks]\n    task = ti.loc[pk + (c[\"task_end\"], c[\"split\"], c[\"norm\"])]\n    return peri, peri0, kin, task\n\nrows = []\nfor c in combos():\n    peri, peri0, kin, task = curves_for(c)\n    best_other = max(kin.max(), task.perf.max())\n    rows.append({**c, \"n_units\": int(peri_df[(peri_df[PREP_KEYS] == pd.Series({k: c[k] for k in PREP_KEYS})).all(1)].n_units.iloc[0])\n                 if False else None,\n                 \"peri_best\": peri.max(), \"peri_best_k\": int(peri.idxmax()), \"peri_k1\": peri.loc[1],\n                 \"peri_kmax\": peri.loc[c[\"kmax\"]],\n                 \"kin_best\": kin.max(), \"kin_best_k\": int(kin.idxmax()), \"kin_k1\": kin.loc[1], \"kin_kmax\": kin.loc[c[\"kmax\"]],\n                 \"task_best\": task.perf.max(), \"task_best_space\": task.perf.idxmax(),\n                 \"n_task_above_0\": int((task.perf > 0).sum()),\n                 \"peri0_best\": peri0.max(), \"peri0_best_k\": int(peri0.idxmax()),\n                 \"peri_beats_all\": peri.max() > best_other, \"margin\": peri.max() - best_other})\ngrid = pd.DataFrame(rows).drop(columns=\"n_units\")\nMAIN = ps.MAIN\nis_main = (grid[list(MAIN)] == pd.Series(MAIN)).all(1)\nprint(\"Combinations of readings:\", len(grid), \"; peri-movement space best in\", int(grid.peri_beats_all.sum()))\nprint(\"\\nMain reading:\")\nprint(grid[is_main].T.to_string())\nprint(\"\\nShare of combinations where the peri-movement space is best, by each reading:\")\nfor n in [\"proto\", \"combine\", \"onset\", \"tuning\", \"t_units\", \"fold\", \"norm\", \"kin_end\", \"task_end\", \"split\", \"kmax\"]:\n    print(f\"  {n}: \" + \", \".join(f\"{v} {grid[grid[n] == v].peri_beats_all.mean():.2f}\" for v in ps.READINGS[n]))\nprint(\"\\nMargin (peri best minus best other) over combinations: min\", round(grid.margin.min(), 3),\n      \"median\", round(grid.margin.median(), 3), \"max\", round(grid.margin.max(), 3))\nprint(\"Peri-movement best k over combinations:\", grid.peri_best_k.value_counts().sort_index().to_dict())\n\n# %% tags=claim:fig6-peri-movement-space-best\nc = dict(MAIN)\nperi, peri0, kin, task = curves_for(c)\npk = tuple(c[k] for k in PREP_KEYS)\nn_inc = int(peri_df.set_index(PREP_KEYS).loc[pk].n_units.iloc[0])\nprint(f\"Main reading, {n_inc} included units. Mean performance by k:\")\nprint(pd.DataFrame({\"peri-movement\": peri, \"kinematic\": kin}).round(3).T.to_string())\nprint(\"\\nTask spaces (dimensionality, mean performance):\")\nprint(task[[\"k\", \"perf\"]].round(3).to_string())\nalt = dict(MAIN, fold=\"refit\")\np2, _, k2, t2 = curves_for(alt)\nprint(\"\\nVariant fold = refit:\")\nprint(pd.DataFrame({\"peri-movement\": p2, \"kinematic\": k2}).round(3).T.to_string())\nfig, axs = plt.subplots(1, 2, figsize=(9, 3.2), sharey=True)\nfor ax, (pp, kk, tk, title) in zip(axs, [(peri, kin, task, \"space computed once\"), (p2, k2, t2, \"space refit per fold\")]):\n    ax.plot(pp.index, pp.values, \"k-o\", ms=3, label=\"peri-movement\")\n    ax.plot(kk.index, kk.values, \"b-o\", ms=3, label=\"kinematic\")\n    ax.plot(tk.k, tk.perf, \"gs\", label=\"task spaces\")\n    ax.axhline(0, color=\"0.7\"); ax.set_ylim(-0.5, 0.5); ax.set_xlabel(\"dimensionality\"); ax.set_title(title)\naxs[0].set_ylabel(\"mean performance\"); axs[0].legend(fontsize=7)\nplt.show()\nallv = np.r_[peri.values, kin.values, task.perf.values, p2.values, k2.values, t2.perf.values]\nprint(\"Values below -0.5 (outside the axes):\", int((allv < -0.5).sum()), \"; min\", round(allv.min(), 3))\n\n# %% [markdown]\n# ### fig6-each-dimensionality\n#\n# > At each dimensionality taken alone the peri-movement space almost always performs best; ...\n# > endpoints + maximum speed does not perform well for the maze task.\n#\n# Every other space at each of its dimensionalities against the peri-movement space at the same\n# k; reproduced when the peri-movement space wins at least 80% and beats endpoints + maximum\n# speed at k = 3.\n\n# %% tags=claim:fig6-each-dimensionality\nrows = []\nfor c in combos():\n    peri, peri0, kin, task = curves_for(c)\n    wins = [peri.loc[k] > kin.loc[k] for k in kin.index]\n    wins += [peri.loc[int(r.k)] > r.perf for _, r in task.iterrows() if r.k <= c[\"kmax\"]]\n    e3 = task.loc[\"endpoints + max speed\"].perf\n    rows.append({**c, \"comparisons\": len(wins), \"won\": int(sum(wins)), \"share\": np.mean(wins),\n                 \"peri_k3\": peri.loc[3], \"endpoints_max_speed\": e3, \"beats_e3\": peri.loc[3] > e3})\neach = pd.DataFrame(rows)\neach[\"criterion_met\"] = (each.share >= 0.8) & each.beats_e3\nprint(\"Main reading:\", each[is_main.values][[\"comparisons\", \"won\", \"share\", \"peri_k3\", \"endpoints_max_speed\", \"criterion_met\"]].round(3).to_dict(\"records\"))\nprint(\"Combinations meeting the criterion:\", int(each.criterion_met.sum()), \"of\", len(each))\nprint(\"Share won over combinations: min\", round(each.share.min(), 3), \"median\", round(each.share.median(), 3), \"max\", round(each.share.max(), 3))\nprint(\"By reading, fraction of combinations meeting the criterion:\")\nfor n in [\"proto\", \"combine\", \"onset\", \"tuning\", \"t_units\", \"fold\", \"norm\", \"kin_end\", \"task_end\", \"split\", \"kmax\"]:\n    print(f\"  {n}: \" + \", \".join(f\"{v} {each[each[n] == v].criterion_met.mean():.2f}\" for v in ps.READINGS[n]))\nperi, _, kin, task = curves_for(dict(MAIN))\nprint(\"\\nMain reading, kinematic minus peri-movement by k:\", (kin - peri).round(3).to_dict())\n\n# %% [markdown]\n# ### fig6-dimensionality-trend\n#\n# > Performance of the PCA-based spaces typically rises with dimensionality and falls beyond\n# > about 10 dimensions, a sign of overfitting.\n#\n# Reproduced when, for the peri-movement space, performance at its best k exceeds that at k = 1,\n# the best k is 10 or less, and performance at the largest tested k is below the best.\n\n# %% tags=claim:fig6-dimensionality-trend\ntrend = grid.copy()\ntrend[\"peri_rises\"] = trend.peri_best > trend.peri_k1\ntrend[\"peri_best_k_le_10\"] = trend.peri_best_k <= 10\ntrend[\"peri_falls\"] = trend.peri_kmax < trend.peri_best\ntrend[\"criterion_met\"] = trend.peri_rises & trend.peri_best_k_le_10 & trend.peri_falls\ntrend[\"kin_met\"] = (trend.kin_best > trend.kin_k1) & (trend.kin_best_k <= 10) & (trend.kin_kmax < trend.kin_best)\nprint(\"Main reading:\", trend[is_main][[\"peri_k1\", \"peri_best\", \"peri_best_k\", \"peri_kmax\", \"criterion_met\",\n                                        \"kin_k1\", \"kin_best\", \"kin_best_k\", \"kin_kmax\", \"kin_met\"]].round(3).to_dict(\"records\"))\nprint(\"Combinations meeting the criterion (peri-movement):\", int(trend.criterion_met.sum()), \"of\", len(trend),\n      \"; kinematic:\", int(trend.kin_met.sum()))\nprint(\"By reading, fraction meeting the criterion:\")\nfor n in [\"proto\", \"combine\", \"onset\", \"tuning\", \"t_units\", \"fold\", \"norm\", \"kmax\"]:\n    print(f\"  {n}: \" + \", \".join(f\"{v} {trend[trend[n] == v].criterion_met.mean():.2f}\" for v in ps.READINGS[n]))\nprint(\"\\nBest k of the peri-movement space, by fold reading:\")\nprint(trend.groupby(\"fold\").peri_best_k.describe().to_string())\n\n# %% [markdown]\n# ### fig6-pd-adequate-all-spaces\n#\n# > The PD performs adequately (above chance, performance above zero) in most spaces.\n#\n# Reproduced when mean performance is above zero for the peri-movement and kinematic spaces at\n# their best k and for more than half of the task spaces.\n\n# %% tags=claim:fig6-pd-adequate-all-spaces\nad = grid.copy()\nad[\"criterion_met\"] = (ad.peri_best > 0) & (ad.kin_best > 0) & (ad.n_task_above_0 > 4)\nprint(\"Main reading:\", ad[is_main][[\"peri_best\", \"kin_best\", \"n_task_above_0\", \"criterion_met\"]].round(3).to_dict(\"records\"))\nprint(\"Combinations meeting the criterion:\", int(ad.criterion_met.sum()), \"of\", len(ad))\nprint(\"Task spaces above zero over combinations:\", ad.n_task_above_0.value_counts().sort_index().to_dict(), \"(of 8)\")\nprint(\"By reading, fraction meeting the criterion:\")\nfor n in [\"proto\", \"combine\", \"onset\", \"tuning\", \"fold\", \"norm\", \"kin_end\", \"task_end\", \"split\"]:\n    print(f\"  {n}: \" + \", \".join(f\"{v} {ad[ad[n] == v].criterion_met.mean():.2f}\" for v in ps.READINGS[n]))\nprint(\"\\nPer task space, share of combinations with mean performance above zero:\")\nprint(task_df.groupby(\"space\").perf.apply(lambda x: (x > 0).mean()).round(2).to_string())\nprint(\"\\nPer task space, main reading: performance per unit above zero (count of units):\")\nctx = ctxs[(\"a\", \"concat\", \"a\")]\ninc = ps.tuning(ctx[\"prep\"], \"a\") > 5\nerrs, dims = ps.task_errors(ctx, inc, \"speed\", \"length\")\nprint({k: f\"{int((ps.performance(e, ctx['prep'][inc]) > 0).sum())} of {int(inc.sum())}\" for k, e in errs.items()})\n\n# %% [markdown]\n# ## fig6e-summary-rank\n#\n# Not tested: the summary combines monkeys A, B and J (single-electrode), whose data and EMG\n# are not in the dandiset.\n#\n# ## fig7a-shuffled-space-poor\n#\n# > A control peri-movement space in which each neuron's peri-movement pattern is inverted on a\n# > random half of conditions performs poorly.\n#\n# For each unit and condition, with probability 0.5 the movement-locked response after -150 ms\n# is reflected about the rate at -150 ms; the PCA space is then built as for the peri-movement\n# space. 20 draws (a standard choice), averaged. Run under the main reading and, one at a time,\n# under the other value of each reading that changes the peri-movement space.\n\n# %% tags=claim:fig7a-shuffled-space-poor\ndef shuffled_move(move, rng):\n    i0 = ps.T_WINDOW[0] - ps.MOVE_TRACE[0]\n    flip = rng.random(move.shape[:2]) < 0.5\n    out = move.copy()\n    ref = move[:, :, i0:i0 + 1]\n    out[:, :, i0:] = np.where(flip[:, :, None], 2 * ref - move[:, :, i0:], move[:, :, i0:])\n    return out\n\nvariants = [dict(MAIN)] + [dict(MAIN, **{n: ps.READINGS[n][1]}) for n in [\"combine\", \"proto\", \"onset\", \"t_units\", \"fold\", \"norm\", \"kin_end\"]]\nrng7a = np.random.default_rng(7)\nrows = []\nt0 = time.time()\nfor v in variants:\n    ctx = ctxs[(v[\"proto\"], v[\"combine\"], v[\"onset\"])]\n    inc = ps.tuning(ctx[\"prep\"], v[\"tuning\"]) > ps.ARRAY_MIN_TUNING\n    X = ctx[\"prep\"][inc]\n    n_draws = 20 if v[\"fold\"] == \"once\" else 5\n    shuf = np.zeros(14)\n    for d in range(n_draws):\n        err = ps.peri_errors(ctx, inc, v[\"t_units\"], v[\"fold\"], 14, move=shuffled_move(ctx[\"move\"], rng7a))\n        shuf += np.array([ps.perf_both(err[:, k], X)[v[\"norm\"]] for k in range(14)]) / n_draws\n    peri, _, kin, task = curves_for(v)\n    rows.append({\"variant\": \", \".join(f\"{n}={v[n]}\" for n in v if v[n] != MAIN[n]) or \"main\", \"draws\": n_draws,\n                 \"shuffled_best\": shuf.max(), \"shuffled_best_k\": int(shuf.argmax() + 1),\n                 \"peri_best\": peri.max(), \"kin_best\": kin.max(),\n                 \"below_peri_every_k\": bool(np.all(shuf < peri.values[:14])),\n                 \"below_kin_best\": shuf.max() < kin.max(),\n                 \"shuffled_by_k\": np.round(shuf, 3).tolist()})\nfig7a = pd.DataFrame(rows)\nfig7a[\"criterion_met\"] = fig7a.below_peri_every_k & fig7a.below_kin_best\nprint(f\"computed in {time.time() - t0:.0f} s\")\nprint(fig7a.drop(columns=\"shuffled_by_k\").round(3).to_string(index=False))\nprint(\"\\nShuffled-space performance by k:\")\nfor _, r in fig7a.iterrows():\n    print(f\"  {r.variant}: {r.shuffled_by_k}\")\n\n# %% [markdown]\n# ## fig7b-window-start-onset\n#\n# > Sliding the start of the peri-movement window from 150 ms before movement onset to movement\n# > onset barely lowers performance, which stays at 97% (monkey J) and 94% (monkeys A, B) of its\n# > original value.\n#\n# Mean performance of the peri-movement space with the window from 0 to +800 ms, divided by\n# that from -150 ms, each at its best k. Only reading (a) of the claims file (J-array against\n# 0.97) can be run; the J single-electrode dataset and monkeys A and B are not in the dandiset.\n\n# %% tags=claim:fig7b-window-start-onset\nfb = grid.copy()\nfb[\"ratio\"] = fb.peri0_best / fb.peri_best\nfb[\"within_tol\"] = (fb.ratio - 0.97).abs() <= 0.097\nprint(\"Expected 0.97 +/- 0.097 (0.873 to 1.067)\")\nprint(\"Main reading:\", fb[is_main][[\"peri_best\", \"peri_best_k\", \"peri0_best\", \"peri0_best_k\", \"ratio\", \"within_tol\"]].round(3).to_dict(\"records\"))\nprint(\"Combinations within tolerance:\", int(fb.within_tol.sum()), \"of\", len(fb))\nprint(\"Ratio over combinations: min\", round(fb.ratio.min(), 3), \"median\", round(fb.ratio.median(), 3), \"max\", round(fb.ratio.max(), 3))\nprint(\"By reading, median ratio and fraction within tolerance:\")\nfor n in [\"proto\", \"combine\", \"onset\", \"tuning\", \"t_units\", \"fold\", \"norm\", \"kmax\"]:\n    print(f\"  {n}: \" + \", \".join(f\"{v} {fb[fb[n] == v].ratio.median():.3f}/{fb[fb[n] == v].within_tol.mean():.2f}\" for v in ps.READINGS[n]))\n# finer sweep of the start under the main reading\nctx = ctxs[(\"a\", \"concat\", \"a\")]\ninc = ps.tuning(ctx[\"prep\"], \"a\") > 5\nX = ctx[\"prep\"][inc]\nsweep = {}\nfor start in [-150, -100, -50, 0, 50, 100]:\n    err = ps.peri_errors(ctx, inc, \"all\", \"once\", 14, start)\n    pf = [ps.perf_both(err[:, k], X)[\"neuron\"] for k in range(14)]\n    sweep[start] = (round(max(pf), 3), int(np.argmax(pf) + 1))\nprint(\"\\nMain reading, best performance (and k) by window start (ms from onset):\", sweep)\n\n# %% [markdown]\n# ## fig7c-anterior-posterior\n#\n# > The peri-movement space captures preparatory tuning at both anterior and posterior sites,\n# > with normalized performance only slightly different from that of random halves of the data,\n# > slightly better at anterior sites.\n#\n# Anterior and posterior are the two arrays, from the unit id prefix (prefix 1 assumed PMd,\n# anterior), as in results-ap-location-no-effect: with array membership as the AP location, the\n# units at or above the median are one array and those at or below it the other. For each\n# subset, the peri-movement space is built from that subset's units only (the unit being fit\n# excluded) and performance computed at k = 6, normalized by the upper limit, the PCA space of\n# the subset's preparatory rates, at k = 6 or at its best k. Whether the upper-limit space\n# includes the unit being fit is not stated (\"derived from the preparatory activity of all\n# neurons\"); both are run. Random halves: the units split at random into two halves, 20 draws\n# (a standard choice).\n\n# %% tags=claim:fig7c-anterior-posterior\ndef subset_scores(ctx, members, inc, fold, t_units, self_in_upper):\n    \"\"\"Mean performance at k = 6 in the peri-movement space of `members`, and of the upper-limit\n    space (k = 1..14), over included units of the subset.\"\"\"\n    fit = members & inc\n    in_t = members if t_units == \"all\" else fit\n    X = ctx[\"prep\"][fit]\n    Gp = ps.neuron_grams(ps.t_matrix(ctx[\"move\"]))\n    G = Gp[in_t].sum(0)\n    err = ps.loo_pca_space(G, Gp[fit] * in_t[fit][:, None, None], X, 6, fold)\n    peri6 = np.mean(ps.performance(err[:, 5], X))\n    P = ctx[\"prep\"][:, :, None]\n    Pp = ps.neuron_grams(P)\n    Gu = Pp[members].sum(0)\n    parts = None if self_in_upper else Pp[fit]\n    if self_in_upper:\n        erru = ps.loo_pca_space(Gu, None, X, 14, fold)\n    else:\n        erru = ps.loo_pca_space(Gu, parts, X, 14, fold)\n    upper = np.array([np.mean(ps.performance(erru[:, k], X)) for k in range(14)])\n    return peri6, upper, int(fit.sum())\n\nrng7c = np.random.default_rng(17)\nrows = []\nfor v in [dict(MAIN), dict(MAIN, fold=\"refit\"), dict(MAIN, combine=\"each\"), dict(MAIN, t_units=\"included\")]:\n    ctx = ctxs[(v[\"proto\"], v[\"combine\"], v[\"onset\"])]\n    inc = ps.tuning(ctx[\"prep\"], v[\"tuning\"]) > ps.ARRAY_MIN_TUNING\n    for self_in in [True, False]:\n        res = {}\n        for name, members in [(\"anterior\", units.id_array.values == 1), (\"posterior\", units.id_array.values == 2),\n                              (\"all\", np.ones(len(units), bool))]:\n            res[name] = subset_scores(ctx, members, inc, v[\"fold\"], v[\"t_units\"], self_in)\n        rand = []\n        for d in range(20 if v[\"fold\"] == \"once\" else 4):\n            perm = rng7c.permutation(len(units))\n            for half in (perm[: len(units) // 2], perm[len(units) // 2:]):\n                m = np.zeros(len(units), bool); m[half] = True\n                rand.append(subset_scores(ctx, m, inc, v[\"fold\"], v[\"t_units\"], self_in))\n        for up in [\"k6\", \"best\"]:\n            def norm(p, u):\n                return p / (u[5] if up == \"k6\" else u.max())\n            r_norm = np.mean([norm(p, u) for p, u, _ in rand])\n            a_norm, p_norm = norm(*res[\"anterior\"][:2]), norm(*res[\"posterior\"][:2])\n            rows.append({\"variant\": \", \".join(f\"{n}={v[n]}\" for n in v if v[n] != MAIN[n]) or \"main\",\n                         \"self_in_upper\": self_in, \"upper\": up,\n                         \"n_anterior\": res[\"anterior\"][2], \"n_posterior\": res[\"posterior\"][2],\n                         \"all_norm\": norm(*res[\"all\"][:2]), \"anterior_norm\": a_norm, \"posterior_norm\": p_norm,\n                         \"random_half_norm\": r_norm, \"anterior_raw\": res[\"anterior\"][0], \"posterior_raw\": res[\"posterior\"][0],\n                         \"random_raw\": np.mean([p for p, _, _ in rand]),\n                         \"ant_vs_random\": a_norm / r_norm, \"post_vs_random\": p_norm / r_norm})\nfig7c = pd.DataFrame(rows)\nfig7c[\"criterion_met\"] = ((fig7c.anterior_norm > 0) & (fig7c.posterior_norm > 0)\n                          & ((fig7c.ant_vs_random - 1).abs() <= 0.1) & ((fig7c.post_vs_random - 1).abs() <= 0.1))\nfig7c[\"anterior_better\"] = fig7c.anterior_norm > fig7c.posterior_norm\nprint(fig7c.round(3).to_string(index=False))\nprint(\"Rows meeting the criterion:\", int(fig7c.criterion_met.sum()), \"of\", len(fig7c))\n\n# %% [markdown]\n# ## fig7d-pd-consistency\n#\n# > In all four datasets and for every comparison, the PD is more stable across random subsets\n# > of conditions when measured in the peri-movement space than in task, kinematic or EMG spaces.\n#\n# Per unit, 25 conditions drawn with replacement, the unit-length PD fitted, another 25 drawn\n# and the PD refitted; consistency is the dot product, averaged over 100 draws (standard choice)\n# and units. Compared: endpoints + maximum speed (3-D) and segment directions (6-D) against the\n# peri-movement space at 3 and 6 dimensions, and the kinematic space at its best k against the\n# peri-movement space at that k. The spaces are taken as computed from all conditions. Whether\n# the axes of a space are scaled before the PD is fitted is not stated; the spaces as they are\n# (PC scores; task variables in mm and mm/s) and with each axis scaled to unit SD are both run.\n\n# %% tags=claim:fig7d-pd-consistency\ndef consistency(S, X, rng, n_draws=100):\n    c = S.shape[0]\n    D = np.column_stack([np.ones(c), S])\n    vals = np.zeros(X.shape[0])\n    for _ in range(n_draws):\n        i1, i2 = rng.integers(0, c, 25), rng.integers(0, c, 25)\n        b1 = np.linalg.lstsq(D[i1], X[:, i1].T, rcond=None)[0][1:]\n        b2 = np.linalg.lstsq(D[i2], X[:, i2].T, rcond=None)[0][1:]\n        b1 /= np.linalg.norm(b1, axis=0, keepdims=True)\n        b2 /= np.linalg.norm(b2, axis=0, keepdims=True)\n        vals += (b1 * b2).sum(0) / n_draws\n    return vals\n\nrng7d = np.random.default_rng(23)\nrows = []\nfor v in [dict(MAIN), dict(MAIN, combine=\"each\"), dict(MAIN, t_units=\"included\"), dict(MAIN, task_end=\"fixed\"),\n          dict(MAIN, split=\"time\"), dict(MAIN, kin_end=\"speed\"), dict(MAIN, onset=\"b\"), dict(MAIN, proto=\"b\")]:\n    ctx = ctxs[(v[\"proto\"], v[\"combine\"], v[\"onset\"])]\n    inc = ps.tuning(ctx[\"prep\"], v[\"tuning\"]) > ps.ARRAY_MIN_TUNING\n    X = ctx[\"prep\"][inc]\n    spaces, _ = ps.task_spaces(ctx[\"pos\"], ctx[\"vel\"], ctx[\"times\"], trials, v[\"task_end\"], v[\"split\"])\n    _, _, kin, _ = curves_for(v)\n    kbest = int(kin.idxmax())\n    KT = ps.kinematic_matrix(ctx[\"pos\"], ctx[\"vel\"], ctx[\"times\"], ps.kinematic_end_ms(ctx, v[\"kin_end\"]))\n    Skin = ps._scores_from_gram(ps.centre_gram(KT @ KT.T), 14)[0][:, :kbest]\n    Gp = ps.neuron_grams(ps.t_matrix(ctx[\"move\"]))\n    in_t = np.ones(len(inc), bool) if v[\"t_units\"] == \"all\" else inc\n    G = Gp[in_t].sum(0)\n    for scale in [\"raw\", \"unit SD\"]:\n        def sc(S):\n            return S / S.std(0) if scale == \"unit SD\" else S\n        comps = [(\"endpoints + max speed\", sc(spaces[\"endpoints + max speed\"]), 3),\n                 (\"segment directions\", sc(spaces[\"segment directions\"]), 6),\n                 (f\"kinematic k={kbest}\", sc(Skin), kbest)]\n        for name, S, k in comps:\n            other = consistency(S, X, rng7d)\n            peri_c = np.zeros(X.shape[0])\n            for j, u in enumerate(np.nonzero(inc)[0]):\n                Gj = G - Gp[u] * in_t[u]\n                Sp = sc(ps._scores_from_gram(ps.centre_gram(Gj), k)[0])\n                peri_c[j] = consistency(Sp, X[j:j + 1], rng7d)[0]\n            rows.append({\"variant\": \", \".join(f\"{n}={v[n]}\" for n in v if v[n] != MAIN[n]) or \"main\",\n                         \"scale\": scale, \"space\": name, \"k\": k, \"other_consistency\": other.mean(),\n                         \"peri_consistency\": peri_c.mean(), \"peri_higher\": peri_c.mean() > other.mean(),\n                         \"units_peri_higher\": int((peri_c > other).sum()), \"n_units\": len(other)})\nfig7d = pd.DataFrame(rows)\nprint(fig7d.round(3).to_string(index=False))\nby = fig7d.groupby([\"variant\", \"scale\"]).peri_higher.all()\nprint(\"\\nPeri-movement higher in every comparison, by variant and scaling:\")\nprint(by.to_string())\n\n# %% [markdown]\n# ## fig8-oscillator-model\n#\n# > In a simulated two-unit linear oscillator held at 25 initial states and then released,\n# > preparatory and peri-movement activity of a unit are nearly uncorrelated (r = 0.08), yet a\n# > PD in the two-dimensional peri-movement space captures the preparatory tuning perfectly.\n#\n# A simulation; no recorded data. W = [1 -2pi/360; 2pi/360 1], 25 initial states held, then\n# released. Readings: initial states uniform in [-1, 1]^2 or standard Gaussian; gray interval\n# one cycle (360 steps) or half (180). 1000 draws each. The PD part: leave-one-out performance\n# of a PD for unit 1's initial rate in the 2-D PCA space of the released activity of both units.\n\n# %% tags=claim:fig8-oscillator-model\nrng8 = np.random.default_rng(8)\nrows = []\nfor init in [\"uniform\", \"gaussian\"]:\n    for release in [360, 180]:\n        rs, perfs = [], []\n        for d in range(1000):\n            act, x0 = ps.oscillator(rng8, 25, 50, release, init)\n            rel = act[:, 50:, :]\n            rs.append(np.corrcoef(x0[:, 0], rel[:, :, 0].mean(1))[0, 1])\n            T = rel.transpose(0, 2, 1).reshape(25, -1)\n            S = ps._scores_from_gram(ps.centre_gram(T @ T.T), 2)[0]\n            err = ps.loo_errors_fixed(S, x0[None, :, 0])\n            perfs.append(ps.performance(err, x0[None, :, 0])[0])\n        rs, perfs = np.array(rs), np.array(perfs)\n        lo, hi = np.percentile(rs, [2.5, 97.5])\n        rows.append({\"init\": init, \"interval_steps\": release, \"median_r\": np.median(rs), \"r_2.5%\": lo, \"r_97.5%\": hi,\n                     \"0.08_inside\": lo <= 0.08 <= hi, \"min_pd_perf\": perfs.min(), \"median_pd_perf\": np.median(perfs),\n                     \"pd_ge_0.99\": perfs.min() >= 0.99})\nfig8 = pd.DataFrame(rows)\nprint(fig8.round(4).to_string(index=False))\n\n# %% [markdown]\n# ## Summary\n#\n# SUMMARY\n\n# %%\nprint(f\"Notebook run time: {(time.time() - started) / 60:.1f} min\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb.py (file state is current in your context — no need to Read it back)
```

**Agent**

Notebook source drafted. Cleaning two leftover expressions, then executing it in the dev environment to see the numbers.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
s=s.replace('''    rows.append({**c, "n_units": int(peri_df[(peri_df[PREP_KEYS] == pd.Series({k: c[k] for k in PREP_KEYS})).all(1)].n_units.iloc[0])
                 if False else None,
                 "peri_best"''','''    rows.append({**c, "peri_best"''')
s=s.replace('''grid = pd.DataFrame(rows).drop(columns="n_units")''','''grid = pd.DataFrame(rows)''')
s=s.replace('''fig4e["criterion_met"] = fig4e.near_zero_at_0 & fig4e.below_half_of_250 if False else (
    fig4e["near_zero_at_0"] & fig4e["below_half_of_-250"] & fig4e["no_early_decline"])''','''fig4e["criterion_met"] = fig4e["near_zero_at_0"] & fig4e["below_half_of_-250"] & fig4e["no_early_decline"]''')
open('nb.py','w').write(s)
EOF
. dev/bin/activate && python build_nb.py nb.py entries/000138-churchland-2010/reproduce_churchland_2010.ipynb && cd entries/000138-churchland-2010 && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output $TMPDIR/run1.ipynb reproduce_churchland_2010.ipynb 2>&1 | tail -5
```

```
55 cells

Available subcommands: execute kernel kernelspec migrate run troubleshoot
trust

Jupyter command `jupyter-nbconvert` not found.

real	0m0.091s
user	0m0.076s
sys	0m0.019s
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && uv pip install -q nbconvert requests 2>&1|tail -1; time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output $TMPDIR/run1.ipynb reproduce_churchland_2010.ipynb 2>&1 | tail -30
```

```
[32m      9[39m rows = []
[32m     10[39m [38;5;28;01mfor[39;00m proto, combine, onset [38;5;28;01min[39;00m itertools.product(ps.READINGS[[33m"proto"[39m], ps.READINGS[[33m"combine"[39m], ps.READINGS[[33m"onset"[39m]):
[32m---> [39m[32m11[39m     ctx = ps.prepare(data, R, onsets, proto, combine, onset)
[32m     12[39m     ctxs[(proto, combine, onset)] = ctx
[32m     13[39m     per = np.bincount(trials.cond_idx[ctx[[33m"mask"[39m]], minlength=[32m27[39m)
[32m     14[39m     row = {"proto": proto, "combine": combine, "onset": onset, "kept": int(ctx["mask"].sum()),

[36mFile [39m[32m~/work/encore/encore/entries/000138-churchland-2010/prepspace.py:473[39m, in [36mprepare[39m[34m(data, R, onsets, proto, combine, onset)[39m
[32m    471[39m t = data[[33m"[39m[33mtrials[39m[33m"[39m]
[32m    472[39m mask, r = select_trials(data, onsets[onset], proto, combine)
[32m--> [39m[32m473[39m pos, vel, times = [30;43mhand_condition_means[39;49m[30;43m([39;49m[30;43mdata[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43monsets[39;49m[30;43m[[39;49m[30;43monset[39;49m[30;43m][39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mmask[39;49m[30;43m)[39;49m
[32m    474[39m [38;5;28;01mreturn[39;00m {[33m"[39m[33mmask[39m[33m"[39m: mask, [33m"[39m[33mr[39m[33m"[39m: r, [33m"[39m[33mprep[39m[33m"[39m: condition_means(R[[33m"[39m[33mprep[39m[33m"[39m], t, mask),
[32m    475[39m         [33m"[39m[33mmove[39m[33m"[39m: condition_means(R[[33m"[39m[33mmove[39m[33m"[39m][onset], t, mask), [33m"[39m[33mpos[39m[33m"[39m: pos, [33m"[39m[33mvel[39m[33m"[39m: vel,
[32m    476[39m         [33m"[39m[33mtimes[39m[33m"[39m: times, [33m"[39m[33mtrials[39m[33m"[39m: t}

[36mFile [39m[32m~/work/encore/encore/entries/000138-churchland-2010/prepspace.py:266[39m, in [36mhand_condition_means[39m[34m(data, onset, mask, window)[39m
[32m    264[39m [38;5;28;01mfor[39;00m c [38
[... 17 more lines not kept]
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && sed -i 's/def hand_condition_means(data, onset, mask, window=(-200, 950)):/def hand_condition_means(data, onset, mask, window=(-200, 900)):/' prepspace.py && time jupyter nbconvert --to notebook --execute --ExecutePreprocessor.timeout=3000 --output $TMPDIR/run1.ipynb reproduce_churchland_2010.ipynb 2>&1 | tail -30
```

```
[31m---------------------------------------------------------------------------[39m
[31mIndexError[39m                                Traceback (most recent call last)
[36mCell[39m[36m [39m[32mIn[11][39m[32m, line 29[39m
[32m     25[39m         rows.append(row)
[32m     26[39m fig4d = pd.DataFrame(rows)
[32m     27[39m print([33m"Expected: mean r 0.13 +/- 0.013, mean Spearman 0.11 +/- 0.011, mean r > 0 at p < 0.05"[39m)
[32m     28[39m print(fig4d.round([32m4[39m).to_string(index=[38;5;28;01mFalse[39;00m))
[32m---> [39m[32m29[39m main4 = fig4d[(fig4d.proto == [33m"a"[39m) & (fig4d.combine == [33m"concat"[39m) & (fig4d.onset == [33m"a"[39m) & (fig4d.tuning == [33m"a"[39m)].iloc[[32m0[39m]
[32m     30[39m print([33m"\nMain reading:"[39m, main4.round([32m4[39m).to_dict())
[32m     31[39m ok = fig4d.dropna(subset=[[33m"mean_r"[39m])
[32m     32[39m print("Readings with a result:", len(ok), "; both means within tolerance:",

[36mFile [39m[32m/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/indexing.py:1342[39m, in [36m_LocationIndexer.__getitem__[39m[34m(self, key)[39m
[32m   1340[39m maybe_callable = com.apply_if_callable(key, [38;5;28mself[39m.obj)
[32m   1341[39m maybe_callable = [38;5;28mself[39m._raise_callable_usage(key, maybe_callable)
[32m-> [39m[32m1342[39m [38;5;28;01mreturn[39;00m [30;43mself[39;49m[30;43m.[39;49m[30;43m_getitem_axis[39;49m[30;43m([39;49m[30;43mmaybe_callable[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43maxis[39;49m[30;43m=[39;49m[30;43maxis[39;49m[30;43m)[39;49m

[36mFile [39m[32m/tmp/claude-1001/dev/lib/python3.13/site-packages/pandas/core/indexing.py:2432[39m, in [36m_iLocIndexer._getitem_axis[39m[34m(self, key, axis)[39m
[32m   2429[39m     [38;5;28;01mraise[39;00m [38;5;167;01mTypeError[39;00m([33m"[39m[33mCannot index by location index with a non-integer key[39m[33m"[39m)
[32m   2431[39m [38;5;66;03m# validate 
[... 14 more lines not kept]
```

**Agent**

`.combine` is a DataFrame method, so attribute access fails silently. Fixing and running with errors allowed so all failures show in one pass.

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "\.combine\b" nb.py; sed -i 's/(fig4d\.combine == "concat")/(fig4d["combine"] == "concat")/' nb.py; grep -n "\.combine\b" nb.py; . dev/bin/activate && python build_nb.py nb.py entries/000138-churchland-2010/reproduce_churchland_2010.ipynb && cd entries/000138-churchland-2010 && time jupyter nbconvert --to notebook --execute --allow-errors --ExecutePreprocessor.timeout=3000 --output $TMPDIR/run1.ipynb reproduce_churchland_2010.ipynb 2>&1 | tail -3
```

```
363:main4 = fig4d[(fig4d.proto == "a") & (fig4d.combine == "concat") & (fig4d.onset == "a") & (fig4d.tuning == "a")].iloc[0]
55 cells
[NbConvertApp] Converting notebook reproduce_churchland_2010.ipynb to notebook
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
[NbConvertApp] Writing 236547 bytes to /tmp/claude-1001/run1.ipynb

real	5m32.922s
user	5m29.736s
sys	0m1.164s
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > show.py <<'EOF'
import nbformat,sys
nb=nbformat.read(sys.argv[1],4)
for i,c in enumerate(nb.cells):
    if c.cell_type!='code': continue
    for o in c.outputs:
        if o.output_type=='stream': print(f'--- cell {i}', c.metadata.get('tags','')); print(o.text[:int(sys.argv[2]) if len(sys.argv)>2 else 6000])
        elif o.output_type=='error': print(f'--- cell {i} ERROR', o.ename, o.evalue)
EOF
. dev/bin/activate; python show.py run1.ipynb 2>&1 | head -400; date -u
```

```
--- cell 1 
loaded dandiset 000138 version 0.220113.0407, sub-Jenkins/sub-Jenkins_ses-large_desc-train_behavior+ecephys.nwb, in 3 s

--- cell 3 ['sanity']
Versions: [('draft', 2, 149392888), ('0.220113.0407', 2, 149392888)]
0.220113.0407 [('sub-Jenkins/sub-Jenkins_ses-large_desc-test_ecephys.nwb', 802352, 'd78a051b-669f-4b7c-bcb6-769f106afb1c'), ('sub-Jenkins/sub-Jenkins_ses-large_desc-train_behavior+ecephys.nwb', 148590536, 'c7549202-993a-42a0-b8b3-27635e053d60')]
draft [('sub-Jenkins/sub-Jenkins_ses-large_desc-test_ecephys.nwb', 802352, 'd78a051b-669f-4b7c-bcb6-769f106afb1c'), ('sub-Jenkins/sub-Jenkins_ses-large_desc-train_behavior+ecephys.nwb', 148590536, 'c7549202-993a-42a0-b8b3-27635e053d60')]

Related resources: [('10.1016/j.neuron.2010.09.015', 'dcite:IsDescribedBy'), ('10.1038/nature11129', 'dcite:IsDescribedBy')]
Description: This dataset contains sorted unit spiking times and behavioral data from a macaque performing a delayed reaching task. The experimental task was a center-out reaching task with obstructing barriers forming a maze, resulting in a variety of straight and curved reaches. Neural activity was recorded from electrode arrays implanted in the motor cortex (M1) and dorsal premotor cortex (PMd). Cursor position, hand position, and eye position were also recorded during the experiment, and hand velocity was calculated offline from hand position. The provided data has been limited to 500 train trials and 100 test trials. Provided as part of the Neural Latents Benchmark: https://neurallatents.github.io.

File metadata: {'session_start': '2009-10-06T00:00:00-07:00', 'subject': 'Jenkins', 'species': 'Macaca mulatta', 'session_description': 'Data from monkey Jenkins performing center-out delayed reaching task. This file contains trials from the full session on 2009-10-06 that can be used for training models for the Neural Latents Benchmark.'}

--- cell 5 ['sanity']
Trials: 500 ; success: {True: 500} ; split: {'train': 375, 'val': 125}
Conditions (tria
[... 386 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate; python show.py run1.ipynb 2>&1 | sed -n 400,600p
```

```
initial velocity                    1.00
kitchen sink                        0.91
segment directions                  0.94

Per task space, main reading: performance per unit above zero (count of units):
{'initial velocity': '56 of 92', 'endpoints + max speed': '42 of 92', 'endpoints + orthogonal excursion': '43 of 92', 'endpoints + viapoint': '60 of 92', 'endpoints + max velocity': '30 of 92', 'endpoints + halfpoint': '58 of 92', 'segment directions': '62 of 92', 'kitchen sink': '69 of 92'}

--- cell 44 ['claim:fig7a-shuffled-space-poor']
computed in 34 s
         variant  draws  shuffled_best  shuffled_best_k  peri_best  kin_best  below_peri_every_k  below_kin_best  criterion_met
            main     20          0.014                3      0.351     0.103                True            True           True
    combine=each     20         -0.014                2      0.150     0.068               False            True          False
         proto=b     20          0.023                3      0.338     0.098                True            True           True
         onset=b     20          0.029                4      0.351     0.099                True            True           True
t_units=included     20          0.017                3      0.353     0.103                True            True           True
      fold=refit      5          0.178               14      0.461     0.160                True           False          False
     norm=pooled     20          0.122                3      0.562     0.289                True            True           True
   kin_end=speed     20          0.012                3      0.351     0.109                True            True           True

Shuffled-space performance by k:
[... 106 more lines not kept]
```

**Agent**

All cells run in 5.5 min; one formatting error in the Fig 4D cell. Checking the truncated Fig 7D summary and the endpoints + max speed value.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate; python - <<'EOF'
import nbformat
nb=nbformat.read('run1.ipynb',4)
for c in nb.cells:
    if 'claim:fig7d-pd-consistency' in c.metadata.get('tags',[]):
        for o in c.outputs:
            if o.output_type=='stream': print(o.text[-1500:])
EOF
```

```
kinematic k=4  4              0.741             0.777         True                 57       92
         proto=b     raw endpoints + max speed  3              0.594             0.755         True                 79       91
         proto=b     raw    segment directions  6              0.559             0.676         True                 63       91
         proto=b     raw         kinematic k=4  4              0.645             0.739         True                 65       91
         proto=b unit SD endpoints + max speed  3              0.630             0.786         True                 78       91
         proto=b unit SD    segment directions  6              0.569             0.721         True                 67       91
         proto=b unit SD         kinematic k=4  4              0.740             0.781         True                 59       91

Peri-movement higher in every comparison, by variant and scaling:
variant           scale  
combine=each      raw        True
                  unit SD    True
kin_end=speed     raw        True
                  unit SD    True
main              raw        True
                  unit SD    True
onset=b           raw        True
                  unit SD    True
proto=b           raw        True
                  unit SD    True
[... 7 more lines not kept]
```

**Agent**

Fig 7D holds in every variant. I have the numbers for all claims. Now writing the conclusions, header and summary into the notebook source.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
s=s.replace('''print("\\nMain reading:", main4.round(4).to_dict())''','''print("\\nMain reading:", {k: (round(v, 4) if isinstance(v, float) else v) for k, v in main4.to_dict().items()})''')
s=s.replace('''print(task[["k", "perf"]].round(3).to_string())''','''print(task[["k", "perf"]].round(4).to_string())''')
s=s.replace('''print("RT (ms) range:", trials.rt.min(), "to", trials.rt.max())''','''print("Trials with delay of 0 ms or less:", int((trials.delay <= 0).sum()))
print("RT (ms) range:", trials.rt.min(), "to", trials.rt.max())''')
open('nb.py','w').write(s)
EOF
grep -n "Main reading:\", {k" nb.py | head -2; date -u
```

```
365:print("\nMain reading:", {k: (round(v, 4) if isinstance(v, float) else v) for k, v in main4.to_dict().items()})
Wed Oct 28 20:09:19 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > results.py <<'PYEOF'
R = {}
R["# %% [markdown]\n# ## fig4e-correlation-time-course"] = """**Result: partially reproduced, under the main reading of trial selection and movement onset (an
assumption).** Under the main reading 20 units pass the criteria. Mean r is 0.195 and mean
Spearman r 0.212, both above the expected 0.13 +/- 0.013 and 0.11 +/- 0.011, and the mean r is
above zero (t-test p = 0.023, on Fisher z p = 0.023, Wilcoxon p = 0.024), which by the criterion
is a partial reproduction. Over the eight readings with a result (all with tuning as a range),
mean r spans 0.105 to 0.195 and mean Spearman r 0.147 to 0.212; mean r is within tolerance in
five readings, mean Spearman r in none, and the mean r is above zero at p < 0.05 in two; in the
other six it is positive but not significant (smallest p 0.049 for the Wilcoxon test, largest
0.205). Under the SD reading of tuning no unit passes. With a peri-movement criterion of 1.0 in
place of 1.5, 52 units give mean r 0.137 (p = 0.0041). The dandiset has 27 of the paper's 108
conditions."""
R["# %% [markdown]\n# ## results-ap-location-no-effect"] = """**Result: not reproduced.** The mean correlation is 0.773 at -400 ms and 0.764 at -300 ms,
0.713 at -250 ms and 0.572 at -200 ms, so the decline begins about 250 ms before movement onset,
as the paper describes. It is 0.218 at movement onset, not near zero by the criterion (below
0.1), and first falls below 0.1 between +150 and +200 ms (0.110 and 0.064). All eight readings
give 0.129 to 0.218 at onset, and all meet the other two parts of the criterion."""
R["# %% [markdown]\n# ## supp-preparatory-dimensionality"] = """**Result: reproduced for the J-array dataset, on the assumption that the unit id prefix gives the
array, prefix 1 being PMd.** Regressing the per-unit correlation on array gives r = 0.047,
p = 0.844 under the main reading (12 anterior and 8 posterior units; mean r 0.209 and 0.176),
and p from 0.432 to 0.844 over the eight readings, so no reading finds an effect. The paper's
J-array values are r = 0.20, p = 0.27. The single-electrode datasets are not in the dandiset."""
R["# %% [markdown]\n# ## PD performance in each space (Figure 6, J-array)"] = """**Result: reproduced under the main reading (an assumption).** With all 162 units, 11 components
capture 90% of the variance, inside 6.3 to 11; with the 92 included units, 10. Under the `each`
trial selection the counts are 12 and 11, so with all units the count is outside the range; under
the SD reading of tuning, with 6 or 7 units, it is 4. On half of the trials the count rises to 14
and 13, so trial noise adds dimensions at these trial counts."""
R["# %% [markdown]\n# ### fig6-each-dimensionality"] = """**Result: reproduced.** Under the main reading the peri-movement space's best mean performance is
0.351 (k = 10), above the kinematic space (0.103, k = 4) and the best task space (kitchen sink,
0.250). Over the 2048 combinations of readings the peri-movement space is best in 1468; the
criterion asks for one. It is best in 95% of the combinations with tuning as a range and 49% with
the SD (6 or 7 units), and in 94% with all units in the T-matrix against 50% with included units
only. Its best k is 7 or more in most combinations (from 2 to 14), and 10 under the main reading.
EMG was not recorded for J-array."""
R["# %% [markdown]\n# ### fig6-dimensionality-trend"] = """**Result: reproduced under the main reading (an assumption).** The peri-movement space wins 20 of
22 comparisons (0.909) and beats endpoints + max speed at k = 3 (0.126 against 0.0). Over all
combinations the criterion is met in 1074 of 2048. It depends most on the trial selection (met in
69% with `concat` and 36% with `each`), the tuning reading (75% and 30%), the units of the
T-matrix (67% and 38%) and the fold reading (37% with the space computed once, 68% refit)."""
R["# %% [markdown]\n# ### fig6-pd-adequate-all-spaces"] = """**Result: reproduced under the main reading (an assumption).** Peri-movement performance rises
from 0.056 at k = 1 to 0.351 at k = 10 and falls to -0.456 at k = 14; the kinematic space does
the same (0.061 at k = 1, best 0.103 at k = 4, -0.451 at k = 14). The fall depends on computing
the space once: the criterion is met in 91% of the combinations with the space computed once and
6% when it is refit without the left-out condition, where performance keeps rising (0.461 at
k = 14 under the main reading otherwise; best k 10 to 14)."""
R["# %% [markdown]\n# ## fig6e-summary-rank"] = """**Result: reproduced under the main reading (an assumption).** Mean performance is above zero for
the peri-movement space (0.351) and the kinematic space (0.103) at their best k, and for 7 of the
8 task spaces; endpoints + max velocity is negative (-0.125) and endpoints + max speed is at
zero. The criterion is met in 1936 of 2048 combinations."""
R["# %% [markdown]\n# ## fig7b-window-start-onset"] = """**Result: reproduced under the main reading (an assumption).** The shuffled space's best mean
performance is 0.014 (k = 3), below the peri-movement space at every k and below the kinematic
space's best (0.103). The criterion also holds with proto-trial (b), onset (b), included units
in the T-matrix, pooled performance and the kinematic window ending with the reach. It fails
under two variants: with the `each` selection the shuffled space is not below the peri-movement
space at every k, and with the space refit per fold the shuffled space reaches 0.178, above the
kinematic best of 0.160 and below the peri-movement best of 0.461 (5 draws in place of 20)."""
R["# %% [markdown]\n# ## fig7c-anterior-posterior"] = """**Result: reproduced under the main reading (an assumption), for J-array only.** With the window
starting at movement onset, the best performance is 0.318 (k = 9), against 0.351 (k = 10) from
-150 ms, a ratio of 0.908, inside 0.873 to 1.067. Over all combinations the ratio is within
tolerance in 1336 of 2048 (median 0.917; within tolerance in 47% with the space computed once and
84% refit). The 0.94 for monkeys A and B cannot be tested."""
R["# %% [markdown]\n# ## fig7d-pd-consistency"] = """**Result: not reproduced under the main reading (an assumption).** With the upper limit built
from all units of each subset, at k = 6, normalized performance is 0.597 for the anterior array
(prefix 1) and 0.382 for the posterior array, against 0.617 for random halves: anterior is within
10% (ratio 0.968), posterior is not (0.618). Anterior exceeds posterior, as the paper reports.
Of the 16 combinations of readings, 2 meet the criterion, both with the space refit per fold and
the unit included in its upper-limit space. The split rests on the assumed array of each unit."""
R["# %% [markdown]\n# ## fig8-oscillator-model"] = """**Result: reproduced, for J-array.** Under the main reading the peri-movement space has the higher
mean consistency in all three comparisons: 0.756 against 0.610 (endpoints + max speed, k = 3),
0.684 against 0.570 (segment directions, k = 6) and 0.748 against 0.666 (kinematic, k = 4). It is
higher in every comparison under all eight variants and with the axes as they are or scaled to
unit SD. The other three datasets, and EMG, are not in the dandiset."""
R["# %% [markdown]\n# ## Summary"] = """**Result: reproduced.** Under every reading the median correlation of unit 1's held and released
activity is near zero (-0.019 to 0.012), with a central 95% from about -0.41 to 0.40, which
contains 0.08. A PD in the 2-D PCA space of the released activity captures unit 1's initial rate
with leave-one-out performance of 1.0 in every draw."""

HEADER = """**Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical
preparatory activity: representation of movement or first cog in a dynamical machine? *Neuron*
68:387-400. [doi:10.1016/j.neuron.2010.09.015](https://doi.org/10.1016/j.neuron.2010.09.015). The
claims file (`claims/000138/10.1016-j.neuron.2010.09.015.yaml`) was written from the NIH author
manuscript in PubMed Central (PMC2991102) with its supplement; the main-text figure panels were
not available to its reader.

**Dandiset.** [DANDI:000138](https://dandiarchive.org/dandiset/000138/0.220113.0407), version
0.220113.0407 (MC_Maze_Large, Neural Latents Benchmark). The paper (2010) predates the dandiset
and cites no version. This is the only published version, and the draft holds the same two files
(same blobs, checked below), so the most recent published version is pinned.

**What it holds.** One session of monkey J (2009-10-06) on the maze task: 500 successful trials
over 27 conditions, 162 sorted units from two Utah arrays, hand, cursor and eye position, and hand
velocity. The paper's J-array dataset had 108 conditions, 146 units and a mean 2166 trials per
neuron; the dandiset is a 500-trial subset of a session, and nothing in it or the paper says
whether this session is the one the paper used. The single-electrode datasets (monkeys A, B and
J) and all EMG are not in it.

**Readings.** The claims file names several open method details and the paper leaves a few
more open. Each is run where it could change an outcome; a main reading, the one best supported by
the paper, decides an outcome when the readings disagree, and the outcome is then marked as
resting on an assumption. Seeds are fixed per claim.

| Claim | Tested | Outcome |
|---|---|---|
| fig4abc-tuning-correlation-single-electrode | no | blocked, data missing |
| fig4d-tuning-correlation-j-array | yes | partially reproduced (assumption) |
| fig4e-correlation-time-course | yes | not reproduced |
| results-ap-location-no-effect | J-array only | reproduced (assumption) |
| supp-preparatory-dimensionality | J-array only | reproduced (assumption) |
| fig6-peri-movement-space-best | J-array only | reproduced |
| fig6-each-dimensionality | J-array only | reproduced (assumption) |
| fig6-dimensionality-trend | J-array only | reproduced (assumption) |
| fig6-pd-adequate-all-spaces | J-array only | reproduced (assumption) |
| fig6e-summary-rank | no | blocked, data missing |
| fig7a-shuffled-space-poor | J-array only | reproduced (assumption) |
| fig7b-window-start-onset | J-array only | reproduced (assumption) |
| fig7c-anterior-posterior | J-array only | not reproduced (assumption) |
| fig7d-pd-consistency | J-array only | reproduced |
| fig8-oscillator-model | simulation | reproduced |"""

SUMMARY = """| Claim | Outcome | Main numbers |
|---|---|---|
| fig4abc-tuning-correlation-single-electrode | blocked (data missing) | single-electrode data not in the dandiset |
| fig4d-tuning-correlation-j-array | partially reproduced (assumption) | mean r 0.195, Spearman 0.212, p = 0.023 |
| fig4e-correlation-time-course | not reproduced | r 0.218 at movement onset |
| results-ap-location-no-effect | reproduced (assumption) | r = 0.047, p = 0.844 (J-array) |
| supp-preparatory-dimensionality | reproduced (assumption) | 11 components |
| fig6-peri-movement-space-best | reproduced | 0.351 against 0.250 and 0.103 |
| fig6-each-dimensionality | reproduced (assumption) | 20 of 22 comparisons |
| fig6-dimensionality-trend | reproduced (assumption) | best k 10, falls to -0.456 at 14 |
| fig6-pd-adequate-all-spaces | reproduced (assumption) | 7 of 8 task spaces above 0 |
| fig6e-summary-rank | blocked (data missing) | monkeys A, B, J and EMG not in the dandiset |
| fig7a-shuffled-space-poor | reproduced (assumption) | shuffled best 0.014 |
| fig7b-window-start-onset | reproduced (assumption) | ratio 0.908 |
| fig7c-anterior-posterior | not reproduced (assumption) | posterior 0.618 of random halves |
| fig7d-pd-consistency | reproduced | higher in 3 of 3 comparisons |
| fig8-oscillator-model | reproduced | 0.08 inside the central 95% |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

**How the analysis differs from the paper's.** Only the array dataset of monkey J can be tested,
on 27 of its 108 conditions and 500 trials of one session, so every J-array number rests on a
quarter of the conditions and fewer trials per condition after selection (11 to 18). The paper
leaves open the proto-trial, how the velocity correlation combines the two axes, the movement
onset method, what "tuning" in spikes/s means, whether the PCA space is recomputed without the
left-out condition, which units form the T-matrix, the end of the kinematic window and of the
reach, how paths are split, and, for Figure 7, the upper-limit space and the scaling of axes.
Each is run, and outcomes that differ between readings are marked as assumptions. The main
reading takes the mean proto-trial, the concatenated velocity profile, the trial table's movement
onset, tuning as the range of condition means, all units in the T-matrix, the space computed once
from all conditions (the paper describes leaving out a condition only for the PD fit), and
performance averaged over units. Figure 4E uses the movement-locked average, the part of the
paper's spliced trace that is locked to movement onset. The anterior and posterior split uses the
array of each unit, inferred from the unit id prefix.

**What was found about the dataset.**

- The units' electrode references all point to the PMd group: the referenced electrode is the
  channel in the unit id minus one, for both id prefixes, so the 79 units of prefix 2 reference
  PMd electrodes. Which prefix is which array is not stated; electrode coordinates are NaN.
- The dandiset holds a 500-trial, 27-condition subset of one session; the paper's J-array dataset
  had 108 conditions and 146 units (the file has 162), and there is no way to tell from the files
  whether the session is the paper's. The single-electrode datasets and EMG are not in it.
- Hand data are at 1 kHz within trials only, where the paper tracked the hand at 60 Hz; the
  resampling is not described. Velocity agrees with the derivative of position.
- The test file holds 100 unlabelled 700 ms segments of the held-in units, not usable for these
  claims; no test segment repeats a training interval sequence."""

s = open("nb.py").read()
for anchor, text in R.items():
    assert anchor in s, anchor
    block = "# %% [markdown]\n" + "\n".join("# " + l if l else "#" for l in text.splitlines()) + "\n\n"
    s = s.replace(anchor, block + anchor, 1)
s = s.replace("# HEADER", "\n".join("# " + l if l else "#" for l in HEADER.splitlines()))
s = s.replace("# SUMMARY", "\n".join("# " + l if l else "#" for l in SUMMARY.splitlines()))
open("nb_final.py", "w").write(s)
print("ok")
PYEOF
python results.py
```

```
ok
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('results.py').read()
s=s.replace('''five readings, mean Spearman r in none, and the mean r is above zero at p < 0.05 in two; in the
other six it is positive but not significant (smallest p 0.049 for the Wilcoxon test, largest
0.205).''','''five readings, mean Spearman r in none, and the mean r is above zero at p < 0.05 in two; in the
other six it is positive, with the smallest p of the three tests from 0.074 to 0.169.''')
s=s.replace('''6% when it is refit without the left-out condition, where performance keeps rising (0.461 at
k = 14 under the main reading otherwise; best k 10 to 14).''','''6% when it is refit without the left-out condition; refit, with the main reading otherwise,
performance keeps rising to 0.461 at k = 14, and the best k is 10 to 14 over those combinations.''')
open('results.py','w').write(s)
EOF
python results.py && . dev/bin/activate && python build_nb.py nb_final.py entries/000138-churchland-2010/reproduce_churchland_2010.ipynb
```

```
ok
68 cells
Shell cwd was reset to
```

**Agent**

Now the entry files.

**Agent calls Bash**

```bash
cd entries/000138-churchland-2010 && cat > requirements.in <<'EOF'
dandi
h5py
matplotlib
numpy
pandas
remfile
requests
scipy
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: 000138-churchland-2010
type: reproduction
title: Preparatory tuning in a peri-movement space (Churchland et al. 2010)
description: Tests the findings of Churchland, Cunningham, Kaufman, Ryu and Shenoy (2010) on
  dandiset 000138 (MC_Maze_Large), which holds 500 maze-task trials over 27 conditions and 162
  array units from one session of monkey J. It compares preparatory and peri-movement tuning, and
  how well a preferred direction captures preparatory tuning in peri-movement, kinematic and task
  spaces, with the controls of Figure 7 and the oscillator of Figure 8. The single-electrode
  datasets of monkeys A, B and J and the EMG are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_churchland_2010.ipynb
  title: Reproducing Churchland et al. (2010) from dandiset 000138
  runtime_minutes: 6
helpers:
- prepspace.py
related:
- id: dandi:000138/0.220113.0407
  relation: uses_data
- id: doi:10.1016/j.neuron.2010.09.015
  relation: reproduces
EOF
cat ../../schemas/entry.schema.json | head -60
```

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "An entry: a directory of notebooks with its metadata (entry.yaml)",
  "description": "Draft. To be revised after the pilot.",
  "type": "object",
  "additionalProperties": false,
  "required": ["schema_version", "name", "type", "title", "description", "license", "notebooks", "related"],
  "properties": {
    "schema_version": {"const": 1},
    "name": {
      "description": "Unique across the registry, and the name of the entry's directory.",
      "type": "string",
      "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$",
      "maxLength": 100
    },
    "type": {"enum": ["orientation", "reproduction", "analysis"]},
    "title": {"type": "string", "minLength": 1, "maxLength": 300},
    "description": {"type": "string", "minLength": 1},
    "license": {"description": "SPDX identifier.", "type": "string"},
    "notebooks": {
[... 37 more lines not kept]
```

**Agent calls Bash**

```bash
cd  && pip list 2>/dev/null | grep -i -E "pyyaml|jsonschema|nbformat"; python tools/entry.py lock entries/000138-churchland-2010 2>&1 | tail -3 && python tools/entry.py check entries/000138-churchland-2010 2>&1 | tail -20
```

```
fastjsonschema            2.22.2
jsonschema                4.26.0
jsonschema-specifications 2025.9.1
nbformat                  5.11.1
PyYAML                    6.0.3
wrote entries/000138-churchland-2010/requirements.lock.txt
0 error(s)
```

**Agent**

Lock and check pass. Running the entry from a clean environment.

**Agent calls Bash**

```bash
date -u && time python tools/entry.py all entries/000138-churchland-2010 2>&1 | tail -15
```

```
Wed Oct 28 20:11:03 UTC 2026
Installed kernelspec registry-000138-churchland-2010 in executed/000138-churchland-2010/.venv/share/jupyter/kernels/registry-000138-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (338 s)

real	6m10.883s
user	6m3.103s
sys	0m5.485s
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && ls executed/000138-churchland-2010/; python show.py executed/000138-churchland-2010/reproduce_churchland_2010.ipynb 2>&1 | grep -n -E "ERROR|Main reading|Range of mean r|Readings with|endpoints \+ max speed  |Combinations|Rows meeting|Trials with delay|Notebook run|k90|ratio over|Ratio over" | head -40
```

```
reproduce_churchland_2010.ipynb
result.json
65:Trials with delay of 0 ms or less: 8
158:Main reading: {'proto': 'a', 'combine': 'concat', 'onset': 'a', 'tuning': 'a', 'n_units': 20, 'mean_r': 0.1954, 'mean_spearman': 0.2119, 'p_t': 0.0233, 'p_t_fisher': 0.0225, 'p_wilcoxon': 0.024, 'r_within_tol': False, 'spearman_within_tol': False, 'positive_p05': True}
159:Readings with a result: 8 ; both means within tolerance: 0 ; mean r positive at p < 0.05: 1
160:Range of mean r over readings with a result: 0.105 to 0.195 ; mean Spearman: 0.146 to 0.212
163:Main reading, per-unit Pearson r: range -0.459 to 0.794 ; by id prefix: {'count': {1: 12, 2: 8}, 'mean': {1: 0.209, 2: 0.176}}
180:Main reading, mean correlation every 50 ms from -600 to +400 ms:
241:Readings with no effect (p >= 0.05): 8 of 8
245:proto combine onset  units_all  k90_all  units_included_a  k90_included_a  units_included_b  k90_included_b
254:Main reading, all units, cumulative variance of the first 15 PCs: [0.297 0.49  0.601 0.682 0.738 0.79  0.829 0.856 0.877 0.896 0.91  0.924
256:Split halves of trials (seed 4): k90 = 14 and 13
263:Combinations of readings: 2048 ; peri-movement space best in 1468
265:Main reading:
315:Main reading, 92 included units. Mean performance by k:
324:endpoints + max speed              3  0.0003
341:Main reading: [{'comparisons': 22, 'won': 20, 'share': 0.909, 'peri_k3': 0.126, 'endpoints_max_speed': 0.0, 'criterion_met': True}]
342:Combinations meeting the criterion: 1074 of 2048
357:Main reading, kinematic minus peri-movement by k: {1: 0.005, 2: -0.063, 3: -0.029, 4: -0.06, 5: -0.16, 6: -0.231, 7: -0.264, 8: -0.255, 9: -0.296, 10: -0.308, 11: -0.45, 12: -0.486, 13: -0.265, 14: 0.004}
360:Main reading: [{'peri_k1': 0.056, 'peri_best': 0.351, 'peri_best_k': 10, 'peri_kmax': -0.456, 'criterion_met': True, 'kin_k1': 0.061, 'kin_best': 0.103, 'kin_best_k': 4, 'kin_kmax': -0.451, 'kin_met': True}]
[... 23 more lines not kept]
```

**Agent**

Two text details to correct (Spearman minimum 0.146; endpoints + max speed is 0.0003). The count of readings with p < 0.05 printed 1, where the table earlier showed 2; checking.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python show.py executed/000138-churchland-2010/reproduce_churchland_2010.ipynb 2>&1 | sed -n 138,158p
```

```
--- cell 23 ['claim:fig4d-tuning-correlation-j-array']
Expected: mean r 0.13 +/- 0.013, mean Spearman 0.11 +/- 0.011, mean r > 0 at p < 0.05
proto combine onset tuning  n_units  mean_r  mean_spearman    p_t  p_t_fisher  p_wilcoxon r_within_tol spearman_within_tol positive_p05
    a  concat     a      a       20  0.1954         0.2119 0.0233      0.0225      0.0240        False               False         True
    a  concat     a      b        0     NaN            NaN    NaN         NaN         NaN          NaN                 NaN          NaN
    a  concat     b      a       19  0.1115         0.1528 0.1802      0.1659      0.1688        False               False        False
    a  concat     b      b        0     NaN            NaN    NaN         NaN         NaN          NaN                 NaN          NaN
    a    each     a      a       22  0.1339         0.1651 0.0845      0.0795      0.0738         True               False        False
    a    each     a      b        0     NaN            NaN    NaN         NaN         NaN          NaN                 NaN          NaN
    a    each     b      a       20  0.1240         0.1609 0.1403      0.1254      0.1429         True               False        False
    a    each     b      b        0     NaN            NaN    NaN         NaN         NaN          NaN                 NaN          NaN
    b  concat     a      a       22  0.1353         0.1601 0.1072      0.0961      0.0854         True               False        False
    b  concat     a      b        0     NaN            NaN    NaN         NaN         NaN          NaN                 NaN          NaN
    b  concat     b      a       19  0.1045         0.1465 0.2046      0.1909      0.1688        False               False        False
    b  concat     b      b        0     NaN            NaN    NaN         NaN         NaN          NaN                 NaN          NaN
    b    each     a      a       24  0.1392         0.1774 0.0772      0.0692      0.0491  
[... 6 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import numpy as np, pandas as pd
rows=[{'a':1,'p':np.True_},{'a':2},{'a':3,'p':(0.1>0 and min(0.08,0.07,0.0491)<0.05)}]
d=pd.DataFrame(rows); print(d.p.tolist(), d.dropna(subset=['a']).p.sum(), d.p.dtype)
"
```

```
[np.True_, nan, True] 2 object
Shell cwd was reset to
```

**Agent**

numpy booleans in an object column add as logical OR, so the count collapsed to 1. Casting to bool in that cell, and fixing the two text details.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
old='''ok = fig4d.dropna(subset=["mean_r"])
'''
new='''ok = fig4d.dropna(subset=["mean_r"]).astype({"r_within_tol": bool, "spearman_within_tol": bool, "positive_p05": bool})
'''
assert old in s; s=s.replace(old,new); open('nb.py','w').write(s)
r=open('results.py').read()
r=r.replace("mean Spearman 0.147 to 0.212","mean Spearman 0.146 to 0.212")
r=r.replace('''8 task spaces; endpoints + max velocity is negative (-0.125) and endpoints + max speed is at
zero.''','''8 task spaces; endpoints + max velocity is negative (-0.125) and endpoints + max speed is just
above zero (0.0003).''')
r=r.replace("beats endpoints + max speed at k = 3 (0.126 against 0.0)","beats endpoints + max speed at k = 3 (0.126 against 0.0003)")
open('results.py','w').write(r)
EOF
grep -c "0.0003" results.py; python results.py && . dev/bin/activate && python build_nb.py nb_final.py entries/000138-churchland-2010/reproduce_churchland_2010.ipynb
```

```
2
ok
68 cells
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb.py').read()
old='''# The `delay` and `rt` fields agree with the event times to rounding.'''
new='''# The `delay` and `rt` fields agree with the event times to rounding. Eight trials have a delay
# of 0 ms or less (down to -2 ms); the 400 ms rule excludes them.'''
assert old in s; s=s.replace(old,new); open('nb.py','w').write(s)
EOF
python results.py && . dev/bin/activate && python build_nb.py nb_final.py entries/000138-churchland-2010/reproduce_churchland_2010.ipynb
cat > entries/000138-churchland-2010/README.md <<'EOF'
# Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010) from dandiset 000138

Tests the findings of [Churchland et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.015)
that can be tested on [DANDI:000138](https://dandiarchive.org/dandiset/000138/0.220113.0407)
(MC_Maze_Large, Neural Latents Benchmark), which holds 500 maze-task trials over 27 conditions and
162 units recorded with two Utah arrays in one session of monkey J. The paper's J-array dataset had
108 conditions; its single-electrode datasets (monkeys A, B and J) and the EMG are not in the
dandiset.

| Claim | Outcome |
|---|---|
| Single-electrode datasets: weak positive tuning correlation (Figure 4A-C) | Blocked: data missing |
| J-array: weak positive tuning correlation, mean r 0.13 (Figure 4D) | Partially reproduced (assumption) |
| The correlation is near zero by movement onset (Figure 4E) | Not reproduced |
| No effect of anterior-posterior location on the correlation | Reproduced for J-array (assumption) |
| 7 to 10 dimensions hold 90% of preparatory variance | Reproduced (assumption) |
| The peri-movement space captures preparatory tuning best (Figure 6) | Reproduced |
| The peri-movement space wins at almost every dimensionality | Reproduced (assumption) |
| Performance rises with dimensionality and falls beyond about 10 | Reproduced (assumption) |
| The PD performs above zero in most spaces | Reproduced (assumption) |
| Summary over monkeys A, B and J (Figure 6E) | Blocked: data missing |
| A shuffled peri-movement space performs poorly (Figure 7A) | Reproduced (assumption) |
| Starting the window at movement onset keeps 97% of performance (Figure 7B) | Reproduced for J-array (assumption) |
| Anterior and posterior sites perform like random halves (Figure 7C) | Not reproduced (assumption) |
| The PD is most stable in the peri-movement space (Figure 7D) | Reproduced for J-array |
| A linear oscillator shows both findings (Figure 8) | Reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The paper leaves several method details open (the proto-trial used to select trials, movement
onset, what "tuning" in spikes/s means, whether the PCA space is recomputed for each left-out
condition, and others). The notebook runs every reading; "assumption" marks an outcome that
differs between readings and rests on the reading best supported by the paper. The units'
electrode references all point to the PMd array; the array of each unit is taken from the unit id
prefix, which the files do not document. The attempt record, with the reasons and the differences
from the paper's method, is
[`attempts/000138-churchland-2010-01.yaml`](../../attempts/000138-churchland-2010-01.yaml).

- `reproduce_churchland_2010.ipynb`: the analysis. It takes about six minutes, most of it the
  grid of readings for Figure 6.
- `prepspace.py`: loading, trial selection, firing rates, the task, kinematic and peri-movement
  spaces, and leave-one-condition-out PD performance. Other notebooks on this dandiset can import
  it.
EOF
date -u
```

```
ok
68 cells
Wed Oct 28 20:18:00 UTC 2026
Shell cwd was reset to
```

**Agent**

Now the attempt record. Checking the schema for field names.

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(json.dumps(s['required'])); print(list(s['properties']))
o=s['properties']['outcomes']['items']; print(json.dumps(o,indent=0)[:2500])
print(json.dumps(s['properties']['findings'],indent=0)[:1500]); print(json.dumps(s['properties']['provenance'],indent=0)[:1500])
"
```

```
["schema_version", "id", "dataset", "paper", "date", "provenance", "outcomes"]
['schema_version', 'id', 'dataset', 'paper', 'date', 'entry', 'deprecated', 'provenance', 'outcomes', 'verifications', 'findings', 'reconciliation', 'inputs']
{
"type": "object",
"additionalProperties": false,
"required": [
"claim",
"outcome"
],
"properties": {
"claim": {
"description": "Claim id from the target's claims file.",
"type": "string"
},
"outcome": {
"enum": [
"reproduced",
"partially_reproduced",
"not_reproduced",
"blocked"
[... 236 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000138-churchland-2010-01.yaml",
 "content": "schema_version: 2\nid: 000138-churchland-2010-01\ndataset:\n  archive: dandi\n  id: \"000138\"\n  version: 0.220113.0407\n  doi: 10.48324/dandi.000138/0.220113.0407\npaper: doi:10.1016/j.neuron.2010.09.015\ndate: 2026-10-28\nentry: 000138-churchland-2010\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-12\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/40756966342\noutcomes:\n- claim: fig4abc-tuning-correlation-single-electrode\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The dandiset holds only array recordings from one session of monkey J. The\n    single-electrode recordings of monkeys A, B and J (64, 74 and 172 units) are not in it, and\n    no other dandiset or public deposit of them is named by the paper or the archive.\n- claim: fig4d-tuning-correlation-j-array\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig4d-tuning-correlation-j-array\n  measured:\n  - 0.195\n  - 0.212\n  notes: Under the main reading 20 of 162 units pass the inclusion criterion (more than 5\n    spikes/s of preparatory tuning, as a range) and the 1.5 times peri-movement criterion. Mean\n    Pearson r 0.195 and mean Spearman r 0.212, both above tolerance (0.13 +/- 0.013 and 0.11 +/-\n    0.011); the mean r is above zero by all three tests (t-test p = 0.023, on Fisher z p = 0.023,\n    Wilcoxon p = 0.024), which the criterion calls a partial reproduction. Over the eight\n    trial-selection and onset readings with a result, mean r is 0.105 to 0.195 (within tolerance\n    in five), mean Spearman r 0.146 to 0.212 (within tolerance in none), and the mean r is above\n    zero at p < 0.05 in two; in the other six the smallest p of the three tests is 0.074 to 0.169,\n    so those readings give not reproduced. With tuning as the SD across conditions no unit\n    passes. With a ratio of 1.0 in place of 1.5, 52 units give mean r 0.137 (p = 0.0041). The\n    correlation is positive and small, as the paper says; its size and significance at 27\n    conditions depend on the readings.\n  deviations:\n  - The dandiset holds 27 of the 108 conditions and 500 trials (11 to 18 per condition after\n    selection) where the paper's J-array dataset had a mean 2166 trials per neuron; it has 162\n    units where the paper reports 146.\n  - Assumed main reading, as the readings give different outcomes. Trials are those whose\n    concatenated horizontal and vertical velocity profile (movement onset -150 to +800 ms)\n    correlates with the condition's mean profile at r > 0.9 (Supplemental Experimental\n    Procedures, Task design; the window and how the two axes combine are not stated). Requiring\n    each axis to pass keeps 81% of trials and leaves 2 or 3 trials in some conditions, as one\n    velocity component of nearly vertical or horizontal reaches is mostly noise; the\n    concatenated test keeps 96%, and the paper reports \"typically ~90%\" with outliers only\n    occasional. Movement onset is the trial table's `move_onset_time`; the paper refers to\n    Churchland et al. 2006c, not available here, and the speed-threshold reading (10% of peak\n    speed, a median 14 ms later) is also run.\n  - Tuning in spikes/s is taken as the range of condition means. The SD reading leaves 6 or 7 of\n    162 units above 5 spikes/s, which does not fit a criterion the paper describes as lower than\n    for single electrodes to suit array data (Methods, Neural recordings and datasets).\n  - The test of the mean against zero is not named; the three readings of the claims file are\n    run and agree under the main reading.\n- claim: fig4e-correlation-time-course\n  outcome: not_reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig4e-correlation-time-course\n  measured: 0.218\n  notes: Mean correlation over the 20 Figure 4D units is 0.773 at -400 ms, 0.764 at -300 ms,\n    0.713 at -250 ms, 0.572 at -200 ms and 0.218 at movement onset; it falls below 0.1 only\n    between +150 and +200 ms (0.110, 0.064). The decline starts about 250 ms before onset and\n    the value at onset is below half of that at -250 ms, as the criterion asks, but it is not\n    below 0.1 at onset. All eight readings give 0.129 to 0.218 at onset and meet the other two\n    parts. The measured value is the correlation at movement onset under the main reading.\n  deviations:\n  - The rate at each time point comes from the movement-locked average, the part of the paper's\n    spliced trace locked to movement onset (Supplemental Experimental Procedures, Computing the\n    mean firing rate versus time); the paper chose the splice points to minimise\n    discontinuities and does not give them. The go-locked curve is shown alongside.\n  - 27 of 108 conditions and 20 units, as for fig4d-tuning-correlation-j-array.\n- claim: results-ap-location-no-effect\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:results-ap-location-no-effect\n  notes: Only the J-array dataset can be tested. Regressing the per-unit correlation of Figure 4D\n    on array (prefix 1 coded anterior) gives r = 0.047, p = 0.844 under the main reading (12\n    anterior and 8 posterior units, mean r 0.209 and 0.176), and p from 0.432 to 0.844 over the\n    eight readings, so no reading finds an effect at p < 0.05. The paper reports r = 0.20,\n    p = 0.27 for J-array. The other three datasets are not in the dandiset.\n  deviations:\n  - Electrode coordinates are NaN, so reading (a), the AP coordinate on the array, cannot be\n    run. Reading (b), array membership, is used.\n  - Assumed array of each unit. Every unit references an electrode of the PMd group, but the\n    unit ids carry a prefix (1 for 83 units, 2 for 79) and a channel, and the referenced\n    electrode is the channel minus one for both prefixes. The prefix is taken as the array, and\n    prefix 1 as PMd, the group the references name. Prefix 1 units also have more preparatory\n    tuning (median range 6.71 against 4.79 spikes/s), consistent with the paper's remark that\n    preparatory activity is more prevalent at anterior sites. Swapping the arrays would only flip\n    the sign of r.\n  - Monkeys A, B and J (single-electrode) are not tested.\n- claim: supp-preparatory-dimensionality\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:supp-preparatory-dimensionality\n  measured: 11\n  notes: Under the main reading 11 components capture 90% of the variance of the 27 x 162\n    matrix of preparatory condition means, inside the widened range 6.3 to 11, and 10 with the\n    92 included units. Under the per-axis trial selection the counts are 12 (outside) and 11;\n    with the 6 or 7 units of the SD tuning reading the count is 4. On each half of the trials the\n    count is 14 and 13, so trial noise adds dimensions at these trial counts. Only J-array is\n    tested, with 27 conditions where the paper had 108.\n  deviations:\n  - Assumed main reading for trial selection, as in fig4d-tuning-correlation-j-array; the\n    claims file's readings of which units enter (all, or included) both fall in range under it.\n  - The single-electrode datasets (per 27-condition set for monkey J) are not in the dandiset.\n- claim: fig6-peri-movement-space-best\n  outcome: reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-peri-movement-space-best\n  notes: Under the main reading, over 92 included units, the peri-movement space's best mean\n    performance is 0.351 (k = 10), above the kinematic space (0.103, k = 4) and every task space\n    (best, kitchen sink, 0.250). Over the 2048 combinations of readings it is best in 1468; the\n    criterion asks for one combination. It is best in 95% of combinations with tuning as a range\n    and 49% with the SD (6 or 7 units), and in 94% with all units in the T-matrix against 50%\n    with included units only. Best k is 7 or more in 1776 of 2048 combinations. EMG was not\n    recorded for J-array.\n  deviations:\n  - Only J-array, on 27 of 108 conditions; the claim says \"for every dataset\" and the other\n    three are not in the dandiset.\n  - Task spaces are measured on each condition's mean hand trajectory from movement onset to the\n    reach end (standard choice; the paper speaks of the \"average endpoint and peak velocity for\n    each condition\"). Acceleration for the kinematic space is the derivative of the mean velocity\n    (standard choice). Replicating the six kinematic variables to the number of units gives the\n    same PD fits, so they are used once.\n  - Movement onset, trial selection and tuning as in fig4d-tuning-correlation-j-array; every\n    reading is run.\n- claim: fig6-each-dimensionality\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-each-dimensionality\n  notes: Under the main reading the peri-movement space wins 20 of 22 comparisons (0.909, at\n    least 0.8 needed) and beats endpoints + max speed at k = 3 (0.126 against 0.0003). Over all\n    combinations the criterion is met in 1074 of 2048 (share won from 0 to 1, median 0.85). It is\n    met in 69% of combinations with the concatenated trial selection and 36% with the per-axis\n    one, 75% and 30% for tuning as range or SD, 67% and 38% for all or included units in the\n    T-matrix, and 37% and 68% with the space computed once or refit. The kinematic space at\n    k = 1 and k = 14 is the one it loses to under the main reading (by 0.005 and 0.004).\n  deviations:\n  - Assumed main reading, as the readings give different outcomes. Besides the readings of\n    fig4d-tuning-correlation-j-array, the PCA space is computed once from all conditions, and\n    only the PD fit leaves a condition out. The Methods say \"One condition was left out and we\n    found the PD that best captured tuning for the remaining conditions\", the Results say \"we\n    computed the PD based on all but one condition\", and both describe leaving out a condition\n    only for the PD; Figure 5 plots the left-out conditions in the same space. All units enter\n    the T-matrix (\"neurons with weak peri-movement activity were included\", Methods, PCA-based\n    spaces). Performance is averaged over units (\"Performance (averaged across neurons)\",\n    Results, PD performance in a variety of spaces).\n  - Only J-array, on 27 of 108 conditions.\n- claim: fig6-dimensionality-trend\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-dimensionality-trend\n  notes: Under the main reading peri-movement performance rises from 0.056 at k = 1 to 0.351 at\n    k = 10 and falls to -0.456 at k = 14; the kinematic space does the same (0.061, best 0.103 at\n    k = 4, -0.451 at k = 14). The criterion is met in 992 of 2048 combinations, 91% of those with\n    the space computed once and 6% of those with the space refit without the left-out condition;\n    refit, performance keeps rising (0.461 at k = 14 under the main reading otherwise) and the\n    best k is 10 to 14.\n  deviations:\n  - Assumed main reading, with the space computed once from all conditions, as argued under\n    fig6-each-dimensionality. The outcome rests mainly on this choice.\n  - Only J-array, on 27 of 108 conditions.\n- claim: fig6-pd-adequate-all-spaces\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-pd-adequate-all-spaces\n  notes: Under the main reading mean performance is above zero for the peri-movement space\n    (0.351) and kinematic space (0.103) at their best k, and for 7 of 8 task spaces; endpoints +\n    max velocity is -0.125 and endpoints + max speed 0.0003. The criterion is met in 1936 of\n    2048 combinations; the others have 3 or 4 task spaces above zero.\n  deviations:\n  - Assumed main reading, as for fig6-each-dimensionality.\n  - Only J-array, on 27 of 108 conditions.\n- claim: fig6e-summary-rank\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The summary combines monkeys A, B and J (single-electrode) and uses their EMG spaces;\n    none of these data are in the dandiset, which holds only the J-array session.\n- claim: fig7a-shuffled-space-poor\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7a-shuffled-space-poor\n  notes: Under the main reading, over 20 draws, the shuffled space's best mean performance is\n    0.014 (k = 3), below the peri-movement space at every k and below the kinematic space's best\n    (0.103). The criterion also holds with proto-trial (b), onset (b), included units in the\n    T-matrix, pooled performance and the kinematic window ending with the reach. It fails with\n    the per-axis trial selection (the shuffled space is not below the peri-movement space at\n    every k, where the latter collapses at high k) and with the space refit per fold (shuffled\n    best 0.178 over 5 draws, above the kinematic best of 0.160, below the peri-movement best of\n    0.461).\n  deviations:\n  - Assumed main reading, as for fig6-each-dimensionality.\n  - Judged on J-array alone, where Figure 7A averages all datasets. The refit variant uses 5\n    draws in place of 20 to keep the run short.\n- claim: fig7b-window-start-onset\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7b-window-start-onset\n  measured: 0.908\n  notes: Under the main reading the best performance with the window from movement onset is\n    0.318 (k = 9) against 0.351 (k = 10) from -150 ms, a ratio of 0.908, inside 0.873 to 1.067.\n    Over all combinations the ratio is within tolerance in 1336 of 2048 (median 0.917, range\n    0.367 to 2.004), in 47% of combinations with the space computed once and 84% with it refit.\n    Reading (a) of the claims file (J-array against 0.97) is the one run; the 0.94 for monkeys A\n    and B, and reading (b), which needs the J single-electrode dataset, cannot be tested. The\n    measured value is for the first expected value.\n  deviations:\n  - Assumed main reading, as for fig6-each-dimensionality.\n  - Monkeys A, B and the J single-electrode dataset are not in the dandiset.\n- claim: fig7c-anterior-posterior\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7c-anterior-posterior\n  notes: Under the main reading, with the upper limit from the preparatory PCA space of all units\n    in each subset at k = 6, normalized performance is 0.597 for the anterior array (55 included\n    units) and 0.382 for the posterior array (37), against 0.617 for random halves; anterior is\n    within 10% (ratio 0.968), posterior is not (0.618). Anterior exceeds posterior, as the paper\n    reports. Of 16 combinations of readings (upper limit at k = 6 or best k, with or without the\n    unit being fit, space once or refit, trial selection, T-matrix units), 2 meet the criterion,\n    both with the space refit and the unit included in the upper-limit space.\n  deviations:\n  - Assumed array of each unit from the id prefix, as for results-ap-location-no-effect; with a\n    binary location, the median split gives the two arrays.\n  - The upper-limit space is \"derived from the preparatory activity of all neurons\"\n    (Supplemental Experimental Procedures, Estimating the upper limit); the main reading\n    includes the unit being fit, as \"all neurons\" says, and the other reading is run. Whether it\n    is taken at k = 6 or its best k is open in the claims file; both are run.\n  - Random halves are 20 random splits of all units (4 in the refit variants); the paper does\n    not say how many.\n  - Judged on J-array alone, where Figure 7C averages the datasets.\n- claim: fig7d-pd-consistency\n  outcome: reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7d-pd-consistency\n  notes: Under the main reading, over 92 units and 100 draws each, the peri-movement space has the\n    higher mean consistency in all three comparisons, 0.756 against 0.610 (endpoints + max speed,\n    k = 3), 0.684 against 0.570 (segment directions, k = 6) and 0.748 against 0.666 (kinematic,\n    k = 4, its best k). It is higher in every comparison under all eight variants of the readings\n    and with the axes as they are or scaled to unit SD, so the outcome does not rest on these\n    choices. EMG was not recorded for J-array.\n  deviations:\n  - Only J-array; the claim covers four datasets.\n  - The spaces are computed once from all 27 conditions; whether axes are scaled before the PD is\n    fitted is not stated, and both are run.\n- claim: fig8-oscillator-model\n  outcome: reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig8-oscillator-model\n  measured: 0.012\n  notes: A simulation with no recorded data. Over 1000 draws of 25 initial states, the\n    correlation between unit 1's held state and its mean released activity has a median of\n    -0.019 to 0.012 and a central 95% of about -0.41 to 0.40 under each reading (uniform or\n    Gaussian initial states, a full or half cycle), which contains 0.08. A PD in the 2-D PCA space\n    of the released activity of both units captures unit 1's initial state with leave-one-out\n    performance 1.0 in every draw. The measured value is the median r under the first reading.\n  deviations:\n  - The paper's 0.08 comes from one draw; the criterion judges it against the distribution over\n    draws.\n  - The hold lasts 50 steps (it cannot change the result, as the held state is constant).\nfindings:\n- kind: data_missing\n  statement: The dandiset holds one session of monkey J's array recordings on the maze task, cut\n    to 500 trials over 27 conditions for the Neural Latents Benchmark. The paper's J-array\n    dataset had 108 conditions and a mean 2166 trials per neuron, and its single-electrode\n    datasets of monkeys A, B and J and all EMG recordings are not in the dandiset, so two of the\n    paper's main findings cannot be tested and the rest only on J-array.\n- kind: metadata_error\n  statement: Every unit's electrode reference points into the PMd group of the electrodes table.\n    The unit ids encode a prefix (1 for 83 units, 2 for 79) and a channel, and the referenced\n    electrode is the channel minus one for both prefixes, so the 79 units of one array reference\n    electrodes of the other. The heldout units split 20 and 20 between the prefixes.\n- kind: metadata_insufficient\n  statement: Which id prefix is the PMd array and which the M1 array is not stated, and all\n    electrode coordinates (x, y, z) are NaN, so neither array membership nor position on the\n    array can be read from the files. Anterior-posterior analyses here rest on an assumption.\n- kind: identifier_missing\n  statement: Nothing in the dandiset or the paper says whether the 2009-10-06 session is the one\n    behind the paper's J-array dataset. The file has 162 units where the paper reports 146\n    isolations, and 27 of its 108 conditions.\n- kind: other\n  statement: Hand, cursor and eye position are at 1 kHz and only within trials, where the paper\n    tracked the hand at 60 Hz and the eye at 240 Hz; the resampling is not described. Hand\n    velocity agrees with the derivative of hand position (slope 1.000).\n- kind: other\n  statement: Eight trials have a delay of 0 ms or less (down to -2 ms), where the `delay` field is\n    described as the delay between target presentation and go cue.\n- kind: paper_inconsistency\n  statement: The mean trials per neuron of the J-array dataset is 2166 in the Results and 2155 in\n    the Methods.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. Is the PCA space (peri-movement and kinematic)\n    computed once from all conditions, with only the PD regression leaving a condition out, or\n    recomputed without the left-out condition? Computed once, performance peaks at k = 10 and\n    falls beyond (as the paper reports); recomputed, it keeps rising to k = 14, and the outcomes of\n    fig6-each-dimensionality, fig6-dimensionality-trend, fig7a and fig7c change. This attempt\n    assumed the space is computed once.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. How was the maze proto-trial defined, over which\n    window, and did the horizontal and vertical profiles each need r > 0.9 or the two together?\n    Requiring each keeps 81% of trials here and leaves 2 or 3 trials in some conditions; the\n    concatenated profile keeps 96%; the paper says about 90%. The fig4d result moves between mean\n    r 0.105 and 0.195 across these readings and the movement onset method. This attempt assumed\n    the condition's mean profile, the concatenated test and the window -150 to +800 ms.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. What does \"spikes/s of preparatory tuning\" measure\n    (the range of condition means, their SD, or another quantity), and how was movement onset\n    detected? With the range, 92 of 162 units pass the 5 spikes/s criterion; with the SD, 6. This\n    attempt assumed the range and used the dataset's movement onset times.\n- kind: methods_unavailable\n  statement: Question for the paper's authors. For Figure 7C, did the upper-limit space of a\n    subset include the neuron being fit, and at which dimensionality was it taken? The\n    normalized posterior performance relative to random halves is 0.62 with the neuron included\n    at k = 6 and 0.79 without it; this attempt assumed it included, as \"all neurons\" says.\n"
}
```

```
File created successfully at: attempts/000138-churchland-2010-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent**

Checking the record for YAML plain scalars containing ": ", then running the entry check.

**Agent calls Bash**

```bash
python - <<'EOF'
import yaml
d=yaml.safe_load(open('attempts/000138-churchland-2010-01.yaml'))
def walk(x,p=''):
    if isinstance(x,dict):
        for k,v in x.items(): walk(v,p+'/'+str(k))
    elif isinstance(x,list):
        for i,v in enumerate(x): walk(v,p+f'[{i}]')
    elif isinstance(x,str) and ': ' in x: print(p, x[:80])
walk(d); print(len(d['outcomes']), [o['outcome'] for o in d['outcomes']])
EOF
python tools/entry.py check entries/000138-churchland-2010 2>&1 | tail
```

```
15 ['blocked', 'partially_reproduced', 'not_reproduced', 'reproduced', 'reproduced', 'reproduced', 'reproduced', 'reproduced', 'reproduced', 'blocked', 'reproduced', 'reproduced', 'not_reproduced', 'reproduced', 'reproduced']
0 error(s)
```

**Agent**

Record validates. Final clean run of the entry.

**Agent calls Bash**

```bash
date -u && python tools/entry.py all entries/000138-churchland-2010 2>&1 | tail -3
```

```
Wed Oct 28 20:19:58 UTC 2026
Installed kernelspec registry-000138-churchland-2010 in executed/000138-churchland-2010/.venv/share/jupyter/kernels/registry-000138-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (340 s)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python show.py executed/000138-churchland-2010/reproduce_churchland_2010.ipynb > final_out.txt 2>&1; grep -n -E "ERROR|Readings with a result|Range of mean r|Trials with delay|Notebook run|k90 =|Combinations of|1074|992 of|1936|1336|Rows meeting|0 of 8|8 of 8|Median preparatory|ratio >=" final_out.txt; diff <(python show.py run1.ipynb 2>&1 | grep -v -E "computed in|run time|Grid computed|Smoothed rates|loaded dandiset") <(grep -v -E "computed in|run time|Grid computed|Smoothed rates|loaded dandiset" final_out.txt) | head -30
```

```
65:Trials with delay of 0 ms or less: 8
133:Median preparatory tuning (range) by id prefix: {1: 6.71, 2: 4.79}
161:Readings with a result: 8 ; both means within tolerance: 0 ; mean r positive at p < 0.05: 2
162:Range of mean r over readings with a result: 0.105 to 0.195 ; mean Spearman: 0.146 to 0.212
166:peri/prep tuning ratio >= 1.0: 52 units, mean r 0.137, mean Spearman 0.132, t-test p 0.0041
167:peri/prep tuning ratio >= 1.25: 35 units, mean r 0.106, mean Spearman 0.114, t-test p 0.0687
168:peri/prep tuning ratio >= 1.5: 20 units, mean r 0.195, mean Spearman 0.212, t-test p 0.0233
169:peri/prep tuning ratio >= 2.0: 12 units, mean r 0.202, mean Spearman 0.231, t-test p 0.0450
181:Readings meeting the criterion: 0 of 8
243:Readings with no effect (p >= 0.05): 8 of 8
258:Split halves of trials (seed 4): k90 = 14 and 13
265:Combinations of readings: 2048 ; peri-movement space best in 1468
344:Combinations meeting the criterion: 1074 of 2048
363:Combinations meeting the criterion (peri-movement): 992 of 2048 ; kinematic: 1776
382:Combinations meeting the criterion: 1936 of 2048
434:Combinations within tolerance: 1336 of 2048
468:Rows meeting the criterion: 2 of 16
526:Notebook run time: 5.5 min
63a64
> Trials with delay of 0 ms or less: 8
[... 29 more lines not kept]
```

**Agent**

Executed numbers match the text. Building the handover package.

**Agent calls Bash**

```bash
python tools/entry.py handover entries/000138-churchland-2010 2>&1 | tail -5; ls executed/000138-churchland-2010/handover/; git status --short; date -u
```

```
wrote executed/000138-churchland-2010/handover
10.1016-j.neuron.2010.09.015.yaml
prepspace.py
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
?? attempts/000138-churchland-2010-01.yaml
?? entries/000138-churchland-2010/
?? scripts
Wed Oct 28 20:26:35 UTC 2026
```

**Agent calls Bash**

```bash
ls -la entries/000138-churchland-2010/; git check-ignore -v entries/000138-churchland-2010/__pycache__ 2>&1 | head -2
```

```
total 148
drwxr-xr-x  4 runner runner  4096 Oct 28 20:18 .
drwxr-xr-x 88 runner runner  4096 Oct 28 19:53 ..
drwxr-xr-x  3 runner runner  4096 Oct 28 19:53 .claude
-rw-r--r--  1 runner runner  3110 Oct 28 20:18 README.md
drwxr-xr-x  2 runner runner  4096 Oct 28 20:01 __pycache__
-rw-r--r--  1 runner runner   998 Oct 28 20:10 entry.yaml
-rw-r--r--  1 runner runner 24007 Oct 28 20:01 prepspace.py
-rw-r--r--  1 runner runner 86088 Oct 28 20:18 reproduce_churchland_2010.ipynb
-rw-r--r--  1 runner runner    58 Oct 28 20:10 requirements.in
-rw-r--r--  1 runner runner  5618 Oct 28 20:10 requirements.lock.txt
.gitignore:1:__pycache__/	entries/000138-churchland-2010/__pycache__
```

**Agent calls Bash**

```bash
find entries/000138-churchland-2010/.claude -type f | head; git check-ignore -v entries/000138-churchland-2010/.claude/x 2>&1
```

```
Exit code 1
```

**Agent calls Bash**

```bash
find entries/000138-churchland-2010/.claude; rmdir -p entries/000138-churchland-2010/.claude/* 2>/dev/null; find entries/000138-churchland-2010/.claude 2>&1 | head -3
```

```
Permission for this tool use was denied. It requires approval, and this session has no approval surface — nobody can answer a permission prompt here — so it was denied automatically. The action was NOT performed; do not claim it succeeded, and do not retry it: this action, and anything else that requires approval, will be denied the same way for the rest of this session. Tell the user what was blocked and why you needed it, then continue with the parts of the task that do not require approval. What required approval: This Bash command contains multiple operations. The following part requires approval: find entries/000138-churchland-2010/.claude; rmdir -p entries/000138-churchland-2010/.claude/* ; find entries/000138-churchland-2010/.claude 2>&1
```

**Agent**

I've done steps 1 to 6 of the Author section: the entry runs from a clean environment in 5.7 min (`python tools/entry.py all` passes, 0 check errors), the attempt record is written, and the handover is built in `executed/000138-churchland-2010/handover/`. Nothing is committed.

The dandiset holds one session of monkey J (2009-10-06): 500 maze trials over 27 conditions, 162 array units, and hand, cursor and eye position. I pinned version 0.220113.0407 because the paper cites no version, it is the only published one, and the draft holds the same two blobs.

**(1) Outcomes**

| Claim | Outcome |
|---|---|
| fig4abc-tuning-correlation-single-electrode | blocked, data_missing |
| fig4d-tuning-correlation-j-array | partially reproduced, assumed (mean r 0.195, Spearman 0.212, p = 0.023) |
| fig4e-correlation-time-course | not reproduced (r is 0.218 at movement onset) |
| results-ap-location-no-effect | reproduced for J-array only, assumed (p = 0.84) |
| supp-preparatory-dimensionality | reproduced, assumed (11 components) |
| fig6-peri-movement-space-best | reproduced (0.351 vs best task space 0.250 and kinematic 0.103) |
| fig6-each-dimensionality | reproduced, assumed (wins 20 of 22 comparisons) |
| fig6-dimensionality-trend | reproduced, assumed |
| fig6-pd-adequate-all-spaces | reproduced, assumed |
| fig6e-summary-rank | blocked, data_missing |
| fig7a-shuffled-space-poor | reproduced, assumed |
| fig7b-window-start-onset | reproduced for J-array only, assumed (ratio 0.908) |
| fig7c-anterior-posterior | not reproduced, assumed (posterior at 0.62 of random halves) |
| fig7d-pd-consistency | reproduced for J-array (higher in every comparison and variant) |
| fig8-oscillator-model | reproduced (simulation) |

**(2) The dataset, assumptions, questions**
- **Coverage:** only J-array can be tested, on 27 of the paper's 108 conditions and 500 trials. The file has 162 units where the paper reports 146, and nothing says whether this is the paper's session. The single-electrode datasets (monkeys A, B, J) and all EMG are missing.
- **Unit metadata error:** every unit references a PMd electrode. The unit ids carry a prefix (1 for 83 units, 2 for 79) plus a channel, and the reference is channel minus one for both prefixes, so one array's units point at the other array's electrodes. Electrode coordinates are all NaN.
- **Smaller findings:**
  - Hand data are resampled to 1 kHz within trials only (the paper tracked at 60 Hz).
  - Eight trials have a delay of 0 ms or less.
  - The paper gives 2166 trials per neuron in the Results and 2155 in the Methods.
- **Assumptions:**
  - Array membership comes from the id prefix, with prefix 1 taken as PMd.
  - Trials are selected by correlating the concatenated velocity profile with the condition's mean profile. Requiring each axis separately keeps 81% of trials and leaves 2 or 3 in some conditions; the paper says about 90%.
  - Movement onset is the dataset's own `move_onset_time`.
  - Tuning is the range of condition means. The SD reading leaves only 6 of 162 units.
  - The PCA space is computed once from all conditions; the paper describes leaving a condition out only for the PD fit.
  - All units enter the T-matrix, and performance is averaged over units.
  - For Fig 7C, the upper-limit space includes the unit being fit.
- **Readings run:** 2048 combinations of readings for Figure 6 and 7B, one at a time for 7A, 7C and 7D.
- **Questions for the paper's authors:** four, recorded as `methods_unavailable` findings: space computed once vs refit; the proto-trial and its window; the tuning measure and onset method; the Fig 7C upper limit.
- **Questions to a reader:** none.

**(3) Where the protocol was unclear**
1. With many open details, it doesn't say whether to run the full product of readings or one at a time. I ran the full grid where it was cheap (Figure 6, 7B) and one at a time elsewhere, and said which in the notebook.
2. It doesn't say what outcome a claim gets when it spans four datasets and only one is in the dandiset. I judged the testable part and listed the missing datasets as deviations; I did not mark these "partially reproduced".
3. `measured` must give one value per expected value, but fig7b's second value (monkeys A, B) cannot be measured. I gave one number and said which expected value it matches.
4. It is unclear whether an author-added reading, one the claims file doesn't name (here the per-axis vs concatenated velocity test), counts under "reproduced under any reading" or under the step 1.6 assumption rule. I treated it under step 1.6.
5. fig8 is marked `with_inputs` but uses no outside input, so `inputs` is empty; the protocol doesn't cover this case.

**(4) Runtime and failures**
- About 45 minutes of the 5 hours (19:45 to 20:27 UTC). The notebook takes 5.5 to 5.7 minutes.
- Development bugs, all fixed before the final run: hand samples are not on a continuous grid; `.combine` is a pandas method; numpy booleans in an object column summed as OR and printed 1 where 2 was right.
- An empty `.claude` directory appeared inside the entry, and stray dotfiles appeared at the repo root; I didn't create them. Removing the directory was denied for lack of an approval surface. Git ignores empty directories, so it won't be committed, but the root dotfiles will be unless someone removes them.

## End of run

67 turns, 40 minutes, result: success.
