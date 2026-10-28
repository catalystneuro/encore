# 000139 · author · run 40756774586

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls
```

```
<persisted-output>
Output too large (35.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fb3175ca-7f04-43f3-89e1-4113f65e12bf/tool-results/bxy3pjumg.txt

Preview (first 2KB):
Wed Oct 28 19:47:59 UTC 2026
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
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/fb3175ca-7f04-43f3-89e1-4113f65e12bf/tool-results/bxy3pjumg.txt"
}
```

```
1	Wed Oct 28 19:47:59 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-12`. Record this version in the attempt's provenance.
5	
6	This is what agents, or people, do to attempt a target and deposit the
7	result. A target is a dataset in a public archive and a paper it names. How
8	each archive's datasets are named, versioned and read is in
9	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
10	([pilot notes](pilot-notes.md)); the reasons for the rules are there.
11	
12	An attempt has three roles, each a separate run with a separate context:
13	
14	- The **reader** reads the paper and writes the claims file: every finding,
15	  and how each is to be tested, taken from the paper. A second reader checks
16	  it against the paper. Readers never see the dataset's data.
17	- The **author** tests the claims on the dataset. It reads the paper to
18	  understand the claims, but the claims file binds it: it cannot change a
19	  claim's statement, expected values or criterion. A method detail the file
20	  lacks it takes from the paper, citing the passage, and it asks a reader
[... 619 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -150; wc -l docs/design.md docs/archives.md; ls claims/000139 paper entries/001453-fouke-2025 claims/001453
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
[... 140 more lines not kept]
```

**Agent calls Bash**

```bash
cat claims/000139/*.yaml
```

```
<persisted-output>
Output too large (37.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fb3175ca-7f04-43f3-89e1-4113f65e12bf/tool-results/bfyc5ougc.txt

Preview (first 2KB):
# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000139.
# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
# protocol as stated in docs/protocol.md (version pilot-12).
#
# Text read: the NIH author manuscript in PubMed Central (PMC2991102), as extracted to
# paper/10.1016-j.neuron.2010.09.015.txt, with its Results, Methods, figure legends and the one
# supplement (NIHMS240235-supplement-01.pdf: Supplemental Figures 1 to 5, Supplemental Text and
# Supplemental Experimental Procedures). Not the version of record. The figures themselves are not
# in the text; values plotted only in Figures 4, 6 and 7 are not available and no claim rests on
# them. The paper links no code, so every method below comes from the Methods, the legends or the
# supplement.
#
# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
# Procedures). Three adult male rhesus monkeys (A, B, J), delayed reaches from a central touch spot
# to a target on a fronto-parallel screen. Trial events: target onset (the target jitters), go cue
# (jitter stops and the touch spot disappears), movement onset. Delays about 0 to 1000 ms; only
[... 9 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/fb3175ca-7f04-43f3-89e1-4113f65e12bf/tool-results/bfyc5ougc.txt"
}
```

```
1	# Claims for Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400, on dandiset 000139.
2	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-10-28,
3	# protocol as stated in docs/protocol.md (version pilot-12).
4	#
5	# Text read: the NIH author manuscript in PubMed Central (PMC2991102), as extracted to
6	# paper/10.1016-j.neuron.2010.09.015.txt, with its Results, Methods, figure legends and the one
7	# supplement (NIHMS240235-supplement-01.pdf: Supplemental Figures 1 to 5, Supplemental Text and
8	# Supplemental Experimental Procedures). Not the version of record. The figures themselves are not
9	# in the text; values plotted only in Figures 4, 6 and 7 are not available and no claim rests on
10	# them. The paper links no code, so every method below comes from the Methods, the legends or the
11	# supplement.
12	#
13	# Data the paper used (Results, Behavior and recordings; Methods; Supplemental Experimental
14	# Procedures). Three adult male rhesus monkeys (A, B, J), delayed reaches from a central touch spot
15	# to a target on a fronto-parallel screen. Trial events: target onset (the target jitters), go cue
16	# (jitter stops and the touch spot disappears), movement onset. Delays about 0 to 1000 ms; only
17	# trials with delays above 400 ms analysed. Four datasets. Monkeys A and B, speed task, 28
18	# conditions (7 directions, 2 distances, 2 instructed speeds), single electrodes, 64 and 74
19	# single units. Monkey J, maze task, single electrodes, 172 single units, recorded on four sets of
20	# 27 conditions each (about 53 neurons per set; population analyses done per set, then averaged).
[... 513 more lines not kept]
```

**Agent calls Bash**

```bash
cat attempts/001453-fouke-2025-01.yaml | head -200; cat entries/001453-fouke-2025/entry.yaml entries/001453-fouke-2025/requirements.in entries/001453-fouke-2025/README.md
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
[... 243 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "DANDI" -A80 docs/archives.md | head -150
```

```
4:the DANDI Archive. The protocol is written for any archive. What is particular
5-to an archive (how its datasets are named, versioned and read) is here, and an
6-agent is pointed to its archive's section.
7-
8-A dataset is keyed as `<archive>:<id>` and shown as `<LABEL>:<id>`, for example
9:`DANDI:000003`. Its files in this repository (`claims/`, `questions/`,
10-`transcripts/`, the `attempt/` branch, the paper store) are under its folder
11:name: the identifier alone for DANDI, which the registry began with, and
12-`<archive>-<id>` for any other archive. Each archive is an adapter, a module in `tools/archives/` ("Adding an archive",
13-below), and `tools/datasets.py` turns one form of a dataset's name into another.
14-The workflows take a dataset in any of these forms.
15-
16:## DANDI
17-
18-- **Datasets.** A dandiset, identified by six digits (`000003`). Targets are the
19-  public dandisets whose metadata names a paper (`targets/dandisets.json`, built
20:  by `tools/build_targets.py` and refreshed daily by the Track DANDI workflow).
21-- **Versions.** A published version (`0.220126.1855`) is fixed and has a DOI,
22-  `10.48324/dandi.<id>/<version>`. The draft can change. Pin the version the
23-  paper cites, or the latest published one. For a draft, record its
[... 127 more lines not kept]
```

**Agent**

Read the protocol and the claims file (21 claims). Now surveying the dandiset.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000139/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000139/versions/" | python -m json.tool | head -60
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s "https://api.dandiarchive.org/api/dandisets/000139/versions/0.220113.0408/" > meta.json; python -c "
import json;m=json.load(open('meta.json'));print(m.get('description'));print(m.get('relatedResource'));print(m.get('citation'));print(m.get('assetsSummary'))"; curl -s "https://api.dandiarchive.org/api/dandisets/000139/versions/0.220113.0408/assets/" | python -m json.tool
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
python -c "import pynwb, remfile, h5py, numpy, scipy, sklearn; print(pynwb.__version__)" 2>&1; which uv python; python --version
```

```
Traceback (most recent call last):
  File "<string>", line 1, in <module>
    import pynwb, remfile, h5py, numpy, scipy, sklearn; print(pynwb.__version__)
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ModuleNotFoundError: No module named 'pynwb'
/opt/hostedtoolcache/Python/3.13.17/x64/bin/uv
/opt/hostedtoolcache/Python/3.13.17/x64/bin/python
Python 3.13.17
```

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q dev && . dev/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy pandas matplotlib dandi diptest 2>&1 | tail -3; python -c "import pynwb, diptest; print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey.py <<'EOF'
import remfile, h5py, pynwb, requests, numpy as np
V='0.220113.0408'
for aid in ['7ef450a8-8684-42e2-8598-cd38ca2b2e50','ac554f8e-7008-4030-9640-6f1cf838a23c']:
    r=requests.get(f'https://api.dandiarchive.org/api/dandisets/000139/versions/{V}/assets/{aid}/')
    url=[u for u in r.json()['contentUrl'] if 's3' in u][0]
    print(url)
    f=h5py.File(remfile.File(url),'r')
    io=pynwb.NWBHDF5IO(file=f,load_namespaces=True); nwb=io.read()
    print(nwb)
    print(nwb.subject)
    print('desc', nwb.session_description, nwb.experiment_description, nwb.related_publications)
    tr=nwb.trials.to_dataframe(); print(tr.shape); print(tr.dtypes); print(tr.head(3).T)
    u=nwb.units.to_dataframe(); print(u.shape); print(u.columns.tolist()); print(u.head(3).T)
    for k,m in nwb.processing.items():
        for n,d in m.data_interfaces.items():
            print(k,n,type(d).__name__)
            if hasattr(d,'spatial_series'):
                for s,ss in d.spatial_series.items(): print('  ',s,ss.data.shape,ss.unit,ss.rate,ss.starting_time, ss.timestamps.shape if ss.timestamps is not None else None, ss.description)
            elif hasattr(d,'time_series'):
                for s,ss in d.time_series.items(): print('  ',s,ss.data.shape,ss.unit,ss.rate,ss.description)
            else: print('  ',d)
    print('acq',list(nwb.acquisition)); print('eg', {k:(v.location,v.description) for k,v in nwb.electrode_groups.items()})
    if nwb.electrodes is not None: print(nwb.electrodes.to_dataframe().head())
EOF
python survey.py 2>&1 | head -300
```

```
https://dandiarchive.s3.amazonaws.com/blobs/8d0/80d/8d080d41-978f-4e60-b929-84fd12165e5f
root pynwb.file.NWBFile at 0x129210022077040
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
  experiment_description: Center-out delayed reaching task with maze barriers.
  experimenter: ['Mark M. Churchland' 'Matthew T. Kaufman']
  file_create_date: [datetime.datetime(2021, 9, 1, 22, 21, 37, 661173, tzinfo=tzoffset(None, -14400))]
  identifier: 80434ca8-0b94-11ec-8a4f-bfff5c83b3dd
  institution: Stanford University
  intervals: {
    trials <class 'pynwb.epoch.TimeIntervals'>
  }
[... 223 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey2.py <<'EOF'
import remfile, h5py, pynwb, numpy as np, pandas as pd
pd.set_option('display.width',200); pd.set_option('display.max_columns',30)
url='https://dandiarchive.s3.amazonaws.com/blobs/8d0/80d/8d080d41-978f-4e60-b929-84fd12165e5f'
f=h5py.File(remfile.File(url),'r')
nwb=pynwb.NWBHDF5IO(file=f,load_namespaces=True).read()
e=nwb.electrodes.to_dataframe(); print(e.columns.tolist()); print(e.drop(columns=['group']).describe(include='all'))
print(e.drop(columns=['group']).head())
u=nwb.units.to_dataframe()
print(u.heldout.value_counts())
ue=[int(np.asarray(x.index)[0]) if len(x) else None for x in u.electrodes]
print('units per electrode-row sample', ue[:20], len(set(ue)))
print('elec col desc', {c:nwb.electrodes[c].description for c in nwb.electrodes.colnames})
print('units col desc', {c:nwb.units[c].description for c in nwb.units.colnames})
print('trial col desc', {c:nwb.trials[c].description for c in nwb.trials.colnames})
tr=nwb.trials.to_dataframe()
print(tr.split.value_counts(), tr.success.value_counts())
print(tr[['trial_type','trial_version','maze_id','num_targets','num_barriers','delay','rt','active_target']].describe())
c=tr.groupby(['trial_type','trial_version']).size(); print('conds',len(c)); print(c.value_counts().sort_index())
print('maze ids', tr.maze_id.nunique())
print(tr[['trial_type','trial_version','maze_id']].drop_duplicates().groupby(['trial_type','trial_version']).size().value_counts())
print((tr.delay>400).sum())
print(tr.num_targets.value_counts(), tr.num_barriers.value_counts().sort_index())
nspk=np.array([len(s) for s in u.spike_times]); print('spikes',nspk.min(),nspk.max())
print('sorted', all(np.all(np.diff(s)>=0) for s in u.spike_times))
print('t range', min(s.min() for s in u.spike_times), max(s.max() for s in u.spike_times), tr.stop_time.max())
hp=nwb.processing['behavior']['hand_pos']; ts=hp.timestamps[:]; print('dt', np.unique(np.round(np.diff(ts),5))[:10], ts[0], ts[-1])
print('keywords', nwb.keywords[:])
EOF
python survey2.py 2>&1
```

```
['x', 'y', 'z', 'imp', 'location', 'filtering', 'group', 'group_name']
          x    y    z  imp location filtering           group_name
count   0.0  0.0  0.0  0.0      192       192                  192
unique  NaN  NaN  NaN  NaN        2         1                    2
top     NaN  NaN  NaN  NaN      PMd   1000 Hz  electrode_group_PMd
freq    NaN  NaN  NaN  NaN       96       192                   96
mean    NaN  NaN  NaN  NaN      NaN       NaN                  NaN
std     NaN  NaN  NaN  NaN      NaN       NaN                  NaN
min     NaN  NaN  NaN  NaN      NaN       NaN                  NaN
25%     NaN  NaN  NaN  NaN      NaN       NaN                  NaN
50%     NaN  NaN  NaN  NaN      NaN       NaN                  NaN
75%     NaN  NaN  NaN  NaN      NaN       NaN                  NaN
max     NaN  NaN  NaN  NaN      NaN       NaN                  NaN
     x   y   z  imp location filtering           group_name
id                                                         
1  NaN NaN NaN  NaN      PMd   1000 Hz  electrode_group_PMd
2  NaN NaN NaN  NaN      PMd   1000 Hz  electrode_group_PMd
3  NaN NaN NaN  NaN      PMd   1000 Hz  electrode_group_PMd
4  NaN NaN NaN  NaN      PMd   1000 Hz  electrode_group_PMd
5  NaN NaN NaN  NaN      PMd   1000 Hz  electrode_group_PMd
[... 47 more lines not kept]
```

**Agent**

Dataset: one session (Jenkins, 2009-09-29), 250 trials over 27 maze conditions, 152 units on two Utah arrays (M1/PMd), no electrode coordinates, no EMG. Now reading the paper's methods.

**Agent calls Bash**

```bash
wc -l paper/*.txt; grep -n -i "J-array\|proto-trial\|movement onset\|2155\|2166\|27 conditions\|27-condition" paper/10.1016-j.neuron.2010.09.015.txt | head -60
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; awk '{print NR": "length($0)": "substr($0,1,100)}' 10.1016-j.neuron.2010.09.015.txt | awk -F': ' '$2>0' | head -120
```

```
1: 33: DOI: 10.1016/j.neuron.2010.09.015
2: 30: Version: as served by ncbi_pmc
3: 46: Source: ncbi_pmc+crossref (paper-text-fetcher)
4: 18: Stored: 2026-10-20
5: 182: Extracted: as fetched; with 1 supplement file(s) from PubMed Central, downloaded in a browser (PMC29
6: 72: ------------------------------------------------------------------------
7: 70710: Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain yes pmc-collection-titl
9: 94: Cortical Preparatory Activity: Representation of Movement or First Cog in a Dynamical Machine?
11: 152: [1] Prior information preshapes the population representation of movement direction in motor cortex.
13: 160: [2] Preshaping and continuous evolution of motor cortical representations during movement preparatio
15: 120: [3] Reference frames for reach planning in macaque dorsal premotor cortex. J. Neurophysiol.. 2007. 1
17: 157: [4] Making arm movements within different parts of space: Dynamic aspects in the primate motor corte
19: 122: [5] Delay of movement caused by disruption of cortical preparatory activity. J. Neurophysiol.. 2007.
21: 143: [6] Temporal complexity and heterogeneity of single-neuron activity in premotor and motor cortex. J.
23: 88: [7] A central source of movement variability. Neuron. 2006. 10.1016/j.neuron.2006.10.034
25: 141: [8] Preparatory activity in premotor and motor cortex reflects the speed of the upcoming reach. J. N
27: 135: [9] Neural variability in premotor cortex provides a signature of motor preparation. J. Neurosci.. 2
29: 154: [10] Techniques for extracting single-trial activity patterns from large-scale neural recordings. Cu
31: 120: [11] Stimulus onset quenches neural variability: A widespread cortical phenomenon. Nat. Neurosci.. 2
33: 164: [12] Integrated neural processes for defining potential actions and deciding between them: A computa
[... 100 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 7p paper/10.1016-j.neuron.2010.09.015.txt | fold -s -w 200 > $TMPDIR/main.txt; wc -l $TMPDIR/main.txt; grep -n -i "experimental procedures\|^.*Methods\|Task design\|Neural recordings and datasets\|Correlations between\|Using a PD\|PD performance\|PCA-based\|Task spaces" $TMPDIR/main.txt | head -40
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 222,300p $TMPDIR/main.txt
```

```
will produce movement. Methods Task design and behavior Animal protocols were approved by the Stanford University Institutional Animal Care and Use Committee. Our basic methods have been described 
previously ( Churchland et al., 2006c ). Briefly, monkeys performed delayed reaches on a fronto-parallel screen. Delays ranged from 0-1000 ms (the exact range varied by monkey). To allow sufficient 
preparatory activity, only trials with delays >400 ms were analyzed. Fixation was enforced (at the central spot) during the delay for monkey J only. For single-electrode recordings using the maze 
task, we employed 4 sets of 27 mazes each. Each neuron was recorded for one or more of these, but rarely for all. The monkey J dataset thus consists of four smaller datasets, of ∼53 neurons each. 
Population-level analyses were performed at the level of these smaller datasets and then averaged. For the monkey J-array dataset, all 108 conditions were interleaved in the standard way. Neural 
recordings and datasets Penetrations were guided by stereotaxic critera, the known response properties of M1 and PMd, and the effects of microstimulation. Recordings were medial to the arcuate spur 
and lateral to – or in a few instances within the lateral bank of – the precentral dimple. Few if any recordings were made within rostral PMd, near the arcuate sulcus. Analysis of preparatory 
responses was restricted to neurons with at least 10 spikes/s of preparatory tuning. Electrode arrays were implanted in PMd and surface M1 ( Supp. Fig. 3 ). The resulting dataset involved 
simultaneous recordings and much larger trial counts per neuron (2155). However, isolations were only occasionally of the same high isolation quality as for the single-electrode recordings. Many 
array recordings were of contaminated single-unit isolations or isolations of two or more neurons. Still, some array-based isolations were of high quality, including those in Figure 3E,F . Firing 
rate modulation was typically lower for
[... 68 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 300,360p $TMPDIR/main.txt | head -20; grep -n "Supplemental Experimental Procedures\|Computing the mean\|upper limit\|proto\|Task design" paper/10.1016-j.neuron.2010.09.015.txt | tail -20
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n "Supplemental Experimental Procedures\|Computing the mean\|upper limit\|upper-limit\|proto\|Task design" paper/10.1016-j.neuron.2010.09.015.txt | awk -F: '$1>119' | cut -c1-150
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 600,700p paper/10.1016-j.neuron.2010.09.015.txt; grep -n "Supplemental Figure 1\b\|Population PSTH" paper/10.1016-j.neuron.2010.09.015.txt | head
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
sed -n 195,240p paper/10.1016-j.neuron.2010.09.015.txt; grep -n "Supplemental Figure 3\." -A12 paper/10.1016-j.neuron.2010.09.015.txt | sed -n 14,40p; date -u
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
grep -n -i "anterior\|AP location" $TMPDIR/main.txt | cut -c1-250; sed -n 56,62p $TMPDIR/main.txt; sed -n 144,180p $TMPDIR/main.txt
```

```
160:Comparison of anterior versus posterior sites A number of response properties – including the prevalence of preparatory activity – vary with anterior/posterior location within and between PMd/M1 ( 
161:Kalaska et al., 1997 ; Kalaska et al., 1998 ; Weinrich et al., 1984 ). We similarly found preparatory activity to be more prevalent at anterior sites (data not shown). However, with respect to our 
162:central results, anterior and posterior sites were similar. The poor correlation between preparatory and peri-movement tuning (at the single-cell level) was equally prevalent at anterior and 
163:posterior sites. Regressing tuning correlation (as in Figure 4 ) against AP location yielded little or no effect: r =-0.05, p =0.82; r =-0.03, p =0.85; r =-0.07, p =0.52; and r =0.20, p =0.27 for the 
164:four datasets. The ability of the peri-movement space to capture tuning also held for both anterior and posterior sites ( Figure 7C ). Some caution is required: any division of the data will likely 
166:Figure 6A-D ). Normalized performance was only slightly different than if we down-selected the data randomly. Performance was slightly better at anterior sites, though this may occur simply because 
293:six-dimensional space, normalized, and averaged across datasets. Left-most bar : performance for all data. Gray bars : performance for sites with AP locations >= the median ( anterior ), <= to the 
failure of preparatory tuning to predict peri-movement tuning are quite apparent even for simple center-out reaches ( Figure 2 ). Correlations between preparatory and peri-movement tuning Similar 
levels of preparatory activity can lead to opposing patterns of peri-movement activity (e.g., middlemost traces in Figure 2D and traces near top of Figure 3C ). Thus, it is not simply that tuning 
preferences can reverse; tuning is often weakly correlated between the two epochs (population analysis in Figure 4A-D ). To compute correlations, for each condition we took the average firing r
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
grep -n "0.08\|gray interval\|harmonic" $TMPDIR/main.txt | cut -c1-80; sed -n 180,192p $TMPDIR/main.txt
```

```
1:Neuron 319 nihpa 8809320 Neuron 0896-6273 1097-4199 pmc-is-collection-domain y
185:bear little relationship with peri-movement activity. The correlation of pre
297:Figure 8 Illustration of the behavior of a simple linear dynamical system: a
314:359 17005608 10.1152/jn.00808.2006 Churchland MM Shenoy KV 2007b Temporal co
332:motor cortex, using a two-dimensional reaching task J Neurosci 9 2080 2102 2
This suggestion is compatible with both of our basic findings. The critical observation is that the trajectory of a linear dynamical system is a weighted sum of component patterns. Changes in the 
initial state lead to linear changes in the magnitudes of those component patterns ( Figure 8A ). If one knows how strongly each pattern is present, one can infer the initial state. This will be 
approximately true for a nonlinear system, to the degree that it can be approximated by a time-varying linear system (see Supp. Materials for a derivation and further illustration ). To illustrate 
the above, Figure 8 shows simple simulated dynamics: circular trajectories through state-space. We employed 25 initial states (25 ‘conditions’, Fig. 8B ). These determine the phase and amplitude of 
the subsequent activity. The system was held at its initial state (a rough analogy with preparatory activity) and then released. At the single-unit level ( Figure 8C ) preparatory activity seems to 
bear little relationship with peri-movement activity. The correlation of preparatory activity with peri-movement activity (averaged over the gray interval) was 0.08. Furthermore, a given preparatory 
firing rate could lead to opposing patterns of peri-movement activity ( asterisks , Figure 8C ) much as was the case for the data (e.g., Figure 3C ). This occurs because a given firing rate for unit 
1 can correspond to different initial states ( asterisks , Figure 8B ). Yet hidden in Figure 8C is a straightforward relationship. When the initial rate of unit one is high, the subsequent pattern 
contains
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > survey3.py <<'EOF'
import remfile, h5py, pynwb, numpy as np, pandas as pd
def op(url):
    f=h5py.File(remfile.File(url),'r'); return pynwb.NWBHDF5IO(file=f,load_namespaces=True).read()
tr_=op('https://dandiarchive.s3.amazonaws.com/blobs/8d0/80d/8d080d41-978f-4e60-b929-84fd12165e5f')
te=op('https://dandiarchive.s3.amazonaws.com/blobs/241/5bb/2415bb59-71db-47ab-9168-f85add83e9d9')
u=tr_.units.to_dataframe(); ut=te.units.to_dataframe()
u['grp']=[x.group_name.iloc[0] for x in u.electrodes]; u['el']=[x.index[0] for x in u.electrodes]
ut['grp']=[x.group_name.iloc[0] for x in ut.electrodes]; ut['el']=[x.index[0] for x in ut.electrodes]
print(u.groupby(['grp','heldout']).size()); print(ut.grp.value_counts())
print('train ids', u.index.min(), u.index.max(), 'test ids', ut.index.min(), ut.index.max())
print('test ids subset of train heldin', set(ut.index)<=set(u.index[~u.heldout]))
print('electrodes per unit', set(len(x) for x in u.electrodes))
print('units per electrode', u.el.value_counts().value_counts().sort_index())
tr=tr_.trials.to_dataframe()
# obs intervals
oi=u.obs_intervals.iloc[0]; print('obs intervals n', len(oi), 'same for all', all(np.array_equal(np.asarray(x),np.asarray(oi)) for x in u.obs_intervals))
print('trial gaps', np.unique(np.round(tr.start_time.values[1:]-tr.stop_time.values[:-1],3))[:10])
print('trial dur', (tr.stop_time-tr.start_time).describe())
print('go-target', ((tr.go_cue_time-tr.target_on_time)*1000-tr.delay).describe())
print('move-go', ((tr.move_onset_time-tr.go_cue_time)*1000-tr.rt).describe())
print('move - start', (tr.move_onset_time-tr.start_time).describe(), 'stop - move', (tr.stop_time-tr.move_onset_time).describe())
print(tr[['target_on_time','go_cue_time','move_onset_time']].isna().sum())
# coincident spikes among units on same electrode
st={i:np.asarray(s) for i,s in zip(u.index,u.spike_times)}
for el,g in u.groupby('el'):
    ids=list(g.index)
    for a in range(len(ids)):
        for b in range(a+1,len(ids)):
            x,y=st[ids[a]],st[ids[b]]
            j=np.searchsorted(y,x); j=np.clip(j,1,len(y)-1)
            d=np.minimum(abs(y[j]-x),abs(y[j-1]-x)); fr=(d<0.0002).mean()
            if fr>0.2: print('coinc',el,ids[a],ids[b],round(fr,3),len(x),len(y))
# across all pairs identical counts
allc=[]
ids=list(u.index)
for a in range(len(ids)):
  for b in range(a+1,len(ids)):
    x,y=st[ids[a]],st[ids[b]]
    j=np.searchsorted(y,x); j=np.clip(j,1,len(y)-1)
    d=np.minimum(abs(y[j]-x),abs(y[j-1]-x)); fr=(d<0.0002).mean()
    allc.append(fr)
allc=np.array(allc); print('pair coincidence max', allc.max(), (allc>0.2).sum(), np.percentile(allc,[50,99]))
# test segments duplicates: compare spike count vectors
te_tr=te.trials.to_dataframe()
heldin=[i for i in ut.index]
def counts(sts, t0, t1):
    return np.array([np.sum((s>=t0)&(s<t1)) for s in sts])
tes=[np.asarray(s) for s in ut.spike_times]; trs=[st[i] for i in heldin]
A=np.array([counts(tes,r.move_onset_time-0.25,r.move_onset_time+0.45) for r in te_tr.itertuples()])
B=np.array([counts(trs,r.move_onset_time-0.25,r.move_onset_time+0.45) for r in tr.itertuples()])
D=np.abs(A[:,None,:]-B[None,:,:]).sum(2); print('min L1 test vs train', D.min(), 'median', np.median(D))
EOF
python survey3.py 2>&1
```

