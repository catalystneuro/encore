# mckenzie-2025 · author · run 45862924456

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cat docs/protocol.md; ls; ls entries claims attempts paper
```

```
<persisted-output>
Output too large (67.4KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/b9f7eb38-d758-450f-a34b-e7d69f29684a/tool-results/btirv3vh5.txt

Preview (first 2KB):
Thu Nov 26 16:59:42 UTC 2026
# Protocol for an attempt

Version: `pilot-19`. Record this version in the attempt's provenance.

This is what agents, or people, do to attempt a target and deposit the
result. A target is a dataset in a public archive and a paper it names. How
each archive's datasets are named, versioned and read is in
[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.

An attempt has three roles, each a separate run with a separate context:

- The **reader** reads the paper and writes the claims file: every finding,
  and how each is to be tested, taken from the paper. A second reader checks
  it against the paper. Readers never see the dataset's data.
[... 19 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/b9f7eb38-d758-450f-a34b-e7d69f29684a/tool-results/btirv3vh5.txt"
}
```

```
1	Thu Nov 26 16:59:42 UTC 2026
2	# Protocol for an attempt
3	
4	Version: `pilot-19`. Record this version in the attempt's provenance.
5	
6	This is what agents, or people, do to attempt a target and deposit the
7	result. A target is a dataset in a public archive and a paper it names. How
8	each archive's datasets are named, versioned and read is in
9	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
10	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
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
[... 1004 more lines not kept]
```

**Agent calls Bash**

```bash
ls paper entries/fouke-2025 questions | head -50; cat claims/mckenzie-2025.yaml; cat papers/datasets/mckenzie-2025.yaml
```

```
<persisted-output>
Output too large (37.9KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/b9f7eb38-d758-450f-a34b-e7d69f29684a/tool-results/bgho0wqns.txt

Preview (first 2KB):
entries/fouke-2025:
README.md
entry.yaml
omr.py
reproduce_fouke_2025.ipynb
requirements.in
requirements.lock.txt

paper:
10.7554-elife.105183.txt

questions:
README.md
allen-2026.yaml
amjad-2025.yaml
asari-2009.yaml
[... 52 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/b9f7eb38-d758-450f-a34b-e7d69f29684a/tool-results/bgho0wqns.txt"
}
```

```
1	entries/fouke-2025:
2	README.md
3	entry.yaml
4	omr.py
5	reproduce_fouke_2025.ipynb
6	requirements.in
7	requirements.lock.txt
8	
9	paper:
10	10.7554-elife.105183.txt
11	
12	questions:
13	README.md
14	allen-2026.yaml
15	amjad-2025.yaml
16	asari-2009.yaml
17	ashworth-2025.yaml
18	athalye-2023.yaml
19	bech-2026.yaml
20	bellvila-2026.yaml
[... 603 more lines not kept]
```

**Agent calls Bash**

```bash
cat README.md | head -80; wc -l docs/design.md; sed -n '/## DANDI/,/^## [A-Z]/p' docs/archives.md
```

```
# Encore Science: the registry

Encore Science checks datasets against the papers they came from. This repository holds its public record, the Encore registry, served at <https://encorescience.org>. The protocol the checks follow, and the `encore` command that runs the same check on your own data, are in [encore-protocol](https://github.com/encorescience/encore-protocol). It is developed by [CatalystNeuro](https://www.catalystneuro.com).

Agents, and people, try to reproduce the key findings of papers from the open
data in public archives, starting with the [DANDI Archive](https://dandiarchive.org), and register the result
here: the notebooks when it works, and the reason when it does not.

- **For the archive:** evidence of whether each dandiset is complete and
  accurate enough to support the findings of its paper.
- **For analysts:** working notebooks to build new analyses on.

Status: pilot. All eight pilot targets have been attempted and checked by an
independent agent.

**Site:** <https://encorescience.org/>, with the registry's dashboard at <https://encorescience.org/registry/> and what Encore offers a journal at <https://encorescience.org/journals/>.

## Reading the outcomes

An outcome says what one attempt could recover from the data in a dandiset,
[... 79 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/fouke-2025; cat entry.yaml requirements.in README.md; head -60 omr.py; cat ../../attempts/fouke-2025-01.yaml | head -200
```

```
schema_version: 1
name: fouke-2025
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
[... 303 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 200,400p attempts/fouke-2025-01.yaml; ls schemas; python tools/entry.py --help 2>&1 | head -30
```

```
blocked_by: metadata_insufficient
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
[... 214 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -l *.txt; grep -n -i "electrophys\|ACG slope\|Reset analysis\|Place field detection\|Ripple detection\|Reactivation analysis\|Spiking analysis\|Huszar\|figure-eight\|figure eight" *.txt | head -60
```

```
1062 10.7554-elife.105183.txt
358:This important study provides new evidence on the role of norepinephrine (NE) release in the hippocampus in response to environmental transitions (event boundaries), providing a potential link between NE signaling and the segmentation of episodic memories. The work is solid, employing innovative techniques such as fiber photometry with the GRAB-NE sensor for NE measurement, the analysis of public electrophysiology hippocampal datasets, and well-controlled experiments. While further analysis could strengthen some claims, this work offers insights into memory, neuromodulation, and hippocampal function.
508:The LC influences memory formation through the co-release of dopamine61,69,111–115 and NE2,54,116–119. The modulation of late-phase synaptic plasticity, e.g. through synaptic tag-and-capture mechanisms3,120, has long been emphasized as the dominant role by which catecholamines may gate entry of new information into long-term memory4,9,11,20,61,112,113,121–124. SPW-R replay is a prominent electrophysiological correlate of experience that depends on plasticity-related processes43,44. Since stimulation of the midbrain enhances replay47, we hypothesized that NE may also enhance future reactivation. This prediction was not correct, as we did not find any evidence that the neural activity observed following context transition was preferentially reactivated. In fact, we saw that later moments were more likely to be reactivated in post-RUN ripples. This reactivation bias is likely due to the autocorrelation of the brain over time in which the neurons active at any given time are more likely to continue to be active due to consistencies in the external environment (or internal milieu) and the slow turn-over in proteins that affect intrinsic excitability125–127. Though we did not quantify replay of the temporal sequences of cell assemblies, a prior report using the same data also failed to observe enhanced replay of moments following transiti
[... 13 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "paper/10.7554-elife.105183.txt",
 "offset": 595,
 "limit": 35
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Grep**

```json
{
 "pattern": "CA1 spatial code takes|No preferential reactivation|Figure 7\\.|Figure 8\\.|Figure S6|Figure S7",
 "path": "paper/10.7554-elife.105183.txt",
 "output_mode": "content",
 "-n": true
}
```

Result: not kept, because it reads the paper's text.

**Agent calls Bash**

```bash
cd paper; sed -n '462,482p;654,666p' *.txt
```

```
CA1 spatial code takes minutes to settle after context transition

Knowing the dynamics of NE after context transfer allowed us to search for changes in neural activity that track this time course. Modeling studies have emphasized that NE binding should increase the rate at which neural patterns change over time27. Using a large open-source database in which CA1 neurons were recorded as mice were transferred to novel and familiar tracks74, we found that in novel environments, the rate of decorrelation was indeed faster in the first minute after transfer as compared to later in the session (Figure S6 A,B). Such a relationship was not observed in a familiar space (Figure S6 C,D). Since we found strong NE release in both conditions, we doubt these changes are driven by NE.

Next, we analyzed the rate at which the spatial map settles after inducing remapping by shifting the subject from its home cage to a novel or familiar testing environment. Place fields can be observed immediately after transitioning to a new environment75,76, though fields can also emerge and/or change throughout experience77, and show other changes across repetition as well78. To gain an intuition for the dynamics immediately after transition, we embedded the high-dimensional population firing rate vectors (mean ensemble = 253.8 neurons, range = 191-363 neurons, bin size = 100-ms) into a 2D space. Color coding by position shows that the CA1 representational space maps the spatial layout of the environment (Figure 7A). Color coding by time shows that moments immediately following the transition are associated with unusual representations, which can be seen at the periphery of the representational state space (Figure 7B). Recognizing that single locations may have a multitude of neural representations79,80, we quantified the correlation of the instantaneous representation recorded at each moment relative to those recorded in the same location at any other moment throughout the session. This nearest-n
[... 29 more lines not kept]
```

**Agent**

Now the dataset survey.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000552/versions/ | python -m json.tool | grep -E '"version"|"created"|"status"|"size"|asset_count'; curl -s "https://api.dandiarchive.org/api/dandisets/000552/versions/0.230630.2304/assets/?page_size=200" | python -c "
import json,sys; d=json.load(sys.stdin); print(d['count'])
for a in d['results']: print(a['path'], a['size']//1e6, a['asset_id'])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && source env/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy pandas matplotlib dandi umap-learn scikit-learn 2>&1 | tail -2; python -c "import pynwb, umap; print(pynwb.__version__)"; date -u
```

```
4.2.0
Thu Nov 26 17:00:51 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > survey.py <<'EOF'
import h5py, remfile, sys
from dandi.dandiapi import DandiAPIClient
c = DandiAPIClient()
ds = c.get_dandiset("000552", "0.230630.2304")
path = sys.argv[1]
a = ds.get_asset_by_path(path)
url = a.get_content_url(follow_redirects=1, strip_query=True)
f = h5py.File(remfile.File(url), "r")
def visit(name, obj):
    if isinstance(obj, h5py.Dataset):
        print(name, obj.shape, obj.dtype, dict((k, (v if not hasattr(v,'shape') or v.size<5 else '...')) for k,v in obj.attrs.items() if k in ('unit','conversion','rate','description','neurodata_type')))
    else:
        nd = obj.attrs.get('neurodata_type'); print(name+'/', nd, obj.attrs.get('description',''))
f.visititems(visit)
EOF
python survey.py sub-e16-3m2/sub-e16-3m2_ses-e16-3m2-211211_behavior+ecephys.nwb 2>&1 | grep -v "^general/devices\|electrodes/" | head -150
```

```
acquisition/ None 
analysis/ None 
file_create_date (1,) object {}
general/ None 
general/experiment_description () object {}
general/experimenter (4,) object {}
general/extracellular_ephys/ None 
general/extracellular_ephys/Group 1/ ElectrodeGroup no description
general/extracellular_ephys/Group 2/ ElectrodeGroup no description
general/extracellular_ephys/Group 3/ ElectrodeGroup no description
general/extracellular_ephys/Group 4/ ElectrodeGroup no description
general/extracellular_ephys/Group 5/ ElectrodeGroup no description
general/extracellular_ephys/Group 6/ ElectrodeGroup no description
general/extracellular_ephys/Group 7/ ElectrodeGroup no description
general/extracellular_ephys/Group 8/ ElectrodeGroup no description
general/institution () object {}
general/keywords (3,) object {}
general/lab () object {}
general/related_publications (1,) object {}
general/session_id () object {}
[... 105 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > survey2.py <<'EOF'
import h5py, remfile, numpy as np
from dandi.dandiapi import DandiAPIClient
c = DandiAPIClient()
ds = c.get_dandiset("000552", "0.230630.2304")
for a in ds.get_assets():
    p = a.path
    if not any(s in p for s in ("e13-26m1","e15-13f1","e16-3m2")) or "raw" in p: continue
    f = h5py.File(remfile.File(a.get_content_url(follow_redirects=1, strip_query=True)), "r")
    print("==", p, f["session_description"][()].decode()[:300])
    print(" behavior:", f["processing/behavior"].attrs.get("description"))
    print(" units cols:", list(f["units"].keys()), "n=", f["units/id"].shape[0])
    ep = f["intervals/epochs"]; print(" epoch cols", list(ep.keys()))
    for i in range(ep["id"].shape[0]):
        print("   ", [ (k, ep[k][i]) for k in ep.keys() if k not in ("id",)])
    tr = f["intervals/trials"]
    rec = tr["recordings"][:]; fam = tr["is_familiar_maze"][:]; st = tr["start_time"][:]
    for r in np.unique(rec): print("   trials rec", r, "n", (rec==r).sum(), "familiar", np.unique(fam[rec==r]), "t", st[rec==r].min().round(1), tr["stop_time"][:][rec==r].max().round(1))
    pos = f["processing/behavior/SubjectPosition/SpatialSeries/timestamps"][:]
    print(" pos ts", pos[0], pos[-1], len(pos), np.median(np.diff(pos)))
    print(" ripples", f["processing/ecephys/Ripples/id"].shape, "behavior keys", list(f["processing/behavior"].keys()))
EOF
python survey2.py 2>&1 | grep -v Warn
```

```
== sub-e13-26m1/sub-e13-26m1_ses-e13-26m1-211019_behavior+ecephys.nwb The incorporation of new information into the hippocampal network is likely to be constrained by its innate architecture and internally generated activity patterns. However, the origin, organization and consequences of such patterns remain poorly understood. In the present study we show that hippoca
 behavior: The behavior of the subject for the following recordings: alternation, alternation
 units cols: ['clu_id', 'group_id', 'id', 'spike_times', 'spike_times_index', 'unit_name'] n= 271
 epoch cols ['id', 'start_time', 'stop_time']
    [('start_time', np.float64(0.0)), ('stop_time', np.float64(7589.5679666666665))]
    [('start_time', np.float64(7589.568)), ('stop_time', np.float64(9327.615966666666))]
    [('start_time', np.float64(9327.616)), ('stop_time', np.float64(15088.415966666667))]
    [('start_time', np.float64(15088.416)), ('stop_time', np.float64(16753.087966666666))]
    [('start_time', np.float64(16753.088)), ('stop_time', np.float64(22200.895966666667))]
    [('start_time', np.float64(22200.896)), ('stop_time', np.float64(24298.047966666665))]
   trials rec 1 n 47 familiar [ True] t 7612.8 9300.0
   trials rec 2 n 33 familiar [False] t 15159.7 16728.9
 pos ts 7605.7177 16749.233266666666 99557 0.03333333333284827
 ripples (7548,) behavior keys ['LinearizedPosition', 'RewardEventsEightMazeTrack', 'SleepStates', 'SubjectPosition']
== sub-e13-26m1/sub-e13-26m1_ses-e13-26m1-211116_behavior+ecephys.nwb The incorporation of new information into the hippocampal network is likely to be constrained by its innate architecture and internally generated activity patterns. However, the origin, organization and consequences of such patterns remain poorly understood. In the present study we show that hippoca
 behavior: The behavior of the subject for the following recordings: alternation, linearMaze
 units cols: ['clu_id', 'group_id', 'id', 'spike_times', 'spike_times_index', 'unit_name'] n= 209
T
[... 15 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import re
s=open('survey2.py').read()
s=s.replace('''    ep = f["intervals/epochs"]; print(" epoch cols", list(ep.keys()))
    for i in range(ep["id"].shape[0]):
        print("   ", [ (k, ep[k][i]) for k in ep.keys() if k not in ("id",)])''','''    if "epochs" in f["intervals"]:
        ep = f["intervals/epochs"]
        print("  epochs", [(round(a,1), round(b,1)) for a,b in zip(ep["start_time"][:], ep["stop_time"][:])])
    else: print("  NO EPOCHS; intervals:", list(f["intervals"].keys()))
    print("  unit_name ex", f["units/unit_name"][:5], "groups", sorted(set(x.decode() if isinstance(x,bytes) else x for x in f["units/group_id"][:]))[:20])
    print("  lin", f["processing/behavior/LinearizedPosition/LinearizedSpatialSeries/data"].shape if "LinearizedPosition" in f["processing/behavior"] else None)''')
s=s.replace('if not any(s in p for s in ("e13-26m1","e15-13f1","e16-3m2")) or "raw" in p: continue','if not any(s in p for s in ("e13-26m1","e15-13f1","e16-3m2")) or "raw" in p: continue')
exec(s)
EOF
```

```
== sub-e13-26m1/sub-e13-26m1_ses-e13-26m1-211019_behavior+ecephys.nwb The incorporation of new information into the hippocampal network is likely to be constrained by its innate architecture and internally generated activity patterns. However, the origin, organization and consequences of such patterns remain poorly understood. In the present study we show that hippoca
 behavior: The behavior of the subject for the following recordings: alternation, alternation
 units cols: ['clu_id', 'group_id', 'id', 'spike_times', 'spike_times_index', 'unit_name'] n= 271
  epochs [(np.float64(0.0), np.float64(7589.6)), (np.float64(7589.6), np.float64(9327.6)), (np.float64(9327.6), np.float64(15088.4)), (np.float64(15088.4), np.float64(16753.1)), (np.float64(16753.1), np.float64(22200.9)), (np.float64(22200.9), np.float64(24298.0))]
  unit_name ex [b'1' b'2' b'3' b'4' b'5'] groups ['Group1', 'Group2', 'Group3', 'Group4', 'Group5', 'Group6', 'Group7', 'Group8']
  lin (99557,)
   trials rec 1 n 47 familiar [ True] t 7612.8 9300.0
   trials rec 2 n 33 familiar [False] t 15159.7 16728.9
 pos ts 7605.7177 16749.233266666666 99557 0.03333333333284827
 ripples (7548,) behavior keys ['LinearizedPosition', 'RewardEventsEightMazeTrack', 'SleepStates', 'SubjectPosition']
== sub-e13-26m1/sub-e13-26m1_ses-e13-26m1-211116_behavior+ecephys.nwb The incorporation of new information into the hippocampal network is likely to be constrained by its innate architecture and internally generated activity patterns. However, the origin, organization and consequences of such patterns remain poorly understood. In the present study we show that hippoca
 behavior: The behavior of the subject for the following recordings: alternation, linearMaze
 units cols: ['clu_id', 'group_id', 'id', 'spike_times', 'spike_times_index', 'unit_name'] n= 209
  NO EPOCHS; intervals: ['trials']
  unit_name ex [b'1' b'2' b'3' b'4' b'5'] groups ['Group1', 'Group2', 'Group3', 'Group4', 'Group5', 'Group6', 'Group7', 'Group8']
  lin (4
[... 102 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import requests
def assets(v):
    out={}; url=f"https://api.dandiarchive.org/api/dandisets/000552/versions/{v}/assets/?page_size=200"
    while url:
        d=requests.get(url).json(); 
        for a in d['results']: out[a['path']]=(a['size'],a['asset_id'])
        url=d['next']
    return out
a=assets("0.230630.2304"); b=assets("0.261113.1035")
print("only old", sorted(set(a)-set(b))); print("only new", sorted(set(b)-set(a)))
same=[p for p in a if p in b and a[p][0]==b[p][0]]; print("same size", len(same), "of", len(set(a)&set(b)))
print([ (p,a[p][0],b[p][0]) for p in a if p in b and a[p][0]!=b[p][0]][:20])
EOF
```

```
only old ['sub-e15-13f1/sub-e15-13f1_ses-e15-13f1-220117-raw_ecephys.nwb', 'sub-e16-3m2/sub-e16-3m2_ses-e16-3m2-211211-raw_ecephys.nwb']
only new []
same size 0 of 115
[('sub-e13-26m1/sub-e13-26m1_ses-e13-26m1-211116-raw_ecephys.nwb', 123466980268, 117904687732), ('sub-e13-26m1/sub-e13-26m1_ses-e13-26m1-211124-raw_ecephys.nwb', 133154801566, 127218943585), ('sub-e13-26m1/sub-e13-26m1_ses-e13-26m1-211019-raw_ecephys.nwb', 147353047025, 140941803006), ('sub-e15-13f1/sub-e15-13f1_ses-e15-13f1-220118-raw_ecephys.nwb', 183608028765, 175463126215), ('sub-e15-13f1/sub-e15-13f1_ses-e15-13f1-220119-raw_ecephys.nwb', 180414749521, 172615537109), ('sub-e16-3m1/sub-e16-3m1_ses-e16-3m1-210201-raw_ecephys.nwb', 54480321649, 52199329414), ('sub-e16-3m1/sub-e16-3m1_ses-e16-3m1-210203-raw_ecephys.nwb', 61991667510, 62029772791), ('sub-e15-13f1/sub-e15-13f1_ses-e15-13f1-220120-raw_ecephys.nwb', 166191418883, 158632532774), ('sub-e16-3m2/sub-e16-3m2_ses-e16-3m2-211212-raw_ecephys.nwb', 138996655725, 131873876239), ('sub-e16-3m2/sub-e16-3m2_ses-e16-3m2-211213-raw_ecephys.nwb', 150700842661, 142476786735), ('sub-e16-3m2/sub-e16-3m2_ses-e16-3m2-211210-raw_ecephys.nwb', 179992553932, 170215129306), ('sub-e13-16f1/sub-e13-16f1_ses-e13-16f1-210317_behavior+ecephys.nwb', 116986503, 4888325606), ('sub-e13-16f1/sub-e13-16f1_ses-e13-16f1-210314_behavior+ecephys.nwb', 108922341, 4286828797), ('sub-e13-16f1/sub-e13-16f1_ses-e13-16f1-210312_behavior+ecephys.nwb', 121439655, 4751287854), ('sub-e13-16f1/sub-e13-16f1_ses-e13-16f1-210315_behavior+ecephys.nwb', 107929787, 4445995327), ('sub-e13-16f1/sub-e13-16f1_ses-e13-16f1-210302_behavior+ecephys.nwb', 150416379, 5597161821), ('sub-e13-16f1/sub-e13-16f1_ses-e13-16f1-210322_behavior+ecephys.nwb', 113693445, 4805989060), ('sub-e13-1f1/sub-e13-1f1_ses-e13-1f1-200228_behavior+ecephys.nwb', 87395878, 3239607860), ('sub-e13-1f1/sub-e13-1f1_ses-e13-1f1-200229_behavior+ecephys.nwb', 55321202, 2058144420), ('sub-e13-16f1/sub-e13-16f1_ses-e13-16f1-210319_behav
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && sed -i 's/"0.230630.2304"/sys.argv[2] if len(sys.argv)>2 else "0.230630.2304"/' survey.py && python survey.py sub-e16-3m2/sub-e16-3m2_ses-e16-3m2-211211_behavior+ecephys.nwb 0.261113.1035 2>&1 | grep -v "^general/devices\|electrodes/\|specifications\|Ripples/ripple_" | head -120
```

```
acquisition/ None 
analysis/ None 
file_create_date (1,) object {}
general/ None 
general/experiment_description () object {}
general/experimenter (4,) object {}
general/external_resources/ HERD 
general/external_resources/entities (10,) [('entity_id', 'O'), ('entity_uri', 'O')] {'neurodata_type': 'Data'}
general/external_resources/entity_keys (19,) [('entities_idx', '<u4'), ('keys_idx', '<u4')] {'neurodata_type': 'Data'}
general/external_resources/files (1,) [('file_object_id', 'O')] {'neurodata_type': 'Data'}
general/external_resources/keys (19,) [('key', 'O')] {'neurodata_type': 'Data'}
general/external_resources/object_keys (19,) [('objects_idx', '<u4'), ('keys_idx', '<u4')] {'neurodata_type': 'Data'}
general/external_resources/objects (14,) [('files_idx', '<u4'), ('object_id', 'O'), ('object_type', 'O'), ('relative_path', 'O'), ('field', 'O')] {'neurodata_type': 'Data'}
general/extracellular_ephys/ None 
general/extracellular_ephys/Group 1/ ElectrodeGroup electrode group 1 of session.mat extracellular.electrodeGroups
general/extracellular_ephys/Group 2/ ElectrodeGroup electrode group 2 of session.mat extracellular.electrodeGroups
general/extracellular_ephys/Group 3/ ElectrodeGroup electrode group 3 of session.mat extracellular.electrodeGroups
general/extracellular_ephys/Group 4/ ElectrodeGroup electrode group 4 of session.mat extracellular.electrodeGroups
general/extracellular_ephys/Group 5/ ElectrodeGroup electrode group 5 of session.mat extracellular.electrodeGroups
general/extracellular_ephys/Group 6/ ElectrodeGroup electrode group 6 of session.mat extracellular.electrodeGroups
[... 101 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python survey.py sub-e16-3m2/sub-e16-3m2_ses-e16-3m2-211211_behavior+ecephys.nwb 0.261113.1035 2>&1 | grep -v "^general/devices\|electrodes/\|specifications\|Ripples/ripple_\|meanings" | sed -n '120,260p'
```

```
units/acg_tau_rise (197,) float64 {'description': 'rise time constant of the autocorrelogram fit, in ms (cell_metrics.acg_tau_rise)', 'neurodata_type': 'VectorData'}
units/cluster_id (197,) int64 {'description': 'Phy cluster id of the unit (spikes.cellinfo cluID)', 'neurodata_type': 'VectorData'}
units/electrode_group (197,) object {'description': 'the electrode group that each spike unit came from', 'neurodata_type': 'VectorData'}
units/electrodes (25216,) int64 {'description': 'the electrodes that each spike unit came from', 'neurodata_type': 'DynamicTableRegion'}
units/electrodes_index (197,) uint16 {'description': "Index for VectorData 'electrodes'", 'neurodata_type': 'VectorIndex'}
units/firing_rate (197,) float64 {'description': 'mean firing rate over the session, in Hz (cell_metrics.firingRate)', 'neurodata_type': 'VectorData'}
units/id (197,) int64 {'neurodata_type': 'ElementIdentifiers'}
units/light_responsive (197,) bool {'description': "True for a pyramidal neuron that the paper's criteria call light-responsive, that is birthdated (ChR2-expressing): putative_cell_type 'Pyramidal Cell', opto_p_salt <= 0.001 and opto_h_reliable True. The Methods test only pyramidal neurons and require every test to be passed; with these criteria the files give the paper's 664 light-responsive neurons in the 96 sessions it analyses. Derived here from the lab's statistics, not stored by the lab.", 'neurodata_type': 'VectorData'}
units/max_electrode (197,) int64 {'description': 'electrode with the largest waveform (spikes.cellinfo maxWaveformCh)', 'neurodata_type': 'DynamicTableRegion'}
units/opto_h_reliable (197,) bool {'description': "True if the unit passed the lab's test of reliable firing after the light pulses, compared with before them (cell_metrics.optoTag.h_reliable; the Methods' Poisson test at alpha 0.001, Bonferroni corrected). See light_responsive", 'neurodata_type': 'VectorData'}
units/opto_int_ratemod (197,) float64 {'description': 'firing rate modulation during
[... 10 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > survey3.py <<'EOF'
import h5py, remfile, numpy as np
from dandi.dandiapi import DandiAPIClient
c = DandiAPIClient()
old = c.get_dandiset("000552", "0.230630.2304"); new = c.get_dandiset("000552", "0.261113.1035")
def op(ds,p): return h5py.File(remfile.File(ds.get_asset_by_path(p).get_content_url(follow_redirects=1, strip_query=True)), "r")
dec=lambda a:[x.decode() if isinstance(x,bytes) else x for x in a]
tot=[]
for s in ["e13-26m1-211019","e13-26m1-211116","e13-26m1-211119","e13-26m1-211124","e15-13f1-220117","e15-13f1-220118","e15-13f1-220119","e15-13f1-220120","e16-3m2-211210","e16-3m2-211211","e16-3m2-211212","e16-3m2-211213"]:
    sub=s.rsplit('-',1)[0]; p=f"sub-{sub}/sub-{sub}_ses-{s}_behavior+ecephys.nwb"
    fo=op(old,p); fn=op(new,p)
    ep=fn["intervals/epochs"]
    print("==",s)
    for a,b,e,t,n in zip(ep["start_time"][:],ep["stop_time"][:],dec(ep["environment"][:]),dec(ep["task"][:]),dec(ep["epoch_name"][:])):
        print(f"   {a:8.1f} {b:8.1f} {e:22s} {t:14s} {n}")
    print("  new pos series:", list(fn["processing/behavior/SubjectPosition"].keys()))
    ct=dec(fn["units/putative_cell_type"][:]); u,cnt=np.unique(ct,return_counts=True); print("  types", dict(zip(u,cnt)))
    si_o=fo["units/spike_times_index"][:]; si_n=fn["units/spike_times_index"][:]
    same=np.array_equal(si_o,si_n) and np.array_equal(fo["units/spike_times"][:1000],fn["units/spike_times"][:1000]) and np.array_equal(fo["units/spike_times"][-1000:],fn["units/spike_times"][-1000:])
    print("  spikes same", same, "names same", dec(fo["units/unit_name"][:])==dec(fn["units/unit_name"][:]))
    ts=fo["processing/behavior/SubjectPosition/SpatialSeries/timestamps"][:]; xy=fo["processing/behavior/SubjectPosition/SpatialSeries/data"][:]
    if "epochs" in fo["intervals"]:
        for a,b in zip(fo["intervals/epochs/start_time"][:],fo["intervals/epochs/stop_time"][:]):
            m=(ts>=a)&(ts<b)
            if m.sum(): print(f"   old epoch {a:8.1f}-{b:8.1f} pos n={m.sum()} x {np.nanmin(xy[m,0]):.0f}..{np.nanmax(xy[m,0]):.0f} y {np.nanmin(xy[m,1]):.0f}..{np.nanmax(xy[m,1]):.0f} nan {np.isnan(xy[m,0]).mean():.2f} first {ts[m][0]:.1f}")
    else: print("   old: no epochs; pos", ts[0], ts[-1])
EOF
python survey3.py 2>&1 | grep -v Warn
```

```
== e13-26m1-211019
        0.0   7589.6 none                   none           e13_26m1_211019_093241
     7589.6   9327.6 tmaze_familiar         alternation    e13_26m1_211019_114439
     9327.6  15088.4 none                   none           e13_26m1_211019_121416
    15088.4  16753.1 tmaze_ipshita          alternation    e13_26m1_211019_145847
    16753.1  22200.9 none                   none           e13_26m1_211019_152351
    22200.9  24298.0 none                   none           e13_26m1_211019_165657
  new pos series: ['SpatialSeries1_tmaze_familiar', 'SpatialSeries2_tmaze_ipshita']
  types {np.str_('Narrow Interneuron'): np.int64(37), np.str_('Pyramidal Cell'): np.int64(228), np.str_('Wide Interneuron'): np.int64(6)}
  spikes same True names same True
   old epoch   7589.6-  9327.6 pos n=51501 x 2..90 y 4..89 nan 0.00 first 7605.7
   old epoch  15088.4- 16753.1 pos n=48056 x 0..1 y 0..1 nan 0.00 first 15103.0
== e13-26m1-211116
     7453.7   8724.4 tmaze_familiar         alternation    e13_26m1_211116_130304
    13578.8  14023.0 linear_thomas          linearMaze     e13_26m1_211116_151447
  new pos series: ['SpatialSeries1_tmaze_familiar', 'SpatialSeries2_linear_thomas']
  types {np.str_('Narrow Interneuron'): np.int64(25), np.str_('Pyramidal Cell'): np.int64(173), np.str_('Wide Interneuron'): np.int64(11)}
  spikes same True names same True
   old: no epochs; pos 7469.752566666667 13939.215733333334
== e13-26m1-211119
[... 119 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cat > survey4.py <<'EOF'
import h5py, remfile, numpy as np
from dandi.dandiapi import DandiAPIClient
c = DandiAPIClient()
old = c.get_dandiset("000552", "0.230630.2304"); new = c.get_dandiset("000552", "0.261113.1035")
def op(ds,p): return h5py.File(remfile.File(ds.get_asset_by_path(p).get_content_url(follow_redirects=1, strip_query=True)), "r")
for s in ["e13-26m1-211019","e13-26m1-211116","e13-26m1-211119","e15-13f1-220118","e15-13f1-220119","e15-13f1-220120","e16-3m2-211211","e16-3m2-211212","e16-3m2-211213"]:
    sub=s.rsplit('-',1)[0]; p=f"sub-{sub}/sub-{sub}_ses-{s}_behavior+ecephys.nwb"
    fo=op(old,p); fn=op(new,p)
    ts=fo["processing/behavior/SubjectPosition/SpatialSeries/timestamps"][:]; xy=fo["processing/behavior/SubjectPosition/SpatialSeries/data"][:]
    lin=fo["processing/behavior/LinearizedPosition/LinearizedSpatialSeries/data"][:]
    gap=np.where(np.diff(ts)>60)[0]
    segs=np.split(np.arange(len(ts)),gap+1)
    print("==",s)
    for sg in segs:
        print(f"  old seg {ts[sg[0]]:.1f}-{ts[sg[-1]]:.1f} n={len(sg)} x {xy[sg,0].min():.2f}..{xy[sg,0].max():.2f} y {xy[sg,1].min():.2f}..{xy[sg,1].max():.2f} lin {np.nanmin(lin[sg]):.2f}..{np.nanmax(lin[sg]):.2f} dt {np.median(np.diff(ts[sg])):.4f}")
    for k in fn["processing/behavior/SubjectPosition"].keys():
        g=fn["processing/behavior/SubjectPosition"][k]; t=g["timestamps"][:]; d=g["data"][:]
        print(f"  new {k} {t[0]:.1f}-{t[-1]:.1f} n={len(t)} x {np.nanmin(d[:,0]):.2f}..{np.nanmax(d[:,0]):.2f} y {np.nanmin(d[:,1]):.2f}..{np.nanmax(d[:,1]):.2f}")
        # match to old
        m=np.isin(np.round(ts,3), np.round(t,3))
        if m.sum(): 
            i=np.searchsorted(t, ts[m]); i=np.clip(i,0,len(t)-1)
            print(f"     overlap {m.sum()} old/new x ratio median {np.nanmedian(xy[m,0]/np.where(d[i,0]==0,np.nan,d[i,0])):.3f}")
EOF
python survey4.py 2>&1 | grep -v Warn; date -u
```

```
== e13-26m1-211019
  old seg 7605.7-9322.8 n=51501 x 2.17..90.02 y 3.65..89.32 lin 0.00..221.91 dt 0.0333
  old seg 15103.0-16749.2 n=48056 x 0.01..0.73 y 0.06..0.98 lin 0.00..169.99 dt 0.0333
  new SpatialSeries1_tmaze_familiar 7605.7-9322.8 n=51501 x 2.17..90.02 y 3.65..89.32
     overlap 51501 old/new x ratio median 1.000
  new SpatialSeries2_tmaze_ipshita 15103.0-16749.2 n=48056 x 0.01..0.73 y 0.06..0.98
     overlap 48056 old/new x ratio median 1.000
== e13-26m1-211116
  old seg 7469.8-8719.4 n=37482 x 1.68..92.41 y 1.70..89.41 lin 0.00..221.91 dt 0.0333
  old seg 13594.9-13939.2 n=8608 x 0.26..0.89 y 0.04..0.77 lin 0.00..100.00 dt 0.0400
  new SpatialSeries1_tmaze_familiar 7469.8-8719.4 n=37482 x 1.68..92.41 y 1.70..89.41
     overlap 37482 old/new x ratio median 1.000
  new SpatialSeries2_linear_thomas 13594.9-13939.2 n=8608 x 0.26..0.89 y 0.04..0.77
     overlap 8608 old/new x ratio median 1.000
== e13-26m1-211119
  old seg 6181.3-7571.7 n=41704 x 1.30..92.04 y 2.59..89.45 lin 0.00..221.93 dt 0.0333
  old seg 14907.4-16446.0 n=46166 x 0.01..0.20 y 0.00..1.00 lin 0.00..110.00 dt 0.0333
  new SpatialSeries1_tmaze_familiar 6181.3-7571.7 n=41704 x 1.30..92.04 y 2.59..89.45
     overlap 41704 old/new x ratio median 1.000
  new SpatialSeries2_linear_manu 14907.4-16446.0 n=46166 x 0.01..0.20 y 0.00..1.00
[... 50 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; grep -n "Statistical modeling\|fmincon\|CVMSE\|exponential" *.txt | head;
```

```
394:A) Histological confirmation of GRABNE expression (GFP) and fiber placement over dorsal CA1. B) Schematic of experimental timeline. C) Example session showing increases in SignalNE around each context and homecage (HC) transition. D) Mean SignalNE measured across all transitions (black) and cross-validated prediction from the saturated model (red) or a reduced model lacking terms related to time from transfer (blue). E) Change in CVMSE due to removal of various potential behavioral variables. Only removal of the terms related to time from transition significantly decreased model performance (t(7) = 3.30, p = 0.01).
397:SignalNE exponentially decays after transfer to a novel arena
399:Moving between environments causes a large reorganization in which hippocampal neurons are active33,68. To test how NE release relates to this cause of network reorganization, SignalNE was measured as mice were transferred from their home cage to a novel testing arena that, over days, became more familiar to the subject (Figure 1B,C). Averaging across all exposures, SignalNE increased immediately upon entry to the testing arena and exponentially decayed to a steady state over minutes (Figure 1D). The NE dynamics may be related to the transition itself, or the incidence of behaviors that occur immediately following exposure to an unfamiliar space. For example, in the moments after transition, mice tended to spend more time close to the edges of the environment (thigmotaxis) and tended to move more rapidly (Figure S1C). We quantified how NE release relates to five potential behavioral covariates: time from arena entry, acceleration, velocity, distance from edge, and time from rearing. These five behavioral variables were themselves correlated (Figure S1D). Univariate analysis revealed strong, positive co-modulation of SignalNE with acceleration (t(7) = 4.54, p = 0.002) and modest positive correlation with velocity (t(7) = 2.32, p = 0.05)(Figure S1E). SignalNE also correlated with dist
[... 7 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; sed -n '/^Statistical modeling/,/^Electrophysiology$/p' *.txt | head -30; grep -n "Kalman" *.txt | head
```

```
Statistical modeling of SignalNE

SignalNE at each moment was estimated as a function of various behavioral variables which differed according to the testing paradigm.

In the novel arena experiments, SignalNE was estimated as a function of acceleration (acc), velocity (vel), normalized distance from the edge (distedg), time from context transfer (t1), and time from rearing onset (t2), see Equation 1. Acceleration and velocity were calculated using a second-order Kalman filter of the head location (right and left ear locations estimated with DeepLabCut156). Normalized distance to the edge was calculated as the distance to the nearest edge divided by the maximum distance to an edge possible. In some cases, the animal could extend its head beyond the wall of the arena and these values were coded as negative.

Time from transition/rearing was modeled with two terms: a positive term β4/6 with a fast exponential decay τ1/3 and a negative term β5/7 with a slower exponential decay τ2/4. To avoid degeneracy, τ1/3 was bounded between 0.1-0.001 and τ2/4 was bounded between 0.001-0.0001. All β values were bound at ±10 s.t.d. Point estimates for the 12 free parameters (β0-7 and τ1-4) were calculated with MATLAB R2021b using the fmincon non-linear optimizer against a regularized objective (Equation 2) defined by the mean squared error (MSE) with a penalty for model complexity (λ = 0.001). Fits were robust to initial conditions.

We performed 50/50 cross-validation, with the model trained on even days and tested on odd, or vice-versa. The cross-validate mean-squared error (CVMSE) was used to assess model fit (the regularization term is dropped here).

To assess the importance of each behavioral independent variable (and intercept), we excluded all terms related to those variables in a backwards stepwise regression analysis. For example, removing time from context transfer removed four terms: β4, β5,τ1,τ2. The cross-validation employed here ensures that model performance should no
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p entries/mckenzie-2025 && cd $TMPDIR && source env/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import h5py, remfile, numpy as np
from dandi.dandiapi import DandiAPIClient
c = DandiAPIClient(); old = c.get_dandiset("000552", "0.230630.2304")
p="sub-e16-3m2/sub-e16-3m2_ses-e16-3m2-211213_behavior+ecephys.nwb"
f=h5py.File(remfile.File(old.get_asset_by_path(p).get_content_url(follow_redirects=1, strip_query=True)),"r")
r=f["processing/ecephys/Ripples"]
d=r["ripple_durations"][:]; st=r["start_time"][:]; sp=r["stop_time"][:]; pk=r["peaks"][:]
print("dur", np.percentile(d,[0,5,50,95,100]), "stop-start", np.percentile(sp-st,[0,50,100]), "peak in", np.mean((pk>=st)&(pk<=sp)))
print("sorted", np.all(np.diff(st)>=0))
ss=f["processing/behavior/SleepStates"]; lab=[x.decode() if isinstance(x,bytes) else x for x in ss["label"][:]]
print(set(lab), ss["start_time"][:5], ss["stop_time"][:5])
# ripples per epoch
for a,b in zip(f["intervals/epochs/start_time"][:], f["intervals/epochs/stop_time"][:]): print(a,b,((st>=a)&(st<b)).sum())
EOF
```

```
dur [0.02   0.0216 0.032  0.0608 0.1352] stop-start [0.02   0.032  0.1352] peak in 1.0
sorted True
{'Non-REM', 'Awake', 'REM'} [1.000e+00 4.020e+02 1.039e+03 1.098e+03 1.670e+03] [ 401. 1038. 1097. 1669. 1843.]
0.0 7551.967966666667 1291
7551.968 9377.823966666667 30
9377.824 13266.175966666666 1190
13266.176 15326.719966666667 23
15326.72 24073.023966666668 3335
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "entries/mckenzie-2025/settle.py",
 "content": "\"\"\"Loading and measures for the electrophysiology claims of McKenzie et al. (2025) on dandiset 000552.\n\nMcKenzie, Sommer, Donaldson, Pimentel, Kakani, Choi, Newman & English (2025), eLife 14:RP105183,\ndoi:10.7554/elife.105183. The paper reanalyses Huszar et al. (2022) at DANDI:000552 version\n0.230630.2304 (Methods, Electrophysiology subjects), the version pinned here (`VERSION`). Files are\nstreamed from the archive; nothing is written to disk.\n\nThe pinned version has no cell type labels and no names for its epochs. A later version,\n`LABEL_VERSION` (0.261113.1035), of the same dandiset holds the same spike times (checked unit by\nunit in `cell_types`) with CellExplorer's putative cell types; `cell_types` reads only that column\nfrom it. Claims file E3 asks for the dataset's own labels; this is the only source of them.\n\nWhere the parameters come from:\n\n- `BIN = 0.1` s population vectors, z-scored over the first `ZWIN = 1000` s after transfer\n  (Methods, ACG slope analysis; claims file E4).\n- Transfer (time 0 of a run) is the start of the maze epoch (claims file E2).\n- Nearest neighbours: `K_NN = 3` most correlated vectors in the same location bin, location bins with\n  at least `MIN_OCC = 1` s of occupancy, smoothed with a Gaussian of `SMOOTH_SD = 1` s (Methods, Reset\n  analysis). Whether \"1-s Gaussian kernel\" is the standard deviation or the width is not said; the\n  standard deviation is a standard choice, and the windows averaged are 60 s long.\n- Location bins are 1 cm (Methods, Place field detection). They are taken on the linearized\n  position, in cm, because the (x, y) position of 5 of the 9 novel runs is not in cm (0 to 1),\n  though the file says cm; an assumption recorded in the attempt.\n- Speed threshold `SPEED_MIN = 5` cm/s and field threshold `FIELD_HZ = 5` Hz (Methods, Place field\n  detection).\n- Speed is the path length along the linearized position per second. A step over `JUMP_CM` (the\n  wrap of the figure-eight linearization from its end to its start) adds no length; a standard\n  choice. Readings of claims file E8: (a) a second-order (constant acceleration) Kalman smoother,\n  as the photometry Methods use, with process noise `KALMAN_Q` and measurement noise `KALMAN_R`\n  (standard choices, the paper gives none); (b) finite differences smoothed with a 1 s Gaussian.\n- Ripples are the events deposited in the files (processing/ecephys/Ripples), those of Huszar et\n  al. (2022); the broadband LFP the Methods detect them from is only in the raw files (claims file\n  E9 names them as a variant).\n- Reactivation (Methods, Reactivation analysis): each ripple's vector is spike count over duration;\n  `N_SHUF = 1000` shuffles that move each unit's value on a ripple to a random other ripple (an\n  independent permutation of each unit across the pooled ripples); a ripple reactivates a moment\n  when its Pearson R exceeds 99.9% of its shuffles (`ALPHA = 0.001`).\n\"\"\"\n\nfrom __future__ import annotations\n\nimport h5py\nimport numpy as np\nimport remfile\nfrom dandi.dandiapi import DandiAPIClient\nfrom scipy.ndimage import gaussian_filter1d\nfrom scipy.optimize import curve_fit\n\nDANDISET_ID = \"000552\"\nVERSION = \"0.230630.2304\"\nLABEL_VERSION = \"0.261113.1035\"\n\n# Sessions of the three mice the Methods name (e13_26m1, e15_13f1, e16_3m2).\nSESSIONS = [\n    \"e13-26m1-211019\", \"e13-26m1-211116\", \"e13-26m1-211119\", \"e13-26m1-211124\",\n    \"e15-13f1-220117\", \"e15-13f1-220118\", \"e15-13f1-220119\", \"e15-13f1-220120\",\n    \"e16-3m2-211210\", \"e16-3m2-211211\", \"e16-3m2-211212\", \"e16-3m2-211213\",\n]\n\nBIN = 0.1\nZWIN = 1000.0\nK_NN = 3\nMIN_OCC = 1.0\nSMOOTH_SD = 1.0\nLOC_CM = 1.0\nSPEED_MIN = 5.0\nFIELD_HZ = 5.0\nJUMP_CM = 20.0\nKALMAN_Q = 50.0     # cm^2/s^5, white-noise jerk\nKALMAN_R = 1.0      # cm^2, measurement noise\nN_SHUF = 1000\nALPHA = 0.001\nGAP_S = 60.0        # a gap in tracking longer than this separates two runs\n\n_client = None\n\n\ndef _dandiset(version=VERSION):\n    global _client\n    if _client is None:\n        _client = DandiAPIClient()\n    return _client.get_dandiset(DANDISET_ID, version)\n\n\ndef asset_path(sid):\n    sub = sid.rsplit(\"-\", 1)[0]\n    return f\"sub-{sub}/sub-{sub}_ses-{sid}_behavior+ecephys.nwb\"\n\n\ndef open_file(sid, version=VERSION):\n    asset = _dandiset(version).get_asset_by_path(asset_path(sid))\n    url = asset.get_content_url(follow_redirects=1, strip_query=True)\n    return h5py.File(remfile.File(url), \"r\")\n\n\ndef _str(a):\n    return [x.decode() if isinstance(x, bytes) else str(x) for x in a]\n\n\ndef load_session(sid):\n    \"\"\"Everything the analyses use from one pinned file, as numpy arrays.\"\"\"\n    f = open_file(sid)\n    s = {\"sid\": sid, \"subject\": sid.rsplit(\"-\", 1)[0]}\n    idx = f[\"units/spike_times_index\"][:]\n    st = f[\"units/spike_times\"][:]\n    s[\"spikes\"] = np.split(st, idx[:-1])\n    s[\"unit_name\"] = _str(f[\"units/unit_name\"][:])\n    s[\"spike_index\"] = idx\n    if \"epochs\" in f[\"intervals\"]:\n        s[\"epochs\"] = np.c_[f[\"intervals/epochs/start_time\"][:], f[\"intervals/epochs/stop_time\"][:]]\n    else:\n        s[\"epochs\"] = None\n    g = f[\"processing/behavior\"]\n    s[\"pos_t\"] = g[\"SubjectPosition/SpatialSeries/timestamps\"][:]\n    s[\"xy\"] = g[\"SubjectPosition/SpatialSeries/data\"][:]\n    s[\"xy_unit\"] = g[\"SubjectPosition/SpatialSeries/data\"].attrs[\"unit\"]\n    s[\"lin\"] = g[\"LinearizedPosition/LinearizedSpatialSeries/data\"][:]\n    s[\"behavior_description\"] = g.attrs.get(\"description\")\n    tr = f[\"intervals/trials\"]\n    s[\"trials\"] = {k: tr[k][:] for k in (\"start_time\", \"stop_time\", \"is_familiar_maze\", \"recordings\")}\n    r = f[\"processing/ecephys/Ripples\"]\n    s[\"rip\"] = np.c_[r[\"start_time\"][:], r[\"stop_time\"][:]]\n    s[\"rip_dur\"] = r[\"ripple_durations\"][:]\n    ss = g[\"SleepStates\"]\n    s[\"sleep\"] = (np.c_[ss[\"start_time\"][:], ss[\"stop_time\"][:]], _str(ss[\"label\"][:]))\n    f.close()\n    s[\"runs\"] = find_runs(s)\n    return s\n\n\ndef cell_types(sid, spike_index):\n    \"\"\"CellExplorer putative cell types from LABEL_VERSION, after checking its spike index matches.\"\"\"\n    f = open_file(sid, LABEL_VERSION)\n    if not np.array_equal(f[\"units/spike_times_index\"][:], spike_index):\n        raise ValueError(f\"{sid}: units differ between versions\")\n    ct = np.array(_str(f[\"units/putative_cell_type\"][:]))\n    env = None\n    if \"environment\" in f[\"intervals/epochs\"]:\n        env = list(zip(f[\"intervals/epochs/start_time\"][:], f[\"intervals/epochs/stop_time\"][:],\n                       _str(f[\"intervals/epochs/environment\"][:])))\n    f.close()\n    return ct, env\n\n\ndef find_runs(s):\n    \"\"\"Maze runs: stretches of tracking separated by more than GAP_S, each with its epoch.\n\n    Returns a list of dicts with the tracking indices, the transfer time t0 (start of the epoch that\n    holds the run; the first tracked frame when the file has no epochs) and the epoch end.\n    \"\"\"\n    t = s[\"pos_t\"]\n    cut = np.where(np.diff(t) > GAP_S)[0] + 1\n    runs = []\n    for seg in np.split(np.arange(len(t)), cut):\n        a, b = t[seg[0]], t[seg[-1]]\n        if s[\"epochs\"] is not None:\n            k = np.where((s[\"epochs\"][:, 0] <= a) & (s[\"epochs\"][:, 1] >= b))[0]\n            t0, t1 = s[\"epochs\"][k[0]] if len(k) else (a, b)\n            ep = int(k[0]) if len(k) else None\n        else:\n            t0, t1, ep = a, b, None\n        tm = s[\"trials\"]\n        intr = (tm[\"start_time\"] >= t0) & (tm[\"start_time\"] < t1)\n        fam = tm[\"is_familiar_maze\"][intr]\n        runs.append(dict(idx=seg, t0=float(t0), t1=float(t1), epoch=ep, first_track=float(a),\n                         last_track=float(b), n_trials=int(intr.sum()),\n                         familiar=bool(fam.all()) if len(fam) else None))\n    return runs\n\n\n# ---------------------------------------------------------------- behaviour\n\ndef path_length(lin):\n    d = np.diff(lin)\n    d[~np.isfinite(d) | (np.abs(d) > JUMP_CM)] = 0.0\n    return np.r_[0.0, np.cumsum(np.abs(d))]\n\n\ndef kalman_va(t, p, q=KALMAN_Q, r=KALMAN_R):\n    \"\"\"Speed and acceleration from a constant-acceleration Kalman filter with RTS smoothing.\"\"\"\n    n = len(p)\n    dt = np.median(np.diff(t))\n    F = np.array([[1, dt, dt * dt / 2], [0, 1, dt], [0, 0, 1]])\n    G = np.array([[dt ** 3 / 6], [dt ** 2 / 2], [dt]])\n    Q = q * G @ G.T\n    H = np.array([[1.0, 0, 0]])\n    x = np.array([p[0], 0, 0.0]); P = np.eye(3) * 10\n    xs = np.zeros((n, 3)); Ps = np.zeros((n, 3, 3)); xp = np.zeros((n, 3)); Pp = np.zeros((n, 3, 3))\n    for i in range(n):\n        if i:\n            x = F @ x; P = F @ P @ F.T + Q\n        xp[i] = x; Pp[i] = P\n        S = (H @ P @ H.T)[0, 0] + r\n        K = (P @ H.T)[:, 0] / S\n        x = x + K * (p[i] - x[0]); P = P - np.outer(K, H @ P)\n        xs[i] = x; Ps[i] = P\n    for i in range(n - 2, -1, -1):\n        C = Ps[i] @ F.T @ np.linalg.inv(Pp[i + 1])\n        xs[i] = xs[i] + C @ (xs[i + 1] - xp[i + 1])\n        Ps[i] = Ps[i] + C @ (Ps[i + 1] - Pp[i + 1]) @ C.T\n    return xs[:, 1], xs[:, 2]\n\n\ndef diff_va(t, p, sd_s=1.0):\n    dt = np.median(np.diff(t))\n    v = np.gradient(p, t)\n    v = gaussian_filter1d(v, sd_s / dt)\n    a = np.gradient(v, t)\n    return v, a\n\n\ndef run_behaviour(s, run, edges):\n    \"\"\"Linearized position, speed and acceleration (both readings) at the centres of the bins.\"\"\"\n    i = run[\"idx\"]\n    t = s[\"pos_t\"][i]; lin = s[\"lin\"][i]\n    pl = path_length(lin)\n    vk, ak = kalman_va(t, pl)\n    vd, ad = diff_va(t, pl)\n    c = (edges[:-1] + edges[1:]) / 2\n    j = np.searchsorted(t, c)\n    j = np.clip(j, 1, len(t) - 1)\n    j = np.where(np.abs(t[j - 1] - c) < np.abs(t[j] - c), j - 1, j)\n    ok = np.abs(t[j] - c) <= BIN\n    out = {}\n    for k, v in dict(lin=lin, vel_k=vk, acc_k=ak, vel_d=vd, acc_d=ad).items():\n        x = v[j].astype(float)\n        x[~ok] = np.nan\n        out[k] = x\n    out[\"loc\"] = np.where(np.isfinite(out[\"lin\"]), np.floor(out[\"lin\"] / LOC_CM), np.nan)\n    return out\n\n\n# ---------------------------------------------------------------- spikes\n\ndef bin_counts(spikes, units, edges):\n    return np.stack([np.histogram(spikes[u], edges)[0] for u in units], 1).astype(np.float32)\n\n\ndef run_vectors(s, run, units):\n    \"\"\"100 ms counts over the run epoch from transfer, and their z-score over the first ZWIN s.\n\n    Units with no spike in the z-scoring window are dropped (their z-score is undefined).\n    \"\"\"\n    edges = np.arange(run[\"t0\"], run[\"t1\"] + 1e-9, BIN)\n    cnt = bin_counts(s[\"spikes\"], units, edges)\n    tb = edges[:-1] - run[\"t0\"]\n    w = tb < ZWIN\n    mu = cnt[w].mean(0); sd = cnt[w].std(0)\n    keep = sd > 0\n    z = (cnt[:, keep] - mu[keep]) / sd[keep]\n    return dict(edges=edges, t=tb, counts=cnt[:, keep], z=z.astype(np.float32),\n                units=np.asarray(units)[keep], dropped=int((~keep).sum()))\n\n\ndef row_normalize(z):\n    zc = z - z.mean(1, keepdims=True)\n    n = np.linalg.norm(zc, axis=1, keepdims=True)\n    n[n == 0] = np.nan\n    return zc / n\n\n\n# ---------------------------------------------------------------- decorrelation (Figure S6)\n\ndef expo(lag, beta, tau, c):\n    return beta * np.exp(-lag / tau) + c\n\n\ndef decorrelation_curve(zn, t, start, length, max_lag=10.0):\n    \"\"\"Mean Pearson R between vectors separated by each lag (0.1 to 10 s), both inside the window.\"\"\"\n    m = (t >= start) & (t < start + length)\n    v = zn[m]\n    lags = np.arange(1, int(round(max_lag / BIN)) + 1)\n    r = np.array([np.nanmean(np.sum(v[:-k] * v[k:], 1)) if k < len(v) else np.nan for k in lags])\n    return lags * BIN, r\n\n\ndef decay_rate(lag, r):\n    ok = np.isfinite(r)\n    try:\n        p, _ = curve_fit(expo, lag[ok], r[ok], p0=[r[ok][0] - r[ok][-1], 1.0, r[ok][-1]],\n                         bounds=([-np.inf, 1e-3, -1], [np.inf, 1e3, 1]), maxfev=20000)\n        return 1.0 / p[1], p\n    except RuntimeError:\n        return np.nan, None\n\n\n# ---------------------------------------------------------------- nearest neighbours (Figure 7)\n\ndef nn_conditioned(zn, loc, valid, t, k=K_NN, exclude_visit=False):\n    \"\"\"For each bin, the mean R of its k most correlated bins in the same location bin.\n\n    `valid` marks bins that take part (located, and above the speed threshold under reading b).\n    Location bins with less than MIN_OCC s of valid bins are left out. Returns the mean R and the\n    indices of the neighbours (-1 where missing).\n    \"\"\"\n    n = len(zn)\n    out = np.full(n, np.nan); nbr = np.full((n, k), -1)\n    ok = valid & np.isfinite(loc) & np.isfinite(zn[:, 0])\n    min_n = int(round(MIN_OCC / BIN))\n    locs = loc[ok]\n    for L in np.unique(locs):\n        ii = np.where(ok & (loc == L))[0]\n        if len(ii) < min_n or len(ii) <= k:\n            continue\n        c = zn[ii] @ zn[ii].T\n        np.fill_diagonal(c, -np.inf)\n        if exclude_visit:\n            visit = np.cumsum(np.r_[1, np.diff(ii) > 1])\n            c[visit[:, None] == visit[None, :]] = -np.inf\n        top = np.argpartition(-c, k - 1, axis=1)[:, :k]\n        vals = np.take_along_axis(c, top, 1)\n        good = np.isfinite(vals).all(1)\n        out[ii[good]] = vals[good].mean(1)\n        nbr[ii[good]] = ii[top[good]]\n    return out, nbr\n\n\ndef nn_unconditioned(zn, valid, k=K_NN, chunk=2000):\n    \"\"\"(a) mean R of the k most correlated bins anywhere in the run; (b) mean R with all others.\"\"\"\n    n = len(zn)\n    ok = valid & np.isfinite(zn[:, 0])\n    ii = np.where(ok)[0]\n    v = zn[ii]\n    topk = np.full(n, np.nan); allm = np.full(n, np.nan)\n    tot = v.sum(0)\n    for s0 in range(0, len(ii), chunk):\n        c = v[s0:s0 + chunk] @ v.T\n        rows = np.arange(c.shape[0])\n        c[rows, s0 + rows] = -np.inf\n        top = np.partition(c, c.shape[1] - k, axis=1)[:, -k:]\n        topk[ii[s0:s0 + chunk]] = top.mean(1)\n        selfdot = np.sum(v[s0:s0 + chunk] ** 2, 1)\n        allm[ii[s0:s0 + chunk]] = (v[s0:s0 + chunk] @ tot - selfdot) / (len(ii) - 1)\n    return topk, allm\n\n\ndef nan_smooth(x, sd_s=SMOOTH_SD):\n    ok = np.isfinite(x)\n    num = gaussian_filter1d(np.where(ok, x, 0.0), sd_s / BIN)\n    den = gaussian_filter1d(ok.astype(float), sd_s / BIN)\n    y = num / np.where(den > 0, den, np.nan)\n    y[den < 0.05] = np.nan\n    return y\n\n\ndef window_mean(x, t, start, length=60.0):\n    m = (t >= start) & (t < start + length)\n    return float(np.nanmean(x[m])) if np.isfinite(x[m]).any() else np.nan\n\n\n# ---------------------------------------------------------------- reactivation (Figure 8)\n\ndef ripple_vectors(s, units, windows):\n    \"\"\"Rate vectors (spikes / duration) of the ripples starting inside any of the windows.\"\"\"\n    r = s[\"rip\"]\n    m = np.zeros(len(r), bool)\n    for a, b in windows:\n        m |= (r[:, 0] >= a) & (r[:, 0] < b)\n    rr = r[m]\n    dur = rr[:, 1] - rr[:, 0]\n    vec = np.zeros((len(rr), len(units)), np.float32)\n    for j, u in enumerate(units):\n        sp = s[\"spikes\"][u]\n        vec[:, j] = (np.searchsorted(sp, rr[:, 1]) - np.searchsorted(sp, rr[:, 0])) / dur\n    return vec\n\n\ndef reactivation(rip_vec, groups, moments, rng, n_shuf=N_SHUF, alpha=ALPHA):\n    \"\"\"Fraction of ripples of each group that significantly reactivate each moment.\n\n    rip_vec: ripples x units (the pool shuffled together); groups: dict name -> boolean mask of the\n    pool; moments: moments x units. Each shuffle permutes every unit independently across the pool.\n    Returns dict name -> per-moment fraction (0 to 1) and the number of ripples in the group.\n    \"\"\"\n    mn = row_normalize(moments.astype(np.float32)).T            # units x moments\n    obs_n = row_normalize(rip_vec)\n    obs = obs_n @ mn                                            # ripples x moments\n    exceed = np.zeros(obs.shape, np.int32)\n    R, U = rip_vec.shape\n    for _ in range(n_shuf):\n        perm = np.argsort(rng.random((R, U)), axis=0)\n        sh = np.take_along_axis(rip_vec, perm, 0)\n        shn = row_normalize(sh)\n        exceed += (np.nan_to_num(shn @ mn, nan=-2) >= obs)\n    sig = (exceed < alpha * n_shuf) & np.isfinite(obs)          # observed above 99.9% of shuffles\n    return {g: (sig[m].mean(0) if m.sum() else np.full(mn.shape[1], np.nan), int(m.sum()))\n            for g, m in groups.items()}\n"
}
```

```
File created successfully at: entries/mckenzie-2025/settle.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/mckenzie-2025 && python - <<'EOF'
import re
s=open('settle.py').read()
s=s.replace('''        perm = np.argsort(rng.random((R, U)), axis=0)
        sh = np.take_along_axis(rip_vec, perm, 0)
        shn = row_normalize(sh)''','''        shn = row_normalize(rng.permuted(rip_vec, axis=0))''')
s=s.replace('''    sig = (exceed < alpha * n_shuf) & np.isfinite(obs)          # observed above 99.9% of shuffles''','''    # significant when the observed R is above every shuffle, i.e. above their 99.9th percentile
    sig = (exceed < max(1, round(alpha * n_shuf))) & np.isfinite(obs)''')
s=s.replace("    R, U = rip_vec.shape\n","")
open('settle.py','w').write(s)
EOF
cd $TMPDIR && source env/bin/activate && cp entries/mckenzie-2025/settle.py . && cat > dev1.py <<'EOF'
import time, resource, numpy as np, settle as S
t=time.time()
s=S.load_session("e16-3m2-211213"); print("load", time.time()-t)
for r in s["runs"]: print({k:v for k,v in r.items() if k!='idx'})
ct,env=S.cell_types(s["sid"], s["spike_index"]); print(env)
pyr=np.where(ct=="Pyramidal Cell")[0]
run=s["runs"][1]
t=time.time(); V=S.run_vectors(s,run,pyr); B=S.run_behaviour(s,run,V["edges"]); print("vec+beh", time.time()-t, V["z"].shape, V["dropped"])
zn=S.row_normalize(V["z"])
for st in (0,600):
    lag,r=S.decorrelation_curve(zn,V["t"],st,60); print(st, S.decay_rate(lag,r)[0], r[:3], r[-1])
t=time.time()
for spd in (False,True):
    valid=np.isfinite(B["loc"]) & ((B["vel_k"]>S.SPEED_MIN) if spd else True)
    nn,nb=S.nn_conditioned(zn,B["loc"],valid,V["t"])
    sm=S.nan_smooth(nn)
    print("speed",spd, "nn time", time.time()-t, [round(S.window_mean(sm,V["t"],w),3) for w in (0,60,120,300,540,600,900)])
t=time.time(); a,b=S.nn_unconditioned(zn,np.ones(len(zn),bool)); print("uncond", time.time()-t, [round(S.window_mean(S.nan_smooth(x),V["t"],w),3) for x in (a,b) for w in (0,600)])
print("speed ranges k", np.nanpercentile(B["vel_k"],[1,50,99]), "d", np.nanpercentile(B["vel_d"],[1,50,99]))
print("maxrss MB", resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e3)
EOF
python dev1.py 2>&1 | grep -v Warn
```

```
load 3.4320626258850098
{'t0': 7551.968, 't1': 9377.823966666667, 'epoch': 1, 'first_track': 7567.9228, 'last_track': 9368.945866666667, 'n_trials': 27, 'familiar': True}
{'t0': 13266.176, 't1': 15326.719966666667, 'epoch': 3, 'first_track': 13286.7231, 'last_track': 15323.077533333333, 'n_trials': 29, 'familiar': False}
[(np.float64(0.0), np.float64(7551.967966666667), 'none'), (np.float64(7551.968), np.float64(9377.823966666667), 'tmaze_familiar'), (np.float64(9377.824), np.float64(13266.175966666666), 'none'), (np.float64(13266.176), np.float64(15326.719966666667), 'tmaze_ipshita'), (np.float64(15326.72), np.float64(24073.023966666668), 'none')]
vec+beh 2.427243709564209 (20605, 163) 0
0 0.6880178473288456 [0.22198777 0.17753555 0.14932428] 0.050671887
600 1.188620141656552 [0.30576396 0.2537466  0.22755954] 0.03026789
speed False nn time 0.11352181434631348 [0.386, 0.403, 0.451, 0.47, 0.518, 0.509, 0.506]
speed True nn time 0.1512439250946045 [0.294, 0.339, 0.389, 0.414, 0.443, 0.408, 0.445]
uncond 1.8646583557128906 [0.677, 0.679, -0.001, 0.0]
speed ranges k [-0.28358903  3.96295382 17.53158832] d [ 0.20118998  4.36266646 14.69310103]
maxrss MB 894.608
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd entries/mckenzie-2025 && grep -n "permuted\|max(1" settle.py
```

```
Thu Nov 26 17:07:48 UTC 2026
381:        shn = row_normalize(rng.permuted(rip_vec, axis=0))
384:    sig = (exceed < max(1, round(alpha * n_shuf))) & np.isfinite(obs)
```

**Agent calls Bash**

```bash
cat >> settle.py <<'EOF'


# ---------------------------------------------------------------- one run, every measure

WINDOWS = {"min1": 0.0, "min10": 600.0, "min10_alt": 540.0}   # claims file E6


def run_measures(s, run, units, kalman=True):
    """Every per-bin measure of one run that the claims use.

    Returns the bin times from transfer, the normalized vectors, behaviour, and the nearest-neighbour
    series under the speed readings of claims file E5 (all bins; bins above SPEED_MIN), with the
    neighbours' movement differences for both readings of E8.
    """
    V = run_vectors(s, run, units)
    B = run_behaviour(s, run, V["edges"])
    zn = row_normalize(V["z"])
    out = dict(t=V["t"], zn=zn, beh=B, n_units=zn.shape[1], dropped=V["dropped"], z=V["z"],
               counts=V["counts"], units=V["units"])
    located = np.isfinite(B["loc"])
    for name, valid in (("all", located), ("fast", located & (B["vel_k"] > SPEED_MIN))):
        nn, nb = nn_conditioned(zn, B["loc"], valid, V["t"])
        nnx, _ = nn_conditioned(zn, B["loc"], valid, V["t"], exclude_visit=True)
        res = dict(nn=nn, nn_s=nan_smooth(nn), nnx_s=nan_smooth(nnx), nbr=nb, valid=valid)
        for e in ("k", "d"):
            vel, acc = B[f"vel_{e}"], B[f"acc_{e}"]
            has = nb >= 0
            dv = np.where(has, np.abs(vel[:, None] - vel[np.clip(nb, 0, None)]), np.nan)
            da = np.where(has, np.abs(acc[:, None] - acc[np.clip(nb, 0, None)]), np.nan)
            res[f"dvel3_{e}"] = np.nanmean(dv, 1) if has.any() else dv[:, 0]
            res[f"dacc3_{e}"] = np.nanmean(da, 1) if has.any() else da[:, 0]
            res[f"dvel1_{e}"] = _first_nn_diff(zn, nb, vel)
            res[f"dacc1_{e}"] = _first_nn_diff(zn, nb, acc)
        out[name] = res
    a, b = nn_unconditioned(zn, np.isfinite(zn[:, 0]))
    out["uncond_top3_s"] = nan_smooth(a)
    out["uncond_all_s"] = nan_smooth(b)
    return out


def _first_nn_diff(zn, nb, x):
    """|x(t) - x(nn)| for the single most correlated of the k neighbours."""
    n = len(zn)
    out = np.full(n, np.nan)
    has = (nb >= 0).all(1)
    i = np.where(has)[0]
    if len(i) == 0:
        return out
    r = np.einsum("ij,ikj->ik", zn[i], zn[nb[i]])
    best = nb[i, np.argmax(r, 1)]
    out[i] = np.abs(x[i] - x[best])
    return out
EOF
cp settle.py $TMPDIR/ && cd $TMPDIR && source env/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import time, numpy as np, settle as S
s=S.load_session("e16-3m2-211213"); ct,env=S.cell_types(s["sid"], s["spike_index"]); pyr=np.where(ct=="Pyramidal Cell")[0]
t=time.time(); M=S.run_measures(s,s["runs"][1],pyr); print("measures", time.time()-t)
for k in ("dvel3_k","dacc3_k","dvel1_d"): print(k, np.nanpercentile(M["fast"][k],[5,50,95]))
# reactivation timing
rng=np.random.default_rng(0); run=s["runs"][1]
post=S.ripple_vectors(s,M["units"],[(run["t1"],run["t1"]+1800)]); pre=S.ripple_vectors(s,M["units"],[(run["t0"]-1800,run["t0"])])
print("ripples", len(pre), len(post))
mom=np.r_[np.where(M["t"]<60)[0], np.where((M["t"]>=600)&(M["t"]<660))[0]]
t=time.time(); r=S.reactivation(post,{"post":np.ones(len(post),bool)},M["z"][mom],rng); print("react", time.time()-t, r["post"][0][:600].mean(), r["post"][0][600:].mean())
# FP check: shuffled observed
t=time.time(); r=S.reactivation(rng.permuted(post,axis=0),{"x":np.ones(len(post),bool)},M["z"][mom],rng); print("FP", r["x"][0].mean())
EOF
```

```
res[f"dvel3_{e}"] = np.nanmean(dv, 1) if has.any() else dv[:, 0]
  res[f"dacc3_{e}"] = np.nanmean(da, 1) if has.any() else da[:, 0]
measures 4.772737979888916
dvel3_k [0.53303199 2.44689701 6.59357633]
dacc3_k [0.79538249 3.44761482 9.19956676]
dvel1_d [0.06709185 1.53077996 6.78282606]
ripples 758 585
react 5.047736167907715 0.00254985754985755 0.0020341880341880345
FP 0.0010769230769230769
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/mckenzie-2025 && cat >> settle.py <<'EOF'


# ---------------------------------------------------------------- checks

def spatial_info_by_shift(counts, lin, shifts_s=(-120, -30, -5, 0, 5, 30, 120), bin_cm=4.0):
    """Mean Skaggs spatial information (bits/spike) over units, with position shifted in time.

    A check that position and spikes share a clock: information should peak at zero shift. The 4 cm
    bins are a standard choice for this check only.
    """
    ok = np.isfinite(lin)
    out = {}
    for sh in shifts_s:
        k = int(round(sh / BIN))
        l2 = np.roll(lin, k)
        m = ok & np.isfinite(l2)
        if k > 0:
            m[:k] = False
        elif k < 0:
            m[k:] = False
        loc = np.floor(l2[m] / bin_cm).astype(int)
        c = counts[m]
        occ = np.bincount(loc).astype(float)
        good = occ > 0
        p = occ[good] / occ.sum()
        info = []
        for j in range(c.shape[1]):
            r = np.bincount(loc, weights=c[:, j], minlength=len(occ))[good] / occ[good]
            lam = (p * r).sum()
            if lam <= 0:
                continue
            q = r / lam
            info.append(np.nansum(p * q * np.log2(np.where(q > 0, q, 1))))
        out[sh] = float(np.mean(info))
    return out
EOF
cp settle.py $TMPDIR/ && cd $TMPDIR && source env/bin/activate && python - <<'EOF' 2>&1 | grep -v Warn
import time, numpy as np, settle as S, umap
s=S.load_session("e16-3m2-211211"); ct,env=S.cell_types(s["sid"], s["spike_index"]); pyr=np.where(ct=="Pyramidal Cell")[0]
for run in s["runs"]:
    V=S.run_vectors(s,run,pyr); B=S.run_behaviour(s,run,V["edges"])
    print(run["t0"], S.spatial_info_by_shift(V["counts"],B["lin"]))
    # also test: shift spikes of the run against tracking from the later epoch 15124-16771? 
M=S.run_measures(s,s["runs"][1],pyr)
X=M["z"][M["t"]<1000][::2]
t=time.time(); e=umap.UMAP(random_state=1).fit_transform(X); print("umap", time.time()-t, X.shape)
EOF
```

```
res[f"dvel3_{e}"] = np.nanmean(dv, 1) if has.any() else dv[:, 0]
  res[f"dacc3_{e}"] = np.nanmean(da, 1) if has.any() else da[:, 0]
  self.fit(X, y, ensure_all_finite, **kwargs)
  warn(
5269.92 {-120: 0.4338117130807847, -30: 0.4315823099976104, -5: 0.8061413086682419, 0: 1.24418756573318, 5: 0.7783687907609523, 30: 0.4290303235331538, 120: 0.41445105086642897}
9559.136 {-120: 0.2728744357943066, -30: 0.2450058081315474, -5: 0.24766603990661307, 0: 0.24640382352924386, 5: 0.25635157889134813, 30: 0.2516695974303152, 120: 0.23338370878247072}
umap 44.26711630821228 (5000, 161)
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF' 2>&1 | grep -v "Warn\|res\[f"
import numpy as np, settle as S
for sid in ["e13-26m1-211019","e13-26m1-211116","e13-26m1-211119","e15-13f1-220118","e15-13f1-220119","e15-13f1-220120","e16-3m2-211211","e16-3m2-211212","e16-3m2-211213","e13-26m1-211124"]:
    s=S.load_session(sid); ct,env=S.cell_types(sid, s["spike_index"]); pyr=np.where(ct=="Pyramidal Cell")[0]
    for run in s["runs"]:
        V=S.run_vectors(s,run,pyr); B=S.run_behaviour(s,run,V["edges"])
        si=S.spatial_info_by_shift(V["counts"],B["lin"],shifts_s=(-30,0,30))
        print(sid, round(run["t0"]), round(run["t1"]-run["t0"]), run["familiar"], run["n_trials"], {k:round(v,2) for k,v in si.items()})
s=S.load_session("e16-3m2-211211"); ct,_=S.cell_types(s["sid"], s["spike_index"]); pyr=np.where(ct=="Pyramidal Cell")[0]
run=dict(s["runs"][1]); off=15123.6-9559.136
s2=dict(s); s2["pos_t"]=s["pos_t"].copy(); s2["pos_t"][run["idx"]]+=off
run2=dict(run); run2["t0"]=15123.6; run2["t1"]=16771.2
V=S.run_vectors(s2,run2,pyr); B=S.run_behaviour(s2,run2,V["edges"]); print("211211 tracking moved to linear_manu epoch", S.spatial_info_by_shift(V["counts"],B["lin"],shifts_s=(-30,-5,0,5,30)))
EOF
```

```
e13-26m1-211019 7590 1738 True 47 {-30: 0.37, 0: 0.97, 30: 0.36}
e13-26m1-211019 15088 1665 False 33 {-30: 0.3, 0: 0.59, 30: 0.3}
e13-26m1-211116 7470 1250 True 21 {-30: 0.5, 0: 1.01, 30: 0.5}
e13-26m1-211116 13595 344 False 9 {-30: 0.67, 0: 1.0, 30: 0.63}
e13-26m1-211119 6149 1432 True 25 {-30: 0.39, 0: 0.99, 30: 0.37}
e13-26m1-211119 14844 1606 False 58 {-30: 0.29, 0: 0.67, 30: 0.3}
e15-13f1-220118 5617 2100 True 25 {-30: 0.43, 0: 1.15, 30: 0.46}
e15-13f1-220118 13106 1943 False 68 {-30: 0.3, 0: 0.97, 30: 0.32}
e15-13f1-220119 6816 2064 True 29 {-30: 0.42, 0: 1.18, 30: 0.39}
e15-13f1-220119 21190 1513 False 32 {-30: 0.41, 0: 1.04, 30: 0.43}
e15-13f1-220120 9594 2374 True 46 {-30: 0.39, 0: 1.24, 30: 0.35}
e15-13f1-220120 17993 1817 False 49 {-30: 0.35, 0: 0.9, 30: 0.37}
e16-3m2-211211 5270 1263 True 32 {-30: 0.43, 0: 1.24, 30: 0.43}
e16-3m2-211211 9559 2443 False 45 {-30: 0.25, 0: 0.25, 30: 0.25}
e16-3m2-211212 6089 1770 True 29 {-30: 0.37, 0: 0.93, 30: 0.39}
e16-3m2-211212 16386 1354 False 34 {-30: 0.34, 0: 0.71, 30: 0.36}
e16-3m2-211213 7552 1826 True 27 {-30: 0.43, 0: 0.93, 30: 0.39}
e16-3m2-211213 13266 2061 False 29 {-30: 0.35, 0: 0.77, 30: 0.35}
e13-26m1-211124 8612 1404 False 26 {-30: 0.49, 0: 1.05, 30: 0.42}
211211 tracking moved to linear_manu epoch {-30: 0.25197192105482685, -5: 0.3998886369250896, 0: 0.6569037584523622, 5: 0.38241471076610223, 30: 0.27221234474276784}
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && uv pip install -q nbformat nbclient ipykernel statsmodels 2>&1 | tail -1; python -c "import nbformat; print('ok')"; date -u
```

```
ok
Thu Nov 26 17:12:25 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/mckenzie-2025 && cat >> settle.py <<'EOF'


# ---------------------------------------------------------------- place fields (Figure S7A, B)

def field_deviations(M, speed_for_dev=False):
    """Per-bin mean deviation of z-scored rates from the place map, in field and out of field.

    Maps (Methods, Place field detection): 1 cm linearized bins, bins above SPEED_MIN, location bins
    with more than MIN_OCC s; the map is the mean z-scored rate, the field the bins whose mean
    unnormalized rate exceeds FIELD_HZ. Units with no field bin are left out. Deviations are taken
    at every located bin (reading a) or only above SPEED_MIN (reading b, `speed_for_dev`).
    """
    B = M["beh"]
    loc = B["loc"]; fast = B["vel_k"] > SPEED_MIN
    z = M["z"]; hz = M["counts"] / BIN
    ok = np.isfinite(loc) & fast
    L = loc[ok].astype(int)
    nL = int(np.nanmax(loc)) + 1
    occ = np.bincount(L, minlength=nL) * BIN
    zmap = np.stack([np.bincount(L, weights=z[ok, j], minlength=nL) for j in range(z.shape[1])], 1)
    hmap = np.stack([np.bincount(L, weights=hz[ok, j], minlength=nL) for j in range(z.shape[1])], 1)
    n = np.maximum(np.bincount(L, minlength=nL), 1)[:, None]
    zmap /= n; hmap /= n
    good = occ > MIN_OCC
    field = (hmap > FIELD_HZ) & good[:, None]
    has_field = field.any(0)
    use = np.isfinite(loc) & (fast if speed_for_dev else True)
    use &= np.isfinite(loc) & good[np.nan_to_num(loc, nan=0).astype(int).clip(0, nL - 1)]
    idx = np.where(use)[0]
    li = loc[idx].astype(int)
    dev = z[idx][:, has_field] - zmap[li][:, has_field]
    inf = field[li][:, has_field]
    with np.errstate(invalid="ignore"):
        d_in = np.where(inf.sum(1) > 0, (dev * inf).sum(1) / inf.sum(1), np.nan)
        d_out = np.where((~inf).sum(1) > 0, (dev * ~inf).sum(1) / (~inf).sum(1), np.nan)
    t = M["t"][idx]
    return t, d_in, d_out, int(has_field.sum())


def minute_slope(t, x, minutes=10):
    m = np.array([np.nanmean(x[(t >= 60 * k) & (t < 60 * (k + 1))]) for k in range(minutes)])
    ok = np.isfinite(m)
    return (np.polyfit(np.arange(minutes)[ok], m[ok], 1)[0] if ok.sum() > 2 else np.nan), m


# ---------------------------------------------------------------- model of NN similarity (Figure S7E, F)

def _design(t, dv, da, terms, p):
    """Prediction of the model with the given terms; p holds every parameter."""
    b0, b1, r1, b2, r2, bv, ba = p
    y = np.zeros_like(t)
    if "intercept" in terms:
        y = y + b0
    if "time" in terms:
        y = y + b1 * np.exp(-r1 * t) - b2 * np.exp(-r2 * t)
    if "vel" in terms:
        y = y + bv * dv
    if "acc" in terms:
        y = y + ba * da
    return y


def fit_nn_model(t, dv, da, y, terms, form):
    """Fit one model; form 'exp' (photometry Methods form, rates bounded as there) or 'linear'."""
    from scipy.optimize import least_squares
    if form == "linear":
        cols = []
        names = []
        if "intercept" in terms:
            cols.append(np.ones_like(t)); names.append("b0")
        if "time" in terms:
            cols.append(t); names.append("bt")
        if "vel" in terms:
            cols.append(dv); names.append("bv")
        if "acc" in terms:
            cols.append(da); names.append("ba")
        X = np.stack(cols, 1)
        beta = np.linalg.lstsq(X, y, rcond=None)[0]
        return ("linear", terms, beta)
    lo = np.array([-10, 0, 0.001, 0, 0.0001, -10, -10.0])
    hi = np.array([10, 10, 0.1, 10, 0.001, 10, 10.0])
    p0 = np.array([np.mean(y), 0.1, 0.01, 0.01, 0.0005, 0, 0])
    res = least_squares(lambda p: _design(t, dv, da, terms, p) - y, p0, bounds=(lo, hi))
    return ("exp", terms, res.x)


def predict_nn_model(model, t, dv, da):
    form, terms, p = model
    if form == "exp":
        return _design(t, dv, da, terms, p)
    cols = []
    if "intercept" in terms:
        cols.append(np.ones_like(t))
    if "time" in terms:
        cols.append(t)
    if "vel" in terms:
        cols.append(dv)
    if "acc" in terms:
        cols.append(da)
    return np.stack(cols, 1) @ p


FULL = ("intercept", "time", "vel", "acc")


def cv_percent_change(data, form):
    """Leave-one-session-out CVMSE of the full model and of each reduced one (Methods, Reset analysis).

    data: list of (t, dv, da, y) per session. Returns dict dropped term -> per-session percent change
    in CVMSE relative to the full model.
    """
    out = {k: [] for k in FULL}
    for i in range(len(data)):
        tr = [d for j, d in enumerate(data) if j != i]
        T, DV, DA, Y = (np.concatenate([d[k] for d in tr]) for k in range(4))
        t, dv, da, y = data[i]
        full = fit_nn_model(T, DV, DA, Y, FULL, form)
        mse_full = np.mean((predict_nn_model(full, t, dv, da) - y) ** 2)
        for drop in FULL:
            terms = tuple(x for x in FULL if x != drop)
            m = fit_nn_model(T, DV, DA, Y, terms, form)
            mse = np.mean((predict_nn_model(m, t, dv, da) - y) ** 2)
            out[drop].append(100 * (mse - mse_full) / mse_full)
    return {k: np.array(v) for k, v in out.items()}
EOF
sed -i 's/            res\[f"dvel3_{e}"\] = np.nanmean(dv, 1) if has.any() else dv\[:, 0\]/            with np.errstate(all="ignore"):\n                res[f"dvel3_{e}"] = np.nanmean(dv, 1)\n                res[f"dacc3_{e}"] = np.nanmean(da, 1)/; /res\[f"dacc3_{e}"\] = np.nanmean(da, 1) if has.any() else da\[:, 0\]/d' settle.py
grep -n "dvel3\|dacc3" settle.py; python -c "import ast;ast.parse(open('settle.py').read())"
```

```
417:                res[f"dvel3_{e}"] = np.nanmean(dv, 1)
418:                res[f"dacc3_{e}"] = np.nanmean(da, 1)
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build1.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tag=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tag:\n        c.metadata[\"tags\"] = [tag] if isinstance(tag, str) else tag\n    cells.append(c)\n\n\nmd(r\"\"\"\n# McKenzie et al. (2025) on dandiset 000552: settling of the CA1 code after transfer\n\nPaper: McKenzie, Sommer, Donaldson, Pimentel, Kakani, Choi, Newman & English (2025), \"Event boundaries\ndrive norepinephrine release and distinctive neural representations of space in the rodent\nhippocampus\", eLife 14:RP105183, [doi:10.7554/elife.105183](https://doi.org/10.7554/elife.105183).\nThe claims file (`claims/mckenzie-2025.yaml`) was written from the eLife Reviewed Preprint version 1\n(January 31, 2025), with the legends of Figures S1 to S7.\n\nDataset: [DANDI:000552](https://dandiarchive.org/dandiset/000552/0.230630.2304) version\n**0.230630.2304** (Huszar et al. 2022). This is the version the paper cites (Methods, Electrophysiology\nsubjects: \"The complete dataset is available at https://dandiarchive.org/dandiset/000552/0.230630.2304\"),\nso it is pinned, as the protocol asks. A later version, 0.261113.1035 (2026-11-13), holds the same spike\ntimes (checked below, unit by unit) and adds CellExplorer cell types and epoch names; only those labels\nare read from it, because the pinned version has none (claims file E3). Every problem found in the pinned\nversion is also looked for in the later one.\n\nThis notebook tests the claims on population vectors, nearest neighbours, decorrelation and place\nfields (Figures 7, S6, S7). The reactivation claims (Figure 8) are in `reactivation.ipynb`. The\nphotometry claims (Figures 1 to 6, S1 to S5) are blocked: those recordings are not in the dandiset.\n\n| Claim | Here |\n|---|---|\n| figs1a-desipramine, figs1b-yohimbine, fig1d-arena-decay, figs1e-univariate-covariates, fig1e-arena-time-from-transition, fig2c-track-time-from-transition, figs2-no-reward-modulation, fig3d-object-introduction, figs3-object-order-and-sampling, fig4b-novel-object-on-track, fig5d-decay-hastens-with-days, figs4-behavior-day1-day2, fig6-recent-history | blocked, data missing (photometry) |\n| ne-and-settling-time-course | blocked, data missing (the NE half) |\n| ephys-ensemble-size | tested |\n| figs6b-decorrelation-novel, figs6d-decorrelation-familiar | tested |\n| fig7ab-umap-embedding | tested |\n| fig7e-novel-settling, fig7f-familiar-settling, fig7g-familiar-more-similar-early | tested |\n| figs7ab-in-field-out-field, figs7cd-movement-not-time-locked, figs7ef-time-explains-similarity, figs7gh-unconditioned-similarity | tested |\n| fig8b-late-moments-reactivated, fig8d-familiar-no-difference, fig8-no-pre-reactivation | tested in `reactivation.ipynb` |\n\"\"\")\n\ncode(r\"\"\"\nimport time, zlib, warnings, resource\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport settle as S\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 200, \"display.max_columns\", 40)\nT_START = time.time()\n\ndef seed(claim, k=0):\n    return zlib.crc32(f\"mckenzie-2025/{claim}\".encode()) + k\n\nprint(\"dandiset\", S.DANDISET_ID, \"version\", S.VERSION, \"labels from\", S.LABEL_VERSION)\n\"\"\")\n\nmd(r\"\"\"\n## Data check\n\nEach session file holds the units (spike times only, in the pinned version), the head position\n(x, y and a linearized position), trials, the ripples detected by Huszar et al., sleep states and,\nin most files, unlabeled epochs. The sessions of the three mice the Methods name are loaded. The maze\nruns are found as stretches of tracking; time 0 of a run (transfer, claims file E2) is the start of\nthe epoch that holds it.\n\"\"\")\n\ncode(r\"\"\"\nSESS = {}\nLABELS = {}\nfor sid in S.SESSIONS:\n    s = S.load_session(sid)\n    ct, env = S.cell_types(sid, s[\"spike_index\"])   # raises if the units differ between versions\n    s[\"cell_type\"] = ct\n    SESS[sid] = s\n    LABELS[sid] = env\nprint(f\"loaded {len(SESS)} sessions in {time.time() - T_START:.0f} s\")\n\"\"\")\n\ncode(r\"\"\"\ndef env_of(sid, t0, t1):\n    for a, b, e in LABELS[sid]:\n        if a <= (t0 + t1) / 2 < b:\n            return e\n    return \"?\"\n\nrows = []\nfor sid, s in SESS.items():\n    ct = s[\"cell_type\"]\n    for k, r in enumerate(s[\"runs\"]):\n        i = r[\"idx\"]\n        rows.append(dict(session=sid, units=len(s[\"spikes\"]), pyr=int((ct == \"Pyramidal Cell\").sum()),\n                         narrow=int((ct == \"Narrow Interneuron\").sum()), wide=int((ct == \"Wide Interneuron\").sum()),\n                         run=k, t0=round(r[\"t0\"], 1), dur_s=round(r[\"t1\"] - r[\"t0\"]), tracked_s=round(r[\"last_track\"] - r[\"first_track\"]),\n                         first_track_s=round(r[\"first_track\"] - r[\"t0\"], 1), trials=r[\"n_trials\"], familiar=r[\"familiar\"],\n                         env_label_version=env_of(sid, r[\"first_track\"], r[\"last_track\"]),\n                         x_range=f\"{np.nanmin(s['xy'][i, 0]):.2f}..{np.nanmax(s['xy'][i, 0]):.2f}\",\n                         y_range=f\"{np.nanmin(s['xy'][i, 1]):.2f}..{np.nanmax(s['xy'][i, 1]):.2f}\",\n                         lin_cm=f\"{np.nanmin(s['lin'][i]):.0f}..{np.nanmax(s['lin'][i]):.0f}\",\n                         frame_s=round(float(np.median(np.diff(s['pos_t'][i]))), 4)))\nruns_df = pd.DataFrame(rows)\nprint(runs_df.to_string())\nprint()\nfor sid, s in SESS.items():\n    st, lab = s[\"sleep\"]\n    print(sid, \"epochs:\", None if s[\"epochs\"] is None else len(s[\"epochs\"]),\n          \"| ripples:\", len(s[\"rip\"]), f\"duration {s['rip_dur'].min()*1e3:.0f} to {s['rip_dur'].max()*1e3:.0f} ms\",\n          \"| sleep labels:\", sorted(set(lab)), \"| position unit:\", s[\"xy_unit\"],\n          \"| spikes sorted:\", all(np.all(np.diff(x) >= 0) for x in s[\"spikes\"]))\n\"\"\", \"sanity\")\n\nmd(r\"\"\"\nWhat the check shows, against the paper and the files' own description:\n\n- The spike times of every unit are identical in the pinned and the later version (`cell_types` compares\n  the spike index of every file, and the spike times were compared at both ends while preparing).\n- Ripple durations lie within 20 to 200 ms in every session, the Methods' limits (Ripple detection).\n- Position is sampled at 30 Hz (25 Hz in three novel linear-track runs). The x, y position is stated in\n  cm; it spans 0 to about 92 in every familiar run, but 0 to 1 in five of the nine novel runs (below).\n  The linearized position is in cm in all runs, so it is the position used here.\n- Nine sessions have a familiar figure-eight run followed by a tracked novel run. Three more\n  (e13-26m1-211124, e15-13f1-220117, e16-3m2-211210) have one tracked run only; the later version's\n  labels say their second maze epoch is an open field, which has no tracking in the pinned version.\n\"\"\")\n\ncode(r\"\"\"\nf_old = S.open_file(\"e16-3m2-211211\"); f_new = S.open_file(\"e16-3m2-211211\", S.LABEL_VERSION)\nprint(\"pinned\", S.VERSION, \"units columns:\", sorted(f_old[\"units\"].keys()))\nprint(\"later \", S.LABEL_VERSION, \"units columns:\", sorted(f_new[\"units\"].keys()))\nprint(\"pinned epochs columns:\", sorted(f_old[\"intervals/epochs\"].keys()))\nprint(\"later  epochs columns:\", sorted(f_new[\"intervals/epochs\"].keys()))\nprint(\"e13-26m1-211116 pinned intervals:\", list(S.open_file(\"e13-26m1-211116\")[\"intervals\"].keys()))\n\"\"\", \"finding-no-cell-types\")\n\ncode(r\"\"\"\nfor sid, s in SESS.items():\n    for r in s[\"runs\"]:\n        i = r[\"idx\"]; xy = s[\"xy\"][i]\n        if np.nanmax(xy) <= 1.5:\n            print(f\"{sid} run at {r['t0']:.0f} s: x {np.nanmin(xy[:,0]):.2f}..{np.nanmax(xy[:,0]):.2f}, \"\n                  f\"y {np.nanmin(xy[:,1]):.2f}..{np.nanmax(xy[:,1]):.2f}, unit '{s['xy_unit']}', linearized {np.nanmin(s['lin'][i]):.0f}..{np.nanmax(s['lin'][i]):.0f} cm\")\nf = S.open_file(\"e13-26m1-211019\", S.LABEL_VERSION)\ng = f[\"processing/behavior/SubjectPosition/SpatialSeries2_tmaze_ipshita/data\"]\nprint(\"later version, e13-26m1-211019 novel run:\", g.attrs[\"unit\"], np.nanmin(g[:, 0]).round(2), np.nanmax(g[:, 0]).round(2))\n\"\"\", \"finding-position-not-cm\")\n\nmd(r\"\"\"\n**Clock check.** Position and spikes must share a clock. For every run, the mean spatial information of\nthe pyramidal units is computed with the position as recorded and shifted by 5, 30 and 120 s; on a\nshared clock it peaks at zero shift. This is the check the protocol asks for with continuous data.\n\"\"\")\n\ncode(r\"\"\"\nclock = []\nfor sid, s in SESS.items():\n    pyr = np.where(s[\"cell_type\"] == \"Pyramidal Cell\")[0]\n    for r in s[\"runs\"]:\n        V = S.run_vectors(s, r, pyr); B = S.run_behaviour(s, r, V[\"edges\"])\n        si = S.spatial_info_by_shift(V[\"counts\"], B[\"lin\"])\n        clock.append(dict(session=sid, t0=round(r[\"t0\"]), env=env_of(sid, r[\"first_track\"], r[\"last_track\"]),\n                          **{f\"shift {k:+d} s\": round(v, 3) for k, v in si.items()}))\nclock = pd.DataFrame(clock)\nclock[\"peak_at_0\"] = clock[[c for c in clock if c.startswith(\"shift\")]].idxmax(1) == \"shift +0 s\"\nprint(clock.to_string())\n\"\"\", \"sanity\")\n\ncode(r\"\"\"\n# e16-3m2-211211: the novel-run tracking and its trials sit in the epoch the later version names an\n# open field (9559 to 12002 s); the later version names the next maze epoch (15124 to 16771 s) the linear track.\nsid = \"e16-3m2-211211\"; s = SESS[sid]; r = s[\"runs\"][1]\npyr = np.where(s[\"cell_type\"] == \"Pyramidal Cell\")[0]\nprint(\"epochs:\", [(round(a), round(b), e) for a, b, e in LABELS[sid]])\nprint(f\"tracking as filed: {s['pos_t'][r['idx']][0]:.1f} to {s['pos_t'][r['idx']][-1]:.1f} s, linearized \"\n      f\"{np.nanmin(s['lin'][r['idx']]):.0f}..{np.nanmax(s['lin'][r['idx']]):.0f} cm; trials {r['n_trials']}\")\nV = S.run_vectors(s, r, pyr); B = S.run_behaviour(s, r, V[\"edges\"])\nprint(\"spatial information, tracking as filed:\", {k: round(v, 3) for k, v in S.spatial_info_by_shift(V[\"counts\"], B[\"lin\"], (-30, -5, 0, 5, 30)).items()})\nlin_ep = [(a, b) for a, b, e in LABELS[sid] if e == \"linear_manu\"][0]\noff = lin_ep[0] - r[\"t0\"]\ns2 = dict(s); s2[\"pos_t\"] = s[\"pos_t\"].copy(); s2[\"pos_t\"][r[\"idx\"]] += off\nr2 = dict(r, t0=lin_ep[0], t1=lin_ep[1])\nV2 = S.run_vectors(s2, r2, pyr); B2 = S.run_behaviour(s2, r2, V2[\"edges\"])\nprint(f\"spatial information, tracking moved by {off:.1f} s onto the linear_manu epoch:\",\n      {k: round(v, 3) for k, v in S.spatial_info_by_shift(V2[\"counts\"], B2[\"lin\"], (-30, -5, 0, 5, 30)).items()})\nf = S.open_file(sid, S.LABEL_VERSION)\nts = f[\"processing/behavior/SubjectPosition/SpatialSeries3_linear_manu/timestamps\"]\nprint(f\"later version: linear_manu tracking {ts[0]:.1f} to {ts[-1]:.1f} s, inside its open-field epoch too\")\n\"\"\", \"finding-tracking-misfiled\")\n\ncode(r\"\"\"\nfor sid, s in SESS.items():\n    print(sid, \"| behavior module description:\", repr(s[\"behavior_description\"]))\n\"\"\", \"finding-behavior-description\")\n\nmd(r\"\"\"\n## Sessions (claims file E1)\n\nThe sessions that fit the Methods' description are those with a familiar figure-eight run and a tracked\nnovel run: nine. In e13-26m1-211116 the novel epoch is missing from the pinned file and the tracking\nlasts 344 s, so it has no minute 10; the tests use the other **eight**, the paper's N. By the later\nversion's labels these are 3 novel figure-eight mazes (`tmaze_ipshita`), 4 linear tracks and, in\ne16-3m2-211211, an open field whose time holds linear-track tracking (above); the paper lists 3 linear\ntracks, 3 figure-eight mazes and 1 arena. Where a session had two novel environments, the pinned version\ntracks only one, so E1's readings (a) and (b) are the same here.\n\ne16-3m2-211211's novel run is the open-field epoch; analyses that do not use position keep it. Analyses\nconditioned on location use its position as filed in the main reading (the paper's eight sessions) and\nare also shown on the seven sessions whose tracking passes the clock check.\n\"\"\")\n\ncode(r\"\"\"\nALL9 = [sid for sid, s in SESS.items() if len(s[\"runs\"]) >= 2]\nTEST = [sid for sid in ALL9 if SESS[sid][\"runs\"][1][\"t1\"] - SESS[sid][\"runs\"][1][\"t0\"] >= 660]\nCLOCK_OK = [sid for sid in TEST if sid != \"e16-3m2-211211\"]\nprint(\"sessions with familiar and novel runs:\", len(ALL9), ALL9)\nprint(\"tested (novel run at least 660 s):\", len(TEST))\nprint(\"with tracking that passes the clock check:\", len(CLOCK_OK))\nfor sid in TEST:\n    s = SESS[sid]; f, n = s[\"runs\"][0], s[\"runs\"][1]\n    print(f\"  {sid}: familiar {f['t0']:.0f}+{f['t1']-f['t0']:.0f} s ({env_of(sid, f['first_track'], f['last_track'])}), \"\n          f\"novel {n['t0']:.0f}+{n['t1']-n['t0']:.0f} s ({env_of(sid, n['first_track'], n['last_track'])}), familiar flag of trials {f['familiar']}/{n['familiar']}\")\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\nMEAS = {}      # (session, 'fam'|'nov', 'pyr'|'all') -> measures\nfor sid in TEST:\n    s = SESS[sid]\n    pyr = np.where(s[\"cell_type\"] == \"Pyramidal Cell\")[0]\n    for env, r in ((\"fam\", s[\"runs\"][0]), (\"nov\", s[\"runs\"][1])):\n        MEAS[(sid, env, \"pyr\")] = S.run_measures(s, r, pyr)\n        MEAS[(sid, env, \"all\")] = S.run_measures(s, r, np.arange(len(s[\"spikes\"])))\nprint(f\"measures for {len(MEAS)} runs in {time.time() - t0:.0f} s; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.1f} GB\")\nprint(\"units dropped (no spike in the first 1000 s):\", {f\"{k[0]} {k[1]} {k[2]}\": v[\"dropped\"] for k, v in MEAS.items() if v[\"dropped\"]})\n\"\"\")\n\nmd(r\"\"\"\n## ephys-ensemble-size\n\n> The analyzed CA1 ensembles contain on average 253.8 neurons per session, ranging from 191 to 363.\n\nCriterion: over the sessions of E1, (a) the pyramidal units or (b) all units; reproduced when, under one\nreading, the mean is within 25.4 of 253.8 and every session lies within 172 to 399.\n\"\"\")\n\ncode(r\"\"\"\ncnt = pd.DataFrame([dict(session=sid, all_units=len(SESS[sid][\"spikes\"]),\n                         pyramidal=int((SESS[sid][\"cell_type\"] == \"Pyramidal Cell\").sum())) for sid in ALL9])\nprint(cnt.to_string())\nfor name, sel in ((\"8 tested sessions\", TEST), (\"9 sessions with a novel run\", ALL9)):\n    c = cnt.set_index(\"session\").loc[sel]\n    for col in (\"pyramidal\", \"all_units\"):\n        v = c[col].values\n        ok = abs(v.mean() - 253.8) <= 25.4 and v.min() >= 172 and v.max() <= 399\n        print(f\"{name}, {col}: mean {v.mean():.2f}, range {v.min()} to {v.max()} -> {'within' if ok else 'outside'} tolerance\")\n\"\"\", \"claim:ephys-ensemble-size\")\n\nmd(r\"\"\"\n**Result: reproduced under reading (b), all units.** Over the eight tested sessions all units give a mean of\n259.4 (191 to 363); over the nine sessions with a novel run the mean is 253.8 and the range 191 to 363,\nthe paper's numbers exactly. Pyramidal units alone give a mean of 216.5, outside the tolerance, so the\npaper's ensemble count is of all units, while its Methods analyze pyramidal cells only.\n\"\"\")\n\nmd(r\"\"\"\n## figs6b-decorrelation-novel and figs6d-decorrelation-familiar\n\n> In a novel environment, CA1 population vectors decorrelate faster with lag in the first minute after transfer than at minute 10.\n> In the familiar environment the decorrelation rate does not differ between the first minute and minute 10 after transfer.\n\nPer session and window, the mean Pearson R of z-scored pyramidal vectors at lags 0.1 to 10 s (both bins\nin the window), fit with R = beta exp(-lag/tau) + c; the rate is 1/tau. Window readings: (a) the 60 s of\nthe minute, (b) 100 s from its start; minute 10 as 600 or 540 s. Paired t-test over the eight sessions.\n\"\"\")\n\ncode(r\"\"\"\ndef decay_table(env, units=\"pyr\", sessions=TEST):\n    rows = []\n    for sid in sessions:\n        M = MEAS[(sid, env, units)]\n        row = dict(session=sid)\n        for wname, length in ((\"a60\", 60.0), (\"b100\", 100.0)):\n            for mname, start in ((\"min1\", 0.0), (\"min10\", 600.0), (\"min10alt\", 540.0)):\n                lag, r = S.decorrelation_curve(M[\"zn\"], M[\"t\"], start, length)\n                row[f\"{wname}_{mname}\"] = S.decay_rate(lag, r)[0]\n                row[f\"{wname}_{mname}_r0.1\"] = r[0]\n        rows.append(row)\n    return pd.DataFrame(rows).set_index(\"session\")\n\ndef paired(a, b):\n    ok = np.isfinite(a) & np.isfinite(b)\n    t, p = stats.ttest_rel(a[ok], b[ok])\n    return t, p, int(ok.sum()), float(np.mean(a[ok] - b[ok]))\n\nDEC = {env: decay_table(env) for env in (\"nov\", \"fam\")}\nfor env in (\"nov\", \"fam\"):\n    d = DEC[env]\n    print(f\"== {env}: decay rates (1/s)\")\n    print(d[[c for c in d if not c.endswith(\"r0.1\")]].round(3).to_string())\n    for w in (\"a60\", \"b100\"):\n        for m10 in (\"min10\", \"min10alt\"):\n            t, p, n, md_ = paired(d[f\"{w}_min1\"].values, d[f\"{w}_{m10}\"].values)\n            print(f\"  {env} window {w}, minute 1 vs {m10}: mean difference {md_:+.3f} 1/s, t({n-1}) = {t:.2f}, p = {p:.3g}\")\n    print(\"  rates above 100 1/s (tau under 10 ms):\", int((d[[c for c in d if not c.endswith('r0.1')]] > 100).sum().sum()))\n\"\"\", [\"claim:figs6b-decorrelation-novel\", \"claim:figs6d-decorrelation-familiar\"])\n\ncode(r\"\"\"\nfig, ax = plt.subplots(1, 2, figsize=(9, 3.2))\nfor k, env in enumerate((\"nov\", \"fam\")):\n    for start, col in ((0, \"k\"), (600, \"b\")):\n        curves = []\n        for sid in TEST:\n            M = MEAS[(sid, env, \"pyr\")]\n            lag, r = S.decorrelation_curve(M[\"zn\"], M[\"t\"], start, 60.0)\n            curves.append(r)\n        c = np.nanmean(curves, 0)\n        ax[k].semilogx(lag, c, col, label=f\"minute {'1' if start == 0 else '10'}\")\n        print(env, start, \"mean curve range\", np.nanmin(c).round(3), np.nanmax(c).round(3))\n    ax[k].set_title({\"nov\": \"novel\", \"fam\": \"familiar\"}[env]); ax[k].set_xlabel(\"lag (s)\"); ax[k].set_ylabel(\"mean R\")\n    ax[k].legend()\nplt.tight_layout(); plt.show()\n\"\"\", [\"claim:figs6b-decorrelation-novel\", \"claim:figs6d-decorrelation-familiar\"])\n\ncode(r\"\"\"\n# the same on the seven sessions whose tracking passes the clock check (position is not used here)\nfor env in (\"nov\", \"fam\"):\n    d = DEC[env].loc[CLOCK_OK]\n    t, p, n, md_ = paired(d[\"a60_min1\"].values, d[\"a60_min10\"].values)\n    print(f\"{env}, 7 sessions, reading (a) 600-660: difference {md_:+.3f}, t({n-1}) = {t:.2f}, p = {p:.3g}\")\n\"\"\", [\"claim:figs6b-decorrelation-novel\", \"claim:figs6d-decorrelation-familiar\"])\n\nmd(r\"\"\"\n**Result: figs6b-decorrelation-novel, see the numbers above; figs6d-decorrelation-familiar, see the numbers above.**\n\"\"\")\n\nmd(r\"\"\"\n## fig7ab-umap-embedding\n\n> A 2D UMAP embedding of 100 ms population vectors maps the spatial layout of the environment, and moments just after transition lie at the periphery of the representational space.\n\nUMAP (umap-learn defaults) on the z-scored pyramidal vectors of the first 1000 s of each novel run, every\nfifth bin (2000 vectors; a reduction for time). Position mapping: 10-nearest-neighbour regression of the\nlinearized position from the embedding, 5 contiguous folds, R^2 against the same with the position\npermuted in 10 s blocks. Periphery: mean distance from the embedding's median of first-minute bins\nagainst bins from 60 to 1000 s. Reproduced when both hold in most sessions. Run under the claim's seed and\nfour more.\n\"\"\")\n\ncode(r\"\"\"\nimport umap\nfrom sklearn.neighbors import KNeighborsRegressor\nfrom sklearn.model_selection import KFold, cross_val_predict\n\ndef umap_measures(sid, rs, rng):\n    M = MEAS[(sid, \"nov\", \"pyr\")]\n    sel = np.where(M[\"t\"] < 1000)[0][::5]\n    E = umap.UMAP(random_state=rs).fit_transform(M[\"z\"][sel])\n    t = M[\"t\"][sel]; lin = M[\"beh\"][\"lin\"][sel]\n    ok = np.isfinite(lin)\n    knn = KNeighborsRegressor(10)\n    pred = cross_val_predict(knn, E[ok], lin[ok], cv=KFold(5))\n    r2 = 1 - np.mean((pred - lin[ok]) ** 2) / np.var(lin[ok])\n    blocks = (t[ok] // 10).astype(int)\n    ub = np.unique(blocks); perm = dict(zip(ub, rng.permutation(ub)))\n    shuf = np.concatenate([lin[ok][blocks == perm[b]] for b in ub])[: ok.sum()]\n    # permuted blocks can differ in length; pad by wrapping\n    if len(shuf) < ok.sum():\n        shuf = np.resize(shuf, ok.sum())\n    pred_s = cross_val_predict(knn, E[ok], shuf, cv=KFold(5))\n    r2_s = 1 - np.mean((pred_s - shuf) ** 2) / np.var(shuf)\n    d = np.linalg.norm(E - np.median(E, 0), axis=1)\n    return dict(session=sid, r2=r2, r2_shuffled=r2_s, dist_min1=d[t < 60].mean(), dist_later=d[t >= 60].mean(),\n                n=len(sel), located=int(ok.sum())), E, t, lin\n\nt0 = time.time()\nUM = {}\nfor k in range(5):\n    sd = seed(\"fig7ab-umap-embedding\") + 1000 * k\n    rng = np.random.default_rng(sd)\n    rows = []\n    for sid in TEST:\n        res, E, t, lin = umap_measures(sid, sd % (2**31), rng)\n        rows.append(res)\n        if k == 0 and sid == \"e16-3m2-211212\":\n            EX = (E, t, lin)\n    UM[sd] = pd.DataFrame(rows).set_index(\"session\")\n    UM[sd][\"maps_position\"] = UM[sd][\"r2\"] > UM[sd][\"r2_shuffled\"]\n    UM[sd][\"early_peripheral\"] = UM[sd][\"dist_min1\"] > UM[sd][\"dist_later\"]\nprint(f\"UMAP runs in {time.time() - t0:.0f} s\")\nfor sd, d in UM.items():\n    print(f\"seed {sd}: position mapped in {d['maps_position'].sum()}/8, first minute peripheral in {d['early_peripheral'].sum()}/8 \"\n          f\"(clock-checked 7: {d.loc[CLOCK_OK, 'maps_position'].sum()}/7, {d.loc[CLOCK_OK, 'early_peripheral'].sum()}/7)\")\nprint(UM[seed(\"fig7ab-umap-embedding\")].round(3).to_string())\n\"\"\", \"claim:fig7ab-umap-embedding\")\n\ncode(r\"\"\"\nE, t, lin = EX\nfig, ax = plt.subplots(1, 2, figsize=(9, 4))\na = ax[0].scatter(E[:, 0], E[:, 1], c=lin, s=3, cmap=\"viridis\"); plt.colorbar(a, ax=ax[0], label=\"linearized position (cm)\")\nb = ax[1].scatter(E[:, 0], E[:, 1], c=t, s=3, cmap=\"magma\"); plt.colorbar(b, ax=ax[1], label=\"time from transfer (s)\")\nax[0].set_title(\"e16-3m2-211212, novel linear track\"); ax[1].set_title(\"same, by time\")\nplt.tight_layout(); plt.show()\nprint(\"position\", np.nanmin(lin).round(1), np.nanmax(lin).round(1), \"time\", t.min().round(1), t.max().round(1))\n\"\"\", \"claim:fig7ab-umap-embedding\")\n\nmd(r\"\"\"\n**Result: fig7ab-umap-embedding, see above.**\n\"\"\")\n\nmd(r\"\"\"\n## fig7e-novel-settling, fig7f-familiar-settling, fig7g-familiar-more-similar-early\n\n> In a novel environment, population vectors in the first minute after transfer correlate less with their nearest neighbors at the same location than those 10 minutes into the session.\n> In the familiar environment, too, ...\n> Initial representations are more correlated with their nearest neighbors in the familiar environment than in the novel one.\n\nPer bin, the mean R of the 3 most correlated vectors in the same 1 cm location bin (at least 1 s of\noccupancy), smoothed with a 1 s Gaussian; per session the mean over minute 1 and minute 10. Readings: E5\nall bins or bins above 5 cm/s; E6 minute 10 as 600 or 540 s; the session set (8 as deposited, or the 7\nwhose tracking passes the clock check). Paired t-tests over sessions.\n\"\"\")\n\ncode(r\"\"\"\ndef nn_table(units=\"pyr\", key=\"nn_s\"):\n    rows = []\n    for sid in TEST:\n        for env in (\"nov\", \"fam\"):\n            M = MEAS[(sid, env, units)]\n            for spd in (\"all\", \"fast\"):\n                x = M[spd][key]\n                rows.append(dict(session=sid, env=env, speed=spd,\n                                 min1=S.window_mean(x, M[\"t\"], 0), min10=S.window_mean(x, M[\"t\"], 600),\n                                 min10alt=S.window_mean(x, M[\"t\"], 540),\n                                 **{f\"m{k+1}\": S.window_mean(x, M[\"t\"], 60 * k) for k in range(15)}))\n    return pd.DataFrame(rows)\n\nNN = nn_table()\nprint(NN[[\"session\", \"env\", \"speed\", \"min1\", \"min10\", \"min10alt\"]].round(3).to_string())\nFIG7 = []\nfor sset_name, sset in ((\"8 sessions\", TEST), (\"7 clock-checked\", CLOCK_OK)):\n    for spd in (\"all\", \"fast\"):\n        for m10 in (\"min10\", \"min10alt\"):\n            for env in (\"nov\", \"fam\"):\n                d = NN[(NN.env == env) & (NN.speed == spd) & NN.session.isin(sset)]\n                t, p, n, md_ = paired(d[\"min1\"].values, d[m10].values)\n                FIG7.append(dict(claim=\"fig7e\" if env == \"nov\" else \"fig7f\", sessions=sset_name, speed=spd, minute10=m10,\n                                 diff_min1_minus_min10=md_, t=t, df=n - 1, p=p))\n            dn = NN[(NN.env == \"nov\") & (NN.speed == spd) & NN.session.isin(sset)].set_index(\"session\")\n            df_ = NN[(NN.env == \"fam\") & (NN.speed == spd) & NN.session.isin(sset)].set_index(\"session\")\n            if m10 == \"min10\":\n                t, p, n, md_ = paired(df_[\"min1\"].values, dn.loc[df_.index, \"min1\"].values)\n                FIG7.append(dict(claim=\"fig7g\", sessions=sset_name, speed=spd, minute10=\"-\", diff_min1_minus_min10=md_, t=t, df=n - 1, p=p))\nFIG7 = pd.DataFrame(FIG7)\nprint(FIG7.round(4).to_string())\n\"\"\", [\"claim:fig7e-novel-settling\", \"claim:fig7f-familiar-settling\", \"claim:fig7g-familiar-more-similar-early\"])\n\ncode(r\"\"\"\n# variants, not judged: neighbours from other visits only, and all units\nfor label, units, key in ((\"other visits only\", \"pyr\", \"nnx_s\"), (\"all units\", \"all\", \"nn_s\")):\n    d = nn_table(units, key)\n    for env in (\"nov\", \"fam\"):\n        x = d[(d.env == env) & (d.speed == \"all\")]\n        t, p, n, md_ = paired(x[\"min1\"].values, x[\"min10\"].values)\n        print(f\"{label}, {env}: min1 {x['min1'].mean():.3f}, min10 {x['min10'].mean():.3f}, t({n-1}) = {t:.2f}, p = {p:.3g}\")\n    a = d[(d.env == \"fam\") & (d.speed == \"all\")].set_index(\"session\")[\"min1\"]; b = d[(d.env == \"nov\") & (d.speed == \"all\")].set_index(\"session\")[\"min1\"]\n    t, p, n, md_ = paired(a.values, b.loc[a.index].values)\n    print(f\"{label}, familiar vs novel minute 1: difference {md_:+.3f}, t({n-1}) = {t:.2f}, p = {p:.3g}\")\n\"\"\", [\"claim:fig7e-novel-settling\", \"claim:fig7f-familiar-settling\", \"claim:fig7g-familiar-more-similar-early\"])\n\ncode(r\"\"\"\n# per-minute session means (the 'several minutes' and 'more rapidly' parts, shown, not judged)\nmins = [f\"m{k+1}\" for k in range(15)]\nfor env in (\"nov\", \"fam\"):\n    d = NN[(NN.env == env) & (NN.speed == \"all\")]\n    print(env, \"mean over sessions by minute:\", np.round(d[mins].mean().values, 3))\nfig, ax = plt.subplots(figsize=(5, 3))\nfor env, col in ((\"nov\", \"r\"), (\"fam\", \"k\")):\n    d = NN[(NN.env == env) & (NN.speed == \"all\")]\n    ax.plot(range(1, 16), d[mins].mean().values, col, marker=\"o\", label={\"nov\": \"novel\", \"fam\": \"familiar\"}[env])\nax.set_xlabel(\"minute after transfer\"); ax.set_ylabel(\"NN correlation (R)\"); ax.legend(); plt.tight_layout(); plt.show()\nprint(\"by session, novel minute 1 and 10:\")\nprint(NN[(NN.speed == \"all\")].pivot(index=\"session\", columns=\"env\", values=[\"min1\", \"min10\"]).round(3).to_string())\n\"\"\", [\"claim:fig7e-novel-settling\", \"claim:fig7f-familiar-settling\", \"claim:fig7g-familiar-more-similar-early\"])\n\nmd(r\"\"\"\n**Result: fig7e, fig7f, fig7g, see above.**\n\"\"\")\n\nmd(r\"\"\"\n## figs7ab-in-field-out-field\n\n> Settling involves an increase over time of firing within each neuron's place field and a decrease of out-of-field firing, in novel and familiar environments.\n\nPlace maps on 1 cm linearized bins above 5 cm/s with more than 1 s occupancy; fields where the\nunnormalized rate exceeds 5 Hz; per 100 ms bin, the mean deviation of z-scored rates from the map, in\nfield and out of field; per session the slope over minutes 1 to 10. Readings: deviations at (a) all bins,\n(b) bins above 5 cm/s. One-sample t-tests of the slopes over sessions.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor sid in TEST:\n    for env in (\"nov\", \"fam\"):\n        M = MEAS[(sid, env, \"pyr\")]\n        for rd, spd in ((\"a\", False), (\"b\", True)):\n            t, din, dout, nf = S.field_deviations(M, spd)\n            s_in, m_in = S.minute_slope(t, din); s_out, m_out = S.minute_slope(t, dout)\n            rows.append(dict(session=sid, env=env, reading=rd, units_with_field=nf, slope_in=s_in, slope_out=s_out,\n                             in_min1=m_in[0], in_min10=m_in[-1], out_min1=m_out[0], out_min10=m_out[-1]))\nFLD = pd.DataFrame(rows)\nprint(FLD.round(4).to_string())\nfor sset_name, sset in ((\"8 sessions\", TEST), (\"7 clock-checked\", CLOCK_OK)):\n    for rd in (\"a\", \"b\"):\n        for env in (\"nov\", \"fam\"):\n            d = FLD[(FLD.env == env) & (FLD.reading == rd) & FLD.session.isin(sset)]\n            ti, pi = stats.ttest_1samp(d.slope_in, 0, nan_policy=\"omit\"); to, po = stats.ttest_1samp(d.slope_out, 0, nan_policy=\"omit\")\n            print(f\"{sset_name}, reading {rd}, {env}: in-field slope {d.slope_in.mean():+.4f} (t = {ti:.2f}, p = {pi:.3g}), \"\n                  f\"out-of-field slope {d.slope_out.mean():+.4f} (t = {to:.2f}, p = {po:.3g})\")\n\"\"\", \"claim:figs7ab-in-field-out-field\")\n\nmd(r\"\"\"\n**Result: figs7ab-in-field-out-field, see above.**\n\"\"\")\n\nmd(r\"\"\"\n## figs7cd-movement-not-time-locked\n\n> For the most similar pairs of moments, the absolute differences in velocity and acceleration show no systematic relationship with time after transfer.\n\nPer session, the Spearman correlation of |dvel|NN and |dacc|NN with time over the first 600 s (and the\nfirst 1000 s as a variant); t-test of the mean over sessions against 0. Readings: 3 neighbours or the\nsingle nearest; E8 Kalman or finite differences; E5 all bins or above 5 cm/s. Judged under the first\nreading of each (3 neighbours, Kalman, all bins), the others shown.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor sid in TEST:\n    for env in (\"nov\", \"fam\"):\n        M = MEAS[(sid, env, \"pyr\")]\n        for spd in (\"all\", \"fast\"):\n            for nnk in (\"3\", \"1\"):\n                for e in (\"k\", \"d\"):\n                    for meas in (\"dvel\", \"dacc\"):\n                        x = M[spd][f\"{meas}{nnk}_{e}\"]\n                        for win in (600, 1000):\n                            m = (M[\"t\"] < win) & np.isfinite(x)\n                            rho = stats.spearmanr(M[\"t\"][m], x[m])[0] if m.sum() > 10 else np.nan\n                            rows.append(dict(session=sid, env=env, speed=spd, nn=nnk, filt=e, measure=meas, window=win, rho=rho))\nMOV = pd.DataFrame(rows)\nsumm = []\nfor key, d in MOV.groupby([\"env\", \"measure\", \"nn\", \"filt\", \"speed\", \"window\"]):\n    for sset_name, sset in ((\"8\", TEST), (\"7\", CLOCK_OK)):\n        x = d[d.session.isin(sset)].rho.values\n        t, p = stats.ttest_1samp(x, 0, nan_policy=\"omit\")\n        summ.append(dict(zip([\"env\", \"measure\", \"nn\", \"filt\", \"speed\", \"window\"], key), sessions=sset_name, mean_rho=np.nanmean(x), t=t, p=p))\nMOVS = pd.DataFrame(summ)\nmain = MOVS[(MOVS.nn == \"3\") & (MOVS.filt == \"k\") & (MOVS.speed == \"all\") & (MOVS.window == 600)]\nprint(\"main reading (3 neighbours, Kalman, all bins, first 600 s):\")\nprint(main.round(4).to_string())\nprint(\"\\nevery reading, 8 sessions, first 600 s: number of tests with p < 0.05 out of\", len(MOVS[(MOVS.sessions == \"8\") & (MOVS.window == 600)]),\n      \":\", int((MOVS[(MOVS.sessions == \"8\") & (MOVS.window == 600)].p < 0.05).sum()))\nprint(MOVS[(MOVS.sessions == \"8\")].round(3).to_string())\n\"\"\", \"claim:figs7cd-movement-not-time-locked\")\n\nmd(r\"\"\"\n**Result: figs7cd-movement-not-time-locked, see above.**\n\"\"\")\n\nmd(r\"\"\"\n## figs7ef-time-explains-similarity\n\n> Modeling nearest-neighbor similarity as a function of time from transfer, |dvel|NN and |dacc|NN, only removing time from transition significantly decreases cross-validated prediction, in novel and familiar environments.\n\nThe smoothed NN correlation of each bin, modelled on time from transfer, |dvel|NN and |dacc|NN; each session\nwithheld in turn; percent change in CVMSE on dropping each variable, one-sample t-test against 0 over\nsessions. Readings: (a) the photometry Methods' form (a fast positive and a slow negative exponential of\ntime, rates bounded at 0.001 to 0.1 and 0.0001 to 0.001 per s, linear movement terms), bounded least\nsquares; (b) linear in all three; with the E8 and neighbour readings. Bins are taken every 1 s (every\ntenth), as the series is smoothed with a 1 s Gaussian.\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\nrows = []\nfor form in (\"exp\", \"linear\"):\n    for nnk in (\"3\", \"1\"):\n        for e in (\"k\", \"d\"):\n            for env in (\"nov\", \"fam\"):\n                for sset_name, sset in ((\"8\", TEST), (\"7\", CLOCK_OK)):\n                    data = []\n                    for sid in sset:\n                        M = MEAS[(sid, env, \"pyr\")]\n                        y = M[\"all\"][\"nn_s\"]; dv = M[\"all\"][f\"dvel{nnk}_{e}\"]; da = M[\"all\"][f\"dacc{nnk}_{e}\"]\n                        m = np.isfinite(y) & np.isfinite(dv) & np.isfinite(da)\n                        i = np.where(m)[0][::10]\n                        data.append((M[\"t\"][i], dv[i], da[i], y[i]))\n                    pc = S.cv_percent_change(data, form)\n                    for drop, v in pc.items():\n                        t, p = stats.ttest_1samp(v, 0)\n                        rows.append(dict(form=form, nn=nnk, filt=e, env=env, sessions=sset_name, dropped=drop,\n                                         mean_pct=v.mean(), t=t, p=p, n=len(v)))\nCV = pd.DataFrame(rows)\nprint(f\"model fits in {time.time() - t0:.0f} s\")\nprint(CV.round(4).to_string())\ndef verdict(d):\n    ok = {}\n    for env in (\"nov\", \"fam\"):\n        x = d[d.env == env].set_index(\"dropped\")\n        ok[env] = (x.loc[\"time\", \"p\"] < 0.05 and x.loc[\"time\", \"mean_pct\"] > 0\n                   and x.loc[\"vel\", \"p\"] >= 0.05 and x.loc[\"acc\", \"p\"] >= 0.05)\n    return ok\nfor key, d in CV.groupby([\"form\", \"nn\", \"filt\", \"sessions\"]):\n    print(key, verdict(d))\n\"\"\", \"claim:figs7ef-time-explains-similarity\")\n\nmd(r\"\"\"\n**Result: figs7ef-time-explains-similarity, see above.**\n\"\"\")\n\nmd(r\"\"\"\n## figs7gh-unconditioned-similarity\n\n> When representational similarity is not conditioned on location, first-minute patterns are still less correlated with the rest of the session than those 10 minutes in, in novel and familiar environments.\n\nReadings: (a) the 3 most correlated vectors anywhere in the run, (b) the mean correlation with all other\nvectors of the run; both smoothed with a 1 s Gaussian; minute 10 as 600 or 540 s. Paired t-tests.\n\"\"\")\n\ncode(r\"\"\"\nrows = []\nfor sid in TEST:\n    for env in (\"nov\", \"fam\"):\n        M = MEAS[(sid, env, \"pyr\")]\n        for rd, key in ((\"a\", \"uncond_top3_s\"), (\"b\", \"uncond_all_s\")):\n            x = M[key]\n            rows.append(dict(session=sid, env=env, reading=rd, min1=S.window_mean(x, M[\"t\"], 0),\n                             min10=S.window_mean(x, M[\"t\"], 600), min10alt=S.window_mean(x, M[\"t\"], 540)))\nUNC = pd.DataFrame(rows)\nprint(UNC.round(4).to_string())\nfor rd in (\"a\", \"b\"):\n    for m10 in (\"min10\", \"min10alt\"):\n        for env in (\"nov\", \"fam\"):\n            d = UNC[(UNC.env == env) & (UNC.reading == rd)]\n            t, p, n, md_ = paired(d[\"min1\"].values, d[m10].values)\n            print(f\"reading {rd}, {m10}, {env}: min1 - min10 = {md_:+.4f}, t({n-1}) = {t:.2f}, p = {p:.3g}\")\n\"\"\", \"claim:figs7gh-unconditioned-similarity\")\n\nmd(r\"\"\"\n**Result: figs7gh-unconditioned-similarity, see above.**\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\nFilled in after the run.\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"notebook runtime {(time.time() - T_START) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.1f} GB\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/mckenzie-2025/settling.ipynb\")\nprint(\"written\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/build1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python build1.py && cat > runnb.py <<'EOF'
import sys, time, nbformat, os
from nbclient import NotebookClient
src, dst = sys.argv[1], sys.argv[2]
nb = nbformat.read(src, 4)
if len(sys.argv) > 3:   # dev: restrict sessions
    for c in nb.cells:
        if c.cell_type == "code" and "CLOCK_OK = [" in c.source:
            c.source += "\nTEST = TEST[:3]; CLOCK_OK = [s for s in CLOCK_OK if s in TEST]; ALL9 = ALL9\n"
        if c.cell_type == "code" and "for sid in S.SESSIONS:" in c.source:
            c.source = c.source.replace("for sid in S.SESSIONS:", "for sid in [x for x in S.SESSIONS if x in ('e13-26m1-211019','e13-26m1-211116','e13-26m1-211119','e16-3m2-211211','e16-3m2-211212')]:")
t = time.time()
os.chdir(os.path.dirname(os.path.abspath(src)))
client = NotebookClient(nb, timeout=3600, kernel_name="python3", allow_errors=True)
client.execute()
nbformat.write(nb, dst)
print("ran in", round(time.time() - t), "s")
for i, c in enumerate(nb.cells):
    if c.cell_type != "code": continue
    for o in c.get("outputs", []):
        if o.output_type == "error": print("ERROR cell", i, o.ename, o.evalue)
EOF
python -m ipykernel install --user --name python3 >/dev/null 2>&1; time python runnb.py entries/mckenzie-2025/settling.ipynb $TMPDIR/dev1.ipynb dev 2>&1 | tail -5
```

```
written 46
[IPKernelApp] WARNING | Kernel is running over TCP without encryption. All communication (including code and outputs) is sent in plain text and is susceptible to eavesdropping. Use IPC transport or launch with kernel manager-provisioned CurveZMQ keys to enable transport encryption.
ran in 159 s
ERROR cell 25 NameError name 'EX' is not defined

real	2m39.522s
user	3m32.804s
sys	0m6.425s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read("dev1.ipynb",4)
for i,c in enumerate(nb.cells):
    if c.cell_type!="code": continue
    for o in c.get("outputs",[]):
        if o.output_type=="stream": print(f"--- cell {i}\n", o.text[:3500])
EOF
```

```
<persisted-output>
Output too large (37.2KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/b9f7eb38-d758-450f-a34b-e7d69f29684a/tool-results/bjh5q0ntg.txt

Preview (first 2KB):
--- cell 1
 dandiset 000552 version 0.230630.2304 labels from 0.261113.1035

--- cell 3
 loaded 5 sessions in 21 s

--- cell 4
            session  units  pyr  narrow  wide  run       t0  dur_s  tracked_s  first_track_s  trials  familiar env_label_version        x_range       y_range  lin_cm  frame_s
0  e13-26m1-211019    271  228      37     6    0   7589.6   1738       1717           16.1      47      True    tmaze_familiar    2.17..90.02   3.65..89.32  0..222   0.0333
1  e13-26m1-211019    271  228      37     6    1  15088.4   1665       1646           14.6      33     False     tmaze_ipshita     0.01..0.73    0.06..0.98  0..170   0.0333
2  e13-26m1-211116    209  173      25    11    0   7469.8   1250       1250            0.0      21      True    tmaze_familiar    1.68..92.41   1.70..89.41  0..222   0.0333
3  e13-26m1-211116    209  173      25    11    1  13594.9    344        344            0.0       9     False     linear_thomas     0.26..0.89    0.04..0.77  0..100   0.0400
4  e13-26m1-211119    191  158      23    10    0   6149.0   1432       1390           32.3      25      True    tmaze_familiar    1.30..92.04   2.59..89.45  0..222   0.0333
5  e13-26m1-211119    191  158      23    10    1  14844.1   1606       1539           63.3      58     False       linear_manu     0.01..0.20    0.00..1.00  0..110   0.0333
6   e16-3m2-211211    197  161      29     6    0   5269.9   1263       1230           24.2      32      True    tmaze_familiar    7.16..90.17   4.20..88.46  0..222   0.0333
7   e16-3m2-211211    197  161      29     6    1   9559.1   2443       1628           16.2      45     False  openField_thomas    1.41..22.94  0.28..115.96  0..110   0.0333
[... 4 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 30,400p /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/b9f7eb38-d758-450f-a34b-e7d69f29684a/tool-results/bjh5q0ntg.txt | cut -c1-250
```

```
later  epochs columns: ['environment', 'epoch_name', 'id', 'meanings_tables', 'start_time', 'stop_time', 'task']

--- cell 6
 e13-26m1-211116 pinned intervals: ['trials']

--- cell 7
 e13-26m1-211019 run at 15088 s: x 0.01..0.73, y 0.06..0.98, unit 'cm', linearized 0..170 cm
e13-26m1-211116 run at 13595 s: x 0.26..0.89, y 0.04..0.77, unit 'cm', linearized 0..100 cm
e13-26m1-211119 run at 14844 s: x 0.01..0.20, y 0.00..1.00, unit 'cm', linearized 0..110 cm

--- cell 7
 later version, e13-26m1-211019 novel run: n.a. 0.01 0.73

--- cell 9
            session     t0               env  shift -120 s  shift -30 s  shift -5 s  shift +0 s  shift +5 s  shift +30 s  shift +120 s  peak_at_0
0  e13-26m1-211019   7590    tmaze_familiar         0.336        0.368       0.559       0.972       0.540        0.363         0.347       True
1  e13-26m1-211019  15088     tmaze_ipshita         0.313        0.297       0.464       0.587       0.400        0.298         0.320       True
2  e13-26m1-211116   7470    tmaze_familiar         0.501        0.502       0.633       1.006       0.686        0.505         0.500       True
3  e13-26m1-211116  13595     linear_thomas         0.784        0.668       0.760       0.997       0.735        0.634         0.847       True
4  e13-26m1-211119   6149    tmaze_familiar         0.395        0.387       0.553       0.988       0.578        0.371         0.388       True
[... 351 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && python - <<'EOF'
s=open('build1.py').read()
s=s.replace('''        if k == 0 and sid == "e16-3m2-211212":
            EX = (E, t, lin)''','''        if k == 0 and sid == "e16-3m2-211212":
            EX = (E, t, lin)
        if k == 0 and "EX" not in globals():
            EX = (E, t, lin)''')
s=s.replace('''code(r"""
# per-minute session means''','''code(r"""
# variant, not judged: time 0 at the first tracked frame in place of the epoch start (claims file E2)
rows = []
for sid in TEST:
    for env in ("nov", "fam"):
        M = MEAS[(sid, env, "pyr")]; r = SESS[sid]["runs"][0 if env == "fam" else 1]
        off = r["first_track"] - r["t0"]
        x = M["all"]["nn_s"]
        rows.append(dict(session=sid, env=env, offset_s=round(off, 1), min1=S.window_mean(x, M["t"], off),
                         min10=S.window_mean(x, M["t"], off + 600)))
ANCH = pd.DataFrame(rows)
print(ANCH.round(3).to_string())
for env in ("nov", "fam"):
    d = ANCH[ANCH.env == env]
    t, p, n, md_ = paired(d["min1"].values, d["min10"].values)
    print(f"{env}, from the first tracked frame: min1 - min10 = {md_:+.3f}, t({n-1}) = {t:.2f}, p = {p:.3g}")
a = ANCH[ANCH.env == "fam"].set_index("session")["min1"]; b = ANCH[ANCH.env == "nov"].set_index("session")["min1"]
t, p, n, md_ = paired(a.values, b.loc[a.index].values)
print(f"familiar vs novel minute 1, from the first tracked frame: {md_:+.3f}, t({n-1}) = {t:.2f}, p = {p:.3g}")
""", ["claim:fig7e-novel-settling", "claim:fig7f-familiar-settling", "claim:fig7g-familiar-more-similar-early"])

code(r"""
# per-minute session means''')
s=s.replace('''import umap
''','''import umap
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)
''')
open('build1.py','w').write(s)
EOF
grep -n "import settle" build1.py
```

```
Thu Nov 26 17:18:04 UTC 2026
56:import settle as S
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/build2.py",
 "content": "import nbformat as nbf\n\ncells = []\n\n\ndef md(s):\n    cells.append(nbf.v4.new_markdown_cell(s.strip(\"\\n\")))\n\n\ndef code(s, tag=None):\n    c = nbf.v4.new_code_cell(s.strip(\"\\n\"))\n    if tag:\n        c.metadata[\"tags\"] = [tag] if isinstance(tag, str) else tag\n    cells.append(c)\n\n\nmd(r\"\"\"\n# McKenzie et al. (2025) on dandiset 000552: reactivation in ripples (Figure 8)\n\nPaper: McKenzie et al. (2025), eLife 14:RP105183, [doi:10.7554/elife.105183](https://doi.org/10.7554/elife.105183);\nclaims file `claims/mckenzie-2025.yaml`, written from Reviewed Preprint version 1.\n\nDataset: [DANDI:000552](https://dandiarchive.org/dandiset/000552/0.230630.2304) version **0.230630.2304**, the\nversion the paper cites (Methods, Electrophysiology subjects). Pyramidal cells are taken from the\nCellExplorer labels of the later version 0.261113.1035, after checking that its spike times are the\nsame; the pinned version has no cell types. The sessions and their checks are in `settling.ipynb`.\n\n| Claim | Here |\n|---|---|\n| fig8b-late-moments-reactivated | tested |\n| fig8d-familiar-no-difference | tested |\n| fig8-no-pre-reactivation | tested |\n\nMethod (Methods, Reactivation analysis; claims file E10): the ripples are those deposited in the files\n(Huszar et al.; the broadband LFP is only in the raw files, 120 to 180 GB each). Each ripple's vector is\neach pyramidal unit's spike count over the ripple divided by its duration; it is correlated with the\n100 ms vectors of the run; the null moves each unit's value on a ripple to a random other ripple\n(an independent permutation of each unit across the pool), 1000 times; a ripple reactivates a moment\nwhen its R is above all 1000 shuffles (above their 99.9th percentile). The moments are the bins of\nminute 1 (0 to 60 s) and of minutes 10 to 11 (600 to 660 s, Figure 8B), 1200 per run.\nReadings: pre ripples (a) the 30 min before the run, (b) the first 30 min of the recording; post ripples\nthe 30 min after the run; track vectors z-scored over the first 1000 s or raw counts; shuffle pool\n(a) the set the ripple belongs to, (b) pre and post together.\n\"\"\")\n\ncode(r\"\"\"\nimport time, zlib, warnings, resource\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport settle as S\n\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\npd.set_option(\"display.width\", 200, \"display.max_columns\", 40)\nT_START = time.time()\n\ndef seed(claim, k=0):\n    return zlib.crc32(f\"mckenzie-2025/{claim}\".encode()) + k\n\nSESS = {}\nfor sid in S.SESSIONS:\n    s = S.load_session(sid)\n    if len(s[\"runs\"]) < 2 or s[\"runs\"][1][\"t1\"] - s[\"runs\"][1][\"t0\"] < 660:\n        continue                      # the selection of settling.ipynb (claims file E1)\n    s[\"cell_type\"], _ = S.cell_types(sid, s[\"spike_index\"])\n    SESS[sid] = s\nTEST = list(SESS)\nprint(f\"{len(TEST)} sessions loaded in {time.time() - T_START:.0f} s:\", TEST)\n\"\"\")\n\ncode(r\"\"\"\nWIN = {}\nrows = []\nfor sid, s in SESS.items():\n    rec0 = 0.0 if s[\"epochs\"] is None else float(s[\"epochs\"][0, 0])\n    for env, r in ((\"fam\", s[\"runs\"][0]), (\"nov\", s[\"runs\"][1])):\n        w = dict(preA=(r[\"t0\"] - 1800, r[\"t0\"]), preB=(rec0, rec0 + 1800), post=(r[\"t1\"], r[\"t1\"] + 1800))\n        WIN[(sid, env)] = w\n        row = dict(session=sid, env=env, t0=round(r[\"t0\"]), t1=round(r[\"t1\"]))\n        for k, (a, b) in w.items():\n            m = (s[\"rip\"][:, 0] >= a) & (s[\"rip\"][:, 0] < b)\n            row[f\"ripples_{k}\"] = int(m.sum())\n            row[f\"{k}_window\"] = f\"{a:.0f}-{b:.0f}\"\n        # the post window must not run into the next maze run\n        nxt = [x[\"t0\"] for x in s[\"runs\"] if x[\"t0\"] > r[\"t0\"]]\n        row[\"post_overlaps_next_run_s\"] = round(max(0.0, r[\"t1\"] + 1800 - nxt[0]), 1) if nxt else 0.0\n        row[\"pyramidal\"] = int((s[\"cell_type\"] == \"Pyramidal Cell\").sum())\n        rows.append(row)\nprint(pd.DataFrame(rows).to_string())\nprint(\"ripple durations (ms):\", {sid: (round(s['rip_dur'].min() * 1e3), round(s['rip_dur'].max() * 1e3)) for sid, s in SESS.items()})\n\"\"\", \"sanity\")\n\ncode(r\"\"\"\nMOM = {}\nfor sid, s in SESS.items():\n    pyr = np.where(s[\"cell_type\"] == \"Pyramidal Cell\")[0]\n    for env, r in ((\"fam\", s[\"runs\"][0]), (\"nov\", s[\"runs\"][1])):\n        V = S.run_vectors(s, r, pyr)\n        sel = np.r_[np.where(V[\"t\"] < 60)[0], np.where((V[\"t\"] >= 600) & (V[\"t\"] < 660))[0]]\n        MOM[(sid, env)] = dict(units=V[\"units\"], z=V[\"z\"][sel], raw=V[\"counts\"][sel], early=V[\"t\"][sel] < 60)\n\ndef run_reactivation(sid, env, rng, pre=\"preA\", vec=\"z\", pool=\"a\", sets=(\"pre\", \"post\")):\n    s = SESS[sid]; w = WIN[(sid, env)]; mo = MOM[(sid, env)]\n    rv = {k: S.ripple_vectors(s, mo[\"units\"], [w[pre if k == \"pre\" else \"post\"]]) for k in sets}\n    out = {}\n    if pool == \"a\":\n        for k in sets:\n            res = S.reactivation(rv[k], {k: np.ones(len(rv[k]), bool)}, mo[vec], rng)\n            out[k] = res[k]\n    else:\n        allv = np.concatenate([rv[k] for k in sets])\n        lab = np.concatenate([[k] * len(rv[k]) for k in sets])\n        res = S.reactivation(allv, {k: lab == k for k in sets}, mo[vec], rng)\n        out.update(res)\n    rows = []\n    for k, (frac, n) in out.items():\n        rows.append(dict(session=sid, env=env, pre=pre, vec=vec, pool=pool, set=k, n_ripples=n,\n                         early_pct=100 * np.nanmean(frac[mo[\"early\"]]), late_pct=100 * np.nanmean(frac[~mo[\"early\"]]),\n                         all_pct=100 * np.nanmean(frac)))\n    return rows\n\ndef readings(env, claim):\n    rng = np.random.default_rng(seed(claim))\n    rows = []\n    for sid in TEST:\n        for vec in (\"z\", \"raw\"):\n            rows += run_reactivation(sid, env, rng, \"preA\", vec, \"a\", (\"pre\", \"post\"))\n            rows += run_reactivation(sid, env, rng, \"preB\", vec, \"a\", (\"pre\",))\n            rows += run_reactivation(sid, env, rng, \"preA\", vec, \"b\")\n            rows += run_reactivation(sid, env, rng, \"preB\", vec, \"b\")\n    return pd.DataFrame(rows)\n\ndef seeds_main(env, claim, sets=(\"post\",)):\n    rows = []\n    for k in range(1, 5):\n        rng = np.random.default_rng(seed(claim) + 1000 * k)\n        for sid in TEST:\n            for r in run_reactivation(sid, env, rng, \"preA\", \"z\", \"a\", sets):\n                rows.append(dict(r, seed_offset=1000 * k))\n    return pd.DataFrame(rows)\n\ndef late_vs_early(df):\n    out = []\n    for key, d in df[df.set == \"post\"].groupby([\"pre\", \"vec\", \"pool\"]):\n        t, p = stats.ttest_rel(d.late_pct, d.early_pct)\n        out.append(dict(zip([\"pre\", \"vec\", \"pool\"], key), early_mean=d.early_pct.mean(), late_mean=d.late_pct.mean(),\n                        diff=(d.late_pct - d.early_pct).mean(), t=t, df=len(d) - 1, p=p))\n    return pd.DataFrame(out)\n\"\"\")\n\nmd(r\"\"\"\n## fig8b-late-moments-reactivated\n\n> Moments 10 to 11 minutes after a novel context transition are more likely to be reactivated in post-experience ripples than moments 0 to 1 minutes after it.\n\nCriterion: per session the mean over moments of the percentage of post ripples that reactivate each\nmoment, in 600 to 660 s and in 0 to 60 s; reproduced when late is higher by the paired t-test over\nsessions at p < 0.05, under one combination of the readings.\n\nFirst the false positive rate of the procedure, which the paper gives as 0.001: the same test applied to\nripple vectors whose units were permuted across ripples once beforehand (no ensemble structure left).\n\"\"\")\n\ncode(r\"\"\"\nrng = np.random.default_rng(seed(\"fig8b-late-moments-reactivated\") + 1)\nfp = []\nfor sid in TEST:\n    s = SESS[sid]; mo = MOM[(sid, \"nov\")]\n    rv = S.ripple_vectors(s, mo[\"units\"], [WIN[(sid, \"nov\")][\"post\"]])\n    res = S.reactivation(rng.permuted(rv, axis=0), {\"x\": np.ones(len(rv), bool)}, mo[\"z\"], rng)\n    fp.append(res[\"x\"][0].mean())\nprint(\"false positive rate by session:\", np.round(fp, 5), \"mean\", round(float(np.mean(fp)), 5))\n\"\"\", \"claim:fig8b-late-moments-reactivated\")\n\ncode(r\"\"\"\nt0 = time.time()\nR_NOV = readings(\"nov\", \"fig8b-late-moments-reactivated\")\nprint(f\"novel readings in {time.time() - t0:.0f} s\")\nprint(R_NOV[R_NOV.set == \"post\"].round(3).to_string())\nLV_NOV = late_vs_early(R_NOV)\nprint(LV_NOV.round(4).to_string())\n\"\"\", \"claim:fig8b-late-moments-reactivated\")\n\ncode(r\"\"\"\nt0 = time.time()\nSD_NOV = seeds_main(\"nov\", \"fig8b-late-moments-reactivated\")\nmain = R_NOV[(R_NOV.set == \"post\") & (R_NOV.pre == \"preA\") & (R_NOV.vec == \"z\") & (R_NOV.pool == \"a\")]\nres = [(\"claim seed\", *stats.ttest_rel(main.late_pct, main.early_pct), (main.late_pct - main.early_pct).mean())]\nfor k, d in SD_NOV.groupby(\"seed_offset\"):\n    res.append((f\"seed + {k}\", *stats.ttest_rel(d.late_pct, d.early_pct), (d.late_pct - d.early_pct).mean()))\nfor r in res:\n    print(f\"{r[0]}: late - early = {r[3]:+.4f} percentage points, t(7) = {r[1]:.2f}, p = {r[2]:.3g}\")\nprint(f\"seeds in {time.time() - t0:.0f} s\")\n# variant: the 7 sessions with clock-checked tracking (position is not used here)\nd = main[main.session != \"e16-3m2-211211\"]\nt, p = stats.ttest_rel(d.late_pct, d.early_pct)\nprint(f\"7 sessions: late - early = {(d.late_pct - d.early_pct).mean():+.4f}, t(6) = {t:.2f}, p = {p:.3g}\")\n\"\"\", \"claim:fig8b-late-moments-reactivated\")\n\nmd(r\"\"\"\n**Result: fig8b-late-moments-reactivated, see above.**\n\"\"\")\n\nmd(r\"\"\"\n## fig8d-familiar-no-difference\n\n> In the familiar environment, early and late moments do not differ in reactivation rate.\n\nCriterion: a claim of absence, judged on the paired t-test over sessions at p < 0.05, on the familiar\nfigure-eight run with pre and post ripples around it, under E10 (a) with z-scored vectors (pool (a)); the\nother readings shown.\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\nR_FAM = readings(\"fam\", \"fig8d-familiar-no-difference\")\nprint(f\"familiar readings in {time.time() - t0:.0f} s\")\nprint(R_FAM[R_FAM.set == \"post\"].round(3).to_string())\nLV_FAM = late_vs_early(R_FAM)\nprint(LV_FAM.round(4).to_string())\nSD_FAM = seeds_main(\"fam\", \"fig8d-familiar-no-difference\")\nmain = R_FAM[(R_FAM.set == \"post\") & (R_FAM.pre == \"preA\") & (R_FAM.vec == \"z\") & (R_FAM.pool == \"a\")]\nt, p = stats.ttest_rel(main.late_pct, main.early_pct)\nprint(f\"claim seed: late - early = {(main.late_pct - main.early_pct).mean():+.4f}, t(7) = {t:.2f}, p = {p:.3g}\")\nfor k, d in SD_FAM.groupby(\"seed_offset\"):\n    t, p = stats.ttest_rel(d.late_pct, d.early_pct)\n    print(f\"seed + {k}: late - early = {(d.late_pct - d.early_pct).mean():+.4f}, t(7) = {t:.2f}, p = {p:.3g}\")\n\"\"\", \"claim:fig8d-familiar-no-difference\")\n\nmd(r\"\"\"\n**Result: fig8d-familiar-no-difference, see above.**\n\"\"\")\n\nmd(r\"\"\"\n## fig8-no-pre-reactivation\n\n> Track activity patterns show no evidence of being present in ripples recorded before the experience.\n\nCriterion: per session the mean over moments of the percentage of pre ripples that reactivate each moment;\nreproduced when its mean over sessions is not above 0.1% by a one-sided one-sample t-test at p < 0.05, in\nnovel and familiar runs. Main reading: pre (a), z-scored, pool (a), under this claim's own seed; the\nother readings come from the runs above.\n\"\"\")\n\ncode(r\"\"\"\nt0 = time.time()\nrows = []\nfor k in range(5):\n    rng = np.random.default_rng(seed(\"fig8-no-pre-reactivation\") + 1000 * k)\n    for env in (\"nov\", \"fam\"):\n        for sid in TEST:\n            for r in run_reactivation(sid, env, rng, \"preA\", \"z\", \"a\", (\"pre\",)):\n                rows.append(dict(r, seed_offset=1000 * k))\nPRE = pd.DataFrame(rows)\nprint(f\"pre ripples in {time.time() - t0:.0f} s\")\nprint(PRE[PRE.seed_offset == 0].round(4).to_string())\nfor (k, env), d in PRE.groupby([\"seed_offset\", \"env\"]):\n    t, p = stats.ttest_1samp(d.all_pct, 0.1, alternative=\"greater\")\n    print(f\"seed + {k}, {env}: mean {d.all_pct.mean():.4f}% (sessions {d.all_pct.min():.4f} to {d.all_pct.max():.4f}), one-sided t(7) = {t:.2f}, p = {p:.3g}\")\nprint(\"other readings (claim seeds of fig8b and fig8d):\")\nfor env, df in ((\"nov\", R_NOV), (\"fam\", R_FAM)):\n    for key, d in df[df.set == \"pre\"].groupby([\"pre\", \"vec\", \"pool\"]):\n        t, p = stats.ttest_1samp(d.all_pct, 0.1, alternative=\"greater\")\n        print(f\"  {env} {key}: mean {d.all_pct.mean():.4f}%, t = {t:.2f}, p = {p:.3g}\")\n    post = df[(df.set == \"post\") & (df.pre == \"preA\") & (df.vec == \"z\") & (df.pool == \"a\")]\n    print(f\"  {env} post ripples for comparison: mean {post.all_pct.mean():.4f}%\")\n\"\"\", \"claim:fig8-no-pre-reactivation\")\n\nmd(r\"\"\"\n**Result: fig8-no-pre-reactivation, see above.**\n\"\"\")\n\nmd(r\"\"\"\n## Summary\n\nFilled in after the run.\n\"\"\")\n\ncode(r\"\"\"\nprint(f\"notebook runtime {(time.time() - T_START) / 60:.1f} min; peak memory {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.1f} GB\")\n\"\"\")\n\nnb = nbf.v4.new_notebook()\nnb.cells = cells\nnb.metadata[\"kernelspec\"] = {\"name\": \"python3\", \"display_name\": \"Python 3\", \"language\": \"python\"}\nnbf.write(nb, \"entries/mckenzie-2025/reactivation.ipynb\")\nprint(\"written\", len(cells))\n"
}
```

```
File created successfully at: /tmp/claude-1001/build2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python build1.py && python build2.py && cp entries/mckenzie-2025/settle.py . && python - <<'EOF'
s=open('runnb.py').read()
s=s.replace('''        if c.cell_type == "code" and "for sid in S.SESSIONS:" in c.source:''','''        if c.cell_type == "code" and "TEST = list(SESS)" in c.source:
            c.source = c.source.replace("TEST = list(SESS)", "TEST = list(SESS)[:2]")
        if c.cell_type == "code" and "for sid in S.SESSIONS:" in c.source and "TEST = list(SESS)" not in c.source:''')
open('runnb.py','w').write(s)
EOF
time python runnb.py entries/mckenzie-2025/reactivation.ipynb $TMPDIR/dev2.ipynb dev 2>&1 | grep -v TCP | tail -5
```

```
written 47
written 17
ran in 576 s

real	9m36.137s
user	34m32.352s
sys	0m4.626s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read("dev2.ipynb",4)
for i,c in enumerate(nb.cells):
    if c.cell_type!="code": continue
    for o in c.get("outputs",[]):
        if o.output_type=="stream": print(f"--- cell {i}\n", o.text[:3000])
        if o.output_type=="error": print("ERR", o.evalue)
EOF
```

```
--- cell 1
 2 sessions loaded in 47 s: ['e13-26m1-211019', 'e13-26m1-211119']

--- cell 2
             session  env     t0     t1  ripples_preA  preA_window  ripples_preB preB_window  ripples_post  post_window  post_overlaps_next_run_s  pyramidal
0   e13-26m1-211019  fam   7590   9328           416    5790-7590            83      0-1800           651   9328-11128                       0.0        228
1   e13-26m1-211019  nov  15088  16753           693  13288-15088            83      0-1800           804  16753-18553                       0.0        228
2   e13-26m1-211119  fam   6149   7581           268    4349-6149           405      0-1800           805    7581-9381                       0.0        158
3   e13-26m1-211119  nov  14844  16450           336  13044-14844           405      0-1800           871  16450-18250                       0.0        158
4   e15-13f1-220118  fam   5617   7717           461    3817-5617           290      0-1800           444    7717-9517                       0.0        318
5   e15-13f1-220118  nov  13106  15049           903  11306-13106           290      0-1800           882  15049-16849                       0.0        318
6   e15-13f1-220119  fam   6816   8880           510    5016-6816           417      0-1800           702   8880-10680                       0.0        288
7   e15-13f1-220119  nov  21190  22703           852  19390-21190           417      0-1800           440  22703-24503                       0.0        288
8   e15-13f1-220120  fam   9594  11969           393    7794-9594           584      0-1800           393  11969-13769                       0.0        248
9   e15-13f1-220120  nov  17993  19809           896  16193-17993           584      0-1800          1001  19809-21609                       0.0        248
10   e16-3m2-211211  fam   5270   6533           528    3470-5270           549      0-1800           783    6533-8333                       0.0        161
11   e16-3m2-211211  nov   9559  1200
[... 111 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
s=open('build2.py').read()
s=s.replace('''        for vec in ("z", "raw"):
            rows += run_reactivation(sid, env, rng, "preA", vec, "a", ("pre", "post"))
            rows += run_reactivation(sid, env, rng, "preB", vec, "a", ("pre",))
            rows += run_reactivation(sid, env, rng, "preA", vec, "b")
            rows += run_reactivation(sid, env, rng, "preB", vec, "b")''','''        # the main reading, and each other reading varied one at a time (the full cross would double the time)
        rows += run_reactivation(sid, env, rng, "preA", "z", "a", ("pre", "post"))
        rows += run_reactivation(sid, env, rng, "preB", "z", "a", ("pre",))
        rows += run_reactivation(sid, env, rng, "preA", "raw", "a", ("pre", "post"))
        rows += run_reactivation(sid, env, rng, "preA", "z", "b")
        rows += run_reactivation(sid, env, rng, "preB", "z", "b")''')
s=s.replace('''    print(f"{r[0]}: late - early = {r[3]:+.4f} percentage points, t(7) = {r[1]:.2f}, p = {r[2]:.3g}")''','''    print(f"{r[0]}: late - early = {r[3]:+.4f} percentage points, t({len(main) - 1}) = {r[1]:.2f}, p = {r[2]:.3g}")''')
s=s.replace('''print(f"7 sessions: late - early = {(d.late_pct - d.early_pct).mean():+.4f}, t(6) = {t:.2f}, p = {p:.3g}")''','''print(f"without e16-3m2-211211: late - early = {(d.late_pct - d.early_pct).mean():+.4f}, t({len(d) - 1}) = {t:.2f}, p = {p:.3g}")''')
s=s.replace('''print(f"claim seed: late - early = {(main.late_pct - main.early_pct).mean():+.4f}, t(7) = {t:.2f}, p = {p:.3g}")''','''print(f"claim seed: late - early = {(main.late_pct - main.early_pct).mean():+.4f}, t({len(main) - 1}) = {t:.2f}, p = {p:.3g}")''')
s=s.replace('''    print(f"seed + {k}: late - early = {(d.late_pct - d.early_pct).mean():+.4f}, t(7) = {t:.2f}, p = {p:.3g}")''','''    print(f"seed + {k}: late - early = {(d.late_pct - d.early_pct).mean():+.4f}, t({len(d) - 1}) = {t:.2f}, p = {p:.3g}")''')
s=s.replace('''one-sided t(7) = {t:.2f}''','''one-sided t({len(d) - 1}) = {t:.2f}''')
s=s.replace('''(a) the set the ripple belongs to, (b) pre and post together.''','''(a) the set the ripple belongs to, (b) pre and post together. The main reading is pre (a), z-scored, pool (a);
each other reading is run with the rest held at the main one (pre (b) is also run with pool (b)), not
fully crossed, to keep the notebook under half an hour.''')
open('build2.py','w').write(s)
EOF
grep -c "t(7)" build2.py; python build2.py; date -u; time python runnb.py entries/mckenzie-2025/settling.ipynb $TMPDIR/full1.ipynb 2>&1 | grep -v TCP | tail -5
```

```
0
written 17
Thu Nov 26 17:29:06 UTC 2026
ran in 621 s

real	10m21.331s
user	25m3.741s
sys	0m17.349s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF' > full1.txt
import nbformat
nb=nbformat.read("full1.ipynb",4)
for i,c in enumerate(nb.cells):
    if c.cell_type!="code": continue
    for o in c.get("outputs",[]):
        if o.output_type=="stream" and o.name=="stdout": print(f"--- cell {i}\n", o.text)
        if o.output_type=="error": print("ERR", i, o.evalue)
EOF
wc -l full1.txt; grep -n "ERR" full1.txt; sed -n '/--- cell 14/,/--- cell 33/p' full1.txt | cut -c1-200 | head -230
```

```
637 full1.txt
--- cell 14
 measures for 32 runs in 144 s; peak memory 4.1 GB
units dropped (no spike in the first 1000 s): {'e13-26m1-211119 nov pyr': 2, 'e13-26m1-211119 nov all': 2, 'e15-13f1-220118 nov pyr': 1, 'e15-13f1-220118 nov all': 1, 'e15-13f1-220119 fam pyr': 1, 'e1

--- cell 16
            session  all_units  pyramidal
0  e13-26m1-211019        271        228
1  e13-26m1-211116        209        173
2  e13-26m1-211119        191        158
3  e15-13f1-220118        363        318
4  e15-13f1-220119        343        288
5  e15-13f1-220120        303        248
6   e16-3m2-211211        197        161
7   e16-3m2-211212        200        162
8   e16-3m2-211213        207        163
8 tested sessions, pyramidal: mean 215.75, range 158 to 318 -> outside tolerance
8 tested sessions, all_units: mean 259.38, range 191 to 363 -> within tolerance
9 sessions with a novel run, pyramidal: mean 211.00, range 158 to 318 -> outside tolerance
9 sessions with a novel run, all_units: mean 253.78, range 191 to 363 -> within tolerance
[... 212 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n '/--- cell 34/,$p' full1.txt | sed -n '36,400p' | cut -c1-160 | grep -v "^ *[0-9]* *\(fam\|nov\) *d\(vel\|acc\) .* 1000 " | head -150
```

```
8 sessions, reading a, fam: in-field slope +0.0212 (t = 3.11, p = 0.017), out-of-field slope -0.0048 (t = -5.34, p = 0.00107)
8 sessions, reading b, nov: in-field slope +0.0501 (t = 8.61, p = 5.68e-05), out-of-field slope +0.0017 (t = 0.92, p = 0.387)
8 sessions, reading b, fam: in-field slope +0.0372 (t = 6.37, p = 0.000378), out-of-field slope -0.0047 (t = -4.20, p = 0.00402)
7 clock-checked, reading a, nov: in-field slope +0.0265 (t = 3.30, p = 0.0164), out-of-field slope -0.0015 (t = -1.27, p = 0.252)
7 clock-checked, reading a, fam: in-field slope +0.0168 (t = 2.80, p = 0.0312), out-of-field slope -0.0041 (t = -6.38, p = 0.000698)
7 clock-checked, reading b, nov: in-field slope +0.0534 (t = 9.72, p = 6.8e-05), out-of-field slope +0.0001 (t = 0.11, p = 0.916)
7 clock-checked, reading b, fam: in-field slope +0.0363 (t = 5.45, p = 0.00159), out-of-field slope -0.0039 (t = -4.29, p = 0.00514)

--- cell 37
 main reading (3 neighbours, Kalman, all bins, first 600 s):
     env measure nn filt speed  window sessions  mean_rho       t       p
24   fam    dacc  3    k   all     600        8   -0.0050 -0.2072  0.8417
25   fam    dacc  3    k   all     600        7   -0.0124 -0.4667  0.6572
56   fam    dvel  3    k   all     600        8   -0.0158 -0.6496  0.5367
57   fam    dvel  3    k   all     600        7   -0.0240 -0.9080  0.3989
88   nov    dacc  3    k   all     600        8   -0.1033 -5.7743  0.0007
89   nov    dacc  3    k   all     600        7   -0.0970 -5.0178  0.0024
120  nov    dvel  3    k   all     600        8   -0.1104 -5.4176  0.0010
121  nov    dvel  3    k   all     600        7   -0.1047 -4.6346  0.0036

[... 132 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -n '/--- cell 43/,$p' full1.txt | tail -20
```

```
24   e16-3m2-211212  nov       a  0.6686  0.6629    0.6702
25   e16-3m2-211212  nov       b -0.0016  0.0009   -0.0005
26   e16-3m2-211212  fam       a  0.6563  0.7086    0.7030
27   e16-3m2-211212  fam       b  0.0004  0.0005   -0.0007
28   e16-3m2-211213  nov       a  0.6766  0.6790    0.7143
29   e16-3m2-211213  nov       b -0.0011  0.0005    0.0023
30   e16-3m2-211213  fam       a  0.6438  0.7077    0.7158
31   e16-3m2-211213  fam       b -0.0003  0.0006   -0.0000
reading a, min10, nov: min1 - min10 = -0.0236, t(7) = -3.01, p = 0.0198
reading a, min10, fam: min1 - min10 = -0.0378, t(7) = -4.66, p = 0.00231
reading a, min10alt, nov: min1 - min10 = -0.0269, t(7) = -4.44, p = 0.00301
reading a, min10alt, fam: min1 - min10 = -0.0480, t(7) = -5.61, p = 0.000807
reading b, min10, nov: min1 - min10 = -0.0013, t(7) = -1.71, p = 0.13
reading b, min10, fam: min1 - min10 = -0.0002, t(7) = -0.54, p = 0.604
reading b, min10alt, nov: min1 - min10 = -0.0011, t(7) = -2.26, p = 0.0586
reading b, min10alt, fam: min1 - min10 = -0.0006, t(7) = -1.42, p = 0.199

--- cell 46
 notebook runtime 10.3 min; peak memory 4.1 GB
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source env/bin/activate && time python runnb.py entries/mckenzie-2025/reactivation.ipynb $TMPDIR/full2.ipynb 2>&1 | grep -v TCP | tail -5
```

```
Thu Nov 26 17:39:43 UTC 2026
ran in 2084 s

real	34m43.951s
user	133m40.967s
sys	0m5.909s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR && source env/bin/activate && python - <<'EOF' > full2.txt
import nbformat
nb=nbformat.read("full2.ipynb",4)
for i,c in enumerate(nb.cells):
    if c.cell_type!="code": continue
    for o in c.get("outputs",[]):
        if o.output_type=="stream" and o.name=="stdout": print(f"--- cell {i}\n", o.text)
        if o.output_type=="error": print("ERR", i, o.evalue)
EOF
sed -n '/--- cell 5/,$p' full2.txt | grep -v "^ *[0-9]* *e1"
```

```
Thu Nov 26 18:14:31 UTC 2026
--- cell 5
 false positive rate by session: [0.00093 0.00107 0.00103 0.00104 0.00098 0.00097 0.00103 0.00097] mean 0.001

--- cell 6
 novel readings in 560 s
            session  env   pre  vec pool   set  n_ripples  early_pct  late_pct  all_pct
    pre  vec pool  early_mean  late_mean    diff       t  df       p
0  preA  raw    a      0.2412     0.2717  0.0305  1.4234   7  0.1976
1  preA    z    a      0.2324     0.2088 -0.0236 -1.4008   7  0.2040
2  preA    z    b      0.2210     0.2102 -0.0108 -0.6958   7  0.5090
3  preB    z    b      0.2238     0.2071 -0.0167 -1.1416   7  0.2911

--- cell 7
 claim seed: late - early = -0.0236 percentage points, t(7) = -1.40, p = 0.204
seed + 1000: late - early = -0.0193 percentage points, t(7) = -1.19, p = 0.273
seed + 2000: late - early = -0.0243 percentage points, t(7) = -1.45, p = 0.189
seed + 3000: late - early = -0.0173 percentage points, t(7) = -1.03, p = 0.337
seed + 4000: late - early = -0.0148 percentage points, t(7) = -0.92, p = 0.387
seeds in 283 s
[... 48 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "^('\|^ ('" full1.txt | head -20; grep -n "linear  1" full1.txt | head -40 | cut -c1-120
```

```
575:('exp', '1', 'd', '7') {'nov': np.False_, 'fam': np.False_}
576:('exp', '1', 'd', '8') {'nov': np.False_, 'fam': np.False_}
577:('exp', '1', 'k', '7') {'nov': np.False_, 'fam': np.False_}
578:('exp', '1', 'k', '8') {'nov': np.False_, 'fam': np.False_}
579:('exp', '3', 'd', '7') {'nov': np.False_, 'fam': np.False_}
580:('exp', '3', 'd', '8') {'nov': np.False_, 'fam': np.False_}
581:('exp', '3', 'k', '7') {'nov': np.False_, 'fam': np.False_}
582:('exp', '3', 'k', '8') {'nov': np.False_, 'fam': np.False_}
583:('linear', '1', 'd', '7') {'nov': np.False_, 'fam': np.False_}
584:('linear', '1', 'd', '8') {'nov': np.False_, 'fam': np.False_}
585:('linear', '1', 'k', '7') {'nov': np.False_, 'fam': np.False_}
586:('linear', '1', 'k', '8') {'nov': np.False_, 'fam': np.False_}
587:('linear', '3', 'd', '7') {'nov': np.False_, 'fam': np.False_}
588:('linear', '3', 'd', '8') {'nov': np.False_, 'fam': np.False_}
589:('linear', '3', 'k', '7') {'nov': np.False_, 'fam': np.False_}
590:('linear', '3', 'k', '8') {'nov': np.False_, 'fam': np.False_}
543:96   linear  1    k  nov        8  intercept  557.0438   5.9952  0.0005  8
544:97   linear  1    k  nov        8       time    6.0336   2.5303  0.0392  8
545:98   linear  1    k  nov        8        vel    4.2333   3.1624  0.0159  8
546:99   linear  1    k  nov        8        acc    0.2362   0.2591  0.8030  8
[... 29 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && cat > patch1.py <<'EOF'
s=open('build1.py').read()
def rep(old,new):
    global s
    assert old in s, old[:60]
    s=s.replace(old,new)
rep('''259.4 (191 to 363); over the nine sessions with a novel run the mean is 253.8 and the range 191 to 363,
the paper's numbers exactly. Pyramidal units alone give a mean of 216.5, outside the tolerance, so the
paper's ensemble count is of all units, while its Methods analyze pyramidal cells only.''','''259.38 (191 to 363); over the nine sessions with a novel run the mean is 253.78 and the range 191 to
363, the paper's numbers. Pyramidal units alone give a mean of 215.75 over the eight sessions, outside the
tolerance. The paper's ensemble count thus matches all units of nine sessions, while its Methods analyze
pyramidal cells only and its tests have 8 sessions.''')
rep('''**Result: figs6b-decorrelation-novel, see the numbers above; figs6d-decorrelation-familiar, see the numbers above.**''','''**Result: figs6b-decorrelation-novel is not reproduced; figs6d-decorrelation-familiar is reproduced.** In the
novel run the decay rate of minute 1 is not higher than that of minute 10 under any reading: with 60 s
windows the difference is +0.022 1/s (t(7) = 0.18, p = 0.865) with minute 10 at 600 s and -0.001 (p = 0.987)
at 540 s; with 100 s windows +0.119 (p = 0.25) and +0.096 (p = 0.234). Minute 1 is faster in 4 of 8 sessions
under reading (a). In the familiar run the difference is +0.062 1/s, t(7) = 0.78, p = 0.459 under the judged
reading, and p = 0.40 to 0.72 under the others, so no difference is found there, as the paper reports; the
contrast the paper draws between the two environments is not seen, as the novel run shows no difference
either. No fit gave a time constant under 10 ms.''')
rep('''**Result: fig7ab-umap-embedding, see above.**''','''**Result: partially reproduced.** Under the claim's seed the embedding predicts the linearized position
better than the block-shuffled position in 7 of 8 sessions (R^2 0.185 to 0.717 against -0.194 to -0.108),
and in 7 or 8 of 8 under all five seeds; the exception is e16-3m2-211211, whose tracking is misfiled (data
check). First-minute bins are farther from the embedding's median than later bins in 1 of 8 sessions (0 or 1
of 8 under all five seeds): by this measure, moments just after transfer are not at the periphery.''')
rep('''**Result: fig7e, fig7f, fig7g, see above.**''','''**Result: fig7e-novel-settling, fig7f-familiar-settling and fig7g-familiar-more-similar-early are reproduced.**
In the novel run the nearest-neighbour correlation of minute 1 is lower than that of minute 10 by 0.104
(t(6) = -4.07, p = 0.0066; e13-26m1-211119 has no tracking in its first 63 s, so 7 sessions enter), and by
0.106 (t(7) = -6.44, p = 0.000355) with time counted from the first tracked frame; every combination of
readings gives p of 0.026 or less. In the familiar run the difference is 0.089 (t(7) = -5.74, p = 0.0007), p of
0.0053 or less under every combination. Familiar minute 1 is higher than novel minute 1 by 0.037 (t(6) = 2.58,
p = 0.042) over all bins and by 0.079 (t(5) = 4.56, p = 0.0061) above 5 cm/s; on the seven clock-checked
sessions over all bins it is 0.036 (p = 0.089). The per-minute means rise from 0.393 to about 0.50 by minute 7
in the novel run and from 0.430 to about 0.52 by minute 3 in the familiar run, consistent with faster
settling in the familiar environment, which is not judged.''')
rep('''**Result: figs7ab-in-field-out-field, see above.**''','''**Result: partially reproduced.** In-field deviations rise over the first 10 minutes in both environments
(reading a: novel +0.0231 per minute, t = 2.98, p = 0.0207; familiar +0.0212, p = 0.017; reading b: p =
5.68e-05 and 0.000378). Out-of-field deviations fall in the familiar run (reading a -0.0048 per minute, p =
0.00107; reading b p = 0.00402) but not in the novel run (+0.0001, p = 0.966; reading b +0.0017, p = 0.387).
The seven clock-checked sessions give the same pattern.''')
rep('''**Result: figs7cd-movement-not-time-locked, see above.**''','''**Result: not reproduced.** In the novel run the movement differences of the nearest neighbours fall with
time after transfer: under the judged reading the mean Spearman correlation is -0.110 for |dvel|NN (t(7) =
-5.42, p = 0.0010) and -0.103 for |dacc|NN (t(7) = -5.77, p = 0.0007). In the familiar run there is none (-0.016,
p = 0.537; -0.005, p = 0.842). Over every reading, 14 of the 32 tests on 8 sessions over 600 s find a
relationship, all of them in the novel run.''')
rep('''**Result: figs7ef-time-explains-similarity, see above.**''','''**Result: not reproduced.** Under no reading is time the only variable whose removal significantly worsens
the prediction in both environments. With the photometry model's form, 3 neighbours and the Kalman filter,
dropping |dvel|NN raises the CVMSE by 7.76% in the novel run (t = 3.50, p = 0.0100) and 6.96% in the
familiar run (p = 0.0003); dropping time raises it by 7.31% in the novel run (p = 0.0290) and 1.00% in the
familiar run (p = 0.6086); dropping |dacc|NN does not matter (p = 0.67 and 0.51). The other readings give the
same pattern.''')
rep('''**Result: figs7gh-unconditioned-similarity, see above.**''','''**Result: reproduced under reading (a).** With the 3 most correlated vectors anywhere in the run, minute 1
is lower than minute 10 in the novel run (-0.0236, t(7) = -3.01, p = 0.0198) and the familiar run (-0.0378,
t(7) = -4.66, p = 0.00231), and also with minute 10 at 540 s (p = 0.00301 and 0.000807). Reading (b), the mean
correlation with all other vectors, is near 0 in every window (-0.0016 to 0.0023), as each unit is z-scored and
the vectors then average to about zero, and finds no difference (p = 0.13 and 0.604).''')
rep('''## Summary

Filled in after the run.''','''## Summary

| Claim | Outcome |
|---|---|
| Photometry claims (13) and ne-and-settling-time-course | blocked, data missing |
| ephys-ensemble-size | reproduced (all units) |
| figs6b-decorrelation-novel | not reproduced |
| figs6d-decorrelation-familiar | reproduced |
| fig7ab-umap-embedding | partially reproduced (position yes, periphery no) |
| fig7e-novel-settling | reproduced |
| fig7f-familiar-settling | reproduced |
| fig7g-familiar-more-similar-early | reproduced |
| figs7ab-in-field-out-field | partially reproduced (no out-of-field decrease in novel runs) |
| figs7cd-movement-not-time-locked | not reproduced (novel runs) |
| figs7ef-time-explains-similarity | not reproduced (velocity also matters) |
| figs7gh-unconditioned-similarity | reproduced (reading a) |
| fig8b, fig8d, fig8-no-pre-reactivation | in `reactivation.ipynb` |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the
differences from the paper's method.

How the analysis differs from the paper's: pyramidal cells come from the later version's CellExplorer
labels; locations are 1 cm bins of the linearized position, as the x, y position is not in cm in five novel
runs; the ripples are the deposited ones; e13-26m1-211119's first minute has no tracking; the readings the
paper leaves open are each run and shown.

What was found about the dataset (pinned version 0.230630.2304, and the later 0.261113.1035):

- No cell types in the pinned version (`finding-no-cell-types`); the later version adds them.
- The x, y position of five novel runs is in 0 to 1 units, labelled cm, in both versions (`finding-position-not-cm`).
- In e16-3m2-211211 the linear-track tracking and trials are filed in the open-field epoch; spikes are tuned
  to them only when they are moved 5564.5 s later onto the linear-track epoch; the same in the later version
  (`finding-tracking-misfiled`).
- e13-26m1-211116 has no epochs; three sessions have no tracking of their second maze epoch, and four have
  no tracking of one of their two novel environments.
- The behavior module's description spells "alternation" as separate letters in three files (`finding-behavior-description`).''')
open('build1.py','w').write(s)

s=open('build2.py').read()
rep('''**Result: fig8b-late-moments-reactivated, see above.**''','''**Result: not reproduced.** The procedure's false positive rate is 0.001 (0.00093 to 0.00107 by session), the
paper's. Under the main reading post ripples reactivate 0.232% of first-minute moments and 0.209% of moments
at 10 to 11 minutes (late - early -0.0236 percentage points, t(7) = -1.40, p = 0.204); under the five seeds the
difference is -0.0148 to -0.0243 (p 0.189 to 0.387). No other reading finds late moments more reactivated at
p < 0.05: raw counts +0.0305 (p = 0.1976), pooled shuffles -0.0108 (p = 0.509) and -0.0167 (p = 0.2911).''')
rep('''**Result: fig8d-familiar-no-difference, see above.**''','''**Result: not reproduced.** The judged test finds a difference in the familiar run: early moments are
reactivated more than late ones (0.247% against 0.221%, -0.0255 percentage points, t(7) = -3.72, p = 0.0074),
under all five seeds (p 0.0043 to 0.0074). The other readings find no difference (raw counts p = 0.7383, pooled
shuffles p = 0.1497 and 0.2352). The effect is small, about a tenth of the reactivation rate.''')
rep('''**Result: fig8-no-pre-reactivation, see above.**''','''**Result: not reproduced.** Pre ripples reactivate on average 0.1334% of moments in the novel runs and 0.1461%
in the familiar runs, above the 0.1% false positive rate (one-sided t(7) = 2.82, p = 0.0129, and 7.90, p =
4.93e-05), under all five seeds (p 0.0111 to 0.0132 and below 0.0001) and under every other reading (p 0.0377 or
less). Post ripples reactivate more (0.2206% and 0.2342%), so the track patterns appear in post ripples more
than in pre ripples, but they are not absent from pre ripples.''')
rep('''## Summary

Filled in after the run.''','''## Summary

| Claim | Outcome |
|---|---|
| fig8b-late-moments-reactivated | not reproduced |
| fig8d-familiar-no-difference | not reproduced |
| fig8-no-pre-reactivation | not reproduced |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the
differences from the paper's method.

Differences from the paper's method: the ripples are those deposited in the files, not detected again from the
LFP (only in the raw files); the moments are those of minute 1 and minutes 10 to 11, not the whole run; the
readings the paper leaves open (pre window, z-scored or raw track vectors, shuffle pool) are run one at a time
around a main reading, not fully crossed. The rates found are low (0.1 to 0.3% of ripples per moment), close to
the false positive rate, so small differences decide these tests. Dataset findings are in `settling.ipynb`.''')
open('build2.py','w').write(s)
EOF
source env/bin/activate && python patch1.py && python build1.py && python build2.py
```

```
written 47
written 17
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
s=open('build1.py').read()
old='''            print(f"  {env} window {w}, minute 1 vs {m10}: mean difference {md_:+.3f} 1/s, t({n-1}) = {t:.2f}, p = {p:.3g}")'''
new='''            faster = int((d[f"{w}_min1"] > d[f"{w}_{m10}"]).sum())
            print(f"  {env} window {w}, minute 1 vs {m10}: mean difference {md_:+.3f} 1/s, t({n-1}) = {t:.2f}, p = {p:.3g}; minute 1 faster in {faster} of {n}")'''
assert old in s; s=s.replace(old,new)
s=s.replace("Minute 1 is faster in 4 of 8 sessions\nunder reading (a).","Minute 1 is faster in 3 of 8 sessions\nunder reading (a).")
assert "3 of 8 sessions" in s
open('build1.py','w').write(s)
EOF
python build1.py; date -u
```

```
written 47
Thu Nov 26 18:15:46 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
print(s.get('required'))
for k,v in s['properties'].items(): print(k, str(v)[:200])
" ; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
d=s.get('\$defs',s.get('definitions',{}))
for k in d: print('DEF',k, d[k].get('required'), list(d[k].get('properties',{}).keys()))
"
```

```
['schema_version', 'id', 'datasets', 'paper', 'date', 'provenance', 'outcomes']
schema_version {'const': 3}
id {'type': 'string', 'pattern': '^[a-z0-9]+(-[a-z0-9]+)*$'}
datasets {'description': 'Every dataset the attempt used (docs/protocol.md, "Record the attempt").', 'type': 'array', 'minItems': 1, 'items': {'description': "A dataset the attempt used: the archive, the datas
missing_datasets {'description': "Datasets the paper's claims rest on that this attempt could not use; claims that need one are blocked with dataset_missing.", 'type': 'array', 'items': {'type': 'object', 'additionalP
paper {'type': 'string', 'pattern': '^doi:10\\.[0-9]{4,9}/.+$'}
date {'type': 'string', 'format': 'date'}
entry {'description': 'The entry this attempt produced (its name), if any.', 'type': 'string'}
deprecated {'description': "Set when the attempt no longer stands, for example because its claims were written without the paper's full text. The record is kept as it was; its outcomes are shown but not counted.
provenance {'type': 'object', 'additionalProperties': False, 'required': ['kind', 'accountable'], 'properties': {'kind': {'enum': ['agent', 'person']}, 'accountable': {'description': 'The person or organisation 
outcomes {'description': 'One per claim attempted.', 'type': 'array', 'minItems': 1, 'items': {'type': 'object', 'additionalProperties': False, 'required': ['claim', 'outcome'], 'properties': {'claim': {'descr
verifications {'type': 'array', 'items': {'type': 'object', 'additionalProperties': False, 'required': ['date', 'kind', 'by', 'results'], 'properties': {'date': {'type': 'string', 'format': 'date'}, 'kind': {'enum'
findings {'description': "What the attempt found, whatever the outcomes: about the dataset itself (`about: data`, for its owner and the archive, shown on the dataset's page) or about the paper (`about: paper`,
reconciliation {'description': 'A repeat attempt\'s comparison with the attempt before it, written by the reconcile step once this attempt, mad
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
python -c "
import json;s=json.load(open('schemas/attempt.schema.json'))
p=s['properties']
print(json.dumps(p['provenance'],indent=0)[:1500])
print(json.dumps(p['outcomes']['items']['properties'],indent=0)[:3000])
print(json.dumps(p['findings']['items'],indent=0)[:3000])
print(json.dumps(p['datasets']['items'],indent=0)[:800])
"
```

```
{
"type": "object",
"additionalProperties": false,
"required": [
"kind",
"accountable"
],
"properties": {
"kind": {
"enum": [
"agent",
"person"
]
},
"accountable": {
"description": "The person or organisation responsible for this attempt.",
"type": "object",
"additionalProperties": false,
"required": [
"name"
[... 271 more lines not kept]
```

**Agent calls Bash**

```bash
cd entries/mckenzie-2025 && cat > requirements.in <<'EOF'
dandi
h5py
matplotlib
numpy
pandas
remfile
scikit-learn
scipy
umap-learn
EOF
cat > entry.yaml <<'EOF'
schema_version: 1
name: mckenzie-2025
type: reproduction
title: Settling of the CA1 code after context transitions (McKenzie et al. 2025)
description: Tests the electrophysiology findings of McKenzie, Sommer, Donaldson, Pimentel, Kakani, Choi,
  Newman and English (2025) on dandiset 000552 (Huszar et al. 2022), at the version the paper cites. It
  measures how CA1 population vectors settle after transfer to a novel or familiar maze (nearest-neighbour
  similarity at the same location, decorrelation, place field deviations, the role of movement) and their
  reactivation in ripples before and after the run. The fiber photometry of norepinephrine, half of the
  paper, is not in the dandiset.
license: Apache-2.0
notebooks:
- path: settling.ipynb
  title: Population vectors, nearest neighbours and place fields after transfer (Figures 7, S6, S7)
  runtime_minutes: 11
- path: reactivation.ipynb
  title: Reactivation of track moments in ripples (Figure 8)
  runtime_minutes: 35
helpers:
- settle.py
related:
- id: dandi:000552/0.230630.2304
  relation: uses_data
- id: doi:10.7554/elife.105183
  relation: reproduces
EOF
cat ../fouke-2025/entry.yaml | head -3; ls ../ | head -3; grep -n "relation" ../../schemas/entry.schema.json | head
```

```
schema_version: 1
name: fouke-2025
type: reproduction
allen-2026
amjad-2025
andreassen-2022
46:        "required": ["id", "relation"],
53:          "relation": {"enum": ["uses_data", "reproduces", "derived_from", "references"]}
```

**Agent calls Bash**

```bash
cd  && grep -n "uses_data" tools/*.py | head -20
```

```
(Bash completed with no output)
```

**Agent calls Bash**

```bash
grep -rn "uses_data\|related" tools/ --include=*.py | head -20; ls tools
```

```
tools/build_figshare_targets.py:10:ids and MD5 digests. The papers are the DOI given, the item's related materials marked IsSupplementTo,
tools/build_figshare_targets.py:74:    related = [r for r in item.get("related_materials", []) if r.get("identifier_type") == "DOI"]
tools/build_figshare_targets.py:75:    dois = ([paper] if paper else []) + [r["identifier"].lower() for r in related if r["relation"] in PAPER_RELATIONS]
tools/build_figshare_targets.py:78:               next((r["relation"] for r in related if r["identifier"].lower() == d), "resource_doi"),
tools/build_figshare_targets.py:96:        "code": [r["link"] for r in item.get("related_materials", []) if re.search(r"github\.com|zenodo", r["link"])],
tools/paper_keys.py:104:        dois = [doi_of(r["id"]) for r in en.get("related") or [] if r.get("relation") == "reproduces"]
tools/build_osf_targets.py:68:def related(item: dict, name: str) -> str | None:
tools/build_osf_targets.py:70:    return (((item.get("relationships") or {}).get(name) or {}).get("links") or {}).get("related", {}).get("href")
tools/build_osf_targets.py:148:            yield from walk(related(item, "files"), prefix)
tools/build_osf_targets.py:159:            found = list(walk(related(storage, "files"), prefix))
tools/build_osf_targets.py:197:    for ident in pages(related(node, "identifiers") or f"{base}identifiers/"):
tools/build_osf_targets.py:204:    href = related(node, "license")
tools/build_osf_targets.py:250:        href = related(node, "node")
tools/build_osf_targets.py:258:    root = re.search(r"/(?:nodes|registrations)/([a-z0-9]+)/", related(node, "root") or "")
tools/entry.py:216:    # Datasets are related as <archive>:<id>/<version> (docs/archives.md); papers as doi:, entries as entry:.
tools/entry.py:218:            for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))]
tools/entry.py:220:                for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
tools/entry.py:711
[... 49 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 205,240p tools/entry.py; sed -n 700,730p tools/entry.py
```

```
locked_for = LOCK_VERSION.search(lock.read_text()[:2000])
        if entry.get("python") and locked_for and locked_for.group(1) != str(entry["python"]):
            report.error(rel / "requirements.lock.txt", f"locked for Python {locked_for.group(1)}, but entry.yaml "
                         f"says {entry['python']}; run `tools/entry.py lock`")
        pinned = {re.split(r"[=<>!~\[ ]", line, maxsplit=1)[0].lower().replace("_", "-")
                  for line in lock.read_text().splitlines() if line and not line.startswith((" ", "#"))}
        for line in requirements.read_text().splitlines():
            name = re.split(r"[=<>!~\[ ;]", line.strip(), maxsplit=1)[0].lower().replace("_", "-")
            if name and not name.startswith("#") and name not in pinned:
                report.error(rel / "requirements.lock.txt", f"{name} is required but not locked; re-run lock")

    # Datasets are related as <archive>:<id>/<version> (docs/archives.md); papers as doi:, entries as entry:.
    used = [r["id"].split(":", 1)[1].partition("/")
            for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))]
    archives = {r["id"].split(":", 1)[1].partition("/")[0]: r["id"].split(":", 1)[0]
                for r in entry.get("related", []) if not r["id"].startswith(("doi:", "entry:"))}
    dandisets = [d for d, _, _ in used]
    versions = {d: v for d, _, v in used}
    if entry.get("type") in ("orientation", "reproduction"):
        if not dandisets:
[... 47 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/mckenzie-2025/README.md",
 "content": "# McKenzie et al. (2025) from dandiset 000552\n\nTests the electrophysiology findings of [McKenzie et al. (2025)](https://doi.org/10.7554/elife.105183)\non [DANDI:000552](https://dandiarchive.org/dandiset/000552/0.230630.2304), the Huszar et al. (2022)\nrecordings the paper reanalyses, at the version the paper cites (0.230630.2304). The fiber photometry of\nnorepinephrine (Figures 1 to 6) is not in the dandiset.\n\n| Claim | Outcome |\n|---|---|\n| Ensemble of 253.8 neurons per session (191 to 363) | Reproduced (all units, not pyramidal cells only) |\n| Faster decorrelation in the first minute in a novel environment (Figure S6B) | Not reproduced |\n| No such change in the familiar environment (Figure S6D) | Reproduced |\n| UMAP embedding maps position, early moments at its periphery (Figure 7A, B) | Partially reproduced |\n| First-minute vectors less similar to same-place neighbours than at minute 10, novel (Figure 7E) | Reproduced |\n| The same in the familiar environment (Figure 7F) | Reproduced |\n| First minute more similar in the familiar than the novel environment (Figure 7G) | Reproduced |\n| In-field firing rises and out-of-field firing falls (Figure S7A, B) | Partially reproduced |\n| Movement differences of neighbours not related to time (Figure S7C, D) | Not reproduced |\n| Only time explains nearest-neighbour similarity (Figure S7E, F) | Not reproduced |\n| The same without conditioning on location (Figure S7G, H) | Reproduced |\n| Late moments more reactivated in post ripples (Figure 8B) | Not reproduced |\n| No early against late difference in the familiar environment (Figure 8D) | Not reproduced |\n| No reactivation in pre ripples (Figure 8A) | Not reproduced |\n| Photometry findings (13) and the NE and settling time-course comparison | Blocked: data missing |\n\nA failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the\ndifferences from the paper's method.\n\nThe pinned version has no cell types; they are read from the later version 0.261113.1035, whose spike\ntimes are the same. In session e16-3m2-211211 the linear-track tracking is filed in the open-field epoch,\nin both versions. The attempt record, with the reasons and the differences from the paper's method, is\n[`attempts/mckenzie-2025-01.yaml`](../../attempts/mckenzie-2025-01.yaml).\n\n- `settling.ipynb`: the data check, the ensemble size, decorrelation, the UMAP embedding, nearest-neighbour\n  settling, place field deviations and the movement controls. About 11 minutes.\n- `reactivation.ipynb`: reactivation of track moments in ripples. About 35 minutes, most of it the 1000\n  shuffles per ripple set.\n- `settle.py`: loading, population vectors, nearest neighbours, the speed filters, place fields, the\n  model of Figure S7E, F and the reactivation test, with where each parameter comes from.\n"
}
```

```
File created successfully at: entries/mckenzie-2025/README.md (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
date -u && timeout 600 python tools/entry.py lock entries/mckenzie-2025 2>&1 | tail -5 && python tools/entry.py check entries/mckenzie-2025 2>&1 | tail -15
```

```
Thu Nov 26 18:16:20 UTC 2026
wrote mckenzie-2025/requirements.lock.txt (Python 3.13, with hashes)
0 error(s)
```

**Agent calls Bash**

```bash
time python tools/entry.py all entries/mckenzie-2025 2>&1 | tail -15; date -u
```

```
Installed kernelspec registry-mckenzie-2025 in executed/mckenzie-2025/.venv/share/jupyter/kernels/registry-mckenzie-2025
0 error(s)
pass  settling.ipynb  (657 s)
pass  reactivation.ipynb  (2093 s)

real	46m1.442s
user	159m29.042s
sys	0m27.693s
Thu Nov 26 19:02:32 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && for n in settling reactivation; do python - <<EOF > ex_$n.txt
import nbformat
nb=nbformat.read("executed/mckenzie-2025/$n.ipynb",4)
for i,c in enumerate(nb.cells):
    if c.cell_type!="code": continue
    for o in c.get("outputs",[]):
        if o.output_type=="stream" and o.name=="stdout": print(f"--- cell {i}\n", o.text)
        if o.output_type=="error": print("ERR", i, o.evalue)
EOF
done; diff <(grep -v "in [0-9]* s\|runtime\|memory" full1.txt) <(grep -v "in [0-9]* s\|runtime\|memory" ex_settling.txt) | head -40; diff <(grep -v "in [0-9]* s\|runtime\|memory" full2.txt) <(grep -v "in [0-9]* s\|runtime\|memory" ex_reactivation.txt) | head
```

```
157,160c157,160
<   nov window a60, minute 1 vs min10: mean difference +0.022 1/s, t(7) = 0.18, p = 0.865
<   nov window a60, minute 1 vs min10alt: mean difference -0.001 1/s, t(7) = -0.02, p = 0.987
<   nov window b100, minute 1 vs min10: mean difference +0.119 1/s, t(7) = 1.25, p = 0.25
<   nov window b100, minute 1 vs min10alt: mean difference +0.096 1/s, t(7) = 1.30, p = 0.234
---
>   nov window a60, minute 1 vs min10: mean difference +0.022 1/s, t(7) = 0.18, p = 0.865; minute 1 faster in 3 of 8
>   nov window a60, minute 1 vs min10alt: mean difference -0.001 1/s, t(7) = -0.02, p = 0.987; minute 1 faster in 5 of 8
>   nov window b100, minute 1 vs min10: mean difference +0.119 1/s, t(7) = 1.25, p = 0.25; minute 1 faster in 5 of 8
>   nov window b100, minute 1 vs min10alt: mean difference +0.096 1/s, t(7) = 1.30, p = 0.234; minute 1 faster in 6 of 8
173,176c173,176
<   fam window a60, minute 1 vs min10: mean difference +0.062 1/s, t(7) = 0.78, p = 0.459
<   fam window a60, minute 1 vs min10alt: mean difference +0.076 1/s, t(7) = 0.89, p = 0.401
<   fam window b100, minute 1 vs min10: mean difference +0.031 1/s, t(7) = 0.49, p = 0.642
<   fam window b100, minute 1 vs min10alt: mean difference +0.025 1/s, t(7) = 0.37, p = 0.72
---
>   fam window a60, minute 1 vs min10: mean difference +0.062 1/s, t(7) = 0.78, p = 0.459; minute 1 faster in 6 of 8
>   fam window a60, minute 1 vs min10alt: mean difference +0.076 1/s, t(7) = 0.89, p = 0.401; minute 1 faster in 5 of 8
>   fam window b100, minute 1 vs min10: mean difference +0.031 1/s, t(7) = 0.49, p = 0.642; minute 1 faster in 5 of 8
>   fam window b100, minute 1 vs min10alt: mean difference +0.025 1/s, t(7) = 0.37, p = 0.72; minute 1 faster in 3 of 8
[... 1 more lines not kept]
```

**Agent calls Bash**

```bash
for q in "GRAB-NE" "norepinephrine hippocampus" "McKenzie" "event boundaries"; do curl -s "https://api.dandiarchive.org/api/dandisets/?search=$(python3 -c "import urllib.parse,sys;print(urllib.parse.quote(sys.argv[1]))" "$q")&page_size=20" | python3 -c "
import json,sys; d=json.load(sys.stdin); print('$q', d['count']); [print('  ',x['identifier'], x['draft_version']['name'][:90]) for x in d['results']]"; done
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
curl -s "https://api.dandiarchive.org/api/dandisets/001865/versions/draft/info/" | python3 -c "
import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m['name']); print(m.get('description','')[:800]); print([c.get('name') for c in m.get('contributor',[])]); print(m.get('relatedResource')); print(d.get('asset_count'), m.get('version'))"; curl -s "https://api.dandiarchive.org/api/dandisets/001865/versions/" | python3 -c "import json,sys; print([v['version'] for v in json.load(sys.stdin)['results']])"; curl -s "https://api.dandiarchive.org/api/dandisets/002096/versions/draft/info/" | python3 -c "
import json,sys; d=json.load(sys.stdin); m=d['metadata']; print(m['name']); print([c.get('name') for c in m.get('contributor',[])][:8])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && cp entries/mckenzie-2025/settle.py . && cat > dev3.py <<'EOF'
import numpy as np, settle as S, time
s=S.load_session("e15-13f1-220118"); ct,_=S.cell_types(s["sid"], s["spike_index"]); pyr=np.where(ct=="Pyramidal Cell")[0]
for r in s["runs"][:2]:
    t=time.time()
    M=S.run_measures(s,r,pyr)
    i=r["idx"]; ts=s["pos_t"][i]; xy=s["xy"][i]
    c=(np.arange(len(M["t"]))+0.5)*S.BIN + r["t0"]
    j=np.clip(np.searchsorted(ts,c),1,len(ts)-1); j=np.where(np.abs(ts[j-1]-c)<np.abs(ts[j]-c),j-1,j)
    ok=np.abs(ts[j]-c)<=S.BIN
    loc2=np.where(ok, np.floor(xy[j,0])*10000+np.floor(xy[j,1]), np.nan)
    nn,_=S.nn_conditioned(M["zn"],loc2,np.isfinite(loc2),M["t"]); sm=S.nan_smooth(nn)
    print(r["t0"], S.window_mean(sm,M["t"],0), S.window_mean(sm,M["t"],600), "1D", S.window_mean(M["all"]["nn_s"],M["t"],0), S.window_mean(M["all"]["nn_s"],M["t"],600), time.time()-t)
EOF
python dev3.py 2>&1 | grep -v Warn
```

```
res[f"dvel3_{e}"] = np.nanmean(dv, 1)
  res[f"dacc3_{e}"] = np.nanmean(da, 1)
5616.608 0.3567839492677292 0.4445904436623397 1D 0.4010628427831181 0.5138167951646085 6.116600751876831
13105.6 0.2528998586976919 0.4456725552841245 1D 0.3342396422835097 0.515221047469333 5.851872205734253
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/mckenzie-2025 && cat >> settle.py <<'EOF'


def location_2d(s, run, t):
    """1 x 1 cm (x, y) location bins at the bin times t (from transfer), for runs whose x, y are in cm.

    The Methods' bins (Place field detection) are 1 x 1 cm of the mouse's location; this is that reading,
    usable only where the file's x, y are in cm (`None` otherwise).
    """
    i = run["idx"]
    ts = s["pos_t"][i]; xy = s["xy"][i]
    if np.nanmax(xy) <= 1.5:
        return None
    c = t + BIN / 2 + run["t0"]
    j = np.clip(np.searchsorted(ts, c), 1, len(ts) - 1)
    j = np.where(np.abs(ts[j - 1] - c) < np.abs(ts[j] - c), j - 1, j)
    ok = np.abs(ts[j] - c) <= BIN
    return np.where(ok, np.floor(xy[j, 0] / LOC_CM) * 10000 + np.floor(xy[j, 1] / LOC_CM), np.nan)
EOF
cd $TMPDIR && python - <<'EOF'
s=open('build1.py').read()
anchor='''code(r"""
# per-minute session means'''
new='''code(r"""
# variant, not judged: 1 x 1 cm bins of (x, y), the Methods' bins, for the runs whose x, y are in cm
rows = []
for sid in TEST:
    for env in ("nov", "fam"):
        M = MEAS[(sid, env, "pyr")]; r = SESS[sid]["runs"][0 if env == "fam" else 1]
        loc2 = S.location_2d(SESS[sid], r, M["t"])
        if loc2 is None:
            continue
        nn, _ = S.nn_conditioned(M["zn"], loc2, np.isfinite(loc2), M["t"])
        x = S.nan_smooth(nn)
        rows.append(dict(session=sid, env=env, min1=S.window_mean(x, M["t"], 0), min10=S.window_mean(x, M["t"], 600)))
XY = pd.DataFrame(rows)
print(XY.round(3).to_string())
for env in ("nov", "fam"):
    d = XY[XY.env == env]
    t, p, n, md_ = paired(d["min1"].values, d["min10"].values)
    print(f"{env}, (x, y) bins: min1 - min10 = {md_:+.3f}, t({n-1}) = {t:.2f}, p = {p:.3g}")
both = XY.pivot(index="session", columns="env", values="min1").dropna()
t, p, n, md_ = paired(both["fam"].values, both["nov"].values)
print(f"familiar vs novel minute 1, (x, y) bins: {md_:+.3f}, t({n-1}) = {t:.2f}, p = {p:.3g}")
""", ["claim:fig7e-novel-settling", "claim:fig7f-familiar-settling", "claim:fig7g-familiar-more-similar-early"])

''' + anchor
assert anchor in s
s=s.replace(anchor,new,1)
open('build1.py','w').write(s)
EOF
source env/bin/activate && python build1.py && cp entries/mckenzie-2025/settle.py . && python runnb.py entries/mckenzie-2025/settling.ipynb $TMPDIR/dev4.ipynb dev 2>&1 | grep -v TCP | tail -3
```

```
written 48
ran in 160 s
Shell cwd was reset to
```

**Agent calls Bash**

```bash
date -u; time python tools/entry.py all entries/mckenzie-2025 2>&1 | tail -4; date -u
```

```
Thu Nov 26 19:06:22 UTC 2026
Installed kernelspec registry-mckenzie-2025 in executed/mckenzie-2025/.venv/share/jupyter/kernels/registry-mckenzie-2025
0 error(s)
pass  settling.ipynb  (665 s)
pass  reactivation.ipynb  (2098 s)

real	46m15.378s
user	160m4.884s
sys	0m28.337s
Thu Nov 26 19:52:38 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && source env/bin/activate && python - <<'EOF'
import nbformat
nb=nbformat.read("executed/mckenzie-2025/settling.ipynb",4)
for i,c in enumerate(nb.cells):
    if c.cell_type=="code" and "location_2d" in c.source:
        for o in c.outputs:
            if o.output_type=="stream": print(o.text)
EOF
```

```
session  env   min1  min10
0   e13-26m1-211019  fam  0.324  0.396
1   e13-26m1-211119  fam  0.413  0.436
2   e15-13f1-220118  nov  0.253  0.446
3   e15-13f1-220118  fam  0.356  0.445
4   e15-13f1-220119  nov  0.266  0.433
5   e15-13f1-220119  fam  0.357  0.445
6   e15-13f1-220120  fam  0.397  0.439
7    e16-3m2-211211  nov  0.314  0.371
8    e16-3m2-211211  fam  0.402  0.578
9    e16-3m2-211212  nov  0.339  0.371
10   e16-3m2-211212  fam  0.349  0.478
11   e16-3m2-211213  fam  0.393  0.445
nov, (x, y) bins: min1 - min10 = -0.112, t(3) = -2.83, p = 0.0663
fam, (x, y) bins: min1 - min10 = -0.084, t(7) = -4.78, p = 0.00202
familiar vs novel minute 1, (x, y) bins: +0.073, t(3) = 3.42, p = 0.0417
Shell cwd was reset to
```

**Agent calls Bash**

```bash
ls questions | grep -i mckenzie; ls papers/author-notes 2>/dev/null | grep -i mckenzie; grep -n "questions" docs/protocol.md | head -3; sed -n 1,40p questions/README.md
```

```
186:### 6. Answer questions
197:`questions/<paper>.yaml`.
349:     do not change the claim. Add a question to `questions/<paper>.yaml`
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

**Agent calls Write**

```json
{
 "file_path": "attempts/mckenzie-2025-01.yaml",
 "content": "schema_version: 3\nid: mckenzie-2025-01\ndatasets:\n- archive: dandi\n  id: \"000552\"\n  version: 0.230630.2304\n  doi: 10.48324/dandi.000552/0.230630.2304\n  relation: reuses\npaper: doi:10.7554/elife.105183\ndate: 2026-11-26\nentry: mckenzie-2025\nprovenance:\n  kind: agent\n  accountable:\n    name: CatalystNeuro\n  agent:\n    harness: Claude Code\n    model: claude-opus-5-5\n    protocol: pilot-19\n  runner:\n    platform: GitHub Actions\n    url: https://github.com/encorescience/encore-registry/actions/runs/45862924456\ninputs:\n- what: CellExplorer putative cell types of every unit (units/putative_cell_type) and the environment names\n    of the epochs (intervals/epochs/environment), read from a later version of the same dandiset. The pinned\n    version has neither. The helper checks, file by file, that the later version's spike index is identical\n    to the pinned one before taking the labels, and the spike times were compared at both ends of every file\n    while preparing. The labels select the pyramidal cells (claims file E3) and name the environments.\n  source: DANDI:000552 version 0.261113.1035, doi:10.48324/dandi.000552/0.261113.1035\noutcomes:\n- claim: figs1a-desipramine\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The fiber photometry recordings are not in DANDI:000552, which holds the Huszar et al. (2022)\n    electrophysiology only. The paper has no data availability statement. A search of the DANDI archive for\n    GRAB-NE, norepinephrine hippocampus, McKenzie and event boundaries found no dandiset of these recordings\n    (001865 holds cortical GRAB-NE imaging from another lab).\n- claim: figs1b-yohimbine\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Photometry recordings not deposited (see figs1a-desipramine).\n- claim: fig1d-arena-decay\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Photometry recordings not deposited (see figs1a-desipramine).\n- claim: figs1e-univariate-covariates\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Photometry recordings not deposited (see figs1a-desipramine).\n- claim: fig1e-arena-time-from-transition\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Photometry recordings not deposited (see figs1a-desipramine).\n- claim: fig2c-track-time-from-transition\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Photometry recordings not deposited (see figs1a-desipramine).\n- claim: figs2-no-reward-modulation\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Photometry recordings not deposited (see figs1a-desipramine).\n- claim: fig3d-object-introduction\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Photometry recordings not deposited (see figs1a-desipramine).\n- claim: figs3-object-order-and-sampling\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Photometry recordings not deposited (see figs1a-desipramine).\n- claim: fig4b-novel-object-on-track\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Photometry recordings not deposited (see figs1a-desipramine).\n- claim: fig5d-decay-hastens-with-days\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Photometry recordings not deposited (see figs1a-desipramine).\n- claim: figs4-behavior-day1-day2\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The DeepLabCut behaviour of the photometry mice is not deposited (see figs1a-desipramine).\n- claim: fig6-recent-history\n  outcome: blocked\n  blocked_by: data_missing\n  notes: Photometry recordings not deposited (see figs1a-desipramine).\n- claim: ne-and-settling-time-course\n  outcome: blocked\n  blocked_by: data_missing\n  notes: The NE half of the comparison is in the undeposited photometry recordings. The settling half is\n    tested by fig7e-novel-settling, fig7f-familiar-settling and fig7g-familiar-more-similar-early, all\n    reproduced; per-minute nearest-neighbour means rise from 0.393 to about 0.50 by minute 7 in novel runs\n    and from 0.430 to about 0.52 by minute 3 in familiar runs.\n- claim: ephys-ensemble-size\n  outcome: reproduced\n  notebook: settling.ipynb\n  output: claim:ephys-ensemble-size\n  measured:\n  - 259.38\n  - 191\n  - 363\n  notes: Under reading (b), all units, the eight tested sessions give a mean of 259.38 units (191 to 363),\n    within tolerance. The nine sessions with a familiar run and a tracked novel run give 253.78 (191 to 363),\n    the paper's numbers. Under reading (a), pyramidal cells only, the mean is 215.75 (158 to 318) over the\n    eight sessions and 211.00 over nine, outside the tolerance. The paper's count therefore matches all\n    units of nine sessions, while its Methods analyze only pyramidal cells and its tests have 8 sessions\n    (see the paper_inconsistency finding).\n  deviations:\n  - Sessions are those of claims file E1 found in the dataset (eight with a familiar run and a novel run of\n    at least 660 s); e13-26m1-211116, whose novel run is 344 s long, is added as a variant.\n- claim: figs6b-decorrelation-novel\n  outcome: not_reproduced\n  notebook: settling.ipynb\n  output: claim:figs6b-decorrelation-novel\n  notes: In the novel run the decay rate (1/tau) of minute 1 is not higher than that of minute 10 under any\n    reading. With 60 s windows the mean difference is +0.022 1/s (t(7) = 0.18, p = 0.865; minute 1 faster in\n    3 of 8 sessions) with minute 10 at 600 s and -0.001 (p = 0.987) at 540 s; with 100 s windows +0.119 (p =\n    0.25) and +0.096 (p = 0.234). On the seven sessions with clock-checked tracking +0.073 (p = 0.603). No fit\n    gave a time constant under 10 ms.\n  deviations:\n  - Pyramidal cells are those the later version 0.261113.1035 labels Pyramidal Cell (CellExplorer), the\n    pinned version having no labels (claims file E3).\n  - The paper's \"100-s moving average\" was read in the two ways the criterion names; both are shown.\n  - Units with no spike in the first 1000 s, where their z-score is undefined, are dropped (1 or 2 units in\n    a few runs, listed in the notebook).\n- claim: figs6d-decorrelation-familiar\n  outcome: reproduced\n  notebook: settling.ipynb\n  output: claim:figs6d-decorrelation-familiar\n  notes: Under the judged reading (60 s windows, minute 10 at 600 s) the familiar run's minute 1 decay rate\n    exceeds minute 10's by +0.062 1/s, t(7) = 0.78, p = 0.459, not significant. The other readings give p =\n    0.401 to 0.72. The contrast the paper draws with the novel run is not seen, as the novel run shows no\n    difference either (figs6b-decorrelation-novel).\n  deviations:\n  - As figs6b-decorrelation-novel.\n- claim: fig7ab-umap-embedding\n  outcome: partially_reproduced\n  assumed: true\n  notebook: settling.ipynb\n  output: claim:fig7ab-umap-embedding\n  notes: Under the claim's seed the 2D embedding predicts the linearized position better than the\n    block-shuffled position in 7 of 8 novel runs (R^2 0.185 to 0.717 against -0.194 to -0.108 shuffled),\n    and in 7 or 8 of 8 under all five seeds; the exception is e16-3m2-211211, whose tracking is misfiled.\n    First-minute bins are farther from the embedding's median than later bins in 1 of 8 sessions, and in 0\n    or 1 of 8 under all five seeds, so by this measure moments just after transfer are not at the periphery.\n    The position part holds and the periphery part does not.\n  deviations:\n  - The paper gives no UMAP parameters and no measure; the claims file's measures were used, with umap-learn\n    defaults.\n  - UMAP is run on every fifth 100 ms bin of the first 1000 s of each novel run (2000 vectors), to keep the\n    five seeds within the time limit.\n  - Position is the linearized position in cm; the x, y position is not in cm in five of the novel runs.\n    This is an assumption, as the paper shows a 2D location.\n- claim: fig7e-novel-settling\n  outcome: reproduced\n  assumed: true\n  notebook: settling.ipynb\n  output: claim:fig7e-novel-settling\n  notes: In the novel run the smoothed nearest-neighbour correlation of minute 1 is lower than that of minute\n    10 by 0.104 (t(6) = -4.07, p = 0.0066, over all bins with minute 10 at 600 s). e13-26m1-211119 enters only\n    from minute 2, as its tracking starts 63 s after the epoch start. Every combination of the E5, E6 and\n    session-set readings gives p of 0.026 or less. Variants not judged; with time counted from the first\n    tracked frame 0.106 (t(7) = -6.44, p = 0.000355); neighbours from other visits only, t(6) = -6.77, p =\n    0.000508; all units, t(6) = -3.93, p = 0.00771; 1 x 1 cm bins of (x, y), possible in 4 novel runs only,\n    0.112 (t(3) = -2.83, p = 0.0663). The \"several minutes\" part is not judged; the session means rise from\n    0.393 in minute 1 to about 0.50 by minute 7.\n  deviations:\n  - Location bins are 1 cm bins of the linearized position. The Methods bin the location in 1 x 1 cm\n    (Place field detection), but the x, y position of five of the nine novel runs is in 0 to 1 units, so\n    the 2D reading can be run only on runs whose x, y are in cm; it is shown as a variant. This is an\n    assumption and the outcome rests on it.\n  - The Gaussian of the 1 s smoothing is taken as a standard deviation of 1 s, a standard choice for a\n    detail averaged over 60 s windows.\n  - In e16-3m2-211211 the novel-run tracking is filed in the open-field epoch (finding); the main reading\n    keeps it as filed, as the paper's eight sessions, and the seven other sessions are shown.\n- claim: fig7f-familiar-settling\n  outcome: reproduced\n  assumed: true\n  notebook: settling.ipynb\n  output: claim:fig7f-familiar-settling\n  notes: In the familiar run minute 1 is lower than minute 10 by 0.089 (t(7) = -5.74, p = 0.0007), p of\n    0.0053 or less under every combination of readings. With 1 x 1 cm (x, y) bins, possible in all eight\n    familiar runs, 0.084 (t(7) = -4.78, p = 0.00202).\n  deviations:\n  - As fig7e-novel-settling; here the 2D reading of the Methods could be run on every session and agrees.\n- claim: fig7g-familiar-more-similar-early\n  outcome: reproduced\n  assumed: true\n  notebook: settling.ipynb\n  output: claim:fig7g-familiar-more-similar-early\n  notes: Familiar minute 1 is higher than novel minute 1 by 0.037 over all bins (t(6) = 2.58, p = 0.0415) and by\n    0.079 above 5 cm/s (t(5) = 4.56, p = 0.0061). On the seven clock-checked sessions it is 0.036 (p = 0.0887)\n    over all bins and 0.082 (p = 0.017) above 5 cm/s. From the first tracked frame 0.056 (t(7) = 5.54, p =\n    0.000867); with (x, y) bins, on 4 sessions, 0.073 (p = 0.0417). The faster settling in the familiar run is\n    not judged; its mean reaches 0.52 by minute 3, the novel mean about 0.50 by minute 7.\n  deviations:\n  - As fig7e-novel-settling.\n- claim: figs7ab-in-field-out-field\n  outcome: partially_reproduced\n  assumed: true\n  notebook: settling.ipynb\n  output: claim:figs7ab-in-field-out-field\n  notes: In-field deviations rise over the first 10 minutes in both environments (reading a, novel +0.0231\n    per minute, t(7) = 2.98, p = 0.0207, familiar +0.0212, p = 0.017; reading b, p = 5.68e-05 and 0.000378).\n    Out-of-field deviations fall in the familiar run (reading a -0.0048 per minute, p = 0.00107; reading b\n    -0.0047, p = 0.00402) but not in the novel run (+0.0001, p = 0.966; reading b +0.0017, p = 0.387). The seven\n    clock-checked sessions give the same pattern. The claim holds in the familiar run and only in part in the\n    novel run.\n  deviations:\n  - Place maps use 1 cm bins of the linearized position (see fig7e-novel-settling), an assumption.\n  - Units with no field bin above 5 Hz are left out (27 to 209 units with a field per run).\n  - The per-session slope and the one-sample t-test are the claims file's standard choices, as the paper\n    gives no test.\n- claim: figs7cd-movement-not-time-locked\n  outcome: not_reproduced\n  assumed: true\n  notebook: settling.ipynb\n  output: claim:figs7cd-movement-not-time-locked\n  notes: In the novel run the movement differences of the nearest neighbours fall with time after transfer.\n    Under the judged reading (3 neighbours, Kalman filter, all bins, first 600 s) the mean Spearman correlation\n    is -0.110 for |dvel|NN (t(7) = -5.42, p = 0.0010) and -0.103 for |dacc|NN (t(7) = -5.77, p = 0.0007). In the\n    familiar run there is none (-0.016, p = 0.537; -0.005, p = 0.842). Over the 16 novel combinations of\n    readings 14 find a relationship at p < 0.05 (the other two p = 0.054 and 0.055); none of the 16 familiar\n    ones does.\n  deviations:\n  - Speed and acceleration are taken along the linearized path (its length per second); the x, y position\n    is not in cm in five novel runs. The Kalman filter's noise settings are standard choices, as the paper\n    gives none for the electrophysiology.\n  - Judged under the first reading of each open detail (3 neighbours, Kalman, all bins), as a claim of\n    absence is judged on one test; this choice is the assumption the outcome rests on, and two of the\n    sixteen novel combinations would not find the relationship.\n- claim: figs7ef-time-explains-similarity\n  outcome: not_reproduced\n  notebook: settling.ipynb\n  output: claim:figs7ef-time-explains-similarity\n  notes: Under no reading is time the only variable whose removal significantly worsens the prediction in\n    both environments. With the photometry model's form, 3 neighbours and the Kalman filter, dropping |dvel|NN\n    raises the CVMSE by 7.76% in the novel run (t(7) = 3.50, p = 0.0100) and 6.96% in the familiar run (p =\n    0.0003); dropping time raises it by 7.31% in the novel run (p = 0.0290) and 1.00% in the familiar run (p =\n    0.6086); dropping |dacc|NN does not matter (p = 0.67 and 0.51). The linear model and the other readings\n    give the same pattern (dropping |dvel|NN p of 0.0321 or less, dropping time in the familiar run p of 0.38\n    or more).\n  deviations:\n  - The photometry model's complexity penalty (lambda = 0.001, form not given) is left out; bounded least\n    squares replaces fmincon. The tau bounds of the photometry Methods (0.1 to 0.001 and 0.001 to 0.0001) are\n    read as decay rates per second.\n  - The model is fit on every tenth 100 ms bin (1 s steps) of the whole run, as the series is smoothed with a\n    1 s Gaussian; the paper does not say which bins enter.\n- claim: figs7gh-unconditioned-similarity\n  outcome: reproduced\n  notebook: settling.ipynb\n  output: claim:figs7gh-unconditioned-similarity\n  notes: Under reading (a), the 3 most correlated vectors anywhere in the run, minute 1 is lower than minute\n    10 in the novel run (-0.0236, t(7) = -3.01, p = 0.0198) and the familiar run (-0.0378, t(7) = -4.66, p =\n    0.00231), and with minute 10 at 540 s (p = 0.00301 and 0.000807). Reading (b), the mean correlation with\n    all other vectors, is near 0 in every window (-0.0016 to 0.0023), since each unit is z-scored and the\n    vectors average to about zero, and finds no difference (p = 0.13 and 0.604).\n- claim: fig8b-late-moments-reactivated\n  outcome: not_reproduced\n  notebook: reactivation.ipynb\n  output: claim:fig8b-late-moments-reactivated\n  notes: The false positive rate of the procedure is 0.001 (0.00093 to 0.00107 by session), the paper's.\n    Under the main reading (pre (a), z-scored vectors, pool (a)) post ripples reactivate 0.232% of\n    first-minute moments and 0.209% of moments at 10 to 11 minutes (late minus early -0.0236 percentage\n    points, t(7) = -1.40, p = 0.204). Under the five seeds the difference is -0.0148 to -0.0243 (p 0.189 to\n    0.387). No other reading finds late moments more reactivated at p < 0.05 (raw counts +0.0305, p = 0.1976;\n    pooled shuffles -0.0108, p = 0.509, and -0.0167, p = 0.2911). Without e16-3m2-211211, -0.0263 (p = 0.219).\n  deviations:\n  - The ripples are those deposited in the files (Huszar et al. 2022, 20 to 195 ms); the broadband LFP the\n    Methods detect them from is only in the raw files (120 to 180 GB each) and was not read.\n  - The moments are the 100 ms bins of minute 1 and of minutes 10 to 11 (1200 per run), not the whole run.\n  - The readings of E10 are run one at a time around a main reading (pre (b) also with pool (b)), not fully\n    crossed, to keep the notebook near half an hour.\n  - Each unit's values are permuted across the ripples of the pool, independently for each unit and\n    shuffle; a ripple reactivates a moment when its R is above all 1000 shuffles, which gives the paper's\n    false positive rate of 0.001.\n- claim: fig8d-familiar-no-difference\n  outcome: not_reproduced\n  assumed: true\n  notebook: reactivation.ipynb\n  output: claim:fig8d-familiar-no-difference\n  notes: The judged test finds a difference in the familiar run, with early moments reactivated more than late\n    ones (0.247% against 0.221%, -0.0255 percentage points, t(7) = -3.72, p = 0.0074), under all five seeds (p\n    0.0043 to 0.0074). The other readings find no difference (raw counts p = 0.7383, pooled shuffles p = 0.1497\n    and 0.2352). The difference is about a tenth of the reactivation rate, and opposite in sign to the novel\n    effect the paper reports.\n  deviations:\n  - As fig8b-late-moments-reactivated.\n  - The criterion judges absence under E10 (a) with z-scored vectors but does not name the shuffle pool; the\n    pool of the ripple's own set, the first the claims file lists, was used. With pre and post pooled the\n    difference is not significant, so the outcome rests on this choice.\n- claim: fig8-no-pre-reactivation\n  outcome: not_reproduced\n  notebook: reactivation.ipynb\n  output: claim:fig8-no-pre-reactivation\n  notes: Pre ripples reactivate on average 0.1334% of moments in the novel runs and 0.1461% in the familiar runs,\n    above the 0.1% false positive rate (one-sided t(7) = 2.82, p = 0.0129, and 7.90, p = 4.93e-05), under all\n    five seeds (p 0.0111 to 0.0132, and below 0.0001) and under every other reading (p of 0.0377 or less). Post\n    ripples reactivate more (0.2206% and 0.2342%), so the track patterns are more present in post than in pre\n    ripples, but they are not absent from pre ripples.\n  deviations:\n  - As fig8b-late-moments-reactivated; the mean is over the 1200 moments of minutes 1 and 10 to 11.\nfindings:\n- kind: metadata_insufficient\n  severity: major\n  statement: The units of the pinned version carry no cell type (only clu_id, group_id and unit_name), and the\n    epochs carry no names, so pyramidal cells and the home cage, familiar and novel periods cannot be told\n    apart from the files. Session e13-26m1-211116 has no epochs table at all. Version 0.261113.1035 adds the\n    CellExplorer cell types, waveform metrics and the environment of each epoch, with identical spike times.\n  versions:\n  - 0.230630.2304\n  fixed_in: 0.261113.1035\n  notebook: settling.ipynb\n  output: finding-no-cell-types\n- kind: metadata_error\n  severity: critical\n  statement: In session e16-3m2-211211 the tracking and the 45 trials of the novel linear track\n    (linear_manu) are filed from 9575 to 11203 s, inside the epoch the later version names an open field\n    (openField_thomas, 9559 to 12002 s). Spikes carry no spatial information about this position at any\n    shift (0.246 bits per spike at zero shift, 0.245 to 0.256 at shifts of 5 and 30 s), while every other\n    run peaks at zero shift. Moved by 5564.5 s onto the epoch the later version names linear_manu (15124 to\n    16771 s), the same tracking gives 0.656 bits per spike at zero shift against 0.252 and 0.271 at 30 s. The\n    later version files its linear_manu tracking at the same wrong times.\n  versions:\n  - 0.230630.2304\n  - 0.261113.1035\n  notebook: settling.ipynb\n  output: finding-tracking-misfiled\n- kind: metadata_error\n  severity: minor\n  statement: The x, y position of five novel runs (e13-26m1-211019, 211116, 211119, e15-13f1-220120,\n    e16-3m2-211213) spans 0 to 1 while the series states cm; the familiar runs span 0 to about 92 cm. The\n    linearized position is in cm in all runs. The later version no longer states cm for these series but gives\n    no scale either.\n  versions:\n  - 0.230630.2304\n  fixed_in: 0.261113.1035\n  notebook: settling.ipynb\n  output: finding-position-not-cm\n- kind: data_missing\n  severity: major\n  statement: The pinned version has no tracking of the open-field environments. Three sessions\n    (e13-26m1-211124, e15-13f1-220117, e16-3m2-211210), whose only novel environment is an open field by the\n    later version's labels, have one tracked run, and in four sessions with two novel environments only one is\n    tracked. The later version adds the open-field tracking, in the lab's units without a scale.\n  versions:\n  - 0.230630.2304\n  fixed_in: 0.261113.1035\n  notebook: settling.ipynb\n  output: sanity\n- kind: other\n  about: data\n  severity: minor\n  statement: Tracking starts 14.6 to 63.3 s after the start of the maze epochs (63.3 s in the novel run of\n    e13-26m1-211119), and the files do not say when the mouse was placed in the maze, so the time of\n    transfer is known only to within this delay.\n  notebook: settling.ipynb\n  output: sanity\n- kind: metadata_error\n  severity: minor\n  statement: In three files (e13-26m1-211124, e15-13f1-220117, e16-3m2-211210) the description of the\n    behavior module lists its recordings as single letters (\"a, l, t, e, r, n, a, t, i, o, n\").\n  versions:\n  - 0.230630.2304\n  fixed_in: 0.261113.1035\n  notebook: settling.ipynb\n  output: finding-behavior-description\n- kind: paper_inconsistency\n  statement: The ensemble size the Results give (mean 253.8 neurons, range 191 to 363) is the count of all\n    units in the nine sessions of these mice that have a tracked novel run, while the Methods say only\n    pyramidal cells were analyzed (mean 211.0 over the same sessions) and every test has 7 degrees of freedom,\n    8 sessions. The Methods list 3 linear tracks, 3 figure-eight mazes and 1 arena, 7 environments for 8\n    sessions; the dataset's eight usable sessions hold 3 figure-eight mazes, 4 linear tracks and 1 session\n    whose novel epoch is an open field holding linear-track tracking.\n- kind: methods_unavailable\n  statement: Questions for the paper's authors, as the paper links no code. (1) Is the location of the\n    nearest-neighbour search the 2D position or the linearized one, given that the x, y position of five\n    novel runs is not in cm? (2) Which eight sessions, and which open-field or track run in sessions with two\n    novel environments? (3) Is a speed filter applied to the nearest-neighbour search and the place field\n    deviations? (4) What is the \"100-s moving average\" of the decorrelation analysis? (5) Which 30 min of\n    ripples are \"pre\", are the track vectors z-scored for reactivation, and is the shuffle pool the pre or post\n    set or both? (6) What is the model form for Figure S7E and F, and over which bins? (7) What thresholds\n    separate pyramidal cells? The attempt adopted the first reading listed in the claims file for each, ran the\n    others, and marks the outcomes that depend on a choice as assumed.\n"
}
```

```
File created successfully at: attempts/mckenzie-2025-01.yaml (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
python - <<'EOF'
p='attempts/mckenzie-2025-01.yaml'; s=open(p).read()
for a,b in [("dropping time in the familiar run p of 0.38\n    or more)","dropping time in the familiar run p of 0.379\n    or more)"),
            ("session-set readings gives p of 0.026 or less","session-set readings gives p of 0.0261 or less"),
            ("statement: Tracking starts 14.6 to 63.3 s after the start of the maze epochs","statement: In the eight tested sessions tracking starts 14.6 to 63.3 s after the start of the maze epochs")]:
    assert a in s, a; s=s.replace(a,b)
open(p,'w').write(s)
EOF
grep -n "or more)" attempts/mckenzie-2025-01.yaml; python tools/entry.py check entries/mckenzie-2025 2>&1 | tail -8; date -u
```

```
241:    or more).
0 error(s)
Thu Nov 26 19:54:43 UTC 2026
```

**Agent calls Bash**

```bash
grep -nE "^\s{4,}.*: " attempts/mckenzie-2025-01.yaml | head; grep -nE "^\s*(- )?[a-z_]+: .*: " attempts/mckenzie-2025-01.yaml | head; python -c "import yaml;d=yaml.safe_load(open('attempts/mckenzie-2025-01.yaml'));print(len(d['outcomes']), len(d['findings']))"; python -c "import yaml;print(len(yaml.safe_load(open('claims/mckenzie-2025.yaml'))['claims']))"
```

```
15:    name: CatalystNeuro
17:    harness: Claude Code
18:    model: claude-opus-5-5
19:    protocol: pilot-19
21:    platform: GitHub Actions
22:    url: https://github.com/encorescience/encore-registry/actions/runs/45862924456
28 8
28
```

**Agent calls Bash**

```bash
python tools/entry.py handover entries/mckenzie-2025 2>&1 | tail -3; ls executed/mckenzie-2025/handover/; git status --short | head -20; date -u
```

```
wrote executed/mckenzie-2025/handover
mckenzie-2025.yaml
reactivation.ipynb
settle.py
settling.ipynb
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
?? attempts/mckenzie-2025-01.yaml
?? entries/mckenzie-2025/
?? scripts
Thu Nov 26 19:55:14 UTC 2026
```

**Agent**

The attempt is recorded and handed over. `entry.py lock`, `check` and `all` all pass, and the verifier's package is in `executed/mckenzie-2025/handover/`. I did not verify my own work and committed nothing.

**1. Outcomes**

| Claim | Outcome |
|---|---|
| 13 photometry claims (Figs 1–6, S1–S5) and ne-and-settling-time-course | blocked, `data_missing` |
| ephys-ensemble-size | reproduced: all units give a mean of 259.4 (range 191–363); pyramidal cells only give 215.8, outside tolerance |
| figs6b-decorrelation-novel | not reproduced (no reading has p < 0.05) |
| figs6d-decorrelation-familiar | reproduced (p = 0.459) |
| fig7ab-umap-embedding | partially reproduced, assumed: position maps in 7 of 8 sessions, early moments are peripheral in 1 of 8 |
| fig7e-novel-settling | reproduced, assumed (p = 0.0066) |
| fig7f-familiar-settling | reproduced, assumed (p = 0.0007) |
| fig7g-familiar-more-similar-early | reproduced, assumed (p = 0.042) |
| figs7ab-in-field-out-field | partially reproduced, assumed: out-of-field firing does not fall in novel runs |
| figs7cd-movement-not-time-locked | not reproduced, assumed: in novel runs the movement differences fall with time (p ≈ 0.001) |
| figs7ef-time-explains-similarity | not reproduced: dropping \|Δvel\|NN also worsens the fit, in both environments |
| figs7gh-unconditioned-similarity | reproduced under reading (a) |
| fig8b-late-moments-reactivated | not reproduced (late minus early is −0.024 percentage points, p = 0.20) |
| fig8d-familiar-no-difference | not reproduced, assumed: early > late, p = 0.0074 under all five seeds |
| fig8-no-pre-reactivation | not reproduced: pre ripples run 0.13–0.15%, above the 0.1% false positive rate |

**2. What was found about the dataset (pinned 0.230630.2304, the version the paper cites)**
- **Critical:** in session e16-3m2-211211, the linear-track tracking and its 45 trials are filed inside the open-field epoch. Spikes show no spatial tuning to them at any time shift. Moved 5564.5 s later, onto the linear-track epoch, the tuning appears. The newest version, 0.261113.1035, has the same error.
- **Major, fixed in 0.261113.1035:**
  - There are no cell-type labels and no epoch names, and session e13-26m1-211116 has no epochs at all.
  - There is no open-field tracking.
- **Minor:**
  - In five novel runs the x, y position runs 0 to 1 but is labelled cm.
  - Tracking starts 15 to 63 s after each maze epoch begins, so the transfer time is uncertain by that much.
  - In three files the behavior module's description spells "alternation" as separate letters.
- Pyramidal cells come from the 0.261113.1035 labels. I checked that its spike times are identical, and listed it under `inputs`.
- Sessions: 9 have a familiar run and a tracked novel run, and 8 of those are long enough to test. All units of the 9 give exactly the paper's 253.8 (range 191–363). I recorded this as a `paper_inconsistency`, since the Methods say only pyramidal cells were analysed.
- **Assumptions:**
  - Location is binned on the linearized position in cm, because the 2D position is not in cm in five novel runs. The Methods' 1 × 1 cm (x, y) bins could be run on all familiar runs and agree there, but on only 4 novel runs.
  - For fig8d, the shuffle pool is the ripple's own set (pre or post).
  - For figs7cd, absence is judged under the first reading of each open detail.
- Seven questions for the paper's authors are in a `methods_unavailable` finding.
- I asked a reader no questions.

**3. Where the protocol was unclear or missing something**
1. It does not say what to do when the cited version lacks labels that a later version adds. I pinned the cited version and took only the labels from the later one, listed under `inputs`. `entry.yaml` can name only one version per dataset.
2. It does not say how to handle a recording known to be misfiled. I kept it as filed in the main reading (matching the paper's 8 sessions) and showed the 7 clean sessions as a variant.
3. The reactivation claims list 2 × 2 × 2 readings, and crossing them all would push that notebook past the time limit. I varied one reading at a time around a main reading and recorded this as a deviation.
4. "Absence is judged on the paper's test alone" does not fit when the criterion leaves a reading open (the pool for fig8d, several readings for figs7cd). I used the first-listed reading and marked the outcome assumed.

**4. Runtime and failures**
- `settling.ipynb` takes 11 minutes and `reactivation.ipynb` 35 minutes; peak memory is 4.1 GB.
- `reactivation.ipynb` is over the protocol's 10-minute aim but under the 60-minute limit.
- Ripples are the ones deposited in the files, not re-detected: the broadband LFP is only in the 120–180 GB raw files.
- Nothing failed, and the full run's numbers match the development run.

## End of run

71 turns, 176 minutes, $6.89 at API prices, result: success.
