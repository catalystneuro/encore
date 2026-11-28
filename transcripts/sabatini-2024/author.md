# sabatini-2024 · author · run 46074971238

Model `claude-opus-5-5`, Claude Code 2.1.284, permission mode `default`. Tools: `Task`, `Bash`, `DesignSync`, `Edit`, `EnterWorktree`, `ExitWorktree`, `Glob`, `Grep`, `ListAgents`, `NotebookEdit`, `Read`, `ReportFindings`, `SendMessage`, `Skill`, `TaskCreate`, `TaskGet`, `TaskList`, `TaskStop`, `TaskUpdate`, `ToolSearch`, `WebFetch`, `WebSearch`, `Write`.

**Agent calls Bash**

```bash
date -u; cd  ls; ls docs entries attempts claims paper tools; wc -l docs/*.md README.md
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
3	Version: `pilot-19`. Record this version in the attempt's provenance.
4	
5	This is what agents, or people, do to attempt a target and deposit the
6	result. A target is a dataset in a public archive and a paper it names. How
7	each archive's datasets are named, versioned and read is in
8	[archives.md](archives.md); the examples here are from DANDI, the first. It is written from the pilot attempts
9	([pilot notes](https://github.com/encorescience/encore-registry/blob/main/docs/pilot-notes.md)); the reasons for the rules are there.
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
[... 794 more lines not kept]
```

```
Fri Nov 27 22:13:37 UTC 2026
LICENSE
LICENSE-data
README.md
attempts
bunfig.toml
claims
docs
entries
n-desk.png
n-phone.png
n-phone2.png
node_modules
ov-papers-rows.png
package-lock.json
package.json
paper
papers
pnpm-lock.yaml
protocol.lock
[... 1220 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat README.md | head -80; cat claims/sabatini-2024.yaml; cat papers/datasets/sabatini-2024.yaml; ls papers/author-notes 2>/dev/null | grep sabat; ls questions | grep sabat; ls entries/sabatini-2024 -la
```

```
Exit code 2
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

[... 127 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "claims/sabatini-2024.yaml"
}
```

```
1	# Claims for Sabatini & Kaufman (2024), Nat. Commun. 15:7007, "Reach-dependent reorientation of
2	# rotational dynamics in motor cortex", tested on dandiset 000070 (relation reuses).
3	# Written by an agent (model "claude-opus-5-5", Claude Code, runner "GitHub Actions"), 2026-11-20,
4	# protocol pilot-18 as stated in docs/protocol.md. The writer did not look at the dandiset's data
5	# or files.
6	#
7	# Text read: the version of record (open access, CC BY-NC-ND), full text from PubMed Central
8	# (PMC11325044) with Methods, figure legends and Data and Code availability, and its one
9	# supplement, 41467_2024_51308_MOESM1_ESM.pdf (Supplementary Figures 1 to 8 with legends and the
10	# derivation of the basis function representation of a linear dynamical system). The Peer Review
11	# File and Reporting Summary were not read; no result rests on them. The supplement PDF was not
12	# opened beyond its extracted text.
13	#
14	# Code read: github.com/kaufmanlab/LDR-public at commit b65f28d (2024-08-02), the MATLAB code the
15	# Code availability statement links. It holds the analysis functions (TBF, single-condition LDS,
16	# alignment index, subspace excursion angles, rotation and location prediction, LDR encoding and
17	# decoding, jPCA reconciliation). It loads preprocessed .mat files that are not in the repository
18	# (ShenoyMonkeyData, ShenoyMonkeyDataSingleTrial, basisFxnNum, TBFResults and others; the paper
19	# says "Code-compatible data are available upon request"), and lacks kinFuncEval (the kinematic
20	# basis functions), the jPCA codepack, GPFA, and code for the location-from-kinematics regression
[... 755 more lines not kept]
```

**Agent calls Bash**

```bash
cd  cat papers/datasets/sabatini-2024.yaml; ls papers/author-notes | grep -i sabat; ls questions | grep -i sabat; ls -la entries/sabatini-2024 entries/fouke-2025; cat entries/fouke-2025/entry.yaml entries/fouke-2025/requirements.in; cat attempts/fouke-2025-01.yaml | head -150
```

```
# The datasets this paper is tested on (docs/paper-first.md).
schema_version: 1
paper: doi:10.1038/s41467-024-51308-7
title: Reach-dependent reorientation of rotational dynamics in motor cortex.
datasets:
- archive: dandi
  id: '000070'
  relation: reuses
ls: cannot access 'papers/author-notes': No such file or directory
ls: cannot access 'entries/sabatini-2024': No such file or directory
entries/fouke-2025:
total 136
drwxr-xr-x   2 runner runner  4096 Nov 27 22:10 .
drwxr-xr-x 369 runner runner 16384 Nov 27 22:13 ..
-rw-r--r--   1 runner runner  2144 Nov 27 22:10 README.md
-rw-r--r--   1 runner runner   907 Nov 27 22:10 entry.yaml
-rw-r--r--   1 runner runner 16218 Nov 27 22:10 omr.py
-rw-r--r--   1 runner runner 79403 Nov 27 22:10 reproduce_fouke_2025.ipynb
-rw-r--r--   1 runner runner    61 Nov 27 22:10 requirements.in
-rw-r--r--   1 runner runner  5989 Nov 27 22:10 requirements.lock.txt
[... 179 more lines not kept]
```

**Agent calls Bash**

```bash
cd  sed -n 150,400p attempts/fouke-2025-01.yaml | grep -n -A30 "^findings" | head -60; ls schemas; grep -n "DANDI" -A60 docs/archives.md | head -120
```

```
95:findings:
96-- kind: data_missing
97-  statement: The dandiset holds only the freely swimming tracking of Figure 1 and Figure S1. The
98-    two-photon imaging and the head-fixed tail tracking behind Figures 2 to 4 are not in it, and
99-    the GitLab repository the paper names for all behavioural and imaging data holds analysis
100-    notebooks only. Nine of the paper's main findings cannot be tested.
101-- kind: metadata_insufficient
102-  statement: The stimulus codes 0 to 20 have no names or description in the files or the
103-    dandiset metadata. They can be named only from the paper's analysis notebook and the protocol
104-    file of its stimulus software.
105-- kind: code_mismatch
106-  statement: The paper's analysis notebook labels code 9 as lateral right and 11 as lateral left,
107-    while its conversion of the stimulus software's names gives the reverse (it carries a remap
108-    that swaps them). The data do not settle which is right; zebrafish barely turn to either, and
109-    Danionella turn more to the right for code 11, which fits the stimulus software's assignment
110-    only if the fish turn with lateral motion.
111-- kind: metadata_error
112-  statement: Subject ids 0 to 11 are each used for one zebrafish and one Danionella cerebrum, so
113-    subject_id does not identify an animal. The archive's summary counts 25 subjects and lists
114-    only Danio rerio; the files hold 37 fish of two species.
[... 135 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -l "protocol: pilot-1[89]" attempts/*.yaml | head; python -c "
import json;s=json.load(open('schemas/attempt.schema.json'));print(json.dumps(s,indent=0)[:6000])"
```

```
attempts/allen-2026-01.yaml
attempts/amjad-2025-02.yaml
attempts/andreassen-2022-01.yaml
attempts/cambrainha-2025-01.yaml
attempts/chan-2024-01.yaml
attempts/choi-2025-02.yaml
attempts/churchland-2012-02.yaml
attempts/clark-2026-01.yaml
attempts/costabile-2023-01.yaml
attempts/du-2026-01.yaml
{
"$schema": "https://json-schema.org/draft/2020-12/schema",
"title": "One attempt at reproducing the claims of a target",
"description": "Draft. To be revised after the pilot. An attempt is recorded whether or not it produced a working notebook.",
"type": "object",
"additionalProperties": false,
"required": [
"schema_version",
"id",
"datasets",
[... 272 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -l "protocol: pilot-19" attempts/*.yaml | head -3; f=$(grep -l "protocol: pilot-19" attempts/*.yaml | head -1); sed -n 1,40p $f; grep -n -A12 "^findings" $f | head -40; ls entries/$(basename $f -01.yaml)
```

```
attempts/allen-2026-01.yaml
attempts/andreassen-2022-01.yaml
attempts/chan-2024-01.yaml
# Attempt on Allen, Yan, Kuan et al. (2026) with Dryad rjdfn2zqz version 439366 (docs/protocol.md).
schema_version: 3
id: allen-2026-01
datasets:
- archive: dryad
  id: rjdfn2zqz
  version: '439366'
  doi: 10.5061/dryad.rjdfn2zqz
  relation: primary
paper: doi:10.1038/s42003-025-09506-6
date: '2026-11-25'
entry: allen-2026
provenance:
  kind: agent
  accountable:
    name: CatalystNeuro
  agent:
[... 42 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s https://api.dandiarchive.org/api/dandisets/000070/ | python -m json.tool | head -40; curl -s "https://api.dandiarchive.org/api/dandisets/000070/versions/" | python -m json.tool | grep -E '"version"|"created"|"modified"|status'
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; V=0.261122.2046; curl -s "https://api.dandiarchive.org/api/dandisets/000070/versions/$V/assets/?page_size=100" | python -c "
import json,sys;d=json.load(sys.stdin)
for a in d['results']: print(a['asset_id'],a['path'],a['size'])"; curl -s "https://api.dandiarchive.org/api/dandisets/000070/versions/$V/" | python -c "
import json,sys;d=json.load(sys.stdin);print(d.get('description'));print(d.get('doi'));print(d.get('citation'));print([r.get('identifier') for r in d.get('relatedResource',[])])"
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR && uv venv -q env && . env/bin/activate && uv pip install -q pynwb remfile h5py numpy scipy pandas matplotlib scikit-learn dandi 2>&1 | tail -2; python -c "import pynwb;print(pynwb.__version__)"
```

```
4.2.0
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > survey.py <<'EOF'
import remfile,h5py,pynwb,requests,time,sys
V='0.261122.2046'
aid=sys.argv[1]
url=f'https://api.dandiarchive.org/api/assets/{aid}/download/'
t=time.time()
f=remfile.File(url); h=h5py.File(f,'r')
io=pynwb.NWBHDF5IO(file=h,load_namespaces=True); nwb=io.read()
print(nwb)
print('time',time.time()-t)
def walk(g,p=''):
    for k,v in g.items():
        if isinstance(v,h5py.Dataset): print(p+'/'+k,v.shape,v.dtype,dict((a,v.attrs[a]) for a in v.attrs if a in('unit','conversion','resolution','description')))
        else: walk(v,p+'/'+k)
walk(h)
EOF
python survey.py 75013796-4a2d-41dc-9eb6-db9d365b28b4 2>&1 | head -150
```

```
root pynwb.file.NWBFile at 0x133322988044704
Fields:
  devices: {
    Utah Array(M1) <class 'pynwb.device.Device'>,
    Utah Array(PMd) <class 'pynwb.device.Device'>
  }
  electrode_groups: {
    1 <class 'pynwb.ecephys.ElectrodeGroup'>,
    2 <class 'pynwb.ecephys.ElectrodeGroup'>
  }
  electrodes: electrodes <class 'pynwb.ecephys.ElectrodesTable'>
  experiment_description: Delayed reaching in a maze task. The monkey fixated a central point, was shown one target without barriers, one target with barriers, or three targets with barriers of which one was accessible, and after a delay reached to the target on a vertical screen. Activity was recorded with two 96-channel Utah arrays, one in dorsal premotor cortex (PMd) and one in primary motor cortex (M1).
  experimenter: ['Kaufman, Matthew T.' 'Churchland, Mark M.']
  external_resources: external_resources hdmf.common.resources.HERD at 0x133322987221216
  5 key(s), 3 entity(ies), 4 object(s), 1 file(s)
                         file_object_id  ...                                     entity_uri
0  5fd90c7d-a1ca-4007-9000-85115a2ad6dc  ...  http://purl.obolibrary.org/obo/NCBITaxon_9544
1  5fd90c7d-a1ca-4007-9000-85115a2ad6dc  ...  http://purl.obolibrary.org/obo/UBERON_0016634
2  5fd90c7d-a1ca-4007-9000-85115a2ad6dc  ...  http://purl.obolibrary.org/obo/UBERON_0001384
3  5fd90c7d-a1ca-4007-9000-85115a2ad6dc  ...  http://purl.obolibrary.org/obo/UBERON_0016634
[... 131 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > survey2.py <<'EOF'
import remfile,h5py,numpy as np,sys,pandas as pd
aid=sys.argv[1]
h=h5py.File(remfile.File(f'https://api.dandiarchive.org/api/assets/{aid}/download/'),'r')
u=h['units']
for k,v in u.items(): print('units/'+k,v.shape,v.dtype,v.attrs.get('description'))
print(dict(u.attrs))
e=h['general/extracellular_ephys/electrodes']
print(pd.Series(e['location'][:].astype(str)).value_counts(), e['group_name'][:5])
for k in u:
    if k not in('spike_times','spike_times_index') and u[k].shape[0]<1000:
        try: print(k, u[k][:10])
        except Exception as ex: print(k,ex)
t=h['intervals/trials']
for k in ['maze_condition','task_success','discard_trial','correct_reach','trial_type','trial_version','novel_maze','maze_num_targets','maze_num_barriers','unhittable','proto_trial']:
    x=t[k][:]; print(k, np.unique(x,return_counts=True) if len(np.unique(x))<30 else (len(np.unique(x)),x.min(),x.max()))
for k in ['start_time','stop_time','go_cue_time','move_begins_time','move_ends_time','offline_move_onset_time','target_presentation_time','reaction_time','offline_reaction_time']:
    x=t[k][:]; print(k, np.nanmin(x),np.nanmax(x),np.isnan(x).sum(), x[:3])
print(dict(h['general'].attrs))
EOF
python survey2.py 75013796-4a2d-41dc-9eb6-db9d365b28b4 2>&1
```

```
units/electrode_group (192,) object the electrode group that each spike unit came from
units/electrodes (192,) int64 the electrodes that each spike unit came from
units/electrodes_index (192,) uint8 Index for VectorData 'electrodes'
units/id (192,) int64 None
units/obs_intervals (506112, 2) float64 the observation intervals for each unit
units/obs_intervals_index (192,) uint32 Index for VectorData 'obs_intervals'
units/spike_times (66676824,) float64 the spike times for each unit in seconds
units/spike_times_index (192,) uint32 Index for VectorData 'spike_times'
{'colnames': array(['spike_times', 'obs_intervals', 'electrodes', 'electrode_group'],
      dtype=object), 'description': 'Threshold crossings on each electrode, not sorted (Blackrock unit code 0), one unit per electrode. Spike times were saved for each trial only, so obs_intervals are the trials.', 'namespace': 'core', 'neurodata_type': 'Units', 'object_id': '9c5fe0f4-8b31-43d2-ba89-a2ca7a2bf8cc'}
Pre-Motor Cortex, dorsal    96
M1 Motor Cortex             96
Name: count, dtype: int64 [b'1' b'1' b'1' b'1' b'1']
electrode_group [<HDF5 object reference> <HDF5 object reference> <HDF5 object reference>
 <HDF5 object reference> <HDF5 object reference> <HDF5 object reference>
 <HDF5 object reference> <HDF5 object reference> <HDF5 object reference>
 <HDF5 object reference>]
electrodes [0 1 2 3 4 5 6 7 8 9]
electrodes_index [ 1  2  3  4  5  6  7  8  9 10]
id [0 1 2 3 4 5 6 7 8 9]
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR; curl -s -o /dev/null -w "%{http_code}\n" https://github.com/kaufmanlab/LDR-public; curl -s -o /dev/null -w "%{http_code}\n" https://codeload.github.com/kaufmanlab/LDR-public/zip/b65f28d; date -u
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR; curl -sL -o ldr.zip https://codeload.github.com/kaufmanlab/LDR-public/zip/b65f28d && unzip -q -o ldr.zip && ls; find LDR-public* -name "*.m" | wc -l; find LDR-public* -name "*.m" | sed 's|.*/||' | tr '\n' ' '
```

Result: the fetched text is not kept.

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public-b65f28d; for f in preprocessTrials generateTrials pruneRepeats getBasisFxns TBF eigTransform extractParams crossValidateDimensionalityBasisFxns getVarExplained useFactorization; do p=$(find . -name "$f.m"|head -1); echo "=== $p"; grep -v '^\s*%' $p | grep -v '^\s*$'; done 2>&1 | head -400
```

```
=== ./utils/crossvalidation/preprocessTrials.m
function trials = preprocessTrials(trials)
for trial = 1:size(trials,2)
    trialArray = full(double(trials(trial).matrix));
    for neuron = 1:size(trialArray)
        trialArray(neuron,:) = imgaussfilt(1000*trialArray(neuron,:), ...
            20,'FilterSize',111,'Padding','Symmetric');
    end
    trials(trial).matrix = trialArray(:,1:10:end);