```
grp                  heldout
electrode_group_PMd  False      114
                     True        38
dtype: int64
grp
electrode_group_PMd    114
Name: count, dtype: int64
train ids 1011 2951 test ids 1041 2951
test ids subset of train heldin True
electrodes per unit {1}
units per electrode count
1    33
2    33
3    13
4     1
5     2
Name: count, dtype: int64
obs intervals n 250 same for all True
trial gaps [0.014 0.019 0.024 0.029 0.034 0.039 0.044 0.049 0.054 0.059]
trial dur count    250.000000
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import remfile,h5py,numpy as np
f=h5py.File(remfile.File('https://dandiarchive.s3.amazonaws.com/blobs/8d0/80d/8d080d41-978f-4e60-b929-84fd12165e5f'),'r')
g=f['units']; print(list(g.keys())); print(g['electrodes'][:], g['electrodes_index'][:20])
e=f['general/extracellular_ephys/electrodes']; print(list(e.keys())); print(e['id'][:5], e['id'][-5:], e['location'][:3], e['location'][95:98], e['group_name'][95:98])
print(dict(g['electrodes'].attrs))
"
```

```
['electrodes', 'electrodes_index', 'heldout', 'id', 'obs_intervals', 'obs_intervals_index', 'spike_times', 'spike_times_index']
[ 0  2  2  3  3  4  4  5  5  6  7  8  9 10 10 11 12 12 13 15 15 16 16 17
 18 18 19 20 21 21 23 24 24 24 25 26 28 28 32 33 34 35 36 37 38 38 39 40
 42 42 43 46 46 47 49 50 50 53 55 57 59 63 65 66 69 69 70 72 73 75 81 83
 87 89 89 14 15 17 18 19 21 22 22 24 24 26 26 27 29 29 30 31 33 34 34 35
 36 37 38 39 40 41 42 42 42 43 44 45 45 46 47 48 49 51 51 53 53 55 56 57
 57 58 59 61 61 61 62 63 64 65 66 67 67 69 71 72 72 72 73 74 75 75 76 78
 79 80 81 83 83 85 90 94] [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20]
['filtering', 'group', 'group_name', 'id', 'imp', 'location', 'x', 'y', 'z']
[1 2 3 4 5] [188 189 190 191 192] [b'PMd' b'PMd' b'PMd'] [b'PMd' b'M1' b'M1'] [b'electrode_group_PMd' b'electrode_group_M1' b'electrode_group_M1']
{'description': 'the electrodes that each spike unit came from', 'namespace': 'hdmf-common', 'neurodata_type': 'DynamicTableRegion', 'object_id': 'cc5767cf-b30b-4478-8a3e-9dcf86d397af', 'table': <HDF5 object reference>}
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && python -c "
import remfile,h5py,numpy as np
f=h5py.File(remfile.File('https://dandiarchive.s3.amazonaws.com/blobs/8d0/80d/8d080d41-978f-4e60-b929-84fd12165e5f'),'r')
g=f['units']; ids=g['id'][:]; el=g['electrodes'][:]; ho=g['heldout'][:]
print(ids[:80]); print(ids[70:]); a=ids//1000; print(np.unique(a,return_counts=True)); print('el by prefix', [ (k, el[a==k].min(), el[a==k].max()) for k in (1,2)])
print('elec within id', np.all((ids%1000)//10==el+1) , list(zip(ids[:8],el[:8])), list(zip(ids[75:80],el[75:80])))
print('heldout by prefix', [(k,ho[a==k].sum()) for k in (1,2)])
"
```

```
[1011 1031 1032 1041 1042 1051 1052 1061 1062 1071 1081 1092 1101 1111
 1112 1122 1132 1133 1141 1161 1162 1171 1172 1182 1191 1192 1201 1211
 1221 1222 1241 1251 1252 1253 1261 1272 1291 1292 1331 1341 1351 1361
 1371 1381 1391 1392 1401 1411 1431 1432 1441 1471 1472 1481 1501 1511
 1512 1541 1561 1581 1601 1641 1662 1671 1701 1702 1711 1731 1741 1761
 1821 1841 1881 1901 1902 2151 2161 2181 2191 2201]
[1821 1841 1881 1901 1902 2151 2161 2181 2191 2201 2221 2231 2232 2251
 2252 2271 2272 2281 2301 2302 2311 2321 2341 2351 2352 2361 2371 2381
 2391 2402 2412 2421 2431 2432 2433 2442 2451 2461 2462 2471 2481 2492
 2501 2521 2522 2541 2542 2561 2571 2581 2582 2591 2601 2621 2622 2623
 2631 2641 2651 2661 2671 2681 2682 2701 2722 2731 2732 2733 2741 2751
 2761 2762 2771 2791 2801 2811 2821 2841 2842 2861 2911 2951]
(array([1, 2]), array([75, 77]))
el by prefix [(1, np.int64(0), np.int64(89)), (2, np.int64(14), np.int64(94))]
elec within id True [(np.int64(1011), np.int64(0)), (np.int64(1031), np.int64(2)), (np.int64(1032), np.int64(2)), (np.int64(1041), np.int64(3)), (np.int64(1042), np.int64(3)), (np.int64(1051), np.int64(4)), (np.int64(1052), np.int64(4)), (np.int64(1061), np.int64(5))] [(np.int64(2151), np.int64(14)), (np.int64(2161), np.int64(15)), (np.int64(2181), np.int64(17)), (np.int64(2191), np.int64(18)), (np.int64(2201), np.int64(19))]
heldout by prefix [(1, np.int64(25)), (2, np.int64(13))]
Shell cwd was reset to
```

**Agent**

Found a metadata error: unit IDs encode array (1xxx, 2xxx = 75/77 units), but every unit's electrode reference points into the PMd rows, so the M1 units are mislabeled. Writing the helper module now.

**Agent calls Bash**

```bash
date -u; mkdir -p entries/000139-churchland-2010; cd $TMPDIR && . dev/bin/activate && python -c "
import remfile,h5py,numpy as np
f=h5py.File(remfile.File('https://dandiarchive.s3.amazonaws.com/blobs/8d0/80d/8d080d41-978f-4e60-b929-84fd12165e5f'),'r')
b=f['processing/behavior']; print(list(b.keys()))
for k in b: print(k, list(b[k].keys()))
"
```

```
Wed Oct 28 19:52:12 UTC 2026
['cursor_pos', 'eye_pos', 'hand_pos', 'hand_vel']
cursor_pos ['data', 'reference_frame', 'timestamps']
eye_pos ['data', 'reference_frame', 'timestamps']
hand_pos ['data', 'reference_frame', 'timestamps']
hand_vel ['data', 'timestamps']
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/000139-churchland-2010/maze.py",
 "content": "\"\"\"Loading and measures for dandiset 000139 (MC_Maze_Medium), used to test\nChurchland, Cunningham, Kaufman, Ryu & Shenoy (2010), Neuron 68, 387-400.\n\nWhere each parameter comes from:\n\n- Version: the only published version of the dandiset (``VERSION``).\n- Trials kept: delays above 400 ms (claims file, opening comment, from Methods,\n  Task design and behavior). Trials whose horizontal and vertical velocity\n  profiles correlate with a reference proto-trial at r > 0.9 (Supplemental\n  Experimental Procedures, Task design and behavioral control). The\n  proto-trial and how the two profiles are combined are open; the claims file\n  names the readings, implemented in ``proto_keep``. The window over which the\n  profiles are correlated is not given; 150 ms before to 800 ms after movement\n  onset (the maze-task peri-movement window of Methods, PCA-based spaces) is\n  used, an assumption.\n- Movement onset: reading (a) the dataset's ``move_onset_time``; reading (b)\n  the first time after the go cue at which hand speed exceeds 10% of the\n  trial's peak speed (the threshold is a standard choice; the paper does not\n  give one).\n- Rates: spike trains smoothed with a Gaussian of 20 ms standard deviation\n  (Supplemental Experimental Procedures, Computing the mean firing rate),\n  computed on a 1 ms grid; the T-matrices sample them every 10 ms (a standard\n  choice that cannot change an outcome).\n- Preparatory rate: mean from 200 ms before to 100 ms after the go cue;\n  peri-movement rate: mean from 100 ms before to 350 ms after movement onset\n  (Methods, Correlations between preparatory and peri-movement tuning).\n- Tuning strength: readings (a) range across conditions, (b) standard\n  deviation across conditions (claims file, opening comment). Array threshold\n  5 spikes/s of preparatory tuning (Methods, Neural recordings and datasets);\n  peri-movement tuning at least 1.5 times preparatory tuning (Methods,\n  Correlations).\n- PD model and leave-one-condition-out performance: Methods, Using a PD and\n  PD performance. Whether a PCA-based S is recomputed in each fold is open;\n  both readings are implemented (``recompute``).\n- Peri-movement T-matrix: 150 ms before to 800 ms after movement onset, all\n  units except the one being fitted, not normalized (Methods, PCA-based\n  spaces). Kinematic T-matrix: hand position, velocity and acceleration from\n  150 ms before onset, each signal scaled to unit range (same passage).\n- Reach end, used for endpoints and the trajectory-based task spaces: the\n  first time after peak speed at which the condition-mean speed falls below\n  10% of its peak (a standard choice; the paper does not define it).\n\"\"\"\n\nimport numpy as np\nimport pandas as pd\nimport requests\nimport h5py\nimport remfile\nimport pynwb\nfrom scipy.ndimage import gaussian_filter1d\n\nDANDISET = \"000139\"\nVERSION = \"0.220113.0408\"\nTRAIN_PATH = \"sub-Jenkins/sub-Jenkins_ses-medium_desc-train_behavior+ecephys.nwb\"\nTEST_PATH = \"sub-Jenkins/sub-Jenkins_ses-medium_desc-test_ecephys.nwb\"\nAPI = \"https://api.dandiarchive.org/api\"\n\n# Windows in ms, relative to the event (go cue or movement onset).\nGO_WIN = (-600, 500)      # stored go-locked bins\nMOVE_WIN = (-600, 1000)   # stored move-locked bins\nPREP = (-200, 100)        # relative to go cue\nPERI = (-100, 350)        # relative to movement onset\nTMAT = (-150, 800)        # peri-movement T-matrix, maze task\nSIGMA_MS = 20\nSTEP_MS = 10\n\n\ndef list_assets():\n    url = f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/\"\n    out = []\n    while url:\n        r = requests.get(url, timeout=60).json()\n        out += r[\"results\"]\n        url = r[\"next\"]\n    return out\n\n\ndef asset_url(path):\n    a = [x for x in list_assets() if x[\"path\"] == path][0]\n    meta = requests.get(f\"{API}/dandisets/{DANDISET}/versions/{VERSION}/assets/{a['asset_id']}/\",\n                        timeout=60).json()\n    return [u for u in meta[\"contentUrl\"] if \"s3\" in u][0]\n\n\ndef open_nwb(path):\n    f = h5py.File(remfile.File(asset_url(path)), \"r\")\n    io = pynwb.NWBHDF5IO(file=f, load_namespaces=True)\n    return io.read(), f\n\n\ndef load(path=TRAIN_PATH):\n    \"\"\"Trials, units (with the array read from the unit id) and hand kinematics.\"\"\"\n    nwb, f = open_nwb(path)\n    trials = nwb.trials.to_dataframe()\n    g = f[\"units\"]\n    ids = g[\"id\"][:]\n    st_idx = g[\"spike_times_index\"][:]\n    st_all = g[\"spike_times\"][:]\n    spikes = np.split(st_all, st_idx[:-1])\n    el_rows = g[\"electrodes\"][:]\n    eg = f[\"general/extracellular_ephys/electrodes\"]\n    el_group = np.array([x.decode() for x in eg[\"group_name\"][:]])\n    units = pd.DataFrame({\n        \"id\": ids,\n        \"heldout\": g[\"heldout\"][:].astype(bool),\n        \"electrode_row\": el_rows,\n        \"electrode_group_in_file\": el_group[el_rows],\n        # The unit id is array * 1000 + channel * 10 + sort (checked in the notebook).\n        \"id_array\": ids // 1000,\n        \"id_channel\": (ids % 1000) // 10,\n    })\n    out = dict(nwb=nwb, file=f, trials=trials, units=units, spikes=spikes,\n               electrodes=pd.DataFrame({k: eg[k][:] for k in [\"x\", \"y\", \"z\", \"imp\"]} |\n                                       {\"group_name\": el_group}))\n    if \"behavior\" in nwb.processing:\n        b = f[\"processing/behavior\"]\n        out[\"t_beh\"] = b[\"hand_pos/timestamps\"][:]\n        out[\"hand_pos\"] = b[\"hand_pos/data\"][:]   # mm (description), conversion 0.001 to m\n        out[\"hand_vel\"] = b[\"hand_vel/data\"][:]   # mm/s\n    return out\n\n\ndef bin_spikes(spikes, events, win):\n    \"\"\"1 ms spike counts, (trials, units, bins), for windows [win) around events (s).\"\"\"\n    nb = win[1] - win[0]\n    out = np.zeros((len(events), len(spikes), nb), dtype=np.uint8)\n    for u, s in enumerate(spikes):\n        for i, e in enumerate(events):\n            t0 = e + win[0] / 1000.0\n            lo, hi = np.searchsorted(s, [t0, t0 + nb / 1000.0])\n            if hi > lo:\n                b = np.floor((s[lo:hi] - t0) * 1000.0).astype(int)\n                b = b[(b >= 0) & (b < nb)]\n                np.add.at(out[i, u], b, 1)\n    return out\n\n\ndef kin_traces(t, x, events, win):\n    \"\"\"Behaviour samples at 1 ms around events, (trials, bins, 2), nearest sample.\"\"\"\n    nb = win[1] - win[0]\n    rel = np.arange(win[0], win[1]) / 1000.0\n    out = np.empty((len(events), nb, x.shape[1]))\n    for i, e in enumerate(events):\n        idx = np.searchsorted(t, e + rel)\n        idx = np.clip(idx, 1, len(t) - 1)\n        left = np.where(np.abs(t[idx - 1] - (e + rel)) < np.abs(t[idx] - (e + rel)), idx - 1, idx)\n        out[i] = x[left]\n    return out\n\n\ndef onset_from_speed(t, vel, go_times, frac=0.10, search=(0.0, 1.0)):\n    \"\"\"Movement onset reading (b): first time after the go cue at which hand speed\n    exceeds `frac` of the trial's peak speed in the search window (s after go).\"\"\"\n    on = np.empty(len(go_times))\n    for i, g in enumerate(go_times):\n        lo, hi = np.searchsorted(t, [g + search[0], g + search[1]])\n        sp = np.hypot(vel[lo:hi, 0], vel[lo:hi, 1])\n        j = np.argmax(sp > frac * sp.max())\n        on[i] = t[lo + j]\n    return on\n\n\ndef smooth_rate(counts_mean, sigma_ms=SIGMA_MS):\n    \"\"\"Condition-mean 1 ms counts -> rate in spikes/s, smoothed along the last axis.\"\"\"\n    return gaussian_filter1d(counts_mean.astype(float) * 1000.0, sigma_ms, axis=-1, mode=\"nearest\")\n\n\ndef cond_mean(arr, cond_codes, conds):\n    \"\"\"Mean over trials of each condition: arr (trials, ...) -> (conds, ...).\"\"\"\n    return np.stack([arr[cond_codes == c].mean(0) for c in conds])\n\n\ndef window_mean(rate, win, ref):\n    \"\"\"Mean of rate (..., bins) over [win) ms, where bin 0 is at `ref` ms.\"\"\"\n    return rate[..., win[0] - ref: win[1] - ref].mean(-1)\n\n\ndef tuning_strength(x, how):\n    \"\"\"x (conds, units). Reading (a) 'range' or (b) 'sd' across conditions.\"\"\"\n    if how == \"range\":\n        return x.max(0) - x.min(0)\n    return x.std(0, ddof=0)\n\n\ndef proto_keep(vel, cond_codes, proto=\"mean\", combine=\"separate\", r_min=0.9):\n    \"\"\"Proto-trial selection. vel (trials, bins, 2) velocity profiles.\n    proto: 'mean' (condition-mean profile) or 'medoid' (the condition's trial with the\n    highest mean correlation to the others). combine: 'separate' (x and y each r > r_min)\n    or 'concat' (the two profiles concatenated, r > r_min).\"\"\"\n    keep = np.zeros(len(vel), dtype=bool)\n    for c in np.unique(cond_codes):\n        idx = np.where(cond_codes == c)[0]\n        v = vel[idx]\n        if proto == \"mean\":\n            p = v.mean(0)\n        else:\n            cat = v.transpose(0, 2, 1).reshape(len(idx), -1)\n            cc = np.corrcoef(cat)\n            p = v[np.argmax((cc.sum(1) - 1) / max(len(idx) - 1, 1))]\n        for j, i in enumerate(idx):\n            if combine == \"separate\":\n                rx = np.corrcoef(v[j, :, 0], p[:, 0])[0, 1]\n                ry = np.corrcoef(v[j, :, 1], p[:, 1])[0, 1]\n                keep[i] = (rx > r_min) and (ry > r_min)\n            else:\n                r = np.corrcoef(v[j].T.ravel(), p.T.ravel())[0, 1]\n                keep[i] = r > r_min\n    return keep\n\n\n# ---------------------------------------------------------------- PD model\n\ndef _centered_parts(G, train, l):\n    \"\"\"From an uncentered Gram matrix G (c x c), the centered Gram of the training rows\n    and the centered cross products of row l with them (training mean removed).\"\"\"\n    Gtt = G[np.ix_(train, train)]\n    rm = Gtt.mean(1)\n    gm = Gtt.mean()\n    Gc = Gtt - rm[:, None] - rm[None, :] + gm\n    gl = G[l, train]\n    cross = gl - gl.mean() - rm + gm\n    return Gc, cross\n\n\ndef pca_scores(G, kmax):\n    \"\"\"PCA scores of all rows from the uncentered Gram matrix (c x c).\"\"\"\n    c = G.shape[0]\n    H = np.eye(c) - 1.0 / c\n    Gc = H @ G @ H\n    w, U = np.linalg.eigh(Gc)\n    o = np.argsort(w)[::-1][:kmax]\n    w, U = np.clip(w[o], 1e-12, None), U[:, o]\n    return U * np.sqrt(w)\n\n\ndef explained(G):\n    c = G.shape[0]\n    H = np.eye(c) - 1.0 / c\n    w = np.sort(np.linalg.eigvalsh(H @ G @ H))[::-1]\n    w = np.clip(w, 0, None)\n    return w / w.sum()\n\n\ndef _fit_predict(S_train, x_train, s_l):\n    A = np.column_stack([np.ones(len(S_train)), S_train])\n    coef, *_ = np.linalg.lstsq(A, x_train, rcond=None)\n    return coef[0] + s_l @ coef[1:]\n\n\ndef pd_performance_pca(x, G, ks, recompute):\n    \"\"\"Leave-one-condition-out PD performance for one neuron in a PCA-based space.\n    x (c,) preparatory rates; G (c x c) uncentered Gram matrix of the T-matrix (without\n    the neuron). recompute: False = S from all conditions, only the regression leaves the\n    condition out (reading a); True = PCA redone on the remaining conditions and the\n    left-out condition projected onto its components (reading b). Returns perf per k.\"\"\"\n    c = len(x)\n    kmax = max(ks)\n    pred = np.zeros((len(ks), c))\n    if not recompute:\n        S = pca_scores(G, kmax)\n    for l in range(c):\n        train = np.delete(np.arange(c), l)\n        if recompute:\n            Gc, cross = _centered_parts(G, train, l)\n            w, U = np.linalg.eigh(Gc)\n            o = np.argsort(w)[::-1][:kmax]\n            w, U = np.clip(w[o], 1e-12, None), U[:, o]\n            S_train = U * np.sqrt(w)\n            s_l = (cross @ U) / np.sqrt(w)\n        else:\n            S_train, s_l = S[train], S[l]\n        for i, k in enumerate(ks):\n            pred[i, l] = _fit_predict(S_train[:, :k], x[train], s_l[:k])\n    v = x.var()\n    return 1.0 - ((pred - x[None, :]) ** 2).mean(1) / v\n\n\ndef pd_performance_fixed(x, S):\n    \"\"\"Leave-one-condition-out PD performance in a fixed (task) space S (c x k).\"\"\"\n    c = len(x)\n    pred = np.array([_fit_predict(np.delete(S, l, 0), np.delete(x, l), S[l]) for l in range(c)])\n    return 1.0 - ((pred - x) ** 2).mean() / x.var()\n\n\ndef pd_unit(x, S):\n    A = np.column_stack([np.ones(len(S)), S])\n    coef, *_ = np.linalg.lstsq(A, x, rcond=None)\n    b = coef[1:]\n    return b / np.linalg.norm(b)\n\n\ndef pd_consistency(x, S, rng, n_draws=100, n_cond=25):\n    \"\"\"Results, Stability of the PD: 25 conditions drawn with replacement, PD fitted,\n    another 25 drawn, PD refitted; consistency is the dot product of the two unit PDs.\"\"\"\n    c = len(x)\n    d = np.empty(n_draws)\n    for i in range(n_draws):\n        a = rng.integers(0, c, n_cond)\n        b = rng.integers(0, c, n_cond)\n        d[i] = pd_unit(x[a], S[a]) @ pd_unit(x[b], S[b])\n    return d.mean()\n\n\n# ---------------------------------------------------------------- task spaces\n\ndef condition_kinematics(pos, vel, rel0):\n    \"\"\"Per-condition kinematic features from condition-mean traces.\n    pos, vel: (conds, bins, 2), bin 0 at rel0 ms from movement onset.\"\"\"\n    out = []\n    for p, v in zip(pos, vel):\n        sp = np.hypot(v[:, 0], v[:, 1])\n        on = -rel0\n        ipk = on + np.argmax(sp[on:])\n        after = np.where(sp[ipk:] < 0.1 * sp[ipk])[0]\n        iend = ipk + (after[0] if len(after) else len(sp) - 1 - ipk)\n        traj = p[on:iend + 1]\n        start, end = traj[0], traj[-1]\n        d = end - start\n        L = np.linalg.norm(d)\n        rel = traj - start\n        signed = (d[0] * rel[:, 1] - d[1] * rel[:, 0]) / L   # left of the reach is positive\n        imax = np.argmax(np.abs(signed))\n        seg = np.linalg.norm(np.diff(traj, axis=0), axis=1)\n        cum = np.concatenate([[0], np.cumsum(seg)])\n        half = traj[np.searchsorted(cum, cum[-1] / 2)]\n        n = len(traj) - 1\n        pts_t = traj[[0, n // 3, 2 * n // 3, n]]\n        pts_l = traj[[0, np.searchsorted(cum, cum[-1] / 3), np.searchsorted(cum, 2 * cum[-1] / 3), n]]\n        vpk = v[ipk]\n        out.append(dict(\n            end_x=end[0], end_y=end[1], peak_speed=sp[ipk],\n            vx_peak_speed=vpk[0], vy_peak_speed=vpk[1],\n            vx_extreme=v[on:iend + 1, 0][np.argmax(np.abs(v[on:iend + 1, 0]))],\n            vy_extreme=v[on:iend + 1, 1][np.argmax(np.abs(v[on:iend + 1, 1]))],\n            init_vx=v[on:on + 150, 0].mean(), init_vy=v[on:on + 150, 1].mean(),\n            excursion=signed[imax], exc_x=traj[imax, 0], exc_y=traj[imax, 1],\n            half_x=half[0], half_y=half[1],\n            **{f\"segt{i}{a}\": (pts_t[i + 1] - pts_t[i])[j] for i in range(3) for j, a in enumerate(\"xy\")},\n            **{f\"segl{i}{a}\": (pts_l[i + 1] - pts_l[i])[j] for i in range(3) for j, a in enumerate(\"xy\")},\n            reach_end_ms=iend - on,\n        ))\n    return pd.DataFrame(out)\n\n\ndef task_spaces(k, barriers, distractors):\n    \"\"\"The maze-task spaces of Methods, Task spaces. Variants for the open details:\n    segments equal in time (t) or in path length (l); peak velocity read as the velocity\n    at peak speed (pk) or each component's extreme (ex).\"\"\"\n    sp = {}\n    sp[\"endpoints + max speed\"] = k[[\"end_x\", \"end_y\", \"peak_speed\"]].values\n    sp[\"initial velocity\"] = k[[\"init_vx\", \"init_vy\"]].values\n    sp[\"endpoints + orth. excursion\"] = k[[\"end_x\", \"end_y\", \"excursion\"]].values\n    sp[\"endpoints + viapoint\"] = k[[\"end_x\", \"end_y\", \"exc_x\", \"exc_y\"]].values\n    sp[\"endpoints + max velocity (pk)\"] = k[[\"end_x\", \"end_y\", \"vx_peak_speed\", \"vy_peak_speed\"]].values\n    sp[\"endpoints + max velocity (ex)\"] = k[[\"end_x\", \"end_y\", \"vx_extreme\", \"vy_extreme\"]].values\n    sp[\"endpoints + halfpoint\"] = k[[\"end_x\", \"end_y\", \"half_x\", \"half_y\"]].values\n    for s in \"tl\":\n        segs = k[[f\"seg{s}{i}{a}\" for i in range(3) for a in \"xy\"]].values\n        sp[f\"segment dirs ({s})\"] = segs\n        sp[f\"kitchen sink ({s})\"] = np.column_stack(\n            [segs, k[[\"excursion\", \"exc_x\", \"exc_y\"]].values, barriers, distractors])\n    return sp\n"
}
```

```
File created successfully at: entries/000139-churchland-2010/maze.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > dev_load.py <<'EOF'
import sys, time, pickle, numpy as np
sys.path.insert(0,'entries/000139-churchland-2010')
import maze as M
t=time.time()
d=M.load(); print('load',time.time()-t)
tr=d['trials']
t=time.time()
go=M.bin_spikes(d['spikes'], tr.go_cue_time.values, M.GO_WIN)
mv=M.bin_spikes(d['spikes'], tr.move_onset_time.values, M.MOVE_WIN)
print('bin',time.time()-t, go.shape, mv.shape, go.max())
pos=M.kin_traces(d['t_beh'], d['hand_pos'], tr.move_onset_time.values, M.MOVE_WIN)
vel=M.kin_traces(d['t_beh'], d['hand_vel'], tr.move_onset_time.values, M.MOVE_WIN)
on_b=M.onset_from_speed(d['t_beh'], d['hand_vel'], tr.go_cue_time.values)
print('onset b - a ms', np.percentile((on_b-tr.move_onset_time.values)*1000,[5,25,50,75,95]))
pickle.dump(dict(trials=tr, units=d['units'], go=go, mv=mv, pos=pos, vel=vel, on_b=on_b, t_beh=d['t_beh'], hand_pos=d['hand_pos'], hand_vel=d['hand_vel'], spikes=d['spikes']), open('cache.pkl','wb'))
EOF
python dev_load.py
```

```
load 3.1460413932800293
bin 0.8323259353637695 (250, 152, 1100) (250, 152, 1600) 1
onset b - a ms [ 5.  8. 12. 18. 27.]
Shell cwd was reset to
```

**Agent**

Loading takes seconds. Now the core analyses on the cached data.

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && cat > dev_a.py <<'EOF'
import sys, time, pickle, numpy as np, pandas as pd
from scipy import stats
sys.path.insert(0,'entries/000139-churchland-2010')
import maze as M
D=pickle.load(open('cache.pkl','rb'))
tr=D['trials']; cond=(tr.trial_type*10+tr.trial_version).values
conds=np.unique(cond)
ok_delay=tr.delay.values>400
r0=M.MOVE_WIN[0]
vwin=slice(M.TMAT[0]-r0, M.TMAT[1]-r0)
for proto in ['mean','medoid']:
    for comb in ['separate','concat']:
        k=M.proto_keep(D['vel'][:,vwin], cond, proto, comb)
        sel=ok_delay&k
        print(proto,comb,'kept',k.sum(),'with delay',sel.sum(), 'min per cond', pd.Series(cond[sel]).value_counts().min())
sel=ok_delay&M.proto_keep(D['vel'][:,vwin], cond,'mean','separate')
go_r=M.smooth_rate(M.cond_mean(D['go'][sel].astype(np.float32),cond[sel],conds))
mv_r=M.smooth_rate(M.cond_mean(D['mv'][sel].astype(np.float32),cond[sel],conds))
prep=M.window_mean(go_r,M.PREP,M.GO_WIN[0])  # (c,n)
peri=M.window_mean(mv_r,M.PERI,M.MOVE_WIN[0])
for how in ['range','sd']:
    tp=M.tuning_strength(prep,how); tq=M.tuning_strength(peri,how)
    thr=5
    p_ok=tp>thr; both=p_ok&(tq>=1.5*tp)
    r=np.array([np.corrcoef(prep[:,i],peri[:,i])[0,1] for i in np.where(both)[0]])
    rs=np.array([stats.spearmanr(prep[:,i],peri[:,i])[0] for i in np.where(both)[0]])
    print(how,'prep pass',p_ok.sum(),'both',both.sum(),'mean r',r.mean().round(3),'spearman',rs.mean().round(3),
      'p t',stats.ttest_1samp(r,0).pvalue, 'wil', stats.wilcoxon(r).pvalue, 'z', stats.ttest_1samp(np.arctanh(r),0).pvalue)
EOF
python dev_a.py
```

```
/tmp/claude-1001/dev_a.py:27: RuntimeWarning: Mean of empty slice
  print(how,'prep pass',p_ok.sum(),'both',both.sum(),'mean r',r.mean().round(3),'spearman',rs.mean().round(3),
/tmp/claude-1001/dev/lib/python3.13/site-packages/numpy/_core/_methods.py:142: RuntimeWarning: invalid value encountered in scalar divide
  ret = ret.dtype.type(ret / rcount)
/tmp/claude-1001/dev_a.py:28: SmallSampleWarning: One or more sample arguments is too small; all returned values will be NaN. See documentation for sample size requirements.
  'p t',stats.ttest_1samp(r,0).pvalue, 'wil', stats.wilcoxon(r).pvalue, 'z', stats.ttest_1samp(np.arctanh(r),0).pvalue)
/tmp/claude-1001/dev/lib/python3.13/site-packages/scipy/_lib/_util.py:882: SmallSampleWarning: One or more sample arguments is too small; all returned values will be NaN. See documentation for sample size requirements.
  return fun(*args, **kwargs)
mean separate kept 198 with delay 185 min per cond 2
mean concat kept 239 with delay 225 min per cond 6
medoid separate kept 175 with delay 164 min per cond 2
medoid concat kept 233 with delay 218 min per cond 5
range prep pass 85 both 16 mean r 0.163 spearman 0.161 p t 0.051484426592658415 wil 0.083251953125 z 0.052288553660053354
sd prep pass 5 both 0 mean r nan spearman nan p t nan wil nan z nan
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cat >> entries/000139-churchland-2010/maze.py <<'EOF'


# ---------------------------------------------------------------- spaces from the data

def grams_per_unit(rate, rel0, win=TMAT, step=STEP_MS):
    """Per-unit Gram matrices of the peri-movement T-matrix.
    rate (conds, units, bins) smoothed condition means, bin 0 at rel0 ms.
    Returns (units, conds, conds); the T-matrix without unit n has Gram G.sum(0) - G[n]."""
    T = rate[:, :, win[0] - rel0: win[1] - rel0: step]
    return np.einsum("aut,but->uab", T, T)