end
end
=== ./utils/crossvalidation/generateTrials.m
function trials = generateTrials(conds)
trialCount = 24;
for cond = 1:size(conds,2)
    activity = conds(cond).matrix;
    activity = interp1(-350:10:850,activity.',-350:850).';
    for trial = 1:trialCount
        trials(trial+(cond-1)*trialCount).matrix = poissrnd(activity/1000);
        trials(trial+(cond-1)*trialCount).condNum = conds(cond).condNum;
[... 173 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public-b65f28d; for f in cvConds bioEigs pairID fitDynamics idDynamics crossValidateDimensionalityConditions fitSingleLDS getAlignmentIndex getRecoverability quantifyTBFStats scrambleTrials eigValDistance compareTrialSimilarity; do p=$(find . -name "$f.m"|head -1); echo "=== $p"; grep -v '^\s*%' $p | grep -v '^\s*$'; done 2>&1 | head -500
```

```
=== ./utils/crossvalidation/cvConds.m
function [trainConds,testConds] = cvConds(trials,ratio)
conds = unique([trials().condNum]);
for cond = conds
    inds = find([trials().condNum] == cond);
    inds = inds(randperm(length(inds)));
    trainInds = inds(1:round(end*ratio));
    testInds = inds(1+round(end*ratio):end);
    condInd = find(conds == cond);
    trainConds(condInd).matrix = assembleCond(trials(trainInds));
    testConds(condInd).matrix = assembleCond(trials(testInds));
end
end
=== ./utils/TBFandCondSpecificDynamics/bioEigs.m
function useEigs = bioEigs(useEigs)
for i = 1:length(useEigs)
    if abs(useEigs(i)) > 0.9993
        useEigs(i) = 0.9993*useEigs(i)/abs(useEigs(i));
    end
end
[... 367 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public-b65f28d; for f in getRotations getRotationalProjCompare corrOverlapWithjPCA getCorrOverlapWithjPCA quantifyProjectedVarianceSingleFrequency singleFrequencyOverlapControl quantifyProjectedVarianceDifferentFrequencies warpTrials warpTrial; do p=$(find . -name "$f.m"|head -1); echo "=== $p"; grep -v '^\s*%' $p | grep -v '^\s*$'; done 2>&1 | head -600
```

```
=== ./reconciliation/jPCAReconciliation/getRotations.m
function [rotations,reconstruction,varExplained,R2s] = getRotations(loadings,basisFxns,planeNum)
data = loadings;
for cond = 1:size(loadings,2)
    data(cond).matrix = loadings(cond).matrix*basisFxns.';
end
meanResponse = 0;
for cond = 1:size(data,2)
    meanResponse = meanResponse + data(cond).matrix/size(data,2);
end
useData = data;
for cond = 1:size(data,2)
    useData(cond).A = data(cond).matrix.' - meanResponse.';
end
softNorms = 1./(range(vertcat(useData().A))+5);
for cond = 1:size(data,2)
    useData(cond).A = softNorms.*useData(cond).A;
    useData(cond).A = useData(cond).A(20:40,:);
end
[~,summary] = jPCA(useData);
[... 335 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > t3.py <<'EOF'
import remfile,h5py,numpy as np,time
aid='75013796-4a2d-41dc-9eb6-db9d365b28b4'
h=h5py.File(remfile.File(f'https://api.dandiarchive.org/api/assets/{aid}/download/'),'r')
t=h['intervals/trials']
mc=t['maze_condition'][:]; nt=t['maze_num_targets'][:]; nb=t['maze_num_barriers'][:]; s=t['task_success'][:]
print('mc%3==0 vs nt==3', np.unique(list(zip(mc%3==0, nt==3)),axis=0,return_counts=True))
print('cond 0:', (mc==0).sum(), nt[mc==0], nb[mc==0][:5])
for r in range(3): print(r, np.unique(nb[(mc%3==r)&(mc>0)],return_counts=True), np.unique(nt[(mc%3==r)&(mc>0)],return_counts=True))
print('trial_version by mc%3', [np.unique(t['trial_version'][:][(mc%3==r)&(mc>0)]) for r in range(3)])
delay=t['go_cue_time'][:]-t['target_presentation_time'][:]
print('delay', np.percentile(delay,[0,5,25,50,75,100]))
keep=(mc>0)&(mc%3!=0)
for name,m in [('succ',keep&(s==1)),('succ delay>400',keep&(s==1)&(delay>0.4)),('succ&!unhit',keep&(s==1)&(t['unhittable'][:]==0)),('succ&correct',keep&(s==1)&(t['correct_reach'][:]==1)),('succ&correct&d>400',keep&(s==1)&(t['correct_reach'][:]==1)&(delay>0.4))]:
    print(name, m.sum(), len(np.unique(mc[m])))
print('unhittable by mc%3', [t['unhittable'][:][(mc%3==r)&(mc>0)].sum() for r in range(3)])
T=time.time(); st=h['units/spike_times']; idx=h['units/spike_times_index'][:]
x=st[0:idx[0]]; print('unit0',len(x),time.time()-T)
T=time.time(); x=st[:20_000_000]; print('20M',time.time()-T)
EOF
python t3.py
```

```
mc%3==0 vs nt==3 (array([[False, False],
       [ True, False],
       [ True,  True]]), array([1625,  129,  882]))
cond 0: 203 [1 1 3 3 1 3 1 3 1 1 3 1 1 1 1 1 1 1 3 1 3 1 1 3 1 1 3 1 3 1 1 3 1 1 1 1 3
 3 1 1 1 1 1 3 1 1 3 3 1 1 3 1 1 3 1 3 1 1 1 1 1 3 1 1 1 3 1 3 3 1 3 1 1 3
 3 1 1 3 1 1 3 3 3 3 3 1 1 1 1 1 3 1 1 1 3 1 3 1 1 1 3 3 1 1 1 3 3 1 3 3 1
 3 1 3 3 3 1 1 1 1 1 1 1 1 1 3 3 1 1 3 1 3 1 1 1 3 1 3 3 1 1 1 1 1 1 1 3 1
 3 1 3 1 1 1 3 1 1 1 3 3 1 1 3 1 1 1 1 1 3 3 1 3 1 1 1 1 1 3 3 3 1 1 3 3 1
 3 3 1 1 1 3 1 1 3 1 3 1 3 1 1 3 1 1] [2 2 9 7 7]
0 (array([6, 7, 8, 9], dtype=uint8), array([ 69, 201, 199, 339])) (array([3], dtype=uint8), array([808]))
1 (array([0], dtype=uint8), array([808])) (array([1], dtype=uint8), array([808]))
2 (array([6, 7, 8, 9], dtype=uint8), array([ 66, 201, 222, 328])) (array([1], dtype=uint8), array([817]))
trial_version by mc%3 [array([2], dtype=uint8), array([0], dtype=uint8), array([1], dtype=uint8)]
delay [-0.004  0.147  0.498  0.664  0.831  0.998]
succ 1595 72
succ delay>400 1381 72
succ&!unhit 1595 72
succ&correct 1557 72
succ&correct&d>400 1345 72
unhittable by mc%3 [np.uint64(0), np.uint64(0), np.uint64(0)]
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; wc -c *.txt; grep -n "^Methods\|^Subjects\|Fitting dynamics\|De-mixing\|Explaining variab\|LDR encoding\|LDR-based decoding\|Extracting kinematic\|Control for\|Measuring the\|Estimating the dim\|Predicting rot\|Comparing the\|Quantifying" 10.1038-s41467-024-51308-7.txt | head -40; date -u
```

```
<persisted-output>
Output too large (101.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/3393396e-2a5d-41a5-a4a5-dabf9d45b058/tool-results/baz6wp4k9.txt

Preview (first 2KB):
131342 10.1038-s41467-024-51308-7.txt
7:pmc Nat Commun Nat Commun Nature Communications 2041-1723 Nature Publishing Group UK London 11325044 39143078 51308 10.1038/s41467-024-51308-7 Article Reach-dependent reorientation of rotational dynamics in motor cortex Sabatini David A. 1 2 http://orcid.org/0000-0002-8072-023X Kaufman Matthew T. [removed: an e-mail address] 1 2 1 https://ror.org/024mw5h28 grid.170205.1 0000 0004 1936 7822 Department of Organismal Biology and Anatomy, The University of Chicago, Chicago, IL 60637 USA 2 grid.170205.1 0000 0004 1936 7822 Neuroscience Institute, The University of Chicago, Chicago, IL 60637 USA 15 8 2024 15 8 2024 2024 15 7007 2 9 2023 5 8 2024 © The Author(s) 2024 2024 https://creativecommons.org/licenses/by-nc-nd/4.0/ Open Access This article is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License, which permits any non-commercial use, sharing, distribution and reproduction in any medium or format, as long as you give appropriate credit to the original author(s) and the source, provide a link to the Creative Commons licence, and indicate if you modified the licensed material. You do not have permission under this licence to share adapted material derived from this article or parts of it. The images or other third party material in this article are included in the article’s Creative Commons licence, unless indicated otherwise in a credit line to the material. If material is not included in the article’s Creative Commons licence and your intended use is not permitted by statutory regulation or exceeds the permitted use, you will need to obtain permission directly from the copyright holder. To view a copy of this licence, visit http://creativecommons.org/licen
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd paper; python3 -c "
t=open('10.1038-s41467-024-51308-7.txt').read()
i=t.find('Subjects, behavior and data pre-processing')
print(i, len(t))
import textwrap
s=t[i:i+60000]
open('/tmp/claude/m.txt','w') if False else None
print(s[:30000])
" | fold -w 200 -s | head -300; date -u
```

```
<persisted-output>
Output too large (29.7KB). Full output saved to: /home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/3393396e-2a5d-41a5-a4a5-dabf9d45b058/tool-results/b44n65ou8.txt

Preview (first 2KB):
48870 130447
Subjects, behavior and data pre-processing All data used here have been analyzed in previous studies. Animal protocols were approved by the Stanford University Animal Care and Use Committee. Two 
adult male rhesus macaque monkeys ( Macaca mulatta ), J and N, performed the “maze” center-out delayed-reaching task for juice reward 19 . Briefly, the monkey initially fixated a central point on a 
vertical screen with the eye and a cursor floating slightly above the fingertips, then a slightly jittering target was shown. After a brief delay (0–1000 ms), a Go cue was presented (cessation of 
target jitter, filling in of target, and disappearance of fixation point), and the monkey was required to make a fast, accurate reach to the target. On some trials, the monkey was required to avoid 
virtual barriers presented at the same time as the target, eliciting curved reaches to produce 72 different reaching “conditions” (36 straight, 36 curved). For both monkeys, data were collected using 
two 96-electrode “Utah” arrays (Blackrock Microsystems, Salt Lake City, UT), one implanted in PMd and one in M1. Both single-units and stable multi-units were included for analysis. Spiking activity 
was binned at 1 millisecond, smoothed with a 20 ms Gaussian kernel, trial-averaged, and down-sampled to 10 millisecond resolution. Except where noted, all analyses were performed on each dataset 
(monkey and array) independently. Fitting dynamics to single conditions Condition-specific dynamics were examined by fitting, for each condition independently, a discrete-time linear dynamical system 
to population activity from 150 ms prior to movement onset to 850 ms after movement onset. If an eigenvalue in a fit LDS had a half-life >10 s, it was reduced to 10
[... 3 more lines not kept]
```

**Agent calls Read**

```json
{
 "file_path": "/home/runner/.claude/projects/-home-runner-work-encore-registry-encore-registry/3393396e-2a5d-41a5-a4a5-dabf9d45b058/tool-results/b44n65ou8.txt"
}
```

```
1	48870 130447
2	Subjects, behavior and data pre-processing All data used here have been analyzed in previous studies. Animal protocols were approved by the Stanford University Animal Care and Use Committee. Two 
3	adult male rhesus macaque monkeys ( Macaca mulatta ), J and N, performed the “maze” center-out delayed-reaching task for juice reward 19 . Briefly, the monkey initially fixated a central point on a 
4	vertical screen with the eye and a cursor floating slightly above the fingertips, then a slightly jittering target was shown. After a brief delay (0–1000 ms), a Go cue was presented (cessation of 
5	target jitter, filling in of target, and disappearance of fixation point), and the monkey was required to make a fast, accurate reach to the target. On some trials, the monkey was required to avoid 
6	virtual barriers presented at the same time as the target, eliciting curved reaches to produce 72 different reaching “conditions” (36 straight, 36 curved). For both monkeys, data were collected using 
7	two 96-electrode “Utah” arrays (Blackrock Microsystems, Salt Lake City, UT), one implanted in PMd and one in M1. Both single-units and stable multi-units were included for analysis. Spiking activity 
8	was binned at 1 millisecond, smoothed with a 20 ms Gaussian kernel, trial-averaged, and down-sampled to 10 millisecond resolution. Except where noted, all analyses were performed on each dataset 
9	(monkey and array) independently. Fitting dynamics to single conditions Condition-specific dynamics were examined by fitting, for each condition independently, a discrete-time linear dynamical system 
10	to population activity from 150 ms prior to movement onset to 850 ms after movement onset. If an eigenvalue in a fit LDS had a half-life >10 s, it was reduced to 10 s. We fit the LDS using 
11	reduced-rank regression to find the optimal low-rank LDS that explained maximum variance in that condition’s neural activity. We determined the dimensionality of the LDS via cross-vali
[... 190 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > t4.py <<'EOF'
import remfile,h5py,numpy as np
for aid in ['75013796-4a2d-41dc-9eb6-db9d365b28b4','1b8d9330-6052-4a43-854f-c63eaa826acd']:
    h=h5py.File(remfile.File(f'https://api.dandiarchive.org/api/assets/{aid}/download/'),'r')
    ts=h['processing/behavior/Position/Hand/timestamps'][:200000]
    print('dt', np.unique(np.round(np.diff(ts),5),return_counts=True))
    d=h['processing/behavior/Position/Hand/data'][:200000]; print('hand range',np.nanmin(d,0),np.nanmax(d,0))
    t=h['intervals/trials']; on=t['move_begins_time'][:]; st=t['start_time'][:]; sp=t['stop_time'][:]
    print('ntr',len(on),'pre',np.percentile(on-st,[0,1,50]),'post',np.percentile(sp-on,[0,1,50]))
    print('offline-online',np.nanpercentile(t['offline_move_onset_time'][:]-on,[1,50,99]))
    print('unit counts', h['units/spike_times_index'][:5], [x for x in h['general/extracellular_ephys/electrodes/location'][[0,95,96,191]]], h['units/electrodes'][[0,95,96,191]])
    print('tp', t['target_positions'][:6], t['hit_target_position'][:3])
    mc=t['maze_condition'][:]; print('n conds', len(np.unique(mc)), 'succ',(t['task_success'][:]==1).sum(), 'keep',((mc>0)&(mc%3!=0)&(t['task_success'][:]==1)).sum(),'d>400',((mc>0)&(mc%3!=0)&(t['task_success'][:]==1)&(t['go_cue_time'][:]-t['target_presentation_time'][:]>0.4)).sum())
EOF
python t4.py
```

```
dt (array([1.00000e-03, 1.19500e+00, 1.27530e+00, 1.29990e+00, 1.30000e+00,
       1.32503e+00, 1.32977e+00, 1.32987e+00, 1.35013e+00, 1.36500e+00,
       1.39000e+00, 1.39503e+00, 1.40013e+00, 1.40487e+00, 1.40503e+00,
       1.40980e+00, 1.40987e+00, 1.41513e+00, 1.41990e+00, 1.42503e+00,
       1.42997e+00, 1.43003e+00, 1.43013e+00, 1.45013e+00, 1.45490e+00,
       1.45987e+00, 1.45993e+00, 1.46500e+00, 1.47000e+00, 1.47010e+00,
       1.47500e+00, 1.47513e+00, 1.47990e+00, 1.48980e+00, 1.48990e+00,
       1.49000e+00, 1.49490e+00, 1.49500e+00, 1.49990e+00, 1.51013e+00,
       1.52013e+00, 1.52997e+00, 1.53013e+00, 1.53490e+00, 1.53507e+00,
       1.53990e+00, 1.54000e+00, 1.54503e+00, 1.54987e+00, 1.55510e+00,
       1.56990e+00, 1.57003e+00, 1.57500e+00, 1.59503e+00, 1.68990e+00,
       1.69000e+00, 1.70000e+00, 1.70500e+00, 1.74527e+00, 2.54513e+00,
       2.89027e+00, 3.00027e+00, 3.04527e+00, 6.83497e+00, 6.95003e+00,
       7.02013e+00, 9.46003e+00]), array([199930,      1,      1,      1,      1,      1,      1,      1,
            1,      1,      1,      1,      1,      1,      1,      1,
            1,      1,      1,      1,      1,      1,      1,      2,
            1,      1,      1,      1,      1,      1,      1,      1,
            1,      1,      1,      1,      1,      1,      1,      1,
            2,      1,      1,      1,      1,      2,      1,      1,
            1,      1,      1,      1,      1,      1,      1,      1,
[... 52 more lines not kept]
```

**Agent calls Write**

```json
{
 "file_path": "entries/sabatini-2024/ldr.py",
 "content": "\"\"\"Loading and measures for testing Sabatini & Kaufman (2024) on DANDI:000070.\n\nThe paper reanalyses the maze-task sessions of Churchland et al. (2010, 2012):\ntwo monkeys (J, N), one PMd and one M1 Utah array each, analysed as four\ndatasets (M1-J, PMd-J, M1-N, PMd-N). Its Data availability statement names the\ntwo sessions read here (SESSIONS).\n\nWhere each parameter comes from is said beside it:\n- \"claims\": the claims file's criterion or shared method (claims/sabatini-2024.yaml),\n  which cites the paper or its code (github.com/kaufmanlab/LDR-public at b65f28d).\n- \"paper\": a passage of the paper (author, step 1.6), cited.\n- \"code\": the paper's code at b65f28d, where the claims file defers to it.\n- \"assumption\": a choice the paper leaves open, with the reason.\n- \"standard\": a detail that cannot change a result.\n\"\"\"\nimport zlib\nimport numpy as np\nimport requests\nimport h5py\nimport remfile\nfrom scipy.ndimage import gaussian_filter1d\nfrom scipy import stats\n\nDANDISET = \"000070\"\nVERSION = \"0.261122.2046\"   # most recent published version; the paper cites none\nAPI = \"https://api.dandiarchive.org/api\"\nSESSIONS = {  # paper, Data availability\n    \"J\": \"sub-Jenkins/sub-Jenkins_ses-20090918_behavior+ecephys.nwb\",\n    \"N\": \"sub-Nitschke/sub-Nitschke_ses-20100923_behavior+ecephys.nwb\",\n}\nDATASETS = [\"M1-J\", \"PMd-J\", \"M1-N\", \"PMd-N\"]\nPAPER_KEY = \"sabatini-2024\"\n\n# Time base (claims, shared method): -350 to +850 ms around movement onset, 1 ms\n# bins, down-sampled every 10 ms to 121 bins. Dynamics are fitted from bin 20\n# (MATLAB index; 0-based 19, -160 ms on this grid) on.\nPRE_MS, POST_MS = 350, 850\nNT = 121\nT0 = 19          # 0-based index of MATLAB bin 20\nTIMES = np.arange(-PRE_MS, POST_MS + 1, 10)  # ms, 121 values\n\n\ndef seed(claim, k=0):\n    \"\"\"Seed of a claim's generator (protocol, author step 3); k adds 0, 1000, ...\"\"\"\n    return zlib.crc32(f\"{PAPER_KEY}/{claim}\".encode()) + k\n\n\ndef rng(claim, k=0):\n    return np.random.default_rng(seed(claim, k))\n\n\n# --------------------------------------------------------------------- loading\ndef asset(path, version=VERSION):\n    r = requests.get(f\"{API}/dandisets/{DANDISET}/versions/{version}/assets/\",\n                     params={\"path\": path}, timeout=60)\n    r.raise_for_status()\n    res = [a for a in r.json()[\"results\"] if a[\"path\"] == path]\n    return res[0][\"asset_id\"]\n\n\ndef open_nwb(path, version=VERSION):\n    aid = asset(path, version)\n    return h5py.File(remfile.File(f\"{API}/assets/{aid}/download/\"), \"r\")\n\n\ndef trial_table(h):\n    t = h[\"intervals/trials\"]\n    cols = [\"maze_condition\", \"task_success\", \"maze_num_targets\", \"maze_num_barriers\",\n            \"go_cue_time\", \"target_presentation_time\", \"move_begins_time\",\n            \"offline_move_onset_time\", \"start_time\", \"stop_time\", \"discard_trial\",\n            \"correct_reach\", \"trial_version\", \"unhittable\"]\n    import pandas as pd\n    d = pd.DataFrame({c: t[c][:] for c in cols})\n    d[\"delay\"] = d.go_cue_time - d.target_presentation_time\n    return d\n\n\ndef select_trials(d, reading=\"all\"):\n    \"\"\"The 72 conditions and the trials (claims, shared method).\n\n    Conditions: maze conditions 1 to 108 without the multiples of 3 (reading a;\n    in this file these are exactly the 3-target versions, reading b). Condition 0\n    (no maze condition) is left out. Trials: successful (reading 'all') or\n    successful with delay above 400 ms (reading 'delay400').\"\"\"\n    m = (d.maze_condition > 0) & (d.maze_condition % 3 != 0) & (d.task_success == 1)\n    if reading == \"delay400\":\n        m &= d.delay > 0.4\n    return m.values\n\n\ndef load_session(monkey, reading=\"all\"):\n    \"\"\"Spike counts at 1 ms and hand position for the selected trials.\n\n    Alignment on move_begins_time, the file's \"movement onset time\"\n    (assumption: the paper says only \"aligned to movement onset\"; the offline\n    onset is shown in the data check). Counts cover -355 to +855 ms so that both\n    the smoothed grid (-350..850) and 10 ms count bins centred on it can be formed.\n    Trials whose window runs past the end of the trial (spikes are stored within\n    trials only) are dropped and counted.\"\"\"\n    h = open_nwb(SESSIONS[monkey])\n    d = trial_table(h)\n    sel = select_trials(d, reading)\n    on = d.move_begins_time.values\n    t0 = on - (PRE_MS + 5) / 1000\n    t1 = on + (POST_MS + 5) / 1000\n    covered = (t0 >= d.start_time.values) & (t1 <= d.stop_time.values)\n    dropped = int((sel & ~covered).sum())\n    sel &= covered\n    idx = np.where(sel)[0]\n    tr = d.iloc[idx].reset_index(drop=True)\n    tr[\"trial_index\"] = idx\n    nb = PRE_MS + POST_MS + 11  # 1211 edges -> 1210 bins of 1 ms\n    st_index = h[\"units/spike_times_index\"][:]\n    loc = h[\"general/extracellular_ephys/electrodes/location\"][:].astype(str)\n    uel = h[\"units/electrodes\"][:]\n    allsp = h[\"units/spike_times\"][:]\n    counts = np.zeros((len(idx), len(st_index), nb - 1), dtype=np.uint8)\n    starts = np.r_[0, st_index[:-1]]\n    for u in range(len(st_index)):\n        sp = allsp[starts[u]:st_index[u]]\n        i0 = np.searchsorted(sp, t0[idx])\n        i1 = np.searchsorted(sp, t1[idx])\n        for j in range(len(idx)):\n            x = sp[i0[j]:i1[j]]\n            if len(x):\n                b = np.floor((x - t0[idx[j]]) * 1000).astype(int)\n                b = b[(b >= 0) & (b < nb - 1)]\n                np.add.at(counts[j, u], b, 1)\n    sorted_ok = bool(np.all(np.diff(allsp[: min(len(allsp), 2_000_000)]) >= -1e-9) or True)\n    del allsp\n    # hand position, 1 kHz within trials (checked in the data check)\n    hts = h[\"processing/behavior/Position/Hand/timestamps\"]\n    hd = h[\"processing/behavior/Position/Hand/data\"]\n    ts_all = hts[:]\n    hand = np.zeros((len(idx), PRE_MS + POST_MS + 1, 2))\n    grid = np.arange(-PRE_MS, POST_MS + 1) / 1000\n    for j, k in enumerate(idx):\n        a = np.searchsorted(ts_all, on[k] - 0.4)\n        b = np.searchsorted(ts_all, on[k] + 0.9)\n        x = hd[a:b]\n        tt = ts_all[a:b]\n        for c in range(2):\n            hand[j, :, c] = np.interp(on[k] + grid, tt, x[:, c])\n    del ts_all\n    region = np.array([\"PMd\" if \"Pre-Motor\" in loc[e] else \"M1\" for e in uel])\n    conds = np.sort(tr.maze_condition.unique())\n    cond_index = np.searchsorted(conds, tr.maze_condition.values)\n    h.close()\n    return dict(monkey=monkey, trials=tr, counts=counts, hand=hand, region=region,\n                conds=conds, cond=cond_index, dropped_uncovered=dropped,\n                n_trials_file=len(d), table=d)\n\n\n# --------------------------------------------------------------- preprocessing\ndef smooth(counts):\n    \"\"\"Claims, shared method; code preprocessTrials.m: 1 ms counts x 1000, Gaussian\n    s.d. 20 ms over 111 taps (truncate 55/20), symmetric padding ('reflect' in\n    scipy equals MATLAB 'symmetric'), every 10th sample. counts: (..., 1210) from\n    -355 ms; the smoothed grid is -350..850 (bins 5..1205).\"\"\"\n    x = counts[..., 5:5 + PRE_MS + POST_MS + 1].astype(np.float32) * 1000\n    y = gaussian_filter1d(x, 20, axis=-1, mode=\"reflect\", truncate=55 / 20)\n    return y[..., ::10]\n\n\ndef smooth_trials(counts, chunk=200):\n    out = np.zeros(counts.shape[:2] + (NT,), np.float32)\n    for i in range(0, counts.shape[0], chunk):\n        out[i:i + chunk] = smooth(counts[i:i + chunk])\n    return out\n\n\ndef binned_counts(counts):\n    \"\"\"Code kinFromTBFSingleTrial / Methods, LDR-based decoding (claims): 1 ms counts\n    summed in 10 ms bins centred on the grid times, scaled to spikes/s.\"\"\"\n    c = counts[..., :NT * 10].astype(np.float32)\n    return c.reshape(c.shape[:-1] + (NT, 10)).sum(-1) * 100\n\n\ndef cond_average(trials_x, cond, n_cond=72):\n    return np.stack([trials_x[cond == c].mean(0) for c in range(n_cond)])\n\n\ndef split_halves(cond, g, ratio=0.5):\n    \"\"\"Code cvConds.m: per condition, trials permuted and the first round(n*ratio)\n    assigned to the first partition.\"\"\"\n    a = np.zeros(len(cond), bool)\n    for c in np.unique(cond):\n        ii = np.where(cond == c)[0]\n        ii = ii[g.permutation(len(ii))]\n        a[ii[: int(np.floor(len(ii) * ratio + 0.5))]] = True\n    return a\n\n\n# -------------------------------------------------------------------- measures\ndef var_explained(X, Xhat, clip=True):\n    \"\"\"Code getVarExplained.m ('ind'): per condition, 1 - summed variance over\n    neurons of the residual over time / summed variance of the data, over the\n    bins where Xhat is not NaN; negatives set to 0. X, Xhat: (C, N, T).\"\"\"\n    ok = ~np.isnan(Xhat[0, 0])\n    r = X[..., ok] - Xhat[..., ok]\n    ve = 1 - r.var(-1, ddof=1).sum(-1) / X[..., ok].var(-1, ddof=1).sum(-1)\n    return np.clip(ve, 0, None) if clip else ve\n\n\ndef alignment_index(D, S):\n    \"\"\"Code getAlignmentIndex.m: fraction of the variance of D (N x T) captured by\n    projection onto span(S) (N x d), negatives 0.\"\"\"\n    ok = ~np.isnan(D[0])\n    D = D[:, ok]\n    P = S @ np.linalg.pinv(S)\n    r = D - P @ D\n    a = 1 - r.var(1, ddof=1).sum() / D.var(1, ddof=1).sum()\n    return max(a, 0.0)\n\n\ndef bio_eigs(e):\n    \"\"\"Code bioEigs.m: |eigenvalue| capped at 0.9993 (half-life 10 s at 100 Hz; paper,\n    Methods, Fitting dynamics to single conditions).\"\"\"\n    e = e.copy()\n    big = np.abs(e) > 0.9993\n    e[big] = 0.9993 * e[big] / np.abs(e[big])\n    return e\n\n\ndef freq_hz(e):\n    \"\"\"Code extractParams.m: angle / 2 pi x 100 Hz.\"\"\"\n    return 100 * np.abs(np.angle(e)) / (2 * np.pi)\n\n\ndef get_basis(X, k):\n    \"\"\"Code getBasisFxns.m: SVD of the (neurons x conditions)-by-time matrix of the\n    unnormalised rates (claims); returns basis (T x k) and loadings (C, N, k).\"\"\"\n    C, N, T = X.shape\n    _, _, Vt = np.linalg.svd(X.reshape(C * N, T), full_matrices=False)\n    B = Vt[:k].T\n    L = X @ np.linalg.pinv(B.T)\n    return B, L\n\n\ndef pair_ids(e):\n    \"\"\"Group eigenvalues into conjugate pairs and real modes; sorted by frequency\n    (code pairID.m groups by real part and |imag|).\"\"\"\n    key = np.round(np.real(e), 10) + 1j * np.round(np.abs(np.imag(e)), 10)\n    uniq = []\n    ids = np.zeros(len(e), int)\n    for i, kk in enumerate(key):\n        for j, u in enumerate(uniq):\n            if abs(u - kk) < 1e-8:\n                ids[i] = j\n                break\n        else:\n            uniq.append(kk)\n            ids[i] = len(uniq) - 1\n    return ids\n\n\ndef eig_transform(X, k):\n    \"\"\"Code eigTransform.m (claims, shared method): de-mix the raw SVD basis by an\n    LDS fitted from bin 20 on, replace the basis by damped sinusoids of the fitted\n    frequencies and half-lives (NaN before bin 20), and correct the loadings.\"\"\"\n    C, N, T = X.shape\n    Braw, L = get_basis(X, k)\n    A = Braw[T0 + 1:].T @ np.linalg.pinv(Braw[T0:-1].T)\n    e = np.linalg.eigvals(A)\n    e = bio_eigs(e)\n    e = e[np.argsort(np.abs(np.angle(e)) / (2 * np.pi), kind=\"stable\")]\n    # within a conjugate pair put the positive-imaginary one first\n    ids = pair_ids(e)\n    Bsim = Braw.copy()\n    for t in range(T0 + 1, T - 20):  # code: for t = 21:(T-20)\n        Bsim[t] = A @ Bsim[t - 1]\n    ff = np.zeros((k, 3))\n    for el in np.unique(ids):\n        inds = np.where(ids == el)[0]\n        ue = e[inds[0]]\n        if np.imag(ue) < 0:\n            ue = np.conj(ue)\n        f = np.angle(ue) / (2 * np.pi)\n        tau = -np.log(np.abs(ue))\n        ff[inds[0]] = [f, 0, tau]\n        if len(inds) == 2:\n            ff[inds[1]] = [f, -np.pi / 2, tau]\n    ts = np.r_[np.full(T0, np.nan), np.arange(T - T0)]\n    Bp = np.zeros((T, k))\n    for c in range(k):\n        Bp[:, c] = np.exp(-ff[c, 2] * ts) * np.cos(2 * np.pi * ff[c, 0] * ts + ff[c, 1])\n    corr = np.linalg.pinv(Bsim[T0:]) @ Bp[T0:]\n    Lc = L @ np.linalg.pinv(corr.T)\n    raw = (corr.T @ Braw.T).T\n    return dict(B=Bp, L=Lc, ids=ids, eig=e, freq=100 * ff[:, 0], halflife=np.where(\n        ff[:, 2] > 0, np.log(2) / np.maximum(ff[:, 2], 1e-12) / 100, np.inf),\n        Braw=Braw, Lraw=L, raw=raw, corr=corr)\n\n\ndef groups(tbf):\n    \"\"\"Rotation groups (pairs) and the offset (a real mode at zero frequency), by\n    frequency; returns list of (freq, column indices).\"\"\"\n    out = []\n    for el in np.unique(tbf[\"ids\"]):\n        inds = np.where(tbf[\"ids\"] == el)[0]\n        out.append((float(tbf[\"freq\"][inds[0]]), inds))\n    return sorted(out, key=lambda x: x[0])\n\n\ndef reconstruct(L, B):\n    return L @ B.T\n\n\ndef cv_tbf_k(Xtr, cond, g, folds=100, kmax=20, ratio=0.5):\n    \"\"\"Code crossValidateDimensionalityBasisFxns.m (claims): halves of trials,\n    basis and loadings from one half, mean held-out variance explained per k;\n    an even best k raised by one.\"\"\"\n    loss = np.zeros((kmax, folds))\n    for f in range(folds):\n        a = split_halves(cond, g, ratio)\n        Xa = cond_average(Xtr[a], cond[a])\n        Xb = cond_average(Xtr[~a], cond[~a])\n        C, N, T = Xa.shape\n        _, _, Vt = np.linalg.svd(Xa.reshape(C * N, T), full_matrices=False)\n        for k in range(1, kmax + 1):\n            B = Vt[:k].T\n            loss[k - 1, f] = var_explained(Xb, (Xa @ B) @ B.T).mean()\n    m = loss.mean(1)\n    best = int(np.argmax(m)) + 1\n    chosen = best + 1 if best % 2 == 0 else best\n    return dict(loss=loss, mean=m, best=best, k=chosen)\n\n\n# ----------------------------------------------------- single-condition LDS\ndef lds_fit(Xc, k, cap=True):\n    \"\"\"Code idDynamics.m: least-squares dynamics from bin 20 on, reduced to rank k\n    by the top k left singular vectors of A X (reduced-rank regression); simulated\n    forward from the state at bin 20. Eigenvalues capped at 10 s half-life\n    (paper, Methods), also in the simulation (cap=True; the code caps only the\n    reported eigenvalues). Returns eigenvalues sorted by frequency and the\n    simulation (NaN before bin 20).\"\"\"\n    X1 = Xc[:, T0:-1]\n    X2 = Xc[:, T0 + 1:]\n    A = X2 @ np.linalg.pinv(X1)\n    U, _, _ = np.linalg.svd(A @ Xc[:, T0:], full_matrices=False)\n    U = U[:, :k]\n    Ak = U.T @ A @ U\n    w, V = np.linalg.eig(Ak)\n    if cap:\n        wc = bio_eigs(w)\n        if np.any(wc != w):\n            Ak = np.real(V @ np.diag(wc) @ np.linalg.inv(V))\n        w = wc\n    else:\n        w = bio_eigs(w)\n    w = w[np.argsort(np.abs(np.angle(w)), kind=\"stable\")]\n    sim = np.full_like(Xc, np.nan)\n    sim[:, T0] = Xc[:, T0]\n    z = U.T @ A @ Xc[:, T0]\n    for t in range(T0 + 1, Xc.shape[1]):\n        sim[:, t] = U @ z\n        z = Ak @ z\n    return w, sim\n\n\ndef lds_eigs(Xc, k):\n    X1 = Xc[:, T0:-1]\n    X2 = Xc[:, T0 + 1:]\n    A = X2 @ np.linalg.pinv(X1)\n    U, _, _ = np.linalg.svd(A @ Xc[:, T0:], full_matrices=False)\n    U = U[:, :k]\n    w = bio_eigs(np.linalg.eigvals(U.T @ A @ U))\n    return w[np.argsort(np.abs(np.angle(w)), kind=\"stable\")]\n\n\ndef sort_eigs(w):\n    \"\"\"Eigenvalues sorted by |frequency|, then the member of a pair with positive\n    imaginary part first (correspondence between conditions).\"\"\"\n    order = np.lexsort((-np.imag(w), np.round(np.abs(np.angle(w)), 8)))\n    return w[order]\n\n\n# ---------------------------------------------------------------------- jPCA\ndef skew_regress(dX, X):\n    \"\"\"Least-squares skew-symmetric M with dX ~ X M (jPCA codepack skewSymRegress).\"\"\"\n    k = X.shape[1]\n    iu = np.triu_indices(k, 1)\n    H = np.zeros((k * k, len(iu[0])))\n    for n, (i, j) in enumerate(zip(*iu)):\n        Mm = np.zeros((k, k))\n        Mm[i, j] = 1\n        Mm[j, i] = -1\n        H[:, n] = Mm.flatten(order=\"F\")\n    Xbig = np.kron(np.eye(k), X)\n    p = np.linalg.lstsq(Xbig @ H, dX.flatten(order=\"F\"), rcond=None)[0]\n    return (H @ p).reshape(k, k, order=\"F\")\n\n\ndef jpca(A_list, num_pcs=6, soften=10, mean_sub=True):\n    \"\"\"jPCA (Churchland et al. 2012 codepack, default parameters: 6 PCs, soft\n    normalisation range+10, mean subtraction across conditions), on a list of\n    (T x N) matrices. Returns the planes in high-d space (N x num_pcs, ordered\n    by plane) and R2 of the skew-symmetric and unconstrained fits in the top plane.\"\"\"\n    A = np.stack(A_list)  # C x T x N\n    if soften is not None:\n        rng_ = A.reshape(-1, A.shape[-1]).max(0) - A.reshape(-1, A.shape[-1]).min(0)\n        A = A / (rng_ + soften)\n    if mean_sub:\n        A = A - A.mean(0, keepdims=True)\n    big = A.reshape(-1, A.shape[-1])\n    mu = big.mean(0)\n    _, _, Vt = np.linalg.svd(big - mu, full_matrices=False)\n    P = Vt[:num_pcs].T\n    red = (A - mu) @ P  # C x T x k\n    pre = red[:, :-1].reshape(-1, num_pcs)\n    dst = (red[:, 1:] - red[:, :-1]).reshape(-1, num_pcs)\n    Mbest = np.linalg.lstsq(pre, dst, rcond=None)[0]\n    Mskew = skew_regress(dst, pre)\n    w, V = np.linalg.eig(Mskew)\n    order = np.argsort(-np.abs(np.imag(w)), kind=\"stable\")\n    planes = []\n    used = set()\n    for i in order:\n        if i in used or np.imag(w[i]) <= 0:\n            continue\n        v = V[:, i]\n        j1, j2 = np.real(v) + np.imag(v), np.real(v) - np.imag(v)  # codepack: v1+v2, (v1-v2)i\n        j1 /= np.linalg.norm(j1)\n        j2 /= np.linalg.norm(j2)\n        planes.append(np.c_[j1, j2])\n        used.add(i)\n    J = np.concatenate(planes, 1)\n    J2 = J[:, :2]\n    def r2(M):\n        d2 = dst @ J2\n        f2 = (pre @ M) @ J2\n        return 1 - ((d2 - f2) ** 2).sum() / ((d2 - d2.mean(0)) ** 2).sum()\n    return dict(jPCs_highD=P @ J, R2_Mskew_2D=r2(Mskew), R2_Mbest_2D=r2(Mbest),\n                Mskew=Mskew, P=P, J=J)\n\n\ndef get_rotations(L, B, plane_num, conds=None):\n    \"\"\"Code getRotations.m (claims): activity reconstructed from the basis,\n    mean-subtracted over conditions, soft-normalised by range + 5, jPCA on bins\n    20 to 40 (0-based 19..39); the retained planes reconstruct the activity.\"\"\"\n    Xr = L @ np.nan_to_num(B).T  # code uses B with NaN rows; jPCA on 20:40 only\n    if conds is not None:\n        Xr = Xr[conds]\n    mean = Xr.mean(0)\n    Ac = np.transpose(Xr - mean, (0, 2, 1))  # C x T x N\n    rng_ = Ac.reshape(-1, Ac.shape[-1]).max(0) - Ac.reshape(-1, Ac.shape[-1]).min(0)\n    sn = 1 / (rng_ + 5)\n    use = [a[T0:40] * sn for a in Ac]\n    jp = jpca(use)\n    J = jp[\"jPCs_highD\"][:, :2 * plane_num]\n    Xn = (Xr - mean) * sn[None, :, None]\n    rot = np.einsum(\"nk,cnt->ckt\", J, Xn)\n    recon = np.einsum(\"nk,ckt->cnt\", J, rot) / sn[None, :, None]\n    Xfull = Xr.copy()\n    Xfull[..., :T0] = np.nan  # basis is NaN before bin 20 in the code\n    ve = var_explained(np.where(np.isnan(Xfull), 0, Xfull),\n                       np.where(np.isnan(Xfull), np.nan, recon))\n    return dict(jp=jp, rot=rot, recon=recon, ve=ve, sn=sn, mean=mean, Xr=Xr)\n\n\n# ---------------------------------------------------------------- statistics\ndef auc_folded(a, b):\n    \"\"\"ROC-AUC of two samples (Mann-Whitney U / n1 n2), folded to >= 0.5 (code\n    compareTrialSimilarity.m).\"\"\"\n    u = stats.mannwhitneyu(a, b).statistic\n    auc = u / (len(a) * len(b))\n    return 0.5 + abs(auc - 0.5), auc\n\n\ndef ridge(X, Y, lam, intercept=True):\n    \"\"\"Ridge regression Y ~ X W (+ b), lambda on W only.\"\"\"\n    if intercept:\n        mx, my = X.mean(0), Y.mean(0)\n        Xc, Yc = X - mx, Y - my\n    else:\n        mx = np.zeros(X.shape[1]); my = np.zeros(Y.shape[1]); Xc, Yc = X, Y\n    W = np.linalg.solve(Xc.T @ Xc + lam * np.eye(X.shape[1]), Xc.T @ Yc)\n    return lambda Z: (Z - mx) @ W + my\n\n\ndef kernel_ou(A, B, ls):\n    d = np.sqrt(((A[:, None, :] - B[None, :, :]) ** 2).sum(-1))\n    return np.exp(-d / ls)\n\n\ndef kernel_gauss(A, B, ls):\n    d2 = ((A[:, None, :] - B[None, :, :]) ** 2).sum(-1)\n    return np.exp(-d2 / (2 * ls ** 2))\n\n\ndef kernel_ridge(X, Y, kern, lam):\n    \"\"\"Kernel ridge regression (centred targets); lam = 0 uses the pseudo-inverse.\"\"\"\n    my = Y.mean(0)\n    K = kern(X, X)\n    if lam > 0:\n        alpha = np.linalg.solve(K + lam * np.eye(len(K)), Y - my)\n    else:\n        alpha = np.linalg.pinv(K) @ (Y - my)\n    return lambda Z: kern(Z, X) @ alpha + my\n\n\ndef folds_over(n, k, g):\n    p = g.permutation(n)\n    return [np.sort(p[i::k]) for i in range(k)]\n"
}
```

```
File created successfully at: entries/sabatini-2024/ldr.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && python3 - <<'EOF'
s=open('ldr.py').read()
s=s.replace("""        j1, j2 = np.real(v) + np.imag(v), np.real(v) - np.imag(v)  # codepack: v1+v2, (v1-v2)i""","""        j1, j2 = np.real(v), -np.imag(v)  # codepack: [v1+v2, (v1-v2)i] of the conjugate pair""")
old=s[s.index("    Xr = L @ np.nan_to_num(B).T"):s.index("    return dict(jp=jp, rot=rot")]
new='''    Xr = L @ B.T  # NaN before bin 20, as the code's de-mixed basis
    if conds is not None:
        Xr = Xr[conds]
    mean = Xr.mean(0)
    Ac = np.transpose(Xr - mean, (0, 2, 1))  # C x T x N
    flat = Ac.reshape(-1, Ac.shape[-1])
    sn = 1 / (np.nanmax(flat, 0) - np.nanmin(flat, 0) + 5)
    use = [a[T0:40] * sn for a in Ac]
    jp = jpca(use)
    J = jp["jPCs_highD"][:, :2 * plane_num]
    Xn = (Xr - mean) * sn[None, :, None]
    rot = np.einsum("nk,cnt->ckt", J, Xn)
    recon = np.einsum("nk,ckt->cnt", J, rot) / sn[None, :, None]
    ve = var_explained(Xr, recon + mean)
'''
s=s.replace(old,new)
open('ldr.py','w').write(s)
EOF
grep -n "recon + mean" ldr.py
```

```
454:    ve = var_explained(Xr, recon + mean)
```

**Agent calls Bash**

```bash
python3 - <<'EOF'
s=open('ldr.py').read()
s=s.replace("""    ve = var_explained(Xr, recon + mean)
""","""    ve = var_explained(Xr, recon)          # code: reconstruction without the mean
    ve_with_mean = var_explained(Xr, recon + mean)   # variant
""")
s=s.replace("return dict(jp=jp, rot=rot, recon=recon, ve=ve,","return dict(jp=jp, rot=rot, recon=recon, ve=ve, ve_with_mean=ve_with_mean,")
open('ldr.py','w').write(s)
EOF
cd $TMPDIR && . env/bin/activate && cat > dev1.py <<'EOF'
import sys,time,resource,numpy as np,pickle
sys.path.insert(0,'entries/sabatini-2024')
import ldr
T=time.time()
S=ldr.load_session('J')
print('load',time.time()-T, S['counts'].shape, S['dropped_uncovered'], resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
T=time.time()
sm=ldr.smooth_trials(S['counts']); print('smooth',time.time()-T, sm.shape)
pickle.dump(dict(sm=sm,cond=S['cond'],hand=S['hand'],region=S['region'],trials=S['trials'],counts=S['counts']),open('J.pkl','wb'),protocol=4)
print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6)
EOF
python dev1.py
```

```
Exit code 1
Traceback (most recent call last):
  File "/tmp/claude-1001/dev1.py", line 5, in <module>
    S=ldr.load_session('J')
  File "entries/sabatini-2024/ldr.py", line 108, in load_session
    sel &= covered
ValueError: output array is read-only
```

**Agent calls Bash**

```bash
sed -i 's/    sel = select_trials(d, reading)/    sel = select_trials(d, reading).copy()/' ldr.py && sed -i '/sorted_ok = /d' ldr.py && cd $TMPDIR && . env/bin/activate && python dev1.py
```

```
load 15.790563344955444 (1595, 192, 1210) 0 1.586184
smooth 13.87313985824585 (1595, 192, 121)
1.65402
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && . env/bin/activate && cat > dev2.py <<'EOF'
import sys,time,numpy as np,pickle
sys.path.insert(0,'entries/sabatini-2024')
import ldr
D=pickle.load(open('J.pkl','rb'))
sm,cond,region=D['sm'],D['cond'],D['region']
for reg in ['M1','PMd']:
    u=region==reg
    Xt=sm[:,u]
    X=ldr.cond_average(Xt,cond)
    rate=X.mean((0,2)); print(reg,'rates',np.percentile(rate,[0,5,50,95,100]).round(2),'n<1Hz',(rate<1).sum())
    T=time.time(); cv=ldr.cv_tbf_k(Xt,cond,ldr.rng('fig3g-basis-frequencies'),folds=20); print('cv',time.time()-T,cv['best'],cv['k'],cv['mean'].round(3))
    tb=ldr.eig_transform(X,cv['k'])
    print('freq',tb['freq'].round(2),'hl',tb['halflife'].round(2))
    ve=ldr.var_explained(X,ldr.reconstruct(tb['L'],tb['B'])); print('TBF VE',ve.mean().round(3),ve.std().round(3))
    Br,Lr=tb['Braw'],tb['Lraw']; print('raw VE whole', ldr.var_explained(X,Lr@Br.T).mean().round(3))
    # recoverability
    ok=~np.isnan(tb['B'][:,0]); rec=[]
    for c in range(72):
        Bh=np.linalg.pinv(tb['L'][c])@X[c][:,ok]; Bt=tb['B'][ok].T
        rec.append(max(0,1-((Bh-Bt).var(1,ddof=1).sum()/Bt.var(1,ddof=1).sum())))
    print('recov',np.mean(rec).round(3))
    pn=2 if reg=='M1' else 1
    r=ldr.get_rotations(tb['L'],tb['B'],pn); print('jPCA R2',r['jp']['R2_Mskew_2D'].round(3),r['jp']['R2_Mbest_2D'].round(3),'VE',r['ve'].mean().round(3),r['ve_with_mean'].mean().round(3))
    for nm,cs in [('str',np.arange(0,72,2)),('cur',np.arange(1,72,2))]:
        rr=ldr.get_rotations(tb['L'],tb['B'],pn,conds=cs); print(nm,rr['jp']['R2_Mskew_2D'].round(3),rr['jp']['R2_Mbest_2D'].round(3))
    for k in [5,7,9]:
        T=time.time(); v=[]
        for c in range(72):
            w,s=ldr.lds_fit(X[c],k); v.append(ldr.var_explained(X[c:c+1],s[None])[0])
        print('LDS',k,np.mean(v).round(3),time.time()-T, ldr.freq_hz(w).round(2))
    # single LDS
    X1=np.concatenate([X[c][:,ldr.T0:-1] for c in range(72)],1); X2=np.concatenate([X[c][:,ldr.T0+1:] for c in range(72)],1)
    M=X2@np.linalg.pinv(X1); v=[];v2=[]
    for c in range(72):
        s=X[c].copy()
        for t in range(ldr.T0+1,121): s[:,t]=M@s[:,t-1]
        v2.append(1-(s-X[c]).var(1,ddof=1).sum()/X[c].var(1,ddof=1).sum())
        s2=s.copy(); s2[:,:ldr.T0]=np.nan; v.append(ldr.var_explained(X[c:c+1],s2[None],clip=False)[0])
    print('singleLDS',np.mean(v).round(3),np.mean(v2).round(3))
EOF
python dev2.py
```

```
M1 rates [19.   21.52 39.03 70.25 86.2 ] n<1Hz 0
cv 3.3928208351135254 7 7 [0.386 0.519 0.655 0.69  0.72  0.728 0.735 0.733 0.729 0.724 0.719 0.713
 0.708 0.702 0.698 0.693 0.689 0.685 0.682 0.679]
freq [0.   0.73 0.73 2.01 2.01 3.38 3.38] hl [4.39 0.43 0.43 0.23 0.23 0.14 0.14]
TBF VE 0.923 0.013
raw VE whole 0.925
recov 0.959
jPCA R2 0.777 0.831 VE 0.091 0.805
str 0.836 0.882
cur 0.713 0.77
LDS 5 0.832 0.2854282855987549 [0.   0.66 0.66 1.9  1.9 ]
LDS 7 0.831 0.2951042652130127 [0.   0.57 0.57 1.49 1.49 2.95 2.95]
LDS 9 0.821 0.28607845306396484 [0.   0.27 0.27 1.35 1.35 2.17 2.17 3.67 3.67]
singleLDS 0.773 0.796
PMd rates [ 17.26  20.3   37.67  75.3  191.5 ] n<1Hz 0
cv 3.406249761581421 7 7 [0.37  0.576 0.755 0.787 0.808 0.81  0.81  0.807 0.802 0.797 0.793 0.788
 0.784 0.779 0.776 0.772 0.769 0.766 0.763 0.761]
freq [0.   0.64 0.64 1.64 1.64 2.64 2.64] hl [9.9  0.33 0.33 0.15 0.15 0.11 0.11]
TBF VE 0.951 0.012
raw VE whole 0.953
[... 9 more lines not kept]
```

**Agent calls Bash**

```bash
date -u; cd $TMPDIR/LDR-public-b65f28d; for f in oneComponentToAnother predictOneComponentFromAnother offsetToRotations kinToTBF predictDataUsingTBFandKinCondStructure predictDataUsingTBFandKinCondStructureNonlinear evalKernel crossValidateDimensionalityRotations getCorrelationsWithFrequency; do p=$(find . -name "$f.m"|head -1); echo "=== $p"; grep -v '^\s*%' $p | grep -v '^\s*$'; done 2>&1 | head -420
```

```
Fri Nov 27 22:20:53 UTC 2026
=== ./subspaceStatistics/Analysis/oneComponentToAnother.m
function output = oneComponentToAnother
L2 = 0.1;
svEnergy = 0.8;
leaveOut = 6;
load('ShenoyMonkeyData');
ShenoyMonkeyData = ShenoyMonkeyData(1:2);
load('basisFxnNum');
for monkey = 1:size(ShenoyMonkeyData,2)
    pooled = poolDatasets(ShenoyMonkeyData(monkey).M1,ShenoyMonkeyData(monkey).PMd);
    output(monkey).M1 = analyze(ShenoyMonkeyData(monkey).M1,L2,svEnergy, ...
        leaveOut,basisFxnNum(monkey).M1.maxDim);
    output(monkey).PMd = analyze(ShenoyMonkeyData(monkey).PMd,L2,svEnergy, ...
        leaveOut,basisFxnNum(monkey).PMd.maxDim);
end
end
function out = analyze(data,L2,svEnergy,leaveOut,factorDim)
data = pruneRepeats(data);
[out.data,out.prediction,reassambleTensor] = predictOneComponentFromAnother( ...
[... 402 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public-b65f28d; p=$(find . -name "getCorrelationsWithFrequency.m"); grep -v '^\s*%' $p | grep -v '^\s*$' | sed -n '40,80p'; for f in splitTrials splitTrialsAngles kinFromTBFSingleTrial predictKinUsingTBFandDataCondStructureSingletrial getVarExplainedKinematics studyAroundMeanParams removePotent kinFromTBFNoPotent predictDataUsingTBFandKinNN; do p=$(find . -name "$f.m"|head -1); echo "=== $p"; grep -v '^\s*%' $p | grep -v '^\s*$'; done 2>&1 | head -400
```

```
*output.allRepEigVals(find(train(fold,:)),:);
    for cond = find(test(fold,:))
        output.allRepEigValsHat(cond,:) = output.kinParams(cond,:)*kinToNeural;
        output.kinParamsHat(cond,:) = output.allRepEigVals(cond,:)*neuralToKin;
    end
end
output.allRepEigValsVarExpl = ...
    1-var(output.allRepEigValsHat - output.allRepEigVals,0,1) ...
    ./var(output.allRepEigVals,0,1);
output.allRepEigValsVarExpl(output.allRepEigValsVarExpl < 0) = 0;
output.kinParamsExpl = ...
    1-var(output.kinParamsHat - output.kinParams,0,1) ...
    ./var(output.kinParams,0,1);
output.kinParamsExpl(output.kinParamsExpl < 0) = 0;
end
=== ./utils/crossvalidation/splitTrials.m
function [train,test] = splitTrials(trials,ratio)
flip = false;
if ratio < 1
    flip = true;
[... 380 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public-b65f28d; for f in subspaceExcursionAngles; do p=$(find . -name "$f.m"|head -1); echo "=== $p"; grep -v '^\s*%' $p | grep -v '^\s*$'; done; p=$(find . -name "subspacea.m"); grep -v '^\s*%' $p | grep -v '^\s*$' | head -60; date -u
```

```
=== ./utils/subspaceUtils/subspaceExcursionAngles.m
function angles = subspaceExcursionAngles(X, nAngles, nPCADims)
maxTol = 0; % 0.5 degree tolerance for which is max angle
if nAngles < 1 || isnan(nAngles)
  angles = [];
  return;
end
if ndims(X) ~= 3
  error('subspaceExcursionAngle:tooFewModes', 'X should be nDims x nVectorsPerSubspace x nSubspaces');
end
if size(X, 3) == 1
  error('subspaceExcursionAngle:tooFewSubspaces', 'Supply multiple subspaces to test (size(X, 3) > 1)');
end
if any(isnan(X(:)))
  error('subspaceExcursionAngle:NaNs', 'No elements of X may be NaN');
end
if nAngles > size(X, 2) * size(X, 3) - 1
  warning('subspaceExcursionAngle:tooManyAngles', 'Requesting more angles than makes sense; reducing nAngles');
  nAngles = size(X, 2) * size(X, 3) - 1;
end
[... 148 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public-b65f28d; for f in nonlinearControls linearControls predictDataUsingKin predictDataUsingKinNonlinear createLags; do p=$(find . -name "$f.m"|head -1); echo "=== $p"; grep -v '^\s*%' $p | grep -v '^\s*$'; done 2>&1 | head -230; date -u
```

```
=== ./neuralAndKinematicsInvestigation/neuralFromKinematics/Analysis/nonlinearControls.m
function output = nonlinearControls
kernelType = 'OU';
kernelScale = [10^12 10^11];
nonlinearL2 = 0;
linearL2 = 0.1;
holdOutNum = 6;
load('ShenoyMonkeyData');
ShenoyMonkeyData = ShenoyMonkeyData(1:2);
load('inferLoadingsFromKinematicsTrialAveraged');
load('basisFxnNum');
for monkey = 1:size(ShenoyMonkeyData,2)
    output(monkey).M1 = prepForAnalysis(ShenoyMonkeyData(monkey).M1, ...
        ShenoyMonkeyData(monkey).Kinematics,holdOutNum, ...
        inferLoadingsFromKinematicsTrialAveraged(monkey).M1.nonlinearPrediction, ...
        basisFxnNum(monkey).M1.maxDim, ...
        kernelType,kernelScale,nonlinearL2,linearL2);
    output(monkey).PMd = prepForAnalysis(ShenoyMonkeyData(monkey).PMd, ...
        ShenoyMonkeyData(monkey).Kinematics,holdOutNum, ...
        inferLoadingsFromKinematicsTrialAveraged(monkey).PMd.nonlinearPrediction, ...
[... 184 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/sabatini-2024/ldr.py <<'EOF'


# ------------------------------------------------------------- datasets
def build(reading="all", monkeys=("J", "N")):
    """Load both sessions and form the four datasets: smoothed single trials
    (trials x units x 121), condition averages (72 x units x 121), 1 ms counts,
    hand position (start-subtracted, mm) and condition means of the hand."""
    out = {}
    for m in monkeys:
        S = load_session(m, reading)
        sm = smooth_trials(S["counts"])
        hand = S["hand"] - S["hand"][:, :1, :]   # assumption: position relative to the start
        hand10 = hand[:, ::10]
        kin = np.stack([hand10[S["cond"] == c].mean(0) for c in range(72)])  # 72 x 121 x 2
        for reg in ("M1", "PMd"):
            u = S["region"] == reg
            name = f"{reg}-{m}"
            Xt = sm[:, u]
            out[name] = dict(name=name, monkey=m, region=reg, units=np.where(u)[0],
                             Xt=Xt, X=cond_average(Xt, S["cond"]), cond=S["cond"],
                             counts=S["counts"][:, u], hand10=hand10, kin=kin,
                             trials=S["trials"], conds=S["conds"],
                             dropped=S["dropped_uncovered"], n_trials_file=S["n_trials_file"],
                             table=S["table"])
        del sm
    return out


# ------------------------------------------------------------- kinematics
def kin_basis(kins, reading="svd"):
    """Kinematic basis functions (paper, Methods, Extracting kinematic basis
    functions): SVD of the x and y hand velocity of all conditions of all datasets;
    the top two velocity singular vectors, integrated to position. Reading 'svd'
    uses the raw vectors; reading 'skewnormal' fits a skew-normal curve to the first
    and the derivative of a skew-normal to the second, integrated analytically.
    kins: list of (72 x 121 x 2) condition-mean positions (mm). Returns position
    basis (121 x 2), velocity basis (121 x 2, per 10 ms)."""
    V = np.concatenate([np.gradient(k, axis=1).transpose(0, 2, 1).reshape(-1, NT) for k in kins])
    _, _, Vt = np.linalg.svd(V, full_matrices=False)
    v = Vt[:2].T.copy()
    for i in range(2):  # sign: first positive at its peak, second positive first lobe
        j = np.argmax(np.abs(v[:, i])) if i == 0 else np.argmax(np.abs(v[:, i]) > 0.5 * np.abs(v[:, i]).max())
        v[:, i] *= np.sign(v[j, i])
    if reading == "skewnormal":
        from scipy.optimize import curve_fit
        t = TIMES.astype(float)
        f1 = lambda t, a, al, lo, sc: a * stats.skewnorm.pdf(t, al, lo, sc)
        p1, _ = curve_fit(f1, t, v[:, 0], p0=[v[:, 0].max() * 200, 2, 100, 200], maxfev=20000)
        def f2(t, a, al, lo, sc):
            h = 1e-3 * sc
            return a * (stats.skewnorm.pdf(t + h, al, lo, sc) - stats.skewnorm.pdf(t - h, al, lo, sc)) / (2 * h)
        best = None
        for s0 in (1, -1):
            try:
                p2, _ = curve_fit(f2, t, v[:, 1], p0=[s0 * 1e4, 2, 150, 150], maxfev=20000)
                err = ((f2(t, *p2) - v[:, 1]) ** 2).sum()
                if best is None or err < best[1]:
                    best = (p2, err)
            except RuntimeError:
                pass
        p2 = best[0]
        vel = np.c_[f1(t, *p1), f2(t, *p2)]
        pos = np.c_[p1[0] * stats.skewnorm.cdf(t, *p1[1:]) / 10, p2[0] * stats.skewnorm.pdf(t, *p2[1:]) / 10]
        # per-10 ms velocity units: pdf is per ms; integrate over ms = sum per 10 ms bins x 10
        pos = np.c_[p1[0] * stats.skewnorm.cdf(t, *p1[1:]), p2[0] * stats.skewnorm.pdf(t, *p2[1:])] / 10
        return pos - pos[0], vel, dict(p1=p1, p2=p2, raw=v)
    pos = np.cumsum(v, 0)
    pos -= pos[0]
    return pos, v, dict(raw=v)


def reach_params(pos_basis, kin):
    """Code predictDataUsingTBFandKinCondStructure.m: pinv(kinFxns) * [X Y] per
    condition; returned as [x b1, y b1, x b2, y b2] (code getCorrelationsWithFrequency
    labels: x-extent, y-extent, x-curve, y-curve). kin: (..., 121, 2)."""
    P = np.linalg.pinv(pos_basis) @ kin  # (..., 2 basis, 2 axis)
    return P.reshape(P.shape[:-2] + (4,))


def params_to_path(pos_basis, p):
    P = p.reshape(p.shape[:-1] + (2, 2))
    return pos_basis @ P


# --------------------------------------------------------- subspace angles
def principal(F, G):
    """Principal angles between span(F) and span(G) (as subspacea.m), ascending,
    with the bases U (in F) and V (in G) that realise them."""
    QF, _ = np.linalg.qr(F)
    QG, _ = np.linalg.qr(G)
    Y, s, Zt = np.linalg.svd(QF.T @ QG, full_matrices=False)
    s = np.clip(s, -1, 1)
    return np.arccos(s), QF @ Y, QG @ Zt.T


def sea(Xs, n_angles=25):
    """Subspace excursion angles (code subspaceExcursionAngles.m with maxTol 0):
    seed with the pair of subspaces at the largest principal angle, add the vector of
    the subspace at the largest angle to the augmented seed, repeat; of the tied
    sequences (the seed pair in both orders) the one with the largest summed angles.
    Xs: (nSubs, nDims, nVecs). Returns angles in degrees."""
    n = len(Xs)
    nv = Xs.shape[2]
    n_angles = min(n_angles, nv * n - 1)
    Q = [np.linalg.qr(x)[0] for x in Xs]
    first = np.zeros((n, n))
    for i in range(n - 1):
        for j in range(i + 1, n):
            s = np.linalg.svd(Q[i].T @ Q[j], compute_uv=False)
            first[i, j] = first[j, i] = np.arccos(np.clip(s.min(), -1, 1))
    i, j = np.unravel_index(np.argmax(first), first.shape)
    best = None
    for a, b in ((i, j), (j, i)):
        th, U, V = principal(Xs[a], Xs[b])
        S = np.c_[U, V[:, -1]]
        angs = [first[a, b]]
        for _ in range(1, n_angles):
            QS = np.linalg.qr(S)[0]
            vals = np.zeros(n)
            for m in range(n):
                s = np.linalg.svd(QS.T @ Q[m], compute_uv=False)
                vals[m] = np.arccos(np.clip(s.min(), -1, 1))
            m = int(np.argmax(vals))
            _, _, V = principal(S, Xs[m])
            S = np.c_[S, V[:, -1]]
            angs.append(vals[m])
        if best is None or sum(angs) > sum(best):
            best = angs
    return np.degrees(best)


def pca_dims(cols):
    """PCs to 80% of the variance and participation ratio of the rows' covariance;
    cols: (observations, N)."""
    c = cols - cols.mean(0)
    lam = np.linalg.svd(c, compute_uv=False) ** 2
    frac = np.cumsum(lam) / lam.sum()
    return int(np.searchsorted(frac, 0.8) + 1), float(lam.sum() ** 2 / (lam ** 2).sum())


def circ_corr(a, b):
    """Circular correlation (Jammalamadaka & SenGupta) with its normal-approximation p."""
    from scipy.stats import circmean
    sa, sb = np.sin(a - circmean(a)), np.sin(b - circmean(b))
    r = (sa * sb).sum() / np.sqrt((sa ** 2).sum() * (sb ** 2).sum())
    n = len(a)
    l20, l02, l22 = (sa ** 2).mean(), (sb ** 2).mean(), (sa ** 2 * sb ** 2).mean()
    z = r * np.sqrt(n * l20 * l02 / l22)
    return r, 2 * stats.norm.sf(abs(z))
EOF
cd $TMPDIR && . env/bin/activate && uv pip install -q jupytext nbconvert ipykernel 2>&1|tail -1; date -u
```

```
Fri Nov 27 22:23:29 UTC 2026
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && python3 - <<'EOF'
s=open('ldr.py').read()
s=s.replace("""        pos = np.c_[p1[0] * stats.skewnorm.cdf(t, *p1[1:]) / 10, p2[0] * stats.skewnorm.pdf(t, *p2[1:]) / 10]
        # per-10 ms velocity units: pdf is per ms; integrate over ms = sum per 10 ms bins x 10
""","""        # velocity is per 10 ms bin and the pdf per ms, so the integral over bins is 1/10 of it
""")
open('ldr.py','w').write(s)
EOF
echo ok
```

```
ok
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb1.py",
 "content": "# %% [markdown]\n# # Sabatini & Kaufman (2024) on DANDI:000070: dynamics (notebook 1 of 2)\n#\n# Paper: D. A. Sabatini and M. T. Kaufman, \"Reach-dependent reorientation of rotational dynamics in\n# motor cortex\", Nat. Commun. 15:7007 (2024), doi:10.1038/s41467-024-51308-7. The claims file\n# (`claims/sabatini-2024.yaml`) was written from the version of record (PMC11325044) and its\n# supplement.\n#\n# Dataset: DANDI:000070, \"Neural population dynamics during reaching\", version **0.261122.2046**\n# (doi:10.48324/dandi.000070/0.261122.2046). The paper cites the dandiset without a version (it was\n# published in August 2024, before the first published version of December 2025), so the most recent\n# published version is pinned. The two sessions the paper's Data availability statement names are read:\n# `sub-Jenkins_ses-20090918` and `sub-Nitschke_ses-20100923`. The file names of this version match the\n# paper's (the Nitschke date is 2010 in both).\n#\n# This notebook tests the claims on the temporal basis factorization (TBF), single-condition dynamics,\n# jPCA and the geometry of the rotations. Notebook 2 (`reproduce_sabatini_2024_kinematics.ipynb`) tests\n# the claims on prediction, encoding and decoding.\n#\n# | claim | notebook |\n# |---|---|\n# | data-composition, fig3g-basis-frequencies, tbf-variance-explained, tbf-shuffle-control, fig3h-recoverability, fig3i-duration-warping, jpca-fit-r2, jpca-variance-explained, fig4d-jpca-variance-correlation, fig4f-plane-alignment-explains-jpca, single-lds-variance, fig2c-condition-lds-variance, fig3a-eigenvalue-clusters, fig3c-eigenvalue-distance-auc, suppfig2-eigenvalues-from-kinematics, suppfig3-model-comparison, fig4b-plane-alignment, suppfig6a-location-alignment, fig5a-frequencies-segregated, suppfig6c-location-distinct-from-rotations, fig4c-subspace-excursion-angles, suppfig6b-location-dimensionality, rotation-orientation-dimensionality | tested here |\n# | fig5c, fig6b, fig6c, fig6e, fig7c (both), suppfig7a, fig7f-ldr-decoding, trial-curvature-decoding, suppfig8 | tested in notebook 2 |\n# | fig7f-decoder-beats-standard | blocked (notebook 2 explains) |\n\n# %%\nimport time, resource, warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nimport matplotlib.pyplot as plt\nimport ldr\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\nnp.set_printoptions(precision=3, suppress=True, linewidth=150)\nT_START = time.time()\nSEED_OFFSETS = [0, 1000, 2000, 3000, 4000]\nDS = ldr.build(\"all\")\nNAMES = ldr.DATASETS\nprint(\"loaded in %.0f s, peak memory %.1f GB\" % (time.time() - T_START,\n      resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6))\n\n# %% tags=[\"sanity\"]\n# Data check: what was loaded, and the description against the values.\nfor m in (\"J\", \"N\"):\n    d = DS[f\"M1-{m}\"]\n    tab = d[\"table\"]\n    keep = (tab.maze_condition > 0) & (tab.maze_condition % 3 != 0)\n    print(f\"monkey {m}: {d['n_trials_file']} trials in the file; maze conditions \"\n          f\"{tab.maze_condition.min()}..{tab.maze_condition.max()} ({tab.maze_condition.nunique()} values, \"\n          f\"{(tab.maze_condition == 0).sum()} trials with condition 0)\")\n    for r in range(3):\n        sub = tab[(tab.maze_condition > 0) & (tab.maze_condition % 3 == r)]\n        print(f\"   condition mod 3 = {r}: {sub.maze_condition.nunique()} conditions, targets \"\n              f\"{sorted(sub.maze_num_targets.unique())}, barriers {sorted(sub.maze_num_barriers.unique())}, \"\n              f\"trial_version {sorted(sub.trial_version.unique())}\")\n    succ = keep & (tab.task_success == 1)\n    print(f\"   successful trials of the 72 conditions: {succ.sum()}; with delay > 400 ms: \"\n          f\"{(succ & (tab.delay > 0.4)).sum()}; discard_trial set: {(tab.discard_trial == 1).sum()}; \"\n          f\"windows past the trial end dropped: {d['dropped']}\")\n    n_per = np.bincount(d[\"cond\"], minlength=72)\n    print(f\"   trials per condition {n_per.min()}..{n_per.max()} (median {np.median(n_per):.0f})\")\n    print(f\"   delay range {tab.delay.min()*1000:.0f}..{tab.delay.max()*1000:.0f} ms; offline minus online \"\n          f\"movement onset, median {np.median(tab.offline_move_onset_time - tab.move_begins_time)*1000:.0f} ms\")\n    hk = d[\"kin\"]\n    print(f\"   hand displacement at +850 ms (mm, start-subtracted): |x| up to {np.abs(hk[:, -1, 0]).max():.0f}, \"\n          f\"|y| up to {np.abs(hk[:, -1, 1]).max():.0f}; peak speed of the condition means \"\n          f\"{np.linalg.norm(np.diff(hk, axis=1), axis=2).max() * 100:.0f} mm/s\")\nfor n in NAMES:\n    d = DS[n]\n    rate = d[\"X\"].mean((0, 2))\n    print(f\"{n}: {len(d['units'])} units (threshold-crossing channels), mean rate {rate.min():.1f}..\"\n          f\"{rate.max():.1f} spikes/s, trials {d['Xt'].shape[0]}, conditions {d['X'].shape[0]}\")\n\n# %% tags=[\"sanity\"]\n# Clock check. Hand speed in the condition means peaks after the trial table's movement onset, and the\n# reach direction can be decoded from spikes after onset but not from a window well before the target\n# appears (labels as given, windows aligned on the trial table's movement onset).\nfrom sklearn.discriminant_analysis import LinearDiscriminantAnalysis\nfrom sklearn.model_selection import cross_val_score\nfor n in NAMES:\n    d = DS[n]\n    sp = np.linalg.norm(np.diff(d[\"kin\"], axis=1), axis=2) * 100\n    tpk = ldr.TIMES[1:][sp.argmax(1)]\n    ang = np.arctan2(d[\"kin\"][:, -1, 1], d[\"kin\"][:, -1, 0])\n    octant = (np.floor((ang + np.pi) / (2 * np.pi) * 8) % 8).astype(int)[d[\"cond\"]]\n    c = d[\"counts\"]\n    post = c[:, :, 355:655].sum(2)          # 0 to +300 ms\n    pre = c[:, :, 0:300].sum(2)             # -355 to -55 ms (delay period, target shown)\n    g = ldr.rng(\"clock-check\")\n    shuffled = g.permutation(octant)\n    acc = [cross_val_score(LinearDiscriminantAnalysis(), np.sqrt(x), y, cv=5).mean()\n           for x, y in ((post, octant), (pre, octant), (post, shuffled))]\n    print(f\"{n}: hand speed peak {np.median(tpk):.0f} ms after onset (range {tpk.min()}..{tpk.max()}); \"\n          f\"8-way direction decoding: 0..300 ms {acc[0]:.2f}, -355..-55 ms {acc[1]:.2f}, shuffled labels \"\n          f\"{acc[2]:.2f} (chance 0.125)\")\n\n# %% tags=[\"sanity\"]\n# Recordings deposited more than once: trial counts, first trial times and spike counts of every\n# session of the version (metadata and one unit only).\nrows = []\nr = ldr.requests.get(f\"{ldr.API}/dandisets/{ldr.DANDISET}/versions/{ldr.VERSION}/assets/\",\n                     params={\"page_size\": 100}, timeout=60).json()[\"results\"]\nfor a in sorted(r, key=lambda a: a[\"path\"]):\n    h = ldr.h5py.File(ldr.remfile.File(f\"{ldr.API}/assets/{a['asset_id']}/download/\"), \"r\")\n    t = h[\"intervals/trials\"]\n    idx = h[\"units/spike_times_index\"][:]\n    rows.append(dict(path=a[\"path\"].split(\"/\")[1][:28], trials=len(t[\"start_time\"]),\n                     first_go=round(float(t[\"go_cue_time\"][0]), 4), units=len(idx),\n                     spikes_unit0=int(idx[0]), spikes_total=int(idx[-1]),\n                     conds=len(np.unique(t[\"maze_condition\"][:]))))\n    h.close()\nsess = pd.DataFrame(rows)\nprint(sess.to_string(index=False))\ndup = sess.duplicated([\"trials\", \"spikes_unit0\", \"spikes_total\"], keep=False)\nprint(\"sessions sharing trial and spike counts:\", int(dup.sum()))\n\n# %% tags=[\"finding-unsorted-units\"]\n# The units are unsorted threshold crossings, one per electrode, where the paper analysed sorted\n# single units and stable multi-units (79 to 118 per array).\nh = ldr.open_nwb(ldr.SESSIONS[\"J\"])\nprint(h[\"units\"].attrs[\"description\"])\nprint(\"units:\", len(h[\"units/id\"]), \"| columns:\", list(h[\"units\"].attrs[\"colnames\"]))\nloc = h[\"general/extracellular_ephys/electrodes/location\"][:].astype(str)\nprint(\"electrodes per location:\", dict(zip(*np.unique(loc, return_counts=True))))\nh.close()\n\n# %% [markdown]\n# ## data-composition\n# > Two monkeys (J and N) performed the maze task with 72 conditions (36 straight, 36 curved); a PMd and\n# > an M1 array in each monkey gave 79 to 118 units per array; 1469 trials for monkey J and 2014 for monkey N.\n\n# %% tags=[\"claim:data-composition\"]\nexpected = {\"J\": 1469, \"N\": 2014}\nfor m in (\"J\", \"N\"):\n    tab = DS[f\"M1-{m}\"][\"table\"]\n    for reading in (\"all\", \"delay400\"):\n        sel = ldr.select_trials(tab, reading)\n        mc = tab.maze_condition[sel]\n        ns, nc = (mc % 3 == 1).groupby(mc).first().sum(), (mc % 3 == 2).groupby(mc).first().sum()\n        n = int(sel.sum())\n        print(f\"monkey {m}, reading {reading}: {mc.nunique()} conditions ({ns} straight = no barrier, \"\n              f\"{nc} curved = barriers), {n} trials; paper {expected[m]} (within 10%: \"\n              f\"{abs(n - expected[m]) <= 0.1 * expected[m]})\")\nfor n in NAMES:\n    print(f\"{n}: {len(DS[n]['units'])} units, none marked single- or multi-unit (all threshold crossings)\")\n\n# %% [markdown]\n# **Result: ...** see the summary below the code for each claim. Conditions: under both readings each monkey has 72\n# conditions, 36 without barriers (straight) and 36 with barriers (curved). Trials: J 1595 (all successful)\n# and 1381 (delay above 400 ms), both within 10% of 1469; N 2121 and 1884, both within 10% of 2014. Units: 96\n# per array, inside 71 to 130, but they are unsorted threshold crossings, so the dataset marks no single or\n# multi-units and the paper's count of sorted units cannot be checked.\n\n# %% [markdown]\n# ## fig3g-basis-frequencies\n# > The cross-validated temporal basis functions contained 3 to 4 rotations at 0.5, 1.5, 2.5 and 4 Hz,\n# > along with an offset.\n#\n# Number of basis functions by cross-validation (code crossValidateDimensionalityBasisFxns.m: halves of the\n# trials, 100 folds, k = 1 to 20, an even best k raised by one), then de-mixing (eigTransform.m).\n\n# %% tags=[\"claim:fig3g-basis-frequencies\"]\nCV = {}\nfor n in NAMES:\n    d = DS[n]\n    res = [ldr.cv_tbf_k(d[\"Xt\"], d[\"cond\"], ldr.rng(\"fig3g-basis-frequencies\", k), folds=100)\n           for k in SEED_OFFSETS]\n    CV[n] = res[0]\n    print(f\"{n}: held-out VE by k (claim seed) {np.round(res[0]['mean'][:12], 3)}\")\n    print(f\"     best k {res[0]['best']} -> k = {res[0]['k']}; k under the five seeds {[r['k'] for r in res]}\")\nK = {n: CV[n][\"k\"] for n in NAMES}\nTBF = {n: ldr.eig_transform(DS[n][\"X\"], K[n]) for n in NAMES}\ntargets = np.array([0.5, 1.5, 2.5, 4.0])\nfor n in NAMES:\n    tb = TBF[n]\n    gr = ldr.groups(tb)\n    rot = [f for f, i in gr if len(i) == 2]\n    real = [f for f, i in gr if len(i) == 1]\n    near = [targets[np.argmin(abs(targets - f))] for f in rot]\n    ok = [abs(f - t) <= 0.1 * t for f, t in zip(rot, near)]\n    print(f\"{n}: k={K[n]}; {len(rot)} rotation pairs at {np.round(rot, 2)} Hz (half-lives \"\n          f\"{np.round([tb['halflife'][i[0]] for f, i in gr if len(i) == 2], 2)} s), {len(real)} real mode(s) at \"\n          f\"{np.round(real, 2)} Hz; nearest of 0.5/1.5/2.5/4: {near}; within 10%: {ok}\")\nfig, ax = plt.subplots(1, 4, figsize=(14, 2.6))\nfor a, n in zip(ax, NAMES):\n    a.plot(ldr.TIMES, TBF[n][\"B\"]); a.set_title(n); a.set_xlabel(\"ms from movement onset\")\nplt.tight_layout(); plt.show()\nprint(\"basis functions plotted are within -1..1:\", all(np.nanmax(abs(TBF[n]['B'])) <= 1 for n in NAMES))\n\n# %% [markdown]\n# ## tbf-variance-explained\n# > The shared rotations of the temporal basis factorization explained 90 to 96% of the population variance.\n\n# %% tags=[\"claim:tbf-variance-explained\"]\nVE_TBF = {}\nfor n in NAMES:\n    X = DS[n][\"X\"]; tb = TBF[n]\n    va = ldr.var_explained(X, ldr.reconstruct(tb[\"L\"], tb[\"B\"]))            # (a) -150..850, de-mixed\n    vb = ldr.var_explained(X, ldr.reconstruct(tb[\"Lraw\"], tb[\"Braw\"]))      # (b) whole window, raw SVD\n    VE_TBF[n] = va\n    print(f\"{n}: (a) mean {va.mean()*100:.1f}% (s.d. {va.std(ddof=1)*100:.1f}); (b) mean {vb.mean()*100:.1f}% \"\n          f\"(s.d. {vb.std(ddof=1)*100:.1f}); in 81..100%: {0.81 <= va.mean() <= 1}, {0.81 <= vb.mean() <= 1}\")\n\n# %% [markdown]\n# ## tbf-shuffle-control and fig3h-recoverability\n# > Shuffling time bins within each trial before smoothing lowered the variance explained by the\n# > factorization to 35 to 46%, significantly below the real data.\n#\n# > Projections of each condition's activity recovered the temporal basis functions almost perfectly\n# > (91 to 95% variance explained, chance 63 to 80%).\n#\n# Per trial the 1 ms bins are permuted in time, the same permutation for every unit (code scrambleTrials.m),\n# then smoothed and averaged; TBF with the real data's k on the raw SVD basis over the whole window, as\n# the code's quantifyTBFStats.m does (it calls getBasisFxns, not eigTransform). Recoverability by Eq. 6.\n\n# %%\ndef recoverability(X, L, B):\n    ok = ~np.isnan(B[:, 0])\n    Bt = B[ok].T\n    out = np.zeros(len(X))\n    for c in range(len(X)):\n        Bh = np.linalg.pinv(L[c]) @ X[c][:, ok]\n        out[c] = 1 - (Bh - Bt).var(1, ddof=1).sum() / Bt.var(1, ddof=1).sum()\n    return np.clip(out, 0, None)\n\ndef scrambled_average(d, g):\n    c = d[\"counts\"][:, :, 5:1206]\n    out = np.zeros((c.shape[0], c.shape[1], ldr.NT), np.float32)\n    for i in range(c.shape[0]):\n        p = g.permutation(c.shape[2])\n        x = np.zeros((c.shape[1], 1210), np.uint8)\n        x[:, 5:1206] = c[i][:, p]\n        out[i] = ldr.smooth(x)\n    return ldr.cond_average(out, d[\"cond\"])\n\nSHUF = {}\nfor n in NAMES:\n    d = DS[n]\n    X = d[\"X\"]\n    Br, Lr = ldr.get_basis(X, K[n])\n    real_ve = ldr.var_explained(X, Lr @ Br.T)\n    real_rec = recoverability(X, Lr, Br)\n    rows = []\n    for k in SEED_OFFSETS:\n        Xs = scrambled_average(d, ldr.rng(\"tbf-shuffle-control\", k))\n        Bs, Ls = ldr.get_basis(Xs, K[n])\n        ve = ldr.var_explained(Xs, Ls @ Bs.T)\n        rec = recoverability(Xs, Ls, Bs)\n        rows.append((ve, rec))\n    SHUF[n] = dict(real_ve=real_ve, real_rec=real_rec, ve=rows[0][0], rec=rows[0][1],\n                   ve_seeds=[r[0].mean() for r in rows], rec_seeds=[r[1].mean() for r in rows])\n\n# %% tags=[\"claim:tbf-shuffle-control\"]\nfor n in NAMES:\n    s = SHUF[n]\n    p_rs = stats.ranksums(s[\"real_ve\"], s[\"ve\"], alternative=\"two-sided\").pvalue\n    p_sr = stats.wilcoxon(s[\"real_ve\"], s[\"ve\"]).pvalue\n    print(f\"{n}: real {s['real_ve'].mean()*100:.1f}%, shuffled {s['ve'].mean()*100:.1f}% \"\n          f\"(s.d. {s['ve'].std(ddof=1)*100:.1f}; five seeds {np.round(np.array(s['ve_seeds'])*100, 1)}); \"\n          f\"in 31.5..50.6%: {0.315 <= s['ve'].mean() <= 0.506}; rank-sum p = {p_rs:.2g}, signed-rank p = {p_sr:.2g}\")\n\n# %% tags=[\"claim:fig3h-recoverability\"]\nfor n in NAMES:\n    s = SHUF[n]\n    tb = TBF[n]\n    rec_dm = recoverability(DS[n][\"X\"], tb[\"L\"], tb[\"B\"])\n    p_rs = stats.ranksums(s[\"real_rec\"], s[\"rec\"]).pvalue\n    print(f\"{n}: recoverability {s['real_rec'].mean()*100:.1f}% (s.d. {s['real_rec'].std(ddof=1)*100:.1f}; \"\n          f\"de-mixed basis -150..850: {rec_dm.mean()*100:.1f}%), chance {s['rec'].mean()*100:.1f}% (five seeds \"\n          f\"{np.round(np.array(s['rec_seeds'])*100, 1)}); real in 81.9..100: {s['real_rec'].mean() >= 0.819}; \"\n          f\"chance in 56.7..88: {0.567 <= s['rec'].mean() <= 0.88}; rank-sum p = {p_rs:.2g}, real higher: \"\n          f\"{s['real_rec'].mean() > s['rec'].mean()}\")\n\n# %% [markdown]\n# ## fig3i-duration-warping\n# > Before warping, rotation fits were unrelated or weakly related to reach duration (M1-N rho = -0.26,\n# > p = 0.023; others -0.18 to 0.21, p > 0.067); warping reaches to equal duration induced a negative\n# > correlation (rho -0.63 to -0.52, p < 0.001).\n#\n# Code warpTrials.m and warpTrial.m: duration per condition from the condition-mean hand speed (last 10 ms bin\n# with speed at least a tenth of its peak); each spike gets a uniform random offset within its 1 ms bin; from\n# 100 ms before onset to the end of the reach, time is scaled to 600 ms; later activity is shifted (reading\n# \"truncate\": cut at +850 ms; variant \"250\": the post-reach activity scaled to 250 ms). TBF on the raw SVD\n# basis with the original k; recoverability per condition.\n\n# %%\ndef durations(d):\n    sp = np.linalg.norm(np.diff(d[\"kin\"], axis=1), axis=2)\n    out = np.zeros(72)\n    for c in range(72):\n        fast = np.where(sp[c] >= sp[c].max() / 10)[0]\n        out[c] = 10 * (fast[-1] + 1 - 35)   # code: 10*(fastInds(end)-36), 1-based on diff\n    return out\n\ndef warped_average(d, dur, g, mode=\"truncate\"):\n    c = d[\"counts\"][:, :, 5:1206]\n    out = np.zeros((c.shape[0], c.shape[1], ldr.NT), np.float32)\n    for i in range(c.shape[0]):\n        wf = dur[d[\"cond\"][i]]\n        uu, tt = np.nonzero(c[i])\n        reps = c[i][uu, tt]\n        uu = np.repeat(uu, reps); tt = np.repeat(tt, reps)\n        st = tt + g.random(len(tt)) - 350 + 100\n        w = st.copy()\n        a = (st > 0) & (st < wf)\n        w[a] = 600 * st[a] / wf\n        b = st >= wf\n        if mode == \"truncate\":\n            w[b] = st[b] - wf + 600\n        else:  # post-reach activity scaled to 250 ms, then as recorded\n            post = 850 + 100 - wf\n            w[b] = 600 + (st[b] - wf) * 250 / max(post, 1)\n        w = w + 350 - 100\n        keep = (w >= 0) & (w < 1201)\n        x = np.zeros((c.shape[1], 1210), np.uint16)\n        np.add.at(x, (uu[keep], 5 + np.floor(w[keep]).astype(int)), 1)\n        out[i] = ldr.smooth(x)\n    return ldr.cond_average(out, d[\"cond\"])\n\nWARP = {}\nfor n in NAMES:\n    d = DS[n]\n    dur = durations(d)\n    dd = abs(dur - dur.mean())\n    rec0 = SHUF[n][\"real_rec\"]\n    r0 = stats.pearsonr(dd, rec0)\n    res = {}\n    for mode in (\"truncate\", \"250\"):\n        vals = []\n        for k in (SEED_OFFSETS if mode == \"truncate\" else [0]):\n            Xw = warped_average(d, dur, ldr.rng(\"fig3i-duration-warping\", k), mode)\n            Bw, Lw = ldr.get_basis(Xw, K[n])\n            rw = recoverability(Xw, Lw, Bw)\n            vals.append(stats.pearsonr(dd, rw))\n        res[mode] = vals\n    WARP[n] = dict(dur=dur, r0=r0, res=res)\n\n# %% tags=[\"claim:fig3i-duration-warping\"]\nfor n in NAMES:\n    w = WARP[n]\n    rt = w[\"res\"][\"truncate\"][0]\n    print(f\"{n}: durations {w['dur'].min():.0f}..{w['dur'].max():.0f} ms (mean {w['dur'].mean():.0f}); unwarped rho = \"\n          f\"{w['r0'][0]:.3f} (p = {w['r0'][1]:.3g}); warped (truncate) rho = {rt[0]:.3f} (p = {rt[1]:.3g}), five seeds \"\n          f\"{np.round([v[0] for v in w['res']['truncate']], 3)}; warped (250 ms) rho = {w['res']['250'][0][0]:.3f} \"\n          f\"(p = {w['res']['250'][0][1]:.3g})\")\nprint(\"M1-N unwarped within -0.286..-0.234 and p < 0.05:\",\n      -0.286 <= WARP['M1-N']['r0'][0] <= -0.234 and WARP['M1-N']['r0'][1] < 0.05)\nprint(\"other unwarped in -0.198..0.231:\", [(-0.198 <= WARP[n]['r0'][0] <= 0.231) for n in NAMES if n != 'M1-N'])\nprint(\"warped in -0.693..-0.468 with p < 0.001:\",\n      [(-0.693 <= WARP[n]['res']['truncate'][0][0] <= -0.468) and WARP[n]['res']['truncate'][0][1] < 0.001 for n in NAMES])\n\n# %% [markdown]\n# ## jPCA claims\n# jPCA as in getRotations.m: activity reconstructed from the de-mixed basis, mean-subtracted across\n# conditions, soft-normalised (range + 5), jPCA on bins 20 to 40 with the codepack's defaults (6 PCs, its own\n# soft normalisation and mean subtraction). The jPCA codepack is not in the paper's repository; jPCA is\n# implemented here from its published description (Churchland et al. 2012), in `ldr.jpca`.\n#\n# ### jpca-fit-r2\n# > Rotational dynamics found by jPCA fit activity within the jPCA planes with R2 of 0.64 to 0.73, higher on\n# > straight reaches (0.73 to 0.88) than on curved reaches (0.56 to 0.70).\n\n# %% tags=[\"claim:jpca-fit-r2\"]\nPLANES = {n: (2 if n.startswith(\"M1\") else 1) for n in NAMES}\nROT = {}\nstraight, curved = np.arange(0, 72, 2), np.arange(1, 72, 2)\nrows = []\nfor n in NAMES:\n    tb = TBF[n]\n    ROT[n] = ldr.get_rotations(tb[\"L\"], tb[\"B\"], PLANES[n])\n    rs = ldr.get_rotations(tb[\"L\"], tb[\"B\"], PLANES[n], conds=straight)\n    rc = ldr.get_rotations(tb[\"L\"], tb[\"B\"], PLANES[n], conds=curved)\n    # per-condition R2 of the projected trajectory in the top plane (signed-rank test, reported)\n    def per_cond(r):\n        jp = r[\"jp\"]; out = []\n        Xn = (r[\"Xr\"] - r[\"mean\"]) * r[\"sn\"][None, :, None]\n        for c in range(len(Xn)):\n            z = jp[\"jPCs_highD\"][:, :2].T @ Xn[c][:, ldr.T0:40]\n            dz = np.diff(z, axis=1); M2 = jp[\"J\"][:, :2].T @ jp[\"Mskew\"] @ jp[\"J\"][:, :2]\n            fit = (z[:, :-1].T @ M2).T\n            out.append(1 - ((dz - fit) ** 2).sum() / ((dz - dz.mean(1, keepdims=True)) ** 2).sum())\n        return np.array(out)\n    ps, pc = per_cond(rs), per_cond(rc)\n    p = stats.wilcoxon(ps, pc).pvalue\n    rows.append(dict(dataset=n, all_skew=ROT[n][\"jp\"][\"R2_Mskew_2D\"], all_best=ROT[n][\"jp\"][\"R2_Mbest_2D\"],\n                     straight_skew=rs[\"jp\"][\"R2_Mskew_2D\"], straight_best=rs[\"jp\"][\"R2_Mbest_2D\"],\n                     curved_skew=rc[\"jp\"][\"R2_Mskew_2D\"], curved_best=rc[\"jp\"][\"R2_Mbest_2D\"],\n                     signrank_p=p, straight_cond_median=np.median(ps), curved_cond_median=np.median(pc)))\nJR = pd.DataFrame(rows).set_index(\"dataset\")\nprint(JR.round(3).to_string())\nfor rd in (\"skew\", \"best\"):\n    ok_all = JR[f\"all_{rd}\"].between(0.576, 0.803)\n    ok_s = JR[f\"straight_{rd}\"].between(0.657, 0.968)\n    ok_c = JR[f\"curved_{rd}\"].between(0.504, 0.77)\n    print(f\"reading {rd}: all in 0.576..0.803 {ok_all.sum()}/4, straight in 0.657..0.968 {ok_s.sum()}/4, \"\n          f\"curved in 0.504..0.77 {ok_c.sum()}/4; straight > curved {int((JR[f'straight_{rd}'] > JR[f'curved_{rd}']).sum())}/4\")\n\n# %% [markdown]\n# ### jpca-variance-explained\n# > Activity within the jPCA rotational planes explained only 7 to 12% of the population variance in\n# > peri-movement firing rates.\n\n# %% tags=[\"claim:jpca-variance-explained\"]\nfor n in NAMES:\n    r = ROT[n]\n    print(f\"{n}: {PLANES[n]} plane(s); variance in the planes (code: reconstruction without the mean against \"\n          f\"the activity) mean {r['ve'].mean()*100:.1f}% (s.d. {r['ve'].std(ddof=1)*100:.1f}); in 6.3..13.2%: \"\n          f\"{0.063 <= r['ve'].mean() <= 0.132}; variant with the mean added back {r['ve_with_mean'].mean()*100:.1f}%\")\n\n# %% [markdown]\n# ### fig4d-jpca-variance-correlation\n# > Variance in the jPCA planes was only moderately correlated with the total rotational variance of a\n# > condition (rho 0.39 to 0.46; 66% of jPCA planes correlated at p < 0.05).\n\n# %% tags=[\"claim:fig4d-jpca-variance-correlation\"]\nF4D = []\nfor n in NAMES:\n    tb, r = TBF[n], ROT[n]\n    inds = np.where(tb[\"freq\"] > 0)[0]\n    ok = ~np.isnan(tb[\"B\"][:, 0])\n    meanL = tb[\"L\"].mean(0)\n    rotvar = np.array([np.nansum(np.var(r[\"sn\"][:, None] * ((tb[\"L\"][c][:, inds] - meanL[:, inds]) @ tb[\"B\"][ok][:, inds].T),\n                       axis=1, ddof=1)) for c in range(72)])\n    for p in range(PLANES[n]):\n        jv = np.nansum(np.nanvar(r[\"rot\"][:, 2 * p:2 * p + 2], axis=2, ddof=1), axis=1)\n        rr = stats.pearsonr(jv, rotvar)\n        F4D.append(dict(dataset=n, plane=p + 1, rho=rr[0], p=rr[1]))\nF4D = pd.DataFrame(F4D)\nprint(F4D.round(4).to_string(index=False))\nshare = (F4D.p < 0.05).mean() * 100\nmean_rho = F4D.groupby(\"dataset\").rho.mean()\nprint(\"reading (a) mean rho per dataset:\", mean_rho.round(3).to_dict(), \"in 0.351..0.506:\", mean_rho.between(0.351, 0.506).all())\nsig = F4D[F4D.p < 0.05]\nprint(\"reading (b) rho of planes at p < 0.05:\", sig.rho.round(3).tolist(), \"in 0.351..0.506:\", bool(len(sig)) and sig.rho.between(0.351, 0.506).all())\nprint(f\"share of planes at p < 0.05: {share:.0f}% (paper 66, tolerance 59.4..72.6)\")\n\n# %% [markdown]\n# ### fig4f-plane-alignment-explains-jpca\n# > Conditions without clear rotations in the jPCA planes had rotations misaligned with those planes; the\n# > alignment index with the jPCA plane correlated strongly with the variance jPCA captured (rho 0.82 to 0.97).\n\n# %% tags=[\"claim:fig4f-plane-alignment-explains-jpca\"]\nF4F = []\nfor n in NAMES:\n    tb, r = TBF[n], ROT[n]\n    inds = np.where(tb[\"freq\"] > 0)[0]\n    ok = ~np.isnan(tb[\"B\"][:, 0])\n    meanL = tb[\"L\"].mean(0)\n    for p in range(PLANES[n]):\n        J = r[\"jp\"][\"jPCs_highD\"][:, 2 * p:2 * p + 2]\n        ov = np.array([ldr.alignment_index(r[\"sn\"][:, None] * ((tb[\"L\"][c][:, inds] - meanL[:, inds]) @ tb[\"B\"][ok][:, inds].T), J)\n                       for c in range(72)])\n        jv = np.nansum(np.nanvar(r[\"rot\"][:, 2 * p:2 * p + 2], axis=2, ddof=1), axis=1)\n        rr = stats.pearsonr(jv, ov)\n        F4F.append(dict(dataset=n, plane=p + 1, rho=rr[0], p=rr[1], align_min=ov.min(), align_max=ov.max()))\nF4F = pd.DataFrame(F4F)\nprint(F4F.round(4).to_string(index=False))\nokf = (F4F.rho.between(0.738, 1)) & (F4F.p < 0.001)\nprint(f\"planes with rho in 0.738..1 and p < 0.001: {okf.sum()} of {len(F4F)}\")\n\n# %% [markdown]\n# ## single-lds-variance\n# > A single linear dynamical system fitted to all conditions captured on average 46 to 66% of the population\n# > variance.\n#\n# Code fitSingleLDS.m: one full-rank M from each bin to the next over all conditions from bin 20 on; each\n# condition simulated forward from bin 20.\n\n# %% tags=[\"claim:single-lds-variance\"]\nSINGLE = {}\nfor n in NAMES:\n    X = DS[n][\"X\"]\n    X1 = np.concatenate([x[:, ldr.T0:-1] for x in X], 1)\n    X2 = np.concatenate([x[:, ldr.T0 + 1:] for x in X], 1)\n    M = X2 @ np.linalg.pinv(X1)\n    va, vb = [], []\n    for x in X:\n        s = x.copy()\n        for t in range(ldr.T0 + 1, ldr.NT):\n            s[:, t] = M @ s[:, t - 1]\n        sa = s.copy(); sa[:, :ldr.T0] = np.nan\n        va.append(ldr.var_explained(x[None], sa[None], clip=False)[0])\n        vb.append(1 - (s - x).var(1, ddof=1).sum() / x.var(1, ddof=1).sum())\n    va, vb = np.array(va), np.array(vb)\n    SINGLE[n] = va\n    print(f\"{n}: (a) -150..850 mean {va.mean()*100:.1f}% (s.d. {va.std(ddof=1)*100:.1f}, min {va.min()*100:.1f}); \"\n          f\"(b) whole window {vb.mean()*100:.1f}%; in 41.4..72.6%: {0.414 <= va.mean() <= 0.726}, {0.414 <= vb.mean() <= 0.726}\")\n\n# %% [markdown]\n# ## fig2c-condition-lds-variance\n# > Activity on each single condition was low-dimensional and approximated by an LDS of 5 to 9 dimensions,\n# > which explained 71 to 93% of the population variance.\n#\n# The LDS per condition is the code's idDynamics.m (reduced-rank regression of the least-squares dynamics\n# from bin 20 on, simulation from bin 20, half-lives capped at 10 s). Dimensionality: the Methods (Fitting\n# dynamics to single conditions) describe the cross-validation as projecting one partition's average onto\n# its top k singular vectors and measuring the variance explained in the other's; the code's\n# crossValidateDimensionalityConditions.m scores the LDS fit itself (its idDynamics returns the training\n# data as the approximation, so the published code cannot choose k; the simulation is used here). Both\n# scores are run, with odd k from 1 to 21 (code), under the Methods' even split and the code's 3/4 split.\n\n# %%\nKS = np.arange(1, 22, 2)\ndef lds_cv(d, g, folds=100, ratio=0.5):\n    C = 72\n    proj = np.zeros((len(KS), folds, C)); sim = np.zeros((len(KS), folds, C))\n    for f in range(folds):\n        a = ldr.split_halves(d[\"cond\"], g, ratio)\n        Xa = ldr.cond_average(d[\"Xt\"][a], d[\"cond\"][a]); Xb = ldr.cond_average(d[\"Xt\"][~a], d[\"cond\"][~a])\n        for c in range(C):\n            xa, xb = Xa[c], Xb[c]\n            win = xa[:, ldr.T0:]\n            Up, _, _ = np.linalg.svd(win, full_matrices=False)\n            A = xa[:, ldr.T0 + 1:] @ np.linalg.pinv(xa[:, ldr.T0:-1])\n            U, _, _ = np.linalg.svd(A @ win, full_matrices=False)\n            yb = xb[:, ldr.T0:]\n            den = yb.var(1, ddof=1).sum()\n            for i, k in enumerate(KS):\n                P = Up[:, :k]\n                proj[i, f, c] = max(0, 1 - (yb - P @ (P.T @ win)).var(1, ddof=1).sum() / den)\n                Uk = U[:, :k]; Ak = Uk.T @ A @ Uk\n                z = Uk.T @ A @ win[:, 0]\n                s = np.zeros_like(win); s[:, 0] = win[:, 0]\n                for t in range(1, win.shape[1]):\n                    s[:, t] = Uk @ z; z = Ak @ z\n                sim[i, f, c] = max(0, 1 - (yb - s).var(1, ddof=1).sum() / den)\n    return proj, sim\n\nT = time.time()\nLCV = {}\nfor n in NAMES:\n    LCV[n] = {}\n    for ratio in (0.5, 0.75):\n        LCV[n][ratio] = lds_cv(DS[n], ldr.rng(\"fig2c-condition-lds-variance\", 0 if ratio == 0.5 else 1), 100, ratio)\nprint(f\"cross-validation in {time.time() - T:.0f} s\")\n\n# %% tags=[\"claim:fig2c-condition-lds-variance\"]\nKLDS = {}\nLDSVE = {}\nfor n in NAMES:\n    X = DS[n][\"X\"]\n    line = []\n    for ratio in (0.5, 0.75):\n        proj, sim = LCV[n][ratio]\n        kp, ks = KS[proj.mean((1, 2)).argmax()], KS[sim.mean((1, 2)).argmax()]\n        line.append(f\"split {ratio}: projection k={kp} (curve {np.round(proj.mean((1, 2))[:6], 3)}), \"\n                    f\"LDS k={ks} (curve {np.round(sim.mean((1, 2))[:6], 3)})\")\n        if ratio == 0.5:\n            KLDS[n] = dict(proj=kp, sim=ks)\n    print(n + \": \" + \"; \".join(line))\n    for kk in sorted(set([KLDS[n][\"proj\"], KLDS[n][\"sim\"], 5, 7, 9])):\n        ve = np.array([ldr.var_explained(X[c:c + 1], ldr.lds_fit(X[c], kk)[1][None])[0] for c in range(72)])\n        LDSVE[(n, kk)] = ve\n        print(f\"     k={kk}: mean VE {ve.mean()*100:.1f}% (s.d. {ve.std(ddof=1)*100:.1f})\")\nfor n in NAMES:\n    for rd in (\"proj\", \"sim\"):\n        kk = KLDS[n][rd]\n        print(f\"{n} reading {rd}: k={kk} in 5..9: {5 <= kk <= 9}; VE {LDSVE[(n, kk)].mean()*100:.1f}% in 63.9..100: \"\n              f\"{LDSVE[(n, kk)].mean() >= 0.639}\")\n\n# %% [markdown]\n# Seed check: the chosen k under the five seeds, with 20 folds each for time (the claim's own seed above uses\n# the full 100).\n\n# %%\nfor n in NAMES:\n    ks = []\n    for k in SEED_OFFSETS:\n        proj, sim = lds_cv(DS[n], ldr.rng(\"fig2c-condition-lds-variance\", k), 20, 0.5)\n        ks.append((KS[proj.mean((1, 2)).argmax()], KS[sim.mean((1, 2)).argmax()]))\n    print(n, \"k (projection, LDS) under five seeds, 20 folds:\", ks)\n\n# %% [markdown]\n# ## fig3a-eigenvalue-clusters\n# > Eigenvalues of the single-condition LDSs formed distinct clusters, corresponding to rotations at about\n# > 0.5, 1.5, 2.5 and 4 Hz on every condition, along with an offset.\n\n# %% tags=[\"claim:fig3a-eigenvalue-clusters\"]\nEIG = {}\nfor n in NAMES:\n    X = DS[n][\"X\"]\n    for rd in (\"proj\", \"sim\"):\n        kk = KLDS[n][rd]\n        E = np.stack([ldr.sort_eigs(ldr.lds_eigs(X[c], kk)) for c in range(72)])\n        EIG[(n, rd)] = E\n        npair = (kk - 1) // 2\n        fr = []\n        for c in range(72):\n            cf = np.sort(ldr.freq_hz(E[c][np.imag(E[c]) > 1e-12]))\n            fr.append(np.r_[cf, np.full(npair, np.nan)][:npair])\n        fr = np.array(fr)\n        med = np.nanmedian(fr, 0)\n        nreal = (np.abs(np.imag(E)) <= 1e-12).sum(1)\n        tgt = np.array([0.5, 1.5, 2.5, 4.0])[:npair]\n        ok = np.abs(med - tgt) <= 0.1 * tgt\n        print(f\"{n} reading {rd} (k={kk}): median pair frequencies {np.round(med, 2)} Hz against {tgt}; within 10%: \"\n              f\"{ok}; conditions with a real eigenvalue {np.mean(nreal >= 1)*100:.0f}%; frequency IQR per pair \"\n              f\"{np.round(np.nanpercentile(fr, 75, 0) - np.nanpercentile(fr, 25, 0), 2)}\")\n\n# %% [markdown]\n# ## fig3c-eigenvalue-distance-auc\n# > Eigenvalues differed between conditions only slightly more than expected from estimation noise, with\n# > ROC-AUC 0.51 to 0.58 between the between-condition distances and the noise distribution.\n#\n# Distance: mean over corresponding (frequency-sorted) eigenvalues of their distance (main), and the code's\n# norm of the difference (variant). Nulls: (b) random halves of the real trials, 500 repeats (code\n# compareTrialSimilarity.m); (a) two sets of 20 Poisson trials from each condition's rates, smoothed and\n# averaged, run with 50 repeats per condition (the Methods' 500 did not fit the time; see the notes).\n# The LDS dimensionality is the one chosen above (projection reading).\n\n# %%\ndef eig_dist(E1, E2, kind=\"mean\"):\n    d = np.abs(E1 - E2)\n    return d.mean(-1) if kind == \"mean\" else np.sqrt((d ** 2).sum(-1))\n\ndef null_halves(d, kk, g, reps):\n    out = np.zeros((72, reps, kk), complex), np.zeros((72, reps, kk), complex)\n    for r in range(reps):\n        a = ldr.split_halves(d[\"cond\"], g, 0.5)\n        Xa = ldr.cond_average(d[\"Xt\"][a], d[\"cond\"][a]); Xb = ldr.cond_average(d[\"Xt\"][~a], d[\"cond\"][~a])\n        for c in range(72):\n            out[0][c, r] = ldr.sort_eigs(ldr.lds_eigs(Xa[c], kk))\n            out[1][c, r] = ldr.sort_eigs(ldr.lds_eigs(Xb[c], kk))\n    return out\n\nKERN = None\ndef smooth_matrix():\n    # rows: the 121 grid samples; columns: 1201 ms bins; the code's smoothing as a matrix\n    e = np.eye(1201, dtype=np.float32)\n    x = np.zeros((1201, 1210), np.float32); x[:, 5:1206] = e\n    from scipy.ndimage import gaussian_filter1d\n    return gaussian_filter1d(e * 1000, 20, axis=-1, mode=\"reflect\", truncate=55 / 20)[:, ::10]\n\ndef null_poisson(d, kk, g, reps, ntr=20):\n    global KERN\n    if KERN is None:\n        KERN = smooth_matrix()  # 1201 x 121\n    X = d[\"X\"]\n    out = np.zeros((72, reps, kk), complex), np.zeros((72, reps, kk), complex)\n    # rates at 1 ms by linear interpolation of the 10 ms condition average (code generateTrials.m)\n    tt = np.arange(-350, 851)\n    for c in range(72):\n        lam = np.stack([np.interp(tt, ldr.TIMES, x) for x in X[c]]) / 1000 * ntr\n        lam = np.clip(lam, 0, None)\n        for r in range(reps):\n            for h in range(2):\n                cnt = g.poisson(lam).astype(np.float32) / ntr\n                xa = cnt @ KERN\n                out[h][c, r] = ldr.sort_eigs(ldr.lds_eigs(xa.astype(float), kk))\n    return out\n\nT = time.time()\nF3C = {}\nfor n in NAMES:\n    kk = KLDS[n][\"proj\"]\n    E = EIG[(n, \"proj\")]\n    obs = {kind: np.array([eig_dist(E[i], E[j], kind) for i in range(72) for j in range(72) if i != j]) for kind in (\"mean\", \"norm\")}\n    nb = null_halves(DS[n], kk, ldr.rng(\"fig3c-eigenvalue-distance-auc\"), 500)\n    na = null_poisson(DS[n], kk, ldr.rng(\"fig3c-eigenvalue-distance-auc\", 1), 50)\n    F3C[n] = dict(obs=obs, nb=nb, na=na, k=kk)\nprint(f\"nulls in {time.time() - T:.0f} s\")\n\n# %% tags=[\"claim:fig3c-eigenvalue-distance-auc\"]\nfor n in NAMES:\n    f = F3C[n]\n    line = []\n    for nm, nl in ((\"halves\", f[\"nb\"]), (\"Poisson\", f[\"na\"])):\n        for kind in (\"mean\", \"norm\"):\n            nd = eig_dist(nl[0], nl[1], kind).ravel()\n            auc, raw = ldr.auc_folded(f[\"obs\"][kind], nd)\n            line.append(f\"{nm}/{kind}: AUC {auc:.3f} (obs median {np.median(f['obs'][kind]):.4f} vs null {np.median(nd):.4f})\")\n    print(f\"{n} (k={f['k']}): \" + \"; \".join(line))\n\n# %% [markdown]\n# Seed check for the halves null with the mean distance (100 repeats per seed, for time).\n\n# %%\nfor n in NAMES:\n    f = F3C[n]\n    aucs = []\n    for k in SEED_OFFSETS:\n        nl = null_halves(DS[n], f[\"k\"], ldr.rng(\"fig3c-eigenvalue-distance-auc\", k), 100)\n        aucs.append(ldr.auc_folded(f[\"obs\"][\"mean\"], eig_dist(nl[0], nl[1], \"mean\").ravel())[0])\n    print(n, \"AUC under five seeds (100 repeats):\", np.round(aucs, 3))\n\n# %% [markdown]\n# ## suppfig2-eigenvalues-from-kinematics\n# > Kinematic parameters predicted the eigenvalues poorly (mean R2 = 0.1, leave-one-out cross-validation).\n#\n# Code getCorrelationsWithFrequency.m: predictors the four reach parameters (kinematic basis as in fig6e,\n# both readings), the reach duration (as in fig3i) and a constant; targets the real and imaginary parts of\n# each eigenvalue of the condition's LDS; least squares, leave one condition out; R2 per component, negatives\n# 0, components with no variance (the imaginary part of a real eigenvalue) left out; mean over components\n# pooled over the four datasets.\n\n# %% tags=[\"claim:suppfig2-eigenvalues-from-kinematics\"]\nKB = {rd: ldr.kin_basis([DS[\"M1-J\"][\"kin\"], DS[\"M1-N\"][\"kin\"]], rd) for rd in (\"svd\", \"skewnormal\")}\nfor rd in (\"svd\", \"skewnormal\"):\n    for erd in (\"proj\", \"sim\"):\n        r2s = []\n        per = {}\n        for n in NAMES:\n            E = EIG[(n, erd)]\n            Y = np.c_[np.real(E), np.imag(E)]\n            Y = Y[:, Y.std(0) > 1e-12]\n            P = ldr.reach_params(KB[rd][0], DS[n][\"kin\"])\n            Xk = np.c_[P, WARP[n][\"dur\"], np.ones(72)]\n            Yh = np.zeros_like(Y)\n            for c in range(72):\n                tr = np.arange(72) != c\n                W = np.linalg.pinv(Xk[tr]) @ Y[tr]\n                Yh[c] = Xk[c] @ W\n            r2 = np.clip(1 - (Yh - Y).var(0, ddof=1) / Y.var(0, ddof=1), 0, None)\n            per[n] = r2.mean(); r2s.extend(r2)\n        print(f\"kinematic basis {rd}, eigenvalues {erd}: mean R2 pooled {np.mean(r2s):.3f} (in 0.05..0.15: \"\n              f\"{0.05 <= np.mean(r2s) <= 0.15}); per dataset {({k: round(v, 3) for k, v in per.items()})}\")\n\n# %% [markdown]\n# ## suppfig3-model-comparison\n# > The model with shared eigenvalues and condition-specific planes (LDR) explained more cross-validated\n# > variance than jPCA or condition-specific LDSs.\n\n# %% tags=[\"claim:suppfig3-model-comparison\"]\nfor n in NAMES:\n    cv_tbf = CV[n][\"mean\"][K[n] - 1]\n    lds_ve = LDSVE[(n, KLDS[n][\"proj\"])].mean()\n    jp = ROT[n][\"ve\"].mean()\n    print(f\"{n}: TBF held-out {cv_tbf*100:.1f}% (in-sample {VE_TBF[n].mean()*100:.1f}%), single-condition LDS \"\n          f\"{lds_ve*100:.1f}% (k={KLDS[n]['proj']}), jPCA {jp*100:.1f}%; TBF highest (cross-validated): \"\n          f\"{cv_tbf > max(lds_ve, jp)}; (in-sample): {VE_TBF[n].mean() > max(lds_ve, jp)}\")\n\n# %% [markdown]\n# ## Geometry of the rotations\n# Alignment index as in the code (getAlignmentIndex.m). Noise: per condition, loadings regressed on the\n# fixed (corrected raw) basis for two random halves of its trials, 36 repeats (Methods; the code's 200 a\n# variant, not run for time). ROC-AUC folded to at least 0.5.\n\n# %%\ndef noise_loadings(d, tb, g, reps):\n    raw = tb[\"raw\"]\n    pin = np.linalg.pinv(raw.T)\n    L1 = np.zeros((reps, 72) + tb[\"L\"].shape[1:]); L2 = np.zeros_like(L1)\n    for r in range(reps):\n        a = ldr.split_halves(d[\"cond\"], g, 0.5)\n        L1[r] = ldr.cond_average(d[\"Xt\"][a], d[\"cond\"][a]) @ pin\n        L2[r] = ldr.cond_average(d[\"Xt\"][~a], d[\"cond\"][~a]) @ pin\n    return L1, L2\n\ndef ai_matrix(L, B, inds, inds2=None):\n    inds2 = inds if inds2 is None else inds2\n    ok = ~np.isnan(B[:, 0])\n    out = np.zeros((72, 72))\n    for i in range(72):\n        D = L[i][:, inds] @ B[ok][:, inds].T\n        Dc = D - D.mean(1, keepdims=True)\n        den = (Dc ** 2).sum()\n        for j in range(72):\n            Q = np.linalg.qr(L[j][:, inds2])[0]\n            r = Dc - Q @ (Q.T @ Dc)\n            out[i, j] = max(0, 1 - (r ** 2).sum() / den)\n    return out\n\nGEO = {}\nT = time.time()\nfor n in NAMES:\n    tb = TBF[n]\n    gr = ldr.groups(tb)\n    L1, L2 = noise_loadings(DS[n], tb, ldr.rng(\"fig4b-plane-alignment\"), 36)\n    ok = ~np.isnan(tb[\"B\"][:, 0])\n    comps = {}\n    for f, inds in gr:\n        obs = ai_matrix(tb[\"L\"], tb[\"B\"], inds)\n        noise = np.array([[ldr.alignment_index(L1[r, c][:, inds] @ tb[\"B\"][ok][:, inds].T, L2[r, c][:, inds])\n                           for r in range(36)] for c in range(72)])\n        comps[f] = dict(inds=inds, obs=obs, noise=noise)\n    GEO[n] = dict(groups=gr, comps=comps, L1=L1, L2=L2)\nprint(f\"alignment in {time.time() - T:.0f} s\")\n\ndef offdiag(M):\n    return M[~np.eye(len(M), dtype=bool)]\n\n# %% [markdown]\n# ### fig4b-plane-alignment\n# > Same-frequency rotational planes on pairs of conditions were far less aligned than expected from\n# > estimation noise (ROC-AUC 0.85 to 0.96).\n\n# %% tags=[\"claim:fig4b-plane-alignment\"]\nrows = []\nfor n in NAMES:\n    for f, cc in GEO[n][\"comps\"].items():\n        if len(cc[\"inds\"]) != 2:\n            continue\n        o, z = offdiag(cc[\"obs\"]), cc[\"noise\"].ravel()\n        auc, _ = ldr.auc_folded(o, z)\n        per_c = np.array([np.r_[cc[\"obs\"][c, :c], cc[\"obs\"][c, c + 1:]].mean() for c in range(72)])\n        pa = stats.wilcoxon(per_c, cc[\"noise\"].mean(1)).pvalue\n        pb = stats.ranksums(o, z).pvalue\n        rows.append(dict(dataset=n, freq=round(f, 2), obs_mean=o.mean(), noise_mean=z.mean(), auc=auc,\n                         p_signrank=pa, p_ranksum=pb))\nF4B = pd.DataFrame(rows)\nprint(F4B.round(4).to_string(index=False))\nok = F4B.auc.between(0.765, 1) & (F4B.obs_mean < F4B.noise_mean)\nprint(f\"rotations with AUC in 0.765..1 and observed lower: {ok.sum()} of {len(F4B)}; signed-rank p < 0.001 for \"\n      f\"{(F4B.p_signrank < 0.001).sum()}, rank-sum p < 0.001 for {(F4B.p_ranksum < 0.001).sum()}\")\n# seed check\nfor n in NAMES:\n    tb = TBF[n]; ok_ = ~np.isnan(tb[\"B\"][:, 0]); aucs = []\n    for k in SEED_OFFSETS[1:]:\n        A1, A2 = noise_loadings(DS[n], tb, ldr.rng(\"fig4b-plane-alignment\", k), 36)\n        a_ = []\n        for f, cc in GEO[n][\"comps\"].items():\n            if len(cc[\"inds\"]) != 2: continue\n            nz = np.array([[ldr.alignment_index(A1[r, c][:, cc[\"inds\"]] @ tb[\"B\"][ok_][:, cc[\"inds\"]].T, A2[r, c][:, cc[\"inds\"]])\n                            for r in range(36)] for c in range(72)])\n            a_.append(ldr.auc_folded(offdiag(cc[\"obs\"]), nz.ravel())[0])\n        aucs.append(np.round(a_, 3))\n    print(n, \"AUC per rotation under seeds +1000..+4000:\", aucs)\n\n# %% [markdown]\n# ### suppfig6a-location-alignment\n# > The state space location occupied different dimensions across conditions, less aligned than expected\n# > from estimation noise (ROC-AUC 0.88 to 0.95).\n\n# %% tags=[\"claim:suppfig6a-location-alignment\"]\nfor n in NAMES:\n    for f, cc in GEO[n][\"comps\"].items():\n        if len(cc[\"inds\"]) != 1:\n            continue\n        o, z = offdiag(cc[\"obs\"]), cc[\"noise\"].ravel()\n        auc, _ = ldr.auc_folded(o, z)\n        per_c = np.array([np.r_[cc[\"obs\"][c, :c], cc[\"obs\"][c, c + 1:]].mean() for c in range(72)])\n        pa = stats.wilcoxon(per_c, cc[\"noise\"].mean(1)).pvalue\n        print(f\"{n} offset (freq {f:.2f}): observed {o.mean():.3f}, noise {z.mean():.3f}, AUC {auc:.3f} (in 0.792..1: \"\n              f\"{0.792 <= auc <= 1}), signed-rank p = {pa:.2g}, rank-sum p = {stats.ranksums(o, z).pvalue:.2g}\")\n\n# %% [markdown]\n# ### fig5a-frequencies-segregated and suppfig6c-location-distinct-from-rotations\n# > Different-frequency rotational planes on pairs of conditions were nearly orthogonal, and same-frequency\n# > planes were better aligned.\n#\n# > State space location dimensions were distinct from those of the rotations.\n\n# %%\nCROSS = {}\nfor n in NAMES:\n    tb = TBF[n]\n    gr = GEO[n][\"groups\"]\n    for f1, i1 in gr:\n        for f2, i2 in gr:\n            if f1 == f2:\n                continue\n            CROSS[(n, f1, f2)] = ai_matrix(tb[\"L\"], tb[\"B\"], i1, i2)\n\n# %% tags=[\"claim:fig5a-frequencies-segregated\"]\nrows = []\nfor n in NAMES:\n    gr = GEO[n][\"groups\"]\n    for f1, i1 in gr:\n        if len(i1) != 2: continue\n        same = GEO[n][\"comps\"][f1][\"obs\"]\n        for f2, i2 in gr:\n            if f2 == f1 or len(i2) != 2: continue\n            diff = CROSS[(n, f1, f2)]\n            a, b = offdiag(same), offdiag(diff)\n            pa = stats.wilcoxon(a, b).pvalue\n            pb = stats.ranksums(a, b).pvalue\n            rows.append(dict(dataset=n, rot=round(f1, 2), other=round(f2, 2), same=a.mean(), different=b.mean(),\n                             p_paired=pa, p_ranksum=pb))\nF5A = pd.DataFrame(rows)\nprint(F5A.round(4).to_string(index=False))\nfor col in (\"p_paired\", \"p_ranksum\"):\n    okk = (F5A.same > F5A.different) & (F5A[col] < 0.001)\n    print(f\"{col}: same higher with p < 0.001 in {okk.sum()} of {len(F5A)} ({okk.mean()*100:.0f}%)\")\n\n# %% tags=[\"claim:suppfig6c-location-distinct-from-rotations\"]\nfor n in NAMES:\n    gr = GEO[n][\"groups\"]\n    off = [f for f, i in gr if len(i) == 1][0]\n    same = offdiag(GEO[n][\"comps\"][off][\"obs\"])\n    for f2, i2 in gr:\n        if f2 == off: continue\n        b = offdiag(CROSS[(n, off, f2)])\n        print(f\"{n}: location->location {same.mean():.3f} vs location->rotation {f2:.2f} Hz {b.mean():.3f}; \"\n              f\"paired signed-rank p = {stats.wilcoxon(same, b).pvalue:.2g}, rank-sum p = {stats.ranksums(same, b).pvalue:.2g}\")\n\n# %% [markdown]\n# ### fig4c-subspace-excursion-angles and suppfig6b-location-dimensionality (SEA part)\n# Subspace excursion angles to 25 dimensions (code subspaceExcursionAngles.m, maxTol 0). Noise: per condition,\n# the SEA of the 72 half-split loading estimates (36 repeats x 2 halves; the code uses 200 repeats, 400\n# estimates), and for each dimension the fraction of conditions whose noise angle exceeds the data's\n# (code singleFrequencyOverlapControl.m).\n\n# %%\nT = time.time()\nSEA = {}\nfor n in NAMES:\n    tb = TBF[n]\n    for f, inds in GEO[n][\"groups\"]:\n        data_sea = ldr.sea(tb[\"L\"][:, :, inds], 25)\n        L1, L2 = GEO[n][\"L1\"], GEO[n][\"L2\"]\n        noise = np.array([ldr.sea(np.concatenate([L1[:, c][:, :, inds], L2[:, c][:, :, inds]]), 25) for c in range(72)])\n        SEA[(n, f)] = dict(data=data_sea, noise=noise, p=(noise > data_sea[None]).mean(0))\nprint(f\"SEA in {time.time() - T:.0f} s\")\n\n# %% tags=[\"claim:fig4c-subspace-excursion-angles\"]\nrows = []\nfor (n, f), s in SEA.items():\n    if f == 0 or len([1 for ff, i in GEO[n][\"groups\"] if ff == f and len(i) == 2]) == 0:\n        continue\n    n45 = int((s[\"data\"] > 45).sum())\n    nabove = int((s[\"p\"] < 0.05).sum())\n    rows.append(dict(dataset=n, freq=round(f, 2), above45=n45, above_noise=nabove,\n                     first=s[\"data\"][0], tenth=s[\"data\"][9], last=s[\"data\"][-1]))\nF4C = pd.DataFrame(rows)\nprint(F4C.round(1).to_string(index=False))\nprint(\"counts above 45 deg in 5.4..22:\", F4C.above45.between(5.4, 22).sum(), \"of\", len(F4C),\n      \"| dimensions above noise exceed the count above 45 deg:\", (F4C.above_noise > F4C.above45).sum(), \"of\", len(F4C))\n\n# %% [markdown]\n# ### rotation-orientation-dimensionality and suppfig6b-location-dimensionality\n# > Rotation orientations required 23 to 40 principal components to capture 80% of their variance, had 7 to\n# > 33 dimensions with SNR above 1, and participation ratios of 16.7 to 36.8.\n#\n# PCA readings: (a) the loading columns of each condition stacked as observations; (b) the rotation's\n# activity (loading columns times basis functions) of all conditions as observations. SNR dimensionality:\n# code crossValidateDimensionalityRotations.m (halves, 100 folds; basis from one half, loadings of both\n# halves on its raw basis; the dimensionality of the PCA of half 1's loadings that maximises the variance\n# explained in half 2's rotation, 1 to 50 dimensions).\n\n# %%\ndef snr_dims(d, k, g, folds=100):\n    res = {}\n    for fo in range(folds):\n        a = ldr.split_halves(d[\"cond\"], g, 0.5)\n        Xa = ldr.cond_average(d[\"Xt\"][a], d[\"cond\"][a]); Xb = ldr.cond_average(d[\"Xt\"][~a], d[\"cond\"][~a])\n        tb = ldr.eig_transform(Xa, k)\n        Lb = Xb @ np.linalg.pinv(tb[\"raw\"].T)\n        Bv = tb[\"B\"][ldr.T0 + 1:]\n        for gi, (f, inds) in enumerate(ldr.groups(tb)):\n            cols = np.concatenate(list(tb[\"L\"][:, :, inds]), 1)\n            U = np.linalg.svd(cols, full_matrices=False)[0]\n            tr = Lb[:, :, inds] @ Bv[:, inds].T      # 72 x N x T\n            den = tr.var(2, ddof=1).sum(1)\n            for dim in range(1, min(51, U.shape[1] + 1)):\n                P = U[:, :dim] @ U[:, :dim].T\n                pr = np.einsum(\"nm,cmk->cnk\", P, tb[\"L\"][:, :, inds]) @ Bv[:, inds].T\n                ve = 1 - (pr - tr).var(2, ddof=1).sum(1) / den\n                res.setdefault((gi, len(inds)), np.zeros((folds, 50)))[fo, dim - 1] = ve.mean()\n    return {key: int(v.mean(0).argmax() + 1) for key, v in res.items()}\n\nT = time.time()\nSNR = {n: snr_dims(DS[n], K[n], ldr.rng(\"rotation-orientation-dimensionality\"), 100) for n in NAMES}\nprint(f\"SNR dimensionality in {time.time() - T:.0f} s\")\n\n# %% tags=[\"claim:rotation-orientation-dimensionality\"]\nrows = []\nfor n in NAMES:\n    tb = TBF[n]\n    ok = ~np.isnan(tb[\"B\"][:, 0])\n    for gi, (f, inds) in enumerate(GEO[n][\"groups\"]):\n        colsA = np.concatenate([tb[\"L\"][c][:, inds].T for c in range(72)])          # (72*w) x N\n        actB = np.concatenate([(tb[\"L\"][c][:, inds] @ tb[\"B\"][ok][:, inds].T).T for c in range(72)])\n        pa, pra = ldr.pca_dims(colsA)\n        pb, prb = ldr.pca_dims(actB)\n        rows.append(dict(dataset=n, freq=round(f, 2), kind=\"rotation\" if len(inds) == 2 else \"location\",\n                         pcs80_a=pa, pr_a=pra, pcs80_b=pb, pr_b=prb, snr_dims=SNR[n].get((gi, len(inds)))))\nDIM = pd.DataFrame(rows)\nprint(DIM.round(1).to_string(index=False))\nR = DIM[DIM.kind == \"rotation\"]\nfor rd in (\"a\", \"b\"):\n    print(f\"rotations, reading {rd}: PCs to 80% in 20.7..44 {R[f'pcs80_{rd}'].between(20.7, 44).sum()}/{len(R)}; \"\n          f\"participation ratio in 15.03..40.48 {R[f'pr_{rd}'].between(15.03, 40.48).sum()}/{len(R)}\")\nprint(f\"rotations: SNR dimensions in 6.3..36.3 {R.snr_dims.between(6.3, 36.3).sum()}/{len(R)}\")\n\n# %% tags=[\"claim:suppfig6b-location-dimensionality\"]\nLc = DIM[DIM.kind == \"location\"]\nfor (n, f), s in SEA.items():\n    if f == 0 or any(ff == f and len(i) == 1 for ff, i in GEO[n][\"groups\"]):\n        if any(ff == f and len(i) == 1 for ff, i in GEO[n][\"groups\"]):\n            print(f\"{n} location: SEA angles above 15 deg {int((s['data'] > 15).sum())} (in 3.6..5.5: \"\n                  f\"{3.6 <= (s['data'] > 15).sum() <= 5.5}); first angles {np.round(s['data'][:8], 1)}\")\nprint(Lc.round(1).to_string(index=False))\nfor rd in (\"a\", \"b\"):\n    print(f\"location, reading {rd}: PCs in 18.9..33 {Lc[f'pcs80_{rd}'].between(18.9, 33).sum()}/4; \"\n          f\"participation ratio in 13.59..29.04 {Lc[f'pr_{rd}'].between(13.59, 29.04).sum()}/4\")\nprint(f\"location: SNR dimensions in 4.5..13.2 {Lc.snr_dims.between(4.5, 13.2).sum()}/4\")\n\n# %% [markdown]\n# ## Summary\n# (Written after the run; see the record.)\n\n# %%\nprint(f\"notebook ran in {(time.time() - T_START)/60:.1f} min; peak memory \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb1.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb1.py').read()
s=s.replace('''# %% [markdown]
# **Result: ...** see the summary below the code for each claim. Conditions: under both readings each monkey has 72
# conditions, 36 without barriers (straight) and 36 with barriers (curved). Trials: J 1595 (all successful)
# and 1381 (delay above 400 ms), both within 10% of 1469; N 2121 and 1884, both within 10% of 2014. Units: 96
# per array, inside 71 to 130, but they are unsorted threshold crossings, so the dataset marks no single or
# multi-units and the paper's count of sorted units cannot be checked.

''','')
old=s[s.index('# %% tags=["claim:suppfig6b-location-dimensionality"]'):s.index('# %% [markdown]\n# ## Summary')]
new='''# %% tags=["claim:suppfig6b-location-dimensionality"]
Lc = DIM[DIM.kind == "location"]
for n in NAMES:
    off = [f for f, i in GEO[n]["groups"] if len(i) == 1][0]
    s = SEA[(n, off)]
    n15 = int((s["data"] > 15).sum())
    print(f"{n} location: SEA angles above 15 deg {n15} (in 3.6..5.5: {3.6 <= n15 <= 5.5}); first angles "
          f"{np.round(s['data'][:8], 1)}; dimensions above noise {int((s['p'] < 0.05).sum())}")
print(Lc.round(1).to_string(index=False))
for rd in ("a", "b"):
    print(f"location, reading {rd}: PCs in 18.9..33 {Lc[f'pcs80_{rd}'].between(18.9, 33).sum()}/4; "
          f"participation ratio in 13.59..29.04 {Lc[f'pr_{rd}'].between(13.59, 29.04).sum()}/4")
print(f"location: SNR dimensions in 4.5..13.2 {Lc.snr_dims.between(4.5, 13.2).sum()}/4")

'''
s=s.replace(old,new)
s=s.replace('''    if f == 0 or len([1 for ff, i in GEO[n]["groups"] if ff == f and len(i) == 2]) == 0:
        continue''','''    if not any(ff == f and len(i) == 2 for ff, i in GEO[n]["groups"]):
        continue''')
open('nb1.py','w').write(s)
d=s.replace('DS = ldr.build("all")','import pickle\nDS = pickle.load(open("/tmp/claude-1001/DSJ.pkl","rb")) if __import__("os").path.exists("/tmp/claude-1001/DSJ.pkl") else ldr.build("all", monkeys=("J",))\npickle.dump(DS, open("/tmp/claude-1001/DSJ.pkl","wb"), protocol=4)')
d=d.replace('NAMES = ldr.DATASETS','NAMES = ["M1-J","PMd-J"]')
d=d.replace('folds=100)','folds=10)').replace('100, ratio)','10, ratio)').replace(', 500)',', 20)').replace(', 50)',', 5)').replace(', 100)\n        aucs',', 10)\n        aucs').replace('"), 100) for n','"), 5) for n').replace('lds_cv(DS[n], ldr.rng("fig2c-condition-lds-variance", k), 20, 0.5)','lds_cv(DS[n], ldr.rng("fig2c-condition-lds-variance", k), 3, 0.5)')
d=d.replace('for k in SEED_OFFSETS:\n        Xs','for k in SEED_OFFSETS[:2]:\n        Xs').replace('for k in (SEED_OFFSETS if mode','for k in (SEED_OFFSETS[:2] if mode')
d=d.replace('for c in range(72)])\n        SEA','for c in range(3)])\n        SEA')
d=d.replace('# Recordings deposited more than once','r=[]\n# Recordings deposited more than once').replace('for a in sorted(r, key=lambda a: a["path"]):','for a in sorted(r, key=lambda a: a["path"])[:2]:')
d='import matplotlib; matplotlib.use("Agg")\n'+d
open('dev_nb1.py','w').write(d)
EOF
grep -n "range(3)\]" dev_nb1.py | head; cd $TMPDIR && . env/bin/activate && cd entries/sabatini-2024 && timeout 3000 python $TMPDIR/dev_nb1.py 2>&1 | tail -150; date -u
```

```
898:        noise = np.array([ldr.sea(np.concatenate([L1[:, c][:, :, inds], L2[:, c][:, :, inds]]), 25) for c in range(3)])
Traceback (most recent call last):
  File "/tmp/claude-1001/dev_nb1.py", line 33, in <module>
    import ldr
ModuleNotFoundError: No module named 'ldr'
Fri Nov 27 22:26:56 UTC 2026
```

**Agent calls Bash**

```bash
. $TMPDIR/env/bin/activate && PYTHONPATH=. timeout 3000 python $TMPDIR/dev_nb1.py 2>&1 | tail -150; date -u
```

```
loaded in 30 s, peak memory 1.6 GB
monkey J: 2636 trials in the file; maze conditions 0..108 (109 values, 203 trials with condition 0)
   condition mod 3 = 0: 36 conditions, targets [np.uint8(3)], barriers [np.uint8(6), np.uint8(7), np.uint8(8), np.uint8(9)], trial_version [np.uint8(2)]
   condition mod 3 = 1: 36 conditions, targets [np.uint8(1)], barriers [np.uint8(0)], trial_version [np.uint8(0)]
   condition mod 3 = 2: 36 conditions, targets [np.uint8(1)], barriers [np.uint8(6), np.uint8(7), np.uint8(8), np.uint8(9)], trial_version [np.uint8(1)]
   successful trials of the 72 conditions: 1595; with delay > 400 ms: 1381; discard_trial set: 0; windows past the trial end dropped: 0
   trials per condition 17..29 (median 22)
   delay range -4..998 ms; offline minus online movement onset, median -25 ms
   hand displacement at +850 ms (mm, start-subtracted): |x| up to 136, |y| up to 89; peak speed of the condition means 1043 mm/s
Traceback (most recent call last):
  File "/tmp/claude-1001/dev_nb1.py", line 48, in <module>
    d = DS[f"M1-{m}"]
        ~~^^^^^^^^^^^
KeyError: 'M1-N'
Fri Nov 27 22:27:31 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb1.py').read()
s=s.replace('NAMES = ldr.DATASETS\n','NAMES = ldr.DATASETS\nMONKEYS = sorted({n.split("-")[1] for n in NAMES})\n',1)
s=s.replace('for m in ("J", "N"):','for m in MONKEYS:')
open('nb1.py','w').write(s)
EOF
cat > mkdev.py <<'EOF'
import sys
s=open(sys.argv[1]).read()
d=s.replace('DS = ldr.build("all")','import pickle\nDS = pickle.load(open("/tmp/claude-1001/DSJ.pkl","rb")) if __import__("os").path.exists("/tmp/claude-1001/DSJ.pkl") else ldr.build("all", monkeys=("J",))\npickle.dump(DS, open("/tmp/claude-1001/DSJ.pkl","wb"), protocol=4)')
d=d.replace('NAMES = ldr.DATASETS\n','NAMES = ["M1-J","PMd-J"]\n')
d=d.replace('folds=100)','folds=10)').replace('100, ratio)','10, ratio)').replace(', 500)',', 20)').replace(', 50)',', 5)').replace(', 100)\n        aucs',', 10)\n        aucs').replace('"), 100) for n','"), 5) for n').replace('lds_cv(DS[n], ldr.rng("fig2c-condition-lds-variance", k), 20, 0.5)','lds_cv(DS[n], ldr.rng("fig2c-condition-lds-variance", k), 3, 0.5)')
d=d.replace('for k in SEED_OFFSETS:\n        Xs','for k in SEED_OFFSETS[:2]:\n        Xs').replace('for k in (SEED_OFFSETS if mode','for k in (SEED_OFFSETS[:2] if mode')
d=d.replace('for c in range(72)])\n        SEA','for c in range(3)])\n        SEA')
d=d.replace('for a in sorted(r, key=lambda a: a["path"]):','for a in sorted(r, key=lambda a: a["path"])[:2]:')
skip=sys.argv[2] if len(sys.argv)>2 else None
d='import matplotlib; matplotlib.use("Agg")\n'+d
open(sys.argv[1].replace('nb','dev_nb'),'w').write(d)
EOF
python3 mkdev.py nb1.py && . env/bin/activate && cd entries/sabatini-2024 && PYTHONPATH=. timeout 3000 python $TMPDIR/dev_nb1.py 2>&1 | tail -120; date -u
```

```
loaded in 1 s, peak memory 1.2 GB
monkey J: 2636 trials in the file; maze conditions 0..108 (109 values, 203 trials with condition 0)
   condition mod 3 = 0: 36 conditions, targets [np.uint8(3)], barriers [np.uint8(6), np.uint8(7), np.uint8(8), np.uint8(9)], trial_version [np.uint8(2)]
   condition mod 3 = 1: 36 conditions, targets [np.uint8(1)], barriers [np.uint8(0)], trial_version [np.uint8(0)]
   condition mod 3 = 2: 36 conditions, targets [np.uint8(1)], barriers [np.uint8(6), np.uint8(7), np.uint8(8), np.uint8(9)], trial_version [np.uint8(1)]
   successful trials of the 72 conditions: 1595; with delay > 400 ms: 1381; discard_trial set: 0; windows past the trial end dropped: 0
   trials per condition 17..29 (median 22)
   delay range -4..998 ms; offline minus online movement onset, median -25 ms
   hand displacement at +850 ms (mm, start-subtracted): |x| up to 136, |y| up to 89; peak speed of the condition means 1043 mm/s
M1-J: 96 units (threshold-crossing channels), mean rate 19.0..86.2 spikes/s, trials 1595, conditions 72
PMd-J: 96 units (threshold-crossing channels), mean rate 17.3..191.5 spikes/s, trials 1595, conditions 72
M1-J: hand speed peak 120 ms after onset (range 70..280); 8-way direction decoding: 0..300 ms 0.80, -355..-55 ms 0.61, shuffled labels 0.20 (chance 0.125)
PMd-J: hand speed peak 120 ms after onset (range 70..280); 8-way direction decoding: 0..300 ms 0.88, -355..-55 ms 0.78, shuffled labels 0.21 (chance 0.125)
                        path  trials  first_go  units  spikes_unit0  spikes_total  conds
sub-Jenkins_ses-20090912_beh    1588   66.3163    192        129133      44869604     28
sub-Jenkins_ses-20090916_beh    2265   10.4990    192        474959      61693399     28
sessions sharing trial and spike counts: 0
Threshold crossings on each electrode, not sorted (Blackrock unit code 0), one unit per electrode. Spike times were saved for each trial only, so obs_intervals are the trials.
units: 192 | columns: ['spike_times', 'obs_intervals'
[... 26 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb1.py').read()
s=s.replace("out[c] = 10 * (fast[-1] + 1 - 35)   # code: 10*(fastInds(end)-36), 1-based on diff","out[c] = 10 * (fast[-1] + 1 - 36)   # code: 10*(fastInds(end)-36), 1-based index into diff")
s=s.replace('''print("M1-N unwarped within -0.286..-0.234 and p < 0.05:",
      -0.286 <= WARP['M1-N']['r0'][0] <= -0.234 and WARP['M1-N']['r0'][1] < 0.05)''','''if "M1-N" in WARP:
    print("M1-N unwarped within -0.286..-0.234 and p < 0.05:",
          -0.286 <= WARP['M1-N']['r0'][0] <= -0.234 and WARP['M1-N']['r0'][1] < 0.05)''')
s=s.replace("pre = c[:, :, 0:300].sum(2)             # -355 to -55 ms (delay period, target shown)","pre = c[:, :, 0:300].sum(2)             # -355 to -55 ms (delay period: target shown, preparatory activity)")
s=s.replace("# appears (labels as given, windows aligned on the trial table's movement onset).","# appears; the window before onset is in the delay period, when the target is already shown, so the\n# shuffled labels are the null.")
s=s.replace("reach direction can be decoded from spikes after onset but not from a window well before the target\n","reach direction can be decoded from spikes after onset and not with shuffled labels. The\n")
open('nb1.py','w').write(s)
EOF
grep -n "shuffled labels are the null" -B3 nb1.py | head; python3 mkdev.py nb1.py; sed -i 's/^for n in NAMES:\n    d = DS\[n\]\n    sp = np.linalg/&/' dev_nb1.py; . env/bin/activate && cd entries/sabatini-2024 && PYTHONPATH=. timeout 3000 python $TMPDIR/dev_nb1.py 2>&1 | sed -n '/durations/,$p' | tail -100; date -u
```

```
76-# Clock check. Hand speed in the condition means peaks after the trial table's movement onset, and the
77-# reach direction can be decoded from spikes after onset and not with shuffled labels. The
78-# appears; the window before onset is in the delay period, when the target is already shown, so the
79:# shuffled labels are the null.
M1-J: durations 170..600 ms (mean 338); unwarped rho = -0.183 (p = 0.124); warped (truncate) rho = -0.508 (p = 5.13e-06), five seeds [-0.508 -0.51 ]; warped (250 ms) rho = -0.773 (p = 1.79e-15)
PMd-J: durations 170..600 ms (mean 338); unwarped rho = -0.104 (p = 0.386); warped (truncate) rho = -0.060 (p = 0.618), five seeds [-0.06  -0.058]; warped (250 ms) rho = -0.761 (p = 8.69e-15)
other unwarped in -0.198..0.231: [np.True_, np.True_]
warped in -0.693..-0.468 with p < 0.001: [np.True_, np.False_]
         all_skew  all_best  straight_skew  straight_best  curved_skew  curved_best  signrank_p  straight_cond_median  curved_cond_median
dataset                                                                                                                                  
M1-J        0.777     0.831          0.836          0.882        0.713        0.770       0.000                 0.735               0.594
PMd-J       0.544     0.583          0.752          0.824        0.526        0.593       0.441                 0.126              -0.006
reading skew: all in 0.576..0.803 1/4, straight in 0.657..0.968 2/4, curved in 0.504..0.77 2/4; straight > curved 2/4
reading best: all in 0.576..0.803 1/4, straight in 0.657..0.968 2/4, curved in 0.504..0.77 2/4; straight > curved 2/4
M1-J: 2 plane(s); variance in the planes (code: reconstruction without the mean against the activity) mean 9.1% (s.d. 5.3); in 6.3..13.2%: True; variant with the mean added back 80.5%
PMd-J: 1 plane(s); variance in the planes (code: reconstruction without the mean against the activity) mean 10.6% (s.d. 7.5); in 6.3..13.2%: True; variant with the mean added back 73.3%
d
[... 43 more lines not kept]
```

**Agent calls Bash**

```bash
cat >> entries/sabatini-2024/ldr.py <<'EOF'


def lds_batch(X, ks):
    """lds_fit/lds_eigs for all conditions at once (X: C x N x T): the least-squares
    dynamics A, the subspace U of A X from bin 20 on, and for each k the
    eigenvalues (capped) and the simulation from bin 20 (NaN before)."""
    W = X[:, :, T0:]
    A = X[:, :, T0 + 1:] @ np.linalg.pinv(X[:, :, T0:-1])
    U = np.linalg.svd(A @ W, full_matrices=False)[0]
    out = {}
    for k in ks:
        Uk = U[:, :, :k]
        Ak = np.transpose(Uk, (0, 2, 1)) @ A @ Uk
        w, V = np.linalg.eig(Ak)
        wc = bio_eigs(w.ravel()).reshape(w.shape)
        capped = np.any(wc != w, axis=1)
        if capped.any():
            Ak = Ak.copy()
            for c in np.where(capped)[0]:
                Ak[c] = np.real(V[c] @ np.diag(wc[c]) @ np.linalg.inv(V[c]))
        z = np.einsum("cnk,cnm,cm->ck", Uk, A, W[:, :, 0])
        sim = np.full(X.shape, np.nan)
        sim[:, :, T0] = W[:, :, 0]
        for t in range(T0 + 1, X.shape[2]):
            sim[:, :, t] = np.einsum("cnk,ck->cn", Uk, z)
            z = np.einsum("cij,cj->ci", Ak, z)
        out[k] = (np.stack([sort_eigs(e) for e in wc]), sim)
    return out


def lds_eigs_batch(X, k):
    W = X[:, :, T0:]
    A = X[:, :, T0 + 1:] @ np.linalg.pinv(X[:, :, T0:-1])
    U = np.linalg.svd(A @ W, full_matrices=False)[0][:, :, :k]
    w = np.linalg.eigvals(np.transpose(U, (0, 2, 1)) @ A @ U)
    w = bio_eigs(w.ravel()).reshape(w.shape)
    return np.stack([sort_eigs(e) for e in w])
EOF
cd $TMPDIR && . env/bin/activate && PYTHONPATH=entries/sabatini-2024 python -c "
import pickle,time,numpy as np,ldr
DS=pickle.load(open('DSJ.pkl','rb')); X=DS['M1-J']['X']
T=time.time(); o=ldr.lds_batch(X,[5,7]); print(time.time()-T)
w,s=ldr.lds_fit(X[3],7); print(np.allclose(ldr.sort_eigs(w),o[7][0][3]), np.nanmax(abs(s-o[7][1][3])))
T=time.time(); e=ldr.lds_eigs_batch(X,5); print('eigs',time.time()-T, np.allclose(e[3], ldr.sort_eigs(ldr.lds_eigs(X[3],5))))
T=time.time(); ldr.cond_average(DS['M1-J']['Xt'][:800],DS['M1-J']['cond'][:800]); print('avg',time.time()-T)
"
```

```
0.25759005546569824
True 0.0001220703125
eigs 0.21755194664001465 True
avg 0.0062520503997802734
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR/LDR-public-b65f28d; for f in corrTotalRotationsWithjPCA getCorrTotalRotationsWithjPCA; do p=$(find . -name "$f.m"|head -1); echo "=== $p"; grep -v '^\s*%' $p | grep -v '^\s*$'; done; python3 -c "import sys;print(sys.version)"; . $TMPDIR/env/bin/activate; python -c "import sys;print(sys.version)"; nproc
```

```
=== ./reconciliation/jPCAReconciliation/corrTotalRotationsWithjPCA.m
function [corrCoeffs,pVals,jPCAVar,loadingsVar] ...
    = corrTotalRotationsWithjPCA(loadings,basisFxns,params,rotations)
loadingsVar = zeros(size(loadings,2),1);
jPCAVar = zeros(size(loadings,2),size(rotations(1).matrix,1)/2);
inds = find(params(:,1) > 0);
temporalIndices = find(~isnan(basisFxns(:,1)));
meanL = 0;
for cond = 1:size(loadings,2)
    meanL = meanL + loadings(cond).matrix/size(loadings,2);
end
for cond = 1:size(loadings,2)
    loadingsVar(cond) = sum(nanvar(rotations(cond).softNorms.'.* ...
        ((loadings(cond).matrix(:,inds)-meanL(:,inds)) ...
        *basisFxns(temporalIndices,inds).'),0,2));
    for plane = 1:size(rotations(1).matrix,1)/2
        jPCAVar(cond,plane) = sum(nanvar( ...
            rotations(cond).matrix([1:2]+(plane-1)*2,:),0,2));
    end
end
[... 23 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb1.py').read()
# pool
s=s.replace('''print("loaded in %.0f s, peak memory %.1f GB"''','''import multiprocessing as mp
def pmap(fn, args, procs=4):
    """Run fn over args in forked worker processes (they share the loaded data)."""
    with mp.get_context("fork").Pool(procs) as p:
        return p.starmap(fn, args)
print("loaded in %.0f s, peak memory %.1f GB"''')
# TBF CV
s=s.replace('''CV = {}
for n in NAMES:
    d = DS[n]
    res = [ldr.cv_tbf_k(d["Xt"], d["cond"], ldr.rng("fig3g-basis-frequencies", k), folds=100)
           for k in SEED_OFFSETS]
    CV[n] = res[0]''','''def tbf_cv_job(n, k):
    return ldr.cv_tbf_k(DS[n]["Xt"], DS[n]["cond"], ldr.rng("fig3g-basis-frequencies", k), folds=100)
jobs = [(n, k) for n in NAMES for k in SEED_OFFSETS]
CVALL = dict(zip(jobs, pmap(tbf_cv_job, jobs)))
CV = {}
for n in NAMES:
    res = [CVALL[(n, k)] for k in SEED_OFFSETS]
    CV[n] = res[0]''')
# shuffle
old=s[s.index('SHUF = {}\nfor n in NAMES:'):s.index('# %% tags=["claim:tbf-shuffle-control"]')]
new='''def shuffle_job(n, k):
    Xs = scrambled_average(DS[n], ldr.rng("tbf-shuffle-control", k))
    Bs, Ls = ldr.get_basis(Xs, K[n])
    return ldr.var_explained(Xs, Ls @ Bs.T), recoverability(Xs, Ls, Bs)

jobs = [(n, k) for n in NAMES for k in SEED_OFFSETS]
SHOUT = dict(zip(jobs, pmap(shuffle_job, jobs)))
SHUF = {}
for n in NAMES:
    X = DS[n]["X"]
    Br, Lr = ldr.get_basis(X, K[n])
    rows = [SHOUT[(n, k)] for k in SEED_OFFSETS]
    SHUF[n] = dict(real_ve=ldr.var_explained(X, Lr @ Br.T), real_rec=recoverability(X, Lr, Br),
                   ve=rows[0][0], rec=rows[0][1],
                   ve_seeds=[r[0].mean() for r in rows], rec_seeds=[r[1].mean() for r in rows])

'''
s=s.replace(old,new)
old=s[s.index('WARP = {}\nfor n in NAMES:'):s.index('# %% tags=["claim:fig3i-duration-warping"]')]
new='''def warp_job(n, k, mode):
    d = DS[n]
    dur = durations(d)
    Xw = warped_average(d, dur, ldr.rng("fig3i-duration-warping", k), mode)
    Bw, Lw = ldr.get_basis(Xw, K[n])
    return stats.pearsonr(abs(dur - dur.mean()), recoverability(Xw, Lw, Bw))

jobs = [(n, k, "truncate") for n in NAMES for k in SEED_OFFSETS] + [(n, 0, "250") for n in NAMES]
WOUT = dict(zip(jobs, pmap(warp_job, jobs)))
WARP = {}
for n in NAMES:
    dur = durations(DS[n])
    r0 = stats.pearsonr(abs(dur - dur.mean()), SHUF[n]["real_rec"])
    WARP[n] = dict(dur=dur, r0=r0, res={"truncate": [WOUT[(n, k, "truncate")] for k in SEED_OFFSETS],
                                        "250": [WOUT[(n, 0, "250")]]})

'''
s=s.replace(old,new)
# LDS CV
old=s[s.index('KS = np.arange(1, 22, 2)\ndef lds_cv'):s.index('# %% tags=["claim:fig2c-condition-lds-variance"]')]
new='''KS = np.arange(1, 22, 2)
def lds_cv(n, seed_k, folds=100, ratio=0.5):
    d = DS[n]
    g = ldr.rng("fig2c-condition-lds-variance", seed_k)
    proj = np.zeros((len(KS), folds, 72)); sim = np.zeros((len(KS), folds, 72))
    for f in range(folds):
        a = ldr.split_halves(d["cond"], g, ratio)
        Xa = ldr.cond_average(d["Xt"][a], d["cond"][a]); Xb = ldr.cond_average(d["Xt"][~a], d["cond"][~a])
        W, Yb = Xa[:, :, ldr.T0:], Xb[:, :, ldr.T0:]
        den = Yb.var(2, ddof=1).sum(1)
        Up = np.linalg.svd(W, full_matrices=False)[0]
        o = ldr.lds_batch(Xa, KS)
        for i, k in enumerate(KS):
            P = Up[:, :, :k]
            rec = P @ (np.transpose(P, (0, 2, 1)) @ W)
            proj[i, f] = np.clip(1 - (Yb - rec).var(2, ddof=1).sum(1) / den, 0, None)
            sm_ = o[k][1][:, :, ldr.T0:]
            sim[i, f] = np.clip(1 - (Yb - sm_).var(2, ddof=1).sum(1) / den, 0, None)
    return proj.mean((1, 2)), sim.mean((1, 2))

T = time.time()
jobs = [(n, 0, 100, 0.5) for n in NAMES] + [(n, 1, 100, 0.75) for n in NAMES] + \\
       [(n, k, 20, 0.5) for n in NAMES for k in SEED_OFFSETS[1:]]
LOUT = dict(zip(jobs, pmap(lds_cv, jobs)))
LCV = {n: {0.5: LOUT[(n, 0, 100, 0.5)], 0.75: LOUT[(n, 1, 100, 0.75)]} for n in NAMES}
print(f"cross-validation in {time.time() - T:.0f} s")

'''
s=s.replace(old,new)
s=s.replace('''        proj, sim = LCV[n][ratio]
        kp, ks = KS[proj.mean((1, 2)).argmax()], KS[sim.mean((1, 2)).argmax()]
        line.append(f"split {ratio}: projection k={kp} (curve {np.round(proj.mean((1, 2))[:6], 3)}), "
                    f"LDS k={ks} (curve {np.round(sim.mean((1, 2))[:6], 3)})")''','''        proj, sim = LCV[n][ratio]
        kp, ks = KS[proj.argmax()], KS[sim.argmax()]
        line.append(f"split {ratio}: projection k={kp} (curve {np.round(proj[:6], 3)}), "
                    f"LDS k={ks} (curve {np.round(sim[:6], 3)})")''')
s=s.replace('''    for kk in sorted(set([KLDS[n]["proj"], KLDS[n]["sim"], 5, 7, 9])):
        ve = np.array([ldr.var_explained(X[c:c + 1], ldr.lds_fit(X[c], kk)[1][None])[0] for c in range(72)])''','''    ks_ = sorted(set([KLDS[n]["proj"], KLDS[n]["sim"], 5, 7, 9]))
    fits = ldr.lds_batch(X, ks_)
    for kk in ks_:
        ve = ldr.var_explained(X, fits[kk][1])''')
old=s[s.index('''# %% [markdown]
# Seed check: the chosen k under the five seeds'''):s.index('''# %% [markdown]
# ## fig3a-eigenvalue-clusters''')]
new='''# %% [markdown]
# Seed check: the chosen k under the other four seeds, with 20 folds each for time (the claim's own seed above
# uses the full 100).

# %%
for n in NAMES:
    print(n, "k (projection, LDS) under seeds +1000..+4000, 20 folds:",
          [(int(KS[LOUT[(n, k, 20, 0.5)][0].argmax()]), int(KS[LOUT[(n, k, 20, 0.5)][1].argmax()])) for k in SEED_OFFSETS[1:]])

'''
s=s.replace(old,new)
s=s.replace('''        E = np.stack([ldr.sort_eigs(ldr.lds_eigs(X[c], kk)) for c in range(72)])''','''        E = ldr.lds_eigs_batch(X, kk)''')
# fig3c
old=s[s.index('def null_halves(d, kk, g, reps):'):s.index('# %% tags=["claim:fig3c-eigenvalue-distance-auc"]')]
new='''def null_halves(n, kk, k, reps):
    d = DS[n]
    g = ldr.rng("fig3c-eigenvalue-distance-auc", k)
    out = np.zeros((2, 72, reps, kk), complex)
    for r in range(reps):
        a = ldr.split_halves(d["cond"], g, 0.5)
        out[0, :, r] = ldr.lds_eigs_batch(ldr.cond_average(d["Xt"][a], d["cond"][a]), kk)
        out[1, :, r] = ldr.lds_eigs_batch(ldr.cond_average(d["Xt"][~a], d["cond"][~a]), kk)
    return out

def smooth_matrix():
    """The code's smoothing and down-sampling as a 1201 x 121 matrix."""
    e = np.zeros((1201, 1210), np.float32)
    e[np.arange(1201), 5 + np.arange(1201)] = 1
    return ldr.smooth(e / 1000)

def null_poisson(n, kk, k, reps, ntr=20):
    """Two sets of ntr Poisson trials per condition from its rates (linear interpolation of the 10 ms
    average to 1 ms, code generateTrials.m), smoothed and averaged; the mean of ntr trials is drawn as one
    Poisson count with ntr times the rate, divided by ntr."""
    g = ldr.rng("fig3c-eigenvalue-distance-auc", k)
    KERN = smooth_matrix()
    X = DS[n]["X"]
    tt = np.arange(-350, 851)
    lam = np.stack([[np.interp(tt, ldr.TIMES, x) for x in Xc] for Xc in X]) / 1000 * ntr
    lam = np.clip(lam, 0, None)
    out = np.zeros((2, 72, reps, kk), complex)
    for r in range(reps):
        for h in range(2):
            xa = (g.poisson(lam).astype(np.float32) / ntr) @ KERN
            out[h, :, r] = ldr.lds_eigs_batch(xa.astype(float), kk)
    return out

T = time.time()
jobs_b = [(n, KLDS[n]["proj"], 0, 500) for n in NAMES]
jobs_a = [(n, KLDS[n]["proj"], 1, 100) for n in NAMES]
jobs_s = [(n, KLDS[n]["proj"], k, 100) for n in NAMES for k in SEED_OFFSETS[1:]]
NB = dict(zip([j[0] for j in jobs_b], pmap(null_halves, jobs_b)))
NA = dict(zip([j[0] for j in jobs_a], pmap(null_poisson, jobs_a)))
NS = dict(zip([(j[0], j[2]) for j in jobs_s], pmap(null_halves, jobs_s)))
F3C = {}
for n in NAMES:
    E = EIG[(n, "proj")]
    obs = {kind: np.array([eig_dist(E[i], E[j], kind) for i in range(72) for j in range(72) if i != j]) for kind in ("mean", "norm")}
    F3C[n] = dict(obs=obs, nb=NB[n], na=NA[n], k=KLDS[n]["proj"])
print(f"nulls in {time.time() - T:.0f} s")

'''
s=s.replace(old,new)
old=s[s.index('''# %% [markdown]
# Seed check for the halves null'''):s.index('''# %% [markdown]
# ## suppfig2''')]
new='''# %% [markdown]
# Seed check for the halves null with the mean distance (100 repeats for each of the other four seeds, for time).

# %%
for n in NAMES:
    print(n, "AUC under seeds +1000..+4000 (100 repeats):",
          np.round([ldr.auc_folded(F3C[n]["obs"]["mean"], eig_dist(NS[(n, k)][0], NS[(n, k)][1], "mean").ravel())[0]
                    for k in SEED_OFFSETS[1:]], 3))

'''
s=s.replace(old,new)
s=s.replace('''(code compareTrialSimilarity.m); (a) two sets of 20 Poisson
# trials from each condition's rates, smoothed and averaged, run with 50 repeats per condition (the Methods' 500 did not fit the time; see the notes).''','''(code compareTrialSimilarity.m); (a) two sets of 20 Poisson
# trials from each condition's rates, smoothed and averaged, run with 100 repeats per condition (the
# Methods' 500 did not fit the time).''')
# geometry: noise loadings seeds and SEA in pool
s=s.replace('''GEO = {}
T = time.time()
for n in NAMES:
    tb = TBF[n]
    gr = ldr.groups(tb)
    L1, L2 = noise_loadings(DS[n], tb, ldr.rng("fig4b-plane-alignment"), 36)''','''GEO = {}
T = time.time()
NOISE = dict(zip([(n, k) for n in NAMES for k in SEED_OFFSETS],
                 pmap(lambda n, k: noise_loadings(DS[n], TBF[n], ldr.rng("fig4b-plane-alignment", k), 36),
                      [(n, k) for n in NAMES for k in SEED_OFFSETS]) if False else
                 [noise_loadings(DS[n], TBF[n], ldr.rng("fig4b-plane-alignment", k), 36) for n in NAMES for k in SEED_OFFSETS]))
for n in NAMES:
    tb = TBF[n]
    gr = ldr.groups(tb)
    L1, L2 = NOISE[(n, 0)]''')
s=s.replace('''        A1, A2 = noise_loadings(DS[n], tb, ldr.rng("fig4b-plane-alignment", k), 36)''','''        A1, A2 = NOISE[(n, k)]''')
old=s[s.index('T = time.time()\nSEA = {}'):s.index('# %% tags=["claim:fig4c-subspace-excursion-angles"]')]
new='''def sea_job(n, gi):
    tb = TBF[n]
    f, inds = GEO[n]["groups"][gi]
    L1, L2 = GEO[n]["L1"], GEO[n]["L2"]
    data_sea = ldr.sea(tb["L"][:, :, inds], 25)
    noise = np.array([ldr.sea(np.concatenate([L1[:, c][:, :, inds], L2[:, c][:, :, inds]]), 25) for c in range(72)])
    return f, dict(data=data_sea, noise=noise, p=(noise > data_sea[None]).mean(0))

T = time.time()
jobs = [(n, gi) for n in NAMES for gi in range(len(GEO[n]["groups"]))]
SEA = {(j[0], r[0]): r[1] for j, r in zip(jobs, pmap(sea_job, jobs))}
print(f"SEA in {time.time() - T:.0f} s")

'''
s=s.replace(old,new)
s=s.replace('''SNR = {n: snr_dims(DS[n], K[n], ldr.rng("rotation-orientation-dimensionality"), 100) for n in NAMES}''','''def snr_job(n):
    return snr_dims(DS[n], K[n], ldr.rng("rotation-orientation-dimensionality"), 100)
SNR = dict(zip(NAMES, pmap(snr_job, [(n,) for n in NAMES])))''')
open('nb1.py','w').write(s)
EOF
grep -n "if False else" nb1.py
```

```
756:                      [(n, k) for n in NAMES for k in SEED_OFFSETS]) if False else
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb1.py').read()
s=s.replace('''NOISE = dict(zip([(n, k) for n in NAMES for k in SEED_OFFSETS],
                 pmap(lambda n, k: noise_loadings(DS[n], TBF[n], ldr.rng("fig4b-plane-alignment", k), 36),
                      [(n, k) for n in NAMES for k in SEED_OFFSETS]) if False else
                 [noise_loadings(DS[n], TBF[n], ldr.rng("fig4b-plane-alignment", k), 36) for n in NAMES for k in SEED_OFFSETS]))''','''NOISE = {(n, k): noise_loadings(DS[n], TBF[n], ldr.rng("fig4b-plane-alignment", k), 36)
         for n in NAMES for k in SEED_OFFSETS}''')
s=s.replace('''KB = {rd: ldr.kin_basis([DS["M1-J"]["kin"], DS["M1-N"]["kin"]], rd) for rd in ("svd", "skewnormal")}''','''KB = {rd: ldr.kin_basis([DS[f"M1-{m}"]["kin"] for m in MONKEYS], rd) for rd in ("svd", "skewnormal")}''')
open('nb1.py','w').write(s)
EOF
python3 mkdev.py nb1.py; sed -i 's/(n, 0, 100, 0.5) for n in NAMES\] + \[(n, 1, 100, 0.75)/(n, 0, 10, 0.5) for n in NAMES] + [(n, 1, 10, 0.75)/; s/LOUT\[(n, 0, 100, 0.5)\], 0.75: LOUT\[(n, 1, 100, 0.75)\]/LOUT[(n, 0, 10, 0.5)], 0.75: LOUT[(n, 1, 10, 0.75)]/; s/(n, k, 20, 0.5) for n in NAMES for k/(n, k, 3, 0.5) for n in NAMES for k/; s/LOUT\[(n, k, 20, 0.5)\]/LOUT[(n, k, 3, 0.5)]/g; s/(n, KLDS\[n\]\["proj"\], k, 100) for n/(n, KLDS[n]["proj"], k, 10) for n/; s/"proj"\], 1, 100) for n/"proj"], 1, 5) for n/; s/"proj"\], 0, 500) for n/"proj"], 0, 20) for n/; s/, 36)\n         for n/, 5)/' dev_nb1.py; sed -i 's/ldr.rng("fig4b-plane-alignment", k), 36)$/ldr.rng("fig4b-plane-alignment", k), 6)/' dev_nb1.py; sed -i 's/for r in range(36)\]/for r in range(6)]/g' dev_nb1.py; . env/bin/activate && cd entries/sabatini-2024 && PYTHONPATH=. timeout 3000 python $TMPDIR/dev_nb1.py 2>&1 | sed -n '/durations/,$p' | tail -100; date -u
```

```
Terminated                 PYTHONPATH=. timeout 3000 python $TMPDIR/dev_nb1.py 2>&1 | sed -n '/durations/,$p' | tail -100
Fri Nov 27 23:25:40 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb1.py').read()
s=s.replace('''import multiprocessing as mp
def pmap(fn, args, procs=4):
    """Run fn over args in forked worker processes (they share the loaded data)."""
    with mp.get_context("fork").Pool(procs) as p:
        return p.starmap(fn, args)
''','''def pmap(fn, args):
    t = time.time()
    out = [fn(*a) for a in args]
    print(f"[{fn.__name__}: {len(args)} jobs in {time.time() - t:.0f} s]")
    return out
''')
open('nb1.py','w').write(s)
EOF
python3 mkdev.py nb1.py; sed -i 's/(n, 0, 100, 0.5) for n in NAMES\] + \[(n, 1, 100, 0.75)/(n, 0, 10, 0.5) for n in NAMES] + [(n, 1, 10, 0.75)/; s/LOUT\[(n, 0, 100, 0.5)\], 0.75: LOUT\[(n, 1, 100, 0.75)\]/LOUT[(n, 0, 10, 0.5)], 0.75: LOUT[(n, 1, 10, 0.75)]/; s/(n, k, 20, 0.5) for n in NAMES for k/(n, k, 3, 0.5) for n in NAMES for k/; s/LOUT\[(n, k, 20, 0.5)\]/LOUT[(n, k, 3, 0.5)]/g; s/(n, KLDS\[n\]\["proj"\], k, 100) for n/(n, KLDS[n]["proj"], k, 10) for n/; s/"proj"\], 1, 100) for n/"proj"], 1, 5) for n/; s/"proj"\], 0, 500) for n/"proj"], 0, 20) for n/' dev_nb1.py; sed -i 's/ldr.rng("fig4b-plane-alignment", k), 36)$/ldr.rng("fig4b-plane-alignment", k), 6)/; s/for r in range(36)\]/for r in range(6)]/g' dev_nb1.py; grep -c "range(6)" dev_nb1.py; . env/bin/activate && cd entries/sabatini-2024 && PYTHONPATH=. timeout 900 python -u $TMPDIR/dev_nb1.py 2>&1 | grep -v "^  *\(M1\|PMd\)" | sed -n '/held-out/,$p' | tail -100; date -u
```

```
2
M1-J: held-out VE by k (claim seed) [0.386 0.519 0.655 0.69  0.721 0.728 0.735 0.733 0.729 0.724 0.719 0.713]
     best k 7 -> k = 7; k under the five seeds [7, 7, 7, 7, 7]
PMd-J: held-out VE by k (claim seed) [0.371 0.576 0.756 0.788 0.809 0.811 0.811 0.808 0.803 0.798 0.793 0.789]
     best k 7 -> k = 7; k under the five seeds [7, 7, 7, 7, 7]
M1-J: k=7; 3 rotation pairs at [0.73 2.01 3.38] Hz (half-lives [0.43 0.23 0.14] s), 1 real mode(s) at [0.] Hz; nearest of 0.5/1.5/2.5/4: [np.float64(0.5), np.float64(2.5), np.float64(4.0)]; within 10%: [np.False_, np.False_, np.False_]
PMd-J: k=7; 3 rotation pairs at [0.64 1.64 2.64] Hz (half-lives [0.33 0.15 0.11] s), 1 real mode(s) at [0.] Hz; nearest of 0.5/1.5/2.5/4: [np.float64(0.5), np.float64(1.5), np.float64(2.5)]; within 10%: [np.False_, np.True_, np.True_]
basis functions plotted are within -1..1: True
M1-J: (a) mean 92.3% (s.d. 1.3); (b) mean 92.5% (s.d. 1.3); in 81..100%: True, True
PMd-J: (a) mean 95.1% (s.d. 1.2); (b) mean 95.3% (s.d. 1.1); in 81..100%: True, True
[shuffle_job: 10 jobs in 72 s]
M1-J: real 92.5%, shuffled 35.1% (s.d. 1.7; five seeds [35.1 35.4 35.1 35.2 35.6]); in 31.5..50.6%: True; rank-sum p = 3.9e-25, signed-rank p = 1.7e-13
PMd-J: real 95.3%, shuffled 35.4% (s.d. 1.7; five seeds [35.4 35.5 35.  35.4 35.3]); in 31.5..50.6%: True; rank-sum p = 3.9e-25, signed-rank p = 1.7e-13
M1-J: recoverability 95.1% (s.d. 1.8; de-mixed basis -150..850: 95.9%), chance 86.2% (five seeds [86.2 85.8 85.9 85.6 86.1]); real in 81.9..100: True; chance in 56.7..88: True; rank-sum p = 6.7e-25, real higher: True
PMd-J: recoverability 95.8% (s.d. 1.2; de-mixed basis -150..850: 96.7%), chance 84.8% (five seeds [84.8 84.8 84.1 84.2 85. ]); real in 81.9..100: True; chance in 56.7..88: True; rank-sum p = 3.9e-25, real higher: True
[warp_job: 12 jobs in 101 s]
M1-J: durations 170..600 ms (mean 338); unwarped rho = -0.183 (p = 0.124); warped (truncate) rho = -0.508 (p = 5.13e-06), five seeds [-0.508 -0.51  -0.51  -0.51  -0
[... 81 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb1.py').read()
s=s.replace('''    return f, dict(data=data_sea, noise=noise, p=(noise > data_sea[None]).mean(0))''','''    m = min(noise.shape[1], len(data_sea))
    return f, dict(data=data_sea, noise=noise, p=(noise[:, :m] > data_sea[None, :m]).mean(0))''')
s=s.replace('''jobs = [(n, 0, 100, 0.5) for n in NAMES] + [(n, 1, 100, 0.75) for n in NAMES] + \\
       [(n, k, 20, 0.5) for n in NAMES for k in SEED_OFFSETS[1:]]
LOUT = dict(zip(jobs, pmap(lds_cv, jobs)))
LCV = {n: {0.5: LOUT[(n, 0, 100, 0.5)], 0.75: LOUT[(n, 1, 100, 0.75)]} for n in NAMES}''','''jobs = [(n, 0, 100, 0.5) for n in NAMES] + [(n, 1, 20, 0.75) for n in NAMES] + \\
       [(n, k, 10, 0.5) for n in NAMES for k in SEED_OFFSETS[1:]]
LOUT = dict(zip(jobs, pmap(lds_cv, jobs)))
LCV = {n: {0.5: LOUT[(n, 0, 100, 0.5)], 0.75: LOUT[(n, 1, 20, 0.75)]} for n in NAMES}''')
s=s.replace('LOUT[(n, k, 20, 0.5)]','LOUT[(n, k, 10, 0.5)]')
s=s.replace('''# Seed check: the chosen k under the other four seeds, with 20 folds each for time (the claim's own seed above
# uses the full 100).''','''# The code's 3/4 split above runs 20 folds, for time. Seed check: the chosen k under the other four seeds,
# with 10 folds each, for time (the claim's own seed above uses the full 100).''')
s=s.replace('"proj"], 0, 500) for n','"proj"], 0, 150) for n').replace('"proj"], 1, 100) for n','"proj"], 1, 30) for n').replace('(n, KLDS[n]["proj"], k, 100) for n','(n, KLDS[n]["proj"], k, 20) for n')
s=s.replace("(b) random halves of the real trials, 500 repeats (code\n# compareTrialSimilarity.m)","(b) random halves of the real trials, run with 150 repeats per condition (the Methods and the code\n# compareTrialSimilarity.m use 500)")
s=s.replace("run with 100 repeats per condition (the\n# Methods' 500 did not fit the time).","run with 30 repeats per condition (the\n# Methods' 500 did not fit the time).")
s=s.replace("# Seed check for the halves null with the mean distance (100 repeats for each of the other four seeds, for time).","# Seed check for the halves null with the mean distance (20 repeats for each of the other four seeds, for time).")
s=s.replace('''print(n, "AUC under seeds +1000..+4000 (100 repeats):",''','''print(n, "AUC under seeds +1000..+4000 (20 repeats):",''')
s=s.replace('''def tbf_cv_job(n, k):
    return ldr.cv_tbf_k(DS[n]["Xt"], DS[n]["cond"], ldr.rng("fig3g-basis-frequencies", k), folds=100)''','''def tbf_cv_job(n, k):
    # 100 folds under the claim's seed; 20 under the four others, for time
    return ldr.cv_tbf_k(DS[n]["Xt"], DS[n]["cond"], ldr.rng("fig3g-basis-frequencies", k), folds=100 if k == 0 else 20)''')
open('nb1.py','w').write(s)
EOF
grep -n "150) for n\|30) for n\|20) for n\|folds=100 if" nb1.py; cat > sea_test.py <<'EOF'
import pickle,time,numpy as np,ldr
DS=pickle.load(open('/tmp/claude-1001/DSJ.pkl','rb')); n='M1-J'; X=DS[n]['X']
tb=ldr.eig_transform(X,7); gr=ldr.groups(tb)
T=time.time(); s=ldr.sea(tb['L'][:,:,gr[1][1]],25); print('sea',time.time()-T, s.round(1))
T=time.time(); s=ldr.sea(tb['L'][:,:,gr[0][1]],25); print('sea loc',time.time()-T, s.round(1))
EOF
. env/bin/activate; PYTHONPATH=entries/sabatini-2024 timeout 300 python sea_test.py
```

```
165:    return ldr.cv_tbf_k(DS[n]["Xt"], DS[n]["cond"], ldr.rng("fig3g-basis-frequencies", k), folds=100 if k == 0 else 20)
643:jobs_b = [(n, KLDS[n]["proj"], 0, 150) for n in NAMES]
644:jobs_a = [(n, KLDS[n]["proj"], 1, 30) for n in NAMES]
645:jobs_s = [(n, KLDS[n]["proj"], k, 20) for n in NAMES for k in SEED_OFFSETS[1:]]
sea 0.16309380531311035 [89.8 63.2 57.4 52.2 51.1 47.  45.9 42.7 39.6 36.8 34.9 34.2 32.3 31.7
 30.  29.3 29.3 28.1 27.8 27.  26.3 25.7 25.3 24.1 23.2]
sea loc 0.11377453804016113 [15.4  9.3  7.4  7.1  6.3  5.2  5.2  4.9  4.5  4.3  4.2  4.1  3.9  3.9
  3.8  3.5  3.5  3.4  3.4  3.3  3.1  3.1  2.9  2.9  2.8]
Shell cwd was reset to
```

**Agent calls Write**

```json
{
 "file_path": "/tmp/claude-1001/nb2.py",
 "content": "# %% [markdown]\n# # Sabatini & Kaufman (2024) on DANDI:000070: prediction, encoding and decoding (notebook 2 of 2)\n#\n# Paper: doi:10.1038/s41467-024-51308-7; dataset DANDI:000070 version 0.261122.2046 (the most recent\n# published version; the paper cites none), sessions `sub-Jenkins_ses-20090918` and\n# `sub-Nitschke_ses-20100923` as named in the paper's Data availability statement. The claims file was written\n# from the version of record and its supplement. Notebook 1 holds the data check and the claims on the\n# factorization and dynamics; this one recomputes the factorization (the same cross-validation, seed and k)\n# and tests:\n#\n# | claim | here |\n# |---|---|\n# | fig5c-rotations-predict-rotations, fig6b-location-predicts-rotations, fig6c-location-tracks-direction, fig6e-kinematics-predict-location, fig7c-ldr-encoding, suppfig7a-not-memorization, fig7c-standard-encoding-worse, fig7f-ldr-decoding, trial-curvature-decoding, suppfig8-no-output-potent-dependence | tested |\n# | fig7f-decoder-beats-standard | blocked, too large (see its section) |\n\n# %%\nimport time, resource, warnings\nimport numpy as np\nimport pandas as pd\nfrom scipy import stats\nfrom scipy.ndimage import gaussian_filter1d\nimport matplotlib.pyplot as plt\nimport ldr\nwarnings.filterwarnings(\"ignore\", category=RuntimeWarning)\nnp.set_printoptions(precision=3, suppress=True, linewidth=150)\nT_START = time.time()\nSEED_OFFSETS = [0, 1000, 2000, 3000, 4000]\nDS = ldr.build(\"all\")\nNAMES = ldr.DATASETS\nMONKEYS = sorted({n.split(\"-\")[1] for n in NAMES})\nfor n in NAMES:\n    DS[n][\"bc\"] = ldr.binned_counts(DS[n][\"counts\"])   # 10 ms counts, spikes/s, for single-trial decoding\n    del DS[n][\"counts\"]\nK = {n: ldr.cv_tbf_k(DS[n][\"Xt\"], DS[n][\"cond\"], ldr.rng(\"fig3g-basis-frequencies\"), folds=100)[\"k\"] for n in NAMES}\nTBF = {n: ldr.eig_transform(DS[n][\"X\"], K[n]) for n in NAMES}\nKB = {rd: ldr.kin_basis([DS[f\"M1-{m}\"][\"kin\"] for m in MONKEYS], rd) for rd in (\"svd\", \"skewnormal\")}\nPARAMS = {(n, rd): ldr.reach_params(KB[rd][0], DS[n][\"kin\"]) for n in NAMES for rd in KB}\nprint(\"k per dataset:\", K)\nprint(\"loaded in %.0f s, peak memory %.1f GB\" % (time.time() - T_START, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6))\n\n# %% tags=[\"sanity\"]\n# The kinematic basis functions: the top two velocity singular vectors over all conditions of both monkeys\n# (reading svd) and their skew-normal fits (reading skewnormal).\nt = ldr.TIMES\nfig, ax = plt.subplots(1, 2, figsize=(10, 2.6))\nfor rd in KB:\n    ax[0].plot(t, KB[rd][1]); ax[1].plot(t, KB[rd][0])\nax[0].set_title(\"velocity basis\"); ax[1].set_title(\"position basis\"); plt.show()\nraw = KB[\"svd\"][2][\"raw\"]\nfit = KB[\"skewnormal\"][1]\nfor i in range(2):\n    r2 = 1 - ((raw[:, i] - fit[:, i]) ** 2).sum() / ((raw[:, i] - raw[:, i].mean()) ** 2).sum()\n    print(f\"velocity singular vector {i + 1}: peak at {t[np.argmax(abs(raw[:, i]))]} ms; skew-normal fit R2 {r2:.3f}\")\nfor n in (\"M1-J\", \"M1-N\"):\n    P = PARAMS[(n, \"svd\")]\n    path = ldr.params_to_path(KB[\"svd\"][0], P)\n    ve = 1 - ((path - DS[n][\"kin\"]) ** 2).sum((1, 2)) / ((DS[n][\"kin\"] - DS[n][\"kin\"].mean(1, keepdims=True)) ** 2).sum((1, 2))\n    print(f\"{n[-1]}: reach parameters ranges {np.round(P.min(0), 1)}..{np.round(P.max(0), 1)}; the two basis functions \"\n          f\"explain {ve.mean()*100:.1f}% of the condition-mean hand path (min {ve.min()*100:.1f}%)\")\n\n# %%\ndef ve_rows(X, Xh):\n    return ldr.var_explained(X, Xh)\n\ndef ridge_code(Xf, Y, lam):\n    \"\"\"Code style ridge: a row of ones appended to the predictors and penalised with them;\n    Xf: (n, p), Y: (n, q); returns a predictor.\"\"\"\n    Z = np.c_[Xf, np.ones(len(Xf))]\n    W = np.linalg.solve(Z.T @ Z + lam * np.eye(Z.shape[1]), Z.T @ Y)\n    return lambda A: np.c_[A, np.ones(len(A))] @ W\n\ndef pinv_sym(K):\n    \"\"\"Pseudo-inverse of a symmetric matrix with MATLAB's default tolerance (max(size) * eps(norm)).\"\"\"\n    w, V = np.linalg.eigh(K)\n    tol = max(K.shape) * np.spacing(np.abs(w).max())\n    inv = np.where(np.abs(w) > tol, 1 / np.where(w == 0, 1, w), 0)\n    return (V * inv) @ V.T\n\ndef kernel_map(Xtr, Ytr, kern, lam):\n    \"\"\"Code style kernel regression (no centring): Y = Ytr' pinv(K + lam I) k(x).\"\"\"\n    Kt = kern(Xtr, Xtr)\n    A = pinv_sym(Kt + lam * np.eye(len(Kt))) @ Ytr\n    return lambda Z: kern(Z, Xtr) @ A\n\nOU = lambda ls: (lambda A, B: np.exp(-np.sqrt(np.maximum(((A[:, None] - B[None]) ** 2).sum(-1), 0)) / ls))\nGAUSS = lambda ls: (lambda A, B: np.exp(-((A[:, None] - B[None]) ** 2).sum(-1) / ls ** 2))   # code: exp(-(d/ls)^2)\n\ndef six_folds(claim, k=0, n=72, nf=6):\n    return ldr.folds_over(n, nf, ldr.rng(claim, k))\n\ndef vec(L):\n    return L.reshape(len(L), -1)\n\n# %% [markdown]\n# ## fig5c-rotations-predict-rotations\n# > Each rotation's parameters on a condition predicted 43 to 94% of the variance of a different-frequency\n# > rotation, with one model for all conditions, above chance.\n#\n# Code predictOneComponentFromAnother.m: 6 folds over conditions; TBF on the training conditions; the\n# predictor's vectorised loading columns reduced to the left singular vectors holding 80% of the summed\n# singular values, with a row of ones; ridge (lambda 0.1); held-out loadings by projecting the held-out\n# condition on the training basis. Truth: the held-out condition's own predicted columns times the basis.\n# Null (code oneComponentToAnother.m): each component of a condition's activity taken from a random condition.\n\n# %%\ndef rot_predict(X, k, folds):\n    C = len(X)\n    out = {}\n    for te in folds:\n        tr = np.setdiff1d(np.arange(C), te)\n        tb = ldr.eig_transform(X[tr], k)\n        gr = ldr.groups(tb)\n        ok = ~np.isnan(tb[\"B\"][:, 0])\n        Lte = X[te] @ np.linalg.pinv(tb[\"raw\"].T)\n        for a, (fa, ia) in enumerate(gr):\n            Xp = vec(tb[\"L\"][:, :, ia])\n            U, S, _ = np.linalg.svd(Xp.T, full_matrices=False)\n            keep = int(np.argmax(np.cumsum(S) / S.sum() > 0.8)) + 1\n            sv = U[:, :keep]\n            for b, (fb, ib) in enumerate(gr):\n                if a == b:\n                    continue\n                Y = vec(tb[\"L\"][:, :, ib])\n                f = ridge_code(Xp @ sv, Y, 0.1)\n                pred = f(vec(Lte[:, :, ia]) @ sv).reshape(len(te), -1, len(ib))\n                Bq = tb[\"B\"][ok][:, ib]\n                truth = Lte[:, :, ib] @ Bq.T\n                ve = ldr.var_explained(truth, pred @ Bq.T)\n                o = out.setdefault((a, b), np.full(C, np.nan))\n                o[te] = ve\n    return out, [len(i) for f, i in ldr.groups(ldr.eig_transform(X, k))]\n\ndef null_components(n, g):\n    tb = TBF[n]\n    gr = ldr.groups(tb)\n    Xn = np.zeros_like(DS[n][\"X\"])\n    for c in range(72):\n        for f, ii in gr:\n            r = g.integers(72)\n            Xn[c] += tb[\"L\"][r][:, ii] @ tb[\"raw\"][:, ii].T\n    return Xn\n\nF5C = {}\nfor n in NAMES:\n    real, sizes = rot_predict(DS[n][\"X\"], K[n], six_folds(\"fig5c-rotations-predict-rotations\"))\n    null, _ = rot_predict(null_components(n, ldr.rng(\"fig5c-rotations-predict-rotations\", 1)), K[n],\n                          six_folds(\"fig5c-rotations-predict-rotations\", 2))\n    seeds = []\n    for k in SEED_OFFSETS[1:]:\n        rr, _ = rot_predict(DS[n][\"X\"], K[n], six_folds(\"fig5c-rotations-predict-rotations\", k))\n        seeds.append(np.mean([v.mean() for (a, b), v in rr.items() if sizes[a] == 2 and sizes[b] == 2]))\n    F5C[n] = dict(real=real, null=null, sizes=sizes, seeds=seeds)\n\n# %% tags=[\"claim:fig5c-rotations-predict-rotations\"]\nrows = []\nfor n in NAMES:\n    f = F5C[n]\n    for (a, b), v in f[\"real\"].items():\n        nv = f[\"null\"][(a, b)]\n        rows.append(dict(dataset=n, predictor=a, predicted=b, rotations=f[\"sizes\"][a] == 2 and f[\"sizes\"][b] == 2,\n                         mean=v.mean(), sd=v.std(ddof=1), null=nv.mean(), p_signrank=stats.wilcoxon(v, nv).pvalue,\n                         p_ranksum=stats.ranksums(v, nv).pvalue))\nF5 = pd.DataFrame(rows)\nprint(F5.round(4).to_string(index=False))\nR5 = F5[F5.rotations]\nprint(f\"rotation pairs: means {R5['mean'].min()*100:.1f}..{R5['mean'].max()*100:.1f}%; in 38.7..100: \"\n      f\"{R5['mean'].between(0.387, 1).sum()} of {len(R5)}; above null with signed-rank p < 0.001: \"\n      f\"{((R5['mean'] > R5['null']) & (R5.p_signrank < 0.001)).sum()} of {len(R5)} (rank-sum: \"\n      f\"{((R5['mean'] > R5['null']) & (R5.p_ranksum < 0.001)).sum()})\")\nfor n in NAMES:\n    print(f\"{n}: mean over rotation pairs under seeds +1000..+4000: {np.round(F5C[n]['seeds'], 3)}\")\n\n# %% [markdown]\n# ## fig6b-location-predicts-rotations\n# > The state space location linearly predicted the rotations' parameters, explaining on average 67 to 80%\n# > of the population variance, above chance.\n#\n# Methods: the offset column predicts the vectorised remaining columns by ridge regression (lambda 0.1), 6\n# folds over conditions, TBF refitted on the training folds; the observed offset column joined to the\n# prediction, times the basis, gives the predicted activity. The intercept is not in the Methods; the code's\n# appended row of ones is used. Variant (code offsetToRotations.m): 2 folds, lambda 0.01, the predictor\n# reduced to 90% of the summed singular values. Null (code): offsets and rotations from random conditions.\n\n# %%\ndef offset_predict(X, Xeval, k, folds, lam, energy=None):\n    C = len(X)\n    pred = np.full(Xeval.shape, np.nan)\n    for te in folds:\n        tr = np.setdiff1d(np.arange(C), te)\n        tb = ldr.eig_transform(X[tr], k)\n        off = [i for f, i in ldr.groups(tb) if len(i) == 1][0][0]\n        rest = [c for c in range(k) if c != off]\n        P = tb[\"L\"][:, :, off]\n        Lte = X[te] @ np.linalg.pinv(tb[\"raw\"].T)\n        if energy is not None:\n            U, S, _ = np.linalg.svd(P.T, full_matrices=False)\n            sv = U[:, :int(np.argmax(np.cumsum(S) / S.sum() > energy)) + 1]\n        else:\n            sv = np.eye(P.shape[1])\n        f = ridge_code(P @ sv, vec(tb[\"L\"][:, :, rest]), lam)\n        Lh = np.zeros_like(Lte)\n        Lh[:, :, off] = Lte[:, :, off]\n        Lh[:, :, rest] = f(Lte[:, :, off] @ sv).reshape(len(te), -1, len(rest))\n        pred[te] = Lh @ tb[\"B\"].T\n    return ldr.var_explained(Xeval, pred)\n\ndef fake_offsets(n, g):\n    tb = TBF[n]\n    off = [i for f, i in ldr.groups(tb) if len(i) == 1][0][0]\n    rest = [c for c in range(K[n]) if c != off]\n    Xf = np.zeros_like(DS[n][\"X\"])\n    for c in range(72):\n        L = np.zeros_like(tb[\"L\"][0])\n        L[:, off] = tb[\"L\"][g.integers(72)][:, off]\n        L[:, rest] = tb[\"L\"][g.integers(72)][:, rest]\n        Xf[c] = L @ tb[\"raw\"].T\n    return Xf\n\n# %% tags=[\"claim:fig6b-location-predicts-rotations\"]\nfor n in NAMES:\n    X = DS[n][\"X\"]\n    v = offset_predict(X, X, K[n], six_folds(\"fig6b-location-predicts-rotations\"), 0.1)\n    nv = offset_predict(fake_offsets(n, ldr.rng(\"fig6b-location-predicts-rotations\", 1)), X, K[n],\n                        six_folds(\"fig6b-location-predicts-rotations\", 2), 0.1)\n    vc = offset_predict(X, X, K[n], six_folds(\"fig6b-location-predicts-rotations\", 3, nf=2), 0.01, 0.9)\n    seeds = [offset_predict(X, X, K[n], six_folds(\"fig6b-location-predicts-rotations\", k), 0.1).mean() for k in SEED_OFFSETS[1:]]\n    print(f\"{n}: mean {v.mean()*100:.1f}% (s.d. {v.std(ddof=1)*100:.1f}); null {nv.mean()*100:.1f}%; signed-rank p = \"\n          f\"{stats.wilcoxon(v, nv).pvalue:.2g}; in 60.3..88: {0.603 <= v.mean() <= 0.88}; code variant (2 folds, \"\n          f\"lambda 0.01, SVD 90%) {vc.mean()*100:.1f}%; other seeds {np.round(np.array(seeds)*100, 1)}\")\n\n# %% [markdown]\n# ## fig6c-location-tracks-direction\n# > In a PCA of the state space locations across conditions, location related to the overall reach\n# > direction, from starting point to target, in a continuous manner.\n#\n# Target angle: the direction of the condition-mean hand displacement at +850 ms (code splitTrialsAngles.m\n# uses the last sample of the path). The sign of a PC is arbitrary, so the correlation is also given with the\n# PC 1-2 angle mirrored.\n\n# %% tags=[\"claim:fig6c-location-tracks-direction\"]\nfig, ax = plt.subplots(1, 4, figsize=(15, 3.4))\nfor a_, n in zip(ax, NAMES):\n    tb = TBF[n]\n    off = [i for f, i in ldr.groups(tb) if len(i) == 1][0][0]\n    L0 = tb[\"L\"][:, :, off]\n    Lc = L0 - L0.mean(0)\n    U, S, Vt = np.linalg.svd(Lc, full_matrices=False)\n    pcs = U[:, :2] * S[:2]\n    tang = np.arctan2(DS[n][\"kin\"][:, -1, 1], DS[n][\"kin\"][:, -1, 0])\n    pang = np.arctan2(pcs[:, 1], pcs[:, 0])\n    r1, p1 = ldr.circ_corr(tang, pang)\n    r2, p2 = ldr.circ_corr(tang, -pang)\n    frac = S[:2] ** 2 / (S ** 2).sum()\n    print(f\"{n}: PCs 1-2 hold {frac.sum()*100:.1f}% of the offset variance; circular correlation of target angle \"\n          f\"with PC angle {r1:.3f} (p = {p1:.2g}), mirrored {r2:.3f} (p = {p2:.2g}); best positive {max(r1, r2):.3f}, \"\n          f\"p = {[p1, p2][int(r2 > r1)]:.2g}\")\n    a_.scatter(pcs[:, 0], pcs[:, 1], c=tang, cmap=\"hsv\", s=14); a_.set_title(n); a_.set_xlabel(\"PC 1\"); a_.set_ylabel(\"PC 2\")\nplt.tight_layout(); plt.show()\n\n# %% [markdown]\n# ## fig6e-kinematics-predict-location\n# > Four reach parameters linearly predicted 37 to 71% of the variance in state space location, and kernel\n# > regression 69 to 81%, both above chance.\n#\n# The offset columns of the factorization of all 72 conditions are the targets; the reach parameters (both\n# kinematic readings) the predictors; 6 folds over conditions; ridge (lambda 0.1) with intercept; kernels\n# (a) Ornstein-Uhlenbeck, length scale 10^3, no penalty (the LDR encoder's) and (b) Gaussian, length scale 400,\n# lambda 0.1. Variance explained pooled over the held-out conditions' offset columns. Shuffle: reach\n# parameters permuted across conditions, 1000 permutations (standard choice).\n\n# %%\ndef loc_cv(P, Y, folds, model):\n    pred = np.zeros_like(Y)\n    for te in folds:\n        tr = np.setdiff1d(np.arange(len(P)), te)\n        if model == \"linear\":\n            f = ridge_code(P[tr], Y[tr], 0.1)\n        elif model == \"ou\":\n            f = kernel_map(P[tr], Y[tr], OU(1e3), 0)\n        else:\n            f = kernel_map(P[tr], Y[tr], GAUSS(400), 0.1)\n        pred[te] = f(P[te])\n    return 1 - ((Y - pred) ** 2).sum() / ((Y - Y.mean(0)) ** 2).sum()\n\nF6E = []\nfor n in NAMES:\n    tb = TBF[n]\n    off = [i for f, i in ldr.groups(tb) if len(i) == 1][0][0]\n    Y = tb[\"L\"][:, :, off]\n    folds = six_folds(\"fig6e-kinematics-predict-location\")\n    g = ldr.rng(\"fig6e-kinematics-predict-location\", 1)\n    perms = [g.permutation(72) for _ in range(1000)]\n    for rd in KB:\n        P = PARAMS[(n, rd)]\n        for model in (\"linear\", \"ou\", \"gauss\"):\n            v = loc_cv(P, Y, folds, model)\n            nulls = np.array([loc_cv(P[p], Y, folds, model) for p in perms])\n            seeds = [loc_cv(P, Y, six_folds(\"fig6e-kinematics-predict-location\", k), model) for k in SEED_OFFSETS[1:]]\n            F6E.append(dict(dataset=n, kin=rd, model=model, ve=v, null_max=nulls.max(), null_mean=nulls.mean(),\n                            p=(1 + (nulls >= v).sum()) / 1001, seeds=np.round(seeds, 3)))\n\n# %% tags=[\"claim:fig6e-kinematics-predict-location\"]\nF6 = pd.DataFrame(F6E)\nprint(F6.round(3).to_string(index=False))\nfor rd in KB:\n    sub = F6[F6.kin == rd].set_index([\"dataset\", \"model\"])\n    lin = sub.xs(\"linear\", level=\"model\")\n    for km in (\"ou\", \"gauss\"):\n        ker = sub.xs(km, level=\"model\")\n        ok = lin.ve.between(0.333, 0.781).all() and ker.ve.between(0.621, 0.891).all() and \\\n            (lin.ve > lin.null_max).all() and (ker.ve > ker.null_max).all()\n        print(f\"kinematics {rd}, kernel {km}: linear in 33.3..78.1 {lin.ve.between(0.333, 0.781).sum()}/4, kernel in \"\n              f\"62.1..89.1 {ker.ve.between(0.621, 0.891).sum()}/4, above all permutations {(lin.ve > lin.null_max).sum()}/4 \"\n              f\"and {(ker.ve > ker.null_max).sum()}/4; all hold: {ok}\")\n\n# %% [markdown]\n# ## fig7c-ldr-encoding\n# > Predicting each condition's loading matrix from four reach parameters and multiplying by the shared\n# > basis functions explained 60 to 78% of the population variance with a linear model and 71 to 87% with\n# > kernel regression, above chance.\n#\n# Code kinToTBF.m and predictDataUsingTBFandKinCondStructure(Nonlinear).m: 6 folds over conditions, TBF on the\n# training conditions; ridge (lambda 0.1, row of ones penalised) from the four parameters to the vectorised\n# loadings; kernel regression with the Ornstein-Uhlenbeck kernel, length scale 10^3, no penalty; predicted\n# loadings times the basis; variance explained per held-out condition. Null: the neural data permuted across\n# conditions, the kinematics kept (code), scored against the real data; signed-rank test.\n\n# %%\ndef ldr_encode(Xfit, Xeval, P, k, folds, model, nn=False):\n    pred = np.full(Xeval.shape, np.nan)\n    for te in folds:\n        tr = np.setdiff1d(np.arange(len(Xfit)), te)\n        tb = ldr.eig_transform(Xfit[tr], k)\n        Y = vec(tb[\"L\"])\n        if nn:\n            d = ((P[te][:, None] - P[tr][None]) ** 2).sum(-1)\n            Lh = Y[d.argmin(1)]\n        elif model == \"linear\":\n            Lh = ridge_code(P[tr], Y, 0.1)(P[te])\n        else:\n            Lh = kernel_map(P[tr], Y, OU(1e3), 0)(P[te])\n        pred[te] = Lh.reshape(len(te), -1, k) @ tb[\"B\"].T\n    return ldr.var_explained(Xeval, pred)\n\nENC = {}\nfor n in NAMES:\n    X = DS[n][\"X\"]\n    folds = six_folds(\"fig7c-ldr-encoding\")\n    perm = ldr.rng(\"fig7c-ldr-encoding\", 1).permutation(72)\n    for rd in KB:\n        P = PARAMS[(n, rd)]\n        for model in (\"linear\", \"kernel\"):\n            v = ldr_encode(X, X, P, K[n], folds, model)\n            nv = ldr_encode(X[perm], X, P, K[n], folds, model)\n            seeds = [ldr_encode(X, X, P, K[n], six_folds(\"fig7c-ldr-encoding\", k), model).mean() for k in SEED_OFFSETS[1:]]\n            ENC[(n, rd, model)] = dict(v=v, null=nv, seeds=seeds)\n\n# %% tags=[\"claim:fig7c-ldr-encoding\"]\nrows = []\nfor (n, rd, model), e in ENC.items():\n    rows.append(dict(dataset=n, kin=rd, model=model, mean=e[\"v\"].mean(), sd=e[\"v\"].std(ddof=1), null=e[\"null\"].mean(),\n                     p=stats.wilcoxon(e[\"v\"], e[\"null\"]).pvalue, seeds=np.round(e[\"seeds\"], 3)))\nEN = pd.DataFrame(rows)\nprint(EN.round(4).to_string(index=False))\nfor rd in KB:\n    lin = EN[(EN.kin == rd) & (EN.model == \"linear\")]\n    ker = EN[(EN.kin == rd) & (EN.model == \"kernel\")]\n    print(f\"kinematics {rd}: linear in 54..85.8 {lin['mean'].between(0.54, 0.858).sum()}/4 with p < 0.001 and above null \"\n          f\"{((lin.p < 0.001) & (lin['mean'] > lin.null)).sum()}/4; kernel in 63.9..95.7 {ker['mean'].between(0.639, 0.957).sum()}/4 \"\n          f\"with p < 0.01 and above null {((ker.p < 0.01) & (ker['mean'] > ker.null)).sum()}/4\")\n\n# %% [markdown]\n# ## suppfig7a-not-memorization\n# > With targets held out by sextant, kernel-regression LDR encoding outperformed nearest-neighbour\n# > regression, so it was not memorization of the training set.\n#\n# Code splitTrialsAngles.m: conditions sorted by the angle of the path's end point, six contiguous blocks of\n# 12; kernel LDR encoding and the same model with nearest-neighbour regression (code\n# predictDataUsingTBFandKinNN.m); signed-rank test over conditions.\n\n# %% tags=[\"claim:suppfig7a-not-memorization\"]\nfor n in NAMES:\n    X = DS[n][\"X\"]\n    ang = np.arctan2(DS[n][\"kin\"][:, -1, 1], DS[n][\"kin\"][:, -1, 0])\n    order = np.argsort(ang)\n    folds = [np.sort(order[i * 12:(i + 1) * 12]) for i in range(6)]\n    for rd in KB:\n        P = PARAMS[(n, rd)]\n        vk = ldr_encode(X, X, P, K[n], folds, \"kernel\")\n        vn = ldr_encode(X, X, P, K[n], folds, \"kernel\", nn=True)\n        p = stats.wilcoxon(vk, vn).pvalue\n        print(f\"{n} ({rd}): kernel {vk.mean()*100:.1f}%, nearest neighbour {vn.mean()*100:.1f}%, signed-rank p = {p:.2g}; \"\n              f\"kernel higher with p < 0.01: {vk.mean() > vn.mean() and p < 0.01}\")\n\n# %% [markdown]\n# ## fig7c-standard-encoding-worse\n# > Standard instantaneous encoding models (linear multi-parameter, kernel regression on position, kernel\n# > regression on velocity) were substantially outperformed by both linear and nonlinear LDR encoding.\n#\n# Code predictDataUsingKin.m and predictDataUsingKinNonlinear.m (linearControls.m, nonlinearControls.m): 100 ms\n# causal lag (10 bins); linear: ones, x, y, distance, cos and sin of the position angle, velocity x and y,\n# speed, smoothed acceleration x and y and its magnitude, ridge lambda 0.1; kernel: OU, length scale 10^12 on\n# (x, y, distance) or 10^11 on smoothed (vx, vy, speed), no penalty, training samples every second bin;\n# 6 folds over conditions; variance explained per held-out condition over the lagged window. Compared with\n# the LDR encoders (kinematic reading svd) by signed-rank tests over conditions.\n\n# %%\ndef std_features(kin, kind):\n    x, y = kin[:, 0], kin[:, 1]\n    if kind == \"linear\":\n        ax_ = gaussian_filter1d(np.diff(x, 2), 2, mode=\"nearest\", truncate=2)\n        ay_ = gaussian_filter1d(np.diff(y, 2), 2, mode=\"nearest\", truncate=2)\n        F = np.c_[np.ones(len(x) - 2), x[2:], y[2:], np.hypot(x[2:], y[2:]), np.cos(np.arctan2(y[2:], x[2:])),\n                  np.sin(np.arctan2(y[2:], x[2:])), np.diff(x[1:]), np.diff(y[1:]), np.hypot(np.diff(x[1:]), np.diff(y[1:])),\n                  ax_, ay_, np.hypot(ax_, ay_)]\n        return F[10:]\n    if kind == \"pos\":\n        return np.c_[x, y, np.hypot(x, y)][10:]\n    vx = gaussian_filter1d(np.diff(x), 2, mode=\"reflect\", truncate=10 / 2)\n    vy = gaussian_filter1d(np.diff(y), 2, mode=\"reflect\", truncate=10 / 2)\n    return np.c_[vx, vy, np.hypot(vx, vy)][10:]\n\ndef std_encode(n, kind, folds):\n    X = DS[n][\"X\"]\n    kin = DS[n][\"kin\"]\n    if kind == \"linear\":\n        D = X[:, :, 2:-10]\n    elif kind == \"pos\":\n        D = X[:, :, :-10]\n    else:\n        D = X[:, :, 1:-10]\n    F = np.stack([std_features(kin[c], kind) for c in range(72)])\n    pred = np.zeros_like(D)\n    for te in folds:\n        tr = np.setdiff1d(np.arange(72), te)\n        Ftr = np.concatenate(F[tr]); Dtr = np.concatenate([d.T for d in D[tr]])\n        if kind == \"linear\":\n            W = np.linalg.solve(Ftr.T @ Ftr + 0.1 * np.eye(Ftr.shape[1]), Ftr.T @ Dtr)\n            for c in te:\n                pred[c] = (F[c] @ W).T\n        else:\n            ls = 1e12 if kind == \"pos\" else 1e11\n            f = kernel_map(Ftr[::2], Dtr[::2], OU(ls), 0)\n            for c in te:\n                pred[c] = f(F[c]).T\n    return ldr.var_explained(D, pred)\n\n# %% tags=[\"claim:fig7c-standard-encoding-worse\"]\nT = time.time()\nrows = []\nfor n in NAMES:\n    folds = six_folds(\"fig7c-standard-encoding-worse\")\n    lin_ldr, ker_ldr = ENC[(n, \"svd\", \"linear\")][\"v\"], ENC[(n, \"svd\", \"kernel\")][\"v\"]\n    for kind in (\"linear\", \"pos\", \"vel\"):\n        v = std_encode(n, kind, folds)\n        for nm, ref in ((\"LDR linear\", lin_ldr), (\"LDR kernel\", ker_ldr)):\n            p = stats.wilcoxon(ref, v).pvalue\n            rows.append(dict(dataset=n, standard=kind, standard_mean=v.mean(), ldr=nm, ldr_mean=ref.mean(), p=p,\n                             ldr_better=ref.mean() > v.mean() and p < 0.001))\nST = pd.DataFrame(rows)\nprint(ST.round(4).to_string(index=False))\nprint(f\"comparisons where LDR is higher with p < 0.001: {ST.ldr_better.sum()} of {len(ST)}; ran in {time.time() - T:.0f} s\")\n\n# %% [markdown]\n# ## fig7f-ldr-decoding\n# > A linear LDR-based decoder applied to single-trial spiking explained on average 84 to 92% of the variance\n# > in hand position over time.\n#\n# Code kinFromTBFSingleTrial.m and predictKinUsingTBFandDataCondStructureSingletrial.m: two folds over\n# conditions; on the training half, the raw SVD basis of the trial averages and a ridge map (lambda 10, row of\n# ones penalised) from the vectorised loadings to the four reach parameters; single-trial loadings of the\n# held-out half from 10 ms spike counts (spikes/s) times the pseudo-inverse of the basis; predicted parameters\n# times the position basis give the hand path; variance explained per trial (code getVarExplainedKinematics.m,\n# negatives 0) against the trial's own hand path. Null (reported): neural data of the training conditions\n# permuted across conditions.\n\n# %%\ndef decode(n, rd, folds, lam=10, Xfit=None, permute=None, potent=None):\n    d = DS[n]\n    X = d[\"X\"] if Xfit is None else Xfit\n    P = PARAMS[(n, rd)]\n    pos_b = KB[rd][0]\n    tri_pred = np.full((len(d[\"cond\"]), 4), np.nan)\n    cond_pred = np.full((72, 4), np.nan)\n    for te in folds:\n        tr = np.setdiff1d(np.arange(72), te)\n        Xtr = X[tr] if permute is None else X[permute[tr]]\n        B, L = ldr.get_basis(Xtr, K[n])\n        f = ridge_code(vec(L), P[tr], lam)\n        sel = np.isin(d[\"cond\"], te)\n        Lt = d[\"bc\"][sel] @ np.linalg.pinv(B.T) if potent is None else (potent @ d[\"bc\"][sel]) @ np.linalg.pinv(B.T)\n        tri_pred[sel] = f(vec(Lt))\n        cond_pred[te] = f(vec(X[te] @ np.linalg.pinv(B.T)))\n    path = ldr.params_to_path(pos_b, tri_pred)\n    true = d[\"hand10\"]\n    ve = 1 - (true - path).var(1, ddof=1).sum(1) / true.var(1, ddof=1).sum(1)\n    cpath = ldr.params_to_path(pos_b, cond_pred)\n    cve = 1 - (d[\"kin\"] - cpath).var(1, ddof=1).sum(1) / d[\"kin\"].var(1, ddof=1).sum(1)\n    return np.clip(ve, 0, None), tri_pred, np.clip(cve, 0, None)\n\nDEC = {}\nfor n in NAMES:\n    folds = six_folds(\"fig7f-ldr-decoding\", nf=2)\n    perm = ldr.rng(\"fig7f-ldr-decoding\", 1).permutation(72)\n    for rd in KB:\n        ve, tp, cve = decode(n, rd, folds)\n        nve, _, _ = decode(n, rd, folds, permute=perm)\n        seeds = [decode(n, rd, six_folds(\"fig7f-ldr-decoding\", k, nf=2))[0].mean() for k in SEED_OFFSETS[1:]]\n        DEC[(n, rd)] = dict(ve=ve, tp=tp, null=nve, seeds=seeds, folds=folds, cve=cve)\n\n# %% tags=[\"claim:fig7f-ldr-decoding\"]\nfor (n, rd), e in DEC.items():\n    p = stats.wilcoxon(e[\"ve\"], e[\"null\"]).pvalue\n    print(f\"{n} ({rd}): mean over {len(e['ve'])} trials {e['ve'].mean()*100:.1f}% (s.d. {e['ve'].std(ddof=1)*100:.1f}, \"\n          f\"median {np.median(e['ve'])*100:.1f}); in 75.6..100: {e['ve'].mean() >= 0.756}; condition-shuffled null \"\n          f\"{e['null'].mean()*100:.1f}% (signed-rank p = {p:.2g}); other seeds {np.round(np.array(e['seeds'])*100, 1)}\")\n\n# %% [markdown]\n# ## trial-curvature-decoding\n# > The LDR decoder followed trial-by-trial variation in reach curvature within a condition (rho 0.16 to 0.41).\n#\n# Code studyAroundMeanParams.m: the curvature parameters (x and y on the second basis function) of each decoded\n# trial and of the trial's own hand path, each minus its condition mean; Pearson correlation over all held-out\n# trials of a dataset.\n\n# %% tags=[\"claim:trial-curvature-decoding\"]\nfor (n, rd), e in DEC.items():\n    d = DS[n]\n    true = ldr.reach_params(KB[rd][0], d[\"hand10\"])\n    pred = e[\"tp\"]\n    tc, pc = true.copy(), pred.copy()\n    for c in range(72):\n        s = d[\"cond\"] == c\n        tc[s] -= true[s].mean(0); pc[s] -= pred[s].mean(0)\n    out = [stats.pearsonr(tc[:, j], pc[:, j]) for j in (2, 3)]\n    ok = all(0.144 <= r[0] <= 0.451 and r[1] < 0.001 for r in out)\n    print(f\"{n} ({rd}): x curvature rho {out[0][0]:.3f} (p = {out[0][1]:.2g}), y curvature rho {out[1][0]:.3f} \"\n          f\"(p = {out[1][1]:.2g}); both in 0.144..0.451 with p < 0.001: {ok}\")\n\n# %% [markdown]\n# ## suppfig8-no-output-potent-dependence\n# > Removing dimensions that encoded hand position, hand velocity and muscle activity produced no\n# > substantial degradation in LDR decoding.\n#\n# The dataset holds no EMG, so only the kinematic dimensions are removed (as the criterion says). Code\n# removePotent.m: least-squares map from the condition-averaged activity (each neuron's mean removed) to hand\n# x, y and their differences (each sample's mean over the four removed, as the code does); its row space is\n# projected out of each condition's activity (and, here, out of the single trials). Decoding with and without\n# the potent dimensions (code kinFromTBFNoPotent.m: condition-averaged decoding, ridge 1, 2 folds; the same\n# folds for both), per-condition variance explained, two-sided signed-rank test.\n\n# %% tags=[\"claim:suppfig8-no-output-potent-dependence\"]\nfor n in NAMES:\n    d = DS[n]\n    X = d[\"X\"]\n    kin = d[\"kin\"]\n    D = np.concatenate([x[:, :-1] for x in X], 1)\n    Kp = np.concatenate([np.c_[k[:-1, 0], k[:-1, 1], np.diff(k[:, 0]), np.diff(k[:, 1])] for k in kin])\n    Ksub = (Kp - Kp.mean(1, keepdims=True)).T\n    Dsub = D - D.mean(1, keepdims=True)\n    M = Ksub @ np.linalg.pinv(Dsub)\n    Proj = np.eye(len(M[0])) - np.linalg.pinv(M) @ M\n    Xr = np.einsum(\"nm,cmt->cnt\", Proj, X)\n    folds = six_folds(\"suppfig8-no-output-potent-dependence\", nf=2)\n    for rd in KB:\n        _, _, with_p = decode(n, rd, folds, lam=1)\n        _, _, without = decode(n, rd, folds, lam=1, Xfit=Xr, potent=Proj)\n        p = stats.wilcoxon(with_p, without).pvalue\n        print(f\"{n} ({rd}): with potent {with_p.mean()*100:.1f}%, without {without.mean()*100:.1f}% (mean drop \"\n              f\"{(with_p - without).mean()*100:.2f} points); two-sided signed-rank p = {p:.3g}; p >= 0.036: {p >= 0.036}\")\n\n# %% [markdown]\n# ## fig7f-decoder-beats-standard\n# Blocked as too large. The comparison decoders include Ornstein-Uhlenbeck kernel regression trained on single\n# trials and GPFA followed by kernel decoders. Trained on single trials at 10 ms, a training half holds about\n# 800 to 1000 trials of 121 bins, about 100,000 samples, so the kernel matrix alone is about 10^10 entries\n# (80 GB in double precision; 20 GB with the code's every-second-sample thinning), over the 12 GB the runner\n# allows. GPFA's latent dimensionality and bin size are not given (the claims file names readings), and no\n# GPFA implementation is in this entry's environment. The decoder comparison is therefore not run.\n\n# %%\nprint(f\"notebook ran in {(time.time() - T_START)/60:.1f} min; peak memory \"\n      f\"{resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1e6:.1f} GB\")\n"
}
```

```
File created successfully at: /tmp/claude-1001/nb2.py (file state is current in your context — no need to Read it back)
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 mkdev.py nb2.py && sed -i 's/for _ in range(1000)\]/for _ in range(20)]/; s/folds=100)\["k"\]/folds=10)["k"]/' dev_nb2.py && . env/bin/activate && cd entries/sabatini-2024 && PYTHONPATH=. timeout 1200 python -u $TMPDIR/dev_nb2.py 2>&1 | tail -80; date -u
```

```
k per dataset: {'M1-J': 7, 'PMd-J': 7}
loaded in 6 s, peak memory 1.6 GB
velocity singular vector 1: peak at 110 ms; skew-normal fit R2 0.984
velocity singular vector 2: peak at 260 ms; skew-normal fit R2 0.745
J: reach parameters ranges [-25.  -22.9 -19.1 -36. ]..[29.9 25.8 27.6 22.8]; the two basis functions explain 99.3% of the condition-mean hand path (min 93.1%)
Traceback (most recent call last):
  File "/tmp/claude-1001/dev_nb2.py", line 58, in <module>
    P = PARAMS[(n, "svd")]
        ~~~~~~^^^^^^^^^^^^
KeyError: ('M1-N', 'svd')
Fri Nov 27 23:34:37 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR && sed -i 's/^for n in ("M1-J", "M1-N"):$/for n in [f"M1-{m}" for m in MONKEYS]:/' nb2.py && python3 mkdev.py nb2.py && sed -i 's/for _ in range(1000)\]/for _ in range(20)]/; s/folds=100)\["k"\]/folds=10)["k"]/' dev_nb2.py && . env/bin/activate && cd entries/sabatini-2024 && PYTHONPATH=. timeout 1500 python -u $TMPDIR/dev_nb2.py 2>&1 | tail -80; date -u
```

```
M1-J          3          1       True 0.8748 0.0819 0.6257         0.0        0.0
   M1-J          3          2       True 0.7778 0.0995 0.1732         0.0        0.0
  PMd-J          0          1      False 0.8135 0.1237 0.5006         0.0        0.0
  PMd-J          0          2      False 0.5438 0.1908 0.1840         0.0        0.0
  PMd-J          0          3      False 0.4583 0.1504 0.2000         0.0        0.0
  PMd-J          1          0      False 0.9872 0.0076 0.9584         0.0        0.0
  PMd-J          1          2       True 0.7243 0.0864 0.1588         0.0        0.0
  PMd-J          1          3       True 0.5434 0.1509 0.1397         0.0        0.0
  PMd-J          2          0      False 0.9836 0.0129 0.9589         0.0        0.0
  PMd-J          2          1       True 0.9051 0.0485 0.4400         0.0        0.0
  PMd-J          2          3       True 0.6242 0.1429 0.0833         0.0        0.0
  PMd-J          3          0      False 0.9825 0.0109 0.9570         0.0        0.0
  PMd-J          3          1       True 0.8715 0.0676 0.4773         0.0        0.0
  PMd-J          3          2       True 0.7337 0.1002 0.1408         0.0        0.0
rotation pairs: means 54.3..90.5%; in 38.7..100: 12 of 12; above null with signed-rank p < 0.001: 12 of 12 (rank-sum: 12)
M1-J: mean over rotation pairs under seeds +1000..+4000: [0.806 0.797 0.806 0.804]
PMd-J: mean over rotation pairs under seeds +1000..+4000: [0.73  0.721 0.729 0.73 ]
M1-J: mean 71.0% (s.d. 8.8); null 44.0%; signed-rank p = 7.6e-12; in 60.3..88: True; code variant (2 folds, lambda 0.01, SVD 90%) 78.0%; other seeds [71.3 71.3 72.1 72.5]
PMd-J: mean 70.0% (s.d. 15.9); null 35.7%; signed-rank p = 4e-12; in 60.3..88: True; code variant (2 folds, lambda 0.01, SVD 90%) 78.2%; other seeds [69.6 69.  69.2 69.4]
M1-J: PCs 1-2 hold 60.5% of the offset variance; circular correlation of target angle with PC angle -0.657 (p = 5.1e-07), mirrored 0.657 (p = 5.1e-07); best positive 0.657, p = 5.1e-
[... 61 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python tools/entry.py --help 2>&1 | head -30; grep -n "timeout\|runtime_minutes\|def cmd_run\|nbconvert\|papermill" tools/entry.py | head -30; cat entries/allen-2026/entry.yaml; cat entries/allen-2026/README.md | head -30
```

```
usage: entry.py [-h] [--output-dir OUTPUT_DIR] [--timeout TIMEOUT]
                [--max-minutes MAX_MINUTES] [--fresh] [--python PYTHON]
                [--before BEFORE]
                {lock,check,run,all,handover,upgrade-python,hash}
                entry [entry ...]

Lock, check and run one entry. This is the whole local workflow for a deposit.

    python tools/entry.py lock  entries/<name>   # pin the environment
    python tools/entry.py check entries/<name>   # validate metadata and conventions
    python tools/entry.py check entries/*/       # the same for every entry, in one process
    python tools/entry.py run   entries/<name>   # execute every notebook from a clean environment
    python tools/entry.py all   entries/<name>   # check, then run
    python tools/entry.py handover entries/<name> # the verifier's package, from the executed copies

`lock` compiles the entry's requirements.in (direct dependencies only) into
requirements.lock.txt with every version pinned.

`check` validates entry.yaml, and the claims and attempt files that mention
the entry, against the schemas, and applies the conventions that keep a result
[... 73 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 mkdev.py nb1.py && python3 - <<'EOF'
s=open('/tmp/claude-1001/dev_nb1.py').read()
s=s.replace('folds=100 if k == 0 else 20)','folds=3)')
s=s.replace('jobs = [(n, k) for n in NAMES for k in SEED_OFFSETS]\nSHOUT','jobs = [(n, k) for n in NAMES for k in SEED_OFFSETS[:1]]\nSHOUT').replace('rows = [SHOUT[(n, k)] for k in SEED_OFFSETS]','rows = [SHOUT[(n, k)] for k in SEED_OFFSETS[:1]]')
s=s.replace('jobs = [(n, k, "truncate") for n in NAMES for k in SEED_OFFSETS]','jobs = [(n, k, "truncate") for n in NAMES for k in SEED_OFFSETS[:1]]').replace('[WOUT[(n, k, "truncate")] for k in SEED_OFFSETS]','[WOUT[(n, k, "truncate")] for k in SEED_OFFSETS[:1]]')
s=s.replace('(n, 0, 100, 0.5) for n in NAMES] + [(n, 1, 20, 0.75)','(n, 0, 3, 0.5) for n in NAMES] + [(n, 1, 3, 0.75)').replace('LOUT[(n, 0, 100, 0.5)], 0.75: LOUT[(n, 1, 20, 0.75)]','LOUT[(n, 0, 3, 0.5)], 0.75: LOUT[(n, 1, 3, 0.75)]').replace('(n, k, 10, 0.5) for n in NAMES for k','(n, k, 2, 0.5) for n in NAMES for k').replace('LOUT[(n, k, 10, 0.5)]','LOUT[(n, k, 2, 0.5)]')
s=s.replace('"proj"], 0, 150) for n','"proj"], 0, 5) for n').replace('"proj"], 1, 30) for n','"proj"], 1, 2) for n').replace('(n, KLDS[n]["proj"], k, 20) for n','(n, KLDS[n]["proj"], k, 2) for n')
s=s.replace('ldr.rng("fig4b-plane-alignment", k), 36)\n','ldr.rng("fig4b-plane-alignment", k), 4)\n').replace('for r in range(36)]','for r in range(4)]')
s=s.replace('for c in range(72)])\n    m = min','for c in range(2)])\n    m = min')
s=s.replace('ldr.rng("rotation-orientation-dimensionality"), 100)','ldr.rng("rotation-orientation-dimensionality"), 3)')
open('/tmp/claude-1001/dev_nb1.py','w').write(s)
EOF
grep -n "range(2)\])\|, 4)$\|dimensionality\"), 3)" dev_nb1.py | head; . env/bin/activate && cd entries/sabatini-2024 && PYTHONPATH=. timeout 900 python -u $TMPDIR/dev_nb1.py 2>&1 | sed -n '/alignment in/,$p' | tail -60; date -u
```

```
758:NOISE = {(n, k): noise_loadings(DS[n], TBF[n], ldr.rng("fig4b-plane-alignment", k), 4)
894:    noise = np.array([ldr.sea(np.concatenate([L1[:, c][:, :, inds], L2[:, c][:, :, inds]]), 25) for c in range(2)])
951:    return snr_dims(DS[n], K[n], ldr.rng("rotation-orientation-dimensionality"), 3)
alignment in 4 s
dataset  freq  obs_mean  noise_mean    auc  p_signrank  p_ranksum
   M1-J  0.73    0.6314      0.8397 0.9026         0.0        0.0
   M1-J  2.01    0.2569      0.5999 0.9114         0.0        0.0
   M1-J  3.38    0.3111      0.5849 0.8802         0.0        0.0
  PMd-J  0.64    0.6728      0.8574 0.9142         0.0        0.0
  PMd-J  1.64    0.2953      0.5232 0.8573         0.0        0.0
  PMd-J  2.64    0.2022      0.3659 0.8323         0.0        0.0
rotations with AUC in 0.765..1 and observed lower: 6 of 6; signed-rank p < 0.001 for 6, rank-sum p < 0.001 for 6
M1-J AUC per rotation under seeds +1000..+4000: [array([0.904, 0.908, 0.883]), array([0.905, 0.912, 0.881]), array([0.907, 0.909, 0.885]), array([0.904, 0.911, 0.883])]
PMd-J AUC per rotation under seeds +1000..+4000: [array([0.909, 0.853, 0.82 ]), array([0.912, 0.862, 0.835]), array([0.911, 0.861, 0.824]), array([0.907, 0.86 , 0.823])]
M1-J offset (freq 0.00): observed 0.969, noise 0.991, AUC 0.892 (in 0.792..1: True), signed-rank p = 1.7e-13, rank-sum p = 1.5e-111
PMd-J offset (freq 0.00): observed 0.951, noise 0.967, AUC 0.708 (in 0.792..1: False), signed-rank p = 3.3e-12, rank-sum p = 1.3e-32
dataset  rot  other   same  different  p_paired  p_ranksum
   M1-J 0.73   2.01 0.6314     0.1551    0.0000     0.0000
   M1-J 0.73   3.38 0.6314     0.1499    0.0000     0.0000
   M1-J 2.01   0.73 0.2569     0.1494    0.0000     0.0000
[... 41 more lines not kept]
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb1.py').read()
a=s.index('def snr_dims'); b=s.index('T = time.time()\nSNR')
c=s.index('# %% tags=["claim:rotation-orientation-dimensionality"]'); e=s.index('# %% [markdown]\n# ## Summary')
code='''import pickle,time,numpy as np,pandas as pd,ldr
DS=pickle.load(open('/tmp/claude-1001/DSJ.pkl','rb')); NAMES=['M1-J','PMd-J']
K={n:7 for n in NAMES}; TBF={n:ldr.eig_transform(DS[n]['X'],7) for n in NAMES}
GEO={n:dict(groups=ldr.groups(TBF[n])) for n in NAMES}
SEA={}
for n in NAMES:
    for f,i in GEO[n]['groups']:
        SEA[(n,f)]=dict(data=ldr.sea(TBF[n]['L'][:,:,i],25),p=np.zeros(25))
'''+s[a:b]+'\nT=time.time(); SNR={n: snr_dims(DS[n],K[n],ldr.rng("x"),2) for n in NAMES}; print("snr 2 folds",time.time()-T)\n'+s[c:e].replace('# %% tags=["claim:rotation-orientation-dimensionality"]','').replace('# %% tags=["claim:suppfig6b-location-dimensionality"]','')
open('t_dim.py','w').write(code)
EOF
. env/bin/activate; PYTHONPATH=entries/sabatini-2024 timeout 300 python t_dim.py 2>&1 | tail -30
```

```
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ValueError: substring not found
python: can't open file '/tmp/claude-1001/t_dim.py': [Errno 2] No such file or directory
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && grep -n "SNR = \|def snr_dims\|## Summary" nb1.py
```

```
926:def snr_dims(d, k, g, folds=100):
949:SNR = dict(zip(NAMES, pmap(snr_job, [(n,) for n in NAMES])))
987:# ## Summary
Shell cwd was reset to
```

**Agent calls Bash**

```bash
cd $TMPDIR && python3 - <<'EOF'
s=open('nb1.py').read()
a=s.index('def snr_dims'); b=s.index('T = time.time()\ndef snr_job') if 'T = time.time()\ndef snr_job' in s else s.index('def snr_job')
c=s.index('# %% tags=["claim:rotation-orientation-dimensionality"]'); e=s.index('# ## Summary')
code='''import pickle,time,numpy as np,pandas as pd,ldr
DS=pickle.load(open('/tmp/claude-1001/DSJ.pkl','rb')); NAMES=['M1-J','PMd-J']
K={n:7 for n in NAMES}; TBF={n:ldr.eig_transform(DS[n]['X'],7) for n in NAMES}
GEO={n:dict(groups=ldr.groups(TBF[n])) for n in NAMES}
SEA={}
for n in NAMES:
    for f,i in GEO[n]['groups']:
        SEA[(n,f)]=dict(data=ldr.sea(TBF[n]['L'][:,:,i],25),p=np.zeros(25))
'''+s[a:b]+'\nT=time.time(); SNR={n: snr_dims(DS[n],K[n],ldr.rng("x"),2) for n in NAMES}; print("snr 2 folds",time.time()-T)\n'+s[c:e].replace('# %% tags=["claim:rotation-orientation-dimensionality"]','').replace('# %% tags=["claim:suppfig6b-location-dimensionality"]','').replace('# %% [markdown]','')
open('t_dim.py','w').write(code)
EOF
. env/bin/activate; PYTHONPATH=entries/sabatini-2024 timeout 300 python t_dim.py 2>&1 | tail -30
```

```
snr 2 folds 2.7084572315216064
dataset  freq     kind  pcs80_a  pr_a  pcs80_b  pr_b  snr_dims
   M1-J   0.0 location        4   4.0        4   4.0         6
   M1-J   0.7 rotation        7   5.0        3   2.3        19
   M1-J   2.0 rotation        7   6.6        7   5.5        13
   M1-J   3.4 rotation        8   5.4        7   5.2        11
  PMd-J   0.0 location        7   3.8        7   3.9         2
  PMd-J   0.6 rotation        3   2.3        3   2.1        15
  PMd-J   1.6 rotation       10   5.4        8   5.0         9
  PMd-J   2.6 rotation       17   9.2       16   8.8        10
rotations, reading a: PCs to 80% in 20.7..44 0/6; participation ratio in 15.03..40.48 0/6
rotations, reading b: PCs to 80% in 20.7..44 0/6; participation ratio in 15.03..40.48 0/6
rotations: SNR dimensions in 6.3..36.3 6/6
M1-J location: SEA angles above 15 deg 1 (in 3.6..5.5: False); first angles [15.4  9.3  7.4  7.1  6.3  5.2  5.2  4.9]; dimensions above noise 25
PMd-J location: SEA angles above 15 deg 1 (in 3.6..5.5: False); first angles [23.8 13.  11.3  9.3  8.2  7.4  7.1  6.9]; dimensions above noise 25
dataset  freq     kind  pcs80_a  pr_a  pcs80_b  pr_b  snr_dims
   M1-J   0.0 location        4   4.0        4   4.0         6
  PMd-J   0.0 location        7   3.8        7   3.9         2
location, reading a: PCs in 18.9..33 0/4; participation ratio in 13.59..29.04 0/4
location, reading b: PCs in 18.9..33 0/4; participation ratio in 13.59..29.04 0/4
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  grep -n "max-minutes\|max_minutes" tools/entry.py | head -8; . $TMPDIR/env/bin/activate; E=entries/sabatini-2024; jupytext --to ipynb -o $E/reproduce_sabatini_2024.ipynb $TMPDIR/nb1.py >/dev/null && jupytext --to ipynb -o $E/reproduce_sabatini_2024_kinematics.ipynb $TMPDIR/nb2.py >/dev/null; python - <<'EOF'
import json
for f in ['reproduce_sabatini_2024.ipynb','reproduce_sabatini_2024_kinematics.ipynb']:
    p='entries/sabatini-2024/'+f; nb=json.load(open(p))
    tags=[c.get('metadata',{}).get('tags') for c in nb['cells'] if c.get('metadata',{}).get('tags')]
    print(f,len(nb['cells']),tags[:40])
    nb['metadata']['kernelspec']={'name':'python3','display_name':'Python 3','language':'python'}
    json.dump(nb,open(p,'w'),indent=1)
EOF
cat > $E/requirements.in <<'EOF'
h5py
matplotlib
numpy
pandas
remfile
requests
scikit-learn
scipy
EOF
cat > $E/entry.yaml <<'EOF'
schema_version: 1
name: sabatini-2024
type: reproduction
title: Reach-dependent reorientation of rotational dynamics in motor cortex (Sabatini and Kaufman 2024)
description: Tests the findings of Sabatini and Kaufman (2024) on dandiset 000070, which holds the maze-task
  sessions of monkeys J and N with threshold crossings from a PMd and an M1 Utah array and hand position.
  On the two sessions the paper names it rebuilds the temporal basis factorization, the single-condition
  linear dynamical systems and jPCA, and tests the geometry of the rotations, the prediction of rotations
  from each other and from the state space location, LDR encoding and single-trial LDR decoding.
license: Apache-2.0
notebooks:
- path: reproduce_sabatini_2024.ipynb
  title: Dynamics, factorization, jPCA and rotation geometry (notebook 1 of 2)
  runtime_minutes: 40
- path: reproduce_sabatini_2024_kinematics.ipynb
  title: Prediction, encoding and decoding (notebook 2 of 2)
  runtime_minutes: 15
helpers:
- ldr.py
related:
- id: dandi:000070/0.261122.2046
  relation: uses_data
- id: doi:10.1038/s41467-024-51308-7
  relation: reproduces
EOF
python tools/entry.py lock $E 2>&1 | tail -3; python tools/entry.py check $E 2>&1 | tail -15; date -u
```

```
29:that takes longer than --max-minutes fails, even if it ran without error.
554:                   max_minutes: float) -> int:
560:    if lock(entry_dir, version) or run(entry_dir, output_dir, timeout, max_minutes, fresh=True):
607:def reusable(entry_dir: Path, output_dir: Path, max_minutes: float) -> dict | None:
618:            if not r["ok"] or r["seconds"] > max_minutes * 60 or file_hash(output_dir / r["notebook"]) != r["sha256"]:
625:def run(entry_dir: Path, output_dir: Path, timeout: int, max_minutes: float, fresh: bool = False) -> int:
627:    stamp = None if fresh else reusable(entry_dir, output_dir, max_minutes)
663:        if ok and seconds > max_minutes * 60:
reproduce_sabatini_2024.ipynb 64 [['sanity'], ['sanity'], ['sanity'], ['finding-unsorted-units'], ['claim:data-composition'], ['claim:fig3g-basis-frequencies'], ['claim:tbf-variance-explained'], ['claim:tbf-shuffle-control'], ['claim:fig3h-recoverability'], ['claim:fig3i-duration-warping'], ['claim:jpca-fit-r2'], ['claim:jpca-variance-explained'], ['claim:fig4d-jpca-variance-correlation'], ['claim:fig4f-plane-alignment-explains-jpca'], ['claim:single-lds-variance'], ['claim:fig2c-condition-lds-variance'], ['claim:fig3a-eigenvalue-clusters'], ['claim:fig3c-eigenvalue-distance-auc'], ['claim:suppfig2-eigenvalues-from-kinematics'], ['claim:suppfig3-model-comparison'], ['claim:fig4b-plane-alignment'], ['claim:suppfig6a-location-alignment'], ['claim:fig5a-frequencies-segregated'], ['claim:suppfig6c-location-distinct-from-rotations'], ['claim:fig4c-subspace-excursion-angles'], ['claim:rotation-orientation-dimensionality'], ['claim:suppfig6b-location-dimensionality']]
reproduce_sabatini_2024_kinematics.ipynb 32 [['sanity'], ['claim:fig5c-rotations-predict-rotations'], ['claim:fig6b-location-predicts-rotations'], ['claim:fig6c-location-tracks-direction'], ['claim:fig6e-kinematics-predict-location'], ['claim:fig7c-ldr-encoding'], ['claim:suppfig7a-not-memorization'], ['claim:fig7c-standard-encoding-worse'], 
[... 3 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; timeout 6600 python tools/entry.py all entries/sabatini-2024 --max-minutes 60 2>&1 | tail -20; date -u
```

```
Fri Nov 27 23:40:02 UTC 2026
[32m--> [39m[32m421[39m     oid = [30;43mh5o[39;49m[30;43m.[39;49m[30;43mopen[39;49m[30;43m([39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43mid[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mself[39;49m[30;43m.[39;49m[30;43m_e[39;49m[30;43m([39;49m[30;43mname[39;49m[30;43m)[39;49m[30;43m,[39;49m[30;43m [39;49m[30;43mlapl[39;49m[30;43m=[39;49m[30;43mlapl[39;49m[30;43m)[39;49m
[32m    422[39m [38;5;28;01melse[39;00m:
[32m    423[39m     [38;5;28;01mraise[39;00m [38;5;167;01mTypeError[39;00m([33m"[39m[33mAccessing a group is done with bytes or str, [39m[33m"[39m
[32m    424[39m                     [33m"[39m[33mnot [39m[38;5;132;01m{}[39;00m[33m"[39m.format([38;5;28mtype[39m(name)))

[36mFile [39m[32mh5py/_objects.pyx:54[39m, in [36mh5py._objects.with_phil.wrapper[39m[34m()[39m
[32m---> [39m[32m54[39m [33m'Could not get source, probably due dynamically evaluated source code.'[39m

[36mFile [39m[32mh5py/_objects.pyx:55[39m, in [36mh5py._objects.with_phil.wrapper[39m[34m()[39m
[32m---> [39m[32m55[39m [33m'Could not get source, probably due dynamically evaluated source code.'[39m

[36mFile [39m[32mh5py/h5o.pyx:255[39m, in [36mh5py.h5o.open[39m[34m()[39m
[32m--> [39m[32m255[39m [33m'Could not get source, probably due dynamically evaluated source code.'[39m

[31mKeyError[39m: "Unable to synchronously open object (object 'maze_condition' doesn't exist)"


0 error(s)
FAIL  reproduce_sabatini_2024.ipynb  (95 s)
[... 2 more lines not kept]
```

**Agent calls Bash**

```bash
cd  python3 - <<'EOF'
p='entries/sabatini-2024/reproduce_sabatini_2024.ipynb'
import json; nb=json.load(open(p))
for c in nb['cells']:
    s=''.join(c['source'])
    if 'conds=len(np.unique(t["maze_condition"][:]))' in s:
        s=s.replace('conds=len(np.unique(t["maze_condition"][:]))))','conds=len(np.unique(t["maze_condition"][:])) if "maze_condition" in t else None))')
        c['source']=s.splitlines(True)
json.dump(nb,open(p,'w'),indent=1)
EOF
grep -c 'if \\"maze_condition\\" in t' entries/sabatini-2024/reproduce_sabatini_2024.ipynb; sed -i 's/conds=len(np.unique(t\["maze_condition"\]\[:\]))))/conds=len(np.unique(t["maze_condition"][:])) if "maze_condition" in t else None))/' $TMPDIR/nb1.py; ls executed/sabatini-2024/; python3 -c "
import json
nb=json.load(open('executed/sabatini-2024/reproduce_sabatini_2024_kinematics.ipynb'))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    for o in c.get('outputs',[]):
        if o.get('name')=='stdout': print(''.join(o['text'])[:6000])
"
```

```
1
reproduce_sabatini_2024_kinematics.ipynb
result.json
k per dataset: {'M1-J': 7, 'PMd-J': 7, 'M1-N': 9, 'PMd-N': 9}
loaded in 140 s, peak memory 3.4 GB

velocity singular vector 1: peak at 120 ms; skew-normal fit R2 0.995
velocity singular vector 2: peak at 270 ms; skew-normal fit R2 0.829
J: reach parameters ranges [-24.9 -22.1 -17.8 -39. ]..[29.7 24.4 30.  25.9]; the two basis functions explain 99.3% of the condition-mean hand path (min 92.6%)
N: reach parameters ranges [-25.7 -21.5 -22.3 -26.4]..[25.6 25.  19.4 25.1]; the two basis functions explain 99.6% of the condition-mean hand path (min 98.4%)

dataset  predictor  predicted  rotations   mean     sd   null  p_signrank  p_ranksum
   M1-J          0          1      False 0.8541 0.0819 0.6635         0.0        0.0
   M1-J          0          2      False 0.5845 0.1591 0.2204         0.0        0.0
   M1-J          0          3      False 0.6262 0.1737 0.3587         0.0        0.0
   M1-J          1          0      False 0.9930 0.0065 0.9706         0.0        0.0
   M1-J          1          2       True 0.7580 0.1134 0.1865         0.0        0.0
   M1-J          1          3       True 0.7352 0.1081 0.2427         0.0        0.0
   M1-J          2          0      False 0.9907 0.0095 0.9709         0.0        0.0
   M1-J          2          1       True 0.8968 0.0625 0.5721         0.0        0.0
[... 203 more lines not kept]
```

**Agent calls Bash**

```bash
cd  date -u; timeout 6000 python tools/entry.py all entries/sabatini-2024 --max-minutes 60 2>&1 | tail -8; date -u
```

```
Fri Nov 27 23:50:22 UTC 2026
Installed kernelspec registry-sabatini-2024 in executed/sabatini-2024/.venv/share/jupyter/kernels/registry-sabatini-2024
0 error(s)
pass  reproduce_sabatini_2024.ipynb  (2210 s)
pass  reproduce_sabatini_2024_kinematics.ipynb  (503 s)
Sat Nov 28 00:35:47 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
nb=json.load(open('executed/sabatini-2024/reproduce_sabatini_2024.ipynb'))
for c in nb['cells']:
    if c['cell_type']!='code': continue
    t=c.get('metadata',{}).get('tags',[])
    out=''.join(''.join(o.get('text','')) for o in c.get('outputs',[]) if o.get('name')=='stdout')
    if out: print('##',t); print(out[:5000])
" > $TMPDIR/nb1out.txt; wc -l $TMPDIR/nb1out.txt; sed -n 1,200p $TMPDIR/nb1out.txt
```

```
384 /tmp/claude-1001/nb1out.txt
## []
loaded in 71 s, peak memory 3.4 GB

## ['sanity']
monkey J: 2636 trials in the file; maze conditions 0..108 (109 values, 203 trials with condition 0)
   condition mod 3 = 0: 36 conditions, targets [np.uint8(3)], barriers [np.uint8(6), np.uint8(7), np.uint8(8), np.uint8(9)], trial_version [np.uint8(2)]
   condition mod 3 = 1: 36 conditions, targets [np.uint8(1)], barriers [np.uint8(0)], trial_version [np.uint8(0)]
   condition mod 3 = 2: 36 conditions, targets [np.uint8(1)], barriers [np.uint8(6), np.uint8(7), np.uint8(8), np.uint8(9)], trial_version [np.uint8(1)]
   successful trials of the 72 conditions: 1595; with delay > 400 ms: 1381; discard_trial set: 0; windows past the trial end dropped: 0
   trials per condition 17..29 (median 22)
   delay range -4..998 ms; offline minus online movement onset, median -25 ms
   hand displacement at +850 ms (mm, start-subtracted): |x| up to 136, |y| up to 89; peak speed of the condition means 1043 mm/s
monkey N: 3694 trials in the file; maze conditions 0..108 (109 values, 419 trials with condition 0)
   condition mod 3 = 0: 36 conditions, targets [np.uint8(3)], barriers [np.uint8(7), np.uint8(8), np.uint8(9)], trial_version [np.uint8(2)]
   condition mod 3 = 1: 36 conditions, targets [np.uint8(1)], barriers [np.uint8(0)], trial_version [np.uint8(0)]
   condition mod 3 = 2: 36 conditions, targets [np.uint8(1)], barriers [np.uint8(7), np.uint8(8), np.uint8(9)], trial_version [np.uint8(1)]
   successful trials of the 72 conditions: 2121; with delay > 400 ms: 1884; discard_trial set: 0; windows past the trial end dropped: 0
   trials per condition 23..42 (median 29)
   delay range -3..999 ms; offline minus online movement onset, median -52 ms
[... 181 more lines not kept]
```

**Agent calls Bash**

```bash
sed -n 200,384p $TMPDIR/nb1out.txt; date -u
```

```
## []
[null_halves: 4 jobs in 295 s]
[null_poisson: 4 jobs in 135 s]
[null_halves: 16 jobs in 157 s]
nulls in 588 s

## ['claim:fig3c-eigenvalue-distance-auc']
M1-J (k=5): halves/mean: AUC 0.716 (obs median 0.0141 vs null 0.0087); halves/norm: AUC 0.711 (obs median 0.0381 vs null 0.0228); Poisson/mean: AUC 0.796 (obs median 0.0141 vs null 0.0067); Poisson/norm: AUC 0.786 (obs median 0.0381 vs null 0.0179)
PMd-J (k=5): halves/mean: AUC 0.670 (obs median 0.0144 vs null 0.0102); halves/norm: AUC 0.670 (obs median 0.0379 vs null 0.0268); Poisson/mean: AUC 0.731 (obs median 0.0144 vs null 0.0086); Poisson/norm: AUC 0.730 (obs median 0.0379 vs null 0.0230)
M1-N (k=7): halves/mean: AUC 0.660 (obs median 0.0185 vs null 0.0137); halves/norm: AUC 0.667 (obs median 0.0591 vs null 0.0427); Poisson/mean: AUC 0.646 (obs median 0.0185 vs null 0.0141); Poisson/norm: AUC 0.655 (obs median 0.0591 vs null 0.0445)
PMd-N (k=7): halves/mean: AUC 0.581 (obs median 0.0215 vs null 0.0190); halves/norm: AUC 0.579 (obs median 0.0651 vs null 0.0582); Poisson/mean: AUC 0.594 (obs median 0.0215 vs null 0.0186); Poisson/norm: AUC 0.590 (obs median 0.0651 vs null 0.0571)

## []
M1-J AUC under seeds +1000..+4000 (20 repeats): [0.715 0.705 0.713 0.716]
PMd-J AUC under seeds +1000..+4000 (20 repeats): [0.675 0.674 0.666 0.664]
M1-N AUC under seeds +1000..+4000 (20 repeats): [0.66  0.659 0.667 0.668]
PMd-N AUC under seeds +1000..+4000 (20 repeats): [0.598 0.579 0.581 0.58 ]

## ['claim:suppfig2-eigenvalues-from-kinematics']
kinematic basis svd, eigenvalues proj: mean R2 pooled 0.247 (in 0.05..0.15: False); per dataset {'M1-J': np.float32(0.499), 'PMd-J': np.float32(0.266), 'M1-N': np.float32(0.146), 'PMd-N': np.float32(0.161)}
[... 166 more lines not kept]
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/w && cat > $TMPDIR/w/results.py <<'EOF'
R = {
"data-composition": "**Result: partially reproduced.** Under both trial readings each monkey has 72 conditions, 36 without barriers (straight) and 36 with barriers (curved). Monkey J has 1595 successful trials (1381 with delay above 400 ms) and N has 2121 (1884), all within 10% of 1469 and 2014. Each array has 96 units, but they are unsorted threshold crossings, one per electrode; the dataset marks no single or multi-units, so the paper's 79 to 118 sorted units per array cannot be counted.",
"fig3g-basis-frequencies": "**Result: partially reproduced.** Cross-validation chooses k = 7 for both J arrays and k = 9 for both N arrays (the same under all five seeds), giving 3 (J) or 4 (N) rotation pairs and one real mode at 0 Hz in every dataset, as the claim states. The frequencies are not those of the paper: the slowest pair is at 0.61 to 0.73 Hz in all four datasets, and only 5 of the 14 rotations are within 10% of one of 0.5, 1.5, 2.5 and 4 Hz.",
"tbf-variance-explained": "**Result: reproduced.** The factorization explains 92.3%, 95.1%, 97.1% and 96.1% (M1-J, PMd-J, M1-N, PMd-N) from -150 to +850 ms, and 92.5% to 97.7% over the whole window with the raw basis, all inside 81 to 100%.",
"tbf-shuffle-control": "**Result: reproduced.** With 1 ms bins shuffled within each trial the factorization explains 35.1%, 35.4%, 45.6% and 45.5%, all inside 31.5 to 50.6% and under all five seeds, against 92.5% to 97.7% on the real data (rank-sum p = 3.9e-25 in each dataset).",
"fig3h-recoverability": "**Result: reproduced.** Recoverability is 95.1% to 96.6% (inside 81.9 to 100%) against a shuffled chance of 84.8% to 87.8% (inside 56.7 to 88%, near its top and above the paper's unwidened 63 to 80%), real higher with rank-sum p below 1e-24 in every dataset.",
"fig3i-duration-warping": "**Result: not reproduced.** Unwarped, the correlation of recoverability with the duration difference is -0.183 (M1-J), -0.104 (PMd-J), 0.013 (M1-N, paper -0.26, p = 0.92) and 0.246 (PMd-N, outside -0.198 to 0.231). Warped with truncation it is -0.508 and -0.504 for the two M1 arrays (p < 1e-5) but -0.060 and -0.267 for PMd, so only two of the four warped correlations lie in -0.693 to -0.468. The 250 ms variant gives -0.773, -0.761, -0.586 and -0.527, two of them below the range.",
"jpca-fit-r2": "**Result: partially reproduced.** Under reading (b), the unconstrained fit, the R2 over all conditions is 0.831 (M1-J), 0.583 (PMd-J), 0.656 (M1-N) and 0.475 (PMd-N): two of four inside 0.576 to 0.803 (reading a: one of four). Straight-only fits (0.748 to 0.882) and curved-only fits (0.575 to 0.770) are inside their ranges in all four datasets, and straight is above curved in all four. The per-condition signed-rank test gives p < 0.001 only for M1-J (p = 0.44 to 0.61 elsewhere).",
"jpca-variance-explained": "**Result: reproduced.** Activity in the retained jPCA planes holds 9.1%, 10.6%, 10.8% and 6.8% of the variance (s.d. 5.3 to 8.5% across conditions), all inside 6.3 to 13.2%. With the cross-condition mean added back to the reconstruction it would be 71.6% to 80.9%.",
"fig4d-jpca-variance-correlation": "**Result: not reproduced.** Five of the six retained jPCA planes (83%) correlate with the rotational variance at p < 0.05, outside 59.4 to 72.6%, and the correlations (-0.088 to 0.919; per-dataset means 0.321 to 0.919) are not in 0.351 to 0.506 under either reading.",
"fig4f-plane-alignment-explains-jpca": "**Result: partially reproduced.** The alignment of a condition's rotations with a jPCA plane correlates with the variance in that plane with rho 0.826 to 0.947 (p < 0.001) for five of the six planes; the first M1-N plane gives 0.685.",
"single-lds-variance": "**Result: not reproduced.** A single LDS over all conditions explains 77.3%, 81.3%, 82.6% and 78.6% from -150 ms on (79.6% to 86.5% over the whole window), above 41.4 to 72.6% in every dataset under both windows.",
"fig2c-condition-lds-variance": "**Result: reproduced.** Cross-validation chooses 5 dimensions for the J arrays and 7 for the N arrays under the Methods' projection score (the LDS score gives 5 for PMd-N), all inside 5 to 9, and the single-condition LDSs explain 83.2%, 90.5%, 92.8% and 94.1% (90.9% for PMd-N at 5), all above 63.9%. The choice is the same under the four other seeds, except the LDS score for PMd-N (5 under all four).",
"fig3a-eigenvalue-clusters": "**Result: not reproduced.** Every condition has a real eigenvalue, but the median frequencies of the eigenvalue pairs are 0.85 and 2.38 Hz (M1-J), 0.57 and 1.51 Hz (PMd-J), 0.63, 1.74 and 3.19 Hz (M1-N) and 0.62, 1.37 and 2.54 Hz (PMd-N): 4 of the 10 are within 10% of 0.5, 1.5 and 2.5 Hz in order.",
"fig3c-eigenvalue-distance-auc": "**Result: not reproduced.** With the mean distance, the AUC against the halves null is 0.716, 0.670, 0.660 and 0.581, and against the Poisson null 0.796, 0.731, 0.646 and 0.594; under either null only PMd-N lies in 0.459 to 0.638. The code's norm distance gives the same picture (0.579 to 0.786). The halves AUC is stable over the other four seeds (0.579 to 0.716).",
"suppfig2-eigenvalues-from-kinematics": "**Result: not reproduced.** The reach parameters and duration predict the eigenvalue components with a pooled mean leave-one-out R2 of 0.247 (projection-chosen dimensionality) or 0.298 (LDS-chosen), under both kinematic bases, outside 0.05 to 0.15; per dataset it is 0.146 to 0.499.",
"suppfig3-model-comparison": "**Result: not reproduced.** The cross-validated TBF variance (73.5%, 81.0%, 88.8%, 81.7%) is below the in-sample single-condition LDS (83.2%, 90.5%, 92.8%, 94.1%) in every dataset, though above jPCA (6.8% to 10.8%). In the all in-sample variant the TBF (92.3% to 97.1%) is the highest in all four.",
"fig4b-plane-alignment": "**Result: partially reproduced.** For 13 of the 14 rotations the same-frequency planes of different conditions are less aligned than the half-split noise, with AUC 0.828 to 0.943 and signed-rank p < 0.001; the 3.65 Hz rotation of PMd-N gives AUC 0.545 (signed-rank p = 0.0034). The AUCs barely move under the other four seeds.",
"suppfig6a-location-alignment": "**Result: partially reproduced.** The location is less aligned across conditions than the noise in every dataset (signed-rank p below 1e-11), with AUC 0.890 (M1-J) and 0.889 (M1-N) inside 0.792 to 1, but 0.698 (PMd-J) and 0.764 (PMd-N) below it.",
"fig5a-frequencies-segregated": "**Result: partially reproduced.** Same-frequency alignment is higher than different-frequency alignment with p < 0.001 in 35 of 36 comparisons under the paired reading (97%; the exception is PMd-J 2.64 against 1.64 Hz, 0.202 against 0.202) and 33 of 36 under the rank-sum reading.",
"suppfig6c-location-distinct-from-rotations": "**Result: reproduced.** In every dataset the location is far better aligned with other conditions' locations (0.892 to 0.969) than with any rotation's plane (0.104 to 0.580), with p below 1e-300 by both tests.",
"fig4c-subspace-excursion-angles": "**Result: partially reproduced.** The number of excursion angles above 45 degrees is 7 to 21 for the J and M1-N rotations, inside 5.4 to 22, but 23 to 25 for PMd-N (10 of 14 in range); the data's angles exceed the half-split noise at all 25 dimensions, more than the count above 45 degrees in 11 of 14 rotations (the PMd-N rotations with 25 are equal).",
"rotation-orientation-dimensionality": "**Result: not reproduced.** The rotations need 3 to 24 PCs for 80% of their variance (reading a; 3 to 22 for reading b) and have participation ratios of 2.3 to 19.6, so 3 of 14 and 2 of 14 rotations are in 20.7 to 44 and 15.03 to 40.48. The SNR dimensionality (5 to 19) is in 6.3 to 36.3 for 13 of 14.",
"suppfig6b-location-dimensionality": "**Result: not reproduced.** The location has 1 or 2 excursion angles above 15 degrees (3.6 to 5.5 expected), needs 3 to 15 PCs for 80% (18.9 to 33) and has participation ratios of 2.3 to 7.4 (13.59 to 29.04); its SNR dimensionality (2 to 9) is in 4.5 to 13.2 for 3 of 4 datasets.",
}
R2 = {
"fig5c-rotations-predict-rotations": "**Result: reproduced.** Over the 36 ordered pairs of different rotations, the mean variance explained is 40.9% to 90.5%, all inside 38.7 to 100%, and every pair is above its null with signed-rank p < 0.001. The means are stable under the other four seeds.",
"fig6b-location-predicts-rotations": "**Result: reproduced.** The location predicts 71.0%, 70.0%, 83.0% and 65.4% of the population variance (inside 60.3 to 88%) against a null of 29.2% to 44.8% (signed-rank p below 1e-11). The code's variant gives 78.0% to 87.9%.",
"fig6c-location-tracks-direction": "**Result: reproduced.** The angle of each condition in the plane of the first two PCs of the location follows the target angle, with circular correlation 0.657, 0.719 and 0.630 after mirroring for M1-J, PMd-J and M1-N and 0.357 for PMd-N, all with p < 0.001.",
"fig6e-kinematics-predict-location": "**Result: partially reproduced.** With the reading that fits best (Ornstein-Uhlenbeck kernel, either kinematic basis) the linear model explains 53.7%, 48.1%, 65.7% and 23.9% of the location (3 of 4 in 33.3 to 78.1%) and the kernel model 69.5%, 53.7%, 85.4% and 43.9% (2 of 4 in 62.1 to 89.1%); all are above all 1000 permutations. The Gaussian kernel gives 23.5% to 59.8% (0 of 4).",
"fig7c-ldr-encoding": "**Result: reproduced.** Linear LDR encoding explains 77.1%, 68.9%, 85.4% and 74.0% (inside 54 to 85.8%) and kernel encoding 84.7%, 86.5%, 92.9% and 88.0% (inside 63.9 to 95.7%), against nulls of 42.2% to 62.7%, with signed-rank p below 1e-12, under both kinematic bases and the other seeds.",
"suppfig7a-not-memorization": "**Result: reproduced.** With sextants held out, kernel encoding (78.2% to 88.8%) beats nearest-neighbour regression (70.5% to 82.4%) in every dataset under both kinematic bases, with p from 1.6e-10 to 1.5e-4.",
"fig7c-standard-encoding-worse": "**Result: reproduced.** In all 24 comparisons (two LDR models, three standard models, four datasets) the LDR model is higher with p < 0.001; the standard models explain 18.6% to 72.4% and the LDR models 68.9% to 92.9%.",
"fig7f-ldr-decoding": "**Result: reproduced.** Decoding hand position from single-trial spikes explains on average 88.9%, 88.9%, 93.3% and 89.6% of its variance over trials (reading svd; 88.4% to 92.8% for skewnormal), inside 75.6 to 100%, against 5.4% to 10.5% with the training conditions shuffled; stable over the other seeds (87.2% to 94.5%).",
"trial-curvature-decoding": "**Result: partially reproduced.** Under the svd basis seven of the eight curvature correlations lie in 0.144 to 0.451 with p < 0.001 (0.193 to 0.442); the y curvature of PMd-J gives 0.092 (p = 2.2e-4). Under the skew-normal basis six of eight do.",
"suppfig8-no-output-potent-dependence": "**Result: not reproduced.** Without EMG, only the hand position and velocity dimensions are removed. Decoding drops by 0.28 to 0.90 points (from 96.5% to 98.4% to 95.7% to 98.0% under svd), a small drop, but the signed-rank test finds it in every dataset (p = 4.5e-10 to 1.1e-05), below the 0.036 of the criterion.",
}
EOF
echo ok; date -u
```

```
ok
Sat Nov 28 00:37:38 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && python3 - <<'EOF'
exec(open('results.py').read())
R["fig2c-condition-lds-variance"]=R["fig2c-condition-lds-variance"].replace(" The choice is the same under the four other seeds, except the LDS score for PMd-N (5 under all four)."," The choice is the same under the four other seeds.")
R["suppfig6c-location-distinct-from-rotations"]=R["suppfig6c-location-distinct-from-rotations"].replace("with p below 1e-300 by both tests","with p printed as 0 by both tests")
R["fig3g-basis-frequencies"]=R["fig3g-basis-frequencies"].replace("only 5 of the 14","only 6 of the 14")
R["fig3a-eigenvalue-clusters"]=R["fig3a-eigenvalue-clusters"].replace("4 of the 10 are within","3 of the 10 are within")
R2["fig7c-ldr-encoding"]=R2["fig7c-ldr-encoding"].replace("with signed-rank p below 1e-12","with signed-rank p < 0.0001")
R2["fig7f-ldr-decoding"]=R2["fig7f-ldr-decoding"].replace("(87.2% to 94.5%)","(86.7% to 94.5%)")
R2["suppfig7a-not-memorization"]=R2["suppfig7a-not-memorization"].replace("with p from 1.6e-10 to 1.5e-4","with p from 3.4e-12 to 1.5e-4")
R2["suppfig8-no-output-potent-dependence"]=R2["suppfig8-no-output-potent-dependence"].replace("(from 96.5% to 98.4% to 95.7% to 98.0% under svd)","(from 96.5% to 98.4% with them to 95.7% to 98.0% without, under svd)")
import json
OUT={**{k:'partially' for k in []}}
def outcome(t): 
    return t.split('**Result: ')[1].split('.**')[0]
FAIL="A failure to reproduce here may be a failure of this attempt, not of the paper: see the reasoning and the differences from the paper's method."
DIFF1="""
**How the analysis differs from the paper's.** The units are the dataset's unsorted threshold crossings (96 per array), not the paper's sorted single and multi-units. Trials are all successful trials of the 72 conditions, aligned on the file's `move_begins_time` (an assumption). jPCA is implemented from its description, as its codepack is not in the paper's repository. The LDS dimensionality is scored as the Methods describe (projection) and by the LDS fit, since the code's score does not depend on k. For time: the code's 3/4 split runs 20 folds, the eigenvalue nulls run 150 (halves) and 30 (Poisson) repeats where the Methods use 500, the seed checks of heavy steps use fewer folds or repeats, and the noise for the excursion angles uses 36 half-splits (72 estimates) where the code uses 200.

**What was found about the dataset.** Conditions and trial counts match the paper (72 conditions; 1595 and 2121 successful trials). The units are unsorted threshold crossings, so the paper's unit counts and its unit selection cannot be checked. The trial table, spikes and hand share a clock (direction decoding 0.80 to 0.92 after onset against 0.20 to 0.23 with shuffled labels; peak hand speed 120 to 140 ms after onset). No two of the ten sessions share trial and spike counts. Two Nitschke sessions (2010-09-20 and 2010-09-22) have no `maze_condition` column.
"""
DIFF2="""
**How the analysis differs from the paper's.** The units are unsorted threshold crossings; hand positions are taken relative to each trial's start (an assumption; the code regresses positions on the basis without an intercept); the kinematic basis is computed from the two sessions here; the decoder comparison of Figure 7f is not run; Supplementary Figure 8 removes only kinematic dimensions, as the dataset has no EMG.
"""
for fn,RR,diff in [('reproduce_sabatini_2024.ipynb',R,DIFF1),('reproduce_sabatini_2024_kinematics.ipynb',R2,DIFF2)]:
    p='entries/sabatini-2024/'+fn
    nb=json.load(open(p)); cells=nb['cells']; new=[]
    last={}
    for i,c in enumerate(cells):
        for t in c.get('metadata',{}).get('tags',[]):
            if t.startswith('claim:'): last[t[6:]]=i
    for i,c in enumerate(cells):
        if c['cell_type']=='markdown' and ''.join(c['source']).startswith('## Summary'):
            continue
        new.append(c)
        for cid,j in last.items():
            if j==i and cid in RR:
                new.append({'cell_type':'markdown','metadata':{},'source':RR[cid].splitlines(True)})
    rows="| claim | outcome |\n|---|---|\n"+"".join(f"| {k} | {outcome(v)} |\n" for k,v in RR.items())
    if fn.endswith('kinematics.ipynb'): rows+="| fig7f-decoder-beats-standard | blocked (too large) |\n"
    summ="## Summary\n\n"+rows+"\n"+FAIL+"\n"+diff
    # insert summary before final code cell
    new.insert(len(new)-1,{'cell_type':'markdown','metadata':{},'source':summ.splitlines(True)})
    nb['cells']=new
    json.dump(nb,open(p,'w'),indent=1)
    print(fn, len(new), [k for k in RR if k not in last])
json.dump({'R':R,'R2':R2},open('/tmp/claude-1001/w/res.json','w'))
EOF
cd  && python tools/entry.py check entries/sabatini-2024 2>&1 | tail -3; date -u
```

```
reproduce_sabatini_2024.ipynb 87 []
reproduce_sabatini_2024_kinematics.ipynb 43 []
/opt/hostedtoolcache/Python/3.13.18/x64/lib/python3.13/site-packages/nbformat/validator.py:434: MissingIDFieldWarning: Cell is missing an id field, this will become a hard error in future nbformat versions. You may want to use `normalize()` on your notebooks before validations (available since nbformat 5.1.4). Previous versions of nbformat are fixing this issue transparently, and will stop doing so in the future.
  _validate(nbdict, ref, version, version_minor, relax_add_props)
0 error(s)
Sat Nov 28 00:38:20 UTC 2026
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && python3 - <<'EOF'
import json,uuid
for fn in ['reproduce_sabatini_2024.ipynb','reproduce_sabatini_2024_kinematics.ipynb']:
    nb=json.load(open(fn)); nb['nbformat']=4; nb['nbformat_minor']=5
    for i,c in enumerate(nb['cells']):
        c['id']=f"c{i:03d}"
        if c['cell_type']=='code': c['outputs']=[]; c['execution_count']=None
    json.dump(nb,open(fn,'w'),indent=1)
EOF
cat > README.md <<'EOF'
# Sabatini and Kaufman (2024) on DANDI:000070

Tests the findings of [Sabatini and Kaufman (2024)](https://doi.org/10.1038/s41467-024-51308-7),
"Reach-dependent reorientation of rotational dynamics in motor cortex", on
[DANDI:000070](https://dandiarchive.org/dandiset/000070/0.261122.2046) version 0.261122.2046, using the
two maze sessions the paper names (monkey J 2009-09-18, monkey N 2010-09-23). Four datasets are analysed
separately: M1-J, PMd-J, M1-N, PMd-N.

- `reproduce_sabatini_2024.ipynb`: data check, temporal basis factorization, single-condition dynamics,
  jPCA and the geometry of the rotations.
- `reproduce_sabatini_2024_kinematics.ipynb`: prediction of rotations, LDR encoding and single-trial LDR
  decoding.
- `ldr.py`: loading (streamed from the archive) and the measures, with the source of each parameter.

| Claims | Outcome |
|---|---|
| Factorization variance, shuffle control, recoverability; jPCA variance; single-condition LDS; location distinct from rotations; rotation and location prediction; location tracks direction; LDR encoding, its controls and decoding | Reproduced |
| Data composition; basis frequencies; jPCA R2; plane alignment and its jPCA link; frequency segregation; excursion angles; location alignment; kinematics predict location; curvature decoding | Partially reproduced |
| Duration warping; single LDS; eigenvalue clusters and distances; eigenvalues from kinematics; model comparison; jPCA variance correlation; orientation and location dimensionality; no output-potent dependence | Not reproduced |
| Decoder comparison of Figure 7f | Blocked: too large |

A failure to reproduce here may be a failure of this attempt, not of the paper: see the
reasoning and the differences from the paper's method.

The record, with the reasons and the differences from the paper's method, is
[`attempts/sabatini-2024-02.yaml`](../../attempts/sabatini-2024-02.yaml). Among other things it reports
that the dandiset's units are unsorted threshold crossings, one per electrode, where the paper analysed
sorted single units and stable multi-units.
EOF
cd  python tools/entry.py check entries/sabatini-2024 2>&1 | tail -2; date -u; timeout 6000 python tools/entry.py all entries/sabatini-2024 --max-minutes 60 2>&1 | tail -5; date -u
```

```
0 error(s)
Sat Nov 28 00:38:42 UTC 2026
Installed kernelspec registry-sabatini-2024 in executed/sabatini-2024/.venv/share/jupyter/kernels/registry-sabatini-2024
0 error(s)
pass  reproduce_sabatini_2024.ipynb  (2187 s)
pass  reproduce_sabatini_2024_kinematics.ipynb  (504 s)
Sat Nov 28 01:23:45 UTC 2026
```

**Agent calls Bash**

```bash
cd  python3 -c "
import json
for f,old in [('reproduce_sabatini_2024.ipynb','/tmp/claude-1001/nb1out.txt')]:
    nb=json.load(open('executed/sabatini-2024/'+f))
    out=''
    for c in nb['cells']:
        if c['cell_type']!='code': continue
        t=c.get('metadata',{}).get('tags',[])
        o=''.join(''.join(x.get('text','')) for x in c.get('outputs',[]) if x.get('name')=='stdout')
        if o: out+='## '+str(t)+'\n'+o[:5000]+'\n'
    open('/tmp/claude-1001/nb1out2.txt','w').write(out)
"; diff <(grep -v "jobs in\|in [0-9]* s\|ran in\|loaded in" $TMPDIR/nb1out.txt) <(grep -v "jobs in\|in [0-9]* s\|ran in\|loaded in" $TMPDIR/nb1out2.txt) | head; echo diffdone
```

```
diffdone
```

**Agent calls Bash**

```bash
mkdir -p $TMPDIR/w && cat > $TMPDIR/w/rec.py <<'EOF'
import json, yaml
res = json.load(open('/tmp/claude-1001/w/res.json'))
R = {**res['R'], **res['R2']}
NB1 = 'reproduce_sabatini_2024.ipynb'; NB2 = 'reproduce_sabatini_2024_kinematics.ipynb'
def oc(cid):
    t = R[cid].split('**Result: ')[1].split('.**')[0].strip()
    return {'reproduced': 'reproduced', 'partially reproduced': 'partially_reproduced', 'not reproduced': 'not_reproduced'}[t]
def body(cid):
    return R[cid].split('.** ', 1)[1]
ONSET = "Trials are aligned on the file's move_begins_time, its movement onset time; the paper says only aligned to movement onset (Methods, Subjects, behavior and data pre-processing). The offline onset in the file is 25 ms (J) and 52 ms (N) earlier in the median. Assumption, as the online onset is the one the file names movement onset."
UNITS = "The units are the dataset's unsorted threshold crossings, all 96 per array, where the paper used sorted single units and stable multi-units (Methods, Subjects, behavior and data pre-processing)."
START = "Hand positions are taken relative to each trial's position at -350 ms before the reach parameters are fitted. The code regresses the positions on the basis without an intercept (predictDataUsingTBFandKinCondStructure.m) and the paper does not say where the origin is; the basis functions start at zero, so the start is subtracted. Assumption."
KIN = "Reach parameters as the least-squares coefficients of the condition's hand path on two kinematic basis functions, the top two velocity singular vectors over all conditions of both sessions integrated to position (reading svd) or their skew-normal fits (reading skewnormal; paper, Methods, Extracting kinematic basis functions); results are shown under both."
TIMEC = "For time, some repetitions are fewer than the paper's or the code's; the notebook says which."
details = {
"data-composition": dict(measured=[72, 1595, 2121], dev=[UNITS + " The dataset marks none as single or multi-unit, so the unit count of the criterion cannot be taken; 96 per array is inside 71 to 130.", "Both trial readings were run (all successful trials; delay above 400 ms) and both match; the measured values are reading (a).", "Condition selection: the maze conditions that are multiples of 3 are exactly the 3-target versions in both sessions (readings a and b agree). Condition 0 (203 and 419 trials) is not a maze condition and is left out."]),
"jpca-fit-r2": dict(dev=["jPCA is implemented from the codepack's published description (6 PCs, its soft normalisation of range plus 10 and mean subtraction, skew-symmetric least squares) because the codepack is not in the paper's repository; the input follows getRotations.m.", "The signed-rank test's pairing is the claims file's reading (per-condition R2 in the top plane, straight against curved conditions paired in code order)."], notes_extra=" Reading (a), the skew-symmetric fit, gives 0.777, 0.544, 0.550 and 0.446 (one of four in range)."),
"jpca-variance-explained": dict(dev=["jPCA implemented from its description (see jpca-fit-r2)."]),
"single-lds-variance": dict(dev=["Both windows of the criterion were run; neither matches."]),
"fig2c-condition-lds-variance": dict(dev=["The Methods describe the dimensionality cross-validation as projecting one partition's average on its top k singular vectors and scoring the other partition (Methods, Fitting dynamics to single conditions); the code's crossValidateDimensionalityConditions.m calls idDynamics, whose returned approximation is the training data itself, so its score does not depend on k. Both the Methods' projection score and a score of the simulated LDS were run; both choose 5 to 7.", "Half-lives above 10 s are capped in the simulated dynamics too (Methods); the code caps only the reported eigenvalues.", "The code's 3/4 split runs 20 folds and the seed check 10 folds per seed, for time."]),
"fig3a-eigenvalue-clusters": dict(dev=["Dimensionality from fig2c under both scores; they differ only for PMd-N (7 and 5) and neither matches."]),
"fig3c-eigenvalue-distance-auc": dict(dev=["The halves null runs 150 repeats per condition and the Poisson null 30, where the Methods and the code use 500, for time; the seed check uses 20 repeats per seed. The AUC changes by at most 0.02 between seeds.", "The Poisson null draws the mean of 20 trials as one Poisson count with 20 times the rate divided by 20, which has the same distribution as averaging 20 Poisson trials."]),
"suppfig2-eigenvalues-from-kinematics": dict(dev=[KIN, START, "The imaginary part of a real eigenvalue has no variance and is left out of the mean R2."], assumed=True),
"fig3g-basis-frequencies": dict(dev=["The visual screen for an unpaired last basis function is replaced by the check for a conjugate partner, as the criterion says; no dataset had an unpaired function."]),
"tbf-variance-explained": dict(dev=[]),
"tbf-shuffle-control": dict(dev=["The same permutation of 1 ms bins is used for every unit of a trial (code scrambleTrials.m permutes the columns of the trial matrix)."]),
"fig3h-recoverability": dict(dev=["Recoverability on the raw SVD basis over the whole window, as quantifyTBFStats.m computes it; on the de-mixed basis it is 95.9% to 98.0%."]),
"fig3i-duration-warping": dict(dev=["Reach duration per condition from the condition-mean hand speed (code warpTrials.m indexes kinematicsCond by condition), the same for all trials of a condition.", "The 250 ms post-reach variant scales the time from the end of the reach to +850 ms into 250 ms; the code for it is not in the repository."]),
"suppfig3-model-comparison": dict(dev=["Cross-validated TBF against in-sample LDS and jPCA (the criterion's main reading); the all in-sample variant is reproduced (TBF 92.3% to 97.1% highest in all four)."]),
"fig4b-plane-alignment": dict(dev=["Noise loadings regressed on the fixed corrected raw basis for two halves of each condition's trials, 36 repeats (Methods); the code's 200 repeats were not run, for time."]),
"fig4c-subspace-excursion-angles": dict(dev=["Noise excursion angles from 36 half-splits per condition (72 estimates) where the code uses 200 (400 estimates), for time; fewer estimates give smaller noise angles, so the comparison with the data is less strict than the code's.", "A dimension counts as above noise when fewer than 5% of conditions have a larger noise angle."]),
"rotation-orientation-dimensionality": dict(dev=["Both PCA inputs of the criterion were run; neither matches."]),
"fig4d-jpca-variance-correlation": dict(dev=["Rotational variance as in the code corrTotalRotationsWithjPCA.m."]),
"fig4f-plane-alignment-explains-jpca": dict(dev=["Alignment of the soft-normalised, mean-subtracted rotational activity with each jPCA plane, as in corrOverlapWithjPCA.m."]),
"fig5a-frequencies-segregated": dict(dev=[]),
"fig5c-rotations-predict-rotations": dict(dev=["The truth for a held-out condition is its own loading columns, projected on the training basis, times the basis (Methods); the code keeps a training condition's loadings in its ground-truth tensor. Pairs involving the offset are shown but not counted, as the claim is about rotations."]),
"suppfig6a-location-alignment": dict(dev=[]),
"suppfig6b-location-dimensionality": dict(dev=[]),
"suppfig6c-location-distinct-from-rotations": dict(dev=[]),
"fig6b-location-predicts-rotations": dict(dev=["The Methods give no intercept; the code's appended row of ones, penalised with the predictors, is used."]),
"fig6c-location-tracks-direction": dict(dev=["Target angle from the direction of the condition-mean hand displacement at +850 ms (code splitTrialsAngles.m uses the end of the path)."]),
"fig6e-kinematics-predict-location": dict(dev=[KIN, START, "Targets are the offset columns of the factorization of all 72 conditions; the regression alone is cross-validated. The paper's code for this regression is not published.", "Variance explained pooled over the held-out conditions' offset columns."], assumed=True),
"fig7c-ldr-encoding": dict(dev=[KIN, START], assumed=True),
"suppfig7a-not-memorization": dict(dev=[KIN, START], assumed=True),
"fig7c-standard-encoding-worse": dict(dev=[START, "Kernel matrices inverted with MATLAB's default pseudo-inverse tolerance, as the code relies on pinv with a near-constant kernel at length scales 10^12 and 10^11.", "The standard models are scored over their lagged windows and the LDR models from -150 ms on, as in the code."], assumed=True),
"fig7f-ldr-decoding": dict(dev=[KIN, START, "Single-trial loadings from 10 ms spike counts centred on the grid times (code rebin)."], assumed=True),
"trial-curvature-decoding": dict(dev=[KIN, START, "The curvature parameters are the x and y coefficients on the second basis function."], assumed=True),
"suppfig8-no-output-potent-dependence": dict(dev=["The dataset has no EMG, so only the hand position and velocity dimensions are removed, as the criterion provides; the outcome rests on that.", "The potent dimensions are also projected out of the held-out conditions' activity, and both decoders use the same two folds.", START], assumed=True),
}
measured = {
"fig3c-eigenvalue-distance-auc": [0.716, 0.670, 0.660, 0.581],
"fig3i-duration-warping": 0.013,
"suppfig2-eigenvalues-from-kinematics": 0.247,
"fig4d-jpca-variance-correlation": 83,
"data-composition": [72, 1595, 2121],
}
outcomes = []
order = [c['id'] for c in yaml.safe_load(open('claims/sabatini-2024.yaml'))['claims']]
nb2claims = set(res['R2'])
for cid in order:
    if cid == 'fig7f-decoder-beats-standard':
        outcomes.append(dict(claim=cid, outcome='blocked', blocked_by='too_large', notebook=NB2,
            notes="Not run. The comparison decoders include Ornstein-Uhlenbeck kernel regression trained on single trials and GPFA followed by kernel decoders. A training half holds about 800 (J) to 1060 (N) trials of 121 bins, about 100,000 samples, so the kernel matrix alone is about 10^10 entries, 80 GB in double precision (20 GB with the code's thinning to every second sample), over the 12 GB the runner allows. GPFA's latent dimensionality and bin size are not given in the paper or its code, and no GPFA implementation is in the entry's environment. The LDR decoder itself is tested under fig7f-ldr-decoding."))
        continue
    d = details[cid]
    o = dict(claim=cid, outcome=oc(cid), notebook=NB2 if cid in nb2claims else NB1, output=f'claim:{cid}')
    if cid in measured: o['measured'] = measured[cid]
    n = body(cid) + d.get('notes_extra', '')
    if cid not in ('data-composition',):
        n += ' Units are unsorted threshold crossings (see data-composition).'
    o['notes'] = n
    dev = list(d['dev']) + [ONSET]
    if cid != 'data-composition': dev.append(UNITS)
    o['deviations'] = dev
    if d.get('assumed'): o['assumed'] = True
    outcomes.append(o)
rec = {
 'schema_version': 3, 'id': 'sabatini-2024-02',
 'datasets': [dict(archive='dandi', id='000070', version='0.261122.2046', doi='10.48324/dandi.000070/0.261122.2046', relation='reuses')],
 'paper': 'doi:10.1038/s41467-024-51308-7', 'date': '2026-11-27', 'entry': 'sabatini-2024',
 'provenance': dict(kind='agent', accountable=dict(name='CatalystNeuro'), agent=dict(harness='Claude Code', model='claude-opus-5-5', protocol='pilot-19'),
                    runner=dict(platform='GitHub Actions', url='https://github.com/encorescience/encore-registry/actions/runs/46074971238')),
 'inputs': [dict(what="The paper's analysis code, read for method details the claims file defers to (no data taken from it).", source='https://github.com/kaufmanlab/LDR-public at commit b65f28d')],
 'outcomes': outcomes,
 'findings': [
  dict(kind='data_missing', about='data', severity='major', notebook=NB1, output='finding-unsorted-units',
       statement="The units are unsorted threshold crossings, one per electrode (96 per array, Blackrock unit code 0, as the units table's description says), where the paper analysed sorted single units and stable multi-units, 79 to 118 per array. The sorting, and so the paper's unit counts and unit selection, are not in the dandiset; every population analysis here runs on the threshold crossings."),
  dict(kind='metadata_insufficient', about='data', severity='minor',
       statement="The trials tables of two Nitschke sessions (2010-09-20 and 2010-09-22) have no maze_condition column, so their trials cannot be grouped by condition from the file. These sessions are not the ones the paper names, and were not analysed."),
  dict(kind='other', about='data', severity='none', notebook=NB1, output='sanity',
       statement="Checks that passed. In both sessions the paper names, 72 conditions split 36 without and 36 with barriers, and the trial counts (1595 and 2121 successful trials) are within 10% of the paper's 1469 and 2014. The trial table, spikes and hand share a clock: the condition-mean hand speed peaks 120 to 140 ms after the table's movement onset, and reach direction decodes from spikes 0 to 300 ms after onset at 0.80 to 0.92 against 0.20 to 0.23 with shuffled labels. Hand positions are in mm with a conversion of 0.001 to meters. No two of the ten sessions share their trial and spike counts."),
  dict(kind='code_mismatch', about='paper',
       statement="In the published code, idDynamics.m returns the training data itself as its approximation (approx(cond).matrix = data(cond).matrix), so crossValidateDimensionalityConditions.m scores every dimensionality the same and cannot choose the 5 to 9 dimensions the paper reports. The Methods describe a different score (projection of one partition on its top k singular vectors, variance explained in the other)."),
  dict(kind='methods_unavailable', about='paper',
       statement="Questions for the authors. (1) Which movement onset were the data aligned on, the online or the offline estimate (they differ by 25 to 52 ms in the median)? (2) Were hand positions taken relative to the start of the reach before the reach parameters were fitted on the kinematic basis without an intercept? (3) Which version and parameters of the jPCA codepack were used (getRotations.m calls jPCA with defaults on data already soft-normalised)? This attempt assumed the online onset, start-relative positions and the codepack's defaults; the kinematic claims and fig7c-standard-encoding-worse are marked as resting on the second assumption."),
  dict(kind='methods_unavailable', about='paper',
       statement="The code for kinFuncEval (the kinematic basis functions), the regression of the state space location on the reach parameters (Figure 6e), GPFA and the 250 ms post-reach warp is not in the repository, and the preprocessed .mat files it loads are available only on request, so the order and selection of the 72 conditions and the units cannot be checked against the code."),
 ],
}
open('attempts/sabatini-2024-02.yaml','w').write(
  "# Attempt on Sabatini and Kaufman (2024) with DANDI:000070 version 0.261122.2046 (docs/protocol.md).\n" +
  yaml.safe_dump(rec, sort_keys=False, allow_unicode=True, width=100))
print(len(outcomes))
EOF
. $TMPDIR/env/bin/activate; uv pip install -q pyyaml 2>/dev/null; python $TMPDIR/w/rec.py && cd  && python tools/entry.py check entries/sabatini-2024 2>&1 | tail -8; date -u
```

```
34
0 error(s)
Sat Nov 28 01:24:56 UTC 2026
```

**Agent calls Bash**

```bash
cd $TMPDIR/w && python3 - <<'EOF'
s=open('rec.py').read()
extra_notes = {
"fig3g-basis-frequencies": " The chosen k is the same under all five seeds (7, 7, 9, 9).",
"fig3h-recoverability": " Over the five seeds the chance recoverability is 84.1% to 87.8%.",
"fig3i-duration-warping": " Over the five seeds the warped correlations move by at most 0.004.",
"fig6b-location-predicts-rotations": " Over the other four seeds the means are 64.0% to 83.2%.",
"fig6e-kinematics-predict-location": " Over the other four seeds the OU kernel gives 40.5% to 83.4% and the linear model 19.5% to 65.2%, the same datasets inside and outside the ranges.",
"tbf-shuffle-control": " Over the five seeds the shuffled means are 35.0% to 45.7%.",
}
noseed = ["fig4c-subspace-excursion-angles","suppfig6a-location-alignment","rotation-orientation-dimensionality","suppfig6b-location-dimensionality","fig7c-standard-encoding-worse","trial-curvature-decoding","suppfig8-no-output-potent-dependence"]
s=s.replace("    n = body(cid) + d.get('notes_extra', '')","    n = body(cid) + d.get('notes_extra', '') + EXTRA.get(cid, '')")
s=s.replace("    dev = list(d['dev']) + [ONSET]","    dev = list(d['dev']) + [ONSET]\n    if cid in NOSEED: dev.append('The result depends on random draws, but only the claim\\'s seed was run (the four further seeds of the protocol were not, for time).')")
s=s.replace("outcomes = []\n","EXTRA = %r\nNOSEED = %r\noutcomes = []\n" % (extra_notes, noseed),1)
open('rec.py','w').write(s)
EOF
. $TMPDIR/env/bin/activate; python $TMPDIR/w/rec.py; cd  grep -n "—\|rather\|\*\*" attempts/sabatini-2024-02.yaml | head; grep -c "—\| rather " entries/sabatini-2024/*.ipynb entries/sabatini-2024/ldr.py entries/sabatini-2024/README.md; python tools/entry.py check entries/sabatini-2024 2>&1 | tail -3
```

```
34
entries/sabatini-2024/reproduce_sabatini_2024.ipynb:0
entries/sabatini-2024/reproduce_sabatini_2024_kinematics.ipynb:0
entries/sabatini-2024/ldr.py:0
entries/sabatini-2024/README.md:0
0 error(s)
```

**Agent calls Bash**

```bash
cd entries/sabatini-2024 && sed -i 's/\*\*How the analysis differs from the paper'"'"'s.\*\*/How the analysis differs from the paper'"'"'s:/; s/\*\*What was found about the dataset.\*\*/What was found about the dataset:/' reproduce_sabatini_2024.ipynb reproduce_sabatini_2024_kinematics.ipynb && grep -o '\*\*[^*]*\*\*' *.ipynb README.md | grep -v "Result:" | head; cd ../..; python tools/entry.py check entries/sabatini-2024 2>&1 | tail -1; date -u; timeout 4800 python tools/entry.py all entries/sabatini-2024 --max-minutes 60 2>&1 | tail -4; date -u
```

```
reproduce_sabatini_2024.ipynb:**0.261122.2046**
reproduce_sabatini_2024.ipynb:** 2).sum() / ((dz - dz.mean(1, keepdims=True)) **
reproduce_sabatini_2024_kinematics.ipynb:** 2).sum() / ((raw[:, i] - raw[:, i].mean()) **
reproduce_sabatini_2024_kinematics.ipynb:** 2).sum((1, 2)) / ((DS[n][\"kin\"] - DS[n][\"kin\"].mean(1, keepdims=True)) **
reproduce_sabatini_2024_kinematics.ipynb:** 2).sum(-1) / ls **
reproduce_sabatini_2024_kinematics.ipynb:** 2 / (S **
reproduce_sabatini_2024_kinematics.ipynb:** 2).sum() / ((Y - Y.mean(0)) **
0 error(s)
Sat Nov 28 01:25:43 UTC 2026
Installed kernelspec registry-sabatini-2024 in executed/sabatini-2024/.venv/share/jupyter/kernels/registry-sabatini-2024
0 error(s)
pass  reproduce_sabatini_2024.ipynb  (2205 s)
pass  reproduce_sabatini_2024_kinematics.ipynb  (503 s)
Sat Nov 28 02:11:03 UTC 2026
```

**Agent calls Bash**

```bash
cd  python tools/entry.py handover entries/sabatini-2024 2>&1 | tail -5; ls executed/sabatini-2024/handover/; python tools/entry.py check entries/sabatini-2024 2>&1 | tail -1; python tools/claims_check.py claims/sabatini-2024.yaml 2>&1 | tail -2; date -u
```

```
wrote executed/sabatini-2024/handover
ldr.py
reproduce_sabatini_2024.ipynb
reproduce_sabatini_2024_kinematics.ipynb
sabatini-2024.yaml
0 error(s)
confirmed by reading. Exits non-zero on any problem.

Sat Nov 28 02:11:44 UTC 2026
```

**Agent**

I finished steps 1 to 5 and the handover (step 6). The entry is at `entries/sabatini-2024` and the record at `attempts/sabatini-2024-02.yaml`. Both notebooks ran clean through `entry.py all`, and `check` reports 0 errors. One thing is left undone: the notebook 1 header puts the version number in bold, which your rules don't allow. I saw it at 02:11, too late for another 46-minute run, so the next revision needs to remove it.

**(1) Outcomes** (34 claims: 13 reproduced, 10 partially reproduced, 10 not reproduced, 1 blocked)

| Outcome | Claims |
|---|---|
| reproduced | tbf-variance-explained, tbf-shuffle-control, fig3h-recoverability, jpca-variance-explained, fig2c-condition-lds-variance, suppfig6c-location-distinct-from-rotations, fig5c-rotations-predict-rotations, fig6b-location-predicts-rotations, fig6c-location-tracks-direction, fig7c-ldr-encoding, suppfig7a-not-memorization, fig7c-standard-encoding-worse, fig7f-ldr-decoding |
| partially reproduced | data-composition, fig3g-basis-frequencies, jpca-fit-r2, fig4b-plane-alignment, suppfig6a-location-alignment, fig5a-frequencies-segregated, fig4c-subspace-excursion-angles, fig4f-plane-alignment-explains-jpca, fig6e-kinematics-predict-location, trial-curvature-decoding |
| not reproduced | fig3i-duration-warping, single-lds-variance, fig3a-eigenvalue-clusters, fig3c-eigenvalue-distance-auc, suppfig2-eigenvalues-from-kinematics, suppfig3-model-comparison, fig4d-jpca-variance-correlation, rotation-orientation-dimensionality, suppfig6b-location-dimensionality, suppfig8-no-output-potent-dependence |
| blocked (too_large) | fig7f-decoder-beats-standard: single-trial kernel decoders need about 10^10 kernel entries (80 GB), and the paper gives no GPFA settings |

**(2) The dataset, assumptions and questions**
- **Version:** I pinned 0.261122.2046. The paper cites no version, and the two sessions it names are in that version.
- **Matches the paper:** 72 conditions (36 straight, 36 curved). Trial counts are within 10%: monkey J has 1595 successful trials (paper 1469), monkey N has 2121 (paper 2014).
- **Units (major finding):** the units are unsorted threshold crossings, 96 per array. The paper used sorted single and multi-units (79 to 118 per array), and that sorting is not in the dandiset.
- **Missing column (minor):** two Nitschke sessions not used by the paper (2010-09-20 and 2010-09-22) have no `maze_condition` column.
- **Checks that passed:** trials, spikes and hand share one clock, and no session is deposited twice.
- **Paper findings:** the published code's dimensionality cross-validation can't choose k, because `idDynamics.m` returns the training data as its approximation. Several code pieces are also missing from the repository (the kinematic basis, the Figure 6e regression, GPFA, the 250 ms warp).
- **Assumptions:**
  - Trials are aligned on `move_begins_time`.
  - Hand positions are taken relative to the start of the reach (marked `assumed` on the kinematic claims).
  - jPCA is written from the codepack's published description, because the codepack is not in the paper's repository.
- **Questions for the paper's authors:** which movement onset they used, whether positions were start-relative, and which jPCA version and parameters.
- **Questions to a reader:** none.

**(3) Protocol points**
1. The rule that every random result runs under five seeds conflicts with the 60-minute notebook limit for heavy resampling. I used fewer folds or repeats for the extra seeds, and skipped the extra seeds on 7 claims; each case is recorded as a deviation.
2. Three steps ran with fewer repeats than the Methods or the code for time, each recorded as a deviation: the eigenvalue nulls (150 and 30 repeats instead of 500), the noise for the excursion angles (36 half-splits instead of 200), and the code's 3/4 split (20 folds).
3. When the Methods and the code describe different procedures and the code is broken (the dimensionality cross-validation), the protocol says nothing about what to do. I ran both the Methods' score and a working LDS score; they agree.
4. Any edit to the entry, even to markdown, forces a full re-run. With conclusions written after the run, that cost two extra 46-minute runs.
5. It is unclear whether a finding's `output` can point at a tag that several cells share. My "checks passed" finding points at `sanity`.

**(4) Runtime and failures**
- Notebook 1 takes 37 minutes and notebook 2 takes 8.4, with peak memory 3.4 GB.
- An early development run that used a fork-based multiprocessing pool hung, and its 50-minute timeout killed it. I removed the pool and ran everything serially.
- The first full run failed on the two sessions without `maze_condition`; I fixed that and the re-run passed.

**Accidental exposure:** the version's DANDI release notes, which I read as dataset metadata, list conversion fixes linked to shenoy-lab-to-nwb issues #9 to #13. These may come from earlier attempts. I did not open the issues, and I saw no earlier results.

## End of run

68 turns, 239 minutes, $8.83 at API prices, result: success.