def kinematic_gram(pos, vel, rel0, n_blocks, end_ms=TMAT[1], start_ms=TMAT[0], replicate=True):
    """Gram matrix of the kinematic T-matrix (Methods, PCA-based spaces).
    pos, vel: condition means (conds, bins, 2), bin 0 at rel0 ms. Acceleration is the time
    derivative of velocity after the 20 ms Gaussian (a standard choice). Each of the six
    signals is scaled to unit range across times and conditions. replicate: reading (a)
    the six signals repeated in turn to `n_blocks` blocks; reading (b) the six once."""
    v_s = gaussian_filter1d(vel, SIGMA_MS, axis=1, mode="nearest")
    acc = np.gradient(v_s, axis=1) * 1000.0
    sl = slice(start_ms - rel0, end_ms - rel0, STEP_MS)
    sigs = [pos[:, sl, 0], pos[:, sl, 1], vel[:, sl, 0], vel[:, sl, 1], acc[:, sl, 0], acc[:, sl, 1]]
    sigs = [s / (s.max() - s.min()) for s in sigs]
    if replicate:
        counts = [n_blocks // 6 + (1 if i < n_blocks % 6 else 0) for i in range(6)]
    else:
        counts = [1] * 6
    return sum(c * (s @ s.T) for c, s in zip(counts, sigs))


def perf_curves_pca(X, G_total, G_units, fit_idx, ks, recompute):
    """PD performance (neurons x ks) for the neurons in fit_idx. X (conds, units) preparatory
    rates. If G_units is None, the space is the same for every neuron (G_total)."""
    out = np.empty((len(fit_idx), len(ks)))
    for j, n in enumerate(fit_idx):
        G = G_total if G_units is None else G_total - G_units[n]
        out[j] = pd_performance_pca(X[:, n], G, ks, recompute)
    return out


def prep_grams(X):
    """Per-unit Gram matrices of the c x n preparatory matrix (upper limit, Supplemental
    Experimental Procedures, Estimating the upper limit of PD performance)."""
    return np.einsum("au,bu->uab", X, X)
EOF
date -u
```

```
Wed Oct 28 19:54:34 UTC 2026
```

**Agent**

Now writing the notebook source as a cell-marked script.

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb_src.py",
 "content": "# %% [markdown]\n# # Churchland et al. (2010) on dandiset 000139 (MC_Maze_Medium)\n#\n# **Paper.** Churchland MM, Cunningham JP, Kaufman MT, Ryu SI, Shenoy KV (2010). Cortical preparatory\n# activity: representation of movement or first cog in a dynamical machine? *Neuron* 68, 387-400.\n# doi:10.1016/j.neuron.2010.09.015.\n#\n# **Dataset.** DANDI:000139, \"MC_Maze_Medium\", version **0.220113.0408**, streamed from the archive.\n# This is the only published version of the dandiset (the other is the draft), so it is pinned; the\n# paper cites no version. The dandiset holds one session of monkey Jenkins (2009-09-29) on the maze\n# task, recorded with two Utah arrays, cut for the Neural Latents Benchmark into 250 training and\n# validation trials (with behaviour and trial labels) and 100 test trials (700 ms segments, no\n# condition labels, held-in units only).\n#\n# **Claims.** `claims/000139/10.1016-j.neuron.2010.09.015.yaml`, written from the NIH author manuscript\n# (PMC2991102) with its supplement, and checked by a second reader. Methods the claims file leaves\n# open are taken from the paper (cited where used) or, where the paper is silent, run under every\n# reading the claims file names.\n#\n# | Claim | Tested here |\n# |---|---|\n# | j-array-recordings | tested |\n# | fig4d-mean-correlation-j-array | tested |\n# | fig4abc-mean-correlation-other-datasets | blocked: data_missing (speed-task and single-electrode data not in the dandiset) |\n# | fig4-broad-unimodal | tested |\n# | fig4e-correlation-time-course | tested |\n# | suppfig1-population-psth-weak-movement-tuning | tested |\n# | fig6d-perimovement-best-j-array | tested |\n# | fig6-perimovement-best-each-dimensionality | tested |\n# | fig6-dimensionality-peak | tested |\n# | fig6-maze-task-spaces | tested |\n# | fig6abc-perimovement-best-other-datasets | blocked: data_missing |\n# | fig6e-summary-rank | blocked: data_missing |\n# | fig6-preparatory-dimensionality | tested |\n# | fig7a-shuffled-space-poor | tested |\n# | fig7b-window-start-slide | tested |\n# | ap-location-no-effect-j-array | tested (AP read as the array) |\n# | ap-location-no-effect-other-datasets | blocked: data_missing |\n# | fig7c-anterior-posterior-performance | tested (AP read as the array) |\n# | prep-activity-more-anterior | tested (AP read as the array) |\n# | fig7d-pd-consistency | tested |\n# | some-neurons-better-elsewhere | tested |\n# | high-dimensional-task-spaces-underperform | tested |\n# | fig8-linear-dynamics-simulation | tested (simulation) |\n\n# %%\nimport itertools\nimport numpy as np\nimport pandas as pd\nimport matplotlib.pyplot as plt\nfrom scipy import stats\nimport diptest\nimport maze as M\n\npd.set_option(\"display.width\", 200)\npd.set_option(\"display.max_columns\", 40)\npd.set_option(\"display.max_rows\", 200)\n\nD = M.load(M.TRAIN_PATH)\nTE = M.load(M.TEST_PATH)\ntr = D[\"trials\"]\nunits = D[\"units\"]\nassets = M.list_assets()\n\n# %% [markdown]\n# ## Data check\n\n# %% tags=[\"sanity\"]\nprint(\"Assets at\", M.VERSION)\nfor a in assets:\n    print(f\"  {a['path']}  {a['size']} bytes\")\nprint(\"Subject:\", D[\"nwb\"].subject.subject_id, D[\"nwb\"].subject.species, \"| session start\", D[\"nwb\"].session_start_time)\nprint(\"Train file: trials\", len(tr), \"| splits\", tr.split.value_counts().to_dict(), \"| success\", tr.success.value_counts().to_dict())\nprint(\"Test file: trials\", len(TE[\"trials\"]), \"columns\", list(TE[\"trials\"].columns), \"| units\", len(TE[\"units\"]))\ncond = (tr.trial_type * 10 + tr.trial_version).values\nconds = np.unique(cond)\nprint(\"Conditions (trial_type x trial_version):\", len(conds), \"| maze_id values:\", tr.maze_id.nunique(),\n      \"| trial_version counts:\", tr.trial_version.value_counts().sort_index().to_dict())\nprint(\"Each condition has one maze_id:\", tr.groupby([\"trial_type\", \"trial_version\"]).maze_id.nunique().max() == 1)\nprint(\"Trials per condition: min\", pd.Series(cond).value_counts().min(), \"max\", pd.Series(cond).value_counts().max())\nprint(\"num_targets by version:\", tr.groupby(\"trial_version\").num_targets.unique().to_dict(),\n      \"| barriers by version:\", tr.groupby(\"trial_version\").num_barriers.apply(lambda x: sorted(x.unique())).to_dict())\nprint(\"Delay (ms): range\", tr.delay.min(), \"to\", tr.delay.max(), \"| trials with delay > 400 ms:\", (tr.delay > 400).sum())\nprint(\"Delay column equals go - target times (ms): max |diff|\",\n      np.abs((tr.go_cue_time - tr.target_on_time) * 1000 - tr.delay).max().round(6))\nprint(\"rt column equals move - go times (ms): max |diff|\",\n      np.abs((tr.move_onset_time - tr.go_cue_time) * 1000 - tr.rt).max().round(6), \"| rt range\", tr.rt.min(), tr.rt.max(),\n      \"| median\", tr.rt.median())\nprint(\"Trial duration (s):\", (tr.stop_time - tr.start_time).min().round(3), \"to\", (tr.stop_time - tr.start_time).max().round(3),\n      \"| movement onset to trial end at least\", (tr.stop_time - tr.move_onset_time).min().round(3), \"s\",\n      \"| trial start to movement onset at least\", (tr.move_onset_time - tr.start_time).min().round(3), \"s\")\nprint()\nprint(\"Units:\", len(units), \"| heldout\", units.heldout.sum(), \"| held-in\", (~units.heldout).sum())\nprint(\"Spike times sorted in every unit:\", all(np.all(np.diff(s) >= 0) for s in D[\"spikes\"]))\nprint(\"Spikes per unit: min\", min(len(s) for s in D[\"spikes\"]), \"max\", max(len(s) for s in D[\"spikes\"]))\nprint(\"Test-file units are the held-in train units:\", set(TE[\"units\"].id) == set(units.id[~units.heldout]))\nel = D[\"electrodes\"]\nprint(\"Electrode table: rows\", len(el), \"| groups\", el.group_name.value_counts().to_dict(),\n      \"| x, y, z all NaN:\", bool(el[[\"x\", \"y\", \"z\"]].isna().all().all()))\nprint(\"Electrode group referenced by units:\", units.electrode_group_in_file.value_counts().to_dict())\nprint(\"Unit id is array*1000 + channel*10 + sort, with channel = electrode row + 1:\",\n      bool(np.all(units.id_channel == units.electrode_row + 1)))\nprint(\"Units by id prefix (array):\", units.id_array.value_counts().sort_index().to_dict(),\n      \"| electrode rows referenced, prefix 1:\", units.electrode_row[units.id_array == 1].min(), \"to\",\n      units.electrode_row[units.id_array == 1].max(), \"; prefix 2:\", units.electrode_row[units.id_array == 2].min(),\n      \"to\", units.electrode_row[units.id_array == 2].max())\n# duplicate recordings: units with coincident spikes\nst = D[\"spikes\"]\ncoinc = []\nfor a, b in itertools.combinations(range(len(st)), 2):\n    x, y = st[a], st[b]\n    j = np.clip(np.searchsorted(y, x), 1, len(y) - 1)\n    coinc.append((np.minimum(np.abs(y[j] - x), np.abs(y[j - 1] - x)) < 2e-4).mean())\ncoinc = np.array(coinc)\nprint(f\"Unit pairs: largest fraction of spikes within 0.2 ms of the other unit's {coinc.max():.3f} (99th percentile {np.percentile(coinc, 99):.4f})\")\n# test segments against train trials\nhin = np.where(~units.heldout.values)[0]\ntest_ids = list(TE[\"units\"].id)\norder = [int(np.where(units.id.values == i)[0][0]) for i in test_ids]\ndef counts(sts, t0, t1):\n    return np.array([np.sum((s >= t0) & (s < t1)) for s in sts])\nA = np.array([counts(TE[\"spikes\"], r.move_onset_time - 0.25, r.move_onset_time + 0.45) for r in TE[\"trials\"].itertuples()])\nB = np.array([counts([st[i] for i in order], r.move_onset_time - 0.25, r.move_onset_time + 0.45) for r in tr.itertuples()])\nL1 = np.abs(A[:, None, :] - B[None, :, :]).sum(2)\nprint(\"Test segments vs train trials (same 700 ms around onset): smallest summed |count difference|\", L1.min(),\n      \"| median\", np.median(L1), \"-> no test segment duplicates a train trial\")\nprint()\ntb = D[\"t_beh\"]\nprint(\"Behaviour samples:\", len(tb), \"| sample interval within trials (ms):\", np.round(np.median(np.diff(tb)) * 1000, 3),\n      \"| hand x range (mm)\", D[\"hand_pos\"][:, 0].min().round(1), \"to\", D[\"hand_pos\"][:, 0].max().round(1),\n      \"| y\", D[\"hand_pos\"][:, 1].min().round(1), \"to\", D[\"hand_pos\"][:, 1].max().round(1))\nsp = np.hypot(D[\"hand_vel\"][:, 0], D[\"hand_vel\"][:, 1])\nprint(\"Hand speed (mm/s): median\", np.median(sp).round(1), \"| 99.9th percentile\", np.percentile(sp, 99.9).round(1))\nvnum = np.gradient(D[\"hand_pos\"][:, 0], tb)\ninside = np.abs(np.diff(tb, prepend=tb[0])) < 0.0015\nprint(\"hand_vel x against the derivative of hand_pos x: r =\", np.corrcoef(vnum[inside], D[\"hand_vel\"][inside, 0])[0, 1].round(3),\n      \"| slope\", np.polyfit(vnum[inside], D[\"hand_vel\"][inside, 0], 1)[0].round(3), \"(1 means hand_vel is in mm/s)\")\n\n# %% [markdown]\n# ### Clocks\n#\n# Spikes, behaviour and the trial table share one clock if a task variable can be decoded from\n# spikes after the event it follows and not before it. The maze condition is decoded (27 classes,\n# nearest class mean, leave one trial out) from spike counts of all units in windows around target\n# onset, with true labels and with labels permuted. Hand speed is shown around the dataset's\n# movement onset.\n\n# %% tags=[\"sanity\"]\ndef decode(X, y):\n    ok = 0\n    for i in range(len(y)):\n        m = np.ones(len(y), bool); m[i] = False\n        cs = np.unique(y[m])\n        cen = np.array([X[m & (y == c)].mean(0) for c in cs])\n        ok += cs[np.argmin(((cen - X[i]) ** 2).sum(1))] == y[i]\n    return ok / len(y)\n\nrng_clk = np.random.default_rng(1)\nrows = []\nfor name, ev in [(\"target\", tr.target_on_time.values), (\"go\", tr.go_cue_time.values)]:\n    for w in [(-300, 0), (50, 350)]:\n        X = np.sqrt(np.array([counts(st, e + w[0] / 1000, e + w[1] / 1000) for e in ev]))\n        acc = decode(X, cond)\n        perm = np.mean([decode(X, rng_clk.permutation(cond)) for _ in range(5)])\n        rows.append(dict(event=name, window_ms=w, accuracy=round(acc, 3), permuted_labels=round(perm, 3)))\nprint(pd.DataFrame(rows).to_string(index=False), \"| chance\", round(1 / len(conds), 3))\nvel_all = M.kin_traces(tb, D[\"hand_vel\"], tr.move_onset_time.values, (-300, 300))\nspd = np.hypot(vel_all[..., 0], vel_all[..., 1])\nprint(\"Mean hand speed around movement onset (mm/s): -300..-100 ms\", spd[:, :200].mean().round(1),\n      \"| -50..0\", spd[:, 250:300].mean().round(1), \"| 0..50\", spd[:, 300:350].mean().round(1),\n      \"| 100..300\", spd[:, 400:].mean().round(1))\non_b = M.onset_from_speed(tb, D[\"hand_vel\"], tr.go_cue_time.values)\ndd = (on_b - tr.move_onset_time.values) * 1000\nprint(\"Onset from hand speed (10% of peak) minus the dataset's move_onset_time (ms): median\", np.median(dd),\n      \"| 5th to 95th percentile\", np.percentile(dd, 5), \"to\", np.percentile(dd, 95))\n\n# %% [markdown]\n# ### Trial selection and condition means\n#\n# Every analysis below starts from condition means under a *reading* of the trial selection: the\n# movement onset (a, the dataset's; b, from hand speed) and the proto-trial rule (Supplemental\n# Experimental Procedures, Task design: \"the subset of trials (typically ~90% of all trials) where\n# the horizontal and vertical velocity profiles correlated with those of a reference 'proto-trial'\n# with r > 0.9\"), proto (a) the condition mean or (b) a representative trial (the medoid), and the\n# profiles compared (a) separately or (b) concatenated. Only trials with delays above 400 ms are\n# kept (Methods, Task design). The main reading is onset (a), proto (a), separate (a); the others\n# are run as variants.\n\n# %%\nRD = {}\ndef condition_data(onset=\"a\", proto=\"mean\", combine=\"separate\"):\n    key = (onset, proto, combine)\n    if key in RD:\n        return RD[key]\n    mo = tr.move_onset_time.values if onset == \"a\" else on_b\n    mv = M.bin_spikes(st, mo, M.MOVE_WIN)\n    go = M.bin_spikes(st, tr.go_cue_time.values, M.GO_WIN)\n    pos = M.kin_traces(tb, D[\"hand_pos\"], mo, M.MOVE_WIN)\n    vel = M.kin_traces(tb, D[\"hand_vel\"], mo, M.MOVE_WIN)\n    r0 = M.MOVE_WIN[0]\n    keep_proto = M.proto_keep(vel[:, M.TMAT[0] - r0: M.TMAT[1] - r0], cond, proto, combine)\n    sel = (tr.delay.values > 400) & keep_proto\n    c = cond[sel]\n    out = dict(sel=sel, keep_proto=keep_proto,\n               go_rate=M.smooth_rate(M.cond_mean(go[sel].astype(np.float32), c, conds)),\n               mv_rate=M.smooth_rate(M.cond_mean(mv[sel].astype(np.float32), c, conds)),\n               pos=M.cond_mean(pos[sel], c, conds), vel=M.cond_mean(vel[sel], c, conds),\n               n_per_cond=pd.Series(c).value_counts().reindex(conds).values)\n    out[\"prep\"] = M.window_mean(out[\"go_rate\"], M.PREP, M.GO_WIN[0])\n    out[\"peri\"] = M.window_mean(out[\"mv_rate\"], M.PERI, M.MOVE_WIN[0])\n    RD[key] = out\n    return out\n\nSEL_READINGS = [(o, p, c) for o in \"ab\" for p in [\"mean\", \"medoid\"] for c in [\"separate\", \"concat\"]]\nrows = []\nfor r in SEL_READINGS:\n    d = condition_data(*r)\n    rows.append(dict(onset=r[0], proto=r[1], combine=r[2], proto_pass=int(d[\"keep_proto\"].sum()),\n                     proto_pass_pct=round(100 * d[\"keep_proto\"].mean(), 1), kept=int(d[\"sel\"].sum()),\n                     min_per_cond=int(d[\"n_per_cond\"].min()), max_per_cond=int(d[\"n_per_cond\"].max())))\nsel_table = pd.DataFrame(rows)\nprint(sel_table.to_string(index=False))\nMAIN = (\"a\", \"mean\", \"separate\")\nd0 = condition_data(*MAIN)\nprint(\"Preparatory rates (spikes/s): range\", d0[\"prep\"].min().round(2), \"to\", d0[\"prep\"].max().round(2),\n      \"| peri-movement\", d0[\"peri\"].min().round(2), \"to\", d0[\"peri\"].max().round(2))\n\n# %% [markdown]\n# ### Neurons\n#\n# Preparatory tuning above 5 spikes/s (array threshold, Methods, Neural recordings and datasets),\n# and for the correlations also peri-movement tuning at least 1.5 times as strong (Methods,\n# Correlations). Tuning strength: reading (a) range across conditions, (b) standard deviation.\n\n# %%\ndef neuron_sets(d, how):\n    tp = M.tuning_strength(d[\"prep\"], how)\n    tq = M.tuning_strength(d[\"peri\"], how)\n    prep_ok = tp > 5\n    both = prep_ok & (tq >= 1.5 * tp)\n    return prep_ok, both\n\nrows = []\nfor r in SEL_READINGS:\n    for how in [\"range\", \"sd\"]:\n        p, b = neuron_sets(condition_data(*r), how)\n        rows.append(dict(onset=r[0], proto=r[1], combine=r[2], tuning=how, prep_pass=int(p.sum()), both_pass=int(b.sum())))\nneuron_table = pd.DataFrame(rows)\nprint(neuron_table.to_string(index=False))\ntp0 = M.tuning_strength(d0[\"prep\"], \"range\")\nprint(\"Main reading, preparatory tuning range (spikes/s): median\", np.median(tp0).round(2), \"| max\", tp0.max().round(2))\nprint(\"Main reading, preparatory tuning SD (spikes/s): median\", np.median(M.tuning_strength(d0[\"prep\"], \"sd\")).round(2),\n      \"| max\", M.tuning_strength(d0[\"prep\"], \"sd\").max().round(2))\n\n# %% [markdown]\n# ## j-array-recordings\n#\n# > The J-array dataset holds 146 single- and multi-unit isolations recorded with two 96-electrode\n# > arrays during the maze task, over 108 conditions, with a mean of 2166 trials per neuron.\n\n# %% tags=[\"claim:j-array-recordings\"]\nn_units = len(units)\nprint(\"Units:\", n_units, \"(expected 146 +/- 14.6) -> within tolerance:\", abs(n_units - 146) <= 14.6)\nprint(\"Units per array (id prefix): 1 ->\", (units.id_array == 1).sum(), \"| 2 ->\", (units.id_array == 2).sum(),\n      \"| electrodes per array in the table:\", el.group_name.value_counts().to_dict())\nprint(\"Conditions:\", len(conds), \"(expected 108) | mazes\", tr.maze_id.nunique(), \"x versions\", tr.trial_version.nunique())\nprint(\"maze_id values:\", sorted(tr.maze_id.unique()))\nprint(\"Trials per neuron: train+val file\", len(tr), \"; with the 100 test segments\", len(tr) + len(TE[\"trials\"]),\n      \"(paper: 2166 in the Results, 2155 in the Methods; reported only)\")\n\n# %% [markdown]\n# **Result: partially reproduced.** The dandiset holds 152 units (within 146 +/- 14.6) from two\n# arrays, but 27 conditions (9 mazes in 3 versions), not 108, and 250 labelled trials per unit. That\n# the 9 mazes are among the paper's 108 conditions is consistent with the data (same monkey, task\n# and 3-version design) but cannot be shown from the files. The claims file's partial outcome\n# applies.\n\n# %% [markdown]\n# ## fig4d-mean-correlation-j-array\n#\n# > For the J-array dataset, preparatory and peri-movement tuning are positively but only weakly\n# > correlated on average across neurons (mean r = 0.13, p = 0.03; mean Spearman r = 0.11).\n#\n# Every reading: trial selection (8), tuning measure (2), test of the mean (3).\n\n# %% tags=[\"claim:fig4d-mean-correlation-j-array\"]\ndef corr_set(d, mask):\n    idx = np.where(mask)[0]\n    r = np.array([np.corrcoef(d[\"prep\"][:, i], d[\"peri\"][:, i])[0, 1] for i in idx])\n    rs = np.array([stats.spearmanr(d[\"prep\"][:, i], d[\"peri\"][:, i])[0] for i in idx])\n    return idx, r, rs\n\ndef mean_tests(r):\n    if len(r) < 3:\n        return dict(p_t=np.nan, p_wilcoxon=np.nan, p_fisher_t=np.nan)\n    return dict(p_t=stats.ttest_1samp(r, 0).pvalue, p_wilcoxon=stats.wilcoxon(r).pvalue,\n                p_fisher_t=stats.ttest_1samp(np.arctanh(np.clip(r, -0.999999, 0.999999)), 0).pvalue)\n\nrows = []\nfor r_ in SEL_READINGS:\n    for how in [\"range\", \"sd\"]:\n        d = condition_data(*r_)\n        _, both = neuron_sets(d, how)\n        idx, r, rs = corr_set(d, both)\n        t = mean_tests(r)\n        row = dict(onset=r_[0], proto=r_[1], combine=r_[2], tuning=how, n=len(r),\n                   mean_r=np.round(r.mean(), 3) if len(r) else np.nan,\n                   mean_spearman=np.round(rs.mean(), 3) if len(rs) else np.nan,\n                   **{k: np.round(v, 4) for k, v in t.items()})\n        pmin = np.nanmin(list(t.values())) if len(r) >= 3 else np.nan\n        row[\"within_tol_both\"] = bool(len(r) and abs(row[\"mean_r\"] - 0.13) <= 0.013 and abs(row[\"mean_spearman\"] - 0.11) <= 0.011)\n        row[\"any_test_p<0.05\"] = bool(pmin < 0.05) if len(r) >= 3 else False\n        row[\"in_0.054_0.231\"] = bool(len(r) and 0.054 <= row[\"mean_r\"] <= 0.231)\n        rows.append(row)\nfig4d = pd.DataFrame(rows)\nprint(fig4d.to_string(index=False))\nprint()\nprint(\"Readings with both means in tolerance and p < 0.05:\", int((fig4d.within_tol_both & fig4d[\"any_test_p<0.05\"]).sum()))\nprint(\"Readings with mean r in 0.054..0.231 and p < 0.05:\", int((fig4d[\"in_0.054_0.231\"] & fig4d[\"any_test_p<0.05\"]).sum()),\n      \"of\", int((fig4d.n >= 3).sum()), \"readings with at least 3 neurons\")\nmain_idx, main_r, main_rs = corr_set(d0, neuron_sets(d0, \"range\")[1])\nprint(\"Main reading (onset a, proto mean, separate, range): n =\", len(main_r), \"| mean r\", main_r.mean().round(3),\n      \"| SD\", main_r.std(ddof=1).round(3), \"| mean Spearman\", main_rs.mean().round(3))\nprint(\"Per-array breakdown (main reading):\", {a: (int((units.id_array.values[main_idx] == a).sum()),\n      np.round(main_r[units.id_array.values[main_idx] == a].mean(), 3)) for a in (1, 2)})\n# threshold dependence (main selection, range measure)\nrows = []\ntpm = M.tuning_strength(d0[\"prep\"], \"range\"); tqm = M.tuning_strength(d0[\"peri\"], \"range\")\nfor thr in [3, 4, 5, 6, 8, 10]:\n    for ratio in [1.0, 1.5, 2.0]:\n        m = (tpm > thr) & (tqm >= ratio * tpm)\n        _, r, rs = corr_set(d0, m)\n        rows.append(dict(prep_thr=thr, peri_ratio=ratio, n=len(r), mean_r=np.round(r.mean(), 3) if len(r) else np.nan,\n                         mean_spearman=np.round(rs.mean(), 3) if len(r) else np.nan,\n                         p_t=np.round(stats.ttest_1samp(r, 0).pvalue, 4) if len(r) > 2 else np.nan))\nprint(\"Threshold dependence (main reading, range):\")\nprint(pd.DataFrame(rows).to_string(index=False))\n\n# %% [markdown]\n# **Result: ...** (filled after the full run)\n\n# %% [markdown]\n# ## fig4-broad-unimodal\n#\n# > Individual neurons span a broad range of preparatory to peri-movement correlations centred near\n# > zero, with little sign of separate populations of concordant (r near 1) and opposing (r near -1)\n# > tuning, except perhaps weakly for monkey B (Figure 4B).\n\n# %% tags=[\"claim:fig4-broad-unimodal\"]\nrows = []\nfor r_ in SEL_READINGS:\n    d = condition_data(*r_)\n    _, r, _ = corr_set(d, neuron_sets(d, \"range\")[1])\n    if len(r) < 4:\n        continue\n    dip, p_dip = diptest.diptest(r)\n    rows.append(dict(onset=r_[0], proto=r_[1], combine=r_[2], n=len(r), min_r=r.min().round(3), max_r=r.max().round(3),\n                     mean_r=r.mean().round(3), sd_r=r.std(ddof=1).round(3), dip=round(dip, 4), p_dip=round(p_dip, 3),\n                     n_abs_gt_0_8=int((np.abs(r) > 0.8).sum()), n_abs_lt_0_5=int((np.abs(r) < 0.5).sum())))\nf4u = pd.DataFrame(rows)\nprint(f4u.to_string(index=False))\nprint(\"SD-based tuning leaves too few neurons in every selection reading (see the neuron table).\")\nfig, ax = plt.subplots(figsize=(4, 3))\nax.hist(main_r, bins=np.linspace(-1, 1, 21), color=\"0.5\")\nax.axvline(main_r.mean(), color=\"r\")\nax.set_xlabel(\"preparatory vs peri-movement r\"); ax.set_ylabel(\"neurons\"); ax.set_title(\"main reading\")\nplt.show()\nprint(\"Histogram range: all\", len(main_r), \"values inside -1..1\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig4e-correlation-time-course\n#\n# > The correlation between preparatory tuning and peri-movement activity at a single time point\n# > begins to decline about 200 ms before movement onset and is near zero by movement onset.\n\n# %% tags=[\"claim:fig4e-correlation-time-course\"]\ndef corr_trace(prep, rate):\n    \"\"\"prep (c, n), rate (c, n, T) -> per-neuron correlation at each time (n, T).\"\"\"\n    a = prep - prep.mean(0)\n    b = rate - rate.mean(0)\n    num = (a[:, :, None] * b).sum(0)\n    den = np.sqrt((a ** 2).sum(0))[:, None] * np.sqrt((b ** 2).sum(0))\n    return num / den\n\nrt_med = int(np.median(tr.rt[d0[\"sel\"]]))\ndef fig4e_traces(d, mask):\n    idx = np.where(mask)[0]\n    r0 = M.MOVE_WIN[0]\n    mv_t = np.arange(-400, 101)\n    mv_c = corr_trace(d[\"prep\"][:, idx], d[\"mv_rate\"][:, idx, mv_t[0] - r0: mv_t[-1] + 1 - r0])\n    g0 = M.GO_WIN[0]\n    go_t = np.arange(-200, 101)\n    go_c = corr_trace(d[\"prep\"][:, idx], d[\"go_rate\"][:, idx, go_t[0] - g0: go_t[-1] + 1 - g0])\n    # reading (a): go-locked part mapped to movement time with the median RT, then movement-locked\n    go_tm = go_t - rt_med\n    keep_mv = mv_t > go_tm[-1]\n    sp_t = np.concatenate([go_tm, mv_t[keep_mv]])\n    sp_c = np.concatenate([go_c, mv_c[:, keep_mv]], axis=1)\n    return dict(b=(mv_t, mv_c), a=(sp_t, sp_c))\n\ndef judge_4e(t, c):\n    m = np.nanmean(c, 0)\n    def at(x):\n        return m[np.argmin(np.abs(t - x))]\n    v400 = at(-400)\n    pre = (t <= 0) & (t >= -400)\n    within = pre & (np.abs(m - v400) <= 0.1 * abs(v400))\n    decline = t[within].max() if within.any() else np.nan\n    on = c[:, np.argmin(np.abs(t))]\n    on = on[np.isfinite(on)]\n    t_ = mean_tests(on)\n    return dict(at_m400=round(v400, 3), at_m200=round(at(-200), 3), at_0=round(at(0), 3),\n                decline_ms=decline, p_t=round(t_[\"p_t\"], 4), p_wil=round(t_[\"p_wilcoxon\"], 4),\n                p_fisher=round(t_[\"p_fisher_t\"], 4), n=len(on))\n\nrows = []\nfor r_ in SEL_READINGS:\n    d = condition_data(*r_)\n    prep_ok, both = neuron_sets(d, \"range\")\n    for nset, mask in [(\"a both thresholds\", both), (\"b preparatory only\", prep_ok)]:\n        tr_ = fig4e_traces(d, mask)\n        for rng_name in [\"a\", \"b\"]:\n            t, c = tr_[rng_name]\n            rows.append(dict(onset=r_[0], proto=r_[1], combine=r_[2], neurons=nset, time_range=rng_name, **judge_4e(t, c)))\nf4e = pd.DataFrame(rows)\nf4e[\"drop_200_to_0\"] = f4e.at_m200 > f4e.at_0\nf4e[\"near_zero_a\"] = ~((f4e.at_0 > 0) & (f4e[[\"p_t\", \"p_wil\", \"p_fisher\"]].min(1) < 0.05))\nf4e[\"near_zero_b\"] = f4e.at_0.abs() < 0.1\nf4e[\"decline_in_-300_-100\"] = f4e.decline_ms.between(-300, -100)\nprint(f4e.to_string(index=False))\nok4e = f4e.drop_200_to_0 & (f4e.near_zero_a | f4e.near_zero_b) & f4e[\"decline_in_-300_-100\"]\nprint(\"Readings meeting the criterion:\", int(ok4e.sum()), \"of\", len(f4e))\nprint(\"Median RT used for the splice (ms):\", rt_med)\ntr_main = fig4e_traces(d0, neuron_sets(d0, \"range\")[1])\nfig, ax = plt.subplots(1, 2, figsize=(9, 3))\nfor a_, (nm, (t, c)) in zip(ax, tr_main.items()):\n    a_.plot(t, np.nanmean(c, 0), \"k\"); a_.axhline(0, color=\"0.7\"); a_.axvline(0, color=\"0.7\")\n    a_.set_title(f\"time range ({nm})\"); a_.set_xlabel(\"ms from movement onset\"); a_.set_ylabel(\"mean r\")\nplt.show()\nprint(\"Plotted mean r range:\", round(min(np.nanmean(c, 0).min() for t, c in tr_main.values()), 3), \"to\",\n      round(max(np.nanmean(c, 0).max() for t, c in tr_main.values()), 3))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## suppfig1-population-psth-weak-movement-tuning\n#\n# > In population averages sorted by each neuron's preparatory preference, the preparatory\n# > differences carry weakly into the peri-movement epoch and show little relationship with\n# > preparatory tuning by movement onset.\n\n# %% tags=[\"claim:suppfig1-population-psth-weak-movement-tuning\"]\ndef supp1(d, mask):\n    idx = np.where(mask)[0]\n    nc = len(conds)\n    ranks = [nc - 1, 2 * (nc - 1) // 3, (nc - 1) // 3, 0]  # strongest, two intermediate, weakest\n    go_tr, mv_tr = [], []\n    for n in idx:\n        o = np.argsort(d[\"prep\"][:, n])\n        mx = max(d[\"go_rate\"][:, n].max(), d[\"mv_rate\"][:, n].max())\n        go_tr.append(d[\"go_rate\"][o[ranks], n] / mx)\n        mv_tr.append(d[\"mv_rate\"][o[ranks], n] / mx)\n    go_tr = np.mean(go_tr, 0); mv_tr = np.mean(mv_tr, 0)\n    g0, m0 = M.GO_WIN[0], M.MOVE_WIN[0]\n    prep_diff = (go_tr[0, M.PREP[0] - g0: M.PREP[1] - g0] - go_tr[3, M.PREP[0] - g0: M.PREP[1] - g0]).mean()\n    onset_diff = mv_tr[0, -m0] - mv_tr[3, -m0]\n    return go_tr, mv_tr, prep_diff, onset_diff\n\nrows = []\nfor r_ in SEL_READINGS:\n    d = condition_data(*r_)\n    for nset, mask in zip([\"both thresholds\", \"preparatory only (variant)\"], neuron_sets(d, \"range\")[::-1]):\n        _, _, pdf, odf = supp1(d, mask)\n        rows.append(dict(onset=r_[0], proto=r_[1], combine=r_[2], neurons=nset, n=int(mask.sum()), prep_diff=round(pdf, 3),\n                         onset_diff=round(odf, 3), ratio=round(odf / pdf, 3)))\ns1 = pd.DataFrame(rows)\ns1[\"a_smaller\"] = s1.onset_diff < s1.prep_diff\ns1[\"b_less_than_half\"] = s1.ratio < 0.5\nprint(s1.to_string(index=False))\ngo_tr, mv_tr, _, _ = supp1(d0, neuron_sets(d0, \"range\")[1])\nfig, ax = plt.subplots(1, 2, figsize=(9, 3), sharey=True)\ncols = [\"r\", \"salmon\", \"yellowgreen\", \"g\"]\nfor i in range(4):\n    ax[0].plot(np.arange(*M.GO_WIN), go_tr[i], color=cols[i]); ax[1].plot(np.arange(*M.MOVE_WIN), mv_tr[i], color=cols[i])\nax[0].set_xlabel(\"ms from go cue\"); ax[1].set_xlabel(\"ms from movement onset\"); ax[0].set_ylabel(\"normalized rate\")\nplt.show()\nprint(\"Plotted normalized rate range:\", round(min(go_tr.min(), mv_tr.min()), 3), \"to\", round(max(go_tr.max(), mv_tr.max()), 3))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## PD performance in each space (Figure 6)\n#\n# The PD model, leave-one-condition-out performance, the peri-movement, kinematic and task spaces\n# and the upper limit, as in the claims file's opening comment and `maze.py`. Neurons fitted: all\n# with preparatory tuning above 5 spikes/s (range), regardless of peri-movement activity (Methods,\n# Correlations, last sentence). The peri-movement and upper-limit T-matrices use every unit but the\n# one fitted. Readings run: S fixed (a) or recomputed in each fold (b); kinematic window end (a) 800\n# ms or (b) the end of the slowest condition's reach; kinematic signals (a) repeated to one block\n# per unit or (b) once; and, for the task spaces, segments equal in time or path length and peak\n# velocity read two ways (each listed as its own space).\n\n# %%\nKS = list(range(1, 15))\n\ndef fig6_all(d, how=\"range\"):\n    prep_ok, _ = neuron_sets(d, how)\n    fit = np.where(prep_ok)[0]\n    X = d[\"prep\"]\n    Gu = M.grams_per_unit(d[\"mv_rate\"], M.MOVE_WIN[0])\n    Gt = Gu.sum(0)\n    Gp = M.prep_grams(X)\n    kin = M.condition_kinematics(d[\"pos\"], d[\"vel\"], M.MOVE_WIN[0])\n    v = tr[d[\"sel\"]].groupby(cond[d[\"sel\"]]).trial_version.first().reindex(conds).values\n    spaces = M.task_spaces(kin, (v > 0).astype(float), (v == 2).astype(float))\n    res = dict(fit=fit, kin=kin, spaces=spaces, curves={}, task={})\n    for rec in [False, True]:\n        R = \"b\" if rec else \"a\"\n        res[\"curves\"][(\"peri\", R)] = M.perf_curves_pca(X, Gt, Gu, fit, KS, rec)\n        res[\"curves\"][(\"upper\", R)] = M.perf_curves_pca(X, Gp.sum(0), Gp, fit, KS, rec)\n        res[\"curves\"][(\"upper incl. neuron\", R)] = M.perf_curves_pca(X, Gp.sum(0), None, fit, KS, rec)\n        for kw in [\"a\", \"b\"]:\n            end = M.TMAT[1] if kw == \"a\" else int(kin.reach_end_ms.max())\n            for rep in [\"a\", \"b\"]:\n                Gk = M.kinematic_gram(d[\"pos\"], d[\"vel\"], M.MOVE_WIN[0], len(units) - 1, end_ms=end, replicate=(rep == \"a\"))\n                res[\"curves\"][(f\"kinematic win {kw} rep {rep}\", R)] = M.perf_curves_pca(X, Gk, None, fit, KS, rec)\n    for nm, S in spaces.items():\n        res[\"task\"][nm] = np.array([M.pd_performance_fixed(X[:, n], S) for n in fit])\n    return res\n\nF6 = fig6_all(d0)\nprint(\"Neurons fitted:\", len(F6[\"fit\"]), \"| by array:\", pd.Series(units.id_array.values[F6[\"fit\"]]).value_counts().sort_index().to_dict())\nprint(\"Reach end (ms after onset) over conditions:\", F6[\"kin\"].reach_end_ms.min(), \"to\", F6[\"kin\"].reach_end_ms.max())\ncurve_tab = pd.DataFrame({f\"{k[0]} | S {k[1]}\": v.mean(0) for k, v in F6[\"curves\"].items()}, index=KS).T.round(3)\nprint(\"Mean performance over neurons, by k:\")\nprint(curve_tab.to_string())\ntask_tab = pd.Series({k: v.mean() for k, v in F6[\"task\"].items()}).round(3)\ndims = {k: v.shape[1] for k, v in F6[\"spaces\"].items()}\nprint()\nprint(pd.DataFrame({\"dim\": dims, \"mean_perf\": task_tab}).to_string())\n\n# %% [markdown]\n# ## fig6d-perimovement-best-j-array\n#\n# > For the J-array dataset, the highest cross-validated PD performance over all tested spaces and\n# > dimensionalities is reached when the PD is expressed in the peri-movement space.\n\n# %% tags=[\"claim:fig6d-perimovement-best-j-array\"]\ndef fig6d_judge(F):\n    rows = []\n    best_task = max(v.mean() for v in F[\"task\"].values())\n    best_task_name = max(F[\"task\"], key=lambda k: F[\"task\"][k].mean())\n    for R in \"ab\":\n        peri = F[\"curves\"][(\"peri\", R)].mean(0)\n        for kw in \"ab\":\n            for rep in \"ab\":\n                kin = F[\"curves\"][(f\"kinematic win {kw} rep {rep}\", R)].mean(0)\n                rows.append(dict(S=R, kin_window=kw, kin_rep=rep, peri_best=peri.max().round(3), peri_best_k=KS[peri.argmax()],\n                                 kin_best=kin.max().round(3), kin_best_k=KS[kin.argmax()], task_best=round(best_task, 3),\n                                 task_best_space=best_task_name, upper_best=F[\"curves\"][(\"upper\", R)].mean(0).max().round(3),\n                                 peri_highest=bool(peri.max() > max(kin.max(), best_task))))\n    return pd.DataFrame(rows)\n\nf6d = fig6d_judge(F6)\nprint(f6d.to_string(index=False))\nfig, ax = plt.subplots(1, 2, figsize=(10, 3.5), sharey=True)\nfor a_, R in zip(ax, \"ab\"):\n    for nm, colr in [(\"peri\", \"k\"), (\"upper\", \"0.6\"), (\"kinematic win a rep a\", \"b\")]:\n        a_.plot(KS, F6[\"curves\"][(nm, R)].mean(0), color=colr, label=nm)\n    for nm, v in F6[\"task\"].items():\n        a_.plot(dims[nm], v.mean(), \"g.\", ms=8)\n    a_.axhline(0, color=\"0.8\"); a_.set_title(f\"S reading {R}\"); a_.set_xlabel(\"dimensionality\")\nax[0].set_ylabel(\"mean performance\"); ax[0].legend(fontsize=7)\nax[0].set_ylim(-0.5, 1)\nplt.show()\nallv = np.concatenate([np.concatenate([v.mean(0) for v in F6[\"curves\"].values()]), task_tab.values])\nprint(\"Points below the axis floor (-0.5):\", int((allv < -0.5).sum()), \"of\", len(allv), \"| min\", allv.min().round(3))\n\n# %% [markdown]\n# Robustness over the trial-selection readings (main tuning measure). The SD measure leaves too few\n# neurons to fit.\n\n# %% tags=[\"claim:fig6d-perimovement-best-j-array\"]\nF6_all = {MAIN: F6}\nrows = []\nfor r_ in SEL_READINGS:\n    if r_ not in F6_all:\n        F6_all[r_] = fig6_all(condition_data(*r_))\n    t = fig6d_judge(F6_all[r_])\n    rows.append(dict(onset=r_[0], proto=r_[1], combine=r_[2], neurons=len(F6_all[r_][\"fit\"]),\n                     peri_best_min=t.peri_best.min(), kin_best_max=t.kin_best.max(), task_best=t.task_best.iloc[0],\n                     peri_highest_all=bool(t.peri_highest.all()), peri_highest_any=bool(t.peri_highest.any())))\nf6d_sel = pd.DataFrame(rows)\nprint(f6d_sel.to_string(index=False))\nby_arr = {a: F6[\"curves\"][(\"peri\", \"a\")][units.id_array.values[F6[\"fit\"]] == a].mean(0).max().round(3) for a in (1, 2)}\nprint(\"Best peri-movement performance (S a) among neurons of array 1 and 2:\", by_arr)\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig6-perimovement-best-each-dimensionality\n#\n# > Even taken one dimensionality at a time, PD performance is almost always higher in the\n# > peri-movement space than in other spaces of the same dimensionality.\n\n# %% tags=[\"claim:fig6-perimovement-best-each-dimensionality\"]\nTASK_SETS = {\"pk, t\": [\"endpoints + max speed\", \"initial velocity\", \"endpoints + orth. excursion\", \"endpoints + viapoint\",\n                       \"endpoints + max velocity (pk)\", \"endpoints + halfpoint\", \"segment dirs (t)\", \"kitchen sink (t)\"],\n             \"ex, l\": [\"endpoints + max speed\", \"initial velocity\", \"endpoints + orth. excursion\", \"endpoints + viapoint\",\n                       \"endpoints + max velocity (ex)\", \"endpoints + halfpoint\", \"segment dirs (l)\", \"kitchen sink (l)\"]}\nrows = []\nfor R in \"ab\":\n    peri = F6[\"curves\"][(\"peri\", R)].mean(0)\n    for kw in \"ab\":\n        for rep in \"ab\":\n            kin = F6[\"curves\"][(f\"kinematic win {kw} rep {rep}\", R)].mean(0)\n            for ts, names in TASK_SETS.items():\n                wins = [peri[i] > kin[i] for i in range(len(KS))]\n                wins += [peri[dims[nm] - 1] > F6[\"task\"][nm].mean() for nm in names]\n                rows.append(dict(S=R, kin_window=kw, kin_rep=rep, task_variant=ts, comparisons=len(wins),\n                                 peri_wins=int(sum(wins)), fraction=round(np.mean(wins), 3)))\nf6e = pd.DataFrame(rows)\nprint(f6e.to_string(index=False))\nprint(\"Fraction range over readings:\", f6e.fraction.min(), \"to\", f6e.fraction.max())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig6-dimensionality-peak\n#\n# > Performance of the PCA-based spaces typically improves with dimensionality, peaks usually at a\n# > middle range, and declines at dimensionalities above 10, a sign of over-fitting.\n\n# %% tags=[\"claim:fig6-dimensionality-peak\"]\nrows = []\nfor (nm, R), v in F6[\"curves\"].items():\n    if nm.startswith(\"upper incl\"):\n        continue\n    m = v.mean(0)\n    kb = KS[m.argmax()]\n    rows.append(dict(space=nm, S=R, k1=m[0].round(3), best=m.max().round(3), best_k=kb, k14=m[-1].round(3),\n                     above_k1=bool(m.max() > m[0]), best_k_2_10=bool(2 <= kb <= 10), k14_below_best=bool(m[-1] < m.max())))\nf6p = pd.DataFrame(rows)\nf6p[\"all_three\"] = f6p.above_k1 & f6p.best_k_2_10 & f6p.k14_below_best\nprint(f6p.to_string(index=False))\nfor r_ in SEL_READINGS:\n    m = F6_all[r_][\"curves\"][(\"peri\", \"a\")].mean(0); mb = F6_all[r_][\"curves\"][(\"peri\", \"b\")].mean(0)\n    print(r_, \"peri best k (S a):\", KS[m.argmax()], \"k14 below best:\", m[-1] < m.max(), \"| (S b):\", KS[mb.argmax()], mb[-1] < mb.max())\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig6-maze-task-spaces\n#\n# > Segment directions and initial velocity are among the task spaces that perform reasonably well,\n# > segment directions doing so for the maze task, while for the maze task the endpoints + maximum\n# > speed space does not perform well.\n\n# %% tags=[\"claim:fig6-maze-task-spaces\"]\nrows = []\nfor seg in [\"segment dirs (t)\", \"segment dirs (l)\"]:\n    for R in \"ab\":\n        sd_, iv, ems = F6[\"task\"][seg].mean(), F6[\"task\"][\"initial velocity\"].mean(), F6[\"task\"][\"endpoints + max speed\"].mean()\n        p3 = F6[\"curves\"][(\"peri\", R)].mean(0)[2]\n        rows.append(dict(segments=seg, S=R, seg_dirs=round(sd_, 3), init_vel=round(iv, 3), endpoints_max_speed=round(ems, 3),\n                         peri_3d=round(p3, 3), seg_above_0=sd_ > 0, iv_above_0=iv > 0, ems_below_peri3=ems < p3,\n                         ems_below_seg_and_iv=ems < min(sd_, iv)))\nf6m = pd.DataFrame(rows)\nprint(f6m.to_string(index=False))\nfor r_ in SEL_READINGS:\n    T = F6_all[r_][\"task\"]\n    print(r_, {k: round(T[k].mean(), 3) for k in [\"segment dirs (t)\", \"segment dirs (l)\", \"initial velocity\", \"endpoints + max speed\"]})\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## high-dimensional-task-spaces-underperform\n#\n# > The high-dimensional task spaces, including the kitchen-sink space, always perform below the\n# > peri-movement space, so high dimensionality alone does not explain its performance.\n\n# %% tags=[\"claim:high-dimensional-task-spaces-underperform\"]\nrows = []\nfor R in \"ab\":\n    peri = F6[\"curves\"][(\"peri\", R)].mean(0)\n    for nm in [\"kitchen sink (t)\", \"kitchen sink (l)\", \"segment dirs (t)\", \"segment dirs (l)\"]:\n        v = F6[\"task\"][nm].mean()\n        rows.append(dict(space=nm, dim=dims[nm], S=R, perf=round(v, 3), peri_same_k=peri[dims[nm] - 1].round(3),\n                         peri_best=peri.max().round(3), below_same_k=v < peri[dims[nm] - 1], below_best=v < peri.max()))\nf6h = pd.DataFrame(rows)\nprint(f6h.to_string(index=False))\nfor r_ in SEL_READINGS:\n    T, Cc = F6_all[r_][\"task\"], F6_all[r_][\"curves\"]\n    print(r_, \"kitchen sink (t)\", round(T[\"kitchen sink (t)\"].mean(), 3), \"| peri 11-D (S a)\", Cc[(\"peri\", \"a\")].mean(0)[10].round(3),\n          \"| peri best (S a)\", Cc[(\"peri\", \"a\")].mean(0).max().round(3))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## some-neurons-better-elsewhere\n#\n# > Although the peri-movement space performs best on average, some individual neurons are better\n# > captured in one of the other spaces.\n\n# %% tags=[\"claim:some-neurons-better-elsewhere\"]\nrows = []\nfor R in \"ab\":\n    pc = F6[\"curves\"][(\"peri\", R)]\n    kbest = pc.mean(0).argmax()\n    peri_n = pc[:, kbest]\n    others = {}\n    kc = F6[\"curves\"][(\"kinematic win a rep a\", R)]\n    others[\"kinematic (win a rep a)\"] = kc[:, kc.mean(0).argmax()]\n    for nm, v in F6[\"task\"].items():\n        others[nm] = v\n    O = np.column_stack(list(others.values()))\n    better = O.max(1) > peri_n\n    rows.append(dict(S=R, peri_k=KS[kbest], neurons=len(peri_n), better_elsewhere=int(better.sum()),\n                     fraction=round(better.mean(), 3)))\n    if R == \"a\":\n        print(\"Neurons better in each space (S a):\", {k: int((v > peri_n).sum()) for k, v in others.items()})\nprint(pd.DataFrame(rows).to_string(index=False))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig6-preparatory-dimensionality\n#\n# > Preparatory activity needs 7 to 10 dimensions, depending on the dataset, to capture 90% of its\n# > variance.\n\n# %% tags=[\"claim:fig6-preparatory-dimensionality\"]\nrows = []\nfor r_ in SEL_READINGS:\n    d = condition_data(*r_)\n    prep_ok, _ = neuron_sets(d, \"range\")\n    for nset, mask in [(\"a PD neurons\", prep_ok), (\"b all units\", np.ones(len(units), bool))]:\n        X = d[\"prep\"][:, mask]\n        for norm in [\"a none\", \"b unit range\"]:\n            Xn = X if norm.startswith(\"a\") else X / (X.max(0) - X.min(0) + 1e-12)\n            ev = M.explained(Xn @ Xn.T)\n            k90 = int(np.searchsorted(np.cumsum(ev), 0.9) + 1)\n            rows.append(dict(onset=r_[0], proto=r_[1], combine=r_[2], neurons=nset, n=int(mask.sum()), normalization=norm,\n                             pcs_90=k90, in_6_3_to_11=6.3 <= k90 <= 11))\nf6dim = pd.DataFrame(rows)\nprint(f6dim.to_string(index=False))\nprint(\"Bound c - 1 =\", len(conds) - 1)\n# noise reference: the same count when trial labels are shuffled within the main selection\nrng_dim = np.random.default_rng(6)\nsel = d0[\"sel\"]\ngo_all = M.bin_spikes(st, tr.go_cue_time.values, (M.PREP[0], M.PREP[1]))\ncnt = go_all[sel].sum(2).astype(float) / ((M.PREP[1] - M.PREP[0]) / 1000)\nk_sh = []\nfor _ in range(20):\n    cs = rng_dim.permutation(cond[sel])\n    Xs = np.stack([cnt[cs == c].mean(0) for c in conds])[:, neuron_sets(d0, \"range\")[0]]\n    ev = M.explained(Xs @ Xs.T); k_sh.append(int(np.searchsorted(np.cumsum(ev), 0.9) + 1))\nprint(\"Reference: PCs for 90% with condition labels shuffled (main selection, PD neurons, 20 draws): median\", np.median(k_sh),\n      \"range\", min(k_sh), \"to\", max(k_sh))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig7a-shuffled-space-poor\n#\n# > A peri-movement space built after randomly inverting each condition's peri-movement response on\n# > half the conditions performs poorly.\n\n# %% tags=[\"claim:fig7a-shuffled-space-poor\"]\nrng7a = np.random.default_rng(7)\nX = d0[\"prep\"]\nr0 = M.MOVE_WIN[0]\nref = d0[\"mv_rate\"][:, :, M.TMAT[0] - r0][:, :, None]\nseg = d0[\"mv_rate\"][:, :, M.TMAT[0] - r0: M.TMAT[1] - r0]\nsh_curves = {\"a\": [], \"b\": []}\nfor draw in range(20):\n    flip = rng7a.random(seg.shape[:2]) < 0.5\n    segs = np.where(flip[:, :, None], 2 * ref - seg, seg)\n    Gu = M.grams_per_unit(segs, M.TMAT[0])\n    for R in \"ab\":\n        sh_curves[R].append(M.perf_curves_pca(X, Gu.sum(0), Gu, F6[\"fit\"], KS, R == \"b\").mean(0))\nrows = []\nfor R in \"ab\":\n    sh = np.mean(sh_curves[R], 0)\n    peri = F6[\"curves\"][(\"peri\", R)].mean(0)\n    kin = max(F6[\"curves\"][(f\"kinematic win {kw} rep {rp}\", R)].mean(0).max() for kw in \"ab\" for rp in \"ab\")\n    task = task_tab.max()\n    rows.append(dict(S=R, shuffled_best=sh.max().round(3), shuffled_best_k=KS[sh.argmax()], peri_best=peri.max().round(3),\n                     best_kin=round(kin, 3), best_task=round(task, 3), a_below_peri=sh.max() < peri.max(),\n                     b_below_kin_and_task=sh.max() < min(kin, task),\n                     draws_best_range=f\"{np.min([c.max() for c in sh_curves[R]]):.3f} to {np.max([c.max() for c in sh_curves[R]]):.3f}\"))\nprint(pd.DataFrame(rows).to_string(index=False))\nprint(\"Shuffled mean curve (S a):\", np.round(np.mean(sh_curves[\"a\"], 0), 3))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig7b-window-start-slide\n#\n# > Sliding the start of the peri-movement window from 150 ms before movement onset to movement onset\n# > barely lowers PD performance, to 97% (monkey J) and 94% (monkeys A, B) of its original value.\n\n# %% tags=[\"claim:fig7b-window-start-slide\"]\nstarts = [-150, -125, -100, -75, -50, -25, 0]\nrows = []\nfor R in \"ab\":\n    for endr in [\"a fixed\", \"b shifted\"]:\n        perf = []\n        for s in starts:\n            end = M.TMAT[1] if endr.startswith(\"a\") else M.TMAT[1] + (s - M.TMAT[0])\n            Gu = M.grams_per_unit(d0[\"mv_rate\"], M.MOVE_WIN[0], win=(s, end))\n            perf.append(M.perf_curves_pca(X, Gu.sum(0), Gu, F6[\"fit\"], KS, R == \"b\").mean(0).max())\n        perf = np.array(perf)\n        rows.append(dict(S=R, window_end=endr, **{f\"start {s}\": round(p, 3) for s, p in zip(starts, perf)},\n                         fraction=round(perf[-1] / perf[0], 3)))\nf7b = pd.DataFrame(rows)\nf7b[\"within_0.97_tol\"] = (f7b.fraction - 0.97).abs() <= 0.097\nf7b[\"within_0.846_1.067\"] = f7b.fraction.between(0.846, 1.067)\nprint(f7b.to_string(index=False))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Anterior and posterior sites\n#\n# The electrode table gives no positions (x, y, z are empty), so AP location can only be read as\n# the array (reading (b) of the claims file): PMd anterior, M1 posterior. The units' electrode\n# references all point at PMd rows; the array is read from the unit id (prefix 1 or 2), and prefix\n# 1 is taken as PMd because the electrode table lists the PMd group first. This is an assumption.\n\n# %% [markdown]\n# ### ap-location-no-effect-j-array\n#\n# > For the J-array dataset the correlation between preparatory and peri-movement tuning does not\n# > depend on anterior-posterior location (r = 0.20, p = 0.27).\n\n# %% tags=[\"claim:ap-location-no-effect-j-array\"]\nrows = []\nfor r_ in SEL_READINGS:\n    d = condition_data(*r_)\n    idx, r, _ = corr_set(d, neuron_sets(d, \"range\")[1])\n    ap = (units.id_array.values[idx] == 1).astype(float)  # 1 = PMd (anterior)\n    if len(r) > 2 and 0 < ap.sum() < len(ap):\n        lr = stats.linregress(ap, r)\n        rows.append(dict(onset=r_[0], proto=r_[1], combine=r_[2], n=len(r), n_pmd=int(ap.sum()), r=round(lr.rvalue, 3),\n                         p=round(lr.pvalue, 4), mean_r_pmd=round(r[ap == 1].mean(), 3), mean_r_m1=round(r[ap == 0].mean(), 3)))\nfap = pd.DataFrame(rows)\nfap[\"absence_holds_p>=0.05\"] = fap.p >= 0.05\nprint(fap.to_string(index=False))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### prep-activity-more-anterior\n#\n# > Preparatory activity is more prevalent at anterior sites.\n\n# %% tags=[\"claim:prep-activity-more-anterior\"]\nrows = []\nfor r_ in SEL_READINGS:\n    for how in [\"range\", \"sd\"]:\n        prep_ok, _ = neuron_sets(condition_data(*r_), how)\n        a1, a2 = units.id_array.values == 1, units.id_array.values == 2\n        tab = [[int(prep_ok[a1].sum()), int((~prep_ok[a1]).sum())], [int(prep_ok[a2].sum()), int((~prep_ok[a2]).sum())]]\n        rows.append(dict(onset=r_[0], proto=r_[1], combine=r_[2], tuning=how, pmd_pass=f\"{tab[0][0]}/{a1.sum()}\",\n                         m1_pass=f\"{tab[1][0]}/{a2.sum()}\", frac_pmd=round(tab[0][0] / a1.sum(), 3),\n                         frac_m1=round(tab[1][0] / a2.sum(), 3), fisher_p=round(stats.fisher_exact(tab)[1], 4)))\nfpa = pd.DataFrame(rows)\nfpa[\"a_higher_pmd\"] = fpa.frac_pmd > fpa.frac_m1\nfpa[\"b_fisher\"] = fpa.a_higher_pmd & (fpa.fisher_p < 0.05)\nprint(fpa.to_string(index=False))\ntp_ = M.tuning_strength(d0[\"prep\"], \"range\")\nprint(\"Median preparatory tuning range (spikes/s), main reading: PMd\", np.median(tp_[units.id_array == 1]).round(2),\n      \"| M1\", np.median(tp_[units.id_array == 2]).round(2), \"| Mann-Whitney p\",\n      round(stats.mannwhitneyu(tp_[units.id_array == 1], tp_[units.id_array == 2]).pvalue, 4))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ### fig7c-anterior-posterior-performance\n#\n# > The peri-movement space captures preparatory tuning at both anterior and posterior sites, with\n# > normalized performance only slightly different from that of randomly divided data, and slightly\n# > better at anterior sites.\n\n# %% tags=[\"claim:fig7c-anterior-posterior-performance\"]\nrng7c = np.random.default_rng(70)\nprep_ok0 = neuron_sets(d0, \"range\")[0]\nGu_all = M.grams_per_unit(d0[\"mv_rate\"], M.MOVE_WIN[0])\n\ndef half_perf(members, R):\n    \"\"\"6-D peri-movement performance of the PD neurons in `members`, from a space built from\n    `members` only, normalized by the upper limit from the same units (6-D or best k).\"\"\"\n    mem = np.where(members)[0]\n    fit = np.where(members & prep_ok0)[0]\n    Gu = Gu_all[mem]; Gt = Gu.sum(0)\n    Xh = X[:, mem]\n    Gp = M.prep_grams(Xh)\n    loc = {n: i for i, n in enumerate(mem)}\n    peri = np.mean([M.pd_performance_pca(X[:, n], Gt - Gu[loc[n]], [6], R == \"b\")[0] for n in fit])\n    up = np.mean([M.pd_performance_pca(X[:, n], Gp.sum(0) - Gp[loc[n]], KS, R == \"b\") for n in fit], 0)\n    return peri, up[5], up.max(), len(fit)\n\nrows = []\nfor R in \"ab\":\n    res = {}\n    res[\"all\"] = half_perf(np.ones(len(units), bool), R)\n    res[\"anterior (PMd)\"] = half_perf(units.id_array.values == 1, R)\n    res[\"posterior (M1)\"] = half_perf(units.id_array.values == 2, R)\n    rand = []\n    for _ in range(20):\n        m = np.zeros(len(units), bool); m[rng7c.choice(len(units), len(units) // 2, replace=False)] = True\n        rand += [half_perf(m, R), half_perf(~m, R)]\n    for nm, (p, u6, ub, n) in res.items():\n        rows.append(dict(S=R, subset=nm, neurons=n, perf_6d=round(p, 3), upper_6d=round(u6, 3), upper_best=round(ub, 3),\n                         norm_a=round(p / u6, 3), norm_b=round(p / ub, 3)))\n    rp = np.array([(p / u6, p / ub) for p, u6, ub, n in rand])\n    rows.append(dict(S=R, subset=\"random halves (20 splits)\", neurons=np.mean([x[3] for x in rand]),\n                     perf_6d=round(np.mean([x[0] for x in rand]), 3), upper_6d=round(np.mean([x[1] for x in rand]), 3),\n                     upper_best=round(np.mean([x[2] for x in rand]), 3), norm_a=round(rp[:, 0].mean(), 3), norm_b=round(rp[:, 1].mean(), 3)))\nf7c = pd.DataFrame(rows)\nprint(f7c.to_string(index=False))\nfor R in \"ab\":\n    for nrm in [\"norm_a\", \"norm_b\"]:\n        t = f7c[f7c.S == R].set_index(\"subset\")[nrm]\n        ant, post, rnd = t[\"anterior (PMd)\"], t[\"posterior (M1)\"], t[\"random halves (20 splits)\"]\n        print(f\"S {R}, {nrm}: both > 0: {ant > 0 and post > 0}; both within 10% of random ({rnd:.3f}): \"\n              f\"{abs(ant - rnd) <= 0.1 * abs(rnd) and abs(post - rnd) <= 0.1 * abs(rnd)}; anterior higher: {ant > post}\")\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig7d-pd-consistency\n#\n# > The PD is most stable across random condition subsets when measured in the peri-movement space,\n# > for every comparison and all four datasets.\n\n# %% tags=[\"claim:fig7d-pd-consistency\"]\nrng7d = np.random.default_rng(71)\nGt_all = Gu_all.sum(0)\nkin_curve = F6[\"curves\"][(\"kinematic win a rep a\", \"a\")].mean(0)\nk_kin = KS[kin_curve.argmax()]\nGk = M.kinematic_gram(d0[\"pos\"], d0[\"vel\"], M.MOVE_WIN[0], len(units) - 1)\nS_kin = M.pca_scores(Gk, k_kin)\ncomps = [(\"endpoints + max speed\", F6[\"spaces\"][\"endpoints + max speed\"]),\n         (\"segment dirs (t)\", F6[\"spaces\"][\"segment dirs (t)\"]),\n         (\"segment dirs (l)\", F6[\"spaces\"][\"segment dirs (l)\"]),\n         (f\"kinematic (best k = {k_kin})\", S_kin)]\nrows = []\nfor nm, S in comps:\n    k = S.shape[1]\n    other, peri = [], []\n    for n in F6[\"fit\"]:\n        x = X[:, n]\n        Sp = M.pca_scores(Gt_all - Gu_all[n], k)\n        other.append(M.pd_consistency(x, S, rng7d))\n        peri.append(M.pd_consistency(x, Sp, rng7d))\n    other, peri = np.array(other), np.array(peri)\n    rows.append(dict(comparison=nm, dim=k, other_space=round(other.mean(), 3), peri_space=round(peri.mean(), 3),\n                     peri_higher=peri.mean() > other.mean(), neurons_peri_higher=f\"{int((peri > other).sum())}/{len(peri)}\",\n                     wilcoxon_p=round(stats.wilcoxon(peri, other).pvalue, 4)))\nf7d = pd.DataFrame(rows)\nprint(f7d.to_string(index=False))\nprint(\"Kinematic best k from the Figure 6 curve (S a, window a, replication a):\", k_kin)\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## fig8-linear-dynamics-simulation\n#\n# > In a simulated two-unit linear dynamical system with 25 random initial states, preparatory\n# > activity correlates weakly with peri-movement activity at the single-unit level (r = 0.08), yet\n# > a PD in the PCA-based peri-movement space captures preparatory tuning perfectly.\n#\n# x(t+1) = W x(t), W = [1, -2pi/360; 2pi/360, 1] (Figure 8 legend). Readings: initial states uniform\n# in [-1, 1]^2 or standard Gaussian; the gray interval one full cycle (360 steps) or the first\n# quarter cycle (90 steps) after release. 1000 draws each.\n\n# %% tags=[\"claim:fig8-linear-dynamics-simulation\"]\nrng8 = np.random.default_rng(8)\neps = 2 * np.pi / 360\nW = np.array([[1, -eps], [eps, 1]])\ndef simulate(x0, steps):\n    out = np.empty((len(x0), steps, 2)); x = x0.copy()\n    for t in range(steps):\n        x = x @ W.T; out[:, t] = x\n    return out\nrows = []\nfor dist in [\"uniform\", \"gaussian\"]:\n    for steps in [360, 90]:\n        rs, perf = [], []\n        for _ in range(1000):\n            x0 = rng8.uniform(-1, 1, (25, 2)) if dist == \"uniform\" else rng8.standard_normal((25, 2))\n            tr8 = simulate(x0, steps)\n            rs.append(np.corrcoef(x0[:, 0], tr8[:, :, 0].mean(1))[0, 1])\n            T8 = tr8.reshape(25, -1)\n            S8 = M.pca_scores(T8 @ T8.T, 2)\n            A8 = np.column_stack([np.ones(25), S8])\n            coef, *_ = np.linalg.lstsq(A8, x0[:, 0], rcond=None)\n            perf.append(1 - ((A8 @ coef - x0[:, 0]) ** 2).mean() / x0[:, 0].var())\n        rs = np.array(rs)\n        lo, hi = np.percentile(rs, [2.5, 97.5])\n        rows.append(dict(initial=dist, interval_steps=steps, median_r=round(np.median(rs), 3), central95=f\"{lo:.3f} to {hi:.3f}\",\n                         contains_0_08=lo <= 0.08 <= hi, min_perf=np.min(perf), max_perf=np.max(perf)))\nf8 = pd.DataFrame(rows)\nprint(f8.to_string(index=False))\n\n# %% [markdown]\n# **Result: ...**\n\n# %% [markdown]\n# ## Summary\n#\n# (filled after the full run)\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb_src.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/000139-churchland-2010 && . $TMPDIR/dev/bin/activate && date -u && time MPLBACKEND=Agg python $TMPDIR/nb_src.py > $TMPDIR/run1.txt 2>&1; tail -5 $TMPDIR/run1.txt; date -u
```

```
Wed Oct 28 19:57:41 UTC 2026

real	0m2.757s
user	0m2.826s
sys	0m0.199s
Traceback (most recent call last):
  File "/tmp/claude-1001/nb_src.py", line 53, in <module>
    import maze as M
ModuleNotFoundError: No module named 'maze'
Wed Oct 28 19:57:43 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/dev/bin/activate && time PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/nb_src.py > $TMPDIR/run1.txt 2>&1; tail -5 $TMPDIR/run1.txt; date -u
```

```
real	6m10.293s
user	6m5.756s
sys	0m0.697s
 initial  interval_steps  median_r       central95  contains_0_08  min_perf  max_perf
 uniform             360     0.012 -0.397 to 0.387           True       1.0       1.0
 uniform              90     0.703  0.496 to 0.847          False       1.0       1.0
gaussian             360     0.000 -0.400 to 0.404           True       1.0       1.0
gaussian              90     0.711  0.455 to 0.871          False       1.0       1.0
Wed Oct 28 20:03:56 UTC 2026
```

**Agent calls Bash**

```bash
cat $TMPDIR/run1.txt | cut -c1-260
```

```
<persisted-output>
Output too large (37.8KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-encore/fb3175ca-7f04-43f3-89e1-4113f65e12bf/tool-results/bpetaxfkb.txt

Preview (first 2KB):
Assets at 0.220113.0408
  sub-Jenkins/sub-Jenkins_ses-medium_desc-test_ecephys.nwb  695928 bytes
  sub-Jenkins/sub-Jenkins_ses-medium_desc-train_behavior+ecephys.nwb  76604764 bytes
Subject: Jenkins Macaca mulatta | session start 2009-09-29 00:00:00-07:00
Train file: trials 250 | splits {'train': 188, 'val': 62} | success {True: 250}
Test file: trials 100 columns ['start_time', 'stop_time', 'move_onset_time', 'split'] | units 114
Conditions (trial_type x trial_version): 27 | maze_id values: 9 | trial_version counts: {0: 81, 1: 86, 2: 83}
Each condition has one maze_id: True
Trials per condition: min 8 max 10
num_targets by version: {0: array([1]), 1: array([1]), 2: array([3])} | barriers by version: {0: [np.int64(0)], 1: [np.int64(8), np.int64(9)], 2: [np.int64(8), np.int64(9)]}
Delay (ms): range -3 to 998 | trials with delay > 400 ms: 235
Delay column equals go - target times (ms): max |diff| 0.0
rt column equals move - go times (ms): max |diff| 0.0 | rt range 247 989 | median 355.0
Trial duration (s): 2.066 to 4.066 | movement onset to trial end at least 0.959 s | trial start to movement onset at least 0.988 s

Units: 152 | heldout 38 | held-in 114
[... 12 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-encore/fb3175ca-7f04-43f3-89e1-4113f65e12bf/tool-results/bpetaxfkb.txt",
 "offset": 24
}
```

```
24	Unit pairs: largest fraction of spikes within 0.2 ms of the other unit's 0.029 (99th percentile 0.0086)
25	Test segments vs train trials (same 700 ms around onset): smallest summed |count difference| 135 | median 240.0 -> no test segment duplicates a train trial
26	
27	Behaviour samples: 757450 | sample interval within trials (ms): 1.0 | hand x range (mm) -134.5 to 158.5 | y -172.6 to 99.5
28	Hand speed (mm/s): median 5.6 | 99.9th percentile 1008.1
29	hand_vel x against the derivative of hand_pos x: r = 1.0 | slope 1.0 (1 means hand_vel is in mm/s)
30	 event window_ms  accuracy  permuted_labels
31	target (-300, 0)     0.024            0.029
32	target (50, 350)     0.272            0.034
33	    go (-300, 0)     0.336            0.026
34	    go (50, 350)     0.452            0.035 | chance 0.037
35	Mean hand speed around movement onset (mm/s): -300..-100 ms 3.3 | -50..0 17.4 | 0..50 205.7 | 100..300 549.1
36	Onset from hand speed (10% of peak) minus the dataset's move_onset_time (ms): median 12.000000000000455 | 5th to 95th percentile 4.9999999999954525 to 27.000000000030866
37	onset  proto  combine  proto_pass  proto_pass_pct  kept  min_per_cond  max_per_cond
38	    a   mean separate         198            79.2   185             2            10
39	    a   mean   concat         239            95.6   225             6            10
40	    a medoid separate         175            70.0   164             2             9
41	    a medoid   concat         233            93.2   218             5            10
42	    b   mean separate         205            82.0   192             5            10
43	    b   mean   concat         241            96.4   226             6            10
[... 359 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('''# kept (Methods, Task design). The main reading is onset (a), proto (a), separate (a); the others
# are run as variants.''','''# kept (Methods, Task design). The main reading is onset (a), proto (a) the condition mean, and the
# profiles concatenated (b): comparing the profiles separately keeps 70 to 82% of trials, against
# the paper's "typically ~90%", while concatenating them keeps 93 to 96% (table below). The
# condition mean over the medoid is an assumption (a template is usually a mean); both are run.''')
s=s.replace('MAIN = ("a", "mean", "separate")','MAIN = ("a", "mean", "concat")')
s=s.replace('''print("Main reading, preparatory tuning SD (spikes/s): median"''','''# split-half reliability of preparatory tuning: odd against even trials of each condition
sel0 = d0["sel"]
go0 = M.bin_spikes(st, tr.go_cue_time.values, M.PREP).sum(2) / ((M.PREP[1] - M.PREP[0]) / 1000)
halves = []
for h in (0, 1):
    m = np.zeros(len(tr), bool)
    for c in conds:
        ii = np.where(sel0 & (cond == c))[0]
        m[ii[h::2]] = True
    halves.append(np.stack([go0[m & (cond == c)].mean(0) for c in conds]))
pdn = neuron_sets(d0, "range")[0]
rel = np.array([np.corrcoef(halves[0][:, n], halves[1][:, n])[0, 1] for n in np.where(pdn)[0]])
print("Split-half reliability of the preparatory rate vector (odd vs even trials), neurons over 5 spikes/s: median r",
      np.round(np.median(rel), 3), "| Spearman-Brown corrected", np.round(2 * np.median(rel) / (1 + np.median(rel)), 3),
      "| fraction with r > 0.5:", np.round((rel > 0.5).mean(), 3), "| n =", len(rel))
print("Main reading, preparatory tuning SD (spikes/s): median"''')
s=s.replace('''# %% [markdown]
# ## j-array-recordings''','''# %% [markdown]
# ### PD code on synthetic data
#
# A check of `maze.pd_performance_pca`: 27 conditions, a T-matrix of rank 3 plus small noise, and
# preparatory rates linear in its first three PCs plus noise. Performance should be near 1 from
# k = 3 under both readings of S.

# %% tags=["sanity"]
rng_syn = np.random.default_rng(3)
Z = rng_syn.standard_normal((27, 3))
Tsyn = Z @ rng_syn.standard_normal((3, 500)) + 0.01 * rng_syn.standard_normal((27, 500))
xs = 10 + Z @ np.array([2.0, -1.0, 0.5]) + 0.05 * rng_syn.standard_normal(27)
for R in "ab":
    print("S reading", R, np.round(M.pd_performance_pca(xs, Tsyn @ Tsyn.T, [1, 2, 3, 6], R == "b"), 3))
print("Fixed space with the true Z:", round(M.pd_performance_fixed(xs, Z), 3))

# %% [markdown]
# ## j-array-recordings''')
open('nb_src.py','w').write(s)
EOF
grep -n "MAIN =" nb_src.py
```

```
225:MAIN = ("a", "mean", "concat")
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/000139-churchland-2010 && . $TMPDIR/dev/bin/activate && PYTHONPATH=. MPLBACKEND=Agg python $TMPDIR/nb_src.py > $TMPDIR/run2.txt 2>&1; grep -v Warning $TMPDIR/run2.txt | sed -n '/Split-half/,/^Units: 152/p;/neurons_peri_higher/,$p' | cut -c1-250; date -u
```

```
Split-half reliability of the preparatory rate vector (odd vs even trials), neurons over 5 spikes/s: median r 0.374 | Spearman-Brown corrected 0.544 | fraction with r > 0.5: 0.382 | n = 76
Main reading, preparatory tuning SD (spikes/s): median 1.19 | max 9.8
S reading a [0.997 0.998 1.    1.   ]
S reading b [0.99  0.997 1.    1.   ]
Fixed space with the true Z: 1.0
Units: 152 (expected 146 +/- 14.6) -> within tolerance: True
            comparison  dim  other_space  peri_space  peri_higher neurons_peri_higher  wilcoxon_p
 endpoints + max speed    3        0.597       0.698         True               56/76      0.0000
      segment dirs (t)    6        0.605       0.613         True               39/76      0.8970
      segment dirs (l)    6        0.542       0.615         True               45/76      0.0227
kinematic (best k = 2)    2        0.670       0.729         True               54/76      0.0004
Kinematic best k from the Figure 6 curve (S a, window a, replication a): 2
 initial  interval_steps  median_r       central95  contains_0_08  min_perf  max_perf
 uniform             360     0.012 -0.397 to 0.387           True       1.0       1.0
 uniform              90     0.703  0.496 to 0.847          False       1.0       1.0
gaussian             360     0.000 -0.400 to 0.404           True       1.0       1.0
gaussian              90     0.711  0.455 to 0.871          False       1.0       1.0
Wed Oct 28 20:11:24 UTC 2026
```

**Agent calls Bash**

```bash
grep -v Warning $TMPDIR/run2.txt | sed -n '/^Neurons fitted/,/neurons_peri_higher/p' | grep -v "^  " | cut -c1-220
```

```
Neurons fitted: 76 | by array: {1: 35, 2: 41}
Reach end (ms after onset) over conditions: 251 to 619
Mean performance over neurons, by k:
peri | S a                  -0.006  0.045  0.052  0.091  0.100  0.117  0.102  0.061  0.026 -0.008 -0.184 -0.396 -0.574 -0.980
upper | S a                 -0.014  0.054  0.026  0.056  0.068  0.061  0.050 -0.028 -0.099 -0.252 -0.281 -0.394 -0.549 -0.838
upper incl. neuron | S a     0.009  0.096  0.102  0.148  0.165  0.176  0.178  0.122  0.103  0.048  0.029 -0.016 -0.064 -0.097
kinematic win a rep a | S a  0.008  0.016  0.013  0.016 -0.005 -0.040 -0.070 -0.128 -0.176 -0.216 -0.328 -0.480 -0.696 -2.005
kinematic win a rep b | S a  0.008  0.016  0.013  0.016 -0.005 -0.040 -0.071 -0.128 -0.176 -0.216 -0.329 -0.481 -0.694 -2.011
kinematic win b rep a | S a  0.011  0.022  0.018  0.017 -0.004 -0.036 -0.070 -0.128 -0.175 -0.214 -0.216 -0.430 -0.506 -2.317
kinematic win b rep b | S a  0.011  0.022  0.018  0.017 -0.004 -0.036 -0.070 -0.128 -0.175 -0.214 -0.217 -0.431 -0.506 -2.319
peri | S b                  -0.004  0.056  0.065  0.108  0.129  0.145  0.195  0.203  0.205  0.205  0.221  0.225  0.226  0.226
upper | S b                 -0.015  0.058  0.042  0.080  0.103  0.115  0.144  0.184  0.172  0.165  0.157  0.151  0.138  0.098
upper incl. neuron | S b     0.004  0.092  0.091  0.151  0.181  0.205  0.236  0.277  0.275  0.282  0.289  0.297  0.300  0.299
kinematic win a rep a | S b  0.007  0.017  0.015  0.019 -0.002 -0.020 -0.029 -0.046 -0.082 -0.142 -0.105 -0.146 -0.188 -0.196
kinematic win a rep b | S b  0.007  0.017  0.015  0.019 -0.002 -0.020 -0.029 -0.046 -0.082 -0.142 -0.105 -0.146 -0.188 -0.196
kinematic win b rep a | S b  0.010  0.024  0.020  0.020 -0.001 -0.013 -0.028 -0.044 -0.085 -0.165 -0.093 -0.148 -0.181 -0.187
kinematic win b rep b | S b  0.009  0.024  0.020  0.020 -0.001 -0.013 -0.028 -0.044 -0.085 -0.165 -0.093 -0.148 -0.181 -0.187

endpoints + max speed            3     -0.045
initial velocity                 2      0.030
[... 116 more lines not kept]
```

**Agent calls Bash**

```bash
grep -v Warning $TMPDIR/run2.txt | grep -A9 "peri_best_min\|absence_holds\|^Main reading (onset" | cut -c1-200; grep -A3 "Readings meeting" $TMPDIR/run2.txt; grep "a   mean   concat" $TMPDIR/run2.txt | cut -c1-200
```

```
Main reading (onset a, proto mean, separate, range): n = 17 | mean r 0.172 | SD 0.321 | mean Spearman 0.139
Per-array breakdown (main reading): {1: (9, np.float64(0.221)), 2: (8, np.float64(0.117))}
Threshold dependence (main reading, range):
 prep_thr  peri_ratio  n  mean_r  mean_spearman    p_t
        3         1.0 54   0.143          0.118 0.0008
        3         1.5 30   0.114          0.090 0.0405
        3         2.0 16  -0.022         -0.020 0.7565
        4         1.0 44   0.171          0.152 0.0007
        4         1.5 23   0.140          0.126 0.0457
        4         2.0 12  -0.010          0.015 0.9175
--
onset  proto  combine  neurons  peri_best_min  kin_best_max  task_best  peri_highest_all  peri_highest_any
    a   mean separate       85          0.000        -0.019     -0.015              True              True
    a   mean   concat       76          0.117         0.024      0.030              True              True
    a medoid separate       86         -0.042        -0.028     -0.028             False              True
    a medoid   concat       77          0.076         0.019      0.027              True              True
    b   mean separate       81          0.038        -0.003     -0.003              True              True
    b   mean   concat       74          0.120         0.033      0.040              True              True
    b medoid separate       89         -0.024        -0.025     -0.024              True              True
    b medoid   concat       77          0.091         0.021      0.028              True              True
[... 36 more lines not kept]
```

**Agent**

Results are stable. Now writing the conclusions into the notebook, then building the entry.

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_src.py').read()
s=s.replace('print("Main reading (onset a, proto mean, separate, range): n ="','print("Main reading", MAIN, "range: n ="')
s=s.replace('''for R in "ab":
    for nrm in ["norm_a", "norm_b"]:''','''print("Random halves, mean performance over mean upper limit (ratio of means): 6-D upper",
      {R: round(f7c[(f7c.S == R) & (f7c.subset.str.startswith("random"))].perf_6d.iloc[0] /
                f7c[(f7c.S == R) & (f7c.subset.str.startswith("random"))].upper_6d.iloc[0], 3) for R in "ab"})
for R in "ab":
    for nrm in ["norm_a", "norm_b"]:''')
R = {}
R['fig4d']='''**Result: partially reproduced, resting on the reading of the trial selection and of the tuning
measure.** Under the main reading 17 neurons pass both thresholds; the mean Pearson r is 0.172 and the
mean Spearman r 0.139, both outside tolerance (0.13 +/- 0.013, 0.11 +/- 0.011), and the mean is above
zero by the t-test (p = 0.0422) and the Fisher-z t-test (p = 0.0443), not by the Wilcoxon test (p =
0.0714). No reading puts both means in tolerance with p < 0.05. The mean r lies in 0.054 to 0.231 in
all 8 selection readings, with p < 0.05 by some test in 5 of them, so the outcome depends on the
selection reading. The SD measure of tuning leaves no neuron passing both thresholds. With these few
trials per condition the counts move with the thresholds (threshold table).'''
R['fig4u']='''**Result: reproduced.** In every selection reading the correlations run from negative (-0.36 to
-0.50) to positive (0.54 to 0.68) values, the mean is 0.141 to 0.207, no neuron has |r| > 0.8, and the
dip test does not reject unimodality (p = 0.195 to 0.993). Under the main reading n = 17, mean 0.172,
SD 0.321, dip p = 0.788. The sample is small.'''
R['fig4e']='''**Result: reproduced, resting on the reading of the neurons and the time range.** With the
neurons of Figure 4D and the spliced trace (readings a, a, best supported: the legend places 4E with
4A to 4D, and the Supplemental Experimental Procedures name the spliced trace for 4E), the main
reading gives a mean r of 0.703 at 400 ms before onset, 0.492 at 200 ms before and 0.118 at onset,
not above zero (t-test p = 0.1267), and the decline begins at -263 ms. Under the same two readings 7
of 8 selection readings meet the criterion. With the movement-locked trace alone the decline begins
at -307 ms, just outside -300 to -100; with all preparatory neurons the onset value (0.107) is above
zero (p = 0.0036). 22 of 32 combinations meet the criterion.'''
R['supp1']='''**Result: reproduced under the claims file's reading (a), not under (b).** Under the main reading
(17 neurons) the strongest-minus-weakest difference of normalized rate is 0.108 in the preparatory
window and 0.101 at movement onset, a ratio of 0.942: smaller, but not less than half. Under the
separate-profile selections the ratio is 0.184 to 0.357, and with all preparatory neurons 0.047 to
0.213. That the difference shows "little relationship" by onset holds only in those variants.'''
R['fig6d']='''**Result: reproduced, resting on the tuning measure.** Under the main reading the best
peri-movement performance is 0.117 (k = 6) with S fixed and 0.226 (k = 13) with S recomputed, above
the best kinematic space (0.016 to 0.024) and the best task space (initial velocity, 0.030) under all
8 combinations of S, kinematic window and replication. Over the selection readings the peri-movement
space is highest under every combination in 7 of 8 and under some in the eighth. All performances are
low: the split-half reliability of the preparatory tuning is a median r of 0.374, and the
peri-movement best exceeds the estimated upper limit (0.068 with S fixed). Neurons of array 1 carry
most of it (best 0.291, array 2 -0.006).'''
R['fig6e']='''**Result: reproduced.** The peri-movement space is higher in 20 to 21 of 22 comparisons (0.909 to
0.955) under every reading of S, the kinematic window and replication, and the task-space variants,
above the 80% the criterion asks.'''
R['fig6p']='''**Result: reproduced, resting on the reading of S.** With S fixed (adopted, below) the
peri-movement curve rises from -0.006 at k = 1 to 0.117 at k = 6 and falls to -0.980 at k = 14; the
kinematic curves peak at k = 2 and fall to about -2. With S recomputed in each fold the peri-movement
curve peaks at k = 13 (0.226), outside 2 to 10, and is nearly flat above k = 10. S fixed is adopted
because the Methods describe one matrix S per space and refit only the PD on the remaining
conditions.'''
R['fig6m']='''**Result: blocked, the segment division is not settled.** Under the main reading initial
velocity performs above zero (0.030) and endpoints + maximum speed below the 3-D peri-movement space
(-0.045 against 0.052 and 0.065) and below initial velocity. Segment directions are above zero with
segments equal in time (0.008) and below with segments equal in path length (-0.027), so the outcome
turns on a detail the paper does not give. Across the selection readings segment directions are at
or below 0.008 in every case, and initial velocity is negative under the separate-profile readings.'''
R['fig6h']='''**Result: reproduced.** Under the main reading the kitchen-sink spaces (-0.244, -0.221) and
segment directions (0.008, -0.027) are below the peri-movement space at the same dimensionality and
below its best (0.117 with S fixed, 0.226 recomputed), under both readings of the comparison and of
S.'''
R['some']='''**Result: reproduced.** 60 of 76 neurons (0.789) with S fixed, and 44 of 76 (0.579) with S
recomputed, perform better in at least one other space than in the peri-movement space at its best
k.'''
R['dim']='''**Result: not reproduced.** 90% of the variance of the preparatory matrix takes 12 to 19 PCs over
every reading (13 for the main reading's PD neurons unnormalized is 12), outside 6.3 to 11. With
condition labels shuffled the count is 17, so with 6 to 10 trials per condition the count reflects
noise more than the structure of preparatory activity.'''
R['f7a']='''**Result: reproduced.** The shuffled space's best performance, averaged over 20 draws, is -0.069
(S fixed) and -0.010 (recomputed), below the unshuffled peri-movement best (0.117, 0.226) and below
the best kinematic and task spaces (readings a and b).'''
R['f7b']='''**Result: reproduced.** With the window end fixed, performance at the best k falls from 0.117 to
0.107 (fraction 0.911) with S fixed and from 0.226 to 0.218 (0.962) with S recomputed, both within
0.97 +/- 0.097. With the whole window shifted the fractions are 0.853 and 0.937.'''
R['ap']='''**Result: reproduced, resting on the array as the AP location.** Regressing each neuron's tuning
correlation on its array gives r = 0.165, p = 0.5258 under the main reading (17 neurons, 9 on array
1), and p from 0.53 to 0.91 over the selection readings, so the paper's test finds no effect. The
paper's J-array value is r = 0.20, p = 0.27.'''
R['prepant']='''**Result: not reproduced, resting on the tuning measure and on array 1 being PMd.** With the
range measure 35 of 75 units on array 1 (0.467) and 41 of 77 on array 2 (0.532) pass the preparatory
threshold under the main reading (Fisher p = 0.5165); array 1 has the lower fraction in every
selection reading. With the SD measure array 1 is higher (4 of 75 against 1 of 77, p = 0.2064). If
the arrays were the other way round the range result would favour the anterior array.'''
R['f7c']='''**Result: not reproduced.** Neither half is within 10% of the random halves' normalized value under
any reading. The normalization is unstable here: the upper limits are close to zero or negative (6-D
upper limit -0.107 on array 2 and -0.043 for random halves with S fixed), so the ratios swing widely
(random halves -0.711 to 27.1). Without normalization the 6-D performance is 0.271 on array 1 and
-0.060 on array 2 (S fixed; 0.270 and 0.049 recomputed), so the peri-movement space captures tuning on
array 1 but hardly on array 2.'''
R['f7d']='''**Result: reproduced.** PD consistency is higher in the peri-movement space than in endpoints +
maximum speed (0.698 against 0.597, Wilcoxon p < 0.0001), segment directions (0.613 against 0.605 for
time segments, p = 0.897; 0.615 against 0.542 for path segments, p = 0.0227) and the kinematic space
at its best k = 2 (0.729 against 0.670, p = 0.0004). The segment-directions comparison is close for
time segments.'''
R['f8']='''**Result: reproduced under the full-cycle reading of the gray interval.** Over one full cycle
(360 steps) the central 95% of the correlation over 1000 draws is -0.397 to 0.387 (uniform initial
states) and -0.400 to 0.404 (Gaussian), which contains 0.08; over a quarter cycle it is 0.496 to 0.847
and 0.455 to 0.871, which does not. The 2-D PCA peri-movement space fits unit 1's initial rates with
performance 1.0 in every draw.'''
R['jarr']='''**Result: partially reproduced.** The dandiset holds 152 units (within 146 +/- 14.6) from two
arrays, 75 and 77 by unit id, but 27 conditions (9 mazes in 3 versions), not 108, and 250 labelled
trials per unit (350 with the unlabelled test segments) against the paper's 2166. That the 9 mazes are
among the paper's 108 conditions is consistent with the data (same monkey, task and three-version
design) but cannot be shown from the files.'''
import re
parts=s.split('# **Result: ...**')
order=['fig4d','fig4u','fig4e','supp1','fig6d','fig6e','fig6p','fig6m','fig6h','some','dim','f7a','f7b','ap','prepant','f7c','f7d','f8']
print(len(parts)-1, len(order))
out=parts[0]
for k,p in zip(order,parts[1:]):
    out+= '\n'.join('# '+l if l else '#' for l in R[k].split('\n')) + p
s=out
s=s.replace('''# **Result: partially reproduced.** The dandiset holds 152 units (within 146 +/- 14.6) from two
# arrays, but 27 conditions (9 mazes in 3 versions), not 108, and 250 labelled trials per unit. That
# the 9 mazes are among the paper's 108 conditions is consistent with the data (same monkey, task
# and 3-version design) but cannot be shown from the files. The claims file's partial outcome
# applies.''', '\n'.join('# '+l for l in R['jarr'].split('\n')))
open('nb_src.py','w').write(s)
EOF
grep -n "Result: \.\.\.\|filled after" nb_src.py
```

```
18 18
380:# trials per condition the counts move with the thresholds (threshold table). (filled after the full run)
1140:# (filled after the full run)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python - <<'EOF'
s=open('nb_src.py').read()
s=s.replace("(threshold table). (filled after the full run)","(threshold table).")
s=s.replace("every reading (13 for the main reading's PD neurons unnormalized is 12), outside","every reading (12 for the main reading's PD neurons, unnormalized), outside")
s=s.replace("(random halves -0.711 to 27.1)","(random halves -0.740 to 2.115, array 2 up to 8.000)")
s=s.replace('''# ## Summary
#
# (filled after the full run)''','''# ## Summary
#
# | Claim | Outcome |
# |---|---|
# | j-array-recordings | partially reproduced (152 units, but 27 of the 108 conditions and 250 trials) |
# | fig4d-mean-correlation-j-array | partially reproduced, resting on the selection and tuning readings |
# | fig4abc-mean-correlation-other-datasets | blocked: data missing |
# | fig4-broad-unimodal | reproduced |
# | fig4e-correlation-time-course | reproduced, resting on readings |
# | suppfig1-population-psth-weak-movement-tuning | reproduced under reading (a) only |
# | fig6d-perimovement-best-j-array | reproduced |
# | fig6-perimovement-best-each-dimensionality | reproduced |
# | fig6-dimensionality-peak | reproduced, resting on S fixed across folds |
# | fig6-maze-task-spaces | blocked: methods underspecified (segment division) |
# | fig6abc-perimovement-best-other-datasets | blocked: data missing |
# | fig6e-summary-rank | blocked: data missing |
# | fig6-preparatory-dimensionality | not reproduced |
# | fig7a-shuffled-space-poor | reproduced |
# | fig7b-window-start-slide | reproduced |
# | ap-location-no-effect-j-array | reproduced, AP read as the array |
# | ap-location-no-effect-other-datasets | blocked: data missing |
# | fig7c-anterior-posterior-performance | not reproduced |
# | prep-activity-more-anterior | not reproduced, AP read as the array |
# | fig7d-pd-consistency | reproduced |
# | some-neurons-better-elsewhere | reproduced |
# | high-dimensional-task-spaces-underperform | reproduced |
# | fig8-linear-dynamics-simulation | reproduced (full-cycle reading) |
#
# A failure to reproduce here may be a failure of this attempt, not of the paper: see the
# reasoning and the differences from the paper's method.
#
# **How the analysis differs from the paper's.** The paper's J-array dataset has 108 conditions and
# about 2166 trials per neuron; this dandiset has 27 conditions and 6 to 10 kept trials per
# condition, so condition means are noisy (split-half reliability of preparatory tuning, median r =
# 0.374) and every PD performance is low (best about 0.1 to 0.2). The tuning strength is read as the
# range across conditions; the SD reading leaves almost no neuron above 5 spikes/s. The proto-trial is
# the condition-mean velocity profile with the two profiles concatenated (the reading closest to the
# paper's ~90% of trials kept); the other readings are shown. S is fixed across folds where the two
# readings differ. AP location is read as the array, and the array from the unit id. EMG, the
# speed-task and single-electrode datasets are not in the dandiset.
#
# **What was found about the dataset.** The units' electrode references all point to PMd rows of the
# electrode table, although the unit ids give 77 units on a second array whose references (rows 14 to
# 94) look like M1 channels without the offset of 96. The electrode table has no positions. The test
# file's 100 trials have no condition labels or go cue times. Nothing in the files links this
# session (2009-09-29) to the paper's J-array dataset, and the 27 conditions are a quarter of the
# paper's 108.''')
open('nb_src.py','w').write(s)
EOF
date -u
```

```
Wed Oct 28 20:13:09 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . dev/bin/activate && uv pip install -q nbformat && python - <<'EOF'
import re, nbformat
s=open('nb_src.py').read()
s=s.replace("# | fig6-maze-task-spaces | tested |","# | fig6-maze-task-spaces | run; blocked after the analysis (methods_underspecified) |")
cells=[]
for chunk in re.split(r'^# %%', s, flags=re.M)[1:]:
    head, _, body = chunk.partition('\n')
    body=body.strip('\n')
    if head.strip().startswith('[markdown]'):
        md='\n'.join(l[2:] if l.startswith('# ') else ('' if l=='#' else l) for l in body.split('\n'))
        cells.append(nbformat.v4.new_markdown_cell(md))
    else:
        m=re.search(r'tags=(\[.*\])', head)
        c=nbformat.v4.new_code_cell(body)
        if m: c.metadata['tags']=eval(m.group(1))
        cells.append(c)
nb=nbformat.v4.new_notebook(); nb.cells=cells
nb.metadata['kernelspec']={'name':'python3','display_name':'Python 3','language':'python'}
nbformat.write(nb,'entries/000139-churchland-2010/reproduce_churchland_2010.ipynb')
print(len(cells))
EOF
cat tools/entry.py 2>/dev/null | head -5; ls tools | head -50
```

```
75
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
[... 9 more lines not kept]
```

**Agent**

Now entry.yaml, requirements, README.

**Agent calls Bash**

```bash
cd entries/000139-churchland-2010 && cat > entry.yaml <<'EOF'
schema_version: 1
name: 000139-churchland-2010
type: reproduction
title: Preparatory activity and a PD in peri-movement space (Churchland et al. 2010)
description: Tests the findings of Churchland, Cunningham, Kaufman, Ryu and Shenoy (2010) on dandiset
  000139 (MC_Maze_Medium), one session of monkey J on the maze task recorded with two Utah arrays and
  cut to 250 labelled trials over 27 conditions for the Neural Latents Benchmark. It tests the weak
  correlation between preparatory and peri-movement tuning, the performance of a preferred direction
  in peri-movement, kinematic and task spaces, the controls of Figure 7, and the simulation of Figure
  8. The speed-task and single-electrode datasets and the EMG are not in the dandiset.
license: Apache-2.0
notebooks:
- path: reproduce_churchland_2010.ipynb
  title: Reproducing Churchland et al. (2010) from dandiset 000139
  runtime_minutes: 7
helpers:
- maze.py
related:
- id: dandi:000139/0.220113.0408
  relation: uses_data
- id: doi:10.1016/j.neuron.2010.09.015
  relation: reproduces
EOF
printf "diptest\nh5py\nmatplotlib\nnumpy\npandas\npynwb\nremfile\nrequests\nscipy\n" > requirements.in
cd ../.. && sed -n 1,80p tools/entry.py | grep -n "def \|argparse\|add_parser" ; time python tools/entry.py lock entries/000139-churchland-2010 2>&1 | tail -5
```

```
42:import argparse
68:    def __init__(self):
71:    def error(self, where, message: str) -> None:
76:def dataset_id(record: dict) -> str | None:
80:def schema(name: str) -> Draft202012Validator:
wrote entries/000139-churchland-2010/requirements.lock.txt

real	0m0.385s
user	0m0.248s
sys	0m0.071s
```

**Agent**

Now the README, then lock/check/run.

**Agent calls Write**

```json
{
 "file_path": "entries/000139-churchland-2010/README.md",
 "content": "# Churchland, Cunningham, Kaufman, Ryu & Shenoy (2010) from dandiset 000139\n\nTests the findings of [Churchland et al. (2010)](https://doi.org/10.1016/j.neuron.2010.09.015) that can\nbe tested on [DANDI:000139](https://dandiarchive.org/dandiset/000139/0.220113.0408) (MC_Maze_Medium).\nThe dandiset holds one session of monkey J on the maze task, with two Utah arrays (152 units) and 250\nlabelled trials over 27 conditions, cut for the Neural Latents Benchmark. The paper's J-array dataset\nhad 108 conditions and about 2166 trials per neuron, so every measure here rests on far fewer trials.\nThe speed-task and single-electrode datasets and the EMG are not in the dandiset.\n\n| Claim | Outcome |\n|---|---|\n| 146 units, 108 conditions in the J-array dataset | Partially reproduced |\n| Mean preparatory vs peri-movement correlation 0.13 (J-array) | Partially reproduced |\n| Correlations broad and unimodal | Reproduced |\n| Correlation declines from 200 ms before onset to near zero | Reproduced |\n| Population PSTHs show weak movement tuning by onset | Reproduced |\n| Peri-movement space gives the best PD performance | Reproduced |\n| Peri-movement space best at almost every dimensionality | Reproduced |\n| Performance peaks at middle dimensionality | Reproduced |\n| Segment directions and initial velocity perform reasonably well | Blocked: methods underspecified |\n| 7 to 10 dimensions for 90% of preparatory variance | Not reproduced |\n| Shuffled space performs poorly | Reproduced |\n| Window start can slide to onset (97%) | Reproduced |\n| No effect of AP location on the tuning correlation | Reproduced |\n| Anterior and posterior halves perform like random halves | Not reproduced |\n| Preparatory activity more prevalent anteriorly | Not reproduced |\n| PD most stable in peri-movement space | Reproduced |\n| Some neurons better in other spaces | Reproduced |\n| High-dimensional task spaces underperform | Reproduced |\n| Linear dynamical system simulation (Figure 8) | Reproduced |\n| Monkeys A, B and J single-electrode results (four claims) | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the\nreasoning and the differences from the paper's method.\n\nSeveral outcomes rest on readings of methods the paper leaves open (the proto-trial, the tuning\nmeasure, whether the PCA space is recomputed in each cross-validation fold); the notebook runs each\nreading, and the attempt record,\n[`attempts/000139-churchland-2010-01.yaml`](../../attempts/000139-churchland-2010-01.yaml), says which\nwas adopted and why. The units' electrode references all point at the PMd array; the array is read\nfrom the unit ids.\n\n- `reproduce_churchland_2010.ipynb`: the analysis, about seven minutes.\n- `maze.py`: loading the files, trial selection, condition means, the PD model with\n  leave-one-condition-out performance, and the peri-movement, kinematic and task spaces.\n"
}
```

```
File created successfully at: entries/000139-churchland-2010/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/000139-churchland-2010 2>&1 | tail -20
```

```
0 error(s)
```

**Agent calls Bash**

```bash
date -u; time python tools/entry.py all entries/000139-churchland-2010 2>&1 | tail -15; date -u
```

```
Wed Oct 28 20:14:04 UTC 2026
Installed kernelspec registry-000139-churchland-2010 in executed/000139-churchland-2010/.venv/share/jupyter/kernels/registry-000139-churchland-2010
0 error(s)
pass  reproduce_churchland_2010.ipynb  (362 s)

real	6m33.945s
user	6m24.728s
sys	0m4.082s
Wed Oct 28 20:20:38 UTC 2026
```

**Agent**

Passed in 362 s. Checking the executed outputs against the conclusions.

**Agent calls Bash**

```bash
ls executed/000139-churchland-2010/; python - <<'EOF' > $TMPDIR/exec.txt
import nbformat,glob
nb=nbformat.read(glob.glob('executed/000139-churchland-2010/*.ipynb')[0],4)
for c in nb.cells:
    if c.cell_type=='code':
        for o in c.get('outputs',[]):
            if o.get('name')=='stdout': print(o['text'])
            if o.get('output_type')=='error': print('ERROR', o['ename'])
EOF
diff <(grep -v Warning $TMPDIR/exec.txt | grep -v "^\s*$" | grep -v "return num\|f4e\[" ) <(grep -v Warning $TMPDIR/run2.txt | grep -v "^\s*$" | grep -v "return num\|f4e\[") | head -40
```

```
reproduce_churchland_2010.ipynb
result.json
92c92
< Main reading ('a', 'mean', 'concat') range: n = 17 | mean r 0.172 | SD 0.321 | mean Spearman 0.139
---
> Main reading (onset a, proto mean, separate, range): n = 17 | mean r 0.172 | SD 0.321 | mean Spearman 0.139
113d112
<        10         2.0  2  -0.133         -0.142    NaN
383d381
< Random halves, mean performance over mean upper limit (ratio of means): 6-D upper {'a': np.float64(-2.209), 'b': np.float64(1.667)}
```

**Agent**

Executed numbers match the dev run exactly. Now the attempt record; checking the schema first.

**Agent calls Bash**

```bash
ls schemas; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:6000])" 2>/dev/null || ls schemas
```

```
attempt.schema.json
claims.schema.json
entry.schema.json
paper-match.schema.json
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
[... 262 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));p=s['properties']
for k in p:
  if k not in ('dataset','provenance','outcomes','deprecated'): print(k, json.dumps(p[k])[:1500]); print()
"; grep -n "findings:" -A30 attempts/001453-fouke-2025-01.yaml | head -50
```

```
schema_version {"const": 2}

id {"type": "string", "pattern": "^[a-z0-9]+(-[a-z0-9]+)*$"}

paper {"type": "string", "pattern": "^doi:10\\.[0-9]{4,9}/.+$"}

date {"type": "string", "format": "date"}

entry {"description": "The entry this attempt produced (its name), if any.", "type": "string"}

verifications {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["date", "kind", "by", "results"], "properties": {"date": {"type": "string", "format": "date"}, "kind": {"enum": ["agent", "person", "paper_author"]}, "by": {"type": "string"}, "results": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["claim", "agrees"], "properties": {"claim": {"type": "string"}, "agrees": {"type": "boolean"}, "reason": {"description": "The verifier's reason, in its own words.", "type": "string"}, "response": {"description": "What the author changed or replied, kept apart from the verifier's reason.", "type": "string"}, "outcome": {"description": "The outcome the verifier would give.", "enum": ["reproduced", "partially_reproduced", "not_reproduced", "blocked"]}}}}, "reviewed": {"description": "What was reviewed, e.g. a commit, when the attempt changed afterwards.", "type": "string"}}}}

findings {"description": "What the attempt found about the dataset itself, whatever the outcomes. These roll up into the per-dataset report.", "type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["kind", "statement"], "properties": {"kind": {"enum": ["metadata_error", "data_missing", "identifier_missing", "metadata_insufficient", "selection_undocumented", "methods_unavailable", "format_error", "code_mismatch", "paper_inconsistency", "other"]}, "statement": {"type": "string", "minLength": 1}, "found": {"description": "How the finding was found. Unset: by the attempt itself. `on_prompt`: by the reconcile step of a repeat attempt, which checked a finding of the earlier attempt that this one, made blin
[... 36 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "attempts/000139-churchland-2010-01.yaml",
 "content": "schema_version: 2\nid: 000139-churchland-2010-01\ndataset:\n  archive: dandi\n  id: \"000139\"\n  version: 0.220113.0408\n  doi: 10.48324/dandi.000139/0.220113.0408\npaper: doi:10.1016/j.neuron.2010.09.015\ndate: 2026-10-28\nentry: 000139-churchland-2010\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-12\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/catalystneuro/encore/actions/runs/40756774586\noutcomes:\n- claim: j-array-recordings\n  outcome: partially_reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:j-array-recordings\n  measured:\n  - 152\n  - 27\n  - 250\n  notes: The dandiset holds 152 units (within 146 +/- 14.6), 75 and 77 on the two arrays by unit id,\n    recorded over 27 conditions (9 mazes, each in the no-barrier, barrier and distractor versions)\n    and 250 labelled trials per unit, 350 with the 100 unlabelled test segments, against the paper's\n    108 conditions and 2166 trials per neuron. The trial count is reported only, as the criterion\n    says. The criterion's partial outcome applies because the units match and the conditions are a\n    27-condition maze set; that these 9 mazes are among the paper's 108 is consistent with the data\n    (same monkey, task and three-version design) but cannot be shown, as nothing in the files links\n    the session (2009-09-29) to the paper's J-array dataset.\n  deviations:\n  - The 100 test trials of the Neural Latents Benchmark carry no condition labels or go cue times,\n    so only the 250 training and validation trials are used in every analysis.\n- claim: fig4d-mean-correlation-j-array\n  outcome: partially_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig4d-mean-correlation-j-array\n  measured:\n  - 0.172\n  - 0.139\n  notes: Under the adopted reading 17 neurons pass both thresholds; mean Pearson r = 0.172 and mean\n    Spearman r = 0.139, both outside tolerance. The mean is above zero by the t-test (p = 0.042) and\n    the Fisher-z t-test (p = 0.044), not by the Wilcoxon test (p = 0.071). Over the 8 trial-selection\n    readings mean r is 0.141 to 0.207 (all inside 0.054 to 0.231) and p < 0.05 by some test in 5;\n    in the other 3 (onset a with condition-mean proto and separate profiles, onset a with medoid\n    and concatenated profiles, onset b with medoid and separate profiles) p is 0.030 to 0.083 by the\n    best test only in some and the outcome would be not reproduced. No reading puts both means in\n    tolerance with p < 0.05 (onset b, medoid, separate has both in tolerance, 0.141 and 0.119, with\n    p = 0.080). The SD tuning measure leaves no neuron passing both thresholds in any reading. The\n    neuron count changes with the thresholds (14 to 30 at 1.5 times; table in the notebook).\n  deviations:\n  - Assumed the tuning strength is the range across conditions. The Methods give the thresholds in\n    spikes/s of tuning (\"at least 10 spikes/s of preparatory tuning\", Methods, Neural recordings and\n    datasets) without the measure; the SD reading leaves 5 to 8 of 152 units above 5 spikes/s and\n    none passing both thresholds, which cannot be the paper's array analysis, so the range is the\n    reading the paper supports.\n  - Assumed the proto-trial is the condition-mean velocity profile and that the horizontal and\n    vertical profiles are concatenated. The Supplemental Experimental Procedures (Task design and\n    behavioral control) keep \"the subset of trials (typically ~90% of all trials)\" that correlate\n    with the proto-trial at r > 0.9; concatenation keeps 93 to 96% of trials, comparing the\n    profiles separately keeps 70 to 82%. Mean against medoid is not settled by the paper; a template\n    is usually a mean. All 8 readings are shown.\n  - Movement onset is the dataset's move_onset_time (reading a); onset from hand speed (10% of\n    peak, a standard choice, a median 12 ms later) is run as reading b.\n  - 6 to 10 trials per condition, against about 20 in the paper's J-array dataset.\n- claim: fig4abc-mean-correlation-other-datasets\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The dandiset holds one maze-task array session of monkey J. The speed-task datasets of\n    monkeys A and B and the single-electrode monkey J dataset are not in it (assets and metadata\n    checked) and the paper names no other archive for them.\n- claim: fig4-broad-unimodal\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig4-broad-unimodal\n  notes: In every selection reading the per-neuron correlations run from negative (-0.36 to -0.50)\n    to positive (0.54 to 0.68) values, the mean is 0.141 to 0.207, no neuron has |r| > 0.8 while 13\n    to 18 have |r| < 0.5, and Hartigan's dip test does not reject unimodality (p = 0.195 to 0.993).\n    Main reading n = 17, SD 0.321, dip p = 0.788. With 15 to 20 neurons the test has little power.\n  deviations:\n  - Rests on the tuning measure and trial selection adopted in fig4d-mean-correlation-j-array.\n- claim: fig4e-correlation-time-course\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig4e-correlation-time-course\n  notes: With the neurons of Figure 4D and the spliced trace, mean r is 0.703 at 400 ms before onset,\n    0.492 at 200 ms before and 0.118 at onset (not above zero, t-test p = 0.127), and the decline\n    begins at -263 ms. These two readings meet the criterion in 7 of 8 selection readings. The\n    movement-locked trace alone puts the decline at -307 ms, just outside -300 to -100, and with all\n    preparatory neurons the onset value (0.107, n = 76) is above zero (p = 0.0036) and above 0.1;\n    22 of 32 combinations meet the criterion.\n  deviations:\n  - Assumed the neurons of Figure 4A to 4D (both thresholds) and the spliced trace. The legend of\n    Figure 4 places E with A to D, and the Supplemental Experimental Procedures (Computing the mean\n    firing rate) say the spliced trace \"was also useful for the analysis in Figure 4E\". The splice\n    maps the go-locked trace (-200 to +100 ms) to movement time with the median RT (354 ms) and\n    continues with the movement-locked trace; where the paper splices is not given.\n- claim: suppfig1-population-psth-weak-movement-tuning\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:suppfig1-population-psth-weak-movement-tuning\n  notes: Under the main reading (17 neurons) the strongest-minus-weakest difference of normalized\n    rate is 0.108 in the preparatory window and 0.101 at movement onset (ratio 0.942); it is smaller\n    (criterion reading a) in all 8 selection readings but less than half (reading b) only under the\n    separate-profile readings (0.184 to 0.357). The statement's \"little relationship\" by onset is\n    supported under those readings and with all preparatory neurons (ratio 0.047 to 0.213), not\n    under the concatenated-profile readings.\n  deviations:\n  - The two intermediate conditions are those at one third and two thirds of the rank order of\n    preparatory rate, a standard choice (the legend says only \"two intermediate conditions\").\n  - Rests on the tuning measure and trial selection adopted in fig4d-mean-correlation-j-array.\n- claim: fig6d-perimovement-best-j-array\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6d-perimovement-best-j-array\n  notes: 76 neurons fitted. Best peri-movement performance 0.117 (k = 6) with S fixed and 0.226 (k =\n    13) with S recomputed in each fold, against the best kinematic space 0.016 to 0.024 and the best\n    task space 0.030 (initial velocity), under all 8 combinations of S, kinematic window and\n    replication. Over the selection readings the peri-movement space is highest under all\n    combinations in 7 of 8 and under some in the eighth (onset a, medoid, separate). All levels are\n    low; the split-half reliability of preparatory tuning is a median r of 0.374 and the estimated\n    upper limit (0.068, S fixed) is below the peri-movement best. The array-1 neurons reach 0.291 and\n    the array-2 neurons -0.006.\n  deviations:\n  - Rests on the tuning measure and trial selection adopted in fig4d-mean-correlation-j-array.\n  - Reach end, used for endpoints and the trajectory-based task spaces, is where the condition-mean\n    speed falls below 10% of its peak, a standard choice; acceleration is the derivative of the\n    smoothed velocity; the T-matrices are sampled every 10 ms, a standard choice.\n  - The EMG space cannot be built; the paper recorded no EMG for J-array.\n- claim: fig6-perimovement-best-each-dimensionality\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-perimovement-best-each-dimensionality\n  notes: The peri-movement space wins 20 or 21 of 22 comparisons (14 kinematic dimensionalities and 8\n    task spaces), 0.909 to 0.955, under every reading of S, kinematic window and replication, and\n    both sets of task-space variants.\n  deviations:\n  - Rests on the tuning measure and trial selection adopted in fig4d-mean-correlation-j-array.\n- claim: fig6-dimensionality-peak\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-dimensionality-peak\n  notes: With S fixed the peri-movement curve goes from -0.006 at k = 1 to 0.117 at k = 6 and -0.980\n    at k = 14; the kinematic curves peak at k = 2 (0.016 to 0.022) and fall to about -2 at k = 14.\n    With S recomputed in each fold the peri-movement curve peaks at k = 13 (0.226), outside 2 to 10,\n    and is flat above k = 10 (0.221 to 0.226), so the criterion fails under that reading. With S fixed\n    the best k is 2 to 6 in all 8 selection readings.\n  deviations:\n  - Assumed S is computed once from all conditions and only the PD regression leaves the condition\n    out. The Methods (Using a PD, PD performance) define S as \"a c x k matrix containing the location\n    of every condition\" and say \"One condition was left out and we found the PD that best captured\n    tuning for the remaining conditions\", which refits only the PD. The recomputed reading is shown.\n- claim: fig6-maze-task-spaces\n  outcome: blocked\n  blocked_by: methods_underspecified\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-maze-task-spaces\n  notes: Under the main reading initial velocity is above zero (0.030) and endpoints + maximum speed\n    (-0.045) is below the 3-D peri-movement space (0.052 S fixed, 0.065 recomputed) and below initial\n    velocity. Segment directions are above zero with segments equal in time (0.008) and below with\n    segments equal in path length (-0.027), so the two readings give different outcomes, and the\n    paper (\"the individual horizontal and vertical displacements after dividing the reach trajectory\n    into three segments\", Methods, Task spaces) does not say which. Neither choice has a basis in the\n    paper. In the other selection readings segment directions are -0.156 to 0.008 and initial\n    velocity -0.028 to 0.040. The question is asked of the paper's authors (findings).\n- claim: fig6abc-perimovement-best-other-datasets\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Needs the speed-task and single-electrode datasets and EMG, which are not in the dandiset.\n- claim: fig6e-summary-rank\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Pools monkeys A, B and J (single electrodes) and EMG spaces, which are not in the dandiset;\n    the summary excludes J-array.\n- claim: fig6-preparatory-dimensionality\n  outcome: not_reproduced\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig6-preparatory-dimensionality\n  measured: 12\n  notes: 90% of the variance of the c x n preparatory matrix takes 12 PCs for the main reading (PD\n    neurons, not normalized), and 12 to 19 over all readings of neurons, normalization and trial\n    selection, outside 6.3 to 11 and below the bound of 26. With condition labels shuffled the same\n    count is 17, so with 6 to 10 trials per condition it measures noise more than the structure of\n    preparatory activity; the paper had about 20 per condition and 108 conditions.\n- claim: fig7a-shuffled-space-poor\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7a-shuffled-space-poor\n  notes: Averaged over 20 shuffles the shuffled space's best performance is -0.069 with S fixed and\n    -0.010 recomputed (single draws -0.099 to 0.042), below the unshuffled peri-movement best (0.117,\n    0.226), reading a, and below the best kinematic (0.022, 0.024) and task (0.030) spaces, reading b.\n  deviations:\n  - Rests on the tuning measure and trial selection adopted in fig4d-mean-correlation-j-array.\n- claim: fig7b-window-start-slide\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7b-window-start-slide\n  measured: 0.911\n  notes: With the window end fixed at 800 ms, performance at the best k falls from 0.117 to 0.107 as\n    the start moves from -150 ms to onset (fraction 0.911) with S fixed, and from 0.226 to 0.218\n    (0.962) with S recomputed, both within 0.97 +/- 0.097. Shifting the whole window gives 0.853 and\n    0.937; 0.853 is outside 0.97 +/- 0.097 but inside reading b's 0.846 to 1.067.\n  deviations:\n  - S fixed across folds, as adopted in fig6-dimensionality-peak; the recomputed reading also\n    reproduces.\n- claim: ap-location-no-effect-j-array\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:ap-location-no-effect-j-array\n  notes: Regressing each neuron's tuning correlation on its array (PMd 1, M1 0) gives r = 0.165, p =\n    0.526 (17 neurons, 9 on array 1) under the main reading and p = 0.53 to 0.91 over the selection\n    readings, so the paper's test finds no effect at p < 0.05. Mean r is 0.221 on array 1 and 0.117\n    on array 2.\n  deviations:\n  - The electrode table has no positions, so AP location is read as the array (the claims file's\n    reading b) and the median split of the paper cannot be made within an array.\n  - Assumed unit id prefix 1 is the PMd array. The units' electrode references all point at PMd rows;\n    those of prefix-1 units (rows 0 to 89) are consistent with PMd, those of prefix-2 units (rows 14\n    to 94) with M1 channels missing the offset of 96 rows, and the electrode table lists PMd first.\n    The regression's p does not depend on which array is coded 1.\n- claim: ap-location-no-effect-other-datasets\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The single-electrode datasets are not in the dandiset.\n- claim: fig7c-anterior-posterior-performance\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7c-anterior-posterior-performance\n  notes: No half is within 10% of the random halves' normalized value under any reading of S or of\n    the upper limit. The normalization is unstable because the upper limits are near zero or\n    negative (6-D upper limit -0.107 on array 2, -0.043 averaged over random halves, S fixed), so the\n    ratios range from -0.740 to 8.000. Unnormalized 6-D performance is 0.271 on array 1 (PMd) and\n    -0.060 on array 2 (M1) with S fixed, 0.270 and 0.049 recomputed, against 0.095 and 0.140 for\n    random halves; the peri-movement space captures tuning on array 1 but hardly on array 2.\n  deviations:\n  - Halves are the two arrays, not a median split of AP location (no positions in the dandiset);\n    array 1 is taken as PMd, as in ap-location-no-effect-j-array.\n  - Random halves are 20 random splits of the units into two equal halves, a standard choice.\n- claim: prep-activity-more-anterior\n  outcome: not_reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:prep-activity-more-anterior\n  notes: With the range measure 35 of 75 units on array 1 (0.467) and 41 of 77 on array 2 (0.532)\n    pass the 5 spikes/s preparatory threshold (Fisher p = 0.517), and array 1 has the lower fraction\n    in all 8 selection readings. With the SD measure array 1 is higher (4 of 75 against 1 of 77, p =\n    0.206). The outcome depends on array 1 being PMd; if it were M1 the range result would favour the\n    anterior array (still not at p < 0.05). With 6 to 10 trials per condition the range threshold\n    also passes noise, and noise ranges grow with firing rate.\n  deviations:\n  - AP location read as the array and array 1 taken as PMd (see ap-location-no-effect-j-array);\n    tuning measured as the range, as adopted in fig4d-mean-correlation-j-array.\n- claim: fig7d-pd-consistency\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig7d-pd-consistency\n  notes: Mean PD consistency over 76 neurons is higher in the peri-movement space than in endpoints +\n    maximum speed (0.698 against 0.597, Wilcoxon p < 0.0001), segment directions (0.613 against 0.605\n    with time segments, p = 0.897; 0.615 against 0.542 with path segments, p = 0.023) and the\n    kinematic space at its best k = 2 (0.729 against 0.670, p = 0.0004). The segment-directions\n    comparison with time segments is a tie in practice.\n  deviations:\n  - 100 pairs of draws per neuron, a standard choice; S from all conditions; the peri-movement\n    space at the dimensionality of each comparison space.\n  - Rests on the tuning measure and trial selection adopted in fig4d-mean-correlation-j-array.\n- claim: some-neurons-better-elsewhere\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:some-neurons-better-elsewhere\n  notes: 60 of 76 neurons (0.789) with S fixed and 44 of 76 (0.579) with S recomputed perform better\n    in at least one other space than in the peri-movement space at its best k (6 and 13).\n  deviations:\n  - Rests on the tuning measure and trial selection adopted in fig4d-mean-correlation-j-array.\n- claim: high-dimensional-task-spaces-underperform\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:high-dimensional-task-spaces-underperform\n  notes: The kitchen-sink spaces (-0.244 and -0.221) and segment directions (0.008 and -0.027) are\n    below the peri-movement space at the same dimensionality (11-D -0.184 and 6-D 0.117 with S fixed;\n    0.221 and 0.145 recomputed) and below its best (0.117, 0.226), under both readings.\n  deviations:\n  - Rests on the tuning measure and trial selection adopted in fig4d-mean-correlation-j-array.\n- claim: fig8-linear-dynamics-simulation\n  outcome: reproduced\n  assumed: true\n  notebook: reproduce_churchland_2010.ipynb\n  output: claim:fig8-linear-dynamics-simulation\n  notes: With the gray interval read as one full cycle (360 steps), the central 95% of the\n    correlation over 1000 draws is -0.397 to 0.387 (uniform initial states) and -0.400 to 0.404\n    (Gaussian), containing 0.08; over a quarter cycle it is 0.496 to 0.847 and 0.455 to 0.871, not\n    containing it. The 2-D PCA peri-movement space fits unit 1's initial rates with performance 1.0\n    in every draw.\n  deviations:\n  - The distribution of initial states and the gray interval are not given (Figure 8 legend); both\n    readings of each are run and the outcome rests on the full-cycle interval.\nfindings:\n- kind: metadata_error\n  statement: Every unit's electrode reference points at a row of the PMd electrode group, although\n    the unit ids (array x 1000 + channel x 10 + sort) put 77 of the 152 units on a second array. The\n    references of those units (rows 14 to 94) match their channel numbers without the offset of 96\n    that would place them on the M1 rows, so the M1 units are labelled as PMd.\n- kind: metadata_insufficient\n  statement: The electrode table's x, y, z and impedance columns are empty, so the anterior-posterior\n    location of a unit cannot be read; the array is known only through the unit id convention, which\n    the files do not describe.\n- kind: data_missing\n  statement: The dandiset holds one array session of monkey J on the maze task with 27 conditions and\n    250 labelled trials. The paper's J-array dataset had 108 conditions and about 2166 trials per\n    neuron, and the speed-task datasets of monkeys A and B, the single-electrode monkey J dataset and\n    all EMG are not deposited, so 4 of the paper's main findings cannot be tested and the others rest\n    on 6 to 10 trials per condition.\n- kind: identifier_missing\n  statement: Nothing in the files or the dandiset metadata says whether this session (2009-09-29) is\n    the paper's J-array recording or a different one, or how its 27 conditions relate to the paper's\n    108.\n- kind: selection_undocumented\n  statement: The files keep 250 successful trials split into train and val, and 100 test trials as\n    700 ms segments without condition labels, go cue or behaviour. How the trials and the 9 mazes\n    were chosen from the session is not described.\n- kind: methods_unavailable\n  statement: For the paper's authors. The supplement keeps trials whose velocity profiles correlate\n    with a reference proto-trial at r > 0.9. Is the proto-trial the condition mean or one trial, and\n    are the horizontal and vertical profiles correlated separately or together? Here separate\n    comparison keeps 70 to 82% of trials and concatenation 93 to 96%, against the stated ~90%; the\n    mean with concatenation was assumed, and the mean correlation of Figure 4D passes p < 0.05 under\n    5 of 8 readings.\n- kind: methods_unavailable\n  statement: For the paper's authors. How is \"spikes/s of preparatory tuning\" measured (range or\n    standard deviation of condition means)? The range was assumed; with the standard deviation almost\n    no array unit passes 5 spikes/s.\n- kind: methods_unavailable\n  statement: For the paper's authors. In the leave-one-condition-out performance, is the PCA-based\n    space S recomputed without the left-out condition? S fixed was assumed (one S per space, only the\n    PD refitted). With S recomputed, peri-movement performance here does not decline at high\n    dimensionality (best k = 13).\n- kind: methods_unavailable\n  statement: For the paper's authors. For the segment-directions and kitchen-sink spaces, is the\n    reach divided into three segments of equal time or equal path length? Here segment directions\n    perform above zero with time segments (0.008) and below with path segments (-0.027), which\n    decides fig6-maze-task-spaces, blocked for this reason.\n- kind: methods_unavailable\n  statement: For the paper's authors. How was movement onset detected, where is the go-locked trace\n    spliced to the movement-locked one in Figure 4E, and what is the gray interval of Figure 8? Here\n    the dataset's onsets, a splice at the median RT and a full cycle were used, and the other readings\n    shown.\n"
}
```

```
File created successfully at: attempts/000139-churchland-2010-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
grep -A19 "^Threshold dependence" $TMPDIR/exec.txt
```

```
Threshold dependence (main reading, range):
 prep_thr  peri_ratio  n  mean_r  mean_spearman    p_t
        3         1.0 54   0.143          0.118 0.0008
        3         1.5 30   0.114          0.090 0.0405
        3         2.0 16  -0.022         -0.020 0.7565
        4         1.0 44   0.171          0.152 0.0007
        4         1.5 23   0.140          0.126 0.0457
        4         2.0 12  -0.010          0.015 0.9175
        5         1.0 34   0.173          0.147 0.0029
        5         1.5 17   0.172          0.139 0.0422
        5         2.0  7  -0.006         -0.009 0.9621
        6         1.0 25   0.177          0.162 0.0153
        6         1.5 11   0.165          0.150 0.1639
        6         2.0  4  -0.084         -0.114 0.7226
        8         1.0 18   0.203          0.193 0.0236
        8         1.5  6   0.210          0.192 0.2293
        8         2.0  2  -0.133         -0.142    NaN
       10         1.0  7   0.111          0.089 0.5579
       10         1.5  3   0.135          0.089 0.7182
       10         2.0  2  -0.133         -0.142    NaN
```

**Agent calls Edit**

```json
{
 "replace_all": false,
 "file_path": "attempts/000139-churchland-2010-01.yaml",
 "old_string": "    readings mean r is 0.141 to 0.207 (all inside 0.054 to 0.231) and p < 0.05 by some test in 5;\n    in the other 3 (onset a with condition-mean proto and separate profiles, onset a with medoid\n    and concatenated profiles, onset b with medoid and separate profiles) p is 0.030 to 0.083 by the\n    best test only in some and the outcome would be not reproduced. No reading puts both means in\n    tolerance with p < 0.05 (onset b, medoid, separate has both in tolerance, 0.141 and 0.119, with\n    p = 0.080). The SD tuning measure leaves no neuron passing both thresholds in any reading. The\n    neuron count changes with the thresholds (14 to 30 at 1.5 times; table in the notebook).",
 "new_string": "    readings mean r is 0.141 to 0.207 (all inside 0.054 to 0.231) and p < 0.05 by some test in 5;\n    in the other 3 (onset a with condition-mean proto and separate profiles, onset a with medoid\n    and concatenated profiles, onset b with medoid and separate profiles) the smallest p is 0.052,\n    0.056 and 0.080, and the outcome would be not reproduced. No reading puts both means in\n    tolerance with p < 0.05 (onset b, medoid, separate has both in tolerance, 0.141 and 0.119, with\n    p = 0.080). The SD tuning measure leaves no neuron passing both thresholds in any reading. The\n    result moves with the thresholds (at 1.5 times, 3 to 30 neurons and mean r 0.114 to 0.210 for\n    preparatory thresholds of 10 to 3 spikes/s; table in the notebook)."
}
```

```
The file attempts/000139-churchland-2010-01.yaml has been updated successfully. (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python tools/entry.py check entries/000139-churchland-2010 2>&1 | tail -5; python -c "
import yaml;d=yaml.safe_load(open('attempts/000139-churchland-2010-01.yaml'));print(len(d['outcomes']))
import collections;print(collections.Counter(o['outcome'] for o in d['outcomes']))"; grep -rn "—\|rather" attempts/000139-churchland-2010-01.yaml entries/000139-churchland-2010/*.md entries/000139-churchland-2010/*.py $TMPDIR/nb_src.py | head; ls tests | head
```

```
0 error(s)
23
Counter({'reproduced': 13, 'blocked': 5, 'not_reproduced': 3, 'partially_reproduced': 2})
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

**Agent**

Check passes. Running the handover step.

**Agent calls Bash**

```bash
python tools/entry.py handover entries/000139-churchland-2010 2>&1 | tail -5; ls executed/000139-churchland-2010/handover/; git status --short; date -u
```

```
wrote executed/000139-churchland-2010/handover
10.1016-j.neuron.2010.09.015.yaml
maze.py
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
?? attempts/000139-churchland-2010-01.yaml
?? entries/000139-churchland-2010/
?? scripts
Wed Oct 28 20:23:05 UTC 2026
```

**Agent**

I've done steps 1 to 6 for DANDI:000139, pinned at 0.220113.0408. It is the only published version and the paper cites none. The notebook passes `entry.py check` and ran clean under `entry.py all` in 362 s; the handover package is built. I did not verify my own work.

## 1. Outcomes (23 claims)

| Claim | Outcome |
|---|---|
| j-array-recordings | partially reproduced (152 units, but 27 conditions, not 108) |
| fig4d-mean-correlation-j-array | partially reproduced, assumed (r = 0.172, p = 0.042) |
| fig4-broad-unimodal | reproduced, assumed |
| fig4e-correlation-time-course | reproduced, assumed |
| suppfig1-population-psth-weak-movement-tuning | reproduced, assumed (reading (a) only; ratio 0.942) |
| fig6d-perimovement-best-j-array | reproduced, assumed |
| fig6-perimovement-best-each-dimensionality | reproduced, assumed (91 to 96% of comparisons) |
| fig6-dimensionality-peak | reproduced, assumed (S fixed across folds) |
| fig6-maze-task-spaces | blocked: methods_underspecified |
| fig6-preparatory-dimensionality | not reproduced (12 PCs; shuffled labels give 17) |
| fig7a-shuffled-space-poor | reproduced, assumed |
| fig7b-window-start-slide | reproduced, assumed (0.911) |
| ap-location-no-effect-j-array | reproduced, assumed (AP read as the array) |
| fig7c-anterior-posterior-performance | not reproduced, assumed (the normalization is unstable) |
| prep-activity-more-anterior | not reproduced, assumed |
| fig7d-pd-consistency | reproduced, assumed |
| some-neurons-better-elsewhere | reproduced, assumed |
| high-dimensional-task-spaces-underperform | reproduced, assumed |
| fig8-linear-dynamics-simulation | reproduced, assumed (full-cycle interval) |
| fig4abc, fig6abc, fig6e, ap-location-other-datasets | blocked: data_missing |

Totals: 13 reproduced, 2 partially reproduced, 3 not reproduced, 5 blocked.

## 2. Dataset, assumptions, questions

**What the dandiset holds.** One session of monkey J (2009-09-29) on the maze task, cut for the Neural Latents Benchmark:
- 152 units on two arrays (75 and 77 by unit id).
- 250 labelled trials over 27 conditions (9 mazes in 3 versions), so 6 to 10 kept trials per condition. The paper's J-array dataset had about 2166 trials per neuron and 108 conditions.
- The 100 test trials have no condition labels, go cue or behaviour, so they cannot be used.
- No EMG, speed-task or single-electrode data.

Because of the low trial count, preparatory tuning is noisy (median split-half r = 0.374) and all PD performances are low (best 0.117 to 0.226).

**Findings recorded about the dataset:**
- **Metadata error:** every unit's electrode reference points at a PMd row. The second array's units reference rows 14 to 94, which looks like M1 channels missing an offset of 96.
- The electrode x, y and z columns are empty, so AP location can only be read as the array.
- Nothing links this session to the paper's J-array recording.
- How the trials and the 9 mazes were chosen is not documented.

**Assumptions, each stated as a deviation with the passage cited:**
- **Tuning strength is the range across conditions.** With the standard deviation, almost no unit passes 5 spikes/s.
- **Proto-trial is the condition mean, with the two velocity profiles concatenated.** This keeps 93 to 96% of trials, close to the paper's "typically ~90%". Comparing the profiles separately keeps only 70 to 82%.
- **The PCA space S is computed once from all conditions** (the Methods' wording); only the PD is refitted in each fold.
- **Unit id prefix 1 is the PMd array.** This decides the direction of prep-activity-more-anterior.
- **Figure 4E** uses the Figure 4D neurons and a trace spliced at the median RT.
- **Figure 8** uses a full-cycle "gray interval".

**Questions for the paper's authors** (five methods_unavailable findings): how the proto-trial is defined, how tuning strength is measured, whether S is recomputed in each fold, whether the reach is split into segments of equal time or equal path length (this is what blocks fig6-maze-task-spaces), and how movement onset, the Figure 4E splice and the Figure 8 interval were set.

**Questions to a reader:** none. I found no misreading in the claims file.

## 3. Where the protocol was unclear

1. Readings multiply across claims: 8 trial-selection readings times claim-specific readings. The protocol does not say whether a reading adopted for one claim carries to the claims that depend on it. I adopted one main reading for all claims, showed the others, and marked every outcome that depends on it as assumed.
2. It is unclear whether `assumed` covers data identity, such as whether the 27 mazes are among the paper's 108, as well as method choices. I did not mark j-array-recordings as assumed and said so in its notes.
3. Where a criterion's reference value comes out degenerate (fig7c, normalized by an upper limit that is near zero or negative), the protocol gives no rule. I applied the criterion as written (not reproduced) and explained the instability in the notes.
4. The criterion's own readings (any reading suffices) and the open-detail readings of step 1.6 (all must agree) can conflict, as in suppfig1. I applied the criterion's "any reading" rule and noted where the stricter reading fails.

## 4. Runtime and failures

The notebook takes 362 s. The author run took from 19:44 to about 20:23 UTC. Nothing failed.

I did not touch some untracked files at the repo root (`.bashrc`, `.profile`, `.idea` and others) that are not mine. Check them before the workflow commits.

Files are in `entries/000139-churchland-2010/`:
- `reproduce_churchland_2010.ipynb`
- `maze.py`
- `README.md`
- `entry.yaml`
- `requirements.in`
- `requirements.lock.txt`

The attempt record is `attempts/000139-churchland-2010-01.yaml`.

## End of run

56 turns, 35 minutes, result: success.
